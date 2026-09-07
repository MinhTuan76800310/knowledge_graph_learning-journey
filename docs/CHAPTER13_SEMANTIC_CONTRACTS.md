# Chapter 13 Semantic Contracts

Authoritative reference for every formal concept in Chapter 13: **Causal Knowledge Graphs & Structural Causal Models (SCMs)**.

Each record specifies:
- **Source**: authoritative academic or primary reference
- **Formal meaning**: precise definition from the source
- **Book wording**: phrasing used in the manuscript (Vietnamese)
- **Dangerous simplification**: what the wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

---

## 1. Pearl's Causal Hierarchy on Graphs

- **Source:** PEARL-01 (Pearl, 2009)
- **Formal meaning:** The 3-level cognitive ladder of causal queries:
  1. *Layer 1 (Association):* $P(y \mid x)$ — "What does observing $x$ tell us about $y$?" Evaluated using standard graph conditional distributions.
  2. *Layer 2 (Intervention):* $P(y \mid do(x))$ — "What will $y$ be if we deliberately take action $x$?" Evaluated via graph mutilation (cutting incoming edges to $x$).
  3. *Layer 3 (Counterfactuals):* $P(y_x \mid x', y')$ — "Given that we observed $x', y'$, what would $y$ have been had $x$ been enacted?" Requires an underlying Structural Causal Model.
- **Book wording:** "Thang bậc Nhân quả Pearl (Pearl's Causal Hierarchy): sự phân biệt nghiêm ngặt giữa Liên kết quan sát ($P(y|x)$), Can thiệp chủ động ($P(y|do(x))$), và Phản thực tế hồi tưởng ($P(y_x|x',y')$)."
- **Dangerous simplification:** Claiming that a standard directed knowledge graph edge $(A \xrightarrow{\text{causes}} B)$ automatically allows computing $P(B \mid do(A))$ without adjusting for confounders.
- **MUST NOT infer:**
  - MUST NOT claim observational correlation implies causal effect ($P(y \mid x) = P(y \mid do(x))$) in the presence of unobserved or observed confounders.
  - MUST NOT claim that higher-level queries (Layer 2 or Layer 3) can be answered purely from Layer 1 observational graph statistics without causal structure assumptions.

---

## 2. Structural Causal Models (SCMs) in Mechanism KGs

- **Source:** PEARL-01 (Pearl, 2009), PETERS-01 (Peters et al., 2017)
- **Formal meaning:** A 4-tuple $\mathcal{M} = \langle U, V, F, P(U) \rangle$ where $U$ is a set of exogenous (unobserved background) variables with prior $P(U)$, $V$ is a set of endogenous variables, and $F = \{f_1, \dots, f_m\}$ is a set of deterministic structural equations $v_i = f_i(\text{PA}_i, u_i)$. In the Mechanism KG, each `Mechanism` node specifies its functional equation $f_i$ connecting inputs $\text{PA}_i$ to output $v_i$.
- **Book wording:** "Mô hình Nhân quả Cấu trúc (Structural Causal Model - SCM): hệ thống phương trình hàm xác định liên kết các biến nội sinh và biến ngoại sinh, biến đồ thị cơ chế thành mô hình thế giới có thể suy luận can thiệp."
- **Dangerous simplification:** Viewing SCMs merely as algebraic equations without directional causal semantics.
- **MUST NOT infer:**
  - MUST NOT treat structural equations $v_i = f_i(\text{PA}_i, u_i)$ as symmetrical mathematical equivalences; the equality is directed (assignment, not symmetric equivalence).
  - MUST NOT omit exogenous noise variables $U$; omitting $U$ eliminates the ability to model counterfactual distributions.

---

## 3. Backdoor Adjustment & Do-Calculus

- **Source:** PEARL-01 (Pearl, 2009)
- **Formal meaning:** Given a causal DAG $\mathcal{G}$, a set of variables $Z$ satisfies the Backdoor Criterion relative to an ordered pair of variables $(X, Y)$ if:
  1. No node in $Z$ is a descendant of $X$.
  2. $Z$ blocks every path between $X$ and $Y$ that contains an arrow into $X$.
  If $Z$ satisfies the backdoor criterion, the interventional distribution is identifiable via the adjustment formula:
  $$P(y \mid do(x)) = \sum_z P(y \mid x, z) P(z)$$
- **Book wording:** "Tiêu chuẩn Cửa sau & Do-Calculus (Backdoor Adjustment): quy tắc tô pô đồ thị cho phép loại bỏ hoàn toàn nhiễu đồng biến (confounder), biến biểu thức can thiệp thành biểu thức xác suất quan sát thuần túy."
- **Dangerous simplification:** Assuming that conditioning on *any* common variable removes confounding (conditioning on a collider opens a spurious path).
- **MUST NOT infer:**
  - MUST NOT condition on a collider node $C$ where $A \to C \leftarrow B$; doing so induces Berkson's bias and invalidates the backdoor criterion.
  - MUST NOT condition on descendants of the treatment variable $X$.

---

## 4. Constraint-Based Causal Discovery (PC / FCI) with Ontological Priors

- **Source:** SPIRTIS-01 (Spirtes et al., 2000), CAUSAL-KG-01 (Schölkopf et al., 2021)
- **Formal meaning:** Algorithms that discover the Markov Equivalence Class (represented as a Completed Partially Directed Acyclic Graph, CPDAG) of the true causal DAG from conditional independence tests $X \perp\!\!\!\perp Y \mid Z$. Ontological background knowledge in the TBox acts as forbidden-edge priors (e.g., forbidding temporal backwards edges or violating domain physical laws), orienting undirected edges into a unique DAG.
- **Book wording:** "Khám phá Nhân quả dựa trên Ràng buộc với Tiên nghiệm Bản thể luận: kết hợp thuật toán kiểm định độc lập điều kiện với tri thức nền TBox để xác định duy nhất cấu trúc DAG nhân quả từ dữ liệu quan sát."
- **Dangerous simplification:** Expecting causal discovery algorithms to return a single directed causal DAG without either background knowledge or non-Gaussian assumptions.
- **MUST NOT infer:**
  - MUST NOT claim that PC/FCI alone without background priors can distinguish between Markov-equivalent DAGs (e.g. $A \to B \to C$ and $A \leftarrow B \leftarrow C$).
  - MUST NOT claim causal discovery succeeds if the Faithfulness or Causal Markov assumptions are violated.
