---
title: 第 7 阶段：理想带通及其等效低通系统
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 低通与带通系统
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: 第 5 章：低通与带通系统
order: 3250800
summary: 带通让中心频率 f 0 附近的一个频带通过。本阶段说明，它可以完全由一个低通系统和频率 f 0 来描述。
tags: 等效低通系统, 对称
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
带通让中心频率 $f_0$ 附近的一个频带通过。本阶段说明，它可以完全由一个低通系统和频率 $f_0$ 来描述。
:::

**理想带通。** 位于 $\pm f_0$ 处、宽度为 $\Delta f$ 的两个矩形（$f_0>\Delta f/2$）：

<span class="anker" id="gl-7-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]\;\bullet\!\!-\!\!\circ\;h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\cdot2\cos(2\pi f_0t). \tag{7.1}$$

冲激响应是频率为 $f_0$ 的振荡，其包络是带宽为 $\Delta f/2$ 的低通的冲激响应。[第 3 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)的调制定理解释了这一点：它是一个频谱被搬移到 $\pm f_0$ 处的低通。

**等效低通系统。** 对实冲激响应有 $H(-f)=H^*(f)$，负频率的一半不包含任何新信息。只保留正频率，将其加倍，并向左平移一个载波频率 $f_0$。结果就是__等效低通系统__ $H_T(f)$：

<span class="anker" id="gl-7-2"></span>
$$H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0),\qquad \text{当}\ f\le-f_0\ \text{时}\ H_T(f)=0. \tag{7.2}$$

$H_T$ 不必关于 $f=0$ 对称，因此它的冲激响应 $h_T(t)$ 可以是复的。若存在某个 $f_0$，使 $H_T(-f)=H_T^*(f)$ 成立（从而 $h_T$ 为实），则称该带通是__对称__的。对于 $f_0$ 位于中心的理想带通，$H_T(f)=2\operatorname{rect}(f/\Delta f)$，$h_T(t)=2\Delta f\operatorname{si}(\pi\Delta f\,t)$，是实的偶函数。这是一个特例：即使是对称带通，其频谱通常也含有虚部。

:::aufgabe 练习 7 ★★ 以不同参考频率表示的等效低通系统
<span class="anker" id="aufg-7"></span>

9 到 11 Hz 的理想带通。

<ol class="al">

<li>

对 $f_0=10$ Hz 求 $H_T$ 和 $h_T$。

</li>

<li>

对 $f_0=9$ Hz 求 $H_T$ 和 $h_T$。为什么现在 $h_T$ 是复的？二者描述的是同一个带通吗？

</li>

</ol>

:::loesung
(a) $f_0=10$ Hz：平移后，频带对称地位于 $-1$ 到 $1$ Hz 之间。$H_T=2\operatorname{rect}(f/2)$，$h_T=4\operatorname{si}(2\pi t)$，为实数。

(b) $f_0=9$ Hz：频带位于 0 到 2 Hz 之间。$H_T=2\operatorname{rect}\bigl(\frac{f-1}{2}\bigr)$，$h_T=4\operatorname{si}(2\pi t)\,\mathrm{e}^{\mathrm{j}2\pi t}$。它是复的，因为 $H_T$ 不关于 $f=0$ 对称。二者描述的是同一个带通：$\operatorname{Re}\{4\operatorname{si}(2\pi t)\mathrm{e}^{\mathrm{j}2\pi t}\mathrm{e}^{\mathrm{j}2\pi9t}\}=4\operatorname{si}(2\pi t)\cos(2\pi\cdot10t)$，与 (a) 及式 [(7.1)](#gl-7-1) 相同。
:::
:::
