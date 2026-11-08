---
title: Projection onto a line
pfad: Computer Science / Machine Learning / Mathematical Foundations / Projection, Eigenvalues and Decompositions
knoten: Foundations 2: Projection, Eigenvalues and Decompositions
nachschlagen: ja
order: 15220300
summary: A point lies off a line.
tags: orthogonal projection, projection matrix, projection
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
A point lies off a line. Which point of the line is closest to it? This section answers the question for lines through the origin, in any dimension. The answer is the foot of the perpendicular, and the reason for this is the Pythagorean theorem.
:::

### The foot of the perpendicular

<span class="anker" id="stufe-2-1"></span>

A line through the origin consists of all multiples $t\,\mathbf{a}$ of a direction vector $\mathbf{a}\ne\mathbf{0}$. We are given a point $\mathbf{y}$ that need not lie on it. We are looking for the point of the line that is closest to $\mathbf{y}$.

In Foundations 1, Section 5.5, an arrow cast a shadow onto a line when the light fell perpendicularly. The endpoint of the shadow is the point where the perpendicular from $\mathbf{y}$ meets the line, the *foot of the perpendicular*. The connection from this point to $\mathbf{y}$ is perpendicular to the line (Fig. [4](#abb-4)). That it is the closest point is shown in the next subsection. Here it is computed first, and this works even when $\mathbf{a}$ is not normalized.

:::herleitung The foot of the perpendicular
The point we are looking for lies on the line, so it is $\hat x\,\mathbf{a}$ with a number $\hat x$ that is still unknown. The connection $\mathbf{y}-\hat x\,\mathbf{a}$ is to be perpendicular to $\mathbf{a}$:

$$\mathbf{a}^{\top}(\mathbf{y}-\hat x\,\mathbf{a})=0\qquad\Longleftrightarrow\qquad \mathbf{a}^{\top}\mathbf{y}-\hat x\,\mathbf{a}^{\top}\mathbf{a}=0\qquad\Longleftrightarrow\qquad \hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} .$$

Since $\mathbf{a}\ne\mathbf{0}$, we have $\mathbf{a}^{\top}\mathbf{a}=\lVert\mathbf{a}\rVert^2>0$, so the division is allowed, and there is exactly one such $\hat x$.
:::

:::definition Definition 2.1 (Projection onto a line)
<span class="anker" id="satz-2-1"></span>

Let $\mathbf{a}\in\mathbb{R}^n$, $\mathbf{a}\ne\mathbf{0}$. The __orthogonal projection__ of $\mathbf{y}\in\mathbb{R}^n$ onto the line through the origin in the direction of $\mathbf{a}$ is the point

<span class="anker" id="gl-2-1"></span>
$$\hat{\mathbf{y}}=\hat x\,\mathbf{a}\qquad\text{with}\qquad\hat x=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}} . \tag{2.1}$$
:::

The point $\hat{\mathbf{y}}$ is a vector in $\mathbb{R}^n$; the number $\hat x$ is its coordinate along $\mathbf{a}$. The two must not be confused. If $\mathbf{a}$ is normalized, then $\mathbf{a}^{\top}\mathbf{a}=1$ and $\hat{\mathbf{y}}=(\mathbf{a}^{\top}\mathbf{y})\,\mathbf{a}$, exactly the shadow point from Foundations 1.

:::abbildung ml/k2lot 4
The projection of $\mathbf{y}=(4,3)^{\top}$ onto the line in the direction of $\mathbf{a}=(1,2)^{\top}$. The foot of the perpendicular is $\hat{\mathbf{y}}=2\mathbf{a}=(2,4)^{\top}$; the connection $\mathbf{r}=(2,-1)^{\top}$ (blue) is perpendicular to the line. Any other point of the line, for example $(1,2)^{\top}$, is farther away from $\mathbf{y}$ (dashed): the triangle formed by $\mathbf{y}$, $\hat{\mathbf{y}}$ and $(1,2)^{\top}$ has a right angle at $\hat{\mathbf{y}}$, and the dashed side is its hypotenuse.
:::

⁠**Worked example 1:** For $\mathbf{a}=(1,\,2)^{\top}$ and $\mathbf{y}=(4,\,3)^{\top}$ we get $\mathbf{a}^{\top}\mathbf{y}=4+6=10$ and $\mathbf{a}^{\top}\mathbf{a}=5$ (Fig. [5](#abb-5)), so $\hat x=2$ and $\hat{\mathbf{y}}=(2,\,4)^{\top}$. The connection $\mathbf{y}-\hat{\mathbf{y}}=(2,\,-1)^{\top}$ is perpendicular to $\mathbf{a}$: $2-2=0$.

:::abbildung ml/k2rproj 5
The two dot products of the projection step by step: $\mathbf{a}^{\top}\mathbf{y}=10$ in the numerator and $\mathbf{a}^{\top}\mathbf{a}=5$ in the denominator of $\hat x$.
:::

⁠**Worked example 2:** For $\mathbf{a}=(3,\,4)^{\top}$ and $\mathbf{y}=(3,\,1)^{\top}$ we get $\hat x=(9+4)/25=0.52$ and $\hat{\mathbf{y}}=0.52\,(3,\,4)^{\top}=(1.56,\ 2.08)^{\top}$, the same shadow point as in Foundations 1 with the normalized vector $(0.6,\ 0.8)^{\top}=\mathbf{a}/5$. The length of the direction vector does not matter: if you replace $\mathbf{a}$ by $c\,\mathbf{a}$ with $c\ne0$, then $\hat x$ becomes $\hat x/c$, and $\hat{\mathbf{y}}$ stays the same. If, on the other hand, you double $\mathbf{y}$, then $\hat{\mathbf{y}}$ doubles as well.

⁠**In short:** The projection of $\mathbf{y}$ onto the line in the direction of $\mathbf{a}$ is the foot of the perpendicular, $\hat{\mathbf{y}}=\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{a}$.

### The foot is the closest point

<span class="anker" id="stufe-2-2"></span>

So far we have only shown that the connection to the foot is perpendicular. That the foot is also the closest point follows from the Pythagorean theorem: moving away from the foot along the line adds a piece in the direction of the line to the perpendicular connection, and that can only increase the distance.

:::satz Theorem 2.2 (The foot is the closest point)
<span class="anker" id="satz-2-2"></span>

Let $\hat{\mathbf{y}}=\hat x\,\mathbf{a}$ be the projection of $\mathbf{y}$ onto the line in the direction of $\mathbf{a}$. For every number $t$,

<span class="anker" id="gl-2-2"></span>
$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2=\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2+(t-\hat x)^2\,\lVert\mathbf{a}\rVert^2 . \tag{2.2}$$

In particular, $\hat{\mathbf{y}}$ is the unique point of the line with the smallest distance to $\mathbf{y}$.
:::

:::beweis The closest point
Write the connection from $t\,\mathbf{a}$ to $\mathbf{y}$ as the sum of two arrows:

$$\mathbf{y}-t\,\mathbf{a}=(\mathbf{y}-\hat{\mathbf{y}})+(\hat x-t)\,\mathbf{a} .$$

By the derivation, the first term is perpendicular to $\mathbf{a}$, hence also to the second. By the Pythagorean theorem from Foundations 1, Section 5.3, the squared length of the sum is the sum of the squared lengths, and that is [(2.2)](#gl-2-2). The second term on the right-hand side is never negative and is zero only for $t=\hat x$. So the distance is smallest exactly for $t=\hat x$.
:::

For the length of the foot, $\lVert\hat{\mathbf{y}}\rVert=|\hat x|\,\lVert\mathbf{a}\rVert=|\mathbf{a}^{\top}\mathbf{y}|/\lVert\mathbf{a}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$, where $\varphi$ is the angle between $\mathbf{a}$ and $\mathbf{y}$. This is the adjacent side in the right triangle with the hypotenuse $\mathbf{y}$.

⁠**Worked example:** In the first worked example of the previous subsection, $\lVert\mathbf{y}-\hat{\mathbf{y}}\rVert^2=\lVert(2,\,-1)^{\top}\rVert^2=5$. For the point $t=1$, that is $(1,\,2)^{\top}$, [(2.2)](#gl-2-2) predicts the squared distance $5+1\cdot5=10$, and indeed $\lVert(3,\,1)^{\top}\rVert^2=10$. For $t=3$, that is $(3,\,6)^{\top}$, it is also $5+1\cdot5=10=\lVert(1,\,-3)^{\top}\rVert^2$. Both points are equally far from the foot, on different sides.

⁠**In short:** The closest point of a line is the foot of the perpendicular, because by Pythagoras every step along the line increases the squared distance.

:::hintergrund Why there is exactly one closest point, and why this is due to the Euclidean norm
The proof uses the Pythagorean theorem, and that theorem holds only for norms that come from a dot product. In Foundations 1, Section 3.4, it turned out that the 1-norm is not such a norm. With it, uniqueness is indeed lost. Example: the line in the direction of $\mathbf{a}=(1,\,1)^{\top}$ and the point $\mathbf{y}=(1,\,0)^{\top}$. For $0\le t\le1$,

$$\lVert\mathbf{y}-t\,\mathbf{a}\rVert_1=|1-t|+|0-t|=(1-t)+t=1 ,$$

so the distance is the same for all points between $\mathbf{0}$ and $\mathbf{a}$; outside this segment it is larger. In this norm there is a whole segment of closest points. In the Euclidean norm there is exactly one: $\hat x=\tfrac12$, the point $(\tfrac12,\,\tfrac12)^{\top}$. The fact that the projection is unique and can be computed with a simple formula is one of the reasons why so many methods use the Euclidean distance.
:::

### The projection matrix

<span class="anker" id="stufe-2-3"></span>

The rule $\mathbf{y}\mapsto\hat{\mathbf{y}}$ is linear: the sum of two points is mapped to the sum of their projections, a multiple to the corresponding multiple. By Foundations 1, Section 8.2, it therefore has a matrix. You can read it off directly by writing the number $\mathbf{a}^{\top}\mathbf{y}$ on the other side of $\mathbf{a}$ and regrouping the matrix product:

$$\hat{\mathbf{y}}=\mathbf{a}\,\frac{\mathbf{a}^{\top}\mathbf{y}}{\mathbf{a}^{\top}\mathbf{a}}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}\,\mathbf{y} .$$

The numerator is the outer product from Foundations 1, Section 9.5.

:::definition Definition 2.3 (Projection matrix of a line)
<span class="anker" id="satz-2-3"></span>

For $\mathbf{a}\ne\mathbf{0}$,

<span class="anker" id="gl-2-3"></span>
$$\mathbf{P}=\frac{\mathbf{a}\,\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}} \tag{2.3}$$

is called the __projection matrix__ onto the line in the direction of $\mathbf{a}$. We have $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$.
:::

:::satz Theorem 2.4 (Properties of the projection matrix of a line)
<span class="anker" id="satz-2-4"></span>

We have $\mathbf{P}^{\top}=\mathbf{P}$ and $\mathbf{P}^2=\mathbf{P}$. Points of the line stay where they are: $\mathbf{P}\mathbf{a}=\mathbf{a}$. Vectors perpendicular to $\mathbf{a}$ are mapped to $\mathbf{0}$. The rank of $\mathbf{P}$ is $1$.
:::

:::beweis Properties
$(\mathbf{a}\mathbf{a}^{\top})^{\top}=\mathbf{a}\mathbf{a}^{\top}$, so $\mathbf{P}$ is symmetric. Furthermore, $\mathbf{P}^2=\mathbf{a}(\mathbf{a}^{\top}\mathbf{a})\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})^2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{P}$, because $\mathbf{a}^{\top}\mathbf{a}$ is a number. $\mathbf{P}\mathbf{a}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{a})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{a}$. If $\mathbf{a}^{\top}\mathbf{z}=0$, then $\mathbf{P}\mathbf{z}=\mathbf{a}\,(\mathbf{a}^{\top}\mathbf{z})/(\mathbf{a}^{\top}\mathbf{a})=\mathbf{0}$. Every column of $\mathbf{P}$ is a multiple of $\mathbf{a}$, so the rank is $1$.
:::

The equation $\mathbf{P}^2=\mathbf{P}$ has a simple meaning: whatever is already on the line stays put when projected a second time.

⁠**Worked example:** For $\mathbf{a}=(1,\,2)^{\top}$,

$$\mathbf{P}=\frac15\begin{pmatrix}1&2\\2&4\end{pmatrix},\qquad \mathbf{P}\begin{pmatrix}4\\3\end{pmatrix}=\frac15\begin{pmatrix}4+6\\8+12\end{pmatrix}=\begin{pmatrix}2\\4\end{pmatrix}.$$

Check of $\mathbf{P}^2=\mathbf{P}$: $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)^2=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)=5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, so $\mathbf{P}^2=\frac1{25}\cdot5\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=\mathbf{P}$. In Foundations 1, Section 11.5, the matrix $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ was the example of a matrix without an inverse. Now it is clear what it does: it is five times a projection and squashes the plane flat onto the line in the direction of $(1,\,2)^{\top}$.

⁠**In short:** The projection onto a line is the matrix-vector product with $\mathbf{P}=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$; this matrix is symmetric and satisfies $\mathbf{P}^2=\mathbf{P}$.

### Projections in general

<span class="anker" id="stufe-2-4"></span>

Shadows also exist when the light falls at a slant. Then the shadow of a point on a line is no longer the foot of the perpendicular, but it still lies on the line, and a point that already lies on the line is its own shadow. So the property $\mathbf{P}^2=\mathbf{P}$ is retained, but the symmetry is not.

:::definition Definition 2.5 (Projection)
<span class="anker" id="satz-2-5"></span>

A square matrix $\mathbf{P}$ with $\mathbf{P}^2=\mathbf{P}$ is called a __projection__. It is called an orthogonal projection if, in addition, for every $\mathbf{y}$ the connection $\mathbf{y}-\mathbf{P}\mathbf{y}$ is perpendicular to all images $\mathbf{P}\mathbf{z}$.
:::

:::satz Theorem 2.6 (Orthogonal means symmetric)
<span class="anker" id="satz-2-6"></span>

A projection $\mathbf{P}$ is an orthogonal projection if and only if $\mathbf{P}^{\top}=\mathbf{P}$.
:::

:::beweis Orthogonal means symmetric
For all $\mathbf{y},\mathbf{z}$, $(\mathbf{y}-\mathbf{P}\mathbf{y})^{\top}\mathbf{P}\mathbf{z}=\mathbf{y}^{\top}(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}\mathbf{z}$. If $\mathbf{P}^{\top}=\mathbf{P}$, then $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}=\mathbf{P}-\mathbf{P}^2=\mathbf 0$, and the expression is zero. Conversely, if the expression is zero for all $\mathbf{y},\mathbf{z}$, then the matrix $(\mathbf{I}-\mathbf{P})^{\top}\mathbf{P}$ is the zero matrix; with $\mathbf{y}=\mathbf{e}_i$ and $\mathbf{z}=\mathbf{e}_l$, the expression picks out its entry $(i,l)$. Then $\mathbf{P}=\mathbf{P}^{\top}\mathbf{P}$, and by Foundations 1, Section 10.2, $\mathbf{P}^{\top}\mathbf{P}$ is symmetric.
:::

⁠**Worked example:** The matrix $\mathbf{P}=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$ maps $(x_1,\,x_2)^{\top}$ to $(x_1+x_2,\,0)^{\top}$. We have $\mathbf{P}^2=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}1&1\\0&0\end{smallmatrix}\bigr)$, so $\mathbf{P}$ is a projection onto the $x_1$-axis. It is not symmetric and therefore not orthogonal: the point $(0,\,1)^{\top}$ is mapped to $(1,\,0)^{\top}$, and the connection $(-1,\,1)^{\top}$ is slanted relative to the axis. Here the light falls in the direction $(1,\,-1)^{\top}$. This projection does not deliver the closest point of the $x_1$-axis, $(0,\,0)^{\top}$.

⁠**In short:** A projection is a matrix with $\mathbf{P}^2=\mathbf{P}$; it is orthogonal, that is, it drops a perpendicular, exactly when it is symmetric.

:::aufgabe Exercise 4 ★ A projection by hand
<span class="anker" id="aufg-4"></span>

Project $\mathbf{y}=(3,\,3,\,0)^{\top}$ onto the line in the direction of $\mathbf{a}=(2,\,1,\,2)^{\top}$.

<ol class="al">

<li>

Compute $\hat x$, $\hat{\mathbf{y}}$ and the connection $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}$. Check $\mathbf{a}^{\top}\mathbf{r}=0$. How far is $\mathbf{y}$ from the line?

</li>

<li>

Set up the projection matrix $\mathbf{P}$ and check $\mathbf{P}\mathbf{y}=\hat{\mathbf{y}}$ and $\mathbf{P}\mathbf{a}=\mathbf{a}$.

</li>

</ol>

:::loesung
(a) We have $\mathbf{a}^{\top}\mathbf{y}=6+3+0=9$ and $\mathbf{a}^{\top}\mathbf{a}=4+1+4=9$, so $\hat x=1$ and $\hat{\mathbf{y}}=\mathbf{a}=(2,\,1,\,2)^{\top}$. The connection is $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(1,\,2,\,-2)^{\top}$, and $\mathbf{a}^{\top}\mathbf{r}=2+2-4=0$: it is perpendicular to the line. The distance from $\mathbf{y}$ to the line is $\lVert\mathbf{r}\rVert=\sqrt{1+4+4}=3$; by the theorem in Section [2.2](#stufe-2-2), no point of the line is closer.

(b)

$$\mathbf{P}=\frac{\mathbf{a}\mathbf{a}^{\top}}{\mathbf{a}^{\top}\mathbf{a}}=\frac19\begin{pmatrix}4&2&4\\2&1&2\\4&2&4\end{pmatrix},\qquad \mathbf{P}\mathbf{y}=\frac19\begin{pmatrix}12+6\\6+3\\12+6\end{pmatrix}=\begin{pmatrix}2\\1\\2\end{pmatrix},\qquad \mathbf{P}\mathbf{a}=\frac19\begin{pmatrix}8+2+8\\4+1+4\\8+2+8\end{pmatrix}=\mathbf{a} .$$
:::
:::

:::aufgabe Exercise 5 ★★ Pythagoras on the line
<span class="anker" id="aufg-5"></span>

Let $\mathbf{a}=(1,\,2)^{\top}$ and $\mathbf{y}=(4,\,3)^{\top}$ as in the worked example.

<ol class="al">

<li>

Compute $\lVert\mathbf{y}-t\,\mathbf{a}\rVert^2$ for $t=0$, $1$, $2$, $3$ and $4$, directly and with [(2.2)](#gl-2-2).

</li>

<li>

Compute the angle $\varphi$ between $\mathbf{a}$ and $\mathbf{y}$ and check $\lVert\hat{\mathbf{y}}\rVert=|\cos\varphi|\,\lVert\mathbf{y}\rVert$.

</li>

</ol>

:::loesung
(a) Directly: $t=0$: $\lVert(4,\,3)^{\top}\rVert^2=25$; $t=1$: $\lVert(3,\,1)^{\top}\rVert^2=10$; $t=2$: $\lVert(2,\,-1)^{\top}\rVert^2=5$; $t=3$: $\lVert(1,\,-3)^{\top}\rVert^2=10$; $t=4$: $\lVert(0,\,-5)^{\top}\rVert^2=25$. With [(2.2)](#gl-2-2), $\hat x=2$, $\lVert\mathbf{r}\rVert^2=5$ and $\lVert\mathbf{a}\rVert^2=5$: $5+5(t-2)^2$ gives $25$, $10$, $5$, $10$, $25$. The values are symmetric about the foot of the perpendicular at $t=2$, because the squared distance grows with the square of the distance along the line.

(b) $\cos\varphi=\mathbf{a}^{\top}\mathbf{y}/(\lVert\mathbf{a}\rVert\,\lVert\mathbf{y}\rVert)=10/(\sqrt5\cdot5)=2/\sqrt5\approx0.894$, so $\varphi\approx26.57^\circ$. We have $\lVert\hat{\mathbf{y}}\rVert=\lVert(2,\,4)^{\top}\rVert=\sqrt{20}=2\sqrt5$ and $|\cos\varphi|\,\lVert\mathbf{y}\rVert=\tfrac2{\sqrt5}\cdot5=2\sqrt5$.
:::
:::

:::aufgabe Exercise 6 ★★ Which matrices are projections?
<span class="anker" id="aufg-6"></span>

For each matrix, check whether it is a projection and whether it is an orthogonal projection. For the projections, describe what they project onto.

$$\mathbf{P}_1=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad \mathbf{P}_2=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad \mathbf{P}_3=\begin{pmatrix}1&0\\1&0\end{pmatrix},\quad \mathbf{P}_4=\begin{pmatrix}1&2\\0&1\end{pmatrix},\quad \mathbf{P}_5=\mathbf{I},\quad \mathbf{P}_6=\mathbf 0 .$$

:::loesung
For each matrix, first check $\mathbf{P}^2=\mathbf{P}$ and then $\mathbf{P}^{\top}=\mathbf{P}$.

<ul>

<li>

$\mathbf{P}_1$: $\mathbf{P}_1^2=\mathbf{P}_1$ and symmetric, so the orthogonal projection onto the $x_1$-axis.

</li>

<li>

$\mathbf{P}_2$: $\mathbf{P}_2^2=\tfrac14\bigl(\begin{smallmatrix}2&2\\2&2\end{smallmatrix}\bigr)=\mathbf{P}_2$ and symmetric: the orthogonal projection onto the line in the direction of $(1,\,1)^{\top}$; indeed, $\mathbf{P}_2=\mathbf{a}\mathbf{a}^{\top}/(\mathbf{a}^{\top}\mathbf{a})$ with $\mathbf{a}=(1,\,1)^{\top}$.

</li>

<li>

$\mathbf{P}_3$: $\mathbf{P}_3^2=\bigl(\begin{smallmatrix}1&0\\1&0\end{smallmatrix}\bigr)=\mathbf{P}_3$, but not symmetric. An oblique projection: it maps $(x_1,\,x_2)^{\top}$ to $x_1\,(1,\,1)^{\top}$, that is, onto the line in the direction of $(1,\,1)^{\top}$, and the vector $(0,\,1)^{\top}$ to zero. The light falls in the direction $(0,\,1)^{\top}$, not perpendicular to the line.

</li>

<li>

$\mathbf{P}_4$: $\mathbf{P}_4^2=\bigl(\begin{smallmatrix}1&4\\0&1\end{smallmatrix}\bigr)\ne\mathbf{P}_4$. Not a projection but a shear; applied twice, it shears twice as much.

</li>

<li>

$\mathbf{P}_5=\mathbf{I}$: $\mathbf{I}^2=\mathbf{I}$, symmetric. The orthogonal projection onto the whole plane; it leaves everything where it is.

</li>

<li>

$\mathbf{P}_6=\mathbf 0$: $\mathbf 0^2=\mathbf 0$, symmetric. The orthogonal projection onto the origin.

</li>

</ul>
:::
:::
