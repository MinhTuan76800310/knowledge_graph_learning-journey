# Chapter 2 — Semantic Contracts

This document defines the semantic contracts for Chapter 2 experiments.
Experiments must teach exactly what is specified here and nothing beyond.

All contracts are derived from authoritative sources listed in `docs/source_index.json`.

---

## 1. RDF Abstract Data Model

**Source:** R11-02 (W3C RDF 1.1 Concepts), R11-01 (RDF 1.1 Primer)

### Contract

An RDF graph is a **set of triples**. Each triple consists of:

- **Subject**: an IRI or a blank node
- **Predicate**: an IRI
- **Object**: an IRI, a blank node, or a literal

Position constraints (RDF 1.1 §3):
- Subject position: IRI | BlankNode
- Predicate position: IRI only
- Object position: IRI | BlankNode | Literal

A **literal** has:
- A lexical form (string)
- A datatype IRI
- An optional language tag (only with `rdf:langString` datatype)

A **blank node** represents a resource that exists but is not named by an IRI. Blank-node
labels are local to a serialization and are not global identifiers; the intuitive semantics
are existential ("there exists some resource such that..."). Deeper formal semantics are
deferred beyond Chapter 2.

An **IRI** is a **globally scoped identifier mechanism**: any two systems can write the same
IRI string to refer to a resource. However, sharing an IRI does not by itself prove that two
parties attach the same real-world identity semantics to it, and two different IRIs do not
necessarily denote two different real-world entities. Identity alignment is a separate problem
(bridge to Chapter 3).

### Boundaries

- The RDF data model is abstract. It is NOT any particular serialization.
- Turtle, N-Triples, RDF/XML, JSON-LD are concrete syntaxes that serialize the same abstract model.
- Do not conflate "RDF" with "Turtle."

---

## 2. Turtle Serialization

**Source:** R11-05 (W3C Turtle REC 2014)

### Contract

Turtle is **one concrete syntax** for serializing RDF graphs.

Key features:
- Prefix declarations (`@prefix ex: <http://example.org/> .`)
- Subject-predicate-object statements terminated by `.`
- Semicolon (`;`) to repeat subject with different predicate-object pairs
- Comma (`,`) to repeat subject-predicate with different objects
- String literals with optional `^^datatype` or `@lang` suffix

### Boundaries

- Turtle is a syntax, not a data model.
- Two syntactically different Turtle documents may produce identical RDF graphs.
- Comparison of RDF content must be done at the graph level (parsed triples), not at the string level.

---

## 3. SPARQL Query Language

**Source:** SP11-01 (SPARQL 1.1 Overview), SP11-02 (SPARQL 1.1 Query)

### Contract

SPARQL operates on RDF graphs via **graph pattern matching**.

Core concepts:
- **Basic Graph Pattern (BGP)**: a set of triple patterns
- **Triple pattern**: like a triple but may contain variables (`?x`)
- **Solution mapping**: a binding from variables to RDF terms that makes the pattern match
- **SELECT query**: returns a table of solution mappings

Matching semantics (faithful to W3C SPARQL 1.1 Query, §"Basic Graph Pattern Matching"):
- A BGP is evaluated via **pattern instance mappings** (solution mappings): a mapping μ
  substitutes each variable with an RDF term such that the instantiated Basic Graph Pattern
  is a **subgraph of the active RDF graph**.
- The result of a BGP is the set of all such solution mappings.
- This is *subgraph* matching under variable instantiation. It is **not** injective graph
  isomorphism: distinct variables may bind to the same term unless constrained otherwise,
  and the match requires only that the instantiated pattern be contained in the graph.

### Boundaries

- SPARQL is NOT "SQL for graphs." This is at best a loose analogy for people familiar with SQL. The execution model, data model, and result structure differ fundamentally.
- SPARQL does not modify the graph (that requires SPARQL Update, covered separately).
- Variable names are local to the query.

---

## 4. Labeled Property Graph Model

**Source:** N4J-03 (Graph Data Modeling Fundamentals), N4J-05 (Neo4j Data Modeling)

### Contract

A labeled property graph consists of:

- **Nodes**: entities with zero or more **labels** and zero or more **properties** (key-value pairs)
- **Relationships**: directed, typed connections between nodes, with zero or more **properties**
- **Relationship type**: a single string label on each relationship
- **Identity**: each node and relationship has an internal identity (implementation-specific)

Key distinctions from RDF:
- Properties are key-value pairs attached directly to nodes/relationships (not separate triples)
- Relationships have exactly one type (not arbitrary IRIs)
- Labels classify nodes into sets (a node can have multiple labels)
- No built-in notion of IRI-based global identity

### Boundaries

- This describes the generic property graph concept.
- Neo4j is one implementation with specific behaviors (e.g., internal IDs, schema indexes, constraints).
- Distinguish "property graph model" from "Neo4j-specific semantics" when teaching.

---

## 5. Cypher Query Language

**Source:** N4J-06 (Neo4j Cypher Manual), GQL-02 (Cypher/GQL conformance)

### Contract

Cypher uses ASCII-art-style graph pattern matching:

- `MATCH (n:Label)-[r:TYPE]->(m)` — find nodes and relationships matching the pattern
- Variables (`n`, `r`, `m`) bind to matched elements
- `WHERE` clause filters by property values or other conditions
- `RETURN` clause projects results

### GQL Relationship

- **GQL** (ISO/IEC 39075:2024) is the ISO standard graph query language.
- Cypher has significant GQL alignment/conformance but is **not identical** to GQL.
- When teaching Cypher, note this relationship but do not equate them.

### Boundaries

- Cypher is specific to Neo4j (and compatible implementations).
- Do not present Cypher as a universal graph query standard.

---

## 6. Representation Boundary

### Contract

The same real-world knowledge does NOT imply the same graph structure across representations.

Representation choice affects:
- **Identity**: IRIs vs internal IDs vs external keys
- **Metadata placement**: properties on edges vs reified triples vs separate nodes
- **Relationship qualification**: n-ary relations require different modeling patterns in each model
- **Interoperability**: RDF has W3C standards; property graphs have vendor-specific formats
- **Formal semantics**: RDF/RDFS/OWL have model-theoretic semantics; property graphs typically lack standardized formal semantics
- **Inference facilities**: RDFS/OWL entailment vs application-level reasoning
- **Query ergonomics**: pattern matching syntax differs significantly
- **Serialization**: standardized RDF formats vs vendor-specific export formats

### Pedagogical Goal

Students should understand what each representation makes **easy, explicit, implicit, or costly** — not which is "better."
