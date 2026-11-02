---
title: Überblick: Wahrscheinlichkeitsrechnung
kurz: Überblick
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3180100
summary: Was sich über den Zufall exakt sagen lässt
tags: Wahrscheinlichkeitsrechnung, Zufallsvariable
lang: de
---

## Worum es geht

Ein Bauteil fällt irgendwann aus, ein Messwert schwankt um den wahren Wert, ein Bit kommt verfälscht an. Im Einzelfall lässt sich das nicht vorhersagen. Trotzdem muss man planen: Wie viele Ersatzteile braucht eine Anlage? Wie oft muss man messen, bis man dem Mittelwert trauen kann? Wie viele Stücke einer Serie muss man prüfen, um ihren Ausschussanteil zu kennen?

Die __Wahrscheinlichkeitsrechnung__ ist die Mathematik für solche Fragen. Eine Zahl, die vom Zufall abhängt, heißt __Zufallsvariable__. Dieses Kapitel fragt: Was lässt sich über eine solche Zahl exakt aussagen, und was ändert sich, wenn man denselben Versuch sehr oft wiederholt?

**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Die Rechenmodelle für dieses Kapitel
<ul>

<li>

⁠**Zwei Vierer-Würfel**: zwei unterscheidbare Würfel mit den Augenzahlen $1,2,3,4$. Jedes der 16 Paare aus erster und zweiter Augenzahl ist gleich wahrscheinlich. $W_1$ und $W_2$ sind die Augenzahlen, $S=W_1+W_2$ ist die Summe.

</li>

<li>

⁠**Kiste**: 20 Widerstände, davon 4 defekt.

</li>

<li>

⁠**LED**: Die Wahrscheinlichkeit, dass sie länger als $x$ Jahre hält, ist $\mathrm{e}^{-x/2}$.

</li>

<li>

⁠**Netzteil**: Die Ausgangsspannung schwankt um den Sollwert $5\,\mathrm{V}$, typisch um $0{,}2\,\mathrm{V}$.

</li>

</ul>

Vorausgesetzt werden Reihen, uneigentliche Integrale, Mehrfachintegrale und das Gauß-Integral ([Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html) und 4), dazu die Mengenschreibweise. Das Zeichen $\subset$ erlaubt Gleichheit.
:::
