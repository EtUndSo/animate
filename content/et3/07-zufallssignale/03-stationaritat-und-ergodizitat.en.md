---
title: Stage 2: Stationarity and ergodicity
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3270300
summary: You never have an infinite ensemble, usually only a single signal.
tags: stationary, ergodic
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
You never have an infinite ensemble, usually only a single signal. When is that enough?
:::

A process is called __stationary__ if none of its averages change when all observation times are shifted by the same time $t_0$:

<span class="anker" id="gl-2-1"></span>
$$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\},\qquad\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2+t_0)]\}. \tag{2.1}$$

Then the mean value $m_s=\mathrm E\{s(t)\}$ is a constant, and the ACF depends only on the difference $\tau=t_2-t_1$: $\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$. A stationary process is called __ergodic__ if, in addition, every time average of a sample function equals the corresponding ensemble average:

<span class="anker" id="gl-2-2"></span>
$$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t\quad\text{for every }k. \tag{2.2}$$

⁠**How to read it:** Stationary means that the statistics do not change with time. Ergodic means that a single sample function, observed for a long time, shows in the course of time everything that the whole ensemble shows. The noise of a resistor at constant temperature is ergodic. Only for this reason can noise be characterized with a single measuring instrument.

:::frage Is every stationary process also ergodic?
No. Example: each sample function is a constant whose value is drawn at random once, ${}^ks(t)=c_k$. The process is stationary, because nothing depends on $t$. But the time average of a sample function is $c_k$, which is different for every sample function and is not the ensemble average. A single sample function never “sees” the other values.
:::
