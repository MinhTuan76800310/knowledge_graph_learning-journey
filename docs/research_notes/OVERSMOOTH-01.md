# OVERSMOOTH-01: Deeper Insights into Graph Convolutional Networks for Semi-Supervised Learning

- **Primary reference:** Li, Q., Han, Z., Wu, X.-M. (2018). "Deeper Insights into Graph Convolutional Networks for Semi-Supervised Learning." *Proceedings of the 32nd AAAI Conference on Artificial Intelligence (AAAI 2018)* (arXiv:1801.07606).
- **URL:** https://arxiv.org/abs/1801.07606
- **Status:** FETCHED_AND_VERIFIED (arXiv abstract page, 2026-08-30)
- **Used in:** Chapter 8

## Key Points (fetched)

- Argues that graph convolution is a "special form of Laplacian smoothing" — this explains why GCNs work but also why "stacking many convolutional layers" creates "potential concerns of over-smoothing".
- Deep networks increasingly smooth vertex features; with many layers, node representations become too similar (less distinguishable), reducing discriminative power and hurting performance.
- Proposes co-training and self-training to improve learning with few labels and remove the need for extra validation labels.

## Semantic Contract

- "More GNN layers = more understanding" is false: deep stacking can destroy the distinctions that matter.
- Local message passing smooths neighborhood information; similarity from message passing is not identity, and global structure may be invisible to a few local hops.
- Oversmoothing is taught conceptually (not as a survey) to explain a real failure mode of GNNs in the Mechanism System.
- MUST NOT: claim deeper GNNs are always better; claim message-passing similarity equals semantic identity.