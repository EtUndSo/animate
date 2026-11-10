---
title: 要点
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 低通与带通系统
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: 第 5 章：低通与带通系统
order: 3251400
summary: 无失真传输、理想低通、 复包络与群时延
tags: 
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

无失真的意思是：只被放大和延迟。为此需要恒定的模和随频率线性下降的相位。

</li>

<li>

严格限带的（理想）低通不是因果的，在阶跃处过冲约 9 %，并且需要 $1/(2f_\mathrm g)$ 的上升时间。较平缓的边沿以牺牲陡峭度为代价减小过冲。

</li>

<li>

带通信号是搭载在载波上的低通信号（复包络）。包络可以像低通信号一样计算：它被延迟一个群时延，载波则被延迟一个相位时延。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

无失真：$h=h_0\delta(t-t_0)$，$H=h_0\mathrm{e}^{-\mathrm{j}2\pi t_0f}$：模恒定，相位线性。

</li>

<li>

$a=-20\lg|H|$ dB；$t_\mathrm p=-\frac{\varphi}{2\pi f}$；$t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}$。

</li>

<li>

理想低通：$\operatorname{rect}(f/2f_\mathrm g)\leftrightarrow2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$，非因果；$f_\mathrm g t_m=\frac12$；过冲 21.7 %（冲激响应）、8.95 %（阶跃响应）。

</li>

<li>

阶跃响应 $\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$，$\operatorname{Si}(\infty)=\frac\pi2$，上升时间 $\frac{1}{2f_\mathrm g}$。

</li>

<li>

截断冲激响应 $=$ 频谱中的卷积；平滑的窗：阻带更深，边沿更平缓。

</li>

<li>

脉冲成形滤波器：$T\operatorname{rect}(Tf)[1+\cos(2\pi Tf)]$，过冲小。

</li>

<li>

$H(f)=\frac12H_T(f-f_0)+\frac12H_T^*(-f-f_0)$；$s=\operatorname{Re}\{s_T\mathrm{e}^{\mathrm{j}2\pi f_0t}\}=s_{Tr}\cos-s_{Ti}\sin$；$s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$。

</li>

<li>

$g_T=\frac12s_T*h_T$；包络延迟 $t_\mathrm g$，载波延迟 $t_\mathrm p$。

</li>

<li>

带通采样：每秒 $2\Delta f$ 个值；数字高通：$(-1)^nh_{\mathrm{TP}}(n)$。

</li>

</ul>
:::
