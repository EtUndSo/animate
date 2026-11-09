---
title: Stage 1: Why current flows into an insulator
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Capacitor
order: 1130200
summary: The plates do not touch.
tags: 
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
The plates do not touch. Nevertheless, a meter in the lead shows current. This stage clarifies which charge moves where.
:::

**The idea.** The uncharged pair of plates is connected to the battery by wires (Fig. [1](#abb-1)). At the first moment both plates are at the same potential, but the battery terminals are 9 V apart. The potential drop therefore lies along the wires. There is a field there, and it pushes the free electrons in the metal. In the wire at plate A they run away from the plate to the plus terminal, in the wire at plate B from the minus terminal onto the plate. A loses electrons and becomes positive, B gains electrons and becomes negative. No electron crosses the gap: every electron that arrives on B comes from the wire before it, not from A.

With every displaced charge, the field between the plates grows and with it the voltage. The plates approach the potential of their terminals, the drop along the wires shrinks, the current decreases. At 9 V between the plates, each plate is at the potential of its terminal. No drop remains along the wires, no force acts on the electrons any more, and the current ends.

:::abbildung et1/k3aufbau 1
Left: the pair of plates during charging. Electrons run from plate A to the plus terminal, and just as many from the minus terminal onto plate B. The current $i$ counts in the direction of positive charge, that is, against the electrons, and is the same in both leads. No charge runs through the insulator; the field $E$ is there. Right: the circuit symbol with reference arrows.
:::

:::definition Definition 1.1 (Capacitor)
<span class="anker" id="satz-1-1"></span>

A capacitor consists of two electrodes separated by a dielectric. Its charge $Q$ is the charge of the positive electrode; the other carries $-Q$. Current through the capacitor means: a current flows in at one terminal, and at the same moment the same current flows out at the other.
:::

⁠**How to read it:** Charged means: charge is separated, not added. The total charge stays zero. Every field line that begins on A ends on B ([Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Typical charges range from nanocoulombs to millicoulombs. **Validity:** The dielectric counts as an ideal insulator; Stage [5](bauformen-und-selbstentladung.html#stufe-5) names the deviation.

:::herleitung Why the same current flows at both terminals
Suppose more flows in than out. Then a net charge $Q_\mathrm{n}$ collects in the component, and the whole component rises in potential relative to its surroundings. How much is shown by a sphere the size of a housing, $r=1$ cm: according to [Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) it has the potential $\varphi=k\,Q_\mathrm{n}/r$, and just 1 µC would give 900 kV. The field of this charge brakes the inflow long before a measurable difference arises. So $Q_\mathrm{n}$ stays practically zero, and Kirchhoff's current law from [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) holds for the component as a whole.
:::

:::analogie
In the pipe of a water circuit, a rubber membrane sits across the flow. The pump presses water against it, and the membrane stretches. Water moves on both sides, none goes through the membrane. Its counterpressure grows with the stretching, and when it reaches the pump pressure, the water stands still. The picture ends at the energy: the membrane stores it in the rubber, the capacitor in the field between the plates (Stage [6](die-gespeicherte-energie.html#stufe-6)).
:::

::::beispiel
A meter in the lead to A shows a constant 0.9 mA for 0.1 s. Then $Q=I\,t=90\,\mu\text{C}$ have been displaced, which is $5.6\cdot10^{14}$ electrons. They have left A, and just as many have arrived on B. A meter in the lead to B shows the same 0.9 mA.
::::

⁠**Limiting case:** If the plates are already at the potentials of the terminals, the drop along the wires is zero and so is the current. A capacitor charged to 9 V draws no current from a 9 V battery.

:::frage So does the current flow through the capacitor or not?
Through the leads yes, through the gap no. From outside you see only the terminals: current goes in at one, and the same current comes out at the other. For the circuit this looks like a continuous current, hence the short way of speaking. But it lasts only as long as the charge is changing.
:::

:::frage Why does the charge stay put when you disconnect the battery?
The electrons on B are attracted by A, but the insulator does not let them through, and the wire ends are open. A path arises only when a conductor connects the terminals (Stage [10](entladen-und-zeitkonstante.html#stufe-10)).
:::

:::aufgabe Exercise 1 ★ What the meters show
<span class="anker" id="aufg-1"></span>

In the lead to plate A of a capacitor, a meter shows a constant 0.45 mA for 2 s.

<ol class="al">

<li>

How much charge has been displaced, and how many electrons is that?

</li>

<li>

What does a meter in the lead to plate B show? How large is the total charge of the capacitor afterward?

</li>

<li>

How many electrons have crossed the insulator?

</li>

</ol>

:::loesung
(a) $Q=I\,t=0.45\,\mathrm{mA}\cdot2\,\mathrm{s}=900\,\mu\text{C}$, so $N=Q/e=5.6\cdot10^{15}$ electrons.

(b) Likewise 0.45 mA: What flows in at A flows out at B. The total charge stays zero; A carries $+900\,\mu\text{C}$, B carries $-900\,\mu\text{C}$.

(c) None. The electrons on B come from the wire; the electrons from A have run into the wire.
:::
:::
