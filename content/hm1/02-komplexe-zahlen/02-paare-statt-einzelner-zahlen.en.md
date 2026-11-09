---
title: Stage 1: Pairs instead of single numbers
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Complex Numbers
order: 1220200
summary: In mathbb R , the equation x 2=-1 has no solution.
tags: standard form
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
In $\mathbb{R}$, the equation $x^2=-1$ has no solution. This stage builds a larger set of numbers in which the equation is solvable and which contains $\mathbb{R}$ unchanged.
:::

**The idea.** Every extension of the numbers solves an equation that had no solution before: $x+1=0$ leads from $\mathbb{N}$ to $\mathbb{Z}$, $2x=1$ from $\mathbb{Z}$ to $\mathbb{Q}$, $x^2=2$ from $\mathbb{Q}$ to $\mathbb{R}$. With $x^2=-1$ the case is different. The parabola $y=x^2$ never reaches the height $-1$ (Fig. [1](#abb-1)), because $x^2\ge0$ holds in $\mathbb{R}$ ([Part 1](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). No point is missing between other points, as with $\sqrt2$; instead, every point of the number line is ruled out. The solution must lie beside the line. That is why a second coordinate is added: You calculate with pairs $(x,y)$. The pairs $(x,0)$ are to remain the real numbers, and $(0,1)$ is to have the square $(-1,0)$.

:::abbildung hm1/k2parabel 1
The line $y=2$ meets the parabola twice; the solutions $\pm\sqrt2$ lie on the number line. The line $y=-1$ never meets it: No real $x$ solves $x^2=-1$.
:::

:::definition Definition 1.1 (Complex numbers)
<span class="anker" id="satz-1-1"></span>

The set of complex numbers is $\mathbb{C}:=\{(x,y):x,y\in\mathbb{R}\}$ with the addition $\oplus$ and the multiplication $\odot$:

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} (x_1,y_1)\oplus(x_2,y_2)&:=(x_1+x_2,\;y_1+y_2),\\ (x_1,y_1)\odot(x_2,y_2)&:=(x_1x_2-y_1y_2,\;x_1y_2+x_2y_1). \end{aligned} \tag{1.1|1.2}$$

The zero element is $(0,0)$, the unit element is $(1,0)$, the imaginary unit is $\mathrm{i}:=(0,1)$.
:::

⁠**How to read it:** $x$ and $y$ are real numbers without units, $\oplus$ and $\odot$ are new operations on pairs. **Limiting case:** For $y_1=y_2=0$, [(1.1)](#gl-1-1) and [(1.2)](#gl-1-2) give the pairs $(x_1+x_2,0)$ and $(x_1x_2,0)$. So the pairs $(x,0)$ calculate exactly like the real numbers $x$. That is why one writes $x$ instead of $(x,0)$, $+$ instead of $\oplus$, $\cdot$ instead of $\odot$, and $\mathbb{R}\subset\mathbb{C}$ holds.

:::satz Theorem 1.2 (Imaginary unit and standard form)
<span class="anker" id="satz-1-2"></span>

<ol class="rm">

<li>

We have $\mathrm{i}^2=-1$.

</li>

<li>

Every complex number has exactly one __standard form__ $z=x+\mathrm{i}y$ with $x,y\in\mathbb{R}$.

</li>

<li>

In standard form, $(x_1+\mathrm{i}y_1)+(x_2+\mathrm{i}y_2)=(x_1+x_2)+\mathrm{i}(y_1+y_2)$ and

</li>

</ol>

<span class="anker" id="gl-1-3"></span>
$$(x_1+\mathrm{i}y_1)(x_2+\mathrm{i}y_2)=(x_1x_2-y_1y_2)+\mathrm{i}(x_1y_2+x_2y_1). \tag{1.3}$$
:::

⁠**How to read it:** Nobody has to memorize the formula [(1.3)](#gl-1-3): Multiply out the parentheses, substitute $\mathrm{i}^2=-1$, sort. The minus in $x_1x_2-y_1y_2$ is the $\mathrm{i}^2$. In mathematics the imaginary unit is called $\mathrm{i}$, in electrical engineering $\mathrm{j}$, because $i$ is the current there. This chapter writes an upright $\mathrm{i}$. **Validity:** $x$ and $y$ must be real. Otherwise the representation is not unique: $\mathrm{i}=\mathrm{i}+\mathrm{i}\cdot0=0+\mathrm{i}\cdot1$.

:::beweis Calculating with pairs
(i) By [(1.2)](#gl-1-2), $\mathrm{i}\cdot\mathrm{i}=(0,1)\odot(0,1)=(0\cdot0-1\cdot1,\;0\cdot1+0\cdot1)=(-1,0)=-1$.

(ii) For real $y$, $\mathrm{i}y=(0,1)\odot(y,0)=(0\cdot y-1\cdot0,\;0\cdot0+y\cdot1)=(0,y)$, so $x+\mathrm{i}y=(x,0)\oplus(0,y)=(x,y)$. The pair determines $x$ and $y$ uniquely.

(iii) By (ii), the right-hand sides are exactly the pairs from [(1.1)](#gl-1-1) and [(1.2)](#gl-1-2).
:::

::::beispiel
Sum and product of the reference model:

$$z_1+z_2=(3+1)+\mathrm{i}(1+2)=4+3\mathrm{i},\qquad z_1z_2=(3+\mathrm{i})(1+2\mathrm{i})=3+6\mathrm{i}+\mathrm{i}+2\mathrm{i}^2=1+7\mathrm{i}.$$

The pair formula [(1.2)](#gl-1-2) gives the same: $(3\cdot1-1\cdot2,\;3\cdot2+1\cdot1)=(1,7)$. The powers of $\mathrm{i}$ repeat with period 4: $\mathrm{i}^1=\mathrm{i}$, $\mathrm{i}^2=-1$, $\mathrm{i}^3=-\mathrm{i}$, $\mathrm{i}^4=1$. So only the remainder of $n$ on division by 4 counts, for example $\mathrm{i}^{10}=\mathrm{i}^8\,\mathrm{i}^2=-1$.
::::

:::frage Does $\mathrm{i}$ really exist, or is it a calculating trick?
On the number line there is no $\mathrm{i}$; that much of the doubt is right. But $\mathrm{i}$ is the pair $(0,1)$, and [(1.2)](#gl-1-2) is an unambiguous rule for pairs. “Imaginary” is only a historical name.
:::

:::aufgabe Exercise 1 ★ Calculating in standard form
<span class="anker" id="aufg-1"></span>

Bring to the form $x+\mathrm{i}y$: (a) $(4-\mathrm{i})(2+3\mathrm{i})$, (b) $(1+\mathrm{i})^2$ and from it $(1+\mathrm{i})^4$, (c) $\mathrm{i}^{27}+\mathrm{i}^{42}$.

:::loesung
(a) $8+12\mathrm{i}-2\mathrm{i}-3\mathrm{i}^2=11+10\mathrm{i}$. (b) $(1+\mathrm{i})^2=1+2\mathrm{i}+\mathrm{i}^2=2\mathrm{i}$, so $(1+\mathrm{i})^4=(2\mathrm{i})^2=-4$. (c) $27=4\cdot6+3$ gives $\mathrm{i}^{27}=\mathrm{i}^3=-\mathrm{i}$, and $42=4\cdot10+2$ gives $\mathrm{i}^{42}=\mathrm{i}^2=-1$. The sum is $-1-\mathrm{i}$.
:::
:::
