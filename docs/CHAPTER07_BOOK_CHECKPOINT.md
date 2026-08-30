# Chapter 7 Book Checkpoint

**Chapter:** 7 — Knowledge Acquisition and Integration / Thu nhận và Tích hợp Tri thức
**Status:** ACCEPTED
**Date:** 2026-08-30

## Acceptance criteria met

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Research complete | ✅ | R2RML-01, CSVW-01, DIRECT-MAP-01, RL-01 (Fellegi–Sunter), SM-01 (Rahm–Bernstein), DI-01 (Lenzerini), HOGAN-CREATE-01 verified and registered |
| Manuscript drafted | ✅ | 37 sections (§7.0–§7.36), ~1900 lines |
| Semantic contracts defined | ✅ | 45 records in docs/CHAPTER07_SEMANTIC_CONTRACTS.md |
| Semantic review passed | ✅ | 45/45 PASS, 0 FAIL, 0 PARTIAL |
| Depth review passed | ✅ | docs/CHAPTER07_DEPTH_REVIEW.md: 25/25 semantic boundaries PASS, all major concepts depth ≥4, system-critical = 5, Mechanism-KG coverage 85% |
| Reader capability test | ✅ | Q1–Q38 ALL = YES (see docs/CHAPTER07_DEPTH_REVIEW.md) |
| Editorial review passed | ✅ | No blocking issues; scope reframings applied during review |
| Source index updated | ✅ | 7 new source records (R2RML-01, RL-01, SM-01, CSVW-01, DIRECT-MAP-01, DI-01, HOGAN-CREATE-01) |
| Bibliography updated | ✅ | 7 new bib entries (w3c-r2rml, w3c-direct-mapping, w3c-tabular-data-model, fellegi-sunter-1969, rahm-bernstein-2001, lenzerini-2002, hogan-creation-enrichment) |
| Citation map updated | ✅ | 9 new rows in docs/CITATION_MAP.md |
| Research notes | ✅ | docs/research_notes/R2RML-01.md, RL-01.md, SM-01.md, CSVW-01.md, DIRECT-MAP-01.md, DI-01.md, HOGAN-CREATE-01.md |
| TikZ figures created | ✅ | 5 figures: central-pipeline, entity-resolution, schema-alignment, integration-decision, acquisition-full |
| TikZ compilation | ✅ | All 19 figures (14 existing + 5 new) compile without errors |
| PDF build | ✅ | 214 pages (print), no LaTeX errors, no undefined citations |
| Tests pass | ✅ | 73 passed |
| ruff check | ✅ | 0 errors |
| ruff format --check | ✅ | 128 files already formatted |
| Concept registry updated | ✅ | 42 Ch7 entries in book/concept_registry.yaml |
| Book manifest updated | ✅ | chapter07.md added before glossary.md |
| Capability test | ✅ | Q1–Q38 ALL = YES |
| Semantic review | ✅ | 45/45 PASS |
| Editorial review | ✅ | Clean |

## Key design decisions

1. **Acquisition/Integration split is BOOK-DEFINED** — not a W3C standard. Clearly labeled
   throughout. Grounded in DI-01 (Lenzerini) for the formal integration framing.
2. **RATE_OF_CHANGE continuous scenario** — three sources (calculus A, mechanics B,
   electronics C) with no premature cross-domain identity. Source C's `current = C·dV/dt`
   is NOT asserted `owl:sameAs` velocity; it enters the review queue.
3. **Fellegi–Sunter as the core of entity resolution** — two-threshold decision rule
   taught with comparison vector γ, m/u probabilities, match/possible/non-match zones.
4. **R2RML + Direct Mapping + CSVW** — three W3C Recommendations for RDB→RDF and
   tabular→RDF; Direct Mapping is the default, R2RML is the custom mapping language.
5. **Content hash ≠ claim identity** — hash is a dedup/idempotency key, never the ledger
   claim IRI (connects to Ch6 claim identity rule).
6. **SHACL gate: conformance ≠ acceptance** — validated data may be rejected; invalid
   data routes to review, never deleted.
7. **Lineage ≠ Evidence** — lineage answers "from where?"; evidence answers "why believe?"
   Rich lineage does not imply correctness.
8. **Seven invariants I1–I7** — provenance completeness, version stamp, hash uniqueness,
   validation accompanies, no overwrite, idempotency, recorded rationale.
9. **Inductive learning explicitly excluded** — §7.34 states why: different epistemic
   character, no stable baseline standard, demands its own chapter.
10. **Integration policy** — operationalizes Ch6 governance over Ch7 pipeline; GAV/LAV
    framing from Lenzerini; sound/complete/exact mapping semantics.

## Misconceptions addressed (10+ callouts)

1. Acquisition output = Accepted Knowledge → No, it's candidate knowledge
2. Source registration = source reliability → No, registration ≠ trust
3. Fragment-level provenance is optional → No, fragment granularity is the minimum
4. Extraction confidence = claim confidence → No, they measure different things
5. Normalization is lossless → No, it may lose information; keep raw value traceable
6. Candidate generation finds duplicates → No, it finds pairs to examine
7. Same column name → same semantics → No, schema alignment is a decision with evidence
8. Deduplication = delete duplicates → No, reconcile evidence, never silently drop
9. SHACL conforms → claim is true → No, conformance ≠ truth
10. Every textual difference is a conflict → No, context may dissolve it
11. Lineage length = reliability → No, lineage and evidence are separate dimensions
12. Multiple sources → independent evidence → No, echo sources inflate apparent support
13. Pipeline runs without errors → data is good → No, silent failures are common
14. Pipeline invariants guarantee truth → No, they guarantee process discipline
15. This chapter teaches inductive learning → No, §7.34 explicitly excludes it

## Self-explanation checkpoints (7)

1. Three-source identity question before reading (§7.0)
2. Pipeline stage input/output table (§7.1)
3. Observation vs extraction record distinction (§7.5)
4. Fellegi–Sunter pair comparison exercise (§7.10)
5. R2RML subject map writing exercise (§7.12)
6. Content hash and idempotency reasoning (§7.14)
7. Failure walkthrough analysis (§7.32)

## Renderer usage

| Type | Count | Details |
|------|-------|--------|
| TikZ figures | 5 | central-pipeline, entity-resolution, schema-alignment, integration-decision, acquisition-full |
| Tables | 12+ | Pipeline stages, source types, comparison vector, Fellegi–Sunter zones, quality dimensions, 13 failure modes, invariants I1–I7, glossary |
| Code blocks | 15+ | Turtle (Source Artifact, Fragment, Extraction, Activity, Content Hash, SHACL shape, R2RML, Identity Decision, Merge Outcome, Claim Ledger, Integration Policy, Lineage), SPARQL query |
| Mermaid | 0 | All formal diagrams use TikZ per renderer policy |

## Constraints carried forward

- Do NOT resume deferred labs
- Do NOT install Neo4j
- SHACL 1.2 Core (SH-02) = CURRENT DEVELOPMENT ONLY; stable baseline is SH-01
- Book quality > lab completeness
- All external claims cite sources from docs/source_index.json / references.bib
- Use GitHub MCP for commits so author shows as "MinhTuan76800310"
- Chapter 7 is ACCEPTED (2026-08-30) — semantic review 45/45 PASS, depth review PASS,
  editorial review clean, PDF verified. Recorded in `docs/CHAPTER07_DEPTH_REVIEW.md`.
- Do NOT start Chapter 8 until explicitly requested (next_prompt.md governs).