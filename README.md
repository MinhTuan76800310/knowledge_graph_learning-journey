# Knowledge Graph: Từ Đồ thị đến Hệ thống Tri thức

[![release](https://img.shields.io/github/v/release/MinhTuan76800310/knowledge_graph_learning-journey?label=release&color=blue)](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/latest)
[![license: GPL-3.0-or-later](https://img.shields.io/badge/license-GPL--3.0--or--later-blue)](LICENSE)
[![language: Vietnamese](https://img.shields.io/badge/lang-vi-green)](#editions)
[![language: English](https://img.shields.io/badge/lang-en-yellowgreen)](#editions)
[![pages: 364 vi · 70 en](https://img.shields.io/badge/pages-364_vi%20%C2%B7%2070_en-lightgrey)](#editions)

> **An open-source, executable, bilingual textbook.** Knowledge Graphs from first
> principles to production knowledge systems — explained at the mechanism level, with
> runnable experiments and traceable citations. Written in **Vietnamese** (canonical,
> complete) with an **English** edition in progress.

**Latest release:** [`v0.2.0`](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/tag/v0.2.0)
— complete Vietnamese book (364 pages) + English edition, Chapters 1–3 (70 pages).

**License:** [GPL-3.0-or-later](LICENSE)

> Badges above are all verifiable today. There is deliberately **no CI badge**: the
> pipeline is still planned (see [Project status](#project-status)), and a build-passing
> badge would contradict the book's own epistemic-honesty rule.

---

## The two ideas this book is built on

```text
Mental Model 1  (introduced in Chapter 1)
  Knowledge Graph  =  Data Graph  +  Semantics  +  Context

Mental Model 2  (emerges gradually; capstone architecture in Chapter 10)
  Knowledge System =  Knowledge Graph
                      + Acquisition + Inference + Validation + Evolution
```

These are **engineering learning models**, not universally accepted formal definitions.
The book is explicit about the distinction between book-defined models and external
standards.

---

## Table of contents

- [The two ideas this book is built on](#the-two-ideas-this-book-is-built-on)
- [What this book is](#what-this-book-is)
- [Editions](#editions)
- [Chapters](#chapters)
- [Repository structure](#repository-structure)
- [Getting started](#getting-started)
- [Building the PDF book](#building-the-pdf-book)
- [Testing and validation](#testing-and-validation)
- [Project status](#project-status)
- [Writing conventions](#writing-conventions)
- [Contributing](#contributing)
- [About the author](#about-the-author)
- [Copyright, sources, citation](#copyright-sources-citation)

---

## What this book is

This is **not** a Neo4j tutorial or a GraphRAG cookbook. It is a mechanism-level
exploration of what turns data into knowledge that a machine can represent, query,
reason about, validate, update, and use.

The reader is an experienced software engineer who wants to understand Knowledge Graphs
deeply enough to design custom knowledge systems for AI agents — not merely to call an
API.

The book is written in **Vietnamese**, with English technical terms preserved on first
occurrence ("thực thể (entity)", "suy diễn (inference)"). Self-contained chapters
document the OWL/RDF/SHACL/SPARQL and related primitives on first use. An **English
edition** is being produced in parallel, chapter by chapter, from the Vietnamese
canonical text.

## Editions

| Edition | Language | Scope | Status |
|---------|----------|-------|--------|
| **Vietnamese** (canonical) | `vi` | Front matter + Chapters 1–10 + Afterword + Glossary (226 terms) + Bibliography (92 sources) | ✅ Complete — 364 print pages |
| **English** | `en` | Chapters 1–3 (Schema, Identity, and Context through Chapter 3) | 🚧 In progress — 70 print pages |

The Vietnamese text is the source of truth; the English edition mirrors it and is kept in
parity chapter by chapter. Every chapter passed an independent acceptance gate before
merge: semantic contracts, depth review, reader-capability test, citation/glossary/registry
integrity, and a clean PDF build. Details per chapter live in
`docs/CHAPTER*nn*_BOOK_CHECKPOINT.md`.

Download the release PDFs:

```text
Vietnamese (complete):
  https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/download/v0.2.0/knowledge-graph-book-v0.2.0.pdf

English (Chapters 1–3):
  https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/download/v0.2.0/knowledge-graph-book-en-v0.2.0.pdf
```

## Chapters

| # | Title | Core Question |
|---|-------|---------------|
| 1 | From Graph to Knowledge | What makes a graph a *knowledge* graph? |
| 2 | Data Models and Query Languages | How do we represent and query graphs? (RDF/SPARQL, Property Graph/Cypher) |
| 3 | Schema, Identity, and Context | How do we model identity and meaning? |
| 4 | Ontologies and Formal Meaning | How do we give machine-readable meaning? (RDFS, OWL, DL) |
| 5 | Deduction, Rules, and Validation | How do we infer and validate? (SHACL, rules) |
| 6 | Claims, Evidence, Provenance, Time, Contradiction | How do we handle competing claims? (epistemic model) |
| 7 | Knowledge Acquisition and Integration | How do we acquire knowledge without blind trust? |
| 8 | Inductive Knowledge and Learning from Graphs | How do graphs learn patterns? (KGE, GNN) |
| 9 | Retrieval, Question Answering, GraphRAG | How do we retrieve knowledge for humans and LLMs? |
| 10 | Building a Living Knowledge System | How do we design a living, trustworthy knowledge system? |

Each chapter closes by motivating the next. The book ends with an **Afterword (Lời bạt)**
that opens the frontier (authority, human oversight, cost, multi-agent governance,
paradigm shifts, societal trust).

## Repository structure

```
knowledge_graph_learning-journey/
├── README.md               # This file
├── CLAUDE.md               # AI-assistant working conventions
├── AGENTS.md               # Subagent guidelines
├── pyproject.toml          # Python project configuration (>=3.12)
├── uv.lock                 # Pinned dependencies
├── Makefile                # make book / book-check / book-clean
├── docker-compose.yml      # Neo4j for Chapter 2 experiments
├── book/                   # Canonical text (Vietnamese)
│   ├── preface.md, how-to-use.md, introduction.md
│   ├── chapter01.md ... chapter10.md, afterword.md
│   ├── glossary.md, references.bib, book-manifest.yaml, metadata.yaml
│   └── figures/            # TikZ + Mermaid sources and generated PDFs
├── book-en/                # English edition (in progress)
│   ├── chapter01.md ... chapter03.md
│   ├── book-manifest.yaml, metadata.yaml
│   └── figures/            # English figure sources
├── chapter01/ ... chapter02/   # Per-chapter runnable experiments + tests
├── capstone/               # Mechanism Knowledge Graph capstone project
├── datasets/               # Toy and capstone datasets
├── tests/                  # Book-level integrity tests (chapters 8–10, repo)
├── docs/                   # Research artifacts & meta-docs
│   ├── BOOK_STATUS.md      # Per-section acceptance state
│   ├── BOOK_PEDAGOGY.md    # Canonical writing policy
│   ├── BOOK_V0_1_MILESTONE.md
│   ├── source_index.json   # 92 registered sources (machine-readable)
│   ├── research_notes/     # Per-source verification notes
│   ├── CITATION_MAP.md
│   └── CHAPTER*nn*_*.md    # Contracts / checkpoints / depth reviews
├── scripts/                # PDF build pipeline (pandoc + LuaLaTeX)
└── dist/                   # Built PDFs (gitignored; attach to Releases)
```

## Getting started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Docker (for the optional Neo4j experiments in Chapter 2)
- Pandoc + LuaLaTeX (only if you want to build the PDF; see below)

### Setup

```bash
# Clone the repository
git clone https://github.com/MinhTuan76800310/knowledge_graph_learning-journey.git
cd knowledge_graph_learning-journey

# Install dependencies
uv sync

# Start Neo4j (optional; needed for Chapter 2 LAB exercises)
docker compose up -d

# Run the test suite
uv run pytest

# Run Chapter 1 experiments
cd chapter01
uv run python exp_1_1_plain_graph.py
```

See each experiment directory's `README.md` (where present) for specific instructions.
The book's main argument is readable **without** running any code — experiments are
companions, not prerequisites (see `docs/BOOK_V0_1_MILESTONE.md`).

## Building the PDF book

The PDF build pipeline lives in `scripts/` and requires **pandoc**, **LuaLaTeX** and the
TeX packages in `book/header.tex`. Building also pre-renders TikZ figures, so a TeX
distribution with the `tikz`/`pgfplots` packages is required.

```bash
# Vietnamese (canonical) — build print + screen PDFs into dist/
make book

# Build, then run the automated PDF verification gate
make book-check

# English edition — same pipeline, switched by LANG=en
LANG=en bash scripts/build_book.sh
LANG=en bash scripts/verify_book_pdf.sh

# Clean build artifacts
make book-clean
```

Outputs land in `dist/` (gitignored). For releases, the versioned PDFs are attached to a
GitHub Release — see the [releases page](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases).

## Testing and validation

The repository is validated by both automated integrity tests and per-chapter human
acceptance audits:

```bash
uv run pytest            # 106 tests: book integrity + chapter experiments
uv run ruff check .      # 0 errors
uv run ruff format --check .
```

What the tests cover:

- `tests/test_book_integrity.py` — book-wide structure
- `tests/test_book_concept_dependencies.py` — concept ordering across chapters
- `tests/test_chapter08_integrity.py` / `test_chapter09_integrity.py` /
  `test_chapter10_integrity.py` — sections, figures, citations, glossary, registry
- `tests/test_repo_integrity.py` — source index, research notes, no leaked artifacts
- `chapter01/test_experiments.py` & `chapter02/test_ch2_experiments.py` — runnable labs

**Note on correctness:** passing tests does *not* prove semantic correctness. Every
chapter additionally passes a human/independent acceptance gate (semantic contracts,
depth review, reader-capability test) before it is marked ACCEPTED.

## Project status

| Milestone | State |
|-----------|-------|
| **v0.2.0** — English edition begins (Ch1–3) + Vietnamese Ch3 quality pass | ✅ **RELEASED** (2026-09-02, tag `v0.2.0`) |
| **v0.1.0** — complete Vietnamese book (Ch1–10 + Afterword) | ✅ RELEASED (2026-08-31, tag `v0.1.0`) |
| Vietnamese Chapters 1–10 + Afterword | ✅ ACCEPTED via independent audits |
| English Chapters 1–3 | ✅ merged, in parity with Vietnamese |
| English Chapters 4–10 | ⏳ planned |
| Experiments | Chapter 1–2 runnable; Chapter 3–10 labs deferred to `docs/LAB_BACKLOG.md` |
| CI pipeline | ⏳ planned (local `make book-check` + `uv run pytest` today) |

Current per-section state is tracked in [`docs/BOOK_STATUS.md`](docs/BOOK_STATUS.md).

## Writing conventions

- **Canonical text in Vietnamese**; technical terms in English on first occurrence. The
  English edition is a faithful parallel translation, kept in parity chapter by chapter.
- **Mechanism-first tone**: every major abstraction answers — what problem, what
  mechanism, what information, what assumptions, what can/cannot be inferred, what
  breaks, how to verify.
- **Epistemic discipline**: fact / claim / assertion / assumption / inference /
  prediction / book-defined model are clearly distinguished.
- **Source-backed**: important factual/formal claims carry reader-facing citations to
  the 92 registered sources (`docs/source_index.json`); book-defined models are labeled
  `BOOK-DEFINED`, never presented as standards.
- **Example continuity**: one recurring capstone domain (the Mechanism Knowledge Graph)
  rather than many unrelated toy domains.

## Contributing

Contributions are welcome — especially **semantic corrections**, which the author treats
as the highest-priority feedback and acts on first.

The project follows a traceable workflow, documented in [`CLAUDE.md`](CLAUDE.md) and
[`AGENTS.md`](AGENTS.md):

```text
Issue → Branch → Commits → PR → Validate → Merge
```

How to help:

- **Report an error or gap** — open an [issue](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/issues)
  pointing to the chapter/section and, where relevant, the registered source it conflicts
  with.
- **Propose a change** — branch from `main`, keep one coherent change per branch, and open
  a PR to `main`. Run `uv run pytest`, `uv run ruff check .`, and (for manuscript changes)
  `make book-check` before requesting review.
- **Contribute to the English edition** — Chapters 4–10 are open; each translation must
  preserve parity with the Vietnamese canonical text and pass the same acceptance gate.

Before writing for this book, read [`docs/BOOK_PEDAGOGY.md`](docs/BOOK_PEDAGOGY.md) — it is
the canonical writing policy (mechanism-first tone, epistemic discipline, source
traceability).

## About the author

This book is an open, public **learning journey** by
[**MinhTuan76800310**](https://github.com/MinhTuan76800310) — a software engineer
building it from first principles, chapter by chapter, in Vietnamese with an English
edition in parallel.

The project values are explicit in the writing:

- Understand the **mechanism**, not only the API.
- Be **epistemically honest**: distinguish what is known, what is believed, and what is
  book-defined.
- Keep everything **verifiable**: every external claim traces to a registered source;
  every chapter passes an independent acceptance audit.

## Copyright, sources, citation

This repository contains **original writing**. No substantial passages are copied from
textbooks, standards, courses, or other repositories; all external content is cited and
traceable.

- Machine-readable source registry: [`docs/source_index.json`](docs/source_index.json)
- BibTeX bibliography: [`book/references.bib`](book/references.bib)
- Topic-to-source map: [`docs/CITATION_MAP.md`](docs/CITATION_MAP.md)

**License:** [GPL-3.0-or-later](LICENSE) — you are free to read, print, and share the
book, provided derivative works remain under the same license.

To cite this book (work-in-progress), you may use the repository itself:

```bibtex
@misc{knowledgeGraphLearningJourney,
  title  = {Knowledge Graph: Từ Đồ thị đến Hệ thống Tri thức},
  author = {Nguyen, Minh Tuan},
  year   = {2026},
  url    = {https://github.com/MinhTuan76800310/knowledge_graph_learning-journey}
}
```
