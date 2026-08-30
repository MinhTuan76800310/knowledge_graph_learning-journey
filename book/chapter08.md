# Chương 8 — Tri thức Quy nạp và Học từ Đồ thị

> **Định hướng chương**
>
> **Câu hỏi trung tâm:** Cho trước nhiều thực thể, quan hệ, phát biểu, ứng dụng cơ chế,
> cấu trúc đồ thị và các ví dụ mang bằng chứng — làm sao hệ thống có thể **sinh GIẢ
> THUYẾT MỚI** từ các quy luật trong đồ thị mà không nhầm lẫn dự đoán thống kê với suy
> dẫn logic hay chân lý?
>
> **Vì sao quan trọng:** Bảy chương trước xây dựng đồ thị (Ch1–2), định danh (Ch3), ngữ
> nghĩa (Ch4), suy diễn (Ch5), tri thức luận (Ch6), và thu nhận/tích hợp (Ch7). Toàn bộ
> đều thao tác trên tri thức *đã được khẳng định*. Nhưng tri thức mới — vượt ra ngoài
> những gì nguồn nói — đến từ đâu? Làm sao từ ba ứng dụng của `RATE_OF_CHANGE` (vận tốc,
> dòng điện, lạm phát) mà hệ thống có thể đề xuất "có lẽ cả ba đều cùng một cơ chế trừu
> tượng"? Làm sao phân biệt một quy luật thực sự với tương quan ngẫu nhiên? Chương 8 mở
> ra nấc *học quy nạp* (inductive learning): nơi đồ thị đã tích hợp trở thành dữ liệu
> huấn luyện cho các mô hình sinh tri thức ứng viên.
>
> **Bạn sẽ hiểu:**
>
> - Ranh giới dứt khoát giữa **suy diễn** (deduction), **quy nạp** (induction),
>   **giả định** (abduction), và **dự đoán** (prediction) — dự đoán ≠ suy dẫn
> - Tri thức tượng trưng (symbolic) khác tri thức thống kê (statistical); học biểu diễn
>   (representation learning) và nhúng đồ thị tri thức (KGE)
> - TransE, DistMult, ComplEx — ba họ chấm điểm với các thiên kiến quy nạp khác nhau
> - Giả định thế giới mở (OWA) và lấy mẫu âm: thiếu ≠ sai
> - Dự đoán liên kết (link prediction) và đánh giá: MRR, Hits@K, filtered evaluation
> - Học chuyển dẫn (transductive) vs học quy nạp trên đồ thị (inductive KG learning)
> - Truyền thông điệp (message passing), GNN, R-GCN, oversmoothing
> - Biểu diễn nút vs biểu diễn đồ thị con; tương tự cấu trúc và độ tương tự cosine
> - Sinh giả thuyết cơ chế ứng viên (CandidateMechanismHypothesis) từ quy luật đồ thị
> - Học quy tắc (rule induction) với AMIE+; xung đột thuật ngữ "confidence" với Ch6
> - Kiến trúc lai (hybrid pipeline): ML sinh ứng viên → tượng trưng lọc → tri thức luận
>   gắn bằng chứng → quản trị quyết định
> - Tổng quát hóa chéo miền, tương quan giả, âm tính khó, calibration
> - Provenance mô hình, vòng phản hồi tự củng cố, model collapse
> - Khi nào KHÔNG dùng graph ML — quyết định dựa trên năng lực hệ thống
> - Ranh giới cuối cùng: học máy không đảm bảo điều gì
>
> **Tiên quyết:**
> - Chương 1–2 (đồ thị, node, cạnh, kiểu)
> - Chương 3 (định danh — entity ≠ embedding)
> - Chương 4 (ngữ nghĩa, OWA, closed-world)
> - Chương 5 (suy diễn, quy tắc, SHACL)
> - Chương 6 (epistemic model, Claim, Claim Ledger, Evidence, Assessment, provenance)
> - Chương 7 (thu nhận nguồn, cấu trúc hóa RATE_OF_CHANGE, CandidateMechanismHypothesis §7.36)
>
> **Bản đồ khái niệm:**
>
> Suy diễn/Quy nạp/Giả định/Dự đoán → Tri thức tượng trưng vs Thống kê → Học biểu diễn
> → KGE (TransE, DistMult, ComplEx) → OWA + Lấy mẫu âm → Link prediction + Đánh giá →
> Chia tách & Rò rỉ → Học chuyển dẫn vs Quy nạp trên đồ thị → GNN (Message passing,
> R-GCN, Oversmoothing) → Biểu diễn đồ thị con → Tương tự cấu trúc → Sinh giả thuyết
> cơ chế → Học quy tắc → Kiến trúc lai → Tổng quát hóa chéo miền → Calibration →
> Provenance & Vòng phản hồi → Quyết định dùng/k dùng ML → Học máy không đảm bảo
>
> **Chuỗi phân biệt trung tâm** (xuyên suốt chương, được nhắc lại nhiều lần):
> tương tự ≠ đồng nhất; dự đoán ≠ suy dẫn; điểm cao ≠ chân lý; mẫu học được ≠ tri thức
> được chấp nhận.

## 8.0 Mở đầu: Ba ứng dụng của một cơ chế

Chương 7 kết thúc bằng một câu hỏi mở: ba nguồn (Giải tích A, Cơ học B, Điện tử C) đều
mô tả "tốc độ thay đổi theo thời gian". Sau pipeline, nguồn A và B cùng củng cố
`ex:claim_vroc` trong sổ cái; nguồn C đi vào hàng đợi chờ xem xét. Nhưng một chi tiết
tinh tế hiện ra ở §7.36: "sự giống nhau về cấu trúc giữa hai ứng dụng (vận tốc và dòng qua
tụ) là một **gợi ý** — nó có thể dẫn tới một giả thuyết ứng viên về một cơ chế trừu tượng
chung, nhưng việc xác lập sự đồng nhất trừu tượng đó thuộc về học quy nạp (Chương 8),
không phải kết luận của chương này."

Chương 8 là chương đó.

Hãy nhìn ba ứng dụng sau dưới góc nhìn của một hệ thống học từ đồ thị:

```
Ứng dụng A (Vận tốc):
  quantity: Position
  operation: DerivativeOperation
  differentiand: Position
  withRespectTo: Time
  result: Velocity

Ứng dụng B (Dòng điện qua tụ):
  quantity: Charge
  operation: DerivativeOperation
  differentiand: Charge
  withRespectTo: Time
  result: Current

Ứng dụng C (Lạm phát / Tăng trưởng dân số):
  quantity: Population
  operation: DerivativeOperation
  differentiand: Population
  withRespectTo: Time
  result: GrowthRate
```

Cả ba đều có cấu trúc giống hệt nhau: một đại lượng đầu ra bằng đạo hàm của một đại lượng
đầu vào theo thời gian. Nhưng liệu đây có phải là **cùng một cơ chế** không? Câu trả lời
phụ thuộc vào mức độ trừu tượng: ở mức độ "đạo hàm đại lượng theo thời gian", cả ba đều
là `RATE_OF_CHANGE`. Nhưng ở mức độ chi tiết: vận tốc là đạo hàm vị trí, dòng là đạo hàm
điện tích, tăng trưởng là đạo hàm dân số — chúng khác nhau về miền và ý nghĩa vật lý.

Chương 8 không trả lời câu hỏi đó bằng một khẳng định. Nó xây dựng **công cụ để hệ thống
tự đề xuất câu trả lời**: học biểu diễn, so sánh cấu trúc, sinh giả thuyết, đánh giá và
quyết định. Và quan trọng nhất — nó xây dựng ranh giới để hệ thống **không bao giờ nhầm
dự đoán với chân lý**.

> ⚠️ **Quy nạp không phải suy diễn.**
> Đây là cảnh báo quan trọng nhất của chương. Khi một mô hình học từ đồ thị "dự đoán"
> rằng `Velocity rateOfChangeOf Position` và `Current rateOfChangeOf Charge` có cùng cấu
> trúc, đó là một **giả thuyết thống kê**, không phải một suy dẫn logic. Hệ thống không
> được phép đối xử với nó như một hệ quả tất yếu của đồ thị (Ch5). Mọi output của học quy
> nạp đều là tri thức ứng viên và phải đi qua quản trị (Ch6) trước khi vào sổ cái.

> 🖊 **Tự kiểm tra 1:** Trước khi đọc tiếp, hãy ghi lại câu trả lời của bạn: ba ứng dụng
> trên (vận tốc, dòng, tăng trưởng) có nên được xem là "cùng một cơ chế" không? Lý do của
> bạn dựa trên điều gì — cấu trúc đồ thị, ý nghĩa vật lý, hay cả hai? Sau §8.19 bạn sẽ
> so sánh với cách hệ thống xử lý.

## 8.1 Suy diễn, Quy nạp, Giả định, và Dự đoán

Trước khi xây dựng bất kỳ mô hình nào, chương phải làm rõ bốn phạm trù suy luận — vì
nhầm lẫn giữa chúng là nguồn gốc của những sai lầm nguy hiểm nhất trong hệ thống tri thức.

### 8.1.1 Suy diễn (Deduction)

Suy diễn là phạm trù đã được xây dựng ở Chương 4–5: từ quy tắc chung và tiền đề cụ thể,
hệ quả được suy ra một cách tất yếu. Nếu quy tắc đúng và tiền đề đúng thì kết luận đúng.
Ví dụ:

- Nếu mọi ứng dụng `RateOfChangeApplication` đều có `operation DerivativeOperation` và
  `withRespectTo Time`, và `ex:velocity_1` được khai báo là `RateOfChangeApplication`,
  thì suy diễn cho phép kết luận `ex:velocity_1 operation DerivativeOperation`.

Suy diễn bảo toàn chân lý. Nó là xương sống của suy luận tự động trên đồ thị tri thức
(Ch5). Nhưng nó không sinh ra tri thức mới — nó chỉ làm tường minh những gì đã ngầm chứa
trong các tiền đề.

### 8.1.2 Quy nạp (Induction)

Quy nạp tổng quát hóa từ các quan sát. Nó là phạm trù chính của chương này. Theo Hogan
và đồng tác giả, tri thức quy nạp "liên quan đến việc tổng quát hóa các mẫu từ một tập
quan sát đầu vào cho trước" và sinh ra "các dự đoán mới nhưng có thể không chính xác"
được gán mức độ tin cậy [@hogan-inductive].

- Ví dụ: từ ba ứng dụng (vận tốc, dòng, tăng trưởng) có cùng cấu trúc, hệ thống đề xuất
  "có lẽ cả ba đều là RateOfChangeApplication". Đây là quy nạp — không tất yếu, có thể
  sai, nhưng hữu ích.

Tri thức quy nạp trong đồ thị tri thức bao gồm **cả mô hình được dùng để mã hóa mẫu lẫn
các dự đoán do mô hình đó sinh ra** [@hogan-inductive]. Nói cách khác, cả bản thân mô
hình nhúng (embedding model) lẫn các bộ ba ứng viên mà nó đề xuất đều thuộc về quy nạp.

> ⚠️ **Quy nạp không phải "suy diễn với nhiều dữ liệu hơn".**
> Một số trình bày ngây thơ coi quy nạp như "suy diễn xác suất" — nhưng đây là sai lầm
> nghiêm trọng. Suy diễn có quy tắc ngữ nghĩa tường minh; quy nạp có mô hình thống kê.
> Suy diễn bảo toàn chân lý; quy nạp sinh ra giả thuyết có thể sai. Gộp hai phạm trù làm
> một là cách nhanh nhất để làm hỏng tầng tri thức luận (Ch6).

### 8.1.3 Giả định (Abduction)

Giả định chọn giả thuyết giải thích tốt nhất cho một quan sát. Nó khác quy nạp ở chỗ:
quy nạp khái quát hóa từ nhiều ví dụ để tìm mẫu chung, còn giả định chọn lời giải thích
cho một quan sát cụ thể. Chương này không xây dựng giả định như một cơ chế chính, nhưng
phân biệt nó với quy nạp để tránh nhầm lẫn thuật ngữ.

### 8.1.4 Dự đoán (Prediction)

Dự đoán là đầu ra của một mô hình học: nó gán một điểm số (score) cho một cấu trúc khả
dĩ — ví dụ, một bộ ba (h, r, t) chưa từng xuất hiện trong đồ thị huấn luyện. Dự đoán có
thể được xếp hạng, so sánh, đánh giá — nhưng nó **không phải là một suy dẫn** (entailment).

> ⚠️ **Dự đoán ≠ suy dẫn.**
> Bộ ba `(ex:velocity_1, rateOfChangeOf, ex:position_1)` có điểm số cao từ mô hình KGE
> không có nghĩa là nó được suy dẫn từ đồ thị. Nó chỉ có nghĩa là mô hình "thấy" nó
> hợp lý dựa trên các mẫu đã học. Đây là sự khác biệt nền tảng: suy dẫn là quan hệ logic,
> dự đoán là ước lượng thống kê.

Bảng tóm tắt bốn phạm trù:

![Bốn phạm trù suy luận: suy diễn (tất yếu), quy nạp (tổng quát hóa, có thể sai), giả định (giải thích tốt nhất), dự đoán (điểm số mô hình).](figures/generated/ch08-reasoning-modes.pdf)

| Phạm trù | Đầu vào | Đầu ra | Bảo toàn chân lý? | Ví dụ |
|----------|---------|--------|-------------------|-------|
| Suy diễn | Quy tắc + tiền đề | Hệ quả tất yếu | Có | R(A) → B |
| Quy nạp | Các quan sát | Mẫu tổng quát / giả thuyết | Không | A₁..Aₙ có cấu trúc S → "có lẽ mọi A đều có cấu trúc S" |
| Giả định | Quan sát + tri thức nền | Giải thích tốt nhất | Không | "Tại sao vận tốc thay đổi?" → "Có lực tác dụng" |
| Dự đoán | Mô hình + đầu vào | Điểm số / xếp hạng | Không | f(h,r,t) = 0.92 |

## 8.2 Tri thức Tượng trưng và Tri thức Thống kê

Một phân biệt quan trọng nữa cần đặt ra trước khi xây dựng mô hình học.

**Tri thức tượng trưng (symbolic knowledge)** là những cấu trúc tường minh, có thể đọc
và kiểm tra được: bộ ba RDF, tiên đề ontology, quy tắc suy diễn, ràng buộc SHACL. Ý
nghĩa của chúng được xác định bởi ngữ nghĩa hình thức (Ch4–5). Toàn bộ đồ thị tri thức
tính đến Chương 7 là tri thức tượng trưng.

**Tri thức thống kê (statistical knowledge)** là những biểu diễn học được từ dữ liệu:
vector nhúng, trọng số mô hình, điểm số, phân cụm. Nó không có ngữ nghĩa hình thức —
một vector không phải là một phát biểu, và một điểm số không phải là một chân trị.

> ⚠️ **Vector không phải là phát biểu.**
> Một embedding của `RateOfChangeMechanism` là một dãy số thực. Dãy số đó không khẳng
> định điều gì. Nó không thể được dùng làm tiền đề cho suy diễn (Ch5), không thể được
> ghi vào sổ cái (Ch6), và không thể được viện dẫn làm bằng chứng (Ch6 §6.5). Nó chỉ
> là một biểu diễn tính toán phục vụ dự đoán.

Chương 8 xây dựng cầu nối giữa hai thế giới này: tri thức thống kê sinh ra các giả thuyết
ứng viên — và các giả thuyết đó, sau khi được đánh giá và quản trị, có thể trở thành tri
thức tượng trưng. Nhưng bản thân quá trình học không tạo ra tri thức tượng trưng trực tiếp.

## 8.3 Phân loại bài toán "Học từ Đồ thị"

Trước khi đi vào kỹ thuật, cần một bức tranh toàn cảnh về các dạng bài toán học từ đồ thị
tri thức. Nickel và đồng tác giả phân loại thành hai họ lớn [@nickel-relational-ml-2016]:

1. **Mô hình đặc trưng tiềm ẩn (latent feature models):** học biểu diễn số (embedding) cho
   thực thể và quan hệ, dùng hàm chấm điểm để dự đoán bộ ba mới. Đây là trọng tâm của
   §8.4–8.20.
2. **Khai phá mẫu quan sát được (observable pattern mining):** học quy tắc tượng trưng từ
   đồ thị, như AMIE+ (§8.22). Đây là cầu nối với tri thức tượng trưng.

Trong khuôn khổ cuốn sách, chúng ta thêm một họ thứ ba mang tính kiến trúc:

3. **Kiến trúc lai (hybrid pipeline):** kết hợp cả hai họ trên với tầng tri thức luận
   (Ch6) và quản trị (Ch7) để tạo thành một hệ thống học quy nạp có kỷ luật (§8.24).

Mỗi họ có điểm mạnh và điểm yếu riêng, và chúng bổ sung cho nhau hơn là cạnh tranh.

## 8.4 Đặc trưng, Học biểu diễn, và Nhúng

### 8.4.1 Từ đặc trưng thủ công đến biểu diễn học được

Trước kỷ nguyên học sâu, mọi mô hình học trên đồ thị đều dùng **đặc trưng thiết kế thủ
công** (hand-engineered features): số lượng neighbor, kiểu quan hệ, bậc của node, độ dài
đường đi ngắn nhất, v.v. Cách làm này có ưu điểm là dễ giải thích nhưng giới hạn ở chỗ
không thể mở rộng: mỗi bài toán mới cần một bộ đặc trưng mới, và đặc trưng không học được
từ dữ liệu [@hamilton-grl-2020].

**Học biểu diễn (representation learning)** thay thế thiết kế thủ công bằng việc học
vector từ dữ liệu. Mỗi thực thể và mỗi quan hệ được ánh xạ vào một không gian vector
d-chiều, sao cho các quy luật cấu trúc của đồ thị được phản ánh trong hình học của không
gian đó.

### 8.4.2 Entity ≠ Embedding(Entity)

Đây là một nguyên tắc nền tảng cần được khắc ghi:

> ⚠️ **Entity ≠ Embedding(Entity).**
> Thực thể "vận tốc" (một khái niệm vật lý có định nghĩa, công thức, ý nghĩa) không đồng
> nhất với vector nhúng của nó (một dãy 100 số thực). Embedding là một biểu diễn tính
> toán phục vụ dự đoán, không phải là bản chất của thực thể. Mọi suy luận từ embedding
> đều là suy luận trên biểu diễn, không phải trên thực thể. Nguyên tắc này kết nối trực
> tiếp với Chương 3: định danh là một quan hệ ngữ nghĩa, không phải một quan hệ hình học.

## 8.5 Nhúng Đồ thị Tri thức (KGE) và TransE

### 8.5.1 Bài toán KGE

Cho một đồ thị tri thức G = (E, R, T) với E là tập thực thể, R là tập quan hệ, T là tập
bộ ba quan sát được (h, r, t). Mô hình **nhúng đồ thị tri thức (KGE)** học:
- Một ánh xạ ε: E → $\mathbb{R}^d$ (vector thực thể)
- Một ánh xạ ρ: R → $\mathbb{R}^d$ hoặc $\mathbb{R}^{d \times d}$ (vector hoặc ma trận quan hệ)
- Một **hàm chấm điểm** f: E × R × E → $\mathbb{R}$ gán một giá trị thực cho mỗi bộ ba

Giá trị của f(h, r, t) càng cao (hoặc càng thấp, tùy quy ước) thì bộ ba càng hợp lý.
Mục tiêu huấn luyện: tối đa hóa điểm của các bộ ba quan sát được và tối thiểu hóa điểm
của các bộ ba nhiễu (negative samples) [@hogan-inductive].

### 8.5.2 TransE: h + r ≈ t

TransE là mô hình KGE nền tảng, được đề xuất bởi Bordes và đồng tác giả
[@bordes-transe-2013]. Ý tưởng rất đơn giản: nếu bộ ba (h, r, t) đúng, thì vector của
h **cộng** với vector của r xấp xỉ bằng vector của t.

```
h + r ≈ t   →   f(h, r, t) = −‖h + r − t‖
```

(Ở đây f là điểm số; giá trị càng cao (âm càng nhỏ) là bộ ba càng hợp lý.)

Ví dụ: nếu `Velocity` = ε(vận tốc), `rateOfChangeOf` = ρ(rateOfChangeOf), và
`Position` = ε(vị trí), thì mô hình kỳ vọng:

```
Velocity + rateOfChangeOf ≈ Position
```

tức là "vận tốc là rate of change của vị trí".

Hình học của TransE là trực quan: mỗi quan hệ là một phép tịnh tiến trong không gian
vector. Nếu bạn biết vị trí của `Velocity` và `rateOfChangeOf`, bạn có thể "dịch chuyển"
đến vị trí của `Position`.

```
  Position ─────────────────────► Velocity
       ↑                           │
       └─────── rateOfChangeOf ─────┘
       (h + r ≈ t)
```

![Hình học TransE: quan hệ là phép tịnh tiến trong không gian vector, h + r ≈ t, và bộ ba nhiễu bị đẩy ra xa bằng hàm mất mát biên.](figures/generated/ch08-transe-geometry.pdf)

> ⚠️ **h + r ≈ t không phải là một suy dẫn logic.**
> Phương trình h + r ≈ t là một xấp xỉ số học, không phải một quy tắc suy diễn. Nó không
> có ngữ nghĩa hình thức. Việc `Velocity + rateOfChangeOf ≈ Position` trong không gian
> embedding không có nghĩa là "vận tốc là rate of change của vị trí" là một chân lý logic
> — nó chỉ là một mẫu thống kê được học từ dữ liệu. Chỉ khi giả thuyết đó đi qua quản trị
> (Ch6) và được chấp nhận, nó mới trở thành một phát biểu có giá trị.

TransE có một hạn chế nổi tiếng: nó xử lý kém các quan hệ 1–N, N–1, và N–N, cũng như
các quan hệ đối xứng. Ví dụ, nếu một thực thể có nhiều quan hệ cùng loại với nhiều thực
thể khác (như `Student` học nhiều `Course`), TransE không thể đặt tất cả các course
quanh student với cùng một phép tịnh tiến.

## 8.6 DistMult, ComplEx, và Thiên kiến Quy nạp

### 8.6.1 DistMult: Chấm điểm song tuyến tính

DistMult (Yang và đồng tác giả, 2015) thuộc họ mô hình **bilinear** (song tuyến tính):
thay vì cộng vector, nó nhân từng phần tử (element-wise) rồi cộng tổng
[@yang-distmult-2015]:

```
f(h, r, t) = ⟨h, r, t⟩ = Σ_i h_i · r_i · t_i
```

trong đó h, r, t là các vector thực d-chiều, và phép nhân từng phần tử cho phép mỗi chiều
của không gian đóng góp độc lập vào điểm số.

Hạn chế: DistMult là **đối xứng** — f(h, r, t) = f(t, r, h). Điều này có nghĩa là nó
không thể phân biệt `(Velocity, rateOfChangeOf, Position)` với `(Position, rateOfChangeOf,
Velocity)`, tức là không thể mô hình hóa các quan hệ bất đối xứng.

### 8.6.2 ComplEx: Nhúng phức

ComplEx (Trouillon và đồng tác giả, 2016) mở rộng DistMult bằng cách dùng số phức thay
vì số thực [@trouillon-complex-2016]. Embedding của mỗi thực thể và quan hệ là một số
phức, và hàm chấm điểm là tích Hermitian:

```
f(h, r, t) = Re(⟨h, r, t̄⟩) = Re(Σ_i h_i · r_i · conj(t_i))
```

Số phức cho phép mô hình hóa cả quan hệ đối xứng và bất đối xứng trong cùng một khuôn
khổ, vì phần thực của tích Hermitian không đối xứng — nó thay đổi khi đổi vai trò h và t.

ComplEx là một cải tiến trực tiếp so với DistMult: nó giữ độ phức tạp tính toán tuyến
tính nhưng xử lý được cả hai loại quan hệ.

### 8.6.3 Thiên kiến Quy nạp (Inductive Bias)

Mỗi họ mô hình KGE có một **thiên kiến quy nạp** (inductive bias) khác nhau — tức là
các giả định cấu trúc về mẫu nào đáng học [@hamilton-grl-2020]:

| Mô hình | Không gian | Thiên kiến | Mạnh về | Yếu về |
|---------|-----------|------------|---------|--------|
| TransE | $\mathbb{R}^d$ | h + r ≈ t (tịnh tiến) | Quan hệ 1–1 | Quan hệ 1–N, N–1, đối xứng |
| DistMult | $\mathbb{R}^d$ | ⟨h, r, t⟩ (bilinear đối xứng) | Quan hệ đối xứng | Quan hệ bất đối xứng |
| ComplEx | $\mathbb{C}^d$ | Re(⟨h, r, t̄⟩) (Hermitian) | Cả hai loại | Không có nhược điểm cơ bản, nhưng vẫn giả định mỗi quan hệ có một biến đổi tuyến tính |

> ⚠️ **Không có mô hình nào "hiểu" ngữ nghĩa.**
> Cả ba mô hình trên đều là các hàm chấm điểm với các thiên kiến hình học khác nhau.
> Không mô hình nào trong số chúng "hiểu" rằng "rate of change" là một khái niệm vi phân
> hay rằng vận tốc và dòng điện là các hiện tượng vật lý khác nhau. Chúng chỉ học các
> tương quan số học từ dữ liệu. Đây là lý do vì sao điểm số KGE không bao giờ được dùng
> làm bằng chứng tri thức luận (Ch6) mà không có Assessment.

## 8.7 Giả định Thế giới Mở (OWA) và Lấy mẫu Âm

### 8.7.1 OWA: Thiếu ≠ Sai

Đồ thị tri thức không bao giờ hoàn chỉnh. Nếu bộ ba `(ex:velocity_1, hasValue, 10)`
không có trong đồ thị, điều đó không có nghĩa là vận tốc không bằng 10 — nó chỉ có nghĩa
là thông tin đó chưa được thu nhận. Đây là **giả định thế giới mở (open-world assumption,
OWA)** đã được giới thiệu ở Chương 4.

OWA đặt ra một thách thức lớn cho học quy nạp: làm sao tạo ra các ví dụ "âm" (negative
examples) để huấn luyện nếu chúng ta không biết bộ ba nào là sai?

### 8.7.2 Lấy mẫu Âm (Negative Sampling)

Giải pháp tiêu chuẩn là **lấy mẫu âm** (negative sampling) [@mikolov-negativesampling-2013]:
từ một bộ ba đúng (h, r, t), tạo bộ ba nhiễu bằng cách thay thế h hoặc t bằng một thực
thể ngẫu nhiên:

```
Bộ ba đúng:  (Velocity, rateOfChangeOf, Position)
Bộ ba âm:    (Velocity, rateOfChangeOf, Mass)      ← thay Position bằng Mass
              (Acceleration, rateOfChangeOf, Position) ← thay Velocity bằng Acceleration
```

Mô hình được huấn luyện để phân biệt bộ ba đúng (điểm cao) và bộ ba âm (điểm thấp).
Đây là một thủ thuật huấn luyện, không phải một khẳng định về chân trị.

![Lấy mẫu âm dưới giả định thế giới mở: bộ ba đúng được sinh mẫu âm bằng cách thay thế đầu/cuối; mẫu âm là giả định huấn luyện, không phải khẳng định "sai" — và có thể là âm tính giả.](figures/generated/ch08-negative-sampling.pdf)

> ⚠️ **Mẫu âm ≠ bộ ba sai.**
> Bộ ba `(Velocity, rateOfChangeOf, Mass)` được dùng làm mẫu âm trong huấn luyện, nhưng
> điều này không có nghĩa là "vận tốc không phải rate of change của khối lượng". Nó chỉ
> có nghĩa là bộ ba đó được chọn ngẫu nhiên để làm nhiễu. Trong một đồ thị đầy đủ hơn,
> có thể có một quan hệ nào đó giữa vận tốc và khối lượng (ví dụ, động lượng). Lấy mẫu
> âm là một giả định kỹ thuật, không phải một tuyên bố về thế giới.

### 8.7.3 Âm tính Giả (False Negative)

Vì đồ thị không hoàn chỉnh (OWA), một bộ ba được sinh ra làm mẫu âm có thể **thực ra là
đúng** nhưng chưa được ghi nhận. Đây gọi là **âm tính giả** (false negative). Ví dụ: nếu
đồ thị chưa có `(Velocity, measuredIn, metersPerSecond)`, thì mẫu âm
`(Velocity, measuredIn, metersPerSecond)` được sinh ra từ phép thay thế ngẫu nhiên sẽ là
một âm tính giả — nó dạy mô hình rằng một bộ ba đúng là sai.

Âm tính giả làm méo ranh giới học được. Càng nhiều âm tính giả, mô hình càng "học" rằng
các bộ ba đúng là bất hợp lý, làm giảm chất lượng dự đoán. Đây là một hệ quả trực tiếp
của OWA: không có cách nào tránh hoàn toàn âm tính giả, nhưng có thể giảm thiểu bằng
cách chọn thực thể thay thế thông minh hơn (ví dụ, chỉ thay bằng thực thể cùng kiểu).

## 8.8 Dự đoán Liên kết (Link Prediction)

Dự đoán liên kết là bài toán ứng dụng chính của KGE: cho một đồ thị quan sát được một
phần, dự đoán các bộ ba còn thiếu [@nickel-relational-ml-2016]. Cụ thể:

- **Cho trước:** (h, r, ?) — tìm t phù hợp nhất
- **Cho trước:** (?, r, t) — tìm h phù hợp nhất
- **Cho trước:** (h, ?, t) — tìm r phù hợp nhất

Mô hình KGE tính điểm cho tất cả các ứng viên và xếp hạng chúng từ cao nhất đến thấp
nhất. Kết quả là một danh sách có thứ tự các bộ ba ứng viên — không phải các sự thật
được khẳng định.

> ⚠️ **Xếp hạng cao ≠ sự thật.**
> Nếu mô hình xếp hạng `(Velocity, rateOfChangeOf, Position)` ở vị trí số 1, điều đó
> không có nghĩa là bộ ba đó đúng. Nó chỉ có nghĩa là, trong số tất cả các ứng viên,
> bộ ba này có điểm số cao nhất. Việc khẳng định nó là sự thật đòi hỏi bằng chứng độc lập
> (Ch6) và quản trị (Ch7).

> 🖊 **Tự kiểm tra 2:** Cho đồ thị có ba thực thể `Velocity`, `Position`, `Time` và
> quan hệ `rateOfChangeOf`. Mô hình TransE học được các vector sao cho
> `Velocity + rateOfChangeOf ≈ Position`. Nếu bạn thêm thực thể `Acceleration` và huấn
> luyện lại, bạn kỳ vọng `Acceleration + rateOfChangeOf ≈ ?` Giải thích.

## 8.9 Đánh giá Dự đoán Liên kết

### 8.9.1 MRR (Mean Reciprocal Rank)

Với mỗi bộ ba đúng trong tập kiểm, mô hình xếp hạng nó trong số tất cả các ứng viên.
MRR là trung bình của nghịch đảo hạng:

```
MRR = (1/N) · Σ_i (1 / rank_i)
```

MRR = 1.0 có nghĩa là bộ ba đúng luôn được xếp hạng 1. MRR = 0.5 có nghĩa là trung bình
bộ ba đúng ở hạng 2. MRR bị ảnh hưởng nhiều bởi các hạng cao — một bộ ba ở hạng 10 đóng
góp 0.1, trong khi ở hạng 2 đóng góp 0.5.

### 8.9.2 Hits@K

Hits@K là tỉ lệ các bộ ba đúng nằm trong top K ứng viên:

```
Hits@K = (số bộ ba đúng có rank ≤ K) / N
```

Hits@10 = 0.8 có nghĩa là 80% bộ ba đúng nằm trong top 10. Hits@K không phân biệt giữa
hạng 1 và hạng K — cả hai đều được tính là "hit" [@bordes-transe-2013].

### 8.9.3 Đánh giá Thô (Raw) và Đã Lọc (Filtered)

Một vấn đề tinh tế: khi xếp hạng, các bộ ba đúng khác (không phải bộ ba đang kiểm tra)
cũng xuất hiện trong danh sách ứng viên. Nếu chúng được xếp trên bộ ba đang kiểm tra,
chúng bị tính là "sai" mặc dù chúng cũng đúng.

**Đánh giá thô (raw evaluation)** không loại bỏ các bộ ba đúng khác khỏi danh sách xếp
hạng. **Đánh giá đã lọc (filtered evaluation)** loại bỏ tất cả các bộ ba đúng đã biết
khỏi danh sách trước khi xếp hạng, chỉ giữ lại bộ ba đích và các ứng viên thực sự chưa
xuất hiện trong đồ thị [@bordes-transe-2013] [@nickel-relational-ml-2016].

> ⚠️ **Đánh giá đã lọc ≠ đánh giá chân lý.**
> Filtered evaluation chỉ loại bỏ các bộ ba đúng *đã biết*. Nó không biết về các bộ ba
> đúng chưa được ghi nhận (OWA). Vì vậy, filtered evaluation là một cải tiến kỹ thuật,
> không phải một phép đo chân lý tuyệt đối.

## 8.10 Chia Tách Dữ liệu và Rò rỉ

### 8.10.1 Train / Validation / Test

Để đánh giá mô hình, chúng ta chia tập dữ liệu thành ba phần:
- **Train:** dùng để học tham số mô hình
- **Validation:** dùng để chọn siêu tham số (hyperparameters)
- **Test:** dùng để đánh giá cuối cùng, không được nhìn trong quá trình phát triển mô hình

Trên đồ thị tri thức, việc chia tách không đơn giản như chia ngẫu nhiên các bộ ba, vì
các bộ ba có quan hệ với nhau qua thực thể dùng chung.

### 8.10.2 Rò rỉ Dữ liệu (Data Leakage)

Rò rỉ dữ liệu xảy ra khi thông tin từ tập kiểm lọt vào quá trình huấn luyện, làm điểm
số đánh giá trở nên lạc quan một cách giả tạo. Trong đồ thị tri thức, có nhiều kiểu rò rỉ:

- **Rò rỉ trùng lặp (duplicate leakage):** cùng một bộ ba xuất hiện ở cả train và test
- **Rò rỉ quan hệ nghịch đảo (inverse-relation leakage):** nếu train có (h, r, t) và test
  có (t, r⁻¹, h), mô hình có thể "gian lận" bằng cách học inverse relation
- **Rò rỉ đường đi (path leakage):** train có (A, r1, B) và (B, r2, C), test có (A, r3, C)
  — mô hình có thể học r3 = r1 ∘ r2
- **Rò rỉ thực thể (entity leakage):** một thực thể ở test đã xuất hiện ở train, mang
  thông tin về các quan hệ của nó
- **Rò rỉ thời gian (temporal leakage):** train chứa dữ liệu tương lai, test chứa dữ liệu
  quá khứ — mô hình "dự đoán" quá khứ dựa trên tương lai
- **Rò rỉ nguồn (source leakage):** cùng một nguồn (ví dụ, cùng một cuốn sách) xuất hiện
  ở cả train và test, làm quá lạc quan về khả năng tổng quát hóa

> ⚠️ **Không có rò rỉ không chứng minh mô hình hiểu cơ chế.**
> Một mô hình sạch rò rỉ vẫn có thể học các tương quan bề mặt (spurious correlation)
> thay vì cấu trúc cơ chế thực sự. Không rò rỉ chỉ có nghĩa là đánh giá sạch hơn, không
> có nghĩa là mô hình đúng. Vấn đề này sẽ được thảo luận chi tiết ở §8.26.

## 8.11 Học Chuyển dẫn và Học Quy nạp trên Đồ thị

### 8.11.1 Học Chuyển dẫn (Transductive Learning)

Các mô hình KGE ở §8.5–8.6 là **chuyển dẫn** (transductive): chúng học một vector cho
mỗi thực thể đã thấy trong huấn luyện, và chỉ có thể dự đoán liên kết **giữa các thực
thể đã biết**. Nếu một thực thể mới xuất hiện sau khi huấn luyện, mô hình không có vector
cho nó.

Điều này phù hợp với bài toán "hoàn thiện đồ thị": các thực thể đã có trong đồ thị, chỉ
thiếu các liên kết.

### 8.11.2 Học Quy nạp trên Đồ thị (Inductive KG Learning)

Nhưng nếu hệ thống cần dự đoán trên **các thực thể mới chưa từng thấy** — ví dụ, một
chương mới của một cuốn sách vật lý giới thiệu `ElectromotiveForce` chưa từng xuất hiện —
thì mô hình chuyển dẫn không dùng được. Đây là **học quy nạp trên đồ thị** (inductive
KG learning): mô hình phải tổng quát hóa tới các thực thể/subgraph chưa thấy
[@teru-grail-2020].

> ⚠️ **Chuyển dẫn ≠ quy nạp.**
> Một mô hình KGE tiêu chuẩn là chuyển dẫn, không phải quy nạp (theo nghĩa học trên đồ
> thị). Nó không tổng quát hóa tới thực thể mới. Nếu hệ thống cơ chế cần đối mặt với các
> khái niệm mới từ các miền mới (một yêu cầu rất thực tế của cơ chế RATE_OF_CHANGE trong
> các cuốn sách khác nhau), thì cần các phương pháp quy nạp như GNN dựa trên subgraph
> (§8.16–8.17).

## 8.12 Thực thể Ngoài Từ vựng (OOV) và Động lực cho GNN

### 8.12.1 Vấn đề OOV

**Thực thể ngoài từ vựng (out-of-vocabulary entity, OOV)** là thực thể không có vector
học sẵn vì chưa từng xuất hiện trong huấn luyện. Bảng tra cứu (lookup table) embedding
không thể xử lý chúng — nó chỉ có vector cho các thực thể đã thấy.

Làm sao tạo biểu diễn cho một thực thể mới? Ba hướng:
1. Từ **thuộc tính/văn bản** của chính nó (nếu có)
2. Từ **lân cận** của nó — các thực thể và quan hệ xung quanh
3. Từ **cấu trúc subgraph** chứa nó — dùng một mô hình mã hóa không phụ thuộc định danh

Hướng thứ ba dẫn trực tiếp đến GNN dựa trên subgraph: thay vì học vector cho từng thực
thể, mô hình học cách **tính toán** biểu diễn từ cấu trúc lân cận. Một mô hình như vậy
có thể áp dụng cho bất kỳ subgraph nào, kể cả những subgraph có thực thể hoàn toàn mới
[@teru-grail-2020].

## 8.13 Trực giác GNN: Học từ Lân cận

**Mạng nơ-ron đồ thị (Graph Neural Network, GNN)** là họ mô hình có phép tính đi theo
cấu trúc đồ thị: biểu diễn của một nút được tính từ biểu diễn của chính nó và của các
nút lân cận, qua nhiều lớp (layer) [@hamilton-grl-2020].

Trực giác: biểu diễn của nút "Velocity" trong một ứng dụng RATE_OF_CHANGE được tính từ
các nút xung quanh nó — `Position`, `Time`, `DerivativeOperation`, `Quantity` — qua các
quan hệ tương ứng.

```
          Position ──hasQuantity──► Application_A
          Time     ──withRespectTo► Application_A
          DerivativeOperation ──operation──► Application_A
          Application_A ──result──► Velocity
```

Sau một lớp truyền thông điệp, biểu diễn của `Velocity` chứa thông tin về các lân cận
của nó. Sau nhiều lớp, nó chứa thông tin về lân cận xa hơn (multi-hop). Điều này cho
phép GNN bắt được cấu trúc cục bộ xung quanh mỗi nút — chính là thứ mà embedding cố
định không làm được.

![Truyền thông điệp quanh một ứng dụng cơ chế: biểu diễn của nút được tính từ (message) các lân cận qua từng quan hệ, gom lại (aggregate) và cập nhật (update) qua từng lớp.](figures/generated/ch08-message-passing.pdf)

## 8.14 Truyền Thông điệp (Message Passing)

### 8.14.1 Công thức tổng quát

Công thức tổng quát của một lớp GNN là một chuỗi ba bước: **message → aggregate →
update** [@hamilton-grl-2020].

```
Với mỗi nút v và mỗi lớp k:
  1. Message:   m_{u→v} = MESSAGE(h_u^(k), h_v^(k), edge(u,v))
  2. Aggregate: m_v      = AGGREGATE({m_{u→v} | u ∈ N(v)})
  3. Update:    h_v^(k+1) = UPDATE(h_v^(k), m_v)
```

- **MESSAGE** tính một thông điệp từ nút lân cận u đến nút v, có thể phụ thuộc vào loại
  cạnh
- **AGGREGATE** gom tất cả các thông điệp đến v (cộng, trung bình, max, attention, ...)
- **UPDATE** kết hợp biểu diễn hiện tại của v với thông điệp đã gom

Lưu ý quan trọng: đây là một **khung khái niệm**, không phải một thuật toán duy nhất.
Mỗi GNN cụ thể là một thể hiện của khung này với các lựa chọn khác nhau cho ba hàm trên.

> ⚠️ **Một công thức không định nghĩa mọi GNN.**
> Nhiều bài viết trình bày "GNN là công thức X". Sai lầm: GNN là một *họ* mô hình. Sự
> khác biệt giữa các thành viên của họ nằm ở cách chọn MESSAGE, AGGREGATE, UPDATE.
> Đọc một công thức cụ thể và gọi đó là "GNN" là bỏ qua toàn bộ thiết kế.

### 8.14.2 Vì sao truyền thông điệp giúp học cơ chế?

Đối với hệ thống RATE_OF_CHANGE: nếu GNN học được rằng một nút có `operation
DerivativeOperation`, `withRespectTo Time`, và `hasQuantity Q` thường dẫn đến `result` là
một RateOfChangeApplication, thì khi gặp một ứng dụng mới (ví dụ `GrowthRate` của dân số),
GNN có thể **tái sử dụng** mẫu đã học mà không cần biết trước `GrowthRate`.

Đây chính là sức mạnh của học quy nạp trên đồ thị: mô hình học *cách* tính toán biểu
diễn từ cấu trúc, không học *các giá trị* cố định của từng thực thể.

## 8.15 R-GCN: Truyền Thông điệp Theo Loại Quan hệ

**R-GCN (Relational Graph Convolutional Network)** là một GNN thiết kế cho đồ thị
**đa quan hệ** (multi-relational) [@schlichtkrull-rgcn-2018]. Ý tưởng chính: mỗi loại
quan hệ r có một ma trận biến đổi riêng W_r trong bước update.

```
h_v^(k+1) = σ( W_self · h_v^(k)  +  Σ_{r} Σ_{u∈N_r(v)} (1/c_v) · W_r · h_u^(k) )
```

trong đó N_r(v) là các lân cận của v qua quan hệ r, c_v là hằng số chuẩn hóa, và W_r là
biến đổi riêng cho quan hệ r.

Vì sao quan trọng? Trong đồ thị cơ chế, các quan hệ khác nhau mang ý nghĩa rất khác
nhau: `operation` (thao tác), `hasQuantity` (đại lượng), `withRespectTo` (đại lượng tham
chiếu), `result` (kết quả), `derivativeApplication` (áp dụng vi phân). Nếu tất cả các
quan hệ này được gộp vào một phép gom chung (relation-blind aggregation), mô hình mất
khả năng phân biệt vai trò của từng quan hệ — và vai trò này chính là thứ quyết định
cấu trúc cơ chế.

R-GCN thường được dùng như một **encoder** (tính biểu diễn nút từ cấu trúc), ghép với
một **decoder** (như DistMult) để dự đoán liên kết: encoder sinh biểu diễn, decoder chấm
điểm bộ ba.

> ⚠️ **Không được gộp mọi quan hệ thành một phép gom.**
> Nếu bạn gộp `operation`, `withRespectTo`, `result` vào một phép cộng đơn giản, bạn
> vô hiệu hóa khả năng mô hình phân biệt vai trò ngữ nghĩa của từng quan hệ. Trên đồ thị
> tri thức (đa quan hệ), điều này là một sai lầm thiết kế.

## 8.16 Oversmoothing: Càng sâu chưa chắc càng tốt

Một hiện tượng nguy hiểm trong GNN: khi xếp nhiều lớp, biểu diễn của các nút **hội tụ
về nhau** và mất thông tin phân biệt. Đây gọi là **oversmoothing** (làm mịn quá mức).

Li và đồng tác giả chứng minh rằng phép gom trong GCN tương đương với **làm mịn Laplace**
(Laplacian smoothing) trên đồ thị: mỗi lớp gom làm biểu diễn các nút "trộn" với nhau
[@li-oversmoothing-2018]. Khi xếp quá nhiều lớp, mọi nút có biểu diễn gần như giống nhau,
và chất lượng dự đoán giảm mạnh.

```
Lớp 1: biểu diễn phân biệt tốt
Lớp 2–3: vẫn còn phân biệt
Lớp 5–10: hội tụ — mọi nút gần như giống nhau (oversmoothing)
```

> ⚠️ **Càng nhiều lớp GNN không có nghĩa là càng hiểu sâu.**
> Trực giác "xếp nhiều lớp để hiểu sâu hơn" là sai với GNN: vượt quá một số lớp nhất
> định, oversmoothing làm mọi biểu diễn hội tụ về nhau và phá hỏng khả năng phân biệt.
> Số lớp tối ưu thường rất nhỏ (1–3) và phụ thuộc vào bài toán.

## 8.17 Biểu diễn Nút và Biểu diễn Đồ thị con

### 8.17.1 Hai cấp độ biểu diễn

Cho đến nay, chúng ta nói về **biểu diễn nút** (node representation): một vector cho một
nút, chứa thông tin về lân cận của nó. Nhưng hệ thống cơ chế cần so sánh **các ứng dụng
cơ chế** — và một ứng dụng là một cấu trúc gồm nhiều nút (quantity, operation,
differentiand, withRespectTo, result).

Để so sánh hai ứng dụng như hai tổng thể, cần **biểu diễn đồ thị con (subgraph
representation)**: gom biểu diễn của các nút trong subgraph thành một vector duy nhất
bằng một phép **pooling/readout** — ví dụ, trung bình, max, hoặc một lớp học được
[@hamilton-grl-2020].

> ⚠️ **Biểu diễn nút ≠ biểu diễn đồ thị con.**
> Vector của nút `Application_A` không phải là vector của toàn bộ ứng dụng A. Nếu bạn
> so sánh hai ứng dụng bằng vector của nút trung tâm của chúng, bạn bỏ qua toàn bộ cấu
> trúc xung quanh — quantity, operation, withRespectTo — vốn là phần quan trọng nhất
> của cấu trúc cơ chế.

### 8.17.2 Lựa chọn thiết kế, không phải định nghĩa

Pooling là một **lựa chọn thiết kế**: cách bạn chọn hàm gom (mean, max, attention, ...)
quyết định thông tin nào của subgraph được giữ lại. Không có pooling nào "đúng" tuyệt
đối. Quan trọng hơn: vector gom được không phải là "ý nghĩa" của subgraph — nó chỉ là
một tóm tắt số học phục vụ một bài toán cụ thể.

## 8.18 Tương tự Cấu trúc và Độ tương tự Cosine

### 8.18.1 Tương tự Cấu trúc (Structural Similarity)

Khi có biểu diễn đồ thị con, chúng ta có thể đo độ giống nhau giữa hai ứng dụng cơ chế.
**Tương tự cấu trúc** là một đánh giá đa chiều: hai cấu trúc giống nhau khi chúng chia
sẻ các mẫu vai trò — cùng thao tác (operation), cùng khuôn mẫu vai trò (role pattern),
cùng kiểu đối số tương thích, cùng hình dạng hàm, cùng lân cận.

Đây không phải một con số duy nhất: nó là một vector bằng chứng nhiều chiều.

> ⚠️ **Tương tự ≠ đồng nhất.**
> Hai ứng dụng có cấu trúc gần như giống hệt nhau (vận tốc và dòng điện) vẫn là **hai
> thực thể khác nhau**. Tương tự cấu trúc là bằng chứng gợi ý, không phải định danh
> (Ch3: owl:sameAs là một quan hệ ngữ nghĩa, không phải quan hệ hình học).

### 8.18.2 Độ tương tự Cosine

**Độ tương tự cosine** đo cosin của góc giữa hai vector:

```
cos(a, b) = (a·b) / (‖a‖·‖b‖)
```

Giá trị nằm trong [−1, 1]: 1 nghĩa là cùng hướng, 0 nghĩa là trực giao, −1 nghĩa là
ngược hướng.

Ví dụ làm việc: hai vector 3 chiều

```
a = (2, 0, 0),  b = (3, 0, 0)  →  cos = 1     (cùng hướng)
a = (2, 0, 0),  c = (0, 5, 0)  →  cos = 0     (trực giao)
a = (2, 0, 0),  d = (−1, 0, 0) →  cos = −1    (ngược hướng)
```

Cosine cao trong không gian embedding thường đi kèm cấu trúc lân cận giống nhau — nhưng
không bao giờ tự nó chứng minh sự đồng nhất ngữ nghĩa.

> 🖊 **Tự kiểm tra 3:** Tính độ tương tự cosine giữa a = (1, 2, 3) và b = (4, 5, 6).
> (Gợi ý: a·b = 32, ‖a‖ = √14, ‖b‖ = √77.) Kết quả nói lên điều gì về hướng của hai
> vector — và điều gì mà nó KHÔNG nói lên về ý nghĩa của chúng?

## 8.19 Sinh Giả thuyết Cơ chế Ứng viên

### 8.19.1 Đường ống sinh giả thuyết

Bây giờ chúng ta ghép mọi thứ lại thành một đường ống sinh giả thuyết cơ chế:

```
1. Trích subgraph của từng ứng dụng (Quantity, Operation, Differentiand,
   WithRespectTo, Result)
2. Tính biểu diễn subgraph bằng GNN + pooling (học quy nạp, xử lý được thực thể mới)
3. Đo tương tự cấu trúc giữa các cặp ứng dụng (nhiều chiều, không chỉ cosine)
4. Gom các ứng dụng thành nhóm ứng viên (clustering, §8.28)
5. Với mỗi nhóm, đề xuất một CandidateMechanismHypothesis:
   "các ứng dụng này có thể cùng một cơ chế trừu tượng"
6. Đính kèm: bằng chứng cấu trúc, hỗ trợ từ nguồn, độ bất định, các giả thuyết cạnh
   tranh, provenance (mô hình nào, dữ liệu nào)
7. Đưa vào Claim Ledger như CandidateKnowledge (Ch6) chờ đánh giá và quản trị
```

### 8.19.2 CandidateMechanismHypothesis

Giả thuyết cơ chế ứng viên là một khái niệm do sách xây dựng (BOOK-DEFINED), nối tiếp
hook ở §7.36. Nó là một **yêu cầu** (claim) đặc biệt: nội dung của nó là "các ứng dụng
này có thể cùng một cơ chế", và nó mang:

- **Bằng chứng học được** (cấu trúc, tương tự, phân cụm)
- **Hỗ trợ nguồn** (các nguồn mô tả từng ứng dụng)
- **Độ bất định** (đa nguồn bất định, §8.32)
- **Các giả thuyết cạnh tranh** (ví dụ: cùng một cơ chế trừu tượng chung so với ba cơ
  chế riêng trông giống nhau)
- **Provenance đầy đủ** (mô hình nào, phiên bản dữ liệu nào, thời điểm nào)

Quan trọng: giả thuyết là **ứng viên**. Nó không phải là tri thức đã được chấp nhận.

> ⚠️ **Mẫu ≠ Cơ chế.**
> Đường ống ở trên chỉ sinh ra *giả thuyết*. Một nhóm các ứng dụng có cấu trúc giống
> nhau là một **mẫu** (pattern). Nó chỉ trở thành một *cơ chế được khẳng định* khi đi
> qua đánh giá tri thức luận (Ch6), so sánh với các giả thuyết cạnh tranh, kiểm tra phản
> ví dụ, và được quản trị chấp nhận. Chuyển từ mẫu sang cơ chế mà bỏ qua các bước này
> là sai lầm nguy hiểm nhất của học quy nạp.

## 8.20 Trừu tượng hóa RATE_OF_CHANGE: Ví dụ làm việc

Quay lại câu hỏi mở đầu. Hệ thống nhìn thấy ba ứng dụng:

```
Ứng dụng A (Vận tốc):     Operation=Derivative, Differentiand=Position,
                          WithRespectTo=Time, Result=Velocity
Ứng dụng B (Dòng điện):   Operation=Derivative, Differentiand=Charge,
                          WithRespectTo=Time, Result=Current
Ứng dụng C (Tăng trưởng): Operation=Derivative, Differentiand=Population,
                          WithRespectTo=Time, Result=GrowthRate
```

Các bước trừu tượng hóa:

1. **Khử khác biệt ngẫu nhiên:** thay `Position`, `Charge`, `Population` bằng biến
   `Quantity`; thay `Velocity`, `Current`, `GrowthRate` bằng biến `Result`.
2. **Giữ cấu trúc bất biến:** `Operation=Derivative`, `WithRespectTo=Time`, và mẫu
   vai trò `Quantity → Derivative → Result`.
3. **Đề xuất giả thuyết:** "có lẽ cả ba đều là một ứng dụng của cơ chế trừu tượng
   `RateOfChange`".

```
Position ──differentiand──► Velocity        Quantity ──differentiand──► Result
    ▲                            ▲              ▲                            ▲
    └────── withRespectTo ───────┘   +  Time    └────── withRespectTo ───────┘
   (cấu trúc ban đầu)                        (cấu trúc trừu tượng hóa)
```

![Trừu tượng hóa RATE_OF_CHANGE: ba ứng dụng (Vận tốc, Dòng điện, Tăng trưởng) cùng một mẫu vai trò; cấu trúc bất biến (Operation=Derivative, WithRespectTo=Time, Quantity→Derivative→Result) được giữ, tên miền được khử thành chi tiết ngẫu nhiên.](figures/generated/ch08-invariant-abstraction.pdf)

**Nhưng** — hệ thống không dừng ở đó. Nó phải hỏi các câu tiếp theo:

- `RateOfChange` ở mức trừu tượng này có giữ được ý nghĩa khi áp dụng cho dân số không?
  (Tăng trưởng dân số là một tỉ lệ rời rạc, khác đạo hàm tức thời của vị trí.)
- Có giả thuyết cạnh tranh nào tốt hơn không? (Ví dụ: vận tốc và dòng điện là "derivative
  theo thời gian của một đại lượng vật lý", còn tăng trưởng là "tỉ lệ thay đổi tương đối
  theo thời gian" — hai họ khác nhau.)
- Bằng chứng nguồn nào ủng hộ/không ủng hộ mức trừu tượng này?

Trừu tượng hóa là một **giả thuyết có cấu trúc**, không phải một phép thay tên biến
ngây thơ. Đổi `Position` thành `Quantity` là dễ; quyết định mức trừu tượng nào giữ ý
nghĩa là khó và cần đánh giá.

> 🖊 **Tự kiểm tra 4:** Theo bạn, mức trừu tượng nào là đúng cho ba ứng dụng? Có phải
> tất cả các "derivative theo thời gian" đều là cùng một cơ chế không? Nếu bạn cần phân
> biệt "derivative tức thời" (vận tốc) với "tỉ lệ thay đổi rời rạc" (tăng trưởng dân
> số), cấu trúc đồ thị nào phân biệt chúng — và phần nào cần văn bản/ngữ nghĩa?

## 8.21 Cấu trúc Bất biến, Cấu trúc Ngẫu nhiên, và "Biểu diễn quyết định khả năng học"

### 8.21.1 Bất biến và Ngẫu nhiên

Khi trừu tượng hóa, mô hình (hoặc con người) đề xuất **cấu trúc bất biến** (invariant
structure) — phần được giữ lại — và **cấu trúc ngẫu nhiên** (incidental structure) —
phần chi tiết miền bị bỏ đi.

Với ví dụ trên:
- **Bất biến (đề xuất):** Operation=Derivative, WithRespectTo=Time, mẫu vai trò
  Quantity → Derivative → Result
- **Ngẫu nhiên (đề xuất):** tên miền (Position vs Charge vs Population), ý nghĩa vật lý
  cụ thể

Việc tách bất biến/ngẫu nhiên là **bài toán học** — không phải điều hiển nhiên. Và
ranh giới này phụ thuộc vào mức trừu tượng mà hệ thống chọn.

### 8.21.2 Biểu diễn quyết định khả năng học

Một nguyên tắc quan trọng: **biểu diễn quyết định khả năng học** (representation
determines learnability). Mô hình chỉ có thể học từ những gì nó nhìn thấy. Nếu lược đồ
đặc trưng không bao gồm `WithRespectTo` (ví dụ, mô hình hóa ứng dụng chỉ bằng
`Operation` và `Result`), thì không một lượng dữ liệu nào giúp mô hình học rằng
`WithRespectTo=Time` là một phần của cấu trúc cơ chế — thông tin đó đã bị loại khỏi
biểu diễn.

Điều này kết nối trực tiếp với §8.4 (features before embeddings): việc chọn biểu diễn
là một quyết định thiết kế có hậu quả ngữ nghĩa, không phải một chi tiết kỹ thuật vô
hại.

> ⚠️ **Mô hình không thể học thứ không có trong đầu vào.**
> Nếu `WithRespectTo` không được đưa vào biểu diễn của ứng dụng, mô hình không bao giờ
> "phát hiện" rằng tham chiếu theo thời gian là phần bất biến của cơ chế. Đây là ranh
> giới hồi tưởng của học máy: garbage in, garbage out — nhưng ở mức lược đồ, không phải
> mức giá trị.

## 8.22 Học Quy tắc (Rule Induction) và AMIE+

### 8.22.1 Quy tắc đường đi

Bên cạnh KGE và GNN, có một họ học quy nạp khác sinh ra **quy tắc tượng trưng** thay vì
vector: **học quy tắc** (rule induction). AMIE+ là một trong những hệ thống khai phá quy
tắc quy mô lớn trên đồ thị tri thức, hoạt động dưới giả định thế giới mở
[@galarraga-amie-2015].

Một **quy tắc đường đi** (path rule) có dạng:

```
r1(x, y) ∧ r2(y, z) → r3(x, z)
```

Ví dụ trong hệ thống cơ chế:

```
hasOperation(x, Derivative) ∧ withRespectTo(x, Time) → resultIsRateOfChange(x)
```

nghĩa là: nếu x có thao tác Derivative và tham chiếu theo thời gian, thì kết quả của x
là một tốc độ thay đổi.

AMIE+ tìm các quy tắc như vậy bằng cách khai phá các đường đi trong đồ thị và đo độ
hỗ trợ/độ tin cậy của chúng.

### 8.22.2 Độ hỗ trợ và Độ tin cậy trong khai phá quy tắc

- **Độ hỗ trợ (support):** số thể hiện của quy tắc trong đồ thị — số lần cả thân và đầu
  cùng xuất hiện.
- **Độ tin cậy (confidence):** trong AMIE+, độ tin cậy được tính theo **giả định đầy đủ
  một phần (Partial Completeness Assumption, PCA)**: nếu một thực thể đã có ít nhất một
  giá trị cho quan hệ ở đầu quy tắc, giả định rằng tập giá trị của nó là đầy đủ — do đó
  các giá trị không xuất hiện là "phản ví dụ đã biết" [@galarraga-amie-2015].

Độ tin cậy PCA cho phép khai phá quy tắc làm việc dưới OWA mà không bị phạt quá nặng vì
thiếu thông tin — nhưng nó là một giả định kỹ thuật mạnh.

> ⚠️ **"Confidence" của khai phá quy tắc ≠ "confidence" của Chương 6.**
> Chương 6 xây dựng độ tin cậy tri thức luận (epistemic confidence): một đánh giá đa
> chiều về bằng chứng, nguồn, xung đột, thời gian — lý do *vì sao tin*. Độ tin cậy PCA
> của AMIE+ là một tần suất thống kê trên một tập dữ liệu cụ thể, dưới một giả định đầy
> đủ mạnh. Đây là một **xung đột thuật ngữ (terminology collision)**: hai khái niệm khác
> nhau, cùng tên "confidence". Chương này — và cuốn sách — luôn phân biệt chúng bằng
> thuật ngữ đầy đủ: "độ tin cậy khai phá quy tắc (rule-mining confidence)" so với "độ
> tin cậy tri thức luận (epistemic confidence)".

### 8.22.3 Quy tắc học được là giả thuyết

Một quy tắc có độ hỗ trợ cao và độ tin cậy PCA cao vẫn là một **giả thuyết**: nó mô tả
một mẫu trong dữ liệu, không phải một định luật logic. Nó chỉ trở thành quy tắc suy diễn
có giá trị khi:
1. Được đánh giá ngữ nghĩa (đúng với ontology Ch4)
2. Được kiểm tra phản ví dụ (§8.42)
3. Được quản trị chấp nhận (Ch6)
4. Được đưa vào bộ quy tắc có kiểm soát (Ch5)

> ⚠️ **Quy tắc học được ≠ định luật logic.**
> Chèn trực tiếp một quy tắc học được vào bộ suy diễn (Ch5) là một sai lầm nghiêm trọng:
> nó biến một giả thuyết thống kê thành một tiên đề bảo toàn chân lý, và mọi hệ quả sai
> sẽ lan truyền trên toàn đồ thị.

## 8.23 So sánh: Tượng trưng vs Nhúng

Hai họ học quy nạp — quy tắc tượng trưng và nhúng — có những điểm mạnh bổ sung nhau
[@nickel-relational-ml-2016]:

| Tiêu chí | Học quy tắc (symbolic) | Nhúng (embeddings) |
|----------|------------------------|--------------------|
| Đầu ra | Quy tắc đọc được | Vector, điểm số |
| Giải thích | Có (cấu trúc tường minh) | Khó (hình học ẩn) |
| Mở rộng tới thực thể mới | Tốt (quy tắc không phụ thuộc định danh) | Chuyển dẫn: kém; quy nạp (GNN): được |
| Xử lý bất định | Khó (không có độ bất định tự nhiên) | Tự nhiên (điểm số) |
| Ngữ nghĩa | Gần với logic, nhưng vẫn là giả thuyết | Không có ngữ nghĩa hình thức |
| Với quan hệ phức tạp | Khó nếu không có đường đi | Linh hoạt |

Không họ nào "đúng" tuyệt đối. Thực tế tốt nhất thường là kết hợp cả hai — dẫn đến kiến
trúc lai ở mục tiếp theo.

## 8.24 Kiến trúc Lai (Hybrid Pipeline): ML sinh ứng viên, Tượng trưng lọc, Tri thức luận quyết định

### 8.24.1 Kiến trúc tổng thể

Kiến trúc lai là **kiến trúc do sách xây dựng (BOOK-DEFINED)** — một sắp xếp kỹ thuật
kết hợp các chuẩn có thật, không phải một chuẩn được công bố. Nó có ba tầng:

```
        TẦNG 1: ML sinh ứng viên (statistical)
        KGE / GNN / rule mining → các bộ ba & quy tắc & giả thuyết ứng viên
                    │
                    ▼
        TẦNG 2: Tượng trưng lọc (symbolic filter)
        Kiểm tra kiểu (type checking), ràng buộc ontology (Ch4),
        cổng SHACL (Ch5, Ch7), truy vấn SPARQL xác minh tiền đề
                    │
                    ▼
        TẦNG 3: Tri thức luận + quản trị (epistemic & governance)
        Bằng chứng (Ch6), độ tin cậy tri thức luận, xung đột,
        Claim Ledger, quyết định accept / reject / review (Ch6–7)
                    │
                    ▼
        Sổ cái (Claim Ledger) → Chiếu hình (Canonical View)
```

![Kiến trúc lai: ML sinh giả thuyết → tượng trưng lọc ràng buộc → tri thức luận gắn bằng chứng → quản trị quyết định. Kiến trúc do sách xây dựng (BOOK-DEFINED).](figures/generated/ch08-hybrid-pipeline.pdf)

**Vai trò của từng tầng:**

- **Tầng 1 (ML):** sinh ứng viên với điểm số. Đây là nơi tri thức mới được *đề xuất*.
- **Tầng 2 (Tượng trưng):** loại bỏ các ứng viên vi phạm ràng buộc ngữ nghĩa đã biết.
  Ví dụ: nếu `withRespectTo` phải trỏ tới một `ReferenceVariable`, một ứng viên trỏ tới
  `Time` khi `Time` chưa được khai báo là ReferenceVariable sẽ bị cổng SHACL bắt
  (như nguồn C ở Chương 7).
- **Tầng 3 (Tri thức luận):** gắn bằng chứng, đánh giá, quyết định. Đây là nơi một ứng
  viên trở thành phát biểu được chấp nhận — hoặc bị từ chối.

### 8.24.2 Suy dẫn như một đặc trưng / bộ lọc

Một chi tiết quan trọng: suy dẫn (entailment) đóng vai trò là **bộ lọc và đặc trưng**
trong kiến trúc lai, không phải là nguồn chân lý.

- Là **bộ lọc**: một ứng viên mâu thuẫn với tri thức đã chấp nhận sẽ bị đưa vào quy trình
  xung đột (Ch6) — nó không tự động bị loại, nhưng phải được xem xét.
- Là **đặc trưng**: kết quả suy diễn (ví dụ: "theo quy tắc đã chấp nhận, mọi
  RateOfChangeApplication đều có withRespectTo Time") có thể là một đầu vào hữu ích cho
  mô hình ML.

> ⚠️ **Ràng buộc tượng trưng không chứng minh ứng viên còn lại là đúng.**
> Nếu một ứng viên vượt qua cổng SHACL và nhất quán với ontology, điều đó không có nghĩa
> là nó đúng. Nó chỉ có nghĩa là nó không vi phạm các ràng buộc đã biết. "Không sai theo
> ràng buộc" ≠ "đúng". Sự khác biệt này là hệ quả trực tiếp của OWA (Ch4).

### 8.24.3 Suy dẫn như một ràng buộc dương

Một ứng dụng tinh tế hơn: suy dẫn có thể đóng vai trò **ràng buộc dương** trong huấn
luyện. Nếu một quy tắc suy diễn đã được chấp nhận (Ch5) suy ra bộ ba T, thì T là một
"âm tính giả" chắc chắn nếu nó được sinh ra làm mẫu âm — và nó có thể được dùng như một
ví dụ dương thêm, không phụ thuộc vào việc nó có trong đồ thị hay không. Đây là một
cách kết hợp suy dẫn và học quy nạp có kỷ luật.

> 🖊 **Tự kiểm tra 5:** Lấy một giả thuyết cơ chế bất kỳ và chạy nó qua ba tầng của kiến
> trúc lai: ở tầng ML nó được đề xuất vì sao; ở tầng tượng trưng nó có thể bị chặn bởi
> ràng buộc nào; ở tầng tri thức luận nó cần bằng chứng gì trước khi được ghi sổ. Với
> mỗi tầng, hãy nói một thứ mà tầng đó KHÔNG thể chứng minh.

## 8.25 Rò rỉ Dữ liệu trong Thực hành Hệ thống

§8.10 giới thiệu các kiểu rò rỉ tổng quát. Mục này đi sâu vào ba kiểu đặc biệt nguy
hiểm với hệ thống cơ chế — vì chúng dễ bị bỏ sót trong đánh giá và dễ làm hệ thống
tự tin sai.

### 8.25.1 Rò rỉ thời gian (Temporal Leakage)

Đồ thị tri thức có thời gian (Ch6: valid time, assertion time). Nếu tập huấn luyện chứa
các phát biểu "tương lai" và tập kiểm chứa các phát biểu "quá khứ", mô hình không dự
đoán quá khứ — nó *hồi tưởng* tương lai.

Biện pháp: chia tách theo thời gian (temporal split) — huấn luyện trên dữ liệu trước
thời điểm T, kiểm tra trên dữ liệu sau T. Nhưng:

> ⚠️ **Chia theo thời gian không phải thuốc chữa bách bệnh.**
> Một mô hình huấn luyện trên 2024–2026 không nên được dùng để "dự đoán" năm 2024. Và
> chia theo thời gian không loại bỏ các kiểu rò rỉ khác (thực thể, nguồn, trùng lặp).
> Đây là một biện pháp, không phải một sự đảm bảo.

### 8.25.2 Rò rỉ nguồn (Source Leakage)

Bài học lớn của Chương 7: echo source không phải bằng chứng độc lập. Phiên bản học máy:
nếu hai cuốn sách khác nhau nhưng cùng chép từ một tài liệu gốc, và một cuốn ở train,
một cuốn ở test, thì điểm test cao không chứng minh tổng quát hóa — nó chỉ chứng minh
mô hình nhớ nguồn.

Biện pháp: chia tách theo nguồn (source split) — toàn bộ một nguồn ở test, không trộn.

> ⚠️ **Đa dạng nguồn trong train không đảm bảo độc lập của test.**
> Nếu 10 nguồn trong train đều là bản sao của một tài liệu gốc, chúng không phải 10 bằng
> chứng độc lập — chúng là 1 bằng chứng lặp 10 lần (Ch7 §7.23). Mô hình học được "mùi"
> của nguồn gốc đó, không phải sự đa dạng ngữ nghĩa.

### 8.25.3 Rò rỉ trùng lặp phát biểu (Claim Duplication)

Cùng một phát biểu (ví dụ "vận tốc là đạo hàm của vị trí") có thể xuất hiện ở nhiều
nơi trong cùng một nguồn, hoặc ở nhiều nguồn. Nếu các bản sao này rơi vào cả train lẫn
test, điểm số bị thổi phồng bởi các bản ghi gần như giống hệt nhau.

Chương 7 đã xử lý việc này ở tầng thu nhận (content hash, khử trùng). Chương 8 nhắc lại
ở tầng học máy: trước khi chia tách, phải khử trùng cấp độ phát biểu.

## 8.26 Tổng quát hóa Chéo Miền và Tương quan Giả

### 8.26.1 Tổng quát hóa chéo miền

Cơ chế RATE_OF_CHANGE xuất hiện ở nhiều miền: cơ học (vận tốc), điện tử (dòng điện),
kinh tế (lạm phát), sinh học (tăng trưởng). Một câu hỏi quyết định đối với hệ thống:
mô hình học từ các ứng dụng ở cơ học và điện tử có nhận ra cơ chế ở kinh tế không?

**Tổng quát hóa chéo miền (cross-domain generalization)** là khả năng nhận ra cơ chế
trong một miền mới dù từ vựng bề mặt khác hẳn. Đây là thử nghiệm quan trọng nhất cho
một hệ thống học cơ chế: huấn luyện trên cơ học + điện tử, kiểm tra trên kinh tế.

> ⚠️ **Độ chính xác trong miền không chứng minh hiểu cơ chế.**
> Một mô hình đạt 95% trên dữ liệu cơ học có thể hoàn toàn thất bại trên dữ liệu kinh
> tế — nếu nó học các dấu hiệu bề mặt của miền cơ học (chữ "m/s", cụm "vận tốc") thay vì
> cấu trúc cơ chế. Đây chính là vấn đề của tương quan giả.

### 8.26.2 Tương quan giả (Spurious Correlation) và Học lối tắt (Shortcut Learning)

**Học lối tắt (shortcut learning)** xảy ra khi mô hình đạt điểm cao trên dữ liệu kiểm
thử theo phân phối cũ bằng cách khai thác các dấu hiệu bề ngoài/trùng hợp, và sụp đổ
trong điều kiện khó hơn [@geirhos-shortcut-2020].

Ví dụ với hệ thống cơ chế: mọi ứng dụng RATE_OF_CHANGE trong dữ liệu huấn luyện đều đến
từ sách vật lý, và mọi sách vật lý đều chứa cụm từ "tốc độ thay đổi". Mô hình học: cụm
từ "tốc độ thay đổi" → RATE_OF_CHANGE. Khi gặp một văn bản kinh tế nói "lạm phát là tốc
độ tăng giá" — không có cụm từ kỳ diệu — mô hình bỏ lỡ, hoặc tệ hơn: gắn nhãn sai cho
một văn bản vật lý chỉ vì cụm từ xuất hiện ở một ngữ cảnh khác.

**Tương quan giả (spurious correlation)** là mối quan hệ học được giữa một dấu hiệu
bề mặt và nhãn, xuất hiện trong dữ liệu huấn luyện nhưng không phải là cấu trúc cơ chế.

> ⚠️ **Điểm cao không chứng minh mô hình học đúng thứ ta muốn.**
> Đây là cạm bẫy kinh điển: mô hình đạt accuracy 95% nhưng học lối tắt. Điểm số cao chỉ
> chứng minh mô hình khớp dữ liệu theo một cách nào đó — không chứng minh nó khớp theo
> *cách mà con người định nghĩa là đúng*.

## 8.27 Kiểm tra Phản thực tế và Âm tính Khó

### 8.27.1 Kiểm tra phản thực tế (Counterfactual Tests)

Làm sao phát hiện mô hình học lối tắt? Một công cụ mạnh: **kiểm tra phản thực tế** —
thay đổi một thành phần cấu trúc và kiểm tra xem mô hình có phản ứng đúng không.

Ví dụ với ứng dụng A (vận tốc):

- **Thay đổi WithRespectTo từ Time sang Distance:** "đạo hàm của vị trí theo quãng
  đường" — nếu mô hình vẫn gắn nhãn RATE_OF_CHANGE (theo thời gian), nó đang bỏ qua
  thành phần quan trọng này. Kết quả mong đợi: không phải RateOfChangeApplication.
- **Thay đổi Operation từ Derivative sang Average:** "tỉ lệ thay đổi trung bình" — nếu
  mô hình vẫn gắn nhãn như cũ, nó không phân biệt derivative với average. Kết quả mong
  đợi: phản hồi khác.

Counterfactual test biến một giả thuyết "mô hình học cấu trúc" thành một dự đoán có thể
kiểm chứng: nếu mô hình học đúng cấu trúc, thay đổi cấu trúc phải thay đổi dự đoán.

> ⚠️ **Một counterfactual test đậu không chứng minh mô hình đúng.**
> Nó chỉ loại bỏ một lớp lối tắt cụ thể. Mô hình có thể vẫn đang học một lối tắt khác.
> Đây là bản chất của giả thuyết: kiểm tra làm tăng sự tự tin, không bao giờ chứng minh
> hoàn toàn.

### 8.27.2 Âm tính khó (Hard Negative)

Khi huấn luyện phân biệt RATE_OF_CHANGE với các cơ chế khác, chất lượng âm tính quyết
định chất lượng ranh giới:

- **Âm tính dễ (easy negative):** `ColorClassification` — khác xa, không dạy gì về ranh
  giới.
- **Âm tính khó (hard negative):** `FiniteDifferenceApplication` — đạo hàm rời rạc,
  gần RATE_OF_CHANGE, buộc mô hình phân biệt "tức thời" với "trung bình/đoạn".

Mô hình chỉ có ranh giới tốt nếu nó được huấn luyện với âm tính khó. Chỉ dùng âm tính
dễ, mô hình sẽ gán nhãn sai cho mọi ứng dụng gần ranh giới.

> ⚠️ **Âm tính khó ≠ phản ví dụ logic.**
> Một âm tính khó là một mẫu huấn luyện nằm gần ranh giới lớp. Một phản ví dụ (Chương
> này, §8.42) là một quan sát bác bỏ một giả thuyết đã được chấp nhận. Chúng khác nhau
> về vai trò và hậu quả: âm tính khó định hình ranh giới học; phản ví dụ định hình tri
> thức đã được quản trị.

## 8.28 Họ Cơ chế vs Cùng Một Cơ chế; Phân cụm

### 8.28.1 Một cơ chế hay một họ cơ chế?

Câu hỏi "vận tốc, dòng điện, tăng trưởng có cùng một cơ chế không?" có thể có nhiều câu
trả lời đúng ở các mức trừu tượng khác nhau:

- **Cùng một cơ chế** (cùng một lớp): nếu chúng ta xác định cơ chế ở mức "đạo hàm một
  đại lượng theo thời gian" — cả ba đều là RATE_OF_CHANGE.
- **Họ cơ chế** (một lớp cha, nhiều lớp con): nếu chúng ta phân biệt "derivative tức
  thời" (vận tốc) với "tỉ lệ thay đổi rời rạc" (tăng trưởng dân số) — đây là một họ gồm
  nhiều cơ chế con.

Quyết định này **không phải là một phát hiện thống kê thuần túy** — nó phụ thuộc vào
mục tiêu tri thức của hệ thống và được quản trị quyết định (§8.40). Học quy nạp sinh ra
các mức trừu tượng ứng viên; quản trị chọn mức nào có giá trị.

### 8.28.2 Phân cụm (Clustering) — khám phá, không phải khẳng định

**Phân cụm** gom các ứng dụng thành nhóm dựa trên biểu diễn/đặc trưng mà không có nhãn.
Trong hệ thống cơ chế, phân cụm là công cụ **khám phá** (exploratory): nó đề xuất "các
ứng dụng này có vẻ cùng nhóm".

> ⚠️ **Cụm không phải lớp ontology.**
> Một cụm phát hiện bởi thuật toán không phải là một lớp trong ontology. Chuyển trực
> tiếp cụm thành lớp (RATE_OF_CHANGE ⊑ ...) mà không qua đánh giá ngữ nghĩa và quản trị
> là một vi phạm nghiêm trọng kiến trúc của sách. Cụm chỉ là bằng chứng gợi ý cho giả
> thuyết cơ chế (§8.19).

## 8.29 Phân lớp và Hiệu chuẩn

### 8.29.1 Phân lớp (Classification) — đầu ra ứng viên

**Phân lớp** là bài toán có nhãn: một mô hình được huấn luyện trên các ứng dụng đã được
gán nhãn (RateOfChangeApplication vs FiniteDifferenceApplication vs ...) để gán nhãn
cho ứng dụng mới. Đầu ra là một phân bố xác suất trên các lớp — ví dụ:

```
Ứng dụng X:  RateOfChange 0.82 | FiniteDifference 0.15 | Other 0.03
```

Đầu ra này là một **giả thuyết ứng viên**, không phải khẳng định kiểu.

> ⚠️ **Nhãn dự đoán không được ghi thẳng vào đồ thị.**
> Ghi `X rdf:type RateOfChangeApplication` vào đồ thị vì mô hình nói 0.82 là bỏ qua toàn
> bộ kiến trúc: nó phải đi qua CandidateClaim (Ch7) → bằng chứng (Ch6) → quản trị.

### 8.29.2 Hiệu chuẩn (Calibration)

Xác suất đầu ra của mô hình học sâu có đáng tin không? **Hiệu chuẩn (calibration)** đo
mức khớp giữa xác suất dự đoán và tần suất đúng thực tế [@guo-calibration-2017]:

- Mô hình **được hiệu chuẩn tốt**: trong nhóm các dự đoán "0.8", khoảng 80% là đúng.
- Mô hình **tự tin quá mức (overconfident)**: trong nhóm "0.8", chỉ 60% đúng.

Nghiên cứu của Guo và đồng tác giả cho thấy các mạng nơ-ron hiện đại thường tự tin quá
mức — đặc biệt trên dữ liệu khó. Một kỹ thuật khắc phục phổ biến: **temperature
scaling** — điều chỉnh độ "phẳng" của phân bố xác suất mà không thay đổi thứ tự dự đoán.

> ⚠️ **Softmax ≠ xác suất chân lý.**
> Giá trị softmax của mô hình là một ước lượng thống kê chưa được hiệu chuẩn. Nó không
> phải là xác suất "bộ ba này đúng" theo nghĩa tri thức luận (Ch6). Để dùng một con số
> như bằng chứng, hệ thống cần một ModelAssessment (§8.30) khai báo ngữ nghĩa của con
> số đó.

## 8.30 ModelAssessment và Provenance Mô hình

### 8.30.1 Vấn đề: con số vô danh

Một điểm số "0.82" xuất hiện trong một phát biểu mà không có ngữ cảnh là một con số vô
danh — không thể kiểm chứng, không thể so sánh, không thể xem xét. Nó đến từ mô hình
nào? Trên dữ liệu nào? Với lược đồ đặc trưng nào? Ở thời điểm nào? Theo quy ước chấm
điểm nào (logit, ranking, softmax, calibrated)?

### 8.30.2 ModelAssessment

**ModelAssessment** là một khái niệm do sách xây dựng (BOOK-DEFINED) — một đối tượng
"bọc" mọi điểm số của mô hình, ghi lại:

- **Target:** bộ ba / ứng dụng được chấm điểm
- **Model:** định danh mô hình + phiên bản
- **Task:** bài toán (link prediction, classification, ...)
- **Score:** giá trị điểm số
- **Score semantics:** ngữ nghĩa của điểm số (logit / ranking / softmax / calibrated)
- **Assessed at:** thời điểm đánh giá
- **Training dataset:** phiên bản dữ liệu huấn luyện
- **Evaluation context:** bối cảnh đánh giá (train / validation / test, miền nào)

### 8.30.3 Provenance huấn luyện

Mọi giả thuyết học được đều được **sinh ra bởi một hoạt động huấn luyện** — theo mô
hình PROV (Ch6): một `TrainingOrInferenceActivity` có `wasGeneratedBy` ghi lại dữ liệu
huấn luyện, phiên bản mô hình, lược đồ đặc trưng, cấu hình. Mô hình không phải là một
hộp đen kỳ diệu: mọi dự đoán đều có provenance [@prov-o].

> ⚠️ **Provenance huấn luyện không phải bằng chứng.**
> "Mô hình được huấn luyện trên các ví dụ ủng hộ P" là thông tin về *nguồn gốc của dự
> đoán*, không phải bằng chứng rằng P đúng. Việc dự đoán dựa trên dữ liệu không làm cho
> dữ liệu đó trở thành bằng chứng cho nội dung của dự đoán. Phân biệt này song song với
> phân biệt lineage vs evidence của Chương 7.

## 8.31 Dữ liệu Huấn luyện có phải Bằng chứng không?

### 8.31.1 Provenance ≠ Evidence

Đây là một trong những ranh giới tri thức luận quan trọng nhất của chương. Một phát
biểu được chấp nhận trong sổ cái (Ch6) cần bằng chứng: các nguồn, độ tin cậy, đánh giá
xung đột, thời gian. Một dự đoán của mô hình có provenance — nhưng không có bằng chứng
theo nghĩa Ch6.

Tại sao? Vì dữ liệu huấn luyện có thể chứa:

- Các lỗi từ khâu trích xuất (Ch7)
- Các phát biểu mâu thuẫn chưa được phân giải
- Các tương quan giả (§8.26)
- Các phát biểu của chính mô hình được tái sử dụng (vòng phản hồi, §8.33)

Mô hình "học từ dữ liệu" không có nghĩa là nó học được sự thật — nó học được sự thật
*theo phân phối của dữ liệu*, và phân phối đó có thể sai lệch.

### 8.31.2 Nguồn Echo và Trùng lặp trong Dữ liệu Huấn luyện

Bài học echo source của Chương 7 (§7.23) áp dụng trực tiếp: nếu một phát biểu được sao
chép 100 lần trên 100 trang web (echo source), mô hình coi nó là một mẫu rất mạnh —
dù nó chỉ là một bằng chứng gốc. Dữ liệu huấn luyện phải được lọc echo trước khi dùng
làm tín hiệu huấn luyện, nếu không mô hình "học" sự lặp lại, không phải sự đồng thuận.

> ⚠️ **"Được huấn luyện trên N ví dụ" không có nghĩa là "có N bằng chứng độc lập".**
> Nếu 90/100 ví dụ là bản sao của cùng một nguồn gốc, mô hình thực chất học từ ~10 bằng
> chứng độc lập, được lặp lại 10 lần. Số lượng ví dụ không phải số lượng bằng chứng.

> 🖊 **Tự kiểm tra 6:** Một mô hình dự đoán "vận tốc là rate of change của vị trí" với
> điểm số 0.9. Trước khi hệ thống xem xét phát biểu này, danh sách nào sau đây là thiếu
> và cần được bổ sung: (a) ngữ nghĩa của con số 0.9; (b) phiên bản mô hình và dữ liệu
> huấn luyện; (c) thời điểm đánh giá; (d) bằng chứng nguồn độc lập cho chính phát biểu;
> (e) kết quả kiểm tra xung đột với sổ cái. Hãy giải thích vai trò của từng mục — và mục
> nào trong số chúng là bằng chứng theo nghĩa Ch6, mục nào chỉ là provenance.

## 8.32 Các Nguồn Bất định và Lỗi Mô hình vs Xung đột Tri thức

### 8.32.1 Nhiều nguồn bất định, không chỉ một

Độ bất định của một giả thuyết cơ chế đến từ nhiều nguồn khác nhau, và chúng **không
thể gộp thành một con số**:

| Nguồn bất định | Câu hỏi | Xuất hiện ở |
|----------------|---------|-------------|
| Trích xuất | Bản ghi có đúng với nguồn không? | Ch7 |
| Định danh | Hai bản ghi có phải một thực thể? | Ch3, Ch7 |
| Lược đồ | Ánh xạ có đúng ngữ nghĩa không? | Ch7 |
| Mô hình | Dự đoán của mô hình đáng tin đến đâu? | Ch8 |
| Bằng chứng | Các nguồn có ủng hộ không? | Ch6 |
| Thời gian | Phát biểu còn hiệu lực không? | Ch6 |

Gộp tất cả thành một "độ tự tin" duy nhất là mất mát thông tin nghiêm trọng: hai giả
thuyết có cùng độ tự tin gộp có thể bất định vì những lý do hoàn toàn khác nhau — một
cái bất định vì mô hình yếu, một cái bất định vì thiếu nguồn. Cách xử lý khác nhau.

### 8.32.2 Lỗi mô hình hay mâu thuẫn tri thức?

Tình huống khó: mô hình dự đoán P, nhưng sổ cái có `not P` đã được chấp nhận. Xử lý thế
nào?

- **Sai lầm:** ghi đè tri thức đã quản trị bằng điểm số của mô hình ("mô hình nói 0.9
  nên nó đúng").
- **Đúng:** tạo một CandidateClaim mới, đưa vào quy trình xung đột (Ch6 §6.18), với các
  khả năng: (a) mô hình sai; (b) tri thức hiện có sai; (c) cả hai đúng nhưng ở ngữ cảnh
  khác (multi-label, scope khác); (d) phiên bản ontology khác nhau.

> ⚠️ **Điểm số không thắng quản trị.**
> Không có điểm số nào của mô hình — dù 0.999 — tự nó ghi đè một phát biểu đã được chấp
> nhận. Thứ tự ưu tiên luôn là: quy trình tri thức luận và quản trị quyết định; mô hình
> chỉ đề xuất ứng viên.

## 8.33 Học Tích cực, Phản hồi Con người, và Vòng lặp Học

### 8.33.1 Học tích cực (Active Learning)

Gán nhãn cho tất cả các ứng dụng mới là tốn kém. **Học tích cực** chọn ra các mẫu
*đáng gán nhãn nhất* — thường là các mẫu có độ bất định cao, như các ứng dụng nằm ngay
tại ranh giới RATE_OF_CHANGE / FiniteDifference — và nhờ con người gán nhãn những mẫu
đó. Mỗi nhãn thu được có giá trị thông tin cao nhất.

### 8.33.2 Phản hồi con người là dữ liệu

Phản hồi của con người (chấp nhận / từ chối / sửa nhãn) trở thành dữ liệu cho các vòng
huấn luyện sau. Điều này tạo ra một vòng lặp học (iterative learning loop):

```
Mô hình dự đoán → Con người đánh giá → Kết quả đánh giá (có provenance)
→ Dữ liệu cho vòng huấn luyện sau → Mô hình mới → ...
```

Vòng lặp này mạnh — nhưng có một cạm bẫy: **tính tuần hoàn (circularity)**. Nếu con
người chỉ "rubber-stamp" (đóng dấu) các dự đoán của mô hình mà không thực sự xem xét,
thì dữ liệu mới chỉ là tiếng vọng của mô hình cũ.

> ⚠️ **Đóng dấu không phải bằng chứng độc lập.**
> Một phát biểu được con người chấp nhận vì mô hình đề xuất nó — mà không qua kiểm tra
> nguồn/bằng chứng — không phải một xác nhận độc lập. Vòng lặp "mô hình đề xuất → con
> người đóng dấu → huấn luyện lại" làm tăng tự tin mà không tăng bằng chứng.

## 8.34 Vòng Phản hồi Tự củng cố và Model Collapse

### 8.34.1 Vòng phản hồi tự củng hồi (self-reinforcing feedback)

Khi các dự đoán của mô hình quay lại làm dữ liệu huấn luyện, một vòng phản hồi được
hình thành. Vòng phản hồi này **tự củng cố** (self-reinforcing): mô hình học các mẫu
của chính nó, các mẫu đó lại được dùng để huấn luyện mô hình tiếp theo, và các sai lệch
nhỏ được khuếch đại dần.

Nguyên tắc của sách: phải phân biệt rõ **tri thức do con người/nguồn sinh ra** với
**tri thức do mô hình sinh ra** (model-generated candidate knowledge). Cái sau phải
được gắn cờ provenance "model-generated" và không bao giờ được trộn vào dữ liệu huấn
luyện mà không có kiểm soát.

### 8.34.2 Model Collapse

Shumailov và đồng tác giả chứng minh một hiện tượng nghiêm trọng: khi mô hình được
huấn luyện trên dữ liệu do chính các mô hình sinh ra (recursively generated data),
**model collapse** xảy ra — các "đuôi" của phân phối gốc biến mất, sự đa dạng của tri
thức suy giảm, và các khiếm khuyết tích lũy không thể đảo ngược [@shumailov-collapse-2024].

> ⚠️ **Huấn luyện lại trên dự đoán không xác nhận dự đoán.**
> "Mô hình cũ dự đoán X, mô hình mới huấn luyện trên dự đoán đó cũng nói X — vậy X chắc
> chắn đúng" là một ngụy biện. Đây không phải hai nguồn xác nhận; đây là một nguồn tự
> nhìn thấy chính nó hai lần. Điều này áp dụng cho cả LLM lẫn mô hình đồ thị.

## 8.35 Giải thích và Giải thích theo Đường đi

### 8.35.1 Tại sao cần giải thích?

Một giả thuyết cơ chế được đề xuất bởi mô hình sẽ được con người xem xét trong quy
trình quản trị (Ch6–7). Để con người quyết định được, giả thuyết phải **giải thích được**
— phải trả lời "tại sao mô hình đề xuất điều này?"

### 8.35.2 Giải thích theo đường đi (path-based explanation)

Với học quy tắc (AMIE+), giải thích tự nhiên là **đường đi trong đồ thị**: quy tắc
`hasOperation(x, Derivative) ∧ withRespectTo(x, Time) → resultIsRateOfChange(x)` kèm
theo đường đi cụ thể trong subgraph của ứng dụng:

```
Application_A —operation→ DerivativeOperation
Application_A —withRespectTo→ Time
Application_A —result→ Velocity
∴ (theo quy tắc học được) Velocity là một rate of change
```

Với KGE/GNN, giải thích khó hơn: các vector không có ý nghĩa tường minh. Một cách tiếp
cận thực dụng: **giải thích ở cấp cấu trúc** — chỉ ra các yếu tố cấu trúc đóng góp
nhiều nhất vào điểm số (các lân cận, các quan hệ, các đặc trưng), thay vì giải thích
từng chiều vector.

> ⚠️ **Giải thích không phải bằng chứng.**
> Một lời giải thích ("mô hình đề xuất vì cấu trúc giống hệt ứng dụng A") làm rõ *vì
> sao mô hình* đưa ra dự đoán — nó không chứng minh *dự đoán đúng*. Giải thích là về
> cơ chế của mô hình; bằng chứng là về sự thật của phát biểu (Ch6).

## 8.36 Mục tiêu Đánh giá, Benchmark, và Khung So sánh Mô hình

### 8.36.1 Mục tiêu đánh giá cho phát hiện cơ chế

Đánh giá một hệ thống học cơ chế cần các mục tiêu cụ thể, không phải accuracy chung
chung:

- **Chính xác về cơ chế:** tỉ lệ giả thuyết cơ chế được quản trị chấp nhận là đúng
  (so với đánh giá của con người có nguồn gốc)
- **Độ bao phủ:** tỉ lệ cơ chế thực sự tồn tại được hệ thống đề xuất
- **Không phát minh sai:** tỉ lệ giả thuyết được đề xuất nhưng sai (false discovery)
- **Ổn định:** cùng một cấu trúc ở các miền khác nhau cho cùng một đề xuất
- **Chống lối tắt:** kết quả counterfactual test (§8.27)

### 8.36.2 Benchmark và so sánh mô hình

So sánh mô hình có ý nghĩa chỉ khi cùng một benchmark với cùng quy tắc chia tách, cùng
bộ dữ liệu, cùng quy ước đánh giá. MRR trên FB15k-237 không so sánh được với MRR trên
một đồ thị cơ chế nhỏ. Mọi con số so sánh phải kèm: dữ liệu, chia tách, quy ước filtered
hay raw, và ngữ nghĩa điểm số.

> ⚠️ **Số liệu đẹp ≠ hệ thống tốt.**
> Một mô hình đạt MRR 0.9 trên benchmark chuẩn vẫn có thể hoàn toàn vô dụng cho hệ thống
> cơ chế nếu nó không tổng quát hóa chéo miền hoặc không phân biệt các cơ chế gần nhau.
> Benchmark đo điểm số trên dữ liệu; hệ thống cần năng lực trên nhiệm vụ.

## 8.37 Khi nào KHÔNG dùng Graph ML — và Quyết định Dựa trên Năng lực

### 8.37.1 Khi nào không cần học máy

Học quy nạp tốn kém: dữ liệu, huấn luyện, đánh giá, quản trị dự đoán. Nó chỉ nên được
dùng khi cần sinh tri thức *vượt ra ngoài* những gì nguồn nói. Các tình huống KHÔNG
dùng:

| Tình huống | Vì sao không dùng ML |
|------------|----------------------|
| Quy tắc đã biết, có thể viết bằng tay (Ch5) | Suy diễn chính xác, đã quản trị, không cần học |
| Dữ liệu quá ít / không đại diện | ML không thể sinh quy luật từ không có gì |
| Hậu quả sai lầm không chấp nhận được | ML không đảm bảo chân lý (§8.47) |
| Cần giải thích đầy đủ theo ngữ nghĩa | Embedding không mang ngữ nghĩa |
| Dữ liệu có tương quan giả mạnh, chưa lọc | Mô hình sẽ học lối tắt |

### 8.37.2 Quyết định dựa trên năng lực (capability-based decision)

Nguyên tắc quyết định của hệ thống: **chỉ đề xuất tri thức bằng học máy khi năng lực
của hệ thống đủ cho mức rủi ro của quyết định.** Hệ thống phải biết nó biết gì (Ch6),
nó đã học gì (Ch8), và nó không đảm bảo điều gì (§8.47). Việc quyết định "dùng hay
không dùng ML" là một quyết định kiến trúc được ghi lại, có lý do — không phải mặc định
"có ML thì tốt hơn".

## 8.38 Mẫu ≠ Cơ chế; Thao tác và Ý nghĩa; Cấu trúc và Văn bản

### 8.38.1 Từ mẫu đến cơ chế

Một mẫu lặp lại trong đồ thị — ba ứng dụng có cùng cấu trúc — có thể xuất hiện tình
cờ, hoặc do quy ước của một nguồn, hoặc do một cơ chế thực sự. Bản thân tần suất không
phân biệt được các trường hợp này. Cơ chế, theo định nghĩa của sách (Ch1/Ch4), là một
cấu trúc có **ý nghĩa giải thích/vận hành ổn định** — một mẫu lặp không tự mang ý
nghĩa đó.

Hệ thống phải giữ ranh giới: **phát hiện mẫu → giả thuyết cơ chế → đánh giá → quyết
định**. Không bước nào được bỏ qua.

### 8.38.2 Thao tác (operation) và Ý nghĩa (meaning)

Học quy nạp có thể học được *hình dạng thao tác* — "có một thao tác Derivative nối
Quantity với Result" — nhưng không tự động học được *ý nghĩa* — "instantaneous" so với
"average", "theo thời gian" so với "theo quãng đường". Ý nghĩa cần:

- Định nghĩa văn bản của nguồn (Ch7 đã thu nhận)
- Ngữ nghĩa ontology (Ch4)
- Bằng chứng và đánh giá của con người (Ch6)
- Sự đồng thuận chéo nguồn (Ch7)

> ⚠️ **Topology không sinh ra semantics.**
> Hai ứng dụng có cấu trúc giống hệt nhau vẫn có thể khác nhau về ý nghĩa (finite
> difference vs derivative tức thời). Ngược lại, hai ứng dụng khác cấu trúc có thể cùng
> một ý nghĩa (các biến thể ký hiệu). Hình học đồ thị là bằng chứng, không phải ngữ
> nghĩa.

### 8.38.3 Cấu trúc + Văn bản

Bằng chứng tốt nhất kết hợp cả hai: cấu trúc đồ thị gợi ý sự tương tự về vai trò; văn
bản nguồn phân biệt ý nghĩa ("tức thời" vs "trung bình"). Một hệ thống bỏ qua văn bản
mất đi khả năng phân biệt tinh tế; một hệ thống dựa hoàn toàn vào văn bản bị lừa bởi
sự giống nhau về từ ngữ (hai khái niệm khác nhau cùng dùng cụm "tốc độ thay đổi").

> ⚠️ **Từ ngữ giống nhau không phải cấu trúc giống nhau.**
> "Tốc độ thay đổi" xuất hiện ở nguồn A (đạo hàm) và nguồn C (dòng điện) không chứng
> minh chúng cùng cơ chế — đây chính là bài học của Chương 7 §7.0. Embedding văn bản bắt
> sự tương tự từ ngữ; cấu trúc đồ thị bắt sự tương tự vai trò; sự thống nhất chỉ đến từ
> đánh giá tri thức luận.

## 8.39 Các loại Giả thuyết và Chính sách Chấp nhận

### 8.39.1 Các loại giả thuyết ứng viên

Hệ thống học quy nạp sinh ra nhiều loại giả thuyết khác nhau, mỗi loại có mức rủi ro
khác nhau:

| Loại giả thuyết | Ví dụ | Rủi ro nếu sai |
|-----------------|-------|----------------|
| Liên kết ứng viên | `(Velocity, rateOfChangeOf, Position)` | Thấp — cục bộ, dễ kiểm tra |
| Nhãn phân lớp | `X rdf:type RateOfChangeApplication` | Trung bình — ảnh hưởng suy diễn qua kiểu |
| Giả thuyết cơ chế | "A, B, C cùng một cơ chế trừu tượng" | Trung bình — đòi hỏi thay đổi quan niệm |
| Quy tắc học được | `r1 ∧ r2 → r3` | Cao — nếu vào bộ suy diễn, lan toàn đồ thị |
| Tiên đề ontology | `RateOfChange ⊑ ChangeMechanism` | Rất cao — thay đổi toàn bộ phân loại |

### 8.39.2 Chính sách chấp nhận và mức rủi ro

Chính sách chấp nhận của hệ thống phân theo mức rủi ro (high-risk / low-risk):

- **Rủi ro thấp** (liên kết cục bộ, hậu quả dễ đảo ngược): có thể chấp nhận với bằng
  chứng nhẹ hơn — nhưng vẫn cần đánh giá và ghi sổ.
- **Rủi ro cao** (tiên đề, quy tắc suy diễn, thay đổi ontology): đòi hỏi bằng chứng
  nhiều nguồn độc lập, kiểm tra phản ví dụ, đánh giá blast radius (§8.41), và quyết
  định của con người.

> ⚠️ **Mức rủi ro cao không bị cấm — bị kiểm soát chặt hơn.**
> Hệ thống không từ chối các giả thuyết rủi ro cao; nó yêu cầu chúng đi qua các cổng
> nghiêm ngặt hơn. Từ chối toàn bộ là bỏ lỡ tri thức; chấp nhận dễ dãi là phá hỏng đồ
> thị.

## 8.40 Ví dụ Làm việc Toàn trình: 15 Bước

Kết hợp tất cả các thành phần trong một ví dụ toàn trình — từ đồ thị đến giả thuyết
được quản trị. Bối cảnh: hệ thống đã tích hợp (Ch7) ba ứng dụng: Vận tốc (cơ học), Dòng
điện (điện tử), Tăng trưởng dân số (kinh tế học).

1. **Xác định subgraph.** Với mỗi ứng dụng, trích subgraph quanh nút ứng dụng: các nút
   Quantity, Operation, WithRespectTo, Result và các cạnh nối.
2. **Chọn biểu diễn.** Quyết định lược đồ đặc trưng: Operation, WithRespectTo, Result,
   kiểu Quantity — biểu diễn quyết định khả năng học (§8.21).
3. **Huấn luyện mô hình (validation).** Chia tách theo nguồn (không rò rỉ §8.25), huấn
   luyện GNN + pooling trên các ứng dụng cơ học/điện tử.
4. **Đánh giá chéo miền.** Kiểm tra trên ứng dụng kinh tế — vượt qua được là một tín
   hiệu quan trọng (§8.26).
5. **Counterfactual tests.** Thay WithRespectTo bằng Distance; kiểm tra dự đoán thay
   đổi (§8.27).
6. **Tính biểu diễn subgraph.** GNN + pooling cho ba ứng dụng; đo tương tự cấu trúc
   (nhiều chiều, không chỉ cosine).
7. **Phân cụm khám phá.** Ba ứng dụng rơi vào cùng một cụm — bằng chứng gợi ý, không
   phải khẳng định (§8.28).
8. **Sinh giả thuyết.** Tạo CandidateMechanismHypothesis: "ba ứng dụng có thể cùng một
   cơ chế trừu tượng" với đầy đủ bằng chứng, bất định, giả thuyết cạnh tranh, provenance
   (§8.19).
9. **Lọc tượng trưng.** Kiểm tra kiểu/ontology: `WithRespectTo=Time` phải trỏ ReferenceVariable; mọi kiểm tra đậu (§8.24).
10. **So sánh giả thuyết cạnh tranh.** "Cùng một cơ chế" so với "họ cơ chế với con
    khác biệt tức thời/rời rạc" — bằng chứng văn bản phân biệt chúng (§8.38).
11. **Đánh giá tri thức luận.** Gắn bằng chứng nguồn (đa nguồn độc lập), đánh giá độ
    tin cậy tri thức luận (Ch6), kiểm tra xung đột với sổ cái.
12. **Kiểm tra phản ví dụ.** Tìm quan sát bác bỏ giả thuyết ở mức trừu tượng đã chọn
    (§8.42).
13. **Quyết định quản trị.** Chấp nhận giả thuyết ở mức "họ cơ chế" với các con được
    quản trị riêng; ghi vào Claim Ledger với provenance mô hình và lý do quyết định.
14. **Đề xuất tiến hóa ontology.** Đề xuất tách con `InstantaneousRateOfChange` /
    `AverageRateOfChange` — như CandidateAxiom chờ đánh giá (§8.41).
15. **Ghi lại toàn bộ.** Mọi bước, mọi điểm số, mọi quyết định — có provenance — vào
    hồ sơ kiểm toán.

Kết quả: hệ thống không "biết" ba ứng dụng là cùng cơ chế — nó có một giả thuyết được
đánh giá, được quản trị, và có thể được xem xét lại khi có dữ liệu mới.

## 8.41 Tiên đề Ứng viên và Blast Radius

### 8.41.1 Tiên đề học được là gì?

Một mô hình có thể đề xuất các cấu trúc ở mức ontology: "mọi RateOfChangeApplication
đều là ChangeMechanism" — một **tiên đề ứng viên (CandidateAxiom)**.

Tiên đề khác với phát biểu cục bộ: nó là một quy tắc **toàn cục**. Nếu được chấp nhận,
nó áp dụng cho mọi thực thể trong đồ thị — hiện tại và tương lai.

### 8.41.2 Blast radius

**Blast radius** (bán kính ảnh hưởng) của một tiên đề ứng viên là tập các kết luận bị
ảnh hưởng nếu tiên đề đó sai. Với `RateOfChange ⊑ ChangeMechanism`: mọi suy diễn
`X rdf:type ChangeMechanism` được suy ra từ tiên đề này đều sai nếu tiên đề sai.

Đánh giá blast radius là bắt buộc trước khi chấp nhận tiên đề ứng viên: truy vấn SPARQL
tính toán tập kết luận bị ảnh hưởng, kiểm tra tính nhất quán (Ch5), và quyết định xem
mức ảnh hưởng có chấp nhận được với bằng chứng hiện có không.

> ⚠️ **Tiên đề học được không được tự động đưa vào ontology.**
> Chèn tiên đề ứng viên vào ontology mà không qua: đánh giá ngữ nghĩa, kiểm tra nhất
> quán, đánh giá bằng chứng, đo blast radius, và quyết định quản trị — là một vi phạm
> nghiêm trọng. Một tiên đề sai phá hỏng mọi suy diễn dựa trên nó (Ch5).

## 8.42 Ranh giới, Phản ví dụ, và Tiến hóa Ontology

### 8.42.1 Ranh giới của cơ chế

Mọi giả thuyết cơ chế có ranh giới: các trường hợp nằm trong, các trường hợp nằm ngoài.
Giả thuyết RATE_OF_CHANGE ở mức trừu tượng đầy đủ phải xác định: `AverageRateOfChange`
có thuộc không? `FiniteDifference` có thuộc không? `Derivative theo quãng đường` có
thuộc không?

Ranh giới này là một phần của giả thuyết và phải được kiểm tra.

### 8.42.2 Phản ví dụ (counterexample) và tinh chỉnh

Khi một quan sát mới (hoặc một quan sát cũ được xem xét lại) bác bỏ một giả thuyết đã
được chấp nhận, hệ thống phải xử lý có kỷ luật:

1. **Ghi nhận phản ví dụ** với provenance đầy đủ
2. **Đánh giá mức độ:** phản ví dụ bác bỏ toàn bộ giả thuyết, hay chỉ một phần (một
   con, một ngữ cảnh)?
3. **Tinh chỉnh giả thuyết:** hẹp lại ranh giới, tách con, hoặc bỏ giả thuyết
4. **Cập nhật sổ cái:** giả thuyết cũ được đánh dấu superseded (Ch6), giả thuyết mới
   được ghi với lý do tinh chỉnh
5. **Học từ phản ví dụ:** phản ví dụ trở thành âm tính khó cho vòng huấn luyện sau
   (§8.27)

Phản ví dụ không phải thất bại — nó là kênh quan trọng nhất để hệ thống học có kỷ luật.
Một hệ thống không bao giờ gặp phản ví dụ thường là một hệ thống không được kiểm tra.

![Tinh chỉnh dựa trên phản ví dụ: phản ví dụ được ghi nhận có provenance → đánh giá mức độ bác bỏ → tinh chỉnh/thu hẹp ranh giới giả thuyết → cập nhật sổ cái (superseded) → phản ví dụ trở thành âm tính khó cho vòng học sau.](figures/generated/ch08-counterexample-refinement.pdf)

> ⚠️ **"Chưa thấy phản ví dụ" không phải "không có phản ví dụ".**
> Đây là hệ quả của OWA: vắng mặt bằng chứng bác bỏ không phải bằng chứng vắng mặt bác
> bỏ. Một giả thuyết được hỗ trợ bởi 100 ví dụ thuận vẫn có thể sai trước phản ví dụ
> thứ 101.

> 🖊 **Tự kiểm tra 7:** Giả thuyết "mọi RateOfChangeApplication đều có
> withRespectTo Time" đã được chấp nhận. Bạn nhận được một quan sát mới: một ứng dụng
> "tốc độ thay đổi nhiệt lượng theo khối lượng" — withRespectTo = Mass. Hãy vẽ quy
> trình tinh chỉnh (5 bước ở trên) cho tình huống này: phản ví dụ bác bỏ toàn bộ hay
> chỉ một phần? Giả thuyết tinh chỉnh sẽ như thế nào? Và bước nào trong quy trình đảm
> bảo việc sửa này không làm hỏng các kết luận đã có trong sổ cái?

### 8.42.3 Tiến hóa ontology có kỷ luật

Phản ví dụ lặp lại ở một vùng ranh giới là tín hiệu: ontology quá thô. Ví dụ: nếu hệ
thống liên tục nhầm lẫn AverageRateOfChange với InstantaneousRateOfChange, đó là bằng
chứng rằng cần hai con riêng. Tiến hóa ontology là một quyết định quản trị, không phải
một phát hiện tự động — và nó mở đường cho hệ thống tri thức sống (Ch10).

## 8.43 Phép loại suy Phương pháp Khoa học

Có một sự tương ứng sâu sắc giữa quy trình học quy nạp của hệ thống và phương pháp
khoa học:

| Phương pháp khoa học | Hệ thống học quy nạp |
|----------------------|----------------------|
| Quan sát hiện tượng | Thu nhận và tích hợp (Ch7) |
| Hình thành giả thuyết | Sinh CandidateMechanismHypothesis (§8.19) |
| Dự đoán kiểm chứng được | Counterfactual tests, cross-domain tests (§8.26–27) |
| Thí nghiệm | Đánh giá trên dữ liệu tách riêng (§8.10) |
| Phản ví dụ | Tinh chỉnh giả thuyết (§8.42) |
| Xuất bản có kiểm duyệt | Quản trị + ghi sổ có provenance (Ch6) |
| Tái lập | Chạy lại pipeline với cùng dữ liệu + phiên bản (Ch7) |

Phép loại suy này không phải trang trí: nó nhắc hệ thống rằng tri thức quy nạp luôn
dự kiến có thể bị bác bỏ — và đó là đặc điểm, không phải lỗi.

## 8.44 Ca thất bại: Khi học quy nạp sai

Để hiểu đầy đủ ranh giới, hãy xem một ca thất bại điển hình — hệ thống làm mọi thứ sai.

**Bối cảnh:** Hệ thống chưa có tầng tri thức luận. Nhà phát triển gộp toàn bộ đồ thị
thu nhận được (Ch7) vào một tập dữ liệu, chia ngẫu nhiên train/test, huấn luyện một mô
hình nhúng, và đạt MRR ấn tượng.

**Chuỗi sai lầm:**

1. **Chia ngẫu nhiên** → rò rỉ thực thể: các ứng dụng cùng cơ chế xuất hiện ở cả train
   lẫn test (§8.10).
2. **Không lọc echo** → các nguồn sao chép nhau lặp lại cùng một phát biểu ở cả hai
   phía (§8.25).
3. **Không kiểm tra counterfactual** → mô hình học lối tắt từ vựng "tốc độ thay đổi"
   (§8.26).
4. **Viết nhãn dự đoán thẳng vào đồ thị** → bỏ qua CandidateClaim và quản trị (§8.29).
5. **Dùng độ tin cậy PCA của quy tắc khai phá như độ tin cậy tri thức luận** → xung
   đột thuật ngữ (§8.22).
6. **Huấn luyện lại trên dự đoán của chính mình** → vòng phản hồi tự củng cố, model
   collapse (§8.34).
7. **Chèn tiên đề học được vào ontology** → blast radius không được đánh giá, suy diễn
   toàn đồ thị bị nhiễm (§8.41).

**Kết quả:** hệ thống tự tin sai trên toàn diện — điểm benchmark cao, hiểu cơ chế bằng
không. Bài học: mỗi bước trong kiến trúc lai (§8.24) tồn tại để chặn một kiểu sai lầm
cụ thể; bỏ bước nào, sai lầm đó quay lại.

## 8.45 Ca giải thích: Vì sao giả thuyết này được đề xuất?

Một giả thuyết cơ chế được đề xuất cho con người xem xét phải mang theo lời giải thích
rõ ràng. Ví dụ:

> **Giả thuyết H-104 (CandidateMechanismHypothesis):** "Vận tốc, dòng điện và tăng
> trưởng dân số có thể là các ứng dụng của cùng một cơ chế trừu tượng."
>
> **Vì sao mô hình đề xuất:** cả ba subgraph có cùng mẫu vai trò — một Quantity, một
> Operation=Derivative, một WithRespectTo=Time, một Result. Độ tương tự cấu trúc trung
> bình 0.91 giữa các cặp (cao hơn mọi cặp cơ chế khác trong đồ thị).
>
> **Kiểm tra đã làm:** cross-domain test (train cơ học+điện tử, test kinh tế) đạt; hai
> counterfactual tests (đổi WithRespectTo, đổi Operation) cho phản ứng đúng.
>
> **Bằng chứng nguồn:** ba nguồn độc lập (A, B, C) — không echo nhau (Ch7).
>
> **Giả thuyết cạnh tranh:** H-105: ba ứng dụng thuộc *họ* cơ chế, phân biệt tức thời
> vs rời rạc. Bằng chứng văn bản hiện phân vân giữa H-104 và H-105.
>
> **Bất định:** mô hình 0.82 (calibrated); bằng chứng nguồn trung bình; xung đột chưa
> phát hiện.
>
> **Provenance:** mô hình GNN v1.2, dữ liệu KG-2026.08 (source-split), thời điểm
> 2026-08-30.

Lời giải thích này cho con người mọi thứ cần để quyết định — và cho thấy giả thuyết
vẫn là ứng viên, chưa phải tri thức.

## 8.46 Học máy không đảm bảo điều gì

Để kết thúc phần nội dung, một bản liệt kê rõ ràng — ranh giới cuối cùng của học quy
nạp trong hệ thống tri thức:

**Học máy không đảm bảo:**

- **Chân lý:** điểm cao ≠ đúng. (Oversmoothing, lối tắt, nhiễu đều có thể đánh lừa.)
- **Cơ chế nhân quả:** mô hình học tương quan, không học nhân quả. Cấu trúc lặp lại
  không phải quan hệ nhân quả.
- **Tính đúng của ontology:** mô hình không biết ontology của bạn có đúng không.
- **Định danh:** tương tự hình học không phải định danh (Ch3).
- **Tính phổ quát:** quy luật học trên một miền không đảm bảo đúng miền khác.
- **Độc lập bằng chứng:** học trên dữ liệu không tạo ra bằng chứng độc lập.
- **Không thiên vị:** dữ liệu huấn luyện mang thiên vị của nguồn (Ch7).
- **Tổng quát hóa chéo miền:** chỉ được chứng minh bằng thử nghiệm chéo miền, không
  phải mặc định.

Những "không đảm bảo" này không phải là điểm yếu cần khắc phục — chúng là bản chất
của quy nạp: tri thức quy nạp là tri thức có thể sai, và hệ thống có kỷ luật là hệ
thống vận hành theo đúng bản chất đó: đề xuất, đánh giá, quản trị, và sẵn sàng sửa sai.

## 8.47 Kỷ luật Nguồn gốc và Nghiên cứu Hiện tại

### 8.47.1 Source-first

Mọi giả thuyết học được đều có nguồn gốc từ dữ liệu — và dữ liệu đến từ nguồn (Ch7).
Kỷ luật source-first của sách áp dụng nguyên vẹn: một dự đoán của mô hình chỉ đáng tin
khi các nguồn dưới nó được đăng ký, xác minh, và truy nguyên (source_index.json,
research notes). Không có nguồn được xác minh, không có dữ liệu huấn luyện đáng tin.

### 8.47.2 Nghiên cứu hiện tại

Học quy nạp trên đồ thị là một lĩnh vực đang phát triển nhanh. Các kết quả mới — GNN
quy nạp tốt hơn, benchmark mới, hiểu biết về lối tắt tốt hơn — xuất hiện liên tục. Sách
giữ kỷ luật: chương này dạy các nguyên tắc ổn định (OWA, ranh giới dự đoán/suy dẫn,
đánh giá, provenance) dựa trên các nguồn đã đăng ký; các phát triển mới phải được đăng
ký nguồn trước khi được đưa vào (quy tắc source → contract → manuscript → test của
CLAUDE.md).

## 8.48 Các Kiểu Hỏng hóc và Bảng Tóm tắt

### 8.48.1 Các kiểu hỏng hóc của học quy nạp

| # | Kiểu hỏng hóc | Tín hiệu phát hiện | Phục hồi |
|---|---------------|--------------------|----------|
| 1 | Rò rỉ thực thể | Test accuracy đột biến cao so với nguồn tách | Source/entity split |
| 2 | Rò rỉ thời gian | Mô hình "dự đoán" quá khứ quá tốt | Temporal split |
| 3 | Echo trong dữ liệu | Cùng phát biểu lặp ở nhiều nguồn (Ch7) | Lọc echo trước khi huấn luyện |
| 4 | Học lối tắt | Cross-domain test sụp đổ | Counterfactual test, hard negative |
| 5 | Âm tính giả tràn lan | Mô hình đánh thấp các bộ ba đúng hiếm | Chọn thực thể thay thế thông minh |
| 6 | Oversmoothing | Thêm lớp làm accuracy giảm | Giảm số lớp, thêm residual |
| 7 | Mất phân biệt quan hệ | Gộp quan hệ làm mất vai trò | R-GCN relation-specific |
| 8 | Tự tin quá mức | Calibration đo được lệch lớn | Temperature scaling |
| 9 | Vòng phản hồi | Dữ liệu mới ngày càng giống dự đoán cũ | Phân biệt model-generated, kiểm soát |
| 10 | Model collapse | Đa dạng tri thức suy giảm | Chặn dữ liệu tái sinh không kiểm soát |
| 11 | Xung đột thuật ngữ | "Confidence" bị dùng hai nghĩa | Thuật ngữ đầy đủ, ModelAssessment |
| 12 | Ghi đè tri thức | Mô hình điểm cao phủ nhận claim Accepted | Quy trình xung đột Ch6 |
| 13 | Chèn tiên đề tự động | Suy diễn toàn đồ thị thay đổi bất ngờ | Blast radius + quản trị |

### 8.48.2 Bảng tóm tắt phân biệt trung tâm

| Phân biệt | Không được nhầm với |
|-----------|---------------------|
| Dự đoán (prediction) | Suy dẫn (entailment) |
| Điểm số (score) | Xác suất chân lý |
| Tương tự (similarity) | Đồng nhất (identity) |
| Mẫu (pattern) | Cơ chế (mechanism) |
| Nhúng (embedding) | Thực thể (entity) |
| Cụm (cluster) | Lớp ontology (class) |
| Độ tin cậy khai phá quy tắc | Độ tin cậy tri thức luận |
| Provenance huấn luyện | Bằng chứng |
| Giải thích mô hình | Bằng chứng phát biểu |
| Dữ liệu huấn luyện | Sự thật |

## 8.49 Hồ sơ Thí nghiệm Bị Hoãn (Experiment Backlog)

Học quy nạp thực nghiệm trên đồ thị cơ chế — huấn luyện mô hình, đo MRR, so sánh các
kiến trúc — cần một bộ dữ liệu được xây dựng và quản trị. Trong phạm vi cuốn sách hiện
tại, các thí nghiệm này được ghi vào hồ sơ và **hoãn đến BOOK v0.1**:

- **EXP-8-1:** So sánh TransE / DistMult / ComplEx trên đồ thị cơ chế (MRR, Hits@10,
  filtered)
- **EXP-8-2:** Ảnh hưởng của tỉ lệ âm tính giả đến chất lượng dự đoán
- **EXP-8-3:** Cross-domain test: train cơ học + điện tử → test kinh tế
- **EXP-8-4:** Counterfactual tests cho phân biệt Derivative / FiniteDifference
- **EXP-8-5:** GNN quy nạp với thực thể OOV mới (GrowthRate chưa từng thấy)
- **EXP-8-6:** Rule mining (AMIE+) so với embeddings cho phát hiện cơ chế
- **EXP-8-7:** Hiệu chuẩn mô hình phân lớp cơ chế (ECE, temperature scaling)
- **EXP-8-8:** Ảnh hưởng của echo source đến điểm benchmark

Mỗi thí nghiệm khi thực hiện phải kèm: dữ liệu (có provenance), mô hình + phiên bản,
quy tắc chia tách, quy ước đánh giá, và kết quả so sánh được ghi vào sổ tay thí nghiệm.

## 8.50 Bậc Năng lực Cuối Chương

Kiểm tra năng lực sau khi đọc xong chương:

| Bậc | Năng lực | Tự kiểm tra |
|-----|----------|-------------|
| 1 | Phân biệt suy diễn / quy nạp / giả định / dự đoán | Cho một câu, gọi đúng phạm trù |
| 2 | Giải thích OWA và hệ quả cho học máy | "Vì sao mẫu âm không phải bộ ba sai?" |
| 3 | Đọc và so sánh TransE / DistMult / ComplEx | Chọn mô hình cho quan hệ bất đối xứng |
| 4 | Giải thích transductive vs inductive, OOV | "Vì sao KGE chuẩn không xử lý thực thể mới?" |
| 5 | Giải thích message passing, R-GCN, oversmoothing | Vẽ sơ đồ truyền thông điệp cho một nút |
| 6 | Giải thích nút vs subgraph representation | "Vì sao vector nút không phải vector ứng dụng?" |
| 7 | Sinh giả thuyết cơ chế có kỷ luật | Mô tả 7 bước pipeline §8.19 |
| 8 | Phân biệt độ tin cậy khai phá quy tắc với Ch6 | Cho hai con số, nói rõ ngữ nghĩa từng cái |
| 9 | Thiết kế đánh giá không rò rỉ | Chọn split cho đồ thị có echo + thời gian |
| 10 | Giải thích học lối tắt và counterfactual test | Thiết kế một test cho một mô hình cụ thể |
| 11 | Giải thích vòng phản hồi và model collapse | "Vì sao huấn luyện lại trên dự đoán không xác nhận?" |
| 12 | Vận hành kiến trúc lai | Vẽ pipeline ML → lọc → tri thức luận → quản trị |
| 13 | Quyết định "không dùng ML" | Cho một tình huống, quyết định và lý do |
| 14 | Trình bày giới hạn học máy | Liệt kê 8 điều học máy không đảm bảo |

## 8.51 Cầu nối Chương 9

Chương 8 xây dựng khả năng *sinh tri thức ứng viên* từ đồ thị. Điều này mở ra một câu
hỏi lớn hơn: khi hệ thống có nhiều tri thức — tượng trưng lẫn thống kê, được chấp nhận
lẫn ứng viên — làm sao người dùng **hỏi và lấy lại** tri thức đó một cách hiệu quả?
Làm sao trả lời một câu hỏi tự nhiên bằng cách kết hợp truy vấn SPARQL, suy diễn, và
các mô hình học máy — ví dụ, "lạm phát và vận tốc có cùng cơ chế không, và bằng chứng
là gì?"

Đó là nội dung của **Chương 9 — Truy vấn, Hỏi đáp và GraphRAG** (chưa được xây dựng
trong cuốn sách này): nơi mọi khả năng của tám chương trước hội tụ thành một giao diện
hỏi đáp. Nhưng trước khi sang chương đó, hãy dừng lại và kiểm tra: chương này đã đặt
ranh giới đúng chưa — hệ thống *đề xuất*, *đánh giá*, *quản trị* — và không bao giờ
*khẳng định* một điều mà nó chỉ mới *học được*.

![Kiến trúc toàn phần tám chương: từ đồ thị cơ bản (Ch1–2) qua định danh (Ch3), ngữ nghĩa (Ch4), suy diễn (Ch5), tri thức luận (Ch6), thu nhận (Ch7), đến học quy nạp (Ch8). Mỗi nấc thêm một năng lực mới, Ch8 là nấc hiện tại.](figures/generated/ch08-full-stack.pdf)

Chuỗi phân biệt trung tâm, một lần cuối: tương tự ≠ đồng nhất; dự đoán ≠ suy dẫn; điểm
cao ≠ chân lý; mẫu học được ≠ tri thức được chấp nhận.

## Thuật ngữ đã gặp trong chương này

| Thuật ngữ | Nghĩa ngắn | Học chi tiết |
|-----------|-----------|--------------|
| Deduction (suy diễn) | Hệ quả tất yếu từ quy tắc + tiền đề | §8.1.1 |
| Induction (quy nạp) | Tổng quát hóa mẫu từ quan sát; có thể sai | §8.1.2 |
| Abduction (giả định) | Chọn lời giải thích tốt nhất | §8.1.3 |
| Prediction (dự đoán) | Điểm số của mô hình cho cấu trúc khả dĩ | §8.1.4 |
| Symbolic vs Statistical knowledge | Tường minh vs học được từ dữ liệu | §8.2 |
| Feature representation | Đặc trưng thiết kế thủ công | §8.4 |
| Representation learning | Học vector từ dữ liệu | §8.4 |
| Embedding | Vector học được; không phải thực thể | §8.4 |
| Knowledge Graph Embedding (KGE) | ε, ρ + hàm chấm điểm f(h,r,t) | §8.5 |
| Scoring function | Hàm số hóa mức độ hợp lý của bộ ba | §8.5 |
| TransE | h + r ≈ t; quan hệ là phép tịnh tiến | §8.5.2 |
| Bilinear model (DistMult) | ⟨h, r, t⟩; đối xứng | §8.6.1 |
| ComplEx | Nhúng phức, tích Hermitian; bất đối xứng | §8.6.2 |
| Inductive bias | Giả định cấu trúc của họ mô hình | §8.6.3 |
| Negative sampling | Tạo mẫu âm bằng thay thế ngẫu nhiên | §8.7 |
| False negative | Bộ ba thật bị dùng làm mẫu âm | §8.7.3 |
| Link prediction | Xếp hạng bộ ba ứng viên còn thiếu | §8.8 |
| MRR / Hits@K | Đo vị trí của câu trả lời đúng | §8.9 |
| Filtered evaluation | Loại bộ ba đúng đã biết khỏi xếp hạng | §8.9.3 |
| Data leakage | Thông tin test lọt vào train | §8.10, §8.25 |
| Temporal / Source leakage | Rò rỉ theo thời gian / theo nguồn | §8.25 |
| Transductive learning | Dự đoán giữa thực thể đã biết | §8.11 |
| Inductive KG learning | Tổng quát hóa tới thực thể mới | §8.11 |
| OOV entity | Thực thể không có vector học sẵn | §8.12 |
| Message passing | message → aggregate → update | §8.14 |
| GNN | Mạng nơ-ron tính theo cấu trúc đồ thị | §8.13 |
| R-GCN | Biến đổi riêng theo loại quan hệ | §8.15 |
| Oversmoothing | Biểu diễn hội tụ khi xếp nhiều lớp | §8.16 |
| Subgraph representation | Pooling/readout cho toàn bộ subgraph | §8.17 |
| Structural similarity | Bằng chứng đa chiều; tương tự ≠ đồng nhất | §8.18 |
| Cosine similarity | cos(a,b) = (a·b)/(‖a‖·‖b‖) | §8.18.2 |
| CandidateMechanismHypothesis | Giả thuyết cơ chế ứng viên (BOOK-DEFINED) | §8.19 |
| Invariant / incidental structure | Bất biến / ngẫu nhiên khi trừu tượng hóa | §8.21 |
| Rule induction (AMIE+) | Quy tắc đường đi r1∧r2→r3 | §8.22 |
| Rule-mining confidence (PCA) | Tần suất dưới giả định PCA; ≠ Ch6 | §8.22.2 |
| Hybrid pipeline | ML sinh ứng viên → lọc → tri thức luận (BOOK-DEFINED) | §8.24 |
| Cross-domain generalization | Nhận cơ chế ở miền mới | §8.26 |
| Spurious correlation / shortcut | Học dấu hiệu bề mặt thay vì cơ chế | §8.26 |
| Counterfactual test | Đổi cấu trúc, kiểm tra phản ứng mô hình | §8.27 |
| Hard negative | Mẫu âm gần ranh giới | §8.27 |
| Clustering | Gom nhóm khám phá; cụm ≠ lớp | §8.28 |
| Classification | Gán nhãn ứng viên | §8.29 |
| Calibration | Điểm số khớp tần suất đúng | §8.29.2 |
| ModelAssessment | Bọc điểm số với ngữ nghĩa + provenance (BOOK-DEFINED) | §8.30 |
| Training provenance | wasGeneratedBy TrainingOrInferenceActivity | §8.30 |
| Self-reinforcing feedback | Dự đoán quay lại làm dữ liệu | §8.34 |
| Model collapse | Đa dạng suy giảm khi huấn luyện trên dữ liệu tái sinh | §8.34 |
| Path-based explanation | Giải thích theo đường đi trong đồ thị | §8.35 |
| CandidateAxiom | Tiên đề ứng viên chờ đánh giá | §8.41 |
| Blast radius | Tập kết luận bị ảnh hưởng nếu tiên đề sai | §8.41 |
| Counterexample | Quan sát bác bỏ giả thuyết | §8.42 |
| Ontology evolution | Tinh chỉnh ontology có quản trị | §8.42 |

## Tài liệu tham khảo

- Knowledge Graphs (Hogan et al.), Inductive Knowledge [@hogan-inductive]
- Translating Embeddings for Modeling Multi-relational Data (Bordes et al., TransE) [@bordes-transe-2013]
- Embedding Entities and Relations for Learning and Inference in Knowledge Bases (Yang et al., DistMult) [@yang-distmult-2015]
- Complex Embeddings for Simple Link Prediction (Trouillon et al., ComplEx) [@trouillon-complex-2016]
- Modeling Relational Data with Graph Convolutional Networks (Schlichtkrull et al., R-GCN) [@schlichtkrull-rgcn-2018]
- Fast Rule Mining in Ontological Knowledge Bases with AMIE+ (Galárraga et al.) [@galarraga-amie-2015]
- Inductive Relation Prediction by Subgraph Reasoning (Teru, Denis & Hamilton, GraIL) [@teru-grail-2020]
- A Review of Relational Machine Learning for Knowledge Graphs (Nickel et al.) [@nickel-relational-ml-2016]
- Distributed Representations of Words and Phrases and their Compositionality (Mikolov et al., negative sampling) [@mikolov-negativesampling-2013]
- Deeper Insights into Graph Convolutional Networks for Semi-Supervised Learning (Li et al., oversmoothing) [@li-oversmoothing-2018]
- Shortcut Learning in Deep Neural Networks (Geirhos et al.) [@geirhos-shortcut-2020]
- On Calibration of Modern Neural Networks (Guo et al.) [@guo-calibration-2017]
- AI models collapse when trained on recursively generated data (Shumailov et al.) [@shumailov-collapse-2024]
- Graph Representation Learning (Hamilton) [@hamilton-grl-2020]
- PROV-O: The PROV Ontology [@prov-o]
- Shapes Constraint Language (SHACL) [@w3c-shacl]