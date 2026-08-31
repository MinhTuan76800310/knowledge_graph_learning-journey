# Chương 10 — Xây dựng Hệ thống Tri thức Sống

> **Định hướng chương**
>
> **Câu hỏi trung tâm:** Một hệ thống tri thức có thể biểu diễn, suy luận, quản trị, thu
> nhận, học quy nạp, truy xuất và trả lời câu hỏi — nhưng làm sao nó tự **giám sát sự
> tăng trưởng** của chính nó? Làm sao nó phát hiện tri thức đã cũ, mâu thuẫn tích lũy,
> chất lượng suy giảm? Làm sao nó tự **bảo trì** — tái xác minh, đánh giá lại, thay thế,
> nghỉ hưu — và vẫn đáng tin cậy dù biết mình không bao giờ "xong"?
>
> **Vì sao quan trọng:** Chín chương trước đã xây dựng một hệ tri thức có thể biểu diễn
> đồ thị (Ch1–2), định danh và ngữ nghĩa (Ch3–4), suy diễn và kiểm định (Ch5), quản trị
> claim (Ch6), thu nhận nguồn (Ch7), học quy nạp (Ch8), và truy xuất hỏi đáp (Ch9). C471
> (Accepted) và C210 (Contested) đứng trong mâu thuẫn được quản trị. Index có thể tụt hậu
> so với Sổ cái. Hệ thống có thể kiêng trả lời khi thiếu bằng chứng. Nhưng không nấc nào
> trong số đó **nhìn toàn hệ thống**: không ai đo chất lượng tri thức tăng hay giảm theo
> thời gian; không ai phát hiện một claim Accepted trở nên cũ khi nguồn của nó bị thay
> thế; không ai đóng vòng lặp từ thất bại QA → tái thu nhận → tái đánh giá. Chương 10
> mở nấc cuối: **vận hành toàn bộ hệ thống như một thực thể sống, được đo, được bảo trì,
> và được kiểm soát**.
>
> **Bạn sẽ hiểu:**
>
> - Từ tạo tác tĩnh đến hệ thống sống; sáu luồng thay đổi
> - Phát hiện **cũ (staleness)** và **độ tươi (freshness)**; tươi ≠ đúng
> - Đồng hồ valid/system/assessment ở quy mô hệ thống
> - Tự quan sát (self-observation): log cái gì, đo cái gì
> - **Vòng giám sát (monitoring loop)** — cơ chế trung tâm: thu thập → tổng hợp → so
>   ngưỡng → cảnh báo → đánh giá → hành động → đo lại
> - Ngưỡng là chính sách, không phải chân lý; ngưỡng ≠ chân lý
> - Cảnh báo phải kiểm chứng được; đánh giá là giai đoạn tri thức luận
> - Giám sát ≠ quản trị
> - Vòng phản hồi: QA → ứng viên, user sửa, an toàn vòng lặp
> - Phản hồi ≠ bằng chứng; sụp đổ phản hồi ≠ sụp đổ mô hình
> - Tích lũy mâu thuẫn và nợ tri thức; chính sách leo thang
> - Năm chiều chất lượng tri thức: đúng, đủ, tươi, nhất quán, đáng tin
> - Mức vs xu hướng; chất lượng ≠ chân lý; suy thoái, mục nát benchmark
> - Sụp đổ phản hồi (feedback collapse) và sụp đổ mô hình (model collapse)
> - Các thao tác bảo trì có quản trị: tái xác minh, tái đánh giá, nghỉ hưu, thay thế
> - Quản trị hàng loạt; vết kiểm toán toàn hệ thống
> - Tin cậy có kiểm soát (controlled trust): tin cậy nhờ kiểm chứng, không phải đức tin
> - Kiến trúc sống (living architecture) và dốc tự động hóa
> - Hệ thống không bao giờ "xong"; vấn đề mở → Afterword
>
> **Tiên quyết:**
> - Chương 1–2 (đồ thị, node, cạnh)
> - Chương 3 (định danh)
> - Chương 4 (ngữ nghĩa, OWA, closed-world)
> - Chương 5 (suy diễn, quy tắc, SHACL)
> - Chương 6 (epistemic model, Claim, Claim Ledger, Evidence, Assessment, governance
>   state, mutiple clocks, C471 Accepted vs C210 Contested)
> - Chương 7 (thu nhận nguồn, tích hợp, pipeline, candidate → accepted)
> - Chương 8 (học quy nạp, CandidateMechanismHypothesis)
> - Chương 9 (truy xuất, hỏi đáp, Evidence Packet, Answer artifact, index ≠ KG, câu trả
>   lời QA ≠ tri thức thu nhận)
>
> **Bản đồ khái niệm:**
>
> Hệ thống sống → Sáu luồng thay đổi → Cũ (staleness) → Tươi (freshness) → Tươi ≠ đúng
> → Đồng hồ toàn hệ thống → Tự quan sát → Đo lường → **Vòng giám sát** (thu thập → tổng
> hợp → ngưỡng → cảnh báo → đánh giá → hành động → đo lại) → Cửa sổ tổng hợp → Ngưỡng
> là chính sách → Ngưỡng ≠ chân lý → Cảnh báo → Đánh giá → Giám sát ≠ quản trị → Vòng
> phản hồi → QA → ứng viên → User sửa → Phản hồi ≠ bằng chứng → An toàn vòng lặp → Tích
> lũy mâu thuẫn → Nợ mâu thuẫn → Leo thang → Năm chiều chất lượng → Đúng/đủ/tươi/nhất
> quán/đáng tin theo thời gian → Mức vs xu hướng → Chất lượng ≠ chân lý → Suy thoái →
> Mục nát benchmark → Sụp đổ phản hồi → Sụp đổ mô hình → Sụp đổ ≠ cũ → Bảo trì → Tái xác
> minh → Tái đánh giá → Nghỉ hưu → Thay thế → Quản trị hàng loạt → Vết kiểm toán → Tin cậy
> có kiểm soát → Tin cậy ≠ đức tin → Kiến trúc sống → Điều phối → Dốc tự động hóa → Tự
> sửa ≠ tự đúng → Không bao giờ xong → Mở → Afterword
>
> **Chuỗi phân biệt trung tâm** (xuyên suốt chương, được nhắc lại nhiều lần):
> tươi ≠ đúng; giám sát ≠ quản trị; đo được ≠ hiểu được; phản hồi ≠ bằng chứng; phiên
> bản ≠ xác minh; tự sửa ≠ tự đúng; nợ tri thức ≠ nợ code; sụp đổ ≠ cũ; tin cậy ≠ đức
> tin; bảo trì ≠ đổi mà không quản trị; điểm chất lượng ≠ chân lý.

## 10.1 Từ tạo tác tĩnh đến hệ thống sống

Chín chương trước xây dựng một hệ thống tri thức ngày càng hoàn chỉnh. Nhưng mọi nấc đều
giả định **một trạng thái tại một thời điểm**: định danh ở Ch3, bản thể luận ở Ch4, claim
trong Sổ cái ở Ch6, pipeline thu nhận ở Ch7. Không nấc nào hỏi: "Chất lượng tri thức hôm
nay so với tháng trước ra sao?" "C471 còn đúng với nguồn mới nhất không?" "Index có tụt
hậu so với Sổ cái không?"

**Hệ thống tri thức sống** (Living Knowledge System, BOOK-DEFINED) là một tiến trình có
trạng thái, không phải một tấm ảnh tĩnh:

- Tri thức vào (Ch7), thay đổi ý nghĩa theo thời gian (Ch6 đồng hồ)
- Tri thức được học (Ch8), được truy vấn và trả lời (Ch9)
- Chất lượng tri thức **tiến hóa** — có thể tăng, giảm, hoặc suy thoái

Định danh của hệ thống không chỉ là nội dung tri thức mà là toàn bộ lịch sử vận hành:

SystemState = knowledge (ledger + canonical + mechanism graph)
            + index state
            + governance state
            + measurement history
            + audit log

Một cơ sở dữ liệu có nội dung hoàn hảo nhưng không có lịch sử đo lường, không kiểm toán
là một cơ sở dữ liệu — không phải hệ thống sống. Nó không thể trả lời "tuần trước hệ
thống có tin điều gì?" hay "chất lượng có cải thiện không?"

**Ví dụ RATE_OF_CHANGE:** Hệ thống biết C471 (Accepted) và C210 (Contested) từ Ch6. Sang
Ch10, câu hỏi mới là: "C471 có còn đúng với nguồn mới nhất không? Nếu E88 (bằng chứng của
C471) bị thay thế bởi E90, hệ thống có phát hiện không?"

## 10.2 Sáu luồng thay đổi

Một hệ thống tri thức sống chịu ít nhất sáu luồng thay đổi:

1. **Thu nhận claim (Ch7)** — CandidateKnowledge mới vào
2. **Đổi trạng thái quản trị (Ch6)** — claim di chuyển
   Accepted/Candidate/Contested/Rejected/Superseded
3. **Tiến hóa schema (Ch3/Ch4)** — phiên bản bản thể luận thay đổi
4. **Tụt hậu index (Ch9)** — cấu trúc truy xuất lệch so với Sổ cái
5. **Thay đổi giả thuyết (Ch8)** — cơ chế ứng viên được đề xuất, thử nghiệm, nghỉ hưu
6. **Dịch chuyển câu hỏi** — tập câu hỏi người dùng đặt thay đổi

![Sáu luồng thay đổi của hệ thống tri thức: mỗi luồng (thu nhận, đổi trạng thái, tiến hóa schema, index tụt hậu, đổi giả thuyết, dịch chuyển câu hỏi) có thể là nguồn của cũ, mâu thuẫn, hoặc nợ tri thức.](figures/generated/ch10-six-flows.pdf)

Mỗi luồng có thể là nguồn của **cũ (staleness)**, mâu thuẫn, hoặc nợ tri thức.

**Ví dụ RATE_OF_CHANGE:**
- E88 bị thay thế → C471 phải được đánh giá lại
- Bản thể luận v3 đổi tên DerivativeOperation → index vẫn ghi tên cũ
- Một CandidateMechanismHypothesis mới thách thức phạm vi của C471

## 10.3 Phát hiện cũ (Staleness Detection)

Một claim có thể:

- đúng tại valid time t_v
- còn trong Sổ cái
- nhưng dựa trên nguồn đã bị thay thế

**Cũ (staleness)** là tình trạng một claim còn đó nhưng không còn được bằng chứng hiện
tại hậu thuẫn. Cũ ≠ sai.

Định nghĩa vận hành:

ClaimStaleness
  claim → C471
  lastAssessmentTime
  sourceSuperseded → true/false
  indexReflects → true/false
  stalenessLevel (policy)

Một claim cũ vẫn có thể đúng — nó chỉ không còn được ủng hộ bởi bằng chứng tốt nhất hiện
tại. Hệ thống không được xóa claim cũ một cách im lặng; nó phải được ghi nhận và đánh giá.

**Ví dụ RATE_OF_CHANGE:**
- C471 được chấp nhận dựa trên E88
- E88 bị phát hiện đã lỗi thời (nguồn mới E90 xuất bản)
- C471 chưa sai — nó đang "cũ" và cần tái đánh giá
- Nếu không phát hiện, QA có thể trả lời từ C471 mà không biết E88 không còn là bằng
  chứng tốt nhất

## 10.4 Độ tươi (Freshness) như một số liệu hạng nhất

Hệ thống phải đo độ tươi của tri thức:

- Freshness(claim) = thời gian từ lần kiểm chứng cuối
- Freshness(index) = thời gian từ lần đồng bộ cuối với Sổ cái
- Freshness(schema) = thời gian từ lần rà soát bản thể luận cuối

**Độ tươi là một phép đo về tính thời sự, không phải phán quyết về chân lý.**

Freshness(correct) = possible, freshness(wrong) = possible.
Một claim vừa kiểm chứng vẫn có thể sai; một claim cũ vẫn có thể đúng.

**Ví dụ RATE_OF_CHANGE:**
- C471: tươi (được kiểm chứng tuần trước với E88)
- C210: tươi (được cập nhật tháng trước)
- Index của RATE_OF_CHANGE: tươi (đồng bộ hôm qua)
- Schema của DerivativeOperation: không tươi (phiên bản v2, phiên bản mới v3 có sẵn)

## 10.5 Tươi ≠ Đúng (Freshness ≠ Correctness)

Đây là ranh giới tri thức luận quan trọng nhất của chương. Một claim có thể:

- **tươi và đúng**: vừa kiểm chứng, được bằng chứng tốt nhất hậu thuẫn
- **tươi và sai**: vừa được thu nhận từ nguồn mới nhưng nguồn đó sai (hoặc hiểu sai)
- **không tươi và đúng**: claim cũ, nhưng vẫn đúng theo bằng chứng hiện tại
- **không tươi và sai**: claim cũ, và bằng chứng mới cho thấy nó sai

**Cảnh báo:** Hệ thống không bao giờ được nói "claim tươi, do đó đúng."

Độ tươi đo **tính gần đây của kiểm chứng**; độ đúng đo **sự phù hợp với bằng chứng**.
Hai trục độc lập.

![Hai trục độc lập: trục ngang là độ tươi (gần đây của kiểm chứng), trục dọc là độ đúng (được bằng chứng hỗ trợ). Bốn ô cho bốn tổ hợp; "tươi" không suy ra "đúng".](figures/generated/ch10-freshness-correctness.pdf)

**Ví dụ RATE_OF_CHANGE:**
- C471 được tái xác minh hôm qua với E90 (tươi, và đúng nếu E90 ủng hộ nó)
- Một claim mới (chưa có ID) từ pipeline thu nhận hôm nay (tươi) nhưng chưa được đánh
  giá (chưa biết đúng/sai)
- C471 không được kiểm chứng từ 6 tháng trước (không tươi) nhưng vẫn đúng (nếu E88 vẫn
  hợp lệ)

## 10.6 Đồng hồ Valid / System / Assessment ở quy mô hệ thống

Chương 6 giới thiệu ba đồng hồ cho từng claim: valid time, publication time, system
time, assessment time. Chương 10 mở rộng chúng lên toàn hệ thống:

- **valid time**: khi claim đúng trong thế giới
- **publication time**: khi nguồn được xuất bản
- **system time**: khi claim vào Sổ cái
- **assessment time**: khi claim được đánh giá lần cuối (Ch6)

Thêm:

- **measurement time**: khi một số liệu chất lượng được tính
- **audit time**: khi một bản ghi kiểm toán được ghi

Truy vấn thời gian phải chọn đúng đồng hồ:

- "Hệ thống tin gì về RATE_OF_CHANGE năm 2020?" → valid-time query
- "Sổ cái hệ thống chứa gì ngày 2025-03-01?" → system-time query
- "C471 được đánh giá lần cuối khi nào?" → assessment-time query

**Không được gộp các đồng hồ này thành một timestamp chung.**

## 10.7 Tự quan sát (Self-Observation)

Một hệ thống sống quan sát chính nó. Nó ghi lại:

- **Log truy vấn** (hành vi QA Ch9)
- **Hành vi truy xuất** (top_k, kiêng trả lời, routing)
- **Hoạt động Sổ cái** (chuyển trạng thái, tỷ lệ thu nhận)
- **Hoạt động index** (độ trễ đồng bộ)
- **Hoạt động giả thuyết** (Ch8: đề xuất, thử nghiệm, nghỉ hưu)
- **Hoạt động nguồn** (nguồn mới, nguồn cập nhật)

Tự quan sát là **ghi thụ động** (recording). Giải thích và hành động là bước riêng.

**Cảnh báo:** Ghi log không có nghĩa hệ thống hiểu chính nó. Log là nhiên liệu cho vòng
giám sát, không phải là sản phẩm cuối.

## 10.8 Đo cái gì, log cái gì

Không phải mọi thứ đều đáng đo. Tối thiểu:

- **Tỷ lệ kiêng trả lời** (QA abstention rate) theo thời gian
- **Độ dài hàng đợi mâu thuẫn** (contradiction queue)
- **Độ trễ index** (index lag)
- **Tỷ lệ thu nhận và đánh giá**
- **Tỷ lệ thay đổi giả thuyết**
- **Tỷ lệ cập nhật nguồn**
- **Phân phối intent câu hỏi** (dịch chuyển theo thời gian)

Mỗi số liệu trả lời một câu hỏi khác nhau:

- Tỷ lệ kiêng trả lời tăng → truy xuất hoặc đủ bằng chứng suy giảm
- Hàng đợi mâu thuẫn dài → chính sách giải quyết xung đột quá tải
- Độ trễ index tăng → đồng bộ suy giảm

Mỗi số liệu phải định nghĩa: đếm cái gì, trên cửa sổ nào, ở đồng hồ nào, thay đổi thế
nào là đáng chú ý.

## 10.9 Vòng giám sát (Monitoring Loop) — CƠ CHẾ TRUNG TÂM

Đây là cơ chế trung tâm của chương, được đánh dấu **BOOK-DEFINED** và **MECHANISM
CRITICAL**.

Vòng giám sát:

![Vòng giám sát (monitoring loop, BOOK-DEFINED — cơ chế trung tâm Ch10): COLLECT → AGGREGATE → COMPARE (ngưỡng là chính sách) → ALERT → ASSESS (tri thức luận, quản trị) → ACT → RE-MEASURE. Vòng quyết định sự chú ý và bảo trì, không quyết định chân lý.](figures/generated/ch10-monitoring-loop.pdf)

Mỗi tầng có chế độ thất bại riêng.

**Ví dụ RATE_OF_CHANGE:**

1. **collect:** ghi nhận sự kiện kiêng trả lời trên các câu hỏi RATE_OF_CHANGE
2. **aggregate:** tỷ lệ kiêng trả lời trên tuần = 0.21
3. **compare:** ngưỡng = 0.15 (chính sách)
4. **alert:** tỷ lệ 0.21 → cảnh báo mức MEDIUM
5. **assess:** bằng chứng cho phân loại cơ chế đã cũ (E88 bị thay thế bởi E90)
6. **act:** tái thu nhận nguồn E90, tái đánh giá C471 qua pipeline Ch7
7. **re-measure:** tỷ lệ kiêng trả lời giảm xuống 0.09

**Quan trọng:** Vòng này quyết định **sự chú ý và bảo trì**, không quyết định chân lý
của thế giới.

## 10.10 Cửa sổ tổng hợp (Aggregation Windows)

Số liệu phụ thuộc vào cửa sổ:

- **point-in-time** (ngay bây giờ)
- **sliding window** (N ngày gần nhất)
- **cumulative** (từ đầu)
- **per-version** (từ phiên bản bản thể luận N)

Cùng một luồng dữ liệu cho tín hiệu khác nhau dưới các cửa sổ khác nhau:

- Cửa sổ 1 ngày: nhiễu
- Cửa sổ 365 ngày: giấu suy thoái gần đây

**Không được trình bày "số liệu" mà không có cửa sổ của nó.**

**Ví dụ RATE_OF_CHANGE:**
- Độ dài hàng đợi mâu thuẫn hôm nay = 12 (point-in-time)
- Độ dài trung bình quý này = 8 (sliding window)
- Index lag: lần đồng bộ cuối cách đây 2.1 ngày (point-in-time, phát hiện xu hướng)

## 10.11 Ngưỡng là chính sách (Thresholds as Policy)

Ngưỡng là **quyết định chính sách**, không phải hằng số vật lý:

- Ngưỡng mã hóa mức dung sai của người vận hành
- Có thể khác nhau theo miền, loại câu hỏi, lớp claim
- Vượt ngưỡng kích hoạt **sự chú ý**, không phải phán quyết về thế giới

**Ví dụ RATE_OF_CHANGE:**
- Ngưỡng kiêng trả lời: 0.15 cho câu hỏi cơ chế, 0.05 cho câu hỏi định nghĩa sự kiện
- Ngưỡng index lag: tái index khi trễ > 1 ngày
- Ngưỡng hàng đợi mâu thuẫn: leo thang khi > 30 ngày mở

## 10.12 Ngưỡng ≠ Chân lý (Threshold ≠ Truth)

Ranh giới tri thức luận. Một số liệu vượt ngưỡng KHÔNG có nghĩa:

- tri thức là sai
- hệ thống hỏng
- một claim cụ thể sai

Nó có nghĩa: "tín hiệu này đáng được chú ý có quản trị."

**Cảnh báo:** Không bao giờ nói "tỷ lệ kiêng trả lời 0.21, do đó phân loại
RATE_OF_CHANGE là sai." Cảnh báo là điểm bắt đầu của đánh giá, không phải kết luận của nó.

## 10.13 Cảnh báo (Alerting)

Cảnh báo là một thông điệp có cấu trúc, không phải tiếng ồn:

Alert
  metric
  observedValue
  threshold
  window
  observedAt
  linkedObservations
  severity (policy-based)

Cảnh báo phải **kiểm chứng được**: một người đánh giá có thể kiểm tra các quan sát gốc
để xác nhận.

**Ví dụ cảnh báo tốt:**
- Metric: indexLag
- Value: 2.1 ngày
- Threshold: 1.0 ngày
- Window: point-in-time
- Linked: log đồng bộ index, list claim đã thêm từ lần đồng bộ cuối
- Severity: MEDIUM

**Ví dụ cảnh báo xấu:**
- "Hệ thống suy thoái" — không tham chiếu, không thể kiểm chứng

## 10.14 Đánh giá (Assessment) — giai đoạn tri thức luận

Đánh giá là giai đoạn tri thức luận của vòng giám sát:

- Số liệu có bị artifact (lỗi đo)?
- Tri thức có thực sự sai?
- Index có tụt hậu?
- Claim có cần chuyển trạng thái?

Đánh giá dùng máy móc Ch6/Ch7:

- kiểm tra chuỗi bằng chứng
- kiểm tra trạng thái quản trị
- quyết định hành động bảo trì hoặc "không hành động"

**Đánh giá ≠ hành động tự động.** Người đánh giá (con người hoặc chính sách có quản trị)
quyết định.

**Ví dụ RATE_OF_CHANGE:**
- Cảnh báo: index lag 2.1 ngày
- Đánh giá: index được xây từ bản thể luận v2, Sổ cái đã ở v3
- Nguyên nhân: lỗi cron đồng bộ
- Hành động: reindex
- Kết quả: lag → 0.1 ngày

## 10.15 Giám sát ≠ Quản trị (Monitored ≠ Governed)

Ranh giới tri thức luận. Giám sát phát hiện vấn đề. Nó không giải quyết vấn đề.

Giải quyết có quản trị đòi hỏi:

- một quyết định quản trị (Ch6/Ch7)
- một hành động được ủy quyền
- một bản ghi kiểm toán

**Cảnh báo:** Không bao giờ nói "hệ thống tự giám sát, do đó nó tự quản trị đúng." Quan
sát mà không có quản trị là giám sát, không phải quản lý.

**Ví dụ RATE_OF_CHANGE:**
- Vòng giám sát phát hiện C471 có thể đã cũ (E88 → E90) → giám sát
- Quyết định tái đánh giá C471 qua pipeline Ch7 → quản trị
- Bản ghi kiểm toán ghi: ai kích hoạt, bằng chứng gì thay đổi, quyết định gì, khi nào

## 10.16 Vòng phản hồi (Feedback Loops)

Một hệ thống sống đóng các vòng phản hồi:

- QA trả lời → user phản hồi → candidate claims
- QA thất bại → tái thu nhận → tái đánh giá
- Kiểm định giả thuyết (Ch8) → bằng chứng → chấp nhận/nghỉ hưu giả thuyết
- Đo lường → hành động bảo trì → đo lại

Vòng phản hồi mạnh và nguy hiểm:

- có thể cải thiện hệ thống
- có thể khuếch đại lỗi (sụp đổ phản hồi)
- có thể thay đổi Sổ cái mà không qua quản trị

Mỗi vòng phản hồi cần một hợp đồng:

- ai/cái gì tạo tín hiệu
- ai/cái gì chuyển tín hiệu thành trạng thái tri thức
- dưới ràng buộc quản trị nào

**Ví dụ RATE_OF_CHANGE:**
- User nói "câu trả lời về RATE_OF_CHANGE sai rồi"
- Tín hiệu: user phản hồi (QA feedback)
- Chuyển thành: CandidateClaim với source = user report
- Quản trị: chỉ pipeline Ch7 mới ghi vào Sổ cái

## 10.17 Câu trả lời QA → Ứng viên (QA Answers → Candidate Claims)

**QUY TẮC VẬN HÀNH (blocking nếu sai):** Câu trả lời QA KHÔNG phải tri thức được chấp
nhận.

Đường thu nhận duy nhất vẫn là Ch7:

QA answer / user correction / feedback
   → CandidateKnowledge
   → pipeline thu nhận + tích hợp (Ch7)
   → đánh giá có quản trị
   → có thể thành claim Accepted

Vòng QA không được tắt ngang Sổ cái.

![Cổng quản trị của vòng phản hồi: QA/user sửa chỉ tạo CandidateClaims; đường vào Sổ cái duy nhất là pipeline Ch7 (thu nhận + đánh giá có quản trị). Đường đỏ là đường bị chặn (blocking).](figures/generated/ch10-feedback-gate.pdf)

**Ví dụ RATE_OF_CHANGE:**
- User nói "thực ra finite difference LÀ một cơ chế RATE_OF_CHANGE"
- Đây trở thành CandidateKnowledge, KHÔNG phải claim Accepted mới
- Nó được đánh giá, được gán bằng chứng, được quản trị như mọi ứng viên

Câu trả lời QA ≠ thu nhận tri thức (kế thừa từ Ch9 §9.59, giờ là quy tắc vận hành).

## 10.18 User sửa (User Corrections)

User sửa là tín hiệu quý, không phải phán quyết:

- một sửa đổi là một candidate claim với provenance giá rẻ (user report)
- phải được kiểm chứng như mọi ứng viên
- có thể chỉ ra một lỗ hổng thật HOẶC một sự hiểu lầm của user

Correction → CandidateClaim (source = user report)
→ thu thập bằng chứng
→ đánh giá
→ chấp nhận / bác bỏ

userCorrection ≠ groundTruth

**Ví dụ RATE_OF_CHANGE:**
- User sửa: "vận tốc không phải tốc độ biến thiên"
- Hệ thống không tự động đổi C471
- Hệ thống tạo CandidateClaim, tìm bằng chứng (nguồn cũ và mới), đánh giá
- Có thể: C471 vẫn Accepted (bằng chứng mới không đổi) — hoặc chuyển Contested

## 10.19 Phản hồi ≠ Bằng chứng (Feedback ≠ Evidence)

Ranh giới tri thức luận. User nói câu trả lời sai — đó là phản hồi, không phải bằng chứng
về miền tri thức.

Để thành bằng chứng, cần:

- nguồn đăng ký
- fragment nguồn
- chuỗi bằng chứng (Ch6)
- đánh giá

**Cảnh báo:** Không bao giờ nói "nhiều user phàn nàn, do đó claim sai." Tín hiệu là thật;
trạng thái tri thức luận vẫn phải được thiết lập.

**Ví dụ RATE_OF_CHANGE:**
- 10 user nói "câu trả lời về dòng điện sai"
- Điều này tạo 10 CandidateClaims + 1 tín hiệu cần kiểm tra
- Không một user nào tự thay đổi C471
- Chỉ bằng chứng từ nguồn đăng ký mới thay đổi trạng thái

## 10.20 An toàn vòng phản hồi (Feedback Loop Safety)

Vòng phản hồi có thể làm hệ thống mất ổn định:

- **echo loop**: hệ thống trả lời từ đáp án của chính nó (tiền thân của model collapse)
- **confirmation loop**: chỉ có bằng chứng ủng hộ được đưa lại
- **rate loop**: sửa chữa gây thêm cảnh báo, cảnh báo gây thêm sửa chữa

Các thuộc tính an toàn cho mỗi vòng:

1. **Tốc độ có giới hạn** (bao nhiêu mục phản hồi mỗi kỳ)
2. **Provenance** (mọi mục truy vết về nguồn của nó)
3. **Cổng quản trị** (chỉ pipeline Ch7 mới ghi vào Sổ cái)
4. **Kiểm toán** (mọi hành động vòng lặp được ghi)
5. **Công tắc ngắt** (vòng lặp có thể bị dừng)

**Ví dụ RATE_OF_CHANGE:**
- Vòng phản hồi "QA → user sửa → CandidateClaims" có:
  - giới hạn 100 mục/ngày
  - provenance: mỗi mục ghi user + câu hỏi + câu trả lời gốc
  - cổng Ch7: không candidate nào vào Sổ cái mà không qua pipeline
  - kiểm toán: mỗi quyết định ghi trong audit log
  - công tắc: tắt vòng này nếu tỷ lệ chấp nhận < 5% (chỉ số chính sách)

## 10.21 Tích lũy mâu thuẫn (Contradiction Accumulation)

Sổ cái có thể tích lũy mâu thuẫn theo thời gian:

- C471 (Accepted) vs C210 (Contested) tồn tại từ Ch6
- nguồn mới xuất hiện củng cố một phía
- không ai tái đánh giá

Định nghĩa:

ContradictionQueue = tập hợp các cặp mâu thuẫn mở với phạm vi của chúng

Một hàng đợi lớn là **nợ**: các xung đột tri thức luận chưa được phân xử.

Tích lũy là bình thường; tích lũy **im lặng** là rủi ro.

**Ví dụ RATE_OF_CHANGE:**
- C471 vs C210 được nhập từ Ch6
- Sang Ch10, hệ thống theo dõi cặp này đã mở bao lâu
- Một cập nhật nguồn (E90) có thể giải quyết hoặc củng cố nó
- Độ dài hàng đợi là số liệu sức khỏe

## 10.22 Nợ tri thức và nợ mâu thuẫn (Knowledge Debt, Contradiction Debt)

**Nợ tri thức** (knowledge debt, BOOK-DEFINED) là chi phí tích lũy của các nghĩa vụ tri
thức luận chưa giải quyết:

- mâu thuẫn mở
- claim Accepted đã cũ chưa đánh giá lại
- candidate chưa đánh giá
- phiên bản schema lỗi thời
- index chưa đồng bộ

nợ tri thức ≠ nợ code (mã chương trình)

Nợ tri thức được đo bằng **đơn vị tri thức luận** (claims đang chờ đánh giá), không phải
dòng mã.

**Nợ mâu thuẫn** là phần nợ tri thức do các cặp mâu thuẫn chưa phân xử.

![Nợ mâu thuẫn theo thời gian: nếu các cặp mâu thuẫn mở không được phân xử, nợ leo thang vượt ngưỡng chính sách và kích hoạt tái đánh giá.](figures/generated/ch10-contradiction-debt.pdf)

**Ví dụ RATE_OF_CHANGE:**
- Nợ = {C471/C210 mở 60 ngày, index lag 2.1 ngày, 14 candidates chưa đánh giá}
- Hệ thống phải hiển thị nợ của nó, không giấu

## 10.23 Chính sách leo thang (Escalation Policy)

Không phải nợ nào cũng phải xử lý ngay. Định nghĩa leo thang:

- **low**: log, rà soát ở chu kỳ tới
- **medium**: tái đánh giá trong một cửa sổ
- **high**: hành động có quản trị NGAY (tái thu nhận nguồn, tái đánh giá claim, reindex)

Leo thang là chính sách (ngưỡng + ưu tiên), không phải phán quyết chân lý tự động.

**Ví dụ RATE_OF_CHANGE:**
- C471/C210 mở 30 ngày → medium
- E88 bị thay thế VÀ C471 phụ thuộc nó → high
- Hàng đợi mâu thuẫn > 20 cặp → medium cho toàn bộ

## 10.24 Năm chiều chất lượng tri thức (Quality Dimensions)

Định nghĩa tối thiểu năm chiều:

| Chiều | Định nghĩa | Đo bằng | Cửa sổ | KHÔNG đo |
|-------|------------|---------|--------|----------|
| **Correctness** | được bằng chứng ủng hộ và đúng | tỷ lệ claim qua re-validation | cửa sổ trượt | độ tươi |
| **Completeness** | phủ phạm vi khai báo | tỷ lệ che phủ theo scope | per-scope | chân lý tuyệt đối |
| **Freshness** | gần đây của kiểm chứng | tuổi kiểm chứng, index lag | cửa sổ trượt | độ đúng |
| **Consistency** | không xung đột cùng phạm vi | số mâu thuẫn không scope | point-in-time | không mâu thuẫn nào cả |
| **Trustworthiness** | độ tin cậy của provenance/governance | tỷ lệ claim có chuỗi bằng chứng lành | cumulative | độ đúng |

Mỗi chiều có định nghĩa, thước đo, cửa sổ, và **điều nó KHÔNG đo**.

![Năm chiều chất lượng tri thức: Correctness (đúng), Completeness (đủ), Freshness (tươi), Consistency (nhất quán), Trustworthiness (đáng tin) — đo hành vi quản lý tri thức, không phải chân lý.](figures/generated/ch10-quality-dimensions.pdf)

chất lượng ≠ chân lý

Một hệ thống chất lượng cao có thể chứa claim sai nhưng được nguồn gốc trung thực; một
hệ thống chất lượng thấp có thể "đúng" do may mắn.

## 10.25 Độ đúng theo thời gian (Correctness over Time)

Độ đúng không phải ảnh tĩnh; nó tiến hóa:

- claim được đánh giá Accepted ngày 1 có thể thất bại re-validation ngày 100
- độ đúng tại t tương đối với bằng chứng có tại t

Đo:

- tỷ lệ claim mà re-validation xác nhận
- tỷ lệ câu trả lời khớp với tri thức kiểm chứng sau

correct(t) ≠ correct(t+Δ) một cách tự động

**Ví dụ RATE_OF_CHANGE:**
- C471 qua đánh giá với E88 ở Ch6
- Một nguồn mới ở Ch10 mâu thuẫn E88
- Trạng thái đúng phải được suy lại, không được giả định vĩnh viễn

## 10.26 Độ đủ theo thời gian (Completeness over Time)

Độ đủ = phủ phạm vi khai báo:

- tất cả ứng dụng RATE_OF_CHANGE đã được biểu diễn chưa?
- cơ chế mới có bị bỏ sót không?

Độ đủ tương đối với phạm vi khai báo, không bao giờ tuyệt đối.

Một hệ thống có thể đủ cho một miền và mù ở miền khác.

**Không được trình bày "độ đủ" như một con số đơn lẻ không có phạm vi.**

**Ví dụ RATE_OF_CHANGE:**
- Phạm vi miền: cơ học, điện học, động học dân số
- Một ứng dụng mới (dòng nhiệt) xuất hiện trong nguồn
- Độ đủ giảm tương đối so với phạm vi mở rộng

## 10.27 Độ tươi theo thời gian (Freshness over Time)

Theo dõi độ tươi từng hệ con:

- **ledger freshness** (lần kiểm chứng toàn phần cuối)
- **index freshness** (độ trễ đồng bộ)
- **schema freshness** (phiên bản bản thể luận)

Độ tươi suy giảm nếu không bảo trì.

Một số liệu "tươi" phải nói rõ đo hệ con nào.

**Ví dụ RATE_OF_CHANGE:**
- Index xây từ bản thể luận v2, Sổ cái đã ở v3 → index freshness thấp
- QA có thể trả lời từ cấu trúc cũ (liên kết Ch9 §9.57)

## 10.28 Nhất quán theo thời gian (Consistency over Time)

Các chiều nhất quán:

- **nhất quán logic** (không có A và not-A cùng Accepted)
- **nhất quán schema** (instance hợp quy)
- **nhất quán provenance** (chuỗi bằng chứng phân giải)

Lưu ý: C471 vs C210 KHÔNG phải vi phạm nhất quán nếu phạm vi khác nhau — đó là mâu thuẫn
được quản trị với phạm vi tường minh.

Số liệu nhất quán phải phân biệt:

- **inconsistency giải quyết được** (bug)
- **mâu thuẫn được quản trị** (cố ý, có phạm vi)

**Ví dụ RATE_OF_CHANGE:**
- C471 và C210 cùng tồn tại với phạm vi khác nhau = mâu thuẫn được quản trị
- Hai claim cùng Accepted, cùng phạm vi, nội dung ngược nhau = inconsistency

## 10.29 Độ đáng tin theo thời gian (Trustworthiness over Time)

Độ đáng tin = độ tin cậy của provenance và quản trị:

- nguồn đã đăng ký và kiểm chứng? (Ch7)
- chuỗi bằng chứng còn nguyên? (Ch6)
- chuyển quản trị được kiểm toán? (Ch6/Ch7)
- provenance có thể lấy cho mọi claim Accepted?

Một claim có thể đúng nhưng độ đáng tin thấp (không trích dẫn, không đánh giá).

đáng tin ≠ đúng

**Ví dụ RATE_OF_CHANGE:**
- C471 có E88 + kiểm toán quản trị → độ đáng tin cao
- Giả thuyết học từ Ch8 không có nguồn → độ đáng tin thấp (candidate)

## 10.30 Mức vs Xu hướng (Levels vs Trends)

Một giá trị đơn là một **mức** (level); thay đổi theo thời gian là **xu hướng** (trend).

- mức: tỷ lệ kiêng trả lời = 0.12 tuần này
- xu hướng: tăng 6 tuần liên tiếp

Xu hướng quan trọng cho phát hiện:

- trôi chậm vô hình trong một điểm
- đột biến nhọn vô hình trong trung bình dài

Một hệ thống khỏe mạnh nhìn xu hướng, không chỉ mức.

**Ví dụ RATE_OF_CHANGE:**
- Hàng đợi mâu thuẫn mức = 12 (phẳng)
- Xu hướng: +3/tháng trong 4 tháng → nợ đang tăng

## 10.31 Chất lượng ≠ Chân lý (Quality ≠ Truth)

Ranh giới tri thức luận.

Các số liệu chất lượng đo **hành vi quản lý tri thức** của hệ thống:

- độ tươi, độ nhất quán, độ đủ, độ đáng tin

Chúng KHÔNG đo việc thế giới có khớp với tri thức hay không.

Một hệ thống có thể:

- chất lượng cao và sai (claim sai được bảo trì tốt)
- chất lượng thấp và đúng (cũ nhưng tình cờ đúng)

**Cảnh báo:** Không bao giờ nói "điểm chất lượng 0.92, do đó tri thức là đúng."

**Ví dụ RATE_OF_CHANGE:**
- C471 được tái xác minh đều đặn (chất lượng cao) nhưng nếu E90 mâu thuẫn nó và chưa ai
  phát hiện, nó vẫn sai
- Hệ thống có độ đáng tin thấp (ít kiểm toán) vẫn có thể đúng về vận tốc

## 10.32 Suy thoái (Degradation)

**Suy thoái** (degradation) = suy giảm kéo dài của một chiều chất lượng:

- độ tươi giảm
- hàng đợi mâu thuẫn tăng
- tỷ lệ kiêng trả lời tăng
- độ đủ thu hẹp (phạm vi miền bị bỏ sót)

Suy thoái là một xu hướng, không phải một sự kiện.

Phát hiện cần:

- baseline (số liệu trước khi suy giảm)
- xu hướng (độ dốc trên cửa sổ)
- so sánh (với dung sai chính sách)

suy thoái ≠ một sự kiện xấu đơn lẻ

**Ví dụ RATE_OF_CHANGE:**
- Tỷ lệ kiêng trả lời tăng từ 0.08 lên 0.18 trong 3 tháng → suy thoái
- Một ngày 0.30 (do nguồn bị gián đoạn tạm thời) → sự kiện, chưa phải suy thoái

## 10.33 Mục nát benchmark (Benchmark Decay)

Benchmark và test set suy giảm theo thời gian:

- test set QA bị pipeline "biết" → overfitting
- benchmark không còn phản ánh câu hỏi thật
- held-out set trở thành một phần của training (leakage)

Hệ thống phải định kỳ **tái soạn hoặc tái lấy mẫu** benchmark của nó.

benchmarkScore(t) ≠ system quality(t)

Điểm benchmark tăng có thể đi cùng chất lượng thực giảm.

**Bằng chứng (Recht et al. 2019):** khi xây lại test set ImageNet bằng đúng quy trình tạo
dữ liệu ban đầu, độ chính xác của nhiều mô hình giảm 11–14%. Kết luận của tác giả: mức
giảm không chủ yếu do overfitting vào test set cũ, mà do các mô hình không tổng quát hóa
được sang hình ảnh khó hơn một chút.

**Ví dụ RATE_OF_CHANGE:**
- Bộ câu hỏi QA về RATE_OF_CHANGE được dùng lại nhiều tháng
- Pipeline tối ưu cho bộ câu hỏi này
- Bộ câu hỏi mới (do chuyên gia soạn lại) cho điểm thấp hơn hẳn
- Bài học: điểm benchmark tăng ≠ chất lượng hệ thống tăng

## 10.34 Sụp đổ phản hồi (Feedback Collapse)

Nếu hệ thống trả lời từ đáp án của chính nó:

1. một câu trả lời đầu sai nhưng trôi chảy
2. user/agent chấp nhận nó
3. nó trở thành câu trả lời "được biết"
4. hệ thống truy xuất và lặp lại nó
5. bằng chứng gốc bị lãng quên

Đây là **sụp đổ phản hồi** (feedback collapse, BOOK-DEFINED): vòng lặp khuếch đại một lỗi
thành sự sai lệch bền vững.

![Sụp đổ phản hồi: một câu trả lời sai nhưng trôi chảy được chấp nhận, trở thành câu trả lời "được biết", được lặp lại, và bằng chứng gốc bị lãng quên — vòng tự củng cố.](figures/generated/ch10-feedback-collapse.pdf)

Phòng ngừa:

- câu trả lời không bao giờ tái vào Sổ cái trực tiếp (quy tắc Ch9, giờ là quy tắc vận hành)
- truy xuất giữ provenance nguồn
- cho phép kiêng trả lời
- vòng lặp giới hạn tốc độ và được kiểm toán

sụp đổ phản hồi ≠ nhiễu ngẫu nhiên

Nó có hệ thống và tự củng cố.

**Ví dụ RATE_OF_CHANGE:**
- QA trả lời sai "RATE_OF_CHANGE chỉ mô tả vận tốc" (từ index cũ)
- User chấp nhận, feedback tạo Candidates
- Không có cổng Ch7, các Candidates sẽ củng cố lỗi
- Có cổng Ch7, chúng vào như candidates và được đánh giá
- Kiểm toán cho thấy lịch sử vòng lặp

## 10.35 Sụp đổ mô hình (Model Collapse)

Khi một mô hình sinh huấn luyện trên đầu ra của chính nó, phân bố đầu ra suy thoái:

- đa dạng co lại
- nội dung đúng nhưng hiếm bị mất
- lỗi cộng dồn

Hệ thống tri thức có dạng nhẹ hơn:

- nếu tóm tắt của KG trở thành KG
- nếu claim sinh ra trở thành nguồn
- nếu bằng chứng tổng hợp thay thế nguồn đăng ký

**Bằng chứng (Shumailov et al. 2024, tái dùng từ Ch8):** huấn luyện trên dữ liệu tạo ra
một cách đệ quy gây "các khuyết tật không thể đảo ngược, nơi đuôi của phân bố nội dung gốc
biến mất".

Sự bảo vệ là kỷ luật quen thuộc từ đầu sách:

- phân biệt artifact suy diễn với nguồn
- không bao giờ để đầu ra thành dữ liệu huấn luyện/thu nhận mà không có provenance
- giữ nguồn gốc đã đăng ký

sụp đổ mô hình ≠ cũ đơn thuần

Đây là một thất bại cấu trúc riêng biệt.

## 10.36 Sụp đổ ≠ Cũ (Collapse ≠ Staleness)

Ranh giới tri thức luận.

- **cũ (staleness)**: nội dung cũ nhưng cấu trúc nguyên vẹn
- **sụp đổ (collapse)**: nội dung bị tái tuần hoàn và thoái hóa

Hệ thống cũ có tri thức cũ.
Hệ thống sụp đổ có tri thức thoái hóa.

Cả hai cần bảo trì; cơ chế khác nhau:

- cũ → tái xác minh, tái thu nhận
- sụp đổ → phá vòng phản hồi, khôi phục nguồn, thu nhận lại / huấn luyện lại

**Ví dụ RATE_OF_CHANGE:**
- C471 cũ (E88 lỗi thời) → re-validation
- Tóm tắt cộng đồng GraphRAG được dùng lại làm nguồn cho câu trả lời → nguy cơ sụp đổ
  → phải phá vòng lặp (không dùng tóm tắt làm nguồn)

## 10.37 Thao tác bảo trì (Maintenance Operations)

Định nghĩa các thao tác có quản trị của hệ thống sống:

1. **re-validation** — kiểm lại claim với nguồn hiện tại
2. **re-assessment** — chạy lại đánh giá Ch6 (trạng thái có thể đổi)
3. **retirement** — đưa claim sang Rejected/Superseded với kiểm toán
4. **supersession** — ghi nhận claim B thay thế claim A
5. **re-ingestion** — chạy lại thu nhận cho một nguồn (Ch7)
6. **reindex** — đồng bộ lại cấu trúc truy xuất với Sổ cái (Ch9)
7. **re-scope** — rà soát/sửa phiên bản bản thể luận (Ch3/Ch4)

Mỗi thao tác:

- có kích hoạt (policy, alert, lịch, yêu cầu)
- có ủy quyền (governance)
- ghi bản ghi kiểm toán
- có thể đảo ngược hoặc có rollback

bảo trì ≠ đổi không qua xem xét

**Ví dụ RATE_OF_CHANGE:**
- reindex: tự động khi lag > 1 ngày
- re-assessment của C471: có quản trị khi E88 → E90
- retirement của C210: có quản trị + kiểm toán nếu bằng chứng mới bác nó

## 10.38 Tái xác minh ở quy mô (Re-validation at Scale)

Hệ thống có nhiều claim; tái xác minh phải mở rộng được:

- **toàn phần** (đắt, hiếm)
- **lấy mẫu** (thống kê, định kỳ)
- **kích hoạt** (khi nguồn cập nhật)

Lấy mẫu dùng thống kê, không phải cảm tính:

- chọn cỡ mẫu cho độ tin cậy mong muốn
- tổng quát hóa từ mẫu ra quần thể cẩn thận
- ghi rõ đã lấy mẫu gì và khi nào

tái xác minh ≠ đúng vĩnh viễn

Tái xác minh giảm rủi ro; không loại bỏ rủi ro.

**Ví dụ RATE_OF_CHANGE:**
- 5% claims phân loại cơ chế được tái xác minh mỗi quý
- Nếu E88 đổi, mọi claim trích dẫn E88 được tái xác minh (kích hoạt)

## 10.39 Tái đánh giá (Re-assessment)

Tái đánh giá là một chuyển trạng thái có quản trị:

- C471 (Accepted) → tái đánh giá dưới bằng chứng mới → giữ Accepted, chuyển Contested,
  hoặc thành Superseded
- chuyển trạng thái ghi: ai/cái gì kích hoạt, bằng chứng gì đổi, quyết định gì, tại thời
  điểm assessment nào

Tái đánh giá là quản trị Ch6 áp dụng lặp lại.

**Ví dụ RATE_OF_CHANGE:**
- E88 bị thay thế bởi E90 (nguồn mới)
- C471 tái đánh giá: bằng chứng E90 ủng hộ nó → giữ Accepted
- Hoặc: E90 làm yếu nó → C471 chuyển Contested với phạm vi mới

## 10.40 Nghỉ hưu (Retirement)

**Nghỉ hưu** = đưa tri thức ra khỏi dòng hoạt động với bản ghi có quản trị:

- claim → Rejected/Superseded
- phiên bản schema → deprecated
- giả thuyết → nghỉ hưu (Ch8)

Nghỉ hưu KHÔNG phải xóa:

- bản ghi vẫn còn (lịch sử được giữ)
- kiểm toán vẫn còn
- claim có thể được phục hồi nếu bằng chứng đổi

nghỉ hưu ≠ xóa

**Ví dụ RATE_OF_CHANGE:**
- C210 vẫn ở Sổ cái như Contested ngay cả khi bị thay thế bởi công thức mới
- Một CandidateMechanismHypothesis đã nghỉ hưu vẫn giữ lịch sử thử nghiệm

## 10.41 Thay thế ở quy mô (Supersession at Scale)

Khi claim B thay thế claim A:

- ghi cạnh A → B
- đánh dấu trạng thái A (Superseded/Rejected)
- giữ nguyên chuỗi bằng chứng của A
- cập nhật các cấu trúc phụ thuộc (index, tóm tắt, câu trả lời QA)

Chuỗi thay thế tạo lịch sử: A → B → C

Truy vấn phải thấy cả trạng thái hiện tại lẫn lịch sử (Ch9 Canonical vs Ledger, giờ ở
quy mô hệ thống).

**Ví dụ RATE_OF_CHANGE:**
- Công thức của cơ chế đạo hàm bị thay thế qua các phiên bản bản thể luận
- QA phải phân biệt "canonical hiện tại" với "lịch sử"

## 10.42 Quản trị hàng loạt (Batch Governance)

Đôi khi quản trị phải tác động lên nhiều claim cùng lúc:

- di trú schema (Ch3/Ch4) tái phân loại nhiều instance
- một nguồn bị rút lại làm mất hiệu lực nhiều chuỗi bằng chứng
- một ngưỡng đổi kích hoạt nhiều tái đánh giá

Thao tác hàng loạt cần:

- kế hoạch (cái gì bị ảnh hưởng, theo thứ tự nào)
- **dry-run** (mô phỏng trước khi áp dụng)
- kiểm toán (mọi thay đổi cá nhân được ghi)
- rollback (đảo ngược nếu batch thất bại)

thay đổi hàng loạt ≠ sửa ồ ạt

**Ví dụ RATE_OF_CHANGE:**
- Bản thể luận v2 → v3 đổi tên DerivativeOperation
- Batch: tái phân loại mọi instance DerivativeOperation, reindex, kiểm tra QA

## 10.43 Vết kiểm toán toàn hệ thống (System-level Audit Trails)

Mọi hành động có quản trị phải kiểm toán được:

AuditRecord
  what (thao tác)
  who/what (actor, agent, policy)
  onWhat (claim/claim-set/index/schema)
  beforeState
  afterState
  evidence (vì sao)
  at (thời điểm audit)
  authorization (tham chiếu quản trị)

Vết kiểm toán là bộ nhớ của hệ thống về hành vi của chính nó.

Không có vết kiểm toán, "tin cậy" chỉ là đức tin.

kiểm toán ≠ chỉ ghi log

Vết kiểm toán phải hỗ trợ **tái dựng**: cho một câu trả lời, bạn có thể phát lại vì sao
hệ thống tin nó?

![Tái dựng niềm tin qua vết kiểm toán: câu trả lời trích dẫn C471 → AuditRecord (chấp nhận lúc T bởi X) → chuỗi bằng chứng E88 → quyết định quản trị + authorization → nguồn đã đăng ký (Ch7).](figures/generated/ch10-audit-replay.pdf)

**Ví dụ RATE_OF_CHANGE:**
- Một câu trả lời trích dẫn C471
- Phát lại: C471 được Accepted tại assessment time T bởi người đánh giá X dưới bằng
  chứng E88
- Câu trả lời sau khi E90 tái đánh giá phản ánh trạng thái mới

## 10.44 Tin cậy có kiểm soát (Controlled Trust)

Tin cậy ở đây là một thuộc tính kỹ thuật, không phải thái độ:

- tin cậy = hành vi hệ thống có thể kiểm chứng qua provenance, quản trị, kiểm toán
- tin cậy có kiểm soát = bạn có thể kiểm tra vì sao hệ thống tin điều nó tin

Tin cậy được xây dựng bằng:

- nguồn đã đăng ký (Ch7)
- chuỗi bằng chứng (Ch6)
- chuyển quản trị (Ch6/Ch7)
- provenance câu trả lời (Ch9)
- vết kiểm toán (chương này)

tin cậy ≠ phụ thuộc mù

**Cảnh báo:** Không bao giờ nói "hệ thống đáng tin vì chúng tôi xây nó." Tin cậy được
chứng minh, không phải được tuyên bố.

## 10.45 Tin cậy ≠ Đức tin (Trust ≠ Blind Trust)

Ranh giới tri thức luận.

Một hệ thống kiểm chứng được là đáng tin theo nghĩa kỹ thuật — bạn CÓ THỂ kiểm tra nó.

Không suy ra rằng bạn không cần kiểm tra, hoặc mọi câu trả lời đều đúng.

tin cậy-có-kiểm-chứng ≠ tin-cậy-không-cần-kiểm-tra

Quan điểm của cuốn sách:

- hệ thống đáng tin nhờ phơi bày suy luận của nó
- người dùng/người vận hành vẫn giám sát
- tin cậy được kiếm từng hệ con, từng hành động, theo thời gian

**Cảnh báo:** Không bao giờ nói "hệ thống tự tin, do đó ta có thể ngừng kiểm tra."

## 10.46 Kiến trúc sống (Living Architecture)

Đề xuất một kiến trúc toàn hệ thống, đánh dấu **BOOK-DEFINED** và **BOOK ENGINEERING
MODEL**:

![Kiến trúc sống (living architecture, BOOK ENGINEERING MODEL): các vòng phản hồi giữa Knowledge Core, Thu nhận (Ch7), Học (Ch8), Truy xuất/QA (Ch9), Quan sát & Giám sát, Đánh giá & Bảo trì, Quản trị & Kiểm toán (Ch6) — một tập các vòng, không phải pipeline tuyến tính.](figures/generated/ch10-living-architecture.pdf)

Kiến trúc là một tập các vòng phản hồi, không phải pipeline tuyến tính.

Rõ: đây là **mô hình kỹ thuật của cuốn sách**, không phải kiến trúc sản phẩm của một
công ty cụ thể.

## 10.47 Điều phối các vòng (Orchestration of the Loops)

Các vòng phải được điều phối:

- khi nào QA thất bại kích hoạt tái thu nhận?
- khi nào nguồn cập nhật kích hoạt tái đánh giá?
- khi nào index lag kích hoạt reindex?
- khi nào giả thuyết thách thức kích hoạt tái xác minh?
- ưu tiên giữa các hành động bảo trì cạnh tranh?

Định nghĩa:

- kích hoạt (điều kiện)
- quyền hạn (ai quyết định)
- ngân sách (bao nhiêu công việc chấp nhận được)
- thứ tự (chính sách ưu tiên)

điều phối ≠ một vòng lớn tự làm mọi thứ

Hệ thống nên tự động hóa ít hơn và làm theo chính sách nhiều hơn khi rủi ro tăng.

**Ví dụ RATE_OF_CHANGE:**
- index lag > 1 ngày → reindex (tự động, rủi ro thấp)
- C471 tái đánh giá dưới bằng chứng mới → có quản trị (rủi ro cao hơn)
- di trú schema → dry-run + kiểm toán (rủi ro cao nhất)

## 10.48 Dốc tự động hóa (Automation Gradient)

Các hành động khác nhau xứng đáng mức tự động hóa khác nhau:

| Hành động | Tự động | Vì sao |
|-----------|---------|--------|
| đồng bộ index | hoàn toàn | cơ học, đảo ngược |
| cảnh báo số liệu | hoàn toàn | chỉ đọc |
| tái xác minh claim rủi ro thấp | tự động + kiểm toán | rủi ro giới hạn |
| tái đánh giá claim | cổng quản trị | đổi tri thức luận |
| di trú schema | dry-run + phê duyệt | bán kính ảnh hưởng rộng |
| nghỉ hưu tri thức | quản trị + kiểm toán | lịch sử quan trọng |

tự động hóa ≠ xóa bỏ quản trị

Tác động càng lớn → càng nhiều cổng.

**Ví dụ RATE_OF_CHANGE:**
- reindex: tự động
- tái đánh giá C471: có quản trị
- di trú bản thể luận v3: dry-run + phê duyệt

## 10.49 Tự sửa ≠ Tự đúng (Auto-repair ≠ Auto-truth)

Ranh giới tri thức luận.

Một thao tác bảo trì tự động có thể sửa một vấn đề quy trình.

Nó không chứng nhận tri thức kết quả là đúng.

tự sửa ≠ tự đúng

**Cảnh báo:** Không bao giờ nói "hệ thống tự sửa, do đó claim được sửa là đúng."

Sửa chữa sửa vận hành; đánh giá thiết lập trạng thái tri thức luận.

**Ví dụ RATE_OF_CHANGE:**
- Reindex tự động (tự sửa) làm index khớp Sổ cái
- Nhưng nội dung (C471) có đúng hay không vẫn cần đánh giá có bằng chứng
- Tự sửa chỉ phục hồi tính nhất quán; không xác nhận chân lý

## 10.50 Hệ thống không bao giờ "xong" (The System is Never "Done")

Quan điểm đóng của cuốn sách:

- một hệ thống tri thức là một tiến trình, không phải một tạo tác
- nó phải được đo, được bảo trì, và được tin cậy dưới kiểm soát
- "xong" là một hư cấu nguy hiểm: nguồn đổi, phạm vi đổi, người dùng đổi

Câu trả lời trung tâm cho câu hỏi mở đầu chương:

> Hệ thống giữ được sự đáng tin không phải vì đã hoàn thành, mà vì nó quan sát được,
> đo được, quản trị được, và kiểm toán được trong khi chạy.

Phần này đóng lập luận của cuốn sách và bàn giao cho Afterword.

## 10.51 Vấn đề mở → Afterword

Kết thúc bằng biên giới mở:

- **quyền hạn**: ai phê duyệt các hành động bảo trì tự động?
- **giám sát con người**: thực hiện ra sao ở quy mô lớn?
- **chi phí**: cái gì giới hạn giám sát và bảo trì?
- **đa hệ thống**: nhiều agent/hệ thống chia sẻ quản trị ra sao?
- **paradigm shift**: hệ thống xử lý một thay đổi làm schema vô hiệu ra sao?

Đây KHÔNG phải những bài toán được giải trong sách — đây là biên giới người đọc bước vào.

Bàn giao cho:

# Afterword

## 10.52 Ca làm việc 1: Báo cáo sức khỏe hệ thống (System Health Report)

Ca làm việc RATE_OF_CHANGE đầy đủ, 10 bước:

1. **Trạng thái hệ thống:** C471 Accepted, C210 Contested, index v2, bản thể luận v3
2. **Quan sát:** tỷ lệ kiêng trả lời, hàng đợi mâu thuẫn, index lag
3. **Tổng hợp:** các số liệu trên cửa sổ 30 ngày
4. **Index lag = 2.1 ngày** (ngưỡng 1.0) → cảnh báo
5. **Đánh giá:** index xây từ v2, Sổ cái đã ở v3
6. **Hành động:** reindex (tự động, kiểm toán)
7. **Đo lại:** lag → 0.1 ngày
8. **Hàng đợi mâu thuẫn:** C471/C210 mở 60 ngày (ngưỡng 30) → medium
9. **Đánh giá:** nguồn mới E90 xuất bản → kích hoạt tái đánh giá C471
10. **Ghi kết quả tái đánh giá; cập nhật báo cáo sức khỏe**

| Số liệu | Mức | Xu hướng | Ngưỡng | Trạng thái |
|---------|-----|----------|--------|------------|
| Tỷ lệ kiêng trả lời | 0.12 | +0.03/tháng | 0.15 | theo dõi |
| Hàng đợi mâu thuẫn | 12 | +3/tháng | 10 | MEDIUM |
| Index lag | 0.1 ngày | −2.0 từ tuần trước | 1.0 ngày | OK |
| Độ tươi C471 | OK (E90) | — | — | OK |
| Độ đủ phạm vi | 3/3 miền | — | — | OK |

## 10.53 Ca làm việc 2: Claim Accepted bị cũ (Stale Accepted Claim)

1. C471 Accepted dựa trên E88
2. E88 bị thay thế bởi E90 (giám sát nguồn phát hiện)
3. Kích hoạt tái xác minh các claim trích dẫn E88
4. Tái đánh giá: E90 thay đổi bức tranh
5. C471 → Contested (hoặc giữ Accepted với bằng chứng cập nhật)
6. Ghi bản ghi kiểm toán
7. QA giờ kiêng trả lời hoặc trả lời với trạng thái cập nhật
8. Tỷ lệ kiêng trả lời về baseline
9. Lịch sử niềm tin của hệ thống được giữ
10. Bài học: Accepted ≠ vĩnh viễn

## 10.54 Ca làm việc 3: Vòng phản hồi đi sai (Feedback Loop Gone Wrong)

1. QA trả lời câu hỏi RATE_OF_CHANGE từ index cũ
2. Câu trả lời sai nhưng trôi chảy
3. User "sửa" bằng chính mô hình sai đó
4. Phản hồi trở thành CandidateClaims
5. Không có cổng quản trị → chúng củng cố lỗi
6. Có cổng Ch7 → chúng vào như candidates và được đánh giá
7. Kiểm toán cho thấy lịch sử vòng lặp
8. Bài học: cổng quản trị là thứ giữ phản hồi khỏi trở thành sụp đổ

Đây là minh chứng mức cơ chế cho sự an toàn của vòng phản hồi.

## 10.55 Những quan niệm sai phổ biến (Common Misconceptions)

1. Claim tươi là claim đúng. — Không (tươi = gần đây kiểm chứng, chưa phải đúng)
2. Điểm chất lượng cao nghĩa là tri thức đúng. — Không (chất lượng ≠ chân lý)
3. Giám sát = quản trị. — Không
4. Hệ thống tự quan sát là hệ thống tự sửa. — Không (quan sát ≠ hành động)
5. User sửa tự động đúng. — Không (phản hồi ≠ bằng chứng)
6. Phản hồi có thể tắt ngang pipeline Ch7. — Không (blocking)
7. Claim Accepted là Accepted mãi mãi. — Không (re-validation bắt buộc)
8. Tái xác minh một lần = hợp lệ mãi. — Không
9. "Không cảnh báo" nghĩa là "mọi thứ ổn." — Không (chỉ bao phủ điều được đo)
10. Vượt ngưỡng chứng minh một claim cụ thể sai. — Không (chỉ cần chú ý)
11. Mâu thuẫn trong Sổ cái luôn là bug. — Không (mâu thuẫn được quản trị hợp lệ)
12. Hàng đợi mâu thuẫn dài là vô hại. — Không (nợ chất lượng)
13. Đáp án của hệ thống có thể an toàn thành dữ liệu thu nhận. — Không (nguy cơ collapse)
14. Điểm benchmark tăng = hệ thống cải thiện. — Không (mục nát benchmark)
15. Tóm tắt của KG có thể thay nguồn đã đăng ký. — Không
16. Di trú schema chỉ là chi tiết cài đặt. — Không (bán kính rộng)
17. Tái đánh giá hàng loạt làm không cần dry-run. — Không
18. Xóa giống nghỉ hưu. — Không (nghỉ hưu giữ lịch sử)
19. Ghi log tự động là vết kiểm toán tốt. — Không (kiểm toán cần tái dựng được)
20. Tin cậy = không bao giờ kiểm tra lại. — Không (tin cậy ≠ đức tin)
21. Tự động hóa xóa bỏ quản trị. — Không (quản trị chuyển lên mức cao hơn)
22. Hành động bảo trì chứng nhận chân lý. — Không (tự sửa ≠ tự đúng)
23. Nợ tri thức giống nợ code. — Không (cơ chế khác nhau)
24. Uptime khỏe mạnh = tri thức khỏe mạnh. — Không (đo cái khác)
25. Hệ thống "xong" một khi được xây. — Không (không bao giờ xong)
26. Giám sát càng nhiều càng tốt. — Không (chi phí, không đo kịch liệt)
27. Số liệu chất lượng không cần cửa sổ có nghĩa. — Không
28. Cũ và sụp đổ là cùng một thất bại. — Không
29. Hệ thống sống không cần giám sát con người. — Không
30. Thu nhận lại một nguồn vô hại theo mặc định. — Không (cần đánh giá ảnh hưởng)

## 10.56 Điểm tự kiểm tra (Self-explanation Checkpoints)

1. **Tại sao claim tươi không nhất thiết đúng?** — Trục tươi đo độ gần đây kiểm chứng;
   trục đúng đo độ phù hợp bằng chứng; hai trục độc lập (§10.5)
2. **Tại sao vượt ngưỡng giám sát không chứng minh tri thức sai?** — Ngưỡng là chính sách,
   kích hoạt chú ý, không phải phán quyết thế giới (§10.12)
3. **Tại sao user sửa là phản hồi, không phải bằng chứng?** — Để thành bằng chứng cần
   nguồn đăng ký + chuỗi bằng chứng + đánh giá (§10.19)
4. **Tại sao câu trả lời QA không thể tái vào Sổ cái mà không qua cổng Ch7?** — Nếu tái
   vào trực tiếp, vòng lặp có thể khuếch đại lỗi thành sụp đổ (§10.17, §10.34)
5. **Tại sao "hệ thống tự giám sát" không phải "hệ thống tự quản trị"?** — Giám sát phát
   hiện; quản trị quyết định, ủy quyền, kiểm toán (§10.15)
6. **Tại sao sụp đổ phản hồi khác đơn thuần cũ?** — Cũ là lệch thời gian; sụp đổ là thoái
   hóa do tái tuần hoàn (§10.36)
7. **Tại sao vết kiểm toán làm hệ thống đáng tin mà không làm nó bất khả ngộ?** — Kiểm
   toán cho phép tái dựng niềm tin; vẫn cần đánh giá từng hành động (§10.43)
8. **Tại sao "hệ thống không bao giờ xong" là nguyên tắc thiết kế, không phải thất bại?**
   — Nguồn và phạm vi và người dùng đổi; chỉ có giám sát + quản trị giữ sự đáng tin (§10.50)

## 10.57 Hồ sơ Thí nghiệm Bị hoãn (Experiment Backlog)

Những thí nghiệm này được HOÃN đến book v0.1 (xem docs/LAB_BACKLOG.md), không chặn chấp
nhận chương:

- EXP-10-1: Freshness metric trên tập claim RATE_OF_CHANGE
- EXP-10-2: Staleness detection trên sự thay thế E88 → E90
- EXP-10-3: Monitoring loop với synthetic logs
- EXP-10-4: Contradiction queue tracking (C471/C210)
- EXP-10-5: Mô phỏng cổng quản trị của vòng phản hồi
- EXP-10-6: Lấy mẫu tái xác minh
- EXP-10-7: Phát lại vết kiểm toán cho một câu trả lời QA
- EXP-10-8: Dashboard chất lượng 5 chiều
- EXP-10-9: Sinh báo cáo sức khỏe cho hệ cơ chế

Trạng thái: DEFERRED_UNTIL_BOOK_V0.1

## 10.58 Kiểm toán độ sâu (Chapter Depth Audit)

Với mọi khái niệm chính của chương:

- độ sâu >= 4
- khái niệm kỹ-cơ chế quan trọng mục tiêu 5: vòng giám sát, phát hiện cũ, tươi ≠ đúng,
  an toàn vòng phản hồi, nợ mâu thuẫn, năm chiều chất lượng, tái đánh giá, vết kiểm toán,
  tin cậy có kiểm soát, kiến trúc sống
- mọi khái niệm chính phải có ví dụ làm việc RATE_OF_CHANGE
- không khái niệm nào chỉ tồn tại trong ví dụ hệ thống/web chung chung

## 10.59 Bài kiểm tra năng lực người đọc (Reader Capability Test Q01–Q48)

Yêu cầu: **Q01–Q48 đều = YES**.

| ID | Sau khi đọc Ch1–10 offline, người đọc có thể... | Điểm |
|----|--------------------------------------------------|------|
| Q01 | Giải thích vì sao hệ thống tri thức là tiến trình, không phải ảnh tĩnh | §10.1 |
| Q02 | Nêu sáu luồng thay đổi của hệ tri thức | §10.2 |
| Q03 | Định nghĩa cũ (staleness) và vì sao nó không phải sai | §10.3 |
| Q04 | Giải thích vì sao tươi không phải đúng | §10.5 |
| Q05 | Chọn đúng đồng hồ cho truy vấn "hệ thống từng tin gì" | §10.6 |
| Q06 | Nêu ý nghĩa tự quan sát và nên log gì | §10.7–10.8 |
| Q07 | Trình bày vòng giám sát từng tầng | §10.9 |
| Q08 | Giải thích vì sao cần cửa sổ tổng hợp và nó thay đổi tín hiệu ra sao | §10.10 |
| Q09 | Giải thích vì sao ngưỡng là chính sách, không phải chân lý | §10.11 |
| Q10 | Giải thích vì sao vượt ngưỡng kích hoạt chú ý, không phải phán quyết | §10.12 |
| Q11 | Nêu điều gì làm một cảnh báo kiểm chứng được | §10.13 |
| Q12 | Giải thích vì sao giám sát không phải quản trị | §10.15 |
| Q13 | Nêu vai trò vòng phản hồi trong hệ tri thức | §10.16 |
| Q14 | Giải thích vì sao câu trả lời QA không thể tái vào Sổ cái không qua cổng Ch7 | §10.17 |
| Q15 | Giải thích vì sao user sửa là phản hồi, không phải bằng chứng | §10.19 |
| Q16 | Nêu các thuộc tính an toàn của vòng phản hồi | §10.20 |
| Q17 | Định nghĩa tích lũy mâu thuẫn và nợ mâu thuẫn | §10.21–10.22 |
| Q18 | Nêu khi nào một mâu thuẫn nên leo thang để giải quyết | §10.23 |
| Q19 | Nêu năm chiều chất lượng tri thức | §10.24 |
| Q20 | Giải thích vì sao độ đúng thay đổi theo thời gian | §10.25 |
| Q21 | Đo độ đủ tương đối với một phạm vi ra sao | §10.26 |
| Q22 | Nêu độ tươi của chỉ mục đo cái gì | §10.27 |
| Q23 | Phân biệt nhất quán và không có mâu thuẫn | §10.28 |
| Q24 | Nêu độ đáng tin đo cái gì và vì sao nó không phải đúng | §10.29 |
| Q25 | Giải thích vì sao xu hướng có nhiều thông tin hơn mức | §10.30 |
| Q26 | Giải thích vì sao chất lượng không phải chân lý | §10.31 |
| Q27 | Định nghĩa suy thoái và phát hiện nó ra sao | §10.32 |
| Q28 | Nêu mục nát benchmark | §10.33 |
| Q29 | Định nghĩa sụp đổ phản hồi và phòng ngừa ra sao | §10.34 |
| Q30 | Nêu sụp đổ mô hình và vì sao nó khác cũ | §10.35–10.36 |
| Q31 | Nêu các thao tác bảo trì có quản trị | §10.37 |
| Q32 | Mở rộng tái xác minh ra sao | §10.38 |
| Q33 | Nêu một chuyển trạng thái tái đánh giá trông thế nào | §10.39 |
| Q34 | Giải thích vì sao nghỉ hưu không phải xóa | §10.40 |
| Q35 | Nêu thay thế và vì sao chuỗi thay thế quan trọng | §10.41 |
| Q36 | Nêu điều làm thao tác hàng loạt an toàn | §10.42 |
| Q37 | Nêu vết kiểm toán và nó phải ghi gì | §10.43 |
| Q38 | Nêu tin cậy có kiểm soát | §10.44 |
| Q39 | Giải thích vì sao tin cậy không phải đức tin | §10.45 |
| Q40 | Các hệ con điều phối thành hệ thống sống ra sao | §10.46–10.47 |
| Q41 | Nêu dốc tự động hóa | §10.48 |
| Q42 | Giải thích vì sao tự sửa không phải tự đúng | §10.49 |
| Q43 | Giải thích vì sao hệ thống không bao giờ "xong" | §10.50 |
| Q44 | Xây báo cáo sức khỏe cho hệ RATE_OF_CHANGE | §10.52 |
| Q45 | Xử lý sự thay thế E88 → E90 từ đầu đến cuối | §10.53 |
| Q46 | Ngăn vòng phản hồi làm hệ thống sụp đổ | §10.54 |
| Q47 | Nêu những gì còn mở cho Afterword | §10.51 |
| Q48 | Trình bày bậc năng lực toàn cuốn sau 10 chương | §10.60 |

**Q01–Q48: ALL = YES.**

## 10.60 Bậc năng lực cuối chương

TRƯỚC CH10
----------

Hệ thống tri thức biết: biểu diễn, suy luận, quản trị, thu nhận, học, truy xuất, trả lời.

NĂNG LỰC MỚI
------------

Hệ thống vận hành chính nó như một thực thể sống: được đo, được bảo trì, được quản trị,
được kiểm toán.

TRÌNH DIỄN RATE_OF_CHANGE
-------------------------

Hệ thống:

- C471 (Accepted) và C210 (Contested) được theo dõi trong hàng đợi mâu thuẫn
- Sự thay thế E88 → E90 được giám sát nguồn phát hiện
- tái xác minh và tái đánh giá C471 có quản trị
- index được đồng bộ lại, tỷ lệ kiêng trả lời được đo lại
- vết kiểm toán ghi mọi chuyển trạng thái
- báo cáo sức khỏe cho thấy các chiều chất lượng theo thời gian

VẪN CHƯA GIẢI
-------------

Quyền hạn, giám sát con người ở quy mô, chi phí, quản trị đa agent, và xử lý paradigm
shift vẫn mở.

→ Afterword đóng cuốn sách với những câu hỏi mở này.

## 10.61 Tóm tắt chương

Chương 10 biến hệ thống tri thức tĩnh thành **hệ thống tri thức sống**: tự quan sát, đo
chất lượng theo năm chiều, phát hiện cũ và suy thoái qua vòng giám sát (thu thập → tổng
hợp → ngưỡng → cảnh báo → đánh giá → hành động → đo lại), đóng vòng phản hữu an toàn (QA
→ ứng viên → cổng Ch7), quản lý nợ tri thức và mâu thuẫn, thực hiện các thao tác bảo trì
có quản trị, giữ vết kiểm toán để có tin cậy có kiểm soát. Hệ thống không bao giờ "xong"
— nó đáng tin vì nó đo được, bảo trì được, và kiểm toán được trong khi chạy. Vấn đề mở
(quyền hạn, giám sát con người, chi phí, đa hệ thống, paradigm shift) được bàn giao cho
Afterword.

## 10.62 Thông tin thêm và tài liệu tham khảo

Chương 10 dựa trên các nguồn đã đăng ký và kiểm chứng:

- Chất lượng tri thức: `[@zaveri-kgquality-2016]`, `[@iso-25012-2008]`
- Tinh chỉnh/chất lượng KG: `[@paulheim-refinement-2017]`
- Tiến hóa/phiên bản bản thể luận: `[@noy-ontology-evolution-2004]`, `[@klein-ontology-versioning-2001]`
- Duy trì KB, học không ngừng: `[@dong-knowledge-vault-2014]`, `[@mitchell-neverending-2018]`
- Concept drift: `[@gama-drift-2014]`, `[@widmer-drift-1996]`
- Nợ kỹ thuật ML, dữ liệu: `[@sculley-debt-2015]`, `[@sambasivan-cascades-2021]`
- Mục nát benchmark: `[@recht-imagenet-2019]`
- Sụp đổ mô hình: `[@shumailov-collapse-2024]`
- KG thời gian: `[@cai-tkgc-2023]`
- Quản trị dữ liệu: `[@iso-8000-2022]`

Thuộc tính tri thức luận (freshness vs correctness, monitoring vs governance, etc.) do
chương tự định nghĩa dựa trên chuỗi khái niệm Ch1–9; các nguồn học thuật được dùng làm
bằng chứng, không phải "chuẩn" được sao chép.

## Thuật ngữ đã gặp trong chương này

| Tiếng Anh | Tiếng Việt |
|-----------|------------|
| Living Knowledge System | Hệ thống Tri thức Sống |
| System State | Trạng thái hệ thống |
| Staleness | Cũ / ứ đọng |
| Freshness | Độ tươi |
| Monitoring Loop | Vòng giám sát |
| Aggregation Window | Cửa sổ tổng hợp |
| Threshold | Ngưỡng |
| Alert | Cảnh báo |
| Assessment | Đánh giá |
| Feedback Loop | Vòng phản hồi |
| Candidate Claim | Claim ứng viên |
| User Correction | Sửa của người dùng |
| Contradiction Queue | Hàng đợi mâu thuẫn |
| Knowledge Debt | Nợ tri thức |
| Contradiction Debt | Nợ mâu thuẫn |
| Escalation Policy | Chính sách leo thang |
| Quality Dimension | Chiều chất lượng |
| Degradation | Suy thoái |
| Benchmark Decay | Mục nát benchmark |
| Feedback Collapse | Sụp đổ phản hồi |
| Model Collapse | Sụp đổ mô hình |
| Re-validation | Tái xác minh |
| Re-assessment | Tái đánh giá |
| Retirement | Nghỉ hưu |
| Supersession | Thay thế |
| Batch Governance | Quản trị hàng loạt |
| Audit Trail | Vết kiểm toán |
| Controlled Trust | Tin cậy có kiểm soát |
| Automation Gradient | Dốc tự động hóa |
| Living Architecture | Kiến trúc sống |
| Orchestration | Điều phối |

## Tài liệu tham khảo