---
title: Stage 6: The rules of calculation (theorems)
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Fourier Series and Transform
order: 3230700
summary: Instead of evaluating every integral anew, you use rules: what happens to the spectrum when the signal is shifted, compressed, differentiated or modulated?
tags: energy density
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
Instead of evaluating every integral anew, you use rules: what happens to the spectrum when the signal is shifted, compressed, differentiated or modulated? Each rule follows from what the operation does to a single oscillation.
:::

:::satz Theorem 6.1 (Theorems of the Fourier transform)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
<span class="anker" id="gl-6-2"></span>
<span class="anker" id="gl-6-3"></span>
<span class="anker" id="gl-6-4"></span>
<span class="anker" id="gl-6-5"></span>
<span class="anker" id="gl-6-6"></span>
<span class="anker" id="gl-6-7"></span>
<span class="anker" id="gl-6-8"></span>
<span class="anker" id="gl-6-9"></span>
<span class="anker" id="gl-6-10"></span>
<span class="anker" id="gl-6-11"></span>
$$\begin{aligned} &\text{Superposition:} && \textstyle\sum_ia_is_i(t)\;\circ\!\!-\!\!\bullet\;\sum_ia_iS_i(f)\\ &\text{Conjugation:} && s^*(t)\;\circ\!\!-\!\!\bullet\;S^*(-f)\\ &\text{Similarity (scaling):} && s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\Bigl(\frac fb\Bigr),\quad b\neq0;\qquad s(-t)\;\circ\!\!-\!\!\bullet\;S(-f)\\ &\text{Shift:} && s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft_0},\qquad\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-\mathrm{j}2\pi ft_0}\\ &\text{Derivative:} && \frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;(\mathrm{j}2\pi f)^nS(f)\\ &\text{Symmetry (duality):} && S(t)\;\circ\!\!-\!\!\bullet\;s(-f)\\ &\text{Modulation:} && \mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f-F)\\ &\text{Frequency-domain derivative:} && -\mathrm{j}2\pi t\,s(t)\;\circ\!\!-\!\!\bullet\;\frac{\mathrm{d}}{\mathrm{d} f}S(f)\\ &\text{Convolution, multiplication:} && s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2,\qquad s_1s_2\;\circ\!\!-\!\!\bullet\;S_1*S_2\\ &\text{Areas:} && \int s(t)\mathrm{d} t=S(0),\qquad\int S(f)\mathrm{d} f=s(0)\\ &\text{Parseval:} && \int|s(t)|^2\mathrm{d} t=\int|S(f)|^2\mathrm{d} f \end{aligned} \tag{6.1|6.2|6.3|6.4|6.5|6.6|6.7|6.8|6.9|6.10|6.11}$$
:::

⁠**How to read the most important ones:**

<ul>

<li>

⁠**Similarity:** A signal compressed in time ($|b|>1$) has a wider spectrum. Short signals need many frequencies. Duration and bandwidth are inversely related.

</li>

<li>

⁠**Shift:** A delay does not change the magnitude, only the phase, and it does so linearly in $f$: every oscillation is shifted by the same time, which at a higher frequency is a larger angle.

</li>

<li>

⁠**Derivative:** $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{j}2\pi f\,\mathrm{e}^{\mathrm{j}2\pi ft}$. Differentiation amplifies high frequencies.

</li>

<li>

⁠**Symmetry:** Forward and inverse transform differ only in the sign of the exponent. Every transform pair therefore yields a second one with the roles swapped.

</li>

<li>

⁠**Modulation:** Multiplication by $\mathrm{e}^{\mathrm{j}2\pi Ft}$ shifts the whole spectrum by $F$. This is how every radio transmitter works.

</li>

<li>

⁠**Multiplication:** The spectrum of the product of two signals is the convolution of the spectra, the counterpart of the convolution theorem.

</li>

<li>

⁠**Parseval:** The energy is the same in both domains. $|S(f)|^2$ is the __energy density__ over frequency.

</li>

</ul>

:::herleitung Similarity, shift, derivative, symmetry, modulation, multiplication, Parseval
⁠**Similarity** ($b>0$, $\tau=bt$): $\int s(bt)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac1b\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi(f/b)\tau}\mathrm{d}\tau=\frac1bS(f/b)$. For $b<0$ the limits are reversed, hence $1/|b|$.

⁠**Shift** ($\tau=t-t_0$): $\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f(\tau+t_0)}\mathrm{d}\tau=\mathrm{e}^{-\mathrm{j}2\pi ft_0}S(f)$. With $s=\delta$, the pair for $\delta(t-t_0)$ follows.

⁠**Derivative:** Differentiate the inverse transform with respect to $t$: $\frac{\mathrm{d}}{\mathrm{d} t}\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f=\int\mathrm{j}2\pi f\,S\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$.

⁠**Symmetry:** In the inverse transform, replace $t$ by $-t$: $s(-t)=\int S(f)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} f$. Now swap the names of the variables $t$ and $f$: $s(-f)=\int S(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, which is the forward transform of $S(t)$.

⁠**Modulation:** $\int\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi(f-F)t}\mathrm{d} t=S(f-F)$. The derivative in the frequency domain follows in the same way by differentiating the forward transform with respect to $f$.

⁠**Multiplication:** Convolution theorem for the signals $s_1(t)$ and $s_2(t)$, that is $s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2$, then apply symmetry to this pair: $S_1(t)S_2(t)\;\circ\!\!-\!\!\bullet\;s_1(-f)*s_2(-f)$. Renaming gives [(6.9)](#gl-6-9).

⁠**Areas:** Set $f=0$ in the forward transform and $t=0$ in the inverse transform.

⁠**Parseval:** $\int|s|^2\mathrm{d} t=\int s\,s^*\mathrm{d} t$ is the product $s(t)s^*(t)$, integrated, so by multiplication, conjugation and the area theorem it equals $\bigl[S(f)*S^*(-f)\bigr]_{f=0}=\int S(\nu)S^*(\nu)\mathrm{d}\nu$.
:::

:::frage Why doesn't a delay change the magnitude of the spectrum?
Because a delay neither attenuates nor amplifies any oscillation; it only shifts each one. Every oscillation is shifted by the same time $t_0$, which at the frequency $f$ is the angle $2\pi ft_0$. That is why the phase is a straight line in $f$ with the slope $-2\pi t_0$. A system with $|H|=1$ and linear phase delays a signal without changing its shape.
:::

:::aufgabe Exercise 6 ★★ Applying the theorems
<span class="anker" id="aufg-6"></span>

Use $\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)$ (Stage [7](rechteck-si-funktion-und-dreieck.html#stufe-7)) and the theorems.

<ol class="al">

<li>

Find the spectrum of a rectangular pulse of height 1 from $t=0$ to $t=2$ s. What is its magnitude at $f=0$, and where is the first zero?

</li>

<li>

Find the spectrum of $\cos(2\pi F_0t)\operatorname{rect}(t)$ with $F_0=5$ Hz and sketch it.

</li>

</ol>

:::loesung
(a) The pulse is $\operatorname{rect}\bigl(\frac{t-1}{2}\bigr)$. Similarity ($T=2$) and shift ($t_0=1$ s): $2\operatorname{si}(2\pi f)\,\mathrm{e}^{-\mathrm{j}2\pi f}$. Magnitude at $f=0$: 2 (the area). First zero at $f=0.5$ Hz. The shift changes only the phase.

(b) $\cos(2\pi F_0t)=\frac12\mathrm{e}^{\mathrm{j}2\pi F_0t}+\frac12\mathrm{e}^{-\mathrm{j}2\pi F_0t}$, modulation: $\frac12\operatorname{si}(\pi(f-5))+\frac12\operatorname{si}(\pi(f+5))$. Two si main lobes of height $\frac12$ at $\pm5$ Hz, with the first zeros 1 Hz on either side.
:::
:::

:::aufgabe Exercise 7 ★★ Symmetry as a tool
<span class="anker" id="aufg-7"></span>

From Exercise [4](vom-periodischen-zum-einmaligen-signal.html#aufg-4) you know that $\mathrm{e}^{-|t|}\;\circ\!\!-\!\!\bullet\;\frac{2}{1+(2\pi f)^2}$. Use this to find the spectrum of $\frac{1}{1+t^2}$ without an integral.

:::loesung
Apply symmetry to the pair: $\frac{2}{1+(2\pi t)^2}\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-|f|}$. Now stretch the time axis. With $x(t)=\frac{2}{1+(2\pi t)^2}$, $x\bigl(\frac{t}{2\pi}\bigr)=\frac{2}{1+t^2}$, so by the similarity theorem with $b=\frac1{2\pi}$ it is $\circ\!\!-\!\!\bullet\;2\pi\,\mathrm{e}^{-2\pi|f|}$. Halving gives

$$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi|f|}.$$

Check with the area theorem: $\int\frac{\mathrm{d} t}{1+t^2}=\pi=S(0)$.
:::
:::
