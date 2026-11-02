---
title: Stage 2: The spectrum of the sampled signal
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Sampling and Discrete-Time Systems
order: 3240300
summary: What does sampling do to the spectrum?
tags: spectral images
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
What does sampling do to the spectrum? This stage shows that it repeats periodically.
:::

**The idea.** Two oscillations whose frequencies differ by a multiple of the sampling rate $1/T$ have the same samples:

$$\mathrm{e}^{\mathrm{j}2\pi(f_0+k/T)nT}=\mathrm{e}^{\mathrm{j}2\pi f_0nT}\cdot\underbrace{\mathrm{e}^{\mathrm{j}2\pi kn}}_{=1}.$$

The samples cannot tell them apart. Therefore the spectrum of the samples must look the same at $f_0$ and at $f_0+k/T$. It is periodic.

:::satz Theorem 2.1 (Spectrum of the ideally sampled signal)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$S_\mathrm a(f)=\frac1T\sum_{k=-\infty}^{\infty}S\Bigl(f-\frac kT\Bigr)\qquad(T>0). \tag{2.1}$$
:::

⁠**How to read it:** the spectrum of the original appears with its shape unchanged, but with the factor $1/T$ and repeated at every multiple of the sampling rate. The copies are called __spectral images__.

:::herleitung Spectrum of the sampled signal
Multiplication becomes convolution ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), and the spectrum of the Dirac comb is again a comb:

$$s(t)\cdot\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;S(f)*\frac1T\sum_k\delta\Bigl(f-\frac kT\Bigr)=\frac1T\sum_kS\Bigl(f-\frac kT\Bigr).$$

Convolution with a shifted Dirac impulse shifts the spectrum.
:::

:::abbildung et3/k4spektrum 1
A spectrum up to $f_\mathrm g=300$ Hz (blue, triangular for clarity), sampled. Top, at 1 kHz: the copies at multiples of 1 kHz lie apart. Bottom, at 500 Hz: copies spaced 500 Hz apart overlap, and the sum (red) is no longer the original. The factor $1/T$ is omitted.
:::

:::frage How does the spectrum “know” that the signal was sampled? The signal between the sampling points is simply gone, after all.
That is exactly why. Between the sampling points the sampled signal is zero, except at the impulses. Every oscillation that has the same values at all points $nT$ describes this signal equally well. The spectrum cannot decide between them and contains all of them: the original and its copies at every multiple of $1/T$.
:::
