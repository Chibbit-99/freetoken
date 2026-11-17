#!/usr/bin/env python3
"""Write the freeinferencing.com additions into data/ and update the manifest.

Usage: python3 tools/add_new_providers.py [--dry-run]
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from models import MODELS  # noqa: E402
from speed import tps_for  # noqa: E402
from new_providers_a import PART_A  # noqa: E402
from new_providers_b import PART_B  # noqa: E402
from new_providers_c import PART_C  # noqa: E402
from new_providers_d import PART_D  # noqa: E402

DATA = os.path.join(os.path.dirname(HERE), "data")
CHECKED = "2026-11-17"
SOURCE_SNAPSHOT = "https://freeinferencing.com/"

OFFER = {
    "af": ("always-free", "emerald"),
    "fm": ("free-models", "blue"),
    "mc": ("monthly-credits", "amber"),
    "rs": ("research", "sky"),
    "tr": ("trials", "amber"),
}
PRIVACY = {"pv": "private", "pp": "partial", "nn": "none", None: "none"}

# Providers whose free offer is not text-model specific still need a model row.
# Providers removed from the catalogue because they are not text-LLM APIs
# (speech, image/video, embeddings) or because the free offer did not hold up.
SKIP = {
    "elevenlabs", "cartesia", "deepgram", "assemblyai", "speechmatics", "palabra",
    "async-voice", "paxa-labs", "lelapa", "viggle", "stability-ai", "wavespeed",
    "inferon", "clarifai", "voyage-ai", "jina-ai", "qdrant-cloud", "mongodb-atlas",
    "vlm-run",
}

MODEL_EXTRA = {
    "inception": {
        "mercury-2": {"token_allowance": 100000000},
    },
}
MERCURY_LIMITS = "100M one-time signup balance shared across Mercury 2/2.5/3; 100 RPM, 100K input TPM, 10K output TPM"

MODEL_FIX = {
    "oracle-oci": ["command-r-plus", "llama-4-maverick", "cohere-embed"],
    "aws-bedrock": ["llama-4-maverick", "mistral-large-4", "command-r-plus"],
    "azure-ai-foundry": ["gpt-oss-120b", "llama-4-maverick", "mistral-small-4"],
    "ramp-router": ["gpt-oss-120b", "qwen3-8-27b", "glm-5-3-flash"],
}


def build_models(ids, provider_id=None):
    out = []
    for mid in ids:
        if isinstance(mid, dict):
            out.append(mid)
            continue
        if mid == "cohere-embed":
            out.append({"id": "cohere-embed-v4", "name": "Embed v4", "family": "Cohere Embed"})
            continue
        if mid not in MODELS:
            raise SystemExit("unknown model id: " + mid)
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
        out.append(m)
    return out


def main():
    dry = "--dry-run" in sys.argv
    manifest_path = os.path.join(DATA, "providers.json")
    manifest = json.load(open(manifest_path, encoding="utf-8"))
    listed = set(manifest["providers"])
    added = []
    for row in PART_A + PART_B + PART_C + PART_D:
        (pid, name, site, offer_code, offer_label, priv_code, priv_label, card,
         desc, overview, bullets, mids, notes) = row[:13]
        if pid in SKIP:
            continue
        models = build_models(MODEL_FIX.get(pid, mids), pid)
        if pid == "inception":
            for m in models:
                m["rate_limits"] = MERCURY_LIMITS
                if m["id"] == "mercury-2":
                    m["token_allowance"] = 100000000
        if not models:
            raise SystemExit("no models for " + pid)
        offer_type, tone = OFFER[offer_code]
        entry = {
            "id": pid,
            "name": name,
            "website": site,
            "docs": site,
            "signup": site,
            "description": desc,
            "overview": overview,
            "offer": {"type": offer_type, "label": offer_label, "tone": tone},
            "privacy": {"type": PRIVACY[priv_code]},
            "requires_payment_card": card,
            "last_updated": CHECKED,
            "verified": {"checked": CHECKED, "sources": [site, SOURCE_SNAPSHOT]},
            "free_access": bullets,
        }
        if priv_label:
            entry["privacy"]["label"] = priv_label
        else:
            entry["privacy"]["label"] = "Privacy not documented"
        if notes:
            entry["notes"] = notes
        entry["models"] = models
        if dry:
            print("would write", pid, len(models), "models")
        else:
            with open(os.path.join(DATA, pid + ".json"), "w", encoding="utf-8") as fh:
                json.dump(entry, fh, indent=2, ensure_ascii=False)
                fh.write("\n")
        if pid + ".json" not in listed:
            manifest["providers"].append(pid + ".json")
            added.append(pid)
    if not dry:
        with open(manifest_path, "w", encoding="utf-8") as fh:
            json.dump(manifest, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
    print("new providers:", len(added), "manifest size:", len(manifest["providers"]))


if __name__ == "__main__":
    main()
