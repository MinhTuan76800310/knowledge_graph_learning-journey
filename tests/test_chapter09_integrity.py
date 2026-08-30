"""Integrity checks specific to Chapter 9 (Retrieval, QA and GraphRAG).

Verifies the manuscript structure, figure coverage, citation integrity,
glossary coverage, and concept-registry registration for Chapter 9.
"""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = ROOT / "book"
CH9 = BOOK_DIR / "chapter09.md"

SECTIONS = [f"9.{i}" for i in range(1, 80)]  # §9.1 .. §9.79

FIGURES = [
    "ch09-full-stack",
    "ch09-multihop-subgraph",
    "ch09-ledger-vs-canonical",
    "ch09-topk-bound",
    "ch09-evidence-packet",
    "ch09-correctness-grounding",
    "ch09-query-router",
    "ch09-text-vs-graph-vs-hybrid",
    "ch09-kgqa-rag-graphrag",
]

CITED_KEYS = [
    "chakraborty-kgqa-2019",
    "cormack-rrf-2009",
    "edge-graphrag-2024",
    "gao-cite-2023",
    "hogan-inductive",
    "jarvelin-ndcg-2002",
    "karpukhin-dpr-2020",
    "lewis-rag-2020",
    "liu-lostmid-2023",
    "manning-ir-2008",
    "microsoft-graphrag-docs",
    "nogueira-rerank-2019",
    "prov-o",
    "rashkin-ais-2021",
    "robertson-bm25-2009",
    "w3c-sparql11-overview",
    "w3c-sparql11-query",
    "zhu-llmkg-2023",
]

# Registry concept name -> glossary entry prefix (first word(s) of the term).
GLOSSARY_TERMS = [
    "Abstention",
    "Agentic retrieval",
    "Answer claim",
    "Answer generation",
    "Answer provenance",
    "BM25",
    "Canonical View",
    "Citation",
    "Claim Ledger",
    "Community retrieval",
    "Context assembly",
    "Contradiction-aware retrieval",
    "Correctness",
    "Dense retrieval",
    "Entity linking",
    "Evidence diversity",
    "Evidence Packet",
    "Faithfulness",
    "Gold evidence",
    "Governance-aware retrieval",
    "Graph-first",
    "Graph serialization",
    "GraphRAG",
    "Grounded answer",
    "Hybrid retrieval",
    "Hypothesis-testing retrieval",
    "Index",
    "KGQA",
    "k-hop neighborhood",
    "Lexical retrieval",
    "Lost in the Middle",
    "Multi-hop retrieval",
    "nDCG",
    "Path bound",
    "Path explosion",
    "Precision",
    "Precision@K",
    "Provenance-aware retrieval",
    "Query decomposition",
    "Query drift",
    "Query embedding",
    "Query intent",
    "Query planning",
    "Query Execution Router",
    "RAG",
    "Rank fusion",
    "Recall",
    "Reranking",
    "Retrieval plan",
    "Retrieval provenance",
    "Retrieval unit",
    "RRF",
    "Score semantics",
    "Stopping condition",
    "Subgraph retrieval",
    "Symbolic graph retrieval",
    "Temporal retrieval",
    "top_k",
    "Unknown vs Not Found",
]

REGISTRY_PATH = BOOK_DIR / "concept_registry.yaml"


class TestManuscriptStructure:
    """Every planned section §9.1–§9.79 must exist as a level-2 header."""

    def test_chapter_file_exists(self):
        assert CH9.exists(), "book/chapter09.md is missing"

    def test_all_sections_present(self):
        text = CH9.read_text(encoding="utf-8")
        headers = set(re.findall(r"^## ([0-9.]+) ", text, flags=re.M))
        missing = [s for s in SECTIONS if s not in headers]
        assert not missing, f"Missing chapter sections: {missing}"

    def test_all_figures_included(self):
        text = CH9.read_text(encoding="utf-8")
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
        text = CH9.read_text(encoding="utf-8")
        assert "## Thuật ngữ đã gặp trong chương này" in text, "Glossary section missing"
        assert "## Tài liệu tham khảo" in text, "References section missing"


class TestCh9Citations:
    """Every citation key used in chapter09.md must exist in references.bib."""

    def test_cited_keys_present_in_bib(self):
        bib = (BOOK_DIR / "references.bib").read_text(encoding="utf-8")
        missing = [k for k in CITED_KEYS if f"{{{k}," not in bib and f"{{{k}}}" not in bib]
        assert not missing, f"Bib entries missing for: {missing}"

    def test_manuscript_cites_all_planned_keys(self):
        text = CH9.read_text(encoding="utf-8")
        missing = [k for k in CITED_KEYS if f"@{k}" not in text]
        assert not missing, f"Keys never cited in chapter09.md: {missing}"


class TestCh9GlossaryCoverage:
    """All planned Chapter 9 glossary terms must be present."""

    def test_glossary_terms_present(self):
        glossary = (BOOK_DIR / "glossary.md").read_text(encoding="utf-8")
        entries = set(re.findall(r"^\*\*([A-Za-z][^()\n]*?)(?:\([^)]*\))?\.\*\*", glossary, re.M))
        missing = []
        for term in GLOSSARY_TERMS:
            # Compare case-insensitively on the leading word(s).
            if not any(term.lower() in e.lower() for e in entries):
                missing.append(term)
        assert not missing, f"Glossary missing Ch9 terms: {missing}"


class TestCh9ConceptRegistry:
    """Chapter 9 concepts must be registered with correct chapter fields."""

    def test_registry_parses(self):
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        ch9 = {
            name: entry
            for name, entry in data["concepts"].items()
            if entry.get("first_explained_chapter") == 9
        }
        # 77 concepts are explained first in Chapter 9.
        assert len(ch9) == 77, f"Expected 77 Ch9 concepts, found {len(ch9)}"

    def test_ch9_concepts_explained_when_required(self):
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        for name, entry in data["concepts"].items():
            if entry.get("first_explained_chapter") == 9:
                assert entry["first_required_use_chapter"] == 9, (
                    f"Ch9 concept '{name}' required in Ch{entry['first_required_use_chapter']}"
                )

    def test_ch9_concepts_mentioned_by_chapter_nine(self):
        with open(REGISTRY_PATH, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        late = []
        for name, entry in data["concepts"].items():
            if (
                entry.get("first_explained_chapter") == 9
                and entry.get("first_mentioned_chapter") > 9
            ):
                late.append(name)
        assert not late, f"Ch9 concepts first mentioned after Ch9: {late}"
