---
title: 概览: 傅里叶级数与傅里叶变换
kurz: 概览
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 傅里叶级数与变换
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: 第 3 章：傅里叶级数与变换
order: 3230100
summary: 每个信号都是振荡的叠加
tags: 频谱
lang: zh
---

## 本章内容

[第 2 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)表明，每个信号都是基本单元 $\mathrm{e}^{pt}$ 的叠加，而 LTI 系统只是把每个基本单元乘以一个数。傅里叶描述只使用虚轴上的基本单元 $p=\mathrm{j}2\pi f$：既不增长也不衰减的纯振荡 $\mathrm{e}^{\mathrm{j}2\pi ft}$。这有一个很大的优点：振荡具有频率，而频率可以听到、测量和滤波。__频谱__ $S(f)$ 表明信号中各个频率分别以怎样的幅度和相位存在。

**所有结论背后的同一个原理。**

| 结论 | 来源 |
|---|---|
| 频率响应 $H(f)$ | 振荡 $\mathrm{e}^{\mathrm{j}2\pi ft}$ 的特征值（第 [1](schwingungen-als-eigenfunktionen.html#stufe-1) 阶段） |
| 傅里叶级数，只含 $F$ 的整数倍 | 只有这些振荡具有周期 $T$（第 [2](periodische-signale-die-fourier-reihe.html#stufe-2) 阶段） |
| 级数的分析公式 | 不同频率的振荡相互正交（第 [2](periodische-signale-die-fourier-reihe.html#stufe-2) 阶段） |
| 帕塞瓦尔定理、吉布斯现象、周期输入下的 LTI 系统 | 每个谐波单独考虑（第 [3](leistung-konvergenz-und-lti-systeme.html#stufe-3) 阶段） |
| 傅里叶积分 | 周期 $\to\infty$，谱线相互靠拢（第 [4](vom-periodischen-zum-einmaligen-signal.html#stufe-4) 阶段） |
| 实信号的 $S(-f)=S^*(f)$ | 振荡以共轭对的形式出现（第 [5](symmetrien-im-signal-und-im-spektrum.html#stufe-5) 阶段） |
| 时移、展缩、微分、调制 | 该运算对 $\mathrm{e}^{\mathrm{j}2\pi ft}$ 的作用（第 [6](die-rechenregeln-theoreme.html#stufe-6) 阶段） |
| 对偶性 | 正变换与逆变换只差一个符号（第 [6](die-rechenregeln-theoreme.html#stufe-6) 阶段） |
| 线谱、狄拉克梳状函数、阶跃 | 含狄拉克冲激的极限情况（第 [8](singulare-signale-und-linienspektren.html#stufe-8) 阶段） |
| 希尔伯特变换 | 因果信号由一半即可确定（第 [9](hilbert-transformation-und-analytisches-signal.html#stufe-9) 阶段） |
| 短时傅里叶变换 | 一个片段的频谱（第 [10](kurzzeit-fourier-transformation.html#stufe-10) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**方波**：在 0 与 1 之间变化，周期 $T=2\pi$ s，占空比为 $\frac12$：$|t|\le T/4$ 时为 1，$T/4<|t|\le T/2$ 时为 0，并作周期延拓。基频 $F=1/T=0.159$ Hz，因此 $2\pi F=1/\mathrm s$。

</li>

<li>

⁠**RC 低通滤波器**，$RC=1$ s，$H(f)=1/(1+\mathrm{j}2\pi f\,RC)$。在方波的第 $k$ 次谐波（频率为 $kF$ 的分量）处，$2\pi kF\cdot RC=k$，因此 $H(kF)=1/(1+\mathrm{j} k)$。

</li>

<li>

⁠**矩形脉冲** $\operatorname{rect}(t)$ 与 $\operatorname{si}(x)=\sin(x)/x$，在零点处用其极限值补充为 $\operatorname{si}(0)=1$。

</li>

</ul>

:::
