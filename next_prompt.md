# Chapter 6 — DRAFTED (2026-08-29)

Chapter 6 has been drafted with semantic contracts, TikZ figures, and PDF verification.
Awaiting semantic review and editorial review before ACCEPTED status.

## Current state

- Chapters 1–5 are ACCEPTED
- Chapter 6 is DRAFTED (research complete, manuscript written, contracts defined, figures created)
- Book PDF builds to 123 pages (was 100 before Ch6; +23 pages for epistemic layer)
- All tests pass: 43 passed (book gate), plus optional lab tests
- Semantic contracts: docs/CHAPTER06_SEMANTIC_CONTRACTS.md (28 records)
- Manuscript: 22 sections (§6.0–§6.22), ~700+ lines
- 5 TikZ figures: epistemic model, PROV chain, contradiction taxonomy, temporal clocks, epistemic layers
- 16 misconceptions addressed, 5 self-explanation checkpoints
- Primary sources added: PROV-DM-01, OWL-TIME-01

## Key design decisions

- Epistemic model is BOOK-DEFINED, not W3C standard
- Claim as first-class object via n-ary pattern (stable baseline)
- RDF 1.2 Triple Terms mentioned as emerging, not baseline
- Five contradiction types with context dissolution
- Four temporal clocks explicitly distinguished
- LLM output = CandidateKnowledge, cannot self-verify
- Governance states: Candidate/Accepted/Rejected/Contested/Superseded

## Next steps for ACCEPTED

1. Semantic review against CHAPTER06_SEMANTIC_CONTRACTS.md
2. Editorial review (reader-friction, pedagogy compliance)
3. Fix any issues found
4. Mark ACCEPTED in BOOK_STATUS.md
5. Create docs/CHAPTER06_BOOK_CHECKPOINT.md

## Constraints carried forward

- Do NOT resume deferred labs
- Do NOT install Neo4j
- SHACL 1.2 Core (SH-02) = CURRENT DEVELOPMENT ONLY; stable baseline is SH-01
- Book quality > lab completeness
- All external claims must cite sources from docs/SOURCES.md
- Use GitHub MCP for commits so author shows as "MinhTuan76800310"
- DO NOT start Chapter 7 until Chapter 6 is ACCEPTED
