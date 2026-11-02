---
title: 第 2 阶段：采样信号的频谱
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 采样与离散时间系统
order: 3240300
summary: 采样对频谱有什么影响？本阶段将表明：频谱周期性地重复。
tags: 频谱镜像
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
采样对频谱有什么影响？本阶段将表明：频谱周期性地重复。
:::

**思路。** 频率相差采样率 $1/T$ 整数倍的两个振荡，具有相同的样本值：

$$\mathrm{e}^{\mathrm{j}2\pi(f_0+k/T)nT}=\mathrm{e}^{\mathrm{j}2\pi f_0nT}\cdot\underbrace{\mathrm{e}^{\mathrm{j}2\pi kn}}_{=1}.$$

样本值无法区分它们。因此，样本值的频谱在 $f_0$ 处和在 $f_0+k/T$ 处必定一样。频谱是周期性的。

:::satz 定理 2.1 (理想采样信号的频谱)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$S_\mathrm a(f)=\frac1T\sum_{k=-\infty}^{\infty}S\Bigl(f-\frac kT\Bigr)\qquad(T>0). \tag{2.1}$$
:::

⁠**如何理解：**原信号的频谱以不变的形状出现，但乘上了因子 $1/T$，并在采样率的每个整数倍处重复出现。这些副本称为__频谱镜像__。

:::herleitung 采样信号的频谱
相乘变为卷积（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)），而狄拉克梳状函数的频谱仍是梳状函数：

$$s(t)\cdot\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;S(f)*\frac1T\sum_k\delta\Bigl(f-\frac kT\Bigr)=\frac1T\sum_kS\Bigl(f-\frac kT\Bigr).$$

与平移后的狄拉克冲激做卷积，就是把频谱平移。
:::

:::abbildung et3/k4spektrum 1
对一个最高频率为 $f_\mathrm g=300$ Hz 的频谱（蓝色，为直观起见画成三角形）进行采样。上：以 1 kHz 采样，位于 1 kHz 整数倍处的副本相互分开。下：以 500 Hz 采样，间隔 500 Hz 的副本相互重叠，其和（红色）不再是原频谱。图中略去了因子 $1/T$。
:::

:::frage 频谱是怎么“知道”信号被采样过的？采样点之间的信号明明就这样没有了。
正是因为这一点。在采样点之间，采样信号为零，只有冲激处例外。凡是在所有点 $nT$ 上取值都相同的振荡，都同样好地描述了这个信号。频谱无法在它们之间做出选择，于是把它们全部包含进来：原信号以及它位于 $1/T$ 每个整数倍处的副本。
:::
