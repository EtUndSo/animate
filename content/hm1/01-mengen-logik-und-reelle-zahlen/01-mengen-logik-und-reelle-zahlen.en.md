---
title: Overview: Sets, Logic and Real Numbers
kurz: Overview
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Sets, Logic and Real Numbers
order: 1210100
summary: What must be assumed about numbers and why the square root of 2 is not a fraction
tags: set, statement, axiom, field, order, Completeness, mathematical induction, absolute value
lang: en
---

## What this is about

School teaches rules like $(-1)\cdot(-1)=1$ or “you must not divide by zero.” Why do they hold? Habit as a justification does not get you far: For complex numbers ([Part 2](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)) the rule “squares are not negative” fails, and all limits (Part 4) depend on a property of the numbers that school never mentions. You can see it in a single number: The diagonal of a square with side length 1 has length $\sqrt2$, and no fraction has this value. The question of this chapter is: *What exactly must be assumed about numbers so that all the rules of arithmetic become provable, and what distinguishes the real numbers from the fractions?*

The answer needs two tools and a short list of assumptions. A __set__ collects objects; a __statement__ is a sentence that is true or false. An __axiom__ is a basic assumption that is laid down and not proved. Three groups of axioms suffice: A __field__ is a set in which plus and times work according to the familiar rules. The __order__ fixes which numbers are positive. __Completeness__ says that the number line has no gaps. In addition there are __mathematical induction__, the proof method for statements about all natural numbers, and the __absolute value__, the distance of a number from zero.



**How to work with this chapter.** Each stage is a short article of its own with the idea, typical questions you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise. Finish one stage before you move on to the next.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Sets:** $G=\{1,2,\dots,12\}$, within it $A=\{1,2,3,4,6,12\}$ (divisors of 12) and $B=\{2,3,5,7,11\}$ (primes).

</li>

<li>

⁠**Statement:** $\mathcal E(n):=(n\ge7\Rightarrow n>5)$ for natural numbers $n$.

</li>

<li>

⁠**Gap set:** $D=\{x\in\mathbb{Q}:x>0,\ x^2<2\}$, the positive fractions with square below 2.

</li>

<li>

⁠**Numbers for inequalities:** $x=-3$, $y=5$ for the absolute value; $x=2$, $y=8$ for the means; the lists $\vec x=(3,4)$, $\vec y=(1,2)$ for Cauchy-Schwarz. The script `rechnung_kap1.py` checks all numbers and tables.

</li>

</ul>
:::
