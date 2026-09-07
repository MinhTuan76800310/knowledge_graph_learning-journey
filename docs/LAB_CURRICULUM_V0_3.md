# Master Executable Lab Curriculum — Knowledge Graph Book (v0.3.0)

This document contains the canonical engineering specifications, mathematical formulations, and test oracles for all **42 executable hands-on labs** across Chapters 1–10 of the Knowledge Graph monograph.

Each lab is designed to be:
1. **Fully Executable & Automated:** Run via Python 3.12+ and verified via `pytest`.
2. **Pedagogically Aligned:** Directly instantiating the formal concepts and semantic contracts established in the manuscript.
3. **Capstone-Centered:** Anchored in the **Mechanism Knowledge Graph** (`datasets/mechanism_kg/rate_of_change.ttl`) or the canonical City/Country domain.
4. **Hermetic & Self-Contained:** Runs in local test environments with zero external network dependencies (Dockerized services have in-memory mocks for CI).

---

## 🗺️ Curriculum Matrix (Chapters 1–10)

> **Current Implementation Status:** **18 Labs Executable** (`pytest`: 131 passed across Ch1–3) | **24 Labs Target Specifications** (Pending implementation for Ch4–10) | **Target Total: 42 Labs**.

| Chapter | Title | Lab Range | Status | Test Module |
|---|---|:---:|:---:|---|
| **Ch 1** | From Graph to Knowledge | `EXP-1-1` $\to$ `EXP-1-5` | ✅ Complete (5 labs) | `chapter01/test_experiments.py` (25 tests) |
| **Ch 2** | Data Models & Query Languages | `EXP-2-1` $\to$ `EXP-2-7` | ✅ Complete (7 labs) | `chapter02/test_ch2_experiments.py` (40 tests) |
| **Ch 3** | Schema, Identity, Context | `EXP-3-1` $\to$ `EXP-3-6` | ✅ Complete (6 labs) | `chapter03/test_ch3_experiments.py` (15 tests) |
| **Ch 4** | Ontologies & Formal Meaning | `EXP-4-1` $\to$ `EXP-4-3` | 🚧 3 Labs to Build | `chapter04/test_ch4_experiments.py` |
| **Ch 5** | Deduction, Rules, Validation | `EXP-5-1` $\to$ `EXP-5-4` | 🚧 4 Labs to Build | `chapter05/test_ch5_experiments.py` |
| **Ch 6** | Claims, Epistemics, Time | `EXP-6-1` $\to$ `EXP-6-4` | 🚧 4 Labs to Build | `chapter06/test_ch6_experiments.py` |
| **Ch 7** | Acquisition & Integration | `EXP-7-1` $\to$ `EXP-7-6` | 🚧 6 Labs to Build | `chapter07/test_ch7_experiments.py` |
| **Ch 8** | Inductive Learning & Graph ML | `EXP-8-1` $\to$ `EXP-8-5` | 🚧 5 Labs to Build | `chapter08/test_ch8_experiments.py` |
| **Ch 9** | Retrieval & GraphRAG | `EXP-9-1` $\to$ `EXP-9-6` | 🚧 6 Labs to Build | `chapter09/test_ch9_experiments.py` |
| **Ch 10**| Living Knowledge Systems | `EXP-10-1` $\to$ `EXP-10-5` | 🚧 5 Labs to Build | `chapter10/test_ch10_experiments.py` |

---

## 🔬 Detailed Lab Specifications

### Chapter 2: Data Models and Query Languages (Missing Property Graph Labs)

#### `EXP-2-5`: Labeled Property Graph (LPG) Modeling & Ingestion
- **File:** `chapter02/exp_2_5_labeled_property_graph.py`
- **Pedagogical Purpose:** Implement the formal 7-tuple LPG model $\mathcal{G} = (V, E, \Sigma_V, \Sigma_E, \lambda_V, \lambda_E, \mu)$. Show how entities become nodes with multiple labels, and relationships become directed typed edges carrying arbitrary key-value properties.
- **Dual Engine Architecture:**
  - *Docker Mode:* Connects to Neo4j via official Python driver (`neo4j`).
  - *In-Memory Mode:* Pure-Python LPG engine providing identical graph operations without external daemon requirements.
- **Domain Data:**
  - Nodes: `(:City {name: "Hà Nội", population: 8053663})`, `(:Country {name: "Việt Nam"})`
  - Edges: `(Hanoi)-[:CAPITAL_OF {since: 1976, status: "Official"}]->(Vietnam)`
  - Mechanism nodes: `(:Mechanism {id: "m1", name: "RateOfChange"})-[:APPLIES_OPERATION {order: 1}]->(:Operation {type: "Derivative"})`
- **Test Oracle (`test_ch2_experiments.py`):**
  - `test_lpg_node_creation_and_labels`: Verify nodes can hold multiple labels.
  - `test_lpg_relationship_properties`: Assert relationship property `since: 1976` is directly accessible on the edge without reification.
  - `test_lpg_directionality`: Assert `CAPITAL_OF` is directed from City to Country.

#### `EXP-2-6`: Cypher Pattern Matching & Graph Traversal
- **File:** `chapter02/exp_2_6_cypher_traversal.py`
- **Pedagogical Purpose:** Demonstrate declarative graph traversal using Cypher ASCII-art syntax and compare its operational semantics with SPARQL BGPs.
- **Query Implementations:**
  1. *Entity Lookup:* `MATCH (c:City)-[:CAPITAL_OF]->(cntry:Country) RETURN c.name, cntry.name`
  2. *Undirected Match:* `MATCH (c:City)-[r:SISTER_CITY]-(other:City) RETURN c.name, other.name, r.agreementDate`
  3. *Variable-Length Path:* `MATCH p = (m:Mechanism)-[:REQUIRES*1..3]->(dep) RETURN length(p), nodes(p)`
- **Test Oracle:**
  - Assert exact returned bindings matching the SPARQL queries in `exp_2_3`.
  - Assert that undirected pattern `-(:SISTER_CITY)-` matches in both directions while directed `->` preserves asymmetry.

#### `EXP-2-7`: RDF vs. Property Graph Executable Benchmark
- **File:** `chapter02/exp_2_7_rdf_vs_property_graph.py`
- **Pedagogical Purpose:** The capstone dual-representation comparison. Load identical facts into RDFLib and LPG, executing queries side-by-side.
- **Comparison Axes:**
  1. Entity attribute lookup (`population`)
  2. Relationship traversal (`capitalOf`)
  3. Edge metadata query (reification quad vs relationship property)
  4. N-ary relation traversal (Derivative application with reference variable)
- **Test Oracle:**
  - Measure execution latency, memory footprint, and code ergonomics. Assert zero semantic divergence in answers.

---

### Chapter 3: Schema, Identity, and Context (6 Labs)

#### `EXP-3-1`: RDFS Entailment vs. Property Graph Schema Constraints
- **File:** `chapter03/exp_3_1_schema_constraints.py`
- **Pedagogical Purpose:** Contrast deductive typing against prescriptive validation.
- **Implementation:**
  - RDFS side: Declare `ex:capitalOf rdfs:domain ex:City; rdfs:range ex:Country`. Assert `ex:MysteryNode ex:capitalOf ex:Vietnam`. RDFS infers `ex:MysteryNode a ex:City`.
  - LPG side: Define uniqueness and non-null constraints. Insert unclassified node; LPG rejects data.
- **Test Oracle:**
  - `test_rdfs_domain_infers_type`: Assert `(ex:MysteryNode, RDF.type, ex:City)` is inferred.
  - `test_property_graph_rejects_missing_required_property`: Assert constraint violation exception.

#### `EXP-3-2`: Entity Identity & `owl:sameAs` Information Merging
- **File:** `chapter03/exp_3_2_entity_identity.py`
- **Pedagogical Purpose:** Demonstrate identity propagation under `owl:sameAs` and the catastrophic merge hazard under No Unique Name Assumption (No UNA).
- **Implementation:**
  - Graph A: `ex:Hanoi ex:population 8053663`.
  - Graph B: `wd:Q1858 wdt:P1082 8246540; rdfs:label "Ha Noi"@en`.
  - Assert `ex:Hanoi owl:sameAs wd:Q1858`.
- **Test Oracle:**
  - `test_same_as_merges_triples`: Querying `ex:Hanoi` returns Wikidata label and population.
  - `test_incorrect_same_as_collapses_distinct_entities`: Assert catastrophic merge when `DaNang owl:sameAs Hanoi` is asserted.

#### `EXP-3-3`: Named Graphs & TriG Quad Datasets
- **File:** `chapter03/exp_3_3_named_graphs.py`
- **Pedagogical Purpose:** Partitioning knowledge across named graphs and demonstrating that graph IRIs do not convey provenance by default.
- **Implementation:**
  - Store diverging population counts in `ex:census2019` and `ex:census2023` graphs using TriG.
  - Execute SPARQL queries with `GRAPH ?g { ... }` and default graph unions.
- **Test Oracle:**
  - Assert that querying without `GRAPH` clause returns the union of assertions without contradiction.

#### `EXP-3-4`: N-ary Relations & Reification Patterns
- **File:** `chapter03/exp_3_4_nary_reification.py`
- **Pedagogical Purpose:** Model temporal relationships using W3C N-ary Relation Pattern 1 vs. RDF reification vs. RDF-star.
- **Implementation:**
  - Encode "Hanoi is capital of Vietnam valid from 1976 with official status".
  - Pattern 1: `CapitalStatus` event node with relations.
  - RDF-star: `<< :Hanoi :capitalOf :Vietnam >> :validFrom 1976 ; :status "Official"`.
- **Test Oracle:**
  - Assert SPARQL queries extract all temporal qualifiers across both representations.

#### `EXP-3-5`: Contextual Knowledge Coexistence
- **File:** `chapter03/exp_3_5_context_coexistence.py`
- **Pedagogical Purpose:** Demonstrate that conflicting measurements in the Mechanism KG coexist validly under distinct experimental contexts.
- **Test Oracle:**
  - Query measurements conditioned on temperature ($25^\circ\text{C}$ vs $100^\circ\text{C}$); assert zero graph corruption.

#### `EXP-3-6`: Deterministic Entity Resolution Pipeline
- **File:** `chapter03/exp_3_6_identity_resolution.py`
- **Pedagogical Purpose:** Implement rule-based entity resolution: Blocking on prefix/soundex, Jaro-Winkler string similarity, InverseFunctionalProperty matching (`ex:doi`, `ex:taxId`), and threshold zones.
- **Test Oracle:**
  - Classify benchmark record pairs into Match, Non-Match, and Clerical Review with precision $\ge 0.95$.

---

### Chapter 4: Ontologies and Formal Meaning (3 Labs)

#### `EXP-4-1`: OWL 2 DL Entailment & Subsumption Reasoning
- **File:** `chapter04/exp_4_1_owl_reasoning.py`
- **Pedagogical Purpose:** Run Description Logics reasoning over Mechanism TBox using `owlrl`.
- **Implementation:**
  - Define class subsumption: `RateOfChangeMechanism ⊑ ChangeMechanism ⊑ Mechanism`.
  - Define property restrictions: `DerivativeApplication ⊑ ∃hasOperation.DerivativeOperation`.
- **Test Oracle:**
  - Assert deductive closure generates all implicit `rdf:type` and `rdfs:subClassOf` triples.

#### `EXP-4-2`: $DL\text{-}Lite_R$ / OWL 2 QL First-Order Query Rewriting Prototype
- **File:** `chapter04/exp_4_2_fol_rewriting.py`
- **Pedagogical Purpose:** Implement backward-chaining ontological query rewriting (Calvanese et al., 2007).
- **Implementation:**
  - Input: Conjunctive SPARQL query $q(x) \leftarrow \text{Mechanism}(x)$.
  - TBox: $\text{RateOfChangeMechanism} \sqsubseteq \text{Mechanism}, \text{AggregationMechanism} \sqsubseteq \text{Mechanism}$.
  - Rewriting Engine: Produces SQL Union of Conjunctive Queries (UCQ) executed on relational tables without storing inferred triples.
- **Test Oracle:**
  - Verify that SQL UCQ query result is 100% equivalent to full graph materialization.

#### `EXP-4-3`: Open World Assumption (OWA) vs. Inconsistency Detection
- **File:** `chapter04/exp_4_3_owa_vs_cwa.py`
- **Pedagogical Purpose:** Contrast missing data under OWA with formal contradiction and class unsatisfiability (`owl:Nothing`).
- **Test Oracle:**
  - Assert that missing properties return unproven (not false). Assert that membership in disjoint classes triggers inconsistency.

---

### Chapter 5: Deduction, Rules, and Validation (4 Labs)

#### `EXP-5-1`: Datalog Knaster-Tarski Forward-Chaining Fixpoint Engine
- **File:** `chapter05/exp_5_1_datalog_fixpoint.py`
- **Pedagogical Purpose:** Build an in-memory Datalog engine computing least fixpoints via the immediate consequence operator $T_P \uparrow \omega$.
- **Implementation:**
  - Implement Semi-Naive evaluation tracking $\Delta P_i$ to prevent redundant join computations.
  - Rule: `requires(X, Z) :- requires(X, Y), requires(Y, Z)`.
- **Test Oracle:**
  - Assert fixpoint convergence: $T_P^k(\emptyset) = T_P^{k+1}(\emptyset)$. Assert correct derivation of multi-hop mechanism prerequisites.

#### `EXP-5-2`: Stratified Negation as Failure (NAF) Engine
- **File:** `chapter05/exp_5_2_stratified_naf.py`
- **Pedagogical Purpose:** Implement stratified Datalog evaluation with closed-world negation `NOT`.
- **Implementation:**
  - Construct Predicate Dependency Graph; detect negative cycles; partition rules into strata $P_1, \dots, P_m$.
- **Test Oracle:**
  - Verify non-monotonicity: adding a base fact retractions previously inferred negative conclusions.

#### `EXP-5-3`: SHACL Constraint Validation with pySHACL
- **File:** `chapter05/exp_5_3_shacl_validation.py`
- **Pedagogical Purpose:** Enforce structural closed-world validation on the Mechanism KG.
- **Implementation:**
  - NodeShape for `ex:Mechanism`: requires `ex:hasOperation` (minCount 1), `ex:hasInput` (class `ex:Quantity`).
- **Test Oracle:**
  - Validate conforming graph (`conforms=True`); validate corrupted graph (`conforms=False`) and inspect `ValidationReport`.

#### `EXP-5-4`: The Semantic Boundary: RDFS Entailment vs. SHACL Validation
- **File:** `chapter05/exp_5_4_deduction_vs_validation.py`
- **Pedagogical Purpose:** Execute the canonical counterexample proving RDFS silently infers while SHACL explicitly validates.

---

### Chapter 6: Claims, Evidence, Provenance, Time, Contradiction (4 Labs)

#### `EXP-6-1`: Dempster-Shafer Evidence Combination Engine
- **File:** `chapter06/exp_6_1_dempster_shafer.py`
- **Pedagogical Purpose:** Combine uncertain evidence using Dempster's rule of combination with conflict normalization.
- **Test Oracle:**
  - Assert $\text{Bel}(A) \le P(A) \le \text{Pl}(A)$; assert conflict coefficient $K$ behavior.

#### `EXP-6-2`: Subjective Logic Opinion Vectors & Cumulative Fusion
- **File:** `chapter06/exp_6_2_subjective_logic.py`
- **Pedagogical Purpose:** Implement opinion tuples $\omega = (b, d, u, a)$ and cumulative fusion operator $\oplus$.
- **Test Oracle:**
  - Prove that combining independent observations monotonically decreases uncertainty $u \to 0$.

#### `EXP-6-3`: 2D Bitemporal Graph Ledger
- **File:** `chapter06/exp_6_3_bitemporal_ledger.py`
- **Pedagogical Purpose:** Build a bitemporal store tracking $T_{\text{valid}}$ (Allen intervals) and $T_{\text{transaction}}$ (system recording time).
- **Test Oracle:**
  - Execute "As-Was" vs. "As-Is" queries; prove that updating a past claim supersedes without deleting history.

#### `EXP-6-4`: AGM Belief Revision Postulates Simulation
- **File:** `chapter06/exp_6_4_agm_belief_revision.py`
- **Pedagogical Purpose:** Implement belief contraction ($K - \phi$) and Levi identity revision ($K * \phi$) over claim graphs, asserting the 6 AGM postulates.

---

### Chapter 7: Knowledge Acquisition and Integration (6 Labs)

#### `EXP-7-1`: R2RML Relational-to-RDF Mapping Prototype
- **File:** `chapter07/exp_7_1_r2rml_mapping.py`
- **Pedagogical Purpose:** Transform SQLite mechanism tables into RDF Turtle using declarative R2RML `TriplesMap`.

#### `EXP-7-2`: Fellegi–Sunter Record Linkage Engine
- **File:** `chapter07/exp_7_2_fellegi_sunter.py`
- **Pedagogical Purpose:** Implement two-threshold decision zones ($T_\mu, T_\lambda$) partitioning candidate pairs into Match, Clerical Review, and Non-Match.

#### `EXP-7-3`: Content-Hash Idempotent Ingestion Harness
- **File:** `chapter07/exp_7_3_idempotent_ingestion.py`
- **Pedagogical Purpose:** Guarantee zero duplicate creation on re-ingestion via SHA-256 hashing.

#### `EXP-7-4`: SHACL Ingestion Gate
- **File:** `chapter07/exp_7_4_shacl_ingestion_gate.py`
- **Pedagogical Purpose:** Automated filter gating incoming triples before ledger commit; quarantine malformed records.

#### `EXP-7-5`: Echo Source & Syndicated Content Detector
- **File:** `chapter07/exp_7_5_echo_source_detection.py`
- **Pedagogical Purpose:** Detect near-duplicate source articles using MinHash/Jaccard to discount redundant evidence.

#### `EXP-7-6`: PROV-O Lineage Traversal & Audit Walk
- **File:** `chapter07/exp_7_6_prov_lineage.py`
- **Pedagogical Purpose:** Trace graph entities back through `prov:wasGeneratedBy` and `prov:used` to source text fragments.

---

### Chapter 8: Inductive Knowledge and Learning from Graphs (5 Labs)

#### `EXP-8-1`: Knowledge Graph Embeddings: TransE vs. ComplEx vs. RotatE
- **File:** `chapter08/exp_8_1_kge_benchmark.py`
- **Pedagogical Purpose:** PyTorch implementation comparing translation, bilinear, and rotational embeddings on the Mechanism KG.
- **Test Oracle:** Evaluate MRR and Hits@10; prove RotatE models symmetry, antisymmetry, and inversion in $\mathbb{C}^d$.

#### `EXP-8-2`: Poincaré Hyperbolic Taxonomy Embeddings
- **File:** `chapter08/exp_8_2_poincare_embeddings.py`
- **Pedagogical Purpose:** Embed hierarchical mechanism trees into the Poincaré ball $\mathbb{B}^d$ via Riemannian optimization.
- **Test Oracle:** Demonstrate lower distortion in 2D hyperbolic space compared to high-dimensional Euclidean space.

#### `EXP-8-3`: Weisfeiler-Lehman 1-WL Isomorphism Test & MPNN Ceiling
- **File:** `chapter08/exp_8_3_wl_expressiveness.py`
- **Pedagogical Purpose:** Run 1-WL color refinement on $C_{10}$ vs. $2 \times C_5$; prove that standard message passing GNNs cannot distinguish them.

#### `EXP-8-4`: Inductive GNN Link Prediction (PyG / NetworkX)
- **File:** `chapter08/exp_8_4_inductive_gnn.py`
- **Pedagogical Purpose:** Train an inductive Graph Neural Network predicting links for newly introduced mechanism nodes.

#### `EXP-8-5`: AMIE Horn Clause Rule Mining Engine
- **File:** `chapter08/exp_8_5_rule_mining.py`
- **Pedagogical Purpose:** Discover symbolic Horn rules from graph triples, calculating Head Coverage and PCA confidence.

---

### Chapter 9: Retrieval, Question Answering, and GraphRAG (6 Labs)

#### `EXP-9-1`: RATE_OF_CHANGE Retrieval Benchmark Dataset
- **File:** `chapter09/exp_9_1_retrieval_benchmark.py`
- **Pedagogical Purpose:** 40-question evaluation benchmark with ground-truth entity IDs, multi-hop paths, and temporal scopes.

#### `EXP-9-2`: Comparative Retrieval: BM25 vs. Dense Vector vs. Hybrid RRF
- **File:** `chapter09/exp_9_2_retrieval_comparison.py`
- **Pedagogical Purpose:** Implement BM25, dense vector search, and Reciprocal Rank Fusion; measure P@K, Recall@K, and nDCG.

#### `EXP-9-3`: Personalized PageRank Subgraph Extraction
- **File:** `chapter09/exp_9_3_ppr_extraction.py`
- **Pedagogical Purpose:** Power-iteration contraction mapping extracting seed entity neighborhoods without combinatorial path explosion.

#### `EXP-9-4`: Steiner Tree 2-Approximation for Multi-Entity Assembly
- **File:** `chapter09/exp_9_4_steiner_tree.py`
- **Pedagogical Purpose:** Extract minimum connecting subgraphs uniting multiple query entities for prompt context assembly.

#### `EXP-9-5`: Evidence Packet Assembly & Lost-in-the-Middle Experiment
- **File:** `chapter09/exp_9_5_evidence_packet.py`
- **Pedagogical Purpose:** Package subgraphs, provenance, and temporal bounds into a 3-compartment dossier; measure LLM accuracy degradation under varying evidence positions.

#### `EXP-9-6`: End-to-End GraphRAG vs. Naive Vector RAG Evaluation
- **File:** `chapter09/exp_9_6_graphrag_vs_vector_rag.py`
- **Pedagogical Purpose:** Head-to-head comparison demonstrating how structured subgraph retrieval reduces hallucination on complex multi-hop queries.

---

### Chapter 10: Building a Living Knowledge System (5 Labs)

#### `EXP-10-1`: Multi-Subsystem Freshness & Quality Degradation Detection
- **File:** `chapter10/exp_10_1_staleness_detection.py`
- **Pedagogical Purpose:** Track multi-subsystem freshness metrics (ledger freshness, index freshness, schema freshness) as defined in §10.27; compute sliding-window degradation trends (§10.32) to detect prolonged staleness before QA accuracy collapses.

#### `EXP-10-2`: Contradiction Queue & Escalation Policy Engine
- **File:** `chapter10/exp_10_2_contradiction_escalation.py`
- **Pedagogical Purpose:** Manage the C471/C210 standing contradiction; trigger automated escalation based on evidence deltas.

#### `EXP-10-3`: Closed-Loop Delayed Feedback DDE Stability Simulation
- **File:** `chapter10/exp_10_3_closed_loop_stability.py`
- **Pedagogical Purpose:** Numerical simulation of open-loop transfer function $L(s) = G(s)H(s)e^{-s\tau_{\text{verify}}}$ and time-domain DDE $\dot{x}(t) = -a\,x(t-\tau)$ (§10.20.1); demonstrate belief limit cycles when $a\tau \ge \pi/2$ and evaluate damping via low-pass filtering and hysteresis bands.

#### `EXP-10-4`: Knowledge Entropy $H_K$ & Autophagous Model Collapse Simulator
- **File:** `chapter10/exp_10_4_model_collapse_simulation.py`
- **Pedagogical Purpose:** Simulate recursive self-consuming generation; track variance shrinkage $\sigma_{t+1}^2 = \sigma_t^2(1 - 1/M)$ and tail extinction over 10 generations.

#### `EXP-10-5`: System-Level Audit Trail Replay & 5-Dimension Health Report
- **File:** `chapter10/exp_10_5_audit_replay_health.py`
- **Pedagogical Purpose:** Replay historical audit logs for past QA answers; generate ISO-compliant 5-dimension system health dashboard.
