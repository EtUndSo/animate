---
title: 第 1 阶段：电流是运动的电荷
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电流、电阻与基尔霍夫定律
order: 1120200
summary: 第 1 部分讨论的是静止的或单个飞行的电荷。在导线中，无数电荷一起运动。本阶段为这种运动给出两个度量。
tags: 电荷密度, 电流强度, 电路, 稳态
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)讨论的是静止的或单个飞行的电荷。在导线中，无数电荷一起运动。本阶段为这种运动给出两个度量。
:::

**基本思路。** 站在导体的某一处，测量每秒有多少电荷经过。这取决于三件事：电荷有多密，运动有多快，横截面有多大。在时间 $\Delta t$ 内，恰好是此前距该面积不超过 $v\,\Delta t$ 的电荷通过该面积（图 [1](#abb-1)）。

:::abbildung et1/k2strom 1
导体中速度为 $v$ 的载流子。阴影段内的全部电荷在时间 $\Delta t$ 内通过面积 $A$。该段的体积为 $A\,v\,\Delta t$。
:::

:::definition 定义 1.1 (电流与电流密度)
<span class="anker" id="satz-1-1"></span>

__电荷密度__ $q=\Delta Q/\Delta V$ 是单位体积的电荷。__电流强度__（简称电流）是单位时间内通过某一面积的电荷。电流密度是单位面积上的电流：

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} i&=\lim_{\Delta t\to0}\frac{\Delta Q}{\Delta t}=\frac{\mathrm{d} Q}{\mathrm{d} t},\qquad I=q\,v\,A,\qquad [I]=\mathrm{C/s}=\mathrm A,\\ j&=\frac IA=q\,v,\qquad\vec j=q\,\vec v. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**如何理解：**$i$ 是随时间变化的电流，$I$ 是恒定电流，单位为安培：参考模型中为 3 mA，发光二极管中为 20 mA，家用线路中为 16 A。$q$ 的单位是 $\mathrm{C/m^3}$。对铜中的自由电子，$q=-n\,e=-1.36\cdot10^{10}\,\mathrm{C/m^3}$。$j$ 的单位是 $\mathrm{A/m^2}$，家用线路约为 $10\,\mathrm{A/mm^2}$。$q>0$ 时矢量 $\vec j$ 与 $\vec v$ 同向，$q<0$ 时反向。**适用条件：**$I=q\,v\,A$ 要求 $q$ 和 $v$ 在 $A$ 上处处相同，且 $v$ 垂直于 $A$。

:::herleitung 由密度和速度求电流
设面积 $A=\Delta x\,\Delta y$。阴影段的体积为 $\Delta V=\Delta x\,\Delta y\,\Delta z$，其中 $\Delta z=v\,\Delta t$。它含有电荷 $\Delta Q=q\,\Delta V=q\,A\,v\,\Delta t$，这些电荷在时间 $\Delta t$ 内通过 $A$。所以 $\Delta Q/\Delta t=q\,v\,A$。
:::

**何时有持续的电流？** 必须满足两个条件。第一，电路需要一个电源，例如电池或电源适配器。它提供的是能量，而不是电荷：载流子本来就在导体中，电源只是推动它们在电路中循环。第二，__电路__必须闭合，即形成一条回到自身的路径。否则电荷会在断开处堆积，其电场抵消驱动电场，电流随之停止。闭合电路中不随时间变化的电流称为__稳态__电流。

::::beispiel
在参考模型中，每秒有 3 mC 通过导线，即 $3\,\mathrm{mC}/e=1.87\cdot10^{16}$ 个电子。电流密度为 $j=3\,\mathrm{mA}/0.5\,\mathrm{mm^2}=6\,\mathrm{mA/mm^2}$。一米导线含有自由电荷 $n\,e\,A=6800$ C。因此，一块方形电池一生所输送的全部电荷（约 1800 C）在这根导线的 26 cm 内就已经有了。**检验：**$v=0$ 时 $I=0$，不管导线中有多少电荷。$v$ 相同时面积加倍，电流加倍，因为这相当于两根并排的导线。
::::

:::frage 电子在负载中被消耗掉了吗？
没有。电荷守恒，每秒从元件流出的电子数与流入的相同。被消耗的是能量：每库仑电荷把它单位电荷的能量（即电压）交给元件，然后以较低的电位继续前进。
:::

:::aufgabe 练习 1 ★ 电流、电荷、电流密度
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

一个发光二极管通过 20 mA 的电流，持续 5 min。有多少电荷通过它？这相当于多少个电子？

</li>

<li>

横截面积为 $1.5\,\mathrm{mm^2}$ 的电缆通过 16 A。$j$ 等于多少 $\mathrm{A/mm^2}$？

</li>

<li>

在一根导线中电子向右运动，$\vec j$ 指向哪个方向？

</li>

</ol>

:::loesung
(a) $Q=I\,t=20\,\mathrm{mA}\cdot300\,\mathrm{s}=6$ C，即 $6\,\mathrm{C}/e=3.7\cdot10^{19}$ 个电子。 (b) $j=16\,\mathrm{A}/1.5\,\mathrm{mm^2}=10.7\,\mathrm{A/mm^2}$。 (c) 向左：对电子有 $q<0$，所以 $\vec j=q\,\vec v$ 与 $\vec v$ 反向。
:::
:::
