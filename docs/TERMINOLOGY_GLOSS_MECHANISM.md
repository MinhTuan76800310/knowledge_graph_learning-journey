# Terminology Gloss Mechanism — Knowledge Graph Book

> Mục tiêu: đảm bảo mọi thuật ngữ / chữ viết tắt xuất hiện lần đầu trong sách đều được **giải thích ngay tại chỗ**, trước khi được trình bày đầy đủ ở chương sau. Cơ chế dưới đây kết hợp các quy tắc viết kỹ thuật phổ biến với nhu cầu cụ thể của cuốn sách.

---

## 1. Nguyên tắc nền tảng (từ các style guide kỹ thuật)

- **Spell out on first reference**: Lần đầu xuất hiện một chữ viết tắt, viết đầy đủ dạng mở rộng rồi để chữ viết tắt trong ngoặc.
- **Italicize both term and abbreviation on first use** (Google Developers Style Guide).
- **Define unfamiliar terms inline**: Không để đọc giả phải lật cuối sách hoặc đoán nghĩa.
- **Avoid unexplained forward references**: Nếu buộc phải nhắc đến khái niệm trước khi giải thích đầy đủ, phải có **preview gloss**.

*Nguồn tham khảo:* [Google Developers Style Guide – Abbreviations](https://developers.google.com/style/abbreviations).

---

## 2. Cơ chế 3 tầng cho cuốn sách

### Tầng 1 — Inline gloss (bắt buộc cho mọi thuật ngữ)

Mỗi thuật ngữ kỹ thuật xuất hiện lần đầu trong một chương phải kèm theo một trong hai dạng:

#### Dạng A: Thuật ngữ Anh có nghĩa Việt ngắn

```markdown
thực thể (entity) — một đối tượng trong thế giới thực hoặc miền vấn đề.
```

> Ví dụ: “**Entity (thực thể).** Một đối tượng trong thế giới thực hoặc miền vấn đề, được biểu diễn bằng một nút trong đồ thị.”

#### Dạng B: Chữ viết tắt được mở rộng đầy đủ

```markdown
RDF (Resource Description Framework — khung mô tả tài nguyên)
```

> Ví dụ: “**RDF (Resource Description Framework — khung mô tả tài nguyên, mô hình dữ liệu đồ thị bộ ba chuẩn của W3C).**”

**Quy tắc chi tiết:**

- Chỉ cần gloss **lần đầu tiên trong toàn bộ sách**, trừ khi chương sau dùng lại với ý nghĩa khác.
- Gloss phải ngắn gọn (một dòng), không cần giải thích đầy đủ chương học.
- Nếu thuật ngữ sẽ được học chi tiết ở chương sau, thêm cụm “sẽ học ở Chương X”.

---

### Tầng 2 — Preview box cho “họ thuật ngữ” xuất hiện sớm

Khi một nhóm thuật ngữ liên quan được nhắc đến trước khi học chi tiết (ví dụ: W3C/RDF/RDFS/OWL/SHACL/SPARQL trong Chương 1), sử dụng một khung preview riêng:

```markdown
> 📦 **Preview — Các thuật ngữ W3C sẽ học chi tiết ở các chương sau**
>
> Dưới đây là bản giới thiệu ngắn để bạn không bị lạc khi gặp chúng trong chương này:
>
> - **W3C** (World Wide Web Consortium): tổ chức phát triển chuẩn web.
> - **RDF** (Resource Description Framework): mô hình dữ liệu đồ thị bộ ba chuẩn.
> - **RDFS** (RDF Schema): tầng lược đồ/lớp của RDF.
> - **OWL** (Web Ontology Language): ngôn ngữ bản thể học.
> - **SHACL** (Shapes Constraint Language): ngôn ngữ ràng buộc dữ liệu RDF.
> - **SPARQL** (Simple Protocol and RDF Query Language): ngôn ngữ truy vấn RDF.
>
> Chi tiết về từng thuật ngữ sẽ có ở Chương 2 (RDF, SPARQL) và Chương 4–5 (RDFS, OWL, SHACL).
```

**Khi nào dùng preview box:**

- Chương hiện tại cần nhắc đến ≥ 3 thuật ngữ thuộc cùng một họ/lĩnh vực.
- Các thuật ngữ đó sẽ chỉ được giải thích đầy đủ ở chương sau.
- Preview box giúp tránh việc mỗi câu văn trong chương bị ngắt bởi nhiều ngoặc giải thích.

---

### Tầng 3 — Chapter-end mini-glossary

Ở cuối mỗi chương, thêm một mục ngắn:

```markdown
## Thuật ngữ đã gặp trong chương này

| Thuật ngữ | Nghĩa ngắn | Học chi tiết |
|-----------|-----------|--------------|
| Entity (thực thể) | Đối tượng trong thế giới thực hoặc miền vấn đề | §1.3 |
| RDF (Resource Description Framework) | Mô hình dữ liệu đồ thị bộ ba chuẩn | Chương 2 |
| IRI (Internationalized Resource Identifier) | Định danh toàn cục dạng chuỗi | Chương 2 |
```

**Tác dụng:**

- Giúp đọc giả ôn tập nhanh.
- Làm “point of truth” để kiểm tra xem inline gloss đã được thêm đủ chưa.

---

## 3. Quy tắc xử lý các trường hợp đặc biệt

### 3.1. Thuật ngữ chỉ nên nhắc đến, chưa giải thích

Nếu một thuật ngữ được nhắc đến nhưng chưa học, phải áp dụng **một trong ba** quy tắc:

1. **Inline gloss ngắn** (một dòng).
2. **Preview box** (nếu là họ thuật ngữ).
3. **Forward reference rõ ràng**: “(sẽ học ở Chương X)” kèm định nghĩa tối thiểu.

**Không được**: chỉ gọi tên thuật ngữ mà không có cả ba thứ trên.

### 3.2. Thuật ngữ đã học ở chương trước

- Không cần gloss lại đầy đủ nếu nghĩa không đổi.
- Có thể thêm liên kết ngắn: “IRI (đã học ở Chương 2)”, nếu cần nhắc lại.

### 3.3. Các từ viết tắt phổ biến

Theo Google Developers Style Guide, các từ viết tắt phổ biến như **API, URL, HTML, REST** có thể không cần mở rộng. Tuy nhiên, với đối tượng là kỹ sư phần mềm Việt Nam, nên mở rộng ít nhất một lần để đảm bảo nhất quán.

---

## 4. Công cụ kiểm tra (đề xuất)

Để đảm bảo cơ chế này được áp dụng nhất quán, có thể dùng các công cụ đơn giản:

1. **Glossary term list**: Danh sách các thuật ngữ cần gloss, lưu trong `docs/GLOSSARY_TERMS.json` hoặc file tương tự.
2. **Pre-commit / CI check**: Một script đơn giản kiểm tra xem các thuật ngữ trong danh sách có xuất hiện lần đầu mà không kèm theo định nghĩa hoặc chưa nằm trong preview box không.
3. **Manual checklist cho mỗi chương mới**: Trước khi đánh dấu chương hoàn thành, duyệt lại tất cả các thuật ngữ mới và đảm bảo đã có inline gloss hoặc preview box.

---

## 5. Ví dụ áp dụng vào Chương 1

### Đoạn gốc (hiện tại)

```markdown
Entity có identity (danh tính) — thường là IRI trong RDF hoặc node ID trong property graph.
```

### Đoạn sửa

```markdown
Entity có identity (danh tính) — thường là **IRI** (Internationalized Resource Identifier — định danh toàn cục dạng chuỗi, sẽ học ở Chương 2) trong **RDF** (Resource Description Framework — mô hình dữ liệu đồ thị bộ ba chuẩn của W3C, sẽ học ở Chương 2) hoặc node ID trong property graph.
```

### Preview box đặt ở §1.3 trước khi đoạn trên xuất hiện

```markdown
> 📦 **Preview — Các thuật ngữ W3C sẽ học chi tiết ở các chương sau**
>
> Chương này cần nhắc đến một số thuật ngữ từ thế giới RDF/ Semantic Web. Đây là bản giới thiệu ngắn:
>
> - **W3C** (World Wide Web Consortium): tổ chức phát triển chuẩn web.
> - **RDF** (Resource Description Framework): mô hình dữ liệu đồ thị bộ ba chuẩn của W3C.
> - **IRI** (Internationalized Resource Identifier): định danh toàn cục dạng chuỗi, dùng trong RDF.
> - **RDFS** (RDF Schema): tầng lược đồ/lớp của RDF.
> - **OWL** (Web Ontology Language): ngôn ngữ bản thể học.
> - **SHACL** (Shapes Constraint Language): ngôn ngữ ràng buộc dữ liệu RDF.
> - **SPARQL** (Simple Protocol and RDF Query Language): ngôn ngữ truy vấn RDF.
>
> Bạn không cần nhớ chi tiết ngay; mỗi thuật ngữ sẽ được giải thích đầy đủ khi đến chương tương ứng.
```

---

## 6. Kết luận

Cơ chế này giúp cuốn sách **vừa giữ được mạch lập luận liền mạch, vừa không bỏ rơi đọc giả ở những thuật ngữ chưa học**. Nó dựa trên quy tắc chuẩn của technical writing và có thể áp dụng tự động hóa bằng script kiểm tra sau này.
