---
title: 第 8 阶段：受控源与放大器
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 网孔电流法与节点电位法
order: 1181000
summary: 放大器含有受控源（第 6 部分）。本阶段给出它们的印记，并说明这对矩阵意味着什么。
tags: 电压控制电流源, 跨导, 电压增益, 负反馈, 跨阻
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
放大器含有受控源（[第 6 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)）。本阶段给出它们的印记，并说明这对矩阵意味着什么。
:::

**基本思路。** __电压控制电流源__（[第 6 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)）是一种推广的电导。对电导，是自身的电压 $U_{ik}$ 控制从 $i$ 到 $k$ 的电流。对这种电源，控制它的是别处的电压 $U_{pq}$。行不变，因为电流在同样的节点流出和流入。列从 $i$、$k$ 移到 $p$、$q$，因为列对应的是起控制作用的电位。这样对称性就失去了。这是物理事实：输入作用于输出，反过来却不然。

:::satz 定理 8.1 (电压控制电流源的印记)
<span class="anker" id="satz-8-1"></span>

从 $i$ 到 $k$ 的电源 $I=g\,(U_p-U_q)$ 在 $(i,p)$ 和 $(k,q)$ 上加 $+g$，在 $(i,q)$ 和 $(k,p)$ 上加 $-g$。
:::

⁠**如何理解：**$g$ 是__跨导__，即单位控制电压产生的电流，单位为西门子，模型中为 50 mS。**适用条件：**电源应是线性的。晶体管只在工作点附近的小变化范围内才如此（[第 10 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)）。

::::beispiel 无负反馈
一个 $I_\mathrm q=20$ µ A 的电流源，带 $G_\mathrm q=0.5$ mS，给节点 1 供电。那里有 $G_\mathrm i=0.5$ mS 接到接地点。电源 $g\,U_1$ 把电流从节点 2 抽到接地点，那里还接有 $G_\mathrm o=0.05$ mS 和 $G_\mathrm L=0.2$ mS。由印记得

<span class="anker" id="gl-8-1"></span>
$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0\\g&G_\mathrm o+G_\mathrm L\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\end{pmatrix}. \tag{8.1}$$

$Y_{12}=0$，但 $Y_{21}=g$。由 $D=(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)$，$D_1=(G_\mathrm o+G_\mathrm L)\,I_\mathrm q$ 和 $D_2=-g\,I_\mathrm q$ 得

<span class="anker" id="gl-8-2"></span>
$$U_1=\frac{I_\mathrm q}{G_\mathrm q+G_\mathrm i},\qquad U_2=-\frac{g\,I_\mathrm q}{(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)},\qquad A_u=\frac{U_2}{U_1}=-\frac{g}{G_\mathrm o+G_\mathrm L}. \tag{8.2}$$

模型中 $D=0.25$，$U_1=20$ mV，$U_2=-4$ V，__电压增益__ $A_u=-200$，与[第 6 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)相同。负号的来源是受控电流从节点 2 流出。
::::

**有负反馈。** 输入和输出共同的下方连接点称为底点。把它与接地点断开，并在那里插入 $R_\mathrm S=1\,\mathrm{k\Omega}$，就出现节点 3（图 [8](#abb-8)）。这时输出电流流过 $R_\mathrm S$，抬高 $U_3$。这使控制电压 $U_1-U_3$ 下降，输出电流随之减小。这种输出对自身输入的反作用称为__负反馈__。

:::abbildung et1/k8verstaerker 8
带负反馈的放大器。电源 $g\,(U_1-U_3)$ 从节点 2 接到节点 3，$G_\mathrm i$ 和 $G_\mathrm o$ 终止于节点 3。红色路径表示输出电流：它抬高节点 3，从而减小控制电压。$G_\mathrm S\to\infty$ 时，节点 3 落到接地点。
:::

$G_\mathrm q$、$G_\mathrm i$、$G_\mathrm S$、$G_\mathrm o$、$G_\mathrm L$ 以及从 2 到 3 的 $g\,(U_1-U_3)$ 的印记给出

<span class="anker" id="gl-8-3"></span>
$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0&-G_\mathrm i\\g&G_\mathrm o+G_\mathrm L&-g-G_\mathrm o\\-g-G_\mathrm i&-G_\mathrm o&G_\mathrm S+g+G_\mathrm i+G_\mathrm o\end{pmatrix} \begin{pmatrix}U_1\\U_2\\U_3\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\\0\end{pmatrix}. \tag{8.3}$$

:::herleitung 行列式
令 $A=G_\mathrm q+G_\mathrm i$，$B=G_\mathrm o+G_\mathrm L$，沿第一行展开得

$$\begin{aligned} D&=A\,[B\,(G_\mathrm S+G_\mathrm i)+G_\mathrm L\,(g+G_\mathrm o)]-G_\mathrm i\,[B\,G_\mathrm i+G_\mathrm L\,g]\\ &=B\,[A\,G_\mathrm S+G_\mathrm qG_\mathrm i]+G_\mathrm L\,[A\,G_\mathrm o+G_\mathrm q\,g]. \end{aligned}$$

$D_2$ 沿第 2 列展开，该列只有 $I_\mathrm q$：$D_2=-I_\mathrm q\,[g\,(G_\mathrm S+g+G_\mathrm i+G_\mathrm o)-(g+G_\mathrm o)(g+G_\mathrm i)]=(G_\mathrm iG_\mathrm o-g\,G_\mathrm S)\,I_\mathrm q$。
:::

由此得__跨阻__，即单位输入电流产生的输出电压，

<span class="anker" id="gl-8-4"></span>
$$\frac{U_2}{I_\mathrm q}=\frac{G_\mathrm iG_\mathrm o-g\,G_\mathrm S}{(G_\mathrm o+G_\mathrm L)\,[(G_\mathrm q+G_\mathrm i)\,G_\mathrm S+G_\mathrm qG_\mathrm i]+G_\mathrm L\,[(G_\mathrm q+G_\mathrm i)\,G_\mathrm o+G_\mathrm q\,g]}. \tag{8.4}$$

在 $G_\mathrm S=1$ mS 的模型中，$D=5.3225$，$D_2/I_\mathrm q=-49.975$，所以 $U_2/I_\mathrm q=-9.39\,\mathrm{k\Omega}$。由 20 µ A 得 $U_1=39.0$ mV，$U_2=-188$ mV，$A_u=-4.81$。**极限情况：**$G_\mathrm S\to\infty$ 时只剩下含 $G_\mathrm S$ 的项，式 [(8.4)](#gl-8-4) 变为 $-g/[(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)]=-200\,\mathrm{k\Omega}$，即式 [(8.2)](#gl-8-2) 的结果。这时底点又回到接地点。

:::ltspice 带负反馈的放大器
⁠**绘制：**`current` 取 `20u`，从接地点到 `1`，`Rq 2k` 从 `1` 到接地点，`Ri 2k` 从 `1` 到 `3`，`RS 1k` 从 `3` 到接地点。受控电流源 `g` 取 `50m`：输出从 `2` 到 `3`，控制输入从 `1` 到 `3`。`Ro 20k` 从 `2` 到 `3`，`RL 5k` 从 `2` 到接地点。

⁠**指令：**`.op`，`.meas op u1 FIND V(1)`，`.meas op u2 FIND V(2)`，`.meas op au PARAM u2/u1`。

⁠**你会看到：**$\mathtt{u1}=39.0$ mV，$\mathtt{u2}=-188$ mV，$\mathtt{au}=-4.81$。把 `RS` 设为 `1u`：这时 $\mathtt{u2}=-4$ V，$\mathtt{au}=-200$。用 `V(3)` 检验你在练习 [10](#aufg-10) 中的结果。
:::

:::frage 为什么要主动降低增益？
因为这样它几乎不再取决于跨导，而晶体管的 $g$ 分散性很大。在模型中把 $g$ 加倍，$A_u$ 只从 $-4.81$ 变到 $-4.90$。而没有 $R_\mathrm S$ 时，$-200$ 会变成 $-400$。结果接近 $-R_\mathrm L/R_\mathrm S=-5$，也就是由两个精确的电阻决定。[第 11 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html)在运算放大器中利用了这一点。
:::

:::aufgabe 练习 10 ★★★ 输入电阻升高
<span class="anker" id="aufg-10"></span>

考虑图 [8](#abb-8) 中 $G_\mathrm S=1$ mS 的放大器。

<ol class="al">

<li>

证明 $D_1=[(G_\mathrm o+G_\mathrm L)(G_\mathrm S+G_\mathrm i)+G_\mathrm L\,(g+G_\mathrm o)]\,I_\mathrm q$，并计算 $U_1/I_\mathrm q$。

</li>

<li>

不含 $G_\mathrm q$ 的输入电导为 $Y_\mathrm{in}=I_\mathrm q/U_1-G_\mathrm q$。输入电阻 $1/Y_\mathrm{in}$ 是多大？与没有 $R_\mathrm S$ 时的 2 k$\Omega$ 比较。

</li>

<li>

解释其机理：$U_3$ 是多大？因此流过 $G_\mathrm i$ 的电流还有多少？

</li>

</ol>

:::loesung
(a) 把第 1 列换成 $(I_\mathrm q,0,0)$，剩下 $D_1=I_\mathrm q\,[(G_\mathrm o+G_\mathrm L)(G_\mathrm S+g+G_\mathrm i+G_\mathrm o)-(g+G_\mathrm o)\,G_\mathrm o]$。展开后，方括号就是题中给出的式子。数值：$0.25\cdot1.5+0.2\cdot50.05=10.385$。由 $D=5.3225$ 得 $U_1/I_\mathrm q=1.95\,\mathrm{k\Omega}$。

(b) $Y_\mathrm{in}=1/(1.951\,\mathrm{k\Omega})-0.5\,\mathrm{mS}=0.0125$ mS，所以 $R_\mathrm{in}=79.9\,\mathrm{k\Omega}$，是原来的四十倍。

(c) $U_3=38.05$ mV 只比 $U_1=39.02$ mV 低 0.98 mV。$R_\mathrm i$ 另一端的电位几乎跟着变化。因此 $R_\mathrm i$ 上的电压不到 1 mV，流过的电流是 0.49 µ A 而不是 10 µ A。同样的电压下电流很小，就意味着输入电阻很大。
:::
:::
