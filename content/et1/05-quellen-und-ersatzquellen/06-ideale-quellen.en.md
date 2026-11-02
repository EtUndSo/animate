---
title: Stage 4: Ideal sources
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Sources and Equivalent Sources
order: 1150600
summary: What has been missing so far is whatever drives the current.
tags: ideal voltage source, ideal current source, source voltage, source current
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
What has been missing so far is whatever drives the current. This stage introduces the two basic building blocks that bring energy into a network.
:::

**The idea.** A source holds a single quantity fixed. The connected network determines the other. An __ideal voltage source__ holds the potential difference between its terminals. The load decides what current flows. An __ideal current source__ holds the current in its branch. The load likewise decides what voltage arises. Both are models. They cannot be built, but a regulated power supply or a transistor circuit ([Part 10](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) comes close to them within a limited range.

:::abbildung et1/k5ideal 5
Left, the ideal voltage source: in the diagram a horizontal line, the voltage does not depend on the current. Right, the ideal current source: a vertical line, the current does not depend on the voltage. The stroke in the circuit symbol shows the behavior at the value zero: drawn along the line, the line is closed; drawn across it, the line is interrupted.
:::

:::definition Definition 4.1 (Ideal sources)
<span class="anker" id="satz-4-1"></span>

For the ideal voltage source and the ideal current source,

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{AB}=U_\mathrm{q}\quad\text{for every current},\qquad\qquad I_\mathrm{A}=I_\mathrm{q}\quad\text{for every voltage}. \tag{4.1}$$
:::

⁠**How to read it:** $U_\mathrm{q}$ is the __source voltage__ in V, from millivolts to kilovolts, here 9 V. $I_\mathrm{q}$ is the __source current__ in A, from microamperes to amperes. In Fig. [5](#abb-5) the slope of the characteristic curve is the internal resistance with a negative sign: zero for the voltage source, infinite for the current source. In calculations, a voltage source replaces the difference of two node potentials by a known value, and a current source fixes the current of a branch.

⁠**Validity:** Two connections contradict the model. A short-circuited voltage source would have to satisfy both $U_\mathrm{AB}=U_\mathrm{q}$ and $U_\mathrm{AB}=0$. An open current source would have to satisfy both $I_\mathrm{A}=I_\mathrm{q}$ and $I_\mathrm{A}=0$, because a current needs a closed path.

**Example.** The 9 V source delivers 0.5625 A into 16 $\Omega$, 9 A into 1 $\Omega$, and it would be 9000 A into 1 m$\Omega$. A 0.5 A source produces 8 V across 16 $\Omega$, 500 V across 1 k$\Omega$, and it would be 500 kV across 1 M$\Omega$. **Limiting case:** The more extreme the load, the further the model departs from any real device. That is the reason for the next stage.

:::frage Can the current also flow backward through a source?
Yes. An ideal source fixes only its one quantity. If the current flows into the plus terminal of a voltage source, then $I_\mathrm{A}<0$, and the source absorbs power. That is how a rechargeable battery is charged.
:::

:::aufgabe Exercise 5 ★ What changes?
<span class="anker" id="aufg-5"></span>

An ideal current source of 2 mA feeds 1 k$\Omega$. (a) What is the voltage, and what is it with 4.7 k$\Omega$? (b) A second resistor of 1 k$\Omega$ is added in series with the source. What changes at the first one, what at the source? (c) In parallel with an ideal 5 V source feeding 1 k$\Omega$, 10 $\Omega$ is added. What changes at the load, what at the source?

:::loesung
(a) $2\,\mathrm{mA}\cdot1\,\mathrm{k\Omega}=2$ V, with 4.7 k$\Omega$ it is 9.4 V. The current stays.

(b) Nothing changes at the first resistor: the current is fixed, the voltage stays 2 V. The source must produce 4 V. In series with an ideal current source, a resistor is invisible from outside.

(c) Nothing changes at the load; it stays at 5 V and 5 mA. The source delivers 505 mA instead of 5 mA. In parallel with an ideal voltage source, a resistor is invisible from outside.
:::
:::
