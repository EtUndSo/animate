---
title: 第 3 阶段：采样定理与信号恢复
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 采样与离散时间系统
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: 第 4 章：采样与离散时间系统
order: 3240400
summary: 什么时候能由样本值精确地恢复原信号？怎样恢复？
tags: 低通（带限）信号, 奈奎斯特率, 混叠频率, 抗混叠滤波器
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
什么时候能由样本值精确地恢复原信号？怎样恢复？
:::

:::satz 定理 3.1 (采样定理)
<span class="anker" id="satz-3-1"></span>

一个频谱在 $f_\mathrm g$ 以上为零的信号（__低通（带限）信号__）由其样本值 $s(nT)$ 唯一确定，条件是

<span class="anker" id="gl-3-1"></span>
$$T\le\frac{1}{2f_\mathrm g}\qquad\text{即}\qquad f_\mathrm A=\frac1T\ge2f_\mathrm g. \tag{3.1}$$

利用理想低通滤波器 $H_\mathrm{TP}(f)=T\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$，有

<span class="anker" id="gl-3-2"></span>
$$s(t)=s_\mathrm a(t)*\bigl[2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)\bigr], \tag{3.2}$$

当 $T=1/(2f_\mathrm g)$ 时：

<span class="anker" id="gl-3-3"></span>
$$s(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr). \tag{3.3}$$
:::

⁠**如何理解：**当 $f_\mathrm A\ge2f_\mathrm g$ 时，图 [1](das-spektrum-des-abgetasteten-signals.html#abb-1) 中的各副本相互分开。低通滤波器截取出位于 $f=0$ 处的副本，它恰好具有原频谱的形状。在时域中，这意味着：每个样本值都被一个 si 函数代替，该函数在它自己的采样点处为 1，在其他所有采样点处为零（图 [2](#abb-2)）。这些函数之和经过所有样本值，并以不产生任何高于 $f_\mathrm g$ 的频率的方式填补其间的空隙。最低采样率 $2f_\mathrm g$ 称为__奈奎斯特率__。

:::herleitung 信号恢复
在 $|f|\le f_\mathrm g$ 内只有副本 $k=0$，因此 $S_\mathrm a(f)=\frac1TS(f)$。取 $H_\mathrm{TP}=T\operatorname{rect}(f/2f_\mathrm g)$，则 $S_\mathrm a\cdot H_\mathrm{TP}=S$。在时域中：$T\operatorname{rect}(f/2f_\mathrm g)\;\bullet\!\!-\!\!\circ\;2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)$（[第 3 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)，矩形与 si 函数）。利用式 [(1.2)](signalklassen-und-ideale-abtastung.html#gl-1-2) 和 $2f_\mathrm g=1/T$，得到 $s_\mathrm a*\operatorname{si}(\pi t/T)=\sum_ns(nT)\operatorname{si}(\pi(t-nT)/T)$。
:::

:::abbildung et3/k4siinterp 2
si 内插：样本值 $0,\ 1,\ 0.6,\ -0.4,\ 0.8,\ 0$（红色）、加权后的 si 函数（灰色）及其和（蓝色）。每个 si 函数在其他采样点处都为零，因此其和精确地经过所有样本值。
:::

**混叠。** 如果采样太慢，各副本就会重叠。高于 $f_\mathrm A/2$ 的频率在恢复后表现为一个错误的、较低的频率，即它的__混叠频率__。在参考模型中，当 $f_\mathrm A=1$ kHz 时，700 Hz 的余弦与 300 Hz 的余弦具有完全相同的样本值，因为 $\cos(2\pi\cdot0.7n)=\cos(2\pi n-2\pi\cdot0.3n)=\cos(2\pi\cdot0.3n)$（图 [3](#abb-3)）。事后已无法再将二者分开。因此，在每个采样器之前都要用低通滤波器对信号进行滤波（__抗混叠滤波器__）。

:::abbildung et3/k4alias 3
当 $f_\mathrm A=1$ kHz 时，700 Hz 与 300 Hz 的样本值（黑色）重合。700 Hz 高于 $f_\mathrm A/2=500$ Hz，表现为 300 Hz 处的混叠频率。
:::

:::frage 恰好取 $f_\mathrm A=2f_\mathrm g$ 难道不够吗？对于频率恰为 $f_\mathrm g$ 的正弦，这样做明明会出错。
对，恰好在边界上会出错：在相位不利的情况下，频率为 $f_\mathrm g=f_\mathrm A/2$ 的正弦可能每次都恰好在过零点处被采样，于是所有样本值都为零。因此，严格地说，该定理要求频谱*在* $f_\mathrm g$ 处没有谱线，或者 $f_\mathrm A>2f_\mathrm g$。实际上人们本来就会采样得更快，因为实际的低通滤波器并不是垂直下降的，需要为其过渡带留出空间。
:::

:::ltspice 采样保持：看见混叠
⁠**绘制：**电压源 `voltage` 接在节点 `in` 上，取 `SINE(0 1 700 0 0 90)`，即 700 Hz 的余弦。开关 `sw`（值为 `SW1`）从 `in` 接到 `sh`，在 `sh` 处接一个 `cap`，取 `100n`，接地。第二个信号源取 `PULSE(0 1 0 10n 10n 1u 1m)`，驱动开关的控制输入：开关每毫秒闭合 1 µ s（$f_\mathrm A=1$ kHz），其间电容保持样本值。`sh` 之后接一个输出为 `out` 的 `e` 源，作为恢复信号用的低通。它是一个截止频率为 400 Hz 的 4 阶巴特沃斯低通（通带尽可能平坦），其值为

`Laplace=1/(((s/wg)**2+0.7654*s/wg+1)*((s/wg)**2+1.8478*s/wg+1))`

⁠**指令：**`.model SW1 SW(Ron=1 Roff=1G Vt=0.5)`，`.param wg=2*pi*400`，`.tran 0 40m 0 1u`，`.options plotwinsize=0`，`.four 100 15 V(sh) V(out)`。

⁠**你会看到：**`sh` 处的阶梯波跟随一个 300 Hz 的振荡，而 `out` 处出现的是 300 Hz 而不是 700 Hz 的余弦。在 `.four` 的结果中，300 Hz 处的谱线最强。改用 `SINE(0 1 300 0 0 90)` 时，出现同样的阶梯波。设为 1.2 kHz，并与你在练习 [1](#aufg-1)(a) 中的结果比较。

⁠**抗混叠：**在开关前面再放一个相同的 `e` 源。输入为 700 Hz 时，`out` 处 300 Hz 的谱线降到约十分之一，而 300 Hz 的输入几乎不受衰减地通过。因此，必须在采样之前防止混叠：采样之后，它就再也无法与真正的 300 Hz 信号区分开了。
:::

:::aufgabe 练习 1 ★ 混叠频率
<span class="anker" id="aufg-1"></span>

$f_\mathrm A=1$ kHz。

<ol class="al">

<li>

1.2 kHz 的余弦在恢复后表现为什么频率？

</li>

<li>

哪些频率与 50 Hz 的余弦给出相同的样本值？

</li>

</ol>

:::loesung
(a) 1.2 kHz 高于 $f_\mathrm A/2$。它与 $1.2-1=0.2$ kHz 具有相同的样本值，表现为 200 Hz。

(b) 所有 $\pm50\,\mathrm{Hz}+k\cdot1\,\mathrm{kHz}$：950 Hz、1050 Hz、1950 Hz、2050 Hz，依此类推。对余弦而言，负频率与正频率是等价的，因此 $1000-50$ 也属于其中。
:::
:::

:::aufgabe 练习 2 ★★ 实际中的采样率
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

电话语音被限制在 3.4 kHz 以内，并以 8 kHz 采样。奈奎斯特率是多少？留出的余量有什么用？

</li>

<li>

音频 CD 以 44.1 kHz 采样。它最高能存储多高频率的声音？若可听频带延伸到 20 kHz，留给抗混叠滤波器的过渡带有多宽？

</li>

</ol>

:::loesung
(a) 奈奎斯特率为 $2\cdot3.4=6.8$ kHz。采样率为 8 kHz 时，$f_\mathrm A/2$ 位于 4 kHz。在 3.4 kHz 与 4 kHz 之间，抗混叠滤波器有空间从通带过渡到阻带。

(b) 最高到 $f_\mathrm A/2=22.05$ kHz。从 20 kHz 到 22.05 kHz 的过渡带只有 2.05 kHz 宽。因此需要陡峭的滤波器或过采样。
:::
:::

:::aufgabe 练习 3 ★★ 手算 si 内插
<span class="anker" id="aufg-3"></span>

用式 [(3.3)](#gl-3-3) 计算图 [2](#abb-2) 中信号在 $t=2.5T$ 处的值。提示：$\operatorname{si}(\pi\cdot0.5)=2/\pi$，$\operatorname{si}(\pi\cdot1.5)=-2/(3\pi)$。哪些样本值没有贡献？

:::loesung
在 $t=2.5T$ 处，$\operatorname{si}(\pi(2.5-k))$ 在 $k\in\{2,3\}$ 时等于 $\frac2\pi$，在 $k\in\{1,4\}$ 时等于 $-\frac{2}{3\pi}$。$k=0$ 和 $k=5$ 处的样本值为零，没有贡献：

$$s(2.5T)=\frac2\pi\Bigl[-\tfrac13\cdot1+0.6-0.4-\tfrac13\cdot0.8\Bigr]=\frac2\pi\cdot(-0.4)=-0.255.$$
:::
:::
