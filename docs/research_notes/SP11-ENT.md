# SP11-ENT — SPARQL 1.1 Entailment Regimes

**Source:** https://www.w3.org/TR/sparql11-entailment/
**Status:** W3C Recommendation (2013-03-21)
**Used in:** Chapter 5

## Key findings

### How entailment regimes are specified
Entailment regimes are specified via **SPARQL Service Description**, NOT via FROM clause:
- `sd:defaultEntailmentRegime` — the default regime for an endpoint
- `sd:entailmentRegime` — regime for a specific named graph

FROM clause selects graphs/datasets, not entailment regimes. This is a critical distinction.

### Standard entailment regime IRIs
- RDF: `http://www.w3.org/ns/entailment/RDF`
- RDFS: `http://www.w3.org/ns/entailment/RDFS`
- D-Entailment: `http://www.w3.org/ns/entailment/D`
- OWL 2 RDF-Based: `http://www.w3.org/ns/entailment/OWL-RDF-Based`
- OWL 2 Direct: `http://www.w3.org/ns/entailment/OWL-Direct`

### Default behavior
The default regime is whatever the endpoint declares via `sd:defaultEntailmentRegime`. There is no universal standard default — it's implementation/configuration-dependent.

## Claims supported
- Entailment regime is a configuration property of the SPARQL service/endpoint
- Service Description advertises supported regimes
- FROM ≠ entailment regime switch

## Safe simplifications
- Saying "the entailment regime is configured at the service level" is accurate
- Listing the standard regime IRIs as examples is fine

## Dangerous simplifications
- Saying "SPARQL uses FROM to select entailment regime" — WRONG
- Saying "SPARQL engines usually default to X" without source — implementation behavior is not a standard
- Implying there is a single universal default regime

## MUST NOT infer
- MUST NOT say FROM clause changes the entailment regime
- MUST NOT claim a universal default entailment regime without citing a specific implementation
- MUST NOT conflate graph selection (FROM) with semantic regime selection
