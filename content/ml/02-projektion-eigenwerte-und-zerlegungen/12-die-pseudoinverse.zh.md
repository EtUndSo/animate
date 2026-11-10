---
title: 伪逆
pfad: 计算机科学 / 机器学习 / 数学基础 / 投影、特征值与矩阵分解
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: 第 2 章：投影、特征值与矩阵分解
nachschlagen: ja
order: 15221200
summary: 在第 1 章中，只有列线性无关的方阵才有逆矩阵。本节给每个矩阵一种逆：方程多于未知数时，有从左边求逆的逆；方程少于未知数时，有从右边求逆的逆；还有一种适用于所有情形的逆，即伪逆。它总是给出最佳近似解，而在有多个最佳近似解时给出最短的那个。
tags: 左逆, 右逆, 伪逆
lang: zh
---

<span class="anker" id="stufe-11"></span>

:::zweck
在[第 1 章](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html)中，只有列线性无关的方阵才有逆矩阵。本节给每个矩阵一种逆：方程多于未知数时，有从左边求逆的逆；方程少于未知数时，有从右边求逆的逆；还有一种适用于所有情形的逆，即伪逆。它总是给出最佳近似解，而在有多个最佳近似解时给出最短的那个。
:::

### 左逆

<span class="anker" id="stufe-11-1"></span>

$m>n$ 的高矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 没有逆矩阵；它甚至不是方阵。但它可以具有逆矩阵性质的一半。

:::definition 定义 11.1 (左逆)
<span class="anker" id="satz-11-1"></span>

满足 $\mathbf F\mathbf{A}=\mathbf{I}_n$ 的矩阵 $\mathbf F\in\mathbb{R}^{n\times m}$ 称为 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 的__左逆__。
:::

:::satz 定理 11.2 (左逆)
<span class="anker" id="satz-11-2"></span>

$\mathbf{A}$ 有左逆，当且仅当它的列线性无关。此时

<span class="anker" id="gl-11-1"></span>
$$\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{11.1}$$

是一个左逆，并且 $\mathbf F\mathbf{y}$ 是 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 的最佳近似解。
:::

:::beweis 左逆
若各列线性无关，则由第 [3.5](die-beste-naherungslosung.html#stufe-3-5) 节，$\mathbf{A}^{\top}\mathbf{A}$ 可逆，且 $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$。由式 [(3.5)](die-beste-naherungslosung.html#gl-3-5)，$\mathbf F\mathbf{y}=\hat{\mathbf{x}}$。反之：若 $\mathbf{A}$ 有左逆且 $\mathbf{A}\mathbf{x}=\mathbf{0}$，则 $\mathbf{x}=\mathbf F\mathbf{A}\mathbf{x}=\mathbf F\mathbf{0}=\mathbf{0}$；所以零空间为 $\{\mathbf{0}\}$，各列线性无关。
:::

从右边乘时，$\mathbf F$ 并不起逆的作用。由式 [(4.1)](projektion-auf-einen-unterraum.html#gl-4-1)，乘积 $\mathbf{A}\mathbf F=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ 是向列空间的投影，而当 $m>n$ 时，它不是 $\mathbf{I}_m$。此外，高矩阵有许多左逆；式 [(11.1)](#gl-11-1) 是与正交投影相对应的那一个。

::::beispiel [算例]
对于列为 $(1,\,0,\,1)^{\top}$ 和 $(0,\,1,\,1)^{\top}$ 的 $\mathbf{H}$，有 $(\mathbf{H}^{\top}\mathbf{H})^{-1}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$，以及

$$\mathbf F=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\end{pmatrix}.$$

有 $\mathbf F\mathbf{H}=\tfrac13\bigl(\begin{smallmatrix}2+1&-1+1\\-1+1&2+1\end{smallmatrix}\bigr)=\mathbf{I}_2$，而 $\mathbf F(1,\,1,\,1)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$ 就是第 [3.3](die-beste-naherungslosung.html#stufe-3-3) 节中的最佳近似解。$\mathbf{H}\mathbf F$ 是第 [4.2](projektion-auf-einen-unterraum.html#stufe-4-2) 节中的投影矩阵 $\tfrac13\Bigl(\begin{smallmatrix}2&-1&1\\-1&2&1\\1&1&2\end{smallmatrix}\Bigr)$。另一个左逆是 $\bigl(\begin{smallmatrix}1&0&0\\0&1&0\end{smallmatrix}\bigr)$，因为 $\mathbf{H}$ 的前两行构成单位矩阵；但对于 $(1,\,1,\,1)^{\top}$，它给出的不是最佳近似解，而是 $(1,\,1)^{\top}$。
::::

⁠**简而言之：**列线性无关的矩阵有左逆 $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$；它把 $\mathbf{y}$ 映射为最佳近似解。

### 右逆

<span class="anker" id="stufe-11-2"></span>

对于 $m<n$ 的宽矩阵，方程个数少于未知数个数。若方程组可解，它就有无穷多个解。右逆从中选出一个，而且是一个特殊的解。

:::definition 定义 11.3 (右逆)
<span class="anker" id="satz-11-3"></span>

满足 $\mathbf{A}\mathbf G=\mathbf{I}_m$ 的矩阵 $\mathbf G\in\mathbb{R}^{n\times m}$ 称为 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 的__右逆__。
:::

:::satz 定理 11.4 (右逆与最短解)
<span class="anker" id="satz-11-4"></span>

若 $\mathbf{A}$ 的行线性无关，则

<span class="anker" id="gl-11-2"></span>
$$\mathbf G=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1} \tag{11.2}$$

是一个右逆。对每个 $\mathbf{y}$，$\mathbf{x}=\mathbf G\mathbf{y}$ 都是 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 的解，并且在所有解中长度最小。
:::

:::beweis 右逆
$\mathbf{A}$ 的行就是 $\mathbf{A}^{\top}$ 的列；把第 [3.5](die-beste-naherungslosung.html#stufe-3-5) 节的结论应用于 $\mathbf{A}^{\top}$，可知 $\mathbf{A}\mathbf{A}^{\top}$ 可逆。于是 $\mathbf{A}\mathbf G=\mathbf{A}\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}=\mathbf{I}$，$\mathbf{A}\mathbf G\mathbf{y}=\mathbf{y}$。若 $\mathbf{x}$ 是任意一个解，则 $\mathbf{A}(\mathbf{x}-\mathbf G\mathbf{y})=\mathbf{0}$，所以 $\mathbf{z}=\mathbf{x}-\mathbf G\mathbf{y}$ 在零空间中。向量 $\mathbf G\mathbf{y}=\mathbf{A}^{\top}\mathbf{w}$（其中 $\mathbf{w}=(\mathbf{A}\mathbf{A}^{\top})^{-1}\mathbf{y}$）垂直于零空间中的每个向量，因为 $(\mathbf{A}^{\top}\mathbf{w})^{\top}\mathbf{z}=\mathbf{w}^{\top}\mathbf{A}\mathbf{z}=0$。由勾股定理，

$$\lVert\mathbf{x}\rVert^2=\lVert\mathbf G\mathbf{y}+\mathbf{z}\rVert^2=\lVert\mathbf G\mathbf{y}\rVert^2+\lVert\mathbf{z}\rVert^2\ge\lVert\mathbf G\mathbf{y}\rVert^2 ,$$

等号只在 $\mathbf{z}=\mathbf{0}$ 时成立。
:::

从几何上看，解集是一条不过原点的直线或一个不过原点的平面，$\mathbf G\mathbf{y}$ 是其中离原点最近的点：从原点所作垂线的垂足。

::::beispiel [算例]
单个方程 $x_1+2x_2=5$ 对应 $\mathbf{A}=(1\ \ 2)$，$\mathbf{A}\mathbf{A}^{\top}=5$。所以 $\mathbf G=\tfrac15(1,\,2)^{\top}$，$\mathbf G\cdot5=(1,\,2)^{\top}$。所有的解为 $(1,\,2)^{\top}+t\,(2,\,-1)^{\top}$，长度的平方为 $(1+2t)^2+(2-t)^2=5+5t^2$；$t=0$ 时解最短。向量 $(1,\,2)^{\top}$ 垂直于方向为 $(2,\,-1)^{\top}$ 的解直线。
::::

⁠**简而言之：**行线性无关的矩阵有右逆 $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$；它给出最短解。

### 伪逆

<span class="anker" id="stufe-11-3"></span>

若 $\mathbf{A}$ 的列不线性无关、行也不线性无关，两个公式就都失效了。一个例子是第 [3.5](die-beste-naherungslosung.html#stufe-3-5) 节中的 $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$：对于 $\mathbf{y}=(1,\,1)^{\top}$，直线 $x_1+2x_2=\tfrac35$ 上的所有点都是最佳近似解。奇异值分解为每个矩阵都提供了一个公式。

:::definition 定义 11.5 (伪逆)
<span class="anker" id="satz-11-5"></span>

设 $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$，秩为 $r$。矩阵 $\mathbf{D}^+\in\mathbb{R}^{n\times m}$ 由 $\mathbf{D}^{\top}$ 得到：把每个 $d_j>0$ 换成 $1/d_j$，零保持不变。$\mathbf{A}$ 的__伪逆__为

<span class="anker" id="gl-11-3"></span>
$$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\sum_{j=1}^r\frac1{d_j}\,\mathbf{v}_j\mathbf{u}_j^{\top} . \tag{11.3}$$
:::

每个构件都把 $\mathbf{A}$ 的一个构件反转过来：$\mathbf{A}$ 把 $\mathbf{v}_j$ 映射为 $d_j\mathbf{u}_j$，$\mathbf{A}^+$ 把 $\mathbf{u}_j$ 映射为 $\mathbf{v}_j/d_j$。对于 $\mathbf{A}$ 达不到的方向 $\mathbf{u}_j$（$j>r$），$\mathbf{A}^+$ 把它们映射为零，而不是除以零。若 $\mathbf{A}$ 可逆，则 $\mathbf{A}^+=\mathbf{A}^{-1}$，因为这时 $\mathbf{A}^{-1}=(\mathbf{V}^{\top})^{-1}\mathbf{D}^{-1}\mathbf{U}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$。

::::beispiel [算例]
$\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ 是对称半正定矩阵，有属于 $\mathbf{q}=(1,\,2)^{\top}/\sqrt5$ 的特征值 $5$ 和特征值 $0$。由第 [9.7](die-singularwertzerlegung.html#stufe-9-7) 节，$\mathbf{A}=5\,\mathbf{q}\mathbf{q}^{\top}$ 是它的紧凑分解，其中 $d_1=5$，$\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$。因此

$$\mathbf{A}^+=\frac15\,\mathbf{q}\mathbf{q}^{\top}=\frac1{25}\begin{pmatrix}1&2\\2&4\end{pmatrix}.$$
::::

⁠**简而言之：**伪逆 $\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ 把每个 $d_j>0$ 的构件 $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ 反转过来，并把属于奇异值 $0$ 的方向映射为零。

### 最短的最佳近似解

<span class="anker" id="stufe-11-4"></span>

$\mathbf{A}^+\mathbf{y}$ 能做到什么？它把前面两个小节结合了起来。

:::satz 定理 11.6 (伪逆与最小二乘法)
<span class="anker" id="satz-11-6"></span>

对每个矩阵 $\mathbf{A}$ 和每个向量 $\mathbf{y}$，向量 $\mathbf{x}^+=\mathbf{A}^+\mathbf{y}$ 都是 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 的一个最佳近似解，并且在所有最佳近似解中长度最小。特别地，

$$\begin{gathered} \mathbf{A}^+=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\quad\text{列线性无关时},\\ \mathbf{A}^+=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}\quad\text{行线性无关时}. \end{gathered}$$
:::

:::beweis 伪逆
在奇异向量的坐标下计算：$\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$，$\boldsymbol\beta=\mathbf{U}^{\top}\mathbf{y}$。由于 $\mathbf{U}^{\top}$ 保持长度不变，

$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{U}^{\top}\mathbf{y}-\mathbf{D}\mathbf{V}^{\top}\mathbf{x}\rVert^2=\lVert\boldsymbol\beta-\mathbf{D}\mathbf{c}\rVert^2=\sum_{j=1}^r(\beta_j-d_jc_j)^2+\sum_{j=r+1}^m\beta_j^2 .$$

第二个和与 $\mathbf{x}$ 无关。第一个和恰好在对所有 $j\le r$ 都有 $c_j=\beta_j/d_j$ 时为零，从而尽可能小；$j>r$ 的 $c_j$ 根本不出现。所以最佳近似解恰好是这样的 $\mathbf{x}=\mathbf{V}\mathbf{c}$：对 $j\le r$ 有 $c_j=\beta_j/d_j$，而 $c_{r+1},\dots,c_n$ 任意。它们的长度为 $\lVert\mathbf{x}\rVert^2=\lVert\mathbf{c}\rVert^2=\sum_{j\le r}(\beta_j/d_j)^2+\sum_{j>r}c_j^2$，在 $j>r$ 时取 $c_j=0$ 最小。这个 $\mathbf{c}$ 就是 $\mathbf{D}^+\boldsymbol\beta$，所以 $\mathbf{x}=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}\mathbf{y}=\mathbf{A}^+\mathbf{y}$。

在各列线性无关时，由第 [3.5](die-beste-naherungslosung.html#stufe-3-5) 节，只有一个最佳近似解 $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$；它必然与 $\mathbf{A}^+\mathbf{y}$ 一致，而且对每个 $\mathbf{y}$ 都如此。在各行线性无关时，由[第 1 章第 13.4 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-4)，秩等于 $m$，所以列空间是整个 $\mathbb{R}^m$，方程组对每个 $\mathbf{y}$ 都可解；最佳近似解就是方程组的解，由第 [11.2](#stufe-11-2) 节，其中最短的是 $\mathbf G\mathbf{y}$。
:::

::::beispiel [算例 1]
对于 $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ 和 $\mathbf{y}=(1,\,1)^{\top}$，得 $\mathbf{x}^+=\tfrac1{25}(1+2,\ 2+4)^{\top}=(0.12,\ 0.24)^{\top}$。它在最佳近似解构成的直线上，因为 $0.12+2\cdot0.24=0.6=\tfrac35$；它沿 $(1,\,2)^{\top}$ 方向，垂直于这条直线：它是直线上离原点最近的点。
::::

::::beispiel [算例 2]
对同一个量测量三次，结果为 $4$、$5$ 和 $9$。方程组“$x=4$，$x=5$，$x=9$”的矩阵是 $\mathbf{1}\in\mathbb{R}^{3\times1}$，即一个全 1 列。它的列线性无关，所以 $\mathbf{1}^+=(\mathbf{1}^{\top}\mathbf{1})^{-1}\mathbf{1}^{\top}=\tfrac13(1,\,1,\,1)$，并且

$$x^+=\tfrac13\,\mathbf{1}^{\top}\mathbf{y}=\tfrac13\,(4+5+9)=6 ,$$

即平均值（图 [27](#abb-27)）。多次测量的平均值，就是把每次测量都当作精确值的那个方程组的最佳近似解。

:::abbildung ml/k2rmittel 27
全 1 列的伪逆作用于测量值 $\mathbf{y}=(4,5,9)^{\top}$：与 $\mathbf{1}$ 的点积是测量值之和，除以 $\mathbf{1}^{\top}\mathbf{1}=3$ 就得到平均值。
:::
::::

⁠**简而言之：**对每个矩阵，$\mathbf{A}^+\mathbf{y}$ 都是一个最佳近似解，在有多个时是最短的那个；在各列或各行线性无关时，$\mathbf{A}^+$ 就是左逆或右逆。

:::hintergrund 为什么伪逆不除以零
在 $d_j=0$ 处，伪逆把 $1/d_j$ 换成 $0$。这看起来很随意，但它可以由一个极限过程得出。对每个 $\delta\ne0$，矩阵 $\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I}$ 都可逆，因为它的特征值为 $d_j^2+\delta^2>0$。在奇异向量的坐标下，$(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ 把第 $j$ 个坐标乘以

$$\frac{d_j}{d_j^2+\delta^2}\ \xrightarrow{\ \delta\to0\ }\ \begin{cases}1/d_j&\text{若 }d_j>0,\\0&\text{若 }d_j=0.\end{cases}$$

所以对每个矩阵都有 $\mathbf{A}^+=\lim_{\delta\to0}(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$。这个极限过程也揭示了一个危险：伪逆并不连续地依赖于矩阵。对于 $\operatorname{diag}(1,\,\varepsilon)$（$\varepsilon>0$ 很小），伪逆是 $\operatorname{diag}(1,\,1/\varepsilon)$，非常大；而当 $\varepsilon=0$ 时，它是 $\operatorname{diag}(1,\,0)$。一个仅仅因为测量误差或舍入才不为零的极小奇异值，会被 $\mathbf{A}^+$ 极度放大。因此，数值计算软件把低于某个小阈值的奇异值当作零处理。小奇异值会把误差放大到什么程度，由下一节来衡量。
:::

:::aufgabe 练习 33 ★ 一个左逆
<span class="anker" id="aufg-33"></span>

第 [3.6](die-beste-naherungslosung.html#stufe-3-6) 节中的最小二乘直线对应于 $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$。

<ol class="al">

<li>

计算左逆 $\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$，并验证 $\mathbf F\mathbf{A}=\mathbf{I}$。

</li>

<li>

把 $\mathbf F$ 作用于 $\mathbf{y}=(1,\,2,\,4)^{\top}$，并与第 [3.6](die-beste-naherungslosung.html#stufe-3-6) 节的结果比较。

</li>

<li>

从 $\mathbf F$ 的各行读出：对任意测量值 $y_1,y_2,y_3$，最小二乘直线的截距和斜率是怎样得出的。

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&3\\3&5\end{smallmatrix}\bigr)$，其逆矩阵为 $\tfrac16\bigl(\begin{smallmatrix}5&-3\\-3&3\end{smallmatrix}\bigr)$，所以

$$\mathbf F=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix}\begin{pmatrix}1&1&1\\0&1&2\end{pmatrix}=\frac16\begin{pmatrix}5&2&-1\\-3&0&3\end{pmatrix},\qquad \mathbf F\mathbf{A}=\frac16\begin{pmatrix}5+2-1&2-2\\-3+3&6\end{pmatrix}=\mathbf{I} .$$

(b) $\mathbf F(1,\,2,\,4)^{\top}=\tfrac16(5+4-4,\ -3+12)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$，正是第 [3.6](die-beste-naherungslosung.html#stufe-3-6) 节中的最小二乘直线。

(c) 对任意测量值，截距为 $\hat x_1=\tfrac16(5y_1+2y_2-y_3)$，斜率为 $\hat x_2=\tfrac12(y_3-y_1)$。截距的各个权重之和为 $1$：如果所有测量值都相等，截距就等于这个值。对于三个等间距的测量点，斜率只取决于两端的两个点；中间的点只影响直线的高度。
:::
:::

:::aufgabe 练习 34 ★★ 最短解
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

求 $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ 的伪逆，以及 $\mathbf{y}=(1,\,3)^{\top}$ 时的 $\mathbf{x}^+$。验证 $\mathbf{x}^+$ 是一个最佳近似解，并且不存在更短的最佳近似解。

</li>

<li>

求 $x_1+2x_2+2x_3=9$ 的最短解。把它的长度与解 $(9,\,0,\,0)^{\top}$ 的长度作比较。

</li>

</ol>

:::loesung
(a) $\mathbf{A}=2\,\mathbf{q}\mathbf{q}^{\top}$，其中 $\mathbf{q}=(1,\,1)^{\top}/\sqrt2$；它是对称且半正定的，所以这就是紧凑形式的分解，其中 $d_1=2$，$\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$。因此 $\mathbf{A}^+=\tfrac12\mathbf{q}\mathbf{q}^{\top}=\tfrac14\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$，$\mathbf{x}^+=\tfrac14(4,\,4)^{\top}=(1,\,1)^{\top}$。$\mathbf{A}\mathbf{x}^+=(2,\,2)^{\top}$，这是 $(1,\,3)^{\top}$ 在沿 $(1,\,1)^{\top}$ 方向的直线上的投影，因为 $\tfrac{1+3}2(1,\,1)^{\top}=(2,\,2)^{\top}$。最佳近似解是所有满足 $x_1+x_2=2$ 的 $\mathbf{x}$，即 $(1+s,\ 1-s)^{\top}$，其长度的平方为 $2+2s^2$。最短的是 $s=0$ 时的解，它就是 $\mathbf{x}^+$。

(b) $\mathbf{A}=(1\ \ 2\ \ 2)$ 满足 $\mathbf{A}\mathbf{A}^{\top}=9$，所以 $\mathbf G=\tfrac19(1,\,2,\,2)^{\top}$，最短解为 $\mathbf G\cdot9=(1,\,2,\,2)^{\top}$，长度为 $3$。解 $(9,\,0,\,0)^{\top}$ 的长度为 $9$。最短解指向解平面的法向量 $(1,\,2,\,2)^{\top}$ 的方向。
:::
:::

:::aufgabe 练习 35 ★★★ 伪逆投影到什么上
<span class="anker" id="aufg-35"></span>

设 $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$，秩为 $r$，$\mathbf{U}_r$、$\mathbf{V}_r$ 分别由 $\mathbf{U}$ 和 $\mathbf{V}$ 的前 $r$ 列组成。

<ol class="al">

<li>

证明 $\mathbf{A}\mathbf{A}^+=\mathbf{U}_r\mathbf{U}_r^{\top}$ 和 $\mathbf{A}^+\mathbf{A}=\mathbf{V}_r\mathbf{V}_r^{\top}$。这两个矩阵分别投影到哪个空间上？

</li>

<li>

由此推出 $\mathbf{A}\mathbf{A}^+\mathbf{A}=\mathbf{A}$ 和 $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=\mathbf{A}^+$。

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{A}^+=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^+\mathbf{U}^{\top}$。$m\times m$ 矩阵 $\mathbf{D}\mathbf{D}^+$ 在前 $r$ 个对角位置上为 $d_j\cdot\tfrac1{d_j}=1$，其余位置为零。因此 $\mathbf{A}\mathbf{A}^+=\sum_{j\le r}\mathbf{u}_j\mathbf{u}_j^{\top}=\mathbf{U}_r\mathbf{U}_r^{\top}$，由式 [(4.2)](projektion-auf-einen-unterraum.html#gl-4-2)，它是到 $\mathbf{u}_1,\dots,\mathbf{u}_r$ 张成的空间上的正交投影，这个空间就是 $\mathbf{A}$ 的列空间。同样，$\mathbf{A}^+\mathbf{A}=\mathbf{V}\mathbf{D}^+\mathbf{D}\mathbf{V}^{\top}=\mathbf{V}_r\mathbf{V}_r^{\top}$，它是到 $\mathbf{v}_1,\dots,\mathbf{v}_r$ 张成的空间（即 $\mathbf{A}^{\top}$ 的列空间）上的投影；这个空间是零空间的正交补。

(b) $\mathbf{A}$ 的每一列都在列空间中，而到列空间上的投影使它保持不动：$\mathbf{A}\mathbf{A}^+\mathbf{A}=(\mathbf{U}_r\mathbf{U}_r^{\top})\mathbf{A}=\mathbf{A}$。同样，$\mathbf{A}^+=\sum_{j\le r}\tfrac1{d_j}\mathbf{v}_j\mathbf{u}_j^{\top}$ 的每一列都在 $\mathbf{v}_1,\dots,\mathbf{v}_r$ 张成的空间中，所以 $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=(\mathbf{V}_r\mathbf{V}_r^{\top})\mathbf{A}^+=\mathbf{A}^+$。
:::
:::
