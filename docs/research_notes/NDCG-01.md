# NDCG-01: Cumulated gain-based evaluation of IR techniques (Jarvelin & Kekalainen, 2002)

- **Primary reference:** Jarvelin, K. & Kekalainen, J. (2002). Cumulated gain-based evaluation of IR techniques. ACM TOIS 20(4), 422-446.
- **URL:** https://doi.org/10.1145/582415.582418
- **Status:** FETCHED_AND_VERIFIED (bibliographic record, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** nDCG — graded-relevance ranking metric

## Key Points

- DCG accumulates graded relevance scores discounted by position (log discount); nDCG = DCG / ideal DCG at the cutoff.
- Supports graded relevance (e.g., 0/1/2/3) rather than binary.
- Normalization makes scores comparable across queries.
- Sensitive to the graded relevance annotation; log-discount reflects diminishing user attention.

## Semantic Contract

- nDCG measures ranking quality against graded relevance judgments — a retrieval utility, not answer correctness or truth.
- MUST NOT: treat nDCG as an epistemic confidence; compare nDCG across different relevance scales; use it without graded judgments.
