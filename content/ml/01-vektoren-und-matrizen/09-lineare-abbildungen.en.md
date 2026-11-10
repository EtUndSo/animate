---
title: Linear maps
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Chapter 1: Vectors and Matrices
nachschlagen: ja
order: 15210900
summary: A matrix is not only a table but also a rule of calculation that turns one vector into another.
tags: map, linear, rotation, stretch, shear, affine, intercept
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
A matrix is not only a table but also a rule of calculation that turns one vector into another. This section shows which rules can be written in this way, namely exactly the linear ones, and what a matrix does to space geometrically.
:::

### Linear maps

<span class="anker" id="stufe-8-1"></span>

Many calculations turn one list of numbers into another list. From the features of an apartment, the purchase price and the rent are estimated; from the readings of a water meter, the consumption in each month is computed. Such a rule is called a __map__ $f\colon\mathbb{R}^n\to\mathbb{R}^m$: it assigns to each vector $\mathbf{x}\in\mathbb{R}^n$ a vector $f(\mathbf{x})\in\mathbb{R}^m$.

The matrix–vector product has two special properties (Subsection [7.1](das-matrix-vektor-produkt.html#stufe-7-1)): $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ and $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$. It makes no difference whether you add first or map first, and likewise whether you take a multiple first or map first. In the plane you can see these properties on a grid: such a map turns straight lines into straight lines or single points, leaves the origin in place and turns parallel, evenly spaced grid lines into parallel, evenly spaced lines or points.

:::definition Definition 8.1 (Linear map)
<span class="anker" id="satz-8-1"></span>

A map $f\colon\mathbb{R}^n\to\mathbb{R}^m$ is called __linear__ if for all $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$ and all scalars $c$:

<span class="anker" id="gl-8-1"></span>
$$f(\mathbf{u}+\mathbf{v})=f(\mathbf{u})+f(\mathbf{v})\qquad\text{and}\qquad f(c\,\mathbf{u})=c\,f(\mathbf{u}) . \tag{8.1}$$
:::

Together, the two conditions say: $f$ preserves linear combinations, $f(c_1\mathbf{u}+c_2\mathbf{v})=c_1f(\mathbf{u})+c_2f(\mathbf{v})$. Every linear map sends the zero vector to the zero vector, because $f(\mathbf{0})=f(0\cdot\mathbf{u})=0\cdot f(\mathbf{u})=\mathbf{0}$.

::::beispiel [Worked example]
The map $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$ from $\mathbb{R}^2$ to $\mathbb{R}^2$ is linear. Both components are sums of multiples of the $x_j$, and such sums satisfy the conditions [(8.1)](#gl-8-1); for example, $f(\mathbf{u}+\mathbf{v})=(u_1+v_1+u_2+v_2,\ 2u_1+2v_1)^{\top}=f(\mathbf{u})+f(\mathbf{v})$. The map $g(\mathbf{x})=x_1x_2$ is not linear, because $g(2\mathbf{x})=4x_1x_2\ne2\,g(\mathbf{x})$ as soon as $x_1x_2\ne0$. Nor is $h(\mathbf{x})=\mathbf{x}+\mathbf 1$ linear, because $h(\mathbf{0})=\mathbf 1\ne\mathbf{0}$.
::::

⁠**In short:** A map is linear if it preserves sums and multiples; it then maps linear combinations to linear combinations.

:::hintergrund Linearity at the supermarket checkout
A supermarket checkout calculates linearly. It turns the list of quantities purchased into the amount due, and if you put two purchases on the belt together, this costs the sum of the two amounts; if you buy twice as much of everything, it costs twice as much. These are exactly the conditions [(8.1)](#gl-8-1). A pricing scheme with a volume discount, where twice the quantity costs less than twice the price, would not be linear, nor would one with a fixed base fee: there, an empty purchase already costs something, and that violates $f(\mathbf{0})=\mathbf{0}$. An audio recording (Subsection [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3)) is also often processed linearly: if you first mix two recordings and then make the result quieter, you get the same as if you make each one quieter on its own and then mix them.
:::

### Every linear map is a matrix

<span class="anker" id="stufe-8-2"></span>

Every matrix gives a linear map $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$. Does the converse hold as well? Yes, and the reason is simple: every vector is a linear combination of the unit vectors, and a linear map preserves linear combinations. So if you know where the $n$ unit vectors go, you know where every vector goes.

:::satz Theorem 8.2 (Matrix of a linear map)
<span class="anker" id="satz-8-2"></span>

For every linear map $f\colon\mathbb{R}^n\to\mathbb{R}^m$ there is exactly one matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ with $f(\mathbf{x})=\mathbf{A}\mathbf{x}$ for all $\mathbf{x}\in\mathbb{R}^n$. Its columns are the images of the unit vectors:

<span class="anker" id="gl-8-2"></span>
$$\mathbf{a}_j=f(\mathbf{e}_j),\qquad j=1,\dots,n . \tag{8.2}$$
:::

:::beweis Matrix of a linear map
By [(1.6)](vektoren-daten-als-zahlenlisten.html#gl-1-6), $\mathbf{x}=\sum_jx_j\mathbf{e}_j$. Because $f$ is linear, it follows that

$$f(\mathbf{x})=f\Bigl(\sum_{j=1}^nx_j\mathbf{e}_j\Bigr)=\sum_{j=1}^nx_j\,f(\mathbf{e}_j)=\sum_{j=1}^nx_j\,\mathbf{a}_j=\mathbf{A}\mathbf{x} ,$$

the last step by the column view [(7.3)](das-matrix-vektor-produkt.html#gl-7-3). If there were a second matrix $\mathbf{B}$ with $\mathbf{B}\mathbf{x}=f(\mathbf{x})$ for all $\mathbf{x}$, then, taking $\mathbf{x}=\mathbf{e}_j$, column $j$ of $\mathbf{B}$ would equal $f(\mathbf{e}_j)=\mathbf{a}_j$, for every $j$. Hence $\mathbf{B}=\mathbf{A}$.
:::

::::beispiel [Worked example]
For $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$ we have $f(\mathbf{e}_1)=(1,\,2)^{\top}$ and $f(\mathbf{e}_2)=(1,\,0)^{\top}$. So

$$\mathbf{A}=\begin{pmatrix}1&1\\2&0\end{pmatrix},\qquad\text{and as a check}\qquad \mathbf{A}\begin{pmatrix}3\\-1\end{pmatrix}=\begin{pmatrix}2\\6\end{pmatrix}=f\bigl((3,\,-1)^{\top}\bigr).$$
::::

⁠**In short:** Linear maps and matrices are the same thing; column $j$ of the matrix is the image of the unit vector $\mathbf{e}_j$.

:::hintergrund An aftereffect as a matrix: the columns are shifted responses
In a wood stove, a log gives off its full heat in the hour in which it burns and, through the embers, half of it in the following hour; this is a greatly simplified picture. If you add exactly $x[n]$ logs in hour $n$, the heat in that hour, measured in logs, is $y[n]=x[n]+0.5\,x[n-1]$. Three hours are considered, and nothing was burning before the first. The calculation is linear, so it has a matrix. By [(8.2)](#gl-8-2), its column $j$ is the response to the unit vector $\mathbf{e}_j$, that is, to a single log in hour $j$. This response is $(1,\,0.5)$, shifted by $j-1$ hours:

$$\mathbf{A}=\begin{pmatrix}1&0&0\\0.5&1&0\\0&0.5&1\end{pmatrix}.$$

The third column contains only the $1$, because the period considered ends after three hours. For $\mathbf{x}=(2,\,4,\,6)^{\top}$ the matrix gives $(2,\,5,\,8)^{\top}$, the same as the formula. In this way every such aftereffect with fixed weights, called a convolution in mathematics, is a matrix–vector product, and the theorem above explains why: if you know the response to every single log, you know the response to every sequence of logs.
:::

:::hintergrund Data or map? Two roles of the same table
A matrix can be a collection of data, like the data matrix $\mathbf{X}$, or a map, like the matrix of the wood stove in the previous box. Formally the two are the same, and sometimes the same matrix plays both roles at once: the data matrix is also the map $\mathbf{w}\mapsto\mathbf{X}\mathbf{w}$ that turns weights into predictions. It maps the $\mathbb{R}^d$ of the weights into the $\mathbb{R}^N$ of the lists of predictions. When reading a formula, it is therefore worth asking in which role a matrix is appearing.
:::

### Linear maps of the plane

<span class="anker" id="stufe-8-3"></span>

In the plane you can see what a matrix does. You draw the unit square with the corners $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_1+\mathbf{e}_2$ and $\mathbf{e}_2$, together with its image. Because the map preserves linear combinations, the square becomes the parallelogram with the corners $\mathbf{0}$, $\mathbf{a}_1$, $\mathbf{a}_1+\mathbf{a}_2$ and $\mathbf{a}_2$. Its two edges at the origin are the columns of the matrix (Fig. [32](#abb-32)). The whole grid of the plane is deformed in the same way: every cell becomes a shifted copy of this parallelogram.

:::abbildung ml/k1ebene 32
Four linear maps of the plane. Dashed gray: the unit square; blue: its image. The red arrow is the image $\mathbf{a}_1$ of $\mathbf{e}_1$, the green one the image $\mathbf{a}_2$ of $\mathbf{e}_2$; these are the two columns of the matrix. In the flattening, $\mathbf{a}_2=\mathbf{0}$, and the square becomes the line segment from $\mathbf{0}$ to $\mathbf{e}_1$.
:::

<ul>

<li>

The __rotation__ by $90^\circ$ counterclockwise sends $\mathbf{e}_1$ to $(0,\,1)^{\top}$ and $\mathbf{e}_2$ to $(-1,\,0)^{\top}$; these are its columns.

</li>

<li>

The __stretch__ $\operatorname{diag}(2,\,0.5)$ pulls the plane horizontally to twice its width and compresses it vertically to half its height.

</li>

<li>

The __shear__ $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ leaves $\mathbf{e}_1$ in place and pushes $\mathbf{e}_2$ to the right: every point is shifted to the right by its height.

</li>

<li>

The matrix $\operatorname{diag}(1,\,0)$ keeps the first component and sets the second to zero. It flattens the whole plane onto the $x_1$-axis.

</li>

</ul>

::::beispiel [Worked example] the rotation by an arbitrary angle
If you rotate counterclockwise by the angle $\alpha$, then $\mathbf{e}_1$ lands at the point $(\cos\alpha,\,\sin\alpha)^{\top}$ on the unit circle, and $\mathbf{e}_2$, which lies $90^\circ$ further on, lands at the point $(-\sin\alpha,\,\cos\alpha)^{\top}$. By [(8.2)](#gl-8-2), the rotation matrix is therefore

<span class="anker" id="gl-8-3"></span>
$$\mathbf R_\alpha=\begin{pmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{pmatrix}. \tag{8.3}$$

For $\alpha=90^\circ$ this gives the matrix from Fig. [32](#abb-32). It rotates the point $(1,\,1)^{\top}$ to $(-1,\,1)^{\top}$; the stretch maps the same point to $(2,\ 0.5)^{\top}$, the shear to $(2,\,1)^{\top}$ and the flattening to $(1,\,0)^{\top}$.
::::

⁠**In short:** A $2\times2$ matrix deforms the grid of the plane; the unit square becomes the parallelogram spanned by its two columns.

### Linear functions with one output

<span class="anker" id="stufe-8-4"></span>

A model that turns the features of an example into a single number is a map from $\mathbb{R}^d$ to $\mathbb{R}$. If it is linear, then by the theorem in Subsection [8.2](#stufe-8-2) its matrix is a single row with $d$ entries.

:::satz Theorem 8.3 (Linear functions are weighted sums)
<span class="anker" id="satz-8-3"></span>

Every linear map $f\colon\mathbb{R}^d\to\mathbb{R}$ has the form $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}$ with the weights $w_j=f(\mathbf{e}_j)$.
:::

This is the theorem from Subsection [8.2](#stufe-8-2) for $m=1$: the $1\times d$ matrix is the row $\mathbf{w}^{\top}$, and its product with $\mathbf{x}$ is the dot product. So the weighted sum from Subsection [2.2](das-skalarprodukt.html#stufe-2-2) is not just one rule among many but the most general linear rule with one output.

::::beispiel [Worked example]
The real estate agent's rule is $f(\mathbf{x})=3x_1+10x_2-4x_3$. We have $f(\mathbf{e}_1)=3$, $f(\mathbf{e}_2)=10$, $f(\mathbf{e}_3)=-4$, so $\mathbf{w}=(3,\,10,\,-4)^{\top}$. The weight $w_j=f(\mathbf{e}_j)$ is the value of the rule for an imaginary example that has one unit of feature $j$ and nothing else: it says how much one unit of this feature contributes.
::::

⁠**In short:** Every linear map with one output is a weighted sum $\mathbf{w}^{\top}\mathbf{x}$, and the weight $w_j$ is its value at $\mathbf{e}_j$.

### Affine maps

<span class="anker" id="stufe-8-5"></span>

The real estate agent notices that her estimates are consistently too low. So she adds a base amount of $20$ thousand euros to every weighted sum. This new rule is no longer linear: to an imaginary apartment $\mathbf{x}=\mathbf{0}$ it assigns $20$, not $0$. It is a linear map followed by a shift.

:::definition Definition 8.4 (Affine map)
<span class="anker" id="satz-8-4"></span>

A map $f\colon\mathbb{R}^n\to\mathbb{R}^m$ of the form

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b} \tag{8.4}$$

with a matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ and a fixed vector $\mathbf{b}\in\mathbb{R}^m$ is called __affine__. For one output ($m=1$) you write $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}+b$ and call the number $b$ the __intercept__.
:::

For $\mathbf{b}\ne\mathbf{0}$, an affine map is not linear, because $f(\mathbf{0})=\mathbf{b}\ne\mathbf{0}$. In the picture of the grid, the plane is first deformed and then shifted as a whole by $\mathbf{b}$; the origin lands at $\mathbf{b}$. In everyday language, affine rules are often called “linear” too. In this series, only a map with $\mathbf{b}=\mathbf{0}$ is called linear.

For all examples at once, you write the affine prediction with the all-ones vector $\mathbf 1\in\mathbb{R}^N$:

<span class="anker" id="gl-8-5"></span>
$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+b\,\mathbf 1 . \tag{8.5}$$

The term $b\,\mathbf 1$ adds the same amount $b$ to every prediction.

::::beispiel [Worked example]
With $\mathbf{w}=(3,\,10,\,-4)^{\top}$ and $b=20$, the predictions $(188,\,126,\,286,\,232)^{\top}$ become

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+20\cdot\mathbf 1=(208,\,146,\,306,\,252)^{\top}\ \text{thousand euros}.$$
::::

⁠**In short:** An affine map is a linear map plus a fixed shift, $\mathbf{A}\mathbf{x}+\mathbf{b}$; with one output, the shift is called the intercept.

:::hintergrund The trick with the appended one
An affine function can be written as a linear function if you append to each example a component with the fixed value $1$:

$$\mathbf{w}^{\top}\mathbf{x}+b=\begin{pmatrix}w_1&\cdots&w_d&b\end{pmatrix}\begin{pmatrix}x_1\\\vdots\\x_d\\1\end{pmatrix}.$$

The intercept thus becomes the weight of a feature that always has the value $1$. For the whole dataset, you append a column of ones to the data matrix: $\begin{pmatrix}\mathbf{X}&\mathbf 1\end{pmatrix}\begin{pmatrix}\mathbf{w}\\b\end{pmatrix}=\mathbf{X}\mathbf{w}+b\,\mathbf 1$. For the apartments, the augmented data matrix has the rows $(60,2,3,1)$, $(40,1,1,1)$, $(90,4,6,1)$, $(70,3,2,1)$, and with the vector $(3,\,10,\,-4,\,20)^{\top}$ you get $(208,\,146,\,306,\,252)^{\top}$ again. With this trick, affine rules need no theory of their own: everything that holds for linear maps also holds for them in the space with one more dimension.
:::

:::aufgabe Exercise 18 ★ Linear or not?
<span class="anker" id="aufg-18"></span>

Check which of the maps are linear, and give the matrix of each linear one:

$$\begin{gathered} f_1(\mathbf{x})=(2x_1,\ x_1-x_2)^{\top},\qquad f_2(\mathbf{x})=x_1^2,\qquad f_3(\mathbf{x})=(x_2,\ x_1)^{\top},\\ f_4(x)=2x+3,\qquad f_5(\mathbf{x})=(0,\ 0)^{\top} \end{gathered}$$

for $\mathbf{x}\in\mathbb{R}^2$, and $x\in\mathbb{R}$ in the case of $f_4$.

:::loesung
<ul>

<li>

$f_1$ is linear; both components are sums of multiples of the $x_j$. The columns are $f_1(\mathbf{e}_1)=(2,\,1)^{\top}$ and $f_1(\mathbf{e}_2)=(0,\,-1)^{\top}$, so $\bigl(\begin{smallmatrix}2&0\\1&-1\end{smallmatrix}\bigr)$.

</li>

<li>

$f_2$ is not linear: $f_2(2\mathbf{x})=4x_1^2\ne2f_2(\mathbf{x})$ as soon as $x_1\ne0$.

</li>

<li>

$f_3$ is linear, with the matrix $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$; it swaps the components.

</li>

<li>

$f_4$ is not linear, because $f_4(0)=3\ne0$. It is affine, with the intercept $3$.

</li>

<li>

$f_5$ is linear, with the zero matrix; both conditions hold because $\mathbf{0}+\mathbf{0}=\mathbf{0}$ and $c\,\mathbf{0}=\mathbf{0}$.

</li>

</ul>
:::
:::

:::aufgabe Exercise 19 ★★ Matrices from the images of the unit vectors
<span class="anker" id="aufg-19"></span>

<ol class="al">

<li>

Give the matrix of the rotation by $30^\circ$ and compute the image of $(2,\,0)^{\top}$.

</li>

<li>

The reflection across the angle bisector $x_1=x_2$ swaps the two components. Give its matrix and the image of $(3,\,1)^{\top}$.

</li>

<li>

A linear map satisfies $f\bigl((1,\,1)^{\top}\bigr)=(1,\,4)^{\top}$ and $f\bigl((2,\,-1)^{\top}\bigr)=(5,\,-1)^{\top}$. Determine its matrix. Hint: write down both conditions in terms of the columns $\mathbf{a}_1,\mathbf{a}_2$.

</li>

</ol>

:::loesung
(a) By [(8.3)](#gl-8-3), with $\cos30^\circ=\sqrt3/2\approx0.866$ and $\sin30^\circ=\tfrac12$:

$$\mathbf R_{30^\circ}=\begin{pmatrix}0.866&-0.5\\0.5&0.866\end{pmatrix},\qquad \mathbf R_{30^\circ}\begin{pmatrix}2\\0\end{pmatrix}=\begin{pmatrix}\sqrt3\\1\end{pmatrix}\approx\begin{pmatrix}1.732\\1\end{pmatrix}.$$

The image is twice the first column, an arrow of length $2$ at an angle of $30^\circ$.

(b) $\mathbf{e}_1$ goes to $\mathbf{e}_2$ and $\mathbf{e}_2$ to $\mathbf{e}_1$, so the matrix is $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$, and $(3,\,1)^{\top}$ goes to $(1,\,3)^{\top}$.

(c) By linearity, $f\bigl((1,1)^{\top}\bigr)=\mathbf{a}_1+\mathbf{a}_2=(1,\,4)^{\top}$ and $f\bigl((2,-1)^{\top}\bigr)=2\mathbf{a}_1-\mathbf{a}_2=(5,\,-1)^{\top}$. Adding the two equations gives $3\mathbf{a}_1=(6,\,3)^{\top}$, so $\mathbf{a}_1=(2,\,1)^{\top}$ and $\mathbf{a}_2=(1,4)^{\top}-(2,1)^{\top}=(-1,\,3)^{\top}$. The matrix is $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)$. Check: $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)(2,\,-1)^{\top}=(5,\,-1)^{\top}$.
:::
:::

:::aufgabe Exercise 20 ★★ Consumption from meter readings as a matrix
<span class="anker" id="aufg-20"></span>

A new water meter shows the readings $x[1],\dots,x[4]$ in cubic meters at the end of four months; before the first month it stood at $x[0]=0$. The consumption in month $n$ is the difference $y[n]=x[n]-x[n-1]$, $n=1,\dots,4$.

<ol class="al">

<li>

Why is this calculation linear? Set up its $4\times4$ matrix by computing the responses to the four unit vectors.

</li>

<li>

Compute the consumption for the readings $\mathbf{x}=(1,\,2,\,4,\,7)^{\top}$ with the matrix and with the formula.

</li>

</ol>

:::loesung
(a) Each component $y[n]=x[n]-x[n-1]$ of the result is a fixed sum of multiples of the components of $\mathbf{x}$, so the calculation is linear. The response to the single $1$ at position $1$, $\mathbf{x}=\mathbf{e}_1=(1,0,0,0)^{\top}$, is $(1,\,-1,\,0,\,0)^{\top}$: first the reading rises to $1$, then it falls back to $0$. Likewise, the calculation responds to $\mathbf{e}_2$ with $(0,\,1,\,-1,\,0)^{\top}$, to $\mathbf{e}_3$ with $(0,\,0,\,1,\,-1)^{\top}$ and to $\mathbf{e}_4$ with $(0,\,0,\,0,\,1)^{\top}$; for this last $1$, the four months end before the reading drops back. These responses are the columns:

$$\mathbf{A}=\begin{pmatrix}1&0&0&0\\-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{pmatrix}.$$

(b) With the matrix: $\mathbf{A}\,(1,2,4,7)^{\top}=(1,\ -1+2,\ -2+4,\ -4+7)^{\top}=(1,\,1,\,2,\,3)^{\top}$. With the formula: $y[1]=1-0=1$, $y[2]=2-1=1$, $y[3]=4-2=2$, $y[4]=7-4=3$. So $1$, $1$, $2$ and $3$ cubic meters of water were used in the four months.
:::
:::
