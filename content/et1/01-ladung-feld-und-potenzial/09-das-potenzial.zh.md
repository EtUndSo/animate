---
title: 第 7 阶段：电位
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电荷、电场与电位
order: 1110900
summary: 既然功只取决于起点和终点，每个位置有一个数就足以算出它。这个数就是电位。
tags: 等位面
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
既然功只取决于起点和终点，每个位置有一个数就足以算出它。这个数就是电位。
:::

**基本思路。** 选定一个参考点，在每个位置写上电场在从该处到参考点的路径上对单位电荷释放的功。除以电荷使这个数成为位置的性质。于是两个位置之间的功就是两个这样的数之差。

:::analogie
电位是地形的高度，电场是地形的坡度，正电荷是向山下滚的球。这个比喻对负电荷不再成立：它们在同样的地形上向山上滚。
:::

:::definition 定义 7.1 (电位)
<span class="anker" id="satz-7-1"></span>

在参考点为 $P_0$ 的静电场中，点 $P$ 的电位为

<span class="anker" id="gl-7-1"></span>
$$\varphi(P)=\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s=-\int_{P_0}^{P}\vec E\cdot\mathrm{d}\vec s,\qquad[\varphi]=\frac{\mathrm J}{\mathrm C}=\mathrm V. \tag{7.1}$$

电荷 $Q$ 在该处具有势能 $W_\mathrm{pot}=Q\,\varphi(P)$。
:::

:::satz 定理 7.2 (功是电位差，两种分布)
<span class="anker" id="satz-7-2"></span>

<span class="anker" id="gl-7-2"></span>
$$W_{12}=Q\,\bigl(\varphi(P_1)-\varphi(P_2)\bigr). \tag{7.2}$$

在沿 $x$ 方向的均匀电场中和点电荷 $Q_0$ 的电场中（参考点在无穷远处），有

<span class="anker" id="gl-7-3"></span>
$$\varphi(x)=\varphi(0)-E\,x,\qquad\varphi(r)=k\,\frac{Q_0}{r}. \tag{7.3}$$
:::

:::herleitung 功是电位差
由于功与路径无关，可以从 $P_1$ 经 $P_0$ 到 $P_2$：

$$\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=\int_{P_1}^{P_0}\vec E\cdot\mathrm{d}\vec s+\int_{P_0}^{P_2}\vec E\cdot\mathrm{d}\vec s=\varphi(P_1)-\varphi(P_2).$$

如果功与路径有关，$\varphi$ 甚至不是唯一确定的。分布式 [(7.3)](#gl-7-3) 由式 [(7.1)](#gl-7-1)（$E$ 恒定）以及第 [6](arbeit-im-feld.html#stufe-6) 阶段的推导（$r_2\to\infty$）得出。
:::

⁠**如何理解：**$\varphi$ 是每个位置的一个数，不是矢量。沿 $\vec E$ 的方向 $\varphi$ 下降，电场强度就是电位的坡度：$E_x=-\mathrm{d}\varphi/\mathrm{d} x$。把 $P_0$ 移到别处时，所有电位都改变相同的量。**适用条件：**电位以静电场为前提。

**等位面。** 电位相同的位置构成__等位面__。电荷在其上移动时不做功。由此可知，电场线垂直于等位面，否则沿面移动就会做功。在平行极板中，等位面是平行于极板的平面；在点电荷周围，等位面是球面。静止的金属体由于 $\vec E=0$，处处电位相同。

:::abbildung et1/k1potenzial 8
左：平行极板，参考点在极板 B 上。虚线是等位面的截面，相邻两条相差 3 V。右：电位沿 $x$ 从 9 V 降到 0 V，其斜率 $-3$ V/mm 等于 $-E$。
:::

**例。** 取 B 上 $\varphi=0$，则 A 为 9 V，且 $\varphi(x)=9\,\mathrm{V}-3\,\mathrm{kV/m}\cdot x$：1 mm 处为 6 V，2 mm 处为 3 V。小球 A（$+10$ nC）在 3 cm 处的电位为 3.0 kV，在 6 cm 处为 1.5 kV。两者之差乘以 1 nC，就得到第 [6](arbeit-im-feld.html#stufe-6) 阶段的 1.5 µ J。

⁠**简而言之：**电位是某一位置上单位电荷的能量，从参考点算起。

⁠**极限情况：**$r\to\infty$ 时 $\varphi\to0$，这就是所选的参考点。$E=0$ 时 $\varphi$ 为常数，但不一定为零。

:::frage 如果 $\varphi=0$，那里也就没有电场了，对吗？
不对。电场取决于坡度，而不是数值。极板 B 的 $\varphi=0$，紧贴它的地方却有完整的电场 3 kV/m。反过来，带电金属球内部 $E=0$，但其电位不为零。
:::

:::aufgabe 练习 7 ★★ 区分电位与电场
<span class="anker" id="aufg-7"></span>

在 $x$ 轴上，$Q_1=+4$ nC 位于 $x=0$，$Q_2=-1$ nC 位于 $x=6$ cm，参考点在无穷远处。

<ol class="al">

<li>

计算 $x=3$ cm 处的电位。为什么这里相加时不考虑方向？

</li>

<li>

在两电荷之间，何处 $\varphi=0$？那里的 $E$ 有多大？

</li>

</ol>

:::loesung
(a) 电位是数，带符号相加：$\varphi=k\,(4\,\mathrm{nC}-1\,\mathrm{nC})/3\,\mathrm{cm}=899$ V。 (b) $4/x-1/(6-x)=0$（$x$ 以 cm 为单位）得 $x=4.8$ cm。在该处两个电场都向右：$E=k\cdot4\,\mathrm{nC}/(4.8\,\mathrm{cm})^2+k\cdot1\,\mathrm{nC}/(1.2\,\mathrm{cm})^2=15.6\,\mathrm{kV/m}+62.4\,\mathrm{kV/m}=78.0$ kV/m。可见 $\varphi=0$ 并不意味着 $E=0$。
:::
:::
