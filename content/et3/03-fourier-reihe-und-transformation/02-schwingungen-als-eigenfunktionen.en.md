---
title: Stage 1: Oscillations as eigenfunctions
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Fourier Series and Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Chapter 3: Fourier Series and Transform
order: 3230200
summary: Of the building blocks e pt , only the pure oscillations are used from now on.
tags: frequency response
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Of the building blocks $\mathrm{e}^{pt}$, only the pure oscillations are used from now on. This stage shows what an LTI system does to them.
:::

For purely imaginary $p=\mathrm{j}2\pi f$, the building block becomes an oscillation with constant amplitude:

$$\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft).$$

Like every building block, it is an eigenfunction of every LTI system (delaying is multiplying by $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$):

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft},\qquad H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t. \tag{1.1}$$

$H(f)$ is called the __frequency response__ or transfer function. Its magnitude says how strongly the oscillation of frequency $f$ is amplified or attenuated, and its phase says how far it is shifted. Two systems in cascade multiply one after the other: $H(f)=H_1(f)H_2(f)$. Where the Laplace transform $H(p)$ exists on the imaginary axis, $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$.

⁠**In short:** The frequency response is the number by which an LTI system multiplies a pure oscillation.
