---
title: Stage 8: Distance and absolute value
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Sets, Logic and Real Numbers
order: 1211000
summary: Limits measure how close two numbers lie to each other.
tags: distance, absolute value, triangle inequality, reverse triangle inequality
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
Limits measure how close two numbers lie to each other. For that you need distance and a rule for detours.
:::

**The idea.** The distance between two numbers is the length of the segment between them on the line. The length does not depend on direction, and a detour via a third point is never shorter (Fig. [8](#abb-8)). The absolute value is the distance from zero.

:::definition Definition 8.1 (Distance and absolute value)
<span class="anker" id="satz-8-1"></span>

For $x,y\in\mathbb{R}$,

<span class="anker" id="gl-8-1"></span>
$$d(x,y):=\begin{cases}x-y,&x\ge y\\y-x,&x<y\end{cases}\qquad\text{and}\qquad|x|:=d(x,0)=\begin{cases}x,&x\ge0\\-x,&x<0\end{cases} \tag{8.1}$$

are called the __distance__ of $x$ and $y$ and the __absolute value__ of $x$.
:::

⁠**How to read it:** $d$ as in distance. From the definition it follows that

<span class="anker" id="gl-8-2"></span>
$$d(x,y)=d(x-y,0)=|x-y|,\ \ -|x|\le x\le|x|,\ \ |x|=\max\{x,-x\},\ \ -|x|=\min\{x,-x\}. \tag{8.2}$$

In the reference model, $|x|=3$, $|y|=5$ and $d(x,y)=|{-3}-5|=8$. The minus sign in [(8.1)](#gl-8-1) is deceptive: For $x<0$, $-x$ is positive; the absolute value is never negative. Values with a tolerance are written like this: $|U-5\,\mathrm V|\le0.1\,\mathrm V$ means that $U$ lies between 4.9 V and 5.1 V.

:::satz Theorem 8.2 (Properties of distance and absolute value)
<span class="anker" id="satz-8-2"></span>

For all $x,y,z\in\mathbb{R}$:

|  | Distance | Absolute value |
|---|---|---|
| positive | $d(x,y)\ge0$ | $\vert x\vert \ge0$ |
| definite | $d(x,y)=0\Leftrightarrow x=y$ | $\vert x\vert =0\Leftrightarrow x=0$ |
| symmetric, product | $d(x,y)=d(y,x)$ | $\vert xy\vert =\vert x\vert \vert y\vert $; for $z\ne0$: $\vert x/z\vert =\vert x\vert /\vert z\vert $ |
| __triangle inequality__ | $d(x,y)\le d(x,z)+d(z,y)$ | $\vert x+y\vert \le\vert x\vert +\vert y\vert $ |

In addition, $|x-y|\le|x|+|y|$, the __reverse triangle inequality__ $\bigl||x|-|y|\bigr|\le|x\pm y|$ and $|x|=\sqrt{x^2}$ hold.
:::

⁠**How to read it:** The triangle inequality estimates a sum from above, the reverse one from below.

:::frage Why doesn't $|x+y|=|x|+|y|$ hold?
It holds only with equal signs or if one summand is zero. With different signs the summands partly cancel: $|-3+5|=2<8$. In the worst case two errors add up; that is what the inequality says.
:::

:::abbildung hm1/k1betrag 8
Reference model $x=-3$, $y=5$. Directly, $d(x,y)=8$. The detour via $z=7$ gives $10+2=12$. For every $z$ between $x$ and $y$, for example $z=1$, it gives exactly 8 ($4+4$).
:::

:::beweis Triangle inequality and consequences
Definiteness and symmetry are in [(8.1)](#gl-8-1). *Triangle inequality for $d$.* Without loss of generality (WLOG for short: the remaining cases turn into this one by renaming) let $x<y$; for $x=y$ the left side is 0. For $z=x$ or $z=y$, one summand is 0 and the inequality is an equality. Three cases remain. $x<y<z$: $d(x,z)+d(z,y)=2z-x-y>2y-x-y=y-x$. $x<z<y$: The sum is exactly $y-x$. $z<x<y$: The sum is $x+y-2z>x+y-2x=y-x$.

⁠*Product.* If $xy=0$, both sides are 0 by Theorem [3.2](korperaxiome.html#satz-3-2) (v). For $xy>0$, $x$, $y$ have equal signs by Theorem [4.2](anordnungsaxiome.html#satz-4-2) (c), and $|x||y|$ is $xy$ or $(-x)(-y)$, both equal to $xy$. $xy<0$ works the same way. For the quotient: $z\cdot\frac xz=x$ gives $|z|\,|\frac xz|=|x|$.

⁠*Absolute value.* $|x+y|=|x-(-y)|=d(x,-y)\le d(x,0)+d(0,-y)=|x|+|y|$, because $|-y|=|y|$. With $-y$ in place of $y$ it follows that $|x-y|\le|x|+|y|$.

⁠*Reverse triangle inequality.* $|x|=|(x-y)+y|\le|x-y|+|y|$, so $|x|-|y|\le|x-y|$. Swapping $x$ and $y$ also gives $|y|-|x|\le|x-y|$. By [(8.2)](#gl-8-2), the maximum of the two is $\bigl||x|-|y|\bigr|$. With $-y$ in place of $y$ the variant with $+$ follows.

⁠*Root.* $|x|\ge0$ and $|x|^2=x^2$, so $|x|$ is the unique nonnegative solution of $z^2=x^2$.
:::

::::beispiel
With $x=-3$, $y=5$: $|x+y|=2\le8=|x|+|y|$ and $\bigl||x|-|y|\bigr|=2\le|x+y|=2$.
::::

⁠**Limiting case** $y=0$: All inequalities become $|x|=|x|$.

:::aufgabe Exercise 9 ★★ Inequalities with absolute values
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Describe $\{x\in\mathbb{R}:|x-2|\le3\}$ as an interval.

</li>

<li>

Solve $|x-2|+|x+1|\le5$ by case analysis at $x=-1$ and $x=2$.

</li>

<li>

Two voltages satisfy $|U_1-5\,\mathrm V|\le0.1\,\mathrm V$, $|U_2-3\,\mathrm V|\le0.2\,\mathrm V$. How far can $U_1+U_2$ deviate from 8 V at most? Give a pair that reaches this value.

</li>

</ol>

:::loesung
(a) $-3\le x-2\le3$, so $[-1,5]$. (b) For $x\ge2$: $2x-1\le5$, so $2\le x\le3$. For $-1\le x<2$: $(2-x)+(x+1)=3\le5$, always true. For $x<-1$: $1-2x\le5$, so $-2\le x<-1$. Together: $[-2,3]$. (c) $|(U_1+U_2)-8\,\mathrm V|\le|U_1-5\,\mathrm V|+|U_2-3\,\mathrm V|\le0.3\,\mathrm V$. Reached at $U_1=5.1\,\mathrm V$, $U_2=3.2\,\mathrm V$.
:::
:::
