---
title: The condition number
pfad: Computer Science / Machine Learning / Projection, Eigenvalues and Decompositions
order: 6221300
summary: Measured data are never exact, and a computer rounds at every step.
tags: condition number
lang: en
---

<span class="anker" id="stufe-12"></span>

:::zweck
Measured data are never exact, and a computer rounds at every step. How much does the solution of a system of equations change when the right-hand side is slightly wrong? This section shows that a single number obtained from the singular values gives the answer, and what it means for the normal equations.
:::

### A sensitive system of equations

<span class="anker" id="stufe-12-1"></span>

The system of equations

$$x_1+x_2=2,\qquad x_1+1.01\,x_2=2.01$$

has the solution $\mathbf{x}=(1,\,1)^{\top}$. If you change the right-hand side of the second equation by $0.01$ to $2.02$, the difference of the equations gives $0.01\,x_2=0.02$, so $x_2=2$ and $x_1=0$. A change in the data in the third digit shifts the solution by its own size.

Geometrically, the two equations are two lines that intersect at the solution point. Here they are almost parallel; they intersect at an angle of only about $0.29^\circ$. If you shift one of them a little, the intersection point moves far along the other one (Fig. [28](#abb-28)). If the lines are perpendicular, by contrast, it moves only as far as the line is shifted.

:::abbildung ml/k2kondition 28
The same shift of the red line by the distance $0.2$ (dashed), shown twice. On the left, it intersects the blue line at a right angle, and the intersection point moves by $0.2$. On the right, the lines intersect at $8^\circ$, and the intersection point moves by $0.2/\sin8^\circ\approx1.44$. The flatter the angle of intersection, the more sensitively the solution reacts to changes in the data.
:::

How large is the effect, measured relative to the quantities themselves? The right-hand side $\mathbf{y}=(2,\ 2.01)^{\top}$ has the length $\sqrt{4+4.0401}\approx2.8355$ (Fig. [29](#abb-29)), and the change $\Delta\mathbf{y}=(0,\ 0.01)^{\top}$ has the length $0.01$. So the right-hand side changes by $0.01/2.8355\approx0.35\,\%$ in relative terms. The solution changes by $\Delta\mathbf{x}=(-1,\,1)^{\top}$, in relative terms by $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt2/\sqrt2=100\,\%$. The relative error is amplified about $284$-fold.

:::abbildung ml/k2rnormy 29
The squared length of the right-hand side as the dot product $\mathbf{y}^{\top}\mathbf{y}$; the length is $\sqrt{8.0401}\approx2.8355$.
:::

⁠**In short:** If the lines of a system of equations intersect almost in parallel, small changes in the data shift the solution a lot.

### The condition number

<span class="anker" id="stufe-12-2"></span>

Where does the factor come from? With the singular value decomposition, the amplification can be estimated precisely.

:::definition Definition 12.1 (Condition number)
<span class="anker" id="satz-12-1"></span>

Let $\mathbf{A}\in\mathbb{R}^{m\times n}$ have linearly independent columns, so $d_n>0$. The __condition number__ of $\mathbf{A}$ is

<span class="anker" id="gl-12-1"></span>
$$\kappa(\mathbf{A})=\frac{d_1}{d_n}, \tag{12.1}$$

the ratio of the largest to the smallest stretch.
:::

We always have $\kappa(\mathbf{A})\ge1$. An orthogonal matrix has $\kappa=1$, because all its singular values are $1$. A matrix with a large condition number is called ill-conditioned.

:::satz Theorem 12.2 (Error amplification)
<span class="anker" id="satz-12-2"></span>

Let $\mathbf{A}\in\mathbb{R}^{n\times n}$ be invertible, $\mathbf{A}\mathbf{x}=\mathbf{y}$ with $\mathbf{y}\ne\mathbf{0}$, and $\mathbf{A}(\mathbf{x}+\Delta\mathbf{x})=\mathbf{y}+\Delta\mathbf{y}$. Then

<span class="anker" id="gl-12-2"></span>
$$\frac{\lVert\Delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}\le\kappa(\mathbf{A})\,\frac{\lVert\Delta\mathbf{y}\rVert}{\lVert\mathbf{y}\rVert} . \tag{12.2}$$

Equality holds when $\mathbf{y}$ points in the direction of $\mathbf{u}_1$ and $\Delta\mathbf{y}$ in the direction of $\mathbf{u}_n$.
:::

:::beweis Error amplification
The two equations give $\mathbf{A}\Delta\mathbf{x}=\Delta\mathbf{y}$. By [(9.5)](die-singularwertzerlegung.html#gl-9-5), $\lVert\mathbf{y}\rVert=\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\lVert\mathbf{x}\rVert$, so $1/\lVert\mathbf{x}\rVert\le d_1/\lVert\mathbf{y}\rVert$, and $\lVert\Delta\mathbf{y}\rVert=\lVert\mathbf{A}\Delta\mathbf{x}\rVert\ge d_n\lVert\Delta\mathbf{x}\rVert$, so $\lVert\Delta\mathbf{x}\rVert\le\lVert\Delta\mathbf{y}\rVert/d_n$. Multiplying gives [(12.2)](#gl-12-2). If $\mathbf{y}$ points in the direction of $\mathbf{u}_1$, then $\mathbf{x}$ is a multiple of $\mathbf{v}_1$ and the first inequality is an equality; if $\Delta\mathbf{y}$ points in the direction of $\mathbf{u}_n$, then $\Delta\mathbf{x}$ is a multiple of $\mathbf{v}_n$ and the second one is an equality.
:::

So the worst case is this: the solution lies in the direction that $\mathbf{A}$ stretches most, so that $\mathbf{y}$ is large compared with $\mathbf{x}$, and the error lies in the direction that $\mathbf{A}$ stretches least, so that solving back enlarges it by $1/d_n$.

⁠**Worked example:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1.01\end{smallmatrix}\bigr)$ is symmetric with the trace $2.01$ and the determinant $0.01$. Its eigenvalues are

$$\lambda_{1,2}=\frac{2.01\pm\sqrt{2.01^2-0.04}}2=\frac{2.01\pm\sqrt{4.0001}}2\approx\frac{2.01\pm2.000025}2,$$

so $\lambda_1\approx2.005012$ and $\lambda_2\approx0.004988$, both positive. By Section [9.7](die-singularwertzerlegung.html#stufe-9-7), these are also the singular values, and $\kappa(\mathbf{A})\approx402$. The observed amplification $284$ lies below this. It does not quite reach the bound, because $\Delta\mathbf{y}=(0,\ 0.01)^{\top}$ does not point exactly in the direction of $\mathbf{u}_2\approx(1,\,-1)^{\top}/\sqrt2$. For $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, we have $\kappa=4/1=4$: relative errors are at most quadrupled.

⁠**In short:** The condition number $\kappa(\mathbf{A})=d_1/d_n$ is the largest factor by which $\mathbf{A}^{-1}$ can enlarge a relative error of the data in the solution.

### Condition number and determinant

<span class="anker" id="stufe-12-3"></span>

The background box in Part 1, Section 14.6, contained a warning: a small determinant does not mean that a matrix is nearly singular. The condition number measures what was meant there.

:::satz Theorem 12.3 (Distance to the nearest singular matrix)
<span class="anker" id="satz-12-3"></span>

For an invertible matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$, the smallest distance $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ to a singular matrix $\mathbf{B}$ equals $d_n$. Relative to the size $\lVert\mathbf{A}\rVert_2=d_1$, it is

<span class="anker" id="gl-12-3"></span>
$$\min_{\mathbf{B}\ \text{singular}}\frac{\lVert\mathbf{A}-\mathbf{B}\rVert_2}{\lVert\mathbf{A}\rVert_2}=\frac1{\kappa(\mathbf{A})} . \tag{12.3}$$
:::

:::beweis Distance
A singular matrix has rank at most $n-1$. By the Eckart–Young theorem with $k=n-1$, we have $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_n$, and the singular matrix $\mathbf{A}_{n-1}$ is at exactly the distance $d_n$.
:::

So a large condition number means: a relatively small change makes the matrix singular. The determinant measures something else. By Exercise [29](die-singularwertzerlegung.html#aufg-29), $|\det\mathbf{A}|=d_1\cdots d_n$, the product of all stretches; it depends on the size of the matrix. The condition number is a ratio and does not change when $\mathbf{A}$ is multiplied by a number: $\kappa(c\mathbf{A})=\kappa(\mathbf{A})$ for $c\ne0$. It only measures how flat the ellipse is into which $\mathbf{A}$ transforms the unit circle.

⁠**Worked example:** The two matrices from Part 1, Section 14.6: $0.1\cdot\mathbf{I}_{10}$ has the determinant $10^{-10}$, but all singular values are $0.1$ and $\kappa=1$; it is as well conditioned as possible. $\operatorname{diag}(1000,\ 0.001)$ has the determinant $1$, but $\kappa=1000/0.001=10^6$. For $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1.01\end{smallmatrix}\bigr)$, the distance to the nearest singular matrix is $d_2\approx0.005$: changing entries by a few thousandths makes it singular. The singular matrix $\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ is at the distance $\lVert\bigl(\begin{smallmatrix}0&0\\0&0.01\end{smallmatrix}\bigr)\rVert_2=0.01$, slightly more than the minimum.

⁠**In short:** $1/\kappa(\mathbf{A})$ is the relative distance to the nearest singular matrix; the determinant says nothing about this, because it depends on the size of the matrix.

### The normal equations square the condition number

<span class="anker" id="stufe-12-4"></span>

The best approximate solution can be computed via the normal equations $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ or via the QR decomposition, $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$. Mathematically, both give the same result. With rounded numbers they do not, and the reason is the condition number.

:::satz Theorem 12.4 (Condition number of the Gram matrix)
<span class="anker" id="satz-12-4"></span>

If $\mathbf{A}$ has linearly independent columns, then

<span class="anker" id="gl-12-4"></span>
$$\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2 . \tag{12.4}$$

For the QR decomposition $\mathbf{A}=\mathbf{Q}\mathbf{R}$, on the other hand, we have $\kappa(\mathbf{R})=\kappa(\mathbf{A})$.
:::

:::beweis Gram matrix
$\mathbf{A}^{\top}\mathbf{A}$ is symmetric and positive definite with the eigenvalues $d_j^2$; by Section [9.7](die-singularwertzerlegung.html#stufe-9-7), these are also its singular values, and their ratio is $d_1^2/d_n^2$. Because $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$, we have $\mathbf{R}^{\top}\mathbf{R}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{A}^{\top}\mathbf{A}$; so $\mathbf{R}$ has the same singular values as $\mathbf{A}$.
:::

⁠**Worked example:** The apartment matrix from Section [3.7](die-beste-naherungslosung.html#stufe-3-7), with floor area and number of rooms, has the singular values $d_1\approx135.02$ and $d_2\approx0.848$, so $\kappa(\mathbf{A})\approx159.3$ and $\kappa(\mathbf{A}^{\top}\mathbf{A})\approx25\,367$. Two causes make $\kappa(\mathbf{A})$ large. First, the units: the floor areas are numbers around $65$, the numbers of rooms around $2.5$. If you measure the floor area in units of $10\,\mathrm m^2$, the condition number drops to about $18.5$. Second, the two columns point in almost the same direction; the angle between them is only about $8.9^\circ$. That is why $\kappa\approx12.8$ remains even if you scale both columns to length $1$. Converting the units does not change the fitted values $\hat{\mathbf{y}}$: if you divide a column by $10$, the corresponding weight becomes $10$ times as large, and the products stay the same.

⁠**In short:** The normal equations work with $\kappa(\mathbf{A})^2$, the QR decomposition with $\kappa(\mathbf{A})$; well-chosen units lower the condition number.

:::hintergrund What the computer does with the condition number
A computer usually stores numbers with about $16$ significant decimal digits and rounds after every arithmetic operation. A good method delivers the exact solution of a problem whose data have been changed only by the order of magnitude of this rounding; such methods are called backward stable. By [(12.2)](#gl-12-2), the result then has a relative error of at most about $\kappa\cdot10^{-16}$: you lose roughly $\log_{10}\kappa$ of the $16$ digits.

The route via the QR decomposition (and via the singular value decomposition) is backward stable; for a small residual, its error grows roughly like $\kappa(\mathbf{A})$. The route via the normal equations is not: it works with the matrix $\mathbf{A}^{\top}\mathbf{A}$, and its error always grows like $\kappa(\mathbf{A})^2$, even when the residual is small. At $\kappa(\mathbf{A})=10^6$ you lose about $12$ of the $16$ digits on this route, and about $6$ with QR. For the apartments, with $\kappa(\mathbf{A})^2\approx2.5\cdot10^4$, this is still harmless; for large data sets with nearly dependent features it is not. That is why good software computes the best approximate solution via QR or the singular value decomposition, not via the normal equations, even though these describe the theory most concisely.
:::

:::aufgabe Exercise 36 ★ Reading off condition numbers
<span class="anker" id="aufg-36"></span>

Determine the condition number of

<ol class="al">

<li>

$\operatorname{diag}(2,\ 0.5)$ and $\operatorname{diag}(-3,\ 3)$;

</li>

<li>

the rotation matrix for the angle $30^\circ$;

</li>

<li>

$5\mathbf{A}$ for $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$. Compare the determinants of $\mathbf{A}$ and $5\mathbf{A}$.

</li>

</ol>

:::loesung
(a) $\operatorname{diag}(2,\,0.5)$ has the singular values $2$ and $0.5$, so $\kappa=4$. By Section [9.7](die-singularwertzerlegung.html#stufe-9-7), $\operatorname{diag}(-3,\,3)$ has the singular values $3$ and $3$, so $\kappa=1$, even though the eigenvalues have different signs.

(b) A rotation matrix is orthogonal, and all its singular values are $1$: $\kappa=1$.

(c) $5\mathbf{A}$ has the singular values $20$ and $5$, so again $\kappa=4$. The determinant, by contrast, grows from $4$ to $\det(5\mathbf{A})=25\cdot4=100$.
:::
:::

:::aufgabe Exercise 37 ★★ Large determinant, poor conditioning
<span class="anker" id="aufg-37"></span>

Let $\mathbf{A}=\bigl(\begin{smallmatrix}10&7\\7&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Compute $\det\mathbf{A}$ and $\mathbf{A}^{-1}$. Solve $\mathbf{A}\mathbf{x}=(17,\,12)^{\top}$ and $\mathbf{A}\mathbf{x}=(17,\ 12.1)^{\top}$.

</li>

<li>

Compute the relative changes of $\mathbf{y}$ and $\mathbf{x}$ and their ratio.

</li>

<li>

Compute $\kappa(\mathbf{A})$ and check [(12.2)](#gl-12-2). How far is $\mathbf{A}$ from the nearest singular matrix?

</li>

</ol>

:::loesung
(a) $\det\mathbf{A}=50-49=1$ and $\mathbf{A}^{-1}=\bigl(\begin{smallmatrix}5&-7\\-7&10\end{smallmatrix}\bigr)$. Hence $\mathbf{A}^{-1}(17,\,12)^{\top}=(85-84,\ -119+120)^{\top}=(1,\,1)^{\top}$ and $\mathbf{A}^{-1}(17,\ 12.1)^{\top}=(85-84.7,\ -119+121)^{\top}=(0.3,\ 2)^{\top}$.

(b) $\lVert\Delta\mathbf{y}\rVert/\lVert\mathbf{y}\rVert=0.1/\sqrt{433}\approx0.1/20.809\approx0.48\,\%$. Further, $\Delta\mathbf{x}=(-0.7,\ 1)^{\top}$, so $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt{1.49}/\sqrt2\approx1.2207/1.4142\approx86.3\,\%$. The ratio is about $180$.

(c) $\mathbf{A}$ is symmetric with trace $15$ and determinant $1$, so $\lambda=\tfrac{15\pm\sqrt{221}}2\approx14.933$ and $0.0670$, both positive. By Section [9.7](die-singularwertzerlegung.html#stufe-9-7), these are the singular values, and $\kappa(\mathbf{A})\approx14.933/0.0670\approx223$. The bound [(12.2)](#gl-12-2) is satisfied: $86.3\,\%\le223\cdot0.48\,\%\approx107\,\%$. The distance to the nearest singular matrix is $d_2\approx0.067$, or $1/223$ in relative terms. The determinant $1$ reveals nothing of this.
:::
:::

:::aufgabe Exercise 38 ★★★ Rules for the condition number
<span class="anker" id="aufg-38"></span>

Let $\mathbf{A}\in\mathbb{R}^{n\times n}$ be invertible and $\mathbf{Q}$ orthogonal. Show:

<ol class="al">

<li>

$\kappa(\mathbf{Q}\mathbf{A})=\kappa(\mathbf{A})$ and $\kappa(\mathbf{A}^{-1})=\kappa(\mathbf{A})$;

</li>

<li>

$|\lambda|/|\mu|\le\kappa(\mathbf{A})$ for all eigenvalues $\lambda$ and $\mu$ of $\mathbf{A}$;

</li>

<li>

if $\mathbf{A}$ is symmetric, then $\kappa(\mathbf{A})=|\lambda|_{\max}/|\lambda|_{\min}$, the ratio of the eigenvalue of largest magnitude to the eigenvalue of smallest magnitude.

</li>

</ol>

:::loesung
(a) By Exercise [29](die-singularwertzerlegung.html#aufg-29), $\mathbf{Q}\mathbf{A}$ has the same singular values as $\mathbf{A}$, and hence the same condition number. From $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ it follows that $\mathbf{A}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$, a singular value decomposition with the singular values $1/d_j$. The largest is $1/d_n$, the smallest $1/d_1$, so $\kappa(\mathbf{A}^{-1})=\tfrac{1/d_n}{1/d_1}=\tfrac{d_1}{d_n}=\kappa(\mathbf{A})$.

(b) For an eigenvector $\mathbf{v}$ belonging to $\lambda$, [(9.5)](die-singularwertzerlegung.html#gl-9-5) gives $d_n\lVert\mathbf{v}\rVert\le\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert\le d_1\lVert\mathbf{v}\rVert$, so $d_n\le|\lambda|\le d_1$; this holds for complex eigenvectors as well, as shown in Section [9.8](die-singularwertzerlegung.html#stufe-9-8). The same holds for $\mu$. Hence $|\lambda|/|\mu|\le d_1/d_n$.

(c) For symmetric $\mathbf{A}$, by Section [9.7](die-singularwertzerlegung.html#stufe-9-7), the singular values are the magnitudes $|\lambda_i|$. The largest singular value is therefore $|\lambda|_{\max}$, the smallest $|\lambda|_{\min}$.
:::
:::
