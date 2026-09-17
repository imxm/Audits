#!/usr/bin/env python3
"""Parse Oak Security audit reports into structured findings data.

Reads the extracted text of each report (see pdftxt.js) from $OAK_WORKDIR/text and
emits JSON on stdout: per report, the severity counts and every finding's number,
title, severity and status, taken from the report's own Detailed Findings section.
"""
import json, os, re, sys

SD = os.environ.get("OAK_WORKDIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
TXT = os.path.join(SD, "text")
SEV = ("Critical", "Major", "Minor", "Informational")

def clean(s):
    s = s.replace(" ", " ")
    s = re.sub(r"\s*\n\s*", " ", s)
    s = re.sub(r"\s*\t\s*", " ", s)
    s = re.sub(r"\s{2,}", " ", s)
    return s.strip()

def analyze(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    # strip page markers / page numbers
    body = re.sub(r"\n-- \d+ of \d+ --\n", "\n", raw)
    body = re.sub(r"(?m)^\d{1,3}\s*$\n", "", body)

    # detailed findings section = from the LAST standalone "Detailed Findings" heading
    idxs = [m.start() for m in re.finditer(r"(?m)^Detailed Findings\s*$", body)]
    sec = body[idxs[-1]:] if idxs else body

    findings = []
    marker = re.compile(r"(?m)^[ \t]*Severity:[ \t]*(Critical|Major|Minor|Informational)\b")
    num = re.compile(r"(?:(?<=\n)|(?<=\s)|^)(\d{1,3})[.\u2024]\s*")
    for m in marker.finditer(sec):
        before = sec[max(0, m.start() - 600):m.start()]
        # the heading always follows the previous finding's Status line
        prev = list(re.finditer(r"(?m)^\s*Status:\s*[A-Za-z ]+$", before))
        if prev:
            before = before[prev[-1].end():]
        before = re.sub(r"(?m)^\s*\d{1,3}\s*$", "", before)  # page numbers
        starts = list(num.finditer(before))
        n, title = None, None
        if starts:
            last = starts[-1]
            n = int(last.group(1))
            title = before[last.end():]
        rest = sec[m.end():m.end() + 8000]
        st = re.search(r"(?m)^\s*Status:\s*([A-Za-z ]+?)\s*$", rest)
        findings.append({
            "n": n,
            "title": clean(title) if title else None,
            "severity": m.group(1),
            "status": clean(st.group(1)) if st else None,
        })

    sev_markers = len(findings)
    counts = {s: sum(1 for f in findings if f["severity"] == s) for s in SEV}
    seq = [f["n"] for f in findings]
    ok = bool(findings) and seq == list(range(1, len(findings) + 1))

    # independent check: summary-of-findings table
    sm = [m.start() for m in re.finditer(r"(?m)^Summary of Findings\s*$", body)]
    summary_counts = None
    if sm:
        end = idxs[-1] if idxs else len(body)
        stab = body[sm[-1]:end]
        pairs = re.findall(r"\b(Critical|Major|Minor|Informational)\b[ \t\n]*(Resolved|Acknowledged|Partially Resolved|Partially resolved|Pending)\b", stab)
        if pairs:
            summary_counts = {s2: sum(1 for a, _ in pairs if a == s2) for s2 in SEV}

    # scope: codebase section
    scope = ""
    cands = list(re.finditer(r"(?m)^\s*Codebase Submitted for the Audit\s*$", body))
    for cm in reversed(cands):
        tail = body[cm.end():cm.end() + 4000]
        end = re.search(r"(?m)^\s*(Methodology|Functionality Overview|Code Quality Criteria)\s*$", tail)
        chunk = tail[:end.start()] if end else tail[:2500]
        if len(clean(chunk)) > 40:
            scope = clean(chunk)
            break

    date = ""
    md = re.search(r"(?m)^\s*((?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4})\s*$", raw[:4000])
    if md:
        date = md.group(1)

    return {
        "file": os.path.basename(path)[:-4].replace("@", "/"),
        "date": date,
        "counts": counts,
        "total": len(findings),
        "severity_markers": sev_markers,
        "ok": ok,
        "summary_counts": summary_counts,
        "agree": summary_counts == counts if summary_counts else None,
        "findings": findings,
        "scope": scope[:1200],
    }

if __name__ == "__main__":
    pats = sys.argv[1:]
    out = []
    for fn in sorted(os.listdir(TXT)):
        if not fn.endswith(".txt"):
            continue
        if pats and not any(p.lower() in fn.lower() for p in pats):
            continue
        out.append(analyze(os.path.join(TXT, fn)))
    json.dump(out, sys.stdout, indent=1)
