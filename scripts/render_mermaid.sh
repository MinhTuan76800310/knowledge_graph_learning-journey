#!/usr/bin/env bash
# render_mermaid.sh — pre-render Mermaid diagrams for the book PDF build.
#
# For every manuscript source listed in book/book-manifest.yaml:
#   1. Extract each ```mermaid fenced block to build/figures/<stem>-figN.mmd
#   2. Render it to a high-resolution PNG with mermaid-cli (mmdc)
#   3. Rewrite the source to build/src/<stem>.md, replacing the fence with a
#      Pandoc image whose caption is taken from the following "Hình:" line
#      (continuation lines up to the next blank line are part of the caption).
#
# SVG would be the preferred vector output, but no SVG->PDF converter
# (inkscape, rsvg-convert, ImageMagick) is installed on the build machine,
# so we render 3x-scale PNGs (~300+ dpi at A4 text width), which are
# print-safe. The Mermaid source stays in the manuscript as the source of
# truth.
#
# Usage: scripts/render_mermaid.sh
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD="$ROOT/build"
FIGDIR="$BUILD/figures"
SRCDIR="$BUILD/src"
mkdir -p "$FIGDIR" "$SRCDIR"

# Language switch: vi (default) reads book/ and uses "Hình:" captions;
# en reads book-en/ and uses "Figure:" captions.
LANG="${LANG:-vi}"
if [ "$LANG" = "en" ]; then
  BOOK_DIR="$ROOT/book-en"
  CAPTION_PREFIX="Figure:"
else
  BOOK_DIR="$ROOT/book"
  CAPTION_PREFIX="Hình:"
fi

# mermaid-cli runs headless Chromium; Ubuntu 24.04 AppArmor blocks the
# sandbox for unprivileged user namespaces, so disable it explicitly.
PUPPETEER_CFG="$BUILD/puppeteer.json"
cat > "$PUPPETEER_CFG" <<'EOF'
{
  "args": ["--no-sandbox", "--disable-setuid-sandbox"]
}
EOF

# Parse the manifest: lines "  - name.md" under the sources: key.
mapfile -t SOURCES < <(sed -n '/^sources:/,/^[^ -]/p' "$BOOK_DIR/book-manifest.yaml" \
  | sed -n 's/^  - \(.*\.md\)$/\1/p')

if [ "${#SOURCES[@]}" -eq 0 ]; then
  echo "render_mermaid: no sources found in $BOOK_DIR/book-manifest.yaml" >&2
  exit 1
fi

for src in "${SOURCES[@]}"; do
  python - "$BOOK_DIR/$src" "$FIGDIR" "$SRCDIR" "$CAPTION_PREFIX" <<'PYEOF'
import re
import subprocess
import sys
from pathlib import Path

src_path = Path(sys.argv[1])
figdir = Path(sys.argv[2])
srcdir = Path(sys.argv[3])
caption_prefix = sys.argv[4]
stem = src_path.stem

lines = src_path.read_text(encoding="utf-8").splitlines()
out = []
i = 0
fig_n = 0
while i < len(lines):
    line = lines[i]
    if line.strip() == "```mermaid":
        # Collect the mermaid block.
        block = []
        i += 1
        while i < len(lines) and lines[i].strip() != "```":
            block.append(lines[i])
            i += 1
        i += 1  # skip closing fence
        fig_n += 1
        mmd = figdir / f"{stem}-fig{fig_n}.mmd"
        png = figdir / f"{stem}-fig{fig_n}.png"
        mmd.write_text("\n".join(block) + "\n", encoding="utf-8")

        # Skip blank lines, then collect the caption ("Hình:" / "Figure:").
        while i < len(lines) and lines[i].strip() == "":
            i += 1
        caption_parts = []
        if i < len(lines) and lines[i].startswith(caption_prefix):
            caption_parts.append(lines[i][len(caption_prefix):].strip())
            i += 1
            while i < len(lines) and lines[i].strip() != "":
                caption_parts.append(lines[i].strip())
                i += 1
        caption = " ".join(caption_parts) or f"{caption_prefix.rstrip(':')} {fig_n}"

        print(f"render_mermaid: rendering {mmd.name} -> {png.name}")
        subprocess.run(
            [
                "npx", "-y", "@mermaid-js/mermaid-cli",
                "-i", str(mmd), "-o", str(png),
                "--scale", "3",
                "--backgroundColor", "white",
                "-p", str(figdir.parent / "puppeteer.json"),
            ],
            check=True,
            shell=True,
        )
        # Pandoc implicit figure: image alone in a paragraph => figure env.
        out.append(f"![{caption}](figures/{png.name})")
        out.append("")
    else:
        out.append(line)
        i += 1

srcdir.joinpath(src_path.name).write_text("\n".join(out) + "\n", encoding="utf-8")
PYEOF
done

echo "render_mermaid: done (${#SOURCES[@]} sources, figures in $FIGDIR)"
