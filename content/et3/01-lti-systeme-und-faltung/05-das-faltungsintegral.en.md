---
title: Stage 4: The convolution integral
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / LTI Systems and Convolution
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Chapter 1: LTI Systems and Convolution
order: 3210500
summary: With linearity and time invariance, the response to any signal can be computed from the response to a single short pulse.
tags: Dirac impulse, impulse response
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
With linearity and time invariance, the response to *any* signal can be computed from the response to a single short pulse. The result is the convolution integral.
:::

**The idea in four steps.**

<ol>

<li>

⁠**Decompose.** Approximate the input signal by a staircase of narrow rectangles of width $T_0$. The building block is a rectangle $s_0(t)$ of duration $T_0$ and height $1/T_0$, that is, of area 1. The stair step at $nT_0$ is this building block, shifted by $nT_0$ and weighted with $s(nT_0)\,T_0$, the area of the strip:

$$s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0.$$

</li>

<li>

⁠**Send one building block through the system.** The system responds to $s_0$ with $g_0(t)$. This has to be known once.

</li>

<li>

⁠**Reassemble.** Time invariance: the shifted building block produces the shifted response. Linearity: weights and sum carry through. Hence

$$g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t).$$

</li>

<li>

⁠**Limit $T_0\to0$.** The staircase becomes the signal. The rectangle of area 1 becomes the __Dirac impulse__ $\delta(t)$, an infinitely short impulse of area 1. Its response is called the __impulse response__ $h(t)$. $nT_0$ becomes the continuous variable $\tau$, $T_0$ becomes the differential $\mathrm{d}\tau$, and the sums become integrals.

</li>

</ol>

:::abbildung et3/k1treppe 5
Top: a triangular pulse $s(t)=\Lambda(t-1)$ and its staircase approximation with $T_0=0.5$ s. Bottom: the exact response of the RC circuit and the sum of the shifted rectangle responses. The largest deviation falls from 0.17 ($T_0=0.5$ s) to 0.08 ($0.25$ s) and 0.03 ($0.1$ s).
:::

:::satz Theorem 4.1 (Convolution integral)
<span class="anker" id="satz-4-1"></span>

Every signal $s(t)$ satisfies

<span class="anker" id="gl-4-1"></span>
$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau, \tag{4.1}$$

and an LTI system with the impulse response $h(t)$ responds to it with

<span class="anker" id="gl-4-2"></span>
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau. \tag{4.2}$$
:::

⁠**How to read it:** $\tau$ is the instant of an input impulse, and $s(\tau)\,\mathrm{d}\tau$ is its weight (the area of the strip). $h(t-\tau)$ is the response of the system at time $t$ to an impulse that arrived at time $\tau$, that is, $t-\tau$ seconds ago. The output collects all impulses of the past, each weighted by how strongly the system still “remembers” it after that time. The equation is exact and holds for every LTI system.

⁠**In short:** the output of an LTI system is the superposition of its impulse responses, shifted to every instant of the input and weighted by the input there.

:::frage Why must the rectangular building blocks have area 1?
So that the response to the building block keeps a fixed shape in the limit. A rectangle of fixed height 1 would have zero area as $T_0\to0$, and its response would vanish. With the height $1/T_0$ the area stays 1, and the response tends to $h(t)$. For the RC circuit, the peak of the response is $(1-\mathrm{e}^{-T_0})/T_0$: 0.632 for $T_0=1$ s, 0.787 for 0.5 s, 0.952 for 0.1 s, and as $T_0\to0$ it becomes $1=h(0^+)$. Throughout, the area of the response stays 1.
:::

:::frage Does the impulse $\delta(t)$ exist in reality? Then how do you measure $h(t)$?
An infinitely short impulse does not exist. But any pulse that is much shorter than the time constants of the system will do. The system then sees only its area, and the response is practically $(\text{area})\cdot h(t)$. For the RC circuit with $RC=1$ s, the peak of the response to a 1-ms pulse deviates from $h(0^+)$ by only 0.05 %. This is also how impulse responses are measured: you clap your hands in a room and record the reverberation.
:::

:::ltspice Approximating the impulse response with a short rectangle
⁠**Draw:** the RC circuit from Stage [2](ein-erstes-system-das-rc-glied.html#stufe-2) with the source `PULSE(0 {1/T0} 0 1n 1n {T0})`: a rectangle of width $T_0$ and height $1/T_0$, hence area 1.

⁠**Directives:** `.param T0=1`, `.step param T0 list 1 0.5 0.1 1m`, `.tran 0 10 0 1m`, `.meas tran peak MAX V(out)`, `.meas tran area INTEG V(out)`.

⁠**What you see:** The peaks are 0.632, 0.787, 0.952 and 0.9995, as given by $(1-\mathrm{e}^{-T_0})/T_0$. For the 1-ms pulse the response is practically $h(t)=\mathrm{e}^{-t}$ already. The area is 1.000 in all four runs: a pulse much shorter than $RC$ acts only through its area.
:::

:::aufgabe Exercise 4 ★★ A closer look at the staircase
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Compute the response $g_0(t)$ of the RC circuit ($RC=1$ s) to the rectangle of height $1/T_0$ from $0$ to $T_0$. To do this, use [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5) and write the rectangle as the difference of two steps.

</li>

<li>

Show that $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$ and that it tends to 1 as $T_0\to0$.

</li>

<li>

Why does the approximation $g_a$ in Fig. [5](#abb-5) come too late? (Hint: where does the stair step lie relative to the triangle on the rising edge, and where on the falling edge?)

</li>

</ol>

:::loesung
(a) The rectangle is $\frac{1}{T_0}[\varepsilon(t)-\varepsilon(t-T_0)]$. Linearity and time invariance together with the step response [(2.5)](ein-erstes-system-das-rc-glied.html#gl-2-5) give

$$g_0(t)=\frac{1}{T_0}\Bigl[\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)-\bigl(1-\mathrm{e}^{-(t-T_0)}\bigr)\varepsilon(t-T_0)\Bigr].$$

(b) At $t=T_0$ the second term is zero: $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$. With $\mathrm{e}^{-T_0}\approx1-T_0+T_0^2/2$ for small $T_0$, this is $\approx1-T_0/2\to1=h(0^+)$. Numbers: 0.632, 0.787 and 0.952 for $T_0=1$, 0.5 and 0.1 s.

(c) Each stair step holds the value $s(nT_0)$ from the *beginning* of its interval to the end. On the rising edge the staircase therefore lies below the triangle, and on the falling edge above it: on average it is delayed by $T_0/2$. The output inherits this delay; on the falling side, $g_a$ lies above $g$ ($g_a(2)=0.508$ instead of $0.400$ for $T_0=0.5$ s). As $T_0$ gets smaller, the delay shrinks, and with it the error.
:::
:::
