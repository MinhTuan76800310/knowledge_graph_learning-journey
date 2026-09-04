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

## Forward Chaining (Fixpoint Algorithm with Substitution)

- **Source:** Hogan et al., Rules and Reasoning (HOGAN-CH5); RDF-MT-01 (Appendix A); RIF-01
- **Formal meaning:** Given a set of rules R and initial graph G₀, forward chaining computes: G_{i+1} = G_i ∪ { θ(head(r)) | r ∈ R, θ(body(r)) ⊆ G_i }, where θ is a substitution mapping variables to concrete values. The algorithm terminates when G_{n+1} = G_n (fixpoint reached). The result G_∞ is the closure of G₀ under R. Termination requires: finite initial graph, finite rule set, function-free rules, safe/range-restricted variables, no mechanism generating unbounded fresh terms.
- **Book wording:** "Tìm mọi quy tắc r và mọi phép thế θ sao cho phần thân đã thế khớp với đồ thị hiện tại, thêm phần đầu đã thế. Dừng khi không còn triple mới. Đồ thị kết quả gọi là bao đóng (closure)."
- **Dangerous simplification:** Omitting θ from the formula; saying forward chaining always terminates without listing assumptions; conflating closure with entailment.
- **MUST NOT infer:**
  - MUST NOT present the formula without substitution θ.
  - MUST NOT say forward chaining terminates for arbitrary rule sets without stating conditions.
  - MUST NOT conflate fixpoint termination with computational tractability.
  - MUST NOT equate closure (algorithmic object) with entailment (semantic relation).

## Substitution / Binding

- **Source:** Standard logic; HOGAN-CH5; RIF-01 (safeness)
- **Formal meaning:** A substitution θ is a mapping from variables to ground terms (IRIs, literals, blank nodes). Applying θ to a rule pattern replaces each variable with its bound value, producing a ground instance. Safeness requires all head variables appear in body, ensuring θ only uses values already in the graph.
- **Book wording:** "Phép thế θ là ánh xạ gán mỗi biến với một giá trị cụ thể. θ(body) là phần thân đã ground; θ(head) là kết luận đã ground. Phép thế kết nối quy tắc trừu tượng với thực thể cụ thể trong đồ thị."
- **Dangerous simplification:** Treating substitution as notation decoration rather than core mechanism.
- **MUST NOT infer:**
  - MUST NOT omit substitution from the forward-chaining explanation.
  - MUST NOT treat rules as if they operate on abstract patterns without grounding.

## Fixpoint

- **Source:** HOGAN-CH5; standard fixpoint theory
- **Formal meaning:** A fixpoint of forward chaining is a state where G_{n+1} = G_n — applying all rules with all valid substitutions produces no new triples. Under monotonicity and finiteness conditions, the fixpoint is guaranteed to exist and is unique (the least fixpoint containing G₀).
- **Book wording:** "Điểm bất động: G_{n+1} = G_n. Không còn triple mới được sinh ra, bao đóng đã ổn định."
- **Dangerous simplification:** Saying fixpoint means "done" without explaining why no-new-facts implies stability.
- **MUST NOT infer:**
  - MUST NOT say fixpoint guarantees completeness for arbitrary entailment regimes.
  - MUST NOT conflate fixpoint existence with fixpoint computability in bounded time.

## Monotonicity

- **Source:** Standard logic; HOGAN-CH5
- **Formal meaning:** A reasoning regime is monotonic if: whenever G ⊆ G', then Consequences(G) ⊆ Consequences(G'). Adding information to the knowledge base never invalidates previously derivable conclusions. Monotonicity ≠ termination, ≠ completeness, ≠ consistency.
- **Book wording:** "Đơn điệu: nếu G ⊆ G' thì Consequences(G) ⊆ Consequences(G'). Thêm thông tin vào đồ thị không bao giờ làm mất kết luận cũ."
- **Dangerous simplification:** Defining monotonicity over rule bodies instead of knowledge bases; saying "adding conditions to body increases results."
- **MUST NOT infer:**
  - MUST NOT define monotonicity as "adding triples to a rule body increases results."
  - MUST NOT equate monotonicity with termination.
  - MUST NOT equate monotonicity with completeness or consistency.

## Termination Assumptions

- **Source:** RIF-01 (safeness); HOGAN-CH5; standard Datalog theory
- **Formal meaning:** Forward chaining terminates when: (1) finite initial graph, (2) finite rule set, (3) function-free rules, (4) safe/range-restricted variables, (5) no mechanism generating unbounded fresh terms. Under these conditions, only finitely many ground facts can exist, so monotonic growth must reach fixpoint. Termination ≠ monotonicity; non-monotonic ≠ non-terminating.
- **Book wording:** "Forward chaining đảm bảo dừng khi: đồ thị hữu hạn, tập quy tắc hữu hạn, không hàm, biến an toàn, không sinh term mới vô hạn."
- **Dangerous simplification:** Saying "finite graph + monotonic rules → always terminates" without listing all conditions.
- **MUST NOT infer:**
  - MUST NOT claim termination without stating all required assumptions.
  - MUST NOT equate termination with monotonicity.
  - MUST NOT equate non-monotonicity with non-termination.

## Materialization

- **Source:** HOGAN-CH5; OWL-05 (Profiles)
- **Formal meaning:** Materialization is the implementation strategy of pre-computing and storing the entailment closure. It is one possible realization of forward chaining. Alternative strategies include query rewriting and backward chaining. Materialization can be unfeasibly large for expressive ontologies. Asserted triples ≠ derived triples; metadata distinguishing them should be preserved.
- **Book wording:** "Vật chất hóa (materialization) là chiến lược tính toán trước toàn bộ bao đóng và lưu trữ kết quả. Đây là một cách triển khai suy diễn, không phải bản thân quan hệ suy diễn."
- **Dangerous simplification:** Saying "the reasoner materializes" as if all reasoners do this. Saying materialization is always feasible.
- **MUST NOT infer:**
  - MUST NOT say entailment requires materialization.
  - MUST NOT say all reasoners use materialization.
  - MUST NOT say materialization is feasible for full OWL 2 DL.

## Backward Chaining

- **Source:** Standard logic programming; HOGAN-CH5
- **Formal meaning:** Goal-driven reasoning: start from query, find rules whose head matches, create subgoals from body, recurse until reaching asserted facts. Contrasted with forward chaining (data-driven). An algorithmic mental model, not a claim about all OWL reasoners.
- **Book wording:** "Suy diễn lùi: bắt đầu từ câu hỏi, tìm quy tắc có head khớp, tạo subgoal, đệ quy đến assertion."
- **Dangerous simplification:** Claiming all OWL reasoners are backward rule engines.
- **MUST NOT infer:**
  - MUST NOT say all Description Logic reasoners use backward chaining.
  - MUST NOT present backward chaining as universally superior or inferior to forward.

## RDFS Entailment Rules

- **Source:** RDF-MT-01 (RDF 1.1 Semantics, §9.2.1); R11-03 (RDF Schema 1.1)
- **Formal meaning:** RDFS defines specific entailment patterns (rdfs2-domain, rdfs3-range, rdfs7-subPropertyOf, rdfs9-subClassOf, etc.) in RDF 1.1 Semantics. These are model-theoretically defined semantic conditions. They CAN be operationalized as forward-chaining rules (Appendix A), which is correct but not complete on standard RDF syntax; completeness requires generalized RDF. Domain/range are INFERENCE rules that ADD information, NOT validation constraints.
- **Book wording:** "Quy tắc RDFS thêm thông tin vào đồ thị. Domain/range không kiểm tra hay từ chối dữ liệu — chúng chỉ suy ra rdf:type mới. Ngữ nghĩa chuẩn được định nghĩa model-theoretically; rule-based approach là operationalization đúng đắn nhưng không đầy đủ trên cú pháp RDF chuẩn."
- **Dangerous simplification:** Saying domain/range "constrain" or "validate" data. Saying naive rule closure computes ALL normative RDFS entailments without qualification.
- **MUST NOT infer:**
  - MUST NOT say rdfs:domain rejects triples where subject type mismatches.
  - MUST NOT say rdfs:range causes errors on type mismatch.
  - MUST NOT treat RDFS entailment rules as validation constraints.
  - MUST NOT claim rule-based closure is complete for all RDFS entailments without noting the generalized RDF requirement.

## SPARQL Entailment Regime

- **Source:** SP11-ENT (SPARQL 1.1 Entailment Regimes)
- **Formal meaning:** Entailment regimes are specified via SPARQL Service Description (sd:defaultEntailmentRegime, sd:entailmentRegime), NOT via FROM clause. FROM selects graphs/datasets. Standard regime IRIs defined for RDF, RDFS, D, OWL-Direct, OWL-RDF-Based. Default behavior is implementation/configuration-dependent, not standardized.
- **Book wording:** "Chế độ suy diễn được chỉ định qua SPARQL Service Description, không phải FROM clause. FROM chọn đồ thị, không chọn regime."
- **Dangerous simplification:** Saying FROM changes entailment regime. Claiming universal default regime.
- **MUST NOT infer:**
  - MUST NOT say FROM clause selects entailment regime.
  - MUST NOT claim a universal default entailment regime without citing specific implementation.
  - MUST NOT conflate graph selection with semantic regime selection.

## SHACL Shape

- **Source:** SH-01 (SHACL §2-3)
- **Formal meaning:** A shape is a condition expressed in RDF that targets specific nodes in a data graph. Shapes define constraints that data nodes must satisfy. Shapes are NOT ontology axioms; they do not participate in entailment. SHACL is not "closed-world OWL" — it is a separate validation framework with its own semantics.
- **Book wording:** "Shape SHACL là điều kiện kiểm tra trên nút dữ liệu. Shape định nghĩa ràng buộc mà dữ liệu phải thỏa mãn, không phải tiên đề suy diễn. SHACL không phải OWL với CWA."
- **Dangerous simplification:** Saying shapes "define what classes are" or "declare property semantics." Teaching SHACL as "closed-world OWL."
- **MUST NOT infer:**
  - MUST NOT say SHACL shapes participate in OWL/RDFS entailment.
  - MUST NOT say shapes define class membership.
  - MUST NOT confuse shape constraints with ontology axioms.
  - MUST NOT teach SHACL as simply OWL with CWA turned on.

## SHACL Instance / targetClass Semantics

- **Source:** SH-01 (§2.1.3.2)
- **Formal meaning:** sh:targetClass c targets all SHACL instances of c. A node n is a SHACL instance of class c if there exists a chain n rdf:type t₁, t₁ rdfs:subClassOf t₂, ..., tₖ rdfs:subClassOf c in the data graph. This includes subclass reasoning, not just exact rdf:type matching. The required rdfs:subClassOf declarations must exist in the data graph.
- **Book wording:** "sh:targetClass nhắm đến tất cả SHACL instances của lớp, bao gồm subclass reasoning qua rdfs:subClassOf*. Không phải exact rdf:type grep."
- **Dangerous simplification:** Describing targetClass as only an exact explicit rdf:type lookup.
- **MUST NOT infer:**
  - MUST NOT say sh:targetClass only matches nodes with explicit rdf:type triple.
  - MUST NOT ignore subclass chain in targeting semantics.

## sh:class Semantics

- **Source:** SH-01 (§4.1.1)
- **Formal meaning:** sh:class C constraint checks whether each value node is a SHACL instance of C (using rdfs:subClassOf* chain). Not just explicit rdf:type C check.
- **Book wording:** "sh:class kiểm tra xem value node có phải SHACL instance của lớp, dùng subclass reasoning."
- **Dangerous simplification:** Reducing sh:class to exact rdf:type match.
- **MUST NOT infer:**
  - MUST NOT say sh:class only checks explicit rdf:type triple.
  - MUST NOT ignore subclass reasoning in class validation.

## Focus Node

- **Source:** SH-01 (§2.1.2)
- **Formal meaning:** A focus node is an RDF term that is validated against a shape using the triples from a data graph. Selected by target mechanism (sh:targetClass, sh:targetNode, etc.).
- **Book wording:** "Focus node là nút dữ liệu đang được đánh giá chống lại một shape."
- **Dangerous simplification:** None significant; straightforward concept.
- **MUST NOT infer:**
  - MUST NOT confuse focus node with value node.

## Value Node

- **Source:** SH-01 (§2.1.2, §3.7)
- **Formal meaning:** For node shapes, value nodes = {focus node}. For property shapes, value nodes are nodes reached from the focus node via the path mapping. Constraints are evaluated against the set of value nodes.
- **Book wording:** "Value node là nút reachable từ focus node qua path. Với node shape, value nodes = {focus node}."
- **Dangerous simplification:** Confusing value nodes with focus nodes.
- **MUST NOT infer:**
  - MUST NOT say value nodes are always different from focus nodes.
  - MUST NOT confuse value node selection with constraint evaluation.

## Validation Result / Report Anatomy

- **Source:** SH-01 (§3.6)
- **Formal meaning:** Validation produces a report with sh:conforms (boolean) and zero or more sh:ValidationResult entries. Each result may include: sh:focusNode, sh:resultPath, sh:value (only when applicable per constraint component), sh:sourceShape, sh:sourceConstraintComponent, sh:resultSeverity, sh:resultMessage. sh:value is optional — e.g., minCount violations may have no offending value node.
- **Book wording:** "Báo cáo gồm conforms + danh sách ValidationResult. Mỗi result trả lời: nút nào, path nào, giá trị nào (khi applicable), shape nào, constraint nào, mức độ, thông báo."
- **Dangerous simplification:** Fabricating sh:value when none exists. Omitting key properties.
- **MUST NOT infer:**
  - MUST NOT say sh:value is always present.
  - MUST NOT fabricate value for minCount/maxCount violations where no offending value exists.
  - MUST NOT say validation report repairs data.

## Conformance ≠ Truth

- **Source:** SH-01 (SHACL §1); general validation theory
- **Formal meaning:** Conformance means data satisfies the specified shapes. It does not mean data is factually correct, complete, or consistent with reality. A graph can conform while containing false information. A graph can violate while containing true information.
- **Book wording:** "Phù hợp (conformance) nghĩa là dữ liệu thỏa mãn các shape — không có nghĩa dữ liệu đúng với thực tế."
- **Dangerous simplification:** Saying "valid data is correct" or "invalid data is wrong."
- **MUST NOT infer:**
  - MUST NOT equate conformance with factual correctness.
  - MUST NOT equate violation with factual error.
  - MUST NOT say validation determines truth.

## Violation ≠ Repair

- **Source:** SH-01 (SHACL); general validation theory
- **Formal meaning:** A SHACL violation identifies that data does not satisfy a constraint. It does not prescribe how to fix the data. Multiple repairs may exist (ADD, DELETE, RECLASSIFY, SHAPE CHANGE). Only domain knowledge/evidence/governance can decide. Passes validation ≠ becomes true.
- **Book wording:** "Vi phạm chỉ ra sự không phù hợp, không chỉ ra cách sửa. Nhiều candidate repairs có thể tồn tại. Chỉ domain knowledge/governance mới quyết định repair đúng."
- **Dangerous simplification:** Saying validation "tells you how to fix" data. Treating repair as syntactic patch.
- **MUST NOT infer:**
  - MUST NOT say SHACL provides automatic repair suggestions.
  - MUST NOT say each violation has exactly one fix.
  - MUST NOT equate passing validation with becoming true.

## Consistency vs Validation (Two Independent Axes)

- **Source:** OWL-01; SH-01; standard logic
- **Formal meaning:** Consistency asks "does at least one model exist?" (model-theoretic). Validation asks "does this supplied data graph conform to declared shapes?" These are independent axes: OWL-inconsistent + SHACL-conformant is possible; OWL-consistent + SHACL-invalid is possible.
- **Book wording:** "Consistency và conformance là hai trục độc lập. Biết một không suy ra cái kia."
- **Dangerous simplification:** Conflating consistency with conformance. Saying inconsistency implies SHACL violation or vice versa.
- **MUST NOT infer:**
  - MUST NOT say OWL inconsistency implies SHACL non-conformance.
  - MUST NOT say SHACL violation implies OWL inconsistency.
  - MUST NOT treat the two axes as correlated.

## Effective Validation Graph

- **Source:** SH-01; engineering practice
- **Formal meaning:** The graph actually validated by the SHACL processor. May be the asserted graph, an expanded graph (after materialization/inference), or a hybrid. This is an architectural decision that must be documented. Different architectures produce different validation results from the same asserted data.
- **Book wording:** "Effective validation graph là đồ thị thực sự được validate. Có thể là asserted, expanded, hoặc hybrid. Phải document rõ."
- **Dangerous simplification:** Assuming all SHACL processors see the same graph. Ignoring the inference-before-validation interaction.
- **MUST NOT infer:**
  - MUST NOT assume all SHACL processors automatically perform inference.
  - MUST NOT assume SHACL always ignores inferred triples.
  - MUST NOT leave effective validation graph undocumented in production systems.

## Soundness

- **Source:** Standard logic; HOGAN-CH5
- **Formal meaning:** A reasoning procedure is sound w.r.t. an entailment regime Φ if everything it derives is entailed: A ⊆ E. Must specify: (1) language/profile, (2) entailment regime, (3) reasoning task.
- **Book wording:** "Soundness: A ⊆ E. Mọi kết quả suy diễn đều là hệ quả logic thực sự. Phải ghi rõ ba thành phần."
- **Dangerous simplification:** Saying a system is "sound" without specifying scope.
- **MUST NOT infer:**
  - MUST NOT say soundness holds universally across all reasoning tasks.
  - MUST NOT omit the three-part qualification.

## Completeness

- **Source:** Standard logic; HOGAN-CH5; OWL-05 (Theorem PR1)
- **Formal meaning:** A reasoning procedure is complete w.r.t. an entailment regime Φ if it derives everything entailed: E ⊆ A. OWL RL forward chaining: complete under specific syntactic conditions (Theorem PR1), NOT on arbitrary RDF graphs. Must specify language + regime + task.
- **Book wording:** "Completeness: E ⊆ A. OWL RL forward chaining complete dưới điều kiện syntactic cụ thể (Theorem PR1), không phải trên arbitrary RDF."
- **Dangerous simplification:** Saying OWL RL is "complete for arbitrary RDF" or tautologically "complete for RL rules."
- **MUST NOT infer:**
  - MUST NOT say forward chaining on OWL RL is complete for all RDF graphs.
  - MUST NOT use tautological completeness claims.
  - MUST NOT omit Theorem PR1 conditions when discussing OWL RL completeness.

## Rule (Horn Clause)

- **Source:** HOGAN-CH5; RIF-01; standard logic programming
- **Formal meaning:** A Horn clause rule: head ← body₁ ∧ ... ∧ bodyₙ, where head and bodyᵢ are atoms (triple patterns with variables). Variables connected via substitution θ. Monotonic. Termination under safety/finiteness conditions. Cannot express negation, disjunction in head, or existential quantification in head.
- **Book wording:** "Quy tắc Horn: head ← body₁ ∧ ... ∧ bodyₙ. Dùng phép thế θ để ground. Đơn điệu, dừng được với điều kiện an toàn."
- **Dangerous simplification:** Saying all KG reasoning uses Horn clauses. Omitting substitution.
- **MUST NOT infer:**
  - MUST NOT say Horn clause rules capture all OWL 2 DL entailments.
  - MUST NOT say rules can express negation-as-failure or disjunction in head.

## SWRL (Semantic Web Rule Language)

- **Source:** SWRL-01 (Member Submission 2004); OWL-01
- **Formal meaning:** SWRL extends OWL with Horn-clause-like rules. W3C Member Submission, NOT Recommendation. Undecidable with OWL DL in general. Ecosystem context, not core teaching content.
- **Book wording:** "SWRL mở rộng OWL bằng quy tắc Horn, nhưng undecidable với OWL DL. Member Submission, không phải Recommendation."
- **Dangerous simplification:** Teaching SWRL as stable standard. Overemphasizing at expense of core mechanisms.
- **MUST NOT infer:**
  - MUST NOT present SWRL as W3C Recommendation.
  - MUST NOT say SWRL + OWL DL reasoning is decidable.

## SHACL vs Ontology Distinction

- **Source:** SH-01; RDF-MT-01; OWL-01
- **Formal meaning:** OWL/RDFS axioms define what follows (entailment, model-theoretic). SHACL shapes define what is allowed (validation, data-graph-specific). Same vocabulary, opposite direction. OWL existential restriction ≠ SHACL minCount. SHACL ≠ closed-world OWL.
- **Book wording:** "Ontology nói 'điều gì suy ra được'; SHACL nói 'điều gì được phép'. Cùng từ vựng, ngược hướng. SHACL không phải OWL với CWA."
- **Dangerous simplification:** Saying SHACL replaces OWL or vice versa. Teaching SHACL as "closed-world OWL."
- **MUST NOT infer:**
  - MUST NOT say SHACL shapes produce entailments.
  - MUST NOT say OWL axioms validate data.
  - MUST NOT say one replaces the other.
  - MUST NOT teach SHACL as simply OWL + CWA.

## Entailment Regime

- **Source:** SP11-ENT; OWL-01
- **Formal meaning:** An entailment regime specifies which semantic rules apply. Different regimes produce different consequence sets. Soundness/completeness claims are always relative to a regime. In SPARQL, specified via Service Description.
- **Book wording:** "Chế độ suy diễn xác định tập quy tắc ngữ nghĩa. Cùng đồ thị, chế độ khác nhau cho kết quả khác nhau."
- **Dangerous simplification:** Talking about "entailment" without specifying regime.
- **MUST NOT infer:**
  - MUST NOT claim entailment results without naming the regime.
  - MUST NOT assume all systems use the same default regime.

## OWL 2 DL Materialization Limits

- **Source:** OWL-05; OWL-04
- **Formal meaning:** General OWL 2 DL reasoning cannot be understood as repeatedly appending entailed RDF triples. Existential semantics may require unnamed witnesses; model structures may not correspond to finite materialized RDF graph; practical DL reasoners use tableau/hypertableau/classification, not naive triple closure.
- **Book wording:** "OWL 2 DL reasoning không thể hiểu đơn giản là vật chất hóa toàn bộ RDF triple closure. Existential witnesses, model structures, và thuật toán chuyên biệt làm cho naive materialization không khả thi hoặc không đúng."
- **Dangerous simplification:** Saying "full OWL 2 DL generates infinitely many triples" without explaining why.
- **MUST NOT infer:**
  - MUST NOT say OWL 2 DL materialization simply produces infinite triples.
  - MUST NOT imply finite RDF materialization is always the correct computation model for OWL 2 DL.

## Graph Repair

- **Source:** SH-01; general validation theory
- **Formal meaning:** Repair is a decision problem: given a violation, multiple candidate repairs exist (ADD, DELETE, RECLASSIFY, SHAPE CHANGE). Only domain knowledge/evidence/governance determines the epistemically correct mutation. Passes validation ≠ becomes true. Pipeline: Violation → Candidates → Evaluate → Select → Revalidate.
- **Book wording:** "Repair là bài toán quyết định. Nhiều candidate repairs. Chỉ domain knowledge mới chọn được. Passes validation ≠ becomes true."
- **Dangerous simplification:** Treating repair as automatic/syntactic. Saying validation determines the correct fix.
- **MUST NOT infer:**
  - MUST NOT say SHACL determines the correct repair.
  - MUST NOT treat repair as purely syntactic.
  - MUST NOT equate passing validation with becoming true.

## Datalog and Its Three Equivalent Semantics

- **Source:** DBFOUND-01 (Abiteboul, Hull & Vianu, *Foundations of Databases*, 1995); DATALOG-01 (Green et al. 2013); HOGAN-CH5
- **Formal meaning:** A Datalog program is a finite set of safe, function-free Horn rules $A \leftarrow B_1,\dots,B_n$ (every head variable occurs in the body). It has three semantics that provably coincide: (1) model-theoretic — the minimal Herbrand model $\mathcal{M}(P)$, the intersection of all Herbrand models of $P$ containing the extensional database $D$; (2) proof-theoretic — the set of facts with a finite derivation; (3) fixpoint — $\mathrm{lfp}(T_P)$, the least fixed point of the immediate consequence operator. Data complexity is PTIME-complete; combined complexity is EXPTIME-complete.
- **Book wording:** "Các quy tắc Horn an toàn, không hàm chính là Datalog. Ba cách nhìn — mô hình nhỏ nhất, chứng minh được, và điểm bất động của $T_P$ — cho cùng một tập sự kiện. Chi phí theo dữ liệu là PTIME, theo chương trình kết hợp dữ liệu là EXPTIME."
- **Dangerous simplification:** Presenting the three-way equivalence as holding for arbitrary first-order logic, or for Datalog with function symbols or unsafe rules. Conflating data complexity with combined complexity.
- **MUST NOT infer:**
  - MUST NOT claim the three semantics coincide outside safe, function-free Datalog.
  - MUST NOT state the practical "cheap once rules are fixed" claim on combined complexity; it rests on data complexity.
  - MUST NOT equate the minimal Herbrand model with an OWL/DL model-theoretic interpretation (different frameworks).

## Monotonicity vs Negation as Failure and Stratification

- **Source:** DBFOUND-01; REITER-CWA-01 (Reiter 1978); HOGAN-CH5
- **Formal meaning:** Classical negation ($\neg$) is monotonic and read under OWA: a derived $\neg P$ is never retracted by adding facts. Negation as Failure (`not` / $\sim$) is non-monotonic and CWA-flavored: `not P` holds when $P$ is not derivable, so adding a fact for $P$ can invalidate prior conclusions. Unstratified negation is ambiguous — $p \leftarrow \text{not } q,\ q \leftarrow \text{not } p$ has two minimal models. A program is stratified when a level map $s$ assigns each predicate an integer such that any predicate under `not` in a rule with head $P$ satisfies $s(Q) < s(P)$; every stratified program has a unique perfect model computed stratum by stratum.
- **Book wording:** "Phủ định cổ điển đơn điệu; phủ định dạng thất bại (`not`) phi đơn điệu. Vòng phủ định không phân tầng tạo mơ hồ. Phân tầng — vị từ bị phủ định phải ở tầng thấp hơn — cho mô hình duy nhất."
- **Dangerous simplification:** Saying `not` is just classical negation; implying stratification is about the data rather than the program; claiming all Datalog-with-not has a unique model.
- **MUST NOT infer:**
  - MUST NOT treat NAF as monotonic or as OWA.
  - MUST NOT assert a unique model for a non-stratifiable negated program.
  - MUST NOT say stratification can be fixed by reordering data; it is a property of the rule set.

## SHACL as Non-Monotonic Local-Closed-World Validation

- **Source:** SH-01 (SHACL §2–3); REITER-CWA-01 (context only)
- **Formal meaning:** SHACL evaluates constraints against the supplied data graph and reads the local absence of triples as constraint failure (e.g. `sh:minCount`, `sh:maxCount`). This is a *local* closed-world reading scoped to the focus node's neighborhood, not the global CWA of a logic program. Consequence: SHACL validation is non-monotonic — adding triples can flip a focus node from conforming to violating (e.g. adding a value that exceeds `sh:maxCount`). This is the opposite of forward chaining, which is monotonic.
- **Book wording:** "SHACL đọc sự vắng mặt cục bộ trong đồ thị đang xét là vi phạm, nên thêm bộ ba có thể lật kết quả từ phù hợp sang vi phạm. Đây là kiểm tra phi đơn điệu — khác suy diễn tiến đơn điệu."
- **Dangerous simplification:** Calling SHACL "closed-world OWL"; implying SHACL performs global CWA inference; saying validation is monotonic like entailment.
- **MUST NOT infer:**
  - MUST NOT say SHACL derives entailments or that its closed-world reading is the global CWA.
  - MUST NOT claim adding data can only help conformance.
  - MUST NOT conflate SHACL's local-closed-world validation with Datalog NAF (different mechanisms, both non-monotonic).

## RETE Pattern Matching

- **Source:** RETE-01 (Forgy 1982); RDFOX-01 (Motik et al. 2014)
- **Formal meaning:** RETE compiles a rule set into a discrimination network: alpha nodes apply single-pattern (intra-element) conditions; beta nodes perform two-input joins of variable bindings across patterns and cache intermediate tuples in beta memory; working-memory elements (WMEs) flow in; matched rule instantiations go on an agenda resolved by a conflict-resolution strategy. RETE reuses partial matches across data changes (memory-for-speed) and computes the same monotonic closure $\mathrm{lfp}(T_P)$ as naive forward chaining, only faster. RDFox instead evaluates Datalog with parallel, lock-free incremental materialisation over a compressed main-memory graph.
- **Book wording:** "RETE biên dịch tập luật thành mạng alpha (lọc trong một mẫu) + beta (nối giữa mẫu, cache bộ ghép), tái dùng khớp từng phần — đánh đổi bộ nhớ lấy tốc độ. Nó tính cùng bao đóng như forward chaining, chỉ nhanh hơn. RDFox dùng hướng khác: Datalog tăng dần song song."
- **Dangerous simplification:** Claiming RETE changes the result; presenting RETE as the only rule-engine strategy; implying parallel evaluation alters semantics.
- **MUST NOT infer:**
  - MUST NOT say RETE computes something different from naive forward chaining.
  - MUST NOT claim RETE is universally best; RDFox-style incremental Datalog is an alternative.
  - MUST NOT imply parallelism changes the fixpoint; it exploits the order-independence of $\mathrm{lfp}(T_P)$.
