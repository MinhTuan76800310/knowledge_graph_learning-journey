"""Integrity checks specific to Chapter 8 (Inductive Knowledge).

Verifies the manuscript structure, figure coverage, citation integrity,
glossary coverage, and concept-registry registration for Chapter 8.
"""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "book"
CH8 = BOOK_DIR / "chapter08.md"

SECTIONS = [f"8.{i}" for i in range(52)]  # §8.0 .. §8.51

FIGURES = [
    "ch08-reasoning-modes",
    "ch08-transe-geometry",
    "ch08-negative-sampling",
    "ch08-message-passing",
    "ch08-invariant-abstraction",
    "ch08-hybrid-pipeline",
    "ch08-counterexample-refinement",
    "ch08-full-stack",
]

CITED_KEYS = [
    "hogan-inductive",
    "bordes-transe-2013",
    "yang-distmult-2015",
    "trouillon-complex-2016",
    "schlichtkrull-rgcn-2018",
    "galarraga-amie-2015",
    "teru-grail-2020",
    "nickel-relational-ml-2016",
    "mikolov-negativesampling-2013",
    "li-oversmoothing-2018",
    "geirhos-shortcut-2020",
    "guo-calibration-2017",
    "shumailov-collapse-2024",
    "hamilton-grl-2020",
    "prov-o",
    "w3c-shacl",
]

# Registry concept name -> glossary entry prefix (first word(s) of the term).
GLOSSARY_TERMS = [
    "Abduction",
    "Calibration",
    "CandidateAxiom",
    "CandidateMechanismHypothesis",
    "Classification",
    "Clustering",
    "ComplEx",
    "Cosine similarity",
    "Cross-domain generalization",
    "Data leakage",
    "Deduction",
    "DistMult",
    "False negative",
    "Filtered evaluation",
    "GNN",
    "Hard negative",
    "Hits@K",
    "Induction",
    "Inductive bias",
    "Inductive KG learning",
    "Invariant structure",
    "Knowledge Graph Embedding",
    "Link prediction",
    "Message passing",
    "Model Assessment",
    "Model collapse",
    "MRR",
    "Negative sampling",
    "OOV entity",
    "Oversmoothing",
    "Path-based explanation",
    "Prediction",
    "R-GCN",
    "Representation learning",
    "Rule induction",
    "Rule-mining confidence",
    "Scoring function",
    "Self-reinforcing feedback",
    "Source leakage",
    "Spurious correlation",
    "Structural similarity",
    "Temporal leakage",
    "Train/validation/test split",
    "Training provenance",
    "Transductive learning",
    "TransE",
]

REGISTRY_PATH = BOOK_DIR / "concept_registry.yaml"


class TestManuscriptStructure:
    """Every planned section §8.0–§8.51 must exist as a level-2 header."""

    def test_chapter_file_exists(self):
        assert CH8.exists(), "book/chapter08.md is missing"

    def test_all_sections_present(self):
        text = CH8.read_text(encoding="utf-8")
        headers = set(re.findall(r"^## ([0-9.]+) ", text, flags=re.M))
        missing = [s for s in SECTIONS if s not in headers]
        assert not missing, f"Missing chapter sections: {missing}"

    def test_all_figures_included(self):
        text = CH8.read_text(encoding="utf-8")
        missing = []
        for fig in FIGURES:
            if f"figures/generated/{fig}.pdf" not in text:
                missing.append(fig)
        assert not missing, f"Figures not included in manuscript: {missing}"

    def test_figure_files_exist(self):
        for fig in FIGURES:
            pdf = BOOK_DIR / "figures" / "generated" / f"{fig}.pdf"
            assert pdf.exists(), f"Compiled figure missing: {pdf}"

    def test_glossary_and_references_sections(self):
        text = CH8.read_text(encoding="utf-8")
        assert "## Thuật ngữ đã gặp trong chương này" in text, "Glossary section missing"
        assert "## Tài liệu tham khảo" in text, "References section missing"


class TestCh8Citations:
    """Every citation key used in chapter08.md must exist in references.bib."""

    def test_cited_keys_present_in_bib(self):
        bib = (BOOK_DIR / "references.bib").read_text(encoding="utf-8")
        missing = [k for k in CITED_KEYS if f"{{{k}," not in bib and f"{{{k}}}" not in bib]
        assert not missing, f"Bib entries missing for: {missing}"

    def test_manuscript_cites_all_planned_keys(self):
        text = CH8.read_text(encoding="utf-8")
        missing = [k for k in CITED_KEYS if f"@{k}" not in text]
        assert not missing, f"Keys never cited in chapter08.md: {missing}"


class TestCh8GlossaryCoverage:
    """All planned Chapter 8 glossary terms must be present."""

    def test_glossary_terms_present(self):
        glossary = (BOOK_DIR / "glossary.md").read_text(encoding="utf-8")
        entries = set(re.findall(r"^\*\*([A-Za-z][^()\n]*?)(?:\([^)]*\))?\.\*\*", glossary, re.M))
        missing = []
        for term in GLOSSARY_TERMS:
            # Compare case-insensitively on the leading word(s).
            if not any(term.lower() in e.lower() for e in entries):
                missing.append(term)
        assert not missing, f"Glossary missing Ch8 terms: {missing}"


class TestCh8ConceptRegistry:
    """Chapter 8 concepts must be registered with correct chapter fields."""

    def test_registry_parses(self):
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        ch8 = {
            name: entry
            for name, entry in data["concepts"].items()
            if entry.get("first_explained_chapter") == 8
        }
        # 52 concepts are explained first in Chapter 8.
        assert len(ch8) == 52, f"Expected 52 Ch8 concepts, found {len(ch8)}"

    def test_ch8_concepts_explained_when_required(self):
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        for name, entry in data["concepts"].items():
            if entry.get("first_explained_chapter") == 8:
                assert entry["first_required_use_chapter"] == 8, (
                    f"Ch8 concept '{name}' required in Ch{entry['first_required_use_chapter']}"
                )

    def test_ch8_concepts_mentioned_by_chapter_eight(self):
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        late = []
        for name, entry in data["concepts"].items():
            if (
                entry.get("first_explained_chapter") == 8
                and entry.get("first_mentioned_chapter") > 8
            ):
                late.append(name)
        assert not late, f"Ch8 concepts first mentioned after Ch8: {late}"
