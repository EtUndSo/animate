---
title: Stage 7: Nested intervals and roots
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Sets, Logic and Real Numbers
order: 1210900
summary: The axiom guarantees boundaries.
tags: interval, nonnegative numbers, square root
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
The axiom guarantees boundaries. This stage turns that into a construction method and uses it to prove that $x^2=2$ has exactly one positive solution in $\mathbb{R}$.
:::

**The idea.** You trap the number you seek between two fractions and halve the interval again and again until it is arbitrarily small (Fig. [7](#abb-7)). Each interval lies in the previous one. Completeness guarantees that there is a point that lies in all of them. In $\mathbb{Q}$ this point can be missing. An __interval__ is $[a,b]:=\{x\in\mathbb{R}:a\le x\le b\}$; the __nonnegative numbers__ are $\mathbb{R}_0^+:=\{x\in\mathbb{R}:x\ge0\}$.

:::satz Theorem 7.1 (Nested intervals)
<span class="anker" id="satz-7-1"></span>

For numbers $a_n,b_n\in\mathbb{R}$, $n\in\mathbb{N}$, suppose that $a_1\le a_2\le a_3\le\dots\le b_3\le b_2\le b_1$ and

<span class="anker" id="gl-7-1"></span>
$$\forall\varepsilon>0\ \exists n\in\mathbb{N}:\ 0\le b_n-a_n<\varepsilon. \tag{7.1}$$

Then there is exactly one $x\in\mathbb{R}$ with $a_n\le x\le b_n$ for all $n\in\mathbb{N}$.
:::

⁠**How to read it:** $\varepsilon$ (Greek epsilon) is an arbitrarily small positive number. [(7.1)](#gl-7-1) means: The intervals $[a_n,b_n]$ become smaller than any given length. **Why the hypotheses:** Without [(7.1)](#gl-7-1), $x$ is not unique: For $a_n=-\frac1n$, $b_n=1+\frac1n$, all of $[0,1]$ lies in all the intervals. In $\mathbb{Q}$ the theorem does not hold: The fractions $a_n,b_n$ from Fig. [7](#abb-7) satisfy all the conditions, but no fraction lies in all the intervals.

:::beweis Nested intervals
⁠*Existence.* For arbitrary $n,k$, let $m$ be the larger of the two numbers. Then $a_n\le a_m\le b_m\le b_k$. So every $b_k$ is an upper bound of $A:=\{a_n:n\in\mathbb{N}\}$. By Theorem [6.5](das-vollstandigkeitsaxiom.html#satz-6-5) (i), $x:=\sup A$ exists. We have $a_n\le x$ because $x$ is an upper bound, and $x\le b_k$ because $x$ is the least one.

⁠*Uniqueness.* If $x<\tilde x$ lay in all the intervals, then $b_n-a_n\ge\tilde x-x=:\varepsilon>0$ for all $n$, contradicting [(7.1)](#gl-7-1).
:::

:::abbildung hm1/k1schachtelung 7
Halving for $x^2=2$: If the square of the midpoint is less than 2, it becomes the new left endpoint, otherwise the new right endpoint. The length is $b_n-a_n=2^{1-n}$.
:::

:::satz Theorem 7.2 (Square root)
<span class="anker" id="satz-7-2"></span>

For every $y\in\mathbb{R}_0^+$ there is exactly one $x\in\mathbb{R}_0^+$ with $x^2=y$. One writes $x=\sqrt y$ (“__square root__ of $y$”). For $x,y\ge0$, $\sqrt{xy}=\sqrt x\sqrt y$.
:::

⁠**How to read it:** The root is the nonnegative solution, $\sqrt{4}=2$ and not $-2$. The equation $z^2=2$ has two solutions: $\sqrt2$ and $-\sqrt2$, because $(-1)(-1)=1$. The product rule needs $x,y\ge0$: $\sqrt{(-1)(-1)}=1$, but $\sqrt{-1}$ does not exist in $\mathbb{R}$. **Limiting case** $y=0$: The only solution is $x=0$.

:::beweis Existence for $y=2$, uniqueness, product rule
Start with $a_1=1$, $b_1=2$ and halve as in Fig. [7](#abb-7). All $a_n$, $b_n$ are fractions, so by Theorem [6.1](das-vollstandigkeitsaxiom.html#satz-6-1) never $a_n^2=2$ or $b_n^2=2$. That gives $a_n^2<2<b_n^2$ and $b_n-a_n=2^{1-n}\le\frac1n$ because $2^{n-1}\ge n$ (Exercise [10](elementare-ungleichungen.html#aufg-10)). By Theorem [6.5](das-vollstandigkeitsaxiom.html#satz-6-5) (vi), [(7.1)](#gl-7-1) holds, so there is $x$ with $a_n\le x\le b_n$ for all $n$.

Why $x^2=2$: From $a_n\le x\le b_n$, Theorem [4.2](anordnungsaxiome.html#satz-4-2) (e) gives $a_n^2\le x^2\le b_n^2$. The number 2 also lies in $[a_n^2,b_n^2]$. This interval has length $(b_n-a_n)(b_n+a_n)\le4\cdot\frac1n$. So the distance between $x^2$ and 2 is smaller than any positive number and therefore zero. For other $y>0$ one starts with $[0,y+1]$; if a midpoint $m$ hits exactly $m^2=y$, then $x=m$. For $y=0$, $x=0$. *Uniqueness:* From $u>v\ge0$ it follows that $u^2>v^2$; two different nonnegative numbers have different squares.

⁠*Product rule:* $\sqrt x\sqrt y\ge0$ and $(\sqrt x\sqrt y)^2=xy$ (M1, M2), and the nonnegative solution is unique.
:::

::::beispiel
After six steps, $1.40625\le\sqrt2\le1.4375$, width $2^{-5}=0.03125$. Decimal numbers are the same idea with ten parts instead of two: Each digit narrows the interval to one tenth. That is why every real number has a representation [(0.1)](von-grund-auf-zahlbereiche-und-dezimalzahlen.html#gl-0-1).
::::

:::frage Surely it is enough to read $\sqrt2$ off a calculator. Why the effort?
For any numerical value, that is enough. But the calculator shows a fraction, $1.414213562$, whose square is not 2. The question here is: Is there a number whose square is exactly 2 at all? In $\mathbb{Q}$ no, in $\mathbb{R}$ yes, and this difference later carries limits and continuity.
:::

:::aufgabe Exercise 8 ★★★ The square root of 3
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Carry out three halving steps for $x^2=3$, starting with $[1,2]$. How wide is the result?

</li>

<li>

Prove $\sqrt3\notin\mathbb{Q}$. Hint: A number that is not divisible by 3 has the form $3k\pm1$.

</li>

<li>

At which point does the same proof fail for $\sqrt4$?

</li>

</ol>

:::loesung
(a) Midpoint $1.5$: $2.25<3$, so $[1.5, 2]$. Midpoint $1.75$: $3.0625>3$, so $[1.5, 1.75]$. Midpoint $1.625$: $2.640625<3$, so $[1.625, 1.75]$. Width $\frac18=0.125$. (b) Assumption: $\sqrt3=\frac pq$, $p,q\in\mathbb{N}$, not both divisible by 3. Then $p^2=3q^2$. If $p=3k\pm1$, then $p^2=3(3k^2\pm2k)+1$, not divisible by 3. So $p=3k$, hence $q^2=3k^2$, and likewise $q$ is divisible by 3. Contradiction. (c) From $p^2=4q^2$ it follows that $p=2k$ and $k^2=q^2$. That says nothing about the divisibility of $q$: $\sqrt4=\frac21$.
:::
:::
