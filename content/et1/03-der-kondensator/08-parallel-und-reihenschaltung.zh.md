---
title: 第 7 阶段：并联与串联
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电容器
order: 1130800
summary: 多个电容器可以当作一个来处理。问题只在于，电路使哪个量对所有电容器都相同。
tags: 孤岛
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
多个电容器可以当作一个来处理。问题只在于，电路使哪个量对所有电容器都相同。
:::

**基本思路。** ⁠**并联：**所有上极板接在一根导线上，所有下极板接在另一根导线上。没有电流的导线处处电位相同，因此所有电容器上的电压相同。电路相当于一块增大的极板，电荷相加。**串联：**$C_1$ 的下极板、$C_2$ 的上极板和它们之间的连接导线构成一个__孤岛__：通向这段导体的只有绝缘体（图 [7](#abb-7)）。电荷既进不去，也出不来。如果孤岛原来不带电，其电荷之和就保持为零：上极板的 $+Q$ 把 $-Q$ 吸引到孤岛上时，缺少的对应电荷必然以 $+Q$ 的形式到达下一块极板。所以所有电容器带相同的电荷，电压相加。电路相当于一个增大的间距。

:::abbildung et1/k3schaltungen 7
$C_1=100\,\mu\text{F}$ 和 $C_2=50\,\mu\text{F}$ 接在 9 V 上。并联：电压相同，电荷相加为 1350 µC。串联：电荷同为 300 µC，因为虚线框出的孤岛保持中性。较小的电容器得到较大的电压。
:::

:::satz 定理 7.1 (总电容)
<span class="anker" id="satz-7-1"></span>

对于 $n$ 个并联的电容器（左）和 $n$ 个串联且初始不带电的电容器（右），有

<span class="anker" id="gl-7-1"></span>
$$C_\mathrm{G}=\sum_{i=1}^nC_i,\qquad\qquad\frac{1}{C_\mathrm{G}}=\sum_{i=1}^n\frac{1}{C_i}. \tag{7.1}$$

两个电容器串联时，$C_\mathrm{G}=\dfrac{C_1C_2}{C_1+C_2}$，电压按 $U_1=U_\mathrm{G}\,\dfrac{C_2}{C_1+C_2}$ 分配。
:::

:::herleitung 总电容
⁠**并联。**电路的约束：对所有 $i$ 有 $U_i=U_\mathrm{G}$。单个电荷：$Q_i=C_iU_i=C_iU_\mathrm{G}$。总电荷：$Q_\mathrm{G}=\sum Q_i=U_\mathrm{G}\sum C_i$。由 $C_\mathrm{G}=Q_\mathrm{G}/U_\mathrm{G}$ 得左边的公式。

⁠**串联。**电路的约束：对所有 $i$ 有 $Q_i=Q_\mathrm{G}$。总电压：$U_\mathrm{G}=\sum U_i$。分电压：$U_i=Q_i/C_i=Q_\mathrm{G}/C_i$。因此 $U_\mathrm{G}=Q_\mathrm{G}\sum 1/C_i$，由 $U_\mathrm{G}=Q_\mathrm{G}/C_\mathrm{G}$ 得右边的公式。分压公式：$U_1=Q_\mathrm{G}/C_1=U_\mathrm{G}\,C_\mathrm{G}/C_1=U_\mathrm{G}\,C_2/(C_1+C_2)$。
:::

⁠**如何理解：**$C_\mathrm{G}$ 是这样一个单独电容器的电容：它在两个外部接线端上表现出相同的行为。并联时 $C_\mathrm{G}$ 大于每个单独的值，串联时小于最小的值。**适用条件：**右边的公式要求开始时孤岛不带电。否则孤岛上原有的电荷保持不变，$Q_i=Q_\mathrm{G}$ 只对新增的电荷成立。

::::beispiel
并联：$C_\mathrm{G}=150\,\mu\text{F}$，$Q_1=900\,\mu\text{C}$，$Q_2=450\,\mu\text{C}$。串联：$1/C_\mathrm{G}=1/(100\,\mu\text{F})+1/(50\,\mu\text{F})$，因此 $C_\mathrm{G}=33.3\,\mu\text{F}$。在 9 V 下 $Q=300\,\mu\text{C}$，$U_1=3$ V，$U_2=6$ V。
::::

⁠**极限情况：**当 $C_2\to\infty$ 时，串联的 $C_\mathrm{G}\to C_1$，极大的电容器相当于一根导线。当 $C_2\to0$ 时，串联的 $C_\mathrm{G}\to0$，间隙使电路断开，并联时则剩下 $C_1$。

:::frage 为什么这些公式恰好与电阻的相反？
电阻有 $u=R\,i$：串联时在相同电流下电压相加，所以 $R$ 相加。电容器有 $u=\frac1C\,q$：串联时在相同电荷下电压相加，所以 $1/C$ 相加。**简而言之：**对电容器来说，$1/C$ 扮演 $R$ 的角色。
:::

:::aufgabe 练习 8 ★★ 混合网络
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

10 µF 和 20 µF 的两个电容器并联，再与 60 µF 串联，整体接在 9 V 上。求 $C_\mathrm{G}$、总电荷、所有电压和所有单个电荷。

</li>

<li>

两个相同的电容器串联，各为 100 µF，最高电压 16 V。这一串的电容和最高电压是多少？

</li>

</ol>

:::loesung
(a) 并联：$10+20=30\,\mu\text{F}$。与 60 µF 串联：$C_\mathrm{G}=\frac{30\cdot60}{30+60}\,\mu\text{F}=20\,\mu\text{F}$。$Q=20\,\mu\text{F}\cdot9\,\mathrm{V}=180\,\mu\text{C}$。60 µF 电容器上：$180\,\mu\text{C}/60\,\mu\text{F}=3$ V。并联部分上：$180\,\mu\text{C}/30\,\mu\text{F}=6$ V，合计 9 V。电荷的分配：$10\,\mu\text{F}\cdot6\,\mathrm{V}=60\,\mu\text{C}$ 和 $20\,\mu\text{F}\cdot6\,\mathrm{V}=120\,\mu\text{C}$。

(b) $C_\mathrm{G}=50\,\mu\text{F}$。电容器相同时电压均分，因此各 16 V，合计 32 V。
:::
:::
