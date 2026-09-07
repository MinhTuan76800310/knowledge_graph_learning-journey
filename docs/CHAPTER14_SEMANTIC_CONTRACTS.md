# Chapter 14 Semantic Contracts

Authoritative reference for every formal concept in Chapter 14: **Autonomous Agent Long-Term Memory & Conformal Knowledge Ingestion**.

Each record specifies:
- **Source**: authoritative academic or primary reference
- **Formal meaning**: precise definition from the source
- **Book wording**: phrasing used in the manuscript (Vietnamese)
- **Dangerous simplification**: what the wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

---

## 1. Tripartite Cognitive Agent Memory Architecture

- **Source:** AGENT-MEM-01 (Park et al., 2023), BOOK-DEFINED synthesis with PROV-O
- **Formal meaning:** Decomposing autonomous agent memory into three distinct, interoperable graph layers:
  1. *Working Memory:* The active context subgraph instantiated in the prompt context window.
  2. *Episodic Memory:* A temporal directed acyclic graph (DAG) capturing step-by-step agent interactions, tool invocations, environment states, and observations, linked via W3C PROV-O (`prov:wasGeneratedBy`, `prov:used`).
  3. *Semantic Memory:* The consolidated, canonical knowledge graph containing generalized facts, mechanism schemas, and accepted ontological assertions.
- **Book wording:** "Kiến trúc Bộ nhớ Tác tử Ba tầng (Tripartite Agent Memory): phân định rành mạch giữa Bộ nhớ làm việc (Working Memory), Bộ nhớ tình tiết theo vết thời gian (Episodic DAG), và Bộ nhớ ngữ nghĩa vĩnh cửu (Semantic KG)."
- **Dangerous simplification:** Dumping all agent chat transcripts directly into a vector database and calling it "agent long-term memory".
- **MUST NOT infer:**
  - MUST NOT treat episodic memory (what happened in session $t$) as equivalent to semantic memory (what is true about the world).
  - MUST NOT allow episodic memory traces to overwrite canonical semantic knowledge without passing through the Claim Ledger validation pipeline.

---

## 2. Conformal Prediction on Knowledge Graphs

- **Source:** VOVK-01 (Vovk et al., 2005), ANGEL-01 (Angelopoulos & Bates, 2021)
- **Formal meaning:** Let $X = (s, p)$ be a query entity-relation pair and $Y \in \mathcal{E}$ be the true object entity. Given a non-conformity score $s(X, Y)$ (e.g. $1 - P_{\text{model}}(Y \mid X)$) and a calibration set of $n$ exchangeable triples, the conformal prediction set is:
  $$\mathcal{C}(X_{n+1}) = \{y \in \mathcal{E} : s(X_{n+1}, y) \le \hat{q}_{\alpha}\}$$
  where $\hat{q}_{\alpha}$ is the $\lceil (n + 1)(1 - \alpha) \rceil / n$ empirical quantile of calibration scores. This guarantees distribution-free, finite-sample marginal coverage:
  $$\mathbb{P}(Y_{n+1} \in \mathcal{C}(X_{n+1})) \ge 1 - \alpha$$
- **Book wording:** "Dự đoán Tương thích trên Đồ thị Tri thức (Conformal Prediction on KGs): cơ chế hiệu chuẩn thống kê phân phối tự do, cung cấp tập ứng viên có bảo chứng toán học chứa đúng thực thể đích với xác suất tối thiểu $1 - \alpha$."
- **Dangerous simplification:** Equating neural softmax probabilities with conformal confidence bounds. Softmax values are uncalibrated and prone to overconfidence under distribution shift.
- **MUST NOT infer:**
  - MUST NOT claim conformal prediction guarantees conditional coverage for every individual instance $X$; it guarantees *marginal coverage* over the exchangeable data distribution.
  - MUST NOT claim conformal guarantees hold under arbitrary non-exchangeable distribution shifts without covariate shift adjustments.

---

## 3. Risk-Controlled Triple Ingestion Protocol

- **Source:** BOOK-DEFINED protocol building on ANGEL-01 and Ch6/Ch10 Claim Ledger architecture
- **Formal meaning:** An automated gating mechanism where candidate triples from neural extractors or peer agents are accepted into `AcceptedKnowledge` if and only if their conformal prediction set size $|\mathcal{C}(X)| = 1$ (singleton) and the non-conformity score satisfies $s(X, Y) \le \hat{q}_{\alpha_{\text{target}}}$. Ambiguous prediction sets ($|\mathcal{C}(X)| > 1$) or high-nonconformity assertions are routed to `CandidateKnowledge` for human or formal tool arbitration.
- **Book wording:** "Giao thức Tiếp nhận Tri thức Kiểm soát Rủi ro (Risk-Controlled Ingestion): chỉ những bộ ba có tập dự đoán tương thích đơn trị và thỏa mãn ngưỡng sai số quy định mới được chuyển thành Tri thức Được chấp nhận (AcceptedKnowledge)."
- **Dangerous simplification:** Assuming automated gating eliminates the need for human oversight; it bounds the statistical false discovery rate, leaving out-of-distribution edge cases for escalation.
- **MUST NOT infer:**
  - MUST NOT claim risk-controlled ingestion permits 0% error; $\alpha$ is a tunable risk tolerance parameter ($\alpha > 0$).

---

## 4. Multi-Agent Epistemic Consensus

- **Source:** MULTI-AGENT-01 (Wooldridge, 2009), JOSANG-01 (Subjective Logic Consensus Operator)
- **Formal meaning:** A decentralized protocol where autonomous agents $A_1, \dots, A_K$ exchanging candidate subgraphs reach consensus on conflicting claims using Subjective Logic consensus fusion $\oplus$:
  $$\omega_A^{A_1 \oplus \dots \oplus A_K} = \bigoplus_{k=1}^K \omega_A^{A_k}$$
  If dogmatic conflict occurs ($b_1 = 1, b_2 = 1$ on contradictory literals), the protocol triggers an escalation event to the distributed Claim Ledger without corrupting local beliefs.
- **Book wording:** "Đồng thuận Tri thức luận Đa tác tử (Multi-Agent Epistemic Consensus): giao thức phi tập trung đồng bộ hóa tri thức và phân xử xung đột giữa các agent thông qua toán tử hợp nhất Subjective Logic."
- **Dangerous simplification:** Believing multi-agent consensus can be solved by simple majority voting of LLMs (which aggregates hallucinations).
- **MUST NOT infer:**
  - MUST NOT use raw unweighted majority voting when agents have varying epistemic uncertainty $(u > 0)$.
  - MUST NOT treat consensus as a proof of objective truth; shared systematic biases can lead to consensus on falsehoods.
