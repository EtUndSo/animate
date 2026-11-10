---
title: Stage 6: A recursive system
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Sampling and Discrete-Time Systems
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Chapter 4: Sampling and Discrete-Time Systems
order: 3240700
summary: The simplest IIR system shows how feedback produces an infinitely long impulse response and when the system is stable.
tags: causal, stable
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
The simplest IIR system shows how feedback produces an infinitely long impulse response and when the system is stable.
:::

The system $g(n)=s(n)+b\,g(n-1)$ adds the last output, weighted by $b$, to the input. For $s=\delta$ and a system at rest before $n=0$:

<span class="anker" id="gl-6-1"></span>
$$h(n)=\delta(n)+b\,h(n-1)\quad\Longrightarrow\quad h(0)=1,\ h(1)=b,\ h(2)=b^2,\dots\quad\Longrightarrow\quad h(n)=\varepsilon(n)\,b^n. \tag{6.1}$$

The impulse circulates in the feedback loop again and again and is multiplied by $b$ each time. The system is __causal__ ($h(n)=0$ for $n<0$). It is __stable__ if $\sum_n|h(n)|<\infty$ (the discrete counterpart of [Chapter 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)), so here exactly for $|b|<1$, with $\sum_n|b|^n=\frac{1}{1-|b|}$.

**Response to a rectangular sequence.** Input $s(n)=\varepsilon(n)-\varepsilon(n-M)$ ($M$ ones). With the convolution sum and the formula for the geometric sum $\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$:

<span class="anker" id="gl-6-2"></span>
$$g(n)=\begin{cases}0&n<0,\\[2pt]\displaystyle\sum_{m=0}^{n}b^{n-m}=\frac{1-b^{n+1}}{1-b}&0\le n<M,\\[8pt]\displaystyle\sum_{m=0}^{M-1}b^{n-m}=\frac{b^{n-M+1}-b^{n+1}}{1-b}&n\ge M.\end{cases} \tag{6.2}$$

In the reference model ($b=0.6$, $M=4$): $g=1,\ 1.6,\ 1.96,\ 2.176$, then $1.306,\ 0.783,\ 0.470,\dots$, each value 0.6 times the previous one (Fig. [5](#abb-5)). This is the discrete counterpart of the response of the RC circuit to a rectangular pulse in [Chapter 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html).

:::abbildung et3/k4rek 5
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

$g(n)=s(n)+0.5\,s(n-1)+0.6\,g(n-1)$ (Fig. [4](zeitdiskrete-signale-und-die-diskrete-faltung.html#abb-4) with $a_0=1$, $a_1=0.5$, $b_1=0.6$).

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
