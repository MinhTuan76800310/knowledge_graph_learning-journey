# Thuật ngữ (Glossary)

Các thuật ngữ được sắp theo bảng chữ cái của tên tiếng Anh. Mỗi mục gồm tên tiếng Anh,
tên/giải thích tiếng Việt, và định nghĩa ngắn dùng trong cuốn sách.

**Assertion (Tuyên bố).** Một mệnh đề được khẳng định là đúng trong ngữ cảnh của một đồ thị.
Trong RDF, một triple có mặt trong đồ thị là một assertion. Assertion chưa chắc là tri thức
được chấp nhận (accepted knowledge).

**Blank node (Nút trống).** Một nút trong đồ thị RDF biểu diễn một tài nguyên tồn tại nhưng
không được đặt tên bằng IRI. Nhãn của blank node chỉ có phạm vi cục bộ trong một tài liệu;
ngữ nghĩa trực giác là "tồn tại một tài nguyên nào đó…".

**Context (Ngữ cảnh).** Lớp thông tin về nguồn gốc, thời gian, phạm vi và độ tin cậy của một
tuyên bố. Trong mô hình kỹ thuật của sách: KG = Data Graph + Semantics + Context.

**Cypher.** Ngôn ngữ truy vấn khai báo do Neo4j phát triển cho đồ thị thuộc tính, dùng mẫu
ASCII-art (`MATCH ... RETURN`). Cypher tương thích phần lớn với GQL nhưng không trùng khớp.

**Data Graph (Đồ thị dữ liệu).** Tập hợp thực thể, quan hệ và thuộc tính mà chưa có định
nghĩa hình thức về ý nghĩa. Trả lời được "có gì" nhưng chưa trả lời được "nghĩa là gì".

**Entailment (Suy diễn logic).** Một mệnh đề được suy ra từ các mệnh đề khác theo quy tắc ngữ
nghĩa (ví dụ RDFS/OWL). Khác với validation: entailment thêm tri thức, không từ chối dữ liệu.

**Entity (Thực thể).** Một đối tượng trong thế giới thực hoặc miền vấn đề, được biểu diễn bằng
một nút trong đồ thị.

**GQL.** Ngôn ngữ truy vấn đồ thị chuẩn do ISO ban hành (ISO/IEC 39075:2024).

**Graph pattern matching (Khớp mẫu đồ thị).** Cơ chế truy vấn của SPARQL và Cypher: mô tả một
mẫu đồ thị cần tìm và trả về các phần của đồ thị khớp với mẫu đó.

**IRI (Internationalized Resource Identifier).** Cơ chế định danh có phạm vi toàn cục trong
RDF. Cùng một IRI không tự động chứng minh hai bên cùng ngữ nghĩa; hai IRI khác nhau chưa
chắc là hai thực thể khác nhau.

**Knowledge Graph (Đồ thị Tri thức).** Theo nghĩa tối thiểu: đồ thị có hướng có nhãn, trong đó
nhãn mang ngữ nghĩa được định nghĩa. Theo mô hình kỹ thuật của sách: Data Graph + Semantics
+ Context.

**Labeled Property Graph (Đồ thị Thuộc tính có nhãn).** Mô hình đồ thị gồm nút (có nhãn và
thuộc tính) và quan hệ (có hướng, có kiểu, và có thể có thuộc tính). Neo4j là một triển khai.

**Literal.** Giá trị dữ liệu trong RDF (chuỗi, số, …), chỉ xuất hiện ở vị trí đối tượng của
bộ ba.

**Ontology (Bản thể học).** Định nghĩa hình thức các khái niệm, quan hệ, ràng buộc và tiên đề
trong một miền tri thức.

**Property Graph.** Xem Labeled Property Graph.

**RDF (Resource Description Framework).** Mô hình dữ liệu chuẩn của W3C biểu diễn tri thức
dưới dạng các bộ ba (subject, predicate, object).

**Relation (Quan hệ).** Mối liên hệ giữa hai thực thể, biểu diễn bằng cạnh có nhãn.

**Reification (Tái hiện).** Kỹ thuật biến một bộ ba/quan hệ thành một tài nguyên để có thể gắn
thêm thông tin cho nó.

**Semantics (Ngữ nghĩa).** Lớp ý nghĩa của đồ thị: schema, ontology, identity, constraints.

**Solution mapping (Ánh xạ nghiệm).** Trong SPARQL: một phép gán biến với các hạng mục của đồ
thị sao cho mẫu truy vấn khớp. Kết quả truy vấn là tập các ánh xạ nghiệm.

**SPARQL.** Ngôn ngữ truy vấn chuẩn của W3C cho RDF, hoạt động bằng khớp mẫu đồ thị.

**Subject / Predicate / Object (Chủ thể / Vị từ / Đối tượng).** Ba vị trí của một bộ ba RDF.
Chủ thể là IRI hoặc blank node; vị từ chỉ là IRI; đối tượng là IRI, literal hoặc blank node.

**Taxonomy (Phân loại).** Hệ thống phân cấp các khái niệm dựa trên quan hệ cha-con
(subclass/superclass).

**Triple (Bộ ba).** Đơn vị cơ bản của biểu diễn tri thức dạng đồ thị: (subject, predicate,
object).

**Turtle.** Một cú pháp văn bản phổ biến để viết RDF. Turtle là cú pháp, không phải bản thân
mô hình RDF.

**Validation (Xác nhận).** Kiểm tra dữ liệu có tuân thủ các ràng buộc đã định hay không (ví dụ
SHACL). Khác với entailment: validation có thể từ chối dữ liệu.
