# Chapter 10 Semantic Contracts

Authoritative reference for every formal concept in Chapter 10. Each record specifies:

- **Source**: authoritative academic or primary reference
- **Formal meaning**: precise definition from the source
- **Book wording**: simplified phrasing used in the manuscript (Vietnamese)
- **Dangerous simplification**: what the book wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

This document is the semantic contract against which `book/chapter10.md` is reviewed.
Concepts marked **BOOK-DEFINED** are the book's own engineering/pedagogical framework, not
an academic standard; they are labeled explicitly in the manuscript. Recurring sources:
KGQ-01 (Zaveri et al. 2016), REFINE-01 (Paulheim 2017), ONTEVOL-01 (Noy & Klein 2004),
ONTVR-01 (Klein & Fensel 2001), KVLT-01 (Dong et al. 2014), NELL-01 (Mitchell et al.
2018), DRIFT-01 (Gama et al. 2014), DRIFT-02 (Widmer & Kubat 1996), HIDDENTECH-01
(Sculley et al. 2015), BENCH-01 (Recht et al. 2019), CASCADE-01 (Sambasivan et al. 2021),
DQSTD-01 (ISO/IEC 25012:2008), GOVDATA-01 (ISO 8000-1:2022), TKG-01 (Cai et al. 2023),
COLLAPSE-01 (Shumailov et al. 2024, reused from Ch8). The Ch6/Ch7 machinery (claim
governance states, evidence chains, acquisition pipeline), Ch9's Evidence Packet / Query
Execution Router / Answer artifact, and the C471/C210 standing contradiction are carried
forward from previous chapters.

Every record uses the Mechanism-KG worked example (C471 Accepted vs C210 Contested,
E88 → E90 supersession, the RATE_OF_CHANGE mechanism) for continuity.

---

## Living Knowledge System

- **Source:** BOOK-DEFINED synthesis; informed by NELL-01 (a continuously self-extending
  learner) and HIDDENTECH-01 (deployed ML systems are sustained by maintenance, not just
  construction)
- **Formal meaning:** The Knowledge System is a *process with state* — knowledge enters
  (Ch7), changes meaning over time (Ch6 clocks), is learned (Ch8), is queried (Ch9), and
  is measured/maintained/audited (this chapter). Its identity is defined by content,
  operation history, measurements, governance actions, and audit trail together.
- **Book wording:** "Hệ thống Tri thức Sống (Living Knowledge System): tri thức không chỉ
  là một tấm ảnh tĩnh — hệ thống là một tiến trình có trạng thái, được đo, được bảo trì,
  được kiểm toán theo thời gian."
- **Dangerous simplification:** Treating "living" as marketing ("AI that learns by
  itself") instead of an engineering property (observation, measurement, governance, audit).
- **MUST NOT infer:**
  - MUST NOT say a system is "living" merely because it ingests new data.
  - MUST NOT say a living system is self-correcting by definition.
  - MUST NOT present a database with good content but no measurement/audit history as a
    living system.

## System State

- **Source:** BOOK-DEFINED (composition of Ch2–Ch9 state)
- **Formal meaning:** SystemState = knowledge (ledger + canonical view + mechanism graph)
  + index state (Ch9) + governance state (Ch6) + measurement history + audit log.
  A snapshot of the system at time t is incomplete without its measurement and audit history.
- **Book wording:** "Trạng thái hệ thống: nội dung tri thức + trạng thái chỉ mục + trạng
  thái quản trị + lịch sử đo lường + nhật ký kiểm toán."
- **Dangerous simplification:** Defining state as content only; answering "what does the
  system believe" from today's snapshot only.
- **MUST NOT infer:**
  - MUST NOT say state is exhausted by the claim set.
  - MUST NOT answer system-time questions from valid-time data without selecting a clock.

## Staleness

- **Source:** DRIFT-01 (concept drift — the distribution a model/source reflects can be
  outdated), TKG-01 (facts in KGs change over time), Ch6 clocks
- **Formal meaning:** A claim is *stale* when it is still present in active knowledge but
  is no longer supported by the current best evidence/sources. Staleness is an epistemic
  lag, not falsity. Operationally: stalenessLevel from lastAssessmentAge + sourceSuperseded
  + indexReflects.
- **Book wording:** "Cũ/ứ đọng (staleness): một claim vẫn còn trong hệ thống nhưng không
  còn được bằng chứng hiện tại hậu thuẫn. Cũ ≠ sai."
- **Dangerous simplification:** Equating staleness with falsity; deleting stale claims.
- **MUST NOT infer:**
  - MUST NOT say a stale claim is false.
  - MUST NOT say a fresh claim is true (see Freshness).
  - MUST NOT silently drop a stale claim without a governance record (it may be a
    Rejected/Superseded transition, not an erasure).

## Freshness

- **Source:** KGQ-01 (timeliness dimension), DQSTD-01 (timeliness/currency characteristic),
  TKG-01 (temporal dynamics)
- **Formal meaning:** Freshness is the recency of *validation*: how long since the claim
  was checked against current sources, how far the index lags the ledger, how recently the
  schema was reviewed. It is a measurement of currency, deliberately NOT a judgment of
  correctness.
- **Book wording:** "Độ tươi (freshness): độ gần đây của lần kiểm chứng — không phải độ
  đúng. Càng vừa kiểm chứng ≠ càng đúng."
- **Dangerous simplification:** Reading freshness as a proxy for truth.
- **MUST NOT infer:**
  - MUST NOT say fresh ⟹ correct.
  - MUST NOT report a single "freshness" number without saying which subsystem (claims /
    index / schema) it measures.

## Knowledge Debt

- **Source:** HIDDENTECH-01 (technical debt as the cost of accumulated shortcuts in ML
  systems), CASCADE-01 (compounding cost of deferred data quality); BOOK-DEFINED extension
  to the epistemic domain
- **Formal meaning:** The accumulated cost of unresolved epistemic obligations
  — open contradictions, stale accepted claims, un-assessed candidates, outdated schema
  versions, un-synced indexes. Measured in epistemic units (claims pending assessment),
  not lines/config.
- **Book wording:** "Nợ tri thức (knowledge debt): chi phí tích lũy của các nghĩa vụ tri
  thức luận chưa giải quyết — mâu thuẫn mở, claim cũ chưa đánh giá lại, chỉ mục lệch."
- **Dangerous simplification:** Measuring debt only in engineering terms; hiding debt.
- **MUST NOT infer:**
  - MUST NOT equate knowledge debt with code debt (mechanism differs: code debt is build
    cost, knowledge debt is epistemic risk).
  - MUST NOT say debt is automatically harmful — manageable debt is normal; silent
    unmanaged debt is the risk.

## Contradiction Debt

- **Source:** BOOK-DEFINED extension of Ch6 contradiction governance; informed by
  CASCADE-01 (compounding effects of deferred data-quality issues)
- **Formal meaning:** The portion of knowledge debt attributable to unresolved
  contradiction pairs (e.g., C471 Accepted vs C210 Contested). Tracking includes how long
  each pair has been open and whether new evidence could resolve it.
- **Book wording:** "Nợ mâu thuẫn: phần nợ tri thức do các cặp mâu thuẫn chưa phân xử —
  theo dõi thời gian mở và khả năng giải quyết bằng bằng chứng mới."
- **Dangerous simplification:** Treating any open contradiction as a bug.
- **MUST NOT infer:**
  - MUST NOT say all ledger contradictions are inconsistencies (see Consistency).
  - MUST NOT leave a contradiction pair open silently without tracking it.

## Self-Observation

- **Source:** NELL-01 (NELL continuously monitors its own extraction to decide what to
  learn next), HIDDENTECH-01 (systems need visibility into their own behavior); BOOK-DEFINED
  as the observation stage
- **Formal meaning:** The system records raw observations of its own operation
  — query log, retrieval behavior, ledger activity, index activity, hypothesis churn,
  source updates. Observation is passive recording; interpretation is separate.
- **Book wording:** "Tự quan sát (self-observation): hệ thống ghi lại hành vi vận hành của
  chính nó — log truy vấn, hành vi truy xuất, hoạt động sổ cái, độ trễ chỉ mục."
- **Dangerous simplification:** Confusing recording with understanding.
- **MUST NOT infer:**
  - MUST NOT say the system understands itself because it logs.
  - MUST NOT say observation alone is governance (see Monitoring ≠ Governance).

## Observability

- **Source:** BOOK-DEFINED (distinct from self-observation); informed by HIDDENTECH-01
- **Formal meaning:** Observability is the property that internal state can be *answered
  about* from traces — given a metric value or alert, an assessor can reconstruct WHY by
  replaying linked observations. Self-observation records; observability enables
  interrogation.
- **Book wording:** "Khả quan sát (observability): từ một cảnh báo hay số liệu, người đánh
  giá có thể truy vấn lại nguyên nhân qua các quan sát liên kết."
- **Dangerous simplification:** Equating observability with having logs.
- **MUST NOT infer:**
  - MUST NOT call a system observable if alerts carry no reference to their observations.

## Monitoring Loop

- **Source:** BOOK-DEFINED — the chapter's central mechanism; stages informed by
  HIDDENTECH-01 (feedback and debt arise when systems run) and DRIFT-01 (change detection);
  governance handoff per Ch6/Ch7
- **Formal meaning:** COLLECT observations → AGGREGATE into metrics over windows →
  COMPARE against thresholds (policy) → ALERT with linked observations → ASSESS (governed,
  epistemic) → ACT (re-validate / re-assess / retire / supersede / ingest) → RE-MEASURE.
  The loop decides *attention and maintenance*, never the truth of the world.
- **Book wording:** "Vòng giám sát (monitoring loop): thu thập → tổng hợp → so ngưỡng →
  cảnh báo → đánh giá → hành động → đo lại. Vòng này quyết định 'cần chú ý gì', không
  quyết định 'cái gì đúng'."
- **Dangerous simplification:** Presenting the loop as a truth-finder; skipping the
  ASSESS step and auto-acting from alerts.
- **MUST NOT infer:**
  - MUST NOT say an alert levels a verdict about the world.
  - MUST NOT claim the loop replaces Ch6/Ch7 governance.

## Aggregation Window

- **Source:** DRIFT-01 (detection depends on the window over which drift is observed)
- **Formal meaning:** A metric is defined over a window — point-in-time, sliding, cumulative,
  or per-version. The same underlying stream yields different signals under different
  windows (a 1-day window is noisy; a 365-day window hides recent degradation).
- **Book wording:** "Cửa sổ tổng hợp (aggregation window): mỗi số liệu phải nói rõ đo trên
  khoảng nào — điểm, trượt, cộng dồn, hay theo phiên bản. Số liệu không có cửa sổ là vô nghĩa."
- **Dangerous simplification:** Reporting "the metric" without its window; choosing a window
  to hide a trend.
- **MUST NOT infer:**
  - MUST NOT compare two metrics of different windows as if equal.
  - MUST NOT say a metric is "normal" without stating its window and baseline.

## Threshold

- **Source:** BOOK-DEFINED as policy; supported by DQSTD-01 (quality targets are chosen
  requirements, not physical constants) and GOVDATA-01 (governance sets acceptable levels)
- **Formal meaning:** A threshold encodes how much staleness/degradation/contradiction the
  operator tolerates. It is chosen by governance, may vary per domain/question class, and
  crossing it triggers *attention*, not a world-verdict.
- **Book wording:** "Ngưỡng (threshold): quyết định chính sách về mức dung sai — do nhà vận
  hành đặt ra, không phải hằng số vật lý. Vượt ngưỡng = cần chú ý, không phải = sai."
- **Dangerous simplification:** Reading a threshold crossing as proof of error.
- **MUST NOT infer:**
  - MUST NOT say "above threshold ⟹ claim false".
  - MUST NOT say thresholds are derivable from the world rather than chosen by policy.

## Alert

- **Source:** BOOK-DEFINED; informed by CASCADE-01 (issues discovered in operation must be
  traceable to their causes)
- **Formal meaning:** A structured, falsifiable message: metric, observedValue, threshold,
  window, observedAt, linkedObservations, severity (policy-based). An assessor must be able
  to verify the alert against underlying observations.
- **Book wording:** "Cảnh báo (alert): thông điệp có cấu trúc — số liệu, giá trị, ngưỡng,
  cửa sổ, thời điểm, các quan sát liên kết, mức độ. Cảnh báo phải kiểm chứng được."
- **Dangerous simplification:** A bare "system degraded" message with no references can't
  be assessed — noise.
- **MUST NOT infer:**
  - MUST NOT say "no alert ⟹ no problem" (thresholds only cover what is measured).
  - MUST NOT treat alert severity as a truth rating.

## Assessment

- **Source:** REFINE-01 (deciding whether KG content is wrong/missing is an analytic step),
  Ch6 (governed assessment of claims)
- **Formal meaning:** The epistemic stage of the loop: is the metric artifact (measurement
  error)? is the knowledge wrong? is the index stale? is a claim superseded? Assessment
  re-uses Ch6/Ch7 machinery (evidence chain, governance state) and outputs a maintenance
  action or "no action". Assessment is NOT automatic action.
- **Book wording:** "Đánh giá (assessment): giai đoạn tri thức luận của vòng giám sát —
  dùng chuỗi bằng chứng (Ch6) và trạng thái quản trị để quyết định hành động bảo trì,
  không phải tự động sửa."
- **Dangerous simplification:** Skipping assessment and acting directly on an alert.
- **MUST NOT infer:**
  - MUST NOT say the loop self-governs without an assessment step.
  - MUST NOT say a metric change alone establishes an epistemic status.

## Feedback Loop

- **Source:** HIDDENTECH-01 (feedback loops are a core dependency/risk of ML systems),
  DRIFT-01 (adaptation loops), COLLAPSE-01 (recursive training as a dangerous loop)
- **Formal meaning:** A cycle where system output becomes input again: QA answers → user
  feedback → candidate claims; QA failure → re-acquisition → re-assessment; measurement →
  action → re-measure. Loops are powerful and must carry a contract: signal source,
  conversion into system state, and governance constraints.
- **Book wording:** "Vòng phản hồi (feedback loop): đầu ra trở lại làm đầu vào. Mỗi vòng
  cần hợp đồng: ai tạo tín hiệu, ai chuyển thành trạng thái tri thức, dưới ràng buộc quản
  trị nào."
- **Dangerous simplification:** Treating loops as uniformly good (self-improvement).
- **MUST NOT infer:**
  - MUST NOT say a loop improves the system by default.
  - MUST NOT let a loop write to the ledger without the Ch7 gate.

## Candidate Claim from QA

- **Source:** BOOK-DEFINED; the Ch9 operating rule (QA answers never enter the ledger
  directly), Ch7 ingestion pipeline
- **Formal meaning:** A QA answer, a user correction, or feedback becomes CandidateKnowledge
  — it enters the Ch7 acquisition/integration pipeline and is only accepted through governed
  assessment. It is a candidate, not accepted knowledge.
- **Book wording:** "Câu trả lời QA chỉ là ứng viên: phải qua đường ống Ch7 (thu nạp →
  tích hợp → đánh giá có quản trị) mới có thể thành claim Accepted."
- **Dangerous simplification:** Treating a fluent answer as ingested knowledge.
- **MUST NOT infer:**
  - MUST NOT say QA output is knowledge (rule from Ch9 §9.59).
  - MUST NOT shortcut the ledger.

## User Correction

- **Source:** NELL-01 (human feedback steers learning but is validated, not trusted
  blindly), Ch7 candidate handling
- **Formal meaning:** A user correction is a valuable, low-cost provenance signal (source =
  user report) that must be verified like any other candidate. It may indicate a real gap
  or a user misunderstanding.
- **Book wording:** "Sửa của người dùng là tín hiệu, không phải phán quyết: vào như
  CandidateClaim với nguồn 'báo cáo người dùng', được thẩm định như mọi ứng viên."
- **Dangerous simplification:** Auto-accepting corrections (majority = truth).
- **MUST NOT infer:**
  - MUST NOT say "many users complained ⟹ claim false" (feedback ≠ evidence).
  - MUST NOT treat a correction as ground truth.

## Model Collapse

- **Source:** COLLAPSE-01 (Shumailov et al. 2024; reused from Ch8)
- **Formal meaning:** When a generative model trains on its own output, learned
  distributions degenerate: tail content disappears and errors compound. The KG system's
  milder form: summaries become sources, generated claims become ingestion input, synthetic
  evidence replaces registered sources.
- **Book wording:** "Sụp đổ mô hình (model collapse): huấn luyện trên đầu ra của chính nó
  làm suy thoái phân bố — đuôi phân bố biến mất, lỗi cộng dồn. Dạng nhẹ trong KG: tóm tắt
  thành nguồn, đáp án sinh thành nguồn."
- **Dangerous simplification:** Treating collapse as mere noise rather than systematic,
  self-reinforcing degeneration.
- **MUST NOT infer:**
  - MUST NOT say any synthetic data is independent evidence (Ch8 rule).
  - MUST NOT conflate collapse with staleness (see the collision table).

## Feedback Collapse

- **Source:** BOOK-DEFINED synthesis from COLLAPSE-01 (recursive reuse) and HIDDENTECH-01
  (feedback dependencies); the Ch9 agentic-retrieval failure analysis (§9.46–9.50)
- **Formal meaning:** The system answers from its own answers: an early wrong-but-fluent
  answer is accepted, becomes the "known" answer, is retrieved and repeated, and original
  evidence is forgotten. Prevention: the Ch7 gate, source provenance, abstention, rate
  bounds, audit.
- **Book wording:** "Phản hồi sụp đổ (feedback collapse): hệ thống trả lời từ đáp án của
  chính nó và quên bằng chứng gốc. Ngăn bằng cổng Ch7, giữ provenance nguồn, cho phép từ
  chối, giới hạn tốc độ vòng lặp, kiểm toán."
- **Dangerous simplification:** Describing collapse as random noise.
- **MUST NOT infer:**
  - MUST NOT say preventive measures eliminate risk (they bound it).
  - MUST NOT say one good answer prevents collapse of the loop.

## Benchmark Decay

- **Source:** BENCH-01 (Recht et al. 2019)
- **Formal meaning:** Re-used test sets and benchmarks decay: they leak into the system, no
  longer reflect real questions, and a rising benchmark score can coexist with declining
  real quality. Newly re-built test sets drop 11–14% accuracy in the source experiment.
- **Book wording:** "Mục nát benchmark (benchmark decay): bộ kiểm thử cũ bị 'dò' ra, không
  còn phản ánh câu hỏi thật; điểm benchmark tăng không chứng minh chất lượng hệ thống tăng."
- **Dangerous simplification:** Treating benchmark score as system quality.
- **MUST NOT infer:**
  - MUST NOT say benchmarkScore(t) = system quality(t).
  - MUST NOT run QA forever on a static, leaked benchmark without re-authoring it.

## Knowledge Quality Dimension

- **Source:** KGQ-01 (LD quality dimensions with metrics), DQSTD-01 (data quality
  characteristics); the book selects five
- **Formal meaning:** A quality dimension is a measurable facet of knowledge-management
  behavior: correctness (supported and true), completeness (domain coverage), freshness
  (recency of validation), consistency (no unresolved conflict), trustworthiness (reliability
  of provenance/governance). Each dimension needs an operational measure and a window.
- **Book wording:** "Năm chiều chất lượng: đúng, đủ, tươi, nhất quán, đáng tin. Mỗi chiều
  có thước đo, cửa sổ, và điều nó KHÔNG đo."
- **Dangerous simplification:** A single quality number; quality = truth.
- **MUST NOT infer:**
  - MUST NOT say high quality ⟹ true (see Quality ≠ Truth).
  - MUST NOT present one dimension as the whole of quality.

## Correctness (over time)

- **Source:** REFINE-01 (correctness is about error detection/repair against evidence)
- **Formal meaning:** Correctness is relative to evidence available at assessment time; a
  claim Accepted at t may fail re-validation at t+Δ. Correctness must be re-derived, not
  assumed permanent.
- **Book wording:** "Đúng theo thời gian: Accepted ở t chỉ có nghĩa 'đúng so với bằng chứng
  ở t'. Phải tái xác minh lại khi bằng chứng đổi."
- **Dangerous simplification:** Treating Accepted as permanent.
- **MUST NOT infer:**
  - MUST NOT say acceptance is a permanent property.
  - MUST NOT report correctness without its evidence-as-of time.

## Completeness (over time)

- **Source:** REFINE-01 (link prediction = completeness gap), KVLT-01 (web-scale coverage
  is bounded and extensible), KGQ-01 (completeness dimension)
- **Formal meaning:** Completeness is coverage of a *declared scope*; it changes as the
  domain gains new members (e.g., a new application of RATE_OF_CHANGE). Never absolute.
- **Book wording:** "Độ đủ: tỉ lệ che phủ so với phạm vi khai báo — không bao giờ tuyệt đối;
  phạm vi mở rộng thì độ đủ giảm tương đối."
- **Dangerous simplification:** Presenting one completeness number without its scope.
- **MUST NOT infer:**
  - MUST NOT say "complete" absolutely, only relative to a scope.

## Freshness (over time)

- **Source:** KGQ-01 (timeliness), DQSTD-01 (currency), TKG-01 (facts change over time)
- **Formal meaning:** Freshness decays without maintenance and must be tracked per
  subsystem (ledger / index / schema). A "fresh" claim measured against an old schema may
  be fresh in content-time but stale in structure-time.
- **Book wording:** "Độ tươi suy giảm theo thời gian; phải nói rõ đo cho hệ con nào — claim,
  chỉ mục, hay schema."
- **Dangerous simplification:** One global freshness flag.
- **MUST NOT infer:**
  - MUST NOT say a fresh index implies fresh schema or fresh claims.

## Consistency

- **Source:** KGQ-01 (consistency dimension: no conflicting statements), Ch6 (scoped
  contradiction)
- **Formal meaning:** Consistency = no unresolved conflict at the same scope. C471 vs C210
  is NOT a consistency violation if scopes differ — it is a *governed contradiction* with
  explicit scope. Resolvable inconsistency (same scope, opposite content, both Accepted)
  is a bug.
- **Book wording:** "Nhất quán: không có xung đột cùng phạm vi. C471 và C210 khác phạm vi là
  mâu thuẫn được quản trị, không phải vết nứt nhất quán."
- **Dangerous simplification:** Counting any contradiction as an inconsistency.
- **MUST NOT infer:**
  - MUST NOT say two scoped claims in tension are inconsistent.
  - MUST NOT say a governed contradiction is harmless by default (still tracked as debt).

## Trustworthiness

- **Source:** KGQ-01 (trustworthiness/provenance dimension), GOVDATA-01 (quality is a
  governed property), Ch6/Ch7 (registered sources, evidence chains, audited governance)
- **Formal meaning:** Trustworthiness is the reliability of the knowledge's provenance and
  governance: sources registered and verified, evidence chains intact, transitions
  audited, provenance retrievable for every Accepted claim. A claim can be correct yet low
  in trustworthiness (uncited, unassessed).
- **Book wording:** "Độ đáng tin: độ tin cậy của provenance và quản trị — nguồn đã đăng ký,
  chuỗi bằng chứng lành, chuyển trạng thái được kiểm toán. Đáng tin ≠ đúng."
- **Dangerous simplification:** Reading trustworthiness as truth.
- **MUST NOT infer:**
  - MUST NOT say trustworthy ⟹ true.
  - MUST NOT say a correct-but-uncited claim is high-trustworthiness.

## Level vs Trend

- **Source:** DRIFT-01 (drift detection examines change over time, not a single point)
- **Formal meaning:** A level is a point value; a trend is its change over a window. Slow
  drift is invisible in a level; a spike is invisible in a long average. Detection needs
  baseline, slope, and policy tolerance.
- **Book wording:** "Mức (level) là điểm; xu hướng (trend) là đổi thay theo cửa sổ. Trôi
  chậm không thấy trong một điểm; nảy mạnh không thấy trong trung bình dài."
- **Dangerous simplification:** Making decisions from a single point.
- **MUST NOT infer:**
  - MUST NOT say a flat level means health without checking the trend.

## Degradation

- **Source:** DRIFT-01 (sustained distribution shift), CASCADE-01 (compounding quality
  decline), BOOK-DEFINED operationalization
- **Formal meaning:** Degradation = sustained decline in a quality dimension (freshness
  falling, contradiction queue growing, abstention rising, completeness shrinking relative
  to scope). It is a trend, not a single bad event.
- **Book wording:** "Suy thoái (degradation): suy giảm kéo dài của một chiều chất lượng —
  là xu hướng, không phải một sự kiện xấu."
- **Dangerous simplification:** Confusing one bad day with degradation, or hiding
  degradation in a long average.
- **MUST NOT infer:**
  - MUST NOT say a single spike is degradation (needs trend + baseline).
  - MUST NOT say quality metrics capture all degradation (they reflect only what is measured).

## Re-validation

- **Source:** REFINE-01 (verifying KG content against sources), KVLT-01 (re-checking
  extracted facts), BOOK-DEFINED as a maintenance operation
- **Formal meaning:** Re-check a claim or claim-set against current sources. Scales by
  full / sampled (statistical, with recorded sample) / triggered (when a cited source
  changes). Reduces risk, does not eliminate it.
- **Book wording:** "Tái xác minh (re-validation): kiểm lại claim so với nguồn hiện tại —
  toàn bộ, lấy mẫu, hay theo kích hoạt khi nguồn trích dẫn đổi."
- **Dangerous simplification:** Saying one re-validation pass makes claims permanently valid.
- **MUST NOT infer:**
  - MUST NOT say re-validated ⟹ permanently true.
  - MUST NOT report a sampled re-validation as a full one without stating the sample.

## Re-assessment

- **Source:** Ch6 (governed state transitions), ONTEVOL-01 (ontology/claim meaning can
  change and must be re-evaluated)
- **Formal meaning:** A governed transition of a claim's state under new evidence (e.g.,
  C471 stays Accepted, moves to Contested, or is Superseded). The transition records:
  trigger, changed evidence, decision, assessment time.
- **Book wording:** "Đánh giá lại (re-assessment): chuyển trạng thái claim có quản trị theo
  bằng chứng mới — ghi kích hoạt, bằng chứng đổi, quyết định, thời điểm."
- **Dangerous simplification:** Re-running assessment without evidence change (churn).
- **MUST NOT infer:**
  - MUST NOT re-assess without recording the evidence delta.
  - MUST NOT let re-assessment bypass the Ch6 governance record.

## Retirement

- **Source:** ONTEVOL-01, ONTVR-01 (leaving old versions available, not deleting),
  Ch6 (Rejected/Superseded states)
- **Formal meaning:** Moving knowledge out of active use with a governed record — claim to
  Rejected/Superseded, schema version deprecated, hypothesis retired (Ch8). Retirement is
  NOT deletion: history and audit remain, and the item can be resurrected.
- **Book wording:** "Nghỉ hưu (retirement): đưa tri thức khỏi dòng hoạt động có ghi chép —
  không phải xóa; lịch sử và kiểm toán còn, có thể phục hồi nếu bằng chứng đổi."
- **Dangerous simplification:** Deleting instead of retiring.
- **MUST NOT infer:**
  - MUST NOT say retired ⟹ erased.
  - MUST NOT say a retired claim cannot be reconsidered.

## Supersession

- **Source:** ONTVR-01 (version compatibility and replacement), Ch6 (Superseded state)
- **Formal meaning:** Claim B supersedes claim A: record edge A → B, mark A's state
  (Superseded/Rejected), keep A's evidence chain, update dependents (index, summaries,
  QA answers). Supersession chains A → B → C form a history; queries can see current and
  historical states (Ch9 Canonical vs Ledger at system scale).
- **Book wording:** "Thay thế (supersession): B thay A — ghi cạnh A→B, đánh dấu A, giữ chuỗi
  bằng chứng, cập nhật nơi phụ thuộc. Chuỗi A→B→C là lịch sử."
- **Dangerous simplification:** Overwriting A without a record.
- **MUST NOT infer:**
  - MUST NOT break supersession chains by silent overwrite.
  - MUST NOT say "current" without the ability to answer "historical at t".

## Batch Governance

- **Source:** ONTEVOL-01 (large-scale ontology/claim changes), GOVDATA-01 (governed
  operations), BOOK-DEFINED
- **Formal meaning:** Acting on many claims at once (schema migration, source retraction,
  threshold change) requires: a plan, a dry-run, an audit per individual change, and a
  rollback. A batch is a governed operation, not a sledgehammer edit.
- **Book wording:** "Thao tác hàng loạt (batch governance): nhiều claim cùng đổi — cần kế
  hoạch, chạy thử (dry-run), kiểm toán từng thay đổi, và khả năng hoàn tác."
- **Dangerous simplification:** Large-scale silent edits.
- **MUST NOT infer:**
  - MUST NOT run a batch without a dry-run for high-blast-radius changes.
  - MUST NOT say a batch is atomic if mid-batch failure leaves partial state (needs rollback).

## Audit Trail

- **Source:** GOVDATA-01 (data quality as a governed, auditable property), Ch6 provenance,
  Ch9 answer provenance; BOOK-DEFINED record schema
- **Formal meaning:** Every governed action writes AuditRecord: what, who/what (actor,
  agent, policy), onWhat, beforeState, afterState, evidence (why), at (audit time),
  authorization. The trail enables *reconstruction*: given an answer, replay why the
  system believes it. Audit ≠ logging alone.
- **Book wording:** "Vết kiểm toán (audit trail): mọi hành động có quản trị ghi bản ghi —
  cái gì, ai, lên gì, trước/sau, bằng chứng, thời điểm, cho phép. Không phải cứ ghi log là
  có vết kiểm toán."
- **Dangerous simplification:** Treating any log file as an audit trail.
- **MUST NOT infer:**
  - MUST NOT say a system is auditable if its records cannot reconstruct belief at t.

## Controlled Trust

- **Source:** GOVDATA-01 (quality/governance as the basis of reliance), Ch6/Ch7/Ch9
  provenance chain; BOOK-DEFINED engineering sense
- **Formal meaning:** Trust is an engineering property: the system's behavior is verifiable
  through provenance, governance, and audit. Controlled trust = you can inspect why the
  system believes what it believes — and you still exercise oversight. Trust is earned per
  subsystem, per action, over time.
- **Book wording:** "Tin cậy có kiểm soát (controlled trust): hệ thống đáng tin theo nghĩa
  kỹ thuật — có thể kiểm tra vì sao nó tin — và người vận hành vẫn giữ sự giám sát."
- **Dangerous simplification:** Trust as an attitude ("we built it, so it's trustworthy").
- **MUST NOT infer:**
  - MUST NOT say trust ⟹ can stop checking (see Trust ≠ Blind Trust).

## Automation Gradient

- **Source:** BOOK-DEFINED (engineering model); supported by GOVDATA-01 (governance sets
  what may be automated) and HIDDENTECH-01 (deployment discipline)
- **Formal meaning:** Different actions deserve different automation levels: index sync
  (full auto), metric alerting (full auto, read-only), re-validation of low-risk claims
  (auto with audit), claim re-assessment (governed gate), schema migration (dry-run +
  approval), knowledge retirement (governed + audit). Higher impact → more gates.
- **Book wording:** "Dốc tự động hóa (automation gradient): tác động càng lớn, cổng quản trị
  càng cao — reindex tự động, đánh giá lại claim cần cổng quản trị, di trú schema cần chạy
  thử + phê duyệt."
- **Dangerous simplification:** Automating everything because it's cheaper.
- **MUST NOT infer:**
  - MUST NOT say automation removes governance (governance is re-placed at a higher level).
  - MUST NOT auto-appraise high-blast-radius actions without gates.

## Living Architecture

- **Source:** BOOK-DEFINED whole-system architecture; informed by NELL-01 (deployed
  continuous learning) and HIDDENTECH-01 (systems are webs of interdependent components)
- **Formal meaning:** A set of feedback loops over the subsystems: Knowledge Core ↔
  Acquisition (Ch7) ↔ Learning (Ch8) ↔ Retrieval/QA (Ch9) ↔ Observability & Monitoring ↔
  Assessment & Maintenance ↔ Governance & Audit (Ch6). Labeled BOOK ENGINEERING MODEL, not
  a product architecture.
- **Book wording:** "Kiến trúc sống (living architecture): các vòng phản hồi nối lõi tri
  thức, thu nạp, học, truy xuất, giám sát, bảo trì, quản trị — là mô hình kỹ thuật của
  sách, không phải kiến trúc sản phẩm cụ thể."
- **Dangerous simplification:** Photocopying this as a product blueprint.
- **MUST NOT infer:**
  - MUST NOT say this is a standard/industry architecture.
  - MUST NOT present the loops as a linear pipeline.

## Orchestration

- **Source:** BOOK-DEFINED; informed by HIDDENTECH-01 (component interactions must be
  managed); DRIFT-01 (change triggers)
- **Formal meaning:** Deciding when a QA failure triggers re-acquisition, when a source
  update triggers re-assessment, when an index lag triggers reindex, and the priority
  between competing actions. Orchestration defines trigger, authority, budget, and
  ordering; it does less automatically as stakes rise.
- **Book wording:** "Điều phối (orchestration): quyết định khi nào sự kiện kích hoạt hành
  động nào, ai có quyền, ngân sách bao nhiêu, ưu tiên ai — càng rủi ro cao càng ít tự động."
- **Dangerous simplification:** One big auto-everything loop.
- **MUST NOT infer:**
  - MUST NOT say orchestration removes per-action governance (rules are per-action, applied
    by the orchestrator).

---

## Terminology Collision Contract

These pairs must stay distinct throughout the chapter (each verified independently in the
records above; the table is the quick audit list).

| Distinction | First term | Second term | MUST NOT say |
|-------------|------------|-------------|--------------|
| Freshness ≠ Correctness | how recently validated | whether supported and true | "fresh ⟹ correct" |
| Monitoring ≠ Governance | detecting a problem | resolving it under authority | "system monitors itself ⟹ governs correctly" |
| Measured ≠ Understood | a number over a window | why the number changed | "measured ⟹ understood" |
| Feedback ≠ Evidence | user/loop signal | registered-source evidence | "users complained ⟹ false" |
| Versioned ≠ Verified | has a version number | checked against the version's content | "versioned ⟹ verified" |
| Auto-repair ≠ Auto-truth | a process was fixed | the fixed content is true | "repaired ⟹ correct" |
| Knowledge Debt ≠ Code Debt | epistemic obligations | engineering build cost | conflating the two |
| Collapse ≠ Staleness | degeneration by re-circulation | age-related lag | treating them as one failure |
| Trust ≠ Blind Trust | verifiable via audit | no further checking needed | "trustworthy ⟹ stop checking" |
| Maintenance ≠ Unreviewed Change | governed operation | unreviewed editing | "changed ⟹ maintained" |
| Quality Score ≠ Truth | metric of management behavior | truth about the world | "quality 0.92 ⟹ true" |
| System Health ≠ System Truth | status of processes | truth of content | "healthy ⟹ correct" |

---

## BOOK-DEFINED labels (required in manuscript)

The following MUST appear labeled as the book's own engineering model in
`book/chapter10.md`:

- Monitoring Loop
- Knowledge Debt (extended from HIDDENTECH-01's technical-debt framing to the epistemic domain)
- Contradiction Debt
- Living Architecture (BOOK ENGINEERING MODEL)
- Automation Gradient
- Audit Record schema
- Alert schema
- Quality-score model (five dimensions, adapted from KGQ-01/DQSTD-01)
