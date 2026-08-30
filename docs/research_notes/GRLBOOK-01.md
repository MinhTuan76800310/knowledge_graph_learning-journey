# GRLBOOK-01: Graph Representation Learning (Hamilton)

- **Primary reference:** Hamilton, W. L. (2020). *Graph Representation Learning*. Morgan & Claypool Publishers / Synthesis Lectures on Artificial Intelligence and Machine Learning (open draft at cs.mcgill.ca).
- **URL:** https://www.cs.mcgill.ca/~wlh/grl_book/
- **Status:** FETCHED_AND_VERIFIED (book site + TOC, 2026-08-30)
- **Used in:** Chapter 8

## Key Points (fetched)

- The book covers: background and traditional approaches (feature engineering), node embeddings and neighborhood reconstruction, multi-relational data and knowledge graphs, the graph neural network model, and generative graph models.
- This is an authoritative academic treatment of representation learning on graphs, including the encoder–decoder framing of node embeddings and the message-passing formulation of GNNs.
- The message-passing GNN update (generic form): a node's representation at layer k+1 is computed from its current representation and aggregated messages from its neighbors — message → aggregate → update.
- The book also covers pool/readout mechanisms for graph- and subgraph-level representations (aggregating node representations into a whole-graph vector), which the Mechanism System needs for comparing mechanism applications as whole structures.

## Semantic Contract

- Node embeddings are task-derived representations; subgraph/graph representations are distinct artifacts (pooling is a modeling choice, not a definition of meaning).
- The generic message-passing formula is a family of models, not a single algorithm; the book must not claim one formula defines every GNN.
- Representations enable similarity estimates; similarity is evidence, never identity.
- MUST NOT: say an embedding is the entity; say a pooled subgraph vector is the subgraph's semantics; treat GNN outputs as formal interpretations.