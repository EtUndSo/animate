---
title: Stage 9: Charging through a resistor
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Capacitor
order: 1131000
summary: At a voltage source, the charging current depends on the capacitor voltage, and that depends on the charging current.
tags: short circuit, open circuit, differential equation
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
At a voltage source, the charging current depends on the capacitor voltage, and that depends on the charging current. This stage sets up the equation for this feedback and solves it from the ground up.
:::

**The idea.** In the RC circuit (Fig. [9](#abb-9)), the switch S moves from position 2 to 1 at $t=0$, and the capacitor is empty. The voltage cannot jump (Stage [3](strom-und-spannung-am-kondensator.html#stufe-3)), so $u_C(0)=0$. The whole battery voltage is across $R$, and $i(0)=U_0/R=0.9$ mA flows. For this moment the capacitor behaves like a wire, hence the term __short circuit__: current flows, the voltage is zero. The reason: no charge is separated yet, so there is no field opposing the current.

The current brings charge, and $u_C$ rises. By Kirchhoff's voltage law, less remains for $R$, the current falls, and $u_C$ rises more slowly. This feedback shapes the whole curve. At the end $u_C=U_0$. Nothing is left across $R$, $i=0$: the capacitor behaves like an __open circuit__, the terminals act as if open. The reason: the field of the separated charge raises the plate to the potential of the terminal, and no drop remains along $R$.

:::abbildung et1/k3rckreis 9
Left, the RC circuit with reference arrows, Kirchhoff's voltage law $U_0=u_R+u_C$. Position 1 charges, position 2 discharges. Right, the two equivalent circuits: At $t=0$ the empty capacitor acts like a wire; after a long time the full one acts like open terminals.
:::

**The equation.** Kirchhoff's voltage law ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) reads $U_0=u_R+u_C$. With Ohm's law $u_R=R\,i$ and with $i=C\,\mathrm{d} u_C/\mathrm{d} t$ from [(3.1)](strom-und-spannung-am-kondensator.html#gl-3-1) it follows that

<span class="anker" id="gl-9-1"></span>
$$U_0=R\,C\,\frac{\mathrm{d} u_C}{\mathrm{d} t}+u_C. \tag{9.1}$$

This is a __differential equation__: an equation in which the quantity sought appears together with its derivative. What is sought is not a number but a whole function $u_C(t)$. Rearranged with $\tau=RC$, it reads

<span class="anker" id="gl-9-2"></span>
$$\frac{\mathrm{d} u_C}{\mathrm{d} t}=\frac{U_0-u_C}{\tau}. \tag{9.2}$$

In words: The slope of the curve is the distance to the final value, divided by $\tau$. So a slope is fixed for every point $(t,u_C)$ (Fig. [10](#abb-10)). Anyone who begins at the starting value and follows this slope everywhere draws the solution. That is why exactly one curve belongs to each starting value.

:::abbildung et1/k3richtung 10
Equation [(9.2)](#gl-9-2) as a picture: Each gray dash shows the slope at that point, for $U_0=9$ V and $\tau=1$ s. Far below 9 V it is large, at 9 V zero, above that negative. The curves follow the dashes from the starting values 0 V, 3 V and 12 V and all approach the same final value.
:::

:::satz Theorem 9.1 (Charging)
<span class="anker" id="satz-9-1"></span>

For $u_C(0)=0$ and $t\ge0$,

<span class="anker" id="gl-9-3"></span>
$$u_C(t)=U_0\bigl(1-\mathrm{e}^{-t/\tau}\bigr),\qquad i(t)=\frac{U_0}{R}\,\mathrm{e}^{-t/\tau},\qquad u_R(t)=U_0\,\mathrm{e}^{-t/\tau},\qquad\tau=R\,C. \tag{9.3}$$
:::

⁠**How to read it:** $\mathrm{e}=2.718$ is Euler's number. $\tau$ is the time constant in s: $\mathrm{\Omega\cdot F}=\frac{\mathrm V}{\mathrm A}\cdot\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm s$. The factor $\mathrm{e}^{-t/\tau}$ starts at 1 and falls in every time $\tau$ to $1/\mathrm{e}$ of its value, that is, to 36.8 %. **Validity:** ideal components, constant source, $t=0$ is the moment of switching.

:::herleitung Solving the equation from the ground up
⁠**Step 1: Only the distance to the end counts.** Let $x(t)=U_0-u_C(t)$. Because $U_0$ is constant, $\mathrm{d} x/\mathrm{d} t=-\mathrm{d} u_C/\mathrm{d} t$, and [(9.2)](#gl-9-2) becomes

$$\frac{\mathrm{d} x}{\mathrm{d} t}=-\frac{x}{\tau},\qquad x(0)=U_0.$$

The change of $x$ is proportional to $x$ itself: the larger the remainder, the faster it shrinks.

⁠**Step 2: Divide by $x$.** For $x>0$, $\frac1x\,\frac{\mathrm{d} x}{\mathrm{d} t}=-\frac1\tau$. By the chain rule the left side is the derivative of $\ln x(t)$, because $\frac{\mathrm{d}}{\mathrm{d} t}\ln x(t)=\frac1x\,\frac{\mathrm{d} x}{\mathrm{d} t}$.

⁠**Step 3: Integrate.** So $\ln x(t)$ has the constant slope $-1/\tau$ and is a straight line: $\ln x(t)=-t/\tau+K$ with a constant $K$.

⁠**Step 4: Undo the logarithm.** Applying the exponential function to both sides gives $x(t)=\mathrm{e}^{K}\,\mathrm{e}^{-t/\tau}$. For $t=0$ this reads $x(0)=\mathrm{e}^{K}$, so $\mathrm{e}^{K}=U_0$. Thus $x(t)=U_0\,\mathrm{e}^{-t/\tau}$.

⁠**Step 5: Convert back.** $u_C=U_0-x=U_0(1-\mathrm{e}^{-t/\tau})$. Differentiating: $i=C\,\mathrm{d} u_C/\mathrm{d} t=\frac{C\,U_0}{\tau}\mathrm{e}^{-t/\tau}=\frac{U_0}{R}\mathrm{e}^{-t/\tau}$, and $u_R=R\,i$.

⁠**Verification:** Substituting into [(9.1)](#gl-9-1) gives $R\,C\cdot\frac{U_0}{\tau}\mathrm{e}^{-t/\tau}+U_0-U_0\mathrm{e}^{-t/\tau}=U_0$. It checks out.

⁠**The same route via the current:** From $U_0=R\,i+\frac1C\int_0^ti\,\mathrm{d} t'$, differentiating gives $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$. Written briefly this is $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$, and steps 2 to 4 give $\ln i=-\frac{t}{RC}+\ln\frac{U_0}{R}$, so again $i=\frac{U_0}{R}\mathrm{e}^{-t/RC}$.
:::

::::beispiel
In the reference model, after $t=1$ s, $u_C=9\,\mathrm{V}\cdot(1-\mathrm{e}^{-1})=5.69$ V, $u_R=3.31$ V and $i=0.331$ mA (Fig. [11](#abb-11)). At any time the two voltages add up to 9 V. The tangent at the start rises at $U_0/\tau=9$ V/s and reaches 9 V exactly at $t=\tau$: if the initial current stayed constant as in Stage [3](strom-und-spannung-am-kondensator.html#stufe-3), the capacitor would be full after $\tau$.
::::

⁠**In short:** $\tau$ is the final charge divided by the initial current, $C\,U_0/(U_0/R)=RC$.

:::abbildung et1/k3laden 11
Charging with $U_0=9$ V, $R=10\,\mathrm{k\Omega}$ and $C=100\,\mu\text{F}$. Left, the voltages; right, the current. The current jumps from zero to 0.9 mA at $t=0$ and decays. The tangents at the start meet the final value at $t=\tau=1$ s. The dots belong to $t=\tau$.
:::

⁠**Limiting cases:** For $t\to0$, $\mathrm{e}^{-t/\tau}\to1$: $u_C=0$, $i=U_0/R$; this is the short circuit. For $t\to\infty$, $\mathrm{e}^{-t/\tau}\to0$: $u_C=U_0$, $i=0$; this is the open circuit. For $R\to0$, $\tau\to0$ and $i(0)\to\infty$. With a real wire resistance of 0.1 $\Omega$ it would be 90 A for 10 µs.

:::frage Does the capacitor ever get completely full?
Mathematically never, because $\mathrm{e}^{-t/\tau}$ does not reach zero. In practice after a few $\tau$: after $5\tau$, 0.7 % is missing, 61 mV in the reference model. The charging current is then still 6 µA and is of the order of magnitude of the leakage current from Stage [5](bauformen-und-selbstentladung.html#stufe-5).
:::

:::aufgabe Exercise 10 ★★ Another RC circuit
<span class="anker" id="aufg-10"></span>

A 12 V source charges an empty 220 µF capacitor through 4.7 k$\Omega$.

<ol class="al">

<li>

Calculate $\tau$ and $i(0)$.

</li>

<li>

How large is $u_C$ after 1 s?

</li>

<li>

When does $u_C$ reach half of 12 V, and when 99 %?

</li>

<li>

Predict: What changes in $\tau$ and in $i(0)$ if $R$ is doubled, and what in the final voltage?

</li>

</ol>

:::loesung
(a) $\tau=4.7\,\mathrm{k\Omega}\cdot220\,\mu\text{F}=1.034$ s, $i(0)=12\,\mathrm{V}/4.7\,\mathrm{k\Omega}=2.55$ mA.

(b) $u_C=12\,\mathrm{V}\cdot(1-\mathrm{e}^{-1/1.034})=7.44$ V.

(c) $\mathrm{e}^{-t/\tau}=\frac12$ gives $t=\tau\ln2=0.717$ s. For 99 %, $\mathrm{e}^{-t/\tau}=0.01$, so $t=\tau\ln100=4.76$ s.

(d) $\tau$ doubles, $i(0)$ halves, the final voltage stays at 12 V, because at the end no more current flows through $R$.
:::
:::

:::aufgabe Exercise 11 ★★★ The energy balance of charging
<span class="anker" id="aufg-11"></span>

The capacitor in the RC circuit is charged from 0 to $U_0$.

<ol class="al">

<li>

Show with $W_\mathrm{B}=\int_0^\infty U_0\,i\,\mathrm{d} t$ that the battery gives up $C\,U_0^2$.

</li>

<li>

Show with $W_R=\int_0^\infty R\,i^2\,\mathrm{d} t$ that $\frac12CU_0^2$ turns into heat in the resistor. Give the numbers in the reference model.

</li>

<li>

Why does $R$ not appear in the result, even though the whole loss arises in $R$?

</li>

</ol>

:::loesung
(a) $W_\mathrm{B}=U_0\int_0^\infty i\,\mathrm{d} t=U_0\,Q=C\,U_0^2$, because the integral of the current is the charge. Calculation: $\int_0^\infty\frac{U_0}{R}\mathrm{e}^{-t/\tau}\mathrm{d} t=\frac{U_0}{R}\tau=C\,U_0$.

(b) $W_R=\int_0^\infty R\,\frac{U_0^2}{R^2}\mathrm{e}^{-2t/\tau}\mathrm{d} t=\frac{U_0^2}{R}\cdot\frac\tau2=\frac12CU_0^2$. Reference model: The battery supplies 8.10 mJ; 4.05 mJ each go into the capacitor and into the resistor.

(c) A smaller $R$ increases the current but shortens the time. In $W_R=\frac{U_0^2}{R}\cdot\frac{\tau}{2}=\frac{U_0^2}{R}\cdot\frac{RC}{2}$, $R$ therefore cancels exactly. The efficiency of charging from a fixed voltage is always 50 %, as long as the capacitor starts from zero. The same calculation lies behind the loss [(8.3)](ladungserhaltung-beim-umschalten.html#gl-8-3).
:::
:::
