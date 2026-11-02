---
title: Stage 3: Backward: injective, surjective, bijective
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Functions and Polynomials
order: 1230500
summary: Going forward, there is exactly one y for each x .
tags: injective, surjective, bijective
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Going forward, there is exactly one $y$ for each $x$. Going backward, this guarantee is missing: The equation $f(x)=y$ can have no solution, one, or many. This stage gives the three cases names.
:::

**The idea.** Draw a horizontal line through the graph at height $y$. Every intersection point is a solution of $f(x)=y$ (Fig. [4](#abb-4)). For the parabola $h$, $y=3$ has two solutions ($x=0$ and $x=4$), and $y=-2$ has none. For every $y\in\mathcal W(f)$ there is by definition at least one solution; only, $\mathcal W(f)$ is often unknown.

:::definition Definition 3.1 (Injective, surjective, bijective)
<span class="anker" id="satz-3-1"></span>

A function $f:A\to B$ is called

<ol class="rm">

<li>

__injective__ if for all $x,y\in A$: $f(x)=f(y)\Rightarrow x=y$;

</li>

<li>

__surjective__ if for every $y\in B$ there is an $x\in A$ with $f(x)=y$;

</li>

<li>

__bijective__ if $f$ is injective and surjective.

</li>

</ol>
:::

⁠**How to read it:** Injective means: Equal images have equal preimages, so $f(x)=y$ has at most one solution for each $y$, and the horizontal line meets the graph at most once. Surjective means $\mathcal W(f)=B$: At least one solution for every $y\in B$. Bijective means: exactly one. **Validity:** These properties belong to the function together with $A$ and $B$, not to the formula:

| $f(x)=x^2$ as a map | injective | surjective |
|---|---|---|
| $\mathbb{R}\to\mathbb{R}$ | no, $f(2)=f(-2)$ | no, $y=-1$ has no preimage |
| $\mathbb{R}\to\mathbb{R}_0^+$ | no | yes |
| $\mathbb{R}_0^+\to\mathbb{R}$ | yes | no |
| $\mathbb{R}_0^+\to\mathbb{R}_0^+$ | yes | yes |

:::abbildung hm1/k3rueckwaerts 4
Left, $h:\mathbb{R}\to[-1,\infty)$: surjective but not injective, height 3 is hit twice. Center, $b:\mathbb{R}_0^+\to\mathbb{R}$: injective but not surjective, height 1.5 is never hit. Right, $x^3:\mathbb{R}\to\mathbb{R}$: bijective, every height is hit exactly once.
:::

:::satz Theorem 3.2 (Strictly monotonic implies bijective)
<span class="anker" id="satz-3-2"></span>

A strictly monotonic real function $f:\mathcal D(f)\to\mathcal W(f)$ is bijective.
:::

:::beweis Strictly monotonic implies bijective
$f$ is surjective by definition of $\mathcal W(f)$. For injectivity we show the equivalent contrapositive ([Part 1](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)): From $x\neq y$ follows $f(x)\neq f(y)$. Let $x<y$ (otherwise swap the names). If $f$ is strictly increasing, then $f(x)<f(y)$; if $f$ is strictly decreasing, then $f(x)>f(y)$. In both cases $f(x)\neq f(y)$.
:::

⁠**How to read it:** The target here is exactly $\mathcal W(f)$. **Why “strictly” is needed:** On the horizontal piece in Fig. [3](gerade-monoton-beschrankt.html#abb-3), many $x$ have the same image. **The converse does not hold:** $f(x)=1/x$ on $\mathbb{R}\setminus\{0\}$ is bijective onto $\mathbb{R}\setminus\{0\}$, but not monotonic, because $-1<1$ gives $f(-1)<f(1)$, and $1<2$ gives $f(1)>f(2)$.

**Examples.** By Theorems [2.2](gerade-monoton-beschrankt.html#satz-2-2) and [3.2](#satz-3-2), $f(x)=x^n$ is bijective onto its range, namely $\mathcal W(f)=\mathbb{R}_0^+$ for even $n$ on $\mathbb{R}_0^+$ and $\mathcal W(f)=\mathbb{R}$ for odd $n$ on $\mathbb{R}$. That every $y$ really is hit follows, as for $\sqrt y$, from the completeness of the real numbers ([Part 1](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Without monotonicity one computes directly: $f:\mathbb{R}\to\mathbb{R}$, $f(x)=2x-5$ is injective, because $2x-5=2y-5$ gives $x=y$, and surjective, because for given $y$, $x=(y+5)/2$ solves the equation. **Limiting case:** $f(x)=x$ is bijective; every height is hit exactly at $x=y$.

:::frage Can every non-injective function be made injective?
Yes, by shrinking the domain. That changes the function, and you must say which piece you keep: $h$ on $[2,\infty)$ and $h$ on $(-\infty,2]$ are both injective and have different inverses. This is also how $\sqrt y$ arises from $x^2$ on $\mathbb{R}_0^+$.
:::

:::aufgabe Exercise 3 ★★ How many solutions?
<span class="anker" id="aufg-3"></span>

(a) For $g(x)=x^2+6x+5$: Choose $A$ with $0\in A$ and $B$ such that $g:A\to B$ is bijective, and give the solution of $g(x)=y$. (b) Prediction without calculation: Is $f:\mathbb{Z}\to\mathbb{Z}$, $f(n)=2n$ injective? Surjective?

:::loesung
(a) $g(x)=(x+3)^2-4$ is strictly increasing on $A=[-3,\infty)$, and $B=[-4,\infty)$. From $(x+3)^2=y+4$ and $x+3\ge0$ follows $x=-3+\sqrt{y+4}$. Check: $y=5$ gives $x=0$. (b) Injective, yes: $2n=2m\Rightarrow n=m$. Surjective, no: $3$ is odd and has no preimage.
:::
:::
