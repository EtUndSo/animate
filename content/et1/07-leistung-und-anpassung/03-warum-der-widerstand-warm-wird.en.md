---
title: Stage 2: Why the resistor gets warm
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / Power, Matching and Efficiency
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Chapter 7: Power, Matching and Efficiency
order: 1170300
summary: In the resistor, the energy leaves the circuit.
tags: power rating, hyperbola
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
In the resistor, the energy leaves the circuit. This stage shows the mechanism and the limit that follows from it.
:::

**The idea.** If a voltage is applied to a resistor, there is a field in it. It accelerates every free electron. After the flight time $T$, the electron collides and loses its directed velocity again ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). In doing so, its kinetic energy goes to the crystal lattice, the atoms vibrate more strongly, and this vibration is heat (Fig. [2](#abb-2)). The electron is only the messenger: behind the resistor it has the same drift as in front of it, because current and cross section are the same. It has lost potential without getting faster. So all the energy ends up in the lattice. The drift itself is negligible: at 0.44 µ m/s ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)), an electron carries $8.8\cdot10^{-44}$ J, while at 9 V it gives off $1.44\cdot10^{-18}$ J, which is $1.6\cdot10^{25}$ times as much.

:::abbildung et1/k7stoss 2
Collision model for one electron. During flight, the work done by the field (blue) grows and is stored as kinetic energy in the electron. At the collision, the heat in the lattice jumps by $W_1$ (red). After each collision, both curves are equally high: everything goes to the lattice.
:::

:::satz Theorem 2.1 (Joule heat and power rating)
<span class="anker" id="satz-2-1"></span>

In a resistor, all the electrical power turns into heat:

<span class="anker" id="gl-2-1"></span>
$$P=U\,I=R\,I^2=\frac{U^2}{R}. \tag{2.1}$$

A component tolerates this only up to its __power rating__ $P_\mathrm{max}$:

<span class="anker" id="gl-2-2"></span>
$$P\le P_\mathrm{max}. \tag{2.2}$$
:::

⁠**How to read it:** A small film resistor has $P_\mathrm{max}=250$ mW, a fan heater converts 2 kW. The formula is quadratic because the current counts twice: twice the current means twice as many coulombs per second, and because of $U=R\,I$ each gives off twice as much. At equal current (series), the heat grows with $R$; at equal voltage (parallel), it falls with $R$. **Validity:** $P=U\,I$ always holds, the other two forms only for the ohmic resistor ($R$ independent of the current), and $U$ and $I$ must belong to this resistor.

:::herleitung From collisions to $U^2/R$
In the model from [Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), an electron is accelerated at $a=e\,E/m_\mathrm e$ and reaches $v_\mathrm{max}=a\,T$ over the distance $s=\frac12a\,T^2$. The field does the work $e\,E\,s=m_\mathrm e\,a\,s=\frac12m_\mathrm e(a\,T)^2=W_1$, exactly the kinetic energy at the collision. The volume $A\,L$ contains $n\,A\,L$ free electrons, and each collides $1/T$ times per second:

$$P=n\,A\,L\,\frac{W_1}{T}=n\,A\,L\,\frac{e^2E^2\,T}{2\,m_\mathrm e}=\sigma\,E^2\,A\,L.$$

Here $\sigma=n\,e\,\mu$ and $\mu=e\,T/(2\,m_\mathrm e)$ ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). With $U=E\,L$ and $R=L/(\sigma A)$, this becomes $P=U^2/R$.
:::

**Power rating.** The temperature rises until the component gives off as much heat per second to the surroundings as arises inside. More power therefore means a higher temperature, and too high a temperature destroys it. In the diagram of Fig. [3](#abb-3), the limit is the __hyperbola__ $I=P_\mathrm{max}/U$, and every resistor is a straight line through the origin. Their intersection lies at $U_\mathrm{max}=\sqrt{P_\mathrm{max}\,R}$ and $I_\mathrm{max}=\sqrt{P_\mathrm{max}/R}$.

:::abbildung et1/k7grenze 3
Limit of a resistor with 250 mW. Each resistance value may be operated only up to the hyperbola: 25 $\Omega$ up to 100 mA, 100 $\Omega$ up to 50 mA, 400 $\Omega$ up to 25 mA.
:::

::::beispiel
With 100 $\Omega$ and 250 mW, $U_\mathrm{max}=5$ V and $I_\mathrm{max}=50$ mA are permissible. At ideal 9 V, 810 mW would arise, 3.24 times the limit. It would take $R\ge(9\,\mathrm{V})^2/250\,\mathrm{mW}=324\,\Omega$.
::::

⁠**Limiting cases:** $R\to\infty$ gives $P\to0$. $R\to0$ gives $P\to\infty$ at fixed voltage. Only the internal resistance of the source prevents this (Stage [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5)).

:::frage Heating wire and lead carry the same current. Why does only the heating wire glow?
At equal current, the heat is proportional to $R$. A lead with 10 m$\Omega$ converts only 2.5 mW at 0.5 A, while the 16 $\Omega$ load converts 4 W, 1600 times as much. In hair dryers and soldering irons the heat is the purpose; in the line it is a loss (Stage [4](leitungsverluste.html#stufe-4)).
:::

:::aufgabe Exercise 2 ★★ Which one gets hotter?
<span class="anker" id="aufg-2"></span>

Two resistors of 100 $\Omega$ and 300 $\Omega$, both rated for 250 mW, are connected to 12 V. First predict which one gets hotter in each case. (a) They are in series. (b) They are in parallel. Calculate all the powers. (c) Where is the power rating exceeded?

:::loesung
(a) Series: $I=12\,\mathrm{V}/400\,\Omega=30$ mA, and $P=R\,I^2$ gives 90 mW and 270 mW. The larger resistor gets hotter: the same number of coulombs, each giving off three times as much there. (b) Parallel: $P=U^2/R$ gives 1.44 W and 0.48 W. The smaller one gets hotter: the same energy per coulomb, but three times as many coulombs. (c) In series, the 300 $\Omega$ resistor is overloaded with 270 mW; in parallel, both are.
:::
:::
