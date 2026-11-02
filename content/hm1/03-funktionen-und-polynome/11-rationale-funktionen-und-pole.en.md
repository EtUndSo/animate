---
title: Stage 9: Rational functions and poles
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Functions and Polynomials
order: 1231100
summary: The remainder T/Q from Stage 6 has points where its denominator becomes zero.
tags: pole, order, gap, asymptote
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
The remainder $T/Q$ from Stage [6](division-mit-rest.html#stufe-6) has points where its denominator becomes zero. The function is not defined there. What happens nearby, and what happens for large $|x|$?
:::

**The idea.** Dividing a fixed number by something very small makes the result very large. At $x=2$, $Q(2)=0$, but the numerator stays at $P(2)=-12$. At $x=2.01$, $Q=0.0301$ and $R=-398$; at $x=1.99$, $Q=-0.0299$ and $R=+402$. The mechanism is the small factor $x-2$ in the denominator: It changes sign at 2, and $R$ changes with it. If the numerator is also zero there, on the other hand, the factor can cancel.

:::definition Definition 9.1 (Pole and gap)
<span class="anker" id="satz-9-1"></span>

Let $R=P_n/Q_m$. Cancel all common linear factors of numerator and denominator. A point $x_0$ with $Q_m(x_0)=0$ is called

<ul>

<li>

a __pole__ of __order__ $m_0$ if after canceling it is an $m_0$-fold zero of the denominator and not a zero of the numerator;

</li>

<li>

a __gap__ if after canceling it is no longer a zero of the denominator.

</li>

</ul>
:::

⁠**How to read it:** Near a pole, $R(x)=A(x)/(x-x_0)^{m_0}$ with $A(x_0)\neq0$: The numerator stays near $A(x_0)$, the denominator becomes arbitrarily small, and $|R|$ grows beyond every bound. (Part 4 makes this precise with limits.) Odd order means a sign change, even order none, for the same reason as in Stage [8](jede-nullstelle-spaltet-einen-linearfaktor-ab.html#stufe-8): $1/(x-2)^2$ equals $10\,000$ at $2.01$ and at $1.99$. At a gap $R$ stays finite, but there too $x_0\notin\mathcal D(R)$. **Example of a gap:** $L(x)=(x^2-4)/(x-2)$ agrees with $x+2$ for $x\neq2$, $L(2.01)=4.01$; at $x=2$ only one point of the graph is removed.

:::abbildung hm1/k3pole 10
Left, $R=P/Q$: poles at $x=-1$ and $x=2$ (vertical dashed lines), zeros at $-2$, $\frac12$ and $3$. For large $|x|$, $R$ approaches the line $2x-1$, the polynomial part. Right, $L=(x^2-4)/(x-2)$: The graph is the line $x+2$ without the point at $x=2$.
:::

**Large $|x|$.** By [(6.2)](division-mit-rest.html#gl-6-2), $R=S+T/Q$. Because $\deg T<\deg Q$, $T/Q$ becomes arbitrarily small for large $|x|$, since the highest power of the denominator grows faster. So $R$ approaches the polynomial $S$, the __asymptote__ (for $n-m=1$ a straight line). In the reference model $R(100)=198.92$ and $2\cdot100-1=199$; the remainder accounts for only $-0.08$. **Limiting cases:** For $n<m$, $S=0$, and $R$ approaches 0. For $n=m$, $S=a_n/b_m$ is a constant.

:::zusatz Partial fraction decomposition
The remainder can be decomposed further so that each pole gets its own term:

$$R(x)=2x-1+\frac{A}{x-2}+\frac{B}{x+1}.$$

Multiplying $\frac{-8x+4}{(x-2)(x+1)}=\frac{A}{x-2}+\frac{B}{x+1}$ by $x-2$ and setting $x=2$ leaves $A=-12/3=-4$, likewise $B=12/(-3)=-4$. For poles of order 1 that is enough. In electrical engineering this is how transfer functions, which describe how a circuit changes a signal, are decomposed into contributions per pole.
:::

:::frage Isn't a gap the same as a pole, since the denominator is zero in both cases?
The denominator is zero in both cases, that is true. The difference lies in the numerator. At a pole it stays nonzero, and a finite value divided by almost zero becomes large. At a gap it is zero as well, the common factor drops out, and the quotient stays finite.
:::

:::aufgabe Exercise 10 ★★ Pole or gap
<span class="anker" id="aufg-10"></span>

Let $L_2(x)=\dfrac{x^2-1}{x^2-3x+2}$. (a) Determine $\mathcal D(L_2)$, poles and gaps. (b) Compute $L_2(2.01)$ and $L_2(1.99)$ and explain the sign. (c) Which value does $L_2$ approach for large $|x|$? Check with $x=1000$.

:::loesung
(a) $L_2(x)=\frac{(x-1)(x+1)}{(x-1)(x-2)}$, so $\mathcal D(L_2)=\mathbb{R}\setminus\{1,2\}$. Canceled: $\frac{x+1}{x-2}$. At $x=1$ a gap (value of the canceled form: $-2$), at $x=2$ a pole of order 1. (b) $L_2(2.01)=3.01/0.01=301$, $L_2(1.99)=2.99/(-0.01)=-299$. The numerator is positive, near 3; the denominator $x-2$ changes sign. (c) We have $n=m=2$, so $L_2\to1/1=1$. $L_2(1000)=1001/998=1.003$.
:::
:::

:::aufgabe Exercise 11 ★★★ Asymptote with Horner
<span class="anker" id="aufg-11"></span>

Let $W(x)=\dfrac{x^2+x+1}{x-1}$. (a) Divide with the Horner scheme and give the polynomial part and the remainder. (b) Where is the pole, and what order does it have? (c) How far does $W$ lie above the asymptote at $x=100$?

:::loesung
(a) Scheme at $x_0=1$ with $1,1,1$: $1,2,3$. So $x^2+x+1=(x-1)(x+2)+3$ and $W(x)=x+2+\frac{3}{x-1}$. (b) At $x=1$, because the numerator is 3 there. The denominator factor occurs once: order 1. (c) Distance $3/99=0.0303$, above the asymptote, because $x-1>0$.
:::
:::
