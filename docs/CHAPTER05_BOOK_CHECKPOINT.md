# Chapter 5 Book Checkpoint

**Date:** 2026-08-29
**Chapter:** 5 — Suy diễn, Quy tắc và Xác nhận (Inference, Rules, and Validation)
**Status:** ACCEPTED

## Deliverables completed

- [x] `book/chapter05.md` — full manuscript (~15 sections, ~470 lines), all math in `$...$` LaTeX mode
- [x] `book/concept_registry.yaml` — updated with 10 Ch5 concepts (forward_chaining, materialization, rule, validation_report, shape, soundness, completeness, conformance, entailment_regime, swrl)
- [x] `book/book-manifest.yaml` — chapter05.md added between chapter04.md and glossary.md
- [x] `book/glossary.md` — new entries: Completeness, Conformance, Entailment Regime, Forward Chaining, Materialization, Rule, SHACL, Shape, Soundness, SWRL, Validation Report; updated Entailment and Validation entries
- [x] `book/references.bib` — 5 entries: w3c-shacl, w3c-shacl12-core, swrl-submission, w3c-rif-core, hogan-rules-reasoning
- [x] `docs/source_index.json` — 4 sources FETCHED_AND_VERIFIED (SWRL-01, RIF-01, HOGAN-CH5, OWL-RL-SPEC)
- [x] `docs/CHAPTER05_SEMANTIC_CONTRACTS.md` — 14 concept records with formal definitions and MUST-NOT-infer statements
- [x] `docs/research_notes/SWRL-01.md`, `RIF-01.md`, `HOGAN-CH5.md`, `OWL-RL-SPEC.md` — all written with real evidence
- [x] `docs/BOOK_STATUS.md` — Ch5 status updated to ACCEPTED
- [x] Tests pass: 9/9 concept dependency tests green, 43 total passed
- [x] PDF builds: 86 pages, no LaTeX errors

## Manuscript structure

| Section | Title | Key content |
|---------|-------|-------------|
| 5.1 | Mở đầu: Hai câu hỏi, hai pipeline | Inference vs Validation distinction, comparison table |
| 5.2 | Forward Chaining: Cơ chế suy diễn cơ bản | Fixpoint algorithm G_{i+1} = G_i ∪ consequences(G_i), worked example, termination conditions |
| 5.3 | RDFS Entailment Rules | subClassOf, subPropertyOf, domain, range; domain/range ADD information, NOT validate |
| 5.4 | Vật chất hóa | Implementation strategy ≠ entailment relation; feasibility conditions |
| 5.5 | SHACL: Xác nhận dữ liệu bằng Shapes | Shape definition, constraint types, validation report structure |
| 5.6 | Phù hợp ≠ Đúng | Conformance ≠ truth; violation ≠ error |
| 5.7 | Shapes ≠ Axioms | SHACL vs ontology comparison table; non-interchangeability |
| 5.8 | Tính đúng đắn và Tính đầy đủ | Soundness/completeness with three-part qualification; OWL RL limitations |
| 5.9 | Chế độ suy diễn | Entailment regime table (Simple → OWL RDF-Based) |
| 5.10 | Quy tắc Horn và SWRL | Horn clause properties; SWRL Member Submission caveat; undecidability |
| 5.11 | Cầu nối đến Mechanism KG | Application to capstone project |
| 5.12 | Những ngộ nhận thường gặp | 8 common misconceptions |
| 5.13 | Câu hỏi suy ngẫm | 5 reflection questions (★ to ★★★) |
| 5.14 | Chúng ta đã biết gì | Summary |
| 5.15 | Chúng ta chưa làm được gì | Bridge to Chapters 6-8 |

## Self-explanation checkpoints (4)

1. §5.1: RDFS domain behavior under inference vs validation pipelines
2. §5.3: Enumerate all triples derived by RDFS domain/range forward chaining
3. §5.5: SHACL validation results for different data scenarios
4. §5.8: Why OWL RL forward chaining misses some OWL 2 DL entailments

## Semantic review pass

Performed 2026-08-29 via independent agent. Read chapter05.md linearly against all 14 records in CHAPTER05_SEMANTIC_CONTRACTS.md.

**Results:** All 14 contract records PASS. No MUST NOT violations found. No dangerous simplifications. Wording consistent with or better than prescribed "Book wording" field.

**One fix applied:** Backward reference "§2.1" for RDFS domain/range corrected to "§3.1" (domain/range as inference rules is taught in Ch3, not Ch2).

## Editorial review pass

Performed 2026-08-29 via independent agent. Results:

- Forward references (Ch6-10): properly marked ✅
- Backward references (§X.Y, Ch1-4): accurate after fix ✅
- Citation format: all match references.bib ✅
- Technical term first-occurrence convention: clean after fixes ✅
- Self-check questions (4): pedagogically sound ✅
- Callout boxes: highlight genuine distinctions ✅
- Vietnamese language: fluent, diacritics complete ✅

**Two fixes applied from editorial review:**
1. Added Vietnamese glosses for "disjunction (phép hoặc)" and "existential quantification (lượng từ tồn tại)"
2. Changed bare "decidability" to "tính quyết định được (decidability)" in two locations

No blocking issues found.

## Quality gate results

| Check | Result |
|-------|--------|
| Concept dependency tests (9) | ✅ 9/9 passed |
| Full test suite | ✅ 43 passed, 1 skipped (rdflib) |
| PDF build (pandoc → LuaLaTeX) | ✅ 86 pages, no errors |
| Unresolved citations | ✅ None |
| Leftover Mermaid blocks | ✅ None |
| U+FFFD replacement chars | ✅ None |
| Wrapper artifacts | ✅ None |
| Math rendering | ✅ All $...$ LaTeX mode |

## Sources used

| Source ID | Title | Status | Used For |
|-----------|-------|--------|----------|
| R11-03 | RDF Schema 1.1 | Stable REC | RDFS entailment rules |
| OWL-01 | OWL 2 Overview | Stable REC | Reasoning overview |
| SH-01 | SHACL 1.0 | Stable REC | Validation baseline |
| SH-02 | SHACL 1.2 Core | WD (EMERGING) | Current development note |
| SWRL-01 | SWRL | Member Submission | Rule extension + undecidability |
| RIF-01 | RIF Core Dialect | Stable REC | Safeness + termination |
| HOGAN-CH5 | Hogan Rules & Reasoning | Academic textbook | Fixpoint, soundness/completeness |
| OWL-RL-SPEC | OWL 2 RL section | Stable REC | Rule tables, conditional completeness |
