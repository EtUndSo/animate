---
title: 第 2 阶段：利用对称性
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电源与等效电源
order: 1150400
summary: 有些网络不含任何组。这时对称性给出等电位的节点，把它们连接起来就出现了组。
tags: 半电路
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
有些网络不含任何组。这时对称性给出等电位的节点，把它们连接起来就出现了组。
:::

**基本思路。** 如果两个节点电位相同，它们之间的电压就为零。因此它们之间的导线不通过电流，加上这根导线什么也不会改变。反过来，无电流的支路可以断开。对称性不需要任何计算就能告诉我们这些节点是哪些。

:::satz 定理 2.1 (两条对称规则)
<span class="anker" id="satz-2-1"></span>

对于接线端为 A 和 B 的电阻网络：

<ol>

<li>

如果网络经镜像或旋转后与自身重合，且 A 和 B 保持不动，那么重合在一起的节点电位相同。可以把它们连接起来。它们之间的电阻不通过电流。

</li>

<li>

如果网络经镜像后与自身重合，且 A 和 B 互换位置，那么对称轴上的每一点都处于平均值 $\frac12(\varphi_\mathrm{A}+\varphi_\mathrm{B})$。可以把这些点全部连接起来，只计算一侧，即__半电路__：

<span class="anker" id="gl-2-1"></span>
$$R_\mathrm{AB}=2\,R_\mathrm{A,axis}. \tag{2.1}$$

</li>

</ol>
:::

⁠**如何理解：**$R_\mathrm{A,axis}$ 是 A 与连成一个节点的对称轴之间的电阻。跨过对称轴的电阻分成两个一半大小的电阻，其中点在轴上。沿着对称轴的电阻两端电位相同，不通过电流。**适用条件：**对称性也必须包括数值。只要有一个电阻不同，对称性就被破坏了。

:::herleitung 电位由对称性得出
规则 1：镜像后的网络有相同的元件、相同的接线端和相同的电压，因而有相同的方程。这些方程只有唯一解。因此重合的两个节点必须电位相同。

规则 2：取中点为参考点，即 $\varphi_\mathrm{A}=+\frac12U$，$\varphi_\mathrm{B}=-\frac12U$。镜像使 A 和 B 互换，作用相当于把电压反接。在线性网络中，反接使每个电位变号（第 [8](uberlagerung.html#stufe-8) 阶段）。因此对点 $P$ 及其镜像 $P'$ 有 $\varphi(P')=-\varphi(P)$。轴上的点是它自身的镜像，所以 $\varphi=-\varphi$，从而 $\varphi=0$，即平均值。两半相同且串联，由此得到式 [(2.1)](#gl-2-1)。
:::

:::abbildung et1/k5symmetrie 2
七个相同的电阻，每个 14 $\Omega$。左：A 上加 16 V 时带有各点电位的网络。对称轴经过 L 和 E、F 之间电阻的中点，因此该电阻分成两个 7 $\Omega$。右：半电路。
:::

**例。** 在图 [2](#abb-2) 中，镜像使 A 与 B、E 与 F 互换，规则 2 适用。在半电路中，E 与对称轴之间是 $14\,\Omega\parallel7\,\Omega=4.67\,\Omega$。加上从 A 到 E 的一段，共 18.67 $\Omega$。与左支路并联得 $R_\mathrm{A,axis}=14\,\Omega\parallel18.67\,\Omega=8\,\Omega$，所以 $R_\mathrm{AB}=16\,\Omega$，又是参考模型中的负载。**检验**（用图中的电位）：从 A 到 L 的电流为 $8\,\mathrm{V}/14\,\Omega=0.571$ A，从 A 到 E 的电流为 $6\,\mathrm{V}/14\,\Omega=0.429$ A。两者之和为 1 A，正如 $16\,\mathrm{V}/16\,\Omega$ 所要求的。

:::abbildung et1/k5wuerfel 3
由十二个相同电阻组成的立方体，电压加在体对角线上。绕这条对角线旋转时，A 的三个相邻顶点彼此重合，B 的三个相邻顶点也是如此。连接之后得到由三个组构成的链。
:::

**电阻立方体。** 十二条棱，每条 $R=12\,\Omega$，接线端位于相对的两个顶点（图 [3](#abb-3)）。根据规则 1，A 的三个相邻顶点电位相同，B 的三个相邻顶点也是如此。这两组三点之间有六条棱。于是得到一条链：

$$R_\mathrm{AB}=\frac R3+\frac R6+\frac R3=\frac56R=10\,\Omega.$$

加 5 V 时电流为 0.5 A。它先分到三条棱上，每条 167 mA，再分到六条棱上，每条 83 mA，然后又分到三条棱上。

:::frage 连接这些点不是对电路的改动吗？
对图纸是改动，对电流不是。只有新导线两端之间有电压，其中才可能有电流。而这个电压并不存在。因此网络其余部分的电流都不改变。这种方法只有在电位确实相等时才成立。
:::

:::aufgabe 练习 2 ★ 预测无电流
<span class="anker" id="aufg-2"></span>

从 A 经 10 $\Omega$ 到节点 C，经 30 $\Omega$ 到节点 D；从 C 经 20 $\Omega$、从 D 经 60 $\Omega$ 到 B。C 和 D 之间接跨接电阻 $R_\mathrm{Q}$（[第 4 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)的电桥）。(a) 证明即使没有对称性，C 和 D 的电位也相同。(b) 计算 $R_\mathrm{Q}\to\infty$ 和 $R_\mathrm{Q}\to0$ 时的 $R_\mathrm{AB}$。(c) 对 $R_\mathrm{Q}=47\,\Omega$ 可得出什么结论？

:::loesung
(a) $R_\mathrm{Q}$ 中无电流时，两条支路都是比例相同的分压器：$\frac{20}{10+20}=\frac{60}{30+60}=\frac23$。这时 C 和 D 电位相同，$R_\mathrm{Q}$ 中确实没有电流。这就是该网络的唯一解（[第 4 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)的电桥平衡）。

(b) $R_\mathrm{Q}\to\infty$：$(10\,\Omega+20\,\Omega)\parallel(30\,\Omega+60\,\Omega)=22.5\,\Omega$。$R_\mathrm{Q}\to0$：$10\,\Omega\parallel30\,\Omega+20\,\Omega\parallel60\,\Omega=7.5\,\Omega+15\,\Omega=22.5\,\Omega$。

(c) 相同：22.5 $\Omega$。跨接电阻中无电流，其数值不起作用。
:::
:::

:::aufgabe 练习 3 ★★ 沿面对角线的立方体
<span class="anker" id="aufg-3"></span>

把电压加在立方体同一面上对角相对的两个顶点上，$R=12\,\Omega$。提示：两条规则都有帮助。哪四个顶点处于平均值？计算 $R_\mathrm{AB}$。

:::loesung
设接线端为 A 和 B。C 和 D 是同时与 A、B 相邻的两个顶点。在另一个面上，C、D 上方是 E、F，A 上方是 P，B 上方是 Q。以垂直于连线 AB 并经过其中点的平面作镜像，A 与 B 互换，P 与 Q 也互换。C、D、E、F 都在这个平面上，所以根据规则 2 它们处于平均值。

从 A 到对称轴的半电路：经 C 和经 D 各为 $R$，合为 $\frac R2$。经 P：先是 $R$，然后从 P 到 E 和到 F 各为 $R$，合为 $R+\frac R2=\frac32R$。并联：$\frac R2\parallel\frac32R=\frac38R$。因此 $R_\mathrm{AB}=\frac34R=9\,\Omega$。
:::
:::
