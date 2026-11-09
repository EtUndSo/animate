---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Ergänzung: Licht und Laser
order: 4290800
summary: Wie Elektronen Licht aufnehmen und abgeben und wie daraus ein Verstärker für Licht wird
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Übergang:** $\hbar\omega_{21}=E_2-E_1$, $\lambda_{21}=hc/(E_2-E_1)$, Ausgang besetzt, Ziel frei. Ohne Photon geht die Energie als Wärme ans Gitter.

</li>

<li>

⁠**Fluoreszenz im Nanokristall:** $\hbar\omega(L)=E_\mathrm g+\frac{3\hbar^2\pi^2}{2L^2}\bigl(\frac1{m_\mathrm C^*}+\frac1{m_\mathrm V^*}\bigr)$.

</li>

<li>

⁠**Drei Vorgänge:** Absorption (Photonen $1\to0$), spontane Emission ($0\to1$, $N_2(t)=N_2(0)\mathrm{e}^{-t/\tau_{21}}$), stimulierte Emission ($1\to2$). Absorption und stimulierte Emission haben dieselbe Rate $r_\mathrm{st}=A_\mathrm{Ph}j_\mathrm{Ph}$.

</li>

<li>

⁠**Licht im Stoff:** $j_\mathrm{Ph}(x)=j_\mathrm{Ph}(0)\mathrm{e}^{-\alpha_\mathrm Px}$, $\alpha_\mathrm P=A_\mathrm{Ph}(N_1-N_2)$. Verstärkung nur für $N_2>N_1$, in Bändern $f(E_2)>f(E_1)$.

</li>

<li>

⁠**Gleichgewicht:** $N_2/N_1=\mathrm{e}^{-(E_2-E_1)/(k_\mathrm BT)}<1$. Zwei Niveaus: $N_2/N=r_\mathrm{st}\tau_{21}/(1+2r_\mathrm{st}\tau_{21})<\frac12$.

</li>

<li>

⁠**Drei Niveaus:** Pumpen mit $\hbar\omega_{31}$. Variante 1: $E_3\to E_2$ aktiv, $\tau_{21}<\tau_{32}$. Variante 2: $E_2\to E_1$ aktiv, $r_\mathrm P>1/\tau_{21}$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Elektron nimmt ein Photon auf oder gibt eines ab, wenn $\hbar\omega$ genau zum Abstand zweier Niveaus passt, das Ausgangsniveau besetzt und das Ziel frei ist.

</li>

<li>

Ein passendes Photon wird von einem Elektron unten geschluckt und von einem Elektron oben kopiert, mit derselben Rate. Licht wächst deshalb nur, wenn oben mehr Elektronen sitzen als unten, und das gilt im Gleichgewicht nie.

</li>

<li>

Ein Laser stellt diese Besetzungsumkehr durch ständiges Pumpen auf einem anderen Weg her als dem des verstärkten Lichts, und zwei Spiegel führen die Kopien immer wieder durch den Stoff.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Licht tauscht mit einem Elektron nur ganze Pakete $\hbar\omega$ aus, und Aufnehmen und Kopieren sind derselbe Vorgang in zwei Richtungen. Alles Weitere ist die Frage, welche Niveaus es gibt und wie sie besetzt sind.

| Ergebnis | Woher es kommt |
|---|---|
| Linien im Atom, Kante im Kristall | Nur passende Abstände absorbieren (Stufe [1](absorption-und-emission.html#stufe-1)) |
| Fluoreszenz, Farbe aus der Größe | Abstieg als Wärme, Einsperren kostet $\propto1/L^2$ (Stufe [2](fluoreszenz-und-nanokristalle.html#stufe-2)) |
| Stimulierte Emission verdoppelt | Das Feld treibt die Ladung im eigenen Takt (Stufe [3](spontane-und-stimulierte-emission.html#stufe-3)) |
| $\alpha_\mathrm P\propto N_1-N_2$ | Beide Richtungen haben dieselbe Rate (Stufe [4](die-besetzungsumkehr.html#stufe-4)) |
| Im Gleichgewicht nie Umkehr | $f$ fällt immer mit der Energie (Stufe [4](die-besetzungsumkehr.html#stufe-4)) |
| Zwei Niveaus unter $\frac12$, drei darüber | Pumplicht holt nur im ersten Fall zurück (Stufe [4](die-besetzungsumkehr.html#stufe-4) und [5](der-laser.html#stufe-5)) |
