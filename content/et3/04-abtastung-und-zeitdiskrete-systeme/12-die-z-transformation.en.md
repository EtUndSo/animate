---
title: Stage 11: The z-transform
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Sampling and Discrete-Time Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Chapter 4: Sampling and Discrete-Time Systems
order: 3241200
summary: Just as the Laplace transform extends the Fourier transform (Chapter 2), the z-transform extends the discrete-time Fourier transform: first weight exponentially, then transform.
tags: unit circle
lang: en
---

<span class="anker" id="stufe-11"></span>

:::zweck
Just as the Laplace transform extends the Fourier transform ([Chapter 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)), the z-transform extends the discrete-time Fourier transform: first weight exponentially, then transform.
:::

**The idea.** Multiply the sequence by $\rho^{-n}$ ($\rho>0$) and transform: $\sum_ns(n)\rho^{-n}\mathrm{e}^{-\mathrm{j}2\pi fn}$. With $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$ this becomes a power series in $z^{-1}$. Equivalently: $z^n$ is an eigenfunction of every LSI system, because $z^{n-k}=z^{-k}z^n$, and the eigenvalue is $H(z)$:

$$z^n*h(n)=\sum_kh(k)z^{n-k}=z^n\sum_kh(k)z^{-k}=H(z)\,z^n.$$

:::satz Theorem 11.1 (z-transform)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n},\qquad s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{n-1}\,\mathrm{d} z, \tag{11.1}$$

where the contour integral runs counterclockwise around a circle $|z|=\rho$ in the region of convergence.
:::

⁠**How to read it:** on the circle $|z|=\rho$ lies one period of the spectrum of the weighted sequence $s(n)\rho^{-n}$. On the __unit circle__ $|z|=1$, $S(z)$ is the ordinary spectrum $S_\mathrm a(f)$, provided the unit circle lies in the region of convergence. In this way the plane of the Laplace transform is mapped onto the z-plane: the imaginary axis becomes the unit circle, and the left half-plane becomes its interior.

**Basic pairs and region of convergence.** With the geometric series:

<span class="anker" id="gl-11-2"></span>
$$\varepsilon(n)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{1}{1-bz^{-1}}=\frac{z}{z-b},\quad|z|>|b|;\qquad -\varepsilon(-n-1)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{z}{z-b},\quad|z|<|b|. \tag{11.2}$$

As with the Laplace transform, the same expression belongs to two signals; only the region of convergence decides. For right-sided sequences it lies outside the circle through the outermost pole, for left-sided ones inside the circle through the innermost pole, and for two-sided ones it is a ring. For $b^{|n|}$ with $0<b<1$ this is the ring $b<|z|<1/b$.

**Rules of calculation.** Convolution becomes a product: $g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$. A delay by $n_0$ clock cycles becomes multiplication by $z^{-n_0}$. This turns the difference equation [(5.2)](zeitdiskrete-signale-und-die-diskrete-faltung.html#gl-5-2) into

<span class="anker" id="gl-11-3"></span>
$$H(z)=\frac{G(z)}{S(z)}=\frac{\sum_{q=0}^{Q}a_q\,z^{-q}}{1-\sum_{p=1}^{P}b_p\,z^{-p}}. \tag{11.3}$$

For the system from Exercise [6](ein-rekursives-system.html#aufg-6), $H(z)=\frac{1+0.5z^{-1}}{1-0.6z^{-1}}$: zero at $z=-0.5$, pole at $z=0.6$.

:::satz Theorem 11.2 (Stability)
<span class="anker" id="satz-11-2"></span>

A causal LSI system is stable if and only if all poles of $H(z)$ lie inside the unit circle.
:::

⁠**Why:** causal means a region of convergence outside the outermost pole. Stable means $\sum|h(n)|<\infty$; then $H(z)$ converges on the unit circle, so the unit circle belongs to the region of convergence. Both together are possible only if the outermost pole lies inside the unit circle. For the recursive system with $H(z)=\frac{1}{1-bz^{-1}}$ this again means $|b|<1$.

::::beispiel
$s(n)=0.5^n\cos(\pi n/3)\,\varepsilon(n)$. With $\cos=\frac12(\mathrm{e}^{\mathrm{j}\pi n/3}+\mathrm{e}^{-\mathrm{j}\pi n/3})$ and [(11.2)](#gl-11-2) for $b=0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}$:

$$S(z)=\frac12\Bigl[\frac{1}{1-0.5\mathrm{e}^{\mathrm{j}\pi/3}z^{-1}}+\frac{1}{1-0.5\mathrm{e}^{-\mathrm{j}\pi/3}z^{-1}}\Bigr]=\frac{1-0.25z^{-1}}{1-0.5z^{-1}+0.25z^{-2}},\qquad|z|>0.5.$$

Poles at $0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}=0.25\pm0.433\mathrm{j}$, zeros at $z=0$ and $z=0.25$ (Fig. [8](#abb-8)). The magnitude of the poles gives the decay per clock cycle (0.5), their angle gives the oscillation ($\pi/3$ per clock cycle, so six clock cycles per period).

:::abbildung et3/k4zebene 8
z-plane of the example: poles (crosses) at $0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}$, zeros (circles) at 0 and 0.25. The region of convergence (blue) lies outside the circle through the poles and contains the unit circle. Read as an impulse response, the sequence describes a causal and stable system.
:::
::::

:::aufgabe Exercise 11 ★★ Applying the z-transform
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Confirm the numerator and denominator of $S(z)$ in the example by bringing the two fractions to a common denominator.

</li>

<li>

Does the spectrum $S_\mathrm a(f)$ of the example signal exist? Justify your answer using the region of convergence.

</li>

</ol>

:::loesung
(a) Common denominator $(1-az^{-1})(1-a^*z^{-1})=1-(a+a^*)z^{-1}+|a|^2z^{-2}$ with $a=0.5\mathrm{e}^{\mathrm{j}\pi/3}$: $a+a^*=2\cdot0.25=0.5$, $|a|^2=0.25$. Numerator $\frac12[2-(a+a^*)z^{-1}]=1-0.25z^{-1}$.

(b) Yes. The region of convergence $|z|>0.5$ contains the unit circle.
:::
:::

:::aufgabe Exercise 12 ★★ Causal or stable
<span class="anker" id="aufg-12"></span>

$H(z)=\dfrac{1}{1-2z^{-1}}$.

<ol class="al">

<li>

Which impulse response belongs to the region of convergence $|z|>2$, and which to $|z|<2$?

</li>

<li>

Which of the two is stable, and which is causal? Is there one that is both?

</li>

</ol>

:::loesung
(a) $|z|>2$: $h(n)=2^n\varepsilon(n)$. $|z|<2$: $h(n)=-2^n\varepsilon(-n-1)$, so $-\frac12,-\frac14,\dots$ for $n=-1,-2,\dots$

(b) The first is causal but unstable (it grows). The second is stable ($\sum_{n\le-1}2^n=1$) but anticausal. Both at once is impossible: the pole at $z=2$ lies outside the unit circle, and then the region of convergence cannot both lie outside the pole and contain the unit circle.
:::
:::
