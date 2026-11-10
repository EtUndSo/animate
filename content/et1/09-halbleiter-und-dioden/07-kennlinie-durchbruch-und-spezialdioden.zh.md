---
title: 第 5 阶段：特性曲线、击穿与特种二极管
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 半导体与二极管
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: 第 9 章：半导体与二极管
order: 1190700
summary: 方程已经有了。本阶段把它读成曲线，补充击穿现象，并说明利用结的特性还能制成什么。
tags: 阳极, 阴极, 雪崩效应, 齐纳效应, 击穿, 结电容, 光子, 内光电效应
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
方程已经有了。本阶段把它读成曲线，补充击穿现象，并说明利用结的特性还能制成什么。
:::

**基本思路。** p 侧称为__阳极__，n 侧称为__阴极__，两者都带有金属触点。电路符号中的三角形指向正向。在线性坐标中，0.6 V 处似乎有一个拐点（图 [6](#abb-6)）。这是刻度造成的，因为指数函数没有阈值。在量程为 10 mA 的轴上，曲线在 0.595 V 处达到终值的 1 %；在量程为 10 µ A 的轴上，在 0.417 V 处就已达到。在对数坐标中它是一条直线。

:::abbildung et1/k9kennlinie 6
结构、带参考箭头的电路符号和参考模型的特性曲线。中：线性坐标，反向电流 $10^{-14}$ A 看不见。右：对数坐标下是一条直线，只有在 $U=0$ 附近因 $-1$ 这一项而弯折。
:::

**击穿。** 反向电压很大时，该区内电场强到载流子通过碰撞释放出新的电子空穴对（__雪崩效应__），或电子直接从价带进入导带（__齐纳效应__）。反向电流急剧上升，这就是__击穿__。击穿本身并无害处。只有在没有任何东西限制电流时，热量 $P=U\,I$ 才会毁坏二极管。

**齐纳二极管。** 它专为在击穿区工作而制造，具有精确规定的电压 $U_\mathrm Z$（图 [7](#abb-7) 左）。在正向，它的行为与 pn 二极管相同。超过 $U_\mathrm Z$ 后特性曲线几乎垂直，其小电阻为 $r_\mathrm Z=\Delta U/\Delta I$。串联电阻吸收电源的波动：元件上的电压几乎不变，变化的是电流。当 $r_\mathrm Z=10\,\Omega$ 时，18 mA 的电流变化只造成 0.18 V。

**变容二极管。** 没有载流子的区域是两个导电区之间的绝缘层，因此是一个电容器（[第 3 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)），面积为 $A$，间距为 $w$。__结电容__随反向电压 $U_\mathrm R=-U$ 增大而减小，因为该区变宽：

<span class="anker" id="gl-5-1"></span>
$$C_\mathrm{j}=\frac{\varepsilon A}{w}=\frac{C_0}{\sqrt{1+U_\mathrm R/U_\mathrm{D0}}}. \tag{5.1}$$

当 $A=1\,\mathrm{mm^2}$ 时，$C_0=241$ pF；在 25 V 时为 40 pF，$w=2.6$ µ m。**适用条件：**突变结，工作于反向。这种效应特别强的二极管称为变容二极管。用它们可以通过电压调节谐振电路的频率，例如在无线电接收机中。由线圈和电容器组成的谐振电路的振荡频率取决于 $C$。

:::abbildung et1/k9spezial 7
左：$U_\mathrm Z=5.1$ V、$r_\mathrm Z=10\,\Omega$ 的齐纳二极管。中：按式 [(5.1)](#gl-5-1) 的电容。右：$I_\mathrm S=1$ nA 的太阳能电池在三种光照下的曲线。电流随光变化，开路电压几乎不变。下：电路符号和光电二极管的等效电路。
:::

**光电二极管。** 光由能量包组成，即__光子__，其能量 $W=h\,c/\lambda$（$h$：普朗克常数，$c$：光速，$\lambda$：波长）。若 $W\ge W_\mathrm g$，光子就把电子抬入导带（__内光电效应__）。对于硅，这要求 $\lambda\le1107$ nm。该区的电场把电子空穴对分开：电子跑向 n 侧，空穴跑向 p 侧。这是一股通过二极管从阴极流向阳极的电流，即反向电流，它与光功率成正比。

:::satz 定理 5.1 (受光照的二极管)
<span class="anker" id="satz-5-1"></span>

特性曲线向下移动__光电流__ $I_\mathrm{Ph}$。等效电路是一个与二极管并联的电流源：

<span class="anker" id="gl-5-2"></span>
$$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)-I_\mathrm{Ph},\qquad\text{开路 }(I=0):\ U_\mathrm L=U_T\ln\Bigl(\frac{I_\mathrm{Ph}}{I_\mathrm S}+1\Bigr). \tag{5.2}$$
:::

⁠**如何理解：**作为光传感器时，光电二极管工作于反向，此时 $I\approx-I_\mathrm{Ph}$。__太阳能电池__是工作于 $U>0$、$I<0$ 的大面积光电二极管：乘积 $U\,I$ 为负，它输出功率。光增强到十倍时，$I_\mathrm{Ph}$ 增大到十倍，而 $U_\mathrm L$ 只升高 60 mV。原因是式 [(5.2)](#gl-5-2) 中的对数。电压主要取决于材料，硅在工作时约为 0.5 V。在 $I_\mathrm S=1$ nA 的模型中，0.3 A、1 A 和 3 A 时 $U_\mathrm L=0.505$ V、0.536 V 和 0.564 V。**极限情况：**$I_\mathrm{Ph}=0$ 时得到式 [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1) 和 $U_\mathrm L=0$。

:::frage 二极管不是从 0.6 V 才开始导通吗？这难道不是阈值？
在电流约为 1 mA 的电路中看起来如此：在 0.4 V 时只有 52 nA，几乎测不出来。但电流从 0 V 起就均匀增长，每 60 mV 增大 10 倍。不存在某个电压使什么东西突然切换。只是电流的大小到某一时刻才变得对电路重要。
:::

:::aufgabe 练习 5 ★★ 稳住电压
<span class="anker" id="aufg-5"></span>

一只 $U_\mathrm Z=5.1$ V、$r_\mathrm Z=10\,\Omega$ 的齐纳二极管经 $R=220\,\Omega$ 接到在 10 V 和 14 V 之间波动的电源上。

<ol class="al">

<li>

如果二极管恰好保持 5.1 V，两种极端情况下的电流各是多少？

</li>

<li>

二极管电压实际变化多少？波动减小了多少倍？

</li>

<li>

在 14 V 时二极管消耗多少功率？

</li>

</ol>

:::loesung
(a) $I=(10\,\mathrm{V}-5.1\,\mathrm{V})/220\,\Omega=22.3$ mA 和 $(14\,\mathrm{V}-5.1\,\mathrm{V})/220\,\Omega=40.5$ mA。 (b) $\Delta U=r_\mathrm Z\Delta I=10\,\Omega\cdot18.2\,\mathrm{mA}=0.18$ V。更精确地说，$R$ 与 $r_\mathrm Z$ 分压：$4\,\mathrm{V}\cdot10/230=0.17$ V。波动减小到 1/23。 (c) $P=5.1\,\mathrm{V}\cdot40.5\,\mathrm{mA}=0.21$ W。
:::
:::

:::aufgabe 练习 6 ★★ 太阳能电池
<span class="anker" id="aufg-6"></span>

一块电池的 $I_\mathrm S=1$ nA，在充足阳光下 $I_\mathrm{Ph}=3$ A。

<ol class="al">

<li>

计算 $U_\mathrm L$。光减弱到三分之一时，$U_\mathrm L$ 如何变化？

</li>

<li>

计算 $U=0.5$ V 时的 $I$ 和输出功率。

</li>

<li>

要以每块 0.5 V 给 14 V 电池充电，需要串联多少块？

</li>

</ol>

:::loesung
(a) $U_\mathrm L=25.85\,\mathrm{mV}\cdot\ln(3\cdot10^{9}+1)=0.564$ V。在 1 A 时 $U_\mathrm L=0.536$ V，只低 28 mV。 (b) $I=10^{-9}\,\mathrm{A}\cdot(\mathrm{e}^{19.34}-1)-3\,\mathrm{A}=0.25\,\mathrm{A}-3\,\mathrm{A}=-2.75$ A。输出功率为 $0.5\,\mathrm{V}\cdot2.75\,\mathrm{A}=1.37$ W。 (c) $14\,\mathrm{V}/0.5\,\mathrm{V}=28$ 块。
:::
:::
