#!/usr/bin/env bash
# render_tikz.sh — compile standalone TikZ figures to PDF.
#
# For every .tex file in book/figures/tikz/:
#   1. Compile with lualatex (same engine as the book)
#   2. Copy the output PDF to book/figures/generated/
#
# Usage: scripts/render_tikz.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# Language switch: vi (default) uses book/figures; en uses book-en/figures.
LANG="${LANG:-vi}"
if [ "$LANG" = "en" ]; then
  BOOK_DIR="$ROOT/book-en"
else
  BOOK_DIR="$ROOT/book"
fi
SRCDIR="$BOOK_DIR/figures/tikz"
OUTDIR="$BOOK_DIR/figures/generated"
TMPDIR="$ROOT/build/tikz-tmp"
mkdir -p "$OUTDIR" "$TMPDIR"

if [ ! -d "$SRCDIR" ] || [ -z "$(ls -A "$SRCDIR"/*.tex 2>/dev/null)" ]; then
  echo "render_tikz: no .tex files in $SRCDIR"
  exit 0
fi

count=0
for src in "$SRCDIR"/*.tex; do
  stem="$(basename "$src" .tex)"
  pdf_out="$OUTDIR/${stem}.pdf"

  # Always recompile: figures may depend on shared fonts/packages that
  # change independently of the .tex source. Compilation cost is low (~2s/figure).

  echo "render_tikz: compiling $stem.tex"
  # Compile in tmp dir to avoid cluttering source dir with aux files
  cp "$src" "$TMPDIR/${stem}.tex"
  (cd "$TMPDIR" && lualatex -interaction=nonstopmode "${stem}.tex" > "${stem}.log" 2>&1) || {
    echo "render_tikz: FAILED $stem.tex — see $TMPDIR/${stem}.log" >&2
    cat "$TMPDIR/${stem}.log" | tail -20 >&2
    exit 1
  }

  if [ ! -f "$TMPDIR/${stem}.pdf" ]; then
    echo "render_tikz: FAILED $stem.tex — no PDF produced" >&2
    exit 1
  fi

  cp "$TMPDIR/${stem}.pdf" "$pdf_out"
  count=$((count + 1))
done

echo "render_tikz: done ($count figures compiled to $OUTDIR)"
