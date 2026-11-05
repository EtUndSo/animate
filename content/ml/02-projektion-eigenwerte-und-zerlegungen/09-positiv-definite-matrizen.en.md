---
title: Positive definite matrices
pfad: Computer Science / Machine Learning / Projection, Eigenvalues and Decompositions
order: 6220900
summary: A quadratic form is a bowl if it is positive everywhere except at the origin.
tags: positive definite, positive semidefinite, indefinite, Rayleigh quotient
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
A quadratic form is a bowl if it is positive everywhere except at the origin. This section gives this property a name and presents tests for checking it: via the eigenvalues, via the pivots and via determinants. Two consequences follow: the largest and smallest value of a form on the unit circle, and a decomposition that only bowls have.
:::

### Positive definite and positive semidefinite

<span class="anker" id="stufe-8-1"></span>

The bowl and the trough from Section [5.3](quadratische-formen.html#stufe-5-3) differ in one respect: the bowl is positive everywhere away from the origin, the trough is merely not negative. These two properties have fixed names.

:::definition Definition 8.1 (Positive definite, positive semidefinite)
<span class="anker" id="satz-8-1"></span>

A symmetric matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ is called __positive definite__ if

<span class="anker" id="gl-8-1"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}>0\qquad\text{for all}\ \mathbf{x}\ne\mathbf{0} , \tag{8.1}$$

and __positive semidefinite__ if $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}\ge0$ for all $\mathbf{x}$.
:::

Symmetry is part of the definition. For the quadratic form this is no restriction, since by Section [5.2](quadratische-formen.html#stufe-5-2) only the symmetric part counts anyway. It is needed, however, for the tests in the next subsection to hold. Every positive definite matrix is also positive semidefinite.

⁠**Worked example:** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ is positive definite, because by Section [5.4](quadratische-formen.html#stufe-5-4), $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=5(x_1+0.4x_2)^2+1.2x_2^2$, and this is zero only if $x_2=0$ and then also $x_1=0$. The matrix $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ has the form $x_1^2+4x_1x_2+4x_2^2=(x_1+2x_2)^2\ge0$; it is positive semidefinite but not positive definite, because the form is zero for $\mathbf{x}=(2,\,-1)^{\top}$. Its graph is a trough with the valley floor in the direction of $(2,\,-1)^{\top}$.

⁠**In short:** Positive definite means: the quadratic form is positive away from the origin, a bowl; positive semidefinite means: nowhere negative.

### The eigenvalue test

<span class="anker" id="stufe-8-2"></span>

The principal axis form [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4) answers the question at once: a sum $\sum_i\lambda_ic_i^2$ is positive for every choice of coordinates that are not all zero if all $\lambda_i$ are positive, and otherwise not.

:::satz Theorem 8.2 (Eigenvalue test)
<span class="anker" id="satz-8-2"></span>

A symmetric matrix is positive definite if and only if all its eigenvalues are positive, and positive semidefinite if and only if none of them is negative.
:::

:::beweis Eigenvalue test
If all $\lambda_i>0$ and $\mathbf{x}\ne\mathbf{0}$, then also $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}\ne\mathbf{0}$, because $\mathbf{Q}$ is invertible; by [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4), $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2>0$. Conversely, if an eigenvalue $\lambda_i\le0$, then for the eigenvector $\mathbf{x}=\mathbf{q}_i$ the form is $\mathbf{q}_i^{\top}\mathbf{A}\mathbf{q}_i=\lambda_i\le0$, and $\mathbf{A}$ is not positive definite. For semidefinite, proceed in the same way, with $\ge$ instead of $>$.
:::

If a symmetric matrix has positive and negative eigenvalues, its form is positive in some directions and negative in others: a saddle. Such a matrix is called __indefinite__. Correspondingly, a matrix with only negative eigenvalues is called negative definite; its form is a dome.

⁠**Worked example:** $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ has the eigenvalues $6$ and $1$: positive definite. $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ has the eigenvalues $5$ and $0$: positive semidefinite. $\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ has only positive entries, but the eigenvalues $4$ and $-2$: indefinite, because for $\mathbf{x}=(1,\,-1)^{\top}$ the form is $1-6+1=-4$. So positive entries say nothing about definiteness.

⁠**In short:** A symmetric matrix is positive definite if and only if all eigenvalues are positive; positive and negative eigenvalues together give a saddle.

:::hintergrund Why symmetry is part of the definition
Some books define positive definite via the quadratic form, others via the eigenvalues. For symmetric matrices this is the same thing by the theorem; for non-symmetric ones it is not. The matrix $\bigl(\begin{smallmatrix}2&-5\\0&2\end{smallmatrix}\bigr)$, being a triangular matrix, has the eigenvalues $2$ and $2$, both positive. Its quadratic form, however, is $2x_1^2-5x_1x_2+2x_2^2$, and for $\mathbf{x}=(1,\,1)^{\top}$ it is $2-5+2=-1$. The reason: the form sees only the symmetric part $\bigl(\begin{smallmatrix}2&-2.5\\-2.5&2\end{smallmatrix}\bigr)$ with the eigenvalues $4.5$ and $-0.5$, whereas the eigenvalues belong to the whole matrix. Anyone who uses the term without symmetry must therefore always say which definition is meant.
:::

### Tests without eigenvalues

<span class="anker" id="stufe-8-3"></span>

Computing eigenvalues is laborious for large matrices. Completing the square from Section [5.4](quadratische-formen.html#stufe-5-4) provides a test without eigenvalues, and a second one with determinants follows from it.

:::satz Theorem 8.3 (Tests for positive definiteness)
<span class="anker" id="satz-8-3"></span>

For a symmetric matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$, the following are equivalent:

<ol class="rm">

<li>

$\mathbf{A}$ is positive definite;

</li>

<li>

Gaussian elimination without row exchanges yields $n$ positive pivots;

</li>

<li>

all leading principal minors are positive: the determinants of the upper left $k\times k$ submatrices are greater than zero for $k=1,\dots,n$.

</li>

</ol>

For $n=2$ and $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$ this means: $a>0$ and $ac-b^2>0$.
:::

For $n=2$ this is [(5.3)](quadratische-formen.html#gl-5-3): the pivots are $a$ and $c-b^2/a$, the form is a bowl if and only if both are positive, and if $a>0$, the condition $c-b^2/a>0$ is equivalent to $ac-b^2>0$. For larger $n$, each elimination step completes the square for one variable, as in the background box in Section [5.4](quadratische-formen.html#stufe-5-4). The determinant of the upper left $k\times k$ submatrix is the product of the first $k$ pivots, so the pivots are all positive if and only if the leading principal minors are. The determinant test is also called Sylvester's criterion.

Two warnings. First, $\det\mathbf{A}>0$ alone is not enough: $\operatorname{diag}(-1,\,-3)$ has the determinant $3$ but is negative definite. Second, the test does not simply carry over to semidefinite: $\operatorname{diag}(0,\,-1)$ has the leading principal minors $0$ and $0$, neither of them negative, and is nevertheless not positive semidefinite.

⁠**Worked example:** For

$$\mathbf{A}=\begin{pmatrix}2&1&0\\1&2&1\\0&1&2\end{pmatrix}$$

the leading principal minors are $2$, $\det\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)=3$ and $\det\mathbf{A}=2\cdot3-1\cdot2=4$, all positive: $\mathbf{A}$ is positive definite. The pivots are $2$, $\tfrac32$ and $\tfrac43$, the quotients of consecutive minors. As a check: the eigenvalues are $2-\sqrt2$, $2$ and $2+\sqrt2$, all positive, and their product is $(4-2)\cdot2=4$.

⁠**In short:** A symmetric matrix is positive definite if and only if all pivots or all leading principal minors are positive; for $2\times2$ this means $a>0$ and $ac-b^2>0$.

### Gram matrices are positive semidefinite

<span class="anker" id="stufe-8-4"></span>

In Part 1, Section 10, the Gram matrices $\mathbf{X}^{\top}\mathbf{X}$ and $\mathbf{X}\mathbf{X}^{\top}$ appeared, and in this chapter $\mathbf{A}^{\top}\mathbf{A}$ appeared in the normal equations. They are always positive semidefinite, and the reason is simple: their quadratic form is a squared length.

:::satz Theorem 8.4 (Gram matrices)
<span class="anker" id="satz-8-4"></span>

For every matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$, the matrix $\mathbf{A}^{\top}\mathbf{A}$ is positive semidefinite. It is positive definite if and only if the columns of $\mathbf{A}$ are linearly independent.
:::

:::beweis Gram matrices
$\mathbf{A}^{\top}\mathbf{A}$ is symmetric, and $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}\mathbf{x})^{\top}(\mathbf{A}\mathbf{x})=\lVert\mathbf{A}\mathbf{x}\rVert^2\ge0$. This is zero exactly when $\mathbf{A}\mathbf{x}=\mathbf{0}$. With independent columns, that happens only for $\mathbf{x}=\mathbf{0}$.
:::

The same holds for $\mathbf{A}\mathbf{A}^{\top}$ with the rows instead of the columns. The theorem explains Section [3.5](die-beste-naherungslosung.html#stufe-3-5) in hindsight: with independent columns, $\mathbf{A}^{\top}\mathbf{A}$ is positive definite, so it has only positive eigenvalues and is invertible.

⁠**Worked example:** $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ has the eigenvalues $3$ and $1$: positive definite, in line with the independent columns of $\mathbf{H}$. For $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, we get $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$ with the determinant $0$ and the eigenvalues $25$ and $0$: positive semidefinite, not positive definite.

⁠**In short:** $\mathbf{A}^{\top}\mathbf{A}$ is always positive semidefinite, because $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf{A}\mathbf{x}\rVert^2$; with independent columns it is positive definite.

### Largest and smallest value on the unit circle

<span class="anker" id="stufe-8-5"></span>

A quadratic form grows with the square of the length of $\mathbf{x}$. How strongly it grows in different directions becomes visible if you only insert vectors of length $1$. In which direction is it largest?

:::satz Theorem 8.5 (Extreme values of a quadratic form)
<span class="anker" id="satz-8-5"></span>

Let $\mathbf{A}$ be symmetric with the smallest eigenvalue $\lambda_{\min}$ and the largest eigenvalue $\lambda_{\max}$. For every vector $\mathbf{x}\ne\mathbf{0}$,

<span class="anker" id="gl-8-2"></span>
$$\lambda_{\min}\le\frac{\mathbf{x}^{\top}\mathbf{A}\mathbf{x}}{\mathbf{x}^{\top}\mathbf{x}}\le\lambda_{\max} . \tag{8.2}$$

The largest value is attained at an eigenvector for $\lambda_{\max}$, the smallest at an eigenvector for $\lambda_{\min}$.
:::

:::beweis Extreme values
With $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$, we have $\mathbf{x}^{\top}\mathbf{x}=\mathbf{c}^{\top}\mathbf{c}=\sum_ic_i^2$, because $\mathbf{Q}$ preserves lengths, and $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2$. So the quotient is

$$\frac{\sum_i\lambda_ic_i^2}{\sum_ic_i^2}=\sum_i\lambda_i\,g_i\qquad\text{with}\qquad g_i=\frac{c_i^2}{\sum_lc_l^2}\ge0,\quad \sum_ig_i=1 .$$

This is a weighted mean of the eigenvalues, and a mean always lies between the smallest and the largest of the averaged values. For $\mathbf{x}=\mathbf{q}_i$, the only nonzero weight is $g_i=1$, and the quotient is $\lambda_i$.
:::

The quotient in [(8.2)](#gl-8-2) is called the __Rayleigh quotient__. For $\lVert\mathbf{x}\rVert=1$ it is the quadratic form itself: on the unit circle, the form lies between the smallest and the largest eigenvalue.

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$, the Rayleigh quotient is $5$ at $\mathbf{e}_1$, $2$ at $\mathbf{e}_2$, $\tfrac{5+4+2}2=5.5$ at $(1,\,1)^{\top}/\sqrt2$ and $\tfrac{5-4+2}2=1.5$ at $(1,\,-1)^{\top}/\sqrt2$. All values lie between $1$ and $6$. It reaches the value $6$ at $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$: $\tfrac15(20+8+2)=6$. The quotient does not depend on the length of $\mathbf{x}$; Fig. [21](#abb-21) computes it for $\mathbf{x}=(1,\,1)^{\top}$ without square roots.

:::abbildung ml/k2rrayleigh 21
The Rayleigh quotient of $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ at the point $\mathbf{x}=(1,1)^{\top}$: numerator and denominator as sums; the quotient $\tfrac{11}2=5.5$ lies between the eigenvalues $1$ and $6$.
:::

⁠**In short:** On the unit circle, a quadratic form lies between the smallest and the largest eigenvalue, and these extreme values are attained in the eigendirections.

### The Cholesky decomposition

<span class="anker" id="stufe-8-6"></span>

Completing the square writes a positive definite form as a sum of squares. If you collect the expressions inside the squares into a vector, the form is the squared length of this vector. This turns into a decomposition of the matrix.

:::satz Theorem 8.6 (Cholesky decomposition)
<span class="anker" id="satz-8-6"></span>

A symmetric matrix $\mathbf{A}$ is positive definite if and only if there is a lower triangular matrix $\mathbf L$ with positive diagonal entries such that

<span class="anker" id="gl-8-3"></span>
$$\mathbf{A}=\mathbf L\mathbf L^{\top} . \tag{8.3}$$

This matrix $\mathbf L$ is unique and is called the Cholesky factor of $\mathbf{A}$.
:::

If $\mathbf{A}=\mathbf L\mathbf L^{\top}$, then $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf L^{\top}\mathbf{x}\rVert^2$, a sum of squares, and because $\mathbf L$ is invertible, it is zero only for $\mathbf{x}=\mathbf{0}$. That is one direction. The other direction, that every positive definite matrix has such a factor, is completing the square: for $n=2$ you read it off from [(5.3)](quadratische-formen.html#gl-5-3),

$$\mathbf L=\begin{pmatrix}\sqrt a&0\\b/\sqrt a&\sqrt{c-b^2/a}\end{pmatrix},$$

and for larger $n$ you continue completing the square variable by variable. By Part 1, Section 14.5, $\det\mathbf{A}=\det\mathbf L\cdot\det\mathbf L^{\top}=(l_{11}\cdots l_{nn})^2$.

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$, we have $a=4$, $b=2$, $c=5$, so $l_{11}=2$, $l_{21}=1$ and $l_{22}=\sqrt{5-1}=2$:

$$\mathbf L=\begin{pmatrix}2&0\\1&2\end{pmatrix},\qquad \mathbf L\mathbf L^{\top}=\begin{pmatrix}4&2\\2&1+4\end{pmatrix}=\mathbf{A} .$$

The form is $4x_1^2+4x_1x_2+5x_2^2=(2x_1+x_2)^2+(2x_2)^2$; the two expressions inside the squares are the components of $\mathbf L^{\top}\mathbf{x}$. The determinant is $20-4=16=(2\cdot2)^2$.

⁠**In short:** Every positive definite matrix is $\mathbf L\mathbf L^{\top}$ with a lower triangular matrix $\mathbf L$; the decomposition is completing the square in matrix form.

:::aufgabe Exercise 24 ★ Checking definiteness
<span class="anker" id="aufg-24"></span>

Use two different tests to decide whether the matrices are positive definite, positive semidefinite, negative definite or indefinite:

$$\mathbf{A}_1=\begin{pmatrix}3&1\\1&2\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}2&6\\6&18\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&2\end{pmatrix},\qquad \mathbf{A}_4=\begin{pmatrix}-2&1\\1&-1\end{pmatrix}.$$

:::loesung
<ul>

<li>

$\mathbf{A}_1$: $a=3>0$ and $ac-b^2=6-1=5>0$: positive definite. Eigenvalues: trace $5$, determinant $5$, $\lambda=\tfrac{5\pm\sqrt5}2\approx3.62$ and $1.38$, both positive.

</li>

<li>

$\mathbf{A}_2$: $a=2>0$, but $ac-b^2=36-36=0$. Eigenvalues $20$ and $0$: positive semidefinite, not definite. Completing the square: $2(x_1+3x_2)^2$, a trough.

</li>

<li>

$\mathbf{A}_3$: $ac-b^2=2-9=-7<0$; the eigenvalues have the product $-7$, so different signs: indefinite. They are $\tfrac{3\pm\sqrt{37}}2\approx4.54$ and $-1.54$.

</li>

<li>

$\mathbf{A}_4$: $a=-2<0$, not positive definite. For $-\mathbf{A}_4=\bigl(\begin{smallmatrix}2&-1\\-1&1\end{smallmatrix}\bigr)$, we have $a=2>0$ and $ac-b^2=1>0$, so $-\mathbf{A}_4$ is positive definite and $\mathbf{A}_4$ is negative definite. Eigenvalues of $\mathbf{A}_4$: trace $-3$, determinant $1$, $\lambda=\tfrac{-3\pm\sqrt5}2\approx-0.38$ and $-2.62$, both negative: a dome.

</li>

</ul>
:::
:::

:::aufgabe Exercise 25 ★★ A trap
<span class="anker" id="aufg-25"></span>

<ol class="al">

<li>

The matrix $\bigl(\begin{smallmatrix}1&-4\\0&1\end{smallmatrix}\bigr)$ has only positive eigenvalues. Is its quadratic form positive? Find a vector that shows the opposite, and explain the contradiction.

</li>

<li>

For which numbers $t$ is $\bigl(\begin{smallmatrix}1&t\\t&4\end{smallmatrix}\bigr)$ positive definite? For which is it positive semidefinite?

</li>

</ol>

:::loesung
(a) The eigenvalues are $1$ and $1$, but at $\mathbf{x}=(1,\,1)^{\top}$ the form $x_1^2-4x_1x_2+x_2^2$ equals $1-4+1=-2<0$. There is no contradiction: the eigenvalue test holds only for symmetric matrices. The form sees only the symmetric part $\bigl(\begin{smallmatrix}1&-2\\-2&1\end{smallmatrix}\bigr)$, and that has the eigenvalues $3$ and $-1$; the form is indefinite.

(b) With the $2\times2$ test: $a=1>0$, and $ac-b^2=4-t^2>0$ exactly for $|t|<2$. For positive semidefinite, you need eigenvalues $\ge0$. Their sum is the trace $5>0$, their product the determinant $4-t^2$; both eigenvalues are $\ge0$ if and only if $4-t^2\ge0$, that is, for $|t|\le2$. At $t=\pm2$ the matrix is positive semidefinite but not definite, with the eigenvalues $5$ and $0$; for $|t|>2$ it is indefinite.
:::
:::

:::aufgabe Exercise 26 ★★ Rayleigh quotient and Cholesky
<span class="anker" id="aufg-26"></span>

Let $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Compute the eigenvalues and the Rayleigh quotient at the points $\mathbf{e}_1$, $\mathbf{e}_2$ and $(1,\,1)^{\top}$. Check [(8.2)](#gl-8-2).

</li>

<li>

Solve $\mathbf{A}\mathbf{x}=(2,\,9)^{\top}$ with the Cholesky factor: first $\mathbf L\mathbf{z}=(2,\,9)^{\top}$ from top to bottom, then $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$ from bottom to top.

</li>

</ol>

:::loesung
(a) Trace $9$, determinant $16$: $\lambda=\tfrac{9\pm\sqrt{81-64}}2=\tfrac{9\pm\sqrt{17}}2\approx6.56$ and $2.44$. The Rayleigh quotient is $4$ at $\mathbf{e}_1$, $5$ at $\mathbf{e}_2$, and $\tfrac{4+2+2+5}2=\tfrac{13}2=6.5$ at $(1,\,1)^{\top}$. All three lie between $2.44$ and $6.56$; the third lies close to the maximum, because $(1,\,1)^{\top}$ points almost in the direction of the eigenvector for the larger eigenvalue.

(b) From Section [8.6](#stufe-8-6): $\mathbf L=\bigl(\begin{smallmatrix}2&0\\1&2\end{smallmatrix}\bigr)$. From top to bottom: $2z_1=2$, so $z_1=1$; $z_1+2z_2=9$, so $z_2=4$. Then $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$ from bottom to top: $2x_2=4$, so $x_2=2$; $2x_1+x_2=1$, so $x_1=-\tfrac12$. Check: $\mathbf{A}(-\tfrac12,\,2)^{\top}=(-2+4,\ -1+10)^{\top}=(2,\,9)^{\top}$. Two triangular systems replace a general system of equations.
:::
:::
