---
title: Transpose, symmetry and the Gram matrix
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Chapter 1: Vectors and Matrices
nachschlagen: ja
order: 15211100
summary: If you swap the rows and columns of a matrix, you get its transpose.
tags: transpose, symmetric, Gram matrix
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
If you swap the rows and columns of a matrix, you get its transpose. With it, all dot products of a dataset can be collected in a single matrix: the similarities of all examples to one another and the relationships of all features to one another.
:::

### The transpose

<span class="anker" id="stufe-10-1"></span>

The symbol $^{\top}$ is familiar from Subsection [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3): it turns a column into a row. For matrices it means the same thing, applied to each column: column $j$ becomes row $j$. In the process, the matrix is reflected across its diagonal.

:::definition Definition 10.1 (Transpose)
<span class="anker" id="satz-10-1"></span>

The __transpose__ of a matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ is the matrix $\mathbf{A}^{\top}\in\mathbb{R}^{n\times m}$ with

<span class="anker" id="gl-10-1"></span>
$$(\mathbf{A}^{\top})_{ij}=a_{ji} . \tag{10.1}$$
:::

A vector $\mathbf{x}\in\mathbb{R}^d$ is a $d\times1$ matrix, and its transpose $\mathbf{x}^{\top}$ is the $1\times d$ matrix with the same entries. So the notation $\mathbf{u}^{\top}\mathbf{v}$ from Subsection [2.1](das-skalarprodukt.html#stufe-2-1) is now literally a matrix product: a $1\times d$ matrix times a $d\times1$ matrix; the result is a $1\times1$ matrix, that is, a number.

:::satz Theorem 10.2 (Rules of calculation for the transpose)
<span class="anker" id="satz-10-2"></span>

For matrices of compatible sizes and scalars $c$,

$$(\mathbf{A}^{\top})^{\top}=\mathbf{A},\qquad(\mathbf{A}+\mathbf{B})^{\top}=\mathbf{A}^{\top}+\mathbf{B}^{\top},\qquad(c\,\mathbf{A})^{\top}=c\,\mathbf{A}^{\top},\qquad(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top} .$$
:::

:::herleitung The transpose of a product
For $\mathbf{A}\in\mathbb{R}^{m\times n}$ and $\mathbf{B}\in\mathbb{R}^{n\times k}$, by [(10.1)](#gl-10-1) and [(9.1)](das-matrixprodukt.html#gl-9-1),

$$\bigl((\mathbf{A}\mathbf{B})^{\top}\bigr)_{li}=(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^na_{ij}\,b_{jl}=\sum_{j=1}^n(\mathbf{B}^{\top})_{lj}\,(\mathbf{A}^{\top})_{ji}=(\mathbf{B}^{\top}\mathbf{A}^{\top})_{li} .$$

The first three rules follow directly from the definition.
:::

::::beispiel [Worked example]
$$\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}^{\top}=\begin{pmatrix}1&4\\2&5\\3&6\end{pmatrix}.$$

For $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ and $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$ we have $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$, so $(\mathbf{C}\mathbf{D})^{\top}=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$. The same result comes from $\mathbf{D}^{\top}\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&4\\3&7\end{smallmatrix}\bigr)$, whereas $\mathbf{C}^{\top}\mathbf{D}^{\top}=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$ is something different.
::::

⁠**In short:** Transposing swaps rows and columns; for a product, the order is reversed, $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$.

:::hintergrund Why the order is reversed when you transpose a product
In the product $\mathbf{A}\mathbf{B}$, the rows of $\mathbf{A}$ meet the columns of $\mathbf{B}$. After transposing, the rows of $\mathbf{A}$ are the columns of $\mathbf{A}^{\top}$, and the columns of $\mathbf{B}$ are the rows of $\mathbf{B}^{\top}$. For rows to meet columns again, $\mathbf{B}^{\top}$ must be on the left. The sizes show it too: $(\mathbf{A}\mathbf{B})^{\top}$ has size $k\times m$, and $\mathbf{B}^{\top}\mathbf{A}^{\top}$ is $(k\times n)\cdot(n\times m)$, so the sizes fit. The expression $\mathbf{A}^{\top}\mathbf{B}^{\top}$ would be $(n\times m)\cdot(k\times n)$ and is defined only if $m=k$ happens to hold. A special case of the rule is $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$: a number is its own transpose, so $\mathbf{u}^{\top}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{u}$.
:::

### Symmetric matrices

<span class="anker" id="stufe-10-2"></span>

Some tables stay the same when they are reflected across their diagonal. A table of distances between cities is one of them: the route from Munich to Cologne is as long as the route from Cologne to Munich.

:::definition Definition 10.3 (Symmetric matrix)
<span class="anker" id="satz-10-3"></span>

A square matrix $\mathbf{A}$ is called __symmetric__ if $\mathbf{A}^{\top}=\mathbf{A}$, that is, $a_{ij}=a_{ji}$ for all $i,j$.
:::

Every diagonal matrix is symmetric. An important source of symmetric matrices are products of a matrix with its own transpose: for every matrix $\mathbf{A}$,

<span class="anker" id="gl-10-2"></span>
$$(\mathbf{A}^{\top}\mathbf{A})^{\top}=\mathbf{A}^{\top}(\mathbf{A}^{\top})^{\top}=\mathbf{A}^{\top}\mathbf{A} , \tag{10.2}$$

so $\mathbf{A}^{\top}\mathbf{A}$ is symmetric, and so is $\mathbf{A}\mathbf{A}^{\top}$.

::::beispiel [Worked example]
$\bigl(\begin{smallmatrix}2&1\\1&3\end{smallmatrix}\bigr)$ is symmetric, the rotation $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ is not. For $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$,

$$\mathbf{C}^{\top}\mathbf{C}=\begin{pmatrix}1&3\\2&4\end{pmatrix}\begin{pmatrix}1&2\\3&4\end{pmatrix}=\begin{pmatrix}10&14\\14&20\end{pmatrix},$$

which is symmetric, as [(10.2)](#gl-10-2) requires.
::::

⁠**In short:** A symmetric matrix equals its transpose; $\mathbf{A}^{\top}\mathbf{A}$ and $\mathbf{A}\mathbf{A}^{\top}$ are always symmetric.

:::hintergrund Dot products with weights
In the dot product $\mathbf{u}^{\top}\mathbf{v}=\sum_ju_jv_j$, every position counts equally. If you want the positions to count with different strengths, you take positive weights $d_1,\dots,d_n$ and form $\sum_jd_j\,u_jv_j$. With the diagonal matrix $\mathbf{D}=\operatorname{diag}(d_1,\dots,d_n)$ this is $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$, because $\mathbf{D}\mathbf{v}=(d_1v_1,\dots,d_nv_n)^{\top}$.

This number obeys the same rules of calculation as the ordinary dot product. It is linear in each of the two vectors, and $\mathbf{u}^{\top}\mathbf{D}\mathbf{u}=\sum_jd_ju_j^2$ is positive for every $\mathbf{u}\ne\mathbf{0}$. It is symmetric because $\mathbf{D}$ is symmetric: a number is its own transpose, and with the rule for the transpose of a product, applied twice, $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}=(\mathbf{u}^{\top}\mathbf{D}\mathbf{v})^{\top}=\mathbf{v}^{\top}\mathbf{D}^{\top}\mathbf{u}=\mathbf{v}^{\top}\mathbf{D}\mathbf{u}$. Because the proof of the Cauchy–Schwarz inequality used only these rules, you can just as well measure lengths, distances and angles with $\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$. They merely come out differently. For example, $(1,\,1)^{\top}$ and $(-1,\,1)^{\top}$ are orthogonal in the ordinary sense, but not with $\mathbf{D}=\operatorname{diag}(2,\,1)$: $(1,\,1)\,\mathbf{D}\,(-1,\,1)^{\top}=2\cdot1\cdot(-1)+1\cdot1\cdot1=-1$.

Standardizing from Subsection [4.5](abstande-und-einheiten.html#stufe-4-5) is exactly such a weighting. The distance between two standardized examples is $\sqrt{(\mathbf{x}_a-\mathbf{x}_b)^{\top}\mathbf{D}\,(\mathbf{x}_a-\mathbf{x}_b)}$ with $\mathbf{D}=\operatorname{diag}(1/s_1^2,\dots,1/s_d^2)$. Conversely, every such weighting acts like a change of units: if you multiply feature $j$ by $\sqrt{d_j}$, the ordinary dot product of the converted vectors is $\sum_j(\sqrt{d_j}\,u_j)(\sqrt{d_j}\,v_j)=\mathbf{u}^{\top}\mathbf{D}\mathbf{v}$. So the choice of units and the choice of the weights in $\mathbf{D}$ are the same decision.
:::

### The Gram matrix of the examples

<span class="anker" id="stufe-10-3"></span>

How similar is each example of a dataset to every other one? You can write all pairwise dot products in a table: row $i$, column $k$ contains $\mathbf{x}_i^{\top}\mathbf{x}_k$. This table is a single matrix product.

:::definition Definition 10.4 (Gram matrix)
<span class="anker" id="satz-10-4"></span>

The __Gram matrix__ of a list of vectors $\mathbf{v}_1,\dots,\mathbf{v}_k$ is the $k\times k$ matrix of the pairwise dot products, with the entry $\mathbf{v}_i^{\top}\mathbf{v}_l$ in row $i$ and column $l$.
:::

For the examples of a dataset, this is the matrix $\mathbf{X}\mathbf{X}^{\top}\in\mathbb{R}^{N\times N}$, because its entry $(i,k)$ is row $i$ of $\mathbf{X}$ times column $k$ of $\mathbf{X}^{\top}$, that is, $\mathbf{x}_i^{\top}\mathbf{x}_k$:

<span class="anker" id="gl-10-3"></span>
$$(\mathbf{X}\mathbf{X}^{\top})_{ik}=\mathbf{x}_i^{\top}\mathbf{x}_k . \tag{10.3}$$

It is symmetric, its diagonal holds the squared lengths $\lVert\mathbf{x}_i\rVert^2$, and by [(4.1)](abstande-und-einheiten.html#gl-4-1) all distances can be read off from it:

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{x}_i-\mathbf{x}_k\rVert^2=(\mathbf{X}\mathbf{X}^{\top})_{ii}+(\mathbf{X}\mathbf{X}^{\top})_{kk}-2\,(\mathbf{X}\mathbf{X}^{\top})_{ik} . \tag{10.4}$$

If you divide entry $(i,k)$ by $\sqrt{(\mathbf{X}\mathbf{X}^{\top})_{ii}\,(\mathbf{X}\mathbf{X}^{\top})_{kk}}$, you get the cosine similarity of $\mathbf{x}_i$ and $\mathbf{x}_k$.

::::beispiel [Worked example]
For the three texts from Subsection [5.4](winkel-und-ahnlichkeit.html#stufe-5-4),

$$\mathbf{X}=\begin{pmatrix}3&2&0\\6&4&0\\0&1&3\end{pmatrix},\qquad \mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}13&26&2\\26&52&4\\2&4&10\end{pmatrix}.$$

By [(10.4)](#gl-10-4), the distance between text 1 and text 3 is $\sqrt{13+10-2\cdot2}=\sqrt{19}$, as computed earlier. The cosine similarity of text 1 and text 2 is $26/\sqrt{13\cdot52}=1$.
::::

⁠**In short:** The Gram matrix $\mathbf{X}\mathbf{X}^{\top}$ is the table of all pairwise dot products of the examples; all lengths, distances and angles follow from it.

:::hintergrund The Gram matrix contains the entire geometry of the dataset
Lengths, distances and angles between the examples depend only on the dot products, not on the individual coordinates. If you rotate the whole dataset about the origin, for example, all coordinates change, but no dot product does, and the Gram matrix stays the same. So two datasets with the same Gram matrix look geometrically the same. If you only want to know which examples are similar to one another, you therefore do not need the data matrix itself, only its Gram matrix.
:::

### The Gram matrix of the features

<span class="anker" id="stufe-10-4"></span>

If you reverse the roles, you get a table about the features: how much do two features go together across all examples? Their feature columns are vectors in $\mathbb{R}^N$, and their dot product measures this. This Gram matrix of the columns is $\mathbf{X}^{\top}\mathbf{X}\in\mathbb{R}^{d\times d}$:

<span class="anker" id="gl-10-5"></span>
$$(\mathbf{X}^{\top}\mathbf{X})_{jl}=\sum_{i=1}^Nx_{ij}\,x_{il} . \tag{10.5}$$

Entry $(j,l)$ is the dot product of the feature columns $j$ and $l$; the diagonal holds the sum of squares of each feature.

:::satz Theorem 10.5 (The Gram matrix as a sum over the examples)
<span class="anker" id="satz-10-5"></span>

<span class="anker" id="gl-10-6"></span>
$$\mathbf{X}^{\top}\mathbf{X}=\sum_{i=1}^N\mathbf{x}_i\,\mathbf{x}_i^{\top} . \tag{10.6}$$

Each example contributes its own outer product.
:::

Entry $(j,l)$ of the right-hand side is $\sum_ix_{ij}\,x_{il}$, the same as in [(10.5)](#gl-10-5). So if a new example is added, $\mathbf{X}^{\top}\mathbf{X}$ changes only by one more layer $\mathbf{x}_{N+1}\mathbf{x}_{N+1}^{\top}$; you do not have to recompute everything.

::::beispiel [Worked example]
For the texts,

$$\mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$

The entries of the first row are the dot products of the “goal” column with the three feature columns (Fig. [37](#abb-37)).

:::abbildung ml/k1rgrammerk 37
The first row of the Gram matrix of the features: the “goal” column $(3,\,6,\,0)^{\top}$ times itself, times the “ball” column $(2,\,4,\,1)^{\top}$ and times the “election” column $(0,\,0,\,3)^{\top}$.
:::

The $0$ in position $(1,3)$ says: the words “goal” and “election” never occur together in any of the texts. As the sum of the three outer products:

$$\begin{pmatrix}9&6&0\\6&4&0\\0&0&0\end{pmatrix}+\begin{pmatrix}36&24&0\\24&16&0\\0&0&0\end{pmatrix}+\begin{pmatrix}0&0&0\\0&1&3\\0&3&9\end{pmatrix}=\begin{pmatrix}45&30&0\\30&21&3\\0&3&9\end{pmatrix}.$$
::::

⁠**In short:** $\mathbf{X}^{\top}\mathbf{X}$ is the Gram matrix of the feature columns; it is the sum of the outer products $\mathbf{x}_i\mathbf{x}_i^{\top}$ of all examples.

:::aufgabe Exercise 24 ★ Transposing
<span class="anker" id="aufg-24"></span>

<ol class="al">

<li>

Give $\mathbf{B}^{\top}$ for $\mathbf{B}=\bigl(\begin{smallmatrix}1&0&2\\2&1&0\end{smallmatrix}\bigr)$ and compute $\mathbf{B}^{\top}\mathbf{B}$ and $\mathbf{B}\mathbf{B}^{\top}$. What are their sizes, and are they symmetric?

</li>

<li>

Show with the rules of calculation: $(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{B}^{\top}=\Bigl(\begin{smallmatrix}1&2\\0&1\\2&0\end{smallmatrix}\Bigr)$. Then

$$\mathbf{B}^{\top}\mathbf{B}=\begin{pmatrix}5&2&2\\2&1&0\\2&0&4\end{pmatrix}\in\mathbb{R}^{3\times3},\qquad \mathbf{B}\mathbf{B}^{\top}=\begin{pmatrix}5&2\\2&5\end{pmatrix}\in\mathbb{R}^{2\times2}.$$

Both are symmetric, as [(10.2)](#gl-10-2) requires. The entry $(1,1)$ of $\mathbf{B}^{\top}\mathbf{B}$ is $1^2+2^2=5$, the sum of squares of the first column; the entry $(1,2)$ of $\mathbf{B}\mathbf{B}^{\top}$ is $1\cdot2+0\cdot1+2\cdot0=2$, the dot product of the two rows.

(b) The rule for the transpose of a product, applied twice: $(\mathbf{A}\mathbf{B}\mathbf{C})^{\top}=\bigl((\mathbf{A}\mathbf{B})\mathbf{C}\bigr)^{\top}=\mathbf{C}^{\top}(\mathbf{A}\mathbf{B})^{\top}=\mathbf{C}^{\top}\mathbf{B}^{\top}\mathbf{A}^{\top}$.
:::
:::

:::aufgabe Exercise 25 ★★ Gram matrices of a small dataset
<span class="anker" id="aufg-25"></span>

A dataset has three examples with two features: $\mathbf{x}_1=(1,\,0)^{\top}$, $\mathbf{x}_2=(2,\,1)^{\top}$, $\mathbf{x}_3=(0,\,3)^{\top}$.

<ol class="al">

<li>

Set up $\mathbf{X}$ and compute $\mathbf{X}\mathbf{X}^{\top}$ and $\mathbf{X}^{\top}\mathbf{X}$.

</li>

<li>

Read off the distance between $\mathbf{x}_2$ and $\mathbf{x}_3$ from $\mathbf{X}\mathbf{X}^{\top}$ and check it directly.

</li>

<li>

Confirm [(10.6)](#gl-10-6) by adding the three outer products $\mathbf{x}_i\mathbf{x}_i^{\top}$.

</li>

</ol>

:::loesung
(a) $\mathbf{X}=\Bigl(\begin{smallmatrix}1&0\\2&1\\0&3\end{smallmatrix}\Bigr)$,

$$\mathbf{X}\mathbf{X}^{\top}=\begin{pmatrix}1&2&0\\2&5&3\\0&3&9\end{pmatrix},\qquad \mathbf{X}^{\top}\mathbf{X}=\begin{pmatrix}5&2\\2&10\end{pmatrix}.$$

(b) By [(10.4)](#gl-10-4), $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert^2=5+9-2\cdot3=8$, so the distance is $\sqrt8\approx2.83$. Directly: $\mathbf{x}_2-\mathbf{x}_3=(2,\,-2)^{\top}$ with the squared length $4+4=8$.

(c) $\mathbf{x}_1\mathbf{x}_1^{\top}=\bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)$, $\mathbf{x}_2\mathbf{x}_2^{\top}=\bigl(\begin{smallmatrix}4&2\\2&1\end{smallmatrix}\bigr)$, $\mathbf{x}_3\mathbf{x}_3^{\top}=\bigl(\begin{smallmatrix}0&0\\0&9\end{smallmatrix}\bigr)$; the sum is $\bigl(\begin{smallmatrix}5&2\\2&10\end{smallmatrix}\bigr)=\mathbf{X}^{\top}\mathbf{X}$.
:::
:::
