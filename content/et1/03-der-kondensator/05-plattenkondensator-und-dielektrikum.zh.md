---
title: 第 4 阶段：平行板电容器与电介质
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电容器
order: 1130500
summary: C 的值从何而来？对于两块平的极板，它由面积、间距和中间的材料决定。本阶段推导这个公式，并说明绝缘体的作用。
tags: 极化, 束缚电荷, 介电常数, 相对介电常数, 击穿, 位移电流
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
$C$ 的值从何而来？对于两块平的极板，它由面积、间距和中间的材料决定。本阶段推导这个公式，并说明绝缘体的作用。
:::

**基本思路。** 电压 $U$ 和间距 $d$ 固定时，电场 $E=U/d$ 也就确定了（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。电场表示电场线的疏密，而每条线都从一个电荷出发。因此单位面积的电荷也确定了。所以面积加倍意味着电荷加倍。间距减半意味着电场加倍，从而单位面积的电荷加倍。

绝缘体还能进一步提高电容。它的电子虽然仍留在各自的原子中，但电场使每个原子或分子中的正电荷相对于负电荷移动一小段距离。这种移动称为__极化__。在内部，相邻的两端相互抵消；在表面则留下__束缚电荷__，在正极板对面为负（图 [4](#abb-4) 右）。一部分电场线终止于这些电荷，极板之间的电场本会减弱。但电池把 $U$ 从而把 $E$ 固定住，于是它继续补充电荷，直到电场恢复原值。在相同电压下，极板上的电荷更多。

:::abbildung et1/k3platte 4
相同的电压，相同的间距，相同的电场。左，空气：每条电场线都从一块极板通到另一块极板，$A$ 是一块极板的面积。右，$\varepsilon_\mathrm{r}=2$ 的电介质：分子排列整齐，内部两端抵消，边缘留下束缚电荷。一半的线终止于那里。因此极板带有两倍的电荷。
:::

:::satz 定理 4.1 (平行板电容器)
<span class="anker" id="satz-4-1"></span>

对于面积为 $A$、间距为 $d$ 的两块平的极板，电介质充满其间时有

<span class="anker" id="gl-4-1"></span>
$$C=\varepsilon\,\frac{A}{d},\qquad\varepsilon=\varepsilon_0\,\varepsilon_\mathrm{r},\qquad\varepsilon_0=8.854\cdot10^{-12}\,\frac{\mathrm{A\,s}}{\mathrm{V\,m}}. \tag{4.1}$$
:::

⁠**如何理解：**面积 $A$ 越大（单位为 m$^2$；斜体 $A$ 不是第 [1](warum-strom-in-einen-isolator-fliet.html#stufe-1) 阶段的极板 A）、间距 $d$ 越小（单位为 m）、$\varepsilon$ 越大，$C$ 就越大。$\varepsilon_0$ 是[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)的真空介电常数。$\varepsilon$ 称为__介电常数__，纯数 $\varepsilon_\mathrm{r}$ 称为__相对介电常数__，它表示材料使电容比真空时增大的倍数。空气按 1 计算，误差为 0.06 %。**适用条件：**$d$ 必须远小于极板宽度。否则边缘处的边缘场（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）不可忽略；在间距 3 mm、宽 10 cm 的平行极板中，它使 $C$ 增大约 10 %。作粗略估算时，式 [(4.1)](#gl-4-1) 已经够用。

| 材料 | 空气 | 纸 | 云母 | 瓷 | 水 | 电容器陶瓷 |
|---|---|---|---|---|---|---|
| $\varepsilon_\mathrm{r}$ | 1 | $\approx2$ | $\approx5$ | $\approx6$ | $\approx81$ | 60 到 3000 |

:::herleitung 从电场线图像到公式
点电荷产生的电场为 $E=\frac{Q}{4\pi\varepsilon_0r^2}=\frac{Q}{\varepsilon_0\cdot4\pi r^2}$。分母中是球面面积，它的所有电场线都穿过这个球面。因此根据[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)：电场强度等于电荷除以 $\varepsilon_0$，再除以电场线均匀穿过的面积。在平行极板中，电荷 $Q$ 的所有电场线都平行地穿过面积 $A$：

$$E=\frac{Q}{\varepsilon_0\,A},\qquad U=E\,d=\frac{Q\,d}{\varepsilon_0\,A}\quad\Longrightarrow\quad C=\frac QU=\varepsilon_0\,\frac Ad.$$

有电介质时，一部分电场线终止于束缚电荷 $Q_\mathrm{g}$，穿过空间的只有 $Q-Q_\mathrm{g}$ 这一部分。在大多数绝缘体中，这一部分是 $Q$ 的固定比例。记作 $Q-Q_\mathrm{g}=Q/\varepsilon_\mathrm{r}$，由此得 $E=Q/(\varepsilon_\mathrm{r}\varepsilon_0A)$，从而得到式 [(4.1)](#gl-4-1)。
:::

::::beispiel
平行极板的电容为 $C=8.854\cdot10^{-12}\,\mathrm{F/m}\cdot0.01\,\mathrm{m^2}/0.003\,\mathrm{m}=29.5$ pF。若用 $\varepsilon_\mathrm{r}=1000$ 的陶瓷，就是 29.5 nF。若要在 3 mm 空气间隙下达到 100 µF，所需面积为 $A=C\,d/\varepsilon_0=33\,900\,\mathrm{m^2}$，即 3.4 公顷。因此实际的电容器都采用薄层（第 [5](bauformen-und-selbstentladung.html#stufe-5) 阶段）。
::::

⁠**检验：**单位正确：$\frac{\mathrm{A\,s}}{\mathrm{V\,m}}\cdot\frac{\mathrm{m^2}}{\mathrm{m}}=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F$。**极限情况：**当 $d\to0$ 时 $C$ 将无限增大。阻止这一点的是__击穿__：在 $E_\mathrm{max}$ 时电介质变为导体，空气的击穿场强为 3 MV/m（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。因此薄层需要固体材料，每个电容器都有最高电压 $U_\mathrm{max}=E_\mathrm{max}\,d$。

:::zusatz 位移电流
利用 $u=E\,d$ 和式 [(4.1)](#gl-4-1)，式 [(3.1)](strom-und-spannung-am-kondensator.html#gl-3-1) 变为 $i=\varepsilon A\,\mathrm{d} E/\mathrm{d} t$。间隙中没有电荷流动，但那里的电场在变化，这种变化的大小恰好等于导线中的电流。麦克斯韦称之为__位移电流__。它在间隙中产生的磁场与导线中电流产生的磁场相同（全电流定律，[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。所以对磁场来说，回路是闭合的。
:::

:::frage 水的 $\varepsilon_\mathrm{r}=81$。为什么没有人造水电容器？
因为实际的水是导电的：溶解的离子在极板之间传导电流，电容器会立刻自行放电。电介质必须同时做到两件事：能极化，又能绝缘。水的 $\varepsilon_\mathrm{r}$ 高，是因为水分子本身的正负电荷中心就是分开的，并会在电场中定向排列。
:::

:::aufgabe 练习 4 ★★ 面积与最高电压
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

如果用 10 µm 厚、$\varepsilon_\mathrm{r}=3$ 的薄膜代替 3 mm 的空气隔开极板，100 µF 需要多大的 $A$？

</li>

<li>

这个面积的 5 cm 宽的带子有多长？

</li>

<li>

平行极板在空气中最高能承受多少电压？

</li>

</ol>

:::loesung
(a) $A=\dfrac{C\,d}{\varepsilon_0\varepsilon_\mathrm{r}}=\dfrac{10^{-4}\,\mathrm{F}\cdot10^{-5}\,\mathrm{m}}{3\cdot8.854\cdot10^{-12}\,\mathrm{F/m}}=37.6\,\mathrm{m^2}$。

(b) $37.6\,\mathrm{m^2}/0.05\,\mathrm{m}=753$ m。实际的卷绕长度更短，因为它们使用更薄的薄膜，并利用每个电极的两面。

(c) $U_\mathrm{max}=E_\mathrm{max}\,d=3\,\mathrm{MV/m}\cdot3\,\mathrm{mm}=9$ kV。
:::
:::

:::aufgabe 练习 5 ★★ 插入电介质
<span class="anker" id="aufg-5"></span>

平行极板接在 9 V 上。现在用 $\varepsilon_\mathrm{r}=4$ 的材料充满极板之间的空间。请先预测什么保持不变，然后再计算。

<ol class="al">

<li>

电池保持连接。$C$、$U$、$Q$ 和 $E$ 各是多少？

</li>

<li>

电池事先已断开。现在 $C$、$U$、$Q$ 和 $E$ 各是多少？

</li>

<li>

既然 $C$ 相同，为什么两种情况不同？

</li>

</ol>

:::loesung
两种情况下都有 $C=4\cdot29.5\,\mathrm{pF}=118$ pF。

(a) 电池把 $U=9$ V 固定住。于是 $E=U/d=3$ kV/m 不变，$Q=C\,U=1.06$ nC。电池补充了增加的电荷。

(b) 没有电池，就没有电荷能够流入，$Q=266$ pC 保持不变。于是 $U=Q/C=2.25$ V，$E=U/d=750$ V/m。

(c) 两种情况下被固定的量不同：有电池时是电压，没有电池时是电荷。电介质改变 $C$，另一个量按 $Q=CU$ 随之调整。
:::
:::
