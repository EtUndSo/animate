---
title: 投影到子空间上
pfad: 计算机科学 / 机器学习 / 数学基础 / 投影、特征值与矩阵分解
knoten: 基础篇 2：投影、特征值与矩阵分解
nachschlagen: ja
order: 15220500
summary: 上一节求出了列空间中的最近点。本节把这个结果表示成一个矩阵，说明当各列标准正交时一切都变得特别简单，并介绍一种把任意线性无关的列变成标准正交列的方法。借助它，无需构造 A top A 就能算出最佳近似解。
tags: 子空间, 投影矩阵, 正交补, 格拉姆-施密特正交化, QR 分解
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
上一节求出了列空间中的最近点。本节把这个结果表示成一个矩阵，说明当各列标准正交时一切都变得特别简单，并介绍一种把任意线性无关的列变成标准正交列的方法。借助它，无需构造 $\mathbf{A}^{\top}\mathbf{A}$ 就能算出最佳近似解。
:::

### 子空间

<span class="anker" id="stufe-4-1"></span>

过原点的直线和平面、列空间和零空间有一个共同的性质：只要包含两个向量，就包含这两个向量的每一个线性组合。通过加法和数乘，永远不会离开它们。这样的集合有一个专门的名称。

:::definition 定义 4.1 (子空间)
<span class="anker" id="satz-4-1"></span>

若集合 $\mathcal U\subseteq\mathbb{R}^n$ 是有限个向量张成的空间，则称它为 $\mathbb{R}^n$ 的__子空间__。
:::

等价地说：$\mathcal U$ 包含零向量，并且只要 $\mathcal U$ 包含两个向量 $\mathbf{u},\mathbf{v}$，它就也包含 $\mathbf{u}+\mathbf{v}$ 和每个倍数 $c\,\mathbf{u}$。每个子空间都有一组基，因此由基础篇 1 第 13.3 节，也有一个维数。

⁠**算例：**在 $\mathbb{R}^3$ 中，以下都是子空间：仅由原点构成的集合，维数为 $0$；每条过原点的直线，维数为 $1$；每个过原点的平面，例如上一节中 $\mathbf{H}$ 的列空间，维数为 $2$；以及整个 $\mathbb{R}^3$。矩阵的零空间是子空间，它的列空间也是。不经过原点的直线不是子空间，因为它不包含零向量。

⁠**简而言之：**子空间是一组向量张成的空间；通过加法和数乘不会离开它。

### 列空间的投影矩阵

<span class="anker" id="stufe-4-2"></span>

对于线性无关的列，式 [(3.5)](die-beste-naherungslosung.html#gl-3-5) 给出最近点 $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$。$\mathbf{y}$ 前面的矩阵只依赖于 $\mathbf{A}$。它对列空间所起的作用，就是 $\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ 对直线所起的作用。

:::definition 定义 4.2 (列空间的投影矩阵)
<span class="anker" id="satz-4-2"></span>

若 $\mathbf{A}$ 的列线性无关，则

<span class="anker" id="gl-4-1"></span>
$$\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{4.1}$$

称为向 $\mathbf{A}$ 的列空间投影的__投影矩阵__。
:::

:::satz 定理 4.3 (性质)
<span class="anker" id="satz-4-3"></span>

有 $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$，$\mathbf{P}^{\top}=\mathbf{P}$，$\mathbf{P}^2=\mathbf{P}$ 以及 $\mathbf{P}\mathbf{A}=\mathbf{A}$。所以 $\mathbf{P}$ 是向列空间的正交投影。
:::

:::beweis 性质
第一个等式就是上面的推导。利用基础篇 1 第 10.1 节和第 11.4 节的规则，$\mathbf{P}^{\top}=\mathbf{A}\bigl((\mathbf{A}^{\top}\mathbf{A})^{-1}\bigr)^{\top}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$，因为 $\mathbf{A}^{\top}\mathbf{A}$ 是对称的，所以它的逆矩阵也是对称的。此外，$\mathbf{P}\mathbf{A}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}(\mathbf{A}^{\top}\mathbf{A})=\mathbf{A}$，由此得 $\mathbf{P}^2=\mathbf{P}\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$。由第 [2.4](projektion-auf-eine-gerade.html#stufe-2-4) 节的定理，对称的投影是正交投影。
:::

等式 $\mathbf{P}\mathbf{A}=\mathbf{A}$ 表明：每一列，从而列空间中的每个向量，在投影时都保持不动。

⁠**算例：**对于 $\mathbf{H}$，

$$\mathbf{P}=\mathbf{H}\cdot\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\mathbf{H}^{\top}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix}.$$

验算：$\mathbf{P}(1,\,1,\,1)^{\top}=\tfrac13(2,\,2,\,4)^{\top}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}=\hat{\mathbf{y}}$，并且 $\mathbf{P}\mathbf{a}_1=\tfrac13(2+1,\ -1+1,\ 1+2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_1$。

⁠**简而言之：**投影矩阵 $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ 把每个向量映射为列空间中的最近点；它是对称的，并满足 $\mathbf{P}^2=\mathbf{P}$。

### 标准正交的列

<span class="anker" id="stufe-4-3"></span>

公式 [(4.1)](#gl-4-1) 中含有一个逆矩阵。当各列标准正交时，它就消失了，因为此时 $\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$。因此，对于列标准正交的矩阵 $\mathbf{Q}$，最佳近似解就是 $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$：它的各分量就是影子长度 $\mathbf{q}_i^{\top}\mathbf{y}$。

:::satz 定理 4.4 (列标准正交时的投影)
<span class="anker" id="satz-4-4"></span>

若 $\mathbf{Q}\in\mathbb{R}^{n\times k}$ 的列 $\mathbf{q}_1,\dots,\mathbf{q}_k$ 标准正交，则向其列空间投影的投影矩阵为

<span class="anker" id="gl-4-2"></span>
$$\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}=\sum_{i=1}^k\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{4.2}$$
:::

求和形式由基础篇 1 第 9.5 节得出：矩阵乘积是各列与各行的外积之和。每一项 $\mathbf{q}_i\mathbf{q}_i^{\top}$ 都是向沿 $\mathbf{q}_i$ 方向的直线投影的投影矩阵。所以在各列标准正交时，向列空间的投影就是向各个坐标轴的投影之和。这也事后解释了第 [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1) 节的最后一个小节：$\mathbf{Q}\mathbf{Q}^{\top}$ 不是单位矩阵，而是向 $\mathbf{Q}$ 的列空间的投影。与列空间垂直的部分都被丢掉了。

⁠**算例：**向量 $\mathbf{q}_1=\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}$ 和 $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$ 是标准正交的：$\lVert\mathbf{q}_1\rVert^2=\tfrac22$，$\lVert\mathbf{q}_2\rVert^2=\tfrac66$，$\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac{-1+0+1}{\sqrt{12}}=0$。二者的第三个分量都等于前两个分量之和；它们构成 $\mathbf{H}$ 的平面的一组标准正交基。有

$$\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}=\frac12\begin{pmatrix}1&0&1\\0&0&0\\1&0&1\end{pmatrix}+\frac16\begin{pmatrix}1&-2&-1\\-2&4&2\\-1&2&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix},$$

这与上一小节中的矩阵相同，这次没有用到逆矩阵。

⁠**简而言之：**在各列标准正交时，$\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$，$\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}$，后者就是向各列分别投影之和。

### 正交补

<span class="anker" id="stufe-4-4"></span>

把 $\mathbf{y}$ 投影到一个子空间上，剩下的是残差 $\mathbf{y}-\mathbf{P}\mathbf{y}$。它垂直于整个子空间。具有这一性质的所有向量本身也构成一个子空间，而 $\mathbf{y}$ 分解为一个子空间中的部分和另一个子空间中的部分。

:::definition 定义 4.5 (正交补)
<span class="anker" id="satz-4-5"></span>

子空间 $\mathcal U\subseteq\mathbb{R}^n$ 的__正交补__是集合

<span class="anker" id="gl-4-3"></span>
$$\mathcal U^\perp=\{\mathbf{z}\in\mathbb{R}^n:\ \mathbf{z}^{\top}\mathbf{u}=0\ \text{对所有}\ \mathbf{u}\in\mathcal U\} . \tag{4.3}$$
:::

符号 $\mathcal U^\perp$ 读作“$\mathcal U$ 垂直”。若 $\mathcal U$ 是 $\mathbf{A}$ 的列空间，则 $\mathbf{z}$ 垂直于 $\mathcal U$ 当且仅当 $\mathbf{A}^{\top}\mathbf{z}=\mathbf{0}$；所以正交补就是 $\mathbf{A}^{\top}$ 的零空间。

:::satz 定理 4.6 (分解为两个互相垂直的部分)
<span class="anker" id="satz-4-6"></span>

若 $\mathbf{P}$ 是向 $\mathbb{R}^n$ 的子空间 $\mathcal U$ 的正交投影，则：

<ol class="rm">

<li>

每个向量 $\mathbf{y}$ 都能以唯一的方式写成和 $\mathbf{y}=\mathbf{u}+\mathbf{z}$，其中 $\mathbf{u}\in\mathcal U$，$\mathbf{z}\in\mathcal U^\perp$，即 $\mathbf{u}=\mathbf{P}\mathbf{y}$，$\mathbf{z}=(\mathbf{I}-\mathbf{P})\mathbf{y}$。

</li>

<li>

$\mathbf{I}-\mathbf{P}$ 是向 $\mathcal U^\perp$ 的正交投影。

</li>

<li>

$\dim\mathcal U^\perp=n-\dim\mathcal U$。

</li>

</ol>
:::

:::beweis 分解
(i) $\mathbf{P}\mathbf{y}$ 在 $\mathcal U$ 中且 $\mathbf{y}-\mathbf{P}\mathbf{y}$ 垂直于 $\mathcal U$，这正是正交投影的定义。如果还有第二种分解 $\mathbf{y}=\mathbf{u}'+\mathbf{z}'$，那么 $\mathbf{u}-\mathbf{u}'=\mathbf{z}'-\mathbf{z}$ 就是一个既在 $\mathcal U$ 中、又垂直于 $\mathcal U$ 的向量，因而垂直于它自身。于是它的长度平方为零，所以它是零向量。(ii) $\mathbf{I}-\mathbf{P}$ 是对称的，且 $(\mathbf{I}-\mathbf{P})^2=\mathbf{I}-2\mathbf{P}+\mathbf{P}^2=\mathbf{I}-\mathbf{P}$。由 (i)，它的像在 $\mathcal U^\perp$ 中。每个 $\mathbf{z}\in\mathcal U^\perp$ 都保持不动：$\mathbf{P}\mathbf{z}$ 在 $\mathcal U$ 中，同时又是两个垂直于 $\mathcal U$ 的向量之差 $\mathbf{z}-(\mathbf{z}-\mathbf{P}\mathbf{z})$；所以 $\mathbf{P}\mathbf{z}$ 垂直于它自身，等于 $\mathbf{0}$。(iii) 选取 $\mathcal U$ 的一组基作为矩阵 $\mathbf{A}$ 的列，则 $\mathcal U^\perp$ 是 $\mathbf{A}^{\top}$ 的零空间。由基础篇 1 第 13.5 节的秩-零化度定理，它的维数为 $n-\operatorname{rank}\mathbf{A}^{\top}=n-\operatorname{rank}\mathbf{A}=n-\dim\mathcal U$。
:::

⁠**算例：**$\mathbf{H}$ 的平面维数为 $2$，所以它在 $\mathbb{R}^3$ 中的正交补维数为 $1$：它是沿法向量 $\mathbf{k}=(1,\,1,\,-1)^{\top}$ 方向的直线。确实有 $\mathbf{H}^{\top}\mathbf{k}=(1-1,\ 1-1)^{\top}=\mathbf{0}$。有

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&1&-1\\1&1&-1\\-1&-1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}},$$

即向这条直线的投影。对于 $\mathbf{y}=(1,\,1,\,1)^{\top}$，$(\mathbf{I}-\mathbf{P})\mathbf{y}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$，正是上一节的残差。

⁠**简而言之：**正交补 $\mathcal U^\perp$ 包含所有垂直于 $\mathcal U$ 的向量；每个向量都可以唯一地分解为 $\mathcal U$ 中的部分与 $\mathcal U^\perp$ 中的部分，两者的维数之和为 $n$。

### 格拉姆-施密特正交化

<span class="anker" id="stufe-4-5"></span>

标准正交的列让一切变得简单，但给定的列通常是任意的。格拉姆-施密特正交化从线性无关的向量 $\mathbf{a}_1,\dots,\mathbf{a}_k$ 出发，构造出张成同一子空间的标准正交向量 $\mathbf{q}_1,\dots,\mathbf{q}_k$。

图 [11](#abb-11) 展示了两个向量时的思路。先把第一个向量归一化。从第二个向量中减去它在第一个向量上的影子，也就是它的投影。剩下的部分垂直于第一个向量，再把它归一化。从第三个向量中减去它在已求出的两个向量上的影子，依此类推。

:::abbildung ml/k2gramschmidt 11
对 $\mathbf{a}_1=(2,1)^{\top}$ 和 $\mathbf{a}_2=(1,2)^{\top}$ 进行格拉姆-施密特正交化。先把 $\mathbf{a}_1$ 归一化：$\mathbf{q}_1=\mathbf{a}_1/\sqrt5$。从第二个向量中减去它的影子 $(\mathbf{q}_1^{\top}\mathbf{a}_2)\,\mathbf{q}_1=(1.6,\,0.8)^{\top}$（蓝色）。余下的 $\tilde{\mathbf{q}}_2=(-0.6,\,1.2)^{\top}$（橙色，与虚线所示的垂线平行）垂直于 $\mathbf{q}_1$；归一化后得到 $\mathbf{q}_2=(-1,2)^{\top}/\sqrt5$。
:::

:::definition 定义 4.7 (格拉姆-施密特正交化)
<span class="anker" id="satz-4-7"></span>

给定线性无关的向量 $\mathbf{a}_1,\dots,\mathbf{a}_k\in\mathbb{R}^n$。__格拉姆-施密特正交化__依次对 $i=1,\dots,k$ 计算

<span class="anker" id="gl-4-4"></span>
$$\tilde{\mathbf{q}}_i=\mathbf{a}_i-\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l,\qquad \mathbf{q}_i=\frac{\tilde{\mathbf{q}}_i}{\lVert\tilde{\mathbf{q}}_i\rVert} . \tag{4.4}$$
:::

当 $i=1$ 时求和为空，所以 $\tilde{\mathbf{q}}_1=\mathbf{a}_1$。由式 [(4.2)](#gl-4-2)，这个和是 $\mathbf{a}_i$ 向已求出的向量所张成空间的投影；$\tilde{\mathbf{q}}_i$ 是这次投影的残差。

:::satz 定理 4.8 (格拉姆-施密特正交化的结果)
<span class="anker" id="satz-4-8"></span>

向量 $\mathbf{q}_1,\dots,\mathbf{q}_k$ 是标准正交的，并且对每个 $i$，向量 $\mathbf{q}_1,\dots,\mathbf{q}_i$ 与 $\mathbf{a}_1,\dots,\mathbf{a}_i$ 张成同一个子空间。
:::

:::beweis 格拉姆-施密特正交化
逐步进行。假设 $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ 已经标准正交，并且与 $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$ 张成同一个子空间。那么 $\tilde{\mathbf{q}}_i$ 是 $\mathbf{a}_i$ 向这个子空间投影的残差，因而垂直于 $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$；直接计算也有 $\mathbf{q}_l^{\top}\tilde{\mathbf{q}}_i=\mathbf{q}_l^{\top}\mathbf{a}_i-\mathbf{q}_l^{\top}\mathbf{a}_i=0$。并且 $\tilde{\mathbf{q}}_i\ne\mathbf{0}$，否则 $\mathbf{a}_i$ 就是 $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ 的线性组合，从而是 $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$ 的线性组合，与线性无关矛盾。所以可以归一化。最后，$\mathbf{a}_i=\tilde{\mathbf{q}}_i+\sum_l(\mathbf{q}_l^{\top}\mathbf{a}_i)\mathbf{q}_l$ 是 $\mathbf{q}_1,\dots,\mathbf{q}_i$ 的线性组合，反过来 $\mathbf{q}_i$ 是 $\mathbf{a}_i$ 与 $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ 的线性组合。所以两组向量张成同一个子空间。
:::

如果给定的向量实际上是线性相关的，这个方法会自己发现：在某一步出现 $\tilde{\mathbf{q}}_i=\mathbf{0}$，无法归一化。

⁠**算例：**对于 $\mathbf{H}$ 的列 $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ 和 $\mathbf{a}_2=(0,\,1,\,1)^{\top}$，得 $\mathbf{q}_1=\mathbf{a}_1/\sqrt2$。于是 $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$，

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\frac1{\sqrt2}\,\mathbf{q}_1=(0,\,1,\,1)^{\top}-\tfrac12(1,\,0,\,1)^{\top}=\bigl(-\tfrac12,\,1,\,\tfrac12\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{\tfrac14+1+\tfrac14}=\sqrt{\tfrac32} .$$

归一化后得 $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$，恰好就是式 [(4.2)](#gl-4-2) 的算例中的标准正交基。图 [12](#abb-12) 给出了本算例中的两个和。

:::abbildung ml/k2rgs 12
对 $\mathbf{H}$ 的列进行格拉姆-施密特正交化：给出影子长度的点积 $\mathbf{q}_1^{\top}\mathbf{a}_2$，其中 $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$，$\mathbf{a}_2=(0,1,1)^{\top}$；以及余下部分 $\tilde{\mathbf{q}}_2=(-\tfrac12,1,\tfrac12)^{\top}$ 的长度平方。
:::

⁠**简而言之：**格拉姆-施密特正交化从每个向量中减去它在已求出向量上的投影，再把余下的部分归一化；这样就得到同一子空间的一组标准正交基。

:::hintergrund 计算量与舍入误差
对于 $k$ 个各有 $n$ 个分量的向量，这个方法大约需要 $2nk^2$ 次算术运算：在第 $i$ 步要计算 $i-1$ 个点积，并减去同样多个倍数，每一项大约耗费 $2n$ 次运算，对 $i$ 求和后按 $k^2$ 增长。使用舍入数时，式 [(4.4)](#gl-4-4) 这种形式很敏感：若给定向量中有两个几乎平行，$\tilde{\mathbf{q}}_i$ 就是大数之间的小差值，算出的 $\mathbf{q}_i$ 便不再精确正交。把计算步骤的顺序稍作改变，就得到修正的格拉姆-施密特正交化：它不是从原来的 $\mathbf{a}_i$ 中一次减去所有影子，而是从已经削减过的余下部分中逐个减去影子。对精确数而言，两者结果相同；对舍入数而言，修正的方法要精确得多。数值计算库大多采用另外的方法，这些方法利用反射，也就是利用正交矩阵。
:::

### QR 分解

<span class="anker" id="stufe-4-6"></span>

格拉姆-施密特正交化可以写成一个矩阵的分解。由上面的证明，每个向量 $\mathbf{a}_i$ 都是 $\mathbf{q}_1,\dots,\mathbf{q}_i$ 的线性组合，即

$$\mathbf{a}_i=\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l+\lVert\tilde{\mathbf{q}}_i\rVert\,\mathbf{q}_i .$$

其中只出现向量 $\mathbf{q}_l$ 中的前 $i$ 个，而不出现后面的。所以把这些系数写成矩阵的列，得到的是一个三角矩阵。

:::definition 定义 4.9 (QR 分解)
<span class="anker" id="satz-4-9"></span>

若 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 的列线性无关，则它的__QR 分解__是表示

<span class="anker" id="gl-4-5"></span>
$$\mathbf{A}=\mathbf{Q}\mathbf{R} \tag{4.5}$$

其中 $\mathbf{Q}\in\mathbb{R}^{m\times n}$ 是列标准正交的矩阵，$\mathbf{R}\in\mathbb{R}^{n\times n}$ 是对角元素为正的上三角矩阵。这里对 $l<i$ 有 $r_{li}=\mathbf{q}_l^{\top}\mathbf{a}_i$，且 $r_{ii}=\lVert\tilde{\mathbf{q}}_i\rVert$。
:::

上三角矩阵在对角线以下只有零。按列视角，$\mathbf{Q}\mathbf{R}$ 的第 $i$ 列为 $\sum_lr_{li}\mathbf{q}_l$，这恰好是上面 $\mathbf{a}_i$ 的表示。格拉姆-施密特正交化给出 $\mathbf{Q}$ 的各列，$\mathbf{R}$ 的元素则作为副产品一并得出。由于 $\mathbf{Q}$ 的列标准正交，还有 $\mathbf{R}=\mathbf{Q}^{\top}\mathbf{A}$。

⁠**算例：**对于 $\mathbf{H}$，

$$\mathbf{Q}=\begin{pmatrix}\tfrac1{\sqrt2}&-\tfrac1{\sqrt6}\\0&\tfrac2{\sqrt6}\\\tfrac1{\sqrt2}&\tfrac1{\sqrt6}\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&\tfrac1{\sqrt2}\\0&\sqrt{\tfrac32}\end{pmatrix}\approx\begin{pmatrix}1.414&0.707\\0&1.225\end{pmatrix}.$$

验算第二列：$\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}+\sqrt{\tfrac32}\cdot\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}=\tfrac12(1,\,0,\,1)^{\top}+\tfrac12(-1,\,2,\,1)^{\top}=(0,\,1,\,1)^{\top}=\mathbf{a}_2$。

⁠**简而言之：**QR 分解 $\mathbf{A}=\mathbf{Q}\mathbf{R}$ 把格拉姆-施密特正交化写成矩阵乘积：$\mathbf{Q}$ 的列标准正交，$\mathbf{R}$ 是上三角矩阵。

### 用 QR 分解求最佳近似解

<span class="anker" id="stufe-4-7"></span>

借助 QR 分解，无需计算 $\mathbf{A}^{\top}\mathbf{A}$ 就能求解正规方程。代入 $\mathbf{A}=\mathbf{Q}\mathbf{R}$，并利用 $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$。

:::satz 定理 4.10 (用 QR 分解求最佳近似解)
<span class="anker" id="satz-4-10"></span>

若 $\mathbf{A}=\mathbf{Q}\mathbf{R}$ 是 QR 分解，则 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 的最佳近似解就是下面这个方程组的解：

<span class="anker" id="gl-4-6"></span>
$$\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y} . \tag{4.6}$$
:::

:::beweis 用 QR 分解求解
有 $\mathbf{A}^{\top}\mathbf{A}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{R}^{\top}\mathbf{R}$ 和 $\mathbf{A}^{\top}\mathbf{y}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$。所以正规方程为 $\mathbf{R}^{\top}\mathbf{R}\hat{\mathbf{x}}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$。三角矩阵 $\mathbf{R}$ 的对角元素为正，所以由基础篇 1 第 14.4 节，它的行列式不为零，它是可逆的；$\mathbf{R}^{\top}$ 也是如此。从左边乘以 $(\mathbf{R}^{\top})^{-1}$，就剩下式 [(4.6)](#gl-4-6)。
:::

方程组 [(4.6)](#gl-4-6) 是三角方程组，从下往上求解，就像基础篇 1 第 12.3 节高斯消元法最后的回代一样。对于 $m\times n$ 矩阵，整个过程大约需要 $2mn^2$ 次算术运算，几乎全部用于 QR 分解。

⁠**算例：**对于 $\mathbf{H}$ 和 $\mathbf{y}=(1,\,1,\,1)^{\top}$，$\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac2{\sqrt2},\ \tfrac{-1+2+1}{\sqrt6}\bigr)^{\top}=\bigl(\sqrt2,\ \tfrac2{\sqrt6}\bigr)^{\top}$。式 [(4.6)](#gl-4-6) 的最下一行为 $\sqrt{\tfrac32}\,\hat x_2=\tfrac2{\sqrt6}$，所以 $\hat x_2=\tfrac2{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac23$。最上一行为 $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac23=\sqrt2$，所以 $\hat x_1=1-\tfrac13=\tfrac23$。这与用正规方程得到的解相同。$\mathbf{Q}^{\top}\mathbf{y}$ 的各分量就是图 [13](#abb-13) 中的点积。

:::abbildung ml/k2rqr 13
对于 $\mathbf{y}=(1,1,1)^{\top}$，三角方程组的右边 $\mathbf{Q}^{\top}\mathbf{y}$，其中 $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$，$\mathbf{q}_2=(-1,2,1)^{\top}/\sqrt6$。
:::

⁠**简而言之：**利用 $\mathbf{A}=\mathbf{Q}\mathbf{R}$，正规方程变成三角方程组 $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$；矩阵 $\mathbf{A}^{\top}\mathbf{A}$ 根本不需要构造。

:::aufgabe 练习 11 ★ 格拉姆-施密特正交化与投影
<span class="anker" id="aufg-11"></span>

设 $\mathbf{a}_1=(1,\,1,\,0)^{\top}$，$\mathbf{a}_2=(1,\,0,\,1)^{\top}$。

<ol class="al">

<li>

进行格拉姆-施密特正交化，并验证 $\mathbf{q}_1,\mathbf{q}_2$ 是标准正交的。

</li>

<li>

计算向 $\mathbf{a}_1$ 和 $\mathbf{a}_2$ 张成的平面投影的投影矩阵 $\mathbf{P}=\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}$，并对 $\mathbf{y}=(1,\,2,\,3)^{\top}$ 作投影。

</li>

<li>

求一个张成该平面正交补的向量，并验证 $\mathbf{I}-\mathbf{P}=\mathbf{k}\mathbf{k}^{\top}/(\mathbf{k}^{\top}\mathbf{k})$。

</li>

</ol>

:::loesung
(a) $\mathbf{q}_1=\mathbf{a}_1/\sqrt2=(1,\,1,\,0)^{\top}/\sqrt2$。于是 $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$，并且

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\tfrac1{\sqrt2}\,\mathbf{q}_1=(1,\,0,\,1)^{\top}-\tfrac12(1,\,1,\,0)^{\top}=\bigl(\tfrac12,\,-\tfrac12,\,1\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert^2=\tfrac14+\tfrac14+1=\tfrac32 ,$$

所以 $\mathbf{q}_2=\tilde{\mathbf{q}}_2/\sqrt{3/2}=(1,\,-1,\,2)^{\top}/\sqrt6$。验算：$\mathbf{q}_1^{\top}\mathbf{q}_2=(1-1+0)/\sqrt{12}=0$，$\lVert\mathbf{q}_2\rVert^2=\tfrac{1+1+4}6=1$。

(b)

$$\mathbf{P}=\frac12\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix}+\frac16\begin{pmatrix}1&-1&2\\-1&1&-2\\2&-2&4\end{pmatrix}=\frac13\begin{pmatrix}2&1&1\\1&2&-1\\1&-1&2\end{pmatrix},$$

$$\mathbf{P}\mathbf{y}=\frac13\begin{pmatrix}2+2+3\\1+4-3\\1-2+6\end{pmatrix}=\begin{pmatrix}7/3\\2/3\\5/3\end{pmatrix}.$$

(c) 要找的 $\mathbf{k}$ 满足 $\mathbf{a}_1^{\top}\mathbf{k}=k_1+k_2=0$ 和 $\mathbf{a}_2^{\top}\mathbf{k}=k_1+k_3=0$，所以 $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ 或它的倍数。$\mathbf{k}^{\top}\mathbf{k}=3$，并且

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&-1&-1\\-1&1&1\\-1&1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}} .$$

平面的正交补是沿 $\mathbf{k}$ 方向的直线，维数为 $3-2=1$。检验：$\mathbf{y}-\mathbf{P}\mathbf{y}=(-\tfrac43,\,\tfrac43,\,\tfrac43)^{\top}=-\tfrac43\mathbf{k}$ 位于这条直线上。
:::
:::

:::aufgabe 练习 12 ★★ 用 QR 分解求解
<span class="anker" id="aufg-12"></span>

使用以练习 [11](#aufg-11) 中的 $\mathbf{a}_1$ 和 $\mathbf{a}_2$ 为列的矩阵 $\mathbf{A}$。

<ol class="al">

<li>

写出 QR 分解，并验证 $\mathbf{Q}\mathbf{R}=\mathbf{A}$。

</li>

<li>

用式 [(4.6)](#gl-4-6) 在最小二乘意义下求解 $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$，并用正规方程验算。

</li>

</ol>

:::loesung
(a) 由练习 [11](#aufg-11)：$\mathbf{q}_1=(1,\,1,\,0)^{\top}/\sqrt2$，$\mathbf{q}_2=(1,\,-1,\,2)^{\top}/\sqrt6$，$r_{11}=\lVert\mathbf{a}_1\rVert=\sqrt2$，$r_{12}=\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$，$r_{22}=\lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{3/2}$：

$$\mathbf{Q}=\begin{pmatrix}1/\sqrt2&1/\sqrt6\\1/\sqrt2&-1/\sqrt6\\0&2/\sqrt6\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&1/\sqrt2\\0&\sqrt{3/2}\end{pmatrix}.$$

验算：$\mathbf{Q}\mathbf{R}$ 的第 1 列是 $\sqrt2\,\mathbf{q}_1=\mathbf{a}_1$；第 2 列是 $\tfrac1{\sqrt2}\mathbf{q}_1+\sqrt{\tfrac32}\,\mathbf{q}_2=\tfrac12(1,\,1,\,0)^{\top}+\tfrac12(1,\,-1,\,2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_2$，因为 $\sqrt{3/2}/\sqrt6=\tfrac12$。

(b) $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac3{\sqrt2},\ \tfrac{1-2+6}{\sqrt6}\bigr)^{\top}=\bigl(\tfrac3{\sqrt2},\ \tfrac5{\sqrt6}\bigr)^{\top}$。$\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ 的下面一行给出 $\hat x_2=\tfrac5{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac53$，上面一行给出 $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac53=\tfrac3{\sqrt2}$；乘以 $\sqrt2$ 得 $2\hat x_1+\tfrac53=3$，所以 $\hat x_1=\tfrac23$。用正规方程检验：$\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$，$\mathbf{A}^{\top}\mathbf{y}=(3,\,4)^{\top}$，$\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(3,\,4)^{\top}=(\tfrac23,\,\tfrac53)^{\top}$。此外，$\mathbf{A}\hat{\mathbf{x}}=(\tfrac73,\,\tfrac23,\,\tfrac53)^{\top}=\mathbf{P}\mathbf{y}$，正是练习 [11](#aufg-11) 中的投影。
:::
:::

:::aufgabe 练习 13 ★★ 正交补
<span class="anker" id="aufg-13"></span>

<ol class="al">

<li>

$\mathbb{R}^3$ 中过原点的直线的正交补维数是多少？$\mathbb{R}^5$ 中的直线呢？

</li>

<li>

证明：$(\mathcal U^\perp)^\perp=\mathcal U$。提示：先证明 $\mathcal U$ 中的每个向量都在 $(\mathcal U^\perp)^\perp$ 中。然后按照第 [4.4](#stufe-4-4) 节的定理分解一个向量 $\mathbf{y}\in(\mathcal U^\perp)^\perp$，并把它与其在 $\mathcal U^\perp$ 中的部分作点积。

</li>

</ol>

:::loesung
(a) 由第 [4.4](#stufe-4-4) 节的定理，$\dim\mathcal U^\perp=n-\dim\mathcal U$：因此在 $\mathbb{R}^3$ 中为 $3-1=2$，是一个平面；在 $\mathbb{R}^5$ 中为 $5-1=4$。

(b) 第一步：若 $\mathbf{u}\in\mathcal U$，则由 $\mathcal U^\perp$ 的定义，对每个 $\mathbf{z}\in\mathcal U^\perp$ 都有 $\mathbf{u}^{\top}\mathbf{z}=0$。所以 $\mathbf{u}$ 垂直于整个 $\mathcal U^\perp$，从而属于 $(\mathcal U^\perp)^\perp$。第二步：设 $\mathbf{y}\in(\mathcal U^\perp)^\perp$。按照该定理作分解 $\mathbf{y}=\mathbf{u}+\mathbf{z}$，其中 $\mathbf{u}\in\mathcal U$，$\mathbf{z}\in\mathcal U^\perp$。于是 $\mathbf{z}^{\top}\mathbf{y}=0$，因为 $\mathbf{y}$ 垂直于 $\mathcal U^\perp$；并且 $\mathbf{z}^{\top}\mathbf{u}=0$，因为 $\mathbf{z}$ 垂直于 $\mathcal U$。因此 $\mathbf{z}^{\top}\mathbf{z}=\mathbf{z}^{\top}\mathbf{y}-\mathbf{z}^{\top}\mathbf{u}=0$，即 $\mathbf{z}=\mathbf{0}$。于是 $\mathbf{y}=\mathbf{u}\in\mathcal U$。两个集合互相包含，所以它们相等。
:::
:::
