---
title: 第 6 阶段：工作点
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 半导体与二极管
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: 第 9 章：半导体与二极管
order: 1190800
summary: 对于电阻， U=R\,I 立刻给出结果。二极管遵循另一条曲线。本阶段求出二极管在电路中的电压和电流。
tags: 负载线, 工作点, 工作点分析, 工作点综合, 开路, 短路, 迟滞, 迭代
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
对于电阻，$U=R\,I$ 立刻给出结果。二极管遵循另一条曲线。本阶段求出二极管在电路中的电压和电流。
:::

**基本思路。** 两个条件必须同时成立。二极管只允许其特性曲线上的点。电路的其余部分，即电源和电阻，只允许__负载线__（[第 5 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）上的点。电路会自行找到交点：若 $U_\mathrm D$ 太小，电阻提供的电流多于二极管通过的电流。电荷在两者之间的节点上积累，抬高其电位，直到两个电流相等。

:::abbildung et1/k9arbeitsgerade 8
参考模型的电路和图解法。红色：通过开路点和短路点的负载线。蓝色：二极管的特性曲线，交点在 0.69 V 和 4.31 mA。绿色：用 250 $\Omega$ 电阻代替二极管时的特性曲线，交点在 1 V 和 4 mA。
:::

:::definition 定义 6.1 (工作点)
<span class="anker" id="satz-6-1"></span>

__工作点__是特性曲线上由通过元件的电流和元件两端的电压确定的点。__工作点分析__是指由给定电路求出它。__工作点综合__是指选择元件，使之形成所需的工作点。
:::

**线性情况。** 若用电阻 $R_1$ 代替二极管，则有元件方程、网孔定律以及由此得到的负载线：

<span class="anker" id="gl-6-1"></span>
$$I=\frac{U_{R1}}{R_1},\qquad U_0=U_R+U_{R1}=R\,I+U_{R1},\qquad I=\frac{U_0-U_{R1}}{R}. \tag{6.1}$$

两个线性方程可以解出，取 $R_1=250\,\Omega$ 得 $I=U_0/(R+R_1)=4$ mA，$U_{R1}=1$ V。解方程组就是求两条直线的交点。

:::satz 定理 6.2 (二极管的工作点)
<span class="anker" id="satz-6-2"></span>

对于串联电路，下面两式同时成立：

<span class="anker" id="gl-6-2"></span>
$$I=\frac{U_0-U_\mathrm D}{R}\qquad\text{和}\qquad I=I_\mathrm S\bigl(\mathrm{e}^{U_\mathrm D/U_T}-1\bigr). \tag{6.2}$$

特性曲线处处上升，直线处处下降，因此恰有一个交点。
:::

⁠**如何理解：**$U_\mathrm D$ 就是式 [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1) 中的电压 $U$。画负载线时不考虑二极管，通过两点：__开路__（$I=0$，$U_\mathrm D=U_0$）和__短路__（$U_\mathrm D=0$，$I=U_0/R$）。特性曲线来自方程或数据手册。**适用条件：**特性曲线回折或状态取决于历史（__迟滞__）的元件可能有多个交点。多个非线性元件要用数值方法或等效电路求解（第 [7](lineare-ersatzschaltungen.html#stufe-7) 阶段）。

式 [(6.2)](#gl-6-2) 无法解出 $U_\mathrm D$，因为 $U_\mathrm D$ 既在指数中又在指数外。可以用图解法或__迭代__法求解，即反复代入：估计 $U_\mathrm D$，计算 $I=(U_0-U_\mathrm D)/R$，再算 $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$，然后重复。

::::beispiel
从 $U_\mathrm D=0.7$ V 开始。第 1 步：$I=4.300$ mA，$U_\mathrm D=0.69245$ V。第 2 步：$I=4.3076$ mA，$U_\mathrm D=0.69249$ V。于是工作点为 (0.692 V | 4.31 mA)，电阻上的电压为 4.31 V。把 $U_0$ 加倍到 10 V，电流几乎加倍，达到 9.29 mA，而 $U_\mathrm D$ 只升高 20 mV，达到 0.712 V。
::::

⁠**极限情况：**$U_0=0.5$ V 时 $I=2.3$ µ A，几乎全部电源电压都加在二极管上。$U_0$ 为负时 $I=-I_\mathrm S$，电源电压完全加在二极管上。

:::frage 为什么不反过来算：估计 $U_\mathrm D$，由指数函数求 $I$，再求 $U_\mathrm D=U_0-R\,I$？
因为这样做是发散的。1 mV 的误差使二极管电流变化 3.9 %，即 0.17 mA，这在电阻上造成 167 mV 的误差。在第一种方法中，误差每步按同一因子缩小，$r/R=0.006$（第 [8](kleine-anderungen-um-den-arbeitspunkt.html#stufe-8) 阶段）。平缓的对数函数起衰减作用，陡峭的指数函数起放大作用。
:::

:::aufgabe 练习 7 ★★ 求出并设定工作点
<span class="anker" id="aufg-7"></span>

参考模型的二极管与 $R=470\,\Omega$ 串联，接在 $U_0=3$ V 上。

<ol class="al">

<li>

确定负载线的开路点和短路点。

</li>

<li>

从 0.7 V 开始迭代，直到前三位数字不再变化。

</li>

<li>

工作点综合：在 $U_0=5$ V 时，多大的 $R$ 能得到 2 mA 的电流？用标准值 2.2 k$\Omega$ 时电流是多少？

</li>

<li>

把二极管反接。在二极管和电阻上测得什么？

</li>

</ol>

:::loesung
(a) 开路 $U_\mathrm D=3$ V，短路 $I=3\,\mathrm{V}/470\,\Omega=6.38$ mA。 (b) 由 $U_\mathrm D=0.7$ V 得 $I=4.894$ mA，由此得 $U_\mathrm D=0.6958$ V，再得 $I=4.903$ mA，又得 $U_\mathrm D=0.6958$ V。工作点：(0.696 V | 4.90 mA)。 (c) 在 2 mA 时 $U_\mathrm D=0.673$ V，所以 $R=(5\,\mathrm{V}-0.673\,\mathrm{V})/2\,\mathrm{mA}=2.16\,\mathrm{k\Omega}$。用 2.2 k$\Omega$ 时电流为 1.97 mA。 (d) 二极管截止：$I=-10^{-14}$ A，电阻上 4.7 pV，二极管上 $-3$ V。
:::
:::
