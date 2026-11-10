---
title: Stage 12: Discrete-time bandpass and highpass filters
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Lowpass and Bandpass Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Chapter 5: Lowpass and Bandpass Systems
order: 3251300
summary: Digital bandpass and highpass filters are obtained from a lowpass by modulation.
tags: highpass
lang: en
---

<span class="anker" id="stufe-12"></span>

:::zweck
Digital bandpass and highpass filters are obtained from a lowpass by modulation.
:::

If the discrete-time lowpass has a real impulse response, multiplication by $2\cos(2\pi f_0n)$ shifts its passband to $\pm f_0$:

<span class="anker" id="gl-12-1"></span>
$$H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr],\qquad h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n), \tag{12.1}$$

valid as long as the shifted bands do not overlap: $f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$. Because of the periodicity, the band at $f_0$ must touch neither the band at $-f_0$ nor its copy at $1-f_0$. In general, also for complex lowpass impulse responses, $h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$ holds as in [(8.1)](komplexe-hullkurve-und-quadraturkomponenten.html#gl-8-1). The factor 2 corresponds to the doubled equivalent lowpass $H_T=2H_{\mathrm{TP}}$.

A __highpass__ is a lowpass shifted to half the sampling rate, $f_0=\frac12$. There the band and its mirror image coincide, so it is shifted only once: $H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$. With $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$:

<span class="anker" id="gl-12-2"></span>
$$h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n). \tag{12.2}$$

⁠**In short:** a digital highpass is obtained from a lowpass by flipping every other sign.

:::aufgabe Exercise 11 ★ Highpass from the moving average
<span class="anker" id="aufg-11"></span>

The moving average $h_{\mathrm{TP}}=\frac13(1,1,1)$ ([Chapter 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)) is a simple lowpass.

<ol class="al">

<li>

Form $h_{\mathrm{HP}}$ according to [(12.2)](#gl-12-2).

</li>

<li>

Compute $H_{\mathrm{TP}}$ and $H_{\mathrm{HP}}$ at $f=0$ and $f=\frac12$. Is this consistent with a highpass?

</li>

</ol>

:::loesung
(a) $h_{\mathrm{HP}}=\frac13(1,-1,1)$.

(b) $H_{\mathrm{TP}}(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}[1+2\cos(2\pi f)]$: $|H_{\mathrm{TP}}(0)|=1$, $|H_{\mathrm{TP}}(\frac12)|=\frac13$. The highpass is shifted by $\frac12$: $|H_{\mathrm{HP}}(0)|=\frac13$, $|H_{\mathrm{HP}}(\frac12)|=1$. It passes the fastest sequence $(+1,-1,+1,\dots)$ in full and attenuates the DC component to one third. A simple highpass, not a very steep one.
:::
:::
