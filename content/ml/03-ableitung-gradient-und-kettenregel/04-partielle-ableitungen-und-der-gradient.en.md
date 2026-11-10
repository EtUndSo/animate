---
title: Partial derivatives and the gradient
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15230400
summary: If a number depends on many inputs, you can change each input a little on its own and hold the others fixed.
tags: function of d variables, level set, contour line, cross-section curve, partial derivative, gradient, tangent plane, differentiable
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
If a number depends on many inputs, you can change each input a little on its own and hold the others fixed. The slopes you find this way are called partial derivatives. Together they form a vector, the gradient, and with it the linear approximation from Section [1](die-ableitung.html#stufe-1) becomes an approximation by a plane. At the end, the section clarifies when this approximation really holds.
:::

### Functions of several variables

<span class="anker" id="stufe-3-1"></span>

In [Chapter 1, Section 2.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2), the prediction for an apartment was the weighted sum $\hat y=\mathbf{w}^{\top}\mathbf{x}$ of the features. If you hold the features fixed and ask how the prediction depends on the weights, then $\hat y$ is a number that depends on the $d$ numbers $w_1,\dots,w_d$. Likewise, the quadratic form $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ from [Chapter 2, Section 5.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1), depends on all components of $\mathbf{x}$. Such assignments call for a term of their own.

:::definition Definition 3.1 (Function of several variables, contour line)
<span class="anker" id="satz-3-1"></span>

A function $f:\mathbb{R}^d\to\mathbb{R}$ assigns a number $f(\mathbf{x})=f(x_1,\dots,x_d)$ to every vector $\mathbf{x}\in\mathbb{R}^d$; it is called a __function of $d$ variables__. For a number $c$, the set of all $\mathbf{x}$ with $f(\mathbf{x})=c$ is called the __level set__ of $f$ for the value $c$. For $d=2$ it is usually a curve and is then called a __contour line__.
:::

For two variables, the picture of a landscape helps. The vector $\mathbf{x}=(x_1,\,x_2)^{\top}$ is a location on a map, and $f(\mathbf{x})$ is the height of the terrain above this location. The graph of $f$, the set of points $(x_1,\,x_2,\,f(x_1,x_2))$ in space, is the surface of the terrain. As on a hiking map, the contour lines connect all locations of equal height. Where they lie close together, the terrain is steep; where they lie far apart, it is flat. With more than two variables the picture is missing, but the calculations stay the same.

::::beispiel [Worked example]
Throughout Sections [3](#stufe-3) through [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8), we work with the function

<span class="anker" id="gl-3-1"></span>
$$f(\mathbf{x})=x_1^2\,x_2+x_2^2 . \tag{3.1}$$

At the point $\mathbf{x}=(1,\,2)^{\top}$, $f(1,2)=1\cdot2+4=6$. The contour line $f=6$ consists of all points with $x_1^2x_2+x_2^2=6$. For $x_1=0$ this is $x_2^2=6$, so the point $(0,\ \sqrt6)^{\top}\approx(0,\ 2.449)^{\top}$ lies on it. In general, for every fixed $x_1$ the equation is quadratic in $x_2$, and its positive solution $x_2=\tfrac12\bigl(\sqrt{x_1^4+24}-x_1^2\bigr)$ describes the entire contour line above the $x_1$-axis; for $x_1=1$ it gives $\tfrac12(5-1)=2$. Fig. [6](#abb-6) shows several contour lines.
::::

⁠**In short:** A function of $d$ variables assigns a number to every vector; with two variables you picture it as a landscape whose contour lines connect locations of equal height.

### Partial derivatives

<span class="anker" id="stufe-3-2"></span>

How strongly does $f$ respond if you change only one input? You hold all others fixed, and $f$ becomes an ordinary function of one variable. In the picture of the landscape, you cut the terrain along a line parallel to one axis. The cut surface shows a curve as its edge, the __cross-section curve__, and its slope is the sensitivity you are looking for.

:::definition Definition 3.2 (Partial derivative)
<span class="anker" id="satz-3-2"></span>

The __partial derivative__ of $f:\mathbb{R}^d\to\mathbb{R}$ with respect to $x_j$ at the point $\mathbf{x}$ is

<span class="anker" id="gl-3-2"></span>
$$\frac{\partial f}{\partial x_j}(\mathbf{x})=\lim_{h\to0}\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x})}{h}, \tag{3.2}$$

provided the limit exists. Here $\mathbf{e}_j$ is the $j$th unit vector from [Chapter 1, Section 1.6](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-daten-als-zahlenlisten.html#stufe-1-6). For short, you also write $\partial_jf(\mathbf{x})$.
:::

The vector $\mathbf{x}+h\,\mathbf{e}_j$ differs from $\mathbf{x}$ only in the $j$th component, namely by $h$. So the definition is the ordinary derivative from Section [1.2](die-ableitung.html#stufe-1-2), applied to the function obtained by holding all variables except $x_j$ fixed. This yields the rule of calculation: you differentiate with respect to $x_j$ and treat all other variables like constants. The symbol $\partial$ is a rounded d and is a reminder that only some of the variables move.

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$, when differentiating with respect to $x_1$ you treat the variable $x_2$ as a constant, and vice versa:

$$\frac{\partial f}{\partial x_1}=2x_1\,x_2,\qquad \frac{\partial f}{\partial x_2}=x_1^2+2x_2 .$$

At the point $(1,\,2)$ this gives $4$ and $5$. The cross-section curves show the same thing (Fig. [6](#abb-6)): if you hold $x_2=2$ fixed, what remains is $f(x_1,2)=2x_1^2+4$ with the slope $4x_1=4$ at the point $x_1=1$. If you hold $x_1=1$ fixed, what remains is $f(1,x_2)=x_2+x_2^2$ with the slope $1+2x_2=5$ at the point $x_2=2$.

:::abbildung ml/k3schnitt 6
Partial derivatives as slopes of cross-section curves, for $f(\mathbf{x})=x_1^2x_2+x_2^2$ at the point $(1,\,2)$. (a) Contour lines for the values $2$, $4$, $6$ (black), $8$ and $10$, together with the two cutting lines through $(1,\,2)$. (b) Along the blue line $x_2=2$, the terrain runs like $2x_1^2+4$, with slope $4$ at $x_1=1$. (c) Along the red line $x_1=1$, it runs like $x_2+x_2^2$, with slope $5$ at $x_2=2$.
:::
::::

⁠**In short:** The partial derivative $\partial f/\partial x_j$ is the slope in the direction of the $x_j$-axis: you differentiate with respect to $x_j$ and hold all other variables fixed.

### The gradient

<span class="anker" id="stufe-3-3"></span>

A function of $d$ variables has $d$ partial derivatives at every point. You collect them into a vector so that you can calculate with them just as with $\mathbf{x}$ itself.

:::definition Definition 3.3 (Gradient)
<span class="anker" id="satz-3-3"></span>

If all partial derivatives of $f:\mathbb{R}^d\to\mathbb{R}$ exist at the point $\mathbf{x}$, then the column vector

<span class="anker" id="gl-3-3"></span>
$$\nabla f(\mathbf{x})=\begin{pmatrix}\partial_1f(\mathbf{x})\\ \vdots\\ \partial_df(\mathbf{x})\end{pmatrix}\in\mathbb{R}^d \tag{3.3}$$

is called the __gradient__ of $f$ at the point $\mathbf{x}$. The symbol $\nabla$ is read “nabla” (or “del”).
:::

The gradient has the same shape as $\mathbf{x}$: one entry per variable, written as a column. This convention holds throughout the chapter; Section [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) returns to it, because not all books adopt it. If you assign to every point $\mathbf{x}$ its gradient, you get a field of arrows, one at every location on the map. Section [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) clarifies where these arrows point.

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$,

$$\nabla f(\mathbf{x})=\begin{pmatrix}2x_1x_2\\ x_1^2+2x_2\end{pmatrix},\qquad \nabla f(1,2)=\begin{pmatrix}4\\5\end{pmatrix},\qquad \nabla f(0,1)=\begin{pmatrix}0\\2\end{pmatrix} .$$

For the sum of squares $f(\mathbf{x})=x_1^2+x_2^2+x_3^2$, $\nabla f(\mathbf{x})=(2x_1,\,2x_2,\,2x_3)^{\top}=2\mathbf{x}$.
::::

⁠**In short:** The gradient is the column vector of all partial derivatives, with the same shape as $\mathbf{x}$.

### The linear approximation in space

<span class="anker" id="stufe-3-4"></span>

For one variable, the tangent line replaces the function near a point. With two variables, a plane takes its place. Under the magnifying glass, smooth terrain near a point looks like a tilted plate: this is the __tangent plane__. A plane through the point $(\mathbf{x},\,f(\mathbf{x}))$ has the form $f(\mathbf{x})+m_1h_1+m_2h_2$, where $\mathbf{h}=(h_1,\,h_2)^{\top}$ is the displacement on the map and $m_1$, $m_2$ are the tilts of the plate in the directions of the two axes. For it to hug the terrain, its tilts along the axes must agree with the slopes of the cross-section curves, that is, $m_j=\partial_jf(\mathbf{x})$.

This yields the linear approximation for many variables:

<span class="anker" id="gl-3-4"></span>
$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=f(\mathbf{x})+\sum_{j=1}^d\partial_jf(\mathbf{x})\,h_j . \tag{3.4}$$

The formula says something remarkable: if you change several inputs at once by small amounts, *their effects add up*. Each variable contributes $\partial_jf\cdot h_j$, as if it alone had been changed. For large changes this is no longer true, because then the variables influence each other's effect, as in $x_1^2x_2$. For small changes, these interactions are products of small quantities and vanish faster than the individual effects, just like the corner piece in the product rule.

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$ at the point $\mathbf{x}=(1,\,2)^{\top}$ and the displacement $\mathbf{h}=(0.01,\ 0.02)^{\top}$,

$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=6+4\cdot0.01+5\cdot0.02=6+0.14=6.14 .$$

The exact value is $f(1.01,\ 2.02)=1.0201\cdot2.02+2.02^2=2.060602+4.0804=6.141002$. The error $0.001002$ is much smaller than the change $0.14$ itself. Fig. [7](#abb-7) shows the dot product step by step.

:::abbildung ml/k3rlinear 7
The change in the linear approximation as the dot product of gradient and displacement: each variable contributes its partial derivative times its own change.
:::
::::

⁠**In short:** Near $\mathbf{x}$, $f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$: for small changes, the effects of the individual variables add up.

### Differentiability

<span class="anker" id="stufe-3-5"></span>

So far, the approximation [(3.4)](#gl-3-4) has only been made plausible. For one variable, it followed from the existence of the derivative. With several variables, the existence of the partial derivatives is not enough for this, as the counterexample below shows. You therefore require the approximation itself: its error should vanish faster than the displacement, just as in [(1.4)](die-ableitung.html#gl-1-4) the error $r(h)$ vanished faster than $h$. You cannot divide by a vector; instead of by $h$, you therefore divide by the length $\lVert\mathbf{h}\rVert$ from [Chapter 1, Section 3.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-1).

:::definition Definition 3.4 (Differentiability)
<span class="anker" id="satz-3-4"></span>

A function $f:\mathbb{R}^d\to\mathbb{R}$ is called __differentiable__ at the point $\mathbf{x}$ if there is a vector $\mathbf{g}\in\mathbb{R}^d$ with

<span class="anker" id="gl-3-5"></span>
$$\lim_{\mathbf{h}\to\mathbf{0}}\frac{f(\mathbf{x}+\mathbf{h})-f(\mathbf{x})-\mathbf{g}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=0 . \tag{3.5}$$

The limit $\mathbf{h}\to\mathbf{0}$ means: the quotient lies arbitrarily close to $0$ as soon as $\lVert\mathbf{h}\rVert$ is small enough and $\mathbf{h}\ne\mathbf{0}$, no matter from which direction $\mathbf{h}$ approaches.
:::

:::satz Theorem 3.5 (Differentiable means: gradient and linear approximation)
<span class="anker" id="satz-3-5"></span>

If $f$ is differentiable at the point $\mathbf{x}$, then all partial derivatives exist there, and the vector in [(3.5)](#gl-3-5) is the gradient: $\mathbf{g}=\nabla f(\mathbf{x})$. Conversely, $f$ is differentiable at the point $\mathbf{x}$ if all partial derivatives exist near $\mathbf{x}$ and are continuous at the point $\mathbf{x}$.
:::

:::beweis The vector is the gradient
In [(3.5)](#gl-3-5), choose specifically $\mathbf{h}=t\,\mathbf{e}_j$ with a number $t\ne0$; then $\lVert\mathbf{h}\rVert=|t|$ and $\mathbf{g}^{\top}\mathbf{h}=t\,g_j$. The quotient reads $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})-t\,g_j}{|t|}$ and tends to $0$. Then $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})}{t}-g_j$ also tends to $0$, because this number has the same absolute value. So the partial derivative with respect to $x_j$ exists, and it is $g_j$. This holds for every $j$.
:::

In practice, the second statement is the important one. Polynomials, the exponential function, the logistic function and everything built from them by basic arithmetic operations and composition have continuous partial derivatives wherever they are defined. Such functions are therefore differentiable, and [(3.4)](#gl-3-4) holds for them. Exceptions in this chapter are kinks, as in $|x|$ or $\max(x,\,0)$.

:::warnung Partial derivatives alone are not enough
The function $f(x_1,x_2)=\dfrac{x_1x_2}{x_1^2+x_2^2}$ with $f(0,0)=0$ is zero on both axes, because there $x_1x_2=0$. Its cross-section curves through the origin along the axes are therefore horizontal: $\partial_1f(0,0)=\partial_2f(0,0)=0$, and the gradient at the origin is $\mathbf{0}$. The linear approximation therefore predicts that $f$ is almost $0$ near the origin. On the diagonal $x_1=x_2=t$ with $t\ne0$, however, $f(t,t)=t^2/(2t^2)=\tfrac12$, no matter how small $t$ is. The function jumps at the origin, and no plane hugs it. It is not differentiable there, although both partial derivatives exist. Anyone who infers the linear approximation from the existence of the gradient therefore needs differentiability, for example via continuous partial derivatives.
:::

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$, the partial derivatives $2x_1x_2$ and $x_1^2+2x_2$ are polynomials, hence continuous everywhere, and $f$ is differentiable everywhere. In the worked example for [(3.4)](#gl-3-4), the error was $0.001002$ at $\lVert\mathbf{h}\rVert=\sqrt{0.0001+0.0004}\approx0.0224$, so the quotient in [(3.5)](#gl-3-5) was about $0.045$. If you halve $\mathbf{h}$ to $(0.005,\ 0.01)^{\top}$, the error is $f(1.005,\ 2.01)-6-0.07=0.000250\ldots$ and the quotient is about $0.022$: it halves along with $\mathbf{h}$ and tends to $0$.
::::

⁠**In short:** Differentiable means that the linear approximation with the gradient has an error that vanishes faster than $\lVert\mathbf{h}\rVert$; continuous partial derivatives guarantee this, their mere existence does not.

:::hintergrund Why continuous partial derivatives suffice
You go from $\mathbf{x}$ to $\mathbf{x}+\mathbf{h}$ not diagonally but in two legs parallel to the axes: first by $h_1$ in the direction of $x_1$, then by $h_2$ in the direction of $x_2$. On each leg only one variable changes, and by the mean value theorem for one variable the change is exactly $\partial_jf\cdot h_j$, evaluated at an intermediate point of the leg. If the partial derivatives are continuous, their values at the intermediate points lie close to the values at the point $\mathbf{x}$, and the sum of the two legs differs from $\nabla f(\mathbf{x})^{\top}\mathbf{h}$ only by an amount that vanishes faster than $\lVert\mathbf{h}\rVert$. In the counterexample, exactly this step breaks down: its partial derivatives exist away from the origin, but they are not continuous. On the axis $x_1=0$, for instance, $\partial_1f(0,x_2)=1/x_2$, and this becomes arbitrarily large the closer you get to the origin, where the value is $0$.
:::

:::aufgabe Exercise 9 ★ Partial derivatives and gradients
<span class="anker" id="aufg-9"></span>

Compute the partial derivatives and the gradient at the given point.

<ol class="al">

<li>

$f(\mathbf{x})=3x_1-2x_2+5$ at the point $(4,\,-1)$;

</li>

<li>

$f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$ at the points $(2,\,0)$ and $(1,\,1)$;

</li>

<li>

$f(\mathbf{x})=x_1x_2+x_2x_3+x_3x_1$ at the point $(1,\,2,\,3)$.

</li>

</ol>

:::loesung
(a) $\partial_1f=3$, $\partial_2f=-2$, so $\nabla f=(3,\,-2)^{\top}$ at every point.

(b) $\partial_1f=\mathrm{e}^{x_2}$ and $\partial_2f=x_1\mathrm{e}^{x_2}$. At the point $(2,\,0)$, $\nabla f=(1,\,2)^{\top}$; at the point $(1,\,1)$, $\nabla f=(\mathrm{e},\,\mathrm{e})^{\top}\approx(2.718,\ 2.718)^{\top}$.

(c) $\partial_1f=x_2+x_3$, $\partial_2f=x_1+x_3$, $\partial_3f=x_1+x_2$; so at the point $(1,\,2,\,3)$, $\nabla f=(5,\,4,\,3)^{\top}$.
:::
:::

:::aufgabe Exercise 10 ★★ Linear approximation with two variables
<span class="anker" id="aufg-10"></span>

Let $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$.

<ol class="al">

<li>

Use the linear approximation at the point $(2,\,0)$ to compute an approximate value for $f(2.1,\ -0.05)$, and compare it with the exact value.

</li>

<li>

Which of the two changes contributes more to the change in $f$? Why do they cancel exactly in the linear approximation but not in the exact value?

</li>

</ol>

:::loesung
(a) We have $f(2,0)=2$ and $\nabla f(2,0)=(1,\,2)^{\top}$ by Exercise [9](#aufg-9). With $\mathbf{h}=(0.1,\ -0.05)^{\top}$:

$$f(2.1,\ -0.05)\approx2+1\cdot0.1+2\cdot(-0.05)=2+0.1-0.1=2.0 .$$

The exact value is $2.1\,\mathrm{e}^{-0.05}\approx2.1\cdot0.951229\approx1.99758$. The error is about $0.0024$.

(b) Both changes contribute equally, $+0.1$ and $-0.1$, and cancel in the linear approximation. In the exact value, however, the variables influence each other: if $x_1$ grows, $f$ responds more strongly to $x_2$, because $\partial_2f=x_1\mathrm{e}^{x_2}$ grows with $x_1$. The decrease in $x_2$ therefore has a somewhat stronger effect than the linear approximation assumes. Such interactions are products of two changes, here about $0.1\cdot(-0.05)=-0.005$, and belong to the second-order terms that the linear approximation leaves out. Section [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) computes them (Exercise [29](die-hesse-matrix-und-die-quadratische-naherung.html#aufg-29)).
:::
:::

:::aufgabe Exercise 11 ★★ Contour lines and cross-section curves
<span class="anker" id="aufg-11"></span>

Let $f(\mathbf{x})=x_1^2x_2+x_2^2$ as in [(3.1)](#gl-3-1).

<ol class="al">

<li>

What is the value of $f$ at the point $(2,\,1)$? Give another point on the same contour line with $x_1=0$.

</li>

<li>

Compute $\nabla f(2,1)$ and the equations of the two cross-section curves through $(2,\,1)$. Check their slopes.

</li>

</ol>

:::loesung
(a) $f(2,1)=4\cdot1+1=5$. With $x_1=0$, the contour line requires $x_2^2=5$, so, for example, $(0,\ \sqrt5)\approx(0,\ 2.236)$ lies on it.

(b) $\nabla f(2,1)=(2\cdot2\cdot1,\ 4+2\cdot1)^{\top}=(4,\,6)^{\top}$. The cross-section curve along $x_2=1$ is $f(x_1,1)=x_1^2+1$, with slope $2x_1=4$ at $x_1=2$. The cross-section curve along $x_1=2$ is $f(2,x_2)=4x_2+x_2^2$, with slope $4+2x_2=6$ at $x_2=1$. Both slopes agree with the components of the gradient.
:::
:::

:::aufgabe Exercise 12 ★★★ Continuous but not differentiable
<span class="anker" id="aufg-12"></span>

Let $f(x_1,x_2)=\sqrt{|x_1x_2|}$.

<ol class="al">

<li>

Show that both partial derivatives exist at the origin and are $0$.

</li>

<li>

Using $\mathbf{h}=(t,\,t)^{\top}$, show that the quotient in [(3.5)](#gl-3-5) with $\mathbf{g}=\mathbf{0}$ does not tend to $0$. Why does it follow that $f$ is not differentiable at the origin, even though $f$ is continuous there?

</li>

</ol>

:::loesung
(a) On both axes, $x_1x_2=0$, so $f=0$. Hence $\frac{f(h,0)-f(0,0)}{h}=0$ for every $h\ne0$, and likewise for the second variable. Both partial derivatives at the origin are $0$.

(b) If $f$ were differentiable at the origin, then by the theorem in Section [3.5](#stufe-3-5) the vector in [(3.5)](#gl-3-5) would have to be the gradient $\mathbf{0}$. With $\mathbf{h}=(t,\,t)^{\top}$, however, $f(\mathbf{h})=\sqrt{t^2}=|t|$ and $\lVert\mathbf{h}\rVert=\sqrt2\,|t|$, so

$$\frac{f(\mathbf{h})-f(\mathbf{0})-\mathbf{0}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=\frac{|t|}{\sqrt2\,|t|}=\frac1{\sqrt2}\approx0.707 ,$$

for every $t\ne0$, however small. The quotient does not tend to $0$, so $f$ is not differentiable. Nevertheless, $f$ is continuous, because $|f(\mathbf{x})|=\sqrt{|x_1|\,|x_2|}\le\max(|x_1|,|x_2|)\le\lVert\mathbf{x}\rVert$ tends to $0$ as $\mathbf{x}$ tends to $\mathbf{0}$. The terrain has no gap at the origin, but along the diagonal it has a crease that no plane can hug.
:::
:::
