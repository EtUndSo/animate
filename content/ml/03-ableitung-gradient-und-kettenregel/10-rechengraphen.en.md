---
title: Computational graphs
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15231000
summary: A computer evaluates long formulas step by step, and each step is a simple operation with a known derivative.
tags: computational graph, forward evaluation, local derivative
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
A computer evaluates long formulas step by step, and each step is a simple operation with a known derivative. A computational graph makes these steps and their dependencies visible. This section draws such a graph, evaluates it forward as a table and writes its local derivative on each edge. With that, everything is prepared to compute the derivatives of the result with respect to all inputs mechanically.
:::

### Intermediate results

<span class="anker" id="stufe-9-1"></span>

With the rules from Section [1.4](die-ableitung.html#stufe-1-4), you can differentiate any formula that consists of basic arithmetic operations and known functions. If you write out the result as a formula, however, it often becomes much longer than the function itself. By the product rule, a product of $n$ factors has a derivative consisting of $n$ terms with $n$ factors each; so the formula grows with $n^2$, while the function has only $n$ factors. With intermediate results, by contrast, the calculation stays small. After each step, you keep the current value and the current derivative and continue calculating with numbers, not with formulas.

::::beispiel [Worked example]
Let $p(x)=(x+1)(x+2)(x+3)(x+4)$; we are looking for $p'(0)$. The written-out product rule gives four terms, in each of which one factor is replaced by its derivative $1$:

$$p'(0)=2\cdot3\cdot4+1\cdot3\cdot4+1\cdot2\cdot4+1\cdot2\cdot3=24+12+8+6=50$$

(Fig. [17](#abb-17)). Step by step, with the partial products $p_1=x+1$, $p_k=p_{k-1}\cdot(x+k)$ and the product rule $p_k'=p_{k-1}'\cdot(x+k)+p_{k-1}\cdot1$, it goes like this:

$$\begin{gathered} p_1=1,\quad p_1'=1;\qquad p_2=1\cdot2=2,\quad p_2'=1\cdot2+1\cdot1=3;\\ p_3=2\cdot3=6,\quad p_3'=3\cdot3+2\cdot1=11;\qquad p_4=6\cdot4=24,\quad p_4'=11\cdot4+6\cdot1=50 . \end{gathered}$$

Each step costs two multiplications and one addition, no matter how many factors have already been processed.

:::abbildung ml/k3rvierfaktoren 17
The written-out product rule for $p(x)=(x+1)(x+2)(x+3)(x+4)$ at the point $0$: in term $k$, the factor $x+k$ is replaced by its derivative $1$.
:::
::::

⁠**In short:** Written-out derivative formulas quickly become much longer than the function; with intermediate results stored as numbers, the cost per step stays small.

### The computational graph

<span class="anker" id="stufe-9-2"></span>

Which intermediate results a calculation has and what each of them depends on is shown most clearly by a picture made of nodes and arrows. An arrow from a node $a$ to a node $b$ means: $a$ is needed to compute $b$.

:::definition Definition 9.1 (Computational graph)
<span class="anker" id="satz-9-1"></span>

A __computational graph__ consists of nodes and directed edges, that is, arrows between nodes. Each node stands for a number or, in larger calculations, for a whole vector or a matrix. The input nodes are the inputs of the calculation; every other node $v$ arises by an elementary operation from the nodes from which an edge leads to $v$. These are called the predecessors of $v$, and $v$ is called their successor. If you follow the edges, you never return to a node you have already visited; such a graph is called acyclic. One distinguished node is the result.
:::

Elementary operations are the basic arithmetic operations and functions of one variable such as the square, the exponential function or the logistic function. Because the graph is acyclic, you can always arrange the nodes so that each node comes after its predecessors; you calculate in this order. A program with loops and branches also yields such a graph for specific input values: a loop that runs three times produces the same nodes three times in a row.

::::beispiel [Worked example]
The example of this section and the next is

<span class="anker" id="gl-9-1"></span>
$$f(x_1,x_2,x_3)=(x_1+x_2)\,(x_2+x_3) \tag{9.1}$$

with the intermediate results $v_1=x_1+x_2$ and $v_2=x_2+x_3$ and the result $f=v_1\cdot v_2$. The graph has three input nodes, two addition nodes and one multiplication node, connected by six edges (Fig. [18](#abb-18)). The input $x_2$ has two successors; the graph branches there.

:::abbildung ml/k3graph 18
The computational graph of $f=(x_1+x_2)\,(x_2+x_3)$. The arrows point in the direction of calculation; the circles contain the elementary operation. The values of the forward evaluation at the point $(1,\,2,\,3)$ are shown in green.
:::
::::

⁠**In short:** A computational graph breaks a calculation down into elementary operations; its edges show which value enters which other one, and because it is acyclic, there is always an order in which you can evaluate it.

### The forward evaluation

<span class="anker" id="stufe-9-3"></span>

Evaluating a computational graph means computing the nodes in an order in which each node comes after its predecessors. If you write the steps one below the other, you get a table that you also need for the derivatives: all values are stored, not just the result.

:::definition Definition 9.2 (Forward evaluation)
<span class="anker" id="satz-9-2"></span>

The __forward evaluation__ of a computational graph computes all nodes in an order in which each node comes after its predecessors, and it stores every value.
:::

::::beispiel [Worked example]
For [(9.1)](#gl-9-1) at the point $(1,\,2,\,3)$, this gives Table [3](#tab-3).

<span class="anker" id="tab-3"></span>

**Table 3:** The forward evaluation for $f=(x_1+x_2)\,(x_2+x_3)$ at the point $(1,\,2,\,3)$.

| Node | Computation | Value |
|---|---|---|
| $x_1$ | input | $1$ |
| $x_2$ | input | $2$ |
| $x_3$ | input | $3$ |
| $v_1$ | $x_1+x_2$ | $3$ |
| $v_2$ | $x_2+x_3$ | $5$ |
| $f$ | $v_1\cdot v_2$ | $15$ |
::::

⁠**In short:** The forward evaluation evaluates the graph node by node and stores every intermediate value.

### Local derivatives

<span class="anker" id="stufe-9-4"></span>

Each edge connects a node with a successor that arises from it by an elementary operation. How strongly the successor responds to a small change in this one predecessor is an ordinary partial derivative of the elementary operation.

:::definition Definition 9.3 (Local derivative)
<span class="anker" id="satz-9-3"></span>

For an edge from $a$ to $b$, the partial derivative $\partial b/\partial a$ of the elementary operation that computes $b$, taken with respect to its input $a$, is called the __local derivative__ of the edge. It is evaluated with the stored values of the forward evaluation.
:::

For the elementary operations, the local derivatives are simple (Table [4](#tab-4)). It is remarkable how little they need: for the exponential function and the logistic function, the stored value of the successor itself suffices. The max node has a kink when both inputs are equal; there you use one of the two one-sided values.

<span class="anker" id="tab-4"></span>

**Table 4:** Local derivatives of the elementary operations, expressed by stored values.

| Operation | local derivatives | values needed |
|---|---|---|
| $b=a_1+a_2$ | $\partial b/\partial a_1=1$, $\ \partial b/\partial a_2=1$ | none |
| $b=a_1\cdot a_2$ | $\partial b/\partial a_1=a_2$, $\ \partial b/\partial a_2=a_1$ | the inputs |
| $b=a^2$ | $\partial b/\partial a=2a$ | the input |
| $b=\mathrm{e}^a$ | $\partial b/\partial a=\mathrm{e}^a=b$ | the output |
| $b=\sigma(a)$ | $\partial b/\partial a=b\,(1-b)$ | the output |
| $b=\max(a_1,a_2)$ | $1$ for the larger input, $0$ for the other | which one is larger |

With the local derivatives, the chain rule from Section [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2) becomes a pure counting exercise: the derivative of the result with respect to an input is the sum over all paths from the input to the result, and along each path you multiply the local derivatives of its edges.

::::beispiel [Worked example]
In the graph of Fig. [18](#abb-18), the four edges from the inputs to the addition nodes have the local derivative $1$. The edge from $v_1$ to the result has $\partial f/\partial v_1=v_2=5$, the one from $v_2$ has $\partial f/\partial v_2=v_1=3$. One path leads from $x_1$ to the result, one from $x_3$ as well, and two from $x_2$. So

$$\frac{\partial f}{\partial x_1}=1\cdot5=5,\qquad \frac{\partial f}{\partial x_2}=1\cdot5+1\cdot3=8,\qquad \frac{\partial f}{\partial x_3}=1\cdot3=3 .$$

Check: multiplied out, $f=x_1x_2+x_1x_3+x_2^2+x_2x_3$ with the partial derivatives $x_2+x_3=5$, $x_1+2x_2+x_3=8$ and $x_1+x_2=3$.
::::

⁠**In short:** Each edge carries the local derivative of its elementary operation, evaluated with the stored values; the derivative of the result is the sum, over all paths, of the products of these numbers.

:::aufgabe Exercise 32 ★ A graph with a square
<span class="anker" id="aufg-32"></span>

Let $f(x_1,x_2,x_3)=(x_1x_2+x_3)^2$.

<ol class="al">

<li>

Draw the computational graph with the intermediate results $v_1=x_1x_2$, $v_2=v_1+x_3$ and $f=v_2^2$.

</li>

<li>

Set up the table of the forward evaluation at the point $(1,\,2,\,3)$, and write its local derivative on each edge.

</li>

<li>

Compute all three partial derivatives as sums over the paths, and check the results.

</li>

</ol>

:::loesung
(a) Inputs $x_1,x_2,x_3$; a multiplication node $v_1$ with edges from $x_1$ and $x_2$; an addition node $v_2$ with edges from $v_1$ and $x_3$; a square node $f$ with an edge from $v_2$.

(b) Forward: $x_1=1$, $x_2=2$, $x_3=3$, $v_1=2$, $v_2=5$, $f=25$. Local derivatives: $\partial v_1/\partial x_1=x_2=2$, $\partial v_1/\partial x_2=x_1=1$, $\partial v_2/\partial v_1=1$, $\partial v_2/\partial x_3=1$, $\partial f/\partial v_2=2v_2=10$.

(c) From each input, exactly one path leads to the result:

$$\frac{\partial f}{\partial x_1}=2\cdot1\cdot10=20,\qquad \frac{\partial f}{\partial x_2}=1\cdot1\cdot10=10,\qquad \frac{\partial f}{\partial x_3}=1\cdot10=10 .$$

Check: $\partial_1f=2\,(x_1x_2+x_3)\,x_2=20$, $\partial_2f=2\,(x_1x_2+x_3)\,x_1=10$, $\partial_3f=2\,(x_1x_2+x_3)=10$.
:::
:::

:::aufgabe Exercise 33 ★★ Five factors
<span class="anker" id="aufg-33"></span>

Let $p(x)=(x+1)(x+2)(x+3)(x+4)(x+5)$.

<ol class="al">

<li>

Compute $p'(1)$ step by step with partial products, as in the worked example in Section [9.1](#stufe-9-1).

</li>

<li>

How many multiplications does the written-out product rule need, and how many the step-by-step calculation? How do both grow with the number $n$ of factors?

</li>

</ol>

:::loesung
(a) At the point $1$, the factors are $2,3,4,5,6$. Step by step:

$$\begin{aligned} p_1&=2, & p_1'&=1,\\ p_2&=2\cdot3=6, & p_2'&=1\cdot3+2\cdot1=5,\\ p_3&=6\cdot4=24, & p_3'&=5\cdot4+6\cdot1=26,\\ p_4&=24\cdot5=120, & p_4'&=26\cdot5+24\cdot1=154,\\ p_5&=120\cdot6=720, & p_5'&=154\cdot6+120\cdot1=1044 . \end{aligned}$$

So $p'(1)=1044$. Check: $p'(1)=p(1)\bigl(\tfrac12+\tfrac13+\tfrac14+\tfrac15+\tfrac16\bigr)=720\cdot\tfrac{87}{60}=1044$.

(b) Written out, the product rule has $n$ terms with $n-1$ factors each, so $n\,(n-2)$ multiplications; for $n=5$, that is $15$. Step by step, each of the $n-1$ steps needs two multiplications, so $8$ for $n=5$. The written-out formula grows with $n^2$, the step-by-step calculation with $n$.
:::
:::

:::aufgabe Exercise 34 ★★ A loop as a graph
<span class="anker" id="aufg-34"></span>

A program sets $y=x$ and then squares $y$ three times in a row.

<ol class="al">

<li>

Draw the computational graph and give the function $y(x)$.

</li>

<li>

At the point $x=2$, compute all intermediate values and the local derivatives, and from them $y'(2)$. Compare with the derivative of the formula from (a).

</li>

</ol>

:::loesung
(a) The graph is a chain $x\to y_1\to y_2\to y_3$ of three square nodes, $y_k=y_{k-1}^2$. Then $y=((x^2)^2)^2=x^8$.

(b) At the point $2$: $y_1=4$, $y_2=16$, $y_3=256$. The local derivatives are $2\cdot2=4$, $2\cdot4=8$ and $2\cdot16=32$, and their product is $4\cdot8\cdot32=1024$. The formula gives $8x^7=8\cdot128=1024$.
:::
:::
