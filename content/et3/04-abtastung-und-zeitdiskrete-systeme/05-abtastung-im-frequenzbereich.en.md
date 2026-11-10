---
title: Stage 4: Sampling in the frequency domain
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Sampling and Discrete-Time Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Chapter 4: Sampling and Discrete-Time Systems
order: 3240500
summary: The same principle holds with the roles swapped: if you sample the spectrum, the signal becomes periodic.
tags: 
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
The same principle holds with the roles swapped: if you sample the spectrum, the signal becomes periodic.
:::

A spectrum that is known only at the frequencies $kF$ is a comb of weighted Dirac impulses. With the factor $F$, the weights are exactly the Fourier coefficients from [Chapter 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html):

<span class="anker" id="gl-4-1"></span>
$$S_p(f)=F\sum_kS(kF)\,\delta(f-kF)=F\,S(f)\cdot\sum_k\delta(f-kF)\;\bullet\!\!-\!\!\circ\;s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr). \tag{4.1}$$

The corresponding signal is the original, repeated periodically with period $1/F$. If the signal is shorter than $1/F$, the repetitions do not overlap. Then it can be recovered with a time window, and the spectrum with si functions:

<span class="anker" id="gl-4-2"></span>
$$s(t)=s_p(t)\cdot\operatorname{rect}(Ft)\qquad\Longrightarrow\qquad S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr). \tag{4.2}$$

⁠**In short:** discrete in time means periodic in the spectrum, and discrete in the spectrum means periodic in time. The second is the Fourier series from [Chapter 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): its coefficients are samples of the spectrum of a single pulse, $S_p(k)=F\cdot S(kF)$.
