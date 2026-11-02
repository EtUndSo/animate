---
title: Stage 3: Reflecting across the real axis
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Complex Numbers
order: 1220400
summary: You cannot yet divide by x+iy .
tags: 
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
You cannot yet divide by $x+\mathrm{i}y$. This stage introduces the mirror image of $z$, which turns any number into a real one by multiplication, and collects the rules of arithmetic.
:::

**The idea.** $-\mathrm{i}$ also solves $x^2=-1$, because $(-\mathrm{i})^2=\mathrm{i}^2=-1$. The rules of arithmetic cannot tell $\mathrm{i}$ and $-\mathrm{i}$ apart. That is why a correct calculation stays correct when $\mathrm{i}$ is swapped for $-\mathrm{i}$ everywhere. In the plane this swap is the reflection across the real axis (Fig. [3](#abb-3)). If you multiply $z$ by its mirror image, the cross terms with $\mathrm{i}$ cancel.

:::abbildung hm1/k2konjugiert 3
$z_1$ and its mirror image $\overline{z_1}$. The sum lies on the real axis because the imaginary parts cancel, the difference on the imaginary axis because the real parts cancel.
:::

:::definition Definition 3.1 (Complex conjugate)
<span class="anker" id="satz-3-1"></span>

For $z=x+\mathrm{i}y$, the number $\overline{z}:=x-\mathrm{i}y\in\mathbb{C}$ is called the conjugate of $z$.
:::

:::satz Theorem 3.2 (Rules of arithmetic in $\mathbb{C}$)
<span class="anker" id="satz-3-2"></span>

For all $z=x+\mathrm{i}y$ and $w=u+\mathrm{i}v$ with real $x,y,u,v$:

<ol class="rm">

<li>

$\operatorname{Re}(z+w)=\operatorname{Re}(z)+\operatorname{Re}(w)$,

</li>

<li>

$\operatorname{Im}(z+w)=\operatorname{Im}(z)+\operatorname{Im}(w)$,

</li>

<li>

$\overline{z+w}=\overline{z}+\overline{w}$,

</li>

<li>

$\overline{z\cdot w}=\overline{z}\cdot\overline{w}$,

</li>

<li>

$\overline{\overline{z}}=z$,

</li>

<li>

$z\overline{z}=x^2+y^2$, so $\operatorname{Im}(z\overline{z})=0$ and $\operatorname{Re}(z\overline{z})=x^2+y^2$,

</li>

<li>

$z+\overline{z}=2\operatorname{Re}(z)$ and $z-\overline{z}=2\mathrm{i}\operatorname{Im}(z)$.

</li>

</ol>
:::

⁠**How to read it:** Real part, imaginary part and conjugation may be pulled into sums. Conjugation may also be pulled into products; that is the swap $\mathrm{i}\leftrightarrow-\mathrm{i}$. The real part may not: $\operatorname{Re}(z_1z_2)=1$, but $\operatorname{Re}(z_1)\operatorname{Re}(z_2)=3$, because $-y_1y_2$ also enters the real part of the product. In electrical engineering, $z^*$ is often written instead of $\overline{z}$.

:::beweis Rules of arithmetic
(i), (ii): Addition works separately, $z+w=(x+u)+\mathrm{i}(y+v)$.

(iii): $\overline{z+w}=(x+u)-\mathrm{i}(y+v)=(x-\mathrm{i}y)+(u-\mathrm{i}v)$.

(iv): By [(1.3)](paare-statt-einzelner-zahlen.html#gl-1-3), $zw=(xu-yv)+\mathrm{i}(xv+uy)$, so $\overline{zw}=(xu-yv)-\mathrm{i}(xv+uy)$. The same formula with $-y$ and $-v$ gives $\overline{z}\,\overline{w}=(xu-yv)+\mathrm{i}(-xv-uy)$. The two agree.

(v): Change the sign of $y$ twice.

(vi): $(x+\mathrm{i}y)(x-\mathrm{i}y)=x^2-\mathrm{i}xy+\mathrm{i}xy-\mathrm{i}^2y^2=x^2+y^2$.

(vii): $(x+\mathrm{i}y)+(x-\mathrm{i}y)=2x$ and $(x+\mathrm{i}y)-(x-\mathrm{i}y)=2\mathrm{i}y$.
:::

**Example.** For $z_1$, we have $\overline{z_1}=3-\mathrm{i}$, $z_1\overline{z_1}=9+1=10$, $z_1+\overline{z_1}=6=2\cdot3$ and $z_1-\overline{z_1}=2\mathrm{i}=2\mathrm{i}\cdot1$. Check of (iv): $\overline{z_1z_2}=1-7\mathrm{i}$ and $\overline{z_1}\,\overline{z_2}=(3-\mathrm{i})(1-2\mathrm{i})=3-6\mathrm{i}-\mathrm{i}+2\mathrm{i}^2=1-7\mathrm{i}$. **Limiting case:** For $y=0$, $\overline{z}=z$ and $z\overline{z}=x^2$. Real numbers lie on the mirror axis and do not change.

:::frage Isn't $z\overline{z}$ the same as $z^2$?
Only for real $z$. In $z^2$ the cross terms add up to $2\mathrm{i}xy$; in $z\overline{z}$ they cancel. In the reference model, $z_2^2=-3+4\mathrm{i}$, but $z_2\overline{z_2}=5$.
:::

:::aufgabe Exercise 3 ★ Real or purely imaginary?
<span class="anker" id="aufg-3"></span>

Let $z=2-5\mathrm{i}$. (a) Predict without calculating which of the numbers $z+\overline{z}$, $z-\overline{z}$, $z\overline{z}$, $z^2+\overline{z}^2$, $(z-\overline{z})^2$ are real and which are purely imaginary. Then calculate them. (b) Show for every $z\in\mathbb{C}$: $z$ is real if and only if $\overline{z}=z$, and purely imaginary if and only if $\overline{z}=-z$.

:::loesung
(a) Prediction: $z+\overline{z}$ is real, $z-\overline{z}$ purely imaginary, $z\overline{z}$ real, $z^2+\overline{z}^2=z^2+\overline{z^2}$ real (sum of a number and its mirror image), $(z-\overline{z})^2$ real (square of a purely imaginary number). Calculation: $z+\overline{z}=4$, $z-\overline{z}=-10\mathrm{i}$, $z\overline{z}=4+25=29$. With $z^2=4-20\mathrm{i}+25\mathrm{i}^2=-21-20\mathrm{i}$ we get $z^2+\overline{z}^2=-42$, and $(z-\overline{z})^2=(-10\mathrm{i})^2=-100$.

(b) By rule (vii) from Stage [3](#stufe-3), $\overline{z}=z$ is equivalent to $2\mathrm{i}\operatorname{Im}(z)=0$, that is, to $\operatorname{Im}(z)=0$. Likewise, $\overline{z}=-z$ is equivalent to $2\operatorname{Re}(z)=0$, that is, to $\operatorname{Re}(z)=0$.
:::
:::
