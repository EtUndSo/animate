---
title: Überblick: Der Kondensator
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1130100
summary: Wie Strom in einen Isolator fließt und wo danach die Energie steckt
tags: Kondensator, Elektrode, Dielektrikum, Kapazität, Plattenkondensator, RC-Kreis
lang: de
---

## Worum es geht

Zwei Metallplatten, dazwischen ein Isolator: Dieses Bauteil heißt __Kondensator__. Schließt man es an eine Batterie an, fließt in den Zuleitungen Strom, obwohl die Platten sich nicht berühren. Der Strom wird schwächer und hört von selbst auf. Trennt man die Batterie ab, bleibt die Spannung stehen, und das Bauteil kann selbst Strom treiben. Die Frage dieses Kapitels lautet: *Wie kann Strom in einen Isolator hineinfließen, warum endet er von selbst, und wo steckt danach die Energie?*

Jede Platte ist eine __Elektrode__, der Isolator dazwischen heißt __Dielektrikum__. Die Größe, die das Bauteil kennzeichnet, ist die __Kapazität__: Sie sagt, wie viel Ladung je Volt auf den Platten sitzt. Die Grundform sind zwei ebene Platten, der __Plattenkondensator__.



**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Plattenpaar aus [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html):** quadratische Platten mit 10 cm Kantenlänge (Fläche $A=100$ cm$^2$), Abstand $d=3$ mm, Luft dazwischen, 9 V Spannung. Das Feld beträgt $E=3$ kV/m.

</li>

<li>

⁠**RC-Kreis:** Ein __RC-Kreis__ ist die Reihenschaltung aus Widerstand und Kondensator an einer Quelle. Hier lädt eine 9-V-Batterie ($U_0=9$ V) über $R=10\,\mathrm{k\Omega}$ einen Kondensator $C=100\,\mu\text{F}$. Damit ist $\tau=RC=1$ s. Der Innenwiderstand der Batterie, rund 2 $\Omega$, entfällt: Er ist 5000-mal kleiner als $R$.

</li>

<li>

⁠**Zwei Kondensatoren:** $C_1=100\,\mu\text{F}$ (derselbe wie im RC-Kreis) und $C_2=50\,\mu\text{F}$.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap3.py` nach.
:::
