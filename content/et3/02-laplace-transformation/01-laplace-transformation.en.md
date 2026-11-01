---
title: The Laplace Transform
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Laplace Transform
order: 3220100
summary: Every signal as a superposition of $\ee^{pt}$, and why an LTI system turns this into a multiplication
tags: growth rate, frequency, absolutely integrable, density, partial fraction expansion, stability, natural response
lang: en
---

## What this is about

:::frage I understand the calculation that leads from the convolution integral with an eigenfunction to $H(p)$. But I think there is much more behind the Laplace transform than this rule of calculation: that any function can be written as a sum of complex exponentials.
This conjecture goes to the heart of the matter. Without it, the eigenfunction calculation would be a mere curiosity, because by itself it holds only for the one signal $\mathrm{e}^{pt}$. Only because (almost) every signal can be built from such building blocks does it tell us something about *every* input signal. Three refinements make the conjecture exact:

<ol>

<li>

In general it is not a sum but an *integral*: infinitely many building blocks $\mathrm{e}^{pt}$, each with an infinitesimal weight. The building blocks lie on a vertical line $\operatorname{Re} p=\sigma$ in the $p$-plane (Stage [2](#stufe-2)).

</li>

<li>

Not every function, but every function for which a region of convergence exists: it may grow at most exponentially on each side of the time axis, and a single damping must tame both sides at once (Section [2.3](#stufe-2-3)).

</li>

<li>

If $S(p)$ is a ratio of polynomials, the integral really does become a *finite sum* $\sum_r A_r\,\mathrm{e}^{p_r t}$. The exponents $p_r$ are the poles of $S(p)$ (Stage [4](#stufe-4)).

</li>

</ol>
:::

:::merke The answer in three sentences (by the end of the article they should feel obvious)
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

**One principle behind all the results.** Almost every result about the Laplace transform follows from these three sentences. The table matches each result to its source, and the stages explain it.

| Result | Where it comes from |
|---|---|
| Eigenfunction $\mathrm{e}^{pt}$, transfer function $H(p)$ | shifting $\mathrm{e}^{pt}$ is multiplying by $\mathrm{e}^{-p\tau}$ (Stage [1](#stufe-1)) |
| Laplace transform $S(p)$ | weight of the building block $\mathrm{e}^{pt}$ in the signal (Stage [2](#stufe-2)) |
| Region of convergence | the damping rates $\sigma$ for which $s(t)\mathrm{e}^{-\sigma t}$ becomes absolutely integrable (Section [2.3](#stufe-2-3)) |
| Convolution $\to$ product, cascade | each building block is multiplied by $H(p)$ (Stage [3](#stufe-3)) |
| Derivative $\to p$, integral $\to 1/p$ | $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ and $\int_{-\infty}^t\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$ (Stage [3](#stufe-3)) |
| Differential equation $\to$ ratio of polynomials | each derivative becomes a factor $p$ (Stage [3](#stufe-3)) |
| Poles, partial fractions | the exponents and weights of the finitely many building blocks (Stage [4](#stufe-4)) |
| Stability | a causal building block $\mathrm{e}^{p_r t}$ decays only if $\operatorname{Re} p_r<0$ (Stage [4](#stufe-4)) |
| Fourier transform | the same superposition on the line $\sigma=0$ (Stage [2](#stufe-2)) |

**How to work with this article.** Each stage has the idea, typical questions with answers you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise.

:::merke The reference model for this article
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

## Stage 1: Why $\mathrm{e}^{pt}$ in particular

<span class="anker" id="stufe-1"></span>

:::zweck
If you insert $\mathrm{e}^{pt}$ into the convolution integral, the result is $H(p)\,\mathrm{e}^{pt}$: $\mathrm{e}^{pt}$ is an eigenfunction. This stage asks which property of $\mathrm{e}^{pt}$ forces this and why the building blocks have to be complex.
:::

**The idea.** The convolution integral

$$g(t)=\int_{-\infty}^{\infty}h(\tau)\,s(t-\tau)\,\mathrm{d}\tau$$

reads as follows: the output is a sum of *delayed copies* of the input. The copy with delay $\tau$ enters with the weight $h(\tau)\,\mathrm{d}\tau$. For an arbitrary signal shape, each delayed copy looks different from the original, and the sum has a new shape. Not so for $\mathrm{e}^{pt}$:

$$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\cdot\mathrm{e}^{pt}.$$

A delay by $\tau$ acts like multiplication by the *constant number* $\mathrm{e}^{-p\tau}$. All copies are multiples of the same function $\mathrm{e}^{pt}$, and so is their sum:

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{pt}*h(t)=\mathrm{e}^{pt}\underbrace{\int_{-\infty}^{\infty}h(\tau)\,\mathrm{e}^{-p\tau}\,\mathrm{d}\tau}_{H(p)}=H(p)\,\mathrm{e}^{pt}. \tag{1.1}$$

⁠**In short:** $\mathrm{e}^{pt}$ is an eigenfunction because for $\mathrm{e}^{pt}$ shifting is the same as multiplying.

**What $p$ means.** With $p=\sigma+\mathrm{j}2\pi f$ the building block splits into two factors:

$$\mathrm{e}^{pt}=\mathrm{e}^{\sigma t}\cdot\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{e}^{\sigma t}\bigl[\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft)\bigr].$$

The real part $\sigma$ (in $1/\mathrm s$) is the __growth rate__: for $\sigma<0$ the building block decays, for $\sigma=0$ it oscillates with constant amplitude, for $\sigma>0$ it grows. The imaginary part $2\pi f$ sets the __frequency__ of the oscillation. So every point of the $p$-plane is a building block, and the position of the point tells you what it looks like (Fig. [1](#abb-1)).

:::abbildung et3/k2bausteine
The $p$-plane as a map of the building blocks. Left: four points $p$. Right: for each point, the real part $\operatorname{Re}\{\mathrm{e}^{pt}\}=\mathrm{e}^{\sigma t}\cos(2\pi ft)$ with the envelope $\pm\mathrm{e}^{\sigma t}$ (dashed). Points b, c, d have $2\pi f=\pi/\mathrm s$, so $f=0.5$ Hz. The distance from the imaginary axis determines decay or growth, the height determines the frequency.
:::

:::frage Why complex? A sine is a simple signal too.
When a sine is shifted, it is not just scaled. With $\omega_0=2\pi f_0$,

$$\sin\bigl(\omega_0(t-\tau)\bigr)=\cos(\omega_0\tau)\,\sin(\omega_0t)-\sin(\omega_0\tau)\,\cos(\omega_0t).$$

A cosine component appears, so the delayed copy has a different shape. This is why a system responds to $\sin(\omega_0t)$ with $|H|\sin(\omega_0t+\varphi)$: amplitude *and phase* change. A phase shift cannot be written as multiplication by a real number, but it can be written as multiplication by the complex number $\mathrm{e}^{\mathrm{j}\varphi}$. That is why the building blocks are complex: the single number $H(p)$ carries magnitude and phase. A real sine consists of two building blocks, $\sin(\omega_0t)=\bigl(\mathrm{e}^{\mathrm{j}\omega_0t}-\mathrm{e}^{-\mathrm{j}\omega_0t}\bigr)/(2\mathrm{j})$, and each of them is multiplied by its own number (Exercise [1](#aufg-1)d).
:::

:::frage Why is $\mathrm{e}^{pt}$ an eigenfunction of *every* LTI system, even though the systems are so different?
The form of the eigenfunction follows from time invariance alone (shifting = multiplying), and all LTI systems share that property. Only the factor $H(p)$ depends on the system, because the weights $h(\tau)$ enter into it. So *one* set of building blocks serves all LTI systems at once. That is what makes the Laplace transform universal.
:::

:::zusatz Only exponential functions have this property
We look for a differentiable function $x(t)$ with $x(0)=1$ whose shifted copies are multiples of itself: $x(t+u)=c(u)\,x(t)$ for all $t,u$. Setting $t=0$ gives $c(u)=x(u)$, so $x(t+u)=x(t)\,x(u)$. Differentiating with respect to $u$ at $u=0$ gives $x'(t)=x'(0)\,x(t)$. This is the differential equation $x'=p\,x$ with $p=x'(0)$, and its solution with $x(0)=1$ is $x(t)=\mathrm{e}^{pt}$. So there are no other building blocks with this property.
:::

:::frage Are exponential functions the only possible eigenfunctions of LTI systems?
Two questions have to be kept apart.

⁠**Eigenfunction of *all* LTI systems at once: yes, only $c\,\mathrm{e}^{pt}$.** The ideal delay element $g(t)=s(t-u)$ is itself an LTI system, for every delay $u$. A function that is an eigenfunction of every LTI system must therefore turn into a multiple of itself under every shift. By the box above, only $\mathrm{e}^{pt}$ does that.

⁠**Eigenfunction of one *particular* system: not only.** The system multiplies each building block $\mathrm{e}^{p_kt}$ by its own number $H(p_k)$. A sum $\sum_kc_k\mathrm{e}^{p_kt}$ stays a multiple of itself exactly when all these factors are equal, $H(p_k)=\lambda$. The common factor $\lambda$ is then the eigenvalue. Two examples:

<ul>

<li>

Ideal delay element by $T$: $H(p)=\mathrm{e}^{-pT}$ has the same value 1 at all points $p_k=\mathrm{j}2\pi k/T$. Every signal with period $T$ is an eigenfunction with eigenvalue 1, because $s(t-T)=s(t)$.

</li>

<li>

Ideal low-pass filter without delay, $H(f)=1$ in the whole passband: every signal whose spectrum lies entirely in the passband comes out unchanged and is an eigenfunction with eigenvalue 1.

</li>

</ul>

For the RC circuit, on the other hand, $H(p)=1/(1+pRC)$ takes each value only once. There the single $c\,\mathrm{e}^{pt}$ (with $p$ in the region of convergence) are the only eigenfunctions that can be built from building blocks.

⁠**In short:** $\mathrm{e}^{pt}$ is the only eigenfunction that *every* LTI system has. A single system can also have mixtures of building blocks as eigenfunctions if it multiplies all of these building blocks by the same number.
:::

:::ltspice An eigenfunction in the experiment
⁠**Draw:** the RC circuit (`res` with `1Meg` from `in` to `out`, `cap` with `1u` to ground). As the source, a behavioural source `bv` with `V=exp(-time/2)`, the building block with $p=-0.5/\mathrm s$.

⁠**Directives:** `.tran 0 10 0 1m` and `.ic V(out)=X` with a number for $X$: the capacitor starts at $X$ volts. Use “Add Traces” to plot the expression `V(out)/V(in)`.

⁠**What you see:** If you set $X$ to the value your result from Exercise [1](#aufg-1)(b) has at $t=0$, the ratio is constant from the start: the output is a number times the input. With $X=0$ it approaches the same number only after a few seconds. The reason: an input that had always been present would have charged the capacitor to exactly this value at $t=0$. The RC circuit removes any other initial voltage with $\mathrm{e}^{-t}$, faster than the input decays with $\mathrm{e}^{-t/2}$.

⁠**For (d):** a `voltage` source with `SINE(0 1 {1/(2*pi)} 0 0 90)`, which is $\cos t$. Compare the amplitude and lag of `V(out)` after the transient with your result from Exercise [1](#aufg-1)(d).
:::

:::aufgabe Exercise 1 ★ Eigenfunction or not?
<span class="anker" id="aufg-1"></span>

Use the RC low-pass filter of the reference model, $h(t)=\mathrm{e}^{-t}\varepsilon(t)$.

<ol class="al">

<li>

Compute $H(p)=\int h(t)\,\mathrm{e}^{-pt}\mathrm{d} t$. For which $p$ does the integral converge, and why does this depend only on $\operatorname{Re} p$?

</li>

<li>

Input $s(t)=\mathrm{e}^{-t/2}$ for all $t$. Compute the output once directly with the convolution integral and once with $H(p)$. Which $p$ does this building block have?

</li>

<li>

Input $s(t)=t$ for all $t$. Use the convolution integral to show that the output is $g(t)=t-1$. Why is $t$ not an eigenfunction, even though the output looks similar? What does the $-1$ mean for the capacitor?

</li>

<li>

Input $s(t)=\cos t$ (so $\omega_0=1/\mathrm s$). Decompose the cosine into two building blocks, multiply each by its $H(p)$ and put them back together. Show that $g(t)=A\cos(t+\varphi)$, and find $A$ and $\varphi$. Is $\cos t$ an eigenfunction?

</li>

</ol>

⁠*Hint for (c):* $\int_0^\infty\mathrm{e}^{-\tau}\mathrm{d}\tau=1$ and $\int_0^\infty\tau\,\mathrm{e}^{-\tau}\mathrm{d}\tau=1$.

:::loesung
(a) $H(p)=\int_0^\infty\mathrm{e}^{-\tau}\mathrm{e}^{-p\tau}\mathrm{d}\tau=\int_0^\infty\mathrm{e}^{-(p+1)\tau}\mathrm{d}\tau=\dfrac{1}{p+1}$. The integral converges if and only if $|\mathrm{e}^{-(p+1)\tau}|=\mathrm{e}^{-(\sigma+1)\tau}$ decays, that is, for $\operatorname{Re} p>-1$. The magnitude depends only on $\sigma$ because $|\mathrm{e}^{-\mathrm{j}2\pi f\tau}|=1$.

(b) Directly:

$$g(t)=\int_0^\infty\mathrm{e}^{-\tau}\,\mathrm{e}^{-(t-\tau)/2}\mathrm{d}\tau=\mathrm{e}^{-t/2}\int_0^\infty\mathrm{e}^{-\tau/2}\mathrm{d}\tau=2\,\mathrm{e}^{-t/2}.$$

With $H(p)$: the building block has $p=-\tfrac12$ (real, no oscillation). This value lies in the region of convergence, $H(-\tfrac12)=1/(\tfrac12)=2$, so $g(t)=2\,\mathrm{e}^{-t/2}$. Both routes agree (numerically: $g(1\,\mathrm{s})=1.2131$).

(c) $g(t)=\int_0^\infty\mathrm{e}^{-\tau}(t-\tau)\mathrm{d}\tau=t\int_0^\infty\mathrm{e}^{-\tau}\mathrm{d}\tau-\int_0^\infty\tau\mathrm{e}^{-\tau}\mathrm{d}\tau=t-1$. This is not a multiple of $t$: the delayed copies $t-\tau$ are not multiples of $t$ (the factor $1-\tau/t$ depends on $t$ itself). The output is the *shifted* ramp: the capacitor voltage follows the input ramp with a delay of $RC=1$ s. Same shape, but shifted instead of scaled, so not an eigenfunction.

(d) $\cos t=\tfrac12\mathrm{e}^{\mathrm{j} t}+\tfrac12\mathrm{e}^{-\mathrm{j} t}$, building blocks at $p=\pm\mathrm{j}$, both in the region of convergence ($\operatorname{Re} p=0>-1$).

$$H(\mathrm{j})=\frac{1}{1+\mathrm{j}}=\frac{1}{\sqrt2}\,\mathrm{e}^{-\mathrm{j}\pi/4},\qquad H(-\mathrm{j})=H(\mathrm{j})^*=\frac{1}{\sqrt2}\,\mathrm{e}^{+\mathrm{j}\pi/4}.$$

$$g(t)=\tfrac12H(\mathrm{j})\mathrm{e}^{\mathrm{j} t}+\tfrac12H(-\mathrm{j})\mathrm{e}^{-\mathrm{j} t}=\operatorname{Re}\bigl\{H(\mathrm{j})\mathrm{e}^{\mathrm{j} t}\bigr\}=\frac{1}{\sqrt2}\cos\Bigl(t-\frac\pi4\Bigr).$$

So $A=1/\sqrt2\approx0.707$ and $\varphi=-45^\circ$ (numerically: $g(1\,\mathrm{s})=0.6909$). Each of the two complex building blocks is an eigenfunction, but their sum $\cos t$ is not: the two building blocks are multiplied by *different* numbers, $H(\mathrm{j})\neq H(-\mathrm{j})$. This shifts the phase.
:::
:::

## Stage 2: A signal made entirely of building blocks

<span class="anker" id="stufe-2"></span>

:::zweck
Stage [1](#stufe-1) applies to a single building block. It becomes useful only if every signal can be built from building blocks $\mathrm{e}^{pt}$. This stage shows that this works, what the weights are called and where the limits lie.
:::

### Starting point $\sigma=0$: pure oscillations

<span class="anker" id="stufe-2-1"></span>

On the imaginary axis ($\sigma=0$) the building blocks are pure oscillations $\mathrm{e}^{\mathrm{j}2\pi ft}$. An __absolutely integrable__ signal ($\int|s(t)|\,\mathrm{d} t<\infty$, so it decays fast enough on both sides) can be built from them. This is the Fourier representation, which is treated in detail in the part on the Fourier transform:

$$s(t)=\int_{-\infty}^{\infty}\mathcal{F}\{s\}(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f,\qquad \mathcal{F}\{s\}(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t.$$

For many signals in system theory this is not enough. The step $\varepsilon(t)$ does not decay, and $\mathrm{e}^{2t}\varepsilon(t)$ (the impulse response of an unstable system) even grows. A signal that grows without bound cannot be built from oscillations of constant amplitude.

### The trick: damp, decompose, multiply back

<span class="anker" id="stufe-2-2"></span>

**The idea.** First make the signal decomposable, then undo the change afterwards:

<ol>

<li>

⁠**Damp.** Multiply by $\mathrm{e}^{-\sigma t}$. If a right-sided signal grows at most like $\mathrm{e}^{\alpha t}$, then $s(t)\,\mathrm{e}^{-\sigma t}$ decays for every $\sigma>\alpha$ and is absolutely integrable.

</li>

<li>

⁠**Decompose.** The damped signal is a superposition of pure oscillations. Its Fourier spectrum is exactly the Laplace transform $S(p)=\int s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ on the line $\operatorname{Re} p=\sigma$ (Exercise [2](#aufg-2)):

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

:::abbildung et3/k2linie
The $p$-plane for the step $\varepsilon(t)$, $S(p)=1/p$. The region of convergence (shaded blue) lies to the right of the pole $p=0$. Any vertical line in it can serve as the path of integration; here $\sigma=0.5/\mathrm s$. Each point on the line is a building block $\mathrm{e}^{pt}$ with the weight $S(p)$.
:::

:::abbildung et3/k2sprung
The step, superposed from the building blocks $\mathrm{e}^{pt}$ on the line $\operatorname{Re} p=0.5/\mathrm s$, keeping only the building blocks with $|f|\le F$: $s_F(t)=\int_{-F}^{F}S(\sigma+\mathrm{j}2\pi f)\,\mathrm{e}^{(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} f$ with $S(p)=1/p$. The more building blocks, the more accurate the step; at $t=0$ the curve tends to $\tfrac12$.
:::

:::frage All building blocks are complex. Why does a real curve come out?
The building blocks come in pairs: $f$ goes with $-f$, so $p$ goes with the conjugate point $p^*$. For a real signal the weight there is the complex conjugate, $S(p^*)=S(p)^*$ (computing $S(p)=\int s(t)\mathrm{e}^{-pt}\mathrm{d} t$ with real $s$ shows this). Each pair gives $S\mathrm{e}^{pt}+(S\mathrm{e}^{pt})^*=2\operatorname{Re}\{S(p)\mathrm{e}^{pt}\}$, a real damped or growing oscillation. The imaginary parts cancel in pairs.
:::

:::frage So is it a sum or an integral?
In general an integral: the line carries a continuum of building blocks, each with an infinitesimal weight $S\,\mathrm{d} f$. A true sum with finitely many terms arises in one important case: when $S(p)$ is a ratio of polynomials. Then the signal is a sum of building blocks at the poles (Stage [4](#stufe-4)). A sum with infinitely many terms is the Fourier series of a periodic signal.
:::

### Region of convergence: which damping rates work

<span class="anker" id="stufe-2-3"></span>

**The idea.** The factor $\mathrm{e}^{-\sigma t}$ acts on both sides of the time axis, but in opposite ways. For $t\to+\infty$ it damps more strongly the larger $\sigma$ is. For $t\to-\infty$, $\mathrm{e}^{-\sigma t}=\mathrm{e}^{\sigma|t|}$, so there a large $\sigma$ amplifies. This gives the three shapes of the region of convergence:

<ul>

<li>

⁠**right-sided signal**, $s(t)=0$ for $t<0$, growing at most like $\mathrm{e}^{\alpha t}$: every $\sigma>\alpha$ works. Region of convergence: the half-plane to the *right* of a boundary.

</li>

<li>

⁠**left-sided signal**: only the side $t\to-\infty$ matters, and small $\sigma$ help. Region of convergence: a half-plane to the *left* of a boundary.

</li>

<li>

⁠**two-sided signal**: both conditions must hold at once. Region of convergence: a *strip*, which may also be empty.

</li>

</ul>

Why are the boundaries always vertical? Because $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$. Whether $\int|s(t)\mathrm{e}^{-pt}|\mathrm{d} t$ is finite depends only on $\sigma$, never on $f$.

⁠**In short:** The region of convergence is the set of all damping rates $\sigma$ for which $s(t)\,\mathrm{e}^{-\sigma t}$ becomes absolutely integrable.

:::merke The basic transform pairs (used throughout the article)
For any complex number $p_0$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
<span class="anker" id="gl-2-4"></span>
<span class="anker" id="gl-2-5"></span>
$$\begin{aligned} \mathrm{e}^{p_0t}\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p>\operatorname{Re} p_0,\\ -\mathrm{e}^{p_0t}\,\varepsilon(-t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p<\operatorname{Re} p_0,\\ \delta(t)\quad&\longleftrightarrow\quad1,&&\text{all }p,\\ t\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p^2},&&\operatorname{Re} p>0. \end{aligned} \tag{2.2|2.3|2.4|2.5}$$

With $p_0=0$, [(2.2)](#gl-2-2) gives the step: $\varepsilon(t)\leftrightarrow1/p$ for $\operatorname{Re} p>0$. The first two lines have the *same* expression and different regions of convergence: only the expression and the region of convergence together determine the signal.
:::

:::herleitung Basic transform pairs
[(2.2)](#gl-2-2): $\int_0^\infty\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_0^\infty=\frac{1}{p-p_0}$. The value at the upper limit vanishes if and only if $\operatorname{Re}(p-p_0)>0$.

[(2.3)](#gl-2-3): $-\int_{-\infty}^0\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=-\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_{-\infty}^0=\frac{1}{p-p_0}$. The value for $t\to-\infty$ vanishes if and only if $\operatorname{Re}(p-p_0)<0$.

[(2.4)](#gl-2-4): sifting property, $\int\delta(t)\mathrm{e}^{-pt}\mathrm{d} t=\mathrm{e}^{0}=1$.

[(2.5)](#gl-2-5): integration by parts, $\int_0^\infty t\,\mathrm{e}^{-pt}\mathrm{d} t=\Bigl[\frac{-t\,\mathrm{e}^{-pt}}{p}\Bigr]_0^\infty+\frac1p\int_0^\infty\mathrm{e}^{-pt}\mathrm{d} t=0+\frac{1}{p^2}$ for $\operatorname{Re} p>0$.
:::

:::frage Why do the exponential terms drop out when evaluating $\int_0^\infty\mathrm{e}^{-bt}\mathrm{e}^{-pt}\mathrm{d} t$, and why is the result $\frac{1}{b+p}$ and not $\frac{1}{-(b+p)}$?
Both come from inserting the limits. The antiderivative of $\mathrm{e}^{-(b+p)t}$ is $-\frac{\mathrm{e}^{-(b+p)t}}{b+p}$, with a minus sign because differentiating produces the factor $-(b+p)$. Then you compute “upper limit minus lower limit”:

$$\int_0^\infty\mathrm{e}^{-(b+p)t}\mathrm{d} t=\underbrace{\lim_{t\to\infty}\Bigl(-\frac{\mathrm{e}^{-(b+p)t}}{b+p}\Bigr)}_{=\,0}-\Bigl(-\frac{\mathrm{e}^{0}}{b+p}\Bigr)=\frac{1}{b+p}.$$

<ul>

<li>

⁠**Upper limit:** $|\mathrm{e}^{-(b+p)t}|=\mathrm{e}^{-(\operatorname{Re} b+\sigma)t}$ tends to zero if and only if $\operatorname{Re} p>-\operatorname{Re} b$. This condition *is* the region of convergence. Outside it, the exponential term would remain and grow without bound.

</li>

<li>

⁠**Lower limit:** $\mathrm{e}^0=1$, so no exponential term is left there.

</li>

<li>

⁠**Sign:** The minus sign of the antiderivative meets the minus sign with which the lower limit is subtracted. Minus times minus gives plus.

</li>

</ul>

For the left-sided pulse $\mathrm{e}^{-bt}\varepsilon(-t)$ it is the other way round. The integral runs from $-\infty$ to $0$, so now $t=0$ is the *upper* limit. Its contribution $-\frac{1}{b+p}$ is not subtracted, so the minus sign remains. The lower limit $t\to-\infty$ vanishes only for $\operatorname{Re}(b+p)<0$, which is why this region of convergence lies on the left. With $p_0=-b$ these are the basic transform pairs [(2.2)](#gl-2-2) and [(2.3)](#gl-2-3).
:::

:::frage Do we look at the real parts of $b$ and $p$ because the decay of the integrand decides integrability? For some $b$ the signal decays, for others it grows and does not fall to zero, and the integral does not converge because something keeps being added.
Yes, exactly. The magnitude of the integrand is

$$\bigl|\mathrm{e}^{-(b+p)t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t}\cdot\underbrace{\bigl|\mathrm{e}^{-\mathrm{j}\operatorname{Im}(b+p)\,t}\bigr|}_{=\,1}.$$

The imaginary part only makes the integrand rotate in the complex plane; it does not change the magnitude. Growth or decay is decided by the real part alone. Three refinements:

<ul>

<li>

What counts is the *sum* $\operatorname{Re} b+\sigma$. The signal itself may grow ($\operatorname{Re} b<0$) as long as the damping $\sigma$ is stronger. This is the “damp” trick from Section 2.2.

</li>

<li>

“Tends to zero” alone is not enough. $1/t$ also tends to zero, but $\int_1^\infty\frac{\mathrm{d} t}{t}=\infty$, because the contributions shrink too slowly. Exponential decay is fast enough: $\int_0^\infty\mathrm{e}^{-\operatorname{Re}(b+p)t}\mathrm{d} t=\frac{1}{\operatorname{Re}(b+p)}$ is finite.

</li>

<li>

On the boundary $\operatorname{Re}(b+p)=0$ the integrand has the constant magnitude 1 and only rotates. The integral then oscillates instead of approaching a value, and exactly at the pole it even grows linearly (Exercise [3a](#aufg-3a)). This is why the boundary line does not belong to the region of convergence.

</li>

</ul>
:::

:::frage So does this hold for any function at all?
No, only for functions with a non-empty region of convergence. Three counterexamples:

<ul>

<li>

$\mathrm{e}^{t^2}\varepsilon(t)$ grows faster than any exponential function. $\mathrm{e}^{t^2-\sigma t}\to\infty$ for every $\sigma$, so no damping is enough.

</li>

<li>

$\mathrm{e}^{|t|}$: the right half requires $\sigma>1$, the left half $\sigma<-1$. Both at once is impossible.

</li>

<li>

Even the constant $s(t)=1$ for all $t$: on the right $\sigma>0$, on the left $\sigma<0$. The Fourier transform still covers such signals, with a Dirac impulse in the spectrum.

</li>

</ul>

For right-sided signals with at most exponential growth it always works. This includes every signal that is switched on in a circuit at $t=0$.
:::

:::frage Why is a single line enough when the $p$-plane is two-dimensional?
Every line in the region of convergence gives the same $s(t)$: with a larger $\sigma$ you damp more strongly in step 1 and multiply back more strongly in step 3, and the two cancel. Numerically confirmed: with $\sigma=0.2$ and $\sigma=1/\mathrm s$, the step gives $s(1\,\mathrm{s})\approx1.00$ and $s(-1\,\mathrm{s})\approx0.00$ both times. So the plane contains more than you need for the superposition. Its use lies elsewhere: in the plane, $S(p)$ can be described by a few numbers, the poles and zeros. (Aside: $S(p)$ is complex differentiable in the region of convergence, so its values on one line determine the function in the whole region.)
:::

:::aufgabe Exercise 2 ★ Laplace is Fourier of a damped signal
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Show that $S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\,\mathrm{e}^{-\sigma t}\}(f)$ by splitting $\mathrm{e}^{-pt}$ into two factors.

</li>

<li>

Check it for the step: compute $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}$ for $\sigma>0$ directly and compare with $S(p)=1/p$.

</li>

</ol>

:::loesung
(a) $S(\sigma+\mathrm{j}2\pi f)=\int s(t)\,\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\int\bigl[s(t)\mathrm{e}^{-\sigma t}\bigr]\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}(f)$.

(b) $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}=\int_0^\infty\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\dfrac{1}{\sigma+\mathrm{j}2\pi f}$ for $\sigma>0$. This is $1/p$ at the point $p=\sigma+\mathrm{j}2\pi f$.
:::
:::

:::aufgabe Exercise 3 ★★ A growing signal
<span class="anker" id="aufg-3"></span>

$s(t)=\mathrm{e}^{2t}\varepsilon(t)$, for example the impulse response of an unstable system ($t$ in s).

<ol class="al">

<li>

Why is there no Fourier transform in the classical sense?

</li>

<li>

For which $\sigma$ is $s(t)\,\mathrm{e}^{-\sigma t}$ absolutely integrable?

</li>

<li>

Compute $S(p)$ directly from the integral. Sketch the pole and the region of convergence in the $p$-plane.

</li>

<li>

Which $\sigma$ may you use in the inversion formula? The expression $S(\mathrm{j}2\pi f)$ is finite. Why may you still not choose $\sigma=0$, and which signal would $\sigma=0$ give? (Hint: [(2.3)](#gl-2-3).)

</li>

</ol>

:::loesung
(a) $\int_0^\infty\mathrm{e}^{2t}\mathrm{d} t=\infty$: the signal is not absolutely integrable. Intuitively: nothing that grows can be built from oscillations of constant amplitude.

(b) $|s(t)\mathrm{e}^{-\sigma t}|=\mathrm{e}^{(2-\sigma)t}$ for $t>0$, integrable if and only if $\sigma>2/\mathrm s$.

(c) $S(p)=\int_0^\infty\mathrm{e}^{-(p-2)t}\mathrm{d} t=\dfrac{1}{p-2}$ for $\operatorname{Re} p>2$. Pole at $p=2$, region of convergence to the right of it, as for every right-sided signal. Numerical check: $S(3)=1$, $S(2.5+\mathrm{j})=0.4-0.8\mathrm{j}$.

(d) Any $\sigma>2/\mathrm s$, for example $\sigma=3/\mathrm s$. The value $\sigma=0$ lies to the left of the pole, so outside the region of convergence. The expression $1/(\mathrm{j}2\pi f-2)$ is finite, but it belongs to a *different* signal: by [(2.3)](#gl-2-3), $-\mathrm{e}^{2t}\varepsilon(-t)$ also has the transform $1/(p-2)$, with region of convergence $\operatorname{Re} p<2$. With $\sigma=0$ you would get this left-sided, decaying signal. It is the signal whose Fourier transform really is $1/(\mathrm{j}2\pi f-2)$.
:::
:::

:::aufgabe Exercise 3a ★★ What happens on the boundary
<span class="anker" id="aufg-3a"></span>

$s(t)=\mathrm{e}^{(1+3\mathrm{j})t}\varepsilon(t)$, so $b=-1-3\mathrm{j}$ ($t$ in s).

<ol class="al">

<li>

For which $\sigma$ does $\int_0^\infty s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ converge? What role does the 3 play?

</li>

<li>

Set $p=1+\mathrm{j}\omega$, exactly on the boundary, and compute $\int_0^T s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$. What happens as $T\to\infty$? Distinguish $\omega\neq3$ and $\omega=3$. Where is the pole?

</li>

</ol>

:::loesung
(a) $b+p=(\sigma-1)+\mathrm{j}(\omega-3)$ with $p=\sigma+\mathrm{j}\omega$. The magnitude of the integrand is $\mathrm{e}^{-(\sigma-1)t}$, so the integral converges if and only if $\sigma>1$. The 3 (the angular frequency of the signal) does not appear in the magnitude. It only determines where on the boundary line the pole sits: $S(p)=\frac{1}{p-(1+3\mathrm{j})}$, pole at $p=1+3\mathrm{j}$.

(b) With $p=1+\mathrm{j}\omega$, $b+p=\mathrm{j}(\omega-3)$.

<ul>

<li>

$\omega\neq3$: $\displaystyle\int_0^T\mathrm{e}^{-\mathrm{j}(\omega-3)t}\mathrm{d} t=\frac{1-\mathrm{e}^{-\mathrm{j}(\omega-3)T}}{\mathrm{j}(\omega-3)}$. As $T$ grows, the numerator runs around a circle centered at 1 and approaches no value. The integral stays bounded but has no limit.

</li>

<li>

$\omega=3$, that is, exactly at the pole $p=1+3\mathrm{j}$: the integrand is constantly 1, the integral equals $T$ and grows without bound.

</li>

</ul>

So the integral converges nowhere on the boundary line. The region of convergence is the open half-plane $\operatorname{Re} p>1$.
:::
:::

:::aufgabe Exercise 4 ★ True or false? Give reasons
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Every function has a Laplace transform.

</li>

<li>

Whether $p$ lies in the region of convergence depends only on $\operatorname{Re} p$.

</li>

<li>

If the imaginary axis lies in the region of convergence, $S(\mathrm{j}2\pi f)$ is the Fourier transform of $s(t)$.

</li>

<li>

In the inversion formula, $\sigma=1/\mathrm s$ gives a different signal than $\sigma=2/\mathrm s$ if both lie in the region of convergence.

</li>

<li>

$\cos(2\pi f_0t)$ is an eigenfunction of every LTI system.

</li>

</ol>

:::loesung
(a) False. Counterexamples: $\mathrm{e}^{t^2}\varepsilon(t)$, $\mathrm{e}^{|t|}$, the two-sided constant.

(b) True. $|s(t)\mathrm{e}^{-pt}|=|s(t)|\mathrm{e}^{-\sigma t}$; the frequency $f$ does not appear in the magnitude. This is why the region of convergence consists of whole vertical lines.

(c) True. With $\sigma=0$, $S(\mathrm{j}2\pi f)=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s\}(f)$.

(d) False. Every line in the region of convergence gives the same signal, because the damping by $\mathrm{e}^{-\sigma t}$ and the multiplication back by $\mathrm{e}^{\sigma t}$ cancel.

(e) False. The output is $|H|\cos(2\pi f_0t+\varphi)$ with $H=H(\mathrm{j}2\pi f_0)$. It is a multiple of $\cos(2\pi f_0t)$ only if $\varphi=0$ or $\varphi=\pi$, that is, only if $H(\mathrm{j}2\pi f_0)$ is real. For the RC low-pass filter this is not the case at any frequency $f_0>0$.
:::
:::

## Stage 3: Convolution becomes multiplication

<span class="anker" id="stufe-3"></span>

:::zweck
Stage [1](#stufe-1) says what the system does to one building block. Stage [2](#stufe-2) says that every signal consists of building blocks. Together they give the most important theorem of the Laplace transform.
:::

**The idea.** An LTI system is linear: it processes each building block of the input separately and adds the results. It multiplies each building block $\mathrm{e}^{pt}$ by $H(p)$. So the output consists of the *same* building blocks as the input, except that each weight is multiplied by $H(p)$. Figure [4](#abb-4) shows the two routes to the output.

:::abbildung et3/k2wege
Two routes from input to output. Top: directly with the convolution integral. Bottom: decompose the input into building blocks, multiply each weight by $H(p)$, reassemble. The bottom route works because every building block is an eigenfunction.
:::

:::satz Theorem 3.1 (Convolution theorem)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$g(t)=s(t)*h(t)\quad\Longleftrightarrow\quad G(p)=S(p)\,H(p), \tag{3.1}$$

valid for all $p$ that lie in the regions of convergence of both $S$ and $H$.
:::

⁠**How to read it:** $S(p)$ is the weight of the building block $\mathrm{e}^{pt}$ in the input, $H(p)$ is the factor by which the system multiplies this building block, and $G(p)$ is the weight in the output. The condition on $p$ arises because the line of the inversion formula must run through both regions of convergence: the input must be decomposable into building blocks, and the system must be able to process each of them.

:::herleitung Convolution theorem from superposition and eigenfunction
Insert the input as the superposition [(2.1)](#gl-2-1) into the convolution, using a line $\operatorname{Re} p=\sigma$ that lies in both regions of convergence:

$$g(t)=s(t)*h(t)=\left[\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\mathrm{e}^{pt}\,\mathrm{d} p\right]*h(t).$$

Linearity: the convolution may be moved inside the integral, where it acts on each building block separately:

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\bigl[\mathrm{e}^{pt}*h(t)\bigr]\,\mathrm{d} p.$$

Eigenfunction [(1.1)](#gl-1-1): $\mathrm{e}^{pt}*h(t)=H(p)\,\mathrm{e}^{pt}$.

$$g(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[S(p)H(p)\bigr]\,\mathrm{e}^{pt}\,\mathrm{d} p.$$

This is the inversion formula for $g$ with the weight $S(p)H(p)$. Since the weights of a signal are unique, $G(p)=S(p)H(p)$.
:::

⁠**In short:** Convolution becomes multiplication because the system only multiplies each building block $\mathrm{e}^{pt}$ by the number $H(p)$.

:::analogie
A graphic equalizer splits music into frequency bands, multiplies each band by the setting of its slider and puts the bands back together. An LTI system does the same with the building blocks $\mathrm{e}^{pt}$, and the slider setting is $H(p)$. The analogy breaks down in two places: an equalizer has finitely many bands with real slider settings. Here there is a continuum of building blocks, which can also grow or decay, and each “slider” is a complex number that also shifts the phase.
:::

**The same mechanism explains derivatives, integrals and differential equations.**

<ul>

<li>

⁠**Differentiation.** $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$. The differentiator is an LTI system, and each building block is an eigenfunction of it with the eigenvalue $p$. So each weight is multiplied by $p$: $\mathcal{L}\{\dot s\}=p\,S(p)$.

</li>

<li>

⁠**Integration.** $\int_{-\infty}^{t}\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$, but only for $\operatorname{Re} p>0$; otherwise the integral diverges at $-\infty$. Hence $\mathcal{L}\{\int_{-\infty}^t s\,\mathrm{d}\tau\}=S(p)/p$ with the additional condition $\operatorname{Re} p>0$.

</li>

<li>

⁠**Cascade.** Two systems in series multiply first by $H_1(p)$ and then by $H_2(p)$, together by $H_1H_2$. The order does not matter, because numbers commute.

</li>

<li>

⁠**Differential equation.** Each derivative becomes a factor $p$. A linear differential equation with constant coefficients

$$\sum_{r=0}^{R}\alpha_r\frac{\mathrm{d}^r g}{\mathrm{d} t^r}=\sum_{q=0}^{Q}\beta_q\frac{\mathrm{d}^q s}{\mathrm{d} t^q} \quad\text{becomes}\quad \Bigl(\sum_{r}\alpha_rp^r\Bigr)G(p)=\Bigl(\sum_q\beta_qp^q\Bigr)S(p),$$

that is, an algebraic equation, and $H(p)=G/S$ is a ratio of polynomials.

</li>

</ul>

**Example: the step response of the RC low-pass filter.** Input $\varepsilon(t)$ with $S(p)=1/p$ ($\operatorname{Re} p>0$), system $H(p)=1/(p+1)$ ($\operatorname{Re} p>-1$). The common region is $\operatorname{Re} p>0$:

$$G(p)=\frac{1}{p}\cdot\frac{1}{p+1}=\frac1p-\frac{1}{p+1}\quad\Longrightarrow\quad g(t)=\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

The inverse transform of the two terms follows from [(2.2)](#gl-2-2) with $p_0=0$ and $p_0=-1$. Checked directly: $g(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$ for $t>0$. The inversion formula [(2.1)](#gl-2-1), evaluated numerically on the line $\sigma=0.5/\mathrm s$, also gives $g(0.5\,\mathrm{s})=0.3935$, $g(1\,\mathrm{s})=0.6321$, $g(3\,\mathrm{s})=0.9502$ and $g(-1\,\mathrm{s})=0$, exactly $\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)$.

:::ltspice Entering the transfer function directly
⁠**Draw:** the RC circuit (`1Meg`, `1u`) from `in` to `rc`. Next to it a voltage-controlled voltage source `e`: control input at `in` and ground, output at net `lap`, value `Laplace=1/(1+s)`. This source is an LTI system given only by $H$: LTspice computes the impulse response from it and convolves the input with it. LTspice writes $s$ instead of $p$.

⁠**Source and directive:** `PULSE(0 1 0 1u 1u 100)`, `.tran 0 5 0 1m`.

⁠**What you see:** `V(rc)` and `V(lap)` lie on top of each other (difference below 0.001), reaching 0.3935 at 0.5 s, 0.6321 at 1 s and 0.9502 at 3 s. With the source value `AC 1` and `.ac dec 100 0.01 100`, LTspice shows $H(s)$ for $s=\mathrm{j}2\pi f$, i.e. only on the imaginary axis: $-3.0$ dB and $-45^\circ$ at 0.159 Hz.

⁠**For Exercise [6](#aufg-6):** source `PWL(0 0 10 10)`, the ramp $t\,\varepsilon(t)$ up to 10 s, and `.tran 0 10 0 1m`. Compare `V(rc)` with your result from Exercise [6](#aufg-6)(b).
:::

:::aufgabe Exercise 5 ★★ Cascade and derivative via the building blocks
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Use the building-block picture (without the convolution integral) to explain why two LTI systems in cascade have the transfer function $H_1(p)H_2(p)$. Why does it follow that convolution is commutative?

</li>

<li>

Derive $\mathcal{L}\{\dot s(t)\}=p\,S(p)$ from the inversion formula by differentiating it with respect to $t$.

</li>

</ol>

:::loesung
(a) The input consists of building blocks $\mathrm{e}^{pt}$ with weights $S(p)$. The first system multiplies each building block by $H_1(p)$, so the weights are then $H_1S$. The second multiplies by $H_2(p)$: $G=H_2H_1S$. So the cascade has $H=H_1H_2$. Because $H_1H_2=H_2H_1$, the result does not depend on the order, and since $h_1*h_2$ is the impulse response of the cascade, it follows that $h_1*h_2=h_2*h_1$.

(b) Differentiating under the integral acts only on $\mathrm{e}^{pt}$:

$$\dot s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\,\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}\,\mathrm{d} p=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}\bigl[p\,S(p)\bigr]\mathrm{e}^{pt}\,\mathrm{d} p.$$

This is the inversion formula with the weight $pS(p)$, so $\mathcal{L}\{\dot s\}=pS(p)$.
:::
:::

:::aufgabe Exercise 6 ★★ Ramp response of the RC low-pass filter
<span class="anker" id="aufg-6"></span>

Input $s(t)=t\,\varepsilon(t)$ with $S(p)=1/p^2$ for $\operatorname{Re} p>0$, basic transform pair [(2.5)](#gl-2-5).

<ol class="al">

<li>

Find $G(p)$ and its region of convergence.

</li>

<li>

Check the decomposition $G(p)=\frac{1}{p^2}-\frac1p+\frac{1}{p+1}$ and find $g(t)$.

</li>

<li>

Check: what is $g(0)$, and why must it be so? What is $\dot g(t)$?

</li>

<li>

How does $g(t)$ behave for $t\gg1$ s? Compare with Exercise [1](#aufg-1)c.

</li>

</ol>

:::loesung
(a) $G(p)=\dfrac{1}{p^2}\cdot\dfrac{1}{p+1}=\dfrac{1}{p^2(p+1)}$ for $\operatorname{Re} p>0$ (intersection of $\operatorname{Re} p>0$ and $\operatorname{Re} p>-1$).

(b) Over the common denominator: $\frac{1}{p^2}-\frac1p+\frac{1}{p+1}=\frac{(p+1)-p(p+1)+p^2}{p^2(p+1)}=\frac{1}{p^2(p+1)}$. Inverse transform with [(2.5)](#gl-2-5) and [(2.2)](#gl-2-2):

$$g(t)=\bigl(t-1+\mathrm{e}^{-t}\bigr)\varepsilon(t).$$

(c) $g(0)=0-1+1=0$: the capacitor voltage cannot jump, and the input starts at zero. $\dot g(t)=(1-\mathrm{e}^{-t})\varepsilon(t)$, exactly the step response. This fits: the ramp is the integral of the step, so the ramp response is the integral of the step response.

(d) For $t\gg1$ s, $\mathrm{e}^{-t}\approx0$ and $g(t)\approx t-1$: the output follows the ramp with a delay of $RC=1$ s, just as for the two-sided ramp in Exercise [1](#aufg-1)c. The difference is the building block $\mathrm{e}^{-t}$ (pole $-1$ of the system): the transient, which arises because here the ramp only starts at $t=0$.
:::
:::

## Stage 4: The integral becomes a sum

<span class="anker" id="stufe-4"></span>

:::zweck
The conjecture taken literally: for the signals that system theory almost always deals with, the signal is a *finite sum* of complex exponentials. The poles are the exponents.
:::

**The idea.** For networks of $R$, $L$, $C$ and for all systems described by a differential equation, $S(p)$ is a ratio of polynomials. For simple poles, the __partial fraction expansion__ writes it as

$$S(p)=A_0+\sum_{r=1}^{R}\frac{A_r}{p-p_r},\qquad A_r=\lim_{p\to p_r}(p-p_r)\,S(p).$$

Each term is the transform of *a single building block*: by [(2.2)](#gl-2-2), $A_r/(p-p_r)$ belongs to $A_r\,\mathrm{e}^{p_r t}\varepsilon(t)$ if the region of convergence lies to the right of the pole, and by [(2.4)](#gl-2-4) the constant term $A_0$ belongs to $A_0\,\delta(t)$. So for a right-sided signal

<span class="anker" id="gl-4-1"></span>
$$s(t)=A_0\,\delta(t)+\sum_{r=1}^{R}A_r\,\mathrm{e}^{p_r t}\,\varepsilon(t). \tag{4.1}$$

⁠**In short:** A right-sided signal with a rational Laplace transform is a finite sum of building blocks $\mathrm{e}^{p_r t}$. The poles are the exponents, and the partial fraction coefficients are the weights.

This means you can read off any such signal from its poles, using the map from Fig. [1](#abb-1): $\operatorname{Re} p_r$ tells you whether the building block decays or grows, and $\operatorname{Im} p_r$ how fast it oscillates. A conjugate pair of poles $p_r,p_r^*$ together gives a real damped oscillation. This is also the core of __stability__: a causal building block $\mathrm{e}^{p_r t}\varepsilon(t)$ decays if and only if $\operatorname{Re} p_r<0$. A causal system is therefore stable if all poles of $H(p)$ lie in the left half-plane.

**Example.** The step response from Stage [3](#stufe-3) has the poles $0$ and $-1$:

$$g(t)=\underbrace{1\cdot\mathrm{e}^{0\cdot t}}_{\text{pole }0\text{ (from }S)}\;\underbrace{-\;1\cdot\mathrm{e}^{-t}}_{\text{pole }-1\text{ (from }H)}\qquad(t>0).$$

The pole of the input gives the part that the input forces (the final voltage 1). The pole of the system gives the __natural response__ of the RC circuit, the decay with $RC=1$ s. This holds in general: the output $G=SH$ contains the poles of the input and the poles of the system.

:::zusatz Why the integral collapses into a sum: the residue theorem
This section needs the residue theorem from complex analysis. It explains why [(2.1)](#gl-2-1) and [(4.1)](#gl-4-1) are the same and why the region of convergence decides the signal.

Let $S(p)$ be a ratio of polynomials whose numerator degree is lower than its denominator degree, with simple poles.

<ul>

<li>

⁠**$t>0$:** Close the line of integration with a large semicircle to the *left*. There $\operatorname{Re} p\to-\infty$, so $|\mathrm{e}^{pt}|=\mathrm{e}^{\operatorname{Re} p\,t}\to0$, and $S(p)\to0$. In the limit the semicircle contributes nothing (Jordan's lemma). The closed path runs counterclockwise, and the residue theorem gives

$$s(t)=\sum_{\text{poles left of the line}}\operatorname*{Res}_{p=p_r}\bigl[S(p)\,\mathrm{e}^{pt}\bigr]=\sum_{\text{left}}A_r\,\mathrm{e}^{p_r t}.$$

The residue at a simple pole is $\lim_{p\to p_r}(p-p_r)S(p)\mathrm{e}^{pt}=A_r\mathrm{e}^{p_rt}$: exactly the partial fraction coefficient.

</li>

<li>

⁠**$t<0$:** Now $\mathrm{e}^{pt}$ vanishes for $\operatorname{Re} p\to+\infty$. Close to the *right*; the path runs clockwise, which gives a minus sign:

$$s(t)=-\sum_{\text{poles right of the line}}A_r\,\mathrm{e}^{p_r t}.$$

</li>

</ul>

⁠**Consequence:** The position of the line, that is, the region of convergence, decides which poles give causal building blocks (left of the line) and which give anticausal ones (right of the line). Example: $S(p)=\frac{1}{(p+1)(p+2)}=\frac{1}{p+1}-\frac{1}{p+2}$ (Fig. [5](#abb-5)). If the line lies between the poles, $-2<\sigma<-1$, then $-2$ acts for $t>0$ and $-1$ for $t<0$:

$$s(t)=-\mathrm{e}^{-2t}\varepsilon(t)-\mathrm{e}^{-t}\varepsilon(-t).$$

Evaluated numerically on the line $\sigma=-1.5/\mathrm s$: $s(1\,\mathrm{s})=-0.1353=-\mathrm{e}^{-2}$ and $s(-1\,\mathrm{s})=-2.7183=-\mathrm{e}^{1}$. If the line lies to the right of both poles, the same formula gives the causal signal $(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(t)$; if it lies to the left of both, it gives the anticausal signal $-(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(-t)$.

:::abbildung et3/k2residuen
Line of integration $\sigma=-1.5/\mathrm s$ in the strip $-2<\operatorname{Re} p<-1$ (blue) and the semicircles that close it (red).
:::
:::

:::aufgabe Exercise 7 ★★★ (Going further) Same formula, two signals
<span class="anker" id="aufg-7"></span>

$S(p)=\dfrac{1}{p+1}$.

<ol class="al">

<li>

Region of convergence $\operatorname{Re} p>-1$. Evaluate the inversion formula with the residue theorem, separately for $t>0$ and $t<0$.

</li>

<li>

The same for the region of convergence $\operatorname{Re} p<-1$.

</li>

<li>

Compare with the basic transform pairs [(2.2)](#gl-2-2) and [(2.3)](#gl-2-3). What does this teach you about the statement “$S(p)=1/(p+1)$” without a region of convergence?

</li>

</ol>

:::loesung
(a) Line to the right of the pole, for example $\sigma=0$. For $t>0$, close to the left: the pole $-1$ lies inside, $\operatorname*{Res}_{p=-1}\frac{\mathrm{e}^{pt}}{p+1}=\mathrm{e}^{-t}$, so $s(t)=\mathrm{e}^{-t}$. For $t<0$, close to the right: there is no pole to the right of the line, so $s(t)=0$. Together, $s(t)=\mathrm{e}^{-t}\varepsilon(t)$.

(b) Line to the left of the pole, for example $\sigma=-2$. For $t>0$, close to the left: no pole, $s(t)=0$. For $t<0$, close to the right: pole inside, clockwise path, $s(t)=-\mathrm{e}^{-t}$. Together, $s(t)=-\mathrm{e}^{-t}\varepsilon(-t)$.

(c) These are exactly the basic transform pairs [(2.2)](#gl-2-2) and [(2.3)](#gl-2-3) with $p_0=-1$. The statement “$S(p)=1/(p+1)$” alone does not determine the signal. Only with the region of convergence is it clear on which side of the line the pole lies and whether it gives a causal or an anticausal building block.
:::
:::

## Stage 5: Why the input is transformed too

<span class="anker" id="stufe-5"></span>

:::frage It makes sense to transform $h(t)$, so that I can multiply eigenfunctions by $H(p)$ and find the output. But transforming $s(t)$ doesn't seem to make sense at first; from a system-theory point of view I can't do anything with it. Sure, $s*h=h*s$, but $h(t)$ is usually not an eigenfunction, so I can't write $h(t)\cdot S(p)$. What does it mean, in terms of the system, to transform an arbitrary signal?
⁠**What is right about the question:** $H(p)$ says what the system does to a building block $\mathrm{e}^{pt}$. And $h(t)\cdot S(p)$ indeed makes no sense.

⁠**Where the reasoning goes wrong:** The input is almost never an eigenfunction either. A step, a speech signal or a rectangular pulse is not a single building block $\mathrm{e}^{pt}$. So $H(p)\cdot s(t)$ makes just as little sense as $h(t)\cdot S(p)$: $H(p)$ may only be applied to a building block, and for an arbitrary $s(t)$ it is not even clear which $p$ is meant. Before $H(p)$ can do anything, the input must be decomposed into building blocks. That is exactly what $S(p)$ does.

⁠**The correct view:** In the convolution theorem $G(p)=H(p)\,S(p)$, each factor has its own meaning in terms of the system:

<ul>

<li>

$S(p)$ is the *recipe of the input*: how much of the building block $\mathrm{e}^{pt}$ the input contains;

</li>

<li>

$H(p)$ is the *action of the system*: the number by which it multiplies this building block;

</li>

<li>

$G(p)$ is the recipe of the output.

</li>

</ul>

Without $S(p)$ you know only the action on individual building blocks, but not which building blocks arrive. $H(p)$ alone answers the question “What happens at the output?” only in the one special case where the input itself is a single building block.

⁠**Example: step and RC low-pass filter.** The step has the recipe $S(p)=1/p$. On the line $\sigma=0.5/\mathrm s$, $|S|=2$ at $f=0$, $0.16$ at 1 Hz and $0.016$ at 10 Hz. The fast building blocks are weak but present, and they form the sharp edge (Fig. [3](#abb-3): the more fast building blocks, the steeper the edge). The RC low-pass filter multiplies them by $|H|=0.67$, $0.15$ and $0.016$. In the output, the fast building blocks are therefore weaker by a further factor of roughly $2\pi f\cdot RC$ (for $f\gg1/(2\pi RC)=0.16$ Hz), and the edge is gone: $g(t)=1-\mathrm{e}^{-t}$ rises continuously. This explanation needs both transforms. $H$ alone only says “fast building blocks are weakened”; only $S$ says that the edge consists of fast building blocks.

⁠**And the symmetry $s*h=h*s$?** Mathematically the two signals are on an equal footing: you can also read $h$ as the input and $s$ as the “system”, and then $H(p)$ is the recipe and $S(p)$ the action. System theory assigns the roles only according to the physics: one signal comes from outside, the other describes the circuit. In the transform domain, *both* are always transformed.
:::

**Further reasons to transform a signal on its own.**

<ul>

<li>

⁠**Measuring a system.** If you measure the input and output of an unknown system, $H(p)=G(p)/S(p)$ gives you the system. For this you transform two signals, each on its own (Exercise [9](#aufg-9)).

</li>

<li>

⁠**Understanding the signal itself.** The sound of a struck bell is a sum of damped oscillations, each one a conjugate pair of poles. $\operatorname{Im} p_r$ is the pitch of a partial, $-\operatorname{Re} p_r$ its decay rate. A few poles describe the whole sound. An instrument that displays a spectrum does the same on the line $\sigma=0$.

</li>

<li>

⁠**Convolution without a system.** Convolution superposes shifted, weighted copies of a signal. The system is one interpretation of this operation, not the only one. An example with no system at all is the sum of two dice, treated in the article on convolution ([Part 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)).

</li>

</ul>

:::ltspice A network for two measurements
⁠**Draw:** the network you found in Exercise [9](#aufg-9)(c), with the source `PULSE(0 1 0 1u 1u 100)` at its input and its output at net `out`. Next to it, not connected to the circuit, a behavioural source `bv` at net `mess` with `V=1-exp(-2*time)`. It plays the measured output curve.

⁠**Directives:** `.tran 0 3 0 1m`, `.meas tran dev MAX abs(V(out)-V(mess))`.

⁠**What you see:** If the network and the component values are right, `V(out)` and `V(mess)` lie on top of each other, and the largest deviation `dev` is practically zero (below $10^{-5}$). In this way, compare the curves with your result from Exercise [9](#aufg-9)(c).
:::

:::aufgabe Exercise 8 ★★ Which building blocks form the edge?
<span class="anker" id="aufg-8"></span>

Input $\varepsilon(t)$, system: RC low-pass filter with $RC=1$ s. Consider the building blocks on the line $\sigma=0.5/\mathrm s$.

<ol class="al">

<li>

Compute $|S(p)|$, $|H(p)|$ and $|G(p)|$ for $f=0$, $1$ Hz and $10$ Hz.

</li>

<li>

By what factor does the system weaken the building blocks at 10 Hz more than those at 1 Hz?

</li>

<li>

Use (a) and Fig. [3](#abb-3) to explain why the output has no edge. Why is $H(p)$ alone not enough for this explanation?

</li>

</ol>

:::loesung
(a) With $p=0.5+\mathrm{j}2\pi f$ (in $1/\mathrm s$), $S=1/p$, $H=1/(p+1)$, $G=SH$:

| $f$ | $\vert S(p)\vert $ | $\vert H(p)\vert $ | $\vert G(p)\vert $ |
|---|---|---|---|
| 0 | 2 | 0.667 | 1.33 |
| 1 Hz | 0.159 | 0.155 | 0.0246 |
| 10 Hz | 0.0159 | 0.0159 | 0.000253 |

(b) $0.155/0.0159\approx9.7$, so almost a factor of 10, just like the frequency. For large $|p|$, $|H|\approx1/|p|\approx1/(2\pi f)$.

(c) The edge of the step consists of the fast building blocks: in Fig. [3](#abb-3) it becomes steeper the more of them are included. In the input their weights fall like $1/f$, in the output like $1/f^2$. In the output the fast building blocks are so weak that no edge forms any more, and $g(t)$ rises continuously. $H(p)$ alone only says that fast building blocks are weakened. That the edge consists of exactly these building blocks is a statement about the input, and that statement is contained in $S(p)$.
:::
:::

:::aufgabe Exercise 9 ★★ An unknown system from two measurements
<span class="anker" id="aufg-9"></span>

A voltage of 1 V is applied to an unknown causal LTI system at time $t=0$, $s(t)=\varepsilon(t)$ in V. At the output one measures $g(t)=\bigl(1-\mathrm{e}^{-2t}\bigr)\varepsilon(t)$ in V ($t$ in s).

<ol class="al">

<li>

Transform both signals, each on its own.

</li>

<li>

Find $H(p)$ and from it $h(t)$.

</li>

<li>

Which network could it be? What value do you get?

</li>

<li>

Which pole in $G(p)$ comes from the input, and which from the system?

</li>

</ol>

:::loesung
(a) $S(p)=\dfrac1p$ for $\operatorname{Re} p>0$. $G(p)=\dfrac1p-\dfrac{1}{p+2}=\dfrac{2}{p(p+2)}$ for $\operatorname{Re} p>0$ (basic transform pair [(2.2)](#gl-2-2) with $p_0=0$ and $p_0=-2$).

(b) $H(p)=\dfrac{G(p)}{S(p)}=\dfrac{2}{p+2}$. Since the system is causal, the region of convergence lies to the right of the pole: $\operatorname{Re} p>-2$. With [(2.2)](#gl-2-2): $h(t)=2\,\mathrm{e}^{-2t}\varepsilon(t)$ in $1/\mathrm s$.

(c) An RC low-pass filter has $H(p)=\dfrac{1}{1+pRC}=\dfrac{1/RC}{p+1/RC}$. Comparing with $\dfrac{2}{p+2}$ gives $RC=0.5$ s, for example $R=500\,\mathrm{k\Omega}$ and $C=1$ µ F. (Any other network with the same transfer function would behave identically at its terminals. Measurements at the input and output reveal only $H$, not the components.)

(d) The pole $p=0$ comes from the input (the step), the pole $p=-2$ from the system. In the division $G/S$, exactly the pole of the input cancels.
:::
:::

:::merke Key points so far
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
