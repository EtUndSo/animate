---
title: The Hessian matrix and the quadratic approximation
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15230900
summary: The gradient describes the tilt of the terrain, but not its curvature.
tags: second partial derivatives, Hessian matrix, mixed difference, second directional derivative
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
The gradient describes the tilt of the terrain, but not its curvature. The Hessian matrix collects the second partial derivatives. It is symmetric, and with it the linear approximation becomes the quadratic one. Its eigenvalues tell how strongly the terrain curves in different directions, and they connect this section with the quadratic forms from [Chapter 2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html).
:::

### Second partial derivatives

<span class="anker" id="stufe-8-1"></span>

The partial derivatives $\partial_jf$ are themselves functions of $\mathbf{x}$. You can differentiate them partially once more, with respect to the same variable or a different one. This describes how the slope in the $x_j$ direction changes as you move on in the $x_i$ direction.

:::definition Definition 8.1 (Second partial derivatives)
<span class="anker" id="satz-8-1"></span>

The __second partial derivatives__ of $f:\mathbb{R}^d\to\mathbb{R}$ are

<span class="anker" id="gl-8-1"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial}{\partial x_i}\Bigl(\frac{\partial f}{\partial x_j}\Bigr), \tag{8.1}$$

differentiated first with respect to $x_j$, then with respect to $x_i$. For $i=j$ you write $\partial^2f/\partial x_i^2$. For $i\ne j$ they are called mixed partial derivatives.
:::

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$, $\partial_1f=2x_1x_2$ and $\partial_2f=x_1^2+2x_2$, so

$$\begin{gathered} \frac{\partial^2f}{\partial x_1^2}=\frac{\partial}{\partial x_1}(2x_1x_2)=2x_2,\qquad \frac{\partial^2f}{\partial x_2\,\partial x_1}=\frac{\partial}{\partial x_2}(2x_1x_2)=2x_1,\\ \frac{\partial^2f}{\partial x_1\,\partial x_2}=\frac{\partial}{\partial x_1}(x_1^2+2x_2)=2x_1,\qquad \frac{\partial^2f}{\partial x_2^2}=\frac{\partial}{\partial x_2}(x_1^2+2x_2)=2 . \end{gathered}$$

At the point $(1,\,2)$ these are $4$, $2$, $2$ and $2$. The two mixed derivatives are equal, although they arose in different ways.
::::

⁠**In short:** Second partial derivatives differentiate a partial derivative partially once more; the mixed ones describe how the slope in one direction changes as you walk in another direction.

### The Hessian matrix

<span class="anker" id="stufe-8-2"></span>

A function of $d$ variables has $d^2$ second partial derivatives. Just as the first derivatives are gathered in the gradient, you gather these in one object, here in a square matrix.

:::definition Definition 8.2 (Hessian matrix)
<span class="anker" id="satz-8-2"></span>

The $d\times d$ matrix

<span class="anker" id="gl-8-2"></span>
$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2}&\cdots&\dfrac{\partial^2f}{\partial x_1\,\partial x_d}\\ \vdots&&\vdots\\ \dfrac{\partial^2f}{\partial x_d\,\partial x_1}&\cdots&\dfrac{\partial^2f}{\partial x_d^2}\end{pmatrix},\qquad \bigl(\mathbf{H}_f(\mathbf{x})\bigr)_{ij}=\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}), \tag{8.2}$$

is called the __Hessian matrix__ of $f$ at the point $\mathbf{x}$.
:::

The matrix is named after the mathematician Otto Hesse; some books write $\nabla^2f$. Its column $j$ is the gradient of the function $\partial_jf$. It is therefore closely related to the Jacobian matrix of the gradient, that is, of the vector-valued function $\mathbf{x}\mapsto\nabla f(\mathbf{x})$: entry $(i,j)$ of that Jacobian matrix is $\partial(\partial_if)/\partial x_j$, the derivative in the other order. The next subsection shows that both orders almost always give the same result; then the Hessian matrix is the Jacobian matrix of the gradient.

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$, by the previous subsection,

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}2x_2&2x_1\\2x_1&2\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}4&2\\2&2\end{pmatrix}.$$

For a quadratic function $f(\mathbf{x})=\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$ with symmetric $\mathbf{A}$, Section [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) gives $\nabla f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$ and therefore $\mathbf{H}_f=\mathbf{A}$ at every point. For the bowl $x_1^2+4x_2^2$ from Section [4](richtungsableitung-und-steilster-anstieg.html#stufe-4), $\mathbf{A}=\operatorname{diag}(2,\,8)$.
::::

⁠**In short:** The Hessian matrix collects all second partial derivatives; for a quadratic function $\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$ it is $\mathbf{A}$ everywhere.

### Schwarz's theorem

<span class="anker" id="stufe-8-3"></span>

In the worked example, the two mixed derivatives were equal. That is no coincidence; it holds for all functions whose second derivatives have no jumps.

:::satz Theorem 8.3 (Schwarz's theorem)
<span class="anker" id="satz-8-3"></span>

If all second partial derivatives of $f$ exist near $\mathbf{x}$ and are continuous at the point $\mathbf{x}$, then at that point

<span class="anker" id="gl-8-3"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial^2f}{\partial x_j\,\partial x_i} \tag{8.3}$$

for all $i,j$. The Hessian matrix is then symmetric.
:::

You can see the reason in a calculation in which the order does not appear at all. You move from $\mathbf{x}$ by $h$ in the $x_1$ direction and by $k$ in the $x_2$ direction and form the __mixed difference__

$$\Delta(h,k)=f(x_1+h,\,x_2+k)-f(x_1+h,\,x_2)-f(x_1,\,x_2+k)+f(x_1,\,x_2).$$

If you group the first term with the third and the second with the fourth, then $\Delta$ is the change in the difference $f(x_1+h,\cdot)-f(x_1,\cdot)$ under the step $k$ in the $x_2$ direction: how does the rise in the $x_1$ direction change as you walk in the $x_2$ direction? Divided by $hk$, this approaches, for small $h$ and $k$, the derivative first with respect to $x_1$, then with respect to $x_2$. If instead you group the first two and the last two terms, you read the same number as the change in the rise in the $x_2$ direction under the step in the $x_1$ direction, and the quotient approaches the derivative in the other order. Both limits belong to the same number $\Delta/(hk)$. Continuity ensures that the order of the two passages to the limit does not matter.

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$ at the point $(1,\,2)$ with $h=k=0.1$,

$$\Delta=f(1.1,\ 2.1)-f(1.1,\ 2)-f(1,\ 2.1)+f(1,2)=6.951-6.42-6.51+6=0.021,$$

so $\Delta/(hk)=2.1$, close to the mixed derivative $2x_1=2$. The deviation arises because $2x_1$ is not constant between $x_1=1$ and $x_1=1.1$.
::::

⁠**In short:** With continuous second derivatives, the order of differentiation does not matter, and the Hessian matrix is symmetric.

:::hintergrund When the second derivatives are not continuous
Without continuity, the theorem can fail. The classic counterexample is $f(x_1,x_2)=x_1x_2\,\frac{x_1^2-x_2^2}{x_1^2+x_2^2}$ with $f(0,0)=0$. If you compute the first partial derivatives on the axes, you get $\partial_1f(0,x_2)=-x_2$ and $\partial_2f(x_1,0)=x_1$. Differentiating the first with respect to $x_2$ gives $-1$ at the origin; differentiating the second with respect to $x_1$ gives $+1$. So the mixed derivatives at the origin differ, because the second derivatives jump there. For the functions in this chapter that have no kink, this does not happen; they are built from polynomials, exponential functions and basic arithmetic operations, and wherever they are defined, they have continuous derivatives of any order.
:::

### The quadratic approximation

<span class="anker" id="stufe-8-4"></span>

In one variable, the tangent line was improved by a parabola in Section [1.5](die-ableitung.html#stufe-1-5). With several variables, the tangent plane is replaced by a curved surface whose curvature is described by the Hessian matrix.

:::satz Theorem 8.4 (Quadratic approximation)
<span class="anker" id="satz-8-4"></span>

If $f$ has continuous second partial derivatives near $\mathbf{x}$, then

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x}+\mathbf{h})=f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{h}+r_2(\mathbf{h})\qquad\text{with}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{r_2(\mathbf{h})}{\lVert\mathbf{h}\rVert^2}=0 . \tag{8.4}$$
:::

:::herleitung The quadratic approximation along a line
Restrict $f$ to the line through $\mathbf{x}$ in the direction $\mathbf{h}$: $\phi(t)=f(\mathbf{x}+t\,\mathbf{h})$. This is a function of one variable. By [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4), $\phi'(t)=\nabla f(\mathbf{x}+t\mathbf{h})^{\top}\mathbf{h}=\sum_jh_j\,\partial_jf(\mathbf{x}+t\mathbf{h})$. You differentiate each term once more with [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4), this time for the function $\partial_jf$:

$$\phi''(t)=\sum_{j=1}^dh_j\sum_{i=1}^d\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}+t\mathbf{h})\,h_i=\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x}+t\mathbf{h})\,\mathbf{h} .$$

The quadratic approximation [(1.6)](die-ableitung.html#gl-1-6) of $\phi$ at the point $0$, evaluated at $t=1$, reads $\phi(1)\approx\phi(0)+\phi'(0)+\tfrac12\phi''(0)$, and that is [(8.4)](#gl-8-4). That the error vanishes faster than $\lVert\mathbf{h}\rVert^2$ follows from the continuity of the second derivatives.
:::

The new term $\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$ is a quadratic form in the sense of [Chapter 2, Section 5.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1), with the Hessian matrix as its matrix. Near $\mathbf{x}$, the function therefore looks like a plane plus a quadratic form.

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$ at the point $(1,\,2)$ and $\mathbf{h}=(0.01,\ 0.02)^{\top}$ as in Section [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4),

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(4\cdot0.01^2+2\cdot2\cdot0.01\cdot0.02+2\cdot0.02^2\bigr)=\tfrac12\,(0.0004+0.0008+0.0008)=0.001$$

(Fig. [15](#abb-15)). The quadratic approximation is $6+0.14+0.001=6.141$, the exact value $6.141002$. The error dropped from $0.001002$ to $0.000002$. The remainder is the third-order term: $x_1^2x_2$ contains the term $h_1^2h_2=0.0001\cdot0.02=0.000002$, which no quadratic approximation captures.

:::abbildung ml/k3rtaylor2 15
The curvature term of the quadratic approximation as a double sum; the two mixed terms $h_1\cdot2\cdot h_2$ and $h_2\cdot2\cdot h_1$ are combined into the middle term.
:::
::::

⁠**In short:** Near $\mathbf{x}$, $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{h}$: a plane plus a quadratic form.

### The curvature in a direction

<span class="anker" id="stufe-8-5"></span>

How strongly is the terrain curved if you walk from $\mathbf{x}$ in the direction $\mathbf{u}$? The derivation in the previous subsection has already given the answer: the second derivative of $\phi(t)=f(\mathbf{x}+t\mathbf{u})$ at the point $0$ is $\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{u}$.

:::definition Definition 8.5 (Curvature in a direction)
<span class="anker" id="satz-8-5"></span>

For a vector $\mathbf{u}$ of length $1$,

<span class="anker" id="gl-8-5"></span>
$$\frac{\mathrm{d}^2}{\mathrm{d} t^2}f(\mathbf{x}+t\,\mathbf{u})\Big|_{t=0}=\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u} \tag{8.5}$$

is called the __second directional derivative__ of $f$ at the point $\mathbf{x}$ in the direction $\mathbf{u}$. It measures the curvature of the cross-section curve in this direction.
:::

With the results from [Chapter 2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html), you can say right away how large this curvature is at most and at least. The Hessian matrix is symmetric and, by the spectral theorem from [Chapter 2, Section 7.6](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-6), has real eigenvalues and mutually perpendicular eigenvectors.

:::satz Theorem 8.6 (Curvature and eigenvalues)
<span class="anker" id="satz-8-6"></span>

Let $\lambda_{\min}$ and $\lambda_{\max}$ be the smallest and the largest eigenvalue of the symmetric Hessian matrix $\mathbf{H}_f(\mathbf{x})$. Then for every direction $\mathbf{u}$ with $\lVert\mathbf{u}\rVert=1$

<span class="anker" id="gl-8-6"></span>
$$\lambda_{\min}\le\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u}\le\lambda_{\max}. \tag{8.6}$$

In the direction of an eigenvector, the curvature is exactly the corresponding eigenvalue. If $\mathbf{H}_f(\mathbf{x})$ is positive definite, the curvature is positive in every direction; if it is indefinite, the terrain curves upward in some directions and downward in others.
:::

The inequality is the statement about the largest and smallest value of a quadratic form on the unit circle from [Chapter 2, Section 8.5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-5). For an eigenvector $\mathbf{u}$ for the eigenvalue $\lambda$, $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\lambda\,\mathbf{u}^{\top}\mathbf{u}=\lambda$. The terms positive definite and indefinite come from [Chapter 2, Section 8](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8); there, the shape of a quadratic form could be read off from its eigenvalues, as a bowl, a trough or a saddle. Via the quadratic approximation [(8.4)](#gl-8-4), this carries over to the terrain near $\mathbf{x}$: for a positive definite Hessian matrix, the contour lines of the curvature term are ellipses whose principal axes, by [Chapter 2, Section 7.7](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-7), lie along the eigenvectors and are short in the direction of strong curvature.

::::beispiel [Worked example 1]
For the bowl $f(\mathbf{x})=x_1^2+4x_2^2$, $\mathbf{H}_f=\operatorname{diag}(2,\,8)$ with the eigenvalues $2$ and $8$. In the $x_1$ direction the curvature is $2$, in the $x_2$ direction it is $8$, and in the direction $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$ it is $\tfrac12(2+8)=5$. This explains the elongated contour lines from Section [4.4](richtungsableitung-und-steilster-anstieg.html#stufe-4-4): in the $x_2$ direction, the bowl curves four times as strongly, its walls are steeper there, and the ellipses are narrow in this direction.
::::

::::beispiel [Worked example 2]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$ at the point $(1,\,2)$, $\mathbf{H}_f=\bigl(\begin{smallmatrix}4&2\\2&2\end{smallmatrix}\bigr)$. By [Chapter 2, Section 6.5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5), trace $6$ and determinant $4$ give the eigenvalues $3\pm\sqrt5$, that is, about $5.236$ and $0.764$. Both are positive, so the Hessian matrix is positive definite: near $(1,\,2)$, the terrain curves upward in every direction. In the direction $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$, the curvature is

$$\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\tfrac12\,(4+2+2+2)=5,$$

and it lies between $0.764$ and $5.236$ (Fig. [16](#abb-16)).

:::abbildung ml/k3rkruemmung 16
The curvature of $f(\mathbf{x})=x_1^2x_2+x_2^2$ at the point $(1,\,2)$ in the direction of the angle bisector; the factor $\tfrac12$ comes from $u_iu_j=\tfrac12$.
:::
::::

⁠**In short:** The curvature in the direction $\mathbf{u}$ is $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$; it lies between the smallest and the largest eigenvalue of the Hessian matrix, and their signs decide whether the terrain curves like a bowl or like a saddle.

:::hintergrund The Hessian-vector product without the Hessian matrix
With many variables, the Hessian matrix is huge: with a million variables, it has $10^{12}$ entries. Often, however, you only need its product with a vector $\mathbf{v}$. You can get it without setting up the matrix. The number $\nabla f(\mathbf{x})^{\top}\mathbf{v}=\sum_jv_j\,\partial_jf(\mathbf{x})$ is a function of $\mathbf{x}$, and its gradient has the components $\sum_jv_j\,\partial^2f/\partial x_i\partial x_j$, so $\nabla_{\mathbf{x}}\bigl(\nabla f(\mathbf{x})^{\top}\mathbf{v}\bigr)=\mathbf{H}_f(\mathbf{x})\,\mathbf{v}$. For $f(\mathbf{x})=x_1^2x_2+x_2^2$ and $\mathbf{v}=(1,\,1)^{\top}$, $\nabla f^{\top}\mathbf{v}=2x_1x_2+x_1^2+2x_2$ with the gradient $(2x_2+2x_1,\ 2x_1+2)^{\top}$, which at the point $(1,\,2)$ is $(6,\,4)^{\top}$, and that is $\mathbf{H}_f\mathbf{v}=(4+2,\ 2+2)^{\top}$. So you compute two gradients instead of a matrix with $d^2$ entries.
:::

:::aufgabe Exercise 28 ★ Hessian matrices
<span class="anker" id="aufg-28"></span>

Compute the Hessian matrix at the given point and check its symmetry.

<ol class="al">

<li>

$f(\mathbf{x})=x_1^3+x_1x_2^2$ at the point $(1,\,2)$;

</li>

<li>

$f(\mathbf{x})=\mathrm{e}^{x_1+2x_2}$ at the point $(0,\,0)$. What is the rank of the matrix?

</li>

<li>

$f(\mathbf{x})=x_1x_2x_3$ at the point $(1,\,2,\,3)$.

</li>

</ol>

:::loesung
(a) $\partial_1f=3x_1^2+x_2^2$ and $\partial_2f=2x_1x_2$, so

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}6x_1&2x_2\\2x_2&2x_1\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}6&4\\4&2\end{pmatrix};$$

the mixed derivatives $\partial_2(3x_1^2+x_2^2)=2x_2$ and $\partial_1(2x_1x_2)=2x_2$ are equal.

(b) With $f=\mathrm{e}^{x_1+2x_2}$, we have $\partial_1f=f$ and $\partial_2f=2f$, so $\mathbf{H}_f=f\cdot\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, and at the origin $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$. The second row is twice the first; the rank is $1$, and the eigenvalues are $5$ and $0$. This fits: $f$ depends only on $x_1+2x_2$ and is constant along the direction $(2,\,-1)^{\top}$, so it is not curved there.

(c) $\partial_1f=x_2x_3$, $\partial_2f=x_1x_3$, $\partial_3f=x_1x_2$, so

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}0&x_3&x_2\\x_3&0&x_1\\x_2&x_1&0\end{pmatrix},\qquad \mathbf{H}_f(1,2,3)=\begin{pmatrix}0&3&2\\3&0&1\\2&1&0\end{pmatrix}.$$
:::
:::

:::aufgabe Exercise 29 ★★ Quadratic approximation
<span class="anker" id="aufg-29"></span>

Let $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ as in Exercise [10](partielle-ableitungen-und-der-gradient.html#aufg-10).

<ol class="al">

<li>

Compute $\mathbf{H}_f(2,0)$.

</li>

<li>

Use the quadratic approximation at the point $(2,\,0)$ to compute an approximation for $f(2.1,\ -0.05)$, and compare it with the linear approximation from Exercise [10](partielle-ableitungen-und-der-gradient.html#aufg-10) and with the exact value.

</li>

</ol>

:::loesung
(a) $\partial_1^2f=0$, $\partial_1\partial_2f=\mathrm{e}^{x_2}$, $\partial_2^2f=x_1\mathrm{e}^{x_2}$, so $\mathbf{H}_f(2,0)=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$.

(b) With $\mathbf{h}=(0.1,\ -0.05)^{\top}$,

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(0+2\cdot1\cdot0.1\cdot(-0.05)+2\cdot0.05^2\bigr)=\tfrac12\,(-0.01+0.005)=-0.0025 .$$

The quadratic approximation is $2+0-0.0025=1.9975$, the linear one was $2.0$, and the exact value is $1.997582$. The error drops from $0.0024$ to $0.00008$. The cross term $-0.005$ is the interaction from Exercise [10](partielle-ableitungen-und-der-gradient.html#aufg-10).
:::
:::

:::aufgabe Exercise 30 ★★ Curvatures of a skewed bowl
<span class="anker" id="aufg-30"></span>

Let $f(\mathbf{x})=x_1^2+4x_2^2+x_1x_2$.

<ol class="al">

<li>

Write $f$ as $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ and give $\mathbf{H}$.

</li>

<li>

Compute the eigenvalues of $\mathbf{H}$ and the curvatures in the directions $\mathbf{e}_1$, $\mathbf{e}_2$ and $(1,\,-1)^{\top}/\sqrt2$. Check [(8.6)](#gl-8-6).

</li>

<li>

In which direction is the curvature largest? Give an eigenvector.

</li>

</ol>

:::loesung
(a) $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ with $\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&8\end{smallmatrix}\bigr)$ gives $\tfrac12\,(2x_1^2+2x_1x_2+8x_2^2)=x_1^2+x_1x_2+4x_2^2$. This is also the Hessian matrix of $f$.

(b) Trace $10$, determinant $16-1=15$, so $\lambda^2-10\lambda+15=0$ and $\lambda=5\pm\sqrt{10}$, about $8.162$ and $1.838$. The curvatures are $\mathbf{e}_1^{\top}\mathbf{H}\mathbf{e}_1=2$, $\mathbf{e}_2^{\top}\mathbf{H}\mathbf{e}_2=8$ and, for $\mathbf{u}=(1,\,-1)^{\top}/\sqrt2$, $\tfrac12\,(2-1-1+8)=4$. All three lie between $1.838$ and $8.162$.

(c) The curvature is largest in the direction of an eigenvector for $\lambda=5+\sqrt{10}$. The first row of $(\mathbf{H}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ gives $(2-\lambda)v_1+v_2=0$, so $\mathbf{v}=(1,\ 3+\sqrt{10})^{\top}\approx(1,\ 6.162)^{\top}$, normalized about $(0.160,\ 0.987)^{\top}$. This is almost the $x_2$-direction, rotated slightly by the cross term $x_1x_2$.
:::
:::

:::aufgabe Exercise 31 ★★★ Different mixed derivatives
<span class="anker" id="aufg-31"></span>

Let $f(x_1,x_2)=x_1x_2\,\dfrac{x_1^2-x_2^2}{x_1^2+x_2^2}$ for $\mathbf{x}\ne\mathbf{0}$ and $f(0,0)=0$.

<ol class="al">

<li>

Use the difference quotient to show that $\partial_1f(0,x_2)=-x_2$ for $x_2\ne0$ and $\partial_1f(0,0)=0$. Compute $\partial_2f(x_1,0)$ in the same way.

</li>

<li>

Conclude that the two mixed derivatives at the origin are $-1$ and $+1$. Which hypothesis of Schwarz's theorem is violated?

</li>

</ol>

:::loesung
(a) On the axis $x_1=0$, $f=0$. For $x_2\ne0$,

$$\partial_1f(0,x_2)=\lim_{h\to0}\frac{f(h,x_2)-0}{h}=\lim_{h\to0}x_2\,\frac{h^2-x_2^2}{h^2+x_2^2}=x_2\cdot\frac{-x_2^2}{x_2^2}=-x_2 .$$

At the origin, $f(h,0)=0$, so $\partial_1f(0,0)=0$; the formula $-x_2$ thus also holds for $x_2=0$. Likewise, $\partial_2f(x_1,0)=\lim_k x_1\frac{x_1^2-k^2}{x_1^2+k^2}=x_1$.

(b) Differentiating first with respect to $x_1$, then with respect to $x_2$: $\frac{\partial}{\partial x_2}(-x_2)=-1$. First with respect to $x_2$, then with respect to $x_1$: $\frac{\partial}{\partial x_1}(x_1)=+1$. The mixed derivatives at the origin are different. What is violated is the continuity of the second derivatives at the origin: away from the origin, the mixed derivative is $-1$ everywhere on the $x_2$-axis and $+1$ everywhere on the $x_1$-axis. So it jumps at the origin, and the two orders of differentiation approach the origin from different sides.
:::
:::
