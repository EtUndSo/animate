---
title: 第 7 阶段：离散时间傅里叶变换
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 采样与离散时间系统
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: 第 4 章：采样与离散时间系统
order: 3240800
summary: 数值序列具有怎样的频谱？它就是理想采样信号的频谱，直接由样本值计算。
tags: 周期卷积
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
数值序列具有怎样的频谱？它就是理想采样信号的频谱，直接由样本值计算。
:::

把 $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ 代入傅里叶积分，利用筛选性质后只剩下一个求和。归一化到 $T=1$ 后：

:::satz 定理 7.1 (离散时间傅里叶变换)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf},\qquad s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f. \tag{7.1}$$
:::

⁠**如何理解：**$S_\mathrm a(f)$ 是周期为 1 的周期函数，而 1 正是采样率。一个周期 $|f|\le\frac12$ 就包含了全部信息。因此，反变换只需在长度为 1 的区间上积分。这个求和式是关于 $f$ 的傅里叶级数，以样本值为系数。

::::beispiel
对 $|b|<1$ 的 $s(n)=\varepsilon(n)\,b^n$（等比级数）：

<span class="anker" id="gl-7-2"></span>
$$S_\mathrm a(f)=\sum_{n=0}^{\infty}\bigl(b\,\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)^n=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}},\qquad|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}. \tag{7.2}$$

这同时也是第 [6](ein-rekursives-system.html#stufe-6) 阶段中递归系统的频率响应 $H_\mathrm a(f)$。当 $b=0.6$ 时：$f=0$ 处 $|H_\mathrm a|=2.5$，$f=0.1$ 处为 $1.60$，$f=0.25$ 处为 $0.86$，$f=0.5$ 处为 $0.625$（图 [6](#abb-6)）。该系统是低通滤波器，但其频率响应是周期性的：在 $f=1$ 处，它的放大作用又和 $f=0$ 处一样强。

:::abbildung et3/k4dtft 6
$b=0.6$ 的递归系统频率响应的幅值。它以采样率为周期。两条红线之间是足以描述全部信息的那一个周期。
:::
::::

**卷积与相乘。** 与函数的情形一样，$s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$。两个序列的乘积对应于两个频谱在一个周期上的__周期卷积__：

<span class="anker" id="gl-7-3"></span>
$$s(n)\cdot h(n)\;\circ\!\!-\!\!\bullet\;\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu. \tag{7.3}$$

:::aufgabe 练习 7 ★ 滑动平均
<span class="anker" id="aufg-7"></span>

$h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$ 对三个相继的值求平均。

<ol class="al">

<li>

证明 $H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$。

</li>

<li>

在哪个频率处 $H_\mathrm a=0$？因此该滤波器会完全消除哪个振荡？原因是什么（提示：周期为 3 的振荡的三个值之和）？

</li>

</ol>

:::loesung
(a) $\frac13\bigl(1+\mathrm{e}^{-\mathrm{j}2\pi f}+\mathrm{e}^{-\mathrm{j}4\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl(\mathrm{e}^{\mathrm{j}2\pi f}+1+\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$。

(b) $\cos(2\pi f)=-\frac12$，因此 $f=\frac13$（当 $f_\mathrm A=1$ kHz 时为 333 Hz）。每个周期有三个值的振荡由三个彼此相隔 $120^\circ$ 的相量组成。它们的和为零；在每个窗口中，滤波器看到的恰好是一个完整的周期。
:::
:::
