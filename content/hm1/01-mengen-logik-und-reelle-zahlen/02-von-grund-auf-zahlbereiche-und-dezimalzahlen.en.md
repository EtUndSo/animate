---
title: From the ground up: Number systems and decimal numbers
pfad: Electrical Engineering / 1st Semester / HöMa1 – Higher Mathematics 1 / Sets, Logic and Real Numbers
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Chapter 1: Sets, Logic and Real Numbers
order: 1210200
summary: What must be assumed about numbers and why the square root of 2 is not a fraction
tags: natural numbers, integers, rational numbers, real number, irrational
lang: en
---

The symbol $:=$ means “is defined as.” The __natural numbers__ are $\mathbb{N}:=\{1,2,3,\dots\}$, the __integers__ $\mathbb{Z}:=\{0,1,-1,2,-2,\dots\}$, the __rational numbers__ (fractions) $\mathbb{Q}:=\{p/q:p,q\in\mathbb{Z},\ q\ne0\}$. The colon means “for which.”

:::definition Definition 0.1 (Real number, provisional)
<span class="anker" id="satz-0-1"></span>

A __real number__ is a number with a decimal representation, that is, with a sign, an $m\in\mathbb{N}\cup\{0\}$ and digits $a_1,a_2,\ldots\in\{0,1,\dots,9\}$, finitely or infinitely many:

<span class="anker" id="gl-0-1"></span>
$$x=\pm\Bigl(m+\frac{a_1}{10}+\frac{a_2}{100}+\frac{a_3}{1000}+\dots\Bigr). \tag{0.1}$$

$\mathbb{R}$ is the set of real numbers. The numbers in $\mathbb{R}$ that are not fractions are called __irrational__.
:::

⁠**How to read it:** $3/8=0.375$ terminates, $5/11=0.4545\ldots$ is periodic, and every fraction has one of these two forms. $\sqrt2=1.41421356\ldots$ never becomes periodic. We have $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}\subset\mathbb{R}$. This definition is a stopgap: It does not explain what an infinite sum is (Chapter 4), and it is not unique: $1.000\ldots$ and $0.999\ldots$ are the same number. Stage [6](das-vollstandigkeitsaxiom.html#stufe-6) replaces it with axioms.
