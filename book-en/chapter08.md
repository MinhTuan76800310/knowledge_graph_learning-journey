# Chapter 8 — Inductive Knowledge and Learning from Graphs

> **Chapter orientation**
>
> **Central question:** Given many entities, relations, claims, mechanism applications,
> graph structures, and evidence-bearing examples — how can a system **generate NEW
> HYPOTHESES** from the regularities in a graph without mistaking statistical prediction
> for logical entailment or truth?
>
> **Why it matters:** The previous seven chapters built the graph (Ch1–2), identity (Ch3),
> semantics (Ch4), deduction (Ch5), epistemology (Ch6), and acquisition/integration (Ch7).
> All of them operate on knowledge *already asserted*. But new knowledge — beyond what the
> sources say — where does it come from? How can the system, from three applications of
> `RATE_OF_CHANGE` (velocity, electric current, inflation), propose "maybe all three are the
> same abstract mechanism"? How can it tell a genuine regularity from a spurious
> correlation? Chapter 8 opens the *inductive learning* rung: where the integrated graph
> becomes training data for models that generate candidate knowledge.
>
> **You will understand:**
>
> - The sharp boundary between **deduction**, **induction**, **abduction**, and
>   **prediction** — prediction ≠ entailment
> - How symbolic knowledge differs from statistical knowledge; representation learning
>   and knowledge graph embeddings (KGE)
> - TransE, DistMult, ComplEx — three scoring families with different inductive biases
> - The open-world assumption (OWA) and negative sampling: missing ≠ false
> - Link prediction and evaluation: MRR, Hits@K, filtered evaluation
> - Transductive learning vs inductive KG learning
> - Message passing, GNN, R-GCN, oversmoothing
> - Node representation vs subgraph representation; structural similarity and cosine similarity
> - Generating candidate mechanism hypotheses (CandidateMechanismHypothesis) from graph regularities
> - Rule induction with AMIE+; the "confidence" terminology collision with Ch6
> - The hybrid pipeline: ML generates candidates → symbolic filtering → epistemology
>   attaches evidence → governance decides
> - Cross-domain generalization, spurious correlation, hard negatives, calibration
> - Model provenance, self-reinforcing feedback loops, model collapse
> - When NOT to use graph ML — capability-based system decisions
> - The final boundary: what machine learning does not guarantee
>
> **Prerequisites:**
> - Chapters 1–2 (graphs, nodes, edges, types)
> - Chapter 3 (identity — entity ≠ embedding)
> - Chapter 4 (semantics, OWA, closed-world)
> - Chapter 5 (deduction, rules, SHACL)
> - Chapter 6 (epistemic model, Claim, Claim Ledger, Evidence, Assessment, provenance)
> - Chapter 7 (source acquisition, structuring RATE_OF_CHANGE, CandidateMechanismHypothesis §7.36)
>
> **Concept map:**
>
> Deduction/Induction/Abduction/Prediction → Symbolic vs Statistical knowledge →
> Representation learning → KGE (TransE, DistMult, ComplEx) → OWA + Negative sampling →
> Link prediction + Evaluation → Splitting & Leakage → Transductive vs Inductive graph
> learning → GNN (Message passing, R-GCN, Oversmoothing) → Subgraph representation →
> Structural similarity → Mechanism hypothesis generation → Rule learning → Hybrid
> pipeline → Cross-domain generalization → Calibration → Provenance & Feedback loops →
> Decide when to use/not use ML → What machine learning does not guarantee
>
> **Central distinction chain** (throughout the chapter, repeated many times):
> similarity ≠ identity; prediction ≠ entailment; high score ≠ truth; learned pattern ≠
> accepted knowledge.

## 8.0 Opening: Three Applications of One Mechanism

Chapter 7 ended with an open question: three sources (Calculus A, Mechanics B, Electronics
C) all describe "rate of change over time". After the pipeline, sources A and B together
strengthen `ex:claim_vroc` in the ledger; source C enters the review queue. But a subtle
detail surfaced in §7.36: "the structural similarity between two applications (velocity and
current through a capacitor) is a **hint** — it may lead to a candidate hypothesis about a
common abstract mechanism, but establishing that abstract identity belongs to inductive
learning (Chapter 8), not to the conclusion of this chapter."

Chapter 8 is that chapter.

Look at the following three applications from the perspective of a system learning from
graphs:

```
Application A (Velocity):
  quantity: Position
  operation: DerivativeOperation
  differentiand: Position
  withRespectTo: Time
  result: Velocity

Application B (Current through a capacitor):
  quantity: Charge
  operation: DerivativeOperation
  differentiand: Charge
  withRespectTo: Time
  result: Current

Application C (Inflation / Population growth):
  quantity: Population
  operation: DerivativeOperation
  differentiand: Population
  withRespectTo: Time
  result: GrowthRate
```

All three share an identical structure: an output quantity equals the derivative of an
input quantity with respect to time. But are they **the same mechanism**? The answer
depends on the level of abstraction: at the level of "derivative of a quantity with
respect to time", all three are `RATE_OF_CHANGE`. But at the level of detail: velocity is
the derivative of position, current is the derivative of charge, growth is the derivative
of population — they differ in domain and physical meaning.

Chapter 8 does not answer that question with an assertion. It builds the **tools for the
system to propose an answer itself**: representation learning, structural comparison,
hypothesis generation, evaluation, and decision. And most importantly — it builds the
boundary that keeps the system from **ever mistaking prediction for truth**.

> ⚠️ **Induction is not deduction.**
> This is the most important warning of the chapter. When a model learning from graphs
> "predicts" that `Velocity rateOfChangeOf Position` and `Current rateOfChangeOf Charge`
> share the same structure, that is a **statistical hypothesis**, not a logical entailment.
> The system must not treat it as a necessary consequence of the graph (Ch5). Every output
> of inductive learning is candidate knowledge and must pass through governance (Ch6)
> before entering the ledger.

> 🖊 **Self-check 1:** Before reading on, write down your answer: should the three
> applications above (velocity, current, growth) be viewed as "the same mechanism"? What is
> your reason based on — graph structure, physical meaning, or both? After §8.19 you will
> compare with how the system handles it.

## 8.1 Deduction, Induction, Abduction, and Prediction

Before building any model, the chapter must clarify the four categories of inference —
because confusing them is the source of the most dangerous errors in a knowledge system.

### 8.1.1 Deduction

Deduction is the category already built in Chapters 4–5: from general rules and specific
premises, the consequence follows necessarily. If the rules are true and the premises are
true, the conclusion is true. For example:

- If every `RateOfChangeApplication` has `operation DerivativeOperation` and
  `withRespectTo Time`, and `ex:velocity_1` is declared a `RateOfChangeApplication`, then
  deduction allows the conclusion `ex:velocity_1 operation DerivativeOperation`.

Deduction preserves truth. It is the backbone of automated reasoning over knowledge graphs
(Ch5). But it does not create new knowledge — it only makes explicit what was already
implicitly contained in the premises.

### 8.1.2 Induction

Induction generalizes from observations. It is the central category of this chapter.
According to Hogan and coauthors, inductive knowledge "concerns generalizing patterns from
a given set of input observations" and yields "new but possibly incorrect predictions"
assigned a level of confidence [@hogan-inductive].

- Example: from three applications (velocity, current, growth) sharing the same structure,
  the system proposes "perhaps all three are RateOfChangeApplications". This is induction —
  not necessary, possibly wrong, but useful.

Inductive knowledge in a knowledge graph comprises **both the model used to encode the
pattern and the predictions that model generates** [@hogan-inductive]. In other words, both
the embedding model itself and the candidate triples it proposes belong to induction.

> ⚠️ **Induction is not "deduction with more data".**
> Some naive presentations treat induction as "probabilistic deduction" — but this is a
> serious error. Deduction has explicit semantic rules; induction has a statistical model.
> Deduction preserves truth; induction generates hypotheses that can be wrong. Merging the
> two categories is the fastest way to corrupt the epistemic layer (Ch6).

### 8.1.3 Abduction

Abduction selects the hypothesis that best explains an observation. It differs from
induction in this way: induction generalizes from many examples to find a common pattern,
while abduction selects an explanation for one specific observation. This chapter does not
build abduction as a central mechanism, but distinguishes it from induction to avoid
terminology confusion.

### 8.1.4 Prediction

A prediction is the output of a learned model: it assigns a score to a possible
structure — for example, a triple (h, r, t) that never appeared in the training graph.
Predictions can be ranked, compared, evaluated — but they are **not entailments**.

> ⚠️ **Prediction ≠ entailment.**
> The triple `(ex:velocity_1, rateOfChangeOf, ex:position_1)` receiving a high score from a
> KGE model does not mean it is entailed by the graph. It only means the model "finds" it
> plausible based on learned patterns. This is the foundational difference: entailment is a
> logical relation, prediction is a statistical estimate.

Summary table of the four categories:

![The four inference categories: deduction (necessary), induction (generalization, possibly wrong), abduction (best explanation), prediction (model score).](figures/generated/ch08-reasoning-modes.pdf)

| Category | Input | Output | Truth-preserving? | Example |
|----------|-------|--------|-------------------|---------|
| Deduction | Rules + premises | Necessary consequence | Yes | R(A) → B |
| Induction | Observations | Generalized pattern / hypothesis | No | A₁..Aₙ have structure S → "perhaps every A has structure S" |
| Abduction | Observation + background knowledge | Best explanation | No | "Why does velocity change?" → "A force is acting" |
| Prediction | Model + input | Score / ranking | No | f(h,r,t) = 0.92 |

## 8.2 Symbolic Knowledge and Statistical Knowledge

Another important distinction to draw before building any learning model.

**Symbolic knowledge** consists of explicit structures that can be read and checked: RDF
triples, ontology axioms, deduction rules, SHACL constraints. Their meaning is fixed by
formal semantics (Ch4–5). The entire knowledge graph up through Chapter 7 is symbolic
knowledge.

**Statistical knowledge** consists of representations learned from data: embedding
vectors, model weights, scores, clusters. It has no formal semantics — a vector is not a
statement, and a score is not a truth value.

> ⚠️ **A vector is not a statement.**
> An embedding of `RateOfChangeMechanism` is a sequence of real numbers. That sequence
> asserts nothing. It cannot be used as a premise for deduction (Ch5), cannot be written
> into the ledger (Ch6), and cannot be cited as evidence (Ch6 §6.5). It is only a
> computational representation serving prediction.

Chapter 8 builds the bridge between these two worlds: statistical knowledge generates
candidate hypotheses — and those hypotheses, once assessed and governed, can become
symbolic knowledge. But the learning process itself does not directly produce symbolic
knowledge.

## 8.3 The Taxonomy of "Learning from Graphs" Problems

Before going technical, we need an overview of the kinds of learning problems on knowledge
graphs. Nickel and coauthors classify them into two large families
[@nickel-relational-ml-2016]:

1. **Latent feature models:** learn numeric representations (embeddings) for entities and
   relations, and use a scoring function to predict new triples. This is the focus of
   §8.4–8.20.
2. **Observable pattern mining:** learn symbolic rules from the graph, such as AMIE+
   (§8.22). This is the bridge back to symbolic knowledge.

Within the framework of this book, we add a third, architectural family:

3. **Hybrid pipeline:** combine both families above with the epistemic layer (Ch6) and
   governance (Ch7) to form a disciplined inductive learning system (§8.24).

Each family has its own strengths and weaknesses, and they complement each other rather
than compete.

## 8.4 Features, Representation Learning, and Embeddings

### 8.4.1 From hand-crafted features to learned representations

Before the deep-learning era, every learning model on graphs used **hand-engineered
features**: number of neighbors, relation type, node degree, shortest-path length, and so
on. This approach had the advantage of interpretability but was limited in that it did not
scale: every new task needed a new feature set, and features were not learned from data
[@hamilton-grl-2020].

**Representation learning** replaces hand-crafting with learning vectors from data. Each
entity and each relation is mapped into a d-dimensional vector space such that the
structural regularities of the graph are reflected in the geometry of that space.

### 8.4.2 Entity ≠ Embedding(Entity)

This is a foundational principle that must be engraved:

> ⚠️ **Entity ≠ Embedding(Entity).**
> The entity "velocity" (a physical concept with a definition, a formula, a meaning) is
> not identical to its embedding vector (a sequence of 100 real numbers). An embedding is a
> computational representation serving prediction, not the essence of the entity. Every
> inference from embeddings is an inference over representations, not over entities. This
> principle connects directly to Chapter 3: identity is a semantic relation, not a
> geometric one.

## 8.5 Knowledge Graph Embedding (KGE) and TransE

### 8.5.1 The KGE problem

Given a knowledge graph G = (E, R, T) with E the set of entities, R the set of relations,
and T the set of observed triples (h, r, t). A **knowledge graph embedding (KGE)** model
learns:
- A mapping ε: E → $\mathbb{R}^d$ (entity vectors)
- A mapping ρ: R → $\mathbb{R}^d$ or $\mathbb{R}^{d \times d}$ (relation vectors or matrices)
- A **scoring function** f: E × R × E → $\mathbb{R}$ assigning a real value to each triple

The higher (or lower, depending on convention) the value of f(h, r, t), the more plausible
the triple. Training objective: maximize the score of observed triples and minimize the
score of corrupted triples (negative samples) [@hogan-inductive].

### 8.5.2 TransE: h + r ≈ t

TransE is the foundational KGE model, proposed by Bordes and coauthors
[@bordes-transe-2013]. The idea is very simple: if the triple (h, r, t) holds, then the
vector of h **plus** the vector of r approximately equals the vector of t.

```
h + r ≈ t   →   f(h, r, t) = −‖h + r − t‖
```

(Here f is the score; a higher value — a smaller negative — means a more plausible triple.)

Example: if `Velocity` = ε(velocity), `rateOfChangeOf` = ρ(rateOfChangeOf), and
`Position` = ε(position), then the model expects:

```
Velocity + rateOfChangeOf ≈ Position
```

that is, "velocity is the rate of change of position".

The geometry of TransE is intuitive: each relation is a translation in the vector space.
If you know the positions of `Velocity` and `rateOfChangeOf`, you can "translate" to the
position of `Position`.

```
  Position ─────────────────────► Velocity
       ↑                           │
       └─────── rateOfChangeOf ─────┘
       (h + r ≈ t)
```

![TransE geometry: relations are translations in vector space, h + r ≈ t, and corrupted triples are pushed away by a margin loss.](figures/generated/ch08-transe-geometry.pdf)

> ⚠️ **h + r ≈ t is not a logical entailment.**
> The equation h + r ≈ t is a numerical approximation, not an inference rule. It has no
> formal semantics. That `Velocity + rateOfChangeOf ≈ Position` in embedding space does
> not mean "velocity is the rate of change of position" is a logical truth — it is only a
> statistical pattern learned from data. Only when that hypothesis passes through
> governance (Ch6) and is accepted does it become a statement with standing.

TransE has a well-known limitation: it handles 1–N, N–1, and N–N relations poorly, as
well as symmetric relations. For example, if one entity has many relations of the same
type to many different entities (like a `Student` taking many `Course`s), TransE cannot
place all the courses around the student with a single translation.

## 8.6 DistMult, ComplEx, and Inductive Bias

### 8.6.1 DistMult: bilinear scoring

DistMult (Yang and coauthors, 2015) belongs to the **bilinear** family of models: instead
of adding vectors, it multiplies element-wise and sums
[@yang-distmult-2015]:

```
f(h, r, t) = ⟨h, r, t⟩ = Σ_i h_i · r_i · t_i
```

where h, r, t are real d-dimensional vectors, and the element-wise product lets each
dimension of the space contribute independently to the score.

Limitation: DistMult is **symmetric** — f(h, r, t) = f(t, r, h). This means it cannot
distinguish `(Velocity, rateOfChangeOf, Position)` from `(Position, rateOfChangeOf,
Velocity)` — that is, it cannot model antisymmetric relations.

### 8.6.2 ComplEx: complex embeddings

ComplEx (Trouillon and coauthors, 2016) extends DistMult by using complex numbers instead
of real numbers [@trouillon-complex-2016]. The embedding of each entity and relation is a
complex number, and the scoring function is a Hermitian product:

```
f(h, r, t) = Re(⟨h, r, t̄⟩) = Re(Σ_i h_i · r_i · conj(t_i))
```

Complex numbers allow modeling both symmetric and antisymmetric relations within a single
framework, because the real part of the Hermitian product is not symmetric — it changes
when the roles of h and t are swapped.

ComplEx is a direct improvement over DistMult: it keeps linear computational complexity
while handling both kinds of relation.

### 8.6.3 Inductive Bias

Each KGE model family carries a different **inductive bias** — that is, structural
assumptions about which patterns are worth learning [@hamilton-grl-2020]:

| Model | Space | Bias | Strong at | Weak at |
|-------|-------|------|-----------|---------|
| TransE | $\mathbb{R}^d$ | h + r ≈ t (translation) | 1–1 relations | 1–N, N–1, symmetric relations |
| DistMult | $\mathbb{R}^d$ | ⟨h, r, t⟩ (symmetric bilinear) | Symmetric relations | Antisymmetric relations |
| ComplEx | $\mathbb{C}^d$ | Re(⟨h, r, t̄⟩) (Hermitian) | Both kinds | No fundamental weakness, but still assumes each relation is one linear transformation |

> ⚠️ **No model "understands" semantics.**
> All three models above are scoring functions with different geometric biases. None of
> them "understands" that "rate of change" is a differential concept, or that velocity and
> electric current are different physical phenomena. They only learn numerical
> correlations from data. This is why a KGE score is never used as epistemic evidence (Ch6)
> without an Assessment.

### 8.6.4 RotatE: Relations as Rotations in Complex Space

TransE uses **addition** (translation); DistMult and ComplEx use element-wise
**multiplication** (bilinear). RotatE (Sun and coauthors, 2019) chooses a different
geometric operation: **rotation** [@sun-rotate-2019]. To see why rotation is valuable, let
us return to a familiar object from elementary algebra: the complex number.

**Bridge from complex numbers.** A complex number $z = a + bi$ represents a point $(a, b)$
on the plane. The polar form $z = r e^{i\theta}$ (with $r = |z| = \sqrt{a^2 + b^2}$ and
Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$) reveals two components: a length
$r$ and an angle $\theta$. Multiplying two complex numbers **adds angles, multiplies
lengths**: $r_1 e^{i\theta_1} \cdot r_2 e^{i\theta_2} = r_1 r_2\, e^{i(\theta_1 +
\theta_2)}$. The key fact: multiplying by a complex number of **length exactly 1**
($|z| = 1$, i.e. $z = e^{i\theta}$) merely **rotates** the point by an angle $\theta$
without changing its distance to the origin. This is exactly the 2D rotation matrix from
linear algebra:

$$
\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}
\begin{pmatrix} a \\ b \end{pmatrix}
=
\begin{pmatrix} a\cos\theta - b\sin\theta \\ a\sin\theta + b\cos\theta \end{pmatrix}
$$

**The formula.** In RotatE, each entity and each relation is a $d$-dimensional vector of
complex numbers: $\mathbf{h}, \mathbf{t} \in \mathbb{C}^d$ and $\mathbf{r} \in
\mathbb{C}^d$. The relation is constrained to have **modulus 1 in every dimension**,
$|r_i| = 1$, so each dimension $i$ is just an angle $\theta_{r,i}$: a rotation. The triple
$(h, r, t)$ holds when $\mathbf{t}$ is the image of $\mathbf{h}$ under the element-wise
rotation (Hadamard product $\circ$):

$$
\mathbf{t} = \mathbf{h} \circ \mathbf{r}, \qquad
d_r(\mathbf{h}, \mathbf{t}) = -\|\mathbf{h} \circ \mathbf{r} - \mathbf{t}\|
$$

The score $d_r$ is the complex distance (modulus of the difference) — the closer to 0, the
more plausible the triple. Compared with TransE (adding an arbitrary vector), RotatE
**preserves the length** of the entity representation and only changes its direction: a
relation does not "drag" an entity along, it "rotates" it around the origin.

**The four relation patterns.** RotatE's real strength is that it can **describe by
structure** the four kinds of relation that TransE and DistMult handle poorly. For each
kind, the condition sits neatly in the rotation angle $\theta_{r,i}$:

| Relation pattern | Meaning | Condition on the rotation | Why |
|------------------|---------|---------------------------|-----|
| **Symmetry** | $r(x,y) \Rightarrow r(y,x)$ | $\theta_{r,i} \in \{0, \pi\}$, i.e. $r_i = \pm 1$ | Rotating by $0$ or $180^\circ$ and again returns you to the same place: $r \circ r = 1$ |
| **Antisymmetry** | $r(x,y) \Rightarrow \neg r(y,x)$ | $\theta_{r,i} \notin \{0, \pi\}$ | Rotating by an angle other than $0/\pi$ means rotating back does not return to the original point |
| **Inversion** | $r_1(x,y) \Leftrightarrow r_2(y,x)$ | $\mathbf{r}_2 = \bar{\mathbf{r}}_1$, i.e. $\theta_{r_2,i} = -\theta_{r_1,i}$ | The complex conjugate $\bar{z}$ flips the sign of the angle, i.e. rotates in the opposite direction |
| **Composition** | $r_1(x,y) \wedge r_2(y,z) \Rightarrow r_3(x,z)$ | $\mathbf{r}_3 = \mathbf{r}_1 \circ \mathbf{r}_2$, i.e. $\theta_{r_3,i} = \theta_{r_1,i} + \theta_{r_2,i}$ | Two successive rotations = one rotation by the sum of the angles |

These four are not four separate mechanisms — they are **a single mechanism** (complex
rotation) appearing under four different angle constraints. TransE can only describe
composition (vector addition) and antisymmetry; DistMult can only describe symmetry;
ComplEx describes symmetry and antisymmetry but does not preserve composition naturally.
RotatE unifies all four.

![The four relation patterns on the complex plane: symmetry (rotate 0/π), antisymmetry (rotate by another angle), inversion (conjugate = reverse rotation), composition (add angles). Each relation is a point on the unit circle |r_i|=1.](figures/generated/ch08-rotate-geometry.pdf)

A consolidated comparison of the four model families along exactly the geometric criteria
just analyzed:

| Criterion | TransE | DistMult | ComplEx | RotatE |
|-----------|--------|----------|---------|--------|
| Space | $\mathbb{R}^d$ | $\mathbb{R}^d$ | $\mathbb{C}^d$ | $\mathbb{C}^d$, $\|r_i\|=1$ |
| Relation transform | translation (add) | scaling (real multiply) | rotation + scaling | pure rotation |
| 1–N, N–1 relations | weak | good | good | good |
| Symmetry | no | **yes** | yes | **yes** ($\theta\in\{0,\pi\}$) |
| Antisymmetry | yes | no | yes | **yes** ($\theta\notin\{0,\pi\}$) |
| Inversion | no | no | no | **yes** ($\mathbf{r}_2=\bar{\mathbf{r}}_1$) |
| Composition | yes | no | no | **yes** ($\theta_3=\theta_1+\theta_2$) |

> 🖊 **Self-check:** In the mechanism system, the relation `hasInverseRateOfChange` links a
> rate of change with its "reverse-direction rate". Which condition in the table above does
> RotatE use to describe this relation, and how does its rotation angle relate to the angle
> of the original relation?
> *(Hint: the "Inversion" row — $\theta_{r_2,i} = -\theta_{r_1,i}$.)*

> ⚠️ **Describing a geometric pattern ≠ understanding the relation.**
> RotatE has the **expressivity** to fit symmetry/antisymmetry/inversion/composition
> patterns — but it still only optimizes a score over data. A triple fitting a rotation
> pattern does not prove it is **true** physically. A good geometric bias makes a
> hypothesis more credible; it does not turn a hypothesis into a law.

### 8.6.5 Hyperbolic Space and Poincaré Embeddings

All four models above live in **Euclidean** space (or the complex plane, essentially
2-dimensional Euclidean per coordinate). There is one class of structure that Euclidean
space represents **fundamentally poorly**: **hierarchy trees** — exactly what the
mechanism ontology (SubClassOf, the taxonomy `PhysicalMechanism → RateOfChange → ...`) is
full of.

**The Euclidean volume deficit.** In $\mathbb{R}^d$, the volume of a ball of radius $r$
grows **polynomially**: $\mathrm{Vol}_{\mathbb{R}^d}(r) \propto r^d$. But a tree with
branching factor $b$ has node count at depth $l$ growing **exponentially**: $N(l) \propto
b^l$. Embedding a large tree into low-dimensional Euclidean space forces nodes at deep
levels to **crowd** — or we must raise the dimension $d$ to unthinkable levels. This is not
a training-parameter problem; it is a **geometric mismatch** between polynomial volume
growth and exponential node growth.

**Hyperbolic space fixes this.** Hyperbolic geometry $\mathbb{H}^d$ has constant **negative
curvature** ($K = -1$). Under negative curvature, the circumference and volume of a sphere
grow **exponentially** with radius: $\mathrm{Vol}_{\mathbb{H}^d}(r) \propto \sinh^{d-1}(r) \sim \tfrac{1}{2^{d-1}} e^{(d-1)r}$. This exponential growth **matches** the
exponential growth of a tree. Intuition: on the Euclidean plane, a circle around the root
holds ever less "room" for branches; on a hyperbolic surface, the circumference inflates
fast enough that every level of the tree has enough space.

**The Poincaré disk model.** A convenient representation of $\mathbb{H}^d$ is the
**Poincaré disk/ball** $\mathbb{B}^d = \{\mathbf{x} \in \mathbb{R}^d : \|\mathbf{x}\| <
1\}$ — the entire hyperbolic space is "compressed" inside an open ball. The distance
between two points $\mathbf{u}, \mathbf{v}$ in the disk:

$$
d_{\mathbb{B}}(\mathbf{u}, \mathbf{v}) = \operatorname{arcosh}\!\left(1 + 2\,
\frac{\|\mathbf{u} - \mathbf{v}\|^2}{(1 - \|\mathbf{u}\|^2)(1 - \|\mathbf{v}\|^2)}\right)
$$

Read the formula with basic linear algebra: the numerator is the ordinary Euclidean
distance $\|\mathbf{u}-\mathbf{v}\|^2$; the denominator has two factors
$(1-\|\mathbf{u}\|^2)$ and $(1-\|\mathbf{v}\|^2)$ that **inflate without bound** as a
point approaches the boundary ($\|\mathbf{u}\| \to 1$). Consequence: two points near the
boundary, however close in Euclidean terms, are **very far apart in hyperbolic terms**.
$\operatorname{arcosh}$ (the inverse of $\cosh$) is just the transform that makes the
distance satisfy the geometric axioms.

**What it means for the Mechanism KG.** In a Poincaré embedding, **abstract root
mechanisms** (`PhysicalMechanism`, `RateOfChange`) sit **near the center**
($\|\mathbf{u}\| \approx 0$), while **concrete domain manifestations**
(`CurrentThroughCapacitor`, `InstantaneousVelocity`) sit **near the boundary**
($\|\mathbf{u}\| \to 1$). A node near the center can have **very many** descendants at the
outer ring while they remain far enough apart — exactly the property of a deep taxonomy.
Hyperbolic distance naturally encodes "parent–child" and "siblings": two mechanisms with
the same parent are close, the root mechanism is far from every leaf.

![The Poincaré disk B²: root mechanisms (RateOfChange, PhysicalMechanism) near the center, concrete domain manifestations expanding toward the boundary. The near-boundary region is distance-"magnified", allowing deep hierarchy trees to be embedded without crowding.](figures/generated/ch08-poincare-disk.pdf)

> ⚠️ **Hyperbolic is not "better" than Euclidean — it fits trees.**
> Poincaré embeddings win when the data has **strong hierarchical structure**. For graphs
> full of cycles, peer relations, or without a clear hierarchy, the advantage disappears
> and the computational complexity (optimization on a manifold, projection back onto the
> disk) only adds cost. Choose the geometry by the **structural shape** of the data, not
> by fashion.

> ℹ **Both RotatE and Poincaré are only geometric biases.** RotatE fits *relation
> patterns*; Poincaré fits *hierarchical shape*. Both are scoring functions, not proof
> engines. Their scores are **candidate-ranking signals**, not evidence — they still pass
> through the SHACL gate (Ch5) and acceptance governance (Ch6) before becoming knowledge.

## 8.7 The Open-World Assumption (OWA) and Negative Sampling

### 8.7.1 OWA: missing ≠ false

Knowledge graphs are never complete. If the triple `(ex:velocity_1, hasValue, 10)` is not
in the graph, that does not mean the velocity is not 10 — it only means the information
has not been acquired. This is the **open-world assumption (OWA)** introduced in Chapter 4.

OWA poses a major challenge for inductive learning: how do we create "negative" examples
for training if we do not know which triples are false?

### 8.7.2 Negative Sampling

The standard solution is **negative sampling** [@mikolov-negativesampling-2013]: from a
true triple (h, r, t), create a corrupted triple by replacing h or t with a random entity:

```
True triple:   (Velocity, rateOfChangeOf, Position)
Negative:      (Velocity, rateOfChangeOf, Mass)      ← replace Position with Mass
               (Acceleration, rateOfChangeOf, Position) ← replace Velocity with Acceleration
```

The model is trained to distinguish true triples (high score) from negative triples (low
score). This is a training trick, not an assertion about truth values.

![Negative sampling under the open-world assumption: a true triple yields negative samples by replacing the head or tail; negatives are training assumptions, not "false" assertions — and may be false negatives.](figures/generated/ch08-negative-sampling.pdf)

> ⚠️ **A negative sample ≠ a false triple.**
> The triple `(Velocity, rateOfChangeOf, Mass)` is used as a negative sample in training,
> but this does not mean "velocity is not the rate of change of mass". It only means that
> triple was randomly chosen as corruption. In a more complete graph, there may be some
> relation between velocity and mass (for example, momentum). Negative sampling is a
> technical assumption, not a claim about the world.

### 8.7.3 False Negatives

Because the graph is incomplete (OWA), a triple generated as a negative sample may
**actually be true** but not yet recorded. This is a **false negative**. For example, if
the graph does not yet contain `(Velocity, measuredIn, metersPerSecond)`, then the
negative sample `(Velocity, measuredIn, metersPerSecond)` produced by random replacement
is a false negative — it teaches the model that a true triple is false.

False negatives distort the learned boundary. The more false negatives, the more the model
"learns" that true triples are implausible, degrading prediction quality. This is a direct
consequence of OWA: there is no way to fully avoid false negatives, but they can be
reduced by choosing replacement entities more intelligently (for example, replacing only
with entities of the same type).

## 8.8 Link Prediction

Link prediction is the main application problem of KGE: given a partially observed graph,
predict the missing triples [@nickel-relational-ml-2016]. Concretely:

- **Given:** (h, r, ?) — find the best-fitting t
- **Given:** (?, r, t) — find the best-fitting h
- **Given:** (h, ?, t) — find the best-fitting r

The KGE model scores all candidates and ranks them from highest to lowest. The result is
an ordered list of candidate triples — not asserted facts.

> ⚠️ **High rank ≠ truth.**
> If the model ranks `(Velocity, rateOfChangeOf, Position)` at position 1, that does not
> mean the triple is true. It only means that, among all candidates, this triple has the
> highest score. Asserting it as fact requires independent evidence (Ch6) and governance
> (Ch7).

> 🖊 **Self-check 2:** Given a graph with three entities `Velocity`, `Position`, `Time` and
> the relation `rateOfChangeOf`. A TransE model learns vectors such that
> `Velocity + rateOfChangeOf ≈ Position`. If you add the entity `Acceleration` and retrain,
> what do you expect for `Acceleration + rateOfChangeOf ≈ ?` Explain.

## 8.9 Evaluating Link Prediction

### 8.9.1 MRR (Mean Reciprocal Rank)

For each true triple in the test set, the model ranks it among all candidates. MRR is the
mean of the reciprocal ranks:

```
MRR = (1/N) · Σ_i (1 / rank_i)
```

MRR = 1.0 means the true triple is always ranked 1. MRR = 0.5 means the true triple sits
at rank 2 on average. MRR is dominated by high ranks — a triple at rank 10 contributes
0.1, while at rank 2 it contributes 0.5.

### 8.9.2 Hits@K

Hits@K is the fraction of true triples that fall within the top K candidates:

```
Hits@K = (number of true triples with rank ≤ K) / N
```

Hits@10 = 0.8 means 80% of true triples are in the top 10. Hits@K does not distinguish
between rank 1 and rank K — both count as a "hit" [@bordes-transe-2013].

### 8.9.3 Raw and Filtered Evaluation

A subtle problem: when ranking, other true triples (not the one being tested) also appear
in the candidate list. If they rank above the triple being tested, they are counted as
"wrong" even though they too are true.

**Raw evaluation** does not remove other true triples from the ranking list. **Filtered
evaluation** removes all known true triples from the list before ranking, keeping only the
target triple and candidates that genuinely do not appear in the graph
[@bordes-transe-2013] [@nickel-relational-ml-2016].

> ⚠️ **Filtered evaluation ≠ truth evaluation.**
> Filtered evaluation only removes *known* true triples. It knows nothing about true
> triples that have not been recorded (OWA). So filtered evaluation is a technical
> improvement, not a measure of absolute truth.

## 8.10 Data Splits and Leakage

### 8.10.1 Train / Validation / Test

To evaluate a model, we split the dataset into three parts:
- **Train:** used to learn the model's parameters
- **Validation:** used to choose hyperparameters
- **Test:** used for the final evaluation, never seen during model development

On a knowledge graph, splitting is not as simple as randomly splitting triples, because
triples are interrelated through shared entities.

### 8.10.2 Data Leakage

Data leakage occurs when information from the test set leaks into the training process,
making evaluation scores artificially optimistic. In knowledge graphs, there are many
kinds of leakage:

- **Duplicate leakage:** the same triple appears in both train and test
- **Inverse-relation leakage:** if train has (h, r, t) and test has (t, r⁻¹, h), the model
  can "cheat" by learning the inverse relation
- **Path leakage:** train has (A, r1, B) and (B, r2, C), test has (A, r3, C) — the model
  can learn r3 = r1 ∘ r2
- **Entity leakage:** an entity in the test set already appeared in the train set,
  carrying information about its relations
- **Temporal leakage:** the train set contains future data, the test set contains past
  data — the model "predicts" the past based on the future
- **Source leakage:** the same source (for example, the same book) appears in both train
  and test, overstating generalization ability

> ⚠️ **No leakage does not prove the model understands mechanisms.**
> A leakage-free model can still learn surface correlations (spurious correlations) rather
> than real mechanism structure. No leakage only means a cleaner evaluation, not a correct
> model. This issue is discussed in detail in §8.26.

## 8.11 Transductive Learning and Inductive KG Learning

### 8.11.1 Transductive Learning

The KGE models of §8.5–8.6 are **transductive**: they learn one vector per entity seen in
training, and can only predict links **between known entities**. If a new entity appears
after training, the model has no vector for it.

This suits the "graph completion" problem: the entities are already in the graph, only the
links are missing.

### 8.11.2 Inductive KG Learning

But if the system must predict over **new, never-seen entities** — for example, a new
chapter of a physics textbook introduces `ElectromotiveForce`, which never appeared before
— a transductive model is unusable. This is **inductive KG learning**: the model must
generalize to unseen entities/subgraphs [@teru-grail-2020].

> ⚠️ **Transductive ≠ inductive.**
> A standard KGE model is transductive, not inductive (in the graph-learning sense). It
> does not generalize to new entities. If the mechanism system must face new concepts from
> new domains (a very realistic requirement for the RATE_OF_CHANGE mechanism across
> different books), inductive methods such as subgraph-based GNNs are needed
> (§8.16–8.17).

## 8.12 Out-of-Vocabulary (OOV) Entities and the Motivation for GNNs

### 8.12.1 The OOV problem

An **out-of-vocabulary entity (OOV)** is an entity with no learned vector because it never
appeared in training. The embedding lookup table cannot handle it — it only has vectors for
entities it has seen.

How do we produce a representation for a new entity? Three directions:
1. From its own **attributes/text** (if available)
2. From its **neighborhood** — the entities and relations around it
3. From the **subgraph structure** containing it — using an identity-independent encoder

The third direction leads directly to subgraph-based GNNs: instead of learning a vector
per entity, the model learns how to **compute** a representation from the surrounding
structure. Such a model can be applied to any subgraph, including subgraphs with entirely
new entities [@teru-grail-2020].

## 8.13 GNN Intuition: Learning from Neighborhoods

A **Graph Neural Network (GNN)** is a family of models whose computation follows the graph
structure: a node's representation is computed from the representations of itself and its
neighboring nodes, across multiple layers [@hamilton-grl-2020].

Intuition: the representation of the node "Velocity" in a RATE_OF_CHANGE application is
computed from the nodes around it — `Position`, `Time`, `DerivativeOperation`,
`Quantity` — through their respective relations.

```
          Position ──hasQuantity──► Application_A
          Time     ──withRespectTo► Application_A
          DerivativeOperation ──operation──► Application_A
          Application_A ──result──► Velocity
```

After one message-passing layer, the representation of `Velocity` contains information
about its neighbors. After several layers, it contains information about farther neighbors
(multi-hop). This lets a GNN capture the local structure around each node — exactly what a
fixed embedding cannot do.

![Message passing around a mechanism application: a node's representation is computed from messages of its neighbors along each relation, aggregated and updated, layer by layer.](figures/generated/ch08-message-passing.pdf)

## 8.14 Message Passing

### 8.14.1 The general formula

The general formula of a GNN layer is a three-step chain: **message → aggregate →
update** [@hamilton-grl-2020].

```
For each node v and each layer k:
  1. Message:   m_{u→v} = MESSAGE(h_u^(k), h_v^(k), edge(u,v))
  2. Aggregate: m_v      = AGGREGATE({m_{u→v} | u ∈ N(v)})
  3. Update:    h_v^(k+1) = UPDATE(h_v^(k), m_v)
```

- **MESSAGE** computes a message from neighbor u to node v, possibly depending on the edge
  type
- **AGGREGATE** collects all messages arriving at v (sum, mean, max, attention, ...)
- **UPDATE** combines v's current representation with the aggregated message

Important note: this is a **conceptual framework**, not a single algorithm. Each concrete
GNN is one instantiation of this framework with different choices for the three functions
above.

> ⚠️ **One formula does not define every GNN.**
> Many articles present "a GNN is formula X". Wrong: GNN is a *family* of models. The
> differences among family members lie in the choice of MESSAGE, AGGREGATE, UPDATE.
> Reading one concrete formula and calling it "the GNN" misses the entire design space.

### 8.14.2 Why does message passing help learn mechanisms?

For the RATE_OF_CHANGE system: if a GNN learns that a node with `operation
DerivativeOperation`, `withRespectTo Time`, and `hasQuantity Q` tends to have a `result`
that is a RateOfChangeApplication, then when it meets a new application (for example,
`GrowthRate` of a population), the GNN can **reuse** the learned pattern without knowing
`GrowthRate` in advance.

This is precisely the power of inductive learning on graphs: the model learns *how* to
compute representations from structure, not the fixed *values* of each entity.

### 8.14.3 Expressivity Limits: the Weisfeiler-Lehman Test (1-WL)

Although the **message → aggregate → update** framework is very flexible, a foundational
theorem of modern graph learning says: **most standard GNNs (GCN, GAT, R-GCN) are capped
exactly at the expressivity of the single Weisfeiler-Lehman test (1-WL)**
[@morris-weisfeiler-2019; @xu-gin-2019]. Understanding 1-WL tells us what a GNN *cannot
do* — as important as knowing what it *can do*.

**What is the 1-WL test?** It is an iterative **color refinement** algorithm:

```
Step 0:    assign each node an initial color c_v^(0) = hash(label(v))
Step t+1:  c_v^(t+1) = hash( c_v^(t), { c_u^(t) | u ∈ N(v) } )
Stop:      when the color partition stops changing
```

Here `{ c_u^(t) | u ∈ N(v) }` is a **multiset** — a neighbor list in which colors may
repeat. At each step, a node receives a new color based on **its own old color** and the
**multiset of its neighbors' colors**. If after step $t$ two graphs have different color
partitions, they are certainly not isomorphic. If 1-WL cannot distinguish two graphs, they
may still differ — 1-WL is only a sufficient, not necessary, method.

**Bridge to message passing.** Look again at the message-passing formula: each node
collects information from neighbors and then updates itself. 1-WL does the same thing, but
with **discrete colors** (hashes) instead of real vectors. Morris et al. (2019) and Xu et
al. (2019) proved that: **an MPNN is as expressive as 1-WL if and only if its aggregation
(AGGREGATE) and update (UPDATE) functions are injective**. This explains the **Graph
Isomorphism Network (GIN)** architecture:

$$
\mathbf{h}_v^{(k+1)} = \text{MLP}\!\left((1 + \epsilon)\,\mathbf{h}_v^{(k)} + \sum_{u \in \mathcal{N}(v)} \mathbf{h}_u^{(k)}\right)
$$

The $(1+\epsilon)$ coefficient and the multiset sum (rather than mean/max) are deliberate:
they preserve information about **how many** neighbors have each color — what is needed for
injectivity. GCN uses mean, GAT uses attention-weighted mean: both **lose** the counting
information, so neither can exceed 1-WL.

| Question | Can 1-WL / MPNN answer it? |
|----------|---------------------------|
| Do two graphs have the same final color partition? | Yes — the algorithm stops at a stable partition |
| Distinguish any two graphs? | **No** — many pairs of distinct graphs receive the same colors |
| Count triangles $C_3$? | **No** — requires knowing 3-node structure, not just 1-hop |
| Count cycles $C_k$? | **No** — same as triangles |
| Distinguish cyclic vs linear structure in mechanisms? | **No** — if node degrees match |

> 🖊 **Self-check:** A GNN using `mean` aggregation on a graph where every node has exactly
> 3 neighbors. Why can it not distinguish a 3-node feedback loop (A→B→C→A) from a 3-node
> path with the same number of neighbors per node? *(Hint: mean loses "who is who"
> information and keeps only the average.)*

> ⚠️ **Homogenization power ≠ deduction.**
> The 1-WL theorem says an MPNN can learn enough to **distinguish** the structures 1-WL can
> distinguish. It does not say the MPNN understands the *physical meaning* of a structure.
> A GNN can learn to tell "loop or no loop" via vectors — yet still not know whether that
> loop is negative feedback or one link in a causal chain. GNN scores are signals; meaning
> must be attached by the ontology (Ch4) and acceptance governance (Ch6).

## 8.15 R-GCN: Message Passing by Relation Type

**R-GCN (Relational Graph Convolutional Network)** is a GNN designed for
**multi-relational** graphs [@schlichtkrull-rgcn-2018]. The main idea: each relation type r
has its own transformation matrix W_r in the update step.

```
h_v^(k+1) = σ( W_self · h_v^(k)  +  Σ_{r} Σ_{u∈N_r(v)} (1/c_v) · W_r · h_u^(k) )
```

where N_r(v) are v's neighbors via relation r, c_v is a normalization constant, and W_r is
the transformation specific to relation r.

Why does this matter? In the mechanism graph, different relations carry very different
meanings: `operation`, `hasQuantity`, `withRespectTo` (reference quantity), `result`,
`derivativeApplication`. If all these relations are merged into one relation-blind
aggregation, the model loses the ability to distinguish the role of each relation — and
those roles are exactly what determines mechanism structure.

R-GCN is typically used as an **encoder** (computing node representations from structure),
paired with a **decoder** (such as DistMult) for link prediction: the encoder produces
representations, the decoder scores triples.

> ⚠️ **Never merge all relations into one aggregation.**
> If you fold `operation`, `withRespectTo`, `result` into a single sum, you disable the
> model's ability to distinguish the semantic role of each relation. On a knowledge graph
> (multi-relational), this is a design error.

## 8.16 Oversmoothing: Deeper Is Not Necessarily Better

A dangerous phenomenon in GNNs: stacking many layers makes node representations **converge
toward each other** and lose distinguishing information. This is called **oversmoothing**.

Li and coauthors proved that GCN's aggregation is equivalent to **Laplacian smoothing** on
the graph: each aggregation layer "blends" node representations together
[@li-oversmoothing-2018]. With too many layers, every node ends up with an almost identical
representation and prediction quality collapses.

```
Layer 1: representations well distinguished
Layer 2–3: still distinguishable
Layer 5–10: convergence — every node nearly identical (oversmoothing)
```

> ⚠️ **More GNN layers does not mean deeper understanding.**
> The intuition "stack more layers to understand more deeply" is wrong for GNNs: past a
> certain number of layers, oversmoothing makes all representations converge and destroys
> distinguishability. The optimal number of layers is usually very small (1–3) and depends
> on the task.

## 8.17 Node Representations and Subgraph Representations

### 8.17.1 Two levels of representation

So far we have talked about **node representations**: one vector for one node, containing
information about its neighborhood. But the mechanism system needs to compare **mechanism
applications** — and an application is a structure of many nodes (quantity, operation,
differentiand, withRespectTo, result).

To compare two applications as wholes, we need a **subgraph representation**: pooling the
representations of the nodes in a subgraph into a single vector via a **pooling/readout**
operation — for example, mean, max, or a learned layer [@hamilton-grl-2020].

> ⚠️ **Node representation ≠ subgraph representation.**
> The vector of the node `Application_A` is not the vector of application A as a whole. If
> you compare two applications by the vectors of their central nodes, you ignore the entire
> surrounding structure — quantity, operation, withRespectTo — which is the most important
> part of the mechanism structure.

### 8.17.2 A design choice, not a definition

Pooling is a **design choice**: how you select the aggregation function (mean, max,
attention, ...) decides which subgraph information is retained. No pooling is absolutely
"correct". More important: the pooled vector is not the "meaning" of the subgraph — it is
only a numerical summary serving a particular task.

### 8.17.3 When 1-WL Is Not Enough: Counting Cycles and Loop Mechanisms

The 1-WL limit of §8.14.3 is not an idle theoretical curiosity — it **touches directly**
the mechanism system's task. Consider a classic counterexample where 1-WL is **powerless**.

**Counterexample: the decagon $C_{10}$ vs two pentagons $2 \times C_5$.** Consider two
graphs: (a) a single cycle of length 10 (a decagon), and (b) two disjoint cycles of length
5 each (two pentagons). Both are **2-regular** (every node has exactly 2 neighbors) and
have the same node count (10). Run 1-WL: at step 0 every node has the same color (same
label); at each later step, every node sees the identical neighbor multiset $\{color,
color\}$, so every node **keeps the same color** at every step. The final color partitions
of the two graphs are **identical**. Conclusion: **no 1-WL MPNN can distinguish $C_{10}$
from $2 \times C_5$**, even though they clearly differ in global structure.

![A pair of non-isomorphic graphs that 1-WL cannot distinguish: the decagon C₁₀ (one 10-node cycle) and two disjoint pentagons 2×C₅ (two 5-node cycles). Both 2-regular; 1-WL colors every node the same at every step.](figures/generated/ch08-1wl-isomorphism.pdf)

**Consequence for the Mechanism KG.** This is the worrying part for this book. A **closed
feedback-loop mechanism** ($A \to B \to C \to A$, e.g. the thermostat loop: temperature →
error → fuel valve → temperature) and a **linear amplification chain** with the same node
degrees *look identical* to a standard MPNN. The model cannot, by 1-WL message passing
alone, know that one of the two has a **feedback link** — and feedback is exactly what
produces the dynamic behavior (stability, oscillation, instability) that Chapter 10 will
exploit. To distinguish them, one must **add structural signal** that 1-WL does not see on
its own.

**Breaking the 1-WL ceiling.** There are three main architectural directions:

1. **Higher-order GNNs ($k$-WL, $k \ge 3$):** instead of coloring single nodes, color
   **tuples of $k$ nodes** with roles distinguished. Power grows with $k$ (more precisely:
   more pairs become distinguishable), but cost grows as $O(n^k)$ — unusable for large
   graphs.
2. **Subgraph GNNs:** run many MPNNs over **subgraphs** selected deliberately (for example,
   each node is "marked" once — node marking), then combine the representations. Short
   cycles become countable because each marking breaks local symmetry.
3. **Graph Transformers (Graphormer, TokenGT):** drop the rigid neighbor-aggregation
   mechanism entirely and use **whole-graph self-attention** plus **structural positional
   encodings** — shortest-path distance, degree centrality, and **learned spatial bias** on
   each node pair. Because attention sees **pairs** $(u,v)$ together with path metadata, it
   distinguishes structures that 1-WL merges.

| Architecture | Expressivity | Counts cycles? | Cost |
|--------------|--------------|----------------|------|
| Standard MPNN (GCN/GAT/R-GCN) | $=$ 1-WL | No | $O(|E|)$ per layer |
| GIN | $=$ 1-WL (maximal injectivity) | No | $O(|E|)$ per layer |
| $k$-WL GNN | $=$ $k$-WL | Yes (for large enough $k$) | $O(n^k)$ |
| Subgraph GNN | Beyond 1-WL | Yes (short cycles) | $O(n \cdot |E|)$ |
| Graph Transformer | Beyond 1-WL | Yes (via path bias) | $O(n^2)$ |

> ⚠️ **Beating 1-WL is not free.**
> Every architecture that breaks the ceiling pays with greater computational cost or
> memory, and is usually **less robust** on small data. For small-to-medium mechanism
> graphs, a standard MPNN plus **explicit structural features** (cycle counts, presence of
> feedback edges, loop paths) is often more pragmatic than a full Graph Transformer. Do not
> upgrade the architecture to solve a problem that one well-placed feature solves.

> ℹ **The through-line lesson:** expressivity is an **upper bound** on what a model *can*
> learn, not what it *will* learn. An architecture beyond 1-WL can still fail to learn loop
> structure if the training data lacks loop examples. Conversely, when the architecture is
> capped at 1-WL, all training effort is futile — the model **in principle** cannot
> distinguish the two mechanisms. Choose the architecture first, train second.

## 8.18 Structural Similarity and Cosine Similarity

### 8.18.1 Structural Similarity

With subgraph representations, we can measure how alike two mechanism applications are.
**Structural similarity** is a multi-dimensional assessment: two structures are similar
when they share role patterns — the same operation, the same role pattern, compatible
argument types, the same function shape, the same neighborhoods.

This is not a single number: it is a multi-dimensional vector of evidence.

> ⚠️ **Similarity ≠ identity.**
> Two applications with nearly identical structure (velocity and electric current) are
> still **two different entities**. Structural similarity is hinting evidence, not
> identification (Ch3: owl:sameAs is a semantic relation, not a geometric one).

### 8.18.2 Cosine Similarity

**Cosine similarity** measures the cosine of the angle between two vectors:

```
cos(a, b) = (a·b) / (‖a‖·‖b‖)
```

The value lies in [−1, 1]: 1 means same direction, 0 means orthogonal, −1 means opposite
direction.

A working example: two 3-dimensional vectors

```
a = (2, 0, 0),  b = (3, 0, 0)  →  cos = 1     (same direction)
a = (2, 0, 0),  c = (0, 5, 0)  →  cos = 0     (orthogonal)
a = (2, 0, 0),  d = (−1, 0, 0) →  cos = −1    (opposite direction)
```

High cosine in embedding space often accompanies similar neighborhood structure — but it
never by itself proves semantic identity.

> 🖊 **Self-check 3:** Compute the cosine similarity between a = (1, 2, 3) and b = (4, 5,
> 6). (Hint: a·b = 32, ‖a‖ = √14, ‖b‖ = √77.) What does the result say about the direction
> of the two vectors — and what does it NOT say about their meaning?

## 8.19 Generating Candidate Mechanism Hypotheses

### 8.19.1 The hypothesis-generation pipeline

Now we assemble everything into a mechanism-hypothesis generation pipeline:

```
1. Extract the subgraph of each application (Quantity, Operation, Differentiand,
   WithRespectTo, Result)
2. Compute subgraph representations with GNN + pooling (inductive, handles new entities)
3. Measure structural similarity between application pairs (multi-dimensional, not just cosine)
4. Group applications into candidate clusters (clustering, §8.28)
5. For each cluster, propose a CandidateMechanismHypothesis:
   "these applications may be one abstract mechanism"
6. Attach: structural evidence, source support, uncertainty, competing
   hypotheses, provenance (which model, which data)
7. Enter the Claim Ledger as CandidateKnowledge (Ch6), awaiting assessment and governance
```

### 8.19.2 CandidateMechanismHypothesis

The candidate mechanism hypothesis is a book-defined concept (BOOK-DEFINED), continuing
the hook at §7.36. It is a special kind of **claim**: its content is "these applications
may be one mechanism", and it carries:

- **Learned evidence** (structure, similarity, clustering)
- **Source support** (the sources describing each application)
- **Uncertainty** (multi-source uncertainty, §8.32)
- **Competing hypotheses** (for example: one shared abstract mechanism vs three separate
  mechanisms that merely look alike)
- **Full provenance** (which model, which data version, when)

Important: the hypothesis is a **candidate**. It is not accepted knowledge.

> ⚠️ **Pattern ≠ mechanism.**
> The pipeline above only generates *hypotheses*. A group of applications with similar
> structure is a **pattern**. It becomes an *asserted mechanism* only after passing
> epistemic assessment (Ch6), comparison with competing hypotheses, counterexample
> checking, and acceptance governance. Jumping from pattern to mechanism while skipping
> these steps is the most dangerous error of inductive learning.

## 8.20 Abstracting RATE_OF_CHANGE: A Worked Example

Back to the opening question. The system sees three applications:

```
Application A (Velocity):   Operation=Derivative, Differentiand=Position,
                            WithRespectTo=Time, Result=Velocity
Application B (Current):    Operation=Derivative, Differentiand=Charge,
                            WithRespectTo=Time, Result=Current
Application C (Growth):     Operation=Derivative, Differentiand=Population,
                            WithRespectTo=Time, Result=GrowthRate
```

The abstraction steps:

1. **Remove incidental differences:** replace `Position`, `Charge`, `Population` with the
   variable `Quantity`; replace `Velocity`, `Current`, `GrowthRate` with the variable
   `Result`.
2. **Keep the invariant structure:** `Operation=Derivative`, `WithRespectTo=Time`, and the
   role pattern `Quantity → Derivative → Result`.
3. **Propose the hypothesis:** "perhaps all three are applications of the abstract
   mechanism `RateOfChange`".

```
Position ──differentiand──► Velocity        Quantity ──differentiand──► Result
    ▲                            ▲              ▲                            ▲
    └────── withRespectTo ───────┘   +  Time    └────── withRespectTo ───────┘
   (original structure)                     (abstracted structure)
```

![RATE_OF_CHANGE abstraction: three applications (Velocity, Current, Growth) share one role pattern; the invariant structure (Operation=Derivative, WithRespectTo=Time, Quantity→Derivative→Result) is kept, domain names are removed as incidental detail.](figures/generated/ch08-invariant-abstraction.pdf)

**But** — the system does not stop there. It must ask the following questions:

- Does `RateOfChange` at this level of abstraction keep its meaning when applied to
  population? (Population growth is a discrete ratio, unlike the instantaneous derivative
  of position.)
- Is there a better competing hypothesis? (For example: velocity and current are
  "time-derivatives of a physical quantity", while growth is a "relative rate of change
  over time" — two different families.)
- Which source evidence supports or does not support this level of abstraction?

Abstraction is a **structured hypothesis**, not a naive variable substitution. Swapping
`Position` for `Quantity` is easy; deciding which level of abstraction preserves meaning is
hard and requires assessment.

> 🖊 **Self-check 4:** In your view, which level of abstraction is right for the three
> applications? Are all "time derivatives" the same mechanism? If you need to distinguish
> "instantaneous derivative" (velocity) from "discrete rate of change" (population growth),
> which graph structure distinguishes them — and which part requires text/semantics?

## 8.21 Invariant Structure, Incidental Structure, and "Representation Determines Learnability"

### 8.21.1 Invariant and Incidental

When abstracting, the model (or a human) proposes an **invariant structure** — the part
that is kept — and an **incidental structure** — the domain detail that is dropped.

For the example above:
- **Invariant (proposed):** Operation=Derivative, WithRespectTo=Time, the role pattern
  Quantity → Derivative → Result
- **Incidental (proposed):** the domain names (Position vs Charge vs Population), the
  specific physical meaning

Separating invariant from incidental is a **learning problem** — not something obvious. And
this boundary depends on the level of abstraction the system chooses.

### 8.21.2 Representation determines learnability

One important principle: **representation determines learnability**. A model can only
learn from what it sees. If the feature schema does not include `WithRespectTo` (for
example, modeling applications only with `Operation` and `Result`), then no amount of data
will help the model learn that `WithRespectTo=Time` is part of the mechanism structure —
that information has been removed from the representation.

This connects directly to §8.4 (features before embeddings): choosing the representation is
a design decision with semantic consequences, not a harmless technical detail.

> ⚠️ **A model cannot learn what is not in its input.**
> If `WithRespectTo` is not included in the application's representation, the model will
> never "discover" that temporal reference is the invariant part of the mechanism. This is
> the recollection boundary of machine learning: garbage in, garbage out — but at the
> schema level, not the value level.

## 8.22 Rule Induction and AMIE+

### 8.22.1 Path rules

Besides KGE and GNNs, there is another inductive-learning family that produces **symbolic
rules** instead of vectors: **rule induction**. AMIE+ is one of the large-scale rule
mining systems over knowledge graphs, operating under the open-world assumption
[@galarraga-amie-2015].

A **path rule** has the form:

```
r1(x, y) ∧ r2(y, z) → r3(x, z)
```

Example in the mechanism system:

```
hasOperation(x, Derivative) ∧ withRespectTo(x, Time) → resultIsRateOfChange(x)
```

meaning: if x has operation Derivative and references Time, then x's result is a rate of
change.

AMIE+ finds such rules by mining paths in the graph and measuring their support and
confidence.

### 8.22.2 Support and Confidence in Rule Mining

- **Support:** the number of rule instantiations in the graph — how many times body and
  head co-occur.
- **Confidence:** in AMIE+, confidence is computed under the **Partial Completeness
  Assumption (PCA)**: if an entity already has at least one value for the rule-head
  relation, assume its value set is complete — so absent values count as "known
  counterexamples" [@galarraga-amie-2015].

PCA confidence lets rule mining work under OWA without being punished too harshly for
missing information — but it is a strong technical assumption.

> ⚠️ **Rule-mining "confidence" ≠ Chapter 6 "confidence".**
> Chapter 6 builds epistemic confidence: a multi-dimensional assessment of evidence,
> sources, conflict, time — the *reasons to believe*. AMIE+'s PCA confidence is a
> statistical frequency over a particular dataset under a strong completeness assumption.
> This is a **terminology collision**: two different concepts sharing the name
> "confidence". This chapter — and the book — always distinguishes them with full terms:
> "rule-mining confidence" vs "epistemic confidence".

### 8.22.3 Learned Rules Are Hypotheses

A rule with high support and high PCA confidence is still a **hypothesis**: it describes a
pattern in data, not a logical law. It becomes a valuable inference rule only when:
1. It is semantically assessed (consistent with the Ch4 ontology)
2. It is counterexample-checked (§8.42)
3. It is accepted by governance (Ch6)
4. It enters the controlled rule set (Ch5)

> ⚠️ **A learned rule ≠ a logical law.**
> Inserting a learned rule directly into the inference engine (Ch5) is a serious error: it
> turns a statistical hypothesis into a truth-preserving axiom, and every wrong consequence
> propagates across the whole graph.

### 8.22.4 Differentiable Rule Learning (Differentiable Logic Programming)

AMIE+ mines rules in a **discrete** way: it enumerates path patterns, counts support,
computes PCA confidence, and returns the rules that pass thresholds. Advantages: fast,
clear, transparent. Disadvantages: (1) no **end-to-end** training by gradient, (2) hard to
optimize objectives involving long inference chains or noisy graphs, (3) rules more complex
than a few links must be found by very large combinatorial search. **Differentiable rule
learning** (differentiable rule learning / differentiable Inductive Logic Programming)
emerged to fill this gap [@yang-neurallp-2017; @sadeghian-drum-2019; @evans-dilp-2018].

**Relations as matrices.** Let $\mathcal{R}$ be the set of relations. Each relation $r$ is
represented by an adjacency matrix $\mathbf{M}_r \in \{0,1\}^{|V| \times |V|}$, where
$[\mathbf{M}_r]_{ij} = 1$ means there is an edge $i \xrightarrow{r} j$. If you have learned
basic linear algebra, $\mathbf{M}_r$ is just a sparse matrix recording the graph per
relation — very much like an ordinary adjacency matrix.

**Softmax relaxation in Neural LP.** Neural LP builds a rule of length $T$ links in matrix
form:

$$
\mathbf{A}_t = \sum_{r \in \mathcal{R}} \alpha_{t,r}\, \mathbf{M}_r, \qquad
\sum_{r} \alpha_{t,r} = 1, \quad \alpha_{t,r} > 0
$$

At each step $t$, the model chooses a probability distribution (softmax) over relations:
$\boldsymbol{\alpha}_t \in \Delta^{|\mathcal{R}|}$. The combined matrix $\mathbf{A}_t$ is a
**weighted average** of adjacency matrices. The composed rule is a chain of matrix
products:

$$
\mathbf{P} = \mathbf{A}_1 \mathbf{A}_2 \cdots \mathbf{A}_T
$$

By linear algebra, $\mathbf{P}_{ij}$ gives the soft probability (or score) of a path from
$i$ to $j$ in $T$ steps. For a query $(h, r_{target}, ?)$, the answer scores are computed
as $\mathbf{s} = \mathbf{e}_h^{\top} \mathbf{P}$. Every parameter $\alpha_{t,r}$ is
differentiable, so the model is optimized by **gradient descent** through cross-entropy
loss, just like classification.

**DRUM extends Neural LP with an RNN over paths.** DRUM (Sadeghian and coauthors, 2019)
observes that $\alpha_t$ need not be independent across steps but can depend on earlier
steps, for example through a hidden RNN. This allows learning longer rules with fewer
candidates and better generalization.

**Rule extraction after training.** Once we have $\alpha_{t,r}$, we can extract a discrete
rule by choosing the highest-weight relation at each step: $r_t = \arg\max_r \alpha_{t,r}$.
This rule looks like an AMIE+ rule, but it was chosen to **minimize prediction loss**, not
to maximize support/PCA confidence. That is an important difference.

> 🖊 **Self-check:** In the formula $\mathbf{P} = \mathbf{A}_1 \mathbf{A}_2 \cdots
> \mathbf{A}_T$, what graph recursion does this matrix product recall? *(Hint: if each
> $\mathbf{A}_t$ is one step "along some relation", the product counts $T$-step paths
> between two nodes — related to powers of the adjacency matrix.)*

**$\partial$ILP: Differentiable Inductive Logic Programming.** Another approach, by Evans
and Grefenstette (2018): instead of relaxing in matrix-chain form, $\partial$ILP relaxes
**logical deduction** using **fuzzy t-norms**. Concretely, it represents each Horn rule as
a fuzzy logic program with weights $\theta$, then uses gradients to learn the weights.
Benefits: (1) it keeps a symbolic rule form, compatible with the formal checkers of Chapter
5; (2) the output is readable probabilistic Horn rules; (3) it can trade off rule
complexity (number of links) against generalization power.

**Quick comparison with AMIE+:**

| Criterion | AMIE+ | Neural LP / DRUM | $\partial$ILP |
|-----------|-------|------------------|---------------|
| Rule space | discrete | relaxed (gradient) | relaxed (fuzzy) |
| Optimization | support + PCA confidence | end-to-end gradient | end-to-end gradient |
| Long chains | combinatorial explosion | matrix product + RNN | fuzzy inference |
| Output | discrete rules | $\arg\max$-weight rules | probabilistic Horn rules |
| Interpretability | yes | yes (if extracted) | yes |
| Relation to logic | close | intermediate | tight (Horn) |

> ⚠️ **Differentiable rule learning still yields hypotheses.**
> Despite the gradients, the extracted rules are still **data hypotheses**. Gradients help
> select rules that fit predictions; they do not turn them into laws. A Neural LP rule may
> be optimal for entirely wrong reasons: source duplication, false negatives, or spurious
> correlation (§8.26). Never load them directly into the inference engine without the
> checks of §8.22.3 and acceptance governance (Ch6).

## 8.23 Comparison: Symbolic vs Embeddings

The two inductive-learning families — symbolic rules and embeddings — have complementary
strengths [@nickel-relational-ml-2016]:

| Criterion | Rule learning (symbolic) | Embeddings | Differentiable |
|-----------|--------------------------|------------|----------------|
| Output | Readable rules | Vectors, scores | Probabilistic Horn rules |
| Interpretability | Yes (explicit structure) | Hard (hidden geometry) | Yes (rules + weights) |
| Generalizes to new entities | Good (rules are identity-independent) | Transductive: poor; inductive (GNN): yes | Good (rules are identity-independent) |
| Handles uncertainty | Hard (no natural uncertainty) | Natural (scores) | Natural (softmax weights) |
| Semantics | Close to logic, but still hypotheses | No formal semantics | Close to logic, but still hypotheses |
| Complex relations | Hard without paths | Flexible | Flexible (matrix chains) |
| Training | Counting + thresholds | Gradient | Gradient |

No family is absolutely "right". In practice the best answer is usually combining all
three — leading to the hybrid architecture of the next section.

## 8.24 The Hybrid Pipeline: ML Generates Candidates, Symbolic Filters, Epistemology Decides

### 8.24.1 The overall architecture

The hybrid pipeline is a **BOOK-DEFINED architecture** — an engineering arrangement
combining real standards, not a published standard. It has three layers:

```
        LAYER 1: ML candidate generation (statistical)
        KGE / GNN / rule mining → candidate triples & rules & hypotheses
                    │
                    ▼
        LAYER 2: Symbolic filter
        Type checking, ontology constraints (Ch4),
        SHACL gate (Ch5, Ch7), SPARQL queries verifying premises
                    │
                    ▼
        LAYER 3: Epistemology + governance
        Evidence (Ch6), epistemic confidence, conflict,
        Claim Ledger, accept / reject / review decisions (Ch6–7)
                    │
                    ▼
        Claim Ledger → Canonical View
```

![The hybrid pipeline: ML generates hypotheses → symbolic filtering of constraints → epistemology attaches evidence → governance decides. A book-defined architecture (BOOK-DEFINED).](figures/generated/ch08-hybrid-pipeline.pdf)

**Role of each layer:**

- **Layer 1 (ML):** generates candidates with scores. This is where new knowledge is
  *proposed*.
- **Layer 2 (Symbolic):** removes candidates that violate known semantic constraints. For
  example: if `withRespectTo` must point to a `ReferenceVariable`, a candidate pointing to
  `Time` when `Time` has not been declared a ReferenceVariable is caught by the SHACL gate
  (like source C in Chapter 7).
- **Layer 3 (Epistemic):** attaches evidence, assesses, decides. This is where a candidate
  becomes an accepted statement — or is rejected.

### 8.24.2 Entailment as a feature / filter

One important detail: entailment plays the role of **filter and feature** in the hybrid
architecture, not of a source of truth.

- As a **filter**: a candidate that contradicts accepted knowledge enters the conflict
  process (Ch6) — it is not automatically removed, but it must be reviewed.
- As a **feature**: inference results (for example: "by the accepted rule, every
  RateOfChangeApplication has withRespectTo Time") can be a useful input to the ML model.

> ⚠️ **Symbolic constraints do not prove the surviving candidates are true.**
> If a candidate passes the SHACL gate and is consistent with the ontology, that does not
> mean it is true. It only means it does not violate known constraints. "Not wrong per the
> constraints" ≠ "true". This distinction is a direct consequence of OWA (Ch4).

### 8.24.3 Entailment as a positive constraint

A subtler application: entailment can serve as a **positive constraint** in training. If an
accepted inference rule (Ch5) entails triple T, then T is a certain "false negative" if it
is ever generated as a negative sample — and it can be used as an additional positive
example, regardless of whether it appears in the graph. This is one disciplined way to
combine entailment and inductive learning.

> 🖊 **Self-check 5:** Take any mechanism hypothesis and run it through the three layers of
> the hybrid pipeline: at the ML layer why is it proposed; at the symbolic layer which
> constraint could block it; at the epistemic layer what evidence it needs before being
> recorded in the ledger. For each layer, name one thing that layer CANNOT prove.

## 8.25 Data Leakage in System Practice

§8.10 introduced the general kinds of leakage. This section goes deeper into the three
kinds especially dangerous for the mechanism system — because they are easy to miss in
evaluation and easy to make the system wrongly confident.

### 8.25.1 Temporal Leakage

Knowledge graphs have time (Ch6: valid time, assertion time). If the training set contains
"future" statements and the test set contains "past" statements, the model is not
predicting the past — it is *recalling* the future.

Countermeasure: split by time (temporal split) — train on data before time T, test on data
after T. But:

> ⚠️ **Temporal splitting is not a cure-all.**
> A model trained on 2024–2026 should not be used to "predict" 2024. And temporal splitting
> does not remove the other kinds of leakage (entity, source, duplicate). It is a measure,
> not a guarantee.

### 8.25.2 Source Leakage

The big lesson of Chapter 7: an echo source is not independent evidence. The machine
learning version: if two different books both copy from one original document, and one
book is in train while the other is in test, a high test score does not prove
generalization — it only proves the model memorized the source.

Countermeasure: split by source (source split) — an entire source goes to test, never
mixed.

> ⚠️ **Source diversity in train does not guarantee test independence.**
> If the 10 sources in train are all copies of one original document, they are not 10
> independent pieces of evidence — they are 1 piece of evidence repeated 10 times (Ch7
> §7.23). The model learns the "scent" of that original source, not semantic diversity.

### 8.25.3 Claim Duplication

The same statement (for example "velocity is the derivative of position") can appear in
many places within one source, or across many sources. If these copies fall into both
train and test, scores are inflated by near-identical records.

Chapter 7 handled this at the acquisition layer (content hash, deduplication). Chapter 8
reiterates it at the learning layer: before splitting, deduplication must be done at the
statement level.

## 8.26 Cross-Domain Generalization and Spurious Correlation

### 8.26.1 Cross-domain generalization

The RATE_OF_CHANGE mechanism appears in many domains: mechanics (velocity), electronics
(current), economics (inflation), biology (growth). One question is decisive for the
system: does a model trained on mechanics and electronics applications recognize the
mechanism in economics?

**Cross-domain generalization** is the ability to recognize a mechanism in a new domain
even though the surface vocabulary is entirely different. This is the most important test
for a mechanism-learning system: train on mechanics + electronics, test on economics.

> ⚠️ **In-domain accuracy does not prove mechanism understanding.**
> A model reaching 95% on mechanics data can fail completely on economics data — if it
> learned the surface cues of the mechanics domain (the string "m/s", the phrase
> "velocity") instead of the mechanism structure. This is exactly the problem of spurious
> correlation.

### 8.26.2 Spurious Correlation and Shortcut Learning

**Shortcut learning** occurs when a model scores well on in-distribution test data by
exploiting superficial/coincidental cues, and collapses under harder conditions
[@geirhos-shortcut-2020].

Example in the mechanism system: every RATE_OF_CHANGE application in the training data
comes from physics books, and every physics book contains the phrase "rate of change". The
model learns: phrase "rate of change" → RATE_OF_CHANGE. When it meets an economics text
saying "inflation is the rate of price increase" — without the magic phrase — the model
misses it, or worse: mislabels a physics text just because the phrase appears in a
different context.

A **spurious correlation** is a learned relationship between a surface cue and a label
that appears in the training data but is not mechanism structure.

> ⚠️ **A high score does not prove the model learned what we meant.**
> This is the classic trap: a model reaches 95% accuracy but learned a shortcut. A high
> score only proves the model fits the data in some way — not that it fits in *the way
> humans define as correct*.

## 8.27 Counterfactual Tests and Hard Negatives

### 8.27.1 Counterfactual Tests

How do we detect shortcut learning? One powerful tool: **counterfactual tests** — change
one structural component and check whether the model responds correctly.

For application A (velocity):

- **Change WithRespectTo from Time to Distance:** "derivative of position with respect to
  distance" — if the model still labels it RATE_OF_CHANGE (over time), it is ignoring this
  critical component. Expected result: not a RateOfChangeApplication.
- **Change Operation from Derivative to Average:** "average rate of change" — if the model
  still labels it the same, it does not distinguish derivative from average. Expected
  result: a different response.

A counterfactual test turns the hypothesis "the model learned structure" into a testable
prediction: if the model truly learned structure, changing structure must change the
prediction.

> ⚠️ **Passing one counterfactual test does not prove the model is right.**
> It only rules out one specific class of shortcut. The model may still be learning another
> shortcut. This is the nature of hypotheses: tests increase confidence, they never fully
> prove.

### 8.27.2 Hard Negatives

When training to distinguish RATE_OF_CHANGE from other mechanisms, the quality of the
negatives determines the quality of the boundary:

- **Easy negative:** `ColorClassification` — far away, teaches nothing about the boundary.
- **Hard negative:** `FiniteDifferenceApplication` — a discrete derivative, close to
  RATE_OF_CHANGE, forcing the model to distinguish "instantaneous" from
  "average/interval".

A model only gets a good boundary if it is trained with hard negatives. Trained only on
easy negatives, the model will mislabel every application near the boundary.

> ⚠️ **Hard negative ≠ logical counterexample.**
> A hard negative is a training sample lying near a class boundary. A counterexample
> (this chapter, §8.42) is an observation that refutes an accepted hypothesis. They differ
> in role and consequence: hard negatives shape the learned boundary; counterexamples
> shape governed knowledge.

## 8.28 Mechanism Family vs One and the Same Mechanism; Clustering

### 8.28.1 One mechanism or a family of mechanisms?

The question "do velocity, current, and growth share one mechanism?" can have multiple
correct answers at different levels of abstraction:

- **One mechanism** (one class): if we define the mechanism at the level of "derivative of
  a quantity with respect to time" — all three are RATE_OF_CHANGE.
- **A mechanism family** (one parent class, several child classes): if we distinguish
  "instantaneous derivative" (velocity) from "discrete rate of change" (population growth)
  — this is a family of several sub-mechanisms.

This decision is **not a pure statistical finding** — it depends on the system's
knowledge goals and is settled by governance (§8.40). Inductive learning generates
candidate levels of abstraction; governance chooses which level has value.

### 8.28.2 Clustering — exploration, not assertion

**Clustering** groups applications based on representation/features without labels. In the
mechanism system, clustering is an **exploratory** tool: it proposes "these applications
look like one group".

> ⚠️ **A cluster is not an ontology class.**
> A cluster discovered by an algorithm is not a class in the ontology. Turning a cluster
> directly into a class (RATE_OF_CHANGE ⊑ ...) without semantic assessment and governance
> is a serious violation of the book's architecture. A cluster is only hinting evidence
> for a mechanism hypothesis (§8.19).

## 8.29 Classification and Calibration

### 8.29.1 Classification — candidate output

**Classification** is the supervised problem: a model trained on labeled applications
(RateOfChangeApplication vs FiniteDifferenceApplication vs ...) assigns labels to new
applications. The output is a probability distribution over classes — for example:

```
Application X:  RateOfChange 0.82 | FiniteDifference 0.15 | Other 0.03
```

This output is a **candidate hypothesis**, not a type assertion.

> ⚠️ **Predicted labels are never written straight into the graph.**
> Writing `X rdf:type RateOfChangeApplication` into the graph because the model said 0.82
> bypasses the entire architecture: it must pass through CandidateClaim (Ch7) → evidence
> (Ch6) → governance.

### 8.29.2 Calibration

Are the output probabilities of a deep model trustworthy? **Calibration** measures how well
predicted probabilities match actual correctness frequencies [@guo-calibration-2017]:

- A **well-calibrated** model: among predictions labeled "0.8", about 80% are correct.
- An **overconfident** model: among "0.8" predictions, only 60% are correct.

Guo and coauthors' research shows modern neural networks are typically overconfident —
especially on hard data. A common remedy: **temperature scaling** — adjusting the
"flatness" of the probability distribution without changing the prediction order.

> ⚠️ **Softmax ≠ probability of truth.**
> A model's softmax value is an uncalibrated statistical estimate. It is not the
> probability that "this triple is true" in the epistemic sense (Ch6). To use a number as
> evidence, the system needs a ModelAssessment (§8.30) declaring what that number means.

## 8.30 ModelAssessment and Model Provenance

### 8.30.1 The problem: an anonymous number

A score "0.82" appearing in a statement without context is an anonymous number —
unverifiable, incomparable, unreviewable. Which model produced it? On what data? With
which feature schema? At what time? Under which scoring convention (logit, ranking,
softmax, calibrated)?

### 8.30.2 ModelAssessment

**ModelAssessment** is a book-defined concept (BOOK-DEFINED) — an object that "wraps" every
model score, recording:

- **Target:** the triple / application being scored
- **Model:** model identity + version
- **Task:** the problem (link prediction, classification, ...)
- **Score:** the score value
- **Score semantics:** the meaning of the score (logit / ranking / softmax / calibrated)
- **Assessed at:** the time of assessment
- **Training dataset:** the training data version
- **Evaluation context:** the evaluation context (train / validation / test, which domain)

### 8.30.3 Training provenance

Every learned hypothesis is **generated by a training activity** — per the PROV model
(Ch6): a `TrainingOrInferenceActivity` with `wasGeneratedBy` recording the training data,
model version, feature schema, configuration. A model is not a magic black box: every
prediction has provenance [@prov-o].

> ⚠️ **Training provenance is not evidence.**
> "The model was trained on examples supporting P" is information about the *origin of the
> prediction*, not evidence that P is true. A prediction being based on data does not make
> that data evidence for the prediction's content. This distinction parallels the
> lineage-vs-evidence distinction of Chapter 7.

## 8.31 Is Training Data Evidence?

### 8.31.1 Provenance ≠ Evidence

This is one of the most important epistemic boundaries of the chapter. A statement accepted
in the ledger (Ch6) needs evidence: sources, reliability, conflict assessment, time. A
model prediction has provenance — but no evidence in the Ch6 sense.

Why? Because training data may contain:

- Errors from the extraction stage (Ch7)
- Unresolved conflicting statements
- Spurious correlations (§8.26)
- The model's own statements recycled (feedback loop, §8.33)

A model "learning from data" does not mean it learned the truth — it learned the truth
*under the data distribution*, and that distribution may be biased.

### 8.31.2 Echo Sources and Duplication in Training Data

The echo-source lesson of Chapter 7 (§7.23) applies directly: if a statement is copied 100
times across 100 websites (echo sources), the model treats it as a very strong sample —
even though it is only one original piece of evidence. Training data must be echo-filtered
before being used as a training signal, or the model "learns" repetition, not consensus.

> ⚠️ **"Trained on N examples" does not mean "N independent pieces of evidence".**
> If 90 of 100 examples are copies of the same original source, the model effectively
> learned from ~10 independent pieces of evidence, repeated 10 times. Example count is not
> evidence count.

> 🖊 **Self-check 6:** A model predicts "velocity is the rate of change of position" with
> score 0.9. Before the system reviews this statement, which of the following are missing
> and must be added: (a) the semantics of the number 0.9; (b) the model version and
> training data; (c) the assessment time; (d) independent source evidence for the statement
> itself; (e) conflict-check results against the ledger. Explain the role of each item —
> and which of them are evidence in the Ch6 sense versus mere provenance.

## 8.32 Uncertainty Sources, and Model Error vs Knowledge Conflict

### 8.32.1 Many uncertainty sources, not just one

The uncertainty of a mechanism hypothesis comes from many different sources, and they
**cannot be merged into a single number**:

| Uncertainty source | Question | Appears in |
|--------------------|----------|------------|
| Extraction | Is the record faithful to the source? | Ch7 |
| Identity | Are two records one entity? | Ch3, Ch7 |
| Schema | Is the mapping semantically right? | Ch7 |
| Model | How reliable is the model's prediction? | Ch8 |
| Evidence | Do the sources support it? | Ch6 |
| Time | Is the statement still in force? | Ch6 |

Collapsing all of these into one "confidence" number is a serious information loss: two
hypotheses with the same collapsed confidence may be uncertain for entirely different
reasons — one uncertain because the model is weak, the other uncertain because sources are
missing. The handling differs.

### 8.32.2 Model error or knowledge conflict?

A hard situation: the model predicts P, but the ledger holds an accepted `not P`. How to
handle it?

- **Wrong:** overwrite governed knowledge with the model's score ("the model said 0.9 so it
  is right").
- **Right:** create a new CandidateClaim, enter the conflict process (Ch6 §6.18), with the
  possibilities: (a) the model is wrong; (b) the existing knowledge is wrong; (c) both are
  right but in different contexts (multi-label, different scope); (d) different ontology
  versions.

> ⚠️ **Scores never beat governance.**
> No model score — not even 0.999 — by itself overwrites an accepted statement. The
> precedence order is always: the epistemic and governance process decides; the model only
> proposes candidates.

## 8.33 Active Learning, Human Feedback, and the Learning Loop

### 8.33.1 Active Learning

Labeling every new application is expensive. **Active learning** selects the samples
*most worth labeling* — typically the samples with the highest uncertainty, such as
applications sitting right at the RATE_OF_CHANGE / FiniteDifference boundary — and asks
humans to label those samples. Each label obtained carries the highest information value.

### 8.33.2 Human Feedback Is Data

Human feedback (accept / reject / correct a label) becomes data for subsequent training
rounds. This creates an iterative learning loop:

```
Model predicts → Humans assess → Assessment outcomes (with provenance)
→ Data for the next training round → New model → ...
```

This loop is powerful — but has a trap: **circularity**. If humans merely "rubber-stamp"
the model's predictions without actually reviewing them, the new data is only an echo of
the old model.

> ⚠️ **A rubber stamp is not independent evidence.**
> A statement accepted by a human because the model proposed it — without source/evidence
> checking — is not an independent confirmation. The loop "model proposes → human
> rubber-stamps → retrain" increases confidence without increasing evidence.

## 8.34 Self-Reinforcing Feedback and Model Collapse

### 8.34.1 Self-reinforcing feedback

When a model's predictions return as training data, a feedback loop forms. This loop is
**self-reinforcing**: the model learns its own patterns, those patterns are used to train
the next model, and small biases are gradually amplified.

The book's principle: clearly separate **knowledge generated by humans/sources** from
**model-generated candidate knowledge**. The latter must be flagged with "model-generated"
provenance and never mixed into training data without controls.

### 8.34.2 Model Collapse

Shumailov and coauthors demonstrated a serious phenomenon: when models are trained on
data generated by models themselves (recursively generated data), **model collapse**
occurs — the "tails" of the original distribution disappear, the diversity of knowledge
decays, and defects accumulate irreversibly [@shumailov-collapse-2024].

> ⚠️ **Retraining on predictions does not confirm predictions.**
> "The old model predicted X, the new model trained on that prediction also says X — so X
> must be true" is a fallacy. This is not two sources confirming; it is one source seeing
> itself twice. This applies to LLMs and graph models alike.

## 8.35 Explanation and Path-Based Explanation

### 8.35.1 Why explanation is needed

A mechanism hypothesis proposed by a model will be reviewed by humans in the governance
process (Ch6–7). For humans to decide, the hypothesis must be **explainable** — it must
answer "why did the model propose this?"

### 8.35.2 Path-based explanation

With rule learning (AMIE+), the natural explanation is a **path in the graph**: the rule
`hasOperation(x, Derivative) ∧ withRespectTo(x, Time) → resultIsRateOfChange(x)` comes with
the concrete path in the application's subgraph:

```
Application_A —operation→ DerivativeOperation
Application_A —withRespectTo→ Time
Application_A —result→ Velocity
∴ (by the learned rule) Velocity is a rate of change
```

With KGE/GNN, explanation is harder: vectors have no explicit meaning. One pragmatic
approach: **explain at the structural level** — point to the structural elements that
contributed most to the score (neighbors, relations, features), instead of explaining
individual vector dimensions.

> ⚠️ **Explanation is not evidence.**
> An explanation ("the model proposed it because the structure is identical to application
> A") clarifies *why the model* made the prediction — it does not prove the *prediction is
> correct*. Explanation is about the model's mechanism; evidence is about the statement's
> truth (Ch6).

## 8.36 Evaluation Objectives, Benchmarks, and a Model-Comparison Framework

### 8.36.1 Evaluation objectives for mechanism discovery

Evaluating a mechanism-learning system needs specific objectives, not generic accuracy:

- **Mechanism precision:** the fraction of mechanism hypotheses accepted by governance that
  are correct (against grounded human assessment)
- **Coverage:** the fraction of mechanisms that truly exist which the system proposes
- **No false invention:** the fraction of proposed hypotheses that are wrong (false
  discovery)
- **Stability:** the same structure in different domains yields the same proposal
- **Shortcut resistance:** counterfactual test results (§8.27)

### 8.36.2 Benchmarks and model comparison

Comparing models is meaningful only under the same benchmark with the same split rules,
the same datasets, and the same evaluation conventions. MRR on FB15k-237 is not comparable
to MRR on a small mechanism graph. Every comparison number must come with: data, splits,
filtered-or-raw convention, and score semantics.

> ⚠️ **Pretty metrics ≠ a good system.**
> A model reaching MRR 0.9 on a standard benchmark can still be completely useless for the
> mechanism system if it does not generalize across domains or distinguish nearby
> mechanisms. Benchmarks measure scores on data; the system needs capability on the task.

## 8.37 When NOT to Use Graph ML — and Capability-Based Decisions

### 8.37.1 When machine learning is not needed

Inductive learning is expensive: data, training, evaluation, prediction governance. It
should only be used when knowledge *beyond* what the sources say must be generated.
Situations to NOT use it:

| Situation | Why not ML |
|-----------|------------|
| Known rules, writable by hand (Ch5) | Exact deduction, already governed, no learning needed |
| Too little / unrepresentative data | ML cannot generate regularities from nothing |
| Error consequences unacceptable | ML guarantees no truth (§8.47) |
| Full semantic explanation required | Embeddings carry no semantics |
| Data with strong, unfiltered spurious correlations | The model will learn shortcuts |

### 8.37.2 Capability-based decision

The system's decision principle: **propose knowledge via machine learning only when the
system's capability is sufficient for the risk level of the decision.** The system must
know what it knows (Ch6), what it has learned (Ch8), and what it does not guarantee
(§8.47). The decision "use ML or not" is a recorded architectural decision with reasons —
not a default assumption that "ML is better".

## 8.38 Pattern ≠ Mechanism; Operation and Meaning; Structure and Text

### 8.38.1 From pattern to mechanism

A recurring pattern in the graph — three applications with the same structure — may arise
by chance, by the convention of one source, or by a real mechanism. Frequency itself
cannot distinguish these cases. A mechanism, per the book's definition (Ch1/Ch4), is a
structure with **stable explanatory/operational meaning** — a recurring pattern does not
carry that meaning by itself.

The system must keep the boundary: **pattern detection → mechanism hypothesis → assessment
→ decision**. No step may be skipped.

### 8.38.2 Operation and meaning

Inductive learning can learn the *operation shape* — "there is a Derivative operation
linking Quantity to Result" — but does not automatically learn the *meaning* —
"instantaneous" vs "average", "with respect to time" vs "with respect to distance".
Meaning requires:

- The source's textual definition (acquired in Ch7)
- Ontology semantics (Ch4)
- Evidence and human assessment (Ch6)
- Cross-source consensus (Ch7)

> ⚠️ **Topology does not yield semantics.**
> Two applications with identical structure can still differ in meaning (finite difference
> vs instantaneous derivative). Conversely, two applications with different structures can
> share one meaning (notational variants). Graph geometry is evidence, not semantics.

### 8.38.3 Structure + text

The best evidence combines both: graph structure suggests role similarity; source text
distinguishes meaning ("instantaneous" vs "average"). A system that ignores text loses
fine discrimination; a system that relies entirely on text is fooled by verbal similarity
(two different concepts both using the phrase "rate of change").

> ⚠️ **The same words are not the same structure.**
> "Rate of change" appearing in source A (derivative) and source C (current) does not prove
> they share one mechanism — this is exactly the lesson of Chapter 7 §7.0. Text embeddings
> catch word similarity; graph structure catches role similarity; identity comes only from
> epistemic assessment.

## 8.39 Hypothesis Types and Acceptance Policy

### 8.39.1 Types of candidate hypotheses

An inductive learning system generates different kinds of hypotheses, each with a
different risk level:

| Hypothesis type | Example | Risk if wrong |
|-----------------|---------|---------------|
| Candidate link | `(Velocity, rateOfChangeOf, Position)` | Low — local, easy to check |
| Classification label | `X rdf:type RateOfChangeApplication` | Medium — affects inference through types |
| Mechanism hypothesis | "A, B, C are one abstract mechanism" | Medium — requires a conceptual change |
| Learned rule | `r1 ∧ r2 → r3` | High — if it enters the inference engine, it spreads across the graph |
| Ontology axiom | `RateOfChange ⊑ ChangeMechanism` | Very high — changes the entire classification |

### 8.39.2 Acceptance policy and risk level

The system's acceptance policy is stratified by risk level (high-risk / low-risk):

- **Low risk** (local links, easily reversible consequences): may be accepted with lighter
  evidence — but still requires assessment and ledger recording.
- **High risk** (axioms, inference rules, ontology changes): requires evidence from
  multiple independent sources, counterexample checks, a blast-radius assessment (§8.41),
  and a human decision.

> ⚠️ **High risk is not forbidden — it is more tightly controlled.**
> The system does not refuse high-risk hypotheses; it requires them to pass stricter
> gates. Refusing them all means missing knowledge; accepting them casually means corrupting
> the graph.

## 8.40 The Full Worked Example: 15 Steps

We combine every component in one end-to-end example — from graph to governed hypothesis.
Context: the system has integrated (Ch7) three applications: Velocity (mechanics), Current
(electronics), Population growth (economics).

1. **Identify subgraphs.** For each application, extract the subgraph around the
   application node: the Quantity, Operation, WithRespectTo, Result nodes and their edges.
2. **Choose the representation.** Decide the feature schema: Operation, WithRespectTo,
   Result, Quantity type — representation determines learnability (§8.21).
3. **Train the model (validation).** Split by source (no leakage, §8.25), train GNN +
   pooling on the mechanics/electronics applications.
4. **Cross-domain evaluation.** Test on the economics application — passing is an
   important signal (§8.26).
5. **Counterfactual tests.** Replace WithRespectTo with Distance; check that the
   prediction changes (§8.27).
6. **Compute subgraph representations.** GNN + pooling for the three applications; measure
   structural similarity (multi-dimensional, not just cosine).
7. **Exploratory clustering.** The three applications fall into one cluster — hinting
   evidence, not assertion (§8.28).
8. **Generate the hypothesis.** Create a CandidateMechanismHypothesis: "the three
   applications may be one abstract mechanism" with full evidence, uncertainty, competing
   hypotheses, provenance (§8.19).
9. **Symbolic filtering.** Type/ontology checks: `WithRespectTo=Time` must point to a
   ReferenceVariable; all checks pass (§8.24).
10. **Compare competing hypotheses.** "One mechanism" vs "a mechanism family with
    instantaneous/discrete children" — textual evidence distinguishes them (§8.38).
11. **Epistemic assessment.** Attach source evidence (multiple independent sources),
    assess epistemic confidence (Ch6), check conflicts with the ledger.
12. **Counterexample check.** Search for observations that refute the hypothesis at the
    chosen abstraction level (§8.42).
13. **Governance decision.** Accept the hypothesis at the "mechanism family" level with
    separately governed children; record in the Claim Ledger with model provenance and
    decision reasons.
14. **Propose ontology evolution.** Propose splitting into
    `InstantaneousRateOfChange` / `AverageRateOfChange` children — as a CandidateAxiom
    awaiting assessment (§8.41).
15. **Record everything.** Every step, every score, every decision — with provenance — in
    the audit trail.

Result: the system does not "know" the three applications are one mechanism — it holds a
hypothesis that is assessed, governed, and revisable when new data arrives.

## 8.41 Candidate Axioms and Blast Radius

### 8.41.1 What is a learned axiom?

A model can propose structures at the ontology level: "every RateOfChangeApplication is a
ChangeMechanism" — a **CandidateAxiom**.

An axiom differs from a local statement: it is a **global** rule. If accepted, it applies
to every entity in the graph — present and future.

### 8.41.2 Blast radius

The **blast radius** of a candidate axiom is the set of conclusions affected if that axiom
is wrong. For `RateOfChange ⊑ ChangeMechanism`: every inference `X rdf:type ChangeMechanism`
derived from this axiom is wrong if the axiom is wrong.

Assessing the blast radius is mandatory before accepting a candidate axiom: SPARQL queries
compute the affected conclusion set, consistency checks (Ch5) run, and a decision is made
on whether the impact is acceptable given the available evidence.

> ⚠️ **Learned axioms never enter the ontology automatically.**
> Inserting a candidate axiom into the ontology without semantic assessment, consistency
> checks, evidence assessment, blast-radius measurement, and a governance decision — is a
> serious violation. One wrong axiom corrupts every inference built on it (Ch5).

## 8.42 Boundaries, Counterexamples, and Ontology Evolution

### 8.42.1 The boundaries of a mechanism

Every mechanism hypothesis has boundaries: cases inside, cases outside. The RATE_OF_CHANGE
hypothesis at full abstraction must settle: does `AverageRateOfChange` belong? Does
`FiniteDifference` belong? Does a `Derivative with respect to distance` belong?

These boundaries are part of the hypothesis and must be tested.

### 8.42.2 Counterexamples and refinement

When a new observation (or an old observation re-examined) refutes an accepted hypothesis,
the system must respond with discipline:

1. **Record the counterexample** with full provenance
2. **Assess the scope:** does the counterexample refute the whole hypothesis, or only a
   part (one child, one context)?
3. **Refine the hypothesis:** narrow the boundary, split a child, or drop the hypothesis
4. **Update the ledger:** the old hypothesis is marked superseded (Ch6), the new one is
   recorded with the refinement rationale
5. **Learn from the counterexample:** the counterexample becomes a hard negative for the
   next training round (§8.27)

Counterexamples are not failure — they are the most important channel through which the
system learns with discipline. A system that never meets a counterexample is usually a
system that is never tested.

![Counterexample-based refinement: the counterexample is recorded with provenance → the scope of refutation is assessed → the hypothesis boundary is refined/narrowed → the ledger is updated (superseded) → the counterexample becomes a hard negative for the next learning round.](figures/generated/ch08-counterexample-refinement.pdf)

> ⚠️ **"No counterexample seen yet" is not "no counterexample exists".**
> This is a consequence of OWA: absence of refuting evidence is not evidence of absence of
> refutation. A hypothesis supported by 100 confirming examples can still fall to the 101st
> counterexample.

> 🖊 **Self-check 7:** The hypothesis "every RateOfChangeApplication has withRespectTo
> Time" has been accepted. You receive a new observation: an application "rate of change
> of heat with respect to mass" — withRespectTo = Mass. Draw the refinement process (the 5
> steps above) for this situation: does the counterexample refute the whole hypothesis or
> only a part? What would the refined hypothesis look like? And which step in the process
> ensures this correction does not damage conclusions already in the ledger?

### 8.42.3 Disciplined ontology evolution

Repeated counterexamples in one boundary region are a signal: the ontology is too coarse.
For example, if the system keeps confusing AverageRateOfChange with
InstantaneousRateOfChange, that is evidence that two separate children are needed.
Ontology evolution is a governance decision, not an automatic discovery — and it paves the
way for the living knowledge system (Ch10).

## 8.43 The Scientific-Method Analogy

There is a deep correspondence between the system's inductive learning process and the
scientific method:

| Scientific method | Inductive learning system |
|-------------------|---------------------------|
| Observe phenomena | Acquisition and integration (Ch7) |
| Form a hypothesis | Generate CandidateMechanismHypothesis (§8.19) |
| Testable predictions | Counterfactual tests, cross-domain tests (§8.26–27) |
| Experiment | Evaluation on held-out data (§8.10) |
| Counterexample | Hypothesis refinement (§8.42) |
| Peer-reviewed publication | Governance + provenance-recorded ledger entry (Ch6) |
| Replication | Re-running the pipeline with the same data + versions (Ch7) |

This analogy is not decoration: it reminds the system that inductive knowledge always
expects to be refutable — and that is a feature, not a bug.

## 8.44 A Failure Case: When Inductive Learning Goes Wrong

To understand the boundary fully, consider a typical failure case — a system doing
everything wrong.

**Context:** The system has no epistemic layer. The developer dumps the entire acquired
graph (Ch7) into one dataset, splits train/test randomly, trains an embedding model, and
achieves an impressive MRR.

**The chain of errors:**

1. **Random split** → entity leakage: applications of the same mechanism appear in both
   train and test (§8.10).
2. **No echo filtering** → duplicated sources repeat the same statement on both sides
   (§8.25).
3. **No counterfactual checks** → the model learns the lexical shortcut "rate of change"
   (§8.26).
4. **Predicted labels written straight into the graph** → CandidateClaim and governance
   bypassed (§8.29).
5. **PCA confidence of mined rules used as epistemic confidence** → terminology collision
   (§8.22).
6. **Retraining on its own predictions** → self-reinforcing feedback, model collapse
   (§8.34).
7. **Learned axioms inserted into the ontology** → blast radius never assessed, graph-wide
   inference contaminated (§8.41).

**Result:** the system is comprehensively, confidently wrong — high benchmark scores,
mechanism understanding equal to zero. The lesson: each step of the hybrid architecture
(§8.24) exists to block one specific kind of error; skip a step, and that error returns.

## 8.45 An Explanation Case: Why Was This Hypothesis Proposed?

A mechanism hypothesis proposed for human review must carry a clear explanation. For
example:

> **Hypothesis H-104 (CandidateMechanismHypothesis):** "Velocity, electric current, and
> population growth may be applications of the same abstract mechanism."
>
> **Why the model proposed it:** all three subgraphs share the same role pattern — one
> Quantity, one Operation=Derivative, one WithRespectTo=Time, one Result. Average
> structural similarity 0.91 across pairs (higher than any other mechanism pair in the
> graph).
>
> **Checks performed:** cross-domain test (train mechanics+electronics, test economics)
> passed; two counterfactual tests (change WithRespectTo, change Operation) gave the
> correct responses.
>
> **Source evidence:** three independent sources (A, B, C) — not echoing each other (Ch7).
>
> **Competing hypothesis:** H-105: the three applications belong to a mechanism *family*,
> distinguishing instantaneous vs discrete. Textual evidence currently undecided between
> H-104 and H-105.
>
> **Uncertainty:** model 0.82 (calibrated); source evidence moderate; no conflict detected.
>
> **Provenance:** model GNN v1.2, data KG-2026.08 (source-split), timestamp 2026-08-30.

This explanation gives humans everything needed to decide — and shows the hypothesis is
still a candidate, not yet knowledge.

## 8.46 What Machine Learning Does Not Guarantee

To close the content section, an explicit list — the final boundary of inductive learning
in a knowledge system:

**Machine learning does not guarantee:**

- **Truth:** high score ≠ correct. (Oversmoothing, shortcuts, and noise can all deceive.)
- **Causal mechanism:** models learn correlations, not causation. Recurring structure is
  not a causal relation.
- **Ontology correctness:** the model does not know whether your ontology is right.
- **Identity:** geometric similarity is not identity (Ch3).
- **Universality:** a regularity learned in one domain is not guaranteed in another.
- **Evidence independence:** learning on data does not create independent evidence.
- **Unbiasedness:** training data carries the biases of its sources (Ch7).
- **Cross-domain generalization:** proven only by cross-domain testing, never by default.

These "non-guarantees" are not weaknesses to fix — they are the nature of induction:
inductive knowledge is knowledge that can be wrong, and a disciplined system is one that
operates according to exactly that nature: propose, assess, govern, and stay ready to
correct.

## 8.47 Source-First Discipline and Current Research

### 8.47.1 Source-first

Every learned hypothesis originates from data — and data comes from sources (Ch7). The
book's source-first discipline applies in full: a model prediction is only trustworthy
when the sources beneath it are registered, verified, and traceable (source_index.json,
research notes). No verified sources, no trustworthy training data.

### 8.47.2 Current research

Inductive learning on graphs is a fast-moving field. New results — better inductive GNNs,
new benchmarks, deeper understanding of shortcuts — appear continuously. The book keeps
its discipline: this chapter teaches stable principles (OWA, the prediction/entailment
boundary, evaluation, provenance) grounded in registered sources; new developments must be
source-registered before being incorporated (the source → contract → manuscript → test
rule of CLAUDE.md).

## 8.48 Failure Modes and Summary Tables

### 8.48.1 Failure modes of inductive learning

| # | Failure mode | Detection signal | Recovery |
|---|--------------|------------------|----------|
| 1 | Entity leakage | Test accuracy spikes vs source-separated runs | Source/entity split |
| 2 | Temporal leakage | Model "predicts" the past too well | Temporal split |
| 3 | Echo in data | Same statement repeated across sources (Ch7) | Echo-filter before training |
| 4 | Shortcut learning | Cross-domain test collapses | Counterfactual tests, hard negatives |
| 5 | Pervasive false negatives | Model scores rare true triples low | Smarter replacement entities |
| 6 | Oversmoothing | Adding layers lowers accuracy | Fewer layers, add residuals |
| 7 | Relation-blindness | Merging relations destroys roles | R-GCN relation-specific transforms |
| 8 | Overconfidence | Calibration measures large gaps | Temperature scaling |
| 9 | Feedback loop | New data increasingly resembles old predictions | Separate model-generated data, control it |
| 10 | Model collapse | Knowledge diversity decays | Block uncontrolled regenerated data |
| 11 | Terminology collision | "Confidence" used in two senses | Full terms, ModelAssessment |
| 12 | Knowledge overwrite | High-score model denies an Accepted claim | Ch6 conflict process |
| 13 | Automatic axiom insertion | Graph-wide inference changes unexpectedly | Blast radius + governance |

### 8.48.2 The central-distinctions summary table

| Distinction | Must not be confused with |
|-------------|---------------------------|
| Prediction | Entailment |
| Score | Probability of truth |
| Similarity | Identity |
| Pattern | Mechanism |
| Embedding | Entity |
| Cluster | Ontology class |
| Rule-mining confidence | Epistemic confidence |
| Training provenance | Evidence |
| Model explanation | Statement evidence |
| Training data | Truth |

## 8.49 Deferred Experiment Backlog

Empirical inductive learning on mechanism graphs — training models, measuring MRR,
comparing architectures — requires a built and governed dataset. Within the current scope
of the book, these experiments are recorded in the backlog and **deferred to BOOK v0.1**:

- **EXP-8-1:** Compare TransE / DistMult / ComplEx on the mechanism graph (MRR, Hits@10,
  filtered)
- **EXP-8-2:** Effect of the false-negative rate on prediction quality
- **EXP-8-3:** Cross-domain test: train mechanics + electronics → test economics
- **EXP-8-4:** Counterfactual tests for the Derivative / FiniteDifference distinction
- **EXP-8-5:** Inductive GNN with brand-new OOV entities (GrowthRate never seen before)
- **EXP-8-6:** Rule mining (AMIE+) vs embeddings for mechanism discovery
- **EXP-8-7:** Calibration of a mechanism classifier (ECE, temperature scaling)
- **EXP-8-8:** Effect of echo sources on benchmark scores

Each experiment, when run, must come with: data (with provenance), model + version, split
rules, evaluation conventions, and comparable results recorded in the experiment notebook.

## 8.50 End-of-Chapter Competence Ladder

Check your competence after finishing the chapter:

| Rung | Competence | Self-check |
|------|------------|------------|
| 1 | Distinguish deduction / induction / abduction / prediction | Given a sentence, name the category |
| 2 | Explain OWA and its consequences for machine learning | "Why is a negative sample not a false triple?" |
| 3 | Read and compare TransE / DistMult / ComplEx | Choose a model for antisymmetric relations |
| 4 | Explain transductive vs inductive, OOV | "Why can't a standard KGE handle new entities?" |
| 5 | Explain message passing, R-GCN, oversmoothing | Draw the message-passing diagram for one node |
| 6 | Explain node vs subgraph representation | "Why is a node vector not an application vector?" |
| 7 | Generate a mechanism hypothesis with discipline | Describe the 7-step pipeline of §8.19 |
| 8 | Distinguish rule-mining confidence from Ch6 confidence | Given two numbers, state each one's semantics |
| 9 | Design a leakage-free evaluation | Choose the split for a graph with echo + time |
| 10 | Explain shortcut learning and counterfactual tests | Design one test for a specific model |
| 11 | Explain feedback loops and model collapse | "Why doesn't retraining on predictions confirm them?" |
| 12 | Operate the hybrid pipeline | Draw the ML → filter → epistemology → governance pipeline |
| 13 | Decide "do not use ML" | Given a situation, decide and justify |
| 14 | Present the limits of machine learning | List the 8 things ML does not guarantee |

## 8.51 Bridge to Chapter 9

Chapter 8 built the capability to *generate candidate knowledge* from the graph. This
opens a bigger question: when the system holds much knowledge — symbolic and statistical,
accepted and candidate — how do users **ask and retrieve** that knowledge effectively? How
do you answer a natural-language question by combining SPARQL queries, inference, and
learned models — for example, "do inflation and velocity share a mechanism, and what is
the evidence?"

That is the content of **Chapter 9 — Querying, Question Answering, and GraphRAG** (not
yet built in this book): where the capabilities of the previous eight chapters converge
into a question-answering interface. But before moving to that chapter, pause and check:
has this chapter drawn the boundary correctly — the system *proposes*, *assesses*,
*governs* — and never *asserts* something it has only *learned*.

![The full eight-chapter architecture: from basic graphs (Ch1–2) through identity (Ch3), semantics (Ch4), deduction (Ch5), epistemology (Ch6), acquisition (Ch7), to inductive learning (Ch8). Each rung adds a new capability; Ch8 is the current rung.](figures/generated/ch08-full-stack.pdf)

The central distinction chain, one last time: similarity ≠ identity; prediction ≠
entailment; high score ≠ truth; learned pattern ≠ accepted knowledge.

## Terms encountered in this chapter

| Term | Short meaning | More in |
|------|---------------|---------|
| Deduction | Necessary consequence from rules + premises | §8.1.1 |
| Induction | Generalizing patterns from observations; can be wrong | §8.1.2 |
| Abduction | Selecting the best explanation | §8.1.3 |
| Prediction | A model's score for a possible structure | §8.1.4 |
| Symbolic vs Statistical knowledge | Explicit vs learned from data | §8.2 |
| Feature representation | Hand-engineered features | §8.4 |
| Representation learning | Learning vectors from data | §8.4 |
| Embedding | A learned vector; not the entity | §8.4 |
| Knowledge Graph Embedding (KGE) | ε, ρ + scoring function f(h,r,t) | §8.5 |
| Scoring function | Numericalizes how plausible a triple is | §8.5 |
| TransE | h + r ≈ t; relations are translations | §8.5.2 |
| Bilinear model (DistMult) | ⟨h, r, t⟩; symmetric | §8.6.1 |
| ComplEx | Complex embeddings, Hermitian product; antisymmetric | §8.6.2 |
| Inductive bias | Structural assumptions of a model family | §8.6.3 |
| RotatE | Relation = complex rotation $\|r_i\|=1$; 4 relation patterns | §8.6.4 |
| Hyperbolic geometry | Negative curvature; exponential volume growth, fits trees | §8.6.5 |
| Poincaré embedding | Embedding in $\mathbb{B}^d$; roots at center, leaves near boundary | §8.6.5 |
| Negative sampling | Creating negatives by random replacement | §8.7 |
| False negative | A true triple used as a negative sample | §8.7.3 |
| Link prediction | Ranking missing candidate triples | §8.8 |
| MRR / Hits@K | Measure where the correct answer lands | §8.9 |
| Filtered evaluation | Remove known true triples from the ranking | §8.9.3 |
| Data leakage | Test information reaching train | §8.10, §8.25 |
| Temporal / Source leakage | Leakage along time / along sources | §8.25 |
| Transductive learning | Predict among known entities | §8.11 |
| Inductive KG learning | Generalize to new entities | §8.11 |
| OOV entity | Entity with no learned vector | §8.12 |
| Message passing | message → aggregate → update | §8.14 |
| GNN | Neural network computing over graph structure | §8.13 |
| R-GCN | Relation-type-specific transformations | §8.15 |
| Oversmoothing | Representations converge when stacking layers | §8.16 |
| 1-WL test (Weisfeiler-Lehman) | Color refinement; expressivity ceiling of standard MPNNs | §8.14.3, §8.17.3 |
| Subgraph representation | Pooling/readout for the whole subgraph | §8.17 |
| Structural similarity | Multi-dimensional evidence; similarity ≠ identity | §8.18 |
| Cosine similarity | cos(a,b) = (a·b)/(‖a‖·‖b‖) | §8.18.2 |
| CandidateMechanismHypothesis | Candidate mechanism hypothesis (BOOK-DEFINED) | §8.19 |
| Invariant / incidental structure | Kept / dropped when abstracting | §8.21 |
| Rule induction (AMIE+) | Path rules r1∧r2→r3 | §8.22 |
| Rule-mining confidence (PCA) | Frequency under the PCA assumption; ≠ Ch6 | §8.22.2 |
| Differentiable logic programming | Neural LP/DRUM/$\partial$ILP; gradients learn Horn rules | §8.22.4 |
| Hybrid pipeline | ML generates candidates → filter → epistemology (BOOK-DEFINED) | §8.24 |
| Cross-domain generalization | Recognize mechanisms in new domains | §8.26 |
| Spurious correlation / shortcut | Learning surface cues instead of mechanisms | §8.26 |
| Counterfactual test | Change structure, check the model's response | §8.27 |
| Hard negative | Negative sample near the boundary | §8.27 |
| Clustering | Exploratory grouping; cluster ≠ class | §8.28 |
| Classification | Assigning candidate labels | §8.29 |
| Calibration | Scores match actual correctness frequencies | §8.29.2 |
| ModelAssessment | Wraps a score with semantics + provenance (BOOK-DEFINED) | §8.30 |
| Training provenance | wasGeneratedBy TrainingOrInferenceActivity | §8.30 |
| Self-reinforcing feedback | Predictions return as training data | §8.34 |
| Model collapse | Diversity decays when training on regenerated data | §8.34 |
| Path-based explanation | Explanation via paths in the graph | §8.35 |
| CandidateAxiom | Candidate axiom awaiting assessment | §8.41 |
| Blast radius | Conclusions affected if the axiom is wrong | §8.41 |
| Counterexample | Observation refuting a hypothesis | §8.42 |
| Ontology evolution | Ontology refinement under governance | §8.42 |

## Further reading

- Knowledge Graphs (Hogan et al.), Inductive Knowledge [@hogan-inductive]
- Translating Embeddings for Modeling Multi-relational Data (Bordes et al., TransE) [@bordes-transe-2013]
- Embedding Entities and Relations for Learning and Inference in Knowledge Bases (Yang et al., DistMult) [@yang-distmult-2015]
- Complex Embeddings for Simple Link Prediction (Trouillon et al., ComplEx) [@trouillon-complex-2016]
- Modeling Relational Data with Graph Convolutional Networks (Schlichtkrull et al., R-GCN) [@schlichtkrull-rgcn-2018]
- Fast Rule Mining in Ontological Knowledge Bases with AMIE+ (Galárraga et al.) [@galarraga-amie-2015]
- Inductive Relation Prediction by Subgraph Reasoning (Teru, Denis & Hamilton, GraIL) [@teru-grail-2020]
- A Review of Relational Machine Learning for Knowledge Graphs (Nickel et al.) [@nickel-relational-ml-2016]
- Distributed Representations of Words and Phrases and their Compositionality (Mikolov et al., negative sampling) [@mikolov-negativesampling-2013]
- Deeper Insights into Graph Convolutional Networks for Semi-Supervised Learning (Li et al., oversmoothing) [@li-oversmoothing-2018]
- Shortcut Learning in Deep Neural Networks (Geirhos et al.) [@geirhos-shortcut-2020]
- On Calibration of Modern Neural Networks (Guo et al.) [@guo-calibration-2017]
- AI models collapse when trained on recursively generated data (Shumailov et al.) [@shumailov-collapse-2024]
- Graph Representation Learning (Hamilton) [@hamilton-grl-2020]
- PROV-O: The PROV Ontology [@prov-o]
- Shapes Constraint Language (SHACL) [@w3c-shacl]
- Weisfeiler and Leman Go Neural: Higher-order Graph Neural Networks (Morris et al.) [@morris-weisfeiler-2019]
- How Powerful are Graph Neural Networks? (Xu et al., GIN) [@xu-gin-2019]
- RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space (Sun et al.) [@sun-rotate-2019]
- Poincaré Embeddings for Learning Hierarchical Representations (Nickel & Kiela) [@nickel-poincare-2017]
- Differentiable Learning of Logical Rules for Knowledge Base Reasoning (Yang et al., Neural LP) [@yang-neurallp-2017]
- DRUM: End-to-end Differentiable Rule Mining on Knowledge Graphs (Sadeghian et al.) [@sadeghian-drum-2019]
- Learning Explanatory Rules from Noisy Data (Evans & Grefenstette, $\partial$ILP) [@evans-dilp-2018]
