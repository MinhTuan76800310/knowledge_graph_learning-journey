# Thuật ngữ (Glossary)

Các thuật ngữ được sắp theo bảng chữ cái của tên tiếng Anh. Mỗi mục gồm tên tiếng Anh,
tên/giải thích tiếng Việt, và định nghĩa ngắn dùng trong cuốn sách.

**Alias (Bí danh).** Một tên khác cùng biểu thị một thực thể. Khác với định danh chính
tắc, alias không được hệ thống chọn làm tên quy chiếu duy nhất.

**Assertion (Tuyên bố).** Một mệnh đề được khẳng định là đúng trong ngữ cảnh của một đồ thị.
Trong RDF, một triple có mặt trong đồ thị là một assertion. Assertion chưa chắc là tri thức
được chấp nhận (accepted knowledge).

**Axiom (Tiên đề).** Phát biểu ràng buộc ngữ nghĩa hình thức của các ký hiệu trong ontology.
Khác với chú thích (annotation): tiên đề tạo ra suy diễn, chú thích chỉ dành cho con người.

**Blank node (Nút trống).** Một nút trong đồ thị RDF biểu diễn một tài nguyên tồn tại nhưng
không được đặt tên bằng IRI. Nhãn của blank node chỉ có phạm vi cục bộ trong một tài liệu;
ngữ nghĩa trực giác là "tồn tại một tài nguyên nào đó…".

**Canonical identifier (Định danh chính tắc).** Định danh duy nhất được một hệ thống chọn
làm tên quy chiếu của một thực thể; các tên khác được giữ như alias.

**Class Expression (Biểu thức lớp).** Tổ hợp của các lớp và thuộc tính tạo thành mô tả phức
tạp: giao (⊓), hợp (⊔), phủ định (¬), hạn chế tồn tại (∃R.C), hạn chế phổ quát (∀R.C).
Mỗi biểu thức có ngữ nghĩa tập hợp chính xác trong diễn giải.

**Backward Chaining (Suy diễn lùi).** Chiến lược suy diễn goal-driven: bắt đầu từ câu hỏi, tìm
quy tắc có head khớp, tạo subgoal từ body, đệ quy cho đến khi đạt assertion. Ngược hướng với
forward chaining (data-driven). Phù hợp khi ít truy vấn trên đồ thị lớn.

**Completeness (Tính đầy đủ).** Tính chất của thủ tục suy diễn: mọi hệ quả logic thực sự đều
được sinh ra ($E \subseteq A$). Không có âm tính giả. Phải ghi rõ ngôn ngữ/hồ sơ + chế độ suy
diễn + tác vụ suy luận. OWL RL forward chaining không complete cho OWL 2 DL đầy đủ trên đồ
thị RDF tùy ý; complete dưới các điều kiện syntactic cụ thể (Theorem PR1).

**Conformance (Sự phù hợp).** Dữ liệu thỏa mãn các shapes SHACL đã định nghĩa. Phù hợp không
có nghĩa dữ liệu đúng với thực tế; vi phạm không có nghĩa dữ liệu sai.

**Effective Validation Graph (Đồ thị xác nhận hiệu lực).** Đồ thị thực sự được SHACL validator
xem xét. Có thể là asserted graph, expanded graph (sau materialization), hoặc hybrid. Là
quyết định kiến trúc, phải được document rõ trong hệ thống production.

**Entailment Regime (Chế độ suy diễn).** Tập quy tắc ngữ nghĩa áp dụng khi tính toán hệ quả
logic. Cùng đồ thị, regime khác nhau cho kết quả khác nhau (Simple, RDFS, OWL RL, OWL
Direct, OWL RDF-Based). Mọi khẳng định về soundness/completeness phải ghi rõ regime. Trong
SPARQL, regime được chỉ định qua Service Description, không phải FROM clause.

**Fixpoint (Điểm bất động).** Trạng thái $G_{n+1} = G_n$ trong forward chaining: vòng lặp
không sinh triple mới, bao đóng đã ổn định. Là điều kiện dừng của thuật toán.

**Focus Node (Nút trọng tâm).** Trong SHACL: nút dữ liệu đang được đánh giá chống lại một
shape. Được chọn bởi cơ chế target (sh:targetClass, sh:targetNode, etc.).

**Forward Chaining (Suy diễn tiến).** Thuật toán suy diễn lặp dùng phép thế $\theta$:
$G_{i+1} = G_i \cup \{ \theta(\text{head}(r)) \mid r \in R, \; \theta(\text{body}(r)) \subseteq G_i \}$,
dừng khi đạt điểm bất động (fixpoint) $G_{n+1} = G_n$. Đảm bảo dừng khi thỏa mãn các điều
kiện: đồ thị hữu hạn, quy tắc hữu hạn, function-free, safe variables.

**Graph Repair (Sửa chữa đồ thị).** Quá trình biến đổi đồ thị để đạt SHACL conformance. Là
bài toán quyết định (decision problem), không phải vá lỗi cú pháp: nhiều candidate repairs
có thể tồn tại, chỉ domain knowledge/governance mới chọn được repair đúng về mặt tri thức.
Passes validation ≠ becomes true.

**Materialization (Vật chất hóa).** Chiến lược triển khai suy diễn bằng cách tính toán trước
bao đóng và lưu trữ kết quả. Khác với bản thân quan hệ entailment (là khái niệm ngữ nghĩa,
không phải thao tác tính toán). Có thể không khả thi với ontology quá biểu cảm. So sánh với
query-time reasoning (§5.4).

**Monotonicity (Tính đơn điệu).** Tính chất của chế độ suy diễn: nếu $G \subseteq G'$ thì
$\text{Consequences}(G) \subseteq \text{Consequences}(G')$. Thêm thông tin vào đồ thị không
bao giờ làm mất kết luận cũ. Khác với termination, completeness, và consistency.

**Rule (Quy tắc).** Mệnh đề dạng Horn: head ← body₁ ∧ ... ∧ bodyₙ. Trong KG, head và body
là mẫu triple chứa biến. Phép thế $\theta$ gán biến với giá trị cụ thể để kết nối quy tắc
trừu tượng với dữ liệu đồ thị. Quy tắc Horn đơn điệu, đảm bảo dừng trên đồ thị hữu hạn với
các điều kiện an toàn. Không biểu diễn được phủ định hay disjunction trong head.

**SHACL Instance.** Trong SHACL: quan hệ thành viên lớp bao gồm chuỗi `rdfs:subClassOf*`.
Một nút typed CapitalCity là SHACL instance của City nếu CapitalCity rdfs:subClassOf City.
Khác với exact rdf:type triple grep.

**SHACL (Shapes Constraint Language).** Ngôn ngữ chuẩn W3C để xác nhận dữ liệu RDF dựa trên
shapes. Shapes định nghĩa ràng buộc kiểm tra, không phải tiên đề suy diễn. Kết quả là
validation report (conforms/violation), không phải tri thức mới. SHACL không phải "OWL với
Closed World Assumption."

**Shape.** Điều kiện kiểm tra trong SHACL nhắm đến tập nút dữ liệu. Shape không tham gia
vào RDFS/OWL entailment. Khác với ontology axiom: shape kiểm tra thông tin, axiom thêm
thông tin.

**Soundness (Tính đúng đắn).** Tính chất của thủ tục suy diễn: mọi kết quả sinh ra đều là hệ
quả logic thực sự. Không có dương tính giả. Phải ghi rõ ngôn ngữ/hồ sơ + chế độ suy diễn +
tác vụ suy luận.

**Substitution (Phép thế).** Ánh xạ $\theta$ gán mỗi biến trong quy tắc với một giá trị cụ thể
(IRI, literal, blank node). Cầu nối giữa quy tắc trừu tượng và dữ liệu đồ thị: $\theta(\text{body})$
là phần thân đã ground, $\theta(\text{head})$ là kết luận đã ground.

**SWRL (Semantic Web Rule Language).** Mở rộng OWL bằng quy tắc Horn-clause. W3C Member
Submission (2004), KHÔNG phải Recommendation. Kết hợp OWL DL + SWRL nói chung không quyết
định được (undecidable).

**Validation Report (Báo cáo xác nhận).** Kết quả SHACL validation: sh:conforms (true/false)
và danh sách sh:ValidationResult. Mỗi result gồm focusNode, resultPath, sourceShape,
sourceConstraintComponent, severity, message, và value (khi applicable). Vi phạm chỉ ra sự
không phù hợp, không chỉ ra cách sửa.

**Value Node (Nút giá trị).** Trong SHACL: nút reachable từ focus node qua property path.
Với node shape, value nodes = {focus node}. Với property shape, value nodes là các đích của
path từ focus node. Constraint được đánh giá trên tập value nodes.

**Consistency (Tính nhất quán).** Ontology nhất quán khi tồn tại ít nhất một mô hình. Khác với
satisfiability (một lớp có thể có thành viên) và entailment (một phát biểu đúng trong mọi mô
hình).

**Context (Ngữ cảnh).** Lớp thông tin về nguồn gốc, thời gian, phạm vi và độ tin cậy của một
tuyên bố. Trong mô hình kỹ thuật của sách: KG = Data Graph + Semantics + Context.

**Cypher.** Ngôn ngữ truy vấn khai báo do Neo4j phát triển cho đồ thị thuộc tính, dùng mẫu
ASCII-art (`MATCH ... RETURN`). Cypher tương thích phần lớn với GQL nhưng không trùng khớp.

**Data Graph (Đồ thị dữ liệu).** Tập hợp thực thể, quan hệ và thuộc tính mà chưa có định
nghĩa hình thức về ý nghĩa. Trả lời được "có gì" nhưng chưa trả lời được "nghĩa là gì".

**Denotation (Sự biểu thị).** Quan hệ giữa một định danh và thực thể mà nó chỉ đến. Định
danh không phải là thực thể; sự biểu thị do quy ước và con người gán, không tự động có sẵn.

**Entailment (Suy diễn logic).** O ⊨ α nghĩa là α đúng trong mọi mô hình của ontology O. Suy
diễn là quan hệ ngữ nghĩa mô tả hệ quả logic; bản thân nó không thay đổi hay thêm triple vào
đồ thị. Hệ thống có thể tính toán, vật chất hóa, hoặc lưu cache các hệ quả — nhưng đó là hành
vi triển khai, không phải bản thân quan hệ suy diễn (§5.4). Khác với validation (§5.5):
validation kiểm tra dữ liệu, entailment mô tả hệ quả logic. Luôn ghi rõ entailment regime (§5.9).

**Entity (Thực thể).** Một đối tượng trong thế giới thực hoặc miền vấn đề, được biểu diễn bằng
một nút trong đồ thị.

**Existential Restriction (Hạn chế tồn tại).** ∃R.C — lớp các cá thể có ít nhất một R-liên kết
đến phần tử thuộc C. Yêu cầu sự tồn tại trong mô hình, không nhất thiết trong dữ liệu RDF.

**GQL.** Ngôn ngữ truy vấn đồ thị chuẩn do ISO ban hành (ISO/IEC 39075:2024).

**Graph pattern matching (Khớp mẫu đồ thị).** Cơ chế truy vấn của SPARQL và Cypher: mô tả một
mẫu đồ thị cần tìm và trả về các phần của đồ thị khớp với mẫu đó.

**Identifier (Định danh).** Chuỗi ký tự dùng để gọi tên một thực thể trong hệ thống (IRI,
Q-id, khóa ứng dụng). Định danh khác thực thể mà nó biểu thị; cùng định danh không chứng
minh thống nhất ngữ nghĩa, khác định danh không chứng minh khác thực thể.

**Identity resolution (Giải quyết định danh).** Quá trình xác định hai định danh trong hai
nguồn có biểu thị cùng một thực thể hay không, đi từ ứng viên đồng nhất qua bằng chứng và
xem xét đến khẳng định được chấp nhận. Đồng nghĩa thực hành với record linkage.

**Interpretation (Diễn giải).** Cách gán nghĩa toán học cho ký hiệu: I = (Δ^I, ·^I), trong đó
Δ^I là miền diễn giải và ·^I ánh xạ lớp → tập hợp, thuộc tính → quan hệ, cá thể → phần tử.

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

**Model (Mô hình).** Diễn giải thỏa mãn tất cả các tiên đề trong ontology. Tập hợp các mô hình
xác định ngữ nghĩa của ontology: suy diễn = đúng trong mọi mô hình.

**Named graph (Đồ thị có tên).** Một cặp (tên đồ thị, đồ thị RDF) trong RDF dataset. Tên đồ
thị chỉ được ghép cặp cú pháp với đồ thị; ý nghĩa provenance/nguồn là quy ước ứng dụng,
không phải ngữ nghĩa hình thức có sẵn.

**N-ary relation (Quan hệ n-ary).** Quan hệ có nhiều hơn hai người tham gia, hoặc quan hệ
cần mang thêm thuộc tính (thời gian, độ tin cậy). Trong RDF được biểu diễn gián tiếp, phổ
biến nhất bằng một thực thể trung gian đại diện cho sự kiện quan hệ.

**Ontology (Bản thể học).** Tập tiên đề ràng buộc ngữ nghĩa hình thức của các ký hiệu trong một
miền tri thức. Khác với schema: ontology nhấn mạnh cam kết ngữ nghĩa và hệ quả logic, không
chỉ cấu trúc kỳ vọng.

**Open World Assumption — OWA (Giả định thế giới mở).** Trong OWL, thiếu thông tin không có
nghĩa là sai; nó chỉ có nghĩa là chưa biết. Khác với cơ sở dữ liệu truyền thống dùng giả định
thế giới đóng (thiếu = sai/vắng).

**owl:sameAs.** Vị từ OWL khẳng định hai định danh biểu thị **cùng một cá thể**. Không phải
"tương tự" hay "gần giống": mọi thông tin của tên này suy ra được cho tên kia.

**Property Graph.** Xem Labeled Property Graph.

**Qualifier (Định ngữ).** Trong Wikidata: cặp thuộc tính–giá trị gắn vào một statement để mở
rộng ngữ cảnh (thời điểm, phạm vi, phương pháp) mà không thay thế nội dung cốt lõi.

**RDF (Resource Description Framework).** Mô hình dữ liệu chuẩn của W3C biểu diễn tri thức
dưới dạng các bộ ba (subject, predicate, object).

**Record linkage (Liên kết bản ghi).** Bài toán suy luận xem hai bản ghi từ các nguồn khác
nhau có phải cùng một thực thể thế giới thực hay không. Là suy luận không chắc chắn, cần
bằng chứng và xác nhận; các thuật toán công nghiệp (blocking, matching) thuộc Chương 7.

**Relation (Quan hệ).** Mối liên hệ giữa hai thực thể, biểu diễn bằng cạnh có nhãn.

**Reification (Tái hiện).** Kỹ thuật biến một bộ ba/quan hệ thành một tài nguyên để có thể gắn
thêm thông tin cho nó.

**Schema (Lược đồ).** Phần mô tả cấu trúc và từ vựng được kỳ vọng của đồ thị dữ liệu: lớp,
quan hệ, kiểu thuộc tính, ràng buộc. Lược đồ không phải ontology: nó cho bộ khung từ vựng
chứ chưa cho ngữ nghĩa suy luận đầy đủ.

**Semantics (Ngữ nghĩa).** Lớp ý nghĩa của đồ thị: schema, ontology, identity, constraints.

**Solution mapping (Ánh xạ nghiệm).** Trong SPARQL: một phép gán biến với các hạng mục của đồ
thị sao cho mẫu truy vấn khớp. Kết quả truy vấn là tập các ánh xạ nghiệm.

**SPARQL.** Ngôn ngữ truy vấn chuẩn của W3C cho RDF, hoạt động bằng khớp mẫu đồ thị.

**Subject / Predicate / Object (Chủ thể / Vị từ / Đối tượng).** Ba vị trí của một bộ ba RDF.
Chủ thể là IRI hoặc blank node; vị từ chỉ là IRI; đối tượng là IRI, literal hoặc blank node.

**Taxonomy (Phân loại).** Hệ thống phân cấp các khái niệm dựa trên quan hệ cha-con
(subclass/superclass). Ontology thường chứa cấu trúc phân cấp subclass và có thể mở rộng bằng
các tiên đề ngữ nghĩa bổ sung. Taxonomy có thể tồn tại độc lập như sản phẩm phân loại.

**Triple (Bộ ba).** Đơn vị cơ bản của biểu diễn tri thức dạng đồ thị: (subject, predicate,
object).

**Turtle.** Một cú pháp văn bản phổ biến để viết RDF. Turtle là cú pháp, không phải bản thân
mô hình RDF.

**Unique name assumption (Giả định tên duy nhất).** Giả định rằng các tên khác nhau luôn chỉ
các thực thể khác nhau. OWL không có giả định này: khác tên không ngụ ý khác thực thể; muốn
khẳng định khác nhau phải dùng owl:differentFrom.

**Validation (Xác nhận).** Kiểm tra dữ liệu có tuân thủ các ràng buộc đã định hay không.
SHACL là ngôn ngữ chuẩn cho RDF validation (§5.6). Khác với entailment: validation kiểm
tra thông tin hiện có, entailment suy ra tri thức mới. Conformance ≠ truth; violation ≠ repair.
Consistency ≠ validation — hai trục độc lập (§5.9).

**Satisfiability (Tính thỏa được).** Lớp C thỏa được đối với ontology O khi tồn tại ít nhất một
mô hình của O trong đó C^I ≠ ∅. Khác với consistency (toàn bộ ontology có mô hình) và
entailment (phát biểu đúng trong mọi mô hình).

**Universal Restriction (Hạn chế phổ quát).** ∀R.C — lớp các cá thể mà mọi R-liên kết đều dẫn
đến phần tử thuộc C. Không khẳng định sự tồn tại của R-liên kết; nếu không có liên kết nào
thì điều kiện được thỏa mãn một cách trống rỗng (vacuously true).
