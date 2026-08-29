# Chapter 6 — ACCEPTED (2026-08-29)

Chapter 6 has passed semantic review (28/28 PASS) and editorial review (no blocking issues).
All acceptance criteria met. Status: ACCEPTED.

## Current state

- Chapters 1–6 are ACCEPTED
- Book PDF builds to 124 pages (was 100 before Ch6; +24 pages for epistemic layer)
- All tests pass: 43 passed (book gate), plus optional lab tests
- Semantic contracts: docs/CHAPTER06_SEMANTIC_CONTRACTS.md (28 records, all PASS)
- Manuscript: 22 sections (§6.0–§6.22), ~1150 lines
- 5 TikZ figures: epistemic model, PROV chain, contradiction taxonomy, temporal clocks, epistemic layers
- 10 misconception callouts, 7 self-explanation checkpoints
- Primary sources: PROV-O, PROV-DM, OWL-Time (all stable W3C Recommendations)
- Checkpoint: docs/CHAPTER06_BOOK_CHECKPOINT.md

## Key design decisions

- Epistemic model is BOOK-DEFINED, not W3C standard
- Claim as first-class object via n-ary pattern (stable baseline)
- RDF 1.2 Triple Terms mentioned as emerging, not baseline
- Five contradiction types with context dissolution
- Four temporal clocks explicitly distinguished
- LLM output = CandidateKnowledge, cannot self-verify
- Governance states: Candidate/Accepted/Rejected/Contested/Superseded

## Next steps

- Chapter 7 can now be started when ready
- Book Preview v0.5 milestone: Front matter + Ch1-6 + Glossary + Bibliography (124 pages)

## Constraints carried forward

- Do NOT resume deferred labs
- Do NOT install Neo4j
- SHACL 1.2 Core (SH-02) = CURRENT DEVELOPMENT ONLY; stable baseline is SH-01
- Book quality > lab completeness
- All external claims must cite sources from docs/SOURCES.md
- Use GitHub MCP for commits so author shows as "MinhTuan76800310"
- DO NOT start Chapter 7 until explicitly requested
