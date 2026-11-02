---
title: Key points
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Sampling and Discrete-Time Systems
order: 3241300
summary: From the continuous signal to a sequence of numbers: sampling theorem, discrete convolution, DFT, FFT and z-transform
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

Sampling is multiplication by a Dirac comb. In the spectrum this becomes a convolution with a comb: the spectrum repeats periodically with the sampling rate.

</li>

<li>

If the repetitions do not lie on top of each other (sampling rate above twice the highest frequency), the signal can be recovered exactly with an ideal low-pass filter. Otherwise aliasing occurs.

</li>

<li>

The same tools apply to sequences of numbers as to functions: convolution as a sum, a Fourier transform with a periodic spectrum, the DFT as its samples, the z-transform as the counterpart of the Laplace transform.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Ideal sampling: $s_\mathrm a=\sum s(nT)\delta(t-nT)$; spectrum $\frac1T\sum_kS(f-k/T)$, periodic with $1/T$.

</li>

<li>

Sampling theorem: $f_\mathrm A\ge2f_\mathrm g$; reconstruction $s(t)=\sum s(nT)\operatorname{si}(\pi(t-nT)/T)$; otherwise aliasing.

</li>

<li>

Discrete in one domain means periodic in the other.

</li>

<li>

Discrete convolution $g(n)=\sum_ms(m)h(n-m)$; $h(n)=\operatorname{Tr}\{\delta(n)\}$; stable: $\sum|h(n)|<\infty$.

</li>

<li>

Recursive system $g(n)=s(n)+bg(n-1)$: $h(n)=b^n\varepsilon(n)$, $H_\mathrm a=\frac{1}{1-b\mathrm{e}^{-\mathrm{j}2\pi f}}$.

</li>

<li>

$S_\mathrm a(f)=\sum s(n)\mathrm{e}^{-\mathrm{j}2\pi nf}$, period 1; $s(n)=\int_{-1/2}^{1/2}S_\mathrm a\mathrm{e}^{\mathrm{j}2\pi nf}\mathrm{d} f$.

</li>

<li>

DFT: $S_d(k)=\sum_{n=0}^{M-1}s_d(n)\mathrm{e}^{-\mathrm{j}2\pi kn/M}$, $s_d=\frac1M\sum S_d\mathrm{e}^{\mathrm{j}2\pi kn/M}$; FFT $\approx M\,\mathrm{lb}\,M$; circular convolution $\leftrightarrow S_dH_d$.

</li>

<li>

Downsampling stretches the band (aliasing if $cf_\mathrm g>\frac12$), upsampling creates spectral images.

</li>

<li>

$S(z)=\sum s(n)z^{-n}$; $z^{-n_0}$ = delay; $H(z)=\frac{\sum a_qz^{-q}}{1-\sum b_pz^{-p}}$; causal and stable: all poles in $|z|<1$.

</li>

</ul>
:::

**One principle behind all the results: discrete in one domain means periodic in the other.**

| Result | Where it comes from |
|---|---|
| Periodic spectrum after sampling | time discrete $\Rightarrow$ spectrum periodic (Stage [2](das-spektrum-des-abgetasteten-signals.html#stufe-2)) |
| Sampling theorem, aliasing | whether the periodic copies overlap (Stage [3](abtasttheorem-und-ruckgewinnung.html#stufe-3)) |
| si interpolation | an ideal low-pass filter cuts out one copy (Stage [3](abtasttheorem-und-ruckgewinnung.html#stufe-3)) |
| Fourier series | spectrum discrete $\Rightarrow$ time periodic (Stage [4](abtastung-im-frequenzbereich.html#stufe-4)) |
| Discrete convolution | convolution integral over Dirac-weighted samples (Stage [5](zeitdiskrete-signale-und-die-diskrete-faltung.html#stufe-5)) |
| Discrete-time Fourier transform | spectrum of the samples, periodic with period 1 (Stage [7](fourier-transformation-zeitdiskreter-signale.html#stufe-7)) |
| DFT | both discrete $\Rightarrow$ both periodic (Stage [8](die-diskrete-fourier-transformation-dft.html#stufe-8)) |
| Decimation, interpolation | sampling an already sampled sequence (Stage [10](abtastrate-andern-dezimation-und-interpolation.html#stufe-10)) |
| z-transform | the Laplace idea for sequences: first weight, then transform (Stage [11](die-z-transformation.html#stufe-11)) |
