---
title: Stage 6: Quadratic equations
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Complex Numbers
order: 1220700
summary: The goal was a solution of x 2=-1 .
tags: double solution, discriminant, polar representation
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
The goal was a solution of $x^2=-1$. This stage shows that $\mathbb{C}$ achieves more: Every quadratic equation is solvable there, even with complex coefficients.
:::

**The idea.** Completing the square uses only field axioms and therefore works in $\mathbb{C}$. What remains is an equation $w^2=D$. In $\mathbb{R}$ it fails for $D<0$. In $\mathbb{C}$ it never fails: $w^2=D$ splits into real part and imaginary part, that is, into two real equations for the two real unknowns of $w$.

:::satz Theorem 6.1 (Square roots in $\mathbb{C}$)
<span class="anker" id="satz-6-1"></span>

Let $D=s+\mathrm{i}t\ne0$ with $s,t\in\mathbb{R}$. For $w=u+\mathrm{i}v$ with real $u,v$, the equation $w^2=D$ is equivalent to $u^2-v^2=s$ and $2uv=t$. There are exactly two solutions $\pm w$, namely with

<span class="anker" id="gl-6-1"></span>
$$u^2=\frac{|D|+s}2,\qquad v^2=\frac{|D|-s}2. \tag{6.1}$$

The signs of $u$ and $v$ must be chosen so that $2uv=t$ holds. For $D=0$, $w=0$ is the only solution.
:::

⁠**How to read it:** $s$ and $t$ are the real part and imaginary part of $D$. If $t>0$, $u$ and $v$ have the same sign; if $t<0$, opposite signs. **Limiting case:** For real $D<0$, $u=0$ and $v^2=-D$: The solutions are purely imaginary, so for $D=-1$ they are $w=\pm\mathrm{i}$.

:::beweis Two real equations
We have $w^2=u^2-v^2+2\mathrm{i}uv$. Comparing real part and imaginary part gives the two equations. From $|w|^2=|w^2|=|D|$ it also follows that $u^2+v^2=|D|$. Adding and subtracting with $u^2-v^2=s$ gives [(6.1)](#gl-6-1). The right-hand sides are nonnegative, because $|s|\le|D|$ (Stage [5](betrag-und-abstand.html#stufe-5), rule (v)). Conversely, $u,v$ from [(6.1)](#gl-6-1) satisfy the equation $u^2-v^2=s$ and $(2uv)^2=(|D|+s)(|D|-s)=|D|^2-s^2=t^2$. So $2uv=\pm t$, and the choice of signs fixes $2uv=t$.
:::

:::satz Theorem 6.2 (Quadratic equation in $\mathbb{C}$)
<span class="anker" id="satz-6-2"></span>

Let $p,q\in\mathbb{C}$ and $D:=p^2/4-q$. The equation $z^2+pz+q=0$ has the solutions

<span class="anker" id="gl-6-2"></span>
$$z=-\frac p2\pm w\qquad\text{with}\qquad w^2=D. \tag{6.2}$$

For $D\ne0$ these are two solutions $z_+\ne z_-$ with $z_++z_-=-p$ and $z_+z_-=q$. For $D=0$ there is only $z=-p/2$, a __double solution__. For real $p,q$: $D>0$ gives two real solutions, $D=0$ one real solution, $D<0$ the mutually conjugate solutions $z=-\frac p2\pm\mathrm{i}\sqrt{-D}$.
:::

⁠**How to read it:** $D$ is called the __discriminant__. The solutions lie point-symmetrically about the center $-p/2$ (Fig. [6](#abb-6)). **Validity:** The coefficient of $z^2$ must be 1. Otherwise divide by it first; in $\mathbb{C}$ this also works with a complex coefficient $\ne0$. Real equations of this kind describe oscillations: A conjugate pair of solutions stands for a damped oscillation.

:::herleitung Completing the square
We have $z^2+pz+q=(z+\frac p2)^2-\frac{p^2}4+q=(z+\frac p2)^2-w^2=(z+\frac p2-w)(z+\frac p2+w)$. A product is zero only if one factor is zero (Stage [4](dividieren-und-was-verloren-geht.html#stufe-4)). This gives [(6.2)](#gl-6-2), and it follows that $z_++z_-=-p$ and $z_+z_-=\frac{p^2}4-w^2=q$. For real $p,q$, $D$ is real, and for $D<0$, $w=\pm\mathrm{i}\sqrt{-D}$.
:::

:::abbildung hm1/k2loesungen 6
Left: the real equation of the reference model: The solutions $3\pm\mathrm{i}$ are mirror images. Right: the complex equation: $z_1$ and $z_2$ lie symmetrically about the center $2+1.5\mathrm{i}$.
:::

::::beispiel [Example 1] real coefficients
$z^2-6z+10=0$ has $p=-6$, $q=10$, $D=9-10=-1$, so $z=3\pm\mathrm{i}$. These are $z_1$ and $\overline{z_1}$. Check: sum $6=-p$, product $|z_1|^2=10=q$.
::::

::::beispiel [Example 2] complex coefficients
For $z^2-(4+3\mathrm{i})z+1+7\mathrm{i}=0$ we have $-p/2=2+1.5\mathrm{i}$ and

$$D=(2+1.5\mathrm{i})^2-(1+7\mathrm{i})=1.75+6\mathrm{i}-1-7\mathrm{i}=0.75-\mathrm{i}.$$

So $s=0.75$, $t=-1$ and $|D|=\sqrt{0.5625+1}=1.25$. From [(6.1)](#gl-6-1) follow $u^2=1$ and $v^2=0.25$. Because $t<0$, $u$ and $v$ have opposite signs: $w=\pm(1-0.5\mathrm{i})$. Thus $z=2+1.5\mathrm{i}\pm(1-0.5\mathrm{i})$, that is, $z=3+\mathrm{i}$ or $z=1+2\mathrm{i}$. Check: sum $4+3\mathrm{i}=-p$, product $1+7\mathrm{i}=q$.
::::

⁠**Limiting case:** For $q=0$, [(6.2)](#gl-6-2) gives $z=-p/2\pm p/2$, so $z=0$ and $z=-p$, matching $z(z+p)=0$.

:::frage Why can't you calculate $\sqrt{-1}\cdot\sqrt{-1}=\sqrt{(-1)(-1)}=1$?
The rule $\sqrt{ab}=\sqrt a\sqrt b$ from [Part 1](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) holds only for $a,b\ge0$. For negative numbers the root is not defined: $w^2=-1$ has two solutions of equal standing, and neither of them is “the” root. That is why this chapter writes $w^2=D$ and not $w=\sqrt D$.
:::

:::aufgabe Exercise 8 ★★ Solving quadratic equations
<span class="anker" id="aufg-8"></span>

(a) Solve $z^2+4z+13=0$ and check sum and product. (b) $z^2+pz+q=0$ with real $p,q$ has the solution $2-5\mathrm{i}$. What is the second solution, and what are $p$ and $q$? (c) Solve $z^2-3z+3-\mathrm{i}=0$ and check the result. (d) Solve $\mathrm{i}z^2+2z-2\mathrm{i}=0$.

:::loesung
(a) $D=4-13=-9$, so $z=-2\pm3\mathrm{i}$. Sum $-4=-p$, product $4+9=13=q$. (b) With real coefficients the second solution is the conjugate one, $2+5\mathrm{i}$. Then $p=-(2-5\mathrm{i})-(2+5\mathrm{i})=-4$ and $q=(2-5\mathrm{i})(2+5\mathrm{i})=29$.

(c) $p=-3$, $q=3-\mathrm{i}$, so $D=2.25-3+\mathrm{i}=-0.75+\mathrm{i}$. With $|D|=\sqrt{0.5625+1}=1.25$, [(6.1)](#gl-6-1) gives $u^2=0.25$ and $v^2=1$. Because $t=1>0$, $u$ and $v$ have the same sign: $w=\pm(0.5+\mathrm{i})$. So $z=1.5\pm(0.5+\mathrm{i})$, that is, $z=2+\mathrm{i}$ or $z=1-\mathrm{i}$. Check: sum $3=-p$, product $(2+\mathrm{i})(1-\mathrm{i})=2-2\mathrm{i}+\mathrm{i}-\mathrm{i}^2=3-\mathrm{i}=q$.

(d) First bring the coefficient of $z^2$ to 1: Dividing by $\mathrm{i}$ with $1/\mathrm{i}=-\mathrm{i}$ gives $z^2-2\mathrm{i}z-2=0$. So $p=-2\mathrm{i}$, $q=-2$ and $D=(-2\mathrm{i})^2/4+2=-1+2=1$. With $w=\pm1$ it follows that $z=\mathrm{i}\pm1$. Check for $z=1+\mathrm{i}$: $\mathrm{i}\cdot2\mathrm{i}+2+2\mathrm{i}-2\mathrm{i}=-2+2=0$. Check for $z=-1+\mathrm{i}$: $\mathrm{i}\cdot(-2\mathrm{i})-2+2\mathrm{i}-2\mathrm{i}=2-2=0$.
:::
:::

**Outlook.** A point of the plane can also be specified by absolute value and angle. Then multiplication multiplies the absolute values and adds the angles; the rotation from Stage [2](die-komplexe-ebene.html#stufe-2) is the special case $|\mathrm{i}|=1$ and angle $90^\circ$. This __polar representation__, the exponential form and the $n$th roots need sine, cosine and the exponential function and therefore follow in Part 7.
