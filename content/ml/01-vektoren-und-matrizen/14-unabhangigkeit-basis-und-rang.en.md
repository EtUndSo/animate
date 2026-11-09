---
title: Independence, basis and rank
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15211400
summary: Some vectors in a list bring nothing new, because they can be put together from the others.
tags: span, linearly independent, linearly dependent, basis, dimension, standard basis, rank, full rank
lang: en
---

<span class="anker" id="stufe-13"></span>

:::zweck
Some vectors in a list bring nothing new, because they can be put together from the others. This section measures how many truly different directions a matrix contains, and it shows what it means for data when features carry the same information twice.
:::

### The span

<span class="anker" id="stufe-13-1"></span>

The column space of a matrix is the set of all linear combinations of its columns. The same construction gives a set for every list of vectors, and this set gets its own name (Fig. [39](#abb-39)).

:::abbildung ml/k1spann 39
The span (blue) of three lists of vectors in the plane, drawn at a scale of $1:2$. (a) One vector spans a line through the origin. (b) A second vector on the same line changes nothing. (c) Two vectors in different directions span the whole plane.
:::

:::definition Definition 13.1 (Span)
<span class="anker" id="satz-13-1"></span>

The __span__ of the vectors $\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ is the set of all their linear combinations:

<span class="anker" id="gl-13-1"></span>
$$\operatorname{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}=\Bigl\{\sum_{l=1}^kc_l\,\mathbf{v}_l\ :\ c_1,\dots,c_k\in\mathbb{R}\Bigr\}. \tag{13.1}$$
:::

So the column space of a matrix is the span of its columns. Along with any two of its vectors, every linear combination of them also lies in the span; adding and taking multiples never lead you out of it.

::::beispiel [Worked example]
$\operatorname{span}\{(1,\,2)^{\top}\}$ is the line of all multiples $c\,(1,\,2)^{\top}$. The span of $(1,\,2)^{\top}$ and $(2,\,4)^{\top}$ is the same line, because $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$. The span of $(1,\,0)^{\top}$ and $(1,\,1)^{\top}$ is the whole plane: every vector $(y_1,\,y_2)^{\top}$ is $(y_1-y_2)\,(1,\,0)^{\top}+y_2\,(1,\,1)^{\top}$. In $\mathbb{R}^3$, $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ is the plane of all vectors with $x_3=0$.
::::

⁠**In short:** The span of a list of vectors is everything you can form from them as a linear combination.

### Linear independence

<span class="anker" id="stufe-13-2"></span>

In Fig. [39](#abb-39) (b), the second vector brings nothing new: it already lies in the span of the first. A dataset can have the same weakness. If it contains the number of bedrooms, the number of living rooms and the total number of rooms, the third column is the sum of the first two and carries no information of its own. You need a word for the property that nothing in a list of vectors is superfluous.

:::definition Definition 13.2 (Linear independence)
<span class="anker" id="satz-13-2"></span>

Vectors $\mathbf{v}_1,\dots,\mathbf{v}_k$ are called __linearly independent__ if

<span class="anker" id="gl-13-2"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\mathbf{0} \tag{13.2}$$

holds only for $c_1=c_2=\dots=c_k=0$. Otherwise they are called __linearly dependent__.
:::

Equivalently, linearly dependent means: at least one of the vectors is a linear combination of the others. Indeed, if [(13.2)](#gl-13-2) holds with a coefficient $c_l\ne0$, you can solve for $\mathbf{v}_l$: $\mathbf{v}_l=-\sum_{l'\ne l}(c_{l'}/c_l)\,\mathbf{v}_{l'}$. Conversely, such a representation immediately gives a combination with the coefficient $-1$ in front of $\mathbf{v}_l$.

::::beispiel [Worked example]
$(1,\,2)^{\top}$ and $(2,\,4)^{\top}$ are linearly dependent: $2\,(1,\,2)^{\top}-(2,\,4)^{\top}=\mathbf{0}$. The vectors $(1,\,0)^{\top}$ and $(1,\,1)^{\top}$ are linearly independent: from $c_1(1,\,0)^{\top}+c_2(1,\,1)^{\top}=(c_1+c_2,\ c_2)^{\top}=\mathbf{0}$ it follows first that $c_2=0$ and then that $c_1=0$. The three vectors $(1,\,0,\,1)^{\top}$, $(0,\,1,\,1)^{\top}$ and $(1,\,1,\,2)^{\top}$ are linearly dependent, because the third is the sum of the first two.
::::

⁠**In short:** Linearly independent means: none of the vectors can be combined from the others; there is no redundancy.

### Basis and dimension

<span class="anker" id="stufe-13-3"></span>

If you want to describe a span as economically as possible, you take as few vectors as necessary, but enough to reach everything. Such a list is like a coordinate system: every vector of the span then has exactly one representation in terms of it.

:::definition Definition 13.3 (Basis, dimension)
<span class="anker" id="satz-13-3"></span>

A list of linearly independent vectors whose span is a set $\mathcal S$ is called a __basis__ of $\mathcal S$. The number of vectors in a basis is called the __dimension__ of $\mathcal S$, written $\dim\mathcal S$.
:::

A set $\mathcal S$ has many different bases, but they all consist of the same number of vectors; this is a theorem of linear algebra on which the definition of dimension rests. The unit vectors $\mathbf{e}_1,\dots,\mathbf{e}_d$ form a basis of $\mathbb{R}^d$, the __standard basis__; that is why $\dim\mathbb{R}^d=d$.

:::satz Theorem 13.4 (Unique coordinates)
<span class="anker" id="satz-13-4"></span>

If $\mathbf{v}_1,\dots,\mathbf{v}_k$ is a basis of $\mathcal S$, then every vector $\mathbf{x}\in\mathcal S$ has exactly one representation $\mathbf{x}=\sum_lc_l\mathbf{v}_l$.
:::

:::beweis Unique coordinates
There is at least one representation, because the basis spans $\mathcal S$. If there were two, $\sum_lc_l\mathbf{v}_l=\sum_lc_l'\mathbf{v}_l$, their difference would be $\sum_l(c_l-c_l')\mathbf{v}_l=\mathbf{0}$. By linear independence, all $c_l-c_l'=0$.
:::

::::beispiel [Worked example]
$(1,\,0)^{\top}$ and $(1,\,1)^{\top}$ form a basis of $\mathbb{R}^2$: they are linearly independent and span the plane. In this basis, the vector $(3,\,2)^{\top}$ has the coordinates $1$ and $2$, because $(3,\,2)^{\top}=1\cdot(1,\,0)^{\top}+2\cdot(1,\,1)^{\top}$. The line $\operatorname{span}\{(0,\,1)^{\top}\}$ has dimension $1$, even though its vectors have two components.
::::

⁠**In short:** A basis is a list of independent vectors that spans everything; its length is the dimension.

### The rank of a matrix

<span class="anker" id="stufe-13-4"></span>

A matrix with $n$ columns can contain fewer than $n$ truly different directions. The number of directions that remain when you leave out everything superfluous tells you how much a matrix actually accomplishes.

:::definition Definition 13.5 (Rank)
<span class="anker" id="satz-13-5"></span>

The __rank__ $\operatorname{rank}\mathbf{A}$ of a matrix $\mathbf{A}$ is the largest number of linearly independent columns of $\mathbf{A}$. It equals the dimension of its column space.
:::

:::satz Theorem 13.6 (Column rank equals row rank)
<span class="anker" id="satz-13-6"></span>

The largest number of linearly independent columns of a matrix equals the largest number of linearly independent rows. In particular, $\operatorname{rank}\mathbf{A}=\operatorname{rank}\mathbf{A}^{\top}\le\min(m,n)$ for $\mathbf{A}\in\mathbb{R}^{m\times n}$.
:::

If $\operatorname{rank}\mathbf{A}=\min(m,n)$, then $\mathbf{A}$ has __full rank__. In practice, you determine the rank with Gaussian elimination: row operations do not change it, and in row echelon form it is the number of rows that do not consist entirely of zeros.

::::beispiel [Worked example]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ has rank $1$: the second column is twice the first, and likewise the second row is twice the first. For

$$\mathbf K=\begin{pmatrix}1&0&1\\0&1&1\\1&1&2\end{pmatrix}$$

you subtract the first and the second row from the third and get the rows $(1,0,1)$, $(0,1,1)$, $(0,0,0)$. Two rows are nonzero, so $\operatorname{rank}\mathbf K=2$; indeed, the third column is the sum of the first two. The data matrix of the apartments has full rank $3$.
::::

⁠**In short:** The rank counts how many truly different directions the columns of a matrix contain, and there are just as many as in its rows.

:::hintergrund Why there are as many independent rows as columns
This is not obvious: the rows and the columns of a $3\times5$ matrix live in completely different spaces. A short argument goes like this. Suppose $r$ columns of $\mathbf{A}$ are linearly independent and every other column is a linear combination of them. These $r$ columns form a matrix $\mathbf G\in\mathbb{R}^{m\times r}$. Each column $\mathbf{a}_j$ of $\mathbf{A}$ is then $\mathbf G$ times a coefficient vector with $r$ components. If you write these coefficient vectors as the columns of a matrix $\mathbf F\in\mathbb{R}^{r\times n}$, then $\mathbf{A}=\mathbf G\mathbf F$ by [(9.2)](das-matrixprodukt.html#gl-9-2). Now read the same product row by row: row $i$ of $\mathbf{A}$ is row $i$ of $\mathbf G$ times $\mathbf F$, that is, a linear combination of the $r$ rows of $\mathbf F$. So all rows of $\mathbf{A}$ lie in the span of the $r$ rows of $\mathbf F$, a set of dimension at most $r$, and therefore no more than $r$ of them can be linearly independent. So the rows have at most as many independent directions as the columns. Applying the same argument to $\mathbf{A}^{\top}$, whose columns are the rows of $\mathbf{A}$, gives the reverse inequality. So the two numbers are equal.
:::

### The null space and the rank–nullity theorem

<span class="anker" id="stufe-13-5"></span>

A matrix with $n$ columns accepts vectors from $n$ directions. Some of these directions arrive in the result; the rest are mapped to the zero vector and are lost. The lost directions form a set of their own.

:::definition Definition 13.7 (Null space)
<span class="anker" id="satz-13-7"></span>

The __null space__ of a matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ is the set of all vectors that $\mathbf{A}$ maps to the zero vector:

<span class="anker" id="gl-13-3"></span>
$$\ker\mathbf{A}=\{\mathbf{x}\in\mathbb{R}^n:\ \mathbf{A}\mathbf{x}=\mathbf{0}\} . \tag{13.3}$$
:::

The null space is the solution set of the homogeneous system from Subsection [12.4](lineare-gleichungssysteme.html#stufe-12-4). It always contains the zero vector, and along with any two of its vectors it also contains every linear combination of them; so it makes sense to speak of its dimension.

:::satz Theorem 13.8 (Rank–nullity theorem)
<span class="anker" id="satz-13-8"></span>

For every matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$,

<span class="anker" id="gl-13-4"></span>
$$\dim\ker\mathbf{A}+\operatorname{rank}\mathbf{A}=n . \tag{13.4}$$
:::

The $n$ directions of the input are divided up: whatever does not arrive in the result ends up in the null space. With Gaussian elimination you can see it like this: in row echelon form there are $\operatorname{rank}\mathbf{A}$ pivots. The remaining $n-\operatorname{rank}\mathbf{A}$ unknowns have no pivot of their own and can be chosen freely in the homogeneous system. Each of them contributes one direction of the null space.

:::satz Theorem 13.9 (When a square matrix is invertible)
<span class="anker" id="satz-13-9"></span>

For $\mathbf{A}\in\mathbb{R}^{n\times n}$, the following are equivalent: (i) $\mathbf{A}$ is invertible; (ii) $\ker\mathbf{A}=\{\mathbf{0}\}$; (iii) $\operatorname{rank}\mathbf{A}=n$; (iv) the columns of $\mathbf{A}$ are linearly independent.
:::

:::beweis Invertibility
(i) implies (ii) by Subsection [11.5](einheitsmatrix-und-inverse.html#stufe-11-5). (ii), (iii) and (iv) are equivalent by the rank–nullity theorem and the definition of rank. It remains to show that (iii) and (ii) imply (i). If $\operatorname{rank}\mathbf{A}=n$, the column space is a space of dimension $n$ in $\mathbb{R}^n$, hence all of $\mathbb{R}^n$. So every system $\mathbf{A}\mathbf{c}_j=\mathbf{e}_j$ is solvable, and the solutions form the columns of a matrix $\mathbf{C}$ with $\mathbf{A}\mathbf{C}=\mathbf{I}$. Moreover, $\mathbf{A}(\mathbf{C}\mathbf{A}-\mathbf{I})=\mathbf{A}\mathbf{C}\mathbf{A}-\mathbf{A}=\mathbf 0$. So every column of $\mathbf{C}\mathbf{A}-\mathbf{I}$ lies in the null space, which by (ii) contains only the zero vector. Hence $\mathbf{C}\mathbf{A}=\mathbf{I}$ as well, and $\mathbf{C}=\mathbf{A}^{-1}$.
:::

::::beispiel [Worked example]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ has the null space $\operatorname{span}\{(2,\,-1)^{\top}\}$, of dimension $1$, and rank $1$: $1+1=2$. The matrix $\mathbf K$ from above has the null space $\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$, because its third column is the sum of the first two; with $\operatorname{rank}\mathbf K=2$ we get $1+2=3$.
::::

**Rank and solvability.** With rank and null space, the questions from Section [12](lineare-gleichungssysteme.html#stufe-12) can be answered by numbers, even for matrices that are not square. Is there a solution? Is it unique? Is there one for every right-hand side?

:::satz Theorem 13.10 (Solvability and rank)
<span class="anker" id="satz-13-10"></span>

For $\mathbf{A}\in\mathbb{R}^{m\times n}$ and $\mathbf{y}\in\mathbb{R}^m$:

<ol class="rm">

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ is solvable if and only if $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rank}\mathbf{A}$;

</li>

<li>

if the system is solvable, the solution is unique if and only if $\operatorname{rank}\mathbf{A}=n$;

</li>

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ is solvable for every $\mathbf{y}\in\mathbb{R}^m$ if and only if $\operatorname{rank}\mathbf{A}=m$.

</li>

</ol>
:::

:::beweis Solvability and rank
(i) By Subsection [12.2](lineare-gleichungssysteme.html#stufe-12-2), the system is solvable exactly when $\mathbf{y}$ lies in the column space of $\mathbf{A}$. If $\mathbf{y}$ lies in it, the additional column brings no new direction: the columns of $(\mathbf{A}\,|\,\mathbf{y})$ span the same space as those of $\mathbf{A}$, and both ranks equal its dimension. If $\mathbf{y}$ does not lie in it, take $r=\operatorname{rank}\mathbf{A}$ linearly independent columns $\mathbf g_1,\dots,\mathbf g_r$ of $\mathbf{A}$ and add $\mathbf{y}$. From $c_1\mathbf g_1+\dots+c_r\mathbf g_r+c\,\mathbf{y}=\mathbf{0}$ it follows that $c=0$, because otherwise $\mathbf{y}$ would be a linear combination of the $\mathbf g_l$ and would lie in the column space; then all $c_l=0$ as well. So $(\mathbf{A}\,|\,\mathbf{y})$ has at least $r+1$ linearly independent columns, and $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})>\operatorname{rank}\mathbf{A}$.

(ii) By Subsection [12.4](lineare-gleichungssysteme.html#stufe-12-4), all solutions are one solution plus the vectors of the null space. So the solution is unique exactly when $\ker\mathbf{A}=\{\mathbf{0}\}$, and by the rank–nullity theorem this means $\operatorname{rank}\mathbf{A}=n$.

(iii) Every $\mathbf{y}$ lies in the column space exactly when the column space is all of $\mathbb{R}^m$. This is the case exactly when it has dimension $m$, that is, when $\operatorname{rank}\mathbf{A}=m$.
:::

For a square matrix with $\operatorname{rank}\mathbf{A}=n=m$, (ii) and (iii) come together: exactly one solution for every right-hand side, in agreement with the theorem on invertibility.

::::beispiel [Worked example]
For $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$, $\operatorname{rank}\mathbf{A}=1$. With $\mathbf{y}=(1,\,1)^{\top}$, the augmented matrix has the rows $(1,\,2\,|\,1)$ and $(2,\,4\,|\,1)$; subtracting the first twice from the second leaves $(0,\,0\,|\,-1)$, which is not a zero row. So $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=2\ne1$, and the system is unsolvable, as in Subsection [12.2](lineare-gleichungssysteme.html#stufe-12-2). With $\mathbf{y}=(3,\,6)^{\top}$, on the other hand, $(0,\,0\,|\,0)$ remains, the ranks are equal, and the system is solvable. Because $\operatorname{rank}\mathbf{A}=1<2=n$, the solution is not unique: all solutions are $(1,\,1)^{\top}+t\,(2,\,-1)^{\top}$. And because $\operatorname{rank}\mathbf{A}=1<2=m$, there are right-hand sides without a solution. In the overdetermined system from Subsection [12.5](lineare-gleichungssysteme.html#stufe-12-5), $\operatorname{rank}\mathbf{A}=2=n$: if there were a solution, it would be unique. But there is none, so by (i), $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=3$ there.
::::

⁠**In short:** The null space collects the directions that a matrix maps to zero; null space and rank share the $n$ input directions between them. A system $\mathbf{A}\mathbf{x}=\mathbf{y}$ is solvable exactly when the right-hand side does not increase the rank, and the solution is unique exactly when the null space contains only the zero vector.

### Dependent features

<span class="anker" id="stufe-13-6"></span>

In real datasets, features sometimes carry the same information twice. A questionnaire records body weight in kilograms and, for a different analysis, once more in pounds. A house description gives the floor area of the ground floor, that of the upper floor and the total floor area. For the data matrix this means: its columns are linearly dependent, and its rank is smaller than the number of features.

::::beispiel [Worked example] ground floor, upper floor, total floor area
Four houses:

$$\mathbf{X}=\begin{pmatrix}50&40&90\\60&0&60\\45&45&90\\70&30&100\end{pmatrix}\qquad(\text{areas in }\mathrm m^2).$$

The third column is the sum of the first two. So $\operatorname{rank}\mathbf{X}=2<3$, and the null space contains $\mathbf k=(1,\,1,\,-1)^{\top}$, because $\mathbf{X}\mathbf k=\mathbf{0}$. Two things follow from this.

<ul>

<li>

⁠**The weights are not unique.** For every number $t$, $\mathbf{w}$ and $\mathbf{w}+t\,\mathbf k$ give the same predictions, because $\mathbf{X}(\mathbf{w}+t\,\mathbf k)=\mathbf{X}\mathbf{w}+t\,\mathbf{X}\mathbf k=\mathbf{X}\mathbf{w}$. The weights $(3,\,3,\,0)^{\top}$, “$3$ per square meter of ground floor and of upper floor”, and $(0,\,0,\,3)^{\top}$, “$3$ per square meter of total floor area”, both give $(270,\,180,\,270,\,300)^{\top}$. From the predictions alone you cannot tell which weights were meant, and it makes no sense to interpret any single one of these weights.

</li>

<li>

⁠**The Gram matrix of the features is singular.** From $\mathbf{X}\mathbf k=\mathbf{0}$ it follows that $\mathbf{X}^{\top}\mathbf{X}\mathbf k=\mathbf{X}^{\top}\mathbf{0}=\mathbf{0}$ with $\mathbf k\ne\mathbf{0}$. By Subsection [11.5](einheitsmatrix-und-inverse.html#stufe-11-5), $\mathbf{X}^{\top}\mathbf{X}$ then has no inverse.

</li>

</ul>
::::

::::beispiel [Worked example] kilograms and pounds
One pound is exactly $0.45359237$ kg, so a mass in pounds is $c=1/0.45359237\approx2.20462$ times the same mass in kilograms. Three people with height (cm), mass (kg) and mass (pounds):

$$\mathbf{X}=\begin{pmatrix}170&70&70\,c\\182&85&85\,c\\165&60&60\,c\end{pmatrix}\approx\begin{pmatrix}170&70&154.3\\182&85&187.4\\165&60&132.3\end{pmatrix}.$$

The third column is $c$ times the second, so $\operatorname{rank}\mathbf{X}=2$ and $(0,\,c,\,-1)^{\top}$ lies in the null space. The pound column brings no new information; it merely duplicates information that is already there.
::::

⁠**In short:** If features carry the same information twice, the columns of the data matrix are linearly dependent; then the rank is smaller than $d$, different weights give the same predictions, and $\mathbf{X}^{\top}\mathbf{X}$ is not invertible.

:::aufgabe Exercise 31 ★★ Rank and null space
<span class="anker" id="aufg-31"></span>

Determine the rank and the null space of

$$\mathbf{A}_1=\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}\qquad\text{and}\qquad \mathbf{A}_2=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}$$

and check the rank–nullity theorem in each case. Which of the two matrices is invertible?

:::loesung
$\mathbf{A}_1$: the second row is twice the first. If you subtract twice the first row from the second, and the first row from the third, the rows $(1,2,3)$, $(0,0,0)$, $(0,-2,-2)$ remain; after swapping the two lower rows, this is a row echelon form with two pivots, so $\operatorname{rank}\mathbf{A}_1=2$. The null space follows from the equations $x_1+2x_2+3x_3=0$ and $-2x_2-2x_3=0$: with $x_3=t$, we get $x_2=-t$ and $x_1=-2(-t)-3t=-t$, so $\ker\mathbf{A}_1=\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$. Check: the sum of the first two columns is $(3,\,6,\,1)^{\top}$, and the third column is $(3,\,6,\,1)^{\top}$. Rank–nullity theorem: $1+2=3$. $\mathbf{A}_1$ is not invertible.

$\mathbf{A}_2$: subtracting the first row from the third gives $(0,\,-1,\,1)$; adding the second row gives $(0,\,0,\,2)$. Three pivots, so $\operatorname{rank}\mathbf{A}_2=3$ and $\ker\mathbf{A}_2=\{\mathbf{0}\}$. Rank–nullity theorem: $0+3=3$. $\mathbf{A}_2$ is invertible; its determinant is $1\cdot(1-0)-1\cdot(0-1)+0=2\ne0$.
:::
:::

:::aufgabe Exercise 32 ★★ Kilograms and pounds
<span class="anker" id="aufg-32"></span>

Use the data matrix of the three people from Subsection [13.6](#stufe-13-6).

<ol class="al">

<li>

Give two different weight vectors that produce the same predictions for all three people, such that one uses only the kilogram column and the other only the pound column.

</li>

<li>

The table gives the pound values rounded to one decimal place. Are the columns of the rounded table still exactly linearly dependent? What does this tell you about a rank computed from rounded data?

</li>

</ol>

:::loesung
(a) The weights $(0,\,1,\,0)^{\top}$ predict each person's mass in kilograms, that is, $(70,\,85,\,60)^{\top}$. The same predictions are given by the weights $(0,\,0,\,1/c)^{\top}\approx(0,\ 0,\ 0.4536)^{\top}$, which use only the pound column, because $\frac1c\cdot c\,x=x$. The two weight vectors differ by $\frac1c\,(0,\,c,\,-1)^{\top}$, a vector in the null space.

(b) The ratios of the rounded pound values to the kilogram values are $154.3/70\approx2.20429$, $187.4/85\approx2.20471$ and $132.3/60=2.205$, not exactly equal. So the rounded columns are no longer exactly proportional, and, computed exactly, the rounded table has full rank $3$. In terms of content, nothing has changed: the pound column still carries almost nothing but the information of the kilogram column. Tiny roundings make the rank jump from $2$ to $3$. For measured or rounded data, the rank alone therefore does not tell you whether two features carry practically the same information.
:::
:::

:::aufgabe Exercise 33 ★★ A district as a number
<span class="anker" id="aufg-33"></span>

The apartments are located either in the north or in the south. You translate this into two features: “North” is $1$ for apartments in the north and $0$ otherwise, “South” likewise for the south. For a base price you also append a column of ones (Subsection [8.5](lineare-abbildungen.html#stufe-8-5)). Four apartments, alternating north and south, give

$$\mathbf{X}=\begin{pmatrix}1&1&0\\1&0&1\\1&1&0\\1&0&1\end{pmatrix}\qquad(\text{columns: ones, North, South}).$$

<ol class="al">

<li>

Determine the rank of $\mathbf{X}$ and a vector $\mathbf k\ne\mathbf{0}$ in the null space. Which relationship between the columns lies behind it?

</li>

<li>

Show that the weights $(100,\,20,\,0)^{\top}$ and $(80,\,40,\,20)^{\top}$ give the same predictions. How do you remove the dependence without losing information?

</li>

</ol>

:::loesung
(a) Each apartment lies either in the north or in the south, so in every row the column “North” plus the column “South” equals $1$, the same as the column of ones. The columns are linearly dependent, and $\mathbf k=(1,\,-1,\,-1)^{\top}$ lies in the null space: $\mathbf{X}\mathbf k=\mathbf{0}$. The first and the second column are independent, so $\operatorname{rank}\mathbf{X}=2$.

(b) $\mathbf{X}\,(100,\,20,\,0)^{\top}=(120,\,100,\,120,\,100)^{\top}$ and $\mathbf{X}\,(80,\,40,\,20)^{\top}=(120,\,100,\,120,\,100)^{\top}$. The two weight vectors differ by $(20,\,-20,\,-20)^{\top}=20\,\mathbf k$. You remove the dependence by dropping one of the two columns “North” or “South”, for example “South”. Then the base price is the price in the south, and the weight of “North” is the premium for the north. No information is lost, because “South” is always $1-\text{North}$ and can be recovered at any time.
:::
:::
