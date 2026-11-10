---
title: Überblick: Ladung, Feld und Potenzial
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1110100
summary: Warum Spannung eine Differenz ist und was sie mit einer Ladung macht
tags: Spannung, Ladung, elektrisches Feld, Potenzial, Bezugspunkt, Widerstand
lang: de
---

## Worum es geht

Auf einer Blockbatterie steht 9 V. Diese Angabe ist eine __Spannung__. Sie sagt nicht, wie viel Energie die Batterie enthält, sondern wie viel Energie jede Einheit __Ladung__ abgibt, die von einem Anschluss zum anderen gelangt: 9 Joule je Coulomb. Ladung ist die Eigenschaft bestimmter Teilchen, elektrische Kräfte auszuüben und zu spüren. Joule ist die Einheit der Energie, Coulomb die Einheit der Ladung. Die Frage dieses Kapitels lautet: *Warum ist Spannung immer eine Differenz zwischen zwei Punkten, und was macht sie mit einer Ladung?*

Die Antwort führt über zwei Begriffe. Ein __elektrisches Feld__ legt für jeden Ort fest, welche Kraft dort auf eine Ladung wirkt. Das __Potenzial__ legt für jeden Ort fest, wie viel Energie je Coulomb eine Ladung dort gegenüber einem frei gewählten Nullpunkt hat, dem __Bezugspunkt__.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Plattenpaar:** zwei ebene Metallplatten A und B im Vakuum (luftleerer Raum), Abstand $d=3$ mm, klein gegen die Plattenbreite. Eine 9-V-Batterie liegt mit dem Pluspol an A, mit dem Minuspol an B. Die Achse $x$ läuft von A ($x=0$) nach B. Zwischen den Platten herrscht das gleichmäßige Feld $E=3$ kV/m (Stufe [5](feldlinien-und-leiter.html#stufe-5) und [8](spannung-und-masse.html#stufe-8)).

</li>

<li>

⁠**Zwei Kugeln:** kleine Kugeln mit $Q_\mathrm{A}=+10$ nC und $Q_\mathrm{B}=-20$ nC im Abstand $r=3$ cm. Kugel A hat die Masse 1 g.

</li>

<li>

⁠**Stromkreis:** dieselbe Batterie an zwei hintereinanderliegenden Widerständen, am ersten 6 V, am zweiten 3 V. Ein __Widerstand__ ist ein Bauteil, in dem durchlaufende Ladung Energie als Wärme abgibt ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)).

</li>

<li>

⁠**Konstanten:** $e=1{,}602\cdot10^{-19}$ C, $m_\mathrm{e}=9{,}109\cdot10^{-31}$ kg, $k=8{,}99\cdot10^{9}\,\mathrm{N\,m^2/C^2}$, $g=9{,}81\,\mathrm{m/s^2}$; die Stufen erklären sie. Alle Zahlen rechnet `rechnung_kap1.py` nach.

</li>

</ul>
:::
