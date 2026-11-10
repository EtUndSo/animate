---
title: Stage 3: Power, convergence and LTI systems
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Fourier Series and Transform
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Chapter 3: Fourier Series and Transform
order: 3230400
summary: How much does each harmonic contribute to the signal, how well does a truncated series approximate the signal, and what does an LTI system do with a periodic input?
tags: power, partial sum, Gibbs phenomenon
lang: en
---

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
$|s_p|^2=s_ps_p^*=\sum_k\sum_lS_p(k)S_p^*(l)\,\mathrm{e}^{\mathrm{j}2\pi(k-l)Ft}$. Averaged over one period, by [(2.4)](periodische-signale-die-fourier-reihe.html#gl-2-4) only $k=l$ remains: $\sum_k|S_p(k)|^2$.
:::

**Truncated series and the Gibbs phenomenon.** If you take only the harmonics up to $|k|\le N$, the __partial sum__ is $s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$. The power of the error $s_p-s_{p,N}$ is the sum of the omitted $|S_p(k)|^2$ and tends to zero as $N\to\infty$ if the signal has finite power. At a jump, however, an overshoot remains (Fig. [2](#abb-2)): it becomes narrower as $N$ grows, but its height tends to about 9 % of the jump height (10.0 % for $N=3$, 9.1 % for $N=9$, 9.0 % for $N=27$, limit 8.95 %). This is the __Gibbs phenomenon__. It does not contradict convergence: the area under the overshoot, and with it the error power, still tends to zero.

:::abbildung et3/k3gibbs 2
Partial sums of the square wave ($T=2\pi$ s) with the harmonics up to $|k|\le N$. At the edges an overshoot of about 9 % of the jump height remains, which only becomes narrower as $N$ grows.
:::

**Periodic input to an LTI system.** Each harmonic is an eigenfunction and is multiplied by $H(kF)$. The output therefore has the same period, and its coefficients are

<span class="anker" id="gl-3-2"></span>
$$G_p(k)=S_p(k)\,H(kF). \tag{3.2}$$

In the reference model, $H(kF)=1/(1+\mathrm{j} k)$. The fundamental is transmitted with $|H|=0.707$ and $-45^\circ$, the third harmonic with $0.316$ and $-71.6^\circ$, the fifth with $0.196$ and $-78.7^\circ$. At the output, the third harmonic is only 15 % as large as the first, instead of 33 % at the input. The RC circuit rounds off the edges (Fig. [3](#abb-3)). The output swings between 0.041 and 0.959.

:::abbildung et3/k3rc 3
Square wave through the RC low-pass filter with $RC=1$ s, computed as a sum of harmonics with $G_p(k)=S_p(k)/(1+\mathrm{j} k)$. The output charges and discharges exponentially between 0.041 and 0.959.
:::

:::frage Isn't a calculation over infinitely many harmonics much more laborious than the differential equation?
For a single square wave through an RC circuit, yes: the charging and discharging curves can be written down directly. In return, the series shows *why* the output looks the way it does. The edges consist of the high harmonics, and it is exactly these that the RC circuit attenuates. Moreover, [(3.2)](#gl-3-2) works for every LTI system, even for those whose differential equation is not known at all, only their measured frequency response.
:::

:::ltspice Square wave through the RC circuit
⁠**Draw:** the RC circuit (`res` with `1Meg`, `cap` with `1u`) with the source `PULSE(0 1 0 1u 1u {pi} {2*pi})`: period $2\pi$ s, duty cycle $\frac12$.

⁠**Directives:** `.tran 0 {20*pi} 0 1m`, `.four {1/(2*pi)} 5 V(in) V(out)` and `.options plotwinsize=0`. The last one switches off data compression; without it `.four` is inaccurate. `.four` decomposes the last period into harmonics and writes the result to the SPICE Error Log.

⁠**What you see:** In the steady state `V(out)` swings between 0.041 and 0.959. For $k\ge1$, `.four` reports the amplitudes $2|S_p(k)|$ of the cosine oscillations in [(2.2)](periodische-signale-die-fourier-reihe.html#gl-2-2). At the input these are 0.637, 0, 0.212, 0, 0.127: the even harmonics are missing. At the output the third harmonic is only 15 % of the first instead of 33 %. The phases at the output are larger than at the input by $45^\circ$, $71.6^\circ$ and $78.7^\circ$, because `.four` counts a lag as positive. Halve the output amplitudes and compare with your result from Exercise [3](#aufg-3)(b). The FFT view (right-click in the plot, View, FFT) shows the same lines at the odd multiples of 0.159 Hz.
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
