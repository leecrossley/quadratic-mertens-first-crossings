#!/bin/sh
set -eu
if [ "$#" -gt 1 ]; then
    echo "Usage: $0 [pinned-mathlib-directory]" >&2
    exit 2
fi
if [ "$#" -eq 1 ]; then
    mathlib=$(CDPATH= cd -- "$1" && pwd)
fi
cd "$(dirname "$0")"
repo=$(pwd)
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

if [ "$#" -eq 1 ]; then
    build=$(mktemp -d)
    trap 'rm -f "$tmp"; rm -rf "$build"' EXIT
    cd "$mathlib"
    test -f Mathlib.lean
    test "$(git rev-parse HEAD)" = 0df444a360eaa60ab8c11dca51a86af692955474
    case "$(lake env lean --version)" in
        *819816b2e0a3bf405af45ae5c7af2491d8f5bee6*) ;;
        *) echo "Expected the pinned Lean 4.33.1 compiler." >&2; exit 1 ;;
    esac
    lake env lean -DwarningAsError=true -R "$repo" -o "$build/ConductorBound.olean" "$repo/ConductorBound.lean" > "$build/axioms.txt"
    diff -u "$repo/evidence/lean.txt" "$build/axioms.txt"
    lake env sh -c 'export LEAN_PATH="$1:$LEAN_PATH"; exec leanchecker -v ConductorBound' sh "$build"
fi
