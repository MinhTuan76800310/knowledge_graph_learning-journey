# Chapter 2: Mô hình Dữ liệu và Ngôn ngữ Truy vấn

## Motivation

Chương 1 đã thiết lập rằng tri thức trong đồ thị tri thức được biểu diễn dưới dạng các bộ ba (subject, predicate, object). Nhưng "bộ ba" là một khái niệm trừu tượng — khi triển khai thực tế, chúng ta phải chọn một **mô hình biểu diễn cụ thể**. Lựa chọn này quyết định:

- Những gì có thể biểu diễn được và những gì bị bỏ sót
- Cách truy vấn và suy luận hoạt động
- Khả năng trao đổi dữ liệu giữa các hệ thống
- Độ phức tạp khi bảo trì và mở rộng

Chương này trả lời câu hỏi trung tâm: **Lựa chọn mô hình biểu diễn đồ thị thay đổi những gì chúng ta có thể biểu đạt, truy vấn, suy luận, trao đổi và bảo trì như thế nào?**

Chúng ta sẽ nghiên cứu hai họ mô hình đồ thị chính:

1. **RDF graph model** — tiêu chuẩn W3C, nền tảng của Semantic Web
2. **Labeled Property Graph** — mô hình được Neo4j và nhiều cơ sở dữ liệu đồ thị hiện đại sử dụng

Cả hai đều được minh họa bằng **cùng một miền tri thức** (Hà Nội, Việt Nam, Paris, Pháp) để sự so sánh có ý nghĩa thực tế.

> **Phạm vi chương:** Đây không phải hướng dẫn cú pháp RDFLib, SPARQL, Neo4j hay Cypher. Mục tiêu học tập là hiểu **cơ chế và sự đánh đổi** của mỗi mô hình, không phải ghi nhớ API.

## 2.1 RDF Graph Model

### 2.1.1 RDF Graph là gì?

Theo RDF 1.1 Concepts and Abstract Syntax (R11-02), một **RDF graph** là một tập hợp các **RDF triple**. Mỗi triple gồm ba thành phần:

| Vị trí | Tên | Kiểu dữ liệu cho phép |
|--------|-----|----------------------|
| Subject | Chủ thể | IRI hoặc Blank Node |
| Predicate | Vị từ | IRI |
| Object | Đối tượng | IRI, Literal, hoặc Blank Node |

Một số điểm quan trọng từ đặc tả:

- **IRI** (Internationalized Resource Identifier) là định danh toàn cục. Ví dụ: `http://example.org/Hanoi`.
- **Literal** là giá trị dữ liệu như chuỗi `"Hà Nội"` hoặc số `8418883`. Literal chỉ xuất hiện ở vị trí object.
- **Blank node** là nút ẩn danh, dùng khi không cần định danh toàn cục.
- **Predicate luôn là IRI.** Không bao giờ là literal hay blank node.
- **RDF graph là tập hợp** (set), không phải danh sách. Thứ tự các triple không có ý nghĩa. Trùng lặp bị loại bỏ.

> ⚠️ **Phân biệt rõ ràng:** RDF graph là **mô hình dữ liệu trừu tượng**. Turtle, N-Triples, RDF/XML, JSON-LD là các **cú pháp cụ thể** (concrete syntax) để biểu diễn cùng một graph. Đừng nhầm lẫn mô hình với cú pháp.

### 2.1.2 Biểu diễn miền tri thức bằng RDF

Xét miền tri thức nhỏ từ Chương 1:

```
Hà Nội   → thủ đô của → Việt Nam
Paris    → thủ đô của → Pháp
Hà Nội   → thành phố kết nghĩa → Paris
```

Trong RDF, mỗi mệnh đề trở thành một hoặc nhiều triple:

```python
from rdflib import Graph, Literal, Namespace, RDF, RDFS

EX = Namespace("http://example.org/")
g = Graph()

g.add((EX.Hanoi, RDF.type, EX.City))
g.add((EX.Hanoi, RDFS.label, Literal("Hà Nội")))
g.add((EX.Hanoi, EX.capitalOf, EX.Vietnam))
g.add((EX.Paris, RDF.type, EX.City))
g.add((EX.Paris, RDFS.label, Literal("Paris")))
g.add((EX.Paris, EX.capitalOf, EX.France))
g.add((EX.Hanoi, EX.sisterCity, EX.Paris))
g.add((EX.Vietnam, RDF.type, EX.Country))
g.add((EX.France, RDF.type, EX.Country))
```

Mỗi dòng `g.add(...)` thêm đúng một triple vào graph. Graph chứa 9 triple, mỗi triple là một mệnh đề độc lập.

**Nhận xét về identity trong RDF:** Định danh của mỗi thực thể là IRI (`http://example.org/Hanoi`). IRI mang tính toàn cục — hai hệ thống khác nhau có thể tham chiếu đến cùng một thực thể nếu dùng cùng IRI. Đây là thiết kế cốt lõi của RDF cho khả năng liên kết dữ liệu mở (Linked Data).

→ **Thí nghiệm 2-1** (`chapter02/exp_2_1_rdf_first_principles.py`) xây dựng một triple store thuần Python từ đầu, sau đó so sánh với RDFLib để chứng minh rằng cả hai đều biểu diễn cùng một mô hình RDF.

### 2.1.3 Turtle: Cú pháp, không phải mô hình

Turtle là cú pháp văn bản phổ biến nhất để viết RDF. Nhưng Turtle **không phải** là RDF — nó chỉ là một cách viết ra RDF graph.

```turtle
@prefix ex: <http://example.org/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Hanoi a ex:City ;
    rdfs:label "Hà Nội" ;
    ex:capitalOf ex:Vietnam .

ex:Paris a ex:City ;
    rdfs:label "Paris" ;
    ex:capitalOf ex:France .

ex:Hanoi ex:sisterCity ex:Paris .
```

Đoạn Turtle trên biểu diễn **cùng một RDF graph** với đoạn Python ở mục 2.1.2. Khi parse lại, ta thu được tập hợp triple giống hệt.

Kiểm chứng bằng round-trip serialization:

```python
turtle_text = g.serialize(format="turtle")
g2 = Graph()
g2.parse(data=turtle_text, format="turtle")
assert set(g) == set(g2)  # ✅ Graph tương đương
```

Cùng một graph cũng có thể serialize thành N-Triples, RDF/XML, hay JSON-LD — tất cả đều cho lại graph tương đương khi parse lại. Prefix declarations (`@prefix`) chỉ là cú pháp tắt; chúng không thay đổi IRI trong graph.

> ⚠️ **Sai lầm phổ biến:** So sánh chuỗi Turtle thô để kiểm tra "hai graph giống nhau". Hai tài liệu Turtle khác nhau về mặt văn bản có thể biểu diễn cùng một RDF graph. Luôn so sánh **parsed graph semantics**, không so sánh chuỗi.

→ **Thí nghiệm 2-2** (`chapter02/exp_2_2_turtle_serialization.py`) chứng minh round-trip equivalence qua Turtle, N-Triples, và RDF/XML.

### 2.1.4 SPARQL: Graph Pattern Matching

SPARQL là ngôn ngữ truy vấn cho RDF. Khác với SQL truy vấn bảng quan hệ, SPARQL **khớp mẫu đồ thị** (graph pattern matching).

#### Basic Graph Pattern (BGP)

Một BGP là tập hợp các **triple pattern**, trong đó mỗi vị trí có thể là biến (`?city`) hoặc hằng (IRI/literal):

```sparql
PREFIX ex: <http://example.org/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?city
WHERE {
    ?city rdf:type ex:City .
}
```

Kết quả là một tập hợp các **solution mapping** — mỗi solution mapping gán biến `?city` tới một IRI trong graph:

```
?city = http://example.org/Hanoi
?city = http://example.org/Paris
```

#### Shared Variables tạo Join

Khi hai triple pattern chia sẻ biến, SPARQL thực hiện join tự nhiên:

```sparql
SELECT ?capital ?country
WHERE {
    ?capital ex:capitalOf ?country .
    ?country rdf:type ex:Country .
}
```

Biến `?country` liên kết hai pattern. Kết quả:

```
?capital = Hanoi,  ?country = Vietnam
?capital = Paris,  ?country = France
```

#### FILTER và OPTIONAL

`FILTER` giới hạn solution mappings dựa trên điều kiện:

```sparql
SELECT ?city ?pop WHERE {
    ?city ex:population ?pop .
    FILTER (?pop > 5000000)
}
```

`OPTIONAL` mở rộng kết quả mà không loại bỏ solution khi pattern con không khớp:

```sparql
SELECT ?entity ?label WHERE {
    ?entity a ?type .
    OPTIONAL { ?entity rdfs:label ?label }
}
```

> ⚠️ **"SPARQL là SQL cho đồ thị"** chỉ là phép loại suy lỏng lẻo. SPARQL hoạt động trên cấu trúc đồ thị (graph structure), không trên bảng quan hệ. Variable binding trong SPARQL khác fundamentally với column selection trong SQL.

→ **Thí nghiệm 2-3** (`chapter02/exp_2_3_sparql_basic_patterns.py`) minh họa năm dạng truy vấn SPARQL với exact result bindings.

### Current Developments: RDF 1.2 và SPARQL 1.2

> 📌 **RDF 1.2** (W3C Candidate Recommendation, 2026-04-07) giới thiệu triple-term-based reification (`rdf:reifies`) như cơ chế hiện đại ưu tiên để tham chiếu mệnh đề. RDF 1.1 reification vocabulary vẫn tồn tại như legacy vocabulary cho tương thích ngược.
>
> 📌 **SPARQL 1.2** (W3C Working Draft, 2026-08-20) đang phát triển, bổ sung hỗ trợ cho RDF 1.2 features. Chưa ổn định để dùng làm baseline giảng dạy.
>
> **Chương này sử dụng RDF 1.1 / SPARQL 1.1 làm stable teaching baseline.**

## 2.2 Labeled Property Graph

*(Phần này sẽ được hoàn thiện trong work slice tiếp theo — Experiments 2-4, 2-5, 2-6)*

## 2.3 So sánh RDF và Property Graph

*(Experiment 2-6 — sẽ được hoàn thiện sau khi cả hai phía RDF và Property Graph đều đã implement)*

## Tóm tắt Chương 2 (RDF Half)

| Khái niệm | Điểm chính |
|-----------|-----------|
| RDF Graph | Tập hợp các triple (s, p, o); subject/predicate là IRI; object là IRI/Literal/BNode |
| Turtle | Cú pháp cụ thể cho RDF, không phải mô hình dữ liệu |
| Round-trip | Serialize → Parse bảo toàn graph equivalence |
| SPARQL | Graph pattern matching; variable binding tạo solution mappings |
| BGP | Tập hợp triple patterns; shared variables = natural join |
| Identity | IRI mang tính toàn cục; hỗ trợ Linked Data |
| Baseline | RDF 1.1 + SPARQL 1.1 là stable; RDF 1.2 / SPARQL 1.2 là emerging |

## Thí nghiệm

| ID | Tiêu đề | Difficulty | Status | File |
|----|---------|-----------|--------|------|
| 2-1 | RDF from first principles / RDFLib | ★★ | ✅ | `chapter02/exp_2_1_rdf_first_principles.py` |
| 2-2 | Turtle serialization round-trip | ★★ | ✅ | `chapter02/exp_2_2_turtle_serialization.py` |
| 2-3 | SPARQL Basic Graph Patterns | ★★ | ✅ | `chapter02/exp_2_3_sparql_basic_patterns.py` |
| 2-4 | Labeled Property Graph / Neo4j | ★★ | 🔲 Designed | *(chưa implement)* |
| 2-5 | Cypher traversal | ★★ | 🔲 Designed | *(chưa implement)* |
| 2-6 | Same knowledge — RDF vs Property Graph | ★★★ | 🔲 Designed | *(chưa implement)* |

## Nguồn tham khảo

- R11-01: RDF 1.1 Primer (W3C REC)
- R11-02: RDF 1.1 Concepts and Abstract Syntax (W3C REC)
- R11-05: RDF 1.1 Turtle (W3C REC)
- SP11-01: SPARQL 1.1 Overview (W3C REC)
- SP11-02: SPARQL 1.1 Query Language (W3C REC)
- TOOL-01: RDFLib documentation
- R12-01: RDF 1.2 Concepts (W3C CR) — *emerging*
- SP12-01: SPARQL 1.2 Query (W3C WD) — *emerging*

