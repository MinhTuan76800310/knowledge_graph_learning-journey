#!/usr/bin/env bash
# build_book.sh — assemble the Knowledge Graph book PDFs with Pandoc.
#
# Pipeline: manuscript Markdown -> pre-render Mermaid figures (see
# render_mermaid.sh) -> Pandoc + citeproc -> LuaLaTeX -> PDF.
#
# Outputs:
#   dist/knowledge-graph-book-print.pdf   (A4, two-sided, links in black)
#   dist/knowledge-graph-book-screen.pdf  (same layout, clickable colored links)
#
# Print profile: A4, 11pt body, twoside with inner margin > outer margin,
# DejaVu system fonts (full Vietnamese coverage, no bundled font binaries),
# TOC, PDF bookmarks (hyperref), chapters on new pages (book class).
#
# Usage: scripts/build_book.sh
#   LANG=en scripts/build_book.sh   build the English edition from book-en/
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$ROOT/build"
DIST="$ROOT/dist"
mkdir -p "$DIST"

# Language switch: vi (default) builds book/, en builds book-en/.
# header.tex, references.bib and ieee.csl are language-neutral and shared from book/.
LANG="${LANG:-vi}"
if [ "$LANG" = "en" ]; then
  BOOK_DIR="$ROOT/book-en"
  OUT_PREFIX="knowledge-graph-book-en"
else
  BOOK_DIR="$ROOT/book"
  OUT_PREFIX="knowledge-graph-book"
fi
SHARED_DIR="$ROOT/book"

echo "build_book: pre-rendering Mermaid figures"
LANG="$LANG" "$ROOT/scripts/render_mermaid.sh"

echo "build_book: pre-rendering TikZ figures"
LANG="$LANG" "$ROOT/scripts/render_tikz.sh"

# TikZ output lands in <book-dir>/figures/generated; chapters reference
# figures/generated/... relative to their own directory, so the PDFs must
# be present under build/figures/generated/ for Pandoc (run from build/) to resolve.
echo "build_book: copying generated PDF figures into build/"
mkdir -p "$BUILD/figures/generated"
if compgen -G "$BOOK_DIR/figures/generated/*.pdf" > /dev/null; then
  cp "$BOOK_DIR"/figures/generated/*.pdf "$BUILD/figures/generated/"
fi

# Ordered source list from the manifest.
mapfile -t SOURCES < <(sed -n '/^sources:/,/^[^ -]/p' "$BOOK_DIR/book-manifest.yaml" \
  | sed -n 's/^  - \(.*\.md\)$/\1/p')

CHAPTERS=()
for src in "${SOURCES[@]}"; do
  CHAPTERS+=("$BUILD/src/$src")
done

# Common Pandoc arguments (shared by print and screen variants).
# Run from build/ so relative figure paths resolve.
COMMON_ARGS=(
  --metadata-file "$BOOK_DIR/metadata.yaml"
  --include-in-header "$SHARED_DIR/header.tex"
  --pdf-engine=lualatex
  --citeproc
  --bibliography "$SHARED_DIR/references.bib"
  --csl "$SHARED_DIR/ieee.csl"
  --toc
  --resource-path "$BUILD"
  -V fontsize=11pt
  -V geometry:a4paper
  -V geometry:twoside
  -V geometry:inner=32mm
  -V geometry:outer=22mm
  -V geometry:top=25mm
  -V geometry:bottom=28mm
  --lua-filter="$ROOT/scripts/longtable-filter.lua"
)

echo "build_book: rendering print PDF (lualatex)"
# Note: do NOT pass -V colorlinks for print — any non-empty value (even
# "false") makes the Pandoc template enable colored links. Omitting it yields
# hidelinks: black, borderless, still internally consistent for print.
# --no-highlight keeps code blocks monochrome for grayscale-safe printing.
(cd "$BUILD" && pandoc "${CHAPTERS[@]}" \
  "${COMMON_ARGS[@]}" \
  --no-highlight \
  -o "$DIST/$OUT_PREFIX-print.pdf")

echo "build_book: rendering screen PDF (lualatex)"
(cd "$BUILD" && pandoc "${CHAPTERS[@]}" \
  "${COMMON_ARGS[@]}" \
  -V colorlinks \
  -o "$DIST/$OUT_PREFIX-screen.pdf")

echo "build_book: OK"
pdfinfo "$DIST/$OUT_PREFIX-print.pdf" | sed -n 's/^/  /p'
