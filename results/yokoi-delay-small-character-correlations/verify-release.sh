#!/bin/sh
set -eu
cd "$(dirname "$0")"
if command -v sha256sum >/dev/null 2>&1; then
    sha256sum -c SHA256SUMS
else
    shasum -a 256 -c SHA256SUMS
fi
result=$(mktemp)
trap 'rm -f "$result"' EXIT
"${PYTHON:-python3}" -B scripts/verify.py > "$result"
"${PYTHON:-python3}" -B scripts/independent.py >> "$result"
diff -u evidence/check.txt "$result"
cat "$result"
