---
title: The best approximate solution
pfad: Computer Science / Machine Learning / Projection, Eigenvalues and Decompositions
order: 6220400
summary: A system of equations with more equations than unknowns usually has no solution.
tags: residual, best approximate solution, normal equations, least-squares line
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
A system of equations with more equations than unknowns usually has no solution. Instead, this section looks for the unknowns that satisfy the system as well as possible. They follow from a smaller system of equations that can always be solved, and the reason for this is once again a right angle.
:::

### Review: more equations than unknowns

<span class="anker" id="stufe-3-1"></span>

In Part 1, Section 12.5, two weights, $w_1$ for the floor area and $w_2$ for the number of rooms, were supposed to hit the prices of apartments exactly. With all four apartments, this is the system $\mathbf{A}\mathbf{w}=\mathbf{y}$ with

$$\mathbf{A}=\begin{pmatrix}60&2\\40&1\\90&4\\70&3\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}200\\130\\290\\240\end{pmatrix}\ \text{thousand euros}.$$

It has no solution. In the column picture this means: the columns of $\mathbf{A}$ span a plane in $\mathbb{R}^4$, the column space, and the price vector $\mathbf{y}$ does not lie in it. Whatever you choose for $\mathbf{w}$, a remainder is left over.

:::definition Definition 3.1 (Residual)
<span class="anker" id="satz-3-1"></span>

For a system of equations $\mathbf{A}\mathbf{x}=\mathbf{y}$ and an arbitrary vector $\mathbf{x}$,

<span class="anker" id="gl-3-1"></span>
$$\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x} \tag{3.1}$$

is called the __residual__ for $\mathbf{x}$.
:::

The word comes from the Latin word for “remainder”. The residual is zero exactly when $\mathbf{x}$ solves the system. It is the error vector from Part 1, Section 3.5, with the opposite sign; its length is the same.

⁠**Worked example:** With the weights $\mathbf{w}=(3,\,10)^{\top}$ from Part 1, $\mathbf{A}\mathbf{w}=(200,\,130,\,310,\,240)^{\top}$, and the residual is $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{w}=(0,\,0,\,-20,\,0)^{\top}$ with length $20$. Three prices are hit exactly, one is missed by $20$ thousand euros.

⁠**In short:** The residual $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ is the remainder that a vector $\mathbf{x}$ leaves over when it is used to solve $\mathbf{A}\mathbf{x}=\mathbf{y}$.

### The best approximate solution

<span class="anker" id="stufe-3-2"></span>

If the residual cannot become zero, it should at least be as small as possible. The measure for this is its Euclidean length.

You can picture the task geometrically. As $\mathbf{x}$ runs through all vectors, $\mathbf{A}\mathbf{x}$ runs through the column space of $\mathbf{A}$, by Part 1, Section 7.4. The distance $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert$ is the distance of the point $\mathbf{y}$ from the point $\mathbf{A}\mathbf{x}$ in the column space. So we are looking for the point of the column space that is closest to $\mathbf{y}$ (Fig. [6](#abb-6)). In the previous section the column space was a line; now it can be a plane or a span of higher dimension.

:::definition Definition 3.2 (Best approximate solution)
<span class="anker" id="satz-3-2"></span>

A vector $\hat{\mathbf{x}}$ is called a __best approximate solution__ of the system $\mathbf{A}\mathbf{x}=\mathbf{y}$ if

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert\le\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\qquad\text{for all }\mathbf{x} . \tag{3.2}$$
:::

The length is smallest where its square is smallest, and the square is the sum of the squared components of the residual. That is why one also speaks of the solution by the *method of least squares*. If the system has an exact solution, it is also the best approximate solution, because its residual has length zero.

:::abbildung ml/k2ebene 6
Projection onto a plane in $\mathbb{R}^3$. The columns $\mathbf{a}_1=(1,0,1)^{\top}$ and $\mathbf{a}_2=(0,1,1)^{\top}$ span the plane $x_3=x_1+x_2$ (blue). The point $\mathbf{y}=(1,1,1)^{\top}$ does not lie in it. The closest point of the plane is $\hat{\mathbf{y}}=(\tfrac23,\tfrac23,\tfrac43)^{\top}$; the residual $\mathbf{r}=\mathbf{y}-\hat{\mathbf{y}}=(\tfrac13,\tfrac13,-\tfrac13)^{\top}$ is perpendicular to the plane.
:::

⁠**Worked example:** The matrix $\mathbf{H}$ from Part 1, Section 7.4, has the columns $\mathbf{a}_1=(1,\,0,\,1)^{\top}$ and $\mathbf{a}_2=(0,\,1,\,1)^{\top}$. Its column space is the plane of all vectors whose third component is the sum of the first two. The vector $\mathbf{y}=(1,\,1,\,1)^{\top}$ does not lie in it, so the system $\mathbf{H}\mathbf{x}=\mathbf{y}$ has no solution. With $\mathbf{x}=(1,\,0)^{\top}$ the residual is $(0,\,1,\,0)^{\top}$ with length $1$; with $\mathbf{x}=(1,\,1)^{\top}$ it is $(0,\,0,\,-1)^{\top}$, also with length $1$. Whether we can do better is answered in the next subsection.

⁠**In short:** The best approximate solution makes the residual as short as possible; geometrically, it looks for the point of the column space that is closest to $\mathbf{y}$.

### The normal equations

<span class="anker" id="stufe-3-3"></span>

For the line, the closest point was the foot of the perpendicular: the residual was perpendicular to the line. For a column space, the same condition suggests itself: the residual should be perpendicular to every vector of the column space. This can be written as a system of equations.

:::herleitung The normal equations
Every vector of the column space is a linear combination $\sum_jz_j\mathbf{a}_j$ of the columns. If $\mathbf{r}$ is perpendicular to every column, it is also perpendicular to every such linear combination, because $\bigl(\sum_jz_j\mathbf{a}_j\bigr)^{\top}\mathbf{r}=\sum_jz_j\,\mathbf{a}_j^{\top}\mathbf{r}$. So it suffices to require for every column:

$$\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=0\qquad\text{for }j=1,\dots,n .$$

The numbers $\mathbf{a}_j^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$ are the components of $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})$, because the rows of $\mathbf{A}^{\top}$ are the columns of $\mathbf{A}$. Together, the $n$ conditions therefore read $\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})=\mathbf{0}$, or, multiplied out, $\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$.
:::

:::definition Definition 3.3 (Normal equations)
<span class="anker" id="satz-3-3"></span>

The __normal equations__ of the system $\mathbf{A}\mathbf{x}=\mathbf{y}$ with $\mathbf{A}\in\mathbb{R}^{m\times n}$ are

<span class="anker" id="gl-3-3"></span>
$$\mathbf{A}^{\top}\mathbf{A}\,\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y} . \tag{3.3}$$
:::

The word “normal” here means “perpendicular”, as in the normal vector of a plane: the equations require the residual to be perpendicular to the column space. The matrix $\mathbf{A}^{\top}\mathbf{A}$ is the Gram matrix of the columns from Part 1, Section 10.4; it is square, with as many rows as there are unknowns. A large, unsolvable system with $m$ equations becomes a small one with $n$ equations. For a single column $\mathbf{a}$, it reads $\mathbf{a}^{\top}\mathbf{a}\,\hat x=\mathbf{a}^{\top}\mathbf{y}$, the formula from the previous section.

⁠**Worked example:** For $\mathbf{H}$ and $\mathbf{y}=(1,\,1,\,1)^{\top}$,

$$\mathbf{H}^{\top}\mathbf{H}=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad \mathbf{H}^{\top}\mathbf{y}=\begin{pmatrix}2\\2\end{pmatrix}.$$

Every entry is a dot product of two columns or of a column with $\mathbf{y}$ (Fig. [7](#abb-7)).

:::abbildung ml/k2rnormal 7
Two entries of the normal equations as dot products: entry $(1,2)$ of $\mathbf{H}^{\top}\mathbf{H}$ is $\mathbf{a}_1^{\top}\mathbf{a}_2$, and the first component of $\mathbf{H}^{\top}\mathbf{y}$ is $\mathbf{a}_1^{\top}\mathbf{y}$.
:::

The normal equations $2\hat x_1+\hat x_2=2$ and $\hat x_1+2\hat x_2=2$ have the solution $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$. Hence $\hat{\mathbf{y}}=\mathbf{H}\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23,\,\tfrac43)^{\top}$, and the residual is $\mathbf{r}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$. Check: $\mathbf{a}_1^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$ and $\mathbf{a}_2^{\top}\mathbf{r}=\tfrac13-\tfrac13=0$. The length of the residual is $\sqrt{3/9}\approx0.577$, shorter than both attempts in the previous subsection.

⁠**In short:** The normal equations $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ require the residual to be perpendicular to all columns.

### Why the normal equations give the best solution

<span class="anker" id="stufe-3-4"></span>

For the line, the fact that a perpendicular residual belongs to the closest point was the Pythagorean theorem. The same argument works here: it splits the error into a part that you can influence through the choice of $\mathbf{x}$ and a part that you cannot influence.

:::satz Theorem 3.4 (The normal equations give the best approximate solution)
<span class="anker" id="satz-3-4"></span>

If $\hat{\mathbf{x}}$ solves the normal equations, then for every vector $\mathbf{x}$

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert^2+\lVert\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})\rVert^2 . \tag{3.4}$$

So $\hat{\mathbf{x}}$ is a best approximate solution. Conversely, every best approximate solution solves the normal equations, and all best approximate solutions give the same point $\hat{\mathbf{y}}=\mathbf{A}\hat{\mathbf{x}}$.
:::

:::beweis Best approximate solution
Split $\mathbf{y}-\mathbf{A}\mathbf{x}=(\mathbf{y}-\mathbf{A}\hat{\mathbf{x}})+\mathbf{A}(\hat{\mathbf{x}}-\mathbf{x})$. The first term is the residual $\mathbf{r}$ for $\hat{\mathbf{x}}$; the second lies in the column space. By the normal equations, $\mathbf{r}$ is perpendicular to the column space, and the Pythagorean theorem gives [(3.4)](#gl-3-4). The second term on the right is never negative, so $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert\ge\lVert\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}\rVert$ for every $\mathbf{x}$.

If $\mathbf{x}$ is also a best approximate solution, both lengths are equal, and [(3.4)](#gl-3-4) forces $\mathbf{A}(\mathbf{x}-\hat{\mathbf{x}})=\mathbf{0}$. Then $\mathbf{A}\mathbf{x}=\mathbf{A}\hat{\mathbf{x}}$, so both give the same point and the same residual, and $\mathbf{x}$ satisfies the normal equations as well.
:::

⁠**Worked example:** For $\mathbf{H}$, $\mathbf{y}=(1,\,1,\,1)^{\top}$ and $\mathbf{x}=(1,\,0)^{\top}$, we have $\lVert\mathbf{y}-\mathbf{H}\mathbf{x}\rVert^2=1$. The right-hand side of [(3.4)](#gl-3-4) is $\lVert\mathbf{r}\rVert^2=\tfrac13$ plus $\lVert\mathbf{H}(\tfrac13,\,-\tfrac23)^{\top}\rVert^2=\lVert(\tfrac13,\,-\tfrac23,\,-\tfrac13)^{\top}\rVert^2=\tfrac69$, together $\tfrac13+\tfrac23=1$.

⁠**In short:** Pythagoras splits the squared error into the perpendicular residual, which no choice of $\mathbf{x}$ can make smaller, and a part in the column space, which vanishes at $\hat{\mathbf{x}}$.

:::hintergrund What you can influence and what you cannot
The formula [(3.4)](#gl-3-4) explains why the perpendicular position is exactly the right condition. Every candidate $\mathbf{A}\mathbf{x}$ lies in the column space. The distance to $\mathbf{y}$ is made up of two pieces at right angles to each other: a piece in the column space, from $\mathbf{A}\mathbf{x}$ to $\hat{\mathbf{y}}$, and the piece $\mathbf{r}$ perpendicular to it, from $\hat{\mathbf{y}}$ to $\mathbf{y}$. You can change the first piece at will through the choice of $\mathbf{x}$, and in particular bring it down to zero. The second does not depend on $\mathbf{x}$ at all: it is the part of $\mathbf{y}$ that the columns cannot reach with any linear combination. The best approximate solution is exactly the one that makes the piece you can influence zero. That the two pieces add up by Pythagoras and cannot cancel each other out is due to their right angle.
:::

### When the best approximate solution is unique

<span class="anker" id="stufe-3-5"></span>

The normal equations are a square system. Whether it has exactly one solution depends on whether $\mathbf{A}^{\top}\mathbf{A}$ is invertible. That in turn is decided by the columns of $\mathbf{A}$.

:::satz Theorem 3.5 (Invertibility of $\mathbf{A}^{\top}\mathbf{A}$)
<span class="anker" id="satz-3-5"></span>

The matrix $\mathbf{A}^{\top}\mathbf{A}$ is invertible if and only if the columns of $\mathbf{A}$ are linearly independent. Then the best approximate solution is unique:

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y} . \tag{3.5}$$
:::

:::beweis Invertibility
By Part 1, Section 13.5, the square matrix $\mathbf{A}^{\top}\mathbf{A}$ is invertible if and only if its null space contains only the zero vector. Let $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$. Then also $\mathbf{z}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=0$, that is, $\lVert\mathbf{A}\mathbf{z}\rVert^2=0$ and $\mathbf{A}\mathbf{z}=\mathbf{0}$. Conversely, $\mathbf{A}\mathbf{z}=\mathbf{0}$ immediately gives $\mathbf{A}^{\top}\mathbf{A}\mathbf{z}=\mathbf{0}$. So the two null spaces are equal. The null space of $\mathbf{A}$ contains only the zero vector if and only if the columns of $\mathbf{A}$ are linearly independent.
:::

If the columns are linearly dependent, there are infinitely many best approximate solutions. You may add any vector from the null space of $\mathbf{A}$ to one of them without changing $\mathbf{A}\hat{\mathbf{x}}$. The closest point $\hat{\mathbf{y}}$ is nevertheless unique, as the theorem in the previous subsection shows. This fits Part 1, Section 13.6: dependent features make the weights ambiguous, but not the predictions.

⁠**Worked example 1:** The columns of $\mathbf{H}$ are linearly independent, and $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ has the inverse $\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)$. With [(3.5)](#gl-3-5), $\hat{\mathbf{x}}=\tfrac13\bigl(\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr)(2,\,2)^{\top}=(\tfrac23,\,\tfrac23)^{\top}$, as above.

⁠**Worked example 2:** For $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ and $\mathbf{y}=(1,\,1)^{\top}$, the columns are dependent. The normal equations read $\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)\hat{\mathbf{x}}=(3,\,6)^{\top}$, which is the same equation $\hat x_1+2\hat x_2=\tfrac35$ twice. Every point of this line is a best approximate solution, for example $(\tfrac35,\,0)^{\top}$ or $(0,\,\tfrac3{10})^{\top}$. All of them give the same point $\hat{\mathbf{y}}=(\tfrac35,\,\tfrac65)^{\top}$, the projection of $\mathbf{y}$ onto the line in the direction of $(1,\,2)^{\top}$.

⁠**In short:** With linearly independent columns, $\mathbf{A}^{\top}\mathbf{A}$ is invertible and the best approximate solution $\hat{\mathbf{x}}=(\mathbf{A}^{\top}\mathbf{A})^{-1}\mathbf{A}^{\top}\mathbf{y}$ is unique; otherwise there are infinitely many, and they all give the same closest point.

### A line through three points

<span class="anker" id="stufe-3-6"></span>

Now the theory is complete, and it can be applied to an everyday task. Three data points $(t,\,y)=(0,\,1)$, $(1,\,2)$ and $(2,\,4)$ are to be described by a line $y=x_1+x_2\,t$. The three points do not lie on a common line. We are looking for the intercept $x_1$ and the slope $x_2$ that fit best.

Every data point gives an equation $x_1+x_2\,t_i=y_i$. With the column of ones for the intercept, as in Part 1, Section 8.5, this is the system

$$\mathbf{A}\mathbf{x}=\mathbf{y}\qquad\text{with}\qquad \mathbf{A}=\begin{pmatrix}1&0\\1&1\\1&2\end{pmatrix},\qquad \mathbf{y}=\begin{pmatrix}1\\2\\4\end{pmatrix}.$$

The components of the residual are the vertical distances of the data points from the line, measured in the $y$ direction (Fig. [8](#abb-8)). The best approximate solution makes the sum of their squares as small as possible. Such a line is called a __least-squares line__.

:::abbildung ml/k2ausgleich 8
The least-squares line through the data points $(0,1)$, $(1,2)$ and $(2,4)$. The red segments are the components of the residual, the vertical distances of the points from the line in the $y$ direction. The line makes the sum of their squares as small as possible, here $\tfrac1{36}+\tfrac19+\tfrac1{36}=\tfrac16$.
:::

⁠**Worked example:** We have

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&3\\3&5\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}7\\10\end{pmatrix},\qquad (\mathbf{A}^{\top}\mathbf{A})^{-1}=\frac16\begin{pmatrix}5&-3\\-3&3\end{pmatrix},$$

so $\hat{\mathbf{x}}=\tfrac16(35-30,\ -21+30)^{\top}=(\tfrac56,\,\tfrac32)^{\top}$. The entries of $\mathbf{A}^{\top}\mathbf{A}$ and $\mathbf{A}^{\top}\mathbf{y}$ are sums over the data points; Fig. [9](#abb-9) shows two of them. The least-squares line is $y=\tfrac56+\tfrac32\,t$. Its values at the data points are $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\,\tfrac73,\,\tfrac{23}6)^{\top}$, and the residual is $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$ with the sum of squares $\tfrac16$. Check: $\mathbf{A}^{\top}\mathbf{r}=(\tfrac16-\tfrac13+\tfrac16,\ 0-\tfrac13+\tfrac13)^{\top}=(0,\,0)^{\top}$.

The first component of the check has a meaning of its own. The first column of $\mathbf{A}$ is the column of ones, and $\mathbf{1}^{\top}\mathbf{r}=0$ means: the residuals add up to zero. On average, the line lies neither too high nor too low. Equivalently, it passes through the centroid of the data points, here $(\bar t,\,\bar y)=(1,\,\tfrac73)$: indeed, $\tfrac56+\tfrac32\cdot1=\tfrac73$.

:::abbildung ml/k2rausgleich 9
Two entries of the normal equations of the least-squares line as sums over the three data points $(t_i,\,y_i)=(0,1)$, $(1,2)$, $(2,4)$.
:::

⁠**In short:** A least-squares line is the best approximate solution of the system that requires all data points to lie on the line; with a column of ones, its residuals add up to zero.

:::hintergrund A filter that reproduces a signal as well as possible
The same calculation is used to design digital filters. A filter with the coefficients $h_0,\dots,h_{K-1}$ is supposed to reproduce a desired signal $d[n]$ as well as possible from an input signal $x[n]$, with the output $\sum_kh_k\,x[n-k]$. For every time step $n$ this is one equation for the $K$ unknowns $h_k$, so for many time steps it is an overdetermined system $\mathbf{X}\mathbf h=\mathbf d$. Row $n$ of $\mathbf{X}$ contains $x[n],x[n-1],\dots,x[n-K+1]$. In the normal equations $\mathbf{X}^{\top}\mathbf{X}\mathbf h=\mathbf{X}^{\top}\mathbf d$, the entry $(k,l)$ of $\mathbf{X}^{\top}\mathbf{X}$ is the sum $\sum_nx[n-k]\,x[n-l]$, which, apart from edge effects at the beginning and end of the signal, is the autocorrelation of $x$ at the lag $l-k$. The vector $\mathbf{X}^{\top}\mathbf d$ contains the cross-correlation of $d$ and $x$. These are exactly the dot products of shifted signals from Part 1, Section 2.4. By [(3.3)](#gl-3-3), the residual $d[n]-\sum_kh_k\,x[n-k]$ of the best filter is perpendicular to every shifted input signal: what the filter cannot reproduce has nothing in common with any of the signals from which it assembles its output.
:::

### The apartments: what Part 1 left open

<span class="anker" id="stufe-3-7"></span>

Now the question from the beginning of the section can be answered. We are looking for the weights for floor area and number of rooms that hit the four prices as well as possible.

⁠**Worked example:** For the system $\mathbf{A}\mathbf{w}=\mathbf{y}$ from the first subsection,

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}18\,200&730\\730&30\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}60\,100\\2\,410\end{pmatrix}.$$

Fig. [10](#abb-10) works out two of the entries.

:::abbildung ml/k2rwohnungen 10
Two entries of the normal equations of the apartments as dot products: $\mathbf{a}_1=(60,40,90,70)^{\top}$ is the floor-area column, $\mathbf{a}_2=(2,1,4,3)^{\top}$ the rooms column, $\mathbf{y}=(200,130,290,240)^{\top}$ the price vector.
:::

The two columns are linearly independent; the determinant is $18\,200\cdot30-730^2=13\,100$. With the inverse from Part 1, Section 11.3,

$$\hat{\mathbf{w}}=\frac1{13\,100}\begin{pmatrix}30&-730\\-730&18\,200\end{pmatrix}\begin{pmatrix}60\,100\\2\,410\end{pmatrix}=\frac1{13\,100}\begin{pmatrix}43\,700\\-11\,000\end{pmatrix}=\begin{pmatrix}437/131\\-110/131\end{pmatrix}\approx\begin{pmatrix}3.336\\-0.840\end{pmatrix}.$$

The estimated prices are $\mathbf{A}\hat{\mathbf{w}}\approx(198.47,\ 132.60,\ 296.87,\ 230.99)^{\top}$, and the residual is

$$\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{w}}=\frac{20}{131}\,(10,\,-17,\,-45,\,59)^{\top}\approx(1.53,\ -2.60,\ -6.87,\ 9.01)^{\top}$$

with length $\lVert\mathbf{r}\rVert\approx11.72$. The weights $(3,\,10)^{\top}$ from Part 1 hit three prices exactly but left a residual of length $20$. The best approximate solution hits no price exactly, but overall it is off by much less. Check: $\mathbf{A}^{\top}\mathbf{r}=\frac{20}{131}(600-680-4050+4130,\ 20-17-180+177)^{\top}=\mathbf{0}$.

⁠**In short:** The best approximate solution for the apartments is the weight vector $\hat{\mathbf{w}}\approx(3.336,\ -0.840)^{\top}$; with length $11.72$, its residual is much shorter than any residual that hits three prices exactly.

:::hintergrund Why the weight of the rooms is negative
A negative weight for the number of rooms looks wrong at first: more rooms should not lower the price. The calculation is nevertheless correct, and the reason lies in the data. In these four apartments, floor area and number of rooms grow together: the larger the apartment, the more rooms it has. The two columns of $\mathbf{A}$ therefore point in almost the same direction; by Part 1, Section 5.2, the cosine of their angle is $730/\sqrt{18\,200\cdot30}\approx0.988$, so the angle is only about $8.9^\circ$. The best combination takes a lot of the floor-area column and subtracts a little of the rooms column again in order to compensate for the deviations of the apartments from the common ratio. For the same floor area, more rooms here mean smaller rooms, and that can actually lower a price; but four apartments cannot show whether this is true. As in Part 1, Section 13.6: when features carry almost the same information, the individual weights say little, but the predictions say a lot.
:::

:::aufgabe Exercise 7 ★ Normal equations by hand
<span class="anker" id="aufg-7"></span>

The system $x_1=1$, $x_2=2$, $x_1+x_2=6$ has no solution.

<ol class="al">

<li>

Write it as $\mathbf{A}\mathbf{x}=\mathbf{y}$, set up the normal equations and solve them.

</li>

<li>

Compute the residual and check that it is perpendicular to both columns. By how much does the best approximate solution miss each of the three equations?

</li>

</ol>

:::loesung
(a) With $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ and $\mathbf{y}=(1,\,2,\,6)^{\top}$, we have $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ and $\mathbf{A}^{\top}\mathbf{y}=(1+6,\ 2+6)^{\top}=(7,\,8)^{\top}$. The normal equations $2\hat x_1+\hat x_2=7$, $\hat x_1+2\hat x_2=8$ have the solution

$$\hat{\mathbf{x}}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}7\\8\end{pmatrix}=\frac13\begin{pmatrix}6\\9\end{pmatrix}=\begin{pmatrix}2\\3\end{pmatrix}.$$

(b) $\mathbf{A}\hat{\mathbf{x}}=(2,\,3,\,5)^{\top}$ and $\mathbf{r}=\mathbf{y}-\mathbf{A}\hat{\mathbf{x}}=(-1,\,-1,\,1)^{\top}$. Check: $\mathbf{a}_1^{\top}\mathbf{r}=-1+0+1=0$ and $\mathbf{a}_2^{\top}\mathbf{r}=0-1+1=0$. Each of the three equations is missed by exactly $1$: $\hat x_1=2$ instead of $1$, $\hat x_2=3$ instead of $2$, $\hat x_1+\hat x_2=5$ instead of $6$. The best approximate solution spreads the contradiction evenly; $\lVert\mathbf{r}\rVert^2=3$.
:::
:::

:::aufgabe Exercise 8 ★★ A least-squares line
<span class="anker" id="aufg-8"></span>

Determine the least-squares line $y=x_1+x_2\,t$ through the points $(1,\,2)$, $(2,\,3)$ and $(3,\,5)$. Compute the residual, check $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$ and show that the line passes through the centroid of the three points.

:::loesung
With $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&2\\1&3\end{smallmatrix}\Bigr)$ and $\mathbf{y}=(2,\,3,\,5)^{\top}$,

$$\mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}3&6\\6&14\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}10\\23\end{pmatrix},\qquad \hat{\mathbf{x}}=\frac16\begin{pmatrix}14&-6\\-6&3\end{pmatrix}\begin{pmatrix}10\\23\end{pmatrix}=\frac16\begin{pmatrix}2\\9\end{pmatrix}=\begin{pmatrix}1/3\\3/2\end{pmatrix}.$$

The least-squares line is $y=\tfrac13+\tfrac32\,t$, with the values $\tfrac{11}6$, $\tfrac{10}3$, $\tfrac{29}6$ at the data points. The residual is $\mathbf{r}=(\tfrac16,\,-\tfrac13,\,\tfrac16)^{\top}$, and $\mathbf{A}^{\top}\mathbf{r}=\bigl(\tfrac16-\tfrac13+\tfrac16,\ \tfrac16-\tfrac23+\tfrac12\bigr)^{\top}=(0,\,0)^{\top}$. The centroid is $(\bar t,\,\bar y)=(2,\,\tfrac{10}3)$, and $\tfrac13+\tfrac32\cdot2=\tfrac{10}3$: the line passes through it. This follows from the first component of $\mathbf{A}^{\top}\mathbf{r}=\mathbf{0}$: the residuals add up to zero, so $\bar y=\hat x_1+\hat x_2\,\bar t$.
:::
:::

:::aufgabe Exercise 9 ★★ Base price and price per square meter
<span class="anker" id="aufg-9"></span>

The four apartments are to be estimated from their floor area alone, with a base price: $y\approx x_1+x_2\cdot\text{floor area}$.

<ol class="al">

<li>

Set up $\mathbf{A}$ with the column of ones and solve the normal equations.

</li>

<li>

Compute the residual and its length. Compare with the result in the last subsection.

</li>

</ol>

:::loesung
(a) The matrix has the column of ones and the floor-area column:

$$\mathbf{A}=\begin{pmatrix}1&60\\1&40\\1&90\\1&70\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{A}=\begin{pmatrix}4&260\\260&18\,200\end{pmatrix},\qquad \mathbf{A}^{\top}\mathbf{y}=\begin{pmatrix}860\\60\,100\end{pmatrix}.$$

The determinant is $4\cdot18\,200-260^2=72\,800-67\,600=5\,200$, and

$$\hat{\mathbf{x}}=\frac1{5\,200}\begin{pmatrix}18\,200&-260\\-260&4\end{pmatrix}\begin{pmatrix}860\\60\,100\end{pmatrix}=\frac1{5\,200}\begin{pmatrix}26\,000\\16\,800\end{pmatrix}=\begin{pmatrix}5\\42/13\end{pmatrix}\approx\begin{pmatrix}5\\3.231\end{pmatrix}.$$

The base price is $5$ thousand euros, plus about $3.23$ thousand euros per square meter.

(b) The estimated prices are $5+\tfrac{42}{13}\cdot\text{floor area}$, and the residual is

$$\mathbf{r}=\tfrac1{13}\,(15,\,-55,\,-75,\,115)^{\top}\approx(1.15,\ -4.23,\ -5.77,\ 8.85)^{\top},\qquad \lVert\mathbf{r}\rVert=\tfrac1{13}\sqrt{22\,100}\approx11.44 .$$

The residuals add up to zero, as the column of ones requires. With floor area and number of rooms, the length was $\lVert\mathbf{r}\rVert\approx11.72$; so base price and floor area, also with two unknowns, fit somewhat better. Which two columns you choose changes the column space and thus the closest point.
:::
:::

:::aufgabe Exercise 10 ★★★ Residuals without a column of ones
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Show: if the column space of $\mathbf{A}$ contains the all-ones vector $\mathbf{1}$, then the components of the residual of the best approximate solution add up to zero.

</li>

<li>

Check with the residual of the apartments from the last subsection that without a column of ones the sum of the residuals is in general not zero.

</li>

</ol>

:::loesung
(a) If $\mathbf{1}$ lies in the column space, then by the normal equations the residual of the best approximate solution is perpendicular to $\mathbf{1}$, because it is perpendicular to the whole column space. Hence $\mathbf{1}^{\top}\mathbf{r}=\sum_ir_i=0$.

(b) The residual of the apartments is $\tfrac{20}{131}(10,\,-17,\,-45,\,59)^{\top}$ with the sum $\tfrac{20}{131}(10-17-45+59)=\tfrac{140}{131}\approx1.07\ne0$. Without a column of ones, $\mathbf{1}$ does not lie in the column space here, and the residuals do not have to balance out.
:::
:::
