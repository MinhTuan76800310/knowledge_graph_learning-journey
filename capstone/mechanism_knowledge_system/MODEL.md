# Mechanism Knowledge System — Evolving Model

**Status:** SEED (frozen minimal model, Chapter 1–6 scope)
**Date:** 2026-08-29
**Seed mechanism:** RATE_OF_CHANGE — *"Velocity is the rate of change of position with respect to time."*

This document is the living capstone model. It starts at the seed frozen for Chapters
1–6 and grows as later chapters add acquisition, integration, learning, and retrieval.

---

## 1. What the system is

A **Mechanism Knowledge System** is a knowledge graph whose central entities are
*mechanisms* — transforms that take inputs and produce outputs under conditions — plus
the machinery to acquire, formalize, validate, and epistemically manage statements
about them.

The system is not a single database; it is a pipeline:

```
RAW PASSAGE
    ↓  (Ch1) recognize domain objects
domain objects
    ↓  (Ch2) graph representation (RDF and LPG)
graph representation
    ↓  (Ch3) identity / context
identity/context
    ↓  (Ch4) formal mechanism model (OWL/DL)
formal mechanism model
    ↓  (Ch5) inference + validation (rules, SHACL)
inference + validation
    ↓  (Ch6) claim / evidence / provenance / time
claim/evidence/provenance/time
    ↓  (Ch7+) acquisition / integration / learning
production knowledge system
```

## 2. Canonical object model (frozen seed)

The class/property/individual vocabulary is canonical in
`docs/MECHANISM_KG_CANONICAL_MODEL.md`; the RDF data lives in
`datasets/mechanism_kg/rate_of_change.ttl`. Summary:

- **Classes:** `Mechanism`, `RateOfChangeMechanism`, `Operation`,
  `DerivativeOperation`, `MechanismApplication`, `DerivativeApplication`,
  `Quantity`, `ReferenceVariable`, `Condition`, `CandidateMechanism`,
  plus the epistemic classes `Claim`, `Evidence`, `Source`, `Observation`,
  `CandidateKnowledge`, `AcceptedKnowledge`.
- **Relations:** `hasOperation`, `hasApplication`, `hasInput`, `hasOutput`,
  `hasReferenceVariable`, `hasCondition`, `requires`, `differentiand`,
  `withRespectTo`, and Ch6's epistemic relations (`hasEvidence`, `hasSource`,
  `hasObservation`).
- **Running individuals:** `ex:rateOfChange_1` (primary), `ex:heatTransferRate_2`
  (comparison), `ex:derivativeApplication_1/2`, `ex:candidateRateOfChange_1`.

## 3. Book-defined vs standard-aligned

- **Book-defined:** the mechanism domain ontology and the epistemic model
  (Observation → Assertion → Claim → Evidence → Accepted Knowledge). Both are
  pedagogical; neither claims to be a W3C standard.
- **Standard-aligned:** RDF/OWL/SHACL/SPARQL semantics; PROV-O for provenance;
  Wikidata statement terminology as external reference; OWL-Time acknowledged for
  temporal entities.

## 4. Design principles

1. **Every modeling decision is justified.** The Introduction says the capstone
   ontology is not pre-given; each class/relation added here is justified in the
   chapter that needs it.
2. **Defer depth, never required understanding.** Richer classes (`Experiment`,
   `Experience`, `Event`, `TimeInterval`, `Hypothesis`, `Concept`, `Definition`) are
   announced in the Introduction but deliberately not modeled in Chapters 1–6.
3. **The graph is the running example.** Every MAJOR concept in the book instantiates
   this system, not just the city/country domain.
4. **Asserted ≠ inferred ≠ accepted.** The system keeps the asserted graph, the
   inferred closures, and the epistemic governance layer separate.
