---
title: Overview: The Laplace Transform
kurz: Overview
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Laplace Transform
order: 3220100
summary: Every signal as a superposition of $\ee^{pt}$, and why an LTI system turns this into a multiplication
tags: 
lang: en
---

## What this is about

:::frage I understand the calculation that leads from the convolution integral with an eigenfunction to $H(p)$. But I think there is much more behind the Laplace transform than this rule of calculation: that any function can be written as a sum of complex exponentials.
This conjecture goes to the heart of the matter. Without it, the eigenfunction calculation would be a mere curiosity, because by itself it holds only for the one signal $\mathrm{e}^{pt}$. Only because (almost) every signal can be built from such building blocks does it tell us something about *every* input signal. Three refinements make the conjecture exact:

<ol>

<li>

In general it is not a sum but an *integral*: infinitely many building blocks $\mathrm{e}^{pt}$, each with an infinitesimal weight. The building blocks lie on a vertical line $\operatorname{Re} p=\sigma$ in the $p$-plane (Stage [2](ein-signal-aus-lauter-bausteinen.html#stufe-2)).

</li>

<li>

Not every function, but every function for which a region of convergence exists: it may grow at most exponentially on each side of the time axis, and a single damping must tame both sides at once (Section [2.3](konvergenzbereich-welche-dampfungen-funktionieren.html#stufe-2-3)).

</li>

<li>

If $S(p)$ is a ratio of polynomials, the integral really does become a *finite sum* $\sum_r A_r\,\mathrm{e}^{p_r t}$. The exponents $p_r$ are the poles of $S(p)$ (Stage [4](aus-dem-integral-wird-eine-summe.html#stufe-4)).

</li>

</ol>
:::



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

The script `rechnung_kap2.py` recomputes the numbers and curves.
:::
