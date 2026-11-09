---
title: Stage 8: Voltage and ground
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Charge, Field and Potential
order: 1111000
summary: The value of a potential depends on the reference point; the difference of two potentials does not.
tags: voltage, ground, earth ground, circuit diagrams, reference arrow, nodes
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
The value of a potential depends on the reference point; the difference of two potentials does not. This difference is the technically important quantity. This stage shows how to calculate with it in a circuit.
:::

**The idea.** A force acts on a charge only if the potential changes with location. A potential that is equally high everywhere has no effect, however high it is. Only differences are effective, which is why every voltmeter has two terminals. The zero point can be chosen freely: if one point of a circuit is declared the zero point, every other point gets a number. If the zero point is shifted, all the numbers shift together; their differences remain.

:::definition Definition 8.1 (Electric voltage and ground)
<span class="anker" id="satz-8-1"></span>

The __voltage__ between $P_1$ and $P_2$ is

<span class="anker" id="gl-8-1"></span>
$$U_{12}=\varphi(P_1)-\varphi(P_2)=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=\frac{W_{12}}{Q}, \tag{8.1}$$

with the unit $[U]=[W]\cdot[Q]^{-1}=\mathrm{N\,m\,A^{-1}\,s^{-1}}=\mathrm{kg\,m^2\,A^{-1}\,s^{-3}}=\mathrm V$. The point of a circuit that is assigned $\varphi:=0$ V is called __ground__ or reference potential, written GND. If it is connected to the soil, it is called __earth ground__. Starting from there,

<span class="anker" id="gl-8-2"></span>
$$\varphi_1=\varphi_2+U_{12}. \tag{8.2}$$
:::

:::satz Theorem 8.2 (Uniform field, freedom of the reference point)
<span class="anker" id="satz-8-2"></span>

Between two parallel plates at the distance $d$ with the voltage $U$, $E=U/d$. If the reference point is shifted, all potentials change by the same constant $c$, and all voltages stay the same:

<span class="anker" id="gl-8-3"></span>
$$E=\frac{U}{d},\qquad\varphi'(P)=\varphi(P)+c\quad\Longrightarrow\quad\varphi'_1-\varphi'_2=U_{12}. \tag{8.3}$$
:::

⁠**How to read it:** $U_{12}$ means “voltage from 1 to 2”; the order matters: $U_{21}=-U_{12}$. In __circuit diagrams__, the drawings of a circuit, this is shown by a __reference arrow__ from point 1 to point 2 (Fig. [9](#abb-9)). It fixes the sign: if $U_{12}>0$, point 1 is higher. A positive charge then gains kinetic energy when moving along the arrow; an electron loses it. The field strength says how much voltage drops per meter of path. Potentials may be negative, meaning lower than ground.

Typical voltages: measuring limit of modern voltmeters 0.1 nV, TV antenna 12 µ V to 10 mV, between hand and heart 1 mV, car battery 12 V, power outlet 230 V, high-voltage line 120 to 800 kV, Van de Graaff generator (belt generator for high voltages) 10 MV, lightning up to 100 MV.

⁠**Validity:** The integral in [(8.1)](#gl-8-1) is independent of the path only in an electrostatic field. A wire in a circuit diagram counts as ideal; all its points have the same potential. This is justified: at 0.1 V/m, only 10 mV drop across 10 cm of wire.

:::herleitung Pair of plates and reference point
⁠**Field strength.** Between A and B, $\vec E$ is constant and points along the path: $U_\mathrm{AB}=\int_0^dE\,\mathrm{d} x=E\,d$.

⁠**Reference point.** With [(7.1)](das-potenzial.html#gl-7-1) and path independence,

$$\varphi'(P)=\int_{P}^{P_0'}\vec E\cdot\mathrm{d}\vec s=\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s+\int_{P_0}^{P_0'}\vec E\cdot\mathrm{d}\vec s=\varphi(P)+c.$$

The second integral does not depend on $P$, so it drops out of the difference.
:::

:::abbildung et1/k1symbole 9
Left and center: circuit symbols of a battery (long thin line: plus terminal) and of a DC voltage source, which supplies a fixed voltage. The reference arrow points from the plus terminal to the minus terminal. Right: two points, two reference arrows, two signs.
:::

:::abbildung et1/k1masse 10
The same circuit with ground at three places. The potentials are 9 V, 3 V, 0 V, then 6 V, 0 V, $-3$ V, then 0 V, $-6$ V, $-9$ V. Each time, 6 V are across the upper resistor and 3 V across the lower one.
:::

::::beispiel
In the pair of plates, $E=9\,\mathrm{V}/3\,\mathrm{mm}=3$ kV/m, 1000 times less than the breakdown field strength of air. A rectangular battery supplies around 0.5 Ah (amperes times hours), which is 1800 C. Its total energy is $W=Q\,U=1800\,\mathrm{C}\cdot9\,\mathrm{V}=16.2$ kJ $=4.5$ Wh. In the circuit, ground is at first at the minus terminal (Fig. [10](#abb-10) left). With [(8.2)](#gl-8-2), from bottom to top this gives 0 V, $0+3$ V, $3+6$ V. If ground moves to the middle, every potential falls by 3 V. The voltage across the upper resistor is $9\,\mathrm{V}-3\,\mathrm{V}$ before and $6\,\mathrm{V}-0\,\mathrm{V}$ after. In motor vehicles, the minus terminal of the battery is usually connected to the body, which is the ground there.
::::

⁠**In short:** voltage is energy per charge between two points.

⁠**Limiting cases:** For $P_2=P_1$, $U=0$, and likewise for two points in the same piece of metal at rest. At $d=3$ µ m, 9 V would already give 3 MV/m.

:::frage Why does nothing happen to a bird on a high-voltage line?
The line is several hundred kilovolts above the earth, but the bird touches only the line. Between its feet, at $E\approx0.1$ V/m and a spacing of 5 cm, there are only 5 mV. What counts is the difference between the points touched, not the potential itself.
:::

:::frage Does current drain away into ground?
Not through a single ground connection. Current needs a closed path, and the one connection offers no return path. Ground is an agreement about the zero point, not a drain.
:::

:::ltspice Shifting ground
⁠**Draw:** source `voltage` with `9` from `a` to `b`, `res` with `2k` from `a` to `m`, `res` with `1k` from `m` to `b`. Place the ground symbol first at `b`, then at `m`, then at `a`. LTspice always needs a ground. [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) explains the resistors; here they only provide the split into 6 V and 3 V.

⁠**Directives:** `.op`, plus for each net without ground a measurement such as `.meas op pa FIND V(a)`. The net with ground has no value of its own; use 0 for it.

⁠**What you see:** Ground at `b`: $\mathtt{V(a)}=9$ V, $\mathtt{V(m)}=3$ V. Ground at `m`: $\mathtt{V(a)}=6$ V, $\mathtt{V(b)}=-3$ V. Ground at `a`: $\mathtt{V(m)}=-6$ V, $\mathtt{V(b)}=-9$ V. The difference between `a` and `m` is always 6 V. Then build the network from Exercise [9](#aufg-9) with `5k`, `4k`, `3k` and check your potentials.
:::

:::aufgabe Exercise 8 ★ Voltage and energy
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

A lightning bolt transports 5 C across 100 MV. How large is the energy in MJ and in kWh?

</li>

<li>

Air breaks down at $3\cdot10^6$ V/m. What voltage does a spark across 1 cm need?

</li>

<li>

$U_{12}=+5$ V. How large is $U_{21}$? Which point is higher?

</li>

</ol>

:::loesung
(a) $W=Q\,U=5\,\mathrm{C}\cdot100\,\mathrm{MV}=500$ MJ $=139$ kWh. (b) $U=E\,d=3\cdot10^6\,\mathrm{V/m}\cdot0.01\,\mathrm{m}=30$ kV. (c) $U_{21}=-5$ V; point 1 is 5 V higher.
:::
:::

:::aufgabe Exercise 9 ★★ Potentials in a chain
<span class="anker" id="aufg-9"></span>

A 12 V source feeds three resistors in series. The connection points (__nodes__) are called 1 (plus terminal), 2, 3 and 4 (minus terminal). $U_{12}=5$ V, $U_{23}=4$ V, $U_{34}=3$ V.

<ol class="al">

<li>

Give all potentials with ground at node 4, and then with ground at node 3.

</li>

<li>

Calculate $U_{24}$ and $U_{13}$ in both cases. What do you notice?

</li>

</ol>

:::loesung
(a) Ground at 4: $\varphi_4=0$, $\varphi_3=3$ V, $\varphi_2=7$ V, $\varphi_1=12$ V. Ground at 3: all values fall by 3 V, $\varphi_4=-3$ V, $\varphi_3=0$, $\varphi_2=4$ V, $\varphi_1=9$ V. (b) First case: $U_{24}=7$ V, $U_{13}=12\,\mathrm{V}-3\,\mathrm{V}=9$ V. Second case: $U_{24}=4\,\mathrm{V}-(-3\,\mathrm{V})=7$ V, $U_{13}=9\,\mathrm{V}-0=9$ V. The voltages stay the same.
:::
:::
