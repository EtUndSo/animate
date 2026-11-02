---
title: Überblick: Komplexe Zahlen
kurz: Überblick
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Komplexe Zahlen
order: 1220100
summary: Wie eine zweite Achse $x^2=-1$ lösbar macht und was dabei verloren geht
tags: Realteil, Imaginärteil
lang: de
---

## Worum es geht

Die Gleichung $x^2=-1$ hat in $\mathbb{R}$ keine Lösung, denn das Quadrat einer reellen Zahl ist nie negativ. Trotzdem führen quadratische Gleichungen immer wieder auf Wurzeln aus negativen Zahlen, und die Wechselstromtechnik rechnet täglich damit. Die Frage lautet: *Lässt sich $\mathbb{R}$ so erweitern, dass $x^2=-1$ lösbar wird und die Rechengesetze erhalten bleiben, und was geht dabei verloren?*



**So arbeitest du mit diesem Kapitel.** Jede Stufe ist ein eigener kurzer Artikel mit der Idee, typischen Fragen zum Aufklappen und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf. Schließe eine Stufe ab, bevor du zur nächsten gehst.

:::merke Das Rechenmodell für dieses Kapitel
<ul>

<li>

⁠**Zwei feste Zahlen:** $z_1=3+\mathrm{i}$ und $z_2=1+2\mathrm{i}$. Bei $z_1$ ist 3 der __Realteil__ (der Anteil ohne $\mathrm{i}$) und 1 der __Imaginärteil__ (die reelle Zahl vor $\mathrm{i}$). Allgemeine Aussagen schreibt das Kapitel mit $z$ und $w$.

</li>

<li>

⁠**Was aus ihnen wird:** $z_1+z_2=4+3\mathrm{i}$, $z_1z_2=1+7\mathrm{i}$, $z_1/z_2=1-\mathrm{i}$, $|z_1+z_2|=5$.

</li>

<li>

⁠**Zwei Gleichungen:** $z^2-6z+10=0$ mit reellen und $z^2-(4+3\mathrm{i})z+1+7\mathrm{i}=0$ mit komplexen Vorfaktoren. Die zweite hat genau $z_1$ und $z_2$ als Lösungen.

</li>

</ul>

Alle Zahlen rechnet `rechnung_kap2.py` nach.
:::
