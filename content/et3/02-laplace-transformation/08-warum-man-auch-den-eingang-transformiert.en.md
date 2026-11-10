---
title: Stage 5: Why the input is transformed too
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Laplace Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Chapter 2: Laplace Transform
order: 3220800
summary: Every signal as a superposition of $\mathrm{e}^{pt}$, and why an LTI system turns this into a multiplication
tags: 
lang: en
---

<span class="anker" id="stufe-5"></span>

:::frage Transforming $h(t)$ is useful: $H(p)$ multiplies the eigenfunctions, and the output follows. But why transform the input signal $s(t)$? True, $s*h=h*s$, but $h(t)$ is usually not an eigenfunction, so $h(t)\cdot S(p)$ makes no sense. What does transforming an arbitrary signal mean for the system?
⁠**What is right about the question:** $H(p)$ says what the system does to a building block $\mathrm{e}^{pt}$. And $h(t)\cdot S(p)$ indeed makes no sense.

⁠**Where the reasoning goes wrong:** The input is almost never an eigenfunction either. A step, a speech signal or a rectangular pulse is not a single building block $\mathrm{e}^{pt}$. So $H(p)\cdot s(t)$ makes just as little sense as $h(t)\cdot S(p)$: $H(p)$ may only be applied to a building block, and for an arbitrary $s(t)$ it is not even clear which $p$ is meant. Before $H(p)$ can do anything, the input must be decomposed into building blocks. That is exactly what $S(p)$ does.

⁠**The correct view:** In the convolution theorem $G(p)=H(p)\,S(p)$, each factor has its own meaning in terms of the system:

<ul>

<li>

$S(p)$ is the *recipe of the input*: how much of the building block $\mathrm{e}^{pt}$ the input contains;

</li>

<li>

$H(p)$ is the *action of the system*: the number by which it multiplies this building block;

</li>

<li>

$G(p)$ is the recipe of the output.

</li>

</ul>

Without $S(p)$ you know only the action on individual building blocks, but not which building blocks arrive. $H(p)$ alone answers the question “What happens at the output?” only in the one special case where the input itself is a single building block.

⁠**Example: step and RC low-pass filter.** The step has the recipe $S(p)=1/p$. On the line $\sigma=0.5/\mathrm s$, $|S|=2$ at $f=0$, $0.16$ at 1 Hz and $0.016$ at 10 Hz. The fast building blocks are weak but present, and they form the sharp edge (Fig. [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3): the more fast building blocks, the steeper the edge). The RC low-pass filter multiplies them by $|H|=0.67$, $0.15$ and $0.016$. In the output, the fast building blocks are therefore weaker by a further factor of roughly $2\pi f\cdot RC$ (for $f\gg1/(2\pi RC)=0.16$ Hz), and the edge is gone: $g(t)=1-\mathrm{e}^{-t}$ rises continuously. This explanation needs both transforms. $H$ alone only says “fast building blocks are weakened”; only $S$ says that the edge consists of fast building blocks.

⁠**And the symmetry $s*h=h*s$?** Mathematically the two signals are on an equal footing: you can also read $h$ as the input and $s$ as the “system”, and then $H(p)$ is the recipe and $S(p)$ the action. System theory assigns the roles only according to the physics: one signal comes from outside, the other describes the circuit. In the transform domain, *both* are always transformed.
:::

**Further reasons to transform a signal on its own.**

<ul>

<li>

⁠**Measuring a system.** If you measure the input and output of an unknown system, $H(p)=G(p)/S(p)$ gives you the system. For this you transform two signals, each on its own (Exercise [9](#aufg-9)).

</li>

<li>

⁠**Understanding the signal itself.** The sound of a struck bell is a sum of damped oscillations, each one a conjugate pair of poles. $\operatorname{Im} p_r$ is the pitch of a partial, $-\operatorname{Re} p_r$ its decay rate. A few poles describe the whole sound. An instrument that displays a spectrum does the same on the line $\sigma=0$.

</li>

<li>

⁠**Convolution without a system.** Convolution superposes shifted, weighted copies of a signal. The system is one interpretation of this operation, not the only one. An example with no system at all is the sum of two dice, treated in the chapter on convolution ([Chapter 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)).

</li>

</ul>

:::ltspice A network for two measurements
⁠**Draw:** the network you found in Exercise [9](#aufg-9)(c), with the source `PULSE(0 1 0 1u 1u 100)` at its input and its output at net `out`. Next to it, not connected to the circuit, a behavioural source `bv` at net `mess` with `V=1-exp(-2*time)`. It plays the measured output curve.

⁠**Directives:** `.tran 0 3 0 1m`, `.meas tran dev MAX abs(V(out)-V(mess))`.

⁠**What you see:** If the network and the component values are right, `V(out)` and `V(mess)` lie on top of each other, and the largest deviation `dev` is practically zero (below $10^{-5}$). In this way, compare the curves with your result from Exercise [9](#aufg-9)(c).
:::

:::aufgabe Exercise 8 ★★ Which building blocks form the edge?
<span class="anker" id="aufg-8"></span>

Input $\varepsilon(t)$, system: RC low-pass filter with $RC=1$ s. Consider the building blocks on the line $\sigma=0.5/\mathrm s$.

<ol class="al">

<li>

Compute $|S(p)|$, $|H(p)|$ and $|G(p)|$ for $f=0$, $1$ Hz and $10$ Hz.

</li>

<li>

By what factor does the system weaken the building blocks at 10 Hz more than those at 1 Hz?

</li>

<li>

Use (a) and Fig. [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3) to explain why the output has no edge. Why is $H(p)$ alone not enough for this explanation?

</li>

</ol>

:::loesung
(a) With $p=0.5+\mathrm{j}2\pi f$ (in $1/\mathrm s$), $S=1/p$, $H=1/(p+1)$, $G=SH$:

| $f$ | $\vert S(p)\vert $ | $\vert H(p)\vert $ | $\vert G(p)\vert $ |
|---|---|---|---|
| 0 | 2 | 0.667 | 1.33 |
| 1 Hz | 0.159 | 0.155 | 0.0246 |
| 10 Hz | 0.0159 | 0.0159 | 0.000253 |

(b) $0.155/0.0159\approx9.7$, so almost a factor of 10, just like the frequency. For large $|p|$, $|H|\approx1/|p|\approx1/(2\pi f)$.

(c) The edge of the step consists of the fast building blocks: in Fig. [3](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#abb-3) it becomes steeper the more of them are included. In the input their weights fall like $1/f$, in the output like $1/f^2$. In the output the fast building blocks are so weak that no edge forms any more, and $g(t)$ rises continuously. $H(p)$ alone only says that fast building blocks are weakened. That the edge consists of exactly these building blocks is a statement about the input, and that statement is contained in $S(p)$.
:::
:::

:::aufgabe Exercise 9 ★★ An unknown system from two measurements
<span class="anker" id="aufg-9"></span>

A voltage of 1 V is applied to an unknown causal LTI system at time $t=0$, $s(t)=\varepsilon(t)$ in V. At the output one measures $g(t)=\bigl(1-\mathrm{e}^{-2t}\bigr)\varepsilon(t)$ in V ($t$ in s).

<ol class="al">

<li>

Transform both signals, each on its own.

</li>

<li>

Find $H(p)$ and from it $h(t)$.

</li>

<li>

Which network could it be? What value do you get?

</li>

<li>

Which pole in $G(p)$ comes from the input, and which from the system?

</li>

</ol>

:::loesung
(a) $S(p)=\dfrac1p$ for $\operatorname{Re} p>0$. $G(p)=\dfrac1p-\dfrac{1}{p+2}=\dfrac{2}{p(p+2)}$ for $\operatorname{Re} p>0$ (basic transform pair [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) with $p_0=0$ and $p_0=-2$).

(b) $H(p)=\dfrac{G(p)}{S(p)}=\dfrac{2}{p+2}$. Since the system is causal, the region of convergence lies to the right of the pole: $\operatorname{Re} p>-2$. With [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2): $h(t)=2\,\mathrm{e}^{-2t}\varepsilon(t)$ in $1/\mathrm s$.

(c) An RC low-pass filter has $H(p)=\dfrac{1}{1+pRC}=\dfrac{1/RC}{p+1/RC}$. Comparing with $\dfrac{2}{p+2}$ gives $RC=0.5$ s, for example $R=500\,\mathrm{k\Omega}$ and $C=1$ µ F. (Any other network with the same transfer function would behave identically at its terminals. Measurements at the input and output reveal only $H$, not the components.)

(d) The pole $p=0$ comes from the input (the step), the pole $p=-2$ from the system. In the division $G/S$, exactly the pole of the input cancels.
:::
:::
