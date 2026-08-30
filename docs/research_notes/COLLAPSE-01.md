# COLLAPSE-01: Model Collapse — Training on Recursively Generated Data

- **Primary reference:** Shumailov, I., Shumaylov, Z., Zhao, Y., Gal, Y., Papernot, N., Anderson, R. (2024). "AI models collapse when trained on recursively generated data." *Nature*, 631, 755–759. Preprint: "The Curse of Recursion: Training on Generated Data Makes Models Forget" (arXiv:2305.17493).
- **URL:** https://arxiv.org/abs/2305.17493
- **Status:** FETCHED_AND_VERIFIED (arXiv abstract page, 2026-08-30; Nature version is paywalled, citation verified)
- **Used in:** Chapter 8

## Key Points (fetched)

- Studies what happens to future generative models once much online text and imagery is itself model-generated.
- Finds that training on such synthetic content can cause "irreversible defects in the resulting models, where tails of the original content distribution disappear" — this is **model collapse**.
- Demonstrates the effect on variational autoencoders, Gaussian mixture models, and LLMs; argues that preserving web-scale training benefits requires taking the problem seriously.

## Semantic Contract

- Recycling model-generated output as training data can distort learned distributions and reduce the independence of evidence — the same mechanism as the self-reinforcing feedback loop in the Mechanism System (model predicts → prediction re-enters training → model sees its own output again).
- The book uses this source cautiously: the relevant insight is contamination of evidence independence, not a blanket prohibition on any synthetic data.
- MUST NOT: claim model-generated knowledge is independent evidence; claim recycled predictions strengthen a claim; overstate the source beyond what it demonstrates (it is about distributional collapse, not about truth).