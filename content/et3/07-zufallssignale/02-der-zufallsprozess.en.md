---
title: Stage 1: The random process
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Random Signals
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Chapter 7: Random Signals
order: 3270200
summary: How do you describe a signal whose waveform you do not know?
tags: sample function, random process, random variable, expected value, autocorrelation function
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
How do you describe a signal whose waveform you do not know? You imagine many signals of the same kind and average over them.
:::

**The idea.** If you measure the noise of many identically built resistors at the same temperature, you get many different curves ${}^ks(t)$, $k=1,2,\dots$ (Fig. [1](#abb-1)). Each one is called a __sample function__ or realization. The imagined totality of all of them is called a __random process__ $s(t)$. The values of all sample functions at a fixed instant $t_1$ form a __random variable__ $s(t_1)$.

:::definition Definition 1.1 (Ensemble averages)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} \mathrm E\{s(t_1)\}&=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1),\qquad \mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr],\\ \varphi_{ss}(t_1,t_2)&=\mathrm E\{s(t_1)\,s(t_2)\}. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**How to read it:** $\mathrm E\{\cdot\}$ is called the __expected value__ or ensemble average: you average over all sample functions at the same instant, that is, vertically in Fig. [1](#abb-1). With $F[x]=x^2$ you obtain the mean square value. The __autocorrelation function__ averages the product of the values at two instants. It tells you how strongly the value at $t_2$ is related to the value at $t_1$.

:::abbildung et3/k7schar 1
Three sample functions of a random process (simulated, mean value 1). The ensemble average is formed vertically, over all sample functions at the same $t_1$ (red, dashed). The time average is formed horizontally, along one sample function.
:::
