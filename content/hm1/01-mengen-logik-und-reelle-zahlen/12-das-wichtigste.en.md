---
title: Key points
pfad: Electrical Engineering / 1st Semester / HöMa1 – Higher Mathematics 1 / Sets, Logic and Real Numbers
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Chapter 1: Sets, Logic and Real Numbers
order: 1211200
summary: What must be assumed about numbers and why the square root of 2 is not a fraction
tags: 
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

All rules of arithmetic follow by logical reasoning from a few axioms: the field axioms for plus and times and the order axioms for “positive.”

</li>

<li>

The fractions satisfy these axioms too, but they have gaps: No fraction $r$ solves $r^2=2$.

</li>

<li>

The completeness axiom closes the gaps: Every nonempty set that has a lower bound (a number less than or equal to all elements) also has a greatest one. With it the real numbers are uniquely determined, and $\sqrt2$ exists.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Sets and statements obey the same rules, proved by table. $\mathcal A\Rightarrow\mathcal B$ is false only for $t\Rightarrow f$.

</li>

<li>

Negating swaps $\forall$ and $\exists$. Different quantifiers must not be swapped.

</li>

<li>

Field: 10 axioms, link $x(y+z)=xy+xz$. Order: $z<0$ flips the inequality, $x\ne0\Rightarrow x^2>0$.

</li>

<li>

Induction: base case plus step.

</li>

<li>

$\sqrt2\notin\mathbb{Q}$. Completeness: Every nonempty set that is bounded below has an infimum in the field. That separates $\mathbb{R}$ from $\mathbb{Q}$. Nested intervals yield $\sqrt y$.

</li>

<li>

$|x+y|\le|x|+|y|$, $(1+x)^n>1+nx$, $\sqrt{xy}\le\frac{x+y}2$, $\sum|x_iy_i|\le\|\vec x\|\|\vec y\|$, $\|\vec x+\vec y\|\le\|\vec x\|+\|\vec y\|$.

</li>

</ul>
:::

**One principle behind all the results.** Nothing is taken on faith: Every rule stands at the end of a chain of inferences that begins with an axiom.

| Result | Where it comes from |
|---|---|
| De Morgan's rules, contraposition | finitely many cases: truth table (Stage [1](mengen-und-aussagen.html#stufe-1)) |
| Negation of “for all” | “for all” is a long “and,” De Morgan (Stage [2](quantoren-und-indirekter-beweis.html#stufe-2)) |
| $(-1)\cdot(-1)=1$, arithmetic with fractions | field axioms, above all the distributive law (Stage [3](korperaxiome.html#stufe-3)) |
| Inequality flips for $z<0$ | order axioms (Stage [4](anordnungsaxiome.html#stufe-4)) |
| Sum formulas, power laws | construction of the natural numbers: induction (Stage [5](vollstandige-induktion-summe-und-produkt.html#stufe-5)) |
| Archimedes, $\sqrt2$ exists | completeness (Stages [6](das-vollstandigkeitsaxiom.html#stufe-6) and [7](intervallschachtelung-und-wurzeln.html#stufe-7)) |
| Triangle inequality | position on the number line (Stage [8](abstand-und-betrag.html#stufe-8)) |
| Young, Cauchy-Schwarz | squares are not negative (Stage [9](elementare-ungleichungen.html#stufe-9)) |
