---
title: Systems of linear equations
pfad: Computer Science / Machine Learning / Mathematical Foundations / Vectors and Matrices
knoten: Foundations 1: Vectors and Matrices
nachschlagen: ja
order: 15211300
summary: So far the input x was given and the output Ax was sought.
tags: system of linear equations, coefficient matrix, right-hand side, solution, augmented matrix, Gaussian elimination, row echelon form, homogeneous
lang: en
---

<span class="anker" id="stufe-12"></span>

:::zweck
So far the input $\mathbf{x}$ was given and the output $\mathbf{A}\mathbf{x}$ was sought. This section asks the reverse question: which input produces a given output? That is a system of linear equations. The section shows how to solve it and when it has no solution, exactly one solution or infinitely many solutions.
:::

### Systems of equations in matrix form

<span class="anker" id="stufe-12-1"></span>

From school you know problems like this: two numbers $x_1$ and $x_2$ satisfy $2x_1+x_2=5$ and $x_1+x_2=3$; what are they? The left-hand sides are the components of a matrix–vector product. So the problem asks: which vector $\mathbf{x}$ is mapped by the matrix $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ to $(5,\,3)^{\top}$?

:::definition Definition 12.1 (System of linear equations)
<span class="anker" id="satz-12-1"></span>

For a matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ and a vector $\mathbf{y}\in\mathbb{R}^m$,

<span class="anker" id="gl-12-1"></span>
$$\mathbf{A}\mathbf{x}=\mathbf{y} \tag{12.1}$$

is called a __system of linear equations__ with $m$ equations and the $n$ unknowns $x_1,\dots,x_n$. The matrix $\mathbf{A}$ is called the __coefficient matrix__, the vector $\mathbf{y}$ the __right-hand side__. Every vector $\mathbf{x}\in\mathbb{R}^n$ that satisfies [(12.1)](#gl-12-1) is called a __solution__.
:::

Written out, row $i$ contains the equation $a_{i1}x_1+\dots+a_{in}x_n=y_i$.

::::beispiel [Worked example]
The system

$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}5\\3\end{pmatrix}$$

has the solution $\mathbf{x}=(2,\,1)^{\top}$: $2\cdot2+1=5$ and $2+1=3$. The coefficient matrix is familiar from Subsection [11.2](einheitsmatrix-und-inverse.html#stufe-11-2), with the inverse $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$. If you multiply the system by this inverse from the left, the solution appears immediately: $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}=(5-3,\ -5+6)^{\top}=(2,\,1)^{\top}$.
::::

⁠**In short:** A system of linear equations $\mathbf{A}\mathbf{x}=\mathbf{y}$ asks which input $\mathbf{x}$ produces the output $\mathbf{y}$.

### Row picture and column picture

<span class="anker" id="stufe-12-2"></span>

As with the matrix–vector product, there are two ways to read a system of equations.

**Row picture.** Each equation on its own describes a set of points. With two unknowns, $2x_1+x_2=5$ is a line in the plane, and so is $x_1+x_2=3$. A solution must satisfy both equations, that is, lie on both lines: it is their point of intersection (Fig. [38](#abb-38), left). With three unknowns, each equation is a plane in space.

**Column picture.** By the column view [(7.3)](das-matrix-vektor-produkt.html#gl-7-3), $\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+\dots+x_n\mathbf{a}_n$. So the equation asks: with which coefficients does the linear combination of the columns give the right-hand side? For the system above: $x_1\,(2,\,1)^{\top}+x_2\,(1,\,1)^{\top}=(5,\,3)^{\top}$, solved by $x_1=2$ and $x_2=1$. This is exactly the picture on the right in Fig. [30](das-matrix-vektor-produkt.html#abb-30).

:::abbildung ml/k1lgs 38
The row picture of three systems of equations with two unknowns. Each equation is a line; a solution lies on all lines. (a) The lines intersect in one point. (b) The lines are parallel and have no point in common. (c) Both equations describe the same line, and each of its points is a solution.
:::

The column picture immediately answers when there is a solution at all. The vectors $\mathbf{A}\mathbf{x}$ form the column space (Subsection [7.4](das-matrix-vektor-produkt.html#stufe-7-4)).

:::satz Theorem 12.2 (Solvability)
<span class="anker" id="satz-12-2"></span>

The system $\mathbf{A}\mathbf{x}=\mathbf{y}$ has a solution if and only if $\mathbf{y}$ lies in the column space of $\mathbf{A}$.
:::

::::beispiel [Worked example]
The system $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)\mathbf{x}=\mathbf{y}$ is solvable for $\mathbf{y}=(3,\,6)^{\top}$, for instance with $\mathbf{x}=(1,\,1)^{\top}$, but not for $\mathbf{y}=(1,\,1)^{\top}$: by Subsection [7.4](das-matrix-vektor-produkt.html#stufe-7-4), the column space is only the line in the direction of $(1,\,2)^{\top}$.
::::

⁠**In short:** In the row picture, a solution is a point common to all equations; in the column picture, it is the choice of coefficients with which the columns give the right-hand side.

### Gaussian elimination

<span class="anker" id="stufe-12-3"></span>

With two unknowns you can find the solution by inspection. With three or more you need a method that always works. The idea is the same as in school: you subtract a multiple of one equation from another so that an unknown disappears. You repeat this until the last equation contains only one unknown.

For this you write down only the numbers: the coefficient matrix and, separated by a vertical bar, the right-hand side. This table is called the __augmented matrix__ $(\mathbf{A}\,|\,\mathbf{y})$.

:::definition Definition 12.3 (Gaussian elimination)
<span class="anker" id="satz-12-3"></span>

__Gaussian elimination__ transforms the augmented matrix with three row operations:

<ol>

<li>

add a multiple of one row to another row;

</li>

<li>

swap two rows;

</li>

<li>

multiply a row by a nonzero number.

</li>

</ol>

The goal is __row echelon form__: in each row, the first nonzero entry is preceded by at least one more zero than in the row above. Then you determine the unknowns from the bottom up (back substitution).
:::

:::satz Theorem 12.4 (Row operations do not change the solutions)
<span class="anker" id="satz-12-4"></span>

A system and the system obtained from it by row operations have the same solutions.
:::

:::beweis Row operations
Every solution of the old system also satisfies the new equations, because these are sums and multiples of the old ones. But each of the three operations can also be undone: subtract the multiple again, swap the rows back, divide by the number. So, conversely, every solution of the new system also satisfies the old one.
:::

::::beispiel [Worked example]
The system

$$\begin{aligned} x_1+2x_2+x_3&=8\\ 2x_1+x_2+x_3&=7\\ x_1+x_2+2x_3&=9 \end{aligned} \qquad\text{has the augmented matrix}\qquad \left(\begin{array}{ccc|c}1&2&1&8\\2&1&1&7\\1&1&2&9\end{array}\right).$$

If you subtract the first row twice from the second and once from the third, $x_1$ disappears from both. If you then swap the new second and third rows and subtract the new second row three times from the third, $x_2$ also disappears from the last row:

$$\left(\begin{array}{ccc|c}1&2&1&8\\0&-3&-1&-9\\0&-1&1&1\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&-3&-1&-9\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&0&-4&-12\end{array}\right).$$

From the bottom up: $-4x_3=-12$, so $x_3=3$; then $-x_2+3=1$, so $x_2=2$; then $x_1+4+3=8$, so $x_1=1$. The solution is $\mathbf{x}=(1,\,2,\,3)^{\top}$, and substituting it into all three equations confirms it.
::::

⁠**In short:** Gaussian elimination eliminates the unknowns step by step with row operations, which do not change the solutions, and then substitutes from the bottom up.

:::hintergrund Why you do not compute an inverse to solve a system
If $\mathbf{A}$ is invertible, the solution is $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}$. This is useful for reasoning but unfavorable as a way of computing. For a system with $n$ equations and $n$ unknowns, Gaussian elimination needs about $\tfrac23n^3$ basic arithmetic operations; computing the inverse costs about $2n^3$, three times as much, and the product $\mathbf{A}^{-1}\mathbf{y}$ comes on top of that. Moreover, a computer calculates with finitely many digits. The inverse can then only be represented in rounded form, and direct elimination usually gives more accurate results. So the inverse is above all a tool for thinking and deriving, not for computing.
:::

### No solution, one solution or infinitely many

<span class="anker" id="stufe-12-4"></span>

Two lines in the plane intersect in one point, are parallel or coincide (Fig. [38](#abb-38)). Exactly two points of intersection are impossible. The same holds for every system of linear equations, no matter how large.

:::satz Theorem 12.5 (Number of solutions)
<span class="anker" id="satz-12-5"></span>

A system of linear equations has either no solution, exactly one solution or infinitely many solutions.
:::

:::beweis Number of solutions
It suffices to show: if the system has two different solutions $\mathbf{x}\ne\mathbf{x}'$, it has infinitely many. For every number $t$,

$$\mathbf{A}\bigl(\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})\bigr)=\mathbf{A}\mathbf{x}+t\,(\mathbf{A}\mathbf{x}'-\mathbf{A}\mathbf{x})=\mathbf{y}+t\,(\mathbf{y}-\mathbf{y})=\mathbf{y} ,$$

so every point $\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})$ of the line through $\mathbf{x}$ and $\mathbf{x}'$ is a solution, and different values of $t$ give different points.
:::

The system $\mathbf{A}\mathbf{x}=\mathbf{0}$ with right-hand side zero is called __homogeneous__. It always has the solution $\mathbf{x}=\mathbf{0}$. If you know a single solution $\mathbf{x}_{\mathrm s}$ of the system $\mathbf{A}\mathbf{x}=\mathbf{y}$, you get all the others by adding the solutions of the homogeneous system: $\mathbf{A}\mathbf{x}=\mathbf{y}$ holds exactly when $\mathbf{A}(\mathbf{x}-\mathbf{x}_{\mathrm s})=\mathbf{y}-\mathbf{y}=\mathbf{0}$.

::::beispiel [Worked example]
The three systems in Fig. [38](#abb-38):

<ol class="al">

<li>

$2x_1+x_2=5$, $x_1+x_2=3$: exactly one solution, $(2,\,1)^{\top}$.

</li>

<li>

$x_1+x_2=3$, $x_1+x_2=1$: no solution, because the same sum cannot be both $3$ and $1$.

</li>

<li>

$x_1+x_2=3$, $2x_1+2x_2=6$: the second equation is twice the first. One solution is $\mathbf{x}_{\mathrm s}=(3,\,0)^{\top}$, and the homogeneous system $x_1+x_2=0$ is solved by all multiples of $(-1,\,1)^{\top}$. So all solutions are $\mathbf{x}=(3,\,0)^{\top}+t\,(-1,\,1)^{\top}$ with arbitrary $t$.

</li>

</ol>
::::

⁠**In short:** A system of linear equations has no solution, exactly one or infinitely many; all solutions are one solution plus the solutions of the homogeneous system.

### More equations than unknowns

<span class="anker" id="stufe-12-5"></span>

With data, the numbers of equations and unknowns are often unbalanced. Suppose you are looking for weights $w_1$ for the floor area and $w_2$ for the rooms such that the weighted sum hits the actual price exactly for three apartments. These are three equations for two unknowns.

:::definition Definition 12.6 (Overdetermined, underdetermined)
<span class="anker" id="satz-12-6"></span>

A system of linear equations with more equations than unknowns ($m>n$) is called __overdetermined__, one with fewer equations than unknowns ($m<n$) __underdetermined__.
:::

An overdetermined system usually has no solution: two equations already fix two unknowns, and the third equation would have to hold by coincidence as well. In the column picture: for $n<m$, the column space of $n$ columns in $\mathbb{R}^m$ is only a small part of $\mathbb{R}^m$, and the right-hand side almost never lies in it. An underdetermined system, on the other hand, has infinitely many solutions if it is solvable at all: in row echelon form at least one unknown remains without a pivot of its own, and it can be chosen freely.

::::beispiel [Worked example]
For apartments 1 to 3 with the prices $200$, $130$ and $290$ thousand euros, the system reads

$$60\,w_1+2\,w_2=200,\qquad 40\,w_1+w_2=130,\qquad 90\,w_1+4\,w_2=290 .$$

The first two equations give $w_1=3$ and $w_2=10$: if you subtract the second twice from the first, $-20\,w_1=-60$ remains. Substituted into the third, however, this gives $270+40=310\ne290$. The system has no solution. No pair of weights hits all three prices exactly. What to look for instead in such a case is a question of its own.
::::

⁠**In short:** An overdetermined system has more equations than unknowns and is usually unsolvable; an underdetermined one has fewer and, if it is solvable, infinitely many solutions.

:::aufgabe Exercise 28 ★★ Gaussian elimination
<span class="anker" id="aufg-28"></span>

Solve with Gaussian elimination and check your result:

$$x_1+x_2+x_3=6,\qquad 2x_1+3x_2+x_3=11,\qquad x_1-x_2+2x_3=5 .$$

:::loesung
The augmented matrix is $\Bigl(\begin{smallmatrix}1&1&1&|&6\\2&3&1&|&11\\1&-1&2&|&5\end{smallmatrix}\Bigr)$. Subtracting the first row twice from the second and once from the third gives the rows $(0,\,1,\,-1\,|\,-1)$ and $(0,\,-2,\,1\,|\,-1)$. If you then add the new second row twice to the third, the third becomes $(0,\,0,\,-1\,|\,-3)$. The row echelon form reads

$$x_1+x_2+x_3=6,\qquad x_2-x_3=-1,\qquad -x_3=-3 .$$

From the bottom up: $x_3=3$, $x_2=-1+3=2$, $x_1=6-2-3=1$. Check: $1+2+3=6$, $2+6+3=11$, $1-2+6=5$. The solution is $\mathbf{x}=(1,\,2,\,3)^{\top}$.
:::
:::

:::aufgabe Exercise 29 ★★ How many solutions?
<span class="anker" id="aufg-29"></span>

For each system, determine the solution set and draw the row picture:

<ol class="al">

<li>

$x_1+2x_2=3$, $2x_1+4x_2=6$;

</li>

<li>

$x_1+2x_2=3$, $2x_1+4x_2=5$;

</li>

<li>

$x_1+2x_2=3$, $x_1-x_2=0$.

</li>

</ol>

:::loesung
(a) The second equation is twice the first; both describe the same line. Infinitely many solutions: with $x_2=t$, we get $x_1=3-2t$, so $\mathbf{x}=(3,\,0)^{\top}+t\,(-2,\,1)^{\top}$.

(b) Doubling the first equation gives $2x_1+4x_2=6$, which contradicts $2x_1+4x_2=5$. The lines are parallel; there is no solution.

(c) The second equation gives $x_1=x_2$; substituted into the first, $3x_2=3$. Exactly one solution: $\mathbf{x}=(1,\,1)^{\top}$, the point of intersection of two nonparallel lines.
:::
:::

:::aufgabe Exercise 30 ★★ Weights that fit
<span class="anker" id="aufg-30"></span>

Add apartment 4 with the price $240$ thousand euros to the overdetermined system from Subsection [12.5](#stufe-12-5).

<ol class="al">

<li>

Which of the four apartments are hit exactly by $w_1=3$, $w_2=10$?

</li>

<li>

Write the system with four equations as $\mathbf{A}\mathbf{w}=\mathbf{y}$. What are the sizes of $\mathbf{A}$, $\mathbf{w}$ and $\mathbf{y}$? What does “no solution” mean in the column picture?

</li>

</ol>

:::loesung
(a) With $w_1=3$, $w_2=10$: apartment 1: $180+20=200$ (hit), apartment 2: $120+10=130$ (hit), apartment 3: $270+40=310$ instead of $290$ (not hit), apartment 4: $210+30=240$ (hit). Three of the four prices are right, but not all of them.

(b) $\mathbf{A}=\Biggl(\begin{smallmatrix}60&2\\40&1\\90&4\\70&3\end{smallmatrix}\Biggr)\in\mathbb{R}^{4\times2}$, $\mathbf{w}\in\mathbb{R}^2$, $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}\in\mathbb{R}^4$. The column space of $\mathbf{A}$ consists of all combinations $w_1\mathbf{a}_1+w_2\mathbf{a}_2$ of the floor area column and the rooms column; it is a plane through the origin in $\mathbb{R}^4$. “No solution” means: the price vector $\mathbf{y}$ does not lie in this plane. No choice of the two weights produces exactly these four prices.
:::
:::
