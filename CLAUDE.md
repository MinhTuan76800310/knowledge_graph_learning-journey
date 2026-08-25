# CLAUDE.md — Knowledge Graph Book

## Project Overview

An open-source executable textbook on Knowledge Graphs, from first principles to production knowledge systems. Written in Vietnamese with English technical terminology. Target audience: experienced software engineers who want to understand KG mechanisms deeply enough to design custom knowledge systems for AI agents.

## Key Commands

```bash
# Install dependencies
uv sync

# Run all tests
uv run pytest

# Run Chapter 1 experiments
cd chapter01 && uv run python exp_1_1_plain_graph.py

# Lint
uv run ruff check .

# Format check
uv run ruff format --check .

# Type check
uv run mypy .

# Start Neo4j (for Ch2+ experiments)
docker compose up -d neo4j
```

## Architecture

- `book/` — Main book content (Vietnamese markdown)
- `chapterNN/` — Per-chapter experiments with README.md
- `common/` — Shared utilities (graph, rdf, neo4j, datasets, visualization)
- `datasets/` — Toy datasets and mechanism_kg evolving capstone data
- `docs/` — Research artifacts, source matrix, glossary, design decisions
- `capstone/mechanism_knowledge_system/` — Evolving capstone domain

## Conventions

- Python 3.12+, type hints required
- Experiments follow fixed template: Question → Hypothesis → Architecture → Run → Observe → Explain → Fail → Extend
- Difficulty: ★ beginner, ★★ intermediate, ★★★ research/design challenge
- Status: ✅ independently runnable, 📖 reproduction/external dependency, 🚧 design/research exercise
- Never mark ✅ without executing and capturing evidence
- Technical terms: English on first occurrence with Vietnamese gloss, e.g., "thực thể (entity)"
- Diagrams: Mermaid or generated SVG, never copyrighted figures
- All external claims must cite a source from docs/SOURCES.md

## Standards Version Policy

- Stable W3C Recommendations = main curriculum
- Candidate Recommendations / Working Drafts = clearly labeled "Current developments" callouts
- Never teach a draft as if it were stable
- As of 2026-08-25: RDF 1.2 is CR, SPARQL 1.2 is WD, SHACL 1.0 is stable REC, OWL 2 is stable REC, PROV-O is stable REC

## Copyright Rules

- ALL writing must be original. No copied passages from any source.
- Paraphrase and cite. Every external claim traceable to docs/SOURCES.md.
- Third-party code requires license verification and attribution.
- Hogan et al. (kgbook.org) is research reference only — no reproduced content.

</parameter>