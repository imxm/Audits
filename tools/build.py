#!/usr/bin/env python3
"""Regenerate README.md and protocols/*.md from data/reports.json + tools/protocols.py."""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from protocols import CATEGORIES, PROTOCOLS

SEV = ("Critical", "Major", "Minor", "Informational")
DATA = json.load(open(os.path.join(ROOT, "data", "reports.json"), encoding="utf-8"))


def reports_of(p):
    return [DATA[r] for r in p["reports"]]


def totals(p):
    t = {s: 0 for s in SEV}
    for r in reports_of(p):
        for s in SEV:
            t[s] += r["counts"][s]
    t["total"] = sum(r["total"] for r in reports_of(p))
    return t


BOILERPLATE = [
    r"Note that only fixes to the issues described in this report have been reviewed at this commit\.?",
    r"Any further changes,? such as additional features,? have not been reviewed\.?",
    r"The audit has been performed on the following targets?:?",
    r"The scope is restricted to:?",
]


def mend_urls(text):
    """PDF line wrapping splits long URLs. Rejoin only when the break is clearly
    mid-token: the trailing path segment is one or two characters, or ends in '-'."""
    def join(m):
        url, tail = m.group(1), m.group(2)
        last = re.split(r"[/.]", url)[-1]
        if url.endswith("-") or len(last) <= 2:
            return url + tail
        return m.group(0)
    return re.sub(r"(https?://[^\s]+) ([a-z0-9][A-Za-z0-9._~%/-]{0,14})\b", join, text)


def clean_scope(text):
    text = mend_urls(re.sub(r"\s+", " ", text).strip())
    fixes = re.findall(r"Fixes verified at commits? ([0-9a-f]{7,40}(?:[ ,]+[0-9a-f]{7,40})*)", text)
    text = re.sub(r"Fixes verified at commits? [0-9a-f]{7,40}(?:[ ,]+[0-9a-f]{7,40})*\.?", "", text)
    for pat in BOILERPLATE:
        text = re.sub(pat, "", text)
    text = text.replace("Label Paths referencing this target are prefixed below with", "path prefix")
    text = re.sub(r"\bScope:?(?=\s*[●○]|\s*$)", "", text)
    text = re.sub(r"\bRepository (https?://\S+)", r"repository \1", text)
    text = re.sub(r"\bCommit ([0-9a-f]{7,40})", r"commit \1", text)
    text = re.sub(r"\s+Scope:?\s+(?=[A-Za-z])", ". ", text)
    text = re.sub(r"\s{2,}", " ", text).strip(" ;:.")
    text = re.sub(r"^([a-z])", lambda m: m.group(1).upper(), text)
    parts = [p.strip(" ;:.") for p in re.split(r"[●○]", text)]
    head = parts[0].strip()
    bullets = [p for p in parts[1:] if p]
    return head, bullets, fixes[0] if fixes else None


def short(text, limit=320):
    if len(text) <= limit:
        return text
    cut = text[:limit]
    dot = cut.rfind(". ")
    return (cut[: dot + 1] if dot > limit // 2 else cut.rstrip()) + " …"


def title_of(r):
    t = re.sub(r"^\d{4}-\d{2}-\d{2} Audit Report\s*[-–]\s*", "", r["title"])
    t = re.sub(r"\s+v\d+(\.\d+)*$", "", t)
    return t.strip()


def iso(r):
    m = re.match(r"(\d{4}-\d{2}-\d{2})", r["title"])
    return m.group(1) if m else r["date"]


def esc(s):
    return s.replace("|", "\\|")


def findings_cell(p):
    t = totals(p)
    if t["total"] == 0:
        return "—"
    high = []
    if t["Critical"]:
        high.append(f"{t['Critical']} critical")
    if t["Major"]:
        high.append(f"{t['Major']} major")
    return f"{t['total']} ({', '.join(high)})" if high else str(t["total"])


def readme_row(p):
    link = f"[{p['name']}](protocols/{p['slug']}.md)"
    if not p["reports"]:
        note = p.get("counts_note", p.get("unpublished", "Not published"))
        return f"| {link} | {p['stack']} | — | *{note.rstrip('.')}* |"
    extra = " ⁺" if p.get("unpublished") else ""
    return f"| {link} | {p['stack']} | {len(p['reports'])}{extra} | {findings_cell(p)} |"


def build_readme():
    pub_reports = sum(len(p["reports"]) for p in PROTOCOLS)
    grand = {s: sum(totals(p)[s] for p in PROTOCOLS) for s in SEV}
    grand_total = sum(totals(p)["total"] for p in PROTOCOLS)
    oak_prot = len([p for p in PROTOCOLS if not p.get("brand")])
    other_prot = len(PROTOCOLS) - oak_prot
    unpub_reports = sum(p.get("unpublished_reports", 0) for p in PROTOCOLS)

    out = ["# Audits", ""]
    out += [
        "Security engagements where I was lead or a named reviewer, almost all delivered through",
        "[Oak Security](https://oaksecurity.io). Reports are public in Oak's",
        "[audit-reports](https://github.com/oak-security/audit-reports) repository. One row per protocol;",
        "each protocol page lists its reports with scope, notable findings and links.",
        "",
        "## Summary",
        "",
        f"- {oak_prot} protocols audited with Oak: {pub_reports} published reports, "
        f"{grand_total} findings",
        f"- {grand['Critical']} critical, {grand['Major']} major, {grand['Minor']} minor, "
        f"{grand['Informational']} informational",
        f"- A further {unpub_reports} reports are not public, plus {other_prot} engagements "
        "delivered under NDA or another brand",
        "- Stacks: Cosmos SDK and CosmWasm, Stellar Core and Soroban, GnoVM, Solana, NEAR, EVM, "
        "Polkadot bridge, Fuel",
        "- Languages: Go, Rust, Solidity, C++ (read), Noir",
        "",
        "`⁺` in the Reports column means further reports from that engagement are not public; "
        "the counts cover the published ones only.",
        "",
    ]
    for title, key in CATEGORIES:
        rows = [p for p in PROTOCOLS if p["cat"] == key]
        if not rows:
            continue
        out += [f"## {title}", ""]
        out += ["| Protocol | Stack | Reports | Findings |",
                "|---|---|---|---|"]
        out += [readme_row(p) for p in rows]
        out += [""]

    return "\n".join(out)


def build_page(p):
    rs = reports_of(p)
    t = totals(p)
    out = [f"# {p['name']}", ""]
    head = p["stack"]
    if rs:
        head += f" · {len(rs)} published report{'s' if len(rs) > 1 else ''} · {t['total']} findings"
    out += [head, "", p["summary"], "", f"**Role:** {p['role']}", ""]
    if p.get("unpublished"):
        out += [f"> {p['unpublished']}", ""]
    if not rs:
        if p.get("counts_note") and p.get("counts_note") != p.get("unpublished"):
            out += [f"> {p['counts_note']}", ""]
        out += ["No public report to link yet. This page will list scope and findings once the client",
                "publishes, or stay as a record of the engagement if it never does.", ""]
        return "\n".join(out)

    out += ["## Reports", "",
            "| Date | Report | Critical | Major | Minor | Info | Total |",
            "|---|---|---|---|---|---|---|"]
    for r in rs:
        c = r["counts"]
        out.append(
            f"| {r['date']} | [{esc(title_of(r))}]({r['url']}) | {c['Critical']} | {c['Major']} | "
            f"{c['Minor']} | {c['Informational']} | {r['total']} |")
    if len(rs) > 1:
        out.append(f"| **Total** | **{len(rs)} reports** | **{t['Critical']}** | **{t['Major']}** | "
                   f"**{t['Minor']}** | **{t['Informational']}** | **{t['total']}** |")
    out += [""]

    for r in rs:
        c = r["counts"]
        out += [f"## {iso(r)} — {title_of(r)}", "",
                f"[Report PDF]({r['url']}) · {r['date']} · {r['total']} findings "
                f"({c['Critical']} critical, {c['Major']} major, {c['Minor']} minor, "
                f"{c['Informational']} informational)", ""]
        if r["scope"]:
            head, bullets, fixes = clean_scope(r["scope"])
            if head:
                head = short(head)
                out += ["**Scope.** " + head + ("" if head.endswith((".", "…")) else "."), ""]
            for b in bullets[:6]:
                out.append(f"- {short(b, 220)}")
            if len(bullets) > 6:
                out.append(f"- …and {len(bullets) - 6} further scope items.")
            if bullets:
                out += [""]
            if fixes:
                out += [f"Fixes verified at commit `{fixes.split()[0][:12]}`.", ""]
        notable = [f for f in r["findings"] if f["severity"] in ("Critical", "Major") and f["title"]]
        if notable:
            out += ["**Notable findings**", ""]
            for f in notable[:8]:
                status = f" — *{f['status']}*" if f["status"] else ""
                out.append(f"- **{f['severity']}** — {esc(f['title'])}{status}")
            if len(notable) > 8:
                out.append(f"- …and {len(notable) - 8} further critical/major findings in the report.")
            out += [""]
        else:
            out += ["No critical or major findings; the report is minor and informational only.", ""]
    return "\n".join(out)


def main():
    open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8").write(build_readme())
    pdir = os.path.join(ROOT, "protocols")
    os.makedirs(pdir, exist_ok=True)
    for p in PROTOCOLS:
        open(os.path.join(pdir, p["slug"] + ".md"), "w", encoding="utf-8").write(build_page(p))
    print(f"wrote README.md and {len(PROTOCOLS)} protocol pages")


if __name__ == "__main__":
    main()
