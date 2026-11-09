---
title: Überblick: Strom, Widerstand und Kirchhoff
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom, Widerstand und Kirchhoff
order: 1120100
summary: Warum Elektronen kriechen, der Strom aber sofort da ist, und warum Netze Erhaltungssätzen gehorchen
tags: Strom, Widerstand, ohmsche Gesetz, Knotenregel, Maschenregel
lang: de
---

## Worum es geht

Schließt man einen Stromkreis, leuchtet die Lampe im selben Augenblick. Dabei kriechen die Elektronen im Draht rund 2000-mal langsamer als eine Schnecke. Ein __Strom__ ist bewegte Ladung, gemessen als Ladung je Zeit. Ein __Widerstand__ ist ein Bauteil, das diese Bewegung bremst und ihre Energie in Wärme umwandelt. Die Frage dieses Kapitels lautet: *Wie wird aus einer Spannung ein Strom, und wie verteilt er sich in einem Netz aus vielen Bauteilen?*

Die Antwort besteht aus drei Gesetzen. Das __ohmsche Gesetz__ verknüpft Spannung und Strom an einem Bauteil. Die __Knotenregel__ sagt, dass an einer Verzweigung kein Strom verschwindet. Die __Maschenregel__ sagt, dass die Spannungen längs eines geschlossenen Wegs zusammen null ergeben.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Kette:** die 9-V-Batterie aus [Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) an zwei hintereinanderliegenden Widerständen $R_1=2\,\mathrm{k\Omega}$ und $R_2=1\,\mathrm{k\Omega}$. Es fließen 3 mA, an $R_1$ liegen 6 V, an $R_2$ liegen 3 V.

</li>

<li>

⁠**Draht:** Kupfer, Länge $L=1$ m, Querschnitt $A=0{,}5\,\mathrm{mm^2}$, spezifischer Widerstand (Materialkonstante, Stufe [3](das-ohmsche-gesetz-aus-feld-und-stoen.html#stufe-3)) $\rho=1{,}7\cdot10^{-8}\,\mathrm{\Omega\,m}$, Dichte der freien Elektronen $n=8{,}5\cdot10^{28}\,\mathrm{m^{-3}}$ (eines je Atom). Er führt die 3 mA der Kette.

</li>

<li>

⁠**Netz:** eine 9-V-Quelle und fünf Widerstände zwischen vier Verzweigungspunkten, $R_\mathrm a=2$, $R_\mathrm b=5$, $R_\mathrm c=3$, $R_\mathrm d=1$, $R_\mathrm e=2$ (alle in $\mathrm{k\Omega}$), Abb. [7](knoten-zweige-maschen.html#abb-7).

</li>

<li>

⁠**Konstanten:** $e=1{,}602\cdot10^{-19}$ C, $m_\mathrm e=9{,}109\cdot10^{-31}$ kg.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap2.py` nach.
:::
