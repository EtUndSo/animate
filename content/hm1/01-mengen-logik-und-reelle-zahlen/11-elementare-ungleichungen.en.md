---
title: Stage 9: Elementary inequalities
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Sets, Logic and Real Numbers
order: 1211100
summary: Often an expression cannot be calculated, only estimated.
tags: Bernoulli, Young, Means, geometric mean, arithmetic mean, Cauchy-Schwarz, Minkowski, vector
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
Often an expression cannot be calculated, only estimated. This stage provides the five standard estimates.
:::

**The idea.** Almost everything follows from one fact: A square is not negative. Writing out $(a-b)^2\ge0$ gives $2ab\le a^2+b^2$. Young, the means and Cauchy-Schwarz are this line, cleverly rewritten. Only Bernoulli needs induction.

:::satz Theorem 9.1 (Five inequalities)
<span class="anker" id="satz-9-1"></span>

In $\mathbb{R}$:

<ol class="rm">

<li>

__Bernoulli__: For $x>-1$, $x\ne0$ and $n\ge2$, $(1+x)^n>1+nx$.

</li>

<li>

__Young__: For $\varepsilon>0$ and $x,y\in\mathbb{R}$, $|xy|\le\frac\varepsilon2x^2+\frac1{2\varepsilon}y^2$.

</li>

<li>

__Means__: For $x,y\ge0$, $\sqrt{xy}\le\frac{x+y}2$. On the left is the __geometric mean__, on the right the __arithmetic mean__.

</li>

<li>

__Cauchy-Schwarz__: For $x_1,\dots,x_n,y_1,\dots,y_n\in\mathbb{R}$, with $\|\vec x\|:=\sqrt{\sum_{i=1}^nx_i^2}\ge0$,

<span class="anker" id="gl-9-1"></span>
$$\sum_{i=1}^n|x_iy_i|\le\sqrt{\sum_{i=1}^nx_i^2}\cdot\sqrt{\sum_{i=1}^ny_i^2}=\|\vec x\|\cdot\|\vec y\|. \tag{9.1}$$

</li>

<li>

__Minkowski__: With $\vec x+\vec y:=(x_1+y_1,\dots,x_n+y_n)$,

<span class="anker" id="gl-9-2"></span>
$$\sqrt{\sum_{i=1}^n(x_i+y_i)^2}\le\sqrt{\sum_{i=1}^nx_i^2}+\sqrt{\sum_{i=1}^ny_i^2},\quad\text{that is,}\quad\|\vec x+\vec y\|\le\|\vec x\|+\|\vec y\|. \tag{9.2}$$

</li>

</ol>
:::

⁠**How to read it:** $\vec x=(x_1,\dots,x_n)$ is a __vector__, a list of $n$ numbers, and $\|\vec x\|$ its __norm__. For $n=2$ this is, by Pythagoras, the length of the arrow from the origin to the point $(x_1,x_2)$. Then [(9.2)](#gl-9-2) is the triangle inequality for arrows, and in Part 8 [(9.1)](#gl-9-1) turns into the dot product. In Young, $\varepsilon$ is an exchange rate: A small $x$ term costs a large $y$ term. **Why the hypotheses:** Bernoulli: $x=-4$, $n=3$ gives $-27>-11$, false, so $x>-1$ is needed. For $x=0$ or $n=1$ there is equality. Means: $x=y=-1$ gives $1\le-1$, false. Young: $\varepsilon=-1$ makes the right side negative.

:::abbildung hm1/k1mittel 9
Left, the means as a semicircle: The radius is the arithmetic mean, the height above the dividing point the geometric mean. The height is never greater than the radius. Right, Bernoulli for $n=3$: The line touches the curve at $x=0$ and lies below it for $x>-1$.
:::

:::beweis The five inequalities
⁠*Bernoulli*, induction from $n_0=2$. Base case: $(1+x)^2=1+2x+x^2>1+2x$, because $x^2>0$ by Theorem [4.2](anordnungsaxiome.html#satz-4-2) (d). Step: Because $1+x>0$, the hypothesis may be multiplied by $1+x$ by (O4): $(1+x)^{n+1}>(1+nx)(1+x)=1+(n+1)x+nx^2>1+(n+1)x$.

⁠*Young.* $\sqrt\varepsilon$ exists by Theorem [7.2](intervallschachtelung-und-wurzeln.html#satz-7-2), and $\sqrt\varepsilon>0$. Squares are not negative:

$$0\le\Bigl(\sqrt\varepsilon\,x\pm\frac1{\sqrt\varepsilon}\,y\Bigr)^2=\varepsilon x^2\pm2xy+\frac1\varepsilon y^2.$$

This gives $\mp2xy\le\varepsilon x^2+\frac1\varepsilon y^2$. Because $|xy|=\max\{xy,-xy\}$, the claim follows after division by 2.

⁠*Means.* Young with $\varepsilon=1$ for $\sqrt x$ and $\sqrt y$: $\sqrt x\sqrt y\le\frac12x+\frac12y$, and $\sqrt x\sqrt y=\sqrt{xy}$.

⁠*Cauchy-Schwarz.* If all $x_i=0$ or all $y_i=0$, we get $0\le0$. Otherwise $\|\vec x\|>0$ and $\|\vec y\|>0$, and we set $\xi_i:=x_i/\|\vec x\|$, $\eta_i:=y_i/\|\vec y\|$. Dividing [(9.1)](#gl-9-1) by $\|\vec x\|\|\vec y\|$, it remains to show $\sum_{i=1}^n|\xi_i\eta_i|\le1$. We have $\sum_i\xi_i^2=\frac1{\|\vec x\|^2}\sum_ix_i^2=1$, likewise $\sum_i\eta_i^2=1$. By the means for $\xi_i^2$, $\eta_i^2$,

$$\sum_{i=1}^n|\xi_i\eta_i|=\sum_{i=1}^n\sqrt{\xi_i^2\eta_i^2}\le\sum_{i=1}^n\frac{\xi_i^2+\eta_i^2}2=\frac12+\frac12=1.$$

⁠*Minkowski.* Let $s_i:=x_i+y_i$, so $\vec s=\vec x+\vec y$. With (AM), then $a\le|a|$, then [(9.1)](#gl-9-1) for the lists $x_i,s_i$ and $y_i,s_i$:

$$\|\vec s\|^2=\sum_ix_is_i+\sum_iy_is_i\le\sum_i|x_is_i|+\sum_i|y_is_i|\le\bigl(\|\vec x\|+\|\vec y\|\bigr)\|\vec s\|.$$

For $\|\vec s\|=0$, the left side of [(9.2)](#gl-9-2) is 0. Otherwise divide by $\|\vec s\|$.
:::

**Example.** Bernoulli: $1.01^{10}>1.1$, exactly $1.1046$. For small $x$, $1+nx$ is a good approximation: 1 % more voltage means roughly 2 % more power in a resistor, exactly 2.01 %. For large $x$ it is crude: $2^{10}=1024$ versus 11. Young with $x=2$, $y=8$: For $\varepsilon=1$ we get $16\le34$, for $\varepsilon=4$ we get $16\le16$. Cauchy-Schwarz with $\vec x=(3,4)$, $\vec y=(1,2)$: $3+8=11\le5\sqrt5\approx11.18$. Minkowski: $\|(4,6)\|=\sqrt{52}\approx7.21\le5+\sqrt5\approx7.24$. **Limiting case:** For $x=y$ both means are equal; in the semicircle the height stands at the center.

:::frage When do I use which inequality?
Power of a number close to 1: Bernoulli. Estimating a product: Young, means. Sum of products: Cauchy-Schwarz. Root of a sum: Minkowski.
:::

:::aufgabe Exercise 10 ★★★ Estimating
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Show $2^{n-1}\ge n$ for all $n\in\mathbb{N}$. (Stage [7](intervallschachtelung-und-wurzeln.html#stufe-7) needs this inequality.)

</li>

<li>

Estimate $0.995^{20}$ from below and compare with the exact value.

</li>

<li>

A rectangle has area 16. Use the means to show that the perimeter is at least 16. For which sides does equality hold?

</li>

<li>

Check Cauchy-Schwarz and Minkowski for $\vec x=(1,2,2)$, $\vec y=(2,-1,2)$.

</li>

<li>

Show: For $\vec y=t\,\vec x$ with $t\in\mathbb{R}$, equality holds in [(9.1)](#gl-9-1).

</li>

</ol>

:::loesung
(a) For $n=1,2$ we get $1\ge1$ and $2\ge2$. For $n\ge3$, $2^{n-1}=(1+1)^{n-1}>1+(n-1)=n$ by Bernoulli. (b) $x=-0.005$, $n=20$: $0.995^{20}>1-0.1=0.9$. Exactly $0.9046$; the bound lies 0.5 % below it. (c) Sides $a,b>0$, $ab=16$: Perimeter $2(a+b)\ge2\cdot2\sqrt{ab}=16$. Equality for $a=b=4$, the square. (d) $\|\vec x\|=\sqrt{1+4+4}=3$, $\|\vec y\|=\sqrt{4+1+4}=3$. Cauchy-Schwarz: $2+2+4=8\le9$. Minkowski: $\vec x+\vec y=(3,1,4)$, $\|\vec x+\vec y\|=\sqrt{26}\approx5.10\le6$. (e) $\sum_i|x_i\cdot tx_i|=|t|\sum_ix_i^2=|t|\,\|\vec x\|^2$. On the right: $\|t\vec x\|=\sqrt{t^2\sum_ix_i^2}=|t|\,\|\vec x\|$, so $\|\vec x\|\,\|\vec y\|=|t|\,\|\vec x\|^2$.
:::
:::
