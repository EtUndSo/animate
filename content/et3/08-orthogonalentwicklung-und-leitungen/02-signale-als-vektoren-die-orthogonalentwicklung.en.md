---
title: Stage 1: Signals as vectors, the orthogonal expansion
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / Orthogonal Expansion and Transmission Lines
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: Chapter 8: Orthogonal Expansion and Transmission Lines
order: 3280200
summary: The Fourier series decomposes a signal into oscillations.
tags: orthogonal, orthonormal, generalized Parseval theorem
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
The Fourier series decomposes a signal into oscillations. The same works with any system of orthogonal functions. This stage shows how to find the coefficients and why they give the best approximation.
:::

**The idea.** A vector in space has the components $b_i=\vec f\cdot\vec e_i$ with respect to perpendicular unit vectors $\vec e_i$. For signals on an interval $[0,T]$, the integral $\int_0^Tf(t)g(t)\mathrm{d} t$ plays the role of the scalar product. Two signals are called __orthogonal__ if it is zero ([Chapter 6](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)). A system of $M$ functions $s_i(t)$ is called __orthonormal__ if

<span class="anker" id="gl-1-1"></span>
$$\int_0^Ts_i(t)\,s_j(t)\,\mathrm{d} t=\begin{cases}1&i=j\\0&i\neq j\end{cases}. \tag{1.1}$$

An energy signal $f(t)$ is approximated by $\sum_{i=0}^{M-1}b_is_i(t)$, and a residual $r(t)=f(t)-\sum b_is_i(t)$ remains.

:::satz Theorem 1.1 (Orthogonal expansion)
<span class="anker" id="satz-1-1"></span>

The energy of the residual, $E_r=\int_0^Tr^2\mathrm{d} t$, is smallest for

<span class="anker" id="gl-1-2"></span>
$$b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t. \tag{1.2}$$

Then $E_r=E_f-\sum_ib_i^2$. If $E_r\to0$ as $M$ grows (complete system), the __generalized Parseval theorem__ $E_f=\sum_ib_i^2$ holds.
:::

:::herleitung Coefficients and residual energy
$E_r=\int_0^T\bigl(f-\sum_ib_is_i\bigr)^2\mathrm{d} t$. Differentiate with respect to $b_j$ and set to zero:

$$\frac{\partial E_r}{\partial b_j}=-2\int_0^T\Bigl(f-\sum_ib_is_i\Bigr)s_j\,\mathrm{d} t=0\quad\Longrightarrow\quad\int_0^Tfs_j\,\mathrm{d} t=\sum_ib_i\int_0^Ts_is_j\,\mathrm{d} t=b_j.$$

Orthonormality leaves only $i=j$ in the sum. If these $b_i$ are substituted and the square is multiplied out, the mixed terms drop out, again because of orthonormality: $E_r=E_f-2\sum b_i^2+\sum b_i^2=E_f-\sum b_i^2$.
:::

⁠**How to read it:** Each coefficient is determined on its own, independently of the others. If you add a basis function, the previous coefficients do not change. This is the advantage of orthogonal systems, just as with the Fourier series ([Chapter 3](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)). $b_i$ is the cross-correlation $\varphi^E_{fs_i}(0)$. That is why the coefficients can be measured with a bank of correlation filters $h_i(t)=s_i(T-t)$ whose outputs are sampled at $t=T$ ([Chapter 7](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)).

::::beispiel
$f(t)=t^2$ on $[0,1]$, $E_f=\frac15$. With $s_0=1$ and $s_1=\sqrt3(2t-1)$:

$$b_0=\int_0^1t^2\mathrm{d} t=\tfrac13,\qquad b_1=\sqrt3\int_0^1t^2(2t-1)\mathrm{d} t=\tfrac{\sqrt3}{6}=0.289,\qquad\sum b_i^2=\tfrac19+\tfrac1{12}=\tfrac{7}{36}.$$

The approximation is $\frac13+\frac{\sqrt3}{6}\sqrt3(2t-1)=t-\frac16$, the best straight line in the sense of energy. The residual energy is $\frac15-\frac7{36}=\frac{1}{180}=0.0056$, that is, 2.8 % of $E_f$. With $s_2=\sqrt5(6t^2-6t+1)$, the coefficient $b_2=\frac{\sqrt5}{30}=0.075$ is added, and the residual becomes zero, because $t^2$ is itself a polynomial of degree two.
::::

:::aufgabe Exercise 1 ★ Checking orthonormality
<span class="anker" id="aufg-1"></span>

Show that $s_0=1$ and $s_1=\sqrt3(2t-1)$ are orthonormal on $[0,1]$. Why does $s_1$ need the factor $\sqrt3$?

:::loesung
$\int_0^11\cdot\sqrt3(2t-1)\mathrm{d} t=\sqrt3\,[t^2-t]_0^1=0$: orthogonal. $\int_0^11^2\mathrm{d} t=1$. $\int_0^13(2t-1)^2\mathrm{d} t=3\cdot\bigl[\frac{(2t-1)^3}{6}\bigr]_0^1=3\cdot\frac{1+1}{6}=1$. Without the factor, the energy of $2t-1$ would be only $\frac13$. The factor $\sqrt3$ normalizes it to 1; otherwise $b_1=\int fs_1\mathrm{d} t$ would not be the correct coefficient.
:::
:::

:::aufgabe Exercise 2 ★★ Best approximation
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Recompute $b_1$ for $f(t)=t^2$ and confirm the approximation $t-\frac16$.

</li>

<li>

Check $E_r=\frac{1}{180}$ by computing $\int_0^1\bigl(t^2-t+\frac16\bigr)^2\mathrm{d} t$ directly.

</li>

<li>

Find the coefficients of $f(t)=\sqrt2\cos(2\pi t)$ with respect to $s_0$ and $s_1$. What does the result mean?

</li>

</ol>

:::loesung
(a) $\int_0^1t^2(2t-1)\mathrm{d} t=\frac24-\frac13=\frac16$, so $b_1=\frac{\sqrt3}{6}$. Approximation: $\frac13+\frac{\sqrt3}{6}\cdot\sqrt3(2t-1)=\frac13+t-\frac12=t-\frac16$.

(b) $\int_0^1\bigl(t^2-t+\tfrac16\bigr)^2\mathrm{d} t=\int_0^1\bigl(t^4-2t^3+\tfrac43t^2-\tfrac13t+\tfrac1{36}\bigr)\mathrm{d} t=\tfrac15-\tfrac12+\tfrac49-\tfrac16+\tfrac1{36}=\tfrac{1}{180}$.

(c) $b_0=\sqrt2\int_0^1\cos(2\pi t)\mathrm{d} t=0$ and $b_1=\sqrt6\int_0^1(2t-1)\cos(2\pi t)\mathrm{d} t=0$ (the cosine is symmetric about $t=\frac12$, and $2t-1$ is antisymmetric). Both coefficients are zero: the function is orthogonal to both basis functions, the approximation is zero, and the entire signal content remains in the residual. A basis is suitable only for signals that resemble its functions.
:::
:::
