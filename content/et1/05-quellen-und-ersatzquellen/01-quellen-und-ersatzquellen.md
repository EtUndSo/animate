---
title: Überblick: Quellen und Ersatzquellen
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1150100
summary: Warum zwei Zahlen ein ganzes Netzwerk ersetzen
tags: 
lang: de
---

## Worum es geht

Ein Sensor hängt an zwei Drähten, dahinter liegt eine Schaltung aus Dutzenden Bauteilen. Er spürt nur Spannung und Strom an seinen Anschlüssen. Die Frage dieses Kapitels lautet: *Wie viele Zahlen braucht man, um ein ganzes Netzwerk an zwei Anschlüssen zu beschreiben?* Die Antwort lautet zwei, solange das Netzwerk linear ist: Es enthält nur Widerstände und feste Quellen, doppelte Ursache ergibt doppelte Wirkung.

Der Weg dorthin hat drei Teile. Die Stufen [1](widerstande-zusammenfassen.html#stufe-1) bis [3](stern-und-dreieck.html#stufe-3) fassen Netze ohne Quelle zusammen. Die Stufen [4](ideale-quellen.html#stufe-4) bis [7](quellen-zusammenschalten.html#stufe-7) führen Quellen ein und zeigen, dass auch sie Geraden sind. Die Stufen [8](uberlagerung.html#stufe-8) und [9](thevenin-und-norton.html#stufe-9) beweisen, dass das für jedes lineare Netz gilt, Stufe [10](der-r-2r-wandler.html#stufe-10) nutzt es in einem Wandler.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Batterie:** die 9-V-Blockbatterie aus [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html). Ihre Quellenspannung (die Spannung, die die Chemie liefert) ist $U_\mathrm{q}=9$ V, ihr Innenwiderstand $R_\mathrm{q}=2\,\Omega$.

</li>

<li>

⁠**Last:** das angeschlossene Gerät, mit dem Widerstand $R_\mathrm{L}=16\,\Omega$. Die Stufen [1](widerstande-zusammenfassen.html#stufe-1) bis [3](stern-und-dreieck.html#stufe-3) bauen Last-Netze aus vielen Widerständen, die alle genau 16 $\Omega$ ergeben.

</li>

<li>

⁠**Netzwerk N:** zwei Quellen und zwei Widerstände (Abb. [9](uberlagerung.html#abb-9)): $U_\mathrm{q1}=18$ V, $R_1=6\,\Omega$, $R_2=3\,\Omega$, $I_\mathrm{q2}=1{,}5$ A. Stufe [9](thevenin-und-norton.html#stufe-9) zeigt: Von außen ist N nicht von der Batterie zu unterscheiden.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap5.py` nach.
:::
