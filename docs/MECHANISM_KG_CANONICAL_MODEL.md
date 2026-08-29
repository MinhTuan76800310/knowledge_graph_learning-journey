# Mechanism-KG Canonical Model

**Status:** FROZEN (pedagogical baseline for Chapters 1–6 remediation)
**Date:** 2026-08-29
**Seed mechanism:** `RATE_OF_CHANGE`
**Canonical source sentence:** *"Velocity is the rate of change of position with respect to time."*

This document is the canonical pedagogical object model used by the running
Mechanism-Knowledge-Graph scenario across Chapters 1–6. It is a **frozen minimal
vocabulary** so that every chapter references the same individuals, classes, and
relations with the same names. It is a pedagogical model, not the production ontology
(see §6).

---

## 1. Why a frozen model

The whole-book depth audit found:

- Chapters 1–3 contain zero mechanism-domain examples.
- The few mechanism objects that exist are scattered across Ch4 §4.13, Ch5 §5.18, and
  Ch6 §6.16–6.17, with **inconsistent naming**: `DerivativeOperation` in Ch4 vs
  `MechanismOperation` in Ch5, and an **ungrounded `Condition`** in Ch5.
- No persistent individuals survive from one chapter to the next.

The remediation freezes the minimal set below so the scenario evolves continuously:
RAW PASSAGE → domain objects → graph representation → identity/context → formal
mechanism model → inference + validation → claim/evidence/provenance/time → later
acquisition/integration.

The book's Introduction says the capstone ontology is "not predefined" and every
modeling decision must be justified. That principle stands for **deferred depth** —
richer classes (`Experiment`, `Experience`, `Event`, …) remain unmodeled until a
chapter needs them. What is now frozen is only the **minimum seed** required for a
coherent Chapters 1–6 thread, plus the justification below for each decision.

---

## 2. Canonical classes

| Canonical name | Meaning (short) | Introduced | Book-defined vs standard-aligned |
|----------------|-----------------|------------|----------------------------------|
| `ex:Mechanism` | A transform/process that takes inputs and produces an output under conditions, e.g. rate of change, heat transfer | Ch1 (recognition) | Book-defined domain class |
| `ex:RateOfChangeMechanism` | A `Mechanism` that operates by computing a rate of change of one quantity with respect to another | Ch4 §4.13 (formal axiom) | Book-defined; the working mechanism |
| `ex:Operation` | A transform primitive a mechanism can perform (generalization) | Ch4 (implied) | Book-defined |
| `ex:DerivativeOperation` | The specific operation *differentiate X with respect to Y* | Ch4 §4.13 | Book-defined; subtype of `Operation` |
| `ex:MechanismApplication` | The act/context of applying a mechanism to concrete inputs | Ch2 (serialization) | Book-defined |
| `ex:DerivativeApplication` | An `MechanismApplication` binding mechanism + differentiand + reference variable + operation into one reified object | Ch3 (n-ary) [promoted from Ch4 sketch] | Book-defined; subtype of `MechanismApplication` |
| `ex:Quantity` | A measurable input/output (position, velocity, temperature) | Ch4 §4.13 (in Ch1-2 recognition only) | Book-defined |
| `ex:ReferenceVariable` | The independent variable a rate is taken with respect to (time) | Ch4 §4.13 | Book-defined |
| `ex:Condition` | A qualifying circumstance in which the mechanism applies (now grounded — see §4) | Ch5 | Book-defined |
| `ex:CandidateMechanism` | A mechanism extracted/inferred from evidence, not yet accepted | Ch5 | Book-defined |
| `ex:Claim` | A first-class epistemic object: assertion + source + time + evidence + governance state | Ch6 | Book-defined epistemic layer |
| `ex:Evidence` | Information supporting or challenging a claim; **≠ source**, **≠ claim** | Ch6 | Book-defined epistemic layer |
| `ex:Source` | Where an assertion came from (textbook, paper, LLM prompt) | Ch6 | Book-defined epistemic layer |
| `ex:Observation` | A raw recorded observation that starts the epistemic pipeline | Ch6 | Book-defined |
| `ex:CandidateKnowledge` | Knowledge proposed but not yet independently verified (incl. all LLM output) | Ch6 | Book-defined |
| `ex:AcceptedKnowledge` | Knowledge that has passed the evidence/governance gate | Ch6 | Book-defined |

**Deferred (Introduction menu, not in minimal set):** `Concept`, `Definition`,
`Experiment`, `Experience`, `Event`, `TimeInterval`, `Hypothesis`. They are announced
in the Introduction as future capstone vocabulary but are deliberately **not frozen**
here — they add no load-bearing structure to Chapters 1–6 and would violate
*Defers Depth, Never Required Understanding*.

---

## 3. Canonical relations

| Canonical name | Domain → Range | Meaning | Introduced |
|----------------|----------------|---------|------------|
| `ex:hasOperation` | `Mechanism → Operation` | The operation a mechanism performs | Ch4 |
| `ex:hasApplication` | `Mechanism → MechanismApplication` | A concrete application of the mechanism | Ch4 |
| `ex:hasInput` | `Mechanism → Quantity` | An input quantity to the mechanism | Ch4 |
| `ex:hasOutput` | `Mechanism → Quantity` | The quantity the mechanism computes | Ch2 (dataset) |
| `ex:hasValue` | `Quantity → xsd:double` | The measured numeric value of a quantity | Ch2 (dataset) |
| `ex:hasReferenceVariable` | `Mechanism → ReferenceVariable` | The independent variable of the rate | Ch4 |
| `ex:hasCondition` | `Mechanism → Condition` | A circumstance constraining application | Ch5 |
| `ex:differentiand` | `DerivativeApplication → Quantity` | The quantity being differentiated | Ch3 (n-ary) |
| `ex:withRespectTo` | `DerivativeApplication → ReferenceVariable` | The variable of differentiation | Ch3 (n-ary) |
| `ex:requires` | `Mechanism → Mechanism` | A mechanism depends on another | Ch5 |
| `ex:hasEvidence` | `Claim → Evidence` | Evidence attached to a claim | Ch6 |
| `ex:hasSource` | `Claim → Source` | Where the claim's assertion came from | Ch6 |
| `ex:hasObservation` | `Claim → Observation` | The observation that grounds the claim | Ch6 |

Ch6 additionally aligns with PROV-O where provenance is modeled: `wasDerivedFrom`,
`wasAttributedTo`, `wasGeneratedBy` on the epistemology classes (§5).

---

## 4. Naming reconciliation

**Resolved deliberately.** The following drift found by the audit is now canonical:

1. **`Operation` is canonical; `MechanismOperation` is a deprecated alias.**
   - Ch4 §4.13 introduced `DerivativeOperation` (correct — a specific operation).
   - Ch5 §5.18 used `MechanismOperation` for the same idea (the generic operation of
     a mechanism). It is renamed to `ex:Operation` everywhere in Ch5; `DerivativeOperation`
     remains the subtype used by `RATE_OF_CHANGE`. Ch5's references to "each Mechanism
     must have at least one …" now read `ex:Operation` / `ex:DerivativeOperation`.

2. **`DerivativeApplication ⊑ MechanismApplication`.**
   - `MechanismApplication` is the generic class (application of a mechanism to
     inputs). `DerivativeApplication` is the specialized reified n-ary relation
     binding `hasOperation`, `differentiand`, `withRespectTo` in one object.
   - Ch5 §5.18's `Condition` is introduced via `ex:hasCondition` in Ch5 instead of
     appearing ungrounded.

3. **`Condition` becomes grounded (Ch5).** It no longer appears as a bare name; the
   chapter's SHACL shapes and rules now target `ex:Condition` instances linked via
   `ex:hasCondition`.

4. **`Quantity` vs `MechanismInput`.** The Introduction's generic `MechanismInput` is
   **superseded** by `ex:Quantity` for the running scenario (inputs of
   `RATE_OF_CHANGE` are measurable quantities: position, velocity, temperature).
   `MechanismInput` is recorded as a deprecated alias in the registry, not used in
   the thread.

5. **Epistemic class names** (`Claim`, `Evidence`, `Source`, `Observation`,
   `CandidateKnowledge`, `AcceptedKnowledge`) match Ch6, which already defines them.
   No new names invented.

---

## 5. Persistent individuals

The following individuals persist across chapters (created in `datasets/mechanism_kg/`,
referenced by Ch1–6):

| Individual | Type | Role in scenario |
|------------|------|------------------|
| `ex:rateOfChange_1` | `RateOfChangeMechanism` | **Main running mechanism**: computes velocity as the rate of change of position with respect to time |
| `ex:derivativeOperation_1` | `DerivativeOperation` | The operation `rateOfChange_1` performs (differentiate position wrt time) |
| `ex:velocity_1` | `Quantity` | Output of the mechanism (what it computes) |
| `ex:position_1` | `Quantity` | Input differentiand of `rateOfChange_1` |
| `ex:time_1` | `ReferenceVariable` | The independent variable of the rate |
| `ex:derivativeApplication_1` | `DerivativeApplication` | Reified binding of the above four into one application |
| `ex:heatTransferRate_2` | `RateOfChangeMechanism` | Second mechanism (rate of change of thermal energy wrt time), used for identity/comparison exercises |
| `ex:newtonCooling_1` | `RateOfChangeMechanism` | Composite: Newton's law of cooling, `requires` the rate-of-change capability and the heat-transfer model |
| `ex:candidateRateOfChange_1` | `CandidateMechanism` | Ch5: a candidate derived from a second textbook source, awaiting validation |
| `ex:claim_1` … | `Claim` | Ch6: mechanism claims carrying source, time, confidence, governance state |

Outside-the-thread examples (Hanoi/city/country, capital-of, etc.) remain valid for
generic teaching; the thread is *in addition*, per the remediation mandate that every
MAJOR concept gets a Mechanism-KG worked application.

---

## 6. Pedagogical status and standard alignment

- **Book-defined domain.** The mechanism ontology (`Mechanism`, `Operation`,
  `Application`, `Quantity`, `ReferenceVariable`, `Condition`) is a pedagogical model
  built to teach KG mechanics. Ch4's warning stands: the flat definition of
  `RateOfChangeMechanism` is a "pedagogical toy structural signature" and is refined
  by the `DerivativeApplication` intermediate object. It is **not** the production
  ontology of a real mechanism-reasoning system.
- **Book-defined epistemology.** `Observation → Assertion → Claim → Evidence →
  Accepted Knowledge` is explicitly book-defined (Ch6); it is not a W3C standard.
- **Standard-aligned where standards exist:** RDF/OWL/SHACL/SPARQL vocabulary per the
  Standards Version Policy; PROV-O (`prov:Entity`, `prov:Activity`, `prov:Agent`)
  for provenance; Wikidata statement terminology (qualifiers, references, ranks) cited
  as external reference; OWL-Time acknowledged for temporal entities (deferred).

---

## 7. Evolution by chapter (target state)

| Chapter | What the thread does with the model |
|---------|-------------------------------------|
| Ch1 | Recognizes `Mechanism` as a first-class KG entity: a mechanism triple beside the city triple; the same mechanism as a labeled, meaningless structure in the §1.6 Step 2 data graph; an annotated mechanism triple (source + confidence + timestamp) as the full KG in Step 5; assertion ≠ accepted-knowledge for mechanisms in §1.8 |
| Ch2 | Serializes and queries the thread: Turtle triples for `newtonCooling_1`, SPARQL BGP over `hasOperation`/`requires`, IRI-vs-literal policy on mechanism elements, the equivalent LPG/Cypher structure, and the RDF-vs-LPG tradeoff paragraph on mechanism data |
| Ch3 | Identity and context over the thread: `DerivativeApplication` as the working n-ary relation (promoted from Ch4's sketch), conceptual identity of the same mechanism under two IRIs (definitional equivalence), named-graph per source, two-source integration mini-case |
| Ch4 | Formal semantics on the thread: interpretation `Δ^I = {m₁, d₁, q₁, r₁}` over mechanism elements, the `RateOfChangeMechanism` axiom, DL axioms for `DerivativeApplication`, two-model demonstration of the existential-filler flaw, OWA/satisfiability questions for mechanisms |
| Ch5 | Inference + validation on the thread: forward-chaining θ trace over mechanism IRIs, `CandidateMechanism` SHACL shape in body text, mechanism 2×2 consistency-vs-validation scenario, mechanism graph-repair case |
| Ch6 | Epistemic management of the thread: mechanism claims with full metadata, evidence/provenance chains, temporal validity (Newtonian → relativistic), governance transitions, bitemporal query |
| (Ch7+) | Acquisition/integration continues the same individuals (not modeled here — Chapter 7 begins in a new session) |
