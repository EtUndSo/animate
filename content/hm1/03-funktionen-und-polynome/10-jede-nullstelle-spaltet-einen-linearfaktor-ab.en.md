---
title: Stage 8: Every zero splits off a linear factor
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Functions and Polynomials
order: 1231000
summary: Now the question from the beginning can be answered: Why does a factor belong to every solution of P(x)=0 , and how many solutions can there be?
tags: m-fold zero, multiplicity
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
Now the question from the beginning can be answered: Why does a factor belong to every solution of $P(x)=0$, and how many solutions can there be?
:::

**The idea.** Theorem [7.2](das-horner-schema.html#satz-7-2) writes every polynomial as $P(x)=(x-x_0)\,Q(x)+c_0$. Substituting $x=x_0$ makes the first term vanish, because its factor $x-x_0$ is zero. What remains is $P(x_0)=c_0$. If $x_0$ is a zero, the remainder is zero, and $x-x_0$ is a factor of $P$. **In short:** The remainder of the division by $x-x_0$ is the function value at $x_0$.

:::definition Definition 8.1 (Zero and multiplicity)
<span class="anker" id="satz-8-1"></span>

$x_0\in\mathbb{R}$ is called a zero of the real function $f$ if $f(x_0)=0$. $x_0$ is called an __$m$-fold zero__ of the polynomial $P_n$ if there is a polynomial $Q_{n-m}$ with

<span class="anker" id="gl-8-1"></span>
$$P_n(x)=(x-x_0)^m\,Q_{n-m}(x)\quad\text{and}\quad Q_{n-m}(x_0)\neq0. \tag{8.1}$$

$m$ is called the __multiplicity__ of the zero $x_0$.
:::

⁠**How to read it:** $m$ counts how many times the factor $x-x_0$ is contained in $P_n$. We have $m\le n$, because the degree $n-m$ of $Q_{n-m}$ cannot be negative.

:::satz Theorem 8.2 (Linear factor)
<span class="anker" id="satz-8-2"></span>

Let $P_n$ be a polynomial of degree $n\ge1$ and $x_0\in\mathbb{R}$. Then

<span class="anker" id="gl-8-2"></span>
$$P_n(x_0)=0\quad\Leftrightarrow\quad P_n(x)=(x-x_0)\,Q_{n-1}(x)\text{ with a polynomial }Q_{n-1}. \tag{8.2}$$

Therefore $P_n$ has at most $n$ zeros, even if each is counted with its multiplicity.
:::

:::beweis Linear factor
“$\Rightarrow$”: In [(7.3)](das-horner-schema.html#gl-7-3), $c_0=P_n(x_0)=0$. “$\Leftarrow$”: Substituting $x_0$ gives the factor 0. **Number:** A product is zero if and only if one factor is zero. So every further zero of $P_n$ is a zero of $Q_{n-1}$. With each zero split off, the degree drops by 1, and after at most $n$ steps a constant $a_n\neq0$ without a zero remains.
:::

⁠**How to read it:** The *linear factor* $x-x_0$ has degree 1 and is zero exactly at $x_0$. **Why $x_0\in\mathbb{R}$ is needed:** $x^2+1$ has no real zero and no real linear factor. **Consequence for the identity theorem:** If two polynomials of degree $\le n$ agree at $n+1$ points, they are equal, because otherwise their difference would have too many zeros.

**Two representations.** Splitting off all zeros produces a form from which they can be read off directly:

<span class="anker" id="gl-8-3"></span>
$$P_n(x)=a_n(x-x_1)(x-x_2)\cdots(x-x_n), \tag{8.3}$$

with $a_n\neq0$ and the zeros $x_1,\dots,x_n\in\mathbb{R}$. A multiple zero appears several times in the list. If a remaining factor has no real zero left, quadratic factors stay:

<span class="anker" id="gl-8-4"></span>
$$P_n(x)=a_n(x^2+\beta_1x+\gamma_1)\cdots(x^2+\beta_kx+\gamma_k)\,(x-x_{2k+1})\cdots(x-x_n), \tag{8.4}$$

where $\beta_i^2-4\gamma_i<0$, so the quadratic factors have no real zeros. The fixed numbers $\beta_1,\dots,\beta_k,\gamma_1,\dots,\gamma_k,x_{2k+1},\dots,x_n$ are $n$ in number, like the coefficients $a_0,\dots,a_{n-1}$. The $n-2k$ numbers $x_i$ are the zeros. Conversely, these numbers determine $P_n$ uniquely by multiplying out; for $n=4$ and $a_4=1$ in [(8.3)](#gl-8-3),

<span class="anker" id="gl-8-5"></span>
$$\begin{aligned} a_3&=-(x_1+x_2+x_3+x_4), & a_2&=x_1x_2+x_1x_3+x_1x_4+x_2x_3+x_2x_4+x_3x_4,\\ a_1&=-(x_1x_2x_3+x_1x_2x_4+x_1x_3x_4+x_2x_3x_4), & a_0&=x_1x_2x_3x_4. \end{aligned} \tag{8.5}$$

Not every real polynomial has the form [(8.3)](#gl-8-3), as $x^2+1$ shows. That the form [(8.4)](#gl-8-4) always exists is harder and is not proved here.

:::zusatz Why quadratic factors suffice
In the complex numbers ([Part 2](/wissen/en/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)), every polynomial of degree $n\ge1$ has a zero (fundamental theorem of algebra). With real coefficients, along with $z$ also $\overline{z}$ is a zero, and $(x-z)(x-\overline{z})=x^2-2\operatorname{Re}(z)\,x+|z|^2$ is real. For $x^2+x+1$, $z=-\frac12+\frac{\sqrt3}{2}\,\mathrm{i}$.
:::

**Example.** For $S$, the scheme at $x_0=2$ gives the row $1,-1,-1,-2,0$, so $S(x)=(x-2)(x^3-x^2-x-2)$. Again at $x_0=2$: $1,1,1,0$, so $S(x)=(x-2)^2(x^2+x+1)$. The third time: $1,3,7$; the remainder $7\neq0$ ends the search. The multiplicity is 2, and because $1-4=-3<0$, the form [(8.4)](#gl-8-4) has been reached, with $n=4$, $k=1$. **Limiting case:** For $m=n$, $P_n(x)=a_n(x-x_0)^n$, the polynomial with only one zero.

**What the multiplicity does.** Near $x_0$, $Q_{n-m}(x)$ does not change its sign, since it is not zero there. The sign of $P_n$ is therefore determined by $(x-x_0)^m$: For odd $m$ it changes, and the graph crosses the axis. For even $m$ it does not change, and the graph only touches it (Fig. [9](#abb-9)).

:::abbildung hm1/k3vielfach 9
The functions $(x-1)^m(x+2)$ for $m=1,2,3$ at the same scale, each with the $m$-fold zero $x_0=1$: For $m=1$ the graph crosses the axis, for $m=2$ it touches it, for $m=3$ it crosses it flatly.
:::

:::frage I find a zero. How do I know whether there are more?
The quotient tells you. After splitting off, a polynomial of lower degree is left, and every further zero of $P$ lies in it. At degree 2 the quadratic formula helps, for $P$, say, $2x^2+3x-2$ with $D=25$ and the zeros $\frac12$ and $-2$. At higher degree you keep trying in the quotient. With integer coefficients and $a_n=1$, only the divisors of $a_0$ come into question as integer zeros, because $a_0$ is, up to sign, the product of the zeros.
:::

:::aufgabe Exercise 9 ★★ Factoring
<span class="anker" id="aufg-9"></span>

(a) Show that $x_0=1$ is a zero of $U(x)=x^4-x^3-3x^2+5x-2$, and determine its multiplicity and the form [(8.3)](#gl-8-3). (b) Bring $x^3-8$ into the form [(8.4)](#gl-8-4). (c) Prediction: A polynomial of degree 5 contains two quadratic factors without a real zero. How many real zeros does it have?

:::loesung
(a) Scheme at 1: $1,0,-3,2,0$, then $1,1,-2,0$, then $1,2,0$, then $1,3$ with remainder $3\neq0$. Multiplicity 3, and $U(x)=(x-1)^3(x+2)$. (b) $x_0=2$ is a zero; the scheme with $1,0,0,-8$ gives $1,2,4,0$. So $x^3-8=(x-2)(x^2+2x+4)$ with $\beta^2-4\gamma=4-16=-12<0$. (c) The two factors together have degree 4, so one linear factor remains: exactly one real zero.
:::
:::
