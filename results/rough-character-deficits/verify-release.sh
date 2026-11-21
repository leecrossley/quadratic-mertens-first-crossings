#!/bin/sh
set -eu
cd "$(dirname "$0")"
if command -v sha256sum >/dev/null 2>&1; then
    sha256sum -c SHA256SUMS
else
    shasum -a 256 -c SHA256SUMS
fi
result=$(mktemp)
binary=$(mktemp)
trap 'rm -f "$result" "$binary"' EXIT
"${PYTHON:-python3}" -B scripts/verify.py > "$result"
"${PYTHON:-python3}" -B scripts/independent.py >> "$result"
diff -u evidence/check.txt "$result"
cat "$result"
"${PYTHON:-python3}" -B scripts/sieve_choice.py > "$result"
"${PYTHON:-python3}" -B scripts/sieve_independent.py >> "$result"
"${PYTHON:-python3}" -B scripts/long_recovery.py >> "$result"
"${CXX:-c++}" -std=c++20 -O3 scripts/long_recovery.cc -o "$binary"
"$binary" >> "$result"
diff -u evidence/sieve-choice.txt "$result"
cat "$result"
