---
title: Stage 5: Distribution function and probability density
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3270600
summary: Averages do not tell everything.
tags: cumulative distribution function, probability density function, quantizer
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Averages do not tell everything. How often does a signal take which values? This is described by the distribution.
:::

:::definition Definition 5.1 (Distribution)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-1"></span>
$$P_s(x)=\mathrm{Prob}[s(t)\le x],\qquad p_s(x)=\frac{\mathrm{d} P_s(x)}{\mathrm{d} x},\qquad P_s(x)=\int_{-\infty}^xp_s(\xi)\,\mathrm{d}\xi. \tag{5.1}$$
:::

⁠**How to read it:** The __cumulative distribution function__ $P_s(x)$ is the fraction of the ensemble (for ergodic processes: the fraction of time) in which the signal lies below the threshold $x$. It rises monotonically from $P_s(-\infty)=0$ to $P_s(\infty)=1$. The __probability density function__ $p_s(x)$ is never negative, has the area 1, and $p_s(x)\,\mathrm{d} x$ is the probability that the signal lies between $x$ and $x+\mathrm{d} x$. All first-order averages follow from it:

<span class="anker" id="gl-5-2"></span>
$$m_s=\int x\,p_s(x)\,\mathrm{d} x,\qquad L_s=\int x^2p_s(x)\,\mathrm{d} x,\qquad\mathrm E\{F[s]\}=\int F(x)\,p_s(x)\,\mathrm{d} x. \tag{5.2}$$

**Example: uniform distribution.** All values in an interval of width $a$ around $m_s$ are equally likely: $p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$. Then

$$L_s=\frac1a\int_{m_s-a/2}^{m_s+a/2}x^2\mathrm{d} x=\frac{a^2}{12}+m_s^2,\qquad\sigma_s^2=\frac{a^2}{12}.$$

The random numbers of the reference model ($a=1$, $m_s=0$) have the variance $\frac1{12}=0.0833$.

**Characteristic curves.** If a signal passes through a characteristic curve (transfer characteristic) $y=k(x)$ (amplifier with saturation, rectifier, quantizer), its distribution changes. For a monotonic characteristic, the probability of every interval is preserved:

<span class="anker" id="gl-5-3"></span>
$$p_g(y)\,|\mathrm{d} y|=p_s(x)\,|\mathrm{d} x|\qquad\Longrightarrow\qquad p_g(y)=\frac{p_s(x)}{|k'(x)|},\qquad P_g\bigl(k(x)\bigr)=P_s(x)\ \ (k\text{ increasing}). \tag{5.3}$$

Where the characteristic is steep, the values are spread over a wide range, and the density decreases. With this rule, any distribution can be transformed into a desired one. Example: $k(x)=(2|x|-x^2)\operatorname{sgn}x$ turns a triangular distribution on $[-1,1]$ into a uniform distribution (Exercise [4](#aufg-4)).

**Quantization.** A __quantizer__ replaces every value by the nearest of $M$ levels. With uniform levels of width $\Delta$ and no overload, the error between $-\frac\Delta2$ and $\frac\Delta2$ is approximately uniformly distributed, hence has the variance $\frac{\Delta^2}{12}$. For a signal uniformly distributed over all $M$ levels (variance $\frac{(M\Delta)^2}{12}$), the signal-to-noise ratio is $M^2$, in decibels $20\lg M\approx6\,\text{dB per bit}$: 48 dB at 8 bits, 96 dB at 16 bits.

:::aufgabe Exercise 3 ★ Uniform distribution
<span class="anker" id="aufg-3"></span>

A signal is uniformly distributed between 1 V and 3 V. Compute $m_s$, $L_s$, $\sigma_s^2$ and the probability that it lies above 2.5 V.

:::loesung
$a=2$ V, $m_s=2$ V. $\sigma_s^2=\frac{a^2}{12}=\frac13$ V$^2$, $L_s=\frac13+4=4.33$ V$^2$. A quarter of the interval lies above 2.5 V, so $\mathrm{Prob}=\frac{0.5}{2}=0.25$.
:::
:::

:::aufgabe Exercise 4 ★★ Transforming distributions
<span class="anker" id="aufg-4"></span>

A signal has the triangular density $p_s(x)=\Lambda(x)$ on $[-1,1]$.

<ol class="al">

<li>

Find $P_s(x)$ for $0\le x\le1$.

</li>

<li>

Use [(5.3)](#gl-5-3) to show that $k(x)=(2x-x^2)$ for $x\ge0$ (continued as an odd function) produces a uniform distribution on $[-1,1]$. Hint: for the uniform distribution, $P_g(y)=\frac12+\frac y2$.

</li>

</ol>

:::loesung
(a) $P_s(x)=\frac12+\int_0^x(1-\xi)\,\mathrm{d}\xi=\frac12+x-\frac{x^2}{2}$ for $0\le x\le1$.

(b) According to [(5.3)](#gl-5-3), $P_g(k(x))=P_s(x)$ must hold, so $\frac12+\frac{k(x)}{2}=\frac12+x-\frac{x^2}{2}$. This gives $k(x)=2x-x^2$. The characteristic is steep at $x=0$ (slope 2), where the triangular density is largest, and flat at the edge. In this way, the frequent values are pulled apart and the rare ones are pushed together. A simulation gives a flat histogram of height 0.5.
:::
:::

:::aufgabe Exercise 4a ★★★ (Going further) The optimal quantizer
<span class="anker" id="aufg-4a"></span>

A quantizer with the thresholds $u_i$ and the level values $v_i$ (level $i$ applies for $u_i<x\le u_{i+1}$) has the mean squared error $N_q=\sum_i\int_{u_i}^{u_{i+1}}(v_i-x)^2p_s(x)\,\mathrm{d} x$.

<ol class="al">

<li>

Show by differentiating with respect to $v_i$: at the optimum, $v_i$ lies at the centroid of the density on its interval.

</li>

<li>

Show by differentiating with respect to $u_i$: at the optimum, $u_i$ lies exactly halfway between $v_{i-1}$ and $v_i$.

</li>

<li>

Why is the uniform quantizer optimal for a uniformly distributed signal?

</li>

</ol>

:::loesung
(a) $\frac{\partial N_q}{\partial v_i}=\int_{u_i}^{u_{i+1}}2(v_i-x)p_s(x)\mathrm{d} x=0$, so $v_i=\dfrac{\int_{u_i}^{u_{i+1}}x\,p_s\,\mathrm{d} x}{\int_{u_i}^{u_{i+1}}p_s\,\mathrm{d} x}$, the centroid.

(b) $u_i$ appears as the upper limit of interval $i-1$ and as the lower limit of interval $i$: $\frac{\partial N_q}{\partial u_i}=(v_{i-1}-u_i)^2p_s(u_i)-(v_i-u_i)^2p_s(u_i)=0$, so $u_i=\frac12(v_{i-1}+v_i)$. A value is assigned to the level whose level value is closer.

(c) For a constant density, the centroid of each interval is its midpoint. Intervals of equal width with their midpoints as level values satisfy both conditions, with the step size $\Delta=a/M$.
:::
:::
