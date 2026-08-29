# RDF-MT-01 — RDF 1.1 Semantics

**Source:** https://www.w3.org/TR/rdf11-mt/
**Status:** W3C Recommendation (2014-02-25)
**Used in:** Chapter 5

## Key findings

### Section 9 — RDFS Interpretations
An RDFS interpretation is an RDF interpretation satisfying additional semantic conditions for RDFS vocabulary. Defines IC, ICEXT, LV formally.

### Section 9.2.1 — Patterns of RDFS Entailment
Normative entailment patterns (not rules per se, but semantic conditions expressed as pattern tables):
- **rdfs2** (domain): `aaa rdfs:domain xxx` + `yyy aaa zzz` → `yyy rdf:type xxx`
- **rdfs3** (range): `aaa rdfs:range xxx` + `yyy aaa zzz` → `zzz rdf:type xxx`
- **rdfs5** (subPropertyOf transitivity)
- **rdfs7** (subPropertyOf use): `aaa rdfs:subPropertyOf bbb` + `xxx aaa yyy` → `xxx bbb yyy`
- **rdfs9** (subClassOf use): `xxx rdfs:subClassOf yyy` + `zzz rdf:type xxx` → `zzz rdf:type yyy`
- **rdfs11** (subClassOf transitivity)

### Appendix A — Rule-based operationalization (Informative)
- The entailment patterns CAN be viewed as left-to-right rules adding conclusions to a graph.
- Procedure: add axiomatic triples, apply patterns as rules to exhaustion, check subset.
- **Correctness:** If the procedure gives positive result, S does entail E.
- **Completeness caveat:** "It is not, however, complete" on standard RDF syntax.
- **Completeness recovery:** With generalized RDF (literals in subject position, blank nodes in predicate position), the rules become complete for both RDF and RDFS entailment.
- Closures are finite and decidable with polynomial complexity; simple entailment detection remains NP-complete.

## Claims supported
- RDFS domain/range are inference rules that ADD information (rdfs2, rdfs3 patterns)
- RDFS entailment is defined model-theoretically; rule-based approach is an operationalization
- Naive rule closure is correct but not complete on standard RDF syntax
- Completeness requires generalized RDF or additional mechanisms

## Safe simplifications
- Teaching the four main patterns (subClassOf, subPropertyOf, domain, range) as forward-chaining rules is pedagogically sound for the subset used in this book
- Saying "forward chaining computes RDFS closure" is acceptable when qualified: "for the subset of RDFS patterns covered here"

## Dangerous simplifications
- Saying "naive rule closure always computes every possible normative RDFS entailment" — FALSE without generalized RDF
- Conflating the rule-based operationalization with the normative model-theoretic definition
- Saying RDFS entailment IS forward chaining (it's defined semantically; forward chaining is one implementation)

## MUST NOT infer
- MUST NOT say rule-based closure is complete for all RDFS entailments without qualification
- MUST NOT present forward chaining as the definition of RDFS semantics (it's an implementation strategy)
- MUST NOT omit the completeness nuance when claiming rule-based approaches compute "the" RDFS closure
