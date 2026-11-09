---
title: Überblick: Der MOSFET
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4270100
summary: Wie eine isolierte Elektrode den Strom zwischen zwei Kontakten steuert
tags: MOSFET, Source, Drain, Kanal, Gradual Channel Approximation, Ausgangskennlinie, Transferkennlinie, Unterschwellstrom
lang: de
---

## Worum es geht

Ein MOS-Kondensator speichert nur Ladung. Er erzeugt aber an der Oberfläche des Halbleiters eine leitende Schicht, ohne dass Strom durch das Gate fließt ([Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html)). Setzt man links und rechts dieser Schicht je einen Kontakt, entsteht ein Schalter, den eine Spannung betätigt. Die Frage dieses Kapitels lautet: *Wie groß ist der Strom zwischen zwei Kontakten, wenn eine isolierte Elektrode die Ladung zwischen ihnen festlegt, und was bleibt von ihm unterhalb der Schwellspannung?* Wer das beantworten kann, kann die Kennlinien des häufigsten Bauelements der Elektronik vorhersagen und es für einen gewünschten Strom auslegen.

Der Weg führt über acht Begriffe. Der __MOSFET__ (metal-oxide-semiconductor field-effect transistor) ist ein MOS-Kondensator mit zwei zusätzlichen Kontakten. Die __Source__ ist der Kontakt, aus dem die Ladungsträger kommen, der __Drain__ der, in den sie fließen. Der __Kanal__ ist die leitende Schicht dazwischen. Die __Gradual Channel Approximation__ berechnet seinen Strom aus dem Plattenkondensator. Die __Ausgangskennlinie__ zeigt den Strom über der Spannung zwischen Drain und Source, die __Transferkennlinie__ über der Spannung am Gate. Der __Unterschwellstrom__ ist der kleine Strom unterhalb der Schwellspannung.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Wärme:** $T=300$ K, $V_\mathrm T=k_\mathrm BT/e=25{,}85$ mV. Die Temperaturspannung $V_\mathrm T$ ist nicht die Schwellspannung $V_\mathrm{th}$.

</li>

<li>

⁠**Substrat und Isolator wie [Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html):** p-Silizium mit $N_\mathrm A=3\cdot10^{16}\,\mathrm{cm^{-3}}$, $n_\mathrm i=8{,}9\cdot10^{9}\,\mathrm{cm^{-3}}$, $n_{p0}=2{,}6\cdot10^{3}\,\mathrm{cm^{-3}}$, $\varepsilon=1{,}036\cdot10^{-10}$ F/m. $\mathrm{SiO_2}$ mit $d_\mathrm{IS}=20$ nm und $\varepsilon_\mathrm{IS}=3{,}9\,\varepsilon_0$, also $C'_\mathrm{IS}=172{,}7\,\mathrm{nF/cm^2}$ und $\gamma=0{,}578\,\sqrt{\mathrm V}$.

</li>

<li>

⁠**Gate wie [Teil 16](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-reale-mos-kondensator/realer-mos-kondensator.html):** Aluminium mit $\Phi_\mathrm M=4{,}10$ eV, $Q'_\mathrm{IS}=8{,}0\,\mathrm{nC/cm^2}$, $Q'_\mathrm{SS}=3{,}2\,\mathrm{nC/cm^2}$. Das ergibt $V_\mathrm{FB}=-0{,}96$ V und $V_\mathrm{th}=0{,}323$ V.

</li>

<li>

⁠**Source und Drain:** n$^+$-Gebiete mit $N_\mathrm D=5\cdot10^{18}\,\mathrm{cm^{-3}}$.

</li>

<li>

⁠**Kanal:** $L=5$ µ m, $W=50$ µ m, $\mu_\mathrm n=500\,\mathrm{cm^2/(V\,s)}$, $D_\mathrm n=12{,}9\,\mathrm{cm^2/s}$. Die Beweglichkeit ist kleiner als im Volumen ([Teil 12](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/strom-im-halbleiter/strom-im-halbleiter.html)), denn die Elektronen streuen zusätzlich an der Grenzfläche. Alle Zahlen rechnet `rechnung_kap17.py` nach.

</li>

</ul>
:::
