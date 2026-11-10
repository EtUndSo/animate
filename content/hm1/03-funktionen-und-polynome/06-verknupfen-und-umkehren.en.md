---
title: Stage 4: Combining and inverting
pfad: Electrical Engineering / 1st Semester / HöMa1 – Higher Mathematics 1 / Functions and Polynomials
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Chapter 3: Functions and Polynomials
order: 1230600
summary: Stage 3 says when f(x)=y has exactly one solution.
tags: sum, difference, product, quotient, composition, nth root
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Stage [3](ruckwarts-injektiv-surjektiv-bijektiv.html#stufe-3) says when $f(x)=y$ has exactly one solution. This stage turns the solution into a function. For that, one must be able to apply functions one after the other.
:::

**The idea.** The inverse function undoes what $f$ does: First $f$, then $g$ leads back to the start, and first $g$, then $f$ likewise (Fig. [5](#abb-5), left). New functions arise from functions in this way, just as new numbers arise from numbers by calculation.

:::definition Definition 4.1 (Combinations)
<span class="anker" id="satz-4-1"></span>

For real functions $f,g$ let $M:=\mathcal D(f)\cap\mathcal D(g)$ and $M':=\{x\in M:g(x)\neq0\}$. Then the __sum__, __difference__ and __product__ on $M$ and the __quotient__ on $M'$ are defined by

<span class="anker" id="gl-4-1"></span>
$$(f\pm g)(x):=f(x)\pm g(x),\qquad(f\cdot g)(x):=f(x)\cdot g(x),\qquad\Bigl(\frac fg\Bigr)(x):=\frac{f(x)}{g(x)}. \tag{4.1}$$

For $f:A\to B$ and $g:B\to C$, the __composition__ or successive application $g\circ f:A\to C$ is defined by

<span class="anker" id="gl-4-2"></span>
$$(g\circ f)(x):=g\bigl(f(x)\bigr)\quad\text{for all }x\in A. \tag{4.2}$$
:::

⁠**How to read it:** $g\circ f$ is read “$g$ after $f$”: $f$ acts first, $f(x)$ lies in $B$, and there $g$ may act. The graph is $\{(x,y)\in A\times C:\text{there is }z\in B\text{ with }f(x)=z,\ g(z)=y\}$. The order counts: For $f(x)=2x$, $g(x)=x+1$, we get $(g\circ f)(1)=3$, but $(f\circ g)(1)=4$. Sum and product are computed point by point, for example $(h/b)(2)=-1/0.2=-5$.

:::satz Theorem 4.2 (Characterization of injective, surjective, bijective)
<span class="anker" id="satz-4-2"></span>

Let $f:A\to B$ be a function, $A$ nonempty. Then:

<ol class="rm">

<li>

$f$ injective $\Leftrightarrow$ there is $g:B\to A$ with $(g\circ f)(x)=x$ for all $x\in A$ (I).

</li>

<li>

$f$ surjective $\Leftrightarrow$ there is $g:B\to A$ with $(f\circ g)(y)=y$ for all $y\in B$ (S).

</li>

<li>

$f$ bijective $\Leftrightarrow$ there is exactly one function $g:B\to A$ with (I) and (S).

</li>

</ol>
:::

:::beweis Characterization
(i) “$\Leftarrow$”: From $f(x_1)=f(x_2)$ follows $x_1=g(f(x_1))=g(f(x_2))=x_2$. “$\Rightarrow$” as an idea: $g$ gives each $y\in\mathcal W(f)$ its only preimage and all other $y$ a fixed value from $A$.

(ii) “$\Leftarrow$”: For $y\in B$ set $z:=g(y)\in A$; then $f(z)=(f\circ g)(y)=y$, so $y\in\mathcal W(f)$. “$\Rightarrow$” as an idea: For each $y$, $g$ chooses one of its preimages.

(iii) “$\Leftarrow$”: (I) gives injective, (S) gives surjective. “$\Rightarrow$”: Bijective means that each $y$ has exactly one preimage $g(y)$; this $g$ satisfies (I) and (S). If $\hat g$ satisfies both as well, then $\hat g(y)=\hat g\bigl(f(g(y))\bigr)=g(y)$ by (S) for $g$ and (I) for $\hat g$.
:::

⁠**How to read it:** Memory aid: “Surjective” is about the images, so (S) stands for all $y\in B$. **Why “bijective” is needed for uniqueness:** $h:\mathbb{R}\to[-1,\infty)$ is only surjective, and both $g_1(y)=2+\sqrt{y+1}$ and $g_2(y)=2-\sqrt{y+1}$ satisfy (S). $h:[2,\infty)\to\mathbb{R}$ is only injective, and $g(y)=2+\sqrt{y+1}$ for $y\ge-1$, $g(y)=c$ for $y<-1$ satisfies (I) for every fixed $c\ge2$.

:::definition Definition 4.3 (Inverse function and root)
<span class="anker" id="satz-4-3"></span>

The function $g$ from Theorem [4.2](#satz-4-2)(iii) is called the inverse function of $f$, written $f^{-1}:=g$. For all $x\in A$, $y\in B$,

<span class="anker" id="gl-4-3"></span>
$$f(x)=y\ \Leftrightarrow\ x=f^{-1}(y),\qquad f^{-1}\bigl(f(x)\bigr)=x,\qquad f\bigl(f^{-1}(y)\bigr)=y. \tag{4.3}$$

The inverse function of $x\mapsto x^n$ (on $\mathbb{R}_0^+$ for even $n$, on $\mathbb{R}$ for odd $n$) is called the __$n$th root__, $f^{-1}(y)=\sqrt[n]{y}=y^{1/n}$.
:::

⁠**How to read it:** The first statement says: $f^{-1}$ solves the equation $f(x)=y$. Proof: From $f(x)=y$ follows $x=g(f(x))=g(y)$ by (I); from $g(y)=x$ follows $y=f(g(y))=f(x)$ by (S). For the root the two other statements read $\sqrt[n]{y^n}=y$ and $(\sqrt[n]{y})^n=y$. **Caution:** $f^{-1}(y)$ is not $1/f(y)$. For $h$ on $[2,\infty)$, $h^{-1}(8)=5$, but $1/h(8)=1/35$.

**The graph.** By [(4.3)](#gl-4-3), $\mathcal G(f)=\{(x,f(x))\}=\{(g(y),y):y\in B\}$, while $\mathcal G(g)=\{(y,g(y)):y\in B\}$. The pairs are swapped, and swapping the coordinates is the reflection in the angle bisector $\{(x,y)\in\mathbb{R}^2:x=y\}$ (Fig. [5](#abb-5), right).

:::abbildung hm1/k3spiegel 5
Left, the way there and back for $h$ on $[2,\infty)$: $h(5)=8$ and $h^{-1}(8)=5$. Right, the graphs of $h$ and $h^{-1}(y)=2+\sqrt{y+1}$: Reflection in the dashed line takes the point $(4\,|\,3)$ to $(3\,|\,4)$.
:::

:::satz Theorem 4.4 (Monotonicity is inherited)
<span class="anker" id="satz-4-4"></span>

Let $f:A\to B$ be real, surjective and strictly monotonically increasing (decreasing). Then $g=f^{-1}:B\to A$ exists and is likewise strictly monotonically increasing (decreasing).
:::

:::beweis Monotonicity is inherited
For increasing $f$ (decreasing works the same way): $f$ is injective as in Theorem [3.2](ruckwarts-injektiv-surjektiv-bijektiv.html#satz-3-2) and surjective, so $g$ exists. Let $y_1<y_2$. If $g(y_1)\ge g(y_2)$ held, applying $f$ would give the contradiction $y_1\ge y_2$. So $g(y_1)<g(y_2)$.
:::

⁠**How to read it and why the hypotheses are needed:** Without “surjective,” $g$ is missing for some $y\in B$. Without monotonicity there is nothing to inherit either. **Application:** $\sqrt[n]{y}$ is strictly monotonically increasing. **Limiting case:** For $f(x)=x$, $f^{-1}=f$; the graph lies on the mirror axis.

:::frage Why does [(4.3)](#gl-4-3) not say $\sqrt{y^2}=y$ for all $y$ in the case of the root?
Because the inversion belongs only to the function on $\mathbb{R}_0^+$. For $y=-3$, $\sqrt{(-3)^2}=3$, so in general $\sqrt{y^2}=|y|$. The error arises when you forget the domain on which $f$ is invertible.
:::

:::aufgabe Exercise 4 ★★ Finding an inverse function
<span class="anker" id="aufg-4"></span>

Let $f:[2,\infty)\to(2,5]$, $f(x)=\dfrac{2x+1}{x-1}=2+\dfrac{3}{x-1}$. (a) Show that $f$ is strictly decreasing. (b) Determine $f^{-1}$. (c) Compare $f^{-1}(4)$ with $1/f(4)$. (d) Prediction: Is $f^{-1}$ increasing or decreasing? Check with $y=3$ and $y=4$.

:::loesung
(a) From $2\le x_1<x_2$ follows $0<x_1-1<x_2-1$, so $\frac{3}{x_1-1}>\frac{3}{x_2-1}$ and $f(x_1)>f(x_2)$. (b) From $y=2+\frac{3}{x-1}$ follows $x-1=\frac{3}{y-2}$, so $f^{-1}(y)=1+\frac{3}{y-2}=\frac{y+1}{y-2}$ for $y\in(2,5]$. (c) $f^{-1}(4)=\frac52$ (check: $f(\frac52)=6/1.5=4$), whereas $1/f(4)=\frac13$. (d) Decreasing by Theorem [4.4](#satz-4-4): $f^{-1}(3)=4>f^{-1}(4)=\frac52$.
:::
:::

:::aufgabe Exercise 5 ★★★ Inverting a chain
<span class="anker" id="aufg-5"></span>

Let $f(x)=2x+1$, $g(x)=x^3$ on $\mathbb{R}$. (a) Compute $(g\circ f)(1)$ and $(f\circ g)(1)$. (b) Show in general for bijective $f:A\to B$, $g:B\to C$: $(g\circ f)^{-1}=f^{-1}\circ g^{-1}$. Why does the order reverse? (c) Determine $(g\circ f)^{-1}(y)$ and check with $y=27$.

:::loesung
(a) $(g\circ f)(1)=g(3)=27$, $(f\circ g)(1)=f(1)=3$. (b) $f^{-1}\bigl(g^{-1}(g(f(x)))\bigr)=f^{-1}(f(x))=x$, likewise in the other order for $y\in C$. So (I) and (S) hold, and by Theorem [4.2](#satz-4-2)(iii) there is only one such function. The way back must undo the last step first. (c) $g^{-1}(y)=\sqrt[3]{y}$, $f^{-1}(y)=\frac{y-1}{2}$, so $(g\circ f)^{-1}(y)=\frac{\sqrt[3]{y}-1}{2}$. At $y=27$: $(3-1)/2=1$.
:::
:::
