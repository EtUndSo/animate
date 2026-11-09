---
title: 第 2 阶段：电容
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电容器
order: 1130300
summary: 一定的电压能在极板上维持多少电荷？答案是每个元件的一个数值。
tags: 
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
一定的电压能在极板上维持多少电荷？答案是每个元件的一个数值。
:::

**基本思路。** 如果两块极板上的电荷都加倍，每份电荷就贡献两倍的电场。根据[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)的叠加原理，电场在每一处都加倍，而形状不变（图 [2](#abb-2) 左）。电压是电场从一块极板到另一块极板的积分，所以也加倍。因此 $Q$ 与 $U$ 成正比。它们的比值与当前有多少电荷无关，只取决于形状、间距和材料。

:::definition 定义 2.1 (电容)
<span class="anker" id="satz-2-1"></span>

电容器的电容是电荷与电压之比：

<span class="anker" id="gl-2-1"></span>
$$C=\frac{Q}{U},\qquad Q=C\,U,\qquad[C]=\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm F\ \text{（法拉）}. \tag{2.1}$$
:::

⁠**如何理解：**$Q$ 是正极板上的电荷，单位为 C（库仑）；$U$ 是极板之间的电压，单位为 V；$C$ 是电容，单位为 F。1 F 时，一伏电压维持一库仑电荷。这是非常大的值。常见值为 fF、pF、nF 和 µF 量级，电解电容器可达 mF 量级。不要混淆符号：斜体 $C$ 是电容，正体 C 是库仑。**适用条件：**式 [(2.1)](#gl-2-1) 的前提是极板之间的材料不随电场变化。$\varepsilon_\mathrm{r}$ 很大的陶瓷（第 [4](plattenkondensator-und-dielektrikum.html#stufe-4) 阶段）在高电压下电容明显下降。

:::abbildung et1/k3qu 2
左：电荷加倍，电场线的密度加倍，电压也加倍。右：电荷随电压成正比增长，直线的斜率就是电容。圆点对应 9 V。
:::

::::beispiel
平行极板的电容为 $C=29.5$ pF（第 [4](plattenkondensator-und-dielektrikum.html#stufe-4) 阶段）。在 9 V 下它带电 $Q=29.5\,\mathrm{pF}\cdot9\,\mathrm{V}=266$ pC，即 $1.66\cdot10^{9}$ 个电子。这样面积、1 mm 厚的铜板含有 $8.5\cdot10^{23}$ 个自由电子。所以每 $5\cdot10^{14}$ 个电子中只有一个移动，而且它们都位于极板的内侧。金属几乎没有变化。RC 电路的电容器在 9 V 下带电 $Q=900\,\mu\text{C}$，是其 340 万倍。
::::

⁠**极限情况：**当 $U=0$ 时 $Q=0$：没有电压，就没有电荷分离。电荷相同时，较小的电容器显示较大的电压。

:::frage 电容听起来像容量。电容器会装满吗？
不是水桶那种意义上的装满。电压越高，电荷总是越多，$C$ 始终不变。极限由电介质决定：超过一定的电场强度，它就被击穿。本章中的“充满”只表示：电压已达到电源电压。
:::

:::aufgabe 练习 2 ★ 电荷与电压
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

一个 470 nF 的电容器接在 12 V 上。它的电荷是多少？

</li>

<li>

电压为多少时，它带电 1 µC？

</li>

<li>

电压减半。$Q$ 和 $C$ 会怎样？

</li>

<li>

10 µF 和 1 µF 的两个电容器各带电 50 µC。它们的电压各是多少？

</li>

</ol>

:::loesung
(a) $Q=470\,\mathrm{nF}\cdot12\,\mathrm{V}=5.64\,\mu\text{C}$。

(b) $U=Q/C=1\,\mu\text{C}/470\,\mathrm{nF}=2.13$ V。

(c) $Q$ 减半为 2.82 µC。$C$ 不变，因为它只取决于元件本身。

(d) $U=Q/C$：10 µF 电容器上为 5 V，1 µF 电容器上为 50 V。相同的电荷在较小的电容器上产生较大的电压。
:::
:::
