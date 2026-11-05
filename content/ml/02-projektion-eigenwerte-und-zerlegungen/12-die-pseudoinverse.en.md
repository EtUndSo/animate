---
title: The pseudoinverse
pfad: Computer Science / Machine Learning / Projection, Eigenvalues and Decompositions
order: 6221200
summary: In Part 1, only a square matrix with independent columns had an inverse.
tags: left inverse, right inverse, pseudoinverse
lang: en
---

<span class="anker" id="stufe-11"></span>

:::zweck
In Part 1, only a square matrix with independent columns had an inverse. This section gives every matrix a kind of inverse: one that inverts from the left when there are more equations than unknowns, one that inverts from the right when there are fewer, and one for all cases, the pseudoinverse. It always delivers the best approximate solution and, among several, the shortest.
:::

### Left inverses

<span class="anker" id="stufe-11-1"></span>

A tall matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ with $m>n$ has no inverse; it is not even square. It can, however, have half of the property of an inverse.

:::definition Definition 11.1 (Left inverse)
<span class="anker" id="satz-11-1"></span>

A matrix $\mathbf F\in\mathbb{R}^{n\times m}$ with $\mathbf F\mathbf{A}=\mathbf{I}_n$ is called a __left inverse__ of $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

:::satz Theorem 11.2 (Left inverse)
<span class="anker" id="satz-11-2"></span>

$\mathbf{A}$ has a left inverse if and only if its columns are linearly independent. Then

<span class="anker" id="gl-11-1"></span>
$$\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top} \tag{11.1}$$

is a left inverse, and $\mathbf F\mathbf{y}$ is the best approximate solution of $\mathbf{A}\mathbf{x}=\mathbf{y}$.
:::

:::beweis Left inverse
If the columns are independent, then $\mathbf{A}^{\top}\mathbf{A}$ is invertible by Section [3.5](die-beste-naherungslosung.html#stufe-3-5), and $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{A}=\mathbf{I}$. By [(3.5)](die-beste-naherungslosung.html#gl-3-5), $\mathbf F\mathbf{y}=\hat{\mathbf{x}}$. Conversely: if $\mathbf{A}$ has a left inverse and $\mathbf{A}\mathbf{x}=\mathbf{0}$, then $\mathbf{x}=\mathbf F\mathbf{A}\mathbf{x}=\mathbf F\mathbf{0}=\mathbf{0}$; so the null space is $\{\mathbf{0}\}$, and the columns are independent.
:::

From the right, $\mathbf F$ does not invert. By [(4.1)](projektion-auf-einen-unterraum.html#gl-4-1), the product $\mathbf{A}\mathbf F=\mathbf{A}(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ is the projection onto the column space, and for $m>n$ this is not $\mathbf{I}_m$. Moreover, a tall matrix has many left inverses; [(11.1)](#gl-11-1) is the one that belongs to the orthogonal projection.

⁠**Worked example:** For $\mathbf{H}$ with the columns $(1,\,0,\,1)^{\top}$ and $(0,\,1,\,1)^{\top}$, we have $(\mathbf{H}^{\top}\mathbf{H})^{-1}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$ and

$$\mathbf F=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}1&0&1\\0&1&1\end{pmatrix}=\frac13\begin{pmatrix}2&-1&1\\-1&2&1\end{pmatrix}.$$

We have $\mathbf F\mathbf{H}=\tfrac13\bigl(\begin{smallmatrix}2+1&-1+1\\-1+1&2+1\end{smallmatrix}\bigr)=\mathbf{I}_2$, and $\mathbf F(1,\,1,\,1)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$ is the best approximate solution from Section [3.3](die-beste-naherungslosung.html#stufe-3-3). $\mathbf{H}\mathbf F$ is the projection matrix $\tfrac13\Bigl(\begin{smallmatrix}2&-1&1\\-1&2&1\\1&1&2\end{smallmatrix}\Bigr)$ from Section [4.2](projektion-auf-einen-unterraum.html#stufe-4-2). Another left inverse is $\bigl(\begin{smallmatrix}1&0&0\\0&1&0\end{smallmatrix}\bigr)$, because the first two rows of $\mathbf{H}$ form the identity matrix; for $(1,\,1,\,1)^{\top}$, however, it does not deliver the best approximate solution but $(1,\,1)^{\top}$.

⁠**In short:** A matrix with independent columns has the left inverse $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$; it maps $\mathbf{y}$ to the best approximate solution.

### Right inverses

<span class="anker" id="stufe-11-2"></span>

For a wide matrix with $m<n$ there are fewer equations than unknowns. If the system is solvable, it has infinitely many solutions. A right inverse selects one of them, and a special one at that.

:::definition Definition 11.3 (Right inverse)
<span class="anker" id="satz-11-3"></span>

A matrix $\mathbf G\in\mathbb{R}^{n\times m}$ with $\mathbf{A}\mathbf G=\mathbf{I}_m$ is called a __right inverse__ of $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

:::satz Theorem 11.4 (Right inverse and shortest solution)
<span class="anker" id="satz-11-4"></span>

If the rows of $\mathbf{A}$ are linearly independent, then

<span class="anker" id="gl-11-2"></span>
$$\mathbf G=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1} \tag{11.2}$$

is a right inverse. $\mathbf{x}=\mathbf G\mathbf{y}$ solves $\mathbf{A}\mathbf{x}=\mathbf{y}$ for every $\mathbf{y}$, and among all solutions it has the smallest length.
:::

:::beweis Right inverse
The rows of $\mathbf{A}$ are the columns of $\mathbf{A}^{\top}$; by Section [3.5](die-beste-naherungslosung.html#stufe-3-5), applied to $\mathbf{A}^{\top}$, the matrix $\mathbf{A}\mathbf{A}^{\top}$ is invertible. Then $\mathbf{A}\mathbf G=\mathbf{A}\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}=\mathbf{I}$ and $\mathbf{A}\mathbf G\mathbf{y}=\mathbf{y}$. If $\mathbf{x}$ is any solution, then $\mathbf{A}(\mathbf{x}-\mathbf G\mathbf{y})=\mathbf{0}$, so $\mathbf{z}=\mathbf{x}-\mathbf G\mathbf{y}$ lies in the null space. The vector $\mathbf G\mathbf{y}=\mathbf{A}^{\top}\mathbf{w}$ with $\mathbf{w}=(\mathbf{A}\mathbf{A}^{\top})^{-1}\mathbf{y}$ is perpendicular to every vector of the null space, because $(\mathbf{A}^{\top}\mathbf{w})^{\top}\mathbf{z}=\mathbf{w}^{\top}\mathbf{A}\mathbf{z}=0$. By the Pythagorean theorem,

$$\lVert\mathbf{x}\rVert^2=\lVert\mathbf G\mathbf{y}+\mathbf{z}\rVert^2=\lVert\mathbf G\mathbf{y}\rVert^2+\lVert\mathbf{z}\rVert^2\ge\lVert\mathbf G\mathbf{y}\rVert^2 ,$$

with equality only for $\mathbf{z}=\mathbf{0}$.
:::

Geometrically, the solution set is a line or plane that does not pass through the origin, and $\mathbf G\mathbf{y}$ is its point closest to the origin: the foot of the perpendicular from the origin.

⁠**Worked example:** The single equation $x_1+2x_2=5$ has $\mathbf{A}=(1\ \ 2)$ and $\mathbf{A}\mathbf{A}^{\top}=5$. So $\mathbf G=\tfrac15(1,\,2)^{\top}$ and $\mathbf G\cdot5=(1,\,2)^{\top}$. All solutions are $(1,\,2)^{\top}+t\,(2,\,-1)^{\top}$, with the squared length $(1+2t)^2+(2-t)^2=5+5t^2$; the solution is shortest at $t=0$. The vector $(1,\,2)^{\top}$ is perpendicular to the solution line, whose direction is $(2,\,-1)^{\top}$.

⁠**In short:** A matrix with independent rows has the right inverse $\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}$; it delivers the shortest solution.

### The pseudoinverse

<span class="anker" id="stufe-11-3"></span>

If $\mathbf{A}$ has neither independent columns nor independent rows, both formulas fail. An example is $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ from Section [3.5](die-beste-naherungslosung.html#stufe-3-5): for $\mathbf{y}=(1,\,1)^{\top}$, all points of the line $x_1+2x_2=\tfrac35$ are best approximate solutions. The singular value decomposition provides a formula for every matrix.

:::definition Definition 11.5 (Pseudoinverse)
<span class="anker" id="satz-11-5"></span>

Let $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ with rank $r$. The matrix $\mathbf{D}^+\in\mathbb{R}^{n\times m}$ is obtained from $\mathbf{D}^{\top}$ by replacing each $d_j>0$ by $1/d_j$; the zeros stay. The __pseudoinverse__ of $\mathbf{A}$ is

<span class="anker" id="gl-11-3"></span>
$$\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\sum_{j=1}^r\frac1{d_j}\,\mathbf{v}_j\mathbf{u}_j^{\top} . \tag{11.3}$$
:::

Each building block inverts a building block of $\mathbf{A}$: $\mathbf{A}$ maps $\mathbf{v}_j$ to $d_j\mathbf{u}_j$, and $\mathbf{A}^+$ maps $\mathbf{u}_j$ to $\mathbf{v}_j/d_j$. For the directions $\mathbf{u}_j$ with $j>r$, which $\mathbf{A}$ does not reach, $\mathbf{A}^+$ returns zero instead of dividing by zero. If $\mathbf{A}$ is invertible, then $\mathbf{A}^+=\mathbf{A}^{-1}$, because then $\mathbf{A}^{-1}=(\mathbf{V}^{\top})^{-1}\mathbf{D}^{-1}\mathbf{U}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$.

⁠**Worked example:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ is symmetric and positive semidefinite with the eigenvalue $5$ for $\mathbf{q}=(1,\,2)^{\top}/\sqrt5$ and the eigenvalue $0$. By Section [9.7](die-singularwertzerlegung.html#stufe-9-7), $\mathbf{A}=5\,\mathbf{q}\mathbf{q}^{\top}$ is its compact decomposition, with $d_1=5$ and $\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$. Hence

$$\mathbf{A}^+=\frac15\,\mathbf{q}\mathbf{q}^{\top}=\frac1{25}\begin{pmatrix}1&2\\2&4\end{pmatrix}.$$

⁠**In short:** The pseudoinverse $\mathbf{A}^+=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}$ inverts every building block $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ with $d_j>0$ and maps the directions for the singular value $0$ to zero.

### The shortest best approximate solution

<span class="anker" id="stufe-11-4"></span>

What does $\mathbf{A}^+\mathbf{y}$ achieve? It combines the two previous subsections.

:::satz Theorem 11.6 (Pseudoinverse and least squares)
<span class="anker" id="satz-11-6"></span>

For every matrix $\mathbf{A}$ and every vector $\mathbf{y}$, the vector $\mathbf{x}^+=\mathbf{A}^+\mathbf{y}$ is a best approximate solution of $\mathbf{A}\mathbf{x}=\mathbf{y}$, and among all best approximate solutions it has the smallest length. In particular,

$$\begin{gathered} \mathbf{A}^+=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\quad\text{for independent columns},\\ \mathbf{A}^+=\mathbf{A}^{\top}(\mathbf{A}\mathbf{A}^{\top})^{-1}\quad\text{for independent rows}. \end{gathered}$$
:::

:::beweis Pseudoinverse
Compute in the coordinates of the singular vectors: $\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$ and $\boldsymbol\beta=\mathbf{U}^{\top}\mathbf{y}$. Because $\mathbf{U}^{\top}$ preserves lengths,

$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{U}^{\top}\mathbf{y}-\mathbf{D}\mathbf{V}^{\top}\mathbf{x}\rVert^2=\lVert\boldsymbol\beta-\mathbf{D}\mathbf{c}\rVert^2=\sum_{j=1}^r(\beta_j-d_jc_j)^2+\sum_{j=r+1}^m\beta_j^2 .$$

The second sum does not depend on $\mathbf{x}$. The first is zero, and thus as small as possible, exactly when $c_j=\beta_j/d_j$ for all $j\le r$; the $c_j$ with $j>r$ do not appear at all. So the best approximate solutions are exactly the $\mathbf{x}=\mathbf{V}\mathbf{c}$ with $c_j=\beta_j/d_j$ for $j\le r$ and arbitrary $c_{r+1},\dots,c_n$. Their length is $\lVert\mathbf{x}\rVert^2=\lVert\mathbf{c}\rVert^2=\sum_{j\le r}(\beta_j/d_j)^2+\sum_{j>r}c_j^2$, smallest for $c_j=0$ at $j>r$. This $\mathbf{c}$ is $\mathbf{D}^+\boldsymbol\beta$, so $\mathbf{x}=\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}\mathbf{y}=\mathbf{A}^+\mathbf{y}$.

With independent columns there is, by Section [3.5](die-beste-naherungslosung.html#stufe-3-5), only one best approximate solution, $(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$; it must agree with $\mathbf{A}^+\mathbf{y}$, and it does so for every $\mathbf{y}$. With independent rows, by Part 1, Section 13.4, the rank equals $m$, so the column space is all of $\mathbb{R}^m$, and the system is solvable for every $\mathbf{y}$; the best approximate solutions are the solutions, and by Section [11.2](#stufe-11-2) the shortest one is $\mathbf G\mathbf{y}$.
:::

⁠**Worked example 1:** For $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ and $\mathbf{y}=(1,\,1)^{\top}$, we get $\mathbf{x}^+=\tfrac1{25}(1+2,\ 2+4)^{\top}=(0.12,\ 0.24)^{\top}$. It lies on the line of best approximate solutions, because $0.12+2\cdot0.24=0.6=\tfrac35$, and it points in the direction of $(1,\,2)^{\top}$, perpendicular to that line: it is the point of the line closest to the origin.

⁠**Worked example 2:** The same quantity is measured three times, with the results $4$, $5$ and $9$. The system “$x=4$, $x=5$, $x=9$” has the matrix $\mathbf{1}\in\mathbb{R}^{3\times1}$, a column of ones. It has an independent column, so $\mathbf{1}^+=(\mathbf{1}^{\top}\mathbf{1})^{-1}\mathbf{1}^{\top}=\tfrac13(1,\,1,\,1)$ and

$$x^+=\tfrac13\,\mathbf{1}^{\top}\mathbf{y}=\tfrac13\,(4+5+9)=6 ,$$

the mean (Fig. [27](#abb-27)). The mean of several measurements is the best approximate solution of the system that takes each measurement to be exact.

:::abbildung ml/k2rmittel 27
The pseudoinverse of the column of ones applied to the measured values $\mathbf{y}=(4,5,9)^{\top}$: the dot product with $\mathbf{1}$ is the sum of the measured values; divided by $\mathbf{1}^{\top}\mathbf{1}=3$, it gives the mean.
:::

⁠**In short:** For every matrix, $\mathbf{A}^+\mathbf{y}$ is a best approximate solution, and among several the shortest; with independent columns or rows, $\mathbf{A}^+$ is the left or right inverse.

:::hintergrund Why the pseudoinverse does not divide by zero
The pseudoinverse replaces $1/d_j$ by $0$ where $d_j=0$. This looks arbitrary, but it follows from a limit. The matrix $\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I}$ is invertible for every $\delta\ne0$, because its eigenvalues are $d_j^2+\delta^2>0$. In the coordinates of the singular vectors, $(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ multiplies the $j$th coordinate by

$$\frac{d_j}{d_j^2+\delta^2}\ \xrightarrow{\ \delta\to0\ }\ \begin{cases}1/d_j&\text{for }d_j>0,\\0&\text{for }d_j=0.\end{cases}$$

So $\mathbf{A}^+=\lim_{\delta\to0}(\mathbf{A}^{\top}\mathbf{A}+\delta^2\mathbf{I})^{-1}\mathbf{A}^{\top}$ for every matrix. The limit also reveals a danger: the pseudoinverse does not depend continuously on the matrix. For $\operatorname{diag}(1,\,\varepsilon)$ with small $\varepsilon>0$, the pseudoinverse is $\operatorname{diag}(1,\,1/\varepsilon)$, which is huge; for $\varepsilon=0$ it is $\operatorname{diag}(1,\,0)$. A tiny singular value that is nonzero only because of measurement errors or rounding is amplified enormously by $\mathbf{A}^+$. Numerical software therefore treats singular values below a small threshold as zero. How strongly small singular values amplify errors is measured in the next section.
:::

:::aufgabe Exercise 33 ★ A left inverse
<span class="anker" id="aufg-33"></span>

The least-squares line in Section [3.6](die-beste-naherungslosung.html#stufe-3-6) belongs to $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$.

<ol class="al">

<li>

Compute the left inverse $\mathbf F=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}$ and check $\mathbf F\mathbf{A}=\mathbf{I}$.

</li>

<li>

Apply $\mathbf F$ to $\mathbf{y}=(1,\,2,\,4)^{\top}$ and compare with Section [3.6](die-beste-naherungslosung.html#stufe-3-6).

</li>

<li>

Read off from the rows of $\mathbf F$ how the intercept and the slope of the least-squares line arise for arbitrary measured values $y_1,y_2,y_3$.

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&3\\3&5\end{smallmatrix}\bigr)$ with the inverse $\tfrac16\bigl(\begin{smallmatrix}5&-3\\-3&3\end{smallmatrix}\bigr)$, so

$$\mathbf F=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix}\begin{pmatrix}1&1&1\\0&1&2\end{pmatrix}=\frac16\begin{pmatrix}5&2&-1\\-3&0&3\end{pmatrix},\qquad \mathbf F\mathbf{A}=\frac16\begin{pmatrix}5+2-1&2-2\\-3+3&6\end{pmatrix}=\mathbf{I} .$$

(b) $\mathbf F(1,\,2,\,4)^{\top}=\tfrac16(5+4-4,\ -3+12)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$, the least-squares line from Section [3.6](die-beste-naherungslosung.html#stufe-3-6).

(c) For arbitrary measured values, the intercept is $\hat x_1=\tfrac16(5y_1+2y_2-y_3)$ and the slope is $\hat x_2=\tfrac12(y_3-y_1)$. The weights of the intercept add up to $1$: if all measured values are equal, the intercept is this value. For three equally spaced data points, the slope depends only on the two outer points; the middle point affects only the height of the line.
:::
:::

:::aufgabe Exercise 34 ★★ Shortest solutions
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

Determine the pseudoinverse of $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ and $\mathbf{x}^+$ for $\mathbf{y}=(1,\,3)^{\top}$. Check that $\mathbf{x}^+$ is a best approximate solution and that no shorter one exists.

</li>

<li>

Determine the shortest solution of $x_1+2x_2+2x_3=9$. Compare its length with that of the solution $(9,\,0,\,0)^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{A}=2\,\mathbf{q}\mathbf{q}^{\top}$ with $\mathbf{q}=(1,\,1)^{\top}/\sqrt2$, symmetric and positive semidefinite, so this is the compact decomposition with $d_1=2$ and $\mathbf{u}_1=\mathbf{v}_1=\mathbf{q}$. Hence $\mathbf{A}^+=\tfrac12\mathbf{q}\mathbf{q}^{\top}=\tfrac14\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ and $\mathbf{x}^+=\tfrac14(4,\,4)^{\top}=(1,\,1)^{\top}$. We have $\mathbf{A}\mathbf{x}^+=(2,\,2)^{\top}$, the projection of $(1,\,3)^{\top}$ onto the line in the direction of $(1,\,1)^{\top}$, because $\tfrac{1+3}2(1,\,1)^{\top}=(2,\,2)^{\top}$. The best approximate solutions are all $\mathbf{x}$ with $x_1+x_2=2$, that is, $(1+s,\ 1-s)^{\top}$ with the squared length $2+2s^2$. The shortest is the one at $s=0$, and that is $\mathbf{x}^+$.

(b) $\mathbf{A}=(1\ \ 2\ \ 2)$ has $\mathbf{A}\mathbf{A}^{\top}=9$, so $\mathbf G=\tfrac19(1,\,2,\,2)^{\top}$, and the shortest solution is $\mathbf G\cdot9=(1,\,2,\,2)^{\top}$ with length $3$. The solution $(9,\,0,\,0)^{\top}$ has length $9$. The shortest solution points in the direction of the normal vector $(1,\,2,\,2)^{\top}$ of the solution plane.
:::
:::

:::aufgabe Exercise 35 ★★★ What the pseudoinverse projects
<span class="anker" id="aufg-35"></span>

Let $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ with rank $r$, and let $\mathbf{U}_r$, $\mathbf{V}_r$ contain the first $r$ columns of $\mathbf{U}$ and $\mathbf{V}$.

<ol class="al">

<li>

Show $\mathbf{A}\mathbf{A}^+=\mathbf{U}_r\mathbf{U}_r^{\top}$ and $\mathbf{A}^+\mathbf{A}=\mathbf{V}_r\mathbf{V}_r^{\top}$. Onto which spaces do these matrices project?

</li>

<li>

Conclude $\mathbf{A}\mathbf{A}^+\mathbf{A}=\mathbf{A}$ and $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=\mathbf{A}^+$.

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{A}^+=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\mathbf{D}^+\mathbf{U}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^+\mathbf{U}^{\top}$. The $m\times m$ matrix $\mathbf{D}\mathbf{D}^+$ has $d_j\cdot\tfrac1{d_j}=1$ in the first $r$ diagonal positions and zeros elsewhere. Hence $\mathbf{A}\mathbf{A}^+=\sum_{j\le r}\mathbf{u}_j\mathbf{u}_j^{\top}=\mathbf{U}_r\mathbf{U}_r^{\top}$, by [(4.2)](projektion-auf-einen-unterraum.html#gl-4-2) the orthogonal projection onto the span of $\mathbf{u}_1,\dots,\mathbf{u}_r$, the column space of $\mathbf{A}$. Likewise, $\mathbf{A}^+\mathbf{A}=\mathbf{V}\mathbf{D}^+\mathbf{D}\mathbf{V}^{\top}=\mathbf{V}_r\mathbf{V}_r^{\top}$, the projection onto the span of $\mathbf{v}_1,\dots,\mathbf{v}_r$, the column space of $\mathbf{A}^{\top}$; this is the orthogonal complement of the null space.

(b) Every column of $\mathbf{A}$ lies in the column space, and the projection onto it leaves it fixed: $\mathbf{A}\mathbf{A}^+\mathbf{A}=(\mathbf{U}_r\mathbf{U}_r^{\top})\mathbf{A}=\mathbf{A}$. Likewise, every column of $\mathbf{A}^+=\sum_{j\le r}\tfrac1{d_j}\mathbf{v}_j\mathbf{u}_j^{\top}$ lies in the span of $\mathbf{v}_1,\dots,\mathbf{v}_r$, so $\mathbf{A}^+\mathbf{A}\mathbf{A}^+=(\mathbf{V}_r\mathbf{V}_r^{\top})\mathbf{A}^+=\mathbf{A}^+$.
:::
:::
