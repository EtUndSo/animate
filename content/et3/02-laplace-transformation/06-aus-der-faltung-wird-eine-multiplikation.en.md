---
title: Stage 3: Convolution becomes multiplication
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Laplace Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Chapter 2: Laplace Transform
order: 3220600
summary: Stage 1 says what the system does to one building block.
tags: 
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Stage [1](warum-gerade.html#stufe-1) says what the system does to one building block. Stage [2](ein-signal-aus-lauter-bausteinen.html#stufe-2) says that every signal consists of building blocks. Together they give the most important theorem of the Laplace transform.
:::

**The idea.** An LTI system is linear: it processes each building block of the input separately and adds the results. It multiplies each building block $\mathrm{e}^{pt}$ by $H(p)$. So the output consists of the *same* building blocks as the input, except that each weight is multiplied by $H(p)$. Figure [4](#abb-4) shows the two routes to the output.

:::abbildung et3/k2wege 4
Two routes from input to output. Top: directly with the convolution integral. Bottom: decompose the input into building blocks, multiply each weight by $H(p)$, reassemble. The bottom route works because every building block is an eigenfunction.
:::

:::satz Theorem 3.1 (Convolution theorem)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$g(t)=s(t)*h(t)\quad\Longleftrightarrow\quad G(p)=S(p)\,H(p), \tag{3.1}$$

valid for all $p$ that lie in the regions of convergence of both $S$ and $H$.
:::

⁠**How to read it:** $S(p)$ is the weight of the building block $\mathrm{e}^{pt}$ in the input, $H(p)$ is the factor by which the system multiplies this building block, and $G(p)$ is the weight in the output. The condition on $p$ arises because the line of the inversion formula must run through both regions of convergence: the input must be decomposable into building blocks, and the system must be able to process each of them.

:::herleitung Convolution theorem from superposition and eigenfunction
Insert the input as the superposition [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1) into the convolution, using a line $\operatorname{Re} p=\sigma$ that lies in both regions of convergence:

$$g(t)=s(t)*h(t)=\left[\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p\right]*h(t).$$

Linearity: the convolution may be moved inside the integral, where it acts on each building block separately:

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\bigl[\mathrm{e}^{pt}*h(t)\bigr]\,\mathrm{d} p.$$

Eigenfunction [(1.1)](warum-gerade.html#gl-1-1): $\mathrm{e}^{pt}*h(t)=H(p)\,\mathrm{e}^{pt}$.

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[S(p)H(p)\bigr]\,\mathrm{e}^{pt}\,\mathrm{d} p.$$

This is the inversion formula for $g$ with the weight $S(p)H(p)$. Since the weights of a signal are unique, $G(p)=S(p)H(p)$.
:::

⁠**In short:** Convolution becomes multiplication because the system only multiplies each building block $\mathrm{e}^{pt}$ by the number $H(p)$.

:::analogie
A graphic equalizer splits music into frequency bands, multiplies each band by the setting of its slider and puts the bands back together. An LTI system does the same with the building blocks $\mathrm{e}^{pt}$, and the slider setting is $H(p)$. The analogy breaks down in two places: an equalizer has finitely many bands with real slider settings. Here there is a continuum of building blocks, which can also grow or decay, and each “slider” is a complex number that also shifts the phase.
:::

**The same mechanism explains derivatives, integrals and differential equations.**

<ul>

<li>

⁠**Differentiation.** $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$. The differentiator is an LTI system, and each building block is an eigenfunction of it with the eigenvalue $p$. So each weight is multiplied by $p$: $\mathcal{L}\{\dot s\}=p\,S(p)$.

</li>

<li>

⁠**Integration.** $\int_{-\infty}^{t}\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$, but only for $\operatorname{Re} p>0$; otherwise the integral diverges at $-\infty$. Hence $\mathcal{L}\{\int_{-\infty}^t s\,\mathrm{d}\tau\}=S(p)/p$ with the additional condition $\operatorname{Re} p>0$.

</li>

<li>

⁠**Cascade.** Two systems in series multiply first by $H_1(p)$ and then by $H_2(p)$, together by $H_1H_2$. The order does not matter, because numbers commute.

</li>

<li>

⁠**Differential equation.** Each derivative becomes a factor $p$. A linear differential equation with constant coefficients

$$\sum_{r=0}^{R}\alpha_r\frac{\mathrm{d}^r g}{\mathrm{d} t^r}=\sum_{q=0}^{Q}\beta_q\frac{\mathrm{d}^q s}{\mathrm{d} t^q} \quad\text{becomes}\quad \Bigl(\sum_{r}\alpha_rp^r\Bigr)G(p)=\Bigl(\sum_q\beta_qp^q\Bigr)S(p),$$

that is, an algebraic equation, and $H(p)=G/S$ is a ratio of polynomials.

</li>

</ul>

**Example: the step response of the RC low-pass filter.** Input $\varepsilon(t)$ with $S(p)=1/p$ ($\operatorname{Re} p>0$), system $H(p)=1/(p+1)$ ($\operatorname{Re} p>-1$). The common region is $\operatorname{Re} p>0$:

$$G(p)=\frac{1}{p}\cdot\frac{1}{p+1}=\frac1p-\frac{1}{p+1}\quad\Longrightarrow\quad g(t)=\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

The inverse transform of the two terms follows from [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) with $p_0=0$ and $p_0=-1$. Checked directly: $g(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$ for $t>0$. The inversion formula [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1), evaluated numerically on the line $\sigma=0.5/\mathrm s$, also gives $g(0.5\,\mathrm{s})=0.3935$, $g(1\,\mathrm{s})=0.6321$, $g(3\,\mathrm{s})=0.9502$ and $g(-1\,\mathrm{s})=0$, exactly $\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)$.

:::ltspice Entering the transfer function directly
⁠**Draw:** the RC circuit (`1Meg`, `1u`) from `in` to `rc`. Next to it a voltage-controlled voltage source `e`: control input at `in` and ground, output at net `lap`, value `Laplace=1/(1+s)`. This source is an LTI system given only by $H$: LTspice computes the impulse response from it and convolves the input with it. LTspice writes $s$ instead of $p$.

⁠**Source and directive:** `PULSE(0 1 0 1u 1u 100)`, `.tran 0 5 0 1m`.

⁠**What you see:** `V(rc)` and `V(lap)` lie on top of each other (difference below 0.001), reaching 0.3935 at 0.5 s, 0.6321 at 1 s and 0.9502 at 3 s. With the source value `AC 1` and `.ac dec 100 0.01 100`, LTspice shows $H(s)$ for $s=\mathrm{j}2\pi f$, i.e. only on the imaginary axis: $-3.0$ dB and $-45^\circ$ at 0.159 Hz.

⁠**For Exercise [6](#aufg-6):** source `PWL(0 0 10 10)`, the ramp $t\,\varepsilon(t)$ up to 10 s, and `.tran 0 10 0 1m`. Compare `V(rc)` with your result from Exercise [6](#aufg-6)(b).
:::

:::aufgabe Exercise 5 ★★ Cascade and derivative via the building blocks
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Use the building-block picture (without the convolution integral) to explain why two LTI systems in cascade have the transfer function $H_1(p)H_2(p)$. Why does it follow that convolution is commutative?

</li>

<li>

Derive $\mathcal{L}\{\dot s(t)\}=p\,S(p)$ from the inversion formula by differentiating it with respect to $t$.

</li>

</ol>

:::loesung
(a) The input consists of building blocks $\mathrm{e}^{pt}$ with weights $S(p)$. The first system multiplies each building block by $H_1(p)$, so the weights are then $H_1S$. The second multiplies by $H_2(p)$: $G=H_2H_1S$. So the cascade has $H=H_1H_2$. Because $H_1H_2=H_2H_1$, the result does not depend on the order, and since $h_1*h_2$ is the impulse response of the cascade, it follows that $h_1*h_2=h_2*h_1$.

(b) Differentiating under the integral acts only on $\mathrm{e}^{pt}$:

$$\dot s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}\,\mathrm{d} p=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[p\,S(p)\bigr]\mathrm{e}^{pt}\,\mathrm{d} p.$$

This is the inversion formula with the weight $pS(p)$, so $\mathcal{L}\{\dot s\}=pS(p)$.
:::
:::

:::aufgabe Exercise 6 ★★ Ramp response of the RC low-pass filter
<span class="anker" id="aufg-6"></span>

Input $s(t)=t\,\varepsilon(t)$ with $S(p)=1/p^2$ for $\operatorname{Re} p>0$, basic transform pair [(2.5)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-5).

<ol class="al">

<li>

Find $G(p)$ and its region of convergence.

</li>

<li>

Check the decomposition $G(p)=\frac{1}{p^2}-\frac1p+\frac{1}{p+1}$ and find $g(t)$.

</li>

<li>

Check: what is $g(0)$, and why must it be so? What is $\dot g(t)$?

</li>

<li>

How does $g(t)$ behave for $t\gg1$ s? Compare with Exercise [1](warum-gerade.html#aufg-1)c.

</li>

</ol>

:::loesung
(a) $G(p)=\dfrac{1}{p^2}\cdot\dfrac{1}{p+1}=\dfrac{1}{p^2(p+1)}$ for $\operatorname{Re} p>0$ (intersection of $\operatorname{Re} p>0$ and $\operatorname{Re} p>-1$).

(b) Over the common denominator: $\frac{1}{p^2}-\frac1p+\frac{1}{p+1}=\frac{(p+1)-p(p+1)+p^2}{p^2(p+1)}=\frac{1}{p^2(p+1)}$. Inverse transform with [(2.5)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-5) and [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2):

$$g(t)=\bigl(t-1+\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

(c) $g(0)=0-1+1=0$: the capacitor voltage cannot jump, and the input starts at zero. $\dot g(t)=(1-\mathrm{e}^{-t})\varepsilon(t)$, exactly the step response. This fits: the ramp is the integral of the step, so the ramp response is the integral of the step response.

(d) For $t\gg1$ s, $\mathrm{e}^{-t}\approx0$ and $g(t)\approx t-1$: the output follows the ramp with a delay of $RC=1$ s, just as for the two-sided ramp in Exercise [1](warum-gerade.html#aufg-1)c. The difference is the building block $\mathrm{e}^{-t}$ (pole $-1$ of the system): the transient, which arises because here the ramp only starts at $t=0$.
:::
:::
