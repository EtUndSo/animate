---
title: Stage 7: Why 50 %, and which goal applies
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Power, Matching and Efficiency
order: 1170800
summary: The power maximum wastes half.
tags: 
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
The power maximum wastes half. This stage shows why that is unavoidable, and when you want it anyway.
:::

**The idea.** From $\eta=U_\mathrm{L}/U_\mathrm{q}$ and the source line it follows: the efficiency falls linearly with the current, because the more current, the more voltage stays in $R_\mathrm{i}$. The power of the source $P_\mathrm{q}=U_\mathrm{q}I$, by contrast, rises linearly with the current. What arrives at the load is the product, $P_\mathrm{L}=P_\mathrm{q}\,\eta$. The product of a rising and a falling straight line is a parabola with its vertex in the middle, and there the falling line stands at half height (Fig. [8](#abb-8)). The 50 % are neither a coincidence nor a question of material.

:::satz Theorem 7.1 (Power and efficiency)
<span class="anker" id="satz-7-1"></span>

Dividing $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ by $U_\mathrm{q}$ gives, with $x=I/I_\mathrm{SC}$,

<span class="anker" id="gl-7-1"></span>
$$\eta=1-x,\qquad\frac{P_\mathrm{L}}{P_\mathrm{SC}}=x\,\eta=x(1-x). \tag{7.1}$$

At power matching, $x=\frac12$, so $\eta=\frac12$.
:::

⁠**How to read it:** $x$ is the current as a fraction of the short-circuit current, $\eta$ the fraction of the energy per coulomb that reaches the load. **In short:** At the power maximum, each charge gives off one half of its energy in the source and the other in the load. **Validity:** as in Stage [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5). **Limiting cases:** $x=0$ is the open circuit with $\eta=1$, $x=1$ the short circuit with $\eta=0$. In both, $P_\mathrm{L}=0$.

:::abbildung et1/k7kurven 8
Left: power at the load and efficiency versus $R_\mathrm{L}/R_\mathrm{i}$. The power maximum lies at 1, where $\eta=0.5$. Right, the same curves versus the current: $\eta$ becomes a straight line, the power a parabola. The normalization is to $P_\mathrm{L,max}=P_\mathrm{SC}/4$.
:::

**Three goals.** Which mode of operation is right depends on what counts.

| Matching | Condition | Result | $\eta$ | Use |
|---|---|---|---|---|
| Voltage | $R_\mathrm{L}\gg R_\mathrm{i}$ | $U_\mathrm{L}\approx U_\mathrm{q}$, hardly load-dependent | close to 1 | Power grid, battery, voltmeter |
| Current | $R_\mathrm{L}\ll R_\mathrm{i}$ | $I\approx I_\mathrm{SC}$, hardly load-dependent | close to 0 | Ammeter, current sources |
| Power | $R_\mathrm{L}=R_\mathrm{i}$ | $P_\mathrm{L}$ maximum | $\frac12$ | Antennas, signal processing |

::::beispiel [Examples]
At the battery, $R_\mathrm{L}=200\,\Omega$ gives the voltage 8.91 V, 99 % of $U_\mathrm{q}$. With $R_\mathrm{L}=0.02\,\Omega$, 4.46 A flow, 99 % of $I_\mathrm{SC}$. The step from 2 $\Omega$ to 8 $\Omega$ costs 36 % of the power and lowers the heat in the battery to 16 %.
::::

⁠**Power engineering.** The powers are in the kW range, and all heat in the source costs money and endangers it. One wants high efficiency, that is, $R_\mathrm{i}\ll R_\mathrm{L}$. A power-tool battery with 18 V and 60 m$\Omega$ still reaches $\eta=1-7.2\,\mathrm{V}/18\,\mathrm{V}=60$ % during startup at 120 A, and $(120\,\mathrm{A})^2\cdot60\,\mathrm{m\Omega}=864$ W arise inside. A work light with 1.8 W acts like 180 $\Omega$, and $\eta=180/180.06=99.97$ %. Matching would mean 1350 W of heat in the battery here.

⁠**Communications engineering.** The powers are in the µ W range. A receiver can only take what the antenna offers. The absolute power counts, not the fraction, and the heat in the source does no harm. An antenna with 10 mV and 50 $\Omega$ delivers exactly 0.5 µ W to 50 $\Omega$, but only 0.165 µ W to 5 $\Omega$ or 500 $\Omega$.

**Equivalent sources: the maximum stays, the 50 % do not.** Often the source is a network. Fig. [9](#abb-9) shows a source with $R_\mathrm{q}$ and, in parallel with it, $R$. With respect to the terminals A, B, it is an equivalent source ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) with $R_\mathrm{i}=R_\mathrm{q}\parallel R$ and $U_\mathrm{OC}=U_\mathrm{q}R/(R_\mathrm{q}+R)$. For the load, only the terminal line counts, so the maximum lies at $R_\mathrm{L}=R_\mathrm{i}$, with

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm{L}=U_\mathrm{q}\,\frac{R}{2(R_\mathrm{q}+R)},\qquad P_\mathrm{L}=\frac{U_\mathrm{L}^2}{R_\mathrm{L}}=\frac{U_\mathrm{q}^2\,R}{4\,R_\mathrm{q}(R_\mathrm{q}+R)}. \tag{7.2}$$

However, the real source works into $R_\mathrm{tot}=R_\mathrm{q}+R\parallel R_\mathrm{L}$, and this gives

<span class="anker" id="gl-7-3"></span>
$$P_\mathrm{q}=\frac{U_\mathrm{q}^2}{R_\mathrm{tot}}=\frac{U_\mathrm{q}^2\,(2R_\mathrm{q}+R)}{2R_\mathrm{q}(R_\mathrm{q}+R)},\qquad\eta=\frac{P_\mathrm{L}}{P_\mathrm{q}}=\frac12\,\frac{R}{2R_\mathrm{q}+R}<\frac12\quad\text{for }R<\infty. \tag{7.3}$$

:::abbildung et1/k7netz 9
Left, the network at matching with the actual powers. Right, its equivalent source. For the load both are the same, in the source they are not.
:::

:::herleitung The steps leading to [(7.3)](#gl-7-3)
With $R_\mathrm{L}=R_\mathrm{q}R/(R_\mathrm{q}+R)$, $R\parallel R_\mathrm{L}=R^2R_\mathrm{q}/(R^2+2R_\mathrm{q}R)=R\,R_\mathrm{q}/(R+2R_\mathrm{q})$. This gives $R_\mathrm{tot}=2R_\mathrm{q}(R_\mathrm{q}+R)/(2R_\mathrm{q}+R)$. In general, the voltage divider gives $U_\mathrm{L}=U_\mathrm{q}(R\parallel R_\mathrm{L})/R_\mathrm{tot}=U_\mathrm{q}\,R\,R_\mathrm{L}/\bigl(R_\mathrm{q}(R+R_\mathrm{L})+R\,R_\mathrm{L}\bigr)$. Substituting gives the formula in [(7.2)](#gl-7-2). Thus $P_\mathrm{L}=U_\mathrm{L}^2(R_\mathrm{q}+R)/(R_\mathrm{q}R)$. The quotient of $P_\mathrm{L}$ and $P_\mathrm{q}$ reduces to [(7.3)](#gl-7-3).
:::

::::beispiel
For $U_\mathrm{q}=18$ V, $R_\mathrm{q}=6\,\Omega$ and $R=3\,\Omega$, $R_\mathrm{i}=2\,\Omega$ and $U_\mathrm{OC}=6$ V. At $R_\mathrm{L}=2\,\Omega$, 3 V are across the load, and it receives 4.5 W. 2.5 A flow through $R_\mathrm{q}$, of which 1 A goes through $R$. That gives 37.5 W in $R_\mathrm{q}$, 3 W in $R$, and together with the load $P_\mathrm{q}=45$ W and $\eta=10$ %. The equivalent source appears to show 50 %, because it says nothing about the interior. The current through $R$ also flows without a load; even in an open circuit the network heats with 36 W.
::::

⁠**Limiting case:** For $R\to\infty$, this branch disappears, and [(7.3)](#gl-7-3) gives $\eta=\frac12$ again.

:::frage Does $\eta=50$ % at the maximum mean that with matching I “lose” half of the energy?
With a source with a real internal resistance, yes; it heats up as much as the load. At low power this is tolerable. Where energy is expensive or the source is sensitive, one operates far to the right of the maximum.
:::

:::aufgabe Exercise 7 ★ Which goal applies?
<span class="anker" id="aufg-7"></span>

Assign and calculate: (a) A voltmeter with 10 M$\Omega$ on the battery. How far does the reading deviate from 9 V? (b) An ammeter with 0.1 $\Omega$ in a circuit of 5 V and 1 k$\Omega$. By what percentage does it change the current? (c) A power supply with 12 V and 50 m$\Omega$ on 6 $\Omega$. What is $\eta$? (d) What would power matching give on the same power supply?

:::loesung
(a) Voltage matching: $R_\mathrm{L}\gg R_\mathrm{i}$. 0.9 µ A flow, and 1.8 µ V drop internally. (b) Current matching: the source appears high-impedance. The current falls from 5 mA by 0.01 %. (c) Voltage matching: $\eta=6/6.05=99.2$ %. (d) $R_\mathrm{L}=50$ m$\Omega$ would give 720 W at the load and 720 W in the power supply, which would be destructive.
:::
:::

:::aufgabe Exercise 8 ★★★ The network at matching
<span class="anker" id="aufg-8"></span>

A source with $U_\mathrm{q}=24$ V and $R_\mathrm{q}=4\,\Omega$ is loaded with $R=12\,\Omega$, and the load is in parallel with $R$. (a) Determine $R_\mathrm{i}$ and $U_\mathrm{OC}$. (b) Calculate $U_\mathrm{L}$ and $P_\mathrm{L}$ at matching. (c) Calculate $P_\mathrm{q}$ and $\eta$, once from the currents and once with [(7.3)](#gl-7-3). (d) How large must $R$ be so that $\eta=45$ %?

:::loesung
(a) $R_\mathrm{i}=4\,\Omega\parallel12\,\Omega=3\,\Omega$, $U_\mathrm{OC}=24\,\mathrm{V}\cdot12/16=18$ V. (b) $U_\mathrm{L}=9$ V, $P_\mathrm{L}=(9\,\mathrm{V})^2/3\,\Omega=27$ W $=U_\mathrm{OC}^2/(4R_\mathrm{i})$. (c) 3 A through the load, 0.75 A through $R$, so 3.75 A from the source. $P_\mathrm{q}=90$ W $=56.25\,\mathrm{W}+6.75\,\mathrm{W}+27\,\mathrm{W}$, $\eta=30$ %, like $\frac12\cdot12/20$. (d) $\frac12R/(8\,\Omega+R)=0.45$ gives $R=72\,\Omega$.
:::
:::
