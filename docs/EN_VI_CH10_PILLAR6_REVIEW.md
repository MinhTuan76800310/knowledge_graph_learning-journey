# Reviewer Brief — v0.3 Pillar 6: Chapter 10 Upgrade & Full English Edition (VI + EN)

**Branch:** `en-vi-ch10-pillar6`
**Issue:** #79
**Date:** 2026-09-07
**Scope:** Final theoretical pillar of `docs/BOOK_V0_3_MILESTONE.md` (Target 6 / P6 —
System Dynamics & Closed-Loop Stability). Deepens the Vietnamese Chapter 10 with two
research-grade mathematical subsections and produces the complete English edition of
Chapter 10 at 100% structural/pedagogical/conceptual parity.

---

## 1. What changed, at a glance

| Area | File(s) | Nature |
|------|---------|--------|
| VI deepening | `book/chapter10.md` | +§10.20.1 (closed-loop control), +§10.35.1 (knowledge entropy), +4 terms rows |
| EN edition | `book-en/chapter10.md` | **new file** — full translation of all 66 H2 sections + 2 new subsections |
| Source | `book/references.bib` | +`wiener-cybernetics-1948` (WIENER-01) |
| Citation map | `docs/CITATION_MAP.md` | +WIENER-01 row |
| Concepts | `book/concept_registry.yaml` | +4 concepts (54 → 58) |
| Glossary | `book/glossary.md` | +4 terms (45 → 49) |
| Figures | `book/figures/tikz/ch10-{closed-loop-stability,knowledge-entropy-collapse}.tex` | 2 new VI TikZ |
| EN figures | `book-en/figures/tikz/ch10-*.tex` | 11 EN mirrors (9 existing + 2 new) |
| Tests | `tests/test_chapter10_integrity.py` | counts bumped to 58/16/11/49 |
| Wiring | `book-en/book-manifest.yaml`, `scripts/verify_book_pdf.sh` | EN chapter registered |
| Status | `docs/BOOK_STATUS.md` | Pillar 5 → MERGED, Pillar 6 → in PR |

---

## 2. Deliverable A — §10.20.1 Closed-Loop Control Theory & Belief Oscillation

**Anchors:** VI `book/chapter10.md:520–562` · EN `book-en/chapter10.md:520–562` (identical).
Extends §10.20 (feedback-loop safety properties) with its mathematical foundation.

**Claims to scrutinize (verify each):**

1. **Open-loop transfer** $L(s) = G(s)\,H(s)\,e^{-s\,\tau_{\text{verify}}}$ — $G$ = ingestion/
   assessment dynamics, $H$ = Ledger feedback, $e^{-s\tau}$ = pure transport delay.
2. **Delay erodes phase, not amplitude:** $|e^{-j\omega\tau}| = 1$ (magnitude unchanged) but
   phase is subtracted by $\omega\tau$ radians — worst at high frequency. Instability when
   total phase hits $-180°$ at gain crossover with amplitude $\ge 1$.
3. **Stability criterion (the load-bearing result):** for the delay differential equation
   $\dot{x}(t) = -a\,x(t-\tau)$, the solution converges asymptatically **iff** $a\,\tau < \pi/2$.
   *Reviewer check:* substitute $s = j\omega$; real part $a\cos(\omega\tau)=0 \Rightarrow \omega\tau=\pi/2$;
   imaginary part gives $\omega = a\sin(\omega\tau) = a$; boundary is $a\tau = \pi/2$. Beyond it →
   Hopf branch → sustained **limit cycle** (`Accepted ↔ Contested ↔ Retracted` never settles).
4. **Lyapunov:** $V(\mathbf{b}) = \lVert\mathbf{b}-\mathbf{b}^*\rVert^2$ positive definite;
   asymptotic stability iff $\dot V < 0$ along trajectories; $a\tau<\pi/2$ is exactly the
   $\dot V<0$ condition for one coordinate.
5. **Safeguards** (all keep $\dot V<0$): low-pass filter (restore phase margin), ingestion rate
   limiting (lower $\omega_{gc}$ → widen $\tau_{\max}$), hysteresis band (kill relay oscillation).
6. **Boundary:** belief oscillation ≠ "learning" — a limit cycle is $V$ failing to decrease, a
   control failure, not progress.

**Running example:** `VibrationVelocityRateOfChange` — slow verification ($\tau$=3 days for sensor
recalibration) + high gain → $a\tau>\pi/2$ → oscillation; fixed by ±15% hysteresis + low-pass +
per-shift cap.

**Source:** Wiener [@wiener-cybernetics-1948] (WIENER-01) — feedback with delay is the origin of
oscillation.

---

## 3. Deliverable B — §10.35.1 Knowledge Entropy ($H_K$) & Autophagous Model Collapse

**Anchors:** VI `book/chapter10.md:885–923` · EN `book-en/chapter10.md:885–923` (identical).
Extends §10.35 (model collapse in words) with its mathematical form and a structural
distinction from §10.34 feedback collapse.

**Claims to scrutinize:**

1. **Knowledge entropy** $H_K(t) = -\sum_{c \in \mathcal{C}} p_t(c)\,\log p_t(c)$ — diversity of
   the concept-class distribution; high = many classes co-present, low = contraction to head classes.
2. **Autophagous collapse (the load-bearing result):** recursive refit on $M$ synthetic samples
   shrinks variance by factor $(1-1/M)$ each generation:
   $\sigma_{t+1}^2 = \sigma_t^2(1-\tfrac{1}{M}) < \sigma_t^2 \Rightarrow \sigma_t^2 = \sigma_0^2(1-\tfrac{1}{M})^t \to 0$.
   *Reviewer check:* the factor is Bessel's correction — the $1/M$-normalised variance estimator
   has expectation $\sigma^2(M-1)/M = \sigma^2(1-1/M)$. Repeated → collapse to a point, $H_K$ minimal.
3. **Tail extinction:** rare class with $p(c)<\epsilon$ has expected count $M\,p(c)$; when
   $M\,p(c)\ll 1$, $P(\text{absent}) \approx e^{-M p(c)} \to 1$. Once absent it cannot regenerate
   → $p_t(c)\to 0$ exponentially; head classes falsely inflated (reclaim tail mass).
4. **Structural distinction table** (feedback vs autophagous collapse): object / mechanism /
   symptom / remedy differ — one is a **control** failure of a loop, the other a **population-level**
   failure of the whole distribution. Fixing one does not fix the other.
5. **Boundary:** autophagous collapse ≠ feedback collapse (§10.34).

**Running example:** rare *quantum transition rate* / *boundary-layer velocity gradient* mechanisms
vanish when GraphRAG summaries are re-ingested without fresh measurements; only generic textbook
derivatives survive — the irreversible-defect pattern.

**Source:** Shumailov et al. [@shumailov-collapse-2024] (COLLAPSE-01, already registered).

---

## 4. Figures

- **`ch10-closed-loop-stability`** (VI + EN): block diagram of the delayed loop
  $L(s)=G(s)H(s)e^{-s\tau}$ + two step responses — stable ($a\tau<\pi/2$, $\dot V<0$) vs limit
  cycle ($a\tau>\pi/2$, `Accepted↔Retracted`). Grayscale-safe (color **and** text labels).
- **`ch10-knowledge-entropy-collapse`** (VI + EN): distribution narrowing across $t{=}0,1,2$
  (peaks **rise** 1.25→1.55→1.85 as variance shrinks at fixed mass — reviewer: confirm this is
  the physically correct direction) + $H_K(t)$ monotonic decline. Tail-extinction arrows annotated.
- 11 EN figure mirrors total (9 pre-existing ch10 figures translated + the 2 new).

---

## 5. Bilingual parity metrics (mechanically verified)

| Metric | VI | EN | Parity |
|--------|----|----|--------|
| Lines | 1584 | 1580 | ±4 (paragraph wrap only) |
| H2 sections | 66 | 66 | ✅ exact |
| H3 sections | 1 | 1 | ✅ exact |
| Unique citekeys | 16 | 16 | ✅ **identical set** |
| Figure embeds | 11 | 11 | ✅ **identical paths** |
| §10.20.1 anchor | 520 | 520 | ✅ |
| §10.35.1 anchor | 885 | 885 | ✅ |
| New terms rows | 4 | 4 | ✅ (VI Vietnamese gloss / EN English gloss) |
| Vietnamese leakage in EN | — | 0 | ✅ (only Δ/π/τ Greek math) |

The 4-line delta is paragraph-wrapping in the body; every structural count (H2/H3/citekeys/
figures) is identical and the new subsections land on the same line numbers.

---

## 6. Verification gates

| Gate | Command | Result |
|------|---------|--------|
| Unit tests | `python -m pytest` | 106 passed (incl. ch10 integrity 58/16/11/49) |
| Lint | `python -m ruff check .` | clean |
| Format | `python -m ruff format --check .` | clean |
| VI build | `bash scripts/build_book.sh` | exit 0 |
| VI verify | `bash scripts/verify_book_pdf.sh` | **GATE PASSED — 434 pages** (≥431) |
| EN build | `LANG=en bash scripts/build_book.sh` | exit 0 |
| EN verify | `LANG=en bash scripts/verify_book_pdf.sh` | **GATE PASSED — 412 pages** (≥376) |

---

## 7. Reviewer focus — where to spend attention

1. **The two stability results** (§2.3 DDE $a\tau<\pi/2$; §3.2 variance $(1-1/M)$) are the
   pillar's spine — both were re-derived analytically before committing; confirm the prose
   states the hypotheses (single coordinate, saturation, fixed mass) honestly and does not
   overclaim generality.
2. **Voice consistency:** the new VI subsections are written in Ch10's native terse register
   (bullets, `**Ví dụ RATE_OF_CHANGE:**`, `≠` boundary lines, `> **Tiêu chuẩn ổn định:**`
   callout) — Ch10 uses **no** `**Formal meaning:**` scaffolding (that is Ch9-only). Do not
   "fix" this toward Ch9 style.
3. **Terms-table shape:** VI ch10 is a 2-column `English | Vietnamese` table (unlike ch8/ch9's
   3-column); the EN edition renders `| Term | Short meaning |` with English glosses to honor
   the zero-Vietnamese rule. This asymmetry is intentional.
4. **Figure 2 peak direction:** rising peaks under shrinking variance — confirm not inverted.
5. **AGENTS.md** carries pre-existing uncommitted edits **not** part of this task; it is
   deliberately excluded from the commit.
