# RDFOX-01: Parallel Materialisation of Datalog Programs in Centralised, Main-Memory RDF Systems

- **URL:** https://doi.org/10.1609/aaai.v28i1.8730
- **Status:** FETCHED_AND_VERIFIED (DOI verified via AAAI OJS: https://ojs.aaai.org/index.php/AAAI/article/view/8730; authors Motik, Nenov, Piro, Horrocks, Olteanu; AAAI 2014)
- **Used in:** Chapter 5 (English + Vietnamese editions — Pillar 2 Part 2: rule-engine internals, §5.5)
- **Document status:** Peer-reviewed conference paper, AAAI 2014

## What this source establishes for Ch5
The algorithm paper behind **RDFox**: parallel, **lock-free incremental materialisation** of Datalog programs over a compressed, columnar, main-memory RDF representation. Establishes that a Datalog closure can be maintained incrementally (only the affected part recomputed on update) and evaluated in parallel without locks — the concrete counterpoint to sequential in-memory RETE engines.

## Safe simplifications
Characterising RDFox as doing parallel, lock-free, incremental Datalog materialisation over main-memory RDF is faithful to the paper. Contrasting it with sequential RETE (Forgy) as a different point on the memory/parallelism trade-off is accurate.

## Dangerous simplifications / limits
This is the *algorithm* paper, distinct from the RDFox *product/tool page* (registered separately as RLP-01); do not merge the two records or cite the tool page for the algorithmic claims. Do not claim parallel evaluation changes the semantics — it returns the same lfp(T_P); parallelism is an implementation property enabled by the order-independence of the fixpoint. Do not overstate: the paper targets centralised main-memory systems, not distributed clusters.
