---
title: Overview: Functions and Polynomials
kurz: Overview
pfad: Electrical Engineering / 1st Semester / HöMa1 – Higher Mathematics 1 / Functions and Polynomials
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Chapter 3: Functions and Polynomials
order: 1230100
summary: When an equation can be solved backward and why every zero splits off a factor
tags: function, inverse function, polynomial, zero, linear factor, Horner scheme, rational function, pole
lang: en
---

## What this is about

A temperature sensor delivers exactly one voltage for each temperature. Such an assignment is called a __function__: Every input $x$ gets exactly one output $f(x)$. Going forward, substituting is enough. What is usually needed is the way back: For the measured voltage $y$ we seek the temperature $x$, that is, the solution of the equation $f(x)=y$. The question of this chapter is: *When does $f(x)=y$ have exactly one solution, and how do you find the solutions of $P(x)=0$ for the most important functions, the polynomials?*

The answer leads through seven concepts. The __inverse function__ provides the way back as a function in its own right. A __polynomial__ is a sum of powers of $x$ with fixed numbers in front. A __zero__ is an $x_0$ with $P(x_0)=0$; it comes with a __linear factor__ $x-x_0$, a factor of degree one. The __Horner scheme__ is the computational procedure that splits it off. Then there are the __rational function__, a quotient of two polynomials, and the __pole__, where its denominator becomes zero and its absolute value grows beyond every bound.



**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right below each exercise.

:::merke The reference model for this chapter
<ul>

<li>

⁠**Parabola** $h(x)=x^2-4x+3=(x-2)^2-1=(x-1)(x-3)$, lowest point $(2\,|\,{-1})$.

</li>

<li>

⁠**Bell** $b(x)=1/(1+x^2)$ with $b(0)=1$, $b(1)=0.5$, $b(3)=0.1$.

</li>

<li>

⁠**Polynomial** $P(x)=2x^3-3x^2-11x+6=(x-3)(2x-1)(x+2)$ with the zeros $3$, $\tfrac12$ and $-2$.

</li>

<li>

⁠**Denominator** $Q(x)=x^2-x-2=(x-2)(x+1)$, together the rational function $R(x)=P(x)/Q(x)$.

</li>

<li>

⁠**Polynomial of degree four** $S(x)=x^4-3x^3+x^2+4=(x-2)^2(x^2+x+1)$ with a double zero.

</li>

</ul>

The script `rechnung_kap3.py` checks all numbers.
:::
