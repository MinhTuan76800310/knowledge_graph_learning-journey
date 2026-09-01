# Makefile — Knowledge Graph book build targets.
#
#   make book          build the Vietnamese print + screen PDFs into dist/
#   make book-check    build, then run the PDF verification gate
#   make book-en       build the English print + screen PDFs into dist/
#   make book-en-check build the English PDFs, then run the verification gate
#   make book-clean    remove build/ and dist/ artifacts
#
# dist/ is gitignored; attach PDFs to GitHub Releases / CI artifacts instead
# of committing them.

.PHONY: book book-check book-en book-en-check book-clean

book:
	bash scripts/build_book.sh

book-check: book
	bash scripts/verify_book_pdf.sh

book-en:
	LANG=en bash scripts/build_book.sh

book-en-check: book-en
	LANG=en bash scripts/verify_book_pdf.sh

book-clean:
	rm -rf build dist
