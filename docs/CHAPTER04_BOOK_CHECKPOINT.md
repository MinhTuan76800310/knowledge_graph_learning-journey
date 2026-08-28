# Chapter 4 Book Checkpoint

**Date:** 2026-08-29
**Chapter:** 4 — Ontologies and Formal Meaning (Bản thể học và Ngữ nghĩa Hình thức)
**Status:** ACCEPTED

## Deliverables completed

- [x] `book/chapter04.md` — full manuscript (~17 sections, ~500 lines), all math in `$...$` LaTeX mode
- [x] `book/concept_registry.yaml` — updated with all Ch4 concepts (interpretation, model, entailment, class_expression, existential_restriction, universal_restriction, owa, necessary_condition, sufficient_condition, description_logic, tbox, abox, rbox, consistency, satisfiability)
- [x] `book/book-manifest.yaml` — chapter04.md added between chapter03.md and glossary.md
- [x] `book/glossary.md` — new entries: Axiom, Class Expression, Consistency, Entailment (updated), Existential Restriction, Interpretation, Model, Ontology (updated), OWA, Satisfiability, Universal Restriction; Taxonomy updated
- [x] `book/references.bib` — 6 entries: w3c-owl2-overview, w3c-owl2-syntax, w3c-owl2-direct-semantics, w3c-owl2-rdf-semantics, w3c-owl2-profiles, hogan-deductive-knowledge
- [x] `docs/source_index.json` — 6 sources FETCHED_AND_VERIFIED (OWL-02 through OWL-06, HOGAN-CH6)
- [x] `docs/CHAPTER04_SEMANTIC_CONTRACTS.md` — 25+ concept records with formal definitions and MUST-NOT-infer statements
- [x] `docs/research_notes/OWL-03.md` through `OWL-06.md`, `HOGAN-CH6.md` — all rewritten with real evidence
- [x] `docs/BOOK_STATUS.md` — Ch4 status updated to ACCEPTED
- [x] Tests pass: 9/9 concept dependency tests green
- [x] PDF builds: 74 pages, no LaTeX errors
- [x] Visual inspection: math rendering verified on pages 48, 54, 58

## Semantic closure corrections applied (23 items from user directive)

1. [x] Declaration semantics: nonlogical under Direct Semantics (§5.8 Structural Spec)
2. [x] Annotation semantics: no semantic meaning under Direct Semantics; semantically weak under RDF-Based
3. [x] Data property semantics: Δ_D separate domain, P^I ⊆ Δ^I × Δ_D
4. [x] Universal restriction: Level A (vacuous truth within interpretation) vs Level B (absence ≠ entailment)
5. [x] Three entailment states: consistent ontology precondition added
6. [x] Inconsistent ontology: ex falso quodlibet breakdown noted
7. [x] CWA/SQL NULL/OWA: three-way distinction in §4.8
8. [x] Necessary/sufficient directionality: A ⊑ B means A sufficient for B, B necessary for A
9. [x] Functional property: entailment vs materialization distinction
10. [x] differentFrom + functionality = inconsistency note
11. [x] Direct vs RDF-Based: serialization ≠ semantic regime
12. [x] DL/SROIQ wording: "tương thích chặt chẽ" not "tương ứng với"
13. [x] EL PTIME: core reasoning only, not conjunctive queries
14. [x] RL completeness: not guaranteed on arbitrary RDF
15. [x] No profile is subset of another
16. [x] RateOfChangeMechanism: pedagogical toy warning + stronger modeling direction
17. [x] Entailment ≠ materialization in glossary
18. [x] Taxonomy entry: removed "subset of ontology"
19. [x] Misconception #1 (taxonomy), #2 (schema), #8 (cardinality/materialization) fixed
20. [x] All backtick-wrapped math converted to $...$ LaTeX math mode
21. [x] Pre-existing Ch2 LaTeX bug fixed (≠, ↦, → moved out of backticks)
22. [x] All 6 primary sources fetched and verified (no placeholders)
23. [x] Semantic contracts document created

## Manuscript structure

| Section | Title | Key content |
|---------|-------|-------------|
| 4.1 | Mở đầu: Cú pháp không phải là ý nghĩa | Syntax ≠ semantics motivation |
| 4.2 | Ontology là gì? | Schema vs ontology, OWL entities/expressions/axioms, annotation ≠ axiom |
| 4.3 | Cơ chế trung tâm: Diễn giải → Mô hình → Suy diễn | Math sidebar, interpretation I=(Δ^I,·^I), satisfaction, models, entailment O⊨α, data properties Δ_D |
| 4.4 | Lớp như tập hợp | Subclass, equivalence, disjointness; sameAs vs equivalentClass |
| 4.5 | Điều kiện cần và điều kiện đủ | SubClassOf one-directional, Equivalence bidirectional, worked example |
| 4.6 | Biểu thức lớp | Intersection, union, complement, ∃R.C, ∀R.C (two-level), cardinality |
| 4.7 | Ngữ nghĩa thuộc tính | Subproperty, inverse, symmetric, transitive, functional (entailment vs materialization), inverse-functional |
| 4.8 | Giả định thế giới mở | CWA vs SQL NULL vs OWA, three entailment states with consistency precondition |
| 4.9 | Nhất quán, Thỏa được, Suy diễn | Three distinct questions with examples |
| 4.10 | Trực giác Description Logic | TBox/ABox/RBox as mental categories, decidability vs tractability |
| 4.11 | OWL Direct vs RDF-Based Semantics | Serialization ≠ semantic regime, annotations differ between regimes |
| 4.12 | OWL 2 Profiles | EL (PTIME core only), QL, RL (completeness caveat) tradeoffs |
| 4.13 | Cầu nối đến Mechanism KG | RateOfChangeMechanism as pedagogical toy, stronger modeling direction |
| 4.14 | Những ngộ nhận thường gặp | 12 common misconceptions |
| 4.15 | Câu hỏi suy ngẫm | 5 reflection questions (★ to ★★★) |
| 4.16 | Chúng ta đã biết gì | Summary of learned concepts |
| 4.17 | Chúng ta chưa làm được gì | Bridge to Chapter 5 |

## Self-explanation checkpoints (4)

1. §4.1: Why naming a node "City" is insufficient for machine understanding
2. §4.3: Why multiple models is a design feature, not a bug
3. §4.5: SubClassOf vs Equivalence entailment difference
4. §4.8: Person ⊑ ∃hasName.String with missing data — consistency under OWA

## Pedagogical compliance

- [x] Five-step formula explanation pattern used throughout §4.3
- [x] Running example: Hanoi/Vietnam/CapitalCity domain
- [x] Math sidebar with symbol reference table
- [x] Forward references clearly marked ("sẽ học ở Chương 5")
- [x] No concept required before explained (registry invariant verified)
- [x] All external claims cite sources from docs/SOURCES.md
- [x] Original content only — no copied passages

## Quality gate results

| Check | Result |
|-------|--------|
| Concept dependency tests (9) | ✅ 9/9 passed |
| PDF build (pandoc → LuaLaTeX) | ✅ 74 pages, no errors |
| Unresolved citations | ✅ None |
| Leftover Mermaid blocks | ✅ None |
| U+FFFD replacement chars | ✅ None |
| Wrapper artifacts | ✅ None |
| Math rendering (visual) | ✅ Verified pages 48, 54, 58 |
| pdftotext Vietnamese extraction | ⚠ Known encoding limitation (not a content issue) |

## Go/No-Go for Chapter 5

**GO.** Chapter 4 has reached ACCEPTED status after comprehensive semantic and editorial closure. All 23 correction items from the user's directive have been applied and verified. All 6 primary sources are fetched and verified. The semantic contracts document establishes formal boundaries for every concept taught. PDF builds cleanly with proper LaTeX math rendering. Tests pass. Chapter 5 may begin.
