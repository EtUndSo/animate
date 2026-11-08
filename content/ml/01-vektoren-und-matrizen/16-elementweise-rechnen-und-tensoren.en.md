---
title: Elementwise calculations and tensors
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15211600
summary: Not every calculation with vectors and matrices is a matrix product.
tags: Hadamard product, elementwise, tensor, axis, shape
lang: en
---

<span class="anker" id="stufe-15"></span>

:::zweck
Not every calculation with vectors and matrices is a matrix product. This section presents the calculations that work entry by entry, and it extends vectors and matrices to arrays of numbers with more than two indices, as they are needed for images.
:::

### The Hadamard product

<span class="anker" id="stufe-15-1"></span>

A shopkeeper has the list of quantities sold and the list of unit prices. For each item he wants the revenue, that is, quantity times price, but not yet the sum. This is a product entry by entry.

:::definition Definition 15.1 (Hadamard product)
<span class="anker" id="satz-15-1"></span>

For two vectors or two matrices of the same size, the __Hadamard product__ $\mathbf{A}\odot\mathbf{B}$ is the product entry by entry:

<span class="anker" id="gl-15-1"></span>
$$(\mathbf{A}\odot\mathbf{B})_{ij}=a_{ij}\,b_{ij} . \tag{15.1}$$
:::

The Hadamard product is *not* the matrix product. The matrix product forms dot products of rows and columns; the Hadamard product only multiplies entries in the same position. Two connections with things you already know: if you add up the Hadamard product of two vectors, you get their dot product, $\mathbf 1^{\top}(\mathbf{u}\odot\mathbf{v})=\mathbf{u}^{\top}\mathbf{v}$. And the Hadamard product with a fixed vector is multiplication by a diagonal matrix: $\mathbf{v}\odot\mathbf{x}=\operatorname{diag}(\mathbf{v})\,\mathbf{x}$.

⁠**Worked example:** $(1,\,2,\,3)^{\top}\odot(4,\,5,\,6)^{\top}=(4,\,10,\,18)^{\top}$, and $4+10+18=32$ is the dot product. For matrices,

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}\odot\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&2\\3&0\end{pmatrix},\qquad\text{but}\qquad \begin{pmatrix}1&2\\3&4\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}2&1\\4&3\end{pmatrix}.$$

With a vector of zeros and ones you can mask out features: $(1,\,0,\,1)^{\top}\odot\mathbf{x}_1=(60,\,0,\,3)^{\top}$ drops the number of rooms of apartment 1.

⁠**In short:** The Hadamard product $\odot$ multiplies entry by entry; it is not the matrix product.

### Elementwise functions

<span class="anker" id="stufe-15-2"></span>

Often you apply the same function to every entry of a vector: you square all errors, take the absolute value of all of them or round all values.

:::definition Definition 15.2 (Elementwise function)
<span class="anker" id="satz-15-2"></span>

For a function $f\colon\mathbb{R}\to\mathbb{R}$ and a vector $\mathbf{x}\in\mathbb{R}^d$, $f$ applied __elementwise__ is the vector $\bigl(f(x_1),\dots,f(x_d)\bigr)^{\top}$. For matrices, the same is done entry by entry.
:::

Many norms can be written this way: the 1-norm is the sum of the elementwise absolute values, $\lVert\mathbf{x}\rVert_1=\mathbf 1^{\top}|\mathbf{x}|$, and the square of the Euclidean norm is the sum of the elementwise squares. An elementwise function is in general not linear: elementwise squaring turns $2\mathbf{x}$ into the vector with the entries $4x_j^2$, not $2x_j^2$.

⁠**Worked example:** The real estate agent's error vector was $(-12,\,-4,\,-4,\,-8)^{\top}$. The elementwise absolute values give $(12,\,4,\,4,\,8)^{\top}$ with the sum $28$, the 1-norm. For appraiser A from Subsection [3.5](normen-die-groe-eines-vektors.html#stufe-3-5), the elementwise squares give $(100,\,100,\,100,\,100)^{\top}$ with the sum $400=20^2$.

⁠**In short:** An elementwise function acts on each entry separately; in general it is not linear.

### Adding a vector to every row

<span class="anker" id="stufe-15-3"></span>

To center a whole dataset, you subtract the same vector, the mean of the examples, from every row of the data matrix. In the same way, the affine prediction adds the same intercept to every component. Such calculations need a notation.

The mean of the examples is given by a matrix–vector product: $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$, because its component $j$ is $\frac1N\sum_ix_{ij}$, the mean of column $j$. The matrix whose rows all equal $\bar{\mathbf{x}}^{\top}$ is the outer product $\mathbf 1\,\bar{\mathbf{x}}^{\top}$. So the centered data matrix is

<span class="anker" id="gl-15-2"></span>
$$\tilde{\mathbf{X}}=\mathbf{X}-\mathbf 1\,\bar{\mathbf{x}}^{\top} , \tag{15.2}$$

and its row $i$ is the vector $(\mathbf{x}_i-\bar{\mathbf{x}})^{\top}$. Many texts write $\mathbf{X}-\bar{\mathbf{x}}^{\top}$ for short and mean by it: subtract the row vector from every row. Strictly speaking, the difference of an $N\times d$ matrix and a $1\times d$ matrix is not defined; the shorthand always stands for [(15.2)](#gl-15-2).

⁠**Worked example:** For the apartments, $\bar{\mathbf{x}}=\tfrac14\mathbf{X}^{\top}\mathbf 1=(65,\ 2.5,\ 3)^{\top}$ and

$$\tilde{\mathbf{X}}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}-\begin{pmatrix}65&2.5&3\\65&2.5&3\\65&2.5&3\\65&2.5&3\end{pmatrix}=\begin{pmatrix}-5&-0.5&0\\-25&-1.5&-2\\25&1.5&3\\5&0.5&-1\end{pmatrix}.$$

Each column is the centered feature column from Subsection [4.3](abstande-und-einheiten.html#stufe-4-3) and sums to zero.

⁠**In short:** Adding a vector $\mathbf{q}$ to every row of a matrix $\mathbf{A}$ means forming $\mathbf{A}+\mathbf 1\,\mathbf{q}^{\top}$; the common shorthand $\mathbf{A}+\mathbf{q}^{\top}$ means exactly this.

### Tensors

<span class="anker" id="stufe-15-4"></span>

A scalar is a single number, a vector a list with one index, a matrix a table with two indices. A color image needs three: row, column and color channel. A stack of color images needs four. All these arrays of numbers are gathered under one name.

:::definition Definition 15.3 (Tensor, shape)
<span class="anker" id="satz-15-3"></span>

In machine learning, a __tensor__ is an array of numbers whose entries are numbered by $k$ indices. Each index runs along an __axis__. The list of the axis lengths is called the __shape__ of the tensor.
:::

A scalar is a tensor with $0$ axes, a vector in $\mathbb{R}^d$ one with a single axis of length $d$, a matrix in $\mathbb{R}^{m\times n}$ one with the shape $m\times n$. A tensor of shape $n_1\times n_2\times\dots\times n_k$ has $n_1\cdot n_2\cdots n_k$ entries. Figure [42](#abb-42) shows the first few levels.

:::abbildung ml/k1tensor 42
Tensors with $0$ to $4$ axes: a scalar, a vector with $4$ entries, a $4\times4$ matrix (such as a grayscale image), a color image made of three $4\times4$ channels for red, green and blue, and a stack of $N$ such color images (indicated by three images).
:::

⁠**Worked example:** A color image with $4\times4$ pixels and three color channels is a tensor of shape $3\times4\times4$ with $48$ entries. The entry with the indices $(1,2,3)$ is the brightness of the first channel, that is, red, at the pixel in row $2$ and column $3$.

⁠**In short:** A tensor is an array of numbers with any number of axes; scalar, vector and matrix are the cases with $0$, $1$ and $2$ axes.

:::hintergrund The tensor of physics is something different
In physics and electrical engineering, a tensor is more than an array of numbers, for example the stress tensor of a material or the permittivity tensor of a crystal. There, a tensor comes with a rule for how its entries change when you rotate the coordinate system; the entries alone do not make it a tensor. In machine learning this rule is absent: there, a tensor is just a multidimensional array of numbers. The word is the same, the concept is a different one.
:::

### Images as tensors

<span class="anker" id="stufe-15-5"></span>

Image data are the most important case of tensors with more than two axes. Their shape shows at once how many numbers a dataset contains.

A grayscale image with $28\times28$ pixels is a matrix, that is, a tensor of shape $28\times28$ with $784$ entries. A color image with $32\times32$ pixels has three channels and the shape $3\times32\times32$, that is, $3072$ entries. A stack of $100$ such color images has the shape $100\times3\times32\times32$ and $307\,200$ entries. The first axis counts the examples, just like the rows of the data matrix: the data matrix is the special case of a stack of vectors, with the shape $N\times d$.

The order of the axes is a convention. Some programs put the color channel first ($3\times32\times32$), others last ($32\times32\times3$). The numbers are the same, only their arrangement differs, and before any calculation it must be clear which axis means what.

⁠**Worked example:** A dataset of $60\,000$ grayscale images with $28\times28$ pixels is a tensor of shape $60\,000\times28\times28$ with $47\,040\,000$ entries. If you read out each image into a vector in $\mathbb{R}^{784}$, this becomes a data matrix in $\mathbb{R}^{60\,000\times784}$, with the same entries.

⁠**In short:** An image is a tensor with two or three axes, a stack of images one with one more axis; the first axis counts the examples.

:::aufgabe Exercise 36 ★ Elementwise or not?
<span class="anker" id="aufg-36"></span>

<ol class="al">

<li>

Compute $\mathbf{u}\odot\mathbf{v}$ and $\mathbf{u}^{\top}\mathbf{v}$ for $\mathbf{u}=(2,\,-1,\,3)^{\top}$ and $\mathbf{v}=(1,\,4,\,2)^{\top}$.

</li>

<li>

Compute $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\odot\bigl(\begin{smallmatrix}2&0\\1&3\end{smallmatrix}\bigr)$ and the matrix product of the same matrices.

</li>

<li>

What shape does a stack of $64$ color images with $224\times224$ pixels have, with the color channel first, and how many entries does it have?

</li>

</ol>

:::loesung
(a) $\mathbf{u}\odot\mathbf{v}=(2,\,-4,\,6)^{\top}$ and $\mathbf{u}^{\top}\mathbf{v}=2-4+6=4$, the sum of the entries of the Hadamard product.

(b) Hadamard: $\bigl(\begin{smallmatrix}1\cdot2&2\cdot0\\3\cdot1&4\cdot3\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&0\\3&12\end{smallmatrix}\bigr)$. Matrix product: $\bigl(\begin{smallmatrix}2+2&0+6\\6+4&0+12\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4&6\\10&12\end{smallmatrix}\bigr)$. Only the bottom right entry happens to agree.

(c) The shape is $64\times3\times224\times224$, with $64\cdot3\cdot224\cdot224=9\,633\,792$ entries.
:::
:::

:::aufgabe Exercise 37 ★★ Centering a dataset
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

Show: the columns of the centered data matrix [(15.2)](#gl-15-2) sum to zero, that is, $\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf{0}^{\top}$. Use $\mathbf 1^{\top}\mathbf 1=N$.

</li>

<li>

Center the data matrix of the three texts from Subsection [5.4](winkel-und-ahnlichkeit.html#stufe-5-4).

</li>

</ol>

:::loesung
(a) We have $\bar{\mathbf{x}}^{\top}=\frac1N\mathbf 1^{\top}\mathbf{X}$, the transpose of $\bar{\mathbf{x}}=\frac1N\mathbf{X}^{\top}\mathbf 1$. Hence

$$\mathbf 1^{\top}\tilde{\mathbf{X}}=\mathbf 1^{\top}\mathbf{X}-(\mathbf 1^{\top}\mathbf 1)\,\bar{\mathbf{x}}^{\top}=\mathbf 1^{\top}\mathbf{X}-N\cdot\tfrac1N\,\mathbf 1^{\top}\mathbf{X}=\mathbf{0}^{\top} .$$

Each column is a centered vector, and its components add up to zero, as in Subsection [4.3](abstande-und-einheiten.html#stufe-4-3).

(b) The mean of the texts is $\bar{\mathbf{x}}=\tfrac13\bigl((3,2,0)^{\top}+(6,4,0)^{\top}+(0,1,3)^{\top}\bigr)=(3,\,\tfrac73,\,1)^{\top}$. Centered:

$$\tilde{\mathbf{X}}=\begin{pmatrix}0&-\frac13&-1\\3&\frac53&-1\\-3&-\frac43&2\end{pmatrix}.$$

Each column sums to zero: $0+3-3=0$, $-\tfrac13+\tfrac53-\tfrac43=0$, $-1-1+2=0$.
:::
:::
