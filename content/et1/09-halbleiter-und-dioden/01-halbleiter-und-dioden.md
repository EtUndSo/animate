---
title: Überblick: Halbleiter und Dioden
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
order: 1190100
summary: Wie aus Silizium ein Ventil für Strom wird und wie man mit ihm rechnet
tags: Diode, Halbleiter, Dotierung, Ladungsträger, pn-Übergang, Raumladungszone, Kennlinie, Arbeitspunkt
lang: de
---

## Worum es geht

Ein Ladegerät macht aus der Wechselspannung der Steckdose die Gleichspannung für den Akku. Das Bauteil, das dafür sorgt, heißt __Diode__: Es lässt Strom in einer Richtung durch (Durchlassrichtung) und sperrt ihn in der anderen (Sperrrichtung). Es besteht aus einem __Halbleiter__, einem Stoff, dessen Leitfähigkeit zwischen Metall und Isolator liegt und sich gezielt einstellen lässt. Die Frage dieses Kapitels lautet: *Wie wird aus einem Stück Silizium ein Ventil für Strom, und wie rechnet man mit einem Bauteil, das dem ohmschen Gesetz nicht folgt?*

Die Antwort führt über sechs Begriffe. __Dotierung__ heißt: Man baut wenige Fremdatome ein und legt so fest, wie viele __Ladungsträger__ (bewegliche Ladungen) der Kristall hat. An der Grenze zweier verschieden dotierter Gebiete, dem __pn-Übergang__, bildet sich von selbst die __Raumladungszone__, eine dünne Schicht ohne bewegliche Ladungen, die als Energiebarriere wirkt. Die __Kennlinie__ ist der Graph des Stroms über der Spannung, der __Arbeitspunkt__ das Paar aus Spannung und Strom, das sich in einer Schaltung einstellt.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Diode:** Silizium, Sättigungssperrstrom $I_\mathrm S=10^{-14}$ A (der kleine Strom in Sperrrichtung), Temperaturspannung $U_T=25{,}85$ mV (Wärmeenergie je Ladung) bei $T=300$ K (27 °C). Als Schaltermodell gilt die Durchlassspannung $U_\mathrm F=0{,}7$ V (Spannung an der leitenden Diode).

</li>

<li>

⁠**pn-Übergang:** je $10^{16}$ Fremdatome pro cm$^3$ auf beiden Seiten, $n_\mathrm i=10^{10}\,\mathrm{cm^{-3}}$ freie Elektronen in reinem Silizium, Permittivitätszahl $\varepsilon_\mathrm r=11{,}7$.

</li>

<li>

⁠**Schaltung:** Quelle $U_0=5$ V, Widerstand $R=1\,\mathrm{k\Omega}$, Diode in Reihe.

</li>

<li>

⁠**Gleichrichter:** Sinusspannung mit Scheitelwert 12 V und 50 Hz, Last 1 k$\Omega$.

</li>

<li>

⁠**Konstanten:** $e=1{,}602\cdot10^{-19}$ C, $k_\mathrm B=1{,}3806\cdot10^{-23}$ J/K. Alle Zahlen rechnet `rechnung_kap9.py` nach.

</li>

</ul>
:::
