---
title: Überblick: Kristallgitter
kurz: Überblick
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Kristallgitter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter
knoten: Kapitel 6: Kristallgitter
order: 4160100
summary: Wie wenige Zahlen die Anordnung unzählig vieler Atome festlegen
tags: Kristall, Punktgitter, Basis, Einheitszelle, Bravais-Gitter, Koordinationszahl, Packungsdichte, Millersche Indizes
lang: de
---

## Worum es geht

Ein Stück Silizium von der Größe eines Zuckerwürfels enthält mehr Atome, als jemand je aufzählen könnte. Trotzdem genügen wenige Zahlen, um zu sagen, wo jedes einzelne sitzt. Wer eine Siliziumscheibe bestellt, nennt drei Ziffern, und der Hersteller weiß, wie die Atome an der Oberfläche liegen. Die Frage dieses Kapitels lautet: *Wie beschreibt man die Anordnung unzählig vieler Atome mit wenigen Zahlen, und wie benennt man darin Orte, Richtungen und Ebenen?* Wer das kann, rechnet aus einer Strukturangabe Abstände, Dichten und Winkel aus.

Der Weg führt über acht Begriffe. Ein __Kristall__ ist eine regelmäßige, sich wiederholende Anordnung von Atomen. Das __Punktgitter__ sagt, wo sich etwas wiederholt, die __Basis__, was sich wiederholt. Die __Einheitszelle__ ist eine Kachel, die den Raum lückenlos füllt. Ein __Bravais-Gitter__ ist ein Punktgitter, in dem jeder Punkt dieselbe Umgebung hat. Die __Koordinationszahl__ zählt die nächsten Nachbarn eines Atoms, die __Packungsdichte__ den gefüllten Anteil des Raums. __Millersche Indizes__ sind Zahlen, die eine Ebene im Kristall benennen.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Würfelkanten bei Raumtemperatur:** Al 0,4050 nm, W 0,3165 nm, Si 0,5431 nm, GaAs 0,5653 nm, NaCl 0,5640 nm.

</li>

<li>

⁠**Stoffmengen:** $N_\mathrm{Av}=6{,}022\cdot10^{23}\,\mathrm{mol^{-1}}$ Teilchen je Mol (__Avogadro-Konstante__). Molmassen in g/mol: Al 26,98, Si 28,09, W 183,84.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap6.py` nach.
:::
