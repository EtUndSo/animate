---
title: Überblick: Zufallssignale
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3270100
summary: Mittelwerte, Verteilungen, Leistungsdichte, Rauschen in Systemen und der optimale Empfänger
tags: 
lang: de
---

## Worum es geht

Das Rauschen eines Widerstands, Sprache, ein Datenstrom: Solche Signale kann man nicht vorhersagen. Ihren genauen Verlauf kennt man nicht, wohl aber ihre *Eigenschaften im Mittel*: wie groß sie typischerweise sind, wie schnell sie sich ändern, welche Frequenzen sie enthalten. Dieses Kapitel zeigt, wie man solche Zufallssignale beschreibt, was ein LTI-System mit ihnen macht und wie man ein bekanntes Signal im Rauschen am sichersten erkennt.

**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Gleichverteilte Zufallszahlen** zwischen $-\frac12$ und $\frac12$ (Varianz $\frac{1}{12}$), auch als zeitdiskretes weißes Rauschen.

</li>

<li>

⁠**Widerstand** $R=1\,\mathrm{k\Omega}$ bei 290 K, Bandbreite 20 kHz (Audio).

</li>

<li>

⁠**Rekursives System** $g(n)=s(n)+0{,}6\,g(n-1)$ aus [Kapitel 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html).

</li>

</ul>

:::
