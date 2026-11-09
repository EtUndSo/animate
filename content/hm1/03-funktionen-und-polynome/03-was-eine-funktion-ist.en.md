---
title: Stage 1: What a function is
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Functions and Polynomials
order: 1230300
summary: School presents functions as formulas.
tags: map, image, preimage, domain, range, graph, real function
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
School presents functions as formulas. That is not enough: A measured relationship has no formula, and the same formula can belong to different functions. This stage says what a function is.
:::

**The idea.** A function fixes exactly one output for each admissible input (Fig. [1](#abb-1)). It is the list of these pairs of input and output; the formula is only a short way of giving the list. Two inputs may share one output; in the reference model $h(0)=h(4)=3$. But one input may not have two outputs, and it may not be left without an output. Otherwise $f(x)$ would not be a definite number, and you could not calculate with it.

:::abbildung hm1/k3zuordnung 1
Left, a function: Every element of $A$ has exactly one arrow, two arrows may end in the same image, and something may be left over in $B$. Center and right, not functions: One element has two images, or one has none.
:::

:::definition Definition 1.1 (Function)
<span class="anker" id="satz-1-1"></span>

Let $A$, $B$ be sets ($A=B$ is possible). A function or __map__ $f:A\to B$ is a rule that assigns to every $a\in A$ a unique $b\in B$:

<span class="anker" id="gl-1-1"></span>
$$f:\begin{cases}A\longrightarrow B\\ a\longmapsto b=:f(a).\end{cases} \tag{1.1}$$

$b$ is called the __image__ of $a$, $a$ is called a __preimage__ of $b$. Further,

<span class="anker" id="gl-1-2"></span>
$$\mathcal D(f):=A,\quad\mathcal W(f):=\{b\in B:\text{there is }a\in A\text{ with }f(a)=b\},\quad\mathcal G(f):=\{(a,f(a)):a\in A\} \tag{1.2}$$

are called the __domain__, the __range__ and the __graph__ of $f$; here $\mathcal G(f)\subset A\times B$. For $A,B\subset\mathbb{R}$, $f$ is called a __real function__. Two functions are equal if their graphs are equal: $f=g:\Leftrightarrow\mathcal G(f)=\mathcal G(g)$.
:::

⁠**How to read it:** The arrow $\to$ connects sets, $\mapsto$ connects elements, and $=:$ means “is called this.” $B$ is only a reservoir; $\mathcal W(f)\subset B$ holds. Since $\mathcal W(f)$ is often unknown, for real functions one usually writes $f:\mathcal D(f)\to\mathbb{R}$. Equal graphs also mean equal domains: $\sqrt x$ on $[0,10]$ and $\sqrt x$ on $\mathbb{R}_0^+$ have the same formula and are different functions.

::::beispiel [Examples]
The parabola reaches only $y\ge-1$: A square is never negative, so $h(x)=(x-2)^2-1\ge-1$, and every $y\ge-1$ is hit by $x=2+\sqrt{y+1}$. For the bell, $1+x^2\ge1$, so $0<b(x)\le1$.

| Function | $\mathcal D(f)$ | $\mathcal W(f)$ |
|---|---|---|
| linear: $f(x)=ax+b$ with $a\neq0$ | $\mathbb{R}$ | $\mathbb{R}$ |
| Parabola $h$ | $\mathbb{R}$ | $[-1,\infty)$ |
| Bell $b$ | $\mathbb{R}$ | $(0,1]$ |
| Root: $f(x)=\sqrt x$ | $\mathbb{R}_0^+$ | $\mathbb{R}_0^+$ |
| Absolute value: $f(x)=x$ for $x\ge0$, $f(x)=-x$ for $x<0$ | $\mathbb{R}$ | $\mathbb{R}_0^+$ |
| Length of a vector: $f(\vec x)=\sqrt{x_1^2+\dots+x_n^2}$ | $\mathbb{R}^n$ | $\mathbb{R}_0^+$ |

The absolute value shows: A function may be defined piecewise. The last row shows: Inputs need not be numbers; this function is not real.
::::

⁠**Limiting case:** For $a=0$, $f(x)=b$ is constant, and all inputs share one output. That is allowed, $\mathcal W(f)=\{b\}$.

**Not every set of pairs is a graph.** The unit circle $\{(x,y)\in\mathbb{R}^2:x^2+y^2=1\}$ contains $(0,1)$ and $(0,-1)$: The input $0$ would have two outputs. In the picture this means: A vertical line meets a graph at most once (Fig. [2](#abb-2)).

:::abbildung hm1/k3graph 2
Left, the graph of the parabola $h$. Every vertical line meets it exactly once; the range is marked on the $y$-axis. Right, the unit circle: The vertical line at $x=0.6$ meets it twice, so it is not a graph.
:::

:::frage Aren't $f(x)=x$ and $g(x)=x^2/x$ the same function?
For every $x\neq0$ they give the same value, that is true. But $g(0)$ would be $0/0$ and is not defined, so $\mathcal D(g)=\mathbb{R}\setminus\{0\}$, and the graphs differ by the point $(0,0)$. Stage [9](rationale-funktionen-und-pole.html#stufe-9) calls this a gap.
:::

:::aufgabe Exercise 1 ★ Domain, range, graph
<span class="anker" id="aufg-1"></span>

(a) Determine the largest possible domain in $\mathbb{R}$ and the range of $f(x)=\sqrt{9-x^2}$ and $g(x)=|x-1|+2$. (b) Is $M_1=\{(x,y)\in\mathbb{R}^2:x=y^2\}$ the graph of a function of $x$? And $M_2=\{(x,y)\in\mathbb{R}^2:x=y^3\}$?

:::loesung
(a) We need $9-x^2\ge0$, so $\mathcal D(f)=[-3,3]$. Largest value 3 at $x=0$, smallest 0 at $x=\pm3$: $\mathcal W(f)=[0,3]$. For $g$, $\mathcal D(g)=\mathbb{R}$, and because $|x-1|\ge0$, then $\mathcal W(g)=[2,\infty)$. (b) $M_1$ is not: $(4,2)$ and $(4,-2)$ lie in it, and for $x<0$ there is no $y$. $M_2$ is: For every $x\in\mathbb{R}$ there is exactly one $y=\sqrt[3]{x}$.
:::
:::
