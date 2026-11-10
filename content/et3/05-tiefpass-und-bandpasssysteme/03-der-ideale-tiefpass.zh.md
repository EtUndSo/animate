---
title: 第 2 阶段：理想低通
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 低通与带通系统
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: 第 5 章：低通与带通系统
order: 3250300
summary: 理想低通让所有不超过 f mathrm g 的频率不变地通过，并阻断高于 f mathrm g 的所有频率。本阶段说明这种陡峭的截止在时域中意味着什么。
tags: 信号持续时间
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
理想低通让所有不超过 $f_\mathrm g$ 的频率不变地通过，并阻断高于 $f_\mathrm g$ 的所有频率。本阶段说明这种陡峭的截止在时域中意味着什么。
:::

:::satz 定理 2.1 (理想低通)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\qquad\bullet\!\!-\!\!\circ\qquad h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt). \tag{2.1}$$
:::

⁠**如何理解：**冲激响应向两个方向一直延伸到无穷远。因此理想低通*不是因果的*：它必须在冲激到来之前就作出响应。它是一个数学上的极限对象，只能近似实现（第 [4](kausale-naherung.html#stufe-4)、[6](zeitdiskrete-tiefpasse-entwurf-mit-fenstern.html#stufe-6) 阶段）。

**持续时间与带宽。** 把冲激响应的__信号持续时间__ $t_m$ 取为一个矩形的宽度，该矩形与冲激响应具有相同的高度 $h_{\max}$ 和相同的面积：

<span class="anker" id="gl-2-2"></span>
$$t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}. \tag{2.2}$$

对理想低通，$H(0)=1$，$h_{\max}=2f_\mathrm g$，因此 $t_m=\frac{1}{2f_\mathrm g}$，$f_\mathrm g\cdot t_m=\frac12$。一般地，低通滤波器满足 $f_\mathrm g\cdot t_m=\text{常数}$：带宽加倍意味着响应持续时间减半。这就是[第 3 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中的尺度变换定理。

**过冲。** 对 si 函数，绝对值最大的旁瓣极值 $a_1$ 与主极大值 $a_0$ 之比为

$$\ddot u=\Bigl|\frac{a_1}{a_0}\Bigr|=21.7\,\%,$$

它与 $f_\mathrm g$ 无关（$\operatorname{si}(\pi u)$ 的第一个旁瓣极小值位于 $u=1.43$ 处，其值为 $-0.217$）。改变 $f_\mathrm g$ 只会压缩曲线，而不会改变它的形状。

:::aufgabe 练习 2 ★ 用于语音的理想低通
<span class="anker" id="aufg-2"></span>

一个 $f_\mathrm g=4$ kHz 的理想低通。其冲激响应的信号持续时间和过冲各是多少？若 $f_\mathrm g=8$ kHz，有什么变化？

:::loesung
$t_m=\frac{1}{2f_\mathrm g}=125$ µ s，过冲 21.7 %。在 8 kHz 时，信号持续时间减半为 62.5 µ s。过冲仍为 21.7 %，因为冲激响应只是被压缩了。
:::
:::
