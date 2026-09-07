# Contributing to Knowledge Graph Book

Thank you for your interest in contributing to **Knowledge Graph: From Graph to Living Knowledge Systems**!

This project is an open-source, bilingual (Vietnamese and English) technical monograph and executable curriculum. It is built to bridge formal knowledge engineering (RDF, OWL, Description Logics, SPARQL, SHACL) with modern frontier AI (Graph Machine Learning, GraphRAG, Neuro-Symbolic Agent Memory, and Cybernetic Feedback Loops).

---

## 🧭 Core Principles & Standards

Before proposing or contributing changes, please familiarize yourself with our fundamental guidelines:

1. **Epistemic Honesty:** We strictly distinguish between *facts*, *claims*, *assumptions*, *inferences*, *predictions*, and *book-defined models*. A book-defined mental model must never be passed off as an official W3C or ISO standard.
2. **Mechanism-First Explanations:** We do not simply list API calls or libraries. Every abstraction must explain:
   - What problem it solves
   - What underlying mechanism makes it work
   - What information is preserved or lost
   - What assumptions are made
   - What can and cannot be logically inferred
   - Where and how it fails
3. **No Plagiarism or Copied Prose:** Never copy text from textbooks, Wikipedia, papers, or documentation. Understand the source, formulate an original explanation, and cite the authoritative reference.
4. **Source Traceability:** Every factual or formal claim must trace back to an authoritative source in [`docs/source_index.json`](docs/source_index.json).
5. **Standards Conformance:** When implementing semantic algorithms (RDFS inference, OWL entailment, SHACL validation), implementations must conform to W3C specifications, not vice-versa. Passing tests only proves code matches the oracle; the oracle itself must match the standard.

---

## 🌐 Bilingual Parity Policy

The book is published in two parallel editions with 100% structural and pedagogical parity:
- `book/`: Vietnamese edition (canonical).
- `book-en/`: English edition.

**Parity Requirement:**
- Any change, correction, or addition to a chapter in `book/` must have an identical, corresponding change in `book-en/` (and vice-versa).
- Section headings, mathematical equations, code snippets, TikZ vector diagrams, pedagogical callout boxes, and references must remain perfectly aligned 1-to-1.

---

## 🛠️ Contribution Workflow

We follow standard GitHub trunk-based workflow:

```text
Issue → Branch → Commits → PR → Automated Validation → Merge
```

### 1. Open or Pick an Issue
- Check existing [GitHub Issues](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/issues) or open a new one describing the bug, semantic error, or proposed improvement.
- **Semantic corrections** (e.g., fixing a mischaracterized DL axiom, correcting an inference rule, or refining a complexity bound) receive top priority.

### 2. Create a Feature Branch
```bash
git checkout -b fix/ch04-dl-complexity-clarification
```

### 3. Make Atomic Commits
Use [Conventional Commits](https://www.conventionalcommits.org/) formatting:
- `docs: fix OWL 2 QL rewritability explanation in Ch4`
- `test: add semantic contract test for RDFS domain inference`
- `fix: correct typo in Subjective Logic fusion operator`

### 4. Run Quality Gates Locally

All quality checks must pass before opening or merging a PR:

```bash
# 1. Run the test suite (106 tests)
python -m pytest

# 2. Run Ruff linter and formatter checks
python -m ruff check .
python -m ruff format --check .

# 3. If manuscript prose was modified, verify PDF compilation gates
# Vietnamese edition
bash scripts/build_book.sh
bash scripts/verify_book_pdf.sh

# English edition
LANG=en bash scripts/build_book.sh
LANG=en bash scripts/verify_book_pdf.sh
```

### 5. Submit a Pull Request
- Target `main` as the base branch.
- Reference the related issue number (e.g., `Closes #85`).
- Provide a concise summary of changes and validation evidence.

---

## 📚 Essential Reading for Authors

- [`docs/BOOK_PEDAGOGY.md`](docs/BOOK_PEDAGOGY.md) — The canonical pedagogical guidelines.
- [`docs/CURRICULUM_RATIONALE.md`](docs/CURRICULUM_RATIONALE.md) — Logical sequencing of topics.
- [`docs/SOURCES.md`](docs/SOURCES.md) & [`docs/source_index.json`](docs/source_index.json) — Registered authoritative references.
- [`docs/BOOK_V0_4_ROADMAP.md`](docs/BOOK_V0_4_ROADMAP.md) — Next frontier research directions.
