# Chapter 12 Semantic Contracts

Authoritative reference for every formal concept in Chapter 12: **High-Dimensional Vector-Graph Entity Resolution & Ontology Alignment**.

Each record specifies:
- **Source**: authoritative academic or primary reference
- **Formal meaning**: precise definition from the source
- **Book wording**: phrasing used in the manuscript (Vietnamese)
- **Dangerous simplification**: what the wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

---

## 1. Bi-Encoder Dense Semantic Blocking

- **Source:** DENSE-ER-01 (Mudgal et al., 2018), HNSW-01 (Malkov & Yashunin, 2020)
- **Formal meaning:** Mapping textual/structural entity descriptions $x_i$ into dense vector space $\mathbb{R}^d$ via an encoder $f_\theta(x_i)$. Candidate blocking reduces the quadratic comparison space $O(N^2)$ to sub-linear $O(N \log N)$ by retrieving the top-$k$ nearest neighbors in metric space using an approximate nearest neighbor graph $\mathcal{G}_{\text{HNSW}}$.
- **Book wording:** "Phân khối ngữ nghĩa dày (Dense Semantic Blocking): nhúng hồ sơ thực thể vào không gian vector để thu hẹp không gian so khớp từ bậc hai $O(N^2)$ xuống tập ứng viên có kích thước tuyến tính."
- **Dangerous simplification:** Believing that dense vector similarity alone constitutes entity resolution (re-committing the Vector Fallacy from Chapter 1).
- **MUST NOT infer:**
  - MUST NOT claim that cosine distance between embeddings replaces formal identity assertions (`owl:sameAs`).
  - MUST NOT claim HNSW graph search guarantees 100% recall; it is an approximate algorithm governed by recall-latency trade-offs.

---

## 2. Cross-Encoder & Structural Neighborhood Matching

- **Source:** DENSE-ER-01 (Mudgal et al., 2018), MUGNN-01 (Cao et al., 2019)
- **Formal meaning:** A fine-grained classification stage taking candidate pairs $(e_a, e_b)$ and feeding both concatenated textual tokens and local $k$-hop relational subgraphs into a joint neural scoring model $S(e_a, e_b) \in [0, 1]$. The score captures fine lexical nuances and structural neighborhood isomorphism that bi-encoders discard due to late fusion.
- **Book wording:** "So khớp cấu trúc lân cận bằng Cross-Encoder: mạng nơ-ron đánh giá đồng thời tương đồng ngữ cảnh sâu và tính đẳng cấu đồ thị của vùng lân cận $k$-bước giữa hai thực thể ứng viên."
- **Dangerous simplification:** Thinking cross-encoders can be run over all $N(N-1)/2$ pairs without a prior blocking stage.
- **MUST NOT infer:**
  - MUST NOT claim cross-encoders scale without candidate filtering; cross-encoders are computationally expensive $O(B \cdot L^2)$ per pair.

---

## 3. Probabilistic Calibration: Cosine Similarity to Fellegi-Sunter Likelihoods

- **Source:** BOOK-DEFINED mathematical formulation bridging FS-01 (Fellegi & Sunter, 1969) and dense metric spaces
- **Formal meaning:** Transforming continuous cosine similarities $s = \cos(f(e_a), f(e_b)) \in [-1, 1]$ into calibrated likelihood ratio weights $w(s) = \log \frac{P(s \mid M)}{P(s \mid U)}$, where $M$ is the match distribution and $U$ is the non-match distribution, fitted via isotonic regression or Platt scaling over validation pairs.
- **Book wording:** "Hiệu chuẩn xác suất: Cầu nối Cosine và Trọng số Fellegi–Sunter: ánh xạ độ tương đồng vector liên tục thành tỷ số hợp lý xác suất có thể cộng dồn theo lý thuyết liên kết thực thể cổ điển."
- **Dangerous simplification:** Directly adding cosine similarities together as if they were log-likelihood ratios.
- **MUST NOT infer:**
  - MUST NOT claim raw cosine similarity is linear with respect to match probability.
  - MUST NOT treat uncalibrated vector distances as rigorous evidence weights in the Claim Ledger.

---

## 4. Multi-Channel GNN Ontology Alignment

- **Source:** MUGNN-01 (Cao et al., 2019), GCN-ALIGN-01 (Wang et al., 2018)
- **Formal meaning:** Projecting independent ontologies $O_1 = (V_1, E_1)$ and $O_2 = (V_2, E_2)$ into a shared vector space $\mathbb{R}^d$. Multi-channel GNNs decouple structural topology channels (preserving neighborhood connectivity) from relation-type channels (preserving semantic role identities), reconciled via cross-graph seed anchors and rule-based completion.
- **Book wording:** "Căn chỉnh Bản thể luận bằng Mạng Nơ-ron Đồ thị Đa kênh (Multi-Channel GNN Alignment): chiếu các bản thể luận độc lập vào không gian vector chung mà vẫn bảo toàn các tiên đề phân cấp và kiểu quan hệ."
- **Dangerous simplification:** Assuming GNN alignment automatically preserves logical satisfiability without subsequent DL consistency checking.
- **MUST NOT infer:**
  - MUST NOT claim GNN alignment mappings are logically valid without running an OWL consistency reasoner (e.g. HermiT or Pellet) to verify that no disjointness axioms are violated.
