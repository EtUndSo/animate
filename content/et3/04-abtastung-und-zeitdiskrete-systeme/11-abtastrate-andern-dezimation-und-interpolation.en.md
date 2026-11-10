---
title: Stage 10: Changing the sampling rate, decimation and interpolation
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Sampling and Discrete-Time Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Chapter 4: Sampling and Discrete-Time Systems
order: 3241100
summary: A sequence can afterwards be represented at a lower or higher rate.
tags: 
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
A sequence can afterwards be represented at a lower or higher rate. The same rules apply to the spectrum as for the original sampling.
:::

**Downsampling by the factor $c$.** Only every $c$th value is kept. Conceptually, first multiply by a comb of unit impulses, then drop the zeros:

$$s_c(n)=s(n)\sum_m\delta(n-mc),\qquad s_u(n)=s(nc).$$

Multiplication by the comb produces $c$ copies of the spectrum spaced $1/c$ apart, and dropping the zeros stretches the frequency axis by $c$:

<span class="anker" id="gl-10-1"></span>
$$S_{c,\mathrm a}(f)=\frac1c\sum_{k=0}^{c-1}S_\mathrm a\Bigl(f-\frac kc\Bigr),\qquad S_{u,\mathrm a}(f)=S_{c,\mathrm a}\Bigl(\frac fc\Bigr). \tag{10.1}$$

If the spectrum extends up to $f_\mathrm g$ (normalized to the old rate), after downsampling it extends up to $cf_\mathrm g$. Aliasing is avoided only if $cf_\mathrm g\le\frac12$. Otherwise a digital low-pass filter must limit the band beforehand.

**Upsampling by the factor $c$.** Insert $c-1$ zeros between every two values: $s_\uparrow(n)=s(n/c)$ for $n$ divisible by $c$, otherwise 0. The spectrum is compressed by $c$, $S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$, and now contains $c-1$ spectral images within the period. A low-pass filter with the cutoff frequency $\frac{1}{2c}$ and the gain $c$ removes them. In doing so it fills the zeros with interpolated values (the si interpolation from Stage [3](abtasttheorem-und-ruckgewinnung.html#stufe-3) in discrete form), and the original values are preserved. Downsampling and upsampling in succession change the rate by a rational factor $c_1/c_2$.

:::abbildung et3/k4rate 7
Spectra (frequency normalized to the respective rate) when the sampling rate is changed. Downsampling stretches the band; upsampling compresses it and creates spectral images, which an interpolation filter removes.
:::

:::aufgabe Exercise 10 ★★ Downsampling
<span class="anker" id="aufg-10"></span>

A sequence has a spectrum up to $f_\mathrm g=0.2$.

<ol class="al">

<li>

May it be downsampled by $c=2$ without a prefilter? By $c=3$?

</li>

<li>

What must happen before downsampling by $c=3$, and what is lost in the process?

</li>

</ol>

:::loesung
(a) $c=2$: afterwards the band extends up to $0.4\le0.5$, no aliasing. $c=3$: up to $0.6>0.5$, aliasing.

(b) Limit the band beforehand to $\frac{1}{2c}=\frac16\approx0.167$ with a digital low-pass filter. The components between 0.167 and 0.2 are lost in the process. That is the price of the lower rate.
:::
:::
