---
title: 概览: 随机信号
kurz: 概览
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 随机信号
order: 3270100
summary: 均值、分布、功率谱密度， 系统中的噪声与最佳接收机
tags: 
lang: zh
---

## 本章内容

电阻的噪声、语音、数据流：这类信号无法预测。人们不知道它们的确切波形，却知道它们的*平均性质*：它们通常有多大，变化有多快，包含哪些频率。本章说明如何描述这样的随机信号，LTI 系统对它们有什么作用，以及怎样才能最可靠地在噪声中检测出一个已知信号。


**所有结论背后的同一个原理。** 用平均值来代替未知的信号本身，而平均运算是线性的：

| 结论 | 来源 |
|---|---|
| 均值、功率、方差 | 集平均与时间平均（第 [1](der-zufallsprozess.html#stufe-1) 至第 [3](mittelwert-leistung-varianz.html#stufe-3) 阶段） |
| 自相关函数、协方差、互相关函数 | 对两个时刻取值的乘积求平均（第 [4](autokorrelation-kovarianz-und-kreuzkorrelation.html#stufe-4) 阶段） |
| 概率密度函数 | 在集合中或在时间上低于某一门限的比例（第 [5](verteilungsfunktion-und-verteilungsdichte.html#stufe-5) 阶段） |
| 独立变量之和 | 概率密度的卷积，因此趋于高斯分布（第 [6](verbundverteilung-unabhangigkeit-unkorreliertheit.html#stufe-6)、[7](die-gau-verteilung.html#stufe-7) 阶段） |
| 功率谱密度、维纳–李关系 | 卷积积分中数学期望的线性（第 [8](zufallssignale-in-lti-systemen-leistungsdichte.html#stufe-8) 阶段） |
| 白噪声 | 恒定的功率谱密度，自相关函数 $=N_0\delta$（第 [9](weies-rauschen-und-thermisches-rauschen.html#stufe-9) 阶段） |
| 匹配滤波器 | 柯西–施瓦茨不等式：信号与自身的相关最大（第 [10](das-korrelationsfilter-matched-filter.html#stufe-10) 阶段） |
| 误码率 | 高斯曲线位于门限另一侧的面积（第 [11](fehlerwahrscheinlichkeit-beim-binarempfang.html#stufe-11) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**均匀分布的随机数**，取值在 $-\frac12$ 与 $\frac12$ 之间（方差为 $\frac{1}{12}$），也用作离散时间白噪声。

</li>

<li>

⁠**电阻** $R=1\,\mathrm{k\Omega}$，温度 290 K，带宽 20 kHz（音频）。

</li>

<li>

⁠**递归系统** $g(n)=s(n)+0.6\,g(n-1)$，取自[第 4 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)。

</li>

</ul>

脚本 `rechnung_kap7.py` 可复算这些数值，其中一部分还用模拟的随机数加以验证。
:::
