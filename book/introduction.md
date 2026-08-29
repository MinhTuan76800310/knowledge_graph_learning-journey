# Giới thiệu

Chào mừng bạn đến với cuốn sách về **Knowledge Graph** — một giáo trình mã nguồn mở về
Đồ thị Tri thức, từ những nguyên lý nền tảng đến hệ thống tri thức trong thực tế.

## Cuốn sách này dành cho ai?

Cuốn sách dành cho kỹ sư phần mềm có kinh nghiệm, người không chỉ muốn học cách sử dụng Neo4j hay gọi API GraphRAG, mà muốn hiểu **cơ chế** đằng sau Knowledge Graph đủ sâu để tự thiết kế hệ thống tri thức tùy chỉnh cho AI agent.

Nếu bạn đã từng thắc mắc:

- "Tại sao không phải đồ thị nào cũng là Knowledge Graph?"
- "Làm sao máy tính 'hiểu' được ý nghĩa của dữ liệu?"
- "Khi hai nguồn mâu thuẫn nhau, hệ thống nên tin vào đâu?"
- "Suy diễn (inference) khác xác nhận (validation) như thế nào?"
- "Làm sao xây dựng hệ thống tri thức sống, tiến hóa theo thời gian?"

...thì đây là cuốn sách dành cho bạn.

## Mô hình sư phạm

Lấy cảm hứng từ cấu trúc và triết lý học tập của các giáo trình kỹ thuật thực hành hiện đại, cuốn sách này tuân thủ các nguyên tắc:

- **Một trừu tượng thống nhất** xuyên suốt toàn bộ sách: Mental Model 1 (`Knowledge Graph = Data Graph + Semantics + Context`) và Mental Model 2 (`Knowledge System = KG + Acquisition + Inference + Validation + Evolution`).
- **Chương trình tăng dần độ khó**: mỗi chương xây dựng trên nền tảng của chương trước.
- **Lý thuyết đi kèm thực hành**: mỗi khái niệm có experiment đồng hành. Các experiment được triển khai tiến dần theo milestone; hiểu bản thảo không phụ thuộc vào việc chạy chúng. Trạng thái chạy được/hoãn hiện tại được ghi trong repository.
- **Đánh giá độ khó rõ ràng**: ★ (cơ bản), ★★ (trung cấp), ★★★ (thử thách nghiên cứu/thiết kế).
- **Câu hỏi tư duy**: yêu cầu suy luận, không chỉ ghi nhớ.
- **Môi trường tái tạo được**: các experiment chạy cục bộ trên laptop Linux/Windows. Trạng thái từng experiment (chạy độc lập / cần dependency / hoãn) được ghi rõ trong repository.
- **Trạng thái experiment minh bạch**: mỗi experiment ghi rõ là "chạy độc lập", "cần dependency bên ngoài", hay "bài tập thiết kế/nghiên cứu".

## Hai mô hình tinh thần

### Mental Model 1: Knowledge Graph = Data Graph + Semantics + Context

Đây là **mô hình học tập kỹ thuật**, KHÔNG phải định nghĩa chính thức được chấp nhận rộng rãi. Nó giúp phân tách ba lớp:

- **Data Graph**: thực thể (entity), quan hệ (relation), thuộc tính (property) — cấu trúc thuần túy.
- **Semantics**: schema, ý nghĩa, ontology, danh tính (identity), ràng buộc — điều biến đồ thị thành tri thức có ngữ nghĩa.
- **Context**: nguồn gốc (provenance), thời gian, phạm vi, độ tin cậy — điều cho phép xử lý mâu thuẫn và tiến hóa.

### Mental Model 2: Knowledge System = KG + Acquisition + Inference + Validation + Evolution

Mô hình này xuất hiện dần qua các chương và trở thành kiến trúc của capstone project (Chương 10). Một Knowledge Graph đơn lẻ chưa đủ; nó cần:

- **Acquisition**: thu thập tri thức từ nhiều nguồn.
- **Inference**: suy diễn ra tri thức mới từ tri thức hiện có.
- **Validation**: kiểm tra tính hợp lệ và nhất quán.
- **Evolution**: cập nhật, sửa đổi, giải quyết mâu thuẫn theo thời gian.

## Cấu trúc sách

| Chương | Chủ đề | Bạn sẽ đạt được gì |
|--------|--------|---------------------|
| 1 | Từ Đồ thị đến Tri thức | Hiểu KG là gì, tại sao không phải đồ thị nào cũng là KG |
| 2 | Mô hình Dữ liệu và Ngôn ngữ Truy vấn | Biểu diễn và truy vấn bằng RDF/SPARQL và Property Graph/Cypher |
| 3 | Schema, Danh tính và Ngữ cảnh | Mô hình hóa identity, entity resolution, reification, named graphs |
| 4 | Ontology và Ý nghĩa Hình thức | RDFS, OWL, Description Logic, TBox/ABox, open-world assumption |
| 5 | Suy diễn, Quy tắc và Xác nhận | Phân biệt inference vs validation, SHACL, rule engine |
| 6 | Tuyên bố, Bằng chứng, Nguồn gốc, Thời gian và Mâu thuẫn | Claim ≠ Fact, provenance, PROV-O, Wikidata statements |
| 7 | Thu thập và Tích hợp Tri thức | Pipeline extraction → candidate → validation → canonical knowledge |
| 8 | Tri thức Quy nạp và Học từ Đồ thị | Embeddings, link prediction, GNN intuition, uncertainty |
| 9 | Truy xuất, Trả lời Câu hỏi và GraphRAG | Vector vs graph retrieval, hybrid, temporal QA, evidence trails |
| 10 | Xây dựng Hệ thống Tri thức Sống | Capstone: mechanism knowledge system hoàn chỉnh |

## Miền Capstone: Mechanism Knowledge Graph

Thay vì dùng ví dụ rời rạc ở mỗi chương, chúng ta duy trì **một đồ thị tiến hóa liên tục** xuyên suốt cuốn sách. Các khái niệm cốt lõi bao gồm: Concept, Definition, Mechanism, MechanismInput, MechanismOperation, Condition, Claim, Evidence, Observation, Experiment, Experience, Event, TimeInterval, Hypothesis.

Ontology này **không được xác định trước**. Mỗi quyết định mô hình hóa đều phải được nghiên cứu và biện minh. Đặc biệt, chúng ta sẽ khám phá câu hỏi: *làm sao hệ thống suy ra rằng các khái niệm trong các miền khác nhau cùng instantiate một mechanism?*

## Ngôn ngữ và Thuật ngữ

Sách viết bằng **tiếng Việt**. Thuật ngữ kỹ thuật giữ nguyên tiếng Anh ở lần xuất hiện đầu tiên: "thực thể (entity)", "suy diễn (inference)", "nguồn gốc dữ liệu (provenance)". Không dịch thuật ngữ một cách không nhất quán.

## Bắt đầu

Hãy bắt đầu từ Chương 1 — *Từ Đồ thị đến Tri thức*.
