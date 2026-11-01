---
title: Sampling and Discrete-Time Systems
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Sampling and Discrete-Time Systems
order: 3240100
summary: From the continuous signal to a sequence of numbers: sampling theorem, discrete convolution, DFT, FFT and z-transform
tags: samples, analog, discrete-time, digital, ideal sampler, spectral images, low-pass (band-limited) signal, Nyquist rate
lang: en
---

## What this is about

A computer cannot store a function $s(t)$, only a sequence of numbers. The signal is therefore measured at fixed intervals $T$, and one works with the __samples__ $s(nT)$. Two questions shape this article: *Is information lost in the process?* And: *How do you calculate with sequences of numbers the way Parts 1 to 3 calculated with functions?*

:::merke The answer in three sentences (by the end of the article they should feel obvious)
<ol>

<li>

Sampling is multiplication by a Dirac comb. In the spectrum this becomes a convolution with a comb: the spectrum repeats periodically with the sampling rate.

</li>

<li>

If the repetitions do not lie on top of each other (sampling rate above twice the highest frequency), the signal can be recovered exactly with an ideal low-pass filter. Otherwise aliasing occurs.

</li>

<li>

The same tools apply to sequences of numbers as to functions: convolution as a sum, a Fourier transform with a periodic spectrum, the DFT as its samples, the z-transform as the counterpart of the Laplace transform.

</li>

</ol>
:::

**One principle behind all the results: discrete in one domain means periodic in the other.**

| Result | Where it comes from |
|---|---|
| Periodic spectrum after sampling | time discrete $\Rightarrow$ spectrum periodic (Stage [2](#stufe-2)) |
| Sampling theorem, aliasing | whether the periodic copies overlap (Stage [3](#stufe-3)) |
| si interpolation | an ideal low-pass filter cuts out one copy (Stage [3](#stufe-3)) |
| Fourier series | spectrum discrete $\Rightarrow$ time periodic (Stage [4](#stufe-4)) |
| Discrete convolution | convolution integral over Dirac-weighted samples (Stage [5](#stufe-5)) |
| Discrete-time Fourier transform | spectrum of the samples, periodic with period 1 (Stage [7](#stufe-7)) |
| DFT | both discrete $\Rightarrow$ both periodic (Stage [8](#stufe-8)) |
| Decimation, interpolation | sampling an already sampled sequence (Stage [10](#stufe-10)) |
| z-transform | the Laplace idea for sequences: first weight, then transform (Stage [11](#stufe-11)) |

**How to work with this article.** Each stage has the idea, typical questions with answers you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise.

:::merke The reference model for this article
<ul>

<li>

⁠**Sampling rate** $f_\mathrm A=1/T=1$ kHz ($T=1$ ms). Test signals: cosine oscillations at 300 Hz and 700 Hz.

</li>

<li>

For sequences, the frequency is normalized to the sampling rate: $f=1$ corresponds to $f_\mathrm A$. With $f_\mathrm A=1$ kHz, $f=0.3$ therefore means 300 Hz.

</li>

<li>

⁠**Recursive system** $g(n)=s(n)+0.6\,g(n-1)$.

</li>

<li>

⁠**DFT example** $s_d=(1,\,2,\,0,\,-1)$.

</li>

</ul>

The script `rechnung_kap4.py` recomputes the numbers and curves.
:::

## Stage 1: Signal classes and ideal sampling

<span class="anker" id="stufe-1"></span>

:::zweck
What kinds of signals are there, and how is sampling described mathematically?
:::

**Four classes.** Time and amplitude can each be continuous or discrete. An __analog__ signal is continuous in both. A __discrete-time__ signal has values only at the times $nT$, but these with arbitrary precision. A __digital__ signal is in addition stepped in amplitude (quantized), because a computer can represent only finitely many numbers. This article deals with the discretization of time. The quantization of the amplitude is a separate topic.

**From the real to the ideal sampler.** In every clock cycle, a real sampler closes a switch for the short time $T_0$:

<span class="anker" id="gl-1-1"></span>
$$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)=s(t)\Bigl[\operatorname{rect}\Bigl(\frac{t}{T_0}\Bigr)*\sum_n\delta(t-nT)\Bigr]. \tag{1.1}$$

If $T_0$ is made shorter and shorter, only the values $s(nT)$ remain. Mathematically, the rectangle is replaced by a Dirac impulse. This is the __ideal sampler__:

<span class="anker" id="gl-1-2"></span>
$$s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT). \tag{1.2}$$

The sampled signal is a train of Dirac impulses, each with a sample as its weight. The second step is the sifting property $s(t)\delta(t-nT)=s(nT)\delta(t-nT)$. In this form, sampled signals can be treated with all the tools for continuous signals.

## Stage 2: The spectrum of the sampled signal

<span class="anker" id="stufe-2"></span>

:::zweck
What does sampling do to the spectrum? This stage shows that it repeats periodically.
:::

**The idea.** Two oscillations whose frequencies differ by a multiple of the sampling rate $1/T$ have the same samples:

$$\mathrm{e}^{\mathrm{j}2\pi(f_0+k/T)nT}=\mathrm{e}^{\mathrm{j}2\pi f_0nT}\cdot\underbrace{\mathrm{e}^{\mathrm{j}2\pi kn}}_{=1}.$$

The samples cannot tell them apart. Therefore the spectrum of the samples must look the same at $f_0$ and at $f_0+k/T$. It is periodic.

:::satz Theorem 2.1 (Spectrum of the ideally sampled signal)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$S_\mathrm a(f)=\frac1T\sum_{k=-\infty}^{\infty}S\Bigl(f-\frac kT\Bigr)\qquad(T>0). \tag{2.1}$$
:::

⁠**How to read it:** the spectrum of the original appears with its shape unchanged, but with the factor $1/T$ and repeated at every multiple of the sampling rate. The copies are called __spectral images__.

:::herleitung Spectrum of the sampled signal
Multiplication becomes convolution ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), and the spectrum of the Dirac comb is again a comb:

$$s(t)\cdot\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;S(f)*\frac1T\sum_k\delta\Bigl(f-\frac kT\Bigr)=\frac1T\sum_kS\Bigl(f-\frac kT\Bigr).$$

Convolution with a shifted Dirac impulse shifts the spectrum.
:::

:::abbildung et3/k4spektrum
A spectrum up to $f_\mathrm g=300$ Hz (blue, triangular for clarity), sampled. Top, at 1 kHz: the copies at multiples of 1 kHz lie apart. Bottom, at 500 Hz: copies spaced 500 Hz apart overlap, and the sum (red) is no longer the original. The factor $1/T$ is omitted.
:::

:::frage How does the spectrum “know” that the signal was sampled? The signal between the sampling points is simply gone, after all.
That is exactly why. Between the sampling points the sampled signal is zero, except at the impulses. Every oscillation that has the same values at all points $nT$ describes this signal equally well. The spectrum cannot decide between them and contains all of them: the original and its copies at every multiple of $1/T$.
:::

## Stage 3: The sampling theorem and reconstruction

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

⁠**How to read it:** for $f_\mathrm A\ge2f_\mathrm g$ the copies in Fig. [1](#abb-1) lie apart. A low-pass filter cuts out the copy at $f=0$, and it has exactly the shape of the original. In the time domain this means: each sample is replaced by an si function that is 1 at its own sampling point and zero at all the others (Fig. [2](#abb-2)). Their sum hits all the samples and fills the gaps in such a way that no frequency above $f_\mathrm g$ arises. The minimum rate $2f_\mathrm g$ is called the __Nyquist rate__.

:::herleitung Reconstruction
For $|f|\le f_\mathrm g$ only the copy $k=0$ is present, so $S_\mathrm a(f)=\frac1TS(f)$. With $H_\mathrm{TP}=T\operatorname{rect}(f/2f_\mathrm g)$, $S_\mathrm a\cdot H_\mathrm{TP}=S$. In the time domain: $T\operatorname{rect}(f/2f_\mathrm g)\;\bullet\!\!-\!\!\circ\;2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)$ ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), rectangle and si). With [(1.2)](#gl-1-2) and $2f_\mathrm g=1/T$ this gives $s_\mathrm a*\operatorname{si}(\pi t/T)=\sum_ns(nT)\operatorname{si}(\pi(t-nT)/T)$.
:::

:::abbildung et3/k4siinterp
si interpolation: samples $0,\ 1,\ 0.6,\ -0.4,\ 0.8,\ 0$ (red), the weighted si functions (gray) and their sum (blue). Each si function is zero at the other sampling points, so the sum hits all values exactly.
:::

**Aliasing.** If the sampling is too slow, the copies overlap. A frequency above $f_\mathrm A/2$ appears after reconstruction as a false, lower frequency, its __alias__. In the reference model, a cosine at 700 Hz and one at 300 Hz have exactly the same samples at $f_\mathrm A=1$ kHz, because $\cos(2\pi\cdot0.7n)=\cos(2\pi n-2\pi\cdot0.3n)=\cos(2\pi\cdot0.3n)$ (Fig. [3](#abb-3)). Afterwards the two can no longer be separated. This is why the signal is filtered with a low-pass filter before every sampler (__anti-aliasing filter__).

:::abbildung et3/k4alias
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

## Stage 4: Sampling in the frequency domain

<span class="anker" id="stufe-4"></span>

:::zweck
The same principle holds with the roles swapped: if you sample the spectrum, the signal becomes periodic.
:::

A spectrum that is known only at the frequencies $kF$ is a comb of weighted Dirac impulses. With the factor $F$, the weights are exactly the Fourier coefficients from [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html):

<span class="anker" id="gl-4-1"></span>
$$S_p(f)=F\sum_kS(kF)\,\delta(f-kF)=F\,S(f)\cdot\sum_k\delta(f-kF)\;\bullet\!\!-\!\!\circ\;s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr). \tag{4.1}$$

The corresponding signal is the original, repeated periodically with period $1/F$. If the signal is shorter than $1/F$, the repetitions do not overlap. Then it can be recovered with a time window, and the spectrum with si functions:

<span class="anker" id="gl-4-2"></span>
$$s(t)=s_p(t)\cdot\operatorname{rect}(Ft)\qquad\Longrightarrow\qquad S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr). \tag{4.2}$$

⁠**In short:** discrete in time means periodic in the spectrum, and discrete in the spectrum means periodic in time. The second is the Fourier series from [Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): its coefficients are samples of the spectrum of a single pulse, $S_p(k)=F\cdot S(kF)$.

## Stage 5: Discrete-time signals and discrete convolution

<span class="anker" id="stufe-5"></span>

:::zweck
From now on, all calculations use only the sequences of numbers $s(n)$. This stage carries convolution, elementary signals and LTI systems over to sequences.
:::

**Convolution of the samples.** If the input $s$ and the impulse response $h$ of a system are low-pass signals and sampling is at the Nyquist rate, each can be written as an si series [(3.3)](#gl-3-3). Because $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$ ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), the samples of the output follow from the samples alone:

$$g(nT)=T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr).$$

Normalized to $T=1$, this is the __discrete convolution__:

<span class="anker" id="gl-5-1"></span>
$$g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n-m)=s(n)*h(n). \tag{5.1}$$

**Elementary sequences.**

$$\delta(n)=\begin{cases}1&n=0\\0&n\neq0\end{cases},\qquad \varepsilon(n)=\sum_{m=-\infty}^n\delta(m)=\begin{cases}0&n<0\\1&n\ge0\end{cases},\qquad \varepsilon(n)\,a^n,\qquad \mathrm{e}^{\mathrm{j}2\pi Fn}.$$

The __unit impulse__ $\delta(n)$ is an ordinary sequence, not a distribution: it has the value 1 at $n=0$. It is the identity element of discrete convolution, $s(n)*\delta(n)=s(n)$. A rectangle of $2M+1$ ones around $n=0$ is $\varepsilon(n+M)-\varepsilon(n-M-1)$.

**Linear and shift-invariant.** A discrete-time system is called linear if the superposition principle holds, and __shift-invariant__ if $\operatorname{Tr}\{s(n-m)\}=g(n-m)$ for every integer $m$. A system with both properties is called an __LSI system__. With the __impulse response__ $h(n)=\operatorname{Tr}\{\delta(n)\}$ it follows, as in [Part 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), that

$$g(n)=\operatorname{Tr}\Bigl\{\sum_ms(m)\delta(n-m)\Bigr\}=\sum_ms(m)\operatorname{Tr}\{\delta(n-m)\}=\sum_ms(m)\,h(n-m).$$

No limit process is needed here: a sequence already *is* a sum of weighted, shifted unit impulses.

**Difference and sum.** The counterpart of the derivative is the __difference__ $g(n)=s(n)-s(n-1)$, so $h(n)=\delta(n)-\delta(n-1)$. The counterpart of the integral is the __accumulation__ $g(n)=\sum_{m\le n}s(m)=s(n)*\varepsilon(n)$. The two cancel each other: $[\delta(n)-\delta(n-1)]*\varepsilon(n)=\varepsilon(n)-\varepsilon(n-1)=\delta(n)$.

**Difference equations, FIR and IIR.** Instead of differential equations, difference equations describe discrete-time systems:

<span class="anker" id="gl-5-2"></span>
$$g(n)=\underbrace{\sum_{q=0}^{Q}a_q\,s(n-q)}_{\text{FIR part}}+\underbrace{\sum_{p=1}^{P}b_p\,g(n-p)}_{\text{IIR part}}. \tag{5.2}$$

The output is a weighted sum of past input and output values. If it depends only on input values ($b_p=0$), the impulse response ends after $Q+1$ values: an __FIR filter__ (finite impulse response). With feedback ($b_p\neq0$) the impulse response can be infinitely long: an __IIR filter__ (infinite impulse response). Both are built from delay elements (memory for one clock cycle), multipliers and adders (Fig. [4](#abb-4)).

:::abbildung et3/k4block
First-order system $g(n)=a_0s(n)+a_1s(n-1)+b_1g(n-1)$. The box $T$ stores a value for one clock cycle. On the left the nonrecursive part, on the right the feedback of the output.
:::

:::aufgabe Exercise 4 ★ Discrete convolution by hand
<span class="anker" id="aufg-4"></span>

Convolve $s=(1,1,1)$ with $h=(1,2)$, both starting at $n=0$. How long is the result, and why?

:::loesung
$g(0)=1$, $g(1)=1\cdot2+1\cdot1=3$, $g(2)=3$, $g(3)=1\cdot2=2$: $(1,3,3,2)$. Length $3+2-1=4$: the last nonzero value arises when the last value of $h$ meets the last value of $s$.
:::
:::

## Stage 6: A recursive system

<span class="anker" id="stufe-6"></span>

:::zweck
The simplest IIR system shows how feedback produces an infinitely long impulse response and when the system is stable.
:::

The system $g(n)=s(n)+b\,g(n-1)$ adds the last output, weighted by $b$, to the input. For $s=\delta$ and a system at rest before $n=0$:

<span class="anker" id="gl-6-1"></span>
$$h(n)=\delta(n)+b\,h(n-1)\quad\Longrightarrow\quad h(0)=1,\ h(1)=b,\ h(2)=b^2,\dots\quad\Longrightarrow\quad h(n)=\varepsilon(n)\,b^n. \tag{6.1}$$

The impulse circulates in the feedback loop again and again and is multiplied by $b$ each time. The system is __causal__ ($h(n)=0$ for $n<0$). It is __stable__ if $\sum_n|h(n)|<\infty$ (the discrete counterpart of [Part 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)), so here exactly for $|b|<1$, with $\sum_n|b|^n=\frac{1}{1-|b|}$.

**Response to a rectangular sequence.** Input $s(n)=\varepsilon(n)-\varepsilon(n-M)$ ($M$ ones). With the convolution sum and the formula for the geometric sum $\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$:

<span class="anker" id="gl-6-2"></span>
$$g(n)=\begin{cases}0&n<0,\\[2pt]\displaystyle\sum_{m=0}^{n}b^{n-m}=\frac{1-b^{n+1}}{1-b}&0\le n<M,\\[8pt]\displaystyle\sum_{m=0}^{M-1}b^{n-m}=\frac{b^{n-M+1}-b^{n+1}}{1-b}&n\ge M.\end{cases} \tag{6.2}$$

In the reference model ($b=0.6$, $M=4$): $g=1,\ 1.6,\ 1.96,\ 2.176$, then $1.306,\ 0.783,\ 0.470,\dots$, each value 0.6 times the previous one (Fig. [5](#abb-5)). This is the discrete counterpart of the response of the RC circuit to a rectangular pulse in [Part 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html).

:::abbildung et3/k4rek
The recursive system with $b=0.6$. Left: the impulse response. Right: the response to four ones; it rises to 2.176 and then decays by the factor 0.6 per clock cycle.
:::

:::aufgabe Exercise 5 ★★ Investigating the recursive system
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Confirm the first five values of $g(n)$ in the reference model directly with the recursion.

</li>

<li>

What value does the output approach for an infinitely long sequence of ones ($M\to\infty$)? Compare with $\sum_nh(n)$.

</li>

<li>

What does $h(n)$ look like for $b=-0.6$ and for $b=1.1$? Which system is stable?

</li>

</ol>

:::loesung
(a) $g(0)=1$, $g(1)=1+0.6=1.6$, $g(2)=1+0.96=1.96$, $g(3)=1+1.176=2.176$, $g(4)=0+0.6\cdot2.176=1.306$.

(b) $\frac{1}{1-b}=2.5$. This is $\sum_nh(n)=\sum0.6^n=2.5$: for a constant input 1, the convolution sums all values of the impulse response. Also, $H_\mathrm a(0)=2.5$.

(c) $b=-0.6$: $1,\ -0.6,\ 0.36,\ -0.216,\dots$, alternating sign, decaying, stable. $b=1.1$: $1,\ 1.1,\ 1.21,\dots$, growing, unstable.
:::
:::

:::aufgabe Exercise 6 ★★ First-order system
<span class="anker" id="aufg-6"></span>

$g(n)=s(n)+0.5\,s(n-1)+0.6\,g(n-1)$ (Fig. [4](#abb-4) with $a_0=1$, $a_1=0.5$, $b_1=0.6$).

<ol class="al">

<li>

Compute $h(0)$ to $h(3)$ with the recursion.

</li>

<li>

Show that $h(n)=\frac{11}{6}\,0.6^n\varepsilon(n)-\frac56\delta(n)$.

</li>

</ol>

:::loesung
(a) $h(0)=1$, $h(1)=0.5+0.6\cdot1=1.1$, $h(2)=0.6\cdot1.1=0.66$, $h(3)=0.396$.

(b) The formula gives $h(0)=\frac{11}{6}-\frac56=1$ and $h(1)=\frac{11}{6}\cdot0.6=1.1$. From $n=2$ on, the input is zero, the recursion reads $h(n)=0.6\,h(n-1)$, and the formula satisfies it, because $\frac{11}{6}0.6^n=0.6\cdot\frac{11}{6}0.6^{n-1}$. (With the z-transform, the formula follows from the decomposition $H(z)=-\frac56+\frac{11/6}{1-0.6z^{-1}}$.)
:::
:::

## Stage 7: The discrete-time Fourier transform

<span class="anker" id="stufe-7"></span>

:::zweck
What spectrum does a sequence of numbers have? It is the spectrum of the ideally sampled signal, computed directly from the samples.
:::

If you insert $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ into the Fourier integral, the sifting property leaves a sum. Normalized to $T=1$:

:::satz Theorem 7.1 (Discrete-time Fourier transform)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf},\qquad s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f. \tag{7.1}$$
:::

⁠**How to read it:** $S_\mathrm a(f)$ is periodic with period 1, which is the sampling rate. One period, $|f|\le\frac12$, contains everything. This is why the inverse transform integrates only over an interval of length 1. The sum is a Fourier series in $f$, with the samples as coefficients.

**Example.** For $s(n)=\varepsilon(n)\,b^n$ with $|b|<1$ (geometric series):

<span class="anker" id="gl-7-2"></span>
$$S_\mathrm a(f)=\sum_{n=0}^{\infty}\bigl(b\,\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)^n=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}},\qquad|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}. \tag{7.2}$$

This is also the frequency response $H_\mathrm a(f)$ of the recursive system from Stage [6](#stufe-6). For $b=0.6$: $|H_\mathrm a|=2.5$ at $f=0$, $1.60$ at $f=0.1$, $0.86$ at $f=0.25$, $0.625$ at $f=0.5$ (Fig. [6](#abb-6)). The system is a low-pass filter, but with a periodic frequency response: at $f=1$ it amplifies as strongly as at $f=0$ again.

:::abbildung et3/k4dtft
Magnitude of the frequency response of the recursive system with $b=0.6$. It is periodic with the sampling rate. Between the red lines lies the one period that describes everything.
:::

**Convolution and multiplication.** As with functions, $s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$. The product of two sequences gives the __periodic convolution__ of the spectra over one period:

<span class="anker" id="gl-7-3"></span>
$$s(n)\cdot h(n)\;\circ\!\!-\!\!\bullet\;\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu. \tag{7.3}$$

:::aufgabe Exercise 7 ★ Moving average
<span class="anker" id="aufg-7"></span>

$h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$ averages three consecutive values.

<ol class="al">

<li>

Show that $H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

</li>

<li>

At which frequency is $H_\mathrm a=0$? Which oscillation does the filter therefore cancel completely, and why (hint: the sum of three values of an oscillation with period 3)?

</li>

</ol>

:::loesung
(a) $\frac13\bigl(1+\mathrm{e}^{-\mathrm{j}2\pi f}+\mathrm{e}^{-\mathrm{j}4\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl(\mathrm{e}^{\mathrm{j}2\pi f}+1+\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

(b) $\cos(2\pi f)=-\frac12$, so $f=\frac13$ (at $f_\mathrm A=1$ kHz: 333 Hz). An oscillation with three values per period consists of three phasors spaced $120^\circ$ apart. Their sum is zero; in every window the filter sees exactly one whole period.
:::
:::

## Stage 8: The discrete Fourier transform (DFT)

<span class="anker" id="stufe-8"></span>

:::zweck
$S_\mathrm a(f)$ is a continuous function, but a computer needs finitely many numbers. For a sequence of finite length, finitely many samples of the spectrum are enough.
:::

**The idea.** If $s(n)$ is limited to $M$ values, then by Stage [4](#stufe-4) samples of the spectrum spaced $F=1/M$ apart are enough. They correspond to the signal $s_d(n)$, repeated periodically with period $M$. Because the spectrum is also periodic (time discrete), $M$ spectral values suffice. Both sides are now discrete and periodic.

:::satz Theorem 8.1 (Discrete Fourier transform)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
$$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M},\qquad s_d(n)=\frac1M\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M},\qquad k,n=0,\dots,M-1. \tag{8.1}$$
:::

⁠**How to read it:** $S_d(k)$ is the value of the spectrum $S_\mathrm a(f)$ at $f=k/M$. The index $k$ counts oscillations that fit exactly $k$ times into the $M$ values. The inverse transform is a Fourier series with $M$ terms. The theorems hold analogously, for example the shift $s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{-\mathrm{j}2\pi mk/M}$ (circular: what is shifted out at the end comes back in at the start) and Parseval $\sum_n|s_d(n)|^2=\frac1M\sum_k|S_d(k)|^2$.

**Example.** $s_d=(1,\,2,\,0,\,-1)$, $M=4$, $\mathrm{e}^{-\mathrm{j}2\pi/4}=-\mathrm{j}$:

$$S_d(k)=\sum_{n=0}^{3}s_d(n)(-\mathrm{j})^{kn}:\qquad S_d(0)=2,\quad S_d(1)=1-3\mathrm{j},\quad S_d(2)=0,\quad S_d(3)=1+3\mathrm{j}.$$

Check: $S_d(3)=S_d^*(1)$, because the signal is real ($k=3$ corresponds to $k=-1$). Parseval: $1+4+0+1=6=\frac14(4+10+0+10)$.

:::aufgabe Exercise 8 ★★ DFT by hand
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Recompute $S_d(1)$ for $s_d=(1,2,0,-1)$.

</li>

<li>

Use the shift theorem to determine the DFT of the circularly shifted sequence $(-1,1,2,0)$, and check $S_d(1)$ directly.

</li>

</ol>

:::loesung
(a) $S_d(1)=1+2(-\mathrm{j})+0\cdot(-1)+(-1)(-\mathrm{j})^3=1-2\mathrm{j}-\mathrm{j}=1-3\mathrm{j}$, because $(-\mathrm{j})^3=\mathrm{j}$.

(b) Shift by $m=1$: $S_d(k)\,(-\mathrm{j})^k$, so $(2,\;(1-3\mathrm{j})(-\mathrm{j}),\;0,\;(1+3\mathrm{j})\mathrm{j})=(2,\;-3-\mathrm{j},\;0,\;-3+\mathrm{j})$. Directly: $S_d(1)=-1+1\cdot(-\mathrm{j})+2\cdot(-1)+0=-3-\mathrm{j}$.
:::
:::

## Stage 9: FFT and fast convolution

<span class="anker" id="stufe-9"></span>

:::zweck
The DFT needs $M^2$ multiplications. The FFT gets by with roughly $M\,\mathrm{lb}\,M$. This also makes convolution via the frequency domain fast.
:::

**The idea of the FFT.** With $W_M=\mathrm{e}^{-\mathrm{j}2\pi/M}$, $S_d(k)=\sum_ns_d(n)W_M^{kn}$. For even $M$, split into values with even and odd index:

<span class="anker" id="gl-9-1"></span>
$$S_d(k)=\underbrace{\sum_{n=0}^{M/2-1}s_d(2n)\,W_{M/2}^{kn}}_{S_{d,1}(k)}+W_M^k\underbrace{\sum_{n=0}^{M/2-1}s_d(2n+1)\,W_{M/2}^{kn}}_{S_{d,2}(k)}, \tag{9.1}$$

because $W_M^{2kn}=W_{M/2}^{kn}$. Instead of one DFT of length $M$ you need two of length $M/2$ and $M$ multiplications by $W_M^k$, so $2(M/2)^2+M$ instead of $M^2$. Both partial DFTs are periodic with period $M/2$, so they also supply the values for $k\ge M/2$. If $M$ is a power of two, the splitting is repeated $\mathrm{lb}\,M$ times. The effort drops to about $M\,\mathrm{lb}\,M$. For $M=1024$ that is 10,240 instead of 1,048,576 multiplications, roughly a hundred times fewer. This is the __fast Fourier transform__ (FFT).

**Circular convolution.** For periodic sequences with period $M$, the __circular__ (periodic) convolution is

<span class="anker" id="gl-9-2"></span>
$$g_d(n)=\sum_{m=0}^{M-1}s_d(m)\,h_d\bigl((n-m)\bmod M\bigr)\;\circ\!\!-\!\!\bullet\;G_d(k)=S_d(k)\,H_d(k). \tag{9.2}$$

It is the periodically repeated result of ordinary convolution. If $M$ is too small, the repetitions overlap. For $s=(1,1,1)$ and $h=(1,2)$ the ordinary convolution is $(1,3,3,2)$, with four values. With $M=3$ the last value falls onto the first: $(3,3,3)$. With $M=4$ the result is correct: $(1,3,3,2)$. In general $M\ge M_1+M_2-1$ is required ($M_1$, $M_2$: lengths of the two sequences); to achieve this, the sequences are padded with zeros.

**Fast convolution.** Instead of evaluating the convolution sum directly, you transform both sequences with the FFT, multiply and transform back. A signal of arbitrary length is split into blocks; each block is convolved separately, and the results are added. This is allowed because convolution is distributive:

$$s(n)*h(n)=\Bigl[\sum_is_i(n)\Bigr]*h(n)=\sum_i\bigl[s_i(n)*h(n)\bigr].$$

:::aufgabe Exercise 9 ★★ Circular or linear
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Compute the circular convolution of $(1,1,1)$ and $(1,2,0)$ with $M=3$ by hand. Which value of the linear convolution has moved where?

</li>

<li>

A signal with 1000 values is to be convolved via the DFT with a filter of 25 values. What is the minimum length of the DFT?

</li>

</ol>

:::loesung
(a) $g(0)=s_0h_0+s_1h_2+s_2h_1=1+0+2=3$, $g(1)=s_0h_1+s_1h_0+s_2h_2=2+1+0=3$, $g(2)=s_0h_2+s_1h_1+s_2h_0=0+2+1=3$. The fourth value of the linear convolution (2 at $n=3$) has moved circularly to $n=0$: $1+2=3$.

(b) At least $1000+25-1=1024$. Conveniently, this is a power of two.
:::
:::

## Stage 10: Changing the sampling rate, decimation and interpolation

<span class="anker" id="stufe-10"></span>

:::zweck
A sequence can afterwards be represented at a lower or higher rate. The same rules apply to the spectrum as for the original sampling.
:::

**Downsampling by the factor $c$.** Only every $c$th value is kept. Conceptually, first multiply by a comb of unit impulses, then drop the zeros:

$$s_c(n)=s(n)\sum_m\delta(n-mc),\qquad s_u(n)=s(nc).$$

Multiplication by the comb produces $c$ copies of the spectrum spaced $1/c$ apart, and dropping the zeros stretches the frequency axis by $c$:

<span class="anker" id="gl-10-1"></span>
$$S_{c,\mathrm a}(f)=\frac1c\sum_{k=0}^{c-1}S_\mathrm a\Bigl(f-\frac kc\Bigr),\qquad S_{u,\mathrm a}(f)=S_{c,\mathrm a}\Bigl(\frac fc\Bigr). \tag{10.1}$$

If the spectrum extends up to $f_\mathrm g$ (normalized to the old rate), after downsampling it extends up to $cf_\mathrm g$. Aliasing is avoided only if $cf_\mathrm g\le\frac12$. Otherwise a digital low-pass filter must limit the band beforehand.

**Upsampling by the factor $c$.** Insert $c-1$ zeros between every two values: $s_\uparrow(n)=s(n/c)$ for $n$ divisible by $c$, otherwise 0. The spectrum is compressed by $c$, $S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$, and now contains $c-1$ spectral images within the period. A low-pass filter with the cutoff frequency $\frac{1}{2c}$ and the gain $c$ removes them. In doing so it fills the zeros with interpolated values (the si interpolation from Stage [3](#stufe-3) in discrete form), and the original values are preserved. Downsampling and upsampling in succession change the rate by a rational factor $c_1/c_2$.

:::abbildung et3/k4rate
Spectra (frequency normalized to the respective rate) when the sampling rate is changed. Downsampling stretches the band; upsampling compresses it and creates spectral images, which an interpolation filter removes.
:::

:::aufgabe Exercise 10 ★★ Downsampling
<span class="anker" id="aufg-10"></span>

A sequence has a spectrum up to $f_\mathrm g=0.2$.

<ol class="al">

<li>

May it be downsampled by $c=2$ without a prefilter? By $c=3$?

</li>

<li>

What must happen before downsampling by $c=3$, and what is lost in the process?

</li>

</ol>

:::loesung
(a) $c=2$: afterwards the band extends up to $0.4\le0.5$, no aliasing. $c=3$: up to $0.6>0.5$, aliasing.

(b) Limit the band beforehand to $\frac{1}{2c}=\frac16\approx0.167$ with a digital low-pass filter. The components between 0.167 and 0.2 are lost in the process. That is the price of the lower rate.
:::
:::

## Stage 11: The z-transform

<span class="anker" id="stufe-11"></span>

:::zweck
Just as the Laplace transform extends the Fourier transform ([Part 2](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)), the z-transform extends the discrete-time Fourier transform: first weight exponentially, then transform.
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

**Rules of calculation.** Convolution becomes a product: $g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$. A delay by $n_0$ clock cycles becomes multiplication by $z^{-n_0}$. This turns the difference equation [(5.2)](#gl-5-2) into

<span class="anker" id="gl-11-3"></span>
$$H(z)=\frac{G(z)}{S(z)}=\frac{\sum_{q=0}^{Q}a_q\,z^{-q}}{1-\sum_{p=1}^{P}b_p\,z^{-p}}. \tag{11.3}$$

For the system from Exercise [6](#aufg-6), $H(z)=\frac{1+0.5z^{-1}}{1-0.6z^{-1}}$: zero at $z=-0.5$, pole at $z=0.6$.

:::satz Theorem 11.2 (Stability)
<span class="anker" id="satz-11-2"></span>

A causal LSI system is stable if and only if all poles of $H(z)$ lie inside the unit circle.
:::

⁠**Why:** causal means a region of convergence outside the outermost pole. Stable means $\sum|h(n)|<\infty$; then $H(z)$ converges on the unit circle, so the unit circle belongs to the region of convergence. Both together are possible only if the outermost pole lies inside the unit circle. For the recursive system with $H(z)=\frac{1}{1-bz^{-1}}$ this again means $|b|<1$.

**Example.** $s(n)=0.5^n\cos(\pi n/3)\,\varepsilon(n)$. With $\cos=\frac12(\mathrm{e}^{\mathrm{j}\pi n/3}+\mathrm{e}^{-\mathrm{j}\pi n/3})$ and [(11.2)](#gl-11-2) for $b=0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}$:

$$S(z)=\frac12\Bigl[\frac{1}{1-0.5\mathrm{e}^{\mathrm{j}\pi/3}z^{-1}}+\frac{1}{1-0.5\mathrm{e}^{-\mathrm{j}\pi/3}z^{-1}}\Bigr]=\frac{1-0.25z^{-1}}{1-0.5z^{-1}+0.25z^{-2}},\qquad|z|>0.5.$$

Poles at $0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}=0.25\pm0.433\mathrm{j}$, zeros at $z=0$ and $z=0.25$ (Fig. [8](#abb-8)). The magnitude of the poles gives the decay per clock cycle (0.5), their angle gives the oscillation ($\pi/3$ per clock cycle, so six clock cycles per period).

:::abbildung et3/k4zebene
z-plane of the example: poles (crosses) at $0.5\mathrm{e}^{\pm\mathrm{j}\pi/3}$, zeros (circles) at 0 and 0.25. The region of convergence (blue) lies outside the circle through the poles and contains the unit circle. Read as an impulse response, the sequence describes a causal and stable system.
:::

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

:::kern Key points
<ul>

<li>

Ideal sampling: $s_\mathrm a=\sum s(nT)\delta(t-nT)$; spectrum $\frac1T\sum_kS(f-k/T)$, periodic with $1/T$.

</li>

<li>

Sampling theorem: $f_\mathrm A\ge2f_\mathrm g$; reconstruction $s(t)=\sum s(nT)\operatorname{si}(\pi(t-nT)/T)$; otherwise aliasing.

</li>

<li>

Discrete in one domain means periodic in the other.

</li>

<li>

Discrete convolution $g(n)=\sum_ms(m)h(n-m)$; $h(n)=\operatorname{Tr}\{\delta(n)\}$; stable: $\sum|h(n)|<\infty$.

</li>

<li>

Recursive system $g(n)=s(n)+bg(n-1)$: $h(n)=b^n\varepsilon(n)$, $H_\mathrm a=\frac{1}{1-b\mathrm{e}^{-\mathrm{j}2\pi f}}$.

</li>

<li>

$S_\mathrm a(f)=\sum s(n)\mathrm{e}^{-\mathrm{j}2\pi nf}$, period 1; $s(n)=\int_{-1/2}^{1/2}S_\mathrm a\mathrm{e}^{\mathrm{j}2\pi nf}\mathrm{d} f$.

</li>

<li>

DFT: $S_d(k)=\sum_{n=0}^{M-1}s_d(n)\mathrm{e}^{-\mathrm{j}2\pi kn/M}$, $s_d=\frac1M\sum S_d\mathrm{e}^{\mathrm{j}2\pi kn/M}$; FFT $\approx M\,\mathrm{lb}\,M$; circular convolution $\leftrightarrow S_dH_d$.

</li>

<li>

Downsampling stretches the band (aliasing if $cf_\mathrm g>\frac12$), upsampling creates spectral images.

</li>

<li>

$S(z)=\sum s(n)z^{-n}$; $z^{-n_0}$ = delay; $H(z)=\frac{\sum a_qz^{-q}}{1-\sum b_pz^{-p}}$; causal and stable: all poles in $|z|<1$.

</li>

</ul>
:::
