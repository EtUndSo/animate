---
title: Diagonalization and the spectral theorem
pfad: Computer Science / Machine Learning / Mathematical Foundations / Projection, Eigenvalues and Decompositions
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: Chapter 2: Projection, Eigenvalues and Decompositions
nachschlagen: ja
order: 15220800
summary: If you describe a matrix in a basis of its eigenvectors, it becomes diagonal: each coordinate is only multiplied by its eigenvalue, and coupled calculations break down into separate ones.
tags: change of basis, diagonalizable, principal axes
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
If you describe a matrix in a basis of its eigenvectors, it becomes diagonal: each coordinate is only multiplied by its eigenvalue, and coupled calculations break down into separate ones. This section shows when this is possible and proves that it is always possible for symmetric matrices, even with an orthonormal basis.
:::

### Change of basis

<span class="anker" id="stufe-7-1"></span>

The same arrow has different coordinates in different bases. Likewise, the same linear map has different matrices in different coordinates. Some bases make the matrix especially simple.

Let $\mathbf s_1,\dots,\mathbf s_n$ be a basis of $\mathbb{R}^n$, and let $\mathbf{S}$ be the matrix with these columns. By [Chapter 1, Section 13.5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5), it is invertible. If $\mathbf{x}$ has the coordinates $\mathbf{c}$ in this basis, then $\mathbf{x}=\sum_ic_i\mathbf s_i=\mathbf{S}\mathbf{c}$, and conversely $\mathbf{c}=\mathbf{S}^{-1}\mathbf{x}$. If you map $\mathbf{x}$ with $\mathbf{A}$, the image $\mathbf{A}\mathbf{x}$ has the coordinates $\mathbf{S}^{-1}\mathbf{A}\mathbf{x}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}\,\mathbf{c}$. In the new coordinates, the map therefore acts through the matrix $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$: first convert to the old coordinates, then map, then convert back.

:::definition Definition 7.1 (Change of basis)
<span class="anker" id="satz-7-1"></span>

If $\mathbf{S}$ is invertible, then $\mathbf{B}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ is called the matrix of $\mathbf{A}$ in the basis of the columns of $\mathbf{S}$. The transition from $\mathbf{A}$ to $\mathbf{B}$ is called a __change of basis__.
:::

Two matrices related in this way are called similar. They describe the same map, only in different coordinates.

:::satz Theorem 7.2 (What a change of basis does not change)
<span class="anker" id="satz-7-2"></span>

$\mathbf{A}$ and $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ have the same characteristic polynomial, and hence the same eigenvalues, the same trace and the same determinant.
:::

:::beweis Change of basis
We have $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}-\lambda\mathbf{I}=\mathbf{S}^{-1}(\mathbf{A}-\lambda\mathbf{I})\mathbf{S}$. By the rules from [Chapter 1, Section 14.5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5), the determinant of this is $\det\mathbf{S}^{-1}\cdot\det(\mathbf{A}-\lambda\mathbf{I})\cdot\det\mathbf{S}=\det(\mathbf{A}-\lambda\mathbf{I})$. By [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5), trace and determinant are determined by the eigenvalues.
:::

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ and the basis $(1,\,0)^{\top}$, $(1,\,1)^{\top}$ from [Chapter 1, Section 13.3](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3), we have $\mathbf{S}=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ and $\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}1&-1\\0&1\end{smallmatrix}\bigr)$. Then

$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}4&5\\2&5\end{pmatrix}=\begin{pmatrix}2&0\\2&5\end{pmatrix}.$$

The trace is again $7$, the determinant again $10$, and the eigenvalues now sit on the diagonal of a triangular matrix: $2$ and $5$.
::::

⁠**In short:** In the basis of the columns of $\mathbf{S}$, the map $\mathbf{A}$ has the matrix $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$; eigenvalues, trace and determinant stay the same.

### Diagonalization

<span class="anker" id="stufe-7-2"></span>

The simplest possible matrix is a diagonal matrix: it multiplies each coordinate by a number of its own, without mixing the coordinates. If you take the eigenvectors as the basis, each basis vector is only multiplied by its eigenvalue. In this basis, the matrix is therefore diagonal.

:::satz Theorem 7.3 (Diagonalization)
<span class="anker" id="satz-7-3"></span>

If $\mathbf{A}\in\mathbb{R}^{n\times n}$ has $n$ linearly independent eigenvectors $\mathbf s_1,\dots,\mathbf s_n$ for the eigenvalues $\lambda_1,\dots,\lambda_n$, and $\mathbf{S}$ is the matrix with these columns, then

<span class="anker" id="gl-7-1"></span>
$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\qquad\text{so}\qquad \mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1} . \tag{7.1}$$

Conversely: if $\mathbf{A}$ can be written in this way, the columns of $\mathbf{S}$ are eigenvectors.
:::

:::beweis Diagonalization
By [Chapter 1, Section 9.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-2), column $i$ of $\mathbf{A}\mathbf{S}$ is the product $\mathbf{A}\mathbf s_i=\lambda_i\mathbf s_i$, and column $i$ of $\mathbf{S}\boldsymbol{\Lambda}$ is also $\lambda_i\mathbf s_i$. So $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$. The columns of $\mathbf{S}$ are independent, so $\mathbf{S}$ is invertible, and multiplying by $\mathbf{S}^{-1}$ from the left gives [(7.1)](#gl-7-1). Reading the same equation $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$ backwards gives the converse.
:::

A matrix that can be written in this way is called __diagonalizable__. By the theorem in Section [6.8](eigenwerte-und-eigenvektoren.html#stufe-6-8), this is the case, for example, whenever all $n$ eigenvalues are different. The shear is not diagonalizable, because it is missing an eigenvector. The rotation by $90^\circ$ is not diagonalizable with real numbers either, only with complex ones. Both are nevertheless invertible: invertible and diagonalizable are two different properties.

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ with the eigenvectors $(1,\,1)^{\top}$ and $(1,\,-2)^{\top}$,

$$\mathbf{S}=\begin{pmatrix}1&1\\1&-2\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix},\qquad \mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix}\begin{pmatrix}5&2\\5&-4\end{pmatrix}=\begin{pmatrix}5&0\\0&2\end{pmatrix}.$$
::::

⁠**In short:** A matrix with $n$ independent eigenvectors is diagonal in their basis: $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$.

### Decoupling: powers and sequences

<span class="anker" id="stufe-7-3"></span>

What this is good for is shown by a matrix that is applied again and again. Two towns A and B exchange residents every year: $20\,\%$ of the residents of A move to B, $30\,\%$ of the residents of B move to A, and everyone else stays. If $\mathbf{x}_k$ contains the populations in year $k$, then

$$\mathbf{x}_{k+1}=\mathbf M\mathbf{x}_k\qquad\text{with}\qquad \mathbf M=\begin{pmatrix}0.8&0.3\\0.2&0.7\end{pmatrix}.$$

The two populations are coupled: each new number depends on both old ones. After $k$ years, $\mathbf{x}_k=\mathbf M^k\mathbf{x}_0$. Computing the power $\mathbf M^k$ directly is tedious and does not show what happens in the long run. In the eigenbasis it is easy.

:::satz Theorem 7.4 (Powers and sequences in the eigenbasis)
<span class="anker" id="satz-7-4"></span>

If $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$, then $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$ with $\boldsymbol{\Lambda}^k=\operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k)$. For the sequence $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k$,

<span class="anker" id="gl-7-2"></span>
$$\mathbf{x}_k=\sum_{i=1}^nc_i\,\lambda_i^k\,\mathbf s_i\qquad\text{with}\qquad \mathbf{c}=\mathbf{S}^{-1}\mathbf{x}_0 . \tag{7.2}$$
:::

:::beweis Powers
$\mathbf{A}^2=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\mathbf{S}\boldsymbol{\Lambda}^2\mathbf{S}^{-1}$, because $\mathbf{S}^{-1}\mathbf{S}=\mathbf{I}$ drops out in the middle; likewise for every power. If you split $\mathbf{x}_0=\sum_ic_i\mathbf s_i$ into eigenvectors, each application of $\mathbf{A}$ multiplies each part only by its eigenvalue.
:::

In the coordinates $\mathbf{c}$ of the eigenbasis, each step multiplies each coordinate by its own number: $c_i\mapsto\lambda_ic_i$. A coupled calculation with $n$ unknowns becomes $n$ separate calculations with one unknown each. These coordinates are decoupled. In the long run, the part with the eigenvalue of largest magnitude dominates.

::::beispiel [Worked example]
$\mathbf M$ has the trace $1.5$ and the determinant $0.56-0.06=0.5$, hence the eigenvalues $1$ and $0.5$. Eigenvectors are $\mathbf s_1=(3,\,2)^{\top}$ for the eigenvalue $1$, because $\mathbf M\mathbf s_1=(2.4+0.6,\ 0.6+1.4)^{\top}=\mathbf s_1$, and $\mathbf s_2=(1,\,-1)^{\top}$ for the eigenvalue $0.5$. If $1000$ people live in A at first and nobody lives in B, then $\mathbf{x}_0=(1000,\,0)^{\top}=200\,\mathbf s_1+400\,\mathbf s_2$, and by [(7.2)](#gl-7-2)

$$\mathbf{x}_k=200\begin{pmatrix}3\\2\end{pmatrix}+400\cdot0.5^k\begin{pmatrix}1\\-1\end{pmatrix}=\begin{pmatrix}600+400\cdot0.5^k\\400-400\cdot0.5^k\end{pmatrix}.$$

After one year the populations are $(800,\,200)^{\top}$, after two years $(700,\,300)^{\top}$, and in the long run they settle at $(600,\,400)^{\top}$. The part for the eigenvalue $0.5$ halves every year; the part for the eigenvalue $1$ stays.
::::

⁠**In short:** In the eigenbasis, every power of the matrix becomes powers of the eigenvalues; coupled sequences break down into separate sequences, one per eigenvector.

:::hintergrund The same principle for sequences, and the Fourier transform
An aftereffect like the one of the wood stove in [Chapter 1, Section 8.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2), mixes each value of a sequence with fixed weights into the following values. Each value of the result depends on several values of the sequence, and everything is coupled. If you split the sequence into complex oscillations $\mathrm e^{\mathrm j\omega n}$, each of them is only multiplied by its own number, and the coupling is gone. The Fourier transform does for sequences and functions what the change of basis $\mathbf{S}^{-1}$ does for vectors: it converts to the coordinates of these oscillations.

For sequences that run in a circle, the correspondence is even literally a diagonalization. A sequence runs in a circle if its last value is followed again by the first, as with the shifts of a business that works around the clock: the night shift is followed again by the morning shift. An aftereffect in a circle, called cyclic convolution in mathematics, $y_k=\sum_lh_{(k-l)\bmod n}\,x_l$, is a matrix. Its first column is the response $(h_0,\dots,h_{n-1})^{\top}$ to a single $1$ in the first position, and its other columns are its shifts around the circle. Its eigenvectors are the complex oscillations $\mathbf f_m=\bigl(1,\ \mathrm e^{\mathrm j2\pi m/n},\ \mathrm e^{\mathrm j2\pi\cdot2m/n},\dots\bigr)^{\top}$, and the eigenvalue for $\mathbf f_m$ is the value $H[m]=\sum_qh_q\,\mathrm e^{-\mathrm j2\pi mq/n}$ of the discrete Fourier transform of the weights. So the matrix of the discrete Fourier transform is, up to the factor $1/n$, the $\mathbf{S}^{-1}$ that diagonalizes every cyclic convolution, and it does so for all weights at once. Example with $n=3$ shifts and $h=(1,\,0.5,\,0)$: the matrix $\Bigl(\begin{smallmatrix}1&0&0.5\\0.5&1&0\\0&0.5&1\end{smallmatrix}\Bigr)$ maps $\mathbf f_0=(1,1,1)^{\top}$ to $1.5\,\mathbf f_0$, and $1.5=H[0]=h_0+h_1+h_2$.
:::

### Symmetric matrices have real eigenvalues

<span class="anker" id="stufe-7-4"></span>

Many things are especially simple for symmetric matrices. The first: their eigenvalues are always real. So a symmetric matrix does not rotate any plane within itself, as the rotations in Section [6.6](eigenwerte-und-eigenvektoren.html#stufe-6-6) do.

:::satz Theorem 7.5 (Real eigenvalues)
<span class="anker" id="satz-7-5"></span>

Every eigenvalue of a real symmetric matrix is real.
:::

:::beweis Real eigenvalues
Let $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ with $\mathbf{v}\ne\mathbf{0}$, where $\lambda$ and $\mathbf{v}$ may for now be complex. Conjugating both sides leaves $\mathbf{A}$ unchanged, because it is real: $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$. Compute the number $(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}$ in two ways. Once with $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$:

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=\lambda\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

Once with $\mathbf{A}=\mathbf{A}^{\top}$ and $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$:

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=(\mathbf{A}^{\top}\mathbf{v}^*)^{\top}\mathbf{v}=(\mathbf{A}\mathbf{v}^*)^{\top}\mathbf{v}=\lambda^*\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

So $(\lambda-\lambda^*)\,(\mathbf{v}^*)^{\top}\mathbf{v}=0$. By Section [6.1](eigenwerte-und-eigenvektoren.html#stufe-6-1), $(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0$, so $\lambda=\lambda^*$, and $\lambda$ is real.
:::

For a real eigenvalue there are then also real eigenvectors, because $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ is a real system of equations.

::::beispiel [Worked example]
$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ has the characteristic polynomial $\lambda^2-7\lambda+6$ with the discriminant $49-24=25>0$ and the real eigenvalues $6$ and $1$. For an arbitrary symmetric $2\times2$ matrix $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$, the discriminant is $(a+c)^2-4(ac-b^2)=(a-c)^2+4b^2\ge0$; so the eigenvalues are always real, as the theorem says.
::::

⁠**In short:** A symmetric matrix has only real eigenvalues and real eigenvectors.

### Eigenvectors of symmetric matrices are perpendicular

<span class="anker" id="stufe-7-5"></span>

The eigenvectors of $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ were at a slant to each other. For symmetric matrices this cannot happen.

:::satz Theorem 7.6 (Orthogonal eigenvectors)
<span class="anker" id="satz-7-6"></span>

Eigenvectors of a symmetric matrix for different eigenvalues are perpendicular to each other.
:::

:::beweis Orthogonal eigenvectors
Let $\mathbf{A}\mathbf{v}_1=\lambda_1\mathbf{v}_1$ and $\mathbf{A}\mathbf{v}_2=\lambda_2\mathbf{v}_2$ with $\lambda_1\ne\lambda_2$. Compute $\mathbf{v}_1^{\top}\mathbf{A}\mathbf{v}_2$ in two ways: as $\mathbf{v}_1^{\top}(\lambda_2\mathbf{v}_2)=\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2$, and, using $\mathbf{A}^{\top}=\mathbf{A}$, as $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\lambda_1\,\mathbf{v}_1^{\top}\mathbf{v}_2$. So $(\lambda_1-\lambda_2)\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$, and since $\lambda_1\ne\lambda_2$, we get $\mathbf{v}_1^{\top}\mathbf{v}_2=0$.
:::

::::beispiel [Worked example]
$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ has the eigenvector $(2,\,1)^{\top}$ for the eigenvalue $6$, because $(10+2,\ 4+2)^{\top}=6\,(2,\,1)^{\top}$, and the eigenvector $(1,\,-2)^{\top}$ for the eigenvalue $1$, because $(5-4,\ 2-4)^{\top}=(1,\,-2)^{\top}$. Their dot product is $2-2=0$ (Fig. [19](#abb-19)).

:::abbildung ml/k2rsenkrecht 19
The dot product of the eigenvectors $(2,1)^{\top}$ for the eigenvalue $6$ and $(1,-2)^{\top}$ for the eigenvalue $1$ of the symmetric matrix $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$: they are perpendicular to each other.
:::
::::

⁠**In short:** For a symmetric matrix, eigenvectors for different eigenvalues are perpendicular to each other.

:::hintergrund Why it is symmetry that makes the eigendirections perpendicular
The proof uses symmetry in exactly one place: $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\mathbf{v}_1^{\top}(\mathbf{A}\mathbf{v}_2)$. For a symmetric matrix this equation holds for all vectors; you may move $\mathbf{A}$ from one side of the dot product to the other. The dot product measures how much of $\mathbf{v}_2$ points in the direction of $\mathbf{v}_1$. If $\mathbf{A}$ stretches one direction by $\lambda_1$ and the other by $\lambda_2$, this share is multiplied by $\lambda_1$ on the left and by $\lambda_2$ on the right. The two sides can only be equal if there is nothing to multiply, that is, if the share is zero. For a non-symmetric matrix this shifting rule does not hold, and slanted eigendirections are possible.

A second, important property follows from this. If $\mathbf{q}$ is an eigenvector and $\mathbf{z}$ is perpendicular to $\mathbf{q}$, then $\mathbf{A}\mathbf{z}$ is also perpendicular to $\mathbf{q}$: $(\mathbf{A}\mathbf{z})^{\top}\mathbf{q}=\mathbf{z}^{\top}\mathbf{A}\mathbf{q}=\lambda\,\mathbf{z}^{\top}\mathbf{q}=0$. So a symmetric matrix maps the orthogonal complement of an eigenvector into itself. There you can look for the next eigenvector, and so on. This is exactly how the proof in the next subsection works.
:::

### The spectral theorem

<span class="anker" id="stufe-7-6"></span>

The two previous theorems suggest that every symmetric matrix is diagonal in an orthonormal basis of eigenvectors. This is true even when eigenvalues occur more than once. The set of eigenvalues of a matrix is called its spectrum, hence the name of the theorem.

:::satz Theorem 7.7 (Spectral theorem)
<span class="anker" id="satz-7-7"></span>

For every symmetric matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ there is an orthonormal basis $\mathbf{q}_1,\dots,\mathbf{q}_n$ of eigenvectors with real eigenvalues $\lambda_1,\dots,\lambda_n$. With the orthogonal matrix $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$ and $\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$,

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}=\sum_{i=1}^n\lambda_i\,\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{7.3}$$
:::

:::beweis Spectral theorem
Proceed step by step. By Section [6.3](eigenwerte-und-eigenvektoren.html#stufe-6-3), $\mathbf{A}$ has at least one eigenvalue $\lambda_1$; by Section [7.4](#stufe-7-4), it is real and has a real eigenvector, normalized $\mathbf{q}_1$. Extend $\mathbf{q}_1$ to an orthonormal basis of $\mathbb{R}^n$, for instance with the Gram–Schmidt process applied to $\mathbf{q}_1,\mathbf{e}_1,\dots,\mathbf{e}_n$, skipping the vectors with $\tilde{\mathbf{q}}=\mathbf{0}$. The remaining basis vectors form the columns of a matrix $\mathbf{W}\in\mathbb{R}^{n\times(n-1)}$, and $\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1&\mathbf{W}\end{pmatrix}$ is orthogonal. Then

$$\mathbf{Q}_1^{\top}\mathbf{A}\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{q}_1^{\top}\mathbf{A}\mathbf{W}\\\mathbf{W}^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{W}^{\top}\mathbf{A}\mathbf{W}\end{pmatrix}=\begin{pmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{B}\end{pmatrix}$$

with the symmetric $(n-1)\times(n-1)$ matrix $\mathbf{B}=\mathbf{W}^{\top}\mathbf{A}\mathbf{W}$. The zeros at the bottom left arise because $\mathbf{A}\mathbf{q}_1=\lambda_1\mathbf{q}_1$ is perpendicular to the columns of $\mathbf{W}$, and those at the top right likewise, because $\mathbf{A}$ is symmetric. Repeat the same for $\mathbf{B}$ until a $1\times1$ matrix is left. Once you have found in this way an orthogonal matrix $\mathbf{Q}_B$ for $\mathbf{B}$ such that $\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B$ is diagonal, $\mathbf{Q}=\mathbf{Q}_1\bigl(\begin{smallmatrix}1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B\end{smallmatrix}\bigr)$ is orthogonal as a product of orthogonal matrices, and $\mathbf{Q}^{\top}\mathbf{A}\mathbf{Q}=\bigl(\begin{smallmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B\end{smallmatrix}\bigr)=\boldsymbol{\Lambda}$ is diagonal. Because $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$, it follows that $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$. The sum form follows from [Chapter 1, Section 9.5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5), because $\mathbf{Q}\boldsymbol{\Lambda}$ has the columns $\lambda_i\mathbf{q}_i$.
:::

By Section [2.3](projektion-auf-eine-gerade.html#stufe-2-3), each term $\mathbf{q}_i\mathbf{q}_i^{\top}$ is the projection onto the line in the direction of $\mathbf{q}_i$. So a symmetric matrix is a sum of projections onto perpendicular axes, each weighted with its eigenvalue. For a multiple eigenvalue, the choice of the $\mathbf{q}_i$ in its eigenspace is free: every orthonormal basis of the eigenspace will do. The sign of each $\mathbf{q}_i$ is free as well. Some books sort the eigenvalues in descending order, others do not.

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$, $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$ and $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$ are the normalized eigenvectors for $6$ and $1$. Then

$$6\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}+1\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\frac15\begin{pmatrix}25&10\\10&10\end{pmatrix}=\begin{pmatrix}5&2\\2&2\end{pmatrix}.$$
::::

⁠**In short:** Every symmetric matrix is $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$: diagonal in a suitably rotated set of axes, a weighted sum of projections onto perpendicular axes.

:::hintergrund Where symmetric matrices come from
Symmetric matrices arise wherever a matrix describes pairwise relationships that do not depend on the order. The Gram matrices $\mathbf{X}^{\top}\mathbf{X}$ and $\mathbf{X}\mathbf{X}^{\top}$ from [Chapter 1, Section 10](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10), contain dot products, and $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$. By Section [5.2](quadratische-formen.html#stufe-5-2), the matrix of a quadratic form can always be chosen symmetric. A table of the distances between cities, measured as the crow flies, is symmetric because the distance from A to B is the same as from B to A. For all of these matrices, the spectral theorem guarantees real eigenvalues and perpendicular eigendirections.
:::

### Principal axes

<span class="anker" id="stufe-7-7"></span>

In Section [5.3](quadratische-formen.html#stufe-5-3), the shape of a quadratic form was easy to recognize as long as its matrix was diagonal. The spectral theorem makes every symmetric matrix diagonal if you rotate the coordinates suitably. This makes the cross terms disappear.

:::satz Theorem 7.8 (Principal axes of a quadratic form)
<span class="anker" id="satz-7-8"></span>

If $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ and $c_i=\mathbf{q}_i^{\top}\mathbf{x}$ are the coordinates of $\mathbf{x}$ in the eigenbasis, then

<span class="anker" id="gl-7-4"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_1c_1^2+\lambda_2c_2^2+\dots+\lambda_nc_n^2 . \tag{7.4}$$
:::

:::beweis Principal axes
With $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$ we get $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}\mathbf{x}=\mathbf{c}^{\top}\boldsymbol{\Lambda}\mathbf{c}=\sum_i\lambda_ic_i^2$.
:::

The directions of the eigenvectors are therefore called the __principal axes__ of the quadratic form. If all eigenvalues are positive, the contour line $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=1$ is an ellipse, and in $\mathbb{R}^3$ an ellipsoid. Its axes lie in the directions $\mathbf{q}_i$, and the semi-axis in the direction $\mathbf{q}_i$ has length $1/\sqrt{\lambda_i}$, because for $\mathbf{x}=t\,\mathbf{q}_i$ we have $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_it^2=1$ exactly at $t=\pm1/\sqrt{\lambda_i}$. A large eigenvalue belongs to a steep direction and a short semi-axis.

:::abbildung ml/k2ellipse 20
The contour lines $5x_1^2+4x_1x_2+2x_2^2=1$ (blue) and $=\tfrac14$ (light blue) are ellipses. Their axes (gray) lie in the directions of the eigenvectors $\mathbf{q}_1=(2,1)^{\top}/\sqrt5$ for the eigenvalue $6$ and $\mathbf{q}_2=(1,-2)^{\top}/\sqrt5$ for the eigenvalue $1$. The semi-axes of the outer ellipse are $1/\sqrt6\approx0.41$ (red) and $1/\sqrt1=1$ (green): in the direction of the large eigenvalue, the form rises most steeply, and the ellipse is narrowest there.
:::

::::beispiel [Worked example]
For $f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$, the coordinates in the eigenbasis are $c_1=(2x_1+x_2)/\sqrt5$ and $c_2=(x_1-2x_2)/\sqrt5$, and

$$5x_1^2+4x_1x_2+2x_2^2=6\,c_1^2+c_2^2=\tfrac65(2x_1+x_2)^2+\tfrac15(x_1-2x_2)^2 .$$

Multiplied out, the right-hand side gives $\tfrac15\bigl(24x_1^2+24x_1x_2+6x_2^2+x_1^2-4x_1x_2+4x_2^2\bigr)=5x_1^2+4x_1x_2+2x_2^2$. The contour line $f=1$ is the ellipse in Fig. [20](#abb-20), with the semi-axes $1/\sqrt6\approx0.408$ and $1$.
::::

⁠**In short:** In the eigenbasis, every quadratic form becomes the sum $\sum_i\lambda_ic_i^2$ without cross terms; the eigenvectors are the principal axes of its ellipses, and the semi-axes are $1/\sqrt{\lambda_i}$.

:::hintergrund Two ways of completing the square
In Section [5.4](quadratische-formen.html#stufe-5-4), the same form could also be written as $5(x_1+0.4x_2)^2+1.2x_2^2$. The factors $5$ and $1.2$ there are different numbers from the eigenvalues $6$ and $1$ here. Both decompositions are correct, but the new coordinates are different: in completing the square, $x_1+0.4x_2$ and $x_2$ are oblique coordinates; in the spectral theorem, $c_1,c_2$ are coordinates in a rotated set of perpendicular axes. Only the second decomposition shows the axes of the ellipse. What the two have in common is something else: the number of positive, negative and vanishing factors is the same. This holds for every decomposition of a quadratic form into a sum of squares of independent coordinates; the theorem is called Sylvester's law of inertia. That is why completing the square and the eigenvalues always lead to the same verdict about bowl, trough or saddle.
:::

:::aufgabe Exercise 21 ★ Diagonalizing
<span class="anker" id="aufg-21"></span>

Let $\mathbf{A}=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$ be the matrix from Exercise [17](eigenwerte-und-eigenvektoren.html#aufg-17).

<ol class="al">

<li>

Give $\mathbf{S}$ and $\boldsymbol{\Lambda}$ with $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ and check the equation.

</li>

<li>

Compute $\mathbf{A}^3$ once directly and once as $\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}$.

</li>

</ol>

:::loesung
(a) From Exercise [17](eigenwerte-und-eigenvektoren.html#aufg-17): eigenvalues $4$ and $1$ with the eigenvectors $(1,\,1)^{\top}$ and $(2,\,-1)^{\top}$. So

$$\mathbf{S}=\begin{pmatrix}1&2\\1&-1\end{pmatrix},\qquad \boldsymbol{\Lambda}=\begin{pmatrix}4&0\\0&1\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}1&2\\1&-1\end{pmatrix},$$

because $\det\mathbf{S}=-3$. Check: $\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}4&2\\4&-1\end{smallmatrix}\bigr)\cdot\tfrac13\bigl(\begin{smallmatrix}1&2\\1&-1\end{smallmatrix}\bigr)=\tfrac13\bigl(\begin{smallmatrix}6&6\\3&9\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$.

(b) Directly: $\mathbf{A}^2=\bigl(\begin{smallmatrix}6&10\\5&11\end{smallmatrix}\bigr)$ and $\mathbf{A}^3=\mathbf{A}^2\mathbf{A}=\bigl(\begin{smallmatrix}12+10&12+30\\10+11&10+33\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}22&42\\21&43\end{smallmatrix}\bigr)$. Via the eigenbasis: $\boldsymbol{\Lambda}^3=\operatorname{diag}(64,\,1)$, $\mathbf{S}\boldsymbol{\Lambda}^3=\bigl(\begin{smallmatrix}64&2\\64&-1\end{smallmatrix}\bigr)$ and

$$\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}=\frac13\begin{pmatrix}64+2&128-2\\64-1&128+1\end{pmatrix}=\begin{pmatrix}22&42\\21&43\end{pmatrix}.$$

For large powers, the second route is much shorter: only the eigenvalues are raised to the power.
:::
:::

:::aufgabe Exercise 22 ★★ Decoupling a sequence
<span class="anker" id="aufg-22"></span>

The Fibonacci numbers $0,1,1,2,3,5,\dots$ satisfy $F_{k+2}=F_{k+1}+F_k$. With $\mathbf{x}_k=(F_{k+1},\,F_k)^{\top}$, we have $\mathbf{x}_{k+1}=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\mathbf{x}_k$.

<ol class="al">

<li>

Determine the eigenvalues and eigenvectors of the matrix.

</li>

<li>

Use [(7.2)](#gl-7-2) to derive a formula for $F_k$ and check it for $k=5$.

</li>

<li>

How does $F_{k+1}/F_k$ behave for large $k$, and why?

</li>

</ol>

:::loesung
(a) $p(\lambda)=\lambda^2-\lambda-1$ with the roots $\varphi=\tfrac{1+\sqrt5}2\approx1.618$ and $\psi=\tfrac{1-\sqrt5}2\approx-0.618$. The first row of $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ reads $(1-\lambda)v_1+v_2=0$; the second, $v_1-\lambda v_2=0$, is equivalent to it because $p(\lambda)=0$. Eigenvectors are $\mathbf s_1=(\varphi,\,1)^{\top}$ and $\mathbf s_2=(\psi,\,1)^{\top}$.

(b) $\mathbf{x}_0=(F_1,\,F_0)^{\top}=(1,\,0)^{\top}=c_1\mathbf s_1+c_2\mathbf s_2$ requires $c_1+c_2=0$ and $c_1\varphi+c_2\psi=1$, so $c_1=1/(\varphi-\psi)=1/\sqrt5$ and $c_2=-1/\sqrt5$. By [(7.2)](#gl-7-2), $\mathbf{x}_k=\tfrac1{\sqrt5}(\varphi^k\mathbf s_1-\psi^k\mathbf s_2)$; the second component is

$$F_k=\frac{\varphi^k-\psi^k}{\sqrt5} .$$

For $k=5$: $\varphi^5=\tfrac{11+5\sqrt5}2$ and $\psi^5=\tfrac{11-5\sqrt5}2$, so $F_5=\tfrac{5\sqrt5}{\sqrt5}=5$. Numerically: $\varphi^5\approx11.090$, $\psi^5\approx-0.090$, $(11.090+0.090)/2.236\approx5.000$.

(c) Because $|\psi|<1$, $\psi^k$ tends to zero, and $F_{k+1}/F_k$ tends to $\varphi\approx1.618$, the golden ratio. The part belonging to the eigenvalue of largest magnitude dominates, as in Section [7.3](#stufe-7-3); each further step multiplies it by $\varphi$.
:::
:::

:::aufgabe Exercise 23 ★★ Spectral decomposition
<span class="anker" id="aufg-23"></span>

<ol class="al">

<li>

Write $\mathbf{A}=\bigl(\begin{smallmatrix}3&4\\4&-3\end{smallmatrix}\bigr)$ as $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ and as a sum $\lambda_1\mathbf{q}_1\mathbf{q}_1^{\top}+\lambda_2\mathbf{q}_2\mathbf{q}_2^{\top}$.

</li>

<li>

Determine the principal axes of the form $3x_1^2+8x_1x_2-3x_2^2$ and write it as $\lambda_1c_1^2+\lambda_2c_2^2$. Which basic shape from Section [5.3](quadratische-formen.html#stufe-5-3) is it?

</li>

<li>

The matrix $\Bigl(\begin{smallmatrix}2&0&0\\0&3&1\\0&1&3\end{smallmatrix}\Bigr)$ has the eigenvalue $2$ twice. Give an orthonormal basis of eigenvectors. Is it unique?

</li>

</ol>

:::loesung
(a) Trace $0$, determinant $-9-16=-25$, so $\lambda^2-25=0$ and $\lambda=\pm5$. For $5$: $\bigl(\begin{smallmatrix}-2&4\\4&-8\end{smallmatrix}\bigr)$, $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$. For $-5$: $\bigl(\begin{smallmatrix}8&4\\4&2\end{smallmatrix}\bigr)$, $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$. With $\mathbf{Q}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr)$ and $\boldsymbol{\Lambda}=\operatorname{diag}(5,\,-5)$, we have $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$, and

$$5\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}-5\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\begin{pmatrix}3&4\\4&-3\end{pmatrix}.$$

(b) The form has exactly this matrix. With $c_1=(2x_1+x_2)/\sqrt5$ and $c_2=(x_1-2x_2)/\sqrt5$,

$$3x_1^2+8x_1x_2-3x_2^2=5c_1^2-5c_2^2=(2x_1+x_2)^2-(x_1-2x_2)^2 ,$$

which multiplied out is $4x_1^2+4x_1x_2+x_2^2-x_1^2+4x_1x_2-4x_2^2$. The principal axes point in the directions $(2,\,1)^{\top}$ and $(1,\,-2)^{\top}$. One eigenvalue positive, one negative: a saddle whose axes are rotated relative to the coordinate axes.

(c) $\mathbf{e}_1$ is an eigenvector for $2$. The lower block $\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ has the eigenvalues $4$ with $(1,\,1)^{\top}$ and $2$ with $(1,\,-1)^{\top}$. An orthonormal basis of eigenvectors is therefore

$$\mathbf{e}_1,\qquad \tfrac1{\sqrt2}(0,\,1,\,-1)^{\top}\quad\text{for }2,\qquad \tfrac1{\sqrt2}(0,\,1,\,1)^{\top}\quad\text{for }4 .$$

It is not unique. The eigenspace for $2$ is the plane spanned by $\mathbf{e}_1$ and $(0,\,1,\,-1)^{\top}$, and every orthonormal basis of this plane will do, for example $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1+\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$ and $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1-\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$. Only the eigenvector for the simple eigenvalue $4$ is unique, up to its sign.
:::
:::
