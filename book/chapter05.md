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
> - Cơ chế forward chaining với phép thế biến (substitution) và điểm bất động (fixpoint)
> - RDFS entailment: quy tắc thêm thông tin, không phải ràng buộc kiểm tra
> - Vật chất hóa (materialization) vs suy diễn tại thời điểm truy vấn
> - SHACL: target → focus node → path → value node → constraint → validation result
> - Phù hợp (conformance) ≠ đúng (truth); vi phạm (violation) ≠ sửa chữa (repair)
> - Tính nhất quán (consistency) vs xác nhận (validation) — hai trục độc lập
> - Soundness/completeness phụ thuộc language + regime + task
> - Giới hạn của OWL RL và quy tắc Horn đối với OWL 2 DL đầy đủ
>
> **Tiên quyết:** Chương 1–4. Đặc biệt: RDFS domain/range như quy tắc suy diễn (§3.1),
> diễn giải → mô hình → suy diễn (§4.3), điều kiện cần/đủ (§4.5), OWL Profiles (§4.12).
>
> **Bản đồ khái niệm:**
>
> Inference ≠ Validation → Forward chaining với θ → Fixpoint → RDFS rules thêm thông tin →
> Materialization vs query-time → Backward reasoning → SHACL mechanism walkthrough →
> Focus/value nodes → Validation report anatomy → Conformance ≠ Truth →
> Consistency ≠ Validation → Repair mechanism → Soundness + Completeness →
> OWL RL giới hạn → SWRL/RIF bối cảnh

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

### Phép thế biến: Cầu nối giữa quy tắc trừu tượng và dữ liệu cụ thể

Trước khi viết công thức, cần hiểu một cơ chế nền tảng: **phép thế** (substitution).

Một quy tắc thường chứa **biến** (variable). Ví dụ:

$$\text{CapitalCity}(x) \to \text{City}(x)$$

Quy tắc này nói: "với *bất kỳ* $x$ nào, nếu $x$ là CapitalCity thì $x$ cũng là City." Nhưng
đồ thị dữ liệu không chứa biến — nó chứa các thực thể cụ thể như `Hanoi`, `HoChiMinh`.

**Phép thế** $\theta$ (theta) là ánh xạ gán mỗi biến với một giá trị cụ thể:

$$\theta = \{ x \mapsto \text{Hanoi} \}$$

Áp dụng $\theta$ lên quy tắc:

- $\theta(\text{body}) = \text{CapitalCity}(\text{Hanoi})$ — phần thân đã được "ground"
- $\theta(\text{head}) = \text{City}(\text{Hanoi})$ — phần đầu đã được "ground"

Nếu $\theta(\text{body})$ khớp với dữ liệu hiện có trong đồ thị, thì ta được phép thêm
$\theta(\text{head})$ vào đồ thị.

> ⚠ **Tại sao phép thế quan trọng?** Không có $\theta$, quy tắc chỉ là mẫu trừu tượng.
> Chính phép thế kết nối quy tắc tổng quát với các thực thể cụ thể trong đồ thị. Đây là cơ
> chế cốt lõi của mọi hệ thống suy diễn dựa trên quy tắc.

### Cơ chế hình thức

Cho tập quy tắc $R$ và đồ thị ban đầu $G_0$, forward chaining tính toán dãy:

$$G_{i+1} = G_i \cup \{ \theta(\text{head}(r)) \mid r \in R, \; \theta(\text{body}(r)) \subseteq G_i \}$$

Nói bằng lời: ở mỗi bước, tìm mọi quy tắc $r$ và mọi phép thế $\theta$ sao cho phần thân
đã thế $\theta(\text{body}(r))$ khớp hoàn toàn với đồ thị hiện tại $G_i$, rồi thêm phần đầu
đã thế $\theta(\text{head}(r))$ vào đồ thị.

Thuật toán dừng khi đạt **điểm bất động** (fixpoint):

$$G_{n+1} = G_n$$

Khi không còn triple mới nào được sinh ra, đồ thị $G_n$ được gọi là **bao đóng** (closure)
của $G_0$ dưới tập quy tắc $R$.

> ⚠ **Phân biệt:** Bao đóng (closure) là đối tượng tính toán — đồ thị chứa các assertion
> ban đầu cộng với mọi hệ quả đã vật chất hóa. Entailment là quan hệ ngữ nghĩa — $\alpha$
> được entail bởi $G$ nếu $\alpha$ đúng trong mọi mô hình của $G$. Closure là một cách để
> *tính toán* entailment, nhưng closure ≠ entailment.

### Ví dụ đầy đủ: Forward chaining qua nhiều vòng

Xét đồ thị ban đầu $G_0$:

```
Hanoi    rdf:type     CapitalCity
```

Và hai quy tắc:

$$r_1: \text{CapitalCity}(x) \to \text{City}(x)$$
$$r_2: \text{City}(x) \to \text{Place}(x)$$

**Vòng 0:** $G_0 = \{ \text{CapitalCity}(\text{Hanoi}) \}$

**Vòng 1:** Tìm quy tắc khớp với $G_0$:
- $r_1$ với $\theta_1 = \{x \mapsto \text{Hanoi}\}$:
  - $\theta_1(\text{body}) = \text{CapitalCity}(\text{Hanoi}) \in G_0$ ✓
  - Thêm $\theta_1(\text{head}) = \text{City}(\text{Hanoi})$
- $r_2$ với $\theta = \{x \mapsto \text{Hanoi}\}$:
  - $\theta(\text{body}) = \text{City}(\text{Hanoi}) \notin G_0$ ✗

$G_1 = G_0 \cup \{ \text{City}(\text{Hanoi}) \}$

**Vòng 2:** Tìm quy tắc khớp với $G_1$:
- $r_1$: $\text{CapitalCity}(\text{Hanoi})$ đã có, $\text{City}(\text{Hanoi})$ đã có → không thêm gì mới
- $r_2$ với $\theta_2 = \{x \mapsto \text{Hanoi}\}$:
  - $\theta_2(\text{body}) = \text{City}(\text{Hanoi}) \in G_1$ ✓
  - Thêm $\theta_2(\text{head}) = \text{Place}(\text{Hanoi})$

$G_2 = G_1 \cup \{ \text{Place}(\text{Hanoi}) \}$

**Vòng 3:** Không quy tắc nào sinh triple mới. $G_3 = G_2$.

**Điểm bất động đạt được.** Bao đóng của $G_0$ dưới $\{r_1, r_2\}$ là:

$$G_\infty = \{ \text{CapitalCity}(\text{Hanoi}), \; \text{City}(\text{Hanoi}), \; \text{Place}(\text{Hanoi}) \}$$

Hình bên dưới tóm tắt quá trình forward chaining qua ba vòng. Mỗi mũi tên biểu thị một vòng
áp dụng quy tắc với phép thế $\theta$ cụ thể. Vòng 3 không sinh triple mới → fixpoint.

![Forward chaining: $G_0 \to G_1 \to G_2 \to G_3 = G_2$ (fixpoint). Mỗi vòng áp dụng quy
tắc với phép thế $\theta = \{x \mapsto \text{Hanoi}\}$, thêm triple mới cho đến khi không
còn gì để thêm.](figures/generated/ch05-forward-fixpoint.pdf)

> 🖊 **Tự kiểm tra:** Tại sao "không còn triple mới" nghĩa là forward chaining đã ổn định?
> Nếu ở vòng $k$ không có triple mới được thêm, điều gì đảm bảo rằng vòng $k+1$ cũng sẽ
> không thêm gì? (Gợi ý: tập quy tắc không thay đổi, và đồ thị không thay đổi.)

### Ví dụ trên miền cơ chế — θ, chuỗi quy tắc và điểm bất động

Áp dụng cùng cơ chế lên dữ liệu cơ chế đang chạy. Trong đồ thị gốc có:

```turtle
ex:rateOfChange_1 a ex:RateOfChangeMechanism .
ex:RateOfChangeMechanism rdfs:subClassOf ex:ChangeMechanism .
ex:ChangeMechanism rdfs:subClassOf ex:Mechanism .
```

Quy tắc RDFS subClassOf có dạng chung:

$$r_{sub}: A \text{ rdfs:subClassOf } B, \; x \text{ rdf:type } A \to x \text{ rdf:type } B$$

**Vòng 0:** $G_0$ chứa ba triple trên.

**Vòng 1:**
- Áp dụng $r_{sub}$ với phép thế
  $$\theta_1 = \{ A \mapsto \text{ex:RateOfChangeMechanism}, B \mapsto \text{ex:ChangeMechanism}, x \mapsto \text{ex:rateOfChange}_1 \}$$
- $\theta_1(\text{body})$ gồm `ex:RateOfChangeMechanism rdfs:subClassOf ex:ChangeMechanism` và `ex:rateOfChange_1 a ex:RateOfChangeMechanism`, cả hai đều $\in G_0$ ✓
- Thêm $\theta_1(\text{head}) =$ `ex:rateOfChange_1 a ex:ChangeMechanism`

$G_1 = G_0 \cup \{ \text{ex:rateOfChange\_1 a ex:ChangeMechanism} \}$

**Vòng 2:**
- Áp dụng $r_{sub}$ với
  $$\theta_2 = \{ A \mapsto \text{ex:ChangeMechanism}, B \mapsto \text{ex:Mechanism}, x \mapsto \text{ex:rateOfChange}_1 \}$$
- $\theta_2(\text{body})$ gồm `ex:ChangeMechanism rdfs:subClassOf ex:Mechanism` và `ex:rateOfChange_1 a ex:ChangeMechanism` (vừa suy ra ở vòng 1) ✓
- Thêm $\theta_2(\text{head}) =$ `ex:rateOfChange_1 a ex:Mechanism`

$G_2 = G_1 \cup \{ \text{ex:rateOfChange\_1 a ex:Mechanism} \}$

**Vòng 3:** Không còn cặp `(A rdfs:subClassOf B, x : A)` mới nào để áp dụng. $G_3 = G_2$.

**Điểm bất động.** Forward chaining đã vật chất hóa phân loại: từ `ex:rateOfChange_1 a
ex:RateOfChangeMechanism`, quy tắc suy ra `ex:rateOfChange_1 a ex:ChangeMechanism` rồi
`ex:rateOfChange_1 a ex:Mechanism`. Đây chính là **classification fixpoint** của cơ chế
phân cấp lớp trong miền cơ chế.

> ⚠ **Từ phép thế đến ground fact.** Các triple cuối cùng (`ex:rateOfChange_1 a
> ex:Mechanism`) không còn chứa biến — chúng là **ground fact**. Một **ground triple**
> (hay ground fact) là một triple trong đó mọi vị trí đều là IRI hoặc literal cụ thể,
> không còn biến. Quá trình thay thế biến bằng giá trị cụ thể gọi là **grounding**.

### Toán tử hệ quả tức thời $T_P$ và điểm bất động nhỏ nhất

Công thức truy hồi $G_{i+1} = G_i \cup \{\,\theta(\text{head}(r)) \mid \theta(\text{body}(r))
\subseteq G_i\,\}$ ở trên là một cách viết cụ thể của một khái niệm tổng quát và mạnh hơn:
**toán tử hệ quả tức thời** (immediate consequence operator) $T_P$.

Cho một chương quy tắc $P$ (một tập các quy tắc Horn/Datalog) và một tập ground fact $I$,
$T_P(I)$ là tập mọi ground head có được từ các quy tắc trong $P$ mà body của chúng đã hoàn
toàn nằm trong $I$:

$$T_P(I) \;=\; \bigl\{\, \theta(\text{head}(r)) \;\big|\; r \in P,\; \theta(\text{body}(r)) \subseteq I \,\bigr\}$$

Forward chaining chính là quá trình lặp $T_P$ bắt đầu từ tập rỗng:

$$\emptyset \;\subseteq\; T_P(\emptyset) \;\subseteq\; T_P^2(\emptyset) \;\subseteq\; T_P^3(\emptyset) \;\subseteq\; \dots$$

**Vì sao dãy này tăng dần?** Vì $T_P$ là **đơn điệu**: nếu $I \subseteq J$ thì $T_P(I)
\subseteq T_P(J)$ — thêm fact vào không thể làm mất đi body đã khớp. Trên một **vũ trụ ground
hữu hạn** (chỉ có hữu hạn ground fact có thể tồn tại), một dãy tập hợp đơn điệu tăng bắt
buộc hội tụ. Đích đến của nó là **điểm bất động nhỏ nhất** (least fixed point) của $T_P$:

$$\mathrm{lfp}(T_P) \;=\; \bigcup_{k \ge 0} T_P^{k}(\emptyset)$$

> ℹ **Cơ sở của phát biểu này là định lý Knaster–Tarski.** Trên lattice các tập ground fact
> (xếp theo quan hệ chứa), mọi toán tử đơn điệu đều có một điểm bất động nhỏ nhất, và điểm
> bất động nhỏ nhất đó là giao của tất cả các điểm bất động. Vì $T_P$ đơn điệu, forward
> chaining luôn hội tụ đúng về $\mathrm{lfp}(T_P)$.

Một hệ quả thực tế quan trọng: $\mathrm{lfp}(T_P)$ **không phụ thuộc vào thứ tự** bạn áp
dụng các quy tắc. Dù engine chạy quy tắc nào trước, kết quả cuối cùng là duy nhất. Đây là
điều cho phép ta nói về "bao đóng của $G_0$ dưới $P$" như một đối tượng có định nghĩa tốt,
và là cơ sở để nhiều engine chạy quy tắc song song (phần RETE và RDFox ở §5.5).

### Cầu nối Đại số tuyến tính: bao đóng bắc cầu qua lũy thừa ma trận kề

Nếu đã học Đại số tuyến tính, bạn có thể nắm cơ chế này qua một tương tự quen thuộc: tính
**bao đóng bắc cầu** (transitive closure) của một đồ thị bằng lũy thừa ma trận kề.

Gọi $A$ là ma trận kề nhị phân của đồ thị ($A_{ij}=1$ nếu có cạnh $i \to j$). Đường đi độ
dài $k$ từ $i$ đến $j$ được ghi nhận bởi phần tử $(A^k)_{ij}$. Bao đóng bắc cầu — mọi cặp
$(i,j)$ có đường đi bất kỳ — là tổng lũy thừa:

$$A^{*} \;=\; A + A^{2} + A^{3} + \dots + A^{k}$$

Lấy cho đến khi $A^{k+1}$ không thêm phần tử khác không nào mới; khi đó tổng đã hội tụ. Đây
chính là một fixpoint: lặp lũy thừa dừng khi không còn đường đi mới xuất hiện.

| Đại số tuyến tính (bao đóng bắc cầu) | Forward chaining ($T_P$) |
|---|---|
| $A$ — cạnh asserted | $G_0$ — đồ thị asserted |
| $A^k$ — đường đi đúng $k$ bước | $T_P^k(\emptyset)$ — fact cần $k$ vòng quy tắc |
| $A^*$ — mọi đường đi | $\mathrm{lfp}(T_P)$ — bao đóng |
| Dừng khi $A^{k+1}$ không thêm gì | Dừng khi $G_{n+1} = G_n$ |

> ℹ **Tương tự, không đồng nhất.** Forward chaining tổng quát hơn bao đóng bắc cầu thuần, vì
> một quy tắc có thể ghép nhiều mẫu cùng lúc (join) chứ không chỉ nối hai cạnh. Nhưng trực
> giác "lặp đến khi không còn gì mới" là chung cho cả hai — và nó giải thích vì sao các
> engine có thể dùng phép nhân ma trận thưa (sparse) để tăng tốc suy diễn quan hệ.

### Trực quan hóa từng khung hình: forward chaining trên Mechanism KG

Hãy quan sát cơ chế này qua bốn khung hình trên chính ontology cơ chế đã xây ở Chương 4.
Đồ thị gốc chứa ba triple khẳng định; ba quy tắc Datalog dưới đây được định nghĩa trên
ontology đó:

$$r_1:\quad \text{hasInput}(m, q) \leftarrow \text{hasApplication}(m, a) \land \text{differentiand}(a, q)$$

$$r_2:\quad \text{hasReferenceVariable}(m, v) \leftarrow \text{hasApplication}(m, a) \land \text{withRespectTo}(a, v)$$

$$r_3:\quad \text{type}(m, \text{RateOfChangeMechanism}) \leftarrow \text{type}(m, \text{Mechanism}) \land \text{hasInput}(m, \_) \land \text{hasReferenceVariable}(m, \_)$$

> ℹ **$r_3$ là bản Datalog của định nghĩa DL ở §4.13.** Ở Chương 4,
> $\text{RateOfChangeMechanism} \equiv \text{Mechanism} \sqcap \exists\text{hasApplication}.\text{DerivativeApplication}$.
> Ở đây ta viết lại nó như một quy tắc suy diễn tiến: một cơ chế được phân loại là
> RateOfChangeMechanism khi nó có cả `hasInput` lẫn `hasReferenceVariable` — hai thuộc tính
> mà mọi DerivativeApplication đều cung cấp (qua `differentiand` và `withRespectTo`). Cùng
> một tri thức, hai hình thức biểu diễn.

**Khung 0 — Đồ thị gốc $G_0$** (ba triple khẳng định):

```turtle
ex:rateOfChange_1            ex:hasApplication    ex:derivativeApplication_1 .
ex:derivativeApplication_1   ex:differentiand     ex:position_1 .
ex:derivativeApplication_1   ex:withRespectTo     ex:time_1 .
```

**Khung 1 — Lượt áp dụng thứ nhất $G_1 = T_P(G_0) \cup G_0$:** $r_1$ và $r_2$ khớp trên
$G_0$; hai triple mới suy ra được (tô đỏ):

```turtle
ex:rateOfChange_1   ex:hasInput                ex:position_1 .   # mới — từ r_1
ex:rateOfChange_1   ex:hasReferenceVariable    ex:time_1 .       # mới — từ r_2
```

**Khung 2 — Lượt áp dụng thứ hai $G_2 = T_P(G_1) \cup G_1$:** $r_3$ khớp vì `hasInput` và
`hasReferenceVariable` vừa xuất hiện; một triple mới suy ra được (tô xanh):

```turtle
ex:rateOfChange_1   rdf:type   ex:RateOfChangeMechanism .        # mới — từ r_3
```

**Khung 3 — Điểm bất động $G_3 = T_P(G_2) \cup G_2$:** một lượt áp dụng quy tắc trên $G_2$
không sinh thêm triple nào; $G_3 = G_2$. Hệ thống dừng, và bao đóng $\mathrm{lfp}(T_P)$ đã
được vật chất hóa.

![Forward chaining từng khung hình trên Mechanism KG: $G_0 \to G_1 \to G_2 \to G_3 = G_2$
(fixpoint). Khung 0: ba triple khẳng định. Khung 1: hai triple suy ra (tô đỏ). Khung 2: một
triple suy ra (tô xanh). Khung 3: không triple mới → dừng.](figures/generated/ch05-frame-by-frame.pdf)

> 🖊 **Tự kiểm tra:** Ở khung 2, vì sao $r_3$ không thể khớp ngay từ khung 0? Hãy chỉ ra
> ground fact nào còn thiếu trong $G_0$ khiến body của $r_3$ chưa thỏa. (Gợi ý: nhìn vào
> hai vị trí `hasInput(m, _)` và `hasReferenceVariable(m, _)`.)

### Đơn điệu (Monotonicity)

Forward chaining hoạt động đúng đắn nhờ tính **đơn điệu** (monotonicity). Một chế độ suy
diễn là đơn điệu khi:

$$\text{Nếu } G \subseteq G' \text{ thì } \text{Consequences}(G) \subseteq \text{Consequences}(G')$$

Nói bằng lời: thêm thông tin vào đồ thị không bao giờ làm mất đi các kết luận đã suy ra được
trước đó. Thông tin mới chỉ *mở rộng* tập kết quả, không bao giờ *thu hẹp*.

> ⚠ **Đơn điệu KHÔNG nghĩa là:**
>
> - "Thêm điều kiện vào body của quy tắc sẽ tăng kết quả" — sai, thêm điều kiện vào body
>   làm quy tắc khó khớp hơn, có thể *giảm* kết quả.
> - "Đơn điệu = dừng được" — sai, đây là hai tính chất độc lập.
> - "Đơn điệu = đầy đủ" — sai, một hệ thống có thể đơn điệu nhưng vẫn bỏ sót entailment.
> - "Đơn điệu = nhất quán" — sai, một hệ thống đơn điệu vẫn có thể suy ra mâu thuẫn nếu dữ
>   liệu ban đầu mâu thuẫn.

**Ví dụ về tính đơn điệu:** Nếu từ $G_0$ ta suy ra `City(Hanoi)`, thì dù sau này thêm bất
kỳ triple nào vào đồ thị, `City(Hanoi)` vẫn là hệ quả hợp lệ. Ta không bao giờ phải "rút
lại" kết luận cũ.

**Suy diễn không đơn điệu:** Ngược lại, các hệ thống dùng phủ định-as-failure hoặc quy tắc
dạng "trừ khi..." (unless) có thể rút lại kết luận khi thông tin mới xuất hiện. Ví dụ: "X
là bird → X flies" nhưng sau đó thêm "X là penguin" thì kết luận "X flies" bị rút lại. Đây
là lĩnh vực nghiên cứu riêng (non-monotonic reasoning); chương này chỉ đề cập ngắn gọn để
phân biệt.

### Điều kiện dừng

Forward chaining đảm bảo dừng khi thỏa mãn đồng thời các điều kiện sau:

1. **Đồ thị ban đầu hữu hạn** — số lượng triple ban đầu là hữu hạn.
2. **Tập quy tắc hữu hạn** — số lượng quy tắc là hữu hạn.
3. **Quy tắc không hàm** (function-free) — không có ký hiệu hàm tạo ra term mới vô hạn.
4. **Biến an toàn** (safe/range-restricted) — mọi biến trong head đều xuất hiện trong body,
   đảm bảo phép thế chỉ dùng các giá trị đã có trong đồ thị.
5. **Không cơ chế sinh term mới vô hạn** — không có cơ chế nào tạo ra vô hạn tài nguyên/tên
   mới (như blank node fresh trong OWL existential).

Trong điều kiện hữu hạn-ground như trên, chỉ có hữu hạn ground fact có thể tồn tại, nên quá
trình đơn điệu tăng dần bắt buộc đạt điểm bất động.

> ⚠ **Quan trọng:**
>
> - **Dừng ≠ Đơn điệu.** Một hệ thống có thể đơn điệu nhưng vẫn không dừng nếu thiếu các
>   điều kiện trên (ví dụ: quy tắc có hàm tạo term mới vô hạn).
> - **Không đơn điệu ≠ Không dừng.** Phủ định/non-monotonicity và termination là hai tính
>   chất độc lập. Một hệ thống non-monotonic vẫn có thể dừng, và một hệ thống monotonic
>   vẫn có thể không dừng.
>
> Các ngôn ngữ quy tắc an toàn cho KG (RDFS entailment rules, OWL RL rules, RIF Core
> [@w3c-rif-core]) được thiết kế để thỏa mãn các điều kiện trên, đảm bảo forward chaining
> luôn dừng trên đồ thị hữu hạn.

> ⚠ **Lưu ý quan trọng:** Forward chaining là một *thuật toán*, không phải một *định nghĩa
> ngữ nghĩa*. Nó tính toán hệ quả dựa trên tập quy tắc cụ thể. Tập quy tắc khác nhau cho
> kết quả khác nhau từ cùng đồ thị ban đầu. Khi nói "suy diễn", luôn phải ghi rõ: suy diễn
> theo *chế độ nào* (entailment regime)?

## 5.3 RDFS Entailment Rules: Suy diễn thêm thông tin

RDF Schema (RDFS) định nghĩa ngữ nghĩa suy diễn chuẩn. Ngữ nghĩa này được định nghĩa
chính thức bằng mô hình lý thuyết (model-theoretic semantics) trong RDF 1.1 Semantics
[@w3c-rdf11-mt]. Bốn quy tắc suy diễn quan trọng nhất, tương ứng với các mẫu suy diễn
(entailment patterns) trong Section 9.2.1 của đặc tả:

### rdfs:subClassOf (Pattern rdfs9)

Nếu `A rdfs:subClassOf B` và `x rdf:type A`, thì suy ra `x rdf:type B`.

Đây là quy tắc truyền loại theo phân cấp lớp. Như ví dụ §5.2 đã minh họa.

### rdfs:subPropertyOf (Pattern rdfs7)

Nếu `P rdfs:subPropertyOf Q` và `x P y`, thì suy ra `x Q y`.

Quy tắc này cho phép xây dựng phân cấp thuộc tính. Ví dụ: nếu `capitalOf rdfs:subPropertyOf locatedIn`, thì mọi cặp `(city, capitalOf, country)` cũng suy ra `(city, locatedIn, country)`.

### rdfs:domain (Pattern rdfs2)

Nếu `P rdfs:domain C` và `x P y`, thì suy ra `x rdf:type C`.

### rdfs:range (Pattern rdfs3)

Nếu `P rdfs:range C` và `x P y`, thì suy ra `y rdf:type C`.

### Domain/Range là quy tắc suy diễn, KHÔNG phải ràng buộc xác nhận

Đây là điểm then chốt đã được nhấn mạnh ở §3.1 và Chương 4, và cần nhắc lại ở đây vì
nó là nguồn nhầm lẫn phổ biến nhất:

> ⚠ **rdfs:domain và rdfs:range THÊM thông tin vào đồ thị.** Chúng KHÔNG kiểm tra, KHÔNG
> từ chối, và KHÔNG gây lỗi khi dữ liệu "không khớp." Nếu property `locatedIn` có
> `rdfs:domain City`, và bạn thấy triple `(UnknownEntity, locatedIn, SomePlace)` trong dữ
> liệu, RDFS *không* báo lỗi — nó suy ra `UnknownEntity rdf:type City`. Triple gốc vẫn
> tồn tại và hợp lệ.

Kết quả suy diễn có thể trông phi lý trong thực tế. Ví dụ:

```
capitalOf   rdfs:domain   City
capitalOf   rdfs:range    Country
Vietnam     capitalOf     Hanoi
```

Forward chaining suy ra:

```
Vietnam   rdf:type   City       ← từ domain
Hanoi     rdf:type   Country    ← từ range
```

Trong thực tế, Vietnam không phải là City và Hanoi không phải là Country. Nhưng RDFS không
quan tâm đến "thực tế" — nó chỉ áp dụng quy tắc ngữ nghĩa. Kết quả suy diễn đúng theo ngữ
nghĩa RDFS, ngay cả khi nó vô nghĩa trong miền ứng dụng. Đây chính là lý do tại sao:

$$\text{suy diễn (inference)} \neq \text{xác nhận (validation)}$$

Việc kiểm tra xem dữ liệu có "khớp" với kỳ vọng hay không là nhiệm vụ của SHACL (§5.6),
không phải RDFS.

**Ví dụ trên miền cơ chế.** Trong ontology cơ chế:

```turtle
ex:RateOfChangeMechanism rdfs:subClassOf ex:ChangeMechanism .
ex:ChangeMechanism rdfs:subClassOf ex:Mechanism .
```

Nếu dữ liệu ghi `ex:rateOfChange_1 a ex:RateOfChangeMechanism`, bao đóng RDFS sẽ thêm:

```turtle
ex:rateOfChange_1 a ex:ChangeMechanism .
ex:rateOfChange_1 a ex:Mechanism .
```

Không ai cần phải viết tường minh `ex:rateOfChange_1 a ex:Mechanism`; đó là hệ quả logic.
Nhưng nếu shape yêu cầu mỗi `ex:Mechanism` phải có ít nhất một `ex:hasOperation` mà dữ liệu
thiếu, SHACL sẽ báo vi phạm — RDFS không quan tâm điều đó.

### Quy tắc RDFS: Operationalization của ngữ nghĩa model-theoretic

Cần phân biệt rõ hai cấp độ:

1. **Ngữ nghĩa chuẩn (normative semantics):** RDFS entailment được định nghĩa bằng mô hình
   lý thuyết trong RDF 1.1 Semantics [@w3c-rdf11-mt]. Định nghĩa này xác định *điều gì là
   hệ quả*, độc lập với bất kỳ thuật toán nào.

2. **Triển khai bằng quy tắc (rule-based operationalization):** Các mẫu suy diễn RDFS có thể
   được vận hành như quy tắc forward chaining. Cách tiếp cận này *đúng đắn* (sound) — mọi
   kết quả đều là entailment hợp lệ. Tuy nhiên, trên cú pháp RDF chuẩn, naive rule closure
   *không đầy đủ* (not complete) — có những entailment hợp lệ mà quy tắc không sinh ra được.
   Tính đầy đủ đòi hỏi cú pháp RDF tổng quát (generalized RDF) hoặc các cơ chế bổ sung
   [@w3c-rdf11-mt, Appendix A].

> ℹ **Trong phạm vi chương này,** chúng ta dùng forward chaining với các mẫu RDFS chính
> (subClassOf, subPropertyOf, domain, range) như một cách triển khai hữu ích và trực quan.
> Đây là tập con đủ để minh họa cơ chế; ngữ nghĩa chuẩn đầy đủ nằm ngoài phạm vi.

### Bao đóng RDFS

Áp dụng forward chaining với tập quy tắc RDFS lên đồ thị $G$ cho kết quả là **bao
đóng RDFS** (RDFS closure) của $G$, ký hiệu $\text{cl}_{\text{RDFS}}(G)$. Bao đóng này chứa
các triple suy ra được từ $G$ theo các quy tắc đã áp dụng.

> 🖊 **Tự kiểm tra:** Cho đồ thị gồm: `(Hanoi, capitalOf, Vietnam)`, `(capitalOf, rdfs:domain, City)`, `(capitalOf, rdfs:range, Country)`. Hãy liệt kê tất cả các triple được suy ra bởi forward chaining với quy tắc RDFS domain và range. Giải thích từng bước, chỉ rõ phép thế $\theta$ được dùng. Tại sao kết quả trông "phi lý" nhưng vẫn đúng theo ngữ nghĩa RDFS?

## 5.4 Vật chất hóa và Suy diễn tại thời điểm truy vấn

### Phân biệt cốt lõi

Ở §4.3, chúng ta đã học rằng **suy diễn (entailment) là một quan hệ ngữ nghĩa**: $O \models
\alpha$ nghĩa là $\alpha$ đúng trong mọi mô hình của $O$. Quan hệ này tồn tại độc lập với
bất kỳ hệ thống tính toán nào.

**Vật chất hóa (materialization)** là một *chiến lược triển khai*: tính toán trước bao đóng
và lưu trữ kết quả vào đồ thị. Đây là một cách để *hiện thực hóa* suy diễn, không phải bản
thân khái niệm suy diễn.

```
Suy diễn (entailment)     = quan hệ ngữ nghĩa (abstract)
Vật chất hóa              = chiến lược tính toán trước (precompute + store)
Forward chaining          = thuật toán cụ thể (algorithm)
Suy diễn tại truy vấn     = chiến lược tính toán lazy (compute on demand)
```

### So sánh kỹ thuật: Vật chất hóa vs Truy vấn

| | Vật chất hóa (Materialization) | Suy diễn tại truy vấn (Query-time) |
|---|---|---|
| **Cách hoạt động** | Tính closure trước, lưu kết quả | Lý luận khi trả lời truy vấn |
| **Ưu điểm** | Truy vấn nhanh, dễ kiểm tra derived graph | Không lưu closure, phản ánh đồ thị hiện tại |
| **Nhược điểm** | Tốn bộ nhớ, phải invalidation khi cập nhật | Truy vấn chậm hơn, tính toán lặp lại |
| **Phù hợp khi** | Truy vấn lặp lại, đồ thị ổn định | Đồ thị thay đổi thường xuyên, closure lớn |

Trong thực tế, nhiều hệ thống dùng **chiến lược lai** (hybrid): vật chất hóa một tập con
các hệ quả có giá trị cao (ví dụ: phân cấp lớp), và suy diễn phần còn lại tại thời điểm
truy vấn.

> ⚠ **Phân biệt asserted vs derived:** Khi derived triple được lưu trữ, cần metadata/trạng
> thái phân biệt chúng với asserted triple. Nếu không, việc cập nhật, gỡ lỗi và truy vết
> nguồn gốc trở nên rất khó khăn. Vấn đề provenance đầy đủ sẽ được xử lý ở Chương 6.

### Khi nào vật chất hóa khả thi?

Vật chất hóa hoạt động tốt khi:

- Tập quy tắc đơn điệu và hữu hạn (RDFS, OWL RL subset)
- Đồ thị không quá lớn
- Truy vấn lặp lại nhiều lần (chi phí tính toán một lần, truy vấn nhanh sau đó)

Vật chất hóa trở nên không khả thi khi:

- Ontology quá biểu cảm (xem §5.15 về OWL 2 DL)
- Đồ thị rất lớn (bao đóng có thể lớn hơn nhiều so với đồ thị gốc)
- Dữ liệu thay đổi thường xuyên (phải tính lại bao đóng mỗi lần cập nhật)

> ⚠ **Ngộ nhận thường gặp:** "Bộ suy diễn (reasoner) vật chất hóa tất cả hệ quả." Sai.
> Nhiều reasoner dùng chiến lược lazy (tính theo yêu cầu) hoặc query rewriting. Vật chất
> hóa chỉ là một lựa chọn triển khai.

**Ví dụ trên miền cơ chế.** Giả sử hệ thống Mechanism-KG phục vụ truy vấn
`?m a ex:Mechanism`. Dữ liệu gốc chỉ ghi `ex:rateOfChange_1 a ex:RateOfChangeMechanism` và
`ex:RateOfChangeMechanism rdfs:subClassOf ex:Mechanism`.

- **Vật chất hóa:** Tính closure một lần, lưu `ex:rateOfChange_1 a ex:Mechanism` (và
tương tự cho `ex:heatTransferRate_2`, `ex:newtonCooling_1`). Từ đó truy vấn trở thành một
`SELECT` đơn giản. Phù hợp khi taxonomy ổn định và truy vấn `?m a ex:Mechanism` được lặp
lại liên tục.
- **Suy diễn tại truy vấn:** Không lưu triple suy ra; mỗi lần truy vấn đều chạy RDFS
subClassOf reasoning. Phù hợp khi dữ liệu thay đổi thường xuyên (ví dụ các
`ex:CandidateMechanism` được thêm/xóa liên tục) hoặc khi closure quá lớn so với truy vấn
thực tế.

Nếu hệ thống vừa có `ex:RateOfChangeMechanism` vừa có `ex:CandidateMechanism` (cũng là
subClassOf `ex:Mechanism`), closure sẽ chứa tất cả chúng dưới dạng `ex:Mechanism`. Khi một
candidate bị từ chối và xóa, closure phải được tính lại — đây là chi phí của vật chất hóa
mà hệ thống cần đánh đổi.

## 5.5 Forward vs Backward: Hai chiến lược tính toán

Forward chaining không phải là chiến lược duy nhất. Để hiểu bức tranh đầy đủ, cần so sánh
với **backward chaining** (suy diễn lùi).

### Forward: Tính trước, tra cứu sau

Với câu hỏi "Hanoi có phải là Place không?", forward chaining:

1. Tính closure từ $G_0$: $\text{CapitalCity}(\text{Hanoi}) \to \text{City}(\text{Hanoi}) \to \text{Place}(\text{Hanoi})$
2. Trả lời bằng tra cứu: `Place(Hanoi)` ∈ closure → Yes.

### Backward: Bắt đầu từ câu hỏi, tìm chứng minh

Với cùng câu hỏi "Place(Hanoi)?", backward chaining:

1. **Mục tiêu:** Chứng minh $\text{Place}(\text{Hanoi})$.
2. Tìm quy tắc có head khớp: $r_2: \text{City}(x) \to \text{Place}(x)$ với $\theta = \{x \mapsto \text{Hanoi}\}$.
3. **Mục tiêu con:** Chứng minh $\theta(\text{body}) = \text{City}(\text{Hanoi})$.
4. Tìm quy tắc: $r_1: \text{CapitalCity}(x) \to \text{City}(x)$ với $\theta = \{x \mapsto \text{Hanoi}\}$.
5. **Mục tiêu con:** Chứng minh $\text{CapitalCity}(\text{Hanoi})$.
6. Đây là assertion trong $G_0$ → **Thành công.** Truyền ngược kết quả lên.

### So sánh

| | Forward | Backward |
|---|---|---|
| **Hướng** | Data-driven: từ dữ liệu → kết quả | Goal-driven: từ câu hỏi → chứng minh |
| **Phù hợp khi** | Nhiều truy vấn trên cùng đồ thị | Ít truy vấn, đồ thị lớn |
| **Chi phí** | Tính closure một lần (có thể lớn) | Tính per-query (có thể lặp lại) |
| **Kết quả** | Toàn bộ closure | Chỉ chứng minh cho câu hỏi cụ thể |

> ⚠ **Lưu ý:** Đây là mô hình tinh thần về chiến lược tính toán, không phải mô tả chính
> xác của mọi OWL reasoner. Các reasoner Description Logic thực tế thường dùng thuật toán
> tableau/hypertableau/classification chuyên biệt, không đơn thuần là forward hay backward
> rule engine.

### Cơ chế chạy thực tế: mạng RETE

Đến đây ta mô tả forward chaining như một vòng lặp "quét mọi quy tắc, mọi phép thế". Đó là
định nghĩa ngữ nghĩa; nhưng cài đặt naive thì cực chậm: mỗi vòng lại xét lại mọi quy tắc
trên mọi tổ hợp triple, chi phí cỡ $O(|R| \cdot |G|^{k})$ với $k$ là số mẫu trong body.
Phần lớn công sức đó là lặp lại — những phần của body đã khớp ở vòng trước vẫn còn đúng.

**RETE** (Forgy, 1982 [@forgy-rete-1982]) giải quyết đúng điểm này bằng cách **giữ lại các
phép khớp trung gian** thay vì tính lại từ đầu. Tư tưởng cốt lõi: *đổi bộ nhớ lấy tốc độ*.

Mạng RETE gồm:

- **Mạng alpha (nút một đầu vào):** lọc *bên trong một mẫu* — ví dụ "subject có phải IRI
  không?", "predicate có bằng `ex:capitalOf` không?". Mỗi mẫu của quy tắc đi qua một đường
  alpha riêng; kết quả là các **WME** (Working Memory Element — phần tử bộ nhớ làm việc) đã
  qua lọc.
- **Mạng beta (nút hai đầu vào):** **nối (join)** ràng buộc biến giữa các mẫu khác nhau và
  **cache** các binding trung gian trong **beta memory**. Khi một WME mới vào, chỉ cần nối
  nó với phần đã cache, không tính lại toàn bộ.
- **Agenda + giải quyết xung đột:** khi một quy tắc khớp hoàn toàn, nó được đặt lên
  **agenda** (hàng đợi ưu tiên); cơ chế **giải quyết xung đột** chọn quy tắc nào "bắn" trước
  khi nhiều quy tắc cùng sẵn sàng.

> ℹ **Vì sao RETE nhanh?** Nó khai thác **tính đơn điệu**: một khi nửa phép nối đã đúng,
> thêm fact mới chỉ cần *nối tiếp*, không phá phần cũ. Beta memory chính là hiện thực hóa
> của nhận xét "$\mathrm{lfp}(T_P)$ không phụ thuộc thứ tự" (§5.2) — engine giữ mọi khớp
> trung gian và chỉ tính phần delta.

Đánh đổi: RETE nhanh trên tập quy tắc lớn nhưng **ngốn bộ nhớ** để cache toàn bộ binding
trung gian.

### RETE trong bộ nhớ vs Datalog tăng dần song song

Hai họ engine hiện đại phản ánh hai cách đánh đổi khác nhau:

| | RETE trong bộ nhớ (Drools, Apache Jena) | Datalog tăng dần song song (RDFox) |
|---|---|---|
| **Bản chất** | Mạng alpha/beta cache binding | Vật chất hóa Datalog trên đồ thị nén |
| **Tối ưu cho** | Nhiều quy tắc, điều kiện phong phú | Đồ thị RDF lớn, cập nhật liên tục |
| **Cập nhật** | Tăng dần theo WME | **Tăng dần, song song, lock-free** |
| **Nguồn** | Forgy 1982 [@forgy-rete-1982] | Motik et al. 2014 [@motik-rdfox-2014] |

**RDFox** đại diện cho hướng thứ hai: nó vật chất hóa chương trình Datalog trực tiếp trên đồ
thị RDF nén dạng cột trong bộ nhớ, và — khác với RETE tuần tự — **vật chất hóa tăng dần,
song song, không khóa** (parallel, lock-free incremental materialization) [@motik-rdfox-2014].
Khi một lược đồ thay đổi, nó chỉ tính lại phần closure bị ảnh hưởng thay vì dựng lại từ đầu.
Đây là lý do RDFox xử lý được đồ thị lớn với cập nhật thường xuyên mà vẫn giữ độ trễ thấp.

> ℹ **Cùng một ngữ nghĩa, nhiều chiến lược cài đặt.** Dù là RETE hay Datalog song song, cả
> hai đều phải trả về đúng $\mathrm{lfp}(T_P)$ — tính duy nhất của điểm bất động (§5.2)
> chính là hợp đồng cho phép các engine cạnh tranh về tốc độ mà không đổi kết quả.

## 5.6 SHACL: Xác nhận dữ liệu bằng Shapes

### Mental model: SHACL không phải "OWL closed-world"

Một ngộ nhận phổ biến: "OWL = open world, SHACL = closed world." Cách hiểu này quá đơn
giản và gây hiểu lầm.

Cách hiểu chính xác hơn:

- **OWL** đặt câu hỏi về các diễn giải (interpretations): "Trong mọi mô hình thỏa mãn
  ontology, điều gì đúng?"
- **SHACL** đặt câu hỏi về một đồ thị dữ liệu cụ thể: "Đồ thị dữ liệu *được cung cấp* này
  có thỏa mãn các shapes đã định nghĩa không?"

SHACL không phải OWL với CWA bật lên. SHACL là một framework xác nhận riêng biệt với ngữ
nghĩa và mục đích riêng. Một số SHACL constraints làm cho sự vắng mặt/số lượng trong đồ thị
được cung cấp trở nên có ý nghĩa — điều này *giống* hành vi closed-world ở một số điểm cụ
thể. Nhưng SHACL không đơn giản là OWL + CWA.

### Pipeline SHACL

```
DATA GRAPH
    +
SHAPES GRAPH
    ↓
VALIDATION PROCESS
    ↓
VALIDATION REPORT
    ↓
report.conforms = true/false
+ zero or more ValidationResults
```

SHACL conformance KHÔNG thiết lập chân lý (truth). SHACL violation KHÔNG thiết lập mâu
thuẫn logic (logical inconsistency). Chúng là các phán đoán về cấu trúc dữ liệu được cung
cấp, không phải về ngữ nghĩa model-theoretic.

### Shape là gì?

Một **shape** trong SHACL là một tài nguyên RDF mô tả điều kiện kiểm tra [@w3c-shacl].
Shape không phải là tiên đề ontology — nó không tham gia vào suy diễn RDFS/OWL. Shape chỉ
được dùng bởi engine xác nhận SHACL.

### Cơ chế SHACL: Target → Focus Node → Path → Value Node → Constraint → Result

Để hiểu SHACL thực sự hoạt động thế nào, cần nắm vững chuỗi cơ chế sau. Xét ví dụ:

**Dữ liệu:**

```turtle
ex:Hanoi  rdf:type  ex:City .
```

**Shape:**

```turtle
ex:CityShape
    a sh:NodeShape ;
    sh:targetClass ex:City ;
    sh:property [
        sh:path ex:name ;
        sh:minCount 1
    ] .
```

**Bước 1 — Target:** `sh:targetClass ex:City` chọn các nút candidate. Theo SHACL spec
[@w3c-shacl, §2.1.3.2], target bao gồm tất cả **SHACL instances** của `ex:City`. SHACL
instance đi theo chuỗi `rdfs:subClassOf*`: nếu `CapitalCity rdfs:subClassOf City` và
`Hanoi rdf:type CapitalCity`, thì Hanoi cũng là SHACL instance của City và được target.
(Lưu ý: các khai báo `rdfs:subClassOf` cần thiết phải tồn tại trong data graph.)

**Bước 2 — Focus node:** Mỗi nút được target trở thành một **focus node** — nút đang được
đánh giá. Ở đây: `ex:Hanoi` là focus node.

**Bước 3 — Path:** `sh:path ex:name` xác định property path từ focus node. Engine tìm tất
cả value node reachable từ focus node qua path này.

**Bước 4 — Value nodes:** Tập các nút đích reached từ focus node qua path. Hiện tại: không
có triple `ex:Hanoi ex:name ...` → tập value nodes = ∅ (rỗng).

**Bước 5 — Constraint:** `sh:minCount 1` yêu cầu ít nhất 1 value node. Tập value nodes
rỗng → constraint KHÔNG thỏa mãn.

**Bước 6 — Result:** Violation được tạo ra.

Bây giờ thêm triple:

```turtle
ex:Hanoi  ex:name  "Hà Nội" .
```

Lặp lại bước 3-6: path `ex:name` bây giờ reach được 1 value node (`"Hà Nội"`). `minCount 1`
→ constraint thỏa mãn. Không có violation cho constraint này.

Hình bên dưới trực quan hóa toàn bộ chuỗi cơ chế SHACL từ target đến result. Đọc từ trên
xuống: mỗi bước là một phép biến đổi xác định, không phải suy diễn.

![Cơ chế SHACL: Target → Focus Node → Path → Value Nodes → Constraint → Result. Mỗi bước
là cơ chế xác định. Shape kiểm tra dữ liệu hiện có, không suy ra tri thức mới.](figures/generated/ch05-shacl-mechanism.pdf)

> ⚠ **sh:targetClass KHÔNG phải exact triple grep.** Nó sử dụng SHACL instance semantics,
> bao gồm subclass reasoning qua `rdfs:subClassOf*`. Tương tự, `sh:class C` kiểm tra xem
> value node có phải SHACL instance của C không (qua subclass chain), không chỉ kiểm tra
> `rdf:type C` explicit [@w3c-shacl, §4.1.1].

### Các loại ràng buộc SHACL (tổ chức theo vấn đề)

#### Presence/Cardinality (Sự hiện diện/Số lượng)

| Constraint | Ý nghĩa | Ví dụ |
|------------|---------|-------|
| `sh:minCount n` | Ít nhất n value nodes | Mỗi City có ≥ 1 name |
| `sh:maxCount n` | Tối đa n value nodes | Mỗi City có ≤ 1 capitalOf |

#### Type (Kiểu)

| Constraint | Ý nghĩa | Lưu ý |
|------------|---------|-------|
| `sh:datatype dt` | Value phải có datatype chỉ định | Literal only |
| `sh:class C` | Value phải là SHACL instance của C | Dùng subclass reasoning |
| `sh:nodeKind kind` | Value phải là IRI/BlankNode/Literal | Kiểm tra loại RDF term |

#### Structural (Cấu trúc)

| Constraint | Ý nghĩa | Lưu ý quan trọng |
|------------|---------|---------------------|
| `sh:closed true` | Chỉ cho phép properties được khai báo | KHÔNG biến toàn bộ RDF thành CWA; chỉ áp dụng cho shape này, trên target set này |

#### Logical Composition (Tổ hợp logic)

| Constraint | Ý nghĩa |
|------------|---------|
| `sh:and` | Tất cả shapes con phải thỏa |
| `sh:or` | Ít nhất một shape con thỏa |
| `sh:not` | Shape con phải KHÔNG thỏa |

> ⚠ **sh:closed không phải Closed World Assumption toàn cục.** Nó chỉ reject các property
> không được khai báo *trong phạm vi shape đó*, cho *các focus node được target*. Các phần
> khác của đồ thị không bị ảnh hưởng.

> 🖊 **Tự kiểm tra:** Cho shape yêu cầu `City` có đúng 1 `capitalOf` với range là `Country`.
> Nếu dữ liệu có `(Hanoi, capitalOf, Vietnam)` và `(Hanoi, capitalOf, France)`, báo cáo
> SHACL sẽ nói gì? Nếu dữ liệu có `(Hanoi, capitalOf, "not-a-country")`, báo cáo sẽ nói
> gì? Hai trường hợp khác nhau như thế nào?

**Shape tuyển lựa trên miền cơ chế.** Trong pipeline Mechanism-KG, mỗi cơ chế mới từ một
nguồn thứ hai (Chương 3) đi vào dưới dạng `ex:CandidateMechanism` — chưa được chấp nhận, cần
kiểm tra cấu trúc trước khi xem xét nội dung. Shape sau đây định nghĩa một ứng viên hợp lệ:

```turtle
ex:CandidateMechanismShape
    a sh:NodeShape ;
    sh:targetClass ex:CandidateMechanism ;
    sh:property [
        sh:path ex:hasOperation ;
        sh:minCount 1
    ] ;
    sh:property [
        sh:path ex:hasInput ;
        sh:minCount 1
    ] ;
    sh:property [
        sh:path ex:hasOutput ;
        sh:minCount 1
    ] ;
    sh:property [
        sh:path rdfs:label ;
        sh:datatype xsd:string ;
        sh:minCount 1
    ] .
```

Dữ liệu:

```turtle
ex:candidateRateOfChange_1 a ex:CandidateMechanism ;
    rdfs:label "RATE_OF_CHANGE (draft)" ;
    ex:hasOperation ex:derivativeOperation_1 ;
    ex:hasInput ex:position_1 .
```

Lặp lại chuỗi cơ chế 6 bước cho constraint `hasOutput`:
`sh:targetClass ex:CandidateMechanism` → focus node `ex:candidateRateOfChange_1` →
`sh:path ex:hasOutput` → **value nodes = ∅** (không có triple `hasOutput` nào) →
`sh:minCount 1` không thỏa → violation. Ba constraint còn lại (`hasOperation`,
`hasInput`, `rdfs:label`-datatype) đều thỏa vì dữ liệu có đủ. Kết quả: 1 violation,
`sh:conforms = false`.

> ⚠ **Shape kiểm tra cấu trúc, không kiểm tra chân lý.** Candidate thiếu `ex:hasOutput` có
> thể vẫn là một mô tả đúng về mặt thực tế — chỉ là nó chưa đủ cấu trúc để hệ thống tin
> dùng. Ngược lại, một candidate đủ mọi field vẫn có thể sai về mặt nội dung. Đây chính là
> ranh giới conformance ≠ truth ở §5.8.

## 5.7 Validation Report: Cấu trúc giải phẫu

Khi chạy SHACL validation, engine sản xuất một **validation report** [@w3c-shacl, §3.6]:

```turtle
[
    a sh:ValidationReport ;
    sh:conforms false ;
    sh:result [
        a sh:ValidationResult ;
        sh:focusNode ex:Hanoi ;
        sh:resultPath ex:name ;
        sh:sourceShape ex:CityShape ;
        sh:sourceConstraintComponent sh:MinCountConstraintComponent ;
        sh:resultSeverity sh:Violation ;
        sh:resultMessage "Mỗi City phải có ít nhất một tên" ;
    ]
] .
```

Mỗi ValidationResult trả lời các câu hỏi gỡ lỗi:

| Câu hỏi | Property | Ghi chú |
|---------|----------|---------|
| Nút nào bị lỗi? | `sh:focusNode` | Luôn có |
| Path nào? | `sh:resultPath` | Có thể vắng cho node-level violations |
| Giá trị nào gây lỗi? | `sh:value` | **Chỉ có khi applicable** — ví dụ minCount violation có thể không có value node |
| Shape nào? | `sh:sourceShape` | Shape gây ra constraint |
| Constraint nào? | `sh:sourceConstraintComponent` | Loại constraint bị vi phạm |
| Mức độ? | `sh:resultSeverity` | Violation / Warning / Info |
| Thông báo? | `sh:resultMessage` | Mô tả con người đọc được |

> ⚠ **sh:value không phải lúc nào cũng có.** Với `sh:minCount`, violation xảy ra vì *thiếu*
> value node — không có "giá trị gây lỗi" cụ thể. `sh:value` chỉ xuất hiện khi constraint
> component definition quy định. Đừng fabricate value khi không có.

**Báo cáo cho candidate cơ chế.** Với vi phạm `ex:hasOutput` ở §5.6, validation report sẽ
ghi:

```turtle
[
    a sh:ValidationReport ;
    sh:conforms false ;
    sh:result [
        a sh:ValidationResult ;
        sh:focusNode ex:candidateRateOfChange_1 ;
        sh:resultPath ex:hasOutput ;
        sh:sourceShape ex:CandidateMechanismShape ;
        sh:sourceConstraintComponent sh:MinCountConstraintComponent ;
        sh:resultSeverity sh:Violation ;
        sh:resultMessage "Mỗi CandidateMechanism phải có ít nhất một đầu ra (hasOutput)" ;
    ]
] .
```

Chú ý: `sh:value` **không** xuất hiện trong result này — violation xảy ra vì thiếu value
node, không phải vì một value cụ thể nào sai. Đọc report phải dựa vào `sh:focusNode` +
`sh:resultPath` + `sh:sourceConstraintComponent` để biết *nút nào, path nào, constraint nào*
bị vi phạm.

## 5.8 Phù hợp ≠ Đúng: Ranh giới của xác nhận

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

## 5.9 Nhất quán ≠ Xác nhận: Hai trục độc lập

Sự phân biệt giữa **tính nhất quán OWL** (OWL consistency) và **xác nhận SHACL** (SHACL
validation) là một trong những điểm tinh tế nhất trong thiết kế hệ thống tri thức. Hai
khái niệm này nằm trên hai trục hoàn toàn độc lập.

### Trục 1: Tính nhất quán (Consistency)

**Câu hỏi:** "Có tồn tại ít nhất một mô hình (interpretation) thỏa mãn ontology không?"

Đây là câu hỏi model-theoretic. Nếu ontology + data có ít nhất một model → consistent. Nếu
không có model nào → inconsistent.

### Trục 2: Xác nhận (Validation)

**Câu hỏi:** "Đồ thị dữ liệu được cung cấp có thỏa mãn các shapes đã định nghĩa không?"

Đây là câu hỏi về cấu trúc dữ liệu cụ thể, không phải về sự tồn tại của mô hình.

### Trường hợp A: OWL-inconsistent nhưng SHACL-conformant

Ontology khai báo:

```
City owl:disjointWith Country
```

Dữ liệu:

```
Hanoi rdf:type City .
Hanoi rdf:type Country .
Hanoi ex:name "Hà Nội" .
```

**OWL:** Inconsistent — Hanoi không thể vừa là City vừa là Country nếu hai lớp disjoint.
Không có model nào thỏa mãn.

**SHACL:** Giả sử shapes chỉ yêu cầu "City có name" và "Country có name". Hanoi có `ex:name`
→ shapes thỏa mãn → **conforms = true**.

SHACL không biết về `owl:disjointWith`. Nó chỉ kiểm tra shapes được cung cấp.

### Trường hợp B: OWL-consistent nhưng SHACL-invalid

Dữ liệu:

```
Hanoi rdf:type City .
```

(Không có triple `ex:name` nào cho Hanoi.)

**OWL (OWA):** Perfectly consistent. Dưới Open World Assumption, Hanoi *có thể* có một name
nào đó mà chúng ta chưa biết. Không có mâu thuẫn.

**SHACL:** Shape yêu cầu `sh:minCount 1` trên `ex:name` cho City. Không có value node →
**violation**.

OWL nói "có thể có name" (không mâu thuẫn). SHACL nói "trong đồ thị được cung cấp, không có
name" (vi phạm). Cả hai đều đúng — chúng trả lời các câu hỏi khác nhau.

### Bảng tóm tắt

Hình bên dưới minh họa bốn tổ hợp có thể của hai trục độc lập. Mỗi ô đều có thể xảy ra trong
thực tế — không có ô nào bị loại trừ.

![Nhất quán (OWL) × Xác nhận (SHACL): bốn tổ hợp đều có thể xảy ra. Hai trục hoàn toàn
độc lập — biết một không suy ra cái kia.](figures/generated/ch05-consistency-vs-validation.pdf)

| | OWL Consistent | OWL Inconsistent |
|---|---|---|
| **SHACL conforms** | ✅ Bình thường | ⚠️ Có thể xảy ra (shapes không cover axiom) |
| **SHACL violates** | ⚠️ Có thể xảy ra (OWA vs data-check) | ⚠️ Có thể xảy ra |

> ⚠ **Bài học:** Consistency và conformance là hai trục độc lập. Biết một không suy ra cái
> kia. Hệ thống tri thức hoàn chỉnh cần cả hai: OWL để đảm bảo ontology nhất quán, SHACL để
> đảm bảo dữ liệu tuân thủ cấu trúc kỳ vọng.

> 🖊 **Tự kiểm tra:** Giải thích tại sao OWL existential restriction `City ⊑ ∃hasName.xsd:string`
> KHÔNG gây ra violation khi Hanoi là City nhưng không có hasName, trong khi SHACL
> `sh:minCount 1` trên hasName LẠI gây violation. Sự khác biệt nằm ở đâu?

**Hai trục trên miền cơ chế.** Cùng phân tích cú pháp, nhưng dùng dữ liệu Mechanism-KG.

*Trường hợp A — OWL-inconsistent nhưng SHACL-conformant.* Ontology khai báo
`ex:ChangeMechanism owl:disjointWith ex:AggregationMechanism`. Dữ liệu ghi:

```
ex:someMechanism_9 a ex:ChangeMechanism .
ex:someMechanism_9 a ex:AggregationMechanism .
ex:someMechanism_9 ex:hasOperation ex:someOperation_1 .
```

- **OWL:** không nhất quán — một cá thể không thể thuộc hai lớp disjoint (§4.9).
- **SHACL:** shape chỉ kiểm tra cấu trúc (có `ex:hasOperation`, có label) → **conforms**.
  SHACL không đọc `owl:disjointWith`, nó không biết hai lớp này xung đột.

*Trường hợp B — OWL-consistent nhưng SHACL-violating.* Dữ liệu chỉ có:

```
ex:candidateRateOfChange_1 a ex:CandidateMechanism .
```

- **OWL (OWA):** nhất quán — thiếu `ex:hasOutput` không gây mâu thuẫn (§4.8).
- **SHACL:** `CandidateMechanismShape` yêu cầu `sh:minCount 1` trên `ex:hasOutput` →
  **violation**.

Bảng 2×2 vẫn giữ nguyên ý nghĩa: biết tính nhất quán OWL không cho biết kết quả xác nhận
SHACL, và ngược lại. Hệ thống Mechanism-KG cần cả hai trục: ontology để phát hiện lỗi mô
hình hóa (disjoint bị vi phạm), shapes để chặn candidate thiếu cấu trúc trước khi đưa vào
kho tri thức.

## 5.10 Shapes ≠ Axioms: Phân biệt SHACL và Ontology

Sự phân biệt giữa SHACL và ontology là một trong những ranh giới quan trọng nhất trong
thiết kế hệ thống tri thức:

| | Ontology (RDFS/OWL) | SHACL Shapes |
|---|---|---|
| **Mục đích** | Định nghĩa điều gì suy ra được | Định nghĩa điều gì được phép |
| **Cơ sở** | Model-theoretic statements về interpretations | Validation của data graph cụ thể |
| **Kết quả** | Entailments (triple mới) | Validation report (conforms/violation) |
| **Tham gia suy diễn** | Có | Không |
| **Ví dụ** | `rdfs:domain` suy ra rdf:type | `sh:class` kiểm tra rdf:type |

Cùng từ vựng (`class`, `property`, `datatype`), nhưng ngược hướng:

- `P rdfs:domain C` + `(x, P, y)` → suy ra `x rdf:type C` (thêm thông tin)
- `sh:property [ sh:path P ; sh:class C ]` + `(x, P, y)` → kiểm tra `y` có phải SHACL instance của C không (kiểm tra thông tin)

**Ba vai trò khác nhau: quy tắc, tiên đề, shape.** Cùng một tri thức miền cơ chế có thể
được thể hiện theo ba cách với ba ngữ nghĩa khác nhau — đừng trộn lẫn:

| Vai trò | Ví dụ cùng tuyên bố "Mechanism phải có Operation" | Điều gì xảy ra khi dữ liệu thiếu `hasOperation`? |
|---------|----------------------------------------------------|--------------------------------------------------|
| **Quy tắc (rule)** | `Mechanism(x) ∧ hasOperation(x, op) → Operation(op)` (Horn rule, §5.2) | Suy ra `Operation(op)` khi có đủ bằng chứng; không phàn nàn gì khi thiếu |
| **Tiên đề OWL (axiom)** | `Mechanism ⊑ ∃hasOperation.Operation` (§4.13) | Không mâu thuẫn — OWA giả định filler không tên tồn tại |
| **Shape SHACL (shape)** | `sh:path ex:hasOperation ; sh:minCount 1` (§5.6) | Báo **violation** — dữ liệu được cung cấp thiếu cấu trúc kỳ vọng |

Quy tắc **thêm** tri thức, tiên đề **ràng buộc ngữ nghĩa model-theoretic**, shape **kiểm tra
cấu trúc dữ liệu cụ thể**. Việc phân biệt ai làm gì quyết định thiết kế đúng của hệ thống.

### OWL Existential Restriction vs SHACL minCount

Đây là ví dụ phân biệt mạnh nhất:

**OWL:** `City ⊑ ∃hasName.xsd:string`

Nghĩa là: "Trong mọi model, mỗi City phải có *ít nhất một* hasName-successor." Nhưng dưới
OWA, nếu dữ liệu không có hasName cho Hanoi, OWL *không* tạo ra inconsistency — nó chỉ giả
định rằng có một unnamed witness tồn tại trong model.

**SHACL:** `sh:path ex:name ; sh:minCount 1`

Nghĩa là: "Trong đồ thị dữ liệu *được cung cấp*, focus node phải có ít nhất 1 value node
qua path ex:name." Nếu không có → violation.

OWL nói về models. SHACL nói về data graph cụ thể. Cùng yêu cầu "có name", nhưng ngữ nghĩa
hoàn toàn khác.

> ⚠ **Không thay thế lẫn nhau.** Ontology không thay thế được SHACL cho việc kiểm tra dữ
> liệu. SHACL không thay thế được ontology cho việc suy diễn tri thức. Hệ thống tri thức
> hoàn chỉnh thường cần cả hai.

### SHACL là kiểm tra phi đơn điệu: Local Closed-World Semantics

Bảng trên cho thấy shape *kiểm tra* chứ không *suy diễn*. Nhưng có một tính chất sâu hơn
giải thích **vì sao** SHACL hành xử khác ontology: SHACL dùng **ngữ nghĩa thế giới đóng cục
bộ** (Local Closed-World Semantics, LCWA) và vì thế là một ngôn ngữ ràng buộc **phi đơn
điệu** (non-monotonic).

- **Mở thế giới (OWA) — phía ontology:** không thấy triple `hasOperation` ⇒ *chưa biết* có
  hay không; có thể tồn tại một witness vô danh (§4.8, §5.10). Thêm dữ liệu không bao giờ làm
  mất kết luận đã suy ra — **đơn điệu**.
- **Đóng thế giới cục bộ (LCWA) — phía SHACL:** với mỗi focus node, những gì *không có* trong
  đồ thị được coi là *không tồn tại* đối với node đó. Thiếu value node ⇒ violation ngay.

Hệ quả trực tiếp: **thêm triple có thể biến một đồ thị đang conform thành vi phạm.** Xét
shape `sh:maxCount 1` trên `ex:hasReferenceVariable`:

```turtle
# Trước: conform
ex:roc_1  ex:hasReferenceVariable  ex:time_1 .

# Sau khi THÊM một triple: VI PHẠM (vượt maxCount 1)
ex:roc_1  ex:hasReferenceVariable  ex:time_1 .
ex:roc_1  ex:hasReferenceVariable  ex:temp_2 .
```

Hành vi "thêm thông tin làm mất kết luận cũ" chính là **tính phi đơn điệu** — đối lập với
forward chaining ở §5.2. Đây là cùng bản chất với *negation as failure* (§5.16): SHACL diễn
dịch "không tìm thấy" thành "không tồn tại", và phép diễn dịch đó không đơn điệu.

> ℹ **Vì sao "cục bộ"?** SHACL không đóng cả thế giới một cách mù quáng như CWA cổ điển
> (Reiter 1978). Nó chỉ đóng *trong phạm vi từng focus node và từng constraint*: sự vắng mặt
> chỉ bị tính là vi phạm khi một shape cụ thể yêu cầu sự hiện diện. Ngoài phạm vi đó, OWA vẫn
> có hiệu lực.

## 5.11 Suy diễn trước Xác nhận: Tương tác giữa hai pipeline

Kết quả xác nhận SHACL phụ thuộc vào đồ thị nào được đưa vào validator. Đây là một quyết
định kiến trúc quan trọng:

### Kiến trúc A: Xác nhận trực tiếp

```
asserted graph → SHACL validator → report
```

Validator chỉ thấy dữ liệu asserted. Derived triples không được xét.

### Kiến trúc B: Suy diễn trước, xác nhận sau

```
asserted graph → RDFS/OWL materialization → expanded graph → SHACL validator → report
```

Validator thấy cả asserted + derived triples. Ví dụ: nếu RDFS suy ra `Hanoi rdf:type City`,
thì SHACL shapes targeting City sẽ áp dụng lên Hanoi.

### Kiến trúc C: Validator tích hợp entailment

```
asserted graph → SHACL processor (configured with entailment support) → report
```

Một số SHACL processors hỗ trợ cấu hình entailment/preprocessing. Không phải tất cả SHACL
processors tự động thực hiện OWL reasoning.

> ⚠ **Quan trọng:**
>
> - KHÔNG giả định tất cả SHACL processors tự động suy diễn RDFS/OWL.
> - KHÔNG giả định SHACL luôn bỏ qua inference.
> - Kiến trúc cụ thể là quyết định triển khai, phải được document rõ.

Hệ thống production nên ghi rõ:

```
asserted graph        = dữ liệu gốc
inferred graph        = kết quả suy diễn (nếu có)
effective validation graph = đồ thị thực sự được validate
entailment regime     = chế độ suy diễn được áp dụng (nếu có)
```

> ⚠ **Effective validation graph** là đồ thị mà validator thực sự nhìn thấy. Nó có thể là
> asserted graph, expanded graph, hoặc một biến thể khác tùy kiến trúc. Hiểu sai về effective
> validation graph là nguồn gốc của nhiều bug tinh vi trong hệ thống tri thức.

## 5.12 Vi phạm ≠ Sửa chữa: Cơ chế Graph Repair

SHACL báo cáo: "Biểu diễn hiện tại vi phạm yêu cầu X." Nó KHÔNG xác định phép biến đổi nào
là đúng về mặt tri thức (epistemically correct).

### Ví dụ: Hanoi thiếu ex:name

Violation: `ex:Hanoi` thiếu `ex:name` (minCount 1).

Các candidate repairs:

| Repair | Hành động | Hệ quả ngữ nghĩa |
|--------|-----------|---------------------|
| A | Thêm `ex:Hanoi ex:name "Hà Nội"` | Bổ sung thông tin — đúng nếu tên thực sự là "Hà Nội" |
| B | Xóa `ex:Hanoi rdf:type ex:City` | Thay đổi phân loại — đúng nếu Hanoi không phải City |
| C | Thay đổi shape (bỏ minCount) | Thay đổi yêu cầu — đúng nếu yêu cầu quá nghiêm ngặt |
| D | Đánh dấu bản ghi incomplete, từ chối ingestion | Từ chối dữ liệu — đúng nếu nguồn không đáng tin |
| E | Resolve identity với nguồn khác, import name | Tích hợp nguồn — đúng nếu có nguồn bổ sung |

Tất cả đều có thể làm SHACL xanh. Nhưng chỉ domain knowledge, bằng chứng, và governance mới
quyết định repair nào là đúng.

### Pipeline repair

Hình bên dưới minh họa pipeline repair như một bài toán quyết định: từ violation đến nhiều
candidate repairs, qua đánh giá ngữ nghĩa/tri thức, rồi chọn repair phù hợp. Lưu ý thông điệp
phía dưới: passes validation ≠ becomes true.

![Pipeline Graph Repair: Violation → Candidate Repairs (ADD/DELETE/SHAPE CHANGE/REJECT) →
Evaluate semantic + epistemic consequences → Select repair → Apply + Revalidate. Passes
validation ≠ becomes true.](figures/generated/ch05-repair-pipeline.pdf)

```
Violation
    ↓
Candidate Repairs (nhiều lựa chọn)
    ↓
Evaluate semantic + epistemic consequences
    ↓
Select repair (dựa trên domain knowledge/governance)
    ↓
Apply repair → Revalidate
```

### Các loại repair operation

- **ADD:** Thêm statement còn thiếu
- **DELETE:** Xóa statement gây vi phạm
- **RECLASSIFY / REMODEL:** Thay đổi type hoặc cấu trúc đồ thị
- **SHAPE CHANGE:** Thay đổi yêu cầu thay vì dữ liệu

> ⚠ **Repairing data để SHACL xanh CÓ THỂ thay đổi ngữ nghĩa dự định.** Do đó repair là bài
> toán quyết định (decision problem), không chỉ là vá lỗi cú pháp.
>
> $$\text{passes validation} \neq \text{becomes true}$$

Đây là cầu nối trực tiếp đến Chương 6: khi nào dữ liệu trở thành tri thức đáng tin? Ai có
thẩm quyền quyết định repair? Bằng chứng nào hỗ trợ?

**Ví dụ trên miền cơ chế.** Candidate `ex:candidateRateOfChange_1` thiếu `ex:hasOutput`
(§5.6). Các candidate repairs:

| Repair | Hành động | Hệ quả | Cơ sở quyết định |
|--------|-----------|--------|------------------|
| A | Thêm `ex:hasOutput ex:velocity_1` | Bổ sung thông tin — đúng nếu candidate thực sự tính velocity | Nguồn thứ hai (textbook B) xác nhận output; bằng chứng mạnh |
| B | Thêm `ex:hasOutput ex:unknownOutput_1` | Bổ sung placeholder — làm SHACL xanh nhưng không có giá trị tri thức | Không có bằng chứng; chỉ che vi phạm |
| C | Xóa `ex:candidateRateOfChange_1 a ex:CandidateMechanism` | Loại candidate khỏi pipeline — mất thông tin từ nguồn thứ hai | Nguồn không đáng tin; quyết định governance |
| D | Sửa shape: `hasOutput` sh:minCount 0 | Shape dễ tính hơn — nhưng chấp nhận candidate không có output | Yêu cầu nghiệp vụ cho phép candidate chưa hoàn chỉnh |

Chỉ (A) là repair có ý nghĩa tri thức — nó dựa trên bằng chứng từ nguồn thứ hai, không chỉ
"làm SHACL xanh" như (B). (C) từ chối dữ liệu, (D) thay đổi shape — đều hợp lệ trong các
ngữ cảnh khác nhau. Quyết định thuộc về domain governance, không phải SHACL engine.

## 5.13 Tính đúng đắn và Tính đầy đủ

Khi đánh giá một hệ thống suy diễn, hai tính chất quan trọng nhất là **soundness** (tính
đúng đắn) và **completeness** (tính đầy đủ). Nhưng cả hai đều vô nghĩa nếu không ghi rõ
phạm vi.

### Mô hình tập hợp

Gọi:

- $E$ = tập tất cả hệ quả ngữ nghĩa theo chế độ suy diễn đã chọn (entailed conclusions)
- $A$ = tập kết quả mà thuật toán trả về

**Sound:** $A \subseteq E$

Thuật toán không trả về kết quả sai (false positive). Mọi thứ nó suy ra đều là entailment
hợp lệ.

**Complete:** $E \subseteq A$

Thuật toán không bỏ sót kết quả (false negative). Mọi entailment hợp lệ đều được suy ra.

**Sound + Complete:** $A = E$

Thuật toán trả về chính xác tập hệ quả ngữ nghĩa — không thừa, không thiếu.

Hình bên dưới minh họa ba trường hợp bằng sơ đồ tập hợp. Sound nhưng incomplete: $A$ nằm
trong $E$ nhưng không phủ hết. Unsound: $A$ tràn ra ngoài $E$ (false positive). Sound +
complete: $A = E$ hoàn hảo.

![Soundness và Completeness như quan hệ tập hợp. Trái: sound nhưng incomplete ($A \subseteq
E$, bỏ sót). Giữa: unsound ($A \not\subseteq E$, có false positive). Phải: sound + complete
($A = E$, chính xác).](figures/generated/ch05-soundness-completeness.pdf)

### Ba thành phần bắt buộc

Mọi khẳng định về soundness/completeness PHẢI ghi rõ ba thành phần:

1. **Ngôn ngữ/hồ sơ** (language/profile): RDFS? OWL EL? OWL RL? OWL 2 DL đầy đủ?
2. **Chế độ suy diễn** (entailment regime): Direct Semantics? RDF-Based? Simple?
3. **Tác vụ suy luận** (reasoning task): Consistency checking? Subsumption? Instance checking? Conjunctive query answering?

Ví dụ đúng: "Forward chaining với tập quy tắc OWL RL là sound và complete cho tác vụ
instance checking trên ontology OWL 2 RL thỏa mãn các hạn chế syntactic của profile."

Ví dụ sai: "Reasoner X là sound và complete." (Thiếu cả ba thành phần.)

### Ba trường hợp trên dữ liệu cơ chế thật

Trừu tượng "$A \subseteq E$" chỉ trọn nghĩa khi thấy A và E *cụ thể*. Dùng chính dữ liệu
RATE_OF_CHANGE từ §5.2:

```
G0 (dữ liệu khai báo):
ex:rateOfChange_1 a ex:RateOfChangeMechanism .
ex:RateOfChangeMechanism rdfs:subClassOf ex:ChangeMechanism .
ex:ChangeMechanism rdfs:subClassOf ex:Mechanism .
```

Chế độ suy diễn: RDFS, tác vụ: instance classification. Tập hệ quả ngữ nghĩa
$E = \{ \texttt{rateOfChange\_1 a ChangeMechanism},\ \texttt{rateOfChange\_1 a Mechanism} \}$
— đây là *chuẩn* mà mọi thuật toán được so vào.

**CASE 1 — Sound nhưng incomplete ($A \subset E$).** Thuật toán, do thiếu quy tắc
`ChangeMechanism rdfs:subClassOf Mechanism` (hoặc quên nạp tầng taxonomy), chỉ suy ra một
bước:

```
A = { rateOfChange_1 a ChangeMechanism }
```

Mọi phần tử của A đều nằm trong E (sound ✓) nhưng bỏ sót `rateOfChange_1 a Mechanism`
(not complete ✗). Kết luận nào cũng đúng, chỉ là hệ thống trả lời thưa hơn mức có thể.

**CASE 2 — Unsound ($A \not\subseteq E$).** Quy tắc bị viết sai: `RateOfChangeMechanism
rdfs:subClassOf AggregationMechanism` (nhầm nhánh taxonomy). Thuật toán suy ra:

```
A = { rateOfChange_1 a ChangeMechanism,
      rateOfChange_1 a Mechanism,
      rateOfChange_1 a AggregationMechanism }   ← false positive!
```

`rateOfChange_1 a AggregationMechanism` nằm ngoài E — một kết luận *sai ngữ nghĩa*.
Đây là lỗi nghiêm trọng nhất của ba trường hợp (xem "Ý nghĩa kỹ thuật" bên dưới).

**CASE 3 — Sound + Complete ($A = E$).** Bộ quy tắc đầy đủ và đúng đắn:

```
A = { rateOfChange_1 a ChangeMechanism, rateOfChange_1 a Mechanism } = E
```

Không thừa, không thiếu — thuật toán trả về chính xác tập hệ quả.

### Ý nghĩa kỹ thuật cho hệ thống tri thức

- **Unsound nguy hiểm hơn incomplete.** Một kết luận sai (false positive) sẽ *lan truyền*
  vào mọi truy vấn phía sau: nếu hệ thống tin `rateOfChange_1` là `AggregationMechanism`,
  nó có thể trả về cơ chế này cho câu hỏi "cơ chế nào gộp nhiều đầu vào?" — câu trả lời
  sai nhưng trông hợp lệ. Incomplete chỉ gây "không có kết quả" — người dùng thấy được,
  còn unsound tạo ra kết quả sai mà không ai hay.
- **Khi buộc chọn, ưu tiên sound-not-complete cho KG.** Một knowledge graph trả lời
  "không suy ra được" có thể được cải thiện (thêm quy tắc, thêm dữ liệu); một KG trả về
  khẳng định sai sẽ phá hủy lòng tin ngay lập tức.
- **Incomplete thường là phí cố ý.** OWL RL đánh đổi completeness để lấy tính khả thi
  của rule-based reasoning (mục sau); chi phí là *trả lời thưa*, lợi ích là dừng được và
  chạy trên rule engine thông thường.
- **Kiểm chứng thực nghiệm.** Với tác vụ đơn giản như classification, có thể kiểm chứng
  CASE 1/3 bằng cách chạy forward chaining (công cụ như RDFLib) và so A với E liệt kê
  thủ công — nhưng với tác vụ khó hơn, "complete" là kết quả lý thuyết (theorem), không
  phải thứ đo được bằng test.

### OWL RL: Sound nhưng completeness có điều kiện

OWL 2 RL là profile được thiết kế để tương thích với rule-based reasoning
[@w3c-owl2-profiles]. W3C đưa ra kết quả tương ứng (correspondence result) dưới dạng
**Theorem PR1** [@w3c-owl2-profiles, §4.3]:

Với các ontology OWL 2 RL thỏa mãn các hạn chế syntactic của profile, forward chaining
với tập quy tắc OWL RL/RDF trả về *tất cả và chỉ* các kết quả đúng cho các loại truy vấn
nhất định.

Tuy nhiên, trên **đồ thị RDF tùy ý** (arbitrary RDF graphs), completeness không được đảm
bảo: "it is no longer possible to guarantee that all correct answers can be returned."
Forward chaining vẫn sound — chỉ trả về entailment hợp lệ — nhưng có thể bỏ sót.

Các hạn chế cụ thể:

- OWL RL disallows `DisjointUnion`, `ReflexiveObjectProperty`
- Class expressions bị giới hạn theo Table 2 của spec
- Negation, existential quantification phức tạp, counting nằm ngoài phạm vi quy tắc Horn

> ⚠ **Không nói:** "OWL RL forward chaining là complete cho mọi đồ thị RDF."
> **Không nói:** "OWL RL là complete cho các quy tắc RL" (tautological).
> **Nói:** "OWL RL forward chaining là sound; complete dưới các điều kiện syntactic cụ thể
> được nêu trong W3C OWL 2 Profiles spec, Theorem PR1."

> 🖊 **Tự kiểm tra:** Giải thích tại sao một hệ thống forward chaining dùng quy tắc OWL RL
> có thể bỏ sót một số entailment OWL 2 DL. Cho ví dụ cụ thể về loại entailment mà quy
> tắc Horn không thể nắm bắt. (Gợi ý: nghĩ về existential restriction và unnamed witnesses.)

## 5.14 Chế độ suy diễn (Entailment Regime)

Cùng một đồ thị RDF, các chế độ suy diễn khác nhau cho kết quả khác nhau:

| Regime | Mô tả | Mức độ suy diễn |
|--------|-------|-----------------|
| Simple | Chỉ RDF cơ bản, không RDFS | Tối thiểu |
| RDFS | Thêm subClassOf, subPropertyOf, domain, range | Trung bình |
| OWL RL | Thêm quy tắc OWL tương thích rule engine | Cao (trong phạm vi RL) |
| OWL Direct | Ngữ nghĩa Description Logic đầy đủ (OWL 2 DL) | Cao nhất (trong DL) |
| OWL RDF-Based | Ngữ nghĩa trực tiếp trên RDF graph (OWL 2 Full) | Cao nhất (undecidable) |

Khi nói "$G \models \alpha$", luôn phải hỏi: $\models$ theo regime nào?

### SPARQL và Entailment Regime

Theo SPARQL 1.1 Entailment Regimes [@w3c-sparql11-entailment], chế độ suy diễn được chỉ
định qua **SPARQL Service Description**, không phải qua mệnh đề `FROM`:

- `sd:defaultEntailmentRegime` — chế độ mặc định của endpoint
- `sd:entailmentRegime` — chế độ cho một named graph cụ thể

Mệnh đề `FROM` trong SPARQL chọn đồ thị/dataset, **không** chọn chế độ suy diễn. Đây là hai
cơ chế độc lập.

Các regime IRI chuẩn:

- RDF: `http://www.w3.org/ns/entailment/RDF`
- RDFS: `http://www.w3.org/ns/entailment/RDFS`
- OWL Direct: `http://www.w3.org/ns/entailment/OWL-Direct`
- OWL RDF-Based: `http://www.w3.org/ns/entailment/OWL-RDF-Based`

**Ví dụ so sánh trên miền cơ chế.** Cùng một truy vấn, hai chế độ suy diễn, hai kết quả khác
nhau:

```sparql
PREFIX ex: <http://example.org/kgbook/mks#>
SELECT ?m WHERE { ?m a ex:Mechanism }
```

Dữ liệu gốc chứa `ex:rateOfChange_1 a ex:RateOfChangeMechanism` và
`ex:RateOfChangeMechanism rdfs:subClassOf ex:ChangeMechanism` và
`ex:ChangeMechanism rdfs:subClassOf ex:Mechanism`.

| Regime | Kết quả | Giải thích |
|--------|---------|------------|
| **Simple** | ∅ (rỗng) | Chỉ khớp triple `?m a ex:Mechanism` tường minh — không có ai được gõ trực tiếp là `ex:Mechanism` |
| **RDFS** | `rateOfChange_1`, `heatTransferRate_2`, `newtonCooling_1` | RDFS subClassOf suy diễn từ RateOfChangeMechanism → ChangeMechanism → Mechanism |

Đây là minh họa thực tế cho thấy: cùng một câu hỏi SPARQL, lựa chọn entailment regime quyết
định kết quả. Nếu không xác định regime, developer có thể nhận được ∅ và nghĩ "không có cơ
chế nào trong đồ thị" — trong khi thực tế có 3 cơ chế, chỉ là chưa kích hoạt RDFS reasoning.

> ⚠ **Không nói:** "SPARQL engines thường mặc định dùng X." Hành vi mặc định là tùy triển
> khai, không phải chuẩn. Luôn kiểm tra Service Description của endpoint cụ thể.

## 5.15 OWL 2 DL và Giới hạn của Vật chất hóa

General OWL 2 DL reasoning không thể được hiểu đơn giản là "lặp lại việc thêm mọi entailed
RDF triple cho đến khi không còn triple mới." Lý do:

- **Ngữ nghĩa existential:** OWL 2 DL có thể đòi hỏi sự tồn tại của unnamed witnesses trong
  models — các cá thể không có tên trong đồ thị RDF. Những witness này không thể được biểu
  diễn như RDF triple hữu hạn.

- **Model structures:** Cấu trúc mô hình OWL 2 DL có thể không tương ứng với một đồ thị RDF
  hữu hạn được vật chất hóa rõ ràng.

- **Thuật toán chuyên biệt:** Các DL reasoner thực tế thường dùng tableau, hypertableau,
  hoặc classification procedures — không phải naive triple closure.

> ⚠ **Bài học:** Formal entailment KHÔNG ngụ ý rằng finite RDF-triple materialization
> luôn là mô hình tính toán đúng. Đối với OWL 2 DL đầy đủ, vật chất hóa toàn bộ closure
> có thể không khả thi hoặc không đúng về mặt ngữ nghĩa.

## 5.16 Quy tắc Horn và SWRL

### Quy tắc Horn trong KG

Quy tắc Horn (Horn clause) có dạng:

$$\text{head} \leftarrow \text{body}_1 \land \text{body}_2 \land \dots \land \text{body}_n$$

Trong ngữ cảnh KG, head và body là các mẫu triple (triple patterns) với biến. Ví dụ:

$$\text{sisterCity}(y, x) \leftarrow \text{sisterCity}(x, y)$$

"Nếu x là sister city của y, thì y là sister city của x."

Quy tắc Horn có các tính chất quan trọng:

- **Đơn điệu:** Thêm thông tin vào đồ thị chỉ mở rộng tập kết quả, không thu hẹp
- **Dừng được:** Trên đồ thị hữu hạn với các điều kiện an toàn (§5.2), forward chaining luôn dừng
- **Giới hạn biểu diễn:** Không thể biểu diễn phủ định (negation), phép hoặc (disjunction) trong head, hoặc lượng từ tồn tại (existential quantification) trong head

Các quy tắc Horn an toàn, không hàm ở §5.2 chính xác là **Datalog**; khảo cứu *Datalog and
Recursive Query Processing* [@datalog-survey-2013] là tài liệu chuẩn về ngữ nghĩa điểm bất động
và các chiến lược đánh giá của chúng.

### Datalog và ba ngữ nghĩa tương đương

Khi bỏ hàm (function-free) và yêu cầu mọi biến trong head phải xuất hiện ở body
(**safeness** / range-restriction), quy tắc Horn trở thành **Datalog**:

$$A \leftarrow B_1, \dots, B_n$$

với $A$ (head) và mỗi $B_i$ (body) là công thức nguyên tử $P(t_1, \dots, t_k)$. Safeness đảm
bảo mỗi phép thế chỉ dùng giá trị đã có trong đồ thị, nên forward chaining dừng (§5.2).

Datalog có **ba cách định nghĩa "chương trình $P$ trên cơ sở dữ liệu $D$ có nghĩa là gì"**,
và định lý nền tảng của lý thuyết Datalog khẳng định cả ba cho **cùng một tập fact**
[@abiteboul-foundations-1995]:

1. **Ngữ nghĩa mô hình (model-theoretic):** ý nghĩa của $P$ là **mô hình Herbrand tối tiểu**
   $\mathcal{M}(P)$ — giao của mọi mô hình Herbrand thỏa $P$ và chứa $D$. (Một *mô hình
   Herbrand* là một cách gán đúng/sai cho mọi ground atom sao cho mọi quy tắc của $P$ đều
   đúng.)
2. **Ngữ nghĩa chứng minh (proof-theoretic):** tập mọi ground fact **derivable** bằng các cây
   chứng minh hữu hạn (quy nạp lùi qua các quy tắc).
3. **Ngữ nghĩa điểm bất động (fixpoint):** $\mathrm{lfp}(T_P)$ — chính là bao đóng forward
   chaining ở §5.2.

$$\mathcal{M}(P) \;=\; \{\text{fact derivable}\} \;=\; \mathrm{lfp}(T_P)$$

> ℹ **Vì sao ba mà một?** Đây là định lý Knaster–Tarski hợp với tính chất Horn: với quy tắc
> Horn đơn điệu, "đúng trong mô hình nhỏ nhất", "có chứng minh", và "đạt được qua lặp $T_P$"
> trùng nhau. Nhờ đó ta *chọn* góc nhìn thuận tiện: chứng minh tính đúng đắn bằng mô hình,
> cài đặt bằng fixpoint, giải thích bằng cây chứng minh.

**Độ phức tạp.** Datalog có **data complexity PTIME-đầy đủ** (chương trình cố định, dữ liệu
lớn dần) và **combined complexity EXPTIME-đầy đủ** (chương trình và dữ liệu cùng biến)
[@abiteboul-foundations-1995]. Khoảng cách lớn giữa hai con số giải thích vì sao Datalog thực
dụng: với một bộ quy tắc đã chốt, chi phí suy diễn chỉ đa thức theo kích thước dữ liệu.

### Phủ định cổ điển vs Phủ định dạng thất bại (NAF)

Horn/Datalog thuần **không có phủ định**. Khi muốn nói "không có bằng chứng cho $q$ thì kết
luận $\neg q$", ta đứng trước hai loại phủ định hoàn toàn khác nhau:

| | Phủ định cổ điển $\neg$ | Negation as Failure $\sim$ (`not`) |
|---|---|---|
| **Giả định thế giới** | Mở (OWA) | Đóng (CWA) |
| **Khi nào kết luận $\neg q$ / $\sim q$** | Cần chứng minh $\neg q$ hoặc tiên đề rời nhau | Chỉ vì $q$ **không chứng minh được** từ dữ liệu hiện có |
| **Đơn điệu?** | **Có** — thêm fact không rút lại kết luận | **Không** — thêm fact có thể làm $q$ chứng minh được, kéo theo $\sim q$ bị rút lại |

Sự **phi đơn điệu** của NAF là con dao hai lưỡi. Nó cho phép suy luận kiểu "nếu không thấy gì
nói khác đi thì coi là sai" (rất hợp với dữ liệu dạng cơ sở dữ liệu), nhưng nó phá vỡ tính
duy nhất của mô hình. Ví dụ kinh điển — một chương trình **không phân tầng**:

$$p \leftarrow \text{not } q \qquad\qquad q \leftarrow \text{not } p$$

Chương trình này có **hai** mô hình tối tiểu: $\{p\}$ và $\{q\}$. Hệ thống nên chọn cái nào?
Không có cơ sở đơn điệu nào để ưu tiên một trong hai — kết quả phụ thuộc thứ tự chạy, và ngữ
nghĩa trở nên nhập nhằng.

### Datalog phân tầng (Stratified Datalog)

Giải pháp chuẩn là **phân tầng**: chia các vị từ của chương trình thành các tầng
$P_1, \dots, P_n$ sao cho nếu một quy tắc ở tầng $i$ chứa $\text{not } q$ trong body, thì mọi
quy tắc định nghĩa $q$ phải nằm ở tầng **nghiêm ngặt thấp hơn** $j < i$. Nói cách khác: *không
được phủ định một vị từ đang được định nghĩa cùng lúc hoặc ở tầng cao hơn.*

> ℹ **Định lý:** Mọi chương trình Datalog phân tầng đều có một **mô hình tối tiểu duy nhất**
> (gọi là **perfect model**). Ta tính nó bằng cách chạy fixpoint tầng 1, rồi tầng 2 (dùng kết
> quả đã chốt của tầng 1 để đánh giá `not`), ... đến tầng $n$. Vì mỗi tầng chỉ phủ định các vị
> từ *đã chốt*, tính phi đơn điệu không còn gây nhập nhằng.

Điều kiện phân tầng **không phải lúc nào cũng thỏa được** — ví dụ $p \leftarrow \text{not }
q,\; q \leftarrow \text{not } p$ ở trên có vòng phủ định nên không phân tầng được. Khi đó phải
dùng ngữ nghĩa mạnh hơn (stable models / answer set programming) nằm ngoài phạm vi chương này.

Quay lại SHACL: chính vì SHACL dùng LCWA (§5.10) — một dạng NAF cục bộ — mà nó **phi đơn
điệu**. Các constraint `sh:minCount`, `sh:maxCount`, `sh:not` đều diễn dịch "không thấy" thành
"không có", nên thêm dữ liệu có thể đổi verdict. SHACL tránh được vòng nhập nhằng kiểu
$p \leftrightarrow q$ vì nó **không suy diễn**: shape chỉ kiểm tra trên một đồ thị đã chốt,
không định nghĩa vị từ quy nạp lẫn nhau.

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

### RIF: Rule Interchange Format

RIF (Rule Interchange Format) [@w3c-rif-core] là họ chuẩn W3C cho trao đổi quy tắc giữa
các hệ thống. RIF Core Dialect định nghĩa definite Horn rules không có ký hiệu hàm
(= Datalog), với điều kiện safeness đảm bảo forward chaining dừng.

> ℹ **SWRL và RIF là bối cảnh hệ sinh thái.** Người đọc nên rời Chương 5 với hiểu biết về
> cơ chế suy diễn bằng quy tắc, không phải với trí nhớ về các dự án ngôn ngữ quy tắc lịch
> sử của W3C. Trọng tâm là cơ chế, không phải lịch sử chuẩn.

## 5.17 SHACL 1.2: Phát triển hiện tại

> ℹ **Phát triển hiện tại (Current Development)**
>
> **Baseline ổn định:** SHACL Recommendation, 2017 [@w3c-shacl]. Đây là ngữ nghĩa chuẩn
> được dạy trong chương này.
>
> **Emerging:** SHACL 1.2 Core, W3C Working Draft, 2026-08-03 [@w3c-shacl12-core]. Đây là
> tài liệu đang phát triển, chưa ổn định. Không dạy các tính năng chỉ có trong draft như
> thể chúng là baseline.
>
> Hướng phát triển đáng chú ý: SHACL 1.2 mở rộng và tinh chỉnh một số constraint components,
> cải thiện khả năng biểu diễn shapes. Chi tiết cụ thể nằm ngoài phạm vi chương này; người
> đọc quan tâm nên theo dõi trực tiếp Working Draft.

## 5.18 Cầu nối đến Mechanism KG

Chương này đã chạy toàn bộ máy móc suy diễn và xác nhận trên dữ liệu Mechanism-KG đang
xây dựng. Bốn ví dụ làm việc đầy đủ:

1. **Suy diễn:** Forward chaining với quy tắc RDFS subClassOf trên dữ liệu cơ chế —
   `ex:rateOfChange_1 a ex:RateOfChangeMechanism` → `a ex:ChangeMechanism` → `a
   ex:Mechanism`, với phép thế $\theta$ và điểm bất động (§5.2). Quy tắc transitive cho
   `ex:requires` (nếu A requires B và B requires C thì A requires C) là biến thể cùng cơ chế.

2. **Xác nhận:** Shape `CandidateMechanismShape` kiểm tra cấu trúc tối thiểu của một ứng
   viên cơ chế (`hasOperation`, `hasInput`, `hasOutput`, `rdfs:label`) và tạo validation
   report tương ứng (§5.6, §5.7). Mỗi Mechanism phải có ít nhất một `ex:Operation`; mỗi
   `ex:Condition` phải liên kết với ít nhất một Mechanism — đều là các shape cùng dạng.

   `Condition` không phải là tên trống: nó là một cá thể gắn với cơ chế qua
   `ex:hasCondition`, chẳng hạn:

   ```turtle
   ex:uniformEnv_1 a ex:Condition ;
       rdfs:label "uniform environment (T constant, h constant)" .
   ex:newtonCooling_1 ex:hasCondition ex:uniformEnv_1 .
   ```

   Shape tương ứng kiểm tra mọi `ex:hasCondition` value node phải là SHACL instance của
   `ex:Condition` (`sh:path ex:hasCondition ; sh:class ex:Condition`).

3. **Hai trục độc lập:** Ví dụ 2×2 consistency-vs-validation trên dữ liệu cơ chế (ontology
   disjoint bị vi phạm nhưng SHACL vẫn conformant; candidate thiếu output thì OWL-consistent
   nhưng SHACL-violating) (§5.9).

4. **Repair governance:** Khi SHACL báo candidate thiếu `ex:hasOutput`, các candidate repairs
   (thêm từ bằng chứng nguồn, thêm placeholder, loại bỏ, thay đổi shape) có hệ quả tri thức
   khác nhau; quyết định thuộc về domain governance, không phải engine (§5.12).

### Pipeline hai tầng: suy diễn rồi xác nhận

Ví dụ xuyên suốt này giờ có thể ghép thành một **pipeline hai tầng** hoàn chỉnh trên đồ thị
cơ chế — đúng kiến trúc B ở §5.11:

**Tầng 1 — Suy diễn (Datalog / quy tắc Horn).** Chạy ba quy tắc từ §5.2 để vật chất hóa các
thuộc tính dẫn xuất và phân loại trên `rateOfChange_1`:

$$\text{hasInput}(m, q) \leftarrow \text{hasApplication}(m, a) \land \text{differentiand}(a, q)$$

$$\text{hasReferenceVariable}(m, v) \leftarrow \text{hasApplication}(m, a) \land \text{withRespectTo}(a, v)$$

Kết quả: `rateOfChange_1` có thêm hai cạnh `hasInput position_1` và `hasReferenceVariable
time_1`, rồi được gán `rdf:type RateOfChangeMechanism`.

**Tầng 2 — Xác nhận (SHACL).** Một `sh:NodeShape` kiểm tra đồ thị *đã được làm giàu* ở tầng 1:

```turtle
ex:RateOfChangeMechanismShape a sh:NodeShape ;
    sh:targetClass ex:RateOfChangeMechanism ;
    sh:property [ sh:path ex:hasOperation ;
                  sh:minCount 1 ; sh:class ex:DerivativeOperation ] ;
    sh:property [ sh:path ex:hasInput ;
                  sh:minCount 1 ; sh:class ex:Quantity ] ;
    sh:property [ sh:path ex:hasReferenceVariable ;
                  sh:minCount 1 ; sh:maxCount 1 ; sh:class ex:ReferenceVariable ] .
```

> ⚠ **Vì sao thứ tự "suy diễn trước, xác nhận sau" là sống còn.** Nếu chạy Tầng 2 ngay trên
> đồ thị gốc (bỏ Tầng 1), shape sẽ báo **violation sai**: `hasInput` và `hasReferenceVariable`
> lúc ấy chỉ *ngầm ẩn* (chưa asserted), nên `sh:minCount 1` bị vi phạm dù dữ liệu hoàn toàn
> hợp lệ về mặt ngữ nghĩa. Chỉ sau khi Tầng 1 vật chất hóa hai cạnh ấy, Tầng 2 mới nhìn thấy
> chúng và cho verdict đúng. Đây là hiện thực hóa của §5.11 (effective validation graph phụ
> thuộc vào những gì được suy diễn trước khi validate).

> ⚠ **Lưu ý thiết kế:** Khi xây dựng mechanism ontology, đừng cố gắng biểu diễn mọi thứ
> bằng OWL axioms. Một số ràng buộc (số lượng tối thiểu, kiểu dữ liệu, pattern) phù hợp
> hơn với SHACL. Một số suy diễn (transitive, symmetric) phù hợp hơn với quy tắc. Chọn
> công cụ đúng cho mục đích đúng. Document rõ: asserted graph, inferred graph, effective
> validation graph, và entailment regime.

## 5.19 Những ngộ nhận thường gặp

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
không complete cho OWL 2 DL đầy đủ hoặc arbitrary RDF. Luôn ghi rõ phạm vi.

### Ngộ nhận 5: "Dữ liệu phù hợp SHACL = dữ liệu đúng"

**Sai.** Conformance chỉ nghĩa là dữ liệu khớp shapes. Dữ liệu có thể phù hợp mà vẫn sai
về mặt nội dung.

### Ngộ nhận 6: "Vi phạm SHACL = dữ liệu sai"

**Sai.** Vi phạm chỉ nghĩa là dữ liệu không khớp shapes. Dữ liệu có thể đúng về nội dung
nhưng không khớp cấu trúc kỳ vọng.

### Ngộ nhận 7: "Forward chaining luôn dừng"

**Sai.** Forward chaining chỉ đảm bảo dừng khi thỏa mãn các điều kiện: đồ thị hữu hạn, quy
tắc hữu hạn, function-free, safe variables, không sinh term mới vô hạn (§5.2).

### Ngộ nhận 8: "SWRL là chuẩn W3C ổn định"

**Sai.** SWRL là Member Submission (2004), không phải Recommendation. Kết hợp OWL DL +
SWRL nói chung không quyết định được.

### Ngộ nhận 9: "SHACL = OWL với Closed World Assumption"

**Sai.** SHACL là framework xác nhận riêng biệt với ngữ nghĩa riêng. Một số constraints
làm cho sự vắng mặt trong data graph trở nên có ý nghĩa, nhưng SHACL không đơn giản là OWL
+ CWA (§5.6).

### Ngộ nhận 10: "Đơn điệu nghĩa là thêm điều kiện vào body tăng kết quả"

**Sai.** Đơn điệu nghĩa là thêm *thông tin vào đồ thị* (knowledge base) không làm mất kết
luận cũ. Thêm điều kiện vào body làm quy tắc khó khớp hơn, có thể giảm kết quả (§5.2).

### Ngộ nhận 11: "sh:targetClass chỉ match exact rdf:type triple"

**Sai.** sh:targetClass dùng SHACL instance semantics, bao gồm subclass reasoning qua
`rdfs:subClassOf*` (§5.6).

### Ngộ nhận 12: "SPARQL FROM clause thay đổi entailment regime"

**Sai.** FROM chọn đồ thị/dataset. Entailment regime được chỉ định qua Service Description
[@w3c-sparql11-entailment] (§5.14).

## 5.20 Câu hỏi suy ngẫm

1. ★ Giải thích sự khác biệt giữa inference và validation bằng một ví dụ cụ thể từ miền
   city/country.

2. ★★ Cho ontology với `Person ⊑ ∃hasName.xsd:string` và dữ liệu có `(Alice, rdf:type, Person)`
   nhưng không có triple `hasName` nào cho Alice. (a) OWL 2 DL entailment nói gì? (b)
   SHACL shape `sh:minCount 1` trên `hasName` nói gì? (c) Hai câu trả lời khác nhau như
   thế nào và tại sao?

3. ★★ Thiết kế bộ SHACL shapes cho Mechanism ontology: mỗi Mechanism phải có ít nhất một
   `ex:Operation`, mỗi `ex:Operation` phải liên kết với đúng một Mechanism (qua
   `ex:hasOperation`), và mỗi `ex:Condition` phải có description kiểu xsd:string. Viết
   shapes bằng Turtle. Kiểm tra shapes của bạn trên `ex:candidateRateOfChange_1` ở §5.6 —
   candidate có pass shape `ex:Operation` không? (Gợi ý: xem `ex:hasOperation
   ex:derivativeOperation_1` trong dữ liệu.)

4. ★★★ So sánh forward chaining trên RDFS và forward chaining trên OWL RL về: (a) tập quy
   tắc, (b) khả năng biểu diễn, (c) tính soundness và completeness, (d) chi phí tính toán.
   Trong trường hợp nào bạn chọn RDFS thay vì OWL RL?

5. ★★★ Một hệ thống dùng OWL RL forward chaining để suy diễn, và SHACL để xác nhận. Xây
   dựng một ví dụ trong đó: (a) dữ liệu OWL-consistent nhưng SHACL-violating, và (b) dữ
   liệu OWL-inconsistent nhưng SHACL-conformant. Giải thích tại sao mỗi trường hợp xảy ra.

### 5.20.1 Gợi ý trả lời

**Câu 1 (★).** Giải thích sự khác biệt giữa inference và validation bằng một ví dụ cụ thể từ miền city/country.

Xét ontology có `capitalOf rdfs:domain City` và `capitalOf rdfs:range Country`, cùng dữ liệu `Vietnam capitalOf Hanoi`. **Pipeline suy diễn** (forward chaining, §5.2) áp quy tắc RDFS domain/range (§5.3) và *thêm* vào đồ thị: `Vietnam rdf:type City` và `Hanoi rdf:type Country`. Nó không hề báo lỗi, dù kết quả "phi lý" với thực tế — vì RDFS chỉ áp dụng ngữ nghĩa, không kiểm tra kỳ vọng. **Pipeline xác nhận** (SHACL, §5.6) đi ngược hướng: một shape như `sh:class Country` trên path `capitalOf` sẽ *kiểm tra* value node và, nếu `Hanoi` không phải Country theo dữ liệu được cung cấp, sinh ra một violation trong validation report (§5.7) mà không thêm bất kỳ triple nào. Cùng một từ vựng (class, property) nhưng hai chiều tác động trái ngược: inference = thêm thông tin, validation = kiểm tra thông tin (§5.1, §5.10).

Lý do: nhầm hai pipeline là nguồn lỗi thiết kế phổ biến nhất — dùng `rdfs:domain` để "kiểm tra" (nó không kiểm tra) hoặc dùng shape để "suy diễn" (nó không suy diễn). Bằng chứng: §5.1 (bảng hai pipeline), §5.3 (domain/range thêm thông tin, ví dụ Vietnam/Hanoi), §5.6 (SHACL kiểm tra), §5.10 (shapes ≠ axioms).

**Câu 2 (★★).** Cho ontology với `Person ⊑ ∃hasName.xsd:string` và dữ liệu có `(Alice, rdf:type, Person)` nhưng không có triple `hasName` nào cho Alice. (a) OWL 2 DL entailment nói gì? (b) SHACL shape `sh:minCount 1` trên `hasName` nói gì? (c) Hai câu trả lời khác nhau như thế nào và tại sao?

(a) **OWL 2 DL:** ontology *nhất quán* và không sinh thêm ground triple nào đặt tên cho hasName của Alice. Dưới Open World Assumption, tiên đề chỉ đòi hỏi "trong mọi model, Alice có một hasName-successor là string"; model thỏa mãn bằng cách đưa vào một *unnamed witness* không có trong đồ thị RDF (§5.10). Không có violation, không có inconsistency. (b) **SHACL:** shape `sh:targetClass ex:Person` + `sh:path ex:hasName ; sh:minCount 1` chạy chuỗi cơ chế §5.6: focus node = Alice, path = hasName, value nodes = ∅ → `minCount 1` không thỏa → một ValidationResult severity Violation, `sh:conforms false` (§5.7). (c) Khác biệt: OWL nói về *mọi model* và tha thứ cho sự vắng mặt (existential witness vô danh); SHACL nói về *một data graph cụ thể được cung cấp* và coi sự vắng mặt là vi phạm cấu trúc. Cùng yêu cầu "phải có name", ngữ nghĩa hoàn toàn khác (§5.10).

Lý do: đây chính là cặp "OWL existential vs SHACL minCount" mà chương dùng làm ví dụ phân biệt mạnh nhất. Bằng chứng: §5.9 (OWA vs data-check), §5.10 (existential restriction ≠ minCount), §5.6, §5.7.

**Câu 3 (★★).** Thiết kế bộ SHACL shapes cho Mechanism ontology: mỗi Mechanism phải có ít nhất một `ex:Operation`, mỗi `ex:Operation` phải liên kết với đúng một Mechanism (qua `ex:hasOperation`), và mỗi `ex:Condition` phải có description kiểu xsd:string. Viết shapes bằng Turtle. Kiểm tra shapes của bạn trên `ex:candidateRateOfChange_1` ở §5.6 — candidate có pass shape `ex:Operation` không?

```turtle
ex:MechanismShape a sh:NodeShape ;
    sh:targetClass ex:Mechanism ;
    sh:property [ sh:path ex:hasOperation ; sh:minCount 1 ] .

ex:OperationShape a sh:NodeShape ;
    sh:targetClass ex:Operation ;
    sh:property [ sh:path [ sh:inversePath ex:hasOperation ] ;
                  sh:minCount 1 ; sh:maxCount 1 ] .

ex:ConditionShape a sh:NodeShape ;
    sh:targetClass ex:Condition ;
    sh:property [ sh:path ex:description ;
                  sh:datatype xsd:string ; sh:minCount 1 ] .
```
Ràng buộc "đúng một Mechanism" cần `sh:inversePath` vì nó đếm số Mechanism trỏ *vào* mỗi Operation, rồi `minCount 1`/`maxCount 1` ép đúng một. **Kiểm tra trên `ex:candidateRateOfChange_1`:** dữ liệu §5.6 có `ex:hasOperation ex:derivativeOperation_1`, nên *nếu* `MechanismShape` áp lên nó thì constraint `hasOperation minCount 1` **pass** (có đúng một value node). Nhưng có hai lưu ý: (i) `MechanismShape` target `ex:Mechanism`, còn candidate là `ex:CandidateMechanism`; theo SHACL instance semantics (§5.6) nó chỉ bị target nếu `CandidateMechanism rdfs:subClassOf Mechanism` có mặt trong data graph — chương không khai báo liên kết này, nên tốt nhất candidate được kiểm bởi `CandidateMechanismShape` (§5.6), vốn vẫn fail vì thiếu `hasOutput`. (ii) `OperationShape` phía inverse: `derivativeOperation_1` được tham chiếu bởi đúng một triple `hasOperation` → pass minCount/maxCount.

Lý do: pass/fail phải đọc theo đúng 6 bước target→result, không đoán. Bằng chứng: §5.6 (cơ chế, CandidateMechanismShape), §5.7 (report), §5.18 (Condition/hasOperation).

**Câu 4 (★★★).** So sánh forward chaining trên RDFS và forward chaining trên OWL RL về: (a) tập quy tắc, (b) khả năng biểu diễn, (c) tính soundness và completeness, (d) chi phí tính toán. Trong trường hợp nào bạn chọn RDFS thay vì OWL RL?

(a) **Tập quy tắc:** RDFS dùng bộ nhỏ — subClassOf (rdfs9), subPropertyOf (rdfs7), domain (rdfs2), range (rdfs3) (§5.3). OWL RL dùng bộ lớn hơn nhiều, phủ các tiên đề OWL tương thích Horn, kể cả quy tắc phát hiện mâu thuẫn như `cax-dw` cho `owl:disjointWith` (§5.13, §5.16). (b) **Khả năng biểu diễn:** RDFS chỉ diễn đạt phân cấp lớp/property và domain/range; OWL RL thêm class expression theo Table 2 của profile, nhưng vẫn cấm `DisjointUnion`, `ReflexiveObjectProperty` và nằm ngoài tầm với phủ định/phép đếm/lượng từ tồn tại phức tạp (§5.13). (c) **Soundness/Completeness:** cả hai *sound*. RDFS naive closure *không complete* trên cú pháp RDF chuẩn (cần generalized RDF, §5.3). OWL RL chỉ complete *có điều kiện* — dưới hạn chế cú pháp của profile (Theorem PR1), không đảm bảo trên đồ thị RDF tùy ý (§5.13). (d) **Chi phí:** OWL RL nhiều quy tắc hơn → closure lớn hơn, tính toán đắt hơn; RDFS rẻ và ổn định hơn để vật chất hóa (§5.4). **Chọn RDFS khi** chỉ cần suy diễn phân cấp loại (classification qua subClassOf/domain/range), dữ liệu lớn, cần vật chất hóa rẻ và dễ kiểm soát, và không đòi hỏi entailment mức OWL.

Lý do: forward chaining là thuật toán, kết quả phụ thuộc tập quy tắc và regime (§5.2, §5.14). Bằng chứng: §5.3, §5.4, §5.13, §5.14, §5.15.

**Câu 5 (★★★).** Một hệ thống dùng OWL RL forward chaining để suy diễn, và SHACL để xác nhận. Xây dựng một ví dụ trong đó: (a) dữ liệu OWL-consistent nhưng SHACL-violating, và (b) dữ liệu OWL-inconsistent nhưng SHACL-conformant. Giải thích tại sao mỗi trường hợp xảy ra.

(a) **OWL-consistent, SHACL-violating.** Ontology không có tiên đề nào buộc `hasOutput`. Dữ liệu: `ex:m1 a ex:Mechanism`. OWL RL forward chaining không suy ra điều gì mâu thuẫn (OWA cho phép m1 *có thể* có output ở model khác, §5.9/§5.10) → consistent. Nhưng `MechanismShape` với `sh:path ex:hasOutput ; sh:minCount 1` (§5.6) thấy value nodes = ∅ trên đồ thị được cung cấp → violation, `sh:conforms false` (§5.7). Xảy ra vì OWL không coi sự vắng mặt là lỗi, còn SHACL kiểm tra chính đồ thị đó.

(b) **OWL-inconsistent, SHACL-conformant.** Ontology: `ex:ChangeMechanism owl:disjointWith ex:AggregationMechanism`. Dữ liệu: `ex:x9 a ex:ChangeMechanism ; a ex:AggregationMechanism ; ex:hasOperation ex:op1 ; rdfs:label "x9"`. OWL RL forward chaining áp quy tắc `cax-dw` (đã kiểm chứng trong OWL 2 RL/RDF rules: hai rdf:type của hai lớp disjoint → `false`) → inconsistent. SHACL chỉ có shape kiểm tra cấu trúc (có `hasOperation`, có label) → mọi constraint thỏa → `sh:conforms true`, vì "SHACL không đọc `owl:disjointWith`" (§5.9).

Lý do: consistency và conformance là hai trục độc lập — biết một không suy ra kia (§5.9, §5.10). Bằng chứng: §5.9 (2×2), §5.10 (shapes ≠ axioms), §5.13 (OWL RL rules), §5.6.

## 5.21 Chúng ta đã biết gì

Chương này đã thiết lập sự phân biệt cốt lõi giữa hai pipeline và các cơ chế nền tảng:

- **Suy diễn (Inference):** Từ dữ liệu + ngữ nghĩa → tri thức mới. Forward chaining dùng
  phép thế $\theta$ để kết nối quy tắc trừu tượng với dữ liệu cụ thể. Điểm bất động (fixpoint)
  là điều kiện dừng. RDFS rules thêm thông tin (không kiểm tra). Vật chất hóa là chiến lược
  triển khai, không phải bản thân suy diễn. Backward reasoning là chiến lược thay thế.

- **Xác nhận (Validation):** Từ dữ liệu + shapes → báo cáo phù hợp/vi phạm. SHACL mechanism:
  target → focus node → path → value node → constraint → result. Shapes ≠ axioms.
  Conformance ≠ truth. Violation ≠ repair. Consistency ≠ validation (hai trục độc lập).

- **Đánh giá:** Soundness ($A \subseteq E$) và completeness ($E \subseteq A$) luôn cần ba
  thành phần: language + regime + task. OWL RL sound nhưng completeness có điều kiện.

- **Kỹ thuật:** Effective validation graph là quyết định kiến trúc. Repair là decision
  problem. Asserted ≠ derived.

## 5.22 Chúng ta chưa làm được gì

Chương này đã dạy cơ chế suy diễn và xác nhận, nhưng chưa giải quyết các câu hỏi:

- **Tri thức đến từ đâu?** Suy diễn chỉ tạo ra tri thức mới từ tri thức cũ. Nhưng tri thức
  ban đầu đến từ đâu? Làm sao thu thập, trích xuất, và tích hợp tri thức từ nhiều nguồn?
  (Chương 7)
- **Khi hai nguồn mâu thuẫn thì sao?** Suy diễn giả định dữ liệu nhất quán. Nhưng trong
  thực tế, các nguồn tri thức khác nhau có thể đưa ra tuyên bố trái ngược. Làm sao xử lý
  mâu thuẫn? Ai có thẩm quyền quyết định repair? (Chương 6)
- **Làm sao suy diễn khi tri thức không chắc chắn?** Forward chaining và SHACL đều làm việc
  với tri thức nhị phân (đúng/sai). Nhưng nhiều tri thức thực tế mang tính xác suất hoặc
  quy nạp. (Chương 8)

Chương tiếp theo sẽ bắt đầu giải quyết câu hỏi về tuyên bố, bằng chứng, nguồn gốc và mâu
thuẫn — lớp Context trong Mental Model 1.

## 5.23 Mechanism Knowledge System — Năng lực đạt được

**TRƯỚC CHƯƠNG NÀY** — hệ thống có ontology OWL (Chương 4) với các khái niệm về diễn giải,
mô hình, suy diễn, OWA, nhất quán. Nhưng ontology là *tuyên bố tĩnh*: không có cơ chế tính
toán hệ quả, không có cách kiểm tra dữ liệu có tuân thủ kỳ vọng hay không, không có chiến
lược sửa lỗi.

**SAU CHƯƠNG NÀY** — hệ thống có hai pipeline hoàn chỉnh:
- **Suy diễn:** Forward chaining với phép thế $\theta$ và điểm bất động trên dữ liệu cơ chế
  (§5.2). RDFS rules áp dụng lên taxonomy cơ chế (§5.3). Vật chất hóa là chiến lược triển
  khai, không phải bản thân suy diễn (§5.4).
- **Xác nhận:** SHACL shapes kiểm tra `CandidateMechanism` (§5.6), validation report cấu
  trúc hóa (§5.7). Phân biệt được conformance ≠ truth, consistency ≠ validation (§5.9).
  Shapes ≠ axioms ≠ rules (§5.10).
- **Sửa chữa:** Graph repair là bài toán quyết định, dựa trên domain governance (§5.12).
- **Đánh giá:** Soundness và completeness chỉ có nghĩa trong phạm vi language + regime +
  task (§5.13). Cùng một truy vấn SPARQL trên dữ liệu cơ chế cho kết quả khác nhau dưới
  Simple và RDFS regime (§5.14).

**VÍ DỤ RATE_OF_CHANGE CỤ THỂ** — forward chaining suy ra `ex:rateOfChange_1 a
ex:Mechanism` từ `a ex:RateOfChangeMechanism` qua hai bước subClassOf (§5.2). SHACL shape
kiểm tra `ex:candidateRateOfChange_1` thiếu `ex:hasOutput` và báo vi phạm (§5.6, §5.7).
Hai trục 2×2 trên dữ liệu cơ chế: ontology disjoint inconsistent nhưng SHACL conformant
(§5.9). SPARQL Simple regime trả về ∅, RDFS regime trả về 3 mechanisms (§5.14).

**VẪN CHƯA GIẢI QUYẾT** — suy diễn và xác nhận giả định dữ liệu đầu vào đã sẵn sàng. Câu
hỏi "tri thức đến từ đâu?", "khi hai nguồn mâu thuẫn thì sao?", "ai có thẩm quyền quyết
định repair?" vẫn chưa có lời giải. Chương 6 mở ra nấc tiếp theo: *tuyên bố, bằng chứng,
nguồn gốc và thời gian*.

## Thuật ngữ đã gặp trong chương này

| Thuật ngữ | Nghĩa ngắn | Học chi tiết |
|-----------|-----------|--------------|
| Forward Chaining (suy diễn tiến) | Áp dụng quy tắc lặp cho đến fixpoint | §5.2 |
| Phép thế $\theta$ (Substitution) | Ánh xạ biến sang giá trị cụ thể; ground fact là kết quả | §5.2 |
| Grounding | Làm cho quy tắc trừu tượng thành cụ thể bằng phép thế | §5.2 |
| Fixpoint (điểm bất động) | $G_{n+1} = G_n$: không còn triple mới được sinh ra | §5.2 |
| Bao đóng (Closure) | Đồ thị chứa mọi hệ quả đã tính | §5.2 |
| Đơn điệu (Monotonicity) | Thêm tri thức không làm mất kết luận cũ | §5.2 |
| RDFS Entailment Rules | Quy tắc suy diễn thêm thông tin, không kiểm tra | §5.3 |
| Vật chất hóa (Materialization) | Chiến lược tính closure trước, lưu kết quả | §5.4 |
| Suy diễn tại truy vấn (Query-time) | Chiến lược tính toán lazy khi có truy vấn | §5.4 |
| Backward Chaining (suy diễn lùi) | Bắt đầu từ câu hỏi, tìm chứng minh | §5.5 |
| SHACL Shape | Mô tả điều kiện kiểm tra dữ liệu | §5.6 |
| Focus Node / Value Node | Nút đang đánh giá / nút đích qua path | §5.6 |
| Validation Report | Báo cáo kết quả xác nhận (conforms/vi phạm) | §5.7 |
| Conformance (phù hợp) | Dữ liệu khớp shapes ≠ dữ liệu đúng | §5.8 |
| Consistency (nhất quán) | Tồn tại mô hình OWL ≠ SHACL conformant | §5.9 |
| Soundness (tính đúng đắn) | Mọi kết quả suy diễn đều đúng ngữ nghĩa | §5.13 |
| Completeness (tính đầy đủ) | Mọi hệ quả ngữ nghĩa đều được suy diễn | §5.13 |
| Effective Validation Graph | Đồ thị thực sự được validator nhìn thấy | §5.11 |
| Entailment Regime (chế độ suy diễn) | Xác định mức độ suy diễn khi truy vấn | §5.14 |
| Graph Repair | Quyết định sửa dữ liệu hay sửa shape dựa trên governance | §5.12 |
| Ground Triple (fact) | Triple không còn biến, sẵn sàng trong đồ thị | §5.2 |
| Toán tử hệ quả tức thời $T_P$ (Immediate consequence operator) | $T_P(I)$ = mọi ground head có body khớp trong $I$ | §5.2 |
| Ngữ nghĩa điểm bất động (Fixed-point semantics) | Ý nghĩa chương trình = $\mathrm{lfp}(T_P)$ (Knaster–Tarski) | §5.2 |
| Mô hình Herbrand tối tiểu (Minimal Herbrand Model) | $\mathcal{M}(P)$ = giao mọi mô hình Herbrand thỏa $P$ chứa $D$ | §5.16 |
| Datalog | Quy tắc Horn function-free, safe; 3 ngữ nghĩa tương đương | §5.16 |
| Phủ định cổ điển vs NAF ($\neg$ vs $\sim$) | $\neg$ theo OWA (đơn điệu) vs `not` theo CWA (phi đơn điệu) | §5.16 |
| Datalog phân tầng (Stratified Datalog) | Tầng thấp chốt trước, tầng cao mới `not`; cho perfect model duy nhất | §5.16 |
| Ngữ nghĩa thế giới đóng cục bộ (LCWA) | SHACL: vắng mặt trong đồ thị = không tồn tại cho focus node | §5.10 |
| Thuật toán RETE (RETE algorithm) | Mạng alpha/beta cache phép khớp trung gian; đổi bộ nhớ lấy tốc độ | §5.5 |
| Mạng Alpha / Mạng Beta (Alpha / Beta network) | Lọc trong một mẫu / nối binding giữa các mẫu | §5.5 |

## Đọc thêm

- SHACL W3C Recommendation [@w3c-shacl] — định nghĩa đầy đủ shapes và validation.
- SPARQL 1.1 Entailment Regimes [@w3c-sparql11-entailment] — chế độ suy diễn trong SPARQL.
- RDF 1.1 Semantics [@w3c-rdf11-mt] — ngữ nghĩa model-theoretic của RDFS.
- Hogan et al., *Knowledge Graphs*, Chapter 7: Inductive Knowledge [@hogan-knowledge-graphs] — suy diễn quy nạp và xác suất.
- OWL 2 RL [@w3c-owl2-profiles] — OWL RL profile và cơ chế forward chaining.
- OWL 2 Direct Semantics [@w3c-owl2-direct-semantics] — ngữ nghĩa OWL 2 cho soundness/completeness.
- Abiteboul, Hull & Vianu, *Foundations of Databases* [@abiteboul-foundations-1995] — nguồn chuẩn cho Datalog, ba ngữ nghĩa và độ phức tạp.
- Forgy, *Rete: A Fast Algorithm for the Many Pattern/Many Object Pattern Match Problem* [@forgy-rete-1982] — thuật toán RETE gốc.
- Motik et al., *Parallel Materialisation of Datalog Programs in Centralised, Main-Memory RDF Systems* [@motik-rdfox-2014] — vật chất hóa Datalog song song (RDFox).
