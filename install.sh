#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-$HOME/.codex/skills}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$TARGET"

for dir in skills superpowers system-skills; do
  src_root="$ROOT/$dir"
  [ -d "$src_root" ] || continue

  for src in "$src_root"/*; do
    [ -d "$src" ] || continue
    name="$(basename "$src")"
    dest="$TARGET/$name"
    rm -rf "$dest"
    cp -R "$src" "$dest"
    printf 'Installed %s -> %s\n' "$name" "$dest"
  done
done

printf 'Done. Target: %s\n' "$TARGET"
