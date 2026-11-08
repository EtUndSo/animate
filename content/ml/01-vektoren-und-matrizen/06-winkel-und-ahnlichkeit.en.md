---
title: Angles and similarity
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15210600
summary: Two vectors can point in similar directions even if they have different lengths.
tags: angle, orthogonal, cosine similarity
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Two vectors can point in similar directions even if they have different lengths. This section measures the angle between them. It is based on an inequality that, in addition, states exactly when a comparison with a pattern responds most strongly.
:::

### The Cauchy–Schwarz inequality

<span class="anker" id="stufe-5-1"></span>

How large can the dot product of two vectors become if their lengths are fixed? An experiment: $\mathbf{u}=(1,\,2,\,2)^{\top}$ has length $3$, and $\mathbf{v}=(2,\,0,\,1)^{\top}$ has length $\sqrt5\approx2.24$. Their dot product is $2+0+2=4$, clearly less than the product of the lengths, $3\cdot2.24\approx6.71$. If you take $\mathbf{v}=2\mathbf{u}$ instead, a vector in the same direction with length $6$, then $\mathbf{u}^{\top}(2\mathbf{u})=2\cdot9=18=3\cdot6$: exactly the product of the lengths. It cannot get any larger.

:::satz Theorem 5.1 (Cauchy–Schwarz inequality)
<span class="anker" id="satz-5-1"></span>

For all $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$,

<span class="anker" id="gl-5-1"></span>
$$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert . \tag{5.1}$$

Equality holds if and only if one of the two vectors is a multiple of the other.
:::

:::beweis Cauchy–Schwarz inequality
If $\mathbf{v}=\mathbf{0}$, both sides are zero. Otherwise, consider the vector $\mathbf{u}-t\,\mathbf{v}$ for an arbitrary number $t$. The square of its length is never negative, and by the rules for the dot product

$$0\le\lVert\mathbf{u}-t\,\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2t\,\mathbf{u}^{\top}\mathbf{v}+t^2\lVert\mathbf{v}\rVert^2 .$$

This holds for every $t$, and so also for $t=\mathbf{u}^{\top}\mathbf{v}/\lVert\mathbf{v}\rVert^2$, the point at which the right-hand side, as a parabola in $t$, is smallest. Substituting gives

$$0\le\lVert\mathbf{u}\rVert^2-2\,\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}+\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}=\lVert\mathbf{u}\rVert^2-\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}.$$

Multiplied by $\lVert\mathbf{v}\rVert^2>0$, this means $(\mathbf{u}^{\top}\mathbf{v})^2\le\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$; its square root is [(5.1)](#gl-5-1).

Equality holds if and only if $\lVert\mathbf{u}-t\,\mathbf{v}\rVert=0$ for this $t$, that is, $\mathbf{u}=t\,\mathbf{v}$. Conversely, for $\mathbf{u}=c\,\mathbf{v}$ we do get $|\mathbf{u}^{\top}\mathbf{v}|=|c|\,\lVert\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$.
:::

⁠**Worked example:** For $\mathbf{u}=(1,\,2,\,2)^{\top}$ and $\mathbf{v}=(2,\,0,\,1)^{\top}$, $|\mathbf{u}^{\top}\mathbf{v}|=4\le3\cdot\sqrt5\approx6.71$. The inequality is strict because $\mathbf{v}$ is not a multiple of $\mathbf{u}$.

With the inequality, you can now prove what was justified only intuitively in Subsection [3.4](normen-die-groe-eines-vektors.html#stufe-3-4): the triangle inequality of the Euclidean norm. We have

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2\le\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2=\bigl(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert\bigr)^2 ,$$

and its square root is (N3).

⁠**In short:** In absolute value, the dot product is at most the product of the lengths, and it equals this product exactly when the vectors lie on a line through the origin.

:::hintergrund Why the dot product recognizes patterns: the precise statement
In Subsection [2.4](das-skalarprodukt.html#stufe-2-4), the comparison with a pattern was an intuitive picture: the dot product $\mathbf{w}^{\top}\mathbf{x}$ is large if the signal follows the pattern. The Cauchy–Schwarz inequality turns this into a precise statement. If you compare only signals with the same length $\lVert\mathbf{x}\rVert$, then $\mathbf{w}^{\top}\mathbf{x}$ always lies between $-\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$ and $+\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$. The largest value is reached exactly by the signal that is a positive multiple of the pattern, and the smallest by the negative multiple. So among all signals with the same energy, the comparison responds most strongly to the pattern itself.

⁠**Worked example:** The alternating pattern $\mathbf{w}=(1,-1,1,-1)^{\top}$ has length $2$. Among all signals of length $2$, $\mathbf{x}=\mathbf{w}$ gives the largest value $4=2\cdot2$, the signal $(2,0,0,0)^{\top}$ gives only $2$, and $\mathbf{x}=-\mathbf{w}$ gives the smallest value $-4$.

In communications engineering, this is the basis of the correlation receiver and the matched filter. Such a filter has the time-reversed transmitted signal as its impulse response; at the sampling instant, it therefore computes exactly the dot product of the received signal and the transmitted signal. That this filter maximizes the signal-to-noise ratio is proved with precisely this inequality.
:::

### The angle between two vectors

<span class="anker" id="stufe-5-2"></span>

Two arrows starting from the origin enclose an angle. It tells you how similar their directions are, regardless of how long they are. In the plane you can measure it with a protractor. For vectors with many components you need a formula, and the dot product provides it.

:::herleitung The dot product in the plane
The arrows $\mathbf{u}$ and $\mathbf{v}$ and their connecting arrow $\mathbf{u}-\mathbf{v}$ form a triangle. If $\varphi$ is the angle between $\mathbf{u}$ and $\mathbf{v}$, the law of cosines from school geometry says

$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

By [(4.1)](abstande-und-einheiten.html#gl-4-1), the same left-hand side equals $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}$. Comparing the two lines leaves

$$\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

So in the plane and in space, the dot product is the product of the lengths times the cosine of the enclosed angle.
:::

In higher dimensions there is no protractor. So you reverse the derivation and use the formula as a definition.

:::definition Definition 5.2 (Angle)
<span class="anker" id="satz-5-2"></span>

For $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$, both different from $\mathbf{0}$, the __angle__ $\varphi$ between $\mathbf{u}$ and $\mathbf{v}$ is the number $\varphi\in[0^\circ,180^\circ]$ with

<span class="anker" id="gl-5-2"></span>
$$\cos\varphi=\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert} . \tag{5.2}$$
:::

This definition is only possible because, by the Cauchy–Schwarz inequality, the right-hand side always lies between $-1$ and $1$. For each such number there is exactly one angle between $0^\circ$ and $180^\circ$. The sign of the dot product tells you whether the angle is acute ($\mathbf{u}^{\top}\mathbf{v}>0$), right ($\mathbf{u}^{\top}\mathbf{v}=0$) or obtuse ($\mathbf{u}^{\top}\mathbf{v}<0$).

⁠**Worked example:** For $(1,\,0)^{\top}$ and $(1,\,1)^{\top}$, $\cos\varphi=1/\sqrt2$, so $\varphi=45^\circ$. For $(1,\,0,\,1)^{\top}$ and $(1,\,1,\,0)^{\top}$, $\cos\varphi=\tfrac12$, so $\varphi=60^\circ$ (Fig. [22](#abb-22)). For $\mathbf{u}=(1,\,2,\,2)^{\top}$ and $\mathbf{v}=(2,\,0,\,1)^{\top}$, $\cos\varphi=4/(3\sqrt5)\approx0.596$, so $\varphi\approx53.4^\circ$.

:::abbildung ml/k1rwinkel 22
The angle between $(1,\,0,\,1)^{\top}$ and $(1,\,1,\,0)^{\top}$: the dot product in the numerator, the two lengths in the denominator.
:::

⁠**In short:** The cosine of the angle between two vectors is their dot product divided by the product of their lengths.

### Orthogonal vectors

<span class="anker" id="stufe-5-3"></span>

If the dot product of two vectors is zero, neither contributes anything in the direction of the other. In the plane, the arrows are then perpendicular to each other. This case is so important that it has its own name.

:::definition Definition 5.3 (Orthogonal)
<span class="anker" id="satz-5-3"></span>

Two vectors $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ are called __orthogonal__ if $\mathbf{u}^{\top}\mathbf{v}=0$.
:::

If both vectors are different from $\mathbf{0}$, their angle is exactly $90^\circ$ by [(5.2)](#gl-5-2). The zero vector is orthogonal to every vector.

:::satz Theorem 5.4 (Pythagorean theorem)
<span class="anker" id="satz-5-4"></span>

If $\mathbf{u}$ and $\mathbf{v}$ are orthogonal, then $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2$.
:::

This follows immediately from $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$, because the middle term is zero.

⁠**Worked example 1:** $(1,\,2,\,2)^{\top}$ and $(2,\,0,\,-1)^{\top}$ are orthogonal, because $2+0-2=0$. Their sum $(3,\,2,\,1)^{\top}$ has the squared length $14=9+5$.

⁠**Worked example 2: two patterns that do not interfere.** The constant pattern $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ and the alternating pattern $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$ from Subsection [2.4](das-skalarprodukt.html#stufe-2-4) are orthogonal, $\mathbf 1^{\top}\mathbf{w}=0$. A signal consisting of $2$ times the constant pattern and $1$ times the alternating pattern is $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}=(3,\,1,\,3,\,1)^{\top}$. The comparison with the constant pattern gives $\mathbf 1^{\top}\mathbf{x}=8=2\cdot4$, the comparison with the alternating pattern $\mathbf{w}^{\top}\mathbf{x}=4=1\cdot4$ (Fig. [23](#abb-23)). Each comparison finds exactly its own share, times $\lVert\mathbf 1\rVert^2=\lVert\mathbf{w}\rVert^2=4$; the other share does not interfere with it.

:::abbildung ml/k1rortho 23
The two patterns are orthogonal (top). Comparing the signal $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}$ with each pattern gives that pattern's share times $4$.
:::

⁠**In short:** Orthogonal means that the dot product is zero; orthogonal arrows are perpendicular to each other, and the Pythagorean theorem holds for them.

:::hintergrund Why orthogonal patterns do not interfere, and what this has to do with Fourier coefficients
If a signal is a linear combination $\mathbf{x}=\alpha\,\mathbf 1+\beta\,\mathbf{w}$ of two orthogonal patterns, the rules give

$$\mathbf 1^{\top}\mathbf{x}=\alpha\,\mathbf 1^{\top}\mathbf 1+\beta\,\mathbf 1^{\top}\mathbf{w}=\alpha\,\lVert\mathbf 1\rVert^2+0 ,\qquad\text{so}\qquad \alpha=\frac{\mathbf 1^{\top}\mathbf{x}}{\lVert\mathbf 1\rVert^2} .$$

So the comparison with a pattern measures only that pattern's own share, because the contribution of the other pattern vanishes with the factor $\mathbf 1^{\top}\mathbf{w}=0$. If the patterns were not orthogonal, each comparison would also count part of the other share.

The coefficients of a Fourier series are built in exactly this way. For a signal $s(t)$ with period $T$ and $\omega_0=2\pi/T$,

$$a_k=\frac{2}{T}\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t=\frac{\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t}{\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t}\qquad(k\ge1),$$

because $\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t=T/2$. The integral of a product of two functions plays the role of the dot product, and the cosine and sine functions of different frequencies are orthogonal in this sense: the integral of their product over one period is zero. That is why you can compute each Fourier coefficient on its own without knowing the others.
:::

### Cosine similarity

<span class="anker" id="stufe-5-4"></span>

Sometimes the length of a vector is beside the point. A text can be described by a vector whose component $j$ counts how often word $j$ of a fixed word list occurs in the text. A detailed report on a soccer game contains the words “goal” and “ball” more often than a short news item about the same game, but in the same ratio. The two vectors have different lengths but point in the same direction. For the content, the direction is what counts.

:::definition Definition 5.5 (Cosine similarity)
<span class="anker" id="satz-5-5"></span>

The __cosine similarity__ of two vectors $\mathbf{u},\mathbf{v}\ne\mathbf{0}$ is the number

<span class="anker" id="gl-5-3"></span>
$$\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert}\in[-1,\,1] , \tag{5.3}$$

that is, the cosine of their angle.
:::

It is $1$ if the vectors point in the same direction, $0$ if they are orthogonal, and $-1$ if they point in opposite directions. If you multiply one of the vectors by a positive number, it does not change, because the number cancels out.

⁠**Worked example:** Three texts and their counts of the words “goal”, “ball” and “election”:

$$\mathbf{x}_1=(3,\,2,\,0)^{\top},\qquad \mathbf{x}_2=(6,\,4,\,0)^{\top},\qquad \mathbf{x}_3=(0,\,1,\,3)^{\top} .$$

Text 2 is a report twice as long about the same game; text 3 is mainly about an election. The cosine similarity of text 1 and text 2 is $1$, that of text 1 and text 3 is $2/\sqrt{130}\approx0.175$ (Fig. [24](#abb-24)). Likewise, that of text 2 and text 3 equals $4/(\sqrt{52}\,\sqrt{10})=4/\sqrt{520}\approx0.175$.

:::abbildung ml/k1rkosinus 24
Two cosine similarities of the word counts: in each case a dot product in the numerator and two lengths in the denominator.
:::

The distances, by contrast, are $\lVert\mathbf{x}_1-\mathbf{x}_2\rVert=\sqrt{13}\approx3.61$, $\lVert\mathbf{x}_1-\mathbf{x}_3\rVert=\sqrt{19}\approx4.36$ and $\lVert\mathbf{x}_2-\mathbf{x}_3\rVert=\sqrt{54}\approx7.35$. By distance, text 1 is hardly farther from text 3 than from text 2, even though text 2 has exactly the same topic. Cosine similarity recognizes this immediately: it is $1$, and the angle to text 3, at about $79.9^\circ$, is almost a right angle.

⁠**In short:** Cosine similarity compares only the directions of two vectors and ignores their lengths.

:::hintergrund Cosine similarity is not the same as correlation
If you first center two vectors with the same number of components (Subsection [4.3](abstande-und-einheiten.html#stufe-4-3)), the cosine of their angle measures whether the components lie above and below their respective means together. This number is called the correlation coefficient. Without centering, the result is often something entirely different. Example: $\mathbf{a}=(1,2,3)^{\top}$, $\mathbf{b}=(3,4,5)^{\top}$ and $\mathbf{c}=(3,2,1)^{\top}$. The cosine similarity of $\mathbf{a}$ and $\mathbf{b}$ is about $0.983$, and that of $\mathbf{a}$ and $\mathbf{c}$ is still $0.714$, so both are clearly positive. Centered, the vectors are $\tilde{\mathbf{a}}=(-1,0,1)^{\top}$, $\tilde{\mathbf{b}}=(-1,0,1)^{\top}$ and $\tilde{\mathbf{c}}=(1,0,-1)^{\top}$: the correlation coefficient of $\mathbf{a}$ and $\mathbf{b}$ is $1$, but that of $\mathbf{a}$ and $\mathbf{c}$ is $-1$, because $\mathbf{c}$ falls exactly where $\mathbf{a}$ rises. The uncentered cosine similarity was positive only because all the numbers are positive, so that all three vectors point in roughly the same direction.
:::

### The dot product as shadow length

<span class="anker" id="stufe-5-5"></span>

The dot product with a normalized vector has a simple geometric meaning. Imagine a line through the origin in the direction of the normalized vector $\mathbf{u}$, and let light fall perpendicularly onto this line. The arrow $\mathbf{x}$ then casts a shadow onto the line (Fig. [25](#abb-25)). How long is it?

:::abbildung ml/k1schatten 25
The shadow of the arrow $\mathbf{x}=(3,1)^{\top}$ on the line in the direction of the normalized vector $\mathbf{u}=(0.6,\,0.8)^{\top}$. The light falls perpendicularly onto the line (dashed). The shadow (light blue) has the length $\mathbf{u}^{\top}\mathbf{x}=\lVert\mathbf{x}\rVert\cos\varphi=2.6$ and ends at the point $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}=(1.56,\,2.08)^{\top}$.
:::

:::satz Theorem 5.6 (Shadow length)
<span class="anker" id="satz-5-6"></span>

Let $\mathbf{u}\in\mathbb{R}^d$ be normalized, that is, $\lVert\mathbf{u}\rVert=1$. Then $\mathbf{u}^{\top}\mathbf{x}$ is the signed length of the shadow of $\mathbf{x}$ on the line in the direction of $\mathbf{u}$: the shadow ends at the point $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$, and the connecting arrow $\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ is orthogonal to $\mathbf{u}$.
:::

:::beweis Shadow length
Since $\mathbf{u}^{\top}\mathbf{u}=\lVert\mathbf{u}\rVert^2=1$, we get $\mathbf{u}^{\top}\bigl(\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}\bigr)=\mathbf{u}^{\top}\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}^{\top}\mathbf{u}=0$. So the connecting arrow is perpendicular to the line; this is exactly the direction from which the light comes. The shadow point $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ is at distance $|\mathbf{u}^{\top}\mathbf{x}|$ from the origin, because $\mathbf{u}$ has length $1$. It lies in the direction of $\mathbf{u}$ if $\mathbf{u}^{\top}\mathbf{x}>0$, and in the opposite direction if $\mathbf{u}^{\top}\mathbf{x}<0$. In the right triangle formed by $\mathbf{x}$, the shadow and the connecting arrow, $\mathbf{x}$ is the hypotenuse; therefore the shadow length is also $\lVert\mathbf{x}\rVert\cos\varphi$.
:::

If $\mathbf{u}$ is not normalized, then $\mathbf{u}^{\top}\mathbf{x}$ is the shadow length of $\mathbf{x}$ in the direction of $\mathbf{u}$, multiplied by $\lVert\mathbf{u}\rVert$.

⁠**Worked example:** $\mathbf{u}=(0.6,\ 0.8)^{\top}$ is normalized, because $0.36+0.64=1$. For $\mathbf{x}=(3,\,1)^{\top}$, the shadow length is $\mathbf{u}^{\top}\mathbf{x}=2.6$ (Fig. [26](#abb-26)), the shadow point is $2.6\,\mathbf{u}=(1.56,\ 2.08)^{\top}$, and the connecting arrow is $\mathbf{x}-2.6\,\mathbf{u}=(1.44,\ -1.08)^{\top}$. It is orthogonal to $\mathbf{u}$: $0.6\cdot1.44-0.8\cdot1.08=0$. With $\lVert\mathbf{x}\rVert=\sqrt{10}\approx3.162$, we get $\cos\varphi=2.6/3.162\approx0.822$, so $\varphi\approx34.7^\circ$.

:::abbildung ml/k1rschatten 26
The shadow length of $\mathbf{x}$ in the direction of the normalized vector $\mathbf{u}$ as a dot product.
:::

For a weighted sum, this means: if the weights are normalized, $\mathbf{w}^{\top}\mathbf{x}$ states how far the example $\mathbf{x}$ reaches in the direction of $\mathbf{w}$. All points that give the same value $\mathbf{w}^{\top}\mathbf{x}$ cast the same shadow. In the plane they therefore lie on a line perpendicular to $\mathbf{w}$, and in space on a plane perpendicular to $\mathbf{w}$.

⁠**In short:** For a normalized vector $\mathbf{u}$, $\mathbf{u}^{\top}\mathbf{x}$ is the length of the shadow that $\mathbf{x}$ casts onto the line in the direction of $\mathbf{u}$.

:::aufgabe Exercise 12 ★ Angles and orthogonality
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Compute the angle between $(2,\,1,\,2)^{\top}$ and $(1,\,0,\,1)^{\top}$ and check the Cauchy–Schwarz inequality.

</li>

<li>

Are $(1,\,1,\,0)^{\top}$ and $(1,\,-1,\,3)^{\top}$ orthogonal?

</li>

<li>

Find a vector $\mathbf{v}\ne\mathbf{0}$ that is orthogonal to $\mathbf{u}=(1,\,2)^{\top}$, and check the Pythagorean theorem for $\mathbf{u}$ and $\mathbf{v}$.

</li>

</ol>

:::loesung
(a) The dot product is $2+0+2=4$, and the lengths are $3$ and $\sqrt2$. So $\cos\varphi=4/(3\sqrt2)\approx0.943$ and $\varphi\approx19.5^\circ$. Cauchy–Schwarz: $4\le3\sqrt2\approx4.243$.

(b) $1\cdot1+1\cdot(-1)+0\cdot3=0$: yes, they are orthogonal.

(c) For $\mathbf{v}=(v_1,v_2)^{\top}$, the condition requires $v_1+2v_2=0$. One solution is $\mathbf{v}=(2,\,-1)^{\top}$, and so is every nonzero multiple of it. Check of the Pythagorean theorem: $\mathbf{u}+\mathbf{v}=(3,\,1)^{\top}$ has the squared length $10$, and $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2=5+5=10$.
:::
:::

:::aufgabe Exercise 13 ★★ Which text is similar?
<span class="anker" id="aufg-13"></span>

Four texts; again the words “goal”, “ball” and “election” were counted: $\mathbf{x}_a=(2,\,0,\,1)^{\top}$, $\mathbf{x}_b=(0,\,3,\,0)^{\top}$, $\mathbf{x}_c=(4,\,0,\,2)^{\top}$ and $\mathbf{x}_d=(1,\,1,\,1)^{\top}$.

<ol class="al">

<li>

Compute the cosine similarity and the Euclidean distance from text $a$ to each of the three other texts.

</li>

<li>

Which text is most similar to text $a$, by distance and by cosine similarity? Explain the difference.

</li>

</ol>

:::loesung
(a) With $\lVert\mathbf{x}_a\rVert=\sqrt5$, $\lVert\mathbf{x}_b\rVert=3$, $\lVert\mathbf{x}_c\rVert=\sqrt{20}$ and $\lVert\mathbf{x}_d\rVert=\sqrt3$:

<ul>

<li>

to text $b$: $\mathbf{x}_a^{\top}\mathbf{x}_b=0$, cosine similarity $0$; distance $\sqrt{4+9+1}=\sqrt{14}\approx3.74$;

</li>

<li>

to text $c$: $\mathbf{x}_a^{\top}\mathbf{x}_c=8+0+2=10$, cosine similarity $10/(\sqrt5\sqrt{20})=1$; distance $\sqrt{4+0+1}=\sqrt5\approx2.24$;

</li>

<li>

to text $d$: $\mathbf{x}_a^{\top}\mathbf{x}_d=3$, cosine similarity $3/(\sqrt5\sqrt3)\approx0.775$; distance $\sqrt{1+1+0}=\sqrt2\approx1.41$.

</li>

</ul>

(b) By distance, text $d$ is the closest; by cosine similarity, text $c$. Text $c$ is $\mathbf{x}_c=2\mathbf{x}_a$: the same distribution of words, only twice as long, so the same topic in terms of content. The distance penalizes the greater length; the cosine similarity sees only the direction. Text $d$ is short and therefore lies close to every short text, even without a common topic. For comparing content, the cosine similarity is the appropriate measure here, and text $b$ has nothing at all in common with text $a$.
:::
:::

:::aufgabe Exercise 14 ★★★ Distance and angle of normalized vectors
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Show that for normalized vectors $\mathbf{u},\mathbf{v}$ with angle $\varphi$, $\lVert\mathbf{u}-\mathbf{v}\rVert^2=2-2\cos\varphi$. What does this imply for the rankings “similar by distance” and “similar by cosine similarity” if all examples are normalized beforehand?

</li>

<li>

Check the formula on the normalized texts $\mathbf{x}_1$ and $\mathbf{x}_3$ from Subsection [5.4](#stufe-5-4).

</li>

<li>

Show that $\lVert\mathbf{u}+\mathbf{v}\rVert=\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ holds if and only if $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$. When is this the case?

</li>

</ol>

:::loesung
(a) By [(4.1)](abstande-und-einheiten.html#gl-4-1), $\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}=1+1-2\cos\varphi$, because $\mathbf{u}^{\top}\mathbf{v}=\cos\varphi$ for normalized vectors. So the distance is a decreasing function of the cosine similarity: the larger the cosine, the smaller the distance. If you normalize all examples beforehand, distance and cosine similarity therefore rank the examples in exactly the same order.

(b) The normalized texts are $\mathbf{x}_1/\sqrt{13}$ and $\mathbf{x}_3/\sqrt{10}$, with the cosine $0.1754$. The formula gives $2-2\cdot0.1754\approx1.649$. Directly: $\mathbf{x}_1/\sqrt{13}-\mathbf{x}_3/\sqrt{10}\approx(0.832,\ 0.238,\ -0.949)^{\top}$ with the squared length $0.692+0.057+0.900\approx1.649$.

(c) Both sides are nonnegative, so you may compare the squares. We have $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$ and $(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert)^2=\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2$. The two are equal if and only if $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$. By the Cauchy–Schwarz inequality and its case of equality, this holds if and only if one of the vectors is a multiple of the other, and with a factor $\ge0$, because otherwise the dot product would be negative. Intuitively: the triangle inequality becomes an equality only if the triangle is flat and both arrows point in the same direction.
:::
:::
