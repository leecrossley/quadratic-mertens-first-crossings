#!/bin/sh
set -eu

cd "$(dirname "$0")"
if command -v sha256sum >/dev/null 2>&1; then
    sha256sum -c SHA256SUMS
else
    shasum -a 256 -c SHA256SUMS
fi

run_output=$(mktemp)
trap 'rm -f "$run_output"' EXIT
python_bin=${PYTHON:-python3}
"$python_bin" -B verify.py > "$run_output"
"$python_bin" -B family_bound.py >> "$run_output"
"$python_bin" -B independent.py >> "$run_output"
diff -u evidence/check.txt "$run_output"
cat "$run_output"
