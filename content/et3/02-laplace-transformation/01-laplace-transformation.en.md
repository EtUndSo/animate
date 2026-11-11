---
title: Overview: The Laplace Transform
kurz: Overview
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Laplace Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Chapter 2: Laplace Transform
order: 3220100
summary: Every signal as a superposition of $\mathrm{e}^{pt}$, and why an LTI system turns this into a multiplication
tags: 
lang: en
---

## What this is about

**How to work with this chapter.** Each stage is a short article of its own with the idea, typical questions you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise. Finish one stage before you move on to the next.

:::merke The reference model for this chapter
All examples use the same two ingredients:

<ul>

<li>

an **RC low-pass filter** with $RC=1$ s (for example $R=1\,\mathrm{M\Omega}$, $C=1\,\mu\text{F}$). Its impulse response and its transfer function are

$$h(t)=\frac{1}{RC}\,\mathrm{e}^{-t/RC}\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t),\qquad H(p)=\frac{1}{1+pRC}=\frac{1}{p+1},\quad \operatorname{Re} p>-1,$$

with $t$ in s and $p$ in $1/\mathrm{s}$;

</li>

<li>

the **unit step** $s(t)=\varepsilon(t)$ with $S(p)=1/p$ for $\operatorname{Re} p>0$.

</li>

</ul>

:::
