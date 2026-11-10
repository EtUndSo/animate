---
title: Key points
pfad: Electrical Engineering / 1st Semester / HöMa1 – Higher Mathematics 1 / Functions and Polynomials
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Chapter 3: Functions and Polynomials
order: 1231200
summary: When an equation can be solved backward and why every zero splits off a factor
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

A function is an assignment that gives each element of its domain (the set of admissible inputs) exactly one image. A formula is only one way of specifying it.

</li>

<li>

The equation $f(x)=y$ has exactly one solution for every $y$ if $f$ is bijective, that is, if no $y$ is hit twice and none is missed. Then the inverse function $f^{-1}$ exists, and its graph (the picture of the assignment in the plane) is the graph of $f$ reflected in $y=x$.

</li>

<li>

A polynomial is determined by its coefficients (the fixed numbers in front of the powers). Dividing it by $x-x_0$ leaves the remainder $P(x_0)$. Therefore every zero splits off a linear factor, and a polynomial of degree $n$ has at most $n$ zeros.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Function $f:A\to B$: exactly one image for each $a\in A$. $\mathcal D(f)=A$, $\mathcal W(f)\subset B$, $\mathcal G(f)=\{(a,f(a))\}$.

</li>

<li>

Even: $f(x)=f(-x)$, odd: $f(x)=-f(-x)$. Strictly increasing: $x<y\Rightarrow f(x)<f(y)$. Bounded: $|f|\le K$.

</li>

<li>

Injective: at most, surjective: at least, bijective: exactly one solution of $f(x)=y$. Strictly monotonic implies bijective onto $\mathcal W(f)$.

</li>

<li>

$(g\circ f)(x)=g(f(x))$. Injective: There is $g$ with $g(f(x))=x$. Surjective: There is $g$ with $f(g(y))=y$. Bijective: Exactly one $g=f^{-1}$ does both.

</li>

<li>

$f(x)=y\Leftrightarrow x=f^{-1}(y)$. Graph: reflection in $y=x$. $f^{-1}(y)\neq1/f(y)$. Monotonicity is inherited.

</li>

<li>

Polynomial $\sum_{i=0}^na_ix^i$, $a_n\neq0$. Equal for all $x$ $\Leftrightarrow$ equal coefficients.

</li>

<li>

Division: $P_n=S_{n-m}Q_m+T_k$ with $k<m$ or $T_k=0$.

</li>

<li>

Horner: $c_n=a_n$, $c_i=c_{i+1}x_0+a_i$; $c_0=P_n(x_0)$; $P_n(x)=(x-x_0)Q_{n-1}(x)+c_0$.

</li>

<li>

$P_n(x_0)=0\Leftrightarrow$ factor $x-x_0$; at most $n$ zeros. $m$-fold: $(x-x_0)^mQ_{n-m}$, $Q_{n-m}(x_0)\neq0$; odd $m$ crosses, even $m$ touches.

</li>

<li>

Pole: denominator zero, numerator not after canceling. Gap: The factor cancels. For large $|x|$, $R\approx S$.

</li>

</ul>
:::

**Looking ahead to Chapter 4.** “Growing beyond every bound” and “approaching” have remained descriptions here. Chapter 4 turns them into the limit, first for sequences.

**One principle behind all the results.** A function gives exactly one $y$ for each $x$. Almost everything in this chapter asks the reverse question: How many $x$ belong to a given $y$?

| Result | Where it comes from |
|---|---|
| Function, graph, range | Exactly one output per input; the $y$ that are reached form the range (Stage [1](was-eine-funktion-ist.html#stufe-1)) |
| even, odd, monotonic, bounded | These properties tell how $f(x)$ changes with $x$ without computing every value (Stage [2](gerade-monoton-beschrankt.html#stufe-2)) |
| injective, surjective, bijective | At most, at least, or exactly one solution of $f(x)=y$ (Stage [3](ruckwarts-injektiv-surjektiv-bijektiv.html#stufe-3)) |
| Inverse function, root | Exactly one solution for every $y$: This solution is itself a function of $y$ (Stage [4](verknupfen-und-umkehren.html#stufe-4)) |
| Comparing coefficients | The same function means the same coefficients; near $x=0$ each one becomes visible separately (Stage [5](polynome-und-koeffizienten.html#stufe-5)) |
| Division with remainder | The highest power is subtracted, the degree drops (Stage [6](division-mit-rest.html#stufe-6)) |
| Horner scheme | Factoring out $x$ saves multiplications and delivers the quotient along the way (Stage [7](das-horner-schema.html#stufe-7)) |
| Linear factor, multiplicity | The remainder of the division by $x-x_0$ is the value $P(x_0)$ (Stage [8](jede-nullstelle-spaltet-einen-linearfaktor-ab.html#stufe-8)) |
| Pole, gap, asymptote | Dividing by almost zero makes $\vert R\vert $ large; for large $\vert x\vert $ the polynomial part remains (Stage [9](rationale-funktionen-und-pole.html#stufe-9)) |
