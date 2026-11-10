---
title: Distances and units
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Chapter 1: Vectors and Matrices
nachschlagen: ja
order: 15210500
summary: Two examples are similar if their vectors lie close together.
tags: distance, feature column, centered, standard deviation, standardized
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Two examples are similar if their vectors lie close together. This section measures distances, shows that the result depends on the chosen units and presents a method that makes the features comparable.
:::

### The distance between two data points

<span class="anker" id="stufe-4-1"></span>

Two apartments are similar if they differ only slightly in all features. The differences are contained in the difference vector $\mathbf{u}-\mathbf{v}$, the arrow from one point to the other. A norm tells you how large this arrow is.

:::definition Definition 4.1 (Distance)
<span class="anker" id="satz-4-1"></span>

The __distance__ between two vectors $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ with respect to a norm is the norm of their difference, $\lVert\mathbf{u}-\mathbf{v}\rVert$. If nothing else is specified, the Euclidean distance is meant.
:::

The properties you expect from a distance follow from the properties of a norm: it is never negative and is zero only for identical points; it is as large from $\mathbf{u}$ to $\mathbf{v}$ as from $\mathbf{v}$ to $\mathbf{u}$, because $\mathbf{v}-\mathbf{u}=-(\mathbf{u}-\mathbf{v})$; and the route via a third point $\mathbf{q}$ is never shorter, $\lVert\mathbf{u}-\mathbf{v}\rVert\le\lVert\mathbf{u}-\mathbf{q}\rVert+\lVert\mathbf{q}-\mathbf{v}\rVert$. This is the triangle inequality (N3), applied to $\mathbf{u}-\mathbf{v}=(\mathbf{u}-\mathbf{q})+(\mathbf{q}-\mathbf{v})$.

**Distance and dot product.** If you expand the square of the Euclidean distance with the rules for the dot product, you get

<span class="anker" id="gl-4-1"></span>
$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=(\mathbf{u}-\mathbf{v})^{\top}(\mathbf{u}-\mathbf{v})=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v} . \tag{4.1}$$

So for fixed lengths, the larger the dot product, the smaller the distance. Both measure similarity, just in opposite directions.

::::beispiel [Worked example]
Apartments 1 and 2 differ by $\mathbf{x}_1-\mathbf{x}_2=(20,\,1,\,2)^{\top}$. Their Euclidean distance is $\sqrt{405}\approx20.12$ (Fig. [18](#abb-18)); in the 1-norm it is $20+1+2=23$, and in the maximum norm $20$.

:::abbildung ml/k1rabstand 18
The Euclidean distance between apartments 1 and 2: first the difference, then its length.
:::

To check [(4.1)](#gl-4-1) with $\mathbf{u}=(1,\,2,\,2)^{\top}$ and $\mathbf{v}=(2,\,0,\,1)^{\top}$: the left side is $\lVert(-1,\,2,\,1)^{\top}\rVert^2=6$, the right side $9+5-2\cdot4=6$.
::::

⁠**In short:** The distance between two data points is the norm of their difference; close together means similar.

### Distances depend on the units

<span class="anker" id="stufe-4-2"></span>

In the worked example just now, the distance $20.12$ is almost exactly the difference in floor area of $20\,\mathrm m^2$. Of the $405$ in the squared distance, $400$ come from the floor area. The difference of one room and two kilometers plays practically no role, and this is only because floor areas in square meters are large numbers.

Three other apartments show what follows from this. The question is which of the apartments B and C is more similar to apartment A:

$$\text{A}=(60,\,2)^{\top},\qquad \text{B}=(63,\,4)^{\top},\qquad \text{C}=(54,\,2)^{\top}\qquad(\text{floor area in m}^2,\ \text{rooms}).$$

In square meters, $\lVert\text{A}-\text{B}\rVert=\sqrt{9+4}\approx3.61$ and $\lVert\text{A}-\text{C}\rVert=\sqrt{36+0}=6$: B is closer. If you measure the floor area in units of $10\,\mathrm m^2$, then $\text{A}=(6,\,2)^{\top}$, $\text{B}=(6.3,\ 4)^{\top}$, $\text{C}=(5.4,\ 2)^{\top}$, and $\lVert\text{A}-\text{B}\rVert=\sqrt{0.09+4}\approx2.02$, $\lVert\text{A}-\text{C}\rVert=0.6$: now C is closer. Figure [19](#abb-19) shows both pictures.

:::abbildung ml/k1einheiten 19
The same three apartments, on the left with the floor area in $\mathrm m^2$, on the right in units of $10\,\mathrm m^2$. Both axes of each picture have the same scale, so the length of a segment is the Euclidean distance. On the left, B is closer to A (dashed: the circle around A through B); on the right, C is closer.
:::

The mechanism is simple. The squared distance contains the squared difference for each feature. If you measure a feature in a different unit, its numbers change by a factor $c$, and its contribution to the squared distance changes by $c^2$. The contributions of the other features stay the same. A feature with large numbers determines the distance almost on its own; a feature with small numbers is almost lost.

⁠**In short:** Distances between examples depend on the units of the features; which example is most similar to another can change when the units change.

:::hintergrund Every choice of units is a weighting
The Euclidean distance adds squares of square meters, rooms and kilometers. Computationally this works, because the computer sees only numbers. Physically it is a sum of quantities of different kinds, and the units decide how much each one counts. Whoever states the floor area in $\mathrm m^2$ has thereby decided, without intending to, that a difference of $1\,\mathrm m^2$ counts just as much as a difference of one room. There is no correct choice given by nature. You have to make it deliberately, and the next method is such a deliberate choice.
:::

### Deviations from the mean

<span class="anker" id="stufe-4-3"></span>

To make features comparable, you look at each feature on its own across all examples. In Table [1](vektoren-daten-als-zahlenlisten.html#tab-1) these are the columns: the floor areas of all apartments form the vector $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}\in\mathbb{R}^4$. Such a vector belongs to one feature and has as many components as there are examples. Here it is called the __feature column__.

For the comparison, what matters is not how large the floor areas are but how much they differ. You therefore measure each floor area as a deviation from the average. This is also how you describe the heights of children in a school class: “$5$ cm taller than the average” says more about a child than “$1.45$ m”.

:::definition Definition 4.2 (Centered vector)
<span class="anker" id="satz-4-2"></span>

For $\mathbf{v}\in\mathbb{R}^N$ with mean $\bar v$,

<span class="anker" id="gl-4-2"></span>
$$\tilde{\mathbf{v}}=\mathbf{v}-\bar v\,\mathbf 1=(v_1-\bar v,\,\dots,\,v_N-\bar v)^{\top} \tag{4.2}$$

is called the __centered__ vector. Its components are the deviations from the mean.
:::

The deviations always cancel each other out: $\mathbf 1^{\top}\tilde{\mathbf{v}}=\mathbf 1^{\top}\mathbf{v}-\bar v\,\mathbf 1^{\top}\mathbf 1=N\bar v-\bar v\,N=0$. So the centered vector has mean zero.

::::beispiel [Worked example]
The floor areas $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}$ have the mean $\bar v=65$. Centered, they are $\tilde{\mathbf{v}}=(-5,\,-25,\,25,\,5)^{\top}$, and the deviations do indeed add up to zero (Fig. [20](#abb-20)). The numbers of rooms $(2,\,1,\,4,\,3)^{\top}$ have the mean $2.5$ and, centered, are $(-0.5,\ -1.5,\ 1.5,\ 0.5)^{\top}$; the distances $(3,\,1,\,6,\,2)^{\top}$ have the mean $3$ and, centered, are $(0,\,-2,\,3,\,-1)^{\top}$.

:::abbildung ml/k1rzentriert 20
The mean of the floor areas and the sum of the deviations from the mean, in $\mathrm m^2$.
:::
::::

⁠**In short:** Centering subtracts the mean from each component; what remains are the deviations, which add up to zero.

### The standard deviation

<span class="anker" id="stufe-4-4"></span>

How much a feature fluctuates can be seen from the size of its deviations. A typical magnitude of a component is the RMS value from Subsection [3.6](normen-die-groe-eines-vektors.html#stufe-3-6). Applied to the centered vector, it is the typical deviation from the mean.

:::definition Definition 4.3 (Standard deviation)
<span class="anker" id="satz-4-3"></span>

The __standard deviation__ of a vector $\mathbf{v}\in\mathbb{R}^N$ is the RMS value of its centered vector:

<span class="anker" id="gl-4-3"></span>
$$\operatorname{std}(\mathbf{v})=\operatorname{rms}(\tilde{\mathbf{v}})=\frac{\lVert\mathbf{v}-\bar v\,\mathbf 1\rVert}{\sqrt N}=\sqrt{\frac1N\sum_{i=1}^N(v_i-\bar v)^2} . \tag{4.3}$$
:::

The standard deviation has the same unit as the feature. It is zero exactly when all components are equal. Many texts divide by $N-1$ instead of $N$ in [(4.3)](#gl-4-3). With many examples the difference is small. This series divides by $N$ and says so whenever it is meant to be different.

::::beispiel [Worked example]
The centered floor areas $(-5,\,-25,\,25,\,5)^{\top}$ have the sum of squares $1\,300$, so $\operatorname{std}(\mathbf{v})=\sqrt{325}\approx18.03\,\mathrm m^2$ (Fig. [21](#abb-21)). In the same way you get $\sqrt{5/4}\approx1.118$ for the rooms and $\sqrt{14/4}\approx1.871$ km for the distances.

:::abbildung ml/k1rstd 21
The standard deviation of the floor areas: square the deviations, average them, take the square root. The result $\sqrt{325}\approx18.03$ has the unit $\mathrm m^2$.
:::
::::

⁠**In short:** The standard deviation is the RMS value of the deviations from the mean, the typical fluctuation of a feature.

:::hintergrund The mean and the deviations share the mean square
A vector is the sum of the constant vector $\bar v\,\mathbf 1$ and its deviations $\tilde{\mathbf{v}}$. For the squared length, the rules for the dot product give

$$\lVert\bar v\,\mathbf 1+\tilde{\mathbf{v}}\rVert^2=\bar v^2\,\mathbf 1^{\top}\mathbf 1+2\,\bar v\,\mathbf 1^{\top}\tilde{\mathbf{v}}+\lVert\tilde{\mathbf{v}}\rVert^2=N\bar v^2+0+\lVert\tilde{\mathbf{v}}\rVert^2 ,$$

because the deviations add up to zero. Dividing by $N$ turns this into $\operatorname{rms}(\mathbf{v})^2=\bar v^2+\operatorname{std}(\mathbf{v})^2$. In words: the mean square of the values is the square of their mean plus the mean square of their deviations. So a large mean square can come from large values or from strong fluctuations, and the formula separates the two. For the floor areas: $\operatorname{rms}^2=(3600+1600+8100+4900)/4=4550=65^2+325$.
:::

### Standardizing

<span class="anker" id="stufe-4-5"></span>

Now each feature can be measured in terms of its own typical fluctuation. Instead of “$25\,\mathrm m^2$ above average” you say “$1.39$ standard deviations above average”. In this language every feature has the same order of magnitude, no matter in which unit it was originally measured.

:::definition Definition 4.4 (Standardizing)
<span class="anker" id="satz-4-4"></span>

A feature $j$ whose feature column has the mean $\bar x_j$ and the standard deviation $s_j>0$ is __standardized__ by computing

<span class="anker" id="gl-4-4"></span>
$$z_{ij}=\frac{x_{ij}-\bar x_j}{s_j},\qquad i=1,\dots,N, \tag{4.4}$$

and using these numbers in place of the original values. The numbers $z_{ij}$ are called the standardized values.
:::

The standardized feature column has mean $0$ and standard deviation $1$, because centering makes the mean zero and dividing by $s_j$ makes the typical deviation one. The values no longer have a unit.

::::beispiel [Worked example 1] the apartment dataset
With the means $65$, $2.5$, $3$ and the standard deviations $18.03$, $1.118$, $1.871$, the four apartments become

$$\begin{aligned} \mathbf{z}_1&\approx(-0.28,\ -0.45,\ 0)^{\top}, & \mathbf{z}_2&\approx(-1.39,\ -1.34,\ -1.07)^{\top},\\ \mathbf{z}_3&\approx(1.39,\ 1.34,\ 1.60)^{\top}, & \mathbf{z}_4&\approx(0.28,\ 0.45,\ -0.53)^{\top}. \end{aligned}$$

All three features now lie in the same range of numbers.
::::

::::beispiel [Worked example 2] A, B and C
The three apartments from Subsection [4.2](#stufe-4-2) have a mean floor area of $59\,\mathrm m^2$ with standard deviation $\sqrt{14}\approx3.74\,\mathrm m^2$ and on average $8/3$ rooms with standard deviation $\sqrt{8/9}\approx0.943$. After standardizing, $\lVert\text A-\text B\rVert\approx2.27$ and $\lVert\text A-\text C\rVert\approx1.60$. So C is the one most similar to A, and this judgment no longer depends on the unit of the floor area.
::::

That the unit drops out holds in general:

:::satz Theorem 4.5 (Standardized values do not depend on the unit)
<span class="anker" id="satz-4-5"></span>

If you convert a feature to a different unit, $v_i'=\alpha\,v_i+\beta$ for all $i$ with numbers $\alpha>0$ and $\beta$, its standardized values stay the same.
:::

:::beweis Independence of the unit
The mean becomes $\bar v'=\frac1N\sum_i(\alpha\,v_i+\beta)=\alpha\,\bar v+\beta$, and the deviations become $v_i'-\bar v'=\alpha\,(v_i-\bar v)$. By [(4.3)](#gl-4-3), we then have $\operatorname{std}(\mathbf{v}')=|\alpha|\operatorname{std}(\mathbf{v})=\alpha\operatorname{std}(\mathbf{v})$. In the quotient [(4.4)](#gl-4-4), $\alpha$ cancels, and $\beta$ already disappeared during centering.
:::

The term $\beta$ also covers conversions with a shifted zero point, such as from degrees Celsius to degrees Fahrenheit.

⁠**In short:** Standardizing measures each feature as a deviation from the mean in multiples of its standard deviation; afterwards, distances no longer depend on the units.

:::hintergrund Why the standard deviation as the scale?
For each feature you need a scale that changes under a change of units by the same factor as the differences between the values. Then it cancels out. Any quantity that is computed from the differences between the values of the feature and has the unit of the feature does this: the standard deviation, but also the range from the smallest to the largest value. The standard deviation is the usual choice because it takes all values into account and not just the two extreme ones.

You can see what standardizing does to a distance by subtracting two standardized examples $\mathbf{z}_a$ and $\mathbf{z}_b$ from each other. The mean drops out, $z_{aj}-z_{bj}=(x_{aj}-x_{bj})/s_j$, and what remains is

$$\lVert\mathbf{z}_a-\mathbf{z}_b\rVert^2=\sum_{j=1}^d\frac{(x_{aj}-x_{bj})^2}{s_j^2} .$$

So the distance between the standardized values is the ordinary distance in which the squared difference in feature $j$ counts with the weight $1/s_j^2$. For apartments A and B this is $3^2/14+2^2/(8/9)=9/14+9/2\approx5.14$, and its square root is $2.27$, as above.

Standardizing, however, is itself a decision. It gives every feature the same weight in the distance, even a feature that plays no role at all for the question at hand. And a feature that has the same value in all examples has standard deviation zero and cannot be standardized; but it also does not distinguish the examples and contributes nothing to any distance.
:::

:::aufgabe Exercise 9 ★ Mean and deviations
<span class="anker" id="aufg-9"></span>

The temperature at seven in the morning on four days is $\mathbf{x}=(1,\,3,\,1,\,-1)^{\top}$ degrees Celsius. Compute the mean, the centered vector, the standard deviation and the RMS value. Check that $\operatorname{rms}(\mathbf{x})^2=\bar x^2+\operatorname{std}(\mathbf{x})^2$.

:::loesung
The mean is $\bar x=(1+3+1-1)/4=1$, and the centered vector is $\tilde{\mathbf{x}}=(0,\,2,\,0,\,-2)^{\top}$. The standard deviation is $\sqrt{(0+4+0+4)/4}=\sqrt2\approx1.414$, and the RMS value is $\sqrt{(1+9+1+1)/4}=\sqrt3\approx1.732$. Check: $\operatorname{rms}^2=3=1^2+(\sqrt2)^2=\bar x^2+\operatorname{std}^2$. The mean and the deviations share the mean square $3$ in the ratio $1:2$.
:::
:::

:::aufgabe Exercise 10 ★★ Which apartment is most similar to apartment 1?
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Compute the Euclidean distances from apartment 1 to apartments 2, 3 and 4 with the values from Table [1](vektoren-daten-als-zahlenlisten.html#tab-1). What fraction of the squared distance to apartment 2 comes from the floor area?

</li>

<li>

Compute the same distances with the standardized values from Subsection [4.5](#stufe-4-5). What fraction of the squared distance to apartment 2 comes from the floor area now?

</li>

<li>

In each case, which apartment is most similar to apartment 1? What has standardizing changed here, if not the answer?

</li>

</ol>

:::loesung
(a) With the values from the table:

$$\begin{aligned} \lVert\mathbf{x}_1-\mathbf{x}_2\rVert&=\sqrt{20^2+1^2+2^2}=\sqrt{405}\approx20.12,\\ \lVert\mathbf{x}_1-\mathbf{x}_3\rVert&=\sqrt{30^2+2^2+3^2}=\sqrt{913}\approx30.22,\\ \lVert\mathbf{x}_1-\mathbf{x}_4\rVert&=\sqrt{10^2+1^2+1^2}=\sqrt{102}\approx10.10 . \end{aligned}$$

Of the $405$ in the squared distance to apartment 2, $400$ come from the floor area, that is, $98.8$ %.

(b) With the standardized vectors from Subsection [4.5](#stufe-4-5), $\mathbf{z}_1-\mathbf{z}_2\approx(1.109,\ 0.894,\ 1.069)^{\top}$, with the squares $1.231$, $0.800$ and $1.143$. The distance is $\sqrt{3.174}\approx1.78$. In the same way you get $\lVert\mathbf{z}_1-\mathbf{z}_3\rVert\approx2.92$ and $\lVert\mathbf{z}_1-\mathbf{z}_4\rVert\approx1.18$. The fraction of the squared distance to apartment 2 that comes from the floor area is now $1.231/3.174\approx38.8$ %.

(c) In both cases apartment 4 is the most similar, followed by apartment 2 and apartment 3. The order does not change here because in this small dataset large apartments also have more rooms and lie farther out; all three features tell roughly the same story. What has changed is *why* apartment 4 is the most similar: with the raw values the floor area decides almost alone, while after standardizing all three features contribute about equally. That the answer nevertheless stays the same is a coincidence of these data; for apartments A, B and C in Subsection [4.2](#stufe-4-2) it did change.
:::
:::

:::aufgabe Exercise 11 ★★ Celsius or Fahrenheit
<span class="anker" id="aufg-11"></span>

On four days, $10$, $20$, $15$ and $25$ $^\circ$C were measured at noon.

<ol class="al">

<li>

Convert to degrees Fahrenheit ($F=1.8\,C+32$). Compute the mean and the standard deviation in both units.

</li>

<li>

Compute the standardized values in both units and compare them.

</li>

<li>

What happens to the standardized values if you convert a feature with a negative factor, for example $v_i'=-v_i$?

</li>

</ol>

:::loesung
(a) In Fahrenheit, the values are $1.8\cdot10+32=50$, $68$, $59$ and $77$. In Celsius, the mean is $17.5$ and the standard deviation is $\sqrt{(56.25+6.25+6.25+56.25)/4}=\sqrt{31.25}\approx5.590$; in Fahrenheit, the mean is $63.5=1.8\cdot17.5+32$ and the standard deviation is $\approx10.062=1.8\cdot5.590$. The term $32$ only shifts the mean; the factor $1.8$ also stretches the standard deviation.

(b) In both units, the standardized values are $\approx(-1.342,\ 0.447,\ -0.447,\ 1.342)$. This is just what the theorem in Subsection [4.5](#stufe-4-5) says: the term drops out during centering, and the factor cancels against the standard deviation.

(c) With $v_i'=-v_i$, all deviations from the mean are multiplied by $-1$, but the standard deviation by $|-1|=1$. So the standardized values change their sign. For distances between examples this makes no difference, because $\lVert-\mathbf{u}\rVert=\lVert\mathbf{u}\rVert$; the dataset is merely reflected.
:::
:::
