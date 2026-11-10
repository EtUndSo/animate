---
title: Stage 10: Quadrature circuit and bandpass sampling
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Lowpass and Bandpass Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Chapter 5: Lowpass and Bandpass Systems
order: 3251100
summary: How are the quadrature components obtained in practice?
tags: 
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
How are the quadrature components obtained in practice? And how many samples does a bandpass signal need?
:::

**Quadrature circuit.** If you multiply a bandpass signal by $\cos(2\pi f_0t)$ and filter it with a lowpass, $\frac12s_{Tr}$ remains. With $-\sin(2\pi f_0t)$, $\frac12s_{Ti}$ remains. The reason is trigonometric:

$$s\cos=s_{Tr}\cos^2-s_{Ti}\sin\cos=\tfrac12s_{Tr}+\underbrace{\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)}_{\text{at }2f_0,\text{ removed by the lowpass}},$$

and likewise $-s\sin=\frac12s_{Ti}+(\text{components at }2f_0)$. The prerequisite is that the band ends below $2f_0$. In the lowpass domain you then filter with four lowpass filters ($h_{Tr}$, $\pm h_{Ti}$) according to [(9.1)](bandpasssignal-durch-bandpasssystem.html#gl-9-1). At the output you modulate back onto the carrier according to [(8.2)](komplexe-hullkurve-und-quadraturkomponenten.html#gl-8-2), or you form the envelope $\sqrt{g_{Tr}^2+g_{Ti}^2}$ (Fig. [6](#abb-6)).

:::abbildung et3/k5quadratur 6
Quadrature demodulator: it extracts the two quadrature components, that is, the complex envelope, from a bandpass signal.
:::

**Sampling theorem for bandpass signals.** With respect to the center frequency, a bandpass signal of bandwidth $\Delta f$ has quadrature components that are lowpass signals up to $\Delta f/2$. Each of them can be sampled at $1/T=\Delta f$:

<span class="anker" id="gl-10-1"></span>
$$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t),\qquad T=\frac{1}{\Delta f}. \tag{10.1}$$

In total you need $2\Delta f$ values per second, as many as for a lowpass signal with the cutoff frequency $\Delta f$. So what matters is the bandwidth, not the highest frequency.

:::aufgabe Exercise 9 ★★ Sampling a radio signal
<span class="anker" id="aufg-9"></span>

A signal occupies the band from 10.0 to 10.2 MHz.

<ol class="al">

<li>

What sampling rate would the ordinary sampling theorem require?

</li>

<li>

With the quadrature circuit, how many samples per second suffice in total, and at what rate is each branch sampled?

</li>

</ol>

:::loesung
(a) At least $2\cdot10.2=20.4$ MHz.

(b) $\Delta f=0.2$ MHz. Each branch is sampled at 0.2 MHz ($T=5$ µ s), together 0.4 MHz, about fifty times less.
:::
:::
