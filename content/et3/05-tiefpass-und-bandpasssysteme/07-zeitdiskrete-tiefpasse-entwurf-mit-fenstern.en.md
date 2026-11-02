---
title: Stage 6: Discrete-time lowpass filters, window design
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Lowpass and Bandpass Systems
order: 3250700
summary: How do you design a digital lowpass?
tags: 
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
How do you design a digital lowpass? Exactly like the causal analog one: take the ideal lowpass, delay it, truncate it with a window.
:::

The ideal discrete-time lowpass has the periodically repeated rectangular frequency response and the impulse response

$$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn),$$

so in the reference model ($f_\mathrm g=0.2$) $h(0)=0.4$, $h(\pm1)=0.303$, $h(\pm2)=0.094$, $h(\pm3)=-0.062$. It, too, is not causal. You multiply it by a window $w(n)$ of $2N+1$ values, shift it by $N$ and obtain an FIR filter with linear phase. The window determines the result (Fig. [4](#abb-4)):

<ul>

<li>

⁠**Rectangular window:** sharpest transition, but high side lobes. In the reference model ($N=10$), the stopband from $f=0.3$ on still reaches $-26.6$ dB, and the passband fluctuates by about $\pm0.5$ dB.

</li>

<li>

⁠**Hann window:** softer transition, but a much deeper stopband: from $f=0.3$ on at most $-45.9$ dB, passband flat to within $0.05$ dB.

</li>

</ul>

The reason is the same as for the short-time Fourier transform in [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): the spectrum of the window is convolved with the ideal, and the hard edges of the rectangle produce slowly decaying side lobes.

:::abbildung et3/k5fenster 4
Magnitude response of two FIR lowpass filters with $f_\mathrm g=0.2$ and 21 coefficients. Rectangular window: steep edge, from $f=0.3$ on attenuation only down to $-26.6$ dB. Hann window: shallower edge, from $f=0.3$ on at most $-45.9$ dB.
:::

:::aufgabe Exercise 6 ★ Half-band filter
<span class="anker" id="aufg-6"></span>

Compute the coefficients $h(0)$ to $h(3)$ of the ideal discrete-time lowpass with $f_\mathrm g=0.25$. What do you notice, and why does this save computation in an FIR filter?

:::loesung
$h(n)=0.5\operatorname{si}(\pi n/2)$: $h(0)=0.5$, $h(\pm1)=\frac1\pi=0.318$, $h(\pm2)=0$, $h(\pm3)=-\frac{1}{3\pi}=-0.106$. All even coefficients except $h(0)$ are zero, because $\sin(\pi n/2)=0$ for even $n$. In the FIR filter these multiplications are dropped, almost half of them.
:::
:::
