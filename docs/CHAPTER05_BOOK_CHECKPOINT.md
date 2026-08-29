# Chapter 5 Book Checkpoint

**Date:** 2026-08-29
**Chapter:** 5 — Suy diễn, Quy tắc và Xác nhận (Inference, Rules, and Validation)
**Status:** ACCEPTED (after semantic closure)

## Status history

- **2026-08-29 (initial):** ACCEPTED after first semantic + editorial review pass.
- **2026-08-29 (revised):** Independent deep review identified blocking formal and pedagogical issues across forward-chaining formalization, monotonicity definition, termination conditions, RDFS normative sourcing, SPARQL entailment-regime wording, SHACL targeting semantics, consistency-vs-validation depth, graph repair mechanism, and OWL RL completeness qualification. Status reverted to SEMANTIC_CLOSURE_REQUIRED. Original ACCEPTED record preserved below as historical evidence.
- **2026-08-29 (closure complete):** All 28 semantic contracts PASS. All 17 final review questions PASS. PDF builds to 97 pages with no errors. Tests: 43 passed, 1 skipped. Status returned to ACCEPTED.

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

## Manuscript structure (revised)

| Section | Title | Key content |
|---------|-------|-------------|
| 5.1 | Mở đầu: Hai câu hỏi, hai pipeline | Inference vs Validation distinction, comparison table |
| 5.2 | Forward Chaining: Cơ chế suy diễn cơ bản | Substitution θ, fixpoint formula with θ, multi-round worked example, monotonicity over KB, termination assumptions (5 conditions), non-monotonic brief mention |
| 5.3 | RDFS Entailment Rules | Sourced from RDF-MT-01 §9.2.1; rdfs2/rdfs3/rdfs7/rdfs9 patterns; domain/range ADD not validate; rule-based operationalization vs normative semantics; completeness nuance |
| 5.4 | Vật chất hóa và Suy diễn tại thời điểm truy vấn | Materialization vs query-time comparison table; hybrid strategy; asserted ≠ derived |
| 5.5 | Forward vs Backward: Hai chiến lược tính toán | Goal-driven vs data-driven; worked example both directions; algorithmic mental model caveat |
| 5.6 | SHACL: Xác nhận dữ liệu bằng Shapes | SHACL ≠ CWA OWL; pipeline diagram; Target→Focus→Path→Value→Constraint→Result walkthrough; targetClass subclass semantics; sh:class subclass semantics; constraints by problem category |
| 5.7 | Validation Report: Cấu trúc giải phẫu | Full Turtle report anatomy; 7 debugging questions; sh:value optional |
| 5.8 | Phù hợp ≠ Đúng | Conformance ≠ truth; validation gate; quality signal; evolution |
| 5.9 | Nhất quán ≠ Xác nhận: Hai trục độc lập | Case A (OWL-inconsistent + SHACL-conformant); Case B (OWL-consistent + SHACL-invalid); 2×2 table; existential restriction vs minCount |
| 5.10 | Shapes ≠ Axioms | Comparison table; OWL ∃R.C vs SHACL minCount deep example |
| 5.11 | Suy diễn trước Xác nhận | Three architectures (A/B/C); effective validation graph; production documentation requirements |
| 5.12 | Vi phạm ≠ Sửa chữa: Cơ chế Graph Repair | 5 candidate repairs table; repair pipeline; 4 repair operation types; passes validation ≠ becomes true |
| 5.13 | Tính đúng đắn và Tính đầy đủ | Set diagram A⊆E / E⊆A; three-part qualification; OWL RL Theorem PR1; qualified completeness |
| 5.14 | Chế độ suy diễn | Regime table; SPARQL Service Description (not FROM); standard regime IRIs |
| 5.15 | OWL 2 DL và Giới hạn của Vật chất hóa | Existential witnesses; model structures; tableau algorithms; formal entailment ≠ finite materialization |
| 5.16 | Quy tắc Horn và SWRL | Horn properties; SWRL Member Submission; undecidability; RIF Core context; ecosystem proportion |
| 5.17 | SHACL 1.2: Phát triển hiện tại | Current development callout; stable baseline = SHACL 2017; emerging = SHACL 1.2 WD 2026-08-03 |
| 5.18 | Cầu nối đến Mechanism KG | Application; repair governance |
| 5.19 | Những ngộ nhận thường gặp | 12 misconceptions (was 8) |
| 5.20 | Câu hỏi suy ngẫm | 5 reflection questions (★ to ★★★) |
| 5.21 | Chúng ta đã biết gì | Summary |
| 5.22 | Chúng ta chưa làm được gì | Bridge to Chapters 6-8 |

## Self-explanation checkpoints (5)

1. §5.1: RDFS domain behavior under inference vs validation pipelines
2. §5.2: Why "no new facts" means forward chaining has stabilized (fixpoint reasoning)
3. §5.3: Enumerate all triples derived by RDFS domain/range with θ; explain why results look absurd but are semantically correct
4. §5.6: SHACL validation results for different data scenarios with focus/value node mechanism
5. §5.9: Why OWL existential restriction does not behave like sh:minCount (consistency vs validation axes)

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

## Quality gate results (semantic closure pass)

| Check | Result |
|-------|--------|
| Concept dependency tests (9) | ✅ 9/9 passed |
| Full test suite | ✅ 43 passed, 1 skipped (rdflib) |
| PDF build (pandoc → LuaLaTeX) | ✅ 97 pages, no LaTeX errors |
| Unresolved citations | ✅ None |
| Leftover Mermaid blocks | ✅ None |
| U+FFFD replacement chars | ✅ None |
| Wrapper artifacts | ✅ None |
| Math rendering | ✅ All $...$ LaTeX mode, θ renders correctly |
| Turtle code blocks | ✅ No clipping |
| Tables | ✅ All fit A4 width |

## Semantic closure review (2026-08-29)

Independent semantic review against 28 contract records in CHAPTER05_SEMANTIC_CONTRACTS.md.

**Results:** All 28 contracts PASS. All 17 final review questions PASS.

Key corrections applied during closure:
- Forward chaining formula now includes substitution θ explicitly
- Monotonicity defined over knowledge base (G⊆G'), not rule body conditions
- Termination lists all 5 required assumptions
- RDFS normative semantics sourced from RDF-MT-01 §9.2.1 with pattern numbers
- Rule-based operationalization vs normative semantics distinction with Appendix A completeness caveat
- SPARQL entailment regime via Service Description, not FROM clause
- targetClass uses SHACL instance semantics (rdfs:subClassOf* chain)
- sh:class uses subclass reasoning
- Focus node vs value node mechanism walkthrough (6 steps)
- Validation report anatomy with sh:value optionality
- Consistency vs validation in BOTH directions (Cases A and B)
- OWL existential restriction vs SHACL minCount deep contrast
- Effective validation graph with three architectures
- Graph repair as decision problem with 5 candidates and pipeline
- OWL RL completeness qualified with Theorem PR1
- SHACL ≠ closed-world OWL explicit section
- Backward chaining section added
- Materialization vs query-time comparison table
- OWL 2 DL materialization limits (existential witnesses, tableau)
- SHACL 1.2 current development callout
- 12 misconceptions (was 8), 5 self-explanation checkpoints (was 4)

## Sources used

| Source ID | Title | Status | Used For |
|-----------|-------|--------|----------|
| RDF-MT-01 | RDF 1.1 Semantics | Stable REC | Normative RDFS entailment patterns, rule-based operationalization completeness |
| R11-03 | RDF Schema 1.1 | Stable REC | RDFS vocabulary |
| OWL-01 | OWL 2 Overview | Stable REC | Reasoning overview |
| OWL-05 | OWL 2 Profiles | Stable REC | OWL RL Theorem PR1, profile limitations |
| SH-01 | SHACL 1.0 | Stable REC | Validation baseline, target/class/focus/value semantics |
| SH-02 | SHACL 1.2 Core | WD (EMERGING) | Current development callout only |
| SP11-ENT | SPARQL 1.1 Entailment Regimes | Stable REC | Service Description regime specification, FROM≠regime |
| SWRL-01 | SWRL | Member Submission | Rule extension + undecidability |
| RIF-01 | RIF Core Dialect | Stable REC | Safeness + termination |
| HOGAN-CH5 | Hogan Rules & Reasoning | Academic textbook | Fixpoint, soundness/completeness, materialization |
