# Chương 4 — Bản thể học và Ngữ nghĩa Hình thức

> **Định hướng chương**
>
> **Câu hỏi trung tâm:** Làm thế nào các ký hiệu trong đồ thị có thể nhận được ý nghĩa hình
> thức đủ chính xác để máy xác định điều gì suy ra một cách logic từ một tập tiên đề?
>
> **Vì sao quan trọng:** Ba chương trước đã xây dựng cấu trúc đồ thị, biểu diễn RDF/Property
> Graph, lược đồ, danh tính và ngữ cảnh. Nhưng tất cả những lớp đó vẫn chưa trả lời được câu
> hỏi: khi nào một kết luận *bắt buộc phải đúng* nếu các tiền đề đúng? Chương này cung cấp cơ
> chế hình thức để trả lời câu hỏi đó.
>
> **Bạn sẽ hiểu:**
>
> - Sự khác biệt giữa cú pháp (ký hiệu) và ngữ nghĩa hình thức (ý nghĩa toán học)
> - Ontology là gì và khác schema ở điểm nào
> - Cơ chế trung tâm: diễn giải (interpretation) → mô hình (model) → suy diễn (entailment)
> - Điều kiện cần và điều kiện đủ trong định nghĩa lớp
> - Giả định thế giới mở (Open World Assumption) và hệ quả của nó
> - Phân biệt tính nhất quán (consistency), tính thỏa được (satisfiability), và suy diễn
> - Trực giác về Description Logic và OWL 2 profiles
>
> **Tiên quyết:** Chương 1–3. Đặc biệt: khái niệm triple RDF (§2.1), owl:sameAs và giả định
> tên duy nhất (§3.2), RDFS domain/range như quy tắc suy diễn (§2.1, §3.1).
>
> **Bản đồ khái niệm:**
>
> Ký hiệu ≠ Ý nghĩa → Ontology = cam kết ngữ nghĩa → Diễn giải gán nghĩa cho ký hiệu →
> Mô hình = diễn giải thỏa mọi tiên đề → Suy diễn = đúng trong mọi mô hình → Lớp như tập
> hợp → Điều kiện cần/đủ → Thế giới mở → Nhất quán vs Thỏa được

## 4.1 Mở đầu: Cú pháp không phải là ý nghĩa

Trong ba chương trước, chúng ta đã làm việc với các ký hiệu như `City`, `Country`,
`capitalOf`, `Hanoi`, `Vietnam`. Chúng ta đã dùng chúng để xây dựng đồ thị, truy vấn, và
gắn ngữ cảnh. Nhưng có một câu hỏi nền tảng mà chúng ta chưa trả lời:

Chuỗi ký tự `City` có nghĩa gì đối với máy?

Không có nghĩa gì cả — ít nhất là không tự thân. Tên gọi `City` chỉ là một chuỗi ký tự. Nó
không tự động tương ứng với tập hợp các thành phố trong thực tế. Tương tự, quan hệ
`capitalOf` không tự động mang theo bất kỳ tính chất logic nào (đối xứng? bắc cầu? hàm?) —
trừ khi chúng ta *nói rõ* bằng một cơ chế hình thức.

Đây là sự phân biệt cốt lõi của chương:

```
cú pháp / ký hiệu    ≠    ngữ nghĩa hình thức
(syntax)                  (formal semantics)
```

Cú pháp là cách viết. Ngữ nghĩa hình thức là quy tắc toán học xác định ký hiệu đó *nghĩa là
gì* — cụ thể hơn, nó xác định những diễn giải nào được phép và những kết luận nào bắt buộc
phải đúng.

Một **ontology** (bản thể học) là công cụ để nối cú pháp với ngữ nghĩa. Trong chương này,
chúng ta sẽ tìm hiểu cơ chế mà qua đó một ontology biến các ký hiệu rời rạc thành một hệ
thống ý nghĩa mà máy có thể suy luận trên đó.

> 🖊 **Tự kiểm tra:** Trước khi đọc tiếp, hãy thử giải thích bằng lời của bạn: tại sao việc
> đặt tên một nút là `City` trong đồ thị RDF chưa đủ để máy "hiểu" rằng nút đó đại diện cho
> lớp các thành phố? Thông tin bổ sung nào cần thiết?

## 4.2 Ontology là gì?

### Từ schema đến ontology

Chương 3 đã giới thiệu **schema** (lược đồ) như phần mô tả cấu trúc và từ vựng được kỳ
vọng của đồ thị dữ liệu: lớp nào tồn tại, quan hệ nào nối từ đâu đến đâu, thuộc tính nào
được phép [@hogan-knowledge-graphs]. Schema trả lời câu hỏi "được phép có gì?"

Một **ontology** đi xa hơn: nó đưa ra các **cam kết ngữ nghĩa hình thức** (formal semantic
commitments) về các khái niệm và quan hệ trong miền tri thức. Nói cách khác:

- Schema nhấn mạnh cấu trúc và từ vựng kỳ vọng.
- Ontology nhấn mạnh các tiên đề logic xác định ý nghĩa của các khái niệm đó.

> ⚠ **Lưu ý về thuật ngữ:** Ranh giới giữa "schema" và "ontology" không tuyệt đối; các cộng
> đồng khác nhau dùng hai từ này với mức độ chồng lấn khác nhau. Trong cuốn sách này, chúng
> ta dùng sự phân biệt trên như một công cụ sư phạm, không phải như một định nghĩa phổ quát.

### Web Ontology Language (OWL)

**Web Ontology Language (OWL)** là chuẩn W3C để biểu diễn ontology trên nền RDF
[@w3c-owl2-overview]. OWL cung cấp một tập hợp các kiến tạo (constructs) để phát biểu các
tiên đề về lớp, thuộc tính và cá thể.

Một ontology OWL gồm ba loại thành phần:

1. **Thực thể** (entities): các đối tượng được đặt tên — lớp (class), thuộc tính đối tượng
   (object property), thuộc tính dữ liệu (data property), cá thể (individual).
2. **Biểu thức** (expressions): các tổ hợp của thực thể tạo thành mô tả phức tạp hơn — ví dụ
   "lớp những thứ vừa là City vừa có capitalOf trỏ đến một Country".
3. **Tiên đề** (axioms): các phát biểu ràng buộc ý nghĩa của thực thể và biểu thức — ví dụ
   "mọi CapitalCity đều là City".

> ⚠ **Phân biệt quan trọng:**
>
> - **Tên/nhãn** (name/label): chuỗi ký tự dùng để tham chiếu — `City`, `capitalOf`.
> - **Khai báo** (declaration): nói rằng một tên tồn tại — "có một lớp tên City". Khai báo
>   không gán ngữ nghĩa vượt quá sự tồn tại.
> - **Tiên đề** (axiom): phát biểu ràng buộc ngữ nghĩa — "mọi City đều là Place". Tiên đề
>   mới là thứ tạo ra suy diễn.
> - **Chú thích** (annotation): thông tin dành cho con người — nhãn hiển thị, mô tả, bình
>   luận. Chú thích **không** ảnh hưởng đến suy diễn logic trừ khi được liên kết với tiên đề
>   tường minh.

Một chú thích `rdfs:label "Thành phố"` giúp con người đọc hiểu, nhưng bộ suy luận không dùng
nó để rút ra kết luận logic. Chỉ có tiên đề mới làm được điều đó.

## 4.3 Cơ chế trung tâm: Diễn giải → Mô hình → Suy diễn

Đây là phần quan trọng nhất của chương. Hãy đọc chậm.

### Toán học tối thiểu cho chương này

Chương này dùng nhiều ký hiệu toán học hơn các chương trước. Dưới đây là các ký hiệu sẽ
xuất hiện, kèm ý nghĩa:

| Ký hiệu | Đọc là | Nghĩa |
|---------|--------|-------|
| ∈ | "thuộc" | x ∈ S: x là phần tử của tập S |
| ⊆ | "tập con của" | A ⊆ B: mọi phần tử của A đều thuộc B |
| ∩ | "giao" | A ∩ B: tập các phần tử thuộc cả A lẫn B |
| ∪ | "hợp" | A ∪ B: tập các phần tử thuộc A hoặc B |
| ∅ | "tập rỗng" | tập không có phần tử nào |
| × | "tích Descartes" | A × B: tập các cặp (a,b) với a∈A, b∈B |
| ∀ | "với mọi" | ∀x: P(x) — P đúng cho mọi x |
| ∃ | "tồn tại" | ∃x: P(x) — có ít nhất một x sao cho P đúng |
| ⇒ | "kéo theo" | P ⇒ Q: nếu P đúng thì Q đúng |
| ⇔ | "khi và chỉ khi" | P ⇔ Q: P đúng khi và chỉ khi Q đúng |
| ⊑ | "lớp con của" | C ⊑ D: C là lớp con của D (subsumption) |
| ⊓ | "giao" (DL) | C ⊓ D: giao của hai lớp trong Description Logic |
| ⊔ | "hợp" (DL) | C ⊔ D: hợp của hai lớp trong Description Logic |
| ¬ | "phủ định" | ¬C: phần bù của lớp C |
| ⊨ | "suy diễn" | O ⊨ α: ontology O suy diễn ra α |
| ^I | "diễn giải I" | C^I: tập mà lớp C được diễn giải thành |

Bạn không cần nhớ hết ngay. Bảng này là tài liệu tham khảo; mỗi ký hiệu sẽ được giải thích
trong ngữ cảnh khi xuất hiện lần đầu.

### Diễn giải (Interpretation)

Một **diễn giải** I là một cách gán ý nghĩa toán học cho các ký hiệu trong ontology. Cụ
thể, một diễn giải gồm:

1. Một **miền diễn giải** (interpretation domain) Δ^I — một tập hợp khác rỗng chứa các "đối
   tượng" mà chúng ta đang nói về.

2. Một **hàm diễn giải** (·)^I gán mỗi ký hiệu với một đối tượng toán học trên miền Δ^I.

Hãy xem xét một ví dụ cụ thể. Giả sử ontology của chúng ta có các ký hiệu: `City`,
`Country`, `Place`, `capitalOf`, `Hanoi`, `Vietnam`. Một diễn giải I có thể là:

```
Δ^I = {h, v, p, f}
```

Đây là miền diễn giải — bốn phần tử trừu tượng. Lưu ý: h, v, p, f **không phải** là chuỗi
ký tự "Hanoi", "Vietnam". Chúng là các phần tử toán học trong miền. Sự kết nối giữa tên gọi
và phần tử miền nằm ở hàm diễn giải:

```
Hanoi^I   = h
Vietnam^I = v
```

Mỗi tên cá thể (individual name) được gán với đúng một phần tử của miền. Đây chính là sự
khác biệt giữa **tên** và **thực thể** mà Chương 3 đã nhấn mạnh: tên là ký hiệu, phần tử
miền là đối tượng toán học mà tên đó biểu thị trong diễn giải này.

Lớp được diễn giải thành **tập con** của miền:

```
City^I    = {h, p}
Country^I = {v, f}
Place^I   = {h, v, p, f}
```

Đọc `City^I ⊆ Δ^I` như sau: "Trong diễn giải I, lớp City được gán với tập con {h, p} của
miền." Nói cách khác, trong diễn giải này, h và p là các "thành phố".

Thuộc tính đối tượng được diễn giải thành **quan hệ hai ngôi** trên miền:

```
capitalOf^I = {(h, v), (p, f)}
```

Đọc `capitalOf^I ⊆ Δ^I × Δ^I` như sau: "Trong diễn giải I, quan hệ capitalOf được gán với
tập các cặp {(h,v), (p,f)}." Nghĩa là: trong diễn giải này, h có quan hệ capitalOf với v,
và p có quan hệ capitalOf với f.

> ⚠ **Quan trọng:** Một diễn giải chỉ là *một cách* gán nghĩa. Có vô số diễn giải khác nhau
> cho cùng một bộ ký hiệu. Ví dụ, một diễn giải J có thể gán `City^J = {v}` — nghĩa là
> trong J, chỉ có v là "thành phố". Diễn giải J hoàn toàn hợp lệ về mặt toán học, dù nó
> không khớp với trực giác của chúng ta về thành phố. Vai trò của ontology là *loại bỏ* các
> diễn giải không phù hợp với ý định mô hình hóa.

### Tiên đề và sự thỏa mãn (Satisfaction)

Một **tiên đề** (axiom) là một phát biểu ràng buộc các diễn giải được phép. Xét tiên đề:

```
City ⊑ Place
```

Đọc: "City là lớp con của Place." Ý nghĩa hình thức của tiên đề này là điều kiện:

```
City^I ⊆ Place^I
```

Nghĩa là: trong bất kỳ diễn giải nào thỏa mãn tiên đề này, tập mà City được gán phải là tập
con của tập mà Place được gán.

Quay lại ví dụ: trong diễn giải I ở trên, `City^I = {h, p}` và `Place^I = {h, v, p, f}`.
Vì {h, p} ⊆ {h, v, p, f}, diễn giải I **thỏa mãn** tiên đề `City ⊑ Place`.

Ngược lại, xét diễn giải J với `City^J = {h, p}` và `Place^J = {h}`. Vì {h, p} ⊄ {h}
(phần tử p thuộc City^J nhưng không thuộc Place^J), diễn giải J **không thỏa mãn** tiên đề
này.

Một diễn giải **thỏa mãn** một tiên đề khi điều kiện ngữ nghĩa của tiên đề đó đúng trong
diễn giải đó.

### Mô hình (Model)

Một **mô hình** của ontology O là một diễn giải thỏa mãn **tất cả** các tiên đề trong O.

Nói cách khác: mô hình là diễn giải "hợp lệ" — diễn giải mà mọi tiên đề đều đúng.

```
Models(O) = { I | I thỏa mãn mọi tiên đề trong O }
```

Xét ontology O gồm hai tiên đề:

```
(1) City ⊑ Place
(2) Country ⊑ Place
```

Diễn giải I ở trên (với `Place^I = {h, v, p, f}`, `City^I = {h, p}`, `Country^I = {v, f}`)
thỏa mãn cả hai → I là một mô hình của O.

Diễn giải J (với `Place^J = {h}`) không thỏa mãn (1) → J không phải mô hình của O.

> 🖊 **Tự kiểm tra:** Tại sao "mô hình" không giống với "ontology"? Ontology là tập tiên đề
> (mô tả các ràng buộc). Mô hình là một diễn giải cụ thể thỏa mãn các ràng buộc đó. Một
> ontology có thể có nhiều mô hình khác nhau. Hãy giải thích bằng lời của bạn: tại sao việc
> có nhiều mô hình là đặc điểm thiết kế, không phải lỗi?

### Suy diễn (Entailment)

Bây giờ chúng ta đã sẵn sàng cho khái niệm trung tâm:

```
O ⊨ α
```

Đọc: **"Ontology O suy diễn ra alpha."**

Nghĩa chính xác: **mọi mô hình của O đều thỏa mãn α**.

Nói cách khác: α đúng trong *tất cả* các diễn giải hợp lệ của O. Không có ngoại lệ. Nếu bạn
tìm được dù chỉ một mô hình của O mà trong đó α sai, thì O ⊭ α (O không suy diễn ra α).

**Ví dụ cụ thể.** Xét ontology O gồm:

```
(1) CapitalCity ⊑ City
(2) Hanoi : CapitalCity
```

(Tiên đề (2) nói: cá thể Hanoi thuộc lớp CapitalCity.)

Câu hỏi: O có suy diễn ra `Hanoi : City` không?

Hãy xét bất kỳ mô hình M nào của O. Vì M thỏa mãn (1), ta có `CapitalCity^M ⊆ City^M`.
Vì M thỏa mãn (2), ta có `Hanoi^M ∈ CapitalCity^M`. Kết hợp hai điều: `Hanoi^M ∈ City^M`.
Vậy `Hanoi : City` đúng trong M.

Vì lập luận trên đúng cho *mọi* mô hình M của O, ta kết luận:

```
O ⊨ Hanoi : City
```

Đây không phải là "máy đoán" hay "AI phát hiện". Đây là hệ quả logic bắt buộc từ cấu trúc
toán học của các mô hình.

> ⚠ **Suy diễn KHÔNG có nghĩa là:**
>
> - α đúng trong thực tế (tiền đề có thể sai).
> - Nguồn dữ liệu đáng tin cậy (suy diễn không đánh giá provenance).
> - Dữ liệu đầu vào hợp lệ (suy diễn không kiểm tra validation).
> - Máy "hiểu" theo nghĩa con người (máy thao tác trên cấu trúc toán học, không có ý thức
>   về ý nghĩa).
>
> Suy diễn chỉ có nghĩa là: **nếu** các tiên đề đúng, **thì** α cũng đúng. Đó là một phát
> biểu có điều kiện, không phải khẳng định tuyệt đối.

### Tóm tắt cơ chế

```
Từ vựng + Tiên đề
        ↓
Các diễn giải có thể
        ↓ áp dụng tiên đề: loại bỏ diễn giải vi phạm
Models(O)
        ↓ α đúng trong mọi mô hình?
O ⊨ α
```

Ontology reasoning không phải là máy "suy nghĩ giống người". Nó là sự thu hẹp tập các diễn
giải có thể bằng các ràng buộc hình thức, rồi kiểm tra xem một phát biểu có đúng trong tất
cả các diễn giải còn lại hay không.

## 4.4 Lớp như tập hợp: subclass, equivalence, disjointness

Bây giờ ta áp dụng cơ chế diễn giải/mô hình/suy diễn vào các quan hệ giữa lớp.

### Subclass (Lớp con)

```
City ⊑ Place
```

Điều kiện ngữ nghĩa: `City^I ⊆ Place^I` trong mọi mô hình.

Đây là quan hệ **một chiều**. Từ `City ⊑ Place`, ta biết mọi City đều là Place. Nhưng ta
**không** biết mọi Place đều là City. Place có thể chứa các phần tử không thuộc City.

### Equivalent Classes (Lớp tương đương)

```
A ≡ B
```

Điều kiện ngữ nghĩa: `A^I = B^I` trong mọi mô hình.

Hai lớp tương đương khi và chỉ khi chúng có **cùng tập thành viên** trong mọi mô hình. Đây
là quan hệ hai chiều: `A ≡ B` tương đương với cả `A ⊑ B` lẫn `B ⊑ A`.

> ⚠ **Ngộ nhận phổ biến:** Nhầm lẫn `owl:equivalentClass` với `owl:sameAs`.
>
> - `owl:sameAs` (Chương 3): hai **cá thể** là một. `ex:Hanoi owl:sameAs wd:Q1858` nghĩa là
>   hai tên này chỉ cùng một cá thể.
> - `owl:equivalentClass`: hai **lớp** có cùng tập thành viên. `City ≡ UrbanArea` nghĩa là
>   trong mọi mô hình, tập các City bằng tập các UrbanArea.
>
> Một bên nói về identity của cá thể. Một bên nói về equality của tập hợp. Đừng nhầm.

### Disjoint Classes (Lớp rời nhau)

```
City ⊓ Country ≡ ⊥
```

Điều kiện ngữ nghĩa: `City^I ∩ Country^I = ∅` trong mọi mô hình.

Nghĩa là: không có phần tử nào vừa là City vừa là Country.

> ⚠ **Quan trọng:** Các tên lớp khác nhau **không tự động** rời nhau. Việc `City` và
> `Country` là hai tên khác nhau không ngụ ý `City^I ∩ Country^I = ∅`. Tính rời nhau phải
> được **khai báo tường minh** bằng một tiên đề. Đây là hệ quả trực tiếp của việc OWL không
> có giả định tên duy nhất (Chương 3): tên khác nhau không ngụ ý thực thể khác nhau, và
> tương tự, tên lớp khác nhau không ngụ ý tập thành viên rời nhau.

**Phản ví dụ:** Giả sử ontology chỉ có `City` và `Country` mà không có tiên đề disjointness.
Khi đó tồn tại một mô hình trong đó `City^I = {h, v}` và `Country^I = {v, f}` — phần tử v
thuộc cả hai lớp. Mô hình này hoàn toàn hợp lệ vì không có tiên đề nào cấm nó.

## 4.5 Điều kiện cần và điều kiện đủ

Đây là một trong những phần sâu nhất của chương. Hãy đọc kỹ.

### SubClassOf là điều kiện đủ một chiều

Xét:

```
CapitalCity ⊑ City
```

Đọc: "Mọi CapitalCity đều là City." Về mặt logic:

- Nếu x là CapitalCity ⇒ x là City. (Điều kiện **đủ**: là CapitalCity đủ để kết luận là City.)
- Nếu x là City ⇒ x là CapitalCity? **KHÔNG.** Là City không đủ để kết luận là CapitalCity.

Nói cách khác, `CapitalCity ⊑ City` cho ta điều kiện đủ cho City (là CapitalCity thì chắc
chắn là City), nhưng chỉ cho điều kiện **cần** cho CapitalCity (muốn là CapitalCity thì
trước hết phải là City).

### Điều kiện cần: SubClassOf với biểu thức lớp

Xét:

```
CapitalCity ⊑ City ⊓ ∃capitalOf.Country
```

Đọc: "Mọi CapitalCity đều là City VÀ có quan hệ capitalOf đến ít nhất một Country."

Vế phải (`City ⊓ ∃capitalOf.Country`) mô tả các **điều kiện cần** cho CapitalCity: nếu một
cá thể là CapitalCity, thì nó *phải* thỏa mãn cả hai điều kiện này. Nhưng ngược lại chưa
đúng: một cá thể thỏa mãn vế phải chưa chắc là CapitalCity (vì tiên đề chỉ nói một chiều).

### Điều kiện cần VÀ đủ: EquivalentClasses

Xét:

```
CapitalCity ≡ City ⊓ ∃capitalOf.Country
```

Đọc: "CapitalCity khi và chỉ khi là City và có quan hệ capitalOf đến ít nhất một Country."

Bây giờ vế phải vừa là điều kiện cần vừa là điều kiện đủ. Bất kỳ cá thể nào thỏa mãn vế
phải đều được phân loại là CapitalCity, và ngược lại.

**Ví dụ cụ thể.** Giả sử ontology O chứa:

```
(1) CapitalCity ≡ City ⊓ ∃capitalOf.Country
(2) Hanoi : City
(3) Vietnam : Country
(4) capitalOf(Hanoi, Vietnam)
```

Câu hỏi: O ⊨ `Hanoi : CapitalCity`?

Hãy xét bất kỳ mô hình M nào của O:

- Từ (2): `Hanoi^M ∈ City^M`
- Từ (3): `Vietnam^M ∈ Country^M`
- Từ (4): `(Hanoi^M, Vietnam^M) ∈ capitalOf^M`

Kết hợp: `Hanoi^M ∈ City^M` và tồn tại `Vietnam^M ∈ Country^M` sao cho
`(Hanoi^M, Vietnam^M) ∈ capitalOf^M`. Vậy `Hanoi^M` thuộc tập `{x | x ∈ City^M và ∃y:
(x,y) ∈ capitalOf^M và y ∈ Country^M}`.

Từ (1), tập này chính là `CapitalCity^M`. Vậy `Hanoi^M ∈ CapitalCity^M`.

Vì lập luận đúng cho mọi mô hình M:

```
O ⊨ Hanoi : CapitalCity
```

> 🖊 **Tự kiểm tra:** Giả sử thay (1) bằng `CapitalCity ⊑ City ⊓ ∃capitalOf.Country` (chỉ
> SubClassOf, không phải Equivalence). Với cùng dữ liệu (2)-(4), O có suy diễn ra
> `Hanoi : CapitalCity` không? Tại sao? Gợi ý: xét xem có tồn tại mô hình nào trong đó
> Hanoi thỏa mãn vế phải nhưng không thuộc CapitalCity^M không.

## 4.6 Biểu thức lớp (Class Expressions)

OWL cung cấp các kiến tạo để xây dựng biểu thức lớp phức tạp từ các lớp đơn giản. Mỗi biểu
thức có ngữ nghĩa tập hợp chính xác.

### Giao (Intersection)

```
C ⊓ D
```

Ngữ nghĩa: `(C ⊓ D)^I = C^I ∩ D^I`

Tập các phần tử thuộc **cả** C lẫn D. Ví dụ: `City ⊓ HasAirport` là lớp các thành phố có
sân bay.

### Hợp (Union)

```
C ⊔ D
```

Ngữ nghĩa: `(C ⊔ D)^I = C^I ∪ D^I`

Tập các phần tử thuộc C **hoặc** D (hoặc cả hai).

### Phủ định (Complement)

```
¬C
```

Ngữ nghĩa: `(¬C)^I = Δ^I \ C^I`

Tập các phần tử trong miền **không** thuộc C. Lưu ý: phủ định tính tương đối so với miền
diễn giải Δ^I, không phải "mọi thứ trong vũ trụ".

### Hạn chế tồn tại (Existential Restriction)

```
∃ R.C
```

Đọc: "những thứ có ít nhất một R-liên kết đến một phần tử thuộc C."

Ngữ nghĩa:

```
(∃ R.C)^I = { x ∈ Δ^I | ∃y: (x,y) ∈ R^I và y ∈ C^I }
```

**Ví dụ:** `∃capitalOf.Country` là lớp các cá thể có quan hệ capitalOf đến ít nhất một
Country. Trong diễn giải I ở trên, `Hanoi^I = h` và `(h,v) ∈ capitalOf^I` với
`v ∈ Country^I`, nên `h ∈ (∃capitalOf.Country)^I`.

> ⚠ **Hệ quả quan trọng của thế giới mở:** Hạn chế tồn tại yêu cầu sự **tồn tại** của một
> phần tử y trong miền diễn giải, nhưng y **không nhất thiết phải có tên** trong đồ thị RDF.
> Nghĩa là: ontology có thể suy diễn rằng "tồn tại một Country mà Hanoi là thủ đô" ngay cả
> khi không có cá thể Country nào được đặt tên tường minh trong dữ liệu. Bộ suy luận có thể
> tạo ra một phần tử ẩn (anonymous element) trong miền để thỏa mãn hạn chế. Đừng nhầm lẫn
> giữa "có trong dữ liệu" và "tồn tại trong mô hình".

### Hạn chế phổ quát (Universal Restriction)

```
∀ R.C
```

Đọc: "những thứ mà mọi R-liên kết đều dẫn đến phần tử thuộc C."

Ngữ nghĩa:

```
(∀ R.C)^I = { x ∈ Δ^I | ∀y: (x,y) ∈ R^I ⇒ y ∈ C^I }
```

> ⚠ **Ranh giới tinh tế:** Hạn chế phổ quát **không** khẳng định rằng R-liên kết tồn tại.
> Nếu x không có bất kỳ R-liên kết nào, thì `∀ R.C` vẫn đúng cho x — một cách trống rỗng
> (vacuously true). Đây là hệ quả của logic cổ điển: "với mọi y, nếu (x,y) ∈ R^I thì y ∈ C^I"
> đúng tự động khi không có y nào thỏa (x,y) ∈ R^I.
>
> **Ví dụ:** Giả sử `∀hasChild.Doctor` ("mọi con đều là bác sĩ"). Nếu Alice không có con nào
> được biết đến trong mô hình, thì Alice thuộc `(∀hasChild.Doctor)^I` — không phải vì con
> cô ấy là bác sĩ, mà vì điều kiện "mọi con" được thỏa mãn một cách trống rỗng. Đây là lý do
> hạn chế phổ quát không thể dùng như một ràng buộc "phải có ít nhất một giá trị".

### Lực lượng (Cardinality)

OWL cung cấp các hạn chế về số lượng:

```
≥ n R.C    (ít nhất n R-liên kết đến phần tử thuộc C)
≤ n R.C    (nhiều nhất n R-liên kết đến phần tử thuộc C)
= n R.C    (đúng n R-liên kết đến phần tử thuộc C)
```

> ⚠ **OWL cardinality KHÔNG phải là form validation.** Trong cơ sở dữ liệu, "required field"
> hay "unique constraint" kiểm tra dữ liệu hiện có. Trong OWL, dưới giả định thế giới mở và
> không có giả định tên duy nhất:
>
> - `≥ 1 hasChild.Person` không yêu cầu dữ liệu RDF phải chứa một triple hasChild tường minh.
>   Bộ suy luận có thể suy diễn sự tồn tại của một Person ẩn.
> - `≤ 1 hasNationalCapital.City` với hai tên `Hanoi` và `HaNoiCity` không tự động gây lỗi.
>   Thay vào đó, bộ suy luận có thể suy diễn `Hanoi owl:sameAs HaNoiCity` (Chương 3).
>
> Validation theo nghĩa "kiểm tra dữ liệu tuân thủ quy tắc" là công việc của SHACL (Chương 5),
> không phải OWL.

## 4.7 Ngữ nghĩa thuộc tính (Property Semantics)

Ngoài lớp, OWL còn cho phép phát biểu tiên đề về thuộc tính. Dưới đây là các đặc trưng
quan trọng nhất, mỗi đặc trưng được giải thích qua cơ chế thay vì chỉ liệt kê.

### Subproperty (Thuộc tính con)

```
capitalOf ⊑ locatedIn
```

Ngữ nghĩa: `capitalOf^I ⊆ locatedIn^I` trong mọi mô hình.

Nếu (x,y) ∈ capitalOf^I thì (x,y) ∈ locatedIn^I. Mọi cặp thủ đô-quốc gia cũng là cặp
"nằm trong".

### Inverse (Nghịch đảo)

```
capitalOf⁻ ≡ hasCapital
```

Ngữ nghĩa: `(x,y) ∈ capitalOf^I ⇔ (y,x) ∈ hasCapital^I`.

Nếu Hanoi capitalOf Vietnam thì Vietnam hasCapital Hanoi, và ngược lại.

### Symmetric (Đối xứng)

```
Sym(sisterCity)
```

Ngữ nghĩa: `(x,y) ∈ sisterCity^I ⇒ (y,x) ∈ sisterCity^I`.

Nếu Hanoi sisterCity Paris thì Paris sisterCity Hanoi.

### Transitive (Bắc cầu)

```
Trans(locatedIn)
```

Ngữ nghĩa: `(x,y) ∈ locatedIn^I và (y,z) ∈ locatedIn^I ⇒ (x,z) ∈ locatedIn^I`.

Nếu Hanoi locatedIn Vietnam và Vietnam locatedIn SoutheastAsia thì Hanoi locatedIn
SoutheastAsia.

### Functional (Hàm)

```
Func(hasNationalCapital)
```

Ngữ nghĩa: `(x,y) ∈ hasNationalCapital^I và (x,z) ∈ hasNationalCapital^I ⇒ y = z`.

Mỗi cá thể có **nhiều nhất một** hasNationalCapital trong mô hình.

> ⚠ **Bất ngờ quan trọng cho kỹ sư cơ sở dữ liệu:** Giả sử ontology khai báo
> `Func(hasNationalCapital)` và dữ liệu chứa:
>
> ```
> Vietnam hasNationalCapital Hanoi
> Vietnam hasNationalCapital HaNoiCity
> ```
>
> Trong cơ sở dữ liệu quan hệ, đây là vi phạm ràng buộc unique. Nhưng trong OWL, vì không có
> giả định tên duy nhất (Chương 3), bộ suy luận **không báo lỗi**. Thay vào đó, nó suy diễn:
>
> ```
> Hanoi owl:sameAs HaNoiCity
> ```
>
> Hai tên được coi là cùng một cá thể. Đây là hệ quả trực tiếp của việc OWL dùng ngữ nghĩa
> mô hình: thay vì từ chối dữ liệu, hệ thống tìm mô hình thỏa mãn tất cả tiên đề — và mô
> hình đó gán hai tên cho cùng một phần tử miền. Nếu bạn muốn từ chối dữ liệu trùng lặp, hãy
> dùng SHACL (Chương 5).

### Inverse-Functional (Nghịch đảo hàm)

```
InvFunc(hasNationalCapital)
```

Ngữ nghĩa: `(x,z) ∈ hasNationalCapital^I và (y,z) ∈ hasNationalCapital^I ⇒ x = y`.

Nếu hai quốc gia đều có cùng thủ đô (theo hasNationalCapital), thì hai quốc gia đó là một.

## 4.8 Giả định thế giới mở (Open World Assumption)

Đây là một trong những khái niệm gây bất ngờ nhất cho kỹ sư quen với cơ sở dữ liệu. Hãy
dành thời gian cho nó.

### Trực giác cơ sở dữ liệu: thiếu = sai

Trong hầu hết hệ thống cơ sở dữ liệu, nếu một trường không có giá trị, hệ thống xử lý như
thể giá trị đó không tồn tại hoặc bị từ chối. Đây là **giả định thế giới đóng** (Closed
World Assumption): những gì không được biết là sai.

```
Cơ sở dữ liệu:
  không có dữ liệu → coi như false / absent
```

### Trực giác OWL: thiếu = chưa biết

OWL hoạt động theo **giả định thế giới mở** (Open World Assumption):

```
OWL:
  không có dữ liệu → unknown (chưa biết)
                    trừ khi falsity suy ra được từ các tiên đề
```

**Ví dụ:** Đồ thị không chứa triple nào về sân bay của Hà Nội:

```
(không có) Hanoi hasAirport X
```

Điều này **KHÔNG** suy diễn ra:

```
"Hà Nội không có sân bay"
```

Nó chỉ có nghĩa là: chúng ta không biết Hà Nội có sân bay hay không. Có thể có, có thể
không. Ontology chưa nói.

### Ba trạng thái suy diễn

Trong OWL, một phát biểu α đối với ontology O rơi vào đúng một trong ba trạng thái:

| Trạng thái | Ký hiệu | Nghĩa |
|------------|---------|-------|
| Được suy diễn | O ⊨ α | α đúng trong mọi mô hình của O |
| Bị phủ định | O ⊨ ¬α | α sai trong mọi mô hình của O |
| Chưa xác định | O ⊭ α và O ⊭ ¬α | Có mô hình thỏa α, có mô hình thỏa ¬α |

Trạng thái thứ ba — **chưa xác định** — là trạng thái mà cơ sở dữ liệu truyền thống không
có. Trong OWL, nó là trạng thái mặc định cho hầu hết các phát biểu mà ontology chưa ràng
buộc đủ chặt.

> ⚠ **OWL không phải là "mọi thứ đều có thể đúng."** Các tiên đề vẫn loại bỏ các diễn giải
> không phù hợp. Thế giới mở có nghĩa là sự vắng mặt của thông tin không phải là bằng chứng
> của sự phủ định — nhưng các tiên đề vẫn ràng buộc tập mô hình. Một ontology càng nhiều
> tiên đề thì tập mô hình càng nhỏ, và càng nhiều phát biểu được xác định (entailed hoặc
> contradicted).

### Hệ quả cho validation

Đây là lý do OWL restrictions không tương đương với:

```
required field / NOT NULL / schema validation
```

Trong cơ sở dữ liệu, "required field" nghĩa là dữ liệu phải chứa giá trị. Trong OWL,
`∃R.C` nghĩa là trong mô hình phải tồn tại một R-filler — nhưng filler đó có thể là phần
tử ẩn, không có tên trong dữ liệu. OWL không kiểm tra dữ liệu; OWL mô tả cấu trúc của các
mô hình hợp lệ.

Validation theo nghĩa "từ chối dữ liệu không tuân thủ" thuộc về SHACL (Chương 5).

> 🖊 **Tự kiểm tra:** Giả sử ontology có `Person ⊑ ∃hasName.String` ("mọi Person đều có ít
> nhất một tên"). Đồ thị RDF chứa `ex:Alice rdf:type ex:Person` nhưng không có triple
> `ex:Alice ex:hasName ...` nào. Theo OWL, ontology có nhất quán không? Alice có phải là
> Person hợp lệ không? Giải thích tại sao câu trả lời khác với trực giác cơ sở dữ liệu.

## 4.9 Nhất quán, Thỏa được, Suy diễn: ba câu hỏi khác nhau

Ba khái niệm này thường bị nhầm lẫn. Hãy phân biệt rõ.

### Tính nhất quán của ontology (Consistency)

**Câu hỏi:** Tồn tại ít nhất một mô hình của O không?

```
O nhất quán ⇔ Models(O) ≠ ∅
```

Nếu ontology mâu thuẫn nội tại (ví dụ: vừa khẳng định `A ⊑ B` vừa `A ⊓ B ≡ ⊥` với
`∃x: x ∈ A`), thì không có mô hình nào → ontology không nhất quán.

### Tính thỏa được của lớp (Class Satisfiability)

**Câu hỏi:** Lớp C có thể có ít nhất một thành viên trong một mô hình nào đó của O không?

```
C thỏa được đối với O ⇔ ∃I ∈ Models(O): C^I ≠ ∅
```

> ⚠ **Phân biệt tinh tế:** Một ontology có thể **nhất quán** trong khi một lớp cụ thể **không
> thỏa được**.
>
> **Ví dụ:**
> ```
> City ⊓ Country ≡ ⊥          (City và Country rời nhau)
> ImpossiblePlace ≡ City ⊓ Country  (ImpossiblePlace = giao của hai lớp rời)
> ```
> Ontology này vẫn nhất quán — tồn tại mô hình trong đó `City^I = {h}`, `Country^I = {v}`,
> `ImpossiblePlace^I = ∅`. Lớp `ImpossiblePlace` chỉ bị buộc phải có tập rỗng. Nó không
> gây mâu thuẫn; nó chỉ không thể có thành viên.
>
> Ngược lại, nếu thêm tiên đề `∃x: x ∈ ImpossiblePlace`, thì ontology trở nên **không nhất
> quán** — vì không có mô hình nào thỏa mãn cả "ImpossiblePlace phải có thành viên" lẫn
> "ImpossiblePlace = ∅".

### Suy diễn (Entailment)

**Câu hỏi:** α đúng trong mọi mô hình của O không?

```
O ⊨ α
```

Đây là câu hỏi đã gặp ở §4.3. Nó khác với cả consistency lẫn satisfiability.

| Câu hỏi | Đối tượng | Trả lời |
|---------|-----------|---------|
| Consistency | Toàn bộ ontology | Có tồn tại mô hình? |
| Satisfiability | Một lớp cụ thể | Lớp có thể có thành viên? |
| Entailment | Một phát biểu | Phát biểu đúng trong mọi mô hình? |

## 4.10 Trực giác Description Logic

Sau khi đã hiểu cơ chế diễn giải/mô hình/suy diễn, chúng ta có thể đặt OWL vào bối cảnh rộng
hơn.

**Description Logic (DL)** là họ các ngôn ngữ logic được thiết kế để cân bằng giữa:

```
khả năng biểu diễn (expressiveness)
        ↕ đánh đổi
tính khả thi của suy luận (decidability / tractability)
```

DL là nền tảng lý thuyết của OWL. OWL 2 DL tương ứng với một DL cụ thể (SROIQ). Chúng ta
không cần học toàn bộ DL để dùng OWL hiệu quả, nhưng hiểu trực giác DL giúp tránh ngộ nhận.

### TBox, ABox, RBox: phân loại tinh thần

Trong truyền thống DL, các tiên đề thường được phân thành ba nhóm:

**TBox** (Terminological Box): tri thức tổng quát về miền — định nghĩa lớp, quan hệ subclass,
equivalence, disjointness.

```
City ⊑ Place
CapitalCity ≡ City ⊓ ∃capitalOf.Country
City ⊓ Country ≡ ⊥
```

**ABox** (Assertional Box): sự kiện về cá thể cụ thể.

```
Hanoi : City
Vietnam : Country
capitalOf(Hanoi, Vietnam)
```

**RBox** (Role Box): tiên đề về thuộc tính — transitivity, symmetry, functionality, v.v.

```
Trans(locatedIn)
Func(hasNationalCapital)
capitalOf⁻ ≡ hasCapital
```

> ⚠ **Rất quan trọng:** TBox/ABox/RBox là **phân loại tinh thần hữu ích**, KHÔNG phải các
> phần vật lý bắt buộc trong file OWL. Một ontology OWL là một tập tiên đề phẳng; không có
> yêu cầu cú pháp nào buộc bạn phải tách chúng thành ba file hay ba section riêng biệt. Phân
> loại này giúp tổ chức tư duy, không phải tổ chức tệp tin.

## 4.11 OWL Direct Semantics và RDF-Based Semantics

OWL 2 có hai ngữ nghĩa chính thức [@w3c-owl2-direct-semantics] [@w3c-owl2-rdf-semantics]:

- **Direct Semantics**: định nghĩa ngữ nghĩa trực tiếp trên cấu trúc OWL structural model.
  Đây là ngữ nghĩa dùng trong chương này vì nó cho phép giải thích interpretation → model →
  entailment một cách sạch sẽ và trực tiếp.

- **RDF-Based Semantics**: định nghĩa ngữ nghĩa dựa trên RDF triples, mở rộng ngữ nghĩa RDF.
  Phù hợp khi làm việc với dữ liệu RDF thuần túy và cần tương thích với RDFS.

Chương này chủ yếu dùng góc nhìn Direct Semantics / OWL 2 DL vì mục tiêu sư phạm: giúp bạn
hiểu cơ chế suy diễn mà không bị phân tán bởi chi tiết serialization. Khi triển khai thực tế
trên dữ liệu RDF, hãy tham khảo RDF-Based Semantics để hiểu sự khác biệt.

## 4.12 OWL 2 Profiles

OWL 2 đầy đủ rất biểu đạt, nhưng suy luận trên nó có thể tốn kém. W3C định nghĩa ba
**profiles** — các tập con của OWL 2 đánh đổi khả năng biểu diễn lấy hiệu suất suy luận
[@w3c-owl2-profiles]:

| Profile | Thiết kế cho | Đặc điểm suy luận |
|---------|-------------|-------------------|
| **OWL 2 EL** | Ontology lớn với nhiều lớp/thuộc tính | Suy luận chuẩn trong thời gian đa thức; phù hợp taxonomy y khoa, sinh học |
| **OWL 2 QL** | Truy vấn trên lượng lớn dữ liệu cá thể | Hỗ trợ query rewriting sang SQL; phù hợp khi ABox rất lớn |
| **OWL 2 RL** | Suy luận dạng luật trên dữ liệu RDF | Tương thích với rule engine; phù hợp forward-chaining trên RDF stores |

> ⚠ **Không có profile "tốt nhất".** Lựa chọn phụ thuộc vào cấu trúc ontology và tác vụ suy
> luận cụ thể. EL không "nhanh hơn QL" trong mọi trường hợp; QL không "tốt hơn RL" cho mọi
> ứng dụng. Hãy chọn dựa trên yêu cầu thực tế, không dựa trên bảng xếp hạng chung chung.

## 4.13 Cầu nối đến Mechanism Knowledge Graph

Tại sao ontology quan trọng cho hệ thống tri thức cơ chế (Mechanism Knowledge System) mà
cuốn sách hướng tới?

Xét ví dụ: chúng ta muốn định nghĩa hình thức thế nào là một **Rate of Change Mechanism**.
Bằng OWL, ta có thể viết:

```
RateOfChangeMechanism
≡
Mechanism
⊓ ∃hasOperation.DerivativeOperation
⊓ ∃hasInput.Quantity
⊓ ∃hasReferenceVariable.ReferenceVariable
```

Đọc: "Một RateOfChangeMechanism khi và chỉ khi nó là một Mechanism, có ít nhất một
DerivativeOperation, có ít nhất một Quantity làm đầu vào, và có ít nhất một
ReferenceVariable."

Điều này cho phép ontology **phân loại tự động**: nếu một cá thể m thỏa mãn tất cả các điều
kiện bên phải, bộ suy luận sẽ suy diễn `m : RateOfChangeMechanism` mà không cần ai gắn nhãn
tường minh.

Nhưng ontology **không giải quyết được**:

- Làm sao trích xuất mô tả cơ chế từ văn bản sách giáo khoa?
- Làm sao đánh giá hai mô tả nhiễu có cùng chỉ một cơ chế?
- Làm sao đánh giá chất lượng bằng chứng?
- Làm sao xử lý mâu thuẫn giữa các nguồn?
- Làm sao quản lý hiệu lực thời gian?
- Làm sao quyết định khi nào một ứng viên trở thành tri thức được chấp nhận?

Những bài toán đó thuộc về các chương sau (Chương 6–10). Ontology cung cấp nền tảng ngữ nghĩa
hình thức — cấu trúc để nói "điều gì suy ra từ điều gì" — nhưng không thay thế được quá
trình thu thập, đánh giá và tiến hóa tri thức.

## 4.14 Những ngộ nhận thường gặp

**Sai lầm 1: "Ontology = taxonomy."** Taxonomy chỉ là cây phân cấp subclass. Ontology bao
gồm taxonomy nhưng thêm equivalence, disjointness, restrictions, property characteristics,
và các tiên đề phức tạp hơn. Taxonomy là tập con của ontology.

**Sai lầm 2: "Ontology = schema."** Schema nhấn mạnh cấu trúc kỳ vọng. Ontology nhấn mạnh
cam kết ngữ nghĩa hình thức. Ranh giới mờ, nhưng sự phân biệt hữu ích: schema nói "được
phép có gì", ontology nói "các khái niệm nghĩa là gì và điều gì suy ra từ đó".

**Sai lầm 3: "OWL tự động gán ý nghĩa con người cho từ ngữ."** OWL gán ngữ nghĩa toán học
(tập hợp, quan hệ), không phải ý nghĩa ngôn ngữ tự nhiên. `City` trong OWL là một tập con
của Δ^I, không phải khái niệm "thành phố" trong tâm trí con người.

**Sai lầm 4: "`owl:equivalentClass` giống `owl:sameAs`."** Đã phân tích ở §4.4.
equivalentClass = equality của tập hợp lớp. sameAs = identity của cá thể.

**Sai lầm 5: "Tên lớp khác nhau tự động rời nhau."** Đã phân tích ở §4.4. Disjointness phải
được khai báo tường minh.

**Sai lầm 6: "Thiếu thông tin nghĩa là sai."** Đã phân tích ở §4.8. OWL dùng Open World
Assumption: thiếu = chưa biết.

**Sai lầm 7: "OWL restriction là database validation rule."** Đã phân tích ở §4.6 và §4.8.
OWL mô tả cấu trúc mô hình, không kiểm tra dữ liệu. Dùng SHACL cho validation.

**Sai lầm 8: "`minCardinality 1` nghĩa là dữ liệu RDF phải chứa giá trị."** Không. OWL có
thể suy diễn sự tồn tại của phần tử ẩn trong mô hình.

**Sai lầm 9: "Suy diễn hình thức chứng minh sự thật thực tế."** Suy diễn chỉ chứng minh hệ
quy logic: nếu tiền đề đúng thì kết luận đúng. Tiền đề có thể sai.

**Sai lầm 10: "Bộ suy luận 'sáng tạo' tri thức bằng AI."** Bộ suy luận thao tác trên cấu
trúc toán học. Nó không sáng tạo; nó tính toán hệ quả logic của các tiên đề.

**Sai lầm 11: "TBox/ABox/RBox là các file OWL bắt buộc."** Đã phân tích ở §4.10. Chúng là
phân loại tinh thần, không phải yêu cầu vật lý.

**Sai lầm 12: "Ngôn ngữ càng biểu đạt càng tốt."** Biểu đạt cao hơn thường đi kèm chi phí
suy luận cao hơn. Chọn profile phù hợp với tác vụ, không phải ngôn ngữ mạnh nhất.

## 4.15 Câu hỏi suy ngẫm

1. (★) Cho `CapitalCity ⊑ City` và dữ liệu `Hanoi : City`. Ta có thể kết luận
   `Hanoi : CapitalCity` không? Tại sao?

2. (★★) Cho `CapitalCity ≡ City ⊓ ∃capitalOf.Country` và dữ liệu:
   ```
   Hanoi : City
   Hanoi capitalOf Vietnam
   Vietnam : Country
   ```
   Tại sao Hanoi được phân loại là CapitalCity? Giải thích bằng ngữ nghĩa tập hợp/mô hình,
   không dùng từ khóa OWL.

3. (★★) Đồ thị không chứa triple `hasChild` nào cho Alice. OWL có thể kết luận Alice không
   có con không? Phát biểu bổ sung nào cần thiết để thiết lập điều gì đó mạnh hơn?

4. (★★★) Giả sử `hasNationalCapital` được khai báo functional và ta có:
   ```
   Vietnam hasNationalCapital Hanoi
   Vietnam hasNationalCapital HaNoiCity
   ```
   mà không có tiên đề nào nói Hanoi và HaNoiCity khác nhau. Tại sao OWL có thể KHÔNG coi
   đây là mâu thuẫn? Kết nối câu trả lời với Chương 3.

5. (★★★) Một ontology có thể nhất quán trong khi chứa một lớp không thỏa được không? Hãy
   xây dựng một ví dụ.

## 4.16 Chúng ta đã biết gì

- Cú pháp (ký hiệu) khác với ngữ nghĩa hình thức (ý nghĩa toán học).
- Ontology là tập tiên đề ràng buộc cách ký hiệu được diễn giải.
- Diễn giải gán nghĩa toán học cho ký hiệu: lớp → tập hợp, thuộc tính → quan hệ, cá thể →
  phần tử miền.
- Mô hình là diễn giải thỏa mãn mọi tiên đề.
- Suy diễn (O ⊨ α) nghĩa là α đúng trong mọi mô hình của O.
- SubClassOf là điều kiện đủ một chiều; Equivalence là điều kiện cần và đủ.
- Hạn chế tồn tại yêu cầu sự tồn tại trong mô hình, không nhất thiết trong dữ liệu.
- Hạn chế phổ quát không khẳng định sự tồn tại của liên kết.
- OWL dùng giả định thế giới mở: thiếu ≠ sai.
- Cardinality OWL là ngữ nghĩa logic, không phải form validation.
- Tính nhất quán, thỏa được, và suy diễn là ba câu hỏi khác nhau.
- TBox/ABox/RBox là phân loại tinh thần, không phải yêu cầu vật lý.

## 4.17 Chúng ta chưa làm được gì

Chúng ta đã hiểu **ngữ nghĩa hình thức là gì** và **hệ quả logic được định nghĩa như thế
nào**. Nhưng chúng ta chưa trả lời:

- Bộ suy luận **tính toán** các hệ quả đó bằng thuật toán nào?
- Nên **materialize** (tính trước) hay suy diễn tại thời điểm truy vấn?
- Hệ thống luật (rule systems) liên quan thế nào đến ngữ nghĩa OWL/RDFS?
- Làm sao phân biệt **inference** (suy diễn) với **validation** (xác nhận)?
- SHACL kiểm tra sự không tuân thủ như thế nào?
- Làm sao sửa chữa dữ liệu không hợp lệ?

Những câu hỏi này mở ra **Chương 5 — Suy diễn, Quy tắc và Xác nhận**.

## Thuật ngữ đã gặp trong chương này

| Thuật ngữ | Nghĩa ngắn | Học chi tiết |
|-----------|-----------|--------------|
| Ontology (bản thể học) | Tập tiên đề ràng buộc ngữ nghĩa hình thức của ký hiệu | §4.2 |
| Axiom (tiên đề) | Phát biểu ràng buộc ngữ nghĩa | §4.2 |
| Interpretation (diễn giải) | Cách gán nghĩa toán học cho ký hiệu | §4.3 |
| Model (mô hình) | Diễn giải thỏa mãn mọi tiên đề | §4.3 |
| Entailment (suy diễn) | O ⊨ α: α đúng trong mọi mô hình của O | §4.3 |
| Subclass (lớp con) | C ⊑ D: C^I ⊆ D^I | §4.4 |
| Equivalent Classes (lớp tương đương) | A ≡ B: A^I = B^I | §4.4 |
| Disjoint Classes (lớp rời nhau) | C ⊓ D ≡ ⊥: C^I ∩ D^I = ∅ | §4.4 |
| Class Expression (biểu thức lớp) | Tổ hợp lớp: giao, hợp, phủ định, hạn chế | §4.6 |
| Existential Restriction (hạn chế tồn tại) | ∃R.C: có ít nhất một R-liên kết đến C | §4.6 |
| Universal Restriction (hạn chế phổ quát) | ∀R.C: mọi R-liên kết đều đến C | §4.6 |
| Necessary Condition (điều kiện cần) | SubClassOf một chiều | §4.5 |
| Sufficient Condition (điều kiện đủ) | Equivalence hai chiều | §4.5 |
| Open World Assumption (giả định thế giới mở) | Thiếu ≠ sai | §4.8 |
| Consistency (tính nhất quán) | Tồn tại ít nhất một mô hình | §4.9 |
| Satisfiability (tính thỏa được) | Lớp có thể có thành viên trong mô hình | §4.9 |
| Description Logic | Họ ngôn ngữ logic cân bằng biểu đạt và khả thi suy luận | §4.10 |
| TBox / ABox / RBox | Phân loại tinh thần: tri thức tổng quát / cá thể / thuộc tính | §4.10 |
| OWL 2 EL / QL / RL | Profiles đánh đổi biểu đạt lấy hiệu suất | §4.12 |

## Đọc thêm

- OWL 2 Web Ontology Language Primer [@w3c-owl2-primer] — giới thiệu toàn diện OWL 2.
- OWL 2 Direct Semantics [@w3c-owl2-direct-semantics] — ngữ nghĩa hình thức chuẩn.
- Hogan et al., *Knowledge Graphs*, Chapter 6: Deductive Knowledge [@hogan-knowledge-graphs] — suy diễn và ontology.
- OWL 2 Profiles [@w3c-owl2-profiles] — EL, QL, RL design rationale.
