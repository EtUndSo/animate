---
title: Stufe 1: Wie viele Größen sind frei?
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Maschenstrom- und Knotenpotentialverfahren
order: 1180300
summary: Teil 2 hat gezeigt, dass ein Netz 2z Unbekannte und 2z Gleichungen hat.
tags: 
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
[Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) hat gezeigt, dass ein Netz $2z$ Unbekannte und $2z$ Gleichungen hat. Diese Stufe zeigt, warum zwei viel kleinere Zahlen für die Rechnung genügen.
:::

**Die Idee.** Ein Baum ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) verbindet alle Knoten mit $k-1$ Zweigen, die restlichen $m=z-k+1$ Zweige sind Verbindungszweige. Kennt man die Spannungen der Baumzweige, kennt man alle Spannungen: Jeder Verbindungszweig schließt mit Baumzweigen genau eine Masche, und die Maschenregel liefert seine Spannung. Kennt man die Ströme der Verbindungszweige, kennt man alle Ströme: Am Ende des Baums hängt ein Baumzweig allein zwischen Verbindungszweigen, die Knotenregel liefert seinen Strom, und so geht es Zweig für Zweig weiter. Von $z$ Strömen darf man also nur $m$ vorgeben, von $z$ Spannungen nur $k-1$.

:::satz Satz 1.1 (Freie Größen eines Netzes)
<span class="anker" id="satz-1-1"></span>

Die $z$ Zweigströme eines zusammenhängenden Netzes müssen $k-1$ unabhängige Knotengleichungen erfüllen, die $z$ Zweigspannungen $z-k+1$ unabhängige Maschengleichungen. Deshalb sind

<span class="anker" id="gl-1-1"></span>
$$m=z-k+1\ \text{Ströme}\qquad\text{und}\qquad k-1\ \text{Spannungen} \tag{1.1}$$

frei wählbar. Alle anderen Ströme und Spannungen folgen aus Kirchhoff.
:::

⁠**So liest man das:** „Frei wählbar“ heißt: Man kann die Werte vorgeben, ohne eine Kirchhoff-Regel zu verletzen. $z$ zählt die Zweige wie in [Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), in englischen Büchern heißt die Zahl oft $b$ (für *branch*). **Gültigkeit:** Die Zählung hängt nur vom Graphen ab, nicht von den Bauteilen. Sie gilt auch für nichtlineare Bauteile.

:::abbildung et1/k8netz 1
Das Rechenmodell. Drei Knoten (rot), sechs Zweige. Der Zweig links enthält Batterie und $R_1$ in Reihe, weil zwischen ihnen nichts abzweigt. Knoten 0 ist die gesamte untere Leitung.
:::

**Beispiel.** Das Netz in Abb. [1](#abb-1) hat $k=3$ und $z=6$, also $m=4$:

| Ansatz | Unbekannte | Gleichungen |
|---|---|---|
| alle Ströme und Spannungen | 12 | 6 Bauteile, 2 Knoten, 4 Maschen |
| ohmsches Gesetz eingesetzt | 6 | 2 Knoten, 4 Maschen |
| Maschenströme | 4 | 4 Maschen; die Stromquelle legt einen Wert fest, es bleiben 3 |
| Knotenpotentiale | 2 | 2 Knoten |

⁠**Grenzfälle:** Eine Reihenschaltung als Ring hat $z=k$ und $m=1$: Ein einziger Strom gilt überall, das ist der Kern der Reihenschaltung. Eine Parallelschaltung hat $k=2$ und $k-1=1$: Eine einzige Spannung gilt überall, das ist der Kern der Parallelschaltung.

:::frage Geht es mit noch weniger Unbekannten?
Nicht ohne das Netz zu ändern, denn $m$ und $k-1$ zählen genau, was man vorgeben kann. Man kann aber vorher vereinfachen. Fasst man Reihen- und Parallelschaltungen zusammen ([Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)), schrumpfen $z$ und $k$. Die Zählung gilt dann für das kleinere Netz.
:::

:::aufgabe Aufgabe 1 ★ Zählen
<span class="anker" id="aufg-1"></span>

Gib $k$, $z$, $m$ und $k-1$ an.

<ol class="al">

<li>

Die Brücke aus [Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html): Quelle und fünf Widerstände zwischen vier Knoten.

</li>

<li>

Fünf Knoten, jeder mit jedem durch einen Widerstand verbunden.

</li>

<li>

Das Rechenmodell, nachdem Stromquelle und $R_5$ zu einem Zweig zusammengefasst sind.

</li>

<li>

Ein Ring aus sechs Bauteilen.

</li>

</ol>

:::loesung
(a) $k=4$, $z=6$, $m=3$, $k-1=3$. (b) $k=5$, $z=10$ (jedes der 10 Paare), $m=6$, $k-1=4$. (c) $k=3$, $z=5$, $m=3$, $k-1=2$. (d) $k=6$, $z=6$, $m=1$, $k-1=5$.
:::
:::
