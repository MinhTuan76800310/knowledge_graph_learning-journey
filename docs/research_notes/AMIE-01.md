# AMIE-01: AMIE+ — Fast Rule Mining in Ontological Knowledge Bases

- **Primary reference:** Galárraga, L., Teflioudi, C., Hose, K., Suchanek, F. M. (2015). "Fast Rule Mining in Ontological Knowledge Bases with AMIE+." *The VLDB Journal*, 24(5), 707–730.
- **DOI:** 10.1007/S00778-015-0394-1 (metadata verified via DBLP, 2026-08-30)
- **Status:** FETCHED_AND_VERIFIED (bibliographic record verified; technical content follows the published paper and the original AMIE WWW 2013 paper)
- **Used in:** Chapter 8

## Key Points

- Goal: mine association rules from knowledge bases that are *incomplete* (subject to the open-world assumption), at knowledge-graph scale.
- Rule patterns have the form r1(x, y) ∧ r2(y, z) → r3(x, z) — a path in the graph implies a third relation between the endpoints.
- Problem with standard data-mining support/confidence: a missing fact in an incomplete KB would count as a *violation* of the rule, unfairly lowering confidence. Under OWA, absence of a triple is not evidence of falsity.
- AMIE introduces support (number of instantiations of the body+head) and a confidence measure that only counts counterexamples against facts that *exist* in the KB, plus extensions in AMIE+:
  - PCA (Partial Completeness Assumption) confidence: when an entity has at least one value for the head relation, the KB is assumed complete for that entity–relation pair; confidence is computed only over the known instances. This reduces false penalization from incompleteness.
  - "Mostly confident" (MC) measure adds a margin for imbalanced cases.
- AMIE+ scales to KBs with millions of triples and supports more complex rule shapes (with constants, etc.) than the original AMIE.

## Semantic Contract

- Rule-mining confidence is a *frequency-style* measure computed under a dataset assumption (PCA); it is NOT an epistemic assessment of whether the rule is true in the world.
- Mined rules are candidate hypotheses derived from observed graph structure; they must be evaluated before any use.
- MUST NOT: treat AMIE confidence as Chapter 6 confidence; treat a mined rule as a logical law; say a rule with high confidence is universally true (counterexamples such as the capital-city/Vaduz case in HOGAN-IND-01).