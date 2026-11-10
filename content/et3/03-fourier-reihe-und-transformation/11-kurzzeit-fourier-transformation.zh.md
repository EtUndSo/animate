---
title: 第 10 阶段：短时傅里叶变换
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 傅里叶级数与变换
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: 第 3 章：傅里叶级数与变换
order: 3231100
summary: 频谱 S(f) 描述的是信号在全部时间上的情况。然而，语音或音乐的频率在不断变化。短时傅里叶变换（STFT）要回答的问题是：信号 在时刻 t 附近 包含哪些频率？
tags: 汉宁窗, 语谱图（时频图）
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
频谱 $S(f)$ 描述的是信号在全部时间上的情况。然而，语音或音乐的频率在不断变化。短时傅里叶变换（STFT）要回答的问题是：信号*在时刻 $t$ 附近*包含哪些频率？
:::

**思路。** 截取 $t$ 附近的一个片段，只对这一片段进行变换。采用宽度为 $T_0$ 的矩形窗：

$$s_T(\tau,t)=s(\tau)\operatorname{rect}\Bigl(\frac{\tau-t}{T_0}\Bigr)\;\circ\!\!-\!\!\bullet\;S_T(f,t)=S(f)*\bigl[T_0\operatorname{si}(\pi T_0f)\,\mathrm{e}^{-\mathrm{j}2\pi tf}\bigr].$$

片段的频谱是真实频谱被窗的 si 频谱模糊之后的结果。短窗在时间上定位准确，但在频率上模糊严重（尺度变换定理）。矩形的硬边沿还会产生衰减缓慢的旁瓣。因此，平滑的窗更好，例如__汉宁窗__

<span class="anker" id="gl-10-1"></span>
$$w(\tau)=\tfrac12\Bigl[1+\cos\Bigl(\frac{2\pi\tau}{T_0}\Bigr)\Bigr]\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)=\cos^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr). \tag{10.1}$$

:::satz 定理 10.1 (短时傅里叶变换)
<span class="anker" id="satz-10-1"></span>

<span class="anker" id="gl-10-2"></span>
$$S_T(f,t)=\int_{-\infty}^{\infty}s(\tau)\,w(\tau-t)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau. \tag{10.2}$$

若依次平移 $T$ 的各个窗相加为常数，即 $\sum_nw(\tau-nT)=c$，则

<span class="anker" id="gl-10-3"></span>
$$s(\tau)=\frac1c\sum_ns(\tau)\,w(\tau-nT),\qquad S(f)=\frac1c\sum_nS_T(f,nT). \tag{10.3}$$
:::

⁠**如何理解：**$S_T(f,t)$ 是一个随时间变化的频谱。把 $|S_T|$ 作为 $t$ 和 $f$ 的函数画出来，就得到__语谱图（时频图）__。对于偏移量 $T=T_0/2$ 的汉宁窗，$c=1$，因为 $\cos^2x+\sin^2x=1$（图 [8](#abb-8)）：各片段无缝地拼合成整个信号，它们的频谱之和就是整个频谱。

:::abbildung et3/k3hann 8
宽度为 $T_0=2$ s 的汉宁窗，依次偏移 $T=1$ s（蓝）。它们的和处处恰好为 1（红）。
:::

:::aufgabe 练习 13 ★ 汉宁窗
<span class="anker" id="aufg-13"></span>

证明当 $T=T_0/2$ 时 $\sum_nw(\tau-nT)=1$。提示：每一点上恰好有两个窗重叠。把第二个窗用 $\cos^2(x-\frac\pi2)$ 表示。

:::loesung
对于 $T=T_0/2$，当 $\tau$ 位于 $nT$ 与 $(n+1)T$ 之间时，恰好只有第 $n$ 个和第 $n+1$ 个窗不为零。令 $x=\pi(\tau-nT)/T_0$：

$$w(\tau-nT)+w(\tau-(n+1)T)=\cos^2x+\cos^2\Bigl(x-\frac\pi2\Bigr)=\cos^2x+\sin^2x=1.$$
:::
:::
