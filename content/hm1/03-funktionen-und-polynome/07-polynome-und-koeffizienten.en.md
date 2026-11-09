---
title: Stage 5: Polynomials and coefficients
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Functions and Polynomials
order: 1230700
summary: The general theory is in place.
tags: degree, coefficients, comparing coefficients, quadratic formula, discriminant
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
The general theory is in place. Now comes the most important family of functions: polynomials, built only from addition and multiplication. The first problem is: The same polynomial can look quite different. When are two polynomials equal?
:::

**The idea.** A polynomial is fixed by finitely many numbers. Near $x=0$ you see them one after another: The value at zero is the last number, the slope there the next one, because the higher powers are tiny for small $|x|$ (Fig. [6](#abb-6)). Two polynomials that are equal everywhere must therefore agree number by number.

:::definition Definition 5.1 (Polynomial)
<span class="anker" id="satz-5-1"></span>

A function $f:\mathbb{R}\to\mathbb{R}$ is called a polynomial of __degree__ $n\in\mathbb{N}_0$ if there are real numbers $a_0,\dots,a_n$ with $a_n\neq0$ such that

<span class="anker" id="gl-5-1"></span>
$$f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+a_1x+a_0=\sum_{i=0}^na_ix^i. \tag{5.1}$$

One writes $P_n:=f$ and $\deg P_n:=n$. The numbers $a_0,\dots,a_n$ are called the __coefficients__ of $P_n$.
:::

⁠**How to read it:** The index on $P_n$ names the degree. For all $x$, $x^0=1$, so $a_0$ is the term without $x$. In the reference model $a_3=2$, $a_2=-3$, $a_1=-11$, $a_0=6$; for $S$, $a_1=0$. Always $\mathcal D(f)=\mathbb{R}$, but $\mathcal W(f)$ can be smaller ($x^2$). A constant $c\neq0$ has degree 0. The function $0$ has no such representation and therefore no degree in this definition.

:::satz Theorem 5.2 (Identity theorem for polynomials)
<span class="anker" id="satz-5-2"></span>

Let $P_n(x)=\sum_{k=0}^na_kx^k$ and $Q_n(x)=\sum_{k=0}^nb_kx^k$ be polynomials of degree $\le n$ (so $a_n=0$ or $b_n=0$ is allowed). Then

<span class="anker" id="gl-5-2"></span>
$$P_n(x)=Q_n(x)\text{ for all }x\in\mathbb{R}\quad\Leftrightarrow\quad a_k=b_k\text{ for }k=0,\dots,n. \tag{5.2}$$
:::

:::beweis Identity theorem
“$\Leftarrow$”: Equal coefficients give equal values.

“$\Rightarrow$”: At $x=0$ we get $a_0=b_0$. Subtracting and dividing by $x\neq0$ gives for all $x\neq0$

$$a_1+a_2x+\dots+a_nx^{n-1}=b_1+b_2x+\dots+b_nx^{n-1}.$$

Here you may not substitute $x=0$, because you divided by $x$. Instead you use small $x$: From the equation follows $a_1-b_1=x\bigl[(b_2-a_2)+(b_3-a_3)x+\dots+(b_n-a_n)x^{n-2}\bigr]$. For $0<|x|\le1$, all powers of $|x|$ are at most 1, so the triangle inequality $|u+v|\le|u|+|v|$ gives

$$|a_1-b_1|\le C\,|x|\quad\text{with}\quad C:=\sum_{k=2}^n\bigl(|a_k|+|b_k|\bigr).$$

$C$ depends only on the coefficients, and $|x|$ may be arbitrarily small. So $|a_1-b_1|<\varepsilon$ for every $\varepsilon>0$. A number $a$ with $|a|<\varepsilon$ for all $\varepsilon>0$ is zero, because $|a|>0$ would give, with $\varepsilon=|a|/2$, the contradiction $|a|<|a|/2$. So $a_1=b_1$. Subtracting $a_0+a_1x$ and dividing by $x^2$ likewise gives $a_2=b_2$, and so on up to $a_n=b_n$.
:::

⁠**How to read it:** The theorem is the basis of __comparing coefficients__: To compare two polynomials as functions, you compare their coefficients. Polynomials of different degree are therefore always different. **Why “for all $x$” is needed:** $x^2-x$ and $0$ agree at $x=0$ and $x=1$, but the coefficients do not.

:::abbildung hm1/k3nahnull 6
Left, $P$ at large scale. Right, the section around $x=0$ with the line $a_0+a_1x=6-11x$: At $x=0.1$ it deviates by only 0.028; near zero the higher powers hardly matter.
:::

::::beispiel
When is $ax^2+bx+c=a(x-x_1)(x-x_2)$ for all $x$? Multiplying out gives $ax^2-a(x_1+x_2)x+ax_1x_2$ on the right, so comparing coefficients gives

<span class="anker" id="gl-5-3"></span>
$$b=-a(x_1+x_2),\qquad c=a\,x_1x_2. \tag{5.3}$$

For $a\neq0$ and $D:=b^2-4ac\ge0$, these two equations are solved by the __quadratic formula__

<span class="anker" id="gl-5-4"></span>
$$x_{1}=\frac{-b+\sqrt D}{2a},\qquad x_{2}=\frac{-b-\sqrt D}{2a}. \tag{5.4}$$

Substituting confirms it: $-a(x_1+x_2)=-a\cdot\frac{-2b}{2a}=b$ and $ax_1x_2=\frac{1}{4a}\bigl(b^2-D\bigr)=c$. The number $D$ is called the __discriminant__. For $Q$, $D=1+8=9$, so $x_{1}=2$, $x_{2}=-1$, and $x_1+x_2=1=-b/a$, $x_1x_2=-2=c/a$.
::::

⁠**Limiting cases:** $D=0$ gives $x_1=x_2$. For $D<0$ there is no real zero, because then $ax^2+bx+c=a\bigl[(x+\frac{b}{2a})^2-\frac{D}{4a^2}\bigr]$, and the bracket is positive. So $x^2+\beta x+\gamma$ has no real zero if and only if $\beta^2-4\gamma<0$.

:::frage Why doesn't the proof simply substitute $x=0$ after dividing by $x$? There is a polynomial there again, after all.
There are polynomials on the left and right, that is true. But the equation was derived only for $x\neq0$, and nothing about the point 0 follows from that immediately. The detour via small $|x|$ closes exactly this gap. Part 5 gives the concept behind it the name continuity.
:::

:::aufgabe Exercise 6 ★★ Comparing coefficients
<span class="anker" id="aufg-6"></span>

(a) Determine $a,b,c$ such that $2x^2-x+3=a(x-1)^2+b(x-1)+c$ for all $x$. (b) Let $x^3+a_2x^2+a_1x+a_0$ have the zeros $-1$, $2$, $4$. Determine the coefficients by multiplying out and express them in terms of the zeros.

:::loesung
(a) On the right stands $ax^2+(b-2a)x+(a-b+c)$. Comparison: $a=2$, $b-4=-1$, so $b=3$, and $2-3+c=3$, so $c=4$. (b) $(x+1)(x-2)(x-4)=x^3-5x^2+2x+8$. So $a_2=-5=-(x_1+x_2+x_3)$, $a_1=2=x_1x_2+x_1x_3+x_2x_3$, $a_0=8=-x_1x_2x_3$.
:::
:::
