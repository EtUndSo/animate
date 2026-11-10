---
title: Stage 2: A signal made entirely of building blocks
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Laplace Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Chapter 2: Laplace Transform
order: 3220300
summary: Stage 1 applies to a single building block.
tags: absolutely integrable, Fourier representation, spectrum
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
Stage [1](warum-gerade.html#stufe-1) applies to a single building block. It becomes useful only if every signal can be built from building blocks $\mathrm{e}^{pt}$. This stage shows that this works, what the weights are called and where the limits lie.
:::

### Starting point $\sigma=0$: pure oscillations

<span class="anker" id="stufe-2-1"></span>

On the imaginary axis ($\sigma=0$) the building blocks are pure oscillations $\mathrm{e}^{\mathrm{j}2\pi ft}$. An __absolutely integrable__ signal ($\int|s(t)|\,\mathrm{d} t<\infty$, so it decays fast enough on both sides) can be built from them. This is the __Fourier representation__. Its formula is all that is needed here. The function $\mathcal{F}\{s\}(f)$ is called the __spectrum__; it gives the weight of the oscillation with frequency $f$:

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

For many signals in system theory this is not enough. The step $\varepsilon(t)$ does not decay, and $\mathrm{e}^{2t}\varepsilon(t)$ (the impulse response of an unstable system) even grows. A signal that grows without bound cannot be built from oscillations of constant amplitude.
