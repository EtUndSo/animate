---
title: 低通与带通系统
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 低通与带通系统
order: 3250100
summary: 无失真传输、理想低通、 复包络与群时延
tags: 相位时延, 群时延, 信号持续时间, 正弦积分, 上升时间, 回波, 升余弦滤波器, 等效低通系统
lang: zh
---

## 本文内容

几乎所有传输都要求信号尽可能不变地到达，但只限于某个频率范围：低通让低频通过，带通让载波频率附近的一个频带通过。本文要回答的问题是：“不变”究竟是什么意思？严格限定的频带要付出什么代价？对于搭载在高频载波上的信号，又该如何计算？

:::merke 三句话的答案（读完本文后应觉得理所当然）
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

**所有结论背后的同一个原理。**

| 结论 | 来源 |
|---|---|
| 无失真系统 | 每个振荡都被同样地放大，并被延迟相同的时间（第 [1](#stufe-1) 阶段） |
| 相位时延与群时延 | 分别是载波和包络的延迟（第 [1](#stufe-1)、[11](#stufe-11) 阶段） |
| 信号持续时间 $\cdot$ 带宽 $=$ 常数 | 尺度变换定理（第 [2](#stufe-2) 阶段） |
| 过冲 21.7 % 与 8.95 % | si 函数的旁瓣，吉布斯现象（第 [2](#stufe-2)、[3](#stufe-3) 阶段） |
| 因果近似、窗函数设计 | 截断冲激响应 $=$ 频谱中的卷积（第 [4](#stufe-4)、[6](#stufe-6) 阶段） |
| 脉冲成形滤波器 | 频谱中平缓的边沿，快速衰减的冲激响应（第 [5](#stufe-5) 阶段） |
| 等效低通系统、复包络 | 把正频率部分搬移到零频处（第 [7](#stufe-7)、[8](#stufe-8) 阶段） |
| 正交电路、带通采样 | 在低通域中计算带通（第 [10](#stufe-10) 阶段） |

**如何使用本文。**每个阶段包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。

:::merke 本文的参考模型
<ul>

<li>

⁠**RC 低通滤波器**，$RC=1$ s，与第 1 至[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)相同。

</li>

<li>

⁠**理想低通**，$f_\mathrm g=1$ Hz（作为比较，也取 2 Hz）。

</li>

<li>

⁠**理想带通**，中心频率 $f_0=10$ Hz，带宽 $\Delta f=2$ Hz。

</li>

<li>

⁠**离散时间低通**，$f_\mathrm g=0.2$（对采样率归一化），21 个系数。

</li>

</ul>

脚本 `rechnung_kap5.py` 可重新计算这些数值和曲线。与[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)相同，抽样函数 $\operatorname{si}(x)=\sin(x)/x$。
:::

## 第 1 阶段：无失真系统

<span class="anker" id="stufe-1"></span>

:::zweck
“好的”传输究竟应该做到什么？又用哪些特征量来衡量一个系统偏离它有多远？
:::

**思路。** 如果信号只是变强或变弱、来得更晚，而形状相同，那么它就是无失真地到达了：

<span class="anker" id="gl-1-1"></span>
$$g(t)=h_0\,s(t-t_0)\qquad\Longleftrightarrow\qquad h(t)=h_0\,\delta(t-t_0),\qquad H(f)=h_0\,\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{1.1}$$

在频谱中，这意味着：每个振荡都乘以同一个因子 $h_0$，并且每个振荡都被平移同一段时间 $t_0$。在频率 $f$ 处，时移 $t_0$ 对应于角度 $2\pi ft_0$。因此相位 $\varphi(f)=-2\pi t_0f$ 必须是一条过原点的直线。

:::definition 定义 1.1 (LTI 系统的特征量)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-2"></span>
<span class="anker" id="gl-1-3"></span>
<span class="anker" id="gl-1-4"></span>
<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} &\text{衰减：} && a(f)=-20\lg|H(f)|\ \text{dB}\quad\text{或}\quad a(f)=-\ln|H(f)|\ \text{Np},\\ &\text{相位衰减角：} && b(f)=-\varphi(f),\\ &\text{相位时延：} && t_\mathrm p(f)=-\frac{\varphi(f)}{2\pi f},\\ &\text{群时延：} && t_\mathrm g(f)=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi(f)}{\mathrm{d} f}. \end{aligned} \tag{1.2|1.3|1.4|1.5}$$
:::

⁠**如何理解：**__相位时延__是频率为 $f$ 的单个振荡的延迟。__群时延__是一组相邻频率的延迟，也就是包络的延迟（第 [11](#stufe-11) 阶段）。对无失真系统，$a$、$t_\mathrm p$ 和 $t_\mathrm g$ 都是常数，且 $t_\mathrm p=t_\mathrm g=t_0$。

**例：RC 电路。** 取 $\varphi=-\arctan(2\pi f\,RC)$ 和 $RC=1$ s：

$$t_\mathrm p=\frac{\arctan(2\pi f\,RC)}{2\pi f},\qquad t_\mathrm g=\frac{RC}{1+(2\pi f\,RC)^2}.$$

当 $f\to0$ 时，二者都等于 $RC=1$ s。在 $f=0.159$ Hz（$2\pi fRC=1$）处，$t_\mathrm p=0.785$ s，$t_\mathrm g=0.5$ s，$a=3.0$ dB。因此 RC 电路不是无失真的：它的衰减与频率有关，不同频率到达的时间也不同。

:::ltspice 读出 RC 电路的衰减和时延
⁠**绘制：**RC 电路（`res` 取 `1Meg`，`cap` 取 `1u`），信号源的值取 `AC 1`，指令为 `.ac dec 100 0.01 10`。

⁠**读数：**左侧坐标轴显示以 dB 表示的 $20\lg|H|=-a$。把鼠标移到右侧坐标轴（相位）上，直到指针变成一把尺子，单击并选择“Group Delay”：这时该坐标轴显示式 [(1.5)](#gl-1-5) 中的 $t_\mathrm g(f)$。相位时延由相位算出，$t_\mathrm p=-\varphi/(2\pi f)$，其中 $\varphi$ 以弧度计。

⁠**你会看到：**频率越低，$t_\mathrm g$ 越接近 1 s。在 0.159 Hz 处读出 $a=3.0$ dB、$\varphi=-45^\circ$ 和 $t_\mathrm g=0.5$ s，由此得 $t_\mathrm p=0.785$ s。把 $2\pi fRC=10$ 处的值与你在练习 [1](#aufg-1)(b) 中的结果比较。
:::

:::aufgabe 练习 1 ★ RC 电路的时延
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

由式 [(1.5)](#gl-1-5) 推导 RC 电路的 $t_\mathrm g$。

</li>

<li>

计算 $2\pi fRC=10$ 时的 $t_\mathrm p$、$t_\mathrm g$ 和 $a$。RC 电路在哪个频率范围内近似无失真？

</li>

</ol>

:::loesung
(a) $\varphi=-\arctan(2\pi fRC)$，$\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-\frac{2\pi RC}{1+(2\pi fRC)^2}$，因此 $t_\mathrm g=-\frac{1}{2\pi}\frac{\mathrm{d}\varphi}{\mathrm{d} f}=\frac{RC}{1+(2\pi fRC)^2}$。

(b) 当 $2\pi fRC=10$ 时：$t_\mathrm p=\frac{\arctan10}{10}RC=0.147$ s，$t_\mathrm g=\frac{RC}{101}=0.0099$ s，$a=20.0$ dB。只有当 $2\pi fRC\ll1$，即频率远低于 0.16 Hz 时，RC 电路才近似无失真：在那里 $|H|\approx1$，且 $t_\mathrm p\approx t_\mathrm g\approx RC$。
:::
:::

## 第 2 阶段：理想低通

<span class="anker" id="stufe-2"></span>

:::zweck
理想低通让所有不超过 $f_\mathrm g$ 的频率不变地通过，并阻断高于 $f_\mathrm g$ 的所有频率。本阶段说明这种陡峭的截止在时域中意味着什么。
:::

:::satz 定理 2.1 (理想低通)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)\qquad\bullet\!\!-\!\!\circ\qquad h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt). \tag{2.1}$$
:::

⁠**如何理解：**冲激响应向两个方向一直延伸到无穷远。因此理想低通*不是因果的*：它必须在冲激到来之前就作出响应。它是一个数学上的极限对象，只能近似实现（第 [4](#stufe-4)、[6](#stufe-6) 阶段）。

**持续时间与带宽。** 把冲激响应的__信号持续时间__ $t_m$ 取为一个矩形的宽度，该矩形与冲激响应具有相同的高度 $h_{\max}$ 和相同的面积：

<span class="anker" id="gl-2-2"></span>
$$t_m=\frac{1}{h_{\max}}\int_{-\infty}^{\infty}h(t)\,\mathrm{d} t=\frac{H(0)}{h_{\max}}. \tag{2.2}$$

对理想低通，$H(0)=1$，$h_{\max}=2f_\mathrm g$，因此 $t_m=\frac{1}{2f_\mathrm g}$，$f_\mathrm g\cdot t_m=\frac12$。一般地，低通滤波器满足 $f_\mathrm g\cdot t_m=\text{常数}$：带宽加倍意味着响应持续时间减半。这就是[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中的尺度变换定理。

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

## 第 3 阶段：阶跃响应与上升时间

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

:::abbildung et3/k5sprung
理想低通在 $f_\mathrm g=1$ Hz 和 2 Hz 时的阶跃响应。虚线：具有最大斜率的斜坡，其上升持续 $t_e=1/(2f_\mathrm g)=0.5$ s。两条曲线的过冲一样大，都达到 1.0895。
:::

:::frage 带宽更大的低通肯定“更好”。那为什么过冲不会变小？
因为过冲来自频率响应的*形状*，而不是它的宽度。过冲产生于 $f_\mathrm g$ 处的竖直边沿：直到该处的所有频率全部通过，高于该处的所有频率完全不通过。如果移动这个边沿，它仍然是竖直的，阶跃响应只是在时间上被压缩。只有当边沿变得平缓时，过冲才会变小（第 [5](#stufe-5) 阶段）。
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

## 第 4 阶段：因果近似

<span class="anker" id="stufe-4"></span>

:::zweck
如何构造一个尽可能接近理想低通的系统？把冲激响应延迟，再把剩余部分截掉。
:::

**思路。** 把 $h(t)$ 向右平移 $t_0$，直到 $t<0$ 的部分可以忽略，然后把这部分截掉。si 函数的包络按 $1/(2\pi f_\mathrm g|t|)$ 衰减。若要求它在 $t=0$ 之前保持在最大值的 1 % 以下，就需要 $t_0\approx16/f_\mathrm g$。采用宽度为 $2t_0$ 的对称窗：

<span class="anker" id="gl-4-1"></span>
$$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)\;\circ\!\!-\!\!\bullet\;H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{4.1}$$

⁠**如何理解：**截断就是乘以一个窗，因而在频谱中就是与窗的 si 频谱作卷积。陡峭的边沿被抹平，并出现波纹。因子 $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ 就是延迟：因果滤波器具有线性相位，它对所有频率的延迟都相同（图 [2](#abb-2)）。$t_0$ 越大，过渡越窄，但响应也越晚。

:::abbildung et3/k5kausal
$f_\mathrm g=1$ Hz、$t_0=3$ s 的因果加窗低通的模（蓝）；虚线：理想情形。边沿处形成一个过渡区，$|H_k(f_\mathrm g)|=0.49$，在它之前有高达 1.10 的波纹。
:::

:::aufgabe 练习 4 ★★ 因果性要付出多少延迟？
<span class="anker" id="aufg-4"></span>

一个 $f_\mathrm g=1$ kHz 的低通要以因果方式近似实现。要求平移后的理想低通响应在 $t=0$ 之前，即在被截掉的部分中，保持在其最大值的 1 % 以下。

<ol class="al">

<li>

$t_0$ 至少要多大？

</li>

<li>

对于经过十个这样的滤波器级联的电话通话，这意味着什么？

</li>

</ol>

:::loesung
(a) 包络条件 $\frac{1}{2\pi f_\mathrm g|t|}<0.01$ 要求 $|t|>\frac{100}{2\pi f_\mathrm g}=15.9$ ms。因此 $t_0\approx16$ ms。

(b) 十个滤波器造成约 0.16 s 的延迟。在通话中，这会被察觉为延迟。陡峭滤波器的因果性要以时间为代价，而且频带越窄，付出的时间越多。
:::
:::

## 第 5 阶段：回波法与脉冲成形滤波器

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

:::abbildung et3/k5pulsform
理想低通和脉冲成形滤波器的冲激响应（面积都为 $T$）。脉冲成形滤波器衰减得快得多：它的最大旁瓣极值是主极大值的 2.7 %，而不是 21.7 %。
:::

**横向滤波器（抽头延迟线）。** 延迟并加权的副本之和，可以用一串延迟单元来实现：对各抽头的信号加权后相加。为了不让任何单元需要用到未来的值，把整体一起延迟。这与 FIR 滤波器（[第 4 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)）的结构相同。

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

(b) $H(0)=2T$，$H(\frac{1}{2T})=T(1+\cos\pi)=0$。斜率 $-2\pi T^2\sin(2\pi Tf)$ 在 $f=\frac{1}{2T}$ 处也为零。频率响应既无跳变、也无折点地趋于零。频谱越光滑，冲激响应衰减得越快（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)）。
:::
:::

## 第 6 阶段：离散时间低通——窗函数设计法

<span class="anker" id="stufe-6"></span>

:::zweck
如何设计数字低通？与因果模拟低通完全一样：取理想低通，加以延迟，再用窗截断。
:::

理想离散时间低通具有周期重复的矩形频率响应，其单位脉冲响应为

$$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn),$$

因此在参考模型中（$f_\mathrm g=0.2$），$h(0)=0.4$，$h(\pm1)=0.303$，$h(\pm2)=0.094$，$h(\pm3)=-0.062$。它同样不是因果的。把它乘以一个有 $2N+1$ 个值的窗 $w(n)$，再平移 $N$，就得到一个具有线性相位的 FIR 滤波器。窗决定了结果（图 [4](#abb-4)）：

<ul>

<li>

⁠**矩形窗：**过渡最陡，但旁瓣高。在参考模型中（$N=10$），从 $f=0.3$ 起的阻带仍高达 $-26.6$ dB，通带波动约 $\pm0.5$ dB。

</li>

<li>

⁠**汉宁窗：**过渡较平缓，但阻带深得多：从 $f=0.3$ 起最高为 $-45.9$ dB，通带平坦度在 $0.05$ dB 以内。

</li>

</ul>

原因与[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中短时傅里叶变换的情形相同：窗的频谱与理想频率响应作卷积，而矩形的硬边沿会产生缓慢衰减的旁瓣。

:::abbildung et3/k5fenster
两个 $f_\mathrm g=0.2$、有 21 个系数的 FIR 低通的幅频响应。矩形窗：边沿陡峭，从 $f=0.3$ 起只衰减到 $-26.6$ dB。汉宁窗：边沿较平缓，从 $f=0.3$ 起最高为 $-45.9$ dB。
:::

:::aufgabe 练习 6 ★ 半带滤波器
<span class="anker" id="aufg-6"></span>

计算 $f_\mathrm g=0.25$ 的理想离散时间低通的系数 $h(0)$ 到 $h(3)$。你注意到了什么？为什么这在 FIR 滤波器中可以节省计算量？

:::loesung
$h(n)=0.5\operatorname{si}(\pi n/2)$：$h(0)=0.5$，$h(\pm1)=\frac1\pi=0.318$，$h(\pm2)=0$，$h(\pm3)=-\frac{1}{3\pi}=-0.106$。除 $h(0)$ 外，所有偶数下标的系数都为零，因为对偶数 $n$ 有 $\sin(\pi n/2)=0$。在 FIR 滤波器中，这些乘法可以省去，几乎占全部乘法的一半。
:::
:::

## 第 7 阶段：理想带通及其等效低通系统

<span class="anker" id="stufe-7"></span>

:::zweck
带通让中心频率 $f_0$ 附近的一个频带通过。本阶段说明，它可以完全由一个低通系统和频率 $f_0$ 来描述。
:::

**理想带通。** 位于 $\pm f_0$ 处、宽度为 $\Delta f$ 的两个矩形（$f_0>\Delta f/2$）：

<span class="anker" id="gl-7-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]\;\bullet\!\!-\!\!\circ\;h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\cdot2\cos(2\pi f_0t). \tag{7.1}$$

冲激响应是频率为 $f_0$ 的振荡，其包络是带宽为 $\Delta f/2$ 的低通的冲激响应。[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)的调制定理解释了这一点：它是一个频谱被搬移到 $\pm f_0$ 处的低通。

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

## 第 8 阶段：复包络与正交分量

<span class="anker" id="stufe-8"></span>

:::zweck
对系统成立的，对信号也成立：带通信号是搭载在载波上的低通信号。本阶段给出写出这一关系的几种不同方式。
:::

用调制定理对式 [(7.2)](#gl-7-2) 作反变换，得到 $h(t)=\frac12h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}+\frac12\bigl[h_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr]^*$，于是由 $z+z^*=2\operatorname{Re} z$ 得：

<span class="anker" id="gl-8-1"></span>
$$h(t)=\operatorname{Re}\bigl\{h_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\},\qquad s(t)=\operatorname{Re}\bigl\{s_T(t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{8.1}$$

$s_T(t)$ 称为__复包络__，$\mathrm{e}^{\mathrm{j}2\pi f_0t}$ 称为__复载波__。二者乘积的一半就是[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中的解析分量 $s_+(t)=\frac12s_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}$，因此 $s_T=2s_+\mathrm{e}^{-\mathrm{j}2\pi f_0t}$。

:::satz 定理 8.1 (正交表示)
<span class="anker" id="satz-8-1"></span>

利用 $s_T=s_{Tr}+\mathrm{j} s_{Ti}$ 和希尔伯特变换 $\hat s=s*\frac{1}{\pi t}$：

<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
$$\begin{aligned} s(t)&=s_{Tr}(t)\cos(2\pi f_0t)-s_{Ti}(t)\sin(2\pi f_0t),\\ s_{Tr}(t)&=s(t)\cos(2\pi f_0t)+\hat s(t)\sin(2\pi f_0t),\qquad s_{Ti}(t)=\hat s(t)\cos(2\pi f_0t)-s(t)\sin(2\pi f_0t),\\ s(t)&=|s_T(t)|\cos\bigl(2\pi f_0t+\varphi_T(t)\bigr),\qquad|s_T|=\sqrt{s_{Tr}^2+s_{Ti}^2}. \end{aligned} \tag{8.2|8.3|8.4}$$
:::

⁠**如何理解：**$s_{Tr}$ 和 $s_{Ti}$ 合称__正交分量__（分别为同相分量和正交分量）：一个调制载波的余弦，另一个调制载波的正弦。$|s_T|$ 是__包络__，即在示波器上看到的信号“轮廓”；$\varphi_T$ 是载波的相位偏移。若复包络为实数（对称情形），则 $s(t)=s_T(t)\cos(2\pi f_0t)$：一个调幅余弦。

:::herleitung 正交分量
式 [(8.2)](#gl-8-2)：$\operatorname{Re}\{(s_{Tr}+\mathrm{j} s_{Ti})(\cos+\mathrm{j}\sin)\}=s_{Tr}\cos-s_{Ti}\sin$。对于式 [(8.3)](#gl-8-3)：$2s_+=s+\mathrm{j}\hat s$（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)），因此

$$s_T=(s+\mathrm{j}\hat s)(\cos-\mathrm{j}\sin)=(s\cos+\hat s\sin)+\mathrm{j}(\hat s\cos-s\sin).$$
:::

:::aufgabe 练习 8 ★★ 求复包络
<span class="anker" id="aufg-8"></span>

相对于 $f_0=10$ Hz，求下列信号的 $s_T$、$s_{Tr}$、$s_{Ti}$ 和 $|s_T|$： (a) $s(t)=\bigl[1+0.5\cos(2\pi\cdot1\,\mathrm{Hz}\cdot t)\bigr]\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t)$， (b) $s(t)=\cos(2\pi\cdot10\,\mathrm{Hz}\cdot t+0.3)$， (c) $s(t)=\sin(2\pi\cdot10\,\mathrm{Hz}\cdot t)$。用式 [(8.2)](#gl-8-2) 验证 (c)。

:::loesung
(a) $s_T=1+0.5\cos(2\pi t)$，为实数：$s_{Tr}=s_T$，$s_{Ti}=0$，$|s_T|=1+0.5\cos(2\pi t)$，在 0.5 与 1.5 之间。这是一个调幅余弦。

(b) $s_T=\mathrm{e}^{\mathrm{j}0.3}$：$s_{Tr}=\cos0.3=0.955$，$s_{Ti}=\sin0.3=0.296$，$|s_T|=1$。包络是恒定的，只是相位移动了 0.3。

(c) $\sin x=\operatorname{Re}\{-\mathrm{j}\,\mathrm{e}^{\mathrm{j} x}\}$，因此 $s_T=-\mathrm{j}$：$s_{Tr}=0$，$s_{Ti}=-1$，$|s_T|=1$。验证：$0\cdot\cos-(-1)\sin=\sin$。
:::
:::

## 第 9 阶段：带通信号通过带通系统

<span class="anker" id="stufe-9"></span>

:::zweck
包络的用处：带通对带通信号的作用，可以完全在低通域中计算。
:::

:::satz 定理 9.1 (在等效低通域中的传输)
<span class="anker" id="satz-9-1"></span>

若 $S_T$ 和 $H_T$ 都满足式 [(7.2)](#gl-7-2)（在 $-f_0$ 以下没有分量），则输出的包络满足

<span class="anker" id="gl-9-1"></span>
$$G_T(f)=\tfrac12S_T(f)\,H_T(f)\qquad\bullet\!\!-\!\!\circ\qquad g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr],\qquad g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{9.1}$$
:::

:::herleitung 传输
用两种表示式 [(7.2)](#gl-7-2) 把 $G=S\cdot H$ 展开，得到四个乘积。混合项，例如 $S_T(f-f_0)H_T^*(-f-f_0)$，为零：第一个因子只存在于正频率，第二个只存在于负频率。剩下的是 $G=\frac14S_T(f-f_0)H_T(f-f_0)+\frac14S_T^*(-f-f_0)H_T^*(-f-f_0)$。将其与 $G=\frac12G_T(f-f_0)+\frac12G_T^*(-f-f_0)$ 比较，得 $G_T=\frac12S_TH_T$。
:::

⁠**如何理解：**因子 $\frac12$ 补偿了 $S_T$ 和 $H_T$ 都被加倍这一事实。除此之外，它就是熟悉的卷积定理，只不过是对包络而言。载波根本不必参与计算。

**例：接通的余弦通过理想带通。** $s(t)=\varepsilon(t)\cos(2\pi f_0t)$，$f_0=10$ Hz，带通以 $f_0$ 为中心，$\Delta f=2$ Hz。输入的包络为 $s_T\approx\varepsilon(t)$。（这是近似：阶跃的频谱并不局限于 $f>-f_0$，但在通带 $|f|\le\Delta f/2\ll f_0$ 内它是正确的。）利用 $h_T=2\Delta f\operatorname{si}(\pi\Delta f\,t)$：

$$g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t),\qquad g(t)\approx\Bigl[\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)\Bigr]\cos(2\pi f_0t).$$

包络就是 $f_\mathrm g=\Delta f/2$ 的理想低通的阶跃响应：上升时间 $1/\Delta f=0.5$ s，过冲 8.95 %（图 [5](#abb-5)）。窄带通需要很长时间才能“稳定下来”。

:::abbildung et3/k5bandpass
理想带通（$f_0=10$ Hz，$\Delta f=2$ Hz）对在 $t=0$ 时接通的中心频率余弦的响应。蓝：输出信号；红：包络 $\pm g_T(t)$。包络在约 0.5 s 内上升，并过冲到 1.09。
:::

:::ltspice 接通的载波通过谐振电路
理想带通无法实现，但串联谐振电路可以实现。**绘制：**电压源 `voltage` 接在节点 `in` 上，然后依次串联 `ind`（取 `{L}`）、`cap`（取 `{1/((2*pi*f0)**2*L)}`）和 `res`（取 `{2*pi*df*L}`）到地。输出 `out` 是电阻两端的电压。取 `.param f0=10 df=2 L=1` 时，中心频率为 10 Hz，两个 $-3$ dB 点之间的带宽为 2 Hz。

⁠**检验：**信号源的值取 `AC 1` 并使用 `.ac lin 2001 5 15`，可以看到 10 Hz 处的最大值 1，以及位于 9.05 Hz 和 11.05 Hz 的 $-3$ dB 点。

⁠**实验：**信号源取 `SINE(0 1 10 0 0 90)`，即 $\varepsilon(t)\cos(2\pi f_0t)$，指令为 `.tran 0 3 0 0.1m`。包络无过冲地上升：载波峰值在 0.2 s 时达到 0.72，0.5 s 时达到 0.96，1 s 后实际上达到 1，几乎恰好与 $1-\mathrm{e}^{-t/0.16\,\mathrm s}$ 一致。相比之下，理想带通会过冲到 1.09（图 [5](#abb-5)）。原因与第 [3](#stufe-3) 阶段中低通的情形相同：谐振电路的边沿是平缓的，而理想带通的边沿是竖直的。
:::

## 第 10 阶段：正交电路与带通采样

<span class="anker" id="stufe-10"></span>

:::zweck
实际中如何得到正交分量？带通信号需要多少个样本值？
:::

**正交电路。** 把带通信号乘以 $\cos(2\pi f_0t)$，再用低通滤波，剩下的就是 $\frac12s_{Tr}$。乘以 $-\sin(2\pi f_0t)$ 时，剩下的是 $\frac12s_{Ti}$。原因在于三角恒等式：

$$s\cos=s_{Tr}\cos^2-s_{Ti}\sin\cos=\tfrac12s_{Tr}+\underbrace{\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)}_{\text{位于}\ 2f_0\ \text{处，被低通滤除}},$$

同理，$-s\sin=\frac12s_{Ti}+(\text{位于}\ 2f_0\ \text{处的分量})$。前提是频带在 $2f_0$ 以下结束。然后在低通域中按照式 [(9.1)](#gl-9-1) 用四个低通滤波器（$h_{Tr}$、$\pm h_{Ti}$）进行滤波。在输出端，按照式 [(8.2)](#gl-8-2) 重新调制到载波上，或者构成包络 $\sqrt{g_{Tr}^2+g_{Ti}^2}$（图 [6](#abb-6)）。

:::abbildung et3/k5quadratur
正交解调器：它从带通信号中提取出两个正交分量，即复包络。
:::

**带通信号的采样定理。** 相对于中心频率，带宽为 $\Delta f$ 的带通信号的正交分量是频率不超过 $\Delta f/2$ 的低通信号。每个分量都可以以 $1/T=\Delta f$ 的速率采样：

<span class="anker" id="gl-10-1"></span>
$$s(t)=\sum_ns_{Tr}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\cos(2\pi f_0t)-\sum_ns_{Ti}(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\sin(2\pi f_0t),\qquad T=\frac{1}{\Delta f}. \tag{10.1}$$

总共每秒需要 $2\Delta f$ 个值，与截止频率为 $\Delta f$ 的低通信号一样多。因此，起决定作用的是带宽，而不是最高频率。

:::aufgabe 练习 9 ★★ 对无线电信号采样
<span class="anker" id="aufg-9"></span>

一个信号占据 10.0 到 10.2 MHz 的频带。

<ol class="al">

<li>

按照普通的采样定理，需要多高的采样率？

</li>

<li>

使用正交电路时，每秒总共有多少个样本值就够了？每个支路以多高的速率采样？

</li>

</ol>

:::loesung
(a) 至少 $2\cdot10.2=20.4$ MHz。

(b) $\Delta f=0.2$ MHz。每个支路以 0.2 MHz 采样（$T=5$ µ s），合计 0.4 MHz，约为前者的五十分之一。
:::
:::

## 第 11 阶段：带通中的相位时延与群时延

<span class="anker" id="stufe-11"></span>

:::zweck
为什么有两种时延？因为载波和包络可以被延迟不同的时间。
:::

**思路。** 设一个带通在通带内模恒定，相位略有弯曲。在 $f_0$ 附近，用相位的切线来近似它：

$$\varphi(f)\approx\varphi(f_0)+(f-f_0)\frac{\mathrm{d}\varphi}{\mathrm{d} f}\Big|_{f_0}=-2\pi f_0t_\mathrm p-2\pi(f-f_0)t_\mathrm g,$$

其中 $t_\mathrm p=t_\mathrm p(f_0)$，$t_\mathrm g=t_\mathrm g(f_0)$，由式 [(1.4)](#gl-1-4) 和式 [(1.5)](#gl-1-5) 给出。在低通域中（$f-f_0\to f$），这就是 $H_T(f)=2\operatorname{rect}(f/\Delta f)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p}\,\mathrm{e}^{-\mathrm{j}2\pi ft_\mathrm g}$：一个恒定相位加上一个延迟。

:::satz 定理 11.1 (带通中的时延)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$g_T(t)=s_T(t-t_\mathrm g)\,\mathrm{e}^{-\mathrm{j}2\pi f_0t_\mathrm p},\qquad g(t)=\operatorname{Re}\bigl\{s_T(t-t_\mathrm g)\,\mathrm{e}^{\mathrm{j}2\pi f_0(t-t_\mathrm p)}\bigr\}. \tag{11.1}$$
:::

⁠**如何理解：**携带信息的包络被延迟一个*群时延*。载波被延迟一个*相位时延*。只有当二者相等时，传输才是严格意义上无失真的，也就是说，相位直线通过原点（或在 $f=0$ 处通过 $2\pi$ 的整数倍）。对信息而言，通常只要群时延恒定就够了：若 $t_\mathrm g$ 不恒定，包络的不同频率分量到达的时间不同，脉冲就会展宽（__时延失真__）。

:::ltspice 包络和载波在不同时刻到达
⁠**绘制：**第 [9](#stufe-9) 阶段 LTspice 提示中的谐振电路（$f_0=10$ Hz，$\Delta f=2$ Hz）。在 `.ac` 分析中，它在 10 Hz 处的相位为 $0^\circ$，因此 $t_\mathrm p(f_0)=0$。如果把相位坐标轴切换为“Group Delay”，它在 10 Hz 处显示 $t_\mathrm g(f_0)=0.16$ s。

⁠**实验：**输入用行为源 `bv`，即一个包络缓慢变化的载波：

`V=(1+0.5*cos(2*pi*0.2*time))*cos(2*pi*10*time)`

指令 `.tran 0 20 0 0.2m` 和 `.options plotwinsize=0`。

⁠**你会看到：**把 `V(in)` 和 `V(out)` 叠画在一起，并缩放到 14.5 s 至 15.5 s。包络的最大值在输出端晚到约 0.16 s，但载波的过零点与输入端位于相同的位置。这正是式 [(11.1)](#gl-11-1) 所说的：包络被延迟 $t_\mathrm g$，载波被延迟 $t_\mathrm p$。
:::

:::aufgabe 练习 10 ★★ 读出时延
<span class="anker" id="aufg-10"></span>

一个带通在 $f_0=1$ MHz 处的相位为 $\varphi(f_0)=-\pi/2$，斜率为 $\frac{\mathrm{d}\varphi}{\mathrm{d} f}=-2\pi\cdot2\,\mu\text{s}$。

<ol class="al">

<li>

计算 $t_\mathrm p$ 和 $t_\mathrm g$。

</li>

<li>

输出端脉冲的包络被延迟了多少？之后载波相对于包络是否仍处于同一位置？

</li>

</ol>

:::loesung
(a) $t_\mathrm p=-\frac{\varphi(f_0)}{2\pi f_0}=\frac{\pi/2}{2\pi\cdot10^6\,\mathrm{Hz}}=0.25$ µ s。$t_\mathrm g=2$ µ s。

(b) 包络晚 2 µ s 到达。载波只移动了 0.25 µ s。因此，它相对于包络转过了 $2\pi f_0(t_\mathrm g-t_\mathrm p)=3.5\pi$，对 $2\pi$ 取模为 $1.5\pi$，即 $-\pi/2$：四分之一周期。只要 $t_\mathrm g$ 在整个频带内恒定，包络中的信息就保持无失真。
:::
:::

## 第 12 阶段：离散时间带通与高通

<span class="anker" id="stufe-12"></span>

:::zweck
数字带通和数字高通可以通过调制由低通得到。
:::

若离散时间低通的单位脉冲响应为实数，乘以 $2\cos(2\pi f_0n)$ 就会把它的通带搬移到 $\pm f_0$：

<span class="anker" id="gl-12-1"></span>
$$H_{\mathrm{BP}}(f)=H_{\mathrm{TP}}(f)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr],\qquad h_{\mathrm{BP}}(n)=2\cos(2\pi f_0n)\,h_{\mathrm{TP}}(n), \tag{12.1}$$

只要搬移后的各频带不重叠，该式就成立：$f_{\mathrm g,\mathrm{TP}}\le f_0\le\frac12-f_{\mathrm g,\mathrm{TP}}$。由于周期性，位于 $f_0$ 处的频带既不能接触位于 $-f_0$ 处的频带，也不能接触它在 $1-f_0$ 处的副本。一般地，对于复的低通单位脉冲响应也一样，与式 [(8.1)](#gl-8-1) 相同，有 $h_{\mathrm{BP}}(n)=2\operatorname{Re}\{h_{\mathrm{TP}}(n)\mathrm{e}^{\mathrm{j}2\pi f_0n}\}$。因子 2 对应于加倍的等效低通系统 $H_T=2H_{\mathrm{TP}}$。

__高通__是被搬移到采样率一半处（$f_0=\frac12$）的低通。在那里，频带与其镜像重合，因此只搬移一次：$H_{\mathrm{HP}}(f)=H_{\mathrm{TP}}(f-\frac12)$。利用 $\mathrm{e}^{\mathrm{j}\pi n}=(-1)^n$：

<span class="anker" id="gl-12-2"></span>
$$h_{\mathrm{HP}}(n)=(-1)^n\,h_{\mathrm{TP}}(n). \tag{12.2}$$

⁠**简而言之：**把低通单位脉冲响应每隔一个值改变一次符号，就得到数字高通。

:::aufgabe 练习 11 ★ 由滑动平均得到高通
<span class="anker" id="aufg-11"></span>

滑动平均 $h_{\mathrm{TP}}=\frac13(1,1,1)$（[第 4 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)）是一个简单的低通。

<ol class="al">

<li>

按照式 [(12.2)](#gl-12-2) 构造 $h_{\mathrm{HP}}$。

</li>

<li>

计算 $f=0$ 和 $f=\frac12$ 处的 $H_{\mathrm{TP}}$ 和 $H_{\mathrm{HP}}$。这与高通相符吗？

</li>

</ol>

:::loesung
(a) $h_{\mathrm{HP}}=\frac13(1,-1,1)$。

(b) $H_{\mathrm{TP}}(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}[1+2\cos(2\pi f)]$：$|H_{\mathrm{TP}}(0)|=1$，$|H_{\mathrm{TP}}(\frac12)|=\frac13$。高通被搬移了 $\frac12$：$|H_{\mathrm{HP}}(0)|=\frac13$，$|H_{\mathrm{HP}}(\frac12)|=1$。它让变化最快的序列 $(+1,-1,+1,\dots)$ 完全通过，并把直流分量衰减到三分之一。这是一个简单的高通，但不是很陡。
:::
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
