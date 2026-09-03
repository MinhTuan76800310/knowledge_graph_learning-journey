# SPARQLALG-01: Semantics and Complexity of SPARQL

- **URL:** https://doi.org/10.1145/1567274.1567278
- **Status:** FETCHED_AND_VERIFIED (verified via DBLP + ACM DL record)
- **Used in:** Chapter 2 (English edition — v0.3 Pillar 1 enrichment, §2.1.6)
- **Document status:** Peer-reviewed journal paper, ACM Transactions on Database Systems 34(3):16:1–16:45, 2009
- **Authors:** Jorge Pérez, Marcelo Arenas, Claudio Gutiérrez

## What this source establishes for Ch2
This is the canonical reference for the compositional relational-algebra semantics of SPARQL:
evaluation is defined over *sets/multisets of solution mappings* μ, with Join (⋈), Left Join (⧑),
Filter (σ), and Union (∪) as the core operators. It also proves the complexity results the chapter
cites: BGP/UNION evaluation is NP-complete in **combined** complexity (query + data), while the
data complexity of conjunctive-query evaluation is in AC0.

## Safe simplifications
Presenting the four algebraic operators and the "NP-complete combined / AC0 data" split is safe
and faithful to the paper.

## Dangerous simplifications / limits
Do not state the NP-completeness as a *query-complexity* result — for a fixed database the problem
is a CSP over that database (tractable or NP-complete per the CSP dichotomy, not uniformly
NP-complete). The book's claim must be phrased as **combined complexity**. The paper's PSPACE
result applies to the full language *with* OPTIONAL; do not attribute PSPACE to plain BGPs.
