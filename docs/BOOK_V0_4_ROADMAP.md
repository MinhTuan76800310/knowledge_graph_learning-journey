# v0.4.0 Specification: Advanced Frontiers (Chapter 10+ & Post-v0.3 Roadmap)

**Target Milestone:** v0.4.0 (Post-v0.3 Frontier Research Extension)  
**Primary Focus:** Neuro-Symbolic Agent Long-Term Memory, Verifiable Scientific World Models, and Causal Mechanism Substrates for Autonomous AI Agents.

---

## 1. Motivation & Strategic Purpose

Following the completion of the core 10-chapter curriculum (v0.1–v0.3), Version 0.4 addresses cutting-edge theoretical and architectural requirements demanded by frontier AI research labs (Google DeepMind, OpenAI, Anthropic) and competitive PhD scholarship standards:

> *"How does an autonomous agent use a Knowledge Graph not merely as an external static database, but as a verifiable, self-updating, and causally sound neuro-symbolic world model?"*

While Chapters 1–10 establish formal semantics, deduction, epistemics, acquisition pipelines, geometric embeddings, and GraphRAG, Version 0.4 expands beyond classic knowledge engineering into **modern neuro-symbolic integration and scientific causality**.

---

## 2. Advanced Curriculum Modules (Chapter 10+)

### Module 11: Neuro-Symbolic Information Extraction & Constrained Decoding
- **Limitation in Ch 7:** Traditional extraction treats the LLM/extractor as an opaque black box producing candidate triples.
- **Frontier Theoretical Upgrade:**
  1. **Grammar-Constrained Decoding:** Formalizing Context-Free Grammar (CFG) and regular-expression decoding (e.g., Outlines, Guidance, Jsonformer) to guarantee that generative LLMs produce syntactically and semantically valid Turtle/JSON-LD conforming to pre-compiled SHACL shapes without syntax hallucination.
  2. **OpenIE vs. Ontology-Guided Extraction:** Mathematical formulations for Open Information Extraction (discovering novel predicates/types) versus Closed/Ontology-Guided Extraction (mapping to an established TBox).
  3. **Mathematical Expression & Equation Extraction:** Parsing scientific equations (e.g., Navier-Stokes, differential kinematics) into symbolic Abstract Syntax Trees (ASTs / SymPy / Content MathML) directly linked to mechanism nodes.

---

### Module 12: High-Dimensional Vector-Graph Hybrid Entity Resolution
- **Limitation in Ch 7:** Fellegi–Sunter (1969) is optimized for tabular databases with discrete categorical fields (names, dates, addresses).
- **Frontier Theoretical Upgrade:**
  1. **Bi-Encoder Dense Semantic Blocking:** Embedding scientific entities, mechanism descriptions, and textual fragments into dense vector space $\mathbb{R}^d$ for sub-linear approximate nearest neighbor (ANN) candidate retrieval.
  2. **Cross-Encoder & Graph Matching Scoring:** Fine-grained re-ranking using joint text-graph encoders that evaluate both semantic similarity and neighborhood structural isomorphism.
  3. **Bridging Likelihood Ratios with Vector Manifolds:** Formal probabilistic calibration linking cosine similarity $\cos(\theta)$ to Fellegi–Sunter log-likelihood agreement ratios $m_i / u_i$.

---

### Module 13: Embedding-Based & GNN-Based Ontology Alignment
- **Limitation in Ch 7:** Focuses on relational-to-RDF mapping (Direct Mapping, R2RML), omitting heterogeneous graph-to-graph ontology matching.
- **Frontier Theoretical Upgrade:**
  1. **Graph Neural Network Alignment (GCN-Align / MuGNN):** Aligning independent scientific ontologies (e.g., Classical Mechanics $\leftrightarrow$ Biochemical Signaling Pathways) across disjoint vector representations.
  2. **Multi-Aspect Similarity Fusion:** Combining lexical embedding similarity, structural topological distance, and logical constraint preservation.
  3. **LLM-Guided Schema Mediation:** Automated discovery of schema bridging rules verified against formal OWL consistency checkers.

---

### Module 14: Causal Mechanisms & Structural Causal Models (SCMs)
- **Limitation in Ch 7:** Mechanisms are modeled as functional operators (inputs, outputs, operations).
- **Frontier Theoretical Upgrade:**
  1. **Judea Pearl's Causal Hierarchy on Graphs:** Formally distinguishing:
     - Layer 1: *Association* $P(y|x)$ (observational edges).
     - Layer 2: *Intervention* $P(y | do(x))$ (causal generative mechanism edges).
     - Layer 3: *Counterfactuals* $P(y_x | x', y')$ (retrospective mechanism evaluation).
  2. **Structural Causal Model (SCM) Integration:** Embedding causal DAGs with non-parametric structural equations into the Knowledge Graph to prevent confounding and enable autonomous intervention planning by AI agents.
  3. **Causal Discovery from Literature:** Distinguishing correlational claims from verified causal mechanisms during automated knowledge ingestion.

---

### Module 15: Statistical Extraction Calibration & Conformal Prediction
- **Limitation in Ch 6 & 7:** Extraction confidence is treated as a subjective or uncalibrated scalar.
- **Frontier Theoretical Upgrade:**
  1. **Expected Calibration Error (ECE):** Measuring and mitigating miscalibration in neural extractions ($P(\text{correct} \mid \text{confidence} = p) = p$).
  2. **Conformal Prediction on Knowledge Graphs:** Constructing prediction sets $\mathcal{C}(X)$ of candidate triples that provably contain the true ground-truth relation with finite-sample statistical coverage guarantee $1 - \alpha$:
     $$P(Y \in \mathcal{C}(X)) \ge 1 - \alpha$$
  3. **Risk-Controlled Ingestion:** Enforcing that only extractions satisfying rigorous conformal error bounds enter the Claim Ledger as `Candidate` or `Accepted`.

---

## 3. Implementation Status & Pre-requisites

- **Prerequisite:** Completion of v0.3 Core Curriculum (Chapters 1–10 in both Vietnamese and English editions).
- **Target Audience:** Researchers, PhD students, and frontier lab research engineers working at the intersection of Knowledge Graphs, Neuro-Symbolic AI, and Autonomous Agents.
