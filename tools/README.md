# tools

Everything in `README.md` and `protocols/` is generated. Nothing in the severity
tables is typed in by hand, so the numbers can always be re-derived from the
published PDFs.

| File | What it does |
|---|---|
| `pdftxt.js` | Extracts text from one report PDF (`pdf-parse`, i.e. pdf.js). |
| `analyze.py` | Parses each report's **Detailed Findings** section: every finding's number, title, `Severity:` and `Status:`. Severity counts are the number of `Severity:` markers, not an estimate. |
| `protocols.py` | The only hand-maintained file: protocol metadata and which reports belong to which engagement. |
| `make_data.py` | Joins the parsed findings to `protocols.py` and writes `data/reports.json`. |
| `build.py` | Renders `README.md` and `protocols/*.md` from `data/reports.json`. |
| `refresh.sh` | Runs the whole chain, cloning the Oak corpus first if needed. |

## Regenerating

```bash
./tools/refresh.sh
```

Requires `node` (for `pdf-parse`) and `python3`. The clone of
[oak-security/audit-reports](https://github.com/oak-security/audit-reports) and the
extracted text are gitignored; only `data/reports.json` and the generated Markdown
are committed.

## Editing content

Prose (protocol summary, stack, role, unpublished notes) lives in `tools/protocols.py`.
Edit it there and re-run `python3 tools/build.py` — edits made directly to the generated
Markdown are overwritten.

## Cross-checking

`analyze.py` also parses the report's own *Summary of Findings* table and compares it
with the detailed section. Where the two disagree it is the summary-table parse that
drifts, because that table's rows wrap across page breaks; the `Severity:` line under
each finding is authoritative and is what the counts use.
