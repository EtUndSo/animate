---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1181200
summary: Warum ein Netz mit wenigen Unbekannten auskommt
tags: Maschenstromverfahren, Maschenstrom, Knotenpotentialverfahren, Knotenpotential, Bezugsknoten, Widerstandsmatrix, Leitwertmatrix, modifizierte Knotenanalyse
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Netz mit $z$ Zweigen und $k$ Knoten hat $m=z-k+1$ unabhängige Maschen und $k-1$ unabhängige Knoten. Von den $z$ Strömen sind nur $m$ frei, von den $z$ Spannungen nur $k-1$.

</li>

<li>

Das __Maschenstromverfahren__ rechnet mit dem __Maschenstrom__, einem gedachten Kreisstrom je Masche. Er tritt in jeden Knoten ein und wieder aus, also gilt die Knotenregel von selbst. Das __Knotenpotentialverfahren__ rechnet mit dem __Knotenpotential__, der Spannung jedes Knotens gegen einen frei gewählten __Bezugsknoten__. Jede Zweigspannung ist eine Differenz, also gilt die Maschenregel von selbst.

</li>

<li>

Die verbleibenden Gleichungen liest man als Matrix aus der Schaltung ab: In der __Widerstandsmatrix__ steht auf der Diagonale die Summe der Widerstände einer Masche, daneben die gemeinsamen Widerstände zweier Maschen. In der __Leitwertmatrix__ steht auf der Diagonale die Summe der Leitwerte an einem Knoten, daneben der negative Leitwert zwischen zwei Knoten. Die __modifizierte Knotenanalyse__ nimmt zusätzlich den Strom jeder Spannungsquelle als Unbekannte, und so rechnet SPICE.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Von $z$ Strömen sind $m=z-k+1$ frei, von $z$ Spannungen $k-1$. Das sind die Größen der beiden Verfahren. Das Knotenpotentialverfahren ist kleiner, wenn $z>2k-2$.

</li>

<li>

Maschenströme laufen im Kreis, die Knotenregel gilt von selbst. Zweigstrom = Summe der Maschenströme mit Vorzeichen. $\mathbf Z\,\mathbf I=\mathbf U_\mathrm q$: Diagonale Summe der Widerstände der Masche, daneben $\pm$ gemeinsame Widerstände, rechts treibende Spannungen.

</li>

<li>

Knotenpotentiale sind Höhen, die Maschenregel gilt von selbst. Zweigspannung = Differenz. $\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$: Diagonale Summe der Leitwerte am Knoten, daneben der negative Koppelleitwert, rechts hineinfließende Quellenströme.

</li>

<li>

Stromquellen stören die Maschen, Spannungsquellen die Knoten: Reale Quellen wandelt man vorher um. Innere Größen der Quelle rechnet man im ursprünglichen Netz.

</li>

<li>

Jedes Bauteil stempelt unabhängig: $G$ auf vier Plätze, Stromquelle nur rechts, $g$ in die Spalten $p$, $q$. Bezugsknoten streichen. Die Matrix ist dünn besetzt, gesteuerte Quellen brechen die Symmetrie.

</li>

<li>

MNA: Jede Spannungsquelle bringt ihren Strom als Unbekannte und $U_i-U_k=U_\mathrm q$ als Gleichung mit. So rechnet SPICE. Eine 0-V-Quelle misst Strom. Die Spannungsverstärkung ist minus Steilheit mal Lastwiderstand.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Kirchhoff verlangt zweierlei: die Knotenregel und die Maschenregel. Wählt man die Unbekannten so, dass eine der beiden Regeln für jeden beliebigen Zahlenwert gilt, muss man nur noch die andere aufschreiben. Die Zahl der Unbekannten ist dann genau die Zahl der übrigen Gleichungen.

| Ergebnis | Woher es kommt |
|---|---|
| $m$ freie Ströme, $k-1$ freie Spannungen | Ein Baum bestimmt, was vorgegeben werden kann und was daraus folgt (Stufe [1](wie-viele-groen-sind-frei.html#stufe-1)) |
| Maschenströme | Ein Kreisstrom bringt keinem Knoten etwas hinein (Stufe [2](maschenstrome-erfullen-die-knotenregel.html#stufe-2)) |
| Widerstandsmatrix $\mathbf Z$ | Der eigene Strom läuft durch alle Widerstände der Masche, ein fremder nur durch die gemeinsamen (Stufe [3](das-maschenstromverfahren.html#stufe-3)) |
| Knotenpotentiale | Ein Umlauf kehrt zum Anfangspotenzial zurück (Stufe [4](potenziale-erfullen-die-maschenregel.html#stufe-4)) |
| Leitwertmatrix $\mathbf Y$ | Das eigene Potenzial treibt Strom durch alle Leitwerte am Knoten, ein fremdes nur durch den gemeinsamen (Stufe [5](das-knotenpotentialverfahren.html#stufe-5)) |
| Wahl des Verfahrens | Die kleinere der beiden Zahlen gewinnt, also $z>2k-2$ oder nicht (Stufe [6](welches-verfahren-wann.html#stufe-6)) |
| Stempel und Netzliste | Ein Bauteil berührt nur seine zwei Knoten (Stufe [7](stempel-und-netzliste.html#stufe-7)) |
| Unsymmetrische Matrix | Eine gesteuerte Quelle hängt von fremden Knoten ab (Stufe [8](gesteuerte-quellen-und-verstarker.html#stufe-8)) |
| Modifizierte Knotenanalyse | Eine ideale Spannungsquelle hat keinen Leitwert, ihr Strom wird Unbekannte (Stufe [9](die-modifizierte-knotenanalyse.html#stufe-9)) |
