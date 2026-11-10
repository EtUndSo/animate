---
title: Stage 12: Discrete-time random signals
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Random Signals
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Chapter 7: Random Signals
order: 3271300
summary: Everything also holds for sequences of random numbers, with sums instead of integrals.
tags: Discrete-time white noise
lang: en
---

<span class="anker" id="stufe-12"></span>

:::zweck
Everything also holds for sequences of random numbers, with sums instead of integrals.
:::

If a process band-limited to $f_\mathrm g$ is sampled with $T\le\frac{1}{2f_\mathrm g}$, the samples form a discrete-time process $s(n)$. Distributions, expected values and correlations are defined as before; the time averages are sums, for example $\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$. Through an LSI system with $h(n)$:

<span class="anker" id="gl-12-1"></span>
$$m_g=m_s\sum_nh(n),\qquad\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m),\qquad\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2, \tag{12.1}$$

with the periodic power spectral density $\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$ and $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$. __Discrete-time white noise__ has $\Phi_{ss,\mathrm a}=N$ and $\varphi_{ss}(m)=N\delta(m)$: successive numbers are uncorrelated. Unlike in the continuous-time case, its power is finite, $L_s=N$.

::::beispiel [Example 1] averaging two values
Uniformly distributed white noise ($\sigma_s^2=\frac1{12}$) passes through $h(n)=\frac12[\delta(n)+\delta(n-1)]$, that is, $g(n)=\frac12[s(n)+s(n-1)]$. With $\varphi^E_{hh}=\frac14\delta(m+1)+\frac12\delta(m)+\frac14\delta(m-1)$:

$$\varphi_{gg}(m)=\tfrac{\sigma_s^2}{4}\delta(m+1)+\tfrac{\sigma_s^2}{2}\delta(m)+\tfrac{\sigma_s^2}{4}\delta(m-1).$$

The variance is halved to $\frac{1}{24}$, and neighboring output values are now correlated (they share an input value). The output values have a triangular distribution, because each is half the sum of two independent, uniformly distributed numbers. A simulation with 200,000 numbers gives the variance 0.0415 instead of $\frac1{24}=0.0417$.
::::

::::beispiel [Example 2] recursive filter (AR(1) process)
White noise of variance $\sigma_s^2$ passes through $h(n)=b^n\varepsilon(n)$ ([Chapter 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)). With $\varphi^E_{hh}(m)=\sum_kb^kb^{k+|m|}=\frac{b^{|m|}}{1-b^2}$:

<span class="anker" id="gl-12-2"></span>
$$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|},\qquad\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}. \tag{12.2}$$

For $b=0.6$, the variance is $1.56$ times the input variance, and neighboring values have the correlation coefficient $0.6$. The closer $b$ is to 1, the stronger the low frequencies (Fig. [5](#abb-5)).

:::abbildung et3/k7ar 5
Power spectral densities of AR(1) processes, periodic with period 1. For $b=0.6$ the density ranges from 6.25 ($f=0$) to 0.39 ($f=\frac12$), for $b=0.9$ from 100 to 0.28.
:::
::::

:::aufgabe Exercise 12 ★★ AR(1) process
<span class="anker" id="aufg-12"></span>

Uniformly distributed white noise ($\sigma_s^2=\frac1{12}$) passes through $g(n)=s(n)+0.6\,g(n-1)$.

<ol class="al">

<li>

Compute the output variance and $\varphi_{gg}(1)/\varphi_{gg}(0)$.

</li>

<li>

Derive $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$ using the geometric series.

</li>

<li>

Is the output still uniformly distributed? What distribution do you roughly expect, and why?

</li>

</ol>

:::loesung
(a) $\sigma_g^2=\frac{1/12}{1-0.36}=0.130$, $\varphi_{gg}(1)/\varphi_{gg}(0)=b=0.6$. The simulation gives 0.130 and 0.600.

(b) For $m\ge0$: $\sum_{k\ge0}b^kb^{k+m}=b^m\sum_kb^{2k}=\frac{b^m}{1-b^2}$. The impulse ACF is even, so $b^{|m|}$ holds.

(c) No longer uniformly distributed: each output value is a weighted sum of many independent input values, $g(n)=\sum_kb^ks(n-k)$. By the central limit theorem, this is approximately Gaussian. For $b=0.6$, only a few terms contribute noticeably, so the approximation is rough, but the distribution is already clearly bell-shaped.
:::
:::
