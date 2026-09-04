# RETE-01: Rete: A Fast Algorithm for the Many Pattern/Many Object Pattern Match Problem

- **URL:** https://doi.org/10.1016/0004-3702(82)90020-0
- **Status:** FETCHED_AND_VERIFIED (DOI verified via Crossref: Artificial Intelligence 19(1):17–37, 1982, Elsevier)
- **Used in:** Chapter 5 (English + Vietnamese editions — Pillar 2 Part 2: rule-engine internals, §5.5)
- **Document status:** Peer-reviewed journal paper, Artificial Intelligence 19(1):17–37, 1982

## What this source establishes for Ch5
The original RETE network architecture that makes large rule sets tractable: **alpha nodes** (one-input, filter within a single pattern), **beta nodes** (two-input, join variable bindings across patterns and cache intermediate tuples in beta memory), **Working Memory Elements (WMEs)**, and the **agenda + conflict resolution** that decides which matched rule fires. Establishes the memory-for-speed trade-off and the reuse-of-partial-matches idea that the chapter connects to monotonicity / order-independence of lfp(T_P).

## Safe simplifications
Describing RETE as caching intermediate join results and exploiting the fact that most partial matches persist across data updates is faithful. Saying RETE "trades memory for speed" is the paper's own framing.

## Dangerous simplifications / limits
Do not claim RETE is the only or always-best rule-engine strategy — modern RDF engines (RDFox, see RDFOX-01) use different (semi-naive / parallel incremental Datalog) evaluation. Do not imply RETE changes the *result*: it computes the same lfp(T_P) as naive forward chaining, only faster. The 1982 paper is about production-rule systems (OPS5), not RDF/OWL specifically; the chapter's mapping to triple stores is an application, not the paper's original scope.
