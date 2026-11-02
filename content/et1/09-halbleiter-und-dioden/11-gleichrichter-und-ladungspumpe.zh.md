---
title: 第 9 阶段：整流器与电荷泵
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 半导体与二极管
order: 1191100
summary: 半波整流器白白浪费了每隔一个的半波。本阶段利用两个半波，并说明如何用二极管和电容器把电压升到电源电压以上。
tags: 桥式整流器, 平滑
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
半波整流器白白浪费了每隔一个的半波。本阶段利用两个半波，并说明如何用二极管和电容器把电压升到电源电压以上。
:::

**基本思路。** __桥式整流器__（格雷茨电路）由四个二极管组成菱形（图 [11](#abb-11)）。它们在每个半波中切换负载，使电流总是从上到下流过负载。左侧电压为正时，电流经过 D$_1$、负载和 D$_3$。此时 D$_2$ 的阴极在上方的高电位，阳极在低输入端，因而截止，D$_4$ 也是如此。在另一个半波中两对二极管互换。

:::abbildung et1/k9graetz 11
上：两个半波中的电桥，导通的二极管为彩色，截止的为灰色，加号标出较高的输入端。通过负载 $R$ 的电流方向始终相同。下：$\hat u=12$ V、$U_\mathrm F=0.7$ V 时的输入 $u_\mathrm e$（灰）和输出 $u_\mathrm a$（蓝）。
:::

:::satz 定理 9.1 (桥式整流器)
<span class="anker" id="satz-9-1"></span>

在含正向电压的模型中，由于电流总是流过两个串联的二极管，有

<span class="anker" id="gl-9-1"></span>
$$u_\mathrm a=\begin{cases}|u_\mathrm e|-2U_\mathrm F&|u_\mathrm e|>2U_\mathrm F\\0&\text{其他情况。}\end{cases} \tag{9.1}$$

截止的二极管最多承受 $\hat u-U_\mathrm F$。
:::

⁠**如何理解：**$|u_\mathrm e|<2U_\mathrm F$ 时两对二极管都不导通，$u_\mathrm a$ 保持为零。从降低的峰值可以读出两倍的正向电压。**适用条件：**电阻性负载。输入和输出没有公共参考点。

**例。** 峰值为 $12\,\mathrm{V}-1.4\,\mathrm{V}=10.6$ V，半波整流器为 11.3 V。每个半波中的间隙持续 0.74 ms，占时间的 7.4 %。平均值为 6.29 V，半波整流器只有 3.48 V。**极限情况：**$U_\mathrm F\to0$ 时 $u_\mathrm a=|u_\mathrm e|$。$\hat u<1.4$ V 时输出保持为零。

:::ltspice 桥式整流器
⁠**绘制：**电源取 `SINE(0 12 50)`，接在 `a` 和 `b` 之间。二极管 DM 分别从 `a` 接到 `p`，从 `b` 接到 `p`，从接地点接到 `a`，从接地点接到 `b`。`res` 1k 从 `p` 接地。

⁠**指令：**`.tran 40m`

⁠**你会看到：**`V(p)` 如图 [11](#abb-11) 所示，峰值 10.57 V，平均值 6.29 V。截止二极管上的电压 $V(p,a)$ 达到 11.28 V。计算值为 10.6 V、6.29 V 和 11.3 V。做练习 [11](#aufg-11) 时，用 24 代替 12。
:::

:::frage 这个电压还脉动得很厉害。这已经是直流电压了吗？
还不是。与负载并联的电容器（__平滑__）充电到峰值，并在间隙中向负载供电。在 10 ms 内它损失 $\Delta U=I\,\Delta t/C$（[第 3 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)）。取 $I=10.6$ mA、$C=470$ µ F，这就是 0.23 V。此时二极管只在峰值处短暂导通。
:::

**电荷泵。** 它不用线圈，就能由直流电压 $U_\mathrm e$ 产生更高的电压。这里把二极管视为理想的（图 [12](#abb-12)）。**第 1 步：**转换开关把 $C_1$ 的下极板接地。$C_1$ 经 D$_1$ 充电到 $U_\mathrm e$。**第 2 步：**转换开关把下极板接到 $U_\mathrm e$。$C_1$ 上的电压不能跳变（[第 3 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)），所以上极板跳变到 $2U_\mathrm e$。D$_1$ 截止，因为它的阴极现在更高；D$_2$ 导通，$C_1$ 向输出电容器 $C_2$ 放出电荷。经过几个周期后，$U_\mathrm a\approx2U_\mathrm e$。实际中用小电阻限制电流尖峰。按同样方式增加泵级，电压还能继续升高。

:::abbildung et1/k9pumpe 12
电荷泵；两个步骤的电流路径用彩色标出。左：$U_\mathrm e$ 给电容器 $C_1$ 充电。右：$U_\mathrm e$ 与 $C_1$ 上的电压串联，向 $C_2$ 供电。
:::

:::herleitung $C_1=C_2$ 时 $k$ 个周期后的电压
在第一步中，$C_2$ 也经两个二极管充电到 $U_\mathrm e$。在泵送步骤中，电压为 $2U_\mathrm e$ 的 $C_1$ 与电压为 $U_\mathrm a$ 的 $C_2$ 相连。电荷守恒，相同的电容器最终达到平均值：$U_\mathrm a'=(2U_\mathrm e+U_\mathrm a)/2$。到终值 $2U_\mathrm e$ 的距离每个周期减半：$U_\mathrm a(k)=2U_\mathrm e-U_\mathrm e\,2^{-k}$。
:::

$U_\mathrm e=5$ V 时得到 7.5 V、8.75 V、9.38 V，依此类推直到 10 V。使用实际二极管时损失两次 $U_\mathrm F$：终值为 $2U_\mathrm e-2U_\mathrm F=8.6$ V。**极限情况：**若输出端有电流，每个周期都缺少电荷，$U_\mathrm a$ 就低于终值。

:::aufgabe 练习 11 ★★ 电源
<span class="anker" id="aufg-11"></span>

一个电桥接在 $\hat u=24$ V 上，$U_\mathrm F=0.7$ V。

<ol class="al">

<li>

$u_\mathrm a$ 的峰值是多少？每个二极管必须承受多大的反向电压？

</li>

<li>

$u_\mathrm a=0$ 的时间占多大比例？

</li>

<li>

负载电流为 100 mA。多大的 $C$ 能把波动限制在 1 V？换成半波整流器时需要多大，为什么？

</li>

</ol>

:::loesung
(a) $24\,\mathrm{V}-1.4\,\mathrm{V}=22.6$ V，反向电压 $24\,\mathrm{V}-0.7\,\mathrm{V}=23.3$ V。 (b) $|\sin|<1.4/24$ 时 $u_\mathrm a=0$，即每个过零点前后各 3.34°，占时间的 $2\cdot3.34^\circ/180^\circ=3.7$ %。 (c) $C=I\,\Delta t/\Delta U=100\,\mathrm{mA}\cdot10\,\mathrm{ms}/1\,\mathrm{V}=1000$ µ F。半波整流器每 20 ms 才补充一次，所以需要 2000 µ F。
:::
:::

:::aufgabe 练习 12 ★★ 数泵送次数
<span class="anker" id="aufg-12"></span>

$U_\mathrm e=3$ V，$C_1=C_2$，理想二极管。

<ol class="al">

<li>

1、2 和 3 个周期后 $U_\mathrm a$ 是多少？

</li>

<li>

多少个周期后达到终值的 99 %？

</li>

<li>

0.7 V 的实际二极管给出什么终值？$U_\mathrm e=1.5$ V 时还剩多少，这对低电压电路意味着什么？

</li>

</ol>

:::loesung
(a) $U_\mathrm a(k)=6\,\mathrm{V}-3\,\mathrm{V}\cdot2^{-k}$：4.5 V、5.25 V、5.63 V。 (b) $3\,\mathrm{V}\cdot2^{-k}\le0.06\,\mathrm{V}$ 要求 $2^k\ge50$，所以 $k=6$。 (c) $6\,\mathrm{V}-1.4\,\mathrm{V}=4.6$ V。在 1.5 V 时只剩 $3\,\mathrm{V}-1.4\,\mathrm{V}=1.6$ V，几乎不比输入高。因此在低电压下要用开关代替二极管。
:::
:::
