---
title: 第 5 阶段：回波法与脉冲成形滤波器
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 低通与带通系统
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: 第 5 章：低通与带通系统
order: 3250600
summary: 如何设计过冲较小的低通？用平移后的 si 函数组合出冲激响应，并选择它们的权重。
tags: 回波, 升余弦滤波器
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
如何设计过冲较小的低通？用平移后的 si 函数组合出冲激响应，并选择它们的权重。
:::

**回波法。** 根据采样定理，截止频率不超过 $f_\mathrm g=\frac{1}{2T}$ 的低通，其任一冲激响应都是一个 si 级数：

<span class="anker" id="gl-5-1"></span>
$$h(t)=\sum_nh(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$h(nT)=\int_{-f_\mathrm g}^{f_\mathrm g}H(f)\,\mathrm{e}^{\mathrm{j}2\pi nTf}\,\mathrm{d} f. \tag{5.2}$$

每个样本值 $h(nT)$ 都是一个__回波__：一个平移了 $nT$ 的 si 函数。在频谱中，这就成为关于 $f$ 的傅里叶级数。若 $h$ 是实的偶函数，则 $H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\cos(2\pi nTf)\bigr]$。

**脉冲成形滤波器。** 在主分量 $\operatorname{si}(\pi t/T)$ 上加上两个位于 $\pm T$ 处、幅度为 $a$ 的回波。当 $a=\frac12$ 时，旁侧振荡在很大程度上相互抵消，频谱获得一个余弦形的平缓边沿：

<span class="anker" id="gl-5-3"></span>
$$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t+T}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t-T}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]. \tag{5.3}$$

这就是__升余弦滤波器__（余弦滚降滤波器）。它的过冲为 2.7 %，而不是 21.7 %；作为代价，主瓣宽度加倍（第一个零点在 $2T$ 处，而不是 $T$ 处）。图 [3](#abb-3) 给出了归一化为相同面积的两个冲激响应。

:::abbildung et3/k5pulsform 3
理想低通和脉冲成形滤波器的冲激响应（面积都为 $T$）。脉冲成形滤波器衰减得快得多：它的最大旁瓣极值是主极大值的 2.7 %，而不是 21.7 %。
:::

**横向滤波器（抽头延迟线）。** 延迟并加权的副本之和，可以用一串延迟单元来实现：对各抽头的信号加权后相加。为了不让任何单元需要用到未来的值，把整体一起延迟。这与 FIR 滤波器（[第 4 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)）的结构相同。

:::aufgabe 练习 5 ★★ 升余弦滤波器
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

由式 [(5.1)](#gl-5-1) 推导式 [(5.3)](#gl-5-3) 中的 $H(f)$。

</li>

<li>

$H$ 在 $f=0$ 和 $f=f_\mathrm g=\frac{1}{2T}$ 处的值各是多少？为什么那里的边沿是光滑的？

</li>

</ol>

:::loesung
(a) 在 $t=mT$ 处，$\operatorname{si}(\pi(t\pm T)/T)$ 只在 $m=\mp1$ 时等于 1，其余均为零。因此 $h(0)=1$，$h(\pm T)=\frac12$，其他所有 $h(nT)=0$。由式 [(5.1)](#gl-5-1)：$H=T\operatorname{rect}(Tf)\bigl[1+\frac12\mathrm{e}^{\mathrm{j}2\pi Tf}+\frac12\mathrm{e}^{-\mathrm{j}2\pi Tf}\bigr]=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]$。

(b) $H(0)=2T$，$H(\frac{1}{2T})=T(1+\cos\pi)=0$。斜率 $-2\pi T^2\sin(2\pi Tf)$ 在 $f=\frac{1}{2T}$ 处也为零。频率响应既无跳变、也无折点地趋于零。频谱越光滑，冲激响应衰减得越快（[第 3 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)）。
:::
:::
