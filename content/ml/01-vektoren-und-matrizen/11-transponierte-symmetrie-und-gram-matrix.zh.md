---
title: 转置、对称性与格拉姆矩阵
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: 第 1 章：向量与矩阵
nachschlagen: ja
order: 15211100
summary: 把矩阵的行与列互换，就得到它的转置。借助转置，一个数据集的所有点积都可以汇集在单个矩阵中：所有样本彼此之间的相似程度，以及所有特征彼此之间的关系。
tags: 转置, 对称矩阵, 格拉姆矩阵
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
把矩阵的行与列互换，就得到它的转置。借助转置，一个数据集的所有点积都可以汇集在单个矩阵中：所有样本彼此之间的相似程度，以及所有特征彼此之间的关系。
:::

### 转置

<span class="anker" id="stufe-10-1"></span>

符号 $^{\top}$ 在第 [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3) 小节中已经出现过：它把一列变成一行。对矩阵，它的意思相同，只是作用于每一列：第 $j$ 列变成第 $j$ 行。这样，矩阵就关于它的对角线作了一次镜像翻转。

:::definition 定义 10.1 (转置)
<span class="anker" id="satz-10-1"></span>

矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 的__转置__是满足下式的矩阵 $\mathbf{A}^{\top}\in\mathbb{R}^{n\times m}$：

<span class="anker" id="gl-10-1"></span>
$$(\mathbf{A}^{\top})_{ij}=a_{ji} . \tag{10.1}$$
:::

向量 $\mathbf{x}\in\mathbb{R}^d$ 是 $d\times1$ 矩阵，它的转置 $\mathbf{x}^{\top}$ 是元素相同的 $1\times d$ 矩阵。所以，第 [2.1](das-skalarprodukt.html#stufe-2-1) 小节中的记号 $\mathbf{u}^{\top}\mathbf{v}$ 现在名副其实地是一个矩阵乘积：$1\times d$ 矩阵乘以 $d\times1$ 矩阵；结果是 $1\times1$ 矩阵，即一个数。

:::satz 定理 10.2 (转置的运算规则)
<span class="anker" id="satz-10-2"></span>

对型相容的矩阵和标量 $c$，有

$$(\mathbf{A}^{\top})^{\top}=\mathbf{A},\qquad(\mathbf{A}+\mathbf{B})^{\top}=\mathbf{A}^{\top}+\mathbf{B}^{\top},\qquad(c\,\mathbf{A})^{\top}=c\,\mathbf{A}^{\top},\qquad(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top} .$$
:::

:::herleitung 乘积的转置
对 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 和 $\mathbf{B}\in\mathbb{R}^{n\times k}$，由式 [(10.1)](#gl-10-1) 和式 [(9.1)](das-matrixprodukt.html#gl-9-1)，

$$\bigl((\mathbf{A}\mathbf{B})^{\top}\bigr)_{li}=(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^na_{ij}\,b_{jl}=\sum_{j=1}^n(\mathbf{B}^{\top})_{lj}\,(\mathbf{A}^{\top})_{ji}=(\mathbf{B}^{\top}\mathbf{A}^{\top})_{li} .$$

前三条规则直接由定义得出。
:::

::::beispiel [算例]
$$\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}^{\top}=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}.$$

对 $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ 和 $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$，有 $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$，所以 $(\mathbf{C}\mathbf{D})^{\top}=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$。由 $\mathbf{D}^{\top}\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$ 得到同样的结果，而 $\mathbf{C}^{\top}\mathbf{D}^{\top}=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$ 则是另一个矩阵。
::::

⁠**简而言之：**转置交换行与列；对乘积，顺序要反过来，$(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$。

:::hintergrund 为什么转置乘积时顺序要反过来
在乘积 $\mathbf{A}\mathbf{B}$ 中，$\mathbf{A}$ 的行与 $\mathbf{B}$ 的列相遇。转置之后，$\mathbf{A}$ 的行成了 $\mathbf{A}^{\top}$ 的列，$\mathbf{B}$ 的列成了 $\mathbf{B}^{\top}$ 的行。要使行再与列相遇，$\mathbf{B}^{\top}$ 必须在左边。从型也能看出这一点：$(\mathbf{A}\mathbf{B})^{\top}$ 是 $k\times m$ 型的，而 $\mathbf{B}^{\top}\mathbf{A}^{\top}$ 是 $(k\times n)\cdot(n\times m)$，型正好匹配。表达式 $\mathbf{A}^{\top}\mathbf{B}^{\top}$ 则是 $(n\times m)\cdot(k\times n)$，只有恰好 $m=k$ 时才有定义。这条规则的一个特例是 $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$：一个数等于它自身的转置，所以 $\mathbf{u}^{\top}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{u}$。
:::

### 对称矩阵

<span class="anker" id="stufe-10-2"></span>

有些表格关于对角线作镜像翻转后保持不变。城市之间的距离表就是一例：从慕尼黑到科隆的路程与从科隆到慕尼黑的一样长。

:::definition 定义 10.3 (对称矩阵)
<span class="anker" id="satz-10-3"></span>

满足 $\mathbf{A}^{\top}=\mathbf{A}$，即对所有 $i,j$ 都有 $a_{ij}=a_{ji}$ 的方阵 $\mathbf{A}$，称为__对称矩阵__。
:::

每个对角矩阵都是对称的。对称矩阵的一个重要来源，是矩阵与其自身转置的乘积：对每个矩阵 $\mathbf{A}$，

<span class="anker" id="gl-10-2"></span>
$$(\mathbf{A}^{\top}\mathbf{A})^{\top}=\mathbf{A}^{\top}(\mathbf{A}^{\top})^{\top}=\mathbf{A}^{\top}\mathbf{A} , \tag{10.2}$$

所以 $\mathbf{A}^{\top}\mathbf{A}$ 是对称的，$\mathbf{A}\mathbf{A}^{\top}$ 也是。

::::beispiel [算例]
$\bigl(\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\bigr)$ 是对称的，旋转 $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ 则不是。对 $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$，

$$\mathbf{C}^{\top}\mathbf{C}=\begin{pmatrix}1&3\\2&4\end{pmatrix}\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}10&14\\14&20\end{pmatrix},$$

它是对称的，正如式 [(10.2)](#gl-10-2) 所要求的。
::::

⁠**简而言之：**对称矩阵等于它的转置；$\mathbf{A}^{\top}\mathbf{A}$ 和 $\mathbf{A}\mathbf{A}^{\top}$ 总是对称的。

:::hintergrund 带权重的点积
在点积 $\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$ 中，每个位置都同等计入。如果希望各位置计入的比重不同，就取正的权重 $d_1,\dots,d_n$，构成 $\sum_jd_j\,u_jv_j$。借助对角矩阵 $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$，这就是 $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$，因为 $\mathbf{D}\mathbf{v}=(d_1v_1,\dots,d_nv_n)^{\top}$。

这个数遵循与普通点积相同的运算规则。它对两个向量中的每一个都是线性的，并且对每个 $\mathbf{u}\ne\mathbf{0}$，$\mathbf{u}^{\top}\mathbf{D}\mathbf{u}=\sum_jd_ju_j^2$ 都为正。它是对称的，因为 $\mathbf{D}$ 是对称的：一个数等于它自身的转置，再两次应用乘积的转置规则，得到 $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{D}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{D}^{\top}\mathbf{u}=\mathbf{v}^{\top}\mathbf{D}\mathbf{u}$。由于柯西-施瓦茨不等式的证明只用到了这些规则，你同样可以用 $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$ 来度量长度、距离和角度。只是结果会不同。例如，$(1,\,1)^{\top}$ 和 $(-1,\,1)^{\top}$ 在通常意义下是正交的，但对 $\mathbf{D}=\operatorname{diag}(2,\,1)$ 则不然：$(1,\,1)\,\mathbf{D}\,(-1,\,1)^{\top}=2\cdot1\cdot(-1)+1\cdot1\cdot1=-1$。

第 [4.5](abstande-und-einheiten.html#stufe-4-5) 小节中的标准化恰好就是这样一种加权。两个标准化样本之间的距离为 $\sqrt{(\mathbf{x}_a-\mathbf{x}_b)^{\top}\mathbf{D}\,(\mathbf{x}_a-\mathbf{x}_b)}$，其中 $\mathbf{D}=\operatorname{diag}(1/s_1^2,\dots,1/s_d^2)$。反过来，每一种这样的加权都相当于换算单位：如果把特征 $j$ 乘以 $\sqrt{d_j}$，换算后向量的普通点积就是 $\sum_j(\sqrt{d_j}\,u_j)(\sqrt{d_j}\,v_j)=\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$。所以，单位的选择与 $\mathbf{D}$ 中权重的选择是同一个决定。
:::

### 样本的格拉姆矩阵

<span class="anker" id="stufe-10-3"></span>

数据集中的每个样本与其他每个样本有多相似？可以把所有两两之间的点积写进一张表格：第 $i$ 行第 $k$ 列是 $\mathbf{x}_i^{\top}\mathbf{x}_k$。这张表格就是单个矩阵乘积。

:::definition 定义 10.4 (格拉姆矩阵)
<span class="anker" id="satz-10-4"></span>

向量列表 $\mathbf{v}_1,\dots,\mathbf{v}_k$ 的__格拉姆矩阵__是由两两之间的点积构成的 $k\times k$ 矩阵，第 $i$ 行第 $l$ 列的元素为 $\mathbf{v}_i^{\top}\mathbf{v}_l$。
:::

对数据集的样本，这就是矩阵 $\mathbf{X}\mathbf{X}^{\top}\in\mathbb{R}^{N\times N}$，因为它的元素 $(i,k)$ 是 $\mathbf{X}$ 的第 $i$ 行乘以 $\mathbf{X}^{\top}$ 的第 $k$ 列，即 $\mathbf{x}_i^{\top}\mathbf{x}_k$：

<span class="anker" id="gl-10-3"></span>
$$(\mathbf{X}\mathbf{X}^{\top})_{ik}=\mathbf{x}_i^{\top}\mathbf{x}_k . \tag{10.3}$$

它是对称的，对角线上是长度的平方 $\lVert\mathbf{x}_i\rVert^2$，并且由式 [(4.1)](abstande-und-einheiten.html#gl-4-1)，从它可以读出所有距离：

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{x}_i-\mathbf{x}_k\rVert^2=(\mathbf{X}\mathbf{X}^{\top})_{ii}+(\mathbf{X}\mathbf{X}^{\top})_{kk}-2\,(\mathbf{X}\mathbf{X}^{\top})_{ik} . \tag{10.4}$$

把元素 $(i,k)$ 除以 $\sqrt{(\mathbf{X}\mathbf{X}^{\top})_{ii}\,(\mathbf{X}\mathbf{X}^{\top})_{kk}}$，就得到 $\mathbf{x}_i$ 与 $\mathbf{x}_k$ 的余弦相似度。

::::beispiel [算例]
对第 [5.4](winkel-und-ahnlichkeit.html#stufe-5-4) 小节中的三篇文本，

$$\mathbf{X}=\begin{pmatrix}3&2&0\\6&4&0\\0&1&3\end{pmatrix},\qquad \mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}13&26&2\\26&52&4\\2&4&10\end{pmatrix}.$$

由式 [(10.4)](#gl-10-4)，文本 1 与文本 3 之间的距离为 $\sqrt{13+10-2\cdot2}=\sqrt{19}$，与前面算出的一致。文本 1 与文本 2 的余弦相似度为 $26/\sqrt{13\cdot52}=1$。
::::

⁠**简而言之：**格拉姆矩阵 $\mathbf{X}\mathbf{X}^{\top}$ 是样本两两之间所有点积构成的表格；所有长度、距离和角度都可以由它得出。

:::hintergrund 格拉姆矩阵包含数据集的全部几何信息
样本之间的长度、距离和角度只取决于点积，而不取决于各个坐标。例如，把整个数据集绕原点旋转，所有坐标都会改变，但没有一个点积改变，格拉姆矩阵保持不变。所以，格拉姆矩阵相同的两个数据集在几何上看起来是一样的。因此，如果只想知道哪些样本彼此相似，就不需要数据矩阵本身，只需要它的格拉姆矩阵。
:::

### 特征的格拉姆矩阵

<span class="anker" id="stufe-10-4"></span>

把角色反过来，就得到一张关于特征的表格：在所有样本上，两个特征在多大程度上相伴而行？它们的特征列是 $\mathbb{R}^N$ 中的向量，而它们的点积衡量的正是这一点。各列的这个格拉姆矩阵是 $\mathbf{X}^{\top}\mathbf{X}\in\mathbb{R}^{d\times d}$：

<span class="anker" id="gl-10-5"></span>
$$(\mathbf{X}^{\top}\mathbf{X})_{jl}=\sum_{i=1}^Nx_{ij}\,x_{il} . \tag{10.5}$$

元素 $(j,l)$ 是第 $j$ 个与第 $l$ 个特征列的点积；对角线上是每个特征的平方和。

:::satz 定理 10.5 (格拉姆矩阵作为对样本的求和)
<span class="anker" id="satz-10-5"></span>

<span class="anker" id="gl-10-6"></span>
$$\mathbf{X}^{\top}\mathbf{X}=\sum_{i=1}^N\mathbf{x}_i\,\mathbf{x}_i^{\top} . \tag{10.6}$$

每个样本贡献它自己的外积。
:::

右边的元素 $(j,l)$ 是 $\sum_ix_{ij}\,x_{il}$，与式 [(10.5)](#gl-10-5) 相同。所以，如果新增一个样本，$\mathbf{X}^{\top}\mathbf{X}$ 只多出一层 $\mathbf{x}_{N+1}\mathbf{x}_{N+1}^{\top}$；不必全部重新计算。

::::beispiel [算例]
对这些文本，

$$\mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$

第一行的元素是“进球”列与三个特征列的点积（图 [37](#abb-37)）。

:::abbildung ml/k1rgrammerk 37
特征的格拉姆矩阵的第一行：“进球”列 $(3,\,6,\,0)^{\top}$ 乘以它自身、乘以“球”列 $(2,\,4,\,1)^{\top}$，以及乘以“选举”列 $(0,\,0,\,3)^{\top}$。
:::

位置 $(1,3)$ 上的 $0$ 是说：“进球”和“选举”这两个词在任何一篇文本中都没有同时出现。写成三个外积之和：

$$\begin{pmatrix}9&6&0\\6&4&0\\0&0&0\end{pmatrix}+\begin{pmatrix}36&24&0\\24&16&0\\0&0&0\end{pmatrix}+\begin{pmatrix}0&0&0\\0&1&3\\0&3&9\end{pmatrix}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$
::::

⁠**简而言之：**$\mathbf{X}^{\top}\mathbf{X}$ 是特征列的格拉姆矩阵；它是所有样本的外积 $\mathbf{x}_i\mathbf{x}_i^{\top}$ 之和。

:::aufgabe 练习 24 ★ 转置
<span class="anker" id="aufg-24"></span>

<ol class="al">

<li>

对 $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ 给出 $\mathbf{B}^{\top}$，并计算 $\mathbf{B}^{\top}\mathbf{B}$ 和 $\mathbf{B}\mathbf{B}^{\top}$。它们是什么型的？是对称的吗？

</li>

<li>

用运算规则证明：$(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$。

</li>

</ol>

:::loesung
(a) $\mathbf{B}^{\top}=\Bigl(\begin{smallmatrix}1&2\\0&1\\2&0\end{smallmatrix}\Bigr)$。于是

$$\mathbf{B}^{\top}\mathbf{B}=\begin{pmatrix}5&2&2\\2&1&0\\2&0&4\end{pmatrix}\in\mathbb{R}^{3\times3},\qquad \mathbf{B}\mathbf{B}^{\top}=\begin{pmatrix}5&2\\2&5\end{pmatrix}\in\mathbb{R}^{2\times2}.$$

两者都是对称的，正如式 [(10.2)](#gl-10-2) 所要求的。$\mathbf{B}^{\top}\mathbf{B}$ 的元素 $(1,1)$ 为 $1^2+2^2=5$，即第一列的平方和；$\mathbf{B}\mathbf{B}^{\top}$ 的元素 $(1,2)$ 为 $1\cdot2+0\cdot1+2\cdot0=2$，即两行的点积。

(b) 两次应用乘积的转置规则：$(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\bigl((\mathbf{A}\mathbf{B})\mathbf{C}\bigr)^{\top}=\mathbf{C}^{\top}(\mathbf{A}\mathbf{B})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$。
:::
:::

:::aufgabe 练习 25 ★★ 一个小数据集的格拉姆矩阵
<span class="anker" id="aufg-25"></span>

一个数据集有三个样本、两个特征：$\mathbf{x}_1=(1,\,0)^{\top}$，$\mathbf{x}_2=(2,\,1)^{\top}$，$\mathbf{x}_3=(0,\,3)^{\top}$。

<ol class="al">

<li>

建立 $\mathbf{X}$，并计算 $\mathbf{X}\mathbf{X}^{\top}$ 和 $\mathbf{X}^{\top}\mathbf{X}$。

</li>

<li>

从 $\mathbf{X}\mathbf{X}^{\top}$ 读出 $\mathbf{x}_2$ 与 $\mathbf{x}_3$ 之间的距离，并直接验算。

</li>

<li>

把三个外积 $\mathbf{x}_i\mathbf{x}_i^{\top}$ 相加，以验证式 [(10.6)](#gl-10-6)。

</li>

</ol>

:::loesung
(a) $\mathbf{X}=\Bigl(\begin{smallmatrix}1&0\\2&1\\0&3\end{smallmatrix}\Bigr)$，

$$\mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}1&2&0\\2&5&3\\0&3&9\end{pmatrix},\qquad \mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}5&2\\2&10\end{pmatrix}.$$

(b) 由式 [(10.4)](#gl-10-4)，$\lVert\mathbf{x}_2-\mathbf{x}_3\rVert^2=5+9-2\cdot3=8$，所以距离为 $\sqrt8\approx2.83$。直接计算：$\mathbf{x}_2-\mathbf{x}_3=(2,\,-2)^{\top}$，其长度平方为 $4+4=8$。

(c) $\mathbf{x}_1\mathbf{x}_1^{\top}=\bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)$，$\mathbf{x}_2\mathbf{x}_2^{\top}=\bigl(\begin{smallmatrix}4&2\\2&1\end{smallmatrix}\bigr)$，$\mathbf{x}_3\mathbf{x}_3^{\top}=\bigl(\begin{smallmatrix}0&0\\0&9\end{smallmatrix}\bigr)$；它们的和为 $\bigl(\begin{smallmatrix}5&2\\2&10\end{smallmatrix}\bigr)=\mathbf{X}^{\top}\mathbf{X}$。
:::
:::
