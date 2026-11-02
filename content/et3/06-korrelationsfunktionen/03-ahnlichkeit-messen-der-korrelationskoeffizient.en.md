---
title: Stage 2: Measuring similarity, the correlation coefficient
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Correlation Functions
order: 3260300
summary: How do you measure with a single number how similar two signals are?
tags: correlation coefficient, orthogonal
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
How do you measure with a single number how similar two signals are? You measure how large their difference is.
:::

**The idea.** The energy of the difference $\Delta(t)=s(t)-g(t)$ is small when the signals are similar. Multiplied out:

$$E_\Delta=\int|s-g|^2\mathrm{d} t=E_s+E_g-\int s^*g\,\mathrm{d} t-\int g^*s\,\mathrm{d} t=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t.$$

So the difference lies solely in the integral of the product. To keep the size of the signals from counting, you normalize both to the energy 1. Then $E_\Delta=2-2\operatorname{Re}\,p_{sg}$ with the __correlation coefficient__

<span class="anker" id="gl-2-1"></span>
$$p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}. \tag{2.1}$$

⁠**How to read it:** $|p_{sg}|\le1$ (Cauchy–Schwarz inequality). $p=1$ means $s=a\,g$ with $a>0$: the same shape. $p=-1$ means $s=-a\,g$: the same shape, opposite sign. $p=0$ means $\int s^*g\,\mathrm{d} t=0$; the signals are __orthogonal__, like the harmonics of a Fourier series in [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html). Example: $\operatorname{rect}(t)$ and $\Lambda(t)$ have $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=0.75$, $E_{\operatorname{rect}}=1$, $E_\Lambda=\frac23$, so $p=0.919$.

:::aufgabe Exercise 2 ★★ Correlation coefficients
<span class="anker" id="aufg-2"></span>

Compute $p$ for (a) $\operatorname{rect}(t)$ and $\operatorname{rect}(t-0.5)$, (b) $\operatorname{rect}(t)$ and $\Lambda(t)$ (result above), (c) $\operatorname{rect}(t)$ and $\operatorname{sgn}(t)\operatorname{rect}(t)$.

:::loesung
(a) The rectangles overlap over a length of 0.5, so $\int=0.5$, and both energies are 1: $p=0.5$. (b) $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=\int_{-1/2}^{1/2}(1-|t|)\mathrm{d} t=0.75$, $E_\Lambda=2\int_0^1(1-t)^2\mathrm{d} t=\frac23$: $p=\frac{0.75}{\sqrt{2/3}}=0.919$. Very similar shapes. (c) $\int\operatorname{sgn}(t)\operatorname{rect}^2(t)\mathrm{d} t=0$: $p=0$; the signals are orthogonal, although they are equal on the right half.
:::
:::
