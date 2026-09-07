# Knowledge Graph Book — Handoff & Next Phase Roadmap (v0.3 Released -> v0.4 Roadmap)

## Current Milestone State (v0.3.0 RELEASED — 2026-09-07)

- **Official Release**: [GitHub Release v0.3.0](https://github.com/MinhTuan76800310/knowledge_graph_learning-journey/releases/tag/v0.3.0)
- **Tag**: `v0.3.0`
- **Publication Assets**:
  - `knowledge-graph-book-v0.3.0.pdf` (Vietnamese, complete book, **434** print pages).
  - `knowledge-graph-book-en-v0.3.0.pdf` (English, complete book, **412** print pages).
  - 100% full bilingual parity across all 10 chapters, Front Matter, Afterword, Glossary, and Bibliography.
- **Verification Gates**:
  - `python -m pytest` → **106/106 tests passed**.
  - `python -m ruff check .` and `python -m ruff format --check .` → Clean.
  - XeLaTeX/PDF gate verification scripts passed for both language editions.

---

## The 6 Completed Theoretical Pillars (v0.3.0)

1. **Pillar 1 (Ch 1–3, PR #66):** Directed Hypergraphs $\mathcal{H} = (V, \mathcal{E})$, LPG 7-tuple, Blank Nodes First-Order Model Theory ($\exists x$), lean graph NP-hardness, Vector Fallacy matrix.
2. **Pillar 2 (Ch 4–5, PRs #68, #70):** Description Logics decidability landscape ($\mathcal{SROIQ}$ 2-NEXPTIME), $DL\text{-}Lite_R$ / OWL 2 QL FOL-rewritability, Datalog 3-way semantics equivalence, Stratified NAF.
3. **Pillar 3 (Ch 6–7, PRs #72, #74):** Dempster-Shafer theory of evidence ($m: 2^\Omega \to [0, 1]$), Subjective Logic opinion vectors & cumulative fusion $\oplus$, 2D Bitemporal Grid ($T_{\text{valid}} \times T_{\text{tx}}$), AGM belief revision postulates.
4. **Pillar 4 (Ch 8, PR #76):** Weisfeiler-Lehman (1-WL) expressive power ceiling on MPNNs, RotatE complex rotational algebra ($\mathbf{h} \circ \mathbf{r} = \mathbf{t}$), Poincaré hyperbolic embeddings ($\mathbb{B}^d$), Differentiable ILP ($\partial\text{ILP}$).
5. **Pillar 5 (Ch 9, PR #78):** Combinatorial path explosion bounds $O(\bar{d}^k)$, Multi-hop error cascading bounds ($p^k$), Personalized PageRank contraction mapping, Steiner Tree 2-approximation, GraphRAG vs 1M–2M Long-Context LLMs Pareto frontier, Physical Evidence Packet dossier.
6. **Pillar 6 (Ch 10, PR #80):** Cybernetic closed-loop feedback control with verification delay, DDE stability theorem ($\tau < \frac{\pi}{2a}$), Nyquist / Hopf bifurcation belief limit cycles, Knowledge Entropy ($H_K$), Autophagous model collapse variance shrinkage ($\sigma_{t+1}^2 = \sigma_t^2(1 - 1/M)$).

---

## Next Strategic Phase: Version 0.4.0 (Chapter 10+ Advanced Frontiers)

See detailed specification in [`docs/BOOK_V0_4_ROADMAP.md`](docs/BOOK_V0_4_ROADMAP.md).

### Planned Research Modules (Chapter 10+):
- **Module 11:** Neuro-Symbolic Information Extraction & Grammar-Constrained Decoding (CFG, Outlines, SymPy AST extraction).
- **Module 12:** High-Dimensional Vector-Graph Hybrid Entity Resolution (Bi-encoder dense blocking + Cross-encoder GNN scoring).
- **Module 13:** Embedding-Based & GNN-Based Ontology Alignment (GCN-Align / MuGNN across heterogeneous scientific ontologies).
- **Module 14:** Causal Mechanisms & Structural Causal Models (Judea Pearl's Causal Hierarchy: Association, Intervention, Counterfactuals on KGs).
- **Module 15:** Statistical Extraction Calibration & Conformal Prediction ($1 - \alpha$ coverage bounds for claim ingestion).

---

## Working Rules Reminder
- Language policy: Book manuscript in Vietnamese (`book/`) and English (`book-en/`) with 100% parity. Code, docs, tests, and commit messages in English.
- Author attribution: `MinhTuan76800310` (no Co-Authored trailer).
- Always verify GitHub state before claiming work done.
