---
title: 第 6 阶段：一个递归系统
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 采样与离散时间系统
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: 第 4 章：采样与离散时间系统
order: 3240700
summary: 通过最简单的 IIR 系统可以看出：反馈如何产生无限长的单位脉冲响应，以及系统何时稳定。
tags: 因果, 稳定
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
通过最简单的 IIR 系统可以看出：反馈如何产生无限长的单位脉冲响应，以及系统何时稳定。
:::

系统 $g(n)=s(n)+b\,g(n-1)$ 把以 $b$ 加权的上一个输出值加到输入上。对于 $s=\delta$，且系统在 $n=0$ 之前处于静止状态，有：

<span class="anker" id="gl-6-1"></span>
$$h(n)=\delta(n)+b\,h(n-1)\quad\Longrightarrow\quad h(0)=1,\ h(1)=b,\ h(2)=b^2,\dots\quad\Longrightarrow\quad h(n)=\varepsilon(n)\,b^n. \tag{6.1}$$

这个脉冲在反馈环路中一圈又一圈地循环，每循环一次就乘以 $b$。该系统是__因果__的（$n<0$ 时 $h(n)=0$）。若 $\sum_n|h(n)|<\infty$（[第 1 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)中条件的离散对应形式），则系统是__稳定__的；在这里，这恰好对应于 $|b|<1$，此时 $\sum_n|b|^n=\frac{1}{1-|b|}$。

**对矩形序列的响应。** 输入 $s(n)=\varepsilon(n)-\varepsilon(n-M)$（$M$ 个 1）。利用卷积和以及等比数列求和公式 $\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$：

<span class="anker" id="gl-6-2"></span>
$$g(n)=\begin{cases}0&n<0,\\[2pt]\displaystyle\sum_{m=0}^{n}b^{n-m}=\frac{1-b^{n+1}}{1-b}&0\le n<M,\\[8pt]\displaystyle\sum_{m=0}^{M-1}b^{n-m}=\frac{b^{n-M+1}-b^{n+1}}{1-b}&n\ge M.\end{cases} \tag{6.2}$$

在参考模型中（$b=0.6$，$M=4$）：$g=1,\ 1.6,\ 1.96,\ 2.176$，随后为 $1.306,\ 0.783,\ 0.470,\dots$，每个值都是前一个值的 0.6 倍（图 [5](#abb-5)）。这就是[第 1 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)中 RC 电路对矩形脉冲的响应在离散情形下的对应。

:::abbildung et3/k4rek 5
$b=0.6$ 的递归系统。左：单位脉冲响应。右：对四个 1 的响应；它上升到 2.176，然后每个采样周期按因子 0.6 衰减。
:::

:::aufgabe 练习 5 ★★ 研究递归系统
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

直接用递推式验证参考模型中 $g(n)$ 的前五个值。

</li>

<li>

对于无限长的全 1 序列（$M\to\infty$），输出趋于什么值？与 $\sum_nh(n)$ 进行比较。

</li>

<li>

当 $b=-0.6$ 和 $b=1.1$ 时，$h(n)$ 是什么样的？哪个系统是稳定的？

</li>

</ol>

:::loesung
(a) $g(0)=1$，$g(1)=1+0.6=1.6$，$g(2)=1+0.96=1.96$，$g(3)=1+1.176=2.176$，$g(4)=0+0.6\cdot2.176=1.306$。

(b) $\frac{1}{1-b}=2.5$。这正是 $\sum_nh(n)=\sum0.6^n=2.5$：对于恒定输入 1，卷积把单位脉冲响应的所有值加起来。此外，$H_\mathrm a(0)=2.5$。

(c) $b=-0.6$：$1,\ -0.6,\ 0.36,\ -0.216,\dots$，符号交替，逐渐衰减，稳定。$b=1.1$：$1,\ 1.1,\ 1.21,\dots$，不断增长，不稳定。
:::
:::

:::aufgabe 练习 6 ★★ 一阶系统
<span class="anker" id="aufg-6"></span>

$g(n)=s(n)+0.5\,s(n-1)+0.6\,g(n-1)$（即图 [4](zeitdiskrete-signale-und-die-diskrete-faltung.html#abb-4) 中 $a_0=1$，$a_1=0.5$，$b_1=0.6$）。

<ol class="al">

<li>

用递推式计算 $h(0)$ 到 $h(3)$。

</li>

<li>

证明 $h(n)=\frac{11}{6}\,0.6^n\varepsilon(n)-\frac56\delta(n)$。

</li>

</ol>

:::loesung
(a) $h(0)=1$，$h(1)=0.5+0.6\cdot1=1.1$，$h(2)=0.6\cdot1.1=0.66$，$h(3)=0.396$。

(b) 由该公式得 $h(0)=\frac{11}{6}-\frac56=1$，$h(1)=\frac{11}{6}\cdot0.6=1.1$。从 $n=2$ 起输入为零，递推式为 $h(n)=0.6\,h(n-1)$，而该公式满足这一递推式，因为 $\frac{11}{6}0.6^n=0.6\cdot\frac{11}{6}0.6^{n-1}$。（利用 z 变换，由分解式 $H(z)=-\frac56+\frac{11/6}{1-0.6z^{-1}}$ 即可得到该公式。）
:::
:::
