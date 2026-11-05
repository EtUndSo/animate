---
title: Projection onto a subspace
pfad: Computer Science / Machine Learning / Projection, Eigenvalues and Decompositions
order: 6220500
summary: The previous section found the closest point of a column space.
tags: subspace, projection matrix, orthogonal complement, Gram–Schmidt process, QR decomposition
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
The previous section found the closest point of a column space. This section expresses the result as a matrix, shows that everything becomes especially simple when the columns are orthonormal, and presents a procedure that turns arbitrary independent columns into orthonormal ones. With it, the best approximate solution can be computed without forming $\mathbf{A}^{\top}\mathbf{A}$.
:::

### Subspaces

<span class="anker" id="stufe-4-1"></span>

Lines and planes through the origin, column spaces and null spaces share a common property: whenever they contain two vectors, they also contain every linear combination of the two. You never leave them by adding and scaling. There is a special word for such sets.

:::definition Definition 4.1 (Subspace)
<span class="anker" id="satz-4-1"></span>

A set $\mathcal U\subseteq\mathbb{R}^n$ is called a __subspace__ of $\mathbb{R}^n$ if it is the span of finitely many vectors.
:::

Equivalently: $\mathcal U$ contains the zero vector, and whenever $\mathcal U$ contains two vectors $\mathbf{u},\mathbf{v}$, it also contains $\mathbf{u}+\mathbf{v}$ and every multiple $c\,\mathbf{u}$. Every subspace has a basis and therefore, by Part 1, Section 13.3, a dimension.

⁠**Worked example:** In $\mathbb{R}^3$, the following are subspaces: the origin alone, with dimension $0$; every line through the origin, with dimension $1$; every plane through the origin, such as the column space of $\mathbf{H}$ from the previous section, with dimension $2$; and all of $\mathbb{R}^3$. The null space of a matrix is a subspace, and so is its column space. A line that does not pass through the origin is not a subspace, because it does not contain the zero vector.

⁠**In short:** A subspace is a span of vectors; you do not leave it by adding and scaling.

### The projection matrix of a column space

<span class="anker" id="stufe-4-2"></span>

For linearly independent columns, [(3.5)](die-beste-naherungslosung.html#gl-3-5) gives the closest point $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$. The matrix in front of $\mathbf{y}$ depends only on $\mathbf{A}$. It does for the column space what $\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ did for a line.

:::definition Definition 4.2 (Projection matrix of a column space)
<span class="anker" id="satz-4-2"></span>

If $\mathbf{A}$ has linearly independent columns, then

<span class="anker" id="gl-4-1"></span>
$$\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{4.1}$$

is called the __projection matrix__ onto the column space of $\mathbf{A}$.
:::

:::satz Theorem 4.3 (Properties)
<span class="anker" id="satz-4-3"></span>

We have $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$, $\mathbf{P}^{\top}=\mathbf{P}$, $\mathbf{P}^2=\mathbf{P}$ and $\mathbf{P}\mathbf{A}=\mathbf{A}$. So $\mathbf{P}$ is the orthogonal projection onto the column space.
:::

:::beweis Properties
The first equation is the derivation above. With the rules from Part 1, Sections 10.1 and 11.4, $\mathbf{P}^{\top}=\mathbf{A}\bigl((\mathbf{A}^{\top}\mathbf{A})^{-1}\bigr)^{\top}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$, because $\mathbf{A}^{\top}\mathbf{A}$ is symmetric and hence so is its inverse. Furthermore, $\mathbf{P}\mathbf{A}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}(\mathbf{A}^{\top}\mathbf{A})=\mathbf{A}$, and from this $\mathbf{P}^2=\mathbf{P}\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}=\mathbf{P}$. By the theorem in Section [2.4](projektion-auf-eine-gerade.html#stufe-2-4), a symmetric projection is orthogonal.
:::

The equation $\mathbf{P}\mathbf{A}=\mathbf{A}$ says: every column, and hence every vector of the column space, stays where it is when projected.

⁠**Worked example:** For $\mathbf{H}$,

$$\mathbf{P}=\mathbf{H}\cdot\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\mathbf{H}^{\top}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix}.$$

Check: $\mathbf{P}(1,\,1,\,1)^{\top}=\tfrac13(2,\,2,\,4)^{\top}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}=\hat{\mathbf{y}}$, and $\mathbf{P}\mathbf{a}_1=\tfrac13(2+1,\ -1+1,\ 1+2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_1$.

⁠**In short:** The projection matrix $\mathbf{P}=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ maps every vector to the closest point of the column space; it is symmetric and satisfies $\mathbf{P}^2=\mathbf{P}$.

### Orthonormal columns

<span class="anker" id="stufe-4-3"></span>

The formula [(4.1)](#gl-4-1) contains an inverse. It disappears when the columns are orthonormal, because then $\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$. For a matrix $\mathbf{Q}$ with orthonormal columns, the best approximate solution is therefore simply $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$: its components are the shadow lengths $\mathbf{q}_i^{\top}\mathbf{y}$.

:::satz Theorem 4.4 (Projection with orthonormal columns)
<span class="anker" id="satz-4-4"></span>

If $\mathbf{Q}\in\mathbb{R}^{n\times k}$ has orthonormal columns $\mathbf{q}_1,\dots,\mathbf{q}_k$, then the projection matrix onto its column space is

<span class="anker" id="gl-4-2"></span>
$$\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}=\sum_{i=1}^k\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{4.2}$$
:::

The sum form follows from Part 1, Section 9.5: a matrix product is the sum of the outer products of columns and rows. Each term $\mathbf{q}_i\mathbf{q}_i^{\top}$ is the projection matrix onto the line in the direction of $\mathbf{q}_i$. So with orthonormal columns, the projection onto the column space is the sum of the projections onto the individual axes. This explains in hindsight the last subsection of Section [1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1): $\mathbf{Q}\mathbf{Q}^{\top}$ is not the identity matrix but the projection onto the column space of $\mathbf{Q}$. Whatever is perpendicular to it is thrown away.

⁠**Worked example:** The vectors $\mathbf{q}_1=\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}$ and $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$ are orthonormal: $\lVert\mathbf{q}_1\rVert^2=\tfrac22$, $\lVert\mathbf{q}_2\rVert^2=\tfrac66$, $\mathbf{q}_1^{\top}\mathbf{q}_2=\tfrac{-1+0+1}{\sqrt{12}}=0$. For both, the third component is the sum of the first two; they form an orthonormal basis of the plane of $\mathbf{H}$. We have

$$\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}=\frac12\begin{pmatrix}1&0&1\\0&0&0\\1&0&1\end{pmatrix}+\frac16\begin{pmatrix}1&-2&-1\\-2&4&2\\-1&2&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\\1&1&2\end{pmatrix},$$

the same matrix as in the previous subsection, this time without an inverse.

⁠**In short:** With orthonormal columns, $\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ and $\mathbf{P}=\mathbf{Q}\mathbf{Q}^{\top}$, the sum of the projections onto the individual columns.

### The orthogonal complement

<span class="anker" id="stufe-4-4"></span>

If you project $\mathbf{y}$ onto a subspace, the residual $\mathbf{y}-\mathbf{P}\mathbf{y}$ is left over. It is perpendicular to the entire subspace. All vectors with this property form a subspace themselves, and $\mathbf{y}$ splits into a part in the one subspace and a part in the other.

:::definition Definition 4.5 (Orthogonal complement)
<span class="anker" id="satz-4-5"></span>

The __orthogonal complement__ of a subspace $\mathcal U\subseteq\mathbb{R}^n$ is the set

<span class="anker" id="gl-4-3"></span>
$$\mathcal U^\perp=\{\mathbf{z}\in\mathbb{R}^n:\ \mathbf{z}^{\top}\mathbf{u}=0\ \text{for all}\ \mathbf{u}\in\mathcal U\} . \tag{4.3}$$
:::

The symbol $\mathcal U^\perp$ is read “$\mathcal U$ perp”. If $\mathcal U$ is the column space of $\mathbf{A}$, then $\mathbf{z}$ is perpendicular to $\mathcal U$ exactly when $\mathbf{A}^{\top}\mathbf{z}=\mathbf{0}$; so the orthogonal complement is the null space of $\mathbf{A}^{\top}$.

:::satz Theorem 4.6 (Splitting into two perpendicular parts)
<span class="anker" id="satz-4-6"></span>

If $\mathbf{P}$ is the orthogonal projection onto a subspace $\mathcal U$ of $\mathbb{R}^n$, then:

<ol class="rm">

<li>

Every vector $\mathbf{y}$ can be written in exactly one way as a sum $\mathbf{y}=\mathbf{u}+\mathbf{z}$ with $\mathbf{u}\in\mathcal U$ and $\mathbf{z}\in\mathcal U^\perp$, namely $\mathbf{u}=\mathbf{P}\mathbf{y}$ and $\mathbf{z}=(\mathbf{I}-\mathbf{P})\mathbf{y}$.

</li>

<li>

$\mathbf{I}-\mathbf{P}$ is the orthogonal projection onto $\mathcal U^\perp$.

</li>

<li>

$\dim\mathcal U^\perp=n-\dim\mathcal U$.

</li>

</ol>
:::

:::beweis Splitting
(i) That $\mathbf{P}\mathbf{y}$ lies in $\mathcal U$ and $\mathbf{y}-\mathbf{P}\mathbf{y}$ is perpendicular to $\mathcal U$ is the definition of the orthogonal projection. If there were a second splitting $\mathbf{y}=\mathbf{u}'+\mathbf{z}'$, then $\mathbf{u}-\mathbf{u}'=\mathbf{z}'-\mathbf{z}$ would be a vector that lies in $\mathcal U$ and at the same time is perpendicular to $\mathcal U$, hence perpendicular to itself. Its squared length is then zero, so it is the zero vector. (ii) $\mathbf{I}-\mathbf{P}$ is symmetric, and $(\mathbf{I}-\mathbf{P})^2=\mathbf{I}-2\mathbf{P}+\mathbf{P}^2=\mathbf{I}-\mathbf{P}$. By (i), its image lies in $\mathcal U^\perp$. Every $\mathbf{z}\in\mathcal U^\perp$ stays fixed: $\mathbf{P}\mathbf{z}$ lies in $\mathcal U$ and is at the same time the difference $\mathbf{z}-(\mathbf{z}-\mathbf{P}\mathbf{z})$ of two vectors that are perpendicular to $\mathcal U$; so $\mathbf{P}\mathbf{z}$ is perpendicular to itself and equals $\mathbf{0}$. (iii) If you choose a basis of $\mathcal U$ as the columns of a matrix $\mathbf{A}$, then $\mathcal U^\perp$ is the null space of $\mathbf{A}^{\top}$. By the rank–nullity theorem from Part 1, Section 13.5, it has dimension $n-\operatorname{rank}\mathbf{A}^{\top}=n-\operatorname{rank}\mathbf{A}=n-\dim\mathcal U$.
:::

⁠**Worked example:** The plane of $\mathbf{H}$ has dimension $2$, so its orthogonal complement in $\mathbb{R}^3$ has dimension $1$: it is the line in the direction of the normal vector $\mathbf{k}=(1,\,1,\,-1)^{\top}$. Indeed, $\mathbf{H}^{\top}\mathbf{k}=(1-1,\ 1-1)^{\top}=\mathbf{0}$. We have

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&1&-1\\1&1&-1\\-1&-1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}},$$

the projection onto this line. For $\mathbf{y}=(1,\,1,\,1)^{\top}$, $(\mathbf{I}-\mathbf{P})\mathbf{y}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$, the residual from the previous section.

⁠**In short:** The orthogonal complement $\mathcal U^\perp$ contains all vectors perpendicular to $\mathcal U$; every vector splits uniquely into a part in $\mathcal U$ and a part in $\mathcal U^\perp$, and the dimensions add up to $n$.

### The Gram–Schmidt process

<span class="anker" id="stufe-4-5"></span>

Orthonormal columns make everything simple, but the columns we are given are usually arbitrary. From linearly independent vectors $\mathbf{a}_1,\dots,\mathbf{a}_k$, the Gram–Schmidt process builds orthonormal vectors $\mathbf{q}_1,\dots,\mathbf{q}_k$ that span the same subspace.

Fig. [11](#abb-11) shows the idea for two vectors. You normalize the first. From the second you subtract its shadow on the first, that is, its projection. What remains is perpendicular to the first, and you normalize it. From the third vector you subtract its shadows on the two vectors already found, and so on.

:::abbildung ml/k2gramschmidt 11
The Gram–Schmidt process for $\mathbf{a}_1=(2,1)^{\top}$ and $\mathbf{a}_2=(1,2)^{\top}$. First $\mathbf{a}_1$ is normalized: $\mathbf{q}_1=\mathbf{a}_1/\sqrt5$. From the second vector, its shadow $(\mathbf{q}_1^{\top}\mathbf{a}_2)\,\mathbf{q}_1=(1.6,\,0.8)^{\top}$ is subtracted (blue). The remainder $\tilde{\mathbf{q}}_2=(-0.6,\,1.2)^{\top}$ (orange, parallel to the dashed perpendicular) is perpendicular to $\mathbf{q}_1$; normalized, it gives $\mathbf{q}_2=(-1,2)^{\top}/\sqrt5$.
:::

:::definition Definition 4.7 (Gram–Schmidt process)
<span class="anker" id="satz-4-7"></span>

Let linearly independent vectors $\mathbf{a}_1,\dots,\mathbf{a}_k\in\mathbb{R}^n$ be given. For $i=1,\dots,k$ in turn, the __Gram–Schmidt process__ computes

<span class="anker" id="gl-4-4"></span>
$$\tilde{\mathbf{q}}_i=\mathbf{a}_i-\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l,\qquad \mathbf{q}_i=\frac{\tilde{\mathbf{q}}_i}{\lVert\tilde{\mathbf{q}}_i\rVert} . \tag{4.4}$$
:::

For $i=1$ the sum is empty, so $\tilde{\mathbf{q}}_1=\mathbf{a}_1$. By [(4.2)](#gl-4-2), the sum is the projection of $\mathbf{a}_i$ onto the span of the vectors already found; $\tilde{\mathbf{q}}_i$ is the residual of this projection.

:::satz Theorem 4.8 (What Gram–Schmidt delivers)
<span class="anker" id="satz-4-8"></span>

The vectors $\mathbf{q}_1,\dots,\mathbf{q}_k$ are orthonormal, and for every $i$, the vectors $\mathbf{q}_1,\dots,\mathbf{q}_i$ span the same subspace as $\mathbf{a}_1,\dots,\mathbf{a}_i$.
:::

:::beweis Gram–Schmidt
Proceed step by step. Suppose $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ are already orthonormal and span the same subspace as $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$. Then $\tilde{\mathbf{q}}_i$ is the residual of the projection of $\mathbf{a}_i$ onto this subspace and is therefore perpendicular to $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$; computed directly, $\mathbf{q}_l^{\top}\tilde{\mathbf{q}}_i=\mathbf{q}_l^{\top}\mathbf{a}_i-\mathbf{q}_l^{\top}\mathbf{a}_i=0$. We have $\tilde{\mathbf{q}}_i\ne\mathbf{0}$, because otherwise $\mathbf{a}_i$ would be a linear combination of $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$ and hence of $\mathbf{a}_1,\dots,\mathbf{a}_{i-1}$, contradicting independence. So we may normalize. Finally, $\mathbf{a}_i=\tilde{\mathbf{q}}_i+\sum_l(\mathbf{q}_l^{\top}\mathbf{a}_i)\mathbf{q}_l$ is a linear combination of $\mathbf{q}_1,\dots,\mathbf{q}_i$, and conversely $\mathbf{q}_i$ is a linear combination of $\mathbf{a}_i$ and $\mathbf{q}_1,\dots,\mathbf{q}_{i-1}$. So both lists span the same subspace.
:::

If the given vectors are dependent after all, the process notices this by itself: at some point $\tilde{\mathbf{q}}_i=\mathbf{0}$, and you cannot normalize.

⁠**Worked example:** For the columns of $\mathbf{H}$, $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ and $\mathbf{a}_2=(0,\,1,\,1)^{\top}$, we get $\mathbf{q}_1=\mathbf{a}_1/\sqrt2$. Then $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$ and

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\frac1{\sqrt2}\,\mathbf{q}_1=(0,\,1,\,1)^{\top}-\tfrac12(1,\,0,\,1)^{\top}=\bigl(-\tfrac12,\,1,\,\tfrac12\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{\tfrac14+1+\tfrac14}=\sqrt{\tfrac32} .$$

Normalized, $\mathbf{q}_2=\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}$, exactly the orthonormal basis from the worked example for [(4.2)](#gl-4-2). Fig. [12](#abb-12) shows the two sums of this worked example.

:::abbildung ml/k2rgs 12
Gram–Schmidt for the columns of $\mathbf{H}$: the dot product $\mathbf{q}_1^{\top}\mathbf{a}_2$ with $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$ and $\mathbf{a}_2=(0,1,1)^{\top}$, which gives the length of the shadow, and the squared length of the remainder $\tilde{\mathbf{q}}_2=(-\tfrac12,1,\tfrac12)^{\top}$.
:::

⁠**In short:** Gram–Schmidt subtracts from each vector its projection onto the vectors already found and normalizes the remainder; this produces an orthonormal basis of the same subspace.

:::hintergrund Cost and rounding errors
For $k$ vectors with $n$ components each, the process needs about $2nk^2$ arithmetic operations: in step $i$, $i-1$ dot products have to be computed and just as many multiples subtracted, each of these costs about $2n$, and the sum over $i$ grows like $k^2$. With rounded numbers, the version [(4.4)](#gl-4-4) is sensitive: if two of the given vectors are almost parallel, $\tilde{\mathbf{q}}_i$ is a small difference of large numbers, and the computed $\mathbf{q}_i$ are then no longer exactly orthogonal. A slightly different order of the computational steps, the modified Gram–Schmidt process, subtracts the shadows one at a time from the already reduced remainder instead of subtracting all of them from the original $\mathbf{a}_i$. With exact numbers it gives the same result; with rounded numbers it is considerably more accurate. Software libraries mostly use yet other methods, which work with reflections, that is, with orthogonal matrices.
:::

### The QR decomposition

<span class="anker" id="stufe-4-6"></span>

The Gram–Schmidt process can be written as a decomposition of a matrix. By the proof above, every vector $\mathbf{a}_i$ is a linear combination of $\mathbf{q}_1,\dots,\mathbf{q}_i$, namely

$$\mathbf{a}_i=\sum_{l=1}^{i-1}(\mathbf{q}_l^{\top}\mathbf{a}_i)\,\mathbf{q}_l+\lVert\tilde{\mathbf{q}}_i\rVert\,\mathbf{q}_i .$$

Only the first $i$ of the vectors $\mathbf{q}_l$ occur in it, not the later ones. That is why writing the coefficients as the columns of a matrix produces a triangular matrix.

:::definition Definition 4.9 (QR decomposition)
<span class="anker" id="satz-4-9"></span>

If $\mathbf{A}\in\mathbb{R}^{m\times n}$ has linearly independent columns, its __QR decomposition__ is the representation

<span class="anker" id="gl-4-5"></span>
$$\mathbf{A}=\mathbf{Q}\mathbf{R} \tag{4.5}$$

with a matrix $\mathbf{Q}\in\mathbb{R}^{m\times n}$ with orthonormal columns and an upper triangular matrix $\mathbf{R}\in\mathbb{R}^{n\times n}$ with positive diagonal entries. Here $r_{li}=\mathbf{q}_l^{\top}\mathbf{a}_i$ for $l<i$ and $r_{ii}=\lVert\tilde{\mathbf{q}}_i\rVert$.
:::

An upper triangular matrix has only zeros below the diagonal. By the column view, column $i$ of $\mathbf{Q}\mathbf{R}$ is $\sum_lr_{li}\mathbf{q}_l$, which is exactly the representation of $\mathbf{a}_i$ above. The Gram–Schmidt process delivers the columns of $\mathbf{Q}$, and the entries of $\mathbf{R}$ come out as a by-product. Because $\mathbf{Q}$ has orthonormal columns, we also have $\mathbf{R}=\mathbf{Q}^{\top}\mathbf{A}$.

⁠**Worked example:** For $\mathbf{H}$,

$$\mathbf{Q}=\begin{pmatrix}\tfrac1{\sqrt2}&-\tfrac1{\sqrt6}\\0&\tfrac2{\sqrt6}\\\tfrac1{\sqrt2}&\tfrac1{\sqrt6}\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&\tfrac1{\sqrt2}\\0&\sqrt{\tfrac32}\end{pmatrix}\approx\begin{pmatrix}1.414&0.707\\0&1.225\end{pmatrix}.$$

Check of the second column: $\tfrac1{\sqrt2}\cdot\tfrac1{\sqrt2}(1,\,0,\,1)^{\top}+\sqrt{\tfrac32}\cdot\tfrac1{\sqrt6}(-1,\,2,\,1)^{\top}=\tfrac12(1,\,0,\,1)^{\top}+\tfrac12(-1,\,2,\,1)^{\top}=(0,\,1,\,1)^{\top}=\mathbf{a}_2$.

⁠**In short:** The QR decomposition $\mathbf{A}=\mathbf{Q}\mathbf{R}$ writes the Gram–Schmidt process as a matrix product: $\mathbf{Q}$ has orthonormal columns, $\mathbf{R}$ is an upper triangular matrix.

### The best approximate solution with QR

<span class="anker" id="stufe-4-7"></span>

With the QR decomposition, the normal equations can be solved without computing $\mathbf{A}^{\top}\mathbf{A}$. Substitute $\mathbf{A}=\mathbf{Q}\mathbf{R}$ and use $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$.

:::satz Theorem 4.10 (Best approximate solution with QR)
<span class="anker" id="satz-4-10"></span>

If $\mathbf{A}=\mathbf{Q}\mathbf{R}$ is the QR decomposition, then the best approximate solution of $\mathbf{A}\mathbf{x}=\mathbf{y}$ is the solution of

<span class="anker" id="gl-4-6"></span>
$$\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y} . \tag{4.6}$$
:::

:::beweis Solving with QR
We have $\mathbf{A}^{\top}\mathbf{A}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{R}^{\top}\mathbf{R}$ and $\mathbf{A}^{\top}\mathbf{y}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$. So the normal equations read $\mathbf{R}^{\top}\mathbf{R}\hat{\mathbf{x}}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{y}$. The triangular matrix $\mathbf{R}$ has positive diagonal entries, so by Part 1, Section 14.4, its determinant is nonzero, and it is invertible; so is $\mathbf{R}^{\top}$. Multiplying from the left by $(\mathbf{R}^{\top})^{-1}$ leaves [(4.6)](#gl-4-6).
:::

The system [(4.6)](#gl-4-6) is triangular and is solved from the bottom up, like the back substitution at the end of Gaussian elimination in Part 1, Section 12.3. For an $m\times n$ matrix, the whole procedure costs about $2mn^2$ arithmetic operations, almost all of them for the QR decomposition.

⁠**Worked example:** For $\mathbf{H}$ and $\mathbf{y}=(1,\,1,\,1)^{\top}$, $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac2{\sqrt2},\ \tfrac{-1+2+1}{\sqrt6}\bigr)^{\top}=\bigl(\sqrt2,\ \tfrac2{\sqrt6}\bigr)^{\top}$. The bottom row of [(4.6)](#gl-4-6) reads $\sqrt{\tfrac32}\,\hat x_2=\tfrac2{\sqrt6}$, so $\hat x_2=\tfrac2{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac23$. The top row reads $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac23=\sqrt2$, so $\hat x_1=1-\tfrac13=\tfrac23$. This is the same solution as with the normal equations. The components of $\mathbf{Q}^{\top}\mathbf{y}$ are the dot products in Fig. [13](#abb-13).

:::abbildung ml/k2rqr 13
The right-hand side $\mathbf{Q}^{\top}\mathbf{y}$ of the triangular system for $\mathbf{y}=(1,1,1)^{\top}$, with $\mathbf{q}_1=(1,0,1)^{\top}/\sqrt2$ and $\mathbf{q}_2=(-1,2,1)^{\top}/\sqrt6$.
:::

⁠**In short:** With $\mathbf{A}=\mathbf{Q}\mathbf{R}$, the normal equations turn into the triangular system $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$; the matrix $\mathbf{A}^{\top}\mathbf{A}$ is never formed.

:::aufgabe Exercise 11 ★ Gram–Schmidt and projection
<span class="anker" id="aufg-11"></span>

Let $\mathbf{a}_1=(1,\,1,\,0)^{\top}$ and $\mathbf{a}_2=(1,\,0,\,1)^{\top}$.

<ol class="al">

<li>

Apply the Gram–Schmidt process and check that $\mathbf{q}_1,\mathbf{q}_2$ are orthonormal.

</li>

<li>

Compute the projection matrix $\mathbf{P}=\mathbf{q}_1\mathbf{q}_1^{\top}+\mathbf{q}_2\mathbf{q}_2^{\top}$ onto the plane spanned by $\mathbf{a}_1$ and $\mathbf{a}_2$, and project $\mathbf{y}=(1,\,2,\,3)^{\top}$.

</li>

<li>

Find a vector that spans the orthogonal complement of the plane, and check $\mathbf{I}-\mathbf{P}=\mathbf{k}\mathbf{k}^{\top}/(\mathbf{k}^{\top}\mathbf{k})$.

</li>

</ol>

:::loesung
(a) $\mathbf{q}_1=\mathbf{a}_1/\sqrt2=(1,\,1,\,0)^{\top}/\sqrt2$. Then $\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$ and

$$\tilde{\mathbf{q}}_2=\mathbf{a}_2-\tfrac1{\sqrt2}\,\mathbf{q}_1=(1,\,0,\,1)^{\top}-\tfrac12(1,\,1,\,0)^{\top}=\bigl(\tfrac12,\,-\tfrac12,\,1\bigr)^{\top},\qquad \lVert\tilde{\mathbf{q}}_2\rVert^2=\tfrac14+\tfrac14+1=\tfrac32 ,$$

so $\mathbf{q}_2=\tilde{\mathbf{q}}_2/\sqrt{3/2}=(1,\,-1,\,2)^{\top}/\sqrt6$. Check: $\mathbf{q}_1^{\top}\mathbf{q}_2=(1-1+0)/\sqrt{12}=0$, $\lVert\mathbf{q}_2\rVert^2=\tfrac{1+1+4}6=1$.

(b)

$$\mathbf{P}=\frac12\begin{pmatrix}1&1&0\\1&1&0\\0&0&0\end{pmatrix}+\frac16\begin{pmatrix}1&-1&2\\-1&1&-2\\2&-2&4\end{pmatrix}=\frac13\begin{pmatrix}2&1&1\\1&2&-1\\1&-1&2\end{pmatrix},$$

$$\mathbf{P}\mathbf{y}=\frac13\begin{pmatrix}2+2+3\\1+4-3\\1-2+6\end{pmatrix}=\begin{pmatrix}7/3\\2/3\\5/3\end{pmatrix}.$$

(c) We are looking for $\mathbf{k}$ with $\mathbf{a}_1^{\top}\mathbf{k}=k_1+k_2=0$ and $\mathbf{a}_2^{\top}\mathbf{k}=k_1+k_3=0$, so $\mathbf{k}=(1,\,-1,\,-1)^{\top}$ or a multiple of it. We have $\mathbf{k}^{\top}\mathbf{k}=3$ and

$$\mathbf{I}-\mathbf{P}=\frac13\begin{pmatrix}1&-1&-1\\-1&1&1\\-1&1&1\end{pmatrix}=\frac{\mathbf{k}\mathbf{k}^{\top}}{\mathbf{k}^{\top}\mathbf{k}} .$$

The orthogonal complement of the plane is the line in the direction of $\mathbf{k}$, with dimension $3-2=1$. As a check: $\mathbf{y}-\mathbf{P}\mathbf{y}=(-\tfrac43,\,\tfrac43,\,\tfrac43)^{\top}=-\tfrac43\mathbf{k}$ lies on it.
:::
:::

:::aufgabe Exercise 12 ★★ Solving with QR
<span class="anker" id="aufg-12"></span>

Use the matrix $\mathbf{A}$ with the columns $\mathbf{a}_1$ and $\mathbf{a}_2$ from Exercise [11](#aufg-11).

<ol class="al">

<li>

Give the QR decomposition and check $\mathbf{Q}\mathbf{R}=\mathbf{A}$.

</li>

<li>

Solve $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$ in the least-squares sense with [(4.6)](#gl-4-6) and, as a check, with the normal equations.

</li>

</ol>

:::loesung
(a) From Exercise [11](#aufg-11): $\mathbf{q}_1=(1,\,1,\,0)^{\top}/\sqrt2$, $\mathbf{q}_2=(1,\,-1,\,2)^{\top}/\sqrt6$, $r_{11}=\lVert\mathbf{a}_1\rVert=\sqrt2$, $r_{12}=\mathbf{q}_1^{\top}\mathbf{a}_2=1/\sqrt2$, $r_{22}=\lVert\tilde{\mathbf{q}}_2\rVert=\sqrt{3/2}$:

$$\mathbf{Q}=\begin{pmatrix}1/\sqrt2&1/\sqrt6\\1/\sqrt2&-1/\sqrt6\\0&2/\sqrt6\end{pmatrix},\qquad \mathbf{R}=\begin{pmatrix}\sqrt2&1/\sqrt2\\0&\sqrt{3/2}\end{pmatrix}.$$

Check: column 1 of $\mathbf{Q}\mathbf{R}$ is $\sqrt2\,\mathbf{q}_1=\mathbf{a}_1$; column 2 is $\tfrac1{\sqrt2}\mathbf{q}_1+\sqrt{\tfrac32}\,\mathbf{q}_2=\tfrac12(1,\,1,\,0)^{\top}+\tfrac12(1,\,-1,\,2)^{\top}=(1,\,0,\,1)^{\top}=\mathbf{a}_2$, because $\sqrt{3/2}/\sqrt6=\tfrac12$.

(b) $\mathbf{Q}^{\top}\mathbf{y}=\bigl(\tfrac3{\sqrt2},\ \tfrac{1-2+6}{\sqrt6}\bigr)^{\top}=\bigl(\tfrac3{\sqrt2},\ \tfrac5{\sqrt6}\bigr)^{\top}$. The lower row of $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$ gives $\hat x_2=\tfrac5{\sqrt6}\cdot\sqrt{\tfrac23}=\tfrac53$, the upper row $\sqrt2\,\hat x_1+\tfrac1{\sqrt2}\cdot\tfrac53=\tfrac3{\sqrt2}$; multiplied by $\sqrt2$, this is $2\hat x_1+\tfrac53=3$, so $\hat x_1=\tfrac23$. Check with the normal equations: $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$, $\mathbf{A}^{\top}\mathbf{y}=(3,\,4)^{\top}$, $\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(3,\,4)^{\top}=(\tfrac23,\,\tfrac53)^{\top}$. Moreover, $\mathbf{A}\hat{\mathbf{x}}=(\tfrac73,\,\tfrac23,\,\tfrac53)^{\top}=\mathbf{P}\mathbf{y}$ from Exercise [11](#aufg-11).
:::
:::

:::aufgabe Exercise 13 ★★ Complements
<span class="anker" id="aufg-13"></span>

<ol class="al">

<li>

What is the dimension of the orthogonal complement of a line through the origin in $\mathbb{R}^3$? And of a line in $\mathbb{R}^5$?

</li>

<li>

Show: $(\mathcal U^\perp)^\perp=\mathcal U$. Hint: first show that every vector of $\mathcal U$ lies in $(\mathcal U^\perp)^\perp$. Then split a vector $\mathbf{y}\in(\mathcal U^\perp)^\perp$ as in the theorem in Section [4.4](#stufe-4-4) and take the dot product with its part in $\mathcal U^\perp$.

</li>

</ol>

:::loesung
(a) By the theorem in Section [4.4](#stufe-4-4), $\dim\mathcal U^\perp=n-\dim\mathcal U$: in $\mathbb{R}^3$, therefore, $3-1=2$, a plane; in $\mathbb{R}^5$ it is $5-1=4$.

(b) First part: if $\mathbf{u}\in\mathcal U$, then $\mathbf{u}^{\top}\mathbf{z}=0$ for every $\mathbf{z}\in\mathcal U^\perp$, by the definition of $\mathcal U^\perp$. So $\mathbf{u}$ is perpendicular to all of $\mathcal U^\perp$ and lies in $(\mathcal U^\perp)^\perp$. Second part: let $\mathbf{y}\in(\mathcal U^\perp)^\perp$. By the theorem, split $\mathbf{y}=\mathbf{u}+\mathbf{z}$ with $\mathbf{u}\in\mathcal U$ and $\mathbf{z}\in\mathcal U^\perp$. Then $\mathbf{z}^{\top}\mathbf{y}=0$, because $\mathbf{y}$ is perpendicular to $\mathcal U^\perp$, and $\mathbf{z}^{\top}\mathbf{u}=0$, because $\mathbf{z}$ is perpendicular to $\mathcal U$. Hence $\mathbf{z}^{\top}\mathbf{z}=\mathbf{z}^{\top}\mathbf{y}-\mathbf{z}^{\top}\mathbf{u}=0$, and $\mathbf{z}=\mathbf{0}$. Thus $\mathbf{y}=\mathbf{u}\in\mathcal U$. Each of the two sets contains the other, so they are equal.
:::
:::
