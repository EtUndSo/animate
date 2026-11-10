---
title: Key points so far
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Chapter 1: Vectors and Matrices
nachschlagen: ja
order: 15211700
summary: Data as lists of numbers, models as linear maps
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

An example with $d$ features is a column vector $\mathbf{x}\in\mathbb{R}^d$; a dataset of $N$ examples is the data matrix $\mathbf{X}\in\mathbb{R}^{N\times d}$ with one example per row.

</li>

<li>

The dot product $\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$ is a weighted sum and a comparison with a pattern; the weighted sum $\mathbf{w}^{\top}\mathbf{x}$ is the most general linear rule with one output.

</li>

<li>

Norms measure size: $\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}$, $\lVert\mathbf{x}\rVert_1=\sum_j|x_j|$, $\lVert\mathbf{x}\rVert_\infty=\max_j|x_j|$; the RMS value is $\lVert\mathbf{x}\rVert/\sqrt n$. Distances $\lVert\mathbf{u}-\mathbf{v}\rVert$ depend on the units; standardizing makes them independent of the units.

</li>

<li>

$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$; the angle is given by $\cos\varphi=\mathbf{u}^{\top}\mathbf{v}/(\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert)$; orthogonal means $\mathbf{u}^{\top}\mathbf{v}=0$.

</li>

<li>

$\mathbf{A}\mathbf{x}$ is a list of dot products (row view) and a linear combination of the columns (column view); $\mathbf{X}\mathbf{w}$ gives all predictions at once.

</li>

<li>

Every linear map is a matrix whose columns are the images of the unit vectors; affine means $\mathbf{A}\mathbf{x}+\mathbf{b}$.

</li>

<li>

$\mathbf{A}\mathbf{B}$ is “first $\mathbf{B}$, then $\mathbf{A}$”; associative, not commutative; linear stages in series are a single matrix.

</li>

<li>

$(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$; $\mathbf{X}\mathbf{X}^{\top}$ contains all dot products of the examples, $\mathbf{X}^{\top}\mathbf{X}=\sum_i\mathbf{x}_i\mathbf{x}_i^{\top}$ those of the features.

</li>

<li>

$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$; $\mathbf{A}\mathbf{x}=\mathbf{y}$ has no solution, one or infinitely many, and it is solvable exactly when $\mathbf{y}$ lies in the column space.

</li>

<li>

$\dim\ker\mathbf{A}+\operatorname{rank}\mathbf{A}=n$; $\mathbf{A}\mathbf{x}=\mathbf{y}$ is solvable exactly when $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rank}\mathbf{A}$, and the solution is then unique exactly when $\operatorname{rank}\mathbf{A}=n$; dependent features lower the rank and make the weights ambiguous.

</li>

<li>

$\det\mathbf{A}$ is the signed volume factor, $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$, and $\mathbf{A}$ is invertible exactly when $\det\mathbf{A}\ne0$.

</li>

<li>

$\odot$ multiplies entry by entry; tensors are arrays of numbers with any number of axes.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

A dataset is a matrix whose rows contain the examples as vectors, and similarity, distance and size are dot products and norms of these vectors, which depend on the chosen units.

</li>

<li>

A linear rule is determined by the images of the unit vectors and is therefore a matrix, and the matrix–vector product applies it to all examples at once.

</li>

<li>

Composition is multiplication of the matrices, and whether a map can be reversed is decided by rank, null space and determinant: they show whether directions are lost along the way.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from two operations: vectors are added and multiplied by numbers, and linear maps preserve exactly these two operations.

| Result | Where it comes from |
|---|---|
| Weighted sum, comparison with a pattern | dot product: products in the same position, added up (Section [2](das-skalarprodukt.html#stufe-2)) |
| Length, distance, angle | all from the dot product: $\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$, [(4.1)](abstande-und-einheiten.html#gl-4-1), Cauchy–Schwarz (Sections [3](normen-die-groe-eines-vektors.html#stufe-3) to [5](winkel-und-ahnlichkeit.html#stufe-5)) |
| Distances depend on the units | each feature enters with its squared numerical value (Section [4](abstande-und-einheiten.html#stufe-4)) |
| Row view and column view | the same double sum, ordered differently (Section [7](das-matrix-vektor-produkt.html#stufe-7)) |
| Matrix of a linear map | $\mathbf{x}=\sum_jx_j\mathbf{e}_j$, and the map preserves linear combinations (Section [8](lineare-abbildungen.html#stufe-8)) |
| Matrix product, not commutative | matrix of the composition (Section [9](das-matrixprodukt.html#stufe-9)) |
| Gram matrix | table of the dot products, $\mathbf{X}\mathbf{X}^{\top}$ and $\mathbf{X}^{\top}\mathbf{X}$ (Section [10](transponierte-symmetrie-und-gram-matrix.html#stufe-10)) |
| No inverse if $\mathbf{A}\mathbf{x}=\mathbf{0}$, $\mathbf{x}\ne\mathbf{0}$ | two inputs, one output: information is lost (Section [11](einheitsmatrix-und-inverse.html#stufe-11)) |
| No solution, one, infinitely many | with two solutions, the whole line through them consists of solutions (Section [12](lineare-gleichungssysteme.html#stufe-12)) |
| Ambiguous weights | vectors in the null space do not change $\mathbf{X}\mathbf{w}$ (Section [13](unabhangigkeit-basis-und-rang.html#stufe-13)) |
| $\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\det\mathbf{B}$ | volume factors multiply under composition (Section [14](die-determinante.html#stufe-14)) |
