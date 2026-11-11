---
title: Stage 2: Periodic signals, the Fourier series
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Fourier Series and Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Chapter 3: Fourier Series and Transform
order: 3230300
summary: A periodic signal repeats itself after T .
tags: fundamental frequency, harmonics, Fourier series, DC component, orthogonal
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
A periodic signal repeats itself after $T$. It can be built from oscillations, but only from very specific ones. This stage shows which ones, and how to find their weights.
:::

**The idea.** An oscillation $\mathrm{e}^{\mathrm{j}2\pi ft}$ repeats itself after $T$ if and only if $fT$ is an integer. So a signal with the period $T$ contains only the frequencies $f_k=kF$ with the __fundamental frequency__ $F=1/T$, the __harmonics__:

<span class="anker" id="gl-2-1"></span>
$$s_p(t)=\sum_{k=-\infty}^{\infty}S_p(k)\,\mathrm{e}^{\mathrm{j}2\pi kFt}. \tag{2.1}$$

This is the __Fourier series__ (synthesis). $S_p(k)$ is the complex weight of the $k$th harmonic.

**Real signals.** For a real signal, $s_p=s_p^*$. Conjugating [(2.1)](#gl-2-1) turns $\mathrm{e}^{\mathrm{j}2\pi kFt}$ into the oscillation with $-k$. Comparing the coefficients gives

$$S_p(-k)=S_p^*(k).$$

Each pair $k,-k$ then gives $2\operatorname{Re}\{S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}\}$, a real cosine oscillation. With $S_p(k)=|S_p(k)|\,\mathrm{e}^{\mathrm{j}\varphi_p(k)}$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} s_p(t)&=S_p(0)+2\sum_{k=1}^{\infty}|S_p(k)|\cos\bigl(2\pi kFt+\varphi_p(k)\bigr)\\ &=S_p(0)+2\sum_{k=1}^{\infty}\Bigl[\operatorname{Re}\{S_p(k)\}\cos(2\pi kFt)-\operatorname{Im}\{S_p(k)\}\sin(2\pi kFt)\Bigr]. \end{aligned} \tag{2.2|2.3}$$

The phase $\varphi_p(k)$ is found as for any complex number, with $\arctan$ and the quadrant correction ($+\pi$ for a negative real part). $S_p(0)$ is the __DC component__, the mean value of the signal.

**Finding the weights: orthogonality.** How do you extract a single $S_p(n)$ from the sum? Multiply by $\mathrm{e}^{-\mathrm{j}2\pi nFt}$ and average over one period. In the process, all other harmonics vanish:

<span class="anker" id="gl-2-4"></span>
$$\frac1T\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\,\mathrm{d} t=\begin{cases}1&k=n\\0&k\neq n\end{cases}. \tag{2.4}$$

For $k\neq n$, the phasor $\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}$ makes exactly $|k-n|$ full turns during the period, and its mean value is zero. For $k=n$ it stands still. Oscillations of different frequencies are therefore called __orthogonal__. What remains is:

:::satz Theorem 2.1 (Fourier series)
<span class="anker" id="satz-2-1"></span>

A signal with the period $T=1/F$ and finite power (the mean of $|s(t)|^2$ over one period is finite) has the representation [(2.1)](#gl-2-1) with

<span class="anker" id="gl-2-5"></span>
$$S_p(k)=\frac1T\int_{t_1}^{t_1+T}s_p(t)\,\mathrm{e}^{-\mathrm{j}2\pi kFt}\,\mathrm{d} t, \tag{2.5}$$

where $t_1$ is arbitrary (analysis). The equals sign in [(2.1)](#gl-2-1) holds in the mean-square sense: the mean of $\bigl|s_p(t)-\sum_{|k|\le N}S_p(k)\,\mathrm{e}^{\mathrm{j}2\pi kFt}\bigr|^2$ over one period, the power of the error, tends to zero as $N\to\infty$. At individual points, for example at jumps, the series need not give the value of the signal.
:::

⁠**How to read it:** $S_p(k)$ is the mean value of the signal after it has been “counter-rotated” with the $k$th harmonic. If the harmonic is contained in the signal, the phasor no longer rotates at this point, and its share remains after averaging. $S_p(0)$ is simply the mean value.

:::herleitung Analysis formula
Multiply [(2.1)](#gl-2-1) by $\mathrm{e}^{-\mathrm{j}2\pi nFt}$, integrate over one period, interchange sum and integral:

$$\int_0^Ts_p(t)\mathrm{e}^{-\mathrm{j}2\pi nFt}\mathrm{d} t=\sum_kS_p(k)\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\mathrm{d} t=S_p(n)\,T.$$

For $k\neq n$ the integral is $\frac{\mathrm{e}^{\mathrm{j}2\pi(k-n)FT}-1}{\mathrm{j}2\pi(k-n)F}=0$, because $\mathrm{e}^{\mathrm{j}2\pi(k-n)}=1$. Since the integrand has the period $T$, you may integrate over any interval of length $T$.
:::

::::beispiel a finite series
$s_p(t)=1+2\cos(2\pi Ft)+\sin(4\pi Ft)$. With Euler's formulas you can read off the coefficients without integrating:

$$2\cos(2\pi Ft)=\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft},\qquad\sin(4\pi Ft)=\frac{1}{2\mathrm{j}}\mathrm{e}^{\mathrm{j}4\pi Ft}-\frac{1}{2\mathrm{j}}\mathrm{e}^{-\mathrm{j}4\pi Ft},$$

so $S_p(0)=1$, $S_p(\pm1)=1$, $S_p(2)=-\tfrac{\mathrm{j}}{2}$, $S_p(-2)=\tfrac{\mathrm{j}}{2}$, all others zero. Check: $S_p(-2)=S_p^*(2)$.
::::

::::beispiel the square wave
For the reference model (1 for $|t|\le T_1/2$ with $T_1=T/2$):

<span class="anker" id="gl-2-6"></span>
$$S_p(0)=\frac{T_1}{T},\qquad S_p(k)=\frac1T\int_{-T_1/2}^{T_1/2}\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac{\sin(\pi kT_1/T)}{\pi k}\quad(k\neq0). \tag{2.6}$$

With $T_1=T/2$: $S_p(0)=0.5$, $S_p(\pm1)=1/\pi=0.318$, $S_p(\pm2)=0$, $S_p(\pm3)=-0.106$, $S_p(\pm5)=0.064$. The even harmonics are missing because $\sin(\pi k/2)=0$ for even $k$. All coefficients are real because the signal is even, $s(-t)=s(t)$: the imaginary part of $S_p(k)$ is $-\frac1T\int_{-T/2}^{T/2}s(t)\sin(2\pi kFt)\,\mathrm{d} t$ and vanishes because the integrand is odd: it changes sign under $t\to-t$, so the contributions left and right of zero cancel. Figure [1](#abb-1) shows them for two duty cycles: the narrower the pulse, the more slowly the coefficients decay.

:::abbildung et3/k3koeff 1
Fourier coefficients of the square wave (0/1) for two pulse widths. Dashed: the envelope $\frac{T_1}{T}\operatorname{si}(\pi kT_1/T)$. For $T_1=T/2$ the even harmonics are missing, for $T_1=T/4$ every fourth one.
:::
::::

:::frage Why are there no frequencies between the harmonics in a periodic signal?
Because every oscillation in the sum must itself have the period $T$; otherwise the sum would not be periodic. An oscillation with $f=1.5F$ has made only one and a half turns after $T$ and is in a different position than at the start. No weight, however cleverly chosen, can compensate for this, because different frequencies are orthogonal and cannot cancel each other.
:::

:::aufgabe Exercise 1 ★ Reading off coefficients
<span class="anker" id="aufg-1"></span>

$s_p(t)=\frac12+\cos\bigl(2\pi Ft+\frac\pi3\bigr)+\frac12\sin(6\pi Ft)$.

<ol class="al">

<li>

Find all $S_p(k)$ using Euler's formulas. Check $S_p(-k)=S_p^*(k)$.

</li>

<li>

Give $|S_p(1)|$ and $\varphi_p(1)$ and compare with [(2.2)](#gl-2-2).

</li>

</ol>

:::loesung
(a) $\cos(x+\frac\pi3)=\frac12\mathrm{e}^{\mathrm{j}\pi/3}\mathrm{e}^{\mathrm{j} x}+\frac12\mathrm{e}^{-\mathrm{j}\pi/3}\mathrm{e}^{-\mathrm{j} x}$ and $\frac12\sin(3x)=\frac{1}{4\mathrm{j}}\mathrm{e}^{\mathrm{j}3x}-\frac{1}{4\mathrm{j}}\mathrm{e}^{-\mathrm{j}3x}$ with $x=2\pi Ft$:

$$S_p(0)=\tfrac12,\quad S_p(\pm1)=\tfrac12\mathrm{e}^{\pm\mathrm{j}\pi/3}=0.25\pm0.433\mathrm{j},\quad S_p(3)=-\tfrac{\mathrm{j}}{4},\quad S_p(-3)=\tfrac{\mathrm{j}}{4},$$

all others zero. $S_p(-1)=S_p^*(1)$ and $S_p(-3)=S_p^*(3)$ hold.

(b) $|S_p(1)|=\frac12$, $\varphi_p(1)=60^\circ$. In [(2.2)](#gl-2-2): $2\cdot\frac12\cos(2\pi Ft+60^\circ)$, exactly the cosine term of the signal. (Power by Parseval: $\frac14+2\cdot\frac14+2\cdot\frac1{16}=0.875$.)
:::
:::

:::aufgabe Exercise 2 ★★ The narrow square wave
<span class="anker" id="aufg-2"></span>

Square wave with $T_1=T/4$.

<ol class="al">

<li>

Compute $S_p(0)$, $S_p(1)$, $S_p(2)$ and $S_p(4)$ from [(2.6)](#gl-2-6).

</li>

<li>

Why is $S_p(4)=0$? Interpret it using orthogonality: how many periods of the fourth harmonic fit into the pulse?

</li>

</ol>

:::loesung
(a) $S_p(0)=\frac14$, $S_p(1)=\frac{\sin(\pi/4)}{\pi}=0.225$, $S_p(2)=\frac{\sin(\pi/2)}{2\pi}=0.159$, $S_p(4)=\frac{\sin\pi}{4\pi}=0$.

(b) The fourth harmonic has the period $T/4$, exactly the pulse width. The analysis formula integrates $\mathrm{e}^{-\mathrm{j}2\pi4Ft}$ over the pulse, that is, over exactly one full turn of the phasor. The mean value is zero. In general, $S_p(k)$ vanishes when an integer number of periods of the $k$th harmonic fits into the pulse.
:::
:::
