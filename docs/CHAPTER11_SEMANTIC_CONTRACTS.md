# Chapter 11 Semantic Contracts

Authoritative reference for every formal concept in Chapter 11: **Neuro-Symbolic Information Extraction & Grammar-Constrained Decoding**.

Each record specifies:
- **Source**: authoritative academic or primary reference
- **Formal meaning**: precise definition from the source
- **Book wording**: phrasing used in the manuscript (Vietnamese)
- **Dangerous simplification**: what the wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

---

## 1. Grammar-Constrained Decoding via Pushdown Automata

- **Source:** OUTLINES-01 (Willard & Louf, 2023), SYNTAX-01 (Scholak et al., 2021)
- **Formal meaning:** Autoregressive language generation computes token probabilities $P(w_t \mid w_{<t}) = \text{softmax}(\mathbf{z}_t)$. Grammar-constrained decoding imposes a binary token mask $\mathbf{m}_t \in \{0, -\infty\}^{|V|}$ derived from the transition function $\delta(q, w_t, \gamma)$ of a Pushdown Automaton (PDA) recognizing Context-Free Grammar $\mathcal{G}_{\text{CFG}}$:
  $$P_{\text{guided}}(w_t \mid w_{<t}, \mathcal{G}_{\text{CFG}}) = \text{softmax}(\mathbf{z}_t + \mathbf{m}_t)$$
  where $m_{t, i} = 0$ if appending token $i$ maintains a valid partial parse in $\mathcal{A}_{\text{PDA}}$, and $-\infty$ otherwise.
- **Book wording:** "Giải mã ràng buộc ngữ pháp (Grammar-Constrained Decoding): điều chỉnh phân phối xác suất token tại từng bước sinh bằng ôtômat ngăn xếp (Pushdown Automaton), loại bỏ triệt để xác suất của mọi token vi phạm cú pháp."
- **Dangerous simplification:** Confusing constrained decoding with post-hoc rejection sampling or regex search-and-replace.
- **MUST NOT infer:**
  - MUST NOT claim that constrained decoding changes the model's factual knowledge or prevents factual hallucination; it guarantees *syntactic and ontological grammar conformance*, not *factual truth*.
  - MUST NOT claim constrained decoding has zero latency overhead; building and traversing the PDA state index requires non-zero pre-computation.

---

## 2. SHACL-to-CFG Compilation

- **Source:** BOOK-DEFINED compilation algorithm building on SH-01 (W3C SHACL Recommendation), OUTLINES-01
- **Formal meaning:** A deterministic mapping $\mathcal{T}: \mathcal{S}_{\text{SHACL}} \to \mathcal{G}_{\text{EBNF}}$ that compiles NodeShapes and PropertyShapes into EBNF production rules. Specifically, `sh:datatype`, `sh:class`, `sh:minCount`, and `sh:maxCount` compile into grammar repetition operators and terminal regular expressions.
- **Book wording:** "Biên dịch SHACL sang CFG (SHACL-to-CFG Compiler): chuyển đổi các ràng buộc hình dạng (shapes) thành văn phạm phi ngữ cảnh EBNF, bảo đảm đồ thị sinh ra thỏa mãn tiên đề TBox ngay từ cấp độ token."
- **Dangerous simplification:** Believing that any arbitrary SHACL shape (e.g., complex SPARQL-based constraints `sh:sparql`) can be compiled into a context-free grammar.
- **MUST NOT infer:**
  - MUST NOT claim that full SHACL-SPARQL is context-free; only core structural constraints (datatypes, cardinalities, allowed IRIs) compile into standard CFGs.
  - MUST NOT claim that CFG compliance eliminates the need for post-ingestion validation; semantic validation against global graph state is still required.

---

## 3. Equation AST Reification & Symbolic Parsing

- **Source:** SYMPY-01 (Meurer et al., 2017), BOOK-DEFINED Mechanism KG ontology
- **Formal meaning:** Transforming mathematical expressions $E = f(x_1, \dots, x_n)$ into directed rooted trees $T = (V_T, E_T)$ where internal nodes represent mathematical operators and leaf nodes represent variables or physical constants. In the Mechanism KG, the root node of $T$ is reified via `ex:hasFormulaAST` and connected to `Quantity` instances via explicit variable-binding edges.
- **Book wording:** "Hiện thực hóa Cây Cú pháp Trừu tượng của Công thức (Equation AST Reification): bóc tách phương trình vi phân và biểu thức giải tích thành đồ thị cây toán học biểu trưng, liên kết trực tiếp vào các nút Cơ chế (Mechanism)."
- **Dangerous simplification:** Treating mathematical equations as opaque string literals (`"v = ds/dt"^^xsd:string`) without traversable graph structure.
- **MUST NOT infer:**
  - MUST NOT claim that string matching on LaTeX or ASCII formulas is equivalent to symbolic AST graph representation.
  - MUST NOT claim that an AST alone verifies dimensional consistency; units of measure require formal dimensional ontology axioms.

---

## 4. Open Information Extraction (OpenIE) vs. Ontology-Guided Extraction

- **Source:** OPENIE-01 (Banko et al., 2007), DI-01 (Doan et al., 2012)
- **Formal meaning:** OpenIE extracts tuples $(e_1, r_{\text{text}}, e_2)$ where $r_{\text{text}}$ is an arbitrary natural language surface pattern. Ontology-Guided extraction maps mentions directly to a predefined TBox $T = \langle C, R \rangle$. The former maximizes recall on unseen domains at the cost of semantic ambiguity; the latter maximizes precision and deductive interoperability at the cost of schema rigidity.
- **Book wording:** "Bóc tách Mở (OpenIE) vs Bóc tách theo Bản thể luận (Ontology-Guided Extraction): sự đánh đổi giữa khám phá quan hệ mới từ văn bản tự do và ánh xạ chặt chẽ vào cấu trúc TBox xác định trước."
- **Dangerous simplification:** Treating OpenIE outputs as ready-to-query knowledge graph triples without canonicalization.
- **MUST NOT infer:**
  - MUST NOT claim OpenIE triples can be reasoned over with standard OWL DL reasoners without an intermediate entity/relation linking step.
