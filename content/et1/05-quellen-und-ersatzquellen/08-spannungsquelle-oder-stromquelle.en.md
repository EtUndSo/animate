---
title: Stage 6: Voltage source or current source
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Sources and Equivalent Sources
order: 1150800
summary: There are two circuit diagrams for the same real source.
tags: equivalent
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
There are two circuit diagrams for the same real source. This stage shows that both describe the same straight line, and how to convert one into the other.
:::

**The idea.** A straight line can be read from the voltage axis (height $U_\mathrm{q}$, slope $R_\mathrm{q}$) or from the current axis (intercept $I_\mathrm{q}$, slope $G_\mathrm{q}$). Two networks are called __equivalent__ if they have the same characteristic curves. Then no measurement at the terminals can establish from outside which of the two is connected.

:::satz Theorem 6.1 (Equivalence of real sources)
<span class="anker" id="satz-6-1"></span>

A real voltage source and a real current source are equivalent if

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{q}=\frac{I_\mathrm{q}}{G_\mathrm{q}}\qquad\text{and}\qquad R_\mathrm{q}=\frac{1}{G_\mathrm{q}}. \tag{6.1}$$
:::

:::herleitung Equating the lines
You solve the current-source equation from [(5.1)](reale-quellen-und-der-arbeitspunkt.html#gl-5-1) for the voltage, $U_\mathrm{AB}=(I_\mathrm{q}-I_\mathrm{A})/G_\mathrm{q}$, and equate it with the voltage-source equation:

$$\frac{I_\mathrm{q}}{G_\mathrm{q}}-\frac{I_\mathrm{A}}{G_\mathrm{q}}=U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}.$$

This must hold for every current. So the terms without $I_\mathrm{A}$ and the terms with $I_\mathrm{A}$ must be equal separately. That is [(6.1)](#gl-6-1).
:::

⁠**How to read it:** The current $I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$ is the short-circuit current, and the resistance stays the same. In the current-source form, the entire source current runs through $G_\mathrm{q}$ in the open circuit and produces the open-circuit voltage there. If the load draws current, less remains for $G_\mathrm{q}$ and the voltage falls. This is the same drop, only as current division instead of voltage division. **Validity:** The equivalence holds only at the terminals and only for $0<R_\mathrm{q}<\infty$.

:::abbildung et1/k5umwandlung 7
The same battery at the same operating point. Left, 0.5 A flows through everything. Right, the source current of 4.5 A divides into 4 A through the conductance and 0.5 A to the load. At the terminals, voltage and current agree.
:::

**Example.** The battery with 9 V and 2 $\Omega$ becomes $I_\mathrm{q}=4.5$ A and $G_\mathrm{q}=0.5$ S. At the operating point with 8 V the conductance takes $0.5\,\mathrm{S}\cdot8\,\mathrm{V}=4$ A, leaving 0.5 A for the load (Fig. [7](#abb-7)). **Limiting case:** For $R_\mathrm{q}\to0$, $I_\mathrm{q}\to\infty$. An ideal voltage source has no current-source form, an ideal current source no voltage-source form.

**Which form do you choose?** For calculation both are equally good. You take the form that shows the behavior better: voltage sources have low resistance (ideally zero), current sources have high resistance (ideally infinite). If $R_\mathrm{q}$ is small compared with the load, the voltage hardly changes, and you choose the voltage-source form. If $R_\mathrm{q}$ is large compared with the load, the current hardly changes, and you choose the current-source form.

:::frage If the two are the same, does the battery burn 40.5 W in the open circuit?
No. On the right in Fig. [7](#abb-7), 4.5 A flows through 2 $\Omega$ in the open circuit, which with $P=UI$ ([Part 7](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)) would be 40.5 W. The real battery stays cold; the voltage-source picture with 0 W is the right one here. Equivalent circuits are correct at the terminals, not inside. What happens inside depends on the construction, not on the characteristic curve. The same is true at the operating point: 0.5 W against 32 W inside, 4 W outside in both cases.
:::

:::aufgabe Exercise 7 ★ Converting
<span class="anker" id="aufg-7"></span>

(a) Convert 5 V with 100 $\Omega$ into a current source. (b) Convert 20 mA with 1 k$\Omega$ in parallel into a voltage source. (c) Connect 400 $\Omega$ to both forms from (a) and compare voltage and current.

:::loesung
(a) $I_\mathrm{q}=5\,\mathrm{V}/100\,\Omega=50$ mA, $G_\mathrm{q}=10$ mS. (b) $U_\mathrm{q}=20\,\mathrm{mA}\cdot1\,\mathrm{k\Omega}=20$ V, $R_\mathrm{q}=1$ k$\Omega$.

(c) Voltage source: voltage divider, $U=5\,\mathrm{V}\cdot\frac{400}{500}=4$ V, $I=10$ mA. Current source: $50\,\mathrm{mA}\cdot(100\,\Omega\parallel400\,\Omega)=50\,\mathrm{mA}\cdot80\,\Omega=4$ V, $I=4\,\mathrm{V}/400\,\Omega=10$ mA. The same.
:::
:::
