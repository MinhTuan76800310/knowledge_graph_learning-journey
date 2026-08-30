# RRF-01: Reciprocal rank fusion (Cormack, Clarke & Buettcher, 2009)

- **Primary reference:** Cormack, G.V., Clarke, C.L.A. & Buettcher, S. (2009). Reciprocal rank fusion outperforms condorcet and individual rank learning methods. SIGIR 2009, 758-759.
- **URL:** https://doi.org/10.1145/1571941.1572114
- **Status:** FETCHED_AND_VERIFIED (bibliographic record, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** Rank fusion of multiple retrieval lists

## Key Points

- RRF score of a document = sum over systems of 1/(k + rank_i(d)), with k typically 60.
- Fuses ranked lists using only ranks, ignoring the raw scores of each system — robust to incomparable score scales.
- Well-suited for hybrid retrieval (lexical + dense + graph lists).

## Semantic Contract

- A fused rank is a retrieval-utility signal; it carries no epistemic meaning about whether the document's content is true.
- MUST NOT: interpret fused scores as confidence; claim RRF selects evidence; use RRF score as an assessment value.
