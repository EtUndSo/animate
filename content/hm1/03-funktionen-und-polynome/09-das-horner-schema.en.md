---
title: Stage 7: The Horner scheme
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Functions and Polynomials
order: 1230900
summary: For the divisor x-x 0 the division is so regular that a scheme with three rows is enough.
tags: Horner form
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
For the divisor $x-x_0$ the division is so regular that a scheme with three rows is enough. At the same time it delivers the value $P(x_0)$ with only $n$ multiplications. That is why computers usually evaluate polynomials this way.
:::

**The idea.** If you compute $P_n(x_0)$ as written, you need $n-1$ multiplications for $x_0^2,\dots,x_0^n$, $n$ more for the coefficients, and $n$ additions, in total $2n-1$ multiplications. If you repeatedly factor out $x$, each power comes out by itself, and $n$ multiplications are enough. For $n=10$ that is 10 instead of 19.

:::definition Definition 7.1 (Horner form)
<span class="anker" id="satz-7-1"></span>

Repeatedly factoring out $x$ turns [(5.1)](polynome-und-koeffizienten.html#gl-5-1) into the __Horner form__

<span class="anker" id="gl-7-1"></span>
$$P_n(x)=\Bigl\{\Bigl[\cdots\bigl(\underbrace{\{a_nx+a_{n-1}\}}_{=\,c_{n-1}(x)}\cdot x+a_{n-2}\bigr)\cdot x+\dots+a_2\Bigr]\cdot x+a_1\Bigr\}\cdot x+a_0. \tag{7.1}$$

Read from the inside out, $c_n(x)=a_n$, $c_i(x)=c_{i+1}(x)\,x+a_i$ and at the end $c_0(x)=P_n(x)$.
:::

:::satz Theorem 7.2 (Horner at $x_0$)
<span class="anker" id="satz-7-2"></span>

Let $P_n(x)=\sum_{k=0}^na_kx^k$ be a polynomial of degree $n\ge1$ and $x_0\in\mathbb{R}$ fixed. Set

<span class="anker" id="gl-7-2"></span>
$$c_n:=a_n,\qquad c_i:=c_{i+1}\,x_0+a_i\quad\text{for }i=n-1,n-2,\dots,0. \tag{7.2}$$

Then

<span class="anker" id="gl-7-3"></span>
$$c_0=P_n(x_0),\qquad P_n(x)=(x-x_0)\,Q_{n-1}(x)+c_0 \tag{7.3}$$

with $Q_{n-1}(x):=c_nx^{n-1}+c_{n-1}x^{n-2}+\dots+c_2x+c_1$ and $\deg Q_{n-1}=n-1$.
:::

:::beweis Horner
$c_0=P_n(x_0)$: The recursion [(7.2)](#gl-7-2) computes [(7.1)](#gl-7-1) at $x=x_0$ from the inside out. For the second equation, multiply out and sort by powers:

$$(x-x_0)\bigl[c_nx^{n-1}+\dots+c_1\bigr]+c_0=c_nx^n+(c_{n-1}-x_0c_n)x^{n-1}+\dots+(c_1-x_0c_2)x+(c_0-x_0c_1).$$

By [(7.2)](#gl-7-2), $c_n=a_n$ and every parenthesis $c_i-x_0c_{i+1}=a_i$, so the right side is $P_n(x)$. Because $c_n=a_n\neq0$, the degree of $Q_{n-1}$ is exactly $n-1$.
:::

⁠**How to read it:** The $c_i$ are intermediate results of the computation and at the same time the coefficients of the quotient. That is why one computation delivers both. The scheme arranges them like this:

|  | $a_n$ | $a_{n-1}$ | $a_{n-2}$ | $\cdots$ | $a_1$ | $a_0$ |
|---|---|---|---|---|---|---|
| $x_0$ |  | $c_nx_0$ | $c_{n-1}x_0$ | $\cdots$ | $c_2x_0$ | $c_1x_0$ |
|  | $c_n$ | $c_{n-1}$ | $c_{n-2}$ | $\cdots$ | $c_1$ | $c_0$ |

The first row contains all coefficients, including the zeros. You write $a_n$ down, multiply by $x_0$, write the result in the next column, add, and so on.

:::abbildung hm1/k3horner 8
Horner scheme for $P$ at $x_0=2$. The arrows show the sequence: times 2, then add. Last number: $P(2)=-12$. The numbers before it are the coefficients of the quotient: $P(x)=(x-2)(2x^2+x-9)-12$.
:::

**Example.** Fig. [8](#abb-8) computes $P(2)=-12$ with 3 multiplications; directly: $2\cdot8-3\cdot4-11\cdot2+6=-12$. For $x_0=3$ the bottom row is $2,\ 3,\ -2,\ 0$: So $P(3)=0$ and $P(x)=(x-3)(2x^2+3x-2)$. **Limiting cases:** For $x_0=0$ the bottom row is the top row, $c_0=a_0=P(0)$. For $x_0=1$ the scheme adds all coefficients, $c_0=2-3-11+6=-6=P(1)$. Repeating the scheme with the quotient produces the representation in powers of $x-x_0$ (Exercise [8](#aufg-8)).

:::frage Why must the zero for a missing power go into the scheme?
Each column belongs to a power; the scheme counts the powers through the columns. If you omit the zero for $x$ in $S$, it computes with $1,-3,1,4$, that is, with $x^3-3x^2+x+4$. At $x_0=2$ it then gives 2 instead of $S(2)=0$.
:::

:::aufgabe Exercise 8 ★ Computing with Horner
<span class="anker" id="aufg-8"></span>

(a) For $3x^4-2x^3+5x-7$, compute the value at $x_0=-2$ and the quotient. (b) How many multiplications does the scheme save for degree 20? (c) Write $P$ in the form $d_3(x-1)^3+d_2(x-1)^2+d_1(x-1)+d_0$. Hint: Apply the scheme repeatedly at $x_0=1$; $d_0$ is the first remainder, $d_1$ the second.

:::loesung
(a) Top row $3,-2,0,5,-7$ with the zero for $x^2$, bottom row $3,-8,16,-27,47$. So the value is 47 (directly: $48+16-10-7=47$), the quotient $3x^3-8x^2+16x-27$. (b) $2\cdot20-1=39$ against 20: 19 multiplications fewer, almost half. (c) At $x_0=1$: $2,-1,-12,-6$; then for the quotient: $2,1,-11$; then $2,3$. So $d_0=-6$, $d_1=-11$, $d_2=3$, $d_3=2$. Check at $x=0$: $-2+3+11-6=6=P(0)$.
:::
:::
