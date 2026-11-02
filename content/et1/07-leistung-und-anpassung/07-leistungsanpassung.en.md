---
title: Stage 6: Power matching
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Power, Matching and Efficiency
order: 1170700
summary: The table shows a maximum of P L .
tags: short-circuit power
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
The table shows a maximum of $P_\mathrm{L}$. This stage finds it and explains why it lies exactly at $R_\mathrm{L}=R_\mathrm{i}$.
:::

**The idea.** Two influences work against each other. With a small $R_\mathrm{L}$, many coulombs arrive, but almost all their energy stays in $R_\mathrm{i}$. With a large $R_\mathrm{L}$, each coulomb gives off almost everything in the load, but few arrive. The straight line $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ from [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) makes this visible: $P_\mathrm{L}=U_\mathrm{L}I$ is the area of the rectangle under it (Fig. [7](#abb-7)). It is largest when its corner lies in the middle of the line, at half the current and half the voltage. Then the same voltage drops across $R_\mathrm{i}$ and $R_\mathrm{L}$ at the same current, so the two resistors are equal.

:::abbildung et1/k7rechteck 7
Source line of the battery with three operating points. Blue: $P_\mathrm{L}$, rectangle of $I$ and $U_\mathrm{L}$. Red: $P_\mathrm{v}$, rectangle of $I$ and $U_\mathrm{Ri}$. Together they make $P_\mathrm{q}=U_\mathrm{q}I$. The middle corner gives the largest blue rectangle.
:::

:::satz Theorem 6.1 (Power matching)
<span class="anker" id="satz-6-1"></span>

With $I=U_\mathrm{q}/(R_\mathrm{i}+R_\mathrm{L})$, the power at the load is

<span class="anker" id="gl-6-1"></span>
$$P_\mathrm{L}(R_\mathrm{L})=\left(\frac{U_\mathrm{q}}{R_\mathrm{i}+R_\mathrm{L}}\right)^{\!2}R_\mathrm{L}=U_\mathrm{q}^2\,\frac{R_\mathrm{L}}{\bigl(R_\mathrm{i}(1+R_\mathrm{L}/R_\mathrm{i})\bigr)^2}=P_\mathrm{SC}\,\frac{\alpha}{(1+\alpha)^2}, \tag{6.1}$$

with $\alpha=R_\mathrm{L}/R_\mathrm{i}$ and $P_\mathrm{SC}=U_\mathrm{q}^2/R_\mathrm{i}$. It is greatest for

<span class="anker" id="gl-6-2"></span>
$$R_\mathrm{L}=R_\mathrm{i},\qquad P_\mathrm{L,max}=\frac{U_\mathrm{q}^2}{4\,R_\mathrm{i}}=\frac{P_\mathrm{SC}}{4},\qquad I=\frac{I_\mathrm{SC}}{2},\qquad U_\mathrm{L}=\frac{U_\mathrm{q}}{2}. \tag{6.2}$$
:::

⁠**How to read it:** $P_\mathrm{SC}=U_\mathrm{q}I_\mathrm{SC}$ is the __short-circuit power__, the power of the source at $R_\mathrm{L}=0$. It ends up entirely in $R_\mathrm{i}$, and no load receives more than a quarter of it. **Validity:** The source is fixed; only $R_\mathrm{L}$ is chosen. With an equivalent source, $U_\mathrm{OC}$ takes the place of $U_\mathrm{q}$.

:::herleitung The maximum, in three ways
By the quotient rule, $\bigl(f/g\bigr)'=(f'g-f\,g')/g^2$, with $f=\alpha$ and $g=(1+\alpha)^2$,

$$\frac{\mathrm{d} P_\mathrm{L}}{\mathrm{d}\alpha}=P_\mathrm{SC}\,\frac{(1+\alpha)^2-2\alpha(1+\alpha)}{(1+\alpha)^4}=P_\mathrm{SC}\,\frac{1-\alpha}{(1+\alpha)^3}.$$

The derivative is zero at $\alpha=1$, positive before it and negative after it. That is the maximum.

Without a derivative: With $x=I/I_\mathrm{SC}$, $P_\mathrm{L}=P_\mathrm{SC}\,x(1-x)$. This parabola has the zeros 0 and 1, so its maximum $\frac14$ lies at $x=\frac12$.

As a mechanism: A current increase $\mathrm{d} I$ brings $U_\mathrm{q}\mathrm{d} I$ out of the source, and the losses grow by $2R_\mathrm{i}I\,\mathrm{d} I$. At $I=I_\mathrm{SC}/2$, the loss eats up the gain: 9 V against $2\cdot2\,\Omega\cdot2.25\,\mathrm{A}=9$ V.
:::

**Example.** For $R_\mathrm{L}=2\,\Omega$, $I=2.25$ A, $U_\mathrm{L}=4.5$ V and $P_\mathrm{L}=10.125$ W, which is a quarter of $P_\mathrm{SC}=40.5$ W. The loads 0.5 $\Omega$ and 8 $\Omega$ both give 6.48 W. In general, $\alpha$ and $1/\alpha$ supply the same power, because they swap $x$ and $1-x$. **Limiting cases:** For $\alpha\to0$, the current is fixed and $P_\mathrm{L}\approx P_\mathrm{SC}\,\alpha$. For $\alpha\to\infty$, the voltage is fixed and $P_\mathrm{L}\approx P_\mathrm{SC}/\alpha$.

:::ltspice Parabola and straight line
⁠**Draw:** `voltage` with 9 from `q` to ground, `res` with 2 from `q` to `a`. As the load, a current source `current` named `I1` from `a` to ground.

⁠**Directives:** `.dc I1 0 4.5 0.01` and `.meas dc Pmax MAX V(a)*I(I1)`

⁠**What you see:** Plot `V(a)*I(I1)`: a parabola with the maximum 10.125 W at 2.25 A. `V(a)/9` is the efficiency, a falling straight line that reaches 0.5 there. At 3.6 A and 0.9 A there are 6.48 W each. For Exercise [6](#aufg-6), enter 12 and 4 and sweep up to 3 A: 9 W at 1.5 A, 8 W each at 1 A and 2 A.
:::

:::frage I have a fixed load. Should I choose the source so that $R_\mathrm{i}=R_\mathrm{L}$?
No. The theorem applies to a fixed source and a selectable load. If the load is fixed and $R_\mathrm{i}$ can be chosen, $R_\mathrm{i}=0$ is best, because $U_\mathrm{q}^2R_\mathrm{L}/(R_\mathrm{i}+R_\mathrm{L})^2$ falls with $R_\mathrm{i}$. The 16 $\Omega$ load then gets 4 W with $R_\mathrm{i}=2\,\Omega$, but 5.06 W with $R_\mathrm{i}=0$.
:::

:::aufgabe Exercise 6 ★★ Loudspeaker on the amplifier
<span class="anker" id="aufg-6"></span>

An amplifier output acts like $U_\mathrm{q}=12$ V and $R_\mathrm{i}=4\,\Omega$. (a) Which loudspeaker extracts the greatest power, and how large is it? (b) What does 8 $\Omega$ give? Compare power and efficiency. (c) Which second load supplies the same power as 8 $\Omega$? (d) ★★★ Prove with [(6.1)](#gl-6-1) that $\alpha$ and $1/\alpha$ always give the same power.

:::loesung
(a) $R_\mathrm{L}=4\,\Omega$, $P_\mathrm{L,max}=144\,\mathrm{V^2}/16\,\Omega=9$ W at $\eta=50$ %. (b) $I=1$ A, $P_\mathrm{L}=8$ W, $\eta=\frac23$. Only 11 % of the power is lost, and the losses fall from 9 W to 4 W. (c) $\alpha=2$ goes with $\alpha=\frac12$, so $R_\mathrm{L}=2\,\Omega$: 8 W, but only $\eta=\frac13$.

(d) $\dfrac{1/\alpha}{(1+1/\alpha)^2}=\dfrac{1/\alpha}{(\alpha+1)^2/\alpha^2}=\dfrac{\alpha}{(1+\alpha)^2}$.
:::
:::
