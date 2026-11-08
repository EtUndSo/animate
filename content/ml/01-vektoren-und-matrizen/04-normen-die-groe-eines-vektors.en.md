---
title: Norms: the size of a vector
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15210400
summary: How large is a vector?
tags: Euclidean norm, length, normalized, normalizing, 1-norm, maximum norm, norm, triangle inequality
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
How large is a vector? There are several correct answers to this question. This section presents the three most important ones, clarifies what they have in common and shows what they are needed for: to measure how large an error is.
:::

### The Euclidean norm

<span class="anker" id="stufe-3-1"></span>

The obvious size of an arrow is its length. In the plane, the Pythagorean theorem gives it: the arrow $(3,\,-4)^{\top}$ is the hypotenuse of a right triangle with legs $3$ and $4$, so its length is $\sqrt{3^2+4^2}=5$. In space you apply Pythagoras twice and get the square root of the sum of the three squares. The same formula is used in every dimension.

:::definition Definition 3.1 (Euclidean norm)
<span class="anker" id="satz-3-1"></span>

The __Euclidean norm__ of a vector $\mathbf{x}\in\mathbb{R}^d$ is

<span class="anker" id="gl-3-1"></span>
$$\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}=\sqrt{x_1^2+x_2^2+\dots+x_d^2} . \tag{3.1}$$

Without a subscript, $\lVert\mathbf{x}\rVert$ in this series always means the Euclidean norm.
:::

It is also called the __length__ of the vector or, because of the squares, the $L_2$ norm. A vector of length $1$ is called __normalized__. If you divide a vector $\mathbf{x}\ne\mathbf{0}$ by its length, then $\mathbf{x}/\lVert\mathbf{x}\rVert$ is normalized and points in the same direction. This step is called __normalizing__.

⁠**Worked example:** The vector $\mathbf{x}=(3,\,-4)^{\top}$ has length $\lVert\mathbf{x}\rVert_2=5$ (Fig. [12](#abb-12)). Normalized, it is $\mathbf{x}/5=(0.6,\ -0.8)^{\top}$. In space, $\lVert(1,\,2,\,2)^{\top}\rVert=\sqrt{1+4+4}=3$.

:::abbildung ml/k1rl2 12
The Euclidean norm of $(3,\,-4)^{\top}$: square the components, add, take the square root. The minus sign disappears when squaring.
:::

⁠**In short:** The Euclidean norm is the length of the arrow, the square root of the sum of the squared components.

### The 1-norm

<span class="anker" id="stufe-3-2"></span>

In a city with a rectangular street grid, a taxi cannot drive diagonally through the blocks. To get from the origin to the point $(3,\,-4)^{\top}$, it drives $3$ blocks in one direction and $4$ blocks in the other, $7$ blocks in total. The 1-norm measures this length.

:::definition Definition 3.2 (1-norm)
<span class="anker" id="satz-3-2"></span>

The __1-norm__ of a vector $\mathbf{x}\in\mathbb{R}^d$ is

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{x}\rVert_1=|x_1|+|x_2|+\dots+|x_d|=\sum_{j=1}^d|x_j| . \tag{3.2}$$
:::

It is also called the $L_1$ norm or, after the street grid of Manhattan, the Manhattan norm.

⁠**Worked example:** For $\mathbf{x}=(3,\,-4)^{\top}$, $\lVert\mathbf{x}\rVert_1=7$ (Fig. [13](#abb-13)), and $\lVert(1,\,2,\,2)^{\top}\rVert_1=1+2+2=5$.

:::abbildung ml/k1rl1 13
The 1-norm of $\mathbf{x}=(3,\,-4)^{\top}$: add the absolute values of the components.
:::

Here the 1-norm is larger than the Euclidean length, because the detour along the streets is longer than the straight line.

⁠**In short:** The 1-norm adds the absolute values of the components; it is the route through a rectangular street grid.

### The maximum norm

<span class="anker" id="stufe-3-3"></span>

In a quality inspection, often only the worst deviation matters. A part has three dimensions, and each may deviate from its nominal value by at most $0.1$ mm. Whether the part passes is decided by the largest of the three deviations alone.

:::definition Definition 3.3 (Maximum norm)
<span class="anker" id="satz-3-3"></span>

The __maximum norm__ of a vector $\mathbf{x}\in\mathbb{R}^d$ is the largest absolute value of a component:

<span class="anker" id="gl-3-3"></span>
$$\lVert\mathbf{x}\rVert_\infty=\max_{j=1,\dots,d}|x_j| . \tag{3.3}$$
:::

It is also called the $L_\infty$ norm. The reason for the infinity symbol is given in the next subsection.

⁠**Worked example:** $\lVert(3,\,-4)^{\top}\rVert_\infty=4$ and $\lVert(1,\,2,\,2)^{\top}\rVert_\infty=2$. If the deviations of a part are $(0.05,\ -0.08,\ 0.02)$ mm, their maximum norm is $0.08$ mm, and the part passes.

⁠**In short:** The maximum norm is the largest absolute value of a component, the worst single deviation.

### What makes a norm

<span class="anker" id="stufe-3-4"></span>

The three norms measure differently, but they share three properties that you expect from any measure of size. Only the zero vector has size zero. A vector twice as long is twice as large. And a detour is never shorter than the direct route.

:::definition Definition 3.4 (Norm)
<span class="anker" id="satz-3-4"></span>

A __norm__ on $\mathbb{R}^d$ assigns a real number $\lVert\mathbf{x}\rVert$ to every vector $\mathbf{x}$ such that for all $\mathbf{u},\mathbf{v},\mathbf{x}\in\mathbb{R}^d$ and all scalars $c$:

<ol>

<li>

$\lVert\mathbf{x}\rVert\ge0$, and $\lVert\mathbf{x}\rVert=0$ only for $\mathbf{x}=\mathbf{0}$;

</li>

<li>

$\lVert c\,\mathbf{x}\rVert=|c|\,\lVert\mathbf{x}\rVert$;

</li>

<li>

$\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ (__triangle inequality__).

</li>

</ol>
:::

The triangle inequality takes its name from a triangle formed by the arrows $\mathbf{u}$, $\mathbf{v}$ and $\mathbf{u}+\mathbf{v}$: the side $\mathbf{u}+\mathbf{v}$ is never longer than the other two together.

**The $p$-norms.** The 1-norm and the Euclidean norm are two cases of a whole family. For every number $p\ge1$, the __$p$-norm__ is

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{x}\rVert_p=\Bigl(\sum_{j=1}^d|x_j|^p\Bigr)^{1/p} . \tag{3.4}$$

For $p=1$ this is the 1-norm, for $p=2$ the Euclidean norm. The larger $p$ is, the more the largest component dominates the sum. For $p\to\infty$ only this component remains; that is why the maximum norm is written $\lVert\cdot\rVert_\infty$.

**The unit sphere.** You can see how a norm measures by looking at the set of all vectors of size $1$. It is called the __unit sphere__ of the norm, even though it need not be a sphere (Fig. [14](#abb-14)). For the Euclidean norm in the plane, it is the circle with radius $1$. For the 1-norm, it is the diamond $|x_1|+|x_2|=1$: in each quadrant this is a line segment, for example $x_1+x_2=1$ for $x_1,x_2\ge0$. For the maximum norm, it is the square with corners $(\pm1,\,\pm1)$, because on this square the larger of the two components has absolute value exactly $1$.

:::abbildung ml/k1einheitskugeln 14
The unit spheres of three norms in the plane: the diamond of the 1-norm (left, orange), the circle of the Euclidean norm (middle, blue) and the square of the maximum norm (right, green); in each panel the other two are shown in gray for comparison. All three pass through the points $(\pm1,\,0)$ and $(0,\,\pm1)$.
:::

⁠**Worked example:** For $\mathbf{x}=(3,\,-4)^{\top}$, we get $\lVert\mathbf{x}\rVert_1=7$, $\lVert\mathbf{x}\rVert_2=5$, $\lVert\mathbf{x}\rVert_3=91^{1/3}\approx4.498$, $\lVert\mathbf{x}\rVert_{10}=1\,107\,625^{1/10}\approx4.022$ (Fig. [15](#abb-15)) and $\lVert\mathbf{x}\rVert_\infty=4$. As $p$ grows, the $p$-norm approaches the largest absolute value of a component, here $4$. The reason can already be seen in the sum: for $p=10$, $4^{10}$ is almost eighteen times as large as $3^{10}$, and the root of the sum is hardly larger than the root of $4^{10}$ alone.

:::abbildung ml/k1rlp 15
Two $p$-norms of $\mathbf{x}=(3,\,-4)^{\top}$, for $p=3$ and $p=10$. The larger $p$ is, the more the term of the largest component dominates.
:::

That the 1-norm satisfies conditions (N1) to (N3) can be checked directly: (N1) and (N2) hold because $|x_j|\ge0$ and $|c\,x_j|=|c|\,|x_j|$. (N3) follows from the triangle inequality for numbers, $|u_j+v_j|\le|u_j|+|v_j|$, summed over all $j$. The maximum norm works the same way. For the Euclidean norm, the triangle inequality is intuitively clear, because the direct route between two points is never longer than a detour via a third point.

⁠**In short:** A norm measures the size of a vector in such a way that only the zero vector has size zero, multiples grow accordingly and the triangle inequality holds; the $p$-norms form a family that includes $L_1$, $L_2$ and $L_\infty$.

:::hintergrund Why $p\ge1$ is required and why the “zero norm” is not a norm
For $p<1$, formula [(3.4)](#gl-3-4) violates the triangle inequality. With $p=\tfrac12$, we have $\lVert(1,0)^{\top}\rVert_{1/2}=1$ and $\lVert(0,1)^{\top}\rVert_{1/2}=1$, but $\lVert(1,1)^{\top}\rVert_{1/2}=(1+1)^2=4>1+1$. Its “unit sphere” is dented inward; it has the shape of a star.

You often read about an “$L_0$ norm”: the number of components that are not zero. It is a useful measure of how many features a vector actually uses. Still, it is not a norm, because it violates (N2): the vector $2\mathbf{x}$ has just as many nonzero components as $\mathbf{x}$, not twice as many.
:::

:::hintergrund Not every norm comes from a dot product
The Euclidean norm is built from the dot product, $\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$. An equation called the parallelogram law follows from this. Expanding with the rules for the dot product gives

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,\qquad \lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,$$

and adding the two lines gives $\lVert\mathbf{u}+\mathbf{v}\rVert^2+\lVert\mathbf{u}-\mathbf{v}\rVert^2=2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2$: in a parallelogram, the sum of the squares of the two diagonals equals the sum of the squares of the four sides. Every norm that comes from a dot product must satisfy this equation. The 1-norm does not: with $\mathbf{u}=\mathbf{e}_1$ and $\mathbf{v}=\mathbf{e}_2$, the left side is $\lVert(1,1)^{\top}\rVert_1^2+\lVert(1,-1)^{\top}\rVert_1^2=4+4=8$, but the right side is $2+2=4$. So there is no dot product whose length is the 1-norm. This is why the 1-norm cannot measure angles the way the dot product does.
:::

### The error vector and its size

<span class="anker" id="stufe-3-5"></span>

A model provides predictions, and at some point you learn the actual values. Then you want to know how good the predictions were. For each example there is a deviation, and these deviations form a vector. Its norm is a measure of the size of the error as a whole.

:::definition Definition 3.5 (Error vector)
<span class="anker" id="satz-3-5"></span>

If $\hat y_1,\dots,\hat y_N$ are the predictions of a model for $N$ examples and $y_1,\dots,y_N$ are the actual values, then the vector

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{y}}-\mathbf{y}=(\hat y_1-y_1,\,\dots,\,\hat y_N-y_N)^{\top} \tag{3.5}$$

is called the __error vector__. Here $\hat{\mathbf{y}}=(\hat y_1,\dots,\hat y_N)^{\top}$ is the vector of predictions and $\mathbf{y}=(y_1,\dots,y_N)^{\top}$ the vector of actual values.
:::

Which norm you apply to the error vector is a decision about which errors you fear most. The sign plays no role, because every norm gives $\mathbf{y}-\hat{\mathbf{y}}$ the same size as $\hat{\mathbf{y}}-\mathbf{y}$.

⁠**Worked example:** The four apartments have been sold, and their actual prices were $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$ thousand euros. Two appraisers, A and B, had made estimates beforehand:

$$\hat{\mathbf{y}}_{\mathrm A}=(210,\,120,\,300,\,230)^{\top},\qquad \hat{\mathbf{y}}_{\mathrm B}=(200,\,130,\,290,\,280)^{\top}.$$

Their error vectors are $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}=(10,\,-10,\,10,\,-10)^{\top}$ and $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}=(0,\,0,\,0,\,40)^{\top}$. Appraiser A is always a little off; appraiser B is exactly right three times and far off once. The three norms judge differently (Table [2](#tab-2)). The Euclidean norms are computed in Fig. [16](#abb-16).

:::abbildung ml/k1rfehler 16
The Euclidean norms of the two error vectors in thousand euros. With $1\,600$, the single large error of B contributes four times as much to the sum of squares as the four small errors of A together.
:::

<span class="anker" id="tab-2"></span>

**Table 2:** The norms of the error vectors of two appraisers, in thousand euros.

|  | $\lVert\cdot\rVert_1$ | $\lVert\cdot\rVert_2$ | $\lVert\cdot\rVert_\infty$ |
|---|---|---|---|
| Appraiser A, $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}$ | $40$ | $\sqrt{4\cdot100}=20$ | $10$ |
| Appraiser B, $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}$ | $40$ | $\sqrt{1600}=40$ | $40$ |

By the 1-norm, both are equally good: each is off by $40$ thousand euros in total. By the Euclidean norm, A is twice as good, and by the maximum norm four times as good. If you consider every thousand euros of deviation equally bad, no matter for which apartment, you measure with $L_1$. If you consider one large outlier worse than many small errors, you measure with $L_2$. If you fear only the worst case, you measure with $L_\infty$.

⁠**In short:** The error vector collects the deviations of all predictions; its norm measures the size of the error, and the choice of norm determines which errors count most.

:::hintergrund Why the sum of squares punishes large errors and almost overlooks small ones
In the Euclidean norm, each deviation enters as a square. A deviation of $0.1$ contributes $0.01$, but a deviation of $10$ contributes $100$. Squaring makes small numbers smaller and large numbers larger. A single large error of $40$ therefore contributes $1600$, four times as much as four errors of $10$ each together. The 1-norm, by contrast, grows equally fast everywhere: each unit of deviation costs the same, whether it belongs to a small or a large error. This is also why it clearly distinguishes between “exactly zero” and “a little off”, while the sum of squares makes hardly any difference between the two. Which property you want depends on the task, and that is precisely why there are several norms.
:::

### The RMS value

<span class="anker" id="stufe-3-6"></span>

The Euclidean norm grows with the number of components. If you rate one appraiser on four apartments and another on four hundred, the second has a much longer error vector, even if the estimates per apartment are just as good. If you want to compare errors per example, you have to factor out the number of components.

:::definition Definition 3.6 (RMS value)
<span class="anker" id="satz-3-6"></span>

The __RMS value__ of a vector $\mathbf{x}\in\mathbb{R}^n$ is

<span class="anker" id="gl-3-6"></span>
$$\operatorname{rms}(\mathbf{x})=\frac{\lVert\mathbf{x}\rVert}{\sqrt n}=\sqrt{\frac1n\sum_{i=1}^nx_i^2} . \tag{3.6}$$
:::

The abbreviation rms stands for *root mean square*: the square root of the mean of the squares. The RMS value is a typical magnitude of a component. If all components have the same absolute value $a$, the RMS value is exactly $a$.

The name is familiar from electrical engineering: the RMS value of an AC voltage is the square root of the time average of its square. For a sampled signal, [(3.6)](#gl-3-6) is the same calculation with samples instead of an integral. If you sample a sine over exactly one period at $n\ge3$ evenly spaced points, you even get exactly the RMS value $1/\sqrt2$ of the sine.

⁠**Worked example:** The error vectors of the appraisers from the previous subsection have the RMS values $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y})=20/\sqrt4=10$ and $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y})=40/\sqrt4=20$ thousand euros: A is typically off by $10$ thousand euros. A sine with amplitude $1$, sampled at four evenly spaced points of one period, has the samples $\mathbf{x}=(0,\,1,\,0,\,-1)^{\top}$ and the RMS value $1/\sqrt2\approx0.707$ (Fig. [17](#abb-17)).

:::abbildung ml/k1rrms 17
The RMS value of a sampled sine: add the squares, divide by the number of components, take the square root.
:::

⁠**In short:** The RMS value $\lVert\mathbf{x}\rVert/\sqrt n$ is the typical magnitude of a component and makes vectors with different numbers of components comparable.

:::hintergrund How many components can be large?
The RMS value limits how many components can have a large absolute value. If $k$ of the $n$ components have an absolute value of at least $a>0$, then these $k$ components alone contribute at least $k\,a^2$ to the sum of squares. The whole sum of squares is $n\operatorname{rms}(\mathbf{x})^2$, so $k\,a^2\le n\operatorname{rms}(\mathbf{x})^2$, or

$$\frac kn\le\Bigl(\frac{\operatorname{rms}(\mathbf{x})}{a}\Bigr)^2 .$$

So at most the fraction $(\operatorname{rms}/a)^2$ of the components can have an absolute value of at least $a$. At most a quarter of the components can reach twice the RMS value, and at most one percent ten times the RMS value. For appraiser B with $\operatorname{rms}=20$, at most $(20/30)^2=4/9\approx44$ % of the errors can be $30$ or more; in fact it is one of four, that is, $25$ %. This bound is called Chebyshev's inequality.
:::

:::aufgabe Exercise 7 ★ Computing norms
<span class="anker" id="aufg-7"></span>

Let $\mathbf{x}=(2,\,-1,\,0,\,2)^{\top}$.

<ol class="al">

<li>

Compute $\lVert\mathbf{x}\rVert_1$, $\lVert\mathbf{x}\rVert_2$, $\lVert\mathbf{x}\rVert_3$ and $\lVert\mathbf{x}\rVert_\infty$, as well as the normalized vector $\mathbf{x}/\lVert\mathbf{x}\rVert$.

</li>

<li>

Check that $\lVert\mathbf{x}\rVert_\infty\le\lVert\mathbf{x}\rVert_2\le\lVert\mathbf{x}\rVert_1$. Explain why this order holds for every vector.

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{x}\rVert_1=2+1+0+2=5$, $\lVert\mathbf{x}\rVert_2=\sqrt{4+1+0+4}=3$, $\lVert\mathbf{x}\rVert_3=(8+1+0+8)^{1/3}=17^{1/3}\approx2.571$ and $\lVert\mathbf{x}\rVert_\infty=2$. The normalized vector is $\mathbf{x}/3=(\tfrac23,\,-\tfrac13,\,0,\,\tfrac23)^{\top}$ with length $\sqrt{(4+1+4)/9}=1$.

(b) We have $2\le3\le5$, and $\lVert\mathbf{x}\rVert_3$, at $2.571$, also lies in between. In general: if $|x_k|$ is the largest absolute value of a component, then $\lVert\mathbf{x}\rVert_\infty^2=x_k^2\le\sum_jx_j^2=\lVert\mathbf{x}\rVert_2^2$, because the sum contains $x_k^2$ and otherwise only nonnegative terms. And $\lVert\mathbf{x}\rVert_1^2=\bigl(\sum_j|x_j|\bigr)^2=\sum_jx_j^2+\sum_{j\ne l}|x_j|\,|x_l|\ge\lVert\mathbf{x}\rVert_2^2$, because the cross terms are nonnegative. Intuitively: the straight-line distance is never longer than the route through the street grid and never shorter than the longest single leg.
:::
:::

:::aufgabe Exercise 8 ★★ How good are the real estate agent's estimates?
<span class="anker" id="aufg-8"></span>

The real estate agent from Subsection [2.2](das-skalarprodukt.html#stufe-2-2) had the predictions $\hat{\mathbf{y}}=(188,\,126,\,286,\,232)^{\top}$; the actual prices were $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$ thousand euros.

<ol class="al">

<li>

Compute the error vector, its three norms and its RMS value. For which apartment is she furthest off?

</li>

<li>

What do you notice about the signs? From now on, the real estate agent adds $7$ thousand euros to every prediction. Compute the new error vector and its norms. Has she improved according to all three norms?

</li>

</ol>

:::loesung
(a) The error vector is $\hat{\mathbf{y}}-\mathbf{y}=(188-200,\ 126-130,\ 286-290,\ 232-240)^{\top}=(-12,\,-4,\,-4,\,-8)^{\top}$. Its norms: $\lVert\cdot\rVert_1=28$, $\lVert\cdot\rVert_2=\sqrt{144+16+16+64}=\sqrt{240}\approx15.49$, $\lVert\cdot\rVert_\infty=12$, RMS value $\sqrt{240}/2\approx7.75$ thousand euros. She is furthest off for apartment 1, by $12$ thousand euros.

(b) All errors are negative: the real estate agent consistently estimates too low, and her error has a DC component. With the $7$ thousand euros added, the error vector becomes $(-5,\,3,\,3,\,-1)^{\top}$ with $\lVert\cdot\rVert_1=12$, $\lVert\cdot\rVert_2=\sqrt{25+9+9+1}=\sqrt{44}\approx6.63$, $\lVert\cdot\rVert_\infty=5$ and the RMS value $\sqrt{44}/2\approx3.32$. She has improved according to all three norms. The added amount $7$ is exactly the mean of the absolute errors, $(12+4+4+8)/4=7$: it removes the DC component of the error and leaves only the AC component.
:::
:::
