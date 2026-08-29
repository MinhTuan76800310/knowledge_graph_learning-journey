# Chapter 5 Semantic Contracts

Authoritative reference for every formal concept in Chapter 5. Each record specifies:

- **Source**: authoritative W3C or academic reference
- **Formal meaning**: precise definition from the source
- **Book wording**: simplified phrasing used in the manuscript
- **Dangerous simplification**: what the book wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

This document is the semantic contract against which `book/chapter05.md` is reviewed.

---

## Inference vs Validation (Two Pipelines)

- **Source:** R11-03 (RDFS §3); SH-01 (SHACL §1); OWL-01 (§2)
- **Formal meaning:** Inference (entailment) derives new statements from existing ones: given graph G and semantics Φ, compute consequences(G, Φ). Validation checks whether data satisfies constraints: given data graph D and shapes S, produce conformance report. These are fundamentally different operations with different inputs, outputs, and purposes.
- **Book wording:** "Hai pipeline riêng biệt: Suy diễn (inference) trả lời 'điều gì suy ra được?' — đầu vào là đồ thị + ngữ nghĩa, đầu ra là tri thức mới. Xác nhận (validation) trả lời 'dữ liệu có tuân thủ không?' — đầu vào là dữ liệu + ràng buộc, đầu ra là báo cáo phù hợp/vi phạm."
- **Dangerous simplification:** Saying "inference checks correctness" or "validation derives knowledge."
- **MUST NOT infer:**
  - MUST NOT say inference validates data.
  - MUST NOT say validation produces entailments.
  - MUST NOT conflate the two pipelines at any point.

## Forward Chaining (Fixpoint Algorithm)

- **Source:** Hogan et al., Chapter 4 (Deductive Knowledge); R11-03 (RDFS entailment rules)
- **Formal meaning:** Given a set of rules R and initial graph G₀, forward chaining computes: G_{i+1} = G_i ∪ {head(r) | r ∈ R, body(r) ⊆ G_i}. The algorithm terminates when G_{i+1} = G_i (fixpoint reached). The result G_∞ is the closure of G₀ under R. Termination is guaranteed for finite rule sets over finite graphs when rules are monotonic (no negation in body).
- **Book wording:** "Lặp lại: áp dụng tất cả quy tắc lên đồ thị hiện tại, thêm kết quả vào đồ thị. Dừng khi không còn triple mới nào được sinh ra. Đồ thị kết quả gọi là bao đóng (closure)."
- **Dangerous simplification:** Saying forward chaining always terminates without noting monotonicity requirement. Saying it produces "all" consequences without specifying the rule language/profile.
- **MUST NOT infer:**
  - MUST NOT say forward chaining terminates for arbitrary rule sets (non-monotonic rules may loop).
  - MUST NOT say forward chaining produces all OWL entailments (it only captures the fragment expressible by the chosen rules).
  - MUST NOT conflate fixpoint termination with computational tractability.

## Materialization

- **Source:** Hogan et al., Chapter 4; OWL-05 (Profiles)
- **Formal meaning:** Materialization is the implementation strategy of pre-computing and storing the entailment closure. It is one possible realization of forward chaining. Alternative strategies include query rewriting and backward chaining. Materialization can be unfeasibly large for expressive ontologies.
- **Book wording:** "Vật chất hóa (materialization) là chiến lược tính toán trước toàn bộ bao đóng và lưu trữ kết quả. Đây là một cách triển khai suy diễn, không phải bản thân quan hệ suy diễn."
- **Dangerous simplification:** Saying "the reasoner materializes" as if all reasoners do this. Saying materialization is always feasible.
- **MUST NOT infer:**
  - MUST NOT say entailment requires materialization.
  - MUST NOT say all reasoners use materialization.
  - MUST NOT say materialization is feasible for full OWL 2 DL.

## RDFS Entailment Rules

- **Source:** R11-03 (RDF Schema 1.1, §3)
- **Formal meaning:** RDFS defines specific entailment rules:
  - rdfs:subClassOf: If A rdfs:subClassOf B and x rdf:type A, then x rdf:type B.
  - rdfs:subPropertyOf: If P rdfs:subPropertyOf Q and x P y, then x Q y.
  - rdfs:domain: If P rdfs:domain C and x P y, then x rdf:type C.
  - rdfs:range: If P rdfs:range C and x P y, then y rdf:type C.
  These are INFERENCE rules that ADD information. They do NOT validate or reject data.
- **Book wording:** "Quy tắc RDFS thêm thông tin vào đồ thị. Domain/range không kiểm tra hay từ chối dữ liệu — chúng chỉ suy ra rdf:type mới."
- **Dangerous simplification:** Saying domain/range "constrain" or "validate" data.
- **MUST NOT infer:**
  - MUST NOT say rdfs:domain rejects triples where subject type mismatches.
  - MUST NOT say rdfs:range causes errors on type mismatch.
  - MUST NOT treat RDFS entailment rules as validation constraints.

## SHACL Shape

- **Source:** SH-01 (SHACL §2-3)
- **Formal meaning:** A shape is a condition expressed in RDF that targets specific nodes in a data graph. Shapes define constraints (property constraints, cardinality constraints, value type constraints, etc.) that data nodes must satisfy. Shapes are NOT ontology axioms; they do not participate in entailment.
- **Book wording:** "Shape SHACL là điều kiện kiểm tra trên nút dữ liệu. Shape định nghĩa ràng buộc mà dữ liệu phải thỏa mãn, không phải tiên đề suy diễn."
- **Dangerous simplification:** Saying shapes "define what classes are" or "declare property semantics."
- **MUST NOT infer:**
  - MUST NOT say SHACL shapes participate in OWL/RDFS entailment.
  - MUST NOT say shapes define class membership.
  - MUST NOT confuse shape constraints with ontology axioms.

## SHACL Validation Report

- **Source:** SH-01 (SHACL §4)
- **Formal meaning:** Validation produces a validation report containing: sh:conforms (boolean), and zero or more sh:ValidationResult entries. Each result identifies the focus node, path, constraint component, severity, and message. A conforming graph produces conforms=true with no results. A non-conforming graph produces conforms=false with violation details.
- **Book wording:** "Báo cáo xác nhận gồm: phù hợp (true/false) và danh sách vi phạm (nếu có). Mỗi vi phạm chỉ rõ nút, đường dẫn, loại ràng buộc bị vi phạm."
- **Dangerous simplification:** Saying validation "fixes" data or "derives" corrections.
- **MUST NOT infer:**
  - MUST NOT say a validation report repairs data.
  - MUST NOT say violations indicate logical inconsistency.
  - MUST NOT say conformance means data is empirically true.

## Conformance ≠ Truth

- **Source:** SH-01 (SHACL §1); general validation theory
- **Formal meaning:** Conformance means data satisfies the specified shapes. It does not mean data is factually correct, complete, or consistent with reality. A graph can conform to shapes while containing false information. A graph can violate shapes while containing true information.
- **Book wording:** "Phù hợp (conformance) nghĩa là dữ liệu thỏa mãn các shape đã định nghĩa — không có nghĩa dữ liệu đúng với thực tế. Vi phạm (violation) nghĩa là dữ liệu không khớp shape — không có nghĩa dữ liệu sai."
- **Dangerous simplification:** Saying "valid data is correct" or "invalid data is wrong."
- **MUST NOT infer:**
  - MUST NOT equate conformance with factual correctness.
  - MUST NOT equate violation with factual error.
  - MUST NOT say validation determines truth.

## Violation ≠ Repair

- **Source:** SH-01 (SHACL); general validation theory
- **Formal meaning:** A SHACL violation identifies that data does not satisfy a constraint. It does not prescribe how to fix the data. Multiple repairs may exist for a single violation. Some violations may have no valid repair within the given schema.
- **Book wording:** "Vi phạm chỉ ra sự không phù hợp, không chỉ ra cách sửa. Có thể có nhiều cách sửa, hoặc không có cách sửa hợp lệ."
- **Dangerous simplification:** Saying validation "tells you how to fix" data.
- **MUST NOT infer:**
  - MUST NOT say SHACL provides automatic repair suggestions.
  - MUST NOT say each violation has exactly one fix.

## Soundness

- **Source:** Standard logic; Hogan et al., Chapter 4
- **Formal meaning:** A reasoning procedure is sound w.r.t. an entailment regime Φ if everything it derives is entailed: if procedure derives α from G, then G ⊨_Φ α. Soundness guarantees no false positives. Must specify: (1) the language/profile, (2) the entailment regime, (3) the reasoning task.
- **Book wording:** "Tính đúng đắn (soundness): mọi kết quả suy diễn đều là hệ quả logic thực sự. Không sinh ra tri thức sai. Phải ghi rõ: ngôn ngữ/hồ sơ nào, chế độ suy diễn nào, tác vụ suy luận nào."
- **Dangerous simplification:** Saying a system is "sound" without specifying the scope.
- **MUST NOT infer:**
  - MUST NOT say soundness holds universally across all reasoning tasks.
  - MUST NOT omit the three-part qualification (language, regime, task).

## Completeness

- **Source:** Standard logic; Hogan et al., Chapter 4; OWL-05 (Profiles)
- **Formal meaning:** A reasoning procedure is complete w.r.t. an entailment regime Φ if it derives everything that is entailed: if G ⊨_Φ α, then procedure derives α from G. Completeness guarantees no false negatives. Like soundness, must specify language + regime + task. OWL RL forward chaining is NOT complete on arbitrary RDF graphs.
- **Book wording:** "Tính đầy đủ (completeness): mọi hệ quả logic thực sự đều được suy diễn ra. Không bỏ sót tri thức. Phải ghi rõ phạm vi. Lưu ý: OWL RL forward chaining không đảm bảo đầy đủ trên đồ thị RDF tùy ý."
- **Dangerous simplification:** Saying a rule engine is "complete" without qualification.
- **MUST NOT infer:**
  - MUST NOT say forward chaining on OWL RL is complete for all RDF graphs.
  - MUST NOT say completeness holds without specifying the entailment regime.
  - MUST NOT conflate completeness with soundness.

## Rule (Horn Clause)

- **Source:** Hogan et al., Chapter 4; standard logic programming
- **Formal meaning:** A Horn clause rule has the form: head ← body₁ ∧ body₂ ∧ ... ∧ bodyₙ, where head and each bodyᵢ are atoms. In KG context, atoms are typically triple patterns. Rules enable deriving new triples from existing ones via pattern matching and variable binding. Horn clause rules are monotonic and guarantee termination under forward chaining on finite graphs.
- **Book wording:** "Quy tắc dạng Horn: nếu các điều kiện trong phần thân (body) đều đúng, thì phần đầu (head) cũng đúng. Quy tắc cho phép suy diễn mẫu triple mới từ triple hiện có."
- **Dangerous simplification:** Saying all KG reasoning uses Horn clauses. Saying rules capture full OWL semantics.
- **MUST NOT infer:**
  - MUST NOT say Horn clause rules capture all OWL 2 DL entailments.
  - MUST NOT say rules can express negation-as-failure or disjunction in head.
  - MUST NOT conflate Horn clause rules with SWRL or RIF (which extend beyond Horn).

## SWRL (Semantic Web Rule Language)

- **Source:** SWRL Member Submission (2004); OWL-01
- **Formal meaning:** SWRL extends OWL with Horn-clause-like rules combining OWL class/property expressions in antecedent and consequent. SWRL is a W3C Member Submission, NOT a Recommendation. SWRL rules combined with OWL DL are undecidable in general. Practical implementations restrict to decidable fragments or accept incompleteness.
- **Book wording:** "SWRL mở rộng OWL bằng quy tắc dạng Horn, nhưng kết hợp OWL DL + SWRL nói chung không quyết định được. SWRL là Member Submission, không phải Recommendation."
- **Dangerous simplification:** Teaching SWRL as a stable standard. Saying SWRL rules are always decidable.
- **MUST NOT infer:**
  - MUST NOT present SWRL as a W3C Recommendation.
  - MUST NOT say SWRL + OWL DL reasoning is decidable.
  - MUST NOT teach SWRL syntax as if it were normative.

## SHACL vs Ontology Distinction

- **Source:** SH-01; R11-03; OWL-01
- **Formal meaning:** SHACL shapes and OWL/RDFS axioms serve fundamentally different purposes:
  - OWL/RDFS axioms: define what follows (entailment). Add information. Open-world.
  - SHACL shapes: define what is allowed (validation). Check information. Closed-world over target set.
  A property's rdfs:domain infers types; a SHACL sh:class constraint checks types. Same vocabulary, opposite direction.
- **Book wording:** "Ontology nói 'điều gì suy ra được'; SHACL nói 'điều gì được phép'. Cùng từ vựng (class, property), ngược hướng: ontology thêm thông tin, SHACL kiểm tra thông tin."
- **Dangerous simplification:** Saying SHACL replaces OWL constraints or vice versa.
- **MUST NOT infer:**
  - MUST NOT say SHACL shapes produce entailments.
  - MUST NOT say OWL axioms validate data.
  - MUST NOT say one replaces the other.

## Entailment Regime

- **Source:** SP11-01 (SPARQL Overview §2.4); OWL-01
- **Formal meaning:** An entailment regime specifies which semantic rules apply when computing entailments. Different regimes (RDFS, OWL Direct, OWL RDF-Based, OWL RL, etc.) produce different sets of consequences from the same graph. Soundness and completeness claims are always relative to a specific regime.
- **Book wording:** "Chế độ suy diễn (entailment regime) xác định tập quy tắc ngữ nghĩa áp dụng. Cùng đồ thị, chế độ khác nhau cho kết quả khác nhau. Mọi khẳng định về tính đúng đắn/đầy đủ phải ghi rõ chế độ."
- **Dangerous simplification:** Talking about "entailment" without specifying the regime.
- **MUST NOT infer:**
  - MUST NOT claim entailment results without naming the regime.
  - MUST NOT assume all systems use the same default regime.
