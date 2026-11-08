---
title: The matrix product
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15211000
summary: Two linear maps applied one after the other again give a linear map, and therefore a matrix.
tags: matrix product, outer product
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
Two linear maps applied one after the other again give a linear map, and therefore a matrix. This section determines it. The result is the matrix product, and its definition follows inevitably from this task.
:::

### The matrix product

<span class="anker" id="stufe-9-1"></span>

First a vector $\mathbf{x}\in\mathbb{R}^k$ is mapped with a matrix $\mathbf{B}\in\mathbb{R}^{n\times k}$, then the result $\mathbf{B}\mathbf{x}\in\mathbb{R}^n$ with a matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ (Fig. [33](#abb-33)). The composition $\mathbf{x}\mapsto\mathbf{A}(\mathbf{B}\mathbf{x})$ is linear, because each of the two stages preserves sums and multiples. So by the theorem in Subsection [8.2](lineare-abbildungen.html#stufe-8-2) it has a matrix. Its column $l$ is the image of $\mathbf{e}_l$: the first stage turns this unit vector into the column $\mathbf{B}\mathbf{e}_l$ of $\mathbf{B}$, and the second stage multiplies this column by $\mathbf{A}$.

:::abbildung ml/k1hinter 33
Top: two linear maps one after the other, first $\mathbf{B}$, then $\mathbf{A}$. Bottom: the same map in one step, with the single matrix $\mathbf{A}\mathbf{B}$. The matrix product is defined precisely so that both ways give the same result.
:::

:::definition Definition 9.1 (Matrix product)
<span class="anker" id="satz-9-1"></span>

For $\mathbf{A}\in\mathbb{R}^{m\times n}$ and $\mathbf{B}\in\mathbb{R}^{n\times k}$, the __matrix product__ $\mathbf{A}\mathbf{B}\in\mathbb{R}^{m\times k}$ is the matrix with the entries

<span class="anker" id="gl-9-1"></span>
$$(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^{n}a_{ij}\,b_{jl},\qquad i=1,\dots,m,\quad l=1,\dots,k . \tag{9.1}$$
:::

Entry $(i,l)$ is the dot product of row $i$ of $\mathbf{A}$ with column $l$ of $\mathbf{B}$. The product is defined only if $\mathbf{A}$ has as many columns as $\mathbf{B}$ has rows: the “inner” sizes must match, $(m\times n)\cdot(n\times k)$, and the result has the “outer” size $m\times k$.

:::satz Theorem 9.2 (The product is the composition)
<span class="anker" id="satz-9-2"></span>

For all $\mathbf{x}\in\mathbb{R}^k$, $(\mathbf{A}\mathbf{B})\,\mathbf{x}=\mathbf{A}\,(\mathbf{B}\mathbf{x})$.
:::

:::herleitung Composition
By [(7.1)](das-matrix-vektor-produkt.html#gl-7-1) and [(9.1)](#gl-9-1), component $i$ of the left-hand side is

$$\sum_{l=1}^k(\mathbf{A}\mathbf{B})_{il}\,x_l=\sum_{l=1}^k\sum_{j=1}^na_{ij}\,b_{jl}\,x_l=\sum_{j=1}^na_{ij}\Bigl(\sum_{l=1}^kb_{jl}\,x_l\Bigr)=\sum_{j=1}^na_{ij}\,(\mathbf{B}\mathbf{x})_j ,$$

and this is component $i$ of $\mathbf{A}(\mathbf{B}\mathbf{x})$. In the middle step, the two sums were swapped and $a_{ij}$ was moved in front of the inner sum.
:::

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ and $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$,

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&1\\1&0\end{pmatrix}.$$

Each of the four entries is a sum according to [(9.1)](#gl-9-1) (Fig. [34](#abb-34)).

:::abbildung ml/k1rprodukt 34
The matrix product entry by entry: entry $(i,l)$ is row $i$ of $\mathbf{A}$ times column $l$ of $\mathbf{B}$.
:::

Check with $\mathbf{x}=(1,\,2)^{\top}$: $\mathbf{B}\mathbf{x}=(2,\,1)^{\top}$, then $\mathbf{A}(\mathbf{B}\mathbf{x})=(4,\,1)^{\top}$; and directly, $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+2,\ 1+0)^{\top}=(4,\,1)^{\top}$.

⁠**In short:** The matrix product $\mathbf{A}\mathbf{B}$ is the matrix of the map “first $\mathbf{B}$, then $\mathbf{A}$”; its entry $(i,l)$ is row $i$ of $\mathbf{A}$ times column $l$ of $\mathbf{B}$.

:::hintergrund Why the matrix product is defined exactly this way
At first glance, formula [(9.1)](#gl-9-1) looks arbitrary. It would seem more natural to multiply matrices entry by entry. But the matrix product is not a free invention; it is fixed by a requirement: it is supposed to be the matrix of the composition. By the theorem in Subsection [8.2](lineare-abbildungen.html#stufe-8-2), this matrix is unique, and its column $l$ must be the image of $\mathbf{e}_l$ under both maps, that is, $\mathbf{A}$ times column $l$ of $\mathbf{B}$. Writing this out component by component gives exactly [(9.1)](#gl-9-1). An entrywise product would have no such meaning: it does not describe the composition of two maps.
:::

### Many vectors at once

<span class="anker" id="stufe-9-2"></span>

By the derivation of the product, column $l$ of $\mathbf{A}\mathbf{B}$ is the product of $\mathbf{A}$ with column $l$ of $\mathbf{B}$. So you can read a matrix product as several matrix–vector products side by side:

<span class="anker" id="gl-9-2"></span>
$$\mathbf{A}\begin{pmatrix}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{B}\mathbf{e}_k\end{pmatrix}=\begin{pmatrix}\mathbf{A}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{A}\mathbf{B}\mathbf{e}_k\end{pmatrix}. \tag{9.2}$$

Likewise, row $i$ of $\mathbf{A}\mathbf{B}$ is row $i$ of $\mathbf{A}$, multiplied by $\mathbf{B}$.

For data this means: if you want to apply several weighted sums to all examples, you write the weight vectors side by side as the columns of a matrix $\mathbf{W}$. The product $\mathbf{X}\mathbf{W}$ then contains in column $l$ the predictions with the $l$th weight vector.

⁠**Worked example:** Besides the purchase price with $\mathbf{w}=(3,\,10,\,-4)^{\top}$ (thousand euros), the monthly rent is to be estimated with the weights $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$ (euros). With $\mathbf{W}=\begin{pmatrix}\mathbf{w}&\mathbf{w}_{\mathrm M}\end{pmatrix}\in\mathbb{R}^{3\times2}$,

$$\mathbf{X}\mathbf{W}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3&12\\10&30\\-4&-8\end{pmatrix}=\begin{pmatrix}188&756\\126&502\\286&1152\\232&914\end{pmatrix}.$$

Row $i$ contains both estimates for apartment $i$, column $1$ all purchase prices, column $2$ all rents.

⁠**In short:** The columns of $\mathbf{A}\mathbf{B}$ are $\mathbf{A}$ times the columns of $\mathbf{B}$; $\mathbf{X}\mathbf{W}$ applies several weighted sums to all examples at once.

### Rules of calculation: the order matters

<span class="anker" id="stufe-9-3"></span>

For numbers, $2\cdot3=3\cdot2$. For matrices this does not hold, and the reason is easy to see: rotating first and then stretching is something different from stretching first and then rotating (Fig. [35](#abb-35)).

:::abbildung ml/k1reihenfolge 35
The unit square with $\mathbf{e}_1$ (red) and $\mathbf{e}_2$ (green), and next to it its images under $\mathbf{S}\mathbf R$ and $\mathbf R\mathbf{S}$. Here $\mathbf R$ is the rotation by $90^\circ$ and $\mathbf{S}=\operatorname{diag}(2,\,0.5)$ the stretch. The order decides whether the rectangle becomes long horizontally or vertically.
:::

:::satz Theorem 9.3 (Rules of calculation for the matrix product)
<span class="anker" id="satz-9-3"></span>

For matrices of compatible sizes and scalars $c$:

<ol class="rm">

<li>

$(\mathbf{A}\mathbf{B})\mathbf{C}=\mathbf{A}(\mathbf{B}\mathbf{C})$ (associative);

</li>

<li>

$\mathbf{A}(\mathbf{B}+\mathbf{C})=\mathbf{A}\mathbf{B}+\mathbf{A}\mathbf{C}$ and $(\mathbf{A}+\mathbf{B})\mathbf{C}=\mathbf{A}\mathbf{C}+\mathbf{B}\mathbf{C}$ (distributive);

</li>

<li>

$c\,(\mathbf{A}\mathbf{B})=(c\,\mathbf{A})\mathbf{B}=\mathbf{A}(c\,\mathbf{B})$.

</li>

</ol>

In general, however, $\mathbf{A}\mathbf{B}\ne\mathbf{B}\mathbf{A}$: the matrix product is *not* commutative.
:::

Rule (i) follows from the meaning: both sides are the matrix of the map “first $\mathbf{C}$, then $\mathbf{B}$, then $\mathbf{A}$”, because $(\mathbf{A}\mathbf{B})(\mathbf{C}\mathbf{x})=\mathbf{A}(\mathbf{B}(\mathbf{C}\mathbf{x}))=\mathbf{A}((\mathbf{B}\mathbf{C})\mathbf{x})$ for every $\mathbf{x}$. Rules (ii) and (iii) are verified entry by entry with [(9.1)](#gl-9-1) and the rules for sums.

⁠**Worked example 1:** With the rotation $\mathbf R=\mathbf R_{90^\circ}=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ and the stretch $\mathbf{S}=\operatorname{diag}(2,\,0.5)$,

$$\mathbf{S}\mathbf R=\begin{pmatrix}0&-2\\0.5&0\end{pmatrix},\qquad \mathbf R\mathbf{S}=\begin{pmatrix}0&-0.5\\2&0\end{pmatrix}.$$

Rotating first, then stretching sends $\mathbf{e}_1$ to $(0,\,0.5)^{\top}$; stretching first, then rotating sends it to $(0,\,2)^{\top}$.

⁠**Worked example 2:** From Subsection [9.1](#stufe-9-1), $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\bigr)$, but $\mathbf{B}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$. With different sizes it is even clearer: for $\mathbf{A}\in\mathbb{R}^{2\times3}$ and $\mathbf{B}\in\mathbb{R}^{3\times2}$, $\mathbf{A}\mathbf{B}$ is a $2\times2$ matrix and $\mathbf{B}\mathbf{A}$ a $3\times3$ matrix.

⁠**In short:** In a matrix product you may regroup the parentheses and multiply out, but you may not swap the order.

:::hintergrund Why the placement of parentheses saves computing time
By rule (i), $(\mathbf{A}\mathbf{B})\mathbf{x}=\mathbf{A}(\mathbf{B}\mathbf{x})$. The result is the same, the effort is not. For two $n\times n$ matrices, the product $\mathbf{A}\mathbf{B}$ needs $n$ multiplications and $n-1$ additions for each of the $n^2$ entries, together about $2n^3$ basic arithmetic operations; after that, $(\mathbf{A}\mathbf{B})\mathbf{x}$ costs about another $2n^2$. The route $\mathbf{A}(\mathbf{B}\mathbf{x})$ consists of two matrix–vector products of about $2n^2$ each. For $n=1000$ that is roughly $2\cdot10^9$ versus $4\cdot10^6$ basic arithmetic operations, a difference by a factor of $500$. Anyone who applies a long chain of matrices to a vector therefore computes from right to left and never forms the product matrix.
:::

### Two linear stages are one

<span class="anker" id="stufe-9-4"></span>

If you connect several linear computing stages in series, no new kind of map arises. By Subsection [9.1](#stufe-9-1) this is clear, but it deserves a theorem of its own, because it marks the limits of linear rules.

:::satz Theorem 9.4 (Linear maps connected in series)
<span class="anker" id="satz-9-4"></span>

If $f(\mathbf{x})=\mathbf{B}\mathbf{x}$ and $g(\mathbf{u})=\mathbf{A}\mathbf{u}$ are linear, then the composition $\mathbf{x}\mapsto g(f(\mathbf{x}))$ is again linear, namely with the single matrix $\mathbf{A}\mathbf{B}$. The same holds for every finite chain of linear stages.
:::

No matter how many linear stages you connect in series, the result can always be computed with a single matrix in one step. So whatever a chain of linear stages can do, a single matrix can already do. From signals and systems you know the same thing: two linear systems connected in series together form a linear system again.

⁠**Worked example:** A first stage turns three numbers into two, $\mathbf{B}=\bigl(\begin{smallmatrix}1&2&0\\0&1&-1\end{smallmatrix}\bigr)$, a second turns two numbers back into three, $\mathbf{A}=\Bigl(\begin{smallmatrix}2&1\\1&-1\\0&3\end{smallmatrix}\Bigr)$. Together this is the single matrix

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&5&-1\\1&1&1\\0&3&-3\end{pmatrix}.$$

Check with $\mathbf{x}=(1,\,1,\,1)^{\top}$: $\mathbf{B}\mathbf{x}=(3,\,0)^{\top}$ and $\mathbf{A}(3,\,0)^{\top}=(6,\,3,\,0)^{\top}$; likewise, $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+5-1,\ 1+1+1,\ 0+3-3)^{\top}=(6,\,3,\,0)^{\top}$.

⁠**In short:** Linear stages in series together form a single linear map; its matrix is the product of the individual matrices.

### The outer product

<span class="anker" id="stufe-9-5"></span>

The dot product $\mathbf{u}^{\top}\mathbf{v}$ is “row times column” and gives a number. If you reverse the order, “column times row”, then by [(9.1)](#gl-9-1) you get a whole matrix: the table of all products of one component of the first vector with one component of the second, like a multiplication table.

:::definition Definition 9.5 (Outer product)
<span class="anker" id="satz-9-5"></span>

For $\mathbf{u}\in\mathbb{R}^m$ and $\mathbf{v}\in\mathbb{R}^n$, the __outer product__ $\mathbf{u}\mathbf{v}^{\top}\in\mathbb{R}^{m\times n}$ is the matrix with the entries

<span class="anker" id="gl-9-3"></span>
$$(\mathbf{u}\mathbf{v}^{\top})_{ij}=u_i\,v_j . \tag{9.3}$$
:::

It is the matrix product of an $m\times1$ matrix with a $1\times n$ matrix. Each column is a multiple of $\mathbf{u}$, namely $v_j\,\mathbf{u}$, and each row is a multiple of $\mathbf{v}^{\top}$.

⁠**Worked example:**

$$\begin{pmatrix}1\\2\\3\end{pmatrix}\begin{pmatrix}4&5\end{pmatrix}=\begin{pmatrix}4&5\\8&10\\12&15\end{pmatrix}.$$

With the outer product, every matrix product can be written as a sum: “column $j$ of $\mathbf{A}$ times row $j$ of $\mathbf{B}$”, summed over $j$,

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}\mathbf{B}=\sum_{j=1}^n\mathbf{a}_j\,\bigl(\text{row $j$ of }\mathbf{B}\bigr) . \tag{9.4}$$

Entry $(i,l)$ of the right-hand side is $\sum_ja_{ij}\,b_{jl}$, exactly as in [(9.1)](#gl-9-1). For $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ and $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ from Subsection [9.1](#stufe-9-1), the sum of two outer products gives $\mathbf{A}\mathbf{B}$ again (Fig. [36](#abb-36)).

:::abbildung ml/k1raeusser 36
The matrix product as a sum of outer products: column $j$ of $\mathbf{A}$ times row $j$ of $\mathbf{B}$, summed over $j=1,2$.
:::

⁠**In short:** The outer product $\mathbf{u}\mathbf{v}^{\top}$ is the table of all products $u_iv_j$; every matrix product is a sum of such tables.

:::aufgabe Exercise 21 ★ Products and sizes
<span class="anker" id="aufg-21"></span>

<ol class="al">

<li>

Compute $\mathbf{C}\mathbf{D}$ and $\mathbf{D}\mathbf{C}$ for $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ and $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$.

</li>

<li>

Let $\mathbf{A}\in\mathbb{R}^{2\times3}$, $\mathbf{B}\in\mathbb{R}^{3\times4}$ and $\mathbf{x}\in\mathbb{R}^4$. Which of the expressions $\mathbf{A}\mathbf{B}$, $\mathbf{B}\mathbf{A}$, $\mathbf{A}\mathbf{B}\mathbf{x}$, $\mathbf{B}\mathbf{x}\mathbf{A}$ are defined, and what is the size of the result?

</li>

<li>

Compute the outer product $(1,\,-1)^{\top}(2,\,0,\,3)$ and check that every row is a multiple of $(2,\,0,\,3)$.

</li>

</ol>

:::loesung
(a) $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot1\\3\cdot0+4\cdot1&3\cdot1+4\cdot1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$ and $\mathbf{D}\mathbf{C}=\bigl(\begin{smallmatrix}0+3&0+4\\1+3&2+4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$. The two are different.

(b) $\mathbf{A}\mathbf{B}$: $(2\times3)\cdot(3\times4)$ fits, size $2\times4$. $\mathbf{B}\mathbf{A}$: $(3\times4)\cdot(2\times3)$, inner sizes $4\ne2$, not defined. $\mathbf{A}\mathbf{B}\mathbf{x}$: $(2\times4)\cdot(4\times1)$ fits, a vector in $\mathbb{R}^2$. $\mathbf{B}\mathbf{x}\mathbf{A}$: $\mathbf{B}\mathbf{x}$ has size $3\times1$, and $(3\times1)\cdot(2\times3)$ does not fit, inner sizes $1\ne2$; not defined.

(c) $(1,\,-1)^{\top}(2,\,0,\,3)=\bigl(\begin{smallmatrix}2&0&3\\-2&0&-3\end{smallmatrix}\bigr)$. The first row is $1\cdot(2,0,3)$, the second $-1\cdot(2,0,3)$.
:::
:::

:::aufgabe Exercise 22 ★★ Two rotations
<span class="anker" id="aufg-22"></span>

<ol class="al">

<li>

Compute $\mathbf R_\alpha\mathbf R_\beta$ with [(8.3)](lineare-abbildungen.html#gl-8-3). Which rotation is this? Which two formulas of trigonometry do you get along the way?

</li>

<li>

Compute $\mathbf R_{90^\circ}^2=\mathbf R_{90^\circ}\mathbf R_{90^\circ}$ and $\mathbf R_{90^\circ}^4$ and interpret the results geometrically.

</li>

<li>

Is $\mathbf R_\alpha\mathbf R_\beta=\mathbf R_\beta\mathbf R_\alpha$? Why does this not contradict the rule that matrices do not commute?

</li>

</ol>

:::loesung
(a) Multiplied out,

$$\mathbf R_\alpha\mathbf R_\beta=\begin{pmatrix}\cos\alpha\cos\beta-\sin\alpha\sin\beta&-(\cos\alpha\sin\beta+\sin\alpha\cos\beta)\\\sin\alpha\cos\beta+\cos\alpha\sin\beta&\cos\alpha\cos\beta-\sin\alpha\sin\beta\end{pmatrix}.$$

Geometrically, this is “first rotate by $\beta$, then by $\alpha$”, that is, the rotation by $\alpha+\beta$, whose matrix by [(8.3)](lineare-abbildungen.html#gl-8-3) is $\mathbf R_{\alpha+\beta}$. Comparing the entries gives the addition formulas $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$ and $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$. The matrix product delivers them without your having to know them by heart.

(b) $\mathbf R_{90^\circ}^2=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-1&0\\0&-1\end{smallmatrix}\bigr)=-\mathbf{I}$: twice $90^\circ$ is a half turn, and every point goes to its mirror image through the origin. $\mathbf R_{90^\circ}^4=(-\mathbf{I})(-\mathbf{I})=\mathbf{I}$: four quarter turns are a full turn.

(c) Yes: both products are $\mathbf R_{\alpha+\beta}=\mathbf R_{\beta+\alpha}$, because rotations of the plane about the same point can be carried out in any order. “Not commutative” only means that $\mathbf{A}\mathbf{B}=\mathbf{B}\mathbf{A}$ does *not always* hold. For certain pairs, for example two rotations of the plane or two diagonal matrices, it can hold nevertheless.
:::
:::

:::aufgabe Exercise 23 ★★ The right parentheses
<span class="anker" id="aufg-23"></span>

Let $\mathbf{A}\in\mathbb{R}^{100\times1000}$, $\mathbf{B}\in\mathbb{R}^{1000\times1000}$ and $\mathbf{x}\in\mathbb{R}^{1000}$. Estimate the number of basic arithmetic operations for $(\mathbf{A}\mathbf{B})\mathbf{x}$ and for $\mathbf{A}(\mathbf{B}\mathbf{x})$. Count about $2mnk$ for a product of an $m\times n$ matrix with an $n\times k$ matrix.

:::loesung
$(\mathbf{A}\mathbf{B})\mathbf{x}$: the product $\mathbf{A}\mathbf{B}$ of a $100\times1000$ matrix with a $1000\times1000$ matrix costs about $2\cdot100\cdot1000\cdot1000=2\cdot10^8$, and then $(\mathbf{A}\mathbf{B})\mathbf{x}$ costs about another $2\cdot100\cdot1000=2\cdot10^5$; about $200.2$ million in total. $\mathbf{A}(\mathbf{B}\mathbf{x})$: $\mathbf{B}\mathbf{x}$ costs about $2\cdot1000\cdot1000=2\cdot10^6$, and then $\mathbf{A}(\mathbf{B}\mathbf{x})$ about $2\cdot10^5$; about $2.2$ million in total. The second way is about $91$ times faster, with the same result.
:::
:::
