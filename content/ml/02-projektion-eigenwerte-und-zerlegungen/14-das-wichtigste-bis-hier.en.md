---
title: Key points so far
pfad: Computer Science / Machine Learning / Mathematical Foundations / Projection, Eigenvalues and Decompositions
knoten: Foundations 2: Projection, Eigenvalues and Decompositions
nachschlagen: ja
order: 15221400
summary: Nearest points, natural directions and the building blocks of a matrix
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

Orthonormal vectors: $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$; coordinates are dot products $c_i=\mathbf{q}_i^{\top}\mathbf{x}$; orthogonal matrices preserve lengths and angles. If $\mathbf{Q}$ is not square, then $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$.

</li>

<li>

Projection onto a line: $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$; the remainder is perpendicular to $\mathbf{a}$, and $\hat{\mathbf{y}}$ is the closest point. Projection matrices satisfy $\mathbf{P}^2=\mathbf{P}$, orthogonal ones also $\mathbf{P}^{\top}=\mathbf{P}$.

</li>

<li>

Best approximate solution: the residual $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}$ is perpendicular to the column space, hence $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$; unique exactly when the columns are independent.

</li>

<li>

Projection onto a subspace: $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{Q}\mathbf{Q}^{\top}$; Gram–Schmidt yields $\mathbf{A}=\mathbf{Q}\mathbf{R}$, and $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$.

</li>

<li>

Quadratic forms $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ depend only on the symmetric part; bowl, trough and saddle are recognized by completing the square.

</li>

<li>

Eigenvalues: $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$, $\det(\mathbf{A}-\lambda\mathbf{I})=0$; trace $=\sum\lambda_i$, $\det=\prod\lambda_i$; rotations have complex eigenvalues.

</li>

<li>

$\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ decouples, $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$. Symmetric: $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ with real $\lambda_i$ and perpendicular principal axes, semi-axes $1/\sqrt{\lambda_i}$.

</li>

<li>

Positive definite $\Leftrightarrow$ all eigenvalues $>0$ $\Leftrightarrow$ all pivots $>0$ $\Leftrightarrow$ all leading principal minors $>0$; $\mathbf{A}^{\top}\mathbf{A}$ is positive semidefinite; Cholesky $\mathbf{A}=\mathbf L\mathbf L^{\top}$.

</li>

<li>

Singular value decomposition $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$ for every matrix: rotate, stretch, rotate; the $d_j^2$ are the eigenvalues of $\mathbf{A}^{\top}\mathbf{A}$, $\lVert\mathbf{A}\rVert_2=d_1$.

</li>

<li>

$\lVert\mathbf{A}\rVert_F^2=\sum_jd_j^2$; $\mathbf{A}_k$ is the best approximation of rank $k$, with the error $d_{k+1}$ in the spectral norm.

</li>

<li>

$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ delivers the shortest best approximate solution; special cases $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ and $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$.

</li>

<li>

$\kappa(\mathbf{A})=d_1/d_n$ bounds the amplification of relative errors; $1/\kappa$ is the relative distance to singularity; $\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2$.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

A system of equations without a solution is best solved by projecting the right-hand side perpendicularly onto the column space: the residual is then perpendicular to all columns, the normal equations follow from this, and by Pythagoras no other point is closer.

</li>

<li>

Eigenvectors are the directions that a matrix only stretches; in their basis the matrix becomes diagonal, and for symmetric matrices they form a set of perpendicular axes from which you read off the shape of every quadratic form.

</li>

<li>

Every matrix is a sum, ordered by size, of building blocks $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ of rank $1$: the first $k$ give the best approximation of rank $k$, and the ratio $d_1/d_n$ tells how strongly errors in the data can distort the solution.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from one principle: in a set of perpendicular axes, a squared length splits into independent parts by Pythagoras, and the shortest path to a line, a plane or a subspace is the perpendicular one.

| Result | Where it comes from |
|---|---|
| Coordinates as dot products, $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$ | perpendicular axes of length $1$: cross terms drop out (Section [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1)) |
| Closest point on a line and in a subspace | Pythagoras: perpendicular remainder plus shift within the subspace (Sections [2](projektion-auf-eine-gerade.html#stufe-2) and [3](die-beste-naherungslosung.html#stufe-3)) |
| Normal equations | residual perpendicular to every column: $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ (Section [3](die-beste-naherungslosung.html#stufe-3)) |
| Gram–Schmidt and QR | subtract the shadow, normalize the perpendicular remainder (Section [4](projektion-auf-einen-unterraum.html#stufe-4)) |
| Bowl, trough, saddle | signs of the factors of a sum of squares (Sections [5](quadratische-formen.html#stufe-5) and [8](positiv-definite-matrizen.html#stufe-8)) |
| Decoupling by diagonalization | in the eigenbasis, each coordinate behaves independently (Section [7](diagonalisierung-und-spektralsatz.html#stufe-7)) |
| Spectral theorem | symmetry: $\mathbf{A}$ may switch sides in the dot product, and the complement of an eigenvector is mapped into itself (Section [7](diagonalisierung-und-spektralsatz.html#stufe-7)) |
| Singular value decomposition of every matrix | spectral theorem for the symmetric matrix $\mathbf{A}^{\top}\mathbf{A}$ (Section [9](die-singularwertzerlegung.html#stufe-9)) |
| Best approximation of rank $k$ | the null space of a matrix of rank $k$ meets the $k+1$ most strongly stretched directions (Section [10](naherung-durch-matrizen-von-kleinem-rang.html#stufe-10)) |
| Shortest best approximate solution | Pythagoras in the coordinates of the singular vectors: parts in the null space only add length (Section [11](die-pseudoinverse.html#stufe-11)) |
| Condition number | largest and smallest stretch $d_1$ and $d_n$ (Section [12](die-konditionszahl.html#stufe-12)) |
