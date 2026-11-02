---
title: Key points
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Complex Numbers
order: 1220800
summary: How a second axis makes $x^2=-1$ solvable and what is lost in the process
tags: complex number, imaginary unit, complex plane, field, complex conjugate, absolute value, triangle inequality
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

A __complex number__ is a pair of real numbers, written $z=x+\mathrm{i}y$. The __imaginary unit__ $\mathrm{i}$ is the pair $(0,1)$ and satisfies $\mathrm{i}^2=-1$. All pairs together form the __complex plane__, in which $\mathbb{R}$ is the horizontal axis.

</li>

<li>

You calculate as in $\mathbb{R}$ and replace $\mathrm{i}^2$ by $-1$. That is why $\mathbb{C}$ is a __field__ (a set in which the four basic operations follow the familiar laws). What is lost is the order: There is no “greater than” between complex numbers.

</li>

<li>

The __complex conjugate__ $\overline{z}=x-\mathrm{i}y$ is the mirror image of $z$ across the real axis, and $z\overline{z}=x^2+y^2$ is real. From this follow division, the __absolute value__ $|z|=\sqrt{x^2+y^2}$ (distance from the origin) and the __triangle inequality__ $|z+w|\le|z|+|w|$ (a detour is never shorter).

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

A complex number is a pair: $z=x+\mathrm{i}y$ with $\mathrm{i}^2=-1$. You calculate as in $\mathbb{R}$.

</li>

<li>

Addition is the parallelogram, multiplication by $\mathrm{i}$ rotates by $90^\circ$.

</li>

<li>

Conjugating reflects: $\overline{z}=x-\mathrm{i}y$, and $z\overline{z}=x^2+y^2=|z|^2$.

</li>

<li>

Division: Multiply top and bottom by the conjugate of the denominator, $w/z=w\overline{z}/|z|^2$.

</li>

<li>

$\mathbb{C}$ is a field, but not ordered. Inequalities stand only between real quantities.

</li>

<li>

$|z|=\sqrt{x^2+y^2}$, $d(z,w)=|z-w|$, $|zw|=|z||w|$, $|z+w|\le|z|+|w|$.

</li>

<li>

$z^2+pz+q=0$ always has solutions in $\mathbb{C}$: $z=-p/2\pm w$ with $w^2=p^2/4-q$.

</li>

</ul>
:::

**One principle behind all the results.** Everything in this chapter follows from one rule: Calculate with $\mathrm{i}$ as with a letter and replace $\mathrm{i}^2$ by $-1$.

| Result | Where it comes from |
|---|---|
| Product formula | Multiplying out, the minus is $\mathrm{i}^2$ (Stage [1](paare-statt-einzelner-zahlen.html#stufe-1)) |
| Addition as a parallelogram | Real and imaginary parts add separately (Stage [2](die-komplexe-ebene.html#stufe-2)) |
| Times $\mathrm{i}$ rotates by $90^\circ$ | $\mathrm{i}(x+\mathrm{i}y)=-y+\mathrm{i}x$, rotated twice is $-1$ (Stage [2](die-komplexe-ebene.html#stufe-2)) |
| $z\overline{z}=x^2+y^2$ | Difference of squares with $-\mathrm{i}^2=+1$ (Stage [3](spiegeln-an-der-reellen-achse.html#stufe-3)) |
| Division | Multiplying top and bottom by $\overline{z}$ makes the denominator real (Stage [4](dividieren-und-was-verloren-geht.html#stufe-4)) |
| No order | $\mathrm{i}^2=-1$ is a negative square (Stage [4](dividieren-und-was-verloren-geht.html#stufe-4)) |
| $\vert zw\vert =\vert z\vert \,\vert w\vert $, triangle inequality | $\vert z\vert ^2=z\overline{z}$ (Stage [5](betrag-und-abstand.html#stufe-5)) |
| Quadratic equations | Completing the square works in every field, every number has a root (Stage [6](quadratische-gleichungen.html#stufe-6)) |
