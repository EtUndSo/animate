---
title: Automatic differentiation
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15231100
summary: With the computational graph, derivatives can be computed mechanically, without rearranging formulas and exactly up to the rounding of the elementary operations.
tags: Automatic differentiation, forward mode, tangent value, adjoint, reverse mode
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
With the computational graph, derivatives can be computed mechanically, without rearranging formulas and exactly up to the rounding of the elementary operations. This is called automatic differentiation. There are two ways to combine the local derivatives: forward, in step with the calculation, or backward, from the result to the inputs. Reverse mode delivers the derivative of a number with respect to all its inputs in a single pass, and this section shows why that costs so little.
:::

### What automatic differentiation is

<span class="anker" id="stufe-10-1"></span>

There are three ways to get the derivative of a calculation. You can transform the formula with the rules; this is called symbolic differentiation, and by Section [9.1](rechengraphen.html#stufe-9-1) the formulas grow quickly in the process. You can evaluate the function at two nearby points and form a difference quotient; this is called numerical differentiation, it is only approximately correct, and Section [11](numerische-ableitung-und-gradientenprufung.html#stufe-11) examines its error. The third way combines the advantages of the other two.

:::definition Definition 10.1 (Automatic differentiation)
<span class="anker" id="satz-10-1"></span>

__Automatic differentiation__ computes derivatives of a calculation by applying the chain rule to its computational graph: it evaluates the local derivatives with the numbers of the calculation and combines them according to the sum over the paths.
:::

Automatic differentiation calculates with numbers, not with formulas, and therefore no expressions swell. It approximates nothing: the result is the exact derivative, distorted only by the rounding of the individual calculation steps. And it works for every program that consists of elementary operations, even with loops and branches, because for the given inputs the program yields a computational graph. The step-by-step calculation in the example in Section [9.1](rechengraphen.html#stufe-9-1) was already automatic differentiation.

::::beispiel [Worked example]
For [(9.1)](rechengraphen.html#gl-9-1), the previous section assembled the derivatives $5$, $8$ and $3$ from the local derivatives, without multiplying out or differentiating the formula of $f$. That was automatic differentiation, though still without a fixed procedure for the order of the calculation. The two following subsections give this order.
::::

⁠**In short:** Automatic differentiation applies the chain rule with numbers to the computational graph; it is exact up to rounding and needs no formula.

### Forward mode

<span class="anker" id="stufe-10-2"></span>

The first option follows the calculation itself. You decide in which direction you change the inputs, and at each node you carry along, next to its value, how fast that value changes under this variation.

:::definition Definition 10.2 (Forward mode)
<span class="anker" id="satz-10-2"></span>

In __forward mode__, you choose a direction $\dot{\mathbf{x}}\in\mathbb{R}^n$ for the inputs and compute, for each node $b$, in addition to its value, the number

<span class="anker" id="gl-10-1"></span>
$$\dot b=\sum_{a\text{ predecessor of }b}\frac{\partial b}{\partial a}\,\dot a , \tag{10.1}$$

in the same order as the values. This number is called the __tangent value__ of $b$; the input nodes receive the components of $\dot{\mathbf{x}}$ as their tangent values.
:::

The name recalls the tangent line from Section [1.2](die-ableitung.html#stufe-1-2), but it is a number: the tangent value $\dot b$ is the rate of change of the node $b$ when you shift the inputs along the line $\mathbf{x}+t\,\dot{\mathbf{x}}$. The formula [(10.1)](#gl-10-1) is the chain rule along this curve, [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4), for a single node. After one pass, the result node holds $\dot f=\nabla f(\mathbf{x})^{\top}\dot{\mathbf{x}}$. If the calculation has several outputs, they hold the product $\mathbf{J}\,\dot{\mathbf{x}}$ of the Jacobian matrix with the direction. With $\dot{\mathbf{x}}=\mathbf{e}_j$, one pass yields the partial derivative with respect to $x_j$, and with several outputs, column $j$ of the Jacobian matrix. For the whole gradient of a function of $n$ variables, forward mode therefore needs $n$ passes.

::::beispiel [Worked example]
For [(9.1)](rechengraphen.html#gl-9-1) at the point $(1,\,2,\,3)$ with the direction $\dot{\mathbf{x}}=\mathbf{e}_2=(0,\,1,\,0)^{\top}$, this gives Table [5](#tab-5). The result node holds $\dot f=8=\partial f/\partial x_2$. For $\partial f/\partial x_1$ and $\partial f/\partial x_3$ you need two more passes with $\mathbf{e}_1$ and $\mathbf{e}_3$.

<span class="anker" id="tab-5"></span>

**Table 5:** Forward mode for $f=(x_1+x_2)\,(x_2+x_3)$ at the point $(1,\,2,\,3)$ in the direction $\dot{\mathbf{x}}=\mathbf{e}_2$.

| Node | Computation | Value | Tangent value |  |
|---|---|---|---|---|
| $x_1$ | input | $1$ | $\dot x_1$ | $0$ |
| $x_2$ | input | $2$ | $\dot x_2$ | $1$ |
| $x_3$ | input | $3$ | $\dot x_3$ | $0$ |
| $v_1$ | $x_1+x_2$ | $3$ | $\dot v_1=\dot x_1+\dot x_2$ | $1$ |
| $v_2$ | $x_2+x_3$ | $5$ | $\dot v_2=\dot x_2+\dot x_3$ | $1$ |
| $f$ | $v_1\cdot v_2$ | $15$ | $\dot f=v_2\,\dot v_1+v_1\,\dot v_2$ | $5+3=8$ |
::::

⁠**In short:** Forward mode carries a tangent value along with every value; one pass yields the derivative in one direction, that is, one column of the Jacobian matrix.

:::hintergrund Forward mode with dual numbers
Forward mode can be viewed as calculating with extended numbers. You calculate with pairs $a+\dot a\,\varepsilon$, where $\varepsilon$ is a new symbol with the single rule $\varepsilon^2=0$; such numbers are called dual numbers. Addition and multiplication work as usual: $(a+\dot a\varepsilon)+(b+\dot b\varepsilon)=(a+b)+(\dot a+\dot b)\varepsilon$ and $(a+\dot a\varepsilon)(b+\dot b\varepsilon)=ab+(a\dot b+\dot ab)\varepsilon$, because the term $\dot a\dot b\varepsilon^2$ drops out. So the factor in front of $\varepsilon$ follows exactly the sum rule and the product rule. For [(9.1)](rechengraphen.html#gl-9-1), you set $x_1=1$, $x_2=2+\varepsilon$, $x_3=3$ and get $(3+\varepsilon)(5+\varepsilon)=15+8\varepsilon+\varepsilon^2=15+8\varepsilon$: value and derivative with respect to $x_2$ in one calculation. For a function $\varphi$ of one variable, you set $\varphi(a+\dot a\varepsilon)=\varphi(a)+\varphi'(a)\,\dot a\,\varepsilon$, which corresponds to the linear approximation, in which the square of the small term plays no role. Dual numbers were introduced by William Kingdon Clifford in 1873, long before any computer.
:::

### Reverse mode

<span class="anker" id="stufe-10-3"></span>

Forward mode asks, for one input, how strongly each node depends on it. Reverse mode asks the opposite question: how strongly does the result depend on each node? This question can be answered backward, starting from the result, and at the end you know the answer for all inputs at once.

:::definition Definition 10.3 (Reverse mode)
<span class="anker" id="satz-10-3"></span>

The __adjoint__ of a node $a$ is $\bar a=\partial f/\partial a$, the derivative of the result with respect to this node when you regard it as an input of the rest of the calculation. In __reverse mode__, you first carry out the forward evaluation and store all values. Then you set $\bar f=1$ and compute the nodes in reverse order,

<span class="anker" id="gl-10-2"></span>
$$\bar a=\sum_{b\text{ successor of }a}\bar b\,\frac{\partial b}{\partial a}. \tag{10.2}$$

The adjoints of the input nodes form the gradient $\nabla f(\mathbf{x})$.
:::

The reverse order is necessary because each node needs the adjoints of its successors, and those come after it in the calculation. Each adjoint has the same shape as its node; if a node is a vector or a matrix, its adjoint is also a vector or a matrix, as with the backward rule of the matrix product in Section [7.6](ableiten-nach-vektoren-und-matrizen.html#stufe-7-6).

:::satz Theorem 10.4 (Reverse mode yields the gradient)
<span class="anker" id="satz-10-4"></span>

For every node $a$, the number $\bar a$ computed by [(10.2)](#gl-10-2) is the sum over all paths from $a$ to the result, with the product of the local derivatives taken along each path. For the input nodes, by Section [9.4](rechengraphen.html#stufe-9-4), this is the partial derivative of $f$.
:::

:::beweis Reverse mode yields the gradient
Group all paths from $a$ to the result by their first edge. Each path begins with an edge to a successor $b$ and then continues as a path from $b$ to the result. The paths that go via $b$ therefore contribute, together, $\frac{\partial b}{\partial a}$ times the sum over all paths from $b$ to the result. If this sum has already been computed correctly for all successors, that is, if it equals $\bar b$, then the sum for $a$ is exactly [(10.2)](#gl-10-2). For the result itself, the statement holds with $\bar f=1$, the empty path. Because you calculate backward, the successors always come before $a$, and the statement carries over node by node all the way to the inputs.
:::

::::beispiel [Worked example]
For [(9.1)](rechengraphen.html#gl-9-1) at the point $(1,\,2,\,3)$, this gives Table [6](#tab-6) and Fig. [19](#abb-19). A single backward pass yields all three partial derivatives $(5,\,8,\,3)$, which forward mode obtained only with three passes.

<span class="anker" id="tab-6"></span>

**Table 6:** Reverse mode for $f=(x_1+x_2)\,(x_2+x_3)$ at the point $(1,\,2,\,3)$; the values come from Table [3](rechengraphen.html#tab-3).

| Node | Computation by [(10.2)](#gl-10-2) | Adjoint |
|---|---|---|
| $f$ | start | $\bar f=1$ |
| $v_2$ | $\bar f\cdot\partial f/\partial v_2=1\cdot v_1$ | $\bar v_2=3$ |
| $v_1$ | $\bar f\cdot\partial f/\partial v_1=1\cdot v_2$ | $\bar v_1=5$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=3$ |
| $x_2$ | $\bar v_1\cdot1+\bar v_2\cdot1$ | $\bar x_2=5+3=8$ |
| $x_1$ | $\bar v_1\cdot1$ | $\bar x_1=5$ |

:::abbildung ml/k3rueckwaerts 19
Forward and backward values in the computational graph of $f=(x_1+x_2)\,(x_2+x_3)$ at the point $(1,\,2,\,3)$: in green the values of the forward evaluation, in red the adjoints, in gray on the edges the local derivatives. In the backward calculation, each adjoint travels against the direction of the arrows and is multiplied by the local derivative of the edge, and where two edges leave a node, as at $x_2$, the contributions are added.
:::
::::

⁠**In short:** Reverse mode first calculates forward and stores all values, then calculates the adjoints $\bar a=\sum\bar b\,\partial b/\partial a$ backward; one backward pass yields the whole gradient.

### Patterns in the backward flow

<span class="anker" id="stufe-10-4"></span>

By Table [4](rechengraphen.html#tab-4), the elementary operations behave in simple, recurring ways in the backward calculation. If you know these patterns, you can write down adjoints almost without calculation and quickly spot mistakes in derivations.

:::satz Theorem 10.5 (Patterns of the elementary operations)
<span class="anker" id="satz-10-5"></span>

<ol class="al">

<li>

An *addition* passes its adjoint on unchanged to each input.

</li>

<li>

A *multiplication* passes on to each input its adjoint times the value of the *other* input.

</li>

<li>

A *maximum* passes its adjoint on entirely to the larger input; the smaller one receives $0$.

</li>

<li>

A function of one variable multiplies the adjoint by its local derivative, so for the logistic function by $b\,(1-b)$.

</li>

<li>

If a node is used several times, the contributions of all its successors *add up*.

</li>

</ol>
:::

Each statement is [(10.2)](#gl-10-2) with the local derivatives from Table [4](rechengraphen.html#tab-4). From (b) follows a useful observation: if one factor is a thousand times as large as the other, the adjoint of the smaller factor is a thousand times as large as that of the larger one. Large differences in the orders of magnitude of the inputs therefore lead to equally large differences in the partial derivatives.

::::beispiel [Worked example]
In Table [6](#tab-6), the multiplication swapped: $v_1$ received $v_2=5$, and $v_2$ received $v_1=3$. The additions passed these values on unchanged, and $x_2$, as a node with two successors, collected $5+3=8$. An example with a maximum: for $f=\max(x_1,x_2)\cdot x_3$ at the point $(1,\,2,\,3)$, $v=\max(1,2)=2$ and $f=6$. Backward, $\bar v=x_3=3$ and $\bar x_3=v=2$; the maximum passes $\bar v$ on to the larger input $x_2$, so $\bar x_2=3$ and $\bar x_1=0$. Indeed, a small change in $x_1$ does not change the result as long as $x_1<x_2$ holds.
::::

⁠**In short:** Addition distributes, multiplication swaps, the maximum passes on, and at branches the contributions add up.

### The cost

<span class="anker" id="stufe-10-5"></span>

Why is reverse mode so important? Because it delivers the gradient of a function with very many inputs almost as cheaply as the function value itself. A comparison of the methods makes this clear.

Forward mode needs $n$ passes for the gradient of a function of $n$ variables, one per input direction. One pass costs a small multiple of one evaluation of $f$, because each elementary operation is accompanied by its tangent value. Difference quotients even need $n+1$ or $2n$ evaluations. Reverse mode, by contrast, always needs exactly one forward evaluation and one backward pass, no matter how large $n$ is. In the backward pass, each edge is used exactly once, with one multiplication and one addition. So it, too, costs only a small multiple of the forward evaluation.

:::satz Theorem 10.6 (Cost of forward and reverse mode)
<span class="anker" id="satz-10-6"></span>

Let $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ be given by a computational graph of elementary operations, and let one evaluation cost the time $T$. Then the whole Jacobian matrix costs about $c\cdot n\cdot T$ in forward mode and about $c\cdot m\cdot T$ in reverse mode. The number $c$ does not depend on $n$ and $m$. If you count each basic arithmetic operation as one step, one can show that function value and gradient together need at most four times as many steps as the function value alone; if you also count the memory accesses, $c$ stays below $6$, and in practice it is often between $2$ and $3$. For a number ($m=1$), the whole gradient in reverse mode therefore costs only a fixed small multiple of one evaluation.
:::

The theorem is proved by counting, for each elementary operation, how many calculation steps its backward step needs relative to the operation itself. A rule of thumb follows: many inputs and one output, as with a number that depends on millions of adjustable knobs, call for reverse mode. Few inputs and many outputs call for forward mode. For the complete Jacobian matrix of a function with many inputs and many outputs, there is no such trick; there, every method costs many passes.

Reverse mode has a price: memory. The backward pass needs all values of the forward evaluation, because the local derivatives are evaluated with them. So you have to keep every intermediate value until the backward pass has gone past it. In long calculations, this memory is often the actual limit.

::::beispiel [Worked example]
Let a function have $n=10^6$ inputs, and let one evaluation take one second. Forward mode needs $10^6$ passes for the gradient, that is, at least $10^6$ seconds, just over $11$ days. Central difference quotients need $2\cdot10^6$ evaluations, just over $23$ days, and are then only approximately correct. Reverse mode needs one forward evaluation and one backward pass, so with $c\approx3$ a few seconds.
::::

⁠**In short:** Reverse mode delivers all $n$ partial derivatives of a number for a small fixed multiple of one evaluation, independent of $n$; it pays for this with the memory for all intermediate values.

:::hintergrund Why reverse mode is so cheap, and where it comes from
The sum over all paths can have very many terms. If you chain ten calculation steps, each of which uses its predecessor twice, for example $v_{k+1}=v_k\cdot v_k$, there are $2^{10}=1024$ paths between input and result, and with $50$ steps more than $10^{15}$. Reverse mode never counts these paths individually. It combines all paths that go through the same node in that node's adjoint and reuses this partial sum for all predecessors. This is the same idea as with the step-by-step product rule in Section [9.1](rechengraphen.html#stufe-9-1): an intermediate result is computed once and then used often. So each edge costs one multiplication and one addition, and the cost grows with the number of edges, not with the number of paths. The memory requirement can be reduced by keeping only some intermediate values and recomputing the others during the backward pass; with a clever distribution, the memory and the factor by which the computing time exceeds that of a plain evaluation then grow only logarithmically with the length of the calculation.

Forward mode was described as a computer program in 1964. Seppo Linnainmaa developed reverse mode in 1970 in his master's thesis at the University of Helsinki, in order to estimate how the rounding errors of all calculation steps affect the result; the sensitivity of the result to each intermediate step is exactly that step's adjoint. A program that automatically generated reverse mode for arbitrary calculations followed in 1980.
:::

### Parenthesization: vector times Jacobian matrix

<span class="anker" id="stufe-10-6"></span>

The difference between the two modes can also be described with matrices. A calculation that consists of stages $\mathbf{g}_1,\dots,\mathbf{g}_L$ and ends with a number has, by [(6.1)](die-kettenregel-fur-mehrere-variablen.html#gl-6-1), the Jacobian matrix

$$\mathbf{J}=\mathbf{J}_L\,\mathbf{J}_{L-1}\cdots\mathbf{J}_1 ,$$

where $\mathbf{J}_L$ is a row because the last stage has only one output. The product is the same however you parenthesize it; by [Chapter 1, Section 9.3](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-3), however, the cost is very different. Reverse mode parenthesizes from the left: $\bigl((\mathbf{J}_L\mathbf{J}_{L-1})\,\mathbf{J}_{L-2}\bigr)\cdots$. Each step multiplies a row by a matrix and again gives a row, the transposed adjoint of the respective stage. Forward mode parenthesizes from the right: $\mathbf{J}_L\bigl(\cdots(\mathbf{J}_2\,(\mathbf{J}_1\dot{\mathbf{x}}))\bigr)$. For a single vector $\dot{\mathbf{x}}$, this is cheap too; for the whole gradient, however, it needs $n$ such vectors, and that is as expensive as fully multiplying out the matrices $\mathbf{J}_2\mathbf{J}_1$, $\mathbf{J}_3\mathbf{J}_2\mathbf{J}_1,\dots$.

A second point comes in addition: the Jacobian matrices are never formed. Each backward step directly computes the product of adjoint and Jacobian matrix, with the rules of the elementary operations. For a matrix–vector product $\mathbf{y}=\mathbf{A}\mathbf{x}$, by [(7.6)](ableiten-nach-vektoren-und-matrizen.html#gl-7-6) this is $\bar{\mathbf{x}}=\mathbf{A}^{\top}\bar{\mathbf{y}}$, without any further matrix; for an elementwise function, by [(5.4)](die-jacobi-matrix.html#gl-5-4) it is the componentwise product with the derivatives, without setting up a diagonal matrix. This is also necessary: if a stage has $10^5$ inputs and $10^5$ outputs, its Jacobian matrix has $10^{10}$ entries, which at eight bytes per number is $80$ gigabytes.

::::beispiel [Worked example]
Let a calculation consist of three stages $\mathbb{R}^{1000}\to\mathbb{R}^{1000}$ and a last stage $\mathbb{R}^{1000}\to\mathbb{R}$. By [Chapter 1, Section 9.3](/wissen/en/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-3), a product of a row and a $1000\times1000$ matrix costs about $2\cdot10^6$ basic arithmetic operations, a product of two such matrices about $2\cdot10^9$. Parenthesized from the left, there are three products of a row and a matrix, together about $6\cdot10^6$. Parenthesized from the right, there are two matrix products and one product of a row and a matrix, together about $4\cdot10^9$, roughly $670$ times as much.
::::

⁠**In short:** Reverse mode multiplies the chain of Jacobian matrices from the left with a row, forward mode from the right with a column; the Jacobian matrices themselves are never formed.

:::aufgabe Exercise 35 ★ Backward through a square
<span class="anker" id="aufg-35"></span>

Let $f=(x_1x_2+x_3)^2$ as in Exercise [32](rechengraphen.html#aufg-32).

<ol class="al">

<li>

At the point $(1,\,2,\,3)$, compute all adjoints in reverse mode, and present them in a table like Table [6](#tab-6).

</li>

<li>

How many passes would forward mode need for the same gradient? Carry out the pass for $\dot{\mathbf{x}}=\mathbf{e}_1$.

</li>

</ol>

:::loesung
(a) With the values from Exercise [32](rechengraphen.html#aufg-32):

| Node | Computation | Adjoint |
|---|---|---|
| $f$ | start | $\bar f=1$ |
| $v_2$ | $\bar f\cdot2v_2$ | $\bar v_2=10$ |
| $v_1$ | $\bar v_2\cdot1$ | $\bar v_1=10$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=10$ |
| $x_2$ | $\bar v_1\cdot x_1$ | $\bar x_2=10$ |
| $x_1$ | $\bar v_1\cdot x_2$ | $\bar x_1=20$ |

(b) Three passes, one per input. With $\dot{\mathbf{x}}=\mathbf{e}_1$: $\dot v_1=x_2\dot x_1+x_1\dot x_2=2$, $\dot v_2=\dot v_1+\dot x_3=2$, $\dot f=2v_2\,\dot v_2=10\cdot2=20=\partial f/\partial x_1$.
:::
:::

:::aufgabe Exercise 36 ★★ The logistic function in the graph
<span class="anker" id="aufg-36"></span>

Let $f(x_1,x_2)=\sigma(2x_1-x_2)$ with the logistic function $\sigma$.

<ol class="al">

<li>

Draw the graph with $v_1=2x_1$, $v_2=v_1-x_2$, $f=\sigma(v_2)$, and calculate forward at the point $(1,\,1)$.

</li>

<li>

Compute all adjoints. Which stored number does the node $\sigma$ need for its local derivative?

</li>

<li>

Verify: $\nabla f(\mathbf{x})=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$.

</li>

</ol>

:::loesung
(a) The graph has the edges $x_1\to v_1$, $v_1\to v_2$, $x_2\to v_2$ and $v_2\to f$. Forward at the point $(1,\,1)$: $v_1=2$, $v_2=1$, $f=\sigma(1)\approx0.7311$.

(b) $\bar f=1$; $\bar v_2=\bar f\cdot f\,(1-f)\approx0.7311\cdot0.2689\approx0.1966$; $\bar v_1=\bar v_2\cdot1\approx0.1966$; $\bar x_2=\bar v_2\cdot(-1)\approx-0.1966$; $\bar x_1=\bar v_1\cdot2\approx0.3932$. For its local derivative, the node $\sigma$ needs only its own stored output $f$, according to Table [4](rechengraphen.html#tab-4).

(c) By the chain rule, $\nabla f=\sigma'(2x_1-x_2)\,\nabla(2x_1-x_2)=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$, so at the point $(1,\,1)$ it is $0.1966\cdot(2,\,-1)^{\top}=(0.3932,\ -0.1966)^{\top}$.
:::
:::

:::aufgabe Exercise 37 ★★ Dual numbers
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

Compute $p(x)=(x+1)(x+2)(x+3)(x+4)$ with the dual number $x=0+1\varepsilon$, and read off $p(0)$ and $p'(0)$.

</li>

<li>

In the same way, compute $(x^2+1)^3$ at the point $x=1+\varepsilon$, and compare with the chain rule.

</li>

</ol>

:::loesung
(a) With $x=\varepsilon$:

$$(1+\varepsilon)(2+\varepsilon)=2+3\varepsilon,\quad (2+3\varepsilon)(3+\varepsilon)=6+11\varepsilon,\quad (6+11\varepsilon)(4+\varepsilon)=24+50\varepsilon .$$

So $p(0)=24$ and $p'(0)=50$; the coefficients of $\varepsilon$ are exactly the $p_k'$ from the worked example in Section [9.1](rechengraphen.html#stufe-9-1).

(b) $(1+\varepsilon)^2=1+2\varepsilon$, plus $1$ gives $2+2\varepsilon$; $(2+2\varepsilon)^2=4+8\varepsilon$ and $(4+8\varepsilon)(2+2\varepsilon)=8+24\varepsilon$. The chain rule gives $3\,(x^2+1)^2\cdot2x=3\cdot4\cdot2=24$ at the point $1$.
:::
:::

:::aufgabe Exercise 38 ★★★ Which mode?
<span class="anker" id="aufg-38"></span>

<ol class="al">

<li>

One calculation has $3$ inputs and $1000$ outputs, another has $1000$ inputs and $3$ outputs. How many passes do forward mode and reverse mode each need for the whole Jacobian matrix?

</li>

<li>

Let $f(\mathbf{x})=\mathbf{c}^{\top}\mathbf{B}\mathbf{x}$ with a dense matrix $\mathbf{B}\in\mathbb{R}^{n\times n}$, computed in two stages $\mathbf{y}=\mathbf{B}\mathbf{x}$ and $f=\mathbf{c}^{\top}\mathbf{y}$. A forward pass computes $\mathbf{c}^{\top}(\mathbf{B}\dot{\mathbf{x}})$, a backward pass $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$. For both approaches, count the basic arithmetic operations that the whole gradient costs if a matrix–vector product costs about $2n^2$ and a dot product about $2n$.

</li>

<li>

Why does reverse mode need more memory than forward mode? Which values may forward mode forget immediately?

</li>

</ol>

:::loesung
(a) With $3$ inputs and $1000$ outputs, forward mode needs $3$ passes and reverse mode $1000$; you take forward mode. With $1000$ inputs and $3$ outputs, it is the other way round: $1000$ forward passes versus $3$ backward passes.

(b) In forward mode, the gradient needs $n$ passes with $\dot{\mathbf{x}}=\mathbf{e}_1,\dots,\mathbf{e}_n$, each with a matrix–vector product $\mathbf{B}\dot{\mathbf{x}}$ and a dot product, together about $n\,(2n^2+2n)\approx2n^3$ basic arithmetic operations. In reverse mode, $\bar{\mathbf{y}}=\mathbf{c}$, and $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$ costs one matrix–vector product, about $2n^2$; on top of that comes the forward evaluation with about $2n^2+2n$. Reverse mode is therefore about $n/2$ times as fast.

(c) The backward pass needs the values of the forward evaluation in order to evaluate the local derivatives, and it starts only after the forward evaluation has finished. All intermediate values must therefore be kept until then. In forward mode, value and tangent value run forward together; neither is needed any longer once all successors of the node have been computed, and both may then be forgotten.
:::
:::
