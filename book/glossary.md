# Thuật ngữ (Glossary)

Các thuật ngữ được sắp theo bảng chữ cái của tên tiếng Anh. Mỗi mục gồm tên tiếng Anh,
tên/giải thích tiếng Việt, và định nghĩa ngắn dùng trong cuốn sách.


**Abduction (Giả định — lựa chọn giải thích tốt nhất).** Suy luận chọn giả thuyết giải thích tốt nhất cho một quan sát. Khác với quy nạp (tổng quát hóa từ nhiều ví dụ) và suy diễn (hệ quả tất yếu). Chương 8 dạy để tránh nhầm lẫn với quy nạp.

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

**Calibration (Hiệu chuẩn).** Mức độ khớp giữa xác suất dự đoán và tần suất đúng thực tế. Mạng nơ-ron hiện đại thường tự tin quá mức (overconfident); temperature scaling cải thiện calibration.

**CandidateAxiom (Tiên đề ứng viên).** Tiên đề do mô hình học quy nạp đề xuất, chưa được đưa vào ontology. Phải qua đánh giá blast radius, kiểm tra nhất quán, và quản trị trước khi chấp nhận.

**CandidateMechanismHypothesis (Giả thuyết cơ chế ứng viên).** Giả thuyết cho rằng nhiều ứng dụng có thể cùng một cơ chế trừu tượng. Mang bằng chứng cấu trúc, hỗ trợ nguồn, bất định, giả thuyết cạnh tranh, và provenance. Là tri thức ứng viên, chưa được chấp nhận.

**Canonical identifier (Định danh chính tắc).** Định danh duy nhất được một hệ thống chọn
làm tên quy chiếu của một thực thể; các tên khác được giữ như alias.

**Class Expression (Biểu thức lớp).** Tổ hợp của các lớp và thuộc tính tạo thành mô tả phức
tạp: giao (⊓), hợp (⊔), phủ định (¬), hạn chế tồn tại (∃R.C), hạn chế phổ quát (∀R.C).
Mỗi biểu thức có ngữ nghĩa tập hợp chính xác trong diễn giải.

**Backward Chaining (Suy diễn lùi).** Chiến lược suy diễn goal-driven: bắt đầu từ câu hỏi, tìm
quy tắc có head khớp, tạo subgoal từ body, đệ quy cho đến khi đạt assertion. Ngược hướng với
forward chaining (data-driven). Phù hợp khi ít truy vấn trên đồ thị lớn.

**Classification (Phân lớp).** Bài toán gán nhãn ứng viên cho một thực thể/ứng dụng dựa trên mô hình học. Đầu ra là xác suất ứng viên, không phải khẳng định kiểu; phải qua quản trị trước khi ghi vào đồ thị.

**Clustering (Phân cụm).** Gom nhóm khám phá dựa trên biểu diễn/đặc trưng, không có nhãn. Cụm không phải lớp ontology. Phân cụm chỉ gợi ý giả thuyết cơ chế, không phải khẳng định.

**Completeness (Tính đầy đủ).** Tính chất của thủ tục suy diễn: mọi hệ quả logic thực sự đều
được sinh ra ($E \subseteq A$). Không có âm tính giả. Phải ghi rõ ngôn ngữ/hồ sơ + chế độ suy
diễn + tác vụ suy luận. OWL RL forward chaining không complete cho OWL 2 DL đầy đủ trên đồ
thị RDF tùy ý; complete dưới các điều kiện syntactic cụ thể (Theorem PR1).

**ComplEx (Nhúng phức).** Mô hình KGE dùng số phức và tích Hermitian: f(h,r,t) = Re(⟨h, r, t̄⟩). Cho phép mô hình hóa cả quan hệ đối xứng và bất đối xứng.

**Conformance (Sự phù hợp).** Dữ liệu thỏa mãn các shapes SHACL đã định nghĩa. Phù hợp không
có nghĩa dữ liệu đúng với thực tế; vi phạm không có nghĩa dữ liệu sai.

**Cosine similarity (Độ tương tự cosine).** cos(a,b) = (a·b)/(‖a‖·‖b‖), giá trị trong [−1,1]. Đo góc giữa hai vector. Cosine cao là bằng chứng gợi ý, không phải đồng nhất ngữ nghĩa.

**Cross-domain generalization (Tổng quát hóa chéo miền).** Khả năng mô hình nhận ra cơ chế trong một miền mới dù từ vựng bề mặt khác hẳn. Được kiểm tra bằng thử nghiệm: huấn luyện trên miền A, kiểm tra trên miền B.

**Data leakage (Rò rỉ dữ liệu).** Thông tin từ tập kiểm lọt vào quá trình huấn luyện, làm điểm đánh giá lạc quan giả tạo. Các kiểu: trùng lặp, quan hệ nghịch đảo, đường đi, thực thể, thời gian, nguồn.

**Deduction (Suy diễn).** Quy tắc chung + tiền đề → hệ quả tất yếu. Bảo toàn chân lý. Không sinh tri thức mới mà chỉ làm tường minh những gì đã ngầm chứa. Khác quy nạp (giả thuyết có thể sai).

**DistMult (Mô hình song tuyến tính).** Mô hình KGE với hàm chấm điểm f(h,r,t) = ⟨h, r, t⟩ (nhân từng phần tử). Đối xứng: không thể phân biệt (h,r,t) và (t,r,h).

**Effective Validation Graph (Đồ thị xác nhận hiệu lực).** Đồ thị thực sự được SHACL validator
xem xét. Có thể là asserted graph, expanded graph (sau materialization), hoặc hybrid. Là
quyết định kiến trúc, phải được document rõ trong hệ thống production.

**Entailment Regime (Chế độ suy diễn).** Tập quy tắc ngữ nghĩa áp dụng khi tính toán hệ quả
logic. Cùng đồ thị, regime khác nhau cho kết quả khác nhau (Simple, RDFS, OWL RL, OWL
Direct, OWL RDF-Based). Mọi khẳng định về soundness/completeness phải ghi rõ regime. Trong
SPARQL, regime được chỉ định qua Service Description, không phải FROM clause.

**False negative (Âm tính giả).** Bộ ba thực sự đúng nhưng bị dùng làm mẫu âm trong huấn luyện vì đồ thị chưa đầy đủ (OWA). Làm méo ranh giới học được.

**Filtered evaluation (Đánh giá đã lọc).** Trước khi xếp hạng, loại bỏ các bộ ba đúng đã biết khỏi danh sách ứng viên. Cải tiến kỹ thuật, không phải đo lường chân lý tuyệt đối.

**Fixpoint (Điểm bất động).** Trạng thái $G_{n+1} = G_n$ trong forward chaining: vòng lặp
không sinh triple mới, bao đóng đã ổn định. Là điều kiện dừng của thuật toán.

**Focus Node (Nút trọng tâm).** Trong SHACL: nút dữ liệu đang được đánh giá chống lại một
shape. Được chọn bởi cơ chế target (sh:targetClass, sh:targetNode, etc.).

**Forward Chaining (Suy diễn tiến).** Thuật toán suy diễn lặp dùng phép thế $\theta$:
$G_{i+1} = G_i \cup \{ \theta(\text{head}(r)) \mid r \in R, \; \theta(\text{body}(r)) \subseteq G_i \}$,
dừng khi đạt điểm bất động (fixpoint) $G_{n+1} = G_n$. Đảm bảo dừng khi thỏa mãn các điều
kiện: đồ thị hữu hạn, quy tắc hữu hạn, function-free, safe variables.

**GNN (Graph Neural Network / Mạng nơ-ron đồ thị).** Họ mô hình tính theo cấu trúc đồ thị: biểu diễn nút được tính từ lân cận qua truyền thông điệp. Một khung khái niệm, không phải một thuật toán duy nhất.

**Graph Repair (Sửa chữa đồ thị).** Quá trình biến đổi đồ thị để đạt SHACL conformance. Là
bài toán quyết định (decision problem), không phải vá lỗi cú pháp: nhiều candidate repairs
có thể tồn tại, chỉ domain knowledge/governance mới chọn được repair đúng về mặt tri thức.
Passes validation ≠ becomes true.

**Hard negative (Âm tính khó).** Mẫu âm nằm gần ranh giới lớp, buộc mô hình học biên phân biệt có ý nghĩa (ví dụ: FiniteDifference gần RateOfChange). Khác với âm tính dễ ở xa ranh giới.

**Hits@K.** Tỉ lệ các câu trả lời đúng nằm trong top K ứng viên. Không phân biệt giữa hạng 1 và hạng K.

**Induction / Quy nạp (induction).** Tổng quát hóa mẫu từ các quan sát, sinh ra giả thuyết có thể sai. Không phải suy diễn (bảo toàn chân lý). Tri thức quy nạp bao gồm cả mô hình mã hóa mẫu lẫn dự đoán của mô hình.

**Inductive bias (Thiên kiến quy nạp).** Tập giả định cấu trúc của một họ mô hình về mẫu nào đáng học. Ví dụ: TransE (h+r≈t), DistMult (đối xứng), ComplEx (Hermitian).

**Inductive KG learning (Học quy nạp trên đồ thị).** Mô hình tổng quát hóa tới các thực thể/subgraph chưa từng thấy trong huấn luyện. Khác học chuyển dẫn (chỉ dự đoán giữa thực thể đã biết).

**Invariant structure (Cấu trúc bất biến).** Phần cấu trúc được giữ lại khi trừu tượng hóa một cơ chế từ nhiều ứng dụng. Phần chi tiết miền bị bỏ đi gọi là cấu trúc ngẫu nhiên (incidental).

**Knowledge Graph Embedding (KGE / Nhúng đồ thị tri thức).** Học vector thực thể và quan hệ + hàm chấm điểm f(h,r,t). Điểm cao = hợp lý hơn, không phải đúng. Gồm các mô hình: TransE, DistMult, ComplEx.

**Link prediction (Dự đoán liên kết).** Với đồ thị quan sát được một phần, xếp hạng các bộ ba ứng viên còn thiếu. Đầu ra là danh sách có thứ tự, không phải sự thật được khẳng định.

**Materialization (Vật chất hóa).** Chiến lược triển khai suy diễn bằng cách tính toán trước
bao đóng và lưu trữ kết quả. Khác với bản thân quan hệ entailment (là khái niệm ngữ nghĩa,
không phải thao tác tính toán). Có thể không khả thi với ontology quá biểu cảm. So sánh với
query-time reasoning (§5.4).

**Message passing (Truyền thông điệp).** Cơ chế tính toán của GNN: message → aggregate → update. Mỗi nút gửi thông điệp đến lân cận, tập hợp chúng, và cập nhật biểu diễn. Là một khung, không phải một thuật toán.

**Model Assessment (Đánh giá mô hình).** Đối tượng bọc điểm số với ngữ nghĩa: target, model, task, score, score semantics, assessed-at, training dataset, evaluation context. Ngăn chặn 'con số vô danh'.

**Model collapse (Sụp đổ mô hình).** Hiện tượng mô hình huấn luyện trên dữ liệu do chính mô hình sinh ra làm mất dần đa dạng tri thức, tích lũy khiếm khuyết không thể đảo ngược.

**Monotonicity (Tính đơn điệu).** Tính chất của chế độ suy diễn: nếu $G \subseteq G'$ thì
$\text{Consequences}(G) \subseteq \text{Consequences}(G')$. Thêm thông tin vào đồ thị không
bao giờ làm mất kết luận cũ. Khác với termination, completeness, và consistency.

**MRR (Mean Reciprocal Rank).** Trung bình của 1/hạng của câu trả lời đúng. MRR = 1.0 nếu luôn đứng hạng 1. Bị ảnh hưởng nhiều bởi các hạng cao.

**Negative sampling (Lấy mẫu âm).** Thủ thuật huấn luyện: tạo bộ ba nhiễu bằng cách thay thế đầu/cuối của bộ ba đúng. Là giả định kỹ thuật, không phải khẳng định bộ ba đó sai. Thiếu ≠ sai (OWA).

**OOV entity (Out-of-vocabulary entity / Thực thể ngoài từ vựng).** Thực thể không có vector học sẵn vì chưa xuất hiện trong huấn luyện. Cần biểu diễn từ lân cận/thuộc tính hoặc mô hình quy nạp (GNN).

**Oversmoothing (Làm mịn quá mức).** Khi xếp nhiều lớp GNN, biểu diễn các nút hội tụ về nhau, mất thông tin phân biệt. Số lớp tối ưu thường nhỏ (1–3).

**Path-based explanation (Giải thích theo đường đi).** Giải thích dự đoán bằng cách chỉ ra đường đi trong đồ thị dẫn tới kết luận. Tự nhiên với học quy tắc, khó với KGE/GNN.

**Prediction (Dự đoán).** Đầu ra của mô hình học: gán điểm số cho một cấu trúc khả dĩ. Không phải suy dẫn (entailment). Điểm cao ≠ chân lý.

**R-GCN (Relational Graph Convolutional Network).** GNN cho đồ thị đa quan hệ: mỗi loại quan hệ có ma trận biến đổi riêng. Thường dùng encoder (R-GCN) + decoder (DistMult) cho link prediction.

**Representation learning (Học biểu diễn).** Học vector từ dữ liệu thay vì thiết kế đặc trưng thủ công. Vector học được không phải thực thể và không mang ngữ nghĩa hình thức.

**Rule (Quy tắc).** Mệnh đề dạng Horn: head ← body₁ ∧ ... ∧ bodyₙ. Trong KG, head và body
là mẫu triple chứa biến. Phép thế $\theta$ gán biến với giá trị cụ thể để kết nối quy tắc
trừu tượng với dữ liệu đồ thị. Quy tắc Horn đơn điệu, đảm bảo dừng trên đồ thị hữu hạn với
các điều kiện an toàn. Không biểu diễn được phủ định hay disjunction trong head.

**Rule induction (Học quy tắc).** Học quy tắc tượng trưng từ đồ thị. AMIE+ sinh quy tắc đường đi r1(x,y) ∧ r2(y,z) → r3(x,z) dưới giả định PCA. Quy tắc học được là giả thuyết, không phải định luật logic.

**Rule-mining confidence (Độ tin cậy khai phá quy tắc).** Tần suất quy tắc dưới giả định PCA (Partial Completeness Assumption). Khác với độ tin cậy tri thức luận (epistemic confidence) của Chương 6 — hai khái niệm khác nhau, cùng tên 'confidence'.

**Scoring function (Hàm chấm điểm).** Hàm số f(h,r,t) gán giá trị thực cho mỗi bộ ba, đo mức độ hợp lý. Mỗi họ mô hình KGE có một hàm chấm điểm khác nhau.

**Self-reinforcing feedback (Vòng phản hồi tự củng cố).** Khi dự đoán của mô hình quay lại làm dữ liệu huấn luyện, vòng phản hồi hình thành. Phân biệt tri thức do nguồn sinh ra và do mô hình sinh ra (model-generated candidate).

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

**Source leakage (Rò rỉ nguồn).** Cùng một nguồn (ví dụ sách) xuất hiện ở cả train và test, làm quá lạc quan về khả năng tổng quát hóa. Biện pháp: chia tách theo nguồn.

**Spurious correlation (Tương quan giả).** Quan hệ học được giữa dấu hiệu bề mặt và nhãn, xuất hiện trong dữ liệu huấn luyện nhưng không phải cấu trúc cơ chế. Dẫn đến học lối tắt (shortcut learning).

**Structural similarity (Tương tự cấu trúc).** Đánh giá đa chiều hai cấu trúc chia sẻ mẫu vai trò, thao tác, kiểu đối số. Tương tự ≠ đồng nhất, ≠ owl:sameAs.

**Substitution (Phép thế).** Ánh xạ $\theta$ gán mỗi biến trong quy tắc với một giá trị cụ thể
(IRI, literal, blank node). Cầu nối giữa quy tắc trừu tượng và dữ liệu đồ thị: $\theta(\text{body})$
là phần thân đã ground, $\theta(\text{head})$ là kết luận đã ground.

**SWRL (Semantic Web Rule Language).** Mở rộng OWL bằng quy tắc Horn-clause. W3C Member
Submission (2004), KHÔNG phải Recommendation. Kết hợp OWL DL + SWRL nói chung không quyết
định được (undecidable).

**Temporal leakage (Rò rỉ thời gian).** Dữ liệu tương lai ở train, dữ liệu quá khứ ở test — mô hình 'dự đoán' quá khứ dựa trên tương lai. Biện pháp: chia tách theo thời gian.

**Train/validation/test split (Chia tách dữ liệu huấn luyện/xác nhận/kiểm tra).** Phân hoạch tập dữ liệu thành ba phần: train (học tham số), validation (chọn siêu tham số), test (đánh giá cuối). Trên đồ thị, cần tránh rò rỉ.

**Training provenance (Provenance huấn luyện).** Hoạt động huấn luyện sinh ra dự đoán, ghi: phiên bản dữ liệu, phiên bản mô hình, lược đồ đặc trưng, cấu hình. Provenance ≠ bằng chứng.

**Transductive learning (Học chuyển dẫn).** Mô hình học vector cho thực thể đã biết, chỉ dự đoán giữa chúng. Không tổng quát tới thực thể mới. KGE chuẩn là chuyển dẫn.

**TransE.** Mô hình KGE: h + r ≈ t, mỗi quan hệ là phép tịnh tiến. Hàm chấm điểm f(h,r,t) = −‖h + r − t‖. Yếu với quan hệ 1–N, N–1, đối xứng.

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


**Abstention (Kiêng trả lời).** Khi bằng chứng không đủ — không có claim liên quan, thực thể mơ hồ chưa phân giải, mâu thuẫn chưa phân xử, hỗ trợ yếu, ngoài phạm vi, truy xuất không chắc — hệ thống nói rõ 'không đủ bằng chứng' thay vì bịa. Kiêng trả lời không có nghĩa sự kiện là sai (Chương 9).

**Agentic retrieval (Truy xuất có tác nhân).** Truy xuất lặp: sau mỗi lượt, kiểm tra khoảng trống và phát hành lượt truy vấn tiếp theo. Cần điều kiện dừng tường minh; rủi ro trôi câu hỏi, leo thang nhiễu/chi phí, thiên kiến xác nhận. Không tự động tốt hơn truy xuất tĩnh (Chương 9).

**Answer claim (Claim con của câu trả lời).** Câu trả lời phân rã thành các claim con, mỗi claim vết được về bằng chứng/đường cấu trúc/claim được chấp nhận. Cho phép trích dẫn và đối chiếu theo từng câu (Chương 9).

**Answer generation (Sinh câu trả lời).** Tầng ánh xạ (câu hỏi, Gói bằng chứng) thành bản nháp câu trả lời với bốn kỷ luật: không thêm quan hệ ngoài gói, tách bạch phát ngôn, trình bày mâu thuẫn, tự kiểm tra. Văn bản trôi chảy không có nghĩa đúng (Chương 9).

**Answer provenance (Hồ sơ câu trả lời).** Bản ghi BOOK-DEFINED của một câu trả lời: generatedFor → Câu hỏi, usedEvidence → Evidence Packet, generatedBy, generatedAt, modelVersion, citations, answerStatus. Provenance là dữ kiện tái hiện được, không phải bằng chứng đúng (Chương 9).

**BM25.** Hàm xếp hạng từ vựng: score = Σ idf(t) · [f(t,D)(k1+1)] / [f(t,D) + k1(1 − b + b·|D|/avgdl)]. idf nhấn từ hiếm, k1 bão hòa tần suất từ, b chuẩn hóa độ dài tài liệu. Là tiện ích xếp hạng, không phải xác suất đúng (Chương 9).

**Canonical View (Chiếu hình).** Trạng thái 'hiện được chấp nhận là gì' — phép chiếu từ Sổ cái claim. Trả lời câu hỏi hiện hành; chiếu hình trống không có nghĩa Sổ cái trống (Chương 9).

**Citation (Trích dẫn).** Gắn một claim con của câu trả lời với bằng chứng thực sự hỗ trợ nó và nguồn gốc của bằng chứng. Có trích dẫn ≠ được hỗ trợ; trích dẫn phải trỏ tới đoạn thật sự chứa thông tin hỗ trợ (Chương 9).

**Claim Ledger (Sổ cái claim).** Kho bất biến mọi claim có provenance, trạng thái, lịch sử. Truy xuất lịch sử/mâu thuẫn/provenance phải vào Sổ cái, không phải chiếu hình (Chương 9).

**Community retrieval (Truy xuất cộng đồng).** Phân cụm đồ thị (Leiden) và tóm tắt cộng đồng từ dưới lên để trả lời câu hỏi toàn cục. Tóm tắt là đồ tạo tác dẫn xuất có provenance, có thể lỗi thời và mất bằng chứng — không phải nguồn (Chương 9).

**Context assembly (Lắp ráp ngữ cảnh).** Chọn, nhóm, sắp thứ tự, dán nhãn các đơn vị bằng chứng thành đầu vào cho LLM. Thứ tự ảnh hưởng độ tin cậy (lost in the middle); là giao diện suy luận, không phải phép nối chuỗi (Chương 9).

**Contradiction-aware retrieval (Truy xuất nhạy mâu thuẫn).** Khi chủ đề đang tranh cãi, truy xuất các claim cạnh tranh kèm phạm vi và trạng thái, không ép mô hình chọn bên. Không hợp nhất các claim mâu thuẫn mất phạm vi (Chương 9).

**Correctness (Tính đúng).** Quan hệ giữa câu trả lời và thế giới: phát biểu có đúng với sự thật bên ngoài không. Khác với groundedness (quan hệ câu trả lời–nguồn). Bảng 2×2: đúng × có căn cứ, mục tiêu là ô C (Chương 9).

**Dense retrieval (Truy xuất mật độ).** Nhúng câu hỏi và đoạn vào vector (dual encoder, DPR) và chấm bằng tích vô hướng/cosine. Bắt được paraphrase; tương tự nhúng là tín hiệu xếp hạng, không phải liên quan chắc chắn hay chân lý (Chương 9).

**Entity linking (Liên kết thực thể).** Ánh xạ mention trong câu hỏi sang các ứng viên thực thể: sinh ứng viên → chấm điểm ngữ cảnh → quyết định/ghi nhận mơ hồ. Chọn điểm cao nhất không phải bước bắt buộc; mơ hồ phải được ghi nhận (Chương 9).

**Evidence diversity (Đa dạng bằng chứng).** Đa nguồn, đa loại, đa quan điểm, đa thời điểm của bằng chứng. Nhiều đoạn trùng nguồn gốc không phải nhiều bằng chứng độc lập (Chương 9).

**Evidence Packet (Gói bằng chứng).** Khái niệm BOOK-DEFINED: container có cấu trúc là giao diện duy nhất giữa tầng truy xuất và tầng sinh câu trả lời. Chứa câu hỏi, intent, thực thể, claim, đường đi, đoạn nguồn, provenance, thời gian, đánh giá, metadata truy xuất, và nhãn asserted/derived/predicted. Gói đầy đủ trường ≠ đủ bằng chứng (Chương 9).

**Faithfulness (Tính trung thành).** Quan hệ giữa câu trả lời và ngữ cảnh được cấp: câu trả lời không bịa ngoài Gói bằng chứng. Trung thành ≠ đúng với thế giới; trung thành với nguồn sai vẫn sai (Chương 9).

**Gold evidence (Bằng chứng vàng).** Tập chú thích 'đơn vị nào nên được truy xuất cho câu hỏi này' trong benchmark. Là chú thích của bộ dữ liệu, không phải chân lý siêu hình (Chương 9).

**Governance-aware retrieval (Truy xuất theo quản trị).** Lọc/ưu tiên theo trạng thái quản trị của claim theo intent: sản xuất ưu tiên Accepted, nghiên cứu/lịch sử gồm Contested/Superseded. Accepted ≠ đúng, Rejected ≠ sai (Chương 9).

**Graph-first / Text-first (Đồ thị trước / Văn bản trước).** Hai hướng truy xuất: từ đồ thị ra văn bản (graph-first) hay từ văn bản vào đồ thị (text-first). Chọn theo intent; không có bên nào luôn thắng (Chương 9).

**GraphRAG.** Họ kiến trúc retrieval-augmented generation dùng cấu trúc đồ thị tường minh khi truy xuất/lắp ráp ngữ cảnh. Không phải một thuật toán chuẩn duy nhất; Microsoft GraphRAG là một hiện thực. Không đảm bảo trả lời tốt hơn hay loại bỏ hallucination (Chương 9).

**Graph serialization (Tuần tự hóa đồ thị).** Chuyển cấu trúc đồ thị thành dạng LLM đọc được: triple, bảng, JSON, lời văn gọn, thẻ bằng chứng. Không dạng nào mất mát bằng không; lời văn dễ bị nhầm thành suy luận của mô hình (Chương 9).

**Grounded answer (Câu trả lời có căn cứ).** Câu trả lời được hỗ trợ bởi các nguồn mà hệ thống đã xác định (AIS). Có căn cứ ≠ đúng — nguồn có thể sai, lỗi thời, diễn giải sai (Chương 9).

**Hybrid retrieval (Truy xuất lai).** Kết hợp lexical + dense + ràng buộc/đồ thị rồi gộp danh sách (ví dụ RRF). Làm giảm rủi ro bỏ sót, không làm tăng độ đúng nội dung (Chương 9).

**Hypothesis-testing retrieval (Truy xuất kiểm định giả thuyết).** Truy xuất cho giả thuyết cơ chế ứng viên: lấy cả bằng chứng ủng hộ lẫn thách thức (âm tính khó, phản ví dụ, định nghĩa ranh giới). Không-thấy-thách-thức ≠ giả thuyết được chấp nhận (Chương 9).

**Index (Chỉ mục truy xuất).** Cấu trúc truy cập dẫn xuất từ KG để tìm nhanh (chuỗi token hóa, vector nhúng, nhãn, lân cận). Không phải KG, không phải Sổ cái; có thể tụt hậu so với trạng thái hiện tại (Chương 9).

**KGQA (Knowledge Graph Question Answering / Hỏi đáp đồ thị tri thức).** Trả lời bằng truy vấn/suy luận cấu trúc trên đồ thị (SPARQL/path) sau bước entity linking + relation linking. Khác với RAG (sinh từ đoạn văn) và GraphRAG (đồ thị dẫn dắt truy xuất) (Chương 9).

**k-hop neighborhood (Vùng lân cận k-chặng).** Mọi nút/cạnh trong bán kính k của nút neo. Đa số là nhiễu với một câu hỏi cụ thể; trong-k-chặng ≠ liên quan, ngoài-k-chặng ≠ không liên quan (Chương 9).

**Lexical retrieval (Truy xuất từ vựng).** Khớp từ chính xác giữa câu hỏi và tài liệu với trọng số (BM25). Giỏi thuật ngữ chính xác, dốt đồng nghĩa/paraphrase không có từ chung (Chương 9).

**Lost in the Middle.** Hiệu ứng thực nghiệm: mô hình ngôn ngữ dùng thông tin ở đầu/cuối cửa sổ ngữ cảnh đáng tin cậy hơn thông tin ở giữa. Hệ quả kỹ thuật: thứ tự lắp ráp ngữ cảnh ảnh hưởng chất lượng trả lời (Chương 9).

**Multi-hop retrieval (Truy xuất đa chặng).** Bước theo cạnh qua nhiều hop để nối các thực thể trong câu hỏi. Đường đi thể hiện sự kết nối cấu trúc, không phải chứng minh (Chương 9).

**nDCG (Normalized Discounted Cumulative Gain).** Độ đo chất lượng xếp hạng với độ liên quan bậc thang, chiết khấu theo vị trí log, chuẩn hóa bằng thứ tự lý tưởng. Đo chất lượng xếp hạng, không phải độ đúng hay độ tin cậy (Chương 9).

**Path bound (Giới hạn đường đi).** Độ sâu tối đa, loại cạnh, chiều, kiểu nút, nhánh tối đa của phép duyệt. Là ranh giới tri thức luận ngầm: ngoài giới hạn là không được nhìn thấy (Chương 9).

**Path explosion (Bùng nổ đường đi).** Số đường đi giữa các nút tăng theo cấp số nhân khi đồ thị lớn. Cần giới hạn cấu trúc và ưu tiên đường quyết định (Chương 9).

**Precision (Độ chính xác).** Trong số đơn vị đã truy xuất, bao nhiêu là liên quan: |R∩A|/|A|. Đo chất lượng truy xuất, không phải độ đúng của câu trả lời (Chương 9).

**Precision@K / Recall@K.** Độ đo theo cutoff: P@K = liên quan trong top-K / K; R@K = liên quan trong top-K / tổng liên quan. P@K cao + R@K thấp = hệ thống đẹp bề ngoài nhưng giấu bằng chứng (Chương 9).

**Provenance-aware retrieval (Truy xuất nguồn gốc).** Lấy chuỗi Claim→Evidence→SourceFragment→SourceArtifact và các đánh giá/quản trị để trả lời 'vì sao hệ thống tin X'. Sự tồn tại chuỗi là dữ kiện, không phải bằng chứng đúng (Chương 9).

**Query decomposition (Phân rã câu hỏi).** Tách câu hỏi phức thành câu con + đồ thị phụ thuộc. Là một kế hoạch, không phải phép tính chân lý; câu con đúng không tự cộng thành câu trả lời đúng (Chương 9).

**Query drift (Trôi câu hỏi).** Lỗi tích lũy của truy xuất lặp: mỗi lượt subquery lệch thêm khỏi intent gốc. Phải giữ bản ghi intent gốc và provenance của từng subquery (Chương 9).

**Query embedding (Vector câu hỏi).** Biểu diễn học được của câu hỏi dùng để truy xuất. Vector ≠ ý nghĩa; hai phiên bản encoder cho hai thứ hạng khác nhau (Chương 9).

**Query intent (Ý định truy vấn).** Nhãn có cấu trúc của điều câu hỏi muốn: factual, structural, comparative, explanatory, provenance, temporal, contradiction, discovery, multi-hop. Quyết định nguồn truy xuất và loại bằng chứng (Chương 9).

**Query planning (Lập kế hoạch truy vấn).** Chọn và sắp thứ tự các phép truy xuất theo intent. Planner có thể là quy tắc, LLM, hay lai — LLM không bắt buộc; kế hoạch không phải chân lý (Chương 9).

**Query Execution Router (Bộ điều hướng truy vấn).** Khái niệm BOOK-DEFINED: thành phần quyết định đường thực thi từ câu hỏi đã hiểu — KGQA, suy luận tượng trưng, Text RAG, GraphRAG/hybrid, ledger — rồi đóng Evidence Packet cho tầng sinh. Đường chính xác nhất đủ trả lời thắng (Chương 9).

**RAG (Retrieval-Augmented Generation / Sinh có truy xuất).** Kiến trúc kết hợp bộ nhớ tham số (mô hình) với bộ nhớ phi tham số (chỉ mục vector/đoạn văn): truy xuất top-k rồi sinh câu trả lời [Lewis et al. 2020]. RAG ≠ suy luận logic (Chương 9).

**Rank fusion (Hợp hạng).** Gộp nhiều danh sách xếp hạng thành một. RRF dùng hạng (1/(k+rank_i)) nên bền với các thang điểm khác nhau. Điểm hợp là tiện ích truy xuất, không phải độ tin cậy (Chương 9).

**Recall (Độ bao phủ).** Trong số đơn vị đáng lấy, đã lấy được bao nhiêu: |R∩A|/|R|. Câu hỏi giải thích/mâu thuẫn cần recall cao; recall=1 không có nghĩa câu trả lời đúng (Chương 9).

**Reranking (Tái xếp hạng).** Hai giai đoạn: tầng một rộng/rẻ lấy túi ứng viên, tầng hai chấm từng cặp (question, candidate) cho sắc. Không cứu được recall của tầng một (Chương 9).

**Retrieval plan (Kế hoạch truy xuất).** Bộ có thứ tự các phép truy xuất với giới hạn và điều kiện dừng, sinh từ intent + thực thể + phân rã. Kế hoạch chạy xong ≠ đã lấy đủ bằng chứng (Chương 9).

**Retrieval provenance (Provenance truy xuất).** Ghi lại câu hỏi, diễn giải, retriever và phiên bản, index snapshot, bộ lọc, top_k, điểm số, re-ranker, thời gian — đủ để tái hiện. Không chứng minh tính đúng (Chương 9).

**Retrieval unit (Đơn vị truy xuất).** Loại đối tượng một bước truy xuất trả về: thực thể, triple, claim, evidence, đoạn nguồn, đường đi, đồ thị con, tóm tắt, câu trả lời chuẩn. Loại đơn vị quyết định recall/precision và khả năng vết nguồn (Chương 9).

**RRF (Reciprocal Rank Fusion).** Hàm hợp hạng: RRF(d) = Σ 1/(k + rank_i(d)), k≈60. Chỉ dùng hạng, không dùng điểm thô; bền với các thang không so sánh được (Chương 9).

**Score semantics (Ngữ nghĩa điểm số).** Mọi điểm trong đường ống truy xuất (BM25, cosine, re-ranker, khoảng cách đồ thị, độ ưu tiên luật) đều là tín hiệu xếp hạng — không tín hiệu nào là xác suất đúng của câu trả lời (Chương 9).

**Stopping condition (Điều kiện dừng).** Chính sách kết thúc truy xuất lặp: đủ ô bằng chứng, không có thông tin mới, dưới ngưỡng liên quan, hết ngân sách, mâu thuẫn cần con người. Dừng-tìm ≠ đầy đủ (Chương 9).

**Subgraph retrieval (Truy xuất đồ thị con).** Chọn một đồ thị con gắn kết (ứng dụng, cơ chế, vai trò, claim, đoạn nguồn) làm ngữ cảnh. 'Đủ tối thiểu' là theo chính sách, không phải cực tiểu toán học (Chương 9).

**Symbolic graph retrieval (Truy xuất đồ thị tượng trưng).** Truy vấn chính xác (SPARQL) khi lược đồ, thực thể, quan hệ đã biết. Chính xác theo nghĩa khớp mẫu; không xử lý paraphrase chưa có mapping; phản ánh đồ thị, không phản ánh thế giới (Chương 9).

**Temporal retrieval (Truy xuất thời gian).** Truy xuất theo nhiều đồng hồ độc lập: valid time, publication/assertion time, transaction/system time. 'Năm 2020' có nghĩa khác nhau theo từng đồng hồ; không trộn lẫn (Chương 9).

**top_k (Giới hạn kết quả).** Ngưỡng cắt danh sách xếp hạng truy xuất. Là ranh giới tri thức luận: mô hình không suy luận trên bằng chứng ngoài top_k; 'không trong top_k' ≠ không liên quan/không tồn tại (Chương 9).

**Unknown vs Not Found (Không biết vs Không tìm thấy).** Chuỗi phân biệt: không truy xuất được ≠ không có trong index ≠ không có trong KG ≠ đã biết sai ≠ chưa biết. Lỗi truy xuất ≠ thiếu tri thức (Chương 9).
