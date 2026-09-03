# SOUFFLE-01: Soufflé — On Synthesis of Program Analyzers

- **URL:** https://doi.org/10.1007/978-3-319-41540-6_23
- **Status:** FETCHED_AND_VERIFIED (verified via DBLP + Springer record)
- **Used in:** Chapter 5 (English edition — real-world enrichment, §5.2)
- **Document status:** Peer-reviewed conference paper, CAV 2016, LNCS 9779:422–430
- **Authors:** Herbert Jordan, Bernhard Scholz, Marko Subotić

## What this source establishes for Ch5
Soufflé compiles Datalog programs to parallel C++ and is used for large-scale static analysis
(points-to, taint). It is concrete industrial evidence that the abstract forward-chaining
recurrence G_{i+1} = G_i ∪ {θ(head(r)) | …} with a fixpoint stopping condition is not a toy
model but the actual inner loop of production rule engines.

## Safe simplifications
Citing Soufflé as a real Datalog/forward-chaining fixpoint engine is safe.

## Dangerous simplifications / limits
Soufflé is a program-analysis engine, not an RDF/OWL reasoner. Do not imply it implements RDFS
or OWL entailment regimes; it demonstrates the shared *fixpoint evaluation* mechanism, not the
same rule semantics.
