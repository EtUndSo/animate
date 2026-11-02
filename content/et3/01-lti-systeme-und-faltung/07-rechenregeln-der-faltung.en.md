---
title: Stage 6: Rules of convolution
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / LTI Systems and Convolution
order: 3210700
summary: In many respects convolution behaves like multiplication.
tags: convolution product, ideally distortion-free
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
In many respects convolution behaves like multiplication. Each rule has a meaning for systems.
:::

The convolution integral is written in short as the __convolution product__ $g(t)=s(t)*h(t)$. Equation [(4.1)](das-faltungsintegral.html#gl-4-1) then reads $s(t)=s(t)*\delta(t)$.

<ol class="al">

<li>

⁠**Identity element.** $s*\delta=s$: the Dirac impulse plays the role of the number one. A system with $h(t)=\delta(t)$ passes every signal on unchanged; it is called __ideally distortion-free__.

</li>

<li>

⁠**Commutative law.** $s*h=h*s$. Meaning: input and impulse response may swap roles. The system with the impulse response $s$ responds to the input $h$ exactly as the system $h$ responds to the input $s$.

</li>

<li>

⁠**Associative law.** $(f*s)*h=f*(s*h)$. Meaning: two systems in cascade act like one system whose impulse response is the convolution of the two impulse responses.

</li>

<li>

⁠**Distributive law.** $f*(s+h)=f*s+f*h$. Meaning: two systems connected in parallel, whose outputs are added, act like one system with the sum of the impulse responses.

</li>

<li>

⁠**Complex signals.** Because convolution is linear, it splits into real and imaginary parts:

<span class="anker" id="gl-6-1"></span>
$$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr]. \tag{6.1}$$

</li>

</ol>

:::herleitung Commutative law
Substitute $\tau'=t-\tau$, so $\tau=t-\tau'$ and $\mathrm{d}\tau=-\mathrm{d}\tau'$. The limits $\tau=\mp\infty$ become $\tau'=\pm\infty$; swapping them cancels the minus sign:

$$s*h=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau=\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'=h*s.$$
:::

:::abbildung et3/k1bloecke 7
Top: cascade connection, impulse response $h_1*h_2$ (associative law). Bottom: parallel connection with addition, impulse response $h_1+h_2$ (distributive law).
:::

:::aufgabe Exercise 7 ★★ Two RC circuits in cascade
<span class="anker" id="aufg-7"></span>

Two RC circuits with $RC=1$ s are connected in cascade. Assume that the second does not load the first (for example, with a voltage follower in between).

<ol class="al">

<li>

Compute the impulse response of the cascade, $h*h$ with $h(t)=\mathrm{e}^{-t}\varepsilon(t)$.

</li>

<li>

When is it at its maximum, and what is its area?

</li>

<li>

Why is the condition “does not load” needed?

</li>

</ol>

:::loesung
(a) For $t\ge0$:

$$(h*h)(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{e}^{-(t-\tau)}\mathrm{d}\tau=\mathrm{e}^{-t}\int_0^t\mathrm{d}\tau=t\,\mathrm{e}^{-t}.$$

So $h_{\text{cascade}}(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$.

(b) Derivative: $(1-t)\mathrm{e}^{-t}=0$ at $t=1$ s, maximum $\mathrm{e}^{-1}=0.368$. Area: $\int_0^\infty t\mathrm{e}^{-t}\mathrm{d} t=1=1\cdot1$ (product of the areas).

(c) Without decoupling, the second RC circuit draws current from the first capacitor. The voltage across the first capacitor is then no longer that of an unloaded RC circuit, and the cascade does not have $h*h$ as its impulse response. It remains an LTI system, but with a different impulse response. Convolving the individual responses assumes that no system acts back on its input.
:::
:::
