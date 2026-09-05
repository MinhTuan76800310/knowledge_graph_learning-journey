# Book Status — v0.2

Tracks the publication state of each manuscript section. State definitions are in
`docs/BOOK_V0_1_MILESTONE.md`. Experiments do **not** gate chapter acceptance unless an
experiment is required to validate an important technical claim.

Last updated: 2026-09-05 (**v0.2.0 RELEASED**: tag `v0.2.0`; Vietnamese complete book
`knowledge-graph-book-v0.2.0.pdf`, 364 print pages + English edition
`knowledge-graph-book-en-v0.2.0.pdf`, 70 print pages, Ch1–3. Delta over v0.1.0: English
edition launched (Ch1–3, PRs #27/#30/#40) + Vietnamese Chapter 3 quality pass (#42).
Prior: v0.1.0 @ aa91115, 358 print pages, full Vietnamese book = front matter + Ch1–10 +
Afterword + Glossary + Bibliography)

## Front matter

| Section | Draft | Editorial | PDF | Status |
|---------|-------|-----------|-----|--------|
| Title page | ✅ | ✅ | ✅ | ACCEPTED |
| Preface | ✅ | ✅ | ✅ | ACCEPTED |
| How to use this book | ✅ | ✅ | ✅ | ACCEPTED |
| Introduction | ✅ | ✅ | ✅ | ACCEPTED |

## Chapters

| Chapter | Research | Draft | Semantic review | Editorial review | PDF | Status |
|---------|----------|-------|-----------------|------------------|-----|--------|
| 1 — From Graph to Knowledge | ✅ | ✅ | ✅ | ✅ | ✅ | ACCEPTED |
| 2 — Data Models and Query Languages | ✅ | ✅ | ✅ | ✅ | ✅ | ACCEPTED |
| 3 — Schema, Identity, and Context | ✅ | ✅ | ✅ | ✅ | ✅ | ACCEPTED |
| 4 — Ontologies and Formal Meaning | ✅ | ✅ | ✅ | ✅ | ✅ | ACCEPTED |
| 5 — Deduction, Rules, and Validation | ✅ | ✅ | ✅ | ✅ | ✅ | ACCEPTED |
| 6 — Claims, Evidence, Provenance, Time, Contradiction | ✅ | ✅ | ✅ | ✅ | ✅ | ACCEPTED |
| 7 — Knowledge Acquisition and Integration | ✅ | ✅ | ✅ | ✅ | ✅ | ACCEPTED |
| 8 — Inductive Knowledge and Learning from Graphs | ✅ | ✅ | ✅ | ✅ | ✅ | ACCEPTED |
| 9 — Retrieval, Question Answering, and GraphRAG | ✅ | ✅ | ✅ | ✅ | ✅ | ACCEPTED |
| 10 — Building a Living Knowledge System | ✅ | ✅ | ✅ | ✅ | ✅ | ACCEPTED |

## Back matter

| Section | Draft | Editorial | PDF | Status |
|---------|-------|-----------|-----|--------|
| Afterword | ✅ | ✅ | ✅ | ACCEPTED |
| Glossary | ✅ | ✅ | ✅ | ACCEPTED |
| Bibliography | ✅ | ✅ | ✅ | ACCEPTED |

## English edition (`book-en/`)

The English edition is a parallel translation of the Vietnamese canonical text, produced
chapter by chapter and kept in parity. It builds with `LANG=en`.

| Chapter | Translated | Accuracy audit | PDF | Status |
|---------|-----------|----------------|-----|--------|
| 1 — From Graph to Knowledge | ✅ | ✅ (Issue #31) | ✅ | MERGED (PR #27) |
| 2 — Data Models and Query Languages | ✅ | ✅ (Issue #31) | ✅ | MERGED (PR #30) |
| 3 — Schema, Identity, and Context | ✅ | ✅ (parity with VI #42) | ✅ | MERGED (PR #40) |
| 4 — Ontologies and Formal Meaning | ✅ | ✅ (Pillar 2, PR #68) | ✅ | MERGED (PR #59/#68) |
| 5 — Deduction, Rules, and Validation | ✅ | ✅ (Pillar 2, PR #70) | ✅ | MERGED (PR #62/#70) |
| 6 — Claims, Evidence, Provenance, Time, Contradiction | ✅ | ✅ (Pillar 3, parity with VI) | ✅ | MERGED (PR #72) |
| 7 — Knowledge Acquisition and Integration | ✅ | ✅ (Pillar 3, parity with VI) | ✅ | MERGED (PR #74) |
| 8 — Inductive Knowledge and Learning from Graphs | ✅ | 🔄 (Pillar 4, parity with VI, this branch) | 🔲 | PR pending (branch `en-vi-ch8-pillar4`) |
| 9–10 | 🔲 |  | 🔲 | PLANNED |

English build verified at v0.2.0: 70 print pages, `verify_book_pdf.sh` (LANG=en) gate
PASSED.

## Upcoming: Book v0.3 Milestone (Theoretical Rigor & Frontier AI Upgrade)

Target specification is established in `docs/BOOK_V0_3_MILESTONE.md` based on DeepMind-standard technical audit.
Focus: 6 theoretical pillars (Hypergraphs, Logic Complexity & Decidability, Dempster-Shafer/AGM Epistemics, Weisfeiler-Lehman & RotatE Geometry, Combinatorial RAG Bounds, and Closed-loop Cybernetics).

| Theoretical Target | Target Chapters | Status | Specification |
|--------------------|-----------------|--------|---------------|
| Pillar 1: Hypergraphs & Formal Blank Node Logic | Ch 1–3 | 🟢 Ch 1–3 MERGED (PR #66) | `docs/BOOK_V0_3_MILESTONE.md` §Target 1 |
| Pillar 2: Complexity Landscape, FOL-Rewritability & Datalog | Ch 4–5 | 🟢 Ch 4 MERGED (PR #68); 🟢 Ch 5 MERGED (PR #70) | `docs/BOOK_V0_3_MILESTONE.md` §Target 2 |
| Pillar 3: Dempster-Shafer Confidence & AGM Belief Revision | Ch 6 | 🟢 Ch 6 MERGED (VI+EN parity, PR #72) | `docs/BOOK_V0_3_MILESTONE.md` §Target 3 |
| Pillar 4: Weisfeiler-Lehman (1-WL), RotatE & Hyperbolic Geometry | Ch 8 | 🔄 Ch 8 in PR (VI+EN parity, branch `en-vi-ch8-pillar4`) | `docs/BOOK_V0_3_MILESTONE.md` §Target 4 |
| Pillar 5: Path Explosion Bounds & Long-Context vs GraphRAG | Ch 9 | 🔲 PLANNED | `docs/BOOK_V0_3_MILESTONE.md` §Target 5 |
| Pillar 6: Closed-Loop Stability & Autophagous Model Collapse | Ch 10 | 🔲 PLANNED | `docs/BOOK_V0_3_MILESTONE.md` §Target 6 |

## Legend

- ✅ complete for the current milestone
- 🔲 not yet complete

## Notes

- Chapters 1–4 form the **Book Preview v0.3** deliverable (Introduction + Chapters 1–4 +
  Glossary + Bibliography, 74 PDF pages). They are complete and printable.
- Chapter 3 acceptance is recorded in `docs/CHAPTER03_BOOK_CHECKPOINT.md`.
- Chapter 4 acceptance is recorded in `docs/CHAPTER04_BOOK_CHECKPOINT.md`.
- Chapter 5 acceptance is recorded in `docs/CHAPTER05_BOOK_CHECKPOINT.md`.
- Chapter 6 acceptance is recorded in `docs/CHAPTER06_BOOK_CHECKPOINT.md`.
- Chapter 7 (ACCEPTED, 2026-08-30) is recorded in `docs/CHAPTER07_BOOK_CHECKPOINT.md`
  and `docs/CHAPTER07_DEPTH_REVIEW.md`. Semantic review 45/45 PASS; depth review PASS;
  capability test Q1–Q38 ALL = YES; PDF verified (214 print pages, Ch7 = physical
  pages 170–206).
- Chapter 8 (ACCEPTED, 2026-08-30) is recorded in `docs/CHAPTER08_BOOK_CHECKPOINT.md`
  and `docs/CHAPTER08_DEPTH_REVIEW.md`. Semantic review 60/60 PASS; depth review PASS;
  capability test Q1–Q40 ALL = YES; PDF verified (258 print pages, Ch8 = pp. 209–247);
  merged via PR #14 (commit f136ba1).
- Chapter 9 (ACCEPTED, 2026-08-31) is recorded in `docs/CHAPTER09_BOOK_CHECKPOINT.md`
  and `docs/CHAPTER09_DEPTH_REVIEW.md`. Semantic review 75/75 PASS; depth review PASS;
  capability test Q01–Q56 ALL = YES; PDF verified (322 print pages, Ch9 = pp. 251–322);
  merged via PR #18 (commit 0a1fca4).
- Chapter 10 (ACCEPTED, 2026-08-31) is recorded in `docs/CHAPTER10_BOOK_CHECKPOINT.md`.
  Independent acceptance audit: 212/213 criteria PASS (1 PARTIAL, 0 FAIL, 0 BLOCKER);
  depth table 47/47 concepts ≥4 (15 at depth 5); Mechanism-KG coverage >95%;
  capability test Q01–Q48 ALL = YES; PDF verified (356 print pages, Ch10 = pp. 310–336).
  3 MINOR findings fixed in commit d49a24f; merged via PR #21 (commit a415cec).
- Chapter 11 does not exist; the book closes with the Afterword (deliverable #15).
- Deferred lab work is tracked in `docs/LAB_BACKLOG.md` and does not block acceptance.
- **TikZ pilot experiment** (2026-08-29): 8 formal TikZ figures added to Ch4 (3) and Ch5 (5).
  Baseline preserved at tag `book-preview-v0.4-baseline-pre-tikz` (commit 103432b).
  Recommendation: adopt TikZ selectively for formal diagrams from Ch6 onward.
  Full report: `docs/TIKZ_PILOT_COMPARISON.md`.
- **Whole-book depth remediation** (2026-08-30): Chapters 1–6 remediated per
  `docs/BOOK_DEPTH_REMEDIATION_PLAN.md` and `docs/BOOK_CONCEPT_DEPTH_AUDIT.md`. Every
  audit row received a mechanism transfer; capability ladders standardized across all six
  chapters; 13 generated TikZ figures replaced the earlier 8 (Ch4–6). Verification:
  `docs/POST_REMEDIATION_AUDIT.md`. Chapters remain ACCEPTED; no content was cut.
- **PDF build notes (2026-08-30):** `scripts/build_book.sh` now copies generated PDF
  figures into `build/figures/generated/` so Pandoc resolves them; fixed two
  backtick-in-math LaTeX errors in Ch5 §5.2 ($G_1$, $G_2$ lines).
