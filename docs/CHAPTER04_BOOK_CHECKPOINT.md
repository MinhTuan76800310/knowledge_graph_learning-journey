# Chapter 4 Book Checkpoint

**Date:** 2026-08-28
**Chapter:** 4 — Ontologies and Formal Meaning (Bản thể học và Ngữ nghĩa Hình thức)
**Status:** DRAFTED

## Deliverables completed

- [x] `book/chapter04.md` — full manuscript (~17 sections, ~500 lines)
- [x] `book/concept_registry.yaml` — updated with all Ch4 concepts (interpretation, model, entailment, class_expression, existential_restriction, universal_restriction, owa, necessary_condition, sufficient_condition, description_logic, tbox, abox, rbox, consistency, satisfiability)
- [x] `book/book-manifest.yaml` — chapter04.md added between chapter03.md and glossary.md
- [x] `book/glossary.md` — new entries: Axiom, Class Expression, Consistency, Entailment (updated), Existential Restriction, Interpretation, Model, Ontology (updated), OWA, Satisfiability, Universal Restriction; Taxonomy updated to note "subset of ontology"
- [x] `book/references.bib` — 5 new entries: w3c-owl2-overview, w3c-owl2-syntax, w3c-owl2-direct-semantics, w3c-owl2-profiles, hogan-deductive-knowledge
- [x] `docs/source_index.json` — 4 new sources registered (OWL-03, OWL-04, OWL-05, HOGAN-CH6)
- [x] `docs/BOOK_STATUS.md` — Ch4 status updated to DRAFTED
- [x] Tests pass: 9/9 concept dependency tests green

## Manuscript structure

| Section | Title | Key content |
|---------|-------|-------------|
| 4.1 | Mở đầu: Cú pháp không phải là ý nghĩa | Syntax ≠ semantics motivation |
| 4.2 | Ontology là gì? | Schema vs ontology, OWL entities/expressions/axioms, annotation ≠ axiom |
| 4.3 | Cơ chế trung tâm: Diễn giải → Mô hình → Suy diễn | Math sidebar, interpretation I=(Δ^I,·^I), satisfaction, models, entailment O⊨α |
| 4.4 | Lớp như tập hợp | Subclass, equivalence, disjointness; sameAs vs equivalentClass |
| 4.5 | Điều kiện cần và điều kiện đủ | SubClassOf one-directional, Equivalence bidirectional, worked example |
| 4.6 | Biểu thức lớp | Intersection, union, complement, ∃R.C, ∀R.C, cardinality |
| 4.7 | Ngữ nghĩa thuộc tính | Subproperty, inverse, symmetric, transitive, functional, inverse-functional |
| 4.8 | Giả định thế giới mở | CWA vs OWA, three entailment states, validation implications |
| 4.9 | Nhất quán, Thỏa được, Suy diễn | Three distinct questions with examples |
| 4.10 | Trực giác Description Logic | TBox/ABox/RBox as mental categories |
| 4.11 | OWL Direct vs RDF-Based Semantics | Two official semantics, pedagogical choice |
| 4.12 | OWL 2 Profiles | EL, QL, RL tradeoffs |
| 4.13 | Cầu nối đến Mechanism KG | RateOfChangeMechanism example, what ontology cannot do |
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

## What remains for ACCEPTED status

- [ ] Semantic review
- [ ] Editorial review
- [ ] PDF build verification
- [ ] Visual inspection of rendered output

## Go/No-Go for Chapter 5

**GO.** Chapter 4 manuscript is complete and structurally sound. All supporting files updated. Tests pass. Ready for review pipeline before proceeding to Chapter 5.
