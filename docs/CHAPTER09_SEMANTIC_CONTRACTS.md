# Chapter 9 Semantic Contracts

Authoritative reference for every formal concept in Chapter 9. Each record specifies:

- **Source**: authoritative academic or primary reference
- **Formal meaning**: precise definition from the source
- **Book wording**: simplified phrasing used in the manuscript (Vietnamese)
- **Dangerous simplification**: what the book wording risks losing
- **MUST NOT infer**: claims the manuscript must never make

This document is the semantic contract against which `book/chapter09.md` is reviewed.
Concepts marked **BOOK-DEFINED** are the book's own engineering/pedagogical framework, not
an academic standard; they are labeled explicitly in the manuscript. Recurring sources:
RAG-01 (Lewis et al. 2020), DPR-01 (Karpukhin et al. 2020), GRAPHRAG-01 (Edge et al.
2024), BM25-01 (Robertson & Zaragoza 2009), IRBOOK-01 (Manning et al. 2008), NDCG-01
(Järvelin & Kekäläinen 2002), RRF-01 (Cormack et al. 2009), RRANK-01 (Nogueira & Cho
2019), LOSTMID-01 (Liu et al. 2024), AIS-01 (Rashkin et al. 2021), CITE-01 (Gao et al.
2023), KGQA-01 (Chakraborty et al. 2019), LLMKG-01 (Zhu et al. 2023), MAGRAPH-01
(Microsoft GraphRAG docs).

---

## Question Interpretation

- **Source:** BOOK-DEFINED (pipeline stage); informed by IRBOOK-01 "information need vs query"
- **Formal meaning:** Interpretation maps a natural-language question to a structured query intent — which entities/concepts are mentioned, what kind of question is being asked, and what evidence would be required. In IR, the user's real need (information need) is distinct from the literal query string; interpretation is a lossy, fallible inference.
- **Book wording:** "Diễn giải câu hỏi (question interpretation): chuyển câu hỏi tự nhiên thành intent có cấu trúc — thực thể, loại câu hỏi, bằng chứng cần thiết. Kết quả có thể sai."
- **Dangerous simplification:** Treating the parsed intent as guaranteed; assuming the query string equals the information need.
- **MUST NOT infer:**
  - MUST NOT say the interpreted intent is the user's true intent.
  - MUST NOT route a question without recording which interpretation was chosen.
  - MUST NOT present interpretation output as accepted knowledge (it is analysis, not a claim about the world).

## Query Intent

- **Source:** BOOK-DEFINED (structured classification of what the question asks); task taxonomy informed by KGQA-01
- **Formal meaning:** A structured label for the requested relation/operation (e.g., FACTUAL, STRUCTURAL, EXPLANATORY, PROVENANCE, TEMPORAL, CONTRADICTION, DISCOVERY, MULTI-HOP). Intent determines which retrieval plan and which knowledge target (canonical/ledger/historical) are appropriate.
- **Book wording:** "Intent truy vấn (query intent): câu hỏi muốn gì — sự kiện, cấu trúc, giải thích, nguồn gốc, lịch sử, mâu thuẫn, khám phá hay nhiều chặng."
- **Dangerous simplification:** One universal retrieve(question) ignoring intent; assuming intent follows from entities.
- **MUST NOT infer:**
  - MUST NOT use a single retrieval recipe for all question types.
  - MUST NOT say intent is fully determined by the named entities.
  - MUST NOT let intent label silently change the epistemic status of the answer.

## Entity Linking (query)

- **Source:** KGQA-01 (entity linking is a core KGQA subproblem); identity semantics from Ch3/Ch7 (fingerprint, sameAs, curated identity)
- **Formal meaning:** Mapping a mention in the question (e.g., "current") to candidate graph entities (ElectricCurrent, CurrentVersion, ...) and selecting/recording resolution with an ambiguity assessment. Candidate generation + contextual scoring + decision are separate steps.
- **Book wording:** "Liên kết thực thể truy vấn (query entity linking): mention → các ứng viên → chấm điểm ngữ cảnh → chọn/mờ. Không tự động lấy vector giống nhất."
- **Dangerous simplification:** Picking the highest embedding similarity without contextual assessment; silently assuming one mention = one entity.
- **MUST NOT infer:**
  - MUST NOT say the highest-similarity candidate is correct.
  - MUST NOT reuse Ch3 identity *resolution* as if it were query linking without adapting to the query context.
  - MUST NOT discard ambiguity (an ambiguous mention must be recorded, not hidden).

## Query Intent ≠ Entity Identity

- **Source:** BOOK-DEFINED; integration of Ch3 identity and KGQA-01 intent/linking separation
- **Formal meaning:** Linking resolves WHAT objects are mentioned; intent resolves WHAT relationship/operation is requested. Both can be ambiguous independently: "How does current change?" links to ElectricCurrent but may ask for derivative, causal driver, history, or classification.
- **Book wording:** "Việc 'đề cập đến ai' khác việc 'hỏi điều gì'. Cả hai đều có thể mơ hồ độc lập."
- **Dangerous simplification:** Assuming resolved entities determine the answer's shape.
- **MUST NOT infer:**
  - MUST NOT collapse identity resolution and intent classification into one step without justification.
  - MUST NOT say entity ambiguity and intent ambiguity always co-occur.

## Query Decomposition

- **Source:** BOOK-DEFINED (complex question → subquestions + dependencies); LLMKG-01/RAG-01 show multi-hop needs decomposition
- **Formal meaning:** Splitting a complex question into subquestions with explicit dependencies (e.g., Q1 structures, Q2 structures, Q3 shared mechanism, Q4 supporting claims, Q5 competing claims, Q6 synthesize). Decomposition is a plan, not a truth computation.
- **Book wording:** "Phân rã truy vấn (query decomposition): câu phức → câu con + phụ thuộc → kế hoạch truy xuất. Không phải câu hỏi nào cũng cần phân rã."
- **Dangerous simplification:** Decomposing every question; treating subanswers as independent truths.
- **MUST NOT infer:**
  - MUST NOT say decomposition output is the only valid reading.
  - MUST NOT assume subquestion answers compose into a true answer automatically.

## Retrieval Plan

- **Source:** BOOK-DEFINED; operation sequencing informed by RAG-01/DPR-01/GRAPHRAG-01
- **Formal meaning:** An ordered set of chosen retrieval operations (entity resolution, symbolic graph query, lexical, dense, hybrid, claim-ledger, temporal, provenance, contradiction) driven by the interpreted intent, with bounds and stopping conditions.
- **Book wording:** "Kế hoạch truy xuất (retrieval plan): chọn và sắp thứ tự các phép truy xuất theo intent, kèm giới hạn và điều kiện dừng."
- **Dangerous simplification:** A fixed pipeline applied to every question.
- **MUST NOT infer:**
  - MUST NOT say the plan guarantees completeness.
  - MUST NOT say a plan is correct just because it runs to completion.

## Retrieval Unit

- **Source:** BOOK-DEFINED (engineering concept); IRBOOK-01 (document as retrieval unit in classical IR)
- **Formal meaning:** The kind of object a retrieval step returns (entity, triple, Claim, Evidence, source passage, chunk, neighborhood, path, subgraph, community, canonical answer object). Unit choice determines recall, precision, context coherence, and provenance traceability.
- **Book wording:** "Đơn vị truy xuất (retrieval unit): 'mảnh' mà máy truy xuất trả về. Câu trả lời giải thích thường cần nhiều loại đơn vị phối hợp — claim chưa đủ nếu thiếu đoạn nguồn."
- **Dangerous simplification:** One unit fits all; retrieving claims without source passages for explanatory answers.
- **MUST NOT infer:**
  - MUST NOT say a single unit type suffices for all question types.
  - MUST NOT equate "unit retrieved" with "evidence sufficient".

## Retrieval Index ≠ Knowledge Graph

- **Source:** BOOK-DEFINED (index as access structure); IRBOOK-01 (inverted index as access structure, not the content itself)
- **Formal meaning:** A search/vector index is a derived access structure over KG content (serialized text, embeddings, labels, neighborhoods). It is not the canonical KG nor the Claim Ledger; it can lag behind them.
- **Book wording:** "Index truy xuất (index) là cấu trúc truy cập dẫn xuất từ KG — không phải KG, không phải Sổ cái; có thể tụt hậu."
- **Dangerous simplification:** Treating index contents as current KG state or as truth.
- **MUST NOT infer:**
  - MUST NOT say index state equals graph state.
  - MUST NOT say a passage found in the index is accepted knowledge.
  - MUST NOT ignore version/staleness of the index.

## Symbolic Graph Retrieval

- **Source:** SP11-01/SP11-02 (SPARQL exact query); KGQA-01 (semantic-parsing QA); Ch2 book model
- **Formal meaning:** Retrieving via an exact graph query (e.g., SPARQL BGP over pattern `?app operation DerivativeOperation; ...`) when schema, entities, and required relations are known. High precision and inspectability; limited to known wording/structure without mappings.
- **Book wording:** "Truy xuất đồ thị tượng trưng (symbolic graph retrieval): SPARQL/đường đi chính xác khi đã biết lược đồ, thực thể, quan hệ — chính xác nhưng kém linh hoạt với từ mới."
- **Dangerous simplification:** Using symbolic retrieval when the query mentions are unresolved; claiming SPARQL finds semantically similar text.
- **MUST NOT infer:**
  - MUST NOT say an exact graph result is semantically complete.
  - MUST NOT say SPARQL handles paraphrase/unknown vocabulary without mapping.
  - MUST NOT treat a query result as automatically true (it reflects what the KG asserts).

## Graph Traversal / Multi-hop Retrieval

- **Source:** BOOK-DEFINED; Ch2 graph walk concepts; KGQA-01 multi-hop path answering
- **Formal meaning:** Retrieval by walking edges across hops (Velocity ←produces Application →operation Derivative →classification RateOfChange). A path can exhibit structural explanation, but a path existing does not prove the conclusion.
- **Book wording:** "Truy xuất đa chặng (multi-hop retrieval): bước theo cạnh để nối câu trả lời cấu trúc. Có đường đi ≠ đã chứng minh kết luận."
- **Dangerous simplification:** Displaying a traversal as a proof.
- **MUST NOT infer:**
  - MUST NOT say a path is a logical derivation.
  - MUST NOT say path existence implies correctness of the relations.

## Path Length / Traversal Bounds

- **Source:** BOOK-DEFINED (epistemic boundary), continuing Ch7 top_k; informed by Ch2 path concepts
- **Formal meaning:** Graph traversal requires explicit bounds — max depth, allowed edge types, direction, node types, branching. Unbounded traversal explodes; too-tight bounds hide evidence. The hidden max-depth is an epistemic boundary just like top_k.
- **Book wording:** "Giới hạn độ sâu (depth bound) là ranh giới tri thức luận — quyết định mảnh cấu trúc nào được nhìn thấy."
- **Dangerous simplification:** Using an unstated depth and presenting results as complete.
- **MUST NOT infer:**
  - MUST NOT say "no result beyond depth d" means "no result exists".
  - MUST NOT hide the depth/edge filter from the reader.

## Relation-aware Traversal

- **Source:** BOOK-DEFINED (retrieval policy by intent)
- **Formal meaning:** Choosing which relation types to traverse based on intent — evidence questions traverse supports/derivedFrom/wasAttributedTo; mechanism-structure questions traverse operation/differentiand/withRespectTo/produces/instanceOf. Not all edges are equally useful.
- **Book wording:** "Traversal theo quan hệ (relation-aware): ưu tiên loại cạnh khớp intent — không đi mọi cạnh bừa bãi."
- **Dangerous simplification:** Traversing every relation and calling it thorough.
- **MUST NOT infer:**
  - MUST NOT say edge-type filtering discards all irrelevant structure (it may discard decisive paths).
  - MUST NOT claim one relation-priority set is universal.

## k-hop Neighborhood

- **Source:** BOOK-DEFINED; local-expansion idea in GRAPHRAG-01/Ch8 subgraph representation
- **Formal meaning:** All nodes/edges reachable within k hops of a seed. Naive k-hop expansion typically yields noise (units, books, authors, laws, domains ...) — only some neighbors are relevant, so expansion requires semantic filtering.
- **Book wording:** "Vùng lân cận k-chặng (k-hop neighborhood): mọi thứ trong phạm vi k cạnh — thường nhiễu, cần lọc theo ngữ nghĩa."
- **Dangerous simplification:** Feeding the whole neighborhood to the LLM as "relevant context".
- **MUST NOT infer:**
  - MUST NOT say within-k-hop equals relevant.
  - MUST NOT say further than-k-hop is irrelevant.

## Lexical Retrieval

- **Source:** IRBOOK-01 (term matching, inverted index, tf-idf/BM25); BM25-01
- **Formal meaning:** Retrieval by exact term/lexical matching with term-based weighting (e.g., BM25). Strong on exact terminology; weak on paraphrases/synonyms with no lexical overlap.
- **Book wording:** "Truy xuất từ vựng (lexical retrieval): khớp từ chính xác có trọng số — giỏi thuật ngữ đúng chữ, dốt đồng nghĩa/paraphrase."
- **Dangerous simplification:** Claiming lexical scores measure semantic relevance.
- **MUST NOT infer:**
  - MUST NOT say lexical match implies topical relevance (it is a signal).
  - MUST NOT treat BM25 score magnitude as confidence.

## BM25

- **Source:** BM25-01 (derivation and components); IRBOOK-01 (BM25 formulation)
- **Formal meaning:** score(D,Q) = Σ over matched terms of idf(t) · f(t,D)·(k1+1) / ( f(t,D) + k1·(1 − b + b·|D|/avgdl) ) with idf(t)=ln( (N − n_t + 0.5)/(n_t + 0.5) + 1 ). k1 saturates term frequency; b normalizes document length; idf downweights common terms.
- **Book wording:** "BM25 chấm mức khớp từ của tài liệu với câu hỏi: từ hiếm nặng hơn (idf), tần suất từ bão hòa (k1), độ dài tài liệu chuẩn hóa (b). Điểm là tiện ích xếp hạng, không phải xác suất đúng."
- **Dangerous simplification:** Reading BM25 scores as probabilities of relevance/truth.
- **MUST NOT infer:**
  - MUST NOT say BM25 score is a confidence/probability.
  - MUST NOT say BM25 captures semantics beyond term co-occurrence.
  - MUST NOT drop the length normalization intuition (docs of very different lengths are not comparable on raw tf alone).

## Dense Retrieval

- **Source:** DPR-01 (dual encoders, dot-product scores); Ch8 representation foundation
- **Formal meaning:** Map query and passage/entity to vectors (Dual Encoder: q = E_Q(query), p = E_P(passage)); score = dot(q,p) (or cosine). Can recover paraphrase similarity but high similarity is not relevance certainty and certainly not truth.
- **Book wording:** "Truy xuất mật độ (dense retrieval): câu hỏi và đoạn cùng vào vector, chấm bằng tích vô hướng. Bắt được paraphrase; nhưng giống không bằng đúng."
- **Dangerous simplification:** Ranking solely by embedding similarity and calling it relevance reasoning.
- **MUST NOT infer:**
  - MUST NOT say high embedding similarity guarantees relevance.
  - MUST NOT say dense retrieval always beats lexical retrieval.
  - MUST NOT treat the top dense hit as evidence.

## Query Embedding ≠ Query Meaning

- **Source:** DPR-01 (query encoder outputs a vector); Ch8 boundary (Entity ≠ Embedding generalized to queries)
- **Formal meaning:** The query embedding is one learned representation used for retrieval; it is not the complete semantics of the question. Different models/versions produce different rankings.
- **Book wording:** "Vector câu hỏi (query embedding) là biểu diễn dùng để truy xuất — không phải toàn bộ ý nghĩa câu hỏi."
- **Dangerous simplification:** Comparing embeddings as if they were exact meanings.
- **MUST NOT infer:**
  - MUST NOT say equal embeddings imply equal meaning.
  - MUST NOT treat a query-embedding comparison as semantic entailment.

## Hybrid Retrieval

- **Source:** BOOK-DEFINED synthesis; combines lexical (BM25-01/IRBOOK-01), dense (DPR-01), and graph constraints/traversal; fusion per RRF-01
- **Formal meaning:** Combining lexical + dense + graph signals (and possibly fusing their ranked lists via RRF) to improve robustness. Hybrid may help but is not universally superior.
- **Book wording:** "Truy xuất lai (hybrid retrieval): từ vựng + mật độ + ràng buộc/rãi đồ thị; gộp hạng có thể bền hơn nhưng không phải lúc nào cũng thắng."
- **Dangerous simplification:** Claiming more signals automatically mean better answers.
- **MUST NOT infer:**
  - MUST NOT say hybrid retrieval guarantees relevance or truth.
  - MUST NOT say hybrid is always better than each component.

## Rank Fusion (RRF)

- **Source:** RRF-01 (score = Σ 1/(k + rank_i(d)), k≈60)
- **Formal meaning:** Fusing multiple ranked lists by position: each system contributes 1/(k + rank_i(d)). Uses ranks, not raw scores; robust across incomparable scales.
- **Book wording:** "Hợp hạng (rank fusion): gộp nhiều danh sách hạng bằng nghịch đảo hạng — điểm hợp là tiện ích truy xuất, không phải độ tin cậy."
- **Dangerous simplification:** Treating the fused score as epistemic confidence.
- **MUST NOT infer:**
  - MUST NOT say fused rank is claim confidence.
  - MUST NOT say a document ranked first by fusion is evidence.

## Graph-first vs Text-first Retrieval

- **Source:** BOOK-DEFINED; both illustrated by GRAPHRAG-01 (local = graph-first) and RAG-01/DPR-01 (text-first)
- **Formal meaning:** Graph-first: question → entity linking → graph neighborhood → linked evidence passages. Text-first: question → passages → entities/claims → graph expansion. Mechanism questions often favor graph-first when schema is known; open definition questions favor text-first.
- **Book wording:** "Đồ thị trước hay văn bản trước tùy câu hỏi — không có bên nào luôn thắng."
- **Dangerous simplification:** Claiming graph-first is always better for KG-backed QA.
- **MUST NOT infer:**
  - MUST NOT say order of access determines truth.
  - MUST NOT claim a universal winner between graph-first and text-first.

## Claim-Ledger Retrieval vs Canonical-View Retrieval

- **Source:** BOOK-DEFINED; Ch6 Claim Ledger model (canonical view is a projection); mandated by spec
- **Formal meaning:** The Canonical View answers "what is accepted now"; the Claim Ledger answers "what has been claimed/proposed/contested/history". Retrieval target depends on epistemic intent — provenance/contradiction/history questions MUST NOT be answered from the canonical view only.
- **Book wording:** "Chiếu hình trả lời 'hiện được chấp nhận là gì'; Sổ cái trả lời 'đã từng được đề xuất/tranh cãi gì'. Hỏi lịch sử/mâu thuẫn phải vào Sổ cái."
- **Dangerous simplification:** Always retrieving the canonical view and silently dropping competing/historical claims.
- **MUST NOT infer:**
  - MUST NOT say canonical-view emptiness implies ledger emptiness.
  - MUST NOT say the accepted definition is the only definition ever proposed.

## Governance-aware Retrieval

- **Source:** BOOK-DEFINED; Ch6 governance states continued
- **Formal meaning:** Retrieval can be filtered/allowed by governance state (Accepted/Candidate/Contested/Rejected/Superseded) according to intent: production facts prefer Accepted; research/audit include Contested/Superseded; historical questions include temporal versions. Non-Accepted claims are not silently discarded.
- **Book wording:** "Truy xuất theo trạng thái quản trị: câu hỏi sản xuất ưu tiên Accepted; câu hỏi nghiên cứu phải kể cả Contested/Superseded."
- **Dangerous simplification:** Filtering out all non-Accepted claims for every question.
- **MUST NOT infer:**
  - MUST NOT say Rejected implies false in the world.
  - MUST NOT say Accepted implies true (it is governed, not guaranteed).

## Temporal Retrieval

- **Source:** BOOK-DEFINED; Ch6 multiple-clock model (system/valid/publication/transaction time)
- **Formal meaning:** "What did the system believe in 2024?" = system/transaction-time view; "what definition applied in 2024?" = valid/reference time; "what was published in 2024?" = publication/assertion time. These are different clocks and MUST NOT be collapsed.
- **Book wording:** "Có nhiều đồng hồ: lúc tin, lúc hiệu lực, lúc công bố — không gộp làm một."
- **Dangerous simplification:** Answering a historical question with the current canonical view.
- **MUST NOT infer:**
  - MUST NOT say current truth was believed in the past.
  - MUST NOT collapse valid time and publication time.

## Provenance-aware Retrieval

- **Source:** BOOK-DEFINED; Ch6 PROV lineage (wasGeneratedBy, wasDerivedFrom, wasAttributedTo); AIS-01 (attribution to sources)
- **Formal meaning:** "Why does the system believe X?" requires retrieving the Claim → Evidence → SourceFragment → SourceArtifact chain + extraction/integration provenance + assessments/governance, assembled into an explanation subgraph.
- **Book wording:** "Truy xuất nguồn gốc (provenance): claim → bằng chứng → đoạn → tài liệu nguồn → tuyến tích hợp, để trả lời 'vì sao tin X'."
- **Dangerous simplification:** Answering "why" with the canonical triple only.
- **MUST NOT infer:**
  - MUST NOT say provenance existence proves correctness.
  - MUST NOT treat a source fragment as independent of its upstream extraction.

## Contradiction-aware Retrieval

- **Source:** BOOK-DEFINED; Ch6 contradiction model; required by Ch9 spec
- **Formal meaning:** When a question touches a contested concept, retrieve relevant competing claims and preserve their scopes rather than returning only the top-supported claim. Do not force the LLM to pick a winner without policy/evidence.
- **Book wording:** "Truy xuất nhạy mâu thuẫn: nếu khái niệm đang tranh cãi, hãy lấy cả các claim đối lập cùng phạm vi của chúng."
- **Dangerous simplification:** Retrieving one accepted claim and hiding the dispute.
- **MUST NOT infer:**
  - MUST NOT say the higher-ranked source is right.
  - MUST NOT merge contradictory claims without preserving scopes.

## Candidate Evidence (Retrieved ≠ Evidence)

- **Source:** AIS-01 (attribution is judged, not automatic); BOOK-DEFINED
- **Formal meaning:** A retrieved passage is a candidate until assessed: relevant to claim/question, interpreted correctly, scope aligned. Not every retrieved chunk deserves the label Evidence.
- **Book wording:** "Đoạn truy xuất được (retrieved) chỉ là ứng viên; thành bằng chứng (evidence) khi được đánh giá phù hợp."
- **Dangerous simplification:** Calling all retrieved items "Evidence".
- **MUST NOT infer:**
  - MUST NOT say retrieval success implies evidentiary value.
  - MUST NOT say relevance assessment is infallible.

## top_k as an Epistemic Bound

- **Source:** BOOK-DEFINED (deepening Ch7 bounds); RAG-01/DPR-01 use fixed top-k
- **Formal meaning:** The LLM can only reason over evidence it sees; top_k=5 missing the decisive #6 passage changes the operational boundary of knowability. Larger k is not always better (noise, distractors).
- **Book wording:** "top_k là ranh giới tri thức luận: mô hình không suy luận được trên bằng chứng nó không thấy. Lớn hơn không hẳn tốt hơn."
- **Dangerous simplification:** Treating top_k as neutral plumbing.
- **MUST NOT infer:**
  - MUST NOT say "not in top_k" implies "not relevant/absent".
  - MUST NOT say increasing top_k monotonically improves answers.

## Recall

- **Source:** IRBOOK-01 (recall = |relevant ∩ retrieved| / |relevant|)
- **Formal meaning:** Fraction of relevant items that were retrieved. High recall matters for contradictions, evidence, multi-hop explanations; huge recall with low precision harms synthesis.
- **Book wording:** "Độ bao phủ (recall): trong số cái đáng lấy, đã lấy được bao nhiêu — câu hỏi giải thích cần recall cao."
- **Dangerous simplification:** Chasing recall without regard to precision.
- **MUST NOT infer:**
  - MUST NOT say recall=1 implies the answer is complete/true.
  - MUST NOT measure recall without a relevance gold set (BOOK-DEFINED or annotation).

## Precision

- **Source:** IRBOOK-01 (precision = |relevant ∩ retrieved| / |retrieved|)
- **Formal meaning:** Fraction of retrieved items that are relevant. High precision reduces synthesis noise; low precision can overwhelm the LLM with distractors.
- **Book wording:** "Độ chính xác (precision): trong số lấy được, bao nhiêu là đúng chỗ — lấy nhiều rác thì tổng hợp kém."
- **Dangerous simplification:** Assuming high precision implies high answer truth.
- **MUST NOT infer:**
  - MUST NOT say precision measures factual correctness.
  - MUST NOT compare precision scores across different relevance definitions.

## Precision@K / Recall@K

- **Source:** IRBOOK-01 (ranked cutoff metrics); BOOK-DEFINED worked example
- **Formal meaning:** P@K = relevant among top-K / K; R@K = relevant among top-K / total relevant.
- **Book wording:** "Ví dụ 8 đoạn liên quan, top-5 lấy 4 → P@5=0.8, R@5=0.5. P@K nhìn chất lượng đầu danh sách; R@K nhìn độ phủ bị cắt."
- **Dangerous simplification:** Using P@K alone on high-recall questions.
- **MUST NOT infer:**
  - MUST NOT say P@K is truth.
  - MUST NOT compute these against an unbounded gold set (needs K and gold relevance).

## MRR

- **Source:** IRBOOK-01 / NICKEL-01 (rank of first relevant result); reused from Ch8 link prediction, now for retrieval
- **Formal meaning:** Mean reciprocal rank = average over queries of 1/rank of the first relevant result. Appropriate when the first relevant result matters.
- **Book wording:** "MRR đo vị trí kết quả đúng đầu tiên — phù hợp khi người dùng cần cái đúng sớm nhất."
- **Dangerous simplification:** Using MRR when graded relevance matters more.
- **MUST NOT infer:**
  - MUST NOT say MRR measures answer correctness.
  - MUST NOT reuse Ch8's MRR claims as retrieval truth (different task).

## nDCG

- **Source:** NDCG-01 (graded relevance, log discount, normalization by ideal)
- **Formal meaning:** DCG = Σ rel_i / log2(i+1); nDCG = DCG/IDCG. Measures ranking quality with graded relevance against an ideal ordering.
- **Book wording:** "nDCG chấm chất lượng xếp hạng theo độ liên quan bậc thang, chiết khấu theo vị trí, chuẩn hóa với thứ tự lý tưởng."
- **Dangerous simplification:** Treating nDCG as epistemic confidence.
- **MUST NOT infer:**
  - MUST NOT say nDCG is truth/correctness.
  - MUST NOT compare nDCG across different relevance scales.

## Reranking

- **Source:** RRANK-01 (two-stage: BM25 first stage → cross-encoder re-ranking; MRR@10 gains)
- **Formal meaning:** First stage is fast/broad/high-recall (e.g., 100–1000 candidates); second stage re-scores query–candidate pairs jointly (cross-encoder, LLM, graph-aware score, filter). Reranking cannot recover what the first stage missed.
- **Book wording:** "Tái xếp hạng (reranking): giai đoạn đầu lấy rộng, giai đoạn hai so từng cặp lại cho sắc. Không hồi phục được thứ tầng một bỏ sót."
- **Dangerous simplification:** Expecting reranking to fix recall failures.
- **MUST NOT infer:**
  - MUST NOT say reranker score is confidence.
  - MUST NOT say LLM reranking guarantees correctness.

## Reranking with Graph Features

- **Source:** BOOK-DEFINED (policy/task dependent; no single universal formula)
- **Formal meaning:** Graph distance, relation type, shared Mechanism, governance state, provenance availability, temporal alignment, source diversity may inform relevance — combined per policy, not one fixed weighted equation.
- **Book wording:** "Đặc trưng đồ thị có thể góp vào đánh giá liên quan — theo chính sách từng bài toán, không có công thức trọng số phổ quát."
- **Dangerous simplification:** Publishing one arbitrary weighted formula as canonical.
- **MUST NOT infer:**
  - MUST NOT say graph features are inherently superior to text features.
  - MUST NOT treat the reranking combination as a truth measure.

## Context Assembly

- **Source:** BOOK-DEFINED; LOSTMID-01 (order/placement affects reliability); RAG-01 (prompt = query + retrieved passages)
- **Formal meaning:** Constructing the LLM's input from ranked retrieval: select items (triples, Claims, passages, provenance, contradictions, temporal metadata), group, and order them. Assembly is a reasoning interface, not mere concatenation.
- **Book wording:** "Lắp ráp ngữ cảnh (context assembly): chọn, nhóm, sắp thứ tự bằng chứng thành đầu vào mô hình — thứ tự ảnh hưởng độ tin cậy."
- **Dangerous simplification:** Concat everything retrieved in any order.
- **MUST NOT infer:**
  - MUST NOT say assembly order has no effect.
  - MUST NOT say more context equals more knowledge.

## Context Compression

- **Source:** BOOK-DEFINED (duplicate removal, summarization, representative selection); GRAPHRAG-01 (community summaries); AIS-01 (derived artifacts)
- **Formal meaning:** Reducing large evidence sets to fit the window: dedupe, summarize neighborhoods, preserve key paths, choose representative evidence. Compression may discard decisive evidence; compressed artifacts should keep provenance links.
- **Book wording:** "Nén ngữ cảnh (context compression): bỏ trùng, tóm tắt, giữ đường đi quyết định — nhưng nén có thể vứt bằng chứng quyết định."
- **Dangerous simplification:** Treating the compressed summary as equivalent to the source.
- **MUST NOT infer:**
  - MUST NOT say a summary is the source.
  - MUST NOT say compression preserves all evidence.

## Context Window ≠ Knowledge

- **Source:** BOOK-DEFINED (KG state ≠ LLM-visible context); central to RAG/GraphRAG
- **Formal meaning:** The system may hold millions of claims; the LLM sees only assembled context. Correct KG + wrong retrieval ⇒ wrong answers even though knowledge is intact.
- **Book wording:** "Cửa sổ ngữ cảnh ≠ tri thức: KG có thể đúng mà câu trả lời vẫn sai vì chỉ nhìn thấy một phần."
- **Dangerous simplification:** Assuming the LLM "knows" whatever the KG contains.
- **MUST NOT infer:**
  - MUST NOT say KG correctness implies answer correctness.
  - MUST NOT say retrieval context is a sample of the whole knowledge.

## Graph Serialization for LLM Context

- **Source:** BOOK-DEFINED (format tradeoffs); RAG-01/GRAPHRAG-01 (how graph info is placed into prompts)
- **Formal meaning:** Graph knowledge can be presented as triples, tables, JSON, compact NL, paths, or structured evidence cards. Raw RDF is precise but token-heavy; NL summaries are compact but lose structure. Representation choice is a task-dependent tradeoff.
- **Book wording:** "Cùng một cấu trúc cơ chế có thể viết thành triple, bảng, JSON, hay lời văn gọn — chính xác thì dài, gọn thì mất cấu trúc."
- **Dangerous simplification:** Picking one serialization for all questions.
- **MUST NOT infer:**
  - MUST NOT say a serialization preserves all semantics.
  - MUST NOT say NL rendering is lossless.

## Evidence Packet

- **Source:** BOOK-DEFINED (BOOK ENGINEERING MODEL — interface between retrieval and synthesis)
- **Formal meaning:** A structured container for one QA request: Question, resolved entities, query intent, relevant canonical claims, competing claims, graph paths, source passages, provenance, temporal scope, assessments, retrieval metadata. It carries statuses (asserted/derived/predicted).
- **Book wording:** "Gói bằng chứng (evidence packet) là giao diện giữa tầng truy xuất và tầng sinh câu trả lời — BOOK ENGINEERING MODEL."
- **Dangerous simplification:** Feeding raw retrieved chunks straight to the LLM and calling that a packet.
- **MUST NOT infer:**
  - MUST NOT say a filled packet guarantees sufficiency.
  - MUST NOT say packet contents are true.

## Answer Generation

- **Source:** RAG-01 (generator over retrieved context); BOOK-DEFINED (evidence-packet-driven synthesis)
- **Formal meaning:** The generator maps the Evidence Packet to an answer draft, able to summarize, compare, explain paths, or render formal relations in prose — without inventing unsupported relations. The draft distinguishes supported statements, inferences, uncertainty, and unknown.
- **Book wording:** "Sinh câu trả lời (answer generation): từ gói bằng chứng ra bản nháp — tóm tắt, so sánh, giải thích đường đi; phân biệt 'được hỗ trợ', 'suy luận', 'không chắc', 'chưa biết'."
- **Dangerous simplification:** Letting the model output extra relations beyond the packet.
- **MUST NOT infer:**
  - MUST NOT say generated text is verified against the world.
  - MUST NOT say a fluent answer is grounded.

## Answer Claim

- **Source:** BOOK-DEFINED (answer decomposes into claims); CITE-01 (per-statement citation evaluation)
- **Formal meaning:** An answer can be decomposed into AnswerClaims A1, A2, ... each traceable to evidence/path/derivation/accepted claim, enabling citation and grounding checks.
- **Book wording:** "Câu trả lời chứa các claim con — mỗi claim phải vết được về bằng chứng/đường đi/câu chấp nhận."
- **Dangerous simplification:** Treating the answer as one indivisible unit.
- **MUST NOT infer:**
  - MUST NOT say every answer claim is externally verifiable.
  - MUST NOT say an answer with one cited claim is fully cited.

## Grounded Answer

- **Source:** AIS-01 (attribution to identified sources); BOOK-DEFINED (groundedness)
- **Formal meaning:** A grounded answer is supported by retrieved system evidence/sources (AIS-supportable). Grounding does NOT mean the answer is true — the evidence itself may be incorrect, outdated, contested, or misinterpreted.
- **Book wording:** "Câu trả lời có căn cứ (grounded): được bằng chứng đã lấy hỗ trợ. Có căn cứ ≠ đúng — bằng chứng cũng có thể sai."
- **Dangerous simplification:** Groundedness as a proxy for truth.
- **MUST NOT infer:**
  - MUST NOT say grounded ⇒ true.
  - MUST NOT say ungrounded ⇒ false.

## Citation

- **Source:** CITE-01 (citation recall/precision); AIS-01 (support judgment); BOOK-DEFINED mechanics
- **Formal meaning:** A citation points from an answer claim to the actual supporting evidence and its source. It must not cite a document merely because it was retrieved, or a source that does not support the sentence.
- **Book wording:** "Trích dẫn (citation): gắn từng claim với bằng chứng/n guồn thật hỗ trợ nó — không trích vì 'nó được truy xuất'."
- **Dangerous simplification:** Auto-citing retrieved documents wholesale.
- **MUST NOT infer:**
  - MUST NOT say citation presence proves support.
  - MUST NOT say every retrieved document is citable.

## Citation Completeness

- **Source:** CITE-01 (citation recall = coverage of statements); BOOK-DEFINED
- **Formal meaning:** Does every externally checkable important answer claim carry supporting evidence? Citation coverage/completeness is the fraction of claims that are supported/cited.
- **Book wording:** "Trích dẫn phải phủ mọi claim quan trọng — hai claim đúng trích dẫn nhưng claim thứ ba thiếu thì vẫn chưa đủ."
- **Dangerous simplification:** Counting citations without checking claim-by-claim coverage.
- **MUST NOT infer:**
  - MUST NOT say "has citations" means "all claims cited".
  - MUST NOT equate citation density with citation quality.

## Faithfulness

- **Source:** AIS-01/RAG terminology (answer remains supported by supplied context); BOOK-DEFINED for the book's meaning
- **Formal meaning:** Faithfulness = the answer does not contradict/hallucinate beyond the supplied retrieved context. It is a relation between answer and provided context, NOT between answer and the real world. A faithfully summarized wrong source is still wrong.
- **Book wording:** "Trung thành (faithful): câu trả lời không bịa ngoài ngữ cảnh đã cấp. Nhưng trung thành với nguồn sai vẫn sai."
- **Dangerous simplification:** Faithfulness = factual correctness.
- **MUST NOT infer:**
  - MUST NOT say faithful ⇒ correct.
  - MUST NOT say unfaithful to context ⇒ actually false.

## Answer Correctness vs Groundedness (2×2)

- **Source:** BOOK-DEFINED; built from AIS-01 + CITE-01 grounding/truth distinction
- **Formal meaning:** Four cells: A = factually correct but unsupported by retrieved context; B = faithful to retrieved source but source wrong; C = supported and correct (goal); D = unsupported and wrong. Evaluation must separate the axes.
- **Book wording:** "Bảng 2×2: đúng-thế-giới ≠ có-căn-cứ-trong-ngữ-cảnh. Chỉ C là mục tiêu; B vẫn 'trung thành nhưng sai'."
- **Dangerous simplification:** Collapsing the two axes into one score.
- **MUST NOT infer:**
  - MUST NOT say a grounded answer is necessarily in cell C.
  - MUST NOT grade only one axis.

## Abstention

- **Source:** BOOK-DEFINED (epistemic behavior); OWA from Ch6/Ch8 (absence ≠ false)
- **Formal meaning:** When evidence is insufficient (no relevant claim, unresolved entity, contradiction, insufficient support, retrieval uncertainty, out of scope), the system should say "không đủ bằng chứng" rather than fabricate.
- **Book wording:** "Kiêng trả lời (abstention): đủ điều kiện thiếu bằng chứng thì nói 'chưa đủ', không bịa câu trả lời có vẻ hợp lý."
- **Dangerous simplification:** Abstaining too early (index miss ≠ knowledge miss).
- **MUST NOT infer:**
  - MUST NOT say abstention means the fact is false.
  - MUST NOT say abstention is an answer failure by itself (it may be the correct behavior).

## Unknown vs Not Found

- **Source:** BOOK-DEFINED; Ch6 OWA (not stated ≠ false)
- **Formal meaning:** NOT FOUND BY THIS RETRIEVAL ≠ NOT IN INDEX ≠ NOT IN KG ≠ KNOWN FALSE ≠ UNKNOWN. These are distinct epistemic states and retrieval output must label which one holds.
- **Book wording:** "'Không truy xuất được' khác 'không tồn tại' khác 'đã biết sai' khác 'chưa biết' — phải nói rõ loại nào."
- **Dangerous simplification:** "No result" ⇒ "absent".
- **MUST NOT infer:**
  - MUST NOT say absence of retrieval is absence of knowledge.
  - MUST NOT say not-found is false.

## Retrieval Failure vs Knowledge Absence

- **Source:** BOOK-DEFINED (diagnostics); RAG/DPR architecture (retrieval is separable from knowledge)
- **Formal meaning:** If the correct Claim exists in the Ledger but the retriever misses it, the failure is retrieval-side, not knowledge-side. Diagnostics must separate them.
- **Book wording:** "Claim đúng có trong Sổ cái mà máy truy xuất bỏ sót → đó là lỗi truy xuất, không phải thiếu tri thức."
- **Dangerous simplification:** Blaming the KG for retrieval misses.
- **MUST NOT infer:**
  - MUST NOT say answer failure implies knowledge failure.
  - MUST NOT fix knowledge when the fix should be retrieval configuration.

## Query Planning

- **Source:** BOOK-DEFINED (plan = ordered retrieval operations); KGQA-01 (query construction)
- **Formal meaning:** Given structured intent, choose the retrieval operations and order (resolve entities → retrieve applications → find mechanism → roles → claims → passages → competing claims → assemble). The planner may be rules, an LLM, or an agent.
- **Book wording:** "Lập kế hoạch truy vấn (query planning): chọn thứ tự phép truy xuất theo intent — không bắt buộc do LLM lập kế hoạch."
- **Dangerous simplification:** Assuming an LLM must always plan.
- **MUST NOT infer:**
  - MUST NOT say the plan is deterministic truth.
  - MUST NOT say any planner is infallible.

## Agentic / Iterative Retrieval

- **Source:** BOOK-DEFINED (retrieve → inspect → refine → repeat); informed by RAG-01 (fixed pass) as contrast
- **Formal meaning:** Dynamic retrieval: after a pass, detect gaps and issue follow-up queries. Benefits multi-step questions; risks loops, query drift, noise escalation, cost, and confirmation bias. Not automatically superior to static retrieval.
- **Book wording:** "Truy xuất lặp (agentic retrieval): lấy → thấy thiếu → lấy tiếp. Hữu ích cho câu đa bước nhưng dễ trôi câu hỏi/tốn chi phí."
- **Dangerous simplification:** “More passes = better”.
- **MUST NOT infer:**
  - MUST NOT say iterative retrieval guarantees better answers.
  - MUST NOT say more retrieval is always justified.

## Stopping Condition

- **Source:** BOOK-DEFINED (termination policy)
- **Formal meaning:** Agentic retrieval stops when: required evidence slots filled, no new relevant info, explicit relevance threshold, budget exhausted, or contradiction requires human review. No "search more just in case".
- **Book wording:** "Phải có điều kiện dừng rõ: đủ ô bằng chứng, hết ngân sách, hay hết thông tin mới."
- **Dangerous simplification:** Endless iterative refinement.
- **MUST NOT infer:**
  - MUST NOT say a stopped search is complete.
  - MUST NOT say budget-limited results are exhaustive.

## Query Drift

- **Source:** BOOK-DEFINED (failure mode)
- **Formal meaning:** Successive subqueries drift from the original intent (RATE_OF_CHANGE → derivative → calculus → finance), degrading relevance. Preserve the original query representation and subquery provenance.
- **Book wording:** "Trôi câu hỏi (query drift): mỗi vòng lại lệch xa intent gốc — phải giữ bản gốc và vết con của subquery."
- **Dangerous simplification:** Ignoring that later retrievals changed the question.
- **MUST NOT infer:**
  - MUST NOT say later retrievals are evaluating the original question.

## Confirmation Bias in Retrieval

- **Source:** BOOK-DEFINED (failure mode tied to Ch8 hypotheses)
- **Formal meaning:** If the system starts with a hypothesis (Velocity and Current share RATE_OF_CHANGE), one-sided retrieval returns only supporting evidence. Robust explanatory retrieval also retrieves counterexamples, competing mechanisms, and boundary definitions.
- **Book wording:** "Thiên kiến xác nhận (confirmation bias): chỉ lấy bằng chứng ủng hộ giả thuyết — lược bỏ phản ví dụ là thiếu."
- **Dangerous simplification:** Treating supporting-only retrieval as thorough.
- **MUST NOT infer:**
  - MUST NOT say hypothesis-support implies hypothesis truth.

## Hypothesis-testing Retrieval

- **Source:** BOOK-DEFINED; bridge to Ch8 CandidateMechanismHypothesis; GRAPHRAG-01/Ch8 hard negatives
- **Formal meaning:** Retrieval becomes a hypothesis-testing interface: given a candidate mechanism hypothesis, retrieve both supporting evidence and challenging evidence (hard negatives: finite difference, ratio, gradient, accumulation).
- **Book wording:** "Truy xuất kiểm định giả thuyết: với giả thuyết cơ chế, lấy cả ủng hộ lẫn thách thức — phản ví dụ là dữ liệu chính."
- **Dangerous simplification:** Using retrieval to confirm rather than test.
- **MUST NOT infer:**
  - MUST NOT say absence of challenge implies hypothesis accepted.
  - MUST NOT say a tested-by-retrieval hypothesis is accepted knowledge.

## Local vs Global Questions

- **Source:** GRAPHRAG-01 (local vs global query modes); BOOK-DEFINED
- **Formal meaning:** LOCAL = about a specific entity/subgraph (needs entity-anchored retrieval). GLOBAL = patterns across the graph/corpus (may need hierarchical/community or aggregate strategies). Different retrieval strategies are needed.
- **Book wording:** "Câu hỏi cục bộ (local) về một thực thể; câu hỏi toàn cục (global) về mô hình chung — chiến lược truy xuất khác nhau."
- **Dangerous simplification:** One retrieval strategy for both.
- **MUST NOT infer:**
  - MUST NOT say global answers exist per-entity.
  - MUST NOT say local retrieval suffices for global questions.

## GraphRAG (family of architectures)

- **Source:** GRAPHRAG-01 (primary); MAGRAPH-01 (one implementation); LLMKG-01 (positioning)
- **Formal meaning:** GraphRAG broadly = retrieval-augmented generation approaches that use explicit graph structure during retrieval/context construction/reasoning, rather than relying only on independent text chunks. It is a family of architectures, not one standard.
- **Book wording:** "GraphRAG là họ kiến trúc dùng cấu trúc đồ thị khi truy xuất/ghép ngữ cảnh — không phải một thuật toán chuẩn duy nhất."
- **Dangerous simplification:** Presenting Microsoft GraphRAG as THE definition.
- **MUST NOT infer:**
  - MUST NOT say GraphRAG is one standardized algorithm.
  - MUST NOT say GraphRAG guarantees better QA.
  - MUST NOT say GraphRAG eliminates hallucination.

## KGQA vs Text RAG vs GraphRAG

- **Source:** KGQA-01 (KGQA = structured query over the graph); RAG-01 (text RAG); GRAPHRAG-01 (graph-assisted context)
- **Formal meaning:** KGQA answers via structured query/reasoning on the graph; text RAG retrieves chunks and generates; GraphRAG uses graph structure to retrieve/assemble context for generation. They overlap but are not identical.
- **Book wording:** "KGQA trả lời bằng truy vấn cấu trúc; text RAG truy xuất đoạn rồi sinh; GraphRAG dùng đồ thị để điều hướng truy xuất — ba cơ chế khác nhau."
- **Dangerous simplification:** Calling any graph-influenced RAG "KGQA".
- **MUST NOT infer:**
  - MUST NOT say KGQA = GraphRAG.
  - MUST NOT say a deterministic SPARQL question needs RAG.

## Subgraph Retrieval

- **Source:** BOOK-DEFINED; GRAPHRAG-01 (coherent neighborhoods); Ch8 subgraph representation
- **Formal meaning:** Retrieving a coherent subgraph (target applications, shared Mechanism, role objects, claims, evidence, source fragments) rather than isolated paths — for coherent context. Subgraph selection is itself a retrieval/optimization problem.
- **Book wording:** "Truy xuất đồ thị con (subgraph): lấy một khối cấu trúc gắn kết thay vì các đường rời — gắn kết hơn, nhưng chọn đồ thị con là bài toán riêng."
- **Dangerous simplification:** Treating any connected set as "the evidence subgraph".
- **MUST NOT infer:**
  - MUST NOT say a retrieved subgraph is minimal/sufficient by default.
  - MUST NOT say subgraph existence implies relevance of all its edges.

## Minimal Sufficient Subgraph

- **Source:** BOOK-DEFINED (engineering intuition; no universal computable minimum claimed)
- **Formal meaning:** Retrieve enough structure to support the answer while avoiding irrelevant expansion. For "Why Velocity = RATE_OF_CHANGE?", the minimal useful structure includes the application, operation, role objects, mechanism, classification claim, and a supporting source passage.
- **Book wording:** "Đồ thị con đủ tối thiểu: đủ cấu trúc để trả lời, không lan tràn. Không tuyên bố tối ưu toàn cục."
- **Dangerous simplification:** Claiming a computable universal minimum.
- **MUST NOT infer:**
  - MUST NOT say a chosen subgraph is provably minimal.
  - MUST NOT say more structure always helps.

## Community / Hierarchical Retrieval

- **Source:** GRAPHRAG-01 (Leiden communities, bottom-up summaries); MAGRAPH-01 (Global Search)
- **Formal meaning:** Organizing a large graph into communities and summarizing them hierarchically to answer global questions. Risks: summary information loss, community instability, stale summaries, lost provenance, cross-community evidence.
- **Book wording:** "Truy xuất cộng đồng (community retrieval): gom nhóm + tóm tắt theo cấp để trả lời câu hỏi toàn cục — nhưng tóm tắt có thể mất bằng chứng."
- **Dangerous simplification:** Community summaries as mandatory or lossless.
- **MUST NOT infer:**
  - MUST NOT say community summarization is required GraphRAG architecture.
  - MUST NOT say summaries are complete.

## Generated Summary (as Derived Knowledge)

- **Source:** AIS-01/GRAPHRAG-01/MAGRAPH-01 (summaries are LLM-generated artifacts); Ch7 provenance model
- **Formal meaning:** A community/vicinity summary is a derived artifact with provenance (which text units, which model, which version). Summary ≠ source truth; generated summaries must not silently become canonical knowledge.
- **Book wording:** "Tóm tắt là đồ tạo tác dẫn xuất — có nguồn gốc, có phiên bản; là đầu vào ứng viên, không phải chân lý."
- **Dangerous simplification:** Storing summaries as canonical.
- **MUST NOT infer:**
  - MUST NOT say a summary equals its sources.
  - MUST NOT insert a summary into the canonical KG without governance.

## Caching

- **Source:** BOOK-DEFINED (supporting engineering concept; staleness tradeoff)
- **Formal meaning:** Query resolution, retrieval results, subgraphs, summaries, and answers may be cached. Since the Knowledge System evolves, cache keys may need to include KG snapshot/version, index version, ontology version, retriever version.
- **Book wording:** "Cache có thể cũ khi hệ tri thức đổi — khóa cache cần gắn phiên bản KG/index/ontology."
- **Dangerous simplification:** Serving stale cached answers as current.
- **MUST NOT infer:**
  - MUST NOT say a cached answer reflects current knowledge.
  - MUST NOT ignore version in cache keys where it matters.

## Index Consistency / Staleness

- **Source:** BOOK-DEFINED (index ≠ KG, from Retrieval Index contract)
- **Formal meaning:** If the Claim Ledger changes but the vector index does not, the retriever sees a stale world. Distinguish: KG current state, index state, LLM-visible state.
- **Book wording:** "Index cũ ≠ KG mới: pipeline 'kỹ thuật đúng' vẫn có thể trả lời dữ liệu cũ."
- **Dangerous simplification:** Assuming index freshness.
- **MUST NOT infer:**
  - MUST NOT say index state is current.
  - MUST NOT blame the answer model for stale-index errors.

## Retrieval Provenance

- **Source:** BOOK-DEFINED (why evidence was shown to the model)
- **Formal meaning:** Recording query, interpretation, retrievers/versions, index snapshot, filters, top_k, scores, reranker, expansion rules, timestamps — enough for reproducibility/debugging; not everything forever by decree.
- **Book wording:** "Provenance truy xuất: ghi đủ để tái hiện 'vì sao mảnh này được đưa cho mô hình'."
- **Dangerous simplification:** Storing nothing about retrieval and calling the answer audit-able.
- **MUST NOT infer:**
  - MUST NOT say retrieval provenance proves correctness.
  - MUST NOT say recorded scores are the answer's confidence.

## Answer Provenance (Answer artifact)

- **Source:** BOOK-DEFINED (BOOK ENGINEERING MODEL); PROV-O from Ch6
- **Formal meaning:** An Answer record: generatedFor → Question; usedEvidence → EvidencePacket; generatedBy → activity; generatedAt; modelVersion; prompt/config version; citations; answerStatus. Not automatically inserted into canonical knowledge.
- **Book wording:** "Hồ sơ câu trả lời (answer provenance) ghi: cho câu hỏi nào, dùng gói bằng chứng nào, mô hình/phiên bản nào, trạng thái gì."
- **Dangerous simplification:** Storing answers without provenance and reusing them as knowledge.
- **MUST NOT infer:**
  - MUST NOT say an Answer is an accepted Claim.
  - MUST NOT say provenance makes it true.

## QA Answer ≠ Knowledge Ingestion

- **Source:** BOOK-DEFINED (mandatory boundary); Ch7 integration pipeline (only governed candidates enter the ledger)
- **Formal meaning:** An LLM answer is not automatically new accepted KG knowledge. If it reveals candidate knowledge, route Answer → CandidateClaim → Ch7/Ch6 integration pipeline. No circular KG → answer → insert → KG without governance.
- **Book wording:** "Câu trả lời QA không tự thành tri thức mới — chỉ vào Sổ cái qua tuyến ứng viên có quản trị."
- **Dangerous simplification:** Feeding answers straight back into the KG.
- **MUST NOT infer:**
  - MUST NOT say "the system answered it, so it knows it".
  - MUST NOT insert answers bypassing governance.

## Retrieval Score Semantics

- **Source:** BOOK-DEFINED; BM25-01 (BM25 ranking utility), DPR-01 (dot-product signal), RRF-01 (fused rank)
- **Formal meaning:** BM25 scores, cosine similarity, reranker scores, graph proximity, and rule priority are different ranking signals. None is inherently a probability that the answer is true.
- **Book wording:** "BM25, cosine, reranker, khoảng cách đồ thị — đều là tín hiệu xếp hạng, không phải xác suất đúng."
- **Dangerous simplification:** Persisting a retrieval score as confidence.
- **MUST NOT infer:**
  - MUST NOT say a high score implies truth.
  - MUST NOT compare score types as if on one scale.

## Multi-signal Ranking

- **Source:** BOOK-DEFINED (policy/task dependent)
- **Formal meaning:** Text relevance, embedding similarity, graph distance, relation relevance, governance state, temporal validity, source quality, and evidence diversity may together inform ranking — configured per policy/task, not one universal weighted formula.
- **Book wording:** "Xếp hạng đa tín hiệu theo chính sách bài toán — không có công thức trọng số chung."
- **Dangerous simplification:** One weighted sum for all questions.
- **MUST NOT infer:**
  - MUST NOT say the combination is a truth measure.
  - MUST NOT claim the weights are universally optimal.

## Retrieval Evaluation (layers)

- **Source:** BOOK-DEFINED (stage-wise evaluation); IRBOOK-01 (retrieval metrics); CITE-01 (answer/citation); KGQA-01 (linking)
- **Formal meaning:** Evaluate each layer separately: (1) entity linking, (2) retrieval quality, (3) evidence sufficiency, (4) answer grounding, (5) answer correctness, (6) citation quality, (7) behavior under contradiction/unknowns. Do not collapse into one score.
- **Book wording:** "Đánh giá theo tầng — liên kết, truy xuất, đủ bằng chứng, căn cứ, đúng, trích dẫn, mâu thuẫn — không gộp một con số."
- **Dangerous simplification:** End-to-end accuracy as the only number.
- **MUST NOT infer:**
  - MUST NOT say a good retrieval metric implies good answers.
  - MUST NOT say one score identifies the failing stage.

## Gold Evidence

- **Source:** BOOK-DEFINED (annotated benchmark); IRBOOK-01 (relevance judgments)
- **Formal meaning:** A defined relevance gold set per question (e.g., for "Why is Velocity RATE_OF_CHANGE?": application structure, accepted classification claim, source definition passage). Measure whether the system retrieves them. Gold evidence is dataset annotation, not metaphysical truth.
- **Book wording:** "Bằng chứng chuẩn (gold evidence) là chú thích bộ dữ liệu — dùng để đo truy xuất, không phải chân lý."
- **Dangerous simplification:** Treating the gold set as ground truth about the world.
- **MUST NOT infer:**
  - MUST NOT say gold annotations are infallible.
  - MUST NOT say retrieval score against gold is answer truth.

## Claim-Evidence Alignment

- **Source:** BOOK-DEFINED (answer validation layer); AIS-01/CITE-01 (support judgment)
- **Formal meaning:** For each answer claim, find supporting retrieved evidence; classify SUPPORTED / PARTIALLY_SUPPORTED / UNSUPPORTED / CONTESTED. Useful validation layer; automatic alignment is not infallible.
- **Book wording:** "Đối chiếu claim-bằng chứng: từng claim trong câu trả lời được hỗ trợ / hỗ trợ một phần / không được hỗ trợ / đang tranh cãi."
- **Dangerous simplification:** Automatically scoring alignment as ground truth.
- **MUST NOT infer:**
  - MUST NOT say alignment proves the answer is right.
  - MUST NOT skip alignment because it is automatic.

## Inferred-Fact Retrieval

- **Source:** BOOK-DEFINED; Ch5 inference (entailment) relationship
- **Formal meaning:** A question may depend on facts implied by the ontology but not explicitly stored. Options: materialized inference, query-time entailment, or retrieval expansion using the ontology (Ch5). Do not assume the graph contains all entailed triples.
- **Book wording:** "Sự kiện suy dẫn (inferred fact) có thể không có sẵn — cần suy diễn (Ch5) hoặc mở rộng truy xuất bằng ontology, không giả định chứa hết."
- **Dangerous simplification:** Searching only asserted triples when entailment is needed.
- **MUST NOT infer:**
  - MUST NOT say absence in the graph implies non-entailment.
  - MUST NOT silently run entailment without labeling the derivation.

## Asserted vs Derived vs Predicted

- **Source:** BOOK-DEFINED (mandatory table); Ch5 (derivation), Ch8 (prediction)
- **Formal meaning:** ASSERTED = from source/KG; DERIVED = by sound symbolic reasoning under explicit semantics; PREDICTED = by a learned model with scores. Different epistemic status: asserted is source-backed, derived is semantics-licensed, predicted is candidate/hypothesis.
- **Book wording:** "Khẳng định (asserted) từ nguồn; dẫn xuất (derived) từ suy diễn âm thanh; dự đoán (predicted) từ mô hình học — ba mức tri thức luận khác nhau."
- **Dangerous simplification:** Mixing the three in one Evidence Packet without labels.
- **MUST NOT infer:**
  - MUST NOT say predicted = asserted.
  - MUST NOT say derived = asserted-to-the-world.
  - MUST NOT present a prediction as an accepted fact.

## Query Execution Router

- **Source:** BOOK-DEFINED (BOOK ENGINEERING MODEL); KGQA-01 + RAG-01 + GRAPHRAG-01 evidence
- **Formal meaning:** A router decides the execution path from the question: Exact Graph Query | Symbolic Reasoning | Text Retrieval | GraphRAG | Hybrid, then feeds an Evidence Packet to answer synthesis. Deterministic paths (SPARQL) should win when they suffice.
- **Book wording:** "Bộ điều hướng truy vấn (query router): chọn đường thực thi — truy vấn đồ thị chính xác, suy diễn, truy xuất văn bản, GraphRAG, hay lai — rồi đưa gói bằng chứng vào sinh câu trả lời (BOOK ENGINEERING MODEL)."
- **Dangerous simplification:** Always routing through the most expensive path.
- **MUST NOT infer:**
  - MUST NOT say router choice is truth.
  - MUST NOT say generative synthesis beats exact query when query suffices.

---

## Terminology Collision Contract

| Distinction | MUST protect | Why it matters |
|---|---|---|
| retrieval relevance ≠ epistemic support | lexical/semantic match ≠ the item genuinely supports the claim | a highly relevant-looking passage may be wrong or misattributed |
| retrieval score ≠ confidence | any ranking score is a retrieval utility | score magnitude is not a probability of truth |
| groundedness ≠ truth | support-by-sources ≠ world-correct | a faithfully summarized wrong source is still wrong |
| faithfulness ≠ real-world correctness | answer-consistent-with-context ≠ true | faithful to bad context is still bad |
| graph path ≠ logical proof | traversal ≠ entailment | a path only shows connectivity, not validity |
| summary ≠ source | derived artifact ≠ original | summaries lose evidence and can be stale |
| retrieved ≠ evidence | candidate until assessed | relevance + interpretation + scope are required |
| not retrieved ≠ false/absent | retrieval miss ≠ non-existence | OWA: absence implies nothing |
| RAG ≠ reasoning | retrieval + generation ≠ inference | generation is not logical consequence |
| GraphRAG ≠ KG semantics | graph help ≠ graph meaning | the graph organizes, it does not provide semantics by itself |
| canonical view ≠ claim ledger | projection ≠ full history | history/contradictions live in the ledger |
| asserted ≠ derived ≠ predicted | three epistemic statuses | each has different evidential weight |
| LLM answer ≠ accepted knowledge | QA output ≠ governed claim | answers enter via the candidate pipeline, not directly |

These boundaries are mandatory in `book/chapter09.md`. Each MUST be explicit where its terms
first appear, and MUST NOT be collapsed anywhere.
