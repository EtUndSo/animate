---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Komplexe Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Kapitel 2: Komplexe Zahlen
order: 1220800
summary: Wie eine zweite Achse $x^2=-1$ lösbar macht und was dabei verloren geht
tags: komplexe Zahl, imaginäre Einheit, komplexe Ebene, Körper, konjugiert komplexe Zahl, Betrag, Dreiecksungleichung
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Eine __komplexe Zahl__ ist ein Paar reeller Zahlen, geschrieben $z=x+\mathrm{i}y$. Die __imaginäre Einheit__ $\mathrm{i}$ ist das Paar $(0,1)$ und erfüllt $\mathrm{i}^2=-1$. Alle Paare zusammen bilden die __komplexe Ebene__, in der $\mathbb{R}$ die waagerechte Achse ist.

</li>

<li>

Man rechnet wie in $\mathbb{R}$ und ersetzt $\mathrm{i}^2$ durch $-1$. Deshalb ist $\mathbb{C}$ ein __Körper__ (eine Menge, in der die vier Grundrechenarten mit den gewohnten Gesetzen gelten). Verloren geht die Anordnung: Zwischen komplexen Zahlen gibt es kein „größer“.

</li>

<li>

Die __konjugiert komplexe Zahl__ $\overline{z}=x-\mathrm{i}y$ ist das Spiegelbild von $z$ an der reellen Achse, und $z\overline{z}=x^2+y^2$ ist reell. Daraus folgen die Division, der __Betrag__ $|z|=\sqrt{x^2+y^2}$ (Abstand zum Nullpunkt) und die __Dreiecksungleichung__ $|z+w|\le|z|+|w|$ (ein Umweg ist nie kürzer).

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Eine komplexe Zahl ist ein Paar: $z=x+\mathrm{i}y$ mit $\mathrm{i}^2=-1$. Man rechnet wie in $\mathbb{R}$.

</li>

<li>

Addition ist das Parallelogramm, Multiplikation mit $\mathrm{i}$ dreht um $90^\circ$.

</li>

<li>

Konjugieren spiegelt: $\overline{z}=x-\mathrm{i}y$, und $z\overline{z}=x^2+y^2=|z|^2$.

</li>

<li>

Division: mit der Konjugierten des Nenners erweitern, $w/z=w\overline{z}/|z|^2$.

</li>

<li>

$\mathbb{C}$ ist ein Körper, aber nicht angeordnet. Ungleichungen stehen nur zwischen reellen Größen.

</li>

<li>

$|z|=\sqrt{x^2+y^2}$, $d(z,w)=|z-w|$, $|zw|=|z||w|$, $|z+w|\le|z|+|w|$.

</li>

<li>

$z^2+pz+q=0$ hat in $\mathbb{C}$ immer Lösungen: $z=-p/2\pm w$ mit $w^2=p^2/4-q$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Alles in diesem Kapitel folgt aus einer Regel: Rechne mit $\mathrm{i}$ wie mit einem Buchstaben und ersetze $\mathrm{i}^2$ durch $-1$.

| Ergebnis | Woher es kommt |
|---|---|
| Produktformel | Ausmultiplizieren, das Minus ist $\mathrm{i}^2$ (Stufe [1](paare-statt-einzelner-zahlen.html#stufe-1)) |
| Addition als Parallelogramm | Real- und Imaginärteil addieren sich getrennt (Stufe [2](die-komplexe-ebene.html#stufe-2)) |
| Mal $\mathrm{i}$ dreht um $90^\circ$ | $\mathrm{i}(x+\mathrm{i}y)=-y+\mathrm{i}x$, zweimal gedreht ist $-1$ (Stufe [2](die-komplexe-ebene.html#stufe-2)) |
| $z\overline{z}=x^2+y^2$ | Dritte binomische Formel mit $-\mathrm{i}^2=+1$ (Stufe [3](spiegeln-an-der-reellen-achse.html#stufe-3)) |
| Division | Erweitern mit $\overline{z}$ macht den Nenner reell (Stufe [4](dividieren-und-was-verloren-geht.html#stufe-4)) |
| Keine Anordnung | $\mathrm{i}^2=-1$ ist ein negatives Quadrat (Stufe [4](dividieren-und-was-verloren-geht.html#stufe-4)) |
| $\vert zw\vert =\vert z\vert \,\vert w\vert $, Dreiecksungleichung | $\vert z\vert ^2=z\overline{z}$ (Stufe [5](betrag-und-abstand.html#stufe-5)) |
| Quadratische Gleichungen | Ergänzen gilt in jedem Körper, jede Zahl hat eine Wurzel (Stufe [6](quadratische-gleichungen.html#stufe-6)) |
