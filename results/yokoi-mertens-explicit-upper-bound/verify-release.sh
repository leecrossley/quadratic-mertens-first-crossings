#!/bin/sh
set -eu
cd "$(dirname "$0")"
if command -v sha256sum >/dev/null 2>&1; then
    sha256sum -c SHA256SUMS
else
    shasum -a 256 -c SHA256SUMS
fi
tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT
export PYTHONDONTWRITEBYTECODE=1
python3 check.py > "$tmp"
diff -u evidence/check.txt "$tmp"
cat "$tmp"
