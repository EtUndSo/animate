---
title: 概览: 电荷、电场与电位
kurz: 概览
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电荷、电场与电位
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: 第 1 章：电荷、电场与电位
order: 1110100
summary: 为什么电压是一个差值 它对电荷起什么作用
tags: 电压, 电荷, 电场, 电位, 参考点, 电阻
lang: zh
---

## 本章内容

一块方形电池上标着 9 V。这个数值是一个__电压__。它说的不是电池储存了多少能量，而是每单位__电荷__从一个接线端到达另一个接线端时释放多少能量：每库仑 9 焦耳。电荷是某些粒子所具有的、能施加和感受电力的性质。焦耳是能量的单位，库仑是电荷的单位。本章要回答的问题是：**为什么电压总是两点之间的差值，它对电荷起什么作用？**

答案要经过两个概念。__电场__规定了每个位置上电荷所受的力。__电位__规定了每个位置上的电荷相对于一个自由选取的零点（即__参考点__）每库仑具有多少能量。


**所有结论背后的同一个原理。** 电荷所受的力和所具有的能量，取决于周围的其他电荷，也取决于它自身。除以电荷自身之后，剩下的就是位置的性质：力变为电场强度，能量变为电位。

| 结论 | 来源 |
|---|---|
| 电场强度 $\vec E=\vec F/Q$ | 单位电荷所受的力：试探电荷已被除去（第 [4](die-feldstarke.html#stufe-4) 阶段） |
| 电场线、屏蔽 | $\vec E$ 的图像；金属中的自由电子自行排布，直到不再受力（第 [5](feldlinien-und-leiter.html#stufe-5) 阶段） |
| $W_{12}=Q\int\vec E\cdot\mathrm{d}\vec s$，与路径无关 | 功是力乘以路程；库仑力沿径向，只有距离起作用（第 [6](arbeit-im-feld.html#stufe-6) 阶段） |
| 电位 $\varphi$ | 到参考点为止单位电荷所得的功（第 [7](das-potenzial.html#stufe-7) 阶段） |
| 电压、接地点 | 两点之间单位电荷所得的功；零点可以自由选取（第 [8](spannung-und-masse.html#stufe-8) 阶段） |
| 电荷的速度 | 能量 $QU$ 转化为动能（第 [9](was-die-spannung-mit-einer-ladung-macht.html#stufe-9) 阶段） |
| 电磁感应 | 这一原理的界限：磁场变化时，功与路径有关（第 [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**平行极板：**两块平的金属板 A 和 B，处于真空（没有空气的空间）中，间距 $d=3$ mm，远小于极板宽度。一节 9 V 电池的正极接 A，负极接 B。$x$ 轴从 A（$x=0$）指向 B。两板之间是均匀电场 $E=3$ kV/m（第 [5](feldlinien-und-leiter.html#stufe-5) 和第 [8](spannung-und-masse.html#stufe-8) 阶段）。

</li>

<li>

⁠**两个小球：**小球的电荷分别为 $Q_\mathrm{A}=+10$ nC 和 $Q_\mathrm{B}=-20$ nC，相距 $r=3$ cm。小球 A 的质量为 1 g。

</li>

<li>

⁠**电路：**同一节电池接在两个串联的电阻上，第一个电阻上为 6 V，第二个上为 3 V。__电阻__是一种元件，流过它的电荷在其中以热的形式释放能量（[第 2 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。

</li>

<li>

⁠**常数：**$e=1.602\cdot10^{-19}$ C，$m_\mathrm{e}=9.109\cdot10^{-31}$ kg，$k=8.99\cdot10^{9}\,\mathrm{N\,m^2/C^2}$，$g=9.81\,\mathrm{m/s^2}$；各阶段会解释它们。脚本 `rechnung_kap1.py` 可复算所有数值。

</li>

</ul>
:::
