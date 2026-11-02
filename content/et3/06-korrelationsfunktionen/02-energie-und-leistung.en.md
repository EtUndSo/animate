---
title: Stage 1: Energy and power
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Correlation Functions
order: 3260200
summary: Before comparing signals, you need a measure of their “size”.
tags: signal energy, energy signal, power, power signal
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Before comparing signals, you need a measure of their “size”. In system theory this is the energy, or, for infinitely long signals, the power.
:::

In a resistor $R$, the energy $\frac1R\int u^2\mathrm{d} t$ is converted into heat during the time from $t_1$ to $t_2$. Without the factor $1/R$, the expression is called the __signal energy__:

<span class="anker" id="gl-1-1"></span>
$$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t. \tag{1.1}$$

If it is finite, $s$ is called an __energy signal__ (for example, any pulse). If a signal lasts infinitely long without decaying (a cosine, a step), its energy is infinite. Then you measure the average __power__:

<span class="anker" id="gl-1-2"></span>
$$L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t. \tag{1.2}$$

If it is finite, $s$ is called a __power signal__. For periodic signals, averaging over one period is sufficient. For Dirac impulses, energy and power are not defined ($\delta^2$ does not exist).

:::aufgabe Exercise 1 ★ Energy or power?
<span class="anker" id="aufg-1"></span>

Find the energy or the power of (a) $a\operatorname{rect}(t/T)$, (b) $\varepsilon(t)\mathrm{e}^{-t}$, (c) $A\cos(2\pi Ft)$, (d) $\varepsilon(t)$.

:::loesung
(a) $E=a^2|T|$. (b) $E=\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$. (c) Infinite energy, power $\frac{A^2}{2}$ (the mean value of $\cos^2$ is $\frac12$). (d) Infinite energy, power $\lim\frac{1}{2T}\int_0^T1\,\mathrm{d} t=\frac12$: the signal is 1 for half of the time.
:::
:::
