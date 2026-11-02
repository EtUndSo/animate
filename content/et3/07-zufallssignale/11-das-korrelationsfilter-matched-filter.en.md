---
title: Stage 10: The matched filter (correlation filter)
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3271100
summary: A known pulse s(t) arrives corrupted by noise.
tags: matched filter, correlator
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
A known pulse $s(t)$ arrives corrupted by noise. With which filter does it become most clearly visible at the sampling instant $T$?
:::

**The approach.** The receiver input carries $s(t)+n(t)$ with white noise $n$. A filter $h$ delivers $y=g+n_e$ with the signal component $g=s*h$ and the noise component $n_e=n*h$. Sampling takes place at $T$. The signal-to-noise ratio there is

$$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}=\frac{E_s}{N_0}\cdot\underbrace{\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{\int|h|^2\mathrm{d}\tau\int|s(T-\tau)|^2\mathrm{d}\tau}}_{=|p|^2\le1}.$$

The fraction on the right is the square of a correlation coefficient ([Part 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)), between $h(\tau)$ and $s(T-\tau)$. It is at most 1, and it equals 1 exactly when both have the same shape.

:::satz Theorem 10.1 (Matched filter)
<span class="anker" id="satz-10-1"></span>

Against white noise, the best achievable signal-to-noise ratio is

<span class="anker" id="gl-10-1"></span>
$$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0},\qquad\text{achieved with}\qquad h(t)=a\,s(T-t),\quad H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}. \tag{10.1}$$
:::

⁠**How to read it:** The best impulse response is the signal itself, time-reversed and shifted by $T$: the __matched filter__ (correlation filter). Its output without noise is $g(t)=a\,\varphi^E_{ss}(t-T)$, the shifted ACF of the signal, and it is sampled exactly at its maximum. Surprisingly, the result depends only on the *energy* of the signal, not on its shape. A short, high pulse is as good as a long, flat one with the same energy. For the filter to be causal, $T$ must be at least the duration of the signal. A __correlator__ is equivalent: it multiplies the received signal by $s(t)$ and integrates over the duration of the signal.

:::aufgabe Exercise 10 ★★ A rectangular pulse in noise
<span class="anker" id="aufg-10"></span>

A rectangular pulse of height 1 V and duration 1 ms is received together with white noise of power spectral density $N_0=10^{-6}$ V$^2$/Hz.

<ol class="al">

<li>

What does the matched filter look like, and what $S_a/N$ (in dB) does it achieve?

</li>

<li>

What does the output look like without noise, and when must it be sampled?

</li>

<li>

The pulse is shortened to 0.25 ms, with the same height. What changes?

</li>

</ol>

:::loesung
(a) $h(t)=a\,s(T-t)$: again a rectangle of 1 ms, causal for $T\ge1$ ms. $E_s=1\,\mathrm{V^2}\cdot1\,\mathrm{ms}=10^{-3}$ V$^2$s, so $S_a/N=10^{-3}/10^{-6}=1000$, that is, 30 dB.

(b) The ACF of the rectangle, a triangle of width 2 ms, shifted by $T$: it rises from $t=T-1$ ms and reaches its maximum at $t=T$. For $T=1$ ms, you sample exactly at the end of the pulse; at that moment the filter has “seen” all of it.

(c) $E_s$ drops to a quarter, $S_a/N=250$, that is, 24 dB, 6 dB worse. Only the energy counts. At the same height, a shorter pulse means less energy.
:::
:::
