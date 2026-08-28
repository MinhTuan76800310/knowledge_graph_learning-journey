# Content Audit: Chương 1 & Chương 2 — Knowledge Graph Book

> Đối tượng: bản preview PDF hiện tại (Chương 1 + Chương 2).
> Mục đích: liệt kê những khái niệm / thuật ngữ / ký hiệu được **giới thiệu sớm hơn so với lời giải thích**, hoặc chỉ được nhắc đến ngắn gọn đến mức đọc giả chưa hiểu. Dùng làm đầu vào trước khi sửa nội dung.

---

## 1. Phương pháp đánh giá

- ọc tuần tự `book/chapter01.md` và `book/chapter02.md` từ đầu đến cuối theo góc nhìn đọc giả lần đầu.
- Kiểm tra quy ước của dự án: thuật ngữ kỹ thuật xuất hiện lần đầu phải kèm **giải thích tiếng Việt hoặc chú thích ngắn**.
- Tập trung vào các khái niệm **được sử dụng trước khi được định nghĩa**, hoặc chỉ được nhắc qua một lần mà không đủ để hiểu.

---

## 2. Chương 1 — “Từ Đồ thị đến Tri thức”

### 2.1. Thuật ngữ / ký hiệu được dùng trước khi giải thích

| STT | Thuật ngữ | Vị trí | Vấn đề | Đề xuất sửa |
|-----|-----------|--------|--------|-------------|
| 1 | **IRI** | §1.3, dòng ~121: “Entity có identity (danh tính) — thường là IRI trong RDF…” | IRI chưa được định nghĩa; RDF cũng chưa. | Thêm chú thích: “IRI (Internationalized Resource Identifier — định danh toàn cục dạng chuỗi, sẽ học ở Chương 2)”. |
| 2 | **RDF** | §1.3, dòng ~121 (kèm IRI), ~256, ~279, ~305 | RDF xuất hiện nhiều lần nhưng chưa được giải thích tại chỗ. | Thêm chú thích ngắn lần đầu: “RDF (Resource Description Framework — mô hình dữ liệu đồ thị bộ ba chuẩn W3C, sẽ học ở Chương 2)”. |
| 3 | **RDFS** | §1.3, dòng ~105: “có ngữ nghĩa RDFS (domain/range dùng để suy diễn kiểu)”; dòng ~256 | RDFS chỉ được gọi tên; domain/range cũng chưa giải thích. | Giải thích: “RDFS (RDF Schema — tầng lược đồ/lớp của RDF, sẽ học ở Chương 4)”. Giải thích domain/range ngay sau đó. |
| 4 | **OWL** | §1.3, dòng ~204; §1.7, dòng ~279, ~285 | OWL xuất hiện nhưng chưa được định nghĩa. | Thêm: “OWL (Web Ontology Language — ngôn ngữ bản thể học, sẽ học ở Chương 4)”. |
| 5 | **domain / range** | §1.3, dòng ~105, ~163, ~204, ~256 | Hai khái niệm quan trọng của RDFS/OWL được nhắc liên tục mà chưa định nghĩa. | Khi xuất hiện lần đầu, giải thích: “domain (miền: loại thực thể làm chủ thể) và range (phạm vi: loại thực thể làm đối tượng) của một quan hệ”. |
| 6 | **Schema** | §1.2 hình; §1.4, dòng ~150, ~163 | Xuất hiện trong mô hình tinh thần nhưng chưa định nghĩa ở Chương 1. | Thêm định nghĩa ngắn: “schema (lược đồ): mô tả cấu trúc và từ vựng được kỳ vọng của đồ thị dữ liệu”. |
| 7 | **Provenance** | §1.2 hình; §1.4, dòng ~150, ~175, ~209, ~312 | Nằm trong `Context` nhưng chưa được định nghĩa. | Giải thích: “provenance (nguồn gốc dữ liệu: ai/đâu/bằng cách nào tạo ra phát biểu này)”. |
| 8 | **Scope / Confidence** | §1.4, dòng ~150, ~175 | Nằm trong Context nhưng chưa giải thích. | Giải thích ngắn: “scope (phạm vi áp dụng)” và “confidence (độ tin cậy)”. |
| 9 | **SHACL** | §1.6, dòng ~262: “ràng buộc SHACL (data → constraint check → conforms/violation)” | SHACL là gì chưa được giải thích. | Thêm: “SHACL (Shapes Constraint Language — ngôn ngữ ràng buộc dữ liệu RDF, sẽ học ở Chương 5)”. |
| 10 | **Cardinality** | §1.4, dòng ~166: “SHACL shapes, cardinality” | Khái niệm chưa giải thích. | Giải thích: “cardinality (số lượng giá trị được phép của một quan hệ/thuộc tính)”. |
| 11 | **Entailment** | §1.4, dòng ~167; §1.6, dòng ~262 | Dùng trong câu quan trọng phân biệt suy diễn và xác nhận. | Thêm: “entailment (suy diễn logic: kết luận mới được suy ra từ các tiên đề)”. |
| 12 | **Forward-chaining** | Bảng thí nghiệm 1.9, dòng ~330 | Khái niệm chưa giải thích trong bảng. | Thêm chú thích ngắn: “forward-chaining (suy diễn theo chiều thuận: từ luật và dữ liệu suy ra kết luận mới)”. |
| 13 | **N-ary relations** | §1.12, dòng ~359 | Chỉ gọi tên, chưa giải thích. | Thêm: “n-ary relations (quan hệ có nhiều hơn hai thành phần, hoặc quan hệ cần mang thêm thuộc tính)”. |
| 14 | **Named graphs / contextual statements** | §1.12, dòng ~360 | Chỉ gọi tên. | Thêm: “named graph (đồ thị có tên, cho phép gom nhóm phát biểu theo ngữ cảnh)”. |
| 15 | **SPARQL / Cypher** | §1.12, dòng ~356 | Được liệt kê là công cụ chưa học; chưa có chú thích. | Thêm: “SPARQL (truy vấn RDF) và Cypher (truy vấn đồ thị thuộc tính), sẽ học ở Chương 2”. |

### 2.2. Từ viết tắt / chữ cái đầu chưa được giải thích

| STT | Từ viết tắt | Vị trí | Đề xuất |
|-----|-------------|--------|---------|
| 1 | **W3C** | §1.1, dòng ~47; §1.5, dòng ~186 | “W3C (World Wide Web Consortium)”. |
| 2 | **RDF** | Như trên | Giải thích đầy đủ. |
| 3 | **RDFS** | Như trên | Giải thích đầy đủ. |
| 4 | **OWL** | Như trên | Giải thích đầy đủ. |
| 5 | **IRI** | Như trên | Giải thích đầy đủ. |
| 6 | **SHACL** | Như trên | Giải thích đầy đủ. |
| 7 | **AI** | §1.10, dòng ~341: “AI agent” | Có thể thêm “AI (Artificial Intelligence / trí tuệ nhân tạo)” nếu muốn rất chặt chẽ. |

### 2.3. Khái niệm toán / logic học chưa giải thích

| STT | Khái niệm | Vị trí | Đề xuất |
|-----|-----------|--------|---------|
| 1 | **Partial order** | §1.5, dòng ~199 | “partial order (quan hệ thứ tự bộ phận)”. |
| 2 | **Reflexive / transitive / antisymmetric** | §1.5, dòng ~199–200 | Liệt kê “phản xạ, bắc cầu, phản đối xứng” nhưng chưa giải thích nghĩa từng khái niệm. Nên bổ sung ví dụ hoặc chú thích nhẹ. | Thêm footnote hoặc câu giải thích: ví dụ “phản đối xứng: nếu A là lớp con của B và B là lớp con của A thì A = B”. |
| 3 | **Set notation** `C ⊆ V`, `⊑ ⊆ C × C` | §1.5, dòng ~198–199 | Với kỹ sư có kinh nghiệm có thể hiểu, nhưng nên đảm bảo đọc giả biết `⊆` và `×` là gì. | Có thể giữ nguyên nhưng bổ sung chú thích dịch sang lời. |

### 2.4. Vấn đề kiến trúc / mạch lập luận

1. **Mâu thuẫn với “không có tiên quyết”**: Chương 1 tuyên bố “Không có” tiên quyết, nhưng lại dùng RDF/RDFS/OWL/SHACL/IRI trước khi giải thích. Cần giảm các forward-reference không cần thiết, hoặc chấp nhận Chương 1 phải **preview ngắn** các thuật ngữ này.
2. **Hệ quả của việc dùng thuật ngữ sớm**: đoạn phân biệt `statement → entailment` khác `data → constraint check → conforms/violation` rất quan trọng, nhưng nếu đọc giả chưa biết SHACL/entailment thì câu này mất hiệu quả.
3. **Mô hình tinh thần ba lớp**: các khái niệm `Schema`, `Ontology`, `Identity`, `Constraints`, `Provenance`, `Time`, `Scope`, `Confidence` cần được giải thích ngay trong hình hoặc ngay sau hình, không để đọc giả đoán.

---

## 3. Chương 2 — “Mô hình Dữ liệu và Ngôn ngữ Truy vấn”

### 3.1. Thuật ngữ / định dạng được nhắc nhưng chưa giải thích đủ

| STT | Thuật ngữ | Vị trí | Vấn đề | Đề xuất |
|-----|-----------|--------|--------|---------|
| 1 | **JSON-LD / N-Triples / RDF/XML** | §2.1.5, dòng ~84, ~235 | Liệt kê là các concrete syntax nhưng chưa mô tả. | Thêm bảng/bullet ngắn mô tả từng định dạng (dòng/cú pháp/đặc điểm). |
| 2 | **Linked Data** | §2.1.2, dòng ~95 | Dùng để giải thích lý do IRI tồn tại, nhưng chưa định nghĩa. | Thêm: “Linked Data (dữ liệu liên kết: dữ liệu được định danh bằng IRI để dễ tích hợp giữa các hệ thống)”. |
| 3 | **Namespace** | §2.1.4, dòng ~140–142 | Code dùng `Namespace(...)` nhưng khái niệm namespace chưa giải thích. | Thêm đoạn ngắn: “Namespace (không gian tên) là tiền tố dùng để viết gọn IRI…”. |
| 4 | **RDF / RDFS trong `from rdflib import RDF, RDFS`** | §2.1.4, dòng ~140 | Hai namespace chuẩn được import nhưng chưa giải thích. | Giải thích rằng đây là các namespace chuẩn của W3C; `RDF.type` = `rdf:type`, `RDFS.label` = `rdfs:label`. |
| 5 | **SPARQL** | §2.1.6, dòng ~241 | Tên SPARQL xuất hiện nhưng không giải thích tên đầy đủ. | Thêm: “SPARQL (Simple Protocol and RDF Query Language) — ngôn ngữ truy vấn chuẩn cho RDF”. |
| 6 | **Reification / reifier / triple term** | §2.4.1 bảng so sánh, dòng ~509; §2.4.2, dòng ~528; §2.1.7, dòng ~326–327 | “Tái hiện (reification)” được nhắc nhưng chưa giải thích cơ chế. | Thêm một câu: “reification là kỹ thuật biến một bộ ba thành một tài nguyên để gắn thêm thông tin cho nó; chi tiết ở Chương 3/6”. |
| 7 | **Entailment** | §2.4.1 bảng so sánh, dòng ~512; §2.4.2, dòng ~544 | Dùng trong bảng so sánh nhưng chưa định nghĩa. | Giải thích: “entailment (suy diễn logic)”. |
| 8 | **ISO / ISO/IEC 39075:2024** | §2.3.4, dòng ~485 | Nhắc đến tổ chức ISO và số hiệu chuẩn. | Có thể thêm: “ISO (International Organization for Standardization)”. |
| 9 | **W3C** | §2.0, dòng ~45 | Tổ chức này lần đầu xuất hiện ở Chương 1; cần mở rộng ở Chương 1, không cần lặp lại nhiều. | Đảm bảo giải thích ở Chương 1. |
| 10 | **Serialization / parse** | §2.1.5, dòng ~214, ~216, ~235 | “Serialize” và “parse” được dùng nhiều nhưng chưa định nghĩa trong ngữ cảnh RDF. | Có thể thêm: “serialize = chuyển đồ thị RDF thành văn bản; parse = đọc văn bản thành đồ thị”. |

### 3.2. Từ viết tắt / chữ cái đầu chưa được giải thích

| STT | Từ viết tắt | Vị trí | Đề xuất |
|-----|-------------|--------|---------|
| 1 | **W3C** | Chương 1 (nên mở rộng tại đó) | Giải thích tại Chương 1. |
| 2 | **ISO** | §2.3.4 | Mở rộng: “ISO (International Organization for Standardization)”. |
| 3 | **SPARQL** | §2.1.6 | Mở rộng: “Simple Protocol and RDF Query Language”. |
| 4 | **GQL** | §2.3.4 | Đã giải thích là “Graph Query Language” qua ngữ cảnh, nhưng nên viết rõ: “GQL (Graph Query Language)”. |
| 5 | **JSON-LD** | §2.1.5 | Mở rộng: “JSON for Linked Data”. |
| 6 | **RDF/XML** | §2.1.5 | Không cần mở rộng nếu đã giải thích RDF, nhưng nên gọi tên là “một định dạng tuần tự hóa RDF theo cú pháp XML”. |

### 3.3. Vấn đề kiến trúc / mạch lập luận

1. **Namespace prefix chưa được giải thích như một khái niệm**: Turtle dùng `@prefix ex: <...>` nhưng chưa giải thích “prefix” là gì, chỉ nói là “cách viết tắt”. Cần nói rõ: “prefix (tiền tố) ánh xạ một chuỗi ngắn thành một IRI đầy đủ; ví dụ `ex:Hanoi` mở rộng thành `http://example.org/Hanoi`.”
2. **Sự khác biệt giữa “mô hình” và “cú pháp” được nhấn mạnh đúng**, nhưng các ví dụ cú pháp (Turtle, N-Triples, RDF/XML, JSON-LD) cần ít nhất một câu mô tả từng loại để đọc giả không bị choáng ngợp.
3. **So sánh RDF với Property Graph ở §2.4 dùng thuật ngữ “entailment”, “interoperability”, “serialization”** — các từ này nên được định nghĩa hoặc chú thích trước khi bảng so sánh.

---

## 4. Vấn đề xuyên suốt cả hai chương

### 4.1. Glossary ở cuối sách chưa đủ

- Glossary đặt ở cuối sách; đọc giả đọc Chương 1–2 chưa biết có glossary. Các thuật ngữ cần được **gloss ngay tại lần xuất hiện đầu tiên** trong văn bản chính, không chỉ tra cứu sau.
- Nhiều thuật ngữ trong glossary (`Blank node`, `IRI`, `Entailment`, `Reification`, `Named graph`) chưa xuất hiện đúng cách trong Chương 1–2 (ví dụ `IRI` chưa có dạng “IRI (Internationalized Resource Identifier)” trong văn bản chính).

### 4.2. Quy ước “thuật ngữ Anh + nghĩa Việt” chưa nhất quán

- **Tuân thủ tốt**: `Entity (Thực thể)`, `Relation (Quan hệ)`, `Data Graph (Đồ thị dữ liệu)`, `Taxonomy (Phân loại)`, `Ontology (Bản thể học)`.
- **Chưa tuân thủ / thiếu**: `IRI`, `RDF`, `RDFS`, `OWL`, `SHACL`, `SPARQL`, `JSON-LD`, `W3C`, `ISO`, `Namespace`, `Linked Data`.

### 4.3. Forward reference không cân đối

- Chương 1 liên tục nói “sẽ học ở Chương X”. Điều này không tránh được hoàn toàn, nhưng với các thuật ngữ cốt lõi (RDF, IRI, RDFS, OWL, SHACL) nên có một **preview box ngắn** hoặc **footnote** để đọc giả hiểu sơ bộ, thay vì chỉ gọi tên.

---

## 5. Những điểm cần ưu tiên sửa trước khi tiếp tục

### 5.1. Ưu tiên CAO (nên sửa ngay)

1. **Định nghĩa IRI, RDF, RDFS, OWL, SHACL ngay tại lần xuất hiện đầu tiên trong Chương 1** — đây là nền tảng cho toàn bộ sách.
2. **Giải thích domain/range** khi lần đầu xuất hiện.
3. **Mở rộng W3C, ISO** lần đầu xuất hiện.
4. **Định nghĩa entailment, provenance, schema, cardinality** trong Chương 1.
5. **Mở rộng SPARQL, JSON-LD** trong Chương 2.

### 5.2. Ưu tiên TRUNG BÌNH (nên sửa khi edit lại Chương 1–2)

1. Giải thích namespace, prefix, serialize/parse trong Chương 2.
2. Giải thích reification / triple term / reifier khi nhắc đến.
3. Giải thích linked data trong Chương 2.
4. Bổ sung chú thích cho partial order / reflexive / transitive / antisymmetric.

### 5.3. Ưu tiên THẤP (nice-to-have)

1. Thêm một bảng “Bảng thuật ngữ nhanh” ở cuối Chương 2 để tổng hợp các thuật ngữ đã học.
2. Kiểm tra lại cách dùng `blank node` / `nút trống`, `literal` trong văn bản chính so với glossary để nhất quán.
3. Xem xét thêm một “preview box” ở Chương 1: “Các thuật ngữ W3C (RDF, RDFS, OWL, SHACL, SPARQL) sẽ được học chi tiết ở các chương sau; dưới đây là bản giới thiệu ngắn.”

---

## 6. Khuyến nghị hành động tiếp theo

1. **Tạo một nhánh sửa nội dung** chỉ tập trung vào việc thêm chú thích / định nghĩa cho các thuật ngữ trên.
2. **Ưu tiên Chương 1 trước**, vì nó là cửa ngõ; nếu Chương 1 khó hiểu, đọc giả sẽ bỏ cuốn.
3. **Duy trì quy tắc**: mỗi thuật ngữ kỹ thuật lần đầu xuất hiện phải có dạng `Tiếng Anh (tiếng Việt: nghĩa ngắn)` hoặc chú thích footnote.
4. **Sau khi sửa**, chạy lại bộ đếm từ hoặc grep để kiểm tra xem còn thuật ngữ chưa được giải thích không.

---

*Ghi chú: Các dòng được trích dẫn từ file nguồn Markdown (`book/chapter01.md`, `book/chapter02.md`). Số dòng có thể khác khi chuyển sang PDF.*
