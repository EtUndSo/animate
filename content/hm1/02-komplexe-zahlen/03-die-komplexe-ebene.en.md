---
title: Stage 2: The complex plane
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Complex Numbers
order: 1220300
summary: A pair is a point.
tags: real axis, imaginary axis, purely imaginary, Gaussian plane
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
A pair is a point. This stage draws the complex numbers in the plane and shows what addition and multiplication by $\mathrm{i}$ mean there.
:::

**The idea.** You plot $x$ to the right and $y$ upward. The horizontal __real axis__ is $\mathbb{R}$; on the vertical __imaginary axis__ lie the __purely imaginary__ numbers $\mathrm{i}y$. Every complex number is a point or, equivalently, an arrow (vector) from the origin to this point. Addition works separately for each coordinate: The arrow of $z_2$ is attached to the tip of $z_1$. Both orders together form a parallelogram, and the sum is its fourth corner (Fig. [2](#abb-2), left). In AC analysis these arrows are called phasors, and voltages add in exactly this way.

:::abbildung hm1/k2ebene 2
Left: $z_1$, $z_2$ and the parallelogram, the real axis in orange: $z_1+z_2=4+3\mathrm{i}$ lies 3 plus 1 to the right and 1 plus 2 up. Right: Each multiplication by $\mathrm{i}$ rotates by $90^\circ$. From $z_1$ come the corners of a square, from $1$ the gray points $\mathrm{i}$, $-1$, $-\mathrm{i}$.
:::

:::definition Definition 2.1 (Real part, imaginary part, Gaussian plane)
<span class="anker" id="satz-2-1"></span>

For $z=x+\mathrm{i}y$ with $x,y\in\mathbb{R}$, $x=:\operatorname{Re}(z)$ is called the real part and $y=:\operatorname{Im}(z)$ the imaginary part of $z$. The complex plane with the coordinates $\operatorname{Re}(z)$ and $\operatorname{Im}(z)$ is also called the __Gaussian plane__. We have $z=w$ if and only if $\operatorname{Re}(z)=\operatorname{Re}(w)$ and $\operatorname{Im}(z)=\operatorname{Im}(w)$.
:::

⁠**How to read it:** Both parts are real: The imaginary part of $3+\mathrm{i}$ is 1, not $\mathrm{i}$. So an equation in $\mathbb{C}$ stands for two real equations. The difference $z-w$ is the arrow from $w$ to $z$, because $w+(z-w)=z$. In the reference model, $z_1-z_2=2-\mathrm{i}$.

:::satz Theorem 2.2 (Multiplication by $\mathrm{i}$)
<span class="anker" id="satz-2-2"></span>

For $z=x+\mathrm{i}y$ we have $\mathrm{i}z=-y+\mathrm{i}x$. The arrow of $z$ is thereby rotated by $90^\circ$ counterclockwise about the origin.
:::

⁠**How to read it:** The point $(x,y)$ becomes $(-y,x)$. Two rotations give the half turn, that is, the sign change: This is the mechanism behind $\mathrm{i}^2=-1$. A quarter turn leaves the number line. That is why $\mathrm{i}$ could not lie on it.

:::beweis Quarter turn
We have $\mathrm{i}(x+\mathrm{i}y)=\mathrm{i}x+\mathrm{i}^2y=-y+\mathrm{i}x$. The arrow of $z$ is the hypotenuse of a right triangle with the horizontal leg $x$ and the vertical leg $y$, both counted with sign. The quarter turn makes $x$ to the right into $x$ upward and $y$ upward into $y$ to the left. So the rotated arrow ends at $(-y,x)$.
:::

::::beispiel
$\mathrm{i}z_1=-1+3\mathrm{i}$, $\mathrm{i}^2z_1=-3-\mathrm{i}=-z_1$, $\mathrm{i}^3z_1=1-3\mathrm{i}$, $\mathrm{i}^4z_1=z_1$ (Fig. [2](#abb-2), right).
::::

⁠**Limiting case:** A real factor $r$ does not rotate, it stretches: $r(x+\mathrm{i}y)=rx+\mathrm{i}ry$. For $r=-1$ it reverses the arrow, like $\mathrm{i}$ applied twice.

:::frage Isn't the complex plane just the ordinary coordinate plane?
As a set and for addition, yes. The difference is multiplication: [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) turns two points into a point again, and this makes division possible (Stage [4](dividieren-und-was-verloren-geht.html#stufe-4)). Only that turns the plane into a number system.
:::

:::aufgabe Exercise 2 ★★ Geometry with numbers
<span class="anker" id="aufg-2"></span>

Given are $P=1+\mathrm{i}$, $Q=4+2\mathrm{i}$, $R=2+4\mathrm{i}$. (a) Compute the fourth corner $S$ of the parallelogram with the sides $PQ$ and $PR$. Show that both diagonals have the same midpoint. (b) Rotate $Q$ about the point $P$ by $90^\circ$ counterclockwise. Hint: The arrow from $P$ to $Q$ is $Q-P$. (c) Limiting case: What does your formula from (b) give for $Q=P$?

:::loesung
(a) From $P$ start the arrows $Q-P=3+\mathrm{i}$ and $R-P=1+3\mathrm{i}$. The fourth corner is $S=P+(Q-P)+(R-P)=Q+R-P=5+5\mathrm{i}$. The midpoints of the diagonals are $(P+S)/2=(6+6\mathrm{i})/2=3+3\mathrm{i}$ and $(Q+R)/2=(6+6\mathrm{i})/2=3+3\mathrm{i}$.

(b) You rotate the arrow $Q-P$ and attach it at $P$ again: $P+\mathrm{i}(Q-P)=1+\mathrm{i}+\mathrm{i}(3+\mathrm{i})=1+\mathrm{i}-1+3\mathrm{i}=4\mathrm{i}$. (c) $P+\mathrm{i}\cdot0=P$: The center of rotation stays where it is.
:::
:::
