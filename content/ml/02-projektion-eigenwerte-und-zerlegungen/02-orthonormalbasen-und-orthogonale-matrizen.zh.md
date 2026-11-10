---
title: 标准正交基与正交矩阵
pfad: 计算机科学 / 机器学习 / 数学基础 / 投影、特征值与矩阵分解
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: 第 2 章：投影、特征值与矩阵分解
nachschlagen: ja
order: 15220200
summary: 有些坐标系用起来特别方便：它们的坐标轴两两垂直，每根轴上的单位长度都相同。在这样的坐标系中，求一个点的坐标不需要解方程组，长度直接由勾股定理得出。本节介绍这类坐标系及其对应的矩阵。
tags: 标准正交, 标准正交基, 正交矩阵
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
有些坐标系用起来特别方便：它们的坐标轴两两垂直，每根轴上的单位长度都相同。在这样的坐标系中，求一个点的坐标不需要解方程组，长度直接由勾股定理得出。本节介绍这类坐标系及其对应的矩阵。
:::

### 标准正交向量

<span class="anker" id="stufe-1-1"></span>

在[第 1 章第 5.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-3)中，若两个向量的点积为零，就称它们正交。恒定模式 $(1,1,1,1)^{\top}$ 和交替模式 $(1,-1,1,-1)^{\top}$ 就是一个例子：把时间序列与其中一个模式比较时，不会受到另一个模式的干扰。不过，比较得到的是该成分的 $4$ 倍，因为两个模式的长度都是 $2$。如果正交向量的长度还都是 $1$，这个因子也就消失了。

设想把平面的两根坐标轴 $\mathbf{e}_1$ 和 $\mathbf{e}_2$ 整体转过某个角度。这两个箭头的长度仍然是 $1$，仍然互相垂直，只是指向了别的方向。

:::definition 定义 1.1 (标准正交)
<span class="anker" id="satz-1-1"></span>

若向量 $\mathbf{q}_1,\dots,\mathbf{q}_k\in\mathbb{R}^n$ 的长度都是 $1$，且任意两个不同的向量都正交，则称它们是__标准正交__的：

<span class="anker" id="gl-1-1"></span>
$$\mathbf{q}_i^{\top}\mathbf{q}_l=\begin{cases}1, & i=l,\\ 0, & i\ne l.\end{cases} \tag{1.1}$$
:::

术语“标准正交”由“标准化”（长度为一）和“正交”组合而成。单位向量 $\mathbf{e}_1,\dots,\mathbf{e}_n$ 是最简单的例子。

:::satz 定理 1.2 (标准正交向量线性无关)
<span class="anker" id="satz-1-2"></span>

若 $\mathbf{q}_1,\dots,\mathbf{q}_k$ 标准正交，则它们线性无关。
:::

:::beweis 线性无关性
设 $c_1\mathbf{q}_1+\dots+c_k\mathbf{q}_k=\mathbf{0}$。两边同时与 $\mathbf{q}_l$ 作点积。由式 [(1.1)](#gl-1-1)，左边只剩下 $c_l\,\mathbf{q}_l^{\top}\mathbf{q}_l=c_l$ 这一项；右边为 $\mathbf{q}_l^{\top}\mathbf{0}=0$。所以 $c_l=0$，而且这对每个 $l$ 都成立。按照[第 1 章第 13.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-2)的定义，这些向量因此线性无关。
:::

::::beispiel [算例]
对于 $\mathbf{q}_1=(0.6,\ 0.8)^{\top}$ 和 $\mathbf{q}_2=(-0.8,\ 0.6)^{\top}$，有

$$\mathbf{q}_1^{\top}\mathbf{q}_1=0.36+0.64=1,\qquad \mathbf{q}_2^{\top}\mathbf{q}_2=0.64+0.36=1,\qquad \mathbf{q}_1^{\top}\mathbf{q}_2=-0.48+0.48=0 .$$

这两个向量是标准正交的；图 [1](#abb-1) 逐步演示了最后一个点积。恒定模式和交替模式除以各自的长度 $2$ 后就成为标准正交的：$\tfrac12(1,1,1,1)^{\top}$ 和 $\tfrac12(1,-1,1,-1)^{\top}$。

:::abbildung ml/k2rorth 1
逐步计算点积 $\mathbf{q}_1^{\top}\mathbf{q}_2$，其中 $0.6=\tfrac35$，$0.8=\tfrac45$：先将对应分量相乘，再求和。
:::
::::

⁠**简而言之：**标准正交向量长度为 $1$ 且两两垂直；它们总是线性无关的。

### 标准正交基

<span class="anker" id="stufe-1-2"></span>

根据[第 1 章第 13.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3)，基就是一个坐标系：每个向量在其中都有唯一的表示。最方便的基是由标准正交向量组成的基。它们就像我们熟悉的坐标轴，只是转了一个角度。

:::definition 定义 1.3 (标准正交基)
<span class="anker" id="satz-1-3"></span>

由标准正交向量组成的基称为__标准正交基__。
:::

对整个 $\mathbb{R}^n$ 而言，只要找到 $n$ 个标准正交向量就够了。由上一小节的定理，它们线性无关。把它们写成一个 $n\times n$ 矩阵的列，这个矩阵的秩为 $n$，由[第 1 章第 13.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5)，它的列空间就是整个 $\mathbb{R}^n$。因此这 $n$ 个向量张成 $\mathbb{R}^n$，构成一组基。同样，也可以为一个张成的空间（比如 $\mathbb{R}^3$ 中的一个平面）寻找标准正交基，也就是一组标准正交向量，它们张成的空间恰好就是给定的那个。

::::beispiel [算例]
向量 $\mathbf{q}_1=(0.6,\ 0.8)^{\top}$ 和 $\mathbf{q}_2=(-0.8,\ 0.6)^{\top}$ 是 $\mathbb{R}^2$ 中的两个标准正交向量，因此构成 $\mathbb{R}^2$ 的一组标准正交基。单位向量 $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ 构成 $\mathbb{R}^3$ 的一组标准正交基，称为标准基。$\mathbb{R}^3$ 中的平面 $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ 有标准正交基 $\mathbf{e}_1,\mathbf{e}_2$。
::::

⁠**简而言之：**标准正交基就是转过一个角度的坐标轴：$\mathbb{R}^n$ 中的 $n$ 个标准正交向量总是构成一组基。

### 标准正交基下的坐标

<span class="anker" id="stufe-1-3"></span>

在一般的基下，要求出一个向量的坐标，必须解一个方程组。在[第 1 章第 13.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3)中，$(3,\,2)^{\top}$ 在基 $(1,\,0)^{\top}$、$(1,\,1)^{\top}$ 下的坐标是 $1$ 和 $2$。而点积 $(1,0)(3,2)^{\top}=3$ 和 $(1,1)(3,2)^{\top}=5$ 则完全是另一回事。与此不同，在标准正交基下，坐标恰好就是点积。

原因可以从[第 1 章第 5.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5)中影子长度的图景看出。对于归一化向量 $\mathbf{q}$，数 $\mathbf{q}^{\top}\mathbf{x}$ 是 $\mathbf{x}$ 在沿 $\mathbf{q}$ 方向的直线上的影子长度。在标准正交基下，每个坐标都是在各自坐标轴上的影子（图 [2](#abb-2)）。

:::abbildung ml/k2onb 2
标准正交基 $\mathbf{q}_1=(0.6,\,0.8)^{\top}$、$\mathbf{q}_2=(-0.8,\,0.6)^{\top}$（绿色）下的坐标。箭头 $\mathbf{x}=(3,1)^{\top}$ 在两根转过的坐标轴（灰色）上各投下一个影子，光线都是垂直照射的（虚线）。影子长度 $\mathbf{q}_1^{\top}\mathbf{x}=2.6$（蓝色）和 $\mathbf{q}_2^{\top}\mathbf{x}=-1.8$（橙色）就是坐标：$\mathbf{x}=2.6\,\mathbf{q}_1-1.8\,\mathbf{q}_2$。
:::

:::satz 定理 1.4 (标准正交基下的坐标)
<span class="anker" id="satz-1-4"></span>

若 $\mathbf{q}_1,\dots,\mathbf{q}_n$ 是 $\mathbb{R}^n$ 的一组标准正交基，则对每个向量 $\mathbf{x}\in\mathbb{R}^n$ 有

<span class="anker" id="gl-1-2"></span>
$$\mathbf{x}=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})\,\mathbf{q}_i\qquad\text{以及}\qquad \lVert\mathbf{x}\rVert^2=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})^2 . \tag{1.2}$$
:::

:::beweis 标准正交基下的坐标
因为这些向量构成一组基，所以存在数 $c_1,\dots,c_n$，使 $\mathbf{x}=\sum_ic_i\mathbf{q}_i$。由式 [(1.1)](#gl-1-1)，与 $\mathbf{q}_l$ 作点积得

$$\mathbf{q}_l^{\top}\mathbf{x}=\sum_{i=1}^nc_i\,\mathbf{q}_l^{\top}\mathbf{q}_i=c_l ,$$

因为只有 $i=l$ 的那一项不为零。对于长度，把乘积展开：

$$\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^nc_i\,c_l\,\mathbf{q}_i^{\top}\mathbf{q}_l=\sum_{i=1}^nc_i^2 ,$$

同样是因为只剩下 $i=l$ 的各项。
:::

第二个公式就是 $\mathbb{R}^n$ 中的勾股定理：只要每根轴上的单位长度都是 $1$，在任何一组互相垂直的坐标轴下，由坐标算出的箭头长度都相同。

::::beispiel [算例]
对于 $\mathbf{x}=(3,\,1)^{\top}$ 和上一小节的基，有

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=1.8+0.8=2.6,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=-2.4+0.6=-1.8 .$$

验算：$2.6\,(0.6,\ 0.8)^{\top}-1.8\,(-0.8,\ 0.6)^{\top}=(1.56+1.44,\ 2.08-1.08)^{\top}=(3,\,1)^{\top}$。并且 $c_1^2+c_2^2=6.76+3.24=10=\lVert\mathbf{x}\rVert^2$。图 [3](#abb-3) 用分数给出了这三个和。

:::abbildung ml/k2rkoord 3
把 $\mathbf{x}$ 的坐标 $c_1=\tfrac{13}5=2.6$ 和 $c_2=-\tfrac95=-1.8$ 作为点积计算，以及它们的平方和，即 $\mathbf{x}$ 长度的平方。
:::
::::

⁠**简而言之：**在标准正交基下，每个坐标都是一个点积 $c_i=\mathbf{q}_i^{\top}\mathbf{x}$，坐标的平方和就是长度的平方。

:::hintergrund 振荡构成标准正交基，以及帕塞瓦尔定理
四个向量

$$\begin{gathered} \mathbf{q}_1=\tfrac12(1,\,1,\,1,\,1)^{\top},\qquad \mathbf{q}_2=\tfrac1{\sqrt2}(1,\,0,\,-1,\,0)^{\top},\\ \mathbf{q}_3=\tfrac1{\sqrt2}(0,\,1,\,0,\,-1)^{\top},\qquad \mathbf{q}_4=\tfrac12(1,\,-1,\,1,\,-1)^{\top} \end{gathered}$$

分别是一个常数、每四步一个周期的余弦振荡和正弦振荡，以及每一步都变号的振荡的取值，并且都已归一化。容易验证它们是标准正交的，因此构成 $\mathbb{R}^4$ 的一组标准正交基。每个由四个值组成的时间序列，例如一天中四个时刻的气温，都是这四个振荡之和，由式 [(1.2)](#gl-1-2)，各部分的贡献就是点积。对于时间序列 $\mathbf{x}=(4,\,2,\,0,\,2)^{\top}$，得到 $\mathbf{q}_1^{\top}\mathbf{x}=4$，$\mathbf{q}_2^{\top}\mathbf{x}=4/\sqrt2=2\sqrt2$，$\mathbf{q}_3^{\top}\mathbf{x}=0$，$\mathbf{q}_4^{\top}\mathbf{x}=0$：该时间序列只由一个常数和一个余弦组成。

式 [(1.2)](#gl-1-2) 中的第二个公式表明，时间序列的平方和 $\lVert\mathbf{x}\rVert^2=24$ 等于各贡献的平方和 $16+8+0+0=24$。在数学中，这一结论称为帕塞瓦尔定理。离散傅里叶变换是用复振荡做的同一种分解；例如，音乐软件就是用它把一个声音分解成各个音。对 $N$ 个值，它的矩阵只有在用 $1/\sqrt N$ 归一化时才保持长度不变；没有这个因子，帕塞瓦尔定理中就会多出一个因子 $N$。
:::

### 正交矩阵

<span class="anker" id="stufe-1-4"></span>

把标准正交基的向量写成矩阵 $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$ 的列，式 [(1.2)](#gl-1-2) 中的两个公式都可以写成矩阵乘积。按照[第 1 章第 7.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-2)的行视角，所有坐标合起来构成向量 $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$，因为 $\mathbf{Q}^{\top}$ 的各行就是向量 $\mathbf{q}_i^{\top}$。反过来，按列视角有 $\mathbf{x}=\sum_ic_i\mathbf{q}_i=\mathbf{Q}\mathbf{c}$。所以矩阵 $\mathbf{Q}^{\top}$ 撤销了 $\mathbf{Q}$ 的作用。

:::definition 定义 1.5 (正交矩阵)
<span class="anker" id="satz-1-5"></span>

列向量标准正交的方阵 $\mathbf{Q}\in\mathbb{R}^{n\times n}$ 称为__正交矩阵__。等价地：$\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$。
:::

两种表述等价，因为 $\mathbf{Q}^{\top}\mathbf{Q}$ 的元素 $(i,l)$ 就是第 $i$ 列与第 $l$ 列的点积 $\mathbf{q}_i^{\top}\mathbf{q}_l$。所以条件 $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ 恰好就是式 [(1.1)](#gl-1-1)。

:::satz 定理 1.6 (正交矩阵的逆)
<span class="anker" id="satz-1-6"></span>

若 $\mathbf{Q}$ 是正交矩阵，则 $\mathbf{Q}$ 可逆，且 $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$。此外 $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$；因此 $\mathbf{Q}$ 的各行也是标准正交的，$\mathbf{Q}^{\top}$ 同样是正交矩阵。
:::

:::beweis 正交矩阵的逆
各列标准正交，由第一小节，它们线性无关。由[第 1 章第 13.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5)的定理，$\mathbf{Q}$ 因而可逆。将 $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ 从右边乘以 $\mathbf{Q}^{-1}$，得到 $\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$，从而也有 $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{Q}\mathbf{Q}^{-1}=\mathbf{I}$。
:::

关于名称说明一句。正交矩阵的列是标准正交的，而不仅仅是正交的；这个名称是历史沿袭下来的。对于列只是正交而未归一化的矩阵，并没有专门的名称。对这样的矩阵，$\mathbf{Q}^{\top}\mathbf{Q}$ 是一个对角矩阵，对角线上是各列长度的平方，但不是 $\mathbf{I}$。

::::beispiel [算例]
以第一小节中的向量为列，

$$\mathbf{Q}=\begin{pmatrix}0.6&-0.8\\0.8&0.6\end{pmatrix},\qquad \mathbf{Q}^{\top}\mathbf{Q}=\begin{pmatrix}0.36+0.64&-0.48+0.48\\-0.48+0.48&0.64+0.36\end{pmatrix}=\mathbf{I} .$$

$\mathbf{Q}^{\top}\mathbf{Q}$ 的元素就是第一小节中各列的点积；图 [1](#abb-1) 给出了非对角元素。所以无需任何计算即得 $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$。这个矩阵就是[第 1 章第 8.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3)中 $\cos\alpha=0.6$、$\sin\alpha=0.8$ 的旋转矩阵，即逆时针旋转 $\alpha\approx53.13^\circ$。逆矩阵 $\mathbf{Q}^{\top}$ 以同样的角度转回去。
::::

⁠**简而言之：**正交矩阵是列向量标准正交的方阵；它的逆矩阵就是它的转置。

### 长度和角度保持不变

<span class="anker" id="stufe-1-5"></span>

旋转既不改变箭头的长度，也不改变两个箭头之间的夹角。所有正交矩阵都具有这一性质，这也是人们如此喜欢用它们计算的原因。

:::satz 定理 1.7 (正交矩阵保持点积不变)
<span class="anker" id="satz-1-7"></span>

若 $\mathbf{Q}$ 是正交矩阵，则对所有 $\mathbf{x},\mathbf{y}\in\mathbb{R}^n$ 有

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{y},\qquad \lVert\mathbf{Q}\mathbf{x}\rVert=\lVert\mathbf{x}\rVert , \tag{1.3}$$

并且 $\mathbf{Q}\mathbf{x}$ 与 $\mathbf{Q}\mathbf{y}$ 之间的夹角等于 $\mathbf{x}$ 与 $\mathbf{y}$ 之间的夹角。行列式 $\det\mathbf{Q}=1$ 或 $\det\mathbf{Q}=-1$。
:::

:::beweis 点积保持不变
由[第 1 章第 10.1 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1)的规则 $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$，有 $(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{y}=\mathbf{x}^{\top}\mathbf{I}\mathbf{y}=\mathbf{x}^{\top}\mathbf{y}$。令 $\mathbf{y}=\mathbf{x}$ 即得关于长度的结论；由于夹角只由点积和长度算出，它也保持不变。对于行列式，利用[第 1 章第 14.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5)的规则：$1=\det\mathbf{I}=\det(\mathbf{Q}^{\top}\mathbf{Q})=\det\mathbf{Q}^{\top}\cdot\det\mathbf{Q}=(\det\mathbf{Q})^2$。
:::

因此，正交矩阵像移动刚体一样移动空间，不使它变形。若 $\det\mathbf{Q}=1$，它是一个旋转。若 $\det\mathbf{Q}=-1$，它包含一次反射，因为由[第 1 章第 14.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-2)，负的行列式会使定向反转。

::::beispiel [算例]
上一小节的旋转把 $\mathbf{x}=(3,\,1)^{\top}$ 映射为 $\mathbf{Q}\mathbf{x}=(1.8-0.8,\ 2.4+0.6)^{\top}=(1,\,3)^{\top}$。两个向量长度的平方都是 $10$。该旋转的行列式为 $0.36+0.64=1$。矩阵 $\bigl(\begin{smallmatrix}0.6&0.8\\0.8&-0.6\end{smallmatrix}\bigr)$ 的列同样标准正交，但行列式为 $-0.36-0.64=-1$：它关于沿 $(2,\,1)^{\top}$ 方向的直线作反射，因为它把 $(2,\,1)^{\top}$ 映射为自身，把 $(-1,\,2)^{\top}$ 映射为 $(1,\,-2)^{\top}$。
::::

⁠**简而言之：**正交矩阵保持点积、长度和角度不变；它们作旋转或反射，行列式为 $\pm1$。

:::hintergrund 为什么数值分析学家喜欢用正交矩阵计算
计算机用舍入后的数计算，所以每个中间结果都带有一个小误差 $\boldsymbol{\delta}$。把这样的中间结果乘以一个矩阵时，误差也随之乘以该矩阵。一般的矩阵可能在此过程中放大误差；正交矩阵则不会，因为由式 [(1.3)](#gl-1-3)，$\lVert\mathbf{Q}\boldsymbol{\delta}\rVert=\lVert\boldsymbol{\delta}\rVert$。因此，只由正交矩阵乘法构成的计算不会让舍入误差增长。出于同样的原因，求逆也不成问题：不必计算逆矩阵，转置就够了，而且转置是精确的。
:::

### 列向量标准正交的矩阵

<span class="anker" id="stufe-1-6"></span>

标准正交向量的个数常常少于空间的维数。$\mathbb{R}^3$ 中的平面有一组由两个向量组成的标准正交基。把它们写成矩阵的列，得到的矩阵不是方阵，而是三行两列。有些规则可以照搬，有些则不行，而这种差别很重要。

:::satz 定理 1.8 (列向量标准正交的矩形矩阵)
<span class="anker" id="satz-1-8"></span>

若 $\mathbf{Q}\in\mathbb{R}^{n\times k}$ 的列标准正交且 $k<n$，则 $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_k$，并且对每个 $\mathbf{c}\in\mathbb{R}^k$ 有 $\lVert\mathbf{Q}\mathbf{c}\rVert=\lVert\mathbf{c}\rVert$。而矩阵 $\mathbf{Q}\mathbf{Q}^{\top}\in\mathbb{R}^{n\times n}$ 不是单位矩阵。
:::

:::beweis 矩形矩阵
前两个结论与方阵的情形完全一样，由式 [(1.1)](#gl-1-1) 得出。关于第三个结论：矩阵 $\mathbf{Q}^{\top}$ 有 $k$ 行 $n$ 列。由[第 1 章第 13.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5)的秩-零化度定理，它的零空间的维数为 $n-\operatorname{rank}\mathbf{Q}^{\top}\ge n-k\ge1$。所以存在向量 $\mathbf{z}\ne\mathbf{0}$ 使 $\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}$，对它有 $\mathbf{Q}\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}\ne\mathbf{z}$。因此 $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$。
:::

::::beispiel [算例 1]
只有一列 $\mathbf{q}=(0.6,\ 0.8)^{\top}$ 的矩阵满足 $\mathbf{q}^{\top}\mathbf{q}=1$，但

$$\mathbf{q}\mathbf{q}^{\top}=\begin{pmatrix}0.36&0.48\\0.48&0.64\end{pmatrix}\ne\mathbf{I} .$$

它把 $(-0.8,\ 0.6)^{\top}$ 映射为 $\mathbf{0}$，把向量 $\mathbf{x}=(3,\,1)^{\top}$ 映射为 $(1.08+0.48,\ 1.44+0.64)^{\top}=(1.56,\ 2.08)^{\top}$。这恰好是[第 1 章第 5.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5)中 $\mathbf{x}$ 的影子的端点，因为 $\mathbf{q}\mathbf{q}^{\top}\mathbf{x}=\mathbf{q}\,(\mathbf{q}^{\top}\mathbf{x})=2.6\,\mathbf{q}$。
::::

::::beispiel [算例 2]
$\mathbf{Q}=\Bigl(\begin{smallmatrix}1&0\\0&1\\0&0\end{smallmatrix}\Bigr)$ 的列是 $\mathbb{R}^3$ 中的 $\mathbf{e}_1$ 和 $\mathbf{e}_2$。有 $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_2$，但 $\mathbf{Q}\mathbf{Q}^{\top}=\operatorname{diag}(1,\,1,\,0)$。这个矩阵保留前两个分量，把第三个分量置为零。
::::

⁠**简而言之：**对于列向量标准正交的矩形矩阵，$\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$，但 $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$：按这个顺序相乘会丢掉向量的一部分。

:::aufgabe 练习 1 ★ 标准正交性与坐标
<span class="anker" id="aufg-1"></span>

设 $\mathbf{q}_1=\tfrac13(1,\,2,\,2)^{\top}$，$\mathbf{q}_2=\tfrac13(2,\,1,\,-2)^{\top}$，$\mathbf{q}_3=\tfrac13(2,\,-2,\,1)^{\top}$。

<ol class="al">

<li>

验证这三个向量是标准正交的。

</li>

<li>

求 $\mathbf{x}=(3,\,0,\,3)^{\top}$ 在这组标准正交基下的坐标，并验算结果。验证 $\lVert\mathbf{x}\rVert^2$ 的公式。

</li>

</ol>

:::loesung
(a) 计算全部六个点积；公因子 $\tfrac13\cdot\tfrac13=\tfrac19$ 提到前面：

$$\mathbf{q}_1^{\top}\mathbf{q}_1=\tfrac19(1+4+4)=1,\quad \mathbf{q}_2^{\top}\mathbf{q}_2=\tfrac19(4+1+4)=1,\quad \mathbf{q}_3^{\top}\mathbf{q}_3=\tfrac19(4+4+1)=1,$$

$$\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac19(2+2-4)=0,\quad \mathbf{q}_1^{\top}\mathbf{q}_3=\tfrac19(2-4+2)=0,\quad \mathbf{q}_2^{\top}\mathbf{q}_3=\tfrac19(4-2-2)=0 .$$

三个向量的长度都是 $1$，并且两两垂直：它们是标准正交的，因而由第 [1.2](#stufe-1-2) 节，它们构成 $\mathbb{R}^3$ 的一组标准正交基。

(b) 由式 [(1.2)](#gl-1-2)，坐标就是点积，无需解方程组：

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=\tfrac13(3+0+6)=3,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=\tfrac13(6+0-6)=0,\qquad c_3=\mathbf{q}_3^{\top}\mathbf{x}=\tfrac13(6+0+3)=3 .$$

验算：$3\mathbf{q}_1+0\cdot\mathbf{q}_2+3\mathbf{q}_3=(1,\,2,\,2)^{\top}+(2,\,-2,\,1)^{\top}=(3,\,0,\,3)^{\top}=\mathbf{x}$。长度公式：$c_1^2+c_2^2+c_3^2=9+0+9=18$，而 $\lVert\mathbf{x}\rVert^2=9+0+9=18$。
:::
:::

:::aufgabe 练习 2 ★ 一个正交矩阵
<span class="anker" id="aufg-2"></span>

设 $\mathbf{Q}$ 是以练习 [1](#aufg-1) 中的 $\mathbf{q}_1,\mathbf{q}_2,\mathbf{q}_3$ 为列的矩阵。

<ol class="al">

<li>

不经计算写出 $\mathbf{Q}^{-1}$。任选一个非对角元素验证 $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$。

</li>

<li>

计算 $\mathbf{Q}\,(1,\,1,\,1)^{\top}$ 并比较长度。计算 $\det\mathbf{Q}$。$\mathbf{Q}$ 是旋转还是反射？

</li>

</ol>

:::loesung
(a) 各列标准正交，所以 $\mathbf{Q}$ 是正交矩阵，无需计算即得 $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$。这里的

$$\mathbf{Q}=\frac13\begin{pmatrix}1&2&2\\2&1&-2\\2&-2&1\end{pmatrix}$$

甚至是对称的，所以 $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}=\mathbf{Q}$。$\mathbf{Q}\mathbf{Q}^{\top}$ 的元素 $(1,2)$ 是第一行与第二行的点积：$\tfrac19(1\cdot2+2\cdot1+2\cdot(-2))=0$。

(b) $\mathbf{Q}\,(1,\,1,\,1)^{\top}=\tfrac13(5,\,1,\,1)^{\top}$，其长度的平方为 $\tfrac19(25+1+1)=3$，恰好等于 $(1,\,1,\,1)^{\top}$ 的长度的平方，正如式 [(1.3)](#gl-1-3) 所要求的。行列式为

$$\det\mathbf{Q}=\tfrac1{27}\bigl(1\cdot(1-4)-2\cdot(2+4)+2\cdot(-4-2)\bigr)=\tfrac1{27}(-3-12-12)=-1 .$$

所以 $\mathbf{Q}$ 是反射。更确切地说：由于 $\mathbf{Q}=\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$，有 $\mathbf{Q}^2=\mathbf{I}$；作用两次，一切都回到原处。向量 $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ 被翻转，$\mathbf{Q}\mathbf{k}=\tfrac13(1-2-2,\ 2-1+2,\ 2+2-1)^{\top}=(-1,\,1,\,1)^{\top}=-\mathbf{k}$，而垂直于 $\mathbf{k}$ 的向量保持不动。$\mathbf{Q}$ 是关于平面 $x_1-x_2-x_3=0$ 的反射。
:::
:::

:::aufgabe 练习 3 ★★ 用正交矩阵计算
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

证明：若 $\mathbf{Q}_1$ 和 $\mathbf{Q}_2$ 是正交矩阵，则 $\mathbf{Q}_1\mathbf{Q}_2$ 也是正交矩阵。

</li>

<li>

两个正交矩阵之和仍是正交矩阵吗？说明理由或给出反例。

</li>

<li>

证明：对角矩阵是正交矩阵，当且仅当每个对角元素都是 $1$ 或 $-1$。这样的矩阵在几何上做了什么？

</li>

</ol>

:::loesung
(a) 利用 $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$，得 $(\mathbf{Q}_1\mathbf{Q}_2)^{\top}(\mathbf{Q}_1\mathbf{Q}_2)=\mathbf{Q}_2^{\top}\mathbf{Q}_1^{\top}\mathbf{Q}_1\mathbf{Q}_2=\mathbf{Q}_2^{\top}\mathbf{I}\mathbf{Q}_2=\mathbf{I}$。直观地说：两个刚体运动先后进行，仍是一个刚体运动。

(b) 不是。反例：$\mathbf{I}+\mathbf{I}=2\mathbf{I}$，而 $(2\mathbf{I})^{\top}(2\mathbf{I})=4\mathbf{I}\ne\mathbf{I}$；这个和把所有长度都变为原来的两倍。同样，$\mathbf{I}+(-\mathbf{I})$ 是零矩阵。

(c) 对于 $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$，有 $\mathbf{D}^{\top}\mathbf{D}=\operatorname{diag}(d_1^2,\dots,d_n^2)$。它等于 $\mathbf{I}$，当且仅当每个 $d_i^2=1$，即 $d_i=1$ 或 $d_i=-1$。这样的矩阵把 $d_i=-1$ 的那些坐标轴反向，其余坐标轴保持不变：它关于坐标平面作反射。例如，$\operatorname{diag}(1,\,-1)$ 是关于 $x_1$ 轴的反射，而 $\operatorname{diag}(-1,\,-1)$ 是旋转 $180^\circ$。
:::
:::
