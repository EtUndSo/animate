---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Unendliche Reihen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen
knoten: Kapitel 6: Unendliche Reihen
order: 1261100
summary: Wann hat eine Summe ohne Ende einen Wert?
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Eine Reihe ist die Folge ihrer Teilsummen $S_N=a_1+\dots+a_N$, ihr Wert ist $\lim_{N\to\infty}S_N$. Alles Wissen über Folgen gilt also weiter.

</li>

<li>

Die Summanden müssen gegen 0 gehen, aber das reicht nicht. Es zählt, wie schnell sie es tun, und gemessen wird das fast immer an der geometrischen Reihe.

</li>

<li>

Nur absolut konvergente Reihen verhalten sich wie endliche Summen: Bei ihnen ändert keine Umordnung den Wert.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Reihe: Folge der Teilsummen $S_N=\sum_{n=1}^Na_n$, Wert $S=\lim S_N$. Geometrisch: $\sum_{n=0}^\infty q^n=\frac1{1-q}$ für $|q|<1$.

</li>

<li>

Konvergent $\Rightarrow$ $a_n\to0$, nicht umgekehrt: $\sum\frac1n$ divergiert (Gruppen $\ge\frac12$). Cauchy: Jedes Stück hinter $N_0$ ist klein.

</li>

<li>

Leibniz: $a_n>0$ fällt monoton gegen 0 $\Rightarrow$ $\sum(-1)^{n+1}a_n$ konvergiert, Fehler $\le a_{N+1}$.

</li>

<li>

Rechenregeln gelten gliedweise. Klammern setzen nur in konvergenten Reihen, Teilsummen sind dann eine Teilfolge.

</li>

<li>

Absolut konvergent $\Rightarrow$ konvergent. Vergleich: $|a_n|\le b_n$. $\sum\frac1{n^s}$ konvergiert genau für $s>1$.

</li>

<li>

Quotient, Wurzel: $\alpha<1$ absolut konvergent, $\alpha>1$ divergent, $\alpha=1$ keine Aussage. Beide vergleichen mit der geometrischen Reihe.

</li>

<li>

Verdichtung: Für positive fallende $a_n$ entscheidet $\sum2^ka_{(2^k)}$. $\sum\frac1{n\log n}$ divergiert.

</li>

<li>

Umordnen erhält den Wert bei absoluter Konvergenz, bei bedingter Konvergenz im Allgemeinen nicht: Zurückgehaltene Glieder können eine feste Summe tragen.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Eine Reihe ist eine Treppe: Jeder Summand ist eine Stufe, jede Teilsumme eine Höhe. Die Frage lautet immer: Hat die Treppe eine Decke, und strebt sie auf eine feste Höhe zu? Jedes Ergebnis antwortet mit einem Satz über Folgen oder mit einem Vergleich gegen die geometrische Reihe.

| Ergebnis | Woher es kommt |
|---|---|
| Wert einer Reihe | Die Teilsummen sind eine Folge, ihr Grenzwert ist der Wert (Stufe [1](eine-reihe-ist-eine-folge.html#stufe-1)) |
| Geometrische Reihe | Geometrische Summe aus Kapitel 4 und $q^N\to0$ (Stufe [1](eine-reihe-ist-eine-folge.html#stufe-1)) |
| Cauchy-Kriterium, $a_n\to0$ | Cauchy-Folgen für $S_N$; ein Summand ist die Differenz zweier Teilsummen (Stufe [2](nullfolge-notig-aber-nicht-genug.html#stufe-2)) |
| Divergenz der harmonischen Reihe | Immer größere Gruppen ergeben je mindestens $\frac12$, die Teilsummen sind unbeschränkt (Stufe [2](nullfolge-notig-aber-nicht-genug.html#stufe-2)) |
| Leibniz-Kriterium | Gerade und ungerade Teilsummen sind monotone Folgen mit demselben Ziel (Stufe [3](wechselnde-vorzeichen.html#stufe-3)) |
| Rechenregeln, Klammern | Rechenregeln für Folgen; Klammern wählt eine Teilfolge der Teilsummen (Stufe [4](rechenregeln-und-klammern.html#stufe-4)) |
| Absolute Konvergenz, Vergleich | Die Teilsummen der Beträge sind monoton, es zählt nur die Decke (Stufe [5](absolute-konvergenz-und-vergleich.html#stufe-5)) |
| Quotient, Wurzel | Ab einem Index liegt die Reihe unter einer geometrischen Reihe (Stufe [6](quotient-und-wurzel.html#stufe-6)) |
| Verdichtung | Ein Block aus $2^k$ Summanden wird durch $2^k$ mal einen Summanden ersetzt (Stufe [7](verdichten-und-der-entscheidungsweg.html#stufe-7)) |
| Umordnen | Die Summe der zurückgehaltenen Summanden muss verschwinden; das sichert nur die absolute Konvergenz (Stufe [8](umordnen.html#stufe-8)) |
