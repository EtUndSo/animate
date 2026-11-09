---
title: Identity matrix and inverse
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15211200
summary: Some linear maps can be undone, others cannot.
tags: identity matrix, invertible, inverse, singular
lang: en
---

<span class="anker" id="stufe-11"></span>

:::zweck
Some linear maps can be undone, others cannot. This section introduces the matrix that changes nothing and the inverse matrix that reverses a map, and it clarifies when the inverse exists.
:::

### The identity matrix

<span class="anker" id="stufe-11-1"></span>

Among all linear maps there is one that does nothing at all: it maps every vector to itself. By [(8.2)](lineare-abbildungen.html#gl-8-2), its columns are the images of the unit vectors, that is, the unit vectors themselves.

:::definition Definition 11.1 (Identity matrix)
<span class="anker" id="satz-11-1"></span>

The __identity matrix__ $\mathbf{I}_n\in\mathbb{R}^{n\times n}$ is the diagonal matrix with all ones on the diagonal. Its columns are $\mathbf{e}_1,\dots,\mathbf{e}_n$.
:::

If the size is clear, you write $\mathbf{I}$ for short. For every vector $\mathbf{x}\in\mathbb{R}^n$, $\mathbf{I}\mathbf{x}=\mathbf{x}$, and for every matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$, $\mathbf{A}\mathbf{I}_n=\mathbf{A}$ and $\mathbf{I}_m\mathbf{A}=\mathbf{A}$. In the matrix product, the identity matrix plays the role of the number $1$.

::::beispiel [Worked example]
$$\mathbf{I}_3=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\qquad \mathbf{I}_3\begin{pmatrix}60\\2\\3\end{pmatrix}=\begin{pmatrix}60\\2\\3\end{pmatrix}.$$
::::

⁠**In short:** The identity matrix has ones on the diagonal and zeros everywhere else; as a map, it leaves every vector unchanged.

### The inverse matrix

<span class="anker" id="stufe-11-2"></span>

A rotation by $90^\circ$ is undone by rotating back by $90^\circ$. A stretch to twice the size is undone by compressing to half the size. In both cases there is a second map that cancels the first: applied one after the other, the two together do nothing.

:::definition Definition 11.2 (Inverse matrix)
<span class="anker" id="satz-11-2"></span>

A square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ is called __invertible__ if there is a matrix $\mathbf{A}^{-1}\in\mathbb{R}^{n\times n}$ with

<span class="anker" id="gl-11-1"></span>
$$\mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=\mathbf{I} . \tag{11.1}$$

The matrix $\mathbf{A}^{-1}$ is called the __inverse__ of $\mathbf{A}$.
:::

There is at most one such matrix. Indeed, if $\mathbf{B}$ and $\mathbf{C}$ are both inverse to $\mathbf{A}$, then $\mathbf{B}=\mathbf{B}\mathbf{I}=\mathbf{B}(\mathbf{A}\mathbf{C})=(\mathbf{B}\mathbf{A})\mathbf{C}=\mathbf{I}\mathbf{C}=\mathbf{C}$. That is why you may speak of *the* inverse. If you know it, you can calculate back from any result $\mathbf{y}=\mathbf{A}\mathbf{x}$: $\mathbf{A}^{-1}\mathbf{y}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{x}$.

::::beispiel [Worked example]
$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\begin{pmatrix}2-1&-2+2\\1-1&-1+2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix},$$

and likewise in the other order, so $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$. The stretch has the inverse $\operatorname{diag}(2,\,0.5)^{-1}=\operatorname{diag}(0.5,\,2)$, and the rotation by $90^\circ$ has the rotation by $-90^\circ$, $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$.
::::

⁠**In short:** The inverse $\mathbf{A}^{-1}$ undoes the map $\mathbf{A}$: $\mathbf{A}^{-1}\mathbf{A}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$.

:::hintergrund The inverse of a diagonal matrix
A diagonal matrix $\operatorname{diag}(\mathbf{v})$ multiplies each component by its own factor $v_j$. You undo this by dividing each component by its factor: $\operatorname{diag}(\mathbf{v})^{-1}=\operatorname{diag}(1/v_1,\dots,1/v_n)$. This works exactly when no factor is zero. A factor $v_j=0$ wipes out component $j$, and no calculation can bring back what has been wiped out.
:::

### The inverse of a $2\times2$ matrix

<span class="anker" id="stufe-11-3"></span>

For $2\times2$ matrices there is a simple formula. You swap the two diagonal entries, put a minus sign in front of the other two and divide by a number formed from all four entries.

:::satz Theorem 11.3 (Inverse of a $2\times2$ matrix)
<span class="anker" id="satz-11-3"></span>

The matrix $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ is invertible if and only if $ad-bc\ne0$, and then

<span class="anker" id="gl-11-2"></span>
$$\mathbf{A}^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}. \tag{11.2}$$
:::

:::herleitung Inverse of a $2\times2$ matrix
Multiplying out gives

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}=\begin{pmatrix}ad-bc&-ab+ba\\cd-dc&-cb+da\end{pmatrix}=(ad-bc)\,\mathbf{I} ,$$

and likewise in the other order. If $ad-bc\ne0$, you divide by this number and obtain [(11.1)](#gl-11-1). If $ad-bc=0$, then $\mathbf{A}$ sends the vector $(d,\,-c)^{\top}$ to $(ad-bc,\ cd-dc)^{\top}=\mathbf{0}$, and likewise $(b,\,-a)^{\top}$ to $\mathbf{0}$. At least one of the two is not the zero vector, unless all four entries are zero, and then $\mathbf{A}$ is the zero matrix anyway. But a matrix that maps a vector $\mathbf{x}\ne\mathbf{0}$ to $\mathbf{0}$ has no inverse: if it had one, then $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$.
:::

::::beispiel [Worked example]
For $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$, $ad-bc=2-1=1$, so the inverse is $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$, as above. For $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$, $ad-bc=5$ and the inverse is $\tfrac15\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$.
::::

⁠**In short:** A $2\times2$ matrix is invertible exactly when $ad-bc\ne0$; the inverse is $\frac{1}{ad-bc}\bigl(\begin{smallmatrix}d&-b\\-c&a\end{smallmatrix}\bigr)$.

### Rules of calculation for inverses

<span class="anker" id="stufe-11-4"></span>

If you apply two maps one after the other and want to undo the result, you must cancel the second one first. That is why the order is reversed when you invert a product.

:::satz Theorem 11.4 (Rules of calculation for inverses)
<span class="anker" id="satz-11-4"></span>

If $\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ are invertible and $c\ne0$, then $\mathbf{A}\mathbf{B}$, $\mathbf{A}^{\top}$, $\mathbf{A}^{-1}$ and $c\,\mathbf{A}$ are also invertible, and

$$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1},\qquad(\mathbf{A}^{\top})^{-1}=(\mathbf{A}^{-1})^{\top},\qquad(\mathbf{A}^{-1})^{-1}=\mathbf{A},\qquad(c\,\mathbf{A})^{-1}=\tfrac1c\,\mathbf{A}^{-1}.$$
:::

:::herleitung Rules of calculation for inverses
In each case you check that the product with the candidate gives the identity matrix. For the product: $(\mathbf{A}\mathbf{B})(\mathbf{B}^{-1}\mathbf{A}^{-1})=\mathbf{A}(\mathbf{B}\mathbf{B}^{-1})\mathbf{A}^{-1}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$, and likewise $(\mathbf{B}^{-1}\mathbf{A}^{-1})(\mathbf{A}\mathbf{B})=\mathbf{I}$. For the transpose: $\mathbf{A}^{\top}(\mathbf{A}^{-1})^{\top}=(\mathbf{A}^{-1}\mathbf{A})^{\top}=\mathbf{I}^{\top}=\mathbf{I}$, and likewise in the other order. The last two rules follow directly from [(11.1)](#gl-11-1).
:::

One rule you might wish for does not hold: $(\mathbf{A}+\mathbf{B})^{-1}$ is in general not $\mathbf{A}^{-1}+\mathbf{B}^{-1}$. Even for numbers, $\frac{1}{2+4}=\frac16$, but $\frac12+\frac14=\frac34$.

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ and $\mathbf{B}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$, $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$ with $ad-bc=21-16=5$, so $(\mathbf{A}\mathbf{B})^{-1}=\tfrac15\bigl(\begin{smallmatrix}3&-4\\-4&7\end{smallmatrix}\bigr)$. The same result comes from

$$\mathbf{B}^{-1}\mathbf{A}^{-1}=\tfrac15\begin{pmatrix}2&-1\\-1&3\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\tfrac15\begin{pmatrix}3&-4\\-4&7\end{pmatrix}.$$
::::

⁠**In short:** The inverse of a product is the product of the inverses in reverse order, $(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$.

:::hintergrund A picture for the reversed order
If you put on a sweater first and then a jacket in the morning, in the evening you take off the jacket first and then the sweater. Undoing runs backward through the steps. The map $\mathbf{A}\mathbf{B}$ is “first $\mathbf{B}$, then $\mathbf{A}$”; to cancel it, you must first cancel $\mathbf{A}$ and then $\mathbf{B}$, that is, apply first $\mathbf{A}^{-1}$ and then $\mathbf{B}^{-1}$. Written as a matrix, with the step carried out first on the right, this is $\mathbf{B}^{-1}\mathbf{A}^{-1}$. The picture holds only as far as the order is concerned; it does not explain why an inverse exists.
:::

### When there is no inverse

<span class="anker" id="stufe-11-5"></span>

The matrix $\operatorname{diag}(1,\,0)$ flattens the plane onto the $x_1$-axis (Fig. [32](lineare-abbildungen.html#abb-32)). The points $(1,\,5)^{\top}$ and $(1,\,-2)^{\top}$ both land at $(1,\,0)^{\top}$. If you see only the result $(1,\,0)^{\top}$, you cannot know which point it came from. The second component is lost, and no calculation brings it back.

:::satz Theorem 11.5 (No inverse)
<span class="anker" id="satz-11-5"></span>

If there is a vector $\mathbf{x}\ne\mathbf{0}$ with $\mathbf{A}\mathbf{x}=\mathbf{0}$, then $\mathbf{A}$ is not invertible.
:::

:::beweis No inverse
If there were an inverse, then $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$, contradicting $\mathbf{x}\ne\mathbf{0}$.
:::

Intuitively: with $\mathbf{A}\mathbf{x}=\mathbf{0}$, for every $\mathbf{u}$ the two different vectors $\mathbf{u}$ and $\mathbf{u}+\mathbf{x}$ land at the same place, because $\mathbf{A}(\mathbf{u}+\mathbf{x})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{x}=\mathbf{A}\mathbf{u}$. Two inputs with the same output cannot be told apart. A square matrix that is not invertible is called __singular__.

::::beispiel [Worked example]
For $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, $ad-bc=4-4=0$. Indeed, $\mathbf{x}=(2,\,-1)^{\top}$ is mapped to $(2-2,\ 4-4)^{\top}=\mathbf{0}$, and the different vectors $(1,\,1)^{\top}$ and $(3,\,0)^{\top}$ both land at $(3,\,6)^{\top}$.
::::

For data this means: a calculation that, for instance, combines the numbers of bedrooms and living rooms into just the total number of rooms can no longer separate the two numbers. For $2\times2$ matrices this is exactly the case $ad-bc=0$ from Subsection [11.3](#stufe-11-3).

⁠**In short:** If a matrix maps a vector $\mathbf{x}\ne\mathbf{0}$ to $\mathbf{0}$, it loses information and has no inverse; it is then called singular.

:::aufgabe Exercise 26 ★ Computing inverses
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

Compute the inverses of $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$ and $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$, and check each result.

</li>

<li>

For which number $t$ is $\bigl(\begin{smallmatrix}2&t\\4&6\end{smallmatrix}\bigr)$ not invertible? For this case, give a vector $\mathbf{x}\ne\mathbf{0}$ with $\mathbf{A}\mathbf{x}=\mathbf{0}$.

</li>

<li>

Give the inverse of $\operatorname{diag}(4,\,-1,\,0.5)$.

</li>

</ol>

:::loesung
(a) For $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$, $ad-bc=4-3=1$, and the inverse is $\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)$. Check: $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4-3&-12+12\\1-1&-3+4\end{smallmatrix}\bigr)=\mathbf{I}$. For $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$, $ad-bc=4-6=-2$, and the inverse is $-\tfrac12\bigl(\begin{smallmatrix}4&-2\\-3&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1\\1.5&-0.5\end{smallmatrix}\bigr)$. Check: $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}-2&1\\1.5&-0.5\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2+3&1-1\\-6+6&3-2\end{smallmatrix}\bigr)=\mathbf{I}$.

(b) $ad-bc=12-4t=0$ for $t=3$. Then the matrix is $\bigl(\begin{smallmatrix}2&3\\4&6\end{smallmatrix}\bigr)$; its second row is twice the first. The vector $(3,\,-2)^{\top}$ is mapped to $(6-6,\ 12-12)^{\top}=\mathbf{0}$.

(c) $\operatorname{diag}(4,\,-1,\,0.5)^{-1}=\operatorname{diag}(0.25,\,-1,\,2)$: each diagonal entry is replaced by its reciprocal.
:::
:::

:::aufgabe Exercise 27 ★★ Arguing with inverses
<span class="anker" id="aufg-27"></span>

<ol class="al">

<li>

Check $(\mathbf{C}^{\top})^{-1}=(\mathbf{C}^{-1})^{\top}$ for $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$.

</li>

<li>

Let $\mathbf{A}$ be invertible and $\mathbf{A}\mathbf{B}=\mathbf 0$. Show that then $\mathbf{B}=\mathbf 0$.

</li>

<li>

For numbers, $ab=0$ implies that $a=0$ or $b=0$. Show with $\mathbf{A}=\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$ that this does not hold for matrices. Why does this not contradict (b)?

</li>

</ol>

:::loesung
(a) $\mathbf{C}^{-1}=\bigl(\begin{smallmatrix}-2&1\\1.5&-0.5\end{smallmatrix}\bigr)$ from the previous exercise, so $(\mathbf{C}^{-1})^{\top}=\bigl(\begin{smallmatrix}-2&1.5\\1&-0.5\end{smallmatrix}\bigr)$. On the other hand, $\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)$ with $ad-bc=-2$, so $(\mathbf{C}^{\top})^{-1}=-\tfrac12\bigl(\begin{smallmatrix}4&-3\\-2&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1.5\\1&-0.5\end{smallmatrix}\bigr)$. The two agree.

(b) Multiply $\mathbf{A}\mathbf{B}=\mathbf 0$ from the left by $\mathbf{A}^{-1}$: $\mathbf{B}=\mathbf{I}\mathbf{B}=\mathbf{A}^{-1}\mathbf{A}\mathbf{B}=\mathbf{A}^{-1}\mathbf 0=\mathbf 0$.

(c) $\mathbf{A}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}0\cdot0+1\cdot0&0\cdot1+1\cdot0\\0&0\end{smallmatrix}\bigr)=\mathbf 0$, even though $\mathbf{A}\ne\mathbf 0$. Geometrically, $\mathbf{A}$ sends the vector $\mathbf{e}_2$ to $\mathbf{e}_1$ and $\mathbf{e}_1$ to $\mathbf{0}$; applied twice, everything ends up at the zero vector. This does not contradict (b), because $\mathbf{A}$ is not invertible: $ad-bc=0$. The conclusion in (b) needs the inverse.
:::
:::
