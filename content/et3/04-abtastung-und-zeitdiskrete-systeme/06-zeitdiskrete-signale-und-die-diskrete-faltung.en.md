---
title: Stage 5: Discrete-time signals and discrete convolution
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Sampling and Discrete-Time Systems
order: 3240600
summary: From now on, all calculations use only the sequences of numbers s(n) .
tags: discrete convolution, unit impulse, shift-invariant, LSI system, impulse response, difference, accumulation, FIR filter
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
From now on, all calculations use only the sequences of numbers $s(n)$. This stage carries convolution, elementary signals and LTI systems over to sequences.
:::

**Convolution of the samples.** If the input $s$ and the impulse response $h$ of a system are low-pass signals and sampling is at the Nyquist rate, each can be written as an si series [(3.3)](abtasttheorem-und-ruckgewinnung.html#gl-3-3). Because $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$ ([Part 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), the samples of the output follow from the samples alone:

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

:::abbildung et3/k4block 4
First-order system $g(n)=a_0s(n)+a_1s(n-1)+b_1g(n-1)$. The box $T$ stores a value for one clock cycle. On the left the nonrecursive part, on the right the feedback of the output.
:::

:::aufgabe Exercise 4 ★ Discrete convolution by hand
<span class="anker" id="aufg-4"></span>

Convolve $s=(1,1,1)$ with $h=(1,2)$, both starting at $n=0$. How long is the result, and why?

:::loesung
$g(0)=1$, $g(1)=1\cdot2+1\cdot1=3$, $g(2)=3$, $g(3)=1\cdot2=2$: $(1,3,3,2)$. Length $3+2-1=4$: the last nonzero value arises when the last value of $h$ meets the last value of $s$.
:::
:::
