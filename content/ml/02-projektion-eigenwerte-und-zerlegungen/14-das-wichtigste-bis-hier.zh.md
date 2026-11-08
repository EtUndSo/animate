---
title: 本章要点
pfad: 计算机科学 / 机器学习 / 数学基础 / 投影、特征值与矩阵分解
knoten: 基础篇 2：投影、特征值与矩阵分解
nachschlagen: ja
order: 15221400
summary: 最近点、自然方向 与矩阵的构件
tags: 
lang: zh
---

:::kern 本章要点
<ul>

<li>

标准正交向量：$\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$；坐标就是点积 $c_i=\mathbf{q}_i^{\top}\mathbf{x}$；正交矩阵保持长度和角度不变。若 $\mathbf{Q}$ 不是方阵，则 $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$。

</li>

<li>

向直线的投影：$\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$；余下的部分垂直于 $\mathbf{a}$，$\hat{\mathbf{y}}$ 是最近点。投影矩阵满足 $\mathbf{P}^2=\mathbf{P}$，正交投影的矩阵还满足 $\mathbf{P}^{\top}=\mathbf{P}$。

</li>

<li>

最佳近似解：残差 $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}$ 垂直于列空间，因此 $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$；解唯一当且仅当各列线性无关。

</li>

<li>

向子空间的投影：$\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{Q}\mathbf{Q}^{\top}$；格拉姆-施密特正交化给出 $\mathbf{A}=\mathbf{Q}\mathbf{R}$，并且 $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$。

</li>

<li>

二次型 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ 只依赖于对称部分；碗形、槽形和鞍形可以通过配方识别。

</li>

<li>

特征值：$\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$，$\det(\mathbf{A}-\lambda\mathbf{I})=0$；迹 $=\sum\lambda_i$，$\det=\prod\lambda_i$；旋转有复数特征值。

</li>

<li>

$\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ 实现解耦，$\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$。对称矩阵：$\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$，其中 $\lambda_i$ 为实数，主轴互相垂直，半轴为 $1/\sqrt{\lambda_i}$。

</li>

<li>

正定 $\Leftrightarrow$ 所有特征值 $>0$ $\Leftrightarrow$ 所有主元 $>0$ $\Leftrightarrow$ 所有顺序主子式 $>0$；$\mathbf{A}^{\top}\mathbf{A}$ 是半正定的；Cholesky 分解 $\mathbf{A}=\mathbf L\mathbf L^{\top}$。

</li>

<li>

每个矩阵都有奇异值分解 $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$：旋转、拉伸、旋转；$d_j^2$ 是 $\mathbf{A}^{\top}\mathbf{A}$ 的特征值，$\lVert\mathbf{A}\rVert_2=d_1$。

</li>

<li>

$\lVert\mathbf{A}\rVert_F^2=\sum_jd_j^2$；$\mathbf{A}_k$ 是秩 $k$ 的最佳逼近，在谱范数下误差为 $d_{k+1}$。

</li>

<li>

$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ 给出最短的最佳近似解；特殊情形为 $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ 和 $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$。

</li>

<li>

$\kappa(\mathbf{A})=d_1/d_n$ 限定了相对误差的放大程度；$1/\kappa$ 是到奇异性的相对距离；$\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2$。

</li>

</ul>
:::

:::merke 三句话的答案
<ol>

<li>

无解的方程组，最好的解法是把右边垂直投影到列空间上：这时残差垂直于所有列，由此得出正规方程，而由勾股定理，没有其他点离得更近。

</li>

<li>

特征向量是矩阵只作拉伸的那些方向；在它们构成的基下，矩阵成为对角矩阵，而对于对称矩阵，它们构成一个直角坐标系，从中可以读出每个二次型的形状。

</li>

<li>

每个矩阵都是按大小排列的秩 $1$ 构件 $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ 之和：前 $k$ 个构件给出秩 $k$ 的最佳逼近，而比值 $d_1/d_n$ 表明数据中的误差能使解失真到什么程度。

</li>

</ol>
:::

**一个原理贯穿所有结果。** 本章中几乎所有内容都源于一个原理：在直角坐标系中，长度的平方按勾股定理分解为彼此独立的部分；而到一条直线、一个平面或一个子空间的最短路径是垂直的那一条。

| 结果 | 来源 |
|---|---|
| 坐标即点积，$\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ | 长度为 $1$ 的互相垂直的坐标轴：交叉项消失（第 [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1) 节） |
| 直线上和子空间中的最近点 | 勾股定理：垂直的余下部分加上子空间内的平移（第 [2](projektion-auf-eine-gerade.html#stufe-2) 节和第 [3](die-beste-naherungslosung.html#stufe-3) 节） |
| 正规方程 | 残差垂直于每一列：$\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$（第 [3](die-beste-naherungslosung.html#stufe-3) 节） |
| 格拉姆-施密特正交化与 QR 分解 | 减去影子，把垂直的余下部分归一化（第 [4](projektion-auf-einen-unterraum.html#stufe-4) 节） |
| 碗形、槽形、鞍形 | 平方和中各系数的符号（第 [5](quadratische-formen.html#stufe-5) 节和第 [8](positiv-definite-matrizen.html#stufe-8) 节） |
| 通过对角化解耦 | 在特征基下，每个坐标各自独立地起作用（第 [7](diagonalisierung-und-spektralsatz.html#stufe-7) 节） |
| 谱定理 | 对称性：在点积中 $\mathbf{A}$ 可以换到另一侧，特征向量的正交补被映射到自身（第 [7](diagonalisierung-und-spektralsatz.html#stufe-7) 节） |
| 每个矩阵的奇异值分解 | 对称矩阵 $\mathbf{A}^{\top}\mathbf{A}$ 的谱定理（第 [9](die-singularwertzerlegung.html#stufe-9) 节） |
| 秩 $k$ 的最佳逼近 | 秩 $k$ 矩阵的零空间与拉伸最强的 $k+1$ 个方向相交（第 [10](naherung-durch-matrizen-von-kleinem-rang.html#stufe-10) 节） |
| 最短的最佳近似解 | 奇异向量坐标下的勾股定理：零空间中的分量只会增加长度（第 [11](die-pseudoinverse.html#stufe-11) 节） |
| 条件数 | 最大拉伸与最小拉伸 $d_1$ 和 $d_n$（第 [12](die-konditionszahl.html#stufe-12) 节） |
