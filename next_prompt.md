# Chapter 7 — ACCEPTED (2026-08-30)

Chapter 7 (Knowledge Acquisition and Integration / Thu nhận và Tích hợp Tri thức) has
passed the full acceptance gate: semantic review 45/45 PASS, depth review PASS
(25/25 semantic boundaries, all major concepts depth ≥4, Mechanism-KG coverage 85%),
reader capability test Q1–Q38 ALL = YES, editorial review clean, PDF verified.
Status: ACCEPTED.

## Current state

- Chapters 1–7 are ACCEPTED
- Book PDF builds to 214 pages (print) / 215 pages (screen); Chapter 7 = physical
  pages 170–206
- All tests pass: 73 passed
- `ruff check .` clean; `ruff format --check .` clean (128 files formatted)
- Semantic contracts: docs/CHAPTER07_SEMANTIC_CONTRACTS.md (45 records, all PASS)
- Depth review: docs/CHAPTER07_DEPTH_REVIEW.md (depth table, 25 semantic boundaries,
  capability test Q1–Q38, pipeline table)
- Manuscript: 37 sections (§7.0–§7.36), ~1900 lines
- 5 new TikZ figures (19 total in book), all compile
- 7 new sources registered (R2RML-01, DIRECT-MAP-01, CSVW-01, RL-01, SM-01, DI-01,
  HOGAN-CREATE-01) — all FETCHED_AND_VERIFIED
- Checkpoint: docs/CHAPTER07_BOOK_CHECKPOINT.md

## Key design decisions (Chapter 7)

- Acquisition/Integration split is BOOK-DEFINED, grounded in Lenzerini (DI-01)
- RATE_OF_CHANGE continuous scenario: A (calculus) and B (mechanics) converge on
  `rateOfChange_1` as two distinct evidence pieces; C (electronics) is NOT identified
  with velocity — deferred at the SHACL gate (missing `withRespectTo`)
- Structural similarity between velocity and capacitor current is only a hint →
  CandidateMechanismHypothesis for Chapter 8, never asserted identity here
- Fellegi–Sunter two-threshold decision rule as the core of entity resolution
- R2RML + Direct Mapping + CSVW (three W3C Recommendations) for RDB→RDF/tabular→RDF
- Content hash ≠ claim identity; SHACL conformance ≠ acceptance ≠ truth
- Failure walkthrough (§7.32): structurally valid ≠ semantically correct ≠
  epistemically accepted (finite-difference Δx/Δt case)
- Chunking is not neutral plumbing — boundaries change what extraction sees
- Inductive learning explicitly excluded (§7.34) — belongs to Chapter 8

## Next steps

- Chapter 8 (Inductive Knowledge and Learning from Graphs) can be started when ready —
  it takes up the CandidateMechanismHypothesis hook from §7.36
- Book Preview v0.6 milestone: Front matter + Ch1-7 + Glossary + Bibliography

## Constraints carried forward

- Do NOT resume deferred labs
- Do NOT install Neo4j
- SHACL 1.2 Core (SH-02) = CURRENT DEVELOPMENT ONLY; stable baseline is SH-01
- Book quality > lab completeness
- All external claims must cite sources from docs/source_index.json / references.bib
- Use GitHub MCP for commits so author shows as "MinhTuan76800310"
- DO NOT start Chapter 8 until explicitly requested
