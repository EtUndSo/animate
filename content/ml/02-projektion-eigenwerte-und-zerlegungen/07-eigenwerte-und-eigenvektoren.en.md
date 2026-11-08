---
title: Eigenvalues and eigenvectors
pfad: Computer Science / Machine Learning / Mathematical Foundations / Projection, Eigenvalues and Decompositions
knoten: Foundations 2: Projection, Eigenvalues and Decompositions
nachschlagen: ja
order: 15220700
summary: A matrix rotates and stretches most vectors at the same time.
tags: complex conjugate, eigenvector, eigenvalue, characteristic polynomial, eigenspace, trace, algebraic multiplicity, geometric multiplicity
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
A matrix rotates and stretches most vectors at the same time. Some directions, however, it does not rotate: an arrow in such a direction only becomes longer, shorter or flipped over. This section finds these directions and the stretch factors that belong to them. They are the natural axes of a matrix.
:::

### What you need for this: complex numbers

<span class="anker" id="stufe-6-1"></span>

The search for stretch factors leads to polynomial equations, and not every one of them has real solutions. This subsection collects what this chapter uses about complex numbers.

**Complex numbers.** A complex number $z=x+\mathrm j\,y$ consists of the real part $x$ and the imaginary part $y$, two real numbers. The imaginary unit satisfies $\mathrm j^2=-1$. Electrical engineering writes $\mathrm j$ instead of $i$, because $i$ is taken for the current.

**Conjugation and magnitude.** The __complex conjugate__ of $z$ is $z^*=x-\mathrm j\,y$. We have $z\,z^*=x^2+y^2=|z|^2$, the square of the magnitude, a real number that is zero only for $z=0$. A number is real if and only if $z=z^*$. Conjugation is compatible with sums and products: $(z+w)^*=z^*+w^*$ and $(zw)^*=z^*w^*$. For a vector $\mathbf{v}$ with complex components, $\mathbf{v}^*$ in this chapter denotes the vector of the conjugated components, not transposed. Then

$$(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0\qquad\text{for }\mathbf{v}\ne\mathbf{0} .$$

**Euler's formula.** For every real number $\alpha$, $\mathrm e^{\mathrm j\alpha}=\cos\alpha+\mathrm j\sin\alpha$, a point on the unit circle of the complex plane with magnitude $1$.

**Roots of polynomials.** Every polynomial of degree $n\ge1$ with real or complex coefficients has exactly $n$ complex roots if multiple roots are counted according to their multiplicity, and it factors into $n$ linear factors. If the polynomial has real coefficients, then whenever $z$ is a root, so is $z^*$: non-real roots come in pairs.

⁠**Worked example:** By the quadratic formula, $\lambda^2-1.2\lambda+1=0$ has the roots $\lambda=0.6\pm\sqrt{0.36-1}=0.6\pm\mathrm j\,0.8$, a conjugate pair with magnitude $\sqrt{0.36+0.64}=1$. For $\mathbf{v}=(1,\,-\mathrm j)^{\top}$, we have $\mathbf{v}^*=(1,\,\mathrm j)^{\top}$ and $(\mathbf{v}^*)^{\top}\mathbf{v}=1\cdot1+\mathrm j\cdot(-\mathrm j)=1+1=2$ (Fig. [16](#abb-16)).

:::abbildung ml/k2rkomplex 16
The dot product $(\mathbf{v}^*)^{\top}\mathbf{v}$ for $\mathbf{v}=(1,-\mathrm j)^{\top}$: each term is $v_i^*v_i=|v_i|^2$, because $\mathrm j\cdot(-\mathrm j)=-\mathrm j^2=1$.
:::

⁠**In short:** Complex numbers $x+\mathrm jy$ with $\mathrm j^2=-1$ solve every polynomial equation; conjugation flips the sign of the imaginary part, and $zz^*=|z|^2$ is real.

### Eigenvectors and eigenvalues

<span class="anker" id="stufe-6-2"></span>

In Foundations 1, Section 8.3, the grid of the plane was rotated, stretched and sheared by matrices. In the process, most arrows change their direction. For some matrices, however, there are directions in which an arrow stays on its line through the origin: it is only stretched, compressed or flipped over (Fig. [17](#abb-17)).

:::abbildung ml/k2eigen 17
The matrix $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ maps the unit circle (gray) to an ellipse (blue). The arrow $\mathbf{v}_1=(1,1)^{\top}/\sqrt2$ (red) stays on its line and is stretched to five times its length, the arrow $\mathbf{v}_2=(1,-2)^{\top}/\sqrt5$ (green) to twice its length; their images are drawn in light colors. The gray lines are the two eigendirections. The unit vector $\mathbf{e}_1$, by contrast, is mapped to $(4,2)^{\top}$ (dashed) and changes its direction.
:::

:::definition Definition 6.1 (Eigenvector, eigenvalue)
<span class="anker" id="satz-6-1"></span>

Let $\mathbf{A}\in\mathbb{R}^{n\times n}$. A vector $\mathbf{v}\ne\mathbf{0}$ is called an __eigenvector__ of $\mathbf{A}$ if there is a number $\lambda$ with

<span class="anker" id="gl-6-1"></span>
$$\mathbf{A}\mathbf{v}=\lambda\,\mathbf{v} . \tag{6.1}$$

The number $\lambda$ is called the corresponding __eigenvalue__.
:::

The zero vector is excluded because $\mathbf{A}\mathbf{0}=\lambda\mathbf{0}$ holds for every number $\lambda$ and reveals nothing. The eigenvalue, on the other hand, may be zero: then the eigenvector is mapped to $\mathbf{0}$. A negative eigenvalue flips the arrow over. In this chapter, eigenvalues are denoted $\lambda$ or $\lambda_i$. The prefix *eigen* comes from German and has been adopted into English: *eigenvalue*, *eigenvector*.

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$,

$$\mathbf{A}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}5\\5\end{pmatrix}=5\begin{pmatrix}1\\1\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\-2\end{pmatrix}=\begin{pmatrix}2\\-4\end{pmatrix}=2\begin{pmatrix}1\\-2\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}4\\2\end{pmatrix}.$$

So $(1,\,1)^{\top}$ is an eigenvector for the eigenvalue $5$, and $(1,\,-2)^{\top}$ is one for the eigenvalue $2$. The vector $(1,\,0)^{\top}$ is not an eigenvector, because $(4,\,2)^{\top}$ is not a multiple of it.

⁠**In short:** An eigenvector is not rotated by the matrix, only multiplied by a number; this number is the eigenvalue.

:::hintergrund You already know eigenfunctions
From signals and systems you know the same idea for functions instead of vectors. An LTI system with the impulse response $h(t)$ responds to the exponential function $\mathrm e^{pt}$ with the complex frequency $p$, written $s$ in many books, with

$$\int_{-\infty}^{\infty}h(\tau)\,\mathrm e^{p(t-\tau)}\,\mathrm{d}\tau=H(p)\,\mathrm e^{pt},\qquad H(p)=\int_{-\infty}^{\infty}h(\tau)\,\mathrm e^{-p\tau}\,\mathrm{d}\tau ,$$

for all $p$ for which the integral exists. The shape of the input is preserved; the only thing added is a numerical factor: $\mathrm e^{pt}$ is an eigenfunction of the system, and the eigenvalue is the value $H(p)$ of the transfer function. Equation [(6.1)](#gl-6-1) says the same thing for a matrix. An LTI system is a linear map from signals to signals, a matrix is a linear map from vectors to vectors; in both cases there are inputs that are only multiplied by a number.
:::

### The characteristic polynomial

<span class="anker" id="stufe-6-3"></span>

How do you find eigenvalues without guessing? Rewrite [(6.1)](#gl-6-1) so that everything is on one side: $\mathbf{A}\mathbf{v}-\lambda\mathbf{v}=\mathbf{0}$, that is, $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$. We are looking for a $\lambda$ for which this homogeneous system has a solution $\mathbf{v}\ne\mathbf{0}$. By Foundations 1, Section 11.5, this means: the matrix $\mathbf{A}-\lambda\mathbf{I}$ is not invertible. By Foundations 1, Section 14.6, this is the case exactly when its determinant is zero.

:::definition Definition 6.2 (Characteristic polynomial)
<span class="anker" id="satz-6-2"></span>

For $\mathbf{A}\in\mathbb{R}^{n\times n}$,

<span class="anker" id="gl-6-2"></span>
$$p(\lambda)=\det(\mathbf{A}-\lambda\mathbf{I}) \tag{6.2}$$

is called the __characteristic polynomial__ of $\mathbf{A}$.
:::

:::satz Theorem 6.3 (Eigenvalues are roots)
<span class="anker" id="satz-6-3"></span>

A number $\lambda$ is an eigenvalue of $\mathbf{A}$ if and only if $p(\lambda)=0$.
:::

The characteristic polynomial has degree $n$. For a $2\times2$ matrix it is

<span class="anker" id="gl-6-3"></span>
$$\det\begin{pmatrix}a-\lambda&b\\c&d-\lambda\end{pmatrix}=(a-\lambda)(d-\lambda)-bc=\lambda^2-(a+d)\,\lambda+(ad-bc) . \tag{6.3}$$

By the subsection on complex numbers, it has exactly $n$ complex roots, counted with multiplicity. So an $n\times n$ matrix has $n$ eigenvalues if complex ones are allowed and multiple ones are counted according to their multiplicity.

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$, $p(\lambda)=\lambda^2-7\lambda+(12-2)=\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2)$. The eigenvalues are $5$ and $2$, as in the previous subsection. For the diagonal matrix $\operatorname{diag}(3,\,-1)$, $p(\lambda)=(3-\lambda)(-1-\lambda)$ with the roots $3$ and $-1$: the eigenvalues of a diagonal matrix are on its diagonal, and the eigenvectors are the unit vectors.

⁠**In short:** The eigenvalues are the roots of the characteristic polynomial $\det(\mathbf{A}-\lambda\mathbf{I})$; counted with multiplicity and including complex ones, an $n\times n$ matrix has $n$ eigenvalues.

### Computing eigenvectors

<span class="anker" id="stufe-6-4"></span>

Once an eigenvalue $\lambda$ is known, the corresponding eigenvectors are the solutions $\mathbf{v}\ne\mathbf{0}$ of the homogeneous system $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$. You find them with Gaussian elimination. Together with $\mathbf{v}$, every multiple $c\,\mathbf{v}$ with $c\ne0$ is an eigenvector, because $\mathbf{A}(c\mathbf{v})=c\lambda\mathbf{v}=\lambda(c\mathbf{v})$. So an eigenvector is never unique; only its direction is, and sometimes not even that.

:::definition Definition 6.4 (Eigenspace)
<span class="anker" id="satz-6-4"></span>

The null space of $\mathbf{A}-\lambda\mathbf{I}$ is called the __eigenspace__ of $\mathbf{A}$ for the eigenvalue $\lambda$.
:::

It contains all eigenvectors for $\lambda$ and the zero vector. As a null space, it is a subspace in the sense of Section [4.1](projektion-auf-einen-unterraum.html#stufe-4-1).

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ and $\lambda=5$,

$$\mathbf{A}-5\mathbf{I}=\begin{pmatrix}-1&1\\2&-2\end{pmatrix}.$$

Both rows require the same thing: $-v_1+v_2=0$. The eigenspace is the line of all multiples of $(1,\,1)^{\top}$. For $\lambda=2$, $\mathbf{A}-2\mathbf{I}=\bigl(\begin{smallmatrix}2&1\\2&1\end{smallmatrix}\bigr)$ with the condition $2v_1+v_2=0$; the eigenspace is the line in the direction of $(1,\,-2)^{\top}$. Normalized, the eigenvectors are $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ and $\mathbf{v}_2=(1,\,-2)^{\top}/\sqrt5$, as in Fig. [17](#abb-17). They are not perpendicular to each other: $(1,\,1)(1,\,-2)^{\top}=-1\ne0$.

⁠**In short:** The eigenvectors for $\lambda$ are the solutions $\mathbf{v}\ne\mathbf{0}$ of $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$; together with the zero vector they form the eigenspace.

### Trace and determinant

<span class="anker" id="stufe-6-5"></span>

Two numbers appear in [(6.3)](#gl-6-3) that you can read directly off the matrix: $ad-bc$ is the determinant, and $a+d$ is the sum of the diagonal entries. This sum has a name of its own. Both numbers are related to the eigenvalues in a simple way and are therefore useful as a check.

:::definition Definition 6.5 (Trace)
<span class="anker" id="satz-6-5"></span>

The __trace__ of a square matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ is the sum of its diagonal entries:

<span class="anker" id="gl-6-4"></span>
$$\operatorname{tr}\mathbf{A}=a_{11}+a_{22}+\dots+a_{nn}=\sum_{i=1}^na_{ii} . \tag{6.4}$$
:::

:::satz Theorem 6.6 (Trace and determinant from the eigenvalues)
<span class="anker" id="satz-6-6"></span>

If $\lambda_1,\dots,\lambda_n$ are the eigenvalues of $\mathbf{A}$, counted with multiplicity and including complex ones, then

<span class="anker" id="gl-6-5"></span>
$$\operatorname{tr}\mathbf{A}=\lambda_1+\lambda_2+\dots+\lambda_n,\qquad \det\mathbf{A}=\lambda_1\cdot\lambda_2\cdots\lambda_n . \tag{6.5}$$

Moreover, $\operatorname{tr}(\mathbf{A}\mathbf{B})=\operatorname{tr}(\mathbf{B}\mathbf{A})$ for $\mathbf{A}\in\mathbb{R}^{m\times n}$ and $\mathbf{B}\in\mathbb{R}^{n\times m}$.
:::

:::herleitung Trace and determinant
For $n=2$: the polynomial $\lambda^2-(a+d)\lambda+(ad-bc)$ factors into $(\lambda-\lambda_1)(\lambda-\lambda_2)=\lambda^2-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2$. Comparing coefficients gives $a+d=\lambda_1+\lambda_2$ and $ad-bc=\lambda_1\lambda_2$.

For arbitrary $n$, $p(\lambda)$ likewise factors into $(\lambda_1-\lambda)(\lambda_2-\lambda)\cdots(\lambda_n-\lambda)$; the sign is right because the term $(-\lambda)^n$ occurs in $\det(\mathbf{A}-\lambda\mathbf{I})$. Setting $\lambda=0$ gives $\det\mathbf{A}$ on the left and $\lambda_1\cdots\lambda_n$ on the right. For the trace, compare the coefficients of $\lambda^{n-1}$. On the right, they are $(-1)^{n-1}(\lambda_1+\dots+\lambda_n)$. On the left, in the Laplace expansion only the product of the diagonal entries $(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$ yields such a high power of $\lambda$, with the coefficient $(-1)^{n-1}(a_{11}+\dots+a_{nn})$.

For the last statement: $\operatorname{tr}(\mathbf{A}\mathbf{B})=\sum_i(\mathbf{A}\mathbf{B})_{ii}=\sum_i\sum_la_{il}b_{li}$ and $\operatorname{tr}(\mathbf{B}\mathbf{A})=\sum_l\sum_ib_{li}a_{il}$. This is the same double sum, only ordered differently.
:::

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$, $\operatorname{tr}\mathbf{A}=7=5+2$ (Fig. [18](#abb-18)) and $\det\mathbf{A}=10=5\cdot2$. For $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$, $\operatorname{tr}=7$ and $\det=6$; so the eigenvalues are the solutions of $\lambda^2-7\lambda+6=0$, namely $6$ and $1$. For $\mathbf{A}\in\mathbb{R}^{2\times3}$ with the rows $(1,0,2)$, $(0,1,1)$ and $\mathbf{B}=\mathbf{A}^{\top}$, $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ with trace $7$, and $\mathbf{B}\mathbf{A}$ is a $3\times3$ matrix with the diagonal entries $1$, $1$ and $5$, also with trace $7$.

:::abbildung ml/k2rspur 18
The trace of $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ as the sum of the diagonal entries; it equals the sum of the eigenvalues $5$ and $2$.
:::

⁠**In short:** The trace is the sum of the diagonal entries and the sum of the eigenvalues; the determinant is the product of the eigenvalues.

### Complex eigenvalues

<span class="anker" id="stufe-6-6"></span>

A rotation by $90^\circ$ leaves no arrow on its line: every arrow is turned further by a right angle. So it cannot have a real eigenvector. The characteristic polynomial shows what happens instead.

⁠**Worked example 1:** For the rotation $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$, $p(\lambda)=\lambda^2+1$ with the roots $\lambda=\mathrm j$ and $\lambda=-\mathrm j$. The eigenvalues are purely imaginary. The complex eigenvector $(1,\,-\mathrm j)^{\top}$ belongs to $\lambda=\mathrm j$, because $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)(1,\,-\mathrm j)^{\top}=(\mathrm j,\,1)^{\top}=\mathrm j\,(1,\,-\mathrm j)^{\top}$.

⁠**Worked example 2:** The rotation $\mathbf{Q}=\bigl(\begin{smallmatrix}0.6&-0.8\\0.8&0.6\end{smallmatrix}\bigr)$ from Section [1.4](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-4) has $p(\lambda)=\lambda^2-1.2\lambda+1$ and, by the worked example on complex numbers, the eigenvalues $0.6\pm\mathrm j\,0.8=\cos\alpha\pm\mathrm j\sin\alpha=\mathrm e^{\pm\mathrm j\alpha}$ with $\alpha\approx53.13^\circ$. In general, the rotation by the angle $\alpha$ has the eigenvalues $\mathrm e^{\pm\mathrm j\alpha}$.

So a real matrix can have complex eigenvalues. Because its characteristic polynomial has real coefficients, they occur in conjugate pairs. A real eigenvector belongs only to a real eigenvalue: if $\mathbf{v}$ were real and $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$, then $\lambda\mathbf{v}$, as the image of a real vector, would be real, and hence so would $\lambda$. Complex eigenvalues indicate that the matrix rotates in a plane.

⁠**In short:** A real matrix can have complex eigenvalues, always in conjugate pairs; a rotation by $\alpha$ has the eigenvalues $\mathrm e^{\pm\mathrm j\alpha}$.

:::hintergrund Rotating means multiplying by $\mathrm e^{\mathrm j\alpha}$
For electrical engineers this result is familiar. Identify the arrow $(x_1,\,x_2)^{\top}$ with the complex number $z=x_1+\mathrm jx_2$, as with a phasor. A rotation by $\alpha$ is then multiplication by $\mathrm e^{\mathrm j\alpha}$: $\mathrm e^{\mathrm j\alpha}z=(x_1\cos\alpha-x_2\sin\alpha)+\mathrm j\,(x_1\sin\alpha+x_2\cos\alpha)$, and these are exactly the two components of $\mathbf{Q}\mathbf{x}$ for the rotation matrix from Foundations 1, Section 8.3. In complex notation, the rotation is thus a multiplication by a number, and this number is an eigenvalue. The second eigenvalue $\mathrm e^{-\mathrm j\alpha}$ belongs to the conjugate notation $z^*$, which rotates in the opposite direction.
:::

### Multiple eigenvalues

<span class="anker" id="stufe-6-7"></span>

The characteristic polynomial can have a double root. Then two of the $n$ eigenvalues coincide. How often an eigenvalue occurs is a number in its own right.

:::definition Definition 6.7 (Algebraic multiplicity)
<span class="anker" id="satz-6-7"></span>

The __algebraic multiplicity__ of an eigenvalue $\lambda$ is the multiplicity of $\lambda$ as a root of the characteristic polynomial.
:::

⁠**Worked example:** The matrix $2\mathbf{I}=\operatorname{diag}(2,\,2)$ has $p(\lambda)=(2-\lambda)^2$: the eigenvalue $2$ has algebraic multiplicity $2$. The shear $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ from Foundations 1, Section 8.3, has $p(\lambda)=(1-\lambda)^2$: the eigenvalue $1$ also has algebraic multiplicity $2$. The matrix $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ has two different eigenvalues, each with algebraic multiplicity $1$.

⁠**In short:** The algebraic multiplicity counts how often an eigenvalue occurs as a root of the characteristic polynomial.

### How many eigenvectors there are

<span class="anker" id="stufe-6-8"></span>

The two examples with a double eigenvalue behave completely differently. The matrix $2\mathbf{I}$ stretches every arrow to twice its length; every vector $\ne\mathbf{0}$ is an eigenvector, and the eigenspace is the whole plane. The shear pushes every point to the right by its height; only arrows on the $x_1$-axis stay on their line. Its eigenspace is $\ker\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$, the line in the direction of $(1,\,0)^{\top}$. The difference is the dimension of the eigenspace.

:::definition Definition 6.8 (Geometric multiplicity)
<span class="anker" id="satz-6-8"></span>

The __geometric multiplicity__ of an eigenvalue is the dimension of its eigenspace.
:::

It is at least $1$, because every eigenvalue has an eigenvector, and at most as large as the algebraic multiplicity; this chapter does not prove the second part. For $2\mathbf{I}$ both multiplicities are $2$; for the shear the algebraic one is $2$ and the geometric one is $1$: the shear is missing an eigenvector.

:::satz Theorem 6.9 (Different eigenvalues, independent eigenvectors)
<span class="anker" id="satz-6-9"></span>

Eigenvectors $\mathbf{v}_1,\dots,\mathbf{v}_k$ for pairwise different eigenvalues $\lambda_1,\dots,\lambda_k$ are linearly independent. If an $n\times n$ matrix has $n$ different eigenvalues, its eigenvectors form a basis.
:::

:::beweis Independent eigenvectors
For two eigenvectors: let $c_1\mathbf{v}_1+c_2\mathbf{v}_2=\mathbf{0}$. Applying $\mathbf{A}$ gives $c_1\lambda_1\mathbf{v}_1+c_2\lambda_2\mathbf{v}_2=\mathbf{0}$. Subtracting $\lambda_2$ times the first equation from this leaves $c_1(\lambda_1-\lambda_2)\mathbf{v}_1=\mathbf{0}$. Since $\lambda_1\ne\lambda_2$ and $\mathbf{v}_1\ne\mathbf{0}$, we get $c_1=0$, and then $c_2=0$ as well. For more eigenvectors, proceed in the same way: if there were a dependence, take one with as few nonzero coefficients as possible. Applying $\mathbf{A}$ and subtracting the dependence multiplied by $\lambda$, one of the eigenvalues involved, would give a dependence with even fewer nonzero coefficients, a contradiction.
:::

⁠**Worked example:** The eigenvectors $(1,\,1)^{\top}$ and $(1,\,-2)^{\top}$ of $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ belong to the different eigenvalues $5$ and $2$; they are linearly independent, because $\det\bigl(\begin{smallmatrix}1&1\\1&-2\end{smallmatrix}\bigr)=-3\ne0$. The shear, by contrast, has only the eigendirection $(1,\,0)^{\top}$; it does not have two independent eigenvectors.

⁠**In short:** The geometric multiplicity counts the independent eigenvectors for an eigenvalue; it can be smaller than the algebraic one, but different eigenvalues always have independent eigenvectors.

### Rules for eigenvalues

<span class="anker" id="stufe-6-9"></span>

If you know the eigenvectors of a matrix, you also know them for many matrices built from it. The rules all follow directly from [(6.1)](#gl-6-1).

:::satz Theorem 6.10 (Rules)
<span class="anker" id="satz-6-10"></span>

Let $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ with $\mathbf{v}\ne\mathbf{0}$. Then:

<ol class="rm">

<li>

$\mathbf{A}^k\mathbf{v}=\lambda^k\mathbf{v}$ for every natural number $k$;

</li>

<li>

$(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=(\lambda+\beta)\mathbf{v}$ for every number $\beta$;

</li>

<li>

$\mathbf{A}$ is invertible if and only if no eigenvalue is zero, and then $\mathbf{A}^{-1}\mathbf{v}=\frac1\lambda\mathbf{v}$;

</li>

<li>

$\mathbf{A}^{\top}$ has the same eigenvalues as $\mathbf{A}$, but in general different eigenvectors.

</li>

</ol>
:::

:::beweis Rules
(i) $\mathbf{A}^2\mathbf{v}=\mathbf{A}(\lambda\mathbf{v})=\lambda\mathbf{A}\mathbf{v}=\lambda^2\mathbf{v}$, and so on. (ii) $(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=\lambda\mathbf{v}+\beta\mathbf{v}$. (iii) By [(6.5)](#gl-6-5), $\det\mathbf{A}$ is the product of the eigenvalues, so it is nonzero exactly when no eigenvalue is zero. Multiplying $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ by $\mathbf{A}^{-1}$ gives $\mathbf{v}=\lambda\mathbf{A}^{-1}\mathbf{v}$. (iv) By Foundations 1, Section 14.5, $\det(\mathbf{A}^{\top}-\lambda\mathbf{I})=\det\bigl((\mathbf{A}-\lambda\mathbf{I})^{\top}\bigr)=\det(\mathbf{A}-\lambda\mathbf{I})$; both have the same characteristic polynomial.
:::

⁠**Worked example:** For $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$, the matrix $\mathbf{A}^2=\bigl(\begin{smallmatrix}18&7\\14&11\end{smallmatrix}\bigr)$ has the eigenvalues $25$ and $4$: $\mathbf{A}^2(1,\,1)^{\top}=(25,\,25)^{\top}$. The matrix $\mathbf{A}-5\mathbf{I}$ has the eigenvalues $0$ and $-3$ and is not invertible. The inverse $\mathbf{A}^{-1}=\tfrac1{10}\bigl(\begin{smallmatrix}3&-1\\-2&4\end{smallmatrix}\bigr)$ has the eigenvalues $\tfrac15$ and $\tfrac12$: $\mathbf{A}^{-1}(1,\,-2)^{\top}=\tfrac1{10}(5,\,-10)^{\top}=\tfrac12(1,\,-2)^{\top}$. The transpose $\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&2\\1&3\end{smallmatrix}\bigr)$ also has the eigenvalues $5$ and $2$, but $\mathbf{A}^{\top}(1,\,1)^{\top}=(6,\,4)^{\top}$: its eigenvectors are $(2,\,1)^{\top}$ and $(1,\,-1)^{\top}$.

⁠**In short:** Powers, shifts by $\beta\mathbf{I}$ and the inverse keep the eigenvectors and change the eigenvalues in the same way; the transpose keeps only the eigenvalues.

:::aufgabe Exercise 17 ★ Eigenvalues and eigenvectors
<span class="anker" id="aufg-17"></span>

Determine the eigenvalues and eigenspaces of

$$\mathbf{A}_1=\begin{pmatrix}2&2\\1&3\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}3&0\\0&3\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&1\end{pmatrix}.$$

In each case, check the trace and the determinant. For which matrix are the eigenvectors perpendicular to each other?

:::loesung
$\mathbf{A}_1$: trace $5$, determinant $6-2=4$, so $\lambda^2-5\lambda+4=(\lambda-4)(\lambda-1)$. For $\lambda=4$: $\mathbf{A}_1-4\mathbf{I}=\bigl(\begin{smallmatrix}-2&2\\1&-1\end{smallmatrix}\bigr)$, eigenspace in the direction of $(1,\,1)^{\top}$. For $\lambda=1$: $\mathbf{A}_1-\mathbf{I}=\bigl(\begin{smallmatrix}1&2\\1&2\end{smallmatrix}\bigr)$, eigenspace in the direction of $(2,\,-1)^{\top}$. Check: $4+1=5$, $4\cdot1=4$. The eigenvectors are not perpendicular: $(1,\,1)(2,\,-1)^{\top}=1$.

$\mathbf{A}_2=3\mathbf{I}$: $p(\lambda)=(3-\lambda)^2$, the eigenvalue $3$ twice; the eigenspace is the whole plane. Check: $3+3=6$, $3\cdot3=9$. You can choose two perpendicular eigenvectors, for example $\mathbf{e}_1$ and $\mathbf{e}_2$, but also two oblique ones.

$\mathbf{A}_3$: trace $2$, determinant $1-9=-8$, so $\lambda^2-2\lambda-8=(\lambda-4)(\lambda+2)$. Eigenvectors $(1,\,1)^{\top}$ for $4$ and $(1,\,-1)^{\top}$ for $-2$. Check: $4-2=2$, $4\cdot(-2)=-8$. They are perpendicular to each other; $\mathbf{A}_3$ is symmetric, and Section [7.5](diagonalisierung-und-spektralsatz.html#stufe-7-5) shows that this is no coincidence.
:::
:::

:::aufgabe Exercise 18 ★ Triangular matrices
<span class="anker" id="aufg-18"></span>

Show: the eigenvalues of an upper triangular matrix are its diagonal entries. Determine the eigenvalues and eigenvectors of $\Bigl(\begin{smallmatrix}2&1&0\\0&3&1\\0&0&5\end{smallmatrix}\Bigr)$.

:::loesung
For an upper triangular matrix, $\mathbf{A}-\lambda\mathbf{I}$ is again an upper triangular matrix, with the diagonal entries $a_{ii}-\lambda$. By Foundations 1, Section 14.4, its determinant is the product of the diagonal entries: $p(\lambda)=(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$. The roots are the diagonal entries.

For the given matrix, the eigenvalues are therefore $2$, $3$ and $5$. For $2$: $\mathbf{A}-2\mathbf{I}=\Bigl(\begin{smallmatrix}0&1&0\\0&1&1\\0&0&3\end{smallmatrix}\Bigr)$ requires $v_3=0$ and $v_2=0$, eigenvector $(1,\,0,\,0)^{\top}$. For $3$: $\Bigl(\begin{smallmatrix}-1&1&0\\0&0&1\\0&0&2\end{smallmatrix}\Bigr)$ requires $v_3=0$ and $v_2=v_1$, eigenvector $(1,\,1,\,0)^{\top}$. For $5$: $\Bigl(\begin{smallmatrix}-3&1&0\\0&-2&1\\0&0&0\end{smallmatrix}\Bigr)$ requires $v_2=3v_1$ and $v_3=2v_2$, eigenvector $(1,\,3,\,6)^{\top}$. Check: $\mathbf{A}(1,\,3,\,6)^{\top}=(2+3,\ 9+6,\ 30)^{\top}=5\,(1,\,3,\,6)^{\top}$.
:::
:::

:::aufgabe Exercise 19 ★★ Multiplicities
<span class="anker" id="aufg-19"></span>

For $\mathbf{B}_1=\bigl(\begin{smallmatrix}2&0\\0&2\end{smallmatrix}\bigr)$, $\mathbf{B}_2=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ and $\mathbf{B}_3=\Bigl(\begin{smallmatrix}1&0&0\\0&1&1\\0&0&1\end{smallmatrix}\Bigr)$, determine all eigenvalues with their algebraic and geometric multiplicities.

:::loesung
$\mathbf{B}_1=2\mathbf{I}$: eigenvalue $2$, algebraic multiplicity $2$, eigenspace the whole plane, geometric multiplicity $2$.

$\mathbf{B}_2$: triangular matrix, eigenvalue $2$ with algebraic multiplicity $2$. $\mathbf{B}_2-2\mathbf{I}=\bigl(\begin{smallmatrix}0&3\\0&0\end{smallmatrix}\bigr)$ requires $v_2=0$; the eigenspace is the $x_1$-axis, geometric multiplicity $1$. Like the shear, $\mathbf{B}_2$ is missing an eigenvector.

$\mathbf{B}_3$: triangular matrix, eigenvalue $1$ with algebraic multiplicity $3$. $\mathbf{B}_3-\mathbf{I}=\Bigl(\begin{smallmatrix}0&0&0\\0&0&1\\0&0&0\end{smallmatrix}\Bigr)$ requires only $v_3=0$; the eigenspace is $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$, geometric multiplicity $2$. Here the geometric multiplicity lies between $1$ and the algebraic one.
:::
:::

:::aufgabe Exercise 20 ★★ A rotation and a reflection
<span class="anker" id="aufg-20"></span>

<ol class="al">

<li>

Compute the eigenvalues of the rotation by $30^\circ$ and write them in the form $\mathrm e^{\pm\mathrm j\alpha}$.

</li>

<li>

The reflection $\bigl(\begin{smallmatrix}0.6&0.8\\0.8&-0.6\end{smallmatrix}\bigr)$ from Section [1.5](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-5) is also orthogonal. Determine its eigenvalues and eigenvectors and interpret them geometrically.

</li>

<li>

Show: every real eigenvalue of an orthogonal matrix is $1$ or $-1$.

</li>

</ol>

:::loesung
(a) The rotation by $30^\circ$ is $\bigl(\begin{smallmatrix}\sqrt3/2&-1/2\\1/2&\sqrt3/2\end{smallmatrix}\bigr)$ with trace $\sqrt3$ and determinant $1$. So $p(\lambda)=\lambda^2-\sqrt3\,\lambda+1$ and

$$\lambda=\frac{\sqrt3\pm\sqrt{3-4}}2=\frac{\sqrt3}2\pm\mathrm j\,\frac12=\cos30^\circ\pm\mathrm j\sin30^\circ=\mathrm e^{\pm\mathrm j\,30^\circ} .$$

(b) Trace $0$, determinant $-0.36-0.64=-1$, so $p(\lambda)=\lambda^2-1$ with the eigenvalues $1$ and $-1$. For $1$: $\bigl(\begin{smallmatrix}-0.4&0.8\\0.8&-1.6\end{smallmatrix}\bigr)$, eigenvector $(2,\,1)^{\top}$. For $-1$: $\bigl(\begin{smallmatrix}1.6&0.8\\0.8&0.4\end{smallmatrix}\bigr)$, eigenvector $(1,\,-2)^{\top}$. Geometrically: the points of the axis of reflection in the direction of $(2,\,1)^{\top}$ stay fixed, and the eigenvalue is $1$; the direction perpendicular to it is flipped over, and the eigenvalue is $-1$. The two eigenvectors are perpendicular because the matrix is symmetric.

(c) Let $\mathbf{Q}\mathbf{v}=\lambda\mathbf{v}$ with real $\lambda$ and real $\mathbf{v}\ne\mathbf{0}$. By [(1.3)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-3), $\lVert\mathbf{v}\rVert=\lVert\mathbf{Q}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$, so $|\lambda|=1$ and $\lambda=\pm1$. A rigid motion can only leave an arrow on its line as it is or flip it over; it cannot stretch it.
:::
:::
