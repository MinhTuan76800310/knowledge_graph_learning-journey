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
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$ROOT/build"
DIST="$ROOT/dist"
mkdir -p "$DIST"

echo "build_book: pre-rendering Mermaid figures"
"$ROOT/scripts/render_mermaid.sh"

echo "build_book: pre-rendering TikZ figures"
"$ROOT/scripts/render_tikz.sh"

# Ordered source list from the manifest.
mapfile -t SOURCES < <(sed -n '/^sources:/,/^[^ -]/p' "$ROOT/book/book-manifest.yaml" \
  | sed -n 's/^  - \(.*\.md\)$/\1/p')

CHAPTERS=()
for src in "${SOURCES[@]}"; do
  CHAPTERS+=("$BUILD/src/$src")
done

# Common Pandoc arguments (shared by print and screen variants).
# Run from build/ so relative figure paths resolve.
COMMON_ARGS=(
  --metadata-file "$ROOT/book/metadata.yaml"
  --include-in-header "$ROOT/book/header.tex"
  --pdf-engine=lualatex
  --citeproc
  --bibliography "$ROOT/book/references.bib"
  --csl "$ROOT/book/ieee.csl"
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
  -o "$DIST/knowledge-graph-book-print.pdf")

echo "build_book: rendering screen PDF (lualatex)"
(cd "$BUILD" && pandoc "${CHAPTERS[@]}" \
  "${COMMON_ARGS[@]}" \
  -V colorlinks \
  -o "$DIST/knowledge-graph-book-screen.pdf")

echo "build_book: OK"
pdfinfo "$DIST/knowledge-graph-book-print.pdf" | sed -n 's/^/  /p'
