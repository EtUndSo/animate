---
title: Differentiating with respect to vectors and matrices
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15230800
summary: Gradients of expressions such as a top x , x top Ax or lVerty-AxrVert 2 are needed again and again.
tags: layout convention
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
Gradients of expressions such as $\mathbf{a}^{\top}\mathbf{x}$, $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ or $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ are needed again and again. This section first fixes the shape of each derivative and then derives the most important formulas componentwise. At the end come derivatives with respect to a matrix and the rule with which you compute a sensitivity backward through a matrix product.
:::

### The layout convention

<span class="anker" id="stufe-7-1"></span>

For functions of one variable, the derivative is a number, and there is nothing to arrange. For vectors and matrices, you have to decide in which shape the many partial derivatives are written down: as a column or as a row, as an $m\times n$ or as an $n\times m$ matrix. Such a decision is called a __layout convention__. Mathematically, every choice is equally good; you just have to stick to it, otherwise formulas suddenly appear transposed.

:::definition Definition 7.1 (Layout convention of this chapter)
<span class="anker" id="satz-7-1"></span>

<ol class="rm">

<li>

Vectors are columns. The gradient of a function $f:\mathbb{R}^n\to\mathbb{R}$ is a column with the same shape as $\mathbf{x}$.

</li>

<li>

The Jacobian matrix of a function $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ is an $m\times n$ matrix: one row per output, one column per input.

</li>

<li>

The derivative of a function $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ with respect to a matrix $\mathbf{A}$ is an $m\times n$ matrix $\nabla_{\mathbf{A}}f$ with the entry $\partial f/\partial a_{ij}$ in position $(i,j)$, that is, with the same shape as $\mathbf{A}$.

</li>

</ol>
:::

Table [2](#tab-2) summarizes this. The chapter has already used two consequences: for a function with one output, the Jacobian matrix is the gradient as a row, $\mathbf{J}_f=\nabla f^{\top}$. And the chain rule for gradients needs the transpose, $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$. Rule (iii) is needed in Section [7.5](#stufe-7-5): if you change a matrix by a small matrix $\mathbf E$, you want to be able to compare $\nabla_{\mathbf{A}}f$ and $\mathbf E$ entry by entry.

<span class="anker" id="tab-2"></span>

**Table 2:** The shape of the derivative depending on the type of function, in the convention of this chapter.

| Function | Derivative | Shape |
|---|---|---|
| $f:\mathbb{R}\to\mathbb{R}$ | $f'(x)$ | number |
| $f:\mathbb{R}^n\to\mathbb{R}$ | $\nabla f(\mathbf{x})$ | column, $n\times1$ (like $\mathbf{x}$) |
| $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ | $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ | $m\times n$ (row $i$ is $\nabla g_i^{\top}$) |
| $f:\mathbb{R}^{m\times n}\to\mathbb{R}$ | $\nabla_{\mathbf{A}}f(\mathbf{A})$ | $m\times n$ (like $\mathbf{A}$) |

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$ at the point $(1,\,2)$, the gradient is the column $\nabla f=(4,\,5)^{\top}$ and the Jacobian matrix is the row $\mathbf{J}_f=(4\ \ 5)$. For $\mathbf{g}$ from [(5.1)](die-jacobi-matrix.html#gl-5-1), $\mathbf{J}_{\mathbf{g}}$ is a $2\times2$ matrix whose first row $(2\ \ 1)$ is the gradient of $g_1=x_1x_2$ as a row.
::::

⁠**In short:** In this chapter, a gradient has the shape of its variable, and a Jacobian matrix has one row per output; from this follow $\mathbf{J}_f=\nabla f^{\top}$ and the transpose in the chain rule for gradients.

:::hintergrund Other conventions in the literature
Many books write the gradient as a row. Then it is the same as the Jacobian matrix of a function with one output, and the chain rule needs no transposing at all, because $\nabla(f\circ\mathbf{g})=\nabla f\,\mathbf{J}_{\mathbf{g}}$ is then a product of a row and a matrix. The price is that the gradient no longer has the shape of $\mathbf{x}$; the line $\mathbf{x}+t\,\nabla f$ in the direction of steepest ascent then needs a transpose. Two arrangements are distinguished. In the numerator layout, the rows follow the components of the function, as with the Jacobian matrix of this chapter. In the denominator layout, they follow the components of the variable; then the derivative of a vector-valued function is the transpose of the Jacobian matrix. This chapter uses a common mixed layout: gradient as a column and Jacobian matrix in numerator layout. You must therefore not combine formulas from different sources without checking them. A quick check is the shape: a gradient with respect to $\mathbf{x}\in\mathbb{R}^n$ must have $n$ entries in a column. A more reliable check is a small numerical example.
:::

### Linear functions

<span class="anker" id="stufe-7-2"></span>

The simplest function of many variables is the weighted sum. Its gradient is so simple that you can write it down immediately; the derivation shows the pattern by which all further formulas of this section arise.

:::satz Theorem 7.2 (Gradients of linear functions)
<span class="anker" id="satz-7-2"></span>

For fixed vectors $\mathbf{a},\mathbf{y}$ and a fixed matrix $\mathbf{A}$ of matching shape,

<span class="anker" id="gl-7-1"></span>
$$\nabla_{\mathbf{x}}(\mathbf{a}^{\top}\mathbf{x})=\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{a})=\mathbf{a},\qquad \nabla_{\mathbf{x}}(\mathbf{y}^{\top}\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\mathbf{y} . \tag{7.1}$$
:::

:::beweis Gradients of linear functions
We have $\mathbf{a}^{\top}\mathbf{x}=\sum_ja_jx_j$. Differentiating with respect to $x_k$, only the term with $j=k$ remains, that is, $a_k$. Because $\mathbf{x}^{\top}\mathbf{a}=\mathbf{a}^{\top}\mathbf{x}$, the same holds for $\mathbf{x}^{\top}\mathbf{a}$. For the second part, set $\mathbf{a}=\mathbf{A}^{\top}\mathbf{y}$, because $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}^{\top}\mathbf{y})^{\top}\mathbf{x}$.
:::

::::beispiel [Worked example]
In [Chapter 1, Section 2.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2), the prediction for apartment 1 with $\mathbf{x}_1=(60,\,2,\,3)^{\top}$ and the weights $\mathbf{w}=(3,\,10,\,-4)^{\top}$ was $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$. As a function of the weights, it has the gradient $\nabla_{\mathbf{w}}\hat y_1=\mathbf{x}_1=(60,\,2,\,3)^{\top}$. If you increase $w_1$ by $0.1$, the prediction rises by $60\cdot0.1=6$ to $194$; indeed, $3.1\cdot60+10\cdot2-4\cdot3=194$. The reason is simple: each weight is multiplied by its feature, and therefore the sensitivity with respect to a weight is exactly the corresponding feature.
::::

⁠**In short:** The gradient of $\mathbf{a}^{\top}\mathbf{x}$ with respect to $\mathbf{x}$ is $\mathbf{a}$; that of $\mathbf{y}^{\top}\mathbf{A}\mathbf{x}$ is $\mathbf{A}^{\top}\mathbf{y}$.

### Quadratic forms

<span class="anker" id="stufe-7-3"></span>

Quadratic forms $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ from [Chapter 2, Section 5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5), appear wherever squares are summed. When you differentiate, $\mathbf{x}$ appears in two places, and both contribute, like the two paths in Section [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2).

:::satz Theorem 7.3 (Gradient of a quadratic form)
<span class="anker" id="satz-7-3"></span>

For a matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$,

<span class="anker" id="gl-7-2"></span>
$$\nabla_{\mathbf{x}}(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\,\mathbf{x} . \tag{7.2}$$

If $\mathbf{A}$ is symmetric, this is $2\mathbf{A}\mathbf{x}$. In particular, $\nabla\lVert\mathbf{x}\rVert^2=\nabla(\mathbf{x}^{\top}\mathbf{x})=2\mathbf{x}$.
:::

:::beweis Gradient of a quadratic form
We have $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{j=1}^nx_i\,a_{ij}\,x_j$. Differentiating with respect to $x_k$, two groups of terms contribute: those with $i=k$, whose derivative is $\sum_ja_{kj}x_j=(\mathbf{A}\mathbf{x})_k$, and those with $j=k$, whose derivative is $\sum_ix_ia_{ik}=(\mathbf{A}^{\top}\mathbf{x})_k$. The term with $i=j=k$ is $a_{kk}x_k^2$ and has the derivative $2a_{kk}x_k$; it is contained once in each of the two groups, with $a_{kk}x_k$. So component $k$ of the gradient is $(\mathbf{A}\mathbf{x})_k+(\mathbf{A}^{\top}\mathbf{x})_k$.
:::

By [Chapter 2, Section 5.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-2), the quadratic form depends only on the symmetric part $\mathbf{S}=\tfrac12(\mathbf{A}+\mathbf{A}^{\top})$. The formula fits this: $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=2\mathbf{S}\mathbf{x}$.

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&3\end{smallmatrix}\bigr)$, $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=x_1^2+2x_1x_2+3x_2^2$, so at the point $\mathbf{x}=(1,\,1)^{\top}$ it is $6$. By [(7.2)](#gl-7-2),

$$\nabla f(1,1)=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}=\begin{pmatrix}2&2\\2&6\end{pmatrix}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}2+2\\2+6\end{pmatrix}=\begin{pmatrix}4\\8\end{pmatrix}.$$

Check with the partial derivatives $2x_1+2x_2=4$ and $2x_1+6x_2=8$. The formula $2\mathbf{A}\mathbf{x}=(6,\,6)^{\top}$, which holds only for symmetric matrices, would be wrong here.
::::

⁠**In short:** The gradient of $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ is $(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$, so $2\mathbf{A}\mathbf{x}$ for symmetric $\mathbf{A}$, and that of $\lVert\mathbf{x}\rVert^2$ is $2\mathbf{x}$.

### The sum of squares of a residual

<span class="anker" id="stufe-7-4"></span>

In [Chapter 2, Section 3](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3), the residual $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}$ was the error vector of a system of equations $\mathbf{A}\mathbf{x}=\mathbf{y}$ that has no solution, and we were looking for the $\mathbf{x}$ with the shortest residual. The sum of squares $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ is a function of $\mathbf{x}$, and its gradient tells how it responds to a change in $\mathbf{x}$.

:::satz Theorem 7.4 (Gradient of the sum of squares)
<span class="anker" id="satz-7-4"></span>

For $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ with $\mathbf{A}\in\mathbb{R}^{m\times n}$ and $\mathbf{y}\in\mathbb{R}^m$,

<span class="anker" id="gl-7-3"></span>
$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})=2\mathbf{A}^{\top}(\mathbf{A}\mathbf{x}-\mathbf{y}). \tag{7.3}$$
:::

:::beweis Gradient of the sum of squares
The function is a composition: first the affine map $\mathbf{r}(\mathbf{x})=\mathbf{y}-\mathbf{A}\mathbf{x}$ forms the residual, then $\mathbf{r}\mapsto\lVert\mathbf{r}\rVert^2$ forms its sum of squares. By Section [5.4](die-jacobi-matrix.html#stufe-5-4), $\mathbf{J}_{\mathbf{r}}=-\mathbf{A}$; by [(7.2)](#gl-7-2), $\nabla_{\mathbf{r}}\lVert\mathbf{r}\rVert^2=2\mathbf{r}$. The chain rule [(6.3)](die-kettenregel-fur-mehrere-variablen.html#gl-6-3) gives $\nabla f=(-\mathbf{A})^{\top}\,2\mathbf{r}=-2\mathbf{A}^{\top}\mathbf{r}$.
:::

::::beispiel [Worked example]
Let $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$, $\mathbf{y}=(1,\,0)^{\top}$ and $\mathbf{x}=(2,\,1)^{\top}$. Then $\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$, the residual is $\mathbf{r}=(-3,\,-1)^{\top}$ and $f(\mathbf{x})=9+1=10$. With $\mathbf{A}^{\top}\mathbf{r}=(-3,\,-7)^{\top}$,

$$\nabla f(\mathbf{x})=-2\mathbf{A}^{\top}\mathbf{r}=-2\begin{pmatrix}-3\\-7\end{pmatrix}=\begin{pmatrix}6\\14\end{pmatrix}$$

(Fig. [13](#abb-13)). Check: written out, $f(\mathbf{x})=(1-x_1-2x_2)^2+x_2^2$ with the partial derivatives $-2\,(1-x_1-2x_2)=6$ and $-4\,(1-x_1-2x_2)+2x_2=12+2=14$.

:::abbildung ml/k3rresiduum 13
The gradient of the sum of squares $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$: each component of $\mathbf{A}^{\top}\mathbf{r}$ is the dot product of a column of $\mathbf{A}$ with the residual.
:::
::::

The formula connects with [Chapter 2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html). There, the residual of the best approximate solution $\hat{\mathbf{x}}$ was perpendicular to all columns of $\mathbf{A}$, that is, $\mathbf{A}^{\top}\hat{\mathbf{r}}=\mathbf{0}$, and from this followed the normal equations $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$. By [(7.3)](#gl-7-3), this means: at the point $\hat{\mathbf{x}}$, the gradient of the sum of squares is zero; there it rises or falls in no direction, apart from second-order terms. For the example from [Chapter 2, Section 3.3](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-3), with the matrix $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$, $\mathbf{y}=(1,\,1,\,1)^{\top}$ and $\hat{\mathbf{x}}=(\tfrac23,\,\tfrac23)^{\top}$, we get $\hat{\mathbf{r}}=(\tfrac13,\,\tfrac13,\,-\tfrac13)^{\top}$ and $\mathbf{A}^{\top}\hat{\mathbf{r}}=(\tfrac13-\tfrac13,\ \tfrac13-\tfrac13)^{\top}=\mathbf{0}$.

⁠**In short:** The gradient of $\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ is $-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$; it vanishes exactly where the residual is perpendicular to the columns of $\mathbf{A}$.

### Differentiating with respect to a matrix

<span class="anker" id="stufe-7-5"></span>

Sometimes the variable is not a vector but a whole matrix: how does a number change if you change one entry of a matrix? By rule (iii) of the convention, you arrange the $m\cdot n$ partial derivatives in the shape of the matrix. Then the linear approximation holds as usual, except that the dot product runs over all entries:

<span class="anker" id="gl-7-4"></span>
$$f(\mathbf{A}+\mathbf E)\approx f(\mathbf{A})+\sum_{i=1}^m\sum_{j=1}^n\bigl(\nabla_{\mathbf{A}}f\bigr)_{ij}\,e_{ij} \tag{7.4}$$

for a small matrix $\mathbf E$ with the entries $e_{ij}$. The double sum is the same as $\operatorname{tr}\bigl((\nabla_{\mathbf{A}}f)^{\top}\mathbf E\bigr)$ with the trace from [Chapter 2, Section 6.5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5).

:::satz Theorem 7.5 (Two derivatives with respect to a matrix)
<span class="anker" id="satz-7-5"></span>

For fixed vectors $\mathbf{u}\in\mathbb{R}^m$, $\mathbf{v}\in\mathbb{R}^n$ and a matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$,

<span class="anker" id="gl-7-5"></span>
$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top},\qquad \nabla_{\mathbf{A}}\lVert\mathbf{A}\rVert_F^2=2\mathbf{A} . \tag{7.5}$$

Here $\lVert\mathbf{A}\rVert_F$ is the Frobenius norm from [Chapter 2, Section 10.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/naherung-durch-matrizen-von-kleinem-rang.html#stufe-10-1).
:::

:::beweis Two derivatives with respect to a matrix
We have $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\sum_i\sum_ju_i\,a_{ij}\,v_j$. The entry $a_{ij}$ occurs in exactly one term, with the factor $u_iv_j$. So $\partial(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})/\partial a_{ij}=u_iv_j$, and that is entry $(i,j)$ of the outer product $\mathbf{u}\mathbf{v}^{\top}$ from [Chapter 1, Section 9.5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5). Likewise, $\lVert\mathbf{A}\rVert_F^2=\sum_{i,j}a_{ij}^2$, and $\partial/\partial a_{ij}$ of it is $2a_{ij}$.
:::

::::beispiel [Worked example]
For $\mathbf{u}=(1,\,2)^{\top}$ and $\mathbf{v}=(3,\,-1)^{\top}$,

$$\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}=\begin{pmatrix}3&-1\\6&-2\end{pmatrix},$$

at every point $\mathbf{A}$, because the function is linear in $\mathbf{A}$. For $\mathbf{A}=\mathbf{I}$, $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}=3-2=1$. If you increase the entry $a_{21}$ by $0.1$, the gradient predicts a change of $6\cdot0.1=0.6$. Indeed, $a_{21}$ occurs only in the term $u_2\,a_{21}\,v_1=2\cdot a_{21}\cdot3$, and that term grows by $0.6$.
::::

⁠**In short:** The derivative of a number with respect to a matrix has the shape of the matrix; for $\mathbf{u}^{\top}\mathbf{A}\mathbf{v}$ it is the outer product $\mathbf{u}\mathbf{v}^{\top}$, for $\lVert\mathbf{A}\rVert_F^2$ it is $2\mathbf{A}$.

### Backward through a matrix product

<span class="anker" id="stufe-7-6"></span>

Often a matrix–vector product $\mathbf{y}=\mathbf{A}\mathbf{x}$ is only an intermediate step of a longer calculation that ends with a number $f(\mathbf{y})$. If you already know how this number responds to $\mathbf{y}$, that is, $\nabla f(\mathbf{y})$, you want to read off from it how the number responds to $\mathbf{A}$ and to $\mathbf{x}$. This calculation backward through a building block is the pattern for reverse mode in Section [10](automatische-differentiation.html#stufe-10).

:::satz Theorem 7.6 (Backward rule of the matrix product)
<span class="anker" id="satz-7-6"></span>

Let $f:\mathbb{R}^m\to\mathbb{R}$ be differentiable, $\mathbf{y}=\mathbf{A}\mathbf{x}$ with $\mathbf{A}\in\mathbb{R}^{m\times n}$ and $F(\mathbf{A},\mathbf{x})=f(\mathbf{A}\mathbf{x})$. Then

<span class="anker" id="gl-7-6"></span>
$$\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\,\nabla f(\mathbf{y}). \tag{7.6}$$

More generally, for $\mathbf{C}=\mathbf{A}\mathbf{B}$ and $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$: $\nabla_{\mathbf{A}}F=(\nabla_{\mathbf{C}}f)\,\mathbf{B}^{\top}$ and $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\,(\nabla_{\mathbf{C}}f)$.
:::

:::beweis Backward rule of the matrix product
We have $y_i=\sum_ka_{ik}x_k$. The entry $a_{ij}$ affects only $y_i$, namely with the factor $\partial y_i/\partial a_{ij}=x_j$. So there is only one path from $a_{ij}$ to $f$, and $\partial F/\partial a_{ij}=\frac{\partial f}{\partial y_i}\,x_j$; that is entry $(i,j)$ of $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$. The variable $x_j$, on the other hand, affects every $y_i$, with the factor $a_{ij}$; summed over all paths, $\partial F/\partial x_j=\sum_i\frac{\partial f}{\partial y_i}\,a_{ij}$, component $j$ of $\mathbf{A}^{\top}\nabla f(\mathbf{y})$. The second statement follows in the same way, because $\mathbf{C}=\mathbf{A}\mathbf{B}$ is, column by column, a matrix–vector product.
:::

::::beispiel [Worked example]
In [Chapter 1, Section 7.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-1), we had $\mathbf{A}=\Bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\Bigr)$ and $\mathbf{x}=(2,\,1)^{\top}$, so $\mathbf{y}=\mathbf{A}\mathbf{x}=(4,\,-1,\,7)^{\top}$. Let $f(\mathbf{y})=y_1-y_3=-3$, so $\nabla f(\mathbf{y})=(1,\,0,\,-1)^{\top}$. By [(7.6)](#gl-7-6),

$$\nabla_{\mathbf{A}}F=\begin{pmatrix}1\\0\\-1\end{pmatrix}\begin{pmatrix}2&1\end{pmatrix}=\begin{pmatrix}2&1\\0&0\\-2&-1\end{pmatrix},\qquad \nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\begin{pmatrix}1\\0\\-1\end{pmatrix}=\begin{pmatrix}-2\\1\end{pmatrix}$$

(Fig. [14](#abb-14)). Check: written out, $F=(x_1+2x_2)-(3x_1+x_2)=-2x_1+x_2$ with the gradient $(-2,\,1)^{\top}$. The second row of $\nabla_{\mathbf{A}}F$ is zero because $y_2$ does not occur in $f$; the entries of the second row of $\mathbf{A}$ act only on $y_2$.

:::abbildung ml/k3rrueck 14
The gradient with respect to the input of a matrix–vector product: each component collects, over all three outputs $y_i$, how strongly $f$ responds to $y_i$, weighted by the factor $a_{ij}$ with which $x_j$ acts on $y_i$.
:::
::::

:::warnung The shape check is a mnemonic, not a proof
The shapes almost determine [(7.6)](#gl-7-6): $\nabla_{\mathbf{A}}F$ must have the shape $m\times n$, and from the column $\nabla f(\mathbf{y})$ with $m$ entries and the column $\mathbf{x}$ with $n$ entries, only $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$ gives this shape. This is a way to remember the rule. But the shape check detects neither a wrong sign nor a missing factor nor a swapped order for square matrices. Only the calculation with the components justifies the rule.
:::

⁠**In short:** Backward through $\mathbf{y}=\mathbf{A}\mathbf{x}$: the gradient with respect to $\mathbf{A}$ is $\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$, the one with respect to $\mathbf{x}$ is $\mathbf{A}^{\top}\nabla f(\mathbf{y})$.

:::aufgabe Exercise 24 ★ Gradients in matrix notation
<span class="anker" id="aufg-24"></span>

Compute with the formulas of this section, and check each result with the partial derivatives.

<ol class="al">

<li>

$f(\mathbf{x})=\mathbf{b}^{\top}\mathbf{x}+5$ with $\mathbf{b}=(2,\,-1,\,4)^{\top}$;

</li>

<li>

$f(\mathbf{x})=\lVert\mathbf{x}\rVert^2$ at the point $(1,\,-1,\,2)$;

</li>

<li>

$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ with $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\3&4\end{smallmatrix}\bigr)$ at the point $(1,\,-1)$.

</li>

</ol>

:::loesung
(a) By [(7.1)](#gl-7-1), $\nabla f=\mathbf{b}=(2,\,-1,\,4)^{\top}$. Check: $f=2x_1-x_2+4x_3+5$.

(b) By [(7.2)](#gl-7-2) with $\mathbf{A}=\mathbf{I}$, $\nabla f=2\mathbf{x}=(2,\,-2,\,4)^{\top}$. Check: $\partial_jf=2x_j$.

(c) $\mathbf{A}+\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&4\\4&8\end{smallmatrix}\bigr)$, so $\nabla f(1,-1)=(4-4,\ 4-8)^{\top}=(0,\,-4)^{\top}$. Check: $f=2x_1^2+4x_1x_2+4x_2^2$ has the partial derivatives $4x_1+4x_2=0$ and $4x_1+8x_2=-4$.
:::
:::

:::aufgabe Exercise 25 ★★ The least-squares line from Chapter 2
<span class="anker" id="aufg-25"></span>

In [Chapter 2, Section 3.6](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-beste-naherungslosung.html#stufe-3-6), a line was fitted through the points $(0,\,1)$, $(1,\,2)$ and $(2,\,4)$, with $\mathbf{A}=\Bigl(\begin{smallmatrix}1&0\\1&1\\1&2\end{smallmatrix}\Bigr)$ and $\mathbf{y}=(1,\,2,\,4)^{\top}$.

<ol class="al">

<li>

Compute $f(\mathbf{x})=\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2$ and $\nabla f(\mathbf{x})$ at the point $\mathbf{x}=(1,\,1)^{\top}$.

</li>

<li>

In which direction should you shift $\mathbf{x}$ a small step away from $(1,\,1)$ so that $f$ decreases fastest?

</li>

<li>

Show that the gradient at the point $\hat{\mathbf{x}}=(\tfrac56,\,\tfrac32)^{\top}$ from [Chapter 2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html) is zero.

</li>

</ol>

:::loesung
(a) $\mathbf{A}\mathbf{x}=(1,\,2,\,3)^{\top}$, $\mathbf{r}=\mathbf{y}-\mathbf{A}\mathbf{x}=(0,\,0,\,1)^{\top}$ and $f=1$. With $\mathbf{A}^{\top}\mathbf{r}=(0+0+1,\ 0+0+2)^{\top}=(1,\,2)^{\top}$, we get $\nabla f=-2\mathbf{A}^{\top}\mathbf{r}=(-2,\,-4)^{\top}$.

(b) $f$ decreases fastest in the direction $-\nabla f/\lVert\nabla f\rVert=(2,\,4)^{\top}/\sqrt{20}=(1,\,2)^{\top}/\sqrt5\approx(0.447,\ 0.894)^{\top}$: the intercept should grow a little, the slope twice as much. This fits the fact that the line $1+t$ misses the third point $(2,\,4)$ by $1$.

(c) $\mathbf{A}\hat{\mathbf{x}}=(\tfrac56,\ \tfrac73,\ \tfrac{23}6)^{\top}$, so $\hat{\mathbf{r}}=(\tfrac16,\ -\tfrac13,\ \tfrac16)^{\top}$ and

$$\mathbf{A}^{\top}\hat{\mathbf{r}}=\begin{pmatrix}\tfrac16-\tfrac13+\tfrac16\\0-\tfrac13+\tfrac26\end{pmatrix}=\begin{pmatrix}0\\0\end{pmatrix}.$$

The gradient is zero: at the best approximate solution, no small displacement changes the sum of squares to first order.
:::
:::

:::aufgabe Exercise 26 ★★ Derivatives with respect to a matrix
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

Show that $\nabla_{\mathbf{A}}\operatorname{tr}\mathbf{A}=\mathbf{I}$ for square $\mathbf{A}$.

</li>

<li>

Use [(7.6)](#gl-7-6) and $\nabla\lVert\mathbf{y}\rVert^2=2\mathbf{y}$ to show that $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$, and compute this for $\mathbf{A}=\mathbf{I}\in\mathbb{R}^{2\times2}$ and $\mathbf{x}=(1,\,2)^{\top}$.

</li>

<li>

Check (b) with the linear approximation [(7.4)](#gl-7-4): by about how much does $\lVert\mathbf{A}\mathbf{x}\rVert^2$ change if you increase $a_{12}$ from $0$ to $0.01$? Verify by calculation.

</li>

</ol>

:::loesung
(a) $\operatorname{tr}\mathbf{A}=\sum_ia_{ii}$. The derivative with respect to $a_{ij}$ is $1$ for $i=j$ and $0$ otherwise; arranged in the shape of $\mathbf{A}$, this is $\mathbf{I}$.

(b) We have $\lVert\mathbf{A}\mathbf{x}\rVert^2=f(\mathbf{y})$ with $\mathbf{y}=\mathbf{A}\mathbf{x}$ and $\nabla f(\mathbf{y})=2\mathbf{y}$. By [(7.6)](#gl-7-6), $\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\mathbf{y}\,\mathbf{x}^{\top}=2\,(\mathbf{A}\mathbf{x})\,\mathbf{x}^{\top}$. For $\mathbf{A}=\mathbf{I}$ and $\mathbf{x}=(1,\,2)^{\top}$:

$$\nabla_{\mathbf{A}}\lVert\mathbf{A}\mathbf{x}\rVert^2=2\begin{pmatrix}1\\2\end{pmatrix}\begin{pmatrix}1&2\end{pmatrix}=\begin{pmatrix}2&4\\4&8\end{pmatrix}.$$

(c) The entry $(1,2)$ of the gradient is $4$, so [(7.4)](#gl-7-4) predicts a change of about $4\cdot0.01=0.04$. Exactly: with $a_{12}=0.01$, we have $\mathbf{A}\mathbf{x}=(1.02,\ 2)^{\top}$ and $\lVert\mathbf{A}\mathbf{x}\rVert^2=1.0404+4=5.0404$, that is, a change of $0.0404$ compared with $5$.
:::
:::

:::aufgabe Exercise 27 ★★★ The backward rule for a product of two matrices
<span class="anker" id="aufg-27"></span>

Let $\mathbf{C}=\mathbf{A}\mathbf{B}$ and $F(\mathbf{A},\mathbf{B})=f(\mathbf{C})$ with $\mathbf G=\nabla_{\mathbf{C}}f$.

<ol class="al">

<li>

Show componentwise that $\nabla_{\mathbf{A}}F=\mathbf G\mathbf{B}^{\top}$ and $\nabla_{\mathbf{B}}F=\mathbf{A}^{\top}\mathbf G$.

</li>

<li>

Check both formulas for $\mathbf{A}=(1\ \ 2)$, $\mathbf{B}=\bigl(\begin{smallmatrix}3\\4\end{smallmatrix}\bigr)$ and $f(\mathbf{C})=c_{11}^2$ by writing out $F$.

</li>

</ol>

:::loesung
(a) We have $c_{ik}=\sum_ja_{ij}b_{jk}$. The entry $a_{ij}$ acts on all $c_{ik}$ of row $i$, with the factor $b_{jk}$; summed over these paths, $\partial F/\partial a_{ij}=\sum_kg_{ik}b_{jk}=(\mathbf G\mathbf{B}^{\top})_{ij}$. The entry $b_{jk}$ acts on all $c_{ik}$ of column $k$, with the factor $a_{ij}$; so $\partial F/\partial b_{jk}=\sum_ia_{ij}g_{ik}=(\mathbf{A}^{\top}\mathbf G)_{jk}$.

(b) $\mathbf{C}=1\cdot3+2\cdot4=11$, $F=121$ and $\mathbf G=2c_{11}=22$. The formulas give $\nabla_{\mathbf{A}}F=22\,(3\ \ 4)=(66\ \ 88)$ and $\nabla_{\mathbf{B}}F=(1,\,2)^{\top}\cdot22=(22,\,44)^{\top}$. Written out, $F=(3a_{11}+4a_{12})^2$, with the derivatives $2\cdot11\cdot3=66$ and $2\cdot11\cdot4=88$, and $F=(b_{11}+2b_{21})^2$, with the derivatives $22$ and $44$.
:::
:::
