"""Integrity checks for book manuscript content.

Catches common terminology errors and formatting issues across all chapters.
"""

from pathlib import Path

BOOK_DIR = Path(__file__).resolve().parent.parent / "book"


def _all_chapter_files():
    return sorted(BOOK_DIR.glob("chapter*.md"))


class TestSparqlExpansion:
    """SPARQL expansion: 'SPARQL Protocol and RDF Query Language',
    not 'Simple Protocol'."""

    WRONG_EXPANSION = "Simple Protocol and RDF Query Language"
    CORRECT_EXPANSION = "SPARQL Protocol and RDF Query Language"

    def test_no_wrong_sparql_expansion_in_chapters(self):
        for path in _all_chapter_files():
            text = path.read_text(encoding="utf-8")
            assert self.WRONG_EXPANSION not in text, (
                f"{path.name} contains wrong SPARQL expansion "
                f"'{self.WRONG_EXPANSION}'. Use '{self.CORRECT_EXPANSION}'."
            )

    def test_no_wrong_sparql_expansion_in_glossary(self):
        glossary = BOOK_DIR / "glossary.md"
        if glossary.exists():
            text = glossary.read_text(encoding="utf-8")
            assert self.WRONG_EXPANSION not in text, "glossary.md contains wrong SPARQL expansion."
