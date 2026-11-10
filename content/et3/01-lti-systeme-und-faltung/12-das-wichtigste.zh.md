---
title: 要点
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / LTI 系统与卷积
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: 第 1 章：LTI 系统与卷积
order: 3211200
summary: 为什么对单个冲激的响应 能够描述整个系统
tags: 
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

每个信号都是无穷多个短冲激的叠加：在每个时刻 $\tau$ 都有一个权重为 $s(\tau)\,\mathrm{d}\tau$ 的冲激。

</li>

<li>

LTI 系统对平移后的冲激的响应是平移后的冲激响应 $h(t-\tau)$（时不变性），对冲激之和的响应是各响应之和（线性）。

</li>

<li>

因此，输出就是卷积 $g(t)=\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$，而 $h(t)$ 完整地描述了该系统。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

平移 $t\to t-t_0$ 产生延迟，展缩 $t\to t/T$ 使信号变宽；$a\operatorname{rect}\bigl(\frac{t-t_0}{T}\bigr)$：中心 $t_0$，持续时间 $|T|$，高度 $a$。

</li>

<li>

RC 低通滤波器：$H(F)=\dfrac{1}{1+\mathrm{j}2\pi FRC}$，$|H|=\dfrac{1}{\sqrt{1+(2\pi FRC)^2}}$， $\varphi=-\arctan(2\pi FRC)$；阶跃响应为 $1-\mathrm{e}^{-t/RC}$。

</li>

<li>

LTI：叠加原理，以及 $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$。

</li>

<li>

$s(t)=\int s(\tau)\delta(t-\tau)\mathrm{d}\tau$，以及 $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau=s*h$。

</li>

<li>

计算方法：反转、平移、相乘、积分。

</li>

<li>

$s*\delta=s$；交换律、结合律（级联：$h_1*h_2$）、分配律（并联：$h_1+h_2$）。

</li>

<li>

$s(t)\delta(t-T)=s(T)\delta(t-T)$；$\delta(bt)=\delta(t)/|b|$；$\delta(t-t_0)*s=s(t-t_0)$；$\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$。

</li>

<li>

阶跃响应 $=\int h$，冲激响应 $=\frac{\mathrm{d}}{\mathrm{d} t}$ 阶跃响应。

</li>

<li>

因果：$t<0$ 时 $h(t)=0$。稳定：$\int|h|\mathrm{d} t<\infty$。

</li>

</ul>
:::

**下一步。** 卷积的计算量很大：每个时刻 $t$ 都要单独算一个积分。下一部分换一种方式分解信号，使积分变成简单的乘法。
