# Chương 7 — Thu nhận và Tích hợp Tri thức

> **Định hướng chương**
>
> **Câu hỏi trung tâm:** Chương 6 giả định các phát biểu đã *nằm sẵn* trong sổ cái với
> provenance đầy đủ. Nhưng tri thức mới đến từ đâu? Làm sao một hệ thống lấy nội dung từ
> nhiều nguồn — giáo trình, cơ sở dữ liệu, API — biến nó thành phát biểu có cấu trúc,
> nhận diện "hai nguồn nói về cùng một thứ", gióng lược đồ, gỡ trùng lặp, và đưa vào sổ
> cái mà không phá hỏng đồ thị đã được quản trị?
>
> **Vì sao quan trọng:** Sáu chương trước xây dựng đồ thị (Ch1–2), định danh (Ch3), ngữ
> nghĩa (Ch4), suy diễn/xác nhận (Ch5), và tầng tri thức luận (Ch6). Nhưng toàn bộ giả
> định rằng dữ liệu đã *sạch, đã có sẵn, đã về đúng chỗ*. Trong thực tế, knowledge graph
> được nuôi bằng các **đường ống thu nhận và tích hợp** (acquisition & integration
> pipelines): nhiều nguồn dị dạng, trùng lặp, lược đồ khác nhau, giá trị mâu thuẫn nhau.
> Nếu không có một quy trình có kỷ luật, đồ thị quản trị sạch sẽ của Chương 6 bị nhiễm
> bởi dữ liệu chưa xác minh, chưa khử trùng, chưa truy nguyên.
>
> **Bạn sẽ hiểu:**
>
> - Ranh giới giữa **Thu nhận** (đưa thông tin vào hệ thống) và **Tích hợp** (hợp nhất,
>   đối chiếu, xác nhận trước khi ghi sổ)
> - Đường ống trung tâm: Đăng ký nguồn → Quan sát → Trích xuất → Chuẩn hóa → Cấu trúc
>   hóa → Nghị quyết định danh → Gióng lược đồ → Khử trùng → Cổng SHACL → Ghi sổ
> - Nghị quyết định danh (entity resolution): sinh ứng viên khác chấm điểm; mô hình
>   Fellegi–Sunter với ba vùng quyết định
> - Gióng lược đồ (schema alignment) và ánh xạ: Direct Mapping mặc định so với ánh xạ
>   tùy biến R2RML
> - Thu nạp lũy đẳng (idempotent ingestion) và content hash — vì sao chạy lại không tạo
>   trùng lặp
> - Hợp lệ hình dạng (SHACL conformance) khác Được chấp nhận (Accepted)
> - Phát hiện xung đột, kết quả hợp nhất, ghi sổ trước — nối liền quản trị Chương 6
> - Lineage (lần theo "từ đâu đến?") khác Evidence (lý do "vì sao tin?")
> - Bảy bất biến I1–I7 bảo vệ đường ống
>
> **Tiên quyết:** Chương 3 (ownership identity, owl:sameAs, n-ary), Chương 5
> (conformance ≠ truth, SHACL), Chương 6 (epistemic model, Claim, governance, Claim
> Ledger, provenance).
>
> **Bản đồ khái niệm:**
>
> Nguồn dị dạng → **Thu nhận** (Quan sát → Trích xuất → Chuẩn hóa → Cấu trúc hóa) →
> **Tích hợp** (Nghị quyết định danh → Gióng lược đồ → Khử trùng → Kiểm soát xung đột)
> → **Ghi sổ** (Claim Ledger) → Chiếu hình (Canonical Knowledge View)

## 7.0 Mở đầu: Ba nguồn, một khái niệm

Chương 6 dẫn dắt bằng hai con số dân số. Chương 7 mở đầu bằng một tình huống khó hơn:
ba nguồn khác nhau, nói *gần như* cùng một khái niệm, nhưng không tự hiển nhiên rằng
chúng nói về cùng một thứ.

**Nguồn A** — giáo trình Giải tích (calculus textbook), Chương 3, định nghĩa đạo hàm:

> "Đạo hàm của hàm số f tại điểm x — ký hiệu f′(x) — là giới hạn của tỉ số
> [f(x+h) − f(x)]/h khi h tiến về 0. Đạo hàm đo tốc độ thay đổi tức thời của f."

**Nguồn B** — giáo trình Cơ học (mechanics textbook), Chương 2, định nghĩa vận tốc:

> "Vận tốc tức thời là đạo hàm của quãng đường theo thời gian: v = ds/dt. Nói cách khác,
> vận tốc là tốc độ thay đổi của vị trí theo thời gian."

**Nguồn C** — giáo trình Điện tử (electronics textbook), Chương 5, dòng điện qua tụ:

> "Dòng điện qua tụ điện bằng tốc độ thay đổi của điện áp theo thời gian: i = C·(dV/dt).
> Khi điện áp không đổi, dòng bằng 0: tụ chặn dòng một chiều."

Ba phát biểu nhìn bề ngoài giống nhau — đều nói về "tốc độ thay đổi theo thời gian".
Nhưng hệ thống không được phép vội kết luận. Hãy hỏi ba câu:

1. **Định danh:** Nguồn A nói về `f′(x)` (đạo hàm hàm số), nguồn B nói về `v = ds/dt`
   (vận tốc một chiều), nguồn C nói về `i = C·dV/dt` (dòng qua tụ). Chúng có nói về *cùng
   một thực thể* không?
2. **Lược đồ:** Nếu cả ba đều mô tả "một đại lượng bằng tốc độ thay đổi của đại lượng
   khác", thì thuộc tính "tốc độ thay đổi" trong ba nguồn có *cùng ngữ nghĩa* không?
3. **Trùng lặp và xung đột:** Nếu cả hai nguồn cùng khẳng định một điều, ghi làm mấy
   phát biểu? Nếu giá trị khác nhau, giữ cả hai hay xử lý thế nào?

Câu trả lời ngây thơ — "chúng giống nhau nên gộp lại" — chính là nơi knowledge graph bị
hỏng. Nếu hệ thống vội nối `owl:sameAs` giữa "đạo hàm hàm số" (A) và "dòng qua tụ" (C)
chỉ vì cùng cụm từ "tốc độ thay đổi", hậu quả lan truyền toàn đồ thị như Chương 3 đã cảnh
báo (§3.2.4).

Chương 7 xây dựng **đường ống thu nhận và tích hợp**: một quy trình có kỷ luật để đưa ba
nguồn này vào hệ thống, biến chúng thành phát biểu có cấu trúc, quyết định *có hay không*
chúng là cùng một khái niệm — và kết nối kết quả với quản trị của Chương 6.

> 🖊 **Tự kiểm tra:** Trước khi đọc tiếp, hãy tự trả lời: theo bạn, "tốc độ thay đổi" ở
> nguồn A, B, C có nên trỏ về cùng một nút hay không? Ghi lại lý do của bạn. Cuối chương
> (§7.32) bạn sẽ đối chiếu với cách hệ thống quyết định.

## 7.1 Đường ống trung tâm: Từ nguồn đến sổ cái

### Trực giác

Mọi tri thức trong hệ thống đều đến từ một nguồn nào đó. Đường ống trung tâm (central
pipeline) là mô tả *có thứ tự* của việc nội dung nguồn được biến đổi dần thành phát biểu
được quản trị. Giống như một nhà máy lọc dầu: nguyên liệu thô đi qua nhiều công đoạn,
mỗi công đoạn có kiểm soát, và chỉ sản phẩm đạt chuẩn mới vào kho thành phẩm.

### Cơ chế

Đường ống gồm hai nửa, tương ứng với hai câu hỏi khác nhau:

![Đường ống trung tâm: Thu nhận (đăng ký nguồn → quan sát → trích xuất → chuẩn hóa → cấu trúc hóa) rồi Tích hợp (nghị quyết định danh → gióng lược đồ → khử trùng → cổng SHACL → xung đột → ghi sổ).](figures/generated/ch07-central-pipeline.pdf)

```
                 THU NHẬN (Acquisition)                      TÍCH HỢP (Integration)
  ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌───────────┐
  │ Đăng ký   │ → │ Quan sát  │ → │ Trích     │ → │ Chuẩn     │ → │ Cấu trúc  │
  │ nguồn     │   │ & mẩu     │   │ xuất      │   │ hóa       │   │ hóa       │
  └───────────┘   └───────────┘   └───────────┘   └───────────┘   └───────────┘
   Source          Source          Extraction      Canonical       Graph-shaped
   Artifact        Fragment        → bản ghi ứng   form           candidate
                                                   viên                        │
                       ┌─────────────────────────────────────────┐              │
                       ▼               TÍCH HỢP (tiếp)            │              ▼
               ┌───────────┐   ┌───────────┐   ┌───────────┐   ┌──────────┐
               │ Nghị      │ → │ Gióng     │ → │ Khử       │ → │ Cổng     │
               │ quyết     │   │ lược đồ   │   │ trùng     │   │ SHACL    │
               │ định danh │   │ & ánh xạ  │   │ & chuẩn   │   │ (hợp lệ) │
               └───────────┘   └───────────┘   └───────────┘   └──────────┘
                                                        │              │
                                               ┌─────────┴──────────┐   │
                                               ▼                    ▼   ▼
                                     ┌──────────────┐   ┌────────────────────────┐
                                     │ Xung đột &   │ → │ Ghi sổ Claim Ledger &  │
                                     │ quyết định   │   │ chiếu hình              │
                                     │ tích hợp     │   │ (Canonical View)        │
                                     └──────────────┘   └────────────────────────┘
```

Mỗi giai đoạn có một "vật phẩm" đầu ra (artifact) đi kèm:

| # | Giai đoạn | Đầu vào | Đầu ra | Mục |
|---|-----------|---------|--------|-----|
| 1 | Đăng ký nguồn | Nguồn thế giới thực | `Source Artifact` (bản ghi có IRI) | §7.3 |
| 2 | Quan sát | Source Artifact | `Source Fragment` + `Observation` | §7.4 |
| 3 | Trích xuất | Observation | bản ghi ứng viên + `Extraction Activity` | §7.5 |
| 4 | Chuẩn hóa | bản ghi thô | bản ghi dạng chính tắc | §7.7 |
| 5 | Cấu trúc hóa | bản ghi chính tắc | bộ ba RDF ứng viên | §7.8 |
| 6 | Nghị quyết định danh | cụm bộ ba | quyết định "cùng thực thể?" | §7.9–7.10 |
| 7 | Gióng lược đồ & ánh xạ | lược đồ nguồn | correspondence + mapping | §7.11–7.12 |
| 8 | Khử trùng & chuẩn hóa ghi | các bản ghi | một bản ghi sạch trùng | §7.13–7.14 |
| 9 | Cổng SHACL | bộ ba ứng viên | báo cáo hợp lệ | §7.15 |
| 10 | Xung đột & quyết định | bộ ba hợp lệ | quyết định: accept/reject/review | §7.16–7.17 |
| 11 | Ghi sổ | quyết định + bộ ba | mục Claim Ledger | §7.18 |

Đường ống này không phải là một chuẩn W3C — nó là **kiến trúc do sách xây dựng**
(BOOK-DEFINED), ghép các chuẩn có thật (R2RML, CSVW, Direct Mapping, Fellegi–Sunter,
SHACL, PROV-O) vào một khung dạy học thống nhất. Mỗi bước sẽ được gắn với chuẩn/khái
niệm tương ứng trong các mục sau.

### Ứng dụng

Với ba nguồn A, B, C trong §7.0: mỗi nguồn được đăng ký thành một Source Artifact; mỗi
định nghĩa trích ra một Observation; các dòng tri thức song song đi qua các giai đoạn
chung, gặp nhau ở *các bước tích hợp* nơi hệ thống quyết định mối quan hệ giữa chúng.

> 🖊 **Tự kiểm tra:** Điền vào bảng trên một giai đoạn bạn chọn: đầu vào và đầu ra là
> gì, và nếu giai đoạn đó bị bỏ qua thì hậu quả gì?

## 7.2 Thu nhận khác Tích hợp

### Trực giác

Hai người làm hai việc khác nhau: một người **mang hàng về kho**, người kia **sắp xếp,
kiểm tra, đối chiếu hàng** trước khi khóa sổ. Trộn hai việc này thành một sẽ sinh hỗn
loạn: hàng mang về chưa kiểm tra đã bị đưa ra bán.

### Cơ chế

**Thu nhận (Acquisition)** trả lời câu hỏi "làm sao đưa thông tin vào hệ thống?" — đọc
nguồn, trích xuất, chuẩn hóa, cấu trúc hóa thành **tri thức ứng viên** (candidate
knowledge) có provenance. Thu nhận *không* quyết định ai đúng, không gỡ trùng, không
gióng lược đồ — nó chỉ làm cho nội dung nguồn trở nên *có cấu trúc và truy nguyên được*.

**Tích hợp (Integration)** trả lời câu hỏi "làm sao hợp nhất nhiều luồng thành một bức
tranh nhất quán?" — nhận diện xem hai mảnh tri thức có nói về cùng một thứ (nghị quyết
định danh), gióng các lược đồ khác nhau (schema alignment), gỡ trùng lặp, kiểm soát xung
đột, và quyết định đưa gì vào sổ cái [@lenzerini-2002] [@hogan-creation-enrichment].

Vì sao phải tách? Vì hai câu hỏi có **tiêu chí thành công khác nhau**:

- Thu nhận đo bằng **độ bao phủ và độ chính xác của trích xuất**: có lấy được hết nội
  dung đáng lấy không? Bản ghi có đúng với nguồn không?
- Tích hợp đo bằng **độ nhất quán và độ tin cậy của sổ cái**: sau khi hợp nhất, có còn
  trùng lặp không? Quyết định định danh/lược đồ có bằng chứng và được ghi lại không?

Một lỗi tinh tế: coi "thu nhận xong = tri thức có trong hệ thống". Sai. Thu nhận chỉ sản
xuất **ứng viên** (candidate). Một bản ghi trích từ nguồn C — "dòng = C·dV/dt" — là một
phát biểu ứng viên, chưa được chấp nhận, chưa biết quan hệ với nguồn A/B.

### Ứng dụng

Trục dọc của đường ống §7.1: các giai đoạn 1–5 thuộc Thu nhận; 6–11 thuộc Tích hợp.
Nguồn C đi qua thu nhận y hệt nguồn A/B — nhưng ở tích hợp, số phận của nó được quyết
định bởi bằng chứng, không phải bởi độ trôi chảy của văn bản nguồn.

> ⚠️ **Ngộ nhận phổ biến:** "Hệ thống đã trích xuất được phát biểu từ nguồn → hệ thống
> *biết* điều đó." Sai. Trích xuất tạo ra *tri thức ứng viên*. Trở thành "được biết" đòi
> hỏi cả đường tích hợp + quản trị (Chương 6). Trích xuất và tri thức chấp nhận cách nhau
> một đường ống dài.

## 7.3 Đăng ký nguồn: Source Artifact

### Trực giác

Trước khi đọc một cuốn sách, thư viện ghi vào hệ thống: cuốn này là gì, của ai, bản nào.
Nguồn dữ liệu cũng vậy. Hệ thống không làm việc trực tiếp với "cuốn giáo trình thật
trong giá sách" — nó làm việc với **bản ghi đăng ký** của cuốn sách đó.

### Cơ chế

**Source Artifact** là bản ghi đăng ký của một nguồn trong hệ thống — một entity PROV có
IRI riêng, với siêu dữ liệu: loại nguồn (tài liệu / cơ sở dữ liệu / API), tác giả/đơn vị
phát hành, thời điểm đăng ký, phiên bản, và hồ sơ tin cậy (trust profile) [@prov-o].

Ví dụ đăng ký ba nguồn của chương:

```turtle
src:sourceA  a                    ex:SourceArtifact ;
             ex:sourceKind         ex:Document ;
             ex:title              "Calculus Textbook, 3rd edition" ;
             ex:publisher          ex:CalcPress ;
             ex:registeredAt      "2026-08-30T09:00:00Z"^^xsd:dateTime ;
             ex:sourceVersion      "3.1" ;
             ex:trustProfile       ex:Trust_High .

src:sourceB  a                    ex:SourceArtifact ;
             ex:sourceKind         ex:Document ;
             ex:title              "Mechanics Textbook, 2nd edition" ;
             ex:publisher          ex:MechPress ;
             ex:registeredAt      "2026-08-30T09:05:00Z"^^xsd:dateTime ;
             ex:sourceVersion      "2.4" ;
             ex:trustProfile       ex:Trust_High .

src:sourceC  a                    ex:SourceArtifact ;
             ex:sourceKind         ex:Document ;
             ex:title              "Electronics Textbook, 1st edition" ;
             ex:publisher          ex:ElecPress ;
             ex:registeredAt      "2026-08-30T09:10:00Z"^^xsd:dateTime ;
             ex:sourceVersion      "1.0" ;
             ex:trustProfile       ex:Trust_Medium .
```

Ba điểm quan trọng:

1. **Source Artifact ≠ nguồn thật.** `src:sourceA` là bản ghi *của hệ thống*, không phải
   cuốn sách. Nếu hệ thống đăng ký nhầm thông tin nguồn, lỗi nằm ở bản ghi — và mọi phát
   biểu dẫn tới bản ghi này đều kế thừa sự nhầm lẫn đó.

2. **Đăng ký ≠ đáng tin.** Có IRI và siêu dữ liệu đầy đủ chưa nói lên chất lượng nội
   dung. `Trust_High` là *hồ sơ tin cậy do hệ thống định nghĩa*, không phải sự thật tuyệt
   đối.

3. **Phiên bản nguồn được ghi.** `sourceVersion "3.1"` — vì cùng một cuốn sách, bản in
   khác nhau có thể khác nội dung. Provenance phải chỉ tới đúng bản.

### Ứng dụng

Khi nguồn C sau này bị phát hiện là một "nguồn vọng" (echo source, §7.23), hồ sơ tin cậy
của nó được hạ, nhưng bản ghi đăng ký **không bị xóa** — nó được cập nhật trạng thái,
giống như claim bị Superseded chứ không bị xóa (Chương 6).

> 🖊 **Tự kiểm tra:** Vì sao hệ thống cần đăng ký nguồn thành một bản ghi có IRI, thay vì
> chỉ lưu chuỗi tên "Calculus Textbook"? Gợi ý: nghĩ về hai cuốn sách khác nhau có cùng
> tên, hay hai bản in của cùng một cuốn.

## 7.4 Quan sát và Mẩu nguồn: Source Fragment

### Trực giác

Khi trích dẫn, ta không trích dẫn "cả cuốn sách" — ta trích dẫn một câu, một đoạn, một
định nghĩa. Trong knowledge graph cũng vậy: provenance tới *cả nguồn* là quá thô. Cần
một mức chi tiết đủ để biết chính xác phát biểu dựa trên phần nào của nguồn.

### Cơ chế

**Source Fragment** là một phần con được đánh địa chỉ của một Source Artifact: trang §,
đoạn, bảng, hoặc một phản hồi API. Nó có IRI riêng và chỉ tới nguồn cha [@prov-dm].

**Observation** là dữ liệu thô được thu từ một fragment — câu định nghĩa, con số trong
bảng — *trước khi* được diễn giải. Observation là mỏ neo của provenance: nó ghi "đã thấy
cái gì, ở đâu, khi nào", tách biệt khỏi lớp diễn giải sau đó.

```turtle
src:fragA_3_2  a                  ex:SourceFragment ;
               ex:partOf           src:sourceA ;
               ex:chapter          "3" ;
               ex:section          "3.2" ;
               ex:retrievedAt      "2026-08-30T10:00:00Z"^^xsd:dateTime .

ex:obsA_1      a                  ex:Observation ;
               ex:extractedFrom    src:fragA_3_2 ;
               ex:rawText          "The derivative of f at x is the limit of (f(x+h)-f(x))/h as h approaches 0." ;
               ex:observedAt       "2026-08-30T10:00:30Z"^^xsd:dateTime .
```

Hai điều cần giữ vững:

- **Quan sát ≠ diễn giải.** `ex:obsA_1` chứa *chuỗi văn bản gốc*. Phát biểu "đạo hàm đo
  tốc độ thay đổi" là *diễn giải* — nó xuất hiện ở bước trích xuất (§7.5), có độ tin cậy
  riêng (§7.6).
- **Provenance càng mịn càng tốt.** Một phát biểu của nguồn A dẫn tới `src:fragA_3_2`
  chính xác hơn là dẫn tới `src:sourceA` nói chung. Nếu phát biểu nằm ở §3.2 nhưng
  provenance chỉ nói "từ giáo trình Giải tích", đó là provenance thiếu chính xác.

> ⚠️ **Ngộ nhận phổ biến:** "Ghi provenance là ghi tên nguồn là đủ." Sai. Provenance tới
> `src:sourceA` mà không có `src:fragA_3_2` thì không biết phát biểu dựa trên phần nào —
> không thể kiểm tra, không thể định vị khi cần đối chiếu. Fragment-granular provenance là
> chuẩn tối thiểu.

## 7.5 Trích xuất: Extraction và Extraction Activity

### Trực giác

Đọc hiểu một câu văn rồi ghi ra "ai – quan hệ – cái gì" là một bước *diễn giải*, không
phải sao chép. Trích xuất làm việc này: biến Observation (văn bản thô) thành bản ghi có
cấu trúc. Và vì là diễn giải nên nó *có thể sai* — hệ thống phải ghi lại ai (công cụ nào)
đã làm, làm khi nào.

### Cơ chế

**Extraction** là hoạt động biến mỗi Observation thành một bản ghi ứng viên: nhận diện
thực thể, quan hệ, thuộc tính, và đưa ra một bản ghi trung gian theo một **lược đồ trích
xuất** (extraction schema, §7.27).

Với nguồn A (định nghĩa đạo hàm):

```turtle
ex:recA_1  a              ex:ExtractedRecord ;
           ex:fromObservation ex:obsA_1 ;
           ex:subject     "derivative of f at x" ;
           ex:relation    "measures_rate_of_change_of" ;
           ex:object      "f" ;
           ex:extractionPattern  ex:Pattern_FormalDefinition .
```

**Extraction Activity** là Activity PROV ghi lại *việc thực thi* trích xuất: thời điểm,
agent (phiên bản công cụ trích xuất), và các Observation đã dùng [@prov-o]. Mỗi bản ghi
ứng viên được `wasGeneratedBy` một Extraction Activity:

```turtle
ex:extractActA_1  a       prov:Activity ;
                    prov:startedAtTime  "2026-08-30T10:01:00Z"^^xsd:dateTime ;
                    prov:endedAtTime    "2026-08-30T10:01:02Z"^^xsd:dateTime ;
                    prov:used            ex:obsA_1 ;
                    prov:wasAssociatedWith  ex:Extractor_v2.3 ;

ex:recA_1          prov:wasGeneratedBy   ex:extractActA_1 .
```

Vì sao cần cả bản ghi lẫn activity? Vì một mình bản ghi chỉ nói "có bản ghi này"; còn
activity nói "bản ghi này đến từ công cụ nào, phiên bản nào, lúc nào". Khi phiên bản công
cụ trích xuất đổi (sửa lỗi), mọi bản ghi cũ vẫn truy nguyên tới đúng phiên bản cũ — đây
là nền móng của pipeline versioning (§7.24).

### Ứng dụng

Ba nguồn A, B, C sinh ra ba luồng bản ghi:

| Luồng | Observation | Bản ghi ứng viên | Quan hệ nhận diện |
|-------|-------------|------------------|-------------------|
| A | `ex:obsA_1` (định nghĩa đạo hàm) | `ex:recA_1` | derivative of f → measures rate of change of f |
| B | `ex:obsB_1` (định nghĩa vận tốc) | `ex:recB_1` | velocity → measures rate of change of position |
| C | `ex:obsC_1` (định nghĩa dòng qua tụ) | `ex:recC_1` | electric current → measures rate of change of voltage |

Ba bản ghi đều có dạng "X measures_rate_of_change_of Y" — nhưng đây mới là *bề mặt*.
Tầng tích hợp sẽ quyết định bề mặt trùng này là thật hay chỉ là ngẫu nhiên.

> 🖊 **Tự kiểm tra:** Quan sát (`ex:obsA_1`) và bản ghi (`ex:recA_1`) khác nhau thế nào?
> Điều gì bị thêm vào khi chuyển từ quan sát sang bản ghi?

## 7.6 Độ tin cậy trích xuất: Extraction Confidence

### Trực giác

Cùng một công cụ trích xuất, trích xuất một công thức toán khác trích xuất một câu văn
mơ hồ. Kết quả không đáng tin như nhau. Cần ghi chú "bản ghi này được tạo ra đáng tin
đến đâu *về mặt trích xuất*".

### Cơ chế

**Extraction Confidence** là đánh giá gắn với từng bản ghi về mức độ mà việc trích xuất
đó đáng tin, xét theo phương pháp trích xuất và đặc điểm nội dung nguồn. Nó là bằng chứng
*về việc trích xuất*, không phải bằng chứng về tính đúng của nội dung trích được.

```turtle
ex:extractAssessA_1  a          ex:ExtractionAssessment ;
                     ex:assesses ex:recA_1 ;
                     ex:pattern   ex:Pattern_FormalDefinition ;
                     ex:confidence 0.97 ;
                     ex:rationale  "Formula-type definition, low ambiguity." .
```

Chú ý điểm tinh tế, nối với Chương 6: **độ tin cậy trích xuất ≠ độ tin cậy phát biểu**.
Bản ghi `ex:recC_1` có thể có độ tin cậy trích xuất cao (câu định nghĩa rõ ràng, công
cụ phân tích tốt) — nhưng điều đó không làm cho "dòng qua tụ là rate of change của điện
áp" trở thành *phát biểu được chấp nhận*. Trích xuất tốt chỉ có nghĩa "nội dung nguồn đã
được bắt đúng", không có nghĩa "nội dung đó là true".

Điều này song song với Chương 6: confidence phải nói rõ *đang đánh giá gì* (§6.11). Ở
đây có ba mức khác nhau:

1. **Extraction confidence** — bắt đúng nội dung nguồn chưa (mục này).
2. **Claim confidence** — phát biểu đáng tin thế nào theo bằng chứng (Chương 6).
3. **Source reliability** — nguồn có đáng tin không (hồ sơ tin cậy §7.3).

Ba con số đo ba việc khác nhau; không được cộng/trộn chúng.

> ⚠️ **Ngộ nhận phổ biến:** "Trích xuất đạt độ tin cậy cao → phát biểu đó đúng." Sai.
> Trích xuất cao nghĩa là *văn bản nguồn được bắt chính xác*. Nếu nguồn C nói điều sai, bản
> ghi trích xuất hoàn hảo vẫn là phát biểu sai — chỉ là được trích đúng.

## 7.7 Chuẩn hóa: Normalization

### Trực giác

Hai nguồn viết "v = ds/dt" và "velocity is the derivative of position w.r.t. time".
Bề mặt khác nhau, ý giống nhau. Ngược lại, hai nguồn cùng viết "rate of change" nhưng
một cái nói đạo hàm theo thời gian, cái kia nói đạo hàm theo không gian. Chuẩn hóa đưa
các giá trị về dạng chính tắc để *so sánh được* — nhưng không được làm phẳng mất sự
khác biệt ngữ nghĩa.

### Cơ chế

**Chuẩn hóa (Normalization)** biến đổi giá trị trong bản ghi về dạng chính tắc
(canonical form): đổi đơn vị (m/s so với km/h), định dạng ngày tháng, cách viết số, chữ
hoa/thường. Mục đích: hai giá trị diễn đạt cùng một thứ phải *bằng nhau về dạng* sau
chuẩn hóa, để các bước sau (so sánh, khử trùng, lưu trữ) không bị lừa bởi bề mặt.

Ví dụ với nguồn B: hai bản ghi viết "10 m/s" và "36 km/h" — sau chuẩn hóa đơn vị, cả hai
thành dạng chính tắc "10.0 m/s".

```turtle
ex:recB_1  ex:unit  "m/s" .
ex:recB_2  ex:unit  "km/h" .

# sau chuẩn hóa:
ex:recB_1n  ex:normValue  10.0 ; ex:normUnit  ex:meter_per_second .
ex:recB_2n  ex:normValue  10.0 ; ex:normUnit  ex:meter_per_second .   # 36 km/h = 10 m/s
```

Điểm then chốt: **chuẩn hóa có thể mất thông tin**. Đơn vị gốc của nguồn, cách viết gốc
của nguồn là *thuộc về nguồn* — sau chuẩn hóa, vẫn giữ liên kết tới bản ghi gốc để truy
nguyên. Chuẩn hóa phải là một bước có ghi chép (derivation), không phải sửa chữa tại chỗ
làm mất dấu vết.

> ⚠️ **Ngộ nhận phổ biến:** "Chuẩn hóa chỉ là việc kỹ thuật vô hại." Sai. Chuẩn hóa quyết
> định *thứ gì được coi là giống nhau*. Chọn sai quy tắc chuẩn hóa (ví dụ: đổi mọi đơn vị
> về "default" không ghi chú) khiến hai giá trị khác nhau bị gộp thành một — hoặc hai giá
> trị giống nhau bị tách rời. Chuẩn hóa là một quyết định ngữ nghĩa, phải được phiên bản
> hóa như các quy tắc khác (§7.24).

## 7.8 Cấu trúc hóa: Structuring thành RDF

### Trực giác

Bản ghi chuẩn hóa vẫn là một hàng dữ liệu trung gian ("subject, relation, object").
Bước cấu trúc hóa đưa nó về dạng đồ thị: chọn IRI cho chủ thể, vị từ, và giá trị — theo
một **lược đồ đích** (target schema). Đây là nơi tri thức ứng viên trở thành bộ ba RDF.

### Cơ chế

**Cấu trúc hóa (Structuring)** sản xuất các bộ ba RDF từ bản ghi chuẩn hóa. Với ba
nguồn của chương, lược đồ đích là lược đồ cơ chế (mechanism schema) quen thuộc từ các
chương trước: `ex:rateOfChange_1` (RateOfChange), `ex:derivativeOperation_1`
(DerivativeOperation), `ex:velocity_1` (Velocity), `ex:position_1` (Position) [khung
cơ chế của sách].

Nguồn A → cấu trúc hóa:

```turtle
ex:mechA_1  a             ex:Mechanism ;
            ex:hasOperation  ex:derivativeOperation_1 ;
            ex:hasOutput     ex:rateOfChange_1 .
```

Nguồn B → cấu trúc hóa:

```turtle
ex:mechB_1  a             ex:Mechanism ;
            ex:hasOperation  ex:derivativeOperation_1 ;
            ex:hasOutput     ex:velocity_1 ;
            ex:hasInput      ex:position_1 ;
            ex:hasInput      ex:time_1 .
```

Nguồn C → cấu trúc hóa (chưa gán vào cơ chế hiện có!):

```turtle
ex:mechC_1  a             ex:Mechanism ;
            ex:hasOperation  ex:derivativeOperation_1 ;
            ex:hasOutput     ex:current_1 ;
            ex:hasInput      ex:voltage_1 ;
            ex:hasInput      ex:time_1 .
```

Chú ý: bước cấu trúc hóa **chưa quyết định** `ex:velocity_1` có bằng `ex:current_1` hay
không. Nó chỉ đưa ba luồng về *cùng một hình dạng biểu diễn* để các bước tích hợp sau có
thể so sánh được. Việc đưa `ex:current_1` về dạng RDF giống `ex:velocity_1` về hình thức
không có nghĩa là chúng đồng nhất — sự đồng nhất là một *quyết định* ở §7.9–7.10.

### Ứng dụng

Cấu trúc hóa là nơi **lược đồ đích** phát huy vai trò: nó là ontology mà mọi nguồn phải
được ánh xạ về (mapping, §7.12). Nếu lược đồ đích không có khái niệm "current" (dòng
điện), bản ghi của nguồn C buộc phải tạo khái niệm mới — hoặc báo "chưa ánh xạ được"
(unresolved, §7.28), không được gắn bừa vào khái niệm gần giống.

> 🖊 **Tự kiểm tra:** Bước nào trong đường ống (a) quyết định hình dạng RDF, (b) quyết
> định "hai thứ là một", (c) quyết định "giá trị nào hợp lệ"? Đánh dấu từng bước trên sơ
> đồ §7.1.

## 7.9 Nghị quyết định danh: Sinh ứng viên khác Chấm điểm

### Trực giác

Hai mảnh tri thức "có thể" nói về cùng một thực thể. So sánh từng cặp một là không khả
thi khi số bản ghi lớn (n bản ghi → n²/2 cặp). Hệ thống cần tách hai việc: *đề xuất các
cặp đáng xem* (rẻ, ưu tiên không bỏ sót) và *chấm điểm từng cặp đã đề xuất* (kỹ hơn, ra
quyết định).

### Cơ chế

**Nghị quyết định danh (Entity Resolution)** là quá trình toàn phần: quyết định xem các
bản ghi từ cùng hoặc khác nguồn có trỏ tới cùng một thực thể thế giới thực hay không
[@hogan-creation-enrichment] [@rahm-bernstein-2001]. Nó gồm hai giai đoạn với mục tiêu
khác nhau:

1. **Sinh ứng viên (Candidate Generation):** tạo các cặp *có khả năng* trùng, dùng khóa
   thô (cùng tên chuẩn hóa, cùng cửa sổ thời gian). Mục tiêu: **độ bao phủ (recall)** —
   không bỏ sót cặp trùng thật, chấp nhận nhiều cặp không trùng. Ở giai đoạn này, "có
   khả năng" ≠ "là một".

2. **Chấm điểm (Scoring):** với từng cặp ứng viên, so sánh chi tiết trên từng thuộc tính
   và ra quyết định: trùng / không trùng / cần xem lại. Đây là lõi của mô hình
   Fellegi–Sunter (§7.10).

**Blocking** là kỹ thuật hiện thực hóa sinh ứng viên: chia bản ghi vào các khối (block)
theo khóa chặn (blocking key), chỉ so sánh trong từng khối. Ví dụ: khối theo chữ cái đầu
của tên chuẩn hóa, hoặc theo `ex:hasInput`. Nếu khóa chặn quá mịn, cặp trùng thật bị xếp
khác khối → không bao giờ được so sánh → **mất recall**. Chọn khóa chặn là một đánh đổi
giữa tốc độ và độ bao phủ.

Với chương này: sinh ứng viên gom `ex:mechB_1` và `ex:mechC_1` vào cùng khối (cùng
`ex:hasInput ex:time_1` — cả hai đều có input thời gian); `ex:mechA_1` không có input
thời gian rõ ràng nên ở khối khác. Hệ thống sẽ so sánh cặp (B, C) nhưng không so sánh
(A, C) — vì khóa chặn cho rằng A và C khác hẳn. Đây là nơi recall có thể bị mất.

> ⚠️ **Ngộ nhận phổ biến:** "Sinh ứng viên tìm thấy các thực thể trùng." Sai. Sinh ứng
> viên tìm *các cặp cần xem xét*. Kết luận trùng/không trùng chỉ đến từ giai đoạn chấm
> điểm. Trộn hai giai đoạn là nguồn gốc của cả false positive lẫn false negative định
> danh.

## 7.10 Liên kết bản ghi: Mô hình Fellegi–Sunter

### Trực giác

Khi nhân viên nhà ga so sánh hai hành khách có cùng tên, họ không chỉ hỏi "tên có giống
không" — họ so sánh nhiều đặc điểm (tuổi, quê, số vé) rồi ước lượng khả năng là cùng một
người. Mô hình Fellegi–Sunter (1969) làm chính việc này một cách có xác suất [@fellegi-sunter-1969].

### Cơ chế

Với mỗi cặp bản ghi ứng viên, ta so sánh trên k thuộc tính và thu được một **véc-tơ so
sánh** γ — mỗi thành phần ghi khớp/không khớp trên một thuộc tính. Ví dụ cặp (B, C):

![Nghị quyết định danh: sinh ứng viên bằng blocking → so sánh véc-tơ γ → quyết định ba vùng theo hai ngưỡng Fellegi–Sunter (không trùng / có thể trùng / trùng).](figures/generated/ch07-entity-resolution.pdf)

| Thuộc tính so sánh | B (vận tốc) | C (dòng điện) | Khớp? |
|--------------------|-------------|---------------|-------|
| operation (đạo hàm) | derivativeOperation_1 | derivativeOperation_1 | ✓ |
| input 1 | position_1 | voltage_1 | ✗ |
| input 2 | time_1 | time_1 | ✓ |
| output | velocity_1 | current_1 | ✗ |

Véc-tơ γ = (khớp, không, khớp, không).

Fellegi–Sunter định nghĩa hai xác suất:

- **m(γ):** xác suất quan sát được γ trong các cặp *thực sự trùng* (cùng thực thể).
- **u(γ):** xác suất quan sát được γ trong các cặp *thực sự không trùng*.

Tỷ số hợp lý (likelihood ratio) m(γ)/u(γ) là trọng số của véc-tơ so sánh. Hai ngưỡng
(chọn theo tỷ lệ lỗi chấp nhận được) chia kết quả thành ba vùng:

```
γ nằm dưới ngưỡng thấp  →  không trùng (non-match)
γ nằm giữa hai ngưỡng   →  có thể trùng (possible match) → xem xét thủ công
γ nằm trên ngưỡng cao   →  trùng (match)
```

Mô hình này tối ưu khi các thuộc tính so sánh độc lập có điều kiện với nhau — một giả
định lý tưởng, không phải lúc nào cũng đúng trong thực tế. Quan trọng: m(γ) và u(γ)
phải được **ước lượng từ dữ liệu** (nhãn hoặc thuật toán không giám sát), không phải
đoán.

Với cặp (B, C): γ = (khớp, không, khớp, không). Nếu hệ thống ước lượng m(γ)/u(γ) thấp
(đầu vào/output khác nhau nhiều khả năng là khác thực thể), cặp rơi xuống vùng "không
trùng" — hệ thống kết luận `ex:velocity_1` ≠ `ex:current_1`, đúng như kỳ vọng vật lý.

Với cặp (A, B) — nếu khóa chặn cho phép so sánh: cả hai cùng output "rate of change",
cùng operation đạo hàm. γ = (khớp, khớp, khớp). m/u cao → trùng? Ở đây cần thận trọng:
§7.11 gióng lược đồ sẽ kiểm tra "output của A" và "output của B" có cùng thuộc tính không
— chưa nói chúng cùng *giá trị*.

### Ứng dụng

Kết quả của Fellegi–Sunter là **quyết định định danh** (identity decision), được ghi lại
như một sự kiện tích hợp:

```turtle
ex:idDecision_BC  a            ex:IdentityDecision ;
                  ex:compares   ex:mechB_1 , ex:mechC_1 ;
                  ex:comparisonVector  "agree,disagree,agree,disagree" ;
                  ex:decision   ex:NonMatch ;
                  ex:rationale  "Different input and output quantities; low likelihood ratio." ;
                  ex:madeAt     "2026-08-30T11:00:00Z"^^xsd:dateTime .
```

Quyết định "không trùng" là một quyết định **có xác suất sai sót**, không phải sự thật
bất biến. Nếu sau này có bằng chứng mới (một nguồn D nói "current chính là rate of change
của voltage theo time, cùng cơ chế đạo hàm"), quyết định có thể bị đảo — và dấu vết của
quyết định cũ vẫn được giữ, giống như governance states của Chương 6.

> 🖊 **Tự kiểm tra:** Một cặp bản ghi có γ toàn khớp (mọi thuộc tính giống nhau). Hệ
> thống có được phép kết luận "cùng thực thể" ngay không? Nếu không, còn cần gì nữa? Gợi
> ý: m(γ)/u(γ) phụ thuộc điều gì, và "có thể trùng" xử lý ra sao?

## 7.11 Gióng lược đồ: Schema Alignment

### Trực giác

Nguồn B gọi là "velocity", nguồn D (chưa xuất hiện) gọi là "vận tốc". Trước khi so sánh
giá trị, phải biết hai *cột/thuộc tính* có cùng ngữ nghĩa không. Gióng lược đồ trả lời
"thuộc tính nào của lược đồ này tương ứng với thuộc tính nào của lược đồ kia".

### Cơ chế

**Gióng lược đồ (Schema Matching / Schema Alignment)** là quá trình tìm các tương ứng
ngữ nghĩa giữa các phần tử lược đồ [@rahm-bernstein-2001]:

- **Mức phần tử (element-level):** khớp từng thuộc tính đơn lẻ — tên giống nhau, kiểu dữ
  liệu giống nhau ("velocity" ↔ "vận tốc").
- **Mức cấu trúc (structure-level):** khớp các tổ hợp phần tử xuất hiện cùng nhau trong
  một cấu trúc ("input pair (position, time) → output velocity" là một mẫu cấu trúc).

Các bộ gióng lược đồ (matcher) phân loại theo thông tin dùng:

- **Schema-level:** chỉ dùng lược đồ — tên, kiểu, ràng buộc, quan hệ.
- **Instance-level:** dùng giá trị dữ liệu để suy nghĩa ("cột này toàn số dương lớn →
  có thể là đo lường vật lý").
- **Hybrid:** kết hợp cả hai.

Quan trọng: **gióng lược đồ không chứng minh** hai thuộc tính là một. Nó đề xuất tương
ứng + bằng chứng (độ giống tên, độ giống cấu trúc) — và tương ứng phải được *xác nhận*
trước khi dùng, như quy trình ứng viên → bằng chứng → chấp nhận của Chương 3 (§3.2.5).

### Ứng dụng

Ba nguồn A, B, C dùng các tên khác nhau cho cùng khái niệm. Gióng lược đồ đề xuất:

![Gióng lược đồ: `velocity`/`position` (B) có tương ứng được xác nhận với ontology đích; `current`/`voltage` (C) có đề xuất bị bác — tương ứng là quyết định có bằng chứng, không phải khớp tên.](figures/generated/ch07-schema-alignment.pdf)

| Lược đồ nguồn | Phần tử | Tương ứng đề xuất | Bằng chứng |
|---------------|---------|-------------------|------------|
| A | "derivative of f" | `ex:derivativeOperation_1` | tên + cấu trúc định nghĩa |
| B | "velocity" | `ex:velocity_1` | tên + định nghĩa |
| B | "position" | `ex:position_1` | tên + định nghĩa |
| C | "current" | (chưa có) — gợi ý tạo mới | không khớp ontology hiện có |

Lưu ý: nguồn C dùng "rate of change of voltage" — gióng lược đồ *có thể* đề xuất nó là
"rate of change" (cùng khái niệm cơ chế). Nhưng đề xuất này phải qua xác nhận: liệu
"dòng điện" có cùng vị trí cấu trúc với "vận tốc"? Cấu trúc nói không — đầu vào khác
(position vs voltage), output khác (velocity vs current). Tương ứng bị bác bỏ ở bước xác
nhận.

> ⚠️ **Ngộ nhận phổ biến:** "Hai cột cùng tên → cùng ngữ nghĩa." Sai. "velocity" trong
> lược đồ A có thể là "tốc độ góc" (angular velocity) — cùng tên, khác nghĩa. Gióng lược
> đồ chỉ là *đề xuất có bằng chứng*; xác nhận mới là quyết định.

## 7.12 Ánh xạ: Direct Mapping và R2RML

### Trực giác

Đã biết "cột này ↔ thuộc tính kia", bước kế tiếp là *biến đổi dữ liệu* từ lược đồ nguồn
sang lược đồ đích. Có hai thái cực: để hệ thống tự động làm (default mapping) hoặc viết
tay một đặc tả ánh xạ (custom mapping). Cả hai đều là chuẩn W3C cho RDB → RDF.

### Cơ chế

**Direct Mapping** (W3C Recommendation 2012-09-27) là ánh xạ mặc định tự động từ cơ sở
dữ liệu quan hệ sang RDF [@w3c-direct-mapping]: mỗi bảng → một lớp; mỗi hàng → một tài
nguyên (IRI dựng từ tên bảng + khóa chính); mỗi cột → một vị từ; giá trị ô → object.
Vì hoàn toàn tự động, hình dạng RDF đầu ra *theo lược đồ cơ sở dữ liệu*, không theo
ontology đích.

**R2RML** (W3C Recommendation 2012-09-27) là ngôn ngữ khai báo ánh xạ tùy biến
[@w3c-r2rml]. Đơn vị trung tâm là **Triples Map**: một quy tắc dịch mỗi hàng của một
bảng logic (bảng gốc, view, hoặc câu SQL) thành không hoặc nhiều bộ ba RDF, qua:

- **Subject Map:** sinh IRI chủ thể (mẫu chuỗi hoặc hằng).
- **Predicate-Object Map:** ghép từng cặp vị từ + object (object có thể là hằng, cột,
  hoặc IRI từ cột khác).

Ví dụ ánh xạ R2RML cho bảng `velocity_defs` của nguồn B:

```turtle
@prefix rr: <http://www.w3.org/ns/r2rml#> .
@prefix ex: <http://example.org/mechkg/> .

<#TriplesMap_Velocity>
    rr:logicalTable [ rr:tableName "velocity_defs" ] ;
    rr:subjectMap [
        rr:template "http://example.org/mechkg/velocity/{def_id}"
    ] ;
    rr:predicateObjectMap [
        rr:predicate ex:hasOutput ;
        rr:objectMap [ rr:column "output_iri" ]
    ] ;
    rr:predicateObjectMap [
        rr:predicate ex:hasInput ;
        rr:objectMap [ rr:column "input1_iri" ]
    ] .
```

Vì sao phân biệt hai loại? Vì **Direct Mapping không biết ontology đích**: nó cho ra
"bảng velocity_defs thành lớp velocity_defs" — đúng với nguồn, nhưng không phải hình dạng
mong muốn (`ex:velocity_1 a ex:Velocity`). R2RML cho phép viết đúng ý đồ. Quyết định
"dùng ánh xạ mặc định hay viết tay" chính là quyết định *hình dạng tri thức trong hệ
thống* — một quyết định ngữ nghĩa, không phải kỹ thuật.

(Cho nguồn dạng bảng tính CSV, chuẩn tương ứng là CSVW — Model for Tabular Data, W3C
Recommendation 2015-12-17 — với mô hình bảng: table/row/column/cell + annotation để khai
báo khóa chính, kiểu dữ liệu, và sinh RDF qua csv2rdf [@w3c-tabular-data-model].)

### Ứng dụng

Trong đường ống của sách, ánh xạ nằm ở ranh giới cấu trúc hóa (§7.8): lược đồ đích của
hệ thống chính là ontology cơ chế; mỗi nguồn mới có một **mapping specification** —
một đặc tả phiên bản hóa (một artifact có thể xem xét, sửa, tái xử lý), không phải code
ẩn trong pipeline.

> 🖊 **Tự kiểm tra:** Cho bảng `definitions(name, meaning, unit)` của nguồn C. Viết
> subject map và một predicate-object map R2RML đưa cột `meaning` thành `ex:hasOutput`.
> Nếu dùng Direct Mapping, output sẽ ra sao — và vì sao có thể không dùng được?

## 7.13 Khử trùng: Deduplication

### Trực giác

Hai nguồn cùng nói "vận tốc là rate of change của vị trí theo thời gian" — cùng nội dung,
khác nguồn. Đây không phải hai phát biểu độc lập đáng giữ nguyên vẹn: chúng là **trùng
nội dung** (content duplicates). Nhưng cũng không được xóa một cái: mỗi cái mang một
provenance riêng. Khử trùng là *hòa giải*, không phải xóa bỏ.

### Cơ chế

**Khử trùng (Deduplication)** là việc nhận diện các bản ghi/phát biểu trùng nhau — trùng
chính xác (identical) hoặc trùng gần (near-duplicate: cùng mệnh đề, khác giá trị/đơn vị)
— và quyết định xử lý chúng. Kết nối với Chương 6: hai claim cùng nội dung vẫn là hai
đối tượng riêng (claim identity ≠ content identity, §6.2). Vì vậy khử trùng ở tầng tích
hợp không gộp IRI claim; nó gộp *cách đưa vào sổ cái*.

**Khử trùng phát biểu (Claim Deduplication)** là quy tắc riêng của sách: hai claim ứng
viên cùng nội dung nhưng khác provenance là *ứng viên trùng nội dung*; chúng chỉ được
gộp thành một mục sổ cái qua một quyết định hợp nhất có ghi lại **cả hai** provenance —
không bao giờ âm thầm vứt bỏ một bên.

So sánh hai bản ghi B (từ nguồn B) và B′ (từ nguồn D, cùng nội dung):

| Bản ghi | Nội dung | Nguồn |
|---------|----------|-------|
| `ex:recB_1` | velocity = rate of change of position | `src:sourceB` |
| `ex:recD_1` | velocity = rate of change of position | `src:sourceD` |

Content hash (§7.14) của hai bản ghi bằng nhau → phát hiện trùng nội dung. Hệ thống
không tạo hai mục sổ cái; nó tạo *một* claim tích hợp mang hai provenance. Nếu hai nguồn
*đều độc lập* (không phải echo source, §7.23), claim tích hợp có hai nguồn hỗ trợ độc
lập — bằng chứng mạnh hơn claim một nguồn.

> ⚠️ **Ngộ nhận phổ biến:** "Khử trùng = xóa bản ghi trùng." Sai. Xóa làm mất bằng chứng
> và provenance. Khử trùng đúng là *hợp nhất có bảo toàn*: cả hai nguồn vẫn được lưu trong
> claim tích hợp, chỉ không còn là hai claim riêng độc lập trong sổ cái.

## 7.14 Thu nạp lũy đẳng: Idempotent Ingestion và Content Hash

### Trực giác

Chạy lại đường ống trên cùng dữ liệu — vì sửa lỗi, vì thử nghiệm — phải cho cùng một kết
quả. Nếu lần chạy thứ hai tạo ra bản sao thứ hai của mọi claim, sổ cái nhanh chóng nhiễm
trùng. Hệ thống cần một cơ chế làm cho việc chạy lại "vô hại": **thu nạp lũy đẳng**.

### Cơ chế

**Thu nạp lũy đẳng (Idempotent Ingestion)** nghĩa là: chạy cùng một quá trình thu
nhận/tích hợp nhiều lần cho ra cùng một trạng thái sổ cái — không claim trùng, không
provenance trùng. Điều kiện: các bước phải *tất định* (deterministic) và dùng **content
hash** làm khóa ổn định.

**Content Hash** là vân tay (digest) tất định của một bản ghi/nội dung đã chuẩn hóa —
băm trên dạng chính tắc (chủ thể IRI, vị từ, object đã gõ kiểu, mẩu nguồn). Thay đổi nội
dung → đổi hash. Ví dụ:

```turtle
ex:recB_1  ex:contentHash  "f3a9…c2"^^xsd:string .
```

Hai lần chạy trên cùng nguồn B cùng cho `ex:recB_1` với cùng hash. Lần chạy thứ hai phát
hiện hash đã tồn tại → bỏ qua (skip), không tạo bản sao. Nếu nguồn B được cập nhật (bản
mới), hash đổi → bản ghi mới được tạo, bản cũ vẫn được giữ với provenance cũ (không ghi
đè, theo nguyên tắc bất biến của Chương 6).

Ba cảnh báo:

1. **Hash ≠ định danh claim.** Hash của nội dung chỉ là khóa phát hiện trùng. IRI của
   claim trong sổ cái là đối tượng quản trị riêng (Chương 6). Dùng hash làm IRI claim là
   một sai lầm: hai claim cùng nội dung khác nguồn sẽ bị gộp nhầm.

2. **Hash ≠ provenance.** Biết "bản ghi này có hash X" không cho biết "bản ghi này từ
   đâu đến". Hash chỉ phục vụ khử trùng và lũy đẳng.

3. **Lũy đẳng ≠ đúng.** Chạy lại cho kết quả giống nhau không có nghĩa kết quả đúng —
   chỉ có nghĩa *ổn định*. Một pipeline lũy đẳng vẫn có thể nhất quán tạo ra phát biểu
   sai, nếu quy tắc của nó sai.

> 🖊 **Tự kiểm tra:** Vì sao hash phải tính trên *dạng chuẩn hóa* chứ không phải trên văn
> bản thô của nguồn? Gợi ý: hai nguồn viết "10 m/s" và "36 km/h" — hash trên dạng thô
> khác nhau, hash trên dạng chuẩn hóa giống nhau. Nếu bỏ qua chuẩn hóa thì điều gì xảy ra
> với khử trùng?

## 7.15 Cổng SHACL: Hợp lệ khác Được chấp nhận

### Trực giác

Trước khi đưa vào sổ cái, phát biểu ứng viên phải đi qua một cổng kiểm tra *hình dạng*:
có đủ thuộc tính bắt buộc không, kiểu dữ liệu có đúng không, bội số có hợp lệ không.
Đây là nơi SHACL (Chương 5) bước vào đường ống.

### Cơ chế

**Cổng SHACL (SHACL gate)** kiểm tra các bộ ba ứng viên chống lại các hình dạng đã khai
báo — yêu cầu về lớp, thuộc tính, kiểu, bội số — và sinh ra báo cáo hợp lệ [@w3c-shacl].

Ví dụ hình dạng cho một Mechanism:

```turtle
ex:MechanismShape  a            sh:NodeShape ;
                   sh:targetClass ex:Mechanism ;
                   sh:property [
                       sh:path ex:hasOperation ;
                       sh:minCount 1 ;
                       sh:nodeKind sh:IRI
                   ] ;
                   sh:property [
                       sh:path ex:hasOutput ;
                       sh:minCount 1 ;
                       sh:nodeKind sh:IRI
                   ] .
```

Nếu `ex:mechC_1` thiếu `ex:hasOperation` (trích xuất nguồn C không bắt được operation),
cổng báo lỗi: bộ ba không hợp lệ. Nhưng — điểm mấu chốt — **hợp lệ ≠ được chấp nhận**:

- Một bộ ba *hợp lệ* về hình dạng vẫn có thể bị *từ chối* ở bước quản trị (mâu thuẫn với
  bằng chứng mạnh hơn, §7.16).
- Một bộ ba *không hợp lệ* không bị xóa tự động — nó được đưa vào hàng đợi xem xét
  (§7.20) hoặc quay lại trích xuất.

Cổng SHACL là một **bộ lọc cấu trúc**, không phải bộ lọc chân lý. Nó đảm bảo "đúng
hình dạng", không đảm bảo "đúng sự thật". Đây chính là bài học conformance ≠ truth của
Chương 5, đặt vào giữa đường ống.

### Ứng dụng

Trong pipeline: tất cả các bộ ba đã cấu trúc hóa (A, B, C) phải qua cổng. Bộ ba của A
và B hợp lệ; bộ ba của C thiếu `hasOperation` → không hợp lệ → rơi vào hàng đợi xem
xét, *không được* đưa thẳng vào sổ cái.

> ⚠️ **Ngộ nhận phổ biến:** "Báo cáo SHACL nói conforms → phát biểu đúng." Sai. `conforms
> true` chỉ nghĩa là *hình dạng khớp*. Một bộ ba hợp lệ về hình dạng có thể vô nghĩa về
> mặt ngữ nghĩa (ví dụ `ex:velocity_1 ex:hasInput ex:voltage_1` — hình dạng đúng, ý nghĩa
> sai). Hợp lệ là điều kiện cần, không phải điều kiện đủ, của việc chấp nhận.

## 7.16 Phát hiện xung đột: Conflict Detection

### Trực giác

Khi hai ứng viên nói khác nhau về cùng một thứ, hệ thống không được phép bỏ qua. Nó phải
*nhận diện* xung đột, phân loại, và quyết định. Đây là nơi phân loại mâu thuẫn năm loại
của Chương 6 được vận hành trong đường ống.

### Cơ chế

**Phát hiện xung đột (Conflict Detection)** tìm các cặp phát biểu (giữa ứng viên với
ứng viên, hoặc ứng viên với claim đã trong sổ cái) mà nội dung không thể cùng đúng trong
cùng một ngữ cảnh. Dùng phân loại năm loại của §6.6:

| Loại | Ví dụ trong cơ chế |
|------|--------------------|
| Logical (logic) | `ex:current_1` vừa là `ex:Velocity` vừa là `ex:Current` nếu hai lớp rời nhau |
| Value (giá trị) | hai claim cùng nói `ex:velocity_1 ex:value` nhưng khác số |
| Temporal (thời gian) | "vận tốc = ds/dt" valid từ 1687, "vận tốc cộng tính" valid từ 1905 — khác valid time, không xung đột |
| Scope (phạm vi) | nguồn A nói "đạo hàm theo không gian", nguồn B nói "theo thời gian" — khác phạm vi |
| Source (nguồn) | hai nguồn nói khác nhau nhưng cùng khẳng định một sự kiện — xung đột nguồn |

Chú ý: **không phải mọi khác biệt văn bản là xung đột.** Nguồn A nói "đạo hàm đo tốc độ
thay đổi của f", nguồn B nói "vận tốc là tốc độ thay đổi của vị trí" — khác nhau về thuật
ngữ nhưng có thể là cùng một mệnh đề dưới ánh xạ lược đồ. Trước khi tuyên bố xung đột,
hệ thống phải *thử hòa giải ngữ cảnh* (§6.6): có phải khác valid time không? khác phạm
vi không? Nếu hòa giải được, không có xung đột — chỉ có hai phát biểu có ngữ cảnh khác
nhau.

### Ứng dụng

Cặp (A, B) sau khi gióng lược đồ: "derivative of f" ↔ `ex:derivativeOperation_1`, cùng
mệnh đề "rate of change" → **không xung đột**, thực ra là trùng nội dung → khử trùng
(§7.13). Cặp (B, C): `ex:velocity_1` so với `ex:current_1` — gióng lược đồ đã bác tương
ứng (đầu vào/output khác) → không phải xung đột, mà là hai khái niệm khác nhau. Xung đột
thật chỉ xuất hiện khi *cùng ngữ cảnh* mà giá trị khác nhau — ví dụ hai nguồn cùng khẳng
định giá trị vận tốc của cùng một vật tại cùng thời điểm nhưng khác số.

> ⚠️ **Ngộ nhận phổ biến:** "Hai nguồn nói khác nhau → hệ thống bất nhất → phải sửa."
> Sai. Khác biệt có thể là khác ngữ cảnh (thời gian, phạm vi) — không phải xung đột. Tuyên
> bố xung đột quá vội dẫn tới việc "sửa" những gì không cần sửa và đánh mất thông tin.

## 7.17 Quyết định tích hợp và Kết quả hợp nhất

### Trực giác

Một nhóm ứng viên đã đi qua định danh, gióng lược đồ, khử trùng, SHACL, phát hiện xung
đột. Đến đây hệ thống phải *quyết định*: đưa gì vào sổ cái, từ chối gì, đưa gì cho người
xem xét.

### Cơ chế

**Quyết định tích hợp (Integration Decision)** là quyết định trên từng nhóm ứng viên:
**chấp nhận** (accept), **từ chối** (reject), hoặc **chuyển xem xét** (defer to review).
Mọi quyết định đều phải có lý do được ghi lại — không được âm thầm chấp nhận.

![Sơ đồ quyết định tích hợp: cổng SHACL → phát hiện xung đột → ba nhánh (chấp nhận / xem xét / từ chối) → ghi sổ. Mọi nhánh đều ghi lại lý do; không claim nào bị xóa.](figures/generated/ch07-integration-decision.pdf)

**Kết quả hợp nhất (Merge Outcome)** là hậu quả lên sổ cái của một nhóm ứng viên được
chấp nhận, theo các khả năng của Chương 6:

- **Chèn mới (insert):** claim tích hợp mới được tạo trong sổ cái.
- **Củng cố (strengthen):** claim đã có nhận thêm bằng chứng từ ứng viên mới (cùng nội
  dung, nguồn độc lập).
- **Thay thế (supersede):** ứng viên tốt hơn thay claim cũ — claim cũ chuyển trạng thái
  Superseded, không bị xóa (§6.13).
- **Hợp nhất (merge):** hai ứng viên cùng nội dung khác nguồn gộp thành một mục, giữ cả
  hai provenance (§7.13).

```turtle
ex:mergeOutcome_1  a            ex:MergeOutcome ;
                   ex:kind       ex:Strengthen ;
                   ex:target     ex:claim_velocity_rate_of_change ;
                   ex:addsEvidence  ex:recD_1 ;
                   ex:fromDecision  ex:integrationDecision_1 .

ex:integrationDecision_1  a         ex:IntegrationDecision ;
                          ex:verdict  ex:Accept ;
                          ex:rationale "Content identical to accepted claim; independent source adds evidence." ;
                          ex:madeAt   "2026-08-30T12:00:00Z"^^xsd:dateTime .
```

Nguyên tắc bảo toàn xuyên suốt: **claim thua không bao giờ bị xóa** — chúng bị Superseded
hoặc được lưu với trạng thái Rejected và đầy đủ lý do, như Chương 6 đã quy định (§6.12,
§6.14).

> 🖊 **Tự kiểm tra:** Cho tình huống: ứng viên mới cùng nội dung với claim Accepted hiện
> có, nhưng nguồn của ứng viên mới là echo source (chép từ nguồn của claim cũ). Quyết định
> tích hợp nên là gì? Có nên củng cố claim cũ bằng bằng chứng "mới" này không?

## 7.18 Ghi sổ trước: Claim Ledger First

### Trực giác

Sổ cái phát biểu (Claim Ledger, Chương 6) là *nơi duy nhất* ghi lại sự thật đã được quản
trị của hệ thống. Mọi truy vấn nên đọc từ sổ cái (qua chiếu hình) chứ không phải từ các
bộ đệm trung gian của đường ống. Nguyên tắc: **sổ cái trước, mọi thứ khác sau**.

### Cơ chế

**Ghi sổ phát biểu (Claim Ledger Insertion)** là phép ghi có cam kết (committed write)
của một claim Accepted vào sổ cái, kèm toàn bộ "phong bì tri thức": nội dung, provenance,
bằng chứng, phạm vi thời gian, trạng thái quản trị, confidence.

**Chiếu hình (Canonical Projection)** là khung nhìn vật chất hóa (materialized view)
được dựng lại *từ* sổ cái sau quản trị — truy vấn đọc khung nhìn này sẽ thấy các claim
Accepted (và đã hòa giải). Nó được tái dựng từ sổ cái; nó không phải một kho chân lý độc
lập.

Tại sao "sổ cái trước"? Vì nếu các bước trung gian (bộ đệm trích xuất, bộ đệm tích hợp)
được đối xử như nguồn chân lý, hệ thống sẽ có nhiều nguồn sự thật cạnh tranh nhau. Một
truy vấn có thể đọc claim "Accepted" từ sổ cái, một truy vấn khác đọc cùng nội dung từ bộ
đệm trung gian nhưng chưa qua quản trị — kết quả mâu thuẫn, không thể giải thích. Nguyên
tắc "sổ cái trước" đảm bảo *một nguồn sự thật duy nhất*.

### Ứng dụng

Trong đường ống: giai đoạn cuối chỉ ghi vào sổ cái sau khi mọi cổng đã qua. Không có
"ghi nháp trước, quản trị sau" — mọi thứ vào sổ cái đều là kết quả của một quyết định
tích hợp được ghi lại.

> ⚠️ **Ngộ nhận phổ biến:** "Truy vấn bộ đệm trích xuất cũng là truy vấn knowledge
> graph." Sai. Bộ đệm trung gian chứa *tri thức ứng viên* — chưa khử trùng, chưa qua
> quản trị. Chỉ chiếu hình từ sổ cái mới là "những gì hệ thống tin". Trộn hai thứ này là
> nguồn gốc của các câu trả lời không nhất quán.

## 7.19 Lineage: Từ đâu đến? — và vì sao Lineage khác Evidence

### Trực giác

Khi một claim Accepted xuất hiện trong chiếu hình, người dùng có quyền hỏi: "điều này từ
đâu ra?" và "tại sao tôi nên tin?". Hai câu hỏi khác nhau, hai thứ dữ liệu khác nhau.

### Cơ chế

**Lineage (dòng dõi)** là chuỗi provenance đầy đủ từ một claim trong sổ cái, lần ngược
qua các quyết định tích hợp, các bản trích xuất, các quan sát, tới các mẩu nguồn
[@prov-dm]. Lineage trả lời "từ đâu đến?" — một đường đi có thể kiểm toán:

```
ex:claim_velocity_rate_of_change
   ← ex:integrationDecision_1          (quyết định tích hợp)
   ← ex:mergeOutcome_1                 (hợp nhất)
   ← ex:recB_1                         (bản ghi trích xuất)
   ← ex:extractActB_1                  (activity trích xuất, phiên bản 2.3)
   ← ex:obsB_1                         (quan sát)
   ← src:fragB_2_1                     (mẩu nguồn)
   ← src:sourceB                       (nguồn)
```

**Evidence** trả lời "vì sao tin?" — thông tin hỗ trợ/phản bác claim (Chương 6, §6.3,
§6.5). Một claim có thể có lineage rất đầy đủ nhưng bằng chứng yếu, hoặc bằng chứng mạnh
nhưng lineage mỏng.

Đây là chỗ tinh tế nhất của chương: **lineage đầy đủ không phải là bằng chứng**. Một
pipeline hoàn hảo (lineage dài, đầy đủ, sạch) có thể tạo ra một claim sai nếu nguồn sai
hoặc quy tắc sai. Lineage dài chỉ cho biết "mọi bước đã được ghi lại" — không cho biết
"các bước đó đúng".

### Ứng dụng

Mọi claim trong sổ cái đều phải có lineage tối thiểu (đây là bất biến I1, §7.31). Khi
kiểm toán, người kiểm tra đi ngược lineage để tái dựng *cách* claim hình thành — rồi
*riêng biệt* đánh giá bằng chứng hỗ trợ claim đó.

> ⚠️ **Ngộ nhận phổ biến:** "Lineage càng dài, claim càng đáng tin." Sai. Lineage nói
> "từ đâu đến"; Evidence nói "vì sao tin". Một claim với lineage 10 bước và bằng chứng
> zero vẫn yếu hơn claim với lineage 2 bước và bằng chứng độc lập mạnh. Dùng lineage làm
> thước đo độ tin cậy là một lỗi ngữ nghĩa nghiêm trọng.

## 7.20 Con người trong vòng lặp: Hàng đợi xem xét

### Trực giác

Mô hình Fellegi–Sunter có một vùng "có thể trùng" (possible match) nằm giữa hai ngưỡng —
không đủ chắc để kết luận, không đủ chắc để bỏ qua. Vùng này, cùng với các ca SHACL lỗi
và xung đột không hòa giải được, đi vào **hàng đợi xem xét** — nơi con người quyết định.

### Cơ chế

**Hàng đợi xem quét (Review Queue)** là làn dành cho các ca mà đường ống tự động không
quyết định được với độ tin cậy theo chính sách. Con người xem xét với *bộ bằng chứng đầy
đủ* — không phải một dòng tóm tắt — và quyết định, quyết định được ghi lại trong sổ cái
như mọi quyết định khác.

Ba loại ca vào hàng đợi:

| Loại ca | Ví dụ |
|---------|-------|
| Possible match (Fellegi–Sunter) | cặp (A, B): khớp 3/4 thuộc tính, cần mắt người xác nhận "cùng mệnh đề?" |
| SHACL fail | `ex:mechC_1` thiếu hasOperation — cần xem lại trích xuất |
| Xung đột không hòa giải | hai claim cùng ngữ cảnh, cùng giá trị khác nhau, không hòa giải được |

Nguyên tắc cân bằng: gửi *mọi* ca cho người → không có pipeline (mọi thứ dừng ở con
người); gửi *không* ca nào → nguy cơ sai sót không kiểm soát. Chính sách xem xét là một
phần của integration policy (§7.29), được phiên bản hóa.

> ⚠️ **Ngộ nhận phổ biến:** "Người xem xét đúng hơn máy." Không tự động đúng. Người xem
> xét cũng mắc lỗi — nhưng họ là một *kênh quyết định khác*, có thể mang kiến thức ngoài
> dữ liệu. Giá trị của hàng đợi là ở chỗ quyết định được *ghi lại và truy nguyên*, không
> phải ở chỗ "con người luôn đúng".

## 7.21 Các chiều chất lượng dữ liệu

### Trực giác

"Chất lượng dữ liệu tốt" là một câu mơ hồ. Dữ liệu có thể chính xác nhưng thiếu, đầy đủ
nhưng lỗi thời, nhất quán nhưng không truy nguyên. Chất lượng là **nhiều chiều** — và mỗi
chiều đo một thứ khác nhau, giống như confidence đa chiều của Chương 6 (§6.11).

### Cơ chế

Sách dùng sáu chiều chất lượng cho đường ống:

| Chiều | Câu hỏi | Đo bằng |
|-------|---------|---------|
| **Accuracy** (chính xác) | Bản ghi có khớp với nguồn / chuẩn đối chiếu không? | đối chiếu mẫu kiểm tra |
| **Completeness** (đầy đủ) | Mọi nội dung đáng lấy đã được lấy chưa? | tỷ lệ fragment đã xử lý |
| **Consistency** (nhất quán) | Có mâu thuẫn không hòa giải trong sổ cái không? | số found/mâu thuẫn tồn đọng |
| **Timeliness** (kịp thời) | Dữ liệu còn hợp thời với valid time không? | so system time với valid time |
| **Provenance completeness** | Mọi claim có lineage đủ không? | bất biến I1–I2 (§7.31) |
| **Conformance** (hợp lệ) | Hình dạng SHACL có khớp không? | báo cáo validation (§7.15) |

Ba bài học quan trọng:

1. **Một con số "chất lượng 95%" là vô nghĩa.** 95% của chiều nào? Accuracy 95% + 
   completeness 40% là hai bức tranh rất khác nhau.
2. **Đầy đủ không kéo theo chính xác.** Lấy được hết (completeness tốt) nhưng trích
   xuất sai (accuracy kém) vẫn tạo ra sổ cái đầy rẫy phát biểu sai.
3. **Chất lượng là theo chính sách hệ thống.** "Chuẩn đối chiếu" dùng để đo accuracy là
   một lựa chọn — đo theo ontology nội bộ khác với đo theo một nguồn tham chiếu ngoài.

> 🖊 **Tự kiểm tra:** Một pipeline báo cáo "completeness 100%, accuracy 92%". Viết hai
> tình huống (một vô hại, một nguy hiểm) cho số 8% thiếu chính xác đó. Vì sao cần cả hai
> con số chứ không chỉ một?

## 7.22 Các kiểu hỏng hóc của đường ống

### Trực giác

Một đường ống 11 giai đoạn có 11 chỗ hỏng. Hệ thống tốt không phải hệ thống không bao
giờ hỏng — mà là hệ thống biết rõ *từng kiểu hỏng*, có tín hiệu phát hiện, và có đường
phục hồi.

### Cơ chế

Sách lập danh mục 13 kiểu hỏng hóc (failure modes) của đường ống thu nhận/tích hợp. Với
mỗi kiểu: tín hiệu phát hiện và hành động phục hồi.

| # | Kiểu hỏng | Tín hiệu phát hiện | Phục hồi |
|---|-----------|--------------------|----------|
| FM1 | Trích xuất sai (bắt nhầm nội dung) | đối chiếu mẫu; độ tin cậy trích xuất thấp | sửa pattern, chạy lại (reprocess) |
| FM2 | Chuẩn hóa sai (gộp nhầm/không gộp) | hai giá trị "giống" ra khác hash; hoặc ngược lại | rà quy tắc chuẩn hóa, phiên bản mới |
| FM3 | Khóa chặn mất recall (cặp trùng không gặp nhau) | đối chiếu kết quả với mẫu đã biết | đổi khóa chặn, chạy lại |
| FM4 | Lỗi định danh (false positive/negative) | kiểm tra mẫu; quyết định bị đảo khi có bằng chứng mới | ghi lại, đảo quyết định có lý do |
| FM5 | Gióng lược đồ sai (ánh xạ nhầm thuộc tính) | bằng chứng gióng yếu, bị bác khi xác nhận | giữ đề xuất bị bác như dấu vết |
| FM6 | Ánh xạ lỗi (R2RML chạy sai) | validation report; dữ liệu ra không như kỳ vọng | sửa mapping spec, phiên bản mới |
| FM7 | Mất lũy đẳng (chạy lại tạo trùng) | đếm claim trước/sau lần chạy lại khác nhau | sửa tính tất định, xóa bản trùng có lý do |
| FM8 | Lẫn lộn validation ≠ acceptance | claim "hợp lệ" vào sổ mà không qua quản trị | cổng SHACL + cổng quản trị tách bạch |
| FM9 | Thu nhận một phần (bỏ sót fragment) | completeness < 100%, fragment thiếu đánh dấu | chạy lại với danh sách fragment đầy đủ |
| FM10 | Nguồn vọng bị tính là bằng chứng độc lập | hai nguồn "độc lập" cùng lineage chung | gắn cờ echo source (§7.23) |
| FM11 | Chunking phá nghĩa (cắt giữa định nghĩa) | fragment thiếu hoàn chỉnh; trích xuất thất bại lặp | đổi ranh giới chunk, chạy lại |
| FM12 | Vi phạm ràng buộc truy hồi (over-reading) | phát biểu vượt nội dung fragment | kiểm tra ∠bound (§7.26) |
| FM13 | Chính sách trôi (policy drift) | quyết định tích hợp lệch chuẩn lịch sử | phiên bản hóa chính sách, cảnh báo |

Quan sát quan trọng: **không có kiểu hỏng nào được phát hiện bởi việc "chạy trơn
tru"** — mọi tín hiệu đều cần *đo lường chủ động* (observability, §7.34). Một pipeline
không báo lỗi không có nghĩa là pipeline không lỗi; nó có thể đang hỏng một cách êm ái.

> ⚠️ **Ngộ nhận phổ biến:** "Pipeline chạy xong không lỗi → dữ liệu tốt." Sai. Ba kiểu
> hỏng (FM3, FM4, FM9) có thể hoàn thành "thành công" mà vẫn cho kết quả sai — sai định
> danh, thiếu dữ liệu. "Không có lỗi được báo" và "không có lỗi" là hai việc khác nhau.

## 7.23 Nguồn vọng: Echo Sources

### Trực giác

Một trang web tổng hợp "10 định nghĩa vật lý quan trọng" chép lại định nghĩa vận tốc từ
giáo trình B. Nếu hệ thống ghi cả hai như hai nguồn độc lập, nó sẽ tin rằng `ex:recB_1`
có hai nguồn hỗ trợ — trong khi thực tế chỉ có một. **Nguồn vọng** làm tăng ảo số bằng
chứng.

### Cơ chế

**Echo Source** là nguồn mà nội dung của nó cuối cùng phái sinh (derived) từ một nguồn
khác đã có trong hệ thống — bản tóm tắt, bản sao, feed tổng hợp. Nhận diện echo source
thường dựa trên: trùng nội dung cao độ, lineage/lịch sử xuất bản, hoặc khai báo "theo
[nguồn gốc]".

Echo source không bị cấm — nó có giá trị truy nguyên (biết "ai đã chép từ ai" cũng là
tri thức). Điều bị cấm là **đếm echo claim như bằng chứng độc lập**:

```turtle
ex:claim_vroc  ex:hasEvidence  ex:recB_1 ;        # nguồn độc lập (textbook B)
               ex:hasEvidence  ex:recD_1 .        # nguồn vọng (trang tổng hợp chép B)
```

Claim có "hai bằng chứng" — nhưng hai bằng chứng này **không độc lập**. Trong chính sách
tin cậy (Chương 6 §6.5), bằng chứng phụ thuộc nhau phải được chấm thấp hơn: hai nguồn
cùng gốc chỉ đáng giá hơn một nguồn một chút, không phải gấp đôi.

### Ứng dụng

Với ba nguồn của chương: nếu nguồn D (trang tổng hợp) đăng ký sau và nội dung trùng
nguồn B, hệ thống gắn cờ `src:sourceD` là echo của `src:sourceB`. Khi nguồn D đưa ứng
viên cùng nội dung, ứng viên đó được giữ (provenance) nhưng **không** được tính là bằng
chứng độc lập cho claim.

> ⚠️ **Ngộ nhận phổ biến:** "Nhiều nguồn nói giống nhau → chắc chắn đúng." Sai — nếu các
> nguồn đó là vọng của nhau, số "nhiều" chỉ là ảo giác. Đếm bằng chứng phải đếm *nguồn
> độc lập*, không đếm *thể hiện* (instances).

## 7.24 Phiên bản hóa pipeline và Xử lý lại

### Trực giác

Đường ống không phải một cỗ máy đứng yên — nó được cải tiến: quy tắc chuẩn hóa sửa lỗi,
ánh xạ R2RML thêm cột, khóa chặn đổi. Mỗi lần đổi, mọi thứ *phía sau* chỗ đổi có thể thay
đổi kết quả. Nếu không ghi phiên bản, không ai biết claim này sinh ra bởi "pipeline nào".

### Cơ chế

**Phiên bản hóa pipeline (Pipeline Versioning):** mọi thành phần định hình đầu ra —
mapping, extraction pattern, quy tắc chuẩn hóa, khóa chặn, lược đồ đích, cổng SHACL,
integration policy — đều được phiên bản hóa; và *dấu phiên bản* được ghi vào provenance
của từng claim thu nhận được.

```turtle
ex:recB_1  ex:pipelineVersion  "acq-int-v7.3"^^xsd:string ;
           ex:extractorVersion  "extractor-2.3"^^xsd:string .
```

**Xử lý lại (Reprocessing)** là chạy lại toàn bộ hoặc một phần đường ống trên cùng dữ
liệu nguồn sau khi pipeline đổi phiên bản. Xử lý lại an toàn **chỉ khi** thu nạp lũy đẳng
(§7.14): chạy lại không tạo trùng. Kết quả xử lý lại đi qua *cùng các cổng* như lần đầu
— không được "ưu tiên quá cảnh" vì nghĩ dữ liệu cũ đã biết.

Quan trọng: xử lý lại **không tự động đảo quyết định cũ**. Claim cũ vẫn là sổ cái; ứng
viên mới (từ pipeline mới) đi qua quản trị: có thể củng cố, thay thế (supersede), hoặc
bị bác. Sổ cái không bao giờ bị "ghi đè bằng bản chạy lại".

### Ứng dụng

Khi sửa extraction pattern của nguồn C (FM9: trước đây bỏ sót operation), hệ thống chạy
lại pipeline phiên bản mới trên nguồn C. Các bản ghi mới ra có `pipelineVersion` mới;
claim cũ thiếu operation không bị xóa — nó được thay thế bởi claim mới đầy đủ, với dấu
vết chuyển đổi.

> 🖊 **Tự kiểm tra:** Vì sao "chạy lại pipeline" và "lũy đẳng" đi kèm với nhau? Nếu
> pipeline không lũy đẳng, lần chạy lại tạo ra điều gì — và vì sao điều đó làm hỏng sổ
> cái?

## 7.25 Xử lý theo lô và theo dòng

### Trực giác

Một số nguồn đến theo khối lượng lớn định kỳ (sao chép cơ sở dữ liệu cuối tuần), một số
khác nhỏ giọt liên tục (API cập nhật mỗi phút). Cùng một đường ống khái niệm, hai nhịp
triển khai khác nhau.

### Cơ chế

**Xử lý theo lô (Batch):** toàn bộ dữ liệu nguồn được xử lý trong một lượt định kỳ, kết
quả ghi sổ sau khi lượt hoàn tất. Ưu điểm: kiểm soát tốt, dễ tái lập, dễ kiểm toán theo
lượt. Nhược điểm: sổ cái cũ đi giữa các lượt.

**Xử lý theo dòng (Streaming):** từng phần dữ liệu được xử lý ngay khi đến. Ưu điểm:
kịp thời (timeliness cao). Nhược điểm: phải xử lý *thứ tự*, trạng thái tích hợp có thể
chưa đủ (ứng viên đến trước, nguồn để đối chiếu đến sau).

Bất kể nhịp nào, **các đoạn lô và dòng phải dùng chung logic và phiên bản** — cùng quy
tắc chuẩn hóa, cùng khóa chặn, cùng cổng SHACL. Nếu lô và dòng dùng hai bản logic khác
nhau, cùng dữ liệu đi hai đường sẽ ra hai kết quả khác nhau — và sổ cái không còn giải
thích được vì sao. Đây là một biến thể của FM13 (chính sách trôi).

Với sổ cái: cả hai nhịp đều kết thúc bằng ghi sổ có cam kết (§7.18) — sổ cái không phân
biệt "đến bằng lô hay bằng dòng"; nó chỉ biết claim + provenance.

> ⚠️ **Ngộ nhận phổ biến:** "Streaming là phiên bản hiện đại hơn của batch, nên tốt
> hơn." Sai. Streaming trả giá bằng độ khó kiểm soát thứ tự và trạng thái. Lựa chọn lô
> hay dòng là lựa chọn theo *đặc tính nguồn và yêu cầu kịp thời*, không phải theo mốt.

## 7.26 Các loại nguồn: Có cấu trúc, bán cấu trúc, văn bản

### Trực giác

Ba nguồn của chương đều là văn bản giáo trình. Nhưng nguồn có thể là cơ sở dữ liệu quan
hệ, bảng CSV, tài liệu PDF dài. Mỗi loại có con đường trích xuất riêng — nhưng mọi con
đường đều đổ về cùng các giai đoạn tích hợp.

### Cơ chế

| Loại nguồn | Ví dụ | Con đường vào pipeline | Chuẩn liên quan |
|------------|-------|------------------------|-----------------|
| **Có cấu trúc** (structured) | cơ sở dữ liệu quan hệ | ánh xạ bảng → bộ ba | Direct Mapping, R2RML [@w3c-direct-mapping] [@w3c-r2rml] |
| **Bán cấu trúc** (semi-structured) | CSV, JSON, HTML | khai báo annotation + ánh xạ cột | CSVW + csv2rdf [@w3c-tabular-data-model] |
| **Phi cấu trúc** (unstructured) | văn bản, PDF | chunking → trích xuất (§7.5) | không có chuẩn trích xuất riêng; kết quả là bản ghi ứng viên |

**Chunking** (chia mẩu) áp dụng cho tài liệu dài: tài liệu được chia thành các fragment
có ranh giới và địa chỉ (theo đề mục, đoạn, hoặc kích thước cố định) để trích xuất làm
việc trên đơn vị mạch lạc và provenance mịn. Ranh giới chunk là **một quyết định**: cắt
giữa định nghĩa (FM11) làm hỏng mẩu và hỏng trích xuất.

**Ràng buộc truy hồi (Retrieval Bound):** trích xuất từ một fragment chỉ được khẳng định
những gì *chính fragment đó* chứa đựng, trong ngữ cảnh của nó — không dùng kiến thức từ
các chương sau, bảng bên cạnh, hoặc "kiến thức thế giới" để lấp đầy khoảng trống. Nguồn
A định nghĩa đạo hàm ở §3.2; hệ thống không được gán cho fragment A câu "vận tốc là đạo
hàm của vị trí" chỉ vì nguồn B nói vậy.

Lưu ý: fragment im lặng ≠ phủ định. Fragment A không nhắc "dòng điện" không có nghĩa
fragment A phủ nhận khái niệm dòng điện (vẫn là Open World Assumption, §5–6). Ràng buộc
truy hồi cấm *thêm*, không cấm *thiếu*.

### Ứng dụng

Nguồn A, B, C (văn bản giáo trình) → chunk theo đề mục: mỗi định nghĩa là một chunk.
Nếu nguồn A được cung cấp cả dạng bảng (bảng đạo hàm các hàm cơ bản), bảng đó đi đường
CSVW với annotation, còn định nghĩa dạng văn bản đi đường chunk. Hai luồng gặp nhau ở
bản ghi ứng viên — và từ đó, bất kể nguồn gốc, đều đi chung một đường.

> 🖊 **Tự kiểm tra:** Một fragment nguồn A chứa định nghĩa đạo hàm, không nhắc đến vận
> tốc. Hệ thống được phép khẳng định "đạo hàm là khái niệm toán học" từ fragment này —
> nhưng không được khẳng định "vận tốc là đạo hàm của vị trí" từ *chính* fragment này.
> Vì sao? Sự khác nhau giữa hai khẳng định đó nằm ở đâu?

## 7.27 Lược đồ trích xuất và Giá trị chưa xác định

### Trực giác

Trích xuất phải biết trước mình *sẽ tạo ra bản ghi hình gì*: những trường nào, kiểu gì,
bắt buộc hay tùy chọn. Không có khai báo này, mỗi nguồn ra một kiểu bản ghi tùy hứng —
và các giai đoạn sau không biết đối phó ra sao. Đồng thời, trích xuất có thể *không tìm
ra* một giá trị: hệ thống phải có cách nói "chưa biết" một cách trung thực.

### Cơ chế

**Lược đồ trích xuất (Extraction Schema)** là khai báo cấu trúc của bản ghi trung gian:
danh sách trường, kiểu dữ liệu kỳ vọng, bội số (1..1, 0..n), và miền giá trị cho phép.
Nó làm cho đầu ra trích xuất *dự đoán được và kiểm tra được* — như một hợp đồng giữa
bước trích xuất và các bước sau.

```turtle
ex:ExtractionSchema_Velocity  a        ex:ExtractionSchema ;
                              ex:field  ex:subject     ; ex:fieldKind ex:Required ;
                              ex:field  ex:relation    ; ex:fieldKind ex:Required ;
                              ex:field  ex:object      ; ex:fieldKind ex:Required ;
                              ex:field  ex:unit        ; ex:fieldKind ex:Optional ;
                              ex:field  ex:contextNote ; ex:fieldKind ex:Optional .
```

Khi trích xuất không xác định được một giá trị (đơn vị không ghi trong câu, tài liệu tham
chiếu mơ hồ), có hai cách sai và một cách đúng:

- **Sai — Đoán** — lấp giá trị bằng suy luận ngoài fragment (vi phạm ràng buộc truy hồi).
- **Sai — Bỏ lặng** — vứt trường đó, làm mất dấu vết "đã từng không biết".
- **Đúng — Giá trị chưa xác định (Unresolved Value)** — mô hình hóa tường minh:

```turtle
ex:recC_1  ex:unit  ex:unknownUnit .
```

Chú ý ngữ nghĩa OWA: `ex:unknownUnit` nghĩa là *"hệ thống chưa xác định được đơn vị"*,
không nghĩa là *"không có đơn vị"*, càng không nghĩa là "giá trị mặc định". Chưa biết ≠
không tồn tại (§6.20 — phủ định khác vắng mặt).

> ⚠️ **Ngộ nhận phổ biến:** "Không trích xuất được thì để trống là vô hại." Sai. Giá trị
> trống bị các bước sau xử lý như "không có giá trị" — khác với "chưa xác định". Để trống
> làm biến dạng: khử trùng có thể coi hai bản ghi "thiếu đơn vị" là trùng nhau dù thực tế
> đơn vị khác nhau. Phải ghi tường minh "unknown".

## 7.28 Integration Policy: Quy tắc điều khiển quyết định

### Trực giác

Những quyết định trong §7.17 không phải tùy hứng — chúng tuân theo một bộ quy tắc khai
báo, được xem xét như một artifact. Bộ quy tắc đó là **integration policy**.

### Cơ chế

**Integration Policy** là tập quy tắc phiên bản hóa quyết định cách tích hợp hoạt động:
ngưỡng nào thì chấp nhận, xung đột nào phải đưa người xem, echo source bị xử lý thế nào,
bằng chứng độc lập yêu cầu ra sao, khi nào supersede. Nó *vận hành hóa* quản trị của
Chương 6 trên đường ống của Chương 7.

Nền tảng lý thuyết đến từ lý thuyết tích hợp dữ liệu: một hệ tích hợp được hình thức hóa
thành ba thành phần (lược đồ toàn cục G, lược đồ nguồn S, mapping M) [@lenzerini-2002].
Hai khái niệm quan trọng:

- **GAV (global-as-view):** lược đồ toàn cục được biểu diễn *qua* các nguồn — dễ truy
  vấn, khó thêm nguồn mới.
- **LAV (local-as-view):** các nguồn được biểu diễn *theo* lược đồ toàn cục — dễ thêm
  nguồn, khó truy vấn.
- Mapping có thể **sound** (dữ liệu là tập con của khẳng định), **complete** (tập cha),
  hoặc **exact** (cả hai).

Sách không yêu cầu triển khai GAV/LAV cụ thể — nó dùng khung này để dạy bài học cốt lõi:
**tích hợp là một quyết định mapping với một ngữ nghĩa được chọn**, không phải phép
trộn cơ học. Chính sách của sách quy định phía tích hợp *theo ngữ nghĩa nào* (mặc định:
sound — không khẳng định quá những gì nguồn cho phép).

Ví dụ các quy tắc chính sách:

```turtle
ex:policy_v1  a          ex:IntegrationPolicy ;
              ex:rule    ex:rule_review_on_value_conflict ;   # xung đột giá trị → người xem
              ex:rule    ex:rule_echo_not_independent ;       # echo không tính bằng chứng độc lập
              ex:rule    ex:rule_sound_mapping_default .      # mapping theo ngữ nghĩa sound
```

Chính sách là một artifact phiên bản hóa (§7.24) — sửa chính sách không sửa lịch sử quyết
định, nhưng các quyết định sau đó tuân theo bản mới.

## 7.29 Ranh giới giao dịch: Transaction Boundary

### Trực giác

Ghi sổ cái nhiều claim cùng một lúc — một nửa ghi được, nửa kia lỗi — sẽ làm sổ cái ở
trạng thái "nửa hoàn thành". Cần xác định đơn vị cam kết: **cái gì ghi thì ghi hết, hoặc
không ghi gì**.

### Cơ chế

**Ranh giới giao dịch (Transaction Boundary)** xác định nhóm thao tác được cam kết như
một đơn vị nguyên tử. Trong đường ống của sách, ranh giới mặc định là *một quyết định
tích hợp đi kèm các hệ quả của nó*: chèn/củng cố/supersede/hợp nhất + ghi lý do + ghi
provenance + cập nhật chiếu hình — tất cả cùng cam kết, hoặc cùng hủy.

Vì sao cần? Vì sổ cái không được ở trạng thái "claim mới đã ghi nhưng lý do bị mất"
(vi phạm bất biến I7, §7.30). Giao dịch đảm bảo *hoặc toàn bộ, hoặc không gì* — sổ cái
luôn là một trạng thái hợp lệ.

> 🖊 **Tự kiểm tra:** Giao dịch ghi claim + evidence + decision rationale. Nếu bước ghi
> rationale thất bại mà claim vẫn được giữ, hậu quả là gì? Bất biến nào bị vi phạm?

## 7.30 Bảy bất biến của đường ống: I1–I7

### Trực giác

Kỷ luật của cả chương có thể gói vào bảy quy tắc không được phép vi phạm. Mỗi bất biến
bảo vệ một chiều: truy nguyên, minh bạch, không phá hủy.

### Cơ chế

**Bất biến (Invariants)** là các ràng buộc mà đường ống *không bao giờ* được vi phạm —
được kiểm tra tự động và bằng kiểm toán. Bảy bất biến của sách:

| # | Bất biến | Ý nghĩa | Bảo vệ chống |
|---|----------|---------|--------------|
| **I1** | Mọi claim trong sổ cái có provenance tới ít nhất một fragment nguồn | Không claim "mọc từ hư không" | FM6, FM8, đánh mất nguồn gốc |
| **I2** | Mọi cạnh provenance mang dấu phiên bản pipeline | Biết claim sinh ra bởi pipeline nào | FM13, chính sách trôi |
| **I3** | Content hash định danh duy nhất nội dung chuẩn hóa trong một nguồn | Khử trùng và lũy đẳng hoạt động đúng | FM7, FM2 |
| **I4** | Báo cáo validation đi kèm mọi ứng viên qua tích hợp | Quyết định nhìn thấy conformance | FM8, lẫn lộn validation/acceptance |
| **I5** | Không claim nào bị ghi đè — chỉ chuyển trạng thái | Sổ cái bất biến, bảo toàn mâu thuẫn (Ch6) | FM ghi đè, mất lịch sử |
| **I6** | Thu nạp lại cho cùng trạng thái sổ cái (lũy đẳng) | Chạy lại vô hại | FM7, trùng lặp |
| **I7** | Mọi quyết định có lý do được ghi lại | Quyết định không tùy hứng | FM4, FM5, mất trách nhiệm |

Bất biến I1–I7 không đảm bảo *đúng* — chúng đảm bảo *không hỏng về mặt kỷ luật*. Một hệ
thống tuân đủ bảy bất biến vẫn có thể chứa claim sai (nguồn sai, quy tắc sai); nhưng mọi
claim sai đều *truy nguyên được, giải thích được, và sửa được* mà không phá hủy dấu vết.

> ⚠️ **Ngộ nhận phổ biến:** "Hệ thống tuân bất biến → dữ liệu đúng." Sai. Bất biến là
> điều kiện của *kỷ luật quá trình*, không phải điều kiện của *chân lý nội dung*. Phân
> biệt này song song với conformance ≠ truth (Ch5) và acceptance ≠ truth (Ch6).

## 7.31 Ví dụ Mechanism KG: Trọn vòng thu nhận – tích hợp cho RATE_OF_CHANGE

### Trực giác

Ghép toàn bộ pipeline vào một ca làm việc cụ thể: ba nguồn A, B, C đưa vào hệ thống, qua
mười một giai đoạn, và kết thúc với một trạng thái sổ cái có thể truy vấn.

### Cơ chế: hành trình của ba luồng

![RATE_OF_CHANGE trọn vòng: ba nguồn qua thu nhận, gặp nhau ở tích hợp, qua cổng SHACL, về sổ cái — kết thúc với claim_vroc được củng cố và current_1 ở hàng đợi.](figures/generated/ch07-acquisition-full.pdf)

**Giai đoạn 1 — Đăng ký (§7.3):** `src:sourceA`, `src:sourceB`, `src:sourceC` được đăng
ký với hồ sơ tin cậy.

**Giai đoạn 2 — Quan sát (§7.4):** ba định nghĩa thành ba fragment + ba observation:
`ex:obsA_1` (đạo hàm), `ex:obsB_1` (vận tốc), `ex:obsC_1` (dòng qua tụ).

**Giai đoạn 3 — Trích xuất (§7.5):** `ex:recA_1`, `ex:recB_1`, `ex:recC_1` với ba
Extraction Activity, độ tin cậy trích xuất ghi cho từng bản (§7.6).

**Giai đoạn 4 — Chuẩn hóa (§7.7):** đơn vị, ký hiệu về dạng chính tắc.

**Giai đoạn 5 — Cấu trúc hóa (§7.8):** `ex:mechA_1`, `ex:mechB_1`, `ex:mechC_1` dưới
lược đồ cơ chế.

**Giai đoạn 6 — Định danh (§7.9–7.10):** khóa chặn gom cặp so sánh; Fellegi–Sunter cho
ra: (A, B) → "có thể trùng", đưa người xem; (B, C) → "không trùng" (đầu vào/output khác);
(A, C) không nằm cùng khối chặn.

**Giai đoạn 7 — Gióng lược đồ (§7.11):** A: "derivative of f" ↔ `ex:derivativeOperation_1`;
B: "velocity"/"position" ↔ `ex:velocity_1`/`ex:position_1`; C: "current"/"voltage" →
không tương ứng, gợi ý tạo khái niệm mới.

**Giai đoạn 8 — Khử trùng (§7.13):** hai bản ghi A và B sau xác nhận — cùng mệnh đề
"rate of change theo thời gian" — được nhận diện trùng nội dung.

**Giai đoạn 9 — Cổng SHACL (§7.15):** `ex:mechC_1` thiếu `hasOperation` → không hợp lệ →
hàng đợi xem xét. A, B hợp lệ.

**Giai đoạn 10 — Xung đột + quyết định (§7.16–7.17):** không xung đột giữa A và B (cùng
mệnh đề sau gióng lược đồ). Quyết định: chấp nhận cụm (A, B) → **strengthen** claim đã có
`ex:claim_vroc` trong sổ cái (đã Accepted từ Chương 6, nay có thêm bằng chứng A); quyết
định của C là *defer* (chờ xem xét).

**Giai đoạn 11 — Ghi sổ (§7.18):** claim `ex:claim_vroc` được củng cố, ghi quyết định +
rationale + pipelineVersion trong một giao dịch (§7.29). Chiếu hình cập nhật.

### Kết quả trong sổ cái

```turtle
ex:claim_vroc  a               ex:Claim ;
               ex:content      ex:prop_velocity_rate_of_change ;
               ex:hasEvidence  ex:recB_1 , ex:recA_1 ;      # hai nguồn độc lập
               ex:status       ex:Accepted ;
               ex:pipelineVersion  "acq-int-v7.3"^^xsd:string .
```

Truy vấn chiếu hình:

```sparql
SELECT ?claim ?status WHERE {
  ?claim ex:content ex:prop_velocity_rate_of_change ;
         ex:status ?status .
}
```

Trả về: `ex:claim_vroc | Accepted` (củng cố). Còn `ex:current_1` — khái niệm mới từ C —
*vẫn là ứng viên*: chưa Accepted, chưa vào chiếu hình, đang chờ người xem xét xác nhận
ánh xạ và operation.

## 7.32 Diễn tập hỏng hóc: Một ca đi sai toàn bộ

### Trực giác

Lý thuyết đẹp nhất cũng phải đối mặt với ca hỏng. Mục này dẫn một ca trong đó *nhiều*
kiểu hỏng xảy ra cùng lúc — và cho thấy các bất biến bắt lỗi từng bước như thế nào.

### Diễn tập

**Ca:** hệ thống thu nhận nguồn E — một bài báo khoa học phổ thông tóm tắt về "đạo hàm,
vận tốc và dòng điện trong tụ".

**FM11 (chunking phá nghĩa):** bước chunk cắt đôi câu định nghĩa dòng qua tụ → fragment
thiếu nửa sau → trích xuất `ex:recE_1` ra "current = C × (dV" — vô nghĩa, thiếu "/dt)".

**FM9 (thu nhận một phần):** pipeline báo completeness dưới mức — fragment thứ hai của
bài báo (định nghĩa vận tốc, chép từ nguồn B) không được lên lịch xử lý.

**FM3 (mất recall):** khóa chặn xếp `ex:recE_1` (current) cùng khối với `ex:mechC_1` —
tốt — nhưng *không* cùng khối với `ex:mechB_1`, vì "current" và "velocity" khác chữ cái
đầu. Cặp (E, B) không bao giờ được so sánh → hệ thống không phát hiện E chép B.

**FM7 (mất lũy đẳng):** do bản ghi E được tạo với dấu thời gian biến thiên trong content
hash (hash tính trên trường thời gian — sai quy tắc §7.14), lần chạy lại tạo bản ghi E′
"khác" E → hai bản ghi trùng trong bộ đệm.

**FM8 (lẫn lộn validation/acceptance):** `ex:recE_1` sửa tay cho "hợp lệ" rồi được đưa
vào tích hợp mà không có báo cáo validation kèm theo — vi phạm I4.

**Các bất biến bắt lỗi:**

| Bất biến | Phát hiện | Phản ứng |
|----------|-----------|----------|
| I3 (hash duy nhất) | bản ghi E và E′ cùng nội dung nhưng khác hash → nghi FM2/FM7 | rà quy tắc hash, phát hiện trường thời gian bị băm |
| I4 (validation đi kèm) | `ex:recE_1` không có báo cáo → chặn ở cổng tích hợp | đưa vào hàng đợi, không vào sổ cái |
| I1 (provenance đủ) | fragment bị cắt đôi → provenance mơ hồ → claim không đủ điều kiện | chỉnh chunk, chạy lại |
| I6 (lũy đẳng) | chạy lại sau sửa hash → không tạo bản sao mới | xác nhận lũy đẳng phục hồi |
| I2 (phiên bản) | mọi bản ghi mới mang phiên bản mới; bản cũ giữ nguyên | kiểm toán được toàn bộ diễn biến |

**Kết quả:** sổ cái *không bị nhiễm* — không claim nào từ E vào chiếu hình. Bộ đệm chứa
các bản ghi lỗi nhưng tất cả đều có dấu vết, phiên bản, và lý do; hệ thống sửa từng kiểu
hỏng (chunk, khóa chặn, hash, cổng), chạy lại, và lần chạy lại đúng quy trình. Bài học:
**hỏng hóc là bình thường; phản ứng có kỷ luật mới là điều phân biệt hệ thống tốt.**

> 🖊 **Tự kiểm tra:** Trong ca diễn tập, nếu hệ thống *không có* I3, kiểu hỏng nào sẽ
> âm thầm đi qua? I6 bảo vệ chống ca gì sau khi sửa hash?

## 7.33 Truy vấn trạng thái thu nạp và Quan sát hệ thống

### Trực giác

Người vận hành cần nhìn *bên trong* đường ống: nguồn nào đã đăng ký, fragment nào còn
chờ, ứng viên nào đang trong hàng đợi, lần chạy gần nhất ra sao. Không có khả năng này,
đường ống là một hộp đen — và mọi kiểu hỏng đều thành "không rõ nguyên nhân".

### Cơ chế

**Truy vấn trạng thái thu nạp:** các vật phẩm của đường ống (artifacts) là dữ liệu RDF —
vì vậy có thể truy vấn bằng SPARQL. Ví dụ: đếm ứng viên đang chờ xem xét:

```sparql
SELECT ?fragment (COUNT(?rec) AS ?pending) WHERE {
  ?rec a ex:ExtractedRecord ;
       ex:fromObservation/ ex:extractedFrom ?fragment .
  FILTER NOT EXISTS { ?rec ex:decision ?d . }
} GROUP BY ?fragment
```

**Quan sát hệ thống (Observability):** mỗi giai đoạn xuất ra số đo — số fragment xử lý,
số bản ghi trích xuất, độ tin cậy trung bình, số ca qua cổng SHACL, số quyết định
accept/reject/defer, tồn đọng hàng đợi. Các số đo này *bản thân là dữ liệu pipeline* và
phải lưu với phiên bản + thời gian — để "lần chạy tuần 34 ra sao" trả lời được.

Bài học cốt lõi: observability không phải là "thêm màn hình" — nó là *điều kiện để các
tín hiệu phát hiện của §7.22 tồn tại*. Một kiểu hỏng không có số đo theo dõi là một kiểu
hỏng không bao giờ được phát hiện đúng lúc.

## 7.34 Giới hạn của chương: Không giải bài toán học quy nạp

### Trực giác

Chương này dạy *đưa tri thức vào* và *hợp nhất tri thức*. Có một bài toán lớn hơn mà
chương **cố ý không giải**: làm sao để suy ra tri thức mới mà không có ở bất kỳ nguồn nào.

### Cơ chế

Sáu chương trước đã xử lý suy diễn *suy luận* (deductive): kết luận logic tuân theo từ
tiền đề (Ch4–5). Chương 7 xử lý *thu nhận và tích hợp*: tri thức nguồn được đưa vào hệ
thống nguyên vẹn theo nghĩa "có ở nguồn". Còn **học quy nạp (inductive learning)** — rút
ra quy luật/khái niệm mới từ dữ liệu, chẳng hạn "từ 1000 bản ghi vận tốc, suy ra công
thức tổng quát" — **không được giải trong chương này**.

Vì sao cố ý loại ra?

1. **Khác bản chất tri thức luận.** Tri thức quy nạp là *giả thuyết* — bản chất khác
   với tri thức nguồn. Trộn hai loại sẽ phá vỡ ngữ nghĩa quản trị của Chương 6 (giả
   thuyết học máy không phải claim có nguồn).
2. **Khác chuẩn mực.** Thu nhận/tích hợp có chuẩn ổn định (R2RML, CSVW, Direct Mapping,
   Fellegi–Sunter). Học quy nạp là một miền nghiên cứu đang phát triển, không có "chuẩn
   nền" tương đương.
3. **Đủ lớn cho một chương riêng.** Nếu có, nó xứng đáng một chương độc lập — với ngữ
   nghĩa riêng về "giả thuyết", "xác nhận", "phản bác".

Nếu máy học xuất hiện trong hệ thống của sách, đầu ra của nó là **CandidateKnowledge**
(Chương 6 §6.16): một loại ứng viên cần bằng chứng độc lập, đi qua các cổng như mọi ứng
viên khác — không bao giờ tự động Accepted.

> ⚠️ **Ngộ nhận phổ biến:** "Pipeline thu nhận có trích xuất bằng ML → chương này dạy
> học máy." Sai. Trích xuất có thể dùng công cụ ML, nhưng *sản phẩm* vẫn là bản ghi ứng
> viên từ nguồn — không phải giả thuyết quy nạp mới. Trộn "công cụ ML trong pipeline" với
> "học quy nạp" là một lỗi khái niệm.

## 7.35 Tóm tắt chương

**Thu nhận (Acquisition)** đưa nội dung nguồn vào hệ thống qua: đăng ký (Source
Artifact, §7.3) → quan sát theo mẩu (Source Fragment, §7.4) → trích xuất có ghi activity
và độ tin cậy (§7.5–7.6) → chuẩn hóa (§7.7) → cấu trúc hóa theo lược đồ đích (§7.8).
Kết quả: **tri thức ứng viên** — có cấu trúc, truy nguyên, chưa được quản trị.

**Tích hợp (Integration)** hợp nhất các luồng ứng viên qua: nghị quyết định danh với
sinh ứng viên/chấm điểm Fellegi–Sunter (§7.9–7.10) → gióng lược đồ và ánh xạ
(Direct Mapping/R2RML, §7.11–7.12) → khử trùng bảo toàn (§7.13) → thu nạp lũy đẳng bằng
content hash (§7.14) → cổng SHACL với conformance ≠ acceptance (§7.15) → phát hiện xung
đột theo phân loại Chương 6 (§7.16) → quyết định/merge outcome (§7.17) → ghi sổ cái
trước, chiếu hình từ sổ cái (§7.18) → lineage khác evidence (§7.19) → người trong vòng
lặp qua hàng đợi (§7.20).

**Kỷ luật vận hành:** chất lượng đa chiều (§7.21); 13 kiểu hỏng hóc — mỗi kiểu có tín
hiệu và phục hồi (§7.22); echo source không tính là bằng chứng độc lập (§7.23); phiên
bản hóa pipeline và xử lý lại an toàn nhờ lũy đẳng (§7.24); lô hay dòng là lựa chọn theo
đặc tính nguồn, chung logic (§7.25); nguồn có cấu trúc/bán cấu trúc/văn bản — mọi đường
đổ về chung các giai đoạn tích hợp (§7.26); lược đồ trích xuất và giá trị chưa xác định
mô hình hóa tường minh (§7.27); integration policy phiên bản hóa — tích hợp là quyết
định mapping có ngữ nghĩa (§7.28); ranh giới giao dịch nguyên tử cho việc ghi sổ
(§7.29); bảy bất biến I1–I7 (§7.30). Học quy nạp không thuộc chương này (§7.34).

**Nối tiếp Chương 6:** sổ cái phát biểu của Ch6 giờ đây có một *con đường vào*: đường
ống này là nơi các claim mới được sinh ra, đánh giá, và ghi sổ — với đầy đủ provenance,
bằng chứng, và quản trị. RATE_OF_CHANGE vẫn là sợi chỉ xuyên suốt: `ex:claim_vroc`
Accepted trong sổ cái (Ch6) được củng cố bởi bằng chứng mới từ nguồn A qua pipeline
(§7.31) — còn `ex:current_1` của nguồn C nằm lại ở hàng đợi, chờ xác nhận, không vội
đồng nhất với vận tốc.

## 7.36 Mechanism Knowledge System — Năng lực đạt được

**TRƯỚC CHƯƠNG NÀY** — hệ thống có tầng tri thức luận (Ch6): claim có nguồn, bằng
chứng, thời gian, trạng thái quản trị. Nhưng mọi claim đều *được đưa vào sổ cái bằng
tay*: `claim_vroc` được soạn sẵn, coi như đã có provenance. Không có câu hỏi "tri thức
mới đến từ đâu?", "hai nguồn nói cùng một thứ nhưng khác lược đồ thì xử lý ra sao?",
"chạy lại pipeline có tạo trùng không?".

**SAU CHƯƠNG NÀY** — hệ thống có một đường ống thu nhận và tích hợp đứng *trước* sổ cái:
- **Thu nhận:** nguồn được đăng ký (`Source Artifact`), nội dung được quan sát theo mẩu
  (`Source Fragment`), trích xuất thành bản ghi ứng viên có `Extraction Activity` + độ tin
  cậy trích xuất (§7.3–7.6), chuẩn hóa và cấu trúc hóa theo lược đồ đích (§7.7–7.8).
- **Tích hợp:** nghị quyết định danh bằng sinh ứng viên + Fellegi–Sunter (§7.9–7.10);
  gióng lược đồ và ánh xạ Direct Mapping/R2RML/CSVW (§7.11–7.12); khử trùng bảo toàn và
  thu nạp lũy đẳng bằng content hash (§7.13–7.14); cổng SHACL với conformance ≠
  acceptance (§7.15); xung đột theo phân loại Ch6 và quyết định tích hợp có lý do
  (§7.16–7.17).
- **Sổ cái trước:** mọi thứ vào sổ cái qua quyết định được ghi; chiếu hình dựng từ sổ
  cái; lineage lần ngược tới fragment, khác với evidence (§7.18–7.19); con người xem xét
  qua hàng đợi (§7.20).
- **Kỷ luật:** chất lượng đa chiều; 13 kiểu hỏng hóc có tín hiệu; echo source không tính
  bằng chứng độc lập; phiên bản hóa pipeline; ranh giới giao dịch; bảy bất biến I1–I7
  (§7.21–7.30).

**VÍ DỤ RATE_OF_CHANGE CỤ THỂ** — ba nguồn (Giải tích A, Cơ học B, Điện tử C) cùng nói
"tốc độ thay đổi theo thời gian". Sau pipeline: nguồn A và B được xác nhận cùng mệnh đề
`ex:prop_velocity_rate_of_change` sau gióng lược đồ, khử trùng thành một claim được củng
cố trong sổ cái (§7.31). Nguồn C (`current = C·dV/dt`) **không** bị đồng nhất với vận tốc:
định danh cho "không trùng", gióng lược đồ không tìm thấy tương ứng, cổng SHACL bắt
thiếu operation → `ex:current_1` nằm ở hàng đợi xem xét. Câu trả lời của §7.0: "ba nguồn
nói cùng một khái niệm?" — hóa ra là *không hẳn*: A và B là một, C thì không. Không có
pipeline, hệ thống đã vội gộp cả ba và làm hỏng ontology cơ chế.

**VẪN CHƯA GIẢI QUYẾT** — đường ống giả định *nguồn đã có sẵn, nội dung đã đầy đủ*.
Ba bài toán còn mở: (1) **học quy nạp** — suy ra tri thức mới không có ở nguồn (không
thuộc chương này, §7.34); (2) **lựa chọn nguồn tự động** — khi có hàng nghìn nguồn, chọn
nguồn nào đáng thu nhận là một bài toán riêng; (3) **trích xuất ngữ nghĩa sâu** — bắt
chính xác ý nghĩa của văn bản tự nhiên vẫn là một miền đang phát triển, không phải một
công đoạn có chuẩn nền. Chương 8 (nếu có) mở ra nấc tiếp theo: dùng đồ thị đã tích hợp
để *suy diễn và truy vấn tri thức ở quy mô lớn* — nơi những claim đã ghi sổ trở thành
tiền đề.

## Thuật ngữ đã gặp trong chương này

| Thuật ngữ | Nghĩa ngắn | Học chi tiết |
|-----------|-----------|--------------|
| Acquisition (thu nhận) | Đưa nội dung nguồn vào hệ thống thành tri thức ứng viên | §7.2 |
| Integration (tích hợp) | Hợp nhất, đối chiếu, xác nhận trước khi ghi sổ | §7.2 |
| Source Artifact | Bản ghi đăng ký của nguồn, có IRI và siêu dữ liệu | §7.3 |
| Source Fragment | Phần con được đánh địa chỉ của nguồn | §7.4 |
| Observation | Dữ liệu thô thu từ fragment, trước khi diễn giải | §7.4 |
| Extraction / Extraction Activity | Trích xuất bản ghi ứng viên + Activity PROV ghi việc thực thi | §7.5 |
| Extraction Confidence | Độ tin cậy *của việc trích xuất*, không phải của nội dung | §7.6 |
| Normalization (chuẩn hóa) | Đưa giá trị về dạng chính tắc để so sánh; có thể mất thông tin | §7.7 |
| Structuring (cấu trúc hóa) | Bản ghi chuẩn hóa → bộ ba RDF theo lược đồ đích | §7.8 |
| Entity Resolution | Quá trình quyết định "hai bản ghi là một thực thể?" | §7.9 |
| Candidate Generation / Blocking | Sinh cặp đáng xem bằng khóa chặn (ưu tiên recall) | §7.9 |
| Record Linkage (Fellegi–Sunter) | So sánh vector γ, m/u, hai ngưỡng: khớp / xem xét / không | §7.10 |
| Schema Alignment | Tìm tương ứng ngữ nghĩa giữa các phần tử lược đồ | §7.11 |
| Direct Mapping / R2RML / CSVW | Ánh xạ mặc định / ánh xạ tùy biến / tabular→RDF (chuẩn W3C) | §7.12 |
| Deduplication (khử trùng) | Nhận diện trùng nội dung và hòa giải, không xóa | §7.13 |
| Idempotent Ingestion | Chạy lại cho cùng trạng thái sổ cái | §7.14 |
| Content Hash | Vân tay nội dung chuẩn hóa; khóa khử trùng/lũy đẳng | §7.14 |
| SHACL gate | Cổng kiểm tra hình dạng; conformance ≠ acceptance | §7.15 |
| Conflict Detection | Tìm cặp không thể cùng đúng trong cùng ngữ cảnh | §7.16 |
| Merge Outcome | Insert / strengthen / supersede / merge — bảo toàn cả hai bên | §7.17 |
| Claim Ledger First | Sổ cái là nguồn chân lý duy nhất; chiếu hình dựng từ sổ cái | §7.18 |
| Lineage vs Evidence | "Từ đâu đến?" khác "vì sao tin?" | §7.19 |
| Review Queue | Hàng đợi xem xét: possible match, SHACL fail, xung đột | §7.20 |
| Data Quality Dimensions | 6 chiều; không có một con số "chất lượng" | §7.21 |
| Failure Modes | 13 kiểu hỏng hóc, mỗi kiểu có tín hiệu + phục hồi | §7.22 |
| Echo Source | Nguồn phái sinh; không tính là bằng chứng độc lập | §7.23 |
| Pipeline Versioning | Mọi thành phần định hình đầu ra được phiên bản hóa | §7.24 |
| Batch vs Streaming | Hai nhịp xử lý; chung logic, khác nhịp | §7.25 |
| Chunking / Retrieval Bound | Chia mẩu tài liệu; chỉ khẳng định điều mẩu tự nội hàm | §7.26 |
| Extraction Schema / Unresolved Value | Khai báo cấu trúc bản ghi; "chưa biết" mô hình hóa tường minh | §7.27 |
| Integration Policy | Bộ quy tắc phiên bản hóa điều khiển quyết định tích hợp | §7.28 |
| Transaction Boundary | Ghi sổ nguyên tử: hoặc toàn bộ, hoặc không gì | §7.29 |
| Invariants I1–I7 | Bảy bất biến bảo vệ truy nguyên, không ghi đè, lũy đẳng | §7.30 |

## Tài liệu tham khảo

- R2RML: RDB to RDF Mapping Language [@w3c-r2rml]
- A Direct Mapping of Relational Data to RDF [@w3c-direct-mapping]
- Model for Tabular Data and Metadata on the Web (CSVW) [@w3c-tabular-data-model]
- A Theory for Record Linkage (Fellegi & Sunter) [@fellegi-sunter-1969]
- A Survey of Approaches to Automatic Schema Matching (Rahm & Bernstein) [@rahm-bernstein-2001]
- Data Integration: A Theoretical Perspective (Lenzerini) [@lenzerini-2002]
- Shapes Constraint Language (SHACL) [@w3c-shacl]
- PROV-O: The PROV Ontology [@prov-o]
- PROV Data Model (PROV-DM) [@prov-dm]
- Knowledge Graphs (Hogan et al.), Creation and Enrichment [@hogan-creation-enrichment]


