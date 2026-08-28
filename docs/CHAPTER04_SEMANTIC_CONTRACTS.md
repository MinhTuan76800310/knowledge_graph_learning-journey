# Chapter 4 Semantic Contracts

Authoritative reference for every formal concept in Chapter 4. Each record specifies:

- **Source**: authoritative W3C or academic reference
- **Formal meaning**: precise definition from the source
- **Book wording**: simplified phrasing used in the manuscript
- **Dangerous simplification**: what the book wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

This document is the semantic contract against which `book/chapter04.md` is reviewed.

---

## Declaration

- **Source:** OWL 2 Structural Specification §5.8; Direct Semantics §1
- **Formal meaning:** A Declaration associates an IRI with an entity type (Class, ObjectProperty, DataProperty, AnnotationProperty, Datatype, NamedIndividual). Declarations are *nonlogical*: "they do not affect the consequences of an OWL 2 ontology" (Structural Spec §5.8). They serve vocabulary management, typing, and disambiguation.
- **Book wording:** "Khai báo liên kết một IRI với một loại thực thể OWL. Khai báo hỗ trợ quản lý từ vựng và phân giải nhập nhằng, nhưng không tạo ra hệ quả logic."
- **Dangerous simplification:** Saying "a declaration states that a name exists" may imply existential commitment. Under Direct Semantics, declaring a NamedIndividual does not assert empirical existence the way a class assertion does.
- **MUST NOT infer:**
  - MUST NOT say declarations have logical consequences under Direct Semantics.
  - MUST NOT say declaring a NamedIndividual asserts its existence in the same sense as a class/property assertion.

## Annotation

- **Source:** OWL 2 Structural Spec §10; Direct Semantics §1; Primer §8.1
- **Formal meaning:** Annotations "have no semantic meaning in OWL 2 and are ignored" by Direct Semantics (Direct Semantics §1). Axioms may carry annotations, but those annotations do not modify the axiom's logical meaning.
- **Book wording:** "Chú thích không có nghĩa ngữ nghĩa trong OWL 2 Direct Semantics. Ứng dụng có thể diễn giải chú thích bên ngoài ngữ nghĩa logic OWL."
- **Dangerous simplification:** Saying annotations don't affect inference "unless linked to an explicit axiom" is misleading — even annotations on axioms don't change the axiom's logical meaning under Direct Semantics.
- **MUST NOT infer:**
  - MUST NOT say annotations affect logical entailment under Direct Semantics.
  - MUST NOT say annotations on axioms modify the axiom's logical meaning.

## Interpretation

- **Source:** OWL 2 Direct Semantics §2.2
- **Formal meaning:** An interpretation I is a tuple (Δ^I, Δ_D, ·^C, ·^OP, ·^DP, ·^I, ·^DT, ·^LT, ·^FA, NAMED) where Δ^I (object domain) and Δ_D (data domain) are nonempty and disjoint. The book uses a pedagogically simplified form I = (Δ^I, ·^I) for initial exposition.
- **Book wording:** Simplified to I = (Δ^I, ·^I) for object-level concepts; data domain introduced locally in §4.6 data-property section.
- **Dangerous simplification:** Omitting Δ_D entirely loses the distinction between object properties (Δ^I × Δ^I) and data properties (Δ^I × Δ_D).
- **MUST NOT infer:**
  - MUST NOT treat data properties as relations on Δ^I alone.
  - MUST NOT omit mention of the data domain when discussing data properties.

## Object Domain (Δ^I)

- **Source:** OWL 2 Direct Semantics §2.2
- **Formal meaning:** Nonempty set of objects/individuals in the interpretation. Disjoint from data domain Δ_D.
- **Book wording:** "Miền diễn giải" — the set of abstract objects we're talking about.
- **Dangerous simplification:** None significant at this level.
- **MUST NOT infer:**
  - MUST NOT conflate domain elements with named individuals (domain may contain unnamed elements).

## Data Domain (Δ_D)

- **Source:** OWL 2 Direct Semantics §2.2
- **Formal meaning:** Nonempty set of data values, disjoint from Δ^I. Data properties map to subsets of Δ^I × Δ_D.
- **Book wording:** Introduced in §4.6 data-property subsection as the domain of literal/data values.
- **Dangerous simplification:** Treating data values as just another kind of object.
- **MUST NOT infer:**
  - MUST NOT treat data property fillers as members of Δ^I.

## Class Interpretation

- **Source:** OWL 2 Direct Semantics §2.2
- **Formal meaning:** ·^C maps each class name to a subset of Δ^I. owl:Thing maps to Δ^I; owl:Nothing maps to ∅.
- **Book wording:** "Lớp được diễn giải thành tập con của miền."
- **Dangerous simplification:** None at this level.
- **MUST NOT infer:**
  - MUST NOT assume class extensions are nonempty (unless asserted).

## Object Property Interpretation

- **Source:** OWL 2 Direct Semantics §2.2
- **Formal meaning:** ·^OP maps each object property to a subset of Δ^I × Δ^I.
- **Book wording:** "Thuộc tính đối tượng được diễn giải thành quan hệ hai ngôi trên miền."
- **Dangerous simplification:** None at this level.
- **MUST NOT infer:**
  - MUST NOT assume properties are functional, symmetric, etc. unless declared.

## Data Property Interpretation

- **Source:** OWL 2 Direct Semantics §2.2
- **Formal meaning:** ·^DP maps each data property to a subset of Δ^I × Δ_D.
- **Book wording:** "Thuộc tính dữ liệu nối cá thể với giá trị dữ liệu: P^I ⊆ Δ^I × Δ_D."
- **Dangerous simplification:** Treating data properties identically to object properties.
- **MUST NOT infer:**
  - MUST NOT write data property semantics as R^I ⊆ Δ^I × Δ^I.

## Satisfaction

- **Source:** OWL 2 Direct Semantics §2.3
- **Formal meaning:** An interpretation I satisfies an axiom when the corresponding semantic condition holds. E.g., I satisfies SubClassOf(C,D) iff C^I ⊆ D^I.
- **Book wording:** "Diễn giải thỏa mãn tiên đề khi điều kiện ngữ nghĩa của tiên đề đó đúng trong diễn giải."
- **Dangerous simplification:** None at this level.
- **MUST NOT infer:**
  - MUST NOT confuse satisfaction of one axiom with satisfaction of all axioms.

## Model

- **Source:** OWL 2 Direct Semantics §2.4
- **Formal meaning:** A model of ontology O is an interpretation that satisfies ALL axioms in O. Models(O) = {I | I satisfies every axiom in O}.
- **Book wording:** "Mô hình là diễn giải thỏa mãn tất cả các tiên đề trong ontology."
- **Dangerous simplification:** None at this level.
- **MUST NOT infer:**
  - MUST NOT say a model is "the correct interpretation" — there may be many models.

## Entailment

- **Source:** OWL 2 Direct Semantics §2.5
- **Formal meaning:** O entails α (O ⊨ α) iff every model of O satisfies α. Entailment is a semantic relation describing logical consequence; it does not mutate any graph.
- **Book wording:** "O ⊨ α nghĩa là α đúng trong mọi mô hình của O."
- **Dangerous simplification:** Saying "entailment adds knowledge" implies materialization. Entailment is a relation, not an operation.
- **MUST NOT infer:**
  - MUST NOT say entailment modifies or adds triples to the graph.
  - MUST NOT say entailment "creates" anything. Systems may materialize consequences, but the entailment relation itself is purely semantic.

## SubClassOf

- **Source:** OWL 2 Direct Semantics §2.3.1
- **Formal meaning:** I satisfies SubClassOf(CE1, CE2) iff (CE1)^I ⊆ (CE2)^I.
- **Book wording:** "C ⊑ D: mọi phần tử của C đều thuộc D."
- **Dangerous simplification:** Confusing directionality of necessary/sufficient conditions.
- **MUST NOT infer:**
  - MUST NOT say C ⊑ D means C is necessary for D. (C is SUFFICIENT for D; D is NECESSARY for C.)

## EquivalentClasses

- **Source:** OWL 2 Direct Semantics §2.3.1
- **Formal meaning:** I satisfies EquivalentClasses(CE1,...,CEn) iff (CEj)^I = (CEk)^I for all j,k.
- **Book wording:** "A ≡ B: A và B có cùng tập thành viên trong mọi mô hình."
- **Dangerous simplification:** Confusing with owl:sameAs (individual identity vs class equality).
- **MUST NOT infer:**
  - MUST NOT use equivalentClasses to assert individual identity.

## DisjointClasses

- **Source:** OWL 2 Direct Semantics §2.3.1
- **Formal meaning:** I satisfies DisjointClasses(CE1,...,CEn) iff (CEj)^I ∩ (CEk)^I = ∅ for all j≠k.
- **Book wording:** "C ⊓ D ≡ ⊥: không phần tử nào thuộc cả C lẫn D."
- **Dangerous simplification:** Assuming different class names are automatically disjoint.
- **MUST NOT infer:**
  - MUST NOT assume disjointness without explicit axiom.

## Existential Restriction (∃R.C)

- **Source:** OWL 2 Direct Semantics §2.2.3
- **Formal meaning:** (∃R.C)^I = {x ∈ Δ^I | ∃y: (x,y) ∈ R^I ∧ y ∈ C^I}
- **Book wording:** "Những thứ có ít nhất một R-liên kết đến phần tử thuộc C."
- **Dangerous simplification:** Saying "a reasoner creates an anonymous element" conflates model-theoretic existence with implementation behavior.
- **MUST NOT infer:**
  - MUST NOT say OWL entailment materializes blank nodes or explicit RDF triples.
  - MUST NOT say "bộ suy luận tạo ra phần tử ẩn." Correct: "ontology đòi hỏi sự tồn tại của phần tử phù hợp trong mọi mô hình."
  - Semantic existence ≠ serialized/materialized node.

## Universal Restriction (∀R.C)

- **Source:** OWL 2 Direct Semantics §2.2.3
- **Formal meaning:** (∀R.C)^I = {x ∈ Δ^I | ∀y: (x,y) ∈ R^I ⇒ y ∈ C^I}
- **Book wording:** Two levels required:
  - Level A (within one interpretation): if x has no R-successors in I, then x ∈ (∀R.C)^I vacuously.
  - Level B (entailment from ontology/data): absence of R-triples in the RDF graph does NOT entail x : ∀R.C, because another model may contain an unasserted R-successor not in C.
- **Dangerous simplification:** Conflating "no R-successor in a particular interpretation" with "no R assertion in the RDF graph." These are NOT equivalent under open-world semantics.
- **MUST NOT infer:**
  - MUST NOT say absence of R-triples in data entails universal restriction membership.
  - MUST NOT say "Alice has no known children, therefore Alice ∈ (∀hasChild.Doctor)^I" as an entailment from the data. This is only true within a specific interpretation, not entailed by the ontology.
  - Absence in serialization/data ≠ absence in an interpretation.

## Cardinality

- **Source:** OWL 2 Direct Semantics §2.2.3
- **Formal meaning:** (≥n R.C)^I = {x | #{y | (x,y)∈R^I ∧ y∈C^I} ≥ n}. Similarly for ≤n and =n.
- **Book wording:** "Hạn chế về số lượng R-liên kết đến phần tử thuộc C."
- **Dangerous simplification:** Treating cardinality as database constraint validation.
- **MUST NOT infer:**
  - MUST NOT say minCardinality requires explicit RDF triples.
  - MUST NOT say maxCardinality violations cause errors (under OWA + no UNA, identity merging may resolve apparent violations).

## Functional Property

- **Source:** OWL 2 Direct Semantics §2.3.2
- **Formal meaning:** I satisfies FunctionalObjectProperty(OPE) iff ∀x,y1,y2: (x,y1)∈OPE^I ∧ (x,y2)∈OPE^I ⇒ y1=y2.
- **Book wording:** "Mỗi cá thể có nhiều nhất một giá trị cho thuộc tính này trong mô hình."
- **Dangerous simplification:** Saying "the reasoner infers owl:sameAs" as if every reasoner materializes that triple.
- **MUST NOT infer:**
  - MUST NOT say every reasoner emits an owl:sameAs RDF triple. Correct: "ontology entails that the two names denote the same individual."
  - MUST add: if the ontology ALSO asserts the two individuals are different (owl:differentFrom), functionality can make the ontology inconsistent.

## Inverse-Functional Property

- **Source:** OWL 2 Direct Semantics §2.3.2
- **Formal meaning:** I satisfies InverseFunctionalObjectProperty(OPE) iff ∀x1,x2,y: (x1,y)∈OPE^I ∧ (x2,y)∈OPE^I ⇒ x1=x2.
- **Book wording:** "Nếu hai cá thể có cùng giá trị cho thuộc tính nghịch đảo hàm, chúng là một."
- **Dangerous simplification:** Same as functional — identity entailment vs materialization.
- **MUST NOT infer:**
  - MUST NOT say reasoners always materialize identity triples.

## Open World Assumption (OWA)

- **Source:** OWL 2 Direct Semantics (implicit); Primer §2
- **Formal meaning:** OWL semantics does not assume that the data/graph is complete. Absence of an assertion does not entail its negation. Models may contain elements and relationships not present in the serialization.
- **Book wording:** Three-way distinction required:
  - A. Closed-world over database facts: absence of a tuple is often treated as false for the represented state.
  - B. SQL NULL: separate concept using three-valued logic; NULL/UNKNOWN ≠ FALSE.
  - C. OWL OWA: absence of assertion does not imply negation.
- **Dangerous simplification:** Teaching "database missing field = false" as universal. SQL NULL uses three-valued logic and is distinct from CWA.
- **MUST NOT infer:**
  - MUST NOT say all databases universally treat missing as false (SQL NULL exists).
  - MUST NOT conflate CWA with SQL NULL semantics.

## Consistency

- **Source:** OWL 2 Direct Semantics §2.4
- **Formal meaning:** O is consistent iff Models(O) ≠ ∅ (at least one model exists).
- **Book wording:** "Ontology nhất quán khi tồn tại ít nhất một mô hình."
- **Dangerous simplification:** Confusing with satisfiability or data correctness.
- **MUST NOT infer:**
  - MUST NOT say consistency means data is correct.
  - MUST NOT say an inconsistent ontology "has no valid interpretations" without noting that classical entailment becomes vacuous (ex falso quodlibet).

## Class Satisfiability

- **Source:** OWL 2 Direct Semantics (derived)
- **Formal meaning:** C is satisfiable w.r.t. O iff ∃I ∈ Models(O): C^I ≠ ∅.
- **Book wording:** "Lớp C thỏa được khi có ít nhất một mô hình của O trong đó C có thành viên."
- **Dangerous simplification:** Confusing with ontology consistency.
- **MUST NOT infer:**
  - MUST NOT say an unsatisfiable class makes the ontology inconsistent (it doesn't — the class simply has empty extension in all models).

## Direct Semantics

- **Source:** OWL 2 Direct Semantics (entire document)
- **Formal meaning:** Model-theoretic semantics defined on OWL structural-specification constructs. Compatible with Description Logic SROIQ extended with OWL-specific features (datatypes, punning). Applies to OWL 2 DL ontologies satisfying global restrictions. Serialization syntax ≠ semantic regime: an OWL 2 DL ontology serialized in RDF/Turtle can still be interpreted via Direct Semantics after mapping to structural form.
- **Book wording:** "Ngữ nghĩa định nghĩa trực tiếp trên cấu trúc OWL structural model."
- **Dangerous simplification:** Implying Direct Semantics only applies to non-RDF representations.
- **MUST NOT infer:**
  - MUST NOT say RDF/Turtle serialization forces RDF-Based Semantics.
  - MUST NOT say Direct Semantics requires a non-RDF format.
  - Serialization syntax ≠ semantic regime.

## RDF-Based Semantics

- **Source:** OWL 2 RDF-Based Semantics (entire document)
- **Formal meaning:** Semantics defined directly on RDF graphs using OWL vocabulary. Extends RDFS semantics. Supports broader RDF-centric treatment including OWL 2 Full (which is undecidable).
- **Book wording:** "Ngữ nghĩa định nghĩa trực tiếp trên đồ thị RDF, mở rộng ngữ nghĩa RDFS."
- **Dangerous simplification:** Equating RDF-Based Semantics with "RDF files" and Direct Semantics with "non-RDF data."
- **MUST NOT infer:**
  - MUST NOT say the choice of semantics is determined by serialization format.
  - MUST NOT say RDF-Based Semantics is "for RDF files" while Direct is "for other formats."

## OWL Profiles (EL, QL, RL)

- **Source:** OWL 2 Profiles (entire document)
- **Formal meaning:** Three sub-languages of OWL 2 trading expressivity for reasoning tractability. No profile is a subset of another. EL: PTIME for core reasoning tasks (not conjunctive queries). QL: query answering via SQL rewriting; AC0 data complexity. RL: rule-based reasoning compatible with forward-chaining; completeness not guaranteed on arbitrary RDF.
- **Book wording:** Table with design rationale per profile.
- **Dangerous simplification:** Saying EL is "polynomial-time" without qualifying "for core reasoning tasks." Saying RL is "compatible with rule engines" without noting completeness limitations.
- **MUST NOT infer:**
  - MUST NOT say any profile is universally faster/better than another.
  - MUST NOT say EL provides polynomial-time for ALL reasoning tasks.
  - MUST NOT say RL guarantees complete answers on arbitrary RDF graphs.

## Necessary and Sufficient Conditions

- **Source:** Standard logic; OWL 2 Primer §4.2, §5.1
- **Formal meaning:** If A ⊑ B: A is sufficient for B; B is necessary for A. If A ≡ B: A is necessary and sufficient for B (and vice versa).
- **Book wording:** Directionality must be explicit everywhere.
- **Dangerous simplification:** Defining "Sufficient Condition = Equivalence" (wrong — equivalence gives BOTH necessary AND sufficient).
- **MUST NOT infer:**
  - MUST NOT define sufficient condition as equivalence.
  - MUST NOT reverse the directionality of SubClassOf.

## Three Entailment States

- **Source:** Classical model theory
- **Formal meaning:** For a CONSISTENT ontology O and proposition α whose negation is expressible: (1) O ⊨ α (entailed), (2) O ⊨ ¬α (refuted), (3) neither (undetermined). If O is inconsistent, this classification breaks down: classical semantics makes every statement entailed (ex falso quodlibet).
- **Book wording:** Must include consistency precondition.
- **Dangerous simplification:** Presenting three-state classification without noting it assumes consistency.
- **MUST NOT infer:**
  - MUST NOT present three-state classification as unconditional.
  - MUST note that inconsistent ontologies break the classification under classical semantics.

## Entailment ≠ Materialization

- **Source:** Model theory; OWL 2 semantics
- **Formal meaning:** Entailment is a semantic relation. A system MAY compute consequences on demand, materialize them, or cache them. The entailment relation itself does not mutate any graph.
- **Book wording:** "Suy diễn là quan hệ ngữ nghĩa mô tả hệ quả logic. Hệ thống có thể tính toán, vật chất hóa, hoặc lưu cache — nhưng bản thân quan hệ suy diễn không thay đổi đồ thị."
- **Dangerous simplification:** Saying "entailment adds knowledge" or "reasoner creates triples."
- **MUST NOT infer:**
  - MUST NOT say entailment mutates the source graph.
  - MUST NOT conflate semantic consequence with implementation behavior.
