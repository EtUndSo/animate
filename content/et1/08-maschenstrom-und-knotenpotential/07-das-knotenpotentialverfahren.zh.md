---
title: 第 5 阶段：节点电位法
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 网孔电流法与节点电位法
order: 1180700
summary: 网孔定律已经解决，剩下 k-1 条节点定律和 k-1 个未知量。本阶段列出这些方程，并第二次求解同一网络。
tags: 互电导
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
网孔定律已经解决，剩下 $k-1$ 条节点定律和 $k-1$ 个未知量。本阶段列出这些方程，并第二次求解同一网络。
:::

**基本思路。** 经电导 $G$ 从节点 $\mu$ 流向相邻节点 $\nu$ 的电流为 $G\,(U_\mu-U_\nu)$。把一个节点所有流出的电流相加并按电位整理，本节点电位前面是该节点所有电导之和。其他节点电位前面只有通向本节点的电导，带负号：抬高相邻节点，流出的电流就减少。图 [5](#abb-5) 以实验的形式展示了这一点。

:::definition 定义 5.1 (节点电位法)
<span class="anker" id="satz-5-1"></span>

该方法有四步：

<ol>

<li>

把实际电压源变换为实际电流源：$I_\mathrm q=U_\mathrm q/R$，同一电阻改为并联（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）。

</li>

<li>

确定一个参考节点，把其余节点的电位标为相对于它的电压。把电阻写成电导。

</li>

<li>

对其余 $k-1$ 个节点列出节点定律，或直接读出矩阵。

</li>

<li>

解方程组得到节点电位，再由此计算支路电压和支路电流。

</li>

</ol>
:::

:::satz 定理 5.2 (节点电位法的矩阵形式)
<span class="anker" id="satz-5-2"></span>

令 $n=k-1$，节点电位满足 $\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$：

<span class="anker" id="gl-5-1"></span>
$$\begin{pmatrix}Y_{11}&Y_{12}&\dots&Y_{1n}\\Y_{21}&Y_{22}&\dots&Y_{2n}\\\vdots&\vdots&\ddots&\vdots\\Y_{n1}&Y_{n2}&\dots&Y_{nn}\end{pmatrix} \begin{pmatrix}U_1\\U_2\\\vdots\\U_n\end{pmatrix}= \begin{pmatrix}I_\mathrm{q1}\\I_\mathrm{q2}\\\vdots\\I_{\mathrm qn}\end{pmatrix}. \tag{5.1}$$

<ul>

<li>

$Y_{\mu\mu}$ 是接在节点 $\mu$ 上的所有电导之和。

</li>

<li>

$Y_{\mu\nu}=Y_{\nu\mu}$ 是负的__互电导__，即直接接在节点 $\mu$ 和 $\nu$ 之间的电导之和的负值。没有直接连接时为零。

</li>

<li>

$I_{\mathrm q\mu}$ 是节点处的电源电流之和，流入节点时为正。

</li>

</ul>
:::

:::herleitung 从节点定律到矩阵
在节点 $\mu$ 处，经每个电导 $G_a$ 流向相邻节点 $\nu$ 的电流为 $G_a\,(U_\mu-U_\nu)$，流向参考节点的电流为 $G_a\,U_\mu$。这些电流之和等于注入的 $I_{\mathrm q\mu}$。整理后，$U_\mu$ 前面是所有 $G_a$ 之和，$U_\nu$ 前面是 $\mu$ 和 $\nu$ 之间电导之和的负值。节点 $\nu$ 得到相同的元素，因为电导没有方向。所以 $\mathbf Y$ 是对称的。
:::

⁠**如何理解：**第 $\mu$ 行是节点定律：左边是经电导流出的所有电流，右边是电源推入的电流。第 $\nu$ 列表示：把节点 $\nu$ 保持在 1 V，其他节点保持在 0 V，就必须在节点 $\nu$ 注入电流 $Y_{\nu\nu}$，并在每个相邻节点 $\mu$ 抽出电流 $-Y_{\mu\nu}$。这正是[第 6 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)的短路试验。**适用条件：**网络含电导和固定电流源。理想电压源放不进来，因为它没有有限的电导（第 [9](die-modifizierte-knotenanalyse.html#stufe-9) 阶段）。

:::abbildung et1/k8yspalte 5
左：用于节点电位法的模型电路，电池已变换为电流源。右：去掉电源，节点 1 为 1 V，节点 2 为 0 V。经 $G_1$、$G_2$、$G_3$ 流出 $1+0.25+0.5=1.75$ mA，这就是 $Y_{11}$。这 0.5 mA 到达节点 2，必须在那里抽出，这就是 $Y_{21}=-0.5$ mS。
:::

**例。** 左边得到 $I_\mathrm{q1}=U_\mathrm q/R_1=9$ mA，与 $G_1=1$ mS 并联。各电导为 $G_2=0.25$ mS，$G_3=0.5$ mS，$G_4=0.1$ mS，$G_5=0.2$ mS（图 [5](#abb-5)）。节点定律为

$$\begin{aligned} \text{节点 1：}\quad&(G_1+G_2)\,U_1+G_3\,(U_1-U_2)-I_\mathrm{q1}=0,\\ \text{节点 2：}\quad&G_3\,(U_2-U_1)+(G_4+G_5)\,U_2-I_\mathrm q=0. \end{aligned}$$

整理后，以 mS、V 和 mA 为单位：

$$\begin{pmatrix}G_1+G_2+G_3&-G_3\\-G_3&G_3+G_4+G_5\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}= \begin{pmatrix}1.75&-0.5\\-0.5&0.8\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}9\\4\end{pmatrix}.$$

由 $D=1.4-0.25=1.15$，$D_1=7.2+2=9.2$ 和 $D_2=7+4.5=11.5$ 得 $U_1=8$ V，$U_2=10$ V。这与由三个网孔得到的结果相同，只是用 $2\times2$ 的计算代替了 $3\times3$ 的计算。

电流由差值得出，而且要在**原始**网络中计算：$(U_\mathrm q-U_1)/R_1=1$ mA，$U_1/R_2=2$ mA，$(U_2-U_1)/R_3=1$ mA，$U_2/R_4=1$ mA，$U_2/R_5=2$ mA。**检验：**在节点 2，$4=1+1+2$ mA。电源提供 $9\,\mathrm{V}\cdot1\,\mathrm{mA}+10\,\mathrm{V}\cdot4\,\mathrm{mA}=49$ mW，电阻吸收 $1+16+2+10+20=49$ mW。**极限情况：**$G_3\to0$ 时非对角元消失，两侧分别计算（练习 [7](#aufg-7)）。

:::frage 在 $\mathbf Z$ 中符号取决于箭头。为什么在 $\mathbf Y$ 中总是负号？
网孔电流有一个可选择的方向，所以在公共支路中也有两种可能。节点电位没有方向，都以同一个参考节点为基准。因此在两个节点之间的电导上总是差值，其他节点的电位总是带负号。
:::

:::frage 变换之后，在网孔图中 $R_5$ 上有 2 mA 向上，而在原始网络中有 2 mA 向下。哪个对？
原始网络。等效电源只在接线端上一致（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）。在节点 2 和接地点，两种形式给出相同的结果，而在电源内部，电流的含义不同。因此，内部量要在原始网络中由接线端电压计算。
:::

:::aufgabe 练习 6 ★★ 三个节点和一个参考
<span class="anker" id="aufg-6"></span>

某网络有节点 0（参考）、1、2、3。电阻：1 到 0 为 1 k$\Omega$，1 到 2 为 1 k$\Omega$，2 到 0 为 500 $\Omega$，2 到 3 为 1 k$\Omega$，3 到 0 为 1 k$\Omega$。电流源向节点 1 推入 6 mA，向节点 2 推入 3 mA。

<ol class="al">

<li>

读出 $\mathbf Y$ 和 $\mathbf I_\mathrm q$。为什么 $Y_{13}=0$？

</li>

<li>

用克莱姆法则计算节点电位。

</li>

<li>

计算所有电阻电流，并在节点 2 处检验。

</li>

<li>

变换两个电源后需要多少个网孔电流？这里哪种方法更短？

</li>

</ol>

:::loesung
(a) 电导为 1 mS，1 mS，2 mS，1 mS，1 mS：

$$\mathbf Y=\begin{pmatrix}2&-1&0\\-1&4&-1\\0&-1&2\end{pmatrix}\mathrm{mS},\qquad\mathbf I_\mathrm q=\begin{pmatrix}6\\3\\0\end{pmatrix}\mathrm{mA}.$$

$Y_{13}=0$，因为 1 和 3 之间没有电阻。

(b) $D=2\cdot7+1\cdot(-2)=12$，$D_1=48$，$D_2=24$，$D_3=12$。所以 $U_1=4$ V，$U_2=2$ V，$U_3=1$ V。

(c) $I_{10}=4$ mA，$I_{12}=2$ mA，$I_{20}=4$ mA，$I_{23}=1$ mA，$I_{30}=1$ mA。节点 2：$3+2=4+1$ mA。

(d) 每个电流源与其并联电阻合为一条支路。于是 $z=5$，$k=4$，所以 $m=2$ 对 $k-1=3$。网孔电流法用两个方程，更短。节点 3 实际上不是节点，而是一个串联。
:::
:::

:::aufgabe 练习 7 ★★ 互电导的极限情况
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

去掉模型电路中的 $R_3$（$G_3=0$）。$\mathbf Y$ 变成什么？计算 $U_1$ 和 $U_2$。

</li>

<li>

预测：把 $R_3$ 换成导线。为什么这不能直接写进 $\mathbf Y$？把两个节点合并，求公共电压和导线中的电流。

</li>

</ol>

:::loesung
(a) 非对角元变为零，方程解耦：$U_1=9\,\mathrm{mA}/1.25\,\mathrm{mS}=7.2$ V，$U_2=4\,\mathrm{mA}/0.3\,\mathrm{mS}=13.3$ V。这是两个分开的网络。

(b) $G_3\to\infty$ 无法作为数字填入。导线把两个节点合为一个：$U=(9+4)\,\mathrm{mA}/(1+0.25+0.1+0.2)\,\mathrm{mS}=8.39$ V。导线中的电流由节点 2 得出：$4\,\mathrm{mA}-0.3\,\mathrm{mS}\cdot8.39\,\mathrm{V}=1.48$ mA，从 2 到 1。第 [9](die-modifizierte-knotenanalyse.html#stufe-9) 阶段用 0 V 电源解决同样的情形。
:::
:::
