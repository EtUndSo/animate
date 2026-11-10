---
title: 第 10 阶段：匹配滤波器（相关滤波器）
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 随机信号
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: 第 7 章：随机信号
order: 3271100
summary: 一个已知的脉冲 s(t) 受噪声干扰后到达。用什么样的滤波器，才能使它在采样时刻 T 显现得最清楚？
tags: 匹配滤波器, 相关接收机
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
一个已知的脉冲 $s(t)$ 受噪声干扰后到达。用什么样的滤波器，才能使它在采样时刻 $T$ 显现得最清楚？
:::

**出发点。** 接收机输入端为 $s(t)+n(t)$，其中 $n$ 为白噪声。滤波器 $h$ 输出 $y=g+n_e$，其中有用分量为 $g=s*h$，噪声分量为 $n_e=n*h$。在 $T$ 时刻采样。该时刻的信噪比为

$$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}=\frac{E_s}{N_0}\cdot\underbrace{\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{\int|h|^2\mathrm{d}\tau\int|s(T-\tau)|^2\mathrm{d}\tau}}_{=|p|^2\le1}.$$

右边的分式是 $h(\tau)$ 与 $s(T-\tau)$ 之间的相关系数（[第 6 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)）的平方。它至多为 1，并且恰好在二者形状相同时等于 1。

:::satz 定理 10.1 (匹配滤波器)
<span class="anker" id="satz-10-1"></span>

在白噪声背景下，可达到的最佳信噪比为

<span class="anker" id="gl-10-1"></span>
$$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0},\qquad\text{条件为}\qquad h(t)=a\,s(T-t),\quad H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}. \tag{10.1}$$
:::

⁠**如何理解：**最佳冲激响应就是信号本身经时间反转并平移 $T$ 后的结果，即__匹配滤波器__（相关滤波器）。它在无噪声时的输出为 $g(t)=a\,\varphi^E_{ss}(t-T)$，即信号的自相关函数平移后的结果，而采样恰好发生在其最大值处。令人惊讶的是，结果只取决于信号的*能量*，而与信号的形状无关。一个短而高的脉冲与一个能量相同的长而平的脉冲效果一样好。为使滤波器是因果的，$T$ 至少要等于信号的持续时间。与之等价的是__相关接收机__（相关器）：它把接收信号乘以 $s(t)$，再在信号的持续时间内积分。

:::aufgabe 练习 10 ★★ 噪声中的矩形脉冲
<span class="anker" id="aufg-10"></span>

接收到一个高度为 1 V、持续时间为 1 ms 的矩形脉冲，同时还有功率谱密度为 $N_0=10^{-6}$ V$^2$/Hz 的白噪声。

<ol class="al">

<li>

匹配滤波器是什么样的？它达到的 $S_a/N$ 是多少（以 dB 表示）？

</li>

<li>

无噪声时输出是什么样的？必须在什么时刻采样？

</li>

<li>

把脉冲缩短到 0.25 ms，高度不变。有什么变化？

</li>

</ol>

:::loesung
(a) $h(t)=a\,s(T-t)$：仍是一个 1 ms 的矩形，当 $T\ge1$ ms 时是因果的。$E_s=1\,\mathrm{V^2}\cdot1\,\mathrm{ms}=10^{-3}$ V$^2$s，因此 $S_a/N=10^{-3}/10^{-6}=1000$，即 30 dB。

(b) 矩形的自相关函数，即一个宽 2 ms 的三角形，平移了 $T$：它从 $t=T-1$ ms 开始上升，在 $t=T$ 处达到最大值。取 $T=1$ ms 时，恰好在脉冲结束的时刻采样；此时滤波器已经“看到”了整个脉冲。

(c) $E_s$ 降为四分之一，$S_a/N=250$，即 24 dB，差了 6 dB。起作用的只有能量。高度相同时，较短的脉冲意味着较少的能量。
:::
:::
