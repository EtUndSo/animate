---
title: 第 10 阶段：正交电路与带通采样
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 低通与带通系统
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: 第 5 章：低通与带通系统
order: 3251100
summary: 实际中如何得到正交分量？带通信号需要多少个样本值？
tags: 
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
实际中如何得到正交分量？带通信号需要多少个样本值？
:::

**正交电路。** 把带通信号乘以 $\cos(2\pi f_0t)$，再用低通滤波，剩下的就是 $\frac12s_{Tr}$。乘以 $-\sin(2\pi f_0t)$ 时，剩下的是 $\frac12s_{Ti}$。原因在于三角恒等式：

$$s\cos=s_{Tr}\cos^2-s_{Ti}\sin\cos=\tfrac12s_{Tr}+\underbrace{\tfrac12s_{Tr}\cos(4\pi f_0t)-\tfrac12s_{Ti}\sin(4\pi f_0t)}_{\text{位于}\ 2f_0\ \text{处，被低通滤除}},$$

同理，$-s\sin=\frac12s_{Ti}+(\text{位于}\ 2f_0\ \text{处的分量})$。前提是频带在 $2f_0$ 以下结束。然后在低通域中按照式 [(9.1)](bandpasssignal-durch-bandpasssystem.html#gl-9-1) 用四个低通滤波器（$h_{Tr}$、$\pm h_{Ti}$）进行滤波。在输出端，按照式 [(8.2)](komplexe-hullkurve-und-quadraturkomponenten.html#gl-8-2) 重新调制到载波上，或者构成包络 $\sqrt{g_{Tr}^2+g_{Ti}^2}$（图 [6](#abb-6)）。

:::abbildung et3/k5quadratur 6
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
