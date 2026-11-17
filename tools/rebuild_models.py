#!/usr/bin/env python3
"""Rewrite the `models` array of the data files from the shared catalogue.

Usage: python3 tools/rebuild_models.py [--check]

For every provider listed in tools/provider_models.py, the models array is
replaced by catalogue entries (name, family, context window, Artificial
Analysis intelligence, curated TPS). The rest of the provider file is untouched.
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models import MODELS  # noqa: E402
from provider_models import PROVIDER_MODELS  # noqa: E402
from speed import tps_for  # noqa: E402

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")


def build_model(mid, rate_limits=None, provider_id=None):
    src = MODELS[mid]
    m = {"id": src["id"], "name": src["name"], "family": src["family"]}
    if src.get("context_window"):
        m["context_window"] = src["context_window"]
    metrics = {}
    tps = tps_for(provider_id, mid, src.get("tps"))
    if tps is not None:
        metrics["tps"] = tps
    if src.get("intelligence") is not None:
        metrics["intelligence"] = src["intelligence"]
    if metrics:
        m["metrics"] = metrics
    if rate_limits:
        m["rate_limits"] = rate_limits
    return m


def main():
    check = "--check" in sys.argv
    unknown = []
    written = 0
    for pid, mids in PROVIDER_MODELS.items():
        path = os.path.join(DATA, pid + ".json")
        if not os.path.exists(path):
            unknown.append("missing provider file: " + pid)
            continue
        d = json.load(open(path, encoding="utf-8"))
        # keep the per-model free-limit wording where we already had it
        old_limits = {m["id"]: m.get("rate_limits") for m in d.get("models", [])}
        default_limit = None
        for m in d.get("models", []):
            if m.get("rate_limits"):
                default_limit = m["rate_limits"]
                break
        models = []
        for mid in mids:
            if mid not in MODELS:
                unknown.append("%s: unknown model id %s" % (pid, mid))
                continue
            models.append(build_model(mid, old_limits.get(mid) or default_limit, pid))
        # preserve account-wide token allowance only when every model shares it
        allowances = {m.get("token_allowance") for m in d.get("models", [])}
        if len(allowances) == 1:
            sole = allowances.pop()
            if isinstance(sole, int):
                for m in models:
                    m["token_allowance"] = sole
        d["models"] = models
        if check:
            continue
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(d, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        written += 1
    print("providers rebuilt:", written)
    for u in unknown:
        print("WARN", u)
    return 1 if unknown else 0


if __name__ == "__main__":
    sys.exit(main())
