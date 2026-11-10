---
title: Stage 3: The sampling theorem and reconstruction
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Sampling and Discrete-Time Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Chapter 4: Sampling and Discrete-Time Systems
order: 3240400
summary: When can the original be recovered exactly from the samples, and how?
tags: low-pass (band-limited) signal, Nyquist rate, alias, anti-aliasing filter
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
When can the original be recovered exactly from the samples, and how?
:::

:::satz Theorem 3.1 (Sampling theorem)
<span class="anker" id="satz-3-1"></span>

A signal whose spectrum vanishes above $f_\mathrm g$ (__low-pass (band-limited) signal__) is uniquely determined by its samples $s(nT)$ if

<span class="anker" id="gl-3-1"></span>
$$T\le\frac{1}{2f_\mathrm g}\qquad\text{that is}\qquad f_\mathrm A=\frac1T\ge2f_\mathrm g. \tag{3.1}$$

With the ideal low-pass filter $H_\mathrm{TP}(f)=T\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$,

<span class="anker" id="gl-3-2"></span>
$$s(t)=s_\mathrm a(t)*\bigl[2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)\bigr], \tag{3.2}$$

and for $T=1/(2f_\mathrm g)$:

<span class="anker" id="gl-3-3"></span>
$$s(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr). \tag{3.3}$$
:::

⁠**How to read it:** for $f_\mathrm A\ge2f_\mathrm g$ the copies in Fig. [1](das-spektrum-des-abgetasteten-signals.html#abb-1) lie apart. A low-pass filter cuts out the copy at $f=0$, and it has exactly the shape of the original. In the time domain this means: each sample is replaced by an si function that is 1 at its own sampling point and zero at all the others (Fig. [2](#abb-2)). Their sum hits all the samples and fills the gaps in such a way that no frequency above $f_\mathrm g$ arises. The minimum rate $2f_\mathrm g$ is called the __Nyquist rate__.

:::herleitung Reconstruction
For $|f|\le f_\mathrm g$ only the copy $k=0$ is present, so $S_\mathrm a(f)=\frac1TS(f)$. With $H_\mathrm{TP}=T\operatorname{rect}(f/2f_\mathrm g)$, $S_\mathrm a\cdot H_\mathrm{TP}=S$. In the time domain: $T\operatorname{rect}(f/2f_\mathrm g)\;\bullet\!\!-\!\!\circ\;2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)$ ([Chapter 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), rectangle and si). With [(1.2)](signalklassen-und-ideale-abtastung.html#gl-1-2) and $2f_\mathrm g=1/T$ this gives $s_\mathrm a*\operatorname{si}(\pi t/T)=\sum_ns(nT)\operatorname{si}(\pi(t-nT)/T)$.
:::

:::abbildung et3/k4siinterp 2
si interpolation: samples $0,\ 1,\ 0.6,\ -0.4,\ 0.8,\ 0$ (red), the weighted si functions (gray) and their sum (blue). Each si function is zero at the other sampling points, so the sum hits all values exactly.
:::

**Aliasing.** If the sampling is too slow, the copies overlap. A frequency above $f_\mathrm A/2$ appears after reconstruction as a false, lower frequency, its __alias__. In the reference model, a cosine at 700 Hz and one at 300 Hz have exactly the same samples at $f_\mathrm A=1$ kHz, because $\cos(2\pi\cdot0.7n)=\cos(2\pi n-2\pi\cdot0.3n)=\cos(2\pi\cdot0.3n)$ (Fig. [3](#abb-3)). Afterwards the two can no longer be separated. This is why the signal is filtered with a low-pass filter before every sampler (__anti-aliasing filter__).

:::abbildung et3/k4alias 3
At $f_\mathrm A=1$ kHz the samples (black) of 700 Hz and 300 Hz coincide. 700 Hz lies above $f_\mathrm A/2=500$ Hz and appears as an alias at 300 Hz.
:::

:::frage Isn't exactly $f_\mathrm A=2f_\mathrm g$ enough? For a sine at exactly $f_\mathrm g$ it goes wrong, though.
Yes, exactly at the limit it goes wrong: with an unfavorable phase, a sine with $f_\mathrm g=f_\mathrm A/2$ can be sampled at a zero crossing every time, and all samples are zero. Strictly speaking, the theorem therefore requires that the spectrum has no line *at* $f_\mathrm g$, or that $f_\mathrm A>2f_\mathrm g$. In practice one samples faster anyway, because real low-pass filters do not drop off vertically and need room for their transition band.
:::

:::ltspice Sample-and-hold: seeing aliasing
⁠**Draw:** a `voltage` source at net `in` with `SINE(0 1 700 0 0 90)`, a cosine at 700 Hz. A switch `sw` (value `SW1`) from `in` to `sh`, and there a `cap` with `100n` to ground. A second source with `PULSE(0 1 0 10n 10n 1u 1m)` drives the control input of the switch: the switch closes every millisecond for 1 µ s ($f_\mathrm A=1$ kHz), and in between the capacitor holds the sample. After `sh` comes an `e` source with output `out` as the reconstruction low-pass. It is a 4th-order Butterworth low-pass (passband as flat as possible) with cut-off frequency 400 Hz and has the value

`Laplace=1/(((s/wg)**2+0.7654*s/wg+1)*((s/wg)**2+1.8478*s/wg+1))`

⁠**Directives:** `.model SW1 SW(Ron=1 Roff=1G Vt=0.5)`, `.param wg=2*pi*400`, `.tran 0 40m 0 1u`, `.options plotwinsize=0`, `.four 100 15 V(sh) V(out)`.

⁠**What you see:** The staircase at `sh` follows a 300-Hz oscillation, and at `out` there is a cosine at 300 Hz instead of 700 Hz. In `.four` the line at 300 Hz is the strongest. With `SINE(0 1 300 0 0 90)` the same staircase appears. Set 1.2 kHz and compare with your result from Exercise [1](#aufg-1)(a).

⁠**Anti-aliasing:** Put a second, identical `e` source in front of the switch. At 700 Hz the 300-Hz line at `out` drops to about one tenth, while a 300-Hz input passes almost unattenuated. So the alias has to be prevented before sampling: afterwards it can no longer be told apart from a genuine 300-Hz signal.
:::

:::aufgabe Exercise 1 ★ Alias frequencies
<span class="anker" id="aufg-1"></span>

$f_\mathrm A=1$ kHz.

<ol class="al">

<li>

At what frequency does a cosine at 1.2 kHz appear after reconstruction?

</li>

<li>

Which frequencies give the same samples as a cosine at 50 Hz?

</li>

</ol>

:::loesung
(a) 1.2 kHz lies above $f_\mathrm A/2$. It has the same samples as $1.2-1=0.2$ kHz and appears as 200 Hz.

(b) All $\pm50\,\mathrm{Hz}+k\cdot1\,\mathrm{kHz}$: 950 Hz, 1050 Hz, 1950 Hz, 2050 Hz and so on. For the cosine, negative and positive frequency count equally, which is why $1000-50$ belongs to them as well.
:::
:::

:::aufgabe Exercise 2 ★★ Sampling rates in practice
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Telephone speech is limited to 3.4 kHz and sampled at 8 kHz. What is the Nyquist rate, and what is the margin for?

</li>

<li>

An audio CD samples at 44.1 kHz. Up to what frequency can it store sounds, and how wide is the transition band for the anti-aliasing filter if the audible band extends to 20 kHz?

</li>

</ol>

:::loesung
(a) Nyquist rate $2\cdot3.4=6.8$ kHz. With 8 kHz, $f_\mathrm A/2$ lies at 4 kHz. Between 3.4 and 4 kHz the anti-aliasing filter has room to make the transition from passband to stopband.

(b) Up to $f_\mathrm A/2=22.05$ kHz. The transition band from 20 to 22.05 kHz is only 2.05 kHz wide. This is why steep filters or oversampling are needed.
:::
:::

:::aufgabe Exercise 3 ★★ si interpolation by hand
<span class="anker" id="aufg-3"></span>

Use [(3.3)](#gl-3-3) to compute the value of the signal from Fig. [2](#abb-2) at $t=2.5T$. Hint: $\operatorname{si}(\pi\cdot0.5)=2/\pi$ and $\operatorname{si}(\pi\cdot1.5)=-2/(3\pi)$. Which samples contribute nothing?

:::loesung
At $t=2.5T$, $\operatorname{si}(\pi(2.5-k))$ equals $\frac2\pi$ for $k\in\{2,3\}$ and $-\frac{2}{3\pi}$ for $k\in\{1,4\}$. The values at $k=0$ and $k=5$ are zero and contribute nothing:

$$s(2.5T)=\frac2\pi\Bigl[-\tfrac13\cdot1+0.6-0.4-\tfrac13\cdot0.8\Bigr]=\frac2\pi\cdot(-0.4)=-0.255.$$
:::
:::
