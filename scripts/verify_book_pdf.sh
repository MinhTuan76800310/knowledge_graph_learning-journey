#!/usr/bin/env bash
# verify_book_pdf.sh — verification gate for the built book PDFs.
#
# Checks (per docs/BOOK_V0_1_MILESTONE.md):
#   1. Both PDFs exist and pdfinfo succeeds
#   2. Expected chapter/front-matter titles appear in extracted text
#   3. Table of contents exists
#   4. Bibliography resolved (section present, numeric entries rendered)
#   5. No unresolved Pandoc citations like [@key]
#   6. No leftover Mermaid fences or raw "Hình:" caption lines
#   7. No U+FFFD replacement characters
#   8. No wrapper artifacts (leaked tool closing tags)
#   9. Representative pages render to images for visual inspection
#
# Exit code 0 = gate passed. Any failure is reported and exits non-zero.
#
# Usage: scripts/verify_book_pdf.sh
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST="$ROOT/dist"

# Language switch: vi (default) verifies the Vietnamese book; en verifies the
# English edition (book-en/, knowledge-graph-book-en-*.pdf).
LANG="${LANG:-vi}"
if [ "$LANG" = "en" ]; then
  OUT_PREFIX="knowledge-graph-book-en"
  # Match dash-free substrings: pdftotext renders the em-dash as "--", so a
  # fixed-string check on the full heading would not match.
  EXPECTED_TITLES=(
    "From Graph to Knowledge"
    "Data Models and Query Languages"
    "Schema, Identity, and Context"
    "Ontologies and Formal Meaning"
    "Deduction, Rules, and Validation"
  )
  TOC_PAT='Contents'
  BIB_TITLE='References'
  CAPTION_LEAK='^Figure:'
else
  OUT_PREFIX="knowledge-graph-book"
  EXPECTED_TITLES=(
    "Lời nói đầu"
    "Cách sử dụng cuốn sách này"
    "Giới thiệu"
    "Chương 1 — Từ Đồ thị đến Tri thức"
    "Chương 2 — Mô hình Dữ liệu và Ngôn ngữ Truy vấn"
    "Chương 3 — Lược đồ, Định danh và Ngữ cảnh"
    "Thuật ngữ"
  )
  TOC_PAT='ục lục'
  BIB_TITLE='Tài liệu tham khảo'
  CAPTION_LEAK='^Hình:'
fi

PRINT="$DIST/$OUT_PREFIX-print.pdf"
SCREEN="$DIST/$OUT_PREFIX-screen.pdf"
PREVIEW="$DIST/preview"
WORK="$DIST/.verify"
mkdir -p "$PREVIEW" "$WORK"

FAIL=0
pass() { echo "  PASS: $1"; }
fail() { echo "  FAIL: $1"; FAIL=1; }

echo "verify_book_pdf: gate start"

# --- 1. Existence + pdfinfo -------------------------------------------------
for pdf in "$PRINT" "$SCREEN"; do
  if [ ! -f "$pdf" ]; then
    fail "missing PDF: $pdf (run 'make book' first)"
    continue
  fi
  if pdfinfo "$pdf" > "$WORK/pdfinfo.$(basename "$pdf").txt" 2>/dev/null; then
    pages=$(sed -n 's/^Pages:[[:space:]]*//p' "$WORK/pdfinfo.$(basename "$pdf").txt")
    pass "$(basename "$pdf"): pdfinfo OK, $pages pages"
  else
    fail "$(basename "$pdf"): pdfinfo failed"
  fi
done
[ "$FAIL" -eq 1 ] && { echo "verify_book_pdf: GATE FAILED"; exit 1; }

# --- Extract text from the print PDF for content checks ---------------------
# PyMuPDF (not pdftotext): Times New Roman's ToUnicode CMap mis-maps Vietnamese
# precomposed glyphs, so pdftotext drops diacritics even though the PDF renders
# correctly (see scripts/extract_pdf_text.py). PyMuPDF preserves them.
python "$ROOT/scripts/extract_pdf_text.py" "$PRINT" "$WORK/book.txt" \
  || { fail "PDF text extraction failed"; echo "verify_book_pdf: GATE FAILED"; exit 1; }
# Whitespace-normalized copy for title/TOC/bibliography checks: PyMuPDF may
# drop or insert a space at some glyph boundaries ("sử dụng" -> "sửdụng"), so
# match on space-free substrings to stay robust.
tr -d '[:space:]' < "$WORK/book.txt" > "$WORK/book.norm.txt"

# --- 2. Expected titles ------------------------------------------------------
for title in "${EXPECTED_TITLES[@]}"; do
  norm_title="${title//[[:space:]]/}"
  if grep -qF "$norm_title" "$WORK/book.norm.txt"; then
    pass "title present: $title"
  else
    fail "title missing from PDF text: $title"
  fi
done

# --- 3. Table of contents ----------------------------------------------------
# Match a whitespace-normalized substring rather than the exact heading.
norm_toc="${TOC_PAT//[[:space:]]/}"
if grep -qF "$norm_toc" "$WORK/book.norm.txt"; then
  pass "table of contents present"
else
  fail "no TOC heading found (Mục lục / Contents)"
fi

# --- 4. Bibliography ----------------------------------------------------------
norm_bib="${BIB_TITLE//[[:space:]]/}"
if grep -qF "$norm_bib" "$WORK/book.norm.txt"; then
  pass "bibliography section present"
else
  fail "bibliography section '$BIB_TITLE' missing"
fi
# Numeric IEEE-style entries, e.g. "[1]  W3C, ..."
if grep -qE '^\[[0-9]+\]' "$WORK/book.txt"; then
  pass "numeric bibliography entries rendered"
else
  fail "no numeric bibliography entries found — citations may not have resolved"
fi

# --- 5. Unresolved citations ---------------------------------------------------
if grep -nE '\[@[A-Za-z0-9_-]+\]' "$WORK/book.txt"; then
  fail "unresolved Pandoc citation markers found (see above)"
else
  pass "no unresolved [@...] citation markers"
fi

# --- 6. Leftover Mermaid / raw captions ----------------------------------------
if grep -nE '```mermaid|^graph LR|^graph TD' "$WORK/book.txt"; then
  fail "leftover Mermaid content in PDF text (see above)"
else
  pass "no leftover Mermaid blocks"
fi
if grep -nE "$CAPTION_LEAK" "$WORK/book.txt"; then
  fail "raw '$CAPTION_LEAK' caption lines leaked into PDF text"
else
  pass "no raw caption lines"
fi

# --- 7. Replacement characters ---------------------------------------------------
if grep -n $'\uFFFD' "$WORK/book.txt"; then
  fail "U+FFFD replacement characters found — font/glyph problem"
else
  pass "no U+FFFD replacement characters"
fi

# --- 8. Wrapper artifacts ---------------------------------------------------------
if grep -nE '<[/](content|parameter|tool_use|invoke)' "$WORK/book.txt"; then
  fail "wrapper/tool artifacts leaked into PDF text"
else
  pass "no wrapper artifacts"
fi

# --- 9. Render representative pages ------------------------------------------------
pages=$(sed -n 's/^Pages:[[:space:]]*//p' "$WORK/pdfinfo.$(basename "$PRINT").txt")
# Page 1 (title), TOC area (p3), chapter starts, and last pages (bibliography).
REPR_PAGES="1 3"
# First page of each chapter: locate via pdftotext per-page scan is costly;
# sample evenly instead: 25%, 50%, 75%, and the final page.
for frac in 25 50 75 100; do
  p=$(( (pages * frac + 99) / 100 ))
  [ "$p" -lt 1 ] && p=1
  REPR_PAGES="$REPR_PAGES $p"
done
REPR_PAGES=$(echo "$REPR_PAGES" | tr ' ' '\n' | sort -nu | tr '\n' ' ')
echo "  rendering representative pages: $REPR_PAGES"
for p in $REPR_PAGES; do
  if pdftoppm -png -r 100 -f "$p" -l "$p" "$PRINT" "$WORK/pp" 2>/dev/null; then
    rendered=$(ls "$WORK"/pp-*.png 2>/dev/null | head -1)
    if [ -n "$rendered" ]; then
      cp "$rendered" "$PREVIEW/page-$p.png"
      rm -f "$WORK"/pp-*.png
      pass "page $p rendered -> preview/page-$p.png"
    else
      fail "page $p produced no image"
    fi
  else
    fail "pdftoppm failed on page $p"
  fi
done

echo
if [ "$FAIL" -eq 0 ]; then
  echo "verify_book_pdf: GATE PASSED ($pages pages, previews in $PREVIEW)"
  exit 0
else
  echo "verify_book_pdf: GATE FAILED"
  exit 1
fi
