#!/usr/bin/env python3
"""extract_pdf_text.py — extract text from a PDF for the verification gate.

Why not pdftotext? The book's main font is Times New Roman (see book/header.tex).
lualatex embeds it with a ToUnicode CMap that mis-maps Vietnamese precomposed
glyphs (ờ -> i, and ơ/ư/ô/â/ê/đ dropped), so xpdf's pdftotext returns mangled
text and the gate's title/TOC/bibliography checks fail even though the PDF
renders correctly. PyMuPDF reads the glyph->Unicode mapping correctly and
preserves Vietnamese diacritics.

Usage: python scripts/extract_pdf_text.py <input.pdf> [output.txt]
Writes to stdout when output.txt is omitted.
"""

import sys

import pymupdf


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: extract_pdf_text.py <input.pdf> [output.txt]", file=sys.stderr)
        return 2
    pdf_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else None

    doc = pymupdf.open(pdf_path)
    text = "\n".join(page.get_text() for page in doc)
    doc.close()

    if out_path:
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(text)
    else:
        sys.stdout.buffer.write(text.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
