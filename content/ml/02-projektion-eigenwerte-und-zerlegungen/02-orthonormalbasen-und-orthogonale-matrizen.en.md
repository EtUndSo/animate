---
title: Orthonormal bases and orthogonal matrices
pfad: Computer Science / Machine Learning / Projection, Eigenvalues and Decompositions
order: 6220200
summary: Some coordinate systems are especially convenient: their axes are perpendicular to one another, and the unit has the same length on every axis.
tags: orthonormal, orthonormal basis, orthogonal matrix
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Some coordinate systems are especially convenient: their axes are perpendicular to one another, and the unit has the same length on every axis. In such a system you need no system of equations to find the coordinates of a point, and lengths follow from the Pythagorean theorem. This section introduces such coordinate systems and the matrices that belong to them.
:::

### Orthonormal vectors

<span class="anker" id="stufe-1-1"></span>

In Part 1, Section 5.3, two vectors were called orthogonal if their dot product is zero. The constant pattern $(1,1,1,1)^{\top}$ and the alternating pattern $(1,-1,1,-1)^{\top}$ were an example: comparing a signal with one pattern was not disturbed by the other pattern. The comparison did, however, return the share multiplied by $4$, because both patterns have length $2$. If orthogonal vectors also have length $1$, this factor disappears as well.

Picture the two axes $\mathbf{e}_1$ and $\mathbf{e}_2$ of the plane, rotated as a whole by some angle. The two arrows still have length $1$ and are still perpendicular to each other; they just point in other directions.

:::definition Definition 1.1 (Orthonormal)
<span class="anker" id="satz-1-1"></span>

Vectors $\mathbf{q}_1,\dots,\mathbf{q}_k\in\mathbb{R}^n$ are called __orthonormal__ if each of them has length $1$ and any two different ones are orthogonal:

<span class="anker" id="gl-1-1"></span>
$$\mathbf{q}_i^{\top}\mathbf{q}_l=\begin{cases}1, & i=l,\\ 0, & i\ne l.\end{cases} \tag{1.1}$$
:::

The word combines “orthogonal” and “normalized”. The unit vectors $\mathbf{e}_1,\dots,\mathbf{e}_n$ are the simplest example.

:::satz Theorem 1.2 (Orthonormal vectors are linearly independent)
<span class="anker" id="satz-1-2"></span>

If $\mathbf{q}_1,\dots,\mathbf{q}_k$ are orthonormal, then they are linearly independent.
:::

:::beweis Linear independence
Let $c_1\mathbf{q}_1+\dots+c_k\mathbf{q}_k=\mathbf{0}$. Take the dot product of both sides with $\mathbf{q}_l$. By [(1.1)](#gl-1-1), only the term $c_l\,\mathbf{q}_l^{\top}\mathbf{q}_l=c_l$ remains on the left; the right side is $\mathbf{q}_l^{\top}\mathbf{0}=0$. So $c_l=0$, and this holds for every $l$. By the definition in Part 1, Section 13.2, the vectors are therefore linearly independent.
:::

⁠**Worked example:** For $\mathbf{q}_1=(0.6,\ 0.8)^{\top}$ and $\mathbf{q}_2=(-0.8,\ 0.6)^{\top}$,

$$\mathbf{q}_1^{\top}\mathbf{q}_1=0.36+0.64=1,\qquad \mathbf{q}_2^{\top}\mathbf{q}_2=0.64+0.36=1,\qquad \mathbf{q}_1^{\top}\mathbf{q}_2=-0.48+0.48=0 .$$

The two vectors are orthonormal; Fig. [1](#abb-1) shows the last dot product step by step. The constant and the alternating pattern become orthonormal when you divide them by their length $2$: $\tfrac12(1,1,1,1)^{\top}$ and $\tfrac12(1,-1,1,-1)^{\top}$.

:::abbildung ml/k2rorth 1
The dot product $\mathbf{q}_1^{\top}\mathbf{q}_2$ step by step, with $0.6=\tfrac35$ and $0.8=\tfrac45$: component times component, then the sum.
:::

⁠**In short:** Orthonormal vectors have length $1$ and are pairwise perpendicular; they are always linearly independent.

### Orthonormal bases

<span class="anker" id="stufe-1-2"></span>

By Part 1, Section 13.3, a basis is a coordinate system: every vector has exactly one representation in it. The most convenient bases are those whose vectors are orthonormal. They are like the familiar set of axes, only rotated.

:::definition Definition 1.3 (Orthonormal basis)
<span class="anker" id="satz-1-3"></span>

A basis of orthonormal vectors is called an __orthonormal basis__.
:::

For all of $\mathbb{R}^n$ it is enough to find $n$ orthonormal vectors. By the theorem in the previous subsection they are linearly independent. If you write them as the columns of an $n\times n$ matrix, this matrix has rank $n$, and by Part 1, Section 13.5, its column space is all of $\mathbb{R}^n$. So the $n$ vectors span $\mathbb{R}^n$ and form a basis. In the same way you can look for an orthonormal basis of a span, say a plane in $\mathbb{R}^3$: orthonormal vectors whose span is exactly the given one.

⁠**Worked example:** The vectors $\mathbf{q}_1=(0.6,\ 0.8)^{\top}$ and $\mathbf{q}_2=(-0.8,\ 0.6)^{\top}$ are two orthonormal vectors in $\mathbb{R}^2$, hence an orthonormal basis of $\mathbb{R}^2$. The unit vectors $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ form the orthonormal basis of $\mathbb{R}^3$ that is called the standard basis. The plane $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ in $\mathbb{R}^3$ has the orthonormal basis $\mathbf{e}_1,\mathbf{e}_2$.

⁠**In short:** An orthonormal basis is a rotated set of axes: $n$ orthonormal vectors in $\mathbb{R}^n$ always form a basis.

### Coordinates in an orthonormal basis

<span class="anker" id="stufe-1-3"></span>

In an ordinary basis you have to solve a system of equations to find the coordinates of a vector. In Part 1, Section 13.3, $(3,\,2)^{\top}$ had the coordinates $1$ and $2$ in the basis $(1,\,0)^{\top}$, $(1,\,1)^{\top}$. The dot products $(1,0)(3,2)^{\top}=3$ and $(1,1)(3,2)^{\top}=5$ are something entirely different. In an orthonormal basis, by contrast, the coordinates are exactly the dot products.

The reason is shown by the picture of the shadow length from Part 1, Section 5.5. For a normalized vector $\mathbf{q}$, the number $\mathbf{q}^{\top}\mathbf{x}$ is the length of the shadow of $\mathbf{x}$ on the line in the direction of $\mathbf{q}$. In an orthonormal basis, every coordinate is the shadow on its own axis (Fig. [2](#abb-2)).

:::abbildung ml/k2onb 2
Coordinates in the orthonormal basis $\mathbf{q}_1=(0.6,\,0.8)^{\top}$, $\mathbf{q}_2=(-0.8,\,0.6)^{\top}$ (green). The arrow $\mathbf{x}=(3,1)^{\top}$ casts a shadow onto each of the two rotated axes (gray); in each case the light falls perpendicularly (dashed). The shadow lengths $\mathbf{q}_1^{\top}\mathbf{x}=2.6$ (blue) and $\mathbf{q}_2^{\top}\mathbf{x}=-1.8$ (orange) are the coordinates: $\mathbf{x}=2.6\,\mathbf{q}_1-1.8\,\mathbf{q}_2$.
:::

:::satz Theorem 1.4 (Coordinates in an orthonormal basis)
<span class="anker" id="satz-1-4"></span>

If $\mathbf{q}_1,\dots,\mathbf{q}_n$ is an orthonormal basis of $\mathbb{R}^n$, then for every vector $\mathbf{x}\in\mathbb{R}^n$

<span class="anker" id="gl-1-2"></span>
$$\mathbf{x}=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})\,\mathbf{q}_i\qquad\text{and}\qquad \lVert\mathbf{x}\rVert^2=\sum_{i=1}^n(\mathbf{q}_i^{\top}\mathbf{x})^2 . \tag{1.2}$$
:::

:::beweis Coordinates in an orthonormal basis
Because the vectors form a basis, there are numbers $c_1,\dots,c_n$ with $\mathbf{x}=\sum_ic_i\mathbf{q}_i$. By [(1.1)](#gl-1-1), the dot product with $\mathbf{q}_l$ gives

$$\mathbf{q}_l^{\top}\mathbf{x}=\sum_{i=1}^nc_i\,\mathbf{q}_l^{\top}\mathbf{q}_i=c_l ,$$

since only the term with $i=l$ is nonzero. For the length, multiply out:

$$\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^nc_i\,c_l\,\mathbf{q}_i^{\top}\mathbf{q}_l=\sum_{i=1}^nc_i^2 ,$$

again because only the terms with $i=l$ remain.
:::

The second formula is the Pythagorean theorem in $\mathbb{R}^n$: the length of an arrow comes out the same from its coordinates in every set of perpendicular axes, as long as the unit has length $1$ on all axes.

⁠**Worked example:** For $\mathbf{x}=(3,\,1)^{\top}$ and the basis from the previous subsection,

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=1.8+0.8=2.6,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=-2.4+0.6=-1.8 .$$

Check: $2.6\,(0.6,\ 0.8)^{\top}-1.8\,(-0.8,\ 0.6)^{\top}=(1.56+1.44,\ 2.08-1.08)^{\top}=(3,\,1)^{\top}$. And $c_1^2+c_2^2=6.76+3.24=10=\lVert\mathbf{x}\rVert^2$. Fig. [3](#abb-3) shows the three sums with fractions.

:::abbildung ml/k2rkoord 3
The coordinates $c_1=\tfrac{13}5=2.6$ and $c_2=-\tfrac95=-1.8$ of $\mathbf{x}$ as dot products, and the sum of their squares, which is the squared length of $\mathbf{x}$.
:::

⁠**In short:** In an orthonormal basis, every coordinate is a dot product, $c_i=\mathbf{q}_i^{\top}\mathbf{x}$, and the sum of the squared coordinates is the squared length.

:::hintergrund Sampled oscillations as an orthonormal basis, and Parseval's theorem
The four vectors

$$\begin{gathered} \mathbf{q}_1=\tfrac12(1,\,1,\,1,\,1)^{\top},\qquad \mathbf{q}_2=\tfrac1{\sqrt2}(1,\,0,\,-1,\,0)^{\top},\\ \mathbf{q}_3=\tfrac1{\sqrt2}(0,\,1,\,0,\,-1)^{\top},\qquad \mathbf{q}_4=\tfrac12(1,\,-1,\,1,\,-1)^{\top} \end{gathered}$$

are the samples of a DC component, of a cosine and a sine oscillation with one period in four samples, and of an oscillation that changes sign at every sample, each normalized. It is easy to check that they are orthonormal. So they form an orthonormal basis of $\mathbb{R}^4$. Every signal with four samples is a sum of these four oscillations, and by [(1.2)](#gl-1-2) the contributions are simply dot products. For the signal $\mathbf{x}=(4,\,2,\,0,\,2)^{\top}$ we get $\mathbf{q}_1^{\top}\mathbf{x}=4$, $\mathbf{q}_2^{\top}\mathbf{x}=4/\sqrt2=2\sqrt2$, $\mathbf{q}_3^{\top}\mathbf{x}=0$ and $\mathbf{q}_4^{\top}\mathbf{x}=0$: the signal consists only of the DC component and the cosine.

The second formula in [(1.2)](#gl-1-2) says that the energy $\lVert\mathbf{x}\rVert^2=24$ of the signal equals the sum of the squared contributions, $16+8+0+0=24$. In signal processing this statement is called Parseval's theorem. The discrete Fourier transform is the same decomposition with complex oscillations. Its matrix for $N$ samples preserves lengths exactly when it is normalized by $1/\sqrt N$; without this factor, Parseval's theorem contains an additional factor $N$.
:::

### Orthogonal matrices

<span class="anker" id="stufe-1-4"></span>

If you write the vectors of an orthonormal basis as the columns of a matrix $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$, both formulas [(1.2)](#gl-1-2) can be written as matrix products. By the row view from Part 1, Section 7.2, all coordinates at once form the vector $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$, because the rows of $\mathbf{Q}^{\top}$ are the vectors $\mathbf{q}_i^{\top}$. Conversely, $\mathbf{x}=\sum_ic_i\mathbf{q}_i=\mathbf{Q}\mathbf{c}$ by the column view. So the matrix $\mathbf{Q}^{\top}$ undoes what $\mathbf{Q}$ does.

:::definition Definition 1.5 (Orthogonal matrix)
<span class="anker" id="satz-1-5"></span>

A square matrix $\mathbf{Q}\in\mathbb{R}^{n\times n}$ whose columns are orthonormal is called an __orthogonal matrix__. Equivalently: $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$.
:::

The two formulations are equivalent because the entry $(i,l)$ of $\mathbf{Q}^{\top}\mathbf{Q}$ is the dot product $\mathbf{q}_i^{\top}\mathbf{q}_l$ of columns $i$ and $l$. So the condition $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ is exactly [(1.1)](#gl-1-1).

:::satz Theorem 1.6 (The inverse of an orthogonal matrix)
<span class="anker" id="satz-1-6"></span>

If $\mathbf{Q}$ is orthogonal, then $\mathbf{Q}$ is invertible with $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$. Moreover, $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$; so the rows of $\mathbf{Q}$ are orthonormal too, and $\mathbf{Q}^{\top}$ is orthogonal as well.
:::

:::beweis Inverse of an orthogonal matrix
The columns are orthonormal, so by the first subsection they are linearly independent. By the theorem in Part 1, Section 13.5, $\mathbf{Q}$ is therefore invertible. Multiplying $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ from the right by $\mathbf{Q}^{-1}$ gives $\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$, and hence also $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{Q}\mathbf{Q}^{-1}=\mathbf{I}$.
:::

A word about the name. An orthogonal matrix has orthonormal columns, not merely orthogonal ones; the name has grown historically. There is no special name for matrices whose columns are only orthogonal but not normalized. For them, $\mathbf{Q}^{\top}\mathbf{Q}$ is a diagonal matrix with the squared lengths of the columns on the diagonal, but not $\mathbf{I}$.

⁠**Worked example:** With the vectors from the first subsection as columns,

$$\mathbf{Q}=\begin{pmatrix}0.6&-0.8\\0.8&0.6\end{pmatrix},\qquad \mathbf{Q}^{\top}\mathbf{Q}=\begin{pmatrix}0.36+0.64&-0.48+0.48\\-0.48+0.48&0.64+0.36\end{pmatrix}=\mathbf{I} .$$

The entries of $\mathbf{Q}^{\top}\mathbf{Q}$ are the dot products of the columns from the first subsection; Fig. [1](#abb-1) shows the off-diagonal entry. So $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, without any calculation. This matrix is the rotation matrix from Part 1, Section 8.3, with $\cos\alpha=0.6$ and $\sin\alpha=0.8$, that is, a counterclockwise rotation by $\alpha\approx53.13^\circ$. The inverse $\mathbf{Q}^{\top}$ rotates back by the same angle.

⁠**In short:** An orthogonal matrix is square with orthonormal columns; its inverse is simply its transpose.

### Lengths and angles are preserved

<span class="anker" id="stufe-1-5"></span>

A rotation changes neither the length of an arrow nor the angle between two arrows. All orthogonal matrices have this property, and it is the reason why people like to compute with them so much.

:::satz Theorem 1.7 (Orthogonal matrices preserve dot products)
<span class="anker" id="satz-1-7"></span>

If $\mathbf{Q}$ is orthogonal, then for all $\mathbf{x},\mathbf{y}\in\mathbb{R}^n$

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{y},\qquad \lVert\mathbf{Q}\mathbf{x}\rVert=\lVert\mathbf{x}\rVert , \tag{1.3}$$

and the angle between $\mathbf{Q}\mathbf{x}$ and $\mathbf{Q}\mathbf{y}$ is the same as the angle between $\mathbf{x}$ and $\mathbf{y}$. The determinant is $\det\mathbf{Q}=1$ or $\det\mathbf{Q}=-1$.
:::

:::beweis Preservation of dot products
By the rule $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ from Part 1, Section 10.1, $(\mathbf{Q}\mathbf{x})^{\top}(\mathbf{Q}\mathbf{y})=\mathbf{x}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{y}=\mathbf{x}^{\top}\mathbf{I}\mathbf{y}=\mathbf{x}^{\top}\mathbf{y}$. With $\mathbf{y}=\mathbf{x}$ the statement about the length follows, and because the angle is computed only from dot products and lengths, it stays the same too. For the determinant, use the rules from Part 1, Section 14.5: $1=\det\mathbf{I}=\det(\mathbf{Q}^{\top}\mathbf{Q})=\det\mathbf{Q}^{\top}\cdot\det\mathbf{Q}=(\det\mathbf{Q})^2$.
:::

So an orthogonal matrix moves space rigidly, without distorting it. If $\det\mathbf{Q}=1$, it is a rotation. If $\det\mathbf{Q}=-1$, it contains a reflection, because by Part 1, Section 14.2, a negative determinant reverses the orientation.

⁠**Worked example:** The rotation from the previous subsection maps $\mathbf{x}=(3,\,1)^{\top}$ to $\mathbf{Q}\mathbf{x}=(1.8-0.8,\ 2.4+0.6)^{\top}=(1,\,3)^{\top}$. Both vectors have the squared length $10$. The determinant of the rotation is $0.36+0.64=1$. The matrix $\bigl(\begin{smallmatrix}0.6&0.8\\0.8&-0.6\end{smallmatrix}\bigr)$ also has orthonormal columns, but the determinant $-0.36-0.64=-1$: it reflects across the line in the direction of $(2,\,1)^{\top}$, because it maps $(2,\,1)^{\top}$ to itself and $(-1,\,2)^{\top}$ to $(1,\,-2)^{\top}$.

⁠**In short:** Orthogonal matrices preserve dot products, lengths and angles; they rotate or reflect, and their determinant is $\pm1$.

:::hintergrund Why numerical analysts like to compute with orthogonal matrices
A computer works with rounded numbers, so every intermediate result carries a small error $\boldsymbol{\delta}$. When you multiply such an intermediate result by a matrix, the error is multiplied by it as well. An arbitrary matrix can enlarge the error in the process; an orthogonal one cannot, because by [(1.3)](#gl-1-3) $\lVert\mathbf{Q}\boldsymbol{\delta}\rVert=\lVert\boldsymbol{\delta}\rVert$. Computations that consist only of multiplications by orthogonal matrices therefore do not let rounding errors grow. For the same reason, the inverse is no problem: you do not have to compute it, the transpose suffices, and it is exact.
:::

### Matrices with orthonormal columns

<span class="anker" id="stufe-1-6"></span>

Often you have fewer orthonormal vectors than the space has dimensions. A plane in $\mathbb{R}^3$ has an orthonormal basis of two vectors. If you write them as the columns of a matrix, it is not square but has three rows and two columns. Some of the rules carry over, some do not, and the difference matters.

:::satz Theorem 1.8 (Rectangular matrices with orthonormal columns)
<span class="anker" id="satz-1-8"></span>

If $\mathbf{Q}\in\mathbb{R}^{n\times k}$ has orthonormal columns and $k<n$, then $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_k$ and $\lVert\mathbf{Q}\mathbf{c}\rVert=\lVert\mathbf{c}\rVert$ for every $\mathbf{c}\in\mathbb{R}^k$. The matrix $\mathbf{Q}\mathbf{Q}^{\top}\in\mathbb{R}^{n\times n}$, on the other hand, is not the identity matrix.
:::

:::beweis Rectangular matrices
The first two statements follow from [(1.1)](#gl-1-1) exactly as for square matrices. For the third: the matrix $\mathbf{Q}^{\top}$ has $k$ rows and $n$ columns. By the rank–nullity theorem from Part 1, Section 13.5, its null space has dimension $n-\operatorname{rank}\mathbf{Q}^{\top}\ge n-k\ge1$. So there is a vector $\mathbf{z}\ne\mathbf{0}$ with $\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}$, and for it $\mathbf{Q}\mathbf{Q}^{\top}\mathbf{z}=\mathbf{0}\ne\mathbf{z}$. Hence $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$.
:::

⁠**Worked example 1:** The matrix with the single column $\mathbf{q}=(0.6,\ 0.8)^{\top}$ satisfies $\mathbf{q}^{\top}\mathbf{q}=1$, but

$$\mathbf{q}\mathbf{q}^{\top}=\begin{pmatrix}0.36&0.48\\0.48&0.64\end{pmatrix}\ne\mathbf{I} .$$

It maps $(-0.8,\ 0.6)^{\top}$ to $\mathbf{0}$. It maps the vector $\mathbf{x}=(3,\,1)^{\top}$ to $(1.08+0.48,\ 1.44+0.64)^{\top}=(1.56,\ 2.08)^{\top}$. This is exactly the endpoint of the shadow of $\mathbf{x}$ from Part 1, Section 5.5, because $\mathbf{q}\mathbf{q}^{\top}\mathbf{x}=\mathbf{q}\,(\mathbf{q}^{\top}\mathbf{x})=2.6\,\mathbf{q}$.

⁠**Worked example 2:** The columns of $\mathbf{Q}=\Bigl(\begin{smallmatrix}1&0\\0&1\\0&0\end{smallmatrix}\Bigr)$ are $\mathbf{e}_1$ and $\mathbf{e}_2$ in $\mathbb{R}^3$. We have $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}_2$, but $\mathbf{Q}\mathbf{Q}^{\top}=\operatorname{diag}(1,\,1,\,0)$. This matrix keeps the first two components and sets the third to zero.

⁠**In short:** For a rectangular matrix with orthonormal columns, $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$, but $\mathbf{Q}\mathbf{Q}^{\top}\ne\mathbf{I}$: the product in this order throws away part of the vector.

:::aufgabe Exercise 1 ★ Orthonormality and coordinates
<span class="anker" id="aufg-1"></span>

Let $\mathbf{q}_1=\tfrac13(1,\,2,\,2)^{\top}$, $\mathbf{q}_2=\tfrac13(2,\,1,\,-2)^{\top}$ and $\mathbf{q}_3=\tfrac13(2,\,-2,\,1)^{\top}$.

<ol class="al">

<li>

Check that the three vectors are orthonormal.

</li>

<li>

Compute the coordinates of $\mathbf{x}=(3,\,0,\,3)^{\top}$ in this orthonormal basis and verify the result. Check the formula for $\lVert\mathbf{x}\rVert^2$.

</li>

</ol>

:::loesung
(a) Form all six dot products; the common factor $\tfrac13\cdot\tfrac13=\tfrac19$ is placed in front:

$$\mathbf{q}_1^{\top}\mathbf{q}_1=\tfrac19(1+4+4)=1,\quad \mathbf{q}_2^{\top}\mathbf{q}_2=\tfrac19(4+1+4)=1,\quad \mathbf{q}_3^{\top}\mathbf{q}_3=\tfrac19(4+4+1)=1,$$

$$\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac19(2+2-4)=0,\quad \mathbf{q}_1^{\top}\mathbf{q}_3=\tfrac19(2-4+2)=0,\quad \mathbf{q}_2^{\top}\mathbf{q}_3=\tfrac19(4-2-2)=0 .$$

All three have length $1$ and are pairwise perpendicular: they are orthonormal, and by Section [1.2](#stufe-1-2) they therefore form an orthonormal basis of $\mathbb{R}^3$.

(b) By [(1.2)](#gl-1-2), the coordinates are dot products, with no system of equations:

$$c_1=\mathbf{q}_1^{\top}\mathbf{x}=\tfrac13(3+0+6)=3,\qquad c_2=\mathbf{q}_2^{\top}\mathbf{x}=\tfrac13(6+0-6)=0,\qquad c_3=\mathbf{q}_3^{\top}\mathbf{x}=\tfrac13(6+0+3)=3 .$$

Check: $3\mathbf{q}_1+0\cdot\mathbf{q}_2+3\mathbf{q}_3=(1,\,2,\,2)^{\top}+(2,\,-2,\,1)^{\top}=(3,\,0,\,3)^{\top}=\mathbf{x}$. Length formula: $c_1^2+c_2^2+c_3^2=9+0+9=18$ and $\lVert\mathbf{x}\rVert^2=9+0+9=18$.
:::
:::

:::aufgabe Exercise 2 ★ An orthogonal matrix
<span class="anker" id="aufg-2"></span>

Let $\mathbf{Q}$ be the matrix with the columns $\mathbf{q}_1,\mathbf{q}_2,\mathbf{q}_3$ from Exercise [1](#aufg-1).

<ol class="al">

<li>

Give $\mathbf{Q}^{-1}$ without computing. Check $\mathbf{Q}\mathbf{Q}^{\top}=\mathbf{I}$ for an off-diagonal entry of your choice.

</li>

<li>

Compute $\mathbf{Q}\,(1,\,1,\,1)^{\top}$ and compare the lengths. Compute $\det\mathbf{Q}$. Does $\mathbf{Q}$ rotate or reflect?

</li>

</ol>

:::loesung
(a) The columns are orthonormal, so $\mathbf{Q}$ is orthogonal and $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, without any computation. Here

$$\mathbf{Q}=\frac13\begin{pmatrix}1&2&2\\2&1&-2\\2&-2&1\end{pmatrix}$$

is even symmetric, so $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}=\mathbf{Q}$. The entry $(1,2)$ of $\mathbf{Q}\mathbf{Q}^{\top}$ is the dot product of the first row with the second: $\tfrac19(1\cdot2+2\cdot1+2\cdot(-2))=0$.

(b) $\mathbf{Q}\,(1,\,1,\,1)^{\top}=\tfrac13(5,\,1,\,1)^{\top}$ with the squared length $\tfrac19(25+1+1)=3$, exactly the squared length of $(1,\,1,\,1)^{\top}$, as [(1.3)](#gl-1-3) requires. The determinant is

$$\det\mathbf{Q}=\tfrac1{27}\bigl(1\cdot(1-4)-2\cdot(2+4)+2\cdot(-4-2)\bigr)=\tfrac1{27}(-3-12-12)=-1 .$$

So $\mathbf{Q}$ reflects. More precisely: because $\mathbf{Q}=\mathbf{Q}^{\top}=\mathbf{Q}^{-1}$, we have $\mathbf{Q}^2=\mathbf{I}$; applied twice, it brings everything back. The vector $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ is flipped over, $\mathbf{Q}\mathbf{k}=\tfrac13(1-2-2,\ 2-1+2,\ 2+2-1)^{\top}=(-1,\,1,\,1)^{\top}=-\mathbf{k}$, and the vectors perpendicular to $\mathbf{k}$ stay fixed. $\mathbf{Q}$ is the reflection across the plane $x_1-x_2-x_3=0$.
:::
:::

:::aufgabe Exercise 3 ★★ Computing with orthogonal matrices
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Show: if $\mathbf{Q}_1$ and $\mathbf{Q}_2$ are orthogonal, then $\mathbf{Q}_1\mathbf{Q}_2$ is orthogonal too.

</li>

<li>

Is the sum of two orthogonal matrices orthogonal again? Justify your answer or give a counterexample.

</li>

<li>

Show that a diagonal matrix is orthogonal if and only if every diagonal entry is $1$ or $-1$. What does such a matrix do geometrically?

</li>

</ol>

:::loesung
(a) With $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$, we get $(\mathbf{Q}_1\mathbf{Q}_2)^{\top}(\mathbf{Q}_1\mathbf{Q}_2)=\mathbf{Q}_2^{\top}\mathbf{Q}_1^{\top}\mathbf{Q}_1\mathbf{Q}_2=\mathbf{Q}_2^{\top}\mathbf{I}\mathbf{Q}_2=\mathbf{I}$. Intuitively: two rigid motions in succession are again a rigid motion.

(b) No. Counterexample: $\mathbf{I}+\mathbf{I}=2\mathbf{I}$, and $(2\mathbf{I})^{\top}(2\mathbf{I})=4\mathbf{I}\ne\mathbf{I}$; the sum doubles all lengths. Likewise, $\mathbf{I}+(-\mathbf{I})$ is the zero matrix.

(c) For $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$, we have $\mathbf{D}^{\top}\mathbf{D}=\operatorname{diag}(d_1^2,\dots,d_n^2)$. This is $\mathbf{I}$ if and only if every $d_i^2=1$, that is, $d_i=1$ or $d_i=-1$. Such a matrix reverses the axes with $d_i=-1$ and leaves the others alone: it reflects across the coordinate planes. For example, $\operatorname{diag}(1,\,-1)$ reflects across the $x_1$-axis, and $\operatorname{diag}(-1,\,-1)$ is the rotation by $180^\circ$.
:::
:::
