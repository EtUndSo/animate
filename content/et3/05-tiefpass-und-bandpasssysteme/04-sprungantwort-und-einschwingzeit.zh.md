---
title: 第 3 阶段：阶跃响应与上升时间
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 低通与带通系统
order: 3250400
summary: 理想低通对阶跃如何响应？它上升得有多快，过冲有多大？
tags: 正弦积分, 上升时间
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
理想低通对阶跃如何响应？它上升得有多快，过冲有多大？
:::

阶跃响应是冲激响应的变上限积分（[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)）。利用__正弦积分__

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Si}(x)=\int_0^x\operatorname{si}(\xi)\,\mathrm{d}\xi,\qquad\operatorname{Si}(-x)=-\operatorname{Si}(x),\qquad\operatorname{Si}(\infty)=\frac\pi2 \tag{3.1}$$

得到

<span class="anker" id="gl-3-2"></span>
$$h_\varepsilon(t)=\int_{-\infty}^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\,\mathrm{d}\tau=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt). \tag{3.2}$$

:::herleitung 阶跃响应
把到 $t$ 为止的积分在 0 处分开。从 $-\infty$ 到 0 的部分是 $h$ 的面积的一半，即 $\frac12H(0)=\frac12$，因为 $h$ 是偶函数。对其余部分作代换 $\xi=2\pi f_\mathrm g\tau$，$\mathrm{d}\tau=\mathrm{d}\xi/(2\pi f_\mathrm g)$：$\int_0^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\mathrm{d}\tau=\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$。$\operatorname{Si}(\infty)=\frac\pi2$ 这个值由面积定理得到：$\int_{-\infty}^\infty\operatorname{si}(\pi u)\mathrm{d} u=1$，因此 $\int_0^\infty\operatorname{si}(\xi)\mathrm{d}\xi=\frac\pi2$。
:::

⁠**如何理解：**在 $t=0$ 时，响应恰好为 $\frac12$；它甚至在此之前就已开始（非因果），并趋于 1。__上升时间__ $t_e$ 定义为一条斜坡的上升持续时间，该斜坡的斜率等于阶跃响应的最大斜率。最大斜率为 $h(0)=2f_\mathrm g$，因此

<span class="anker" id="gl-3-3"></span>
$$t_e=\frac{h_\varepsilon(\infty)}{\max\dot h_\varepsilon}=\frac{1}{2f_\mathrm g}. \tag{3.3}$$

阶跃响应的过冲为 $8.95\,\%$（在 $t=\frac{1}{2f_\mathrm g}$ 处）。这就是[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中的吉布斯现象：更大的 $f_\mathrm g$ 会缩短上升时间，但过冲保持不变（图 [1](#abb-1)）。

:::abbildung et3/k5sprung 1
理想低通在 $f_\mathrm g=1$ Hz 和 2 Hz 时的阶跃响应。虚线：具有最大斜率的斜坡，其上升持续 $t_e=1/(2f_\mathrm g)=0.5$ s。两条曲线的过冲一样大，都达到 1.0895。
:::

:::frage 带宽更大的低通肯定“更好”。那为什么过冲不会变小？
因为过冲来自频率响应的*形状*，而不是它的宽度。过冲产生于 $f_\mathrm g$ 处的竖直边沿：直到该处的所有频率全部通过，高于该处的所有频率完全不通过。如果移动这个边沿，它仍然是竖直的，阶跃响应只是在时间上被压缩。只有当边沿变得平缓时，过冲才会变小（第 [5](echomethode-und-pulsformfilter.html#stufe-5) 阶段）。
:::

:::aufgabe 练习 3 ★★ 正弦积分
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

利用式 [(3.1)](#gl-3-1) 证明 $h_\varepsilon(0)=\frac12$ 和 $h_\varepsilon(\infty)=1$。

</li>

<li>

阶跃响应的最大值在哪里？提示：阶跃响应的导数就是冲激响应。

</li>

</ol>

:::loesung
(a) $h_\varepsilon(0)=\frac12+\frac1\pi\operatorname{Si}(0)=\frac12$，$h_\varepsilon(\infty)=\frac12+\frac1\pi\cdot\frac\pi2=1$。

(b) 阶跃响应的斜率为 $h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$。它在 $2\pi f_\mathrm gt=\pi$ 处第一次变为零，并在该处由正变负。因此最大值位于 $t=\frac{1}{2f_\mathrm g}$，其值为 $\frac12+\frac{\operatorname{Si}(\pi)}{\pi}=\frac12+\frac{1.852}{\pi}=1.0895$。
:::
:::
