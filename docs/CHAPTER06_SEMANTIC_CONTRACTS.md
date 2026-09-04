# Chapter 6 Semantic Contracts

Authoritative reference for every formal concept in Chapter 6. Each record specifies:

- **Source**: authoritative W3C or academic reference
- **Formal meaning**: precise definition from the source
- **Book wording**: simplified phrasing used in the manuscript
- **Dangerous simplification**: what the book wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

This document is the semantic contract against which `book/chapter06.md` is reviewed.

---

## Epistemic Model (Observation → Assertion → Claim → Evidence → Accepted Knowledge)

- **Source:** Book-defined framework (NOT a W3C standard); grounded in PROV-DM-01, WD-01, H01
- **Formal meaning:** A five-stage conceptual model for organizing epistemic concepts in knowledge graphs. Observation = raw data from the world. Assertion = graph representation of a proposition. Claim = first-class epistemic object with source, time, evidence, status. Evidence = information supporting or challenging a claim. Accepted Knowledge = claim that has passed governance review. This model is a pedagogical framework, not a normative specification.
- **Book wording:** "Quan sát → Khẳng định → Phát biểu → Bằng chứng → Tri thức được chấp nhận"
- **Dangerous simplification:** Presenting this as a W3C standard or implying it is universally adopted.
- **MUST NOT infer:**
  - MUST NOT say this model is a W3C standard.
  - MUST NOT imply all KG systems implement these stages.
  - MUST NOT conflate this model with PROV-O's Entity/Activity/Agent.

## Proposition vs Assertion vs Claim

- **Source:** Standard logic (proposition); RDF 1.1 Concepts R11-02 (assertion/triple); Book-defined (claim)
- **Formal meaning:** Proposition = abstract content P, independent of representation. Assertion = graph-level representation of P (e.g., RDF triple). Claim = first-class epistemic object containing assertion + provenance + temporal scope + evidence + governance state. Two claims C₁, C₂ may have content(C₁) = content(C₂) but remain distinct objects with independent provenance.
- **Book wording:** "Mệnh đề là nội dung trừu tượng. Khẳng định là biểu diễn trong đồ thị. Phát biểu là đối tượng tri thức luận hạng nhất."
- **Dangerous simplification:** Conflating assertion with claim; treating proposition as if it exists in the graph.
- **MUST NOT infer:**
  - MUST NOT say a triple IS a claim.
  - MUST NOT use proposition identity as claim identity.
  - MUST NOT say two claims with same content are the same claim.

## Source ≠ Evidence

- **Source:** PROV-DM-01 (wasAttributedTo vs derivation chain); WD-01 (statement vs reference)
- **Formal meaning:** Source answers "where did this claim come from?" (provenance attribution). Evidence answers "why should we believe or disbelieve this claim?" (support/challenge relation). A reliable source may produce claims with weak evidence; an unreliable source may produce claims with strong evidence. Source reliability and claim confidence are separate dimensions.
- **Book wording:** "Nguồn trả lời 'từ đâu?'; Bằng chứng trả lời 'tại sao tin?'"
- **Dangerous simplification:** Treating source as proxy for evidence; assuming reliable source → correct claim.
- **MUST NOT infer:**
  - MUST NOT equate source reliability with claim correctness.
  - MUST NOT say "source X says P" constitutes evidence for P.
  - MUST NOT collapse source and evidence into a single dimension.

## PROV-O Core Classes (Entity, Activity, Agent)

- **Source:** PROV-01 (PROV-O); PROV-DM-01
- **Formal meaning:** Entity = "a physical, digital, conceptual, or other kind of thing with some fixed aspects." Activity = "something that occurs over a period of time and acts upon or with entities." Agent = "something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity." Entity and Activity are disjoint: "An activity is not an entity." Agent is a separate concept: PROV-DM states an agent "may be a particular type of entity or activity" — Agent is NOT a universal subclass of Entity, and the three classes are NOT pairwise disjoint.
- **Book wording:** "Entity là vật có khía cạnh cố định. Activity là quá trình xảy ra trong thời gian. Agent chịu trách nhiệm."
- **Dangerous simplification:** Saying the three classes are pairwise disjoint; saying Agent is always an Entity; saying an Agent can never be an Entity.
- **MUST NOT infer:**
  - MUST NOT say an Activity is an Entity (Entity ⊥ Activity).
  - MUST NOT say Entity, Activity, and Agent are all pairwise disjoint.
  - MUST NOT say Agent is a universal subclass of Entity.
  - MUST NOT treat the three classes as fully overlapping.

## PROV-O Core Relations

- **Source:** PROV-01; PROV-DM-01
- **Formal meaning:** wasGeneratedBy(Entity, Activity): entity was produced by activity. used(Activity, Entity): activity consumed entity. wasAttributedTo(Entity, Agent): entity ascribed to agent. wasAssociatedWith(Activity, Agent): agent assigned responsibility for activity. wasDerivedFrom(Entity, Entity): entity transformed from another. wasInformedBy(Activity, Activity): activity informed by another via shared entity. All relations signify some form of influence.
- **Book wording:** See §6.4 table in manuscript.
- **Dangerous simplification:** Omitting directionality; treating wasDerivedFrom as symmetric.
- **MUST NOT infer:**
  - MUST NOT reverse relation directions.
  - MUST NOT say wasDerivedFrom implies causal necessity.
  - MUST NOT treat provenance relations as validation.

## Provenance Chain

- **Source:** PROV-DM-01
- **Formal meaning:** Provenance descriptions form directed graphs rooted at the entity whose history is described, pointing backward through generation, usage, and attribution relations to prior entities, activities, and agents. The chain enables tracing the full lineage of a knowledge artifact.
- **Book wording:** "Chuỗi provenance hình thành đồ thị có hướng ngược về quá khứ."
- **Dangerous simplification:** Saying provenance chain guarantees correctness; treating it as linear when it may branch.
- **MUST NOT infer:**
  - MUST NOT say longer provenance chain → more reliable.
  - MUST NOT say provenance chain proves truth.
  - MUST NOT assume provenance chains are always acyclic (cycles are possible in practice).

## Evidence Relations (supports, contradicts, isRelevantTo)

- **Source:** Book-defined; inspired by argumentation frameworks
- **Formal meaning:** supports(E, C): evidence E increases confidence in claim C. contradicts(E, C): evidence E decreases confidence in claim C. isRelevantTo(E, C): evidence E is contextually related to C without directly supporting or contradicting. These relations are NOT symmetric and NOT transitive. They do not constitute proof.
- **Book wording:** "Ba quan hệ bằng chứng: hỗ trợ, phản bác, liên quan."
- **Dangerous simplification:** Treating supports as proof; treating contradicts as refutation.
- **MUST NOT infer:**
  - MUST NOT say supports(E,C) means C is true.
  - MUST NOT say contradicts(E,C) means C is false.
  - MUST NOT assume transitivity of evidence relations.

## Contradiction Taxonomy (Five Types)

- **Source:** Book-defined taxonomy; grounded in temporal database theory and KG literature
- **Formal meaning:** Five types: (1) Logical contradiction: P ∧ ¬P cannot both be true in any interpretation. (2) Value conflict: different values for same property, same entity, same context. (3) Temporal disagreement: statements true at different times. (4) Scope disagreement: statements true in different scopes. (5) Source disagreement: different sources, same context. Context alignment (identity, predicate semantics, temporal scope, spatial scope) must precede contradiction declaration.
- **Book wording:** "Năm loại mâu thuẫn: logic, giá trị, thời gian, phạm vi, nguồn."
- **Dangerous simplification:** Declaring contradiction before checking context alignment.
- **MUST NOT infer:**
  - MUST NOT declare contradiction without first attempting context dissolution.
  - MUST NOT treat all disagreements as logical contradictions.
  - MUST NOT assume temporal/scope disagreements are errors.

## Context Dissolution of Apparent Contradictions

- **Source:** Book-defined; grounded in H01 (context), WD-01 (qualifiers)
- **Formal meaning:** Before declaring two statements contradictory, align four dimensions: (1) entity identity (sameAs resolution), (2) predicate semantics (same meaning?), (3) temporal scope (same valid time?), (4) spatial/jurisdictional scope (same context?). If alignment dissolves the apparent contradiction, the statements are compatible under their respective contexts. Only residual disagreement after alignment constitutes genuine contradiction.
- **Book wording:** "Trước khi tuyên bố mâu thuẫn, căn chỉnh bốn chiều ngữ cảnh."
- **Dangerous simplification:** Skipping context alignment; assuming all surface-level disagreements are contradictions.
- **MUST NOT infer:**
  - MUST NOT declare contradiction without context alignment.
  - MUST NOT assume context always dissolves contradictions.
  - MUST NOT treat context dissolution as automatic — it requires judgment.

## Multiple Temporal Clocks (Valid, Assertion, Observation, System Time)

- **Source:** OWL-TIME-01; temporal database theory (Snodgrass); bitemporal model
- **Formal meaning:** Four distinct temporal dimensions: Valid time = when statement applies to the world. Assertion time = when statement entered the system. Observation time = when data was collected from the world. System/Transaction time = when record was stored. These are NOT interchangeable. OWL-Time provides vocabulary (hasTime, Instant, Interval) but does not assign temporal semantics — that is an application convention.
- **Book wording:** "Bốn đồng hồ thời gian: hiệu lực, khẳng định, quan sát, hệ thống."
- **Dangerous simplification:** Using one clock for all purposes; conflating valid time with assertion time.
- **MUST NOT infer:**
  - MUST NOT say RDF has built-in temporal semantics.
  - MUST NOT conflate valid time with system time.
  - MUST NOT assume observation time = assertion time.

## Bitemporal Intuition (Valid Time + System Time)

- **Source:** Temporal database theory; Snodgrass bitemporal model
- **Formal meaning:** Bitemporal model uses two time dimensions: valid time (when fact is true in reality) and transaction/system time (when system recorded it). This enables queries like "what did the system believe at time T?" while maintaining accurate world-state history. Valid time may be retroactively corrected without losing the original record.
- **Book wording:** "Valid time cho biết 'đúng khi nào trong thế giới'; system time cho biết 'hệ thống biết khi nào'."
- **Dangerous simplification:** Saying bitemporal = complete temporal modeling (it omits observation and assertion time).
- **MUST NOT infer:**
  - MUST NOT say bitemporal covers all temporal needs.
  - MUST NOT confuse valid time with assertion time.
  - MUST NOT assume system time is always monotonically increasing relative to valid time.

## Claim Time ≠ Event Time

- **Source:** Book-defined; grounded in temporal database theory
- **Formal meaning:** Event time = valid time of the claim's content (when described state holds in world). Claim time = assertion time (when claim entered system). These are independent: a claim about 1976 may be asserted in 2024; a claim asserted today may describe future events. Confusing them leads to incorrect temporal queries.
- **Book wording:** "Thời gian sự kiện là valid time của nội dung. Thời gian phát biểu là assertion time."
- **Dangerous simplification:** Using assertion time as proxy for valid time.
- **MUST NOT infer:**
  - MUST NOT use claim insertion date as valid time.
  - MUST NOT assume recently asserted claims describe current state.
  - MUST NOT sort claims by assertion time when querying by valid time.

## Wikidata Statement Model

- **Source:** WD-01; WD-02
- **Formal meaning:** Statement = property-value pair about an item + qualifiers + references + rank. Claim = statement core without references/ranks. Snak = claim without qualifiers. Rank (preferred/normal/deprecated) manages competing values without deletion. References record sources, not proof. Qualifiers contextualize beyond bare property-value. A statement should remain useful without its qualifiers.
- **Book wording:** See §6.9 in manuscript.
- **Dangerous simplification:** Treating rank as truth score; treating reference as proof.
- **MUST NOT infer:**
  - MUST NOT say preferred rank = true.
  - MUST NOT say deprecated rank = false.
  - MUST NOT say presence of reference guarantees correctness.
  - MUST NOT treat qualifiers as required for statement validity.

## Confidence Semantics

- **Source:** Book-defined; grounded in information quality literature
- **Formal meaning:** Confidence must specify WHAT is being assessed: extraction confidence, source reliability, evidence assessment, temporal validity, or composite. No universal formula exists for composite confidence. Source reliability ≠ claim confidence. Confidence is subjective and policy-dependent, not an objective probability unless explicitly defined as such.
- **Book wording:** "Confidence phải nói rõ đang đánh giá gì."
- **Dangerous simplification:** Using unqualified "confidence = 0.8"; treating confidence as objective probability.
- **MUST NOT infer:**
  - MUST NOT use confidence without specifying type.
  - MUST NOT equate confidence with probability of truth.
  - MUST NOT assume high source reliability → high claim confidence.

## Governance States (Candidate, Accepted, Rejected, Contested, Superseded)

- **Source:** Book-defined; inspired by Wikidata ranks, scientific publication lifecycle
- **Formal meaning:** Five states governing claim lifecycle. Candidate = proposed, unevaluated. Accepted = evaluated, currently most reliable. Rejected = evaluated, refused. Contested = challenged by new evidence. Superseded = replaced by better claim. Accepted ≠ eternal truth. Rejected ≠ deleted. State transitions are governed by system-specific policies.
- **Book wording:** "Năm trạng thái: Candidate, Accepted, Rejected, Contested, Superseded."
- **Dangerous simplification:** Treating Accepted as permanent truth; deleting Rejected claims.
- **MUST NOT infer:**
  - MUST NOT say Accepted means always true.
  - MUST NOT delete Rejected claims from the graph.
  - MUST NOT assume state transitions are automatic.

## Supersession vs Contradiction

- **Source:** Book-defined
- **Formal meaning:** Supersession = new claim replaces old because it is better (newer, more detailed, stronger evidence). Old claim is not necessarily wrong. Contradiction = two claims cannot both be true in same context. At least one is wrong. Supersession → mark old as Superseded. Contradiction → mark as Contested, investigate.
- **Book wording:** "Thay thế = tốt hơn. Mâu thuẫn = ít nhất một bên sai."
- **Dangerous simplification:** Treating all replacements as supersession; treating all disagreements as contradiction.
- **MUST NOT infer:**
  - MUST NOT assume newer claim is always correct.
  - MUST NOT auto-supersede without evaluation.
  - MUST NOT treat supersession as refutation.

## Evidence Graph

- **Source:** Book-defined; inspired by argumentation frameworks
- **Formal meaning:** Directed graph where nodes are Claims and Evidence (may overlap), edges are supports/contradicts/isRelevantTo relations. Parallel to data graph. Provides evaluation layer. Does not automatically resolve contradictions.
- **Book wording:** "Đồ thị bằng chứng liên kết phát biểu qua quan hệ hỗ trợ/phản bác/liên quan."
- **Dangerous simplification:** Treating evidence graph as automatic truth determination.
- **MUST NOT infer:**
  - MUST NOT say more supporting edges → true.
  - MUST NOT treat evidence graph as decision procedure.
  - MUST NOT assume evidence graph is acyclic.

## Contradiction Preservation

- **Source:** Book-defined; grounded in paraconsistent approaches
- **Formal meaning:** System does not delete contradictions. Instead: (1) record contradiction explicitly (contradicts relation), (2) classify type (§6.6), (3) attach reconciling context if possible, (4) flag as Contested if irreconcilable. Preservation enables audit, re-evaluation, and multi-perspective queries.
- **Book wording:** "Hệ thống không xóa mâu thuẫn; nó bảo tồn và phân loại."
- **Dangerous simplification:** Deleting contradictions to maintain "clean" data.
- **MUST NOT infer:**
  - MUST NOT delete contradictory claims.
  - MUST NOT assume preservation means acceptance of both sides.
  - MUST NOT treat contradiction preservation as endorsement.

## Claim Identity vs Content Identity

- **Source:** Book-defined; grounded in reification semantics (H01, NARY-01)
- **Formal meaning:** Claim identity = unique IRI of claim object. Content identity = proposition/assertion content. C₁ ≠ C₂ even when content(C₁) = content(C₂). Separate identities enable independent provenance, evidence, and governance per claim. Using content as claim identity collapses distinct epistemic objects.
- **Book wording:** "Định danh phát biểu khác định danh nội dung."
- **Dangerous simplification:** Using content hash as claim ID; merging claims with same content.
- **MUST NOT infer:**
  - MUST NOT merge claims solely based on content equality.
  - MUST NOT use proposition identity as claim identity.
  - MUST NOT assume same content → same provenance.

## Negation vs Absence (OWA Applied to Claims)

- **Source:** OWA from Ch4 (§4.8); Book-defined extension to epistemic layer
- **Formal meaning:** Claim(¬P) = explicit negation claim exists. No Claim(P) = epistemic absence — system has not considered P. Under OWA: absence of Claim(P) ≠ Claim(¬P). No evidence supporting P ≠ evidence contradicting P. Three epistemic states: Accepted(P), Rejected(P), Unknown(P).
- **Book wording:** "Phủ định là Claim(¬P). Vắng mặt là không có Claim(P)."
- **Dangerous simplification:** Treating absence as negation (CWA); treating unknown as false.
- **MUST NOT infer:**
  - MUST NOT infer ¬P from absence of Claim(P).
  - MUST NOT treat missing claims as rejected claims.
  - MUST NOT apply CWA reasoning to epistemic layer.

## Contradiction vs Inconsistency

- **Source:** Standard logic; Ch4 consistency definition; Book-defined distinction
- **Formal meaning:** Contradiction = two statements cannot both be true (property of content). Inconsistency = system contains P ∧ ¬P in same logical context, making no interpretation satisfy both (property of system). When contradictory claims are contextualized as separate claim objects with distinct sources/times/scopes, the system remains logically consistent — no interpretation forces both claims true simultaneously.
- **Book wording:** "Mâu thuẫn ở nội dung; nhất quán ở metadata."
- **Dangerous simplification:** Saying contradictory data makes system inconsistent.
- **MUST NOT infer:**
  - MUST NOT say two disagreeing sources → system inconsistency.
  - MUST NOT require deletion of contradictions to maintain consistency.
  - MUST NOT confuse content-level contradiction with system-level inconsistency.

## LLM Output as CandidateKnowledge

- **Source:** Book-defined; grounded in AI safety principles
- **Formal meaning:** LLM-generated statements receive governance state Candidate. LLM is recorded as Agent in PROV-O provenance. LLM output cannot serve as its own verification evidence (circular verification). Independent external evidence required for promotion to Accepted. Self-verification by same LLM does not constitute independent evidence.
- **Book wording:** "Đầu ra LLM là CandidateKnowledge — cần bằng chứng độc lập."
- **Dangerous simplification:** Treating LLM output as verified knowledge; using same LLM for self-verification.
- **MUST NOT infer:**
  - MUST NOT promote LLM output to Accepted without independent evidence.
  - MUST NOT treat LLM confidence scores as claim confidence.
  - MUST NOT use same-model verification as evidence.

## Claim Ledger / Epistemic Layer Architecture

- **Source:** Book-defined architecture
- **Formal meaning:** Three-layer architecture: Data Graph (entities, relations) → Epistemic Layer (claims, evidence, provenance, time) → Governance Layer (status, confidence, review decisions). Claim Ledger = set of all Claim objects in the graph, queryable via SPARQL. Not a separate data structure — integrated into the same RDF graph.
- **Book wording:** "Ba tầng: Dữ liệu → Tri thức luận → Quản trị."
- **Dangerous simplification:** Treating layers as physically separate databases.
- **MUST NOT infer:**
  - MUST NOT require separate storage for epistemic metadata.
  - MUST NOT treat governance layer as optional for production systems.
  - MUST NOT assume layer boundaries are rigid — they are conceptual.

## Bitemporal 2D Coordinate Grid (Rectangle + Point-Probe)

- **Source:** SNODGRASS-01 (Developing Time-Oriented Database Applications in SQL, Snodgrass 1999)
- **Formal meaning:** A bitemporal record occupies a rectangle R = [Tv_start, Tv_end] × [Ttx_start, Ttx_end] in the 2D plane whose horizontal axis is valid time and whose vertical axis is transaction/system time. A point-probe query (Tv*, Ttx*) asks "at system time Ttx*, what did the system believe about validity interval Tv*?" and is answered by the rectangle containing that point: Tv_start ≤ Tv* < Tv_end and Ttx_start ≤ Ttx* < Ttx_end. When a correction arrives, the old rectangle is not deleted — its transaction interval is closed and a new rectangle is appended (append-only). Different system-time slices may therefore give different answers for the same valid-time year, and this reflects belief history, not contradiction.
- **Book wording:** "Mỗi bản ghi chiếm một hình chữ nhật R trong lưới 2D; một point-probe (Tv*, Ttx*) rơi vào ô nào thì nhận ô đó."
- **Dangerous simplification:** Reducing bitemporal to two timestamp columns (loses the interval/rectangle semantics and the valid-time retrospection); conflating a corrected retrospective value with a contradiction.
- **MUST NOT infer:**
  - MUST NOT say bitemporal means merely "two timestamp columns".
  - MUST NOT say deleting/updating the old record is an acceptable correction strategy (append-only principle).
  - MUST NOT treat two answers for the same valid-time year at different system times as a contradiction — it is belief history.
  - MUST NOT apply the probe inequalities at open boundaries without the half-open convention.

## Dempster–Shafer Theory of Evidence

- **Source:** SHAFER-01 (A Mathematical Theory of Evidence, Shafer 1976)
- **Formal meaning:** Generalizes Bayesian probability by assigning mass m : 2^Θ → [0,1] to subsets of a frame of discernment Θ (a set of mutually exclusive hypotheses), with m(∅) = 0 and Σ_{B⊆Θ} m(B) = 1. Mass on Θ as a whole expresses total ignorance (m(Θ)=1), distinct from a 0.5 singleton. The belief and plausibility functions Bel(A) = Σ_{B⊆A} m(B) and Pl(A) = 1 − Bel(Ā) bracket a claim into an interval [Bel, Pl]; its width is the uncommitted ignorance. Dempster's rule of combination (m₁⊕m₂)(A) = (1/(1−K)) Σ_{B∩C=A} m₁(B)m₂(C) merges independent sources, where K = Σ_{B∩C=∅} m₁(B)m₂(C) measures conflict. As K → 1 the normalization 1/(1−K) becomes numerically arbitrary (Zadeh's paradox).
- **Book wording:** "Gán khối lượng cho các tập trong khung phân biệt; Bel/Pl kẹp claim vào một khoảng; quy tắc Dempster chuẩn hóa qua 1−K."
- **Dangerous simplification:** Applying Dempster's rule to highly conflicting sources and reading the normalized result as a confident conclusion; presenting [Bel, Pl] as a single point probability.
- **MUST NOT infer:**
  - MUST NOT use Dempster's rule when conflict K is large — the book keeps conflicting branches separate (Claim Ledger, state Contested).
  - MUST NOT equate a wide [Bel, Pl] interval with a mid-point probability.
  - MUST NOT claim Dempster–Shafer is a drop-in replacement for Bayesian probability — it is a generalization that represents ignorance explicitly.

## Subjective Logic (Opinions, Simplex, Fusion)

- **Source:** JOSANG-01 (Subjective Logic, Jøsang 2016)
- **Formal meaning:** An opinion is a quadruple ω = (b, d, u, a) with belief, disbelief, uncertainty and base rate; b + d + u = 1. Because of the constraint, an opinion lives on an equilateral 2-simplex (barycentric coordinates) with vertices Belief–Disbelief–Uncertainty. The reference (subjective) probability is P(x) = b + a·u. Cumulative fusion ⊕ of two independent opinions (same a) is b⊕ = (b₁u₂ + b₂u₁)/(u₁+u₂−u₁u₂), d⊕ = (d₁u₂ + d₂u₁)/(u₁+u₂−u₁u₂), u⊕ = (u₁u₂)/(u₁+u₂−u₁u₂). Key property: when sources agree, uncertainty shrinks monotonically, u⊕ ≤ min(u₁, u₂). Subjective Logic is numerically equivalent to Dempster–Shafer but geometrically transparent.
- **Book wording:** "Opinion ω=(b,d,u,a) sống trên tam giác đều; xác suất chủ quan P=b+a·u; kết hợp ⊕ làm vô tri co hẹp khi đồng thuận."
- **Dangerous simplification:** Reading fusion as a guarantee of certainty; collapsing opinion into a single scalar and losing the b/d/u breakdown.
- **MUST NOT infer:**
  - MUST NOT say fusion always reduces uncertainty — only when sources are consistent; conflicting opinions keep b and d both substantial.
  - MUST NOT equate subjective probability with objective probability.
  - MUST NOT ignore the base rate a when computing P(x).

## AGM Belief Revision (Expansion, Contraction, Revision)

- **Source:** AGM-01 (On the Logic of Theory Change, Alchourrón, Gärdenfors & Makinson 1985)
- **Formal meaning:** AGM formalizes rational change of a belief set K (closed under logical consequence). Expansion K+φ adds φ and closes under logic (does not self-heal contradiction). Contraction K÷φ removes φ while keeping logical closure and losing as little information as possible. Revision K*φ accepts φ even if it contradicts K, giving up the minimal set of old beliefs. Two identities link the operations: Levi K*φ = (K÷¬φ)+φ and Harper K÷φ = K ∩ (K*¬φ). Six postulates govern revision (success, inclusion, vacuity, consistency, extensionality, super-/sub-expansion), capturing the minimal-information-loss principle.
- **Book wording:** "Ba phép: mở rộng K+φ, co rút K÷φ, sửa đổi K*φ; nối bằng đẳng thức Levi/Harper; 6 tiên đề tối thiểu."
- **Dangerous simplification:** Presenting AGM as an algorithm (it is a set of rationality constraints, not a unique procedure); claiming revision always has a unique result (selection functions may differ).
- **MUST NOT infer:**
  - MUST NOT say AGM prescribes a unique revision operator — it specifies rationality postulates that many operators satisfy.
  - MUST NOT apply expansion K+φ when ¬φ ∈ K and expect consistency (expansion becomes trivial).
  - MUST NOT conflate contraction with deletion of a single sentence — it removes the logical consequences needed to drop φ.

## Claim Ledger as Lossless Projection Satisfying AGM

- **Source:** Book-defined bridge between AGM-01 and the Claim Ledger architecture (PROV-DM-01, SNODGRASS-01)
- **Formal meaning:** Classical AGM is destructive: K*φ replaces K, and the old belief set is discarded (only an abstract entrenchment ordering survives). The book's Claim Ledger reverses this: the raw graph G_raw only appends claims forever, and the "active belief set" at system time t_tx is a projection K_active(t_tx) = Π_active(G_raw, t_tx). AGM revision happens in the projection layer — Π_active "contracts" a claim by closing its system-time interval rather than deleting it. Each t_tx slice of the projection satisfies the AGM postulates (consistency, minimality), but G_raw itself keeps the whole history for retrospective point-probing. This is the "lossless epistemic projection": AGM-rational belief change at the view layer combined with full audit history at the raw layer.
- **Book wording:** "Sửa đổi AGM diễn ra trong lớp chiếu Π_active, không trong kho thô G_raw — mỗi lát cắt t_tx thỏa mãn AGM, lịch sử nguyên vẹn."
- **Dangerous simplification:** Claiming the Claim Ledger literally IS an AGM belief set (it is not — it is an append-only store plus a family of projections); saying projection preserves contradictions (it does not — projection filters by Accepted + valid time).
- **MUST NOT infer:**
  - MUST NOT say the Claim Ledger is a single AGM belief set — it is G_raw + Π_active.
  - MUST NOT say AGM revision in the book deletes claims from G_raw — revision is confined to the projection.
  - MUST NOT assume every projection policy yields an AGM-rational slice — only policies respecting consistency and minimality do.
  - MUST NOT conflate the lossless raw layer with the canonical view (I30: storing a claim ≠ asserting it).