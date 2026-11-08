---
title: 矩阵与数据矩阵
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
knoten: 基础篇 1：向量与矩阵
nachschlagen: ja
order: 15210700
summary: 一个数据集由许多分量个数相同的向量组成。本节把它们合成一张数字表格，即一个矩阵，并规定矩阵的写法和运算方法。
tags: 矩阵, 元素, 型, 方阵, 对角线, 对角矩阵, 零矩阵, 数据矩阵
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
一个数据集由许多分量个数相同的向量组成。本节把它们合成一张数字表格，即一个矩阵，并规定矩阵的写法和运算方法。
:::

### 矩阵

<span class="anker" id="stufe-6-1"></span>

公寓表格不只是四个各自独立的向量：它是一个你想要作为整体来计算的对象。灰度图像也是一张表格，即按行和列排列的亮度值。这种矩形排列的数阵称为矩阵。

:::definition 定义 6.1 (矩阵)
<span class="anker" id="satz-6-1"></span>

__矩阵__ $\mathbf{A}\in\mathbb{R}^{m\times n}$ 是把 $m\cdot n$ 个实数排成 $m$ 行、$n$ 列的矩形阵列：

$$\mathbf{A}=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix}.$$

第 $i$ 行第 $j$ 列的数 $a_{ij}$ 称为矩阵的__元素__。$m\times n$ 这一对数称为矩阵的__型__。
:::

矩阵用粗体大写字母表示，它的元素用相应的小写字母加两个下标表示：先写行，再写列。$\mathbf{A}$ 的第 $j$ 列是一个有 $m$ 个分量的向量，记作 $\mathbf{a}_j$。于是矩阵也可以写成由它的各列排成的一行：$\mathbf{A}=\begin{pmatrix}\mathbf{a}_1&\cdots&\mathbf{a}_n\end{pmatrix}$。有 $d$ 个分量的向量是 $d\times1$ 型矩阵，有 $d$ 个数的一行是 $1\times d$ 型矩阵。

如果两个矩阵型相同，并且每个位置上的元素都相同，就称它们相等。同型矩阵的加法和数乘与向量一样，都是逐个元素进行的：$(\mathbf{A}+\mathbf{B})_{ij}=a_{ij}+b_{ij}$，$(c\,\mathbf{A})_{ij}=c\,a_{ij}$。

⁠**算例：**矩阵

$$\mathbf{A}=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\in\mathbb{R}^{2\times3}$$

的型为 $2\times3$，元素 $a_{12}=2$，$a_{21}=4$，第二列为 $\mathbf{a}_2=(2,\,5)^{\top}$。一幅 $3\times3$ 像素、在暗背景上显示一个亮十字的灰度图像，就是行为 $(0,1,0)$、$(1,1,1)$ 和 $(0,1,0)$ 的矩阵。此外，

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}+\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}1&3\\4&4\end{pmatrix},\qquad 2\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}2&4\\6&8\end{pmatrix}.$$

⁠**简而言之：**矩阵是有 $m$ 行、$n$ 列的矩形数字表格；元素 $a_{ij}$ 位于第 $i$ 行第 $j$ 列。

:::hintergrund 图像作为矩阵和作为向量
把一幅图像逐行读出并把各行首尾相接，矩阵就变成一个长向量：$3\times3$ 的十字变成向量 $(0,1,0,1,1,1,0,1,0)^{\top}\in\mathbb{R}^9$，一幅 $28\times28$ 的图像变成 $\mathbb{R}^{784}$ 中的一个向量。数还是那些数，但这种写法丢失了一项信息：哪些像素彼此相邻。紧挨在某个像素下方的像素，在长向量中要往后数 $28$ 个位置。对于逐个给每个特征加权的计算，这无关紧要。对于想要利用邻域关系的计算，矩阵形式更为自然。
:::

### 方阵与对角矩阵

<span class="anker" id="stufe-6-2"></span>

有些矩阵出现得非常频繁，因此有了专门的名称。在这三种情况下，表格的形状都特别简单。

行数与列数相同的矩阵称为__方阵__。方阵的元素 $a_{11},a_{22},\dots,a_{nn}$ 构成它的__对角线__，从左上角延伸到右下角。

:::definition 定义 6.2 (对角矩阵、零矩阵)
<span class="anker" id="satz-6-2"></span>

对角线以外的元素全为零的方阵称为__对角矩阵__。对向量 $\mathbf{v}\in\mathbb{R}^n$，$\operatorname{diag}(\mathbf{v})$ 表示对角元素为 $v_1,\dots,v_n$ 的对角矩阵。

元素全为零的矩阵称为__零矩阵__，记作 $\mathbf 0$。
:::

⁠**算例：**

$$\operatorname{diag}\bigl((2,\ 0.5)^{\top}\bigr)=\begin{pmatrix}2&0\\0&0.5\end{pmatrix},\qquad \operatorname{diag}\bigl((1,\,0,\,3)^{\top}\bigr)=\begin{pmatrix}1&0&0\\0&0&0\\0&0&3\end{pmatrix}.$$

第二个矩阵有一个对角元素为零，但仍是对角矩阵；唯一的要求是对角线以外的元素全为零。$\operatorname{diag}\bigl((2,\ 0.5)^{\top}\bigr)$ 可以简写为 $\operatorname{diag}(2,\,0.5)$。

⁠**简而言之：**方阵的行数与列数相同；对角矩阵只在对角线上有非零元素。

### 数据矩阵

<span class="anker" id="stufe-6-3"></span>

第 [1.2](vektoren-daten-als-zahlenlisten.html#stufe-1-2) 小节中的公寓表格就是一个矩阵：四行，每套公寓一行；三列，每个特征一列。这种排列方式，即每行一个样本，是数据集的标准形式（图 [27](#abb-27)）。

:::abbildung ml/k1datenmatrix 27
公寓数据集的数据矩阵 $\mathbf{X}$。每一行是一个样本，即写成一行的向量 $\mathbf{x}_i^{\top}$（蓝色：公寓 2）。每一列是一个特征在所有样本上的特征列（橙色：各套公寓的面积）。元素 $x_{21}=40$ 同时属于两者。
:::

:::definition 定义 6.3 (数据矩阵)
<span class="anker" id="satz-6-3"></span>

对样本为 $\mathbf{x}_1,\dots,\mathbf{x}_N\in\mathbb{R}^d$ 的数据集，__数据矩阵__是矩阵 $\mathbf{X}\in\mathbb{R}^{N\times d}$，它的第 $i$ 行是写成一行的样本 $\mathbf{x}_i$：

<span class="anker" id="gl-6-1"></span>
$$\mathbf{X}=\begin{pmatrix}\mathbf{x}_1^{\top}\\\mathbf{x}_2^{\top}\\\vdots\\\mathbf{x}_N^{\top}\end{pmatrix}=\begin{pmatrix}x_{11}&\cdots&x_{1d}\\\vdots&&\vdots\\x_{N1}&\cdots&x_{Nd}\end{pmatrix}. \tag{6.1}$$
:::

元素 $x_{ij}$ 是样本 $i$ 的特征 $j$ 的值，与第 [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3) 小节中的约定完全一致。$\mathbf{X}$ 的第 $j$ 列就是第 [4.3](abstande-und-einheiten.html#stufe-4-3) 小节中特征 $j$ 的特征列：该特征在所有样本上的全部取值。所以行对应样本，列对应特征。样本均值 $\bar{\mathbf{x}}$ 的第 $j$ 个分量是第 $j$ 列的均值。

⁠**算例：**对公寓数据集，

$$\mathbf{X}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\in\mathbb{R}^{4\times3}.$$

元素 $x_{32}=4$ 是公寓 3 的房间数，第一列 $(60,\,40,\,90,\,70)^{\top}$ 包含所有面积，它的均值 $65$ 是 $\bar{\mathbf{x}}=(65,\ 2.5,\ 3)^{\top}$ 的第一个分量。

⁠**简而言之：**数据矩阵 $\mathbf{X}\in\mathbb{R}^{N\times d}$ 每行包含一个样本，每列包含一个特征。

:::hintergrund 样本作为行还是作为列？
本系列把样本写成行，就像在电子表格以及当今大多数教材和软件库中那样。有些文献反过来，把样本作为列并排放置；这时它们的数据矩阵是 $d\times N$ 型的。字母也不统一：样本数常记作 $m$，特征数记作 $n$，第 $i$ 个样本写作 $\mathbf{x}^{(i)}$，编号写在右上角的括号里。内容并没有变化。所以阅读别人的文献时，先要弄清楚那里什么是行、什么是列。
:::

:::aufgabe 练习 15 ★ 读取和建立矩阵
<span class="anker" id="aufg-15"></span>

<ol class="al">

<li>

$\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ 是什么型的？给出 $b_{13}$、$b_{21}$ 以及 $\mathbf{B}$ 的第三列。

</li>

<li>

建立第 [5.4](winkel-und-ahnlichkeit.html#stufe-5-4) 小节中三篇文本的数据矩阵。$N$、$d$ 和元素 $x_{23}$ 分别表示什么？

</li>

<li>

一幅 $4\times4$ 像素的灰度图像显示一个亮的“L”：第一列和最下面一行是亮的（$1$），其余都是暗的（$0$）。写出这个矩阵，并把它逐行读出成一个向量。这个向量有多少个分量？

</li>

</ol>

:::loesung
(a) $\mathbf{B}$ 的型为 $2\times3$。$b_{13}=2$（第 1 行、第 3 列），$b_{21}=2$（第 2 行、第 1 列）；第三列为 $(2,\,0)^{\top}$。

(b) $\mathbf{X}=\Bigl(\begin{smallmatrix}3&2&0\\6&4&0\\0&1&3\end{smallmatrix}\Bigr)$，有 $N=3$ 篇文本和 $d=3$ 个词。元素 $x_{23}=0$ 表示：第三个词“选举”没有出现在第二篇文本中。

(c) 这个矩阵的各行为 $(1,0,0,0)$、$(1,0,0,0)$、$(1,0,0,0)$ 和 $(1,1,1,1)$。逐行读出，得到向量

$$(1,0,0,0,\ 1,0,0,0,\ 1,0,0,0,\ 1,1,1,1)^{\top}\in\mathbb{R}^{16}$$

它共有 $4\cdot4=16$ 个分量。
:::
:::
