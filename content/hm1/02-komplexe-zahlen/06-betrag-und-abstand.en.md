---
title: Stage 5: Absolute value and distance
pfad: Electrical Engineering / 1st Semester / HöMa1 – Higher Mathematics 1 / Complex Numbers
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Chapter 2: Complex Numbers
order: 1220600
summary: Complex numbers cannot be ordered, but they can be measured.
tags: distance, reverse triangle inequality
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Complex numbers cannot be ordered, but they can be measured. This stage carries distance and absolute value over from [Chapter 1](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) to the plane and shows which rules survive.
:::

**The idea.** In $\mathbb{R}$, $|x|$ measures the distance from the origin. In the plane the Pythagorean theorem takes over: The segment from 0 to $z$ is the hypotenuse of a right triangle with the legs $|x|$ and $|y|$ (Fig. [5](#abb-5), left). The distance between two points is the hypotenuse over the differences of their coordinates. The result is real, so “greater than” is allowed again here.

:::abbildung hm1/k2betrag 5
Left: absolute value and distance as hypotenuses: $|z_1|^2=3^2+1^2$ and $d(z_1,z_2)^2=2^2+1^2$. Right: the triangle inequality: The path via $z_1$ is longer than the direct path to $z_1+z_2$.
:::

:::definition Definition 5.1 (Distance and absolute value)
<span class="anker" id="satz-5-1"></span>

For $z=x+\mathrm{i}y$ and $w=u+\mathrm{i}v$ with real $x,y,u,v$, let

<span class="anker" id="gl-5-1"></span>
$$d(z,w):=\sqrt{(x-u)^2+(y-v)^2},\qquad |z|:=d(z,0)=\sqrt{x^2+y^2}. \tag{5.1}$$
:::

⁠**How to read it:** Under the root stands a real number greater than or equal to zero, and $\sqrt a$ is the nonnegative solution of $b^2=a$ ([Chapter 1](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). The __distance__ $d(z,w)$ depends only on the difference: $d(z,w)=|z-w|$. **Limiting case:** For real $z$, $|z|=\sqrt{x^2}=|x|$, the absolute value from [Chapter 1](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html).

:::satz Theorem 5.2 (Rules for absolute value and distance)
<span class="anker" id="satz-5-2"></span>

For all $z,w,\tilde z\in\mathbb{C}$:

<ol class="rm">

<li>

$|z|\ge0$ and ($|z|=0\Leftrightarrow z=0$), likewise $d(z,w)\ge0$ and ($d(z,w)=0\Leftrightarrow z=w$),

</li>

<li>

$d(z,w)=d(w,z)$ and $|\overline{z}|=|{-z}|=|z|$,

</li>

<li>

$z\overline{z}=|z|^2$, so for $z\ne0$, $1/z=\overline{z}\cdot1/|z|^2$,

</li>

<li>

$|z\cdot w|=|z|\cdot|w|$,

</li>

<li>

$\max\{|\operatorname{Re}(z)|,|\operatorname{Im}(z)|\}\le|z|\le|\operatorname{Re}(z)|+|\operatorname{Im}(z)|$,

</li>

<li>

$|z+w|\le|z|+|w|$ and $d(z,w)\le d(z,\tilde z)+d(\tilde z,w)$ (triangle inequality),

</li>

<li>

$|z-w|\le|z|+|w|$, $\bigl||z|-|w|\bigr|\le|z-w|$ and $\bigl||z|-|w|\bigr|\le|z+w|$ (__reverse triangle inequality__).

</li>

</ol>
:::

⁠**How to read it:** (iv): The absolute value of a product is the product of the absolute values. (v): The hypotenuse is at most as long as both legs together, and each leg is at most as long as the hypotenuse. (vi): A detour via $\tilde z$ is never shorter. **Validity:** The rules hold without restriction, but $|z+w|=|z|+|w|$ is not a rule: Equality occurs when the arrows point in the same direction, as for $z_2$ and $2z_2$: $3\sqrt5=\sqrt5+2\sqrt5$.

:::beweis Rules for the absolute value
(i), (ii): A sum of squares is zero if and only if both squares are zero, and sign changes do not alter it.

(iii): Stage [3](spiegeln-an-der-reellen-achse.html#stufe-3), rule (vi), and [(4.1)](dividieren-und-was-verloren-geht.html#gl-4-1).

(iv): $|zw|^2=zw\,\overline{zw}=z\overline{z}\,w\overline{w}=|z|^2|w|^2$ by (iii) and $\overline{zw}=\overline{z}\,\overline{w}$. Both absolute values are nonnegative, so the root may be taken.

(v): $x^2\le x^2+y^2$ and $y^2\le x^2+y^2$ give the left inequality, $x^2+y^2\le x^2+2|x||y|+y^2=(|x|+|y|)^2$ the right one.

(vi): With (iii) and the conjugation rules,

$$|z+w|^2=(z+w)(\overline{z}+\overline{w})=|z|^2+z\overline{w}+\overline{z}w+|w|^2=|z|^2+2\operatorname{Re}(z\overline{w})+|w|^2,$$

because $\overline{z}w$ is the conjugate of $z\overline{w}$. By (v) and (iv), $\operatorname{Re}(z\overline{w})\le|z\overline{w}|=|z||w|$. So $|z+w|^2\le(|z|+|w|)^2$. The distance form follows from $z-w=(z-\tilde z)+(\tilde z-w)$.

(vii): $-w$ instead of $w$ in (vi) gives the first inequality. From $|z|=|(z-w)+w|\le|z-w|+|w|$ follows $|z|-|w|\le|z-w|$, with the roles swapped $|w|-|z|\le|z-w|$, together the second. $-w$ instead of $w$ in that gives the third.
:::

::::beispiel
$|z_1|=\sqrt{10}\approx3.162$ and $|z_2|=\sqrt5\approx2.236$. The triangle inequality: $|z_1+z_2|=|4+3\mathrm{i}|=5\le5.398$. The product: $|z_1z_2|=|1+7\mathrm{i}|=\sqrt{50}=\sqrt{10}\cdot\sqrt5$. The distance: $d(z_1,z_2)=|2-\mathrm{i}|=\sqrt5$. The reverse inequality: $0.926\le2.236$. Rule (v) for $z_1$: $3\le3.162\le4$.
::::

**Point sets.** Because $|z-c|$ is the distance from $z$ to $c$, $|z-c|=r$ describes the circle about $c$ with radius $r$, and $|z-c|\le r$ the disk. Conditions on $\operatorname{Re}(z)$ or $\operatorname{Im}(z)$ cut out half-planes. Such inequalities are allowed because both sides are real.

:::frage Why is $x^2+y^2$ under the root and not $z^2$?
For real $z$, $|z|=\sqrt{z^2}$, and that is tempting. In $\mathbb{C}$, $z^2$ is in general not real and can be negative, for example $(2\mathrm{i})^2=-4$. The absolute value is meant to be a length, and Pythagoras adds squares of real lengths. The correct form is $|z|=\sqrt{z\overline{z}}$.
:::

:::aufgabe Exercise 6 ★★ Point sets
<span class="anker" id="aufg-6"></span>

Sketch in the complex plane: (a) $\{z:|z-1-\mathrm{i}|\le2\}$, (b) $\{z:|z-2|=|z+2\mathrm{i}|\}$, (c) $\{z:\operatorname{Re}((1+\mathrm{i})z)>1\}$. Hint for (b): Square both sides and substitute $z=x+\mathrm{i}y$.

:::loesung
(a) $|z-(1+\mathrm{i})|\le2$ is the disk about $1+\mathrm{i}$ with radius 2, including the boundary.

(b) $(x-2)^2+y^2=x^2+(y+2)^2$ gives $-4x+4=4y+4$, so $y=-x$. This is the line through the origin with slope $-1$. Geometrically it consists of all points equally far from $2$ and $-2\mathrm{i}$: the perpendicular bisector of the connecting segment.

(c) $(1+\mathrm{i})(x+\mathrm{i}y)=(x-y)+\mathrm{i}(x+y)$. The condition reads $x-y>1$, that is, $y<x-1$. This is the half-plane below the line $y=x-1$, without the line.
:::
:::

:::aufgabe Exercise 7 ★★★ Parallelogram and unit circle
<span class="anker" id="aufg-7"></span>

(a) Show $|z+w|^2+|z-w|^2=2|z|^2+2|w|^2$ and check the equation with $z_1$ and $z_2$. What does it say about the diagonals of the parallelogram? (b) Show: $|z|=1$ implies $1/z=\overline{z}$. Check this with $z=0.6+0.8\mathrm{i}$. (c) Predict where $1/(2z)$ lies for this $z$, and calculate it.

:::loesung
(a) As in the proof of the triangle inequality, $|z\pm w|^2=|z|^2\pm2\operatorname{Re}(z\overline{w})+|w|^2$. On adding, the cross terms drop out. Check: $25+5=30=2\cdot10+2\cdot5$. The squares of the two diagonals of a parallelogram together equal the squares of all four sides.

(b) From $z\overline{z}=|z|^2=1$ follows $1/z=\overline{z}$. For $z=0.6+0.8\mathrm{i}$ we have $|z|^2=0.36+0.64=1$ and $(0.6+0.8\mathrm{i})(0.6-0.8\mathrm{i})=0.36+0.64=1$.

(c) Prediction: Reflect and divide by $|2z|^2=4$, so the reciprocal lies on the arrow of $\overline{z}$ at absolute value $0.5$. Calculation: $1/(2z)=\overline{z}/2=0.3-0.4\mathrm{i}$.
:::
:::
