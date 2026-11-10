---
title: 概览: 电源与等效电源
kurz: 概览
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电源与等效电源
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: 第 5 章：电源与等效电源
order: 1150100
summary: 为什么两个数就能代替整个网络
tags: 
lang: zh
---

## 本章内容

一个传感器接在两根导线上，导线后面是由几十个元件组成的电路。它感受到的只有接线端上的电压和电流。本章要回答的问题是：**在两个接线端上描述整个网络，需要多少个数？**答案是两个，只要网络是线性的：它只含电阻和固定的电源，原因加倍，结果也加倍。

通向答案的路分为三段。第 [1](widerstande-zusammenfassen.html#stufe-1) 到第 [3](stern-und-dreieck.html#stufe-3) 阶段合并不含电源的网络。第 [4](ideale-quellen.html#stufe-4) 到第 [7](quellen-zusammenschalten.html#stufe-7) 阶段引入电源，并说明电源同样是直线。第 [8](uberlagerung.html#stufe-8) 和第 [9](thevenin-und-norton.html#stufe-9) 阶段证明这对每个线性网络都成立，第 [10](der-r-2r-wandler.html#stufe-10) 阶段把它用于一个转换器。


**所有结论背后的同一个原理。** 线性网络在两个接线端上的行为，就像电流-电压图中的一条直线，因此两个数就够了。从外部看，起作用的只有这条特性曲线：直线相同的两个电路可以互换，不管它们内部是什么样子。下表把各个结论归到这一思想之下。

| 结论 | 来源 |
|---|---|
| 总电阻 | 没有电源时特性曲线过原点，一个数就够（第 [1](widerstande-zusammenfassen.html#stufe-1) 阶段） |
| 对称性、半电路 | 等电位的点可以连接，无电流的支路可以断开（第 [2](symmetrie-nutzen.html#stufe-2) 阶段） |
| 星形与三角形 | 三个接线端、三个数，因此可以互换（第 [3](stern-und-dreieck.html#stufe-3) 阶段） |
| 理想电源 | 直线的极限情况：水平和竖直（第 [4](ideale-quellen.html#stufe-4) 阶段） |
| 工作点 | 电源直线与负载线的交点（第 [5](reale-quellen-und-der-arbeitspunkt.html#stufe-5) 阶段） |
| 电源的转换 | 同一条直线，从另一根坐标轴读取（第 [6](spannungsquelle-oder-stromquelle.html#stufe-6) 阶段） |
| 电源的组合 | 直线按电压或按电流相加（第 [7](quellen-zusammenschalten.html#stufe-7) 阶段） |
| 叠加 | 方程是线性的，每个电源单独起作用（第 [8](uberlagerung.html#stufe-8) 阶段） |
| 戴维南与诺顿 | 把接线端电流作为又一个原因进行叠加（第 [9](thevenin-und-norton.html#stufe-9) 阶段） |
| R-2R 转换器 | 每个开关是一个电源，每一梯级减半（第 [10](der-r-2r-wandler.html#stufe-10) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**电池：**[第 1 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)中的 9 V 方形电池。其源电压（化学反应提供的电压）为 $U_\mathrm{q}=9$ V，内阻为 $R_\mathrm{q}=2\,\Omega$。

</li>

<li>

⁠**负载：**接上的用电设备，电阻为 $R_\mathrm{L}=16\,\Omega$。第 [1](widerstande-zusammenfassen.html#stufe-1) 到第 [3](stern-und-dreieck.html#stufe-3) 阶段用许多电阻搭建负载网络，它们的结果都恰好是 16 $\Omega$。

</li>

<li>

⁠**网络 N：**两个电源和两个电阻（图 [9](uberlagerung.html#abb-9)）：$U_\mathrm{q1}=18$ V，$R_1=6\,\Omega$，$R_2=3\,\Omega$，$I_\mathrm{q2}=1.5$ A。第 [9](thevenin-und-norton.html#stufe-9) 阶段将说明：从外部看，N 与电池无法区分。

</li>

</ul>

脚本 `rechnung_kap5.py` 可复算所有数值。
:::
