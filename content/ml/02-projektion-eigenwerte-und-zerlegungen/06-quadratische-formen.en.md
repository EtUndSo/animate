---
title: Quadratic forms
pfad: Computer Science / Machine Learning / Mathematical Foundations / Projection, Eigenvalues and Decompositions
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Chapter 2: Projection, Eigenvalues and Decompositions
nachschlagen: ja
order: 15220600
summary: After the linear functions, the quadratic ones are the simplest functions of several variables.
tags: quadratic form
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
After the linear functions, the quadratic ones are the simplest functions of several variables. They describe squared distances, squared errors and curved surfaces. This section writes them with a matrix, shows the three basic shapes bowl, trough and saddle, and explains how to tell from the matrix which shape you have, as long as it has no cross terms.
:::

### Quadratic forms

<span class="anker" id="stufe-5-1"></span>

In [Chapter 1, Section 8.4](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-4), every linear function with one output was a weighted sum $\mathbf{w}^{\top}\mathbf{x}$ of the components. The next simplest kind of function sums products of two components each: squares such as $x_1^2$ and cross terms such as $x_1x_2$. An example from everyday life is a walk along two straight roads that are not perpendicular to each other. Someone walks $x_1$ km in the direction of the unit vector $\mathbf{u}$ of the first road and then $x_2$ km in the direction of the unit vector $\mathbf{v}$ of the second; negative distances mean the opposite direction. They then stand at $x_1\mathbf{u}+x_2\mathbf{v}$, and by the rules of the dot product the square of their distance from the start is

$$d^2=\lVert x_1\mathbf{u}+x_2\mathbf{v}\rVert^2=x_1^2+2\,(\mathbf{u}^{\top}\mathbf{v})\,x_1x_2+x_2^2 .$$

Such sums can be written with a matrix in the middle.

:::definition Definition 5.1 (Quadratic form)
<span class="anker" id="satz-5-1"></span>

For a square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$, the function

<span class="anker" id="gl-5-1"></span>
$$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^na_{il}\,x_ix_l \tag{5.1}$$

is called the __quadratic form__ of $\mathbf{A}$.
:::

The result is a number: $\mathbf{A}\mathbf{x}$ is a vector, and $\mathbf{x}^{\top}(\mathbf{A}\mathbf{x})$ is the dot product of $\mathbf{x}$ with it. Written out for $n=2$,

$$\mathbf{x}^{\top}\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}\mathbf{x}=a_{11}x_1^2+(a_{12}+a_{21})\,x_1x_2+a_{22}x_2^2 .$$

If you double $\mathbf{x}$, then $f$ quadruples: $f(c\,\mathbf{x})=c^2f(\mathbf{x})$. Hence the name.

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$, $f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$. At the point $\mathbf{x}=(1,\,-1)^{\top}$, $f=5-4+2=3$; as a check, $\mathbf{A}\mathbf{x}=(3,\,0)^{\top}$ and $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=3$. Fig. [14](#abb-14) works out the double sum [(5.1)](#gl-5-1) at this point term by term. At the point $(1,\,1)^{\top}$, $f=11$; at the origin, $f=0$. The squared distance of the walk is $d^2=\mathbf{x}^{\top}\bigl(\begin{smallmatrix}1&\mathbf{u}^{\top}\mathbf{v}\\\mathbf{u}^{\top}\mathbf{v}&1\end{smallmatrix}\bigr)\,\mathbf{x}$ with $\mathbf{x}=(x_1,\,x_2)^{\top}$; the matrix is the Gram matrix of the two directions $\mathbf{u}$ and $\mathbf{v}$ from [Chapter 1, Section 10](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10). If the roads enclose the angle $60^\circ$, then $\mathbf{u}^{\top}\mathbf{v}=\cos60^\circ=\tfrac12$ and $d^2=x_1^2+x_1x_2+x_2^2$: after $1$ km on each of the two roads, you are $\sqrt3\approx1.73$ km from the start.

:::abbildung ml/k2rqf 14
The quadratic form of $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ at the point $\mathbf{x}=(1,-1)^{\top}$ as a double sum: four terms, one for each entry of $\mathbf{A}$.
:::
::::

⁠**In short:** A quadratic form $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ is a sum of squares and mixed products of the components, with the entries of $\mathbf{A}$ as weights.

### Only the symmetric part counts

<span class="anker" id="stufe-5-2"></span>

In the expression for $n=2$, $a_{12}$ and $a_{21}$ occur only as a sum. The matrices $\bigl(\begin{smallmatrix}5&4\\0&2\end{smallmatrix}\bigr)$ and $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ therefore have the same quadratic form. You may always pick the symmetric one.

:::satz Theorem 5.2 (The symmetric part)
<span class="anker" id="satz-5-2"></span>

For every square matrix $\mathbf{A}$ and every $\mathbf{x}$,

<span class="anker" id="gl-5-2"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\Bigl(\frac{\mathbf{A}+\mathbf{A}^{\top}}2\Bigr)\mathbf{x} . \tag{5.2}$$
:::

:::beweis The symmetric part
The number $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ equals its own transpose, so $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})^{\top}=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{x}$. The mean of the two expressions is $\mathbf{x}^{\top}\frac{\mathbf{A}+\mathbf{A}^{\top}}2\mathbf{x}$.
:::

The matrix $\frac12(\mathbf{A}+\mathbf{A}^{\top})$ is symmetric. In this chapter, a quadratic form therefore always has a symmetric matrix. You read it off as follows: the diagonal holds the coefficients of the squares, and each off-diagonal entry holds half the coefficient of the corresponding cross term.

::::beispiel [Worked example]
The form $3x_1^2-6x_1x_2+x_2^2$ has the symmetric matrix $\bigl(\begin{smallmatrix}3&-3\\-3&1\end{smallmatrix}\bigr)$. The form $x_1^2+2x_2^2+4x_3^2+2x_1x_3$ in $\mathbb{R}^3$ has the matrix $\Bigl(\begin{smallmatrix}1&0&1\\0&2&0\\1&0&4\end{smallmatrix}\Bigr)$; the cross term $2x_1x_3$ is split between the entries $(1,3)$ and $(3,1)$.
::::

⁠**In short:** A quadratic form sees only the symmetric part of its matrix; that is why it is always written with a symmetric matrix.

### Bowl, trough and saddle

<span class="anker" id="stufe-5-3"></span>

With two variables you can draw the quadratic form as a surface above the plane, with $f(\mathbf{x})$ as the height, and, as on a map, its contour lines, the lines of equal height. This is easiest when the matrix is a diagonal matrix. Then there are no cross terms, and $f(\mathbf{x})=a_{11}x_1^2+a_{22}x_2^2$. Depending on the signs of the two entries, three basic shapes arise (Fig. [15](#abb-15)).

:::abbildung ml/k2formen 15
Top: the graphs of the quadratic forms $x_1^2+2x_2^2$ (bowl), $x_1^2$ (trough) and $x_1^2-x_2^2$ (saddle) over the square $|x_1|,|x_2|\le1$; bottom: their contour lines. For the bowl they are ellipses ($f=\tfrac14,\tfrac12,1$), for the trough pairs of parallel lines; dashed is the line $x_1=0$, on which the trough has height zero. For the saddle they are hyperbolas, bold for $f=\tfrac14,\tfrac12$ and pale for $f=-\tfrac14,-\tfrac12$; dashed are the two lines with $f=0$.
:::

<ul>

<li>

⁠**Bowl:** Both diagonal entries are positive, for example $f=x_1^2+2x_2^2$. Then $f(\mathbf{x})>0$ for every $\mathbf{x}\ne\mathbf{0}$, and $f=0$ only at the origin. The contour lines are ellipses around the origin, with their semi-axes on the coordinate axes.

</li>

<li>

⁠**Trough:** One entry is positive, the other zero, for example $f=x_1^2$. Then $f\ge0$, but $f=0$ on the entire line $x_1=0$: there the surface has a straight valley floor. The contour lines are pairs of parallel lines.

</li>

<li>

⁠**Saddle:** The entries have different signs, for example $f=x_1^2-x_2^2$. Along the $x_1$-axis the surface rises on both sides; along the $x_2$-axis it falls on both sides. The contour lines are hyperbolas.

</li>

</ul>

If both entries are negative, the bowl is upside down; that is a dome. A negative and a zero entry give an upside-down trough, a ridge. With more than two variables the same holds: the signs of the diagonal entries decide the shape.

::::beispiel [Worked example]
For the bowl $f=x_1^2+2x_2^2$, the contour line $f=1$ is the ellipse with the semi-axes $1$ on the $x_1$-axis and $1/\sqrt2\approx0.707$ on the $x_2$-axis: at $(1,\,0)^{\top}$ and at $(0,\,1/\sqrt2)^{\top}$, $f=1$. For the saddle $f=x_1^2-x_2^2$, $f(1,\,0)=1$, $f(0,\,1)=-1$ and $f(1,\,1)=0$.
::::

⁠**In short:** Without cross terms, you read off the shape from the signs on the diagonal: all positive gives a bowl, positive and zero a trough, mixed signs a saddle.

### Completing the square

<span class="anker" id="stufe-5-4"></span>

With cross terms, you can no longer see the shape right away. Is $5x_1^2+4x_1x_2+2x_2^2$ a bowl? The cross term can become negative. From school you know a tool that removes cross terms: completing the square. It writes the form as a sum of squares, and from the coefficients of the squares you read off the shape as in the previous subsection.

:::herleitung Completing the square in two variables
Let $a\ne0$. Factor $a$ out of the terms containing $x_1$ and complete the square:

$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1^2+\frac{2b}ax_1x_2\Bigr)+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2-\frac{b^2}ax_2^2+cx_2^2 .$$

Hence

<span class="anker" id="gl-5-3"></span>
$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2+\Bigl(c-\frac{b^2}a\Bigr)x_2^2 . \tag{5.3}$$
:::

The right-hand side is a sum of two squares. The new variables $z_1=x_1+\frac bax_2$ and $z_2=x_2$ take on every pair of numbers as $\mathbf{x}$ runs through the plane. So the form in the variables $z_1,z_2$ has no cross terms anymore, and the signs of $a$ and $c-b^2/a$ decide between bowl, trough and saddle.

::::beispiel [Worked example 1]
$5x_1^2+4x_1x_2+2x_2^2$ has $a=5$, $b=2$, $c=2$:

$$5x_1^2+4x_1x_2+2x_2^2=5\,(x_1+0.4\,x_2)^2+1.2\,x_2^2 .$$

Both coefficients are positive: the form is a bowl. Check at $\mathbf{x}=(1,\,-1)^{\top}$: $5\cdot0.36+1.2=3$.
::::

::::beispiel [Worked example 2]
$x_1^2+6x_1x_2+x_2^2=(x_1+3x_2)^2-8x_2^2$. The coefficients have different signs: a saddle. Indeed, $f(1,\,0)=1>0$ and $f(1,\,-1)=1-6+1=-4<0$.
::::

⁠**In short:** Completing the square writes a quadratic form as a sum of squares; the signs of the coefficients of the squares show whether it is a bowl, a trough or a saddle.

:::hintergrund Completing the square is Gaussian elimination
The numbers in [(5.3)](#gl-5-3) are the same as in Gaussian elimination from [Chapter 1, Section 12.3](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-gleichungssysteme.html#stufe-12-3), applied to the symmetric matrix $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$. To produce a zero below the diagonal, you subtract $\frac ba$ times the first row from the second and obtain $\bigl(\begin{smallmatrix}a&b\\0&c-b^2/a\end{smallmatrix}\bigr)$. The diagonal entries of this echelon form, the so-called pivots, are exactly the coefficients of the squares, and the elimination factor $\frac ba$ appears in the first parenthesis. For the matrix $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$: factor $0.4$, pivots $5$ and $1.2$. With $n$ variables you continue in the same way: each elimination step completes the square for one variable. The form is a bowl if and only if all pivots are positive. By the rules from [Chapter 1, Section 14.5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), the product of the pivots is the determinant, here $5\cdot1.2=6=5\cdot2-2\cdot2$.
:::

:::aufgabe Exercise 14 ★ Forms and matrices
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Give the symmetric matrix of the forms $2x_1^2-2x_1x_2+3x_2^2$ and $x_1x_2$.

</li>

<li>

Compute the form of $\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)$ and its symmetric matrix.

</li>

<li>

Determine without calculation whether $3x_1^2+x_2^2$, $-x_1^2$ and $2x_1^2-x_2^2+x_3^2$ are a bowl, a trough, a saddle or something else.

</li>

</ol>

:::loesung
(a) The diagonal holds the coefficients of the squares, the off-diagonal entries half the coefficient of the cross term: $2x_1^2-2x_1x_2+3x_2^2$ has the matrix $\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$, and $x_1x_2$ has $\bigl(\begin{smallmatrix}0&1/2\\1/2&0\end{smallmatrix}\bigr)$.

(b) $\mathbf{x}^{\top}\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)\mathbf{x}=x_1^2+(3-1)\,x_1x_2+2x_2^2=x_1^2+2x_1x_2+2x_2^2$. The symmetric matrix is $\tfrac12(\mathbf{A}+\mathbf{A}^{\top})=\bigl(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\bigr)$.

(c) $3x_1^2+x_2^2$: both coefficients positive, a bowl. $-x_1^2$: one negative and one vanishing coefficient, so an upside-down trough, a ridge along the $x_2$-axis. $2x_1^2-x_2^2+x_3^2$: mixed signs, a saddle; along $x_1$ and $x_3$ the form rises, along $x_2$ it falls.
:::
:::

:::aufgabe Exercise 15 ★★ Completing the square
<span class="anker" id="aufg-15"></span>

Complete the square and determine the shape:

$$f_1=2x_1^2+8x_1x_2+11x_2^2,\qquad f_2=x_1^2+4x_1x_2+4x_2^2,\qquad f_3=x_1^2+4x_1x_2+x_2^2 .$$

For the trough, give the line on which $f=0$, and for the saddle, a point with $f<0$.

:::loesung
With [(5.3)](#gl-5-3):

<ul>

<li>

$f_1$: $a=2$, $b=4$, $c=11$, so $f_1=2(x_1+2x_2)^2+(11-8)\,x_2^2=2(x_1+2x_2)^2+3x_2^2$. Both coefficients positive: a bowl.

</li>

<li>

$f_2=(x_1+2x_2)^2+0\cdot x_2^2$: a trough. It is zero on the line $x_1+2x_2=0$, that is, in the direction of $(2,\,-1)^{\top}$.

</li>

<li>

$f_3=(x_1+2x_2)^2-3x_2^2$: different signs, a saddle. If you choose $x_2=1$ and $x_1=-2$, the first square vanishes: $f_3(-2,\,1)=4-8+1=-3<0$.

</li>

</ul>
:::
:::

:::aufgabe Exercise 16 ★★ Two roads
<span class="anker" id="aufg-16"></span>

For the walk along two straight roads with the directions $\mathbf{u}$ and $\mathbf{v}$ from Subsection [5.1](#stufe-5-1), $d^2=x_1^2+2\,(\mathbf{u}^{\top}\mathbf{v})\,x_1x_2+x_2^2$.

<ol class="al">

<li>

Complete the square in $d^2$.

</li>

<li>

For which values of $\mathbf{u}^{\top}\mathbf{v}$ is $d^2>0$ for all distances $(x_1,\,x_2)\ne(0,\,0)$? Why can $|\mathbf{u}^{\top}\mathbf{v}|$ never be greater than $1$ by the Cauchy–Schwarz inequality from [Chapter 1, Section 5.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-1), and what does $|\mathbf{u}^{\top}\mathbf{v}|=1$ mean for the two roads?

</li>

</ol>

:::loesung
(a) In [(5.3)](#gl-5-3), $a=1$, $b=\mathbf{u}^{\top}\mathbf{v}$ and $c=1$, so $b/a=\mathbf{u}^{\top}\mathbf{v}$ and $b^2/a=(\mathbf{u}^{\top}\mathbf{v})^2$:

$$d^2=\bigl(x_1+(\mathbf{u}^{\top}\mathbf{v})\,x_2\bigr)^2+\bigl(1-(\mathbf{u}^{\top}\mathbf{v})^2\bigr)\,x_2^2 .$$

(b) The first coefficient is $a=1>0$. $d^2>0$ for all distances $\ne(0,\,0)$ holds if and only if the second is positive as well: $1-(\mathbf{u}^{\top}\mathbf{v})^2>0$, so $|\mathbf{u}^{\top}\mathbf{v}|<1$. By the Cauchy–Schwarz inequality, $|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert=1$, with equality if and only if $\mathbf{v}=\pm\mathbf{u}$: when the two roads run parallel. Then the form would only be a trough: for $x_1=-(\mathbf{u}^{\top}\mathbf{v})\,x_2$, for instance $1$ km out and $1$ km back, you are standing at the start again. For two roads that really cross, $|\mathbf{u}^{\top}\mathbf{v}|<1$, and every walk with $(x_1,\,x_2)\ne(0,\,0)$ ends at a positive distance from the start.
:::
:::
