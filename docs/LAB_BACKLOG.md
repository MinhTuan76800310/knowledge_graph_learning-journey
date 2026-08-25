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

## Chapter 2 — Deferred Property-Graph Labs

### EXP-2-4 — Labeled Property Graph in Neo4j

- **Pedagogical purpose:** Show how the same Hanoi/Vietnam/Paris/France domain looks
  when entities become nodes with labels and properties, and relationships become
  first-class typed, directed edges that can carry their own properties.
- **Current design document:** `docs/CHAPTER02_EXPERIMENT_PLAN.md` (Experiment 2-4)
- **Semantic contracts:** `docs/CHAPTER02_SEMANTIC_CONTRACTS.md` §4 (Labeled Property
  Graph Model), §6 (Representation Boundary). Sources N4J-03, N4J-05.
- **Dependencies:** Pinned Neo4j server (see `docs/decisions/ADR-002-neo4j-version.md`),
  Docker runtime, Neo4j Python driver (N4J-07).
- **Acceptance criteria:**
  - Creates the four-entity domain as nodes (`City`, `Country` labels) with properties.
  - Creates `CAPITAL_OF` and `SISTER_CITY` relationships with direction and type.
  - Direct semantic tests assert node labels, property values, and relationship
    endpoints — not stdout substrings.
  - Clearly distinguishes generic property-graph concepts from Neo4j-specific behavior.
- **Priority:** P1 (first property-graph lab after Book v0.1)
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-2-5 — Cypher Traversal

- **Pedagogical purpose:** Demonstrate how Cypher pattern matching differs operationally
  and syntactically from SPARQL graph matching, using the same domain.
- **Current design document:** `docs/CHAPTER02_EXPERIMENT_PLAN.md` (Experiment 2-5)
- **Semantic contracts:** `docs/CHAPTER02_SEMANTIC_CONTRACTS.md` §5 (Cypher Query
  Language). Sources N4J-06, GQL-02.
- **Dependencies:** EXP-2-4 (populated Neo4j graph), Neo4j Python driver.
- **Acceptance criteria:**
  - `MATCH` patterns return the same capital-of and sister-city facts as the SPARQL
    queries in EXP-2-3.
  - Tests assert exact returned bindings.
  - Includes the Cypher-vs-GQL conformance callout (Cypher aligns with GQL but is not
    identical).
- **Priority:** P1
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-2-6 — Same Knowledge: RDF vs Property Graph (executable comparison)

- **Pedagogical purpose:** The capstone comparison. Load the identical domain into both
  an RDF store and a property graph, then compare identity, typing, relationship
  metadata, n-ary modeling, schema, inference, interoperability, and query ergonomics
  by running real queries on both.
- **Current design document:** `docs/CHAPTER02_EXPERIMENT_PLAN.md` (Experiment 2-6)
- **Semantic contracts:** `docs/CHAPTER02_SEMANTIC_CONTRACTS.md` §6 (Representation
  Boundary). Sources R11-02, TOOL-01, N4J-05, N4J-06, S04.
- **Dependencies:** EXP-2-4 and EXP-2-5 (property-graph side), EXP-2-1/2-2/2-3 (RDF side).
- **Acceptance criteria:**
  - Same domain expressed in both representations.
  - Side-by-side query comparison for at least: entity lookup, relationship metadata,
    and one n-ary/contextual relation.
  - No declared "winner"; output frames what each representation makes easy, explicit,
    implicit, or costly.
- **Priority:** P2 (depends on both sides being runnable)
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

> **Note:** The *conceptual* content of EXP-2-6 is delivered in Book v0.1 as
> `book/chapter02.md` §2.4 "Same Knowledge, Different Representations," using diagrams,
> side-by-side tables, and static code examples. Only the runnable implementation is
> deferred.

---

## Backlog outside Chapter 2

Chapters 4–10 experiments are not yet designed. They will be added here as each
chapter is written, applying the same rule: defer any experiment that is not required
to validate a factual claim in the manuscript.

---

## Chapter 3 — Deferred Labs

The conceptual content of these labs is delivered in Book Preview v0.2 as
`book/chapter03.md` (diagrams, static examples, and citations). Only the runnable
implementations are deferred. No Docker work is performed in the book-first phase.

### EXP-3-1 — Schema modeling

- **Pedagogical purpose:** Let the reader design a small schema for the
  Hanoi/Vietnam domain on both sides: RDFS classes/properties/domain/range, and
  property-graph labels/types/constraints; then observe what each schema does and
  does not imply.
- **Semantic contracts:** `book/chapter03.md` §3.1 (schema ≠ ontology; domain/range
  are inference rules). Sources H01, S05, R11-03, N4J-05.
- **Dependencies:** RDFLib (RDF side); pinned Neo4j server (property-graph side).
- **Acceptance criteria:**
  - RDFS schema for the domain loads and yields the expected `rdf:type` entailments.
  - Property-graph schema uses labels, relationship types, and at least one
    uniqueness constraint.
  - A test asserts that `rdfs:domain` *infers* a type rather than rejecting data.
- **Priority:** P1
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-3-2 — Entity identity / owl:sameAs

- **Pedagogical purpose:** Make the propagation consequence of `owl:sameAs`
  executable: two graphs with `ex:Hanoi` and `wd:Q1858`, assert sameAs, and observe
  information merging; then assert `owl:differentFrom` and observe the no-UNA
  behavior (two names, no automatic distinctness).
- **Semantic contracts:** `book/chapter03.md` §3.2 (sameAs = identity; no UNA).
  Sources OWL-02, H01.
- **Dependencies:** RDFLib or an OWL-capable reasoner (e.g., owlrl) for entailment
  checks.
- **Acceptance criteria:**
  - Before sameAs: queries on `wd:Q1858` do not see `ex:Hanoi`'s properties.
  - After sameAs: properties of both names are visible under either name.
  - A wrong sameAs demonstrably merges unrelated entities (the hazard case).
- **Priority:** P1
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-3-3 — Named graphs

- **Pedagogical purpose:** Store the two sources as named graphs in an RDF dataset
  (TriG), query per-graph and across graphs, and demonstrate that the graph name
  carries no automatic provenance meaning.
- **Semantic contracts:** `book/chapter03.md` §3.3.2 (named graph = grouping;
  provenance is an application convention). Sources R11-02.
- **Dependencies:** RDFLib (ConjunctiveGraph/Dataset + TriG).
- **Acceptance criteria:**
  - Same triple stored in two named graphs; per-graph queries isolate it.
  - A test asserts the dataset structure (default graph + named graphs) and that
    nothing in the model states *who asserted* the triples.
- **Priority:** P2
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-3-4 — N-ary relation

- **Pedagogical purpose:** Implement the CapitalStatus pattern: binary
  `capitalOf` vs qualified relation entity with `validFrom`; compare query shapes.
- **Semantic contracts:** `book/chapter03.md` §3.3.3 (Pattern 1 of the N-ary note;
  reified edge does not assert the edge). Sources NARY-01, H01.
- **Dependencies:** RDFLib.
- **Acceptance criteria:**
  - Both representations encode "Hanoi capital of Vietnam since 1976".
  - Queries retrieve the temporal context in both; the n-ary form supports adding a
    second context dimension without schema surgery.
- **Priority:** P2
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-3-5 — Context modeling

- **Pedagogical purpose:** Attach source/time/scope context to the capital statement
  using at least two mechanisms (named graph + relationship property or n-ary), and
  show that context changes *evaluation*, not *truth*.
- **Semantic contracts:** `book/chapter03.md` §3.3 ("Context enables evaluation;
  context does not create truth."). Sources H01, WD-01, WD-02.
- **Dependencies:** EXP-3-3, EXP-3-4.
- **Acceptance criteria:**
  - The same statement is retrievable with different context annotations.
  - A conflicting population value from a second source coexists without deletion,
    each with its own context (Wikidata rank/qualifier analogue).
- **Priority:** P2
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

### EXP-3-6 — Identity-resolution exercise

- **Pedagogical purpose:** A guided, non-ML exercise: given two small source files
  with overlapping entities, the reader applies the candidate → evidence → accepted
  flow and produces sameAs/canonical-merge output; contrast with what automated
  blocking/matching would add (Chapter 7 preview).
- **Semantic contracts:** `book/chapter03.md` §3.2.5 and §3.4. Sources S06, H01.
- **Dependencies:** None beyond Python standard library + RDFLib.
- **Acceptance criteria:**
  - Exercise data contains true matches, near-misses, and homonyms.
  - Solution records evidence per candidate and only promotes candidates that pass
    the stated policy.
- **Priority:** P2
- **Status:** `DEFERRED_UNTIL_BOOK_V0.1`

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
