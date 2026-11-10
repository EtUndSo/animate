---
title: 第 7 阶段：印记与网表
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 网孔电流法与节点电位法
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: 第 8 章：网孔电流法与节点电位法
order: 1180900
summary: 程序看不到网孔，也不做变形。本阶段说明，矩阵如何逐个元件地形成，而无需任何元件了解其他元件。
tags: 印记, 网表, 稀疏
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
程序看不到网孔，也不做变形。本阶段说明，矩阵如何逐个元件地形成，而无需任何元件了解其他元件。
:::

**基本思路。** 一个元件只接触它的两个节点。因此它的电流恰好出现在两个节点方程中，一个带正号，另一个带负号。所以每个元件都有固定的填写模式，即它的__印记__（图 [7](#abb-7)）。从全零矩阵开始，逐个元件加上它的印记。顺序无关紧要。

:::abbildung et1/k8stempel 7
节点的行和列中的填写模式。左：$i$ 和 $k$ 之间的电导 $G$。中：把 $I_\mathrm q$ 从 $k$ 推向 $i$ 的固定电流源，它只填在右端。右：从 $i$ 到 $k$ 的电压控制电流源 $g\,U_{pq}$。它位于第 $i$、$k$ 行，但位于第 $p$、$q$ 列（第 [8](gesteuerte-quellen-und-verstarker.html#stufe-8) 阶段）。
:::

:::satz 定理 7.1 (电导和电流源的印记)
<span class="anker" id="satz-7-1"></span>

每一行都是节点定律“流出的电流 = 注入的电流”。

<ul>

<li>

$i$ 和 $k$ 之间的电导 $G$ 从 $i$ 到 $k$ 流过电流 $I_Y=G\,(U_i-U_k)$。它在位置 $(i,i)$ 和 $(k,k)$ 上加 $+G$，在 $(i,k)$ 和 $(k,i)$ 上加 $-G$。

</li>

<li>

把 $I_\mathrm q$ 经自身从 $k$ 推向 $i$ 的固定电流源，在右端的第 $i$ 行加 $+I_\mathrm q$，在第 $k$ 行加 $-I_\mathrm q$。它不填入 $\mathbf Y$，因为它的电流不取决于任何电压。

</li>

</ul>
:::

⁠**如何理解：**首先，$k$ 个节点各得到一行和一列，参考节点也不例外。这个完整矩阵的行列式为零，因为所有行的和都为零：把所有电位一起抬高，任何地方都不会多出电流。从物理上说，网络只确定差值。只有规定 $U_0=0$ 才使解唯一：划去第 0 列，因为它的未知量为零；划去第 0 行，因为它可由其余节点定律得出（[第 2 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。剩下的就是第 [5](das-knotenpotentialverfahren.html#stufe-5) 阶段的 $\mathbf Y$。**适用条件：**这些印记适用于线性元件。电压源见第 [9](die-modifizierte-knotenanalyse.html#stufe-9) 阶段。

**网表。** 电路图以__网表__的形式保存：每个元件一行，包括名称、节点和数值。在 SPICE 中，`R3 1 2 2k` 表示：节点 1 和 2 之间的电阻。`I2 0 2 4m` 表示：4 mA 经电源从节点 0 流向节点 2。程序逐行读取列表并填入印记。出现新的节点名时，矩阵就增加一行一列。谁也不必事先知道它的大小。这种死板的格式源于 20 世纪 70 年代，当时 SPICE 用 FORTRAN 编写，每行占一张穿孔卡片。

::::beispiel
电池已变换的模型电路给出这张列表：

| 行 | 数值 | 填写 |
|---|---|---|
| `R1 1 0 1k` | $G_1=1$ | $+1$ 加在 $(1,1)$、$(0,0)$；$-1$ 加在 $(1,0)$、$(0,1)$ |
| `R2 1 0 4k` | $G_2=0.25$ | $+0.25$ 加在 $(1,1)$、$(0,0)$；$-0.25$ 加在 $(1,0)$、$(0,1)$ |
| `R3 1 2 2k` | $G_3=0.5$ | $+0.5$ 加在 $(1,1)$、$(2,2)$；$-0.5$ 加在 $(1,2)$、$(2,1)$ |
| `R4 2 0 10k` | $G_4=0.1$ | $+0.1$ 加在 $(2,2)$、$(0,0)$；$-0.1$ 加在 $(2,0)$、$(0,2)$ |
| `R5 2 0 5k` | $G_5=0.2$ | $+0.2$ 加在 $(2,2)$、$(0,0)$；$-0.2$ 加在 $(2,0)$、$(0,2)$ |
| `I1 0 1 9m` | $I=9$ | 右端第 1 行 $+9$，第 0 行 $-9$ |
| `I2 0 2 4m` | $I=4$ | 右端第 2 行 $+4$，第 0 行 $-4$ |

行和列按 0、1、2 的顺序排列，得到

$$\begin{pmatrix}1.55&-1.25&-0.3\\-1.25&1.75&-0.5\\-0.3&-0.5&0.8\end{pmatrix} \begin{pmatrix}U_0\\U_1\\U_2\end{pmatrix}=\begin{pmatrix}-13\\9\\4\end{pmatrix}.$$

每行之和都为零。划去第 0 行和第 0 列，就剩下第 [5](das-knotenpotentialverfahren.html#stufe-5) 阶段的方程组。**检验：**在划去后的 $\mathbf Y$ 中，行和就是到接地点的电导：$1.75-0.5=1.25=G_1+G_2$，$0.8-0.5=0.3=G_4+G_5$。
::::

⁠**极限情况：**没有支路通向接地点的节点，其行和为零。

**大型网络。** 一个节点通常只连接两到五个相邻节点，所以大矩阵的几乎所有位置都是零。这样的矩阵称为__稀疏__矩阵。仿真器只存储非零元素，并通过逐步消元求解方程组。克莱姆法则在这里毫无用处：20 行的行列式按式 [(0.1)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-1) 的模式约有 $2.4\cdot10^{18}$ 个乘积。

:::zusatz 交流电、电容器、二极管
对正弦量要用复电导，即导纳来计算。字母 $Y$ 和 $Z$ 就来源于此。电容器的印记与电导相同。阻抗 $Z$ 只有不为零时才能以 $Y=1/Z$ 填入，线圈在频率为零时就不行了。第 [9](die-modifizierte-knotenanalyse.html#stufe-9) 阶段解决这个问题。对二极管（[第 9 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)）这样的非线性元件，仿真器用其特性曲线的切线代替，填入印记并反复进行，直到不再变化。
:::

:::frage 为什么偏偏可以划去参考节点的那一行？
$k$ 个节点方程中的每一个都可由其余方程得出（[第 2 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。划去哪一个都可以。划去参考节点的那一行，是因为连同它的列一起划去后又得到对称矩阵，而且流入接地点的电流很少令人关心。
:::

:::aufgabe 练习 9 ★★ 从网表到解
<span class="anker" id="aufg-9"></span>

给定列表 `R1 1 0 1k`，`R2 1 2 2k`，`R3 2 0 2k`，`I1 0 1 7m`，`I2 2 1 1m`。

<ol class="al">

<li>

填写完整的 $3\times3$ 矩阵和右端。检验行和。

</li>

<li>

划去参考节点并求解。

</li>

<li>

检验：经电阻流入接地点的电流是多少？从接地点流出的又是多少？

</li>

</ol>

:::loesung
(a) 电导为 1，0.5，0.5 mS，行为 0，1，2：

$$\begin{pmatrix}1.5&-1&-0.5\\-1&1.5&-0.5\\-0.5&-0.5&1\end{pmatrix}\begin{pmatrix}U_0\\U_1\\U_2\end{pmatrix}=\begin{pmatrix}-7\\8\\-1\end{pmatrix}.$$

`I2 2 1 1m` 把 1 mA 从 2 推向 1，所以第 1 行 $+1$，第 2 行 $-1$。所有行和都为零，右端之和也为零。

(b) $\begin{pmatrix}1.5&-0.5\\-0.5&1\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}8\\-1\end{pmatrix}$，$D=1.25$，$D_1=7.5$，$D_2=2.5$。所以 $U_1=6$ V，$U_2=2$ V。

(c) 经 `R1` 有 6 mA 流入接地点，经 `R3` 有 1 mA，共 7 mA。`I1` 恰好从接地点取走 7 mA。
:::
:::
