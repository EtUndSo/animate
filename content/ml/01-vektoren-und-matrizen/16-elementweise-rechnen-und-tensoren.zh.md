---
title: 逐元素运算与张量
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: 第 1 章：向量与矩阵
nachschlagen: ja
order: 15211600
summary: 并非向量和矩阵的每种运算都是矩阵乘积。本节介绍逐个元素进行的运算，并把向量和矩阵推广为有两个以上下标的数阵，图像就需要这样的数阵。
tags: 哈达玛积, 逐元素, 张量, 轴, 形状
lang: zh
---

<span class="anker" id="stufe-15"></span>

:::zweck
并非向量和矩阵的每种运算都是矩阵乘积。本节介绍逐个元素进行的运算，并把向量和矩阵推广为有两个以上下标的数阵，图像就需要这样的数阵。
:::

### 哈达玛积

<span class="anker" id="stufe-15-1"></span>

一位商人有一份已售数量的列表和一份单价的列表。他想知道每种商品的营业额，即数量乘以价格，但暂时还不求总和。这是逐个元素的乘积。

:::definition 定义 15.1 (哈达玛积)
<span class="anker" id="satz-15-1"></span>

对两个型相同的向量或两个型相同的矩阵，__哈达玛积__ $\mathbf{A}\odot\mathbf{B}$ 是逐个元素的乘积：

<span class="anker" id="gl-15-1"></span>
$$(\mathbf{A}\odot\mathbf{B})_{ij}=a_{ij}\,b_{ij} . \tag{15.1}$$
:::

哈达玛积**不是**矩阵乘积。矩阵乘积构成行与列的点积；哈达玛积只把同一位置上的元素相乘。它与已知内容有两点联系：把两个向量的哈达玛积的各分量相加，就得到它们的点积，$\mathbf 1^{\top}(\mathbf{u}\odot\mathbf{v})=\mathbf{u}^{\top}\mathbf{v}$。与一个固定向量的哈达玛积，就是乘以一个对角矩阵：$\mathbf{v}\odot\mathbf{x}=\operatorname{diag}(\mathbf{v})\,\mathbf{x}$。

::::beispiel [算例]
$(1,\,2,\,3)^{\top}\odot(4,\,5,\,6)^{\top}=(4,\,10,\,18)^{\top}$，而 $4+10+18=32$ 就是点积。对矩阵，

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}\odot\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&2\\3&0\end{pmatrix},\qquad\text{但}\qquad \begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\4&3\end{pmatrix}.$$

用由零和一组成的向量可以屏蔽特征：$(1,\,0,\,1)^{\top}\odot\mathbf{x}_1=(60,\,0,\,3)^{\top}$ 去掉了公寓 1 的房间数。
::::

⁠**简而言之：**哈达玛积 $\odot$ 逐个元素相乘；它不是矩阵乘积。

### 逐元素函数

<span class="anker" id="stufe-15-2"></span>

常常要对向量的每个元素作用同一个函数：把所有误差平方，对所有误差取绝对值，或者把所有值取整。

:::definition 定义 15.2 (逐元素函数)
<span class="anker" id="satz-15-2"></span>

对函数 $f\colon\mathbb{R}\to\mathbb{R}$ 和向量 $\mathbf{x}\in\mathbb{R}^d$，__逐元素__作用的 $f$ 给出向量 $\bigl(f(x_1),\dots,f(x_d)\bigr)^{\top}$。对矩阵，同样逐个元素进行。
:::

许多范数可以这样写出：1-范数是逐元素绝对值之和，$\lVert\mathbf{x}\rVert_1=\mathbf 1^{\top}|\mathbf{x}|$，欧几里得范数的平方是逐元素平方之和。逐元素函数一般不是线性的：逐元素平方把 $2\mathbf{x}$ 变成元素为 $4x_j^2$ 而不是 $2x_j^2$ 的向量。

::::beispiel [算例]
房产经纪人的误差向量是 $(-12,\,-4,\,-4,\,-8)^{\top}$。逐元素取绝对值得到 $(12,\,4,\,4,\,8)^{\top}$，其和 $28$ 就是 1-范数。对第 [3.5](normen-die-groe-eines-vektors.html#stufe-3-5) 小节中的评估师 A，逐元素平方得到 $(100,\,100,\,100,\,100)^{\top}$，其和为 $400=20^2$。
::::

⁠**简而言之：**逐元素函数分别作用于每个元素；它一般不是线性的。

### 给每一行加上一个向量

<span class="anker" id="stufe-15-3"></span>

要使整个数据集中心化，就从数据矩阵的每一行减去同一个向量，即样本均值。同样，仿射预测给每个分量加上同一个截距。这样的运算需要一种记号。

样本均值由一个矩阵-向量乘积给出：$\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$，因为它的第 $j$ 个分量是 $\frac1N\sum_ix_{ij}$，即第 $j$ 列的均值。各行都等于 $\bar{\mathbf{x}}^{\top}$ 的矩阵是外积 $\mathbf 1\,\bar{\mathbf{x}}^{\top}$。所以中心化的数据矩阵为

<span class="anker" id="gl-15-2"></span>
$$\tilde{\mathbf{X}}=\mathbf{X}-\mathbf 1\,\bar{\mathbf{x}}^{\top} , \tag{15.2}$$

它的第 $i$ 行是向量 $(\mathbf{x}_i-\bar{\mathbf{x}})^{\top}$。许多文献简写为 $\mathbf{X}-\bar{\mathbf{x}}^{\top}$，意思是：从每一行减去这个行向量。严格地说，$N\times d$ 矩阵与 $1\times d$ 矩阵之差是没有定义的；这种简写总是代表式 [(15.2)](#gl-15-2)。

::::beispiel [算例]
对公寓数据集，$\bar{\mathbf{x}}=\tfrac14\mathbf{X}^{\top}\mathbf 1=(65,\ 2.5,\ 3)^{\top}$，并且

$$\tilde{\mathbf{X}}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}-\begin{pmatrix}65&2.5&3\\65&2.5&3\\65&2.5&3\\65&2.5&3\end{pmatrix}=\begin{pmatrix}-5&-0.5&0\\-25&-1.5&-2\\25&1.5&3\\5&0.5&-1\end{pmatrix}.$$

每一列都是第 [4.3](abstande-und-einheiten.html#stufe-4-3) 小节中中心化的特征列，其和为零。
::::

⁠**简而言之：**给矩阵 $\mathbf{A}$ 的每一行加上向量 $\mathbf{q}$，就是计算 $\mathbf{A}+\mathbf 1\,\mathbf{q}^{\top}$；常见的简写 $\mathbf{A}+\mathbf{q}^{\top}$ 指的正是这个。

### 张量

<span class="anker" id="stufe-15-4"></span>

标量是单个数，向量是带一个下标的列表，矩阵是带两个下标的表格。彩色图像需要三个下标：行、列和颜色通道。一叠彩色图像需要四个。所有这些数阵都归在一个名称之下。

:::definition 定义 15.3 (张量、形状)
<span class="anker" id="satz-15-3"></span>

在机器学习中，__张量__是一个数阵，它的元素用 $k$ 个下标编号。每个下标沿一根__轴__变化。各轴长度构成的列表称为张量的__形状__。
:::

标量是有 $0$ 根轴的张量，$\mathbb{R}^d$ 中的向量是只有一根长度为 $d$ 的轴的张量，$\mathbb{R}^{m\times n}$ 中的矩阵是形状为 $m\times n$ 的张量。形状为 $n_1\times n_2\times\dots\times n_k$ 的张量有 $n_1\cdot n_2\cdots n_k$ 个元素。图 [42](#abb-42) 展示了最初的几级。

:::abbildung ml/k1tensor 42
有 $0$ 至 $4$ 根轴的张量：标量、有 $4$ 个元素的向量、$4\times4$ 矩阵（例如一幅灰度图像）、由红、绿、蓝三个 $4\times4$ 通道组成的彩色图像，以及由 $N$ 幅这样的彩色图像组成的堆叠（图中用三幅图像示意）。
:::

::::beispiel [算例]
一幅 $4\times4$ 像素、有三个颜色通道的彩色图像，是形状为 $3\times4\times4$ 的张量，有 $48$ 个元素。下标为 $(1,2,3)$ 的元素，是第一个通道（即红色）在第 $2$ 行第 $3$ 列像素处的亮度。
::::

⁠**简而言之：**张量是有任意多根轴的数阵；标量、向量和矩阵是有 $0$、$1$ 和 $2$ 根轴的情形。

:::hintergrund 物理学中的张量是另一回事
在物理学中，张量不只是一个数阵，例如惯性张量，它给出绕每个轴转动一个物体有多难；又如描述一根受载的梁在每个方向上被拉伸或压缩得多厉害的张量。在那里，张量附带一条规则，规定旋转坐标系时它的元素如何变化；光有这些元素还不构成张量。在机器学习中没有这条规则：张量在那里只是一个多维数阵。词是同一个，概念却不同。
:::

### 作为张量的图像

<span class="anker" id="stufe-15-5"></span>

图像数据是轴多于两根的张量中最重要的情形。从它们的形状，立刻就能看出一个数据集包含多少个数。

一幅 $28\times28$ 像素的灰度图像是一个矩阵，即形状为 $28\times28$、有 $784$ 个元素的张量。一幅 $32\times32$ 像素的彩色图像有三个通道，形状为 $3\times32\times32$，即有 $3072$ 个元素。由 $100$ 幅这样的彩色图像组成的堆叠，形状为 $100\times3\times32\times32$，有 $307\,200$ 个元素。这里第一根轴为样本计数，与数据矩阵的行一样：数据矩阵是向量堆叠的特例，形状为 $N\times d$。

轴的顺序是一种约定。有些程序把颜色通道放在最前面，即 $3\times32\times32$；有些放在最后面，即 $32\times32\times3$。数是相同的，只是排列不同；在任何计算之前，都必须弄清楚哪根轴表示什么。

::::beispiel [算例]
由 $60\,000$ 幅 $28\times28$ 像素的灰度图像组成的数据集，是形状为 $60\,000\times28\times28$、有 $47\,040\,000$ 个元素的张量。如果把每幅图像读出成 $\mathbb{R}^{784}$ 中的一个向量，它就变成 $\mathbb{R}^{60\,000\times784}$ 中的数据矩阵，元素不变。
::::

⁠**简而言之：**一幅图像是有两根或三根轴的张量，一叠图像则多一根轴；第一根轴为样本计数。

:::aufgabe 练习 36 ★ 是否逐元素？
<span class="anker" id="aufg-36"></span>

<ol class="al">

<li>

对 $\mathbf{u}=(2,\,-1,\,3)^{\top}$ 和 $\mathbf{v}=(1,\,4,\,2)^{\top}$，计算 $\mathbf{u}\odot\mathbf{v}$ 和 $\mathbf{u}^{\top}\mathbf{v}$。

</li>

<li>

计算 $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\odot\bigl(\begin{smallmatrix}2&0\\1&3\end{smallmatrix}\bigr)$，以及这两个矩阵的矩阵乘积。

</li>

<li>

由 $64$ 幅 $224\times224$ 像素的彩色图像组成的堆叠，颜色通道在前，形状是什么？有多少个元素？

</li>

</ol>

:::loesung
(a) $\mathbf{u}\odot\mathbf{v}=(2,\,-4,\,6)^{\top}$，$\mathbf{u}^{\top}\mathbf{v}=2-4+6=4$，即哈达玛积各元素之和。

(b) 哈达玛积：$\bigl(\begin{smallmatrix}1\cdot2&2\cdot0\\3\cdot1&4\cdot3\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&0\\3&12\end{smallmatrix}\bigr)$。矩阵乘积：$\bigl(\begin{smallmatrix}2+2&0+6\\6+4&0+12\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4&6\\10&12\end{smallmatrix}\bigr)$。只有右下角的元素碰巧一致。

(c) 形状为 $64\times3\times224\times224$，共有 $64\cdot3\cdot224\cdot224=9\,633\,792$ 个元素。
:::
:::

:::aufgabe 练习 37 ★★ 数据集的中心化
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

证明：中心化数据矩阵式 [(15.2)](#gl-15-2) 的各列之和为零，即 $\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf{0}^{\top}$。请利用 $\mathbf 1^{\top}\mathbf 1=N$。

</li>

<li>

把第 [5.4](winkel-und-ahnlichkeit.html#stufe-5-4) 小节中三篇文本的数据矩阵中心化。

</li>

</ol>

:::loesung
(a) 有 $\bar{\mathbf{x}}^{\top}=\frac1N\mathbf 1^{\top}\mathbf{X}$，它是 $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$ 的转置。因此

$$\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf 1^{\top}\mathbf{X}-(\mathbf 1^{\top}\mathbf 1)\,\bar{\mathbf{x}}^{\top}=\mathbf 1^{\top}\mathbf{X}-N\cdot\tfrac1N\,\mathbf 1^{\top}\mathbf{X}=\mathbf{0}^{\top} .$$

每一列都是一个中心化向量，它的各分量之和为零，与第 [4.3](abstande-und-einheiten.html#stufe-4-3) 小节中一样。

(b) 三篇文本的均值为 $\bar{\mathbf{x}}=\tfrac13\bigl((3,2,0)^{\top}+(6,4,0)^{\top}+(0,1,3)^{\top}\bigr)=(3,\,\tfrac73,\,1)^{\top}$。中心化后：

$$\tilde{\mathbf{X}}=\begin{pmatrix}0&-\frac13&-1\\3&\frac53&-1\\-3&-\frac43&2\end{pmatrix}.$$

每一列之和都为零：$0+3-3=0$，$-\tfrac13+\tfrac53-\tfrac43=0$，$-1-1+2=0$。
:::
:::
