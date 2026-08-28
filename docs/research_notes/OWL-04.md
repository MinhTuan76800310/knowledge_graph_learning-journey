# OWL-04: OWL 2 Direct Semantics

- **URL:** https://www.w3.org/TR/owl2-direct-semantics/
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 4
- **Document status:** W3C Recommendation (2012-12-11)

## Key findings for Chapter 4

### Interpretation (§2.2)
An interpretation I is a **10-tuple**: (Δ^I, Δ_D, ·^C, ·^OP, ·^DP, ·^I, ·^DT, ·^LT, ·^FA, NAMED). Critically, there is a **separate data domain Δ_D** that is nonempty and **disjoint** from the object domain Δ^I. The manuscript's pedagogical simplification I = (Δ^I, ·^I) omits this — acceptable for initial exposition but must be introduced when discussing data properties.

### Class semantics (§2.2)
·^C maps each class to a subset of Δ^I. owl:Thing → Δ^I, owl:Nothing → ∅.

### Object property semantics (§2.2)
·^OP maps each object property to a subset of Δ^I × Δ^I.

### Data property semantics (§2.2)
·^DP maps each data property to a subset of Δ^I × Δ_D. This confirms data properties relate objects to data values, NOT objects to objects.

### Satisfaction conditions (§2.3)
- SubClassOf(CE1,CE2): (CE1)^C ⊆ (CE2)^C
- EquivalentClasses: (CEj)^C = (CEk)^C for all j,k
- DisjointClasses: (CEj)^C ∩ (CEk)^C = ∅ for j≠k
- FunctionalObjectProperty(OPE): ∀x,y1,y2: (x,y1)∈OPE^OP ∧ (x,y2)∈OPE^OP ⇒ y1=y2
- InverseFunctionalObjectProperty(OPE): ∀x1,x2,y: (x1,y)∈OPE^OP ∧ (x2,y)∈OPE^OP ⇒ x1=x2
- ObjectSomeValuesFrom(OPE,CE): {x | ∃y: (x,y)∈OPE^OP ∧ y∈CE^C}
- ObjectAllValuesFrom(OPE,CE): {x | ∀y: (x,y)∈OPE^OP ⇒ y∈CE^C}
- Cardinality: based on #{y | (x,y)∈OPE^OP ∧ y∈CE^C} ≥n / ≤n / =n

### Entailment (§2.5)
O entails O1 iff every model of O is also a model of O1. Purely semantic relation.

### Declarations (§1)
NO logical consequences. "used only to disambiguate … therefore, they are not mentioned explicitly in this document."

### Annotations (§1)
NO logical consequences. "All these types of annotations, however, have no semantic meaning in OWL 2 and are ignored in this document."

### Direct Semantics vs RDF serialization
Direct Semantics operates on structural-specification constructs, not on RDF triples. OWL 2 ontologies are "primarily exchanged as RDF documents" but the semantics operates on the structural form. **Serialization syntax ≠ semantic regime.**

## What this source establishes for Ch4
- Complete formal definition of interpretation including separate data domain
- All satisfaction conditions used in the chapter
- Declaration and annotation nonlogical status confirmed
- Serialization ≠ semantic regime

## Safe simplifications
- Using simplified I = (Δ^I, ·^I) for object-level concepts is safe IF data domain is introduced separately.
- Omitting datatype interpretation details (·^DT, ·^LT, ·^FA) is safe for Ch4 scope.

## Dangerous simplifications
- Completely omitting Δ_D when discussing data properties.
- Saying declarations "state existence" — they don't under Direct Semantics.
- Implying Direct Semantics requires non-RDF format.

## What this source does NOT justify
- Claims about RDF-Based Semantics behavior (separate document).
- Claims about reasoning complexity or tractability (see Profiles spec).
- Any implementation-specific behavior of particular reasoners.
