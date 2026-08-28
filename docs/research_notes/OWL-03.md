# OWL-03: OWL 2 Structural Specification and Functional-Style Syntax

- **URL:** https://www.w3.org/TR/owl2-syntax/
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 4
- **Document status:** W3C Recommendation (2012-12-11)

## Key findings for Chapter 4

### Declarations (§5.8)
Declarations associate an IRI with an entity type: Class, Datatype, ObjectProperty, DataProperty, AnnotationProperty, NamedIndividual. They are explicitly **nonlogical**: "These axioms are nonlogical in the sense that they do not affect the consequences of an OWL 2 ontology." Purpose: vocabulary management, typing, disambiguation only.

### Annotations (§10)
"Annotations have no effect on the logical aspects of an ontology — that is, for the purposes of the OWL 2 semantics, annotations are treated as not being present." Axioms CAN carry annotations (axiomAnnotations), but those annotations still do not modify the axiom's logical meaning under Direct Semantics.

### Object vs Data Properties (§5.3, §5.4)
Object properties connect pairs of individuals. Data properties connect individuals with literals. Separate expression hierarchies: ObjectPropertyExpression (§6.1) vs DataPropertyExpression (§6.2). Under Direct Semantics, data property domains/ranges involve a separate data domain Δ_D.

### Class Expressions (§8)
All forms: Intersection (§8.1.1), Union (§8.1.2), Complement (§8.1.3), Enumeration/OneOf (§8.1.4), Existential/SomeValuesFrom (§8.2.1), Universal/AllValuesFrom (§8.2.2), HasValue (§8.2.3), HasSelf (§8.2.4), Min/Max/Exact Cardinality (§8.3). Data-property versions in §8.4–§8.5.

### OWL 2 DL Restrictions (§3, §11)
Global restrictions include property hierarchy constraints, axiom closure restrictions, typing constraints, declaration consistency, reserved vocabulary restrictions, datatype restrictions. These define what makes an ontology "OWL 2 DL" vs "OWL 2 Full."

### Structural Spec vs Direct Semantics (§1, §2.1)
The structural specification defines abstract constructs independent of serialization. Direct Semantics gives formal model-theoretic meaning to those constructs in a separate document.

## What this source establishes for Ch4
- Declaration nonlogical status
- Annotation semantic inertness under Direct Semantics
- Object/data property structural distinction
- Complete class expression taxonomy
- OWL 2 DL global restrictions

## Safe simplifications
- Omitting HasSelf and HasValue from initial exposition is safe; they're less common.
- Omitting detailed datatype restrictions is safe for Ch4 scope.

## Dangerous simplifications
- Saying declarations "state that a name exists" implies existential commitment they don't have.
- Saying annotations don't affect inference "unless linked to an axiom" is wrong — even axiom annotations don't change logical meaning.

## What this source does NOT justify
- Any claim about RDF-Based Semantics (separate document).
- Any claim about reasoning complexity (see Profiles spec).
