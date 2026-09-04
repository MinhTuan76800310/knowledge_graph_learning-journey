# Glossary — Knowledge Graph Book

Technical terms used in the book, consolidated from each chapter's "Thuật ngữ đã gặp
trong chương này" term table into a single registry. Vietnamese translations appear on
first occurrence in the manuscript; the per-chapter term tables are the authoritative
per-chapter lists, and this document aggregates them by **first appearance**.

Last updated: Chapter 6

## Registry (Chapters 1–6)

| Term (English) | Term (Vietnamese) | Definition | First appearance |
|---|---|---|---|
| Mechanism | Cơ chế | Quá trình biến đổi: nhận đầu vào, sinh đầu ra trong điều kiện (condition) | §1.2 |
| Entity | Thực thể | Đối tượng trong thế giới thực hoặc miền vấn đề | §1.3 |
| Relation | Quan hệ | Mối liên hệ giữa hai entity | §1.3 |
| Triple | Bộ ba | Đơn vị cơ bản: (subject, predicate, object) | §1.3 |
| Data Graph | Đồ thị dữ liệu | Tập hợp entity/relation/property chưa có nghĩa hình thức | §1.3 |
| Taxonomy | Phân loại | Hệ thống phân cấp subclass/superclass | §1.3 |
| Ontology | Bản thể học | Định nghĩa hình thức khái niệm, quan hệ, ràng buộc | §1.3 |
| Knowledge Graph | Đồ thị tri thức | Đồ thị có hướng có nhãn mang ngữ nghĩa | §1.3 |
| Semantics | Ngữ nghĩa | Lớp ý nghĩa của đồ thị: khai báo cho máy biết ký hiệu nghĩa | §1.3 |
| Context | Ngữ cảnh | Lớp thông tin bên ngoài đồ thị để đánh giá: nguồn, thời gian | §1.3 |
| Cardinality | Số lượng | Số giá trị được phép của quan hệ/thuộc tính | §1.4 |
| Partial order | Thứ tự bộ phận | Quan hệ thứ tự bộ phận (phản xạ, bắc cầu, phản đối xứng) | §1.5 |
| Operation | Phép toán | Phép biến đổi cơ sở mà một cơ chế thực hiện (vd: đạo hàm) | §1.3 |
| Quantity | Đại lượng | Giá trị đo được làm đầu vào/đầu ra của cơ chế (vị trí, vận tốc…) | §1.3 |
| Reference variable | Biến tham chiếu | Biến độc lập mà tốc độ được lấy theo (vd: thời gian) | §1.6 |
| DerivativeApplication | Ứng dụng đạo hàm | Đối tượng trung gian ràng buộc cơ chế, đại lượng được đạo hàm, biến tham chiếu | §1.6 |
| Graph | Đồ thị | Cấu trúc toán học G = (V, E) gồm đỉnh và cạnh | §1 |
| Node / Vertex | Đỉnh / Nút | Đơn vị cơ bản của đồ thị đại diện một entity | §1 |
| Edge | Cạnh | Kết nối giữa hai nút trong đồ thị | §1 |
| Schema | Lược đồ | Mô tả cấu trúc và từ vựng được kỳ vọng của đồ thị dữ liệu | §1 |
| Inference | Suy diễn | Suy ra tri thức mới từ dữ kiện và quy tắc hiện có | §1 |
| RDF | RDF | Resource Description Framework — mô hình đồ thị bộ ba chuẩn W3C | §2.1 |
| IRI | IRI | Internationalized Resource Identifier — định danh toàn cục dạng chuỗi | §2.1.2 |
| Literal | Literal | Giá trị dữ liệu (chuỗi, số) ở vị trí đối tượng | §2.1.1 |
| Blank node | Nút trống | Tài nguyên tồn tại nhưng không có IRI | §2.1.3 |
| Turtle | Turtle | Cú pháp văn bản phổ biến để viết RDF | §2.1.5 |
| N-Triples | N-Triples | Định dạng dòng đơn giản, mỗi dòng một bộ ba | §2.1.5 |
| RDF/XML | RDF/XML | Định dạng tuần tự hóa RDF theo cú pháp XML | §2.1.5 |
| JSON-LD | JSON-LD | JSON for Linked Data — định dạng JSON cho dữ liệu liên kết | §2.1.5 |
| SPARQL | SPARQL | SPARQL Protocol and RDF Query Language — ngôn ngữ truy vấn chuẩn cho RDF | §2.1.6 |
| Basic Graph Pattern (BGP) | Mẫu đồ thị cơ bản | Tập hợp các mẫu bộ ba trong truy vấn SPARQL | §2.1.6 |
| Solution mapping | Ánh xạ nghiệm | Phép gán biến với hạng mục đồ thị khớp mẫu | §2.1.6 |
| Labeled Property Graph | Đồ thị Thuộc tính có nhãn | Mô hình đồ thị gồm nút, nhãn, thuộc tính, quan hệ | §2.2 |
| Cypher | Cypher | Ngôn ngữ truy vấn khai báo cho đồ thị thuộc tính | §2.3 |
| GQL | GQL | Graph Query Language — ngôn ngữ truy vấn đồ thị chuẩn ISO | §2.3.4 |
| ISO | ISO | International Organization for Standardization | §2.3.4 |
| W3C | W3C | World Wide Web Consortium — tổ chức phát triển chuẩn web | §2.0 |
| RateOfChangeMechanism | Cơ chế tốc độ thay đổi | Lớp cơ chế tính tốc độ thay đổi của một đại lượng theo một biến | §2.1.5 |
| Namespace | Không gian tên | Ánh xạ tiền tố ngắn thành IRI đầy đủ | §2.1.4 |
| Linked Data | Dữ liệu liên kết | Dữ liệu được định danh bằng IRI để tích hợp | §2.1.2 |
| Triple term / Reifier | Bộ ba-mệnh đề / Reifier | Cơ chế RDF 1.2 tham chiếu mệnh đề (phát triển hiện tại) | §2.1.7 |
| Entailment | Suy diễn logic / Hệ quả logic | Kết luận mới suy ra từ tiên đề; dưới ngữ nghĩa hình thức (RDFS, OWL) | §2.4.1 |
| Serialize / Parse | Tuần tự hóa / Phân tích | Chuyển đồ thị thành văn bản / Đọc văn bản thành đồ thị | §2.1.5 |
| Graph isomorphism | Đẳng cấu đồ thị | Hai đồ thị tương đương nếu có song ánh bảo toàn bộ ba | §2.1.5 |
| RDFS | RDF Schema | Từ vựng mô tả lớp, subclass, domain/range với ngữ nghĩa suy luận | §3.1.3 |
| Schema alignment | Gióng hàng lược đồ | Quy trình tìm và xác nhận tương ứng từ vựng giữa các nguồn | §3.4 |
| Identifier | Định danh | Chuỗi ký tự dùng để gọi tên thực thể trong hệ thống | §3.2.1 |
| Denotation | Sự biểu thị | Quan hệ "định danh này chỉ đến thực thể kia" | §3.2.1 |
| Entity resolution | Giải quyết định danh | Suy luận hai định danh có cùng một thực thể hay không | §3.2.5 |
| Record linkage | Liên kết bản ghi | Tên gọi của bài toán ghép bản ghi trong tích hợp dữ liệu | §3.2.5 |
| Canonical identifier | Định danh chính tắc | Định danh duy nhất được chọn làm "tên thật" của thực thể | §3.2.5 |
| Alias | Bí danh | Những tên khác cùng biểu thị thực thể, nối về định danh chính tắc | §3.2.5 |
| owl:sameAs | owl:sameAs | Khẳng định hai định danh là một, kéo theo lan truyền thông tin | §3.2.4 |
| Unique name assumption | Giả định tên duy nhất | Giả định tên khác nhau thì thực thể khác nhau — OWL không có quy tắc này | §3.2.3 |
| Named graph | Đồ thị có tên | Cơ chế gom nhóm phát biểu trong RDF dataset | §3.3.2 |
| N-ary relation | Quan hệ n-ngôi | Quan hệ nhiều hơn hai tham gia hoặc cần thuộc tính riêng | §3.3.3 |
| Reification | Sự tái hiện hóa | Coi một phát biểu như một đối tượng có thể mang thuộc tính | §3.3.3 |
| Qualifier | Định ngữ ngữ cảnh | Cặp (thuộc tính, giá trị) gắn vào phát biểu để thêm chiều ngữ cảnh | §3.3.6 |
| OWL | OWL | Web Ontology Language — dùng qua owl:sameAs từ Ch3, hình thức hóa ở Ch4 | §3.2.4 |
| Axiom | Tiên đề | Phát biểu ràng buộc ngữ nghĩa | §4.2 |
| Interpretation | Diễn giải | Cách gán nghĩa toán học cho ký hiệu | §4.3 |
| Model | Mô hình | Diễn giải thỏa mãn mọi tiên đề | §4.3 |
| Subclass | Lớp con | C ⊑ D: C^I ⊆ D^I | §4.4 |
| Equivalent Classes | Lớp tương đương | A ≡ B: A^I = B^I | §4.4 |
| Disjoint Classes | Lớp rời nhau | C ⊓ D ≡ ⊥: C^I ∩ D^I = ∅ | §4.4 |
| Class Expression | Biểu thức lớp | Tổ hợp lớp: giao, hợp, phủ định, hạn chế | §4.6 |
| Existential Restriction | Hạn chế tồn tại | ∃R.C: có ít nhất một R-liên kết đến C | §4.6 |
| Universal Restriction | Hạn chế phổ quát | ∀R.C: mọi R-liên kết đều đến C | §4.6 |
| Reflexive / Irreflexive | Phản xạ / Không phản xạ | Mọi phần tử tự liên kết / không phần tử nào tự liên kết | §4.7 |
| Asymmetric | Bất đối xứng | (x,y) ∈ R^I ⇒ (y,x) ∉ R^I | §4.7 |
| Property Chain | Chuỗi thuộc tính | R ∘ S ⊑ T: đi qua hai bước rồi suy ra một bước | §4.7 |
| Class Extension | Phần mở rộng lớp | C^I: tập các phần tử thuộc lớp C trong diễn giải | §4.3 |
| Necessary Condition | Điều kiện cần | A ⊑ B: B cần cho A | §4.5 |
| Sufficient Condition | Điều kiện đủ | A ⊑ B: A đủ cho B | §4.5 |
| Necessary & Sufficient | Cần và đủ | A ≡ B: A và B cần và đủ cho nhau | §4.5 |
| Open World Assumption | Giả định thế giới mở | Thiếu ≠ sai | §4.8 |
| Consistency | Tính nhất quán | Tồn tại ít nhất một mô hình | §4.9 |
| Satisfiability | Tính thỏa được | Lớp có thể có thành viên trong mô hình | §4.9 |
| Description Logic | Logic mô tả | Họ ngôn ngữ logic cân bằng biểu đạt và khả thi suy luận | §4.10 |
| TBox / ABox / RBox | TBox / ABox / RBox | Phân loại tinh thần: tri thức tổng quát / cá thể / thuộc tính | §4.10 |
| OWL 2 EL / QL / RL | Hồ sơ OWL 2 | Profiles đánh đổi biểu đạt lấy hiệu suất | §4.12 |
| Forward Chaining | Suy diễn tiến | Áp dụng quy tắc lặp cho đến fixpoint | §5.2 |
| Substitution θ | Phép thế | Ánh xạ biến sang giá trị cụ thể; ground fact là kết quả | §5.2 |
| Grounding | Sự ground hóa | Làm cho quy tắc trừu tượng thành cụ thể bằng phép thế | §5.2 |
| Fixpoint | Điểm bất động | $G_{n+1} = G_n$: không còn triple mới được sinh ra | §5.2 |
| Closure | Bao đóng | Đồ thị chứa mọi hệ quả đã tính | §5.2 |
| Monotonicity | Đơn điệu | Thêm tri thức không làm mất kết luận cũ | §5.2 |
| RDFS Entailment Rules | Quy tắc suy diễn RDFS | Quy tắc suy diễn thêm thông tin, không kiểm tra | §5.3 |
| Materialization | Vật chất hóa | Chiến lược tính closure trước, lưu kết quả | §5.4 |
| Query-time entailment | Suy diễn tại truy vấn | Chiến lược tính toán lazy khi có truy vấn | §5.4 |
| Backward Chaining | Suy diễn lùi | Bắt đầu từ câu hỏi, tìm chứng minh | §5.5 |
| SHACL Shape | Shape SHACL | Mô tả điều kiện kiểm tra dữ liệu | §5.6 |
| Focus Node / Value Node | Nút trọng tâm / Nút giá trị | Nút đang đánh giá / nút đích qua path | §5.6 |
| Validation Report | Báo cáo xác nhận | Báo cáo kết quả xác nhận (conforms/vi phạm) | §5.7 |
| Conformance | Phù hợp | Dữ liệu khớp shapes ≠ dữ liệu đúng | §5.8 |
| Soundness | Tính đúng đắn | Mọi kết quả suy diễn đều đúng ngữ nghĩa | §5.13 |
| Completeness | Tính đầy đủ | Mọi hệ quả ngữ nghĩa đều được suy diễn | §5.13 |
| Effective Validation Graph | Đồ thị xác nhận hiệu dụng | Đồ thị thực sự được validator nhìn thấy | §5.11 |
| Entailment Regime | Chế độ suy diễn | Xác định mức độ suy diễn khi truy vấn | §5.14 |
| Graph Repair | Sửa chữa đồ thị | Quyết định sửa dữ liệu hay sửa shape dựa trên governance | §5.12 |
| Ground Triple | Bộ ba nền | Triple không còn biến, sẵn sàng trong đồ thị | §5.2 |
| Epistemic model | Mô hình tri thức luận | Chuỗi Observation → Assertion → Claim → Evidence → Accepted Knowledge | §6.1 |
| Proposition / Assertion / Claim | Mệnh đề / Khẳng định / Phát biểu | Nội dung trừu tượng / thể hiện trong ngôn ngữ / bản ghi có metadata | §6.2 |
| Provenance | Xuất xứ | Ai tạo, từ đâu, khi nào — PROV-O Entity/Activity/Agent | §6.4 |
| supports / contradicts / isRelevantTo | Hỗ trợ / Mâu thuẫn / Liên quan | Ba quan hệ bằng chứng giữa evidence và claim | §6.5 |
| Contradiction taxonomy | Phân loại mâu thuẫn | 5 loại: logical, value, temporal, scope, source | §6.6 |
| Bitemporal | Song thời gian | Lưu cả valid time lẫn system time | §6.7 |
| ProperInterval | Khoảng thời gian chuẩn | Lớp OWL-Time: khoảng thời gian có điểm đầu và điểm cuối | §6.7 |
| Qualified statement (n-ary) | Câu có định ngữ (n-ngôi) | Gói quan hệ thành object để gắn metadata (Wikidata pattern) | §6.9 |
| Governance states | Trạng thái quản trị | Candidate, Accepted, Rejected, Contested, Superseded | §6.12 |
| Supersession ≠ Contradiction | Thay thế ≠ Mâu thuẫn | Thay thế = tốt hơn; Mâu thuẫn = ít nhất một bên sai | §6.13 |
| Claim ledger | Sổ cái phát biểu | Nhật ký bất biến chứa mọi claim, kể cả mâu thuẫn | §6.15 |
| CandidateKnowledge | Tri thức ứng viên | Đầu ra LLM — cần bằng chứng độc lập trước khi Accepted | §6.16 |
| Confidence policy | Chính sách độ tin cậy | 0.6·sourceReliability + 0.4·evidenceScore | §6.11 |
| Negation ≠ Absence | Phủ định ≠ Vắng mặt | Claim(¬P) khác "không có claim nào về P" | §6.20 |
| Contradiction ≠ Inconsistency | Mâu thuẫn ≠ Bất nhất | Mâu thuẫn ở nội dung; nhất quán ở metadata | §6.21 |
| Validation | Kiểm chứng | Kiểm tra dữ liệu có thỏa mãn ràng buộc khai báo hay không | §5 |
| SHACL | SHACL | Shapes Constraint Language — chuẩn W3C về xác nhận đồ thị | §5 |
| Immediate consequence operator $T_P$ | Toán tử hệ quả tức thời | $T_P(I)$ = mọi head ground có thân khớp trong $I$; đơn điệu → lfp | §5.2 |
| Least fixed point | Điểm bất động nhỏ nhất | $\mathrm{lfp}(T_P)=\bigcup_{k\ge0}T_P^k(\emptyset)$; kết quả forward chaining (Knaster–Tarski) | §5.2 |
| Datalog | Datalog | Luật Horn an toàn, không hàm; ba ngữ nghĩa tương đương; PTIME data / EXPTIME combined | §5.16 |
| Minimal Herbrand model | Mô hình Herbrand nhỏ nhất | $\mathcal{M}(P)$ = giao mọi Herbrand model ⊇ $D$; trùng $\mathrm{lfp}(T_P)$ | §5.16 |
| Classical negation | Phủ định cổ điển | $\neg$; OWA; đơn điệu; đúng khi sai trong mọi mô hình | §5.16 |
| Negation as Failure (NAF) | Phủ định dạng thất bại | `not`/$\sim$; CWA; phi đơn điệu; cần stratification để có mô hình duy nhất | §5.16 |
| Stratified Datalog | Datalog phân tầng | Vị từ trong `not` phải ở tầng thấp hơn head → perfect model duy nhất | §5.16 |
| Local Closed-World Semantics | Ngữ nghĩa thế giới đóng cục bộ | SHACL đọc vắng mặt cục bộ; thêm triple có thể lật conform→violate (phi đơn điệu) | §5.10 |
| RETE algorithm | Thuật toán RETE | Mạng alpha/beta cache khớp từng phần; WME + agenda/conflict resolution; memory-for-speed | §5.5 |
| Alpha/Beta network | Mạng alpha/beta | Alpha: lọc 1 đầu vào trong một mẫu; Beta: join 2 đầu vào giữa các mẫu + beta memory | §5.5 |