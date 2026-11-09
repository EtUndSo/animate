---
title: Stufe 6: Knoten, Zweige, Maschen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom, Widerstand und Kirchhoff
order: 1120700
summary: Ein Netz hat viele Unbekannte.
tags: Knoten, Zweig, Graph, Masche, Baum, Verbindungszweige, linear unabhängig, vollständiges
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Ein Netz hat viele Unbekannte. Bevor man rechnet, zählt man: Wie viele Ströme und Spannungen gibt es, und wie viele unabhängige Gleichungen stehen dafür bereit?
:::

**Die Idee.** Für die Zahl der Gleichungen ist gleichgültig, welches Bauteil in einem Zweig sitzt. Ersetzt man jeden Zweig durch eine Linie, bleibt das Gerippe des Netzes übrig (Abb. [7](#abb-7)). Dieses Gerippe bestimmt die Rechnung.

:::abbildung et1/k2netz 7
Links: das Netz des Rechenmodells mit vier Knoten und sechs Zweigen. Der Zweig der Quelle heißt 0, die übrigen tragen den Buchstaben ihres Widerstands. Rechts: sein Graph. Der Baum aus den drei schwarzen Zweigen lässt drei Verbindungszweige übrig. Jeder schließt über Baumzweige genau eine Masche (rot der Verbindungszweig).
:::

:::definition Definition 6.1 (Topologische Grundbegriffe)
<span class="anker" id="satz-6-1"></span>

Die Struktur eines Netzes beschreiben fünf Begriffe:

<ul>

<li>

Ein __Knoten__ ist ein Punkt, an dem sich der Strom verzweigt. $k$ ist ihre Anzahl.

</li>

<li>

Ein __Zweig__ verbindet zwei Knoten über Zweipole, in ihm fließt ein Strom. $z$ ist ihre Anzahl.

</li>

<li>

Der __Graph__ ist die Darstellung aus Knoten und Zweigen. Er ist zusammenhängend: Von jedem Knoten führt ein Weg zu jedem anderen. Jeder Zweig bekommt die Richtung seines Strompfeils.

</li>

<li>

Eine __Masche__ ist ein geschlossener Weg, in dem jeder Knoten mit genau zwei benachbarten Zweigen verbunden ist. Kein Zweig und kein Knoten wird mehrfach durchlaufen.

</li>

<li>

Ein __Baum__ ist ein zusammenhängender Teilgraph, der alle Knoten enthält und keine Masche bildet. Die restlichen Zweige heißen __Verbindungszweige__.

</li>

</ul>
:::

:::satz Satz 6.2 (Zahl der unabhängigen Maschen)
<span class="anker" id="satz-6-2"></span>

Maschen heißen __linear unabhängig__, wenn man sie so ordnen kann, dass jede mindestens einen Zweig enthält, der in den vorherigen fehlt. Ein Graph mit $k$ Knoten und $z$ Zweigen hat genau

<span class="anker" id="gl-6-1"></span>
$$m=z-k+1 \tag{6.1}$$

unabhängige Maschen. Sie bilden ein __vollständiges__ System: Keine weitere Masche bringt etwas Neues. Jeder Baum legt ein solches System fest: Jeder Verbindungszweig schließt über die Baumzweige genau eine Masche.
:::

⁠**So liest man das:** $m$ zählt die Maschen, deren Gleichungen neue Information tragen. Alle anderen Maschen setzen sich aus ihnen zusammen. **Gültigkeit:** Der Graph muss zusammenhängend sein.

:::herleitung Warum $z-k+1$
Man baut einen Baum auf: Beginnend bei einem Knoten holt jeder neue Zweig genau einen neuen Knoten hinzu, sonst entstünde eine Masche. Für $k$ Knoten braucht man $k-1$ Baumzweige. Es bleiben $z-(k-1)$ Verbindungszweige. Im Baum gibt es zwischen zwei Knoten genau einen Weg, also schließt jeder Verbindungszweig genau eine Masche. Sie enthält keinen anderen Verbindungszweig, deshalb sind diese Maschen unabhängig.
:::

**Unbekannte und Gleichungen.** Jeder Zweig trägt einen Strom und eine Spannung, das sind $2z$ Unbekannte. Dagegen stehen $z$ Bauteilgleichungen (eine je Zweig), $k-1$ Knotengleichungen (Stufe [7](die-knotenregel-ist-ladungserhaltung.html#stufe-7)) und $z-k+1$ Maschengleichungen (Stufe [8](die-maschenregel-ist-energieerhaltung.html#stufe-8)). Die Summe ist genau $2z$. **Kurz gesagt:** Jedes Netz hat genau so viele Gleichungen wie Unbekannte.

::::beispiel
Das Netz hat $k=4$, $z=6$, also $m=3$. Sein Graph hat 16 Bäume mit je drei Zweigen. Abb. [7](#abb-7) wählt den Stern um $K_4$ mit den Zweigen 0, b und d. Die Verbindungszweige a, c und e schließen die Maschen $M_1$, $M_2$ und $M_3$. Das System umfasst 12 Unbekannte und 12 Gleichungen.
::::

⁠**Grenzfälle:** Ein einzelner Kreis hat $z=k$, also $m=1$. Ein Baum allein hat $z=k-1$, also $m=0$: Ohne geschlossenen Weg fließt kein stationärer Strom.

:::frage Ist die Verbindung zweier Bauteile ohne Abzweig ein Knoten?
Nach der Definition nicht, denn dort verzweigt sich nichts. Zählt man sie trotzdem mit, ändert sich $m$ nicht: Ein zusätzlicher Knoten teilt einen Zweig in zwei, $k$ und $z$ wachsen beide um 1.
:::

:::aufgabe Aufgabe 6 ★★ Zählen
<span class="anker" id="aufg-6"></span>

Gib jeweils $k$, $z$, $m$ und die Zahl der Baumzweige an.

<ol class="al">

<li>

Eine Quelle speist drei parallele Widerstände.

</li>

<li>

Aus dem Netz in Abb. [7](#abb-7) wird $R_\mathrm e$ entfernt.

</li>

<li>

Ein Netz hat 6 Knoten und 10 Zweige. Wie viele Gleichungen welcher Art braucht man?

</li>

</ol>

:::loesung
(a) Die beiden Schienen sind die Knoten: $k=2$, $z=4$, $m=3$, ein Baumzweig. (b) $k=2$, $z=3$, $m=2$, ein Baumzweig. Ohne $R_\mathrm e$ verzweigt sich an $K_2$ und $K_3$ nichts mehr: $R_\mathrm a$ und $R_\mathrm b$ bilden einen Zweig, $R_\mathrm c$ und $R_\mathrm d$ den anderen. (c) $m=10-6+1=5$. Man braucht 5 Knotengleichungen, 5 Maschengleichungen und 10 Bauteilgleichungen für 20 Unbekannte. Ein Baum hat 5 Zweige.
:::
:::
