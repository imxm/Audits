#!/usr/bin/env python3
"""Build data/reports.json from the analyzer output over a local clone of
oak-security/audit-reports. Run: python3 tools/make_data.py <analyze-output.json>"""
import json, os, sys, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from protocols import PROTOCOLS

BASE = "https://github.com/oak-security/audit-reports/blob/main/"


def url_for(path):
    return BASE + urllib.parse.quote(path)


def main(src):
    raw = {x["file"]: x for x in json.load(open(src))}
    out, missing = {}, []
    for p in PROTOCOLS:
        for rel in p["reports"]:
            r = raw.get(rel)
            if r is None:
                missing.append(rel)
                continue
            out[rel] = {
                "protocol": p["slug"],
                "client": rel.split("/")[0],
                "title": rel.split("/")[-1].rsplit(".pdf", 1)[0],
                "date": r["date"],
                "url": url_for(rel),
                "counts": r["counts"],
                "total": r["total"],
                "scope": r["scope"],
                "findings": [f for f in r["findings"]],
            }
    if missing:
        print("MISSING from the Oak clone:", *missing, sep="\n  ", file=sys.stderr)
        sys.exit(1)
    dest = os.path.join(HERE, "..", "data", "reports.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print(f"wrote {len(out)} reports -> data/reports.json")


if __name__ == "__main__":
    main(sys.argv[1])
