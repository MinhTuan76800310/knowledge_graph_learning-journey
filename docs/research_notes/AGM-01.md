# AGM-01: On the Logic of Theory Change

- **URL:** https://www.jstor.org/stable/2274659
- **Status:** FETCHED_AND_VERIFIED (Crossref-indexed reprint DOI 10.1007/978-3-319-20451-2_13 confirms exact title + all three authors; original is Journal of Symbolic Logic 50(2):510-530, 1985)
- **Used in:** Chapter 6 (English + Vietnamese editions — Pillar 3: AGM belief revision, §6.13)
- **Document status:** Peer-reviewed journal article, Journal of Symbolic Logic 50(2):510-530, 1985

## What this source establishes for Ch6
The **AGM postulates** for rational belief change: three operations on a belief set K = Cn(K) — expansion (K + phi), contraction (K div phi), and revision (K * phi); the **Levi identity** K * phi = (K div not phi) + phi and the dual **Harper identity** K div phi = K intersect (K * not phi); and the **principle of minimal information loss** (change no more than the new information forces). Cited in §6.13 to formalise why a Claim Ledger prefers non-destructive supersession over classical destructive revision.

## Safe simplifications
Stating that AGM defines expansion, contraction, and revision, and that revision = contract-the-negation-then-expand, is safe. Summarising the postulates at an introductory level (closure, success, minimal change, consistency preservation) is standard.

## Dangerous simplifications / limits
Do not claim the book *implements* full AGM revision. AGM postulates are about logically closed belief sets, not raw RDF graphs. Do not assert that a Claim Ledger satisfies every AGM postulate in the technical sense; the book only argues the ledger architecture is *compatible with the spirit of* AGM because it never deletes prior claims — it projects an active belief set over an append-only graph.
