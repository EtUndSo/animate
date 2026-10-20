---
title: Topologische Grundbegriffe – Knoten, Zweige, Maschen
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Ströme und Spannungen in Netzen
order: 50400
summary: Die Sprache, in der man über die Struktur einer Schaltung spricht – Knoten, Zweige und Maschen – und wie man damit abzählt, wie viele Gleichungen ein Netzwerk überhaupt braucht.
tags: Netzwerk, Knoten, Zweig, Masche, Topologie, Baum, unabhängige Maschen
---

:::konzept
Um eine Schaltung zu berechnen, muss man sie erst einmal sauber beschreiben — nicht *welche* Bauteile drin
sind, sondern *wie* sie verbunden sind. Diese Struktur nennt man die **Topologie** des Netzwerks. Sie
interessiert sich nur für das „Gerüst": Wo treffen Leitungen zusammen, welche Pfade verbinden diese
Treffpunkte, welche geschlossenen Runden gibt es? Mit drei Begriffen — **Knoten**, **Zweig**, **Masche** — lässt
sich jede Schaltung wie eine Landkarte aus Kreuzungen und Straßen lesen.
:::

**Worum es geht:** Bevor man die Kirchhoffschen Gesetze anwendet, braucht man das Vokabular dafür. Dieser
Abschnitt führt die topologischen Grundbegriffe ein und beantwortet eine überraschend wichtige Frage: Wie viele
Gleichungen braucht man eigentlich, um ein Netzwerk eindeutig zu lösen?

## Die drei Grundbegriffe

Ein __Zweipol__ ist ein Bauteil mit zwei Anschlüssen (ein Widerstand, eine Quelle). Setzt man mehrere zu einer
Schaltung zusammen, entsteht ein __Netzwerk__, dessen Struktur man mit drei Begriffen beschreibt:

- __Knoten__: ein Verbindungspunkt, an dem mehrere Leitungen zusammenlaufen (im Sinne der Analyse zählt man die
  Punkte, an denen sich **drei oder mehr** Zweige treffen). An einem Knoten kann sich der Strom aufteilen.
- __Zweig__: der Leitungszug **zwischen zwei Knoten**, mit einem oder mehreren in Reihe liegenden Bauteilen —
  ohne weiteren Knoten dazwischen. Weil sich der Strom nur an Knoten aufteilt, ist der __Zweigstrom__ längs des
  ganzen Zweigs **konstant**.
- __Masche__: ein **geschlossener Umlauf** im Netzwerk, also ein Weg, der wieder zum Ausgangspunkt zurückführt,
  ohne eine Leitung doppelt zu benutzen.

Diese drei Begriffe reichen, um jede noch so verschachtelte Schaltung zu zerlegen — unabhängig davon, welche
Bauteile in den Zweigen sitzen.

:::grafik
Ein kleines Netzwerk mit drei bis vier Knoten (dick markierte Punkte), dazwischen Zweige mit Widerständen und
einer Quelle. Ein geschlossener Umlauf ist als Masche farbig hervorgehoben, ein Zweig und ein Knoten sind
beschriftet.
:::

## Ein Netzwerk abzählen

Für die Berechnung ist entscheidend, wie viele **unabhängige** Gleichungen man aufstellen kann. Dazu zählt man
zwei Größen:

- __$k$__: die Anzahl der __Knoten__,
- __$z$__: die Anzahl der __Zweige__ (das ist zugleich die Zahl der unbekannten Zweigströme).

Die __Knotenregel__ liefert pro Knoten eine Gleichung — aber nicht alle sind voneinander unabhängig. Die letzte
ergibt sich immer aus den übrigen (was in alle Knoten hineinfließt, muss irgendwo wieder heraus). Es bleiben
also genau

$$n_\text{Knoten} = k - 1$$

unabhängige Knotengleichungen. Die restlichen unbekannten Zweigströme bestimmt man über __Maschen__ — und zwar
über genau so viele unabhängige Maschengleichungen, wie noch Gleichungen fehlen:

$$m = z - (k - 1).$$

- __$m$__: die Anzahl __unabhängiger Maschen__ (und damit Maschengleichungen).
- __$z$__: die Anzahl der __Zweige__.
- __$k-1$__: die bereits durch die Knotenregel abgedeckten Gleichungen.

Zusammen ergeben $k-1$ Knoten- und $m = z-(k-1)$ Maschengleichungen genau $z$ Gleichungen für die $z$
unbekannten Zweigströme — das Netzwerk ist damit vollständig und eindeutig bestimmt.

## Baum und Verbindungszweige

Woher weiß man, *welche* Maschen unabhängig sind? Dafür gibt es ein anschauliches Werkzeug: den __vollständigen
Baum__. Man wählt aus allen Zweigen so viele aus, dass alle Knoten verbunden sind, aber **keine** geschlossene
Masche entsteht. Ein solcher Baum enthält immer genau $k-1$ Zweige, die __Baumzweige__.

Die übrigen $m = z-(k-1)$ Zweige heißen __Verbindungszweige__ (oder Maschenzweige). Fügt man einen einzelnen
Verbindungszweig zum Baum hinzu, entsteht **genau eine** neue geschlossene Masche. Jeder Verbindungszweig liefert
also eine unabhängige Masche — das ist der Grund für die Formel $m = z-(k-1)$. Man hat damit ein sicheres
Rezept, um gerade die richtige Anzahl unabhängiger Maschen zu finden, ohne welche doppelt zu zählen.

:::grafik
Dasselbe Netzwerk zweimal: links der vollständige Baum mit durchgezogenen Baumzweigen (alle Knoten verbunden,
keine Masche), rechts zusätzlich die gestrichelten Verbindungszweige — bei jedem ist die eine Masche farbig
markiert, die er schließt.
:::

:::kern
Die __Topologie__ beschreibt, *wie* eine Schaltung verbunden ist. Ein __Knoten__ ist ein Verbindungspunkt
(≥3 Zweige), ein __Zweig__ der Leitungszug zwischen zwei Knoten mit konstantem __Zweigstrom__, eine __Masche__
ein geschlossener Umlauf. Bei $k$ Knoten und $z$ Zweigen gibt es $k-1$ unabhängige Knotengleichungen und
$m = z-(k-1)$ unabhängige Maschengleichungen — zusammen genau $z$ Gleichungen für die $z$ Zweigströme. Der
__vollständige Baum__ ($k-1$ Baumzweige, keine Masche) macht das sichtbar: Jeder __Verbindungszweig__ schließt
genau eine unabhängige Masche.
:::

Mit diesem Vokabular lassen sich die beiden zentralen Gesetze der Netzwerkanalyse sauber formulieren: die
__Kirchhoffsche Knoten- und Maschenregel__.

:::quiz
F: Was beschreibt die Topologie eines Netzwerks, und was lässt sie bewusst weg?
A: Sie beschreibt nur, *wie* die Bauteile verbunden sind — das Gerüst aus Treffpunkten und Verbindungen. *Welche* Bauteile in den Zweigen sitzen, spielt für die topologische Betrachtung keine Rolle.
F: Warum ist der Strom längs eines ganzen Zweigs konstant?
A: Ein Zweig verläuft zwischen zwei Knoten ohne weiteren Knoten dazwischen, und nur an Knoten kann sich der Strom aufteilen. Ohne Verzweigungspunkt fließt also überall im Zweig derselbe Zweigstrom.
F: Was ist eine Masche genau?
A: Ein geschlossener Umlauf durch das Netzwerk, der zum Ausgangspunkt zurückführt, ohne eine Leitung doppelt zu benutzen. Maschen sind die Grundlage für die zweite Kirchhoffsche Regel.
F: Warum liefern nicht alle $k$ Knoten unabhängige Gleichungen, sondern nur $k-1$?
A: Die Knotenregeln hängen zusammen: Was in alle Knoten hineinfließt, muss insgesamt wieder heraus. Die letzte Knotengleichung ergibt sich daher automatisch aus den übrigen und ist nicht unabhängig.
F: Wie viele unabhängige Maschengleichungen braucht man, und warum gerade so viele?
A: $m=z-(k-1)$ — genau so viele, wie nach den $k-1$ Knotengleichungen noch zu den $z$ unbekannten Zweigströmen fehlen. Zusammen ergeben sie exakt $z$ Gleichungen für $z$ Unbekannte.
F: Warum ergeben $k-1$ Knoten- plus $m$ Maschengleichungen zusammen genau $z$?
A: Es ist $(k-1)+(z-(k-1))=z$. Die Aufteilung ist so gewählt, dass genau ein eindeutig lösbares Gleichungssystem für die $z$ Zweigströme entsteht.
F: Was ist ein vollständiger Baum, und welche Eigenschaft hat er?
A: Eine Auswahl von Zweigen, die alle Knoten verbindet, aber keine geschlossene Masche bildet. Ein solcher Baum enthält immer genau $k-1$ Baumzweige.
F: Warum liefert jeder Verbindungszweig genau eine unabhängige Masche?
A: Fügt man einen Verbindungszweig zum masch­enfreien Baum hinzu, schließt er genau einen Umlauf. Da es $z-(k-1)$ Verbindungszweige gibt, erhält man ebenso viele unabhängige Maschen — genau die Formel $m=z-(k-1)$.
F: Warum ist der Baum ein sicheres Rezept gegen doppelt gezählte Maschen?
A: Jede der so gefundenen Maschen enthält genau einen Verbindungszweig, den keine andere enthält. Dadurch ist garantiert, dass keine Masche sich aus den anderen zusammensetzen lässt — sie sind alle unabhängig.
F: Wozu braucht man das Abzählen von Knoten und Zweigen überhaupt?
A: Es sagt vorab, wie viele unabhängige Gleichungen ein Netzwerk zur eindeutigen Lösung braucht. So stellt man genau die richtige Zahl auf — weder zu wenige (unterbestimmt) noch redundante.
:::
