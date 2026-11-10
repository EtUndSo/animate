---
title: Key points
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Random Signals
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Chapter 7: Random Signals
order: 3271400
summary: Mean values, distributions, power spectral density, noise in systems and the optimal receiver
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

A random signal is described by averages: mean value, power, variance, autocorrelation function and probability density function. For ergodic processes, they may be determined from a single, long signal.

</li>

<li>

The Fourier transform of the autocorrelation function is the power spectral density. An LTI system multiplies it by $|H(f)|^2$, exactly as for energy signals ([Chapter 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)).

</li>

<li>

Against white noise, the matched filter $h(t)=s(T-t)$ is optimal. It achieves the signal-to-noise ratio $E_s/N_0$, regardless of the signal shape.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Ensemble average $\mathrm E\{\cdot\}$; stationary: independent of shifts; ergodic: time average $=$ ensemble average.

</li>

<li>

$m_s$ (DC component), $L_s=\mathrm E\{s^2\}$ (power), $\sigma_s^2=L_s-m_s^2$ (AC power).

</li>

<li>

ACF: $\varphi_{ss}(0)=L_s$, even, maximum at 0; covariance $\mu=\varphi-m^2$; sum: $\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0)$.

</li>

<li>

$P_s(x)=\mathrm{Prob}[s\le x]$, $p_s=P_s'$; $m_s=\int xp_s$, $L_s=\int x^2p_s$; uniform distribution $\sigma^2=a^2/12$.

</li>

<li>

Characteristic curve: $p_g(y)|\mathrm{d} y|=p_s(x)|\mathrm{d} x|$; quantization error $\Delta^2/12$, 6 dB per bit.

</li>

<li>

Independent $\Rightarrow$ uncorrelated; sum of independent variables: $p_s=p_f*p_g$; Gaussian: $\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{e}^{-(x-m)^2/2\sigma^2}$.

</li>

<li>

LTI: $m_g=m_sH(0)$, $\varphi_{gg}=\varphi_{ss}*\varphi^E_{hh}$, $\Phi_{gg}=\Phi_{ss}|H|^2$, $L=\int\Phi\,\mathrm{d} f$.

</li>

<li>

White: $\Phi=N_0$, $\varphi=N_0\delta$; thermal $\mathrm E\{u^2\}=4kTRf_\mathrm g$, $kT\approx4$ pW/GHz.

</li>

<li>

Matched filter: $h=a\,s(T-t)$, $(S_a/N)_{\max}=E_s/N_0$; $P_{e,\min}=\frac12\operatorname{erfc}\sqrt{E_s/(8N_0)}$.

</li>

</ul>
:::

**One principle behind all the results.** You replace the unknown signal by its averages, and averages are linear:

| Result | Where it comes from |
|---|---|
| Mean value, power, variance | ensemble average and time average (Stages [1](der-zufallsprozess.html#stufe-1)–[3](mittelwert-leistung-varianz.html#stufe-3)) |
| ACF, covariance, CCF | average over products of values at two instants (Stage [4](autokorrelation-kovarianz-und-kreuzkorrelation.html#stufe-4)) |
| Probability density function | fraction of time or of the ensemble below a threshold (Stage [5](verteilungsfunktion-und-verteilungsdichte.html#stufe-5)) |
| Sum of independent variables | convolution of the densities, hence Gaussian (Stages [6](verbundverteilung-unabhangigkeit-unkorreliertheit.html#stufe-6), [7](die-gau-verteilung.html#stufe-7)) |
| Power spectral density, Wiener–Lee | linearity of the expected value in the convolution integral (Stage [8](zufallssignale-in-lti-systemen-leistungsdichte.html#stufe-8)) |
| White noise | constant power spectral density, ACF $=N_0\delta$ (Stage [9](weies-rauschen-und-thermisches-rauschen.html#stufe-9)) |
| Matched filter | Cauchy–Schwarz: the correlation is greatest with the signal itself (Stage [10](das-korrelationsfilter-matched-filter.html#stufe-10)) |
| Error probability | area under a Gaussian curve beyond the threshold (Stage [11](fehlerwahrscheinlichkeit-beim-binarempfang.html#stufe-11)) |
