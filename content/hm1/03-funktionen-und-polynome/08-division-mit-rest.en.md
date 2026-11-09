---
title: Stage 6: Division with remainder
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Functions and Polynomials
order: 1230800
summary: Sum, difference and product of polynomials are again polynomials, but the quotient usually is not.
tags: 
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
Sum, difference and product of polynomials are again polynomials, but the quotient usually is not. Division with remainder decomposes it into a polynomial and a remainder that is as small as possible, as in $17:5=3$ remainder $2$.
:::

**The idea.** With numbers you subtract multiples of the divisor until the remainder is smaller than the divisor. With polynomials the degree measures the size. You subtract a multiple of the denominator that exactly cancels the highest power of the numerator, and repeat this until the degree of the remainder is smaller than that of the denominator (Fig. [7](#abb-7)).

:::definition Definition 6.1 (Rational function)
<span class="anker" id="satz-6-1"></span>

For polynomials $P_n$ and $Q_m$ of degree $n$ and $m$,

<span class="anker" id="gl-6-1"></span>
$$R(x):=\frac{P_n(x)}{Q_m(x)},\qquad\mathcal D(R):=\{x\in\mathbb{R}:Q_m(x)\neq0\} \tag{6.1}$$

is called a rational function.
:::

⁠**How to read it:** The zeros of the denominator do not belong to $\mathcal D(R)$. In the reference model $x=2$ and $x=-1$ are missing.

:::satz Theorem 6.2 (Division with remainder)
<span class="anker" id="satz-6-2"></span>

Let $R(x)=P_n(x)/Q_m(x)$ with $n\ge m\ge1$. Then there are polynomials $S_{n-m}$ and $T_k$ with $\deg S_{n-m}=n-m$ such that for all $x\in\mathcal D(R)$

<span class="anker" id="gl-6-2"></span>
$$R(x)=S_{n-m}(x)+\frac{T_k(x)}{Q_m(x)}, \tag{6.2}$$

where $\deg T_k=k<m$ or $T_k=0$. After multiplying by $Q_m$ this means for all $x\in\mathbb{R}$

<span class="anker" id="gl-6-3"></span>
$$P_n(x)=S_{n-m}(x)\,Q_m(x)+T_k(x). \tag{6.3}$$
:::

:::beweis Division with remainder
Let $a_n$, $b_m\neq0$ be the leading coefficients of $P_n$, $Q_m$. Set

$$\widetilde P(x):=P_n(x)-\frac{a_n}{b_m}x^{n-m}\,Q_m(x).$$

The subtracted term begins with $\frac{a_n}{b_m}x^{n-m}\cdot b_mx^m=a_nx^n$, so $x^n$ cancels, and $\widetilde P=0$ or $\deg\widetilde P\le n-1$. Dividing by $Q_m$ gives

$$\frac{P_n(x)}{Q_m(x)}=\frac{a_n}{b_m}x^{n-m}+\frac{\widetilde P(x)}{Q_m(x)}.$$

If $\widetilde P=0$ or $\deg\widetilde P<m$, you are done with $T_k=\widetilde P$. Otherwise you make the same step with $\widetilde P$ instead of $P_n$. The degree drops by at least 1 each time, and after at most $n-m+1$ steps the procedure ends. The sum of all prefactors is $S_{n-m}$; the first one determines its degree $n-m$.
:::

⁠**How to read it:** $S_{n-m}$ is the polynomial part, $T_k$ the remainder. $b_m\neq0$ is needed, because you divide by $b_m$. For $n<m$ there is nothing to divide; then $S=0$ and $T=P_n$. The example $x^2:x$ shows the clean case $T=0$.

::::beispiel
For $P:Q$, $2x\cdot Q$ cancels the term $2x^3$, then $-1\cdot Q$ cancels the term $-x^2$:

$$\begin{array}{lrrrr} & 2x^3 & -3x^2 & -11x & +6\\ -2x\cdot Q: & -2x^3 & +2x^2 & +4x & \\ \hline & & -x^2 & -7x & +6\\ +1\cdot Q: & & +x^2 & -x & -2\\ \hline & & & -8x & +4 \end{array}$$

So $R(x)=2x-1+\dfrac{-8x+4}{x^2-x-2}$, with $n-m=1$ and $k=1<2$. **Check** by [(6.3)](#gl-6-3) at $x=3$: $5\cdot4+(-20)=0=P(3)$.
::::

:::abbildung hm1/k3division 7
The division $P:Q$ as coefficients per power. In each step the highest power disappears, and the degree drops from 3 to 2 and to 1. Then it is smaller than the degree 2 of $Q$, and the procedure ends.
:::

:::frage Why may the remainder have degree 1 when $Q$ has degree 2? With numbers the remainder is just a number.
The remainder is a polynomial, and its size is measured by the degree. “Smaller than the divisor” here means: smaller degree, that is, $k<m$. Only for the divisor $x-x_0$ with $m=1$ is the remainder a constant. That is exactly what Stage [8](jede-nullstelle-spaltet-einen-linearfaktor-ab.html#stufe-8) uses.
:::

:::aufgabe Exercise 7 ★★ Division with remainder
<span class="anker" id="aufg-7"></span>

(a) Compute $(x^4-3x^2+2x+5):(x^2+x-1)$ with remainder. Watch out for the missing power $x^3$. (b) Check at $x=2$. (c) Limiting case: What does $(x+1):(x^2+1)$ give?

:::loesung
(a) With $x^4+0x^3-3x^2+2x+5$: Subtracting $x^2\cdot(x^2+x-1)$ leaves $-x^3-2x^2+2x+5$, subtracting $-x\cdot(x^2+x-1)$ leaves $-x^2+x+5$, subtracting $-1\cdot(x^2+x-1)$ leaves $2x+4$. Result: $S(x)=x^2-x-1$, remainder $2x+4$. (b) Left $16-12+4+5=13$. Right $1\cdot5+8=13$. (c) Here $n=1<m=2$, there is nothing to divide: polynomial part 0, remainder $x+1$.
:::
:::
