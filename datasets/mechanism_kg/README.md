# datasets/mechanism_kg/ — Canonical Mechanism-KG Running Dataset

The canonical, chapter-spanning dataset for the book's Mechanism-Knowledge-Graph
scenario (Chapters 1–6 and beyond). Chapters 1–6 reference the files in this
directory instead of re-inventing IRIs, so the running scenario is continuous.

## Files

| File | Purpose |
|------|---------|
| `rate_of_change.ttl` | The seed dataset: the `RATE_OF_CHANGE` mechanism family (classes, properties, persistent individuals) in canonical Turtle |

## Canonical vocabulary

The object vocabulary (class names, property names, persistent individuals) is
**frozen** in `docs/MECHANISM_KG_CANONICAL_MODEL.md`. Do not introduce new names
without updating that document. Naming conflicts are resolved there deliberately
(e.g. `Operation` is canonical; `MechanismOperation` is a deprecated alias;
`DerivativeApplication ⊑ MechanismApplication`).

## How chapters use it

- **Ch1** recognizes `RATE_OF_CHANGE` (`ex:rateOfChange_1`) as a first-class domain
  entity: "Velocity is the rate of change of position with respect to time."
- **Ch2** serializes and queries the same graph in RDF (Turtle + SPARQL) and LPG/Cypher.
- **Ch3** uses `ex:derivativeApplication_1` (the reified n-ary `DerivativeApplication`)
  for identity and context exercises.
- **Ch4** formalizes `RateOfChangeMechanism` and `DerivativeApplication` in OWL/DL.
- **Ch5** targets `ex:candidateRateOfChange_1` with SHACL shapes and inference rules.
- **Ch6** manages claims/evidence/provenance/time over the mechanism individuals.

## Status discipline

This directory contains **data only** (a canonical RDF graph). Formal OWL axioms and
SHACL shapes are taught in the manuscript and may be added to the dataset only when a
chapter introduces them. Property declarations appear here once the chapter that
introduces them has been remediated.
