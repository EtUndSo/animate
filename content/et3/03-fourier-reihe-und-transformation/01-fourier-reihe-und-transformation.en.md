---
title: Overview: Fourier Series and the Fourier Transform
kurz: Overview
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Fourier Series and Transform
order: 3230100
summary: Every signal as a superposition of oscillations
tags: spectrum
lang: en
---

## What this is about

[Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) showed that every signal is a superposition of building blocks $\mathrm{e}^{pt}$, and that an LTI system merely multiplies each building block by a number. The Fourier description uses only the building blocks on the imaginary axis, $p=\mathrm{j}2\pi f$: pure oscillations $\mathrm{e}^{\mathrm{j}2\pi ft}$ that neither grow nor decay. This has a big advantage. An oscillation has a frequency that you can hear, measure and filter. The __spectrum__ $S(f)$ tells you with which amplitude and phase each frequency is contained in the signal.



**How to work with this chapter.** Each stage is a short article of its own with the idea, typical questions you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise. Finish one stage before you move on to the next.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Square wave** between 0 and 1 with the period $T=2\pi$ s and the duty cycle $\frac12$: 1 for $|t|\le T/4$, 0 for $T/4<|t|\le T/2$, continued periodically. Fundamental frequency $F=1/T=0.159$ Hz, so $2\pi F=1/\mathrm s$.

</li>

<li>

⁠**RC low-pass filter** with $RC=1$ s, $H(f)=1/(1+\mathrm{j}2\pi f\,RC)$. At the $k$th harmonic of the square wave (its component at the frequency $kF$), $2\pi kF\cdot RC=k$, so $H(kF)=1/(1+\mathrm{j} k)$.

</li>

<li>

⁠**Rectangular pulse** $\operatorname{rect}(t)$ and $\operatorname{si}(x)=\sin(x)/x$.

</li>

</ul>

The script `rechnung_kap3.py` recomputes the numbers and curves.
:::
