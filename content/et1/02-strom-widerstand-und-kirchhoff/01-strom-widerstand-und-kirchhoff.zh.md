---
title: 概览: 电流、电阻与基尔霍夫定律
kurz: 概览
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电流、电阻与基尔霍夫定律
order: 1120100
summary: 为什么电子缓慢爬行，电流却立刻出现， 以及为什么电路网络服从守恒定律
tags: 电流, 电阻, 欧姆定律, 节点定律, 网孔定律
lang: zh
---

## 本章内容

闭合电路的瞬间，灯就亮了。可是导线中的电子爬行的速度，比蜗牛还慢约 2000 倍。__电流__是运动的电荷，用单位时间的电荷量来度量。__电阻__是一种阻碍这种运动、并把其能量转化为热的元件。本章要回答的问题是：**电压如何变成电流，电流又如何在由许多元件组成的网络中分配？**

答案由三条定律组成。__欧姆定律__把一个元件上的电压和电流联系起来。__节点定律__指出，在分支处电流不会消失。__网孔定律__指出，沿闭合路径各电压之和为零。


**所有结论背后的同一个原理。** 两条守恒定律和一个平衡贯穿本章：电荷不会丢失，能量不会丢失，而在导体中，电场的驱动与碰撞的制动相互平衡。

| 结论 | 来源 |
|---|---|
| $I=\mathrm{d} Q/\mathrm{d} t$，$j=q\,v$ | 一定时间内通过某一面积的电荷（第 [1](strom-ist-bewegte-ladung.html#stufe-1) 阶段） |
| 微小而恒定的漂移 | 电场与碰撞的平衡，极大的电子密度（第 [2](langsame-elektronen-sofortiger-strom.html#stufe-2) 阶段） |
| 电流立刻出现 | 传播的是电场，而不是电子；导线中本来就充满电子（第 [2](langsame-elektronen-sofortiger-strom.html#stufe-2) 阶段） |
| $U=R\,I$，$R=\rho L/A$ | 漂移与电场成正比，电场与电压成正比（第 [3](das-ohmsche-gesetz-aus-feld-und-stoen.html#stufe-3) 阶段） |
| 温度依赖性 | 热改变飞行时间或载流子数目（第 [4](reale-widerstande-werte-und-temperatur.html#stufe-4) 阶段） |
| 参考箭头，$m=z-k+1$ | 计算之前的约定和计数（第 [5](zweipole-und-zahlpfeile.html#stufe-5) 和第 [6](knoten-zweige-maschen.html#stufe-6) 阶段） |
| 节点定律 | 电荷守恒：节点不储存任何东西（第 [7](die-knotenregel-ist-ladungserhaltung.html#stufe-7) 阶段） |
| 网孔定律 | 能量守恒：绕行一周回到起始电位（第 [8](die-maschenregel-ist-energieerhaltung.html#stufe-8) 阶段） |
| 分压器、分流器 | 两条定律应用于串联和并联（第 [9](reihenschaltung-und-spannungsteiler.html#stufe-9) 和第 [10](parallelschaltung-stromteiler-und-belastung.html#stufe-10) 阶段） |

**如何使用本章。**每个阶段都是一篇简短的文章，包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。完成一个阶段后再进入下一个。

:::merke 本章的参考模型
<ul>

<li>

⁠**串联链：**[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)的 9 V 电池接在两个串联电阻 $R_1=2\,\mathrm{k\Omega}$ 和 $R_2=1\,\mathrm{k\Omega}$ 上。电流为 3 mA，$R_1$ 上为 6 V，$R_2$ 上为 3 V。

</li>

<li>

⁠**导线：**铜，长度 $L=1$ m，横截面积 $A=0.5\,\mathrm{mm^2}$，电阻率（材料常数，第 [3](das-ohmsche-gesetz-aus-feld-und-stoen.html#stufe-3) 阶段）$\rho=1.7\cdot10^{-8}\,\mathrm{\Omega\,m}$，自由电子密度 $n=8.5\cdot10^{28}\,\mathrm{m^{-3}}$（每个原子一个）。它流过串联链的 3 mA。

</li>

<li>

⁠**网络：**一个 9 V 电源和五个电阻，接在四个分支点之间，$R_\mathrm a=2$，$R_\mathrm b=5$，$R_\mathrm c=3$，$R_\mathrm d=1$，$R_\mathrm e=2$（单位均为 $\mathrm{k\Omega}$），图 [7](knoten-zweige-maschen.html#abb-7)。

</li>

<li>

⁠**常数：**$e=1.602\cdot10^{-19}$ C，$m_\mathrm e=9.109\cdot10^{-31}$ kg。

</li>

</ul>

脚本 `rechnung_kap2.py` 可复算所有数值。
:::
