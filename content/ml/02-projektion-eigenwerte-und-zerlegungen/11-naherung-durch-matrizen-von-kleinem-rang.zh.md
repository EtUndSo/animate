---
title: 用低秩矩阵逼近
pfad: 计算机科学 / 机器学习 / 数学基础 / 投影、特征值与矩阵分解
knoten: 基础篇 2：投影、特征值与矩阵分解
nachschlagen: ja
order: 15221100
summary: 奇异值分解把矩阵的构件按大小排列。略去小的构件，剩下一个秩较低的矩阵，存储它所需的数要少得多。本节衡量这种逼近与原矩阵相差多远，并证明没有其他同秩矩阵离原矩阵更近。
tags: Frobenius 范数, 截断奇异值分解
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
奇异值分解把矩阵的构件按大小排列。略去小的构件，剩下一个秩较低的矩阵，存储它所需的数要少得多。本节衡量这种逼近与原矩阵相差多远，并证明没有其他同秩矩阵离原矩阵更近。
:::

### Frobenius 范数

<span class="anker" id="stufe-10-1"></span>

要说明两个矩阵彼此有多接近，就需要一个衡量它们之差大小的量。谱范数就是这样一个量；它衡量最大的拉长。第二个量更为直接：像基础篇 1 第 6.1 节中的图像那样，把矩阵逐行读成一个长向量，再取这个向量的欧几里得范数。

:::definition 定义 10.1 (Frobenius 范数)
<span class="anker" id="satz-10-1"></span>

$\mathbf{A}\in\mathbb{R}^{m\times n}$ 的__Frobenius 范数__为

$$\lVert\mathbf{A}\rVert_F=\sqrt{\sum_{i=1}^m\sum_{j=1}^na_{ij}^2} .$$
:::

:::satz 定理 10.2 (Frobenius 范数与奇异值)
<span class="anker" id="satz-10-2"></span>

对每个秩为 $r$ 的矩阵 $\mathbf{A}$，有

<span class="anker" id="gl-10-1"></span>
$$\lVert\mathbf{A}\rVert_F^2=\operatorname{tr}(\mathbf{A}^{\top}\mathbf{A})=d_1^2+d_2^2+\dots+d_r^2 . \tag{10.1}$$
:::

:::beweis Frobenius 范数
$\mathbf{A}^{\top}\mathbf{A}$ 的第 $j$ 个对角元素是 $\mathbf{a}_j^{\top}\mathbf{a}_j=\sum_ia_{ij}^2$，即第 $j$ 列长度的平方。所以迹，即这些元素之和，就是 $\mathbf{A}$ 的所有元素的平方和。由式 [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5)，迹也是 $\mathbf{A}^{\top}\mathbf{A}$ 的特征值之和，而这些特征值就是各个 $d_j^2$。
:::

两个推论。由于 $d_1^2\le\sum_jd_j^2$，有 $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F$。此外，正交矩阵不改变 Frobenius 范数：$(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$，所以 $\mathbf{Q}\mathbf{A}$ 与 $\mathbf{A}$ 有相同的奇异值。

⁠**算例：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$，有 $\lVert\mathbf{A}\rVert_F^2=4+9+0+4=17=4^2+1^2$（图 [24](#abb-24)），所以 $\lVert\mathbf{A}\rVert_F=\sqrt{17}\approx4.12$，比 $\lVert\mathbf{A}\rVert_2=4$ 稍大。

:::abbildung ml/k2rfrobenius 24
$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ 的 Frobenius 范数的平方：所有元素的平方和，等于各奇异值的平方和。
:::

⁠**简而言之：**Frobenius 范数是由所有元素构成的向量的欧几里得范数；它的平方是各奇异值的平方和。

### 截断分解

<span class="anker" id="stufe-10-2"></span>

把和 [(9.4)](die-singularwertzerlegung.html#gl-9-4) 在 $k$ 个最大的构件之后截断，就得到一个逼近。

:::definition 定义 10.3 (截断奇异值分解)
<span class="anker" id="satz-10-3"></span>

对于 $k<r$，

<span class="anker" id="gl-10-2"></span>
$$\mathbf{A}_k=\sum_{j=1}^kd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} \tag{10.2}$$

称为 $\mathbf{A}$ 含 $k$ 个构件的__截断奇异值分解__。
:::

$\mathbf{A}_k$ 的秩为 $k$，因为对 $j\le k$ 有 $\mathbf{A}_k\mathbf{v}_j=d_j\mathbf{u}_j$，对 $j>k$ 有 $\mathbf{A}_k\mathbf{v}_j=\mathbf{0}$；所以这些像张成一个 $k$ 维空间。误差就是和的其余部分：

$$\mathbf{A}-\mathbf{A}_k=\sum_{j=k+1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} .$$

它的格拉姆矩阵是 $\sum_{j>k}d_j^2\mathbf{v}_j\mathbf{v}_j^{\top}$，因为由 $\mathbf{u}_i^{\top}\mathbf{u}_j=0$，交叉项都消失了。它的特征值为 $d_{k+1}^2,\dots,d_r^2$，其余为零。所以误差的奇异值为 $d_{k+1},\dots,d_r$，由式 [(9.5)](die-singularwertzerlegung.html#gl-9-5) 和式 [(10.1)](#gl-10-1)，

<span class="anker" id="gl-10-3"></span>
$$\lVert\mathbf{A}-\mathbf{A}_k\rVert_2=d_{k+1},\qquad \lVert\mathbf{A}-\mathbf{A}_k\rVert_F=\sqrt{d_{k+1}^2+\dots+d_r^2} . \tag{10.3}$$

存储时，$\mathbf{A}_k$ 只需要 $k$ 个各有 $m$ 个分量的向量 $\mathbf{u}_j$、$k$ 个各有 $n$ 个分量的向量 $\mathbf{v}_j$ 以及 $k$ 个数 $d_j$，共 $k(m+n+1)$ 个数，而不是 $mn$ 个。

⁠**算例：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ 和 $k=1$，

$$\mathbf{A}_1=4\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1.6&3.2\\0.8&1.6\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\mathbf{u}_2\mathbf{v}_2^{\top}=\begin{pmatrix}0.4&-0.2\\-0.8&0.4\end{pmatrix}.$$

误差的 Frobenius 范数为 $\sqrt{0.16+0.04+0.64+0.16}=1=d_2$（图 [25](#abb-25)），它的谱范数同样如此。

:::abbildung ml/k2rfehler 25
秩 $1$ 最佳逼近在 Frobenius 范数下的误差的平方，其中 $0.4=\tfrac25$，$0.2=\tfrac15$，$0.8=\tfrac45$：它等于 $d_2^2=1$。
:::

⁠**简而言之：**$\mathbf{A}_k$ 保留 $k$ 个最大的构件；误差具有其余的奇异值，它的谱范数为 $d_{k+1}$。

### 最佳逼近

<span class="anker" id="stufe-10-3"></span>

秩为 $k$ 的矩阵有很多。截断分解是其中最好的吗？是的，在两种范数下都是。

:::satz 定理 10.4 (Eckart–Young 定理)
<span class="anker" id="satz-10-4"></span>

设 $\mathbf{A}$ 的秩为 $r$，且 $k<r$。对每个形状相同、满足 $\operatorname{rank}\mathbf{B}\le k$ 的矩阵 $\mathbf{B}$，有

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_2,\qquad \lVert\mathbf{A}-\mathbf{B}\rVert_F\ge\sqrt{d_{k+1}^2+\dots+d_r^2}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_F . \tag{10.4}$$

所以在所有秩至多为 $k$ 的矩阵中，$\mathbf{A}_k$ 离 $\mathbf{A}$ 最近。
:::

:::beweis 谱范数
由秩-零化度定理，$\mathbf{B}$ 的零空间的维数为 $n-\operatorname{rank}\mathbf{B}\ge n-k$。在零空间中选取 $n-k$ 个线性无关的向量 $\mathbf{b}_1,\dots,\mathbf{b}_{n-k}$，再添上 $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$。这是 $\mathbb{R}^n$ 中的 $n+1$ 个向量，由基础篇 1 第 13.4 节，它们线性相关，因为 $n$ 行的矩阵的秩至多为 $n$。所以存在不全为零的数，使 $\sum_l\alpha_l\mathbf{b}_l=\sum_j\beta_j\mathbf{v}_j$。这个向量 $\mathbf{z}$ 不为零，否则由两组向量各自的线性无关性，所有的数都为零。它既在 $\mathbf{B}$ 的零空间中，又在 $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$ 张成的空间中。把它归一化为长度 $1$。于是 $(\mathbf{A}-\mathbf{B})\mathbf{z}=\mathbf{A}\mathbf{z}$，并且由 $\mathbf{z}=\sum_{j\le k+1}c_j\mathbf{v}_j$、$\sum_jc_j^2=1$ 得

$$\lVert(\mathbf{A}-\mathbf{B})\mathbf{z}\rVert^2=\lVert\mathbf{A}\mathbf{z}\rVert^2=\sum_{j=1}^{k+1}d_j^2c_j^2\ge d_{k+1}^2\sum_{j=1}^{k+1}c_j^2=d_{k+1}^2 .$$

所以 $\mathbf{A}-\mathbf{B}$ 至少把单位向量 $\mathbf{z}$ 拉长 $d_{k+1}$ 倍，从而 $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}$。
:::

证明揭示了原因：秩为 $k$ 的矩阵必须把一整组方向映射为零，即它的零空间。这个零空间必然与 $\mathbf{A}$ 拉伸最强的 $k+1$ 个方向所张成的空间相交，而在那里 $\mathbf{B}$ 至少产生 $d_{k+1}$ 的误差。

⁠**算例：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$，$\mathbf{A}_1$ 是秩 $1$ 的最佳矩阵，在两种范数下误差都是 $1$。另一个秩 $1$ 矩阵，例如直接把第二行划掉的 $\mathbf{B}=\bigl(\begin{smallmatrix}2&3\\0&0\end{smallmatrix}\bigr)$，误差为 $\mathbf{A}-\mathbf{B}=\bigl(\begin{smallmatrix}0&0\\0&2\end{smallmatrix}\bigr)$，其范数为 $2$。

⁠**简而言之：**截断分解 $\mathbf{A}_k$ 是秩 $k$ 的最佳逼近，无论在谱范数下还是在 Frobenius 范数下都是如此。

:::hintergrund 为什么这一结论对 Frobenius 范数也成立
Frobenius 范数情形的证明把 $\mathbf{A}$ 的各行 $\mathbf{a}^{(1)\top},\dots,\mathbf{a}^{(m)\top}$ 看作 $\mathbb{R}^n$ 中的 $m$ 个点，就像数据矩阵中的各个样本那样。若 $\mathbf{B}$ 的秩至多为 $k$，它的各行就位于一个 $k$ 维子空间 $\mathcal S$ 中，即 $\mathbf{B}^{\top}$ 的列空间，必要时扩充到 $k$ 维。对于一个固定的子空间 $\mathcal S$ 及其投影矩阵 $\mathbf{P}$，由第 [4](projektion-auf-einen-unterraum.html#stufe-4) 节，每一行的投影 $\mathbf{P}\mathbf{a}^{(i)}$ 是 $\mathcal S$ 中离它最近的点。借助 $\mathcal S$ 的一组标准正交基 $\mathbf{w}_1,\dots,\mathbf{w}_k$，由勾股定理得

$$\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge\sum_i\bigl\lVert\mathbf{a}^{(i)}-\mathbf{P}\mathbf{a}^{(i)}\bigr\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_i\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2 ,$$

因为 $\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\sum_l(\mathbf{w}_l^{\top}\mathbf{a}^{(i)})^2$，而 $\mathbf{w}_l^{\top}\mathbf{a}^{(i)}$ 是 $\mathbf{A}\mathbf{w}_l$ 的第 $i$ 个分量。剩下要证明的是 $\sum_l\lVert\mathbf{A}\mathbf{w}_l\rVert^2\le d_1^2+\dots+d_k^2$。在各 $\mathbf{v}_j$ 的坐标下，

$$\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2=\sum_{l=1}^k\sum_jd_j^2(\mathbf{v}_j^{\top}\mathbf{w}_l)^2=\sum_jd_j^2\,g_j\qquad\text{其中}\qquad g_j=\sum_{l=1}^k(\mathbf{v}_j^{\top}\mathbf{w}_l)^2 .$$

每个 $g_j$ 都是 $\mathbf{v}_j$ 在 $\mathcal S$ 上的投影长度的平方，所以 $0\le g_j\le1$，而所有 $g_j$ 之和为 $\sum_l\lVert\mathbf{w}_l\rVert^2=k$。具有这种权重的和 $\sum_jd_j^2g_j$，在 $k$ 个最大的 $d_j^2$ 获得全部权重 $1$ 时最大；这个最大值是 $d_1^2+\dots+d_k^2$。结合式 [(10.1)](#gl-10-1)，得 $\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge d_{k+1}^2+\dots+d_r^2$。这个计算还顺带表明：使 $\mathbf{A}$ 的各行离它最近的子空间，就是 $\mathbf{v}_1,\dots,\mathbf{v}_k$ 张成的空间。
:::

### 用少数几个数表示一幅图像

<span class="anker" id="stufe-10-4"></span>

灰度图像就是一个矩阵。由 Eckart–Young 定理，$\mathbf{A}_k$ 是含 $k$ 个构件的最佳逼近，而式 [(10.3)](#gl-10-3) 表明损失了多少。比值

$$\frac{d_1^2+\dots+d_k^2}{d_1^2+\dots+d_r^2}$$

表明所有亮度值的平方和中有多大一部分得以保留。

⁠**算例：**基础篇 1 第 6.1 节中的十字为

$$\mathbf{C}=\begin{pmatrix}0&1&0\\1&1&1\\0&1&0\end{pmatrix}.$$

它是对称的。它的特征多项式为 $-\lambda^3+\lambda^2+2\lambda=-\lambda(\lambda-2)(\lambda+1)$；特征值为 $2$、$-1$ 和 $0$，对应的特征向量为 $(1,\,2,\,1)^{\top}$、$(1,\,-1,\,1)^{\top}$ 和 $(1,\,0,\,-1)^{\top}$。由第 [9.7](die-singularwertzerlegung.html#stufe-9-7) 节，奇异值为 $2$、$1$ 和 $0$；秩为 $2$。取 $\mathbf{q}_1=(1,\,2,\,1)^{\top}/\sqrt6$，秩 $1$ 的最佳逼近为

$$\mathbf{C}_1=2\,\mathbf{q}_1\mathbf{q}_1^{\top}=\frac13\begin{pmatrix}1&2&1\\2&4&2\\1&2&1\end{pmatrix},\qquad \mathbf{C}-\mathbf{C}_1=\frac13\begin{pmatrix}-1&1&-1\\1&-1&1\\-1&1&-1\end{pmatrix}$$

见图 [26](#abb-26)。在两种范数下，误差的大小都是 $1$。$\mathbf{C}_1$ 保留了和 $\lVert\mathbf{C}\rVert_F^2=5$ 中的 $4/5=80\,\%$。$\mathbf{C}_1$ 的每一行都是同一行 $(1,\,2,\,1)$ 的倍数：秩 $1$ 的图像是各列的亮度分布乘以各行的亮度分布，这里是一个中间最亮的模糊斑点。存储它只需要 $1\cdot(3+3+1)=7$ 个数，而不是 $9$ 个。

:::abbildung ml/k2bild 26
由 $3\times3$ 个像素组成的十字 $\mathbf{C}$（左，$0$ 为黑色，$1$ 为白色），它的秩 $1$ 最佳逼近 $\mathbf{C}_1$（中；值 $\tfrac43$ 比白色更亮，按白色显示），以及误差 $\mathbf{C}-\mathbf{C}_1$（右，红色为正，蓝色为负）。误差本身也是一个秩为 $1$ 的矩阵，即属于奇异值 $1$ 的构件。
:::

对于 $3\times3$ 像素的十字，这节省不了多少。对于大图像，差别就很可观了：一幅 $1000\times1000$ 像素的图像有 $10^6$ 个元素；含 $k=50$ 个构件的逼近需要 $50\cdot(1000+1000+1)=100\,050$ 个数，约为 $10\,\%$。逼近看起来是否好，取决于奇异值下降得有多快。在许多照片中，相邻的行非常相似；这时各行都靠近一个低维子空间，少数几个大的奇异值就承载了几乎整个和 $\sum_jd_j^2$。

⁠**简而言之：**秩为 $k$ 的图像需要 $k(m+n+1)$ 个数；截断分解是这类图像中最好的一个，$\sum_{j\le k}d_j^2/\sum_jd_j^2$ 表明保留了多少。

:::aufgabe 练习 30 ★ 矩阵的范数
<span class="anker" id="aufg-30"></span>

<ol class="al">

<li>

对练习 [27](die-singularwertzerlegung.html#aufg-27) 中的 $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$，计算 $\lVert\mathbf{A}\rVert_F$ 和 $\lVert\mathbf{A}\rVert_2$，并验证式 [(10.1)](#gl-10-1)。

</li>

<li>

$n\times n$ 正交矩阵的 Frobenius 范数是多少？

</li>

<li>

证明 $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F\le\sqrt r\,\lVert\mathbf{A}\rVert_2$。右边的不等式何时取等号？

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{A}\rVert_F^2=9+0+16+25=50=45+5=d_1^2+d_2^2$，所以 $\lVert\mathbf{A}\rVert_F=\sqrt{50}\approx7.07$，而 $\lVert\mathbf{A}\rVert_2=d_1=3\sqrt5\approx6.71$。

(b) 正交矩阵的所有奇异值都是 $1$，所以 $\lVert\mathbf{Q}\rVert_F^2=n$，$\lVert\mathbf{Q}\rVert_F=\sqrt n$。这也可以直接看出：$n$ 列中每一列的长度的平方都是 $1$。

(c) $\lVert\mathbf{A}\rVert_2^2=d_1^2\le d_1^2+\dots+d_r^2=\lVert\mathbf{A}\rVert_F^2$，并且这 $r$ 项中每一项至多为 $d_1^2$，所以 $\lVert\mathbf{A}\rVert_F^2\le r\,d_1^2$。开平方即得两个不等式。右边的不等式取等号，当且仅当所有正奇异值都等于 $d_1$，正交矩阵就是这种情况。
:::
:::

:::aufgabe 练习 31 ★★ 秩 1 的最佳矩阵
<span class="anker" id="aufg-31"></span>

设 $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$ 是练习 [28](die-singularwertzerlegung.html#aufg-28) 中的矩阵。

<ol class="al">

<li>

计算 $\mathbf{A}_1$，以及误差 $\mathbf{A}-\mathbf{A}_1$ 在两种范数下的大小。

</li>

<li>

全 1 矩阵 $\mathbf{B}$ 的秩也是 $1$。计算 $\lVert\mathbf{A}-\mathbf{B}\rVert_F$ 和 $\lVert\mathbf{A}-\mathbf{B}\rVert_2$，并与 (a) 比较。

</li>

<li>

所有元素的平方和中有多大比例保留在 $\mathbf{A}_1$ 中？

</li>

</ol>

:::loesung
(a) 由练习 [28](die-singularwertzerlegung.html#aufg-28)：$d_1=2$，$\mathbf{u}_1=(1,\,1,\,0)^{\top}/\sqrt2$，$\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$。所以

$$\mathbf{A}_1=2\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1&1\\1&1\\0&0\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\begin{pmatrix}0&0\\0&0\\1&-1\end{pmatrix}.$$

误差的 Frobenius 范数为 $\sqrt{1+1}=\sqrt2=d_2$。它是外积 $\mathbf{e}_3\,(1,\,-1)$，由练习 [29](die-singularwertzerlegung.html#aufg-29)，它唯一的奇异值为 $1\cdot\sqrt2$；它的谱范数也是 $\sqrt2$。

(b) $\mathbf{A}-\mathbf{B}=\Bigl(\begin{smallmatrix}0&0\\0&0\\0&-2\end{smallmatrix}\Bigr)$ 在两种范数下的大小都是 $2>\sqrt2$。正如 Eckart–Young 定理所要求的，$\mathbf{B}$ 比 $\mathbf{A}_1$ 离 $\mathbf{A}$ 更远。

(c) $\lVert\mathbf{A}\rVert_F^2=6=4+2$，$\mathbf{A}_1$ 保留了其中的 $d_1^2/(d_1^2+d_2^2)=\tfrac46=\tfrac23\approx67\,\%$。
:::
:::

:::aufgabe 练习 32 ★ 存储需求
<span class="anker" id="aufg-32"></span>

一幅灰度图像有 $600\times800$ 个像素。

<ol class="al">

<li>

含 $k=40$ 个构件的逼近需要多少个数？这占原来个数的多大比例？

</li>

<li>

$k$ 从多大开始，逼近就不再节省存储空间？

</li>

</ol>

:::loesung
(a) 需要 $40\cdot(600+800+1)=40\cdot1\,401=56\,040$ 个数，而不是 $600\cdot800=480\,000$ 个，约占 $11.7\,\%$。

(b) 只要 $k\cdot1\,401<480\,000$，即 $k\le342$，逼近就能节省存储空间，因为 $342\cdot1\,401=479\,142$，而 $343\cdot1\,401=480\,543$。从 $k=343$ 起，逼近所需的数比图像本身还多。秩至多为 $600$；反正也不会有超过 $600$ 个构件。
:::
:::
