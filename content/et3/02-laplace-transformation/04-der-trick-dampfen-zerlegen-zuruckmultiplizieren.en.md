---
title: The trick: damp, decompose, multiply back
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Laplace Transform
order: 3220400
summary: Every signal as a superposition of $\ee^{pt}$, and why an LTI system turns this into a multiplication
tags: density
lang: en
---

<span class="anker" id="stufe-2-2"></span>

**The idea.** First make the signal decomposable, then undo the change afterwards:

<ol>

<li>

⁠**Damp.** Multiply by $\mathrm{e}^{-\sigma t}$. If a right-sided signal grows at most like $\mathrm{e}^{\alpha t}$, then $s(t)\,\mathrm{e}^{-\sigma t}$ decays for every $\sigma>\alpha$ and is absolutely integrable.

</li>

<li>

⁠**Decompose.** The damped signal is a superposition of pure oscillations. Its Fourier spectrum is exactly the Laplace transform $S(p)=\int s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ on the line $\operatorname{Re} p=\sigma$ (Exercise [2](konvergenzbereich-welche-dampfungen-funktionieren.html#aufg-2)):

$$\mathcal{F}\bigl\{s(t)\,\mathrm{e}^{-\sigma t}\bigr\}(f)=S(\sigma+\mathrm{j}2\pi f).$$

</li>

<li>

⁠**Multiply back.** Multiply the decomposition by $\mathrm{e}^{\sigma t}$. The factor does not depend on $f$ and may be moved inside the integral. There it turns each oscillation $\mathrm{e}^{\mathrm{j}2\pi ft}$ into the building block $\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}=\mathrm{e}^{pt}$.

</li>

</ol>

The result is the conjectured superposition.

:::satz Theorem 2.1 (Inversion formula of the Laplace transform)
<span class="anker" id="satz-2-1"></span>

If $\sigma$ lies in the region of convergence of $S(p)$, then

<span class="anker" id="gl-2-1"></span>
$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p =\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f. \tag{2.1}$$
:::

⁠**How to read it:**

<ul>

<li>

The path of integration is the vertical line $\operatorname{Re} p=\sigma$ in the $p$-plane, traversed from bottom to top ($f$ from $-\infty$ to $+\infty$, Fig. [2](#abb-2)).

</li>

<li>

$\mathrm{e}^{pt}$ is the building block, and $S(p)\,\mathrm{d} p/(2\pi\mathrm{j})=S(\sigma+\mathrm{j}2\pi f)\,\mathrm{d} f$ is its complex weight. $S(p)$ itself is a __density__: weight per frequency interval. If $s$ is a voltage in V, $S$ has the unit V s.

</li>

<li>

The integral is meant as the limit $\lim_{F\to\infty}\int_{-F}^{F}\dots\mathrm{d} f$. It returns $s(t)$ at every point where $s$ is continuous, and at a jump it returns the mean of the left-hand and right-hand limits.

</li>

</ul>

⁠**Limiting case $\sigma=0$:** If the imaginary axis lies in the region of convergence, you may choose $\sigma=0$. Then $p=\mathrm{j}2\pi f$, and [(2.1)](#gl-2-1) becomes the Fourier inversion formula. The Laplace transform contains the Fourier transform as a special case.

:::herleitung Inversion formula from the Fourier inversion formula
By step 2, $S(\sigma+\mathrm{j}2\pi f)$ is the Fourier spectrum of $s(t)\mathrm{e}^{-\sigma t}$. The Fourier inversion formula gives

$$s(t)\,\mathrm{e}^{-\sigma t}=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f.$$

Multiply by $\mathrm{e}^{\sigma t}$, which does not depend on $f$:

$$s(t)=\int_{-\infty}^{\infty}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\,\mathrm{d} f.$$

Substitute $p=\sigma+\mathrm{j}2\pi f$ with $\sigma$ fixed: $\mathrm{d} p=\mathrm{j}2\pi\,\mathrm{d} f$, so $\mathrm{d} f=\mathrm{d} p/(2\pi\mathrm{j})$. The limits $f=\mp\infty$ become $p=\sigma\mp\mathrm{j}\infty$:

$$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p.$$
:::

**Example: the step from building blocks.** For $\varepsilon(t)$, $S(p)=1/p$ with $\operatorname{Re} p>0$. We choose $\sigma=0.5/\mathrm s$ (Fig. [2](#abb-2)). Figure [3](#abb-3) shows the result of superposing only the building blocks with $|f|\le F$. Already at $F=0.25$ Hz the shape of the step is recognizable. As $F$ grows, the edge becomes steeper; at $t=0$ the curve tends to the mean value $\tfrac12$ (0.40, 0.47, 0.49), and at $t=-1$ s it tends to zero (0.053, 0.029, 0.008).

:::abbildung et3/k2linie 2
The $p$-plane for the step $\varepsilon(t)$, $S(p)=1/p$. The region of convergence (shaded blue) lies to the right of the pole $p=0$. Any vertical line in it can serve as the path of integration; here $\sigma=0.5/\mathrm s$. Each point on the line is a building block $\mathrm{e}^{pt}$ with the weight $S(p)$.
:::

:::abbildung et3/k2sprung 3
The step, superposed from the building blocks $\mathrm{e}^{pt}$ on the line $\operatorname{Re} p=0.5/\mathrm s$, keeping only the building blocks with $|f|\le F$: $s_F(t)=\int_{-F}^{F}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} f$ with $S(p)=1/p$. The more building blocks, the more accurate the step; at $t=0$ the curve tends to $\tfrac12$.
:::

:::frage All building blocks are complex. Why does a real curve come out?
The building blocks come in pairs: $f$ goes with $-f$, so $p$ goes with the conjugate point $p^*$. For a real signal the weight there is the complex conjugate, $S(p^*)=S(p)^*$ (computing $S(p)=\int s(t)\mathrm{e}^{-pt}\mathrm{d} t$ with real $s$ shows this). Each pair gives $S\mathrm{e}^{pt}+(S\mathrm{e}^{pt})^*=2\operatorname{Re}\{S(p)\mathrm{e}^{pt}\}$, a real damped or growing oscillation. The imaginary parts cancel in pairs.
:::

:::frage So is it a sum or an integral?
In general an integral: the line carries a continuum of building blocks, each with an infinitesimal weight $S\,\mathrm{d} f$. A true sum with finitely many terms arises in one important case: when $S(p)$ is a ratio of polynomials. Then the signal is a sum of building blocks at the poles (Stage [4](aus-dem-integral-wird-eine-summe.html#stufe-4)). A sum with infinitely many terms is the Fourier series of a periodic signal.
:::
