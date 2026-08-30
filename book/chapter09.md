# Chương 9 — Truy xuất, Hỏi đáp và GraphRAG

> **Định hướng chương**
>
> **Câu hỏi trung tâm:** Khi người dùng đặt câu hỏi cho hệ thống tri thức — "Vì sao vận
> tốc là một tốc độ biến thiên?", "Cơ chế chung của vận tốc và dòng điện là gì?", "Định
> nghĩa 'current' năm 2020 là gì?", "Ai từng đề xuất điều ngược lại?" — làm sao hệ thống
> biết **phải truy xuất gì, từ đâu, theo thứ tự nào**, rồi **sinh ra câu trả lời** sao
> cho mọi khẳng định đều vết được về bằng chứng và không một khẳng định nào được sinh ra
> từ khoảng trống?
>
> **Vì sao quan trọng:** Tám chương trước đã xây dựng một hệ tri thức trọn vẹn: đồ thị
> (Ch1–2), định danh (Ch3), ngữ nghĩa (Ch4), suy diễn (Ch5), tri thức luận với Claim
> Ledger (Ch6), thu nhận nguồn (Ch7), và học quy nạp (Ch8). Nhưng một hệ tri thức không
> có **cửa sổ hỏi đáp** thì giống một thư viện không có thủ thư: tri thức có ở đó, mà
> không ai tìm ra được. Chương 9 mở nấc cuối cùng của hành trình: **truy xuất
> (retrieval)** — lấy đúng bằng chứng từ đúng nơi — và **hỏi đáp (question answering)** —
> biến bằng chứng thành câu trả lời có căn cứ. Đây cũng là nơi hệ thống gặp người dùng
> thật, và nơi mọi lỗi nhỏ ở tầng dưới (định danh sai, claim lỗi thời, index tụt hậu) bị
> phơi bày thành câu trả lời sai.
>
> **Bạn sẽ hiểu:**
>
> - IO mới của hệ thống: từ câu hỏi tiếng Việt đến câu trả lời có căn cứ, trích dẫn
> - Diễn giải câu hỏi (question interpretation) và phân loại intent: factual, structural,
>   comparative, explanatory, provenance, temporal, contradiction, discovery, multi-hop
> - Liên kết thực thể truy vấn; intent ≠ định danh; phân rã câu hỏi; kế hoạch truy xuất
> - Đơn vị truy xuất (retrieval unit); **index ≠ KG**; truy xuất đồ thị tượng trưng (SPARQL)
> - Duyệt đa chặng, giới hạn độ sâu, traversal theo quan hệ, vùng lân cận k-chặng
> - Truy xuất từ vựng (BM25), truy xuất mật độ (Dual Encoder), vector câu hỏi ≠ ý nghĩa
> - Truy xuất lai (hybrid) và hợp hạng RRF; đồ thị trước vs văn bản trước
> - Truy xuất theo tri thức luận: Canonical View vs Claim Ledger, quản trị, thời gian
>   (nhiều đồng hồ), nguồn gốc, mâu thuẫn, đa dạng bằng chứng
> - **top_k là ranh giới tri thức luận**; precision/recall/P@K/R@K/MRR/nDCG; tái xếp hạng
> - Lắp ráp và nén ngữ cảnh; lost in the middle; tuần tự hóa đồ thị
> - **Evidence Packet** (BOOK-DEFINED) — giao diện giữa truy xuất và sinh câu trả lời
> - Sinh câu trả lời, claim con, câu trả lời có căn cứ, trích dẫn, độ đầy đủ trích dẫn
> - Trung thành (faithfulness) ≠ đúng (correctness); bảng 2×2; kiêng trả lời (abstention)
> - Không biết ≠ không tìm thấy; lỗi truy xuất ≠ thiếu tri thức
> - Lập kế hoạch truy vấn, truy xuất tĩnh vs agentic, điều kiện dừng, trôi câu hỏi
> - Thiên kiến xác nhận; truy xuất kiểm định giả thuyết; câu hỏi local vs global
> - GraphRAG là **một họ kiến trúc** (không phải một thuật toán chuẩn); bảng quyết định
>   KGQA vs RAG vs GraphRAG
> - Đường đi là giải thích nhưng không phải chứng minh; bùng nổ đường đi
> - Truy xuất cộng đồng/phân cấp; cache và nhất quán index; provenance truy xuất
> - **Câu trả lời QA ≠ tri thức thu nhận**; ngữ nghĩa điểm số; xếp hạng đa tín hiệu
> - Đánh giá truy xuất 7 tầng; bằng chứng vàng (gold evidence); QA benchmark; test đối
>   kháng, distractor, mâu thuẫn, thời gian
> - Ca làm việc toàn trình 15 bước trên RATE_OF_CHANGE; ca thất bại; phân loại
>   hallucination; tự kiểm tra; đối chiếu claim-bằng chứng
> - Suy luận đồ thị vs suy luận LLM; GraphRAG không đảm bảo điều gì; khi nào KHÔNG dùng RAG
> - Router thực thi truy vấn (BOOK-DEFINED); 34 quan niệm sai; 8 điểm tự kiểm tra;
>   EXP-9-1..EXP-9-9 (hoãn đến v0.1); kiểm toán độ sâu; Q01–Q50; bậc năng lực cuối chương
>
> **Tiên quyết:**
> - Chương 1–2 (đồ thị, node, cạnh, kiểu, đường đi)
> - Chương 3 (định danh — entity ≠ embedding)
> - Chương 4 (ngữ nghĩa, OWA, closed-world)
> - Chương 5 (suy diễn, quy tắc, SPARQL, SHACL)
> - Chương 6 (epistemic model, Claim, Claim Ledger, Evidence, Assessment, provenance,
>   multiple clocks)
> - Chương 7 (thu nhận nguồn, tích hợp, governance, canonical view)
> - Chương 8 (học quy nạp, giả thuyết cơ chế, hybrid pipeline, dự đoán ≠ suy dẫn)
>
> **Bản đồ khái niệm:**
>
> Diễn giải câu hỏi → Intent (8 loại) → Liên kết thực thể → Phân rã → Kế hoạch truy xuất
> → Đơn vị truy xuất → Index ≠ KG → Đồ thị (SPARQL, đa chặng, k-chặng, subgraph) → Văn
> bản (BM25, dense, lai, RRF) → Tri thức luận (Canonical vs Ledger, governance, thời
> gian, provenance, mâu thuẫn) → top_k bound → Đo lường → Tái xếp hạng → Lắp ráp ngữ
> cảnh → Evidence Packet → Sinh câu trả lời → Căn cứ/trích dẫn/trung thành → Kiêng trả
> lời → Truy xuất động (agentic, dừng, drift, thiên kiến) → GraphRAG họ kiến trúc →
> Subgraph/community → Cache → Provenance → Đánh giá 7 tầng → Benchmark → Ca làm việc →
> Ca thất bại → Giới hạn → Router → Quan niệm sai → Bậc năng lực
>
> **Chuỗi phân biệt trung tâm** (xuyên suốt chương, được nhắc lại nhiều lần):
> retrieved ≠ evidence; điểm truy xuất ≠ độ tin cậy; có căn cứ ≠ đúng; trung thành ≠
> đúng; đường đi ≠ chứng minh; tóm tắt ≠ nguồn; không tìm thấy ≠ không tồn tại;
> câu trả lời QA ≠ tri thức được chấp nhận.

## 9.1 IO mới: Từ câu hỏi đến câu trả lời

Tám chương trước dạy hệ thống cách **xây dựng và duy trì tri thức**: định danh thực thể,
gán ngữ nghĩa, suy diễn hệ quả, quản trị claim trong Sổ cái, thu nhận từ nguồn, và học
giả thuyết từ đồ thị. Nhưng không có nấc nào trong số đó mô tả cách người dùng **lấy tri
thức ra** khi cần. Chương 9 thêm hai đầu vào–đầu ra (IO) mới cho toàn hệ thống:

- **Đầu vào mới: một câu hỏi tự nhiên** — "Vì sao vận tốc được coi là tốc độ biến thiên?"
- **Đầu ra mới: một câu trả lời có căn cứ, có trích dẫn, có hồ sơ nguồn gốc** — không chỉ
  đúng về nội dung, mà còn phải *giải thích được vì sao hệ thống tin điều đó*.

IO này không phải một phép tra cứu đơn giản. Nó là **một quy trình truy xuất–suy luận–
tổng hợp** (retrieval–reasoning–synthesis pipeline) gồm ba tầng khác biệt:

1. **Tầng hiểu câu hỏi** (question understanding): câu hỏi tự nhiên → intent có cấu trúc
   + các thực thể được đề cập (có thể mơ hồ) → kế hoạch truy xuất.
2. **Tầng truy xuất** (retrieval): chạy kế hoạch trên các nguồn tri thức — đồ thị cấu
   trúc, Sổ cái claim, văn bản nguồn, index vector — rồi gom thành một **Gói bằng chứng**
   (Evidence Packet, BOOK-DEFINED, §9.36).
3. **Tầng sinh câu trả lời** (answer generation): mô hình ngôn ngữ (LLM) đọc Gói bằng
   chứng, tổng hợp câu trả lời, phân tách thành các claim con, và gắn từng claim với
   bằng chứng (trích dẫn).

Điểm mấu chốt về mặt kiến trúc: LLM — dù mạnh đến đâu — **chỉ suy luận trên phần tri
thức được đưa vào cửa sổ ngữ cảnh của nó**, không phải trên toàn bộ hệ tri thức. Câu nói
này nghe hiển nhiên nhưng là gốc rễ của hầu hết các thất bại trong chương này:

> **Cửa sổ ngữ cảnh ≠ Tri thức.** Hệ thống có thể chứa đúng mọi claim, đúng mọi đường
> cấu trúc — nhưng nếu tầng truy xuất không đưa đúng mảnh vào cửa sổ, câu trả lời vẫn sai.

Ví dụ minh họa ngay cho khái niệm này: hệ tri thức của chúng ta có ba ứng dụng của cơ
chế `RATE_OF_CHANGE` — `VelocityDerivativeApplication`, `CurrentDerivativeApplication`,
`PopulationDerivativeApplication`. Nếu người dùng hỏi "Cơ chế chung của vận tốc và dòng
điện là gì?", một LLM không được cấp ngữ cảnh có thể "biết" về vật lý, nhưng nó **không
biết** hệ thống của chúng ta đã kết nối hai khái niệm đó qua cùng một cơ chế — đó là tri
thức *nội bộ*, chỉ tồn tại trong đồ thị. Nếu tầng truy xuất chỉ gửi một đoạn văn về dòng
điện, câu trả lời sẽ thiếu một nửa cấu trúc. Ngược lại, nếu gửi đủ cấu trúc cơ chế +
đoạn nguồn, LLM mới có cơ sở để tổng hợp câu trả lời đúng chỗ.

Một cảnh báo phương pháp luận trước khi đi tiếp, đúng tinh thần của toàn bộ cuốn sách:
**quy trình chạy xong không có nghĩa là câu trả lời đúng.** Truy xuất thành công, tổng
hợp trôi chảy, trích dẫn đầy đủ — tất cả đều là các thuộc tính *quy trình*. Sự đúng đắn
với thế giới là một thuộc tính *khác*, chỉ có thể được đánh giá bởi người dùng và các
quy trình đối chiếu bên ngoài. Chương này dạy cách làm cho quy trình **trung thực về mức
độ chắc chắn của chính nó** — nói rõ cái gì được hỗ trợ, cái gì suy luận, cái gì chưa
biết — chứ không dạy cách khiến quy trình thành không thể sai.

## 9.2 Bức tranh toàn cảnh: truy xuất là nơi mọi nấc gặp nhau

Trước khi đi vào chi tiết, hãy đặt chương này vào kiến trúc chín chương (Hình 9.1). Mỗi
nấc trước đây cung cấp cho tầng truy xuất một khả năng riêng:

- **Ch1–2** cho cấu trúc: node, cạnh, kiểu, đường đi — truy xuất đồ thị di chuyển trên đó.
- **Ch3** cho định danh: `sameAs`, dấu vân tay, danh tính — liên kết thực thể truy vấn
  dựa vào đó để quyết định "mention này là ai".
- **Ch4** cho ngữ nghĩa: lớp, thuộc tính, OWA — truy xuất hiểu "lớp cha của Dòng điện" là gì.
- **Ch5** cho suy diễn: SPARQL/entailment — truy xuất tượng trưng thực thi trên đó.
- **Ch6** cho tri thức luận: Claim, Claim Ledger, Evidence, Assessment, PROV — truy xuất
  theo nguồn gốc, theo thời gian, theo mâu thuẫn sống nhờ các khái niệm này.
- **Ch7** cho thu nhận và quản trị: canonical view, governance state — truy xuất phân
  biệt "điều đang được chấp nhận" với "điều đã từng được đề xuất".
- **Ch8** cho quy nạp: giả thuyết cơ chế, hybrid pipeline — truy xuất kiểm định giả
  thuyết sử dụng khái niệm này.

![Kiến trúc toàn phần chín chương: đồ thị → định danh → ngữ nghĩa → suy diễn → tri thức luận → thu nhận → học quy nạp → truy xuất và hỏi đáp. Chương 9 là nấc hiện tại: cửa sổ giao tiếp với người dùng.](figures/generated/ch09-full-stack.pdf)

Vị trí của Ch9 trong kiến trúc cũng quy định **phạm vi cam kết** của nó: Ch9 không thêm
quy tắc mới vào ontology, không thêm claim mới vào Sổ cái. Nó *tiêu thụ* tất cả các nấc
đó để phục vụ một mục đích duy nhất: trả lời câu hỏi một cách trung thực với tri thức
hiện có. Đây là lý do các ranh giới của chương đặc biệt quan trọng — một hệ thống trả lời
sai "vì hệ thống nói vậy" còn nguy hiểm hơn một hệ thống không trả lời.

---

# Phần A — Hiểu câu hỏi và kế hoạch truy xuất

## 9.3 Diễn giải câu hỏi (Question Interpretation)

Bước đầu tiên của pipeline: biến câu hỏi tự nhiên thành **intent có cấu trúc** — câu hỏi
đang hỏi điều gì, về thực thể nào, và loại bằng chứng nào sẽ được chấp nhận. Trong truy
xuất thông tin cổ điển, sách giáo khoa chuẩn phân biệt ba khái niệm [@manning-ir-2008]:

- **Nhu cầu thông tin** (information need) — điều người dùng *thực sự muốn biết*;
- **Câu hỏi** (query) — biểu thức ngôn ngữ họ gõ ra;
- **Tài liệu** (document) — đơn vị mà hệ thống có thể tìm thấy.

Ba khái niệm này không trùng nhau. Người dùng gõ "current" có thể cần "dòng điện là gì"
(định nghĩa khái niệm), "dòng điện hiện tại là bao nhiêu" (giá trị đo), hoặc "phiên bản
hiện hành của định nghĩa là gì" (trạng thái quản trị). Chính vì vậy, chương này không gọi
bước đầu tiên là "phân tích câu hỏi" mà gọi là **diễn giải** (interpretation): một phép
suy luận có thể sai, luôn phải được ghi nhận và có thể bị sửa lại.

**Formal meaning:** diễn giải câu hỏi ánh xạ câu hỏi tự nhiên thành một cấu trúc gồm
(a) danh sách mention thực thể (có độ mơ hồ), (b) loại intent, (c) các ràng buộc (thời
gian, trạng thái quản trị, miền), (d) loại bằng chứng được yêu cầu. Kết quả diễn giải là
*một phân tích*, không phải một khẳng định về thế giới.

**Trong sách:** "Diễn giải câu hỏi: chuyển câu hỏi tự nhiên thành intent có cấu trúc —
thực thể, loại câu hỏi, bằng chứng cần thiết. Kết quả có thể sai và phải được ghi lại."

Ví dụ trong miền liên tục của chúng ta:

| Câu hỏi | Intent có cấu trúc |
|---|---|
| "Vận tốc là gì?" | FACTUAL — thực thể `Velocity`, yêu cầu định nghĩa được chấp nhận |
| "Vận tốc so với dòng điện giống nhau ở đâu?" | COMPARATIVE — hai thực thể, yêu cầu cấu trúc chung |
| "Vì sao vận tốc là tốc độ biến thiên?" | EXPLANATORY — thực thể + thuộc tính, yêu cầu đường cấu trúc + bằng chứng |
| "Định nghĩa current 2020 là gì?" | TEMPORAL — thực thể + mốc thời gian |
| "Ai từng phản đối định nghĩa này?" | CONTRADICTION/PROVENANCE — yêu cầu Sổ cái, không phải chiếu hình |
| "Có cơ chế nào khác ngoài RATE_OF_CHANGE điều khiển vận tốc?" | DISCOVERY — yêu cầu tìm kiếm mở |

**Nguy hiểm khi đơn giản hóa:** xem kết quả diễn giải như một sự thật hiển nhiên, rồi
chuyển thẳng sang truy xuất mà không kiểm tra lại; hoặc nhầm lẫn "câu hỏi gõ ra" với
"nhu cầu thông tin".

**MUST NOT suy ra:**
- Không được khẳng định intent đã diễn giải là intent thật của người dùng.
- Không được bỏ qua bước ghi nhận diễn giải nào đã được chọn (diễn giải là dữ liệu
  provenance của toàn bộ phần sau).
- Không được trình bày sản phẩm của diễn giải (intent, danh sách thực thể) như tri thức
  đã được chấp nhận — nó là phân tích, không phải khẳng định.

## 9.4 Phân loại intent: tám loại câu hỏi

Để chọn đúng kế hoạch truy xuất, hệ thống phân loại câu hỏi theo **loại intent**. Mỗi
loại có yêu cầu bằng chứng và nguồn truy xuất riêng. Bảng 9.1 là bảng phân loại của
chương (BOOK-DEFINED, dựa trên phân loại truy vấn trong khảo sát KGQA [@chakraborty-kgqa-2019]
và các chế độ truy vấn GraphRAG [@edge-graphrag-2024]):

| # | Intent | Câu hỏi điển hình | Nguồn truy xuất ưu tiên | Bằng chứng tối thiểu |
|---|---|---|---|---|
| 1 | FACTUAL | "Dòng điện là gì?" | Canonical View, định nghĩa được chấp nhận | Claim được chấp nhận + đoạn nguồn |
| 2 | STRUCTURAL | "Velocity là ứng dụng của cơ chế nào?" | Đồ thị cấu trúc (instanceOf/mechanism) | Đường đi cấu trúc |
| 3 | COMPARATIVE | "Vận tốc và dòng điện giống nhau ở đâu?" | Đồ thị + các đường cấu trúc song song | Cấu trúc chung (cơ chế dùng chung) |
| 4 | EXPLANATORY | "Vì sao vận tốc là tốc độ biến thiên?" | Đồ thị + Sổ cái + văn bản nguồn | Đường cơ chế + claim chấp nhận + đoạn nguồn |
| 5 | PROVENANCE | "Vì sao hệ thống tin định nghĩa này?" | PROV chain: Claim→Evidence→SourceFragment→Source | Chuỗi nguồn gốc đầy đủ |
| 6 | TEMPORAL | "Định nghĩa current năm 2020?" | Sổ cái theo valid/publication time | Claim có mốc thời gian |
| 7 | CONTRADICTION | "Ai từng phản đối?" / "Có mâu thuẫn không?" | Sổ cái: các claim cạnh tranh + phạm vi | ≥2 claim đối lập kèm phạm vi |
| 8 | DISCOVERY | "Còn cơ chế nào khác không?" | Tìm kiếm mở (lexical/dense + đồ thị) | Tập ứng viên đa dạng, kèm giới hạn |
| 9 | MULTI-HOP | "Vì sao tăng trưởng dân số dùng chung cơ chế với dòng điện?" | Kết hợp: cấu trúc + tương tự + bằng chứng | Chuỗi các bước con có dependency |

Chín dòng (tám loại cộng một loại tổng hợp) không phải là một phân loại "đúng duy nhất"
— nó là **chính sách của cuốn sách**, đủ để minh họa nguyên tắc: *loại intent quyết định
loại bằng chứng cần truy xuất, và loại bằng chứng quyết định nguồn dữ liệu nào được phép
trả lời.*

**MUST NOT suy ra:**
- Không được dùng một công thức truy xuất chung cho mọi loại câu hỏi.
- Không được khẳng định intent được quyết định hoàn toàn bởi các thực thể xuất hiện
  ("hỏi về vận tốc" không tự nó cho biết hỏi định nghĩa, lịch sử, hay tranh cãi).
- Không được để nhãn intent âm thầm thay đổi trạng thái tri thức luận của câu trả lời
  (ví dụ: trả lời câu hỏi lịch sử bằng định nghĩa hiện hành).

## 9.5 Liên kết thực thể truy vấn (Query Entity Linking)

Câu hỏi thường chứa các mention — "current", "vận tốc", "tốc độ biến thiên". Liên kết
thực thể truy vấn ánh xạ mỗi mention sang các **ứng viên thực thể** trong đồ thị. Đây là
bài toán con lõi của KGQA [@chakraborty-kgqa-2019], và nó kế thừa trực tiếp ngữ nghĩa
định danh của Ch3: danh tính là một quyết định có quản trị, không phải phép so sánh
chuỗi.

Một mention có thể có nhiều ứng viên vì nhiều lý do khác nhau:

- **Trùng tên (homonym):** "current" → `ElectricCurrent` (khái niệm) hay `CurrentValue`
  (giá trị hiện thời)?
- **Đa nghĩa miền:** "tăng trưởng" → `PopulationGrowth` (mô hình dân số) hay
  `EconomicGrowth` (kinh tế)?
- **Mập mờ cú pháp:** "current" là tính từ ("hiện tại") hay danh từ ("dòng điện")?

Quy trình chuẩn gồm ba bước, theo mô hình của hệ thống KGQA điển hình [@chakraborty-kgqa-2019]:

1. **Sinh ứng viên** (candidate generation): từ chuỗi mention + các biến thể, tìm các
   thực thể có nhãn/đồng nghĩa khớp — qua chỉ mục chuỗi, qua nhúng, qua các thực thể
   kết nối trong ngữ cảnh câu hỏi.
2. **Chấm điểm ngữ cảnh** (contextual scoring): mỗi ứng viên được chấm theo mức khớp với
   ngữ cảnh — các thực thể khác trong câu hỏi, lớp, quan hệ, miền. "Dòng điện" đi cùng
   "điện trở" nghiêng về `ElectricCurrent`.
3. **Quyết định** (decision): chọn ứng viên hoặc **tuyên bố mơ hồ** (ambiguity) — quan
   trọng hơn cả việc chọn đúng là *biết mình không chắc*.

**Formal meaning:** liên kết thực thể truy vấn = ánh xạ mention → (tập ứng viên, phân
phối điểm, quyết định/độ mơ hồ). Chọn ứng viên có điểm cao nhất *không phải* là bước
cuối bắt buộc; ghi nhận độ mơ hồ là một đầu ra hợp lệ.

**Trong sách:** "Liên kết thực thể truy vấn: mention → các ứng viên → chấm điểm ngữ cảnh
→ chọn hoặc báo mơ hồ. Không tự động lấy vector giống nhất làm câu trả lời."

Ví dụ: "current" trong câu hỏi "Vì sao current thay đổi khi điện trở thay đổi?" — ứng
viên `ElectricCurrent` thắng vì cùng ngữ cảnh `ElectricalResistance` (quan hệ
`affects`/`dependsOn`). Nhưng "Định nghĩa 'current' trong sách năm 2020?" vẫn có thể mơ
hồ giữa thực thể khái niệm và thực thể phiên bản — hệ thống nên hỏi lại hoặc trả lời với
cả hai phạm vi, thay vì chọn đại.

**Nguy hiểm khi đơn giản hóa:** chọn thực thể có vector giống nhất mà không đánh giá ngữ
cảnh; giả định một mention = một thực thể; giấu độ mơ hồ.

**MUST NOT suy ra:**
- Không được khẳng định ứng viên có điểm cao nhất là đúng.
- Không được tái sử dụng định danh *thực thể* của Ch3 như thể nó là liên kết *truy vấn*
  mà không thích ứng với ngữ cảnh câu hỏi (Ch3 hợp nhất danh tính qua thời gian; câu hỏi
  lại cần phân biệt các phạm vi tạm thời).
- Không được vứt bỏ sự mơ hồ — một mention mơ hồ phải được ghi nhận, không phải che giấu.

## 9.6 Intent ≠ Định danh: hai trục mơ hồ độc lập

Đây là một ranh giới ngữ nghĩa mà chương này nhấn mạnh vì nó bị vi phạm thường xuyên:

> **"Đề cập đến ai" (entity identity) và "hỏi điều gì" (query intent) là hai trục độc
> lập. Cả hai đều có thể mơ hồ, và độ mơ hồ của trục này không kéo theo độ mơ hồ của
> trục kia.**

Ví dụ phân tích: câu hỏi "Dòng điện thay đổi như thế nào?"

- Trục thực thể: `ElectricCurrent` — rõ ràng (điện tử học, không phải kinh tế).
- Trục intent: mơ hồ nghiêm trọng. "Thay đổi như thế nào" có thể muốn:
  - cơ chế: "dòng điện thay đổi theo *đạo hàm của điện tích theo thời gian*" (STRUCTURAL);
  - nguyên nhân: "dòng điện thay đổi *khi điện trở đổi*" (EXPLANATORY);
  - định luật: "dòng điện tỉ lệ nghịch điện trở" (FACTUAL);
  - lịch sử: "định nghĩa dòng điện đã thay đổi ra sao qua các phiên bản" (TEMPORAL).

Ngược lại: "Vận tốc là gì?" — trục intent rõ (định nghĩa), nhưng trục thực thể có thể mơ
hồ nếu đồ thị có cả `Velocity` (khái niệm) và `InstantaneousVelocity` (biến thể).

Hệ quả thiết kế: **diễn giải câu hỏi phải tạo ra hai bản ghi tách biệt** — danh sách thực
thể (kèm độ mơ hồ) và nhãn intent (kèm độ mơ hồ). Nếu hệ thống gộp hai trục này thành
một bước "hiểu câu hỏi" không phân biệt, nó sẽ không thể báo cáo đúng loại không chắc
chắn của mình.

**MUST NOT suy ra:**
- Không được gộp định danh thực thể và phân loại intent thành một bước không có lý do.
- Không được khẳng định hai trục mơ hồ luôn xảy ra cùng nhau.
- Không được để việc đã phân giải được thực thể ngụ ý rằng đã hiểu được intent.

## 9.7 Phân rã câu hỏi (Query Decomposition)

Một câu hỏi phức hợp thường phải được tách thành các câu hỏi con có phụ thuộc rõ ràng.
Ví dụ trung tâm của chương — câu hỏi chứng minh cho toàn bộ phần sau:

> **Q0:** "Vì sao vận tốc và dòng điện được xem là cùng một cơ chế RATE_OF_CHANGE, và
> bằng chứng nào ủng hộ điều đó?"

Phân rã (một trong nhiều cách hợp lệ):

- **Q1 (STRUCTURAL):** `VelocityDerivativeApplication` là ứng dụng của cơ chế nào?
  → `RATE_OF_CHANGE`, qua quan hệ `instanceOf` (hoặc mechanism attribution).
- **Q2 (STRUCTURAL):** `CurrentDerivativeApplication` là ứng dụng của cơ chế nào?
  → cùng `RATE_OF_CHANGE`.
- **Q3 (STRUCTURAL/COMPARATIVE):** Vai trò của hai ứng dụng có giống nhau không? → cùng
  `operation=DerivativeOperation`, `withRespectTo=Time`, `produces` ra đại lượng.
- **Q4 (FACTUAL/PROVENANCE):** Claim chấp nhận nào khẳng định sự tương ứng này, từ nguồn
  nào? → Claim + Evidence + SourceFragment.
- **Q5 (CONTRADICTION):** Có claim nào phản đối/giới hạn sự tương ứng này không? → tra
  Sổ cái.
- **Q6 (TỔNG HỢP):** Gộp Q1–Q5 thành câu trả lời giải thích.

**Formal meaning:** phân rã câu hỏi = tách câu hỏi phức thành câu con + đồ thị phụ thuộc
(Q3 cần kết quả Q1, Q2; Q6 cần tất cả). Phân rã là một *kế hoạch*, không phải một phép
tính chân lý — một phân rã khác có thể đúng không kém.

**Trong sách:** "Phân rã truy vấn: câu phức → câu con + phụ thuộc → kế hoạch truy xuất.
Không phải câu hỏi nào cũng cần phân rã."

Hai lưu ý quan trọng:

1. **Không phải câu hỏi nào cũng cần phân rã.** "Vận tốc là gì?" — một truy vấn đơn.
   Phân rã bừa bãi tạo chi phí, nhiễu, và nhiều nơi để lỗi len vào.
2. **Các câu trả lời con không tự động cộng thành câu trả lời đúng.** Mỗi câu con có thể
   đúng riêng lẻ nhưng việc ghép chúng (đặc biệt bước tổng hợp Q6) là một suy luận riêng
   cần kiểm tra lại — đây chính là nơi "thành phần đúng, tổng thể sai".

**MUST NOT suy ra:**
- Không được khẳng định kết quả phân rã là cách đọc duy nhất đúng.
- Không được giả định câu trả lời của các câu con tự cộng thành một câu trả lời đúng.

## 9.8 Kế hoạch truy xuất (Retrieval Plan) và Bộ điều hướng truy vấn

Từ intent + danh sách thực thể + phân rã, hệ thống xây **kế hoạch truy xuất**: một chuỗi
có thứ tự các phép truy xuất cụ thể với giới hạn và điều kiện dừng. Kế hoạch cho câu hỏi
Q0 có thể là:

```
1. resolveEntity("Velocity") → Velocity
2. graphQuery(instanceOf, Velocity) → RATE_OF_CHANGE          (Q1)
3. resolveEntity("ElectricCurrent") → ElectricCurrent
4. graphQuery(instanceOf, ElectricCurrent) → RATE_OF_CHANGE   (Q2)
5. graphQuery(roleObjects, VelocityDerivativeApplication)     (Q3)
6. ledgerQuery(Accepted claims mentioning RATE_OF_CHANGE tương ứng)  (Q4)
7. ledgerQuery(Contested/Superseded claims về sự tương ứng)   (Q5)
8. sourcePassageRetrieval(BM25+dense cho "vận tốc ... đạo hàm ...") (bằng chứng văn bản)
9. assemble EvidencePacket; kết thúc (điều kiện dừng: đủ ô bằng chứng)
```

**Bộ điều hướng truy vấn** (Query Execution Router, BOOK-DEFINED) là thành phần quyết
định *đường thực thi* từ câu hỏi đã hiểu:

| Điều kiện | Đường thực thi |
|---|---|
| Thực thể + thuộc tính đã phân giải, lược đồ biết trước | **Truy vấn đồ thị chính xác** (SPARQL) |
| Cần suy diễn hệ quả | **Suy luận tượng trưng** (Ch5) |
| Thực thể mơ hồ / hỏi mở / định nghĩa | **Truy xuất văn bản** (BM25 + dense) |
| Cần cấu trúc + bằng chứng văn bản | **GraphRAG/hybrid** |
| Câu hỏi lịch sử/mâu thuẫn | **Tra Sổ cái** (ledger retrieval) |

Nguyên tắc của router: **đường rẻ nhất có thể trả lời đúng thì thắng.** Không dùng một
LLM sinh câu trả lời cho một truy vấn mà SPARQL trả về chính xác [@chakraborty-kgqa-2019]:
truy vấn cấu trúc đã là câu trả lời; sinh văn bản thêm khả năng bịa.

**Formal meaning:** kế hoạch truy xuất = bộ có thứ tự (phép truy xuất, tham số, giới hạn,
điều kiện dừng); router = hàm quyết định từ (intent, độ phân giải, lược đồ) → đường thực
thi.

**MUST NOT suy ra:**
- Không được khẳng định kế hoạch đảm bảo đầy đủ (plan chạy xong ≠ đã lấy đủ bằng chứng).
- Không được khẳng định kế hoạch đúng chỉ vì nó chạy đến hết.
- Không được để router chọn đường tốn kém nhất khi đường chính xác đủ dùng.

---

# Phần B — Đơn vị truy xuất và truy xuất đồ thị

## 9.9 Đơn vị truy xuất (Retrieval Unit)

Khi nói "truy xuất", phải nói rõ hệ thống trả về **đơn vị** gì. Trong truy xuất văn bản
cổ điển, đơn vị là tài liệu hoặc đoạn (passage) [@manning-ir-2008]. Trong một hệ tri
thức, có nhiều loại đơn vị, mỗi loại mang một khả năng và một giới hạn riêng:

| Đơn vị | Ví dụ | Mạnh để | Yếu để |
|---|---|---|---|
| Thực thể (entity) | `ElectricCurrent` | định danh, neo câu hỏi | trả lời phức hợp |
| Bộ ba (triple) | `CurrentDerivativeApplication instanceOf RATE_OF_CHANGE` | sự kiện đơn lẻ | ngữ cảnh |
| Claim | `#C471: "Current = RATE_OF_CHANGE(DerivativeOperation, ...)"` | tri thức luận (trạng thái, đánh giá) | bằng chứng gốc |
| Bằng chứng (Evidence) | bản ghi Ch6 gắn claim với đoạn nguồn | vết nguồn | nội dung tự thân |
| Đoạn nguồn (source passage) | đoạn trong sách vật lý | nội dung thật, trích dẫn được | cấu trúc |
| Đường đi (path) | `Velocity ->produces-> DerivativeApplication ->operation-> DerivativeOperation` | giải thích cấu trúc | chứng minh |
| Đồ thị con (subgraph) | ba ứng dụng + cơ chế chung | ngữ cảnh gắn kết | kích thước |
| Tóm tắt cộng đồng (summary) | "ba ứng dụng chia sẻ vai trò..." | gọn | nén mất bằng chứng |
| Đối tượng câu trả lời chuẩn (canonical answer) | bản ghi câu trả lời có quản trị | tái sử dụng | lỗi thời |

**Điểm mấu chốt:** câu trả lời *giải thích* thường cần nhiều loại đơn vị phối hợp. Một
claim được chấp nhận (đơn vị tri thức luận) chưa đủ nếu thiếu đoạn nguồn (đơn vị văn
bản) để trích dẫn; một đường đi (đơn vị cấu trúc) chưa đủ nếu thiếu claim (đơn vị tri
thức luận) để biết đường đó có được chấp nhận hay không.

**Formal meaning:** đơn vị truy xuất = loại đối tượng mà một bước truy xuất trả về; lựa
chọn đơn vị quyết định recall/precision, độ gắn kết ngữ cảnh, và khả năng vết nguồn gốc.

**MUST NOT suy ra:**
- Không được khẳng định một loại đơn vị là đủ cho mọi loại câu hỏi.
- Không được đồng nhất "đã truy xuất được đơn vị" với "đã đủ bằng chứng".

## 9.10 Index truy xuất ≠ Đồ thị tri thức

Một trong những nhầm lẫn kiến trúc nguy hiểm nhất trong các hệ RAG là coi **chỉ mục truy
xuất** (index) như thể nó là chính tri thức. Hãy phân biệt ba thực thể khác nhau:

1. **Đồ thị tri thức (KG)** — nguồn chân lý cấu trúc: node, cạnh, claim, đánh giá, quản
   trị. Đây là thứ được xây và duy trì từ Ch2 đến Ch8.
2. **Sổ cái claim (Claim Ledger)** — kho bất biến các claim có provenance, có trạng thái.
3. **Chỉ mục truy xuất (search/vector index)** — cấu trúc truy cập *dẫn xuất*: chuỗi đã
   token hóa, vector nhúng, nhãn, vùng lân cận được xây sẵn để truy xuất nhanh.

Trong truy xuất thông tin cổ điển, chỉ mục đảo (inverted index) đã được định nghĩa rõ là
một *cấu trúc truy cập* trên tập tài liệu, không phải nội dung tài liệu [@manning-ir-2008].
Nguyên tắc này mở rộng nguyên vẹn: **index là bản sao có chủ đích để tìm nhanh; nó có
thể tụt hậu so với KG và Sổ cái.**

Vì sao điều này quan trọng trong thực hành? Xét kịch bản: một claim bị chuyển sang
`Superseded` trong Sổ cái lúc 09:00; chỉ mục vector chỉ được tái lập lúc 10:00. Trong
khoảng thời gian đó, một truy vấn "Định nghĩa current là gì?" có thể trả về đoạn văn của
claim cũ với điểm cao — và LLM, trung thực với ngữ cảnh, sẽ trả lời bằng định nghĩa đã
bị thay thế. **Kỹ thuật chạy không lỗi, tri thức vẫn cũ.** Đây là lỗi *nhất quán chỉ mục*
(index consistency), chứ không phải lỗi của mô hình sinh.

**Formal meaning:** index ≠ KG: index là quan hệ dẫn xuất (KG hoặc Sổ cái → biểu diễn
truy xuất) có thể không đồng bộ; trạng thái index không bao hàm trạng thái KG.

**Trong sách:** "Index truy xuất là cấu trúc truy cập dẫn xuất từ KG — không phải KG,
không phải Sổ cái; có thể tụt hậu."

**MUST NOT suy ra:**
- Không được khẳng định trạng thái index bằng trạng thái đồ thị.
- Không được khẳng định một đoạn tìm thấy trong index là tri thức được chấp nhận.
- Không được bỏ qua độ tươi (freshness) của index khi đánh giá câu trả lời.

## 9.11 Truy xuất đồ thị tượng trưng (Symbolic Graph Retrieval)

Khi lược đồ, thực thể và quan hệ cần thiết đã biết chắc, đường truy xuất mạnh nhất là
**truy vấn đồ thị chính xác** — SPARQL [@w3c-sparql11-query] [@w3c-sparql11-overview]. Đây là
phép truy xuất tượng trưng: kết quả là chính xác theo nghĩa *khớp mẫu cấu trúc*, không
phải theo nghĩa *xếp hạng gần đúng*.

Ví dụ: hỏi cấu trúc "Vận tốc là ứng dụng của cơ chế nào và các vai trò ra sao?"

```sparql
SELECT ?app ?role ?obj WHERE {
  VALUES ?app { velocity:VelocityDerivativeApplication }
  ?app velocity:instanceOf ?mech ;
       velocity:operation ?op ;
       velocity:differentiand ?diff ;
       velocity:produces ?res .
}
```

Kết quả: `?mech = rate:RATE_OF_CHANGE`, `?op = DerivativeOperation`,
`?diff = Position`, `?res = Velocity` — một khối cấu trúc hoàn chỉnh, có thể đưa thẳng
vào Gói bằng chứng.

Điểm mạnh của truy xuất tượng trưng [@chakraborty-kgqa-2019]:

- **Chính xác cao:** nếu mẫu khớp, kết quả *đúng theo nghĩa đồ thị* — không có xác suất.
- **Kiểm tra được:** ai cũng đọc lại được câu truy vấn và kết quả.
- **Vết nguồn gốc tự nhiên:** mỗi triple trả về có provenance từ Ch6.

Giới hạn:

- **Cứng nhắc về từ ngữ:** không tìm thấy gì nếu dữ liệu dùng từ khác (trừ khi có ánh xạ
  từ vựng — Ch3).
- **Không "gần đúng":** không tìm được "thứ gì đó tương tự như đạo hàm" nếu chưa có
  mapping.
- **Phản ánh đồ thị, không phản ánh thế giới:** nếu KG sai, kết quả SPARQL sai mà vẫn
  "chính xác theo mẫu".

**MUST NOT suy ra:**
- Không được khẳng định kết quả đồ thị tượng trưng là đầy đủ về mặt ngữ nghĩa.
- Không được khẳng định SPARQL xử lý được paraphrase/từ vựng chưa có mapping.
- Không được coi kết quả truy vấn là tự động đúng với thế giới — nó phản ánh những gì KG
  khẳng định (và KG có thể sai hoặc lỗi thời).

## 9.12 Duyệt đồ thị và truy xuất đa chặng (Graph Traversal / Multi-hop Retrieval)

Khi câu trả lời cần *nối các thực thể qua nhiều bước*, hệ thống duyệt đồ thị theo cạnh.
Ví dụ câu hỏi Q3 ở §9.7: "Vai trò của hai ứng dụng có giống nhau không?" — truy xuất
đa chặng đi từ `VelocityDerivativeApplication` qua `operation` đến
`DerivativeOperation`, rồi từ `CurrentDerivativeApplication` qua `operation` đến cùng
nút — phát hiện sự chia sẻ cấu trúc (Hình 9.2).

![Truy xuất đa chặng: hai ứng dụng cùng trỏ đến cơ chế RATE_OF_CHANGE với cùng vai trò (operation=DerivativeOperation, withRespectTo=Time). Đường đi thể hiện sự tương ứng cấu trúc — không phải một chứng minh.](figures/generated/ch09-multihop-subgraph.pdf)

Từ góc độ KGQA, đây là phép trả lời "multi-hop path" [@chakraborty-kgqa-2019]: câu trả
lời nằm ở đầu kia của một chuỗi quan hệ. Nhưng chương này nhấn mạnh một ranh giới tri
thức luận:

> **Có đường đi ≠ đã chứng minh kết luận.** Một đường đi cho thấy đồ thị *kết nối* các
> khái niệm theo cách đó — nó không chứng minh các quan hệ trên đường đi là đúng với thế
> giới, cũng không chứng minh không còn đường đi khác (đặc biệt đường đi *bác bỏ*).

Ví dụ: đường đi `Velocity ->produces-> VelocityDerivativeApplication ->instanceOf->
RATE_OF_CHANGE` là một sự kiện cấu trúc. Nhưng nếu Sổ cái có claim phản đối rằng đạo hàm
chỉ là *một mô hình*, không phải bản chất của vận tốc, thì đường đi trên chỉ là một
phía. Truy xuất đa chặng trung thực phải ghi nhận cả hai phía — đây là cầu nối đến truy
xuất nhạy mâu thuẫn ở §9.27.

**Formal meaning:** truy xuất đa chặng = bước theo cạnh qua nhiều hop, có thể với ràng
buộc kiểu nút/kiểu cạnh/chiều, để tìm tập đường đi hoặc đồ thị con nối các thực thể
được đề cập trong câu hỏi.

**MUST NOT suy ra:**
- Không được trình bày một đường duyệt như một suy dẫn logic.
- Không được khẳng định sự tồn tại của đường đi hàm ý tính đúng đắn của các quan hệ trên
  đường.

## 9.13 Giới hạn độ sâu và phạm vi duyệt (Path Bounds)

Đồ thị tri thức không bao giờ nhỏ. Từ `CurrentDerivativeApplication`, một bước là
`ElectricCurrent`, `RATE_OF_CHANGE`, `Time`, `DerivativeOperation`; hai bước là lớp cha,
nguồn, tác giả, đánh giá, claim liên quan, ứng dụng tương tự... Đến bước ba, số nút có
thể tăng theo cấp số nhân. Vì vậy **mọi phép duyệt phải có ranh giới tường minh**:

- **Độ sâu tối đa** (max depth): bao nhiêu hop;
- **Loại cạnh được phép** (edge types): `operation`, `instanceOf`, `produces`... hay mọi
  cạnh;
- **Chiều** (direction): xuôi, ngược, hay cả hai;
- **Kiểu nút** (node types): nút nào được phép lọt vào kết quả;
- **Nhánh tối đa** (branching limit): mỗi nút xét tối đa bao nhiêu cạnh ra.

Ranh giới này không phải chi tiết kỹ thuật vô hại — nó là **một ranh giới tri thức luận
ngầm**, cùng bản chất với top_k (§9.29):

> **Độ sâu tối đa quyết định mảnh cấu trúc nào được nhìn thấy. Cái hệ thống không duyệt
> tới, hệ thống không thể trả lời — dù nó có tồn tại trong đồ thị.**

Hệ quả đối xứng nguy hiểm: giới hạn quá chặt giấu bằng chứng quyết định; giới hạn quá
lỏng làm ngập Gói bằng chứng bằng nhiễu. Chọn giới hạn là một quyết định thiết kế phải
được ghi lại trong provenance truy xuất (§9.58), chứ không phải một hằng số ngầm.

**MUST NOT suy ra:**
- Không được khẳng định "không có kết quả ngoài độ sâu d" hàm ý "không có kết quả".
- Không được giấu bộ lọc độ sâu/loại cạnh khỏi người đọc câu trả lời.

## 9.14 Traversal theo quan hệ (Relation-aware Traversal)

Không phải mọi cạnh đều hữu ích như nhau cho mọi intent. Traversal theo quan hệ = chọn
loại cạnh được duyệt theo loại câu hỏi:

- Câu hỏi **provenance** ("vì sao hệ thống tin X?"): duyệt `supports`, `derivedFrom`,
  `wasAttributedTo`, `wasGeneratedBy` — tuyến bằng chứng.
- Câu hỏi **cấu trúc cơ chế** ("vận tốc là ứng dụng của gì?"): duyệt `instanceOf`,
  `operation`, `differentiand`, `withRespectTo`, `produces`.
- Câu hỏi **thời gian** ("định nghĩa 2020?"): duyệt theo valid time/publication time của
  claim, không phải theo cạnh cấu trúc.
- Câu hỏi **mâu thuẫn** ("ai phản đối?"): duyệt các claim cùng chủ đề với trạng thái
  khác nhau trong Sổ cái.

**Formal meaning:** traversal theo quan hệ = policy ánh xạ intent → tập ưu tiên loại
cạnh (bao gồm cả việc loại trừ) khi duyệt; bộ lọc là một giả định thiết kế, có thể bỏ
sót đường quyết định.

**MUST NOT suy ra:**
- Không được khẳng định bộ lọc loại cạnh vứt bỏ được mọi cấu trúc không liên quan (nó có
  thể vứt luôn đường quyết định).
- Không được khẳng định một tập ưu tiên quan hệ là phổ quát cho mọi câu hỏi.

## 9.15 Vùng lân cận k-chặng (k-hop Neighborhood)

Một kỹ thuật phổ biến trong GraphRAG là mở rộng từ một thực thể neo ra **vùng lân cận
k-chặng** — mọi nút trong phạm vi k cạnh [@edge-graphrag-2024]. Kỹ thuật này mạnh để lấy
ngữ cảnh, nhưng phải hiểu bản chất thật của nó:

- Vùng lân cận của `CurrentDerivativeApplication` trong phạm vi 2 cạnh không chỉ chứa
  cơ chế và vai trò — nó còn chứa `ElectricCurrent`, các đơn vị đo, nguồn, tác giả, các
  đánh giá, các claim liên quan, các ứng dụng cơ chế *khác*...
- **Đa số lân cận là nhiễu theo quan điểm của một câu hỏi cụ thể.** Trong vùng 1-chặng
  của `ElectricCurrent` có cả `ElectricalResistance` (có thể quan trọng) và đơn vị đo
  `Ampere` (ít quan trọng với câu hỏi cơ chế).

Hệ quả thiết kế: **không bao giờ đổ nguyên vùng lân cận k-chặng vào cửa sổ ngữ cảnh**.
Phải lọc theo ngữ nghĩa — giữ các nút/cạnh khớp intent, gom phần còn lại thành tham chiếu
tĩnh. Hình 9.2 minh họa vùng lân cận được lọc: chỉ giữ các vai trò cấu trúc, vứt các
nhánh nhiễu.

**Formal meaning:** vùng lân cận k-chặng = tập nút/cạnh trong bán kính k của nút neo;
độ liên quan không được bao hàm bởi khoảng cách — cần lọc ngữ nghĩa bổ sung.

**MUST NOT suy ra:**
- Không được khẳng định "trong k-chặng" = "liên quan".
- Không được khẳng định "ngoài k-chặng" = "không liên quan".
- Không được đổ toàn bộ lân cận vào ngữ cảnh và gọi đó là "ngữ cảnh phong phú".

## 9.16 Truy xuất đồ thị con (Subgraph Retrieval) và đồ thị con đủ tối thiểu

Thay vì các đường rời rạc, hệ thống thường cần một **đồ thị con gắn kết** — một khối
cấu trúc đủ để trả lời trọn câu hỏi. Với câu hỏi Q0, đồ thị con mục tiêu là:

```
VelocityDerivativeApplication
 ├─ operation → DerivativeOperation
 ├─ differentiand → Position
 ├─ withRespectTo → Time
 ├─ produces → Velocity
 └─ instanceOf → RATE_OF_CHANGE
CurrentDerivativeApplication
 ├─ operation → DerivativeOperation
 ├─ differentiand → ElectricCharge
 ├─ withRespectTo → Time
 ├─ produces → ElectricCurrent
 └─ instanceOf → RATE_OF_CHANGE
```

Chọn đồ thị con *nào* là một bài toán truy xuất riêng: sinh tập ứng viên rồi tối ưu giữa
đủ thông tin và tránh nhiễu. Một khái niệm hữu ích là **đồ thị con đủ tối thiểu** (minimal
sufficient subgraph, BOOK-DEFINED): đủ cấu trúc để câu trả lời có căn cứ, không lan tràn.
Với câu hỏi giải thích, cấu trúc tối thiểu thường gồm: (a) các ứng dụng được hỏi,
(b) cơ chế chung, (c) các vai trò liên quan, (d) claim chấp nhận gắn kết, (e) một đoạn
nguồn để trích dẫn.

**Lưu ý cam kết:** "tối thiểu" ở đây là *đủ tối thiểu theo chính sách thiết kế*, không
phải một cực tiểu toán học có thể tính phổ quát. Không có công thức chung nào chứng minh
được một đồ thị con là nhỏ nhất có thể — vì "đủ" phụ thuộc ngữ nghĩa của câu hỏi.

**Formal meaning:** truy xuất đồ thị con = chọn một đồ thị con gắn kết thỏa ràng buộc
(cấu trúc tối thiểu, phủ các thực thể, chứa bằng chứng) từ một tập ứng viên lớn hơn;
tối ưu là theo chính sách, không theo nghĩa toán học.

**MUST NOT suy ra:**
- Không được khẳng định một đồ thị con được chọn là tối thiểu chứng minh được.
- Không được khẳng định nhiều cấu trúc hơn luôn tốt hơn.
- Không được coi một tập nút liên thông bất kỳ là "đồ thị con bằng chứng".

---

# Phần C — Truy xuất văn bản

Phần B truy xuất *cấu trúc*. Nhưng nhiều câu hỏi không thể trả lời bằng đường cấu trúc:
khái niệm mơ hồ, cần định nghĩa từ nguồn, hoặc cần tìm "thứ gì đó tương tự" mà chưa có
mapping tượng trưng. Với những câu hỏi này, hệ thống truy xuất **văn bản** — các đoạn
nguồn, các bản ghi claim được tuần tự hóa, các tài liệu đã đưa vào hệ. Phần C trình bày
hai họ truy xuất văn bản và cách kết hợp chúng.

## 9.17 Truy xuất từ vựng và BM25

**Truy xuất từ vựng** (lexical retrieval) khớp các *từ* của câu hỏi với *từ* của tài
liệu. Nền tảng lý thuyết là khuôn khổ xác suất liên quan của IR [@robertson-bm25-2009],
và hàm chuẩn được dạy trong chương này là **BM25** (Okapi BM25). Công thức chuẩn
[@robertson-bm25-2009] [@manning-ir-2008]:

$$\mathrm{score}(D,Q) = \sum_{t \in Q} \mathrm{idf}(t) \cdot \frac{f_{t,D}\,(k_1+1)}{f_{t,D} + k_1\left(1 - b + b\,\frac{|D|}{\mathrm{avgdl}}\right)}$$

với:

- $\mathrm{idf}(t) = \ln\!\left(\frac{N - n_t + 0.5}{n_t + 0.5} + 1\right)$ — **tần suất
  nghịch đảo tài liệu**: từ hiếm trong kho tài liệu nặng điểm hơn;
- $f_{t,D}$ — tần suất của từ $t$ trong tài liệu $D$;
- $k_1$ — hằng số **bão hòa tần suất** (saturation): càng nhiều lần lặp, mỗi lần lặp
  thêm càng ít điểm;
- $b$ — mức **chuẩn hóa độ dài tài liệu** (0 = không chuẩn hóa, 1 = chuẩn hóa hoàn toàn):
  tài liệu dài bị phạt để công bằng với tài liệu ngắn.

Đọc công thức theo ngôn ngữ đời thường: *"một tài liệu liên quan nếu nó chứa nhiều từ
hiếm của câu hỏi, lặp không lạm dụng, và không quá dài dòng"* [@robertson-bm25-2009].

**Điểm mạnh của BM25:**
- Không cần dữ liệu huấn luyện — xây được ngay trên kho văn bản.
- Khớp chính xác thuật ngữ kỹ thuật ("đạo hàm", "electromagnetic induction") rất tốt.
- Diễn giải được: ai cũng biết vì sao tài liệu được xếp hạng cao.

**Giới hạn cố hữu:**
- **Không hiểu đồng nghĩa/paraphrase** khi không có từ chung: hỏi "tốc độ biến thiên"
  mà đoạn nguồn viết "đạo hàm theo thời gian" thì điểm rất thấp dù nội dung đúng.
- Điểm số là *tiện ích xếp hạng*, không phải xác suất đúng.

**Ngữ nghĩa điểm số:** điểm BM25 cao nói lên "khớp từ tốt", không nói lên "tài liệu này
trả lời đúng". Khoảng cách điểm giữa hạng 1 và hạng 2 là một tín hiệu xếp hạng tương
đối, không phải độ tin cậy tuyệt đối.

**MUST NOT suy ra:**
- Không được diễn giải độ lớn điểm BM25 như độ tin cậy.
- Không được khẳng định BM25 nắm được ngữ nghĩa ngoài sự đồng xuất hiện từ.
- Không được dùng idf mà không giải thích nó (từ càng hiếm càng nặng — vì vậy từ viết
  sai chính tả, vốn hiếm, có thể được ưu tiên sai).

## 9.18 Truy xuất mật độ và Dual Encoder (Dense Retrieval)

**Truy xuất mật độ** (dense retrieval) khắc phục giới hạn từ vựng bằng cách nhúng câu
hỏi và tài liệu vào không gian vector rồi đo độ gần. Kiến trúc chuẩn là **dual encoder**
từ DPR [@karpukhin-dpr-2020]:

$$\mathrm{score}(q, p) = E_Q(q) \cdot E_P(p)$$

với $E_Q$ là bộ mã hóa câu hỏi, $E_P$ là bộ mã hóa đoạn; tích vô hướng (hoặc cosine) đo
độ tương tự. DPR được huấn luyện bằng mất mát đối lập (contrastive) với âm tính trong
batch (in-batch negatives) cộng một âm tính khó BM25 (hard negative) mỗi ví dụ
[@karpukhin-dpr-2020] — chính xác là kỹ thuật lấy mẫu âm mà Ch8 đã dạy, giờ áp dụng cho
bài toán retriever.

**Điểm mạnh:**
- Bắt được paraphrase và tương tự ngữ nghĩa mà khớp từ bỏ sót: "tốc độ biến thiên" và
  "đạo hàm theo thời gian" có thể gần nhau trong không gian nhúng.
- Khi được huấn luyện tốt, dense retrieval vượt BM25 đáng kể trên các benchmark hỏi đáp
  mở [@karpukhin-dpr-2020].

**Giới hạn:**
- Giống nhất không bằng đúng: vector gần nhất có thể là một đoạn nói *ngược lại* đúng
  cách dùng từ.
- Điểm nhúng là tín hiệu xếp hạng, không phải liên quan chắc chắn, càng không phải chân lý.
- Nhạy phiên bản mô hình: cùng một pass, hai phiên bản encoder cho hai thứ hạng khác nhau.

**Ranh giới quan trọng từ Ch8 được mở rộng sang miền này:** Ch8 đã dạy
**entity ≠ embedding** — thực thể không phải vector của nó [@hogan-inductive]. Nguyên lý
này áp dụng nguyên vẹn cho câu hỏi và văn bản:

> **Vector câu hỏi ≠ ý nghĩa câu hỏi; vector đoạn ≠ nội dung đoạn.** Nhúng là biểu diễn
> học được phục vụ xếp hạng, không phải bản chất của đối tượng.

**MUST NOT suy ra:**
- Không được khẳng định độ tương tự nhúng cao đảm bảo liên quan.
- Không được khẳng định dense retrieval luôn thắng lexical retrieval.
- Không được coi kết quả nhúng đứng đầu là bằng chứng.

## 9.19 So sánh: khi nào lexical, khi nào dense

Bảng 9.2 tóm tắt quyết định chọn họ truy xuất văn bản (BOOK-DEFINED, dựa trên đặc tính
của hai họ [@robertson-bm25-2009] [@karpukhin-dpr-2020]):

| Tiêu chí | Lexical (BM25) | Dense (DPR) |
|---|---|---|
| Thuật ngữ chính xác | rất tốt | trung bình (nhạy paraphrase) |
| Đồng nghĩa / paraphrase | kém | tốt |
| Không cần huấn luyện | có | không (cần model + dữ liệu) |
| Diễn giải được | cao | thấp |
| Nhạy lỗi chính tả | nhạy (idf đẩy từ lạ lên) | bền hơn |
| Chi phí | thấp | trung bình (mỗi đoạn cần nhúng) |

Nguyên tắc vận hành thực tế trong chương: **không chọn một, mà dùng cả hai theo kiểu
truy xuất lai** (§9.20) — lexical giữ recall cho thuật ngữ chính xác, dense mở rộng cho
paraphrase. Đây không phải một công thức vạn năng cho kết quả "đúng hơn"; nó là một
chiến lược bền hơn trước đa dạng cách diễn đạt.

## 9.20 Truy xuất lai (Hybrid Retrieval)

**Truy xuất lai** chạy song song nhiều retriever (lexical + dense + có thể là truy vấn đồ
thị) rồi gộp các danh sách xếp hạng. Động lực: các retriever khác nhau trượt theo những
cách khác nhau — BM25 trượt khi không có từ chung, dense trượt khi một cụm từ hiếm quyết
định. Kết hợp làm tăng khả năng *ít nhất một hệ* thấy được mảnh quan trọng.

Nhưng phải giữ trung thực về kỳ vọng:

> **Nhiều tín hiệu hơn ≠ câu trả lời đúng hơn.** Hybrid làm giảm rủi ro *bỏ sót*, không
> làm tăng *độ đúng* của nội dung. Nếu cả ba hệ cùng đưa vào một đoạn sai bài bản,
> hybrid hợp nhất sai.

![Ba họ truy xuất: văn bản (chunk độc lập), đồ thị (cấu trúc liên kết), và hybrid (đồ thị dẫn dắt + văn bản) — mỗi họ mạnh theo một cách khác, không họ nào "đúng hơn" tuyệt đối.](figures/generated/ch09-text-vs-graph-vs-hybrid.pdf)

Chi tiết kỹ thuật của việc gộp danh sách — **hợp hạng** — ở phần tiếp theo.

**MUST NOT suy ra:**
- Không được khẳng định hybrid đảm bảo liên quan hoặc đúng.
- Không được khẳng định hybrid luôn tốt hơn từng thành phần.

## 9.21 Hợp hạng (Rank Fusion) và RRF

Khi có nhiều danh sách xếp hạng từ các retriever khác nhau, cần gộp thành một danh sách.
Vấn đề: điểm của các hệ không so sánh được (BM25 tính theo thang của nó, cosine theo
thang của nó). **RRF** (Reciprocal Rank Fusion) giải quyết bằng cách chỉ dùng *hạng*
[@cormack-rrf-2009]:

$$\mathrm{RRF}(d) = \sum_{s \in \mathrm{systems}} \frac{1}{k + \mathrm{rank}_s(d)}$$

với $k$ thường là 60. Đọc: *"mỗi hệ đóng góp theo vị trí của tài liệu trong danh sách của
hệ đó; hạng càng thấp, đóng góp càng nhỏ"*

Điểm mạnh: không cần chuẩn hóa điểm, bền với các thang không tương thích, và kết hợp
tốt các danh sách pure hạng [@cormack-rrf-2009]. Đây là lựa chọn tự nhiên cho hybrid
(lexical + dense + tín hiệu đồ thị).

**Ngữ nghĩa điểm hợp:** điểm RRF là *tiện ích truy xuất tổng hợp* — nó nói vị trí tương
đối tốt của một tài liệu trong mắt các hệ. Nó **không phải** độ tin cậy, không phải xác
suất, không phải cường độ bằng chứng.

**MUST NOT suy ra:**
- Không được diễn giải điểm hợp RRF như độ tin cậy.
- Không được khẳng định RRF chọn ra bằng chứng (nó chỉ xếp hạng ứng viên).
- Không được dùng điểm RRF làm trị số assessment (giá trị đánh giá) của Ch6.

## 9.22 Đồ thị trước vs Văn bản trước (Graph-first vs Text-first)

Một câu hỏi kiến trúc quan trọng: khi bắt đầu truy xuất, nên **đi từ đồ thị ra văn bản**
(graph-first) hay **từ văn bản vào đồ thị** (text-first)?

- **Graph-first:** câu hỏi → liên kết thực thể → lấy cấu trúc/đồ thị con → mở rộng sang
  các đoạn văn bản gắn với các nút. Phù hợp khi lược đồ đã biết, thực thể phân giải được,
  và câu hỏi thiên cấu trúc (cơ chế, vai trò).
- **Text-first:** câu hỏi → đoạn văn (BM25/dense) → từ đoạn phát hiện thực thể/claim →
  mở rộng vào đồ thị. Phù hợp khi câu hỏi mở, thực thể mơ hồ, hoặc cần định nghĩa từ
  nguồn trước khi nói đến cấu trúc.

Trong GraphRAG, hai chế độ truy vấn chính phản ánh đúng hai hướng này: **Local Search**
khởi đầu từ thực thể (graph-first) cho câu hỏi về thực thể; **Global Search** khởi đầu
từ tóm tắt cộng đồng cho câu hỏi toàn cục [@edge-graphrag-2024] [@microsoft-graphrag-docs].

**Nguyên tắc trung thực:** không có bên nào luôn thắng. Câu hỏi cơ chế trong hệ tri thức
của chúng ta thường *thiên graph-first* (schema đã biết); câu hỏi định nghĩa mở từ nguồn
*thiên text-first*. Router (§9.8) chọn hướng theo intent.

**MUST NOT suy ra:**
- Không được khẳng định thứ tự truy cập quyết định tính đúng.
- Không được tuyên bố một bên luôn thắng giữa graph-first và text-first.

---

# Phần D — Truy xuất theo tri thức luận

## 9.23 Chiếu hình vs Sổ cái (Canonical View vs Claim Ledger)

Đây là khác biệt tri thức luận quan trọng nhất của chương. Từ Ch6–Ch7, hệ thống lưu một
**Claim Ledger** (Sổ cái claim: mọi claim có provenance, có trạng thái, có lịch sử) và
duy trì một **canonical view** (chiếu hình: trạng thái "hiện được chấp nhận là gì").

Truy xuất phải *chọn đúng nguồn theo intent*:

- Câu hỏi **FACTUAL/STRUCTURAL** ("vận tốc là gì?") → truy xuất chiếu hình: định nghĩa
  đang được chấp nhận.
- Câu hỏi **PROVENANCE/TEMPORAL/CONTRADICTION** ("ai từng phản đối?", "định nghĩa 2020?")
  → truy xuất Sổ cái: lịch sử claim, các claim cạnh tranh, các phiên bản đã bị thay thế.

Vi phạm kinh điển: trả lời câu hỏi *lịch sử/tranh cãi* bằng chiếu hình hiện tại. Hình
9.3 minh họa hai miền truy xuất khác nhau.

![Truy xuất theo tri thức luận: Canonical View trả lời "hiện được chấp nhận là gì"; Claim Ledger trả lời "đã từng được đề xuất/tranh cãi gì". Hỏi lịch sử hay mâu thuẫn phải vào Sổ cái, không phải chiếu hình.](figures/generated/ch09-ledger-vs-canonical.pdf)

**Formal meaning:** hai miền truy xuất: chiếu hình (state: Accepted, hiện hành) và Sổ cái
(bất biến, có trạng thái + lịch sử); lựa chọn miền là một quyết định tri thức luận theo
intent, không phải chi tiết truy vấn.

**Trong sách:** "Chiếu hình trả lời 'hiện được chấp nhận là gì'; Sổ cái trả lời 'đã từng
được đề xuất/tranh cãi gì'. Hỏi lịch sử/mâu thuẫn phải vào Sổ cái."

**MUST NOT suy ra:**
- Không được suy "chiếu hình trống" ⇒ "Sổ cái trống" (chiếu hình có thể trống vì chưa có
  claim Accepted, trong khi Sổ cái chứa đầy ứng viên).
- Không được khẳng định định nghĩa đang được chấp nhận là định nghĩa duy nhất từng được
  đề xuất.

## 9.24 Truy xuất theo trạng thái quản trị (Governance-aware Retrieval)

Từ Ch6, mỗi claim mang một trạng thái quản trị: `Accepted`, `Candidate`, `Contested`,
`Rejected`, `Superseded`. Truy xuất có thể lọc hoặc ưu tiên theo trạng thái này — và
*việc lọc phải theo intent*:

| Intent | Chính sách trạng thái mặc định |
|---|---|
| Sản xuất / FAQ | chỉ `Accepted` (và ghi chú nếu có tranh cãi) |
| Nghiên cứu / so sánh | `Accepted` + `Contested` + `Superseded` (kèm trạng thái) |
| Lịch sử tri thức | mọi trạng thái theo đúng thời điểm |
| Kiểm toán | mọi trạng thái, cả `Rejected` (để hiểu vì sao bị bác) |

Nguyên tắc tri thức luận: **không một trạng thái nào tự nó là chân lý.** `Accepted` có
nghĩa "được quản trị chấp nhận", không phải "đúng với thế giới"; `Rejected` có nghĩa
"không lọt quản trị", không phải "sai với thế giới". Truy xuất trình bày trạng thái như
một dữ kiện provenance của bằng chứng, không như một kết luận.

**MUST NOT suy ra:**
- Không được khẳng định `Rejected` ⇒ sai với thế giới.
- Không được khẳng định `Accepted` ⇒ đúng (được quản trị ≠ được chứng minh).
- Không được lọc hết mọi claim không-Accepted cho mọi loại câu hỏi (điều này phá hỏng
  câu hỏi mâu thuẫn/lịch sử).

## 9.25 Truy xuất thời gian: nhiều đồng hồ (Temporal Retrieval)

Câu hỏi "Định nghĩa current năm 2020 là gì?" nghe đơn giản nhưng chứa một cái bẫy: *năm
2020 là thời điểm gì?* Từ Ch6, hệ thống có nhiều đồng hồ độc lập:

- **valid time** (thời gian hiệu lực): khẳng định `ElectricCurrent` được định nghĩa áp
  dụng từ/thay đổi khi nào;
- **publication time / assertion time** (thời gian công bố/khẳng định): claim được đưa
  vào hệ từ nguồn nào, khi nào;
- **transaction/system time** (thời gian hệ thống): hệ thống *tin* điều đó từ khi nào,
  và tin đến khi nào trước khi bị thay thế.

Ba đồng hồ này không trùng nhau. "Định nghĩa current áp dụng từ 2019 (valid), được công
bố 2021 (publication), và hệ thống tin từ 2022 (system)" là hoàn toàn hợp lệ. Vì vậy:

- "Hệ thống tin gì vào năm 2020?" → truy xuất theo **system time**.
- "Định nghĩa áp dụng năm 2020 là gì?" → truy xuất theo **valid time**.
- "Điều gì được công bố năm 2020?" → truy xuất theo **publication time**.

**Formal meaning:** truy xuất thời gian = chọn đồng hồ + mốc thời gian theo intent; các
đồng hồ độc lập và không được lẫn.

**Nguy hiểm khi đơn giản hóa:** trả lời mọi câu hỏi "năm X" bằng trạng thái hiện tại,
hoặc gộp ba đồng hồ làm một.

**MUST NOT suy ra:**
- Không được khẳng định sự thật hiện tại được tin trong quá khứ.
- Không được trộn valid time với publication time.
- Không được trả lời câu hỏi hiệu lực bằng bản ghi công bố (và ngược lại).

## 9.26 Truy xuất nguồn gốc (Provenance-aware Retrieval)

Câu hỏi thường gặp nhất và khó nhất về tri thức luận: **"Vì sao hệ thống tin điều này?"**
Trả lời câu hỏi này cần một loại truy xuất đặc biệt — truy xuất nguồn gốc — đi dọc chuỗi
provenance được xây từ Ch6 (PROV lineage):

```
Claim #C471
  ← supports:  Evidence #E88
  ← derivedFrom: SourceFragment "đạo hàm theo thời gian..."
  ← wasAttributedTo: SourceArtifact (sách, trang, xuất bản)
  ← wasGeneratedBy: ExtractionActivity (model, phiên bản, tham số)
  + assessments: độ tin cậy, tính nhất quán, mức độ hỗ trợ
  + governance: trạng thái, người/hoạt động quyết định, thời điểm
```

Chuỗi này ghép thành một **đồ thị giải thích** (explanation subgraph). Khái niệm then
chốt song song với nghiên cứu attribution trong NLP: một phát biểu về thế giới là
**attributable to identified sources** nếu (các) nguồn được xác định hỗ trợ nó
[@rashkin-ais-2021]. Truy xuất nguồn gốc chính là cơ chế để hệ thống có thể chứng minh
"attribution" theo cách đó.

**Formal meaning:** truy xuất nguồn gốc = lấy chuỗi Claim→Evidence→SourceFragment→
SourceArtifact→(hoạt động, đánh giá, quản trị) và lắp thành đồ thị giải thích; sự tồn tại
của chuỗi là dữ kiện, không phải bằng chứng về tính đúng.

**MUST NOT suy ra:**
- Không được khẳng định sự tồn tại chuỗi nguồn gốc chứng minh tính đúng.
- Không được coi một đoạn nguồn là độc lập với chuỗi trích xuất đã tạo ra nó (đoạn có
  thể là kết quả của một phép trích xuất sai).

## 9.27 Truy xuất nhạy mâu thuẫn (Contradiction-aware Retrieval)

Khi câu hỏi đụng vào một khái niệm đang tranh cãi — tức Sổ cái có nhiều claim cùng chủ
đề với trạng thái/đánh giá khác nhau — truy xuất thông thường (lấy top bằng chứng của
một phía) sẽ *giấu* sự tranh cãi. **Truy xuất nhạy mâu thuẫn** phải:

1. Nhận diện chủ đề đang tranh cãi (nhiều claim cùng chủ đề, trạng thái đối lập);
2. Truy xuất **các claim cạnh tranh** và **phạm vi** của từng claim (claim phản đối có
   thể chỉ giới hạn trong một miền con);
3. Đưa tất cả vào Gói bằng chứng — *không* ép LLM tự chọn bên thắng mà không có chính
   sách/bằng chứng.

Ví dụ: claim `C471: "RATE_OF_CHANGE mô tả bản chất vận tốc"` và claim
`C210: "đạo hàm chỉ là mô hình; vận tốc có bản chất định nghĩa riêng"` cùng chủ đề nhưng
phạm vi khác nhau. Truy xuất nhạy mâu thuẫn trả cả hai kèm phạm vi; LLM trình bày "theo
một số nguồn là ..., theo các quan điểm khác ...", thay vì chọn đại.

**Formal meaning:** truy xuất nhạy mâu thuẫn = khi nút/cụm claim có nhiều ứng viên đối
lập, trả về tập claim cạnh tranh kèm phạm vi và trạng thái, và duy trì ràng buộc "không
hợp nhất các claim mâu thuẫn mất phạm vi".

**MUST NOT suy ra:**
- Không được khẳng định nguồn điểm cao hơn là đúng.
- Không được gộp các claim mâu thuẫn mà không giữ phạm vi của chúng.
- Không được trả lời câu hỏi mâu thuẫn từ chiếu hình (chỉ có một phía).

## 9.28 Đa dạng bằng chứng (Evidence Diversity)

Một câu trả lời giải thích tốt cần bằng chứng **đa dạng** chứ không chỉ *nhiều*: nhiều
bản sao cùng một nguồn không làm tăng sức thuyết phục. Các chiều đa dạng (BOOK-DEFINED):

- **Đa nguồn:** đoạn nguồn từ các tài liệu độc lập, không phải một tài liệu trích nhiều
  lần;
- **Đa loại:** cấu trúc (đường cơ chế) + claim (được quản trị) + văn bản (đoạn nguồn) —
  ba loại bổ sung nhau như §9.9;
- **Đa quan điểm:** nếu chủ đề tranh cãi, gồm cả các claim đối lập (§9.27);
- **Đa thời điểm:** nếu câu hỏi về tiến hóa, gồm cả các phiên bản cũ (§9.25).

Nghịch lý truy xuất: LLM có xu hướng "chắc chắn hơn" khi thấy nhiều đoạn giống nhau —
nhưng số lượng đoạn *trùng quan điểm từ cùng một nguồn gốc* là một dạng đo lường lặp
(pseudo-replication), không phải bằng chứng độc lập. Chính sách đa dạng phòng điều này.

**MUST NOT suy ra:**
- Không được khẳng định nhiều đoạn trùng nguồn = nhiều bằng chứng.
- Không được giả định mọi loại đơn vị đều cần trong mọi câu trả lời (chính sách theo intent).

## 9.29 top_k là Ranh giới Tri thức luận (top_k as Epistemic Bound)

Khái niệm trung tâm của toàn chương, được nhắc trong các pipeline RAG chuẩn
[@lewis-rag-2020] [@karpukhin-dpr-2020]: mọi truy xuất xếp hạng đều *cắt* ở một ngưỡng
top_k. Từ Ch7, cuốn sách đã dạy top_k là một ranh giới ngầm. Ở đây nó được nâng thành
nguyên lý:

> **top_k là ranh giới tri thức luận: mô hình không suy luận được trên bằng chứng nó
> không thấy.** Với câu hỏi giải thích, kết quả thay đổi toàn bộ nếu bằng chứng quyết
> định nằm ở hạng 6 mà top_k=5.

Đồng thời, cạm bẫy ngược cũng thật:

- **top_k quá nhỏ** → mất bằng chứng quyết định → câu trả lời "hợp lý" mà thiếu nửa sự
  thật (Hình 9.4).
- **top_k quá lớn** → ngập nhiễu và distractor → LLM "lạc" giữa đống ngữ cảnh, độ chính
  xác giảm chứ không tăng.

![top_k như ranh giới tri thức luận: bằng chứng quyết định nằm ngoài cửa sổ top_k thì hệ thống không biết nó tồn tại — "không trong top_k" ≠ "không liên quan".](figures/generated/ch09-topk-bound.pdf)

**Chính sách của chương:** top_k không phải một hằng số. Nó được điều chỉnh theo loại câu
hỏi (câu hỏi mâu thuẫn cần recall cao hơn) và được *ghi vào provenance truy xuất* để
người đọc câu trả lời biết ranh giới họ đang nhìn.

**MUST NOT suy ra:**
- Không được suy "không nằm trong top_k" ⇒ "không liên quan" hoặc "không tồn tại".
- Không được khẳng định tăng top_k đơn điệu cải thiện câu trả lời.
- Không được xem top_k như chi tiết ống dẫn trung tính (nó là ranh giới tri thức luận).

## 9.30 Đo lường truy xuất: Precision, Recall, P@K, R@K, MRR, nDCG

Để đánh giá tầng truy xuất (tách khỏi tầng sinh), cần các độ đo từ IR [@manning-ir-2008]
[@jarvelin-ndcg-2002]. Định nghĩa với tập liên quan chuẩn $R$ và tập đã truy xuất $A$:

- **Precision** = $|R \cap A|\,/\,|A|$ — trong số đã lấy, bao nhiêu là liên quan.
- **Recall** = $|R \cap A|\,/\,|R|$ — trong số đáng lấy, đã lấy được bao nhiêu.

Hai độ đo đánh đổi nhau: nâng recall (lấy nhiều hơn) thường hạ precision (thêm rác). Với
câu hỏi giải thích, recall thấp là thảm họa ngầm (§9.29); với câu hỏi có nhiều distractor,
precision thấp làm hỏng tổng hợp.

**Khi truy xuất xếp hạng thay vì trả tập phẳng**, dùng các độ đo theo cutoff:

- **P@K**: trong top-K, bao nhiêu liên quan.
- **R@K**: trong top-K, bao nhiêu *phần của toàn bộ tập liên quan* bị cắt ra.

Ví dụ làm việc: kho có 8 đoạn liên quan cho câu hỏi Q0; truy xuất top-5 chứa 4 trong số
đó. Khi đó P@5 = 4/5 = 0.8, R@5 = 4/8 = 0.5. Một hệ thống "chất lượng cao" có P@5=1.0
nhưng R@5=0.25 (chỉ 2/8 liên quan) — bề ngoài hoàn hảo, thực tế giấu 6/8 bằng chứng.

- **MRR** (Mean Reciprocal Rank): trung bình của 1/hạng của *kết quả liên quan đầu tiên*
  [@manning-ir-2008]. Phù hợp khi người dùng chỉ cần câu trả lời đúng đầu tiên.
- **nDCG** (normalized Discounted Cumulative Gain): chấm *độ liên quan bậc thang*
  (graded, ví dụ 0/1/2/3) thay vì nhị phân, chiết khấu theo vị trí log, và chuẩn hóa
  bằng thứ tự lý tưởng [@jarvelin-ndcg-2002]:

$$\mathrm{DCG}@k = \sum_{i=1}^{k} \frac{\mathrm{rel}_i}{\log_2(i+1)}, \qquad
\mathrm{nDCG}@k = \frac{\mathrm{DCG}@k}{\mathrm{IDCG}@k}$$

**Ngữ nghĩa thống nhất của TẤT CẢ các độ đo này:** chúng đo *chất lượng xếp hạng so với
một tập đánh giá liên quan (relevance judgments)* — không phải độ đúng của câu trả lời,
không phải chân lý, không phải độ tin cậy tri thức luận.

**Chú thích quan trọng về sự kế thừa:** MRR xuất hiện ở Ch8 cho link prediction. Hệ số
đo lường dùng chung, nhưng *đối tượng* khác nhau: Ch8 đánh giá dự đoán liên kết (bộ ba
ứng viên), chương này đánh giá truy xuất (đơn vị bằng chứng). Không được mượn ngữ nghĩa
của MRR-Ch8 làm "chân lý truy xuất".

**MUST NOT suy ra:**
- Không được khẳng định P@K/R@K/MRR/nDCG đo độ đúng của câu trả lời.
- Không được so sánh nDCG giữa các thang liên quan khác nhau.
- Không được tính các độ đo này mà thiếu tập liên quan chuẩn (gold relevance) rõ nghĩa.

## 9.31 Tái xếp hạng (Reranking)

Kiến trúc hai giai đoạn: **giai đoạn đầu rộng và rẻ** — lexical/dense lấy ra một túi ứng
viên lớn (ví dụ 100–1000) — sau đó **giai đoạn hai lại cho sắc** bằng một re-ranker mạnh
hơn nhưng chậm hơn, chấm *từng cặp (câu hỏi, ứng viên)* một cách liên kết
[@nogueira-rerank-2019]. Nghiên cứu gốc của BERT re-ranking đã chứng minh lợi ích MRR@10
trên MS MARCO khi cross-encoder thấy đồng thời câu hỏi và đoạn [@nogueira-rerank-2019].

Re-ranker có thể là:

- **Cross-encoder** (BERT) — chấm cặp (q, p) cùng lúc [@nogueira-rerank-2019];
- **LLM re-ranker** — hỏi LLM "đoạn nào liên quan hơn" (đắt, cần giám sát);
- **Re-ranker có đặc trưng đồ thị** (BOOK-DEFINED) — bổ sung khoảng cách đồ thị, loại
  quan hệ, cơ chế dùng chung, trạng thái quản trị, sự sẵn có của provenance, sự khớp
  thời gian, đa dạng nguồn vào quyết định liên quan. **Lưu ý đặc biệt:** không có một
  công thức trọng số phổ quát được sách xác nhận — việc kết hợp các tín hiệu là *chính
  sách theo bài toán*, phải ghi rõ.

Ranh giới thiết yếu:

> **Tái xếp hạng không cứu được recall.** Nếu giai đoạn đầu bỏ sót đoạn quyết định,
> re-ranker xuất sắc đến đâu cũng không thấy nó để đưa lên. Lỗi tầng một là lỗi chí mạng.

**MUST NOT suy ra:**
- Không được khẳng định điểm re-ranker là độ tin cậy.
- Không được kỳ vọng re-ranker sửa lỗi recall của tầng một.
- Không được khẳng định LLM re-ranking đảm bảo đúng.
- Không được công bố một công thức trọng số tín hiệu như "chuẩn" khi nó chỉ là chính
  sách của một bài toán.

---

# Phần E — Lắp ráp ngữ cảnh và sinh câu trả lời

## 9.32 Lắp ráp ngữ cảnh (Context Assembly)

Sau khi truy xuất, các đơn vị bằng chứng (đường cấu trúc, claim, đoạn nguồn, mâu thuẫn,
provenance, dữ kiện thời gian) phải được **lắp ráp** thành đầu vào cho LLM. Lắp ráp là
một quyết định thiết kế có ngữ nghĩa, không phải phép nối chuỗi:

- **Chọn:** đơn vị nào vào cửa sổ (theo §9.28 đa dạng và §9.29 ranh giới);
- **Nhóm:** gom theo chủ đề/khía cạnh (cấu trúc chung, bằng chứng, mâu thuẫn, nguồn gốc);
- **Sắp thứ tự:** đặt bằng chứng quyết định ở vị trí được đọc tin cậy nhất (§9.34);
- **Dán nhãn:** mỗi khối kèm loại, trạng thái, và nguồn gốc.

Chuẩn hóa từ nghiên cứu: RAG gốc nối câu hỏi với các đoạn đã truy xuất để tạo đầu vào
generator [@lewis-rag-2020]. Chương này mở rộng: đầu vào không chỉ là "câu hỏi + đoạn"
mà là "câu hỏi + gói bằng chứng có cấu trúc".

**MUST NOT suy ra:**
- Không được khẳng định thứ tự lắp ráp không ảnh hưởng kết quả (nó ảnh hưởng, §9.34).
- Không được khẳng định càng nhiều ngữ cảnh càng nhiều tri thức (nhiễu cũng tăng).

## 9.33 Nén ngữ cảnh (Context Compression)

Khi tập bằng chứng vượt cửa sổ, cần **nén**: bỏ trùng, tóm tắt vùng lân cận, giữ đường đi
quyết định, chọn đại diện. Ba kỹ thuật:

1. **Khử trùng (dedupe):** bỏ các đoạn trùng nguồn/trùng nội dung (§9.28).
2. **Chọn đại diện (representative selection):** giữ đoạn hỗ trợ đầy đủ nhất cho mỗi
   claim quan trọng.
3. **Tóm tắt (summarization):** rút gọn vùng lân cận/đồ thị con thành lời văn gọn.

Kỹ thuật 3 là nơi nguy hiểm nhất:

> **Tóm tắt là đồ tạo tác dẫn xuất — không phải nguồn.** Một tóm tắt có thể vứt mất bằng
> chứng quyết định, làm mất sắc thái của mâu thuẫn, và trở nên lỗi thời khi nguồn đổi.
> Tóm tắt phải giữ liên kết provenance về nguồn gốc của nó [@rashkin-ais-2021].

Đây cũng là nguyên tắc vận hành của tóm tắt cộng đồng trong GraphRAG (§9.56): chúng là
sản phẩm LLM có provenance, là đầu vào ứng viên — không phải tri thức chuẩn
[@edge-graphrag-2024] [@microsoft-graphrag-docs].

**MUST NOT suy ra:**
- Không được khẳng định tóm tắt tương đương nguồn.
- Không được khẳng định nén giữ được mọi bằng chứng.
- Không được nhét tóm tắt vào KG chuẩn mà không qua quản trị (Ch6/Ch7).

## 9.34 Lost in the Middle: thứ tự ngữ cảnh ảnh hưởng độ tin cậy

Nghiên cứu thực nghiệm trên các mô hình ngôn ngữ dài đã chỉ ra: **thông tin ở đầu và
cuối cửa sổ ngữ cảnh được mô hình dùng đáng tin cậy hơn thông tin ở giữa** — hiệu ứng
"lost in the middle" [@liu-lostmid-2023]. Khi đoạn quyết định nằm giữa một ngữ cảnh dài,
chất lượng trả lời tụt rõ rệt so với khi nó ở đầu hoặc cuối.

Hệ quả kỹ thuật cho tầng lắp ráp:

- Đặt bằng chứng quyết định (đường cơ chế, claim chấp nhận, đoạn nguồn chính) ở đầu hoặc
  cuối cửa sổ;
- Không chôn các mâu thuẫn quan trọng vào giữa đống bằng chứng phụ;
- Khi cửa sổ dài, giảm kỳ vọng mô hình "nhìn thấy" được mọi chi tiết giữa cửa sổ.

**Lưu ý cam kết:** kết quả là thực nghiệm trên các mô hình/công việc cụ thể — không nâng
nó thành định luật phổ quát, nhưng hệ quả kỹ thuật (thứ tự ảnh hưởng chất lượng) là thật
và phải được thiết kế theo [@liu-lostmid-2023].

**MUST NOT suy ra:**
- Không được khẳng định mọi mô hình chịu ảnh hưởng như nhau.
- Không được dùng nghiên cứu này để biện minh việc sắp xếp lại thứ tự một cách tùy tiện.
- Không được coi vị trí ngữ cảnh là cơ chế *đúng/sai*, chỉ là yếu tố *độ tin cậy*.

## 9.35 Tuần tự hóa đồ thị cho LLM (Graph Serialization)

LLM đọc văn bản, không đọc trực tiếp RDF. Vì vậy cấu trúc đồ thị phải được **tuần tự
hóa** thành dạng chữ. Các lựa chọn và đánh đổi:

| Dạng | Ví dụ | Ưu | Nhược |
|---|---|---|---|
| Triple | `C_app operation DerivativeOperation` | chính xác, không suy diễn thêm | dài, thiếu ngữ cảnh |
| Bảng | bảng vai trò × ứng dụng | so sánh trực quan | cồng kềnh khi nhiều nút |
| JSON | cấu trúc lồng | máy đọc được | người đọc kém tự nhiên |
| Lời văn gọn | "cả hai ứng dụng đều dùng phép đạo hàm theo thời gian" | gọn, tự nhiên | mất cấu trúc, dễ lẫn với suy luận của mô hình |
| Thẻ bằng chứng | Evidence Card có trường cố định | vết được (BOOK-DEFINED) | khung cứng |

Nguyên tắc: **không có một dạng tuần tự hóa giữ nguyên toàn bộ ngữ nghĩa.** RDF thô thì
chính xác mà tốn token; lời văn thì gọn mà dễ "dịch chuyển" ý nghĩa — đặc biệt nguy hiểm
nếu mô hình trình bày lại như thể đó là suy luận của chính nó. Chính sách của chương:
với câu hỏi cấu trúc, ưu tiên triple/bảng kèm nhãn "đây là dữ liệu đồ thị"; với câu hỏi
giải thích, dùng cả cấu trúc lẫn lời văn và dán nhãn từng loại.

**MUST NOT suy ra:**
- Không được khẳng định một dạng tuần tự hóa giữ nguyên mọi ngữ nghĩa.
- Không được coi việc viết cấu trúc thành lời văn là mất mát bằng không.

## 9.36 Gói bằng chứng (Evidence Packet) — BOOK ENGINEERING MODEL

**Gói bằng chứng** (Evidence Packet) là khái niệm kiến trúc do cuốn sách định nghĩa
(BOOK-DEFINED): một container có cấu trúc, là **giao diện duy nhất giữa tầng truy xuất
và tầng sinh câu trả lời**. Thay vì ném các chunk rời vào LLM, tầng truy xuất đóng gói
mọi thứ tầng sinh cần để trả lời một cách trung thực.

Cấu trúc chuẩn của một Gói bằng chứng (Hình 9.5):

```
EvidencePacket
├─ question (gốc) + interpreted_intent (kèm độ mơ hồ)
├─ resolved_entities (mỗi thực thể: id, độ chắc, ghi chú mơ hồ)
├─ canonical_claims    (claim Accepted liên quan + trạng thái)
├─ competing_claims    (Contested/Superseded + phạm vi + trạng thái)
├─ structural_paths    (đường cấu trúc đã duyệt + giới hạn độ sâu)
├─ source_passages     (đoạn nguồn để trích dẫn + nguồn gốc)
├─ provenance_chain    (Claim→Evidence→SourceFragment→SourceArtifact)
├─ temporal_scope      (đồng hồ nào + mốc nào được dùng)
├─ assessments         (đánh giá Ch6 liên quan)
├─ retrieval_metadata  (retriever, phiên bản, index snapshot, top_k, scores, reranker)
└─ statuses            (mỗi mục được dán nhãn: asserted / derived / predicted)
```

![Gói bằng chứng (Evidence Packet, BOOK-DEFINED): container có cấu trúc — câu hỏi, intent, thực thể, claim, đường đi, đoạn nguồn, provenance, thời gian, đánh giá, metadata truy xuất, và nhãn trạng thái tri thức luận.](figures/generated/ch09-evidence-packet.pdf)

Vì sao cần một cấu trúc như vậy thay vì "cứ truy xuất rồi đổ vào prompt"?

1. **Tách trách nhiệm:** tầng truy xuất chịu trách nhiệm *lấy đúng gì*; tầng sinh chịu
   trách nhiệm *tổng hợp trung thực*. Gói bằng chứng khiến ranh giới này kiểm tra được.
2. **Dán nhãn tri thức luận:** mỗi mục trong gói mang nhãn `asserted` (khẳng định từ
   nguồn), `derived` (suy dẫn âm thanh, Ch5), hay `predicted` (dự đoán từ mô hình, Ch8).
   Ba mức không được trộn lẫn (xem §9.60).
3. **Provenance đầy đủ:** câu trả lời sau này "vì sao nói điều này" chính là đọc lại Gói
   bằng chứng đã cấp.

**Lưu ý trung thực:** một Gói bằng chứng "đầy đủ trường" không đảm bảo *đủ bằng chứng*
— nó có thể đầy mà vẫn thiếu mảnh quyết định (lỗi recall §9.30), hoặc đầy nhiễu. Gói
bằng chứng là điều kiện cần cho câu trả lời tốt, không phải điều kiện đủ.

**MUST NOT suy ra:**
- Không được khẳng định gói đầy ⇒ bằng chứng đủ.
- Không được khẳng định nội dung gói là đúng với thế giới.
- Không được gọi việc đổ chunk thô vào prompt là "gói bằng chứng".

## 9.37 Sinh câu trả lời (Answer Generation)

Tầng sinh nhận Gói bằng chứng và tạo bản nháp câu trả lời. Trong RAG gốc, generator là
mô hình seq2seq đọc câu hỏi + đoạn đã truy xuất [@lewis-rag-2020]; trong kiến trúc của
chương, generator đọc câu hỏi + gói bằng chứng và phải tuân thủ bốn kỷ luật:

1. **Không thêm quan hệ ngoài gói:** mọi khẳng định mới về quan hệ giữa các thực thể mà
   không có trong gói là hành vi bị cấm (đây là nguồn hallucination chính, §9.66).
2. **Tách bạch các phát ngôn:** câu trả lời gồm các loại khác nhau — tóm tắt cấu trúc,
   so sánh, giải thích đường đi, phát biểu không chắc chắn, tuyên bố chưa biết — và mỗi
   loại được viết khác đi.
3. **Trình bày mâu thuẫn thay vì chọn bên** (khi gói chứa claim cạnh tranh).
4. **Tự kiểm tra trước khi phát:** đối chiếu mỗi câu với mục trong gói (self-check §9.67).

**Formal meaning:** sinh câu trả lời = ánh xạ (câu hỏi, Evidence Packet) → bản nháp, với
ràng buộc không phát minh quan hệ; bản nháp phân biệt được các câu được hỗ trợ, suy luận,
không chắc, chưa biết.

**MUST NOT suy ra:**
- Không được khẳng định văn bản sinh ra đã được xác minh với thế giới.
- Không được khẳng định một câu trả lời trôi chảy là một câu trả lời có căn cứ.

## 9.38 Claim con trong câu trả lời (Answer Claims)

Một câu trả lời không phải một khối đơn nhất — nó phân rã được thành **các claim con**
(AnswerClaims). Ví dụ câu trả lời cho Q0 có thể tách thành:

- **A1:** "VelocityDerivativeApplication và CurrentDerivativeApplication đều là ứng dụng
  của cơ chế RATE_OF_CHANGE." — được hỗ trợ bởi đường cấu trúc + claim Accepted.
- **A2:** "Cả hai đều lấy đạo hàm theo thời gian (withRespectTo=Time)." — được hỗ trợ
  bởi bảng vai trò.
- **A3:** "Điều này có nghĩa vận tốc 'về bản chất là' một tốc độ biến thiên." — **suy
  luận**, cần nhãn khác; có thể bị claim C210 phản đối.
- **A4:** "Không tồn tại cơ chế nào khác điều khiển vận tốc." — **chưa biết** (chưa tìm
  hết), không được viết như sự thật.

Phân rã claim con cho phép đánh giá *theo câu*: trích dẫn, độ hỗ trợ, mức trung thành —
thay vì chấm cả đoạn một khối [@gao-cite-2023] [@rashkin-ais-2021].

**MUST NOT suy ra:**
- Không được khẳng định mọi claim con đều kiểm chứng được với thế giới.
- Không được khẳng định câu trả lời có một câu được trích dẫn là đã được trích dẫn đầy đủ.

## 9.39 Câu trả lời có căn cứ (Grounded Answer)

Một câu trả lời **có căn cứ** (grounded) nghĩa là nó được hỗ trợ bởi các nguồn mà hệ
thống đã xác định — thuộc tính "attributable to identified sources" (AIS) [@rashkin-ais-2021].
Đây là khái niệm trung tâm của đánh giá attribution: *văn bản sinh ra về thế giới bên
ngoài là attributable nếu nguồn đã xác định hỗ trợ nó*.

Ranh giới tri thức luận quyết định:

> **Có căn cứ ≠ đúng.** Một câu trả lời có thể hoàn toàn có căn cứ — từng claim đều được
> một nguồn xác định hỗ trợ — mà vẫn sai với thế giới, nếu nguồn đó sai, lỗi thời, hoặc
> được diễn giải sai. Groundedness là thuộc tính của quan hệ *câu trả lời–nguồn*, không
> phải quan hệ *câu trả lời–thế giới* [@rashkin-ais-2021].

Ngược lại, một câu trả lời đúng với thế giới mà không có nguồn trong hệ thống hỗ trợ là
"đúng may mắn" — không thể phòng vệ trong kiểm toán.

**MUST NOT suy ra:**
- Không được suy "có căn cứ" ⇒ "đúng".
- Không được suy "không có căn cứ" ⇒ "sai" (có thể đúng mà không vết được).

## 9.40 Trích dẫn và độ đầy đủ trích dẫn (Citation & Citation Completeness)

**Trích dẫn** gắn một claim con của câu trả lời với *bằng chứng thực sự hỗ trợ nó* và
nguồn gốc của bằng chứng đó. Benchmark ALCE định nghĩa hai độ đo bổ sung nhau
[@gao-cite-2023]:

- **Citation recall** — bao nhiêu phần *các câu/claim cần hỗ trợ* đã có trích dẫn;
- **Citation precision** — trong số trích dẫn, bao nhiêu trích dẫn *thực sự hỗ trợ* câu
  được gắn.

Hai độ đo tách hai lỗi khác nhau: thiếu trích dẫn (lỗi recall) và trích dẫn nhầm (lỗi
precision). Nghiên cứu ALCE cũng chỉ ra rằng ngay cả các mô hình mạnh cũng gặp khó khăn
trong việc trích dẫn đầy đủ từng claim [@gao-cite-2023] — vì vậy chương này dạy trích dẫn
như một *đầu ra cần được kiểm tra*, không phải một tùy chọn làm đẹp.

Quy tắc trích dẫn của chương (BOOK-DEFINED):

1. Mỗi claim con quan trọng, có thể kiểm chứng được → tối thiểu một trích dẫn.
2. Trích dẫn phải trỏ tới *đoạn nguồn thật sự chứa thông tin hỗ trợ* — không trỏ tài liệu
   chỉ vì nó nằm trong gói.
3. Trích dẫn suy luận (A3 ở §9.38) phải trỏ tới *đường cấu trúc/claim* làm tiền đề, và
   được dán nhãn "suy luận từ ...".
4. Khi câu trả lời trình bày mâu thuẫn, mỗi phía phải có trích dẫn riêng.

**MUST NOT suy ra:**
- Không được khẳng định có trích dẫn ⇒ được hỗ trợ.
- Không được khẳng định mọi tài liệu trong gói là trích dẫn được (chỉ đoạn thực sự hỗ
  trợ mới đáng trích).
- Không được đếm số trích dẫn thay cho kiểm tra từng claim (coverage).

## 9.41 Trung thành (Faithfulness) ≠ Đúng (Correctness)

**Trung thành** (faithfulness) đo quan hệ giữa câu trả lời và *ngữ cảnh được cấp*: câu
trả lời không bịa, không mâu thuẫn với ngữ cảnh đó. Trong thuật ngữ của chương:

> **Trung thành = câu trả lời nằm trong phạm vi hỗ trợ của Gói bằng chứng.**

Ranh giới then chốt: trung thành là thuộc tính **câu trả lời–ngữ cảnh**, hoàn toàn khác
với đúng là thuộc tính **câu trả lời–thế giới**:

- Một câu trả lời có thể **trung thành mà sai**: nếu gói chứa nguồn sai/lỗi thời, và mô
  hình tóm tắt trung thực nguồn đó, kết quả "trung thành với nguồn sai" vẫn sai.
- Một câu trả lời có thể **đúng mà không trung thành với gói**: mô hình bỏ gói, dùng tri
  thức tiềm ẩn của nó trả lời đúng — đây là "đúng may mắn", không kiểm soát được.

**MUST NOT suy ra:**
- Không được suy "trung thành" ⇒ "đúng".
- Không được suy "không trung thành với ngữ cảnh" ⇒ "sai với thế giới".

## 9.42 Bảng 2×2: Đúng vs Có căn cứ (Correctness × Groundedness)

Kết hợp hai trục — *đúng với thế giới* (correctness) và *có căn cứ trong gói* (grounded)
— ta có bảng 2×2 quyết định (Hình 9.6):

| | Có căn cứ (grounded) | Không có căn cứ |
|---|---|---|
| **Đúng** (correct) | **C** — mục tiêu: đúng và được hỗ trợ | **A** — đúng "may mắn": không vết được |
| **Sai** (wrong) | **B** — trung thành với nguồn sai | **D** — sai và bịa |

- Ô **C** là mục tiêu của mọi thiết kế: đúng với thế giới *và* mỗi claim đều được nguồn
  xác định hỗ trợ.
- Ô **B** là cạm bẫy nguy hiểm nhất về mặt kiểm toán: hệ thống "làm đúng quy trình" —
  truy xuất, lắp ráp, trích dẫn đầy đủ — mà vẫn sai vì nguồn sai. **Quy trình tốt không
  chuyển ô B thành ô C**; chỉ đánh giá bên ngoài (người dùng, đối chiếu) làm được.
- Ô **A** là "đúng may mắn": LLM dùng tri thức tiềm ẩn bỏ qua gói; không thể phòng vệ
  và không lặp lại được.
- Ô **D** là hallucination toàn diện.

![Bảng 2×2 đúng/căn cứ: mục tiêu là ô C (đúng và được hỗ trợ); ô B (trung thành với nguồn sai) là cạm bẫy kiểm toán — quy trình tốt không biến ô B thành ô C.](figures/generated/ch09-correctness-grounding.pdf)

Hệ quả thiết kế: đánh giá câu trả lời phải đo *cả hai trục*, không được gộp thành một
điểm. Chương này và §9.61 xây quy trình đánh giá theo đúng hai trục này.

**MUST NOT suy ra:**
- Không được khẳng định câu trả lời có căn cứ tự động ở ô C.
- Không được chấm một trục duy nhất rồi tuyên bố chất lượng.
- Không được dùng "quy trình đã đúng" để kết luận "câu trả lời đúng" (ô B là bằng chứng
  phản).

## 9.43 Kiêng trả lời (Abstention)

Khi bằng chứng không đủ, hành vi đúng của hệ thống là **kiêng trả lời**: nói rõ "không
đủ bằng chứng" thay vì bịa một câu trả lời trôi chảy. Các điều kiện kiêng (BOOK-DEFINED):

1. **Không có claim liên quan** — không tìm thấy gì trong Sổ cái/chiếu hình;
2. **Thực thể chưa phân giải** — mention mơ hồ chưa quyết được (§9.5);
3. **Mâu thuẫn chưa thể phân xử** — các claim đối lập đều có sức nặng, chưa có chính
   sách/chỉ số để chọn;
4. **Hỗ trợ yếu** — claim tồn tại nhưng đánh giá thấp/không nhất quán;
5. **Ngoài phạm vi** — câu hỏi vượt miền tri thức của hệ thống;
6. **Sự không chắc của truy xuất cao** — độ mơ hồ diễn giải lớn (§9.3).

Kiêng trả lời *không phải* một lỗi — nó là hành vi tri thức luận đúng đắn. Câu trả lời
kiêng phải nói được *loại thiếu* nào đang xảy ra (xem §9.44), để người dùng biết đi tiếp
thế nào.

**MUST NOT suy ra:**
- Không được khẳng định kiêng trả lời ⇒ sự kiện là sai (thiếu bằng chứng ≠ sai).
- Không được coi kiêng trả lời là lỗi hệ thống khi nó là hành vi đúng theo chính sách.
- Không được kiêng quá sớm khi lỗi thật nằm ở tầng truy xuất (§9.44).

## 9.44 Không biết vs Không tìm thấy; Lỗi truy xuất vs Thiếu tri thức

Chuỗi phân biệt cuối cùng của phần này — và là một trong những chuỗi quan trọng nhất của
chương:

> **KHÔNG TRUY XUẤT ĐƯỢC ≠ KHÔNG CÓ TRONG INDEX ≠ KHÔNG CÓ TRONG KG ≠ ĐÃ BIẾT SAI ≠
> CHƯA BIẾT.**

Năm trạng thái tri thức luận khác nhau, và hệ thống phải nói rõ nó đang ở trạng thái nào:

1. **Not found by this retrieval** — kế hoạch truy xuất không tìm thấy (có thể do top_k,
   độ sâu, retriever kém);
2. **Not in index** — index không chứa (index tụt hậu, §9.10);
3. **Not in KG** — đồ thị/Sổ cái không có claim (nhưng OWA từ Ch4: không có ≠ sai);
4. **Known false** — có đánh giá bác bỏ (chỉ khi Sổ cái có bằng chứng bác);
5. **Unknown** — không đủ thông tin ở mọi cấp.

Kèm theo đó là một chẩn đoán tách bạch hai loại lỗi:

> **Lỗi truy xuất ≠ Thiếu tri thức.** Nếu claim đúng *có trong Sổ cái* mà retriever bỏ
> sót, lỗi thuộc tầng truy xuất (top_k, index, embedding, độ sâu), không phải "hệ thống
> không biết". Chẩn đoán sai sẽ dẫn đến sửa sai chỗ: đổ thêm dữ liệu trong khi vấn đề là
> cấu hình retriever.

**MUST NOT suy ra:**
- Không được suy "không có kết quả truy xuất" ⇒ "không có tri thức".
- Không được suy "không tìm thấy" ⇒ "sai".
- Không được đổ lỗi cho KG/mô hình khi lỗi thật ở cấu hình truy xuất.

---

# Phần F — Truy xuất động và agentic

## 9.45 Lập kế hoạch truy vấn và thực thi (Query Planning & Execution)

Trong §9.8, kế hoạch truy xuất đã được giới thiệu như một chuỗi phép truy xuất. Ở đây ta
đi sâu vào *ai lập kế hoạch*. Có ba lựa chọn, không bắt buộc phải dùng LLM:

1. **Quy tắc cứng (rule-based):** intent FACTUAL/STRUCTURAL → chuỗi cố định; rẻ, xác
   định, kiểm tra được.
2. **Planner LLM:** cho intent + kho phép truy xuất, LLM đề xuất chuỗi; linh hoạt cho
   câu bất thường, nhưng cần giám sát và giới hạn (LLM có thể "phát minh" một chuỗi
   truy xuất vô nghĩa).
3. **Lai:** quy tắc cho các mẫu phổ biến, LLM cho ngoại lệ: lập kế hoạch thay đổi route
   của router (§9.71).

**MUST NOT suy ra:**
- Không được khẳng định LLM *bắt buộc* lập kế hoạch.
- Không được khẳng định kế hoạch là chân lý xác định (planner có thể sai).
- Không được khẳng định bất kỳ planner nào là không thể sai.

## 9.46 Tĩnh vs Agentic Retrieval

- **Tĩnh (static):** chạy kế hoạch một lượt, lắp rắp, sinh câu trả lời. Đủ cho câu hỏi
  đơn giản/đơn chặng. RAG gốc là kiểu tĩnh một-pass [@lewis-rag-2020].
- **Agentic / lặp (iterative):** sau mỗi lượt truy xuất, kiểm tra khoảng trống và phát
  hành lượt truy vấn tiếp theo. Hữu ích cho câu hỏi đa bước ("tìm cơ chế, rồi tìm các
  ứng dụng khác của cơ chế đó, rồi tìm bằng chứng từng ứng dụng").

Agentic không tự động tốt hơn:

| Rủi ro agentic | Vì sao |
|---|---|
| Trôi câu hỏi | mỗi lượt lệch xa intent (§9.48) |
| Leo thang nhiễu/cost | mỗi lượt thêm token, thêm độ trễ |
| Thiên kiến xác nhận | các lượt sau thường chỉ củng cố lượt trước (§9.49) |
| Không hội tụ | không có điều kiện dừng → lặp vô hạn (§9.47) |

**MUST NOT suy ra:**
- Không được khẳng định truy xuất lặp đảm bảo trả lời tốt hơn.
- Không được khẳng định nhiều lượt truy xuất luôn đáng chi phí.

## 9.47 Điều kiện dừng (Stopping Conditions)

Agentic retrieval phải có **điều kiện dừng tường minh** (BOOK-DEFINED), vì "cứ tìm thêm
cho chắc" là sai lầm tuần hoàn — thêm bằng chứng có thể thêm nhiễu và chi phí. Các điều
kiện dừng hợp lệ:

1. **Đủ ô bằng chứng:** mọi claim con quan trọng của câu hỏi đã có mục trong gói
   (theo chính sách của từng intent, §9.4);
2. **Không có thông tin mới:** lượt truy xuất mới không thêm đơn vị liên quan đáng kể;
3. **Ngưỡng liên quan:** điểm/tỷ lệ mới giảm dưới ngưỡng;
4. **Hết ngân sách:** đã dùng hết số lượt/token cho phép → *báo cáo trạng thái thiếu*,
   không tiếp tục mù quáng;
5. **Mâu thuẫn cần con người:** các claim đối lập đều có sức nặng → dừng và chuyển lên
   quyết định của người/policy.

**Lưu ý trung thực:** hầu hết các điều kiện dừng chỉ đảm bảo *quy trình ngừng*, không
đảm bảo *đã đủ bằng chứng*. Báo cáo cuối phải ghi điều kiện dừng nào đã kích hoạt —
ngân sách hết thì kết quả là "thiếu do ngân sách", không phải "đầy đủ".

**MUST NOT suy ra:**
- Không được suy dừng-tìm ⇒ đầy đủ.
- Không được suy kết quả giới hạn-ngân-sách là đầy đủ.

## 9.48 Trôi câu hỏi (Query Drift)

**Trôi câu hỏi** là lỗi tích lũy của truy xuất lặp: mỗi lượt subquery lệch thêm khỏi
intent gốc. Ví dụ thực tế trong miền liên tục:

```
Lượt 1: "cơ chế của RATE_OF_CHANGE"          → intent gốc: cấu trúc cơ chế
Lượt 2: "phép đạo hàm"                       → co hẹp sang toán học
Lượt 3: "đạo hàm trong tài chính"            → trôi sang miền khác
```

Đến lượt 4, hệ thống "thành công" truy xuất được các đoạn về đạo hàm tài chính — hoàn
toàn xa intent gốc, nhưng mọi bước đều hợp lệ cục bộ. Đây là lý do phải **giữ một bản
ghi intent gốc** và so sánh mỗi lượt với nó, cùng việc ghi provenance cho từng subquery
(con nào sinh từ con nào).

**MUST NOT suy ra:**
- Không được khẳng định các lượt truy xuất sau đang đánh giá cùng câu hỏi gốc.
- Không được bỏ qua việc ghi nguồn gốc của subquery (làm mất khả năng phát hiện drift).

## 9.49 Thiên kiến xác nhận trong truy xuất (Confirmation Bias)

Khi hệ thống (hoặc người dùng) bắt đầu với một giả thuyết — "vận tốc và dòng điện về
bản chất là cùng cơ chế" — truy xuất một chiều sẽ chỉ lấy bằng chứng ủng hộ. Chuỗi phân
biệt của chương:

> **Bằng chứng ủng hộ ≠ sự thật.** Một hệ thống chỉ truy xuất phía ủng hộ là một hệ
> thống *xác nhận* chứ không *kiểm định*.

Ví dụ: câu hỏi Q5 (có claim nào phản đối/giới hạn sự tương ứng không?) phải vào Sổ cái
tìm các claim đối lập — không chỉ để "trình bày khách quan" mà vì **phản ví dụ là dữ
liệu chính** của một câu trả lời giải thích trung thực. Bỏ qua phía phản đối là một lỗi
tri thức luận, không chỉ một lỗi thiếu sót.

**MUST NOT suy ra:**
- Không được suy tập bằng chứng chỉ-ủng-hộ ⇒ giả thuyết đúng.
- Không được khẳng định một cuộc truy xuất "thấu đáo" khi nó chỉ lấy một phía.

## 9.50 Truy xuất kiểm định giả thuyết (Hypothesis-testing Retrieval)

Đây là cầu nối trực tiếp với Ch8. Giả sử Ch8 đã sinh giả thuyết cơ chế ứng viên
(CandidateMechanismHypothesis): "vận tốc, dòng điện, và tăng trưởng dân số chia sẻ cơ
chế RATE_OF_CHANGE". Truy xuất ở đây đóng vai *giao diện kiểm định* [@edge-graphrag-2024]:

- Truy xuất **ủng hộ**: các ứng dụng hiện có, các claim Accepted khẳng định tương ứng;
- Truy xuất **thách thức**: các âm tính khó — finite difference (tốc độ trung bình khác
  đạo hàm tức thời), tỉ lệ (tăng trưởng %) khác đạo hàm tuyệt đối, gradient, tích lũy —
  tất cả đều là *ứng viên cạnh tranh* với cơ chế đạo hàm;
- Truy xuất **ranh giới**: định nghĩa chính xác của từng khái niệm để phát hiện phạm vi
  không khớp.

Kết quả: một câu trả lời trung thực không khẳng định "ba hiện tượng là cùng cơ chế" một
cách tuyệt đối, mà trình bày sự tương ứng *có giới hạn và có cạnh tranh*: "về mặt cấu
trúc derivative, chúng giống nhau; về mặt ý nghĩa số, có sự khác biệt ...".

**MUST NOT suy ra:**
- Không được suy không-có-thách-thức ⇒ giả thuyết được chấp nhận.
- Không được khẳng định giả thuyết đã kiểm định bằng truy xuất là tri thức được chấp
  nhận (vẫn là ứng viên cho đến khi qua Ch6/Ch7).

## 9.51 Câu hỏi local vs global

GraphRAG phân biệt hai loại câu hỏi với hai chiến lược truy xuất khác nhau
[@edge-graphrag-2024]:

- **LOCAL** — về một thực thể/đồ thị con cụ thể: "Định nghĩa dòng điện là gì?" — cần
  truy xuất neo thực thể (entity-anchored): giải quyết thực thể → đồ thị con/vùng lân
  cận of nó → bằng chứng gắn.
- **GLOBAL** — về mô hình chung trên toàn bộ đồ thị: "Các cơ chế nào được dùng nhiều
  nhất trong hệ tri thức này?" — câu trả lời không nằm ở một thực thể mà nằm *trên toàn
  cục*; cần chiến lược tổng hợp phân cấp hoặc truy vấn tổng hợp (§9.56).

**Nguyên tắc:** không có một chiến lược duy nhất cho cả hai. Định nghĩa được mô hình hóa
bởi từng câu hỏi theo §9.4 — intent 8/9 (discovery/multi-hop) thường nghiêng global.

**MUST NOT suy ra:**
- Không được khẳng định câu trả lời toàn cục tồn tại trong từng thực thể con.
- Không được khẳng định truy xuất local đủ cho câu hỏi global.

---

# Phần G — GraphRAG và hệ truy xuất hoàn chỉnh

## 9.52 GraphRAG là một họ kiến trúc, không phải một thuật toán chuẩn

Thuật ngữ **GraphRAG** nghe như một kỹ thuật đơn nhất, nhưng thực tế là một *họ* kiến
trúc: các phương pháp retrieval-augmented generation dùng cấu trúc đồ thị tường minh
trong quá trình truy xuất/lắp ráp ngữ cảnh — trái với RAG thuần chỉ dựa trên các đoạn
văn bản độc lập [@edge-graphrag-2024].

Nghiên cứu gốc "From Local to Global" mô tả một đường ống cụ thể [@edge-graphrag-2024]:

```
TextUnits → LLM trích thực thể/quan hệ/claim
  → đồ thị entity/relation/claim
  → phát hiện cộng đồng Leiden
  → tóm tắt cộng đồng từ dưới lên (bottom-up)
  → truy xuất theo câu hỏi:
      Local Search  (fan-out quanh thực thể)
      Global Search (map-reduce trên tóm tắt cộng đồng)
```

Tài liệu chính thức của Microsoft mô tả một hiện thực hiện công khai (MIT license) với
các chế độ search: Global, Local, DRIFT, Basic [@microsoft-graphrag-docs]. Điều quan trọng cho
ngữ nghĩa của cuốn sách:

> **Microsoft GraphRAG là MỘT hiện thực của họ GraphRAG — không phải định nghĩa của
> GraphRAG.** Tóm tắt cộng đồng là *một lựa chọn thiết kế*; cấu trúc đồ thị trong truy
> xuất là đặc điểm trung tâm của họ, không phải của riêng một sản phẩm.

**Cảnh báo tiếp thị:** bất kỳ hệ thống nào "thêm chút đồ thị" vào RAG cũng có thể tự gọi
là GraphRAG; từ đó nói lên rất ít về chất lượng. Trong sách, cụm từ "GraphRAG" luôn đi
kèm mô tả *cấu trúc cụ thể nào* đang được dùng.

**MUST NOT suy ra:**
- Không được khẳng định GraphRAG là một thuật toán chuẩn hóa duy nhất.
- Không được khẳng định Microsoft GraphRAG là chuẩn của GraphRAG.
- Không được khẳng định GraphRAG đảm bảo trả lời tốt hơn, hay loại bỏ hallucination.

## 9.53 RAG vs KGQA vs GraphRAG: bảng quyết định

Ba cơ chế hỏi đáp thường bị nhầm lẫn. Phân biệt theo *cơ chế trả lời* [@chakraborty-kgqa-2019]
[@lewis-rag-2020] [@edge-graphrag-2024]:

| Tiêu chí | KGQA | Text RAG | GraphRAG |
|---|---|---|---|
| Cơ chế trả lời | truy vấn/suy luận cấu trúc trên đồ thị | truy xuất đoạn văn + sinh | đồ thị dẫn dắt truy xuất ngữ cảnh + sinh |
| Kết quả | bộ kết quả/tập | văn bản sinh | văn bản sinh (ngữ cảnh có cấu trúc) |
| Sự kiện chính xác | rất mạnh | trung bình (cần grounding) | trung bình-cao |
| Câu hỏi mở/định nghĩa | yếu (cần mapping) | mạnh | mạnh |
| Giải thích dạng đường | trực tiếp | gián tiếp | trung gian |

Bảng quyết định của router (§9.8, §9.71):

| Câu hỏi | Đường tốt nhất | Vì sao |
|---|---|---|
| "Vận tốc là ứng dụng của cơ chế nào?" (thực thể rõ, schema biết) | **KGQA** — truy vấn đồ thị chính xác | chính xác tuyệt đối, chi phí thấp [@chakraborty-kgqa-2019] |
| "Định nghĩa 'current' 2020?" | **KGQA temporal / ledger** | cần chính xác về thời gian + trạng thái |
| "Cái gì tương tự 'tốc độ biến thiên' trong tài liệu?" (mở) | **Text RAG** | không có schema để truy vấn chính xác |
| "Vì sao vận tốc và dòng điện cùng cơ chế?" (cấu trúc + bằng chứng) | **GraphRAG/hybrid** | cần cấu trúc + đoạn nguồn phối hợp |
| "Các cơ chế phổ biến nhất?" (toàn cục) | **GraphRAG Global** | cần tổng hợp chéo cộng đồng [@edge-graphrag-2024] |

**Điểm mấu chốt:** không có cơ chế nào "tốt hơn" tuyệt đối — mỗi cơ chế mạnh ở một vùng
câu hỏi. Câu hỏi cấu trúc chính xác mà đi qua RAG/LLM là *lãng phí và thêm rủi ro bịa*;
câu hỏi mở mà ép thành SPARQL là *vô dụng*.

![So sánh ba cơ chế hỏi đáp: KGQA (truy vấn chính xác trên đồ thị), Text RAG (đoạn văn + sinh), GraphRAG (đồ thị dẫn dắt truy xuất + sinh). Bổ sung nhau, không thay thế nhau.](figures/generated/ch09-kgqa-rag-graphrag.pdf)

**MUST NOT suy ra:**
- Không được gọi mọi RAG "có đồ thị" là KGQA.
- Không được khẳng định câu hỏi truy vấn xác định được cần RAG.
- Không được khẳng định GraphRAG thay thế được KGQA cho các câu hỏi chính xác.

## 9.54 Đường đi là giải thích, không phải chứng minh

Một trong những sức mạnh của hỏi đáp trên đồ thị là **giải thích theo đường đi**: trình
bày câu trả lời kèm chuỗi quan hệ "vì sao". Ví dụ:

> "Velocity được sinh ra bởi VelocityDerivativeApplication — một ứng dụng của cơ chế
> RATE_OF_CHANGE, trong đó operation = DerivativeOperation, withRespectTo = Time. Vì vậy
> vận tốc được phân loại là một tốc độ biến thiên."

Đường đi này là *giải thích cấu trúc*: nó cho thấy câu trả lời bám vào cấu trúc đồ thị
nào. Nhưng ranh giới tri thức luận phải được giữ (khác biệt này ở khắp chương, xem
§9.12):

> **Đường đi ≠ suy dẫn logic.** Một đường đi cho thấy đồ thị gắn kết các khái niệm theo
> một cách nào đó, trong phạm vi độ sâu được duyệt với các quan hệ được chọn. Nó không
> chứng minh các quan hệ đúng với thế giới, không chứng minh không có đường phản đối.

Thêm một bước phân biệt: đường đi *cấu trúc* (structural path) khác với *suy diễn*
(entailment, Ch5). Suy diễn là phép suy ra hệ quả theo ngữ nghĩa; đường đi là sự kiện
kết nối. Trình bày đường đi như "vì vậy" là hợp lệ; trình bày như "đã chứng minh" là
vượt quyền.

**MUST NOT suy ra:**
- Không được trình bày đường đi như một suy dẫn.
- Không được khẳng định sự tồn tại đường đi ⇒ đúng.

## 9.55 Bùng nổ đường đi (Path Explosion)

Khi đồ thị lớn và kết nối dày đặc, số đường đi giữa hai nút tăng theo cấp số nhân. Ví
dụ: trong phạm vi 3 chặng từ `VelocityDerivativeApplication`, các đường đi đi qua
`DerivativeOperation`, `RATE_OF_CHANGE`, `Time`, `Position`, các lớp cha, các nguồn, các
claim liên quan — và mỗi nút nhánh lại mở thêm nhánh. Đây là **bùng nổ đường đi** (path
explosion): nếu liệt kê mọi đường, ngữ cảnh sập.

Ba đối sách (BOOK-DEFINED):

1. **Giới hạn cấu trúc (§9.13):** độ sâu, loại quan hệ, kiểu nút — cắt phân nhánh ngay
   từ đầu;
2. **Ưu tiên đường quyết định:** về mặt giải thích, *một* đường quyết định (đường trả
   lời được intent) đáng giá *một nghìn* đường phụ; giữ đường quyết định, gom phần còn
   lại (đường phản đối thì §9.27);
3. **Khử trùng cấu trúc:** bỏ các đường lặp vai trò/xoay vòng (cycle) không thêm thông
   tin.

**MUST NOT suy ra:**
- Không được khẳng định liệt kê được "mọi đường" (bùng nổ là tính chất thật của đồ thị).
- Không được khẳng định đường được chọn là đường "duy nhất đúng" — chỉ là đường quyết
  định theo chính sách truy xuất.

## 9.56 Truy xuất cộng đồng và phân cấp (Community / Hierarchical Retrieval)

Khi đồ thị lớn, một chiến lược cho câu hỏi toàn cục là **phân cụm rồi tóm tắt theo cấp**:
phát hiện cộng đồng (trong GraphRAG gốc dùng Leiden) và sinh tóm tắt từ dưới lên cho từng
cộng đồng [@edge-graphrag-2024] [@microsoft-graphrag-docs]. Truy xuất global sau đó map-reduce
trên các tóm tắt này để trả lời câu hỏi về toàn cục.

Ba rủi ro phải quản lý:

1. **Mất thông tin trong tóm tắt:** tóm tắt nén mất bằng chứng chi tiết;
2. **Cộng đồng không ổn định:** khi đồ thị đổi vài claim, phân cụm có thể nhảy hẳn — câu
   trả lời global đổi dù nội dung hầu như không đổi;
3. **Tóm tắt lỗi thời:** tóm tắt cũ không còn phản ánh đồ thị hiện tại;
4. **Mất provenance:** người đọc khó vết "tóm tắt này từ đâu mà có".

Chính sách (nối tiếp §9.33): tóm tắt cộng đồng là **đồ tạo tác dẫn xuất có provenance**
model/version/nguồn — là *đầu vào ứng viên*, không phải tri thức chuẩn. Không được âm
thầm quy tóm tắt thành chân lý.

**MUST NOT suy ra:**
- Không được khẳng định tóm tắt cộng đồng là thành phần bắt buộc của mọi GraphRAG.
- Không được khẳng định tóm tắt là đầy đủ.
- Không được nhét tóm tắt vào KG chuẩn nếu không qua quản trị.

## 9.57 Cache và nhất quán index

Hệ thống có thể **cache** nhiều thứ: kết quả phân giải thực thể, kết quả truy xuất,
subgraph đã chọn, tóm tắt, và cả câu trả lời. Cache giảm chi phí nhưng mang lại **sự
lỗi thời**, vì hệ tri thức không ngừng tiến hóa (§9.10). Chính sách (BOOK-DEFINED):

- Khóa cache nơi cần sự chính xác phải gắn **phiên bản** của: KG/Sổ cái snapshot,
  index version, ontology version, retriever version;
- Câu trả lời cached phải mang nhãn thời điểm trạng thái hệ thống mà nó phản ánh;
- Khi Sổ cái đổi (claim mới/Superseded), cache liên quan phải bị vô hiệu hoặc đánh dấu.

**MUST NOT suy ra:**
- Không được khẳng định câu trả lời cached phản ánh tri thức hiện tại.
- Không được phục vụ cache cũ như thể nó là trạng thái mới.

## 9.58 Provenance truy xuất và hồ sơ câu trả lời (Retrieval & Answer Provenance)

**Provenance truy xuất** ghi lại *vì sao mảnh này được đưa cho mô hình*: câu hỏi gốc,
diễn giải, các retriever và phiên bản, index snapshot, bộ lọc, top_k, điểm số, re-ranker,
quy tắc mở rộng, thời gian. Đủ để tái hiện và gỡ lỗi.

**Hồ sơ câu trả lời** (Answer artifact, BOOK ENGINEERING MODEL — PROV-O [@prov-o]) ghi:

```
Answer
  └─ generatedFor → Question
  └─ usedEvidence → EvidencePacket
  └─ generatedBy → AnswerGenerationActivity
  └─ generatedAt → time
  └─ modelVersion / promptConfigVersion
  └─ citations → (claim con ↔ đoạn nguồn)
  └─ answerStatus → SUPPORTED | PARTIAL | CONTESTED | ABSTAINED | UNKNOWN
```

Hai loại provenance này là dữ kiện *tái hiện được*, không phải bằng chứng về tính đúng:
một hồ sơ hoàn hảo vẫn có thể là hồ sơ của một câu trả lời sai (ô B, §9.42).

**MUST NOT suy ra:**
- Không được khẳng định provenace truy xuất chứng minh tính đúng.
- Không được khẳng định điểm số ghi lại là độ tin cậy của câu trả lời.
- Không được tuyên bố câu trả lời là audit-able khi không có hồ sơ truy xuất.

## 9.59 Câu trả lời QA ≠ Tri thức thu nhận (QA Answer ≠ Knowledge Ingestion)

Đây là một trong những ranh giới quản trị quan trọng nhất của toàn bộ cuốn sách:

> **Một câu trả lời của hệ thống QA không tự động trở thành tri thức mới được chấp nhận.**

Quy trình đúng có dạng vòng:

```
KG/chính → retrieval → answer → (nếu phát hiện tri thức ứng viên mới)
  → CandidateClaim → Ch7 integration pipeline (đánh giá, bằng chứng, quản trị)
  → (nếu Accepted) → mới vào Sổ cái
```

Cấm có vòng tắt `answer -> insert into KG` không qua quản trị. Nguyên nhân: câu trả lời
là sản phẩm của đường ống có lỗi (retrieval miss, nguồn sai, LLM bịa); đưa thẳng vào KG
là *đóng băng lỗi thành tri thức* và mở vòng tự củng cố (nhắc lại model collapse — Ch8
§8.34 tương tự ở cấp hệ thống).

**MUST NOT suy ra:**
- Không được suy "hệ thống trả lời được" ⇒ "hệ thống biết điều đó".
- Không được chèn câu trả lời vào KG bỏ qua quản trị.
- Không được khẳng định Answer là Claim Accepted (hai loại bản ghi khác nhau).

## 9.60 Ngữ nghĩa điểm số, xếp hạng đa tín hiệu, và ba trạng thái tri thức luận

**Ngữ nghĩa điểm số (score semantics).** Trong một quy trình truy xuất có nhiều loại
điểm: BM25 (tiện ích xếp hạng từ vựng), cosine/dot-product (tín hiệu nhúng), điểm
re-ranker (tiện ích xếp hạng liên kết), khoảng cách đồ thị (cấu trúc), độ ưu tiên luật.
Ranh giới duy nhất phải giữ:

> **Mọi điểm trong đường ống truy xuất đều là tín hiệu xếp hạng — không tín hiệu nào là
> xác suất đúng của câu trả lời.**

**Xếp hạng đa tín hiệu (multi-signal ranking, BOOK-DEFINED).** Khi gộp nhiều tín hiệu để
đánh giá liên quan, sự gộp là *chính sách theo bài toán*: độ khớp văn bản, độ tương tự
nhúng, khoảng cách đồ thị, loại quan hệ, trạng thái quản trị, thời gian hiệu lực, chất
lượng nguồn, và đa dạng bằng chứng có thể kết hợp — nhưng không có công thức trọng số
phổ quát. Quy tắc của chương: công bố rõ chính sách gộp, đừng giả vờ một hằng số vạn năng.

**Ba trạng thái tri thức luận (mandatory).** Mỗi mục trong Gói bằng chứng mang nhãn:

- **ASSERTED** — khẳng định từ nguồn/Sổ cái (có nguồn xác định);
- **DERIVED** — suy dẫn bằng suy luận âm thanh theo ngữ nghĩa (Ch5), tiền đề là asserted;
- **PREDICTED** — dự đoán bởi mô hình học (Ch8), là ứng viên, có điểm số.

Ba mức này không được trộn: một câu trả lời viết "dòng điện tỉ lệ nghịch điện trở"
(predicted) phải khác với khi viết "dòng điện được mô hình hóa là đạo hàm theo thời
gian" (asserted+derived). Trạng thái được ghi trong hồ sơ câu trả lời (§9.58) để người
đọc phân biệt được mức độ tin cậy.

**MUST NOT suy ra:**
- Không được khẳng định predicted = asserted.
- Không được khẳng định derived = asserted với thế giới.
- Không được trình bày dự đoán như sự kiện được chấp nhận.
- Không được lưu một điểm truy xuất như "độ tin cậy" của câu trả lời.

---

# Phần H — Đánh giá, ca làm việc và ranh giới

## 9.61 Đánh giá truy xuất theo 7 tầng

Đánh giá một hệ thống hỏi đáp bằng một con số end-to-end là sai lầm phổ biến nhất: nó
không cho biết lỗi nằm ở tầng nào. Chương này dạy đánh giá **theo tầng** (BOOK-DEFINED):

| Tầng | Câu hỏi đo | Độ đo/kiểm tra |
|---|---|---|
| 1. Liên kết thực thể | mention → thực thể đúng? | accuracy trên tập mơ hồ/khó |
| 2. Truy xuất | đơn vị liên quan có trong top_k? | P@K, R@K, MRR, nDCG (§9.30) |
| 3. Đủ bằng chứng | gói có chứa mọi claim con quan trọng? | kiểm tra gold evidence (§9.62) |
| 4. Căn cứ (grounding) | mỗi câu trả lời được gói hỗ trợ? | AIS-style đánh giá [@rashkin-ais-2021] |
| 5. Đúng (correctness) | đúng với thế giới? | đánh giá ngoài (người/chuyên gia) |
| 6. Trích dẫn | recall/precision trích dẫn? | ALCE metrics [@gao-cite-2023] |
| 7. Hành vi ranh giới | ứng xử với mâu thuẫn/unknown? | test §9.63 |

Mỗi tầng có công cụ riêng; một hệ thống có thể đạt 100% ở tầng 2 và thất bại thảm hại ở
tầng 4 (đúng bằng chứng, sai tổng hợp). Ngược lại, hệ thống thất bại ở tầng 2 sẽ kéo
theo mọi tầng sau — chẩn đoán theo tầng là cách duy nhất biết chữa đâu.

**MUST NOT suy ra:**
- Không được suy chỉ số truy xuất tốt ⇒ câu trả lời tốt.
- Không được khẳng định một con số duy nhất xác định được tầng lỗi.

## 9.62 Bằng chứng vàng (Gold Evidence) và QA benchmark

**Bằng chứng vàng** là tập chú thích "đơn vị nào nên được truy xuất cho câu hỏi này" —
tương đương relevance judgment trong IR [@manning-ir-2008]. Ví dụ cho câu hỏi Q0:

```
gold_evidence(Q0) = {
  structural: VelocityDerivativeApplication, CurrentDerivativeApplication,
              RATE_OF_CHANGE, vai trò operation/differentiand/withRespectTo/produces,
  claims:     claim Accepted "Velocity = derivative application of RATE_OF_CHANGE",
              claim phản đối (nếu có),
  passages:   đoạn nguồn định nghĩa vận tốc + đạo hàm theo thời gian
}
```

Dùng để đo tầng 2–3 (§9.61): hệ thống truy xuất được bao nhiêu phần của gold?

**QA benchmark** của chương là bộ câu hỏi gắn với tri thức của hệ thống, với mỗi câu có:
intent, gold evidence, gold answer (theo ô C của bảng 2×2 — *đúng và có căn cứ*), và các
biến thể adversarial (§9.63).

**Lưu ý cam kết:** gold evidence là *chú thích của bộ dữ liệu*, không phải chân lý siêu
hình. Nó có thể sai, thiếu, lỗi thời — giống mọi đánh giá của con người. Đánh giá so với
gold là đo *khớp với chú thích*, không phải đo *chân lý*.

**MUST NOT suy ra:**
- Không được coi gold annotation là không thể sai.
- Không được suy điểm so với gold ⇒ đúng với thế giới.

## 9.63 Test đối kháng: distractor, mâu thuẫn, thời gian

Ngoài benchmark chuẩn, hệ thống cần các **test đối kháng** — cố tình gài bẫy để kiểm tra
ranh giới tri thức luận (BOOK-DEFINED, nối tiếp khái niệm âm tính khó của Ch8
[@edge-graphrag-2024]):

1. **Distractor test:** chèn các đoạn giống bề mặt nhưng không liên quan/sai hướng vào
   kho — hệ thống có bị lừa chọn không? (đo precision/độ bền tổng hợp);
2. **Contradiction test:** đưa câu hỏi về chủ đề có claim cạnh tranh — hệ thống có truy
   xuất cả hai phía và trình bày mâu thuẫn, hay chọn đại một phía? (§9.27);
3. **Temporal test:** hỏi về trạng thái quá khứ — hệ thống có dùng đúng đồng hồ, hay trả
   lời bằng hiện tại? (§9.25);
4. **Absence test:** hỏi về thứ không tồn tại — hệ thống kiêng trả lời hay bịa? (§9.43);
5. **Top_k test:** đặt bằng chứng quyết định ở vị trí vừa ngoài top_k — hệ thống có "ổn
   định" theo cách đáng ngờ không, hay đúng ra phải báo thiếu? (§9.29).

Một hệ thống vượt benchmark mà trượt các test này là hệ thống trông giỏi trong phòng
thí nghiệm, dễ vỡ ngoài đời.

**MUST NOT suy ra:**
- Không được suy vượt benchmark ⇒ bền vững (test đối kháng là phần bắt buộc).
- Không được khẳng định một test duy nhất phủ mọi ranh giới.

## 9.64 Ca làm việc toàn trình: 15 bước trên RATE_OF_CHANGE

Bây giờ ta chạy toàn bộ hệ thống qua câu hỏi trung tâm của chương:

> **Q0:** "Vì sao vận tốc và dòng điện được xem là cùng một cơ chế RATE_OF_CHANGE, và
> bằng chứng nào ủng hộ điều đó?"

**Bước 1 — Diễn giải (question interpretation, §9.3).** Intent: EXPLANATORY + COMPARATIVE
(yêu cầu cấu trúc chung + bằng chứng). Mentions: "vận tốc", "dòng điện", "RATE_OF_CHANGE".

**Bước 2 — Liên kết thực thể (§9.5).** "vận tốc" → `Velocity` (điểm 0.93, không mơ hồ);
"dòng điện" → `ElectricCurrent` (0.91, không mơ hồ trong ngữ cảnh điện tử);
"RATE_OF_CHANGE" → `rate:RATE_OF_CHANGE` (0.98). Ghi nhận: không mơ hồ đáng kể.

**Bước 3 — Phân rã (§9.7).** Q1/Q2 (structure từng bên), Q3 (vai trò so sánh),
Q4 (claim Accepted), Q5 (mâu thuẫn), Q6 (tổng hợp).

**Bước 4 — Lập kế hoạch (§9.8).** Router chọn: Graph-first hybrid — truy vấn cấu trúc
+ ledger + văn bản; bảng kế hoạch như §9.8.

**Bước 5 — Truy vấn cấu trúc (KGQA, §9.11).** SPARQL lấy 2 application + vai trò:
`VelocityDerivativeApplication instanceOf RATE_OF_CHANGE; operation DerivativeOperation;
differentiand Position; withRespectTo Time; produces Velocity` — và tương tự cho
`CurrentDerivativeApplication` (differentiand = ElectricCharge, produces = ElectricCurrent).
Kết quả: 2 đường cấu trúc khớp hoàn toàn về operation/withRespectTo.

**Bước 6 — Tra Sổ cái cho Q4 (§9.23).** Ledger query: claims Accepted về sự tương ứng
cơ chế giữa hai khái niệm → claim `C471` với Evidence `E88` (đoạn nguồn) và assessment.

**Bước 7 — Tra Sổ cái cho Q5 (§9.27).** Ledger query các claim Contested/Superseded cùng
chủ đề → `C210` ("đạo hàm chỉ là mô hình; vận tốc có bản chất định nghĩa riêng", trạng
thái Contested, phạm vi: triết học vật lý).

**Bước 8 — Truy xuất văn bản (§9.17–9.18).** BM25 + dense với query "vận tốc đạo hàm
theo thời gian dòng điện" → top-10 đoạn; RRF hợp hạng; chọn top-5 sau re-rank.

**Bước 9 — Đánh giá bằng chứng (§9.28).** Lọc: giữ 3 đoạn nguồn độc lập, 1 đoạn phản
đối, bỏ 2 đoạn trùng nguồn. Kiểm tra gold coverage: 5/5 nhóm gold có mặt — đủ.

**Bước 10 — Lắp ráp gói (§9.32–9.36).** Đóng **Evidence Packet**: câu hỏi, intent, thực
thể, 2 đường cấu trúc, C471 (asserted), C210 (contested, phạm vi), 3 đoạn nguồn (asserted
source), chuỗi provenance E88→fragment→sách, temporal scope "hiện hành", retrieval
metadata (top_k=5, độ sâu=2, retriever phiên bản 2.1). Sắp: đường cấu trúc đầu cửa sổ,
mâu thuẫn cuối cửa sổ (§9.34).

**Bước 11 — Sinh câu trả lời (§9.37–9.38).** LLM viết bản nháp 4 claim con A1–A4 (§9.38),
phân biệt rõ cái được hỗ trợ, cái suy luận, cái chưa biết.

**Bước 12 — Trích dẫn (§9.40).** A1→C471+E88; A2→bảng vai trò (derived từ cấu trúc);
A3→nhãn "suy luận từ C471+Cấu trúc" + ghi chú C210 phản đối; A4→kiêng trả lời.

**Bước 13 — Tự kiểm tra (§9.67).** Đối chiếu từng câu với gói: không có claim con nào
ngoài gói; A3 đúng là suy luận và được dán nhãn; mâu thuẫn được trình bày cả hai phía.

**Bước 14 — Hồ sơ câu trả lời (§9.58).** Answer artifact: generatedFor Q0, usedEvidence
= gói, answerStatus = SUPPORTED_WITH_CONTESTATION (do C210), citations đầy đủ.

**Bước 15 — Trả lời và ghi nhận.** Người dùng nhận câu trả lời: (1) cấu trúc chung;
(2) bằng chứng; (3) quan điểm phản đối và phạm vi; (4) điều chưa biết. QA answer KHÔNG
được chèn vào KG (§9.59); nếu câu trả lời phát hiện claim mới → CandidateClaim → Ch7.

**Bài học của ca làm việc:** mỗi bước đều có thể sai theo một cách riêng; câu trả lời
tốt không phải là câu trả lời "tự nhiên nhất" mà là câu trả lời *mà mọi bước đều có thể
kiểm tra lại*.

## 9.65 Ca thất bại: khi hệ thống sai

Ba ca thất bại kinh điển, mỗi ca minh họa một ranh giới của chương.

**Ca A — "Trung thành với nguồn sai" (ô B, §9.42).**

- Kịch bản: index cũ (§9.10). Sổ cái đã Superseded định nghĩa cũ lúc 09:00; index được
  tái lập lúc 10:00. Người dùng hỏi lúc 09:30 "current là gì?".
- Điều gì xảy ra: retriever (đúng quy trình) trả đoạn định nghĩa cũ; LLM (trung thực với
  gói) trả lời đúng theo đoạn cũ; trích dẫn đầy đủ. Mọi bước "đúng", câu trả lời sai.
- Chẩn đoán: lỗi nhất quán index — không phải lỗi LLM, không phải lỗi truy vấn.
- Bài học: hệ thống phải báo cáo index snapshot trong provenance (§9.58) và có cơ chế
  phát hiện staleness trước khi trả lời các câu hỏi nhạy thời gian.

**Ca B — "Người dùng không nói điều họ muốn" (diễn giải sai, §9.3).**

- Kịch bản: người dùng hỏi "Vận tốc và tốc độ khác nhau thế nào?" Intent FACTUAL đơn
  giản, nhưng thực tế họ đang tranh luận về một claim mâu thuẫn trong Sổ cái.
- Điều gì xảy ra: hệ thống trả lời so sánh định nghĩa chuẩn; người dùng thấy vô nghĩa.
- Chẩn đoán: diễn giải không nắm được nhu cầu thông tin; cũng có thể là lỗi intent mơ hồ
  không được hỏi lại.
- Bài học: diễn giải phải ghi nhận độ mơ hồ (§9.3) và hệ thống được phép hỏi lại thay vì
  đoán (§9.43).

**Ca C — "Chứng minh bằng đường đi" (lạm dụng đường đi, §9.54).**

- Kịch bản: hệ thống trả lời "vận tốc là tốc độ biến thiên vì đường đi
  Velocity→produces→VelocityDerivativeApplication→instanceOf→RATE_OF_CHANGE" mà không
  nói gì về C210 (claim phản đối Contested).
- Điều gì xảy ra: đường đi đúng về mặt đồ thị; câu trả lời trình bày như chứng minh.
- Chẩn đoán: truy xuất một phía (thiên kiến xác nhận §9.49), thiếu bước Q5; trình bày
  đường đi như suy dẫn (§9.54).
- Bài học: đường đi là dữ kiện cấu trúc; câu trả lời phải gồm cả phía phản đối, và ngôn
  ngữ "vì vậy" chỉ hợp lệ khi có claim+đánh giá hỗ trợ, không phải chỉ vì có cạnh.

## 9.66 Phân loại hallucination và tự kiểm tra (self-check)

**Hallucination** trong ngữ cảnh chương này được định nghĩa hẹp: *khẳng định về thế giới
không được hỗ trợ bởi Gói bằng chứng đã cấp* (không phải "sai" nói chung — một câu đúng
mà ngoài gói vẫn là hành vi không kiểm soát được, ô A §9.42). Bốn loại (BOOK-DEFINED):

1. **Quan hệ bịa (relation fabrication):** khẳng định quan hệ không có trong gói — ví dụ
   "vận tốc và dòng điện chia sẻ `differentiand`" (sai: differentiand khác nhau);
2. **Số liệu bịa (entity/number fabrication):** đưa số/đơn vị không có trong gói;
3. **Gán sai nguồn (misattribution):** trích dẫn một đoạn không thực sự hỗ trợ câu
   (lỗi citation precision [@gao-cite-2023]);
4. **Chắc chắn giả (false certainty):** viết điều chưa biết như điều đã biết — "không có
   cơ chế nào khác" khi chưa tìm hết (ô chưa biết §9.44).

**Tự kiểm tra (self-check)** là bước 13 của ca làm việc: trước khi phát hành, hệ thống
đối chiếu từng claim con với gói và dán nhãn kết quả: `SUPPORTED` / `PARTIALLY_SUPPORTED`
/ `UNSUPPORTED` / `CONTESTED`. Đây là **lớp kiểm tra tự động có giá trị**, nhưng phải
trung thực về giới hạn: *việc đối chiếu cũng do một mô hình thực hiện và cũng có thể
sai*. Nó làm giảm rủi ro, không loại bỏ nó.

**MUST NOT suy ra:**
- Không được suy tự kiểm tra đậu ⇒ câu trả lời đúng (vẫn có thể là ô B).
- Không được suy mọi câu không-có-căn-cứ là sai với thế giới.

## 9.67 Đối chiếu claim–bằng chứng (Claim–Evidence Alignment)

Kỹ thuật kiểm tra chi tiết hơn: với mỗi claim con, tìm *mục trong gói* hỗ trợ nó và
phân loại:

| Kết quả đối chiếu | Ý nghĩa | Hành động |
|---|---|---|
| SUPPORTED | mục trong gói hỗ trợ trực tiếp | giữ nguyên, trích dẫn |
| PARTIALLY_SUPPORTED | chỉ một phần claim được hỗ trợ | thu hẹp claim hoặc bổ sung bằng chứng |
| UNSUPPORTED | không có mục nào hỗ trợ | bỏ claim hoặc đánh dấu suy luận |
| CONTESTED | gói có claim đối lập có sức nặng | trình bày hai phía + trạng thái |

Đối chiếu là *kiểm tra quy trình*: nó không chứng minh claim đúng với thế giới, nhưng nó
bắt buộc hệ thống phải *nói rõ* mối quan hệ giữa lời của nó và bằng chứng của nó
[@rashkin-ais-2021] [@gao-cite-2023].

**MUST NOT suy ra:**
- Không được khẳng định đối chiếu đậu ⇒ câu trả lời đúng.
- Không được bỏ qua lớp đối chiếu vì "nó cũng chỉ là mô hình".

## 9.68 Suy luận đồ thị vs Suy luận LLM

So sánh hai "cỗ máy suy luận" trong hệ thống (BOOK-DEFINED, tổng hợp từ các chương):

| Khía cạnh | Suy luận đồ thị (symbolic) | Suy luận LLM |
|---|---|---|
| Tiền đề | triple trong KG, quy tắc ngữ nghĩa (Ch4–5) | văn bản trong cửa sổ ngữ cảnh |
| Bước suy ra | xác định theo ngữ nghĩa (entailment) | xác suất theo mô hình |
| Kiểm tra lại | ai cũng tái diễn được | không tái diễn được trọn vẹn |
| Lỗi đặc trưng | KG sai/thiếu, quy tắc sai | hallucination, lệch trọng tâm, lost-in-middle |
| Vết nguồn | tự nhiên (mỗi triple có provenance) | cần lớp trích dẫn riêng |
| Điểm mạnh | chính xác, có thể giải thích tiền đề | linh hoạt, diễn đạt tự nhiên |

Kết luận kiến trúc: **không thay thế, mà phân công.** Câu hỏi cấu trúc → suy luận đồ
thị (KGQA); câu hỏi mở/tổng hợp → LLM trên gói bằng chứng. Nơi ranh giới mờ — ví dụ
"cơ chế nào" giữa hai khái niệm — thì để đồ thị làm phần *quyết định cấu trúc* và LLM
làm phần *diễn đạt*, với đường cấu trúc là tiền đề được kiểm tra lại được.

**MUST NOT suy ra:**
- Không được khẳng định LLM "suy luận" giống hệt suy luận đồ thị.
- Không được khẳng định đồ thị thay được LLM cho câu hỏi mở.

## 9.69 GraphRAG không đảm bảo điều gì

Tổng kết các giới hạn đã xây dựng rải rác trong chương, thành một tuyên bố tập trung:

**GraphRAG (hay bất kỳ đường ống RAG nào) không đảm bảo:**

1. **Không đảm bảo đúng** — nguồn sai/lỗi thời ⇒ trả lời "đúng quy trình" mà sai (ô B);
2. **Không đảm bảo đầy đủ** — index tụt hậu, top_k, độ sâu: những thứ ngoài ranh giới
   truy xuất không được "biết";
3. **Không đảm bảo không hallucination** — lớp trích dẫn/tự kiểm tra làm giảm rủi ro,
   không loại bỏ;
4. **Không đảm bảo tri thức mới** — câu trả lời không tự thành tri thức được chấp nhận;
5. **Không đảm bảo ngữ nghĩa** — đồ thị *tổ chức* truy xuất, không *cung cấp* ngữ nghĩa
   đúng: entity linking sai, claim sai, cộng đồng nhiễu đều truyền thẳng vào câu trả lời;
6. **Không đảm bảo công bằng/mức độ chắc chắn** — điểm số không phải xác suất đúng.

Một hệ thống GraphRAG tốt là hệ thống *biết mình không đảm bảo*: báo cáo trạng thái,
kiêng trả lời khi thiếu, và làm mọi bước có thể kiểm tra lại.

## 9.70 Khi nào KHÔNG dùng RAG

Đối xứng với §8.37 của chương trước: có những câu hỏi không nên đi qua RAG/LLM tổng hợp.

**Không dùng RAG khi:**

1. **Truy vấn chính xác đủ dùng** — thực thể + thuộc tính + schema biết trước: SPARQL
   trả lời chính xác, rẻ, kiểm tra được (KGQA);
2. **Cần sự kiện có thẩm quyền chính xác** — số liệu, quy định, định nghĩa đã quản trị:
   trả thẳng từ Canonical View, không qua sinh văn bản;
3. **Rủi ro hallucination không chấp nhận được** — kiểm toán, pháp lý: câu trả lời sinh
   phải kèm kiêng trả lời mạnh, hoặc không dùng LLM tổng hợp;
4. **Câu hỏi ngoài tri thức hệ thống** — miền không có nguồn: trả lời "ngoài phạm vi"
   tốt hơn RAG "tìm gì đó đại loại";
5. **Chi phí/độ trễ vượt lợi ích** — FAQ được đánh index sẵn thì khỏi cần LLM mỗi lần;
6. **Tính tái lập tuyệt đối bắt buộc** — LLM không tái diễn được chính xác cùng đầu ra:
   dùng đường tượng trưng.

**Chẩn đoán ngược:** nếu một câu hỏi *lẽ ra* có đường tượng trưng mà hệ thống vẫn đi RAG,
đó là lỗi router (§9.71), không phải "RAG mạnh hơn".

## 9.71 Router thực thi truy vấn tổng hợp (Query Execution Router — BOOK-DEFINED)

Gom toàn bộ chương vào một quyết định duy nhất. **Router** (giới thiệu §9.8) là thành
phần trung tâm của hệ thống hỏi đáp — BOOK ENGINEERING MODEL — có đầu vào là câu hỏi đã
diễn giải và đầu ra là đường thực thi + Gói bằng chứng:

```
                  ┌─────────── intent/entities/decomposition ───────────┐
                  ▼                                                      │
        ┌─ thực thể rõ + schema biết + intent cấu trúc ──► KGQA (SPARQL/đồ thị) ──┐
        │                                                                          │
        ├─ cần suy diễn hệ quả ──────────────────────────► Suy luận tượng trưng ───┤
        │                                                                          │
Router ─┼─ thực thể mơ hồ / hỏi mở / định nghĩa ─────────► Text RAG (BM25+dense) ──┤
        │                                                                          │
        ├─ cấu trúc + bằng chứng văn bản ────────────────► GraphRAG / hybrid ─────┤
        │                                                                          │
        └─ lịch sử / mâu thuẫn / provenance ─────────────► Ledger retrieval ──────┘
                                  │
                                  ▼
                        Evidence Packet (BOOK-DEFINED)
                                  ▼
                        Answer Generation + trích dẫn + tự kiểm tra
                                  ▼
                        Answer artifact (provenance đầy đủ)
```

Hình 9.7 vẽ router này. Nguyên tắc vận hành: **đường chính xác nhất đủ trả lời thắng**;
sự mơ hồ đi xuống tầng linh hoạt hơn; mọi đường đều kết thúc ở Gói bằng chứng để tầng
sinh và tầng kiểm tra làm việc trên một giao diện duy nhất.

![Router thực thi truy vấn (BOOK-DEFINED): từ intent chọn đường KGQA/suy luận/text RAG/GraphRAG/ledger, mọi đường đều đóng thành Evidence Packet rồi mới sinh câu trả lời có trích dẫn và hồ sơ nguồn gốc.](figures/generated/ch09-query-router.pdf)

**MUST NOT suy ra:**
- Không được khẳng định lựa chọn của router là chân lý.
- Không được khẳng định tổng hợp sinh văn bản thắng truy vấn chính xác khi truy vấn đủ.

## 9.72 Những quan niệm sai phổ biến (Common Misconceptions)

Ba mươi bốn quan niệm sai mà chương này trực tiếp bác bỏ — mỗi mục trỏ về mục đã giải
thích:

1. "Truy xuất được rồi thì trả lời được" — retrieved ≠ evidence (§9.28, §9.37).
2. "Điểm truy xuất cao nghĩa là chắc đúng" — score semantics (§9.60).
3. "BM25 hiểu ngữ nghĩa" — chỉ là khớp từ (§9.17).
4. "Embedding giống nhau nghĩa là cùng ý nghĩa" — vector ≠ meaning (§9.18).
5. "Dense retrieval luôn thắng lexical" — hai họ mạnh theo kiểu khác nhau (§9.19).
6. "Càng nhiều tín hiệu càng đúng" — hybrid giảm miss, không tăng truth (§9.20).
7. "top_k chỉ là chi tiết triển khai" — nó là ranh giới tri thức luận (§9.29).
8. "Không nằm trong top_k nghĩa là không tồn tại" — OWA (§9.29, §9.44).
9. "Index chính là tri thức" — index ≠ KG (§9.10).
10. "Trả lời theo Sổ cái cũng giống trả lời theo chiếu hình" — hai miền tri thức luận
    khác nhau (§9.23).
11. "Hỏi lịch sử thì dùng trạng thái hiện tại" — nhiều đồng hồ (§9.25).
12. "Có đường đi là đã chứng minh" — path ≠ proof (§9.12, §9.54).
13. "Đường duyệt càng sâu càng tốt" — giới hạn độ sâu cũng là ranh giới (§9.13).
14. "Trong phạm vi k-chặng là liên quan" — k-hop ≠ relevance (§9.15).
15. "Tóm tắt thay được nguồn" — summary ≠ source (§9.33, §9.56).
16. "Nén ngữ cảnh không mất gì" — nén có thể vứt bằng chứng quyết định (§9.33).
17. "Thứ tự ngữ cảnh không quan trọng" — lost in the middle (§9.34).

18. "Đầy gói bằng chứng nghĩa là đủ bằng chứng" — packet ≠ sufficiency (§9.36).
19. "Có căn cứ nghĩa là đúng" — grounded ≠ true (ô B) (§9.39, §9.42).
20. "Câu trả lời trôi chảy là câu trả lời đúng" — fluency ≠ correctness (§9.37).
21. "Có trích dẫn nghĩa là được hỗ trợ" — citation precision (§9.40).
22. "Trích dẫn nhiều nghĩa là trích dẫn tốt" — citation recall/completeness (§9.40).
23. "Trung thành nghĩa là đúng" — faithfulness ≠ correctness (§9.41).
24. "Không tìm thấy → không tồn tại" — unknown vs not found (§9.44).
25. "Lỗi trả lời → lỗi tri thức" — retrieval failure ≠ knowledge absence (§9.44).
26. "Kiêng trả lời là lỗi" — abstention can be correct behavior (§9.43).
27. "Một hệ thống GraphRAG là một thuật toán chuẩn" — family, not standard (§9.52).
28. "KGQA = GraphRAG" — different mechanisms (§9.53).
29. "GraphRAG thay được KGQA cho câu hỏi chính xác" — decision table (§9.53).
30. "GraphRAG loại bỏ hallucination" — không đảm bảo (§9.69).
31. "Câu trả lời QA tự thành tri thức mới" — không qua quản trị (§9.59).
32. "LLM thay được suy luận đồ thị" — hai cỗ máy khác nhau (§9.68).
33. "Đường hình thành cầu được chứng minh" — path explosion hides alternatives (§9.55).
34. "Tất cả câu hỏi đều cần RAG" — khi nào KHÔNG dùng RAG (§9.70).

## 9.73 Điểm tự kiểm tra (Self-explanation Checkpoints)

Tám câu hỏi để người đọc tự kiểm tra rằng mình đã nắm được các ranh giới của chương.
Không có đáp án duy nhất — có câu trả lời có lập luận.

1. Câu hỏi "Định nghĩa current 2020?" cần truy xuất miền nào: chiếu hình hay Sổ cái?
   Vì sao?
2. Giả sử BM25 xếp đoạn A hạng 1 với điểm 12.3, đoạn B hạng 2 với điểm 12.1. Có thể kết
   luận "hệ thống chắc A đúng hơn B 0.2 đơn vị" không? Vì sao không?
3. top_k=5, và bằng chứng quyết định cho câu hỏi của bạn nằm ở hạng 6. Câu trả lời sẽ
   ra sao, và hệ thống "sai" ở tầng nào (theo 7 tầng §9.61)?
4. Một tóm tắt cộng đồng trong GraphRAG nói "cả ba hiện tượng là một cơ chế". Nó có phải
   là bằng chứng không? Nó missing gì để thành bằng chứng?
5. Phân biệt asserted/derived/predicted cho phát biểu "vận tốc là tốc độ biến thiên":
   phát biểu đó thuộc nhóm nào nếu (a) từ môt quy tắc? (b) từ Sổ cái? (c) từ mô hình học?
6. Ô B của bảng 2×2 (trung thành với nguồn sai) — vì sao "quy trình chạy đúng" không
   biến ô B thành ô C?
7. Agentic retrieval thêm lượt truy xuất thứ 4 và thứ 5, mỗi lượt "thành công". Vì sao
   câu trả lời có thể vẫn kém — kể ba cơ chế thất bại (§9.46–9.50)?
8. Nếu Q0 trả lời "không có cơ chế nào khác ngoài RATE_OF_CHANGE điều khiển vận tốc" —
   câu này nên được dán nhãn tri thức luận nào (§9.60)? Vì sao?

## 9.74 Hồ sơ Thí nghiệm Bị hoãn (Experiment Backlog)

Chín thí nghiệm đề xuất nhưng **HOÃN ĐẾN BOOK V0.1** — nằm ngoài phạm vi lý thuyết của
chương, cần dữ liệu thật, hệ thống thật, và dữ liệu đánh giá:

- **EXP-9-1:** (HOÃN) Xây benchmark RATE_OF_CHANGE gồm ≥40 câu hỏi (mỗi intent ≥4), gold
  evidence + gold answer cho từng câu; đo 7 tầng (§9.61).
- **EXP-9-2:** (HOÃN) So sánh BM25 vs dense vs hybrid trên chính kho văn bản của hệ —
  P@K/R@K/MRR/nDCG với gold của EXP-9-1.
- **EXP-9-3:** (HOÃN) Đo tác động top_k: cố định 1 câu hỏi, di chuyển bằng chứng quyết
  định đến hạng 1..10, quan sát chất lượng trả lời (kiểm chứng §9.29).
- **EXP-9-4:** (HOÃN) Kiểm chứng lost-in-the-middle trên mô hình hiện dùng: cùng gói,
  đổi thứ tự, đo độ ổn định (§9.34).
- **EXP-9-5:** (HOÃN) Xây test suite đối kháng (§9.63): distractor, mâu thuẫn, thời gian,
  absence, top_k; chạy định kỳ trên pipeline thật.
- **EXP-9-6:** (HOÃN) Đo hiệu quả agentic vs static trên câu hỏi đa bước: chất lượng,
  số lượt, cost; kiểm tra điều kiện dừng (§9.46–9.47).
- **EXP-9-7:** (HOÃN) Cài đặt một GraphRAG implementation (ví dụ Microsoft GraphRAG) trên
  kho tài liệu của hệ; đo Local/Global trên benchmark EXP-9-1; ghi nhận community
  instability (§9.56).
- **EXP-9-8:** (HOÃN) Đo staleness: sau khi Superseded một claim, theo dõi xác suất hệ
  vẫn trả lời theo claim cũ ở các cấu hình cache/index khác nhau (§9.10, §9.57).
- **EXP-9-9:** (HOÃN) Kiểm tra router (§9.71): so sánh tỉ lệ "câu hỏi chính xác đi nhầm
  đường RAG" khi dùng rule-based vs LLM planner, kèm ghi nhận chi phí.

## 9.75 Kiểm toán độ sâu (Chapter Depth Audit)

Các khái niệm chính của chương và mức độ sâu tối thiểu cam kết (rubric 1–6, từ "được đề
cập" đến "phân tích và tổng hợp trong nhiều ngữ cảnh"):

| Khái niệm chính | Mục | Độ sâu | Khái niệm chính | Mục | Độ sâu |
|---|---|---|---|---|---|
| Question Interpretation | §9.3 | 4 | Symbolic Graph Retrieval | §9.11 | 5 |
| Query Intent (9 loại) | §9.4 | 4 | Multi-hop Retrieval | §9.12 | 4 |
| Query Entity Linking | §9.5 | 4 | Path Bounds | §9.13 | 4 |
| Intent ≠ Identity | §9.6 | 4 | Relation-aware Traversal | §9.14 | 4 |
| Query Decomposition | §9.7 | 4 | k-hop Neighborhood | §9.15 | 4 |
| Retrieval Plan | §9.8 | 4 | Subgraph Retrieval | §9.16 | 4 |
| Retrieval Unit | §9.9 | 4 | BM25 | §9.17 | 5 |
| Index ≠ KG | §9.10 | 4 | Dense Retrieval (DPR) | §9.18 | 4 |
| Query Embedding ≠ Meaning | §9.18–9.19 | 4 | Hybrid Retrieval | §9.20 | 4 |
| Rank Fusion (RRF) | §9.21 | 5 | Graph-first vs Text-first | §9.22 | 4 |
| Canonical View vs Claim Ledger | §9.23 | 5 | Governance-aware Retrieval | §9.24 | 4 |
| Temporal Retrieval (clocks) | §9.25 | 4 | Provenance-aware Retrieval | §9.26 | 4 |
| Contradiction-aware Retrieval | §9.27 | 4 | Evidence Diversity | §9.28 | 4 |
| top_k as Epistemic Bound | §9.29 | 5 | Precision/Recall | §9.30 | 4 |
| P@K / R@K | §9.30 | 4 | MRR / nDCG | §9.30 | 4 |
| Reranking | §9.31 | 4 | Context Assembly | §9.32 | 4 |
| Context Compression | §9.33 | 4 | Lost in the Middle | §9.34 | 4 |
| Graph Serialization | §9.35 | 4 | Evidence Packet | §9.36 | 5 |
| Answer Generation | §9.37 | 4 | Answer Claims | §9.38 | 4 |
| Grounded Answer | §9.39 | 5 | Citation (completeness) | §9.40 | 4 |
| Faithfulness | §9.41 | 4 | Correctness × Groundedness 2×2 | §9.42 | 5 |
| Abstention | §9.43 | 4 | Unknown vs Not Found | §9.44 | 5 |
| Query Planning | §9.45 | 4 | Static vs Agentic | §9.46 | 4 |
| Stopping Conditions | §9.47 | 4 | Query Drift | §9.48 | 4 |
| Confirmation Bias | §9.49 | 4 | Hypothesis-testing Retrieval | §9.50 | 4 |
| Local vs Global | §9.51 | 4 | GraphRAG (family) | §9.52 | 5 |
| RAG vs KGQA vs GraphRAG | §9.53 | 5 | Path as Explanation | §9.54 | 4 |
| Path Explosion | §9.55 | 4 | Community Retrieval | §9.56 | 4 |
| Caching / Index Consistency | §9.57 | 4 | Retrieval & Answer Provenance | §9.58 | 4 |
| QA Answer ≠ Ingestion | §9.59 | 5 | Score Semantics / 3 statuses | §9.60 | 5 |
| 7-layer Retrieval Evaluation | §9.61 | 5 | Gold Evidence / Benchmark | §9.62 | 4 |
| Adversarial Tests | §9.63 | 4 | End-to-end 15-step Case | §9.64 | 6 |
| Failure Walkthroughs | §9.65 | 5 | Hallucination Taxonomy | §9.66 | 4 |
| Claim–Evidence Alignment | §9.67 | 4 | Graph vs LLM Reasoning | §9.68 | 4 |
| GraphRAG Limits | §9.69 | 4 | When NOT to use RAG | §9.70 | 4 |
| Query Execution Router | §9.71 | 5 | | | |

## 9.76 Bài kiểm tra năng lực người đọc (Reader Capability Test Q01–Q50)

Yêu cầu: **Q01–Q50 đều = YES**. Nếu có câu trả lời NO, hãy đọc lại mục được trỏ trước
khi tiếp tục.

| # | Tôi có thể... | Mục |
|---|---|---|
| Q01 | ...phân biệt information need, query, document | §9.3 |
| Q02 | ...liệt kê 9 loại intent và nguồn truy xuất ưu tiên của từng loại | §9.4 |
| Q03 | ...thực hiện sinh/chấm điểm/quyết định cho một mention mơ hồ | §9.5 |
| Q04 | ...giải thích vì sao intent và định danh là hai trục mơ hồ độc lập | §9.6 |
| Q05 | ...phân rã một câu hỏi phức và vẽ đồ thị phụ thuộc của các câu con | §9.7 |
| Q06 | ...viết một kế hoạch truy xuất có thứ tự, giới hạn, điều kiện dừng | §9.8 |
| Q07 | ...chọn đơn vị truy xuất theo loại câu hỏi | §9.9 |
| Q08 | ...giải thích index ≠ KG và hậu quả của index tụt hậu | §9.10 |
| Q09 | ...viết SPARQL đơn giản và nói đúng giới hạn của nó | §9.11 |
| Q10 | ...kể vì sao một đường đi đa chặng không phải chứng minh | §9.12 |
| Q11 | ...thiết kế giới hạn độ sâu và giải thích vì sao nó là ranh giới tri thức luận | §9.13 |
| Q12 | ...chọn loại cạnh duyệt theo intent | §9.14 |
| Q13 | ...giải thích vì sao k-chặng ≠ liên quan | §9.15 |
| Q14 | ...lý giải khái niệm đồ thị con đủ tối thiểu theo chính sách (không tối ưu toán học) | §9.16 |
| Q15 | ...viết công thức BM25 và giải thích idf, k1, b | §9.17 |
| Q16 | ...giải thích dual encoder và ý nghĩa của dot product | §9.18 |
| Q17 | ...giải thích vector câu hỏi ≠ ý nghĩa câu hỏi | §9.18 |
| Q18 | ...bàn luận khi nào lexical mạnh hơn dense và ngược lại | §9.19 |
| Q19 | ...giải thích hybrid giảm miss chứ không tăng truth | §9.20 |
| Q20 | ...tính RRF của một tài liệu từ 2 hệ | §9.21 |
| Q21 | ...chọn graph-first hay text-first theo intent | §9.22 |
| Q22 | ...giải thích chiếu hình vs Sổ cái và chọn đúng miền theo intent | §9.23 |
| Q23 | ...thiết kế chính sách lọc theo trạng thái quản trị | §9.24 |
| Q24 | ...phân biệt ba đồng hồ thời gian và chọn đồng hồ đúng | §9.25 |
| Q25 | ...vẽ chuỗi provenance Claim→Evidence→Source và giải thích nó không chứng minh đúng | §9.26 |
| Q26 | ...truy xuất các claim cạnh tranh kèm phạm vi khi hỏi về chủ đề tranh cãi | §9.27 |
| Q27 | ...giải thích vì sao nhiều đoạn trùng nguồn không phải nhiều bằng chứng | §9.28 |
| Q28 | ...giải thích top_k là ranh giới tri thức luận và hệ quả của nó | §9.29 |
| Q29 | ...tính P@K, R@K, MRR, nDCG cho một ví dụ cụ thể | §9.30 |
| Q30 | ...giải thích vì sao các độ đo truy xuất không đo độ đúng | §9.30 |
| Q31 | ...giải thích re-ranking không cứu được recall | §9.31 |
| Q32 | ...thiết kế lắp ráp ngữ cảnh (chọn, nhóm, sắp, dán nhãn) | §9.32 |
| Q33 | ...giải thích tóm tắt là đồ tạo tác dẫn xuất, không phải nguồn | §9.33 |
| Q34 | ...giải thích lost-in-the-middle và áp dụng khi sắp xếp gói | §9.34 |
| Q35 | ...đánh đổi giữa các dạng tuần tự hóa đồ thị | §9.35 |
| Q36 | ...liệt kê các trường của Evidence Packet và vì sao nó là giao diện | §9.36 |
| Q37 | ...giải thích 4 kỷ luật của tầng sinh câu trả lời | §9.37 |
| Q38 | ...phân rã câu trả lời thành claim con và dán nhãn từng claim | §9.38 |
| Q39 | ...giải thích grounded ≠ đúng | §9.39 |
| Q40 | ...giải thích citation recall vs precision | §9.40 |
| Q41 | ...giải thích faithfulness ≠ correctness | §9.41 |
| Q42 | ...xếp một câu trả lời vào 1 trong 4 ô của bảng 2×2 | §9.42 |
| Q43 | ...liệt kê 6 điều kiện kiêng trả lời và nói rõ loại thiếu hụt | §9.43 |
| Q44 | ...phân biệt 5 trạng thái "không tìm thấy" và lỗi truy xuất vs thiếu tri thức | §9.44 |
| Q45 | ...thiết kế truy xuất agentic có điều kiện dừng và phát hiện query drift | §9.46–9.48 |
| Q46 | ...giải thích thiên kiến xác nhận và truy xuất kiểm định giả thuyết | §9.49–9.50 |
| Q47 | ...phân biệt câu hỏi local vs global và chọn chiến lược | §9.51 |
| Q48 | ...giải thích GraphRAG là họ kiến trúc, không phải chuẩn | §9.52 |
| Q49 | ...dùng bảng quyết định KGQA/RAG/GraphRAG cho một câu hỏi cụ thể | §9.53 |
| Q50 | ...giải thích đường đi là giải thích, bùng nổ đường đi, và các giới hạn của GraphRAG | §9.54–9.55, §9.69 |

## 9.77 Bậc năng lực cuối chương

Kết thúc chương này, người đọc (và hệ thống) đạt được các nấc năng lực sau:

1. **Nhận biết** — biết các khái niệm: intent, entity linking, decomposition, BM25, DPR,
   RRF, nDCG, Evidence Packet, faithfulness, abstention, agentic, GraphRAG, KGQA, router.
2. **Phân biệt** — không nhầm retrieved ≠ evidence, index ≠ KG, có căn cứ ≠ đúng, trung
   thành ≠ đúng, đường đi ≠ chứng minh, không tìm thấy ≠ không tồn tại.
3. **Phân tích** — từ một câu hỏi, phân rã thành 9 loại intent, chọn chiến lược truy xuất,
   thiết kế Evidence Packet, chỉ ra các rủi ro (độ sâu, top_k, query drift, confirmation
   bias, lost-in-the-middle).
4. **Tổng hợp** — chạy được ca làm việc 15 bước, thiết kế router, lập bảng quyết định
   KGQA/RAG/GraphRAG, xây bộ test đối kháng, đánh giá 7 tầng.
5. **Phê bình** — phát hiện bằng chứng đơn điệu, thiên kiến xác nhận, trôi câu hỏi, mất
   provenance, và phân biệt ô B vs ô C của bảng 2×2.

## 9.78 Tóm tắt chương

Chương 9 đã mở **nấc truy xuất và hỏi đáp** — IO mới của hệ thống tri thức gồm ba tầng:
hiểu câu hỏi, truy xuất (cấu trúc + văn bản + tri thức luận), và sinh câu trả lời. Các
nguyên lý xuyên suốt:

- **Chín loại intent** — mỗi loại quyết định nguồn truy xuất và loại bằng chứng.
- **Index ≠ KG** — index tụt hậu, truy xuất sai, câu trả lời sai dù quy trình "đúng".
- **top_k là ranh giới tri thức luận** — mô hình chỉ suy luận trên bằng chứng nó thấy.
- **Evidence Packet (BOOK-DEFINED)** — giao diện duy nhất giữa truy xuất và tầng sinh.
- **Bảng 2×2 (đúng × căn cứ)** — grounded ≠ true; faithfulness ≠ correctness.
- **GraphRAG là họ kiến trúc** — không phải một thuật toán chuẩn; KGQA, RAG, GraphRAG bổ
  sung nhau, không thay thế nhau.
- **Câu trả lời QA ≠ tri thức thu nhận** — không vòng tắt bỏ qua quản trị.
- **Ba trạng thái** — asserted, derived, predicted — không trộn lẫn.
- **15 bước toàn trình** — mỗi bước đều có thể sai; câu trả lời kiểm tra được là đích.

## 9.79 Cầu nối Chương 10

Chương 9 kết thúc phần hỏi đáp trên tri thức hiện có. Chương 10 — **Quản trị hệ thống và
Vận hành** — sẽ mở rộng sang các câu hỏi vận hành: làm sao hệ thống tự giám sát sự phát
triển của chính nó? Làm sao phát hiện lỗi thời, vòng phản hồi, mâu thuẫn tích lũy? Làm
sao đo lường chất lượng tri thức theo thời gian? Quản trị vòng đời không chỉ cho từng
claim (Ch6) mà cho toàn bộ hệ. Chương 10 bắt đầu từ đó — và để lại các câu hỏi mở cho
người đọc muốn xây hệ thống thật, trong đó quan trọng nhất là: **một hệ thống tri thức
không bao giờ "xong" — nó phải được đo, được bảo dưỡng, và được tin tưởng một cách có
kiểm soát.**

## Thuật ngữ đã gặp trong chương này

| Thuật ngữ | Bản dịch / Giải thích | Mục |
|---|---|---|
| Question interpretation | Diễn giải câu hỏi | §9.3 |
| Query intent | Ý định truy vấn (9 loại) | §9.4 |
| Entity linking | Liên kết thực thể truy vấn | §9.5 |
| Query decomposition | Phân rã câu hỏi | §9.7 |
| Retrieval plan | Kế hoạch truy xuất | §9.8 |
| Retrieval unit | Đơn vị truy xuất | §9.9 |
| Search index | Chỉ mục truy xuất | §9.10 |
| Symbolic retrieval | Truy xuất tượng trưng (SPARQL) | §9.11 |
| Multi-hop retrieval | Truy xuất đa chặng | §9.12 |
| Path bound / depth limit | Giới hạn độ sâu | §9.13 |
| k-hop neighborhood | Vùng lân cận k-chặng | §9.15 |
| Subgraph retrieval | Truy xuất đồ thị con | §9.16 |
| BM25 | Hàm xếp hạng từ vựng | §9.17 |
| Dense retrieval / Dual encoder | Truy xuất mật độ / bộ mã hóa kép | §9.18 |
| Hybrid retrieval | Truy xuất lai | §9.20 |
| Reciprocal Rank Fusion (RRF) | Hợp hạng theo hạng nghịch đảo | §9.21 |
| Graph-first / Text-first | Đồ thị trước / Văn bản trước | §9.22 |
| Canonical View | Chiếu hình (trạng thái hiện được chấp nhận) | §9.23 |
| Claim Ledger | Sổ cái claim (lịch sử, đầy đủ) | §9.23 |
| Governance-aware retrieval | Truy xuất theo quản trị | §9.24 |
| Temporal retrieval | Truy xuất thời gian (nhiều đồng hồ) | §9.25 |
| Provenance-aware retrieval | Truy xuất nguồn gốc | §9.26 |
| Contradiction-aware retrieval | Truy xuất nhạy mâu thuẫn | §9.27 |
| Evidence diversity | Đa dạng bằng chứng | §9.28 |
| Epistemic bound | Ranh giới tri thức luận | §9.29 |
| P@K, R@K, MRR, nDCG | Các độ đo truy xuất | §9.30 |
| Reranking | Tái xếp hạng | §9.31 |
| Context assembly | Lắp ráp ngữ cảnh | §9.32 |
| Context compression | Nén ngữ cảnh | §9.33 |
| Lost in the middle | Hiệu ứng mất thông tin giữa cửa sổ | §9.34 |
| Graph serialization | Tuần tự hóa đồ thị | §9.35 |
| **Evidence Packet** | **Gói bằng chứng (BOOK-DEFINED)** | §9.36 |
| Answer generation | Sinh câu trả lời | §9.37 |
| Answer claim | Claim con trong câu trả lời | §9.38 |
| Grounded answer | Câu trả lời có căn cứ | §9.39 |
| Citation | Trích dẫn | §9.40 |
| Citation completeness | Độ đầy đủ trích dẫn | §9.40 |
| Faithfulness | Trung thành (với ngữ cảnh) | §9.41 |
| Correctness | Đúng (với thế giới) | §9.42 |
| Abstention | Kiêng trả lời | §9.43 |
| Query planning | Lập kế hoạch truy vấn | §9.45 |
| Agentic retrieval | Truy xuất lặp/có tác nhân | §9.46 |
| Stopping condition | Điều kiện dừng | §9.47 |
| Query drift | Trôi câu hỏi | §9.48 |
| Confirmation bias | Thiên kiến xác nhận | §9.49 |
| Hypothesis-testing retrieval | Truy xuất kiểm định giả thuyết | §9.50 |
| Local vs Global question | Câu hỏi cục bộ vs toàn cục | §9.51 |
| GraphRAG | Họ kiến trúc RAG trên đồ thị | §9.52 |
| KGQA | Hỏi đáp đồ thị tri thức | §9.53 |
| Path explanation | Giải thích theo đường đi | §9.54 |
| Path explosion | Bùng nổ đường đi | §9.55 |
| Community retrieval | Truy xuất cộng đồng | §9.56 |
| Answer provenance | Hồ sơ câu trả lời (BOOK-DEFINED) | §9.58 |
| Score semantics | Ngữ nghĩa điểm số | §9.60 |
| Asserted / Derived / Predicted | Ba trạng thái tri thức luận | §9.60 |
| Gold evidence | Bằng chứng vàng | §9.62 |
| **Query Execution Router** | **Bộ điều hướng truy vấn (BOOK-DEFINED)** | §9.71 |

## Tài liệu tham khảo

- Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (Lewis et al., NeurIPS
  2020) [@lewis-rag-2020]
- Dense Passage Retrieval for Open-Domain Question Answering (Karpukhin et al., EMNLP
  2020) [@karpukhin-dpr-2020]
- From Local to Global: A Graph RAG Approach (Edge et al., 2024) [@edge-graphrag-2024]
- Microsoft GraphRAG Documentation [@microsoft-graphrag-docs]
- The Probabilistic Relevance Framework: BM25 and Beyond (Robertson & Zaragoza, 2009)
  [@robertson-bm25-2009]
- Introduction to Information Retrieval (Manning, Raghavan & Schutze, 2008)
  [@manning-ir-2008]
- Cumulated gain-based evaluation of IR techniques (Jarvelin & Kekalainen, 2002)
  [@jarvelin-ndcg-2002]
- Reciprocal rank fusion (Cormack, Clarke & Buettcher, 2009) [@cormack-rrf-2009]
- Passage Re-ranking with BERT (Nogueira & Cho, 2019) [@nogueira-rerank-2019]
- Lost in the Middle (Liu et al., 2024) [@liu-lostmid-2023]
- Measuring Attribution in Natural Language Generation Models (Rashkin et al., 2021)
  [@rashkin-ais-2021]
- Enabling Large Language Models to Generate Text with Citations (Gao et al., 2023)
  [@gao-cite-2023]
- Introduction to Neural Network based Approaches for KGQA (Chakraborty et al., 2019)
  [@chakraborty-kgqa-2019]
- Unifying Large Language Models and Knowledge Graphs (Zhu et al., 2023)
  [@zhu-llmkg-2023]
