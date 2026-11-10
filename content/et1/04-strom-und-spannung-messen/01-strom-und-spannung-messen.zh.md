---
title: 概览: 电流与电压的测量
kurz: 概览
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电流与电压的测量
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: 第 4 章：电流与电压的测量
order: 1140100
summary: 为什么每台测量仪表都会改变电路 以及如何仍然测得准确
tags: 内阻, 表头, 量程
lang: zh
---

## 本章内容

一个分压器上本应有 3 V，测量仪表却显示 2.73 V。分压器没有问题，读数也没有错：它显示的是仪表接入之后实际存在的电压。因为测量仪表是一个具有__内阻__的元件，内阻就是其接线端之间的电阻。问题是：**为什么每台测量仪表都会改变被测电路，误差有多大，为什么电桥比单独一台仪表测得更准确？**


**所有结论背后的同一个原理。** 对电路来说，测量仪表就是多出来的一个电阻。所有误差都来自与[第 2 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)相同的规律：基尔霍夫电压定律、基尔霍夫电流定律、欧姆定律。

| 结论 | 来源 |
|---|---|
| 内阻 | 仪表需要电流，其线圈有电阻（第 [1](das-messgerat-ist-ein-bauteil.html#stufe-1) 阶段） |
| 分流电阻与串联电阻 | 分流电路和分压器保护仪表（第 [2](den-messbereich-erweitern.html#stufe-2) 阶段） |
| $I_R'=U/(R+R_\mathrm i)$ | 回路中多了一个电阻（第 [3](der-fehler-beim-strommessen.html#stufe-3) 阶段） |
| $U_L'=U_L/(1+R_L/R_\mathrm i)$ | 节点上多了一条支路（第 [4](der-fehler-beim-spannungsmessen.html#stufe-4) 阶段） |
| 电流正确与电压正确 | 每台仪表都处在另一台仪表的测量回路中（第 [5](strom-und-spannung-zugleich.html#stufe-5) 阶段） |
| 平衡 $R_4=R_3R_2/R_1$ | 没有电流时，仪表不从电桥取走任何东西（第 [6](die-wheatstonesche-brucke.html#stufe-6) 阶段） |
| $U_\mathrm d\approx\frac14U_\mathrm q\,\Delta R/R$ | 电桥减去了公共电压（第 [7](die-verstimmte-brucke.html#stufe-7) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的参考模型
<ul>

<li>

⁠**仪表：**一个__表头__（仪表中把电流转换为指针偏转的部分），满偏电流 $I_\mathrm M=50$ µ A，自身电阻 $R_\mathrm M=2$ k$\Omega$。作为电流表，在 10 mA 的__量程__（可显示的数值范围）内，$R_\mathrm{iA}=10\,\Omega$；作为电压表，在 10 V 的量程内，$R_\mathrm{iV}=200$ k$\Omega$（第 [2](den-messbereich-erweitern.html#stufe-2) 阶段）。其读数偏差最大为满量程值的 1 %。

</li>

<li>

⁠**被测对象：**$R=1.8$ k$\Omega$，接在理想电压源 $U=9$ V 上（在任何电流下都保持 9 V）。不接仪表时电流为 5 mA。

</li>

<li>

⁠**分压器：**$R_1=60$ k$\Omega$ 和 $R_2=30$ k$\Omega$ 串联后接 9 V，$R_2$ 上为 3 V。

</li>

<li>

⁠**电桥：**$R_1=1$ k$\Omega$，$R_2=1.8$ k$\Omega$，$R_3=1$ k$\Omega$，接 9 V；待求 $R_4$。对于微小变化，用四个各 350 $\Omega$ 的电阻，接 9 V。

</li>

</ul>

脚本 `rechnung_kap4.py` 复核了所有数值。
:::
