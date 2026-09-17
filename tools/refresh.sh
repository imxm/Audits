#!/usr/bin/env bash
# Regenerate data/reports.json, README.md and protocols/*.md from the published PDFs.
#
#   ./tools/refresh.sh            # uses ./audit-reports (cloned on first run)
#   OAK_WORKDIR=/tmp/oak ./tools/refresh.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${OAK_WORKDIR:-$ROOT}"
REPO="$WORK/audit-reports"
TEXT="$WORK/text"

command -v node >/dev/null || { echo "node is required (pdf-parse)"; exit 1; }

[ -d "$REPO" ] || git clone --depth 1 https://github.com/oak-security/audit-reports.git "$REPO"
[ -d "$ROOT/tools/node_modules/pdf-parse" ] || (cd "$ROOT/tools" && npm install --silent pdf-parse)

mkdir -p "$TEXT"
cd "$REPO"
find . -iname '*.pdf' -print0 | xargs -0 -P 6 -I{} bash -c '
  f="${1#./}"
  out="$2/$(echo "$f" | tr "/" "@").txt"
  [ -s "$out" ] || node "$3/tools/pdftxt.js" "$4/$f" > "$out"
' _ {} "$TEXT" "$ROOT" "$REPO"

cd "$ROOT"
OAK_WORKDIR="$WORK" python3 tools/analyze.py > "$WORK/all.json"
python3 tools/make_data.py "$WORK/all.json"
python3 tools/build.py
