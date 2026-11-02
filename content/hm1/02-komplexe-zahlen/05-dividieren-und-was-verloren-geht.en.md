---
title: Stage 4: Division, and what is lost
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Complex Numbers
order: 1220500
summary: Stage 3 provides a real product.
tags: 
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Stage [3](spiegeln-an-der-reellen-achse.html#stufe-3) provides a real product. This stage turns it into division, shows that $\mathbb{C}$ is a field, and explains why the order is missing.
:::

**The idea.** Dividing by a real number is possible: Real part and imaginary part are divided individually. So you multiply the top and bottom of the fraction by the conjugate of the denominator. The value stays the same, the denominator becomes real. In the plane, $1/z$ arises in two steps: reflect across the real axis, then divide by $x^2+y^2$ (Fig. [4](#abb-4)). In exactly this way AC analysis splits fractions of complex impedances into real and imaginary parts.

:::abbildung hm1/k2kehrwert 4
The reciprocal of $z_2$ in two steps: reflect and divide by 5. The reciprocal lies on the arrow of $\overline{z_2}$.
:::

:::satz Theorem 4.1 (Reciprocal and division)
<span class="anker" id="satz-4-1"></span>

For every $z=x+\mathrm{i}y\ne0$ there is the number

<span class="anker" id="gl-4-1"></span>
$$z^{-1}=\frac1z=\frac{\overline{z}}{z\overline{z}}=\frac{x}{x^2+y^2}-\mathrm{i}\,\frac{y}{x^2+y^2}\qquad\text{with}\qquad z\cdot z^{-1}=1. \tag{4.1}$$

For arbitrary $w$, this gives $\dfrac wz=w\cdot z^{-1}=\dfrac{w\,\overline{z}}{x^2+y^2}$.
:::

⁠**How to read it:** The denominator $x^2+y^2$ is real. **Validity:** Because $z\ne0$, either $x\ne0$ or $y\ne0$, so $x^2+y^2>0$. For $z=0$ there is no reciprocal, because $0\cdot w=0\ne1$ for every $w$. **Limiting case:** For $y=0$, [(4.1)](#gl-4-1) becomes the real reciprocal $x/x^2=1/x$.

:::beweis Product with the reciprocal
Let $N:=x^2+y^2>0$. The reciprocal is the pair $(x/N,\,-y/N)$. By [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2),

$$(x,y)\odot\Bigl(\frac xN,\frac{-y}N\Bigr)=\Bigl(\frac{x\cdot x}N-\frac{y\cdot(-y)}N,\;\frac{x\cdot(-y)}N+\frac{y\cdot x}N\Bigr)=\Bigl(\frac{x^2+y^2}N,\;0\Bigr)=(1,0).$$
:::

**Example.** With the reference model, denominator $z_2\overline{z_2}=5$:

$$\frac{z_1}{z_2}=\frac{(3+\mathrm{i})(1-2\mathrm{i})}{(1+2\mathrm{i})(1-2\mathrm{i})}=\frac{3-6\mathrm{i}+\mathrm{i}-2\mathrm{i}^2}{5}=\frac{5-5\mathrm{i}}{5}=1-\mathrm{i}.$$

Check: $(1-\mathrm{i})(1+2\mathrm{i})=1+2\mathrm{i}-\mathrm{i}-2\mathrm{i}^2=3+\mathrm{i}$. Moreover, $1/z_2=(1-2\mathrm{i})/5=0.2-0.4\mathrm{i}$ and $1/\mathrm{i}=-\mathrm{i}$.

:::satz Theorem 4.2 ($\mathbb{C}$ is a field)
<span class="anker" id="satz-4-2"></span>

$\mathbb{C}$ with $+$ and $\cdot$ satisfies all field axioms from [Part 1](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html): commutative, associative and distributive laws, neutral elements $0\ne1$, the negative $-z$ for every $z$ and the reciprocal $1/z$ for every $z\ne0$.
:::

⁠**How to read it:** What follows in [Part 1](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) from the field axioms alone also holds in $\mathbb{C}$: arithmetic with fractions, the binomial formulas and the inference from $zw=0$ to $z=0$ or $w=0$.

:::beweis Idea
Addition works separately and inherits all laws from $\mathbb{R}$, with $-z=-x-\mathrm{i}y$. [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) does not change when the indices 1 and 2 are swapped: Multiplication is commutative. The associative and distributive laws are shown by computing both sides according to [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2). $(1,0)\odot(x,y)=(x,y)$ shows the unit element, [(4.1)](#gl-4-1) the axiom (M4), the reciprocal.
:::

:::satz Theorem 4.3 ($\mathbb{C}$ is not ordered)
<span class="anker" id="satz-4-3"></span>

There is no relation “$>0$” on $\mathbb{C}$ with the order axioms from [Part 1](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html): (T1) For every $x$, exactly one of $x>0$, $x=0$, $-x>0$ holds. (T2) From $x>0$ and $y>0$ follows $x+y>0$. (T3) From $x>0$ and $y>0$ follows $x\cdot y>0$.
:::

⁠**How to read it:** For non-real numbers, $z<w$ and $z>0$ have no meaning. Only real quantities such as $\operatorname{Re}(z)$ or $|z|$ may be compared.

:::beweis Contradiction
Suppose there were such a relation. Then $x\cdot x>0$ would hold for every $x\ne0$: For $x>0$ this follows from (T3), for $-x>0$ from (T3) and $(-x)(-x)=x\cdot x$. In particular, $1\cdot1>0$ and $\mathrm{i}\cdot\mathrm{i}>0$. With (T2) it would follow that $1\cdot1+\mathrm{i}\cdot\mathrm{i}>0$. That is $1+(-1)=0>0$, a contradiction to (T1).
:::

:::frage Couldn't one fix a ranking, say first by the real part, then by the imaginary part?
You can sort that way. It just does not get along with multiplication: It would give $\mathrm{i}>0$, but $\mathrm{i}\cdot\mathrm{i}=-1<0$, against (T3). The proof shows that this hits every possible choice.
:::

:::aufgabe Exercise 4 ★ Dividing
<span class="anker" id="aufg-4"></span>

(a) Bring $\dfrac{7+\mathrm{i}}{2-\mathrm{i}}$ to standard form. (b) Compute $\dfrac{10}{1+3\mathrm{i}}+\dfrac{3-\mathrm{i}}{1+\mathrm{i}}$. (c) Solve $(2+\mathrm{i})z-3=-2+3\mathrm{i}$ and check the result.

:::loesung
(a) $\dfrac{(7+\mathrm{i})(2+\mathrm{i})}{(2-\mathrm{i})(2+\mathrm{i})}=\dfrac{14+7\mathrm{i}+2\mathrm{i}+\mathrm{i}^2}{5}=\dfrac{13+9\mathrm{i}}5=2.6+1.8\mathrm{i}$.

(b) $\dfrac{10(1-3\mathrm{i})}{10}=1-3\mathrm{i}$ and $\dfrac{(3-\mathrm{i})(1-\mathrm{i})}{2}=\dfrac{3-3\mathrm{i}-\mathrm{i}+\mathrm{i}^2}2=\dfrac{2-4\mathrm{i}}2=1-2\mathrm{i}$. The sum is $2-5\mathrm{i}$.

(c) $(2+\mathrm{i})z=1+3\mathrm{i}$, so $z=\dfrac{(1+3\mathrm{i})(2-\mathrm{i})}{5}=\dfrac{2-\mathrm{i}+6\mathrm{i}-3\mathrm{i}^2}5=\dfrac{5+5\mathrm{i}}5=1+\mathrm{i}$. Check: $(2+\mathrm{i})(1+\mathrm{i})-3=1+3\mathrm{i}-3=-2+3\mathrm{i}$.
:::
:::

:::aufgabe Exercise 5 ★★ An attempt to order $\mathbb{C}$
<span class="anker" id="aufg-5"></span>

Someone calls $z$ positive if $\operatorname{Re}(z)>0$. Check (T1), (T2) and (T3) and give a counterexample for each violated axiom.

:::loesung
(T1) is violated: For $\mathrm{i}$ we have $\operatorname{Re}(\mathrm{i})=0$ and $\operatorname{Re}(-\mathrm{i})=0$, so neither $\mathrm{i}$ nor $-\mathrm{i}$ is positive, although $\mathrm{i}\ne0$. (T2) holds, because by Stage [3](spiegeln-an-der-reellen-achse.html#stufe-3), $\operatorname{Re}(z+w)=\operatorname{Re}(z)+\operatorname{Re}(w)>0$. (T3) is violated: $z=1+2\mathrm{i}$ is positive, but $z\cdot z=-3+4\mathrm{i}$ has the real part $-3$. The reason is the term $-y_1y_2$ in the real part of the product.
:::
:::
