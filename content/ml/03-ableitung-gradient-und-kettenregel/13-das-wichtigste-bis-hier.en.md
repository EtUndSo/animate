---
title: Key points so far
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15231300
summary: How a number responds to its inputs: from the tangent line to reverse mode
tags: 
lang: en
---

:::kern Key points so far
<ul>

<li>

Derivative: $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$; near $x$, $f(x+h)\approx f(x)+f'(x)h$, with an error that vanishes faster than $h$. With the second derivative: $f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$.

</li>

<li>

Chain rule: $(f\circ g)'(x)=f'(g(x))\,g'(x)$; for long chains, the product of all factors. Logistic function: $\sigma'=\sigma(1-\sigma)\le\tfrac14$.

</li>

<li>

Gradient $\nabla f\in\mathbb{R}^d$ as a column; $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$ if $f$ is differentiable; partial derivatives alone are not enough.

</li>

<li>

Directional derivative $D_{\mathbf{u}}f=\nabla f^{\top}\mathbf{u}$; steepest ascent in the direction $\nabla f$ with slope $\lVert\nabla f\rVert$ (Cauchy–Schwarz); $\nabla f$ is perpendicular to the contour lines; $-\nabla f$ points to the lowest point only for round contour lines.

</li>

<li>

Jacobian matrix $\mathbf{J}_{\mathbf{g}}\in\mathbb{R}^{m\times n}$, one row per output: $\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}\mathbf{h}$; for $\mathbf{A}\mathbf{x}+\mathbf{b}$ it is $\mathbf{A}$, for elementwise functions it is diagonal.

</li>

<li>

Chain rule: $\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$, componentwise a sum over all paths; $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$.

</li>

<li>

$\nabla(\mathbf{a}^{\top}\mathbf{x})=\mathbf{a}$, $\nabla(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})=(\mathbf{A}+\mathbf{A}^{\top})\mathbf{x}$, $\nabla\lVert\mathbf{y}-\mathbf{A}\mathbf{x}\rVert^2=-2\mathbf{A}^{\top}(\mathbf{y}-\mathbf{A}\mathbf{x})$, $\nabla_{\mathbf{A}}(\mathbf{u}^{\top}\mathbf{A}\mathbf{v})=\mathbf{u}\mathbf{v}^{\top}$; backward through $\mathbf{y}=\mathbf{A}\mathbf{x}$ with $F=f(\mathbf{A}\mathbf{x})$: $\nabla_{\mathbf{A}}F=\nabla f(\mathbf{y})\,\mathbf{x}^{\top}$, $\nabla_{\mathbf{x}}F=\mathbf{A}^{\top}\nabla f(\mathbf{y})$.

</li>

<li>

Hessian matrix $\mathbf{H}_f$, symmetric by Schwarz's theorem; $f(\mathbf{x}+\mathbf{h})\approx f+\nabla f^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$; the curvature in the direction $\mathbf{u}$ is $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$, between the smallest and the largest eigenvalue.

</li>

<li>

Computational graph: elementary operations, forward evaluation with stored values, local derivatives on the edges.

</li>

<li>

Forward mode: tangent values, one pass per direction ($\mathbf{J}\dot{\mathbf{x}}$). Reverse mode: adjoints $\bar a=\sum\bar b\,\partial b/\partial a$ starting from $\bar f=1$, one pass for the whole gradient, cost a small multiple of one evaluation, price: memory.

</li>

<li>

Numerical: forward difference error $\approx\tfrac12f''h$, central difference $\approx\tfrac16f'''h^2$; rounding grows like $\varepsilon_{\mathrm M}/h$, hence the V-shaped curve; gradient check with the relative error, above $10^{-2}$ wrong, below $10^{-7}$ good.

</li>

</ul>
:::

:::merke The answer in three sentences
<ol>

<li>

The linear approximation of a number tells how it responds to small changes in its inputs: each input contributes its partial derivative times its change, and the contributions add up to the dot product with the gradient.

</li>

<li>

By the Cauchy–Schwarz inequality, for steps of fixed length this dot product is largest in the direction of the gradient, which therefore points uphill most steeply and is perpendicular to the contour lines.

</li>

<li>

If the number arises from a long chain of calculation steps, its derivative is a product of Jacobian matrices, that is, a sum over all paths, and reverse mode computes this product starting from the number with row vectors, so that it delivers all derivatives at once for a small multiple of the cost of a single evaluation.

</li>

</ol>
:::

**One principle behind all the results.** Almost everything in this chapter follows from one principle: close enough to a point, every differentiable function is linear. Derivative, gradient and Jacobian matrix are this linear approximation, the chain rule connects linear approximations in series and multiplies their matrices in doing so, and forward and reverse mode are two ways of parenthesizing this product.

| Result | Where it comes from |
|---|---|
| Derivative and tangent line | the only line whose error vanishes faster than $h$ (Section [1](die-ableitung.html#stufe-1)) |
| Product rule | the corner piece $\Delta u\,\Delta v$ is small of second order (Section [1.4](die-ableitung.html#stufe-1-4)) |
| Chain rule in one variable | each stage passes small changes on with its factor (Section [2](die-kettenregel.html#stufe-2)) |
| Gradient and tangent plane | the effects of small changes add up (Section [3](partielle-ableitungen-und-der-gradient.html#stufe-3)) |
| Steepest ascent | Cauchy–Schwarz for $\nabla f^{\top}\mathbf{u}$ (Section [4](richtungsableitung-und-steilster-anstieg.html#stufe-4)) |
| Gradient perpendicular to the contour line | along the contour line, the slope is zero (Sections [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) and [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6)) |
| Jacobian matrix | the matrix of the linear approximation of a vector-valued function (Section [5](die-jacobi-matrix.html#stufe-5)) |
| Chain rule as a matrix product, sum over paths | linear approximations connected in series (Section [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6)) |
| Matrix identities, backward rule | chain rule componentwise, in a fixed layout convention (Section [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7)) |
| Hessian matrix and curvature | second derivative along a line, eigenvalues of a quadratic form (Section [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8)) |
| Reverse mode | group paths by their first edge, reuse partial sums; parenthesization from the left (Sections [9](rechengraphen.html#stufe-9) and [10](automatische-differentiation.html#stufe-10)) |
| Central difference, V-shaped curve | even Taylor terms cancel; rounding errors grow like $1/h$ (Section [11](numerische-ableitung-und-gradientenprufung.html#stufe-11)) |
