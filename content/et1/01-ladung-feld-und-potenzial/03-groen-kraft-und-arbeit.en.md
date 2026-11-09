---
title: Stage 1: Quantities, force and work
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Charge, Field and Potential
order: 1110300
summary: Voltage will turn out to be work per charge.
tags: qualitative, quantitative, Ohm's law, physical quantity, SI system of units, base quantities, current, SI prefixes
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Voltage will turn out to be work per charge. That requires quantities with units, force, work and kinetic energy.
:::

**The idea.** Someone coming in from the snow calls a room warm; someone coming out of the sauna calls it cool. Such judgments are __qualitative__. A thermometer shows both of them 21 °C; that is __quantitative__: a number on a scale, independent of who is measuring. Physics states its laws in terms of such quantities, for example __Ohm's law__ $U=R\cdot I$ ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). The most important mechanical quantity in this chapter is work: a force acting along a path transfers energy, and only its component along the path counts. Lifting a backpack means working against gravity; carrying it horizontally does not (Fig. [2](#abb-2)).

:::definition Definition 1.1 (Physical quantity)
<span class="anker" id="satz-1-1"></span>

A __physical quantity__ is a measurable property, the product of numerical value and unit:

<span class="anker" id="gl-1-1"></span>
$$\text{quantity}=\text{numerical value}\cdot\text{unit}. \tag{1.1}$$
:::

⁠**How to read it:** In $U=9$ V, $U$ is the symbol (italic), 9 the numerical value, V the unit (upright). Square brackets ask for the unit: $[U]=\mathrm V$. The numerical value depends on the unit, the quantity does not: 72 km/h and 20 m/s are the same speed.

**Units.** The __SI system of units__ has seven __base quantities__, which cannot be expressed in terms of one another: length (meter, m), mass (kilogram, kg), time (second, s), electric current (ampere, A), absolute temperature (kelvin, K), luminous intensity (candela, cd) and amount of substance (mole, mol). Their definitions continue to be refined along with measurement technology. The units of all other quantities are products of powers of the base units. An electric __current__ is moving charge; one ampere transports one coulomb per second. Power is energy per time. For this chapter the following is enough:

| Quantity | Unit | in base units | also |
|---|---|---|---|
| Force $F$ | newton, N | $\mathrm{kg\,m/s^2}$ | $\mathrm{J/m}$ |
| Energy, work $W$ | joule, J | $\mathrm{kg\,m^2/s^2}$ | $\mathrm{N\,m}=\mathrm{W\,s}$ |
| Power $P$ | watt, W | $\mathrm{kg\,m^2/s^3}$ | $\mathrm{V\,A}$ |
| Charge $Q$ | coulomb, C | $\mathrm{A\,s}$ |  |
| Voltage $U$ | volt, V | $\mathrm{kg\,m^2/(s^3\,A)}$ | $\mathrm{J/C}$ |

__SI prefixes__ scale a numerical value by powers of ten. Multiples are written in capitals, fractions in lowercase; only deka, hecto and kilo deviate, for historical reasons. There is only ever one prefix in front of a unit, and it forms a single symbol with the unit.

| Prefix | Power | in words | Prefix | Power | in words |
|---|---|---|---|---|---|
| Atto, a | $10^{-18}$ | quintillionth | Exa, E | $10^{18}$ | quintillion |
| Femto, f | $10^{-15}$ | quadrillionth | Peta, P | $10^{15}$ | quadrillion |
| Pico, p | $10^{-12}$ | trillionth | Tera, T | $10^{12}$ | trillion |
| Nano, n | $10^{-9}$ | billionth | Giga, G | $10^{9}$ | billion |
| Micro, µ | $10^{-6}$ | millionth | Mega, M | $10^{6}$ | million |
| Milli, m | $10^{-3}$ | thousandth | Kilo, k | $10^{3}$ | thousand |
| Centi, c | $10^{-2}$ | hundredth | Hecto, h | $10^{2}$ | hundred |
| Deci, d | $10^{-1}$ | tenth | Deka, da | $10^{1}$ | ten |

**Calculating with units.**

<ol>

<li>

⁠**Adding** is allowed only for quantities with the same unit; prefixes are matched first: $2\,\mathrm{kV}+40\,\mathrm{V}=2.04\,\mathrm{kV}$, not 42 kV. Different units in a sum nearly always reveal a calculation error.

</li>

<li>

⁠**Multiplying** is always allowed. Numerical values, units and prefixes are multiplied separately, and in fractions units cancel like numbers: $\frac{6\,\mathrm{N\,m}}{3\,\mathrm{m}}=2\,\mathrm{N}$, $0.5\,\mathrm{A}\cdot9\,\mathrm{V}=4.5\,\mathrm{W}$, $\mathrm{k\cdot M}=\mathrm G$, $\mu\text{}\cdot\mathrm M=1$. In the reference model, $9\,\mathrm{V}/3\,\mathrm{mm}=3000\,\mathrm{V/m}=3\,\mathrm{kV/m}$.

</li>

<li>

⁠**Converting** sometimes needs a factor: $1\,\mathrm{Wh}=3600\,\mathrm{W\,s}$, $1\,\mathrm{km/h}=\frac{1}{3.6}\,\mathrm{m/s}$. Because prefix and unit form one symbol, $1\,\mathrm{km^2}=(1000\,\mathrm{m})^2=10^6\,\mathrm{m^2}$, not 1000 m$^2$.

</li>

<li>

⁠**The quantity determines the unit.** Depending on the field, energy is written in W s, N m or J. But equal base units do not prove equal quantities: hertz (oscillations per second) and becquerel (decays per second) are both $1/\mathrm s$, and N m is also torque (force times lever arm).

</li>

</ol>

**Force and work.** A __force__ deforms a body that is held in place or accelerates a movable one. __Energy__ is the capacity to do work. Force and displacement are __vectors__: quantities with magnitude and direction, written with an arrow, $\vec F$. __Velocity__ is the change of position per time, $v=\mathrm{d} s/\mathrm{d} t$, __acceleration__ the change of velocity per time, $a=\mathrm{d} v/\mathrm{d} t$.

:::definition Definition 1.2 (Force and work)
<span class="anker" id="satz-1-2"></span>

The force on a body with mass $m$ and acceleration $a$, and the force between two masses $m$, $M$ at the distance $r$, are

<span class="anker" id="gl-1-2"></span>
$$F=m\,a,\qquad F=\gamma\,\frac{m\,M}{r^2}. \tag{1.2}$$

The __work__ done by a force along a path is

<span class="anker" id="gl-1-3"></span>
$$\Delta W=\vec F\cdot\Delta\vec s=F\,\Delta s\cos\alpha,\qquad W=\int_{P_1}^{P_2}\vec F\cdot\mathrm{d}\vec s. \tag{1.3}$$
:::

:::satz Theorem 1.3 (Constant acceleration and kinetic energy)
<span class="anker" id="satz-1-3"></span>

With the initial values $s_0$ and $v_0$ at $t=0$, for constant $a$

<span class="anker" id="gl-1-4"></span>
$$v(t)=v_0+a\,t,\qquad s(t)=s_0+v_0\,t+\tfrac12a\,t^2. \tag{1.4}$$

A body with the velocity $v$ carries the __kinetic energy__ $W_\mathrm{kin}=\frac12m\,v^2$.
:::

⁠**How to read it:** $[F]=\mathrm N$; at the surface of the Earth, about 1 N acts on 100 g. $\gamma=6.674\cdot10^{-11}\,\mathrm{N\,m^2/kg^2}$ is the __gravitational constant__. $\alpha$ is the angle between the force and the path segment. The product $\vec F\cdot\Delta\vec s$ is called the __scalar product__; its result is a number. The integral is called a __line integral__: the path is divided into short straight pieces and their contributions are summed. $[W]=\mathrm J$; one joule lifts 102 g by one meter. For $\alpha<90^\circ$ the force gives energy to the body, for $\alpha>90^\circ$ it takes energy from it. **Validity:** [(1.4)](#gl-1-4) holds only for constant acceleration; Stage [9](was-die-spannung-mit-einer-ladung-macht.html#stufe-9) needs exactly this case.

:::herleitung Kinetic energy
From [(1.4)](#gl-1-4) with $v_0=0$ and $s_0=0$ it follows that $t=v/a$ and $s=\frac12a\,t^2=v^2/(2a)$. Over this distance, a constant force $F=m\,a$ does the work $F\,s=m\,a\,v^2/(2a)=\frac12m\,v^2$.
:::

:::abbildung et1/k1wegarbeit 2
A backpack of 2 kg is carried from A to B, 8 m sideways and 6 m up. On the stairs, only the red pieces count, 6 m in total. On the ramp, the path is 10 m long and $\cos\alpha=0.6$. Both paths give 117.7 J.
:::

::::beispiel
The __weight__ $F_\mathrm{G}=m\,g=19.62\,\mathrm{N}$ acts on the backpack. To lift it steadily, the hand applies the same force upward. Over the stairs, $W=19.62\,\mathrm{N}\cdot6\,\mathrm{m}=117.7\,\mathrm{J}$; over the ramp, $W=19.62\,\mathrm{N}\cdot10\,\mathrm{m}\cdot0.6=117.7\,\mathrm{J}$. The hand does $+117.7$ J of work, the weight $-117.7$ J. The energy is then stored in the height, as __potential energy__: if the backpack falls, it becomes kinetic energy. This pair, work of the field force and work from outside, returns in Stage [6](arbeit-im-feld.html#stufe-6).
::::

⁠**Limiting cases:** $\alpha=0$ gives $\Delta W=F\,\Delta s$, $\alpha=90^\circ$ gives $\Delta W=0$.

:::frage Carrying something horizontally still makes your arm tired. Is no work being done there?
Not on the backpack: it gains neither height nor speed. The muscle consumes energy all the same, because its fibers keep tensing anew. That energy turns into heat in the body and never reaches the backpack.
:::

:::aufgabe Exercise 1 ★ Units and prefixes
<span class="anker" id="aufg-1"></span>

Calculate and give the result in a suitable unit: (a) $3\,\mathrm{kN}+450\,\mathrm{N}$, (b) $2\,\mathrm{mA}\cdot4\,\mathrm{ks}$, (c) $6\,\mu\text{C}/3\,\mathrm{ms}$, (d) 1 kWh in joules, (e) 1.5 mm$^2$ in m$^2$, (f) the unit V/m in base units.

:::loesung
(a) $3000\,\mathrm{N}+450\,\mathrm{N}=3.45\,\mathrm{kN}$. (b) Milli and kilo cancel, $\mathrm{A\cdot s}=\mathrm C$: 8 C. (c) $\mu\text{}/\mathrm m=\mathrm m$ (milli) and $\mathrm{C/s}=\mathrm A$: 2 mA. (d) $1000\,\mathrm{W}\cdot3600\,\mathrm{s}=3.6\,\mathrm{MJ}$. (e) $1\,\mathrm{mm^2}=(10^{-3}\,\mathrm{m})^2=10^{-6}\,\mathrm{m^2}$, so $1.5\cdot10^{-6}\,\mathrm{m^2}$. (f) $\frac{\mathrm V}{\mathrm m}=\frac{\mathrm{kg\,m^2}}{\mathrm{A\,s^3}\cdot\mathrm m}=\frac{\mathrm{kg\,m}}{\mathrm{A\,s^3}}$.
:::
:::
