---
title: Überblick: Leistung, Anpassung und Wirkungsgrad
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Leistung, Anpassung und Wirkungsgrad
order: 1170100
summary: Warum am Leistungsmaximum die Hälfte der Energie in der Quelle bleibt
tags: Innenwiderstand, Last, Leistung
lang: de
---

## Worum es geht

Eine 9-V-Batterie hat 2 $\Omega$ __Innenwiderstand__, den Widerstand, den der Strom in der Quelle selbst überwinden muss. Sie speist eine __Last__, das angeschlossene Gerät. Wie groß muss die Last sein, damit möglichst viel __Leistung__, also Energie je Zeit, bei ihr ankommt? Die Antwort lautet 2 $\Omega$, und sie hat einen Preis: Dann bleibt die Hälfte der Energie als Wärme in der Batterie. Die Frage dieses Kapitels lautet: *Woher kommt die Leistung, wohin geht sie, und warum liegt das Maximum ausgerechnet bei 50 % Ausnutzung?*



**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Batterie:** der 9-V-Block aus [Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) mit der Quellenspannung $U_\mathrm{q}=9$ V (die Spannung, die die Chemie liefert) und dem Innenwiderstand $R_\mathrm{i}=2\,\Omega$. [Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) nennt ihn bei der einzelnen Quelle $R_\mathrm{q}$. Der Kurzschlussstrom ist $I_\mathrm{KS}=4{,}5$ A.

</li>

<li>

⁠**Last:** ein Widerstand $R_\mathrm{L}$ mit 16, 8, 2 oder 0,5 $\Omega$.

</li>

<li>

⁠**Weitere:** $R=5\,\Omega$ an einer Sinusspannung mit 10 V Spitzenwert (Stufe [3](mittlere-leistung-bei-sinusspannung.html#stufe-3)), eine Leitung mit $R_\mathrm{Kabel}=1\,\Omega$ vor 40 kW Last (Stufe [4](leitungsverluste.html#stufe-4)).

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap7.py` nach.
:::
