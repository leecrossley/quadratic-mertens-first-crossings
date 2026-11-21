#!/bin/sh
set -eu

cd "$(dirname "$0")"
if command -v sha256sum >/dev/null 2>&1; then
    sha256sum -c SHA256SUMS
else
    shasum -a 256 -c SHA256SUMS
fi
python_bin=${PYTHON:-python3}
result=$(mktemp)
trap 'rm -f "$result"' EXIT
"$python_bin" -B verify.py > "$result"
diff -u evidence/census.tsv "$result"
"$python_bin" -B independent.py > "$result"
diff -u evidence/census.tsv "$result"
"$python_bin" -B check_identities.py > "$result"
diff -u evidence/check.txt "$result"
cat "$result"
