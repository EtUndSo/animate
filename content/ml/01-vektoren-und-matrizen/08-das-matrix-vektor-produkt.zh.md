---
title: 矩阵-向量乘积
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: 第 1 章：向量与矩阵
nachschlagen: ja
order: 15210800
summary: 要对数据集中的所有样本计算同一个加权和。为此，本节引入矩阵与向量的乘积，并说明它的两种读法：按行读或按列读。
tags: 矩阵-向量乘积, 列空间
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
要对数据集中的所有样本计算同一个加权和。为此，本节引入矩阵与向量的乘积，并说明它的两种读法：按行读或按列读。
:::

### 矩阵乘以向量

<span class="anker" id="stufe-7-1"></span>

第 [2.2](das-skalarprodukt.html#stufe-2-2) 小节中的房产经纪人用同一个加权和估算每套公寓。对四套公寓，她要计算四次 $\mathbf{w}^{\top}\mathbf{x}_i$。如果把各套公寓写成一个矩阵的各行，就能用一步表示全部四个计算：矩阵的每一行都与同一个向量相乘。

:::definition 定义 7.1 (矩阵-向量乘积)
<span class="anker" id="satz-7-1"></span>

对 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 和 $\mathbf{x}\in\mathbb{R}^n$，__矩阵-向量乘积__ $\mathbf{A}\mathbf{x}$ 是 $\mathbb{R}^m$ 中分量如下的向量：

<span class="anker" id="gl-7-1"></span>
$$(\mathbf{A}\mathbf{x})_i=\sum_{j=1}^{n}a_{ij}\,x_j=a_{i1}x_1+a_{i2}x_2+\dots+a_{in}x_n ,\qquad i=1,\dots,m . \tag{7.1}$$
:::

只有当 $\mathbf{x}$ 的分量个数与 $\mathbf{A}$ 的列数相同时，乘积才存在。结果的分量个数与 $\mathbf{A}$ 的行数相同。由求和规则可得 $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ 和 $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$。

::::beispiel [算例]
对于

$$\mathbf{A}=\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\quad\text{和}\quad \mathbf{x}=\begin{pmatrix}2\\1\end{pmatrix}\qquad\text{有}\qquad \mathbf{A}\mathbf{x}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$

每个分量都是按式 [(7.1)](#gl-7-1) 求出的和（图 [28](#abb-28)）。$3\times2$ 矩阵乘以有 $2$ 个分量的向量，得到有 $3$ 个分量的向量。

:::abbildung ml/k1rmv 28
逐个分量计算矩阵-向量乘积：对每一行 $i$，把元素 $a_{ij}$ 与对应的 $x_j$ 相乘再相加。
:::
::::

⁠**简而言之：**$\mathbf{A}\mathbf{x}$ 是第 $i$ 个分量为和 $\sum_ja_{ij}x_j$ 的向量；$m\times n$ 矩阵把 $\mathbb{R}^n$ 中的向量变成 $\mathbb{R}^m$ 中的向量。

### 行视角：许多个点积

<span class="anker" id="stufe-7-2"></span>

对每个分量，式 [(7.1)](#gl-7-1) 说的是：矩阵的第 $i$ 行与 $\mathbf{x}$ 逐个元素相乘再求和。这就是第 $i$ 行与 $\mathbf{x}$ 的点积（图 [30](#abb-30) 左）。

:::satz 定理 7.2 (行视角)
<span class="anker" id="satz-7-2"></span>

$\mathbf{A}\mathbf{x}$ 的第 $i$ 个分量是 $\mathbf{A}$ 的第 $i$ 行与 $\mathbf{x}$ 的点积。对行为 $\mathbf{x}_i^{\top}$ 的数据矩阵 $\mathbf{X}$ 和权重向量 $\mathbf{w}$，这意味着

<span class="anker" id="gl-7-2"></span>
$$\mathbf{X}\mathbf{w}=\begin{pmatrix}\mathbf{x}_1^{\top}\mathbf{w}\\\vdots\\\mathbf{x}_N^{\top}\mathbf{w}\end{pmatrix}. \tag{7.2}$$
:::

所以，矩阵-向量乘积把权重为 $\mathbf{w}$ 的加权和同时用于所有样本，并给出全部预测值构成的向量。用模式比对的图景来说：每个样本都与同一个模式 $\mathbf{w}$ 进行比对。

::::beispiel [算例]
对公寓数据集和 $\mathbf{w}=(3,\,10,\,-4)^{\top}$，

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3\\10\\-4\end{pmatrix}=\begin{pmatrix}188\\126\\286\\232\end{pmatrix},$$

即房产经纪人的四个预测值，单位为千欧元。每个分量都是一行与 $\mathbf{w}$ 的点积（图 [29](#abb-29)）。

:::abbildung ml/k1rzeilen 29
房产经纪人估价的行视角：每套公寓，即 $\mathbf{X}$ 的每一行，乘以权重 $\mathbf{w}$。
:::
::::

⁠**简而言之：**按行视角，$\mathbf{A}\mathbf{x}$ 是一串点积，每行一个；$\mathbf{X}\mathbf{w}$ 是所有样本的预测值列表。

:::hintergrund 矩阵-向量乘积的计算量有多大
$m$ 个分量中的每一个都需要 $n$ 次乘法和 $n-1$ 次加法。合计为 $m(2n-1)$ 次，即大约 $2mn$ 次基本算术运算。对于有三个特征的四套公寓，是 $4\cdot5=20$ 次。对于有一百万个样本、一百个特征的数据集，约为 $2\cdot10^8$ 次。现代处理器每秒可执行数十亿次这样的运算，所以这种规模的单个矩阵-向量乘积很快就能算完。不过，这样的计数只给出计算时间的数量级，因为计算机实际有多快，还取决于它能多快地从内存中取出这些数。
:::

### 列视角：各列的线性组合

<span class="anker" id="stufe-7-3"></span>

同一个和也可以按别的顺序排列。不再逐行进行，而是先把属于 $x_1$ 的所有贡献收集起来，再收集属于 $x_2$ 的所有贡献，依此类推。$x_j$ 的贡献全都在矩阵的第 $j$ 列中。于是乘积就变成各列的线性组合（图 [30](#abb-30) 右）。

:::abbildung ml/k1zeilenspalten 30
对 $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ 和 $\mathbf{x}=(2,\,1)^{\top}$，$\mathbf{A}\mathbf{x}$ 的两种读法。左边是行视角：结果的第 $1$ 个分量是第一行与 $\mathbf{x}$ 的点积。右边是列视角：$\mathbf{A}\mathbf{x}$ 等于 $2$ 倍的第一列 $\mathbf{a}_1=(2,1)^{\top}$ 加 $1$ 倍的第二列 $\mathbf{a}_2=(1,1)^{\top}$。
:::

:::satz 定理 7.3 (列视角)
<span class="anker" id="satz-7-3"></span>

若 $\mathbf{a}_1,\dots,\mathbf{a}_n$ 是 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 的各列，则

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2+\dots+x_n\mathbf{a}_n=\sum_{j=1}^nx_j\,\mathbf{a}_j . \tag{7.3}$$

矩阵-向量乘积是以 $\mathbf{x}$ 的各分量为系数的、$\mathbf{A}$ 各列的线性组合。
:::

:::beweis 列视角
右边的第 $i$ 个分量是 $\sum_jx_j\,(\mathbf{a}_j)_i=\sum_jx_j\,a_{ij}$，因为列 $\mathbf{a}_j$ 的第 $i$ 个分量就是元素 $a_{ij}$。按式 [(7.1)](#gl-7-1)，这恰好是 $\mathbf{A}\mathbf{x}$ 的第 $i$ 个分量。
:::

::::beispiel [算例 1]
对第 [7.1](#stufe-7-1) 小节中的乘积 $\mathbf{A}\mathbf{x}$，

$$\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\begin{pmatrix}2\\1\end{pmatrix}=2\begin{pmatrix}1\\0\\3\end{pmatrix}+1\begin{pmatrix}2\\-1\\1\end{pmatrix}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$
::::

::::beispiel [算例 2]
房产经纪人的预测值等于 $3$ 倍的面积列加 $10$ 倍的房间数列加 $(-4)$ 倍的距离列（图 [31](#abb-31)）。与第 [6.1](matrizen-und-die-datenmatrix.html#stufe-6-1) 小节一样，$\mathbf{X}$ 的各列记作 $\mathbf{a}_1$、$\mathbf{a}_2$、$\mathbf{a}_3$。从这种形式可以看出每个预测值的哪一部分来自哪个特征：第一项包含面积的贡献，第二项包含房间数的贡献，第三项包含距离的贡献。

:::abbildung ml/k1rspalten 31
房产经纪人估价的列视角：$\mathbf{X}$ 的每一列 $\mathbf{a}_j$ 乘以它的权重 $w_j$，然后把三个向量相加。
:::
::::

⁠**简而言之：**按列视角，$\mathbf{A}\mathbf{x}$ 是 $\mathbf{A}$ 各列的线性组合；$\mathbf{x}$ 的各分量说明每一列取多少。

:::hintergrund 同一个计算为什么有两种视角
两种视角计算的都是同样的 $m\cdot n$ 个乘积 $a_{ij}x_j$，并把它们相加。行视角先按行合并，列视角先按列合并；项数有限时顺序无关紧要，就像第 [1.1](vektoren-daten-als-zahlenlisten.html#stufe-1-1) 小节中的双重求和一样。但每种视角回答不同的问题。行视角问的是：第 $i$ 个分量得到什么？列视角问的是：如果自由选择 $\mathbf{x}$，矩阵究竟能给出哪些结果？第二个问题直接引出下一个概念。
:::

### 列空间

<span class="anker" id="stufe-7-4"></span>

让 $\mathbf{x}$ 取遍 $\mathbb{R}^n$ 中的所有向量，按列视角，$\mathbf{A}\mathbf{x}$ 就取遍各列的所有线性组合。一般来说，这些并不是 $\mathbb{R}^m$ 中的所有向量。

:::definition 定义 7.4 (列空间)
<span class="anker" id="satz-7-4"></span>

矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 的__列空间__是所有向量 $\mathbf{A}\mathbf{x}$（其中 $\mathbf{x}\in\mathbb{R}^n$）构成的集合，也就是 $\mathbf{A}$ 各列的所有线性组合构成的集合。
:::

::::beispiel [算例 1]
矩阵 $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ 的列为 $(1,\,2)^{\top}$ 和 $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$。每个线性组合都是 $(1,\,2)^{\top}$ 的倍数。所以，尽管结果有两个分量，列空间却只是过原点、沿 $(1,\,2)^{\top}$ 方向的直线。向量 $(3,\,6)^{\top}$ 在其中；向量 $(1,\,1)^{\top}$ 不在。
::::

::::beispiel [算例 2]
矩阵 $\mathbf{H}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ 给出 $\mathbf{H}\mathbf{x}=(x_1,\,x_2,\,x_1+x_2)^{\top}$。它的列空间由 $\mathbb{R}^3$ 中第三个分量等于前两个分量之和的向量组成；这是空间中的一个平面。向量 $(1,\,2,\,3)^{\top}=\mathbf{H}\,(1,\,2)^{\top}$ 在其中，而 $(1,\,1,\,1)^{\top}$ 不在，因为 $1+1\ne1$。
::::

对数据矩阵而言，这意味着：无论选择什么权重，预测值 $\mathbf{X}\mathbf{w}$ 总是位于 $\mathbf{X}$ 的列空间中。用这些特征，只能产生非常特定的预测值列表。

⁠**简而言之：**矩阵的列空间是所有向量 $\mathbf{A}\mathbf{x}$ 构成的集合，也就是能由它的各列线性组合而成的一切。

:::aufgabe 练习 16 ★ 一个乘积的两种视角
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

对 $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ 和 $\mathbf{x}=(1,\,3,\,-1)^{\top}$，分别按行视角和列视角计算 $\mathbf{B}\mathbf{x}$。

</li>

<li>

$\mathbf{B}\,(1,\,2)^{\top}$ 有定义吗？$\mathbf{B}\,(1,\,2,\,3)^{\top}$ 呢？根据型说明理由；如果有定义，说明结果有多少个分量。

</li>

<li>

$(2,\,0,\,2)^{\top}$ 是否位于第 [7.4](#stufe-7-4) 小节中矩阵 $\mathbf{H}$ 的列空间中？$(2,\,1,\,2)^{\top}$ 呢？

</li>

</ol>

:::loesung
(a) 行视角：$(1\cdot1+0\cdot3+2\cdot(-1),\ 2\cdot1+1\cdot3+0\cdot(-1))^{\top}=(-1,\,5)^{\top}$。列视角：$1\,(1,\,2)^{\top}+3\,(0,\,1)^{\top}-1\,(2,\,0)^{\top}=(1+0-2,\ 2+3-0)^{\top}=(-1,\,5)^{\top}$。

(b) $\mathbf{B}$ 有三列。$\mathbf{B}\,(1,\,2)^{\top}$ 没有定义，因为这个向量只有两个分量。$\mathbf{B}\,(1,\,2,\,3)^{\top}$ 有定义，它的分量个数与 $\mathbf{B}$ 的行数相同，即两个：$(1+0+6,\ 2+2+0)^{\top}=(7,\,4)^{\top}$。

(c) $\mathbf{H}$ 的列空间由第三个分量等于前两个分量之和的向量组成。对 $(2,\,0,\,2)^{\top}$，$2+0=2$：是，它就是 $\mathbf{H}\,(2,\,0)^{\top}$。对 $(2,\,1,\,2)^{\top}$，$2+1=3\ne2$：否。
:::
:::

:::aufgabe 练习 17 ★★ 月租金
<span class="anker" id="aufg-17"></span>

一份租金参考表用权重 $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ 估算公寓的月租金，单位分别是欧元每平方米、欧元每房间和欧元每公里。

<ol class="al">

<li>

把所有四套公寓的估计租金作为 $\mathbf{X}\mathbf{w}_{\mathrm M}$ 计算出来，按行视角和列视角各算一次。

</li>

<li>

你用了多少次乘法和加法？对于有 $20$ 个特征的 $10\,000$ 套公寓，需要多少次？

</li>

</ol>

:::loesung
(a) 行视角，对公寓 1：$12\cdot60+30\cdot2-8\cdot3=720+60-24=756$，同样得到 $502$、$1152$ 和 $914$ 欧元。列视角：

$$12\begin{pmatrix}60\\40\\90\\70\end{pmatrix}+30\begin{pmatrix}2\\1\\4\\3\end{pmatrix}-8\begin{pmatrix}3\\1\\6\\2\end{pmatrix}=\begin{pmatrix}720\\480\\1080\\840\end{pmatrix}+\begin{pmatrix}60\\30\\120\\90\end{pmatrix}-\begin{pmatrix}24\\8\\48\\16\end{pmatrix}=\begin{pmatrix}756\\502\\1152\\914\end{pmatrix}.$$

(b) 四个分量中的每一个都需要 $3$ 次乘法和 $2$ 次加法，共计 $12+8=20$ 次。对于有 $20$ 个特征的 $10\,000$ 套公寓，需要 $10\,000\cdot20=200\,000$ 次乘法和 $10\,000\cdot19=190\,000$ 次加法，共计 $390\,000\approx2mn$ 次，其中 $m=10\,000$，$n=20$。
:::
:::
