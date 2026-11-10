---
title: 第 7 阶段：矩形、si 函数与三角形
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 傅里叶级数与变换
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: 第 3 章：傅里叶级数与变换
order: 3230800
summary: 有三个变换对经常出现。借助上述定理，它们都可以由一次计算得到。
tags: 
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
有三个变换对经常出现。借助上述定理，它们都可以由一次计算得到。
:::

**矩形。** 利用 $\operatorname{si}(x)=\sin(x)/x$：

$$\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{\mathrm{e}^{-\mathrm{j}\pi f}-\mathrm{e}^{\mathrm{j}\pi f}}{-\mathrm{j}2\pi f}=\frac{\sin(\pi f)}{\pi f}=\operatorname{si}(\pi f).$$

:::satz 定理 7.1 (矩形、si 函数与三角形)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \operatorname{rect}\Bigl(\frac tT\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf),\\ \operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf),\\ \Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)&\;\circ\!\!-\!\!\bullet\;\operatorname{si}^2(\pi f),\\ \operatorname{si}(\pi t)*\operatorname{si}(\pi t)&=\operatorname{si}(\pi t). \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**如何理解：**持续时间为 $T$ 的矩形，其频谱的高度为 $T$（即矩形的面积），零点位于 $1/T$ 的所有非零整数倍处。时长加倍，频谱宽度就减半（图 [6](#abb-6)）。式 [(7.2)](#gl-7-2) 由对偶性得到，式 [(7.3)](#gl-7-3) 由卷积定理得到；式 [(7.4)](#gl-7-4) 成立，是因为在频域中 $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$：理想低通滤波器不会改变已经限制在其通带内的信号。

:::abbildung et3/k3rectsi 6
$\operatorname{rect}(t/T)$ 及其频谱 $|T|\operatorname{si}(\pi Tf)$，$T=1$ s 和 $T=2$ s。持续时间加倍：高度加倍（$=$ 面积），宽度减半，第一个零点位于 $1/T$。
:::

:::ltspice 矩形脉冲的频谱
⁠**绘制：**只需一个电压源 `voltage`，取 `PULSE(0 1 0 1u 1u {T0} 16)`：持续时间为 $T_0$ 的矩形，每 16 s 重复一次。

⁠**指令：**`.param T0=1`，`.step param T0 list 1 2`，`.tran 0 16 0 1m`，再加上用来关闭数据压缩的 `.options plotwinsize=0` 和 `.four 0.0625 40 V(in)`。

⁠**你会看到：**每 16 s 重复一次，使频谱变成间隔为 $1/16$ Hz 的谱线（第 [4](vom-periodischen-zum-einmaligen-signal.html#stufe-4) 阶段）。`.four` 给出它们的幅度 $\frac{2}{16}\,|T_0\operatorname{si}(\pi T_0f)|$，即 si 包络的采样值。$T_0=1$ s 时，1 Hz 和 2 Hz 处的谱线为零；$T_0=2$ s 时，0.5 Hz、1 Hz、1.5 Hz 和 2 Hz 处的谱线都已为零。直流分量从 0.0625 加倍到 0.125。因此，持续时间加倍意味着宽度减半、高度加倍，与图 [6](#abb-6) 相同。在 FFT 视图中可以直接看到包络及其零点。
:::

:::aufgabe 练习 8 ★ si 函数的面积与能量
<span class="anker" id="aufg-8"></span>

不用积分，计算 $\int_{-\infty}^\infty\operatorname{si}(\pi t)\mathrm{d} t$ 和 $\int_{-\infty}^\infty\operatorname{si}^2(\pi t)\mathrm{d} t$。利用面积定理和帕塞瓦尔定理。

:::loesung
面积定理：$\int\operatorname{si}(\pi t)\mathrm{d} t=\mathcal{F}\{\operatorname{si}(\pi t)\}(0)=\operatorname{rect}(0)=1$。帕塞瓦尔定理：$\int\operatorname{si}^2(\pi t)\mathrm{d} t=\int\operatorname{rect}^2(f)\mathrm{d} f=1$。
:::
:::

:::aufgabe 练习 9 ★★ 三角形与多次卷积
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

求 $\Lambda(t/2)$（半宽为 2 s 的三角形）的频谱。零点在哪里？

</li>

<li>

$\operatorname{rect}*\operatorname{rect}*\operatorname{rect}$ 的频谱是什么？为什么卷积的次数越多，旁瓣衰减得越快？

</li>

</ol>

:::loesung
(a) $\Lambda(t)\circ\!\!-\!\!\bullet\operatorname{si}^2(\pi f)$，再由 $T=2$ 的尺度变换得：$\Lambda(t/2)\circ\!\!-\!\!\bullet\,2\operatorname{si}^2(2\pi f)$。零点位于 $f=k/2$，$k\neq0$。

(b) $\operatorname{si}^3(\pi f)$。每多卷积一次，频谱就多乘一个 $\operatorname{si}(\pi f)$，而它在旁瓣中按 $1/(\pi f)$ 衰减。对 $M$ 重卷积，旁瓣按 $1/f^M$ 衰减。在时域中：矩形有跳变（按 $1/f$ 衰减），三角形有折点（$1/f^2$），三重卷积的导数是连续的（$1/f^3$）。信号越光滑，其频谱衰减越快。
:::
:::
