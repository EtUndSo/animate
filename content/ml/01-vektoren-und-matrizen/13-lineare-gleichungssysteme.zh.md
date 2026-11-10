---
title: 线性方程组
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: 第 1 章：向量与矩阵
nachschlagen: ja
order: 15211300
summary: 到目前为止，都是给定输入 x ，求输出 Ax 。本节提出相反的问题：哪个输入产生给定的输出？这就是线性方程组。本节说明如何求解它，以及它何时无解、何时恰有一个解、何时有无穷多解。
tags: 线性方程组, 系数矩阵, 右端项, 解, 增广矩阵, 高斯消元法, 行阶梯形, 齐次
lang: zh
---

<span class="anker" id="stufe-12"></span>

:::zweck
到目前为止，都是给定输入 $\mathbf{x}$，求输出 $\mathbf{A}\mathbf{x}$。本节提出相反的问题：哪个输入产生给定的输出？这就是线性方程组。本节说明如何求解它，以及它何时无解、何时恰有一个解、何时有无穷多解。
:::

### 矩阵形式的方程组

<span class="anker" id="stufe-12-1"></span>

在中学里你已经见过这样的问题：两个数 $x_1$ 和 $x_2$ 满足 $2x_1+x_2=5$ 和 $x_1+x_2=3$；它们是多少？左边是矩阵-向量乘积的分量。所以这个问题问的是：矩阵 $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ 把哪个向量 $\mathbf{x}$ 映射为 $(5,\,3)^{\top}$？

:::definition 定义 12.1 (线性方程组)
<span class="anker" id="satz-12-1"></span>

对矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 和向量 $\mathbf{y}\in\mathbb{R}^m$，

<span class="anker" id="gl-12-1"></span>
$$\mathbf{A}\mathbf{x}=\mathbf{y} \tag{12.1}$$

称为含 $m$ 个方程、$n$ 个未知数 $x_1,\dots,x_n$ 的__线性方程组__。矩阵 $\mathbf{A}$ 称为__系数矩阵__，向量 $\mathbf{y}$ 称为__右端项__。满足式 [(12.1)](#gl-12-1) 的每个向量 $\mathbf{x}\in\mathbb{R}^n$ 都称为一个__解__。
:::

写开来，第 $i$ 行是方程 $a_{i1}x_1+\dots+a_{in}x_n=y_i$。

::::beispiel [算例]
方程组

$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}5\\3\end{pmatrix}$$

的解为 $\mathbf{x}=(2,\,1)^{\top}$：$2\cdot2+1=5$，$2+1=3$。这个系数矩阵在第 [11.2](einheitsmatrix-und-inverse.html#stufe-11-2) 小节中已经出现过，其逆矩阵为 $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$。把方程组从左边乘以这个逆矩阵，解立刻就出来了：$\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}=(5-3,\ -5+6)^{\top}=(2,\,1)^{\top}$。
::::

⁠**简而言之：**线性方程组 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 问的是：哪个输入 $\mathbf{x}$ 产生输出 $\mathbf{y}$。

### 行图与列图

<span class="anker" id="stufe-12-2"></span>

与矩阵-向量乘积一样，方程组也有两种读法。

**行图。** 每个方程单独描述一个点集。有两个未知数时，$2x_1+x_2=5$ 是平面上的一条直线，$x_1+x_2=3$ 也是。解必须同时满足两个方程，即同时位于两条直线上：它就是两直线的交点，见图 [38](#abb-38) 左侧。有三个未知数时，每个方程是空间中的一个平面。

**列图。** 由列视角，即式 [(7.3)](das-matrix-vektor-produkt.html#gl-7-3)，$\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+\dots+x_n\mathbf{a}_n$。所以方程问的是：各列的线性组合取什么系数时等于右端项？对上面的方程组：$x_1\,(2,\,1)^{\top}+x_2\,(1,\,1)^{\top}=(5,\,3)^{\top}$，解为 $x_1=2$ 和 $x_2=1$。这恰好就是图 [30](das-matrix-vektor-produkt.html#abb-30) 右边的图景。

:::abbildung ml/k1lgs 38
三个含两个未知数的方程组的行图。每个方程是一条直线；解位于所有直线上。(a) 两直线交于一点。(b) 两直线平行，没有公共点。(c) 两个方程描述同一条直线，它上面的每个点都是解。
:::

列图立刻回答了到底何时有解。向量 $\mathbf{A}\mathbf{x}$ 构成列空间（第 [7.4](das-matrix-vektor-produkt.html#stufe-7-4) 小节）。

:::satz 定理 12.2 (可解性)
<span class="anker" id="satz-12-2"></span>

方程组 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 有解，当且仅当 $\mathbf{y}$ 位于 $\mathbf{A}$ 的列空间中。
:::

::::beispiel [算例]
方程组 $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)\mathbf{x}=\mathbf{y}$ 对 $\mathbf{y}=(3,\,6)^{\top}$ 可解，例如 $\mathbf{x}=(1,\,1)^{\top}$，但对 $\mathbf{y}=(1,\,1)^{\top}$ 不可解：由第 [7.4](das-matrix-vektor-produkt.html#stufe-7-4) 小节，列空间只是沿 $(1,\,2)^{\top}$ 方向的直线。
::::

⁠**简而言之：**在行图中，解是所有方程的公共点；在列图中，解是使各列组合成右端项的那组系数。

### 高斯消元法

<span class="anker" id="stufe-12-3"></span>

有两个未知数时，凭观察就能找到解。有三个或更多未知数时，需要一种总能奏效的方法。思路与中学里一样：从一个方程中减去另一个方程的倍数，使一个未知数消失。重复这一步，直到最后一个方程只含一个未知数。

为此只写出数字：系数矩阵，以及用竖线隔开的右端项。这张表格称为__增广矩阵__ $(\mathbf{A}\,|\,\mathbf{y})$。

:::definition 定义 12.3 (高斯消元法)
<span class="anker" id="satz-12-3"></span>

__高斯消元法__用三种初等行变换对增广矩阵进行变换：

<ol>

<li>

把一行的倍数加到另一行上；

</li>

<li>

交换两行；

</li>

<li>

把一行乘以一个非零的数。

</li>

</ol>

目标是__行阶梯形__：在每一行中，第一个非零元素前面的零至少比上一行多一个。然后自下而上求出各未知数（回代）。
:::

:::satz 定理 12.4 (初等行变换不改变解)
<span class="anker" id="satz-12-4"></span>

一个方程组与由它经初等行变换得到的方程组有相同的解。
:::

:::beweis 初等行变换
旧方程组的每个解也满足新方程，因为新方程是旧方程的和与倍数。而三种变换中的每一种都可以撤销：再减去那个倍数，把两行换回来，除以那个数。所以反过来，新方程组的每个解也满足旧方程组。
:::

::::beispiel [算例]
方程组

$$\begin{aligned} x_1+2x_2+x_3&=8\\ 2x_1+x_2+x_3&=7\\ x_1+x_2+2x_3&=9 \end{aligned} \qquad\text{的增广矩阵为}\qquad \left(\begin{array}{ccc|c}1&2&1&8\\2&1&1&7\\1&1&2&9\end{array}\right).$$

从第二行减去第一行的两倍，从第三行减去第一行的一倍，$x_1$ 就从这两行中消失了。然后交换新的第二行和第三行，再从第三行减去新的第二行的三倍，$x_2$ 也从最后一行中消失了：

$$\left(\begin{array}{ccc|c}1&2&1&8\\0&-3&-1&-9\\0&-1&1&1\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&-3&-1&-9\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&0&-4&-12\end{array}\right).$$

自下而上：$-4x_3=-12$，所以 $x_3=3$；然后 $-x_2+3=1$，所以 $x_2=2$；然后 $x_1+4+3=8$，所以 $x_1=1$。解为 $\mathbf{x}=(1,\,2,\,3)^{\top}$，把它代入全部三个方程即可验证。
::::

⁠**简而言之：**高斯消元法用不改变解的初等行变换逐步消去未知数，然后自下而上回代。

:::hintergrund 为什么解方程组时不求逆矩阵
若 $\mathbf{A}$ 可逆，解为 $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}$。这对论证很有用，但作为计算方法却不利。对含 $n$ 个方程、$n$ 个未知数的方程组，高斯消元法约需 $\tfrac23n^3$ 次基本算术运算；求逆矩阵约需 $2n^3$ 次，是它的三倍，还要再加上乘积 $\mathbf{A}^{-1}\mathbf{y}$。此外，计算机只用有限位数字计算。这时逆矩阵只能以舍入后的形式表示，而直接消元通常给出更精确的结果。所以，逆矩阵首先是思考和推导的工具，而不是计算的工具。
:::

### 无解、唯一解或无穷多解

<span class="anker" id="stufe-12-4"></span>

平面上的两条直线或者交于一点，或者平行，或者重合（图 [38](#abb-38)）。恰好有两个交点是不可能的。这对每个线性方程组都成立，无论它有多大。

:::satz 定理 12.5 (解的个数)
<span class="anker" id="satz-12-5"></span>

线性方程组要么无解，要么恰有一个解，要么有无穷多解。
:::

:::beweis 解的个数
只需证明：如果方程组有两个不同的解 $\mathbf{x}\ne\mathbf{x}'$，它就有无穷多解。对每个数 $t$，

$$\mathbf{A}\bigl(\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})\bigr)=\mathbf{A}\mathbf{x}+t\,(\mathbf{A}\mathbf{x}'-\mathbf{A}\mathbf{x})=\mathbf{y}+t\,(\mathbf{y}-\mathbf{y})=\mathbf{y} ,$$

所以过 $\mathbf{x}$ 和 $\mathbf{x}'$ 的直线上的每个点 $\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})$ 都是解，而不同的 $t$ 值给出不同的点。
:::

右端项为零的方程组 $\mathbf{A}\mathbf{x}=\mathbf{0}$ 称为__齐次__方程组。它总有解 $\mathbf{x}=\mathbf{0}$。如果知道方程组 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 的一个解 $\mathbf{x}_{\mathrm s}$，把齐次方程组的解加上去，就得到所有其他解：$\mathbf{A}\mathbf{x}=\mathbf{y}$ 成立，当且仅当 $\mathbf{A}(\mathbf{x}-\mathbf{x}_{\mathrm s})=\mathbf{y}-\mathbf{y}=\mathbf{0}$。

::::beispiel [算例]
图 [38](#abb-38) 中的三个方程组：

<ol class="al">

<li>

$2x_1+x_2=5$，$x_1+x_2=3$：恰有一个解，$(2,\,1)^{\top}$。

</li>

<li>

$x_1+x_2=3$，$x_1+x_2=1$：无解，因为同一个和不可能既是 $3$ 又是 $1$。

</li>

<li>

$x_1+x_2=3$，$2x_1+2x_2=6$：第二个方程是第一个的两倍。一个解是 $\mathbf{x}_{\mathrm s}=(3,\,0)^{\top}$，而齐次方程组 $x_1+x_2=0$ 的解是 $(-1,\,1)^{\top}$ 的所有倍数。所以全部解为 $\mathbf{x}=(3,\,0)^{\top}+t\,(-1,\,1)^{\top}$，其中 $t$ 任意。

</li>

</ol>
::::

⁠**简而言之：**线性方程组无解、恰有一个解或有无穷多解；全部解等于一个解加上齐次方程组的解。

### 方程多于未知数

<span class="anker" id="stufe-12-5"></span>

对数据而言，方程个数与未知数个数常常不相称。假设要找面积的权重 $w_1$ 和房间的权重 $w_2$，使加权和对三套公寓都恰好等于实际价格。这是含两个未知数的三个方程。

:::definition 定义 12.6 (超定、欠定)
<span class="anker" id="satz-12-6"></span>

方程多于未知数（$m>n$）的线性方程组称为__超定的__，方程少于未知数（$m<n$）的称为__欠定的__。
:::

超定方程组通常无解：两个方程已经确定了两个未知数，第三个方程必须碰巧也成立。用列图来说：当 $n<m$ 时，$\mathbb{R}^m$ 中 $n$ 个列的列空间只是 $\mathbb{R}^m$ 的一小部分，右端项几乎从不落在其中。与此相反，欠定方程组只要有解，就有无穷多解：在行阶梯形中，至少有一个未知数没有自己的主元，它可以自由选取。

::::beispiel [算例]
对价格为 $200$、$130$ 和 $290$ 千欧元的公寓 1 至 3，方程组为

$$60\,w_1+2\,w_2=200,\qquad 40\,w_1+w_2=130,\qquad 90\,w_1+4\,w_2=290 .$$

由前两个方程得 $w_1=3$ 和 $w_2=10$：从第一个方程减去第二个方程的两倍，剩下 $-20\,w_1=-60$。然而代入第三个方程，得到 $270+40=310\ne290$。方程组无解。没有哪一对权重能恰好命中全部三个价格。在这种情况下应当改为寻找什么，是另一个问题。
::::

⁠**简而言之：**超定方程组的方程多于未知数，通常无解；欠定方程组的方程少于未知数，只要有解，就有无穷多解。

:::aufgabe 练习 28 ★★ 高斯消元法
<span class="anker" id="aufg-28"></span>

用高斯消元法求解，并验算结果：

$$x_1+x_2+x_3=6,\qquad 2x_1+3x_2+x_3=11,\qquad x_1-x_2+2x_3=5 .$$

:::loesung
增广矩阵为 $\Bigl(\begin{smallmatrix}1&1&1&|&6\\2&3&1&|&11\\1&-1&2&|&5\end{smallmatrix}\Bigr)$。从第二行减去第一行的两倍，从第三行减去第一行，得到行 $(0,\,1,\,-1\,|\,-1)$ 和 $(0,\,-2,\,1\,|\,-1)$。再把新的第二行的两倍加到第三行上，第三行就变为 $(0,\,0,\,-1\,|\,-3)$。行阶梯形为

$$x_1+x_2+x_3=6,\qquad x_2-x_3=-1,\qquad -x_3=-3 .$$

自下而上：$x_3=3$，$x_2=-1+3=2$，$x_1=6-2-3=1$。验算：$1+2+3=6$，$2+6+3=11$，$1-2+6=5$。解为 $\mathbf{x}=(1,\,2,\,3)^{\top}$。
:::
:::

:::aufgabe 练习 29 ★★ 有多少个解？
<span class="anker" id="aufg-29"></span>

求每个方程组的解集，并画出行图：

<ol class="al">

<li>

$x_1+2x_2=3$，$2x_1+4x_2=6$；

</li>

<li>

$x_1+2x_2=3$，$2x_1+4x_2=5$；

</li>

<li>

$x_1+2x_2=3$，$x_1-x_2=0$。

</li>

</ol>

:::loesung
(a) 第二个方程是第一个方程的两倍；两者描述同一条直线。有无穷多解：令 $x_2=t$，得 $x_1=3-2t$，所以 $\mathbf{x}=(3,\,0)^{\top}+t\,(-2,\,1)^{\top}$。

(b) 第一个方程的两倍是 $2x_1+4x_2=6$，与 $2x_1+4x_2=5$ 矛盾。两直线平行；无解。

(c) 由第二个方程得 $x_1=x_2$；代入第一个方程，得 $3x_2=3$。恰有一个解：$\mathbf{x}=(1,\,1)^{\top}$，即两条不平行直线的交点。
:::
:::

:::aufgabe 练习 30 ★★ 恰好吻合的权重
<span class="anker" id="aufg-30"></span>

在第 [12.5](#stufe-12-5) 小节的超定方程组中加入价格为 $240$ 千欧元的公寓 4。

<ol class="al">

<li>

$w_1=3$，$w_2=10$ 恰好命中四套公寓中的哪几套？

</li>

<li>

把含四个方程的方程组写成 $\mathbf{A}\mathbf{w}=\mathbf{y}$。$\mathbf{A}$、$\mathbf{w}$ 和 $\mathbf{y}$ 分别是什么型的？“无解”在列图中意味着什么？

</li>

</ol>

:::loesung
(a) 取 $w_1=3$，$w_2=10$：公寓 1：$180+20=200$（命中），公寓 2：$120+10=130$（命中），公寓 3：$270+40=310$，而不是 $290$（未命中），公寓 4：$210+30=240$（命中）。四个价格中有三个正确，但不是全部。

(b) $\mathbf{A}=\Biggl(\begin{smallmatrix}60&2\\40&1\\90&4\\70&3\end{smallmatrix}\Biggr)\in\mathbb{R}^{4\times2}$，$\mathbf{w}\in\mathbb{R}^2$，$\mathbf{y}=(200,\,130,\,290,\,240)^{\top}\in\mathbb{R}^4$。$\mathbf{A}$ 的列空间由面积列与房间列的所有组合 $w_1\mathbf{a}_1+w_2\mathbf{a}_2$ 组成；它是 $\mathbb{R}^4$ 中过原点的一个平面。“无解”意味着：价格向量 $\mathbf{y}$ 不在这个平面上。无论怎样选择两个权重，都不能恰好得到这四个价格。
:::
:::
