---
title: Vectors: data as lists of numbers
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Chapter 1: Vectors and Matrices
nachschlagen: ja
order: 15210200
summary: A computer can only handle numbers.
tags: index, summation sign, summation index, double sum, feature, example, dataset, vector
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
A computer can only handle numbers. This section clarifies how to describe a thing from the real world by a list of numbers and which calculations with such lists are allowed.
:::

### What you need for this: the summation sign and indices

<span class="anker" id="stufe-1-1"></span>

This chapter constantly adds up many numbers. So that you do not have to write out “$a_1+a_2+\dots$” every time, there is a shorthand.

**Indices.** If you have several numbers of the same kind, you number them consecutively: $a_1,a_2,\dots,a_n$. The subscript number is called an __index__. It only says which number in the sequence is meant and has nothing to do with the value of the number.

**The summation sign.** For the sum of $a_1$ through $a_n$ you write

<span class="anker" id="gl-1-1"></span>
$$\sum_{i=1}^{n} a_i = a_1+a_2+\dots+a_n , \tag{1.1}$$

read “sum of $a_i$ for $i$ from $1$ to $n$”. The large Greek sigma is called the __summation sign__. The letter $i$ below it is the __summation index__: it takes the values $1,2,\dots,n$ one after another, and for each value one term is added. The summation index is a placeholder. Whether you call it $i$, $j$ or $k$ does not change the sum: $\sum_{i=1}^n a_i=\sum_{j=1}^n a_j$.

**Two rules of calculation.** A sum with a summation sign is just an abbreviated way of writing an ordinary sum of finitely many numbers. Therefore the familiar rules apply to it: you may factor out a common factor (distributive law) and rearrange and group the terms in any way (commutative and associative laws). Written with the summation sign, this means: a common factor may be moved in front of the sum, and a sum of sums may be split up:

<span class="anker" id="gl-1-2"></span>
$$\sum_{i=1}^n c\,a_i=c\sum_{i=1}^n a_i ,\qquad \sum_{i=1}^n (a_i+b_i)=\sum_{i=1}^n a_i+\sum_{i=1}^n b_i . \tag{1.2}$$

**Double sums.** Numbers arranged in a table get two indices: $a_{ij}$ is the number in row $i$ and column $j$. The sum of all entries of a table with $m$ rows and $n$ columns is written as a __double sum__

$$\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij} .$$

You read it from the inside out: for each row $i$, the inner sum adds the numbers of this row, and the outer sum adds the row sums. Because the order does not matter for finitely many terms, you may swap the two summation signs and add column by column first.

::::beispiel [Worked example 1]
For $a_1=2$, $a_2=5$, $a_3=1$, you first write out each sum, then insert the numbers and add (Fig. [1](#abb-1)). This gives $\sum_{i=1}^3 a_i=8$ and $\sum_{i=1}^3 a_i^2=30$. In the third sum, the summation index itself is the term: $\sum_{j=1}^{3}j=6$.

:::abbildung ml/k1rsumme 1
Three sums step by step: write out the summation sign, insert the numbers, add.
:::
::::

::::beispiel [Worked example 2]
The table with the rows $(1,\,2)$ and $(3,\,4)$ has the entries $a_{11}=1$, $a_{12}=2$, $a_{21}=3$, $a_{22}=4$. Added row by row, the double sum gives $(1+2)+(3+4)=10$; added column by column, $(1+3)+(2+4)=10$ (Fig. [2](#abb-2)).

:::abbildung ml/k1rdoppel 2
The double sum over the table with the rows $(1,\,2)$ and $(3,\,4)$: at the top row by row first, at the bottom column by column first. Both orders give the same sum.
:::
::::

⁠**In short:** $\sum_{i=1}^n a_i$ is the sum of $a_1$ through $a_n$; the summation index $i$ is only a placeholder.

### Examples and features

<span class="anker" id="stufe-1-2"></span>

If you want to learn from data, you first have a collection of things of the same kind in front of you: apartments, patients, letters, measurements on a machine. Each thing is described by the same measured quantities. Apartments, for instance, by their floor area, the number of rooms and the distance to the city center. If you write this down for several apartments, you get a table (Table [1](#tab-1)). It accompanies the entire chapter.

<span class="anker" id="tab-1"></span>

**Table 1:** The apartment dataset of this chapter: four apartments, each described by three features. The numbers are made up.

|  | Floor area in $\mathrm{m}^2$ | Rooms | Distance to the center in km |
|---|---|---|---|
| Apartment 1 | 60 | 2 | 3 |
| Apartment 2 | 40 | 1 | 1 |
| Apartment 3 | 90 | 4 | 6 |
| Apartment 4 | 70 | 3 | 2 |

Each row of the table belongs to one thing, each column to one measured quantity. There are fixed words for both.

:::definition Definition 1.1 (Feature, example, dataset)
<span class="anker" id="satz-1-1"></span>

A __feature__ is a property that can be stated as a real number.

An __example__ is a single thing described by the values of $d$ features.

A __dataset__ is a collection of $N$ examples, all described by the same $d$ features.
:::

Throughout the series, $N$ is the number of examples and $d$ the number of features. The examples are numbered $i=1,\dots,N$, the features $j=1,\dots,d$.

Two notes on the words. In databases, a single row of a table is often called a “record”; here the dataset is the whole collection, not a single row. And in this chapter the word “example” always means a thing from a dataset; calculations carried out in full are therefore called “worked examples”.

::::beispiel [Worked example]
The apartment dataset has $N=4$ examples and $d=3$ features. Feature 2 is the number of rooms. For apartment 3 it has the value $4$.
::::

Not every property is a number by itself. The district of an apartment is a name. Such properties must first be translated into numbers before you can calculate with them. In this chapter all features are already numbers.

⁠**In short:** A dataset consists of $N$ examples, and each example is described by the same $d$ features.

:::hintergrund The same things under other names
Other texts call an example a *sample*, an *instance* or a *data point*, and a feature an *attribute*. In statistics, *observation* is also common for an example. The meaning is always the same: a row of the table.
:::

### Vectors

<span class="anker" id="stufe-1-3"></span>

To the computer, an apartment is nothing but its three numbers. So that you can calculate with these three numbers as with a single object, you combine them into a list. The order is fixed: first the floor area, then the rooms, then the distance.

Such a list can also be drawn if it contains only two numbers. If you take only the number of rooms $3$ and the distance $2$ of apartment 4, this is the point with the coordinates $(3,\,2)$ in a plane whose horizontal axis counts the rooms and whose vertical axis counts the kilometers. You can also picture the same list as an arrow leading from the origin to this point (Fig. [3](#abb-3)). Both pictures describe the same two numbers.

:::abbildung ml/k1punktpfeil 3
The vector $\mathbf{x}=(3,\,2)^{\top}$, on the left as a point, on the right as an arrow from the origin to this point. Here $x_1$ stands for the number of rooms and $x_2$ for the distance to the center in km of apartment 4.
:::

:::definition Definition 1.2 (Vector)
<span class="anker" id="satz-1-2"></span>

A __vector__ $\mathbf{x}$ with $d$ components is an ordered list of $d$ real numbers $x_1,\dots,x_d$, written one below the other:

$$\mathbf{x}=\begin{pmatrix}x_1\\\vdots\\x_d\end{pmatrix}.$$

The number $x_j$ is called the $j$th __component__ of $\mathbf{x}$. The set of all vectors with $d$ components is called $\mathbb{R}^d$. Two vectors are equal if they have the same number of components and all components in the same position agree.
:::

Vectors are written in bold lowercase letters, their components in regular type. A single real number, as opposed to a vector, is called a __scalar__.

**Column and row.** In this series a vector is always a column. In running text, a column takes up a lot of space. So you write the numbers side by side and put a superscript $\top$ after them: $(x_1,\dots,x_d)^{\top}$ means the same numbers as a column. The symbol stands for __transposed__. It turns a row into a column and a column into a row. Conversely, $\mathbf{x}^{\top}=(x_1,\,\dots,\,x_d)$ is the vector $\mathbf{x}$ written as a row. The components are separated by commas; since decimal numbers here are written with a point, there is no risk of confusion: $(0.2,\ 0.25,\ 0.3)^{\top}$ has three components.

**The examples of a dataset.** Example number $i$ is the vector $\mathbf{x}_i\in\mathbb{R}^d$. The vector of an example is also called its __feature vector__. Its components get two indices: $x_{ij}$ is the value of feature $j$ for example $i$. So a bold letter with one index is a whole vector from a list of vectors, and a regular letter with two indices is a single number.

::::beispiel [Worked example]
Apartment 1 is the vector $\mathbf{x}_1=(60,\,2,\,3)^{\top}\in\mathbb{R}^3$. Its second component is $x_{12}=2$. The vector $(2,\,60,\,3)^{\top}$ contains the same numbers but is a different vector: the first position now holds the number $2$, and you would read it as the floor area.
::::

⁠**In short:** A vector is an ordered list of numbers that can be drawn as a point or as an arrow; an example with $d$ features is a vector in $\mathbb{R}^d$.

:::hintergrund What a vector really is
A list of numbers is the vector you calculate with. Mathematically, the concept is broader: a vector is anything that can be added and multiplied by a number without leaving the kind of object. Arrows in the plane are vectors, but so are audio recordings. An audio recording captures, at equal and very short intervals, how far the air pressure currently deviates from its resting value. With $n$ such values $x[0],\dots,x[n-1]$, it is a vector in $\mathbb{R}^n$. Adding two recordings means mixing them, and multiplying a recording by a number means making it louder or quieter; both give a recording of the same length again.

An image is a vector, too. A grayscale image with $28\times28$ pixels consists of $784$ brightness values. If you read them row by row, one after another, the image is a point in $\mathbb{R}^{784}$. This picture can no longer be drawn, but you calculate with it exactly as with two or three components.
:::

### Addition and multiples

<span class="anker" id="stufe-1-4"></span>

You want to calculate with lists of measured values: add up the electricity consumption of two apartments, convert kilowatt-hours to megawatt-hours or see by how much two apartments differ. All of this happens component by component.

In the picture of arrows, adding means attaching the second arrow to the tip of the first. The arrow from the origin to the new tip is the sum (Fig. [4](#abb-4), left). Multiplying by a number means stretching or shrinking the arrow; a negative factor also reverses its direction (Fig. [4](#abb-4), right).

:::abbildung ml/k1addition 4
Left: $\mathbf{u}=(3,\,1)^{\top}$ plus $\mathbf{v}=(1,\,2)^{\top}$. If you attach $\mathbf{v}$ to the tip of $\mathbf{u}$ (or $\mathbf{u}$ to the tip of $\mathbf{v}$, dashed), you end up at $\mathbf{u}+\mathbf{v}=(4,\,3)^{\top}$. Right: $\mathbf{u}=(2,\,1)^{\top}$, its double $2\mathbf{u}=(4,\,2)^{\top}$ (gray) and $-\mathbf{u}=(-2,\,-1)^{\top}$.
:::

:::definition Definition 1.3 (Addition and multiple)
<span class="anker" id="satz-1-3"></span>

For two vectors $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ and a scalar $c$, the __sum__ $\mathbf{u}+\mathbf{v}$ and the __multiple__ $c\,\mathbf{u}$ are the vectors with the components

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{u}+\mathbf{v})_j=u_j+v_j ,\qquad (c\,\mathbf{u})_j=c\,u_j ,\qquad j=1,\dots,d. \tag{1.3}$$

The __zero vector__ $\mathbf{0}$ has only zeros as components. You write $-\mathbf{u}$ for $(-1)\,\mathbf{u}$ and $\mathbf{u}-\mathbf{v}$ for $\mathbf{u}+(-\mathbf{v})$.
:::

You can only add vectors with the same number of components. Moreover, it only makes sense if the same quantity is in the same position: kilowatt-hours to kilowatt-hours, not square meters to rooms.

Because each component on its own is an ordinary calculation with numbers, the familiar rules hold: $\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}$, $(\mathbf{u}+\mathbf{v})+\mathbf{q}=\mathbf{u}+(\mathbf{v}+\mathbf{q})$, $c\,(\mathbf{u}+\mathbf{v})=c\,\mathbf{u}+c\,\mathbf{v}$, $(c+c')\,\mathbf{u}=c\,\mathbf{u}+c'\,\mathbf{u}$ and $\mathbf{u}+\mathbf{0}=\mathbf{u}$ for all vectors $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ and scalars $c,c'$.

The difference $\mathbf{u}-\mathbf{v}$ has a picture of its own. It is the arrow leading from the tip of $\mathbf{v}$ to the tip of $\mathbf{u}$, because $\mathbf{v}+(\mathbf{u}-\mathbf{v})=\mathbf{u}$. For two examples, it states by how much they differ in each feature.

::::beispiel [Worked example]
From January to March, apartment 1 consumed $\mathbf{u}=(200,\,250,\,300)^{\top}$ kilowatt-hours of electricity, and apartment 2 in the same building consumed $\mathbf{v}=(150,\,100,\,120)^{\top}$. Together they consume

$$\mathbf{u}+\mathbf{v}=(350,\,350,\,420)^{\top}\ \text{kWh}.$$

The consumption of apartment 1 in megawatt-hours is given by the multiple $0.001\,\mathbf{u}=(0.2,\ 0.25,\ 0.3)^{\top}$. The difference $\mathbf{u}-\mathbf{v}=(50,\,150,\,180)^{\top}$ tells you how many more kilowatt-hours apartment 1 consumes than apartment 2 in each month. In the apartment dataset, $\mathbf{x}_3-\mathbf{x}_1=(30,\,2,\,3)^{\top}$: apartment 3 is $30\,\mathrm m^2$ larger, has two more rooms and is $3$ km farther out than apartment 1.
::::

⁠**In short:** You add vectors and multiply them by a number by doing it component by component.

### Linear combinations

<span class="anker" id="stufe-1-5"></span>

Almost every calculation in this chapter takes several vectors, multiplies each one by its own number and adds the results. An average is such a calculation, and so is a mixture.

In the picture of arrows: you walk $c_1$ times the distance $\mathbf{v}_1$, then $c_2$ times the distance $\mathbf{v}_2$, and so on. Where you arrive is the result.

:::definition Definition 1.4 (Linear combination)
<span class="anker" id="satz-1-4"></span>

For vectors $\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ and scalars $c_1,\dots,c_k$,

<span class="anker" id="gl-1-4"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\sum_{l=1}^{k}c_l\,\mathbf{v}_l \tag{1.4}$$

is called a __linear combination__ of the vectors $\mathbf{v}_1,\dots,\mathbf{v}_k$. The numbers $c_l$ are called its __coefficients__.
:::

A word of caution when reading: $\mathbf{v}_l$ is bold, so it is the $l$th vector of the list, not the $l$th component of a vector.

::::beispiel [Worked example 1]
$(1,\,2)^{\top}+3\,(0,\,1)^{\top}=(1,\,2)^{\top}+(0,\,3)^{\top}=(1,\,5)^{\top}$.
::::

::::beispiel [Worked example 2] the midpoint
The linear combination $\tfrac12\mathbf{x}_1+\tfrac12\mathbf{x}_2$ of apartments 1 and 2 is

$$\tfrac12\,(60,\,2,\,3)^{\top}+\tfrac12\,(40,\,1,\,1)^{\top}=(50,\ 1.5,\ 2)^{\top}.$$

This is an imaginary apartment that lies exactly halfway between the two in every feature. The point lies in the middle of the connecting segment.
::::

One linear combination is needed especially often in this chapter. If you take all $N$ examples with the coefficient $1/N$, you get the __mean of the examples__

<span class="anker" id="gl-1-5"></span>
$$\bar{\mathbf{x}}=\frac1N\sum_{i=1}^{N}\mathbf{x}_i . \tag{1.5}$$

It is an imagined example that has the average of all examples in every feature: its $j$-th component is the mean of the $j$-th features.

::::beispiel [Worked example 3] the mean of the examples
For the apartment dataset, $\bar{\mathbf{x}}=(65,\ 2.5,\ 3)^{\top}$ (Fig. [5](#abb-5)), the “average apartment”: on average $65\,\mathrm m^2$, $2.5$ rooms and $3$ km to the center.

:::abbildung ml/k1rmittelvektor 5
The mean of the four apartments: the sum of the vectors is formed component by component and then divided by $4$; $5/2=2.5$.
:::
::::

⁠**In short:** A linear combination multiplies each vector by its own number and adds everything up.

:::hintergrund Where the mixtures of two points lie
If, for two vectors $\mathbf{x}_1,\mathbf{x}_2$, you choose the coefficients so that they add up to $1$, that is, $(1-t)\,\mathbf{x}_1+t\,\mathbf{x}_2$ with a number $t$, then the result always lies on the line through the two points. This is because you can rewrite it as

$$(1-t)\,\mathbf{x}_1+t\,\mathbf{x}_2=\mathbf{x}_1+t\,(\mathbf{x}_2-\mathbf{x}_1) .$$

That is: starting from the point $\mathbf{x}_1$, go $t$ times the connecting arrow $\mathbf{x}_2-\mathbf{x}_1$. For $t=0$ you are at $\mathbf{x}_1$, for $t=1$ at $\mathbf{x}_2$, for $t=\tfrac12$ in the middle. All $t$ between $0$ and $1$ give the points of the connecting segment. You need such mixtures whenever you want to form intermediate values between two data points.
:::

### The unit vectors

<span class="anker" id="stufe-1-6"></span>

The simplest vectors have a single component $1$ and zeros everywhere else. For an example this would mean that only one feature is “switched on”, with the value $1$. In the plane they are the two arrows of length $1$ along the axes.

:::definition Definition 1.5 (Unit vector)
<span class="anker" id="satz-1-5"></span>

The $j$th __unit vector__ $\mathbf{e}_j\in\mathbb{R}^d$ has a $1$ in position $j$ and a $0$ in every other position.
:::

In $\mathbb{R}^2$, $\mathbf{e}_1=(1,\,0)^{\top}$ and $\mathbf{e}_2=(0,\,1)^{\top}$. Every vector is a linear combination of the unit vectors, and the coefficients are exactly its components:

<span class="anker" id="gl-1-6"></span>
$$\mathbf{x}=x_1\mathbf{e}_1+x_2\mathbf{e}_2+\dots+x_d\mathbf{e}_d=\sum_{j=1}^d x_j\,\mathbf{e}_j . \tag{1.6}$$

You can see this by computing the right-hand side component by component: in position $j$ only the term $x_j\mathbf{e}_j$ contributes, namely $x_j\cdot1$. No other coefficients are possible, because they would give a different number in some position.

::::beispiel [Worked example]
$\mathbf{x}_1=(60,\,2,\,3)^{\top}=60\,\mathbf{e}_1+2\,\mathbf{e}_2+3\,\mathbf{e}_3$, that is, $60$ times “one square meter” plus $2$ times “one room” plus $3$ times “one kilometer”.
::::

⁠**In short:** The unit vector $\mathbf{e}_j$ has a one in position $j$ and zeros elsewhere; every vector is the sum $\sum_jx_j\mathbf{e}_j$.

:::aufgabe Exercise 1 ★ Reading and writing sums
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Compute $\sum_{i=1}^{5}(2i-1)$ and $\sum_{i=1}^{2}\sum_{j=1}^{3}i\,j$.

</li>

<li>

Write $3+6+9+12$ with a summation sign.

</li>

<li>

Let $a_i$ be the floor area of apartment $i$ from Table [1](#tab-1). What do $\sum_{i=1}^4a_i$ and $\frac14\sum_{i=1}^4a_i$ mean, and which numbers come out?

</li>

</ol>

:::loesung
(a) The summation index $i$ takes the values $1$ to $5$, and the terms are the odd numbers $1,3,5,7,9$:

$$\sum_{i=1}^{5}(2i-1)=1+3+5+7+9=25 .$$

In the double sum, for each fixed $i$ the inner sum is $\sum_{j=1}^3i\,j=i\,(1+2+3)=6i$; the factor $i$ does not depend on $j$ and, by [(1.2)](#gl-1-2), may be moved in front of the inner sum. Then $\sum_{i=1}^2 6i=6+12=18$.

(b) The terms are the multiples of $3$: $3+6+9+12=\sum_{i=1}^43i$. Equally correct is $3\sum_{i=1}^4i$, by the rule for common factors.

(c) $\sum_{i=1}^4a_i=60+40+90+70=260$ is the total floor area of all four apartments in $\mathrm m^2$, and $\frac14\sum_{i=1}^4a_i=65$ is the average floor area of an apartment.
:::
:::

:::aufgabe Exercise 2 ★ Calculating with vectors
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Compute $2\mathbf{u}-3\mathbf{v}$ for $\mathbf{u}=(1,\,-1,\,0)^{\top}$ and $\mathbf{v}=(0,\,1,\,2)^{\top}$.

</li>

<li>

Write $(4,\,-1,\,2)^{\top}$ as a linear combination of the unit vectors of $\mathbb{R}^3$.

</li>

<li>

Find numbers $c_1,c_2$ with $c_1(1,\,2)^{\top}+c_2(2,\,1)^{\top}=(3,\,3)^{\top}$. Draw the solution with arrows.

</li>

<li>

Compute $\mathbf{x}_3-\mathbf{x}_2$ for the apartment dataset and describe in words what the vector says.

</li>

</ol>

:::loesung
(a) Component by component: $2\mathbf{u}=(2,\,-2,\,0)^{\top}$ and $3\mathbf{v}=(0,\,3,\,6)^{\top}$, so $2\mathbf{u}-3\mathbf{v}=(2,\,-5,\,-6)^{\top}$.

(b) By [(1.6)](#gl-1-6), the coefficients are the components: $(4,\,-1,\,2)^{\top}=4\,\mathbf{e}_1-\mathbf{e}_2+2\,\mathbf{e}_3$.

(c) Component by component, the condition reads $c_1+2c_2=3$ and $2c_1+c_2=3$. Subtracting the first equation twice from the second leaves $-3c_2=-3$, so $c_2=1$ and then $c_1=1$. Check: $(1,\,2)^{\top}+(2,\,1)^{\top}=(3,\,3)^{\top}$. In the drawing, you attach the arrow $(2,\,1)^{\top}$ to the tip of $(1,\,2)^{\top}$ and land at $(3,\,3)^{\top}$.

(d) $\mathbf{x}_3-\mathbf{x}_2=(90-40,\ 4-1,\ 6-1)^{\top}=(50,\,3,\,5)^{\top}$: apartment 3 is $50\,\mathrm m^2$ larger than apartment 2, has three more rooms and is $5$ km farther from the center. The vector is the arrow from the point $\mathbf{x}_2$ to the point $\mathbf{x}_3$.
:::
:::

:::aufgabe Exercise 3 ★ A dataset of your own
<span class="anker" id="aufg-3"></span>

Choose four things from your everyday life, for example foods, bicycles or songs, and three properties that you can state as a number for each thing. Measure or look up the values.

<ol class="al">

<li>

Set up the table. What are $N$ and $d$? Write the second example as a vector $\mathbf{x}_2$.

</li>

<li>

Which property that would also interest you is not a number? How could you translate it into numbers?

</li>

<li>

Compute the mean of the examples $\bar{\mathbf{x}}$. Is there a thing that looks exactly like it?

</li>

</ol>

:::loesung
One possible solution: four apples with the features mass in g, diameter in cm and price in cents.

(a) Suppose the table has the rows $(180,\ 7.5,\ 45)$, $(150,\ 7.0,\ 40)$, $(210,\ 8.0,\ 55)$ and $(165,\ 7.2,\ 40)$. Then $N=4$ and $d=3$, and $\mathbf{x}_2=(150,\ 7.0,\ 40)^{\top}$. All that matters is that each thing is described by the same three features in the same order.

(b) The variety is a name, not a number. You can translate it by introducing a separate feature for each variety that is $1$ if the apple belongs to this variety and $0$ otherwise. Simply numbering the varieties, on the other hand, is usually not a good idea: the numbers suggest an order and distances that do not exist between varieties.

(c) The mean of the examples is the average taken component by component, here $\bar{\mathbf{x}}=(176.25,\ 7.425,\ 45)^{\top}$. There is no apple with exactly these values in the table. The mean is an imagined example, not a measured one, and for a property such as the number of rooms it can even be a value that no real thing can take, for instance $2.5$ rooms.
:::
:::
