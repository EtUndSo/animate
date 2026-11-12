---
title: Stufe 1: Wie viele Größen sind frei?
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1180300
summary: Kapitel 2 hat gezeigt, dass ein Netz 2z Unbekannte und 2z Gleichungen hat.
tags: 
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
[Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) hat gezeigt, dass ein Netz $2z$ Unbekannte und $2z$ Gleichungen hat. Diese Stufe zeigt, warum zwei viel kleinere Zahlen für die Rechnung genügen.
:::

**Die Idee.** Ein Baum ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) verbindet alle Knoten mit $k-1$ Zweigen, die restlichen $m=z-k+1$ Zweige sind Verbindungszweige. Kennt man die Spannungen der Baumzweige, kennt man alle Spannungen: Jeder Verbindungszweig schließt mit Baumzweigen genau eine Masche, und die Maschenregel liefert seine Spannung. Kennt man die Ströme der Verbindungszweige, kennt man alle Ströme: Am Ende des Baums hängt ein Baumzweig allein zwischen Verbindungszweigen, die Knotenregel liefert seinen Strom, und so geht es Zweig für Zweig weiter. Von $z$ Strömen darf man also nur $m$ vorgeben, von $z$ Spannungen nur $k-1$.

:::satz Satz 1.1 (Freie Größen eines Netzes)
<span class="anker" id="satz-1-1"></span>

Die $z$ Zweigströme eines zusammenhängenden Netzes müssen $k-1$ unabhängige Knotengleichungen erfüllen, die $z$ Zweigspannungen $z-k+1$ unabhängige Maschengleichungen. Deshalb sind

<span class="anker" id="gl-1-1"></span>
$$m=z-k+1\ \text{Ströme}\qquad\text{und}\qquad k-1\ \text{Spannungen} \tag{1.1}$$

frei wählbar. Alle anderen Ströme und Spannungen folgen aus Kirchhoff.
:::

⁠**So liest man das:** „Frei wählbar“ heißt: Man kann die Werte vorgeben, ohne eine Kirchhoff-Regel zu verletzen. $z$ zählt die Zweige wie in [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), in englischen Büchern heißt die Zahl oft $b$ (für *branch*). **Gültigkeit:** Die Zählung hängt nur vom Graphen ab, nicht von den Bauteilen. Sie gilt auch für nichtlineare Bauteile.

:::abbildung et1/k8netz 1
Das Rechenmodell. Drei Knoten (rot), sechs Zweige. Der Zweig links enthält Batterie und $R_1$ in Reihe, weil zwischen ihnen nichts abzweigt. Knoten 0 ist die gesamte untere Leitung.
:::

::::beispiel
Das Netz in Abb. [1](#abb-1) hat $k=3$ und $z=6$, also $m=4$:

| Ansatz | Unbekannte | Gleichungen |
|---|---|---|
| alle Ströme und Spannungen | 12 | 6 Bauteile, 2 Knoten, 4 Maschen |
| ohmsches Gesetz eingesetzt | 6 | 2 Knoten, 4 Maschen |
| Maschenströme | 4 | 4 Maschen; die Stromquelle legt einen Wert fest, es bleiben 3 |
| Knotenpotentiale | 2 | 2 Knoten |
::::

⁠**Grenzfälle:** Eine Reihenschaltung als Ring hat $z=k$ und $m=1$: Ein einziger Strom gilt überall, das ist der Kern der Reihenschaltung. Eine Parallelschaltung hat $k=2$ und $k-1=1$: Eine einzige Spannung gilt überall, das ist der Kern der Parallelschaltung.

:::frage Geht es mit noch weniger Unbekannten?
Nicht ohne das Netz zu ändern, denn $m$ und $k-1$ zählen genau, was man vorgeben kann. Man kann aber vorher vereinfachen. Fasst man Reihen- und Parallelschaltungen zusammen ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)), schrumpfen $z$ und $k$. Die Zählung gilt dann für das kleinere Netz.
:::

:::aufgabe Aufgabe 1 ★ Zählen
<span class="anker" id="aufg-1"></span>

Gib $k$, $z$, $m$ und $k-1$ an.

<ol class="al">

<li>

Die Brücke aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html): Quelle und fünf Widerstände zwischen vier Knoten.

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

::::formelsammlung
**Freie Größen eines Netzes**

$$m=z-k+1\ \text{Ströme}\qquad\text{und}\qquad k-1\ \text{Spannungen}$$

Zusammenhängendes Netz mit $z$ Zweigen und $k$ Knoten. Die $z$ Zweigströme müssen $k-1$ unabhängige Knotengleichungen erfüllen, die $z$ Zweigspannungen $z-k+1$ unabhängige Maschengleichungen. Ein Baum hat $k-1$ Zweige, die übrigen $m$ sind Verbindungszweige. „Frei wählbar“ heißt: vorgebbar, ohne eine Kirchhoff-Regel zu verletzen. Die Zählung hängt nur vom Graphen ab und gilt auch für nichtlineare Bauteile. Reihenschaltung als Ring: $m=1$; Parallelschaltung: $k-1=1$.
::::

::::lernkarten
:::karte formel Freie Größen eines Netzes
Wie viele Zweigströme und wie viele Zweigspannungen eines zusammenhängenden Netzes mit $z$ Zweigen und $k$ Knoten sind frei wählbar?
---
$m=z-k+1$ Ströme und $k-1$ Spannungen. Die Ströme müssen $k-1$ unabhängige Knotengleichungen erfüllen, die Spannungen $z-k+1$ unabhängige Maschengleichungen. Die Zählung hängt nur vom Graphen ab.
--- falsch
$m=z-k+1$ Spannungen und $k-1$ Ströme. Die Spannungen müssen $k-1$ unabhängige Knotengleichungen erfüllen, die Ströme $z-k+1$ unabhängige Maschengleichungen. Die Zählung hängt nur vom Graphen ab.
--- falsch
$m=z-k+1$ Ströme und $k-1$ Spannungen. Die Ströme müssen $k-1$ Knotengleichungen erfüllen, die Spannungen $z-k+1$ Maschengleichungen. Die Zählung gilt aber nur für lineare Bauteile wie Widerstände.
--- falsch
$z-k$ Ströme und $k$ Spannungen, zusammen also so viele wie Zweige. Jeder Zweig trägt genau eine freie Größe, die andere folgt aus seinem Bauteil. Die Zählung hängt nur vom Graphen ab.
:::
:::karte zusammenhang Verbindungszweige und Maschen
Wie viele Verbindungszweige bleiben übrig, wenn man in einem Netz einen Baum wählt, und welche Rolle spielt jeder von ihnen?
---
Die Zweige, die nicht zum Baum gehören. Der Baum verbindet alle $k$ Knoten mit $k-1$ Zweigen, also bleiben $m=z-k+1$ Verbindungszweige. Jeder schließt mit Baumzweigen genau eine Masche.
--- falsch
Die Zweige des Baums selbst, weil sie alle Knoten miteinander verbinden. Der Baum hat $k-1$ Zweige, also gibt es $k-1$ Verbindungszweige, die zusammen genau eine Masche bilden.
--- falsch
Die Zweige, die nicht zum Baum gehören. Der Baum verbindet alle $k$ Knoten mit $k$ Zweigen, also bleiben $z-k$ Verbindungszweige. Jeder schließt mit Baumzweigen mehrere Maschen.
--- falsch
Die Zweige, die zwei Maschen gemeinsam haben, weil sie benachbarte Maschen verbinden. Ihre Zahl hängt davon ab, wie man das Netz zeichnet, und zusammen bilden sie den Baum.
:::
:::karte zusammenhang Frei wählbare Größen
Was bedeutet es, dass von den Zweigströmen eines Netzes nur $m$ frei wählbar sind?
---
Man kann $m$ Ströme vorgeben, ohne eine Kirchhoff-Regel zu verletzen. Alle übrigen Ströme folgen dann aus Kirchhoff und lassen sich nicht mehr unabhängig festlegen.
--- falsch
Man kann $m$ Ströme beliebig wählen, und die Bauteile passen sich so an, dass trotzdem jede Kirchhoff-Regel gilt. Die übrigen Ströme bleiben dabei ebenfalls frei.
--- falsch
Genau $m$ Ströme sind null, die übrigen fließen. Welche Ströme verschwinden, hängt davon ab, welche Zweige man zum Baum zählt und welche nicht.
--- falsch
Man kann $m$ Ströme messen, ohne die Schaltung aufzutrennen. Die übrigen Ströme sind nur über die Spannungen an den Widerständen zugänglich.
:::
:::karte zusammenhang Spannungen der Baumzweige
Warum kennt man alle Zweigspannungen eines Netzes, sobald man die Spannungen der Baumzweige kennt?
---
Jeder Verbindungszweig schließt mit Baumzweigen genau eine Masche. Die Maschenregel dieser Masche liefert seine Spannung aus den bekannten Spannungen der Baumzweige.
--- falsch
Weil die Baumzweige alle Knoten verbinden und deshalb dieselbe Spannung tragen wie die Verbindungszweige daneben. Jeder Verbindungszweig übernimmt die Spannung eines Baumzweigs.
--- falsch
Jeder Verbindungszweig schließt mit Baumzweigen genau eine Masche. Die Knotenregel an seinen beiden Enden liefert seine Spannung aus den bekannten Spannungen der Baumzweige.
--- falsch
Weil an den Verbindungszweigen keine Spannung abfällt. Sie verbinden nur die Enden des Baums, und die ganze Spannung des Netzes liegt an den Baumzweigen.
:::
:::karte zusammenhang Ströme der Verbindungszweige
Warum kennt man alle Zweigströme eines Netzes, sobald man die Ströme der Verbindungszweige kennt?
---
An einem Ende des Baums hängt ein Baumzweig als einziger Baumzweig zwischen Verbindungszweigen. Die Knotenregel liefert dort seinen Strom, und so geht es Zweig für Zweig weiter, bis alle Baumzweige bekannt sind.
--- falsch
Weil jeder Baumzweig mit Verbindungszweigen genau eine Masche schließt. Die Maschenregel dieser Masche liefert seinen Strom aus den bekannten Strömen der Verbindungszweige.
--- falsch
Weil im Baum kein Strom fließt. Ein Baum enthält keine Masche, also gibt es dort keinen geschlossenen Weg, auf dem Ladung umlaufen könnte, und alle Baumzweige sind stromlos.
--- falsch
An einem Ende des Baums führt der Baumzweig die Summe aller Verbindungsströme des Netzes. Die übrigen Baumzweige teilen sich diesen Strom zu gleichen Teilen, weil sie im Baum gleichberechtigt nebeneinander liegen.
:::
:::karte zusammenhang Zählung unabhängig von den Bauteilen
Warum gilt die Zahl der frei wählbaren Ströme und Spannungen eines Netzes auch dann, wenn es nichtlineare Bauteile enthält?
---
Weil die Zählung nur vom Graphen abhängt, also davon, wie Zweige und Knoten verbunden sind. Die Knoten- und Maschengleichungen, die sie bestimmen, sagen nichts über die Bauteile in den Zweigen.
--- falsch
Weil nichtlineare Bauteile für die Zählung wie lineare Widerstände behandelt werden dürfen, solange die Ströme klein bleiben. Bei großen Strömen ändert sich die Zahl der freien Größen.
--- falsch
Sie gilt dort nicht: Ein nichtlineares Bauteil liefert je Zweig eine zusätzliche Gleichung. Deshalb sind bei solchen Bauteilen mehr Ströme frei als in einem linearen Netz.
--- falsch
Weil nichtlineare Bauteile keinen Strom führen, solange die Spannung klein ist. Ihre Zweige fallen dann aus der Zählung heraus, und die übrigen Zweige bestimmen $m$.
:::
:::karte zusammenhang Reihen- und Parallelschaltung als Grenzfälle
Was ergibt die Zählung der freien Größen für eine Reihenschaltung als Ring und für eine Parallelschaltung?
---
Ein Ring hat $z=k$, also $m=1$: Ein einziger Strom gilt überall, der Kern der Reihenschaltung. Eine Parallelschaltung hat $k=2$, also $k-1=1$: Eine einzige Spannung gilt überall.
--- falsch
Ein Ring hat $z=k$, also $m=1$: Eine einzige Spannung gilt überall, der Kern der Reihenschaltung. Eine Parallelschaltung hat $k=2$, also $k-1=1$: Ein einziger Strom gilt überall.
--- falsch
Ein Ring hat $z=k$, also $m=0$: Kein Strom ist frei, alle folgen aus den Quellen. Eine Parallelschaltung hat $k=2$, also $k-1=1$: Eine einzige Spannung gilt überall.
--- falsch
Ein Ring hat $z=k+1$, also $m=2$: Zwei Ströme sind frei, einer je Umlaufrichtung. Eine Parallelschaltung hat $k=1$ und deshalb gar keine freie Spannung.
:::
:::karte zusammenhang Weniger Unbekannte durch Vereinfachen
Kann man ein Netz mit weniger Unbekannten als $m$ Strömen oder $k-1$ Spannungen berechnen, und wie lässt sich diese Zahl verkleinern?
---
Nicht ohne das Netz zu ändern, denn $m$ und $k-1$ zählen genau, was man vorgeben kann. Fasst man aber vorher Reihen- und Parallelschaltungen zusammen, schrumpfen $z$ und $k$, und die Zählung gilt für das kleinere Netz.
--- falsch
Ja, man lässt die Zweige mit den kleinsten Strömen einfach weg, weil sie das Ergebnis kaum ändern. Dann schrumpft $z$, und die Zählung gilt für das kleinere Netz, ohne dass sich etwas Wesentliches ändert.
--- falsch
Nein, und auch Zusammenfassen hilft nicht, denn Reihen- und Parallelschaltungen ändern weder $z$ noch $k$. Die Zahl der Unbekannten ist eine feste Eigenschaft der verwendeten Bauteile.
--- falsch
Ja, man wählt einen anderen Baum mit mehr Zweigen. Dann bleiben weniger Verbindungszweige übrig, und $m$ sinkt, ohne dass man am Netz selbst etwas ändern muss.
:::
::::
