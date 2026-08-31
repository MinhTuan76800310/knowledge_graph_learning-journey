# Lời bạt (Afterword)

## 1. Hành trình mười chương

Mười chương trước đã xây dựng một hệ thống tri thức từ những nguyên lý nền tảng nhất:

- **Chương 1–2** bắt đầu từ đồ thị và ngôn ngữ truy vấn — câu trả lời cho "tri thức được biểu
  diễn và truy xuất thế nào trong máy tính."
- **Chương 3–4** thêm ngữ nghĩa: schema, ontology, bản thể luận — câu trả lời cho "dữ liệu đồ thị
  có ý nghĩa gì, và làm sao máy tính 'hiểu' được nó."
- **Chương 5** thêm suy diễn và xác nhận — câu trả lời cho "tri thức mới được sinh ra và kiểm tra
  thế nào từ tri thức đã có."
- **Chương 6** thêm tầng nhận thức luận: claim, bằng chứng, provenance, thời gian, mâu thuẫn —
  câu trả lời cho "hệ thống biết điều nó biết, và xử lý xung đột ra sao."
- **Chương 7** thêm thu nhận và tích hợp — câu trả lời cho "tri thức từ thế giới bên ngoài vào hệ
  thống thế nào."
- **Chương 8** thêm học từ đồ thị — câu trả lời cho "tri thức mới được phát hiện từ dữ liệu mà
  không cần con người viết tường minh."
- **Chương 9** thêm truy xuất và trả lời câu hỏi — câu trả lời cho "tri thức được phục vụ cho
  người dùng và AI agent thế nào."
- **Chương 10** thêm lớp vận hành: giám sát, đo lường, bảo trì, quản trị, kiểm toán — câu trả lời
  cho "hệ thống tri thức sống và đáng tin theo thời gian thế nào."

Mỗi chương xây trên nền chương trước. Mỗi chương trả lời một câu hỏi trung tâm duy nhất. Mười
chương, một mạch xuyên suốt: từ một triple RDF đến một **Living Knowledge System** tự quan sát,
tự đo, và tự bảo trì dưới quản trị.

Con đường đó không phải là một pipeline tuyến tính — nó là một tập các vòng phản hồi, nơi tri thức
được thu nhận, được kiểm chứng, được truy xuất, được giám sát, và được tái đánh giá. Mỗi vòng cho
thấy một góc của câu trả lời cho câu hỏi mở đầu cuốn sách: *làm sao xây dựng một hệ thống tri thức
đáng tin?*

## 2. Biên giới vẫn mở

Chương 10 đã bàn giao năm vấn đề mở. Ở đây chúng tôi đặt chúng trong bối cảnh rộng hơn.

**Quyền hạn (authority).** Ai — hoặc cái gì — phê duyệt một hành động bảo trì tự động? Khi hệ
thống tự phát hiện một claim cũ và tự đề xuất tái đánh giá, quyết định cuối cùng thuộc về con
người, một thuật toán, hay một chính sách có thể kiểm toán? Đây là bài toán về delegation và
accountability trong một hệ thống không ngừng tiến hóa. Nó không có đáp án một chiều; nó phụ
thuộc vào rủi ro, bối cảnh, và văn hóa tổ chức.

**Giám sát con người ở quy mô (human oversight at scale).** Khi một hệ thống tri thức chứa hàng
triệu claim và xử lý hàng ngàn câu hỏi mỗi ngày, một người đánh giá không thể đọc từng claim.
Mẫu ngẫu nhiên, cảnh báo leo thang, và dashboard là những công cụ — nhưng chúng không thay thế
được phán xét của con người. Làm sao thiết kế một giao diện giám sát cho phép con người phát
hiện sai lệch hệ thống mà không bị quá tải thông tin? Đây là một bài toán HCI (Human-Computer
Interaction) chưa có lời giải tổng quát.

**Chi phí (cost).** Giám sát, đo lường, và bảo trì có chi phí: thời gian tính toán, không gian
lưu trữ vết kiểm toán, băng thông con người cho đánh giá. Một hệ thống đo mọi thứ sẽ không đủ
khả năng vận hành. Cái gì quyết định ngưỡng đầu tư cho observability? Câu trả lời không nằm trong
lý thuyết tri thức — nó nằm trong kinh tế học vận hành.

**Đa hệ thống (multi-system / multi-agent).** Khi nhiều hệ thống tri thức — hoặc nhiều AI agent —
chia sẻ một phần tri thức và hành động dựa trên nó, quản trị trở thành một bài toán phân tán.
Ai sở hữu một claim khi nó được ba hệ thống khác nhau thu nhận và tái đánh giá? Mâu thuẫn giữa
các hệ thống được phân xử ra sao? Mô hình Living Knowledge System của Chương 10 là đơn hệ thống;
mở rộng nó lên đa tác tử là một hướng nghiên cứu đang hoạt động.

**Paradigm shift.** Cuốn sách này giả định bản thể luận và schema tương đối ổn định. Nhưng lịch
sử AI cho thấy các paradigm shift xảy ra: từ symbolic sang statistical, từ KG thuần túy sang
neural-symbolic, từ mô hình cố định sang mô hình ngôn ngữ lớn. Một hệ thống tri thức sống phải
xử lý được — hoặc ít nhất phát hiện được — một sự thay đổi làm schema hiện tại vô hiệu. Đây có
thể là bài toán khó nhất trong số các bài toán mở.

Một vấn đề thứ sáu, xuyên suốt cả năm vấn đề trên, là **lòng tin xã hội (societal trust).** Một
hệ thống tri thức không bao giờ "xong" — nhưng xã hội có chấp nhận một hệ thống mà trạng thái
tri thức của nó luôn thay đổi? Làm sao một tổ chức giải thích với kiểm toán viên rằng "hệ thống
của chúng tôi đáng tin vì nó được đo, được bảo trì, và được kiểm toán trong khi chạy — không
phải vì nó đã hoàn thành"? Câu trả lời cho câu hỏi này vượt ra ngoài kỹ thuật; nó đụng đến
văn hóa tổ chức, quy định pháp lý, và niềm tin của công chúng.

## 3. Không bao giờ xong

Cuốn sách này đã đi một hành trình dài từ triple RDF đến vòng giám sát. Nhưng điểm đến không phải
là một hệ thống "hoàn thiện" — nó là một hệ thống có thể tiếp tục thay đổi mà không mất kiểm soát.

Câu trả lời của cuốn sách cho câu hỏi "làm sao xây dựng một hệ thống tri thức đáng tin?" là:

> Một hệ thống tri thức đáng tin không phải vì nó đã hoàn thành, mà vì nó **quan sát được, đo
> được, quản trị được, và kiểm toán được trong khi chạy.**

Đây không phải là một tuyên bố triết học — nó là một thiết kế kỹ thuật. Mười chương của cuốn sách
là bản thiết kế của thiết kế đó. Mỗi lớp — từ biểu diễn đồ thị đến vòng phản hồi an toàn — đều
cần thiết. Không lớp nào đủ một mình.

## 4. Con đường phía trước

Nếu bạn muốn đi sâu hơn sau khi đọc cuốn sách này:

- **Các chuẩn W3C và ISO** được trích dẫn xuyên suốt — RDF, SPARQL, OWL, SHACL, PROV-O,
  ISO 8000 — là tài liệu tham khảo chính thống cho các cơ chế được dạy trong sách.
- **Các tài liệu học thuật** trong `book/references.bib` và `docs/source_index.json` là nơi
  bắt đầu cho nghiên cứu sâu hơn về từng chủ đề.
- **Các experiment bị hoãn** (xem `docs/LAB_BACKLOG.md`) — EXP-10-1 đến EXP-10-9 và các bài tập
  thiết kế từ Chương 2–9 — là cơ hội để bạn xây tay trên nền kiến thức của sách.
- **Cộng đồng Knowledge Graph** — các hội nghị (ISWC, ESWC, K-CAP), nhóm W3C, và các dự án mã
  nguồn mở (Apache Jena, RDFLib, Neo4j, Ontotext) — là nơi những vấn đề mở của cuốn sách đang
  được giải quyết từng ngày.

## 5. Lời kết

Cuốn sách này bắt đầu bằng một câu hỏi: "Làm sao xây dựng một hệ thống tri thức đáng tin?"

Nó kết thúc bằng một câu trả lời: không phải bằng cách xây một hệ thống hoàn hảo ngay từ đầu, mà
bằng cách xây một hệ thống có thể — và sẽ — thay đổi, nhưng luôn giữ được khả năng quan sát, đo
lường, quản trị, và kiểm toán.

Hệ thống tri thức sống không phải là một sản phẩm. Nó là một tiến trình. Và tiến trình đó không
bao giờ kết thúc.

Cảm ơn bạn đã đọc đến dòng cuối cùng.

— *Những người viết*