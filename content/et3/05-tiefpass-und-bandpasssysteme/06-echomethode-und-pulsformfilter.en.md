---
title: Stage 5: Echo method and pulse-shaping filters
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Lowpass and Bandpass Systems
order: 3250600
summary: How do you design a lowpass with less overshoot?
tags: echo, raised-cosine filter
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
How do you design a lowpass with less overshoot? You assemble the impulse response from shifted si functions and choose their weights.
:::

**Echo method.** By the sampling theorem, every impulse response of a lowpass up to $f_\mathrm g=\frac{1}{2T}$ is an si series:

<span class="anker" id="gl-5-1"></span>
$$h(t)=\sum_nh(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$h(nT)=\int_{-f_\mathrm g}^{f_\mathrm g}H(f)\,\mathrm{e}^{\mathrm{j}2\pi nTf}\,\mathrm{d} f. \tag{5.2}$$

Each sample $h(nT)$ is an __echo__: an si function shifted by $nT$. In the spectrum this becomes a Fourier series in $f$. If $h$ is real and even, $H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\cos(2\pi nTf)\bigr]$.

**Pulse-shaping filter.** Two echoes with the amplitude $a$ at a distance of $\pm T$ are added to the main component $\operatorname{si}(\pi t/T)$. For $a=\frac12$ the side oscillations largely cancel, and the spectrum gets a cosine-shaped, soft edge:

<span class="anker" id="gl-5-3"></span>
$$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t+T}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t-T}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]. \tag{5.3}$$

This is the __raised-cosine filter__ (cosine roll-off filter). Its overshoot is 2.7 % instead of 21.7 %; in exchange, the main lobe is twice as wide (first zero at $2T$ instead of $T$). Figure [3](#abb-3) shows both impulse responses normalized to the same area.

:::abbildung et3/k5pulsform 3
Impulse responses of the ideal lowpass and of the pulse-shaping filter (both with the area $T$). The pulse-shaping filter decays much faster: its largest side maximum is 2.7 % of the main maximum instead of 21.7 %.
:::

**Transversal filter (tapped delay line).** A sum of delayed, weighted copies is built with a chain of delay elements whose taps are weighted and added. So that no element has to reach into the future, everything is delayed together. This is the same structure as an FIR filter ([Part 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)).

:::aufgabe Exercise 5 ★★ The raised-cosine filter
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Derive $H(f)$ in [(5.3)](#gl-5-3) from [(5.1)](#gl-5-1).

</li>

<li>

What is the value of $H$ at $f=0$ and at $f=f_\mathrm g=\frac{1}{2T}$? Why is the edge smooth there?

</li>

</ol>

:::loesung
(a) At $t=mT$, $\operatorname{si}(\pi(t\pm T)/T)$ equals 1 only for $m=\mp1$ and is zero otherwise. So $h(0)=1$, $h(\pm T)=\frac12$, and all other $h(nT)=0$. By [(5.1)](#gl-5-1): $H=T\operatorname{rect}(Tf)\bigl[1+\frac12\mathrm{e}^{\mathrm{j}2\pi Tf}+\frac12\mathrm{e}^{-\mathrm{j}2\pi Tf}\bigr]=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]$.

(b) $H(0)=2T$, $H(\frac{1}{2T})=T(1+\cos\pi)=0$. The slope $-2\pi T^2\sin(2\pi Tf)$ is also zero at $f=\frac{1}{2T}$. The frequency response goes to zero without a jump and without a kink. The smoother the spectrum, the faster the impulse response decays ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).
:::
:::
