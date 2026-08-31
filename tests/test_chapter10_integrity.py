"""Integrity checks specific to Chapter 10 (Living Knowledge Systems).

Verifies the manuscript structure, figure coverage, citation integrity,
glossary coverage, and concept-registry registration for Chapter 10.
"""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "book"
CH10 = BOOK_DIR / "chapter10.md"

SECTIONS = [f"10.{i}" for i in range(1, 63)]  # §10.1 .. §10.62

FIGURES = [
    "ch10-six-flows",
    "ch10-freshness-correctness",
    "ch10-monitoring-loop",
    "ch10-feedback-gate",
    "ch10-contradiction-debt",
    "ch10-quality-dimensions",
    "ch10-feedback-collapse",
    "ch10-audit-replay",
    "ch10-living-architecture",
]

CITED_KEYS = [
    "cai-tkgc-2023",
    "dong-knowledge-vault-2014",
    "gama-drift-2014",
    "iso-25012-2008",
    "iso-8000-2022",
    "klein-ontology-versioning-2001",
    "mitchell-neverending-2018",
    "noy-ontology-evolution-2004",
    "paulheim-refinement-2017",
    "recht-imagenet-2019",
    "sambasivan-cascades-2021",
    "sculley-debt-2015",
    "shumailov-collapse-2024",
    "widmer-drift-1996",
    "zaveri-kgquality-2016",
]

# Registry concept name -> glossary entry prefix (first word(s) of the term).
GLOSSARY_TERMS = [
    "Aggregation Window",
    "Alert",
    "Assessment Clock",
    "Audit Replay",
    "Audit Trail",
    "Automation Gradient",
    "Batch Governance",
    "Benchmark Decay",
    "Candidate Claim",
    "Contradiction Accumulation",
    "Contradiction Debt",
    "Contradiction Queue",
    "Controlled Trust",
    "Correctness over Time",
    "Data Drift",
    "Degradation",
    "Escalation Policy",
    "Feedback Collapse",
    "Feedback Loop",
    "Feedback Loop Safety",
    "Freshness",
    "Knowledge Debt",
    "Level vs Trend",
    "Living Architecture",
    "Living Knowledge System",
    "Maintenance Operations",
    "Monitoring Loop",
    "Orchestration",
    "Quality Dimension",
    "Re-assessment",
    "Re-validation",
    "Retirement",
    "Self-Observation",
    "Six Flows of Change",
    "Staleness",
    "Supersession at Scale",
    "System Clock",
    "System Health Report",
    "System State",
    "Threshold as Policy",
    "User Correction",
    "Valid Clock",
]

REGISTRY_PATH = BOOK_DIR / "concept_registry.yaml"


class TestManuscriptStructure:
    """Every planned section §10.1–§10.62 must exist as a level-2 header."""

    def test_chapter_file_exists(self):
        assert CH10.exists(), "book/chapter10.md is missing"

    def test_all_sections_present(self):
        text = CH10.read_text(encoding="utf-8")
        headers = set(re.findall(r"^## ([0-9.]+) ", text, flags=re.M))
        missing = [s for s in SECTIONS if s not in headers]
        assert not missing, f"Missing chapter sections: {missing}"

    def test_all_figures_included(self):
        text = CH10.read_text(encoding="utf-8")
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
        text = CH10.read_text(encoding="utf-8")
        assert "## Thuật ngữ đã gặp trong chương này" in text, "Glossary section missing"
        assert "## Tài liệu tham khảo" in text, "References section missing"


class TestCh10Citations:
    """Every citation key used in chapter10.md must exist in references.bib."""

    def test_cited_keys_present_in_bib(self):
        bib = (BOOK_DIR / "references.bib").read_text(encoding="utf-8")
        missing = [k for k in CITED_KEYS if f"{{{k}," not in bib and f"{{{k}}}" not in bib]
        assert not missing, f"Bib entries missing for: {missing}"

    def test_manuscript_cites_all_planned_keys(self):
        text = CH10.read_text(encoding="utf-8")
        missing = [k for k in CITED_KEYS if f"@{k}" not in text]
        assert not missing, f"Keys never cited in chapter10.md: {missing}"


class TestCh10GlossaryCoverage:
    """All planned Chapter 10 glossary terms must be present."""

    def test_glossary_terms_present(self):
        glossary = (BOOK_DIR / "glossary.md").read_text(encoding="utf-8")
        entries = set(re.findall(r"^\*\*([A-Za-z][^()\n]*?)(?:\([^)]*\))?\.\*\*", glossary, re.M))
        missing = []
        for term in GLOSSARY_TERMS:
            # Compare case-insensitively on the leading word(s).
            if not any(term.lower() in e.lower() for e in entries):
                missing.append(term)
        assert not missing, f"Glossary missing Ch10 terms: {missing}"


class TestCh10ConceptRegistry:
    """Chapter 10 concepts must be registered with correct chapter fields."""

    def test_registry_parses(self):
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        ch10 = {
            name: entry
            for name, entry in data["concepts"].items()
            if entry.get("first_explained_chapter") == 10
        }
        # 54 concepts are explained first in Chapter 10.
        assert len(ch10) == 54, f"Expected 54 Ch10 concepts, found {len(ch10)}"

    def test_ch10_concepts_explained_when_required(self):
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        for name, entry in data["concepts"].items():
            if entry.get("first_explained_chapter") == 10:
                assert entry["first_required_use_chapter"] == 10, (
                    f"Ch10 concept '{name}' required in Ch{entry['first_required_use_chapter']}"
                )

    def test_ch10_concepts_mentioned_by_chapter_ten(self):
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        late = []
        for name, entry in data["concepts"].items():
            if (
                entry.get("first_explained_chapter") == 10
                and entry.get("first_mentioned_chapter") > 10
            ):
                late.append(name)
        assert not late, f"Ch10 concepts first mentioned after Ch10: {late}"
