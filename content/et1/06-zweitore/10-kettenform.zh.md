---
title: 第 8 阶段：链式形式
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 二端口网络
order: 1161000
summary: 二端口网络常常前后相接，一个的输出馈入下一个的输入。本阶段选择输出量作为原因，并由此得到矩阵乘积。
tags: A 参数, 级联
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
二端口网络常常前后相接，一个的输出馈入下一个的输入。本阶段选择输出量作为原因，并由此得到矩阵乘积。
:::

**基本思路。** 一个二端口网络接在另一个后面时，前者的输出量恰好是后者的输入量。如果一种形式用输出量描述输入量，就可以把它们串接起来：从负载出发，逐级往回算到电源。链式形式做的正是这件事。$I_2$ 前的负号就是它合适的原因：离开一个二端口网络的电流，正是流入下一个二端口网络的电流。

:::definition 定义 8.1 (链式形式，A 形式)
<span class="anker" id="satz-8-1"></span>

链式形式以 $U_2$ 和 $-I_2$ 为原因：

<span class="anker" id="gl-8-1"></span>
$$U_1=A_{11}U_2+A_{12}(-I_2),\quad I_1=A_{21}U_2+A_{22}(-I_2),\qquad\text{简写为}\quad \begin{pmatrix}U_1\\I_1\end{pmatrix}=\mathbf A\begin{pmatrix}U_2\\-I_2\end{pmatrix}. \tag{8.1}$$

__A 参数__由输出端的试验得到：

<span class="anker" id="gl-8-2"></span>
$$A_{11}=\left.\frac{U_1}{U_2}\right|_{I_2=0},\quad A_{21}=\left.\frac{I_1}{U_2}\right|_{I_2=0},\quad A_{12}=\left.-\frac{U_1}{I_2}\right|_{U_2=0},\quad A_{22}=\left.-\frac{I_1}{I_2}\right|_{U_2=0}. \tag{8.2}$$

两个二端口网络__级联__时，$\mathbf A=\mathbf A'\mathbf A''$。
:::

⁠**如何理解：**$A_{11}$ 是正向开路电压比的倒数，$A_{21}$ 是正向开路转移电导，$A_{12}$ 是正向短路转移电阻，$A_{22}$ 是正向短路电流比的倒数。倒数的意思是：输入比输出，即通常比值的倒数。$A_{11}$ 和 $A_{22}$ 无单位，$A_{12}$ 的单位是 $\Omega$，$A_{21}$ 的单位是 S。衰减器有 $A_{11}>1$。**适用条件：**级联要求顺序为 $\mathbf A'\mathbf A''$，电源在左边。

:::herleitung 为什么级联是矩阵乘积
一撇表示第一个二端口网络，两撇表示第二个。连接迫使 $U_2'=U_1''$，$-I_2'=I_1''$。代入：

$$\begin{pmatrix}U_1'\\I_1'\end{pmatrix}=\mathbf A'\begin{pmatrix}U_2'\\-I_2'\end{pmatrix}=\mathbf A'\begin{pmatrix}U_1''\\I_1''\end{pmatrix}=\mathbf A'\mathbf A''\begin{pmatrix}U_2''\\-I_2''\end{pmatrix}.$$
:::

:::abbildung et1/k6kette 10
上：两个二端口网络级联。第一个的输出和第二个的输入共享电压和电流。下：T 形网络作为三个基本二端口网络的级联：串联电阻、并联电导、串联电阻。
:::

::::beispiel
最简单的构件是串联电阻和并联电导。对串联电阻，$U_1=U_2+R(-I_2)$，$I_1=-I_2$；对并联电导，$U_1=U_2$，$I_1=G\,U_2+(-I_2)$：

$$\mathbf A_R=\begin{pmatrix}1&R\\0&1\end{pmatrix},\qquad \mathbf A_G=\begin{pmatrix}1&0\\G&1\end{pmatrix}.$$

T 形网络是 $R_\mathrm{a}$、$G_\mathrm{b}=1/R_\mathrm{b}=50$ mS 和 $R_\mathrm{c}$ 的级联（图 [10](#abb-10) 下）：

$$\mathbf A=\begin{pmatrix}1&15\,\Omega\\0&1\end{pmatrix}\begin{pmatrix}1&0\\50\,\mathrm{mS}&1\end{pmatrix}\begin{pmatrix}1&20\,\Omega\\0&1\end{pmatrix}=\begin{pmatrix}1.75&50\,\Omega\\50\,\mathrm{mS}&2\end{pmatrix}.$$

从负载往回算，取 $U_2=3$ V，$-I_2=50$ mA：$U_1=5.25\,\mathrm{V}+2.5\,\mathrm{V}=7.75$ V，$I_1=150\,\mathrm{mA}+100\,\mathrm{mA}=250$ mA。这些就是第 [4](das-zweitor-im-betrieb.html#stufe-4) 阶段的值，无需解方程组。
::::

等效的 $\pi$ 形网络，并联电导为 $G_1$、$G_3$，串联电导为 $G_2$，一般有

<span class="anker" id="gl-8-3"></span>
$$A_{11}=1+\frac{G_3}{G_2},\qquad A_{21}=G_1+G_3+\frac{G_1G_3}{G_2},\qquad A_{12}=\frac{1}{G_2},\qquad A_{22}=1+\frac{G_1}{G_2}, \tag{8.3}$$

例如 $A_{11}=1+15/20=1.75$。输出端开路时，$G_2$ 和 $G_3$ 构成分压器，$U_2=U_1\,G_2/(G_2+G_3)$，由此得 $A_{11}$。其余参数同样由式 [(8.2)](#gl-8-2) 得出。

⁠**极限情况：**$R=0$ 和 $G=0$ 给出单位矩阵，即什么也不做的二端口网络。两个相同的 T 形网络级联时 $A_{11}=5.56$，而不是 $1.75^2=3.06$。第二个是第一个的负载，中间电压因此降到开路值以下。

:::frage 信号是向前传的。为什么链式形式要往回算？
因为它是计算规则，不是过程。在输出端，负载使 $-I_2$ 随 $U_2$ 确定。从那里起，每一级都无需解方程组就给出它前面的量。物理上一切是共同建立的。
:::

:::ltspice 级联自身加载
⁠**绘制：**电压源 `voltage` 取 `9`，从 `1` 接地。第一个 T：`Ra1` 取 `15`，从 `1` 接到 `m1`，`Rb1` 取 `20`，从 `m1` 接地，`Rc1` 取 `20`，从 `m1` 接到 `k`。第二个 T 同样，从 `k` 经 `m2` 到 `3`。`RL` 取 `1G`，从 `3` 接地，即几乎开路。

⁠**指令：**`.op`，`.meas op Uk FIND V(k)`，`.meas op Uout FIND V(3)`，`.meas op Iin FIND I(Ra1)`。

⁠**你会看到：**$\mathtt{V(3)}=1.618$ V，所以 $9\,\mathrm{V}/1.618\,\mathrm{V}=5.56$，与 $\mathbf A\mathbf A$ 的 $A_{11}$ 相同。点 `k` 上是 2.83 V，而不是单个 T 开路时的 5.14 V。把 `RL` 设为 60，检验练习 [8](#aufg-8)(c)：$\mathtt{V(3)}=1.036$ V。
:::

:::aufgabe 练习 8 ★★★ 顺序很重要
<span class="anker" id="aufg-8"></span>

一个 30 $\Omega$ 的串联电阻与 T 形网络级联。

<ol class="al">

<li>

分别计算“T 在前，串联电阻在后”和“串联电阻在前，T 在后”的 $\mathbf A$。

</li>

<li>

不用矩阵，用电流和分压器解释 $A_{11}$ 的差别。

</li>

<li>

两个相同的 T 形网络级联，接理想 9 V 电源，向 60 $\Omega$ 负载供电。$U_2$ 是多少？用 $\mathbf A\mathbf A$ 计算。

</li>

</ol>

:::loesung
(a) T 在前，串联电阻在后：$A_{11}=1.75$，$A_{12}=102.5\,\Omega$，$A_{21}=50$ mS，$A_{22}=3.5$。串联电阻在前，T 在后：$A_{11}=3.25$，$A_{12}=110\,\Omega$，$A_{21}=50$ mS，$A_{22}=2$。

(b) $A_{11}$ 对应输出端开路。第一种情况下，串联电阻悬空在末端，没有电流，$A_{11}$ 仍为 1.75。第二种情况下，它位于 T 的输入端之前，T 呈现 35 $\Omega$。两者构成分压器，$65/35=1.857$，$1.857\cdot1.75=3.25$。

(c) $\mathbf A\mathbf A$ 有 $A_{11}=5.5625$，$A_{12}=187.5\,\Omega$，$A_{21}=187.5$ mS，$A_{22}=6.5$。由 $-I_2=U_2/60\,\Omega$ 得 $U_1=(5.5625+187.5/60)\,U_2=8.6875\,U_2$，所以 $U_2=1.036$ V。
:::
:::
