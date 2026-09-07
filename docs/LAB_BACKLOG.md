# Lab Backlog — Deferred Experiments

**Policy:** As of the Book v0.1 milestone, the primary deliverable is a complete,
printable, high-quality PDF book covering Chapters 1–10. Hands-on experiments remain
valuable but are **secondary** and must not block book completion.

Experiments that are not required to validate a factual claim in the manuscript are
deferred here. Their **pedagogical content is still written into the book chapters**
using authoritative sources, diagrams, static examples, and carefully marked code
examples. Runnable implementations return after Book v0.1.

**Priority rule:** `BOOK QUALITY > LAB COMPLETENESS`. Research correctness remains
non-negotiable.

---

## How to read this backlog

Each entry records:

- **Experiment ID**
- **Pedagogical purpose** — what the reader learns
- **Current design document** — where the full design lives
- **Semantic contracts** — the contracts the experiment must honor
- **Dependencies** — infrastructure or prior experiments required
- **Acceptance criteria** — what "done" means
- **Priority**
- **Status** — currently `DEFERRED_UNTIL_BOOK_V0.1`

---

## Chapter 2 — Property-Graph Labs (COMPLETED)

> **Status Update (v0.3.0 Completeness):** The 3 deferred property-graph experiments for Chapter 2 have been fully implemented and verified via automated test suites in `chapter02/test_ch2_experiments.py`. They feature a dual-engine architecture with pure-Python standalone in-memory execution and openCypher/Neo4j query compatibility:
> - `EXP-2-5` (`exp_2_5_labeled_property_graph.py`): Formal 7-tuple LPG model, node multi-labels, direct edge properties.
> - `EXP-2-6` (`exp_2_6_cypher_traversal.py`): Directed/undirected pattern matching, WHERE filtering, variable-length path traversal.
> - `EXP-2-7` (`exp_2_7_rdf_vs_property_graph.py`): Side-by-side executable comparison between RDFLib (with W3C reification) and LPG.

### EXP-2-5 (formerly EXP-2-4) — Labeled Property Graph Model
- **Status:** ✅ COMPLETED (`chapter02/exp_2_5_labeled_property_graph.py`)

### EXP-2-6 (formerly EXP-2-5) — Cypher Traversal
- **Status:** ✅ COMPLETED (`chapter02/exp_2_6_cypher_traversal.py`)

### EXP-2-7 (formerly EXP-2-6) — Same Knowledge: RDF vs Property Graph
- **Status:** ✅ COMPLETED (`chapter02/exp_2_7_rdf_vs_property_graph.py`)

---

## Backlog outside Chapter 2

Chapters 4–10 experiments are not yet designed. They will be added here as each
chapter is written, applying the same rule: defer any experiment that is not required
to validate a factual claim in the manuscript.

---

## Chapter 3 — Labs (COMPLETED)

> **Status Update (v0.3.0 Completeness):** All 6 experiments for Chapter 3 have been fully implemented, verified with 15 direct semantic tests in `chapter03/test_ch3_experiments.py`, and documented:
> - `EXP-3-1`: `chapter03/exp_3_1_schema_constraints.py` (RDFS deductive typing vs. LPG prescriptive validation).
> - `EXP-3-2`: `chapter03/exp_3_2_entity_identity.py` (`owl:sameAs` equivalence closure, property unification, No-UNA catastrophic merge hazard).
> - `EXP-3-3`: `chapter03/exp_3_3_named_graphs.py` (Named graphs, TriG quad parsing, and cross-context SPARQL queries).
> - `EXP-3-4`: `chapter03/exp_3_4_nary_reification.py` (W3C Pattern 1 Qualified Relation vs. RDF Reification vs. N3 Quoted Statements).
> - `EXP-3-5`: `chapter03/exp_3_5_context_coexistence.py` (Contextual knowledge coexistence under varying experimental temperatures in Mechanism KG).
> - `EXP-3-6`: `chapter03/exp_3_6_identity_resolution.py` (Deterministic entity resolution pipeline: Blocking, IFP matching, Jaro-Winkler, and Fellegi–Sunter 3-zone decision boundary).

### EXP-3-1 — Schema modeling
- **Status:** ✅ COMPLETED (`chapter03/exp_3_1_schema_constraints.py`)

### EXP-3-2 — Entity identity / owl:sameAs
- **Status:** ✅ COMPLETED (`chapter03/exp_3_2_entity_identity.py`)

### EXP-3-3 — Named graphs
- **Status:** ✅ COMPLETED (`chapter03/exp_3_3_named_graphs.py`)

### EXP-3-4 — N-ary relation
- **Status:** ✅ COMPLETED (`chapter03/exp_3_4_nary_reification.py`)

### EXP-3-5 — Context modeling
- **Status:** ✅ COMPLETED (`chapter03/exp_3_5_context_coexistence.py`)

### EXP-3-6 — Identity-resolution exercise
- **Status:** ✅ COMPLETED (`chapter03/exp_3_6_identity_resolution.py`)

---

## GitHub issue sync

Synced 2026-08-25 (GitHub CLI authenticated):

- EXP-2-4 → issue #1
- EXP-2-5 → issue #2
- EXP-2-6 → issue #3

All labelled `lab`, `deferred`, `chapter-02`.

Synced 2026-08-25 (Chapter 3 labs):

- EXP-3-1 → issue #4
- EXP-3-2 → issue #5
- EXP-3-3 → issue #6
- EXP-3-4 → issue #7
- EXP-3-5 → issue #8
- EXP-3-6 → issue #9

All labelled `lab`, `deferred`, `chapter-03`. This file remains the design-level
source of truth; the issues track execution after Book v0.1.

---

## Chapter 7 — Deferred Acquisition/Integration Labs

### EXP-7-1 — R2RML mapping exercise

- **Pedagogical purpose:** Practice writing a Triples Map (subject map + predicate-object
  maps) transforming a small relational table into mechanism-KG-shaped RDF; contrast with
  Direct Mapping output.
- **Current design document:** `book/chapter07.md` §7.12 examples
- **Semantic contracts:** `docs/CHAPTER07_SEMANTIC_CONTRACTS.md` (Mapping Specification,
  Direct Mapping, Semantic Mapping)
- **Dependencies:** an R2RML processor (e.g., R2RML-Mapper)
- **Acceptance criteria:** identical table → identical RDF output across runs (determinism);
  output conforms to the mechanism target schema
- **Priority:** P2
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-7-2 — Record linkage on synthetic records

- **Pedagogical purpose:** Reproduce the Fellegi–Sunter two-threshold decision on a
  synthetic dataset (true matches, near-misses, homonyms); estimate m(γ)/u(γ) and inspect
  the three decision zones.
- **Current design document:** `book/chapter07.md` §7.10
- **Semantic contracts:** `docs/CHAPTER07_SEMANTIC_CONTRACTS.md` (Record Linkage,
  Candidate Generation, Blocking, Identity Decision)
- **Dependencies:** Python record-linkage toolkit or manual implementation
- **Acceptance criteria:** three-zone output matches hand-computed expectations on the
  synthetic dataset; clerical cases are isolated for review
- **Priority:** P2
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-7-3 — Content-hash idempotency harness

- **Pedagogical purpose:** Demonstrate idempotent ingestion: running the same ingestion
  twice produces no duplicate claims; a changed record produces a new hash and a new
  candidate without overwriting the old.
- **Current design document:** `book/chapter07.md` §7.14
- **Semantic contracts:** `docs/CHAPTER07_SEMANTIC_CONTRACTS.md` (Idempotent Ingestion,
  Content Hash)
- **Dependencies:** a small RDF store (RDFLib in-memory is sufficient)
- **Acceptance criteria:** second run leaves the graph unchanged; old claim persists after
  replacement
- **Priority:** P2
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-7-4 — SHACL gate demonstration

- **Pedagogical purpose:** Validate candidate mechanism triples against a SHACL shape
  (hasOperation, hasOutput required), and show that conformance passes do not imply
  acceptance.
- **Current design document:** `book/chapter07.md` §7.15
- **Semantic contracts:** `docs/CHAPTER07_SEMANTIC_CONTRACTS.md` (Structural Validation)
- **Dependencies:** pySHACL
- **Acceptance criteria:** intentionally malformed candidate fails; conforming-but-wrong
  candidate passes SHACL and is handled by the governance gate, not the SHACL gate
- **Priority:** P2
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-7-5 — Echo source detection

- **Pedagogical purpose:** Detect near-duplicate content between two sources and tag the
  derived source as an echo; recompute evidence counts excluding echo claims.
- **Current design document:** `book/chapter07.md` §7.23
- **Semantic contracts:** `docs/CHAPTER07_SEMANTIC_CONTRACTS.md` (Echo Source)
- **Dependencies:** content-hash + similarity join implementation (EXP-7-3 basis)
- **Acceptance criteria:** echo pair flagged; independent-evidence count decreases
  accordingly
- **Priority:** P3
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-7-6 — Pipeline versioning and reprocessing

- **Pedagogical purpose:** Run ingestion under pipeline version v1, change a normalization
  rule, re-run as v2; verify old candidates keep their v1 stamp and new candidates carry
  v2.
- **Current design document:** `book/chapter07.md` §7.24
- **Semantic contracts:** `docs/CHAPTER07_SEMANTIC_CONTRACTS.md` (Pipeline Versioning,
  Reprocessing)
- **Dependencies:** idempotency harness (EXP-7-3)
- **Acceptance criteria:** version stamps recorded in provenance; reprocessing is
  duplicate-free and old claims are not overwritten
- **Priority:** P3
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-7-7 — Integration policy engine

- **Pedagogical purpose:** Encode a small integration policy (accept/strengthen/supersede)
  and process a candidate cluster through it; record decision rationale for each verdict.
- **Current design document:** `book/chapter07.md` §7.28
- **Semantic contracts:** `docs/CHAPTER07_SEMANTIC_CONTRACTS.md` (Integration Policy,
  Integration Decision, Merge Outcome)
- **Dependencies:** claim ledger model from Chapter 6
- **Acceptance criteria:** verdicts match policy table; every decision has recorded
  rationale; superseded claims preserved
- **Priority:** P3
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-7-8 — Chain-of-custody provenance walk

- **Pedagogical purpose:** Reconstruct the full lineage of a claim from ledger back to
  source fragment (PROV chain) and verify invariants I1, I2, I5, I7 on a sample.
- **Current design document:** `book/chapter07.md` §7.19, §7.30
- **Semantic contracts:** `docs/CHAPTER07_SEMANTIC_CONTRACTS.md` (Lineage, Acquisition
  Invariant)
- **Dependencies:** EXP-7-3 and EXP-7-7 outputs
- **Acceptance criteria:** lineage traversal yields the expected chain; invariant checks
  pass on the sample
- **Priority:** P3
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

---

## GitHub issue sync (Chapter 7)

Not yet synced — deferred until Chapter 7 is ACCEPTED.
