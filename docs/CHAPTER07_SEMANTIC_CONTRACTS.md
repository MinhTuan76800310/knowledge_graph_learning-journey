# Chapter 7 Semantic Contracts

Authoritative reference for every formal concept in Chapter 7. Each record specifies:

- **Source**: authoritative W3C or academic reference
- **Formal meaning**: precise definition from the source
- **Book wording**: simplified phrasing used in the manuscript
- **Dangerous simplification**: what the book wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

This document is the semantic contract against which `book/chapter07.md` is reviewed.
Concepts marked **BOOK-DEFINED** are the book's own pedagogical framework, not W3C or
academic standards; they are labeled explicitly in the manuscript.

---

## Acquisition vs Integration (pipeline split)

- **Source:** DI-01 (integration as mapping+query answer), HOGAN-CREATE-01 (creation & enrichment), BOOK-DEFINED split
- **Formal meaning:** Data integration formalizes reconciling heterogeneous sources under one global schema (G, S, M) with query answering over G [DI-01]. Knowledge *acquisition* brings information from sources into the system as candidate knowledge; knowledge *integration* reconciles, validates, and commits candidate knowledge into the Claim Ledger. The split is a book-level architectural discipline, not a standard.
- **Book wording:** "Thu nhận mang thông tin vào hệ thống; tích hợp đối chiếu, xác nhận và đưa vào sổ phát biểu."
- **Dangerous simplification:** Implying the split is a normative standard; implying the boundary is crisp for all systems.
- **MUST NOT infer:**
  - MUST NOT say the acquisition/integration boundary is a W3C or ISO standard.
  - MUST NOT say acquisition alone produces accepted knowledge.
  - MUST NOT say integration can fix facts that were never acquired.

## Knowledge Acquisition

- **Source:** HOGAN-CREATE-01 (creation/enrichment as a KG-building stage); BOOK-DEFINED
- **Formal meaning:** The stage that converts source content (documents, databases, APIs) into structured candidate knowledge inside the system, with provenance to the source fragment. It answers "bring information in." Acquisition is not yet integration: no identity resolution, no conflict handling, no commitment to the ledger.
- **Book wording:** "Thu nhận = biến nội dung nguồn thành tri thức ứng viên có provenance."
- **Dangerous simplification:** Treating extraction output as accepted knowledge; skipping provenance during acquisition.
- **MUST NOT infer:**
  - MUST NOT say acquired candidate knowledge is accepted knowledge.
  - MUST NOT say acquisition preserves the source's implicit trustworthiness.
  - MUST NOT say a system can acquire without provenance.

## Knowledge Integration

- **Source:** DI-01 (global schema + mapping reconciliation); BOOK-DEFINED
- **Formal meaning:** The stage that takes candidate knowledge from multiple acquisitions, resolves identity (which things are the same), aligns schemas (which properties line up), detects duplication and conflict, and commits the reconciled result into the Claim Ledger. It answers "put information together coherently."
- **Book wording:** "Tích hợp = hợp nhất, đối chiếu và kiểm soát xung đột trước khi ghi sổ."
- **Dangerous simplification:** Presenting integration as a mechanical merge; implying homogeneity of sources (DI-01 emphasizes heterogeneity as the hard case).
- **MUST NOT infer:**
  - MUST NOT say integration is a solved/automatic problem.
  - MUST NOT say integration removes the need for identity resolution.
  - MUST NOT say integration outputs are automatically true.

## Source Artifact

- **Source:** PROV-01 (Entity); BOOK-DEFINED registration concept
- **Formal meaning:** A registered, addressable container of information that the system will acquire from — a document, database, API, or dataset — identified by an IRI, with metadata (type, creator, registration time, version, trust profile). The Source Artifact is the *system's record* of the source, distinct from the physical source itself.
- **Book wording:** "Source Artifact là bản ghi đăng ký nguồn, có IRI riêng và siêu dữ liệu."
- **Dangerous simplification:** Equating the Source Artifact with the physical source; skipping registration metadata.
- **MUST NOT infer:**
  - MUST NOT say the Source Artifact IS the real-world source.
  - MUST NOT say registration implies reliability.
  - MUST NOT say every pipeline shares the same source ontology (registration scheme is book-defined).

## Source Fragment

- **Source:** PROV-DM-01 (entity granularity); BOOK-DEFINED
- **Formal meaning:** A delimited, addressable portion of a Source Artifact (a page, a section, a table, an API response) from which observations are extracted. Fragment-level provenance is finer than artifact-level provenance: a claim traces to the exact fragment that supports it, not just the whole source.
- **Book wording:** "Source Fragment là phần con được đánh địa chỉ của nguồn."
- **Dangerous simplification:** Using whole-source provenance when fragment provenance is available.
- **MUST NOT infer:**
  - MUST NOT say a claim's provenance is satisfied by naming the whole book/document when the specific fragment differs.
  - MUST NOT say fragments have meaning without their parent artifact.

## Observation (into the pipeline)

- **Source:** PROV-DM-01 (Entity/Activity used-for-generation); BOOK-DEFINED (Ch6 model continued)
- **Formal meaning:** The raw data item captured from a source fragment during acquisition — e.g., "the textbook §3.2 sentence: 'the derivative of x² is 2x'". An Observation anchors provenance: it records what was seen, where, and when, before any interpretation is layered on.
- **Book wording:** "Observation là dữ liệu thô được thu từ một mẩu nguồn."
- **Dangerous simplification:** Conflating observation with the interpreted claim derived from it.
- **MUST NOT infer:**
  - MUST NOT say an observation is already a claim or a fact.
  - MUST NOT say the observation equals the source's intended meaning.
  - MUST NOT discard the observation while keeping only its extraction.

## Extraction

- **Source:** HOGAN-CREATE-01 (creation from data/text); BOOK-DEFINED stage
- **Formal meaning:** The activity of turning an Observation (raw content) into candidate structured knowledge: identifying entities, relations, and properties and producing an intermediate structured record (e.g., `{subject: "x²", relation: "derivative of", object: "2x", context: ...}`). Extraction is content-specific: it depends on the source type and the extraction pattern used.
- **Book wording:** "Trích xuất là bước biến nội dung thô thành bản ghi có cấu trúc ứng viên."
- **Dangerous simplification:** Presenting extraction as error-free transcription; hiding the extraction pattern.
- **MUST NOT infer:**
  - MUST NOT say extraction output is ground truth.
  - MUST NOT say extraction preserves all source nuance/ambiguity.
  - MUST NOT say a single extractor works for all source types.

## Extraction Activity

- **Source:** PROV-01 (Activity); BOOK-DEFINED binding
- **Formal meaning:** A PROV Activity that performed the Extraction, recorded with a start/end time, an agent (system or tool version), and the used Observations. Every extracted record is `wasGeneratedBy` an Extraction Activity, giving the pipeline a time-stamped breadcrumb.
- **Book wording:** "Extraction Activity là Activity PROV ghi lại việc thực thi trích xuất."
- **Dangerous simplification:** Omitting the activity node and linking records directly to sources.
- **MUST NOT infer:**
  - MUST NOT say an extraction activity implies extraction correctness.
  - MUST NOT conflate extraction activity time with the claim's valid time.

## Extraction Confidence

- **Source:** HOGAN-CREATE-01 (quality of extraction); Ch6 confidence multi-dimensionality; BOOK-DEFINED
- **Formal meaning:** A per-record assessment of how reliable the extraction is, given the extraction method and the source content (e.g., letter-regular expression for a formula vs. free-text relation extraction). It is evidence *about the extraction*, not evidence about the truth of the extracted content.
- **Book wording:** "Độ tin cậy trích xuất nói về chất lượng trích xuất, không nói về tính đúng của nội dung."
- **Dangerous simplification:** Using extraction confidence as claim confidence.
- **MUST NOT infer:**
  - MUST NOT say high extraction confidence → the claimed fact is true.
  - MUST NOT say extraction confidence subsumes governance.
  - MUST NOT treat extraction confidence as a normalized probability of truth.

## Normalization

- **Source:** R2RML-01 / DIRECT-MAP-01 / CSVW-01 (value typing and mapping); BOOK-DEFINED
- **Formal meaning:** Converting extracted values into canonical, comparable forms: unit conversion (m/s vs km/h), date formats (day/month/year), number representations, string case. Normalization makes later identity comparison and typed storage meaningful.
- **Book wording:** "Chuẩn hóa đưa giá trị về dạng chung để so sánh được."
- **Dangerous simplification:** Applying normalization silently (losing the raw value's provenance).
- **MUST NOT infer:**
  - MUST NOT say normalization is lossless.
  - MUST NOT say normalized values are the source's own representation.
  - MUST NOT drop the original value without keeping the normalized version's derivation.

## Structuring

- **Source:** R2RML-01 (triples), CSVW-01 (annotations), BOOK-DEFINED
- **Formal meaning:** The step that produces graph statements (RDF triples / Turtle) from normalized records, applying a target schema: choosing IRIs for subjects, predicates, and typed objects. Structuring is where raw facts become *graph-shaped candidate knowledge*.
- **Book wording:** "Cấu trúc hóa biến bản ghi chuẩn hóa thành các câu RDF theo lược đồ đích."
- **Dangerous simplification:** Pretending the target schema is the only possible shape.
- **MUST NOT infer:**
  - MUST NOT say structured triples are automatically well-typed.
  - MUST NOT say the structuring schema is source-derived.

## CandidateGeneration

- **Source:** RL-01 (candidate generation stage of record linkage); BOOK-DEFINED
- **Formal meaning:** The stage that proposes pairs (or groups) of candidate records that *might* denote the same thing, using cheap, coarse keys (e.g., same normalized name, same timestamp window). It must be *recall-oriented*: miss few true matches, at the cost of including many non-matches.
- **Book wording:** "Sinh ứng viên ưu tiên độ bao phủ: gom mọi cặp có khả năng trùng."
- **Dangerous simplification:** Treating candidate generation as identity resolution itself.
- **MUST NOT infer:**
  - MUST NOT say candidate pairs are same; they are only candidates.
  - MUST NOT say candidate generation decides identity.

## Blocking

- **Source:** RL-01 (practical record linkage avoids the O(n²) pair space); HOGAN-CREATE-01; BOOK-DEFINED term
- **Formal meaning:** Grouping records into blocks by a blocking key (e.g., first letter of normalized surname, same property `ex:hasDerivativeOf`), so comparisons only happen within a block. Blocking trades completeness of candidate generation for tractability.
- **Book wording:** "Blocking chia tập bản ghi thành khối để không so sánh toàn bộ cặp."
- **Dangerous simplification:** Using a blocking key that splits true matches across blocks (recall loss).
- **MUST NOT infer:**
  - MUST NOT say blocking preserves all true pairs.
  - MUST NOT say blocking assigns identity.

## Candidate Matching (comparison)

- **Source:** RL-01 (comparison vector γ)
- **Formal meaning:** For each candidate pair, compute a comparison vector γ whose components record agreements/disagreements on each attribute (e.g., names agree, timestamps agree, synonyms disagree). The vector is the evidence input to the linkage decision.
- **Book wording:** "Véc-tơ so sánh γ ghi từng khớp/không khớp giữa hai bản ghi."
- **Dangerous simplification:** Reducing matching to a single similarity number without showing which attributes agreed.
- **MUST NOT infer:**
  - MUST NOT say a comparison vector is a truth judgment.
  - MUST NOT say agreement on one attribute suffices.

## Record Linkage (identity decision)

- **Source:** RL-01 (Fellegi–Sunter)
- **Formal meaning:** The probabilistic model of deciding whether two records refer to the same entity. Let m(γ) be the probability of observing γ among truly matching pairs and u(γ) among truly non-matching pairs; the linkage weight is the likelihood ratio m(γ)/u(γ); two thresholds split pairs into linked (match), possible (clerical review), and non-linked (non-match). The model is optimal when comparison attributes are conditionally independent.
- **Book wording:** "Tỷ lệ hợp lý m/u quyết định khớp, hai ngưỡng chia thành: khớp / xem xét / không khớp."
- **Dangerous simplification:** Teaching only the thresholds while dropping that m(γ) and u(γ) must be estimated from data (often by an unsupervised EM approach or labeled data).
- **MUST NOT infer:**
  - MUST NOT say a pair above the upper threshold is a *fact* of identity; it is a decision with a residual error rate.
  - MUST NOT present Fellegi–Sunter as the only linkage method (modern: embedding-, ML-, graph-based).
  - MUST NOT say the model is exact when independence fails.

## Entity Resolution (overview)

- **Source:** RL-01; HOGAN-CREATE-01; BOOK-DEFINED scope
- **Formal meaning:** The end-to-end process of determining which records/mentions across (or within) sources refer to the same real-world entity: candidate generation → comparison → decision → merge/link. Record linkage is its quantitative core; entity resolution additionally covers the merge/annotation of resolved entities.
- **Book wording:** "Giải quyết định danh là toàn bộ quá trình quy hai bản ghi về cùng một thực thể."
- **Dangerous simplification:** Using "entity resolution" and "deduplication" interchangeably.
- **MUST NOT infer:**
  - MUST NOT say entity resolution decides truth, only identity.
  - MUST NOT say resolution is idempotent by default (must be designed to be).

## Schema Alignment (schema matching)

- **Source:** SM-01 (Rahm–Bernstein)
- **Formal meaning:** Identifying semantic correspondences between schema elements of two schemas — e.g., `textbookA:velocity` ↔ `textbookB:van toc` ↔ canonical `ex:velocity`. Matching operates at element level (single attributes) or structure level (combinations); uses schema-level information (names, types, constraints), instance-level (data values), or hybrids.
- **Book wording:** "Đối chiếu lược đồ tìm quan hệ ngữ nghĩa giữa các thành phần lược đồ."
- **Dangerous simplification:** Acting as if corresponding elements are the same property.
- **MUST NOT infer:**
  - MUST NOT say schema alignment proves the properties denote the same thing in all contexts.
  - MUST NOT say element name equality suffices.

## Mapping Specification

- **Source:** R2RML-01 (explicit mapping artifact)
- **Formal meaning:** An explicit, versioned description of how source-schema data is translated into the target graph (a Triples Map in R2RML: Subject Map generating the subject IRI plus Predicate-Object Maps). Because it is an artifact, a mapping can be reviewed, versioned, and reprocessed.
- **Book wording:** "Mapping là đặc tả phiên bản hóa: nguồn → lược đồ đích."
- **Dangerous simplification:** Treating mapping as code with no separate review.
- **MUST NOT infer:**
  - MUST NOT say a mapping is correct just because it runs.
  - MUST NOT conflate mapping with identity resolution.

## Direct Mapping

- **Source:** DIRECT-MAP-01 (W3C Recommendation)
- **Formal meaning:** The automatic, default RDB→RDF mapping: each table becomes a class, each row a resource (IRI built from table name + primary key), each column a predicate, values typed by SQL type. No custom rules; the output shape follows the database schema, not a target ontology.
- **Book wording:** "Direct Mapping là phép ánh xạ mặc định tự động RDB→RDF, hình dạng theo lược đồ cơ sở dữ liệu."
- **Dangerous simplification:** Assuming the mechanical RDF shape is semantically optimal.
- **MUST NOT infer:**
  - MUST NOT say direct mapping produces a target-ontology-shaped graph.
  - MUST NOT conflate direct mapping (RDB→RDF) with CSVW (tabular→RDF) with R2RML (custom).

## Semantic / Structural Mapping (custom)

- **Source:** R2RML-01 (custom mapping); CSVW-01
- **Formal meaning:** A mapping written to a target schema/ontology rather than the source schema — the author decides which source columns fill which target properties, which classes, which values become IRIs vs literals. R2RML expresses such mappings for RDB; CSVW annotations + csv2rdf for tabular data.
- **Book wording:** "Mapping ngữ nghĩa do tác giả viết theo ontology đích."
- **Dangerous simplification:** Presenting mappings as reversible or lossless.
- **MUST NOT infer:**
  - MUST NOT say a custom mapping preserves all source information.
  - MUST NOT say mapping decisions are value-neutral.

## Deduplication

- **Source:** RL-01 (duplicate detection via linkage); BOOK-DEFINED
- **Formal meaning:** Identifying records that duplicate each other — either exact duplicates (identical content) or near-duplicates (the same claim stated with different values/units). Duplicates are candidates to be merged or reconciled before ledger insertion. Claims with identical content but different provenance are *not* the same claim (Ch6 identity).
- **Book wording:** "Khử trùng phân biệt bản ghi trùng nội dung để hợp nhất, không xóa."
- **Dangerous simplification:** Deleting duplicates instead of reconciling their evidence.
- **MUST NOT infer:**
  - MUST NOT say two duplicate-content claims are one claim.
  - MUST NOT say deduplication is safe to do by dropping evidence.

## Claim Deduplication

- **Source:** Ch6 claim identity (content ≠ identity); BOOK-DEFINED
- **Formal meaning:** The book's specific dedup rule for the Claim Ledger: two candidate claims with the same content but different provenance are candidate *duplicates of content*; they may be merged into one ledger claim only through the claimed-merge decision with both provenances preserved, never by silently discarding one.
- **Book wording:** "Khử trùng phát biểu bảo toàn cả hai provenance."
- **Dangerous simplification:** Using SHA of content as claim identity.
- **MUST NOT infer:**
  - MUST NOT use content hash as the ledger claim IRI.
  - MUST NOT say merged claims lose individual provenance.

## Idempotent Ingestion

- **Source:** BOOK-DEFINED (systems discipline; grounded in content-hash mechanisms)
- **Formal meaning:** Running the same acquisition/integration more than once produces the same ledger state — no duplicate claims, no duplicate provenance. Idempotency is achieved by determinism and content-hash keys, so reprocessing does not corrupt the ledger.
- **Book wording:** "Thu nạp vào hệ thống nhiều lần cho cùng một kết quả sổ phát biểu."
- **Dangerous simplification:** Assuming double ingestion is harmless without a mechanism.
- **MUST NOT infer:**
  - MUST NOT say idempotency is free.
  - MUST NOT say idempotency implies the result is correct.

## Content Hash

- **Source:** BOOK-DEFINED (uses standard cryptographic hashing)
- **Formal meaning:** A deterministic digest of a normalized record or extracted fragment (over its canonical form: subject IRI, predicate, typed object, source fragment), used as a stable key for deduplication and idempotency. Changing the record content changes the hash.
- **Book wording:** "Content Hash là vân tay định danh nội dung chuẩn hóa."
- **Dangerous simplification:** Hashing the raw extraction, whose form varies run-to-run.
- **MUST NOT infer:**
  - MUST NOT say hash equality implies the claims are identical in meaning.
  - MUST NOT say a hash is provenance.

## Structural Validation (SHACL gate)

- **Source:** SH-01 (SHACL)
- **Formal meaning:** Checking candidate graph data against declared shapes — required properties, expected classes, datatypes, cardinalities — producing a validation report. Validation checks *shape conformance*, not *truth*.
- **Book wording:** "Valid hóa SHACL kiểm tra hình dạng khớp, không kiểm tra tính đúng."
- **Dangerous simplification:** Reporting "validated" as if it meant "true".
- **MUST NOT infer:**
  - MUST NOT say SHACL validation implies semantic correctness.
  - MUST NOT say passing shapes justifies acceptance.

## Validation ≠ Acceptance

- **Source:** SH-01; Ch6 governance; BOOK-DEFINED
- **Formal meaning:** A structurally valid candidate may still be rejected (contradicts stronger evidence) and an invalid one is never accepted as-is. Acceptance is a governance decision (Ch6 states) that validation reports inform but never replace.
- **Book wording:** "Hợp lệ về hình dạng ≠ được chấp nhận vào sổ."
- **Dangerous simplification:** Turning the SHACL gate into the single acceptance test.
- **MUST NOT infer:**
  - MUST NOT say `sh:conforms true` → accepted knowledge.
  - MUST NOT say invalid data is automatically discarded (it may route to review).

## Conflict Detection

- **Source:** Ch6 contradiction taxonomy; BOOK-DEFINED
- **Formal meaning:** Detecting, among candidate claims (and against ledger claims), pairs whose contents cannot both hold in the same context — e.g., two different `ex:rateOfChange` values for the same mechanism in the same context, or a predicate-semantics contradiction (derivative vs integral). Detection uses the Ch6 five-type taxonomy (identity, predicate semantics, temporal scope, spatial/jurisdictional scope, context).
- **Book wording:** "Phát hiện xung đột tìm cặp phát biểu không thể cùng đúng trong một ngữ cảnh."
- **Dangerous simplification:** Treating every textual difference as a conflict.
- **MUST NOT infer:**
  - MUST NOT say conflict means one is false; context may dissolve it.
  - MUST NOT say conflict detection is complete (undecidable in general practice).

## Integration Decision

- **Source:** DI-01 (sound/complete/exact mapping semantics informs the decision); BOOK-DEFINED
- **Formal meaning:** The decision per candidate claim or group of claims: accept, reject, or defer to human review, applying the system's integration policy and considering evidence (Ch6). The decision is recorded with its rationale as part of claim governance state.
- **Book wording:** "Quyết định tích hợp trả về: chấp nhận / từ chối / chuyển xem xét."
- **Dangerous simplification:** Silently accepting with no recorded rationale.
- **MUST NOT infer:**
  - MUST NOT say an accept decision is a proof of truth.
  - MUST NOT say decisions are unrevisable.

## Merge Outcome

- **Source:** Ch6 governance (merge preserves losing claims); BOOK-DEFINED
- **Formal meaning:** The result of integrating a cluster of candidate claims into the ledger: either a new claim inserted, an existing ledger claim strengthened by additional evidence, a superseded claim marked (Ch6 Superseded state), or a merge recorded with both provenances retained. Losing claims are never deleted.
- **Book wording:** "Kết quả hợp nhất ghi trạng thái mới và bảo toàn cả hai xâu provenance."
- **Dangerous simplification:** Overwriting the ledger with the winner.
- **MUST NOT infer:**
  - MUST NOT say merged-out claims disappear.
  - MUST NOT say superseded means false.

## Claim Ledger Insertion

- **Source:** Ch6 Claim Ledger → projection; BOOK-DEFINED
- **Formal meaning:** The committed write of an accepted claim into the Claim Ledger with its full epistemic envelope: content, provenance, evidence, temporal scope, governance state, confidence. The Claim Ledger is the system of record; the Canonical Knowledge View is its projection (Ch6).
- **Book wording:** "Ghi sổ phát biểu là phép ghi có bảo toàn toàn bộ phong bì tri thức."
- **Dangerous simplification:** Writing only the triple without provenance/state.
- **MUST NOT infer:**
  - MUST NOT say ledger insertion implies eternal truth.
  - MUST NOT say the projection is the ledger.

## Canonical Projection

- **Source:** Ch6 Canonical Knowledge View; BOOK-DEFINED
- **Formal meaning:** The materialized view derived from the Claim Ledger after governance — queries see accepted (and reconciled) claims. It is rebuilt/refreshed from the ledger; it is not an independent store of truth.
- **Book wording:** "Chiếu hình là khung nhìn được dựng lại từ sổ phát biểu."
- **Dangerous simplification:** Querying the projection as if it were the ledger.
- **MUST NOT infer:**
  - MUST NOT say projection edits update the ledger.
  - MUST NOT say the projection contains rejected claims.

## Lineage

- **Source:** PROV-DM-01 (derivation chains); PROV-01
- **Formal meaning:** The full provenance chain from a ledger claim back through integration decisions, extractions, and observations to source fragments. Lineage answers "how did this claim come to be here?" as an auditable path.
- **Book wording:** "Lineage là chuỗi provenance truy về từ phát biểu đến mẩu nguồn."
- **Dangerous simplification:** Equating lineage with evidence; treating it as truth.
- **MUST NOT infer:**
  - MUST NOT say a complete lineage implies correctness.
  - MUST NOT say lineage tells you *why to believe*.

## Evidence vs Lineage

- **Source:** Ch6 Source ≠ Evidence; PROV-DM-01; BOOK-DEFINED
- **Formal meaning:** Lineage tells you *where a claim came from* (derivation/attribution); evidence tells you *why to believe or disbelieve it* (support/challenge). A claim can have rich lineage and weak evidence, or strong evidence with thin lineage.
- **Book wording:** "Lineage trả lời 'từ đâu đến?'; bằng chứng trả lời 'vì sao tin?'"
- **Dangerous simplification:** Reporting lineage length as confidence.
- **MUST NOT infer:**
  - MUST NOT say long lineage → true.
  - MUST NOT use lineage as a substitute for evidence.

## Human Review (review queue)

- **Source:** RL-01 (clerical review zone between thresholds); BOOK-DEFINED
- **Formal meaning:** The lane for cases the automatable pipeline cannot decide confidently: pairs in the "possible match" zone, claims below a confidence policy, conflicts not dissolved by context. Humans review with the full evidence bundle and record decisions in the ledger.
- **Book wording:** "Hàng đợi xem xét là làn dành cho ca máy chưa quyết được."
- **Dangerous simplification:** Sending every case to humans (no pipeline decides anything) or none (humans never gate).
- **MUST NOT infer:**
  - MUST NOT say human review guarantees correctness.
  - MUST NOT say human review subsumes evidence.

## Data Quality Dimensions

- **Source:** HOGAN-CREATE-01 (quality assessment framing); Ch6 confidence; BOOK-DEFINED dimensions
- **Formal meaning:** The measurable aspects of the ingested data that the pipeline tracks: accuracy (conforms to validated reference), completeness (all expected content acquired), consistency (no internal contradictions), timeliness (freshness vs valid time), provenance completeness, conformance (shapes). Quality is multi-dimensional — one score cannot capture it (mirrors Ch6 multi-dimensional confidence).
- **Book wording:** "Chất lượng dữ liệu là nhiều chiều: chính xác, đầy đủ, nhất quán, kịp thời, truy nguyên."
- **Dangerous simplification:** Reporting one overall "quality %".
- **MUST NOT infer:**
  - MUST NOT say completeness implies accuracy.
  - MUST NOT say quality dimensions are objectively fixed (they depend on system policy).

## Failure Modes (acquisition)

- **Source:** BOOK-DEFINED (catalog of pipeline failure classes; grounded in RL-01/SM-01 failure sources)
- **Formal meaning:** The recurring ways acquisition/integration can go wrong: extraction failure (wrong record), normalization failure (wrong canonical value), blocking failure (true match never compared — recall loss), linkage error (false positive/negative identity), schema misalignment (wrong property correspondence), idempotency failure (duplicates on reprocess), validation-regime confusion, partial acquisition (missing fragments), echo-source contamination, unbounded chunking, and silent policy drift. Each failure mode has a detection signal and a recovery action.
- **Book wording:** "Mỗi dạng hỏng hóc có tín hiệu phát hiện và phục hồi."
- **Dangerous simplification:** Pretending failures are exceptional rather than expected.
- **MUST NOT infer:**
  - MUST NOT say a pipeline with no detected failure is failure-free.
  - MUST NOT say any single metric catches all failure modes.

## Echo Source

- **Source:** BOOK-DEFINED (systems discipline)
- **Formal meaning:** A source that ultimately derives its content from another source already in the system (a summary of a primary source, a mirror, an aggregated feed). Acquiring an echo source adds lineage but often no independent evidence; failing to detect echoes inflates evidence counts.
- **Book wording:** "Echo source là nguồn phái sinh không cung cấp bằng chứng độc lập."
- **Dangerous simplification:** Counting echo claims as independent support.
- **MUST NOT infer:**
  - MUST NOT say two echo claims are two independent pieces of evidence.
  - MUST NOT say an echo proves a primary source's content.

## Pipeline Versioning

- **Source:** R2RML-01 (mapping as versioned artifact); BOOK-DEFINED
- **Formal meaning:** Every component that shapes the output — mappings, extraction patterns, normalization rules, blocking keys, target schema, SHACL gates, integration policy — is versioned with the pipeline; a pipeline version stamp is recorded in the provenance of every ingested claim. Reprocessing is per-version.
- **Book wording:** "Mỗi bước định hình kết quả được đánh phiên bản và ghi vào provenance."
- **Dangerous simplification:** Recording only the data, not the pipeline that produced it.
- **MUST NOT infer:**
  - MUST NOT say claims from an old pipeline version are recomputed automatically.
  - MUST NOT say versioning implies correctness of the latest version.

## Reprocessing

- **Source:** BOOK-DEFINED (idempotency prerequisite)
- **Formal meaning:** Re-running acquisition/integration over source data after a pipeline change to recompute candidate knowledge under the new version. Safe only when ingestion is idempotent; results go through the same gates as first-time ingestion.
- **Book wording:** "Xử lý lại chạy lại pipeline trên cùng dữ liệu sau khi đổi phiên bản."
- **Dangerous simplification:** Reprocessing that writes over the ledger without re-review.
- **MUST NOT infer:**
  - MUST NOT say reprocessing with a new pipeline version preserves old decisions.
  - MUST NOT say reprocessing is free of conflict regeneration.

## Chunking

- **Source:** BOOK-DEFINED (document acquisition practice; grounded in retrieval systems)
- **Formal meaning:** Splitting long documents into bounded, addressable fragments (by headings, paragraphs, or fixed sizes) so extraction operates on coherent units and provenance can be fragment-granular. Chunk size and boundaries are a pipeline decision with quality consequences.
- **Book wording:** "Chunking chia tài liệu dài thành mẩu có ranh giới và địa chỉ."
- **Dangerous simplification:** Splitting mid-formula or mid-definition, breaking fragment meaning.
- **MUST NOT infer:**
  - MUST NOT say chunk boundaries are semantically neutral.
  - MUST NOT say any chunking scheme is universally optimal.

## Retrieval Bound

- **Source:** BOOK-DEFINED
- **Formal meaning:** The scope rule for what a fragment may contribute: extraction from a fragment may only assert what the fragment's own content supports, within its context — not what later chapters, neighboring tables, or world knowledge imply. It is the acquisition-side guard against over-reading.
- **Book wording:** "Ràng buộc truy hồi: chỉ khẳng định điều mẩu nguồn tự nội hàm."
- **Dangerous simplification:** Using whole-source knowledge to fill fragment gaps.
- **MUST NOT infer:**
  - MUST NOT say absent-from-fragment → false (OWA still applies).
  - MUST NOT say a fragment's silence contradicts a claim.

## Extraction Schema

- **Source:** CSVW-01 (annotations typify columns); R2RML-01; BOOK-DEFINED
- **Formal meaning:** The declared intermediate schema for extracted records — fields, expected datatypes, cardinality, allowed values — that extraction must produce before normalization/structuring. It makes extraction output predictable and checkable.
- **Book wording:** "Lược đồ trích xuất khai báo cấu trúc bản ghi trung gian."
- **Dangerous simplification:** Allowing extraction to emit ad-hoc records.
- **MUST NOT infer:**
  - MUST NOT say extraction-schema conformance implies semantic correctness.

## Unresolved Value

- **Source:** Ch6 OWA discipline; BOOK-DEFINED
- **Formal meaning:** A value the pipeline could not determine (unit unknown, ambiguous reference, missing field). It is modeled explicitly as unknown/undetermined (e.g., `ex:unknownValue`) rather than guessed or silently dropped, preserving OWA.
- **Book wording:** "Giá trị chưa xác định được mô hình hóa tường minh, không đoán."
- **Dangerous simplification:** Filling unknown values with defaults.
- **MUST NOT infer:**
  - MUST NOT say unresolved value means the value does not exist.
  - MUST NOT say unresolved value means false.

## Integration Policy

- **Source:** DI-01 (sound/complete/exact mapping semantics); Ch6 governance policy; BOOK-DEFINED
- **Formal meaning:** The system's declared rules for how integration decisions are made: which conflicts require human review, what evidence thresholds apply (Ch6 confidence policy), how echo sources are weighted, when claims are superseded. The policy is a versioned artifact; it operationalizes Ch6 governance over Ch7's pipeline.
- **Book wording:** "Integration policy là bộ quy tắc phiên bản hóa điều khiển quyết định tích hợp."
- **Dangerous simplification:** Hard-coding integration rules inside code without a reviewable policy.
- **MUST NOT infer:**
  - MUST NOT say a policy is neutral or universally right.

## Acquisition Invariant (I1–I7)

- **Source:** BOOK-DEFINED (systems invariants; grounded in PROV-01, SH-01, Ch6 governance)
- **Formal meaning:** The invariants the pipeline must never violate: (I1) every ledger claim has provenance to at least one source fragment; (I2) every provenance edge names a pipeline version; (I3) content hash uniquely identifies normalized content within a source; (I4) validation results accompany every candidate through integration; (I5) no claim is overwritten — state transitions only (Ch6 governance); (I6) idempotency: re-ingestion yields the same ledger state; (I7) every conflict decision has a recorded rationale.
- **Book wording:** "Bảy bất biến bảo vệ tính truy nguyên, không ghi đè, và thu nạp lặp an toàn."
- **Dangerous simplification:** Treating invariants as best-effort.
- **MUST NOT infer:**
  - MUST NOT say invariants guarantee truth.
  - MUST NOT say invariant-preserving systems cannot contain wrong claims.

---

## Review Status (2026-08-30 — acceptance review)

Independent semantic review of `book/chapter07.md` against all 45 records above,
completed 2026-08-30. Every record was checked against the manuscript wording, the
authoritative source, and the prior-chapter semantics (Ch3 identity, Ch5 validation,
Ch6 epistemology).

**Result: 45/45 PASS, 0 PARTIAL, 0 FAIL.**

| # | Contract | Verdict | Review notes |
|---|----------|---------|--------------|
| 1 | Acquisition vs Integration (pipeline split) | PASS | §7.2 two halves with distinct success criteria; split labeled BOOK-DEFINED |
| 2 | Knowledge Acquisition | PASS | §7.2 candidate knowledge, not accepted knowledge |
| 3 | Knowledge Integration | PASS | §7.2 reconciling before ledger; §7.31 C deferred |
| 4 | Source Artifact | PASS | §7.3 registration ≠ reliability; IRI + metadata Turtle |
| 5 | Source Fragment | PASS | §7.4 fragment-granular provenance |
| 6 | Observation (into the pipeline) | PASS | §7.4 raw data before interpretation |
| 7 | Extraction | PASS | §7.5 structured candidate records; not truth |
| 8 | Extraction Activity | PASS | §7.5 PROV Activity breadcrumb |
| 9 | Extraction Confidence | PASS | §7.6 extraction confidence ≠ claim confidence |
| 10 | Normalization | PASS | §7.7 lossy; keep raw value traceable |
| 11 | Structuring | PASS | §7.8 RDF under target schema; target-shape clarification |
| 12 | CandidateGeneration | PASS | §7.9 candidates ≠ decisions |
| 13 | Blocking | PASS | §7.9 recall-oriented coarse pairing |
| 14 | Candidate Matching (comparison) | PASS | §7.10 γ vector evidence, not truth judgment |
| 15 | Record Linkage (identity decision) | PASS | §7.10 Fellegi–Sunter two-threshold zones |
| 16 | Entity Resolution (overview) | PASS | §7.9–7.10 end-to-end |
| 17 | Schema Alignment (schema matching) | PASS | §7.11 element vs structure level |
| 18 | Mapping Specification | PASS | §7.12 versioned source→target artifact |
| 19 | Direct Mapping | PASS | §7.12 W3C default RDB→RDF |
| 20 | Semantic / Structural Mapping (custom) | PASS | §7.12 R2RML/CSVW author decisions; lossy |
| 21 | Deduplication | PASS | §7.13 reconcile, never silently drop |
| 22 | Claim Deduplication | PASS | §7.13 A,B kept separate as two evidence pieces |
| 23 | Idempotent Ingestion | PASS | §7.14 same ledger state on re-run |
| 24 | Content Hash | PASS | §7.14 hash ≠ claim identity; "Hash khác nhau ≠ khác nghĩa" |
| 25 | Structural Validation (SHACL gate) | PASS | §7.15 full focus node/path/constraint/severity report |
| 26 | Validation ≠ Acceptance | PASS | §7.15 valid may be rejected; invalid not deleted |
| 27 | Conflict Detection | PASS | §7.16 not every text difference is conflict |
| 28 | Integration Decision | PASS | §7.17 recorded rationale; not proof of truth |
| 29 | Merge Outcome | PASS | §7.17 insert/strengthen/supersede/merge; preserve both sides |
| 30 | Claim Ledger Insertion | PASS | §7.18 ledger is system of record |
| 31 | Canonical Projection | PASS | §7.18 rebuilt view, not independent of truth |
| 32 | Lineage | PASS | §7.19 provenance path to fragment |
| 33 | Evidence vs Lineage | PASS | §7.19 "from where?" ≠ "why believe?" |
| 34 | Human Review (review queue) | PASS | §7.20 possible match / SHACL fail / conflict |
| 35 | Data Quality Dimensions | PASS | §7.21 six dimensions; no single score |
| 36 | Failure Modes (acquisition) | PASS | §7.22 13 modes with signal + recovery |
| 37 | Echo Source | PASS | §7.23 echo ≠ independent evidence |
| 38 | Pipeline Versioning | PASS | §7.24 every output-shaping component versioned |
| 39 | Reprocessing | PASS | §7.24 safe with idempotency; re-gated |
| 40 | Chunking | PASS | §7.26 boundaries are a decision; changes visible info |
| 41 | Retrieval Bound | PASS | §7.26 top_k/context limit decides visible fragments |
| 42 | Extraction Schema | PASS | §7.27 conformance ≠ semantic correctness |
| 43 | Unresolved Value | PASS | §7.27 modeled explicitly; never guessed; OWA |
| 44 | Integration Policy | PASS | §7.28 versioned decision rules; not neutral |
| 45 | Acquisition Invariant (I1–I7) | PASS | §7.30 invariants ≠ truth; process discipline |

All 45 records verified against manuscript `book/chapter07.md` at branch HEAD. See also
`docs/CHAPTER07_DEPTH_REVIEW.md` (depth table, semantic boundary checklist, capability
test) and `docs/CHAPTER07_BOOK_CHECKPOINT.md` (acceptance criteria).
