#!/usr/bin/env python3
"""Prepend a dated entry to data/announcements.json.

Usage:
  python3 tools/add_announcement.py --date 2026-11-18 --kind added \
      --title "Provider X joins the index" \
      --summary "One sentence on what the user gets." \
      --providers xkiro,cheapllm-shop \
      --details "Bullet one;Bullet two"

Kinds: added, pruned, corrected, audit, changed, update.
The file is validated after writing: unique ids, known kind, ISO date, and every
provider id must exist as data/<id>.json (a warning, not an error, when it does
not — a provider may be announced in the same pass that creates it).
"""

import argparse
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(os.path.dirname(HERE), "data")
PATH = os.path.join(DATA, "announcements.json")
KINDS = {"added", "pruned", "corrected", "audit", "changed", "update"}


def load():
    with open(PATH, encoding="utf-8") as fh:
        return json.load(fh)


def validate(doc):
    problems = []
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", doc.get("updated", "")):
        problems.append("updated must be an ISO date")
    seen = set()
    for it in doc.get("items", []):
        iid = it.get("id")
        if not iid:
            problems.append("item without id")
        elif iid in seen:
            problems.append("duplicate id: " + iid)
        seen.add(iid)
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", it.get("date", "")):
            problems.append(iid + ": date must be an ISO date")
        if it.get("kind") not in KINDS:
            problems.append(iid + ": unknown kind " + str(it.get("kind")))
        for key in ("title", "summary"):
            if not str(it.get(key, "")).strip():
                problems.append(iid + ": missing " + key)
        if len(str(it.get("title", ""))) > 120:
            problems.append(iid + ": title longer than 120 characters")
    for it in doc.get("items", []):
        for pid in it.get("providers", []):
            if not os.path.exists(os.path.join(DATA, pid + ".json")):
                print("warning: " + it.get("id", "?") + " references unknown provider " + pid, file=sys.stderr)
    return problems


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:48] or "entry"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--kind", default="update", choices=sorted(KINDS))
    ap.add_argument("--title", required=True)
    ap.add_argument("--summary", required=True)
    ap.add_argument("--providers", default="")
    ap.add_argument("--details", default="")
    ap.add_argument("--id", dest="entry_id")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    doc = load()
    entry = {
        "id": args.entry_id or (args.date + "-" + slug(args.title)),
        "date": args.date,
        "kind": args.kind,
        "title": args.title.strip(),
        "summary": args.summary.strip(),
        "providers": [p.strip() for p in args.providers.split(",") if p.strip()],
        "details": [d.strip() for d in args.details.split(";") if d.strip()],
    }
    doc["items"] = [entry] + [it for it in doc["items"] if it.get("id") != entry["id"]]
    doc["items"].sort(key=lambda it: it.get("date", ""), reverse=True)
    doc["updated"] = max([doc.get("updated", ""), args.date])

    problems = validate(doc)
    if problems:
        print("\n".join("error: " + p for p in problems), file=sys.stderr)
        raise SystemExit(1)

    if args.dry_run:
        print(json.dumps(entry, indent=2, ensure_ascii=False))
        return
    with open(PATH, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print("announcements:", len(doc["items"]), "updated:", doc["updated"])


if __name__ == "__main__":
    main()
