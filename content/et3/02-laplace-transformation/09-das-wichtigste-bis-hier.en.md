---
title: Key points so far
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Laplace Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Chapter 2: Laplace Transform
order: 3220900
summary: Every signal as a superposition of $\mathrm{e}^{pt}$, and why an LTI system turns this into a multiplication
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

An LTI system can only multiply the building block $\mathrm{e}^{pt}$ by a number $H(p)$, because for $\mathrm{e}^{pt}$ shifting is the same as multiplying.

</li>

<li>

Every signal with a region of convergence is a superposition of such building blocks. $S(p)$ gives the weight with which the building block $\mathrm{e}^{pt}$ is contained in the signal.

</li>

<li>

This is why convolution becomes multiplication, $G(p)=H(p)\,S(p)$. If $S(p)$ is rational, the signal is a finite sum $\sum_r A_r\mathrm{e}^{p_r t}$ with the poles as exponents.

</li>

</ol>
:::

:::kern Key points so far
<ul>

<li>

$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\mathrm{e}^{pt}$, hence $\mathrm{e}^{pt}*h=H(p)\,\mathrm{e}^{pt}$ with $H(p)=\int h(t)\mathrm{e}^{-pt}\mathrm{d} t$.

</li>

<li>

$p=\sigma+\mathrm{j}2\pi f$: $\sigma$ is the growth rate, $f$ the frequency of the building block.

</li>

<li>

$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\mathrm{e}^{pt}\mathrm{d} p$, $\sigma$ in the region of convergence; every such line gives the same $s(t)$.

</li>

<li>

$S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}$; for $\sigma=0$ the Fourier transform.

</li>

<li>

Region of convergence: depends only on $\sigma$; right-sided: a right half-plane, left-sided: a left half-plane, two-sided: a strip.

</li>

<li>

$\mathrm{e}^{p_0t}\varepsilon(t)\leftrightarrow\frac{1}{p-p_0}$ for $\operatorname{Re} p>\operatorname{Re} p_0$; $-\mathrm{e}^{p_0t}\varepsilon(-t)\leftrightarrow\frac{1}{p-p_0}$ for $\operatorname{Re} p<\operatorname{Re} p_0$.

</li>

<li>

$G(p)=S(p)H(p)$; differentiation $\to p$, integration $\to1/p$.

</li>

<li>

Rational and right-sided: $s(t)=A_0\delta(t)+\sum_rA_r\mathrm{e}^{p_rt}\varepsilon(t)$, poles = exponents. Causal and stable: all poles on the left.

</li>

</ul>
:::

**One principle behind all the results.** Almost every result about the Laplace transform follows from these three sentences. The table matches each result to its source, and the stages explain it.

| Result | Where it comes from |
|---|---|
| Eigenfunction $\mathrm{e}^{pt}$, transfer function $H(p)$ | shifting $\mathrm{e}^{pt}$ is multiplying by $\mathrm{e}^{-p\tau}$ (Stage [1](warum-gerade.html#stufe-1)) |
| Laplace transform $S(p)$ | weight of the building block $\mathrm{e}^{pt}$ in the signal (Stage [2](ein-signal-aus-lauter-bausteinen.html#stufe-2)) |
| Region of convergence | the damping rates $\sigma$ for which $s(t)\mathrm{e}^{-\sigma t}$ becomes absolutely integrable (Section [2.3](konvergenzbereich-welche-dampfungen-funktionieren.html#stufe-2-3)) |
| Convolution $\to$ product, cascade | each building block is multiplied by $H(p)$ (Stage [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3)) |
| Derivative $\to p$, integral $\to 1/p$ | $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ and $\int_{-\infty}^t\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$ (Stage [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3)) |
| Differential equation $\to$ ratio of polynomials | each derivative becomes a factor $p$ (Stage [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3)) |
| Poles, partial fractions | the exponents and weights of the finitely many building blocks (Stage [4](aus-dem-integral-wird-eine-summe.html#stufe-4)) |
| Stability | a causal building block $\mathrm{e}^{p_r t}$ decays only if $\operatorname{Re} p_r<0$ (Stage [4](aus-dem-integral-wird-eine-summe.html#stufe-4)) |
| Fourier transform | the same superposition on the line $\sigma=0$ (Stage [2](ein-signal-aus-lauter-bausteinen.html#stufe-2)) |
