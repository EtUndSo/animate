---
title: Key points
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Lowpass and Bandpass Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Chapter 5: Lowpass and Bandpass Systems
order: 3251400
summary: Distortionless transmission, ideal lowpass, complex envelope and group delay
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

Undistorted means: only amplified and delayed. This requires a constant magnitude and a phase that falls linearly with frequency.

</li>

<li>

A sharply band-limited (ideal) lowpass is not causal, overshoots by about 9 % at steps and needs a rise time of $1/(2f_\mathrm g)$. Softer edges reduce the overshoot at the expense of sharpness.

</li>

<li>

A bandpass signal is a lowpass signal (the complex envelope) on a carrier. You calculate with the envelope as with a lowpass signal: it is delayed by the group delay, the carrier by the phase delay.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Distortionless: $h=h_0\delta(t-t_0)$, $H=h_0\mathrm{e}^{-\mathrm{j}2\pi t_0f}$: constant magnitude, linear phase.

</li>

<li>

$a=-20\lg|H|$ dB; $t_\mathrm p=-\frac{\varphi}{2\pi f}$; $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}$.

</li>

<li>

Ideal lowpass: $\operatorname{rect}(f/2f_\mathrm g)\leftrightarrow2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$, not causal; $f_\mathrm g t_m=\frac12$; overshoot 21.7 % (impulse), 8.95 % (step).

</li>

<li>

Step response $\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$, $\operatorname{Si}(\infty)=\frac\pi2$, rise time $\frac{1}{2f_\mathrm g}$.

</li>

<li>

Truncating the impulse response $=$ convolution in the spectrum; smooth windows: deeper stopband, shallower edge.

</li>

<li>

Pulse-shaping filter: $T\operatorname{rect}(Tf)[1+\cos(2\pi Tf)]$, little overshoot.

</li>

<li>

$H(f)=\frac12H_T(f-f_0)+\frac12H_T^*(-f-f_0)$; $s=\operatorname{Re}\{s_T\mathrm{e}^{\mathrm{j}2\pi f_0t}\}=s_{Tr}\cos-s_{Ti}\sin$; $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

</li>

<li>

$g_T=\frac12s_T*h_T$; envelope delayed by $t_\mathrm g$, carrier by $t_\mathrm p$.

</li>

<li>

Bandpass sampling: $2\Delta f$ values per second; digital highpass: $(-1)^nh_{\mathrm{TP}}(n)$.

</li>

</ul>
:::

**One principle behind all the results.**

| Result | Where it comes from |
|---|---|
| Distortionless system | every oscillation amplified equally and delayed by the same time (Stage [1](das-verzerrungsfreie-system.html#stufe-1)) |
| Phase and group delay | delay of the carrier and of the envelope, respectively (Stages [1](das-verzerrungsfreie-system.html#stufe-1), [11](phasen-und-gruppenlaufzeit-beim-bandpass.html#stufe-11)) |
| Signal duration $\cdot$ bandwidth $=$ const. | similarity theorem (Stage [2](der-ideale-tiefpass.html#stufe-2)) |
| Overshoot 21.7 % and 8.95 % | side lobes of the si function, Gibbs (Stages [2](der-ideale-tiefpass.html#stufe-2), [3](sprungantwort-und-einschwingzeit.html#stufe-3)) |
| Causal approximation, window design | truncating the impulse response = convolution in the spectrum (Stages [4](kausale-naherung.html#stufe-4), [6](zeitdiskrete-tiefpasse-entwurf-mit-fenstern.html#stufe-6)) |
| Pulse-shaping filter | soft edge in the spectrum, rapidly decaying impulse response (Stage [5](echomethode-und-pulsformfilter.html#stufe-5)) |
| Equivalent lowpass, complex envelope | shift the positive frequencies to zero (Stages [7](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#stufe-7), [8](komplexe-hullkurve-und-quadraturkomponenten.html#stufe-8)) |
| Quadrature circuit, bandpass sampling | calculate the bandpass in the lowpass domain (Stage [10](quadraturschaltung-und-bandpass-abtastung.html#stufe-10)) |
