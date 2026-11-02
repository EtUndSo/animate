---
title: Stage 9: What voltage does to a charge
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Charge, Field and Potential
order: 1111100
summary: This stage brings field, potential and voltage together on a single electron: What force acts, what energy does it gain, how fast does it get?
tags: electronvolt
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
This stage brings field, potential and voltage together on a single electron: What force acts, what energy does it gain, how fast does it get?
:::

**The idea.** An electron detaches from plate B and starts from rest. The field points from A to B. Because of $\vec F=Q\vec E$ and $Q=-e$, the force acts opposite to the field, toward plate A. It is equally large everywhere, so the acceleration is constant and [(1.4)](groen-kraft-und-arbeit.html#gl-1-4) holds. On the way, potential energy turns into kinetic energy. The electron moves toward the high potential, yet its energy $Q\varphi$ falls, because $Q$ is negative.

:::satz Theorem 9.1 (Charge in the field)
<span class="anker" id="satz-9-1"></span>

In an electrostatic field, the sum of kinetic energy and potential energy stays constant:

<span class="anker" id="gl-9-1"></span>
$$\tfrac12m\,v^2+Q\,\varphi=\text{constant}. \tag{9.1}$$

A charge that passes through the voltage $U$ from rest reaches, in a uniform field of length $d$,

<span class="anker" id="gl-9-2"></span>
$$v=\sqrt{\frac{2\,|Q\,U|}{m}},\qquad a=\frac{|Q|\,E}{m},\qquad t=\frac{2\,d}{v}. \tag{9.2}$$
:::

:::herleitung Energy theorem and flight time
The work of the field becomes kinetic energy entirely: $\frac12mv_2^2-\frac12mv_1^2=W_{12}=Q(\varphi_1-\varphi_2)$. Rearranging gives [(9.1)](#gl-9-1). With $v_1=0$ it follows that $|Q\,U|=\frac12m\,v^2$. At constant acceleration the average speed is $v/2$, so $t=d/(v/2)$.
:::

⁠**How to read it:** $m$ is the mass in kg, $\varphi$ the potential at the location. The path does not appear in $v$; the voltage alone determines the energy. **Validity and neglected effects:** The equations hold in vacuum. In air, an electron collides with a molecule after only fractions of a micrometer. The weight $m_\mathrm{e}g=8.9\cdot10^{-30}$ N is dropped; it is $5.4\cdot10^{13}$ times smaller than the field force. In addition, $v\ll c$ must hold. Here $v$ is only 0.6 % of the speed of light $c$, and the correction to the kinetic energy is 0.003 %.

:::abbildung et1/k1elektron 11
Left: the electron starts at plate B and moves against the field to plate A. Right: from $x=3$ mm to $x=0$ the kinetic energy grows to $1.44\cdot10^{-18}$ J, and the potential energy falls by the same amount, reference point B. The sum stays zero.
:::

**Example.** For the electron in the pair of plates,

$$\begin{aligned} F&=e\,E=4.81\cdot10^{-16}\,\mathrm{N},\qquad a=\frac{F}{m_\mathrm{e}}=5.28\cdot10^{14}\,\mathrm{m/s^2},\qquad W=e\,U=1.44\cdot10^{-18}\,\mathrm{J},\\ v&=\sqrt{\frac{2\cdot1.44\cdot10^{-18}\,\mathrm{J}}{9.109\cdot10^{-31}\,\mathrm{kg}}}=1.78\cdot10^{6}\,\mathrm{m/s},\qquad t=\frac{2\cdot3\,\mathrm{mm}}{v}=3.37\,\mathrm{ns}. \end{aligned}$$

A proton moves from A to B. It gains the same energy but is 1836 times heavier: $v=4.15\cdot10^4$ m/s, $\sqrt{1836}=42.9$ times slower, flight time 144 ns.

⁠**In short:** if a charge in vacuum passes through a voltage, its kinetic energy changes by charge times voltage, regardless of path and distance.

⁠**Limiting cases:** For $U\to0$, $v\to0$. Double the plate distance at the same voltage halves $E$ and $a$ but does not change $v$: the electron accelerates more weakly but for longer, and needs 6.74 ns. Four times the voltage gives twice the speed.

:::frage Does the electron really move against the field? Surely a field drives charges in its own direction.
It drives *positive* charges in its direction; that is how the direction of $\vec E$ is defined. Every charge moves of its own accord to where its potential energy $Q\varphi$ becomes smaller. For the electron, that is the higher potential.
:::

:::zusatz The electronvolt
The energy an elementary charge gains on passing through 1 V is called the __electronvolt__: $1\,\mathrm{eV}=1.602\cdot10^{-19}$ J. The electron in the example gains 9 eV.
:::

:::aufgabe Exercise 10 ★★★ Electron against the field
<span class="anker" id="aufg-10"></span>

An electron leaves plate A of the reference model with $v_0=1.0\cdot10^6$ m/s toward plate B.

<ol class="al">

<li>

Does it reach plate B? Compare its kinetic energy with the energy needed.

</li>

<li>

At which location $x$ does it turn around? Calculate once with the energy theorem and once with [(1.4)](groen-kraft-und-arbeit.html#gl-1-4).

</li>

<li>

When is it back at plate A, and with what speed?

</li>

<li>

What initial speed would it need to just reach B?

</li>

</ol>

:::loesung
(a) $W_\mathrm{kin}=\frac12m_\mathrm{e}v_0^2=4.55\cdot10^{-19}$ J. Reaching B would take $e\cdot9\,\mathrm{V}=1.44\cdot10^{-18}$ J. It does not reach B. (b) Energy theorem: it travels until $\Delta\varphi=W_\mathrm{kin}/e=2.84$ V are used up. At 3 V/mm, $x=0.948$ mm. With [(1.4)](groen-kraft-und-arbeit.html#gl-1-4): deceleration $a=5.28\cdot10^{14}\,\mathrm{m/s^2}$, turnaround at $t=v_0/a$, so $x=v_0^2/(2a)=0.948$ mm.

(c) There and back: $t=2v_0/a=3.79$ ns. The potential is the same again, so by [(9.1)](#gl-9-1) $v=v_0=1.0\cdot10^6$ m/s, in the opposite direction. (d) Exactly the energy from the example: $v_0=1.78\cdot10^6$ m/s.
:::
:::
