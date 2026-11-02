---
title: Überblick: Maschenstrom- und Knotenpotentialverfahren
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Maschenstrom- und Knotenpotentialverfahren
order: 1180100
summary: Warum ein Netz mit wenigen Unbekannten auskommt
tags: 
lang: de
---

## Worum es geht

Das Netz aus [Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) hat sechs Zweige. Jeder trägt einen Strom und eine Spannung, das sind zwölf Unbekannte, und erst nach langem Einsetzen blieben drei Gleichungen übrig. Eine Schaltung mit Transistoren hat Hunderte Zweige. Die Frage dieses Kapitels lautet: *Wie wenige Unbekannte reichen für ein ganzes Netz, und wie schreibt man die Gleichungen hin, ohne umzuformen?*



**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Das Netz** (Abb. [1](wie-viele-groen-sind-frei.html#abb-1)) hat drei Knoten: die Masse 0 und die Knoten 1 und 2. Links speist eine Batterie mit $U_\mathrm q=9$ V und Innenwiderstand $R_1=1\,\mathrm{k\Omega}$ ([Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)), rechts eine reale Stromquelle mit $I_\mathrm q=4$ mA und $R_5=5\,\mathrm{k\Omega}$ parallel. Dazwischen liegen $R_2=4\,\mathrm{k\Omega}$ von 1 nach Masse, $R_3=2\,\mathrm{k\Omega}$ von 1 nach 2 und $R_4=10\,\mathrm{k\Omega}$ von 2 nach Masse.

</li>

<li>

⁠**Der Verstärker** (Stufe [8](gesteuerte-quellen-und-verstarker.html#stufe-8)) ist das Modell aus [Teil 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html): Eingangswiderstand $R_\mathrm i=2\,\mathrm{k\Omega}$, gesteuerte Stromquelle mit $g=50$ mS, Ausgangswiderstand $R_\mathrm o=20\,\mathrm{k\Omega}$, Last $R_\mathrm L=5\,\mathrm{k\Omega}$.

</li>

<li>

⁠**Einheiten:** Gerechnet wird in V, mA, k$\Omega$ und mS. Wegen $\mathrm{k\Omega\cdot mA}=\mathrm V$ und $\mathrm{mS\cdot V}=\mathrm{mA}$ tauchen keine Zehnerpotenzen auf. Alle Zahlen rechnet `rechnung_kap8.py` nach.

</li>

</ul>
:::
