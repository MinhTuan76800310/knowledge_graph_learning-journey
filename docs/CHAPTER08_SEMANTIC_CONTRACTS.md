# Chapter 8 Semantic Contracts

Authoritative reference for every formal concept in Chapter 8. Each record specifies:

- **Source**: authoritative academic or W3C reference
- **Formal meaning**: precise definition from the source
- **Book wording**: simplified phrasing used in the manuscript
- **Dangerous simplification**: what the book wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

This document is the semantic contract against which `book/chapter08.md` is reviewed.
Concepts marked **BOOK-DEFINED** are the book's own pedagogical framework, not an
academic standard; they are labeled explicitly in the manuscript.

---

## Induction

- **Source:** HOGAN-IND-01 (inductive knowledge generalizes patterns from observations); BOOK-DEFINED for the epistemic framing
- **Formal meaning:** Inductive learning "involves generalising patterns from a given set of input observations", yielding "novel but potentially imprecise predictions" assigned confidence levels. Inductive knowledge is "both the models used to encode patterns, as well as the predictions made by those models" [HOGAN-IND-01]. It is fallible by construction.
- **Book wording:** "Quy nạp (induction) tổng quát hóa từ các ví dụ quan sát được, sinh ra giả thuyết có thể sai — không được suy diễn logic đảm bảo."
- **Dangerous simplification:** Treating induction as "deduction with more data"; treating a well-supported generalization as logically guaranteed.
- **MUST NOT infer:**
  - MUST NOT say many matching examples logically prove a universal rule.
  - MUST NOT say inductive output is a consequence of the graph semantics.
  - MUST NOT equate inductive confidence with entailment.

## Deduction

- **Source:** HOGAN-CH5 (rules/reasoning), HOGAN-IND-01 (deductive knowledge = precise logical consequences); Ch4–5 book model
- **Formal meaning:** Deduction derives consequences licensed by explicit semantics/rules: from a general rule plus instance premises, a consequence follows necessarily (e.g., rule R and facts F entail R(F)). Sound and complete procedures preserve truth.
- **Book wording:** "Suy diễn (deduction): quy tắc chung + tiền đề → hệ quả bắt buộc."
- **Dangerous simplification:** Claiming induction reaches the same certainty as deduction; blurring the two modes.
- **MUST NOT infer:**
  - MUST NOT say a prediction is an entailment.
  - MUST NOT say an induced rule behaves like a Horn rule in the Ch5 materialization sense until it is validated and accepted.
  - MUST NOT present the deduction/induction boundary as a W3C or ISO standard (it is a logic/ML distinction).

## Abduction

- **Source:** BOOK-DEFINED (inference to the best explanation, taught only to prevent terminology confusion; see HOGAN-IND-01 framing of explanation)
- **Formal meaning:** Abduction chooses a hypothesis that would best explain an observation. It differs from induction (generalizing a pattern from instances) and from deduction (deriving consequences). Taught lightly to keep deduction/induction/abduction distinct.
- **Book wording:** "Giả định (abduction): chọn giả thuyết giải thích tốt nhất quan sát — khác quy nạp là khái quát hóa từ ví dụ."
- **Dangerous simplification:** Using abduction and induction interchangeably.
- **MUST NOT infer:**
  - MUST NOT say "best explanation" implies truth.
  - MUST NOT claim abduction is the chapter's core mechanism (the chapter's core is induction).

## Prediction (vs Entailment)

- **Source:** NICKEL-01 (predicting new edges from trained models); HOGAN-IND-01 (predictions are fallible)
- **Formal meaning:** A prediction assigns plausibility/score to a possible unseen structure (e.g., a missing triple). Entailment is a logical relation: a structure follows necessarily from the graph's semantics. They are different kinds of objects.
- **Book wording:** "Dự đoán (prediction) chấm điểm khả năng; suy dẫn (entailment) khẳng định hệ quả logic. Không được nhầm."
- **Dangerous simplification:** Reporting model scores as if they were derived consequences.
- **MUST NOT infer:**
  - MUST NOT say a high-scoring triple is entailed.
  - MUST NOT insert a prediction directly into the canonical knowledge view.
  - MUST NOT present prediction as a superset of entailment.

## Symbolic Knowledge

- **Source:** BOOK-DEFINED (Ch1–5 model); NICKEL-01 observable-pattern framing
- **Formal meaning:** Explicit, inspectable structures: graph triples, ontology axioms, rules, constraints. Their meaning is given by formal semantics (Ch4–5).
- **Book wording:** "Tri thức tượng trưng (symbolic): cấu trúc tường minh — bộ ba, ontology, quy tắc, ràng buộc."
- **Dangerous simplification:** Claiming learned vectors are symbolic statements.
- **MUST NOT infer:**
  - MUST NOT say an embedding is an axiom.
  - MUST NOT say symbolic and statistical objects are interchangeable.

## Statistical Knowledge

- **Source:** NICKEL-01 (latent feature models); HOGAN-IND-01 (numeric representations)
- **Formal meaning:** Knowledge encoded as learned representations, scores, or pattern estimates — numbers produced by a model from data. It is candidate/inductive knowledge, not asserted fact.
- **Book wording:** "Tri thức thống kê (statistical): biểu diễn học được, điểm số, ước lượng — không phải khẳng định."
- **Dangerous simplification:** Treating statistical outputs as accepted knowledge.
- **MUST NOT infer:**
  - MUST NOT insert model predictions directly into the canonical KG.
  - MUST NOT say scores are probabilities of truth without an Assessment object.

## Feature Representation

- **Source:** GRLBOOK-01 (traditional approaches / feature engineering); BOOK-DEFINED
- **Formal meaning:** An explicit, hand-chosen encoding of an object as a vector of attributes (e.g., operation type, arity, role relations). The model sees only the chosen representation; information omitted from features cannot influence learning.
- **Book wording:** "Biểu diễn đặc trưng (feature representation) là một lựa chọn kỹ thuật; mô hình chỉ nhìn thấy phần được chọn."
- **Dangerous simplification:** Assuming features capture everything relevant.
- **MUST NOT infer:**
  - MUST NOT say feature equality implies semantic identity.
  - MUST NOT say a model can recover information not present in its input (connect Ch7 retrieval bound).

## Representation Learning

- **Source:** GRLBOOK-01 (learning vector/latent representations from data); HOGAN-IND-01
- **Formal meaning:** Learning vector/latent representations from data rather than manually defining all features. A learned representation is useful for a task; it is not the entity and not its formal semantics.
- **Book wording:** "Học biểu diễn (representation learning): học vector từ dữ liệu; vector ≠ thực thể, ≠ ngữ nghĩa."
- **Dangerous simplification:** Saying "vector = meaning".
- **MUST NOT infer:**
  - MUST NOT say Entity = Embedding(Entity).
  - MUST NOT say representations replace the ontology.

## Embedding

- **Source:** GRLBOOK-01; HOGAN-IND-01 (embeddings as latent feature models)
- **Formal meaning:** A mapping from graph objects (entities, relations) to low-dimensional vectors such that structural regularities are reflected in geometry. The vectors are trained artifacts, not denotations.
- **Book wording:** "Nhúng (embedding): vector học được phản ánh quy luật cấu trúc; là biểu diễn, không phải thực thể."
- **Dangerous simplification:** Treating the embedding space as a semantic interpretation.
- **MUST NOT infer:**
  - MUST NOT say embedding distance is formal semantics.
  - MUST NOT say an embedding IS the entity (Ch3 identity rules still govern identity).

## Knowledge Graph Embedding (KGE)

- **Source:** HOGAN-IND-01 (embedding as pair of mappings (ε,ρ) + plausibility scoring φ: T×T×T→R); TRANSE-01
- **Formal meaning:** A KGE learns embeddings for entities and relations and a scoring function f(h,r,t) whose value indicates plausibility of triple (h,r,t). Training maximizes scores of observed/plausible triples and minimizes scores of negative/corrupted examples.
- **Book wording:** "Nhúng đồ thị tri thức (KGE): học vector thực thể + quan hệ và hàm chấm điểm; điểm cao = hợp lý hơn, không phải đúng."
- **Dangerous simplification:** Reading scores as truth probabilities.
- **MUST NOT infer:**
  - MUST NOT say higher score ⇒ true triple.
  - MUST NOT say KGE computes entailment.
  - MUST NOT say one embedding model fits every relation type.

## Scoring Function

- **Source:** HOGAN-IND-01 (plausibility scoring function φ : T × T × T → R); TRANSE-01, DISTMULT-01
- **Formal meaning:** A function assigning a real-valued plausibility to a candidate triple; higher/lower (per convention) means more plausible. Its specific geometry encodes the model's inductive bias.
- **Book wording:** "Hàm chấm điểm (scoring function): số hóa mức độ hợp lý của một bộ ba ứng viên."
- **Dangerous simplification:** Treating the score as calibrated probability.
- **MUST NOT infer:**
  - MUST NOT say scores are probabilities (unless explicitly calibrated).
  - MUST NOT say a score is evidence about truth (it is model output, subject to Assessment).

## TransE

- **Source:** TRANSE-01
- **Formal meaning:** Embeddings where a relation acts as a translation: for (h,r,t), h + r ≈ t; score = ||h + r − t|| (L1 or L2). Training uses corrupted triples (replace head or tail) as negatives and a margin-based ranking loss. Evaluation uses mean rank and hits@10 in raw and filtered settings. Known limitation: struggles with 1-to-N, N-to-1, N-to-N, and symmetric relations.
- **Book wording:** "TransE: h + r ≈ t; mỗi quan hệ là một phép tịnh tiến trong không gian vector."
- **Dangerous simplification:** Presenting TransE as SOTA; ignoring its geometry limitations.
- **MUST NOT infer:**
  - MUST NOT say h + r = t semantically.
  - MUST NOT claim TransE handles one-to-many relations gracefully.
  - MUST NOT present it as the canonical foundation (label CURRENT / EXEMPLAR).

## Bilinear Model (DistMult)

- **Source:** DISTMULT-01
- **Formal meaning:** A tensor-decomposition embedding family: score f_r(h,t) = ⟨h, r, t⟩ (elementwise product, equivalently diagonal bilinear form). Relation composition corresponds to matrix multiplication. Symmetric scoring cannot directly model asymmetric relations.
- **Book wording:** "DistMult: chấm điểm song tuyến tính ⟨h, r, t⟩; dễ, nhanh, nhưng đối xứng nên yếu với quan hệ bất đối xứng."
- **Dangerous simplification:** Using DistMult scores for asymmetric relations without caveat.
- **MUST NOT infer:**
  - MUST NOT say symmetric score implies symmetric truth.
  - MUST NOT say bilinear composition is rule inference (it is an analogy, not logic).

## ComplEx

- **Source:** COMPLEX-01
- **Formal meaning:** Complex-valued embeddings scoring with the Hermitian dot product; the conjugate on the tail breaks symmetry, so symmetric and antisymmetric relations can be modeled. Linear space/time.
- **Book wording:** "ComplEx: nhúng phức, chấm điểm qua tích Hermitian; xử lý được quan hệ bất đối xứng tốt hơn DistMult."
- **Dangerous simplification:** Claiming complex numbers carry meaning.
- **MUST NOT infer:**
  - MUST NOT say complex embeddings are semantics.
  - MUST NOT say ComplEx handles all relation patterns.

## Inductive Bias

- **Source:** GRLBOOK-01 (design choices in models); BOOK-DEFINED phrasing
- **Formal meaning:** The set of structural assumptions a model family makes about what patterns matter (e.g., translation, bilinearity, relation-specific transforms). Different scoring families encode different inductive biases.
- **Book wording:** "Thiên kiến quy nạp (inductive bias): các giả định cấu trúc của họ mô hình về mẫu nào đáng học."
- **Dangerous simplification:** Claiming any single bias is universally correct.
- **MUST NOT infer:**
  - MUST NOT say a model with a good bias understands semantics.
  - MUST NOT say similarMechanism, instanceOf, supports, contradicts share one optimal geometry.

## Negative Sampling

- **Source:** NEGSAMP-01 (origin of negative sampling in representation learning); TRANSE-01 (corrupted triples in KGE); BOOK-DEFINED for the OWA discussion
- **Formal meaning:** A training procedure that constructs assumed-negative examples (by random corruption or heuristic drawing) so the model learns to rank positives above negatives. It is an ML assumption, not a statement of falsity.
- **Book wording:** "Lấy mẫu âm (negative sampling): tạo ví dụ 'giả định sai' để huấn luyện; không phải khẳng định bộ ba đó sai."
- **Dangerous simplification:** Treating sampled negatives as known false triples.
- **MUST NOT infer:**
  - MUST NOT say a missing triple is false (OWA).
  - MUST NOT say negative sampling converts OWA into closed-world assumption.
  - MUST NOT say sampled negatives are counterexamples in the Ch6/Ch11 sense.

## False Negative (in KGE training)

- **Source:** TRANSE-01, NEGSAMP-01 (corruption may hit a true but unobserved triple); BOOK-DEFINED
- **Formal meaning:** A triple used as a training negative that is actually true but absent from the training graph. Because KGs are incomplete, corrupted negatives can be false negatives, teaching the wrong boundary.
- **Book wording:** "Âm tính giả (false negative): bộ ba thật bị dùng làm mẫu âm vì đồ thị chưa đầy đủ — làm lệch ranh giới học."
- **Dangerous simplification:** Assuming all negatives are truly false.
- **MUST NOT infer:**
  - MUST NOT say the training set proves a triple false.
  - MUST NOT blame only negative sampling for wrong boundaries (it is one source).

## Link Prediction

- **Source:** NICKEL-01 (predicting new edges); HOGAN-IND-01 (completing edges with missing components); BOOK-DEFINED pipeline to CandidateKnowledge
- **Formal meaning:** Given a partially observed KG, rank plausible completions (missing tail/head/relation) using a model. Output is an ordered list of candidate triples, not asserted facts.
- **Book wording:** "Dự đoán liên kết (link prediction): xếp hạng bộ ba ứng viên còn thiếu; hạng cao ≠ sự thật."
- **Dangerous simplification:** Treating the top-ranked candidate as true.
- **MUST NOT infer:**
  - MUST NOT say a ranked candidate is an accepted fact.
  - MUST NOT bypass the CandidateClaim → evidence → validation → governance pipeline.

## Mean Reciprocal Rank (MRR)

- **Source:** NICKEL-01 (evaluation practices in KG literature); BOOK-DEFINED exposition
- **Formal meaning:** For a set of queries, MRR = mean over queries of 1/rank of the correct answer; 1.0 if always first. Measures where the correct answer typically lands, but says nothing about its absolute plausibility.
- **Book wording:** "MRR = trung bình 1/hạng của câu trả lời đúng; gần 1 là thường đứng đầu."
- **Dangerous simplification:** Reading MRR as knowledge-system quality.
- **MUST NOT infer:**
  - MUST NOT say high MRR ⇒ model's top predictions are true.
  - MUST NOT compare MRR across different datasets/corruptions without context.

## Hits@K

- **Source:** TRANSE-01 (hits@10 used in evaluation); NICKEL-01
- **Formal meaning:** Fraction of queries where the correct answer appears within the top-K ranked candidates. Captures "does the answer surface early enough", independent of exact position beyond K.
- **Book wording:** "Hits@K: tỉ lệ câu đúng nằm trong top K."
- **Dangerous simplification:** Picking K to make results look good; ignoring rank quality inside K.
- **MUST NOT infer:**
  - MUST NOT say Hits@10 success means the model's other top-10 are true.
  - MUST NOT say evaluation without filtering reflects real ranking.

## Filtered Evaluation

- **Source:** TRANSE-01 (raw vs filtered settings); NICKEL-01
- **Formal meaning:** Before ranking the target, remove other known positive triples from the candidate list so that an alternate true fact is not counted as a wrong answer. Note: known positives ≠ all true facts because KGs are incomplete.
- **Book wording:** "Đánh giá đã lọc (filtered evaluation): loại các bộ ba đúng đã biết khỏi danh sách trước khi xếp hạng."
- **Dangerous simplification:** Believing filtered evaluation equals truth evaluation.
- **MUST NOT infer:**
  - MUST NOT say filtered results measure truth.
  - MUST NOT say the KG's known positives are the complete set of true facts.

## Train / Validation / Test Split

- **Source:** NICKEL-01 (data split protocols in KG learning); BOOK-DEFINED for Mechanism System
- **Formal meaning:** Partitioning triples (or entities/sources) into training, validation, and test sets so model selection and evaluation use held-out data. Graph splits are tricky: edge/entity/temporal/source overlap can leak signal.
- **Book wording:** "Chia train/validation/test: dữ liệu thử phải tách khỏi huấn luyện; chia trên đồ thị dễ bị rò rỉ."
- **Dangerous simplification:** Assuming random split always measures generalization.
- **MUST NOT infer:**
  - MUST NOT say a random split prevents leakage.
  - MUST NOT say test performance transfers across domains.

## Data Leakage

- **Source:** BOOK-DEFINED synthesis (NICKEL-01 evaluation framing; SHORTCUT-01 related cue-exploitation); Ch6 temporal/claim concepts
- **Formal meaning:** Information from the test distribution reaching the model through training data, inflating measured performance. Types: duplicate leakage, inverse-relation leakage, path leakage, entity leakage, temporal leakage, source leakage, claim duplication across sources.
- **Book wording:** "Rò rỉ dữ liệu (data leakage): thông tin từ tập kiểm lọt vào huấn luyện làm điểm số ảo."
- **Dangerous simplification:** Claiming a leak-free model is a truthful model.
- **MUST NOT infer:**
  - MUST NOT say eliminating leakage proves truth (only that evaluation is cleaner).
  - MUST NOT say same-book passages across splits are independent.

## Temporal Leakage

- **Source:** BOOK-DEFINED; connects Ch6 temporal dimensions (valid/assertion time)
- **Formal meaning:** Random splits can put future claims in training while testing on past claims; for future-prediction tasks, split by time so training precedes test temporally. Not universally superior — depends on the task.
- **Book wording:** "Rò rỉ thời gian (temporal leakage): chia ngẫu nhiên có thể để thông tin tương lai vào huấn luyện."
- **Dangerous simplification:** Claiming temporal splits are always best.
- **MUST NOT infer:**
  - MUST NOT say temporal ordering alone fixes all leakage.
  - MUST NOT say 2026 training data is appropriate for 2024 predictions.

## Source Leakage

- **Source:** BOOK-DEFINED; connects Ch7 echo-source discipline
- **Formal meaning:** Passages from the SAME source appearing in both train and test overestimate cross-source generalization. Mitigation: hold out entire sources/domains.
- **Book wording:** "Rò rỉ nguồn (source leakage): cùng một nguồn ở cả train lẫn test làm quá lạc quan về tổng quát hóa."
- **Dangerous simplification:** Treating duplicate passages from one book as independent evidence (Ch7 echo lesson).
- **MUST NOT infer:**
  - MUST NOT say a model trained on one book generalizes to other books.
  - MUST NOT say source diversity in train implies test independence.

## Transductive Learning

- **Source:** GRAIL-01 (transductive vs inductive settings); BOOK-DEFINED
- **Formal meaning:** In the transductive KG setting, entities are (mostly) known during training; the task is predicting missing links among known entities. Standard entity-ID embeddings operate here.
- **Book wording:** "Học chuyển dẫn (transductive): thực thể đã biết khi huấn luyện; dự đoán liên kết thiếu giữa thực thể quen."
- **Dangerous simplification:** Calling all KGE "inductive".
- **MUST NOT infer:**
  - MUST NOT say transductive performance extends to new entities.
  - MUST NOT say transductive models generalize to new books/domains.

## Inductive Learning (KG sense)

- **Source:** GRAIL-01 (generalizing to unseen entities/subgraphs)
- **Formal meaning:** In KG learning, the inductive setting requires the model to generalize to entities/subgraphs never observed in training — e.g., new mechanism applications, new quantities, new domains from new books.
- **Book wording:** "Học quy nạp trên đồ thị (inductive KG learning): tổng quát hóa tới thực thể mới chưa từng thấy khi huấn luyện."
- **Dangerous simplification:** Claiming every embedding model is inductive.
- **MUST NOT infer:**
  - MUST NOT say entity-ID embeddings handle unseen entities.
  - MUST NOT say the Mechanism System's need for new-entity generalization is satisfied by transductive models alone.

## Out-of-Vocabulary Entity

- **Source:** GRAIL-01 (new entities without trained embeddings); BOOK-DEFINED
- **Formal meaning:** An entity with no trained embedding because it was unseen at training time. Approaches: derive representation from attributes/text, neighborhood, or an inductive encoder (e.g., subgraph GNN).
- **Book wording:** "Thực thể ngoài từ vựng (out-of-vocabulary entity): chưa có vector học sẵn; cần biểu diễn từ lân cận/thuộc tính."
- **Dangerous simplification:** Assuming every new entity gets an embedding for free.
- **MUST NOT infer:**
  - MUST NOT say lookup-table embeddings cover new entities.
  - MUST NOT say neighborhood-derived representations are identities.

## Message Passing

- **Source:** GRLBOOK-01 (generic GNN update); RGCN-01
- **Formal meaning:** Node representation at layer k+1 is computed from its current representation plus aggregated messages from neighbors: m_v = AGGREGATE({MESSAGE(h_u, h_v, edge)}); h_v' = UPDATE(h_v, m_v). A generic conceptual framework, not one algorithm.
- **Book wording:** "Truyền thông điệp (message passing): thông điệp từ lân cận được gom rồi cập nhật biểu diễn nút."
- **Dangerous simplification:** Pretending one formula defines every GNN.
- **MUST NOT infer:**
  - MUST NOT say message passing computes semantics.
  - MUST NOT say aggregation preserves relation distinctions automatically.

## Graph Neural Network (GNN)

- **Source:** GRLBOOK-01; HOGAN-IND-01 (numeric supervised models on graphs)
- **Formal meaning:** Neural models whose computation follows the graph structure via message passing; node representations depend on their neighborhoods (multi-hop). Used for node classification, link prediction, graph classification.
- **Book wording:** "Mạng nơ-ron đồ thị (GNN): mô hình tính theo cấu trúc đồ thị, mỗi nút học từ lân cận của nó."
- **Dangerous simplification:** Claiming GNNs understand graphs like humans do.
- **MUST NOT infer:**
  - MUST NOT say GNN output is an interpretation.
  - MUST NOT say deeper GNNs are always better (oversmoothing).

## Relational Graph Convolutional Network (R-GCN)

- **Source:** RGCN-01
- **Formal meaning:** A GNN designed for multi-relational data: each relation type gets its own transformation during aggregation so different relations (e.g., differentiand vs withRespectTo) are not treated identically; used as encoder with a decoder (e.g., DistMult) for link prediction.
- **Book wording:** "R-GCN: truyền thông điệp có biến đổi riêng theo từng loại quan hệ."
- **Dangerous simplification:** Collapsing all relation types into one aggregation.
- **MUST NOT infer:**
  - MUST NOT say relation-blind aggregation is fine for KGs.
  - MUST NOT say R-GCN output is formal semantics.

## Node Representation vs Subgraph Representation

- **Source:** GRLBOOK-01 (pooling/readout for graph-level vectors)
- **Formal meaning:** A node embedding represents one node; a subgraph/graph representation summarizes a set of nodes (via pooling/readout or dedicated encoders). Comparing mechanism applications requires subgraph-level representations; node embedding ≠ subgraph embedding.
- **Book wording:** "Biểu diễn nút khác biểu diễn đồ thị con; so sánh hai ứng dụng cơ chế cần biểu diễn toàn cục."
- **Dangerous simplification:** Comparing applications by pooling arbitrary nodes without design.
- **MUST NOT infer:**
  - MUST NOT say a pooled vector is the subgraph's meaning.
  - MUST NOT say node similarity equals application similarity.

## Structural Similarity

- **Source:** BOOK-DEFINED (multi-dimensional similarity evidence; connects Ch3 identity, Ch7 structural similarity as hint)
- **Formal meaning:** A multi-dimensional assessment that two structures share role/operation/neighborhood patterns (same operation, same role pattern, compatible argument types, same functional shape, similar neighborhood). Similarity is evidence, never identity.
- **Book wording:** "Tương tự cấu trúc (structural similarity): bằng chứng đa chiều; tương tự ≠ đồng nhất, ≠ owl:sameAs."
- **Dangerous simplification:** Reducing similarity to one cosine score.
- **MUST NOT infer:**
  - MUST NOT say similar structures are the same entity (Ch3).
  - MUST NOT say similarity implies same mechanism (identity is a governance decision).

## Cosine Similarity

- **Source:** BOOK-DEFINED (standard linear algebra; taught with worked example)
- **Formal meaning:** cos(a,b) = (a·b)/(||a||·||b||), in [−1,1]: 1 for same direction, 0 orthogonal, −1 opposite. Measures directional agreement of vectors.
- **Book wording:** "Độ tương tự cosine: cosin góc giữa hai vector."
- **Dangerous simplification:** Reading high cosine as semantic equivalence.
- **MUST NOT infer:**
  - MUST NOT say high cosine ⇒ owl:sameAs (Ch3).
  - MUST NOT say cosine similarity is semantic similarity.

## Mechanism Hypothesis / CandidateMechanismHypothesis

- **Source:** BOOK-DEFINED; continues Ch7 §7.36 hook; grounded in HOGAN-IND-01 (patterns as candidates)
- **Formal meaning:** A candidate claim that several applications may instantiate a common abstract mechanism (or family). It carries learned evidence, structural support, source evidence, uncertainty, competing hypotheses, and provenance. It enters the Claim Ledger as CandidateKnowledge until governed.
- **Book wording:** "Giả thuyết cơ chế ứng viên (CandidateMechanismHypothesis): 'các ứng dụng này có thể cùng một cơ chế' — là ứng viên, không phải khẳng định."
- **Dangerous simplification:** Jumping from similar embeddings to "same mechanism".
- **MUST NOT infer:**
  - MUST NOT say a pattern is a mechanism (pattern → candidate only).
  - MUST NOT insert the hypothesis directly into canonical knowledge.

## Invariant Structure

- **Source:** BOOK-DEFINED (what a hypothesis proposes to retain across examples)
- **Formal meaning:** The structure a hypothesis treats as invariant across applications (e.g., derivative operation + differentiand + reference variable + result-is-a-rate) versus incidental components (Position, Charge, domain labels). Proposing invariant vs incidental is the learning task; representation choice shapes what can be learned.
- **Book wording:** "Cấu trúc bất biến (invariant structure): phần được giữ khi trừu tượng hóa; phần ngẫu nhiên (incidental) là chi tiết miền."
- **Dangerous simplification:** Claiming the invariant is discovered solely by similarity.
- **MUST NOT infer:**
  - MUST NOT say an invariant is guaranteed correct (it is a hypothesis).
  - MUST NOT say the abstraction falls out of replacing names with X.

## Rule Induction

- **Source:** AMIE-01 (path rules); BOOK-DEFINED candidate status
- **Formal meaning:** Learning candidate symbolic rules from examples, e.g., IF application hasOperation DerivativeOperation AND hasDifferentiand some Quantity AND withRespectTo some ReferenceVariable THEN candidate instanceOf RateOfChangeApplication. A learned rule is a hypothesis, not a logical law; it must be evaluated.
- **Book wording:** "Học quy tắc (rule induction): sinh quy tắc ứng viên từ ví dụ; quy tắc học được ≠ định luật logic."
- **Dangerous simplification:** Inserting learned rules into the rule engine directly.
- **MUST NOT infer:**
  - MUST NOT say a learned rule is valid logic (Ch5 sense).
  - MUST NOT say a high-support rule is universal truth.

## Rule Mining Support

- **Source:** AMIE-01 (support counts instantiations)
- **Formal meaning:** Support of a rule = number of instantiations of body+head in the graph (AMIE defines it over observed facts). It is a frequency measure over the dataset.
- **Book wording:** "Độ hỗ trợ (support): số lần mẫu quy tắc xuất hiện trong đồ thị."
- **Dangerous simplification:** Reading support as importance or truth.
- **MUST NOT infer:**
  - MUST NOT say high support ⇒ rule is true.
  - MUST NOT say support is evidence strength in the Ch6 sense.

## Rule Mining Confidence (PCA)

- **Source:** AMIE-01 (PCA confidence under Partial Completeness Assumption)
- **Formal meaning:** In AMIE+, confidence is computed under the Partial Completeness Assumption: if an entity has one value for the head relation, the KB is assumed complete for that pair; confidence then counts known counterexamples only. A frequency-style, dataset-relative measure.
- **Book wording:** "Độ tin cậy khai phá quy tắc (rule-mining confidence): tần suất dưới giả định PCA — khác độ tin cậy tri thức luận Chương 6."
- **Dangerous simplification:** Silently reusing "confidence" for both meanings.
- **MUST NOT infer:**
  - MUST NOT say rule-mining confidence equals Ch6 epistemic confidence.
  - MUST NOT say a PCA-confidence rule holds outside the dataset assumption.
  - MUST NOT label it ClaimAssessment without an explicit mapping.

## Hybrid / Neuro-symbolic Architecture (book engineering)

- **Source:** BOOK-DEFINED architecture; informed by NICKEL-01 (combining latent and observable models)
- **Formal meaning:** A pragmatic pipeline: statistical model generates/ranks candidate relations → symbolic layer checks ontology/type/SHACL constraints → epistemic layer attaches evidence/provenance → governance decides acceptance. Labeled "book engineering architecture", not a formal neuro-symbolic AI definition.
- **Book wording:** "Kiến trúc lai (hybrid pipeline, book-defined): ML sinh ứng viên, tầng tượng trưng lọc, tầng tri thức luận gắn bằng chứng, quản trị quyết định."
- **Dangerous simplification:** Calling any neural+RDF diagram "neuro-symbolic" without a literature definition.
- **MUST NOT infer:**
  - MUST NOT say constraints prove a remaining candidate true.
  - MUST NOT say the pipeline is a standard.

## Calibration

- **Source:** CALIB-01
- **Formal meaning:** Calibrated confidence means predicted probabilities match observed correctness rates (ECE measures the gap). Modern neural nets are often overconfident; temperature scaling improves calibration without changing accuracy.
- **Book wording:** "Hiệu chuẩn (calibration): điểm số khớp với tần suất đúng thực tế; mạng hiện đại thường tự tin quá mức."
- **Dangerous simplification:** Reading softmax as truth probability.
- **MUST NOT infer:**
  - MUST NOT say a calibrated model is correct.
  - MUST NOT use an ML score as Ch6 confidence without an Assessment object.

## Model Assessment

- **Source:** Ch6 Assessment structure (BOOK-DEFINED); CALIB-01 (score semantics)
- **Formal meaning:** An object that records what a model scored: target, model id/version, task, score, score semantics (logit/ranking/softmax/calibrated), assessed-at time, training dataset, evaluation context. Prevents anonymous numbers.
- **Book wording:** "Đánh giá mô hình (ModelAssessment): bọc mọi điểm số với ngữ nghĩa, phiên bản mô hình, dữ liệu huấn luyện, bối cảnh đánh giá."
- **Dangerous simplification:** Attaching a bare number to a claim.
- **MUST NOT infer:**
  - MUST NOT say a ModelAssessment is evidence of truth.
  - MUST NOT say score semantics are obvious from the number.

## Training Provenance

- **Source:** PROV-O/PROV-DM (Activity); BOOK-DEFINED (Ch6 provenance applied to models)
- **Formal meaning:** A learned hypothesis is wasGeneratedBy a TrainingOrInferenceActivity that records: training dataset version, model version, feature schema, hyperparameters/config where useful, input graph snapshot. Model artifacts are not magical.
- **Book wording:** "Provenance huấn luyện: hoạt động sinh ra dự đoán ghi phiên bản dữ liệu, mô hình, lược đồ đặc trưng."
- **Dangerous simplification:** Omitting model provenance in claims.
- **MUST NOT infer:**
  - MUST NOT say training provenance is evidence for prediction truth.
  - MUST NOT say "trained on supporting examples" is direct evidence for the claim.

## Training Data as Evidence?

- **Source:** BOOK-DEFINED; Ch6 evidence semantics
- **Formal meaning:** Training data influences model output (provenance), but "the model was trained on examples supporting P" is not direct evidence that P is true. Provenance ≠ evidence.
- **Book wording:** "Dữ liệu huấn luyện là provenance, không phải bằng chứng trực tiếp."
- **Dangerous simplification:** Citing a model's training set as evidence for a claim.
- **MUST NOT infer:**
  - MUST NOT say training-data lineage strengthens a claim's evidence.
  - MUST NOT say a prediction is independent of its training data.

## Cross-Domain Generalization

- **Source:** SHORTCUT-01 (robustness/transfer framing); BOOK-DEFINED test design (train mechanics+EM, test economics)
- **Formal meaning:** Whether a model recognizes the mechanism in a new domain despite different surface vocabulary. Distinguished from in-domain interpolation: cross-domain transfer requires the learned pattern to be the structural mechanism, not domain cues.
- **Book wording:** "Tổng quát hóa chéo miền: nhận cơ chế ở miền mới dù từ vựng khác."
- **Dangerous simplification:** Claiming in-domain accuracy implies cross-domain understanding.
- **MUST NOT infer:**
  - MUST NOT say high IID accuracy ⇒ mechanism understanding.
  - MUST NOT say domain-shared vocabulary proves mechanism learning.

## Spurious Correlation

- **Source:** SHORTCUT-01 (shortcut cues); BOOK-DEFINED mechanism example
- **Formal meaning:** A correlation in the training data between a superficial cue and the label that the model exploits instead of the intended feature (e.g., physics vocabulary "d/dt" → RateOfChange). Works on IID data, breaks on out-of-domain data.
- **Book wording:** "Tương quan giả (spurious correlation): mô hình học dấu hiệu bề ngoài thay vì cơ chế."
- **Dangerous simplification:** Treating validation accuracy as mechanism understanding.
- **MUST NOT infer:**
  - MUST NOT say a model that scores well learned the mechanism.
  - MUST NOT say removing one cue fixes all shortcuts.

## Hard Negative

- **Source:** BOOK-DEFINED (decision boundaries among nearby mechanisms)
- **Formal meaning:** A negative example close to the positive class that forces the model to learn a meaningful boundary (e.g., finite difference vs instantaneous derivative) rather than a trivial one (RateOfChange vs ColorClassification). Easy negatives are not informative.
- **Book wording:** "Âm tính khó (hard negative): ví dụ sai gần ranh giới, buộc mô hình học biên đúng."
- **Dangerous simplification:** Using only easy negatives and claiming discrimination.
- **MUST NOT infer:**
  - MUST NOT say easy-negative performance implies boundary quality.
  - MUST NOT say a hard negative is a counterexample in the logical sense.

## Clustering (exploratory)

- **Source:** BOOK-DEFINED (exploratory grouping; connects Ch1–2 graph structures)
- **Formal meaning:** Grouping applications by features/embeddings without labels. Cluster membership is not ontology class membership; clusters suggest hypotheses, then semantic/evidence evaluation follows.
- **Book wording:** "Phân cụm (clustering): gom nhóm khám phá; cụm ≠ lớp ontology."
- **Dangerous simplification:** Using clusters as automatic class assertions.
- **MUST NOT infer:**
  - MUST NOT say cluster membership = ontology membership.
  - MUST NOT say a clustering visualization is proof.

## Classification (candidate)

- **Source:** BOOK-DEFINED (supervised labeling; Ch6 governance applied)
- **Formal meaning:** A classifier trained on labeled applications outputs candidate class scores for a new application (e.g., PopulationGrowthApplication). Output is a candidate claim, not a canonical type assertion.
- **Book wording:** "Phân lớp (classification): đầu ra là xác suất ứng viên; không phải khẳng định kiểu."
- **Dangerous simplification:** Writing the predicted class directly into the graph.
- **MUST NOT infer:**
  - MUST NOT say a predicted class is a true type.
  - MUST NOT bypass CandidateClaim processing.

## Self-Reinforcing Feedback / Model Contamination

- **Source:** COLLAPSE-01 (model collapse under recycled data); BOOK-DEFINED epistemic rule
- **Formal meaning:** If model predictions re-enter training data without provenance control, the model increasingly sees its own outputs; confidence grows without independent evidence. Must distinguish human/source-derived knowledge from model-generated candidate knowledge.
- **Book wording:** "Vòng phản hồi tự củng cố: dự đoán của mô hình quay lại làm dữ liệu huấn luyện → tự tin giả tạo."
- **Dangerous simplification:** Treating model-generated claims as independent evidence.
- **MUST NOT infer:**
  - MUST NOT say retraining on predictions validates them.
  - MUST NOT say recycled claims strengthen a claim's evidence.

## CandidateAxiom

- **Source:** BOOK-DEFINED (Ch5 axioms vs assertions; Ch6 governance)
- **Formal meaning:** A model-proposed axiom (e.g., RateOfChangeMechanism ⊑ ChangeMechanism) kept as a candidate until semantic review, consistency/satisfiability check, evidence/governance, and possible ontology update. Axioms change global inference, so blast radius matters.
- **Book wording:** "Tiên đề ứng viên (CandidateAxiom): đề xuất của mô hình, chưa được đưa vào ontology."
- **Dangerous simplification:** Inserting learned axioms automatically.
- **MUST NOT infer:**
  - MUST NOT say a learned axiom is safe to adopt.
  - MUST NOT say an axiom's acceptance has no global effect (blast radius).

## Ontology Evolution

- **Source:** BOOK-DEFINED; connects Ch10 Living Knowledge System
- **Formal meaning:** Induction may reveal the ontology is too coarse (e.g., RateOfChangeMechanism needs subclasses: Instantaneous/Average/Spatial/Temporal). Treated as candidate ontology evolution with review, never as automatic reclassification.
- **Book wording:** "Tiến hóa ontology (candidate): thêm/tinh chỉnh lớp do bằng chứng quy nạp; là quyết định quản trị."
- **Dangerous simplification:** Splitting classes on one counterexample without review.
- **MUST NOT infer:**
  - MUST NOT say a refined taxonomy is final.
  - MUST NOT say evolution is done without governance.

## Uncertainty Sources (plural)

- **Source:** BOOK-DEFINED; Ch6 confidence multi-dimensionality
- **Formal meaning:** Uncertainty may come from extraction, identity, schema mapping, model, evidence, or time. They are separate dimensions; do not collapse into one "confidence" number.
- **Book wording:** "Nhiều nguồn bất định: trích xuất, định danh, lược đồ, mô hình, bằng chứng, thời gian."
- **Dangerous simplification:** Merging all uncertainty into a single score.
- **MUST NOT infer:**
  - MUST NOT say a mechanism hypothesis is uncertain for one reason only.
  - MUST NOT say model uncertainty covers evidence uncertainty.

## Model Error vs Knowledge Conflict

- **Source:** Ch6 contradiction/governance model (BOOK-DEFINED); applied to model vs accepted knowledge
- **Formal meaning:** If a model predicts X and an AcceptedClaim says not-X, do not overwrite: it may be model error, existing-knowledge error, multi-label, scope difference, or ontology version difference. Create a CandidateClaim + conflict workflow (Ch6).
- **Book wording:** "Lỗi mô hình ≠ mâu thuẫn tri thức: tạo ứng viên + quy trình xung đột, không ghi đè."
- **Dangerous simplification:** Overwriting accepted knowledge with a model score.
- **MUST NOT infer:**
  - MUST NOT say a higher score wins over governance.
  - MUST NOT say the model must be right and the ledger wrong.

## Active Learning (supporting)

- **Source:** BOOK-DEFINED (uncertainty-guided labeling; sourced conceptually)
- **Formal meaning:** The model selects informative/uncertain examples for human labeling (e.g., applications near the RateOfChange/FiniteDifference boundary). Reduces labeling effort; does not guarantee optimal labels.
- **Book wording:** "Học tích cực (active learning): chọn mẫu bất định nhờ con người gán nhãn."
- **Dangerous simplification:** Claiming active learning guarantees better labels.
- **MUST NOT infer:**
  - MUST NOT say model-selected examples are more important truth-wise.
  - MUST NOT say active learning replaces governance.

## Human Feedback as Data

- **Source:** BOOK-DEFINED (Ch6 Assessment; Ch7 Review Queue)
- **Formal meaning:** Human review creates labeled assessments with provenance and rationale; future models may train on them. Track reviewer independence to avoid silent circularity (model predicts → human rubber-stamps → retrain).
- **Book wording:** "Phản hồi con người là dữ liệu có provenance; tránh vòng luẩn quẩn thẩm định."
- **Dangerous simplification:** Using rubber-stamped predictions as fresh validation.
- **MUST NOT infer:**
  - MUST NOT say human-accepted model output is independent evidence.
  - MUST NOT say retraining on labels validates the labeler.

## Pattern ≠ Mechanism

- **Source:** BOOK-DEFINED (Mechanism definition from Ch1/4: stable explanatory/operational meaning)
- **Formal meaning:** A repeated graph pattern (e.g., A→B→C) may recur accidentally; a Mechanism requires a stable explanatory/operational meaning. Pattern discovery produces Mechanism candidates, never Mechanisms directly.
- **Book wording:** "Mẫu lặp ≠ cơ chế; mẫu chỉ sinh giả thuyết cơ chế."
- **Dangerous simplification:** Promoting patterns to mechanisms on frequency alone.
- **MUST NOT infer:**
  - MUST NOT say pattern discovery = mechanism discovery.
  - MUST NOT say similarity proves mechanism identity.

## Operation + Meaning

- **Source:** BOOK-DEFINED (Mechanism = operation + meaning); HOGAN-IND-01 (meaning hard from structure alone)
- **Formal meaning:** Which parts can be learned from structural repetition: operation pattern (possibly), role structure (possibly). Semantic "meaning" (instantaneous vs average) is much harder; it may require textual definitions, ontology semantics, evidence, expert interpretation, cross-source agreement. Embeddings do not discover meaning automatically.
- **Book wording:** "Cấu trúc học được hình dạng thao tác; ý nghĩa cần văn bản, ontology, bằng chứng, chuyên gia."
- **Dangerous simplification:** Claiming embeddings discover meaning.
- **MUST NOT infer:**
  - MUST NOT say topology alone yields semantics.
  - MUST NOT say similar topology implies same meaning.

## Structure + Text

- **Source:** BOOK-DEFINED (complementary evidence); GRLBOOK-01 (representations from text/attributes)
- **Formal meaning:** Graph structure plus textual definitions can provide richer candidate representations; e.g., FiniteDifference and Derivative may share topology, but text distinguishes "average" vs "instantaneous". Language similarity may dominate structural differences (similarity ≠ identity).
- **Book wording:** "Cấu trúc + văn bản bổ sung bằng chứng; từ ngữ giống nhau không phải cấu trúc giống nhau."
- **Dangerous simplification:** Relying on text similarity alone.
- **MUST NOT infer:**
  - MUST NOT say "rate of change" phrase co-occurrence proves same mechanism.
  - MUST NOT say text embeddings capture formal structure.

## What Learning Cannot Guarantee

- **Source:** BOOK-DEFINED synthesis (HOGAN-IND-01 fallibility; SHORTCUT-01; CALIB-01)
- **Formal meaning:** Learning cannot guarantee truth, causal mechanism, ontology correctness, entity identity, universal validity, evidence independence, absence of bias, or cross-domain generalization unless additional assumptions/evidence hold.
- **Book wording:** "Học máy không đảm bảo: chân lý, cơ chế nhân quả, tính đúng ontology, định danh, phổ quát, độc lập bằng chứng."
- **Dangerous simplification:** Treating model confidence as these guarantees.
- **MUST NOT infer:**
  - MUST NOT say a learned model is exempt from governance.
  - MUST NOT say "no counterexample seen" ⇒ universally valid.
