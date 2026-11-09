---
title: Stage 2: Slow electrons, immediate current
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Current, Resistance and Kirchhoff's Laws
order: 1120300
summary: Stage 1 needs a velocity v .
tags: crystal lattice, mobility, mean free path
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
Stage [1](strom-ist-bewegte-ladung.html#stufe-1) needs a velocity $v$. This stage shows why it is constant and tiny, and resolves the contradiction with the lamp that lights up at once.
:::

**The idea.** In a metal, at least one electron per atom is no longer bound to its atom. The positive ions left behind form a regular __crystal lattice__. If a voltage is applied, there is a field in the wire. It accelerates every free electron against the field direction. After a short time, the electron is scattered and gives the directed velocity it gained to the lattice, then it starts again (Fig. [2](#abb-2)). On average, a constant velocity remains: the collisions take exactly as much as the field gives.

:::abbildung et1/k2drift 2
Left: path of an electron in the lattice (schematic, not to scale). Right: model for the directed part of the velocity. It grows in the field up to $v_\mathrm{max}$ and falls to zero at a collision. Its mean value is the drift velocity $v_\mathrm D=v_\mathrm{max}/2$.
:::

:::satz Theorem 2.1 (Drift velocity)
<span class="anker" id="satz-2-1"></span>

If each flight between two collisions takes the time $T$, then

<span class="anker" id="gl-2-1"></span>
$$|\vec v_\mathrm{max}|=\frac{e\,|\vec E|}{m_\mathrm e}\,T,\qquad\vec v_\mathrm D=-\mu\,\vec E,\qquad\mu=\frac{e\,T}{2\,m_\mathrm e}. \tag{2.1}$$

With Stage [1](strom-ist-bewegte-ladung.html#stufe-1), the current gives $v_\mathrm D=j/(n\,e)=I/(n\,e\,A)$.
:::

⁠**How to read it:** $\vec v_\mathrm D$ is the drift velocity in m/s. The minus sign says: electrons are negative, they move against $\vec E$. $\mu$ is the __mobility__, the drift velocity per field strength, in $\mathrm{m^2/(V\,s)}$. It is a material constant, in copper $4.3\cdot10^{-3}\,\mathrm{m^2/(V\,s)}$. $T$ is the flight time, around 49 fs in copper. In this time, the electron covers on average the __mean free path__ $\lambda$. **Validity:** [(2.1)](#gl-2-1) is a model. It counts only the part of the velocity produced by the field. In addition, the electrons fly randomly in all directions at around 1600 km/s. This motion cancels on average, carries no current and is preserved in the collisions.

:::herleitung From field to drift
From $F=m_\mathrm e\,a$ and $F=e\,E$ ([Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)) follows the acceleration $a=e\,E/m_\mathrm e$. A flight starts with a directed part of zero, so $v(t)=a\,t$ and $v_\mathrm{max}=a\,T$. The sawtooth has the mean value $v_\mathrm{max}/2=e\,E\,T/(2\,m_\mathrm e)$. The velocity does not keep growing, because each collision resets it.
:::

::::beispiel
In the wire, $v_\mathrm D=j/(n\,e)=6\cdot10^3\,\mathrm{A/m^2}/(1.36\cdot10^{10}\,\mathrm{C/m^3})=4.4\cdot10^{-7}$ m/s, that is 0.44 µ m/s. For one meter, an electron would need 26 days. The field in the wire is $E=v_\mathrm D/\mu=0.10$ mV/m. The drift is so small because the wire contains so many charge carriers: 6800 C per meter only have to deliver 3 mC per second.
::::

⁠**In short:** The drift velocity is the current divided by the free charge per meter. **Limiting cases:** Without a field, $v_\mathrm D=0$. Twice the current gives twice the drift. Many collisions ($T\to0$) give $\mu\to0$: the material does not conduct.

**Why the current is there at once all the same.** Two things travel in the wire, and they must not be confused. The electrons drift slowly. The field, by contrast, spreads along the wire as an electromagnetic wave when the switch closes, in cables at around $2\cdot10^8$ m/s. The electrons are already everywhere in the wire. Each one starts drifting as soon as the field front reaches it (Fig. [3](#abb-3)). After a few such transit times, the steady current flows in the whole circuit. The energy travels with the field, not with the electrons. The front takes 5 ns for one meter. In these 5 ns, an electron drifts 2.2 fm, which is around 100 000 times less than the distance between two copper atoms. The two speeds differ by a factor of $4.5\cdot10^{14}$.

:::abbildung et1/k2sofort 3
One meter of wire at three moments after the switch on the left closes. The field front passes through it in 5 ns. Behind the front all electrons drift; ahead of it they are at rest on average. The electrons themselves have practically not advanced in this time.
:::

:::analogie
A bicycle chain is full of links everywhere. Push the pedal at the front and it moves at the back at the same moment, although each link moves only slowly. The analogy ends at the mechanism: chain links push one another mechanically, and the effect travels through the metal at the speed of sound. In the wire, a field travels, and its speed is close to the speed of light.
:::

:::frage Part 1 says that $\vec E=0$ in metal. Why is there a field in the wire, and how does it follow the curves?
$\vec E=0$ holds only in the state of rest, when all charges have come to rest. The source does not allow that: it removes electrons at one end and supplies them at the other, so the state of rest is never reached. A small field remains, here 0.10 mV/m. At bends, tiny charges collect on the wire surface. Their field steers $\vec E$ along the wire everywhere; otherwise the electrons would run into the wall, and the charge there would keep growing.
:::

:::zusatz How fast electrons really are
The random motion is $3.6\cdot10^{12}$ times faster than the drift in the wire. It is a consequence of quantum mechanics and persists even near absolute zero. The flight times are spread out, and with scattered times the factor $\frac12$ in $\mu$ disappears if $T$ is the mean flight time. Then $T=25$ fs, and the free path $\lambda$ is around 39 nm, about 150 atomic spacings. The picture “collision with every atom” is therefore too crude: a perfect lattice at rest does not scatter electrons at all. They collide with lattice vibrations, impurity atoms and defects.
:::

:::aufgabe Exercise 2 ★★ Drift and transit time
<span class="anker" id="aufg-2"></span>

The cable from Exercise [1](strom-ist-bewegte-ladung.html#aufg-1) is made of copper and is 30 m long.

<ol class="al">

<li>

Calculate $v_\mathrm D$ and the field $E=\rho\,j$ in the cable.

</li>

<li>

How long would an electron take for the 30 m, and how long the field front?

</li>

<li>

Prediction: How does $v_\mathrm D$ change if the cross section doubles at the same current?

</li>

</ol>

:::loesung
(a) $j=1.07\cdot10^7\,\mathrm{A/m^2}$, $v_\mathrm D=j/(n\,e)=0.78$ mm/s. $E=\rho\,j=0.18$ V/m.

(b) Electron: $30\,\mathrm{m}/0.78\,\mathrm{mm/s}=3.8\cdot10^4$ s $=10.6$ h. Field front: $30\,\mathrm{m}/(2\cdot10^8\,\mathrm{m/s})=150$ ns.

(c) It halves: twice as many charge carriers per meter share the same current, $v_\mathrm D=I/(n\,e\,A)$.
:::
:::
