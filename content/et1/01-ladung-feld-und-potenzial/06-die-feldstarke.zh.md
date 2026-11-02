---
title: 第 4 阶段：电场强度
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电荷、电场与电位
order: 1110600
summary: 库仑定律给出了力，却没有说明力是怎样穿过空无一物的空间的。电场的概念回答了这个问题，并把原因和作用分开。
tags: 试探电荷, 电场强度
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
库仑定律给出了力，却没有说明力是怎样穿过空无一物的空间的。电场的概念回答了这个问题，并把原因和作用分开。
:::

**基本思路。** 不说“B 隔着 3 cm 吸引 A”，而是把过程分解开。第一：电荷 B 改变了它周围的空间，产生了电场。第二：电荷 A 在自身所在位置感受到电场，并在那里受力。电荷为什么会产生电场，无法归结为更简单的东西，这是一条基本定律。但这个图像解决了三个问题。**原因和作用被分开：**电场只取决于产生它的电荷，并对放入其中的任何电荷都适用。**多个电荷变得容易处理：**把它们的电场相加一次，之后每个位置只需用一个矢量计算。**作用需要时间：**移动 B 时，只有当电场的变化以光速到达 A 处，A 所受的力才会改变。跨越 3 cm 需要 100 ps，从太阳到地球需要 8.3 分钟。在这段时间里，变化存在于电场之中，可见电场不只是一种计算工具。

:::analogie
地球周围有重力场：在每个位置上，任何质量都受到力 $\vec F=m\,\vec g$。场 $\vec g$ 是单位质量所受的力，电场是单位电荷所受的力。这个比喻在两处不再成立：质量总是相互吸引，而且重力场无法屏蔽。
:::

:::definition 定义 4.1 (电场强度)
<span class="anker" id="satz-4-1"></span>

把一个小的__试探电荷__ $Q$ 放到某一位置，测量它所受的力 $\vec F$，则该处的__电场强度__为

<span class="anker" id="gl-4-1"></span>
$$\vec E:=\lim_{Q\to0}\frac{\vec F}{Q},\qquad\text{即}\quad\vec F=Q\cdot\vec E. \tag{4.1}$$

$\vec E$ 的方向就是正试探电荷受力的方向。电场给每个位置都指定这样一个矢量。
:::

⁠**如何理解：**单位为 $[E]=\mathrm{N/C}=\mathrm{m\,kg\,A^{-1}\,s^{-3}}=\mathrm{V/m}$，因为 $\mathrm V=\mathrm{J/C}=\mathrm{N\,m/C}$。负电荷受力的方向与 $\vec E$ 相反。典型值：载流导体中 0.1 V/m，晴天大气中 100 到 200 V/m，广播天线表面 1 到 1000 V/m，高压线处 $10^6$ V/m，电容器（由两块极板构成的元件，[第 3 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)）中 $10^6$ 到 $10^8$ V/m。在 $3\cdot10^6$ V/m 时空气被击穿，产生电火花。**适用条件：**极限 $Q\to0$ 是必要的，因为大的试探电荷会使产生电场的电荷移动，例如金属板中的自由电子。而要测量的是没有试探电荷时的电场。

:::satz 定理 4.2 (点电荷的电场)
<span class="anker" id="satz-4-2"></span>

点电荷 $Q_0$ 在距离 $r$ 处产生的电场为

<span class="anker" id="gl-4-2"></span>
$$\vec E=k\,\frac{Q_0}{r^2}\cdot\frac{\vec r}{r},\qquad E=k\,\frac{|Q_0|}{r^2}, \tag{4.2}$$

其中 $\vec r$ 由电荷指向该位置。多个电荷共同产生的电场是各电场之和：$\vec E=\sum_i\vec E_i$。
:::

:::herleitung 点电荷的电场
根据式 [(3.2)](die-kraft-zwischen-ladungen.html#gl-3-2)，试探电荷 $Q$ 受力 $\vec F=k\,Q\,Q_0/r^2\cdot\vec r/r$。除以 $Q$ 后 $Q$ 消失，结果只取决于 $Q_0$ 和位置。求和法则来自力的叠加。
:::

:::abbildung et1/k1feldpfeile 5
正、负点电荷周围的电场矢量。电场从正电荷出发，指向负电荷。箭头长度与 $1/r^2$ 成正比。
:::

**例。** 小球 B（$-20$ nC）在小球 A 处产生的电场为 $E=k\cdot20\,\mathrm{nC}/(3\,\mathrm{cm})^2=2.0\cdot10^5$ V/m，方向指向 B。A 所受的力为 $F=10\,\mathrm{nC}\cdot2.0\cdot10^5\,\mathrm{V/m}=2.0$ mN，与第 [3](die-kraft-zwischen-ladungen.html#stufe-3) 阶段相同。反过来，A 在 B 处只产生 $1.0\cdot10^5$ V/m，但那里的电荷是两倍：结果同样是 2.0 mN。

⁠**简而言之：**电荷所受的力等于其电荷乘以所在位置的电场。

⁠**极限情况：**$r\to\infty$ 时 $E\to0$。$r\to0$ 时 $E$ 将无限增大，这表明了点电荷模型的界限。

:::frage 电荷也感受到自身的电场吗？
$\vec F=Q\vec E$ 中只包含**其他**电荷的电场。静止的电荷对自身不施加力。
:::

:::aufgabe 练习 4 ★★ 两个电荷，一个无场点
<span class="anker" id="aufg-4"></span>

在 $x$ 轴上，$Q_1=+4$ nC 位于 $x=0$，$Q_2=+1$ nC 位于 $x=6$ cm。

<ol class="al">

<li>

计算 $x=3$ cm 处电场的大小和方向。电子在那里受到多大的力？

</li>

<li>

在两电荷之间，何处 $E=0$？

</li>

<li>

极限情况：$Q_2\to0$ 时这一点移向何处？这与单个电荷的电场相符吗？

</li>

</ol>

:::loesung
(a) $E_1=k\cdot4\,\mathrm{nC}/(3\,\mathrm{cm})^2=40.0$ kV/m，向右；$E_2=k\cdot1\,\mathrm{nC}/(3\,\mathrm{cm})^2=9.99$ kV/m，向左；合成 $E=30.0$ kV/m，向右。电子：$F=e\,E=4.8\cdot10^{-15}$ N，向左。

(b) $E=0$ 要求 $Q_1/x^2=Q_2/(a-x)^2$，其中 $a=6$ cm。由此得 $2/x=1/(a-x)$，即 $x=\frac23a=4$ cm。 (c) 一般地，$x=a/(1+\sqrt{Q_2/Q_1})$。$Q_2\to0$ 时 $x\to a$：这一点移到 $Q_2$ 所在位置并消失。单个电荷没有无场点。
:::
:::
