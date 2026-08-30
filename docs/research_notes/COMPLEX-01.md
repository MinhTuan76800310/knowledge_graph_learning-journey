# COMPLEX-01: ComplEx — Complex Embeddings for Simple Link Prediction

- **Primary reference:** Trouillon, T., Welbl, J., Riedel, S., Gaussier, É., Bouchard, G. (2016). "Complex Embeddings for Simple Link Prediction." *Proceedings of the 33rd International Conference on Machine Learning (ICML 2016)* (arXiv:1606.06357).
- **URL:** https://arxiv.org/abs/1606.06357
- **Status:** FETCHED_AND_VERIFIED (arXiv abstract page, 2026-08-30)
- **Used in:** Chapter 8

## Key Points (fetched)

- Addresses link prediction via latent factorization using complex-valued embeddings.
- Claims to model many binary relations, "including symmetric and antisymmetric ones", more simply than prior work, scaling linearly in space and time.
- Technical model (from the paper): entities and relations are embedded as complex vectors; the score of (h, r, t) uses the Hermitian dot product: Re(⟨e_h, w_r, conj(e_t)⟩) — the complex conjugate of the tail vector breaks the symmetry that DistMult suffers from, so the score of (h, r, t) can differ from (t, r, h).
- Contrast with DistMult: both are tensor-decomposition models; DistMult is a special case (imaginary parts zero); ComplEx adds the ability to model antisymmetric relations.
- Comparisons in the paper are drawn against Neural Tensor Networks and Holographic Embeddings.

## Semantic Contract

- ComplEx is taught as a representative of the tensor-decomposition family with a specific inductive bias (conjugation for directionality) — not as a universal model.
- Complex embeddings are still vectors: they do not encode formal semantics or meaning.
- The design lesson is that different scoring families encode different inductive biases about relations; no single model is right for every relation type.
- MUST NOT: claim complex-valued coordinates carry semantic meaning; claim ComplEx handles all relation patterns.