# Chapter 5 — Deduction, Rules, and Validation

> **Chapter orientation**
>
> **Central question:** Once we have an ontology with formal semantics, how do we *compute*
> the logical consequences of the data? And how do we *check* whether the data conforms to the
> constraints we defined? These two questions sound similar but belong to two entirely
> different pipelines.
>
> **Why it matters:** Chapter 4 taught us how to define formal meaning for symbols. But
> defining is not enough — we need a computational mechanism to (1) derive new knowledge from
> existing knowledge, and (2) validate whether data fits the constraints. Confusing these two
> pipelines is the root cause of many knowledge-system design errors.
>
> **You will understand:**
>
> - The core distinction: inference vs validation
> - Forward chaining with substitution ($\theta$) and the fixpoint
> - RDFS entailment: rules that ADD information, not constraints that check it
> - Materialization vs query-time reasoning
> - SHACL: target → focus node → path → value node → constraint → validation result
> - Conformance ≠ truth; violation ≠ repair
> - Consistency vs validation — two independent axes
> - Soundness/completeness depend on language + regime + task
> - The limits of OWL RL and Horn rules for full OWL 2 DL
>
> **Prerequisites:** Chapters 1–4. In particular: RDFS domain/range as inference rules (§3.1),
> interpretation → model → entailment (§4.3), necessary/sufficient conditions (§4.5), OWL
> Profiles (§4.12).
>
> **Concept map:**
>
> Inference ≠ Validation → Forward chaining with θ → Fixpoint → RDFS rules add information →
> Materialization vs query-time → Backward reasoning → SHACL mechanism walkthrough →
> Focus/value nodes → Validation report anatomy → Conformance ≠ Truth →
> Consistency ≠ Validation → Repair mechanism → Soundness + Completeness →
> OWL RL limits → SWRL/RIF context

## 5.1 Introduction: Two Questions, Two Pipelines

Chapter 4 answered the question "what do the symbols mean?" with the interpretation → model →
entailment mechanism. Now we face two practical questions:

1. **From what we know, what *follows*?** (What follows?)
2. **Does the existing data *conform* to the constraints we defined?** (Does data conform?)

These two questions look similar because both concern the relationship between data and
rules/semantics. But they belong to two entirely different pipelines:

| | Inference Pipeline | Validation Pipeline |
|---|---|---|
| **Question** | What follows? | Does the data conform? |
| **Input** | Graph + semantics (entailment regime) | Data + shapes/constraints |
| **Output** | New knowledge (entailments) | Conformance/violation report |
| **Direction** | Adds information | Checks information |
| **Example** | RDFS domain derives rdf:type | SHACL sh:class checks rdf:type |

The most common confusion in practice is using one pipeline's tool for the other pipeline's
purpose — for example, using `rdfs:domain` to "check" data (it does not check, it only derives),
or using a SHACL shape to "infer" new knowledge (it does not infer, it only validates).

> 🖊 **Self-check:** Before reading on, try to explain in your own words: if a property P has
> `rdfs:domain C`, and you see the triple `(x, P, y)` in the data while x has not been declared
> of type C, then (a) what does the inference pipeline do? (b) what does the validation pipeline
> do? How do the answers differ?

## 5.2 Forward Chaining: The Basic Inference Mechanism

### Intuition

Imagine you have a set of "if... then..." rules and an initial data graph. You apply all the
rules to the graph, add the new results to the graph, then apply the rules again to the
expanded graph. You repeat this process until no new results are produced. The final graph
contains everything that can be derived from the initial data under the chosen rule set.

That is **forward chaining** — the most basic inference mechanism in a knowledge system.

### Substitution: The Bridge Between Abstract Rules and Concrete Data

Before writing any formula, we need to understand a foundational mechanism: **substitution**.

A rule usually contains **variables**. For example:

$$\text{CapitalCity}(x) \to \text{City}(x)$$

This rule says: "for *any* $x$, if $x$ is a CapitalCity then $x$ is also a City." But the data
graph does not contain variables — it contains concrete entities like `Hanoi`, `HoChiMinh`.

A **substitution** $\theta$ (theta) is a mapping that assigns each variable a concrete value:

$$\theta = \{ x \mapsto \text{Hanoi} \}$$

Applying $\theta$ to the rule:

- $\theta(\text{body}) = \text{CapitalCity}(\text{Hanoi})$ — the body, now "ground"
- $\theta(\text{head}) = \text{City}(\text{Hanoi})$ — the head, now "ground"

If $\theta(\text{body})$ matches the data already present in the graph, then we are allowed to
add $\theta(\text{head})$ to the graph.

> ⚠ **Why substitution matters?** Without $\theta$, a rule is only an abstract pattern. It is
> substitution that connects a general rule to the concrete entities in the graph. This is the
> core mechanism of every rule-based inference system.

### The Formal Mechanism

Given a rule set $R$ and an initial graph $G_0$, forward chaining computes the sequence:

$$G_{i+1} = G_i \cup \{ \theta(\text{head}(r)) \mid r \in R, \; \theta(\text{body}(r)) \subseteq G_i \}$$

In words: at each step, find every rule $r$ and every substitution $\theta$ such that the
substituted body $\theta(\text{body}(r))$ matches the current graph $G_i$ completely, then add
the substituted head $\theta(\text{head}(r))$ to the graph.

The algorithm stops when it reaches a **fixpoint**:

$$G_{n+1} = G_n$$

When no new triple is produced, the graph $G_n$ is called the **closure** of $G_0$ under the
rule set $R$.

> ⚠ **Distinction:** A closure is a computational object — the graph containing the original
> assertions plus every materialized consequence. Entailment is a semantic relation — $\alpha$
> is entailed by $G$ if $\alpha$ is true in every model of $G$. Closure is one way to *compute*
> entailment, but closure ≠ entailment.

### A Full Worked Example: Forward Chaining Over Several Rounds

Consider the initial graph $G_0$:

```
Hanoi    rdf:type     CapitalCity
```

And two rules:

$$r_1: \text{CapitalCity}(x) \to \text{City}(x)$$
$$r_2: \text{City}(x) \to \text{Place}(x)$$

**Round 0:** $G_0 = \{ \text{CapitalCity}(\text{Hanoi}) \}$

**Round 1:** Find rules that match $G_0$:
- $r_1$ with $\theta_1 = \{x \mapsto \text{Hanoi}\}$:
  - $\theta_1(\text{body}) = \text{CapitalCity}(\text{Hanoi}) \in G_0$ ✓
  - Add $\theta_1(\text{head}) = \text{City}(\text{Hanoi})$
- $r_2$ with $\theta = \{x \mapsto \text{Hanoi}\}$:
  - $\theta(\text{body}) = \text{City}(\text{Hanoi}) \notin G_0$ ✗

$G_1 = G_0 \cup \{ \text{City}(\text{Hanoi}) \}$

**Round 2:** Find rules that match $G_1$:
- $r_1$: $\text{CapitalCity}(\text{Hanoi})$ already present, $\text{City}(\text{Hanoi})$ already present → nothing new added
- $r_2$ with $\theta_2 = \{x \mapsto \text{Hanoi}\}$:
  - $\theta_2(\text{body}) = \text{City}(\text{Hanoi}) \in G_1$ ✓
  - Add $\theta_2(\text{head}) = \text{Place}(\text{Hanoi})$

$G_2 = G_1 \cup \{ \text{Place}(\text{Hanoi}) \}$

**Round 3:** No rule produces a new triple. $G_3 = G_2$.

**Fixpoint reached.** The closure of $G_0$ under $\{r_1, r_2\}$ is:

$$G_\infty = \{ \text{CapitalCity}(\text{Hanoi}), \; \text{City}(\text{Hanoi}), \; \text{Place}(\text{Hanoi}) \}$$

The figure below summarizes the forward-chaining process over three rounds. Each arrow
represents one round of rule application with a specific substitution $\theta$. Round 3
produces no new triple → fixpoint.

![Forward chaining: $G_0 \to G_1 \to G_2 \to G_3 = G_2$ (fixpoint). Each round applies the rules with the substitution $\theta = \{x \mapsto \text{Hanoi}\}$, adding new triples until there is nothing left to add.](figures/generated/ch05-forward-fixpoint.pdf)

> 🖊 **Self-check:** Why does "no new triple" mean forward chaining has stabilized? If at round
> $k$ no new triple is added, what guarantees that round $k+1$ will also add nothing? (Hint: the
> rule set does not change, and the graph does not change.)

### A Worked Example on the Mechanism Domain — θ, Rule Chains, and Fixpoint

Apply the same mechanism to the running mechanism data. In the source graph we have:

```turtle
ex:rateOfChange_1 a ex:RateOfChangeMechanism .
ex:RateOfChangeMechanism rdfs:subClassOf ex:ChangeMechanism .
ex:ChangeMechanism rdfs:subClassOf ex:Mechanism .
```

The general form of the RDFS subClassOf rule is:

$$r_{sub}: A \text{ rdfs:subClassOf } B, \; x \text{ rdf:type } A \to x \text{ rdf:type } B$$

**Round 0:** $G_0$ contains the three triples above.

**Round 1:**
- Apply $r_{sub}$ with the substitution
  $$\theta_1 = \{ A \mapsto \text{ex:RateOfChangeMechanism}, B \mapsto \text{ex:ChangeMechanism}, x \mapsto \text{ex:rateOfChange}_1 \}$$
- $\theta_1(\text{body})$ consists of `ex:RateOfChangeMechanism rdfs:subClassOf ex:ChangeMechanism` and `ex:rateOfChange_1 a ex:RateOfChangeMechanism`, both $\in G_0$ ✓
- Add $\theta_1(\text{head}) =$ `ex:rateOfChange_1 a ex:ChangeMechanism`

$G_1 = G_0 \cup \{ \text{ex:rateOfChange\_1 a ex:ChangeMechanism} \}$

**Round 2:**
- Apply $r_{sub}$ with
  $$\theta_2 = \{ A \mapsto \text{ex:ChangeMechanism}, B \mapsto \text{ex:Mechanism}, x \mapsto \text{ex:rateOfChange}_1 \}$$
- $\theta_2(\text{body})$ consists of `ex:ChangeMechanism rdfs:subClassOf ex:Mechanism` and `ex:rateOfChange_1 a ex:ChangeMechanism` (just derived in round 1) ✓
- Add $\theta_2(\text{head}) =$ `ex:rateOfChange_1 a ex:Mechanism`

$G_2 = G_1 \cup \{ \text{ex:rateOfChange\_1 a ex:Mechanism} \}$

**Round 3:** No new pair `(A rdfs:subClassOf B, x : A)` remains to apply. $G_3 = G_2$.

**Fixpoint.** Forward chaining has materialized the classification: from `ex:rateOfChange_1 a
ex:RateOfChangeMechanism`, the rule derives `ex:rateOfChange_1 a ex:ChangeMechanism` and then
`ex:rateOfChange_1 a ex:Mechanism`. This is precisely the **classification fixpoint** of the
class-hierarchy mechanism in the mechanism domain.

> ⚠ **From substitution to ground fact.** The final triples (`ex:rateOfChange_1 a
> ex:Mechanism`) no longer contain variables — they are **ground facts**. A **ground triple**
> (or ground fact) is a triple in which every position is a concrete IRI or literal, with no
> variables remaining. The process of replacing variables with concrete values is called
> **grounding**.

### The Immediate Consequence Operator $T_P$ and the Least Fixed Point

The recurrence $G_{i+1} = G_i \cup \{\,\theta(\text{head}(r)) \mid \theta(\text{body}(r))
\subseteq G_i\,\}$ above is one concrete way of writing a more general and more powerful
notion: the **immediate consequence operator** $T_P$.

Given a rule program $P$ (a set of Horn/Datalog rules) and a set of ground facts $I$,
$T_P(I)$ is the set of every ground head obtainable from rules in $P$ whose bodies already lie
entirely in $I$:

$$T_P(I) \;=\; \bigl\{\, \theta(\text{head}(r)) \;\big|\; r \in P,\; \theta(\text{body}(r)) \subseteq I \,\bigr\}$$

Forward chaining is exactly the process of iterating $T_P$ starting from the empty set:

$$\emptyset \;\subseteq\; T_P(\emptyset) \;\subseteq\; T_P^2(\emptyset) \;\subseteq\; T_P^3(\emptyset) \;\subseteq\; \dots$$

**Why does this sequence grow?** Because $T_P$ is **monotone**: if $I \subseteq J$ then
$T_P(I) \subseteq T_P(J)$ — adding facts cannot remove a body that already matched. Over a
**finite ground universe** (only finitely many ground facts can exist), a monotonically
increasing sequence of sets must converge. Its destination is the **least fixed point** of
$T_P$:

$$\mathrm{lfp}(T_P) \;=\; \bigcup_{k \ge 0} T_P^{k}(\emptyset)$$

> ℹ **The basis of this claim is the Knaster–Tarski theorem.** On the lattice of ground-fact
> sets (ordered by inclusion), every monotone operator has a least fixed point, and that least
> fixed point is the intersection of all fixed points. Because $T_P$ is monotone, forward
> chaining always converges to exactly $\mathrm{lfp}(T_P)$.

An important practical consequence: $\mathrm{lfp}(T_P)$ **does not depend on the order** in
which you apply the rules. Whichever rule the engine runs first, the final result is unique.
This is what lets us speak of "the closure of $G_0$ under $P$" as a well-defined object, and
it is the foundation that lets many engines run rules in parallel (the RETE and RDFox parts of
§5.5).

### The Linear-Algebra Bridge: Transitive Closure via Powers of the Adjacency Matrix

If you have taken linear algebra, you can grasp this mechanism through a familiar analogy:
computing the **transitive closure** of a graph via powers of its adjacency matrix.

Let $A$ be the binary adjacency matrix of a graph ($A_{ij}=1$ if there is an edge $i \to j$).
Paths of length $k$ from $i$ to $j$ are recorded by the entry $(A^k)_{ij}$. The transitive
closure — every pair $(i,j)$ connected by some path — is the sum of powers:

$$A^{*} \;=\; A + A^{2} + A^{3} + \dots + A^{k}$$

taken until $A^{k+1}$ adds no new non-zero entry; at that point the sum has converged. This is
a fixed point: the power iteration stops when no new path appears.

| Linear algebra (transitive closure) | Forward chaining ($T_P$) |
|---|---|
| $A$ — asserted edges | $G_0$ — asserted graph |
| $A^k$ — paths of exactly $k$ steps | $T_P^k(\emptyset)$ — facts needing $k$ rule rounds |
| $A^*$ — all paths | $\mathrm{lfp}(T_P)$ — the closure |
| Halt when $A^{k+1}$ adds nothing | Halt when $G_{n+1} = G_n$ |

> ℹ **Analogy, not identity.** Forward chaining is more general than pure transitive closure,
> because a rule can join several patterns at once, not just connect two edges. But the
> intuition "iterate until nothing new appears" is common to both — and it explains why engines
> can use sparse matrix multiplication to speed up relational inference.

### Frame-by-Frame Visualization: Forward Chaining on the Mechanism KG

Let us watch this mechanism across four frames on the very mechanism ontology built in
Chapter 4. The source graph contains three asserted triples; the three Datalog rules below are
defined over that ontology:

$$r_1:\quad \text{hasInput}(m, q) \leftarrow \text{hasApplication}(m, a) \land \text{differentiand}(a, q)$$

$$r_2:\quad \text{hasReferenceVariable}(m, v) \leftarrow \text{hasApplication}(m, a) \land \text{withRespectTo}(a, v)$$

$$r_3:\quad \text{type}(m, \text{RateOfChangeMechanism}) \leftarrow \text{type}(m, \text{Mechanism}) \land \text{hasInput}(m, \_) \land \text{hasReferenceVariable}(m, \_)$$

> ℹ **$r_3$ is the Datalog form of the DL definition in §4.13.** In Chapter 4,
> $\text{RateOfChangeMechanism} \equiv \text{Mechanism} \sqcap \exists\text{hasApplication}.\text{DerivativeApplication}$.
> Here we rewrite it as a forward-chaining rule: a mechanism is classified as a
> RateOfChangeMechanism when it has both `hasInput` and `hasReferenceVariable` — the two
> properties every DerivativeApplication supplies (via `differentiand` and `withRespectTo`).
> The same knowledge, two representation styles.

**Frame 0 — Source graph $G_0$** (three asserted triples):

```turtle
ex:rateOfChange_1            ex:hasApplication    ex:derivativeApplication_1 .
ex:derivativeApplication_1   ex:differentiand     ex:position_1 .
ex:derivativeApplication_1   ex:withRespectTo     ex:time_1 .
```

**Frame 1 — First pass $G_1 = T_P(G_0) \cup G_0$:** $r_1$ and $r_2$ fire on $G_0$; two newly
inferred triples appear (highlighted in red):

```turtle
ex:rateOfChange_1   ex:hasInput                ex:position_1 .   # new — from r_1
ex:rateOfChange_1   ex:hasReferenceVariable    ex:time_1 .       # new — from r_2
```

**Frame 2 — Second pass $G_2 = T_P(G_1) \cup G_1$:** $r_3$ fires because `hasInput` and
`hasReferenceVariable` have just appeared; one new triple is added (highlighted in blue):

```turtle
ex:rateOfChange_1   rdf:type   ex:RateOfChangeMechanism .        # new — from r_3
```

**Frame 3 — Fixpoint $G_3 = T_P(G_2) \cup G_2$:** a pass over the rules on $G_2$ produces no
new triple; $G_3 = G_2$. The system halts, and the closure $\mathrm{lfp}(T_P)$ is materialized.

![Frame-by-frame forward chaining on the Mechanism KG: $G_0 \to G_1 \to G_2 \to G_3 = G_2$
(fixpoint). Frame 0: three asserted triples. Frame 1: two inferred triples (red). Frame 2: one
inferred triple (blue). Frame 3: no new triple → halt.](figures/generated/ch05-frame-by-frame.pdf)

> 🖊 **Self-check:** In Frame 2, why could $r_3$ not have fired already in Frame 0? Point to
> the ground fact that is missing from $G_0$ so that $r_3$'s body is not yet satisfied. (Hint:
> look at the two positions `hasInput(m, _)` and `hasReferenceVariable(m, _)`.)

### Monotonicity

Forward chaining works correctly thanks to **monotonicity**. An inference regime is monotonic
when:

$$\text{If } G \subseteq G' \text{ then } \text{Consequences}(G) \subseteq \text{Consequences}(G')$$

In words: adding information to the graph never removes conclusions that were already derivable.
New information only *extends* the result set, never *shrinks* it.

> ⚠ **Monotonicity does NOT mean:**
>
> - "Adding a condition to a rule body increases the results" — false; adding a condition to
>   the body makes the rule harder to match and can *reduce* the results.
> - "Monotonic = terminates" — false; these are two independent properties.
> - "Monotonic = complete" — false; a system can be monotonic yet still miss entailments.
> - "Monotonic = consistent" — false; a monotonic system can still derive a contradiction if
>   the initial data is contradictory.

**An example of monotonicity:** If from $G_0$ we derive `City(Hanoi)`, then no matter what
triples we add to the graph later, `City(Hanoi)` remains a valid consequence. We never have to
"retract" an old conclusion.

**Non-monotonic reasoning:** Conversely, systems that use negation-as-failure or "unless"-style
rules can retract a conclusion when new information appears. For example: "X is a bird → X
flies", but then adding "X is a penguin" retracts the "X flies" conclusion. This is a research
area of its own (non-monotonic reasoning); **default logic** [@reiter-default-1980] and
circumscription formalize exactly this "true-by-default, retract-when-contradicted" behavior.
This chapter mentions it only briefly, to draw the boundary.

### Termination Conditions

Forward chaining is guaranteed to terminate when all of the following hold at once:

1. **Finite initial graph** — the number of initial triples is finite.
2. **Finite rule set** — the number of rules is finite.
3. **Function-free rules** — no function symbol generates infinitely many new terms.
4. **Safe variables** (safe/range-restricted) — every variable in the head also appears in the
   body, ensuring the substitution only uses values already present in the graph.
5. **No mechanism generating unbounded fresh terms** — nothing creates infinitely many new
   resources/names (such as the fresh blank nodes of OWL existential semantics).

Under such a finite-ground condition, only finitely many ground facts can exist, so the
monotonically increasing process must reach a fixpoint.

> ⚠ **Important:**
>
> - **Termination ≠ Monotonicity.** A system can be monotonic yet still not terminate if the
>   conditions above are missing (for example, a rule with a function that generates infinitely
>   many new terms).
> - **Non-monotonic ≠ Non-terminating.** Negation/non-monotonicity and termination are two
>   independent properties. A non-monotonic system can still terminate, and a monotonic system
>   can still fail to terminate.
>
> The rule languages that are safe for KGs (RDFS entailment rules, OWL RL rules, RIF Core
> [@w3c-rif-core]) are designed to satisfy the conditions above, guaranteeing that forward
> chaining always terminates on a finite graph.

> ⚠ **Key note:** Forward chaining is an *algorithm*, not a *semantic definition*. It computes
> consequences based on a specific rule set. Different rule sets give different results from the
> same initial graph. Whenever you say "inference", you must always state: inference under
> *which regime* (entailment regime)?

> **In practice.** Forward chaining over safe, function-free, finite rules is exactly how a
> **Datalog** engine evaluates a recursive query. Production Datalog systems push this mechanism
> to industrial scale: **Soufflé** compiles Datalog programs to parallel C++ and is used for
> large-scale static analysis such as points-to and taint analysis [@souffle]; the survey *Datalog
> and Recursive Query Processing* [@datalog-survey-2013] covers the same fixpoint semantics we
> defined here, together with the semi-naïve optimizations that make it fast. The Python library
> **OWL-RL** [@owlrl] runs precisely this loop to materialize RDFS and OWL 2 RL closures over an
> RDFLib graph. The takeaway for an engineer: the abstract recurrence
> $G_{i+1}=G_i\cup\{\dots\}$ is not a toy — it is the inner loop of real rule engines.

## 5.3 RDFS Entailment Rules: Inference That Adds Information

RDF Schema (RDFS) defines a standard inference semantics. This semantics is defined formally by
model-theoretic semantics in RDF 1.1 Semantics [@w3c-rdf11-mt]. The four most important inference
rules, corresponding to the entailment patterns in Section 9.2.1 of the specification:

### rdfs:subClassOf (Pattern rdfs9)

If `A rdfs:subClassOf B` and `x rdf:type A`, then derive `x rdf:type B`.

This is the type-propagation rule along the class hierarchy, as the §5.2 example illustrated.

### rdfs:subPropertyOf (Pattern rdfs7)

If `P rdfs:subPropertyOf Q` and `x P y`, then derive `x Q y`.

This rule lets us build property hierarchies. For example: if `capitalOf rdfs:subPropertyOf
locatedIn`, then every pair `(city, capitalOf, country)` also entails `(city, locatedIn,
country)`.

### rdfs:domain (Pattern rdfs2)

If `P rdfs:domain C` and `x P y`, then derive `x rdf:type C`.

### rdfs:range (Pattern rdfs3)

If `P rdfs:range C` and `x P y`, then derive `y rdf:type C`.

### Domain/Range Are Inference Rules, NOT Validation Constraints

This is the key point emphasized in §3.1 and Chapter 4, and it needs repeating here because it
is the source of the most common confusion:

> ⚠ **rdfs:domain and rdfs:range ADD information to the graph.** They do NOT check, do NOT
> reject, and do NOT raise an error when data "does not match." If the property `locatedIn` has
> `rdfs:domain City`, and you see the triple `(UnknownEntity, locatedIn, SomePlace)` in the data,
> RDFS does *not* report an error — it derives `UnknownEntity rdf:type City`. The original triple
> still exists and remains valid.

The derived result can look absurd in practice. For example:

```
capitalOf   rdfs:domain   City
capitalOf   rdfs:range    Country
Vietnam     capitalOf     Hanoi
```

Forward chaining derives:

```
Vietnam   rdf:type   City       ← from domain
Hanoi     rdf:type   Country    ← from range
```

In reality, Vietnam is not a City and Hanoi is not a Country. But RDFS does not care about
"reality" — it only applies the semantic rule. The derived result is correct under RDFS
semantics even when it is meaningless in the application domain. This is exactly why:

$$\text{inference} \neq \text{validation}$$

Checking whether data "matches" expectations is the job of SHACL (§5.6), not of RDFS.

**A worked example on the mechanism domain.** In the mechanism ontology:

```turtle
ex:RateOfChangeMechanism rdfs:subClassOf ex:ChangeMechanism .
ex:ChangeMechanism rdfs:subClassOf ex:Mechanism .
```

If the data records `ex:rateOfChange_1 a ex:RateOfChangeMechanism`, the RDFS closure will add:

```turtle
ex:rateOfChange_1 a ex:ChangeMechanism .
ex:rateOfChange_1 a ex:Mechanism .
```

No one needs to write `ex:rateOfChange_1 a ex:Mechanism` explicitly; it is a logical consequence.
But if a shape requires every `ex:Mechanism` to have at least one `ex:hasOperation` and the data
lacks it, SHACL will report a violation — RDFS does not care about that.

> **In practice.** The **OWL-RL** library [@owlrl] and **Apache Jena**'s RDFS reasoner
> [@apache-jena-rules] implement exactly these rdfs2/rdfs3/rdfs7/rdfs9 patterns as forward-chaining
> rules over an RDF graph, producing the RDFS closure described above. When you call
> `apply_rdfs` in OWL-RL, you are running the mechanism of this section line for line.

### RDFS Rules: An Operationalization of Model-Theoretic Semantics

We must clearly separate two levels:

1. **Normative semantics:** RDFS entailment is defined by model-theoretic semantics in RDF 1.1
   Semantics [@w3c-rdf11-mt]. This definition determines *what counts as a consequence*,
   independently of any algorithm.

2. **Rule-based implementation:** The RDFS entailment patterns can be operationalized as
   forward-chaining rules. This approach is *sound* — every result is a valid entailment.
   However, on standard RDF syntax, a naive rule closure is *not complete* — there are valid
   entailments the rules cannot generate. Completeness requires generalized RDF syntax or
   additional mechanisms [@w3c-rdf11-mt, Appendix A].

> ℹ **Within the scope of this chapter,** we use forward chaining with the main RDFS patterns
> (subClassOf, subPropertyOf, domain, range) as a useful and intuitive implementation. This is a
> subset sufficient to illustrate the mechanism; the full normative semantics is out of scope.

### The RDFS Closure

Applying forward chaining with the RDFS rule set to a graph $G$ yields the **RDFS closure** of
$G$, written $\text{cl}_{\text{RDFS}}(G)$. This closure contains the triples derivable from $G$
under the rules applied.

> 🖊 **Self-check:** Given a graph containing: `(Hanoi, capitalOf, Vietnam)`, `(capitalOf,
> rdfs:domain, City)`, `(capitalOf, rdfs:range, Country)`. List all the triples derived by forward
> chaining with the RDFS domain and range rules. Explain each step, making the substitution
> $\theta$ explicit. Why do the results look "absurd" yet remain correct under RDFS semantics?

## 5.4 Materialization and Query-Time Inference

### The Core Distinction

In §4.3 we learned that **entailment is a semantic relation**: $O \models \alpha$ means $\alpha$
is true in every model of $O$. This relation exists independently of any computing system.

**Materialization** is an *implementation strategy*: precompute the closure and store the results
into the graph. It is one way to *realize* inference, not the concept of inference itself.

```
Entailment              = a semantic relation (abstract)
Materialization         = a precompute strategy (precompute + store)
Forward chaining        = a concrete algorithm
Query-time inference    = a lazy compute-on-demand strategy
```

### Technical Comparison: Materialization vs Query-Time

| | Materialization | Query-time inference |
|---|---|---|
| **How it works** | Compute the closure first, store the results | Reason while answering the query |
| **Advantages** | Fast queries, easy to inspect the derived graph | No stored closure, reflects the current graph |
| **Disadvantages** | Uses memory, needs invalidation on updates | Slower queries, repeated computation |
| **Best when** | Repeated queries, stable graph | Frequently changing data, large closure |

In practice, many systems use a **hybrid** strategy: materialize a subset of high-value
consequences (for example, the class hierarchy) and reason over the rest at query time.

> ⚠ **Asserted vs derived:** When a derived triple is stored, we need metadata/state to
> distinguish it from an asserted triple. Without it, updating, debugging, and tracing provenance
> become very difficult. The full provenance problem is handled in Chapter 6.

### When Is Materialization Feasible?

Materialization works well when:

- The rule set is monotonic and finite (RDFS, an OWL RL subset)
- The graph is not too large
- Queries are repeated many times (compute once, query fast afterward)

Materialization becomes infeasible when:

- The ontology is too expressive (see §5.15 on OWL 2 DL)
- The graph is very large (the closure can be far larger than the source graph)
- The data changes frequently (the closure must be recomputed on every update)

> ⚠ **Common misconception:** "The reasoner materializes all consequences." False. Many
> reasoners use a lazy strategy (compute on demand) or query rewriting. Materialization is only
> one implementation choice.

**A worked example on the mechanism domain.** Suppose the Mechanism-KG system serves the query
`?m a ex:Mechanism`. The source data only records `ex:rateOfChange_1 a
ex:RateOfChangeMechanism` and `ex:RateOfChangeMechanism rdfs:subClassOf ex:Mechanism`.

- **Materialization:** Compute the closure once, store `ex:rateOfChange_1 a ex:Mechanism` (and
  similarly for `ex:heatTransferRate_2`, `ex:newtonCooling_1`). From then on the query becomes a
  simple `SELECT`. Suitable when the taxonomy is stable and the `?m a ex:Mechanism` query is
  repeated continuously.
- **Query-time inference:** Do not store the derived triple; run RDFS subClassOf reasoning on
  every query. Suitable when the data changes frequently (for example, `ex:CandidateMechanism`
  entries added/deleted continuously) or when the closure is too large relative to actual queries.

If the system has both `ex:RateOfChangeMechanism` and `ex:CandidateMechanism` (also a subClassOf
`ex:Mechanism`), the closure will contain all of them as `ex:Mechanism`. When a candidate is
rejected and deleted, the closure must be recomputed — this is the cost of materialization that
the system must weigh.

> **Real-world anchors.** Materialization vs query-time is a real architectural fork in
> commercial KG platforms. **RDFox** materializes RDFS/OWL 2 RL consequences *incrementally* —
> recomputing only the affected part of the closure when data changes, rather than from
> scratch [@rdfox]. **Apache Jena** offers both a forward-chaining rule reasoner (eager
> materialization) and lazy query-time inference [@apache-jena-rules]. **OWL-RL** materializes
> the closure eagerly into a Python graph [@owlrl]. The hybrid strategy this section recommends
> is the default posture of most production stores.

## 5.5 Forward vs Backward: Two Computation Strategies

Forward chaining is not the only strategy. To see the full picture, we must compare it with
**backward chaining**.

### Forward: Compute First, Look Up Later

For the question "Is Hanoi a Place?", forward chaining:

1. Computes the closure from $G_0$: $\text{CapitalCity}(\text{Hanoi}) \to \text{City}(\text{Hanoi}) \to \text{Place}(\text{Hanoi})$
2. Answers by lookup: `Place(Hanoi)` ∈ closure → Yes.

### Backward: Start from the Question, Find a Proof

For the same question "Place(Hanoi)?", backward chaining:

1. **Goal:** Prove $\text{Place}(\text{Hanoi})$.
2. Find a rule whose head matches: $r_2: \text{City}(x) \to \text{Place}(x)$ with $\theta = \{x \mapsto \text{Hanoi}\}$.
3. **Subgoal:** Prove $\theta(\text{body}) = \text{City}(\text{Hanoi})$.
4. Find a rule: $r_1: \text{CapitalCity}(x) \to \text{City}(x)$ with $\theta = \{x \mapsto \text{Hanoi}\}$.
5. **Subgoal:** Prove $\text{CapitalCity}(\text{Hanoi})$.
6. This is an assertion in $G_0$ → **Success.** Propagate the result back up.

### Comparison

| | Forward | Backward |
|---|---|---|
| **Direction** | Data-driven: from data → results | Goal-driven: from question → proof |
| **Best when** | Many queries over the same graph | Few queries, large graph |
| **Cost** | Compute the closure once (possibly large) | Compute per-query (possibly repeated) |
| **Result** | The whole closure | Only the proof for the specific question |

> ⚠ **Note:** This is a mental model of computation strategies, not an exact description of
> every OWL reasoner. Real Description Logic reasoners typically use specialized
> tableau/hypertableau/classification algorithms, not simply a forward or backward rule engine.

### How Engines Actually Run: the RETE Network

So far we have described forward chaining as a loop that "scans every rule, every
substitution". That is the semantic definition; a naive implementation, however, is extremely
slow: each round re-examines every rule against every combination of triples, at a cost of
about $O(|R| \cdot |G|^{k})$ where $k$ is the number of patterns in a body. Most of that work
is repeated — the parts of a body that matched last round are still true.

**RETE** (Forgy, 1982 [@forgy-rete-1982]) fixes exactly this by **keeping the intermediate
matches** instead of recomputing them from scratch. The core idea: *trade memory for speed*.

A RETE network consists of:

- **Alpha network (one-input nodes):** filters *within a single pattern* — e.g. "is the subject
  an IRI?", "is the predicate equal to `ex:capitalOf`?". Each pattern of a rule goes through its
  own alpha path; the survivors are the filtered **Working Memory Elements (WMEs)**.
- **Beta network (two-input nodes):** **joins** variable bindings across different patterns and
  **caches** the resulting intermediate tuples in **beta memory**. When a new WME arrives, it
  only needs to be joined with the cached part, not recomputed entirely.
- **Agenda + conflict resolution:** when a rule matches completely it is placed on the **agenda**
  (a priority queue); **conflict resolution** chooses which rule fires first when several are
  simultaneously ready.

> ℹ **Why is RETE fast?** It exploits **monotonicity**: once half of a join is correct, adding a
> new fact only needs to *extend* the join, never to undo the old part. Beta memory is the
> physical embodiment of the observation that "$\mathrm{lfp}(T_P)$ is order-independent" (§5.2)
> — the engine keeps every intermediate match and computes only the delta.

The trade-off: RETE is fast on large rule sets but **consumes memory** to cache all the
intermediate bindings.

### In-Memory RETE vs Parallel Incremental Datalog

Two families of modern engines reflect two different points on the trade-off curve:

| | In-memory RETE (Drools, Apache Jena) | Parallel incremental Datalog (RDFox) |
|---|---|---|
| **Nature** | Alpha/beta network caching bindings | Datalog materialization over a compressed graph |
| **Optimized for** | Many rules, rich conditions | Large RDF graphs, continuous updates |
| **Updates** | Incremental per WME | **Incremental, parallel, lock-free** |
| **Source** | Forgy 1982 [@forgy-rete-1982] | Motik et al. 2014 [@motik-rdfox-2014] |

**RDFox** represents the second direction: it materializes Datalog programs directly over a
compressed, columnar, in-memory RDF graph, and — unlike sequential RETE — performs **parallel,
lock-free incremental materialization** [@motik-rdfox-2014]. When a schema changes, it recomputes
only the affected part of the closure rather than rebuilding from scratch. This is why RDFox
handles large, frequently-updated graphs while keeping latency low.

> ℹ **One semantics, many implementations.** Whether RETE or parallel Datalog, both must return
> exactly $\mathrm{lfp}(T_P)$ — the uniqueness of the fixed point (§5.2) is the contract that
> lets engines compete on speed without changing the result.

## 5.6 SHACL: Validating Data with Shapes

### Mental Model: SHACL Is Not "OWL Closed-World"

A common misconception: "OWL = open world, SHACL = closed world." This framing is too simple and
misleading.

A more accurate understanding:

- **OWL** asks about interpretations: "In every model satisfying the ontology, what is true?"
- **SHACL** asks about one specific data graph: "Does *this supplied* data graph satisfy the
  defined shapes?"

SHACL is not OWL with CWA switched on. SHACL is a separate validation framework with its own
semantics and purpose. Some SHACL constraints make the absence/count in the supplied graph
meaningful — this *resembles* closed-world behavior at certain points. But SHACL is not simply
OWL + CWA.

### The SHACL Pipeline

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

SHACL conformance does NOT establish truth. A SHACL violation does NOT establish logical
inconsistency. They are judgments about the supplied data structure, not about model-theoretic
semantics.

### What Is a Shape?

A **shape** in SHACL is an RDF resource describing a checking condition [@w3c-shacl]. A shape is
not an ontology axiom — it does not participate in RDFS/OWL inference. A shape is used only by
the SHACL validation engine.

### The SHACL Mechanism: Target → Focus Node → Path → Value Node → Constraint → Result

To understand how SHACL actually works, we must grasp the following mechanism chain. Consider the
example:

**Data:**

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

**Step 1 — Target:** `sh:targetClass ex:City` selects the candidate nodes. Per the SHACL spec
[@w3c-shacl, §2.1.3.2], the targets include all **SHACL instances** of `ex:City`. A SHACL
instance follows the `rdfs:subClassOf*` chain: if `CapitalCity rdfs:subClassOf City` and `Hanoi
rdf:type CapitalCity`, then Hanoi is also a SHACL instance of City and is targeted. (Note: the
required `rdfs:subClassOf` declarations must be present in the data graph.)

**Step 2 — Focus node:** Each targeted node becomes a **focus node** — the node being evaluated.
Here: `ex:Hanoi` is the focus node.

**Step 3 — Path:** `sh:path ex:name` defines the property path from the focus node. The engine
finds all value nodes reachable from the focus node via this path.

**Step 4 — Value nodes:** The set of target nodes reached from the focus node via the path.
Currently: there is no triple `ex:Hanoi ex:name ...` → the value-node set = ∅ (empty).

**Step 5 — Constraint:** `sh:minCount 1` requires at least 1 value node. The value-node set is
empty → the constraint is NOT satisfied.

**Step 6 — Result:** A violation is produced.

Now add the triple:

```turtle
ex:Hanoi  ex:name  "Hà Nội" .
```

Repeat steps 3–6: the path `ex:name` now reaches 1 value node (`"Hà Nội"`). `minCount 1` → the
constraint is satisfied. There is no violation for this constraint.

The figure below visualizes the whole SHACL mechanism chain from target to result. Read top to
bottom: each step is a deterministic transformation, not an inference.

![The SHACL mechanism: Target → Focus Node → Path → Value Nodes → Constraint → Result. Each step is a deterministic mechanism. The shape checks existing data; it does not derive new knowledge.](figures/generated/ch05-shacl-mechanism.pdf)

> ⚠ **sh:targetClass is NOT an exact triple grep.** It uses SHACL instance semantics, including
> subclass reasoning over `rdfs:subClassOf*`. Likewise, `sh:class C` checks whether a value node
> is a SHACL instance of C (via the subclass chain), not merely whether `rdf:type C` is explicit
> [@w3c-shacl, §4.1.1].

### SHACL Constraint Types (Organized by Problem)

#### Presence/Cardinality

| Constraint | Meaning | Example |
|------------|---------|---------|
| `sh:minCount n` | At least n value nodes | Every City has ≥ 1 name |
| `sh:maxCount n` | At most n value nodes | Every City has ≤ 1 capitalOf |

#### Type

| Constraint | Meaning | Note |
|------------|---------|------|
| `sh:datatype dt` | Value must have the specified datatype | Literal only |
| `sh:class C` | Value must be a SHACL instance of C | Uses subclass reasoning |
| `sh:nodeKind kind` | Value must be an IRI/BlankNode/Literal | Checks the RDF term kind |

#### Structural

| Constraint | Meaning | Important note |
|------------|---------|---------------------|
| `sh:closed true` | Only declared properties are allowed | Does NOT turn all of RDF into a CWA; applies only to this shape, over this target set |

#### Logical Composition

| Constraint | Meaning |
|------------|---------|
| `sh:and` | All sub-shapes must be satisfied |
| `sh:or` | At least one sub-shape is satisfied |
| `sh:not` | The sub-shape must NOT be satisfied |

> ⚠ **sh:closed is not a global Closed World Assumption.** It only rejects properties not
> declared *within that shape*, for *the targeted focus nodes*. Other parts of the graph are
> unaffected.

> 🖊 **Self-check:** Given a shape requiring `City` to have exactly 1 `capitalOf` with range
> `Country`. If the data has `(Hanoi, capitalOf, Vietnam)` and `(Hanoi, capitalOf, France)`, what
> will the SHACL report say? If the data has `(Hanoi, capitalOf, "not-a-country")`, what will the
> report say? How do the two cases differ?

> **In practice.** The target→focus→path→value→constraint→result chain is exactly what a SHACL
> engine executes. **pySHACL** [@pyshacl] is a pure-Python validator that implements the SHACL
> 1.0 Recommendation and is the validator used in this book's toolchain. Conformance to the spec
> is measured by the **W3C SHACL test suite** [@shacl-cts], which runs each validator against the
> same shapes and data and checks the produced report — which is why "does my validator implement
> `sh:class` subclass semantics?" is a testable question, not a guess.

**A selection shape on the mechanism domain.** In the Mechanism-KG pipeline, each new mechanism
from a second source (Chapter 3) enters as an `ex:CandidateMechanism` — not yet accepted, needing
a structural check before its content is considered. The following shape defines a valid
candidate:

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

Data:

```turtle
ex:candidateRateOfChange_1 a ex:CandidateMechanism ;
    rdfs:label "RATE_OF_CHANGE (draft)" ;
    ex:hasOperation ex:derivativeOperation_1 ;
    ex:hasInput ex:position_1 .
```

Repeat the 6-step mechanism chain for the `hasOutput` constraint:
`sh:targetClass ex:CandidateMechanism` → focus node `ex:candidateRateOfChange_1` →
`sh:path ex:hasOutput` → **value nodes = ∅** (no `hasOutput` triple at all) → `sh:minCount 1`
not satisfied → violation. The other three constraints (`hasOperation`, `hasInput`,
`rdfs:label`-datatype) are all satisfied because the data has them. Result: 1 violation,
`sh:conforms = false`.

> ⚠ **A shape checks structure, not truth.** A candidate missing `ex:hasOutput` may still be a
> factually correct description — it simply lacks the structure the system needs to trust it.
> Conversely, a candidate with every field present may still be wrong in content. This is exactly
> the conformance ≠ truth boundary of §5.8.

## 5.7 Validation Report: Anatomy

When SHACL validation runs, the engine produces a **validation report** [@w3c-shacl, §3.6]:

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
        sh:resultMessage "Every City must have at least one name" ;
    ]
] .
```

Each ValidationResult answers a debugging question:

| Question | Property | Note |
|----------|----------|---------|
| Which node failed? | `sh:focusNode` | Always present |
| Which path? | `sh:resultPath` | May be absent for node-level violations |
| Which value caused it? | `sh:value` | **Only when applicable** — e.g. a minCount violation may have no value node |
| Which shape? | `sh:sourceShape` | The shape that raised the constraint |
| Which constraint? | `sh:sourceConstraintComponent` | The kind of constraint violated |
| Severity? | `sh:resultSeverity` | Violation / Warning / Info |
| Message? | `sh:resultMessage` | A human-readable description |

> ⚠ **sh:value is not always present.** For `sh:minCount`, the violation happens because a value
> node is *missing* — there is no specific "offending value". `sh:value` appears only when the
> constraint component definition specifies it. Do not fabricate a value when there is none.

**The report for the mechanism candidate.** For the `ex:hasOutput` violation in §5.6, the
validation report records:

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
        sh:resultMessage "Every CandidateMechanism must have at least one output (hasOutput)" ;
    ]
] .
```

Note: `sh:value` does **not** appear in this result — the violation happens because a value node
is missing, not because some specific value is wrong. Reading the report relies on
`sh:focusNode` + `sh:resultPath` + `sh:sourceConstraintComponent` to know *which node, which
path, which constraint* was violated.

## 5.8 Conformance ≠ Truth: The Boundary of Validation

### Conformance Is Not Truth

A graph that **conforms** to SHACL shapes means the data satisfies the defined conditions. This
does NOT mean:

- The data is true to reality
- The data is complete
- The data is logically consistent
- The data is trustworthy

A graph can fully conform to shapes while still containing false information. Conversely, a graph
can violate shapes while still containing true information — only that information does not match
the expected structure.

```
Conformance   = data matches the shapes      ≠ data is correct
Violation     = data does not match shapes   ≠ data is wrong
```

### Why Does This Distinction Matter?

In the practice of building knowledge systems:

1. **Validation gate:** Use SHACL to filter incoming data — violating data is rejected or
   flagged. But data that passes the gate is not necessarily correct.
2. **Quality signal:** A SHACL violation is a signal about structural quality, not about content
   correctness.
3. **Evolution:** When the schema changes, old data may violate new shapes while still being
   correct in content.

## 5.9 Consistency ≠ Validation: Two Independent Axes

The distinction between **OWL consistency** and **SHACL validation** is one of the subtlest
points in knowledge-system design. These two concepts lie on two entirely independent axes.

### Axis 1: Consistency

**Question:** "Does at least one model (interpretation) satisfying the ontology exist?"

This is a model-theoretic question. If ontology + data has at least one model → consistent. If no
model exists → inconsistent.

### Axis 2: Validation

**Question:** "Does the supplied data graph satisfy the defined shapes?"

This is a question about a specific data structure, not about the existence of a model.

### Case A: OWL-inconsistent but SHACL-conformant

The ontology declares:

```
City owl:disjointWith Country
```

Data:

```
Hanoi rdf:type City .
Hanoi rdf:type Country .
Hanoi ex:name "Hà Nội" .
```

**OWL:** Inconsistent — Hanoi cannot be both a City and a Country if the two classes are
disjoint. No model satisfies this.

**SHACL:** Suppose the shapes only require "City has a name" and "Country has a name". Hanoi has
`ex:name` → the shapes are satisfied → **conforms = true**.

SHACL knows nothing about `owl:disjointWith`. It only checks the shapes provided.

### Case B: OWL-consistent but SHACL-invalid

Data:

```
Hanoi rdf:type City .
```

(No `ex:name` triple for Hanoi.)

**OWL (OWA):** Perfectly consistent. Under the Open World Assumption, Hanoi *may* have some name
we do not know about. There is no contradiction.

**SHACL:** The shape requires `sh:minCount 1` on `ex:name` for City. No value node →
**violation**.

OWL says "there may be a name" (no contradiction). SHACL says "in the supplied graph, there is no
name" (violation). Both are correct — they answer different questions.

### Summary Table

The figure below illustrates the four possible combinations of the two independent axes. Every
cell can occur in practice — none is excluded.

![Consistency (OWL) × Validation (SHACL): all four combinations can occur. The two axes are entirely independent — knowing one does not imply the other.](figures/generated/ch05-consistency-vs-validation.pdf)

| | OWL Consistent | OWL Inconsistent |
|---|---|---|
| **SHACL conforms** | ✅ Normal | ⚠️ Can occur (shapes do not cover the axiom) |
| **SHACL violates** | ⚠️ Can occur (OWA vs data-check) | ⚠️ Can occur |

> ⚠ **Lesson:** Consistency and conformance are two independent axes. Knowing one does not imply
> the other. A complete knowledge system needs both: OWL to ensure the ontology is consistent,
> SHACL to ensure the data conforms to the expected structure.

> 🖊 **Self-check:** Explain why the OWL existential restriction `City ⊑ ∃hasName.xsd:string`
> does NOT cause a violation when Hanoi is a City but has no hasName, while the SHACL
> `sh:minCount 1` on hasName DOES cause a violation. Where does the difference lie?

**The two axes on the mechanism domain.** Same analysis, but using Mechanism-KG data.

*Case A — OWL-inconsistent but SHACL-conformant.* The ontology declares
`ex:ChangeMechanism owl:disjointWith ex:AggregationMechanism`. The data records:

```
ex:someMechanism_9 a ex:ChangeMechanism .
ex:someMechanism_9 a ex:AggregationMechanism .
ex:someMechanism_9 ex:hasOperation ex:someOperation_1 .
```

- **OWL:** inconsistent — an individual cannot belong to two disjoint classes (§4.9).
- **SHACL:** the shape only checks structure (has `ex:hasOperation`, has a label) → **conforms**.
  SHACL does not read `owl:disjointWith`; it does not know these two classes conflict.

*Case B — OWL-consistent but SHACL-violating.* The data has only:

```
ex:candidateRateOfChange_1 a ex:CandidateMechanism .
```

- **OWL (OWA):** consistent — the missing `ex:hasOutput` causes no contradiction (§4.8).
- **SHACL:** `CandidateMechanismShape` requires `sh:minCount 1` on `ex:hasOutput` →
  **violation**.

The 2×2 table keeps its meaning: knowing OWL consistency does not tell you the SHACL validation
result, and vice versa. The Mechanism-KG system needs both axes: the ontology to catch modeling
errors (a violated disjointness), the shapes to block structurally incomplete candidates before
they enter the knowledge store.

> **Real-world anchors.** The "closed-world" intuition SHACL partially evokes has a precise
> origin: **Reiter's Closed World Assumption** [@reiter-cwa-1978], which treats anything not
> derivable from a database as false. SHACL borrows that *flavor* for its count constraints
> (absence of a value node fails `minCount`) but is not CWA in Reiter's logical sense — it makes
> no claim about truth, only about whether the supplied graph matches the shapes. That gap is
> exactly the conformance ≠ truth boundary of §5.8.

## 5.10 Shapes ≠ Axioms: Distinguishing SHACL from an Ontology

The distinction between SHACL and an ontology is one of the most important boundaries in
knowledge-system design:

| | Ontology (RDFS/OWL) | SHACL Shapes |
|---|---|---|
| **Purpose** | Define what follows | Define what is allowed |
| **Basis** | Model-theoretic statements about interpretations | Validation of a specific data graph |
| **Result** | Entailments (new triples) | Validation report (conforms/violation) |
| **Participates in inference** | Yes | No |
| **Example** | `rdfs:domain` derives rdf:type | `sh:class` checks rdf:type |

Same vocabulary (`class`, `property`, `datatype`), but opposite direction:

- `P rdfs:domain C` + `(x, P, y)` → derive `x rdf:type C` (adds information)
- `sh:property [ sh:path P ; sh:class C ]` + `(x, P, y)` → check whether `y` is a SHACL instance of C (checks information)

**Three different roles: rule, axiom, shape.** The same piece of mechanism-domain knowledge can be
expressed in three ways with three different semantics — do not mix them up:

| Role | Example stating "a Mechanism must have an Operation" | What happens when the data lacks `hasOperation`? |
|---------|----------------------------------------------------|--------------------------------------------------|
| **Rule** | `Mechanism(x) ∧ hasOperation(x, op) → Operation(op)` (Horn rule, §5.2) | Derives `Operation(op)` when there is enough evidence; complains about nothing when it is missing |
| **OWL axiom** | `Mechanism ⊑ ∃hasOperation.Operation` (§4.13) | No contradiction — OWA assumes an unnamed filler exists |
| **SHACL shape** | `sh:path ex:hasOperation ; sh:minCount 1` (§5.6) | Reports a **violation** — the supplied data lacks the expected structure |

A rule **adds** knowledge, an axiom **constrains model-theoretic semantics**, a shape **checks the
structure of specific data**. Who does what decides the correct design of the system.

### OWL Existential Restriction vs SHACL minCount

This is the strongest distinguishing example:

**OWL:** `City ⊑ ∃hasName.xsd:string`

Means: "In every model, each City must have *at least one* hasName-successor." But under OWA, if
the data has no hasName for Hanoi, OWL does *not* create an inconsistency — it only assumes an
unnamed witness exists in the model.

**SHACL:** `sh:path ex:name ; sh:minCount 1`

Means: "In the *supplied* data graph, the focus node must have at least 1 value node via the path
ex:name." If there is none → violation.

OWL talks about models. SHACL talks about a specific data graph. Same requirement "must have a
name", but entirely different semantics.

> ⚠ **They do not replace each other.** An ontology cannot replace SHACL for checking data.
> SHACL cannot replace an ontology for inferring knowledge. A complete knowledge system usually
> needs both.

### SHACL Is a Non-Monotonic Constraint Language: Local Closed-World Semantics

The table above shows that a shape *checks* rather than *infers*. But there is a deeper
property that explains **why** SHACL behaves differently from an ontology: SHACL uses **Local
Closed-World Semantics (LCWA)** and is therefore a **non-monotonic** constraint language.

- **Open World (OWA) — ontology side:** not seeing a triple `hasOperation` ⇒ *unknown* whether
  it exists; an unnamed witness might exist (§4.8, §5.10). Adding data never retracts a
  previously derived conclusion — **monotonic**.
- **Local Closed-World (LCWA) — SHACL side:** for each focus node, what is *absent* from the
  graph is treated as *non-existent* for that node. Missing a value node ⇒ immediate violation.

The direct consequence: **adding a triple can turn a conforming graph into a violating one.**
Consider a shape with `sh:maxCount 1` on `ex:hasReferenceVariable`:

```turtle
# Before: conforms
ex:roc_1  ex:hasReferenceVariable  ex:time_1 .

# After ADDING one more triple: VIOLATION (exceeds maxCount 1)
ex:roc_1  ex:hasReferenceVariable  ex:time_1 .
ex:roc_1  ex:hasReferenceVariable  ex:temp_2 .
```

The behaviour "adding information retracts an old conclusion" is exactly **non-monotonicity**
— the opposite of the forward chaining we saw in §5.2. This is the same mechanism as
*negation as failure* (§5.16): SHACL interprets "not found" as "does not exist", and that
interpretation is non-monotonic.

> ℹ **Why "local"?** SHACL does not close the whole world blindly like classical CWA (Reiter
> 1978). It only closes *within the scope of each focus node and each constraint*: absence is
> counted as a violation only when a specific shape demands presence. Outside that scope, OWA
> still applies.

## 5.11 Inference Before Validation: Interaction Between the Two Pipelines

The result of SHACL validation depends on which graph is fed into the validator. This is an
important architectural decision:

### Architecture A: Validate Directly

```
asserted graph → SHACL validator → report
```

The validator sees only the asserted data. Derived triples are not considered.

### Architecture B: Infer First, Validate After

```
asserted graph → RDFS/OWL materialization → expanded graph → SHACL validator → report
```

The validator sees both asserted + derived triples. For example: if RDFS derives `Hanoi rdf:type
City`, then SHACL shapes targeting City will apply to Hanoi.

### Architecture C: Validator with Integrated Entailment

```
asserted graph → SHACL processor (configured with entailment support) → report
```

Some SHACL processors support configuring entailment/preprocessing. Not all SHACL processors
perform OWL reasoning automatically.

> ⚠ **Important:**
>
> - Do NOT assume all SHACL processors automatically infer RDFS/OWL.
> - Do NOT assume SHACL always ignores inference.
> - The specific architecture is an implementation decision and must be documented clearly.

A production system should state clearly:

```
asserted graph        = the source data
inferred graph        = the inference result (if any)
effective validation graph = the graph actually validated
entailment regime     = the inference regime applied (if any)
```

> ⚠ **Effective validation graph** is the graph the validator actually sees. It may be the
> asserted graph, the expanded graph, or another variant depending on the architecture.
> Misunderstanding the effective validation graph is the source of many subtle bugs in knowledge
> systems.

## 5.12 Violation ≠ Repair: The Graph Repair Mechanism

SHACL reports: "the current representation violates requirement X." It does NOT determine which
transformation is epistemically correct.

### Example: Hanoi Lacks ex:name

Violation: `ex:Hanoi` lacks `ex:name` (minCount 1).

Candidate repairs:

| Repair | Action | Semantic consequence |
|--------|-----------|---------------------|
| A | Add `ex:Hanoi ex:name "Hà Nội"` | Adds information — correct if the name really is "Hà Nội" |
| B | Delete `ex:Hanoi rdf:type ex:City` | Changes the classification — correct if Hanoi is not a City |
| C | Change the shape (drop minCount) | Changes the requirement — correct if the requirement is too strict |
| D | Mark the record incomplete, reject ingestion | Rejects the data — correct if the source is untrustworthy |
| E | Resolve identity with another source, import the name | Integrates a source — correct if a supplementary source exists |

All of them can make SHACL green. But only domain knowledge, evidence, and governance decide which
repair is correct.

### The Repair Pipeline

The figure below illustrates the repair pipeline as a decision problem: from a violation to many
candidate repairs, through a semantic/epistemic evaluation, then selecting a repair. Note the
message at the bottom: passes validation ≠ becomes true.

![The Graph Repair pipeline: Violation → Candidate Repairs (ADD/DELETE/SHAPE CHANGE/REJECT) → Evaluate semantic + epistemic consequences → Select repair → Apply + Revalidate. Passes validation ≠ becomes true.](figures/generated/ch05-repair-pipeline.pdf)

```
Violation
    ↓
Candidate Repairs (many options)
    ↓
Evaluate semantic + epistemic consequences
    ↓
Select repair (based on domain knowledge/governance)
    ↓
Apply repair → Revalidate
```

### Repair Operation Types

- **ADD:** Add the missing statement
- **DELETE:** Delete the statement causing the violation
- **RECLASSIFY / REMODEL:** Change the type or graph structure
- **SHAPE CHANGE:** Change the requirement instead of the data

> ⚠ **Repairing data to make SHACL green CAN change the intended semantics.** Therefore repair is
> a decision problem, not merely a syntactic patch.
>
> $$\text{passes validation} \neq \text{becomes true}$$

This is a direct bridge to Chapter 6: when does data become trustworthy knowledge? Who has the
authority to decide a repair? What evidence supports it?

**A worked example on the mechanism domain.** The candidate `ex:candidateRateOfChange_1` lacks
`ex:hasOutput` (§5.6). The candidate repairs:

| Repair | Action | Consequence | Basis for the decision |
|--------|-----------|--------|------------------|
| A | Add `ex:hasOutput ex:velocity_1` | Adds information — correct if the candidate really computes velocity | A second source (textbook B) confirms the output; strong evidence |
| B | Add `ex:hasOutput ex:unknownOutput_1` | Adds a placeholder — makes SHACL green but has no knowledge value | No evidence; only hides the violation |
| C | Delete `ex:candidateRateOfChange_1 a ex:CandidateMechanism` | Removes the candidate from the pipeline — loses the second source's information | The source is untrustworthy; a governance decision |
| D | Fix the shape: `hasOutput` sh:minCount 0 | The shape becomes lenient — but accepts a candidate with no output | The business requirement allows incomplete candidates |

Only (A) is a knowledge-meaningful repair — it rests on evidence from a second source, not merely
"making SHACL green" like (B). (C) rejects the data, (D) changes the shape — both valid in
different contexts. The decision belongs to domain governance, not to the SHACL engine.

## 5.13 Soundness and Completeness

When evaluating an inference system, the two most important properties are **soundness** and
**completeness**. But both are meaningless without a stated scope.

### The Set Model

Let:

- $E$ = the set of all semantic consequences under the chosen entailment regime (entailed conclusions)
- $A$ = the set of results the algorithm returns

**Sound:** $A \subseteq E$

The algorithm returns no wrong results (no false positive). Everything it derives is a valid
entailment.

**Complete:** $E \subseteq A$

The algorithm misses no result (no false negative). Every valid entailment is derived.

**Sound + Complete:** $A = E$

The algorithm returns exactly the set of semantic consequences — nothing extra, nothing missing.

The figure below illustrates the three cases with set diagrams. Sound but incomplete: $A$ sits
inside $E$ but does not cover it. Unsound: $A$ spills outside $E$ (a false positive). Sound +
complete: $A = E$ exactly.

![Soundness and Completeness as set relations. Left: sound but incomplete ($A \subseteq E$, misses some). Middle: unsound ($A \not\subseteq E$, has a false positive). Right: sound + complete ($A = E$, exact).](figures/generated/ch05-soundness-completeness.pdf)

### Three Mandatory Components

Every claim about soundness/completeness MUST state three components:

1. **Language/profile**: RDFS? OWL EL? OWL RL? full OWL 2 DL?
2. **Entailment regime**: Direct Semantics? RDF-Based? Simple?
3. **Reasoning task**: Consistency checking? Subsumption? Instance checking? Conjunctive query answering?

A correct example: "Forward chaining with the OWL RL rule set is sound and complete for the
instance-checking task on an OWL 2 RL ontology satisfying the profile's syntactic restrictions."

A wrong example: "Reasoner X is sound and complete." (Missing all three components.)

### Three Cases on Real Mechanism Data

The abstract "$A \subseteq E$" is only fully meaningful when we see A and E *concretely*. Using
the very RATE_OF_CHANGE data from §5.2:

```
G0 (asserted data):
ex:rateOfChange_1 a ex:RateOfChangeMechanism .
ex:RateOfChangeMechanism rdfs:subClassOf ex:ChangeMechanism .
ex:ChangeMechanism rdfs:subClassOf ex:Mechanism .
```

Entailment regime: RDFS; task: instance classification. The set of semantic consequences
$E = \{ \texttt{rateOfChange\_1 a ChangeMechanism},\ \texttt{rateOfChange\_1 a Mechanism} \}$ —
this is the *standard* every algorithm is measured against.

**CASE 1 — Sound but incomplete ($A \subset E$).** The algorithm, missing the rule
`ChangeMechanism rdfs:subClassOf Mechanism` (or failing to load the taxonomy layer), derives only
one step:

```
A = { rateOfChange_1 a ChangeMechanism }
```

Every element of A is in E (sound ✓) but it misses `rateOfChange_1 a Mechanism` (not complete ✗).
Every conclusion is correct; the system simply answers more sparsely than it could.

**CASE 2 — Unsound ($A \not\subseteq E$).** A rule is written wrong: `RateOfChangeMechanism
rdfs:subClassOf AggregationMechanism` (the wrong taxonomy branch). The algorithm derives:

```
A = { rateOfChange_1 a ChangeMechanism,
      rateOfChange_1 a Mechanism,
      rateOfChange_1 a AggregationMechanism }   ← false positive!
```

`rateOfChange_1 a AggregationMechanism` lies outside E — a *semantically wrong* conclusion. This
is the most serious of the three cases (see "Technical significance" below).

**CASE 3 — Sound + Complete ($A = E$).** A full and correct rule set:

```
A = { rateOfChange_1 a ChangeMechanism, rateOfChange_1 a Mechanism } = E
```

Nothing extra, nothing missing — the algorithm returns exactly the consequence set.

### Technical Significance for a Knowledge System

- **Unsound is more dangerous than incomplete.** A wrong conclusion (false positive) *propagates*
  into every downstream query: if the system believes `rateOfChange_1` is an `AggregationMechanism`,
  it may return this mechanism for the question "which mechanisms aggregate multiple inputs?" — a
  wrong answer that looks valid. Incomplete only causes "no result" — the user can see that,
  whereas unsound produces a wrong result no one notices.
- **When forced to choose, prefer sound-not-complete for a KG.** A knowledge graph that answers
  "cannot derive" can be improved (add rules, add data); a KG that returns a false assertion
  destroys trust immediately.
- **Incompleteness is often a deliberate cost.** OWL RL trades completeness for the feasibility of
  rule-based reasoning (next subsection); the cost is *sparser answers*, the benefit is
  termination and running on an ordinary rule engine.
- **Empirical verification.** For a simple task like classification, CASE 1/3 can be verified by
  running forward chaining (a tool such as RDFLib) and comparing A against a hand-listed E — but
  for harder tasks, "complete" is a theoretical result (a theorem), not something measured by a
  test.

### OWL RL: Sound, with Conditional Completeness

OWL 2 RL is the profile designed to be compatible with rule-based reasoning
[@w3c-owl2-profiles]. W3C states the corresponding correspondence result as **Theorem PR1**
[@w3c-owl2-profiles, §4.3]:

For OWL 2 RL ontologies satisfying the profile's syntactic restrictions, forward chaining with the
OWL RL/RDF rule set returns *all and only* the correct answers for certain query types.

However, on **arbitrary RDF graphs**, completeness is not guaranteed: "it is no longer possible to
guarantee that all correct answers can be returned." Forward chaining remains sound — it only
returns valid entailments — but it may miss some.

The specific restrictions:

- OWL RL disallows `DisjointUnion`, `ReflexiveObjectProperty`
- Class expressions are limited per Table 2 of the spec
- Negation, complex existential quantification, and counting lie outside the reach of Horn rules

> ⚠ **Do NOT say:** "OWL RL forward chaining is complete for every RDF graph."
> **Do NOT say:** "OWL RL is complete for the RL rules" (tautological).
> **DO say:** "OWL RL forward chaining is sound; complete under the specific syntactic conditions
> stated in the W3C OWL 2 Profiles spec, Theorem PR1."

> 🖊 **Self-check:** Explain why a forward-chaining system using the OWL RL rules can miss some
> OWL 2 DL entailments. Give a concrete example of the kind of entailment a Horn rule cannot
> capture. (Hint: think about existential restrictions and unnamed witnesses.)

> **In practice.** OWL 2 RL is the profile that rule engines actually implement. **RDFox**
> [@rdfox] and **Apache Jena**'s GenericRuleReasoner [@apache-jena-rules] fire the OWL 2 RL/RDF
> rules by forward chaining; **OWL-RL** [@owlrl] ships the same rule set for RDFLib; and the W3C
> **RIF** suite [@w3c-rif-overview] standardizes the Datalog-compatible interchange these engines
> target. All of them inherit the qualified-completeness caveat of Theorem PR1: sound always,
> complete only under the profile's syntactic conditions.

## 5.14 Entailment Regime

The same RDF graph, under different entailment regimes, gives different results:

| Regime | Description | Inference strength |
|--------|-------|-----------------|
| Simple | Basic RDF only, no RDFS | Minimal |
| RDFS | Adds subClassOf, subPropertyOf, domain, range | Medium |
| OWL RL | Adds rule-engine-compatible OWL rules | High (within RL) |
| OWL Direct | Full Description Logic semantics (OWL 2 DL) | Highest (in DL) |
| OWL RDF-Based | Semantics directly on the RDF graph (OWL 2 Full) | Highest (undecidable) |

When you write "$G \models \alpha$", always ask: $\models$ under which regime?

### SPARQL and the Entailment Regime

Per SPARQL 1.1 Entailment Regimes [@w3c-sparql11-entailment], the entailment regime is specified
via the **SPARQL Service Description**, not via the `FROM` clause:

- `sd:defaultEntailmentRegime` — the endpoint's default regime
- `sd:entailmentRegime` — the regime for a specific named graph

The `FROM` clause in SPARQL selects the graph/dataset; it does **not** select the entailment
regime. These are two independent mechanisms.

The standard regime IRIs:

- RDF: `http://www.w3.org/ns/entailment/RDF`
- RDFS: `http://www.w3.org/ns/entailment/RDFS`
- OWL Direct: `http://www.w3.org/ns/entailment/OWL-Direct`
- OWL RDF-Based: `http://www.w3.org/ns/entailment/OWL-RDF-Based`

**A comparison example on the mechanism domain.** Same query, two entailment regimes, two
different results:

```sparql
PREFIX ex: <http://example.org/kgbook/mks#>
SELECT ?m WHERE { ?m a ex:Mechanism }
```

The source data contains `ex:rateOfChange_1 a ex:RateOfChangeMechanism` and
`ex:RateOfChangeMechanism rdfs:subClassOf ex:ChangeMechanism` and
`ex:ChangeMechanism rdfs:subClassOf ex:Mechanism`.

| Regime | Result | Explanation |
|--------|---------|------------|
| **Simple** | ∅ (empty) | Matches only an explicit `?m a ex:Mechanism` triple — nothing is typed directly as `ex:Mechanism` |
| **RDFS** | `rateOfChange_1`, `heatTransferRate_2`, `newtonCooling_1` | RDFS subClassOf infers RateOfChangeMechanism → ChangeMechanism → Mechanism |

This is a real illustration that, for the same SPARQL question, the choice of entailment regime
decides the result. If the regime is not specified, a developer may get ∅ and think "there are no
mechanisms in the graph" — when in fact there are 3 mechanisms, only RDFS reasoning has not been
enabled.

> ⚠ **Do NOT say:** "SPARQL engines usually default to X." Default behavior is
> implementation-dependent, not standardized. Always check the specific endpoint's Service
> Description.

## 5.15 OWL 2 DL and the Limits of Materialization

General OWL 2 DL reasoning cannot be understood simply as "repeatedly appending every entailed RDF
triple until no new triple appears." The reasons:

- **Existential semantics:** OWL 2 DL may require the existence of unnamed witnesses in models —
  individuals with no name in the RDF graph. These witnesses cannot be represented as a finite
  set of RDF triples.

- **Model structures:** The model structure of OWL 2 DL may not correspond to an explicitly
  materialized finite RDF graph.

- **Specialized algorithms:** Practical DL reasoners typically use tableau, hypertableau, or
  classification procedures — not naive triple closure.

> ⚠ **Lesson:** Formal entailment does NOT imply that finite RDF-triple materialization is always
> the correct computational model. For full OWL 2 DL, materializing the entire closure may be
> infeasible or semantically incorrect.

## 5.16 Horn Rules and SWRL

### Horn Rules in KGs

A Horn clause has the form:

$$\text{head} \leftarrow \text{body}_1 \land \text{body}_2 \land \dots \land \text{body}_n$$

In the KG context, the head and body are triple patterns with variables. For example:

$$\text{sisterCity}(y, x) \leftarrow \text{sisterCity}(x, y)$$

"If x is a sister city of y, then y is a sister city of x."

Horn rules have important properties:

- **Monotonic:** Adding information to the graph only extends the result set, never shrinks it
- **Terminating:** On a finite graph under the safety conditions (§5.2), forward chaining always terminates
- **Limited expressiveness:** Cannot express negation, disjunction in the head, or existential quantification in the head

The safe, function-free Horn rules of §5.2 are precisely **Datalog**; the survey *Datalog and
Recursive Query Processing* [@datalog-survey-2013] is the standard reference for their fixpoint
semantics and evaluation strategies.

### Datalog and Its Three Equivalent Semantics

Drop function symbols (function-free) and require every head variable to appear in the body
(**safeness** / range-restriction), and a Horn rule becomes a **Datalog** rule:

$$A \leftarrow B_1, \dots, B_n$$

where $A$ (the head) and each $B_i$ (the body) are atomic formulas $P(t_1, \dots, t_k)$.
Safeness guarantees each substitution only uses values already present in the graph, so forward
chaining terminates (§5.2).

Datalog has **three ways of defining "what program $P$ means over database $D$"**, and the
foundational theorem of Datalog theory says all three give **the same set of facts**
[@abiteboul-foundations-1995]:

1. **Model-theoretic semantics:** the meaning of $P$ is the **minimal Herbrand model**
   $\mathcal{M}(P)$ — the intersection of every Herbrand model that satisfies $P$ and contains
   $D$. (A *Herbrand model* is a truth assignment to all ground atoms under which every rule of
   $P$ holds.)
2. **Proof-theoretic semantics:** the set of every ground fact **derivable** by a finite proof
   tree (backward induction through the rules).
3. **Fixpoint semantics:** $\mathrm{lfp}(T_P)$ — exactly the forward-chaining closure of §5.2.

$$\mathcal{M}(P) \;=\; \{\text{derivable facts}\} \;=\; \mathrm{lfp}(T_P)$$

> ℹ **Why three that are one?** This is the Knaster–Tarski theorem combined with the Horn
> property: for monotone Horn rules, "true in the least model", "has a proof", and "reached by
> iterating $T_P$" coincide. This lets us *choose* the convenient angle: prove correctness with
> models, implement with the fixpoint, explain with proof trees.

**Complexity.** Datalog has **PTIME-complete data complexity** (fixed program, growing data)
and **EXPTIME-complete combined complexity** (program and data both varying)
[@abiteboul-foundations-1995]. The large gap between the two numbers explains why Datalog is
practical: once the rule set is fixed, inference cost is only polynomial in the data size.

### Classical Negation vs Negation as Failure (NAF)

Pure Horn/Datalog has **no negation**. The moment we want to say "there is no evidence for $q$,
so conclude $\neg q$", we face two fundamentally different kinds of negation:

| | Classical negation $\neg$ | Negation as Failure $\sim$ (`not`) |
|---|---|---|
| **World assumption** | Open (OWA) | Closed (CWA) |
| **When we conclude $\neg q$ / $\sim q$** | Requires a proof of $\neg q$ or a disjointness axiom | Merely because $q$ **cannot be proven** from the current data |
| **Monotonic?** | **Yes** — adding facts never retracts a conclusion | **No** — adding a fact can make $q$ provable, retracting $\sim q$ |

The **non-monotonicity** of NAF is a double-edged sword. It enables "if nothing says otherwise,
treat it as false" reasoning (very natural for database-style data), but it breaks the
uniqueness of the model. The classic example — a program that is **not stratified**:

$$p \leftarrow \text{not } q \qquad\qquad q \leftarrow \text{not } p$$

This program has **two** minimal models: $\{p\}$ and $\{q\}$. Which should a system pick? No
monotonic basis prefers one — the result depends on execution order, and the semantics becomes
ambiguous.

### Stratified Datalog

The standard remedy is **stratification**: partition the program's predicates into ordered
layers $P_1, \dots, P_n$ such that if a rule in stratum $i$ has a negated body atom
$\text{not } q$, then every rule defining $q$ must live in a **strictly lower** stratum $j < i$.
In other words: *never negate a predicate that is being defined at the same time or higher up.*

> ℹ **Theorem:** Every stratified Datalog program has a **unique minimal model** (the **perfect
> model**). We compute it by running the fixpoint of stratum 1, then stratum 2 (using stratum
> 1's settled result to evaluate `not`), ... up to stratum $n$. Because each stratum only
> negates *already-settled* predicates, non-monotonicity no longer causes ambiguity.

Stratification **is not always achievable** — the example $p \leftarrow \text{not } q,\; q
\leftarrow \text{not } p$ above has a negation cycle and cannot be stratified. Then one needs a
stronger semantics (stable models / answer set programming), outside this chapter's scope.

Back to SHACL: precisely because SHACL uses LCWA (§5.10) — a local form of NAF — it is
**non-monotonic**. The constraints `sh:minCount`, `sh:maxCount`, `sh:not` all interpret "not
found" as "does not exist", so adding data can flip the verdict. SHACL avoids the
$p \leftrightarrow q$ ambiguity because it **does not infer**: a shape only checks a settled
graph, never defining predicates recursively against each other.

### SWRL: Extending OWL with Rules

SWRL (Semantic Web Rule Language) extends OWL by allowing OWL class/property expressions in the
body and head of rules [@swrl-submission].

> ⚠ **SWRL is a W3C Member Submission (2004), NOT a W3C Recommendation.** It is a reference
> document, not a stable standard.

The core problem: **OWL DL + SWRL is generally undecidable**. The combination of expressive OWL
class expressions and Horn rules creates representational power beyond the decidability boundary
of Description Logic.

In practice, systems that use SWRL typically:
- Restrict the SWRL rules to preserve decidability
- Accept incompleteness (not deriving everything)
- Or switch to OWL RL (limited expressiveness but decidable)

### RIF: Rule Interchange Format

RIF (Rule Interchange Format) [@w3c-rif-core] is a W3C standard family for exchanging rules
between systems. The RIF Core Dialect defines definite Horn rules without function symbols
(= Datalog), with a safeness condition that guarantees forward chaining terminates.

> ℹ **SWRL and RIF are ecosystem context.** The reader should leave Chapter 5 understanding the
> rule-based inference mechanism, not memorizing the history of W3C rule-language projects. The
> focus is the mechanism, not the standards history.

## 5.17 SHACL 1.2: Current Development

> ℹ **Current Development**
>
> **Stable baseline:** the SHACL Recommendation, 2017 [@w3c-shacl]. This is the normative
> semantics taught in this chapter.
>
> **Emerging:** SHACL 1.2 Core, W3C Working Draft, 2026-08-03 [@w3c-shacl12-core]. This is a
> developing document, not yet stable. Do not teach features that exist only in the draft as if
> they were baseline.
>
> A notable direction: SHACL 1.2 extends and refines several constraint components and improves
> shape expressiveness. The specific details are out of scope for this chapter; readers who care
> should follow the Working Draft directly.

## 5.18 Bridge to the Mechanism KG

This chapter ran the entire inference and validation machinery on the Mechanism-KG data being
built. Four fully worked examples:

1. **Inference:** Forward chaining with the RDFS subClassOf rule on mechanism data —
   `ex:rateOfChange_1 a ex:RateOfChangeMechanism` → `a ex:ChangeMechanism` → `a ex:Mechanism`,
   with the substitution $\theta$ and the fixpoint (§5.2). The transitive rule for `ex:requires`
   (if A requires B and B requires C then A requires C) is a variant of the same mechanism.

2. **Validation:** The `CandidateMechanismShape` checks the minimal structure of a mechanism
   candidate (`hasOperation`, `hasInput`, `hasOutput`, `rdfs:label`) and produces the matching
   validation report (§5.6, §5.7). Every Mechanism must have at least one `ex:Operation`; every
   `ex:Condition` must link to at least one Mechanism — both are shapes of the same form.

   `Condition` is not an empty name: it is an individual attached to a mechanism via
   `ex:hasCondition`, for example:

   ```turtle
   ex:uniformEnv_1 a ex:Condition ;
       rdfs:label "uniform environment (T constant, h constant)" .
   ex:newtonCooling_1 ex:hasCondition ex:uniformEnv_1 .
   ```

   The corresponding shape checks that every `ex:hasCondition` value node is a SHACL instance of
   `ex:Condition` (`sh:path ex:hasCondition ; sh:class ex:Condition`).

3. **Two independent axes:** The 2×2 consistency-vs-validation example on mechanism data (a
   violated ontology disjointness that is still SHACL-conformant; a candidate missing its output
   that is OWL-consistent but SHACL-violating) (§5.9).

4. **Repair governance:** When SHACL reports a candidate missing `ex:hasOutput`, the candidate
   repairs (add from source evidence, add a placeholder, remove, change the shape) have different
   knowledge consequences; the decision belongs to domain governance, not to the engine (§5.12).

### Two-Stage Pipeline: Inference Then Validation

This running example can now be packaged into a complete **two-stage pipeline** on the
mechanism graph — exactly Architecture B from §5.11:

**Stage 1 — Inference (Datalog / Horn rules).** Run the three rules from §5.2 to materialize
derived properties and classification on `rateOfChange_1`:

$$\text{hasInput}(m, q) \leftarrow \text{hasApplication}(m, a) \land \text{differentiand}(a, q)$$

$$\text{hasReferenceVariable}(m, v) \leftarrow \text{hasApplication}(m, a) \land \text{withRespectTo}(a, v)$$

Result: `rateOfChange_1` gains the two edges `hasInput position_1` and `hasReferenceVariable
time_1`, and is then given `rdf:type RateOfChangeMechanism`.

**Stage 2 — Validation (SHACL).** A `sh:NodeShape` checks the *enriched* graph from Stage 1:

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

> ⚠ **Why the order "infer before validate" is critical.** If Stage 2 ran on the raw graph
> without Stage 1, the shape would report a **false violation**: `hasInput` and
> `hasReferenceVariable` were then only *implicit*, so `sh:minCount 1` would fire even though
> the data is semantically fine. Only after Stage 1 materializes those two edges does Stage 2 see
> them and produce the correct verdict. This is the practical instantiation of §5.11 (the
> effective validation graph depends on what has been inferred before validation).

> ⚠ **Design note:** When building a mechanism ontology, do not try to express everything with OWL
> axioms. Some constraints (minimum counts, datatypes, patterns) are better expressed with SHACL.
> Some inferences (transitive, symmetric) are better expressed with rules. Choose the right tool
> for the right purpose. Document clearly: the asserted graph, the inferred graph, the effective
> validation graph, and the entailment regime.

## 5.19 Common Misconceptions

### Misconception 1: "RDFS domain/range check the data"

**False.** RDFS domain/range are inference rules — they ADD rdf:type to the graph and reject no
triple. Checking data is SHACL's job.

### Misconception 2: "A SHACL shape infers new knowledge"

**False.** SHACL shapes only check existing data. They do not participate in RDFS/OWL entailment
and produce no new triples.

### Misconception 3: "Materialization = inference"

**False.** Materialization is an implementation strategy. Entailment is a semantic relation that
exists independently of any implementation.

### Misconception 4: "A reasoner is always complete"

**False.** Completeness depends on language + regime + task. OWL RL forward chaining is not
complete for full OWL 2 DL or arbitrary RDF. Always state the scope.

### Misconception 5: "Data conforming to SHACL = correct data"

**False.** Conformance only means the data matches the shapes. Data can conform yet be wrong in
content.

### Misconception 6: "A SHACL violation = wrong data"

**False.** A violation only means the data does not match the shapes. Data can be correct in
content yet not match the expected structure.

### Misconception 7: "Forward chaining always terminates"

**False.** Forward chaining is guaranteed to terminate only when the conditions hold: finite
graph, finite rules, function-free, safe variables, no unbounded fresh-term generation (§5.2).

### Misconception 8: "SWRL is a stable W3C standard"

**False.** SWRL is a Member Submission (2004), not a Recommendation. The combination OWL DL +
SWRL is generally undecidable.

### Misconception 9: "SHACL = OWL with a Closed World Assumption"

**False.** SHACL is a separate validation framework with its own semantics. Some constraints make
absence in the data graph meaningful, but SHACL is not simply OWL + CWA (§5.6).

### Misconception 10: "Monotonic means adding a condition to the body increases results"

**False.** Monotonic means adding *information to the graph* (the knowledge base) does not lose
old conclusions. Adding a condition to the body makes the rule harder to match and can reduce the
results (§5.2).

### Misconception 11: "sh:targetClass only matches an exact rdf:type triple"

**False.** sh:targetClass uses SHACL instance semantics, including subclass reasoning over
`rdfs:subClassOf*` (§5.6).

### Misconception 12: "The SPARQL FROM clause changes the entailment regime"

**False.** FROM selects the graph/dataset. The entailment regime is specified via the Service
Description [@w3c-sparql11-entailment] (§5.14).

## 5.20 Reflection Questions

1. ★ Explain the difference between inference and validation with a concrete example from the
   city/country domain.

2. ★★ Given an ontology with `Person ⊑ ∃hasName.xsd:string` and data containing `(Alice, rdf:type,
   Person)` but no `hasName` triple for Alice. (a) What does the OWL 2 DL entailment say? (b) What
   does a SHACL shape `sh:minCount 1` on `hasName` say? (c) How do the two answers differ, and
   why?

3. ★★ Design a set of SHACL shapes for the Mechanism ontology: every Mechanism must have at least
   one `ex:Operation`, every `ex:Operation` must link to exactly one Mechanism (via
   `ex:hasOperation`), and every `ex:Condition` must have an xsd:string description. Write the
   shapes in Turtle. Test your shapes on `ex:candidateRateOfChange_1` from §5.6 — does the
   candidate pass the `ex:Operation` shape? (Hint: look at `ex:hasOperation
   ex:derivativeOperation_1` in the data.)

4. ★★★ Compare forward chaining over RDFS and forward chaining over OWL RL on: (a) the rule set,
   (b) representational power, (c) soundness and completeness, (d) computational cost. When would
   you choose RDFS over OWL RL?

5. ★★★ A system uses OWL RL forward chaining to infer and SHACL to validate. Build an example in
   which: (a) the data is OWL-consistent but SHACL-violating, and (b) the data is OWL-inconsistent
   but SHACL-conformant. Explain why each case occurs.

### 5.20.1 Answer Key

**Question 1 (★).** Explain the difference between inference and validation with a concrete example from the city/country domain.

Consider an ontology with `capitalOf rdfs:domain City` and `capitalOf rdfs:range Country`, together with the data `Vietnam capitalOf Hanoi`. The **inference pipeline** (forward chaining, §5.2) applies the RDFS domain/range rules (§5.3) and *adds* to the graph: `Vietnam rdf:type City` and `Hanoi rdf:type Country`. It reports no error at all, even though the result is "absurd" relative to reality — because RDFS only applies semantics, it does not check expectations. The **validation pipeline** (SHACL, §5.6) goes the other way: a shape like `sh:class Country` on the path `capitalOf` will *check* the value node and, if `Hanoi` is not a Country in the supplied data, produce a violation in the validation report (§5.7) without adding any triple. Same vocabulary (class, property) but two opposite directions of effect: inference = adds information, validation = checks information (§5.1, §5.10).

Why: confusing the two pipelines is the most common source of design error — using `rdfs:domain` to "check" (it does not check) or using a shape to "infer" (it does not infer). Evidence: §5.1 (the two-pipeline table), §5.3 (domain/range add information, the Vietnam/Hanoi example), §5.6 (SHACL checks), §5.10 (shapes ≠ axioms).

**Question 2 (★★).** Given an ontology with `Person ⊑ ∃hasName.xsd:string` and data containing `(Alice, rdf:type, Person)` but no `hasName` triple for Alice. (a) What does the OWL 2 DL entailment say? (b) What does a SHACL shape `sh:minCount 1` on `hasName` say? (c) How do the two answers differ, and why?

(a) **OWL 2 DL:** the ontology is *consistent* and derives no new ground triple naming Alice's hasName. Under the Open World Assumption, the axiom only requires "in every model, Alice has a hasName-successor that is a string"; a model satisfies this by including an *unnamed witness* not present in the RDF graph (§5.10). No violation, no inconsistency. (b) **SHACL:** the shape `sh:targetClass ex:Person` + `sh:path ex:hasName ; sh:minCount 1` runs the §5.6 mechanism chain: focus node = Alice, path = hasName, value nodes = ∅ → `minCount 1` not satisfied → a ValidationResult of severity Violation, `sh:conforms false` (§5.7). (c) The difference: OWL talks about *every model* and forgives absence (an anonymous existential witness); SHACL talks about *one specific supplied data graph* and treats absence as a structural violation. Same requirement "must have a name", entirely different semantics (§5.10).

Why: this is exactly the "OWL existential vs SHACL minCount" pair the chapter uses as its strongest distinguishing example. Evidence: §5.9 (OWA vs data-check), §5.10 (existential restriction ≠ minCount), §5.6, §5.7.

**Question 3 (★★).** Design a set of SHACL shapes for the Mechanism ontology: every Mechanism must have at least one `ex:Operation`, every `ex:Operation` must link to exactly one Mechanism (via `ex:hasOperation`), and every `ex:Condition` must have an xsd:string description. Write the shapes in Turtle. Test your shapes on `ex:candidateRateOfChange_1` from §5.6 — does the candidate pass the `ex:Operation` shape?

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

The "exactly one Mechanism" constraint needs `sh:inversePath` because it counts how many Mechanisms point *into* each Operation, then `minCount 1`/`maxCount 1` force exactly one. **Testing on `ex:candidateRateOfChange_1`:** the §5.6 data has `ex:hasOperation ex:derivativeOperation_1`, so *if* `MechanismShape` applied to it, the `hasOperation minCount 1` constraint would **pass** (there is exactly one value node). But two caveats: (i) `MechanismShape` targets `ex:Mechanism`, while the candidate is an `ex:CandidateMechanism`; under SHACL instance semantics (§5.6) it is only targeted if `CandidateMechanism rdfs:subClassOf Mechanism` is present in the data graph — the chapter does not declare this link, so the candidate is best checked by `CandidateMechanismShape` (§5.6), which still fails for the missing `hasOutput`. (ii) The `OperationShape` inverse side: `derivativeOperation_1` is referenced by exactly one `hasOperation` triple → passes minCount/maxCount.

Why: pass/fail must be read through the exact 6-step target→result chain, not guessed. Evidence: §5.6 (mechanism, CandidateMechanismShape), §5.7 (report), §5.18 (Condition/hasOperation).

**Question 4 (★★★).** Compare forward chaining over RDFS and forward chaining over OWL RL on: (a) the rule set, (b) representational power, (c) soundness and completeness, (d) computational cost. When would you choose RDFS over OWL RL?

(a) **Rule set:** RDFS uses a small set — subClassOf (rdfs9), subPropertyOf (rdfs7), domain (rdfs2), range (rdfs3) (§5.3). OWL RL uses a much larger set, covering the Horn-compatible OWL axioms, including contradiction-detection rules such as `cax-dw` for `owl:disjointWith` (§5.13, §5.16). (b) **Representational power:** RDFS expresses only class/property hierarchies and domain/range; OWL RL adds class expressions per the profile's Table 2, but still forbids `DisjointUnion`, `ReflexiveObjectProperty` and lies beyond the reach of negation/counting/complex existential quantification (§5.13). (c) **Soundness/Completeness:** both are *sound*. RDFS naive closure is *not complete* on standard RDF syntax (it needs generalized RDF, §5.3). OWL RL is complete only *conditionally* — under the profile's syntactic restrictions (Theorem PR1), not on arbitrary RDF graphs (§5.13). (d) **Cost:** OWL RL has more rules → a larger closure, more expensive computation; RDFS is cheaper and more stable to materialize (§5.4). **Choose RDFS when** you only need type-hierarchy inference (classification via subClassOf/domain/range), the data is large, you need cheap and controllable materialization, and you do not require OWL-level entailments.

Why: forward chaining is an algorithm; the result depends on the rule set and regime (§5.2, §5.14). Evidence: §5.3, §5.4, §5.13, §5.14, §5.15.

**Question 5 (★★★).** A system uses OWL RL forward chaining to infer and SHACL to validate. Build an example in which: (a) the data is OWL-consistent but SHACL-violating, and (b) the data is OWL-inconsistent but SHACL-conformant. Explain why each case occurs.

(a) **OWL-consistent, SHACL-violating.** The ontology has no axiom forcing `hasOutput`. Data: `ex:m1 a ex:Mechanism`. OWL RL forward chaining derives nothing contradictory (OWA allows m1 to *possibly* have an output in another model, §5.9/§5.10) → consistent. But `MechanismShape` with `sh:path ex:hasOutput ; sh:minCount 1` (§5.6) sees value nodes = ∅ on the supplied graph → violation, `sh:conforms false` (§5.7). It happens because OWL does not treat absence as an error, while SHACL checks that very graph.

(b) **OWL-inconsistent, SHACL-conformant.** Ontology: `ex:ChangeMechanism owl:disjointWith ex:AggregationMechanism`. Data: `ex:x9 a ex:ChangeMechanism ; a ex:AggregationMechanism ; ex:hasOperation ex:op1 ; rdfs:label "x9"`. OWL RL forward chaining applies the `cax-dw` rule (verified in the OWL 2 RL/RDF rules: two rdf:type of two disjoint classes → `false`) → inconsistent. SHACL only has a shape checking structure (has `hasOperation`, has a label) → every constraint satisfied → `sh:conforms true`, because "SHACL does not read `owl:disjointWith`" (§5.9).

Why: consistency and conformance are two independent axes — knowing one does not imply the other (§5.9, §5.10). Evidence: §5.9 (2×2), §5.10 (shapes ≠ axioms), §5.13 (OWL RL rules), §5.6.

## 5.21 What We Now Know

This chapter established the core distinction between the two pipelines and the foundational
mechanisms:

- **Inference:** From data + semantics → new knowledge. Forward chaining uses the substitution
  $\theta$ to connect abstract rules to concrete data. The fixpoint is the stopping condition.
  RDFS rules add information (they do not check). Materialization is an implementation strategy,
  not inference itself. Backward reasoning is an alternative strategy.

- **Validation:** From data + shapes → a conformance/violation report. The SHACL mechanism:
  target → focus node → path → value node → constraint → result. Shapes ≠ axioms.
  Conformance ≠ truth. Violation ≠ repair. Consistency ≠ validation (two independent axes).

- **Evaluation:** Soundness ($A \subseteq E$) and completeness ($E \subseteq A$) always need three
  components: language + regime + task. OWL RL is sound but conditionally complete.

- **Engineering:** The effective validation graph is an architectural decision. Repair is a
  decision problem. Asserted ≠ derived.

## 5.22 What We Still Cannot Do

This chapter taught the inference and validation mechanisms, but has not yet addressed the
questions:

- **Where does knowledge come from?** Inference only produces new knowledge from old knowledge.
  But where does the initial knowledge come from? How do we collect, extract, and integrate
  knowledge from many sources? (Chapter 7)
- **What when two sources conflict?** Inference assumes consistent data. But in reality, different
  knowledge sources can make contradictory claims. How do we handle contradiction? Who has the
  authority to decide a repair? (Chapter 6)
- **How do we reason when knowledge is uncertain?** Forward chaining and SHACL both work with
  binary knowledge (true/false). But much real-world knowledge is probabilistic or inductive.
  (Chapter 8)

The next chapter begins to address the question of claims, evidence, provenance, and contradiction
— the Context layer in Mental Model 1.

## 5.23 Mechanism Knowledge System — Capabilities Achieved

**BEFORE THIS CHAPTER** — the system had an OWL ontology (Chapter 4) with the concepts of
interpretation, model, entailment, OWA, consistency. But the ontology was a *static assertion*: no
mechanism to compute consequences, no way to check whether data conformed to expectations, no
repair strategy.

**AFTER THIS CHAPTER** — the system has two complete pipelines:
- **Inference:** Forward chaining with the substitution $\theta$ and the fixpoint on mechanism data
  (§5.2). RDFS rules applied to the mechanism taxonomy (§5.3). Materialization as an
  implementation strategy, not inference itself (§5.4).
- **Validation:** SHACL shapes checking `CandidateMechanism` (§5.6), a structured validation report
  (§5.7). The ability to distinguish conformance ≠ truth, consistency ≠ validation (§5.9).
  Shapes ≠ axioms ≠ rules (§5.10).
- **Repair:** Graph repair as a decision problem, grounded in domain governance (§5.12).
- **Evaluation:** Soundness and completeness are only meaningful within language + regime + task
  (§5.13). The same SPARQL query on mechanism data returns different results under the Simple and
  RDFS regimes (§5.14).

**THE CONCRETE RATE_OF_CHANGE EXAMPLE** — forward chaining derives `ex:rateOfChange_1 a
ex:Mechanism` from `a ex:RateOfChangeMechanism` via two subClassOf steps (§5.2). A SHACL shape
checks that `ex:candidateRateOfChange_1` lacks `ex:hasOutput` and reports a violation (§5.6,
§5.7). The 2×2 two-axis case on mechanism data: a disjoint ontology that is inconsistent yet
SHACL-conformant (§5.9). The SPARQL Simple regime returns ∅, the RDFS regime returns 3 mechanisms
(§5.14).

**STILL UNRESOLVED** — inference and validation assume the input data is already prepared. The
questions "where does knowledge come from?", "what when two sources conflict?", "who has the
authority to decide a repair?" remain unanswered. Chapter 6 opens the next level: *claims,
evidence, provenance, and time*.

## Terms Encountered in This Chapter

| Term | Short meaning | Taught in |
|-----------|-----------|--------------|
| Forward Chaining | Apply rules repeatedly until a fixpoint | §5.2 |
| Substitution $\theta$ | Map variables to concrete values; a ground fact is the result | §5.2 |
| Grounding | Make an abstract rule concrete via substitution | §5.2 |
| Fixpoint | $G_{n+1} = G_n$: no new triple is produced | §5.2 |
| Closure | The graph containing every computed consequence | §5.2 |
| Monotonicity | Adding knowledge does not lose old conclusions | §5.2 |
| RDFS Entailment Rules | Inference rules that add information, not check it | §5.3 |
| Materialization | A strategy that precomputes the closure and stores the results | §5.4 |
| Query-time inference | A lazy strategy that computes when a query arrives | §5.4 |
| Backward Chaining | Start from the question, find a proof | §5.5 |
| SHACL Shape | Describes a data-checking condition | §5.6 |
| Focus Node / Value Node | The node being evaluated / the target nodes reached via a path | §5.6 |
| Validation Report | The validation result report (conforms/violation) | §5.7 |
| Conformance | Data matches the shapes ≠ data is correct | §5.8 |
| Consistency | An OWL model exists ≠ SHACL conformant | §5.9 |
| Soundness | Every derived result is semantically correct | §5.13 |
| Completeness | Every semantic consequence is derived | §5.13 |
| Effective Validation Graph | The graph the validator actually sees | §5.11 |
| Entailment Regime | Determines the inference strength at query time | §5.14 |
| Graph Repair | Deciding whether to fix the data or the shape, based on governance | §5.12 |
| Ground Triple (fact) | A triple with no variables, ready in the graph | §5.2 |
| Immediate consequence operator $T_P$ | $T_P(I)$ = every ground head whose body matches in $I$ | §5.2 |
| Fixed-point semantics | Program meaning = $\mathrm{lfp}(T_P)$ (Knaster–Tarski) | §5.2 |
| Minimal Herbrand Model | $\mathcal{M}(P)$ = intersection of all Herbrand models satisfying $P$ and containing $D$ | §5.16 |
| Datalog | Function-free, safe Horn rules; three equivalent semantics | §5.16 |
| Classical negation vs NAF ($\neg$ vs $\sim$) | $\neg$ under OWA (monotonic) vs `not` under CWA (non-monotonic) | §5.16 |
| Stratified Datalog | Lower strata settle first; yields a unique perfect model | §5.16 |
| Local Closed-World Semantics (LCWA) | SHACL: absence in the graph = non-existence for a focus node | §5.10 |
| RETE algorithm | Alpha/beta network caching intermediate matches; memory for speed | §5.5 |
| Alpha / Beta network | Filter within one pattern / join bindings across patterns | §5.5 |

## Further Reading

- SHACL W3C Recommendation [@w3c-shacl] — the full definition of shapes and validation.
- SPARQL 1.1 Entailment Regimes [@w3c-sparql11-entailment] — entailment regimes in SPARQL.
- RDF 1.1 Semantics [@w3c-rdf11-mt] — the model-theoretic semantics of RDFS.
- Hogan et al., *Knowledge Graphs*, Chapter 7: Inductive Knowledge [@hogan-knowledge-graphs] — inductive and probabilistic inference.
- OWL 2 RL [@w3c-owl2-profiles] — the OWL RL profile and the forward-chaining mechanism.
- OWL 2 Direct Semantics [@w3c-owl2-direct-semantics] — OWL 2 semantics for soundness/completeness.
- Abiteboul, Hull & Vianu, *Foundations of Databases* [@abiteboul-foundations-1995] — the canonical source for Datalog, its three semantics, and complexity.
- Forgy, *Rete: A Fast Algorithm for the Many Pattern/Many Object Pattern Match Problem* [@forgy-rete-1982] — the original RETE algorithm.
- Motik et al., *Parallel Materialisation of Datalog Programs in Centralised, Main-Memory RDF Systems* [@motik-rdfox-2014] — parallel Datalog materialization (RDFox).
