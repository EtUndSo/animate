---
title: Stage 2: The ideal lowpass
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Lowpass and Bandpass Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Chapter 5: Lowpass and Bandpass Systems
order: 3250300
summary: The ideal lowpass passes all frequencies up to f mathrm g unchanged and blocks all frequencies above.
tags: signal duration
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
The ideal lowpass passes all frequencies up to $f_\mathrm g$ unchanged and blocks all frequencies above. This stage shows what this sharp cutoff means in the time domain.
:::

:::satz Theorem 2.1 (Ideal lowpass)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\qquad\bullet\!\!-\!\!\circ\qquad h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt). \tag{2.1}$$
:::

⁠**How to read it:** the impulse response extends to infinity in both directions. So the ideal lowpass is *not causal*: it would have to respond to an impulse before the impulse arrives. It is a mathematical limiting object that can only be approximated (Stages [4](kausale-naherung.html#stufe-4), [6](zeitdiskrete-tiefpasse-entwurf-mit-fenstern.html#stufe-6)).

**Duration and bandwidth.** The __signal duration__ $t_m$ of an impulse response is taken to be the width of a rectangle with the same height $h_{\max}$ and the same area:

<span class="anker" id="gl-2-2"></span>
$$t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}. \tag{2.2}$$

For the ideal lowpass, $H(0)=1$ and $h_{\max}=2f_\mathrm g$, so $t_m=\frac{1}{2f_\mathrm g}$ and $f_\mathrm g\cdot t_m=\frac12$. In general, lowpass filters satisfy $f_\mathrm g\cdot t_m=\text{const.}$: double the bandwidth means half the response duration. This is the similarity theorem from [Chapter 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html).

**Overshoot.** For the si function, the ratio of the side maximum with the largest magnitude, $a_1$, to the main maximum $a_0$ is

$$\ddot u=\Bigl|\frac{a_1}{a_0}\Bigr|=21.7\,\%,$$

independent of $f_\mathrm g$ (the first side minimum of $\operatorname{si}(\pi u)$ lies at $u=1.43$ and is $-0.217$). Changing $f_\mathrm g$ only compresses the curve; it does not change its shape.

:::aufgabe Exercise 2 ★ Ideal lowpass for speech
<span class="anker" id="aufg-2"></span>

An ideal lowpass with $f_\mathrm g=4$ kHz. What are the signal duration of the impulse response and the overshoot? What changes for $f_\mathrm g=8$ kHz?

:::loesung
$t_m=\frac{1}{2f_\mathrm g}=125$ µ s, overshoot 21.7 %. At 8 kHz the signal duration halves to 62.5 µ s. The overshoot remains 21.7 %, because the impulse response is only compressed.
:::
:::
