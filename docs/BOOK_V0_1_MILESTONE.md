# Book v0.1 Milestone — Complete Printable Book, Chapters 1–10

**Milestone goal:** Produce a complete, printable, publication-quality PDF book covering
the Introduction and Chapters 1–10, plus Glossary and Bibliography.

**Priority rule:** `BOOK QUALITY > LAB COMPLETENESS`. Experiments are secondary and must
not block chapter acceptance. Research correctness remains non-negotiable — semantic
correctness is never sacrificed for speed.

---

## Deliverables

The manuscript must include, in order:

1. Title page
2. Preface
3. How to use this book
4. Introduction
5. Chapter 1 — From Graph to Knowledge
6. Chapter 2 — Data Models and Query Languages
7. Chapter 3 — Schema, Identity, and Context
8. Chapter 4 — Ontologies and Formal Meaning
9. Chapter 5 — Deduction, Rules, and Validation
10. Chapter 6 — Claims, Evidence, Provenance, Time, and Contradiction
11. Chapter 7 — Knowledge Acquisition and Integration
12. Chapter 8 — Inductive Knowledge and Learning from Graphs
13. Chapter 9 — Retrieval, Question Answering, and GraphRAG
14. Chapter 10 — Building a Living Knowledge System
15. Afterword
16. Glossary
17. Bibliography

Optional: a Lab Companion appendix linking to deferred experiments in
`docs/LAB_BACKLOG.md`.

---

## Chapter state machine

Each chapter advances through these states, in order:

| State | Meaning |
|-------|---------|
| `RESEARCHING` | Primary sources being fetched and verified into `docs/source_index.json` / research notes. |
| `OUTLINED` | Source-backed outline exists; central mechanism identified. |
| `DRAFTED` | Full prose draft exists in `book/`. |
| `SEMANTICALLY_REVIEWED` | Factual/formal claims checked against sources; epistemic labels applied. |
| `EDITORIALLY_REVIEWED` | Readability, structure, opening map, thought questions, transitions done. |
| `PDF_VERIFIED` | Chapter builds into the PDF and passes the verification gate. |
| `ACCEPTED` | Chapter meets the full quality bar and is frozen for v0.1. |

Current state per chapter is tracked in `docs/BOOK_STATUS.md`.

---

## Acceptance rule: experiments do not gate chapters

A chapter may be `ACCEPTED` without its experiments being implemented, **unless** an
experiment is required to validate an important technical claim in the prose. Deferred
experiments are logged in `docs/LAB_BACKLOG.md` with status `DEFERRED_UNTIL_BOOK_V0.1`.

---

## Chapter quality bar

A chapter is accepted only if it satisfies all of:

- **Conceptual coherence** — one clear question, one clear progression.
- **Mechanistic depth** — the reader understands *why* something works, not only *what*
  the API is.
- **Formal precision** — formal definitions are correct and clearly distinguished from
  book-defined mental models.
- **Example continuity** — prefer one recurring example over many unrelated toy domains.
- **Comparative understanding** — design alternatives and trade-offs are explained.
- **Epistemic discipline** — fact / claim / assertion / assumption / inference /
  prediction / book-defined model are clearly distinguished.
- **Readability** — a software engineer can read it offline without opening the repo.
- **Independence from labs** — the main argument is understandable without running code.
- **Sources** — important factual/formal claims carry reader-facing citations.
- **Transition** — the chapter ends by motivating the next chapter.

Do **not** optimize for page count. Every section must earn its place by helping answer
the chapter's central question.

---

## Book-first writing workflow (Chapters 3–10)

For each chapter, in order:

1. Research map
2. Source-backed outline
3. Identify the chapter's single central mechanism
4. Draft manuscript
5. Semantic correctness pass
6. Cross-chapter consistency pass
7. Editorial / readability pass
8. Original diagrams
9. Thought questions
10. Build PDF and inspect
11. Mark chapter `ACCEPTED`

Do not implement chapter experiments during this sequence unless one is genuinely
necessary to resolve an uncertain technical claim. Instead, create/update lab backlog
entries.

---

## Publication pipeline

The PDF build pipeline lives in `scripts/` and is driven by `make book` /
`make book-check`. See `docs/BOOK_PREVIEW_CHECKPOINT.md` for the current build evidence.
Generated PDFs go to `dist/` (gitignored); they are not committed to normal history.
