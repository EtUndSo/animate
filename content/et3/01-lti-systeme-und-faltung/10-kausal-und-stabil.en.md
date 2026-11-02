---
title: Stage 9: Causal and stable
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / LTI Systems and Convolution
order: 3211000
summary: Two properties that every real system should have can be read directly from h(t) .
tags: causal, stable
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
Two properties that every real system should have can be read directly from $h(t)$.
:::

:::definition Definition 9.1 (Causal, stable)
<span class="anker" id="satz-9-1"></span>

A system is called __causal__ if the output does not begin before the input. For an LTI system this means

<span class="anker" id="gl-9-1"></span>
$$h(t)=0\quad\text{for }t<0. \tag{9.1}$$

A system is called __stable__ (more precisely, BIBO stable, *bounded input, bounded output*) if it responds to every bounded input $|s(t)|\le A<\infty$ with a bounded output.
:::

Causal: an impulse at time 0 cannot have any effect before that time. In the convolution, only impulses from the past then contribute, $g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$.

:::satz Theorem 9.2 (Stability condition)
<span class="anker" id="satz-9-2"></span>

An LTI system is stable if and only if its impulse response is absolutely integrable:

<span class="anker" id="gl-9-2"></span>
$$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty. \tag{9.2}$$
:::

:::herleitung Stability condition
⁠**Sufficient.** With the triangle inequality for integrals and $|s|\le A$:

$$|g(t)|=\Bigl|\int h(\tau)\,s(t-\tau)\,\mathrm{d}\tau\Bigr|\le\int|h(\tau)|\,|s(t-\tau)|\,\mathrm{d}\tau\le A\int|h(\tau)|\,\mathrm{d}\tau.$$

If the integral is finite, $g$ is bounded.

⁠**Necessary.** If $\int|h|=\infty$, choose the least favorable bounded input: $s(t_1-\tau)=\operatorname{sign}h(\tau)$, that is, always $\pm1$ with the sign of $h$. Then $g(t_1)=\int|h(\tau)|\,\mathrm{d}\tau=\infty$, although $|s|\le1$.
:::

Examples: the RC circuit has $\int|h|=1$ and is stable. The ideal delay element ($\int|\delta(t-t_0)|\mathrm{d} t=1$) is stable. The integrator has $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$ and is unstable: it responds to the bounded step with the unbounded ramp $t\,\varepsilon(t)$.

:::aufgabe Exercise 10 ★★ Causal? Stable?
<span class="anker" id="aufg-10"></span>

Examine (a) $h(t)=\mathrm{e}^{-2t}\varepsilon(t)$, (b) $h(t)=\mathrm{e}^{t}\varepsilon(t)$, (c) $h(t)=\varepsilon(t)-\varepsilon(t-1)$, (d) $h(t)=\mathrm{e}^{-|t|}$, (e) $h(t)=\delta(t+1)$. For each unstable system, give a bounded input that produces an unbounded output.

:::loesung
(a) Causal, $\int|h|=\tfrac12$: stable.

(b) Causal, $\int_0^\infty\mathrm{e}^t\mathrm{d} t=\infty$: unstable. The step $\varepsilon(t)$ produces $\int_0^t\mathrm{e}^\tau\mathrm{d}\tau=\mathrm{e}^t-1$, which is unbounded.

(c) Causal, $\int|h|=1$: stable. The system forms the integral of the input over the last second (sliding window).

(d) Not causal, because $h(t)\neq0$ for $t<0$. $\int\mathrm{e}^{-|t|}\mathrm{d} t=2$: stable.

(e) $\delta(t+1)$ acts at $t=-1<0$: $g(t)=s(t+1)$; the system “sees” the input one second in advance. Not causal, but stable ($\int|h|=1$).
:::
:::
