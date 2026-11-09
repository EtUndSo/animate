---
title: Stage 3: Field axioms
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Sets, Logic and Real Numbers
order: 1210500
summary: Which few rules for plus and times must be assumed so that all other rules of arithmetic become provable?
tags: operation, distributive law, difference, quotient
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
Which few rules for plus and times must be assumed so that all other rules of arithmetic become provable?
:::

**The idea.** Each number system arises because an equation has no solution in the previous one (Fig. [3](#abb-3)): $x+3=1$ has no solution in $\mathbb{N}$, $3x=1$ none in $\mathbb{Z}$. A field is the system in which both types of equation are always solvable: Plus and times can be reversed. The axioms demand no more. The only link between plus and times is the distributive law, and almost all proofs in this stage run through it.

:::abbildung hm1/k1zahlbereiche 3
Each equation only becomes solvable in the system in which it stands.
:::

:::definition Definition 3.1 (Field)
<span class="anker" id="satz-3-1"></span>

An __operation__ assigns to any two elements an element of the same set. A set $\mathbb K$ with two operations “$+$” and “$\cdot$” is called a field if for all $x,y,z\in\mathbb K$:

|  | Addition | Multiplication |
|---|---|---|
| commutative | (A1) $x+y=y+x$ | (M1) $x\cdot y=y\cdot x$ |
| associative | (A2) $x+(y+z)=(x+y)+z$ | (M2) $x\cdot(y\cdot z)=(x\cdot y)\cdot z$ |
| neutral element | (A3) There is $0\in\mathbb K$ with $x+0=x$ for all $x$. | (M3) There is $1\in\mathbb K$ with $x\cdot1=x$ for all $x$. |
| inverse element | (A4) For every $x$ there is $y$ with $x+y=0$, written $-x$. | (M4) For every $x\ne0$ there is $y$ with $x\cdot y=1$, written $x^{-1}$ or $\frac1x$. |

In addition there are (AM) $x\cdot(y+z)=(x\cdot y)+(x\cdot z)$ (__distributive law__) and (NNE) $0\ne1$.
:::

⁠**How to read it:** Here $0$ and $1$ are just names for two distinguished elements. Minus and divided-by are not separate operations: $x-y:=x+(-y)$ and $\frac yx:=y\cdot x^{-1}$. By agreement, multiplication comes before addition, and $xy:=x\cdot y$. Whatever follows from the axioms holds in every field, hence also for the complex numbers in [Part 2](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). Examples are $\mathbb{Q}$ and $\mathbb{R}$. $\mathbb{N}$ is not a field (no 0, no $-1$), nor is $\mathbb{Z}$ (2 has no inverse). The smallest field is $\{0,1\}$ with $1+1=0$, the addition of digital electronics (XOR). **Why the hypotheses:** Without (NNE), $\{0\}$ would be a field. Without $x\ne0$ in (M4), we would get $1=0\cdot0^{-1}=0$ by (iii) below.

:::satz Theorem 3.2 (Rules of arithmetic in a field)
<span class="anker" id="satz-3-2"></span>

For all $x,y,z,u,v\in\mathbb K$:

<ol class="rm">

<li>

Inverses are unique: $(xy=1\wedge xz=1)\Rightarrow y=z$ and $(x+y=0\wedge x+z=0)\Rightarrow y=z$.

</li>

<li>

Equations are uniquely solvable: $x+z=y$ has exactly the solution $z=y-x$ (__difference__). $xz=y$ has, for $x\ne0$, exactly the solution $z=y\cdot x^{-1}=\frac yx$ (__quotient__).

</li>

<li>

$x\cdot0=0$, and for $x\ne0$, $(x^{-1})^{-1}=x$.

</li>

<li>

$-(-x)=x$ and $(-x)(-y)=xy$.

</li>

<li>

$xy=0\Rightarrow(x=0\vee y=0)$.

</li>

<li>

For $u,v\ne0$, $\frac xu\cdot\frac yv=\frac{xy}{uv}$ and $\frac xu+\frac yv=\frac{xv+yu}{uv}$, and for $u,v,y\ne0$, $\frac xu:\frac yv=\frac{xv}{uy}$.

</li>

</ol>
:::

⁠**How to read it:** Only (i) makes the notations $-x$ and $x^{-1}$ meaningful: If there were two inverses, one would not know which is meant. (v) is the reason why one factors an equation and sets each factor to zero. **Why $x\ne0$:** $0\cdot z=1$ has no solution by (iii), and $0\cdot z=0$ has every $z$ as a solution. Division by zero fails on existence or on uniqueness.

:::beweis Rules of arithmetic, each step with its axiom
(i) From $xy=xz$ (both are 1), multiplying by $y$ gives $(xy)y=(xz)y$. On the left stands $1\cdot y=y$ (M1, M3). On the right: $(xz)y\overset{\text{M2}}{=}x(zy)\overset{\text{M1}}{=}x(yz)\overset{\text{M2}}{=}(xy)z=1\cdot z=z$. For addition it works the same way (Exercise [4](#aufg-4)).

(ii) Existence: $x(yx^{-1})=x(x^{-1}y)=(xx^{-1})y=1\cdot y=y$ (M1, M2, M4, M3). Uniqueness: From $xz=x\tilde z$, multiplying by $x^{-1}$ gives $z=\tilde z$ via the same axioms. For addition likewise with $-x$.

(iii) $x\cdot0\overset{\text{A3}}{=}(x\cdot0)+0\overset{\text{A4}}{=}(x\cdot0)+\bigl((x\cdot0)+(-(x\cdot0))\bigr)\overset{\text{A2}}{=}\bigl((x\cdot0)+(x\cdot0)\bigr)+(-(x\cdot0))\overset{\text{AM}}{=}x\cdot(0+0)+(-(x\cdot0))\overset{\text{A3}}{=}(x\cdot0)+(-(x\cdot0))\overset{\text{A4}}{=}0$. For $x\ne0$, $x^{-1}\ne0$ (indirectly: $x^{-1}=0$ would imply $1=xx^{-1}=x\cdot0=0$, contradicting NNE). So $x^{-1}$ has an inverse. We have $(x^{-1})^{-1}x^{-1}=1$ and $x\,x^{-1}=1$; by (i), $x$ and $(x^{-1})^{-1}$ agree.

(iv) $x$ and $-(-x)$ are both additive inverses of $-x$, so they are equal by (i). Further, $x+(-1)x=(1+(-1))x=0\cdot x=0$, so $(-1)x=-x$. From $(-1)+(-1)(-1)=(-1)(1+(-1))=(-1)\cdot0=0$ it follows likewise that $(-1)(-1)$ is inverse to $-1$, so $(-1)(-1)=-(-1)=1$. Thus $(-x)(-y)=(-1)(-1)xy=xy$.

(v) If $x\ne0$, then $y=x^{-1}(xy)=x^{-1}\cdot0=0$.

(vi) $\frac xu\cdot\frac yv=(xu^{-1})(yv^{-1})=(xy)(u^{-1}v^{-1})$, and $u^{-1}v^{-1}=(uv)^{-1}$, because $(u^{-1}v^{-1})(uv)=1$ and the inverse is unique. The division rule follows with $(y v^{-1})^{-1}=y^{-1}v$, the sum rule by expanding: $\frac xu=\frac{xv}{uv}$, $\frac yv=\frac{yu}{uv}$, then (AM).
:::

::::beispiel
$(-3)(-5)=15$, $\frac23+\frac57=\frac{14+15}{21}=\frac{29}{21}$, $\frac34:\frac58=\frac{3\cdot8}{4\cdot5}=\frac65$.
::::

⁠**Limiting case** $v=u=1$: The sum rule becomes $x+y=x+y$.

:::frage I know this from school. Why a proof?
They are familiar for $\mathbb{Q}$ and $\mathbb{R}$. But they are not among the axioms, and only the proof shows where they hold: in every field. The school rule “squares are not negative,” by contrast, does not follow from this list and fails in [Part 2](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html). Besides, you practice reasoning on content whose result you already know.
:::

:::aufgabe Exercise 4 ★★ Proving in a field
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Show: $(x+y=0\wedge x+z=0)\Rightarrow y=z$. Give the axiom for each step.

</li>

<li>

Show $(x+y)(x-y)=x^2-y^2$ and state where (AM) and (M1) are needed.

</li>

<li>

In the field $\{0,1\}$ with $1+1=0$ and $1\cdot1=1$: What is $-1$? Check $(-1)(-1)=1$.

</li>

</ol>

:::loesung
(a) From $x+y=0=x+z$ it follows that $(-x)+(x+y)=(-x)+(x+z)$. With (A2), (A1), (A4) this becomes $0+y=0+z$, with (A1), (A3) it becomes $y=z$. (b) (AM) and (M1): $(x+y)(x-y)=(x+y)x+(x+y)(-y)=x^2+yx-xy-y^2=x^2-y^2$, where $yx=xy$ by (M1) and $(x+y)(-y)=-(x+y)y$ by $(-1)x=-x$. (c) $1+1=0$ means $-1=1$. Then $(-1)(-1)=1\cdot1=1$. That is the rule from Theorem [3.2](#satz-3-2); it holds in every field.
:::
:::
