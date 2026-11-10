---
title: The chain rule for several variables
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15230700
summary: Calculations with many variables are chains of functions with many inputs and outputs.
tags: curve, velocity vector
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
Calculations with many variables are chains of functions with many inputs and outputs. The chain rule carries over to them: the Jacobian matrices of the stages are multiplied. Componentwise, this means that you sum over all paths along which a change travels from an input to the output. For the gradient of a number, the transposed Jacobian matrix appears.
:::

### The chain rule as a matrix product

<span class="anker" id="stufe-6-1"></span>

Suppose two stages are connected in series: $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ turns $\mathbf{x}$ into the intermediate vector $\mathbf{u}=\mathbf{g}(\mathbf{x})$, and $\mathbf f:\mathbb{R}^m\to\mathbb{R}^p$ turns that into $\mathbf{y}=\mathbf f(\mathbf{u})$. You follow a small change $\Delta\mathbf{x}$ as in Section [2.2](die-kettenregel.html#stufe-2-2). By [(5.3)](die-jacobi-matrix.html#gl-5-3), the first stage passes it on as $\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$, the second as $\Delta\mathbf{y}\approx\mathbf{J}_{\mathbf f}\,\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$. The product of two numbers becomes the product of two matrices. This fits [Chapter 1, Section 9.4](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-4): two linear stages in a row form one linear stage whose matrix is the product of the two matrices.

:::satz Theorem 6.1 (Chain rule for several variables)
<span class="anker" id="satz-6-1"></span>

If $\mathbf{g}$ is differentiable at the point $\mathbf{x}$ and $\mathbf f$ is differentiable at the point $\mathbf{g}(\mathbf{x})$, then $\mathbf f\circ\mathbf{g}$ is differentiable at the point $\mathbf{x}$, and

<span class="anker" id="gl-6-1"></span>
$$\mathbf{J}_{\mathbf f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_{\mathbf f}\bigl(\mathbf{g}(\mathbf{x})\bigr)\,\mathbf{J}_{\mathbf{g}}(\mathbf{x}). \tag{6.1}$$
:::

The shapes fit together: on the left is a $p\times n$ matrix, on the right a $p\times m$ matrix times an $m\times n$ matrix. The common number $m$ is the number of intermediate variables. As with one variable, each Jacobian matrix is evaluated where its stage operates, so $\mathbf{J}_{\mathbf f}$ at the intermediate value $\mathbf{u}=\mathbf{g}(\mathbf{x})$. For longer chains $\mathbf f_L\circ\dots\circ\mathbf f_1$, the Jacobian matrix is the product $\mathbf{J}_{\mathbf f_L}\cdots\mathbf{J}_{\mathbf f_1}$, with the stage applied last on the far left. Unlike with numbers, you may not swap the factors.

:::beweis Chain rule for several variables
The proof goes as in Section [2.2](die-kettenregel.html#stufe-2-2), with lengths instead of absolute values. With $\mathbf{u}=\mathbf{g}(\mathbf{x})$ and $\mathbf{k}=\mathbf{g}(\mathbf{x}+\mathbf{h})-\mathbf{u}=\mathbf{J}_{\mathbf{g}}\mathbf{h}+\mathbf{r}_{\mathbf{g}}(\mathbf{h})$,

$$\mathbf f\bigl(\mathbf{g}(\mathbf{x}+\mathbf{h})\bigr)-\mathbf f(\mathbf{u})=\mathbf{J}_{\mathbf f}\,\mathbf{k}+\mathbf{r}_{\mathbf f}(\mathbf{k})=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}\,\mathbf{h}+\mathbf{J}_{\mathbf f}\,\mathbf{r}_{\mathbf{g}}(\mathbf{h})+\mathbf{r}_{\mathbf f}(\mathbf{k}).$$

The middle error vanishes faster than $\lVert\mathbf{h}\rVert$, because $\mathbf{r}_{\mathbf{g}}$ does and multiplication by a fixed matrix enlarges lengths by at most a fixed factor. The last one vanishes faster than $\lVert\mathbf{k}\rVert$, and $\lVert\mathbf{k}\rVert$ is at most a fixed multiple of $\lVert\mathbf{h}\rVert$ once $\mathbf{h}$ is small. So $\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$ is the matrix of the linear approximation of $\mathbf f\circ\mathbf{g}$.
:::

::::beispiel [Worked example]
Let $\mathbf{g}$ be as in [(5.1)](die-jacobi-matrix.html#gl-5-1) and $f(\mathbf{u})=u_1^2+3u_2$, a function with one output ($p=1$). Their composition is $F(\mathbf{x})=f(\mathbf{g}(\mathbf{x}))=x_1^2x_2^2+6x_1+3x_2^2$. At the point $\mathbf{x}=(1,\,2)^{\top}$, $\mathbf{u}=\mathbf{g}(\mathbf{x})=(2,\,6)^{\top}$ and $\mathbf{J}_f(\mathbf{u})=(2u_1\ \ 3)=(4\ \ 3)$. By [(6.1)](#gl-6-1),

$$\mathbf{J}_F(1,2)=\begin{pmatrix}4&3\end{pmatrix}\begin{pmatrix}2&1\\2&4\end{pmatrix}=\begin{pmatrix}4\cdot2+3\cdot2&\ 4\cdot1+3\cdot4\end{pmatrix}=\begin{pmatrix}14&16\end{pmatrix}.$$

Check with the written-out function: $\partial_1F=2x_1x_2^2+6=8+6=14$ and $\partial_2F=2x_1^2x_2+6x_2=4+12=16$.
::::

⁠**In short:** The Jacobian matrix of a composition is the product of the Jacobian matrices of the stages, with the stage applied last on the left: $\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}$.

### Sum over all paths

<span class="anker" id="stufe-6-2"></span>

If you write out the matrix product [(6.1)](#gl-6-1) for one entry, you get a sum over the intermediate variables. For a function $F=f\circ\mathbf{g}$ with one output,

<span class="anker" id="gl-6-2"></span>
$$\frac{\partial F}{\partial x_j}(\mathbf{x})=\sum_{i=1}^m\frac{\partial f}{\partial u_i}(\mathbf{u})\,\frac{\partial u_i}{\partial x_j}(\mathbf{x}),\qquad \mathbf{u}=\mathbf{g}(\mathbf{x}). \tag{6.2}$$

This sum has an intuitive meaning. A change in $x_j$ does not reach $F$ directly but via the intermediate variables $u_1,\dots,u_m$. Each intermediate variable is a path: on the path via $u_i$, the change is multiplied first by $\partial u_i/\partial x_j$ and then by $\partial f/\partial u_i$. At the output, the contributions of all paths arrive and add up (Fig. [11](#abb-11)). That is why the chain rule is often summarized as: multiply along a path, sum over all paths.

:::abbildung ml/k3wege 11
The chain rule as a network of paths for $F=f\circ\mathbf{g}$ at the point $(1,\,2)$. Each edge carries the local derivative of its target with respect to its starting point. From $x_1$, two paths lead to $F$: via $u_1$ (blue) and via $u_2$ (orange). Along each path the factors are multiplied, and the two contributions are added. You can picture a pipe network in which each pipe multiplies the quantity flowing through it by its factor and the flows merge at the target.
:::

::::beispiel [Worked example 1]
For $F=f\circ\mathbf{g}$ from the previous subsection, the edge factors at the point $(1,\,2)$ are

$$\frac{\partial u_1}{\partial x_1}=x_2=2,\quad \frac{\partial u_1}{\partial x_2}=x_1=1,\quad \frac{\partial u_2}{\partial x_1}=2,\quad \frac{\partial u_2}{\partial x_2}=2x_2=4,\quad \frac{\partial f}{\partial u_1}=2u_1=4,\quad \frac{\partial f}{\partial u_2}=3 .$$

Summed over both paths, this gives the entries $14$ and $16$, as in the matrix product (Fig. [12](#abb-12)).

:::abbildung ml/k3rwege 12
The partial derivatives of $F=f\circ\mathbf{g}$ at the point $(1,\,2)$ as sums over the two paths through $u_1$ and $u_2$.
:::
::::

::::beispiel [Worked example 2]
One input, two paths. Let $F(x)=g_1(x)\,g_2(x)$ with $g_1(x)=x^2$ and $g_2(x)=3x$, so $f(\mathbf{u})=u_1u_2$. The paths via $u_1$ and $u_2$ give

$$\frac{\mathrm{d} F}{\mathrm{d} x}=\frac{\partial f}{\partial u_1}\,g_1'(x)+\frac{\partial f}{\partial u_2}\,g_2'(x)=u_2\cdot2x+u_1\cdot3=3x\cdot2x+x^2\cdot3=9x^2 .$$

Check: $F(x)=3x^3$ has the derivative $9x^2$. If you forget one path, you get $6x^2$ or $3x^2$. Incidentally, this is exactly the product rule [(1.5)](die-ableitung.html#gl-1-5): it is the chain rule for two paths.
::::

⁠**In short:** Componentwise, the chain rule is a sum over all paths from the input to the output; along each path, the local derivatives are multiplied.

:::hintergrund Why you sum over the paths
The reason is the observation from Section [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4): for small changes, the effects add up. If you change $x_j$ by $\Delta x_j$, all intermediate variables change at once, each by approximately $\frac{\partial u_i}{\partial x_j}\Delta x_j$. How these simultaneous changes affect $f$ is given by the linear approximation of $f$ in the variables $u_1,\dots,u_m$: each contributes $\frac{\partial f}{\partial u_i}\Delta u_i$, and the contributions add up as if each intermediate variable had changed alone. The sum over the paths is therefore the sum of these individual contributions. In longer chains this continues: a path then passes through several intermediate variables one after another, along the path you multiply all edge factors, and at the end you sum over all paths from the input to the output. The number of paths can grow very quickly; Section [10](automatische-differentiation.html#stufe-10) shows how to combine them cleverly.
:::

### The gradient of a composition

<span class="anker" id="stufe-6-3"></span>

For a function $F=f\circ\mathbf{g}$ with one output, the Jacobian matrix is the gradient as a row. If you want the gradient as a column, as this chapter has agreed, you must transpose the chain rule.

:::satz Theorem 6.2 (Gradient of a composition)
<span class="anker" id="satz-6-2"></span>

If $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ is differentiable at the point $\mathbf{x}$ and $f:\mathbb{R}^m\to\mathbb{R}$ is differentiable at the point $\mathbf{u}=\mathbf{g}(\mathbf{x})$, then

<span class="anker" id="gl-6-3"></span>
$$\nabla(f\circ\mathbf{g})(\mathbf{x})=\mathbf{J}_{\mathbf{g}}(\mathbf{x})^{\top}\,\nabla f(\mathbf{u}). \tag{6.3}$$
:::

:::beweis Gradient of a composition
By [(6.1)](#gl-6-1), $\nabla(f\circ\mathbf{g})(\mathbf{x})^{\top}=\mathbf{J}_{f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_f(\mathbf{u})\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\nabla f(\mathbf{u})^{\top}\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})$. Transposing both sides with the rule $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ from [Chapter 1, Section 10.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1), gives the claim.
:::

The transpose is pure bookkeeping: it arises because the gradient is written as a column, while the rows of the Jacobian matrix belong to the outputs. In content, [(6.3)](#gl-6-3) says the same as [(6.2)](#gl-6-2): component $j$ of $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ is column $j$ of $\mathbf{J}_{\mathbf{g}}$ times $\nabla f$, that is, the sum over the paths starting at $x_j$. If the inner function is linear, $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}$, then by Section [5.4](die-jacobi-matrix.html#stufe-5-4) this becomes the rule $\nabla_{\mathbf{x}}f(\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\,\nabla f(\mathbf{A}\mathbf{x})$. The subscript $\mathbf{x}$ on the nabla says with respect to which variable the gradient is taken.

::::beispiel [Worked example]
With $\mathbf{J}_{\mathbf{g}}(1,2)$ and $\nabla f(\mathbf{u})=(4,\,3)^{\top}$ from the example for [(6.1)](#gl-6-1),

$$\nabla F(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}^{\top}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}2&2\\1&4\end{pmatrix}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}8+6\\4+12\end{pmatrix}=\begin{pmatrix}14\\16\end{pmatrix}.$$

Without transposing, you would get $\mathbf{J}_{\mathbf{g}}\,\nabla f=(8+3,\ 8+12)^{\top}=(11,\,20)^{\top}$, and that is wrong.
::::

:::warnung Do not forget the transpose
If the Jacobian matrix of the inner function is symmetric, a forgotten transpose goes unnoticed. So check a gradient formula you derived yourself on an example whose Jacobian matrix is not symmetric. If $\mathbf{J}_{\mathbf{g}}$ does not have the same number of rows and columns, a glance at the shapes reveals the mistake immediately: $\nabla f$ has $m$ entries, $\mathbf{J}_{\mathbf{g}}^{\top}$ has $m$ columns, and only $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ gives a vector with $n$ entries.
:::

⁠**In short:** The gradient of a composition is the transposed Jacobian matrix of the inner function times the gradient of the outer one: $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$.

### Derivative along a curve

<span class="anker" id="stufe-6-4"></span>

A walk across the map is a curve: at each time $t$ you are at a location $\boldsymbol{\gamma}(t)\in\mathbb{R}^d$. How fast does the height $f(\boldsymbol{\gamma}(t))$ change along the way? This is a special case of the chain rule with a single input variable $t$.

:::definition Definition 6.3 (Curve and velocity)
<span class="anker" id="satz-6-3"></span>

A __curve__ is a function $\boldsymbol{\gamma}:\mathbb{R}\to\mathbb{R}^d$, $t\mapsto\boldsymbol{\gamma}(t)=(\gamma_1(t),\dots,\gamma_d(t))^{\top}$. Its derivative $\boldsymbol{\gamma}'(t)=(\gamma_1'(t),\dots,\gamma_d'(t))^{\top}$ is called the __velocity vector__.
:::

The velocity vector is the Jacobian matrix of $\boldsymbol{\gamma}$, a $d\times1$ matrix. It points in the direction in which you are currently moving, and its length is the speed. By [(6.1)](#gl-6-1) with $n=1$, for differentiable $f$

<span class="anker" id="gl-6-4"></span>
$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)=\nabla f\bigl(\boldsymbol{\gamma}(t)\bigr)^{\top}\boldsymbol{\gamma}'(t). \tag{6.4}$$

For a line $\boldsymbol{\gamma}(t)=\mathbf{x}+t\,\mathbf{h}$, $\boldsymbol{\gamma}'=\mathbf{h}$ and the rate is $\nabla f(\mathbf{x})^{\top}\mathbf{h}$; if $\mathbf{h}$ has length $1$, this is the directional derivative from Section [4.1](richtungsableitung-und-steilster-anstieg.html#stufe-4-1). If a curve runs entirely within a contour line, $f(\boldsymbol{\gamma}(t))$ is constant, so the left-hand side is zero: the gradient is perpendicular to every velocity vector within the contour line. This is the theorem from Section [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3), now justified with the chain rule.

::::beispiel [Worked example]
Let $f(\mathbf{x})=x_1^2x_2+x_2^2$ and $\boldsymbol{\gamma}(t)=(1+t,\ 2+2t)^{\top}$, a line through $(1,\,2)$ with $\boldsymbol{\gamma}'(t)=(1,\,2)^{\top}$. At $t=0$,

$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)\Big|_{t=0}=\begin{pmatrix}4&5\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix}=4+10=14 .$$

Check: $f(\boldsymbol{\gamma}(t))=(1+t)^2(2+2t)+(2+2t)^2=2\,(1+t)^3+4\,(1+t)^2$ has the derivative $6+8=14$ at $t=0$.
::::

⁠**In short:** Along a curve, $f$ changes at the rate $\nabla f^{\top}\boldsymbol{\gamma}'$; within a contour line, this rate is zero.

:::aufgabe Exercise 20 ★ Chain rule with Jacobian matrices
<span class="anker" id="aufg-20"></span>

Let $\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1x_2)^{\top}$ and $f(\mathbf{u})=u_1^2-u_2$.

<ol class="al">

<li>

At the point $\mathbf{x}=(1,\,3)^{\top}$, compute the intermediate value $\mathbf{u}$, the Jacobian matrix $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ and $\nabla f(\mathbf{u})$.

</li>

<li>

Compute $\nabla(f\circ\mathbf{g})(\mathbf{x})$ with [(6.3)](#gl-6-3) and check it with the written-out function. What would you get without transposing?

</li>

</ol>

:::loesung
(a) $\mathbf{u}=\mathbf{g}(1,3)=(4,\,3)^{\top}$. The Jacobian matrix is $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}1&1\\x_2&x_1\end{smallmatrix}\bigr)$, so at the point $(1,\,3)$ it is $\bigl(\begin{smallmatrix}1&1\\3&1\end{smallmatrix}\bigr)$. The gradient of the outer function is $\nabla f(\mathbf{u})=(2u_1,\,-1)^{\top}=(8,\,-1)^{\top}$.

(b) By [(6.3)](#gl-6-3):

$$\nabla(f\circ\mathbf{g})(1,3)=\begin{pmatrix}1&3\\1&1\end{pmatrix}\begin{pmatrix}8\\-1\end{pmatrix}=\begin{pmatrix}8-3\\8-1\end{pmatrix}=\begin{pmatrix}5\\7\end{pmatrix}.$$

Check: $F(\mathbf{x})=(x_1+x_2)^2-x_1x_2=x_1^2+x_1x_2+x_2^2$ has the partial derivatives $2x_1+x_2=5$ and $x_1+2x_2=7$. Without transposing, you would get $\mathbf{J}_{\mathbf{g}}\nabla f=(8-1,\ 24-1)^{\top}=(7,\,23)^{\top}$, which is a wrong result.
:::
:::

:::aufgabe Exercise 21 ★★ Three paths
<span class="anker" id="aufg-21"></span>

Let $F(x)=g_1(x)\,g_2(x)\,g_3(x)$ with $g_1(x)=x$, $g_2(x)=x^2$ and $g_3(x)=x^3$.

<ol class="al">

<li>

Draw the network of paths from $x$ via $u_1,u_2,u_3$ to $F=u_1u_2u_3$, and write its factor on each edge.

</li>

<li>

Compute $F'(x)$ as a sum over the three paths and compare with the derivative of $x^6$.

</li>

</ol>

:::loesung
(a) From $x$, three edges lead to $u_1$, $u_2$, $u_3$ with the factors $1$, $2x$ and $3x^2$. From each $u_i$, one edge leads to $F=u_1u_2u_3$; its factor is the product of the other two: $u_2u_3=x^5$, $u_1u_3=x^4$ and $u_1u_2=x^3$.

(b) Summed over the three paths:

$$F'(x)=x^5\cdot1+x^4\cdot2x+x^3\cdot3x^2=x^5+2x^5+3x^5=6x^5 .$$

This is the derivative of $F(x)=x^6$. The path via $u_k$ contributes $k\,x^5$, because $g_k=x^k$ has the derivative $k\,x^{k-1}$ and the other two factors together give $x^{6-k}$. So the product rule for three factors is the sum over three paths.
:::
:::

:::aufgabe Exercise 22 ★★ A curve within a contour line
<span class="anker" id="aufg-22"></span>

Let $f(\mathbf{x})=x_1^2+4x_2^2$ and $\boldsymbol{\gamma}(t)=\bigl(\sqrt5\cos t,\ \tfrac{\sqrt5}2\sin t\bigr)^{\top}$.

<ol class="al">

<li>

Show that $\boldsymbol{\gamma}$ runs entirely within the contour line $f=5$.

</li>

<li>

Determine $t$ with $\boldsymbol{\gamma}(t)=(1,\,1)^{\top}$, compute $\boldsymbol{\gamma}'(t)$ there and check that $\nabla f^{\top}\boldsymbol{\gamma}'=0$. Compare the direction with the vector $\mathbf{t}$ from Section [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3).

</li>

<li>

Use [(6.4)](#gl-6-4) to show in general: if a differentiable curve runs within a level set of $f$, then $\nabla f$ is perpendicular to its velocity vector.

</li>

</ol>

:::loesung
(a) $f(\boldsymbol{\gamma}(t))=5\cos^2t+4\cdot\tfrac54\sin^2t=5\,(\cos^2t+\sin^2t)=5$ for every $t$.

(b) From $\sqrt5\cos t=1$ and $\tfrac{\sqrt5}2\sin t=1$ it follows that $\cos t=1/\sqrt5$ and $\sin t=2/\sqrt5$, so $t\approx1.107$. There,

$$\boldsymbol{\gamma}'(t)=\bigl(-\sqrt5\sin t,\ \tfrac{\sqrt5}2\cos t\bigr)^{\top}=\bigl(-2,\ \tfrac12\bigr)^{\top},\qquad \nabla f(1,1)^{\top}\boldsymbol{\gamma}'=2\cdot(-2)+8\cdot\tfrac12=0 .$$

The velocity vector is $-\tfrac12\,(4,\,-1)^{\top}$, so it is parallel to the vector $\mathbf{t}$ from Section [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3).

(c) If $\boldsymbol{\gamma}$ runs within the level set for the value $c$, then $f(\boldsymbol{\gamma}(t))=c$ for all $t$, and the derivative with respect to $t$ is zero. By [(6.4)](#gl-6-4), this derivative is $\nabla f(\boldsymbol{\gamma}(t))^{\top}\boldsymbol{\gamma}'(t)$. So the gradient is perpendicular to every velocity vector of a curve within the level set.
:::
:::

:::aufgabe Exercise 23 ★★★ A chain with three stages
<span class="anker" id="aufg-23"></span>

Let $F(\mathbf{x})=\sum_{i=1}^2(\mathbf{A}\mathbf{x})_i^2$ with $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$. The calculation consists of three stages: $\mathbf{u}=\mathbf{A}\mathbf{x}$, then $v_i=u_i^2$ for each component, then $F=v_1+v_2$.

<ol class="al">

<li>

Give the three Jacobian matrices at the point $\mathbf{x}=(2,\,1)^{\top}$ and compute $\mathbf{J}_F$ as their product.

</li>

<li>

Show in general that $\nabla F(\mathbf{x})=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$, and check the result from (a).

</li>

<li>

Compute the product from (a) once from the left and once from the right. Which order needs fewer multiplications if $\mathbf{A}$ is an $n\times n$ matrix?

</li>

</ol>

:::loesung
(a) At the point $(2,\,1)$, $\mathbf{u}=\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$, $\mathbf{v}=(16,\,1)^{\top}$ and $F=17$. The Jacobian matrices are $\mathbf{J}_1=\mathbf{A}$, $\mathbf{J}_2=\operatorname{diag}(2u_1,\,2u_2)=\operatorname{diag}(8,\,2)$ and $\mathbf{J}_3=(1\ \ 1)$. Their product is

$$\mathbf{J}_F=(1\ \ 1)\,\operatorname{diag}(8,\,2)\,\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 2)\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 18).$$

(b) Transposed, $\nabla F=\mathbf{A}^{\top}\,\operatorname{diag}(2\mathbf{u})\,\mathbf{1}=\mathbf{A}^{\top}\,2\mathbf{u}=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$. With $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&5\end{smallmatrix}\bigr)$, we get $2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=2\,(4,\,9)^{\top}=(8,\,18)^{\top}$, as in (a). Check: $F=(x_1+2x_2)^2+x_2^2$ has the partial derivatives $2\cdot4=8$ and $4\cdot4+2=18$.

(c) From the left: $(1\ \ 1)\,\operatorname{diag}(8,2)$ is a row, for which you need $n$ multiplications, and the row times $\mathbf{A}$ needs $n^2$. From the right: $\operatorname{diag}(8,2)\,\mathbf{A}$ needs $n^2$ multiplications, and the row times the result another $n^2$. So from the left it takes about $n^2$ multiplications, from the right about $2n^2$. If the middle matrix were not diagonal but dense, the matrix product from the right would even cost about $n^3$. From the left, starting at the result, only rows ever arise.
:::
:::
