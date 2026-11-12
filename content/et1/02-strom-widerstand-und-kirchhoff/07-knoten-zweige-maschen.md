---
title: Stufe 6: Knoten, Zweige, Maschen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom, Widerstand und Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Kapitel 2: Strom, Widerstand und Kirchhoff
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

::::formelsammlung
**Zahl der unabhängigen Maschen**

$$m=z-k+1$$

$k$ Knoten, $z$ Zweige, zusammenhängender Graph. Die $m$ Maschen bilden ein vollständiges System; jeder Baum legt eines fest, denn jeder Verbindungszweig schließt über die Baumzweige genau eine Masche.

**Baumzweige und Verbindungszweige**

$$k-1\ \text{Baumzweige},\qquad z-(k-1)\ \text{Verbindungszweige}$$

Ein Baum ist ein zusammenhängender Teilgraph, der alle Knoten enthält und keine Masche bildet.

**Unbekannte und Gleichungen**

$$z+(k-1)+(z-k+1)=2z$$

Je Zweig ein Strom und eine Spannung, also $2z$ Unbekannte. Dagegen stehen $z$ Bauteilgleichungen, $k-1$ Knotengleichungen und $z-k+1$ Maschengleichungen: Jedes Netz hat genau so viele Gleichungen wie Unbekannte.
::::

::::lernkarten
:::karte begriff Knoten
Was ist ein Knoten in einem Netzwerk, und wie bezeichnet man ihre Anzahl?
---
Ein Punkt, an dem sich der Strom verzweigt; ihre Anzahl ist $k$. Eine Verbindung zweier Bauteile ohne Abzweig ist nach dieser Bestimmung kein Knoten.
--- falsch
Jeder Punkt, an dem zwei Bauteile verbunden sind, auch ohne Abzweig; ihre Anzahl ist $k$. Jedes Bauteil hat also an seinen beiden Enden zwei eigene Knoten.
--- falsch
Ein Bauteil, durch das ein Strom fließt; ihre Anzahl ist $k$. Zwei Bauteile in Reihe bilden zusammen einen einzigen Knoten.
--- falsch
Ein geschlossener Weg im Netz, der jeden Punkt nur einmal berührt; ihre Anzahl ist $k$. Ein einzelner Kreis hat genau einen Knoten.
:::
:::karte begriff Zweig
Was ist ein Zweig in einem Netzwerk, und was fließt in ihm?
---
Eine Verbindung zweier Knoten über Zweipole; in ihm fließt ein Strom. $z$ ist ihre Anzahl.
--- falsch
Eine Verbindung zweier Knoten über Zweipole, in der sich der Strom auf mehrere Wege aufteilt. $z$ ist ihre Anzahl.
--- falsch
Ein einzelnes Bauteil; zwei Bauteile in Reihe bilden zwei Zweige mit verschiedenen Strömen. $z$ ist ihre Anzahl.
--- falsch
Ein Draht ohne Bauteil zwischen zwei Knoten; Verbindungen mit Bauteilen heißen Maschen. $z$ ist ihre Anzahl.
:::
:::karte begriff Graph
Was ist der Graph eines Netzwerks, und welche Eigenschaft wird für ihn vorausgesetzt?
---
Die Darstellung des Netzes aus Knoten und Zweigen, ohne die Bauteile. Er ist zusammenhängend: Von jedem Knoten führt ein Weg zu jedem anderen.
--- falsch
Die Kennlinie $I=f(U)$ eines Zweipols, gezeichnet als Kurve über der Spannung. Er ist zusammenhängend, wenn die Kurve nirgends Sprünge oder Lücken hat.
--- falsch
Die Darstellung des Netzes aus Knoten und Zweigen. Er darf in Teile zerfallen, zwischen denen kein Weg führt; seine Zweige haben keine Richtung.
--- falsch
Der Schaltplan mit allen Bauteilen und ihren Werten. Er ist zusammenhängend, wenn jedes Bauteil direkt an eine Quelle angeschlossen ist.
:::
:::karte begriff Masche
Welcher Weg in einem Netzwerk heißt Masche?
---
Ein geschlossener Weg, in dem jeder Knoten mit genau zwei benachbarten Zweigen verbunden ist. Kein Zweig und kein Knoten wird mehrfach durchlaufen.
--- falsch
Jeder Weg von einem Knoten zu einem anderen, auch wenn er nicht zum Start zurückkehrt. Zweige und Knoten dürfen dabei mehrfach durchlaufen werden.
--- falsch
Ein geschlossener Weg, der jeden Zweig des Netzes genau einmal durchläuft. Ein Netz hat deshalb genau eine Masche.
--- falsch
Ein geschlossener Weg, der nur über Widerstände führt; ein Weg über eine Quelle ist keine Masche. Knoten dürfen mehrfach vorkommen.
:::
:::karte begriff Baum und Verbindungszweige
Was ist ein Baum eines Netzgraphen, und welche Zweige heißen Verbindungszweige?
---
Ein zusammenhängender Teilgraph, der alle Knoten enthält und keine Masche bildet. Die restlichen Zweige heißen Verbindungszweige; jeder schließt über Baumzweige eine Masche.
--- falsch
Ein Teilgraph, der alle Zweige enthält und mindestens eine Masche bildet. Die Zweige, die in keiner Masche liegen, heißen Verbindungszweige.
--- falsch
Ein zusammenhängender Teilgraph, der alle Knoten enthält und keine Masche bildet. Verbindungszweige heißen seine eigenen Zweige, weil gerade sie die Knoten des Baums miteinander verbinden.
--- falsch
Der Teil eines Netzes, der nur die Quellen enthält; von ihm gehen die übrigen Zweige wie Äste ab. Diese heißen Verbindungszweige.
:::
:::karte begriff linear unabhängig und vollständig
Wann heißen Maschen linear unabhängig, und wann bilden sie ein vollständiges System?
---
Linear unabhängig, wenn man sie so ordnen kann, dass jede mindestens einen Zweig enthält, der in den vorherigen fehlt. Vollständig, wenn keine weitere Masche etwas Neues bringt: genau $m=z-k+1$ Maschen.
--- falsch
Linear unabhängig, wenn sie keinen einzigen Zweig gemeinsam haben. Vollständig ist das System, wenn jeder Zweig in genau einer der Maschen liegt; das sind genau $m=z-k$ Maschen.
--- falsch
Linear unabhängig, wenn jede einen Widerstand enthält, der in keiner anderen Masche vorkommt. Vollständig ist das System erst, wenn es wirklich alle Maschen des Netzes enthält.
--- falsch
Linear unabhängig, wenn man sie so ordnen kann, dass jede mindestens einen Knoten enthält, der in den vorherigen fehlt. Vollständig ist das System bei $m=k-1$.
:::
:::karte formel Zahl der unabhängigen Maschen
Wie viele unabhängige Maschen hat ein zusammenhängender Graph mit $k$ Knoten und $z$ Zweigen?
---
$m=z-k+1$. Jeder Baum legt ein solches System fest: Jeder seiner $z-(k-1)$ Verbindungszweige schließt genau eine Masche.
--- falsch
$m=z-k$. Jeder Baum legt ein solches System fest: Jeder seiner $z-k$ Verbindungszweige schließt genau eine Masche.
--- falsch
$m=z+k-1$. Jeder Zweig und jeder Knoten außer einem trägt eine eigene Masche bei, die die anderen nicht enthalten.
--- falsch
$m=k-1$. Jeder Baum legt ein solches System fest: Jeder seiner $k-1$ Baumzweige schließt genau eine Masche.
:::
:::karte herleitung Zahl der Maschen
Leite her, dass ein zusammenhängender Graph mit $k$ Knoten und $z$ Zweigen genau $m=z-k+1$ unabhängige Maschen hat.
---
Man baut einen Baum auf: Beginnend bei einem Knoten holt jeder neue Zweig genau einen neuen Knoten hinzu, weil sonst eine Masche entstünde.
---
Für $k$ Knoten braucht man deshalb $k-1$ Baumzweige, weil nur der Startknoten ohne eigenen Zweig dazukommt.
---
Es bleiben $z-(k-1)$ Verbindungszweige, weil alle übrigen Zweige nicht zum Baum gehören.
---
Jeder Verbindungszweig schließt genau eine Masche, weil es im Baum zwischen zwei Knoten genau einen Weg gibt.
---
Diese Maschen sind unabhängig, weil jede ihren eigenen Verbindungszweig enthält und keinen anderen.
:::
:::karte zusammenhang Gleichungen und Unbekannte
Warum hat jedes Netz genau so viele unabhängige Gleichungen wie Unbekannte?
---
Jeder Zweig trägt einen Strom und eine Spannung, also $2z$ Unbekannte. Dagegen stehen $z$ Bauteilgleichungen, $k-1$ Knotengleichungen und $z-k+1$ Maschengleichungen, zusammen $2z$.
--- falsch
Jeder Knoten trägt ein Potenzial, also $k$ Unbekannte. Dagegen stehen $k$ Knotengleichungen, eine für jeden Knoten; Maschengleichungen braucht man nicht.
--- falsch
Jeder Zweig trägt einen Strom, also $z$ Unbekannte. Dagegen stehen $k$ Knotengleichungen und $z-k$ Maschengleichungen, zusammen $z$.
--- falsch
Jeder Zweig trägt Strom und Spannung, also $2z$ Unbekannte. Dagegen stehen $k$ Knotengleichungen und $z$ Maschengleichungen; die überzähligen dienen nur zur Kontrolle der Lösung.
:::
:::karte zusammenhang Baum ohne Strom
Warum fließt in einem Netz, dessen Graph nur ein Baum ist, kein stationärer Strom?
---
Weil ein Baum keine Masche enthält: Mit $z=k-1$ ist $m=0$, und ohne geschlossenen Weg fließt kein stationärer Strom.
--- falsch
Weil ein Baum zu viele Knoten hat: An jedem Knoten teilt sich der Strom, bis in den äußeren Zweigen nichts mehr übrig bleibt.
--- falsch
Weil ein Baum keine Quelle enthalten darf: Quellen liegen nach der Bestimmung immer in Verbindungszweigen.
--- falsch
Weil in einem Baum alle Zweige parallel liegen: Die Ströme heben sich am gemeinsamen Knoten paarweise auf.
:::
:::karte zusammenhang Verbindung ohne Abzweig
Was ändert sich an der Zahl $m$ der unabhängigen Maschen, wenn man die Verbindung zweier Bauteile ohne Abzweig trotzdem als Knoten mitzählt?
---
Nichts: Der zusätzliche Knoten teilt einen Zweig in zwei, $k$ und $z$ wachsen beide um 1, und $m=z-k+1$ bleibt gleich.
--- falsch
$m$ wächst um 1: Der zusätzliche Knoten schließt mit seinen Nachbarknoten eine weitere Masche.
--- falsch
$m$ sinkt um 1: Nur $k$ wächst um 1, die Zahl der Zweige bleibt gleich, weil sich am Bauteil nichts ändert.
--- falsch
Die Formel gilt dann nicht mehr: $m=z-k+1$ setzt voraus, dass man nur echte Verzweigungen zählt, sonst wird $m$ falsch.
:::
::::
