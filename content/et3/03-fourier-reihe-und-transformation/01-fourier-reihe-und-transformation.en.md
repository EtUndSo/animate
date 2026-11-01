---
title: Fourier Series and the Fourier Transform
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Fourier Series and Transform
order: 3230100
summary: Every signal as a superposition of oscillations
tags: spectrum, frequency response, fundamental frequency, harmonics, Fourier series, DC component, orthogonal, power
lang: en
---

## What this is about

[Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html) showed that every signal is a superposition of building blocks $\mathrm{e}^{pt}$, and that an LTI system merely multiplies each building block by a number. The Fourier description uses only the building blocks on the imaginary axis, $p=\mathrm{j}2\pi f$: pure oscillations $\mathrm{e}^{\mathrm{j}2\pi ft}$ that neither grow nor decay. This has a big advantage. An oscillation has a frequency that you can hear, measure and filter. The __spectrum__ $S(f)$ tells you with which amplitude and phase each frequency is contained in the signal.

:::merke The answer in three sentences (by the end of the article they should feel obvious)
<ol>

<li>

A periodic signal is a sum of oscillations at multiples of the fundamental frequency (Fourier series); a non-repeating signal is an integral over all frequencies (Fourier integral).

</li>

<li>

Every oscillation $\mathrm{e}^{\mathrm{j}2\pi ft}$ is an eigenfunction: an LTI system multiplies it by $H(f)$, and that is why convolution becomes the product $G(f)=S(f)\,H(f)$.

</li>

<li>

All the rules of calculation (shift, stretching, modulation, symmetry) follow from what the respective operation does to a single oscillation.

</li>

</ol>
:::

**One principle behind all the results.**

| Result | Where it comes from |
|---|---|
| Frequency response $H(f)$ | eigenvalue of the oscillation $\mathrm{e}^{\mathrm{j}2\pi ft}$ (Stage [1](#stufe-1)) |
| Fourier series, only multiples of $F$ | only these oscillations have the period $T$ (Stage [2](#stufe-2)) |
| Analysis formula of the series | oscillations of different frequencies are orthogonal (Stage [2](#stufe-2)) |
| Parseval, Gibbs, LTI with periodic input | each harmonic on its own (Stage [3](#stufe-3)) |
| Fourier integral | period $\to\infty$, the lines move closer together (Stage [4](#stufe-4)) |
| $S(-f)=S^*(f)$ for real signals | oscillations occur in conjugate pairs (Stage [5](#stufe-5)) |
| Shift, stretching, derivative, modulation | what the operation does to $\mathrm{e}^{\mathrm{j}2\pi ft}$ (Stage [6](#stufe-6)) |
| Symmetry (duality) | forward and inverse transform differ only in the sign (Stage [6](#stufe-6)) |
| Line spectra, Dirac comb, step | limiting cases with Dirac impulses (Stage [8](#stufe-8)) |
| Hilbert transform | a causal signal is determined by one half (Stage [9](#stufe-9)) |
| Short-time Fourier transform | spectrum of a segment (Stage [10](#stufe-10)) |

**How to work with this article.** Each stage has the idea, typical questions with answers you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise.

:::merke The reference model for this article
<ul>

<li>

⁠**Square wave** between 0 and 1 with the period $T=2\pi$ s and the duty cycle $\frac12$: 1 for $|t|\le T/4$, 0 for $T/4<|t|\le T/2$, continued periodically. Fundamental frequency $F=1/T=0.159$ Hz, so $2\pi F=1/\mathrm s$.

</li>

<li>

⁠**RC low-pass filter** with $RC=1$ s, $H(f)=1/(1+\mathrm{j}2\pi f\,RC)$. At the $k$th harmonic of the square wave, $2\pi kF\cdot RC=k$, so $H(kF)=1/(1+\mathrm{j} k)$.

</li>

<li>

⁠**Rectangular pulse** $\operatorname{rect}(t)$ and $\operatorname{si}(x)=\sin(x)/x$.

</li>

</ul>

The script `rechnung_kap3.py` recomputes the numbers and curves.
:::

## Stage 1: Oscillations as eigenfunctions

<span class="anker" id="stufe-1"></span>

:::zweck
Of the building blocks $\mathrm{e}^{pt}$, only the pure oscillations are used from now on. This stage shows what an LTI system does to them.
:::

For purely imaginary $p=\mathrm{j}2\pi f$, the building block becomes an oscillation with constant amplitude:

$$\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft).$$

Like every building block, it is an eigenfunction of every LTI system (delaying is multiplying by $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$):

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft},\qquad H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t. \tag{1.1}$$

$H(f)$ is called the __frequency response__ or transfer function. Its magnitude says how strongly the oscillation of frequency $f$ is amplified or attenuated, and its phase says how far it is shifted. Two systems in cascade multiply one after the other: $H(f)=H_1(f)H_2(f)$. Where the Laplace transform $H(p)$ exists on the imaginary axis, $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$.

⁠**In short:** The frequency response is the number by which an LTI system multiplies a pure oscillation.

## Stage 2: Periodic signals, the Fourier series

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

A signal with the period $T=1/F$ and finite power has the representation [(2.1)](#gl-2-1) with

<span class="anker" id="gl-2-5"></span>
$$S_p(k)=\frac1T\int_{t_1}^{t_1+T}s_p(t)\,\mathrm{e}^{-\mathrm{j}2\pi kFt}\,\mathrm{d} t, \tag{2.5}$$

where $t_1$ is arbitrary (analysis).
:::

⁠**How to read it:** $S_p(k)$ is the mean value of the signal after it has been “counter-rotated” with the $k$th harmonic. If the harmonic is contained in the signal, the phasor no longer rotates at this point, and its share remains after averaging. $S_p(0)$ is simply the mean value.

:::herleitung Analysis formula
Multiply [(2.1)](#gl-2-1) by $\mathrm{e}^{-\mathrm{j}2\pi nFt}$, integrate over one period, interchange sum and integral:

$$\int_0^Ts_p(t)\mathrm{e}^{-\mathrm{j}2\pi nFt}\mathrm{d} t=\sum_kS_p(k)\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\mathrm{d} t=S_p(n)\,T.$$

For $k\neq n$ the integral is $\frac{\mathrm{e}^{\mathrm{j}2\pi(k-n)FT}-1}{\mathrm{j}2\pi(k-n)F}=0$, because $\mathrm{e}^{\mathrm{j}2\pi(k-n)}=1$. Since the integrand has the period $T$, you may integrate over any interval of length $T$.
:::

**Example: a finite series.** $s_p(t)=1+2\cos(2\pi Ft)+\sin(4\pi Ft)$. With Euler's formulas you can read off the coefficients without integrating:

$$2\cos(2\pi Ft)=\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft},\qquad\sin(4\pi Ft)=\frac{1}{2\mathrm{j}}\mathrm{e}^{\mathrm{j}4\pi Ft}-\frac{1}{2\mathrm{j}}\mathrm{e}^{-\mathrm{j}4\pi Ft},$$

so $S_p(0)=1$, $S_p(\pm1)=1$, $S_p(2)=-\tfrac{\mathrm{j}}{2}$, $S_p(-2)=\tfrac{\mathrm{j}}{2}$, all others zero. Check: $S_p(-2)=S_p^*(2)$.

**Example: the square wave.** For the reference model (1 for $|t|\le T_1/2$ with $T_1=T/2$):

<span class="anker" id="gl-2-6"></span>
$$S_p(0)=\frac{T_1}{T},\qquad S_p(k)=\frac1T\int_{-T_1/2}^{T_1/2}\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac{\sin(\pi kT_1/T)}{\pi k}\quad(k\neq0). \tag{2.6}$$

With $T_1=T/2$: $S_p(0)=0.5$, $S_p(\pm1)=1/\pi=0.318$, $S_p(\pm2)=0$, $S_p(\pm3)=-0.106$, $S_p(\pm5)=0.064$. The even harmonics are missing because $\sin(\pi k/2)=0$ for even $k$. All coefficients are real because the signal is even (Stage [5](#stufe-5)). Figure [1](#abb-1) shows them for two duty cycles: the narrower the pulse, the more slowly the coefficients decay.

:::abbildung et3/k3koeff
Fourier coefficients of the square wave (0/1) for two pulse widths. Dashed: the envelope $\frac{T_1}{T}\operatorname{si}(\pi kT_1/T)$. For $T_1=T/2$ the even harmonics are missing, for $T_1=T/4$ every fourth one.
:::

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

## Stage 3: Power, convergence and LTI systems

<span class="anker" id="stufe-3"></span>

:::zweck
How much does each harmonic contribute to the signal, how well does a truncated series approximate the signal, and what does an LTI system do with a periodic input?
:::

:::satz Theorem 3.1 (Parseval for Fourier series)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=-\infty}^{\infty}|S_p(k)|^2. \tag{3.1}$$
:::

⁠**How to read it:** The average __power__ of the signal is the sum of the powers of the individual harmonics. Cross terms drop out because different harmonics are orthogonal. For the square wave, $L_s=\frac12$. The DC component contributes $0.25$, that is, 50 %. With $k=\pm1$ it is 90.5 %, with $|k|\le3$ 95.0 %, with $|k|\le9$ 98.0 %.

:::herleitung Parseval
$|s_p|^2=s_ps_p^*=\sum_k\sum_lS_p(k)S_p^*(l)\,\mathrm{e}^{\mathrm{j}2\pi(k-l)Ft}$. Averaged over one period, by [(2.4)](#gl-2-4) only $k=l$ remains: $\sum_k|S_p(k)|^2$.
:::

**Truncated series and the Gibbs phenomenon.** If you take only the harmonics up to $|k|\le N$, the __partial sum__ is $s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$. The power of the error $s_p-s_{p,N}$ is the sum of the omitted $|S_p(k)|^2$ and tends to zero as $N\to\infty$ if the signal has finite power. At a jump, however, an overshoot remains (Fig. [2](#abb-2)): it becomes narrower as $N$ grows, but its height tends to about 9 % of the jump height (10.0 % for $N=3$, 9.1 % for $N=9$, 9.0 % for $N=27$, limit 8.95 %). This is the __Gibbs phenomenon__. It does not contradict convergence: the area under the overshoot, and with it the error power, still tends to zero.

:::abbildung et3/k3gibbs
Partial sums of the square wave ($T=2\pi$ s) with the harmonics up to $|k|\le N$. At the edges an overshoot of about 9 % of the jump height remains, which only becomes narrower as $N$ grows.
:::

**Periodic input to an LTI system.** Each harmonic is an eigenfunction and is multiplied by $H(kF)$. The output therefore has the same period, and its coefficients are

<span class="anker" id="gl-3-2"></span>
$$G_p(k)=S_p(k)\,H(kF). \tag{3.2}$$

In the reference model, $H(kF)=1/(1+\mathrm{j} k)$. The fundamental is transmitted with $|H|=0.707$ and $-45^\circ$, the third harmonic with $0.316$ and $-71.6^\circ$, the fifth with $0.196$ and $-78.7^\circ$. At the output, the third harmonic is only 15 % as large as the first, instead of 33 % at the input. The RC circuit rounds off the edges (Fig. [3](#abb-3)). The output swings between 0.041 and 0.959.

:::abbildung et3/k3rc
Square wave through the RC low-pass filter with $RC=1$ s, computed as a sum of harmonics with $G_p(k)=S_p(k)/(1+\mathrm{j} k)$. The output charges and discharges exponentially between 0.041 and 0.959.
:::

:::frage Isn't a calculation over infinitely many harmonics much more laborious than the differential equation?
For a single square wave through an RC circuit, yes: the charging and discharging curves can be written down directly. In return, the series shows *why* the output looks the way it does. The edges consist of the high harmonics, and it is exactly these that the RC circuit attenuates. Moreover, [(3.2)](#gl-3-2) works for every LTI system, even for those whose differential equation is not known at all, only their measured frequency response.
:::

:::ltspice Square wave through the RC circuit
⁠**Draw:** the RC circuit (`res` with `1Meg`, `cap` with `1u`) with the source `PULSE(0 1 0 1u 1u {pi} {2*pi})`: period $2\pi$ s, duty cycle $\frac12$.

⁠**Directives:** `.tran 0 {20*pi} 0 1m`, `.four {1/(2*pi)} 5 V(in) V(out)` and `.options plotwinsize=0`. The last one switches off data compression; without it `.four` is inaccurate. `.four` decomposes the last period into harmonics and writes the result to the SPICE Error Log.

⁠**What you see:** In the steady state `V(out)` swings between 0.041 and 0.959. For $k\ge1$, `.four` reports the amplitudes $2|S_p(k)|$ of the cosine oscillations in [(2.2)](#gl-2-2). At the input these are 0.637, 0, 0.212, 0, 0.127: the even harmonics are missing. At the output the third harmonic is only 15 % of the first instead of 33 %. The phases at the output are larger than at the input by $45^\circ$, $71.6^\circ$ and $78.7^\circ$, because `.four` counts a lag as positive. Halve the output amplitudes and compare with your result from Exercise [3](#aufg-3)(b). The FFT view (right-click in the plot, View, FFT) shows the same lines at the odd multiples of 0.159 Hz.
:::

:::aufgabe Exercise 3 ★★ Power and higher harmonics
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Use [(3.1)](#gl-3-1) to confirm that the harmonics $k=0,\pm1$ of the square wave carry 90.5 % of the power.

</li>

<li>

Compute $|G_p(1)|$, $|G_p(3)|$, $|G_p(5)|$ for the RC output. What fraction of the AC power of the output (without $k=0$) is in the fundamental if you take only $k=\pm1,\pm3,\pm5$ into account?

</li>

<li>

Why does the output already look “more sinusoidal” than the input?

</li>

</ol>

:::loesung
(a) $|S_p(0)|^2+2|S_p(1)|^2=0.25+2/\pi^2=0.25+0.2026=0.4526$, which is 90.5 % of $0.5$.

(b) $|G_p(k)|=|S_p(k)|/\sqrt{1+k^2}$: $|G_p(1)|=0.2251$, $|G_p(3)|=0.0336$, $|G_p(5)|=0.0125$. AC power from these harmonics: $2(0.0507+0.0011+0.0002)=0.1039$. The share of the fundamental is $0.0507/0.0519=97.5\,\%$. At the input, for the same harmonics, it would be only 86.9 %.

(c) $|H(kF)|=1/\sqrt{1+k^2}\approx1/k$: the higher harmonics are attenuated more strongly the higher they are. What remains is mainly the fundamental, and a signal that consists almost entirely of the fundamental is almost a sinusoid.
:::
:::

## Stage 4: From periodic to non-repeating signals

<span class="anker" id="stufe-4"></span>

:::zweck
A single pulse is not periodic. But it can be regarded as a periodic signal with an infinitely long period. In the process, the sum becomes an integral.
:::

**The idea.** Continue a pulse $s(t)$ of duration less than $T$ periodically. The coefficients of the series are then values of a fixed function:

$$S_p(k)=\frac1T\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=F\cdot S(kF),\qquad S(f)=\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t.$$

If you double the period, the line spacing $F$ is halved, and the lines sample the same envelope $S(f)$ twice as densely (Fig. [4](#abb-4)). In the limit $T\to\infty$, the spacing $F$ becomes the differential $\mathrm{d} f$, and the sum $\sum_kS(kF)\mathrm{e}^{\mathrm{j}2\pi kFt}F$ becomes the integral.

:::abbildung et3/k3grenz
A rectangular pulse $\operatorname{rect}(t)$, continued periodically with $T=2$ s and $T=4$ s. The Fourier coefficients multiplied by $T$ lie on the same envelope $S(f)=\operatorname{si}(\pi f)$, with the spacing $1/T$. As $T\to\infty$ they fill the curve without gaps.
:::

:::satz Theorem 4.1 (Fourier transform)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t,\qquad s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f. \tag{4.1}$$

Shorthand: $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ or $S(f)=\mathcal{F}\{s(t)\}$.
:::

⁠**How to read it:** $S(f)$ is a __spectral density__: weight per frequency interval. If $s$ is a voltage in V, $S$ has the unit V/Hz. The inverse transform builds the signal from all oscillations, each with the weight $S(f)\,\mathrm{d} f$. A sufficient condition for existence is $\int|s(t)|\mathrm{d} t<\infty$. The Fourier transform is the Laplace transform on the imaginary axis, $S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$, provided the axis lies in the region of convergence ([Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)).

⁠**Convolution becomes a product.** As in [Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html): $s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$. From $s*\delta=s$ it follows that $S(f)\cdot\mathcal{F}\{\delta\}=S(f)$, so $\delta(t)\;\circ\!\!-\!\!\bullet\;1$: the Dirac impulse contains all frequencies with equal weight.

**Example: the exponential pulse.** The impulse response of the RC circuit, $h(t)=\frac1{RC}\varepsilon(t)\mathrm{e}^{-t/RC}$:

$$H(f)=\frac1{RC}\int_0^\infty\mathrm{e}^{-(1/RC+\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{1+\mathrm{j}2\pi f\,RC}.$$

This is the same frequency response as from AC analysis ([Part 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). So the impulse response contains all the information about the frequency behavior.

:::frage What is the difference between $S_p(k)$ and $S(f)$, apart from the fact that one is discrete?
The unit. $S_p(k)$ is an amplitude (V): the $k$th harmonic really has this strength. $S(f)$ is a density (V/Hz): in a non-repeating signal no single frequency has a finite amplitude; only a frequency band $\Delta f$ carries approximately $S(f)\,\Delta f$. That is why $S_p(k)=F\cdot S(kF)$: each line represents a band of width $F$.
:::

:::aufgabe Exercise 4 ★ The two-sided exponential pulse
<span class="anker" id="aufg-4"></span>

Compute $\mathcal{F}\{\mathrm{e}^{-a|t|}\}$ for $a>0$ by splitting the integral into $t<0$ and $t>0$. Show that the result is real and even, and explain this with the symmetry of the signal.

:::loesung
$$\int_{-\infty}^0\mathrm{e}^{at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t+\int_0^\infty\mathrm{e}^{-at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{1}{a-\mathrm{j}2\pi f}+\frac{1}{a+\mathrm{j}2\pi f}=\frac{2a}{a^2+(2\pi f)^2}.$$

Real and even in $f$. This must be so: the signal is real and even, so its odd part is zero, and hence so is $\operatorname{Im} S$ (Stage [5](#stufe-5)).
:::
:::

## Stage 5: Symmetries in the signal and in the spectrum

<span class="anker" id="stufe-5"></span>

:::zweck
Whether a signal is real, even or odd can be seen immediately from its spectrum. This stage derives the rules.
:::

**Even and odd parts.** A complex function is called __even__ if $x(t)=x^*(-t)$, and __odd__ if $x(t)=-x^*(-t)$. (For real functions these are the usual mirror symmetry and point symmetry about the origin.) Every signal splits uniquely into the two parts:

<span class="anker" id="gl-5-1"></span>
$$s(t)=s_g(t)+s_u(t),\qquad s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr],\qquad s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]. \tag{5.1}$$

:::satz Theorem 5.1 (Symmetries)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-2"></span>
$$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\},\qquad s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}. \tag{5.2}$$

For **real** signals, $S(-f)=S^*(f)$: the real part and the magnitude $|S|$ are even in $f$, the imaginary part and the phase are odd. A real, even signal has a real, even spectrum. A real, odd signal has a purely imaginary, odd spectrum.
:::

:::herleitung Symmetries
First: $\mathcal{F}\{s^*(-t)\}=\int s^*(-t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$. With $\tau=-t$ this is $\int s^*(\tau)\mathrm{e}^{\mathrm{j}2\pi f\tau}\mathrm{d}\tau=\bigl(\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f\tau}\mathrm{d}\tau\bigr)^*=S^*(f)$. Hence

$$\mathcal{F}\{s_g\}=\tfrac12\bigl[S(f)+S^*(f)\bigr]=\operatorname{Re}\{S(f)\},\qquad\mathcal{F}\{s_u\}=\tfrac12\bigl[S(f)-S^*(f)\bigr]=\mathrm{j}\operatorname{Im}\{S(f)\}.$$

For real $s$, $\mathcal{F}\{s^*(t)\}=\mathcal{F}\{s(t)\}$. In general, $\mathcal{F}\{s^*(t)\}=\int s^*\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\bigl(\int s\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} t\bigr)^*=S^*(-f)$. So $S(f)=S^*(-f)$.
:::

⁠**In short:** For a real signal, the negative half of the spectrum is the conjugate mirror image of the positive half. It contains no new information.

**Example.** The exponential pulse $\varepsilon(t)\mathrm{e}^{-t}$ (real) has the even part $\frac12\mathrm{e}^{-|t|}$ and the odd part $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$. Its spectrum $H(f)=\frac{1}{1+\mathrm{j}2\pi f}$ has the even real part $\frac{1}{1+(2\pi f)^2}$, the transform of $\frac12\mathrm{e}^{-|t|}$, and the odd imaginary part $\frac{-2\pi f}{1+(2\pi f)^2}$ (Fig. [5](#abb-5)).

:::abbildung et3/k3gerade
The exponential pulse ($RC=1$ s), decomposed into an even part (blue) and an odd part (red). Right: the spectrum. The even part yields the real part (even in $f$), the odd part the imaginary part (odd in $f$).
:::

:::aufgabe Exercise 5 ★ Reading off symmetry
<span class="anker" id="aufg-5"></span>

What can be said about the spectrum without calculation? (a) $s(t)=\operatorname{rect}(t)$, (b) $s(t)=\operatorname{sgn}(t)\operatorname{rect}(t/2)$, (c) $s(t)=\mathrm{e}^{\mathrm{j}2\pi t}\operatorname{rect}(t)$, (d) a real signal with $S(1\,\mathrm{Hz})=2-3\mathrm{j}$: what is $S(-1\,\mathrm{Hz})$?

:::loesung
(a) Real and even: spectrum real and even ($\operatorname{si}(\pi f)$). (b) Real and odd: spectrum purely imaginary and odd. (c) Complex, but $x^*(-t)=\mathrm{e}^{-\mathrm{j}2\pi(-t)}\operatorname{rect}(-t)=x(t)$: in the sense of the definition the signal is even, so its spectrum is real. By the modulation rule it is $\operatorname{si}(\pi(f-1))$, real, but not symmetric about $f=0$, because the signal is not real. (d) $S(-1\,\mathrm{Hz})=S^*(1\,\mathrm{Hz})=2+3\mathrm{j}$.
:::
:::

## Stage 6: The rules of calculation (theorems)

<span class="anker" id="stufe-6"></span>

:::zweck
Instead of evaluating every integral anew, you use rules: what happens to the spectrum when the signal is shifted, compressed, differentiated or modulated? Each rule follows from what the operation does to a single oscillation.
:::

:::satz Theorem 6.1 (Theorems of the Fourier transform)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
<span class="anker" id="gl-6-2"></span>
<span class="anker" id="gl-6-3"></span>
<span class="anker" id="gl-6-4"></span>
<span class="anker" id="gl-6-5"></span>
<span class="anker" id="gl-6-6"></span>
<span class="anker" id="gl-6-7"></span>
<span class="anker" id="gl-6-8"></span>
<span class="anker" id="gl-6-9"></span>
<span class="anker" id="gl-6-10"></span>
<span class="anker" id="gl-6-11"></span>
$$\begin{aligned} &\text{Superposition:} && \textstyle\sum_ia_is_i(t)\;\circ\!\!-\!\!\bullet\;\sum_ia_iS_i(f)\\ &\text{Conjugation:} && s^*(t)\;\circ\!\!-\!\!\bullet\;S^*(-f)\\ &\text{Similarity (scaling):} && s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\Bigl(\frac fb\Bigr),\quad b\neq0;\qquad s(-t)\;\circ\!\!-\!\!\bullet\;S(-f)\\ &\text{Shift:} && s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft_0},\qquad\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-\mathrm{j}2\pi ft_0}\\ &\text{Derivative:} && \frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;(\mathrm{j}2\pi f)^nS(f)\\ &\text{Symmetry (duality):} && S(t)\;\circ\!\!-\!\!\bullet\;s(-f)\\ &\text{Modulation:} && \mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f-F)\\ &\text{Frequency-domain derivative:} && -\mathrm{j}2\pi t\,s(t)\;\circ\!\!-\!\!\bullet\;\frac{\mathrm{d}}{\mathrm{d} f}S(f)\\ &\text{Convolution, multiplication:} && s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2,\qquad s_1s_2\;\circ\!\!-\!\!\bullet\;S_1*S_2\\ &\text{Areas:} && \int s(t)\mathrm{d} t=S(0),\qquad\int S(f)\mathrm{d} f=s(0)\\ &\text{Parseval:} && \int|s(t)|^2\mathrm{d} t=\int|S(f)|^2\mathrm{d} f \end{aligned} \tag{6.1|6.2|6.3|6.4|6.5|6.6|6.7|6.8|6.9|6.10|6.11}$$
:::

⁠**How to read the most important ones:**

<ul>

<li>

⁠**Similarity:** A signal compressed in time ($|b|>1$) has a wider spectrum. Short signals need many frequencies. Duration and bandwidth are inversely related.

</li>

<li>

⁠**Shift:** A delay does not change the magnitude, only the phase, and it does so linearly in $f$: every oscillation is shifted by the same time, which at a higher frequency is a larger angle.

</li>

<li>

⁠**Derivative:** $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{j}2\pi f\,\mathrm{e}^{\mathrm{j}2\pi ft}$. Differentiation amplifies high frequencies.

</li>

<li>

⁠**Symmetry:** Forward and inverse transform differ only in the sign of the exponent. Every transform pair therefore yields a second one with the roles swapped.

</li>

<li>

⁠**Modulation:** Multiplication by $\mathrm{e}^{\mathrm{j}2\pi Ft}$ shifts the whole spectrum by $F$. This is how every radio transmitter works.

</li>

<li>

⁠**Multiplication:** The spectrum of the product of two signals is the convolution of the spectra, the counterpart of the convolution theorem.

</li>

<li>

⁠**Parseval:** The energy is the same in both domains. $|S(f)|^2$ is the __energy density__ over frequency.

</li>

</ul>

:::herleitung Similarity, shift, derivative, symmetry, modulation, multiplication, Parseval
⁠**Similarity** ($b>0$, $\tau=bt$): $\int s(bt)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac1b\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi(f/b)\tau}\mathrm{d}\tau=\frac1bS(f/b)$. For $b<0$ the limits are reversed, hence $1/|b|$.

⁠**Shift** ($\tau=t-t_0$): $\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f(\tau+t_0)}\mathrm{d}\tau=\mathrm{e}^{-\mathrm{j}2\pi ft_0}S(f)$. With $s=\delta$, the pair for $\delta(t-t_0)$ follows.

⁠**Derivative:** Differentiate the inverse transform with respect to $t$: $\frac{\mathrm{d}}{\mathrm{d} t}\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f=\int\mathrm{j}2\pi f\,S\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$.

⁠**Symmetry:** In the inverse transform, replace $t$ by $-t$: $s(-t)=\int S(f)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} f$. Now swap the names of the variables $t$ and $f$: $s(-f)=\int S(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, which is the forward transform of $S(t)$.

⁠**Modulation:** $\int\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi(f-F)t}\mathrm{d} t=S(f-F)$. The derivative in the frequency domain follows in the same way by differentiating the forward transform with respect to $f$.

⁠**Multiplication:** Convolution theorem for the signals $s_1(t)$ and $s_2(t)$, that is $s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2$, then apply symmetry to this pair: $S_1(t)S_2(t)\;\circ\!\!-\!\!\bullet\;s_1(-f)*s_2(-f)$. Renaming gives [(6.9)](#gl-6-9).

⁠**Areas:** Set $f=0$ in the forward transform and $t=0$ in the inverse transform.

⁠**Parseval:** $\int|s|^2\mathrm{d} t=\int s\,s^*\mathrm{d} t$ is the product $s(t)s^*(t)$, integrated, so by multiplication, conjugation and the area theorem it equals $\bigl[S(f)*S^*(-f)\bigr]_{f=0}=\int S(\nu)S^*(\nu)\mathrm{d}\nu$.
:::

:::frage Why doesn't a delay change the magnitude of the spectrum?
Because a delay neither attenuates nor amplifies any oscillation; it only shifts each one. Every oscillation is shifted by the same time $t_0$, which at the frequency $f$ is the angle $2\pi ft_0$. That is why the phase is a straight line in $f$ with the slope $-2\pi t_0$. A system with $|H|=1$ and linear phase delays a signal without changing its shape.
:::

:::aufgabe Exercise 6 ★★ Applying the theorems
<span class="anker" id="aufg-6"></span>

Use $\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)$ (Stage [7](#stufe-7)) and the theorems.

<ol class="al">

<li>

Find the spectrum of a rectangular pulse of height 1 from $t=0$ to $t=2$ s. What is its magnitude at $f=0$, and where is the first zero?

</li>

<li>

Find the spectrum of $\cos(2\pi F_0t)\operatorname{rect}(t)$ with $F_0=5$ Hz and sketch it.

</li>

</ol>

:::loesung
(a) The pulse is $\operatorname{rect}\bigl(\frac{t-1}{2}\bigr)$. Similarity ($T=2$) and shift ($t_0=1$ s): $2\operatorname{si}(2\pi f)\,\mathrm{e}^{-\mathrm{j}2\pi f}$. Magnitude at $f=0$: 2 (the area). First zero at $f=0.5$ Hz. The shift changes only the phase.

(b) $\cos(2\pi F_0t)=\frac12\mathrm{e}^{\mathrm{j}2\pi F_0t}+\frac12\mathrm{e}^{-\mathrm{j}2\pi F_0t}$, modulation: $\frac12\operatorname{si}(\pi(f-5))+\frac12\operatorname{si}(\pi(f+5))$. Two si main lobes of height $\frac12$ at $\pm5$ Hz, with the first zeros 1 Hz on either side.
:::
:::

:::aufgabe Exercise 7 ★★ Symmetry as a tool
<span class="anker" id="aufg-7"></span>

From Exercise [4](#aufg-4) you know that $\mathrm{e}^{-|t|}\;\circ\!\!-\!\!\bullet\;\frac{2}{1+(2\pi f)^2}$. Use this to find the spectrum of $\frac{1}{1+t^2}$ without an integral.

:::loesung
Apply symmetry to the pair: $\frac{2}{1+(2\pi t)^2}\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-|f|}$. Now stretch the time axis. With $x(t)=\frac{2}{1+(2\pi t)^2}$, $x\bigl(\frac{t}{2\pi}\bigr)=\frac{2}{1+t^2}$, so by the similarity theorem with $b=\frac1{2\pi}$ it is $\circ\!\!-\!\!\bullet\;2\pi\,\mathrm{e}^{-2\pi|f|}$. Halving gives

$$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi|f|}.$$

Check with the area theorem: $\int\frac{\mathrm{d} t}{1+t^2}=\pi=S(0)$.
:::
:::

## Stage 7: Rectangle, si function and triangle

<span class="anker" id="stufe-7"></span>

:::zweck
Three transform pairs come up all the time. With the theorems, they follow from a single calculation.
:::

**Rectangle.** With $\operatorname{si}(x)=\sin(x)/x$:

$$\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{\mathrm{e}^{-\mathrm{j}\pi f}-\mathrm{e}^{\mathrm{j}\pi f}}{-\mathrm{j}2\pi f}=\frac{\sin(\pi f)}{\pi f}=\operatorname{si}(\pi f).$$

:::satz Theorem 7.1 (Rectangle, si and triangle)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \operatorname{rect}\Bigl(\frac tT\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf),\\ \operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf),\\ \Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)&\;\circ\!\!-\!\!\bullet\;\operatorname{si}^2(\pi f),\\ \operatorname{si}(\pi t)*\operatorname{si}(\pi t)&=\operatorname{si}(\pi t). \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**How to read it:** A rectangle of duration $T$ has a spectrum of height $T$ (its area) with zeros at all non-zero multiples of $1/T$. Twice as long means half as wide in the spectrum (Fig. [6](#abb-6)). [(7.2)](#gl-7-2) follows from symmetry, [(7.3)](#gl-7-3) from the convolution theorem, and [(7.4)](#gl-7-4) holds because $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$ in the frequency domain: an ideal low-pass filter does not change a signal that is already limited to its band.

:::abbildung et3/k3rectsi
$\operatorname{rect}(t/T)$ and its spectrum $|T|\operatorname{si}(\pi Tf)$ for $T=1$ s and $T=2$ s. Double the duration: double the height ($=$ area), half the width, first zero at $1/T$.
:::

:::ltspice Spectrum of a rectangular pulse
⁠**Draw:** just one `voltage` source with `PULSE(0 1 0 1u 1u {T0} 16)`: a rectangle of duration $T_0$, repeated every 16 s.

⁠**Directives:** `.param T0=1`, `.step param T0 list 1 2`, `.tran 0 16 0 1m`, `.options plotwinsize=0`, `.four 0.0625 40 V(in)`.

⁠**What you see:** The repetition every 16 s turns the spectrum into lines spaced $1/16$ Hz apart (Stage [4](#stufe-4)). `.four` reports their amplitudes $\frac{2}{16}\,|T_0\operatorname{si}(\pi T_0f)|$, i.e. samples of the si envelope. For $T_0=1$ s the lines at 1 Hz and 2 Hz are zero, for $T_0=2$ s already those at 0.5 Hz, 1 Hz, 1.5 Hz and 2 Hz. The DC component doubles from 0.0625 to 0.125. So double the duration means half the width and double the height, as in Fig. [6](#abb-6). In the FFT view you see the envelope and its zeros directly.
:::

:::aufgabe Exercise 8 ★ Areas and energy of the si function
<span class="anker" id="aufg-8"></span>

Compute $\int_{-\infty}^\infty\operatorname{si}(\pi t)\mathrm{d} t$ and $\int_{-\infty}^\infty\operatorname{si}^2(\pi t)\mathrm{d} t$ without integration. Use the area theorem and Parseval.

:::loesung
Area theorem: $\int\operatorname{si}(\pi t)\mathrm{d} t=\mathcal{F}\{\operatorname{si}(\pi t)\}(0)=\operatorname{rect}(0)=1$. Parseval: $\int\operatorname{si}^2(\pi t)\mathrm{d} t=\int\operatorname{rect}^2(f)\mathrm{d} f=1$.
:::
:::

:::aufgabe Exercise 9 ★★ Triangle and repeated convolution
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Find the spectrum of $\Lambda(t/2)$ (triangle with half-width 2 s). Where are the zeros?

</li>

<li>

What is the spectrum of $\operatorname{rect}*\operatorname{rect}*\operatorname{rect}$? Why do the side lobes decay faster the more often you convolve?

</li>

</ol>

:::loesung
(a) $\Lambda(t)\circ\!\!-\!\!\bullet\operatorname{si}^2(\pi f)$ and similarity with $T=2$: $\Lambda(t/2)\circ\!\!-\!\!\bullet\,2\operatorname{si}^2(2\pi f)$. Zeros at $f=k/2$, $k\neq0$.

(b) $\operatorname{si}^3(\pi f)$. Each further convolution multiplies the spectrum by $\operatorname{si}(\pi f)$, which decays like $1/(\pi f)$ in the side lobes. For the $M$-fold convolution, the side lobes decay like $1/f^M$. In the time domain: the rectangle jumps (decay $1/f$), the triangle has kinks ($1/f^2$), the threefold convolution has a continuous derivative ($1/f^3$). The smoother a signal, the faster its spectrum decays.
:::
:::

## Stage 8: Singular signals and line spectra

<span class="anker" id="stufe-8"></span>

:::zweck
Constants, oscillations, the step and periodic signals are not absolutely integrable. With Dirac impulses in the spectrum they can still be transformed. In this way the Fourier series and the Fourier integral become one.
:::

:::satz Theorem 8.1 (Singular pairs)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
<span class="anker" id="gl-8-5"></span>
<span class="anker" id="gl-8-6"></span>
<span class="anker" id="gl-8-7"></span>
$$\begin{aligned} \delta(t)&\;\circ\!\!-\!\!\bullet\;1, & c&\;\circ\!\!-\!\!\bullet\;c\,\delta(f),\\ \mathrm{e}^{\mathrm{j}2\pi Ft}&\;\circ\!\!-\!\!\bullet\;\delta(f-F), & \cos(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)+\tfrac12\delta(f-F),\\ & & \sin(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F),\\ \textstyle\sum_kS_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}&\;\circ\!\!-\!\!\bullet\;\textstyle\sum_kS_p(k)\,\delta(f-kF),\\ \textstyle\sum_n\delta(t-nT)&\;\circ\!\!-\!\!\bullet\;\frac{1}{|T|}\textstyle\sum_k\delta\Bigl(f-\frac kT\Bigr),\\ \varepsilon(t)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}, & \operatorname{sgn}(t)&\;\circ\!\!-\!\!\bullet\;\frac{1}{\mathrm{j}\pi f},\\ \int_{-\infty}^ts(\tau)\mathrm{d}\tau&\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{\mathrm{j}2\pi f}+\tfrac12S(0)\,\delta(f). \end{aligned} \tag{8.1|8.2|8.3|8.4|8.5|8.6|8.7}$$
:::

⁠**How to read it:**

<ul>

<li>

A constant is an oscillation of frequency 0; its spectrum is a single line at $f=0$. An oscillation $\mathrm{e}^{\mathrm{j}2\pi Ft}$ is a line at $F$. A real cosine has two lines of half weight at $\pm F$.

</li>

<li>

A periodic signal has a __line spectrum__: Dirac impulses at the harmonics, with the Fourier coefficients as weights. So the Fourier series is a special case of the Fourier integral.

</li>

<li>

The __Dirac comb__ (impulses spaced $T$ apart) again has a Dirac comb as its spectrum, with the spacing $1/T$ and the weight $1/|T|$ (Fig. [7](#abb-7)). This pair becomes crucial for sampling ([Part 4](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)).

</li>

<li>

The step has a DC component $\frac12$ (line $\frac12\delta(f)$) and an AC component $\frac12\operatorname{sgn}(t)$, whose spectrum decays like $1/f$.

</li>

</ul>

:::herleitung Singular pairs
⁠**Constant, oscillation:** Apply symmetry to $\delta(t)\circ\!\!-\!\!\bullet\,1$: $1\circ\!\!-\!\!\bullet\,\delta(-f)=\delta(f)$. Modulation shifts the line: $\mathrm{e}^{\mathrm{j}2\pi Ft}\cdot1\circ\!\!-\!\!\bullet\,\delta(f-F)$. Cosine and sine follow with Euler's formulas.

⁠**Line spectrum:** superposition over all harmonics.

⁠**Dirac comb:** It is periodic with $T$. Its Fourier coefficients are $S_p(k)=\frac1T\int_{-T/2}^{T/2}\delta(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac1T$ for all $k$. With the line spectrum, [(8.5)](#gl-8-5) follows.

⁠**Signum:** $\operatorname{sgn}(t)$ is the limiting case of $\operatorname{sgn}(t)\mathrm{e}^{-a|t|}$ as $a\to0$:

$$\int_0^\infty\mathrm{e}^{-(a+\mathrm{j}2\pi f)t}\mathrm{d} t-\int_{-\infty}^0\mathrm{e}^{(a-\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{a+\mathrm{j}2\pi f}-\frac{1}{a-\mathrm{j}2\pi f}=\frac{-\mathrm{j}4\pi f}{a^2+(2\pi f)^2}\;\xrightarrow{a\to0}\;\frac{1}{\mathrm{j}\pi f}.$$

⁠**Step:** $\varepsilon(t)=\frac12+\frac12\operatorname{sgn}(t)$, so $\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$.

⁠**Integration:** $\int_{-\infty}^ts\,\mathrm{d}\tau=s*\varepsilon$, convolution theorem and sifting property $S(f)\delta(f)=S(0)\delta(f)$.
:::

:::abbildung et3/k3kamm
Dirac comb with $T=0.5$ s and its spectrum: again a comb, with the spacing $1/T=2$ Hz and the weight $1/T=2$. The denser the impulses in time, the farther apart the lines.
:::

:::frage But $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$ implies $\mathrm{j}2\pi f\,S(f)=1$, so $S(f)=\frac{1}{\mathrm{j}2\pi f}$. Where does the $\frac12\delta(f)$ come from?
The equation $\mathrm{j}2\pi f\,S(f)=1$ determines $S$ only for $f\neq0$. At $f=0$ the left-hand side is $0\cdot S(0)$, and a term $c\,\delta(f)$ drops out because $f\delta(f)=0$. This is the counterpart of the fact that differentiation “forgets” a constant: $\varepsilon(t)$ and $\varepsilon(t)+b$ have the same derivative. Which constant is correct is decided by the even part: $\varepsilon$ has the mean value $\frac12$, so $c=\frac12$.
:::

**Example: the switched-on cosine.** $\varepsilon(t)\cos(2\pi Ft)$. Multiplication becomes convolution, and convolution with a Dirac impulse shifts:

$$\Bigl[\tfrac12\delta(f)+\tfrac{1}{\mathrm{j}2\pi f}\Bigr]*\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr] =\tfrac14\bigl[\delta(f+F)+\delta(f-F)\bigr]-\frac{\mathrm{j}}{4\pi}\Bigl[\frac{1}{f+F}+\frac{1}{f-F}\Bigr].$$

Besides the halved lines at $\pm F$, a broad spectrum arises: the switch-on process itself contains frequencies near $\pm F$.

:::aufgabe Exercise 10 ★ Line spectra
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Give the spectrum of $s(t)=3+2\cos(2\pi\cdot50\,\mathrm{Hz}\cdot t)$ and sketch it.

</li>

<li>

Give the spectrum of the square wave of the reference model for $|f|\le0.5$ Hz.

</li>

</ol>

:::loesung
(a) $3\,\delta(f)+\delta(f-50\,\mathrm{Hz})+\delta(f+50\,\mathrm{Hz})$: one line of weight 3 at zero, two of weight 1 at $\pm50$ Hz.

(b) $F=0.159$ Hz. Up to 0.5 Hz lie $k=0,\pm1,\pm2,\pm3$, but $k=\pm2$ is missing:

$$0.5\,\delta(f)+0.318\bigl[\delta(f-0.159)+\delta(f+0.159)\bigr]-0.106\bigl[\delta(f-0.477)+\delta(f+0.477)\bigr].$$
:::
:::

:::aufgabe Exercise 11 ★★ Signum and integration
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Use [(5.2)](#gl-5-2) to check that the spectrum of $\operatorname{sgn}(t)$ must be purely imaginary and odd.

</li>

<li>

Use [(8.7)](#gl-8-7) to compute the spectrum of $\int_{-\infty}^t\operatorname{rect}(\tau)\mathrm{d}\tau$. Which signal is this?

</li>

</ol>

:::loesung
(a) $\frac{1}{\mathrm{j}\pi f}=-\frac{\mathrm{j}}{\pi f}$: purely imaginary, and $-\frac{\mathrm{j}}{\pi(-f)}=+\frac{\mathrm{j}}{\pi f}$, so odd. This fits a real, odd signal.

(b) $\frac{\operatorname{si}(\pi f)}{\mathrm{j}2\pi f}+\frac12\delta(f)$. The signal is the running integral of the rectangle: 0 for $t\le-\frac12$, then a ramp up to 1 at $t=\frac12$, constant 1 after that. The mean value over all time is $\frac12$, hence $\frac12\delta(f)$.
:::
:::

## Stage 9: Hilbert transform and analytic signal

<span class="anker" id="stufe-9"></span>

:::zweck
For a causal signal, the real and imaginary parts of the spectrum are linked: one determines the other. The same calculation yields a signal that contains only positive frequencies.
:::

**Causal signals.** If $s(t)=0$ for $t<0$, then the even and odd parts are equal for $t>0$ ($\frac12s$) and opposite for $t<0$. So $s_u(t)=s_g(t)\operatorname{sgn}(t)$ and $s_g(t)=s_u(t)\operatorname{sgn}(t)$. In the frequency domain, multiplication by $\operatorname{sgn}$ becomes convolution with $\frac{1}{\mathrm{j}\pi f}$:

:::satz Theorem 9.1 (Hilbert relation for causal signals)
<span class="anker" id="satz-9-1"></span>

For a causal signal,

<span class="anker" id="gl-9-1"></span>
$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}. \tag{9.1}$$
:::

⁠**How to read it:** Convolution with $\frac{1}{\pi f}$ is called the __Hilbert transform__. For a causal system it is enough to know the real part of the frequency response; the imaginary part follows from it. Causality is therefore a strong constraint on the spectrum.

**Analytic component.** With the step in the *frequency domain* you cut off the negative frequencies: $S_+(f)=S(f)\,\varepsilon(f)$. Symmetry gives $\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$, so

<span class="anker" id="gl-9-2"></span>
$$s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t),\qquad\hat s(t)=s(t)*\frac{1}{\pi t}\;\circ\!\!-\!\!\bullet\;-\mathrm{j}\operatorname{sgn}(f)\,S(f). \tag{9.2}$$

$s_+$ is called the __analytic component__, $\hat s$ the Hilbert transform of $s$. For real signals, $S_-(f)=S_+^*(-f)$, so $s_-=s_+^*$ and $s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$. The real and imaginary parts of $s_+$ are again Hilbert transforms of each other.

**The Hilbert transformer.** The LTI system with $h(t)=\frac{1}{\pi t}$ has $H(f)=-\mathrm{j}\operatorname{sgn}(f)$: magnitude 1 at all frequencies (an __all-pass__), phase $-90^\circ$ for $f>0$ and $+90^\circ$ for $f<0$. It turns $\cos(2\pi Ft)$ into

$$\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr]\cdot\bigl(-\mathrm{j}\operatorname{sgn}(f)\bigr)=\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)\;\bullet\!\!-\!\!\circ\;\sin(2\pi Ft).$$

⁠**In short:** The Hilbert transformer shifts the phase of every oscillation by $90^\circ$ without changing its amplitude.

:::aufgabe Exercise 12 ★★ Hilbert transformer
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

What does the Hilbert transformer make of $\sin(2\pi Ft)$? What does applying it twice give?

</li>

<li>

Find the analytic component $s_+(t)$ of $\cos(2\pi Ft)$ and check $s=2\operatorname{Re}\{s_+\}$.

</li>

<li>

Why is the Hilbert transformer not causal? Look at $h(t)$.

</li>

</ol>

:::loesung
(a) $\sin(2\pi Ft)\circ\!\!-\!\!\bullet\frac{\mathrm{j}}{2}\delta(f+F)-\frac{\mathrm{j}}{2}\delta(f-F)$. Multiplication by $-\mathrm{j}\operatorname{sgn}(f)$: at $-F$ by $+\mathrm{j}$, at $+F$ by $-\mathrm{j}$. Result: $-\frac12\delta(f+F)-\frac12\delta(f-F)$, that is, $-\cos(2\pi Ft)$. Applied twice: $(-\mathrm{j}\operatorname{sgn}f)^2=-1$, so the signal is inverted.

(b) $S_+(f)=S(f)\varepsilon(f)=\frac12\delta(f-F)$, so $s_+(t)=\frac12\mathrm{e}^{\mathrm{j}2\pi Ft}=\frac12\bigl[\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft)\bigr]$. This agrees with $\frac12(s+\mathrm{j}\hat s)$ with $\hat s=\sin$. $2\operatorname{Re}\{s_+\}=\cos(2\pi Ft)$.

(c) $h(t)=\frac{1}{\pi t}$ is nonzero for $t<0$ as well. So the output at time $t$ depends on future input values. In practice, the Hilbert transformer is approximated with a truncated impulse response, at the cost of a delay.
:::
:::

## Stage 10: Short-time Fourier transform

<span class="anker" id="stufe-10"></span>

:::zweck
The spectrum $S(f)$ describes a signal over all time. Speech or music, however, change their frequencies continually. The short-time Fourier transform (STFT) asks: which frequencies does the signal contain *around the instant $t$*?
:::

**The idea.** Cut out a segment around $t$ and transform only that segment. With a rectangular window of width $T_0$:

$$s_T(\tau,t)=s(\tau)\operatorname{rect}\Bigl(\frac{\tau-t}{T_0}\Bigr)\;\circ\!\!-\!\!\bullet\;S_T(f,t)=S(f)*\bigl[T_0\operatorname{si}(\pi T_0f)\,\mathrm{e}^{-\mathrm{j}2\pi tf}\bigr].$$

The spectrum of the segment is the true spectrum, smeared by the si spectrum of the window. A short window localizes well in time but smears strongly in frequency (similarity theorem). The hard edges of the rectangle also produce slowly decaying side lobes. Smooth windows are therefore better, for example the __Hann window__

<span class="anker" id="gl-10-1"></span>
$$w(\tau)=\tfrac12\Bigl[1+\cos\Bigl(\frac{2\pi\tau}{T_0}\Bigr)\Bigr]\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)=\cos^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr). \tag{10.1}$$

:::satz Theorem 10.1 (Short-time Fourier transform)
<span class="anker" id="satz-10-1"></span>

<span class="anker" id="gl-10-2"></span>
$$S_T(f,t)=\int_{-\infty}^{\infty}s(\tau)\,w(\tau-t)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau. \tag{10.2}$$

If the windows shifted by $T$ add up to a constant, $\sum_nw(\tau-nT)=c$, then

<span class="anker" id="gl-10-3"></span>
$$s(\tau)=\frac1c\sum_ns(\tau)\,w(\tau-nT),\qquad S(f)=\frac1c\sum_nS_T(f,nT). \tag{10.3}$$
:::

⁠**How to read it:** $S_T(f,t)$ is a spectrum that depends on time. Plotting $|S_T|$ over $t$ and $f$ gives a __spectrogram__. For the Hann window with the offset $T=T_0/2$, $c=1$, because $\cos^2x+\sin^2x=1$ (Fig. [8](#abb-8)): the segments fit together seamlessly into the whole signal, and the sum of their spectra is the whole spectrum.

:::abbildung et3/k3hann
Hann windows of width $T_0=2$ s, each offset by $T=1$ s (blue). Their sum is exactly 1 everywhere (red).
:::

:::aufgabe Exercise 13 ★ Hann window
<span class="anker" id="aufg-13"></span>

Show that $\sum_nw(\tau-nT)=1$ for $T=T_0/2$. Hint: at every point exactly two windows overlap. Write the second one using $\cos^2(x-\frac\pi2)$.

:::loesung
For $\tau$ between $nT$ and $(n+1)T$ with $T=T_0/2$, exactly the windows $n$ and $n+1$ are nonzero. With $x=\pi(\tau-nT)/T_0$:

$$w(\tau-nT)+w(\tau-(n+1)T)=\cos^2x+\cos^2\Bigl(x-\frac\pi2\Bigr)=\cos^2x+\sin^2x=1.$$
:::
:::

## Stage 11: Fourier and Laplace, limits of existence

<span class="anker" id="stufe-11"></span>

:::zweck
When does the Fourier integral exist, and how is it related to the Laplace transform?
:::

A sufficient condition for existence is absolute integrability, $\int|s(t)|\mathrm{d} t<\infty$. The Laplace transform extends the class by weighting with $\mathrm{e}^{-\sigma t}$ first ([Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)):

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f).$$

So it examines a signal for two things: for frequency components, like the Fourier transform, and for exponential growth or decay. If $\sigma=0$ lies in the region of convergence, the Fourier transform is the Laplace transform on the imaginary axis. With Dirac impulses (Stage [8](#stufe-8)), however, the Fourier transform also covers signals that the Laplace transform does not cover: constants and oscillations over all time. In general it is sufficient that $\int|s(t)|\mathrm{e}^{-c|t|}\mathrm{d} t<\infty$ holds for every $c>0$. The signal may then grow like a power $t^n$, but not exponentially.

:::zusatz Why repeated convolutions become Gaussian
If you form the $M$-fold convolution of $\operatorname{rect}(t)$ with itself, the spectrum is $\operatorname{si}^M(\pi f)$. For small $f$, $\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$ and $\ln(1+w)\approx w$, so

$$\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}.$$

For large $M$ only the region of small $f$ contributes, and the approximation becomes better and better. For $M=4$ the exact value at $t=0$ is $0.667$, and the Gaussian curve gives $0.691$. This is an instance of the __central limit theorem__ (the part on statistics): the convolution of many positive pulses of finite area approaches a Gaussian curve. One example is the impulse response of a cascade of many short integrators.
:::

:::aufgabe Exercise 14 ★★★ (Going further) Checking the Gaussian approximation
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

For $M=2$, compare the exact value $\Lambda(0)=1$ with the Gaussian approximation.

</li>

<li>

Show that the Gaussian curve $\sqrt{6/(\pi M)}\,\mathrm{e}^{-6t^2/M}$ has the area 1. Why must this be so?

</li>

</ol>

:::loesung
(a) $M=2$: $\sqrt{6/(2\pi)}=0.977$ instead of $\Lambda(0)=1$, that is, 2.3 % too low. For $M=4$: 0.691 instead of 0.667, that is, 3.6 % too high. So even after only a few convolutions the Gaussian curve is close to the exact result. The approximation becomes arbitrarily good only for large $M$, because only then do just the small $f$ contribute to the spectrum.

(b) $\int\mathrm{e}^{-6t^2/M}\mathrm{d} t=\sqrt{\pi M/6}$; multiplied by $\sqrt{6/(\pi M)}$, this gives 1. This must be so: the area of a convolution is the product of the areas, here $1^M=1$. In the spectrum this is the value at $f=0$, $\operatorname{si}^M(0)=1$, and the approximation $\mathrm{e}^{-M(\pi f)^2/6}$ also has the value 1 there.
:::
:::

:::kern Key points
<ul>

<li>

$\mathrm{e}^{\mathrm{j}2\pi ft}*h=H(f)\mathrm{e}^{\mathrm{j}2\pi ft}$; $H(f)=\int h\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$.

</li>

<li>

Series: $s_p=\sum S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$, $S_p(k)=\frac1T\int_Ts_p\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t$; real: $S_p(-k)=S_p^*(k)$.

</li>

<li>

Parseval: $\frac1T\int_T|s_p|^2=\sum|S_p(k)|^2$; Gibbs: about 9 % overshoot at jumps; LTI: $G_p(k)=S_p(k)H(kF)$.

</li>

<li>

$S(f)=\int s\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, $s=\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$; $s*h\leftrightarrow SH$, $s_1s_2\leftrightarrow S_1*S_2$.

</li>

<li>

Real: $S(-f)=S^*(f)$; even $\leftrightarrow\operatorname{Re} S$, odd $\leftrightarrow\mathrm{j}\operatorname{Im} S$.

</li>

<li>

$s(bt)\leftrightarrow\frac1{|b|}S(f/b)$; $s(t-t_0)\leftrightarrow S\mathrm{e}^{-\mathrm{j}2\pi ft_0}$; $\frac{\mathrm{d}}{\mathrm{d} t}\leftrightarrow\mathrm{j}2\pi f$; $\mathrm{e}^{\mathrm{j}2\pi Ft}s\leftrightarrow S(f-F)$; $S(t)\leftrightarrow s(-f)$.

</li>

<li>

$\operatorname{rect}(t/T)\leftrightarrow|T|\operatorname{si}(\pi Tf)$; $\Lambda\leftrightarrow\operatorname{si}^2$; $\delta\leftrightarrow1$; $1\leftrightarrow\delta(f)$; $\cos\leftrightarrow\frac12[\delta(f+F)+\delta(f-F)]$.

</li>

<li>

Comb $\leftrightarrow$ comb: $\sum\delta(t-nT)\leftrightarrow\frac1{|T|}\sum\delta(f-k/T)$; $\varepsilon\leftrightarrow\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$.

</li>

<li>

Hilbert: $h=\frac{1}{\pi t}$, $H=-\mathrm{j}\operatorname{sgn}(f)$; $s_+=\frac12(s+\mathrm{j}\hat s)$, $s=2\operatorname{Re} s_+$.

</li>

</ul>
:::
