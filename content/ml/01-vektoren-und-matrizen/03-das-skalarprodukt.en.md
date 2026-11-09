---
title: The dot product
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15210300
summary: Two vectors with the same number of components give a single number if you multiply their components pairwise and add the products.
tags: dot product, weight, weighted sum, model, prediction, all-ones vector, mean
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
Two vectors with the same number of components give a single number if you multiply their components pairwise and add the products. This calculation is the most common one in all of machine learning: it turns measured values into an estimate and compares data with a pattern.
:::

### The dot product of two vectors

<span class="anker" id="stufe-2-1"></span>

A shopping bill works like this: quantity times price for each item, then add everything up. The same calculation with any two vectors is called the dot product.

You can picture it as a row meeting a column. The first vector is written as a row, the second as a column next to it. Then you multiply the first element of the row by the first element of the column, the second by the second, and so on, and add:

$$\begin{pmatrix}1&2&3\end{pmatrix}\begin{pmatrix}4\\-1\\2\end{pmatrix}=1\cdot4+2\cdot(-1)+3\cdot2=8 .$$

:::definition Definition 2.1 (Dot product)
<span class="anker" id="satz-2-1"></span>

The __dot product__ of two vectors $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ is the number

<span class="anker" id="gl-2-1"></span>
$$\mathbf{u}^{\top}\mathbf{v}=\sum_{j=1}^{d}u_j\,v_j=u_1v_1+u_2v_2+\dots+u_dv_d . \tag{2.1}$$
:::

The notation $\mathbf{u}^{\top}\mathbf{v}$ says exactly what happens: $\mathbf{u}^{\top}$ is $\mathbf{u}$ as a row, and the row meets the column $\mathbf{v}$. The result is a scalar, which is why the dot product is also called the scalar product.

:::satz Theorem 2.2 (Rules for the dot product)
<span class="anker" id="satz-2-2"></span>

For all $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ and every scalar $c$:

<ol class="rm">

<li>

$\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$ (symmetric);

</li>

<li>

$(c\,\mathbf{u})^{\top}\mathbf{v}=c\,(\mathbf{u}^{\top}\mathbf{v})$ and $(\mathbf{u}+\mathbf{q})^{\top}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}+\mathbf{q}^{\top}\mathbf{v}$ (linear, and likewise in the second vector);

</li>

<li>

$\mathbf{u}^{\top}\mathbf{u}=\sum_ju_j^2\ge0$, and $\mathbf{u}^{\top}\mathbf{u}=0$ only for $\mathbf{u}=\mathbf{0}$.

</li>

</ol>
:::

:::beweis Rules for the dot product
(i) follows from $u_jv_j=v_ju_j$ for each component. (ii) is the sum rule [(1.2)](vektoren-daten-als-zahlenlisten.html#gl-1-2): $\sum_j(c\,u_j)v_j=c\sum_ju_jv_j$ and $\sum_j(u_j+q_j)v_j=\sum_ju_jv_j+\sum_jq_jv_j$. (iii) Each term $u_j^2$ is nonnegative. The sum is zero only if every term is zero, that is, if every $u_j=0$.
:::

::::beispiel [Worked example]
For $\mathbf{u}=(1,\,2,\,3)^{\top}$ and $\mathbf{v}=(4,\,-1,\,2)^{\top}$, we get $\mathbf{u}^{\top}\mathbf{v}=8$ and $\mathbf{u}^{\top}\mathbf{u}=14$ (Fig. [6](#abb-6)). In the reverse order the result is the same number, $\mathbf{v}^{\top}\mathbf{u}=4\cdot1+(-1)\cdot2+2\cdot3=8$, as symmetry requires.

:::abbildung ml/k1rskp 6
Two dot products step by step: component times component, then the sum of the products. The dot product of a vector with itself is the sum of the squares of its components.
:::
::::

⁠**In short:** The dot product multiplies two vectors component by component and adds the products; it is a number.

:::hintergrund Other notations for the same thing
Many books write $\mathbf{u}\cdot\mathbf{v}$ or $\langle\mathbf{u},\mathbf{v}\rangle$ instead of $\mathbf{u}^{\top}\mathbf{v}$, and the same number is also called the *inner product* or the *scalar product*. The meaning is always the same. This series writes $\mathbf{u}^{\top}\mathbf{v}$ because the notation shows that a row meets a column. This pays off as soon as tables of numbers come into play.
:::

### Weights and weighted sums

<span class="anker" id="stufe-2-2"></span>

A real estate agent estimates the price of an apartment in her head roughly like this: each square meter is worth about $3$ thousand euros, each room adds another $10$ thousand euros, and each kilometer of distance from the center takes off $4$ thousand euros. So she takes each feature with its own factor and adds everything up.

The number with which a feature enters such a calculation is called its __weight__. A large positive weight means that each unit of this feature raises the result strongly. A negative weight means that the feature lowers the result.

:::definition Definition 2.3 (Weighted sum)
<span class="anker" id="satz-2-3"></span>

For a vector of weights $\mathbf{w}=(w_1,\dots,w_d)^{\top}$ and an example $\mathbf{x}\in\mathbb{R}^d$, the __weighted sum__ is

<span class="anker" id="gl-2-2"></span>
$$\hat y=\mathbf{w}^{\top}\mathbf{x}=\sum_{j=1}^{d}w_j\,x_j . \tag{2.2}$$
:::

A fixed rule that computes a number from the features of an example is called a __model__. The number that the model returns for an example is called its __prediction__. The hat over the $y$ in $\hat y$ indicates that this is a computed estimate and not a measured value. In this chapter the weights are always given; where good weights come from is a question of its own.

::::beispiel [Worked example]
The real estate agent uses the weights $\mathbf{w}=(3,\,10,\,-4)^{\top}$ in thousand euros per square meter, per room and per kilometer. For apartment 1, $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$ (Fig. [7](#abb-7)), that is, $188$ thousand euros.

:::abbildung ml/k1rgewicht 7
The real estate agent's estimate for apartment 1: each feature times its weight, then the sum. The contributions of the three features are $180$, $20$ and $-12$ thousand euros.
:::

In the same way, the other apartments give $\hat y_2=126$, $\hat y_3=286$ and $\hat y_4=232$. Each product $w_jx_j$ has the unit thousand euros, because the unit of the feature cancels against the unit in the denominator of the weight. Only for this reason may you add the three products.
::::

⁠**In short:** A weighted sum is the dot product $\mathbf{w}^{\top}\mathbf{x}$ of weights and features; it is the simplest model that makes a prediction from features.

:::hintergrund A large weight does not mean that the feature is important
For the real estate agent, the weight of the rooms, $10$, is more than three times as large as that of the floor area, $3$. Nevertheless, for apartment 1 the floor area contributes $180$ thousand euros and the number of rooms only $20$. The reason: a weight applies per unit of the feature, and the floor area has many units. If you measure the floor area in units of $10\,\mathrm m^2$, apartment 1 is only $6$ units large, and the same model needs the weight $30$ thousand euros per $10\,\mathrm m^2$. The prediction stays the same; only the weight has become ten times as large. So how large a weight is depends on the chosen unit. If you want to know how much a feature contributes to the prediction, you have to look at the product $w_jx_j$, not at the weight alone.
:::

### Sum and mean as a dot product

<span class="anker" id="stufe-2-3"></span>

Many everyday calculations are dot products with a particularly simple second vector. The ones you need most often are the sum and the average of all components.

The __all-ones vector__ $\mathbf 1\in\mathbb{R}^n$ has only ones as components. The dot product with it simply adds up all components: $\mathbf 1^{\top}\mathbf{v}=v_1+\dots+v_n$.

:::definition Definition 2.4 (Mean)
<span class="anker" id="satz-2-4"></span>

The __mean__ of the components of a vector $\mathbf{v}\in\mathbb{R}^n$ is

<span class="anker" id="gl-2-3"></span>
$$\bar v=\frac1n\sum_{i=1}^nv_i=\frac1n\,\mathbf 1^{\top}\mathbf{v} . \tag{2.3}$$
:::

More calculations of this kind: the dot product with a unit vector picks out one component, $\mathbf{e}_j^{\top}\mathbf{v}=v_j$, because all other products contain a zero. The dot product of a vector with itself is the sum of squares, $\mathbf{v}^{\top}\mathbf{v}=\sum_iv_i^2$. Quantities times prices, summed up, give the amount of an invoice. And evaluating a polynomial $p(t)=c_1+c_2t+\dots+c_nt^{n-1}$ at a point $t$ means forming the dot product $\mathbf{c}^{\top}\mathbf{z}$ of its coefficients $\mathbf{c}=(c_1,\dots,c_n)^{\top}$ with the powers $\mathbf{z}=(1,\,t,\,t^2,\dots,t^{n-1})^{\top}$. For $p(t)=1+2t+3t^2$ at $t=2$, this is $(1,\,2,\,3)\,(1,\,2,\,4)^{\top}=1+4+12=17$.

::::beispiel [Worked example]
From January to March, apartment 1 consumed $\mathbf{u}=(200,\,250,\,300)^{\top}$ kWh of electricity (Subsection [1.4](vektoren-daten-als-zahlenlisten.html#stufe-1-4)). In total this is $\mathbf 1^{\top}\mathbf{u}=750$ kWh, on average $\bar u=250$ kWh per month (Fig. [8](#abb-8)). The consumption in February is $\mathbf{e}_2^{\top}\mathbf{u}=250$ kWh.

:::abbildung ml/k1rmittel 8
Sum and mean of the electricity consumption as a dot product with the all-ones vector, in kWh.
:::

If a kilowatt-hour costs $\mathbf{p}=(0.32,\ 0.34,\ 0.28)^{\top}$ euros in the three months, the electricity bill is the dot product of prices and quantities: $\mathbf{p}^{\top}\mathbf{u}=233$ euros (Fig. [9](#abb-9)). Each product $p_ju_j$ is the amount for one month, in euros per kWh times kWh, that is, in euros.

:::abbildung ml/k1rstrom 9
The electricity bill as a dot product: price times quantity for each month, then the sum, in euros.
:::
::::

⁠**In short:** The sum, the mean, picking out a component and the sum of squares are dot products with $\mathbf 1$, $\tfrac1n\mathbf 1$, $\mathbf{e}_j$ and the vector itself.

### The dot product as a comparison with a pattern

<span class="anker" id="stufe-2-4"></span>

Suppose a measured signal is to be checked for whether it jumps back and forth from sample to sample. To do this, you write the pattern you are looking for as a vector, here $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$, and form the dot product with the signal.

Fig. [10](#abb-10) shows what happens. Each sample is multiplied by the pattern value at the same position. If the signal has the same sign as the pattern at a position, the product is positive; if it has the opposite sign, the product is negative. If the signal follows the pattern everywhere, only positive contributions add up to a large sum. If the signal has nothing to do with the pattern, positive and negative contributions cancel each other out.

:::abbildung ml/k1muster 10
Comparison with a pattern using the dot product. At the top the pattern $\mathbf{w}=(1,-1,1,-1)^{\top}$, in the middle two signals, at the bottom the products $w_j\,x_j$ at each position $j$. On the left, the signal $\mathbf{x}=(2,-1,3,-2)^{\top}$ jumps in step with the pattern: all products are positive, and the sum is $8$. On the right, $\mathbf{x}'=(2,2,3,3)^{\top}$ rises steadily: the products cancel, and the sum is $0$.
:::

More precisely: the contribution of position $j$ to the dot product $\mathbf{w}^{\top}\mathbf{x}$ is $w_jx_j$. It is positive if $w_j$ and $x_j$ have the same sign, and negative if they have opposite signs. The larger the magnitudes at positions with matching signs, the larger the dot product.

In signal processing, this calculation is known as correlation. The cross-correlation of two real sequences $x[n]$ and $y[n]$ at shift zero is $\sum_nx[n]\,y[n]$. If you write the samples of two signals of finite length as vectors $\mathbf{x}$ and $\mathbf{y}$, this is exactly the dot product $\mathbf{x}^{\top}\mathbf{y}$. The energy of a signal, $\sum_nx[n]^2$, is likewise $\mathbf{x}^{\top}\mathbf{x}$. So comparing with a pattern is not a new tool; it is the same one a correlator uses to search for a known pattern in a signal.

::::beispiel [Worked example]
With the alternating pattern $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$, we get $\mathbf{w}^{\top}\mathbf{x}=8$ for $\mathbf{x}=(2,\,-1,\,3,\,-2)^{\top}$ and $\mathbf{w}^{\top}\mathbf{x}'=0$ for $\mathbf{x}'=(2,\,2,\,3,\,3)^{\top}$ (Fig. [11](#abb-11)). With the constant pattern $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ it is the other way around: $\mathbf 1^{\top}\mathbf{x}=2$, but $\mathbf 1^{\top}\mathbf{x}'=10$. So the signal $\mathbf{x}$ mainly alternates, while $\mathbf{x}'$ mainly stays constant.

:::abbildung ml/k1rmuster 11
The alternating pattern $\mathbf{w}$ with two signals. At the top, $\mathbf{x}$ follows the pattern: all four products are positive. At the bottom, $\mathbf{x}'$ rises steadily: the products cancel in pairs.
:::
::::

The real estate agent's weighted sum is also a comparison with a pattern. Her pattern $\mathbf{w}=(3,\,10,\,-4)^{\top}$ describes what makes an apartment valuable: a lot of floor area, many rooms, little distance. The better an apartment fits this pattern, the higher its prediction.

⁠**In short:** The dot product $\mathbf{w}^{\top}\mathbf{x}$ is large if $\mathbf{x}$ has large values where the pattern $\mathbf{w}$ has large values with the same sign; it is the correlation at shift zero.

:::hintergrund The correlation function consists entirely of dot products
Cross-correlation compares a signal with a pattern not just at one position but for every possible shift. For each shift $k$, its value is a dot product: the signal with the pattern shifted by $k$ steps. So the whole correlation function is a sequence of dot products, one per shift. Where the pattern is hidden in the signal, the positive contributions accumulate, and the correlation function has its largest value there. This is how a radar receiver finds the echo of its own pulse and a radio receiver finds the start of a known data frame. In machine learning the shift usually stays fixed at zero: you compare an example as a whole with a pattern.
:::

:::aufgabe Exercise 4 ★ Checking the rules
<span class="anker" id="aufg-4"></span>

Let $\mathbf{u}=(1,\,0,\,2)^{\top}$, $\mathbf{v}=(3,\,-1,\,1)^{\top}$ and $\mathbf{q}=(0,\,2,\,1)^{\top}$. Compute $\mathbf{u}^{\top}\mathbf{v}$, $\mathbf{v}^{\top}\mathbf{u}$, $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})$, $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}$, $(3\mathbf{u})^{\top}\mathbf{v}$ and $\mathbf{u}^{\top}\mathbf{u}$. Which rule does each comparison show?

:::loesung
We have $\mathbf{u}^{\top}\mathbf{v}=3+0+2=5$ and $\mathbf{v}^{\top}\mathbf{u}=3+0+2=5$: the dot product is symmetric, rule (i). With $\mathbf{v}+\mathbf{q}=(3,\,1,\,2)^{\top}$, we get $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})=3+0+4=7$, and $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}=5+(0+0+2)=7$: linearity in the second vector, rule (ii). Furthermore, $(3\mathbf{u})^{\top}\mathbf{v}=(3,0,6)\,(3,-1,1)^{\top}=9+0+6=15=3\cdot5$, again rule (ii). Finally, $\mathbf{u}^{\top}\mathbf{u}=1+0+4=5>0$, as rule (iii) requires for $\mathbf{u}\ne\mathbf{0}$.
:::
:::

:::aufgabe Exercise 5 ★★ The real estate agent's estimate
<span class="anker" id="aufg-5"></span>

Use the weights $\mathbf{w}=(3,\,10,\,-4)^{\top}$ from Subsection [2.2](#stufe-2-2).

<ol class="al">

<li>

Compute the predictions for all four apartments. What unit do they have?

</li>

<li>

A wall is put up in apartment 2, so that it has two rooms with the same floor area. How does the prediction change, and why does the change not depend on the floor area?

</li>

<li>

A colleague says: “For the real estate agent, the rooms count the most; they have the largest weight.” Check this statement for apartment 1 by comparing the three contributions $w_jx_{1j}$.

</li>

</ol>

:::loesung
(a) As in Subsection [2.2](#stufe-2-2): $188$, $126$, $286$ and $232$, each in thousand euros. The unit is thousand euros because every weight has the unit “thousand euros per unit of the feature” and the unit of the feature cancels in the product.

(b) Apartment 2 becomes $(40,\,2,\,1)^{\top}$. The prediction rises from $126$ to $120+20-4=136$, that is, by $10$. In general, a change $\Delta x_2$ in the second feature changes the weighted sum by $w_2\,\Delta x_2$, because $\mathbf{w}^{\top}(\mathbf{x}+\Delta x_2\,\mathbf{e}_2)=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,\mathbf{w}^{\top}\mathbf{e}_2=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,w_2$. The other features play no role in this. This is the linearity of the dot product: each feature contributes on its own, without interacting with the others.

(c) The contributions for apartment 1 are $w_1x_{11}=180$, $w_2x_{12}=20$ and $w_3x_{13}=-12$. By far the largest contribution comes from the floor area, even though its weight is the smallest in absolute value. The colleague's statement confuses the weight per unit with the contribution to the prediction; the floor area has very many units.
:::
:::

:::aufgabe Exercise 6 ★★ A pattern for rising signals
<span class="anker" id="aufg-6"></span>

A signal with four samples is to be checked for whether it rises. The proposed pattern is $\mathbf{w}=(-3,\,-1,\,1,\,3)^{\top}$.

<ol class="al">

<li>

Compute $\mathbf{w}^{\top}\mathbf{x}$ for $\mathbf{x}=(1,2,3,4)^{\top}$, $(4,3,2,1)^{\top}$, $(5,5,5,5)^{\top}$ and $(1,3,2,4)^{\top}$ and interpret the results.

</li>

<li>

Why does every constant signal $c\,\mathbf1$ give exactly zero? Use $\mathbf 1^{\top}\mathbf{w}$.

</li>

</ol>

:::loesung
(a) $\mathbf{w}^{\top}(1,2,3,4)^{\top}=-3-2+3+12=10$: the signal rises, and the result is clearly positive. $\mathbf{w}^{\top}(4,3,2,1)^{\top}=-12-3+2+3=-10$: the signal falls, and the result is just as clearly negative. $\mathbf{w}^{\top}(5,5,5,5)^{\top}=-15-5+5+15=0$: constant, no rise. $\mathbf{w}^{\top}(1,3,2,4)^{\top}=-3-3+2+12=8$: the signal rises overall, with a step back in the middle, and the result is somewhat smaller than for the steady rise. The pattern weights the early values negatively and the late ones positively; so it responds to whether the late values are larger than the early ones.

(b) $\mathbf 1^{\top}\mathbf{w}=-3-1+1+3=0$. For a constant signal, therefore, $\mathbf{w}^{\top}(c\,\mathbf 1)=c\,\mathbf{w}^{\top}\mathbf 1=c\cdot0=0$. Because the weights add up to zero, the pattern ignores a common DC component completely: it measures only differences between the samples.
:::
:::
