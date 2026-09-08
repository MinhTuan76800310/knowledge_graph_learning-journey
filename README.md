# Knowledge Graph: From Graph to Living Knowledge Systems

<h4 align="center">Từ Đồ thị đến Hệ thống Tri thức Sống — An Open-Source Bilingual Monograph</h4>

<p align="center">
  <a href="https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/latest"><img src="https://img.shields.io/github/v/release/MinhTuan76800310/knowledge_graph_learning-journey?label=release&color=blue" alt="release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-GPL--3.0--or--later-blue" alt="license: GPL-3.0-or-later"></a>
  <a href="#editions"><img src="https://img.shields.io/badge/Vietnamese-Canonical-green" alt="Vietnamese"></a>
  <a href="#editions"><img src="https://img.shields.io/badge/English-Complete-blue" alt="English"></a>
  <a href="#testing"><img src="https://img.shields.io/badge/tests-144%20passed-brightgreen" alt="tests: 144 passed"></a>
  <a href="pyproject.toml"><img src="https://img.shields.io/badge/python-%3E%3D3.12-informational" alt="python: >=3.12"></a>
</p>

> An open-source, executable monograph on Knowledge Graphs — from first principles to production systems. Explained at the mechanism level, with runnable experiments, rigorous mathematical foundations, and traceable citations.

---

## 📥 Downloads

| Edition | Pages | Download |
|---------|:-----:|:--------:|
| **Vietnamese** (Canonical) | 434 | [📥 PDF](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/download/v0.3.0/knowledge-graph-book-v0.3.0.pdf) |
| **English** | 412 | [📥 PDF](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/download/v0.3.0/knowledge-graph-book-en-v0.3.0.pdf) |

---

## The Two Mental Models

```
Model 1  (Chapter 1)
  Knowledge Graph  =  Data Graph  +  Semantics  +  Context

Model 2  (Chapters 7–10)
  Knowledge System =  KG  +  Acquisition  +  Inference  +  Validation  +  Evolution
```

These are **engineering learning models** — not universally accepted formal definitions. The book clearly separates pedagogical constructs from authoritative standards (W3C RDF, OWL 2, SPARQL, SHACL).

---

## Chapters

| # | Title | Core Question |
|:-:|-------|---------------|
| 1 | **From Graph to Knowledge** | What turns a graph into a *knowledge* graph? |
| 2 | **Data Models & Query Languages** | RDF triples vs. Property Graphs — how do we represent and query knowledge? |
| 3 | **Schema, Identity, and Context** | How do we model identity, ambiguity, and provenance? |
| 4 | **Ontologies and Formal Meaning** | How do ontologies give machine-readable meaning to data? |
| 5 | **Deduction, Rules, and Validation** | Inference (RDFS/OWL/Datalog) vs. Validation (SHACL) — what's the difference? |
| 6 | **Claims, Evidence, and Contradiction** | How do we handle competing, temporal, uncertain claims? |
| 7 | **Knowledge Acquisition & Integration** | How does raw data become governed knowledge? |
| 8 | **Inductive Knowledge & Graph Learning** | KG embeddings, GNNs, link prediction — and why prediction ≠ truth |
| 9 | **Retrieval, QA, and GraphRAG** | How do we ground LLMs with structured graph evidence? |
| 10 | **System Governance & Operation** | How do we build a self-sustaining, trustworthy knowledge system? |

The book concludes with an **Afterword** exploring societal authority, multi-agent epistemic governance, and future paradigm shifts.

---

## Theoretical Depth

The monograph is not a survey — it builds theory from the ground up across six pillars:

| Pillar | Chapters | Key Formalisms |
|--------|:--------:|----------------|
| Structural Foundations & Identity | 1–3 | Directed hypergraphs, LPG 7-tuple, blank node model theory, lean graph NP-hardness |
| Logic & Fixpoint Semantics | 4–5 | Description Logics decidability, DL-Lite FOL-rewritability, Datalog fixpoint semantics, stratified negation |
| Epistemics & Belief Revision | 6–7 | Dempster-Shafer evidence theory, Subjective Logic, bitemporal modeling, AGM belief revision |
| Graph Representation Learning | 8 | TransE/RotatE/ComplEx, Poincaré embeddings, 1-WL expressiveness bounds, GNN message passing |
| Retrieval & GraphRAG Bounds | 9 | Path explosion analysis, multi-hop error cascading, Personalized PageRank, Steiner tree approximation |
| Cybernetic Stability | 10 | Delayed feedback control, DDE stability, knowledge entropy, autophagous model collapse |

---

## Editions

The book is maintained in two parallel editions:

- **Vietnamese (Canonical):** [`book/`](book/) — 434 print pages. Full manuscript with front matter, all 10 chapters, afterword, glossary, and bibliography.
- **English:** [`book-en/`](book-en/) — 412 print pages. All 10 chapters with 100% structural and mathematical parity. Supplementary materials (glossary, bibliography, introduction, afterword) are in progress.

Both editions are compiled using XeLaTeX via an automated build pipeline.

---

## Repository Structure

```
├── book/                   # Vietnamese manuscript (canonical)
│   ├── chapter01–10.md     # Main content
│   ├── glossary.md         # 750+ term glossary
│   ├── references.bib      # Full bibliography
│   └── figures/            # TikZ diagrams (source + compiled PDF)
├── book-en/                # English manuscript
│   ├── chapter01–10.md     # 100% parity with Vietnamese chapters
│   └── figures/
├── chapter01–04/           # Runnable Python experiments & tests
├── capstone/               # Mechanism Knowledge Graph capstone system
├── datasets/               # Running datasets (e.g. rate_of_change.ttl)
├── tests/                  # Structural & pedagogical integrity tests
├── docs/                   # Specifications, semantic contracts, research notes
├── scripts/                # Build & verification pipeline
└── dist/                   # Built PDFs (gitignored; attached to Releases)
```

---

## Getting Started

### Prerequisites

- **Python 3.12+**
- **Docker** (optional — for Neo4j Cypher exercises)
- **Pandoc + XeLaTeX** (only for building PDFs)

### Quick Start

```bash
git clone https://github.com/MinhTuan76800310/knowledge_graph_learning-journey.git
cd knowledge_graph_learning-journey
pip install -e .
pytest                    # 144 tests
```

### Running Experiments

```bash
python chapter01/exp_1_1_plain_graph.py
python chapter02/exp_2_1_rdf_first_principles.py
python chapter02/exp_2_4_mechanism_turtle_sparql.py
```

### Building PDFs

```bash
make book                           # Vietnamese edition
LANG=en bash scripts/build_book.sh  # English edition
make book-check                     # Verify built PDF
```

---

## Testing

```bash
pytest                  # All 144 tests
ruff check .            # Lint
ruff format --check .   # Format verification
```

The test suite covers:

- **Empirical experiments** — graph models, SPARQL queries, RDFS entailment, OWL reasoning
- **Structural integrity** — Markdown headings, LaTeX math, section structure
- **Pedagogical progression** — concept dependency ordering across chapters
- **Source & citation integrity** — source index validation, research note links

---

## Release History

| Version | Date | Highlights |
|:-------:|:----:|------------|
| **v0.3.0** | 2026-09-07 | Complete bilingual monograph (434 pp VI + 412 pp EN) with 6 frontier theoretical pillars |
| **v0.2.0** | 2026-09-02 | English edition inception (Ch 1–3) + Vietnamese Ch 3 deep rework |
| **v0.1.0** | 2026-08-31 | Complete Vietnamese manuscript baseline (Ch 1–10, 358 pages) |

Detailed per-section tracking: [`docs/BOOK_STATUS.md`](docs/BOOK_STATUS.md)

---

## Contributing

Contributions, feedback, and semantic reviews are welcome.

- Read [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.
- Review [`docs/BOOK_PEDAGOGY.md`](docs/BOOK_PEDAGOGY.md) before proposing chapter changes.
- **Semantic corrections** (fixing inference rules, complexity bounds, or proofs) are top priority.

---

## Citation

```bibtex
@book{nguyen2026knowledgegraph,
  title     = {Knowledge Graph: From Graph to Living Knowledge Systems},
  author    = {Nguyen, Minh Tuan},
  year      = {2026},
  publisher = {Open Source Monograph},
  url       = {https://github.com/MinhTuan76800310/knowledge_graph_learning-journey},
  note      = {v0.3.0 — 434 pp. (Vietnamese), 412 pp. (English)}
}
```

---

## Author

Created by [**Nguyen Minh Tuan**](https://github.com/MinhTuan76800310) as an open learning journey in Knowledge Graphs, Neuro-Symbolic AI, and Autonomous Multi-Agent Systems.

**License:** [GPL-3.0-or-later](LICENSE)
