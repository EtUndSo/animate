---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
order: 1211200
summary: Was man über die Zahlen voraussetzen muss und warum die Wurzel aus 2 kein Bruch ist
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Alle Rechenregeln folgen durch logisches Schließen aus wenigen Axiomen: den Körperaxiomen für Plus und Mal und den Anordnungsaxiomen für „positiv“.

</li>

<li>

Die Brüche erfüllen diese Axiome auch, aber sie haben Lücken: Kein Bruch $r$ löst $r^2=2$.

</li>

<li>

Das Vollständigkeitsaxiom schließt die Lücken: Jede nicht leere Menge, die eine untere Schranke hat (eine Zahl, die kleiner oder gleich allen Elementen ist), hat auch eine größte. Mit ihm sind die reellen Zahlen eindeutig festgelegt, und $\sqrt2$ existiert.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Mengen und Aussagen gehorchen denselben Regeln, bewiesen per Tafel. $\mathcal A\Rightarrow\mathcal B$ ist nur bei $w\Rightarrow f$ falsch.

</li>

<li>

Verneinen tauscht $\forall$ und $\exists$. Verschiedene Quantoren darf man nicht vertauschen.

</li>

<li>

Körper: 10 Axiome, Bindeglied $x(y+z)=xy+xz$. Anordnung: $z<0$ dreht die Ungleichung, $x\ne0\Rightarrow x^2>0$.

</li>

<li>

Induktion: Anfang plus Schritt.

</li>

<li>

$\sqrt2\notin\mathbb{Q}$. Vollständigkeit: Jede nach unten beschränkte, nicht leere Menge hat ein Infimum im Körper. Das trennt $\mathbb{R}$ von $\mathbb{Q}$. Intervallschachtelung liefert $\sqrt y$.

</li>

<li>

$|x+y|\le|x|+|y|$, $(1+x)^n>1+nx$, $\sqrt{xy}\le\frac{x+y}2$, $\sum|x_iy_i|\le\|\vec x\|\|\vec y\|$, $\|\vec x+\vec y\|\le\|\vec x\|+\|\vec y\|$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Nichts wird geglaubt: Jede Regel steht am Ende einer Kette von Schlüssen, die bei einem Axiom beginnt.

| Ergebnis | Woher es kommt |
|---|---|
| De-Morgan-Regeln, Kontraposition | endlich viele Fälle: Wahrheitstafel (Stufe [1](mengen-und-aussagen.html#stufe-1)) |
| Verneinung von „für alle“ | „für alle“ ist ein langes „und“, De Morgan (Stufe [2](quantoren-und-indirekter-beweis.html#stufe-2)) |
| $(-1)\cdot(-1)=1$, Bruchrechnen | Körperaxiome, vor allem das Distributivgesetz (Stufe [3](korperaxiome.html#stufe-3)) |
| Ungleichung dreht sich bei $z<0$ | Anordnungsaxiome (Stufe [4](anordnungsaxiome.html#stufe-4)) |
| Summenformeln, Potenzgesetze | Aufbau der natürlichen Zahlen: Induktion (Stufe [5](vollstandige-induktion-summe-und-produkt.html#stufe-5)) |
| Archimedes, $\sqrt2$ existiert | Vollständigkeit (Stufe [6](das-vollstandigkeitsaxiom.html#stufe-6) und [7](intervallschachtelung-und-wurzeln.html#stufe-7)) |
| Dreiecksungleichung | Lage auf der Zahlengeraden (Stufe [8](abstand-und-betrag.html#stufe-8)) |
| Young, Cauchy-Schwarz | Quadrate sind nicht negativ (Stufe [9](elementare-ungleichungen.html#stufe-9)) |
