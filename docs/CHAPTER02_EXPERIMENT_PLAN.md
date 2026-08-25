# Chapter 2 — Experiment Plan

**Domain:** Hanoi, Vietnam, Paris, France (reused from Chapter 1)

All experiments use the SAME domain to enable direct representation comparison.

---

## Experiment 2-1: RDF from First Principles / RDFLib ★

**Question:** "What exactly exists in an RDF graph?"

### Learning Objectives
- Construct an RDF graph programmatically using RDFLib
- Understand IRIs, literals, blank nodes as distinct node types
- Verify exact triple membership in a graph
- Observe that an RDF graph is a set of triples (no duplicates)

### Implementation
- File: `chapter02/exp_2_1_rdf_first_principles.py`
- Uses: RDFLib `Graph`, `URIRef`, `Literal`, `Namespace`
- Domain triples (identical content in pure-Python store and RDFLib):
  - `ex:Hanoi rdf:type ex:City`, `rdfs:label "Hà Nội"`
  - `ex:Hanoi ex:capitalOf ex:Vietnam`
  - `ex:Hanoi ex:sisterCity ex:Paris`
  - `ex:Paris rdf:type ex:City`, `rdfs:label "Paris"`, `ex:capitalOf ex:France`
  - `ex:Vietnam` / `ex:France` typed `ex:Country` with labels
  - (population literal introduced in 2-2/2-3 for literal/datatype contrast)
- Demonstrates: adding triples, iterating, checking membership, counting

### Tests
- Exact triple count after construction
- Specific triple membership assertions
- Literal datatype verification (xsd:integer, rdf:langString)
- IRI vs blank node distinction

### Source Contract
R11-02 (RDF 1.1 Concepts §3), TOOL-01 (RDFLib docs)

---

## Experiment 2-2: Turtle Serialization Round-Trip ★

**Question:** "What changes when representation is serialized?"

### Learning Objectives
- Serialize an RDF graph to Turtle text
- Parse Turtle text back into an RDF graph
- Verify graph-isomorphism (same knowledge, different representation)
- Understand that Turtle is ONE concrete syntax for RDF, not the model itself

### Implementation
- File: `chapter02/exp_2_2_turtle_serialization.py`
- Build same domain graph as 2-1
- Serialize to Turtle string
- Parse Turtle string into new graph
- Compare graphs using RDFLib's `isomorphic()` method
- Print Turtle output for human inspection

### Tests
- Round-trip produces isomorphic graph
- Turtle output contains expected prefixed names
- Parsed graph has same triple count
- NOT comparing raw Turtle strings (semantic comparison only)

### Source Contract
R11-05 (Turtle 1.1), R11-02 (RDF 1.1 Concepts §7)

---

## Experiment 2-3: SPARQL Basic Graph Patterns ★★

**Question:** "How does graph pattern matching answer a question?"

### Learning Objectives
- Write SPARQL SELECT queries with variables
- Understand Basic Graph Pattern (BGP) matching
- Observe solution mappings (variable bindings)
- Distinguish SPARQL pattern matching from SQL table joins

### Implementation
- File: `chapter02/exp_2_3_sparql_basic_patterns.py`
- Build same domain graph as 2-1
- Queries:
  1. Find all capitals: `?city ex:capitalOf ?country`
  2. Find sister cities of Hanoi: `ex:Hanoi ex:sisterCity ?sister`
  3. Find cities with population: `?city ex:population ?pop`
- Print solution mappings as variable binding dictionaries

### Tests
- Query 1 returns exactly 2 solution mappings (Hanoi/Vietnam, Paris/France)
- Query 2 returns exactly 1 binding (Paris)
- Query 3 returns integer literal binding
- Variable names match query specification

### Source Contract
SP11-02 (SPARQL 1.1 Query §3), SP11-01 (SPARQL 1.1 Overview)

---

## Experiment 2-4: Labeled Property Graph / Neo4j ★★ (DESIGN ONLY)

**Question:** "How does the same domain look when relationships and properties become first-class parts of a property graph?"

### Design Notes
- Uses Neo4j Python driver + Docker container
- Same domain: Hanoi, Vietnam, Paris, France
- Node labels: `City`, `Country`
- Relationship types: `CAPITAL_OF`, `SISTER_CITY`
- Properties on nodes: `name`, `population`
- Key difference from RDF: relationships can have properties directly
- No APOC required for basic operations

### Deferred To
Next work slice. Must be compatible with 2-6 comparison design.

### Source Contract
N4J-05 (Neo4j data modeling), N4J-06 (Cypher Manual)

---

## Experiment 2-5: Cypher Traversal ★★ (DESIGN ONLY)

**Question:** "How does Cypher pattern matching differ operationally and syntactically from SPARQL graph matching?"

### Design Notes
- Same queries as 2-3 but in Cypher syntax
- MATCH/RETURN pattern vs SELECT/WHERE
- ASCII-art relationship patterns: `(city)-[:CAPITAL_OF]->(country)`
- GQL conformance callout: Cypher aligns with ISO GQL but is not identical

### Deferred To
After 2-4 implementation.

### Source Contract
N4J-06 (Cypher Manual), GQL-02 (GQL conformance)

---

## Experiment 2-6: Same Knowledge — RDF vs Property Graph ★★★ (DESIGN ONLY)

**Question:** "What does each representation make easy, explicit, implicit, or costly?"

### Comparison Dimensions
1. **Identity**: IRIs vs internal node IDs + property-based identity
2. **Entity typing**: rdf:type triple vs node label
3. **Literal attributes**: object-position literal vs node property
4. **Relationship representation**: predicate IRI vs typed relationship
5. **Relationship metadata**: reification/n-ary vs relationship properties
6. **N-ary/contextual relations**: reification patterns vs relationship properties
7. **Schema/semantics**: RDFS/OWL entailment vs schema constraints
8. **Interoperability**: W3C standards vs vendor ecosystem
9. **Inference ecosystem**: reasoners vs application-level logic
10. **Query ergonomics**: SPARQL BGP vs Cypher ASCII patterns
11. **Serialization**: Turtle/N-Triples vs vendor export
12. **Standards**: W3C Recommendations vs ISO GQL alignment
13. **Implementation coupling**: multiple RDF stores vs Neo4j-specific

### Pedagogical Goal
No winner declared. Students understand trade-offs.

### Deferred To
After 2-4 and 2-5 are implemented.

---

## Dependency Order

```
2-1 (RDF basics) → 2-2 (Turtle) → 2-3 (SPARQL)
                                        ↓
                              2-4 (Property Graph) → 2-5 (Cypher)
                                        ↓
                                   2-6 (Comparison)
```

Experiments 2-1 through 2-3 are independent of Neo4j and can proceed immediately.
Experiments 2-4 through 2-6 require Neo4j Docker setup (ADR-002).
