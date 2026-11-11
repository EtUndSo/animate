---
title: Stage 11: Fourier and Laplace, limits of existence
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Fourier Series and Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Chapter 3: Fourier Series and Transform
order: 3231200
summary: When does the Fourier integral exist, and how is it related to the Laplace transform?
tags: central limit theorem
lang: en
---

<span class="anker" id="stufe-11"></span>

:::zweck
When does the Fourier integral exist, and how is it related to the Laplace transform?
:::

A sufficient condition for existence is absolute integrability, $\int|s(t)|\mathrm{d} t<\infty$. The Laplace transform extends the class by weighting with $\mathrm{e}^{-\sigma t}$ first ([Chapter 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)):

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f).$$

So it examines a signal for two things: for frequency components, like the Fourier transform, and for exponential growth or decay. If $\sigma=0$ lies in the region of convergence, the Fourier transform is the Laplace transform on the imaginary axis. With Dirac impulses (Stage [8](singulare-signale-und-linienspektren.html#stufe-8)), however, the Fourier transform also covers signals that the Laplace transform does not cover: constants and oscillations over all time. In general it is sufficient that the signal grows at most as fast as a power of $t$, more precisely, that $\int|s(t)|\,(1+t^2)^{-n}\mathrm{d} t<\infty$ holds for some $n\ge0$. Constants, oscillations, the step and $t^n$ satisfy this, but exponentially growing signals such as $\mathrm{e}^{t}\varepsilon(t)$ do not; only the Laplace transform covers them.

:::zusatz Why repeated convolutions become Gaussian
If you form the $M$-fold convolution of $\operatorname{rect}(t)$ with itself, the spectrum is $\operatorname{si}^M(\pi f)$. For small $f$, $\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$ and $\ln(1+w)\approx w$, so

$$\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}.$$

For large $M$ only the region of small $f$ contributes, and the approximation becomes better and better. For $M=4$ the exact value at $t=0$ is $0.667$, and the Gaussian curve gives $0.691$. This is an instance of the __central limit theorem__ (the part on statistics): the convolution of many identical positive pulses of finite area approaches a Gaussian curve, provided the pulses decay fast enough, more precisely, provided their second moment $\int t^2s(t)\,\mathrm{d} t$ is finite. One example is the impulse response of a cascade of many short integrators. Without this condition it does not work: $\frac{1}{1+t^2}$ from Exercise [7](die-rechenregeln-theoreme.html#aufg-7) has an infinite second moment, and the $M$-fold convolution, with the spectrum $\pi^M\mathrm{e}^{-2\pi M|f|}$, is again a stretched curve of the form $\frac{1}{1+t^2}$.
:::

:::aufgabe Exercise 14 ★★★ (Going further) Checking the Gaussian approximation
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

For $M=2$, compare the exact value $\Lambda(0)=1$ with the Gaussian approximation.

</li>

<li>

Show that the Gaussian curve $\sqrt{6/(\pi M)}\,\mathrm{e}^{-6t^2/M}$ has the area 1. Why must this be so?

</li>

</ol>

:::loesung
(a) $M=2$: $\sqrt{6/(2\pi)}=0.977$ instead of $\Lambda(0)=1$, that is, 2.3 % too low. For $M=4$: 0.691 instead of 0.667, that is, 3.6 % too high. So even after only a few convolutions the Gaussian curve is close to the exact result. The approximation becomes arbitrarily good only for large $M$, because only then do just the small $f$ contribute to the spectrum.

(b) $\int\mathrm{e}^{-6t^2/M}\mathrm{d} t=\sqrt{\pi M/6}$; multiplied by $\sqrt{6/(\pi M)}$, this gives 1. This must be so: the area of a convolution is the product of the areas, here $1^M=1$. In the spectrum this is the value at $f=0$, $\operatorname{si}^M(0)=1$, and the approximation $\mathrm{e}^{-M(\pi f)^2/6}$ also has the value 1 there.
:::
:::
