---
title: 第 7 阶段：线性等效电路
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 半导体与二极管
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: 第 9 章：半导体与二极管
order: 1190900
summary: 有多个二极管时，多个指数方程相互耦合，手工已无法求解。本阶段用线性部件代替二极管，并给出一种总是有效的方法。
tags: 理想二极管, 含正向电压的二极管, 正向电压
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
有多个二极管时，多个指数方程相互耦合，手工已无法求解。本阶段用线性部件代替二极管，并给出一种总是有效的方法。
:::

**基本思路。** 在三个十倍程的电流范围内，$U_\mathrm D$ 只变化 180 mV。因此特性曲线几乎是一个直角，元件几乎是一个开关。这个模型的代价是：必须知道每个二极管的开关状态。先假设，事后再检验。

:::abbildung et1/k9ersatz 9
左上：实际特性曲线（蓝）、理想二极管（绿）和 $U_\mathrm F=0.7$ V 的模型（红）。右上：两种模型在导通和截止状态下的等效电路。下：含两个二极管的例子及其结果。
:::

:::definition 定义 7.1 (两种二极管模型)
<span class="anker" id="satz-7-1"></span>

__理想二极管__：导通时为短路，截止时为开路。

<span class="anker" id="gl-7-1"></span>
$$I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=0,\qquad U_\mathrm D<0\ \Rightarrow\ I_\mathrm D=0. \tag{7.1}$$

__含正向电压的二极管__：导通时为电压源 $U_\mathrm F$，截止时为开路。

<span class="anker" id="gl-7-2"></span>
$$I_\mathrm D>0\ \Rightarrow\ U_\mathrm D=U_\mathrm F,\qquad U_\mathrm D<U_\mathrm F\ \Rightarrow\ I_\mathrm D=0. \tag{7.2}$$
:::

⁠**如何理解：**$U_\mathrm F$ 称为__正向电压__，也称正向压降。它既不像 $U_\mathrm{D0}$ 那样是材料值，也不是阈值，而是一个模型值：取预期电流下的电压。常用 0.6 V 或 0.7 V。模型二极管在 0.12 mA 时为 0.6 V，在 5.8 mA 时为 0.7 V。**适用条件：**在参考模型中，精确值为 $I=4.31$ mA。理想二极管给出 5.00 mA（偏大 16 %），$U_\mathrm F=0.7$ V 给出 4.30 mA（$-0.2$ %），$U_\mathrm F=0.6$ V 给出 4.40 mA（偏大 2 %）。只有当电路中的电压远大于 0.7 V 时，理想二极管才够用。

**方法。**

<ol>

<li>

为二极管选择等效电路。

</li>

<li>

合理假设哪个二极管导通，哪个截止。

</li>

<li>

替换二极管，计算所有电流和电压。

</li>

<li>

检验：导通的二极管需要 $I_\mathrm D>0$，截止的需要 $U_\mathrm D<U_\mathrm F$。若有矛盾，就换一个假设。

</li>

</ol>

$n$ 个二极管有 $2^n$ 种组合，所以好的初始假设很值得。看一看电位会有帮助。

::::beispiel
图 [9](#abb-9) 下方：5 V 和 2 V 各经 1 k$\Omega$ 和一个二极管向节点 X 供电，$R_3=2\,\mathrm{k\Omega}$ 从 X 接地。$U_\mathrm F=0.7$ V。

⁠**假设 1：两者都导通。**在 X 处的节点定律（[第 2 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）为 $(4.3\,\mathrm{V}-\varphi_\mathrm X)/R_1+(1.3\,\mathrm{V}-\varphi_\mathrm X)/R_2=\varphi_\mathrm X/R_3$。由此得 $\varphi_\mathrm X=2.24$ V，$I_\mathrm{D1}=2.06$ mA，$I_\mathrm{D2}=-0.94$ mA。负电流是矛盾。

⁠**假设 2：D$_1$ 导通，D$_2$ 截止。**于是 $I=(5\,\mathrm{V}-0.7\,\mathrm{V})/3\,\mathrm{k\Omega}=1.43$ mA，$\varphi_\mathrm X=2.87$ V。D$_2$ 上的电压为 $U_\mathrm{D2}=2\,\mathrm{V}-2.87\,\mathrm{V}=-0.87$ V。它小于 $U_\mathrm F$，没有矛盾。工作点为 D$_1$ (0.7 V | 1.43 mA) 和 D$_2$ ($-0.87$ V | 0)。完整仿真给出 2.89 V 和 1.45 mA。

⁠**看电位：**只有当 $\varphi_\mathrm X<2\,\mathrm{V}-0.7\,\mathrm{V}=1.3$ V 时，D$_2$ 才导通。仅 5 V 电源就把 X 抬到 2.87 V，因此 D$_2$ 的阴极高于阳极。较高的电压占了上风。假设 3（只有 D$_2$ 导通）会给出 $U_\mathrm{D1}=4.13$ V，假设 4（两者都截止）给出 $U_\mathrm{D1}=5$ V，都大于 $U_\mathrm F$，因而都是矛盾。
::::

⁠**极限情况：**$U_2=5$ V 时两条支路相同，每个二极管各承担一半电流。

:::frage 为什么负电流是矛盾？电压源不是可以吸收电流吗？
等效电源可以，二极管不行：在反向只流过 $I_\mathrm S$。该模型只适用于 $I_\mathrm D>0$。负的结果说明计算在这个范围之外使用了二极管。
:::

:::aufgabe 练习 8 ★★ 谁占上风？
<span class="anker" id="aufg-8"></span>

在上例中，把 2 V 电源换成电源 $U_2$。

<ol class="al">

<li>

设 $U_2=4.5$ V。哪些二极管导通？计算 $\varphi_\mathrm X$ 和所有二极管电流。

</li>

<li>

$U_2$ 多大时 D$_2$ 开始导通？

</li>

</ol>

:::loesung
(a) 假设两者都导通。$(4.3\,\mathrm{V}-\varphi_\mathrm X)/R_1+(3.8\,\mathrm{V}-\varphi_\mathrm X)/R_2=\varphi_\mathrm X/R_3$ 给出 $\varphi_\mathrm X=3.24$ V，$I_\mathrm{D1}=1.06$ mA，$I_\mathrm{D2}=0.56$ mA。两者都为正，没有矛盾。检验：$1.62\,\mathrm{mA}\cdot2\,\mathrm{k\Omega}=3.24$ V。 (b) 只要 D$_2$ 截止，$\varphi_\mathrm X=2.87$ V。当 $U_2-0.7\,\mathrm{V}=2.87$ V，即 $U_2=3.57$ V 时，D$_2$ 开始导通。
:::
:::

:::aufgabe 练习 9 ★★★ 保护二极管
<span class="anker" id="aufg-9"></span>

芯片的输入端是节点 X。电压 $U_\mathrm e$ 经 $R=1\,\mathrm{k\Omega}$ 向它供电。D$_1$ 从 X（阳极）接到 $+5$ V 电源。D$_2$ 从接地点（阳极）接到 X。$U_\mathrm F=0.7$ V。

<ol class="al">

<li>

对 $U_\mathrm e=3$ V、$12$ V 和 $-3$ V，确定哪个二极管导通，并求 $\varphi_\mathrm X$ 和通过 $R$ 的电流。

</li>

<li>

画出 $\varphi_\mathrm X$ 随 $U_\mathrm e$ 的变化。

</li>

<li>

为什么不用计算就能排除四种组合中的一种？

</li>

</ol>

:::loesung
(a) $U_\mathrm e=3$ V：没有二极管导通，$I=0$，$\varphi_\mathrm X=3$ V。检验：$U_\mathrm{D1}=-2$ V，$U_\mathrm{D2}=-3$ V。$U_\mathrm e=12$ V：D$_1$ 导通，$\varphi_\mathrm X=5.7$ V，$I=6.3$ mA 流入电源。$U_\mathrm e=-3$ V：D$_2$ 导通，$\varphi_\mathrm X=-0.7$ V，$I=-2.3$ mA，电流来自接地点。 (b) 在 $-0.7$ V 和 5.7 V 之间是斜线 $\varphi_\mathrm X=U_\mathrm e$，此范围之外是水平线：输入端受到保护。 (c) 若两者都导通，$\varphi_\mathrm X$ 必须同时为 5.7 V 和 $-0.7$ V。
:::
:::
