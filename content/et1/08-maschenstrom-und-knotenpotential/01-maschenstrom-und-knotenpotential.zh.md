---
title: 概览: 网孔电流法与节点电位法
kurz: 概览
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 网孔电流法与节点电位法
order: 1180100
summary: 为什么一个网络只需很少的未知量
tags: 
lang: zh
---

## 本章内容

[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)的网络有六条支路。每条支路有一个电流和一个电压，共十二个未知量，经过漫长的代入之后才剩下三个方程。一个含晶体管的电路有数百条支路。本章要回答的问题是：**整个网络最少需要多少个未知量，又如何不经变形就写出方程？**


**所有结论背后的同一个原理。** 基尔霍夫要求两件事：节点定律和网孔定律。如果这样选取未知量，使其中一条定律对任意数值都成立，就只需写出另一条。这时未知量的个数恰好等于余下方程的个数。

| 结论 | 来源 |
|---|---|
| $m$ 个自由电流，$k-1$ 个自由电压 | 一棵树决定了哪些量可以给定、哪些量由此得出（第 [1](wie-viele-groen-sind-frei.html#stufe-1) 阶段） |
| 网孔电流 | 环流不给任何节点带来净电流（第 [2](maschenstrome-erfullen-die-knotenregel.html#stufe-2) 阶段） |
| 电阻矩阵 $\mathbf Z$ | 本网孔电流流过网孔的所有电阻，其他网孔的电流只流过公共电阻（第 [3](das-maschenstromverfahren.html#stufe-3) 阶段） |
| 节点电位 | 绕行一周回到起始电位（第 [4](potenziale-erfullen-die-maschenregel.html#stufe-4) 阶段） |
| 电导矩阵 $\mathbf Y$ | 本节点电位驱动电流流过该节点的所有电导，其他节点的电位只驱动电流流过公共电导（第 [5](das-knotenpotentialverfahren.html#stufe-5) 阶段） |
| 方法的选择 | 两个数中较小者胜出，即是否 $z>2k-2$（第 [6](welches-verfahren-wann.html#stufe-6) 阶段） |
| 印记与网表 | 一个元件只接触它的两个节点（第 [7](stempel-und-netzliste.html#stufe-7) 阶段） |
| 不对称矩阵 | 受控源取决于其他节点（第 [8](gesteuerte-quellen-und-verstarker.html#stufe-8) 阶段） |
| 改进节点法 | 理想电压源没有电导，它的电流成为未知量（第 [9](die-modifizierte-knotenanalyse.html#stufe-9) 阶段） |

**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。

:::merke 本章的模型电路
<ul>

<li>

⁠**网络**（图 [1](wie-viele-groen-sind-frei.html#abb-1)）有三个节点：接地点 0 以及节点 1 和 2。左边由一节 $U_\mathrm q=9$ V、内阻 $R_1=1\,\mathrm{k\Omega}$（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）的电池供电，右边由一个 $I_\mathrm q=4$ mA 的实际电流源供电，并联 $R_5=5\,\mathrm{k\Omega}$。两者之间是从 1 到接地点的 $R_2=4\,\mathrm{k\Omega}$、从 1 到 2 的 $R_3=2\,\mathrm{k\Omega}$ 和从 2 到接地点的 $R_4=10\,\mathrm{k\Omega}$。

</li>

<li>

⁠**放大器**（第 [8](gesteuerte-quellen-und-verstarker.html#stufe-8) 阶段）是[第 6 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)的模型：输入电阻 $R_\mathrm i=2\,\mathrm{k\Omega}$，$g=50$ mS 的受控电流源，输出电阻 $R_\mathrm o=20\,\mathrm{k\Omega}$，负载 $R_\mathrm L=5\,\mathrm{k\Omega}$。

</li>

<li>

⁠**单位：**计算使用 V、mA、k$\Omega$ 和 mS。由于 $\mathrm{k\Omega\cdot mA}=\mathrm V$，$\mathrm{mS\cdot V}=\mathrm{mA}$，不会出现十的幂。脚本 `rechnung_kap8.py` 可复算所有数值。

</li>

</ul>
:::
