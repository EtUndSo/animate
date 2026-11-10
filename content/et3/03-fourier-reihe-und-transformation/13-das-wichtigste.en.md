---
title: Key points
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Fourier Series and Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Chapter 3: Fourier Series and Transform
order: 3231300
summary: Every signal as a superposition of oscillations
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

A periodic signal is a sum of oscillations at multiples of the fundamental frequency (Fourier series); a non-repeating signal is an integral over all frequencies (Fourier integral).

</li>

<li>

Every oscillation $\mathrm{e}^{\mathrm{j}2\pi ft}$ is an eigenfunction: an LTI system multiplies it by $H(f)$, and that is why convolution becomes the product $G(f)=S(f)\,H(f)$.

</li>

<li>

All the rules of calculation (shift, stretching, modulation, symmetry) follow from what the respective operation does to a single oscillation.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

$\mathrm{e}^{\mathrm{j}2\pi ft}*h=H(f)\mathrm{e}^{\mathrm{j}2\pi ft}$; $H(f)=\int h\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$.

</li>

<li>

Series: $s_p=\sum S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$, $S_p(k)=\frac1T\int_Ts_p\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t$; real: $S_p(-k)=S_p^*(k)$.

</li>

<li>

Parseval: $\frac1T\int_T|s_p|^2=\sum|S_p(k)|^2$; Gibbs: about 9 % overshoot at jumps; LTI: $G_p(k)=S_p(k)H(kF)$.

</li>

<li>

$S(f)=\int s\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, $s=\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$; $s*h\leftrightarrow SH$, $s_1s_2\leftrightarrow S_1*S_2$.

</li>

<li>

Real: $S(-f)=S^*(f)$; even $\leftrightarrow\operatorname{Re} S$, odd $\leftrightarrow\mathrm{j}\operatorname{Im} S$.

</li>

<li>

$s(bt)\leftrightarrow\frac1{|b|}S(f/b)$; $s(t-t_0)\leftrightarrow S\mathrm{e}^{-\mathrm{j}2\pi ft_0}$; $\frac{\mathrm{d}}{\mathrm{d} t}\leftrightarrow\mathrm{j}2\pi f$; $\mathrm{e}^{\mathrm{j}2\pi Ft}s\leftrightarrow S(f-F)$; $S(t)\leftrightarrow s(-f)$.

</li>

<li>

$\operatorname{rect}(t/T)\leftrightarrow|T|\operatorname{si}(\pi Tf)$; $\Lambda\leftrightarrow\operatorname{si}^2$; $\delta\leftrightarrow1$; $1\leftrightarrow\delta(f)$; $\cos\leftrightarrow\frac12[\delta(f+F)+\delta(f-F)]$.

</li>

<li>

Comb $\leftrightarrow$ comb: $\sum\delta(t-nT)\leftrightarrow\frac1{|T|}\sum\delta(f-k/T)$; $\varepsilon\leftrightarrow\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$.

</li>

<li>

Hilbert: $h=\frac{1}{\pi t}$, $H=-\mathrm{j}\operatorname{sgn}(f)$; $s_+=\frac12(s+\mathrm{j}\hat s)$, $s=2\operatorname{Re} s_+$.

</li>

</ul>
:::

**One principle behind all the results.**

| Result | Where it comes from |
|---|---|
| Frequency response $H(f)$ | eigenvalue of the oscillation $\mathrm{e}^{\mathrm{j}2\pi ft}$ (Stage [1](schwingungen-als-eigenfunktionen.html#stufe-1)) |
| Fourier series, only multiples of $F$ | only these oscillations have the period $T$ (Stage [2](periodische-signale-die-fourier-reihe.html#stufe-2)) |
| Analysis formula of the series | oscillations of different frequencies are orthogonal (Stage [2](periodische-signale-die-fourier-reihe.html#stufe-2)) |
| Parseval, Gibbs, LTI with periodic input | each harmonic on its own (Stage [3](leistung-konvergenz-und-lti-systeme.html#stufe-3)) |
| Fourier integral | period $\to\infty$, the lines move closer together (Stage [4](vom-periodischen-zum-einmaligen-signal.html#stufe-4)) |
| $S(-f)=S^*(f)$ for real signals | oscillations occur in conjugate pairs (Stage [5](symmetrien-im-signal-und-im-spektrum.html#stufe-5)) |
| Shift, stretching, derivative, modulation | what the operation does to $\mathrm{e}^{\mathrm{j}2\pi ft}$ (Stage [6](die-rechenregeln-theoreme.html#stufe-6)) |
| Symmetry (duality) | forward and inverse transform differ only in the sign (Stage [6](die-rechenregeln-theoreme.html#stufe-6)) |
| Line spectra, Dirac comb, step | limiting cases with Dirac impulses (Stage [8](singulare-signale-und-linienspektren.html#stufe-8)) |
| Hilbert transform | a causal signal is determined by one half (Stage [9](hilbert-transformation-und-analytisches-signal.html#stufe-9)) |
| Short-time Fourier transform | spectrum of a segment (Stage [10](kurzzeit-fourier-transformation.html#stufe-10)) |
