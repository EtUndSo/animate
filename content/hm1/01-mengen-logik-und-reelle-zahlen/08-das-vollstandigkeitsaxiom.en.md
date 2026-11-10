---
title: Stage 6: The completeness axiom
pfad: Electrical Engineering / 1st Semester / HöMa1 – Higher Mathematics 1 / Sets, Logic and Real Numbers
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Chapter 1: Sets, Logic and Real Numbers
order: 1210800
summary: mathbb Q satisfies all the axioms so far.
tags: bounded above, upper bound, bounded below, lower bound, bounded, supremum, infimum, maximum
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
$\mathbb{Q}$ satisfies all the axioms so far. Yet something is missing: the number whose square is 2. This stage shows that and names the axiom that separates $\mathbb{R}$ from $\mathbb{Q}$.
:::

**The idea.** $\mathbb{N}$ and $\mathbb{Z}$ have visible gaps. $\mathbb{Q}$ seems to lie without gaps: Between two fractions $p/q<u/v$ there is always another, $\frac12(p/q+u/v)=p/q+\frac12(u/v-p/q)$. Yet there are points that no fraction hits (Fig. [6](#abb-6)). Completeness means: Every such boundary is a number.

:::satz Theorem 6.1 (The square root of 2 is not a fraction)
<span class="anker" id="satz-6-1"></span>

There is no $r\in\mathbb{Q}$ with $r^2=2$.
:::

:::beweis Indirect
Assumption: $r=\frac pq$ with $p,q\in\mathbb{N}$ (the sign does not matter), reduced far enough that $p$ and $q$ are not both even. From $r^2=2$ it follows that $p^2=2q^2$, so $p^2$ is even. By the contraposition from Stage [1](mengen-und-aussagen.html#stufe-1), $p$ is even, $p=2k$. Substituting: $4k^2=2q^2$, so $q^2=2k^2$, and likewise $q$ is even. Then $p$ and $q$ are both even, contradicting the reduction.
:::

⁠**How to read it:** So $r^2=2$ is not solvable in $\mathbb{Q}$. For $r^2=4$ the proof fails, as it must (Exercise [8](intervallschachtelung-und-wurzeln.html#aufg-8)).

:::abbildung hm1/k1luecke 6
The fractions from $D$ and the fractions with $x^2>2$ lie arbitrarily close together, for example 1.414 and 1.415. The point between them is not a fraction.
:::

:::definition Definition 6.2 (Bound, supremum, infimum)
<span class="anker" id="satz-6-2"></span>

Let $\mathbb K$ be totally ordered and $M\subset\mathbb K$.

<ol class="rm">

<li>

$M$ is called __bounded above__ if there is $S\in\mathbb K$ with $x\le S$ for all $x\in M$. Every such $S$ is called an __upper bound__. Correspondingly __bounded below__ and __lower bound__ with $R\le x$. Both together are called __bounded__.

</li>

<li>

$S$ is called the __supremum__ of $M$, $S=\sup M$, if $S$ is an upper bound and for every upper bound $\tilde S$ we have $S\le\tilde S$ (least upper bound).

</li>

<li>

$R$ is called the __infimum__ of $M$, $R=\inf M$, if $R$ is a lower bound and for every lower bound $\tilde R$ we have $\tilde R\le R$ (greatest lower bound).

</li>

<li>

If $S$ lies in $M$, it is called the __maximum__ ($\max M$); if $R$ lies in $M$, it is called the __minimum__ ($\min M$).

</li>

</ol>
:::

⁠**How to read it:** Bounds stand outside and are not unique: $\{2,3,5,7\}$ has the upper bound 7, but also 100. Here $\sup=\max=7$, $\inf=\min=2$. $\mathbb{N}$ has the lower bound 1 and no upper one (Theorem [6.5](#satz-6-5)).

:::frage Isn't the supremum the largest element?
Only if it lies in the set. $M=\{2-\frac1n:n\in\mathbb{N}\}=\{1,\frac32,\frac53,\dots\}$ has $\min M=1$ and $\sup M=2$, but no maximum, because $2\notin M$. In the reference model, $D$ is bounded above, for example by $1.5$. In $\mathbb{Q}$, $D$ nevertheless has no supremum: For every upper bound there is a smaller one.
:::

:::definition Definition 6.3 (Completeness axiom (V))
<span class="anker" id="satz-6-3"></span>

A totally ordered field $\mathbb K$ is called __complete__ if every nonempty set $M\subset\mathbb K$ that is bounded below has a greatest lower bound $\inf M\in\mathbb K$.
:::

⁠**How to read it:** What matters is “$\in\mathbb K$.” $\mathbb{Q}$ is not complete: $\{x\in\mathbb{Q}:x>0,\ x^2>2\}$ is bounded below and nonempty, but has no greatest lower bound in $\mathbb{Q}$. The candidate would be $\sqrt2\notin\mathbb{Q}$. **Why “nonempty” and “bounded”:** For $M=\emptyset$, every number is a lower bound; there is no greatest one. $M=\mathbb{Z}$ has no lower bound.

:::satz Theorem 6.4 (Main theorem)
<span class="anker" id="satz-6-4"></span>

There is essentially exactly one totally ordered, complete field that contains $\mathbb{Q}$. It is the __field of real numbers__ $\mathbb{R}$; its order agrees on $\mathbb{Q}$ with the usual one.
:::

⁠**How to read it:** The proof goes too far here; the meaning is enough: The three groups of axioms fix $\mathbb{R}$ uniquely up to renaming, which is why one may speak of *the* real numbers. This replaces the provisional definition. The field $\{0,1\}$ satisfies only the field axioms, $\mathbb{Q}$ also the order axioms, only $\mathbb{R}$ all three groups. Equivalent to (V) is the requirement that every Cauchy sequence converges (Chapter 4).

:::satz Theorem 6.5 (Consequences of completeness)
<span class="anker" id="satz-6-5"></span>

In $\mathbb{R}$:

<ol class="rm">

<li>

Every nonempty set $M$ that is bounded above has a supremum, and $\sup M=-\inf(-M)$ with $-M:=\{-x:x\in M\}$.

</li>

<li>

Supremum and infimum of a set are unique.

</li>

<li>

If $S=\sup M$, then for every $y<S$ there is an $x\in M$ with $y<x\le S$. The corresponding statement holds for the infimum.

</li>

<li>

$\mathbb{N}$ is not bounded above.

</li>

<li>

__Theorem of Archimedes:__ For all $x,y>0$ there is an $n\in\mathbb{N}$ with $nx>y$.

</li>

<li>

For every $x>0$ there is an $n\in\mathbb{N}$ with $0<\frac1n<x$ (Eudoxus).

</li>

</ol>
:::

⁠**How to read it:** (iii): Just below the supremum there is always an element of the set. (v): With enough small steps $x$ you get above any height $y$. For $x=0.001$ and $y=1000$, $n=1\,000\,001$ suffices. For $x=0$, (v) does not hold, because $nx=0$. (vi): For $x=0.003$, $n=334$ suffices. One can also demand (v) as an axiom. That is less than (V), because $\mathbb{Q}$ satisfies it.

:::beweis Consequences
(i) With $M$, $-M$ is nonempty too, and if $S$ is an upper bound of $M$, then $-S$ is a lower bound of $-M$ by Theorem [4.2](anordnungsaxiome.html#satz-4-2) (a). (V) gives $R=\inf(-M)$. Because reflecting translates upper bounds into lower bounds and flips the order, $-R$ is the least upper bound of $M$.

(ii) If $S_1$, $S_2$ are suprema, both are upper bounds. So $S_1\le S_2$ because $S_1$ is the least, and likewise $S_2\le S_1$. By (O1), $S_1=S_2$.

(iii) Indirectly: If there were $y<S$ without such an $x$, then $x\le y$ for all $x\in M$ (negation, [(2.1)](quantoren-und-indirekter-beweis.html#gl-2-1)). Then $y$ would be an upper bound smaller than $S$, contradicting the definition of $\sup M$. That $x\le S$ holds is because $S$ is an upper bound.

(iv) Indirectly: Otherwise $S=\sup\mathbb{N}$ would exist by (i). By (iii) there is $n\in\mathbb{N}$ with $S-1<n$. Then $n+1>S$ and $n+1\in\mathbb{N}$, contradicting “upper bound.”

(v) Indirectly: Let $nx\le y$ for all $n$. Because $x^{-1}>0$, (O4) gives $n\le yx^{-1}$ for all $n$, contradicting (iv). (vi): $y:=1$ in (v) gives $nx>1$, so $x>\frac1n>0$.
:::

:::aufgabe Exercise 7 ★★ Determining bounds
<span class="anker" id="aufg-7"></span>

Determine supremum, infimum, maximum and minimum in $\mathbb{R}$, where they exist, and justify: (a) $M_1=\{x\in\mathbb{Q}:x^2\le4\}$, (b) $M_2=\{\frac{(-1)^n}n:n\in\mathbb{N}\}$, (c) $M_3=\{x\in\mathbb{Q}:x^2<3\}$. Which of these quantities are missing in (c) if one searches only in $\mathbb{Q}$?

:::loesung
(a) $M_1=\{x\in\mathbb{Q}:-2\le x\le2\}$: $\sup=\max=2$, $\inf=\min=-2$. (b) $M_2=\{-1,\frac12,-\frac13,\frac14,\dots\}$: $\sup=\max=\frac12$, $\inf=\min=-1$. (c) $\sup M_3=\sqrt3$, $\inf M_3=-\sqrt3$, no maximum and no minimum, because $\sqrt3\notin\mathbb{Q}$ (Exercise [8](intervallschachtelung-und-wurzeln.html#aufg-8)). In $\mathbb{Q}$, supremum and infimum are missing too: For every rational upper bound there is a smaller one.
:::
:::
