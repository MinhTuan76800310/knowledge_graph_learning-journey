# CITE-01: Enabling Large Language Models to Generate Text with Citations (Gao et al., 2023)

- **Primary reference:** Gao, T., Yen, H., Yu, J. & Chen, D. (2023). Enabling Large Language Models to Generate Text with Citations. EMNLP 2023 (ALCE benchmark).
- **URL:** https://arxiv.org/abs/2305.14627
- **Status:** FETCHED_AND_VERIFIED (paper content read, 2026-08-30)
- **Used in:** Chapter 9
- **Canonical topic:** Citation generation and citation quality evaluation

## Key Points

- ALCE: benchmark for Automatic Long-form Citation Evaluation — answers must be fluent, correct, AND cited.
- Citation quality metrics: citation recall (fraction of statements with support) and citation precision (fraction of citations that actually support the statement).
- Even strong LLMs struggle to cite every claim completely.

## Semantic Contract

- Citation recall/precision measure whether each answer claim links to genuinely supporting evidence.
- A citation exists != the citation supports the claim.
- MUST NOT: treat citation presence as evidence; skip citation-completeness checks on important claims.
