---
title: Stage 4: Order axioms
pfad: Electrical Engineering / 1st Semester / HöMa1 – Higher Mathematics 1 / Sets, Logic and Real Numbers
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Chapter 1: Sets, Logic and Real Numbers
order: 1210600
summary: The field axioms say nothing about “greater.” What assumptions lie behind calculating with inequalities?
tags: totally ordered, Trichotomy
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
The field axioms say nothing about “greater.” What assumptions lie behind calculating with inequalities?
:::

**The idea.** Real numbers lie on a line according to size. One only has to fix which numbers are positive. Then “$x$ greater than $y$” is the same as “$x-y$ is positive.” Multiplication by a negative number reflects the line at zero, which is why the order flips (Fig. [4](#abb-4)).

:::definition Definition 4.1 (Totally ordered field)
<span class="anker" id="satz-4-1"></span>

A field $\mathbb K$ with a relation “$>0$” is called __totally ordered__ if:

<ul>

<li>

⁠**(T1)** Every $x\in\mathbb K$ satisfies exactly one of the relations $x>0$, $x=0$, $(-x)>0$.

</li>

<li>

⁠**(T2)** $x>0\wedge y>0\Rightarrow x+y>0$.

</li>

<li>

⁠**(T3)** $x>0\wedge y>0\Rightarrow x\cdot y>0$.

</li>

</ul>

One sets $x>y:\Leftrightarrow x-y>0$, $x<y:\Leftrightarrow y>x$ and $x\ge y:\Leftrightarrow(x=y\vee x>y)$, and likewise $x\le y$.
:::

⁠**How to read it:** $x>0$ means “$x$ is positive.” (T2) and (T3): Sum and product of positive numbers are positive. $x<0$ is synonymous with $(-x)>0$: $x$ is negative.

:::satz Theorem 4.2 (Calculating with inequalities)
<span class="anker" id="satz-4-2"></span>

In a totally ordered field, for all $x,y,z,u,v$:

|  |  |
|---|---|
| (O1) __Trichotomy__ | exactly one of the relations $x<y$, $x=y$, $x>y$ holds |
| (O2) Transitivity | $x<y\wedge y<z\Rightarrow x<z$ |
| (O3) Monotonicity of addition | $x<y\Rightarrow x+z<y+z$ |
| (O4) Monotonicity of multiplication | $x<y\wedge z>0\Rightarrow xz<yz$ |
| (a) Reflecting | $x<y\Leftrightarrow-y<-x$ |
| (b) Adding | $x<y\wedge u<v\Rightarrow x+u<y+v$ |
| (c) Signs | $xy>0\Leftrightarrow\bigl((x>0\wedge y>0)\vee(x<0\wedge y<0)\bigr)$ |
| (d) Squares | $x\ne0\Rightarrow x\cdot x>0$; in particular $1>0$ |
| (e) Squaring | for $x\ge0$, $y\ge0$: $x^2\ge y^2\Leftrightarrow x\ge y$ |
:::

⁠**How to read it:** An inequality tolerates any addition, but only multiplication by positive numbers. For $z<0$ it flips: $x<y\wedge z<0\Rightarrow xz>yz$. For $z=0$, (O4) becomes $0<0$, false. If an ordered field contained an $i$ with $i\cdot i=-1$, then by (d) $-1>0$ and $1>0$, hence by (T2) $0>0$. That is why the complex numbers from [Chapter 2](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html) cannot be ordered. Instead of (T1) to (T3) one could equivalently take (O1) to (O4) as axioms.

:::frage May I square an inequality?
Only if both sides are not negative; that is (e). Without this assumption: $-3<2$, but $9>4$. Squaring reflects the negative part of the line into the positive one, like times $-1$ in Fig. [4](#abb-4).
:::

:::abbildung hm1/k1spiegel 4
Reference model $x=-3<y=2$. Times 2 stretches the line away from zero; the order stays. Times $-1$ reflects at zero; the order flips: $3>-2$.
:::

:::beweis Order rules from (T1) to (T3)
(O1): (T1) for $x-y$. (O2): $(y-x)+(z-y)=z-x$ is positive by (T2). (O3): $(y+z)-(x+z)=y-x$. (O4): $(y-x)z>0$ by (T3), so with (AM) $yz-xz>0$. (a): $(-x)-(-y)=y-x$. (b): $x+u<y+u$ and $u+y<v+y$ by (O3), then (O2).

(c) “$\Leftarrow$”: For $x,y>0$ this is (T3). For $x,y<0$ we have $(-x)(-y)>0$, and $(-x)(-y)=xy$. “$\Rightarrow$” indirectly: Let $xy>0$, but suppose the pair $(x,y)$ does not belong to the two cases on the right. Then four cases remain. For $x=0$ or $y=0$, $xy=0$, contradicting (T1). For $x<0<y$, (O4) gives $xy<0\cdot y=0$, contradicting $xy>0$. Likewise for $y<0<x$. (d): For $x\ne0$, $x>0$ or $x<0$, and by (c) $x\cdot x>0$. With $x=1\ne0$ it follows that $1>0$.

(e) “$\Leftarrow$”: For $x=y$ there is nothing to show. From $x>y\ge0$ it follows that $x\cdot x>y\cdot x\ge y\cdot y$ by (O4) with $z=x$ and $z=y$. “$\Rightarrow$” as contraposition: From $0\le x<y$ it follows likewise that $x\cdot x\le x\cdot y<y\cdot y$.
:::

::::beispiel
For $x\ne0$, $x$ is positive if and only if $x^{-1}$ is positive, because $x\cdot x^{-1}=1>0$ and (c). Therefore: Solve $\frac1x>2$. For $x>0$ we may multiply by $x$: $1>2x$, so $0<x<\frac12$. For $x<0$ the left side is negative; there is no solution.
::::

⁠**Limiting case:** At $x=\frac12$ we get $2>2$, false; the boundary does not belong.

:::aufgabe Exercise 5 ★★ Inequalities
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Show $x<y\wedge z<0\Rightarrow xz>yz$ from (O4) and (a).

</li>

<li>

For which real $x\ne1$ does $\frac3{x-1}>1$ hold? Distinguish two cases.

</li>

</ol>

:::loesung
(a) From $z<0$ it follows that $-z>0$, by (O4) $-xz<-yz$, by (a) $yz<xz$. (b) Case $x>1$: Multiplying by $x-1>0$ gives $3>x-1$, so $1<x<4$. Case $x<1$: The left side is negative; no solution. Result: $1<x<4$.
:::
:::
