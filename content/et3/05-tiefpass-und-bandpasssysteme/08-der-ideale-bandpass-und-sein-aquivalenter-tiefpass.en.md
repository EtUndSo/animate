---
title: Stage 7: The ideal bandpass and its equivalent lowpass
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Lowpass and Bandpass Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Chapter 5: Lowpass and Bandpass Systems
order: 3250800
summary: A bandpass passes a band around the center frequency f 0 .
tags: equivalent lowpass, symmetric
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
A bandpass passes a band around the center frequency $f_0$. This stage shows that it can be described completely by a lowpass and the frequency $f_0$.
:::

**Ideal bandpass.** Two rectangles of width $\Delta f$ at $\pm f_0$ ($f_0>\Delta f/2$):

<span class="anker" id="gl-7-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]\;\bullet\!\!-\!\!\circ\;h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\cdot2\cos(2\pi f_0t). \tag{7.1}$$

The impulse response is an oscillation at $f_0$ whose envelope is the impulse response of a lowpass with the bandwidth $\Delta f/2$. The modulation rule from [Chapter 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html) explains this: it is a lowpass whose spectrum is shifted to $\pm f_0$.

**Equivalent lowpass.** For a real impulse response, $H(-f)=H^*(f)$; the negative half contains nothing new. Keep only the positive frequencies, double them and shift them to the left by a carrier frequency $f_0$. The result is the __equivalent lowpass__ $H_T(f)$:

<span class="anker" id="gl-7-2"></span>
$$H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0),\qquad H_T(f)=0\ \text{for}\ f\le-f_0. \tag{7.2}$$

$H_T$ need not be symmetric about $f=0$, so its impulse response $h_T(t)$ can be complex. If there is an $f_0$ for which $H_T(-f)=H_T^*(f)$ holds (so that $h_T$ is real), the bandpass is called __symmetric__. For the ideal bandpass with $f_0$ at the center, $H_T(f)=2\operatorname{rect}(f/\Delta f)$ and $h_T(t)=2\Delta f\operatorname{si}(\pi\Delta f\,t)$, real and even. This is a special case: even symmetric bandpass filters generally have an imaginary part in the spectrum.

:::aufgabe Exercise 7 ★★ Equivalent lowpass with a different reference
<span class="anker" id="aufg-7"></span>

Ideal bandpass from 9 to 11 Hz.

<ol class="al">

<li>

Determine $H_T$ and $h_T$ for $f_0=10$ Hz.

</li>

<li>

Determine $H_T$ and $h_T$ for $f_0=9$ Hz. Why is $h_T$ complex now? Do both describe the same bandpass?

</li>

</ol>

:::loesung
(a) $f_0=10$ Hz: after the shift, the band lies symmetrically from $-1$ to $1$ Hz. $H_T=2\operatorname{rect}(f/2)$, $h_T=4\operatorname{si}(2\pi t)$, real.

(b) $f_0=9$ Hz: the band lies from 0 to 2 Hz. $H_T=2\operatorname{rect}\bigl(\frac{f-1}{2}\bigr)$, $h_T=4\operatorname{si}(2\pi t)\,\mathrm{e}^{\mathrm{j}2\pi t}$. Complex, because $H_T$ is not symmetric about $f=0$. Both describe the same bandpass: $\operatorname{Re}\{4\operatorname{si}(2\pi t)\mathrm{e}^{\mathrm{j}2\pi t}\mathrm{e}^{\mathrm{j}2\pi9t}\}=4\operatorname{si}(2\pi t)\cos(2\pi\cdot10t)$, the same as in (a) and as [(7.1)](#gl-7-1).
:::
:::
