# RGCN-01: R-GCN — Modeling Relational Data with Graph Convolutional Networks

- **Primary reference:** Schlichtkrull, M., Kipf, T. N., Bloem, P., van den Berg, R., Titov, I., Welling, M. (2018). "Modeling Relational Data with Graph Convolutional Networks." *European Semantic Web Conference (ESWC) 2018* (arXiv:1703.06103).
- **URL:** https://arxiv.org/abs/1703.06103
- **Status:** FETCHED_AND_VERIFIED (arXiv abstract page, 2026-08-30)
- **Used in:** Chapter 8

## Key Points (fetched)

- Introduces Relational Graph Convolutional Networks (R-GCNs), developed "specifically to deal with the highly multi-relational data characteristic of realistic knowledge bases".
- Applied to two standard knowledge base completion tasks: link prediction (recovering missing facts) and entity classification (recovering missing entity attributes).
- Architecture from the paper: each node's representation at layer k+1 aggregates messages from its neighbors, where the transformation depends on the relation type of the incoming edge (relation-specific transformation matrices); self-loop included.
- Regularization: basis decomposition and block-diagonal decomposition over relation transformations to control parameters for many relation types.
- Link prediction setup: R-GCN used as an *encoder* producing entity representations, fed into a *decoder* factorization model (DistMult) that scores triples; trained with negative sampling (corrupted triples). Shows "a large improvement of 29.8% on FB15k-237 over a decoder-only baseline".
- Lesson for the book: the encoder–decoder split (graph structure → representations → scoring) and the need for relation-specific message passing.

## Semantic Contract

- R-GCN is a representative relational GNN, taught to expose the design principle "relation types matter in message passing" — not as a deployment requirement.
- Neighborhood aggregation conflates relation types only if the model ignores them; relation-specific transformation is the fix.
- Representations remain task artifacts; they are not formal semantics of the entities.
- MUST NOT: claim GNN outputs are interpretations of the graph; claim R-GCN "understands" relations.