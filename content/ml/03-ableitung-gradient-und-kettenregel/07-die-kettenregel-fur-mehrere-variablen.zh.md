---
title: 多元函数的链式法则
pfad: 计算机科学 / 机器学习 / 数学基础 / 导数、梯度与链式法则
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: 第 3 章：导数、梯度与链式法则
nachschlagen: ja
order: 15230700
summary: 涉及许多变量的计算，是由有许多输入和输出的函数组成的链。链式法则可以推广到这种情形：把各级的雅可比矩阵相乘。按分量来看，这意味着要对变化从某个输入到达输出的所有路径求和。对一个数的梯度，这时出现的是转置的雅可比矩阵。
tags: 曲线, 速度向量
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
涉及许多变量的计算，是由有许多输入和输出的函数组成的链。链式法则可以推广到这种情形：把各级的雅可比矩阵相乘。按分量来看，这意味着要对变化从某个输入到达输出的所有路径求和。对一个数的梯度，这时出现的是转置的雅可比矩阵。
:::

### 链式法则作为矩阵乘积

<span class="anker" id="stufe-6-1"></span>

设有两级前后串联：$\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ 把 $\mathbf{x}$ 变成中间向量 $\mathbf{u}=\mathbf{g}(\mathbf{x})$，$\mathbf f:\mathbb{R}^m\to\mathbb{R}^p$ 再把它变成 $\mathbf{y}=\mathbf f(\mathbf{u})$。像第 [2.2](die-kettenregel.html#stufe-2-2) 节那样追踪一个微小变化 $\Delta\mathbf{x}$。由式 [(5.3)](die-jacobi-matrix.html#gl-5-3)，第一级把它以 $\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$ 的形式传递下去，第二级再以 $\Delta\mathbf{y}\approx\mathbf{J}_{\mathbf f}\,\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$ 的形式传递下去。两个数的乘积变成了两个矩阵的乘积。这与[第 1 章第 9.4 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-4)相符：两个前后相接的线性级构成一个线性级，它的矩阵是这两个矩阵的乘积。

:::satz 定理 6.1 (多元函数的链式法则)
<span class="anker" id="satz-6-1"></span>

如果 $\mathbf{g}$ 在点 $\mathbf{x}$ 处可微，$\mathbf f$ 在点 $\mathbf{g}(\mathbf{x})$ 处可微，那么 $\mathbf f\circ\mathbf{g}$ 在点 $\mathbf{x}$ 处可微，并且

<span class="anker" id="gl-6-1"></span>
$$\mathbf{J}_{\mathbf f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_{\mathbf f}\bigl(\mathbf{g}(\mathbf{x})\bigr)\,\mathbf{J}_{\mathbf{g}}(\mathbf{x}). \tag{6.1}$$
:::

形状是相容的：左边是一个 $p\times n$ 矩阵，右边是一个 $p\times m$ 矩阵乘以一个 $m\times n$ 矩阵。共同的数 $m$ 是中间变量的个数。和一元情形一样，每个雅可比矩阵都在它那一级工作的地方求值，所以 $\mathbf{J}_{\mathbf f}$ 在中间值 $\mathbf{u}=\mathbf{g}(\mathbf{x})$ 处求值。对更长的链 $\mathbf f_L\circ\dots\circ\mathbf f_1$，雅可比矩阵是乘积 $\mathbf{J}_{\mathbf f_L}\cdots\mathbf{J}_{\mathbf f_1}$，最后作用的那一级位于最左边。与数不同，这些因子不能交换。

:::beweis 多元函数的链式法则
证明与第 [2.2](die-kettenregel.html#stufe-2-2) 节中的相同，只是用长度代替绝对值。记 $\mathbf{u}=\mathbf{g}(\mathbf{x})$，$\mathbf{k}=\mathbf{g}(\mathbf{x}+\mathbf{h})-\mathbf{u}=\mathbf{J}_{\mathbf{g}}\mathbf{h}+\mathbf{r}_{\mathbf{g}}(\mathbf{h})$，则

$$\mathbf f\bigl(\mathbf{g}(\mathbf{x}+\mathbf{h})\bigr)-\mathbf f(\mathbf{u})=\mathbf{J}_{\mathbf f}\,\mathbf{k}+\mathbf{r}_{\mathbf f}(\mathbf{k})=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}\,\mathbf{h}+\mathbf{J}_{\mathbf f}\,\mathbf{r}_{\mathbf{g}}(\mathbf{h})+\mathbf{r}_{\mathbf f}(\mathbf{k}).$$

中间的误差比 $\lVert\mathbf{h}\rVert$ 消失得更快，因为 $\mathbf{r}_{\mathbf{g}}$ 如此，而乘以一个固定的矩阵至多把长度放大一个固定的倍数。最后一个误差比 $\lVert\mathbf{k}\rVert$ 消失得更快，而只要 $\mathbf{h}$ 很小，$\lVert\mathbf{k}\rVert$ 至多是 $\lVert\mathbf{h}\rVert$ 的一个固定倍数。所以 $\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$ 是 $\mathbf f\circ\mathbf{g}$ 的线性近似的矩阵。
:::

::::beispiel [算例]
设 $\mathbf{g}$ 如式 [(5.1)](die-jacobi-matrix.html#gl-5-1)，$f(\mathbf{u})=u_1^2+3u_2$ 是只有一个输出的函数（$p=1$）。它们的复合是 $F(\mathbf{x})=f(\mathbf{g}(\mathbf{x}))=x_1^2x_2^2+6x_1+3x_2^2$。在点 $\mathbf{x}=(1,\,2)^{\top}$ 处，$\mathbf{u}=\mathbf{g}(\mathbf{x})=(2,\,6)^{\top}$，$\mathbf{J}_f(\mathbf{u})=(2u_1\ \ 3)=(4\ \ 3)$。由式 [(6.1)](#gl-6-1)，

$$\mathbf{J}_F(1,2)=\begin{pmatrix}4&3\end{pmatrix}\begin{pmatrix}2&1\\2&4\end{pmatrix}=\begin{pmatrix}4\cdot2+3\cdot2&\ 4\cdot1+3\cdot4\end{pmatrix}=\begin{pmatrix}14&16\end{pmatrix}.$$

用写开的函数验算：$\partial_1F=2x_1x_2^2+6=8+6=14$，$\partial_2F=2x_1^2x_2+6x_2=4+12=16$。
::::

⁠**简而言之：**复合函数的雅可比矩阵是各级雅可比矩阵的乘积，最后作用的那一级在左边：$\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}$。

### 对所有路径求和

<span class="anker" id="stufe-6-2"></span>

把矩阵乘积式 [(6.1)](#gl-6-1) 对一个元素写开，得到的是对中间变量的求和。对只有一个输出的函数 $F=f\circ\mathbf{g}$，有

<span class="anker" id="gl-6-2"></span>
$$\frac{\partial F}{\partial x_j}(\mathbf{x})=\sum_{i=1}^m\frac{\partial f}{\partial u_i}(\mathbf{u})\,\frac{\partial u_i}{\partial x_j}(\mathbf{x}),\qquad \mathbf{u}=\mathbf{g}(\mathbf{x}). \tag{6.2}$$

这个和有一个直观的含义。$x_j$ 的变化不是直接到达 $F$，而是经过中间变量 $u_1,\dots,u_m$。每个中间变量都是一条路径：在经过 $u_i$ 的路径上，变化先乘以 $\partial u_i/\partial x_j$，再乘以 $\partial f/\partial u_i$。所有路径的贡献都到达输出，并在那里相加（图 [11](#abb-11)）。因此链式法则常被概括为：沿一条路径相乘，对所有路径求和。

:::abbildung ml/k3wege 11
把链式法则看作路径网络：$F=f\circ\mathbf{g}$ 在点 $(1,\,2)$ 处。每条边上标着它的终点对它的起点的局部导数。从 $x_1$ 出发有两条路径通向 $F$：经过 $u_1$（蓝色）和经过 $u_2$（橙色）。沿每条路径把因子相乘，再把两个贡献相加。可以想象一个管网：每根管子把流过它的量乘以自己的因子，各股水流在终点汇合。
:::

::::beispiel [算例 1]
对于上一小节中的 $F=f\circ\mathbf{g}$，在点 $(1,\,2)$ 处各边上的因子为

$$\frac{\partial u_1}{\partial x_1}=x_2=2,\quad \frac{\partial u_1}{\partial x_2}=x_1=1,\quad \frac{\partial u_2}{\partial x_1}=2,\quad \frac{\partial u_2}{\partial x_2}=2x_2=4,\quad \frac{\partial f}{\partial u_1}=2u_1=4,\quad \frac{\partial f}{\partial u_2}=3 .$$

对两条路径求和，就得到元素 $14$ 和 $16$，与矩阵乘积的结果相同（图 [12](#abb-12)）。

:::abbildung ml/k3rwege 12
$F=f\circ\mathbf{g}$ 在点 $(1,\,2)$ 处的偏导数，写成对经过 $u_1$ 和 $u_2$ 的两条路径的求和。
:::
::::

::::beispiel [算例 2]
一个输入，两条路径。设 $F(x)=g_1(x)\,g_2(x)$，其中 $g_1(x)=x^2$，$g_2(x)=3x$，于是 $f(\mathbf{u})=u_1u_2$。经过 $u_1$ 和 $u_2$ 的两条路径给出

$$\frac{\mathrm{d} F}{\mathrm{d} x}=\frac{\partial f}{\partial u_1}\,g_1'(x)+\frac{\partial f}{\partial u_2}\,g_2'(x)=u_2\cdot2x+u_1\cdot3=3x\cdot2x+x^2\cdot3=9x^2 .$$

验算：$F(x)=3x^3$ 的导数是 $9x^2$。漏掉一条路径，就会得到 $6x^2$ 或 $3x^2$。顺便说一句，这恰好就是乘积法则式 [(1.5)](die-ableitung.html#gl-1-5)：它是有两条路径的链式法则。
::::

⁠**简而言之：**按分量来看，链式法则是对从输入到输出的所有路径的求和；沿每条路径，把局部导数相乘。

:::hintergrund 为什么要对路径求和
原因是第 [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4) 节中的观察：变化很小时，各个作用相加。把 $x_j$ 改变 $\Delta x_j$，所有中间变量会同时变化，每个大约变化 $\frac{\partial u_i}{\partial x_j}\Delta x_j$。这些同时发生的变化对 $f$ 有什么影响，由 $f$ 关于变量 $u_1,\dots,u_m$ 的线性近似给出：每个中间变量贡献 $\frac{\partial f}{\partial u_i}\Delta u_i$，各贡献相加，就好像每个中间变量都是单独变化的一样。因此，对路径求和就是对这些单个贡献求和。对更长的链，情况依此类推：一条路径依次经过好几个中间变量，沿这条路径把所有边上的因子相乘，最后对从输入到输出的所有路径求和。路径的数目可能增长得非常快；怎样巧妙地把它们合并起来，见第 [10](automatische-differentiation.html#stufe-10) 节。
:::

### 复合函数的梯度

<span class="anker" id="stufe-6-3"></span>

对只有一个输出的函数 $F=f\circ\mathbf{g}$，雅可比矩阵是写成一行的梯度。如果想按本章的约定把梯度写成一列，就必须把链式法则转置。

:::satz 定理 6.2 (复合函数的梯度)
<span class="anker" id="satz-6-2"></span>

如果 $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ 在点 $\mathbf{x}$ 处可微，$f:\mathbb{R}^m\to\mathbb{R}$ 在点 $\mathbf{u}=\mathbf{g}(\mathbf{x})$ 处可微，那么

<span class="anker" id="gl-6-3"></span>
$$\nabla(f\circ\mathbf{g})(\mathbf{x})=\mathbf{J}_{\mathbf{g}}(\mathbf{x})^{\top}\,\nabla f(\mathbf{u}). \tag{6.3}$$
:::

:::beweis 复合函数的梯度
由式 [(6.1)](#gl-6-1)，$\nabla(f\circ\mathbf{g})(\mathbf{x})^{\top}=\mathbf{J}_{f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_f(\mathbf{u})\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\nabla f(\mathbf{u})^{\top}\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})$。利用[第 1 章第 10.1 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1)的法则 $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ 把两边转置，就得到结论。
:::

转置纯粹是记账的需要：它之所以出现，是因为梯度写成一列，而雅可比矩阵的各行属于各个输出。就内容而言，式 [(6.3)](#gl-6-3) 与式 [(6.2)](#gl-6-2) 说的是同一件事：$\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ 的第 $j$ 个分量是 $\mathbf{J}_{\mathbf{g}}$ 的第 $j$ 列乘以 $\nabla f$，也就是对从 $x_j$ 出发的所有路径求和。如果内层函数是线性的，即 $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}$，那么由第 [5.4](die-jacobi-matrix.html#stufe-5-4) 节，它就变成法则 $\nabla_{\mathbf{x}}f(\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\,\nabla f(\mathbf{A}\mathbf{x})$。nabla 上的下标 $\mathbf{x}$ 说明梯度是对哪个变量求的。

::::beispiel [算例]
利用式 [(6.1)](#gl-6-1) 处算例中的 $\mathbf{J}_{\mathbf{g}}(1,2)$ 和 $\nabla f(\mathbf{u})=(4,\,3)^{\top}$，有

$$\nabla F(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}^{\top}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}2&2\\1&4\end{pmatrix}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}8+6\\4+12\end{pmatrix}=\begin{pmatrix}14\\16\end{pmatrix}.$$

如果不转置，就会得到 $\mathbf{J}_{\mathbf{g}}\,\nabla f=(8+3,\ 8+12)^{\top}=(11,\,20)^{\top}$，这是错的。
::::

:::warnung 别忘了转置
如果内层函数的雅可比矩阵是对称的，忘了转置也不会被发现。因此，要用一个雅可比矩阵不对称的例子检验自己推导出的梯度公式。如果 $\mathbf{J}_{\mathbf{g}}$ 的行数和列数不同，看一眼形状就能立刻发现错误：$\nabla f$ 有 $m$ 个元素，$\mathbf{J}_{\mathbf{g}}^{\top}$ 有 $m$ 列，只有 $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ 才得到一个有 $n$ 个元素的向量。
:::

⁠**简而言之：**复合函数的梯度等于内层函数的转置雅可比矩阵乘以外层函数的梯度：$\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$。

### 沿曲线的导数

<span class="anker" id="stufe-6-4"></span>

在地图上散步就是一条曲线：在每个时刻 $t$，人都在某个位置 $\boldsymbol{\gamma}(t)\in\mathbb{R}^d$。一路上高度 $f(\boldsymbol{\gamma}(t))$ 变化得有多快？这是链式法则只有一个输入变量 $t$ 的特殊情形。

:::definition 定义 6.3 (曲线与速度)
<span class="anker" id="satz-6-3"></span>

__曲线__是一个函数 $\boldsymbol{\gamma}:\mathbb{R}\to\mathbb{R}^d$，$t\mapsto\boldsymbol{\gamma}(t)=(\gamma_1(t),\dots,\gamma_d(t))^{\top}$。它的导数 $\boldsymbol{\gamma}'(t)=(\gamma_1'(t),\dots,\gamma_d'(t))^{\top}$ 称为__速度向量__。
:::

速度向量是 $\boldsymbol{\gamma}$ 的雅可比矩阵，是一个 $d\times1$ 矩阵。它指向当前运动的方向，它的长度就是速率。由式 [(6.1)](#gl-6-1)（取 $n=1$），对可微的 $f$ 有

<span class="anker" id="gl-6-4"></span>
$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)=\nabla f\bigl(\boldsymbol{\gamma}(t)\bigr)^{\top}\boldsymbol{\gamma}'(t). \tag{6.4}$$

对直线 $\boldsymbol{\gamma}(t)=\mathbf{x}+t\,\mathbf{h}$，有 $\boldsymbol{\gamma}'=\mathbf{h}$，变化率为 $\nabla f(\mathbf{x})^{\top}\mathbf{h}$；如果 $\mathbf{h}$ 的长度为 $1$，这就是第 [4.1](richtungsableitung-und-steilster-anstieg.html#stufe-4-1) 节中的方向导数。如果一条曲线完全在一条等高线内延伸，那么 $f(\boldsymbol{\gamma}(t))$ 是常数，左边就为零：梯度垂直于等高线内的每个速度向量。这正是第 [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3) 节中的定理，现在用链式法则给出了理由。

::::beispiel [算例]
设 $f(\mathbf{x})=x_1^2x_2+x_2^2$，$\boldsymbol{\gamma}(t)=(1+t,\ 2+2t)^{\top}$ 是经过 $(1,\,2)$ 的直线，$\boldsymbol{\gamma}'(t)=(1,\,2)^{\top}$。在 $t=0$ 处，

$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)\Big|_{t=0}=\begin{pmatrix}4&5\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix}=4+10=14 .$$

验算：$f(\boldsymbol{\gamma}(t))=(1+t)^2(2+2t)+(2+2t)^2=2\,(1+t)^3+4\,(1+t)^2$ 在 $t=0$ 处的导数为 $6+8=14$。
::::

⁠**简而言之：**沿一条曲线，$f$ 以变化率 $\nabla f^{\top}\boldsymbol{\gamma}'$ 变化；在等高线内，这个变化率为零。

:::aufgabe 练习 20 ★ 雅可比矩阵形式的链式法则
<span class="anker" id="aufg-20"></span>

设 $\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1x_2)^{\top}$，$f(\mathbf{u})=u_1^2-u_2$。

<ol class="al">

<li>

在点 $\mathbf{x}=(1,\,3)^{\top}$ 处，计算中间值 $\mathbf{u}$、雅可比矩阵 $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ 和 $\nabla f(\mathbf{u})$。

</li>

<li>

用式 [(6.3)](#gl-6-3) 计算 $\nabla(f\circ\mathbf{g})(\mathbf{x})$，并用写开的函数验算。如果不转置，会得到什么？

</li>

</ol>

:::loesung
(a) $\mathbf{u}=\mathbf{g}(1,3)=(4,\,3)^{\top}$。雅可比矩阵是 $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}1&1\\x_2&x_1\end{smallmatrix}\bigr)$，所以在点 $(1,\,3)$ 处为 $\bigl(\begin{smallmatrix}1&1\\3&1\end{smallmatrix}\bigr)$。外层函数的梯度是 $\nabla f(\mathbf{u})=(2u_1,\,-1)^{\top}=(8,\,-1)^{\top}$。

(b) 由式 [(6.3)](#gl-6-3)：

$$\nabla(f\circ\mathbf{g})(1,3)=\begin{pmatrix}1&3\\1&1\end{pmatrix}\begin{pmatrix}8\\-1\end{pmatrix}=\begin{pmatrix}8-3\\8-1\end{pmatrix}=\begin{pmatrix}5\\7\end{pmatrix}.$$

验算：$F(\mathbf{x})=(x_1+x_2)^2-x_1x_2=x_1^2+x_1x_2+x_2^2$ 的偏导数为 $2x_1+x_2=5$ 和 $x_1+2x_2=7$。如果不转置，会得到 $\mathbf{J}_{\mathbf{g}}\nabla f=(8-1,\ 24-1)^{\top}=(7,\,23)^{\top}$，这是错误的结果。
:::
:::

:::aufgabe 练习 21 ★★ 三条路径
<span class="anker" id="aufg-21"></span>

设 $F(x)=g_1(x)\,g_2(x)\,g_3(x)$，其中 $g_1(x)=x$，$g_2(x)=x^2$，$g_3(x)=x^3$。

<ol class="al">

<li>

画出从 $x$ 经过 $u_1,u_2,u_3$ 到 $F=u_1u_2u_3$ 的路径网络，并在每条边上写出它的因子。

</li>

<li>

把 $F'(x)$ 作为对三条路径的求和算出来，并与 $x^6$ 的导数比较。

</li>

</ol>

:::loesung
(a) 从 $x$ 出发有三条边通向 $u_1$、$u_2$、$u_3$，因子分别为 $1$、$2x$ 和 $3x^2$。从每个 $u_i$ 出发各有一条边通向 $F=u_1u_2u_3$；它的因子是另外两个的乘积：$u_2u_3=x^5$、$u_1u_3=x^4$ 和 $u_1u_2=x^3$。

(b) 对三条路径求和：

$$F'(x)=x^5\cdot1+x^4\cdot2x+x^3\cdot3x^2=x^5+2x^5+3x^5=6x^5 .$$

这就是 $F(x)=x^6$ 的导数。经过 $u_k$ 的路径贡献 $k\,x^5$，因为 $g_k=x^k$ 的导数是 $k\,x^{k-1}$，而另外两个因子合起来是 $x^{6-k}$。所以三个因子的乘积法则就是对三条路径的求和。
:::
:::

:::aufgabe 练习 22 ★★ 等高线内的曲线
<span class="anker" id="aufg-22"></span>

设 $f(\mathbf{x})=x_1^2+4x_2^2$，$\boldsymbol{\gamma}(t)=\bigl(\sqrt5\cos t,\ \tfrac{\sqrt5}2\sin t\bigr)^{\top}$。

<ol class="al">

<li>

证明 $\boldsymbol{\gamma}$ 完全在等高线 $f=5$ 内延伸。

</li>

<li>

求满足 $\boldsymbol{\gamma}(t)=(1,\,1)^{\top}$ 的 $t$，计算该处的 $\boldsymbol{\gamma}'(t)$，并检验 $\nabla f^{\top}\boldsymbol{\gamma}'=0$。把这个方向与第 [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3) 节中的向量 $\mathbf{t}$ 比较。

</li>

<li>

用式 [(6.4)](#gl-6-4) 一般地说明：如果一条可微曲线在 $f$ 的某个水平集内延伸，那么 $\nabla f$ 垂直于它的速度向量。

</li>

</ol>

:::loesung
(a) 对每个 $t$，$f(\boldsymbol{\gamma}(t))=5\cos^2t+4\cdot\tfrac54\sin^2t=5\,(\cos^2t+\sin^2t)=5$。

(b) 由 $\sqrt5\cos t=1$ 和 $\tfrac{\sqrt5}2\sin t=1$ 得 $\cos t=1/\sqrt5$，$\sin t=2/\sqrt5$，所以 $t\approx1.107$。在那里，

$$\boldsymbol{\gamma}'(t)=\bigl(-\sqrt5\sin t,\ \tfrac{\sqrt5}2\cos t\bigr)^{\top}=\bigl(-2,\ \tfrac12\bigr)^{\top},\qquad \nabla f(1,1)^{\top}\boldsymbol{\gamma}'=2\cdot(-2)+8\cdot\tfrac12=0 .$$

速度向量是 $-\tfrac12\,(4,\,-1)^{\top}$，所以它平行于第 [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3) 节中的向量 $\mathbf{t}$。

(c) 如果 $\boldsymbol{\gamma}$ 在值为 $c$ 的水平集内延伸，那么对所有 $t$ 都有 $f(\boldsymbol{\gamma}(t))=c$，它对 $t$ 的导数为零。由式 [(6.4)](#gl-6-4)，这个导数是 $\nabla f(\boldsymbol{\gamma}(t))^{\top}\boldsymbol{\gamma}'(t)$。所以梯度垂直于水平集内任何曲线的每个速度向量。
:::
:::

:::aufgabe 练习 23 ★★★ 有三级的链
<span class="anker" id="aufg-23"></span>

设 $F(\mathbf{x})=\sum_{i=1}^2(\mathbf{A}\mathbf{x})_i^2$，$\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$。这个计算由三级组成：$\mathbf{u}=\mathbf{A}\mathbf{x}$，然后对每个分量 $v_i=u_i^2$，最后 $F=v_1+v_2$。

<ol class="al">

<li>

写出在点 $\mathbf{x}=(2,\,1)^{\top}$ 处的三个雅可比矩阵，并把 $\mathbf{J}_F$ 作为它们的乘积算出来。

</li>

<li>

一般地证明 $\nabla F(\mathbf{x})=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$，并检验 (a) 的结果。

</li>

<li>

把 (a) 中的乘积分别从左边和从右边算一遍。如果 $\mathbf{A}$ 是 $n\times n$ 矩阵，哪种顺序需要的乘法次数更少？

</li>

</ol>

:::loesung
(a) 在点 $(2,\,1)$ 处，$\mathbf{u}=\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$，$\mathbf{v}=(16,\,1)^{\top}$，$F=17$。各雅可比矩阵为 $\mathbf{J}_1=\mathbf{A}$、$\mathbf{J}_2=\operatorname{diag}(2u_1,\,2u_2)=\operatorname{diag}(8,\,2)$ 和 $\mathbf{J}_3=(1\ \ 1)$。它们的乘积为

$$\mathbf{J}_F=(1\ \ 1)\,\operatorname{diag}(8,\,2)\,\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 2)\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 18).$$

(b) 转置后，$\nabla F=\mathbf{A}^{\top}\,\operatorname{diag}(2\mathbf{u})\,\mathbf{1}=\mathbf{A}^{\top}\,2\mathbf{u}=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$。由 $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&5\end{smallmatrix}\bigr)$，得 $2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=2\,(4,\,9)^{\top}=(8,\,18)^{\top}$，与 (a) 一致。验算：$F=(x_1+2x_2)^2+x_2^2$ 的偏导数为 $2\cdot4=8$ 和 $4\cdot4+2=18$。

(c) 从左边算：$(1\ \ 1)\,\operatorname{diag}(8,2)$ 是一行，需要 $n$ 次乘法；这一行乘以 $\mathbf{A}$ 需要 $n^2$ 次。从右边算：$\operatorname{diag}(8,2)\,\mathbf{A}$ 需要 $n^2$ 次乘法，行乘以这个结果还需要 $n^2$ 次。所以从左边算约需 $n^2$ 次乘法，从右边算约需 $2n^2$ 次。如果中间的矩阵不是对角矩阵，而是稠密矩阵，那么从右边算时，矩阵乘积甚至约需 $n^3$ 次。从左边算，也就是从结果开始，得到的始终只是行。
:::
:::
