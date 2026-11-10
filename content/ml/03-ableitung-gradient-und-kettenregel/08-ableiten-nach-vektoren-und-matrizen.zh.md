---
title: 对向量和矩阵求导
pfad: 计算机科学 / 机器学习 / 数学基础 / 导数、梯度与链式法则
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: 第 3 章：导数、梯度与链式法则
nachschlagen: ja
order: 15230800
summary: 像 a top x 、 x top Ax 或 lVerty-AxrVert 2 这样的表达式的梯度会反复用到。本节先规定每种导数的形状，再逐分量推导最重要的公式。最后介绍对矩阵的导数，以及把灵敏度反向推过矩阵乘积的法则。
tags: 布局约定
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
像 $\mathbf{a}^{\top}\mathbf{x}$、$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ 或 $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ 这样的表达式的梯度会反复用到。本节先规定每种导数的形状，再逐分量推导最重要的公式。最后介绍对矩阵的导数，以及把灵敏度反向推过矩阵乘积的法则。
:::

### 布局约定

<span class="anker" id="stufe-7-1"></span>

一元函数的导数是一个数，没有什么需要排列的。对向量和矩阵，则必须规定把众多偏导数写成什么形状：写成一列还是一行，写成 $m\times n$ 矩阵还是 $n\times m$ 矩阵。这样的规定称为__布局约定__。从数学上说，每种选择都一样好；只是必须始终坚持同一种，否则公式会突然以转置的形式出现。

:::definition 定义 7.1 (本章的布局约定)
<span class="anker" id="satz-7-1"></span>

<ol class="rm">

<li>

向量是列。函数 $f:\mathbb{R}^n\to\mathbb{R}$ 的梯度是一列，形状与 $\mathbf{x}$ 相同。

</li>

<li>

函数 $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ 的雅可比矩阵是 $m\times n$ 矩阵：每个输出一行，每个输入一列。

</li>

<li>

函数 $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ 对矩阵 $\mathbf{A}$ 的导数是 $m\times n$ 矩阵 $\nabla_{\mathbf{A}}f$，它在位置 $(i,j)$ 上的元素为 $\partial f/\partial a_{ij}$，也就是说，它的形状与 $\mathbf{A}$ 相同。

</li>

</ol>
:::

表 [2](#tab-2) 对此作了总结。本章已经用过其中的两个推论：对只有一个输出的函数，雅可比矩阵就是写成一行的梯度，$\mathbf{J}_f=\nabla f^{\top}$。而梯度的链式法则需要转置，$\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$。规则 (iii) 在第 [7.5](#stufe-7-5) 节中要用到：把一个矩阵改变一个小矩阵 $\mathbf E$ 时，人们希望能逐个元素地比较 $\nabla_{\mathbf{A}}f$ 和 $\mathbf E$。

<span class="anker" id="tab-2"></span>

**表 2:** 导数的形状随函数类型而定（按本章的约定）。

| 函数 | 导数 | 形状 |
|---|---|---|
| $f:\mathbb{R}\to\mathbb{R}$ | $f'(x)$ | 数 |
| $f:\mathbb{R}^n\to\mathbb{R}$ | $\nabla f(\mathbf{x})$ | 列，$n\times1$（与 $\mathbf{x}$ 相同） |
| $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ | $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ | $m\times n$（第 $i$ 行是 $\nabla g_i^{\top}$） |
| $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ | $\nabla_{\mathbf{A}}f(\mathbf{A})$ | $m\times n$（与 $\mathbf{A}$ 相同） |

::::beispiel [算例]
对 $f(\mathbf{x})=x_1^2x_2+x_2^2$，在点 $(1,\,2)$ 处，梯度是列 $\nabla f=(4,\,5)^{\top}$，雅可比矩阵是行 $\mathbf{J}_f=(4\ \ 5)$。对式 [(5.1)](die-jacobi-matrix.html#gl-5-1) 中的 $\mathbf{g}$，$\mathbf{J}_{\mathbf{g}}$ 是 $2\times2$ 矩阵，它的第一行 $(2\ \ 1)$ 就是写成一行的 $g_1=x_1x_2$ 的梯度。
::::

⁠**简而言之：**在本章中，梯度具有其变量的形状，雅可比矩阵每个输出占一行；由此得出 $\mathbf{J}_f=\nabla f^{\top}$，以及梯度的链式法则中的转置。

:::hintergrund 文献中的其他约定
许多书把梯度写成一行。这样它就与只有一个输出的函数的雅可比矩阵相同，链式法则也完全不需要转置，因为这时 $\nabla(f\circ\mathbf{g})=\nabla f\,\mathbf{J}_{\mathbf{g}}$ 是行与矩阵的乘积。代价是梯度不再具有 $\mathbf{x}$ 的形状；沿最速上升方向的直线 $\mathbf{x}+t\,\nabla f$ 这时就需要转置。人们区分两种排列方式。在分子布局中，各行对应函数的分量，就像本章的雅可比矩阵那样。在分母布局中，各行对应变量的分量；这时向量值函数的导数是雅可比矩阵的转置。本章采用一种常见的混合布局：梯度写成列，雅可比矩阵采用分子布局。因此，不同来源的公式不能不加检查就组合使用。一种快速的检查是看形状：对 $\mathbf{x}\in\mathbb{R}^n$ 的梯度必须是有 $n$ 个元素的一列。更可靠的检查是一个小的数值例子。
:::

### 线性函数

<span class="anker" id="stufe-7-2"></span>

多元函数中最简单的是加权和。它的梯度简单到可以立即写出；推导过程展示了一种模式，本节其余所有公式都按这种模式得出。

:::satz 定理 7.2 (线性函数的梯度)
<span class="anker" id="satz-7-2"></span>

对固定的向量 $\mathbf{a},\mathbf{y}$ 和形状匹配的固定矩阵 $\mathbf{A}$，有

<span class="anker" id="gl-7-1"></span>
$$\nabla_{\mathbf{x}}(\mathbf{a}^{\top}\mathbf{x})=\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{a})=\mathbf{a},\qquad \nabla_{\mathbf{x}}(\mathbf{y}^{\top}\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\mathbf{y} . \tag{7.1}$$
:::

:::beweis 线性函数的梯度
$\mathbf{a}^{\top}\mathbf{x}=\sum_ja_jx_j$。对 $x_k$ 求导，只剩下 $j=k$ 的那一项，即 $a_k$。由于 $\mathbf{x}^{\top}\mathbf{a}=\mathbf{a}^{\top}\mathbf{x}$，对 $\mathbf{x}^{\top}\mathbf{a}$ 同样成立。对第二部分，令 $\mathbf{a}=\mathbf{A}^{\top}\mathbf{y}$，因为 $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}^{\top}\mathbf{y})^{\top}\mathbf{x}$。
:::

::::beispiel [算例]
在[第 1 章第 2.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2)中，对特征为 $\mathbf{x}_1=(60,\,2,\,3)^{\top}$ 的公寓 1，在权重 $\mathbf{w}=(3,\,10,\,-4)^{\top}$ 下的预测值为 $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$。把它看作权重的函数，它的梯度是 $\nabla_{\mathbf{w}}\hat y_1=\mathbf{x}_1=(60,\,2,\,3)^{\top}$。把 $w_1$ 增大 $0.1$，预测值就增加 $60\cdot0.1=6$，变为 $194$；实际上 $3.1\cdot60+10\cdot2-4\cdot3=194$。原因很简单：每个权重都与它的特征相乘，因此对一个权重的灵敏度恰好就是对应的特征。
::::

⁠**简而言之：**$\mathbf{a}^{\top}\mathbf{x}$ 对 $\mathbf{x}$ 的梯度是 $\mathbf{a}$，$\mathbf{y}^{\top}\mathbf{A}\mathbf{x}$ 的梯度是 $\mathbf{A}^{\top}\mathbf{y}$。

### 二次型

<span class="anker" id="stufe-7-3"></span>

[第 2 章第 5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5)中的二次型 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$，凡是对平方求和的地方都会出现。求导时，$\mathbf{x}$ 出现在两个位置，两处都有贡献，就像第 [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2) 节中的两条路径。

:::satz 定理 7.3 (二次型的梯度)
<span class="anker" id="satz-7-3"></span>

对矩阵 $\mathbf{A}\in\mathbb{R}^{n\times n}$，有

<span class="anker" id="gl-7-2"></span>
$$\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\,\mathbf{x} . \tag{7.2}$$

若 $\mathbf{A}$ 对称，则它等于 $2\mathbf{A}\mathbf{x}$。特别地，$\nabla\lVert\mathbf{x}\rVert^2=\nabla(\mathbf{x}^{\top}\mathbf{x})=2\mathbf{x}$。
:::

:::beweis 二次型的梯度
$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{j=1}^nx_i\,a_{ij}\,x_j$。对 $x_k$ 求导时，有两组项作出贡献：$i=k$ 的那些项，其导数为 $\sum_ja_{kj}x_j=(\mathbf{A}\mathbf{x})_k$；$j=k$ 的那些项，其导数为 $\sum_ix_ia_{ik}=(\mathbf{A}^{\top}\mathbf{x})_k$。$i=j=k$ 的那一项是 $a_{kk}x_k^2$，导数为 $2a_{kk}x_k$；它在两组中各以 $a_{kk}x_k$ 出现一次。所以梯度的第 $k$ 个分量是 $(\mathbf{A}\mathbf{x})_k+(\mathbf{A}^{\top}\mathbf{x})_k$。
:::

由[第 2 章第 5.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-2)，二次型只取决于对称部分 $\mathbf{S}=\tfrac12(\mathbf{A}+\mathbf{A}^{\top})$。这个公式与此吻合：$(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=2\mathbf{S}\mathbf{x}$。

::::beispiel [算例]
对 $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&3\end{smallmatrix}\bigr)$，$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=x_1^2+2x_1x_2+3x_2^2$，在点 $\mathbf{x}=(1,\,1)^{\top}$ 处等于 $6$。由式 [(7.2)](#gl-7-2)，

$$\nabla f(1,1)=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=\begin{pmatrix}2&2\\2&6\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}2+2\\2+6\end{pmatrix}=\begin{pmatrix}4\\8\end{pmatrix}.$$

用偏导数验算：$2x_1+2x_2=4$，$2x_1+6x_2=8$。只对对称矩阵成立的公式 $2\mathbf{A}\mathbf{x}=(6,\,6)^{\top}$ 在这里是错的。
::::

⁠**简而言之：**$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ 的梯度是 $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$，对对称的 $\mathbf{A}$ 即为 $2\mathbf{A}\mathbf{x}$；$\lVert\mathbf{x}\rVert^2$ 的梯度是 $2\mathbf{x}$。

### 残差的平方和

<span class="anker" id="stufe-7-4"></span>

在[第 2 章第 3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3)中，残差 $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ 是无解方程组 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 的误差向量，要找的是残差最短的那个 $\mathbf{x}$。平方和 $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ 是 $\mathbf{x}$ 的函数，它的梯度说明它如何响应 $\mathbf{x}$ 的变化。

:::satz 定理 7.4 (平方和的梯度)
<span class="anker" id="satz-7-4"></span>

对 $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$，其中 $\mathbf{A}\in\mathbb{R}^{m\times n}$，$\mathbf{y}\in\mathbb{R}^m$，有

<span class="anker" id="gl-7-3"></span>
$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})=2\mathbf{A}^{\top}(\mathbf{A}\mathbf{x}-\mathbf{y}). \tag{7.3}$$
:::

:::beweis 平方和的梯度
这个函数是一个复合：先由仿射映射 $\mathbf{r}(\mathbf{x})=\mathbf{y}-\mathbf{A}\mathbf{x}$ 得到残差，再由 $\mathbf{r}\mapsto\lVert\mathbf{r}\rVert^2$ 得到它的平方和。由第 [5.4](die-jacobi-matrix.html#stufe-5-4) 节，$\mathbf{J}_{\mathbf{r}}=-\mathbf{A}$；由式 [(7.2)](#gl-7-2)，$\nabla_{\mathbf{r}}\lVert\mathbf{r}\rVert^2=2\mathbf{r}$。链式法则式 [(6.3)](die-kettenregel-fur-mehrere-variablen.html#gl-6-3) 给出 $\nabla f=(-\mathbf{A})^{\top}\,2\mathbf{r}=-2\mathbf{A}^{\top}\mathbf{r}$。
:::

::::beispiel [算例]
设 $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$，$\mathbf{y}=(1,\,0)^{\top}$，$\mathbf{x}=(2,\,1)^{\top}$。于是 $\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$，残差为 $\mathbf{r}=(-3,\,-1)^{\top}$，$f(\mathbf{x})=9+1=10$。由 $\mathbf{A}^{\top}\mathbf{r}=(-3,\,-7)^{\top}$ 得（图 [13](#abb-13)）

$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}\mathbf{r}=-2\begin{pmatrix}-3\\-7\end{pmatrix}=\begin{pmatrix}6\\14\end{pmatrix}$$

验算：展开写出，$f(\mathbf{x})=(1-x_1-2x_2)^2+x_2^2$，其偏导数为 $-2\,(1-x_1-2x_2)=6$ 和 $-4\,(1-x_1-2x_2)+2x_2=12+2=14$。

:::abbildung ml/k3rresiduum 13
平方和 $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ 的梯度：$\mathbf{A}^{\top}\mathbf{r}$ 的每个分量都是 $\mathbf{A}$ 的一列与残差的点积。
:::
::::

这个公式与[第 2 章](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html)的结果相衔接。在那里，最佳近似解 $\hat{\mathbf{x}}$ 的残差垂直于 $\mathbf{A}$ 的所有列，即 $\mathbf{A}^{\top}\hat{\mathbf{r}}=\mathbf{0}$，由此得出正规方程 $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$。由式 [(7.3)](#gl-7-3)，这意味着：在点 $\hat{\mathbf{x}}$ 处，平方和的梯度为零；除二阶项外，平方和在那里沿任何方向都既不上升也不下降。对[第 2 章第 3.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-3)中的例子，矩阵为 $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$，$\mathbf{y}=(1,\,1,\,1)^{\top}$，$\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$，有 $\hat{\mathbf{r}}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$ 和 $\mathbf{A}^{\top}\hat{\mathbf{r}}=(\tfrac13-\tfrac13,\ \tfrac13-\tfrac13)^{\top}=\mathbf{0}$。

⁠**简而言之：**$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ 的梯度是 $-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$；它恰好在残差垂直于 $\mathbf{A}$ 的各列的地方为零。

### 对矩阵求导

<span class="anker" id="stufe-7-5"></span>

有时变量不是一个向量，而是整个矩阵：改变矩阵的一个元素时，一个数会怎样变化？按约定的规则 (iii)，把 $m\cdot n$ 个偏导数按矩阵的形状排列。这样线性近似照常成立，只是点积要遍历所有元素：

<span class="anker" id="gl-7-4"></span>
$$f(\mathbf{A}+\mathbf E)\approx f(\mathbf{A})+\sum_{i=1}^m\sum_{j=1}^n\bigl(\nabla_{\mathbf{A}}f\bigr)_{ij}\,e_{ij} \tag{7.4}$$

其中 $\mathbf E$ 是元素为 $e_{ij}$ 的小矩阵。这个双重求和等于 $\operatorname{tr}\bigl((\nabla_{\mathbf{A}}f)^{\top}\mathbf E\bigr)$，其中的迹见[第 2 章第 6.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5)。

:::satz 定理 7.5 (对矩阵的两个导数)
<span class="anker" id="satz-7-5"></span>

对固定的向量 $\mathbf{u}\in\mathbb{R}^m$、$\mathbf{v}\in\mathbb{R}^n$ 和矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$，有

<span class="anker" id="gl-7-5"></span>
$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top},\qquad \nabla_{\mathbf{A}}\lVert\mathbf{A}\rVert_F^2=2\mathbf{A} . \tag{7.5}$$

其中 $\lVert\mathbf{A}\rVert_F$ 是[第 2 章第 10.1 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/naherung-durch-matrizen-von-kleinem-rang.html#stufe-10-1)中的 Frobenius 范数。
:::

:::beweis 对矩阵的两个导数
$\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\sum_i\sum_ju_i\,a_{ij}\,v_j$。元素 $a_{ij}$ 恰好出现在一项中，因子为 $u_iv_j$。所以 $\partial(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})/\partial a_{ij}=u_iv_j$，这正是[第 1 章第 9.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5)中外积 $\mathbf{u}\mathbf{v}^{\top}$ 的元素 $(i,j)$。同样，$\lVert\mathbf{A}\rVert_F^2=\sum_{i,j}a_{ij}^2$，它的 $\partial/\partial a_{ij}$ 为 $2a_{ij}$。
:::

::::beispiel [算例]
对 $\mathbf{u}=(1,\,2)^{\top}$ 和 $\mathbf{v}=(3,\,-1)^{\top}$，有

$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}=\begin{pmatrix}3&-1\\6&-2\end{pmatrix},$$

而且在每个点 $\mathbf{A}$ 处都是如此，因为这个函数对 $\mathbf{A}$ 是线性的。当 $\mathbf{A}=\mathbf{I}$ 时，$\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}=3-2=1$。把元素 $a_{21}$ 增大 $0.1$，梯度预测的变化为 $6\cdot0.1=0.6$。实际上，$a_{21}$ 只出现在项 $u_2\,a_{21}\,v_1=2\cdot a_{21}\cdot3$ 中，而这一项正好增加 $0.6$。
::::

⁠**简而言之：**一个数对矩阵的导数具有该矩阵的形状；对 $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}$，它是外积 $\mathbf{u}\mathbf{v}^{\top}$，对 $\lVert\mathbf{A}\rVert_F^2$，它是 $2\mathbf{A}$。

### 反向通过矩阵乘积

<span class="anker" id="stufe-7-6"></span>

矩阵-向量乘积 $\mathbf{y}=\mathbf{A}\mathbf{x}$ 常常只是一个较长计算的中间步骤，这个计算的末尾是一个数 $f(\mathbf{y})$。如果已经知道这个数如何响应 $\mathbf{y}$，即 $\nabla f(\mathbf{y})$，人们就想从中读出它如何响应 $\mathbf{A}$ 和 $\mathbf{x}$。这种反向通过一个构件的计算，正是第 [10](automatische-differentiation.html#stufe-10) 节中反向模式的范本。

:::satz 定理 7.6 (矩阵乘积的反向法则)
<span class="anker" id="satz-7-6"></span>

设 $f:\mathbb{R}^m\to\mathbb{R}$ 可微，$\mathbf{y}=\mathbf{A}\mathbf{x}$，其中 $\mathbf{A}\in\mathbb{R}^{m\times n}$，并设 $F(\mathbf{A},\mathbf{x})=f(\mathbf{A}\mathbf{x})$。则

<span class="anker" id="gl-7-6"></span>
$$\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\,\nabla f(\mathbf{y}). \tag{7.6}$$

更一般地，对 $\mathbf{C}=\mathbf{A}\mathbf{B}$ 和 $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$，有 $\nabla_{\mathbf{A}}F=(\nabla_{\mathbf{C}}f)\,\mathbf{B}^{\top}$ 和 $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\,(\nabla_{\mathbf{C}}f)$。
:::

:::beweis 矩阵乘积的反向法则
$y_i=\sum_ka_{ik}x_k$。元素 $a_{ij}$ 只影响 $y_i$，影响的因子为 $\partial y_i/\partial a_{ij}=x_j$。所以从 $a_{ij}$ 到 $f$ 只有一条路径，$\partial F/\partial a_{ij}=\frac{\partial f}{\partial y_i}\,x_j$；这正是 $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$ 的元素 $(i,j)$。而变量 $x_j$ 影响每个 $y_i$，因子为 $a_{ij}$；对所有路径求和，得 $\partial F/\partial x_j=\sum_i\frac{\partial f}{\partial y_i}\,a_{ij}$，即 $\mathbf{A}^{\top}\nabla f(\mathbf{y})$ 的第 $j$ 个分量。第二个结论同理可得，因为 $\mathbf{C}=\mathbf{A}\mathbf{B}$ 逐列来看就是矩阵-向量乘积。
:::

::::beispiel [算例]
在[第 1 章第 7.1 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-1)中，$\mathbf{A}=\Bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\Bigr)$，$\mathbf{x}=(2,\,1)^{\top}$，于是 $\mathbf{y}=\mathbf{A}\mathbf{x}=(4,\,-1,\,7)^{\top}$。设 $f(\mathbf{y})=y_1-y_3=-3$，则 $\nabla f(\mathbf{y})=(1,\,0,\,-1)^{\top}$。由式 [(7.6)](#gl-7-6) 得（图 [14](#abb-14)）

$$\nabla_{\mathbf{A}}F=\begin{pmatrix}1\\0\\-1\end{pmatrix}\begin{pmatrix}2&1\end{pmatrix}=\begin{pmatrix}2&1\\0&0\\-2&-1\end{pmatrix},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\begin{pmatrix}1\\0\\-1\end{pmatrix}=\begin{pmatrix}-2\\1\end{pmatrix}$$

验算：展开写出，$F=(x_1+2x_2)-(3x_1+x_2)=-2x_1+x_2$，其梯度为 $(-2,\,1)^{\top}$。$\nabla_{\mathbf{A}}F$ 的第二行为零，因为 $y_2$ 不出现在 $f$ 中；$\mathbf{A}$ 第二行的元素只作用于 $y_2$。

:::abbildung ml/k3rrueck 14
对矩阵-向量乘积的输入求梯度：每个分量都遍历所有三个输出 $y_i$，把 $f$ 对 $y_i$ 的响应强度汇总起来，每一项以 $x_j$ 作用于 $y_i$ 的因子 $a_{ij}$ 为权重。
:::
::::

:::warnung 形状检查是助记方法，不是证明
形状几乎就确定了式 [(7.6)](#gl-7-6)：$\nabla_{\mathbf{A}}F$ 必须具有 $m\times n$ 的形状，而由有 $m$ 个元素的列 $\nabla f(\mathbf{y})$ 和有 $n$ 个元素的列 $\mathbf{x}$，只有 $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$ 能得到这个形状。可以这样记住这条法则。但形状检查既发现不了错误的符号，也发现不了缺失的因子，对方阵也发现不了颠倒的顺序。只有用分量进行的计算才能证明这条法则。
:::

⁠**简而言之：**反向通过 $\mathbf{y}=\mathbf{A}\mathbf{x}$：对 $\mathbf{A}$ 的梯度是 $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$，对 $\mathbf{x}$ 的梯度是 $\mathbf{A}^{\top}\nabla f(\mathbf{y})$。

:::aufgabe 练习 24 ★ 矩阵记号下的梯度
<span class="anker" id="aufg-24"></span>

用本节的公式计算，并分别用偏导数验算。

<ol class="al">

<li>

$f(\mathbf{x})=\mathbf{b}^{\top}\mathbf{x}+5$，其中 $\mathbf{b}=(2,\,-1,\,4)^{\top}$；

</li>

<li>

$f(\mathbf{x})=\lVert\mathbf{x}\rVert^2$，在点 $(1,\,-1,\,2)$ 处；

</li>

<li>

$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$，其中 $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\3&4\end{smallmatrix}\bigr)$，在点 $(1,\,-1)$ 处。

</li>

</ol>

:::loesung
(a) 由式 [(7.1)](#gl-7-1)，$\nabla f=\mathbf{b}=(2,\,-1,\,4)^{\top}$。验算：$f=2x_1-x_2+4x_3+5$。

(b) 由式 [(7.2)](#gl-7-2)，取 $\mathbf{A}=\mathbf{I}$，得 $\nabla f=2\mathbf{x}=(2,\,-2,\,4)^{\top}$。验算：$\partial_jf=2x_j$。

(c) $\mathbf{A}+\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&4\\4&8\end{smallmatrix}\bigr)$，所以 $\nabla f(1,-1)=(4-4,\ 4-8)^{\top}=(0,\,-4)^{\top}$。验算：$f=2x_1^2+4x_1x_2+4x_2^2$ 的偏导数为 $4x_1+4x_2=0$ 和 $4x_1+8x_2=-4$。
:::
:::

:::aufgabe 练习 25 ★★ 第 2 章中的最小二乘直线
<span class="anker" id="aufg-25"></span>

在[第 2 章第 3.6 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-6)中，用 $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$ 和 $\mathbf{y}=(1,\,2,\,4)^{\top}$ 对点 $(0,\,1)$、$(1,\,2)$ 和 $(2,\,4)$ 拟合了一条直线。

<ol class="al">

<li>

在点 $\mathbf{x}=(1,\,1)^{\top}$ 处计算 $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ 和 $\nabla f(\mathbf{x})$。

</li>

<li>

应当把 $\mathbf{x}$ 从 $(1,\,1)$ 出发朝哪个方向移动一小段，才能使 $f$ 减小得最快？

</li>

<li>

证明：在[第 2 章](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html)中的点 $\hat{\mathbf{x}}=(\tfrac56,\,\tfrac32)^{\top}$ 处，梯度为零。

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$，$\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}=(0,\,0,\,1)^{\top}$，$f=1$。由 $\mathbf{A}^{\top}\mathbf{r}=(0+0+1,\ 0+0+2)^{\top}=(1,\,2)^{\top}$，得 $\nabla f=-2\mathbf{A}^{\top}\mathbf{r}=(-2,\,-4)^{\top}$。

(b) $f$ 沿方向 $-\nabla f/\lVert\nabla f\rVert=(2,\,4)^{\top}/\sqrt{20}=(1,\,2)^{\top}/\sqrt5\approx(0.447,\ 0.894)^{\top}$ 减小得最快：截距应稍微增大，斜率的增量则是截距增量的两倍。这符合以下事实：直线 $1+t$ 与第三个点 $(2,\,4)$ 相差 $1$。

(c) $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\ \tfrac73,\ \tfrac{23}6)^{\top}$，所以 $\hat{\mathbf{r}}=(\tfrac16,\ -\tfrac13,\ \tfrac16)^{\top}$，并且

$$\mathbf{A}^{\top}\hat{\mathbf{r}}=\begin{pmatrix}\tfrac16-\tfrac13+\tfrac16\\0-\tfrac13+\tfrac26\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.$$

梯度为零：在最佳近似解处，任何小的位移都不会使平方和发生一阶变化。
:::
:::

:::aufgabe 练习 26 ★★ 对矩阵的导数
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

对方阵 $\mathbf{A}$，证明 $\nabla_{\mathbf{A}}\operatorname{tr}\mathbf{A}=\mathbf{I}$。

</li>

<li>

利用式 [(7.6)](#gl-7-6) 和 $\nabla\lVert\mathbf{y}\rVert^2=2\mathbf{y}$ 证明 $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$，并对 $\mathbf{A}=\mathbf{I}\in\mathbb{R}^{2\times2}$ 和 $\mathbf{x}=(1,\,2)^{\top}$ 计算它。

</li>

<li>

用线性近似式 [(7.4)](#gl-7-4) 检验 (b)：把 $a_{12}$ 从 $0$ 增大到 $0.01$ 时，$\lVert\mathbf{A}\mathbf{x}\rVert^2$ 大约改变多少？请验算。

</li>

</ol>

:::loesung
(a) $\operatorname{tr}\mathbf{A}=\sum_ia_{ii}$。对 $a_{ij}$ 的导数在 $i=j$ 时为 $1$，否则为 $0$；按 $\mathbf{A}$ 的形状排列，就是 $\mathbf{I}$。

(b) $\lVert\mathbf{A}\mathbf{x}\rVert^2=f(\mathbf{y})$，其中 $\mathbf{y}=\mathbf{A}\mathbf{x}$，$\nabla f(\mathbf{y})=2\mathbf{y}$。由式 [(7.6)](#gl-7-6)，$\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\mathbf{y}\,\mathbf{x}^{\top}=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$。对 $\mathbf{A}=\mathbf{I}$ 和 $\mathbf{x}=(1,\,2)^{\top}$：

$$\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\begin{pmatrix}1\\2\end{pmatrix}\begin{pmatrix}1&2\end{pmatrix}=\begin{pmatrix}2&4\\4&8\end{pmatrix}.$$

(c) 梯度的元素 $(1,2)$ 是 $4$，所以式 [(7.4)](#gl-7-4) 预测的变化约为 $4\cdot0.01=0.04$。精确计算：取 $a_{12}=0.01$，有 $\mathbf{A}\mathbf{x}=(1.02,\ 2)^{\top}$，$\lVert\mathbf{A}\mathbf{x}\rVert^2=1.0404+4=5.0404$，即相对于 $5$ 改变了 $0.0404$。
:::
:::

:::aufgabe 练习 27 ★★★ 两个矩阵之积的反向法则
<span class="anker" id="aufg-27"></span>

设 $\mathbf{C}=\mathbf{A}\mathbf{B}$，$F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$，并记 $\mathbf G=\nabla_{\mathbf{C}}f$。

<ol class="al">

<li>

逐分量证明 $\nabla_{\mathbf{A}}F=\mathbf G\mathbf{B}^{\top}$ 和 $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\mathbf G$。

</li>

<li>

对 $\mathbf{A}=(1\ \ 2)$、$\mathbf{B}=\bigl(\begin{smallmatrix}3\\4\end{smallmatrix}\bigr)$ 和 $f(\mathbf{C})=c_{11}^2$，把 $F$ 展开写出，检验这两个公式。

</li>

</ol>

:::loesung
(a) 有 $c_{ik}=\sum_ja_{ij}b_{jk}$。元素 $a_{ij}$ 作用于第 $i$ 行的所有 $c_{ik}$，因子为 $b_{jk}$；对这些路径求和，得 $\partial F/\partial a_{ij}=\sum_kg_{ik}b_{jk}=(\mathbf G\mathbf{B}^{\top})_{ij}$。元素 $b_{jk}$ 作用于第 $k$ 列的所有 $c_{ik}$，因子为 $a_{ij}$；所以 $\partial F/\partial b_{jk}=\sum_ia_{ij}g_{ik}=(\mathbf{A}^{\top}\mathbf G)_{jk}$。

(b) $\mathbf{C}=1\cdot3+2\cdot4=11$，$F=121$，$\mathbf G=2c_{11}=22$。公式给出 $\nabla_{\mathbf{A}}F=22\,(3\ \ 4)=(66\ \ 88)$ 和 $\nabla_{\mathbf{B}}F=(1,\,2)^{\top}\cdot22=(22,\,44)^{\top}$。展开写出：$F=(3a_{11}+4a_{12})^2$，导数为 $2\cdot11\cdot3=66$ 和 $2\cdot11\cdot4=88$；$F=(b_{11}+2b_{21})^2$，导数为 $22$ 和 $44$。
:::
:::
