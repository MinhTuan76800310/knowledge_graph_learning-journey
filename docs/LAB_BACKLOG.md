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

Chapters 3–10 experiments are not yet designed. They will be added here as each
chapter is written, applying the same rule: defer any experiment that is not required
to validate a factual claim in the manuscript.

---

## GitHub issue sync

Synced 2026-08-25 (GitHub CLI authenticated):

- EXP-2-4 → issue #1
- EXP-2-5 → issue #2
- EXP-2-6 → issue #3

All labelled `lab`, `deferred`, `chapter-02`. This file remains the design-level
source of truth; the issues track execution after Book v0.1.
