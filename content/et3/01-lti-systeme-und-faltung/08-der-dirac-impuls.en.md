---
title: Stage 7: The Dirac impulse
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / LTI Systems and Convolution
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Chapter 1: LTI Systems and Convolution
order: 3210800
summary: The Dirac impulse is the limiting object from Stage 4.
tags: distribution, ideal delay element, generalized differentiation
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
The Dirac impulse is the limiting object from Stage [4](das-faltungsintegral.html#stufe-4). It is not an ordinary function. All of its properties follow from the fact that it acts only through its area.
:::

**What $\delta$ is and what it is not.** As $T_0\to0$, the rectangles $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ become ever narrower and taller, while their area stays 1 (Fig. [8](#abb-8)). There is no limit in the sense of ordinary functions: a function that is zero everywhere except at one point has zero area, whatever its value at that point. $\delta(t)$ is therefore a __distribution__: an object that is defined only by its effect under an integral, namely by [(4.1)](das-faltungsintegral.html#gl-4-1). It is drawn as an arrow whose height gives the weight (the area).

:::abbildung et3/k1dirac 8
Left: rectangles of area 1, ever narrower and taller. Right: the symbol for the limiting object. The height of the arrow is the weight, not the function value.
:::

:::satz Theorem 7.1 (Properties of the Dirac impulse)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
<span class="anker" id="gl-7-5"></span>
<span class="anker" id="gl-7-6"></span>
$$\begin{aligned} &\text{Weight:} && [a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t),\\ &\text{Sifting:} && \int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\\ &\text{Area:} && \int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a,\\ &\text{Scaling:} && \delta(bt)=\frac{1}{|b|}\,\delta(t)\quad(b\neq0),\qquad \delta(-t)=\delta(t),\\ &\text{Shifting:} && \delta(t-t_0)*s(t)=s(t-t_0),\\ &\text{Integral:} && \varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t). \end{aligned} \tag{7.1|7.2|7.3|7.4|7.5|7.6}$$
:::

⁠**How to read it:** the product $s(t)\,\delta(t-T)$ can have an effect only at the point $T$, so only $s(T)$ counts. A compressed impulse $\delta(bt)$ is just as “infinitely high”, but its area is only $1/|b|$. A system with $h(t)=\delta(t-t_0)$ delays every signal by $t_0$; it is called an __ideal delay element__. And because the step is the running integral of the impulse, functions with jumps may be differentiated: a jump of height $A$ becomes $A\,\delta$. This is called __generalized differentiation__. Caution: many operations, such as squaring ($\delta^2$), are not defined for Dirac impulses.

:::herleitung Scaling and the sifting product
⁠**Scaling.** For $b>0$, with $\vartheta=b\tau$:

$$\delta(bt)*s(t)=\int\delta(b\tau)\,s(t-\tau)\,\mathrm{d}\tau=\frac1b\int\delta(\vartheta)\,s\Bigl(t-\frac\vartheta b\Bigr)\mathrm{d}\vartheta=\frac1b\,s(t).$$

For $b<0$ the substitution reverses the direction of integration, and the result is $-\frac1b=\frac{1}{|b|}$. So $\delta(bt)$ acts like $\frac1{|b|}\delta(t)$. With $b=-1$ the symmetry $\delta(-t)=\delta(t)$ follows.

⁠**Sifting product.** If $s(t)\delta(t)$ is convolved with an arbitrary $g(t)$, the sifting property gives

$$[s(t)\delta(t)]*g(t)=\int s(\tau)\delta(\tau)\,g(t-\tau)\,\mathrm{d}\tau=s(0)\,g(t)=[s(0)\delta(t)]*g(t).$$

Both act identically on every $g$, so $s(t)\delta(t)=s(0)\delta(t)$. Shifting then gives $s(t)\delta(t-T)=s(T)\delta(t-T)$.

⁠**Integral.** $\varepsilon(t)=\delta(t)*\varepsilon(t)=\int\delta(\tau)\,\varepsilon(t-\tau)\,\mathrm{d}\tau$, and $\varepsilon(t-\tau)=1$ exactly for $\tau\le t$.
:::

:::frage But $\delta(0)$ is infinite. So $\delta(2t)$ is the same as $\delta(t)$, isn't it?
No. “Infinitely high” does not describe $\delta$, because all function values except at $0$ are the same, and the value at $0$ is not a number. What characterizes $\delta$ is its area. If you compress the rectangle of area 1 to half its width and keep its height, the area halves. That is why $\delta(2t)=\frac12\delta(t)$.
:::

:::aufgabe Exercise 8 ★ Calculating with $\delta$
<span class="anker" id="aufg-8"></span>

Compute: (a) $\int_{-\infty}^\infty\delta(t-2)\,\mathrm{e}^{-t}\mathrm{d} t$, (b) $\mathrm{e}^{-t}\,\delta(t-1)$, (c) $\int_{-\infty}^\infty\delta(2t)\,\mathrm{d} t$, (d) $\delta(t)*\delta(t-3)$, (e) $\operatorname{rect}(t)*\delta(t-1)$, (f) $\frac{\mathrm{d}}{\mathrm{d} t}\bigl[3\,\varepsilon(t-1)\bigr]$.

:::loesung
(a) $\mathrm{e}^{-2}=0.135$. (b) $\mathrm{e}^{-1}\,\delta(t-1)$. (c) $\tfrac12$. (d) $\delta(t-3)$. (e) $\operatorname{rect}(t-1)$. (f) $3\,\delta(t-1)$.
:::
:::
