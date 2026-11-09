---
title: Matrices and the data matrix
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15210700
summary: A dataset consists of many vectors with the same number of components.
tags: matrix, entry, size, square, diagonal, diagonal matrix, zero matrix, data matrix
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
A dataset consists of many vectors with the same number of components. This section combines them into a single table of numbers, a matrix, and establishes how to write and calculate with matrices.
:::

### Matrices

<span class="anker" id="stufe-6-1"></span>

The table of apartments is more than four separate vectors: it is one object that you want to calculate with as a whole. A grayscale image is also a table, namely of brightness values, arranged in rows and columns. Such a rectangular array of numbers is called a matrix.

:::definition Definition 6.1 (Matrix)
<span class="anker" id="satz-6-1"></span>

A __matrix__ $\mathbf{A}\in\mathbb{R}^{m\times n}$ is a rectangular arrangement of $m\cdot n$ real numbers in $m$ rows and $n$ columns:

$$\mathbf{A}=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix}.$$

The number $a_{ij}$ in row $i$ and column $j$ is called an __entry__ of the matrix. The pair $m\times n$ is called the __size__ of the matrix.
:::

Matrices are written in bold capital letters, their entries with the corresponding lowercase letter and two indices: first the row, then the column. The $j$th column of $\mathbf{A}$ is a vector with $m$ components; it is called $\mathbf{a}_j$. The matrix is then also written as a row of its columns, $\mathbf{A}=\begin{pmatrix}\mathbf{a}_1&\cdots&\mathbf{a}_n\end{pmatrix}$. A vector with $d$ components is a matrix of size $d\times1$, and a row with $d$ numbers is a matrix of size $1\times d$.

Two matrices are equal if they have the same size and the same entry in every position. Matrices of the same size are added and multiplied by a number entry by entry, just like vectors: $(\mathbf{A}+\mathbf{B})_{ij}=a_{ij}+b_{ij}$ and $(c\,\mathbf{A})_{ij}=c\,a_{ij}$.

::::beispiel [Worked example]
The matrix

$$\mathbf{A}=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}\in\mathbb{R}^{2\times3}$$

has size $2\times3$, the entries $a_{12}=2$ and $a_{21}=4$, and the second column $\mathbf{a}_2=(2,\,5)^{\top}$. A grayscale image of $3\times3$ pixels that shows a bright cross on a dark background is the matrix with the rows $(0,1,0)$, $(1,1,1)$ and $(0,1,0)$. Furthermore,

$$\begin{pmatrix}1&2\\3&4\end{pmatrix}+\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}1&3\\4&4\end{pmatrix},\qquad 2\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}2&4\\6&8\end{pmatrix}.$$
::::

⁠**In short:** A matrix is a rectangular table of numbers with $m$ rows and $n$ columns; the entry $a_{ij}$ is in row $i$ and column $j$.

:::hintergrund An image as a matrix and as a vector
If you read out an image row by row and string the rows together, the matrix becomes a long vector: the $3\times3$ cross becomes the vector $(0,1,0,1,1,1,0,1,0)^{\top}\in\mathbb{R}^9$, and a $28\times28$ image becomes a vector in $\mathbb{R}^{784}$. The numbers stay the same, but one piece of information is lost in this notation: which pixels are neighbors. The pixel directly below another one is $28$ positions further back in the long vector. For calculations that weight each feature individually, this does not matter. For calculations that want to exploit neighborhoods, the matrix form is the more natural one.
:::

### Square matrices and diagonal matrices

<span class="anker" id="stufe-6-2"></span>

Some matrices occur so often that they have their own names. In all three cases the shape of the table is particularly simple.

A matrix with the same number of rows and columns is called __square__. The entries $a_{11},a_{22},\dots,a_{nn}$ of a square matrix form its __diagonal__, which runs from the top left to the bottom right.

:::definition Definition 6.2 (Diagonal matrix, zero matrix)
<span class="anker" id="satz-6-2"></span>

A square matrix whose entries off the diagonal are all zero is called a __diagonal matrix__. For a vector $\mathbf{v}\in\mathbb{R}^n$, $\operatorname{diag}(\mathbf{v})$ is the diagonal matrix with the diagonal entries $v_1,\dots,v_n$.

The matrix whose entries are all zero is called the __zero matrix__ and is written $\mathbf 0$.
:::

::::beispiel [Worked example]
$$\operatorname{diag}\bigl((2,\ 0.5)^{\top}\bigr)=\begin{pmatrix}2&0\\0&0.5\end{pmatrix},\qquad \operatorname{diag}\bigl((1,\,0,\,3)^{\top}\bigr)=\begin{pmatrix}1&0&0\\0&0&0\\0&0&3\end{pmatrix}.$$

The second matrix has a diagonal entry zero and is still a diagonal matrix; the only requirement is that all entries off the diagonal are zero. Instead of $\operatorname{diag}\bigl((2,\ 0.5)^{\top}\bigr)$ you write $\operatorname{diag}(2,\,0.5)$ for short.
::::

⁠**In short:** A square matrix has as many rows as columns; a diagonal matrix has nonzero entries only on the diagonal.

### The data matrix

<span class="anker" id="stufe-6-3"></span>

The apartment table from Subsection [1.2](vektoren-daten-als-zahlenlisten.html#stufe-1-2) is a matrix: four rows, one per apartment, and three columns, one per feature. This arrangement, one example per row, is the standard form of a dataset (Fig. [27](#abb-27)).

:::abbildung ml/k1datenmatrix 27
The data matrix $\mathbf{X}$ of the apartment dataset. Each row is an example, the vector $\mathbf{x}_i^{\top}$ written as a row (blue: apartment 2). Each column is the feature column of one feature across all examples (orange: the floor areas). The entry $x_{21}=40$ belongs to both.
:::

:::definition Definition 6.3 (Data matrix)
<span class="anker" id="satz-6-3"></span>

For a dataset with the examples $\mathbf{x}_1,\dots,\mathbf{x}_N\in\mathbb{R}^d$, the __data matrix__ is the matrix $\mathbf{X}\in\mathbb{R}^{N\times d}$ whose row $i$ is the example $\mathbf{x}_i$, written as a row:

<span class="anker" id="gl-6-1"></span>
$$\mathbf{X}=\begin{pmatrix}\mathbf{x}_1^{\top}\\\mathbf{x}_2^{\top}\\\vdots\\\mathbf{x}_N^{\top}\end{pmatrix}=\begin{pmatrix}x_{11}&\cdots&x_{1d}\\\vdots&&\vdots\\x_{N1}&\cdots&x_{Nd}\end{pmatrix}. \tag{6.1}$$
:::

The entry $x_{ij}$ is the value of feature $j$ for example $i$, exactly as agreed in Subsection [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3). Column $j$ of $\mathbf{X}$ is the feature column of feature $j$ from Subsection [4.3](abstande-und-einheiten.html#stufe-4-3): all values of this feature across all examples. So the rows belong to the examples and the columns to the features. Component $j$ of the mean of the examples $\bar{\mathbf{x}}$ is the mean of column $j$.

::::beispiel [Worked example]
For the apartment dataset,

$$\mathbf{X}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\in\mathbb{R}^{4\times3}.$$

The entry $x_{32}=4$ is the number of rooms of apartment 3, the first column $(60,\,40,\,90,\,70)^{\top}$ contains all floor areas, and its mean $65$ is the first component of $\bar{\mathbf{x}}=(65,\ 2.5,\ 3)^{\top}$.
::::

⁠**In short:** The data matrix $\mathbf{X}\in\mathbb{R}^{N\times d}$ contains one example per row and one feature per column.

:::hintergrund Examples as rows or as columns?
This series writes the examples as rows, as in a spreadsheet and in most current textbooks and software libraries. Some texts do it the other way around and place the examples side by side as columns; their data matrix then has size $d\times N$. The letters vary as well: often the number of examples is called $m$ and the number of features $n$, and example number $i$ is written $\mathbf{x}^{(i)}$, with the index at the top in parentheses. The content does not change. So when you read someone else's text, first check what is a row and what is a column there.
:::

:::aufgabe Exercise 15 ★ Reading and setting up matrices
<span class="anker" id="aufg-15"></span>

<ol class="al">

<li>

What is the size of $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$? Give $b_{13}$, $b_{21}$ and the third column of $\mathbf{B}$.

</li>

<li>

Set up the data matrix of the three texts from Subsection [5.4](winkel-und-ahnlichkeit.html#stufe-5-4). What do $N$, $d$ and the entry $x_{23}$ mean?

</li>

<li>

A grayscale image of $4\times4$ pixels shows a bright “L”: the first column and the bottom row are bright ($1$), everything else is dark ($0$). Write down the matrix and read it out row by row into a vector. How many components does it have?

</li>

</ol>

:::loesung
(a) $\mathbf{B}$ has size $2\times3$. We have $b_{13}=2$ (row 1, column 3) and $b_{21}=2$ (row 2, column 1); the third column is $(2,\,0)^{\top}$.

(b) $\mathbf{X}=\Bigl(\begin{smallmatrix}3&2&0\\6&4&0\\0&1&3\end{smallmatrix}\Bigr)$ with $N=3$ texts and $d=3$ words. The entry $x_{23}=0$ says: the third word, “election”, does not occur in the second text.

(c) The matrix has the rows $(1,0,0,0)$, $(1,0,0,0)$, $(1,0,0,0)$ and $(1,1,1,1)$. Read out row by row, it gives the vector

$$(1,0,0,0,\ 1,0,0,0,\ 1,0,0,0,\ 1,1,1,1)^{\top}\in\mathbb{R}^{16}$$

with $4\cdot4=16$ components.
:::
:::
