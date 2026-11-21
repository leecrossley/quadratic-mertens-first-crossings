#!/bin/sh
set -eu
repo_dir=$(CDPATH= cd -- "$(dirname "$0")" && pwd)
mathlib_dir=${1:?Pass the path to the pinned mathlib4 checkout.}
cd "$mathlib_dir"
test "$(cat lean-toolchain)" = "$(cat "$repo_dir/lean-toolchain")"
result=$(mktemp)
trap 'rm -f "$result"' EXIT
lake env lean "$repo_dir/Packets.lean" > "$result"
diff -u "$repo_dir/evidence/lean.txt" "$result"
cat "$result"
