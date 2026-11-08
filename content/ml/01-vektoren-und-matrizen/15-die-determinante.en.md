---
title: The determinant
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15211500
summary: A linear map deforms the grid of the plane, and in the process areas become larger or smaller.
tags: determinant, orientation, Laplace expansion
lang: en
---

<span class="anker" id="stufe-14"></span>

:::zweck
A linear map deforms the grid of the plane, and in the process areas become larger or smaller. This section determines the factor by which they change. This factor is a single number, the determinant, and it also tells you whether a matrix is invertible.
:::

### The determinant of a $2\times2$ matrix

<span class="anker" id="stufe-14-1"></span>

The unit square has area $1$. A matrix $\mathbf{A}$ maps it to the parallelogram spanned by its two columns (Subsection [8.3](lineare-abbildungen.html#stufe-8-3)). How large is the area of this parallelogram? Figure [40](#abb-40) shows it for $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$.

:::abbildung ml/k1det 40
Left: the unit square with area $1$; right: its image under $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$, the parallelogram formed by the columns $\mathbf{a}_1$ and $\mathbf{a}_2$. It has area $5=3\cdot2-1\cdot1$. Dashed: the enclosing rectangle, from which the area can be computed.
:::

:::herleitung The area of the parallelogram
Let the columns be $\mathbf{a}_1=(a,\,c)^{\top}$ and $\mathbf{a}_2=(b,\,d)^{\top}$ with all four numbers positive, and let $\mathbf{a}_2$ lie above and to the left of $\mathbf{a}_1$, as in Fig. [40](#abb-40). The parallelogram with the corners $\mathbf{0}$, $\mathbf{a}_1$, $\mathbf{a}_1+\mathbf{a}_2$, $\mathbf{a}_2$ fits into the rectangle with sides $a+b$ and $c+d$. To leave only the parallelogram, you cut out of the rectangle two triangles with legs $a$ and $c$, two triangles with legs $b$ and $d$, and two rectangles with sides $b$ and $c$:

$$(a+b)(c+d)-2\cdot\tfrac12ac-2\cdot\tfrac12bd-2\,bc=ac+ad+bc+bd-ac-bd-2bc=ad-bc .$$

For $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$: $4\cdot3-3-2-2=5$.
:::

:::definition Definition 14.1 (Determinant of a $2\times2$ matrix)
<span class="anker" id="satz-14-1"></span>

The __determinant__ of the matrix $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ is the number

<span class="anker" id="gl-14-1"></span>
$$\det\mathbf{A}=ad-bc . \tag{14.1}$$
:::

Its absolute value is the area of the parallelogram spanned by the columns, that is, the factor by which $\mathbf{A}$ changes the area of the unit square. It is the same number that appears in the denominator of the inverse [(11.2)](einheitsmatrix-und-inverse.html#gl-11-2).

⁠**Worked example:** $\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=6-1=5$, $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=2-1=1$, $\det\operatorname{diag}(2,\,0.5)=1$ and $\det\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=0$. The stretch changes the shape of the square but not its area: what it gains in width, it loses in height.

⁠**In short:** In absolute value, the determinant $ad-bc$ of a $2\times2$ matrix is the factor by which the map changes the area of the unit square.

### The sign of the determinant

<span class="anker" id="stufe-14-2"></span>

An area is never negative, but the determinant can be. Its sign carries additional information: whether the map reflects the plane.

In the unit square, $\mathbf{e}_2$ lies counterclockwise from $\mathbf{e}_1$. If this stays so for the images, that is, if $\mathbf{a}_2$ also lies counterclockwise from $\mathbf{a}_1$, then $\det\mathbf{A}>0$. If $\mathbf{a}_2$ lies clockwise from $\mathbf{a}_1$, the plane has been reflected, and $\det\mathbf{A}<0$. This property is called __orientation__: a positive determinant preserves the orientation, a negative one reverses it.

⁠**Worked example:** The reflection across the $x_1$-axis, $\operatorname{diag}(1,\,-1)$, has determinant $-1$: the area stays the same, the orientation is reversed. If you swap the columns of a matrix, the determinant changes its sign: $\det\bigl(\begin{smallmatrix}1&3\\2&1\end{smallmatrix}\bigr)=1-6=-5$. The rotation by $90^\circ$ has $\det=0\cdot0-(-1)\cdot1=1$, the shear $\det=1\cdot1-1\cdot0=1$, and the flattening $\operatorname{diag}(1,\,0)$ has determinant $0$.

⁠**In short:** The absolute value of the determinant is the area factor; its sign tells whether the map reflects.

### The area factor holds for every figure

<span class="anker" id="stufe-14-3"></span>

So far we have looked at the unit square. But a linear map treats every location in the plane in the same way, and therefore it changes the area of every figure by the same factor.

:::satz Theorem 14.2 (Area factor)
<span class="anker" id="satz-14-2"></span>

If $\mathbf{A}\in\mathbb{R}^{2\times2}$ maps a figure of area $F$, the image has area $|\det\mathbf{A}|\cdot F$.
:::

:::herleitung Area factor
Lay a fine grid of small squares with side length $h$ over the figure. A square with the corner $\mathbf{q}$ has the corners $\mathbf{q}$, $\mathbf{q}+h\mathbf{e}_1$, $\mathbf{q}+h\mathbf{e}_1+h\mathbf{e}_2$ and $\mathbf{q}+h\mathbf{e}_2$. Its image has the corners $\mathbf{A}\mathbf{q}$, $\mathbf{A}\mathbf{q}+h\mathbf{a}_1$, $\mathbf{A}\mathbf{q}+h\mathbf{a}_1+h\mathbf{a}_2$ and $\mathbf{A}\mathbf{q}+h\mathbf{a}_2$: it is the parallelogram formed by $h\mathbf{a}_1$ and $h\mathbf{a}_2$, shifted to $\mathbf{A}\mathbf{q}$. Its area is $h^2\,|\det\mathbf{A}|$, no matter where the square was. So every small square becomes larger or smaller by the same factor $|\det\mathbf{A}|$. The figure consists approximately of such squares, and the finer the grid, the more accurate the approximation. Therefore the factor holds for the whole figure.
:::

⁠**Worked example:** The disk of radius $1$ has area $\pi$. The stretch $\operatorname{diag}(3,\,2)$ turns it into an ellipse with semi-axes $3$ and $2$. The area of the ellipse is $\pi\cdot3\cdot2=6\pi$, that is, exactly $|\det\mathbf{A}|=6$ times the area of the disk. The triangle with the corners $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$ has area $\tfrac12$; under $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ it becomes the triangle with the corners $\mathbf{0}$, $(3,1)^{\top}$, $(1,2)^{\top}$ and area $\tfrac52$.

⁠**In short:** A linear map changes the area of every figure by the same factor $|\det\mathbf{A}|$, because it treats every small cell of the grid in the same way.

### Determinants of larger matrices

<span class="anker" id="stufe-14-4"></span>

In space, the unit cube becomes the parallelepiped spanned by the three columns of the matrix, a slanted box. Its volume is the factor by which the map changes volumes. For larger matrices, too, there is such a number. You compute it by reducing it to determinants of smaller matrices.

:::definition Definition 14.3 (Determinant)
<span class="anker" id="satz-14-3"></span>

For $\mathbf{A}\in\mathbb{R}^{1\times1}$, $\det\mathbf{A}=a_{11}$. For $\mathbf{A}\in\mathbb{R}^{n\times n}$ with $n\ge2$,

<span class="anker" id="gl-14-2"></span>
$$\det\mathbf{A}=\sum_{j=1}^n(-1)^{1+j}\,a_{1j}\,\det\mathbf{A}_{1j} , \tag{14.2}$$

where $\mathbf{A}_{1j}$ is the $(n-1)\times(n-1)$ matrix obtained from $\mathbf{A}$ by deleting the first row and column $j$. This rule is called the __Laplace expansion__ along the first row.
:::

For $n=2$, [(14.2)](#gl-14-2) again gives $a_{11}a_{22}-a_{12}a_{21}$. You may just as well expand along any other row or column, with the sign $(-1)^{i+j}$ for the entry $a_{ij}$; the result is always the same. For $n=3$, $|\det\mathbf{A}|$ is the volume of the parallelepiped formed by the three columns, and the sign tells whether the columns have the same handedness as $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ (right-hand rule) or are mirrored.

⁠**Worked example:** For the coefficient matrix from Subsection [12.3](lineare-gleichungssysteme.html#stufe-12-3),

$$\mathbf{A}=\begin{pmatrix}1&2&1\\2&1&1\\1&1&2\end{pmatrix},$$

the Laplace expansion along the first row gives $\det\mathbf{A}=-4$ (Fig. [41](#abb-41)).

:::abbildung ml/k1rlaplace 41
The Laplace expansion along the first row: each entry of the first row times the determinant of the matrix that remains without its row and column, with alternating signs.
:::

For an upper triangular matrix, which has only zeros below its diagonal, you expand along the first column again and again and get the product of the diagonal entries, for example $\det\Bigl(\begin{smallmatrix}2&1&3\\0&3&1\\0&0&4\end{smallmatrix}\Bigr)=2\cdot3\cdot4=24$.

⁠**In short:** The determinant of an $n\times n$ matrix is reduced to smaller determinants by the Laplace expansion; its absolute value is the factor by which the map changes volumes.

### Rules of calculation for determinants

<span class="anker" id="stufe-14-5"></span>

The most important rule follows directly from the geometric picture. If you apply two maps one after the other, the first changes the volume by its factor, and the second changes the result once more by its own factor. The factors multiply.

:::satz Theorem 14.4 (Rules of calculation for the determinant)
<span class="anker" id="satz-14-4"></span>

For $\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ and a number $c$:

<ol class="rm">

<li>

$\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\cdot\det\mathbf{B}$;

</li>

<li>

$\det\mathbf{A}^{\top}=\det\mathbf{A}$;

</li>

<li>

$\det\mathbf{A}^{-1}=1/\det\mathbf{A}$ if $\mathbf{A}$ is invertible;

</li>

<li>

$\det(c\,\mathbf{A})=c^n\det\mathbf{A}$;

</li>

<li>

adding a multiple of one row to another does not change the determinant; swapping two rows changes its sign; multiplying a row by $c$ multiplies the determinant by $c$.

</li>

</ol>
:::

Rule (iii) follows from (i) with $\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$ and $\det\mathbf{I}=1$. Rule (iv) says: if you stretch all $n$ edges of the unit cube by $c$, its volume is multiplied by $c^n$. Rule (v) makes Gaussian elimination the practical way to compute determinants: you bring the matrix to row echelon form, keep track of the number of swaps and multiply the diagonal entries.

⁠**Worked example 1:** Since $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=1$ and $\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=5$, the product $\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$ must have determinant $5$: $21-16=5$.

⁠**Worked example 2:** In Gaussian elimination from Subsection [12.3](lineare-gleichungssysteme.html#stufe-12-3), the coefficient matrix was brought, with additions of multiples and one swap, to the echelon form with the diagonal $1$, $-1$, $-4$. So its determinant is $(-1)\cdot\bigl(1\cdot(-1)\cdot(-4)\bigr)=-4$, as with the Laplace expansion.

⁠**In short:** The determinant of a product is the product of the determinants, because the volume factors multiply when maps are applied one after the other; in practice you compute it with Gaussian elimination.

:::hintergrund Why row operations change the determinant in exactly this way
By rule (ii), you may transform the columns instead of the rows, and the columns span the parallelogram or the parallelepiped. If you add a multiple of one column to another, say $\mathbf{a}_2\to\mathbf{a}_2+t\,\mathbf{a}_1$, the side opposite $\mathbf{a}_1$ slides along parallel to $\mathbf{a}_1$. The parallelogram is sheared like a deck of cards pushed sideways. Base and height stay the same, and so does the area. In space, the same holds for the parallelepiped: every cross section parallel to the base is only shifted, not changed, and solids with equally large cross sections at every height have the same volume (Cavalieri's principle). If you swap two columns, the area stays the same, but the sense of rotation from the first column to the second is reversed, and with it the sign. If you multiply a column by $c$, one edge becomes $c$ times as long and the volume $c$ times as large. For $2\times2$ matrices, the formula $ad-bc$ confirms this directly, for example for the shear: $a\,(d+t\,c)-(b+t\,a)\,c=ad-bc$.

Conversely, three properties already determine the determinant completely: $\det\mathbf{I}=1$; swapping two rows changes the sign; and if all rows but one are held fixed, the determinant is linear in that one row. Every function of the matrix with these three properties is the determinant. The reason is Gaussian elimination: it reduces every square matrix by row operations to $\mathbf{I}$ or to a matrix with a zero row, and the effect of each operation is fixed by the three properties. Many textbooks therefore define the determinant by these properties and derive the Laplace expansion from them.
:::

:::hintergrund Why determinants are not computed with the Laplace expansion
The Laplace expansion of an $n\times n$ matrix calls $n$ determinants of size $n-1$, each of them calls $n-1$ of size $n-2$, and so on. Written out, this produces $n!$ products. For $n=20$ that is more than $2\cdot10^{18}$, far too many for a computer. Gaussian elimination, in contrast, needs only about $\tfrac23n^3$ basic arithmetic operations, so for $n=20$ a few thousand. The Laplace expansion is therefore a definition and a tool for small matrices and for derivations, not a computational method.
:::

### Determinant and invertibility

<span class="anker" id="stufe-14-6"></span>

If the determinant is zero, the unit square becomes a figure without area, that is, a line segment or a point. The map flattens the plane, and what has been flattened cannot be restored.

:::satz Theorem 14.5 (Determinant and invertibility)
<span class="anker" id="satz-14-5"></span>

A square matrix $\mathbf{A}$ is invertible if and only if $\det\mathbf{A}\ne0$.
:::

:::beweis Determinant and invertibility
If $\mathbf{A}$ is invertible, then by rule (i) $\det\mathbf{A}\cdot\det\mathbf{A}^{-1}=\det\mathbf{I}=1$, so $\det\mathbf{A}\ne0$. Conversely, if $\det\mathbf{A}\ne0$, bring $\mathbf{A}$ to row echelon form with Gaussian elimination. By rule (v), the determinant changes at most by nonzero factors in the process, so the determinant of the echelon form is not zero either. It is the product of the diagonal entries of the echelon form, so none of them is zero, and there are $n$ pivots. Thus $\operatorname{rank}\mathbf{A}=n$, and by the theorem in Subsection [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5), $\mathbf{A}$ is invertible.
:::

Together with the theorem from Subsection [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5), the following are therefore equivalent for a square matrix: $\det\mathbf{A}\ne0$, $\mathbf{A}$ invertible, $\operatorname{rank}\mathbf{A}=n$, $\ker\mathbf{A}=\{\mathbf{0}\}$, columns linearly independent.

⁠**Worked example:** The matrix $\mathbf K$ from Subsection [13.4](unabhangigkeit-basis-und-rang.html#stufe-13-4) has $\det\mathbf K=1\cdot(2-1)-0+1\cdot(0-1)=0$, in agreement with $\operatorname{rank}\mathbf K=2$. The coefficient matrix from the worked example on Gaussian elimination has $\det=-4\ne0$ and is invertible; that is why the system had exactly one solution.

⁠**In short:** A square matrix is invertible exactly when its determinant is not zero, that is, when it does not flatten space.

:::hintergrund A small determinant does not mean “nearly singular”
You might think that a matrix with a very small determinant is nearly singular. That is not true. The matrix $0.1\,\mathbf{I}_{10}$ has determinant $0.1^{10}=10^{-10}$, but it is perfectly invertible: its inverse is $10\,\mathbf{I}_{10}$, and all it does is shrink all lengths to one tenth. The tiny determinant comes only from the factor $0.1$ being multiplied in once for each of the ten directions. Conversely, $\operatorname{diag}(1000,\,0.001)$ has determinant $1$, even though it almost flattens the plane in one direction. The determinant measures volume, and volume depends on the scale. Whether a matrix “nearly” destroys information cannot be read off reliably from its determinant.
:::

:::aufgabe Exercise 34 ★ Computing determinants
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

Compute the determinants of $\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)$ and $\Bigl(\begin{smallmatrix}1&2&0\\3&1&2\\0&1&1\end{smallmatrix}\Bigr)$. Which of the two matrices is invertible?

</li>

<li>

What is the area of the triangle with the corners $(0,\,0)$, $(3,\,1)$ and $(1,\,2)$?

</li>

<li>

What is the volume of the parallelepiped formed by the vectors $(1,\,0,\,0)^{\top}$, $(1,\,2,\,0)^{\top}$ and $(0,\,1,\,3)^{\top}$?

</li>

</ol>

:::loesung
(a) $\det\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)=4-4=0$: not invertible; the second column is twice the first. For the $3\times3$ matrix, expanding along the first row:

$$1\cdot\det\begin{pmatrix}1&2\\1&1\end{pmatrix}-2\cdot\det\begin{pmatrix}3&2\\0&1\end{pmatrix}+0=1\cdot(1-2)-2\cdot3=-7 .$$

It is invertible.

(b) The triangle is half of the parallelogram formed by $(3,1)^{\top}$ and $(1,2)^{\top}$, which has the area $|\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)|=5$; so the triangle has the area $2.5$. The same follows from the area factor: the triangle with the corners $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$ and the area $\tfrac12$ is mapped onto this triangle.

(c) The vectors as columns give $\Bigl(\begin{smallmatrix}1&1&0\\0&2&1\\0&0&3\end{smallmatrix}\Bigr)$, an upper triangular matrix with the determinant $1\cdot2\cdot3=6$. The volume is $6$.
:::
:::

:::aufgabe Exercise 35 ★★ Checking the rules of calculation
<span class="anker" id="aufg-35"></span>

<ol class="al">

<li>

Check $\det(\mathbf{C}\mathbf{D})=\det\mathbf{C}\cdot\det\mathbf{D}$ for $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ and $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$, and compute $\det(3\,\mathbf{C})$.

</li>

<li>

Show that every rotation matrix $\mathbf R_\alpha$ has determinant $1$. What does this mean geometrically?

</li>

<li>

Explain without calculation why a matrix with two equal columns has determinant $0$.

</li>

</ol>

:::loesung
(a) $\det\mathbf{C}=4-6=-2$, $\det\mathbf{D}=0-1=-1$, and $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$ with $\det=14-12=2=(-2)\cdot(-1)$. Furthermore, $3\mathbf{C}=\bigl(\begin{smallmatrix}3&6\\9&12\end{smallmatrix}\bigr)$ with $\det=36-54=-18=3^2\cdot(-2)$, as rule (iv) with $n=2$ says.

(b) $\det\mathbf R_\alpha=\cos\alpha\cdot\cos\alpha-(-\sin\alpha)\cdot\sin\alpha=\cos^2\alpha+\sin^2\alpha=1$. A rotation changes no area and does not reflect.

(c) Two equal columns are linearly dependent. The parallelogram or parallelepiped spanned by the columns is flat and has area or volume zero. The same follows from rule (v), carried over to columns with $\det\mathbf{A}^{\top}=\det\mathbf{A}$: if you swap the two equal columns, the matrix stays the same, but the determinant would have to change its sign. So $\det\mathbf{A}=-\det\mathbf{A}$, and hence $\det\mathbf{A}=0$.
:::
:::
