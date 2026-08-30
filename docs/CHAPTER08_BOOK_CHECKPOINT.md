# Chapter 8 Book Checkpoint

**Chapter:** 8 — Inductive Knowledge and Learning from Graphs / Tri thức Quy nạp và Học từ Đồ thị
**Status:** DRAFTED (semantic + depth review PASS; PDF + PR + merge pending)
**Date:** 2026-08-30

## Acceptance criteria met

| Criterion | Status | Evidence |
|-----------|--------|----------|
| Research complete | ✅ | 14 Ch8 sources registered and verified in docs/source_index.json |
| Manuscript drafted | ✅ | 52 sections (§8.0–§8.51), ~1919 lines |
| Semantic contracts defined | ✅ | 60 records in docs/CHAPTER08_SEMANTIC_CONTRACTS.md |
| Semantic review passed | ✅ | 60/60 PASS, 0 FAIL, 0 PARTIAL |
| Depth review passed | ✅ | docs/CHAPTER08_DEPTH_REVIEW.md: 52/52 major concepts depth ≥4, 25/25 critical boundaries PASS, 40/40 reader capabilities = YES |
| Reader capability test | ✅ | Q1–Q40 ALL = YES (see docs/CHAPTER08_DEPTH_REVIEW.md) |
| Editorial review passed | ✅ | No blocking issues |
| Source index updated | ✅ | 14 new Ch8 source records |
| Bibliography updated | ✅ | 16 new bib entries (hogan-inductive, bordes-transe-2013, yang-distmult-2015, trouillon-complex-2016, schlichtkrull-rgcn-2018, galarraga-amie-2015, teru-grail-2020, nickel-relational-ml-2016, mikolov-negativesampling-2013, li-oversmoothing-2018, geirhos-shortcut-2020, guo-calibration-2017, shumailov-collapse-2024, hamilton-grl-2020, prov-o, w3c-shacl) |
| Citation map updated | ✅ | 14 new rows in docs/CITATION_MAP.md |
| Research notes | ✅ | 14 new research notes in docs/research_notes/ |
| TikZ figures created | ✅ | 8 figures: ch08-reasoning-modes, ch08-transe-geometry, ch08-negative-sampling, ch08-message-passing, ch08-invariant-abstraction, ch08-hybrid-pipeline, ch08-counterexample-refinement, ch08-full-stack |
| TikZ compilation | ✅ | All 8 Ch8 figures compiled with lualatex |
| Concept registry updated | ✅ | 52 Ch8 concepts in book/concept_registry.yaml |
| Glossary updated | ✅ | 46 Ch8 terms added; book/glossary.md now 113 entries |
| Book manifest updated | ✅ | chapter08.md added before glossary.md |
| Tests pass | ✅ | 84 passed (11 new Ch8 integrity tests) |
| ruff check | ✅ | 0 errors |
| ruff format --check | ✅ | clean |
| PDF build | 🔲 | pending in task #12 |
| PR / merge | 🔲 | pending in task #12 |

## Key design decisions

1. **Prediction ≠ Entailment** — the central epistemic distinction of the chapter; scores and ranks are candidates, never truth.
2. **Entity ≠ Embedding** — vectors represent entities but are not the entities; protects against reification fallacy.
3. **Open-World Assumption as the grounding** — negative sampling is an engineering device; missing triples are not false.
4. **BOOK-DEFINED CandidateMechanismHypothesis** — seven-step generation pipeline for mechanism hypotheses, treated as candidates.
5. **BOOK-DEFINED hybrid pipeline** — ML candidates → symbolic filter → epistemic review → governance; no direct ledger insertion.
6. **BOOK-DEFINED ModelAssessment** — score semantics wrapper; no anonymous numbers.
7. **BOOK-DEFINED CandidateAxiom** — model-proposed axiom with mandatory blast-radius evaluation before acceptance.
8. **GraIL framing for inductive KG learning** — unseen-entity/subgraph generalization as the standard meaning.
9. **Rule induction confidence terminology** — explicit collision warning between PCA confidence and Ch6 epistemic confidence.
10. **Source-first discipline** — training data provenance traced to source fragments; provenance ≠ evidence.
11. **Self-reinforcing feedback / model collapse** — predictions re-entering training are tracked and controlled.
12. **Capability ladder ending at Ch8** — Ch9 is bridged but not started.

## Misconceptions addressed (43 ⚠️ callouts)

A representative sample (all callouts use ⚠️ in the manuscript):

1. Induction = deduction with more data — No
2. Prediction = entailment — No
3. Vector = statement — No
4. Entity = embedding — No
5. h + r ≈ t is a logical entailment — No
6. Models "understand" semantics — No
7. Negative sample = false triple — No
8. Score = probability of truth — No
9. Top rank = truth — No
10. Absence in KG = falsity — No
11. More GNN layers always better — No
12. Transductive and inductive are synonyms — No
13. Cluster = ontology class — No
14. PCA confidence = epistemic confidence — No
15. Training provenance = evidence — No
16. Training data = truth — No
17. Learned rule = logical law — No
18. Model explanation = evidence — No
19. Filtered evaluation = truth measurement — No
20. Pattern = mechanism — No
21. Similarity = identity — No
22. Model error = knowledge conflict — No
23. Calibrated = correct — No
24. Self-reinforcing reuse harmless — No
25. Model-proposed axiom can be inserted directly — No
26. Blast radius optional — No
27. Oversmoothing means noise — No
28. Data leakage a benign shortcut — No
29. Echo sources independent evidence — No
30. Benchmark score guarantees mechanism understanding — No

## Self-explanation checkpoints (7)

1. Before reading: rate-of-change in physics vs electronics (§8.0)
2. Deduction/induction/abduction/prediction sorting (§8.1)
3. Compute cosine similarity (§8.18)
4. Generate CandidateMechanismHypothesis H-104 (§8.19)
5. Design hard negatives for Derivative vs FiniteDifference (§8.27)
6. Score semantics for ModelAssessment (§8.30)
7. Counterexample-driven axiom refinement cycle (§8.42)

## Renderer usage

| Type | Count | Details |
|------|-------|--------|
| TikZ figures | 8 | ch08-reasoning-modes, ch08-transe-geometry, ch08-negative-sampling, ch08-message-passing, ch08-invariant-abstraction, ch08-hybrid-pipeline, ch08-counterexample-refinement, ch08-full-stack |
| Tables | 18+ | reasoning modes, task taxonomy, KGE comparison, symbolic vs embeddings, failure modes (13), central distinctions (10), capability ladder (14), glossary |
| Code blocks | 25+ | Turtle (CandidateMechanismHypothesis, ModelAssessment, TrainingOrInferenceActivity, CandidateAxiom), SPARQL, formulas |
| Mermaid | 0 | All formal diagrams use TikZ per renderer policy |

## Constraints carried forward

- Do NOT resume deferred labs
- Do NOT start Chapter 9 (only a bridge in §8.51)
- All external claims traceable to docs/source_index.json / references.bib
- BOOK-DEFINED terms labeled explicitly
- Use GitHub MCP for commits so author shows as "MinhTuan76800310"
- Chapter 8 is DRAFTED (2026-08-30) — PDF build, validation, PR, and merge pending in task #12

## Remaining work

1. Run `scripts/build_book.sh` to produce PDF
2. Verify page count, undefined citations, LaTeX errors
3. Run `uv run pytest`, `uv run ruff check .`, `uv run ruff format --check .`
4. Commit checkpoint and depth review
5. Push branch, open PR #13, validate, merge
6. Update BOOK_STATUS.md to ACCEPTED after merge