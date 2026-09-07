# Knowledge Graph: From Graph to Living Knowledge Systems

<h4 align="center">Từ Đồ thị đến Hệ thống Tri thức — An Executable, Bilingual Monograph</h4>

<p align="center">
  <a href="https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/latest"><img src="https://img.shields.io/github/v/release/MinhTuan76800310/knowledge_graph_learning-journey?label=release&color=blue" alt="release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL--3.0--or--later-blue" alt="license: GPL-3.0-or-later"></a>
  <a href="#editions"><img src="https://img.shields.io/badge/language-Vietnamese%20(Canonical)-green" alt="language: Vietnamese"></a>
  <a href="#editions"><img src="https://img.shields.io/badge/language-English%20(100%25%20Parity)-blue" alt="language: English"></a>
  <a href="#editions"><img src="https://img.shields.io/badge/pages-434_vi%20%C2%B7%20412_en-purple" alt="pages: 434 vi · 412 en"></a>
  <a href="#testing-and-validation"><img src="https://img.shields.io/badge/tests-106%20passed-brightgreen" alt="tests: 106 passed"></a>
  <a href="pyproject.toml"><img src="https://img.shields.io/badge/python-%3E%3D3.12-informational" alt="python: >=3.12"></a>
</p>

> **An open-source, executable, bilingual monograph.** Knowledge Graphs from first principles to production knowledge systems — explained at the mechanism level, with runnable experiments, rigorous mathematical foundations, and traceable citations.
>
> Published in **both Vietnamese and English** across all 10 chapters with **100% structural, pedagogical, and mathematical parity**.

**Latest release:** [`v0.3.0`](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/tag/v0.3.0) — Complete bilingual monograph: Vietnamese complete edition (**434** print pages) + English complete edition (**412** print pages), incorporating all **6 Frontier Theoretical Pillars**.

**License:** [GPL-3.0-or-later](LICENSE)

---

## 📥 Publication Downloads

The complete publication-ready PDF editions can be downloaded directly from GitHub Releases:

| Edition | Language | Pages | Content Scope | Download Link |
|---|:---:|:---:|---|:---:|
| **Vietnamese** | `vi` | **434** | Full Monograph (Front Matter, Ch 1–10, Afterword, Glossary, Bibliography) | [📥 `knowledge-graph-book-v0.3.0.pdf`](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/download/v0.3.0/knowledge-graph-book-v0.3.0.pdf) |
| **English** | `en` | **412** | Full Monograph (Front Matter, Ch 1–10, Afterword, Glossary, Bibliography) | [📥 `knowledge-graph-book-en-v0.3.0.pdf`](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/download/v0.3.0/knowledge-graph-book-en-v0.3.0.pdf) |

---

## 💡 The Two Mental Models

```text
Mental Model 1  (introduced in Chapter 1)
  Knowledge Graph  =  Data Graph  +  Semantics  +  Context

Mental Model 2  (emerges gradually; capstone architecture in Chapter 10)
  Knowledge System =  Knowledge Graph
                      + Acquisition + Inference + Validation + Evolution
```

These are **engineering learning models**, not universally accepted formal definitions. The book clearly demarcates the boundary between book-defined pedagogical models and authoritative formal standards (W3C RDF 1.1/1.2, OWL 2, SPARQL 1.1, SHACL).

---

## 🏛️ The Six Theoretical Pillars (v0.3.0 Upgrade)

The monograph bridges foundational knowledge engineering with frontier AI research through six core theoretical pillars:

1. **Structural Foundations & Identity (Chapters 1–3):** Directed Hypergraphs $\mathcal{H} = (V, \mathcal{E})$, LPG formal 7-tuple $\mathcal{G}$, Blank Nodes First-Order Model Theory ($\exists x$, lean graph NP-hardness), and the Vector Fallacy matrix.
2. **Logic Complexity & Fixpoint Semantics (Chapters 4–5):** Description Logics decidability landscape ($\mathcal{SROIQ}$ 2-NEXPTIME vs. Tractable Profiles), $DL\text{-}Lite_R$ First-Order Rewritability into SQL UCQ, Datalog 3-way semantics equivalence (Knaster-Tarski $T_P \uparrow \omega$), and Stratified Negation as Failure (NAF).
3. **Epistemics, Temporal Validity & Belief Revision (Chapters 6–7):** Dempster-Shafer theory of evidence ($m: 2^\Omega \to [0, 1]$), Subjective Logic $(b, d, u, a)$ opinion vectors & cumulative fusion $\oplus$, 2D Bitemporal Grid ($T_{\text{valid}} \times T_{\text{tx}}$), and AGM Belief Revision Postulates.
4. **Graph Representation Learning & Invariance (Chapter 8):** Weisfeiler-Lehman (1-WL) isomorphism bound on MPNN expressiveness, RotatE complex rotational algebra ($\mathbf{h} \circ \mathbf{r} = \mathbf{t}$), Poincaré hyperbolic taxonomy embeddings ($\mathbb{B}^d$), and Differentiable ILP ($\partial\text{ILP}$).
5. **Retrieval Dynamics & GraphRAG Bounds (Chapter 9):** Path explosion asymptotic bounds $O(\bar{d}^k)$, multi-hop error cascading bounds ($p^k$), Personalized PageRank contraction mapping, Steiner Tree 2-approximation, GraphRAG vs. 1M–2M Long-Context LLMs Pareto frontier, and Physical Evidence Packet dossiers.
6. **Cybernetic Stability & Model Collapse (Chapter 10):** Delayed closed-loop feedback control transfer functions $L(s) = G(s)H(s)e^{-s\tau_{\text{verify}}}$, Delay Differential Equation (DDE) stability theorems ($a\tau < \frac{\pi}{2}$), Hopf bifurcation limit cycles, Lyapunov stability ($\dot{V} < 0$), Knowledge Entropy ($H_K$), and Autophagous Model Collapse variance shrinkage ($\sigma_{t+1}^2 = \sigma_t^2(1 - 1/M)$).

---

## 📖 Chapters Overview

| # | Title | Core Question | Key Foundations & Frontier Mechanisms |
|:---:|---|---|---|
| **1** | From Graph to Knowledge | What turns a graph into a *knowledge* graph? | Graph topology, entity-relation-attribute substrates, semantic layering, vector fallacy matrix |
| **2** | Data Models and Query Languages | How do we represent and query knowledge mechanically? | RDF 1.1/1.2 triples, SPARQL 1.1 Basic Graph Patterns, Property Graphs, Cypher traversals, reification trade-offs |
| **3** | Schema, Identity, and Context | How do we model identity, ambiguity, and context? | URI/IRI minting, entity resolution, Blank Node model theory, Named Graphs, quad semantics |
| **4** | Ontologies and Formal Meaning | How do we give machine-readable meaning to data? | RDFS entailment, OWL 2 Description Logics ($\mathcal{SROIQ}$), DL-Lite FOL-rewritability, TBox vs. ABox |
| **5** | Deduction, Rules, and Validation | How do we infer new knowledge and validate integrity? | Datalog 3-way semantics, Knaster-Tarski fixpoint, Stratified NAF, SHACL closed-world constraint validation |
| **6** | Claims, Evidence, Provenance, Time, Contradiction | How do we handle competing, temporal, uncertain claims? | PROV-O provenance, Dempster-Shafer evidence, Subjective Logic fusion, 2D bitemporal modeling, AGM belief revision |
| **7** | Knowledge Acquisition and Integration | How do we acquire knowledge without blindly trusting extraction? | Extraction-to-candidate pipelines, Fellegi-Sunter entity linking, R2RML relational mapping, human-in-the-loop review |
| **8** | Inductive Knowledge and Learning from Graphs | How do graphs learn patterns and predict missing facts? | TransE/RotatE embeddings, Poincaré hyperbolic geometry, 1-WL expressiveness bound of MPNNs, Differentiable ILP |
| **9** | Retrieval, Question Answering, GraphRAG | How do we retrieve knowledge for humans and LLMs? | Combinatorial path explosion $O(\bar{d}^k)$, multi-hop error cascading $p^k$, Personalized PageRank, Steiner trees, GraphRAG vs. Long-Context |
| **10** | Building a Living Knowledge System | How do we build a self-sustaining, trustworthy knowledge system? | Delayed closed-loop feedback control, DDE stability criterion, Knowledge Entropy, autophagous collapse prevention |

The book concludes with an **Afterword (Lời bạt)** exploring societal authority, multi-agent epistemic governance, economic viability, and future paradigm shifts.

---

## 🌐 Editions & Parity Guarantee

The book is maintained in two parallel editions with **100% mutual parity**:

- **Vietnamese (Canonical):** `book/` — 434 print pages. Technical terms are introduced with their English equivalents on first occurrence ("thực thể (entity)", "suy diễn (inference)").
- **English Edition:** `book-en/` — 412 print pages. A rigorous, faithful parallel edition preserving exact section hierarchies, mathematical formulations, TikZ diagrams, and pedagogical structure.

Every single section, code listing, citation, and equation is aligned 1-to-1. Both editions are compiled using XeLaTeX through our automated PDF build and verification gates.

---

## 📂 Repository Structure

```
knowledge_graph_learning-journey/
├── README.md               # Repository overview (this document)
├── CONTRIBUTING.md         # Open-source contributor guidelines & quality standards
├── CLAUDE.md               # AI assistant working conventions & release protocol
├── pyproject.toml          # Python project dependencies (>=3.12)
├── uv.lock                 # Pinned dependencies lockfile
├── Makefile                # Build automation (make book, make book-check)
├── docker-compose.yml      # Optional Neo4j graph database container
├── book/                   # Canonical Vietnamese manuscript (Ch 1–10 + Front/Back Matter)
│   ├── chapter01.md ... chapter10.md
│   ├── preface.md, introduction.md, afterword.md
│   ├── glossary.md, references.bib, book-manifest.yaml, metadata.yaml
│   └── figures/            # TikZ source diagrams and compiled vector PDFs
├── book-en/                # English manuscript (Ch 1–10 + Front/Back Matter, 100% parity)
│   ├── chapter01.md ... chapter10.md
│   ├── preface.md, introduction.md, afterword.md
│   ├── glossary.md, references.bib, book-manifest.yaml, metadata.yaml
│   └── figures/            # English TikZ source diagrams and vector PDFs
├── chapter01/ ... /        # Standalone runnable Python experiments & tests
├── capstone/               # Mechanism Knowledge Graph capstone domain system
├── datasets/               # Running toy and mechanism datasets (e.g. rate_of_change.ttl)
├── tests/                  # Integrity test suite (106 tests: structure, concepts, citations)
├── docs/                   # Specifications, research notes, and semantic contracts
│   ├── README.md           # Navigational guide to the docs directory
│   ├── BOOK_STATUS.md      # Publication state of each manuscript section
│   ├── BOOK_PEDAGOGY.md    # Canonical authoring policy & pedagogical guidelines
│   ├── BOOK_V0_3_MILESTONE.md # Specification of the 6 theoretical pillars
│   ├── BOOK_V0_4_ROADMAP.md   # Roadmap for post-v0.3 frontier research modules
│   ├── source_index.json   # 92+ registered authoritative sources (W3C, papers, books)
│   └── CHAPTER*nn*_*.md    # Semantic contracts, depth reviews, and checkpoints
├── scripts/                # XeLaTeX / Pandoc compilation & verification pipeline
└── dist/                   # Built publication PDFs (gitignored; attached to Releases)
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.12+**
- **[uv](https://docs.astral.sh/uv/)** or standard `python -m venv` / `pip`
- **Docker** (optional; for live Neo4j Cypher exercises)
- **Pandoc & XeLaTeX / LuaLaTeX** (required only for building PDFs from markdown sources)

### Setup & Environment

```bash
# 1. Clone repository
git clone https://github.com/MinhTuan76800310/knowledge_graph_learning-journey.git
cd knowledge_graph_learning-journey

# 2. Install dependencies
uv sync
# Or with standard pip:
# python -m venv .venv && source .venv/bin/activate && pip install -e .

# 3. Run automated verification suite
python -m pytest
```

### Running Experiments

```bash
# Chapter 1: Plain Graph vs. Semantic KG
python chapter01/exp_1_1_plain_graph.py
python chapter01/exp_1_5_relation_semantics.py

# Chapter 2: RDFLib & SPARQL Querying
python chapter02/exp_2_1_rdf_first_principles.py
python chapter02/exp_2_4_mechanism_turtle_sparql.py
```

---

## 🛠️ Building the PDF Monograph

The monograph compilation pipeline uses Pandoc and XeLaTeX to produce publication-grade PDFs with custom typography, syntax highlighting, and vector TikZ diagrams:

```bash
# Build Vietnamese edition (creates dist/knowledge-graph-book-print.pdf)
make book
# Or run script directly:
bash scripts/build_book.sh

# Run automated verification gate on built Vietnamese PDF
make book-check
# Or run script directly:
bash scripts/verify_book_pdf.sh

# Build English edition (creates dist/knowledge-graph-book-en-print.pdf)
LANG=en bash scripts/build_book.sh

# Run automated verification gate on built English PDF
LANG=en bash scripts/verify_book_pdf.sh

# Clean build artifacts
make book-clean
```

---

## 🧪 Testing and Validation

The codebase enforces strict quality controls across empirical code, theoretical consistency, and manuscript structure:

```bash
# 1. Run all 106 unit, integration, and integrity tests
python -m pytest

# 2. Run Ruff code linter
python -m ruff check .

# 3. Run Ruff code formatter verification
python -m ruff format --check .
```

### Test Suite Architecture (106 tests)

- **Empirical Experiments:** `chapter01/test_experiments.py` (25 tests) & `chapter02/test_ch2_experiments.py` (30 tests) verify exact graph models, SPARQL query results, and RDFS entailment semantics.
- **Structural Integrity:** `tests/test_book_integrity.py` (8 tests) verifies Markdown headings, LaTeX math delimiters, and section structures.
- **Pedagogical Progression:** `tests/test_book_concept_dependencies.py` (8 tests) asserts that no chapter introduces concepts before their formal dependencies are defined.
- **Frontier Chapters Integrity:** `tests/test_chapter08_integrity.py` (4 tests), `tests/test_chapter09_integrity.py` (13 tests), and `tests/test_chapter10_integrity.py` (11 tests) verify coverage of theoretical terms, equations, and glossary entries.
- **Source & Repo Integrity:** `tests/test_repo_integrity.py` (7 tests) validates `docs/source_index.json`, research notes links, and ensures zero leaked development markers.

---

## 🗺️ Project Milestones & Roadmap

| Milestone | Scope & Highlights | Status |
|:---:|---|:---:|
| **v0.3.0** | **Full Bilingual Edition & 6 Frontier Theoretical Pillars:** All 10 chapters in Vietnamese (434 pages) and English (412 pages) in 100% parity; Hypergraphs, DL Decidability, Dempster-Shafer/AGM, 1-WL/RotatE, Combinatorial GraphRAG, Closed-Loop Cybernetics. | ✅ **RELEASED** (2026-09-07) |
| **v0.2.0** | **English Edition Inception & Chapter 3 Quality Pass:** English Ch 1–3 + Vietnamese Ch 3 deep rework (364 pages VI, 70 pages EN). | ✅ **RELEASED** (2026-09-02) |
| **v0.1.0** | **Complete Vietnamese Manuscript Baseline:** Chapters 1–10 + Afterword + Glossary (358 pages). | ✅ **RELEASED** (2026-08-31) |
| **v0.4.0** | **Advanced Frontiers (Post-v0.3 Extension):** Neuro-Symbolic Information Extraction, Vector-Graph Hybrid Entity Resolution, GNN-based Ontology Alignment, Structural Causal Models (SCMs), and Conformal Prediction. | 🚧 **PLANNED** (See [`docs/BOOK_V0_4_ROADMAP.md`](docs/BOOK_V0_4_ROADMAP.md)) |

Current per-section tracking lives in [`docs/BOOK_STATUS.md`](docs/BOOK_STATUS.md).

---

## 🤝 Contributing

Contributions, feedback, and semantic reviews from researchers, practitioners, and educators are warmly welcomed!

- Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution guidelines, branch conventions, and code standards.
- Before proposing changes to manuscript chapters, review [`docs/BOOK_PEDAGOGY.md`](docs/BOOK_PEDAGOGY.md) for pedagogical constraints.
- **Semantic corrections** (fixing an incorrect logical inference rule, clarifying Description Logic complexity bounds, or refining a mathematical proof) are treated with top priority.

---

## 👨‍💻 About the Author

This book is created by [**MinhTuan76800310**](https://github.com/MinhTuan76800310) as an open, public learning journey, dedicated to advancing deep conceptual mastery of Knowledge Graphs, Neuro-Symbolic AI, and Autonomous Multi-Agent Systems.

Core engineering values:
- **Understand mechanisms, not just APIs.**
- **Practice strict epistemic honesty.**
- **Ensure everything is traceable and verifiable.**

---

## 📜 Citation, Sources & Copyright

This repository contains original technical writing. All external concepts, algorithms, and W3C standards are cited and traceable:

- **Machine-readable Source Index:** [`docs/source_index.json`](docs/source_index.json)
- **BibTeX Bibliography:** [`book/references.bib`](book/references.bib)
- **Concept-to-Source Mapping:** [`docs/CITATION_MAP.md`](docs/CITATION_MAP.md)

If you find this work helpful in your research or engineering projects, please cite it as:

```bibtex
@book{nguyen2026knowledgegraph,
  title     = {Knowledge Graph: From Graph to Living Knowledge Systems},
  author    = {Nguyen, Minh Tuan},
  year      = {2026},
  publisher = {Open Source Monograph},
  url       = {https://github.com/MinhTuan76800310/knowledge_graph_learning-journey},
  note      = {Version 0.3.0, 434 pp. (Vietnamese), 412 pp. (English)}
}
```

**License:** [GPL-3.0-or-later](LICENSE)
