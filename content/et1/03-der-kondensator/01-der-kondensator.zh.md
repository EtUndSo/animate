---
title: 概览: 电容器
kurz: 概览
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电容器
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: 第 3 章：电容器
order: 1130100
summary: 电流如何流入绝缘体 能量之后又在哪里
tags: 电容器, 电极, 电介质, 电容, 平行板电容器, RC 电路
lang: zh
---

## 本章内容

两块金属板，中间隔着绝缘体：这种元件称为__电容器__。把它接到电池上，引线中就有电流流过，尽管两块极板并不接触。电流逐渐减弱，并自行停止。断开电池后，电压仍然保持，元件自身还能驱动电流。本章要回答的问题是：**电流怎么能流入绝缘体，它为什么会自行停止，能量之后又在哪里？**

每块极板是一个__电极__，中间的绝缘体称为__电介质__。表征这种元件的量是__电容__：它说明每伏电压使极板上有多少电荷。基本形式是两块平的极板，即__平行板电容器__。

**所有结论背后的同一个原理。** 电压表明有多少电荷被分离，而电荷只能通过电流改变。本章的所有结论都来自这两个事实：$u=q/C$ 和 $i=\mathrm{d} q/\mathrm{d} t$。

| 结论 | 来源 |
|---|---|
| 有间隙却有电流 | 电荷被移动，而不是被传递过去（第 [1](warum-strom-in-einen-isolator-fliet.html#stufe-1) 阶段） |
| $Q=CU$ | 电荷加倍，电场加倍，电压加倍（第 [2](die-kapazitat.html#stufe-2) 阶段） |
| $i=C\,\mathrm{d} u/\mathrm{d} t$，$u$ 不跳变 | 电流是单位时间的电荷（第 [3](strom-und-spannung-am-kondensator.html#stufe-3) 阶段） |
| $C=\varepsilon A/d$ | 单位电荷产生的电场取决于面积、间距和材料（第 [4](plattenkondensator-und-dielektrikum.html#stufe-4) 阶段） |
| 结构类型 | 大 $A$、小 $d$、大 $\varepsilon$（第 [5](bauformen-und-selbstentladung.html#stufe-5) 阶段） |
| $W=\frac12CU^2$ | 每份新增电荷都要克服已有的电压（第 [6](die-gespeicherte-energie.html#stufe-6) 阶段） |
| 并联与串联 | 电压相同或电荷相同（第 [7](parallel-und-reihenschaltung.html#stufe-7) 阶段） |
| 电荷重新分配 | 电荷不能离开孤岛（第 [8](ladungserhaltung-beim-umschalten.html#stufe-8) 阶段） |
| 短路、开路、指数曲线 | 电流取决于它自己建立的电压（第 [9](aufladen-uber-einen-widerstand.html#stufe-9) 阶段） |
| 放电，$\tau=RC$ | 同样的反馈，只是初始值不同（第 [10](entladen-und-zeitkonstante.html#stufe-10) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**[第 1 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)的平行极板：**边长 10 cm 的正方形极板（面积 $A=100$ cm$^2$），间距 $d=3$ mm，中间是空气，电压 9 V。电场为 $E=3$ kV/m。

</li>

<li>

⁠**RC 电路：**__RC 电路__是电阻与电容器串联后接到电源上的电路。这里一节 9 V 电池（$U_0=9$ V）通过 $R=10\,\mathrm{k\Omega}$ 给电容器 $C=100\,\mu\text{F}$ 充电。于是 $\tau=RC=1$ s。电池的内阻约 2 $\Omega$，比 $R$ 小 5000 倍，可以忽略。

</li>

<li>

⁠**两个电容器：**$C_1=100\,\mu\text{F}$（就是 RC 电路中的那一个）和 $C_2=50\,\mu\text{F}$。

</li>

</ul>

:::
