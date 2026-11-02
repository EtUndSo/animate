---
title: 第 6 阶段：电场中的功
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电荷、电场与电位
order: 1110800
summary: 电荷在电场中运动时，场力做功。本阶段计算这个功，并指出后面一切所依赖的性质：功与路径无关。
tags: 无旋, 静电场
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
电荷在电场中运动时，场力做功。本阶段计算这个功，并指出后面一切所依赖的性质：功与路径无关。
:::

**基本思路。** 电场中的电荷就像第 [1](groen-kraft-und-arbeit.html#stufe-1) 阶段的背包，只是力变成了 $Q\vec E$。正电荷沿电场方向运动时，电场把能量传给它。逆着电场运动时，必须由别的力做功，能量进入电场。垂直于电场运动时，什么也不发生。

:::satz 定理 6.1 (电场中的功)
<span class="anker" id="satz-6-1"></span>

电荷 $Q$ 从 $P_1$ 到 $P_2$ 时，电场对它做的功为

<span class="anker" id="gl-6-1"></span>
$$W_{12}=\int_{P_1}^{P_2}\vec F\cdot\mathrm{d}\vec s=Q\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s,\qquad\text{在均匀电场中}\quad W_{12}=Q\,E\,s\cos\alpha. \tag{6.1}$$

在静止电荷的电场中，$W_{12}$ 只取决于 $P_1$ 和 $P_2$，与路径无关。与此等价，沿任意闭合路径的积分为零，这样的电场是__无旋__的：

<span class="anker" id="gl-6-2"></span>
$$\oint_L\vec E\cdot\mathrm{d}\vec s=0. \tag{6.2}$$
:::

⁠**如何理解：**$Q$ 是运动电荷，带符号；$s$ 是与 $\vec E$ 成 $\alpha$ 角的直线路径的长度。积分号上的圆圈表示路径 $L$ 回到起点。$W_{12}>0$ 表示电场把能量传给电荷，能量被**释放**。$W_{12}<0$ 表示必须从外部提供 $W_\text{ext}=-W_{12}$，前提是电荷在此过程中既不加速也不减速。在 1 nC 和几伏的情况下，这是纳焦量级。**适用条件：**式 [(6.2)](#gl-6-2) 要求电荷静止且没有变化的磁场（第 [10](grenze-des-bildes-magnetismus-und-induktion.html#stufe-10) 阶段）。这样的电场称为__静电场__。

:::herleitung 为什么功与路径无关
⁠**一个点电荷。**设 $Q$ 在 $Q_0$ 的电场中从 $r_1$ 运动到 $r_2$。把路径分解为沿半径的小段和垂直于半径的小段。在垂直于半径的小段上，电场与路径垂直，只有距离的变化才起作用：

$$W_{12}=Q\int_{r_1}^{r_2}k\,\frac{Q_0}{r^2}\,\mathrm{d} r=k\,Q\,Q_0\Bigl(\frac{1}{r_1}-\frac{1}{r_2}\Bigr).$$

⁠**任意静止电荷。**任何这样的电场都是点电荷电场之和，功也是各部分功之和。

⁠**闭合路径。**若路径 $a$ 从 $P_1$ 到 $P_2$，路径 $b$ 返回，则把返回路径按相反方向看时符号改变：$\oint\vec E\cdot\mathrm{d}\vec s=\int_a\vec E\cdot\mathrm{d}\vec s-\int_{b,\,P_1\to P_2}\vec E\cdot\mathrm{d}\vec s=0$，因为两条路径给出相同的值。
:::

:::abbildung et1/k1feldarbeit 7
平行极板的局部，按比例绘制。试探电荷 $+1$ nC 沿三角形运动。从 1 到 2 获得 9 nJ。从 2 到 3 垂直于电场运动：不做功。从 3 到 1 失去 9 nJ。闭合路径的总和为零。
:::

**例。** 在图 [7](#abb-7) 中，$F=Q\,E=3$ µ N，沿 $x$ 方向，$W_{12}=10^{-9}\,\mathrm{C}\cdot3000\,\mathrm{V/m}\cdot3\,\mathrm{mm}=9$ nJ。从 1 直接到 3 的路径长 5 mm，$\cos\alpha=0.6$：同样是 9 nJ。在小球 A（$Q_0=+10$ nC）的电场中，$+1$ nC 从 3 cm 到 6 cm 获得的能量为 $k\cdot1\,\mathrm{nC}\cdot10\,\mathrm{nC}\cdot(1/r_1-1/r_2)=1.5$ µ J。

⁠**极限情况：**$\alpha=90^\circ$ 时和 $P_2=P_1$ 时 $W=0$。负电荷的符号相反：电子逆着 $\vec E$ 运动时获得能量。$r_2\to\infty$ 时 $W_{12}=kQQ_0/r_1$ 仍是有限值。

:::frage 去了再回来总是得零。这为什么算是一个特别的结论？
沿同一条路径往返，这对任何力场都成立。式 [(6.2)](#gl-6-2) 更强：即使回程走另一条路径，它也成立。否则就可以让电荷绕圈，每转一圈都获得能量。
:::

:::aufgabe 练习 6 ★★ 电场中的路径
<span class="anker" id="aufg-6"></span>

在沿 $x$ 方向的均匀电场 $E=3$ kV/m 中，$Q=+2$ nC 从 $P_1=(0;\,0)$ 运动到 $P_2=(2\,\mathrm{mm};\,1.5\,\mathrm{mm})$。

<ol class="al">

<li>

计算沿直线路径的 $W_{12}$。

</li>

<li>

计算绕行路径（先沿 $y$ 方向，再沿 $x$ 方向）的 $W_{12}$。

</li>

<li>

$Q=-2$ nC 时有什么变化？

</li>

</ol>

:::loesung
(a) 长度 $s=\sqrt{2^2+1.5^2}\,\mathrm{mm}=2.5$ mm，$\cos\alpha=0.8$：$W_{12}=2\,\mathrm{nC}\cdot3000\,\mathrm{V/m}\cdot2.5\,\mathrm{mm}\cdot0.8=12$ nJ。 (b) 沿 $y$ 方向时路径垂直于 $\vec E$：0。沿 $x$ 方向：$2\,\mathrm{nC}\cdot3000\,\mathrm{V/m}\cdot2\,\mathrm{mm}=12$ nJ。 (c) $W_{12}=-12$ nJ，必须从外部提供 12 nJ。
:::
:::
