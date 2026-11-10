---
title: 第 4 阶段：理想电源
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电源与等效电源
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: 第 5 章：电源与等效电源
order: 1150600
summary: 到目前为止，还缺少驱动电流的东西。本阶段引入向网络输送能量的两种基本元件。
tags: 理想电压源, 理想电流源, 源电压, 源电流
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
到目前为止，还缺少驱动电流的东西。本阶段引入向网络输送能量的两种基本元件。
:::

**基本思路。** 电源只把一个量固定下来。另一个量由所接的网络决定。__理想电压源__保持其接线端之间的电位差。流过多大的电流，由负载决定。__理想电流源__保持其支路中的电流。产生多大的电压，同样由负载决定。两者都是模型。它们造不出来，但稳压电源或晶体管电路（[第 10 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)）在有限范围内可以接近它们。

:::abbildung et1/k5ideal 5
左：理想电压源，在图中是一条水平线，电压与电流无关。右：理想电流源，是一条竖直线，电流与电压无关。电路符号中的短线表示数值为零时的行为：沿线路方向画的，表示线路接通；横跨线路画的，表示线路断开。
:::

:::definition 定义 4.1 (理想电源)
<span class="anker" id="satz-4-1"></span>

对理想电压源和理想电流源有

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{AB}=U_\mathrm{q}\quad\text{对任意电流},\qquad\qquad I_\mathrm{A}=I_\mathrm{q}\quad\text{对任意电压}. \tag{4.1}$$
:::

⁠**如何理解：**$U_\mathrm{q}$ 是__源电压__，单位 V，从毫伏到千伏，这里是 9 V。$I_\mathrm{q}$ 是__源电流__，单位 A，从微安到安。在图 [5](#abb-5) 中，特性曲线的斜率是带负号的内阻：电压源为零，电流源为无穷大。计算时，电压源把两个节点电位之差换成已知值，电流源确定一条支路的电流。

⁠**适用条件：**有两种接法与模型矛盾。被短路的电压源要同时满足 $U_\mathrm{AB}=U_\mathrm{q}$ 和 $U_\mathrm{AB}=0$。开路的电流源要同时满足 $I_\mathrm{A}=I_\mathrm{q}$ 和 $I_\mathrm{A}=0$，因为电流需要闭合的路径。

::::beispiel
9 V 电源接 16 $\Omega$ 时输出 0.5625 A，接 1 $\Omega$ 时输出 9 A，接 1 m$\Omega$ 时将是 9000 A。0.5 A 电源在 16 $\Omega$ 上产生 8 V，在 1 k$\Omega$ 上产生 500 V，在 1 M$\Omega$ 上将是 500 kV。
::::

⁠**极限情况：**负载越极端，模型离任何真实设备就越远。这正是下一阶段的理由。

:::frage 电流也能反向流过电源吗？
能。理想电源只确定它自己的那一个量。如果电流流入电压源的正极，则 $I_\mathrm{A}<0$，电源吸收功率。给蓄电池充电就是这样。
:::

:::aufgabe 练习 5 ★ 什么发生了变化？
<span class="anker" id="aufg-5"></span>

2 mA 的理想电流源向 1 k$\Omega$ 供电。(a) 电压是多少？换成 4.7 k$\Omega$ 时又是多少？(b) 与电源串联再接入一个 1 k$\Omega$ 的电阻。第一个电阻上有什么变化，电源上有什么变化？(c) 一个理想 5 V 电源向 1 k$\Omega$ 供电，再并联接入 10 $\Omega$。负载上有什么变化，电源上有什么变化？

:::loesung
(a) $2\,\mathrm{mA}\cdot1\,\mathrm{k\Omega}=2$ V，接 4.7 k$\Omega$ 时为 9.4 V。电流不变。

(b) 第一个电阻上没有变化：电流固定，电压仍为 2 V。电源必须提供 4 V。与理想电流源串联的电阻，从外部看不见。

(c) 负载上没有变化，仍为 5 V 和 5 mA。电源输出 505 mA 而不是 5 mA。与理想电压源并联的电阻，从外部看不见。
:::
:::
