---
title: Stage 6: The stored energy
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / The Capacitor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Chapter 3: The Capacitor
order: 1130700
summary: Charging costs energy, because every further charge has to run against the voltage already present.
tags: energy density
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
Charging costs energy, because every further charge has to run against the voltage already present. This stage calculates how much it is and where the energy is afterward.
:::

**The idea.** Voltage is energy per charge ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Bringing the small charge $\Delta q$ from the negative to the positive plate costs $\Delta W=u\,\Delta q$. The first charges cost almost nothing, because there is no field yet. The last ones cost the full amount $U$ per coulomb. On average each charge pays $U/2$. This is the area under the line $u=q/C$ (Fig. [6](#abb-6) left).

:::satz Theorem 6.1 (Energy in the capacitor)
<span class="anker" id="satz-6-1"></span>

A capacitor with the charge $Q$ and the voltage $U$ stores

<span class="anker" id="gl-6-1"></span>
$$W=\int_0^Q\frac qC\,\mathrm{d} q=\frac{Q^2}{2C}=\frac12\,Q\,U=\frac12\,C\,U^2. \tag{6.1}$$

It resides in the field between the plates. For the parallel-plate capacitor, with the volume $V=A\,d$,

<span class="anker" id="gl-6-2"></span>
$$W=\frac12\,\varepsilon\,E^2\cdot A\,d,\qquad w=\frac WV=\frac12\,\varepsilon\,E^2. \tag{6.2}$$

Here $w$ is the __energy density__, the energy per volume.
:::

⁠**How to read it:** $W$ in J, $C$ in F, $U$ in V, $w$ in J/m$^3$. The voltage enters squared: twice the voltage means twice the charge, and that runs against twice the voltage. $q$ is the charge during charging, $Q$ its final value. **Validity:** $C$ constant, no leakage current.

:::herleitung Energy from force and distance
The force on $\Delta q$ in the field is $F=\Delta q\,E$ ([Chapter 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Over the distance $\Delta s$ between the plates, this costs $\Delta W=F\,\Delta s=\Delta q\,E\,\Delta s$. With $E\,\Delta s=u$ it follows that $\Delta W=\Delta q\,u$, and with $u=q/C$, $\Delta W=\frac qC\,\Delta q$. For small $\Delta q$, the sum of all portions becomes the integral [(6.1)](#gl-6-1).

The circuit side gives the same result. The power (energy per time) is $p=u\,i$ ([Chapter 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). With $i=C\,\mathrm{d} u/\mathrm{d} t$, $W=\int u\,i\,\mathrm{d} t=C\int_0^Uu\,\mathrm{d} u=\frac12CU^2$.

⁠**From the component to the field:** Substituting $C=\varepsilon A/d$ and $U=E\,d$ in [(6.1)](#gl-6-1) gives [(6.2)](#gl-6-2).
:::

:::abbildung et1/k3energie 6
Left: Six portions of 150 µC each. Each portion costs $u\,\Delta q$; its voltage is the one in the middle of the portion. The area of all the bars is the area of the triangle under $u=q/C$, that is, $W=\frac12QU=4.05$ mJ. Right: The energy resides in the space between the plates, per volume $w=\frac12\varepsilon E^2$. In the metal, $E=0$.
:::

**Where the energy resides.** The metal cannot contain it, because there $E=0$ and the electrons are only displaced a tiny bit (Stage [2](die-kapazitat.html#stufe-2)). Equation [(6.2)](#gl-6-2) says: every cubic meter of field contains $\frac12\varepsilon E^2$. That this is more than a way of calculating is shown by an experiment. You disconnect the battery and pull the plates apart. $Q$ stays, and so does $E=Q/(\varepsilon A)$. But the field fills more volume, and the field energy grows by $\frac12\varepsilon E^2A\,\Delta d$. The energy comes from the hand pulling against the attraction of the plates. Each plate feels only the field of the other, which is half of $E$, so $F=\frac12QE$. The work is $F\,\Delta d=\frac12QE\,\Delta d=\frac12\varepsilon E^2A\,\Delta d$, exactly the increase. That field energy exists independently of charges is shown by light: it carries energy through empty space.

::::beispiel
At 9 V the capacitor of the RC circuit stores $W=\frac12\cdot100\,\mu\text{F}\cdot(9\,\mathrm{V})^2=4.05$ mJ, the pair of plates only 1.20 nJ. There $w=\frac12\varepsilon_0(3\,\mathrm{kV/m})^2=3.98\cdot10^{-5}$ J/m$^3$, times $V=3\cdot10^{-5}\,\mathrm{m^3}$ gives the same 1.20 nJ. A 100 F supercap stores a respectable 365 J at 2.7 V, but a 9 V rectangular battery with 0.5 Ah stores 16 kJ, four million times as much as the 100 µF capacitor. Capacitors store little energy but release it very quickly, for example in a camera flash.
::::

⁠**Limiting case:** For $U\to0$, $W\to0$: no field, no energy. **Check:** $\mathrm{F\cdot V^2}=\frac{\mathrm{C}}{\mathrm V}\cdot\mathrm{V^2}=\mathrm{C\,V}=\mathrm J$.

:::frage Why not $W=Q\,U$? After all, voltage times charge is energy.
$Q\,U$ is right when the whole charge passes through the full voltage. During charging, however, $U$ is the final value; the voltage grows from zero. The battery really does give up $Q\,U$, because every charge runs through it at the full voltage. The capacitor receives only half. Where the rest goes is clarified by Exercise [11](aufladen-uber-einen-widerstand.html#aufg-11).
:::

:::aufgabe Exercise 7 ★★★ Pulling the plates apart
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

A 470 µF capacitor is connected to 12 V, then to 24 V. How large is $W$ in each case?

</li>

<li>

The pair of plates is charged to 9 V and disconnected. Then $d$ is doubled to 6 mm. How large are $C$, $U$, $E$ and $W$? Check the increase in $W$ with $F\,\Delta d$.

</li>

<li>

The same, but the battery stays connected. Now $W$ falls, even though the hand does work. Where does the energy go? The mechanical work here is 0.60 nJ.

</li>

</ol>

:::loesung
(a) $W=\frac12\cdot470\,\mu\text{F}\cdot(12\,\mathrm{V})^2=33.8$ mJ, at 24 V four times that, 135 mJ.

(b) $Q=266$ pC stays. $C=14.8$ pF, $U=Q/C=18$ V, $E=U/d=3$ kV/m as before. $W=\frac12QU=2.39$ nJ; the increase is 1.20 nJ. The force is $F=\frac12QE=0.398\,\mu\text{N}$, and $F\,\Delta d=0.398\,\mu\text{N}\cdot3\,\mathrm{mm}=1.20$ nJ. The two agree.

(c) $U=9$ V stays. $C=14.8$ pF, $Q=133$ pC, $E=1.5$ kV/m, $W=0.60$ nJ. The field loses 0.60 nJ. Added to this are 0.60 nJ from the hand. Both flow into the battery, because 133 pC run back at 9 V: $133\,\mathrm{pC}\cdot9\,\mathrm{V}=1.20$ nJ. The battery is charged a little.
:::
:::
