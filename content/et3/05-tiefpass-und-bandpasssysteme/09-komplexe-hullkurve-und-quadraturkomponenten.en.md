---
title: Stage 8: Complex envelope and quadrature components
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Lowpass and Bandpass Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Chapter 5: Lowpass and Bandpass Systems
order: 3250900
summary: What holds for systems also holds for signals: a bandpass signal is a lowpass signal on a carrier.
tags: complex envelope, complex carrier, quadrature components, envelope
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
What holds for systems also holds for signals: a bandpass signal is a lowpass signal on a carrier. This stage shows the different ways of writing this down.
:::

Transforming [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) back with the modulation rule gives $h(t)=\frac12h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}+\frac12\bigl[h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr]^*$, and so, because $z+z^*=2\operatorname{Re} z$:

<span class="anker" id="gl-8-1"></span>
$$h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\},\qquad s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{8.1}$$

$s_T(t)$ is called the __complex envelope__, $\mathrm{e}^{\mathrm{j}2\pi f_0t}$ the __complex carrier__. Half their product is the analytic component from [Chapter 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), $s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$, so $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$.

:::satz Theorem 8.1 (Quadrature representation)
<span class="anker" id="satz-8-1"></span>

With $s_T=s_{Tr}+\mathrm{j} s_{Ti}$ and the Hilbert transform $\hat s=s*\frac{1}{\pi t}$:

<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
$$\begin{aligned} s(t)&=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t),\\ s_{Tr}(t)&=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t),\qquad s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t),\\ s(t)&=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr),\qquad|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}. \end{aligned} \tag{8.2|8.3|8.4}$$
:::

⁠**How to read it:** $s_{Tr}$ and $s_{Ti}$ are called __quadrature components__ (the in-phase and the quadrature component): one modulates the cosine of the carrier, the other its sine. $|s_T|$ is the __envelope__, which you see on an oscilloscope as the “outline” of the signal, and $\varphi_T$ is the phase deviation of the carrier. If the complex envelope is real (symmetric case), $s(t)=s_T(t)\cos(2\pi f_0t)$: an amplitude-modulated cosine.

:::herleitung Quadrature components
[(8.2)](#gl-8-2): $\operatorname{Re}\{(s_{Tr}+\mathrm{j} s_{Ti})(\cos+\mathrm{j}\sin)\}=s_{Tr}\cos-s_{Ti}\sin$. For [(8.3)](#gl-8-3): $2s_+=s+\mathrm{j}\hat s$ ([Chapter 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), so

$$s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)=(s\cos+\hat s\sin)+\mathrm{j}(\hat s\cos-s\sin).$$
:::

:::aufgabe Exercise 8 ★★ Determining complex envelopes
<span class="anker" id="aufg-8"></span>

Determine $s_T$, $s_{Tr}$, $s_{Ti}$ and $|s_T|$ with respect to $f_0=10$ Hz for (a) $s(t)=\bigl[1+0.5\cos(2\pi\cdot1\,\mathrm{Hz}\cdot t)\bigr]\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t)$, (b) $s(t)=\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t+0.3)$, (c) $s(t)=\sin(2\pi\cdot10\,\mathrm{Hz}\cdot t)$. Check (c) with [(8.2)](#gl-8-2).

:::loesung
(a) $s_T=1+0.5\cos(2\pi t)$, real: $s_{Tr}=s_T$, $s_{Ti}=0$, $|s_T|=1+0.5\cos(2\pi t)$ between 0.5 and 1.5. An amplitude-modulated cosine.

(b) $s_T=\mathrm{e}^{\mathrm{j}0.3}$: $s_{Tr}=\cos0.3=0.955$, $s_{Ti}=\sin0.3=0.296$, $|s_T|=1$. The envelope is constant; only the phase is shifted by 0.3.

(c) $\sin x=\operatorname{Re}\{-\mathrm{j}\,\mathrm{e}^{\mathrm{j} x}\}$, so $s_T=-\mathrm{j}$: $s_{Tr}=0$, $s_{Ti}=-1$, $|s_T|=1$. Check: $0\cdot\cos-(-1)\sin=\sin$.
:::
:::
