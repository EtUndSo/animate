---
title: 第 9 阶段：改进节点法
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 网孔电流法与节点电位法
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: 第 8 章：网孔电流法与节点电位法
order: 1181100
summary: 理想电压源没有电导，也没有电流源形式（第 5 章）。本阶段去掉最后这个限制。SPICE 就是这样计算每个电路的。
tags: 电流增益, 特征频率
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
理想电压源没有电导，也没有电流源形式（[第 5 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）。本阶段去掉最后这个限制。SPICE 就是这样计算每个电路的。
:::

**基本思路。** 电压源确定两个节点之间的电压。它的电流要由网络才能确定，所以是未知的。把它取作附加的未知量。附加的未知量需要附加的方程，而电源本身就提供了这个方程：电位差等于 $U_\mathrm q$。这样，每个电压源恰好带回一个网孔方程，其余一切仍是节点分析（图 [9](#abb-9)）。

:::abbildung et1/k8mna 9
改进节点法。$i$ 和 $k$ 之间的电源得到一个新列用于其电流 $I_V$（绿色），和一个新行用于其电压（红色）。$\mathbf Y$ 保持不变。
:::

:::satz 定理 9.1 (改进节点法，MNA)
<span class="anker" id="satz-9-1"></span>

除参考节点外有 $n$ 个节点、并在 $i$ 和 $k$ 之间有一个理想电压源的网络满足

<span class="anker" id="gl-9-1"></span>
$$\begin{pmatrix}\mathbf Y&\mathbf C\\\mathbf B&0\end{pmatrix}\begin{pmatrix}\mathbf U\\I_V\end{pmatrix}=\begin{pmatrix}\mathbf I_\mathrm q\\U_\mathrm q\end{pmatrix}. \tag{9.1}$$

$\mathbf C$ 是新列，第 $i$ 行为 $+1$，第 $k$ 行为 $-1$。$\mathbf B$ 是新行，第 $i$ 列为 $+1$，第 $k$ 列为 $-1$。$I_V$ 从 $i$ 经电源到 $k$ 计数。新行为

<span class="anker" id="gl-9-2"></span>
$$U_i-U_k=U_\mathrm q. \tag{9.2}$$

每增加一个电压源，就增加一行和一列。
:::

⁠**如何理解：**$I_V$ 在 $i$ 处流出，在 $k$ 处流入，所以它在第 $i$ 行为 $+1$，在第 $k$ 行为 $-1$，就像电导的流出电流一样。电源输出功率时，其电流在电源内部从负极流向正极，$I_V$ 为负。这正是 SPICE 显示的 `I(V1)`。这些 1 没有单位，新行以伏特计算，新列以安培计算。**适用条件：**现在对角线上有一个零，但只要网络是确定的，方程组仍然可解。两个理想电源并联就不是确定的。**简而言之：**每个网络元件都有自己的印记，所有印记都可以彼此独立地填入。

::::beispiel SPICE 眼中的模型电路
SPICE 不做任何变换。电池是新节点 3 与接地点之间的理想电源 $U_\mathrm q$，其后是从 3 到 1 的 $R_1$。电流源和 $R_5$ 保持原样。未知量为 $U_1$、$U_2$、$U_3$ 和 $I_V$：

$$\begin{pmatrix}1.75&-0.5&-1&0\\-0.5&0.8&0&0\\-1&0&1&1\\0&0&1&0\end{pmatrix} \begin{pmatrix}U_1\\U_2\\U_3\\I_V\end{pmatrix}=\begin{pmatrix}0\\4\\0\\9\end{pmatrix}.$$

最后一行给出 $U_3=9$ V，于是前两行变成第 [5](das-knotenpotentialverfahren.html#stufe-5) 阶段的方程组：$U_1=8$ V，$U_2=10$ V。第三行给出 $I_V=G_1\,(U_1-U_3)=-1$ mA。这些就是两种方法的结果，完全不需要变换。
::::

⁠**极限情况：**$R_1\to0$ 时节点 3 变成节点 1。节点电位法在这里失效，MNA 则不然（练习 [11](#aufg-11)）。

:::ltspice SPICE 如何求解模型电路
⁠**绘制：**`voltage` 取 `9`，从 `3` 到接地点，`R1 1k` 从 `3` 到 `1`，`R2 4k` 从 `1` 到接地点，`R3 2k` 从 `1` 到 `2`，`R4 10k` 和 `R5 5k` 从 `2` 到接地点，`current` 取 `4m`，从接地点到 `2`。

⁠**指令：**`.op`，`.meas op u1 FIND V(1)`，`.meas op u2 FIND V(2)`，`.meas op u3 FIND V(3)`，`.meas op iv FIND I(V1)`。

⁠**你会看到：**$\mathtt{u1}=8$ V，$\mathtt{u2}=10$ V，$\mathtt{u3}=9$ V，$\mathtt{iv}=-1$ mA。这正是上面矩阵的四个未知量。`I(V1)` 从正接线端经电源到负接线端计数，与 $I_V$ 相同。然后按练习 [11](#aufg-11) 替换电池。
:::

**0 V 电源就是电流表。** $U_\mathrm q=0$ 的理想电压源相当于一根导线，但 MNA 能给出它的电流。这可用来测量__电流增益__。在放大器上，$I_\mathrm{in}$ 给带 $G_\mathrm i$ 的节点 1 供电，输出 2 经 0 V 电源接到接地点。设 $I_\mathrm{out}$ 从节点 2 经电源流到接地点，则

<span class="anker" id="gl-9-3"></span>
$$\begin{pmatrix}G_\mathrm i&0&0\\g&G_\mathrm o&1\\0&1&0\end{pmatrix}\begin{pmatrix}U_1\\U_2\\I_\mathrm{out}\end{pmatrix}=\begin{pmatrix}I_\mathrm{in}\\0\\0\end{pmatrix},\qquad \frac{I_\mathrm{out}}{I_\mathrm{in}}=\frac{1}{I_\mathrm{in}}\cdot\frac{g\,I_\mathrm{in}}{-G_\mathrm i}=-\frac{g}{G_\mathrm i}. \tag{9.3}$$

模型中这个值为 $-100$。因为 $U_2=0$，$G_\mathrm o$ 中没有电流，全部受控电流都流过电流表。频率高时这个幅值下降。它降到 1 时的频率称为__特征频率__，表征晶体管的速度。

**接理想电源的放大器。** 如果输入端接理想电压 $U_\mathrm q$，计算比式 [(8.2)](gesteuerte-quellen-und-verstarker.html#gl-8-2) 更短。设 $I_V$ 从节点 1 经电源流到接地点，$G=G_\mathrm o+G_\mathrm L$，则

<span class="anker" id="gl-9-4"></span>
$$\begin{pmatrix}G_\mathrm i&0&1\\g&G&0\\1&0&0\end{pmatrix}\begin{pmatrix}U_\mathrm i\\U_\mathrm o\\I_V\end{pmatrix}=\begin{pmatrix}0\\0\\U_\mathrm q\end{pmatrix},\qquad A_u=\frac{U_\mathrm o}{U_\mathrm q}=\frac{1}{U_\mathrm q}\cdot\frac{g\,U_\mathrm q}{-G}=-\frac gG=-g\,R, \tag{9.4}$$

其中 $R=1/G$。这是几乎所有放大器中都会重复出现的基本结构：

<span class="anker" id="gl-9-5"></span>
$$\text{电压增益}=-\text{跨导}\cdot\text{负载电阻}. \tag{9.5}$$

负载电阻是输出节点上所有电阻的并联，模型中为 $20\,\mathrm{k\Omega}\parallel5\,\mathrm{k\Omega}=4\,\mathrm{k\Omega}$，所以 $A_u=-50\,\mathrm{mS}\cdot4\,\mathrm{k\Omega}=-200$。如果多个控制电压相同的电源共同馈入输出，它们的跨导相加。这条规则适合用于估算和检验计算。**极限情况：**无负载且 $G_\mathrm o\to0$ 时，$A_u$ 无限增大，实际上这时是电源电压起限制作用。

:::frage 既然 SPICE 本来就需要电压源，为什么不用网孔计算？
因为 MNA 只为每个电压源增加一行，而网孔必须先去搜索。网络通常只有很少的电压源和大量的元件。此外，这种扩展几乎不增大矩阵，矩阵仍然是稀疏的。
:::

:::aufgabe 练习 11 ★★★ 替换而不改变
<span class="anker" id="aufg-11"></span>

把模型电路中的电池和 $R_1$ 换成一个从节点 1 到接地点的 8 V 理想电源。

<ol class="al">

<li>

列出 $U_1$、$U_2$、$I_V$ 的 MNA 方程组，并用克莱姆法则求解。

</li>

<li>

为什么与原始网络相比，被替换支路之外什么都没有变？

</li>

<li>

现在理想电源提供 9 V。$U_2$ 和 $I_V$ 是多大？

</li>

</ol>

:::loesung
(a) 未知量为 $U_1$、$U_2$、$I_V$。剩下 $G_2$、$G_3$、$G_4$、$G_5$ 和电流源：

$$\begin{pmatrix}0.75&-0.5&1\\-0.5&0.8&0\\1&0&0\end{pmatrix}\begin{pmatrix}U_1\\U_2\\I_V\end{pmatrix}=\begin{pmatrix}0\\4\\8\end{pmatrix}.$$

$D=-0.8$，$D_1=-6.4$，$D_2=-8$，$D_3=0.8$。所以 $U_1=8$ V，$U_2=10$ V，$I_V=-1$ mA。

(b) 节点 1 原本就是 8 V，而该支路向节点送入 1 mA。恰好为这个电压的理想电源强制出同样的状态。网络的其余部分只感受到这个节点上的电压和电流。

(c) $U_1=9$ V。第 2 行：$U_2=(4+0.5\cdot9)/0.8=10.6$ V。第 1 行：$I_V=-0.75\cdot9+0.5\cdot10.625=-1.44$ mA。
:::
:::
