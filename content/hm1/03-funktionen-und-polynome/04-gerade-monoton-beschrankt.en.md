---
title: Stage 2: Even, monotonic, bounded
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Functions and Polynomials
order: 1230400
summary: The definition says what a function is, but not what it looks like.
tags: even, odd, monotonically increasing, strictly monotonically increasing, monotonically decreasing, strictly monotonically decreasing, bounded
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
The definition says what a function is, but not what it looks like. Three properties save computation: Symmetry halves the work, monotonicity orders the values, boundedness limits them.
:::

**The idea.** If $f(x)$ depends only on the distance from zero, the values on the left are a mirror image of the values on the right (Fig. [3](#abb-3)). If $f$ grows with $x$, then $x<y$ already tells you something about the values without computing them. If $f$ stays below a fixed number, nothing can grow beyond all bounds.

:::definition Definition 2.1 (Symmetry, monotonicity, boundedness)
<span class="anker" id="satz-2-1"></span>

Let $f$ be a real function. If $\mathcal D(f)$ contains $-x$ along with $x$, then $f$ is called __even__ if $f(x)=f(-x)$ for all $x\in\mathcal D(f)$, and __odd__ if $f(x)=-f(-x)$ for all $x\in\mathcal D(f)$. Further, $f$ is called, in each case for all $x,y\in\mathcal D(f)$,

<ol class="rm">

<li>

__monotonically increasing__ if $x<y$ implies $f(x)\le f(y)$;

</li>

<li>

__strictly monotonically increasing__ if $x<y$ implies $f(x)<f(y)$;

</li>

<li>

__monotonically decreasing__ if $x<y$ implies $f(x)\ge f(y)$;

</li>

<li>

__strictly monotonically decreasing__ if $x<y$ implies $f(x)>f(y)$.

</li>

</ol>

$f$ is called __bounded__ above (below) if there is a number $K$ with $f(x)\le K$ ($f(x)\ge K$) for all $x\in\mathcal D(f)$, that is, if the set $\mathcal W(f)$ is bounded above (below). If both hold, $f$ is called bounded.
:::

⁠**How to read it:** Even means: Reflection in the $y$-axis maps the graph onto itself. Odd means: Point reflection through the origin maps it onto itself. The names come from the powers: $(-x)^{2n}=x^{2n}$ and $(-x)^{2n+1}=-x^{2n+1}$. It is therefore enough to know the values on $\mathcal D(f)\cap\mathbb{R}_0^+$; the reflection supplies the rest. Decreasing and increasing are linked: $f$ is (strictly) monotonically decreasing if and only if $-f$ is (strictly) monotonically increasing, because multiplication by $-1$ flips the inequality.

:::abbildung hm1/k3eigenschaften 3
Left, the even bell $b$: The values at $\pm1.5$ are equal. Center, the odd function $x^3-3x$: The values at $\pm1.5$ are opposite, $\mp1.125$. Right, a monotonically increasing function with a horizontal piece: It is not strictly monotonic.
:::

:::satz Theorem 2.2 (Powers are monotonic)
<span class="anker" id="satz-2-2"></span>

Let $n\in\mathbb{N}$. For odd $n$, $f(x)=x^n$ is strictly monotonically increasing on $\mathbb{R}$; for even $n$, on $\mathbb{R}_0^+$.
:::

:::beweis Powers
⁠**Case $0\le x<y$, every $n$:** Induction on $n$. For $n=1$ there is nothing to show. From $x^n<y^n$ follows $x^{n+1}=x\cdot x^n\le y\cdot x^n<y\cdot y^n=y^{n+1}$. The first step uses $x<y$ and $x^n\ge0$, the second $y>0$. This settles even $n$. **Case $x<y\le0$, $n$ odd:** We have $0\le-y<-x$, by the first case $(-y)^n<(-x)^n$, and because $n$ is odd, $-y^n<-x^n$, so $x^n<y^n$. **Case $x<0<y$, $n$ odd:** $x^n<0<y^n$.
:::

⁠**How to read it:** $n$ is the fixed power. **Why “on $\mathbb{R}_0^+$” is needed:** For even $n$, $f$ is not monotonic on all of $\mathbb{R}$: $-2<-1$, but $(-2)^2>(-1)^2$.

**Examples.** $h$ is bounded below by $-1$, but not above. The bell is bounded and strictly decreasing on $\mathbb{R}_0^+$: From $0\le x<y$ follows $1+x^2<1+y^2$, so $b(x)>b(y)$. Sum and product of bounded functions are again bounded: From $|f|\le K$ and $|g|\le L$ follow $|f+g|\le K+L$ and $|f\cdot g|\le K\,L$. **Limiting cases:** A constant function is monotonically increasing and decreasing at the same time, but not strictly. $f(x)=0$ is even and odd at the same time.

:::frage Is a function that is not even automatically odd?
For numbers that is true; for functions it is not: $f(x)=x^2+x$ has $f(1)=2$ and $f(-1)=0$: neither equal nor opposite. Most functions are neither.
:::

:::aufgabe Exercise 2 ★★ Symmetry and bounds
<span class="anker" id="aufg-2"></span>

(a) Even, odd or neither: $f_1(x)=x^4-3x^2$, $f_2(x)=x^3+x$, $f_3(x)=x^2+x$, $f_4(x)=x\,|x|$? (b) Show: The product of two odd functions is even. (c) For $v(x)=3/(2+x^2)$, determine bounds and the range, and show that $v$ is strictly decreasing on $\mathbb{R}_0^+$.

:::loesung
(a) $f_1(-x)=f_1(x)$: even. $f_2(-x)=-x^3-x=-f_2(x)$: odd. $f_3(1)=2$, $f_3(-1)=0$: neither. $f_4(-x)=-x\,|x|=-f_4(x)$: odd. (b) With $f(-x)=-f(x)$ and $g(-x)=-g(x)$ we get $(f\cdot g)(-x)=(-f(x))(-g(x))=(f\cdot g)(x)$. (c) Because $2+x^2\ge2$, we have $0<v(x)\le\frac32$. Every $y\in(0,\frac32]$ is hit by $x=\sqrt{3/y-2}$, so $\mathcal W(v)=(0,\frac32]$. For $0\le x<y$ the denominator grows and the fraction falls.
:::
:::
