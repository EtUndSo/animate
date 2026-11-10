---
title: Stufe 6: Welches Verfahren wann?
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1180800
summary: Beide Verfahren liefern dasselbe.
tags: Dualität
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Beide Verfahren liefern dasselbe. Diese Stufe klärt, welches weniger Arbeit macht und was jedes nicht kann.
:::

**Die Idee.** Die Rechenarbeit steckt in der Größe der Matrix. Das Maschenstromverfahren braucht $z-k+1$ Unbekannte, das Knotenpotentialverfahren $k-1$. Viele Zweige an wenigen Knoten bedeuten viele Maschen, aber wenige Knoten. Lange Ketten bedeuten das Gegenteil.

:::satz Satz 6.1 (Vergleich der Gleichungszahl)
<span class="anker" id="satz-6-1"></span>

Das Knotenpotentialverfahren braucht genau dann weniger Gleichungen, wenn $k-1<z-k+1$ ist, also

<span class="anker" id="gl-6-1"></span>
$$z>2k-2. \tag{6.1}$$
:::

⁠**So liest man das:** Im Mittel hängen an einem Knoten $2z/k$ Zweigenden, denn jeder Zweig hat zwei Enden. Auf der Grenze sind das $4-4/k$, also knapp vier. Hängen im Mittel mehr Zweige an den Knoten, gewinnt das Knotenpotentialverfahren (Abb. [6](#abb-6)). **Gültigkeit:** Jede reale Quelle zählt als ein Zweig, denn für die Maschen wird sie zu Spannungsquelle und Reihenwiderstand. An $k-1$ ändert das Umwandeln nichts.

:::abbildung et1/k8zahl 6
Jeder Punkt ist ein Netz. Unterhalb von $z=k-1$ wäre es nicht zusammenhängend. Oberhalb der roten Geraden $z=2k-2$ braucht das Knotenpotentialverfahren weniger Gleichungen, darunter das Maschenstromverfahren, auf der Geraden sind beide gleich.
:::

|  | Maschenstromverfahren | Knotenpotentialverfahren |
|---|---|---|
| Unbekannte | $z-k+1$ Maschenströme | $k-1$ Knotenpotentiale |
| von selbst erfüllt | Knotenregel | Maschenregel |
| aufgestellt | Maschenregeln | Knotenregeln |
| Matrix | $\mathbf Z$ in $\Omega$ | $\mathbf Y$ in S |
| Diagonale | Summe der Widerstände der Masche | Summe der Leitwerte am Knoten |
| Nebendiagonale | $\pm$ gemeinsamer Widerstand | $-$ Koppelleitwert |
| rechte Seite | Quellenspannungen | Quellenströme |
| stört | Stromquelle | Spannungsquelle |
| kleinster Fall | Reihenschaltung, $m=1$ | Parallelschaltung, $k-1=1$ |
| Einsatz | Handrechnung | Handrechnung und Simulator |

Die Tabelle zeigt eine __Dualität__, eine Spiegelung: Tauscht man Masche und Knoten, Strom und Spannung, Reihe und parallel, Widerstand und Leitwert, wird aus dem einen Verfahren das andere. Der Grund liegt in Kirchhoff: Beide Regeln sagen „die Summe ist null“, nur über verschiedene Mengen.

::::beispiel
Das Rechenmodell hat nach dem Umwandeln rechts $k=3$ und $z=5$. Es liegt mit $5>4$ über der Geraden, und tatsächlich waren es drei Maschen gegen zwei Knoten.
::::

⁠**Grenzfall:** Die Brücke aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) mit $k=4$ und $z=6$ liegt genau auf der Geraden. Dann entscheiden die Quellen: Eine ideale Spannungsquelle spricht für Maschen, denn sie steht dort auf der rechten Seite.

Simulatoren verwenden nur Knotenpotentiale. Die Maschen eines Netzes muss ein Programm erst suchen, und Fenster gibt es nur, wenn sich das Netz ohne Kreuzungen zeichnen lässt. Knoten dagegen stehen schon in der Schaltungsbeschreibung (Stufe [7](stempel-und-netzliste.html#stufe-7)).

:::frage Ist das Maschenstromverfahren nicht überflüssig, wenn die Simulatoren es nicht nutzen?
Für große Netze ja. Von Hand ist es oft kürzer, und es hält den Blick auf die Stromkreise gerichtet: Man sieht, welche Ströme sich welchen Weg teilen. Bei wenigen Maschen und vielen Knoten, etwa in langen Ketten aus Reihenschaltungen, gewinnt es klar.
:::

:::aufgabe Aufgabe 8 ★ Das Verfahren wählen
<span class="anker" id="aufg-8"></span>

Welches Verfahren braucht weniger Gleichungen? Gib beide Zahlen an.

<ol class="al">

<li>

Drei reale Spannungsquellen liegen parallel an einer Last, jede als ein Zweig.

</li>

<li>

Ein Ring aus sechs Bauteilen.

</li>

<li>

Fünf Knoten, jeder mit jedem verbunden.

</li>

<li>

Zeige: Fasst man an einem Netz zwei Bauteile in Reihe mit dem Knoten dazwischen zusammen, sinken $k$ und $z$ um 1, $m$ bleibt.

</li>

</ol>

:::loesung
(a) $k=2$, $z=4$: $m=3$ gegen $k-1=1$, Knotenpotentiale. Hier ist $z=4>2$.

(b) $k=6$, $z=6$: $m=1$ gegen 5, Maschenströme.

(c) $k=5$, $z=10$: $m=6$ gegen 4, Knotenpotentiale.

(d) Der Knoten dazwischen entfällt und aus zwei Zweigen wird einer, also $m'=(z-1)-(k-1)+1=z-k+1=m$. Die Zählung aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html) kommt zum selben Schluss.
:::
:::
