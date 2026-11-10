---
title: The Jacobian matrix
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15230600
summary: Many calculation steps produce not one number but several: a matrix–vector product turns one vector into another.
tags: vector-valued, Jacobian matrix
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Many calculation steps produce not one number but several: a matrix–vector product turns one vector into another. For such functions, the Jacobian matrix collects the partial derivatives of all outputs with respect to all inputs. It is the matrix of the linear approximation, and for the two most common building blocks, linear maps and elementwise functions, it has a particularly simple form.
:::

### Functions with several outputs

<span class="anker" id="stufe-5-1"></span>

In [Chapter 1, Section 8](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8), a linear map $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ mapped vectors of $\mathbb{R}^n$ to vectors of $\mathbb{R}^m$, and in [Chapter 1, Section 15.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/elementweise-rechnen-und-tensoren.html#stufe-15-2), a function was applied to each component of a vector separately. In both cases, several numbers come out of one vector. Each of them is, on its own, a function of several variables.

:::definition Definition 5.1 (Vector-valued function)
<span class="anker" id="satz-5-1"></span>

A function $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ that assigns to every $\mathbf{x}\in\mathbb{R}^n$ a vector

$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}g_1(\mathbf{x})\\ \vdots\\ g_m(\mathbf{x})\end{pmatrix}\in\mathbb{R}^m$$

is called __vector-valued__. The functions $g_1,\dots,g_m:\mathbb{R}^n\to\mathbb{R}$ are called its components.
:::

This chapter writes vector-valued functions in bold, like vectors; functions whose value is a number are written in non-bold type.

::::beispiel [Worked example]
Throughout Sections [5](#stufe-5) and [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6), we work with the function $\mathbf{g}:\mathbb{R}^2\to\mathbb{R}^2$ with

<span class="anker" id="gl-5-1"></span>
$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}x_1x_2\\ 2x_1+x_2^2\end{pmatrix},\qquad \mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix}. \tag{5.1}$$

Its components are $g_1(\mathbf{x})=x_1x_2$ and $g_2(\mathbf{x})=2x_1+x_2^2$.
::::

⁠**In short:** A vector-valued function $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ consists of $m$ functions of $n$ variables, one for each output.

### The Jacobian matrix

<span class="anker" id="stufe-5-2"></span>

Each component $g_i$ has $n$ partial derivatives, one with respect to each input. Together these are $m\cdot n$ numbers. You arrange them in a table with one row per output and one column per input.

:::definition Definition 5.2 (Jacobian matrix)
<span class="anker" id="satz-5-2"></span>

If all partial derivatives of the components of $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ exist at the point $\mathbf{x}$, then the $m\times n$ matrix

<span class="anker" id="gl-5-2"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}\dfrac{\partial g_1}{\partial x_1}&\cdots&\dfrac{\partial g_1}{\partial x_n}\\ \vdots&&\vdots\\ \dfrac{\partial g_m}{\partial x_1}&\cdots&\dfrac{\partial g_m}{\partial x_n}\end{pmatrix},\qquad \bigl(\mathbf{J}_{\mathbf{g}}(\mathbf{x})\bigr)_{ij}=\frac{\partial g_i}{\partial x_j}(\mathbf{x}), \tag{5.2}$$

is called the __Jacobian matrix__ of $\mathbf{g}$ at the point $\mathbf{x}$.
:::

Row $i$ belongs to the output $g_i$; it is its gradient, written as a row: $\nabla g_i(\mathbf{x})^{\top}$. Column $j$ belongs to the input $x_j$; it says how all outputs respond at once when you change only $x_j$. For a function $f:\mathbb{R}^n\to\mathbb{R}$ with a single output, the Jacobian matrix is a $1\times n$ matrix, namely the gradient as a row: $\mathbf{J}_f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}$. The matrix is named after the mathematician Carl Gustav Jacob Jacobi.

::::beispiel [Worked example]
For $\mathbf{g}$ from [(5.1)](#gl-5-1),

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}x_2&x_1\\2&2x_2\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}.$$

The first column $(2,\,2)^{\top}$ says: if $x_1$ grows by a small $h$, both outputs grow by about $2h$. The second column $(1,\,4)^{\top}$ says: if $x_2$ grows, the second output responds four times as strongly as the first.
::::

⁠**In short:** The Jacobian matrix has one row per output and one column per input; its entry $(i,j)$ is $\partial g_i/\partial x_j$.

### The linear approximation with the Jacobian matrix

<span class="anker" id="stufe-5-3"></span>

Each component has its linear approximation [(3.4)](partielle-ableitungen-und-der-gradient.html#gl-3-4). If you write all $m$ approximations one below the other, the components of $\mathbf{g}(\mathbf{x}+\mathbf{h})$ stand on the left and the rows of the Jacobian matrix times $\mathbf{h}$ on the right. By the row view from [Chapter 1, Section 7.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-2), this is a matrix–vector product.

:::satz Theorem 5.3 (Linear approximation of a vector-valued function)
<span class="anker" id="satz-5-3"></span>

If every component of $\mathbf{g}$ is differentiable at the point $\mathbf{x}$, then

<span class="anker" id="gl-5-3"></span>
$$\mathbf{g}(\mathbf{x}+\mathbf{h})=\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}+\mathbf{r}(\mathbf{h})\qquad\text{with}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{\lVert\mathbf{r}(\mathbf{h})\rVert}{\lVert\mathbf{h}\rVert}=0 . \tag{5.3}$$
:::

:::beweis Linear approximation of a vector-valued function
Component $i$ of $\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$ is $\nabla g_i(\mathbf{x})^{\top}\mathbf{h}$. By the definition of differentiability [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5), for every $i$ the quotient $r_i(\mathbf{h})/\lVert\mathbf{h}\rVert$ tends to $0$. Because $\lVert\mathbf{r}\rVert\le|r_1|+\dots+|r_m|$, $\lVert\mathbf{r}(\mathbf{h})\rVert/\lVert\mathbf{h}\rVert$ also tends to $0$.
:::

Near $\mathbf{x}$, $\mathbf{g}$ therefore acts like the linear map $\mathbf{h}\mapsto\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$, and by [Chapter 1, Section 8.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2), every linear map has exactly one matrix. The Jacobian matrix is this matrix. Under the magnifying glass, $\mathbf{g}$ deforms a small grid around $\mathbf{x}$ the way the matrix $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ deforms the unit grid: it is rotated, stretched or sheared, but straight lines remain almost straight.

::::beispiel [Worked example]
For $\mathbf{g}$ from [(5.1)](#gl-5-1) at the point $(1,\,2)$ and $\mathbf{h}=(0.1,\ -0.1)^{\top}$,

$$\mathbf{J}_{\mathbf{g}}(1,2)\,\mathbf{h}=\begin{pmatrix}2\cdot0.1+1\cdot(-0.1)\\2\cdot0.1+4\cdot(-0.1)\end{pmatrix}=\begin{pmatrix}0.1\\-0.2\end{pmatrix}, \qquad \mathbf{g}(1.1,\ 1.9)\approx\begin{pmatrix}2.1\\5.8\end{pmatrix}.$$

The exact value is $\mathbf{g}(1.1,\ 1.9)=(2.09,\ 5.81)^{\top}$. Fig. [10](#abb-10) shows the product row by row.

:::abbildung ml/k3rjacobi 10
The change in the linear approximation of $\mathbf{g}$ at the point $\mathbf{x}=(1,\,2)^{\top}$ as a matrix–vector product: each row is the dot product of the gradient of one output and the displacement.
:::
::::

⁠**In short:** Near $\mathbf{x}$, $\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$; the Jacobian matrix is the matrix of the linear map that $\mathbf{g}$ acts like on a small scale.

### Two important Jacobian matrices

<span class="anker" id="stufe-5-4"></span>

Two building blocks occur all the time in calculations with data: the matrix–vector product and functions applied to each component separately. You need their Jacobian matrices again and again, and both can be stated without calculation.

:::satz Theorem 5.4 (Jacobian matrices of the building blocks)
<span class="anker" id="satz-5-4"></span>

<ol class="al">

<li>

For $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$ with $\mathbf{A}\in\mathbb{R}^{m\times n}$ and $\mathbf{b}\in\mathbb{R}^m$, $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\mathbf{A}$ at every point.

</li>

<li>

If $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^n$ applies a differentiable function $\varphi$ of one variable to each component, $g_i(\mathbf{x})=\varphi(x_i)$, then

<span class="anker" id="gl-5-4"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\operatorname{diag}\bigl(\varphi'(x_1),\,\dots,\,\varphi'(x_n)\bigr). \tag{5.4}$$

</li>

</ol>
:::

:::beweis Jacobian matrices of the building blocks
(a) Component $i$ is $g_i(\mathbf{x})=\sum_ka_{ik}x_k+b_i$. Differentiating with respect to $x_j$, only the term with $k=j$ remains, so $\partial g_i/\partial x_j=a_{ij}$. (b) The component $g_i=\varphi(x_i)$ depends only on $x_i$. Its derivative with respect to $x_j$ is therefore $0$ for $j\ne i$ and $\varphi'(x_i)$ for $j=i$.
:::

Both results have a simple reason. An affine map is already linear except for the shift $\mathbf{b}$; its best linear approximation is itself without $\mathbf{b}$. In an elementwise function, each input acts only on its own output; all entries off the diagonal are zero because there are no connections between different components.

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\bigr)$, the Jacobian matrix of $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ is $\mathbf{A}$ itself everywhere. If you square each component, $\varphi(t)=t^2$, the Jacobian matrix at the point $\mathbf{x}=(1,\,-2,\,3)^{\top}$ is $\operatorname{diag}(2,\,-4,\,6)$. If you apply the logistic function to each component of $\mathbf{x}=(0,\,2)^{\top}$, then by [(2.4)](die-kettenregel.html#gl-2-4) it is $\operatorname{diag}\bigl(\sigma'(0),\,\sigma'(2)\bigr)\approx\operatorname{diag}(0.25,\ 0.105)$.
::::

⁠**In short:** The Jacobian matrix of $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}+\mathbf{b}$ is $\mathbf{A}$; that of an elementwise function is the diagonal matrix of the individual derivatives.

:::hintergrund The determinant of the Jacobian matrix as an area factor
By [Chapter 1, Section 14.3](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-3), a linear map multiplies the area of every figure by the same factor $|\det\mathbf{A}|$. Because $\mathbf{g}$ acts like $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ on a small scale, this also holds approximately for $\mathbf{g}$: a small square around $\mathbf{x}$ with area $F$ turns into a figure that is almost a parallelogram with area $|\det\mathbf{J}_{\mathbf{g}}(\mathbf{x})|\cdot F$. For $\mathbf{g}$ from [(5.1)](#gl-5-1), $\det\mathbf{J}_{\mathbf{g}}(1,2)=2\cdot4-1\cdot2=6$: near $(1,\,2)$, $\mathbf{g}$ enlarges areas by a factor of about six. Polar coordinates are a well-known example, $\mathbf{g}(r,\varphi)=(r\cos\varphi,\ r\sin\varphi)^{\top}$. Their Jacobian matrix has the columns $(\cos\varphi,\,\sin\varphi)^{\top}$ and $(-r\sin\varphi,\,r\cos\varphi)^{\top}$ and the determinant $r\cos^2\varphi+r\sin^2\varphi=r$. A small rectangle with sides $\Delta r$ and $\Delta\varphi$ becomes a piece of an annulus with area about $r\,\Delta r\,\Delta\varphi$, because the arc for the angle $\Delta\varphi$ at distance $r$ has length $r\,\Delta\varphi$.
:::

:::aufgabe Exercise 17 ★ Computing Jacobian matrices
<span class="anker" id="aufg-17"></span>

Compute the Jacobian matrix at the given point.

<ol class="al">

<li>

$\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1-x_2,\ x_1x_2)^{\top}$ at the point $(3,\,1)$;

</li>

<li>

$\mathbf{g}(\mathbf{x})=(\mathrm{e}^{x_1},\,\mathrm{e}^{x_2},\,\mathrm{e}^{x_3})^{\top}$ at the point $(0,\,1,\,-1)$;

</li>

<li>

$f(\mathbf{x})=x_1^2x_2+x_2^2$ from [(3.1)](partielle-ableitungen-und-der-gradient.html#gl-3-1) at the point $(1,\,2)$. What shape does the matrix have, and what is it?

</li>

</ol>

:::loesung
(a) The Jacobian matrix has three rows and two columns:

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}1&1\\1&-1\\x_2&x_1\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(3,1)=\begin{pmatrix}1&1\\1&-1\\1&3\end{pmatrix}.$$

(b) The function is elementwise; by [(5.4)](#gl-5-4), $\mathbf{J}=\operatorname{diag}(\mathrm{e}^0,\,\mathrm{e}^1,\,\mathrm{e}^{-1})\approx\operatorname{diag}(1,\ 2.718,\ 0.368)$.

(c) A function with one output has a $1\times2$ Jacobian matrix, the gradient as a row: $\mathbf{J}_f(1,2)=(4\ \ 5)=\nabla f(1,2)^{\top}$.
:::
:::

:::aufgabe Exercise 18 ★★ Linear approximation of a map of the plane
<span class="anker" id="aufg-18"></span>

Let $\mathbf{g}(\mathbf{x})=(x_1^2-x_2,\ x_1x_2)^{\top}$.

<ol class="al">

<li>

Compute $\mathbf{J}_{\mathbf{g}}(2,1)$ and use it to find an approximate value for $\mathbf{g}(2.05,\ 0.9)$. Compare with the exact value.

</li>

<li>

How must you shift the inputs so that the first output changes but the second, in linear approximation, does not change at all? Give such a displacement $\mathbf{h}$.

</li>

</ol>

:::loesung
(a) $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}2x_1&-1\\x_2&x_1\end{smallmatrix}\bigr)$, so $\mathbf{J}_{\mathbf{g}}(2,1)=\bigl(\begin{smallmatrix}4&-1\\1&2\end{smallmatrix}\bigr)$, and $\mathbf{g}(2,1)=(3,\,2)^{\top}$. With $\mathbf{h}=(0.05,\ -0.1)^{\top}$,

$$\mathbf{J}_{\mathbf{g}}\mathbf{h}=\begin{pmatrix}0.2+0.1\\0.05-0.2\end{pmatrix}=\begin{pmatrix}0.3\\-0.15\end{pmatrix},\qquad \mathbf{g}(2.05,\ 0.9)\approx\begin{pmatrix}3.3\\1.85\end{pmatrix}.$$

The exact value is $\mathbf{g}(2.05,\ 0.9)=(4.2025-0.9,\ 1.845)^{\top}=(3.3025,\ 1.845)^{\top}$.

(b) In linear approximation, the second output changes by $h_1+2h_2$; this is zero for $\mathbf{h}$ in the direction $(2,\,-1)^{\top}$. For a step by exactly this vector, the first output then changes by $4\cdot2-1\cdot(-1)=9$. So both inputs must change: $x_1$ grows and $x_2$ falls half as much, for example $\mathbf{h}=(0.02,\ -0.01)^{\top}$ with the effect $(0.09,\ 0)^{\top}$.
:::
:::

:::aufgabe Exercise 19 ★★★ How much $\mathbf{g}$ enlarges areas
<span class="anker" id="aufg-19"></span>

Let $\mathbf{g}$ be as in [(5.1)](#gl-5-1).

<ol class="al">

<li>

Compute the images of the four corners of the square with the corners $(1,\,2)$, $(1.1,\ 2)$, $(1.1,\ 2.1)$ and $(1,\ 2.1)$.

</li>

<li>

The images almost form a parallelogram. Estimate its area using the images of the two edges that start at $\mathbf{g}(1,2)$, and compare with $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0.01$.

</li>

</ol>

:::loesung
(a) With $\mathbf{g}(\mathbf{x})=(x_1x_2,\ 2x_1+x_2^2)^{\top}$:

$$\mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix},\quad \mathbf{g}(1.1,\,2)=\begin{pmatrix}2.2\\6.2\end{pmatrix},\quad \mathbf{g}(1.1,\,2.1)=\begin{pmatrix}2.31\\6.61\end{pmatrix},\quad \mathbf{g}(1,\,2.1)=\begin{pmatrix}2.1\\6.41\end{pmatrix}.$$

(b) The images of the two edges that start at $\mathbf{g}(1,2)$ are $(0.2,\ 0.2)^{\top}$ and $(0.1,\ 0.41)^{\top}$. By [Chapter 1, Section 14.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-1), the parallelogram they span has the area $|0.2\cdot0.41-0.1\cdot0.2|=0.062$. The Jacobian matrix predicts $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0.01=6\cdot0.01=0.06$. The discrepancy arises because the square is not arbitrarily small; the fourth corner, at $(2.31,\ 6.61)$, also lies only almost where a true parallelogram would have it, at $(2.3,\ 6.61)$.
:::
:::
