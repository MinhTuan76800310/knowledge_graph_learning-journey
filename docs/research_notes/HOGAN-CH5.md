# HOGAN-CH5: Knowledge Graphs — Deductive Knowledge (Rules & Reasoning Sections)

- **URL:** https://kgbook.org/#sec-rules (Section 4.2.1) and https://kgbook.org/#ssec-reasoning (Section 4.2)
- **Status:** FETCHED_AND_VERIFIED
- **Fetched:** 2026-08-29, via GitHub source (raw.githubusercontent.com/Knowledge-Graphs-Book/HTML-Book/main/chapters/04-deductive.php)
- **Used in:** Chapter 5
- **Document status:** Academic textbook (Springer 2021), open full text
- **Note:** This supplements HOGAN-CH6.md which covers the broader Ch4 overview. This note focuses specifically on the rules/reasoning sections needed for Ch5.

## Key Findings: Forward Chaining & Fixpoint Algorithm

### Formal Rule Definition
A rule is formally defined as a pair R := (B, H) where B is the body (graph pattern) and H is the head (graph pattern). Applying the rule means replacing body variables with graph terms and deriving the corresponding head. The head must use a subset of variables appearing in the body (safety condition).

These correspond to positive Datalog in databases and Horn clauses in logic programming.

### Materialization and Fixpoint Computation
**This is the primary source for the fixpoint algorithm taught in Ch5.**

Rule application is formally defined as:

```
R(G) := ⋃_{μ ∈ B(G)} μ(H)
```

where B(G) is the set of matches of the body pattern in graph G, and μ(H) applies the substitution to the head.

Then the one-step closure:
```
R⁺(G) := R(G) ∪ G
```

Recursive application:
```
R^k(G) = R⁺(R^{k-1}(G))
```

The least model (materialization):
```
R*(G) := ⋃_{k∈ℕ} R^k(G)
```

**Fixpoint reached when:** R^{k'}(G) = R^{k'+1}(G) — i.e., no new facts can be derived.

This is exactly the G_{i+1} = G_i ∪ consequences(G_i) formulation used in Ch5 teaching.

### Correctness and Completeness
Hogan defines these precisely for rule sets relative to semantic conditions Φ:

- **Correct (sound):** G ⊨_Φ R*(G) — everything derived by the rules is entailed
- **Complete:** No graph G' ⊈ R*(G) is entailed by G — everything entailed can be derived

**Critical finding:** The RDFS-style rules presented are correct but INCOMPLETE. OWL 2 RL/RDF rules are also incomplete for negation, existentials, universals, and counting.

This directly supports the Ch5 teaching point: "Soundness/completeness must specify language/profile + entailment regime + reasoning task."

### Materialization Caveats
- Materialization can be unfeasibly large (exponential blowup)
- Rules incomplete for negation
- Not all OWL features capturable by rules
- Optimizations include Rete networks and distributed frameworks (MapReduce)

### Alternative Reasoning Strategies
- **Query rewriting:** Extends input query to capture entailed answers; OWL 2 QL designed for this
- **Tableau methods (Description Logics):** Reduce entailment to satisfiability checking; extend models like materialization but branch on disjunction and introduce new elements for existentials

## Teaching Relevance for Ch5

### Primary Source For
1. **Forward chaining fixpoint algorithm** — the formal G_{i+1} = G_i ∪ consequences(G_i) definition
2. **Termination condition** — fixpoint when no new facts derivable
3. **Soundness/completeness definitions** — precise mathematical formulation
4. **Why completeness fails** — negation, existentials, counting cannot be captured by forward chaining alone
5. **Materialization feasibility** — when it works, when it doesn't

### Two Pipelines Distinction
Hogan's treatment supports the INFERENCE vs VALIDATION distinction:
- Rules/materialization → inference pipeline (what follows?)
- Tableau/satisfiability → can serve both inference and consistency checking
- Neither is validation in the SHACL sense

### Connection to OWL RL
The incompleteness results for OWL 2 RL/RDF rules directly connect to OWL-RL-SPEC findings. Hogan confirms: RL rules applied to arbitrary RDF graphs cannot guarantee completeness, though they remain sound.

## Safe Simplifications
- Using the simplified notation G_{i+1} = G_i ∪ consequences(G_i) instead of the full R^k(G) formalism is pedagogically safe.
- Saying "forward chaining computes the least model" is safe for Datalog/Horn clause contexts.
- Omitting Rete algorithm details is safe.

## Dangerous Simplifications
- Saying "materialization always terminates" — it doesn't for unrestricted rule sets.
- Saying "rules are complete for OWL reasoning" — they aren't, even for RL profile on arbitrary RDF.
- Conflating correctness with completeness.
- Implying tableau and materialization are interchangeable approaches.

## What This Source Does NOT Justify
- Specific OWL 2 RL rule tables (use OWL-RL-SPEC / OWL-05).
- SHACL validation semantics (use SH-01).
- SWRL-specific syntax or decidability results (use SWRL-01).
- RIF interchange format details (use RIF-01).
