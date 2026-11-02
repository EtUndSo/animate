---
title: Stage 3: Current and voltage at the capacitor
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Capacitor
order: 1130400
summary: At a resistor, the voltage fixes the current at the same moment.
tags: current source
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
At a resistor, the voltage fixes the current at the same moment. At a capacitor it is different: here the current depends on how fast the voltage is changing. This stage sets up the law.
:::

**The idea.** The voltage shows how much charge has flowed in so far. Current changes this charge. If much current flows, the voltage rises quickly. If none flows, it stays where it is, even if it is high. So the current does not follow from the value of the voltage, but from its change.

:::satz Theorem 3.1 (Current and voltage at the capacitor)
<span class="anker" id="satz-3-1"></span>

With the current and voltage reference arrows in the same direction ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)), the following holds for time-dependent quantities:

<span class="anker" id="gl-3-1"></span>
<span class="anker" id="gl-3-2"></span>
$$\begin{aligned} i(t)&=\frac{\mathrm{d} q}{\mathrm{d} t}=C\,\frac{\mathrm{d} u(t)}{\mathrm{d} t},\\ u(t)&=\frac{q(t)}{C}=u(t_0)+\frac1C\int_{t_0}^{t}i(t')\,\mathrm{d} t'. \end{aligned} \tag{3.1|3.2}$$
:::

:::herleitung Current and voltage
Current is charge per time, $i=\mathrm{d} q/\mathrm{d} t$ ([Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Substituting $q=C\,u$ and pulling out the constant number $C$ gives [(3.1)](#gl-3-1). Conversely, the charge is the area under the current curve, just as distance is the area under the velocity ([Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)): $q(t)=q(t_0)+\int_{t_0}^{t}i\,\mathrm{d} t'$. Dividing by $C$ gives [(3.2)](#gl-3-2).
:::

⁠**How to read it:** Lowercase letters stand for time-dependent quantities, $t'$ is the integration variable, $u(t_0)$ the voltage at the starting time. $i$ in A, $C$ in F, $\mathrm{d} u/\mathrm{d} t$ in V/s. 1 mA into 100 µF makes the voltage rise at 10 V/s. **Sign:** $q$ is the charge of the plate into which the current arrow points. For $i>0$ it grows and $u$ rises; for $i<0$, $u$ falls. **Validity:** $C$ must be constant.

**Two consequences.** First: **The voltage does not jump.** A jump by $\Delta U$ in the time $\Delta t$ requires $i=C\,\Delta U/\Delta t$. For $\Delta t\to0$ the current would grow without limit, because the charge $C\,\Delta U$ would have to arrive in zero time. 9 V in 1 µs across 100 µF already requires 900 A. The current, on the other hand, may jump, because it is not tied to a stored quantity. Second: **At constant voltage no current flows.** With $\mathrm{d} u/\mathrm{d} t=0$, $i=0$: the capacitor blocks direct current.

**Example.** A __current source__, a component that holds its current fixed regardless of the voltage, feeds a resistor and an uncharged capacitor in series through the switch S (Fig. [3](#abb-3)). It supplies $I=0.9$ mA; $R$ and $C$ are the values of the RC circuit. When S closes at $t=0$, $u_R$ jumps to the fixed value $R\,I=9$ V. At the capacitor, [(3.2)](#gl-3-2) with $u_C(0)=0$ gives

<span class="anker" id="gl-3-3"></span>
$$u_C(t)=\frac{Q(t)}{C}=\frac{I\,t}{C}=9\,\mathrm{V/s}\cdot t. \tag{3.3}$$

The voltage grows in a straight line. It starts continuously at zero even though the current jumps. An ideal current source keeps charging without end, until the dielectric breaks down. At 1 s both voltages are equal.

:::abbildung et1/k3rampe 3
A current source charges a capacitor through $R=10\,\mathrm{k\Omega}$. When S closes, $u_R$ jumps to 9 V and stays there. $u_C$ starts at zero and rises at 9 V/s, because the same charge arrives every second.
:::

⁠**Limiting case:** For $C\to\infty$ the slope becomes zero and the voltage does not budge. A very large capacitor therefore holds a voltage fixed.

:::frage An empty capacitor has 0 V across it. Doesn't the current then have to be zero?
That holds for a resistor. At a capacitor, $u=0$ says nothing about $i$, because $i$ depends on the slope of $u$, not on its value. In Fig. [3](#abb-3), at $t=0$ the voltage is zero, but the current is 0.9 mA.
:::

:::aufgabe Exercise 3 ★★ From current to voltage and back
<span class="anker" id="aufg-3"></span>

A 100 µF capacitor is empty at $t=0$. The current is $+0.5$ mA from 0 to 2 s, zero from 2 s to 3 s and $-1$ mA from 3 s to 4 s.

<ol class="al">

<li>

Sketch $u(t)$ and give the values at 2 s, 3 s and 4 s.

</li>

<li>

What charge does it carry at 3 s?

</li>

<li>

On another capacitor of 10 µF, the voltage rises uniformly from 2 V to 7 V in 5 ms. What current flows?

</li>

<li>

Why may $i(t)$ have a vertical edge, but $u(t)$ may not?

</li>

</ol>

:::loesung
(a) At constant current, $u$ is a straight line with the slope $i/C$. From 0 to 2 s: $0.5\,\mathrm{mA}/100\,\mu\text{F}=5$ V/s, so $u(2\,\mathrm{s})=10$ V. From 2 s to 3 s: $i=0$, the voltage stays at 10 V. From 3 s to 4 s: $-10$ V/s, so $u(4\,\mathrm{s})=0$. The curve is a trapezoid.

(b) $Q=C\,u=100\,\mu\text{F}\cdot10\,\mathrm{V}=1$ mC. This is also the area under $i(t)$ up to 3 s: $0.5\,\mathrm{mA}\cdot2\,\mathrm{s}$.

(c) $i=C\,\Delta u/\Delta t=10\,\mu\text{F}\cdot5\,\mathrm{V}/5\,\mathrm{ms}=10$ mA.

(d) $u$ follows from the area under $i$. An area always grows continuously, even if $i$ has an edge. An edge in $u$, by contrast, would require unlimited current.
:::
:::
