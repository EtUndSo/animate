---
title: The singular value decomposition
pfad: Computer Science / Machine Learning / Projection, Eigenvalues and Decompositions
order: 6221000
summary: Eigenvectors exist only for square matrices, and they are perpendicular to each other only for symmetric ones.
tags: singular values, right singular vectors, left singular vector, spectral norm
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
Eigenvectors exist only for square matrices, and they are perpendicular to each other only for symmetric ones. This section shows that every matrix, even a rectangular one, has a pair of sets of perpendicular axes: one in the space of the inputs and one in the space of the outputs. The matrix maps each axis of the one onto a multiple of an axis of the other. This yields a decomposition of every matrix into rotation, stretch and rotation.
:::

### Perpendicular directions that stay perpendicular

<span class="anker" id="stufe-9-1"></span>

The matrix $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, being a triangular matrix, has the double eigenvalue $2$, but only one eigendirection: $(\mathbf{A}-2\mathbf{I})\mathbf{v}=\mathbf{0}$ means $3v_2=0$, so only multiples of $\mathbf{e}_1$ come into question (Exercise [19](eigenwerte-und-eigenvektoren.html#aufg-19)). By Section [7.2](diagonalisierung-und-spektralsatz.html#stufe-7-2), it is not diagonalizable. Nevertheless, it turns the unit circle into an ellipse (Fig. [23](#abb-23)), and an ellipse has two perpendicular axes. Which arrows of the circle land on these axes?

What we are looking for is less than an eigenvector: an arrow may change its direction. We are looking for two perpendicular unit vectors $\mathbf{v}_1$, $\mathbf{v}_2$ whose images $\mathbf{A}\mathbf{v}_1$ and $\mathbf{A}\mathbf{v}_2$ are again perpendicular to each other. Their dot product tells whether two images are perpendicular:

$$(\mathbf{A}\mathbf{v}_1)^{\top}(\mathbf{A}\mathbf{v}_2)=\mathbf{v}_1^{\top}\,\mathbf{A}^{\top}\mathbf{A}\,\mathbf{v}_2 .$$

Here the Gram matrix $\mathbf{A}^{\top}\mathbf{A}$ appears. It is symmetric even if $\mathbf{A}$ is not, and by the spectral theorem it has an orthonormal basis of eigenvectors. If $\mathbf{v}_2$ is an eigenvector of $\mathbf{A}^{\top}\mathbf{A}$ for the eigenvalue $\lambda_2$ and $\mathbf{v}_1$ is perpendicular to $\mathbf{v}_2$, then the dot product is $\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$. So the eigenvectors of $\mathbf{A}^{\top}\mathbf{A}$ do what we want. The same calculation with $\mathbf{v}_1=\mathbf{v}_2$ gives the lengths of the images: $\lVert\mathbf{A}\mathbf{v}_i\rVert^2=\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_i=\lambda_i$.

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, we have $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}4&6\\6&13\end{smallmatrix}\bigr)$ with the trace $17$ and the determinant $52-36=16$. The characteristic polynomial $\lambda^2-17\lambda+16=(\lambda-16)(\lambda-1)$ has the roots $16$ and $1$. Normalized eigenvectors are $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$ for $16$ and $\mathbf{v}_2=(-2,\,1)^{\top}/\sqrt5$ for $1$. Their images

$$\mathbf{A}\mathbf{v}_1=\frac1{\sqrt5}\begin{pmatrix}8\\4\end{pmatrix},\qquad \mathbf{A}\mathbf{v}_2=\frac1{\sqrt5}\begin{pmatrix}-1\\2\end{pmatrix}$$

have the dot product $\tfrac15(-8+8)=0$ and the lengths $\sqrt{80/5}=4=\sqrt{16}$ and $1=\sqrt1$ (Fig. [22](#abb-22)).

:::abbildung ml/k2rsvdidee 22
The images $\mathbf{A}\mathbf{v}_1=(8,4)^{\top}/\sqrt5$ and $\mathbf{A}\mathbf{v}_2=(-1,2)^{\top}/\sqrt5$ are perpendicular to each other and have the squared lengths $16$ and $1$, the eigenvalues of $\mathbf{A}^{\top}\mathbf{A}$.
:::

⁠**In short:** The eigenvectors of the symmetric matrix $\mathbf{A}^{\top}\mathbf{A}$ are perpendicular directions whose images under $\mathbf{A}$ are again perpendicular to each other; the images have the lengths $\sqrt{\lambda_i}$.

### Singular values

<span class="anker" id="stufe-9-2"></span>

The lengths of the images are the most important characteristic numbers of a matrix: they tell how strongly the matrix stretches in its principal directions. By Section [8.4](positiv-definite-matrizen.html#stufe-8-4), $\mathbf{A}^{\top}\mathbf{A}$ is positive semidefinite, so its eigenvalues are not negative, and you may take the square root.

:::definition Definition 9.1 (Singular values)
<span class="anker" id="satz-9-1"></span>

Let $\mathbf{A}\in\mathbb{R}^{m\times n}$, and let $\lambda_1\ge\lambda_2\ge\dots\ge\lambda_n\ge0$ be the eigenvalues of $\mathbf{A}^{\top}\mathbf{A}$, sorted in descending order, with multiple ones counted according to their multiplicity. The numbers

<span class="anker" id="gl-9-1"></span>
$$d_j=\sqrt{\lambda_j},\qquad d_1\ge d_2\ge\dots\ge d_n\ge0 , \tag{9.1}$$

are called the __singular values__ of $\mathbf{A}$.
:::

Many books write $\sigma_j$ instead of $d_j$. Here the singular values always carry an index; the $d$ without an index from Part 1, the number of features, is something else.

:::satz Theorem 9.2 (Singular values and rank)
<span class="anker" id="satz-9-2"></span>

The number of singular values that are not zero is the rank of $\mathbf{A}$.
:::

:::beweis Singular values and rank
Let $\mathbf{v}_1,\dots,\mathbf{v}_n$ be orthonormal eigenvectors of $\mathbf{A}^{\top}\mathbf{A}$ for $\lambda_1,\dots,\lambda_n$. Every vector is $\mathbf{x}=\sum_jc_j\mathbf{v}_j$, so $\mathbf{A}\mathbf{x}=\sum_jc_j\,\mathbf{A}\mathbf{v}_j$: the column space is spanned by the images $\mathbf{A}\mathbf{v}_1,\dots,\mathbf{A}\mathbf{v}_n$. By the previous subsection, these are pairwise perpendicular and have the lengths $d_j$. The images with $d_j=0$ are the zero vector and contribute nothing. The others are perpendicular to each other and nonzero; divided by their lengths, they are orthonormal and, by the theorem in Section [1.1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-1), linearly independent. They form a basis of the column space, and their number is the rank.
:::

In what follows, the rank of a matrix is denoted by $r$. We have $d_1\ge\dots\ge d_r>0$ and $d_{r+1}=\dots=d_n=0$.

⁠**Worked example:** $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ has the singular values $d_1=4$ and $d_2=1$ and rank $2$. The eigenvalues are $2$ and $2$: singular values and eigenvalues are in general different numbers. The matrix $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ has $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$ with the eigenvalues $25$ and $0$, hence the singular values $5$ and $0$ and rank $1$.

⁠**In short:** The singular values $d_j$ are the square roots of the eigenvalues of $\mathbf{A}^{\top}\mathbf{A}$; they measure how strongly $\mathbf{A}$ stretches in its principal directions, and the number of positive ones is the rank.

### Singular vectors

<span class="anker" id="stufe-9-3"></span>

Each positive singular value comes with two directions: an input direction $\mathbf{v}_j$ and the direction of its image.

:::definition Definition 9.3 (Singular vectors)
<span class="anker" id="satz-9-3"></span>

Orthonormal eigenvectors $\mathbf{v}_1,\dots,\mathbf{v}_n$ of $\mathbf{A}^{\top}\mathbf{A}$ for the eigenvalues $d_1^2,\dots,d_n^2$ are called __right singular vectors__ of $\mathbf{A}$. For $d_j>0$,

<span class="anker" id="gl-9-2"></span>
$$\mathbf{u}_j=\frac{\mathbf{A}\mathbf{v}_j}{d_j},\qquad\text{so}\qquad \mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j , \tag{9.2}$$

is called the corresponding __left singular vector__.
:::

The names come from the position the vectors occupy in the decomposition of the next subsection. The left singular vectors are again orthonormal, because

$$\mathbf{u}_i^{\top}\mathbf{u}_j=\frac{\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_id_j}=\frac{d_j^2\,\mathbf{v}_i^{\top}\mathbf{v}_j}{d_id_j},$$

and this is $1$ for $i=j$ and $0$ otherwise. They are the eigenvectors of $\mathbf{A}\mathbf{A}^{\top}$, and the equation in the opposite direction holds:

$$\mathbf{A}^{\top}\mathbf{u}_j=\frac{\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_j}=d_j\mathbf{v}_j,\qquad \mathbf{A}\mathbf{A}^{\top}\mathbf{u}_j=d_j\,\mathbf{A}\mathbf{v}_j=d_j^2\,\mathbf{u}_j .$$

$\mathbf{A}$ maps $\mathbf{v}_j$ to $d_j\mathbf{u}_j$, and $\mathbf{A}^{\top}$ maps $\mathbf{u}_j$ to $d_j\mathbf{v}_j$.

:::warnung The signs belong together
An eigenvector is determined only up to its sign. If you compute the $\mathbf{v}_j$ as eigenvectors of $\mathbf{A}^{\top}\mathbf{A}$ and, separately, the $\mathbf{u}_j$ as eigenvectors of $\mathbf{A}\mathbf{A}^{\top}$, a $\mathbf{u}_j$ may end up with the wrong sign, and then $\mathbf{A}\mathbf{v}_j=-d_j\mathbf{u}_j$. The safe way is via [(9.2)](#gl-9-2): first choose $\mathbf{v}_j$, then compute $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$. If you flip $\mathbf{v}_j$ and $\mathbf{u}_j$ together, everything stays correct.
:::

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, we get $\mathbf{u}_1=\mathbf{A}\mathbf{v}_1/4=(2,\,1)^{\top}/\sqrt5$ and $\mathbf{u}_2=\mathbf{A}\mathbf{v}_2/1=(-1,\,2)^{\top}/\sqrt5$. As a check: $\mathbf{A}\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}13&6\\6&4\end{smallmatrix}\bigr)$ maps $(2,\,1)^{\top}$ to $(32,\,16)^{\top}=16\,(2,\,1)^{\top}$. The vector $(-2,\,-1)^{\top}/\sqrt5$ would also be a normalized eigenvector of $\mathbf{A}\mathbf{A}^{\top}$ for $16$, but with it, $\mathbf{A}\mathbf{v}_1=-4\,\mathbf{u}_1$.

⁠**In short:** The right singular vectors $\mathbf{v}_j$ are eigenvectors of $\mathbf{A}^{\top}\mathbf{A}$, the left ones are $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$; both families are orthonormal, and $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$.

### The decomposition

<span class="anker" id="stufe-9-4"></span>

Writing the equations $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$ for all $j$ side by side produces a decomposition of the whole matrix.

:::satz Theorem 9.4 (Singular value decomposition)
<span class="anker" id="satz-9-4"></span>

Every matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ of rank $r$ can be written as

<span class="anker" id="gl-9-3"></span>
$$\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top} \tag{9.3}$$

with orthogonal matrices $\mathbf{U}\in\mathbb{R}^{m\times m}$ and $\mathbf{V}\in\mathbb{R}^{n\times n}$ and a matrix $\mathbf{D}\in\mathbb{R}^{m\times n}$ that carries the singular values $d_1\ge\dots\ge d_r>0$ on its diagonal and only zeros elsewhere. The columns of $\mathbf{V}$ are right singular vectors, and the first $r$ columns of $\mathbf{U}$ are the corresponding left ones. An equivalent form is the compact form

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}=\sum_{j=1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} . \tag{9.4}$$
:::

:::beweis Singular value decomposition
For $j\le r$ we have $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$. For $j>r$ we have $d_j=0$, so $\lVert\mathbf{A}\mathbf{v}_j\rVert=0$ and $\mathbf{A}\mathbf{v}_j=\mathbf{0}$. If $r<m$, extend $\mathbf{u}_1,\dots,\mathbf{u}_r$ to an orthonormal basis of $\mathbb{R}^m$, for instance with the Gram–Schmidt process as in the proof of the spectral theorem. By Part 1, Section 9.2, column $j$ of $\mathbf{A}\mathbf{V}$ is the vector $\mathbf{A}\mathbf{v}_j$, and column $j$ of $\mathbf{U}\mathbf{D}$ is $d_j\mathbf{u}_j$ for $j\le r$ and the zero vector otherwise. So $\mathbf{A}\mathbf{V}=\mathbf{U}\mathbf{D}$. Because $\mathbf{V}$ is orthogonal, $\mathbf{V}\mathbf{V}^{\top}=\mathbf{I}$, and multiplying by $\mathbf{V}^{\top}$ from the right gives $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$. The compact form follows from Part 1, Section 9.5: column $j$ of $\mathbf{U}\mathbf{D}$ times row $j$ of $\mathbf{V}^{\top}$, summed over $j$; only the terms with $j\le r$ are nonzero.
:::

The shape of $\mathbf{D}$ follows the shape of $\mathbf{A}$. For $m=3$ and $n=2$, for example, $\mathbf{D}=\Bigl(\begin{smallmatrix}d_1&0\\0&d_2\\0&0\end{smallmatrix}\Bigr)$. The usual abbreviation is SVD, for *singular value decomposition*.

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$,

$$\mathbf{A}=\underbrace{\frac1{\sqrt5}\begin{pmatrix}2&-1\\1&2\end{pmatrix}}_{\mathbf{U}}\underbrace{\begin{pmatrix}4&0\\0&1\end{pmatrix}}_{\mathbf{D}}\underbrace{\frac1{\sqrt5}\begin{pmatrix}1&2\\-2&1\end{pmatrix}}_{\mathbf{V}^{\top}},$$

because $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}8&-1\\4&2\end{smallmatrix}\bigr)$ and $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\tfrac15\bigl(\begin{smallmatrix}8+2&16-1\\4-4&8+2\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$. In compact form:

$$4\cdot\frac15\begin{pmatrix}2&4\\1&2\end{pmatrix}+1\cdot\frac15\begin{pmatrix}2&-1\\-4&2\end{pmatrix}=\begin{pmatrix}1.6&3.2\\0.8&1.6\end{pmatrix}+\begin{pmatrix}0.4&-0.2\\-0.8&0.4\end{pmatrix}=\begin{pmatrix}2&3\\0&2\end{pmatrix}.$$

⁠**In short:** Every matrix is $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ with two orthogonal matrices and the singular values on the diagonal of $\mathbf{D}$, or, equivalently, a sum $\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$.

:::hintergrund Why the decomposition exists for every matrix
Not every matrix has eigenvectors, and its eigenvectors are not always perpendicular. The singular value decomposition gets around both obstacles with a trick: it does not use the eigenvectors of $\mathbf{A}$ but those of $\mathbf{A}^{\top}\mathbf{A}$. This matrix is symmetric and positive semidefinite for every $\mathbf{A}$, and for it the spectral theorem guarantees an orthonormal basis of eigenvectors with eigenvalues $\ge0$. The price: you need two bases instead of one, one for the inputs and one for the outputs.

The singular vectors can also be described without $\mathbf{A}^{\top}\mathbf{A}$. By [(8.2)](positiv-definite-matrizen.html#gl-8-2), applied to $\mathbf{A}^{\top}\mathbf{A}$, every unit vector satisfies $\lVert\mathbf{A}\mathbf{v}\rVert^2=\mathbf{v}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}\le\lambda_1=d_1^2$, with equality at $\mathbf{v}_1$. So $\mathbf{v}_1$ is the direction that $\mathbf{A}$ stretches most, and $d_1$ is this largest stretch. Among all unit vectors perpendicular to $\mathbf{v}_1$, the one stretched most is $\mathbf{v}_2$, and so on; this is shown by the same weighted-mean calculation as in the proof of [(8.2)](positiv-definite-matrizen.html#gl-8-2), with $c_1=0$. So the decomposition lists the directions in order, from the strongest to the weakest stretch.

The singular values are unique. If all $d_j$ are different and positive, each pair $\mathbf{v}_j,\mathbf{u}_j$ is fixed up to a common sign. With equal singular values there is more freedom: an orthogonal matrix $\mathbf{Q}$ has all singular values equal to $1$, and for every orthogonal matrix $\mathbf{V}$, the factorization $\mathbf{Q}=(\mathbf{Q}\mathbf{V})\,\mathbf{I}\,\mathbf{V}^{\top}$ is a singular value decomposition.
:::

### Rotation, stretch, rotation

<span class="anker" id="stufe-9-5"></span>

Reading $\mathbf{A}\mathbf{x}=\mathbf{U}\bigl(\mathbf{D}(\mathbf{V}^{\top}\mathbf{x})\bigr)$ from right to left, every matrix acts in three steps (Fig. [23](#abb-23)):

<ol>

<li>

By [(1.2)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-2), $\mathbf{V}^{\top}\mathbf{x}$ computes the coordinates $c_j=\mathbf{v}_j^{\top}\mathbf{x}$ of $\mathbf{x}$ in the basis of the $\mathbf{v}_j$. Geometrically, this is a rotation or reflection that puts $\mathbf{v}_j$ onto $\mathbf{e}_j$.

</li>

<li>

$\mathbf{D}$ multiplies each coordinate $c_j$ by $d_j$. If $m>n$, $\mathbf{D}$ appends zeros; if $m<n$, $\mathbf{D}$ drops the last coordinates. The unit circle becomes an ellipse whose axes lie on the coordinate axes.

</li>

<li>

$\mathbf{U}$ puts $\mathbf{e}_j$ onto $\mathbf{u}_j$, again a rotation or reflection.

</li>

</ol>

So every linear map is, up to reflections, a rotation, a stretch along the axes and another rotation. It turns the unit circle into an ellipse and the unit sphere into an ellipsoid, with the semi-axes $d_j\mathbf{u}_j$. If $\det\mathbf{A}<0$, at least one reflection is involved, because by Part 1, Section 14.5, $\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$, and $\det\mathbf{D}\ge0$.

:::abbildung ml/k2svd 23
The matrix $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ as rotation, stretch, rotation. Top left, the unit circle with $\mathbf{v}_1=(1,2)^{\top}/\sqrt5$ (red) and $\mathbf{v}_2=(-2,1)^{\top}/\sqrt5$ (green). $\mathbf{V}^{\top}$ rotates by $-63.4^\circ$ and puts $\mathbf{v}_1$ onto $\mathbf{e}_1$ and $\mathbf{v}_2$ onto $\mathbf{e}_2$ (bottom left). $\mathbf{D}$ stretches the first axis by $d_1=4$ and the second by $d_2=1$ (bottom right). $\mathbf{U}$ rotates by $26.6^\circ$ and puts the axes onto $\mathbf{u}_1=(2,1)^{\top}/\sqrt5$ and $\mathbf{u}_2=(-1,2)^{\top}/\sqrt5$ (top right). The black point $\mathbf{x}=\mathbf{e}_2$ ends up at $\mathbf{A}\mathbf{x}=(3,2)^{\top}$ by either route. The direct route at the top is $\mathbf{A}$ itself: the unit circle becomes the ellipse with the semi-axes $4\,\mathbf{u}_1$ and $1\cdot\mathbf{u}_2$.
:::

⁠**Worked example:** For $\mathbf{x}=\mathbf{e}_2$ and $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, the coordinates are $\mathbf{V}^{\top}\mathbf{x}=(2,\,1)^{\top}/\sqrt5$. Stretched, this gives $\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=(8,\,1)^{\top}/\sqrt5$, and rotated,

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=\frac15\begin{pmatrix}2&-1\\1&2\end{pmatrix}\begin{pmatrix}8\\1\end{pmatrix}=\frac15\begin{pmatrix}15\\10\end{pmatrix}=\begin{pmatrix}3\\2\end{pmatrix}=\mathbf{A}\mathbf{e}_2 .$$

$\mathbf{V}$ has the columns $(\cos\theta,\,\sin\theta)^{\top}$ and $(-\sin\theta,\,\cos\theta)^{\top}$ with $\cos\theta=1/\sqrt5$, so it is the rotation by $\theta\approx63.4^\circ$, and $\mathbf{V}^{\top}$ rotates back by $-63.4^\circ$. $\mathbf{U}$ is the rotation by $26.6^\circ$, because $\cos26.6^\circ\approx2/\sqrt5$.

⁠**In short:** Every matrix rotates, stretches along the axes and rotates again, up to reflections; the unit circle becomes an ellipse with the semi-axes $d_j\mathbf{u}_j$.

### Building blocks of rank 1 and the spaces of a matrix

<span class="anker" id="stufe-9-6"></span>

Each term $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ of the compact form [(9.4)](#gl-9-4) has rank $1$, because all its columns are multiples of $\mathbf{u}_j$. It acts on a vector as follows:

$$d_j\mathbf{u}_j\mathbf{v}_j^{\top}\mathbf{x}=d_j\,(\mathbf{v}_j^{\top}\mathbf{x})\,\mathbf{u}_j .$$

It reads off the coordinate of $\mathbf{x}$ along $\mathbf{v}_j$, multiplies it by $d_j$ and outputs the result in the direction of $\mathbf{u}_j$. The matrix is the sum of $r$ such building blocks, ordered by their size $d_j$. Along the way, the decomposition provides orthonormal bases for the subspaces that belong to a matrix.

:::satz Theorem 9.5 (What the singular vectors span)
<span class="anker" id="satz-9-5"></span>

Let $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ with rank $r$. Then:

<ol class="rm">

<li>

$\mathbf{u}_1,\dots,\mathbf{u}_r$ is an orthonormal basis of the column space of $\mathbf{A}$, and $\mathbf{u}_{r+1},\dots,\mathbf{u}_m$ is an orthonormal basis of its orthogonal complement;

</li>

<li>

$\mathbf{v}_{r+1},\dots,\mathbf{v}_n$ is an orthonormal basis of the null space of $\mathbf{A}$, and $\mathbf{v}_1,\dots,\mathbf{v}_r$ is an orthonormal basis of the column space of $\mathbf{A}^{\top}$.

</li>

</ol>
:::

:::beweis Spaces
(i) Every $\mathbf{A}\mathbf{x}=\sum_{j\le r}d_j(\mathbf{v}_j^{\top}\mathbf{x})\mathbf{u}_j$ lies in the span of $\mathbf{u}_1,\dots,\mathbf{u}_r$, and conversely $\mathbf{u}_j=\mathbf{A}(\mathbf{v}_j/d_j)$ is an image. The remaining columns of $\mathbf{U}$ are perpendicular to these, so by Section [4.4](projektion-auf-einen-unterraum.html#stufe-4-4) they span the orthogonal complement. (ii) Because the $\mathbf{u}_j$ are independent and the $d_j$ positive, $\mathbf{A}\mathbf{x}=\mathbf{0}$ if and only if $\mathbf{v}_j^{\top}\mathbf{x}=0$ for all $j\le r$, that is, if $\mathbf{x}$ has coordinates only along $\mathbf{v}_{r+1},\dots,\mathbf{v}_n$. Finally, $\mathbf{A}^{\top}=\mathbf{V}\mathbf{D}^{\top}\mathbf{U}^{\top}$ is a singular value decomposition of $\mathbf{A}^{\top}$ in which $\mathbf{U}$ and $\mathbf{V}$ swap roles; (i) for $\mathbf{A}^{\top}$ gives the rest.
:::

The numbers match the rank–nullity theorem from Part 1, Section 13.5: the null space has dimension $n-r$.

⁠**Worked example:** The matrix $\mathbf{H}$ with the columns $(1,\,0,\,1)^{\top}$ and $(0,\,1,\,1)^{\top}$ from Section [3.2](die-beste-naherungslosung.html#stufe-3-2) has $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ with the eigenvalues $3$ and $1$, hence the singular values $d_1=\sqrt3$ and $d_2=1$, and the right singular vectors $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$, $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$. The left ones are

$$\mathbf{u}_1=\frac{\mathbf{H}\mathbf{v}_1}{\sqrt3}=\frac1{\sqrt6}\begin{pmatrix}1\\1\\2\end{pmatrix},\qquad \mathbf{u}_2=\frac{\mathbf{H}\mathbf{v}_2}{1}=\frac1{\sqrt2}\begin{pmatrix}1\\-1\\0\end{pmatrix}.$$

They form an orthonormal basis of the plane $x_3=x_1+x_2$, a different one from that in Section [4.3](projektion-auf-einen-unterraum.html#stufe-4-3). It is completed by $\mathbf{u}_3=(1,\,1,\,-1)^{\top}/\sqrt3$, the normalized normal vector from Section [4.4](projektion-auf-einen-unterraum.html#stufe-4-4). In the full decomposition, $\mathbf{D}=\Bigl(\begin{smallmatrix}\sqrt3&0\\0&1\\0&0\end{smallmatrix}\Bigr)$. The null space consists only of the zero vector, because $r=n=2$.

⁠**In short:** A matrix is the sum of $r$ building blocks $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ of rank $1$; the $\mathbf{u}_j$ with $d_j>0$ span the column space, and the $\mathbf{v}_j$ with $d_j=0$ span the null space.

### Symmetric matrices

<span class="anker" id="stufe-9-7"></span>

For a symmetric matrix there is already a decomposition with an orthonormal basis, $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$. How is it related to the singular value decomposition?

:::satz Theorem 9.6 (Singular values of symmetric matrices)
<span class="anker" id="satz-9-6"></span>

The singular values of a symmetric matrix are the magnitudes $|\lambda_i|$ of its eigenvalues. If $\mathbf{q}_i$ is a normalized eigenvector for $\lambda_i\ne0$, then $\mathbf{v}=\mathbf{q}_i$ is a right singular vector and $\mathbf{u}=\operatorname{sign}(\lambda_i)\,\mathbf{q}_i$ the corresponding left singular vector.
:::

:::beweis Symmetric matrices
We have $\mathbf{A}^{\top}\mathbf{A}=\mathbf{A}^2=\mathbf{Q}\boldsymbol{\Lambda}^2\mathbf{Q}^{\top}$, so $\mathbf{A}^{\top}\mathbf{A}$ has the eigenvectors $\mathbf{q}_i$ with the eigenvalues $\lambda_i^2$, and the singular values are $\sqrt{\lambda_i^2}=|\lambda_i|$. By [(9.2)](#gl-9-2), $\mathbf{u}=\mathbf{A}\mathbf{q}_i/|\lambda_i|=(\lambda_i/|\lambda_i|)\,\mathbf{q}_i$.
:::

If $\mathbf{A}$ is positive semidefinite, the spectral decomposition and the singular value decomposition are the same decomposition, with $\mathbf{U}=\mathbf{V}=\mathbf{Q}$. For negative eigenvalues, the sign moves into $\mathbf{U}$. For non-symmetric matrices, eigenvalues and singular values generally have nothing to do with each other, as $\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ with the eigenvalues $2,2$ and the singular values $4,1$ shows. There is always one connection, though: every eigenvalue is at most $d_1$ in magnitude; this follows from the next subsection.

⁠**Worked example:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ has the eigenvalues $4$ with $\mathbf{q}_1=(1,\,1)^{\top}/\sqrt2$ and $-2$ with $\mathbf{q}_2=(1,\,-1)^{\top}/\sqrt2$. The singular values are $4$ and $2$. With $\mathbf{v}_2=\mathbf{q}_2$ we get $\mathbf{A}\mathbf{v}_2=(-2,\,2)^{\top}/\sqrt2=2\cdot(-1,\,1)^{\top}/\sqrt2$, so $\mathbf{u}_2=-\mathbf{q}_2$.

⁠**In short:** For symmetric matrices, the singular values are the magnitudes of the eigenvalues, and for positive semidefinite ones the singular value decomposition is the spectral decomposition.

### The spectral norm

<span class="anker" id="stufe-9-8"></span>

By how much can a matrix lengthen a vector at most? For vectors, the norm measures size. For a matrix, a natural measure of size is its largest lengthening factor.

:::definition Definition 9.7 (Spectral norm)
<span class="anker" id="satz-9-7"></span>

The __spectral norm__ of a matrix $\mathbf{A}$ is

$$\lVert\mathbf{A}\rVert_2=\max_{\mathbf{x}\ne\mathbf{0}}\frac{\lVert\mathbf{A}\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert} .$$
:::

:::satz Theorem 9.8 (Largest and smallest stretch)
<span class="anker" id="satz-9-8"></span>

For every $\mathbf{A}\in\mathbb{R}^{m\times n}$ with the singular values $d_1\ge\dots\ge d_n$ and every $\mathbf{x}\in\mathbb{R}^n$,

<span class="anker" id="gl-9-5"></span>
$$d_n\,\lVert\mathbf{x}\rVert\le\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\,\lVert\mathbf{x}\rVert . \tag{9.5}$$

The bounds are attained at $\mathbf{x}=\mathbf{v}_1$ and $\mathbf{x}=\mathbf{v}_n$. In particular, $\lVert\mathbf{A}\rVert_2=d_1$.
:::

:::beweis Largest and smallest stretch
With $\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$, we have $\lVert\mathbf{c}\rVert=\lVert\mathbf{x}\rVert$ and $\lVert\mathbf{A}\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\sum_jd_j^2c_j^2$. This lies between $d_n^2\sum_jc_j^2$ and $d_1^2\sum_jc_j^2$. It is the Rayleigh quotient [(8.2)](positiv-definite-matrizen.html#gl-8-2) of $\mathbf{A}^{\top}\mathbf{A}$, multiplied by $\lVert\mathbf{x}\rVert^2$.
:::

Two consequences. First, $\lVert\mathbf{A}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{x}\rVert$ and therefore $\lVert\mathbf{A}\mathbf{B}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2\lVert\mathbf{x}\rVert$, so $\lVert\mathbf{A}\mathbf{B}\rVert_2\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2$: when two maps are applied one after the other, their largest stretch factors at most multiply. Second, every eigenvector satisfies $\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$, so $|\lambda|\le d_1$ for every eigenvalue of a square matrix. For a complex eigenvector $\mathbf{v}=\mathbf{a}+\mathrm j\mathbf{b}$ with real $\mathbf{a},\mathbf{b}$ the same holds if you set $\lVert\mathbf{v}\rVert^2=(\mathbf{v}^*)^{\top}\mathbf{v}=\lVert\mathbf{a}\rVert^2+\lVert\mathbf{b}\rVert^2$, because by [(9.5)](#gl-9-5), $\lVert\mathbf{A}\mathbf{v}\rVert^2=\lVert\mathbf{A}\mathbf{a}\rVert^2+\lVert\mathbf{A}\mathbf{b}\rVert^2$ lies between $d_n^2\lVert\mathbf{v}\rVert^2$ and $d_1^2\lVert\mathbf{v}\rVert^2$; for square $\mathbf{A}$, therefore, $|\lambda|\ge d_n$ as well.

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, we have $\lVert\mathbf{A}\rVert_2=4$. The unit vectors are stretched less: $\lVert\mathbf{A}\mathbf{e}_1\rVert=\lVert(2,\,0)^{\top}\rVert=2$ and $\lVert\mathbf{A}\mathbf{e}_2\rVert=\lVert(3,\,2)^{\top}\rVert=\sqrt{13}\approx3.61$. The factor $4$ is reached only at $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$, the smallest factor $1$ at $\mathbf{v}_2$. The eigenvalue $2$ lies between $1$ and $4$.

⁠**In short:** The spectral norm $\lVert\mathbf{A}\rVert_2=d_1$ is the largest factor by which $\mathbf{A}$ lengthens a vector; the smallest is $d_n$.

:::hintergrund Multiple antennas: parallel channels from the singular value decomposition
A radio system with several transmit and receive antennas is called a MIMO system. Each receive antenna receives a mixture of all transmitted signals. In a simple model, the received vector is $\mathbf{y}=\mathbf{K}\mathbf{x}+\boldsymbol\nu$: $\mathbf{x}$ contains the transmitted signals of the antennas, the channel matrix $\mathbf{K}$ describes how strongly each transmit antenna arrives at each receive antenna, and $\boldsymbol\nu$ is the noise.

If transmitter and receiver know the decomposition $\mathbf{K}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$, the transmitter sends $\mathbf{x}=\mathbf{V}\tilde{\mathbf{x}}$, and the receiver computes $\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{y}$. Then

$$\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\tilde{\mathbf{x}}+\mathbf{U}^{\top}\boldsymbol\nu=\mathbf{D}\tilde{\mathbf{x}}+\tilde{\boldsymbol\nu} .$$

The mixed channel has turned into $r$ separate channels: $\tilde y_j=d_j\tilde x_j+\tilde\nu_j$. Each carries its own data stream, with the gain $d_j$. The noise is only rotated in the process; its length stays the same, because $\mathbf{U}^{\top}$ is orthogonal. The number of usable parallel channels is the rank of the channel matrix, and the singular value of each channel tells how good it is. This is rotation, stretch, rotation in practice: the transmitter pre-rotates, the channel stretches, the receiver rotates back.
:::

:::aufgabe Exercise 27 ★★ A decomposition by hand
<span class="anker" id="aufg-27"></span>

Let $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Compute $\mathbf{A}^{\top}\mathbf{A}$, its eigenvalues and the singular values of $\mathbf{A}$.

</li>

<li>

Determine $\mathbf{v}_1,\mathbf{v}_2$ and from them $\mathbf{u}_1,\mathbf{u}_2$ with [(9.2)](#gl-9-2). Check $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$.

</li>

<li>

Compare the singular values with the eigenvalues of $\mathbf{A}$. What agrees, and what does not?

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}9+16&20\\20&25\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}25&20\\20&25\end{smallmatrix}\bigr)$ with trace $50$ and determinant $625-400=225$, so $\lambda^2-50\lambda+225=(\lambda-45)(\lambda-5)$. The singular values are $d_1=\sqrt{45}=3\sqrt5\approx6.708$ and $d_2=\sqrt5\approx2.236$.

(b) Eigenvectors of $\mathbf{A}^{\top}\mathbf{A}$: $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ for $45$ and $\mathbf{v}_2=(-1,\,1)^{\top}/\sqrt2$ for $5$. Then

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}{d_1}=\frac{(3,\,9)^{\top}}{\sqrt2\cdot3\sqrt5}=\frac{(1,\,3)^{\top}}{\sqrt{10}},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{d_2}=\frac{(-3,\,1)^{\top}}{\sqrt2\cdot\sqrt5}=\frac{(-3,\,1)^{\top}}{\sqrt{10}} .$$

Check: $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt{10}}\bigl(\begin{smallmatrix}3\sqrt5&-3\sqrt5\\9\sqrt5&\sqrt5\end{smallmatrix}\bigr)=\tfrac1{\sqrt2}\bigl(\begin{smallmatrix}3&-3\\9&1\end{smallmatrix}\bigr)$ and

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\frac1{\sqrt2}\begin{pmatrix}3&-3\\9&1\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\frac12\begin{pmatrix}6&0\\8&10\end{pmatrix}=\begin{pmatrix}3&0\\4&5\end{pmatrix}.$$

(c) The eigenvalues of the triangular matrix are $3$ and $5$. The products agree: $3\cdot5=15=3\sqrt5\cdot\sqrt5=|\det\mathbf{A}|$. The sums do not: $8$ versus $4\sqrt5\approx8.94$. In magnitude, the eigenvalues lie between $d_2$ and $d_1$: $2.236\le3$ and $5\le6.708$.
:::
:::

:::aufgabe Exercise 28 ★★ A rectangular matrix
<span class="anker" id="aufg-28"></span>

Let $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$.

<ol class="al">

<li>

Determine the singular values and the singular vectors $\mathbf{v}_1,\mathbf{v}_2,\mathbf{u}_1,\mathbf{u}_2$.

</li>

<li>

Add $\mathbf{u}_3$ and write down the full decomposition $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$.

</li>

<li>

Give orthonormal bases of the column space and of its orthogonal complement.

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ has the eigenvalues $4$ with $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ and $2$ with $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$. So $d_1=2$, $d_2=\sqrt2$, and

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}2=\frac{(2,\,2,\,0)^{\top}}{2\sqrt2}=\frac{(1,\,1,\,0)^{\top}}{\sqrt2},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{\sqrt2}=\frac{(0,\,0,\,2)^{\top}}{\sqrt2\cdot\sqrt2}=(0,\,0,\,1)^{\top} .$$

(b) $\mathbf{u}_3$ is perpendicular to both: $\mathbf{u}_3=(1,\,-1,\,0)^{\top}/\sqrt2$. The full decomposition is

$$\mathbf{A}=\begin{pmatrix}1/\sqrt2&0&1/\sqrt2\\1/\sqrt2&0&-1/\sqrt2\\0&1&0\end{pmatrix}\begin{pmatrix}2&0\\0&\sqrt2\\0&0\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$

(c) By the theorem in Section [9.6](#stufe-9-6), $\mathbf{u}_1,\mathbf{u}_2$ is an orthonormal basis of the column space and $\mathbf{u}_3$ one of the orthogonal complement. As a check: the columns $(1,\,1,\,1)^{\top}=\sqrt2\,\mathbf{u}_1+\mathbf{u}_2$ and $(1,\,1,\,-1)^{\top}=\sqrt2\,\mathbf{u}_1-\mathbf{u}_2$ lie in the span of $\mathbf{u}_1,\mathbf{u}_2$, and both are perpendicular to $\mathbf{u}_3$.
:::
:::

:::aufgabe Exercise 29 ★★★ Properties of singular values
<span class="anker" id="aufg-29"></span>

<ol class="al">

<li>

Show: for a square matrix, $|\det\mathbf{A}|=d_1d_2\cdots d_n$.

</li>

<li>

Show: $\mathbf{A}$ and $\mathbf{A}^{\top}$ have the same positive singular values.

</li>

<li>

Show: for $\mathbf{u}\ne\mathbf{0}$ and $\mathbf{v}\ne\mathbf{0}$, the outer product $\mathbf{u}\mathbf{v}^{\top}$ has exactly one positive singular value, namely $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.

</li>

<li>

Show: if $\mathbf{Q}$ is orthogonal, then $\mathbf{Q}\mathbf{A}$ and $\mathbf{A}$ have the same singular values.

</li>

</ol>

:::loesung
(a) By Part 1, Section 14.5, $\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$. The two orthogonal matrices have the determinant $\pm1$, and $\mathbf{D}$ is a diagonal matrix with the determinant $d_1\cdots d_n$. Hence $|\det\mathbf{A}|=d_1\cdots d_n$.

(b) From $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ it follows that $\mathbf{A}^{\top}\mathbf{A}=\mathbf{V}\mathbf{D}^{\top}\mathbf{D}\mathbf{V}^{\top}$ and $\mathbf{A}\mathbf{A}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^{\top}\mathbf{U}^{\top}$. The diagonal matrices $\mathbf{D}^{\top}\mathbf{D}$ and $\mathbf{D}\mathbf{D}^{\top}$ have the same entries $d_j^2>0$ on the diagonal, only different numbers of zeros. The singular values of $\mathbf{A}^{\top}$ are the square roots of the eigenvalues of $(\mathbf{A}^{\top})^{\top}\mathbf{A}^{\top}=\mathbf{A}\mathbf{A}^{\top}$, so again the $d_j$, supplemented by zeros.

(c) $(\mathbf{u}\mathbf{v}^{\top})^{\top}(\mathbf{u}\mathbf{v}^{\top})=\mathbf{v}\,\mathbf{u}^{\top}\mathbf{u}\,\mathbf{v}^{\top}=\lVert\mathbf{u}\rVert^2\,\mathbf{v}\mathbf{v}^{\top}$. This matrix maps $\mathbf{v}$ to $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2\,\mathbf{v}$ and every vector perpendicular to $\mathbf{v}$ to zero. Its eigenvalues are therefore $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$ and otherwise $0$, and the only positive singular value is $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.

(d) $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$. Both matrices have the same Gram matrix and hence the same singular values. Intuitively: a rotation or reflection after $\mathbf{A}$ does not change the shape of the ellipse, only its position.
:::
:::
