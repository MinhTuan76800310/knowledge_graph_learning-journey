# OWLRL-01: OWL-RL — RDF Closure Rules for RDFS and OWL 2 RL

- **URL:** https://github.com/RDFLib/OWL-RL
- **Status:** FETCHED_AND_VERIFIED
- **Used in:** Chapter 5 (English edition — real-world enrichment, §5.2, §5.3, §5.4, §5.13)
- **Document status:** Open-source tool, RDFLib project (stable)

## What this source establishes for Ch5
A pure-Python library that runs forward chaining to materialize RDFS and OWL 2 RL closures over
an RDFLib graph. It implements exactly the rdfs2/rdfs3/rdfs7/rdfs9 patterns of §5.3 and the OWL
2 RL/RDF rule set of §5.13, so `apply_rdfs` is the chapter's mechanism executed line for line.

## Safe simplifications
Citing OWL-RL as a concrete forward-chaining RDFS/OWL 2 RL materializer is safe.

## Dangerous simplifications / limits
It is a reference implementation, not a performance-tuned production reasoner. Do not claim it is
complete for full OWL 2 DL — it targets the RL profile, subject to the same Theorem PR1 caveat.
