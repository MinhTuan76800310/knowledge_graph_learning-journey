# RLP-02: Apache Jena Inference / GenericRuleReasoner

- **URL:** https://jena.apache.org/documentation/inference/
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 4 (English edition - real-world enrichment)
- **Document status:** Apache Jena documentation (stable)

## What this source establishes for Ch4
Jena's GenericRuleReasoner supports forward/backward/hybrid strategies with a RETE-based forward engine, and Jena's RDFS/OWL reasoners are built on it - showing how RL-style entailment is implemented as deduction rules fired over a model.

## Safe simplifications
Citing Jena's rule reasoner as an RL-style mechanism is safe.

## Dangerous simplifications / limits
Jena's default OWL RL is a rule subset; do not present it as complete OWL 2 DL reasoning.
