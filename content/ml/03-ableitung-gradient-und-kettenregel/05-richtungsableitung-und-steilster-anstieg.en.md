---
title: Directional derivative and steepest ascent
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15230500
summary: The partial derivatives say how the function responds when you change one input alone.
tags: directional derivative
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
The partial derivatives say how the function responds when you change one input alone. If you shift all inputs at once in one direction, the directional derivative measures the slope. With it, this section shows that the gradient points in the direction of steepest ascent and is perpendicular to the contour lines. An example shows that the steepest path downhill nevertheless does not necessarily lead to the lowest point.
:::

### The directional derivative

<span class="anker" id="stufe-4-1"></span>

In the terrain you rarely walk exactly north or exactly east. Standing at the point $\mathbf{x}$ and setting off in some direction, you feel a slope that depends on the direction. A direction is described by a vector $\mathbf{u}$ of length $1$. The length must be fixed: if you take steps twice as large, you climb twice as much with each step, although the terrain is no steeper.

:::definition Definition 4.1 (Directional derivative)
<span class="anker" id="satz-4-1"></span>

For a vector $\mathbf{u}$ with $\lVert\mathbf{u}\rVert=1$,

<span class="anker" id="gl-4-1"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\lim_{t\to0}\frac{f(\mathbf{x}+t\,\mathbf{u})-f(\mathbf{x})}{t} \tag{4.1}$$

is called the __directional derivative__ of $f$ at the point $\mathbf{x}$ in the direction $\mathbf{u}$, provided the limit exists.
:::

For $\mathbf{u}=\mathbf{e}_j$, this is the partial derivative with respect to $x_j$. In the picture of the landscape, you cut the terrain along the line through $\mathbf{x}$ in the direction $\mathbf{u}$, and the directional derivative is the slope of this cross-section curve. But you do not have to compute it anew for every direction.

:::satz Theorem 4.2 (Directional derivative and gradient)
<span class="anker" id="satz-4-2"></span>

If $f$ is differentiable at the point $\mathbf{x}$, then for every vector $\mathbf{u}$ of length $1$

<span class="anker" id="gl-4-2"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}\mathbf{u} . \tag{4.2}$$
:::

:::beweis Directional derivative and gradient
In [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5), set specifically $\mathbf{h}=t\,\mathbf{u}$ with $t\ne0$; then $\lVert\mathbf{h}\rVert=|t|$. The quotient $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})-t\,\nabla f(\mathbf{x})^{\top}\mathbf{u}}{|t|}$ tends to $0$, and so does $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})}{t}-\nabla f(\mathbf{x})^{\top}\mathbf{u}$.
:::

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$ at the point $(1,\,2)$ with $\nabla f=(4,\,5)^{\top}$ and the direction $\mathbf{u}=(0.6,\ 0.8)^{\top}$, which has length $\sqrt{0.36+0.64}=1$,

$$D_{\mathbf{u}}f(1,2)=4\cdot0.6+5\cdot0.8=2.4+4.0=6.4$$

(Fig. [8](#abb-8)). In the opposite direction $-\mathbf{u}$ the slope is $-6.4$, and in the direction $(0.8,\ -0.6)^{\top}$, which is perpendicular to $\mathbf{u}$, it is $3.2-3.0=0.2$.

:::abbildung ml/k3rrichtung 8
The directional derivative as the dot product of gradient and direction, for $f(\mathbf{x})=x_1^2x_2+x_2^2$ at the point $\mathbf{x}=(1,\,2)^{\top}$.
:::
::::

⁠**In short:** The slope in the direction of a unit vector $\mathbf{u}$ is the dot product $\nabla f(\mathbf{x})^{\top}\mathbf{u}$.

### The direction of steepest ascent

<span class="anker" id="stufe-4-2"></span>

In which direction must you go so that the path leads uphill most steeply? By [(4.2)](#gl-4-2), you are looking for the unit vector $\mathbf{u}$ for which the dot product $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ is largest. [Chapter 1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) provided the tool for this: the Cauchy–Schwarz inequality.

:::satz Theorem 4.3 (Steepest ascent)
<span class="anker" id="satz-4-3"></span>

Let $f$ be differentiable at the point $\mathbf{x}$ and $\nabla f(\mathbf{x})\ne\mathbf{0}$. Then for every vector $\mathbf{u}$ of length $1$

<span class="anker" id="gl-4-3"></span>
$$-\lVert\nabla f(\mathbf{x})\rVert\le D_{\mathbf{u}}f(\mathbf{x})\le\lVert\nabla f(\mathbf{x})\rVert . \tag{4.3}$$

The upper bound is attained only for $\mathbf{u}=\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$, the lower bound only for $\mathbf{u}=-\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$. The gradient therefore points in the direction of steepest ascent, and its length is the slope in this direction; the negative gradient points in the direction of steepest descent.
:::

:::beweis Steepest ascent
By the Cauchy–Schwarz inequality from [Chapter 1, Section 5.1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-1), $|\nabla f(\mathbf{x})^{\top}\mathbf{u}|\le\lVert\nabla f(\mathbf{x})\rVert\,\lVert\mathbf{u}\rVert=\lVert\nabla f(\mathbf{x})\rVert$, and equality holds exactly when $\mathbf{u}$ is a multiple of $\nabla f(\mathbf{x})$. The multiples of length $1$ are $\pm\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$. Substituting them gives $\pm\nabla f(\mathbf{x})^{\top}\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert=\pm\lVert\nabla f(\mathbf{x})\rVert$.
:::

With the angle $\varphi$ between $\nabla f(\mathbf{x})$ and $\mathbf{u}$ from [Chapter 1, Section 5.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-2), $D_{\mathbf{u}}f(\mathbf{x})=\lVert\nabla f(\mathbf{x})\rVert\cos\varphi$. If you go in the direction of the gradient, $\varphi=0$ and $\cos\varphi=1$. If you deviate by $90^\circ$, the slope is zero. If you go against it, the slope is most strongly negative. By [Chapter 1, Section 5.5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5), $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ is the shadow length of the gradient on the line in the direction $\mathbf{u}$, and a shadow is longest when the line points in the direction of the arrow itself.

Three assumptions are built into the theorem. First, $\nabla f(\mathbf{x})\ne\mathbf{0}$ must hold; if the gradient is zero, then by [(4.2)](#gl-4-2) the slope is zero in every direction, and no direction is steeper than any other. Second, $f$ must be differentiable, otherwise [(4.2)](#gl-4-2) does not hold. Third, the theorem compares directions of equal Euclidean length; if you measure steps differently, the steepest direction changes (Background box below).

::::beispiel [Worked example]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$ at the point $(1,\,2)$, $\lVert\nabla f\rVert=\sqrt{16+25}=\sqrt{41}\approx6.403$, and the steepest direction is $(4,\,5)^{\top}/\sqrt{41}\approx(0.625,\ 0.781)^{\top}$. No direction has a larger slope. The direction $\mathbf{u}=(0.6,\ 0.8)^{\top}$ from the previous subsection deviates from it by only about $1.8^\circ$; that is why its slope $6.4$ was already almost at the maximum. In the direction $(5,\,-4)^{\top}/\sqrt{41}$, perpendicular to the gradient, the slope is $(20-20)/\sqrt{41}=0$.
::::

⁠**In short:** The gradient points in the direction of steepest ascent, and its length is the slope there; against the gradient, the path leads downhill most steeply.

:::hintergrund The steepest direction depends on how you measure steps
The theorem compares all directions $\mathbf{u}$ with $\lVert\mathbf{u}\rVert=1$ in the Euclidean norm. [Chapter 1, Section 3](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3), introduced further norms. If you allow all steps with $\lVert\mathbf{u}\rVert_\infty\le1$, so that each component may lie between $-1$ and $1$, then $\nabla f^{\top}\mathbf{u}=\sum_j\partial_jf\cdot u_j$ is largest when each component $u_j$ has the value $+1$ or $-1$ with the sign of $\partial_jf$. The steepest direction is then $\operatorname{sign}(\nabla f)$, componentwise, and the slope is $\sum_j|\partial_jf|=\lVert\nabla f\rVert_1$. If, on the other hand, you allow all steps with $\lVert\mathbf{u}\rVert_1\le1$, you put the whole budget into the component with the largest $|\partial_jf|$: the steepest direction is a coordinate axis, and the slope is $\lVert\nabla f\rVert_\infty$. For $\nabla f=(4,\,5)^{\top}$ this gives the directions $(1,\,1)^{\top}$ with slope $9$ and $(0,\,1)^{\top}$ with slope $5$. “The gradient is the steepest direction” is therefore a statement about Euclidean length. It also depends on the units of the variables: if you measure $x_1$ in different units, the lengths of the steps change, and with them the steepest direction, just like the distances in [Chapter 1, Section 4.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2).
:::

### The gradient is perpendicular to the contour lines

<span class="anker" id="stufe-4-3"></span>

If you walk along a contour line, you neither climb nor descend. In the direction of the contour line, the slope is therefore zero, and by the previous subsection the slope is zero exactly in the directions perpendicular to the gradient. The gradient is therefore perpendicular to the contour line. More precisely, this means:

:::satz Theorem 4.4 (Gradient and contour line)
<span class="anker" id="satz-4-4"></span>

Let $f$ be differentiable at the point $\mathbf{x}$, $\nabla f(\mathbf{x})\ne\mathbf{0}$ and $c=f(\mathbf{x})$. The level set of the linear approximation through $\mathbf{x}$, that is, the set of points $\mathbf{x}+\mathbf{h}$ with $\nabla f(\mathbf{x})^{\top}\mathbf{h}=0$, is, for two variables, the line through $\mathbf{x}$ perpendicular to the gradient. It is the tangent line to the contour line of $f$ for the value $c$.
:::

That the line touches the contour line follows from the magnifying glass: near $\mathbf{x}$, $f$ and its linear approximation differ only by an error that vanishes faster than $\lVert\mathbf{h}\rVert$, and so their contour lines for the value $c$ also differ so little that they have the same direction at $\mathbf{x}$. Exercise [22](die-kettenregel-fur-mehrere-variablen.html#aufg-22) provides a proof with the chain rule. With more than two variables, the same holds for the level set, which is then a surface: the gradient is perpendicular to it.

::::beispiel [Worked example]
For the bowl $f(\mathbf{x})=x_1^2+4x_2^2$, $\nabla f(\mathbf{x})=(2x_1,\,8x_2)^{\top}$, which at the point $(1,\,1)$ equals $(2,\,8)^{\top}$. The contour line through this point is the ellipse $x_1^2+4x_2^2=5$. The direction $\mathbf{t}=(4,\,-1)^{\top}$ is perpendicular to the gradient, because $2\cdot4+8\cdot(-1)=0$. If you go from $(1,\,1)$ by an amount $s$ in this direction, then

$$f(1+4s,\ 1-s)=(1+4s)^2+4\,(1-s)^2=5+20s^2 .$$

The value changes only by $20s^2$, which vanishes faster than $s$: the line touches the contour line and is its tangent line. Fig. [9](#abb-9) shows the gradients at many points; each is perpendicular to the contour line through its base point.

:::abbildung ml/k3hoehen 9
Gradients (red, drawn shortened) on contour lines (gray). (a) For the round bowl, all gradients point exactly away from the center. (b) For the elongated bowl, they are also perpendicular to the contour lines but point exactly away from the center only on the axes. At the point $(1,\,1)$ (black), the direction of steepest descent is drawn in blue. In (a) it points to the lowest point; in (b) it deviates by about $31^\circ$ from the direction to the lowest point (dashed).
:::
::::

⁠**In short:** Along a contour line, $f$ does not change; that is why the gradient is perpendicular to it.

### Steepest descent and the lowest point

<span class="anker" id="stufe-4-4"></span>

For a round bowl, it is obvious that the steepest path downhill leads to the center. For an elongated bowl, it is false, and this difference matters because it is easy to expect more from the gradient than it knows.

For $f(\mathbf{x})=x_1^2+x_2^2$, $\nabla f(\mathbf{x})=2\mathbf{x}$. The negative gradient $-2\mathbf{x}$ therefore points from every point exactly at the origin, the lowest point of the bowl. For $f(\mathbf{x})=x_1^2+4x_2^2$, $-\nabla f(\mathbf{x})=(-2x_1,\,-8x_2)^{\top}$, and this is a multiple of $-\mathbf{x}$ only if $x_1=0$ or $x_2=0$, that is, on the axes. Everywhere else, the steepest descent points past the lowest point.

The reason lies in the shape of the contour lines. The gradient knows only how the terrain is tilted at its base point; it is perpendicular to the contour line there. With elongated contour lines, the perpendicular is oblique to the direction toward the center. In the example, $f$ grows four times as fast in the $x_2$ direction as in the $x_1$ direction; the walls of the bowl are steeper in the $x_2$ direction, and the steepest descent leads mainly across them.

::::beispiel [Worked example]
At the point $(1,\,1)$, $-\nabla f=(-2,\,-8)^{\top}$ with length $\sqrt{68}\approx8.246$, so the direction of steepest descent is $(-0.243,\ -0.970)^{\top}$. The direction to the lowest point is $(-1,\,-1)^{\top}/\sqrt2\approx(-0.707,\ -0.707)^{\top}$. The angle between the two has the cosine

$$\frac{(-2)\cdot(-1)+(-8)\cdot(-1)}{\sqrt{68}\cdot\sqrt2}=\frac{10}{\sqrt{136}}\approx0.857,$$

so it is about $31^\circ$. In the direction of the lowest point, the slope by [(4.2)](#gl-4-2) is only $-10/\sqrt2\approx-7.07$, whereas in the steepest descent it is $-8.246$.
::::

⁠**In short:** The negative gradient points downhill most steeply, but it points at the lowest point only for round contour lines; for elongated contour lines it points past it.

:::aufgabe Exercise 13 ★ Slopes in many directions
<span class="anker" id="aufg-13"></span>

Let $f(\mathbf{x})=x_1^2+4x_2^2$ and $\mathbf{x}=(1,\,1)^{\top}$.

<ol class="al">

<li>

Compute the directional derivatives in the directions $\mathbf{e}_1$, $\mathbf{e}_2$, $(1,\,1)^{\top}/\sqrt2$ and $(-1,\,1)^{\top}/\sqrt2$.

</li>

<li>

Compare with $\lVert\nabla f(\mathbf{x})\rVert$. Which of the four directions is closest to the steepest one?

</li>

</ol>

:::loesung
(a) We have $\nabla f(1,1)=(2,\,8)^{\top}$. By [(4.2)](#gl-4-2):

$$D_{\mathbf{e}_1}f=2,\qquad D_{\mathbf{e}_2}f=8,\qquad D_{(1,1)/\sqrt2}f=\frac{2+8}{\sqrt2}\approx7.071,\qquad D_{(-1,1)/\sqrt2}f=\frac{-2+8}{\sqrt2}\approx4.243 .$$

(b) $\lVert\nabla f\rVert=\sqrt{68}\approx8.246$; none of the slopes is larger, as [(4.3)](#gl-4-3) requires. Closest to the steepest direction is $\mathbf{e}_2$, with $8$. The angle between $\mathbf{e}_2$ and $\nabla f$ has the cosine $8/\sqrt{68}\approx0.970$, so it is about $14^\circ$; for $(1,\,1)^{\top}/\sqrt2$ it is about $31^\circ$.
:::
:::

:::aufgabe Exercise 14 ★★ A hyperbola as a contour line
<span class="anker" id="aufg-14"></span>

Let $f(\mathbf{x})=x_1x_2$ and $\mathbf{x}=(2,\,1)^{\top}$.

<ol class="al">

<li>

Compute $\nabla f(\mathbf{x})$, the steepest direction and the slope in it.

</li>

<li>

The contour line through $\mathbf{x}$ is $x_2=2/x_1$. Compute the slope of this curve at $x_1=2$, write its tangent direction as a vector and check that it is perpendicular to $\nabla f(\mathbf{x})$.

</li>

</ol>

:::loesung
(a) $\nabla f(\mathbf{x})=(x_2,\,x_1)^{\top}$, so at the point $(2,\,1)$ it is $(1,\,2)^{\top}$. The steepest direction is $(1,\,2)^{\top}/\sqrt5\approx(0.447,\ 0.894)^{\top}$, and the slope in it is $\sqrt5\approx2.236$.

(b) The contour line $x_2=2/x_1$ has the slope $-2/x_1^2$, so $-\tfrac12$ at $x_1=2$. A tangent direction is $(1,\,-\tfrac12)^{\top}$ or, multiplied by $2$, $(2,\,-1)^{\top}$. We have $(1,\,2)(2,\,-1)^{\top}=2-2=0$: the gradient is perpendicular to the contour line.
:::
:::

:::aufgabe Exercise 15 ★★ Linear functions
<span class="anker" id="aufg-15"></span>

Let $f(\mathbf{x})=\mathbf{a}^{\top}\mathbf{x}+b$ with a fixed $\mathbf{a}\in\mathbb{R}^d$, $\mathbf{a}\ne\mathbf{0}$, and a number $b$.

<ol class="al">

<li>

Show that $\nabla f(\mathbf{x})=\mathbf{a}$ at every point. What are the contour lines for $d=2$?

</li>

<li>

For the apartments from [Chapter 1](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html), $\hat y=\mathbf{w}^{\top}\mathbf{x}+b$ with $\mathbf{w}=(3,\,10,\,-4)^{\top}$, where $x_1$ is the floor area in $\mathrm m^2$, $x_2$ the number of rooms and $x_3$ the distance to the center in km. Which change $\mathbf{u}$ of the features with $\lVert\mathbf{u}\rVert=1$ increases the prediction most, and by how much?

</li>

<li>

If you give the floor area in $10\,\mathrm m^2$, the weight $w_1=3$ becomes $30$. What is the steepest direction now? What does this teach you about the theorem on steepest ascent?

</li>

</ol>

:::loesung
(a) $\partial_k(\mathbf{a}^{\top}\mathbf{x}+b)=a_k$, so $\nabla f=\mathbf{a}$ everywhere. For $d=2$, the contour lines are the lines $a_1x_1+a_2x_2+b=c$; they are parallel to one another and perpendicular to $\mathbf{a}$.

(b) The gradient with respect to $\mathbf{x}$ is $\mathbf{w}=(3,\,10,\,-4)^{\top}$ with $\lVert\mathbf{w}\rVert=\sqrt{9+100+16}=\sqrt{125}\approx11.18$. The steepest change of length $1$ is $\mathbf{u}=\mathbf{w}/\sqrt{125}\approx(0.268,\ 0.894,\ -0.358)^{\top}$, and it increases the prediction by about $11.18$ thousand euros: a little more floor area, considerably more rooms and a little closer to the center.

(c) In the new units, $\mathbf{w}'=(30,\,10,\,-4)^{\top}$ with $\lVert\mathbf{w}'\rVert=\sqrt{1016}\approx31.87$, and the steepest direction is $\mathbf{w}'/\lVert\mathbf{w}'\rVert\approx(0.941,\ 0.314,\ -0.125)^{\top}$: now it lies almost entirely in the floor area. The same apartment, the same prices, but a different steepest direction. The theorem on steepest ascent compares steps of equal Euclidean length in the chosen coordinates, and what “length $1$” means depends on the units, just like the distances in [Chapter 1, Section 4.2](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2). For features in different units, the steepest direction becomes meaningful only after the standardization from [Chapter 1, Section 4.5](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-5).
:::
:::

:::aufgabe Exercise 16 ★★★ When does the steepest descent point to the center?
<span class="anker" id="aufg-16"></span>

Let $f(\mathbf{x})=a\,x_1^2+b\,x_2^2$ with numbers $a,b>0$.

<ol class="al">

<li>

Show: $-\nabla f(\mathbf{x})$ is a positive multiple of $-\mathbf{x}$ if and only if $a=b$ or $\mathbf{x}$ lies on one of the axes ($\mathbf{x}\ne\mathbf{0}$).

</li>

<li>

For $a=1$, $b=4$, compute the angle between $-\nabla f$ and $-\mathbf{x}$ at the points $(1,\,1)$, $(2,\,1)$ and $(4,\,1)$. How does it change as you move outward along the line $x_2=1$?

</li>

</ol>

:::loesung
(a) We have $-\nabla f(\mathbf{x})=(-2ax_1,\,-2bx_2)^{\top}$. This vector equals $c\,(-x_1,\,-x_2)^{\top}$ with some $c>0$ if and only if $2ax_1=c\,x_1$ and $2bx_2=c\,x_2$. If both coordinates are nonzero, it follows that $2a=c=2b$, so $a=b$. If $x_1=0$, $c=2b$ suffices; if $x_2=0$, $c=2a$ suffices. So for a round bowl the steepest descent points to the origin everywhere, for an elongated one only on the axes.

(b) For $a=1$, $b=4$, we have $-\nabla f=(-2x_1,\,-8x_2)^{\top}$:

$$\begin{aligned} (1,\,1)&:\ \cos\varphi=\frac{2+8}{\sqrt{68}\,\sqrt2}\approx0.857,\ \varphi\approx31.0^\circ;\\ (2,\,1)&:\ \cos\varphi=\frac{8+8}{\sqrt{80}\,\sqrt5}=0.8,\ \varphi\approx36.9^\circ;\\ (4,\,1)&:\ \cos\varphi=\frac{32+8}{\sqrt{128}\,\sqrt{17}}\approx0.857,\ \varphi\approx31.0^\circ . \end{aligned}$$

Along the line $x_2=1$, the angle first increases from $0^\circ$ at $x_1=0$ and then decreases again; far out, the point lies almost in the direction of the $x_1$-axis, and there the steepest descent again points almost to the center.
:::
:::
