# Chapter 3 — Semantic Contracts

Authoritative reference for every formal concept in Chapter 3. Each record specifies:

- **Source**: authoritative W3C or academic reference
- **Formal meaning**: precise definition from the source
- **Book wording**: simplified phrasing used in the manuscript
- **Dangerous simplification**: what the book wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

This document is the semantic contract against which `book/chapter03.md` is reviewed.

---

## RDFS Semantics (subClassOf, subPropertyOf, domain, range)

- **Source:** R11-03 (RDF Schema 1.1 §5); RDF-MT-01 (RDF 1.1 Semantics §7)
- **Formal meaning:** RDFS axioms have model-theoretic semantics. `rdfs:subClassOf`
  constrains class extensions: if C rdfs:subClassOf D then C^I ⊆ D^I. `rdfs:domain` on
  property p with class C gives: if (x,y) ∈ p^I then x ∈ C^I. `rdfs:range` gives: if
  (x,y) ∈ p^I then y ∈ D^I. `rdfs:subPropertyOf` gives: if p rdfs:subPropertyOf q then
  p^I ⊆ q^I. These produce entailments (e.g., type propagation from predicate usage).
- **Book wording:** "Nếu khai báo ex:capitalOf rdfs:domain ex:City, bộ suy luận *suy ra*
  ex:Hanoi rdf:type ex:City từ triple ex:Hanoi ex:capitalOf ex:Vietnam." (§3.1.3 and the
  §3.1.7 schema table: subClassOf = subclass, domain = subject's class, range = object's class)
- **Dangerous simplification:** Treating domain/range as documentation ("this is where the
  predicate is normally used") instead of a semantic constraint that licenses entailment;
  or treating them as hard cardinality type constraints (they are not; they derive types,
  they do not enforce them).
- **MUST NOT infer:**
  - MUST NOT say declarations `rdfs:domain`/`rdfs:range` validate input data (validation is
    a SHACL concern, Ch5 — this is the conformance ≠ consistency distinction echoed in Ch5 §5.9).
  - MUST NOT present RDFS entailment as optional or application-specific behavior.
  - MUST NOT say a resource is "in" a class merely because a term is defined as `rdfs:Class`.

## owl:sameAs

- **Source:** OWL-01 (OWL 2 Overview), OWL-02 (OWL 2 Primer)
- **Formal meaning:** `owl:sameAs` asserts that two IRIs denote the same individual. Under
  OWL semantics, if a owl:sameAs b, then for any property p, p(a, x) iff p(b, x), and
  class membership transfers: a and b are interchangeable in every assertion. It is an
  equivalence relation (reflexive, symmetric, transitive).
- **Book wording:** "owl:sameAs là khẳng định đồng nhất — không phải 'gần giống'. Thông
  tin lan truyền qua owl:sameAs: dân số, quan hệ, nhãn." (§3.2.4)
- **Dangerous simplification:** Treating sameAs as "similar" or "related" — Ch3 teaches
  "sameAs is identity, not similarity" and shows the propagation consequence plus the
  danger when the claim is wrong.
- **MUST NOT infer:**
  - MUST NOT use owl:sameAs to express "similar but not identical."
  - MUST NOT say sameAs only merges labels — it merges the individuals across all roles.

## Unique Name Assumption (UNA)

- **Source:** OWL-01, OWL-02 (OWL does not adopt UNA)
- **Formal meaning:** The Unique Name Assumption states distinct names denote distinct
  individuals. OWL does not make this assumption: two different IRIs MAY denote the same
  individual unless the tie is asserted (e.g., via owl:sameAs) or provable from the
  axioms. Identity is open.
- **Book wording:** "Không có giả định tên duy nhất: tên khác nhau thì thực thể khác
  nhau chỉ là một giả định mà OWL không dùng." (§3.2.3)
- **Dangerous simplification:** Assuming that because the data shows no sameAs between two
  IRIs, they are automatically distinct — that is a closed-world reading.
- **MUST NOT infer:**
  - MUST NOT state "two different IRIs are different entities" without qualification.
  - MUST NOT present UNA as an RDFS/OWL default behavior.

## Named Graph / RDF Dataset

- **Source:** R11-02 (RDF 1.1 Concepts §4, dataset with graph names); SP11-02 (RDF Dataset
  semantics); R12-01 (RDF 1.2 emerging — dataset terminology)
- **Formal meaning:** An RDF dataset is a collection of graphs: one default graph plus zero
  or more named graphs, where each named graph is a pair (graph name, graph). Graph names
  are IRIs (or blank nodes). A named graph groups statements under a name; it does not, by
  itself, attribute the triples to a source in the epistemic sense.
- **Book wording:** "Named graph cho phép gom nhóm các phát biểu và gắn cả nhóm với một
  tên; mỗi named graph là cặp (tên đồ thị, đồ thị)." (§3.3.2)
- **Dangerous simplification:** Equating "the graph is named ex:textbookA" with "the
  source ex:textbookA asserted these triples" — the book explicitly warns this is not
  automatic (§3.3.2 callout); the epistemic attribution requires a claim/evidence model
  (Ch6).
- **MUST NOT infer:**
  - MUST NOT say named graph naming by itself asserts provenance/attribution.
  - MUST NOT say the default graph is the union of all named graphs (dataset semantics
    treat them as distinct graphs; SPARQL default graph selection is query-dependent).

## N-ary Relation (Qualified / Reified Statement)

- **Source:** NARY-01 (Defining N-ary Relations on the Semantic Web)
- **Formal meaning:** When a relation has more than two participants, or needs
  first-class properties of its own (time, confidence, method), the binary-edge encoding
  is insufficient. The pattern introduces an intermediate object (reification or
  qualification) whose predicates capture the participants. In RDF 1.1 this is often done
  with the `rdf:Statement`/`rdf:subject`/`rdf:predicate`/`rdf:object` vocabulary
  (reification) or with a domain-specific relation object (e.g., `ex:derivativeApplication_1`).
- **Book wording:** "Quan hệ n-ngôi: quan hệ nhiều hơn hai tham gia hoặc cần thuộc tính
  của chính quan hệ đó, mô hình hóa bằng đối tượng trung gian." (§3.3.3)
- **Dangerous simplification:** Claiming reification "adds nothing but noise" (it has
  known limitations under RDF 1.1 semantics but is a standard, learnable pattern), or
  claiming a qualified statement introduces new *entailments* on the original triple.
- **MUST NOT infer:**
  - MUST NOT say reifying a triple creates a new true statement with logical force beyond
    what is asserted.
  - MUST NOT describe DerivativeApplication as an edge labeled "is applied to" — it is an
    n-ary object with explicit participants.

## Qualifier (Wikidata Statement Qualification)

- **Source:** WD-02 (Wikidata Help: Qualifiers)
- **Formal meaning:** A Wikidata statement is the unit subject–property–value; qualifiers
  are additional property–value pairs attached to that statement to provide context (time,
  location, validity, method, "applies to part"). Qualifiers narrow or refine the
  statement's scope; they are not separate statements about the subject.
- **Book wording:** "Qualifier là các cặp (thuộc tính, giá trị) gắn vào phát biểu để thêm
  chiều ngữ cảnh cho phát biểu, không phải phát biểu độc lập về chủ thể." (§3.3)
- **Dangerous simplification:** Treating a qualifier as a property of the entity (it
  qualifies the statement, not the subject).
- **MUST NOT infer:**
  - MUST NOT say qualified statements carry inherent truth — Wikidata statements carry
    references and ranks (§6.9) which are separate mechanisms.
  - MUST NOT conflate qualifiers with confidence scores (confidence is a Ch6 concern).

## Entity Resolution / Identity Alignment (book model)

- **Source:** H01 (Hogan et al.), S04 (Stanford What Are Graph Data Models); book-defined
  and research-grounded
- **Formal meaning:** Entity resolution decides whether two identifiers denote the same
  real-world entity, using definitional evidence (what the two sources say about the
  entity). It produces either a merge (owl:sameAs) or a rejection (they are distinct).
  Record linkage is the data-integration term for this problem. The book treats this as a
  decision procedure with evidence, not a naming convention.
- **Book wording:** "Entity resolution: suy luận hai định danh có cùng một thực thể hay
  không, dựa trên bằng chứng định nghĩa, rồi nối bằng owl:sameAs hoặc loại trừ." (§3.2.5)
- **Dangerous simplification:** Making identity a string-comparison problem, or resolving
  identity by trusting a single label.
- **MUST NOT infer:**
  - MUST NOT say two sources "must" be the same because their names look alike.
  - MUST NOT present owl:sameAs as the output of a mere syntactic match.
