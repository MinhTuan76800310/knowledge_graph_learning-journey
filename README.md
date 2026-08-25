# Knowledge Graph Book

An open-source executable textbook: **Knowledge Graphs from first principles to production knowledge systems**.

Written in Vietnamese with English technical terminology preserved on first occurrence.

## What this book is

This is not a Neo4j tutorial or a GraphRAG cookbook. It is a mechanism-level exploration of what turns data into knowledge that a machine can represent, query, reason about, validate, update, and use.

The reader is an experienced software engineer who wants to understand Knowledge Graphs deeply enough to design custom knowledge systems for AI agents.

## Pedagogical model

Inspired by the structure and learning philosophy of `bojieli/ai-agent-book`:

- One unifying abstraction that evolves across chapters
- Progressive difficulty with explicit scaffolding
- Theory paired with runnable experiments at every stage
- Difficulty-rated experiments (★ beginner / ★★ intermediate / ★★★ research/design)
- Thought questions that require reasoning, not recall
- Reproducible environments via `uv` and Docker
- Chapter-level README files with experiment status
- Source-backed technical writing with traceable citations

## Two mental models

**Mental Model 1** (introduced in Chapter 1):

```
Knowledge Graph = Data Graph + Semantics + Context
```

**Mental Model 2** (emerges gradually, becomes capstone architecture):

```
Knowledge System = Knowledge Graph + Acquisition + Inference + Validation + Evolution
```

These are engineering learning models, not universally accepted formal definitions.

## Chapters

| # | Title | Core Question |
|---|-------|---------------|
| 1 | From Graph to Knowledge | What makes a graph a *knowledge* graph? |
| 2 | Data Models and Query Languages | How do we represent and query graphs? |
| 3 | Schema, Identity, and Context | How do we model identity and meaning? |
| 4 | Ontologies and Formal Meaning | How do we give machine-readable meaning? |
| 5 | Deduction, Rules, and Validation | How do we infer and validate? |
| 6 | Claims, Evidence, Provenance, Time, and Contradiction | How do we handle competing claims? |
| 7 | Knowledge Acquisition and Integration | How do we acquire knowledge without blind trust? |
| 8 | Inductive Knowledge and Learning from Graphs | How do graphs learn patterns? |
| 9 | Retrieval, Question Answering, and GraphRAG | How do we retrieve knowledge for humans and LLMs? |
| 10 | Building a Living Knowledge System | How do we design a living knowledge system? |

## Repository structure

```
knowledge-graph-book/
├── README.md              # This file
├── CLAUDE.md              # AI assistant conventions
├── AGENTS.md              # Subagent guidelines
├── pyproject.toml         # Python project configuration
├── uv.lock                # Pinned dependencies
├── docker-compose.yml     # Neo4j and optional services
├── book/                  # Main text (Vietnamese)
│   ├── introduction.md
│   ├── chapter01.md ... chapter10.md
│   └── images/
├── chapter01/ ... chapter10/  # Per-chapter experiments
│   └── README.md
├── common/                # Shared utilities
│   ├── graph/
│   ├── rdf/
│   ├── neo4j/
│   ├── datasets/
│   └── visualization/
├── datasets/              # Toy and capstone datasets
│   ├── toy/
│   └── mechanism_kg/
├── docs/                  # Research artifacts and meta-docs
│   ├── SOURCES.md
│   ├── SOURCE_MATRIX.md
│   ├── RESEARCH_LOG.md
│   ├── CURRICULUM_RATIONALE.md
│   ├── LEARNING_PATH.md
│   ├── EXPERIMENT_STATUS.md
│   ├── GLOSSARY.md
│   └── DESIGN_DECISIONS.md
└── capstone/
    └── mechanism_knowledge_system/
```

## Getting started

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Docker (for Neo4j experiments)

### Setup

```bash
# Clone the repository
git clone <repo-url>
cd knowledge-graph-book

# Install dependencies
uv sync

# Start Neo4j (optional, needed from Chapter 2)
docker compose up -d

# Run Chapter 1 experiments
cd chapter01
python exp_1_1_plain_graph.py
```

See each chapter's `README.md` for specific setup and run instructions.

## Engineering constraints

- **Language**: Python 3.12+
- **Package manager**: uv
- **Testing**: pytest
- **Linting**: ruff
- **Type checking**: type hints throughout
- **Reproducibility**: pinned dependencies via `uv.lock`
- **Local-first**: most experiments run on an Ubuntu laptop without cloud services

## Writing conventions

- Main text in Vietnamese
- Technical terms in English on first occurrence: "thực thể (entity)", "suy diễn (inference)"
- Tone: technically precise, mechanism-oriented, no marketing language
- Every major abstraction answers: what problem, what mechanism, what information, what assumptions, what can/cannot be inferred, what breaks, how to verify

## Copyright and citation

This repository contains **original writing**. All external sources are cited and traceable. No substantial passages are copied from textbooks, standards, courses, or other repositories.

See `docs/SOURCES.md` for the complete source registry and `docs/SOURCE_MATRIX.md` for topic-to-source mapping.

## License

TBD — will be selected before public release. All third-party code included only after license verification.

## Status

**Phase 1 in progress.** Currently building Chapter 1 and its experiments. See `docs/PHASE1_REPORT.md` (when available) for current milestone status.

</parameter>