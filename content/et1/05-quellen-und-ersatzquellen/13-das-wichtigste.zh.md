---
title: 要点
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电源与等效电源
order: 1151300
summary: 为什么两个数就能代替整个网络
tags: 叠加, 开路电压, 内阻, 等效电源, 短路
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

在线性网络中，各电源的作用相加，因为所有方程都是线性的。这就是__叠加__，即各作用的相互重叠。

</li>

<li>

因此，两个接线端 A 和 B 之间的电压是接线端电流的一条直线：$U_\mathrm{AB}=U_\mathrm{OC}-R_\mathrm{i}\,I_\mathrm{A}$。电源决定__开路电压__ $U_\mathrm{OC}$（接线端断开时的电压），电阻决定__内阻__ $R_\mathrm{i}$（斜率）。

</li>

<li>

一条直线有两个数。因此网络的行为就像一个__等效电源__，即一个带内阻的电源。开路和__短路__（接线端相连）给出这两个数：$R_\mathrm{i}=U_\mathrm{OC}/I_\mathrm{SC}$。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

串联：电阻相加，电流相同。并联：电导相加，电压相同。由内向外合并。

</li>

<li>

等电位的节点可以连接，无电流的支路可以断开。对称性指出哪里可以这样做。

</li>

<li>

星形和三角形在接线端上可以互换：$R_{10}=R_{12}R_{31}/(R_{12}+R_{23}+R_{31})$。

</li>

<li>

理想电源固定一个量。实际电源：$U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}$。转换：$I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$，电阻相同。

</li>

<li>

叠加：电压源变成导线，电流源变成断口，部分作用相加。功率不相加。

</li>

<li>

每个线性一端口网络都是一条直线：$U_\mathrm{i}=U_\mathrm{OC}$，$I_\mathrm{i}=I_\mathrm{SC}$，$R_\mathrm{i}=U_\mathrm{OC}/I_\mathrm{SC}$。工作点是它与负载直线的交点。

</li>

</ul>
:::
