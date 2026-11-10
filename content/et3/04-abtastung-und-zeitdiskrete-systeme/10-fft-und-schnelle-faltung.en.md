---
title: Stage 9: FFT and fast convolution
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Sampling and Discrete-Time Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Chapter 4: Sampling and Discrete-Time Systems
order: 3241000
summary: The DFT needs M 2 multiplications.
tags: fast Fourier transform, circular
lang: en
---

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
