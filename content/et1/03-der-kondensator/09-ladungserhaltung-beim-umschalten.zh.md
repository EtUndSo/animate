---
title: 第 8 阶段：切换时的电荷守恒
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电容器
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: 第 3 章：电容器
order: 1130900
summary: 切换已充电的电容器时，无需计算电流就能求出新的电压。只要数电荷就够了。
tags: 
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
切换已充电的电容器时，无需计算电流就能求出新的电压。只要数电荷就够了。
:::

**基本思路。** 在封闭系统中，电荷之和保持不变（[第 1 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。在电路中，如果从一个节点到接地点的每条路径都经过电容器，就形成这样的系统。这就是第 [7](parallel-und-reihenschaltung.html#stufe-7) 阶段的孤岛：电介质阻断了所有通路。电荷可以在孤岛内重新分布，但不能离开它。比较前后两种状态时，无需知道均衡过程是如何进行的。

:::satz 定理 8.1 (孤岛上的电荷守恒)
<span class="anker" id="satz-8-1"></span>

如果从一个节点到接地点的每条路径都经过电容，则相连极板上的电荷之和保持不变：

<span class="anker" id="gl-8-1"></span>
$$Q_\mathrm{tot}=\sum_iC_iU_i=\text{const}. \tag{8.1}$$
:::

⁠**如何理解：**$U_i$ 是节点到对面极板的电压，因此 $C_iU_i$ 是节点处极板上的电荷，带符号。这个比较在两个静止状态之间成立，电压由 $Q=C\,U$ 求得。**适用条件：**节点上不得有通向外部的电阻或电源，而且均衡过程必须远快于自放电。

:::abbildung et1/k3umladen 8
位置 1：$C_1$ 充电到 9 V，$C_2$ 是空的。位置 2：虚线孤岛包含两个电容器的上极板。这 900 µC 重新分布，直到两个电压相等。
:::

::::beispiel
在图 [8](#abb-8) 中，位置 1 时 $C_1$ 带电荷 $C_1U_0=900\,\mu\text{C}$，$C_2$ 是空的。开关转到位置 2。现在两块上极板接在同一根导线上，所以均衡之后电压同为 $U$。由式 [(8.1)](#gl-8-1) 得

<span class="anker" id="gl-8-2"></span>
$$C_1U+C_2U=C_1U_0\quad\Longrightarrow\quad U=U_0\,\frac{C_1}{C_1+C_2}=9\,\mathrm{V}\cdot\frac{100}{150}=6\,\mathrm{V}. \tag{8.2}$$

之后 $C_1$ 还带 600 µC，$C_2$ 得到了 300 µC。
::::

**能量并不守恒。** 之前储存 $\frac12C_1U_0^2=4.05$ mJ，之后为 $\frac12(C_1+C_2)U^2=2.70$ mJ。少了 1.35 mJ，即三分之一。均衡电流使导线和开关发热。损耗与它们的电阻无关：电阻越小，电流越大，但时间越短，两者恰好抵消。一般地，两个电压 $U_1$ 和 $U_2$ 均衡时的损耗为：

<span class="anker" id="gl-8-3"></span>
$$W_\mathrm{V}=\frac12\,\frac{C_1C_2}{C_1+C_2}\,(U_1-U_2)^2. \tag{8.3}$$

:::herleitung 均衡时的损耗
由式 [(8.1)](#gl-8-1) 得 $U=\frac{C_1U_1+C_2U_2}{C_1+C_2}$，于是

$$W_\mathrm{V}=\tfrac12C_1U_1^2+\tfrac12C_2U_2^2-\tfrac12\,\frac{(C_1U_1+C_2U_2)^2}{C_1+C_2}.$$

通分到公分母 $2(C_1+C_2)$ 后，$C_1^2U_1^2$ 和 $C_2^2U_2^2$ 相互抵消。分子中剩下 $C_1C_2(U_1^2-2U_1U_2+U_2^2)$，这就是式 [(8.3)](#gl-8-3)。
:::

⁠**极限情况：**当 $C_2\to0$ 时 $U=U_0$ 不变，没有损耗。当 $C_2\gg C_1$ 时 $U\to0$：电荷并没有消失，只是分布到一个极大的电容器上，几乎不剩电压。

:::frage 在位置 1 充电时电荷也在变化。为什么那里不守恒？
因为那里没有孤岛。节点通过电池直接接到接地点，这是一条没有电容的路径。电荷正是通过它流入的。守恒对整体总是成立的，但式 [(8.1)](#gl-8-1) 要求节点的所有通路都经过电介质。
:::

:::ltspice 通过电阻重新分配电荷
⁠**绘制：**`cap`，值为 `100u`，从 `a` 到接地点，初值 `IC=9`。`cap`，值为 `50u`，从 `b` 到接地点，初值 `IC=0`。`res`，值为 `{Rv}`，从 `a` 到 `b`。这个电阻代表导线和开关。

⁠**指令：**`.param Rv=10`、`.step param Rv list 1 10 100`、`.tran 0 100m 0 1u uic`，另外加 `.meas tran ua FIND V(a) AT=100m` 和 `.meas tran wr INTEG V(a,b)*I(R1)`。结果显示在 SPICE Error Log 中。

⁠**你会看到：**对全部三个电阻值，`ua` $=6$ V，`wr` $=1.35$ mJ，与式 [(8.2)](#gl-8-2) 和式 [(8.3)](#gl-8-3) 一致。变化的只是均衡的时间。在 $C_2$ 上设置 `IC=3`，并与练习 [9](#aufg-9)(a) 比较。
:::

:::aufgabe 练习 9 ★★ 预充电时的电荷重新分配
<span class="anker" id="aufg-9"></span>

$C_1=100\,\mu\text{F}$ 上有 9 V。然后接入已充电的 $C_2=50\,\mu\text{F}$。

<ol class="al">

<li>

$C_2$ 上有 $+3$ V，与 $C_1$ 同向。最终电压是多少？损失多少能量？

</li>

<li>

$C_2$ 上有 $-3$ V，即极性相反。现在最终电压和损耗是多少？

</li>

<li>

极限情况：$U_2=9$ V 时结果如何？为什么没有均衡电流？

</li>

</ol>

:::loesung
(a) $Q=100\,\mu\text{F}\cdot9\,\mathrm{V}+50\,\mu\text{F}\cdot3\,\mathrm{V}=1050\,\mu\text{C}$，$U=1050\,\mu\text{C}/150\,\mu\text{F}=7$ V。由式 [(8.3)](#gl-8-3) 得损耗：$\frac12\cdot33.3\,\mu\text{F}\cdot(9\,\mathrm{V}-3\,\mathrm{V})^2=0.60$ mJ。检验：之前 4.275 mJ，之后 3.675 mJ。

(b) $Q=900\,\mu\text{C}-150\,\mu\text{C}=750\,\mu\text{C}$，$U=5$ V。损耗：$\frac12\cdot33.3\,\mu\text{F}\cdot(12\,\mathrm{V})^2=2.40$ mJ。两电压之差是 12 V，不是 6 V。

(c) $U=9$ V，$W_\mathrm{V}=0$。两个节点已处于相同电位，因此没有什么能驱动电流。
:::
:::
