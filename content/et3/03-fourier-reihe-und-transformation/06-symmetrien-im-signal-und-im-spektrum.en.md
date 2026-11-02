---
title: Stage 5: Symmetries in the signal and in the spectrum
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Fourier Series and Transform
order: 3230600
summary: Whether a signal is real, even or odd can be seen immediately from its spectrum.
tags: even, odd
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Whether a signal is real, even or odd can be seen immediately from its spectrum. This stage derives the rules.
:::

**Even and odd parts.** A complex function is called __even__ if $x(t)=x^*(-t)$, and __odd__ if $x(t)=-x^*(-t)$. (For real functions these are the usual mirror symmetry and point symmetry about the origin.) Every signal splits uniquely into the two parts:

<span class="anker" id="gl-5-1"></span>
$$s(t)=s_g(t)+s_u(t),\qquad s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr],\qquad s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]. \tag{5.1}$$

:::satz Theorem 5.1 (Symmetries)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-2"></span>
$$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\},\qquad s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}. \tag{5.2}$$

For **real** signals, $S(-f)=S^*(f)$: the real part and the magnitude $|S|$ are even in $f$, the imaginary part and the phase are odd. A real, even signal has a real, even spectrum. A real, odd signal has a purely imaginary, odd spectrum.
:::

:::herleitung Symmetries
First: $\mathcal{F}\{s^*(-t)\}=\int s^*(-t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$. With $\tau=-t$ this is $\int s^*(\tau)\mathrm{e}^{\mathrm{j}2\pi f\tau}\mathrm{d}\tau=\bigl(\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f\tau}\mathrm{d}\tau\bigr)^*=S^*(f)$. Hence

$$\mathcal{F}\{s_g\}=\tfrac12\bigl[S(f)+S^*(f)\bigr]=\operatorname{Re}\{S(f)\},\qquad\mathcal{F}\{s_u\}=\tfrac12\bigl[S(f)-S^*(f)\bigr]=\mathrm{j}\operatorname{Im}\{S(f)\}.$$

For real $s$, $\mathcal{F}\{s^*(t)\}=\mathcal{F}\{s(t)\}$. In general, $\mathcal{F}\{s^*(t)\}=\int s^*\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\bigl(\int s\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} t\bigr)^*=S^*(-f)$. So $S(f)=S^*(-f)$.
:::

⁠**In short:** For a real signal, the negative half of the spectrum is the conjugate mirror image of the positive half. It contains no new information.

**Example.** The exponential pulse $\varepsilon(t)\mathrm{e}^{-t}$ (real) has the even part $\frac12\mathrm{e}^{-|t|}$ and the odd part $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$. Its spectrum $H(f)=\frac{1}{1+\mathrm{j}2\pi f}$ has the even real part $\frac{1}{1+(2\pi f)^2}$, the transform of $\frac12\mathrm{e}^{-|t|}$, and the odd imaginary part $\frac{-2\pi f}{1+(2\pi f)^2}$ (Fig. [5](#abb-5)).

:::abbildung et3/k3gerade 5
The exponential pulse ($RC=1$ s), decomposed into an even part (blue) and an odd part (red). Right: the spectrum. The even part yields the real part (even in $f$), the odd part the imaginary part (odd in $f$).
:::

:::aufgabe Exercise 5 ★ Reading off symmetry
<span class="anker" id="aufg-5"></span>

What can be said about the spectrum without calculation? (a) $s(t)=\operatorname{rect}(t)$, (b) $s(t)=\operatorname{sgn}(t)\operatorname{rect}(t/2)$, (c) $s(t)=\mathrm{e}^{\mathrm{j}2\pi t}\operatorname{rect}(t)$, (d) a real signal with $S(1\,\mathrm{Hz})=2-3\mathrm{j}$: what is $S(-1\,\mathrm{Hz})$?

:::loesung
(a) Real and even: spectrum real and even ($\operatorname{si}(\pi f)$). (b) Real and odd: spectrum purely imaginary and odd. (c) Complex, but $x^*(-t)=\mathrm{e}^{-\mathrm{j}2\pi(-t)}\operatorname{rect}(-t)=x(t)$: in the sense of the definition the signal is even, so its spectrum is real. By the modulation rule it is $\operatorname{si}(\pi(f-1))$, real, but not symmetric about $f=0$, because the signal is not real. (d) $S(-1\,\mathrm{Hz})=S^*(1\,\mathrm{Hz})=2+3\mathrm{j}$.
:::
:::
