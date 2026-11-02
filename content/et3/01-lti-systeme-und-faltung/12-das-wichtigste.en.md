---
title: Key points
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / LTI Systems and Convolution
order: 3211200
summary: Why the response to a single impulse describes the whole system
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

Every signal is a superposition of infinitely many short impulses: at each instant $\tau$, one impulse with the weight $s(\tau)\,\mathrm{d}\tau$.

</li>

<li>

An LTI system responds to a shifted impulse with the shifted impulse response $h(t-\tau)$ (time invariance), and to a sum of impulses with the sum of the responses (linearity).

</li>

<li>

Therefore the output is the convolution $g(t)=\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$, and $h(t)$ describes the system completely.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Shifting $t\to t-t_0$ delays, stretching $t\to t/T$ widens; $a\operatorname{rect}\bigl(\frac{t-t_0}{T}\bigr)$: center $t_0$, duration $|T|$, height $a$.

</li>

<li>

RC low-pass: $H(F)=\dfrac{1}{1+\mathrm{j}2\pi FRC}$, $|H|=\dfrac{1}{\sqrt{1+(2\pi FRC)^2}}$, $\varphi=-\arctan(2\pi FRC)$; step response $1-\mathrm{e}^{-t/RC}$.

</li>

<li>

LTI: superposition principle and $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$.

</li>

<li>

$s(t)=\int s(\tau)\delta(t-\tau)\mathrm{d}\tau$ and $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau=s*h$.

</li>

<li>

Evaluating: flip, shift, multiply, integrate.

</li>

<li>

$s*\delta=s$; commutative, associative (cascade: $h_1*h_2$), distributive (parallel: $h_1+h_2$).

</li>

<li>

$s(t)\delta(t-T)=s(T)\delta(t-T)$; $\delta(bt)=\delta(t)/|b|$; $\delta(t-t_0)*s=s(t-t_0)$; $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$.

</li>

<li>

Step response $=\int h$, impulse response $=\frac{\mathrm{d}}{\mathrm{d} t}$ step response.

</li>

<li>

Causal: $h(t)=0$ for $t<0$. Stable: $\int|h|\mathrm{d} t<\infty$.

</li>

</ul>
:::

**What comes next.** Convolution takes a lot of work: every time $t$ needs an integral of its own. The next part decomposes signals in such a way that the integral becomes a simple multiplication.

**One principle behind all the results.** The table links each result of this chapter to the principle “decompose, send one building block through, reassemble”.

| Result | Where it comes from |
|---|---|
| Convolution integral | superpose impulses, superpose shifted impulse responses (Stage [4](das-faltungsintegral.html#stufe-4)) |
| Flipping during evaluation | $h(t-\tau)$ is the response to an impulse that arrived $t-\tau$ seconds ago (Stage [5](die-faltung-ausrechnen.html#stufe-5)) |
| $\delta$ is the identity element | a signal made of impulses, sent through a system that leaves every impulse unchanged (Stage [6](rechenregeln-der-faltung.html#stufe-6)) |
| Commutative, associative, distributive laws | swap roles, systems in cascade, systems in parallel (Stage [6](rechenregeln-der-faltung.html#stufe-6)) |
| Sifting property, scaling of the Dirac impulse | $\delta$ is defined only through its area (Stage [7](der-dirac-impuls.html#stufe-7)) |
| Step response = integral of the impulse response | a step is the sum of all impulses up to $t$ (Stage [8](integrieren-und-differenzieren.html#stufe-8)) |
| Causality, stability | conditions on $h(t)$: zero before the impulse, finite area of $\vert h\vert $ (Stage [9](kausal-und-stabil.html#stufe-9)) |
| Convolution without a system | the same superposition, for example for the sum of two dice (Stage [10](faltung-ganz-ohne-system.html#stufe-10)) |
