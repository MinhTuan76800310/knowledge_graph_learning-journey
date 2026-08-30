# Book Status — v0.2

Tracks the publication state of each manuscript section. State definitions are in
`docs/BOOK_V0_1_MILESTONE.md`. Experiments do **not** gate chapter acceptance unless an
experiment is required to validate an important technical claim.

Last updated: 2026-08-31 (Chapter 9 drafted, PDF built)

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
| 9 — Retrieval, Question Answering, and GraphRAG | ✅ | ✅ | ✅ | 🔲 | ✅ | DRAFTED |
| 10 — Building a Living Knowledge System | 🔲 | 🔲 | 🔲 | 🔲 | 🔲 | NOT_STARTED |

## Back matter

| Section | Draft | Editorial | PDF | Status |
|---------|-------|-----------|-----|--------|
| Afterword | 🔲 | 🔲 | 🔲 | NOT_STARTED |
| Glossary | ✅ | ✅ | ✅ | ACCEPTED |
| Bibliography | ✅ | ✅ | ✅ | ACCEPTED |

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
- Chapter 9 (DRAFTED, 2026-08-31) is recorded in `docs/CHAPTER09_BOOK_CHECKPOINT.md`
  and `docs/CHAPTER09_DEPTH_REVIEW.md`. Semantic review 75/75 PASS; depth review PASS;
  capability test Q01–Q50 ALL = YES; PDF verified (322 print pages, Ch9 = pp. 251–322);
  branch `chapter09-retrieval-qa-graphrag` pending PR.
- Chapters 5–10 are written sequentially after the Ch4 checkpoint, following the
  book-first workflow in `docs/BOOK_V0_1_MILESTONE.md`.
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
