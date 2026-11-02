---
title: Overview: Complex Numbers
kurz: Overview
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Complex Numbers
order: 1220100
summary: How a second axis makes $x^2=-1$ solvable and what is lost in the process
tags: real part, imaginary part
lang: en
---

## What this is about

The equation $x^2=-1$ has no solution in $\mathbb{R}$, because the square of a real number is never negative. Yet quadratic equations keep leading to square roots of negative numbers, and AC engineering calculates with them every day. The question is: *Can $\mathbb{R}$ be extended so that $x^2=-1$ becomes solvable and the rules of arithmetic stay intact, and what is lost in the process?*



**How to work with this chapter.** Each stage is a short article of its own with the idea, typical questions you can expand, and exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise. Finish one stage before you move on to the next.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Two fixed numbers:** $z_1=3+\mathrm{i}$ and $z_2=1+2\mathrm{i}$. In $z_1$, 3 is the __real part__ (the portion without $\mathrm{i}$) and 1 is the __imaginary part__ (the real number in front of $\mathrm{i}$). General statements in this chapter use $z$ and $w$.

</li>

<li>

⁠**What becomes of them:** $z_1+z_2=4+3\mathrm{i}$, $z_1z_2=1+7\mathrm{i}$, $z_1/z_2=1-\mathrm{i}$, $|z_1+z_2|=5$.

</li>

<li>

⁠**Two equations:** $z^2-6z+10=0$ with real and $z^2-(4+3\mathrm{i})z+1+7\mathrm{i}=0$ with complex coefficients. The second has exactly $z_1$ and $z_2$ as solutions.

</li>

</ul>

The script `rechnung_kap2.py` checks all numbers.
:::
