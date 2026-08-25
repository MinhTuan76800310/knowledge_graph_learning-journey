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

A **blank node** is an existential variable with local scope. It has no global identity.

An **IRI** is the universal identifier mechanism in RDF.

### Boundaries

- The RDF data model is abstract. It is NOT any particular serialization.
- Turtle, N-Triples, RDF/XML, JSON-LD are concrete syntaxes that serialize the same abstract model.
- Do not conflate "RDF" with "Turtle."

---

## 2. Turtle Serialization

**Source:** R11-04 (W3C Turtle REC 2014)

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

Matching semantics:
- A BGP matches against an RDF graph when there exists a substitution of variables such that all resulting triples are present in the graph.
- SPARQL matching is based on subgraph isomorphism for BGPs.

### Boundaries

- SPARQL is NOT "SQL for graphs." This is at best a loose analogy for people familiar with SQL. The execution model, data model, and result structure differ fundamentally.
- SPARQL does not modify the graph (that requires SPARQL Update, covered separately).
- Variable names are local to the query.

---

## 4. Labeled Property Graph Model

**Source:** NG-03 (Neo4j Graph Data Modeling Fundamentals), Neo4j documentation

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

**Source:** NG-02 (Neo4j Cypher Manual), GQL-02 (Cypher/GQL conformance)

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
