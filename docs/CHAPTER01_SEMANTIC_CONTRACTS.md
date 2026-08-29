# Chapter 1 — Semantic Contracts

Authoritative reference for every formal concept in Chapter 1. Each record specifies:

- **Source**: authoritative W3C, academic, or book-defined reference
- **Formal meaning**: precise definition from the source
- **Book wording**: simplified phrasing used in the manuscript
- **Dangerous simplification**: what the book wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

This document is the semantic contract against which `book/chapter01.md` is reviewed.

---

## Graph as a Data Structure

- **Source:** Standard graph theory; R11-02 (RDF 1.1 Concepts §3)
- **Formal meaning:** A graph G = (V, E) consists of vertices V and edges E, where each
  edge is an ordered pair (u, v) for a directed graph. A labeled graph attaches labels to
  nodes and/or edges. A triple is one concrete encoding of a directed labeled edge.
- **Book wording:** "Đồ thị là G = (V, E): đỉnh và cạnh; cạnh có hướng khi là cặp có thứ tự."
- **Dangerous simplification:** Equating "has structure" with "has knowledge" — a graph
  being connected does not make its content true or meaningful.
- **MUST NOT infer:**
  - MUST NOT say a graph with edges is a knowledge graph.
  - MUST NOT say graph structure alone determines meaning.

## Triple (Subject, Predicate, Object)

- **Source:** R11-02 (RDF 1.1 Concepts §3)
- **Formal meaning:** A triple is an ordered tuple (s, p, o). Position constraints:
  subject ∈ IRI ∪ BlankNode; predicate ∈ IRI; object ∈ IRI ∪ BlankNode ∪ Literal.
  Predicates (properties) must be IRIs; literals may appear only in object position.
- **Book wording:** "Bộ ba (subject, predicate, object) là đơn vị cơ bản biểu diễn một
  cạnh có hướng có nhãn."
- **Dangerous simplification:** Treating a triple as a free-form sentence; forgetting the
  predicate-position constraint (a literal cannot be a predicate).
- **MUST NOT infer:**
  - MUST NOT show literals in subject or predicate position as valid RDF.
  - MUST NOT present a triple where the predicate is a blank node or literal.

## Entity / Relation / Property

- **Source:** R11-02; book-defined engineering vocabulary
- **Formal meaning:** An entity is a thing denoted by a resource; a relation connects two
  entities; a property is an attribute (often modeled as a datatype-property-like
  predicate in RDF, distinguished by object being a literal). The book uses these as
  informal domain terms, not as formal OWL constructs at Chapter 1 depth.
- **Book wording:** "Thực thể là đối tượng; quan hệ nối hai thực thể; thuộc tính gắn giá
  trị cho thực thể."
- **Dangerous simplification:** Treating property and relation as synonyms when RDF
  distinguishes them only by object type (literal vs. resource).
- **MUST NOT infer:**
  - MUST NOT claim property and relation are interchangeable RDF terms.
  - MUST NOT present entity/relation/property as formal OWL terminology in Ch1.

## Data Graph + Semantics + Context (book engineering model)

- **Source:** Book-defined learning model (not a W3C standard)
- **Formal meaning:** The book's three-layer model: Data Graph (entities, relations,
  labels — no formal semantics), Semantics (schema/ontology giving machine-readable
  meaning), Context (provenance, time, scope, confidence attached to statements). This is
  a pedagogical lens for understanding knowledge graphs, not a formal W3C definition.
- **Book wording:** "Knowledge Graph = Data Graph + Semantics + Context."
- **Dangerous simplification:** Students concluding this is the official academic/W3C
  definition of knowledge graph — many definitions exist in research; this is the book's
  engineering model.
- **MUST NOT infer:**
  - MUST NOT attribute this three-layer equation verbatim to a W3C Recommendation.
  - MUST NOT claim all knowledge graphs necessarily have all three layers materialized.

## Mechanism (book-defined domain class)

- **Source:** Book-defined; canonical model — docs/MECHANISM_KG_CANONICAL_MODEL.md
- **Formal meaning:** A Mechanism is a transform/process that takes inputs and produces an
  output under conditions, e.g., rate of change. In the capstone, ex:Mechanism is the root
  of the mechanism taxonomy; RateOfChangeMechanism ⊑ ChangeMechanism ⊑ Mechanism.
- **Book wording:** "Cơ chế là quá trình biến đổi: nhận đầu vào, sinh đầu ra trong điều
  kiện (condition)."
- **Dangerous simplification:** Using "mechanism" loosely to mean any process, blurring the
  input–operation–output–condition signature that the capstone relies on.
- **MUST NOT infer:**
  - MUST NOT treat mechanism as a synonym for "algorithm" or "function" without the
    operation/quantity/reference-variable vocabulary.
  - MUST NOT introduce a new mechanism instance that contradicts the canonical individuals
    (ex:rateOfChange_1, ex:heatTransferRate_2, ex:newtonCooling_1).

## Operation / Quantity / ReferenceVariable

- **Source:** Book-defined; canonical model
- **Formal meaning:** Operation is the basic transform a mechanism performs (e.g.,
  derivative); Quantity is a measurable input/output of a mechanism; ReferenceVariable is
  the independent variable with respect to which the rate is taken. These are the
  structural parts a MechanismApplication binds together.
- **Book wording:** "Phép toán là phép biến đổi cơ sở; đại lượng là đầu vào/đầu ra đo
  được; biến tham chiếu là biến độc lập để lấy tốc độ."
- **Dangerous simplification:** Collapsing operation into mechanism, or quantity into
  variable — the chapter must keep them distinct because the capstone models each role.
- **MUST NOT infer:**
  - MUST NOT say an Operation is itself a Mechanism (it is a component, not the process).
  - MUST NOT say a ReferenceVariable is a Quantity (they occupy different roles in the
    rate-of-change signature).

## DerivativeApplication (n-ary preview)

- **Source:** NARY-01 (n-ary relations pattern) applied to the capstone; canonical model
- **Formal meaning:** ex:derivativeApplication_1 is a mechanism application binding
  ex:rateOfChange_1 (mechanism) with ex:position_1 (quantity being derived), ex:time_1
  (reference variable), ex:velocity_1 (derived quantity). Reifying the two-place connection
  "mechanism applies to quantity" into a node permits attaching context. Full n-ary formal
  treatment is Chapter 3 (§3.3.3); Chapter 1 previews the object only.
- **Book wording:** "Đối tượng trung gian ràng buộc cơ chế, đại lượng được đạo hàm, biến
  tham chiếu."
- **Dangerous simplification:** Presenting the application as an ordinary two-place edge —
  Chapter 1 must keep it as a staged object so Chapter 3's n-ary reification is a
  continuation, not a contradiction.
- **MUST NOT infer:**
  - MUST NOT claim DerivativeApplication is modeled as a reification in Ch1 (it is previewed;
    the n-ary pattern is formalized in Ch3).
  - MUST NOT omit that the object exists specifically to attach source/time/confidence.

## Assertion ≠ Accepted Knowledge

- **Source:** Book-defined epistemic boundary (expanded in Ch6)
- **Formal meaning:** A triple asserted in the graph is a data statement, not an accepted
  truth. "A says B" ≠ "B is true." Epistemic status (Candidate/Accepted/…) is a Ch6
  concept; Ch1 must plant the distinction without teaching the full lifecycle.
- **Book wording:** "Khi Textbook B khẳng định một bộ ba về rateOfChange_1, đó là khẳng
  định, chưa là tri thức được chấp nhận."
- **Dangerous simplification:** Writing mechanism triples as if existing in the graph made
  them true.
- **MUST NOT infer:**
  - MUST NOT say an asserted triple is automatically true.
  - MUST NOT use governance vocabulary (Accepted/Rejected/Contested/Superseded) before Ch6
    without marking it as a forward reference.
