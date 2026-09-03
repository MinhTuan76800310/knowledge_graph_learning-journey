# GDM-01: An Introduction to Graph Data Management

- **URL:** https://doi.org/10.1007/978-3-319-96193-4_1
- **Status:** FETCHED_AND_VERIFIED (verified via DBLP + Springer record)
- **Used in:** Chapter 2 (English edition — v0.3 Pillar 1 enrichment, §2.2.1)
- **Document status:** Peer-reviewed book chapter, in *Graph Data Management* (Springer LNCS 11510), pp. 1–32, 2018
- **Authors:** Renzo Angles, Claudio Gutiérrez

## What this source establishes for Ch2
Angles & Gutiérrez give the formal definition of the labeled property graph as an attributed graph
structure: a finite set of nodes and edges with an incidence function, node/edge labeling functions,
and partial property functions mapping (element, key) pairs to values. The chapter's 7-tuple
G = (V, E, ρ, λ_V, λ_E, σ_V, σ_E) is a faithful, slightly expanded rendering of this definition
(splitting the labeling and property functions into node and edge components, and allowing a node to
carry a *set* of labels as Neo4j does).

## Safe simplifications
Citing this as the academic reference for the formal property-graph data model is safe.

## Dangerous simplifications / limits
The book's 7-tuple is an adaptation, not a verbatim quote: the original uses a single labeling
function λ over V ∪ E and a single property function σ over (V ∪ E) × K. The split into λ_V/λ_E and
σ_V/σ_E, and the powerset λ_V: V → P(L_V) for multi-label nodes, are the book's pedagogical
refinement to match Neo4j semantics. Do not claim the exact 7-tuple appears in the paper.
