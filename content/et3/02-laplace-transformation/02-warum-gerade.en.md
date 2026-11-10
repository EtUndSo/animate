---
title: Stage 1: Why $\mathrm{e}^{pt}$ in particular
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Laplace Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: Chapter 2: Laplace Transform
order: 3220200
summary: If you insert e pt into the convolution integral, the result is H(p)\,e pt : e pt is an eigenfunction.
tags: growth rate, frequency
lang: en
---

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

:::abbildung et3/k2bausteine 1
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

Ideal low-pass filter without delay, $H(f)=1$ in the whole passband: every signal made up only of oscillations with frequencies in the passband comes out unchanged and is an eigenfunction with eigenvalue 1.

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
