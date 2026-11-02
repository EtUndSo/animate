---
title: Key points
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Correlation Functions
order: 3260900
summary: How similar are two signals, and how is the energy distributed over frequency?
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

The similarity of two signals is measured by the integral of their product. The correlation function does this for every shift $\tau$; it is a convolution with the flipped signal.

</li>

<li>

The Fourier transform of the autocorrelation function is the energy spectral density $|S(f)|^2$. At $\tau=0$ it equals the energy (Parseval).

</li>

<li>

An LTI system multiplies energy spectral densities by $|H(f)|^2$ and convolves autocorrelation functions with the autocorrelation function of $h$.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

$E_s=\int|s|^2\mathrm{d} t$; $L_s=\lim\frac{1}{2T}\int_{-T}^T|s|^2\mathrm{d} t$.

</li>

<li>

$p_{sg}=\frac{\int s^*g\,\mathrm{d} t}{\sqrt{E_sE_g}}$, $|p|\le1$, $p=0$: orthogonal.

</li>

<li>

$\varphi^E_{sg}(\tau)=\int s^*(t)g(t+\tau)\mathrm{d} t=s^*(-\tau)*g(\tau)$; $\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau)$.

</li>

<li>

ACF: even (for real signals), maximum $\varphi^E_{ss}(0)=E_s$, twice the duration.

</li>

<li>

$\varphi^E_{ss}\leftrightarrow|S|^2$, $\varphi^E_{sg}\leftrightarrow S^*G$; Parseval $\int|s|^2\mathrm{d} t=\int|S|^2\mathrm{d} f$.

</li>

<li>

Wiener–Lee: $\varphi^E_{gg}=\varphi^E_{ss}*\varphi^E_{hh}$, $|G|^2=|S|^2|H|^2$; $\varphi^E_{sg}=\varphi^E_{ss}*h$.

</li>

<li>

Bandpass: $\varphi^E_{sgT}=\frac12s_T^*(-\tau)*g_T(\tau)$.

</li>

<li>

Discrete: $\varphi(m)=\sum s^*(n)g(n+m)$, $\leftrightarrow|S_\mathrm a|^2$; periodic: $S_d^*G_d$.

</li>

</ul>
:::

**One principle behind all the results.** Correlation is convolution with a flipped signal. That is why all the tools of convolution apply:

| Result | Where it comes from |
|---|---|
| Correlation coefficient | energy of the difference of two normalized signals (Stage [2](ahnlichkeit-messen-der-korrelationskoeffizient.html#stufe-2)) |
| Correlation product | convolution with the flipped, conjugated signal (Stage [3](korrelationsfunktion-und-korrelationsprodukt.html#stufe-3)) |
| ACF even, maximum at 0 | flipping, and a signal is most similar to itself (Stage [3](korrelationsfunktion-und-korrelationsprodukt.html#stufe-3)) |
| Energy spectral density, Parseval | flipping and conjugating become $S^*$, convolution becomes a product (Stage [4](energiedichtespektrum.html#stufe-4)) |
| Wiener–Lee | associative law of convolution (Stage [5](korrelation-und-lti-systeme.html#stufe-5)) |
| Discrete-time, periodic, DFT | the same calculation with sums (Stage [7](zeitdiskrete-und-periodische-korrelation.html#stufe-7)) |
