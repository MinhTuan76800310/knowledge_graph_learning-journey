# DISTMULT-01: DistMult — Embedding Entities and Relations for Learning and Inference in Knowledge Bases

- **Primary reference:** Yang, B., Yih, W., He, X., Gao, J., Deng, L. (2015). "Embedding Entities and Relations for Learning and Inference in Knowledge Bases." *ICLR 2015* (arXiv:1412.6575).
- **URL:** https://arxiv.org/abs/1412.6575
- **Status:** FETCHED_AND_VERIFIED (arXiv abstract page, 2026-08-30)
- **Used in:** Chapter 8

## Key Points (fetched)

- Studies learning low-dimensional representations of entities and relations; shows several prior models unify under a framework where entities are vectors and relations act as bilinear and/or linear mappings.
- Reports a simple bilinear model reaching top-10 accuracy "73.2% vs. 54.7% by TransE on Freebase".
- Notes that "composition of relations is characterized by matrix multiplication" — relation composition is tied to matrix multiplication, which supports rule-like behavior.
- DistMult as a specific model: entity vectors h, t and a diagonal relation matrix (equivalently an elementwise product over the relation vector), scoring f_r(h,t) = ⟨h, r, t⟩ (sum of h_i · r_i · t_i).
- Known limitation (documented in the follow-up literature, e.g. ComplEx/ANALOGY): the symmetric bilinear score assigns the same score to (h, r, t) and (t, r, h), so it cannot model asymmetric relations directly.

## Semantic Contract

- Bilinear scoring is one design family (tensor decomposition); it is not truth semantics.
- Scores are plausibility estimates used for ranking; ranking is not entailment.
- The matrix-composition property is what connects DistMult-style models to (approximate) rule behavior — an inductive pattern, not a logical law.
- MUST NOT: claim DistMult scores are calibrated probabilities; claim symmetric scores imply symmetric truth.