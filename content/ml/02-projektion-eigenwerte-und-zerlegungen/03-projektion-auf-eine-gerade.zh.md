---
title: 投影到直线上
pfad: 计算机科学 / 机器学习 / 数学基础 / 投影、特征值与矩阵分解
knoten: 基础篇 2：投影、特征值与矩阵分解
nachschlagen: ja
order: 15220300
summary: 一个点位于一条直线之外。直线上哪个点离它最近？本节针对过原点的直线、在任意维数下回答这个问题。答案是垂足，其原因在于勾股定理。
tags: 正交投影, 投影矩阵, 投影
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
一个点位于一条直线之外。直线上哪个点离它最近？本节针对过原点的直线、在任意维数下回答这个问题。答案是垂足，其原因在于勾股定理。
:::

### 垂足

<span class="anker" id="stufe-2-1"></span>

过原点的直线由方向向量 $\mathbf{a}\ne\mathbf{0}$ 的所有倍数 $t\,\mathbf{a}$ 组成。给定一个点 $\mathbf{y}$，它不一定在这条直线上。我们要找直线上离 $\mathbf{y}$ 最近的点。

在[基础篇 1 第 5.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5)中，光线垂直照射时，箭头在直线上投下影子。影子的端点就是从 $\mathbf{y}$ 向直线所作垂线与直线的交点，即**垂足**。从这一点到 $\mathbf{y}$ 的连线垂直于直线（图 [4](#abb-4)）。它是最近点，这将在下一小节中证明。这里先把它算出来，而且即使 $\mathbf{a}$ 没有归一化也能计算。

:::herleitung 垂足
所求的点在直线上，所以它是 $\hat x\,\mathbf{a}$，其中数 $\hat x$ 尚未知。连线 $\mathbf{y}-\hat x\,\mathbf{a}$ 应垂直于 $\mathbf{a}$：

$$\mathbf{a}^{\top}(\mathbf{y}-\hat x\,\mathbf{a})=0\qquad\Longleftrightarrow\qquad \mathbf{a}^{\top}\mathbf{y}-\hat x\,\mathbf{a}^{\top}\mathbf{a}=0\qquad\Longleftrightarrow\qquad \hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} .$$

由于 $\mathbf{a}\ne\mathbf{0}$，有 $\mathbf{a}^{\top}\mathbf{a}=\lVert\mathbf{a}\rVert^2>0$，所以可以作除法，并且这样的 $\hat x$ 恰好只有一个。
:::

:::definition 定义 2.1 (向直线的投影)
<span class="anker" id="satz-2-1"></span>

设 $\mathbf{a}\in\mathbb{R}^n$，$\mathbf{a}\ne\mathbf{0}$。$\mathbf{y}\in\mathbb{R}^n$ 在沿 $\mathbf{a}$ 方向、过原点的直线上的__正交投影__是点

<span class="anker" id="gl-2-1"></span>
$$\hat{\mathbf{y}}=\hat x\,\mathbf{a}\qquad\text{其中}\qquad\hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} . \tag{2.1}$$
:::

点 $\hat{\mathbf{y}}$ 是 $\mathbb{R}^n$ 中的向量；数 $\hat x$ 是它沿 $\mathbf{a}$ 的坐标。二者不能混淆。若 $\mathbf{a}$ 已归一化，则 $\mathbf{a}^{\top}\mathbf{a}=1$，$\hat{\mathbf{y}}=(\mathbf{a}^{\top}\mathbf{y})\,\mathbf{a}$，恰好就是[基础篇 1](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) 中的影子点。

:::abbildung ml/k2lot 4
$\mathbf{y}=(4,3)^{\top}$ 在沿 $\mathbf{a}=(1,2)^{\top}$ 方向的直线上的投影。垂足为 $\hat{\mathbf{y}}=2\mathbf{a}=(2,4)^{\top}$；连线 $\mathbf{r}=(2,-1)^{\top}$（蓝色）垂直于直线。直线上的任何其他点，例如 $(1,2)^{\top}$，离 $\mathbf{y}$ 都更远（虚线）：由 $\mathbf{y}$、$\hat{\mathbf{y}}$ 和 $(1,2)^{\top}$ 构成的三角形在 $\hat{\mathbf{y}}$ 处是直角，虚线边是它的斜边。
:::

::::beispiel [算例 1]
对于 $\mathbf{a}=(1,\,2)^{\top}$ 和 $\mathbf{y}=(4,\,3)^{\top}$，得到 $\mathbf{a}^{\top}\mathbf{y}=4+6=10$ 和 $\mathbf{a}^{\top}\mathbf{a}=5$（图 [5](#abb-5)），所以 $\hat x=2$，$\hat{\mathbf{y}}=(2,\,4)^{\top}$。连线 $\mathbf{y}-\hat{\mathbf{y}}=(2,\,-1)^{\top}$ 垂直于 $\mathbf{a}$：$2-2=0$。

:::abbildung ml/k2rproj 5
逐步计算投影中的两个点积：$\hat x$ 分子中的 $\mathbf{a}^{\top}\mathbf{y}=10$ 和分母中的 $\mathbf{a}^{\top}\mathbf{a}=5$。
:::
::::

::::beispiel [算例 2]
对于 $\mathbf{a}=(3,\,4)^{\top}$ 和 $\mathbf{y}=(3,\,1)^{\top}$，得到 $\hat x=(9+4)/25=0.52$ 和 $\hat{\mathbf{y}}=0.52\,(3,\,4)^{\top}=(1.56,\ 2.08)^{\top}$，与[基础篇 1](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) 中用归一化向量 $(0.6,\ 0.8)^{\top}=\mathbf{a}/5$ 得到的影子点相同。方向向量的长度无关紧要：若把 $\mathbf{a}$ 换成 $c\,\mathbf{a}$（$c\ne0$），则 $\hat x$ 变为 $\hat x/c$，而 $\hat{\mathbf{y}}$ 不变。反之，若把 $\mathbf{y}$ 加倍，$\hat{\mathbf{y}}$ 也随之加倍。
::::

⁠**简而言之：**$\mathbf{y}$ 在沿 $\mathbf{a}$ 方向的直线上的投影就是垂足 $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$。

### 垂足是最近点

<span class="anker" id="stufe-2-2"></span>

到目前为止，我们只证明了到垂足的连线是垂直的。垂足同时也是最近点，这由勾股定理得出：沿直线离开垂足，就是在垂直的连线上再加上一段沿直线方向的分量，这只会使距离增大。

:::satz 定理 2.2 (垂足是最近点)
<span class="anker" id="satz-2-2"></span>

设 $\hat{\mathbf{y}}=\hat x\,\mathbf{a}$ 是 $\mathbf{y}$ 在沿 $\mathbf{a}$ 方向的直线上的投影。对每个数 $t$ 有

<span class="anker" id="gl-2-2"></span>
$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2=\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2+(t-\hat x)^2\,\lVert\mathbf{a}\rVert^2 . \tag{2.2}$$

特别地，$\hat{\mathbf{y}}$ 是直线上与 $\mathbf{y}$ 距离最小的唯一点。
:::

:::beweis 最近点
把从 $t\,\mathbf{a}$ 到 $\mathbf{y}$ 的连线写成两个箭头之和：

$$\mathbf{y}-t\,\mathbf{a}=(\mathbf{y}-\hat{\mathbf{y}})+(\hat x-t)\,\mathbf{a} .$$

由推导，第一项垂直于 $\mathbf{a}$，因而也垂直于第二项。由[基础篇 1 第 5.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-3)的勾股定理，和的长度平方等于各项长度平方之和，这就是式 [(2.2)](#gl-2-2)。右边第二项永远不为负，且只在 $t=\hat x$ 时为零。所以距离恰好在 $t=\hat x$ 时最小。
:::

对于垂足的长度，有 $\lVert\hat{\mathbf{y}}\rVert=|\hat x|\,\lVert\mathbf{a}\rVert=|\mathbf{a}^{\top}\mathbf{y}|/\lVert\mathbf{a}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$，其中 $\varphi$ 是 $\mathbf{a}$ 与 $\mathbf{y}$ 之间的夹角。这就是以 $\mathbf{y}$ 为斜边的直角三角形中的邻边。

::::beispiel [算例]
在上一小节的第一个算例中，$\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2=\lVert(2,\,-1)^{\top}\rVert^2=5$。对于 $t=1$ 的点，即 $(1,\,2)^{\top}$，式 [(2.2)](#gl-2-2) 预言距离的平方为 $5+1\cdot5=10$，实际上确实有 $\lVert(3,\,1)^{\top}\rVert^2=10$。对于 $t=3$，即 $(3,\,6)^{\top}$，结果同样是 $5+1\cdot5=10=\lVert(1,\,-3)^{\top}\rVert^2$。两个点离垂足一样远，分处两侧。
::::

⁠**简而言之：**直线上的最近点是垂足，因为由勾股定理，沿直线每走一步都会使距离的平方增大。

:::hintergrund 为什么最近点恰好只有一个，以及这为什么归功于欧几里得范数
证明用到了勾股定理，而勾股定理只对由点积导出的范数成立。在[基础篇 1 第 3.4 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-4)中已经看到，1-范数不是这样的范数。对于它，唯一性确实不再成立。例子：沿 $\mathbf{a}=(1,\,1)^{\top}$ 方向的直线和点 $\mathbf{y}=(1,\,0)^{\top}$。对于 $0\le t\le1$，

$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert_1=|1-t|+|0-t|=(1-t)+t=1 ,$$

因此 $\mathbf{0}$ 与 $\mathbf{a}$ 之间所有点的距离都相同；在这条线段之外，距离更大。在这种范数下，最近点构成一整条线段。在欧几里得范数下则恰好只有一个：$\hat x=\tfrac12$，即点 $(\tfrac12,\,\tfrac12)^{\top}$。投影唯一，并且可以用简单的公式算出，这正是许多方法采用欧几里得距离的原因之一。
:::

### 投影矩阵

<span class="anker" id="stufe-2-3"></span>

映射规则 $\mathbf{y}\mapsto\hat{\mathbf{y}}$ 是线性的：两个点之和被映射为它们的投影之和，一个倍数被映射为相应的倍数。由[基础篇 1 第 8.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2)，它因此有一个矩阵。把数 $\mathbf{a}^{\top}\mathbf{y}$ 写到 $\mathbf{a}$ 的另一侧，再重新组合矩阵乘积，就可以直接读出这个矩阵：

$$\hat{\mathbf{y}}=\mathbf{a}\,\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{y} .$$

分子是[基础篇 1 第 9.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5)中的外积。

:::definition 定义 2.3 (直线的投影矩阵)
<span class="anker" id="satz-2-3"></span>

对于 $\mathbf{a}\ne\mathbf{0}$，

<span class="anker" id="gl-2-3"></span>
$$\mathbf{P}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}} \tag{2.3}$$

称为向沿 $\mathbf{a}$ 方向的直线投影的__投影矩阵__。有 $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$。
:::

:::satz 定理 2.4 (直线投影矩阵的性质)
<span class="anker" id="satz-2-4"></span>

有 $\mathbf{P}^{\top}=\mathbf{P}$ 和 $\mathbf{P}^2=\mathbf{P}$。直线上的点保持不动：$\mathbf{P}\mathbf{a}=\mathbf{a}$。垂直于 $\mathbf{a}$ 的向量被映射为 $\mathbf{0}$。$\mathbf{P}$ 的秩为 $1$。
:::

:::beweis 性质
$(\mathbf{a}\mathbf{a}^{\top})^{\top}=\mathbf{a}\mathbf{a}^{\top}$，所以 $\mathbf{P}$ 是对称的。此外，$\mathbf{P}^2=\mathbf{a}(\mathbf{a}^{\top}\mathbf{a})\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})^2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{P}$，因为 $\mathbf{a}^{\top}\mathbf{a}$ 是一个数。$\mathbf{P}\mathbf{a}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{a})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{a}$。若 $\mathbf{a}^{\top}\mathbf{z}=0$，则 $\mathbf{P}\mathbf{z}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{z})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{0}$。$\mathbf{P}$ 的每一列都是 $\mathbf{a}$ 的倍数，所以秩为 $1$。
:::

等式 $\mathbf{P}^2=\mathbf{P}$ 有一个简单的含义：已经在直线上的东西，第二次投影时保持不动。

::::beispiel [算例]
对于 $\mathbf{a}=(1,\,2)^{\top}$，

$$\mathbf{P}=\frac15\begin{pmatrix}1&2\\2&4\end{pmatrix},\qquad \mathbf{P}\begin{pmatrix}4\\3\end{pmatrix}=\frac15\begin{pmatrix}4+6\\8+12\end{pmatrix}=\begin{pmatrix}2\\4\end{pmatrix}.$$

验算 $\mathbf{P}^2=\mathbf{P}$：$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)^2=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)=5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$，所以 $\mathbf{P}^2=\frac1{25}\cdot5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=\mathbf{P}$。在[基础篇 1 第 11.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-5)中，矩阵 $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ 是不可逆矩阵的例子。现在清楚它做了什么：它是一个投影的五倍，把平面压扁到沿 $(1,\,2)^{\top}$ 方向的直线上。
::::

⁠**简而言之：**向直线的投影就是与 $\mathbf{P}=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ 的矩阵-向量乘积；这个矩阵是对称的，并满足 $\mathbf{P}^2=\mathbf{P}$。

### 一般的投影

<span class="anker" id="stufe-2-4"></span>

光线斜射时也有影子。这时一个点在直线上的影子不再是垂足，但仍然在直线上，而已经在直线上的点就是它自己的影子。所以性质 $\mathbf{P}^2=\mathbf{P}$ 保留了下来，对称性却没有。

:::definition 定义 2.5 (投影)
<span class="anker" id="satz-2-5"></span>

满足 $\mathbf{P}^2=\mathbf{P}$ 的方阵 $\mathbf{P}$ 称为__投影__。如果此外对每个 $\mathbf{y}$，连线 $\mathbf{y}-\mathbf{P}\mathbf{y}$ 都垂直于所有的像 $\mathbf{P}\mathbf{z}$，则称它为正交投影。
:::

:::satz 定理 2.6 (正交即对称)
<span class="anker" id="satz-2-6"></span>

投影 $\mathbf{P}$ 是正交投影，当且仅当 $\mathbf{P}^{\top}=\mathbf{P}$。
:::

:::beweis 正交即对称
对所有 $\mathbf{y},\mathbf{z}$，有 $(\mathbf{y}-\mathbf{P}\mathbf{y})^{\top}\mathbf{P}\mathbf{z}=\mathbf{y}^{\top}(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}\mathbf{z}$。若 $\mathbf{P}^{\top}=\mathbf{P}$，则 $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}=\mathbf{P}-\mathbf{P}^2=\mathbf 0$，该表达式为零。反之，若该表达式对所有 $\mathbf{y},\mathbf{z}$ 都为零，则矩阵 $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}$ 是零矩阵；取 $\mathbf{y}=\mathbf{e}_i$、$\mathbf{z}=\mathbf{e}_l$，表达式恰好取出它的元素 $(i,l)$。于是 $\mathbf{P}=\mathbf{P}^{\top}\mathbf{P}$，而由[基础篇 1 第 10.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-2)，$\mathbf{P}^{\top}\mathbf{P}$ 是对称的。
:::

::::beispiel [算例]
矩阵 $\mathbf{P}=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$ 把 $(x_1,\,x_2)^{\top}$ 映射为 $(x_1+x_2,\,0)^{\top}$。有 $\mathbf{P}^2=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$，所以 $\mathbf{P}$ 是向 $x_1$ 轴的投影。它不对称，因而不是正交投影：点 $(0,\,1)^{\top}$ 被映射为 $(1,\,0)^{\top}$，连线 $(-1,\,1)^{\top}$ 相对于坐标轴是斜的。这里光线沿 $(1,\,-1)^{\top}$ 方向照射。这个投影给出的不是 $x_1$ 轴上的最近点 $(0,\,0)^{\top}$。
::::

⁠**简而言之：**投影是满足 $\mathbf{P}^2=\mathbf{P}$ 的矩阵；它是正交投影（即作垂线）当且仅当它是对称的。

:::aufgabe 练习 4 ★ 手算一个投影
<span class="anker" id="aufg-4"></span>

把 $\mathbf{y}=(3,\,3,\,0)^{\top}$ 投影到沿 $\mathbf{a}=(2,\,1,\,2)^{\top}$ 方向的直线上。

<ol class="al">

<li>

计算 $\hat x$、$\hat{\mathbf{y}}$ 和连线 $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}$。验证 $\mathbf{a}^{\top}\mathbf{r}=0$。$\mathbf{y}$ 离直线有多远？

</li>

<li>

写出投影矩阵 $\mathbf{P}$，并验证 $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$ 和 $\mathbf{P}\mathbf{a}=\mathbf{a}$。

</li>

</ol>

:::loesung
(a) $\mathbf{a}^{\top}\mathbf{y}=6+3+0=9$，$\mathbf{a}^{\top}\mathbf{a}=4+1+4=9$，所以 $\hat x=1$，$\hat{\mathbf{y}}=\mathbf{a}=(2,\,1,\,2)^{\top}$。连线为 $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(1,\,2,\,-2)^{\top}$，并且 $\mathbf{a}^{\top}\mathbf{r}=2+2-4=0$：它垂直于直线。$\mathbf{y}$ 到直线的距离为 $\lVert\mathbf{r}\rVert=\sqrt{1+4+4}=3$；由第 [2.2](#stufe-2-2) 节的定理，直线上没有离它更近的点。

(b)

$$\mathbf{P}=\frac{\mathbf{a}\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}=\frac19\begin{pmatrix}4&2&4\\2&1&2\\4&2&4\end{pmatrix},\qquad \mathbf{P}\mathbf{y}=\frac19\begin{pmatrix}12+6\\6+3\\12+6\end{pmatrix}=\begin{pmatrix}2\\1\\2\end{pmatrix},\qquad \mathbf{P}\mathbf{a}=\frac19\begin{pmatrix}8+2+8\\4+1+4\\8+2+8\end{pmatrix}=\mathbf{a} .$$
:::
:::

:::aufgabe 练习 5 ★★ 直线上的勾股定理
<span class="anker" id="aufg-5"></span>

设 $\mathbf{a}=(1,\,2)^{\top}$，$\mathbf{y}=(4,\,3)^{\top}$，与算例中相同。

<ol class="al">

<li>

对 $t=0$、$1$、$2$、$3$ 和 $4$，分别直接计算和用式 [(2.2)](#gl-2-2) 计算 $\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2$。

</li>

<li>

计算 $\mathbf{a}$ 与 $\mathbf{y}$ 之间的夹角 $\varphi$，并验证 $\lVert\hat{\mathbf{y}}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$。

</li>

</ol>

:::loesung
(a) 直接计算：$t=0$：$\lVert(4,\,3)^{\top}\rVert^2=25$；$t=1$：$\lVert(3,\,1)^{\top}\rVert^2=10$；$t=2$：$\lVert(2,\,-1)^{\top}\rVert^2=5$；$t=3$：$\lVert(1,\,-3)^{\top}\rVert^2=10$；$t=4$：$\lVert(0,\,-5)^{\top}\rVert^2=25$。用式 [(2.2)](#gl-2-2)，其中 $\hat x=2$，$\lVert\mathbf{r}\rVert^2=5$，$\lVert\mathbf{a}\rVert^2=5$：$5+5(t-2)^2$ 依次给出 $25$、$10$、$5$、$10$、$25$。这些值关于 $t=2$ 处的垂足对称，因为距离的平方随沿直线离开垂足的距离按平方增大。

(b) $\cos\varphi=\mathbf{a}^{\top}\mathbf{y}/(\lVert\mathbf{a}\rVert\,\lVert\mathbf{y}\rVert)=10/(\sqrt5\cdot5)=2/\sqrt5\approx0.894$，所以 $\varphi\approx26.57^\circ$。$\lVert\hat{\mathbf{y}}\rVert=\lVert(2,\,4)^{\top}\rVert=\sqrt{20}=2\sqrt5$，而 $|\cos\varphi|\,\lVert\mathbf{y}\rVert=\tfrac2{\sqrt5}\cdot5=2\sqrt5$。
:::
:::

:::aufgabe 练习 6 ★★ 哪些矩阵是投影？
<span class="anker" id="aufg-6"></span>

对每个矩阵，判断它是否是投影，以及是否是正交投影。对于是投影的矩阵，描述它们投影到什么上。

$$\mathbf{P}_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\enspace \mathbf{P}_2=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\enspace \mathbf{P}_3=\begin{pmatrix}1&0\\1&0\end{pmatrix},\enspace \mathbf{P}_4=\begin{pmatrix}1&2\\0&1\end{pmatrix},\enspace \mathbf{P}_5=\mathbf{I},\enspace \mathbf{P}_6=\mathbf 0 .$$

:::loesung
对每个矩阵，先检验 $\mathbf{P}^2=\mathbf{P}$，再检验 $\mathbf{P}^{\top}=\mathbf{P}$。

<ul>

<li>

$\mathbf{P}_1$：$\mathbf{P}_1^2=\mathbf{P}_1$ 且对称，所以是到 $x_1$ 轴上的正交投影。

</li>

<li>

$\mathbf{P}_2$：$\mathbf{P}_2^2=\tfrac14\bigl(\begin{smallmatrix}2&2\\2&2\end{smallmatrix}\bigr)=\mathbf{P}_2$ 且对称：到沿 $(1,\,1)^{\top}$ 方向的直线上的正交投影；事实上，$\mathbf{P}_2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$，其中 $\mathbf{a}=(1,\,1)^{\top}$。

</li>

<li>

$\mathbf{P}_3$：$\mathbf{P}_3^2=\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)=\mathbf{P}_3$，但不对称。这是一个斜投影：它把 $(x_1,\,x_2)^{\top}$ 映射为 $x_1\,(1,\,1)^{\top}$，即映射到沿 $(1,\,1)^{\top}$ 方向的直线上，并把向量 $(0,\,1)^{\top}$ 映射为零。光线沿 $(0,\,1)^{\top}$ 方向照射，而不是垂直于直线照射。

</li>

<li>

$\mathbf{P}_4$：$\mathbf{P}_4^2=\bigl(\begin{smallmatrix}1&4\\0&1\end{smallmatrix}\bigr)\ne\mathbf{P}_4$。它不是投影，而是剪切；作用两次，剪切的程度加倍。

</li>

<li>

$\mathbf{P}_5=\mathbf{I}$：$\mathbf{I}^2=\mathbf{I}$，对称。这是到整个平面上的正交投影；它让一切都留在原处。

</li>

<li>

$\mathbf{P}_6=\mathbf 0$：$\mathbf 0^2=\mathbf 0$，对称。这是到原点上的正交投影。

</li>

</ul>
:::
:::
