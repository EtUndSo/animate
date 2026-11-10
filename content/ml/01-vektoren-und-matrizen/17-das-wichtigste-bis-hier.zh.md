---
title: 本章要点
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: 第 1 章：向量与矩阵
nachschlagen: ja
order: 15211700
summary: 数据即数字列表， 模型即线性映射
tags: 
lang: zh
---

:::kern 本章要点
<ul>

<li>

有 $d$ 个特征的样本是列向量 $\mathbf{x}\in\mathbb{R}^d$；由 $N$ 个样本组成的数据集是数据矩阵 $\mathbf{X}\in\mathbb{R}^{N\times d}$，每行一个样本。

</li>

<li>

点积 $\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$ 是加权和，也是与一个模式的比对；加权和 $\mathbf{w}^{\top}\mathbf{x}$ 是只有一个输出的最一般的线性规则。

</li>

<li>

范数衡量大小：$\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}$，$\lVert\mathbf{x}\rVert_1=\sum_j|x_j|$，$\lVert\mathbf{x}\rVert_\infty=\max_j|x_j|$；均方根值为 $\lVert\mathbf{x}\rVert/\sqrt n$。距离 $\lVert\mathbf{u}-\mathbf{v}\rVert$ 取决于单位；标准化使距离与单位无关。

</li>

<li>

$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$；夹角由 $\cos\varphi=\mathbf{u}^{\top}\mathbf{v}/(\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert)$ 给出；正交意味着 $\mathbf{u}^{\top}\mathbf{v}=0$。

</li>

<li>

$\mathbf{A}\mathbf{x}$ 是一串点积（行视角），也是各列的线性组合（列视角）；$\mathbf{X}\mathbf{w}$ 一次给出所有预测值。

</li>

<li>

每个线性映射都是一个矩阵，它的各列是单位向量的像；仿射意味着 $\mathbf{A}\mathbf{x}+\mathbf{b}$。

</li>

<li>

$\mathbf{A}\mathbf{B}$ 是“先 $\mathbf{B}$，后 $\mathbf{A}$”；矩阵乘积满足结合律，但不满足交换律；串联的线性级就是单个矩阵。

</li>

<li>

$(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$；$\mathbf{X}\mathbf{X}^{\top}$ 包含样本之间的所有点积，$\mathbf{X}^{\top}\mathbf{X}=\sum_i\mathbf{x}_i\mathbf{x}_i^{\top}$ 包含特征之间的所有点积。

</li>

<li>

$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$；$\mathbf{A}\mathbf{x}=\mathbf{y}$ 无解、恰有一个解或有无穷多解，并且当且仅当 $\mathbf{y}$ 位于列空间中时可解。

</li>

<li>

$\dim\ker\mathbf{A}+\operatorname{rank}\mathbf{A}=n$；$\mathbf{A}\mathbf{x}=\mathbf{y}$ 可解，当且仅当 $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rank}\mathbf{A}$，此时解唯一，当且仅当 $\operatorname{rank}\mathbf{A}=n$；线性相关的特征使秩降低，并使权重不唯一。

</li>

<li>

$\det\mathbf{A}$ 是带符号的体积因子，$\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$，而 $\mathbf{A}$ 可逆当且仅当 $\det\mathbf{A}\ne0$。

</li>

<li>

$\odot$ 逐个元素相乘；张量是有任意多根轴的数阵。

</li>

</ul>
:::

:::merke 三句话的答案
<ol>

<li>

数据集是一个矩阵，它的各行以向量形式包含各个样本；相似度、距离和大小就是这些向量的点积和范数，它们取决于所选的单位。

</li>

<li>

线性规则由单位向量的像确定，因而就是一个矩阵；矩阵-向量乘积把它一次用于所有样本。

</li>

<li>

复合就是矩阵相乘；映射能否逆转，由秩、零空间和行列式决定：它们说明在映射过程中是否有方向丢失。

</li>

</ol>
:::

**一个原理贯穿所有结果。** 本章中几乎所有内容都源于两种运算：向量可以相加，也可以乘以数；而线性映射恰好保持这两种运算。

| 结果 | 来源 |
|---|---|
| 加权和，与模式比对 | 点积：同一位置上的乘积相加（第 [2](das-skalarprodukt.html#stufe-2) 节） |
| 长度、距离、夹角 | 全部来自点积：$\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$，式 [(4.1)](abstande-und-einheiten.html#gl-4-1)，柯西-施瓦茨不等式（第 [3](normen-die-groe-eines-vektors.html#stufe-3) 节至第 [5](winkel-und-ahnlichkeit.html#stufe-5) 节） |
| 距离取决于单位 | 每个特征以其数值的平方计入（第 [4](abstande-und-einheiten.html#stufe-4) 节） |
| 行视角与列视角 | 同一个双重求和，按不同顺序排列（第 [7](das-matrix-vektor-produkt.html#stufe-7) 节） |
| 线性映射的矩阵 | $\mathbf{x}=\sum_jx_j\mathbf{e}_j$，而映射保持线性组合（第 [8](lineare-abbildungen.html#stufe-8) 节） |
| 矩阵乘积，不可交换 | 复合的矩阵（第 [9](das-matrixprodukt.html#stufe-9) 节） |
| 格拉姆矩阵 | 点积构成的表格，$\mathbf{X}\mathbf{X}^{\top}$ 和 $\mathbf{X}^{\top}\mathbf{X}$（第 [10](transponierte-symmetrie-und-gram-matrix.html#stufe-10) 节） |
| $\mathbf{A}\mathbf{x}=\mathbf{0}$，$\mathbf{x}\ne\mathbf{0}$ 时没有逆矩阵 | 两个输入，一个输出：信息丢失了（第 [11](einheitsmatrix-und-inverse.html#stufe-11) 节） |
| 无解、唯一解、无穷多解 | 有两个解时，过它们的整条直线都由解组成（第 [12](lineare-gleichungssysteme.html#stufe-12) 节） |
| 权重不唯一 | 零空间中的向量不改变 $\mathbf{X}\mathbf{w}$（第 [13](unabhangigkeit-basis-und-rang.html#stufe-13) 节） |
| $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$ | 复合时体积因子相乘（第 [14](die-determinante.html#stufe-14) 节） |
