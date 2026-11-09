---
title: Stage 5: Mathematical induction, sum and product
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Sets, Logic and Real Numbers
order: 1210700
summary: Statements about all ninmathbb N cannot be proved by trial.
tags: base case, induction step, induction hypothesis, induction conclusion
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Statements about all $n\in\mathbb{N}$ cannot be proved by trial. This stage provides the method and with it a clean definition of sum, product and power.
:::

**The idea.** Every natural number arises from 1 by repeated counting on. If you show a statement for 1 and show that it carries over from every $n$ to $n+1$, the chain reaches every number (Fig. [5](#abb-5)).

:::satz Theorem 5.1 (Mathematical induction)
<span class="anker" id="satz-5-1"></span>

Let $\mathcal A(n)$ be statements with $n\in\mathbb{N}$. If (1) $\mathcal A(1)$ is true (__base case__) and (2) for arbitrary $n$ the implication $\mathcal A(n)\Rightarrow\mathcal A(n+1)$ is true (__induction step__, $\mathcal A(n)$ is called the __induction hypothesis__), then $\mathcal A(n)$ is true for all $n\in\mathbb{N}$ (__induction conclusion__).

⁠**Second version:** Let $n_0\in\mathbb{N}$ be fixed. If $\mathcal A(n_0)$ is true and for every $n\ge n_0$

$$\bigl(\mathcal A(n_0)\wedge\mathcal A(n_0+1)\wedge\dots\wedge\mathcal A(n)\bigr)\Rightarrow\mathcal A(n+1),$$

then $\mathcal A(n)$ is true for all $n\ge n_0$.
:::

⁠**How to read it:** The second version allows a later start and all earlier cases as hypothesis. **Why both parts:** Without a base case: $\mathcal A(n):=(n=n+1)$ has a valid step (add 1 on both sides) but is always false. Without a step: $n^2-n+41$ is prime for $n=1,\dots,40$, but for $n=41$ it is $41^2$.

:::frage Doesn't the step assume what is to be proved?
No. You assume $\mathcal A(n)$ for an arbitrary but fixed $n$ and show only the implication $\mathcal A(n)\Rightarrow\mathcal A(n+1)$. That $\mathcal A(n)$ is true follows only from the base case and the chain.
:::

:::beweis Why induction works
$\mathbb{N}$ has this property: If $M\subset\mathbb{N}$ with $1\in M$ and $n\in M$ always implies $n+1\in M$, then $M=\mathbb{N}$. That is the construction of $\mathbb{N}$ itself. Set $M:=\{n\in\mathbb{N}:\mathcal A(n)\text{ true}\}$. For the second version let $\mathcal B(n):=\mathcal A(n_0)\wedge\dots\wedge\mathcal A(n)$. Then the hypothesis gives $\mathcal B(n)\Rightarrow\mathcal B(n+1)$, and the same property of $\mathbb{N}$, started at $n_0$, gives $\mathcal B(n)$ for all $n\ge n_0$.
:::

:::definition Definition 5.2 (Sum, product, power: recursive)
<span class="anker" id="satz-5-2"></span>

For $x_1,x_2,\ldots\in\mathbb K$ one sets

<span class="anker" id="gl-5-1"></span>
$$\sum_{i=1}^{1}x_i:=x_1,\quad\sum_{i=1}^{n+1}x_i:=\Bigl(\sum_{i=1}^{n}x_i\Bigr)+x_{n+1},\qquad \prod_{i=1}^{1}x_i:=x_1,\quad\prod_{i=1}^{n+1}x_i:=\Bigl(\prod_{i=1}^{n}x_i\Bigr)\cdot x_{n+1}. \tag{5.1}$$

If all $x_i=x$, then $x^n:=\prod_{i=1}^nx$. For $x\ne0$ and $n\in\mathbb{N}$ one sets $x^0:=1$ and $x^{-n}:=(x^n)^{-1}=(\frac1x)^n$. Also $n!:=\prod_{i=1}^ni$ and $0^0:=1$.
:::

⁠**How to read it:** $\sum_{i=1}^nx_i=x_1+\dots+x_n$; the dots are now explained by the recursion, and by Theorem [5.1](#satz-5-1) the value is fixed for every $n$. $x^0:=1$ is forced because $x^n\cdot x^0=x^{n+0}$ is supposed to hold. $0^0:=1$ is a convention: With it, $x^0=1$ extends to $x=0$, and $(x+y)^2=x^2y^0+2x^1y^1+x^0y^2$ stays correct for $x=0$ or $y=0$.

:::satz Theorem 5.3 (Rules for sum, product, power)
<span class="anker" id="satz-5-3"></span>

In every field:

<ol class="rm">

<li>

The value of $\sum_{i=1}^nx_i$ and $\prod_{i=1}^nx_i$ does not depend on the order of the $x_i$.

</li>

<li>

Product of sums: $\Bigl(\sum_{i=1}^nx_i\Bigr)\Bigl(\sum_{j=1}^Ny_j\Bigr)=\sum_{i=1}^n\Bigl(\sum_{j=1}^Nx_iy_j\Bigr)$.

</li>

<li>

Power laws for $x,y\ne0$, $p,q\in\mathbb{Z}$: $x^px^q=x^{p+q}$, $(x^p)^q=x^{p\cdot q}$, $(xy)^p=x^py^p$.

</li>

</ol>
:::

⁠**How to read it:** (i) is induction over (A1), (A2), (M1), (M2). (ii) says “each with each”; that is (AM) repeated. For $p,q\in\mathbb{N}$, (iii) is renumbering: $x^px^q=\prod_{i=1}^{p+q}x=x^{p+q}$. **Why $x\ne0$:** $0^{-1}$ does not exist; for $x=0$ only exponents $n\ge0$ are allowed, and $0^n=0$ for $n\ge1$. For $x,y>0$ the laws also hold with rational exponents, for example $x^{1/2}=\sqrt x$ (Part 5).

:::abbildung hm1/k1induktion 5
Left, each color is an L-shaped piece. Right, the induction step: $n^2$ grows by $2n+1$ squares.
:::

::::beispiel [Example 1] Sum of the odd numbers
Claim: $\sum_{i=1}^n(2i-1)=n^2$. **Base case:** $2\cdot1-1=1=1^2$. **Step:** If the formula holds for $n$, then $\sum_{i=1}^{n+1}(2i-1)=n^2+2(n+1)-1=n^2+2n+1=(n+1)^2$. **Conclusion:** It holds for all $n$. In the same way one proves $\sum_{i=1}^ni=\frac{n(n+1)}2$ and $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$ (Exercise [6](#aufg-6)).
::::

::::beispiel [Example 2] late start
$n!>2^n$ for $n\ge n_0=4$. Base case: $24>16$. Step: $(n+1)!=(n+1)\,n!>(n+1)\,2^n\ge2\cdot2^n$, because $n+1\ge2$.
::::

⁠**Limiting case:** For $n=3$, $6<8$; the start at 4 is necessary.

::::beispiel [Example 3] all earlier cases
Every $n\ge2$ is a product of primes. Base case: 2 is prime. Step: If $n+1$ is not prime, then $n+1=ab$ with $2\le a,b\le n$. Here $\mathcal A(n)$ alone is not enough; you need $\mathcal A(a)$ and $\mathcal A(b)$.
::::

:::aufgabe Exercise 6 ★★ Practicing induction
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Prove $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$ and check $n=3$.

</li>

<li>

Calculate $\prod_{i=1}^5(1+\frac1i)$. Predict the formula for $\prod_{i=1}^n(1+\frac1i)$ and prove it.

</li>

<li>

Find the error: “All cables have the same color. Base case: One cable has one color. Step: From $n+1$ cables take one away; the remaining $n$ have the same color. Take a different one away, likewise. So all have the same color.”

</li>

</ol>

:::loesung
(a) Base case: $1=\frac{1\cdot4}4$. Step: $\frac{n^2(n+1)^2}4+(n+1)^3=\frac{(n+1)^2(n^2+4n+4)}4=\frac{(n+1)^2(n+2)^2}4$. Check: $1+8+27=36=\frac{9\cdot16}4$. (b) $2\cdot\frac32\cdot\frac43\cdot\frac54\cdot\frac65=6$. Conjecture: $n+1$. Base case: $1+\frac11=2$. Step: $(n+1)(1+\frac1{n+1})=n+2$. (c) The step fails at $n=1$: Of two cables, taking one away leaves a different one each time, and the remainders have no cable in common. The step must hold for every $n$.
:::
:::
