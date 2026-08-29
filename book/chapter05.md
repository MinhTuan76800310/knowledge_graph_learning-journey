# Chương 5 — Suy diễn, Quy tắc và Xác nhận

> **Định hướng chương**
>
> **Câu hỏi trung tâm:** Khi đã có ontology với ngữ nghĩa hình thức, làm thế nào để *tính
> toán* các hệ quả logic từ dữ liệu? Và làm thế nào để *kiểm tra* dữ liệu có tuân thủ các
> ràng buộc đã định nghĩa? Hai câu hỏi này nghe tương tự nhưng thuộc về hai pipeline hoàn
> toàn khác nhau.
>
> **Vì sao quan trọng:** Chương 4 đã dạy cách định nghĩa ý nghĩa hình thức cho ký hiệu.
> Nhưng định nghĩa thôi chưa đủ — chúng ta cần cơ chế tính toán để (1) suy ra tri thức mới
> từ tri thức hiện có, và (2) xác nhận dữ liệu có phù hợp với các ràng buộc. Nhầm lẫn hai
> pipeline này là nguồn gốc của nhiều lỗi thiết kế hệ thống tri thức.
>
> **Bạn sẽ hiểu:**
>
> - Sự phân biệt cốt lõi: suy diễn (inference) vs xác nhận (validation)
> - Cơ chế forward chaining và bao đóng (closure) dưới quy tắc RDFS
> - Vật chất hóa (materialization) như chiến lược triển khai, không phải bản thân suy diễn
> - SHACL shapes và validation report — ràng buộc dữ liệu, không phải tiên đề suy diễn
> - Tính đúng đắn (soundness) và đầy đủ (completeness) trong ngữ cảnh cụ thể
> - Giới hạn của OWL RL và quy tắc Horn đối với OWL 2 DL đầy đủ
>
> **Tiên quyết:** Chương 1–4. Đặc biệt: RDFS domain/range như quy tắc suy diễn (§3.1),
> diễn giải → mô hình → suy diễn (§4.3), điều kiện cần/đủ (§4.5), OWL Profiles (§4.12).
>
> **Bản đồ khái niệm:**
>
> Inference ≠ Validation → Forward chaining fixpoint → RDFS rules thêm thông tin →
> Materialization = chiến lược triển khai → SHACL shapes kiểm tra dữ liệu →
> Validation report ≠ repair → Soundness + Completeness phụ thuộc regime →
> OWL RL giới hạn → SWRL mở rộng nhưng không quyết định được

## 5.1 Mở đầu: Hai câu hỏi, hai pipeline

Chương 4 đã trả lời câu hỏi "ký hiệu nghĩa là gì?" bằng cơ chế diễn giải → mô hình → suy
diễn. Bây giờ chúng ta đối mặt với hai câu hỏi thực hành:

1. **Từ những gì đã biết, điều gì *suy ra được*?** (What follows?)
2. **Dữ liệu hiện có *tuân thủ* các ràng buộc đã định nghĩa không?** (Does data conform?)

Hai câu hỏi này trông tương tự vì cả hai đều liên quan đến mối quan hệ giữa dữ liệu và
các quy tắc/ngữ nghĩa. Nhưng chúng thuộc về hai pipeline hoàn toàn khác nhau:

| | Pipeline Suy diễn (Inference) | Pipeline Xác nhận (Validation) |
|---|---|---|
| **Câu hỏi** | Điều gì suy ra được? | Dữ liệu có tuân thủ không? |
| **Đầu vào** | Đồ thị + ngữ nghĩa (entailment regime) | Dữ liệu + shapes/ràng buộc |
| **Đầu ra** | Tri thức mới (entailments) | Báo cáo phù hợp/vi phạm |
| **Hướng** | Thêm thông tin | Kiểm tra thông tin |
| **Ví dụ** | RDFS domain suy ra rdf:type | SHACL sh:class kiểm tra rdf:type |

Sự nhầm lẫn phổ biến nhất trong thực tế là dùng công cụ của pipeline này cho mục đích của
pipeline kia — ví dụ, dùng rdfs:domain để "kiểm tra" dữ liệu (nó không kiểm tra, nó chỉ suy
ra), hoặc dùng SHACL shape để "suy diễn" tri thức mới (nó không suy diễn, nó chỉ xác nhận).

> 🖊 **Tự kiểm tra:** Trước khi đọc tiếp, hãy thử giải thích bằng lời của bạn: nếu một
> property P có `rdfs:domain C`, và bạn thấy triple `(x, P, y)` trong dữ liệu mà x chưa
> được khai báo là kiểu C, thì (a) pipeline suy diễn sẽ làm gì? (b) pipeline xác nhận sẽ
> làm gì? Câu trả lời khác nhau như thế nào?

## 5.2 Forward Chaining: Cơ chế suy diễn cơ bản

### Trực giác

Hãy tưởng tượng bạn có một tập các quy tắc "nếu... thì..." và một đồ thị dữ liệu ban đầu.
Bạn áp dụng tất cả quy tắc lên đồ thị, thêm các kết quả mới vào đồ thị, rồi lại áp dụng
quy tắc lên đồ thị đã mở rộng. Bạn lặp lại quá trình này cho đến khi không còn kết quả mới
nào được sinh ra. Đồ thị cuối cùng chứa tất cả những gì có thể suy ra được từ dữ liệu ban
đầu theo tập quy tắc đã chọn.

Đó chính là **forward chaining** (suy diễn tiến) — cơ chế suy diễn cơ bản nhất trong hệ
thống tri thức.

### Cơ chế hình thức

Cho tập quy tắc $R$ và đồ thị ban đầu $G_0$, forward chaining tính toán dãy:

$$G_{i+1} = G_i \cup \{ \text{head}(r) \mid r \in R, \; \text{body}(r) \subseteq G_i \}$$

Nói bằng lời: ở mỗi bước, áp dụng mọi quy tắc $r$ mà phần thân (body) khớp với đồ thị hiện
tại $G_i$, thêm phần đầu (head) của các quy tắc đó vào đồ thị.

Thuật toán dừng khi đạt **điểm bất động** (fixpoint):

$$G_{n+1} = G_n$$

Khi không còn triple mới nào được sinh ra, đồ thị $G_n$ được gọi là **bao đóng** (closure)
của $G_0$ dưới tập quy tắc $R$.

### Ví dụ cụ thể: RDFS subClassOf

Xét đồ thị ban đầu:

```
Hanoi    rdf:type     CapitalCity
CapitalCity  rdfs:subClassOf  City
City     rdfs:subClassOf  Settlement
```

Quy tắc RDFS subClassOf: nếu `A rdfs:subClassOf B` và `x rdf:type A`, thì suy ra
`x rdf:type B`.

**Bước 1 ($G_0 \to G_1$):** Áp dụng quy tắc với `CapitalCity ⊑ City`:
- Body khớp: `Hanoi rdf:type CapitalCity` và `CapitalCity rdfs:subClassOf City`
- Head: `Hanoi rdf:type City` → thêm vào $G_1$

**Bước 2 ($G_1 \to G_2$):** Áp dụng quy tắc với `City ⊑ Settlement`:
- Body khớp: `Hanoi rdf:type City` (mới từ bước 1) và `City rdfs:subClassOf Settlement`
- Head: `Hanoi rdf:type Settlement` → thêm vào $G_2$

**Bước 3 ($G_2 \to G_3$):** Không còn quy tắc nào sinh triple mới. $G_3 = G_2$. Điểm bất
động đạt được.

Kết quả: từ 3 triple ban đầu, forward chaining với quy tắc subClassOf đã suy ra 2 triple
mới: `Hanoi rdf:type City` và `Hanoi rdf:type Settlement`.

### Điều kiện dừng

Forward chaining đảm bảo dừng khi tập quy tắc là **đơn điệu** (monotonic): áp dụng quy tắc
chỉ thêm triple, không bao giờ xóa. Với đồ thị hữu hạn và tập quy tắc đơn điệu hữu hạn, số
triple có thể sinh ra là hữu hạn, nên thuật toán luôn đạt điểm bất động.

Nếu quy tắc có phủ định (negation) trong phần thân, tính đơn điệu bị phá vỡ và thuật toán
có thể không dừng. Đây là lý do tại sao các ngôn ngữ quy tắc an toàn cho KG (như RDFS
entailment rules, OWL RL rules) hạn chế hoặc cấm phủ định.

> ⚠ **Lưu ý quan trọng:** Forward chaining là một *thuật toán*, không phải một *định nghĩa
> ngữ nghĩa*. Nó tính toán hệ quả dựa trên tập quy tắc cụ thể. Tập quy tắc khác nhau cho
> kết quả khác nhau từ cùng đồ thị ban đầu. Khi nói "suy diễn", luôn phải ghi rõ: suy diễn
> theo *chế độ nào* (entailment regime)?

## 5.3 RDFS Entailment Rules: Suy diễn thêm thông tin

RDF Schema (RDFS) định nghĩa một tập quy tắc suy diễn chuẩn [@w3c-rdf-schema]. Bốn quy
tắc quan trọng nhất:

### rdfs:subClassOf

Nếu `A rdfs:subClassOf B` và `x rdf:type A`, thì suy ra `x rdf:type B`.

Đây là quy tắc truyền loại theo phân cấp lớp. Như ví dụ §5.2 đã minh họa.

### rdfs:subPropertyOf

Nếu `P rdfs:subPropertyOf Q` và `x P y`, thì suy ra `x Q y`.

Quy tắc này cho phép xây dựng phân cấp thuộc tính. Ví dụ: nếu `capitalOf rdfs:subPropertyOf locatedIn`, thì mọi cặp `(city, capitalOf, country)` cũng suy ra `(city, locatedIn, country)`.

### rdfs:domain

Nếu `P rdfs:domain C` và `x P y`, thì suy ra `x rdf:type C`.

### rdfs:range

Nếu `P rdfs:range C` và `x P y`, thì suy ra `y rdf:type C`.

### Domain/Range là quy tắc suy diễn, KHÔNG phải ràng buộc xác nhận

Đây là điểm then chốt đã được nhấn mạnh ở Chương 2 và Chương 4, và cần nhắc lại ở đây vì
nó là nguồn nhầm lẫn phổ biến nhất:

> ⚠ **rdfs:domain và rdfs:range THÊM thông tin vào đồ thị.** Chúng KHÔNG kiểm tra, KHÔNG
> từ chối, và KHÔNG gây lỗi khi dữ liệu "không khớp." Nếu property `locatedIn` có
> `rdfs:domain City`, và bạn thấy triple `(UnknownEntity, locatedIn, SomePlace)` trong dữ
> liệu, RDFS *không* báo lỗi — nó suy ra `UnknownEntity rdf:type City`. Triple gốc vẫn
> tồn tại và hợp lệ.

Việc kiểm tra xem dữ liệu có "khớp" với kỳ vọng hay không là nhiệm vụ của SHACL (§5.5),
không phải RDFS.

### Bao đóng RDFS

Áp dụng forward chaining với toàn bộ tập quy tắc RDFS lên đồ thị $G$ cho kết quả là **bao
đóng RDFS** (RDFS closure) của $G$, ký hiệu $\text{cl}_{\text{RDFS}}(G)$. Bao đóng này chứa
tất cả các triple có thể suy ra được từ $G$ theo ngữ nghĩa RDFS [@w3c-rdf-schema].

> 🖊 **Tự kiểm tra:** Cho đồ thị gồm: `(Hanoi, capitalOf, Vietnam)`, `(capitalOf, rdfs:domain, City)`, `(capitalOf, rdfs:range, Country)`. Hãy liệt kê tất cả các triple được suy ra bởi forward chaining với quy tắc RDFS domain và range. Giải thích từng bước.

## 5.4 Vật chất hóa: Chiến lược triển khai, không phải bản thân suy diễn

### Phân biệt cốt lõi

Ở §4.3, chúng ta đã học rằng **suy diễn (entailment) là một quan hệ ngữ nghĩa**: $O \models
\alpha$ nghĩa là $\alpha$ đúng trong mọi mô hình của $O$. Quan hệ này tồn tại độc lập với
bất kỳ hệ thống tính toán nào.

**Vật chất hóa (materialization)** là một *chiến lược triển khai*: tính toán trước bao đóng
và lưu trữ kết quả vào đồ thị. Đây là một cách để *hiện thực hóa* suy diễn, không phải bản
thân khái niệm suy diễn.

```
Suy diễn (entailment)     = quan hệ ngữ nghĩa (abstract)
Vật chất hóa              = chiến lược tính toán (implementation)
Forward chaining          = thuật toán cụ thể (algorithm)
```

Ba khái niệm này liên quan nhưng không đồng nhất:

- Một hệ thống có thể trả lời truy vấn suy diễn mà *không* vật chất hóa (query rewriting, backward chaining).
- Vật chất hóa có thể dùng forward chaining hoặc các thuật toán khác.
- Bản thân quan hệ entailment không thay đổi đồ thị — chỉ hệ thống triển khai mới thay đổi đồ thị.

### Khi nào vật chất hóa khả thi?

Vật chất hóa hoạt động tốt khi:

- Tập quy tắc đơn điệu và hữu hạn (RDFS, OWL RL subset)
- Đồ thị không quá lớn
- Truy vấn lặp lại nhiều lần (chi phí tính toán một lần, truy vấn nhanh sau đó)

Vật chất hóa trở nên không khả thi khi:

- Ontology quá biểu cảm (OWL 2 DL đầy đủ có thể sinh vô hạn triple)
- Đồ thị rất lớn (bao đóng có thể lớn hơn nhiều so với đồ thị gốc)
- Dữ liệu thay đổi thường xuyên (phải tính lại bao đóng mỗi lần cập nhật)

> ⚠ **Ngộ nhận thường gặp:** "Bộ suy diễn (reasoner) vật chất hóa tất cả hệ quả." Sai.
> Nhiều reasoner dùng chiến lược lazy (tính theo yêu cầu) hoặc query rewriting. Vật chất
> hóa chỉ là một lựa chọn triển khai.

## 5.5 SHACL: Xác nhận dữ liệu bằng Shapes

### Trực giác

Nếu RDFS/OWL trả lời "điều gì suy ra được?", thì SHACL (Shapes Constraint Language) trả
lời "dữ liệu có tuân thủ không?" [@w3c-shacl].

SHACL định nghĩa một ngôn ngữ để mô tả các **shapes** — điều kiện kiểm tra trên nút dữ
liệu. Mỗi shape nhắm đến một tập nút (target) và định nghĩa các ràng buộc (constraints) mà
nút đó phải thỏa mãn. Kết quả xác nhận là một **báo cáo** (validation report), không phải
tri thức mới.

### Shape là gì?

Một **shape** trong SHACL là một tài nguyên RDF mô tả điều kiện kiểm tra. Shape không
phải là tiên đề ontology — nó không tham gia vào suy diễn RDFS/OWL. Shape chỉ được dùng
bởi engine xác nhận SHACL.

Ví dụ: shape yêu cầu mọi `City` phải có ít nhất một `rdfs:label`:

```turtle
:CityShape
    a sh:NodeShape ;
    sh:targetClass :City ;
    sh:property [
        sh:path rdfs:label ;
        sh:minCount 1 ;
        sh:message "Mỗi City phải có ít nhất một nhãn" ;
    ] .
```

Shape này:
- **Nhắm đến** (`sh:targetClass`) tất cả nút có `rdf:type :City`
- **Kiểm tra** rằng mỗi nút đó có ít nhất 1 giá trị cho `rdfs:label`
- **Không suy diễn** gì cả — nó chỉ kiểm tra dữ liệu hiện có

### Các loại ràng buộc SHACL

SHACL cung cấp nhiều loại ràng buộc [@w3c-shacl]:

| Loại | Ví dụ | Ý nghĩa |
|------|-------|---------|
| Kiểu giá trị | `sh:datatype xsd:string` | Giá trị phải có kiểu chỉ định |
| Lớp | `sh:class :City` | Giá trị phải là instance của lớp |
| Số lượng | `sh:minCount 1`, `sh:maxCount 5` | Số lượng giá trị trong phạm vi |
| Mẫu | `sh:pattern "^VN"` | Giá trị chuỗi khớp regex |
| Phạm vi | `sh:minInclusive 0` | Giá trị số ≥ ngưỡng |
| Đóng | `sh:closed true` | Không cho phép property ngoài danh sách |

### Validation Report: Kết quả xác nhận

Khi chạy SHACL validation, engine sản xuất một **validation report** [@w3c-shacl]:

- `sh:conforms true` — dữ liệu phù hợp, không có vi phạm
- `sh:conforms false` — dữ liệu không phù hợp, kèm danh sách `sh:ValidationResult`

Mỗi `sh:ValidationResult` chứa:
- `sh:focusNode` — nút bị vi phạm
- `sh:resultPath` — property path dẫn đến vi phạm
- `sh:sourceConstraintComponent` — loại ràng buộc bị vi phạm
- `sh:resultSeverity` — mức độ (Violation, Warning, Info)
- `sh:resultMessage` — thông báo mô tả vi phạm

> ⚠ **Vi phạm ≠ Sửa chữa.** Báo cáo SHACL chỉ ra *điều gì không phù hợp*, không chỉ ra
> *cách sửa*. Có thể có nhiều cách sửa cho một vi phạm, hoặc không có cách sửa hợp lệ trong
> khuôn khổ schema hiện tại. Việc sửa chữa dữ liệu là trách nhiệm của ứng dụng, không phải
> của SHACL.

> 🖊 **Tự kiểm tra:** Cho shape yêu cầu `City` có đúng 1 `capitalOf` với range là `Country`.
> Nếu dữ liệu có `(Hanoi, capitalOf, Vietnam)` và `(Hanoi, capitalOf, France)`, báo cáo
> SHACL sẽ nói gì? Nếu dữ liệu có `(Hanoi, capitalOf, "not-a-country")`, báo cáo sẽ nói
> gì? Hai trường hợp khác nhau như thế nào?

## 5.6 Phù hợp ≠ Đúng: Ranh giới của xác nhận

### Conformance không phải là Truth

Một đồ thị **phù hợp** (conforms) với shapes SHACL nghĩa là dữ liệu thỏa mãn các điều kiện
đã định nghĩa. Điều này KHÔNG có nghĩa:

- Dữ liệu đúng với thực tế
- Dữ liệu đầy đủ
- Dữ liệu nhất quán về mặt logic
- Dữ liệu đáng tin cậy

Một đồ thị có thể phù hợp hoàn toàn với shapes mà vẫn chứa thông tin sai. Ngược lại, một
đồ thị có thể vi phạm shapes mà vẫn chứa thông tin đúng — chỉ là thông tin đó không khớp
với cấu trúc kỳ vọng.

```
Phù hợp (conformance)   = dữ liệu khớp shapes      ≠ dữ liệu đúng
Vi phạm (violation)     = dữ liệu không khớp shapes ≠ dữ liệu sai
```

### Tại sao phân biệt này quan trọng?

Trong thực tế xây dựng hệ thống tri thức:

1. **Validation gate:** Dùng SHACL để lọc dữ liệu đầu vào — dữ liệu vi phạm bị từ chối hoặc
   gắn cờ. Nhưng dữ liệu qua gate chưa chắc đúng.
2. **Quality signal:** Vi phạm SHACL là tín hiệu về chất lượng cấu trúc, không phải về tính
   đúng đắn nội dung.
3. **Evolution:** Khi schema thay đổi, dữ liệu cũ có thể vi phạm shapes mới mà vẫn đúng về
   mặt nội dung.

## 5.7 Shapes ≠ Axioms: Phân biệt SHACL và Ontology

Sự phân biệt giữa SHACL và ontology là một trong những ranh giới quan trọng nhất trong
thiết kế hệ thống tri thức:

| | Ontology (RDFS/OWL) | SHACL Shapes |
|---|---|---|
| **Mục đích** | Định nghĩa điều gì suy ra được | Định nghĩa điều gì được phép |
| **Hướng** | Thêm thông tin (open-world) | Kiểm tra thông tin (closed-world trên target set) |
| **Kết quả** | Entailments (triple mới) | Validation report (conforms/violation) |
| **Tham gia suy diễn** | Có | Không |
| **Ví dụ** | `rdfs:domain` suy ra rdf:type | `sh:class` kiểm tra rdf:type |

Cùng từ vựng (`class`, `property`, `datatype`), nhưng ngược hướng:

- `P rdfs:domain C` + `(x, P, y)` → suy ra `x rdf:type C` (thêm thông tin)
- `sh:property [ sh:path P ; sh:class C ]` + `(x, P, y)` → kiểm tra `y rdf:type C` có đúng không (kiểm tra thông tin)

> ⚠ **Không thay thế lẫn nhau.** Ontology không thay thế được SHACL cho việc kiểm tra dữ
> liệu. SHACL không thay thế được ontology cho việc suy diễn tri thức. Hệ thống tri thức
> hoàn chỉnh thường cần cả hai.

## 5.8 Tính đúng đắn và Tính đầy đủ

Khi đánh giá một hệ thống suy diễn, hai tính chất quan trọng nhất là **soundness** (tính
đúng đắn) và **completeness** (tính đầy đủ). Nhưng cả hai đều vô nghĩa nếu không ghi rõ
phạm vi.

### Định nghĩa

Cho chế độ suy diễn (entailment regime) $\Phi$ và thủ tục suy diễn $P$:

**Soundness:** Mọi kết quả $P$ sinh ra đều là hệ quả logic thực sự.

$$\text{Nếu } P \text{ derives } \alpha \text{ from } G, \text{ thì } G \models_\Phi \alpha$$

Không có dương tính giả (false positive).

**Completeness:** Mọi hệ quả logic thực sự đều được $P$ sinh ra.

$$\text{Nếu } G \models_\Phi \alpha, \text{ thì } P \text{ derives } \alpha \text{ from } G$$

Không có âm tính giả (false negative).

### Ba thành phần bắt buộc

Mọi khẳng định về soundness/completeness PHẢI ghi rõ ba thành phần:

1. **Ngôn ngữ/hồ sơ** (language/profile): RDFS? OWL EL? OWL RL? OWL 2 DL đầy đủ?
2. **Chế độ suy diễn** (entailment regime): Direct Semantics? RDF-Based? Simple?
3. **Tác vụ suy luận** (reasoning task): Consistency checking? Subsumption? Instance checking? Conjunctive query answering?

Ví dụ đúng: "Forward chaining với tập quy tắc OWL RL là sound và complete cho tác vụ
instance checking trên đồ thị RDF thỏa mãn các hạn chế OWL RL."

Ví dụ sai: "Reasoner X là sound và complete." (Thiếu cả ba thành phần.)

### OWL RL: Sound nhưng không always complete

OWL 2 RL là profile được thiết kế để tương thích với rule-based reasoning
[@w3c-owl2-profiles]. Forward chaining với tập quy tắc OWL RL:

- **Sound:** Mọi kết quả suy ra đều là entailment OWL 2 hợp lệ
- **Complete cho tập quy tắc RL:** Mọi entailment có thể biểu diễn bằng quy tắc RL đều được suy ra
- **KHÔNG complete cho OWL 2 DL đầy đủ:** Có những entailment OWL 2 DL hợp lệ mà quy tắc RL không thể nắm bắt

Điều này không phải là lỗi — đó là sự đánh đổi thiết kế. OWL RL hy sinh một phần khả năng
biểu diễn để đạt được tính khả thi tính toán với forward chaining.

> 🖊 **Tự kiểm tra:** Giải thích tại sao một hệ thống forward chaining dùng quy tắc OWL RL
> có thể bỏ sót một số entailment OWL 2 DL. Cho ví dụ cụ thể về loại entailment mà quy
> tắc Horn không thể nắm bắt.

## 5.9 Chế độ suy diễn (Entailment Regime)

Cùng một đồ thị RDF, các chế độ suy diễn khác nhau cho kết quả khác nhau:

| Regime | Mô tả | Mức độ suy diễn |
|--------|-------|-----------------|
| Simple | Chỉ RDF cơ bản, không RDFS | Tối thiểu |
| RDFS | Thêm subClassOf, subPropertyOf, domain, range | Trung bình |
| OWL RL | Thêm quy tắc OWL tương thích rule engine | Cao (trong phạm vi RL) |
| OWL Direct | Ngữ nghĩa Description Logic đầy đủ (OWL 2 DL) | Cao nhất (trong DL) |
| OWL RDF-Based | Ngữ nghĩa trực tiếp trên RDF graph (OWL 2 Full) | Cao nhất (undecidable) |

Khi nói "$G \models \alpha$", luôn phải hỏi: $\models$ theo regime nào?

SPARQL 1.1 hỗ trợ chỉ định entailment regime qua `FROM` clause hoặc protocol parameter
[@w3c-sparql11-overview]. Engine SPARQL mặc định thường dùng Simple hoặc RDFS regime; OWL
regime yêu cầu cấu hình riêng.

## 5.10 Quy tắc Horn và SWRL

### Quy tắc Horn trong KG

Quy tắc Horn (Horn clause) có dạng:

$$\text{head} \leftarrow \text{body}_1 \land \text{body}_2 \land \dots \land \text{body}_n$$

Trong ngữ cảnh KG, head và body là các mẫu triple (triple patterns) với biến. Ví dụ:

$$\text{sisterCity}(y, x) \leftarrow \text{sisterCity}(x, y)$$

"Nếu x là sister city của y, thì y là sister city của x."

Quy tắc Horn có các tính chất quan trọng:

- **Đơn điệu:** Thêm triple vào body chỉ tăng kết quả, không giảm
- **Dừng được:** Trên đồ thị hữu hạn, forward chaining với quy tắc Horn luôn dừng
- **Giới hạn biểu diễn:** Không thể biểu diễn phủ định (negation), phép hoặc (disjunction) trong head, hoặc lượng từ tồn tại (existential quantification) trong head

### SWRL: Mở rộng OWL bằng quy tắc

SWRL (Semantic Web Rule Language) mở rộng OWL bằng cách cho phép dùng OWL class/property
expressions trong body và head của quy tắc [@swrl-submission].

> ⚠ **SWRL là W3C Member Submission (2004), KHÔNG phải W3C Recommendation.** Đây là tài
> liệu tham khảo, không phải chuẩn ổn định.

Vấn đề cốt lõi: **OWL DL + SWRL nói chung không quyết định được** (undecidable). Sự kết
hợp giữa expressive OWL class expressions và quy tắc Horn tạo ra khả năng biểu diễn vượt
qua giới hạn tính quyết định được (decidability) của Description Logic.

Trong thực tế, các hệ thống dùng SWRL thường:
- Hạn chế quy tắc SWRL để duy trì tính quyết định được
- Chấp nhận incompleteness (không suy ra hết)
- Hoặc chuyển sang OWL RL (giới hạn biểu diễn nhưng decidable)

## 5.11 Cầu nối đến Mechanism KG

Trong capstone project (Chương 10), chúng ta sẽ xây dựng hệ thống tri thức về mechanisms.
Chương 5 cung cấp hai công cụ then chốt:

1. **Suy diễn:** Từ các mechanism đã biết, suy ra các relationship mới (ví dụ: nếu mechanism
   A requires mechanism B, và B requires C, thì A transitively requires C). Forward chaining
   với quy tắc transitive property là ví dụ đơn giản nhất.

2. **Xác nhận:** Kiểm tra dữ liệu mechanism có tuân thủ ontology đã định nghĩa không. Ví
   dụ: mỗi Mechanism phải có ít nhất một MechanismOperation; mỗi Condition phải liên kết
   với ít nhất một Mechanism. SHACL shapes là công cụ phù hợp.

> ⚠ **Lưu ý thiết kế:** Khi xây dựng mechanism ontology, đừng cố gắng biểu diễn mọi thứ
> bằng OWL axioms. Một số ràng buộc (số lượng tối thiểu, kiểu dữ liệu, pattern) phù hợp
> hơn với SHACL. Một số suy diễn (transitive, symmetric) phù hợp hơn với quy tắc. Chọn
> công cụ đúng cho mục đích đúng.

## 5.12 Những ngộ nhận thường gặp

### Ngộ nhận 1: "RDFS domain/range kiểm tra dữ liệu"

**Sai.** RDFS domain/range là quy tắc suy diễn — chúng THÊM rdf:type vào đồ thị, không từ
chối triple nào. Kiểm tra dữ liệu là nhiệm vụ của SHACL.

### Ngộ nhận 2: "SHACL shape suy diễn tri thức mới"

**Sai.** SHACL shapes chỉ kiểm tra dữ liệu hiện có. Chúng không tham gia vào RDFS/OWL
entailment và không sinh ra triple mới.

### Ngộ nhận 3: "Vật chất hóa = suy diễn"

**Sai.** Vật chất hóa là chiến lược triển khai. Suy diễn (entailment) là quan hệ ngữ nghĩa
tồn tại độc lập với bất kỳ cài đặt nào.

### Ngộ nhận 4: "Reasoner luôn complete"

**Sai.** Completeness phụ thuộc vào language + regime + task. OWL RL forward chaining
không complete cho OWL 2 DL đầy đủ. Luôn ghi rõ phạm vi.

### Ngộ nhận 5: "Dữ liệu phù hợp SHACL = dữ liệu đúng"

**Sai.** Conformance chỉ nghĩa là dữ liệu khớp shapes. Dữ liệu có thể phù hợp mà vẫn sai
về mặt nội dung.

### Ngộ nhận 6: "Vi phạm SHACL = dữ liệu sai"

**Sai.** Vi phạm chỉ nghĩa là dữ liệu không khớp shapes. Dữ liệu có thể đúng về nội dung
nhưng không khớp cấu trúc kỳ vọng.

### Ngộ nhận 7: "Forward chaining luôn dừng"

**Sai.** Forward chaining chỉ đảm bảo dừng với quy tắc đơn điệu trên đồ thị hữu hạn. Quy
tắc có phủ định có thể phá vỡ tính đơn điệu và gây vòng lặp.

### Ngộ nhận 8: "SWRL là chuẩn W3C ổn định"

**Sai.** SWRL là Member Submission (2004), không phải Recommendation. Kết hợp OWL DL +
SWRL nói chung không quyết định được.

## 5.13 Câu hỏi suy ngẫm

1. ★ Giải thích sự khác biệt giữa inference và validation bằng một ví dụ cụ thể từ miền
   city/country.

2. ★★ Cho ontology với `Person ⊑ ∃hasName.xsd:string` và dữ liệu có `(Alice, rdf:type, Person)`
   nhưng không có triple `hasName` nào cho Alice. (a) OWL 2 DL entailment nói gì? (b)
   SHACL shape `sh:minCount 1` trên `hasName` nói gì? (c) Hai câu trả lời khác nhau như
   thế nào và tại sao?

3. ★★ Thiết kế bộ SHACL shapes cho Mechanism ontology: mỗi Mechanism phải có ít nhất một
   Definition, mỗi MechanismOperation phải liên kết với đúng một Mechanism, và mỗi
   Condition phải có description kiểu xsd:string. Viết shapes bằng Turtle.

4. ★★★ So sánh forward chaining trên RDFS và forward chaining trên OWL RL về: (a) tập quy
   tắc, (b) khả năng biểu diễn, (c) tính soundness và completeness, (d) chi phí tính toán.
   Trong trường hợp nào bạn chọn RDFS thay vì OWL RL?

5. ★★★ Một hệ thống dùng OWL RL forward chaining để suy diễn, và SHACL để xác nhận. Có
   trường hợp nào dữ liệu phù hợp SHACL nhưng hệ thống suy diễn ra kết quả sai (so với OWL
   2 DL semantics)? Giải thích bằng ví dụ.

## 5.14 Chúng ta đã biết gì

Chương này đã thiết lập sự phân biệt cốt lõi giữa hai pipeline:

- **Suy diễn (Inference):** Từ dữ liệu + ngữ nghĩa → tri thức mới. Forward chaining là
  thuật toán cơ bản. RDFS rules thêm thông tin. Vật chất hóa là chiến lược triển khai.
- **Xác nhận (Validation):** Từ dữ liệu + shapes → báo cáo phù hợp/vi phạm. SHACL là ngôn
  ngữ chuẩn. Shapes ≠ axioms. Conformance ≠ truth. Violation ≠ repair.

Chúng ta cũng đã học cách đánh giá hệ thống suy diễn bằng soundness và completeness — luôn
trong ngữ cảnh cụ thể của language + regime + task.

## 5.15 Chúng ta chưa làm được gì

Chương này đã dạy cơ chế suy diễn và xác nhận, nhưng chưa giải quyết các câu hỏi:

- **Tri thức đến từ đâu?** Suy diễn chỉ tạo ra tri thức mới từ tri thức cũ. Nhưng tri thức
  ban đầu đến từ đâu? Làm sao thu thập, trích xuất, và tích hợp tri thức từ nhiều nguồn?
  (Chương 7)
- **Khi hai nguồn mâu thuẫn thì sao?** Suy diễn giả định dữ liệu nhất quán. Nhưng trong
  thực tế, các nguồn tri thức khác nhau có thể đưa ra tuyên bố trái ngược. Làm sao xử lý
  mâu thuẫn? (Chương 6)
- **Làm sao suy diễn khi tri thức không chắc chắn?** Forward chaining và SHACL đều làm việc
  với tri thức nhị phân (đúng/sai). Nhưng nhiều tri thức thực tế mang tính xác suất hoặc
  quy nạp. (Chương 8)

Chương tiếp theo sẽ bắt đầu giải quyết câu hỏi về tuyên bố, bằng chứng, nguồn gốc và mâu
thuẫn — lớp Context trong Mental Model 1.
