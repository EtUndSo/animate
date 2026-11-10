---
title: Approximation by matrices of low rank
pfad: Computer Science / Machine Learning / Mathematical Foundations / Projection, Eigenvalues and Decompositions
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Chapter 2: Projection, Eigenvalues and Decompositions
nachschlagen: ja
order: 15221100
summary: The singular value decomposition orders the building blocks of a matrix by their size.
tags: Frobenius norm, truncated singular value decomposition
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
The singular value decomposition orders the building blocks of a matrix by their size. If you leave out the small ones, a matrix of lower rank remains that can be stored with far fewer numbers. This section measures how far this approximation is from the original matrix and proves that no other matrix of the same rank is closer.
:::

### The Frobenius norm

<span class="anker" id="stufe-10-1"></span>

To say how close two matrices are to each other, you need a measure of size for their difference. The spectral norm is one such measure; it measures the largest lengthening. A second one is even more obvious: you read the matrix out row by row into one long vector, like an image in [Chapter 1, Section 6.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/matrizen-und-die-datenmatrix.html#stufe-6-1), and take the Euclidean norm of that vector.

:::definition Definition 10.1 (Frobenius norm)
<span class="anker" id="satz-10-1"></span>

The __Frobenius norm__ of $\mathbf{A}\in\mathbb{R}^{m\times n}$ is

$$\lVert\mathbf{A}\rVert_F=\sqrt{\sum_{i=1}^m\sum_{j=1}^na_{ij}^2} .$$
:::

:::satz Theorem 10.2 (Frobenius norm and singular values)
<span class="anker" id="satz-10-2"></span>

For every matrix $\mathbf{A}$ of rank $r$,

<span class="anker" id="gl-10-1"></span>
$$\lVert\mathbf{A}\rVert_F^2=\operatorname{tr}(\mathbf{A}^{\top}\mathbf{A})=d_1^2+d_2^2+\dots+d_r^2 . \tag{10.1}$$
:::

:::beweis Frobenius norm
Diagonal entry $j$ of $\mathbf{A}^{\top}\mathbf{A}$ is $\mathbf{a}_j^{\top}\mathbf{a}_j=\sum_ia_{ij}^2$, the squared length of column $j$. The trace, the sum of these entries, is therefore the sum of all squared entries of $\mathbf{A}$. By [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5), the trace is also the sum of the eigenvalues of $\mathbf{A}^{\top}\mathbf{A}$, and these are the $d_j^2$.
:::

Two consequences. Because $d_1^2\le\sum_jd_j^2$, we have $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F$. And an orthogonal matrix does not change the Frobenius norm: $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$, so $\mathbf{Q}\mathbf{A}$ and $\mathbf{A}$ have the same singular values.

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, we have $\lVert\mathbf{A}\rVert_F^2=4+9+0+4=17=4^2+1^2$ (Fig. [24](#abb-24)), so $\lVert\mathbf{A}\rVert_F=\sqrt{17}\approx4.12$, slightly more than $\lVert\mathbf{A}\rVert_2=4$.

:::abbildung ml/k2rfrobenius 24
The squared Frobenius norm of $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$: the sum of all squared entries, equal to the sum of the squared singular values.
:::
::::

⁠**In short:** The Frobenius norm is the Euclidean norm of all entries; its square is the sum of the squared singular values.

### The truncated decomposition

<span class="anker" id="stufe-10-2"></span>

If you break off the sum [(9.4)](die-singularwertzerlegung.html#gl-9-4) after the $k$ largest building blocks, you get an approximation.

:::definition Definition 10.3 (Truncated singular value decomposition)
<span class="anker" id="satz-10-3"></span>

For $k<r$,

<span class="anker" id="gl-10-2"></span>
$$\mathbf{A}_k=\sum_{j=1}^kd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} \tag{10.2}$$

is called the __truncated singular value decomposition__ of $\mathbf{A}$ with $k$ building blocks.
:::

$\mathbf{A}_k$ has rank $k$, because $\mathbf{A}_k\mathbf{v}_j=d_j\mathbf{u}_j$ for $j\le k$ and $\mathbf{A}_k\mathbf{v}_j=\mathbf{0}$ for $j>k$; so the images span a space of dimension $k$. The error is the rest of the sum:

$$\mathbf{A}-\mathbf{A}_k=\sum_{j=k+1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} .$$

Its Gram matrix is $\sum_{j>k}d_j^2\mathbf{v}_j\mathbf{v}_j^{\top}$, because the cross terms drop out due to $\mathbf{u}_i^{\top}\mathbf{u}_j=0$. It has the eigenvalues $d_{k+1}^2,\dots,d_r^2$ and zero otherwise. So the error has the singular values $d_{k+1},\dots,d_r$, and by [(9.5)](die-singularwertzerlegung.html#gl-9-5) and [(10.1)](#gl-10-1),

<span class="anker" id="gl-10-3"></span>
$$\lVert\mathbf{A}-\mathbf{A}_k\rVert_2=d_{k+1},\qquad \lVert\mathbf{A}-\mathbf{A}_k\rVert_F=\sqrt{d_{k+1}^2+\dots+d_r^2} . \tag{10.3}$$

For storage, $\mathbf{A}_k$ needs only the $k$ vectors $\mathbf{u}_j$ with $m$ entries each, the $k$ vectors $\mathbf{v}_j$ with $n$ entries each and the $k$ numbers $d_j$, a total of $k(m+n+1)$ numbers instead of $mn$.

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ and $k=1$,

$$\mathbf{A}_1=4\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1.6&3.2\\0.8&1.6\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\mathbf{u}_2\mathbf{v}_2^{\top}=\begin{pmatrix}0.4&-0.2\\-0.8&0.4\end{pmatrix}.$$

The Frobenius norm of the error is $\sqrt{0.16+0.04+0.64+0.16}=1=d_2$ (Fig. [25](#abb-25)), and so is its spectral norm.

:::abbildung ml/k2rfehler 25
The error of the best approximation of rank $1$ in the Frobenius norm, squared, with $0.4=\tfrac25$, $0.2=\tfrac15$ and $0.8=\tfrac45$: it equals $d_2^2=1$.
:::
::::

⁠**In short:** $\mathbf{A}_k$ keeps the $k$ largest building blocks; the error has the remaining singular values, and its spectral norm is $d_{k+1}$.

### The best approximation

<span class="anker" id="stufe-10-3"></span>

There are many matrices of rank $k$. Is the truncated decomposition the best among them? Yes, in both norms.

:::satz Theorem 10.4 (Eckart–Young theorem)
<span class="anker" id="satz-10-4"></span>

Let $\mathbf{A}$ have rank $r$, and let $k<r$. For every matrix $\mathbf{B}$ of the same shape with $\operatorname{rank}\mathbf{B}\le k$,

<span class="anker" id="gl-10-4"></span>
$$\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_2,\qquad \lVert\mathbf{A}-\mathbf{B}\rVert_F\ge\sqrt{d_{k+1}^2+\dots+d_r^2}=\lVert\mathbf{A}-\mathbf{A}_k\rVert_F . \tag{10.4}$$

So among all matrices of rank at most $k$, the matrix $\mathbf{A}_k$ is closest to $\mathbf{A}$.
:::

:::beweis Spectral norm
By the rank–nullity theorem, the null space of $\mathbf{B}$ has dimension $n-\operatorname{rank}\mathbf{B}\ge n-k$. Choose $n-k$ linearly independent vectors $\mathbf{b}_1,\dots,\mathbf{b}_{n-k}$ in the null space and add $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$. These are $n+1$ vectors in $\mathbb{R}^n$, and by [Chapter 1, Section 13.4](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-4), they are linearly dependent, because a matrix with $n$ rows has rank at most $n$. So there are numbers, not all zero, with $\sum_l\alpha_l\mathbf{b}_l=\sum_j\beta_j\mathbf{v}_j$. This vector $\mathbf{z}$ is not zero, because otherwise, by the independence of both lists, all numbers would be zero. It lies in the null space of $\mathbf{B}$ and in the span of $\mathbf{v}_1,\dots,\mathbf{v}_{k+1}$. Normalize it to length $1$. Then $(\mathbf{A}-\mathbf{B})\mathbf{z}=\mathbf{A}\mathbf{z}$, and with $\mathbf{z}=\sum_{j\le k+1}c_j\mathbf{v}_j$, $\sum_jc_j^2=1$:

$$\lVert(\mathbf{A}-\mathbf{B})\mathbf{z}\rVert^2=\lVert\mathbf{A}\mathbf{z}\rVert^2=\sum_{j=1}^{k+1}d_j^2c_j^2\ge d_{k+1}^2\sum_{j=1}^{k+1}c_j^2=d_{k+1}^2 .$$

So $\mathbf{A}-\mathbf{B}$ lengthens the unit vector $\mathbf{z}$ by at least the factor $d_{k+1}$, and $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_{k+1}$.
:::

The proof shows the reason: a matrix of rank $k$ must map a whole set of directions to zero, namely its null space. This null space inevitably meets the space of the $k+1$ most strongly stretched directions of $\mathbf{A}$, and there $\mathbf{B}$ makes an error of at least $d_{k+1}$.

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$, the matrix $\mathbf{A}_1$ is the best matrix of rank $1$, with the error $1$ in both norms. Another matrix of rank $1$, say $\mathbf{B}=\bigl(\begin{smallmatrix}2&3\\0&0\end{smallmatrix}\bigr)$, which simply strikes out the second row, has the error $\mathbf{A}-\mathbf{B}=\bigl(\begin{smallmatrix}0&0\\0&2\end{smallmatrix}\bigr)$ with norm $2$.
::::

⁠**In short:** The truncated decomposition $\mathbf{A}_k$ is the best approximation of rank $k$, in the spectral norm as well as in the Frobenius norm.

:::hintergrund Why the statement also holds for the Frobenius norm
The proof for the Frobenius norm views the rows $\mathbf{a}^{(1)\top},\dots,\mathbf{a}^{(m)\top}$ of $\mathbf{A}$ as $m$ points in $\mathbb{R}^n$, like the examples of a data matrix. If $\mathbf{B}$ has rank at most $k$, its rows lie in a subspace $\mathcal S$ of dimension $k$: the column space of $\mathbf{B}^{\top}$, extended to dimension $k$. For a fixed subspace $\mathcal S$ with the projection matrix $\mathbf{P}$, by Section [4](projektion-auf-einen-unterraum.html#stufe-4) the projection $\mathbf{P}\mathbf{a}^{(i)}$ of each row is the closest point in $\mathcal S$. With an orthonormal basis $\mathbf{w}_1,\dots,\mathbf{w}_k$ of $\mathcal S$, the Pythagorean theorem gives

$$\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge\sum_i\bigl\lVert\mathbf{a}^{(i)}-\mathbf{P}\mathbf{a}^{(i)}\bigr\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_i\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\lVert\mathbf{A}\rVert_F^2-\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2 ,$$

because $\lVert\mathbf{P}\mathbf{a}^{(i)}\rVert^2=\sum_l(\mathbf{w}_l^{\top}\mathbf{a}^{(i)})^2$, and $\mathbf{w}_l^{\top}\mathbf{a}^{(i)}$ is entry $i$ of $\mathbf{A}\mathbf{w}_l$. It remains to show that $\sum_l\lVert\mathbf{A}\mathbf{w}_l\rVert^2\le d_1^2+\dots+d_k^2$. In the coordinates of the $\mathbf{v}_j$,

$$\sum_{l=1}^k\lVert\mathbf{A}\mathbf{w}_l\rVert^2=\sum_{l=1}^k\sum_jd_j^2(\mathbf{v}_j^{\top}\mathbf{w}_l)^2=\sum_jd_j^2\,g_j\qquad\text{with}\qquad g_j=\sum_{l=1}^k(\mathbf{v}_j^{\top}\mathbf{w}_l)^2 .$$

Each $g_j$ is the squared length of the projection of $\mathbf{v}_j$ onto $\mathcal S$, so $0\le g_j\le1$, and the sum of all $g_j$ is $\sum_l\lVert\mathbf{w}_l\rVert^2=k$. A sum $\sum_jd_j^2g_j$ with such weights is largest when the $k$ largest $d_j^2$ get the full weight $1$; that gives $d_1^2+\dots+d_k^2$. Together with [(10.1)](#gl-10-1), it follows that $\lVert\mathbf{A}-\mathbf{B}\rVert_F^2\ge d_{k+1}^2+\dots+d_r^2$. Along the way, the calculation shows: the subspace to which the rows of $\mathbf{A}$ are closest is the span of $\mathbf{v}_1,\dots,\mathbf{v}_k$.
:::

### An image with few numbers

<span class="anker" id="stufe-10-4"></span>

A grayscale image is a matrix. By the Eckart–Young theorem, $\mathbf{A}_k$ is the best approximation with $k$ building blocks, and [(10.3)](#gl-10-3) tells how much is lost. The fraction

$$\frac{d_1^2+\dots+d_k^2}{d_1^2+\dots+d_r^2}$$

indicates which part of the sum of all squared brightness values is preserved.

::::beispiel [Worked example]
The cross from [Chapter 1, Section 6.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/matrizen-und-die-datenmatrix.html#stufe-6-1), is

$$\mathbf{C}=\begin{pmatrix}0&1&0\\1&1&1\\0&1&0\end{pmatrix}.$$

It is symmetric. Its characteristic polynomial is $-\lambda^3+\lambda^2+2\lambda=-\lambda(\lambda-2)(\lambda+1)$; the eigenvalues are $2$, $-1$ and $0$, with the eigenvectors $(1,\,2,\,1)^{\top}$, $(1,\,-1,\,1)^{\top}$ and $(1,\,0,\,-1)^{\top}$. By Section [9.7](die-singularwertzerlegung.html#stufe-9-7), the singular values are $2$, $1$ and $0$; the rank is $2$. With $\mathbf{q}_1=(1,\,2,\,1)^{\top}/\sqrt6$, the best approximation of rank $1$ is

$$\mathbf{C}_1=2\,\mathbf{q}_1\mathbf{q}_1^{\top}=\frac13\begin{pmatrix}1&2&1\\2&4&2\\1&2&1\end{pmatrix},\qquad \mathbf{C}-\mathbf{C}_1=\frac13\begin{pmatrix}-1&1&-1\\1&-1&1\\-1&1&-1\end{pmatrix}$$

(Fig. [26](#abb-26)). The error has size $1$ in both norms. $\mathbf{C}_1$ keeps $4/5=80\,\%$ of the sum $\lVert\mathbf{C}\rVert_F^2=5$. Every row of $\mathbf{C}_1$ is a multiple of the same row $(1,\,2,\,1)$: an image of rank $1$ is a brightness profile of the columns times a brightness profile of the rows, here a blurred spot with the brightest point in the middle. It takes $1\cdot(3+3+1)=7$ numbers to store instead of $9$.

:::abbildung ml/k2bild 26
The cross $\mathbf{C}$ of $3\times3$ pixels (left, $0$ black, $1$ white), its best approximation $\mathbf{C}_1$ of rank $1$ (middle; the value $\tfrac43$ is brighter than white and is shown as white) and the error $\mathbf{C}-\mathbf{C}_1$ (right, red positive, blue negative). The error is itself a matrix of rank $1$, the building block for the singular value $1$.
:::
::::

For a cross of $3\times3$ pixels this saves little. For large images the difference is considerable: an image of $1000\times1000$ pixels has $10^6$ entries; the approximation with $k=50$ building blocks needs $50\cdot(1000+1000+1)=100\,050$ numbers, about $10\,\%$. Whether the approximation looks good depends on how quickly the singular values fall off. In many photos, neighboring rows are very similar; the rows then lie close to a subspace of small dimension, and a few large singular values carry almost the entire sum $\sum_jd_j^2$.

⁠**In short:** An image of rank $k$ needs $k(m+n+1)$ numbers; the truncated decomposition is the best such image, and $\sum_{j\le k}d_j^2/\sum_jd_j^2$ tells how much is preserved.

:::aufgabe Exercise 30 ★ Norms of a matrix
<span class="anker" id="aufg-30"></span>

<ol class="al">

<li>

Compute $\lVert\mathbf{A}\rVert_F$ and $\lVert\mathbf{A}\rVert_2$ for $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$ from Exercise [27](die-singularwertzerlegung.html#aufg-27) and check [(10.1)](#gl-10-1).

</li>

<li>

What is the Frobenius norm of an orthogonal $n\times n$ matrix?

</li>

<li>

Show $\lVert\mathbf{A}\rVert_2\le\lVert\mathbf{A}\rVert_F\le\sqrt r\,\lVert\mathbf{A}\rVert_2$. When does equality hold on the right?

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{A}\rVert_F^2=9+0+16+25=50=45+5=d_1^2+d_2^2$, so $\lVert\mathbf{A}\rVert_F=\sqrt{50}\approx7.07$, and $\lVert\mathbf{A}\rVert_2=d_1=3\sqrt5\approx6.71$.

(b) All singular values of an orthogonal matrix are $1$, so $\lVert\mathbf{Q}\rVert_F^2=n$ and $\lVert\mathbf{Q}\rVert_F=\sqrt n$. This can also be seen directly: each of the $n$ columns has the squared length $1$.

(c) We have $\lVert\mathbf{A}\rVert_2^2=d_1^2\le d_1^2+\dots+d_r^2=\lVert\mathbf{A}\rVert_F^2$, and each of the $r$ terms is at most $d_1^2$, so $\lVert\mathbf{A}\rVert_F^2\le r\,d_1^2$. Taking square roots gives both inequalities. Equality holds on the right if and only if all positive singular values are equal to $d_1$, as for an orthogonal matrix.
:::
:::

:::aufgabe Exercise 31 ★★ The best matrix of rank 1
<span class="anker" id="aufg-31"></span>

Let $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$ be the matrix from Exercise [28](die-singularwertzerlegung.html#aufg-28).

<ol class="al">

<li>

Compute $\mathbf{A}_1$ and the error $\mathbf{A}-\mathbf{A}_1$ in both norms.

</li>

<li>

The matrix $\mathbf{B}$ of all ones also has rank $1$. Compute $\lVert\mathbf{A}-\mathbf{B}\rVert_F$ and $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ and compare with (a).

</li>

<li>

What fraction of the sum of the squared entries is preserved in $\mathbf{A}_1$?

</li>

</ol>

:::loesung
(a) From Exercise [28](die-singularwertzerlegung.html#aufg-28): $d_1=2$, $\mathbf{u}_1=(1,\,1,\,0)^{\top}/\sqrt2$, $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$. So

$$\mathbf{A}_1=2\,\mathbf{u}_1\mathbf{v}_1^{\top}=\begin{pmatrix}1&1\\1&1\\0&0\end{pmatrix},\qquad \mathbf{A}-\mathbf{A}_1=\begin{pmatrix}0&0\\0&0\\1&-1\end{pmatrix}.$$

The error has the Frobenius norm $\sqrt{1+1}=\sqrt2=d_2$. It is the outer product $\mathbf{e}_3\,(1,\,-1)$, by Exercise [29](die-singularwertzerlegung.html#aufg-29) with the single singular value $1\cdot\sqrt2$; its spectral norm is $\sqrt2$ as well.

(b) $\mathbf{A}-\mathbf{B}=\Bigl(\begin{smallmatrix}0&0\\0&0\\0&-2\end{smallmatrix}\Bigr)$ has the size $2>\sqrt2$ in both norms. As the Eckart–Young theorem requires, $\mathbf{B}$ is farther from $\mathbf{A}$ than $\mathbf{A}_1$ is.

(c) $\lVert\mathbf{A}\rVert_F^2=6=4+2$, and $\mathbf{A}_1$ preserves $d_1^2/(d_1^2+d_2^2)=\tfrac46=\tfrac23\approx67\,\%$.
:::
:::

:::aufgabe Exercise 32 ★ Storage requirements
<span class="anker" id="aufg-32"></span>

A grayscale image has $600\times800$ pixels.

<ol class="al">

<li>

How many numbers does the approximation with $k=40$ building blocks need? What fraction of the original number is that?

</li>

<li>

From which $k$ on does the approximation no longer save any storage?

</li>

</ol>

:::loesung
(a) $40\cdot(600+800+1)=40\cdot1\,401=56\,040$ numbers instead of $600\cdot800=480\,000$, that is, about $11.7\,\%$.

(b) The approximation saves storage as long as $k\cdot1\,401<480\,000$, that is, for $k\le342$, because $342\cdot1\,401=479\,142$ and $343\cdot1\,401=480\,543$. From $k=343$ on, the approximation needs more numbers than the image itself. The rank is at most $600$; there are no more than $600$ building blocks anyway.
:::
:::
