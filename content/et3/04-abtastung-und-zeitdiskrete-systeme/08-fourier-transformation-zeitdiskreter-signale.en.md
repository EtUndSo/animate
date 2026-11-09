---
title: Stage 7: The discrete-time Fourier transform
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Sampling and Discrete-Time Systems
order: 3240800
summary: What spectrum does a sequence of numbers have?
tags: periodic convolution
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
What spectrum does a sequence of numbers have? It is the spectrum of the ideally sampled signal, computed directly from the samples.
:::

If you insert $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ into the Fourier integral, the sifting property leaves a sum. Normalized to $T=1$:

:::satz Theorem 7.1 (Discrete-time Fourier transform)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf},\qquad s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f. \tag{7.1}$$
:::

⁠**How to read it:** $S_\mathrm a(f)$ is periodic with period 1, which is the sampling rate. One period, $|f|\le\frac12$, contains everything. This is why the inverse transform integrates only over an interval of length 1. The sum is a Fourier series in $f$, with the samples as coefficients.

::::beispiel
For $s(n)=\varepsilon(n)\,b^n$ with $|b|<1$ (geometric series):

<span class="anker" id="gl-7-2"></span>
$$S_\mathrm a(f)=\sum_{n=0}^{\infty}\bigl(b\,\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)^n=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}},\qquad|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}. \tag{7.2}$$

This is also the frequency response $H_\mathrm a(f)$ of the recursive system from Stage [6](ein-rekursives-system.html#stufe-6). For $b=0.6$: $|H_\mathrm a|=2.5$ at $f=0$, $1.60$ at $f=0.1$, $0.86$ at $f=0.25$, $0.625$ at $f=0.5$ (Fig. [6](#abb-6)). The system is a low-pass filter, but with a periodic frequency response: at $f=1$ it amplifies as strongly as at $f=0$ again.

:::abbildung et3/k4dtft 6
Magnitude of the frequency response of the recursive system with $b=0.6$. It is periodic with the sampling rate. Between the red lines lies the one period that describes everything.
:::
::::

**Convolution and multiplication.** As with functions, $s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$. The product of two sequences gives the __periodic convolution__ of the spectra over one period:

<span class="anker" id="gl-7-3"></span>
$$s(n)\cdot h(n)\;\circ\!\!-\!\!\bullet\;\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu. \tag{7.3}$$

:::aufgabe Exercise 7 ★ Moving average
<span class="anker" id="aufg-7"></span>

$h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$ averages three consecutive values.

<ol class="al">

<li>

Show that $H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

</li>

<li>

At which frequency is $H_\mathrm a=0$? Which oscillation does the filter therefore cancel completely, and why (hint: the sum of three values of an oscillation with period 3)?

</li>

</ol>

:::loesung
(a) $\frac13\bigl(1+\mathrm{e}^{-\mathrm{j}2\pi f}+\mathrm{e}^{-\mathrm{j}4\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl(\mathrm{e}^{\mathrm{j}2\pi f}+1+\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

(b) $\cos(2\pi f)=-\frac12$, so $f=\frac13$ (at $f_\mathrm A=1$ kHz: 333 Hz). An oscillation with three values per period consists of three phasors spaced $120^\circ$ apart. Their sum is zero; in every window the filter sees exactly one whole period.
:::
:::
