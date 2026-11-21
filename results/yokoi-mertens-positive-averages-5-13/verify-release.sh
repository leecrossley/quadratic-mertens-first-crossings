#!/bin/sh
set -eu
cd "$(dirname "$0")"
if command -v sha256sum >/dev/null 2>&1; then
    sha256sum -c SHA256SUMS
else
    shasum -a 256 -c SHA256SUMS
fi
output=$(mktemp)
trap 'rm -f "$output"' EXIT
"${PYTHON:-python3}" -B verify.py > "$output"
"${PYTHON:-python3}" -B independent.py >> "$output"
diff -u evidence/check.txt "$output"
cat "$output"
