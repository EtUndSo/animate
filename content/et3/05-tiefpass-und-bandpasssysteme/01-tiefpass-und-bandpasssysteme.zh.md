---
title: 概览: 低通与带通系统
kurz: 概览
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 低通与带通系统
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: 第 5 章：低通与带通系统
order: 3250100
summary: 无失真传输、理想低通、 复包络与群时延
tags: 
lang: zh
---

## 本章内容

几乎所有传输都要求信号尽可能不变地到达，但只限于某个频率范围：低通让低频通过，带通让载波频率附近的一个频带通过。本章要回答的问题是：“不变”究竟是什么意思？严格限定的频带要付出什么代价？对于搭载在高频载波上的信号，又该如何计算？

**所有结论背后的同一个原理。**

| 结论 | 来源 |
|---|---|
| 无失真系统 | 每个振荡都被同样地放大，并被延迟相同的时间（第 [1](das-verzerrungsfreie-system.html#stufe-1) 阶段） |
| 相位时延与群时延 | 分别是载波和包络的延迟（第 [1](das-verzerrungsfreie-system.html#stufe-1)、[11](phasen-und-gruppenlaufzeit-beim-bandpass.html#stufe-11) 阶段） |
| 信号持续时间 $\cdot$ 带宽 $=$ 常数 | 尺度变换定理（第 [2](der-ideale-tiefpass.html#stufe-2) 阶段） |
| 过冲 21.7 % 与 8.95 % | si 函数的旁瓣，吉布斯现象（第 [2](der-ideale-tiefpass.html#stufe-2)、[3](sprungantwort-und-einschwingzeit.html#stufe-3) 阶段） |
| 因果近似、窗函数设计 | 截断冲激响应 $=$ 频谱中的卷积（第 [4](kausale-naherung.html#stufe-4)、[6](zeitdiskrete-tiefpasse-entwurf-mit-fenstern.html#stufe-6) 阶段） |
| 脉冲成形滤波器 | 频谱中平缓的边沿，快速衰减的冲激响应（第 [5](echomethode-und-pulsformfilter.html#stufe-5) 阶段） |
| 等效低通系统、复包络 | 把正频率部分搬移到零频处（第 [7](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#stufe-7)、[8](komplexe-hullkurve-und-quadraturkomponenten.html#stufe-8) 阶段） |
| 正交电路、带通采样 | 在低通域中计算带通（第 [10](quadraturschaltung-und-bandpass-abtastung.html#stufe-10) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**RC 低通滤波器**，$RC=1$ s，与第 1 至[第 3 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)相同。

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

与[第 3 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)相同，抽样函数 $\operatorname{si}(x)=\sin(x)/x$。
:::
