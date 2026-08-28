# Deep Readability Audit — Chapters 1–3

> Audit date: 2026-08-28
> Auditor: Claude (AI-assisted)
> Policy: docs/BOOK_PEDAGOGY.md v1.0

---

## Summary

This audit applies the Local Sufficiency principle from BOOK_PEDAGOGY.md to Chapters 1–3.
All findings have been addressed in this work slice. The audit serves as a record of what
was found and how it was resolved.

---

## Chapter 1 Findings and Resolutions

### F1: Formal model G=(V,E,λ) cannot represent multi-predicate pairs [MEDIUM]

**Problem:** The labeled-graph model maps each edge to exactly one label via λ: E→L. Between
the same pair of nodes, only one edge exists in E⊆V×V, so only one predicate can be represented.
This contradicts the RDF reality where `(Hanoi, locatedIn, Vietnam)` and `(Hanoi, capitalOf, Vietnam)` coexist.

**Resolution:** Replaced with K⊆V×L×V (triple-set model). Added explanation of why G=(V,E,λ)
fails, worked example with concrete V and L sets, and self-explanation checkpoint. Updated
Book Engineering Model from KSE=(G,T,C) to KSE=(K,T,C).

### F2: Premature Turtle syntax in §1.6 [MEDIUM]

**Problem:** Bước 3 used `rdfs:subClassOf` and Bước 4 used `rdf:type`, `owl:ObjectProperty`,
semicolons — all Turtle serialization constructs not taught until Chapter 2. Violates Local
Sufficiency (§1 of BOOK_PEDAGOGY.md).

**Resolution:** Replaced with representation-neutral conceptual notation ("là subclass của",
"domain/range" in plain prose). Added note explaining that concrete syntax will be taught in Ch2.

### F3: Preview box cognitive overload [LOW]

**Problem:** §1.2 preview box dumped 7 W3C acronyms (W3C, RDF, IRI, RDFS, OWL, SHACL, SPARQL).
Only W3C, RDF, and IRI are actually needed in Chapter 1.

**Resolution:** Reduced to 3 terms. Other terms deferred to their respective chapters with
inline glosses at point of first use.

### F4: TransE/ComplEx named unnecessarily [LOW]

**Problem:** §1.7 named specific embedding algorithms (TransE, ComplEx) that serve no
pedagogical purpose in Chapter 1 and create incidental forward-reference debt.

**Resolution:** Replaced with generic "graph embeddings" description.

### F5: Unsupported Property Graph performance claim [LOW]

**Problem:** §1.7 claimed Property Graph has "hiệu năng cao cho traversal" without citation
or qualification. Performance depends on implementation, workload, and indexing strategy.

**Resolution:** Replaced with neutral description: "mô hình dữ liệu gần với cách lập trình
viên thường nghĩ về đồ thị."

### F6: Entity definition too shallow [MEDIUM]

**Problem:** §1.3 defined entity as "đối tượng trong thế giới thực... được biểu diễn bằng
một nút trong đồ thị" — conflating real-world entity, graph node, identifier, and label into
one sentence. Missing the four-way distinction critical for understanding identity resolution.

**Resolution:** Expanded to explicit four-level model (real-world entity ≠ graph node ≠
identifier ≠ label) with counterexample showing confusion between levels and self-explanation
checkpoint.

### F7: Missing math prerequisites sidebar [LOW]

**Problem:** §1.5 uses set theory notation (∈, ×, ⊆) without confirming reader has the
prerequisites locally.

**Resolution:** Added "Toán học tối thiểu cho chương này" sidebar covering sets, Cartesian
product, subset, and function — the four concepts needed for the entire chapter.

### F8: Missing partial-order / OWL equivalence note [LOW]

**Problem:** §1.5 discussed partial order for subClassOf but didn't mention that when both
A⊑B and B⊑A hold, OWL treats them as equivalent classes.

**Resolution:** Added sentence connecting partial-order coincidence to owl:equivalentClasses
with forward reference to Ch4.

---

## Chapter 2 Findings and Resolutions

### F9: FILTER queries non-existent population triples [MEDIUM]

**Problem:** §2.1.6 FILTER example queries `ex:population` but the canonical dataset in §2.1.4
had no population triples. The query would return empty results, confusing readers.

**Resolution:** Added two population triples to canonical dataset (Hanoi: 8000000, Paris: 2161000).
Updated triple count from 9 to 11 throughout. Updated Mermaid diagram and Turtle representation.

### F10: OPTIONAL example has unused ?type variable [LOW]

**Problem:** OPTIONAL example bound `?type` via `?entity a ?type` but never used `?type` in
SELECT or elsewhere. Confusing for learners.

**Resolution:** Changed to `?entity rdf:type ex:City` — concrete type match with no unused variable.

### F11: BGP/solution mapping explanation too compressed [MEDIUM]

**Problem:** §2.1.6 defined BGP and solution mappings abstractly without a worked substitution
example showing μ = {?city ↦ ex:Hanoi} applied step-by-step.

**Resolution:** Added concrete worked example showing: (1) the BGP pattern, (2) a valid mapping
μ₁ with substitution result, (3) an invalid mapping μ' showing why it fails.

### F12: Graph isomorphism mentioned but not demonstrated [LOW]

**Problem:** §2.1.5 mentioned graph isomorphism for blank nodes but gave no concrete example
showing why raw set comparison fails and how the bijection works.

**Resolution:** Added concrete example with G₁ and G₂ using different blank node labels (_:b0 vs _:x7),
showing raw comparison fails but bijection proves isomorphism.

### F13: No pip install rdflib note [LOW]

**Problem:** §2.1.4 uses RDFLib without telling readers how to install it.

**Resolution:** Added installation note before the code block.

---

## Chapter 3 Findings and Resolutions

### F14: PROV mentioned without minimum usable gloss [LOW]

**Problem:** §3.3.2 mentions "PROV — sẽ gặp ở Chương 6" without explaining what PROV provides.
Reader cannot understand why PROV is relevant.

**Resolution:** Expanded to explain PROV-O is a W3C standard providing classes and properties
for describing provenance, agents, and activities.

### F15: N-ary relation section lacks clear binary/ternary/n-ary progression [LOW]

**Problem:** §3.3.3 jumped directly to n-ary without clearly distinguishing the three levels
(binary → ternary → n-ary) that motivate the mechanism.

**Resolution:** Added explicit three-level progression with examples at each level before
introducing the W3C pattern.

---

## Infrastructure Created

| Artifact | Purpose |
|----------|---------|
| `docs/BOOK_PEDAGOGY.md` | Canonical authoring policy (14 sections) |
| `book/concept_registry.yaml` | Concept dependency tracking (~45 concepts) |
| `tests/test_book_concept_dependencies.py` | Registry integrity tests (8 tests, all passing) |
| `next_prompt.md` | Marked as SUPERSEDED to prevent premature Ch4 start |

## Self-Explanation Checkpoints Added

| Chapter | Location | Topic |
|---------|----------|-------|
| Ch1 | §1.3 after Entity | Identifier vs entity distinction |
| Ch1 | §1.4 after mechanism | Classify a system you've used |
| Ch1 | §1.5 after formal model | Why K⊆V×L×V over G=(V,E,λ) |
| Ch2 | §2.1.6 after BGP | Solution mappings vs lists |
| Ch3 | §3.2.4 after owl:sameAs | Information propagation through sameAs |
| Ch3 | §3.3.3 after n-ary | Design an n-ary structure |

---

## Remaining Items for PDF Verification

- [ ] Rebuild PDF with updated content
- [ ] Verify all new math notation renders correctly
- [ ] Verify Mermaid diagrams render (especially updated Ch2 diagram with population)
- [ ] Verify no table overflow regressions
- [ ] Visual inspection of representative pages
- [ ] Create BOOK_DEEP_READABILITY_CHECKPOINT.md
- [ ] Commit and push
- [ ] Report Go/No-Go for Chapter 4
