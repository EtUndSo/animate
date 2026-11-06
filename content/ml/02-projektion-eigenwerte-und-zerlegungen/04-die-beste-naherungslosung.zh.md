---
title: 最佳近似解
pfad: 计算机科学 / 机器学习 / 投影、特征值与矩阵分解
order: 6220400
summary: 方程个数多于未知数个数的方程组通常无解。本节转而寻找尽可能好地满足方程组的未知数。它们由一个总是可解的较小方程组得出，其原因又是一个直角。
tags: 残差, 最佳近似解, 正规方程, 最小二乘直线
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
方程个数多于未知数个数的方程组通常无解。本节转而寻找尽可能好地满足方程组的未知数。它们由一个总是可解的较小方程组得出，其原因又是一个直角。
:::

### 回顾：方程多于未知数

<span class="anker" id="stufe-3-1"></span>

在第 1 部分第 12.5 节中，两个权重，即面积的权重 $w_1$ 和房间数的权重 $w_2$，应当恰好给出公寓的价格。用全部四套公寓，就得到方程组 $\mathbf{A}\mathbf{w}=\mathbf{y}$，其中

$$\mathbf{A}=\begin{pmatrix}60&2\\40&1\\90&4\\70&3\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}200\\130\\290\\240\end{pmatrix}\ \text{千欧元}.$$

它无解。用列的图景来说就是：$\mathbf{A}$ 的列在 $\mathbb{R}^4$ 中张成一个平面，即列空间，而价格向量 $\mathbf{y}$ 不在其中。无论 $\mathbf{w}$ 怎样选，总会剩下一个余量。

:::definition 定义 3.1 (残差)
<span class="anker" id="satz-3-1"></span>

对于方程组 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 和任意向量 $\mathbf{x}$，

<span class="anker" id="gl-3-1"></span>
$$\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x} \tag{3.1}$$

称为 $\mathbf{x}$ 的__残差__。
:::

残差的西文名称（residual）源自拉丁语中表示“剩余”的词。残差为零，当且仅当 $\mathbf{x}$ 是方程组的解。它就是第 1 部分第 3.5 节中的误差向量，只是符号相反；长度相同。

⁠**算例：**用第 1 部分中的权重 $\mathbf{w}=(3,\,10)^{\top}$，得 $\mathbf{A}\mathbf{w}=(200,\,130,\,310,\,240)^{\top}$，残差为 $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{w}=(0,\,0,\,-20,\,0)^{\top}$，长度为 $20$。三个价格恰好命中，一个偏差 $20$ 千欧元。

⁠**简而言之：**残差 $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ 是用向量 $\mathbf{x}$ 去解 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 时剩下的余量。

### 最佳近似解

<span class="anker" id="stufe-3-2"></span>

如果残差不能为零，至少应当让它尽可能小。衡量的标准是它的欧几里得长度。

这个任务可以从几何上来想象。由第 1 部分第 7.4 节，当 $\mathbf{x}$ 取遍所有向量时，$\mathbf{A}\mathbf{x}$ 取遍 $\mathbf{A}$ 的列空间。距离 $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert$ 是点 $\mathbf{y}$ 到列空间中的点 $\mathbf{A}\mathbf{x}$ 的距离。所以我们要找列空间中离 $\mathbf{y}$ 最近的点（图 [6](#abb-6)）。在上一节中，列空间是一条直线；现在它可以是一个平面，或者是更高维的张成空间。

:::definition 定义 3.2 (最佳近似解)
<span class="anker" id="satz-3-2"></span>

满足下式的向量 $\hat{\mathbf{x}}$ 称为方程组 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 的__最佳近似解__：

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert\le\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\qquad\text{对所有 }\mathbf{x} . \tag{3.2}$$
:::

长度在其平方最小处最小，而平方就是残差各分量的平方和。因此人们也称之为用**最小二乘法**求得的解。如果方程组有精确解，它也就是最佳近似解，因为它的残差长度为零。

:::abbildung ml/k2ebene 6
向 $\mathbb{R}^3$ 中平面的投影。列 $\mathbf{a}_1=(1,0,1)^{\top}$ 和 $\mathbf{a}_2=(0,1,1)^{\top}$ 张成平面 $x_3=x_1+x_2$（蓝色）。点 $\mathbf{y}=(1,1,1)^{\top}$ 不在其中。平面上的最近点是 $\hat{\mathbf{y}}=(\tfrac23,\tfrac23,\tfrac43)^{\top}$；残差 $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(\tfrac13,\tfrac13,-\tfrac13)^{\top}$ 垂直于平面。
:::

⁠**算例：**第 1 部分第 7.4 节中的矩阵 $\mathbf{H}$ 的列为 $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ 和 $\mathbf{a}_2=(0,\,1,\,1)^{\top}$。它的列空间是第三个分量等于前两个分量之和的所有向量构成的平面。向量 $\mathbf{y}=(1,\,1,\,1)^{\top}$ 不在其中，所以方程组 $\mathbf{H}\mathbf{x}=\mathbf{y}$ 无解。取 $\mathbf{x}=(1,\,0)^{\top}$，残差为 $(0,\,1,\,0)^{\top}$，长度为 $1$；取 $\mathbf{x}=(1,\,1)^{\top}$，残差为 $(0,\,0,\,-1)^{\top}$，长度同样为 $1$。能否做得更好，下一小节给出答案。

⁠**简而言之：**最佳近似解使残差尽可能短；从几何上看，它寻找的是列空间中离 $\mathbf{y}$ 最近的点。

### 正规方程

<span class="anker" id="stufe-3-3"></span>

对于直线，最近点是垂足：残差垂直于直线。对于列空间，自然会想到同样的条件：残差应当垂直于列空间中的每个向量。这可以写成一个方程组。

:::herleitung 正规方程
列空间中的每个向量都是各列的线性组合 $\sum_jz_j\mathbf{a}_j$。如果 $\mathbf{r}$ 垂直于每一列，它也就垂直于每一个这样的线性组合，因为 $\bigl(\sum_jz_j\mathbf{a}_j\bigr)^{\top}\mathbf{r}=\sum_jz_j\,\mathbf{a}_j^{\top}\mathbf{r}$。所以只需对每一列要求：

$$\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=0\qquad\text{对 }j=1,\dots,n .$$

数 $\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$ 就是 $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$ 的各分量，因为 $\mathbf{A}^{\top}$ 的各行就是 $\mathbf{A}$ 的各列。因此，这 $n$ 个条件合起来就是 $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=\mathbf{0}$，展开后即 $\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$。
:::

:::definition 定义 3.3 (正规方程)
<span class="anker" id="satz-3-3"></span>

方程组 $\mathbf{A}\mathbf{x}=\mathbf{y}$（其中 $\mathbf{A}\in\mathbb{R}^{m\times n}$）的__正规方程__为

<span class="anker" id="gl-3-3"></span>
$$\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y} . \tag{3.3}$$
:::

名称中的“正规”（normal）在这里意为“垂直”，与平面的法向量（normal vector）中的含义相同：这些方程要求残差垂直于列空间。矩阵 $\mathbf{A}^{\top}\mathbf{A}$ 是第 1 部分第 10.4 节中各列的格拉姆矩阵；它是方阵，行数与未知数个数相同。一个有 $m$ 个方程的、无解的大方程组，变成了一个只有 $n$ 个方程的小方程组。对于单独一列 $\mathbf{a}$，它就是 $\mathbf{a}^{\top}\mathbf{a}\,\hat x=\mathbf{a}^{\top}\mathbf{y}$，即上一节的公式。

⁠**算例：**对于 $\mathbf{H}$ 和 $\mathbf{y}=(1,\,1,\,1)^{\top}$，

$$\mathbf{H}^{\top}\mathbf{H}=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad \mathbf{H}^{\top}\mathbf{y}=\begin{pmatrix}2\\2\end{pmatrix}.$$

每个元素都是两列的点积，或一列与 $\mathbf{y}$ 的点积（图 [7](#abb-7)）。

:::abbildung ml/k2rnormal 7
正规方程中的两个元素作为点积：$\mathbf{H}^{\top}\mathbf{H}$ 的元素 $(1,2)$ 是 $\mathbf{a}_1^{\top}\mathbf{a}_2$，$\mathbf{H}^{\top}\mathbf{y}$ 的第一个分量是 $\mathbf{a}_1^{\top}\mathbf{y}$。
:::

正规方程 $2\hat x_1+\hat x_2=2$ 和 $\hat x_1+2\hat x_2=2$ 的解为 $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$。于是 $\hat{\mathbf{y}}=\mathbf{H}\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}$，残差为 $\mathbf{r}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$。验算：$\mathbf{a}_1^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$，$\mathbf{a}_2^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$。残差的长度为 $\sqrt{3/9}\approx0.577$，比上一小节的两次尝试都短。

⁠**简而言之：**正规方程 $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ 要求残差垂直于所有列。

### 为什么正规方程给出最佳解

<span class="anker" id="stufe-3-4"></span>

对于直线，垂直的残差对应最近点，这正是勾股定理的结果。同样的论证在这里也适用：它把误差分成两部分，一部分可以通过选择 $\mathbf{x}$ 来影响，另一部分则无法影响。

:::satz 定理 3.4 (正规方程给出最佳近似解)
<span class="anker" id="satz-3-4"></span>

若 $\hat{\mathbf{x}}$ 是正规方程的解，则对每个向量 $\mathbf{x}$ 有

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert^2+\lVert\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})\rVert^2 . \tag{3.4}$$

所以 $\hat{\mathbf{x}}$ 是一个最佳近似解。反之，每个最佳近似解都满足正规方程，并且所有最佳近似解都给出同一个点 $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}$。
:::

:::beweis 最佳近似解
把差拆成两项：$\mathbf{y}-\mathbf{A}\mathbf{x}=(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})+\mathbf{A}(\hat{\mathbf{x}}-\mathbf{x})$。第一项是 $\hat{\mathbf{x}}$ 的残差 $\mathbf{r}$；第二项在列空间中。由正规方程，$\mathbf{r}$ 垂直于列空间，勾股定理给出式 [(3.4)](#gl-3-4)。右边第二项永远不为负，所以对每个 $\mathbf{x}$ 都有 $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\ge\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert$。

如果 $\mathbf{x}$ 也是最佳近似解，那么两个长度相等，式 [(3.4)](#gl-3-4) 迫使 $\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})=\mathbf{0}$。于是 $\mathbf{A}\mathbf{x}=\mathbf{A}\hat{\mathbf{x}}$，二者给出相同的点和相同的残差，$\mathbf{x}$ 也满足正规方程。
:::

⁠**算例：**对于 $\mathbf{H}$、$\mathbf{y}=(1,\,1,\,1)^{\top}$ 和 $\mathbf{x}=(1,\,0)^{\top}$，有 $\lVert\mathbf{y}-\mathbf{H}\mathbf{x}\rVert^2=1$。式 [(3.4)](#gl-3-4) 的右边是 $\lVert\mathbf{r}\rVert^2=\tfrac13$ 加上 $\lVert\mathbf{H}(\tfrac13,\,-\tfrac23)^{\top}\rVert^2=\lVert(\tfrac13,\,-\tfrac23,\,-\tfrac13)^{\top}\rVert^2=\tfrac69$，合计 $\tfrac13+\tfrac23=1$。

⁠**简而言之：**勾股定理把误差的平方分成两部分：垂直的残差，任何 $\mathbf{x}$ 的选择都无法使它变小；以及列空间中的部分，它在 $\hat{\mathbf{x}}$ 处消失。

:::hintergrund 哪些可以影响，哪些无法影响
式 [(3.4)](#gl-3-4) 解释了为什么垂直恰好是正确的条件。每个候选点 $\mathbf{A}\mathbf{x}$ 都在列空间中。到 $\mathbf{y}$ 的距离由互相垂直的两段组成：列空间中的一段，从 $\mathbf{A}\mathbf{x}$ 到 $\hat{\mathbf{y}}$；以及与之垂直的一段 $\mathbf{r}$，从 $\hat{\mathbf{y}}$ 到 $\mathbf{y}$。第一段可以通过选择 $\mathbf{x}$ 任意改变，特别是可以让它变为零。第二段则完全与 $\mathbf{x}$ 无关：它是 $\mathbf{y}$ 中各列的任何线性组合都无法达到的部分。最佳近似解恰好就是使可影响的那一段为零的解。两段按勾股定理相加、不会相互抵消，这要归功于它们之间的直角。
:::

### 最佳近似解何时唯一

<span class="anker" id="stufe-3-5"></span>

正规方程是一个系数矩阵为方阵的方程组。它是否恰有一个解，取决于 $\mathbf{A}^{\top}\mathbf{A}$ 是否可逆。而这又由 $\mathbf{A}$ 的列决定。

:::satz 定理 3.5 ($\mathbf{A}^{\top}\mathbf{A}$ 的可逆性)
<span class="anker" id="satz-3-5"></span>

矩阵 $\mathbf{A}^{\top}\mathbf{A}$ 可逆，当且仅当 $\mathbf{A}$ 的列线性无关。此时最佳近似解唯一：

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y} . \tag{3.5}$$
:::

:::beweis 可逆性
由第 1 部分第 13.5 节，方阵 $\mathbf{A}^{\top}\mathbf{A}$ 可逆，当且仅当它的零空间只含零向量。设 $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$。那么也有 $\mathbf{z}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=0$，即 $\lVert\mathbf{A}\mathbf{z}\rVert^2=0$，从而 $\mathbf{A}\mathbf{z}=\mathbf{0}$。反之，由 $\mathbf{A}\mathbf{z}=\mathbf{0}$ 立即得到 $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$。所以两个零空间相等。$\mathbf{A}$ 的零空间只含零向量，当且仅当 $\mathbf{A}$ 的列线性无关。
:::

如果各列线性相关，最佳近似解就有无穷多个。可以给其中一个加上 $\mathbf{A}$ 零空间中的任意向量，而不改变 $\mathbf{A}\hat{\mathbf{x}}$。不过，正如上一小节的定理所示，最近点 $\hat{\mathbf{y}}$ 仍是唯一的。这与第 1 部分第 13.6 节相符：相关的特征使权重不唯一，但不会使预测值不唯一。

⁠**算例 1：**$\mathbf{H}$ 的列线性无关，$\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ 的逆矩阵为 $\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$。由式 [(3.5)](#gl-3-5)，$\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(2,\,2)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$，与上面相同。

⁠**算例 2：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ 和 $\mathbf{y}=(1,\,1)^{\top}$，各列线性相关。正规方程为 $\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)\hat{\mathbf{x}}=(3,\,6)^{\top}$，即同一个方程 $\hat x_1+2\hat x_2=\tfrac35$ 出现了两次。这条直线上的每个点都是最佳近似解，例如 $(\tfrac35,\,0)^{\top}$ 或 $(0,\,\tfrac3{10})^{\top}$。它们都给出同一个点 $\hat{\mathbf{y}}=(\tfrac35,\,\tfrac65)^{\top}$，即 $\mathbf{y}$ 在沿 $(1,\,2)^{\top}$ 方向的直线上的投影。

⁠**简而言之：**若各列线性无关，则 $\mathbf{A}^{\top}\mathbf{A}$ 可逆，最佳近似解 $\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$ 唯一；否则有无穷多个最佳近似解，它们都给出同一个最近点。

### 过三个点的直线

<span class="anker" id="stufe-3-6"></span>

现在理论已经完整，可以用于一个日常任务了。三个测量点 $(t,\,y)=(0,\,1)$、$(1,\,2)$ 和 $(2,\,4)$ 要用一条直线 $y=x_1+x_2\,t$ 来描述。这三个点不在同一条直线上。我们要找最合适的截距 $x_1$ 和斜率 $x_2$。

每个测量点给出一个方程 $x_1+x_2\,t_i=y_i$。像第 1 部分第 8.5 节那样，用全 1 列表示截距，就得到方程组

$$\mathbf{A}\mathbf{x}=\mathbf{y}\qquad\text{其中}\qquad \mathbf{A}=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}1\\2\\4\end{pmatrix}.$$

残差的各分量是测量点到直线沿 $y$ 方向量得的竖直距离（图 [8](#abb-8)）。最佳近似解使它们的平方和尽可能小。这样的直线称为__最小二乘直线__。

:::abbildung ml/k2ausgleich 8
测量点 $(0,1)$、$(1,2)$ 和 $(2,4)$ 的最小二乘直线。红色线段是残差的各分量，即各点到直线沿 $y$ 方向的竖直距离。这条直线使它们的平方和尽可能小，这里为 $\tfrac1{36}+\tfrac19+\tfrac1{36}=\tfrac16$。
:::

⁠**算例：**有

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&3\\3&5\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}7\\10\end{pmatrix},\qquad (\mathbf{A}^{\top}\mathbf{A})^{-1}=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix},$$

所以 $\hat{\mathbf{x}}=\tfrac16(35-30,\ -21+30)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$。$\mathbf{A}^{\top}\mathbf{A}$ 和 $\mathbf{A}^{\top}\mathbf{y}$ 的元素是对各测量点求的和；图 [9](#abb-9) 给出了其中两个。最小二乘直线为 $y=\tfrac56+\tfrac32\,t$。它在各测量点处的值为 $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\,\tfrac73,\,\tfrac{23}6)^{\top}$，残差为 $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$，平方和为 $\tfrac16$。验算：$\mathbf{A}^{\top}\mathbf{r}=(\tfrac16-\tfrac13+\tfrac16,\ 0-\tfrac13+\tfrac13)^{\top}=(0,\,0)^{\top}$。

验算的第一个分量有其自身的含义。$\mathbf{A}$ 的第一列是全 1 列，$\mathbf{1}^{\top}\mathbf{r}=0$ 意味着：残差之和为零。平均而言，直线既不偏高也不偏低。等价地说，它经过测量点的质心，这里是 $(\bar t,\,\bar y)=(1,\,\tfrac73)$：确实有 $\tfrac56+\tfrac32\cdot1=\tfrac73$。

:::abbildung ml/k2rausgleich 9
最小二乘直线的正规方程中的两个元素，作为对三个测量点 $(t_i,\,y_i)=(0,1)$、$(1,2)$、$(2,4)$ 求的和。
:::

⁠**简而言之：**最小二乘直线是“所有测量点都在直线上”这一方程组的最佳近似解；有全 1 列时，它的残差之和为零。

:::hintergrund 尽可能好地重现信号的滤波器
设计数字滤波器时用的也是同样的计算。一个系数为 $h_0,\dots,h_{K-1}$ 的滤波器，要从输入信号 $x[n]$ 出发，以输出 $\sum_kh_k\,x[n-k]$ 尽可能好地重现期望信号 $d[n]$。对每个时间步 $n$，这都是关于 $K$ 个未知数 $h_k$ 的一个方程，所以对许多时间步而言，就是一个超定方程组 $\mathbf{X}\mathbf h=\mathbf d$。$\mathbf{X}$ 的第 $n$ 行包含 $x[n],x[n-1],\dots,x[n-K+1]$。在正规方程 $\mathbf{X}^{\top}\mathbf{X}\mathbf h=\mathbf{X}^{\top}\mathbf d$ 中，$\mathbf{X}^{\top}\mathbf{X}$ 的元素 $(k,l)$ 是和 $\sum_nx[n-k]\,x[n-l]$，除去信号首尾的边缘效应，它就是 $x$ 在延迟 $l-k$ 处的自相关。向量 $\mathbf{X}^{\top}\mathbf d$ 包含 $d$ 与 $x$ 的互相关。这些恰好是第 1 部分第 2.4 节中平移信号的点积。由式 [(3.3)](#gl-3-3)，最佳滤波器的残差 $d[n]-\sum_kh_k\,x[n-k]$ 垂直于每个平移后的输入信号：滤波器无法重现的部分，与它用来组合输出的任何一个信号都毫无共同之处。
:::

### 公寓：第 1 部分留下的问题

<span class="anker" id="stufe-3-7"></span>

现在可以回答本节开头提出的问题了。我们要找面积和房间数的权重，使它们尽可能好地给出四个价格。

⁠**算例：**对于第一小节中的方程组 $\mathbf{A}\mathbf{w}=\mathbf{y}$，

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}18\,200&730\\730&30\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}60\,100\\2\,410\end{pmatrix}.$$

图 [10](#abb-10) 详细算出了其中两个元素。

:::abbildung ml/k2rwohnungen 10
公寓问题的正规方程中的两个元素作为点积：$\mathbf{a}_1=(60,40,90,70)^{\top}$ 是面积列，$\mathbf{a}_2=(2,1,4,3)^{\top}$ 是房间数列，$\mathbf{y}=(200,130,290,240)^{\top}$ 是价格向量。
:::

两列线性无关；行列式为 $18\,200\cdot30-730^2=13\,100$。用第 1 部分第 11.3 节中的逆矩阵，

$$\hat{\mathbf{w}}=\frac1{13\,100}\begin{pmatrix}30&-730\\-730&18\,200\end{pmatrix}\begin{pmatrix}60\,100\\2\,410\end{pmatrix}=\frac1{13\,100}\begin{pmatrix}43\,700\\-11\,000\end{pmatrix}=\begin{pmatrix}437/131\\-110/131\end{pmatrix}\approx\begin{pmatrix}3.336\\-0.840\end{pmatrix}.$$

估计价格为 $\mathbf{A}\hat{\mathbf{w}}\approx(198.47,\ 132.60,\ 296.87,\ 230.99)^{\top}$，残差为

$$\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{w}}=\frac{20}{131}\,(10,\,-17,\,-45,\,59)^{\top}\approx(1.53,\ -2.60,\ -6.87,\ 9.01)^{\top}$$

长度为 $\lVert\mathbf{r}\rVert\approx11.72$。第 1 部分中的权重 $(3,\,10)^{\top}$ 恰好命中三个价格，但留下长度为 $20$ 的残差。最佳近似解一个价格也没有恰好命中，但总体偏差要小得多。验算：$\mathbf{A}^{\top}\mathbf{r}=\frac{20}{131}(600-680-4050+4130,\ 20-17-180+177)^{\top}=\mathbf{0}$。

⁠**简而言之：**公寓问题的最佳近似解是权重向量 $\hat{\mathbf{w}}\approx(3.336,\ -0.840)^{\top}$；它的残差长度为 $11.72$，比任何恰好命中三个价格的解的残差都短得多。

:::hintergrund 为什么房间数的权重是负的
房间数的权重为负，乍看起来不对：房间多了，价格不应该降低。然而计算是正确的，原因在于数据。在这四套公寓中，面积和房间数同步增长：公寓越大，房间越多。因此 $\mathbf{A}$ 的两列几乎指向同一方向；由第 1 部分第 5.2 节，它们夹角的余弦为 $730/\sqrt{18\,200\cdot30}\approx0.988$，所以夹角只有约 $8.9^\circ$。最佳组合取了大量的面积列，再减去少量的房间数列，以补偿各套公寓偏离共同比例的部分。在面积相同的情况下，这里房间更多意味着房间更小，这确实可能使价格降低；但仅凭四套公寓无法表明这是否属实。正如第 1 部分第 13.6 节所说：当各特征携带的信息几乎相同时，单个权重说明不了多少，而预测值却很能说明问题。
:::

:::aufgabe 练习 7 ★ 手算正规方程
<span class="anker" id="aufg-7"></span>

方程组 $x_1=1$，$x_2=2$，$x_1+x_2=6$ 无解。

<ol class="al">

<li>

把它写成 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 的形式，写出正规方程并求解。

</li>

<li>

计算残差，并验证它垂直于两列。最佳近似解在三个方程上各偏差多少？

</li>

</ol>

:::loesung
(a) 取 $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ 和 $\mathbf{y}=(1,\,2,\,6)^{\top}$，有 $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$，$\mathbf{A}^{\top}\mathbf{y}=(1+6,\ 2+6)^{\top}=(7,\,8)^{\top}$。正规方程 $2\hat x_1+\hat x_2=7$，$\hat x_1+2\hat x_2=8$ 的解为

$$\hat{\mathbf{x}}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}7\\8\end{pmatrix}=\frac13\begin{pmatrix}6\\9\end{pmatrix}=\begin{pmatrix}2\\3\end{pmatrix}.$$

(b) $\mathbf{A}\hat{\mathbf{x}}=(2,\,3,\,5)^{\top}$，$\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}=(-1,\,-1,\,1)^{\top}$。验算：$\mathbf{a}_1^{\top}\mathbf{r}=-1+0+1=0$，$\mathbf{a}_2^{\top}\mathbf{r}=0-1+1=0$。三个方程中的每一个都恰好偏差 $1$：$\hat x_1=2$ 而不是 $1$，$\hat x_2=3$ 而不是 $2$，$\hat x_1+\hat x_2=5$ 而不是 $6$。最佳近似解把矛盾平均分摊到各个方程上；$\lVert\mathbf{r}\rVert^2=3$。
:::
:::

:::aufgabe 练习 8 ★★ 一条最小二乘直线
<span class="anker" id="aufg-8"></span>

求点 $(1,\,2)$、$(2,\,3)$ 和 $(3,\,5)$ 的最小二乘直线 $y=x_1+x_2\,t$。计算残差，验证 $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$，并证明这条直线经过三个点的质心。

:::loesung
取 $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&2\\1&3\end{smallmatrix}\Bigr)$ 和 $\mathbf{y}=(2,\,3,\,5)^{\top}$，有

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&6\\6&14\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}10\\23\end{pmatrix},\qquad \hat{\mathbf{x}}=\frac16\begin{pmatrix}14&-6\\-6&3\end{pmatrix}\begin{pmatrix}10\\23\end{pmatrix}=\frac16\begin{pmatrix}2\\9\end{pmatrix}=\begin{pmatrix}1/3\\3/2\end{pmatrix}.$$

最小二乘直线为 $y=\tfrac13+\tfrac32\,t$，它在各测量点处的值为 $\tfrac{11}6$、$\tfrac{10}3$、$\tfrac{29}6$。残差为 $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$，并且 $\mathbf{A}^{\top}\mathbf{r}=\bigl(\tfrac16-\tfrac13+\tfrac16,\ \tfrac16-\tfrac23+\tfrac12\bigr)^{\top}=(0,\,0)^{\top}$。质心为 $(\bar t,\,\bar y)=(2,\,\tfrac{10}3)$，而 $\tfrac13+\tfrac32\cdot2=\tfrac{10}3$：直线经过质心。这由 $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ 的第一个分量得出：残差之和为零，所以 $\bar y=\hat x_1+\hat x_2\,\bar t$。
:::
:::

:::aufgabe 练习 9 ★★ 基础价格与每平方米价格
<span class="anker" id="aufg-9"></span>

这四套公寓的价格只用面积并加上一个基础价格来估计：$y\approx x_1+x_2\cdot\text{面积}$。

<ol class="al">

<li>

写出带全 1 列的 $\mathbf{A}$，并求解正规方程。

</li>

<li>

计算残差及其长度。与最后一小节的结果比较。

</li>

</ol>

:::loesung
(a) 矩阵由全 1 列和面积列组成：

$$\mathbf{A}=\begin{pmatrix}1&60\\1&40\\1&90\\1&70\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}4&260\\260&18\,200\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}860\\60\,100\end{pmatrix}.$$

行列式为 $4\cdot18\,200-260^2=72\,800-67\,600=5\,200$，于是

$$\hat{\mathbf{x}}=\frac1{5\,200}\begin{pmatrix}18\,200&-260\\-260&4\end{pmatrix}\begin{pmatrix}860\\60\,100\end{pmatrix}=\frac1{5\,200}\begin{pmatrix}26\,000\\16\,800\end{pmatrix}=\begin{pmatrix}5\\42/13\end{pmatrix}\approx\begin{pmatrix}5\\3.231\end{pmatrix}.$$

基础价格为 $5$ 千欧元，另外每平方米约加 $3.23$ 千欧元。

(b) 估计价格为 $5+\tfrac{42}{13}\cdot\text{面积}$，残差为

$$\mathbf{r}=\tfrac1{13}\,(15,\,-55,\,-75,\,115)^{\top}\approx(1.15,\ -4.23,\ -5.77,\ 8.85)^{\top},\qquad \lVert\mathbf{r}\rVert=\tfrac1{13}\sqrt{22\,100}\approx11.44 .$$

残差之和为零，这正是全 1 列所要求的。用面积和房间数时，残差长度为 $\lVert\mathbf{r}\rVert\approx11.72$；所以同样是两个未知数，基础价格加面积拟合得稍好一些。选择哪两列，会改变列空间，从而改变最近点。
:::
:::

:::aufgabe 练习 10 ★★★ 没有全 1 列时的残差
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

证明：若 $\mathbf{A}$ 的列空间包含全 1 向量 $\mathbf{1}$，则最佳近似解的残差各分量之和为零。

</li>

<li>

用最后一小节中公寓问题的残差验证：没有全 1 列时，残差之和一般不为零。

</li>

</ol>

:::loesung
(a) 若 $\mathbf{1}$ 在列空间中，则由正规方程，最佳近似解的残差垂直于 $\mathbf{1}$，因为它垂直于整个列空间。因此 $\mathbf{1}^{\top}\mathbf{r}=\sum_ir_i=0$。

(b) 公寓问题的残差为 $\tfrac{20}{131}(10,\,-17,\,-45,\,59)^{\top}$，其各分量之和为 $\tfrac{20}{131}(10-17-45+59)=\tfrac{140}{131}\approx1.07\ne0$。这里没有全 1 列，$\mathbf{1}$ 不在列空间中，残差不必互相抵消。
:::
:::
