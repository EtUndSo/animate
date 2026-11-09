---
title: The matrix–vector product
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15210800
summary: The same weighted sum is to be computed for all examples of a dataset.
tags: matrix–vector product, column space
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
The same weighted sum is to be computed for all examples of a dataset. For this purpose, this section introduces the product of a matrix and a vector and shows the two ways to read it: row by row or column by column.
:::

### Matrix times vector

<span class="anker" id="stufe-7-1"></span>

The real estate agent from Subsection [2.2](das-skalarprodukt.html#stufe-2-2) estimates each apartment with the same weighted sum. For four apartments she computes $\mathbf{w}^{\top}\mathbf{x}_i$ four times. If you write the apartments as rows of a matrix, you can express all four calculations in one step: each row of the matrix is multiplied by the same vector.

:::definition Definition 7.1 (Matrix–vector product)
<span class="anker" id="satz-7-1"></span>

For $\mathbf{A}\in\mathbb{R}^{m\times n}$ and $\mathbf{x}\in\mathbb{R}^n$, the __matrix–vector product__ $\mathbf{A}\mathbf{x}$ is the vector in $\mathbb{R}^m$ with the components

<span class="anker" id="gl-7-1"></span>
$$(\mathbf{A}\mathbf{x})_i=\sum_{j=1}^{n}a_{ij}\,x_j=a_{i1}x_1+a_{i2}x_2+\dots+a_{in}x_n ,\qquad i=1,\dots,m . \tag{7.1}$$
:::

The product exists only if $\mathbf{x}$ has as many components as $\mathbf{A}$ has columns. The result has as many components as $\mathbf{A}$ has rows. From the rules for sums it follows that $\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ and $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$.

::::beispiel [Worked example]
For

$$\mathbf{A}=\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\quad\text{and}\quad \mathbf{x}=\begin{pmatrix}2\\1\end{pmatrix}\qquad\text{we have}\qquad \mathbf{A}\mathbf{x}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$

Each component is a sum according to [(7.1)](#gl-7-1) (Fig. [28](#abb-28)). A $3\times2$ matrix times a vector with $2$ components gives a vector with $3$ components.

:::abbildung ml/k1rmv 28
The matrix–vector product component by component: for each row $i$, the entries $a_{ij}$ are multiplied by the matching $x_j$ and added.
:::
::::

⁠**In short:** $\mathbf{A}\mathbf{x}$ is the vector whose component $i$ is the sum $\sum_ja_{ij}x_j$; an $m\times n$ matrix turns a vector in $\mathbb{R}^n$ into a vector in $\mathbb{R}^m$.

### The row view: many dot products

<span class="anker" id="stufe-7-2"></span>

For each component, formula [(7.1)](#gl-7-1) says: row $i$ of the matrix, multiplied entry by entry by $\mathbf{x}$ and summed up. This is the dot product of row $i$ with $\mathbf{x}$ (Fig. [30](#abb-30), left).

:::satz Theorem 7.2 (Row view)
<span class="anker" id="satz-7-2"></span>

Component $i$ of $\mathbf{A}\mathbf{x}$ is the dot product of the $i$th row of $\mathbf{A}$ with $\mathbf{x}$. For a data matrix $\mathbf{X}$ with the rows $\mathbf{x}_i^{\top}$ and a weight vector $\mathbf{w}$, this means

<span class="anker" id="gl-7-2"></span>
$$\mathbf{X}\mathbf{w}=\begin{pmatrix}\mathbf{x}_1^{\top}\mathbf{w}\\\vdots\\\mathbf{x}_N^{\top}\mathbf{w}\end{pmatrix}. \tag{7.2}$$
:::

So the matrix–vector product applies the weighted sum with the weights $\mathbf{w}$ to all examples at once and returns the vector of all predictions. In the picture of comparison with a pattern: each example is compared with the same pattern $\mathbf{w}$.

::::beispiel [Worked example]
For the apartment dataset and $\mathbf{w}=(3,\,10,\,-4)^{\top}$,

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3\\10\\-4\end{pmatrix}=\begin{pmatrix}188\\126\\286\\232\end{pmatrix},$$

the real estate agent's four predictions in thousand euros. Each component is the dot product of a row with $\mathbf{w}$ (Fig. [29](#abb-29)).

:::abbildung ml/k1rzeilen 29
The row view for the real estate agent: each apartment, that is, each row of $\mathbf{X}$, times the weights $\mathbf{w}$.
:::
::::

⁠**In short:** In the row view, $\mathbf{A}\mathbf{x}$ is a list of dot products, one per row; $\mathbf{X}\mathbf{w}$ is the list of predictions for all examples.

:::hintergrund How much computational work a matrix–vector product costs
Each of the $m$ components needs $n$ multiplications and $n-1$ additions. In total that is $m(2n-1)$, or roughly $2mn$ basic arithmetic operations. For the four apartments with three features it is $4\cdot5=20$. For a dataset with one million examples and one hundred features it is about $2\cdot10^8$. A modern processor carries out several billion such operations per second, so a single matrix–vector product of this size is done quickly. Such counts, however, only give the order of magnitude of the computing time, because how fast a computer actually is also depends on how fast it can fetch the numbers from memory.
:::

### The column view: a linear combination of the columns

<span class="anker" id="stufe-7-3"></span>

You can also order the same sum differently. Instead of proceeding row by row, you collect all contributions that belong to $x_1$, then all that belong to $x_2$, and so on. The contributions to $x_j$ are all in column $j$ of the matrix. The product then becomes a linear combination of the columns (Fig. [30](#abb-30), right).

:::abbildung ml/k1zeilenspalten 30
Two ways to read $\mathbf{A}\mathbf{x}$ for $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ and $\mathbf{x}=(2,\,1)^{\top}$. Left, the row view: component $1$ of the result is the dot product of the first row with $\mathbf{x}$. Right, the column view: $\mathbf{A}\mathbf{x}$ is $2$ times the first column $\mathbf{a}_1=(2,1)^{\top}$ plus $1$ times the second column $\mathbf{a}_2=(1,1)^{\top}$.
:::

:::satz Theorem 7.3 (Column view)
<span class="anker" id="satz-7-3"></span>

If $\mathbf{a}_1,\dots,\mathbf{a}_n$ are the columns of $\mathbf{A}\in\mathbb{R}^{m\times n}$, then

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+x_2\mathbf{a}_2+\dots+x_n\mathbf{a}_n=\sum_{j=1}^nx_j\,\mathbf{a}_j . \tag{7.3}$$

The matrix–vector product is the linear combination of the columns of $\mathbf{A}$ with the components of $\mathbf{x}$ as coefficients.
:::

:::beweis Column view
Component $i$ of the right-hand side is $\sum_jx_j\,(\mathbf{a}_j)_i=\sum_jx_j\,a_{ij}$, because the $i$th component of the column $\mathbf{a}_j$ is the entry $a_{ij}$. This is exactly component $i$ of $\mathbf{A}\mathbf{x}$ according to [(7.1)](#gl-7-1).
:::

::::beispiel [Worked example 1]
For the product $\mathbf{A}\mathbf{x}$ from Subsection [7.1](#stufe-7-1),

$$\begin{pmatrix}1&2\\0&-1\\3&1\end{pmatrix}\begin{pmatrix}2\\1\end{pmatrix}=2\begin{pmatrix}1\\0\\3\end{pmatrix}+1\begin{pmatrix}2\\-1\\1\end{pmatrix}=\begin{pmatrix}4\\-1\\7\end{pmatrix}.$$
::::

::::beispiel [Worked example 2]
The real estate agent's predictions are $3$ times the column of floor areas plus $10$ times the column of rooms plus $(-4)$ times the column of distances (Fig. [31](#abb-31)). As in Subsection [6.1](matrizen-und-die-datenmatrix.html#stufe-6-1), the columns of $\mathbf{X}$ are called $\mathbf{a}_1$, $\mathbf{a}_2$, $\mathbf{a}_3$. In this form you can see which part of each prediction comes from which feature: the first term contains the contributions of the floor area, the second those of the rooms, the third those of the distance.

:::abbildung ml/k1rspalten 31
The column view for the real estate agent: each column $\mathbf{a}_j$ of $\mathbf{X}$ is multiplied by its weight $w_j$, and then the three vectors are added.
:::
::::

⁠**In short:** In the column view, $\mathbf{A}\mathbf{x}$ is a linear combination of the columns of $\mathbf{A}$; the components of $\mathbf{x}$ say how much of each column is taken.

:::hintergrund Why there are two views of the same calculation
Both views compute the same $m\cdot n$ products $a_{ij}x_j$ and add them up. The row view first combines them row by row, the column view first column by column; for finitely many terms the order does not matter, as with the double sum in Subsection [1.1](vektoren-daten-als-zahlenlisten.html#stufe-1-1). But each view answers a different question. The row view asks: what comes out in component $i$? The column view asks: which results can the matrix produce at all if you choose $\mathbf{x}$ freely? The second question leads directly to the next concept.
:::

### The column space

<span class="anker" id="stufe-7-4"></span>

If you let $\mathbf{x}$ run through all vectors of $\mathbb{R}^n$, then by the column view $\mathbf{A}\mathbf{x}$ runs through all linear combinations of the columns. In general, these are not all vectors of $\mathbb{R}^m$.

:::definition Definition 7.4 (Column space)
<span class="anker" id="satz-7-4"></span>

The __column space__ of a matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ is the set of all vectors $\mathbf{A}\mathbf{x}$ with $\mathbf{x}\in\mathbb{R}^n$, that is, the set of all linear combinations of the columns of $\mathbf{A}$.
:::

::::beispiel [Worked example 1]
The matrix $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ has the columns $(1,\,2)^{\top}$ and $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$. Every linear combination is a multiple of $(1,\,2)^{\top}$. So the column space is only the line through the origin in the direction of $(1,\,2)^{\top}$, even though the results have two components. The vector $(3,\,6)^{\top}$ lies in it; the vector $(1,\,1)^{\top}$ does not.
::::

::::beispiel [Worked example 2]
The matrix $\mathbf{H}=\Bigl(\begin{smallmatrix}1&0\\0&1\\1&1\end{smallmatrix}\Bigr)$ gives $\mathbf{H}\mathbf{x}=(x_1,\,x_2,\,x_1+x_2)^{\top}$. Its column space consists of the vectors of $\mathbb{R}^3$ whose third component is the sum of the first two; this is a plane in space. The vector $(1,\,2,\,3)^{\top}=\mathbf{H}\,(1,\,2)^{\top}$ lies in it, but $(1,\,1,\,1)^{\top}$ does not, because $1+1\ne1$.
::::

For a data matrix this means: the predictions $\mathbf{X}\mathbf{w}$ always lie in the column space of $\mathbf{X}$, no matter which weights you choose. With these features, only very specific lists of predictions can be produced at all.

⁠**In short:** The column space of a matrix is the set of all vectors $\mathbf{A}\mathbf{x}$, that is, everything that can be formed as a linear combination of its columns.

:::aufgabe Exercise 16 ★ Two views of one product
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

Compute $\mathbf{B}\mathbf{x}$ for $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ and $\mathbf{x}=(1,\,3,\,-1)^{\top}$, once in the row view and once in the column view.

</li>

<li>

Is $\mathbf{B}\,(1,\,2)^{\top}$ defined? And $\mathbf{B}\,(1,\,2,\,3)^{\top}$? Explain your answer using the sizes, and state how many components the result has if it is defined.

</li>

<li>

Does $(2,\,0,\,2)^{\top}$ lie in the column space of the matrix $\mathbf{H}$ from Subsection [7.4](#stufe-7-4)? And $(2,\,1,\,2)^{\top}$?

</li>

</ol>

:::loesung
(a) Row view: $(1\cdot1+0\cdot3+2\cdot(-1),\ 2\cdot1+1\cdot3+0\cdot(-1))^{\top}=(-1,\,5)^{\top}$. Column view: $1\,(1,\,2)^{\top}+3\,(0,\,1)^{\top}-1\,(2,\,0)^{\top}=(1+0-2,\ 2+3-0)^{\top}=(-1,\,5)^{\top}$.

(b) $\mathbf{B}$ has three columns. $\mathbf{B}\,(1,\,2)^{\top}$ is not defined, because the vector has only two components. $\mathbf{B}\,(1,\,2,\,3)^{\top}$ is defined and has as many components as $\mathbf{B}$ has rows, namely two: $(1+0+6,\ 2+2+0)^{\top}=(7,\,4)^{\top}$.

(c) The column space of $\mathbf{H}$ consists of the vectors whose third component is the sum of the first two. For $(2,\,0,\,2)^{\top}$, $2+0=2$: yes, it is $\mathbf{H}\,(2,\,0)^{\top}$. For $(2,\,1,\,2)^{\top}$, $2+1=3\ne2$: no.
:::
:::

:::aufgabe Exercise 17 ★★ The monthly rent
<span class="anker" id="aufg-17"></span>

A rent index estimates the monthly rent of an apartment with the weights $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ in euros per square meter, per room and per kilometer.

<ol class="al">

<li>

Compute the estimated rents of all four apartments as $\mathbf{X}\mathbf{w}_{\mathrm M}$, once in the row view and once in the column view.

</li>

<li>

How many multiplications and additions did you need? How many would it be for $10\,000$ apartments with $20$ features?

</li>

</ol>

:::loesung
(a) Row view, for apartment 1: $12\cdot60+30\cdot2-8\cdot3=720+60-24=756$, and likewise $502$, $1152$ and $914$ euros. Column view:

$$12\begin{pmatrix}60\\40\\90\\70\end{pmatrix}+30\begin{pmatrix}2\\1\\4\\3\end{pmatrix}-8\begin{pmatrix}3\\1\\6\\2\end{pmatrix}=\begin{pmatrix}720\\480\\1080\\840\end{pmatrix}+\begin{pmatrix}60\\30\\120\\90\end{pmatrix}-\begin{pmatrix}24\\8\\48\\16\end{pmatrix}=\begin{pmatrix}756\\502\\1152\\914\end{pmatrix}.$$

(b) Each of the four components needs $3$ multiplications and $2$ additions, $12+8=20$ in total. For $10\,000$ apartments with $20$ features, it is $10\,000\cdot20=200\,000$ multiplications and $10\,000\cdot19=190\,000$ additions, $390\,000\approx2mn$ in total, with $m=10\,000$, $n=20$.
:::
:::
