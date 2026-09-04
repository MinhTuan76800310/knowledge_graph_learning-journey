# Thuật ngữ (Glossary)

Các thuật ngữ được sắp theo bảng chữ cái của tên tiếng Anh. Mỗi mục gồm tên tiếng Anh,
tên/giải thích tiếng Việt, và định nghĩa ngắn dùng trong cuốn sách.

**Abduction (Giả định — lựa chọn giải thích tốt nhất).** Suy luận chọn giả thuyết giải thích tốt nhất cho một quan sát. Khác với quy nạp (tổng quát hóa từ nhiều ví dụ) và suy diễn (hệ quả tất yếu). Chương 8 dạy để tránh nhầm lẫn với quy nạp.

**Abstention (Kiêng trả lời).** Khi bằng chứng không đủ — không có claim liên quan, thực thể mơ hồ chưa phân giải, mâu thuẫn chưa phân xử, hỗ trợ yếu, ngoài phạm vi, truy xuất không chắc — hệ thống nói rõ 'không đủ bằng chứng' thay vì bịa. Kiêng trả lời không có nghĩa sự kiện là sai (Chương 9).

**Agentic retrieval (Truy xuất có tác nhân).** Truy xuất lặp: sau mỗi lượt, kiểm tra khoảng trống và phát hành lượt truy vấn tiếp theo. Cần điều kiện dừng tường minh; rủi ro trôi câu hỏi, leo thang nhiễu/chi phí, thiên kiến xác nhận. Không tự động tốt hơn truy xuất tĩnh (Chương 9).

**Aggregation Window (Cửa sổ tổng hợp).** Khoảng thời gian gộp các quan sát thô thành một số liệu (giờ, ngày, tuần). Cùng một tín hiệu với các cửa sổ khác nhau ra các kết luận khác nhau; không trình bày số liệu mà không nói cửa sổ của nó (Chương 10).

**Alert (Cảnh báo).** Thông báo kích hoạt khi số liệu vượt ngưỡng chính sách, kèm tham chiếu đến quan sát và ngưỡng đã dùng. Cảnh báo tốt cho người đọc tự kiểm chứng; cảnh báo không phải phán quyết chân lý (Chương 10).

**Alias (Bí danh).** Một tên khác cùng biểu thị một thực thể. Khác với định danh chính
tắc, alias không được hệ thống chọn làm tên quy chiếu duy nhất.

**Alpha/Beta network (Mạng alpha/beta).** Hai tầng của mạng RETE (§5.5): nút alpha một đầu vào lọc ràng buộc *trong* một mẫu; nút beta hai đầu vào nối (join) ràng buộc *giữa* các mẫu và cache bộ ghép trung gian trong beta memory. Cơ chế "memory-for-speed": giữ lại các khớp từng phần để không tính lại từ đầu khi dữ liệu thay đổi.

**Answer claim (Claim con của câu trả lời).** Câu trả lời phân rã thành các claim con, mỗi claim vết được về bằng chứng/đường cấu trúc/claim được chấp nhận. Cho phép trích dẫn và đối chiếu theo từng câu (Chương 9).

**Answer generation (Sinh câu trả lời).** Tầng ánh xạ (câu hỏi, Gói bằng chứng) thành bản nháp câu trả lời với bốn kỷ luật: không thêm quan hệ ngoài gói, tách bạch phát ngôn, trình bày mâu thuẫn, tự kiểm tra. Văn bản trôi chảy không có nghĩa đúng (Chương 9).

**Answer provenance (Hồ sơ câu trả lời).** Bản ghi BOOK-DEFINED của một câu trả lời: generatedFor → Câu hỏi, usedEvidence → Evidence Packet, generatedBy, generatedAt, modelVersion, citations, answerStatus. Provenance là dữ kiện tái hiện được, không phải bằng chứng đúng (Chương 9).

**Assertion (Tuyên bố).** Một mệnh đề được khẳng định là đúng trong ngữ cảnh của một đồ thị.
Trong RDF, một triple có mặt trong đồ thị là một assertion. Assertion chưa chắc là tri thức
được chấp nhận (accepted knowledge).

**Assessment (Đánh giá — giai đoạn vòng giám sát).** Bước tri thức luận của Vòng giám sát: quyết định ý nghĩa của tín hiệu và hành động quản trị phù hợp. Đánh giá ≠ hành động tự động; không phán quyết chân lý (Chương 10).

**Assessment Clock (Đồng hồ đánh giá).** Thời điểm hệ thống thực hiện đánh giá (định kỳ hoặc theo sự kiện). Khác Valid Clock (thế giới) và System Clock (hệ thống); không gộp ba đồng hồ thành một timestamp (Chương 10).

**Audit Replay (Tái dựng vết kiểm toán).** Khả năng phát lại vì sao hệ thống tin một câu trả lời: trích dẫn → AuditRecord → chuỗi bằng chứng → quyết định quản trị → nguồn đã đăng ký. Kiểm toán ≠ chỉ ghi log (Chương 10).

**Audit Trail (Vết kiểm toán).** Bản ghi toàn hệ thống về ai nói gì, khi nào, dựa trên gì: quyết định quản trị, authorization, phiên bản nguồn, trạng thái claim. Cho phép tái dựng niềm tin tại mọi thời điểm (Chương 10).

**Automation Gradient (Dốc tự động hóa).** Thang phân bổ quyền quyết định giữa con người và máy theo rủi ro tri thức luận: hành động tự động chỉ ở bậc thấp, leo thang con người ở bậc cao. Cấu hình quản trị, không phải giá trị kỹ thuật (Chương 10).

**Axiom (Tiên đề).** Phát biểu ràng buộc ngữ nghĩa hình thức của các ký hiệu trong ontology.
Khác với chú thích (annotation): tiên đề tạo ra suy diễn, chú thích chỉ dành cho con người.

**Backward Chaining (Suy diễn lùi).** Chiến lược suy diễn goal-driven: bắt đầu từ câu hỏi, tìm
quy tắc có head khớp, tạo subgoal từ body, đệ quy cho đến khi đạt assertion. Ngược hướng với
forward chaining (data-driven). Phù hợp khi ít truy vấn trên đồ thị lớn.

**Batch Governance (Quản trị hàng loạt).** Áp dụng quyết định quản trị (re-validate, retire, supersede) lên nhiều claim cùng lúc với chính sách rõ ràng, log và cơ chế rollback. Thao tác hàng loạt an toàn vì có quản trị, không phải vì chạy nhanh (Chương 10).

**Belief revision (AGM) (Sửa đổi niềm tin AGM).** Lý thuyết hình thức của Alchourrón–Gärdenfors–Makinson về cách một tập niềm tin thay đổi hợp lý khi gặp bằng chứng trái ngược: ba phép mở rộng $K+\varphi$, co rút $K\div\varphi$, sửa đổi $K*\varphi$, nối với nhau qua đẳng thức Levi/Harper và 6 tiên đề tối thiểu (mất ít thông tin nhất) (Chương 6).

**Benchmark Decay (Mục nát benchmark).** Tập kiểm tra cũ dần không còn phản ánh phân phối hiện tại; điểm cao trên benchmark cũ không chứng minh chất lượng hiện tại. Tái tạo benchmark theo đúng quy trình tạo gốc là cách kiểm chứng (Chương 10).

**Bitemporal / 2D bitemporal grid (Song thời gian / Lưới tọa độ bitemporal 2D).** Mô hình lưu mỗi claim dưới dạng hình chữ nhật $R=[T_v^{\text{start}},T_v^{\text{end}}]\times[T_{tx}^{\text{start}},T_{tx}^{\text{end}}]$ trong đó trục ngang là valid time và trục dọc là system/transaction time. Một truy vấn point-probe $(T_v^*,T_{tx}^*)$ kiểm tra claim nào chứa điểm đó; nguyên tắc append-only đảm bảo lịch sử niềm tin không bị xóa (Chương 6).

**Blank node (Nút trống).** Một nút trong đồ thị RDF biểu diễn một tài nguyên tồn tại nhưng
không được đặt tên bằng IRI. Nhãn của blank node chỉ có phạm vi cục bộ trong một tài liệu;
ngữ nghĩa trực giác là "tồn tại một tài nguyên nào đó…".

**BM25.** Hàm xếp hạng từ vựng: score = Σ idf(t) · [f(t,D)(k1+1)] / [f(t,D) + k1(1 − b + b·|D|/avgdl)]. idf nhấn từ hiếm, k1 bão hòa tần suất từ, b chuẩn hóa độ dài tài liệu. Là tiện ích xếp hạng, không phải xác suất đúng (Chương 9).

**Calibration (Hiệu chuẩn).** Mức độ khớp giữa xác suất dự đoán và tần suất đúng thực tế. Mạng nơ-ron hiện đại thường tự tin quá mức (overconfident); temperature scaling cải thiện calibration.

**Candidate Claim (Claim ứng viên).** Tuyên bố đề xuất (từ QA, user sửa, học) chưa được chấp nhận vào Sổ cái. Phải qua cổng quản trị (Ch7) và được đánh giá trước khi trở thành tri thức (Chương 10).

**CandidateAxiom (Tiên đề ứng viên).** Tiên đề do mô hình học quy nạp đề xuất, chưa được đưa vào ontology. Phải qua đánh giá blast radius, kiểm tra nhất quán, và quản trị trước khi chấp nhận.

**CandidateMechanismHypothesis (Giả thuyết cơ chế ứng viên).** Giả thuyết cho rằng nhiều ứng dụng có thể cùng một cơ chế trừu tượng. Mang bằng chứng cấu trúc, hỗ trợ nguồn, bất định, giả thuyết cạnh tranh, và provenance. Là tri thức ứng viên, chưa được chấp nhận.

**Canonical identifier (Định danh chính tắc).** Định danh duy nhất được một hệ thống chọn
làm tên quy chiếu của một thực thể; các tên khác được giữ như alias.

**Canonical View (Chiếu hình).** Trạng thái 'hiện được chấp nhận là gì' — phép chiếu từ Sổ cái claim. Trả lời câu hỏi hiện hành; chiếu hình trống không có nghĩa Sổ cái trống (Chương 9).

**Citation (Trích dẫn).** Gắn một claim con của câu trả lời với bằng chứng thực sự hỗ trợ nó và nguồn gốc của bằng chứng. Có trích dẫn ≠ được hỗ trợ; trích dẫn phải trỏ tới đoạn thật sự chứa thông tin hỗ trợ (Chương 9).

**Claim Ledger (Sổ cái claim).** Kho bất biến mọi claim có provenance, trạng thái, lịch sử. Truy xuất lịch sử/mâu thuẫn/provenance phải vào Sổ cái, không phải chiếu hình (Chương 9).

**Class Expression (Biểu thức lớp).** Tổ hợp của các lớp và thuộc tính tạo thành mô tả phức
tạp: giao (⊓), hợp (⊔), phủ định (¬), hạn chế tồn tại (∃R.C), hạn chế phổ quát (∀R.C).
Mỗi biểu thức có ngữ nghĩa tập hợp chính xác trong diễn giải.

**Classical negation (Phủ định cổ điển).** Ký hiệu ¬, hoạt động dưới Open World Assumption và đơn điệu: ¬P đúng khi P sai trong mọi mô hình; thêm thông tin không bao giờ rút lại một kết luận ¬P đã suy ra. Khác phủ định dạng thất bại (NAF). Trong OWL/RDFS, ¬ là phủ định lớp/thuộc tính model-theoretic, không phải "không thấy trong dữ liệu" (Chương 5).

**Classification (Phân lớp).** Bài toán gán nhãn ứng viên cho một thực thể/ứng dụng dựa trên mô hình học. Đầu ra là xác suất ứng viên, không phải khẳng định kiểu; phải qua quản trị trước khi ghi vào đồ thị.

**Clustering (Phân cụm).** Gom nhóm khám phá dựa trên biểu diễn/đặc trưng, không có nhãn. Cụm không phải lớp ontology. Phân cụm chỉ gợi ý giả thuyết cơ chế, không phải khẳng định.

**Community retrieval (Truy xuất cộng đồng).** Phân cụm đồ thị (Leiden) và tóm tắt cộng đồng từ dưới lên để trả lời câu hỏi toàn cục. Tóm tắt là đồ tạo tác dẫn xuất có provenance, có thể lỗi thời và mất bằng chứng — không phải nguồn (Chương 9).

**Completeness (Tính đầy đủ).** Tính chất của thủ tục suy diễn: mọi hệ quả logic thực sự đều
được sinh ra ($E \subseteq A$). Không có âm tính giả. Phải ghi rõ ngôn ngữ/hồ sơ + chế độ suy
diễn + tác vụ suy luận. OWL RL forward chaining không complete cho OWL 2 DL đầy đủ trên đồ
thị RDF tùy ý; complete dưới các điều kiện syntactic cụ thể (Theorem PR1).

**Completeness over Time (Độ đủ theo thời gian).** Độ đủ đo so với phạm vi khai báo; khi phạm vi đổi (ứng dụng mới, câu hỏi mới), độ đủ giảm dù không claim nào đổi. Tương đối, không bao giờ tuyệt đối (Chương 10).

**ComplEx (Nhúng phức).** Mô hình KGE dùng số phức và tích Hermitian: f(h,r,t) = Re(⟨h, r, t̄⟩). Cho phép mô hình hóa cả quan hệ đối xứng và bất đối xứng.

**Conformance (Sự phù hợp).** Dữ liệu thỏa mãn các shapes SHACL đã định nghĩa. Phù hợp không
có nghĩa dữ liệu đúng với thực tế; vi phạm không có nghĩa dữ liệu sai.

**Consistency (Tính nhất quán).** Ontology nhất quán khi tồn tại ít nhất một mô hình. Khác với
satisfiability (một lớp có thể có thành viên) và entailment (một phát biểu đúng trong mọi mô
hình).

**Consistency over Time (Tính nhất quán theo thời gian).** Không tồn tại xung đột cùng phạm vi tại một thời điểm; mâu thuẫn được quản trị với phạm vi rõ không phải vi phạm nhất quán. Không mâu thuẫn ≠ nhất quán (yên lặng ≠ nhất quán). Đo point-in-time (Chương 10).

**Context (Ngữ cảnh).** Lớp thông tin về nguồn gốc, thời gian, phạm vi và độ tin cậy của một
tuyên bố. Trong mô hình kỹ thuật của sách: KG = Data Graph + Semantics + Context.

**Context assembly (Lắp ráp ngữ cảnh).** Chọn, nhóm, sắp thứ tự, dán nhãn các đơn vị bằng chứng thành đầu vào cho LLM. Thứ tự ảnh hưởng độ tin cậy (lost in the middle); là giao diện suy luận, không phải phép nối chuỗi (Chương 9).

**Contradiction Accumulation (Tích lũy mâu thuẫn).** Quá trình các cặp claim cạnh tranh dồn lại trong hàng đợi khi không được phân xử. Tích lũy được đo, có hạn mức, và leo thang theo chính sách (Chương 10).

**Contradiction Debt (Nợ mâu thuẫn).** Phần nợ tri thức do các cặp mâu thuẫn chưa phân xử; đo bằng số cặp mở, tuổi, phạm vi ảnh hưởng. Khác knowledge debt ở chỗ có ranh giới rõ (Chương 10).

**Contradiction Queue (Hàng đợi mâu thuẫn).** Nơi các mâu thuẫn chưa phân xử được ghi nhận kèm tuổi và phạm vi; độ dài và tuổi là tín hiệu cần leo thang (Chương 10).

**Contradiction-aware retrieval (Truy xuất nhạy mâu thuẫn).** Khi chủ đề đang tranh cãi, truy xuất các claim cạnh tranh kèm phạm vi và trạng thái, không ép mô hình chọn bên. Không hợp nhất các claim mâu thuẫn mất phạm vi (Chương 9).

**Controlled Trust (Tin cậy có kiểm soát).** Mức tin cậy gắn với bằng chứng, provenance, và quản trị; tin cậy được cấp, đo và thu hồi. Khác đức tin: có điều kiện và có thể rút lại (Chương 10).

**Correctness (Tính đúng).** Quan hệ giữa câu trả lời và thế giới: phát biểu có đúng với sự thật bên ngoài không. Khác với groundedness (quan hệ câu trả lời–nguồn). Bảng 2×2: đúng × có căn cứ, mục tiêu là ô C (Chương 9).

**Correctness over Time (Độ đúng theo thời gian).** Độ đúng của claim thay đổi khi bằng chứng, nguồn hoặc bối cảnh đổi; 'từng đúng' khác 'đang đúng'. Accepted ≠ vĩnh viễn (Chương 10).

**Cosine similarity (Độ tương tự cosine).** cos(a,b) = (a·b)/(‖a‖·‖b‖), giá trị trong [−1,1]. Đo góc giữa hai vector. Cosine cao là bằng chứng gợi ý, không phải đồng nhất ngữ nghĩa.

**Cross-domain generalization (Tổng quát hóa chéo miền).** Khả năng mô hình nhận ra cơ chế trong một miền mới dù từ vựng bề mặt khác hẳn. Được kiểm tra bằng thử nghiệm: huấn luyện trên miền A, kiểm tra trên miền B.

**Cumulative fusion (Subjective Logic) (Kết hợp lũy tích).** Phép $\oplus$ kết hợp hai opinion độc lập $\omega_1,\omega_2$ (cùng base rate $a$): $b_\oplus=(b_1u_2+b_2u_1)/(u_1+u_2-u_1u_2)$, tương tự cho $d_\oplus$, và $u_\oplus=u_1u_2/(u_1+u_2-u_1u_2)$. Tính chất chủ chốt: khi hai nguồn đồng thuận, vô tri co hẹp đơn điệu $u_\oplus\le\min(u_1,u_2)$ — thêm bằng chứng cùng chiều làm niềm tin chắc hơn (Chương 6).

**Cypher.** Ngôn ngữ truy vấn khai báo do Neo4j phát triển cho đồ thị thuộc tính, dùng mẫu
ASCII-art (`MATCH ... RETURN`). Cypher tương thích phần lớn với GQL nhưng không trùng khớp.

**Data Drift (Trôi dạt dữ liệu).** Phân phối của đầu vào/ngữ cảnh thay đổi theo thời gian khiến tri thức cũ giảm độ phù hợp. Phát hiện bằng giám sát, xử lý bằng vòng bảo trì có quản trị (Chương 10).

**Data Graph (Đồ thị dữ liệu).** Tập hợp thực thể, quan hệ và thuộc tính mà chưa có định
nghĩa hình thức về ý nghĩa. Trả lời được "có gì" nhưng chưa trả lời được "nghĩa là gì".

**Data leakage (Rò rỉ dữ liệu).** Thông tin từ tập kiểm lọt vào quá trình huấn luyện, làm điểm đánh giá lạc quan giả tạo. Các kiểu: trùng lặp, quan hệ nghịch đảo, đường đi, thực thể, thời gian, nguồn.

**Datalog.** Ngôn ngữ truy vấn/khẳng định dạng luật Horn an toàn, không hàm, không có số hạng mới: head(v) ← body₁(v) ∧ ... ∧ bodyₙ(v) với biến trong đầu phải xuất hiện trong thân (safety/range-restriction). Ba ngữ nghĩa tương đương: mô hình Herbrand nhỏ nhất, chứng minh giới hạn, điểm bất động nhỏ nhất của T_P. Độ phức tạp: PTIME theo dữ liệu, EXPTIME kết hợp. Là nền tảng của các engine suy diễn tiến hiệu quả (Chương 5).

**Deduction (Suy diễn).** Quy tắc chung + tiền đề → hệ quả tất yếu. Bảo toàn chân lý. Không sinh tri thức mới mà chỉ làm tường minh những gì đã ngầm chứa. Khác quy nạp (giả thuyết có thể sai).

**Degradation (Suy thoái).** Suy giảm kéo dài của một chiều chất lượng (độ đúng, độ đủ, độ tươi, nhất quán, đáng tin). Phát hiện bằng mức + xu hướng qua các cửa sổ (Chương 10).

**Dempster–Shafer theory (Lý thuyết bằng chứng Dempster–Shafer).** Tổng quát hóa xác suất Bayes của Shafer: thay vì gán xác suất cho từng mệnh đề, gán **khối lượng** $m:2^{\Theta}\to[0,1]$ cho các tập trong **khung phân biệt** $\Theta$, với $m(\emptyset)=0$ và $\sum m=1$. Khối lượng trên cả $\Theta$ biểu thị vô tri. Hai hàm **Belief** $\mathrm{Bel}(A)=\sum_{B\subseteq A}m(B)$ và **Plausibility** $\mathrm{Pl}(A)=1-\mathrm{Bel}(\bar A)$ kẹp claim vào khoảng $[\mathrm{Bel},\mathrm{Pl}]$. Quy tắc kết hợp Dempster chuẩn hóa qua $1-K$ với $K$ = mức xung đột; khi $K\to1$ (nghịch lý Zadeh) không nên trộn hai nguồn xung đột mà giữ nhánh tách biệt (Chương 6).

**Denotation (Sự biểu thị).** Quan hệ giữa một định danh và thực thể mà nó chỉ đến. Định
danh không phải là thực thể; sự biểu thị do quy ước và con người gán, không tự động có sẵn.

**Dense retrieval (Truy xuất mật độ).** Nhúng câu hỏi và đoạn vào vector (dual encoder, DPR) và chấm bằng tích vô hướng/cosine. Bắt được paraphrase; tương tự nhúng là tín hiệu xếp hạng, không phải liên quan chắc chắn hay chân lý (Chương 9).

**DistMult (Mô hình song tuyến tính).** Mô hình KGE với hàm chấm điểm f(h,r,t) = ⟨h, r, t⟩ (nhân từng phần tử). Đối xứng: không thể phân biệt (h,r,t) và (t,r,h).

**Effective Validation Graph (Đồ thị xác nhận hiệu lực).** Đồ thị thực sự được SHACL validator
xem xét. Có thể là asserted graph, expanded graph (sau materialization), hoặc hybrid. Là
quyết định kiến trúc, phải được document rõ trong hệ thống production.

**Entailment (Suy diễn logic).** O ⊨ α nghĩa là α đúng trong mọi mô hình của ontology O. Suy
diễn là quan hệ ngữ nghĩa mô tả hệ quả logic; bản thân nó không thay đổi hay thêm triple vào
đồ thị. Hệ thống có thể tính toán, vật chất hóa, hoặc lưu cache các hệ quả — nhưng đó là hành
vi triển khai, không phải bản thân quan hệ suy diễn (§5.4). Khác với validation (§5.5):
validation kiểm tra dữ liệu, entailment mô tả hệ quả logic. Luôn ghi rõ entailment regime (§5.9).

**Entailment Regime (Chế độ suy diễn).** Tập quy tắc ngữ nghĩa áp dụng khi tính toán hệ quả
logic. Cùng đồ thị, regime khác nhau cho kết quả khác nhau (Simple, RDFS, OWL RL, OWL
Direct, OWL RDF-Based). Mọi khẳng định về soundness/completeness phải ghi rõ regime. Trong
SPARQL, regime được chỉ định qua Service Description, không phải FROM clause.

**Entity (Thực thể).** Một đối tượng trong thế giới thực hoặc miền vấn đề, được biểu diễn bằng
một nút trong đồ thị.

**Entity linking (Liên kết thực thể).** Ánh xạ mention trong câu hỏi sang các ứng viên thực thể: sinh ứng viên → chấm điểm ngữ cảnh → quyết định/ghi nhận mơ hồ. Chọn điểm cao nhất không phải bước bắt buộc; mơ hồ phải được ghi nhận (Chương 9).

**Escalation Policy (Chính sách leo thang).** Quy tắc quyết định khi nào một tín hiệu (mâu thuẫn, suy thoái) được đưa lên mức quản trị cao hơn: theo hạn mức, tuổi, phạm vi. Chính sách được bản thể hóa và kiểm toán (Chương 10).

**Evidence diversity (Đa dạng bằng chứng).** Đa nguồn, đa loại, đa quan điểm, đa thời điểm của bằng chứng. Nhiều đoạn trùng nguồn gốc không phải nhiều bằng chứng độc lập (Chương 9).

**Evidence Packet (Gói bằng chứng).** Khái niệm BOOK-DEFINED: container có cấu trúc là giao diện duy nhất giữa tầng truy xuất và tầng sinh câu trả lời. Chứa câu hỏi, intent, thực thể, claim, đường đi, đoạn nguồn, provenance, thời gian, đánh giá, metadata truy xuất, và nhãn asserted/derived/predicted. Gói đầy đủ trường ≠ đủ bằng chứng (Chương 9).

**Existential Restriction (Hạn chế tồn tại).** ∃R.C — lớp các cá thể có ít nhất một R-liên kết
đến phần tử thuộc C. Yêu cầu sự tồn tại trong mô hình, không nhất thiết trong dữ liệu RDF.

**Faithfulness (Tính trung thành).** Quan hệ giữa câu trả lời và ngữ cảnh được cấp: câu trả lời không bịa ngoài Gói bằng chứng. Trung thành ≠ đúng với thế giới; trung thành với nguồn sai vẫn sai (Chương 9).

**False negative (Âm tính giả).** Bộ ba thực sự đúng nhưng bị dùng làm mẫu âm trong huấn luyện vì đồ thị chưa đầy đủ (OWA). Làm méo ranh giới học được.

**Feedback Collapse (Sụp đổ phản hồi).** Câu trả lời QA được tái tuần hoàn làm đầu vào học mà không qua cổng quản trị, làm nội dung thoái hóa và sai lệch dần. Phòng ngừa bằng cổng Ch7 và vòng phản hồi an toàn (Chương 10).

**Feedback Loop (Vòng phản hồi).** Vòng tri thức từ hệ thống ra (QA, học) quay lại làm đầu vào. Vòng an toàn khi có cổng quản trị và vết kiểm toán; vòng không có cổng là con đường dẫn tới sụp đổ (Chương 10).

**Feedback Loop Safety (An toàn vòng phản hồi).** Các thuộc tính giữ phản hồi không phá hệ thống: cổng quản trị, tách nguồn khỏi model-generated, đo nhiễm bẩn, vết kiểm toán. An toàn là thuộc tính thiết kế, không phải mặc định (Chương 10).

**Feedback ≠ Evidence (Phản hồi ≠ Bằng chứng).** User sửa, phàn nàn, hay câu trả lời QA là tín hiệu — không phải bằng chứng về chân lý thế giới. Phản hồi vào hệ thống như candidate, được đánh giá như candidate (Chương 10).

**Filtered evaluation (Đánh giá đã lọc).** Trước khi xếp hạng, loại bỏ các bộ ba đúng đã biết khỏi danh sách ứng viên. Cải tiến kỹ thuật, không phải đo lường chân lý tuyệt đối.

**Fixpoint (Điểm bất động).** Trạng thái $G_{n+1} = G_n$ trong forward chaining: vòng lặp
không sinh triple mới, bao đóng đã ổn định. Là điều kiện dừng của thuật toán.

**Focus Node (Nút trọng tâm).** Trong SHACL: nút dữ liệu đang được đánh giá chống lại một
shape. Được chọn bởi cơ chế target (sh:targetClass, sh:targetNode, etc.).

**Forward Chaining (Suy diễn tiến).** Thuật toán suy diễn lặp dùng phép thế $\theta$:
$G_{i+1} = G_i \cup \{ \theta(\text{head}(r)) \mid r \in R, \; \theta(\text{body}(r)) \subseteq G_i \}$,
dừng khi đạt điểm bất động (fixpoint) $G_{n+1} = G_n$. Đảm bảo dừng khi thỏa mãn các điều
kiện: đồ thị hữu hạn, quy tắc hữu hạn, function-free, safe variables.

**Frame of discernment (Khung phân biệt).** Trong lý thuyết Dempster–Shafer, tập $\Theta$ các giả thuyết đôi một loại trừ nhau mà bằng chứng được phân bổ trên đó. Hàm khối lượng gán $m$ cho các tập con của $\Theta$; khối lượng đặt trên chính $\Theta$ (không phải tập đơn nào) biểu thị vô tri — chưa nghiêng về giả thuyết nào (Chương 6).

**Freshness (Độ tươi).** Phép đo tính thời sự: claim còn được bằng chứng hiện tại hỗ trợ gần đây không. Độ tươi không phải phán quyết đúng/sai; tươi ≠ đúng (Chương 10).

**Freshness over Time (Độ tươi theo thời gian).** Độ tươi của index/claim được đo trong cửa sổ thời gian; index lag là số liệu hạng nhất. Tươi theo đồng hồ nào phải nói rõ (Chương 10).

**Freshness ≠ Correctness (Tươi ≠ Đúng).** Một claim tươi (mới kiểm chứng) chưa chứng minh đúng; một claim cũ chưa hẳn sai. Hai trục độc lập (Chương 10).

**GNN (Graph Neural Network / Mạng nơ-ron đồ thị).** Họ mô hình tính theo cấu trúc đồ thị: biểu diễn nút được tính từ lân cận qua truyền thông điệp. Một khung khái niệm, không phải một thuật toán duy nhất.

**Gold evidence (Bằng chứng vàng).** Tập chú thích 'đơn vị nào nên được truy xuất cho câu hỏi này' trong benchmark. Là chú thích của bộ dữ liệu, không phải chân lý siêu hình (Chương 9).

**Governance-aware retrieval (Truy xuất theo quản trị).** Lọc/ưu tiên theo trạng thái quản trị của claim theo intent: sản xuất ưu tiên Accepted, nghiên cứu/lịch sử gồm Contested/Superseded. Accepted ≠ đúng, Rejected ≠ sai (Chương 9).

**GQL.** Ngôn ngữ truy vấn đồ thị chuẩn do ISO ban hành (ISO/IEC 39075:2024).

**Graph pattern matching (Khớp mẫu đồ thị).** Cơ chế truy vấn của SPARQL và Cypher: mô tả một
mẫu đồ thị cần tìm và trả về các phần của đồ thị khớp với mẫu đó.

**Graph Repair (Sửa chữa đồ thị).** Quá trình biến đổi đồ thị để đạt SHACL conformance. Là
bài toán quyết định (decision problem), không phải vá lỗi cú pháp: nhiều candidate repairs
có thể tồn tại, chỉ domain knowledge/governance mới chọn được repair đúng về mặt tri thức.
Passes validation ≠ becomes true.

**Graph serialization (Tuần tự hóa đồ thị).** Chuyển cấu trúc đồ thị thành dạng LLM đọc được: triple, bảng, JSON, lời văn gọn, thẻ bằng chứng. Không dạng nào mất mát bằng không; lời văn dễ bị nhầm thành suy luận của mô hình (Chương 9).

**Graph-first / Text-first (Đồ thị trước / Văn bản trước).** Hai hướng truy xuất: từ đồ thị ra văn bản (graph-first) hay từ văn bản vào đồ thị (text-first). Chọn theo intent; không có bên nào luôn thắng (Chương 9).

**GraphRAG.** Họ kiến trúc retrieval-augmented generation dùng cấu trúc đồ thị tường minh khi truy xuất/lắp ráp ngữ cảnh. Không phải một thuật toán chuẩn duy nhất; Microsoft GraphRAG là một hiện thực. Không đảm bảo trả lời tốt hơn hay loại bỏ hallucination (Chương 9).

**Grounded answer (Câu trả lời có căn cứ).** Câu trả lời được hỗ trợ bởi các nguồn mà hệ thống đã xác định (AIS). Có căn cứ ≠ đúng — nguồn có thể sai, lỗi thời, diễn giải sai (Chương 9).

**Hard negative (Âm tính khó).** Mẫu âm nằm gần ranh giới lớp, buộc mô hình học biên phân biệt có ý nghĩa (ví dụ: FiniteDifference gần RateOfChange). Khác với âm tính dễ ở xa ranh giới.

**Hits@K.** Tỉ lệ các câu trả lời đúng nằm trong top K ứng viên. Không phân biệt giữa hạng 1 và hạng K.

**Hybrid retrieval (Truy xuất lai).** Kết hợp lexical + dense + ràng buộc/đồ thị rồi gộp danh sách (ví dụ RRF). Làm giảm rủi ro bỏ sót, không làm tăng độ đúng nội dung (Chương 9).

**Hypothesis-testing retrieval (Truy xuất kiểm định giả thuyết).** Truy xuất cho giả thuyết cơ chế ứng viên: lấy cả bằng chứng ủng hộ lẫn thách thức (âm tính khó, phản ví dụ, định nghĩa ranh giới). Không-thấy-thách-thức ≠ giả thuyết được chấp nhận (Chương 9).

**Identifier (Định danh).** Chuỗi ký tự dùng để gọi tên một thực thể trong hệ thống (IRI,
Q-id, khóa ứng dụng). Định danh khác thực thể mà nó biểu thị; cùng định danh không chứng
minh thống nhất ngữ nghĩa, khác định danh không chứng minh khác thực thể.

**Identity resolution (Giải quyết định danh).** Quá trình xác định hai định danh trong hai
nguồn có biểu thị cùng một thực thể hay không, đi từ ứng viên đồng nhất qua bằng chứng và
xem xét đến khẳng định được chấp nhận. Đồng nghĩa thực hành với record linkage.

**Immediate consequence operator $T_P$ (Toán tử hệ quả tức thời).** Với tập sự kiện ground $I$, $T_P(I)$ = tập mọi head ground mà thân đã khớp trong $I$: $T_P(I) = \{\theta(\text{head}(r)) \mid r \in P,\ \theta(\text{body}(r)) \subseteq I\}$. Đơn điệu trên vũ trụ ground hữu hạn, nên theo Knaster–Tarski tồn tại điểm bất động nhỏ nhất $\mathrm{lfp}(T_P) = \bigcup_{k\ge0} T_P^k(\emptyset)$; lặp tới nó chính là forward chaining (Chương 5).

**Index (Chỉ mục truy xuất).** Cấu trúc truy cập dẫn xuất từ KG để tìm nhanh (chuỗi token hóa, vector nhúng, nhãn, lân cận). Không phải KG, không phải Sổ cái; có thể tụt hậu so với trạng thái hiện tại (Chương 9).

**Induction / Quy nạp (induction).** Tổng quát hóa mẫu từ các quan sát, sinh ra giả thuyết có thể sai. Không phải suy diễn (bảo toàn chân lý). Tri thức quy nạp bao gồm cả mô hình mã hóa mẫu lẫn dự đoán của mô hình.

**Inductive bias (Thiên kiến quy nạp).** Tập giả định cấu trúc của một họ mô hình về mẫu nào đáng học. Ví dụ: TransE (h+r≈t), DistMult (đối xứng), ComplEx (Hermitian).

**Inductive KG learning (Học quy nạp trên đồ thị).** Mô hình tổng quát hóa tới các thực thể/subgraph chưa từng thấy trong huấn luyện. Khác học chuyển dẫn (chỉ dự đoán giữa thực thể đã biết).

**Interpretation (Diễn giải).** Cách gán nghĩa toán học cho ký hiệu: I = (Δ^I, ·^I), trong đó
Δ^I là miền diễn giải và ·^I ánh xạ lớp → tập hợp, thuộc tính → quan hệ, cá thể → phần tử.

**Invariant structure (Cấu trúc bất biến).** Phần cấu trúc được giữ lại khi trừu tượng hóa một cơ chế từ nhiều ứng dụng. Phần chi tiết miền bị bỏ đi gọi là cấu trúc ngẫu nhiên (incidental).

**IRI (Internationalized Resource Identifier).** Cơ chế định danh có phạm vi toàn cục trong
RDF. Cùng một IRI không tự động chứng minh hai bên cùng ngữ nghĩa; hai IRI khác nhau chưa
chắc là hai thực thể khác nhau.

**k-hop neighborhood (Vùng lân cận k-chặng).** Mọi nút/cạnh trong bán kính k của nút neo. Đa số là nhiễu với một câu hỏi cụ thể; trong-k-chặng ≠ liên quan, ngoài-k-chặng ≠ không liên quan (Chương 9).

**KGQA (Knowledge Graph Question Answering / Hỏi đáp đồ thị tri thức).** Trả lời bằng truy vấn/suy luận cấu trúc trên đồ thị (SPARQL/path) sau bước entity linking + relation linking. Khác với RAG (sinh từ đoạn văn) và GraphRAG (đồ thị dẫn dắt truy xuất) (Chương 9).

**Knowledge Debt (Nợ tri thức).** Chi phí tích lũy của các nghĩa vụ tri thức chưa thanh toán: claim chưa re-validate, mâu thuẫn chưa phân xử, index chưa cập nhật. Nợ khác với sai — có thể sống chung nếu đo và trả (Chương 10).

**Knowledge Graph (Đồ thị Tri thức).** Theo nghĩa tối thiểu: đồ thị có hướng có nhãn, trong đó
nhãn mang ngữ nghĩa được định nghĩa. Theo mô hình kỹ thuật của sách: Data Graph + Semantics
+ Context.

**Knowledge Graph Embedding (KGE / Nhúng đồ thị tri thức).** Học vector thực thể và quan hệ + hàm chấm điểm f(h,r,t). Điểm cao = hợp lý hơn, không phải đúng. Gồm các mô hình: TransE, DistMult, ComplEx.

**Labeled Property Graph (Đồ thị Thuộc tính có nhãn).** Mô hình đồ thị gồm nút (có nhãn và
thuộc tính) và quan hệ (có hướng, có kiểu, và có thể có thuộc tính). Neo4j là một triển khai.

**Level vs Trend (Mức vs Xu hướng).** Mức là trạng thái hiện tại; xu hướng là đạo hàm qua cửa sổ. Xu hướng dự báo tốt hơn cho bảo trì; một mức không nói lên suy thoái (Chương 10).

**Levi identity (Đẳng thức Levi).** Trong AGM, phép sửa đổi biểu diễn qua co rút và mở rộng: $K*\varphi = (K\div\neg\varphi)+\varphi$ — muốn tiếp nhận $\varphi$ thì trước hết bỏ cái đối lập $\neg\varphi$, rồi thêm $\varphi$. Tương ứng thao tác "dời claim cũ sang Superseded rồi thêm claim mới" (Chương 6).

**Lexical retrieval (Truy xuất từ vựng).** Khớp từ chính xác giữa câu hỏi và tài liệu với trọng số (BM25). Giỏi thuật ngữ chính xác, dốt đồng nghĩa/paraphrase không có từ chung (Chương 9).

**Link prediction (Dự đoán liên kết).** Với đồ thị quan sát được một phần, xếp hạng các bộ ba ứng viên còn thiếu. Đầu ra là danh sách có thứ tự, không phải sự thật được khẳng định.

**Literal.** Giá trị dữ liệu trong RDF (chuỗi, số, …), chỉ xuất hiện ở vị trí đối tượng của
bộ ba.

**Living Architecture (Kiến trúc sống).** Mô hình hệ thống tri thức như một tập các vòng phản hồi (thu nhận, học, truy xuất, giám sát, bảo trì, quản trị) thay vì pipeline tuyến tính. Mô hình kỹ thuật của sách, không phải sản phẩm (Chương 10).

**Least fixed point (Điểm bất động nhỏ nhất).** Theo định lý Knaster–Tarski: $T_P$ đơn điệu trên dàn đầy đủ (tập con của ground universe) → có điểm bất động nhỏ nhất $\mathrm{lfp}(T_P) = \bigcup_{k\ge0} T_P^k(\emptyset)$. $\mathrm{lfp}(T_P)$ chính là mô hình Herbrand nhỏ nhất $\mathcal{M}(P)$ và là kết quả của forward chaining. Mọi quy tắc đều đã được áp dụng hết (Chương 5).

**Living Knowledge System (Hệ thống tri thức sống).** Một tiến trình vận hành liên tục: thu nhận, học, truy xuất, giám sát, bảo trì và quản trị cùng vận động; không phải cơ sở dữ liệu tĩnh (Chương 10).

**Local Closed-World Semantics (Ngữ nghĩa thế giới đóng cục bộ).** SHACL đọc sự vắng mặt của một bộ ba *trong đồ thị dữ liệu đang xét* như "không thỏa ràng buộc", nhưng không giả định đóng thế giới toàn cục như CWA cổ điển. Hệ quả: thêm bộ ba có thể lật kết quả từ conform sang violate (vd `sh:maxCount`), nên SHACL **phi đơn điệu** — khác forward chaining đơn điệu (Chương 5).

**Lost in the Middle.** Hiệu ứng thực nghiệm: mô hình ngôn ngữ dùng thông tin ở đầu/cuối cửa sổ ngữ cảnh đáng tin cậy hơn thông tin ở giữa. Hệ quả kỹ thuật: thứ tự lắp ráp ngữ cảnh ảnh hưởng chất lượng trả lời (Chương 9).

**Maintenance Operations (Thao tác bảo trì).** Các thao tác có quản trị: re-validate, re-assess, retire, supersede, reindex. Mỗi thao tác có tác nhân, authorization, log và vết kiểm toán (Chương 10).

**Materialization (Vật chất hóa).** Chiến lược triển khai suy diễn bằng cách tính toán trước
bao đóng và lưu trữ kết quả. Khác với bản thân quan hệ entailment (là khái niệm ngữ nghĩa,
không phải thao tác tính toán). Có thể không khả thi với ontology quá biểu cảm. So sánh với
query-time reasoning (§5.4).

**Mass function (Hàm khối lượng).** Trong lý thuyết Dempster–Shafer, hàm $m: 2^{\Theta} \to [0,1]$ với $m(\emptyset) = 0$ và $\sum_{B \subseteq \Theta} m(B) = 1$, gán khối lượng cho mỗi tập con của khung phân biệt $\Theta$. $m(\Theta)=1$ = vô tri toàn phần, khác hẳn $m(\{\text{Acc}\}) = 0.5$ — ghim một nửa lên tập đơn (Chương 6).

**Message passing (Truyền thông điệp).** Cơ chế tính toán của GNN: message → aggregate → update. Mỗi nút gửi thông điệp đến lân cận, tập hợp chúng, và cập nhật biểu diễn. Là một khung, không phải một thuật toán.

**Minimal Herbrand model (Mô hình Herbrand nhỏ nhất).** Giao của mọi mô hình Herbrand của chương trình $P$ chứa các sự kiện đã khẳng định $D$. Với Datalog an toàn không hàm, $\mathcal{M}(P)$ trùng với $\mathrm{lfp}(T_P)$ và với tập mọi sự kiện chứng minh được — ba ngữ nghĩa tương đương. Là nền tảng ngữ nghĩa model-theoretic của bao đóng suy diễn (Chương 5).

**Model (Mô hình).** Diễn giải thỏa mãn tất cả các tiên đề trong ontology. Tập hợp các mô hình
xác định ngữ nghĩa của ontology: suy diễn = đúng trong mọi mô hình.

**Model Assessment (Đánh giá mô hình).** Đối tượng bọc điểm số với ngữ nghĩa: target, model, task, score, score semantics, assessed-at, training dataset, evaluation context. Ngăn chặn 'con số vô danh'.

**Model collapse (Sụp đổ mô hình).** Hiện tượng mô hình huấn luyện trên dữ liệu do chính mô hình sinh ra làm mất dần đa dạng tri thức, tích lũy khiếm khuyết không thể đảo ngược.

**Monitored ≠ Governed (Giám sát ≠ Quản trị).** Giám sát chỉ quan sát và cảnh báo; quản trị ra quyết định và chịu trách nhiệm. Hệ thống tự giám sát không tự quản trị đúng (Chương 10).

**Monitoring Loop (Vòng giám sát).** Cơ chế trung tâm Ch10: COLLECT → AGGREGATE → COMPARE → ALERT → ASSESS → ACT → RE-MEASURE. Vòng quyết định sự chú ý và bảo trì, không quyết định chân lý (Chương 10).

**Monotonicity (Tính đơn điệu).** Tính chất của chế độ suy diễn: nếu $G \subseteq G'$ thì
$\text{Consequences}(G) \subseteq \text{Consequences}(G')$. Thêm thông tin vào đồ thị không
bao giờ làm mất kết luận cũ. Khác với termination, completeness, và consistency.

**MRR (Mean Reciprocal Rank).** Trung bình của 1/hạng của câu trả lời đúng. MRR = 1.0 nếu luôn đứng hạng 1. Bị ảnh hưởng nhiều bởi các hạng cao.

**Multi-hop retrieval (Truy xuất đa chặng).** Bước theo cạnh qua nhiều hop để nối các thực thể trong câu hỏi. Đường đi thể hiện sự kết nối cấu trúc, không phải chứng minh (Chương 9).

**N-ary relation (Quan hệ n-ary).** Quan hệ có nhiều hơn hai người tham gia, hoặc quan hệ
cần mang thêm thuộc tính (thời gian, độ tin cậy). Trong RDF được biểu diễn gián tiếp, phổ
biến nhất bằng một thực thể trung gian đại diện cho sự kiện quan hệ.

**Named graph (Đồ thị có tên).** Một cặp (tên đồ thị, đồ thị RDF) trong RDF dataset. Tên đồ
thị chỉ được ghép cặp cú pháp với đồ thị; ý nghĩa provenance/nguồn là quy ước ứng dụng,
không phải ngữ nghĩa hình thức có sẵn.

**nDCG (Normalized Discounted Cumulative Gain).** Độ đo chất lượng xếp hạng với độ liên quan bậc thang, chiết khấu theo vị trí log, chuẩn hóa bằng thứ tự lý tưởng. Đo chất lượng xếp hạng, không phải độ đúng hay độ tin cậy (Chương 9).

**Negative sampling (Lấy mẫu âm).** Thủ thuật huấn luyện: tạo bộ ba nhiễu bằng cách thay thế đầu/cuối của bộ ba đúng. Là giả định kỹ thuật, không phải khẳng định bộ ba đó sai. Thiếu ≠ sai (OWA).

**Negation as Failure — NAF (Phủ định dạng thất bại).** Ký hiệu `not` / $\sim$ trong Datalog có phủ định: $\text{not } P$ đúng khi $P$ **không chứng minh được** từ dữ liệu (đọc theo CWA). Phi đơn điệu: thêm sự kiện có thể làm một kết luận chứa NAF trở nên sai. Không nhất quán khi có vòng lặp phủ định không phân tầng (vd `p ← not q`, `q ← not p` → hai mô hình nhỏ nhất). Cần stratification để có mô hình duy nhất (Chương 5).

**Never-Done (Hệ thống không bao giờ 'xong').** Tri thức sống liên tục cần duy trì: tái xác minh, tái đánh giá, phân xử mâu thuẫn. 'Xong' là ảo tưởng của hệ tĩnh (Chương 10).

**Ontology (Bản thể học).** Tập tiên đề ràng buộc ngữ nghĩa hình thức của các ký hiệu trong một
miền tri thức. Khác với schema: ontology nhấn mạnh cam kết ngữ nghĩa và hệ quả logic, không
chỉ cấu trúc kỳ vọng.

**OOV entity (Out-of-vocabulary entity / Thực thể ngoài từ vựng).** Thực thể không có vector học sẵn vì chưa xuất hiện trong huấn luyện. Cần biểu diễn từ lân cận/thuộc tính hoặc mô hình quy nạp (GNN).

**Open World Assumption — OWA (Giả định thế giới mở).** Trong OWL, thiếu thông tin không có
nghĩa là sai; nó chỉ có nghĩa là chưa biết. Khác với cơ sở dữ liệu truyền thống dùng giả định
thế giới đóng (thiếu = sai/vắng).

**Orchestration (Điều phối).** Sắp xếp các vòng phản hồi hoạt động cùng nhau: xung đột tài nguyên, ưu tiên, xếp hàng, và vết kiểm toán xuyên vòng (Chương 10).

**Oversmoothing (Làm mịn quá mức).** Khi xếp nhiều lớp GNN, biểu diễn các nút hội tụ về nhau, mất thông tin phân biệt. Số lớp tối ưu thường nhỏ (1–3).

**owl:sameAs.** Vị từ OWL khẳng định hai định danh biểu thị **cùng một cá thể**. Không phải
"tương tự" hay "gần giống": mọi thông tin của tên này suy ra được cho tên kia.

**Path bound (Giới hạn đường đi).** Độ sâu tối đa, loại cạnh, chiều, kiểu nút, nhánh tối đa của phép duyệt. Là ranh giới tri thức luận ngầm: ngoài giới hạn là không được nhìn thấy (Chương 9).

**Path explosion (Bùng nổ đường đi).** Số đường đi giữa các nút tăng theo cấp số nhân khi đồ thị lớn. Cần giới hạn cấu trúc và ưu tiên đường quyết định (Chương 9).

**Path-based explanation (Giải thích theo đường đi).** Giải thích dự đoán bằng cách chỉ ra đường đi trong đồ thị dẫn tới kết luận. Tự nhiên với học quy tắc, khó với KGE/GNN.

**Point-probe (Thăm dò điểm).** Trong mô hình bitemporal 2D, một truy vấn là một điểm $(T_v^*, T_{tx}^*)$ trong lưới tọa độ (valid time × system time). Câu trả lời là claim có hình chữ nhật chứa điểm đó — kiểm tra bằng hai bất đẳng thức $T_v^{\text{start}} \le T_v^* < T_v^{\text{end}}$ và $T_{tx}^{\text{start}} \le T_{tx}^* < T_{tx}^{\text{end}}$. Cùng một năm hiệu lực nhưng hai thời điểm hỏi khác nhau cho hai câu trả lời khác nhau (Chương 6).

**Precision (Độ chính xác).** Trong số đơn vị đã truy xuất, bao nhiêu là liên quan: |R∩A|/|A|. Đo chất lượng truy xuất, không phải độ đúng của câu trả lời (Chương 9).

**Precision@K / Recall@K.** Độ đo theo cutoff: P@K = liên quan trong top-K / K; R@K = liên quan trong top-K / tổng liên quan. P@K cao + R@K thấp = hệ thống đẹp bề ngoài nhưng giấu bằng chứng (Chương 9).

**Prediction (Dự đoán).** Đầu ra của mô hình học: gán điểm số cho một cấu trúc khả dĩ. Không phải suy dẫn (entailment). Điểm cao ≠ chân lý.

**Property Graph.** Xem Labeled Property Graph.

**Provenance-aware retrieval (Truy xuất nguồn gốc).** Lấy chuỗi Claim→Evidence→SourceFragment→SourceArtifact và các đánh giá/quản trị để trả lời 'vì sao hệ thống tin X'. Sự tồn tại chuỗi là dữ kiện, không phải bằng chứng đúng (Chương 9).

**Qualifier (Định ngữ).** Trong Wikidata: cặp thuộc tính–giá trị gắn vào một statement để mở
rộng ngữ cảnh (thời điểm, phạm vi, phương pháp) mà không thay thế nội dung cốt lõi.

**Quality Dimension (Chiều chất lượng tri thức).** Một trong năm chiều: Correctness, Completeness, Freshness, Consistency, Trustworthiness. Mỗi chiều có định nghĩa, thước đo, cửa sổ, và điều nó KHÔNG đo (Chương 10).

**Quality ≠ Truth (Chất lượng ≠ Chân lý).** Điểm chất lượng mô tả hành vi quản lý tri thức, không phải chân lý thế giới. 'Chất lượng 0.92' không làm claim đúng (Chương 10).

**Query decomposition (Phân rã câu hỏi).** Tách câu hỏi phức thành câu con + đồ thị phụ thuộc. Là một kế hoạch, không phải phép tính chân lý; câu con đúng không tự cộng thành câu trả lời đúng (Chương 9).

**Query drift (Trôi câu hỏi).** Lỗi tích lũy của truy xuất lặp: mỗi lượt subquery lệch thêm khỏi intent gốc. Phải giữ bản ghi intent gốc và provenance của từng subquery (Chương 9).

**Query embedding (Vector câu hỏi).** Biểu diễn học được của câu hỏi dùng để truy xuất. Vector ≠ ý nghĩa; hai phiên bản encoder cho hai thứ hạng khác nhau (Chương 9).

**Query Execution Router (Bộ điều hướng truy vấn).** Khái niệm BOOK-DEFINED: thành phần quyết định đường thực thi từ câu hỏi đã hiểu — KGQA, suy luận tượng trưng, Text RAG, GraphRAG/hybrid, ledger — rồi đóng Evidence Packet cho tầng sinh. Đường chính xác nhất đủ trả lời thắng (Chương 9).

**Query intent (Ý định truy vấn).** Nhãn có cấu trúc của điều câu hỏi muốn: factual, structural, comparative, explanatory, provenance, temporal, contradiction, discovery, multi-hop. Quyết định nguồn truy xuất và loại bằng chứng (Chương 9).

**Query planning (Lập kế hoạch truy vấn).** Chọn và sắp thứ tự các phép truy xuất theo intent. Planner có thể là quy tắc, LLM, hay lai — LLM không bắt buộc; kế hoạch không phải chân lý (Chương 9).

**R-GCN (Relational Graph Convolutional Network).** GNN cho đồ thị đa quan hệ: mỗi loại quan hệ có ma trận biến đổi riêng. Thường dùng encoder (R-GCN) + decoder (DistMult) cho link prediction.

**RAG (Retrieval-Augmented Generation / Sinh có truy xuất).** Kiến trúc kết hợp bộ nhớ tham số (mô hình) với bộ nhớ phi tham số (chỉ mục vector/đoạn văn): truy xuất top-k rồi sinh câu trả lời [Lewis et al. 2020]. RAG ≠ suy luận logic (Chương 9).

**Rank fusion (Hợp hạng).** Gộp nhiều danh sách xếp hạng thành một. RRF dùng hạng (1/(k+rank_i)) nên bền với các thang điểm khác nhau. Điểm hợp là tiện ích truy xuất, không phải độ tin cậy (Chương 9).

**RDF (Resource Description Framework).** Mô hình dữ liệu chuẩn của W3C biểu diễn tri thức
dưới dạng các bộ ba (subject, predicate, object).

**Re-assessment (Tái đánh giá).** Đánh giá lại một claim khi có tín hiệu mới (nguồn mới, bằng chứng thay đổi); có thể chuyển trạng thái Accepted → Contested. Ghi vết kiểm toán (Chương 10).

**Re-validation (Tái xác minh).** Kiểm tra lại một claim đã chấp nhận theo bằng chứng mới nhất; quy trình giống lần đầu nhưng trả lời 'vẫn còn đúng không'. Re-validation có quản trị (Chương 10).

**Recall (Độ bao phủ).** Trong số đơn vị đáng lấy, đã lấy được bao nhiêu: |R∩A|/|R|. Câu hỏi giải thích/mâu thuẫn cần recall cao; recall=1 không có nghĩa câu trả lời đúng (Chương 9).

**Record linkage (Liên kết bản ghi).** Bài toán suy luận xem hai bản ghi từ các nguồn khác
nhau có phải cùng một thực thể thế giới thực hay không. Là suy luận không chắc chắn, cần
bằng chứng và xác nhận; các thuật toán công nghiệp (blocking, matching) thuộc Chương 7.

**Reification (Tái hiện).** Kỹ thuật biến một bộ ba/quan hệ thành một tài nguyên để có thể gắn
thêm thông tin cho nó.

**Relation (Quan hệ).** Mối liên hệ giữa hai thực thể, biểu diễn bằng cạnh có nhãn.

**Representation learning (Học biểu diễn).** Học vector từ dữ liệu thay vì thiết kế đặc trưng thủ công. Vector học được không phải thực thể và không mang ngữ nghĩa hình thức.

**Reranking (Tái xếp hạng).** Hai giai đoạn: tầng một rộng/rẻ lấy túi ứng viên, tầng hai chấm từng cặp (question, candidate) cho sắc. Không cứu được recall của tầng một (Chương 9).

**RETE algorithm (Thuật toán RETE).** Thuật toán khớp mẫu nhiều-luật của Forgy (1982) [RETE-01]: xây mạng các nút alpha (lọc trong một mẫu) và beta (nối giữa các mẫu, cache bộ ghép) để tái sử dụng khớp từng phần khi dữ liệu thay đổi. WME (Working Memory Element) là đơn vị dữ liệu vào mạng; agenda + conflict resolution quyết định luật nào fire. Tính cùng bao đóng $\mathrm{lfp}(T_P)$ như forward chaining naive nhưng nhanh hơn bằng đánh đổi bộ nhớ (Chương 5).

**Retirement (Nghỉ hưu).** Đưa tri thức ra khỏi dòng hoạt động với bản ghi có quản trị; nghỉ hưu ≠ xóa — lịch sử niềm tin được giữ (Chương 10).

**Retrieval plan (Kế hoạch truy xuất).** Bộ có thứ tự các phép truy xuất với giới hạn và điều kiện dừng, sinh từ intent + thực thể + phân rã. Kế hoạch chạy xong ≠ đã lấy đủ bằng chứng (Chương 9).

**Retrieval provenance (Provenance truy xuất).** Ghi lại câu hỏi, diễn giải, retriever và phiên bản, index snapshot, bộ lọc, top_k, điểm số, re-ranker, thời gian — đủ để tái hiện. Không chứng minh tính đúng (Chương 9).

**Retrieval unit (Đơn vị truy xuất).** Loại đối tượng một bước truy xuất trả về: thực thể, triple, claim, evidence, đoạn nguồn, đường đi, đồ thị con, tóm tắt, câu trả lời chuẩn. Loại đơn vị quyết định recall/precision và khả năng vết nguồn (Chương 9).

**RRF (Reciprocal Rank Fusion).** Hàm hợp hạng: RRF(d) = Σ 1/(k + rank_i(d)), k≈60. Chỉ dùng hạng, không dùng điểm thô; bền với các thang không so sánh được (Chương 9).

**Rule (Quy tắc).** Mệnh đề dạng Horn: head ← body₁ ∧ ... ∧ bodyₙ. Trong KG, head và body
là mẫu triple chứa biến. Phép thế $\theta$ gán biến với giá trị cụ thể để kết nối quy tắc
trừu tượng với dữ liệu đồ thị. Quy tắc Horn đơn điệu, đảm bảo dừng trên đồ thị hữu hạn với
các điều kiện an toàn. Không biểu diễn được phủ định hay disjunction trong head.

**Rule induction (Học quy tắc).** Học quy tắc tượng trưng từ đồ thị. AMIE+ sinh quy tắc đường đi r1(x,y) ∧ r2(y,z) → r3(x,z) dưới giả định PCA. Quy tắc học được là giả thuyết, không phải định luật logic.

**Rule-mining confidence (Độ tin cậy khai phá quy tắc).** Tần suất quy tắc dưới giả định PCA (Partial Completeness Assumption). Khác với độ tin cậy tri thức luận (epistemic confidence) của Chương 6 — hai khái niệm khác nhau, cùng tên 'confidence'.

**Satisfiability (Tính thỏa được).** Lớp C thỏa được đối với ontology O khi tồn tại ít nhất một
mô hình của O trong đó C^I ≠ ∅. Khác với consistency (toàn bộ ontology có mô hình) và
entailment (phát biểu đúng trong mọi mô hình).

**Schema (Lược đồ).** Phần mô tả cấu trúc và từ vựng được kỳ vọng của đồ thị dữ liệu: lớp,
quan hệ, kiểu thuộc tính, ràng buộc. Lược đồ không phải ontology: nó cho bộ khung từ vựng
chứ chưa cho ngữ nghĩa suy luận đầy đủ.

**Score semantics (Ngữ nghĩa điểm số).** Mọi điểm trong đường ống truy xuất (BM25, cosine, re-ranker, khoảng cách đồ thị, độ ưu tiên luật) đều là tín hiệu xếp hạng — không tín hiệu nào là xác suất đúng của câu trả lời (Chương 9).

**Scoring function (Hàm chấm điểm).** Hàm số f(h,r,t) gán giá trị thực cho mỗi bộ ba, đo mức độ hợp lý. Mỗi họ mô hình KGE có một hàm chấm điểm khác nhau.

**Self-Observation (Tự quan sát).** Hệ thống quan sát chính mình: log, ledger diff, index state, hàng đợi. Ghi log không có nghĩa hiểu chính mình; log là nhiên liệu cho vòng giám sát (Chương 10).

**Self-reinforcing feedback (Vòng phản hồi tự củng cố).** Khi dự đoán của mô hình quay lại làm dữ liệu huấn luyện, vòng phản hồi hình thành. Phân biệt tri thức do nguồn sinh ra và do mô hình sinh ra (model-generated candidate).

**Semantics (Ngữ nghĩa).** Lớp ý nghĩa của đồ thị: schema, ontology, identity, constraints.

**SHACL (Shapes Constraint Language).** Ngôn ngữ chuẩn W3C để xác nhận dữ liệu RDF dựa trên
shapes. Shapes định nghĩa ràng buộc kiểm tra, không phải tiên đề suy diễn. Kết quả là
validation report (conforms/violation), không phải tri thức mới. SHACL không phải "OWL với
Closed World Assumption."

**SHACL Instance.** Trong SHACL: quan hệ thành viên lớp bao gồm chuỗi `rdfs:subClassOf*`.
Một nút typed CapitalCity là SHACL instance của City nếu CapitalCity rdfs:subClassOf City.
Khác với exact rdf:type triple grep.

**Shape.** Điều kiện kiểm tra trong SHACL nhắm đến tập nút dữ liệu. Shape không tham gia
vào RDFS/OWL entailment. Khác với ontology axiom: shape kiểm tra thông tin, axiom thêm
thông tin.

**Six Flows of Change (Sáu luồng thay đổi).** Các dòng biến động khiến hệ tri thức lệch khỏi thực tại: nguồn mới, nguồn đổi, claim đổi, quan hệ đổi, phạm vi đổi, ngữ cảnh đổi. Nền tảng của giám sát (Chương 10).

**Solution mapping (Ánh xạ nghiệm).** Trong SPARQL: một phép gán biến với các hạng mục của đồ
thị sao cho mẫu truy vấn khớp. Kết quả truy vấn là tập các ánh xạ nghiệm.

**Soundness (Tính đúng đắn).** Tính chất của thủ tục suy diễn: mọi kết quả sinh ra đều là hệ
quả logic thực sự. Không có dương tính giả. Phải ghi rõ ngôn ngữ/hồ sơ + chế độ suy diễn +
tác vụ suy luận.

**Source leakage (Rò rỉ nguồn).** Cùng một nguồn (ví dụ sách) xuất hiện ở cả train và test, làm quá lạc quan về khả năng tổng quát hóa. Biện pháp: chia tách theo nguồn.

**SPARQL.** Ngôn ngữ truy vấn chuẩn của W3C cho RDF, hoạt động bằng khớp mẫu đồ thị.

**Spurious correlation (Tương quan giả).** Quan hệ học được giữa dấu hiệu bề mặt và nhãn, xuất hiện trong dữ liệu huấn luyện nhưng không phải cấu trúc cơ chế. Dẫn đến học lối tắt (shortcut learning).

**Staleness (Cũ / ứ đọng).** Tình trạng một claim còn đó nhưng không còn được bằng chứng hiện tại hỗ trợ. Cũ ≠ sai: có thể vẫn đúng nhưng chưa được kiểm chứng lại (Chương 10).

**Stopping condition (Điều kiện dừng).** Chính sách kết thúc truy xuất lặp: đủ ô bằng chứng, không có thông tin mới, dưới ngưỡng liên quan, hết ngân sách, mâu thuẫn cần con người. Dừng-tìm ≠ đầy đủ (Chương 9).

**Stratified Datalog (Datalog phân tầng).** Chương trình Datalog có NAF được phân tầng khi tồn tại ánh xạ $s$ từ vị từ sang số nguyên sao cho nếu $Q$ xuất hiện trong phạm vi `not` của một luật có head $P$, thì $s(Q) < s(P)$. Khi đó chương trình có **perfect model** duy nhất, tính được bằng cách lặp từng tầng theo thứ tự tăng dần. Không phân tầng được → mơ hồ ngữ nghĩa (Chương 5).

**Structural similarity (Tương tự cấu trúc).** Đánh giá đa chiều hai cấu trúc chia sẻ mẫu vai trò, thao tác, kiểu đối số. Tương tự ≠ đồng nhất, ≠ owl:sameAs.

**Subgraph retrieval (Truy xuất đồ thị con).** Chọn một đồ thị con gắn kết (ứng dụng, cơ chế, vai trò, claim, đoạn nguồn) làm ngữ cảnh. 'Đủ tối thiểu' là theo chính sách, không phải cực tiểu toán học (Chương 9).

**Subject / Predicate / Object (Chủ thể / Vị từ / Đối tượng).** Ba vị trí của một bộ ba RDF.
Chủ thể là IRI hoặc blank node; vị từ chỉ là IRI; đối tượng là IRI, literal hoặc blank node.

**Subjective logic (Logic chủ quan).** Khung của Jøsang biểu diễn niềm tin về một mệnh đề bằng **opinion** $\omega = (b, d, u, a)$: belief, disbelief, uncertainty ($b+d+u=1$) và base rate $a$. Sống trên tam giác đều 2-simplex (tọa độ trọng tâm); **xác suất chủ quan** tham chiếu $P(x) = b + a \cdot u$. Hai opinion độc lập kết hợp bằng **cumulative fusion** $\oplus$ với tính chất co hẹp vô tri đơn điệu khi đồng thuận. Tương đương số học với Dempster–Shafer nhưng trực quan hơn về hình học (Chương 6).

**Substitution (Phép thế).** Ánh xạ $\theta$ gán mỗi biến trong quy tắc với một giá trị cụ thể
(IRI, literal, blank node). Cầu nối giữa quy tắc trừu tượng và dữ liệu đồ thị: $\theta(\text{body})$
là phần thân đã ground, $\theta(\text{head})$ là kết luận đã ground.

**Supersession at Scale (Thay thế ở quy mô).** Thay claim cũ bằng claim mới cùng chuỗi supersede được ghi; chuỗi thay thế cho phép truy vết lịch sử niềm tin. Ở quy mô lớn cần chính sách hàng loạt (Chương 10).

**SWRL (Semantic Web Rule Language).** Mở rộng OWL bằng quy tắc Horn-clause. W3C Member
Submission (2004), KHÔNG phải Recommendation. Kết hợp OWL DL + SWRL nói chung không quyết
định được (undecidable).

**Symbolic graph retrieval (Truy xuất đồ thị tượng trưng).** Truy vấn chính xác (SPARQL) khi lược đồ, thực thể, quan hệ đã biết. Chính xác theo nghĩa khớp mẫu; không xử lý paraphrase chưa có mapping; phản ánh đồ thị, không phản ánh thế giới (Chương 9).

**System Clock (Đồng hồ hệ thống).** Thời điểm sự kiện được ghi vào hệ thống (transaction time). Khác Valid Clock (thế giới) và Assessment Clock (đánh giá); không trộn lẫn (Chương 10).

**System Health Report (Báo cáo sức khỏe hệ thống).** Báo cáo định kỳ về mức + xu hướng của các số liệu so với ngưỡng chính sách; là kết quả của Vòng giám sát (Chương 10).

**System State (Trạng thái hệ thống).** Ảnh chụp có thể truy vết của hệ tại thời điểm T: trạng thái claim, phiên bản index/ontology, hàng đợi. Trạng thái thay đổi theo thời gian; phải gắn đồng hồ (Chương 10).

**Taxonomy (Phân loại).** Hệ thống phân cấp các khái niệm dựa trên quan hệ cha-con
(subclass/superclass). Ontology thường chứa cấu trúc phân cấp subclass và có thể mở rộng bằng
các tiên đề ngữ nghĩa bổ sung. Taxonomy có thể tồn tại độc lập như sản phẩm phân loại.

**Temporal leakage (Rò rỉ thời gian).** Dữ liệu tương lai ở train, dữ liệu quá khứ ở test — mô hình 'dự đoán' quá khứ dựa trên tương lai. Biện pháp: chia tách theo thời gian.

**Temporal retrieval (Truy xuất thời gian).** Truy xuất theo nhiều đồng hồ độc lập: valid time, publication/assertion time, transaction/system time. 'Năm 2020' có nghĩa khác nhau theo từng đồng hồ; không trộn lẫn (Chương 9).

**Threshold as Policy (Ngưỡng là chính sách).** Ngưỡng là quyết định quản trị về mức chấp nhận rủi ro, không phải chân lý tuyệt đối; được đặt, đo, và điều chỉnh có quản trị (Chương 10).

**Threshold ≠ Truth (Ngưỡng ≠ Chân lý).** Vượt ngưỡng kích hoạt chú ý, không kết luận claim đúng/sai; dưới ngưỡng không có nghĩa ổn (Chương 10).

**top_k (Giới hạn kết quả).** Ngưỡng cắt danh sách xếp hạng truy xuất. Là ranh giới tri thức luận: mô hình không suy luận trên bằng chứng ngoài top_k; 'không trong top_k' ≠ không liên quan/không tồn tại (Chương 9).

**Train/validation/test split (Chia tách dữ liệu huấn luyện/xác nhận/kiểm tra).** Phân hoạch tập dữ liệu thành ba phần: train (học tham số), validation (chọn siêu tham số), test (đánh giá cuối). Trên đồ thị, cần tránh rò rỉ.

**Training provenance (Provenance huấn luyện).** Hoạt động huấn luyện sinh ra dự đoán, ghi: phiên bản dữ liệu, phiên bản mô hình, lược đồ đặc trưng, cấu hình. Provenance ≠ bằng chứng.

**Transductive learning (Học chuyển dẫn).** Mô hình học vector cho thực thể đã biết, chỉ dự đoán giữa chúng. Không tổng quát tới thực thể mới. KGE chuẩn là chuyển dẫn.

**TransE.** Mô hình KGE: h + r ≈ t, mỗi quan hệ là phép tịnh tiến. Hàm chấm điểm f(h,r,t) = −‖h + r − t‖. Yếu với quan hệ 1–N, N–1, đối xứng.

**Triple (Bộ ba).** Đơn vị cơ bản của biểu diễn tri thức dạng đồ thị: (subject, predicate,
object).

**Trust ≠ Blind Trust (Tin cậy ≠ Đức tin).** Tin cậy dựa trên bằng chứng và kiểm toán; đức tin là chấp nhận không điều kiện. Hệ thống tự tin không miễn kiểm tra (Chương 10).

**Trustworthiness (Độ đáng tin).** Độ tin cậy của provenance và governance khiến claim truy ra nguồn đăng ký, chuỗi bằng chứng lành, và quá trình đánh giá có kiểm toán. Đáng tin ≠ đúng (Chương 10).

**Turtle.** Một cú pháp văn bản phổ biến để viết RDF. Turtle là cú pháp, không phải bản thân
mô hình RDF.

**Unique name assumption (Giả định tên duy nhất).** Giả định rằng các tên khác nhau luôn chỉ
các thực thể khác nhau. OWL không có giả định này: khác tên không ngụ ý khác thực thể; muốn
khẳng định khác nhau phải dùng owl:differentFrom.

**Universal Restriction (Hạn chế phổ quát).** ∀R.C — lớp các cá thể mà mọi R-liên kết đều dẫn
đến phần tử thuộc C. Không khẳng định sự tồn tại của R-liên kết; nếu không có liên kết nào
thì điều kiện được thỏa mãn một cách trống rỗng (vacuously true).

**Unknown vs Not Found (Không biết vs Không tìm thấy).** Chuỗi phân biệt: không truy xuất được ≠ không có trong index ≠ không có trong KG ≠ đã biết sai ≠ chưa biết. Lỗi truy xuất ≠ thiếu tri thức (Chương 9).

**User Correction (Sửa của người dùng).** Phản hồi của người dùng chỉ ra lỗi hoặc bổ sung; được xử lý như candidate có nguồn là người dùng, không tự động thành tri thức (Chương 10).

**Valid Clock (Đồng hồ Valid).** Thời điểm sự kiện đúng trong thế giới (valid time). Ba đồng hồ Valid/System/Assessment độc lập; câu hỏi 'hệ thống từng tin gì' dùng đồng hồ nào phải nói rõ (Chương 10).

**Validation (Xác nhận).** Kiểm tra dữ liệu có tuân thủ các ràng buộc đã định hay không.
SHACL là ngôn ngữ chuẩn cho RDF validation (§5.6). Khác với entailment: validation kiểm
tra thông tin hiện có, entailment suy ra tri thức mới. Conformance ≠ truth; violation ≠ repair.
Consistency ≠ validation — hai trục độc lập (§5.9).

**Validation Report (Báo cáo xác nhận).** Kết quả SHACL validation: sh:conforms (true/false)
và danh sách sh:ValidationResult. Mỗi result gồm focusNode, resultPath, sourceShape,
sourceConstraintComponent, severity, message, và value (khi applicable). Vi phạm chỉ ra sự
không phù hợp, không chỉ ra cách sửa.

**Value Node (Nút giá trị).** Trong SHACL: nút reachable từ focus node qua property path.
Với node shape, value nodes = {focus node}. Với property shape, value nodes là các đích của
path từ focus node. Constraint được đánh giá trên tập value nodes.
