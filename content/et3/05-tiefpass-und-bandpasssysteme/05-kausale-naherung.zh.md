---
title: 第 4 阶段：因果近似
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 低通与带通系统
order: 3250500
summary: 如何构造一个尽可能接近理想低通的系统？把冲激响应延迟，再把剩余部分截掉。
tags: 
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
如何构造一个尽可能接近理想低通的系统？把冲激响应延迟，再把剩余部分截掉。
:::

**思路。** 把 $h(t)$ 向右平移 $t_0$，直到 $t<0$ 的部分可以忽略，然后把这部分截掉。si 函数的包络按 $1/(2\pi f_\mathrm g|t|)$ 衰减。若要求它在 $t=0$ 之前保持在最大值的 1 % 以下，就需要 $t_0\approx16/f_\mathrm g$。采用宽度为 $2t_0$ 的对称窗：

<span class="anker" id="gl-4-1"></span>
$$h_k(t)=2f_\mathrm g\operatorname{si}\bigl(2\pi f_\mathrm g(t-t_0)\bigr)\operatorname{rect}\Bigl(\frac{t-t_0}{2t_0}\Bigr)\;\circ\!\!-\!\!\bullet\;H_k(f)=\Bigl[\operatorname{rect}\Bigl(\frac{f}{2f_\mathrm g}\Bigr)*2t_0\operatorname{si}(2\pi t_0f)\Bigr]\mathrm{e}^{-\mathrm{j}2\pi t_0f}. \tag{4.1}$$

⁠**如何理解：**截断就是乘以一个窗，因而在频谱中就是与窗的 si 频谱作卷积。陡峭的边沿被抹平，并出现波纹。因子 $\mathrm{e}^{-\mathrm{j}2\pi t_0f}$ 就是延迟：因果滤波器具有线性相位，它对所有频率的延迟都相同（图 [2](#abb-2)）。$t_0$ 越大，过渡越窄，但响应也越晚。

:::abbildung et3/k5kausal 2
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
