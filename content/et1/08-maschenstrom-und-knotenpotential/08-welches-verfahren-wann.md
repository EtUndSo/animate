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

::::formelsammlung
**Vergleich der Gleichungszahl**

$$k-1<z-k+1,\qquad\text{also}\qquad z>2k-2$$

Dann braucht das Knotenpotentialverfahren ($k-1$ Unbekannte) weniger Gleichungen als das Maschenstromverfahren ($z-k+1$ Unbekannte). Jede reale Quelle zählt als ein Zweig. Auf der Geraden $z=2k-2$ sind beide gleich, dann entscheiden die Quellen.

**Mittlere Zahl der Zweigenden je Knoten**

$$2z/k,\qquad\text{auf der Grenze}\quad 4-4/k$$

Jeder Zweig hat zwei Enden. Hängen im Mittel mehr als knapp vier Zweige an einem Knoten, gewinnt das Knotenpotentialverfahren.
::::

::::lernkarten
:::karte formel Vergleich der Gleichungszahl
Unter welcher Bedingung braucht das Knotenpotentialverfahren weniger Gleichungen als das Maschenstromverfahren?
---
Wenn $k-1<z-k+1$ ist, also $z>2k-2$. Das Maschenstromverfahren braucht $z-k+1$ Unbekannte, das Knotenpotentialverfahren $k-1$. Jede reale Quelle zählt dabei als ein Zweig.
--- falsch
Wenn $k-1>z-k+1$ ist, also $z<2k-2$. Das Maschenstromverfahren braucht $z-k+1$ Unbekannte, das Knotenpotentialverfahren $k-1$. Jede reale Quelle zählt dabei als zwei Zweige.
--- falsch
Wenn $k-1<z-k+1$ ist, also $z>2k-2$. Das Maschenstromverfahren braucht $z-k+1$ Unbekannte, das Knotenpotentialverfahren $k$, weil auch der Bezugsknoten eine Gleichung bekommt.
--- falsch
Wenn das Netz mehr Knoten als Zweige hat, also $k>z$. Das Maschenstromverfahren braucht dann $z$ Unbekannte, das Knotenpotentialverfahren nur $k-1$, und die kleinere Zahl gewinnt.
:::
:::karte zusammenhang Zweigenden je Knoten
Woran erkennt man an der mittleren Zahl der Zweige je Knoten, welches Verfahren weniger Gleichungen braucht?
---
Im Mittel hängen an einem Knoten $2z/k$ Zweigenden, denn jeder Zweig hat zwei Enden. Auf der Grenze sind das $4-4/k$, also knapp vier. Hängen im Mittel mehr Zweige an den Knoten, gewinnt das Knotenpotentialverfahren.
--- falsch
Im Mittel hängen an einem Knoten $z/k$ Zweige, denn jeder Zweig gehört zu genau einem Knoten. Auf der Grenze sind das knapp zwei. Hängen im Mittel mehr Zweige an den Knoten, gewinnt das Maschenstromverfahren.
--- falsch
Im Mittel hängen an einem Knoten $2z/k$ Zweigenden, denn jeder Zweig hat zwei Enden. Auf der Grenze sind das knapp vier. Hängen im Mittel mehr Zweige an den Knoten, gewinnt das Maschenstromverfahren.
--- falsch
Im Mittel hängen an einem Knoten $2z/k$ Zweigenden. Auf der Grenze sind das genau zwei, wie in einer Kette. Hängen im Mittel mehr Zweige an den Knoten, gewinnt das Knotenpotentialverfahren.
:::
:::karte begriff Dualität
Was bezeichnet man als Dualität zwischen dem Maschenstrom- und dem Knotenpotentialverfahren?
---
Eine Spiegelung zwischen beiden Verfahren: Tauscht man Masche und Knoten, Strom und Spannung, Reihe und parallel, Widerstand und Leitwert, wird aus dem einen Verfahren das andere.
--- falsch
Die Tatsache, dass beide Verfahren für jedes Netz gleich viele Gleichungen brauchen. Tauscht man Masche und Knoten, bleibt die Zahl der Unbekannten gleich, weil $m=k-1$ gilt.
--- falsch
Eine Spiegelung zwischen beiden Verfahren: Tauscht man Masche und Knoten, Strom und Spannung, wird aus dem einen das andere. Widerstand und Reihe bleiben dabei, wie sie sind.
--- falsch
Die Tatsache, dass beide Verfahren nur gemeinsam ein Netz vollständig lösen. Das eine liefert die Ströme, das andere die Spannungen, erst zusammen erfüllen sie Kirchhoff.
:::
:::karte zusammenhang Grund der Dualität
Woran liegt es, dass Maschenstrom- und Knotenpotentialverfahren einander spiegeln?
---
An Kirchhoff: Knotenregel und Maschenregel sagen beide „die Summe ist null“, nur über verschiedene Mengen. Jedes Verfahren erfüllt eine der beiden Regeln von selbst und stellt die andere auf.
--- falsch
An den Bauteilen: Jeder Widerstand ist zugleich ein Leitwert, deshalb lässt sich jede Rechnung mit Widerständen auch mit Leitwerten führen. Die Kirchhoff-Regeln spielen dafür keine Rolle.
--- falsch
An den Quellen: Jede Spannungsquelle lässt sich in eine Stromquelle umwandeln, und damit wird aus jeder Masche ein Knoten. Ohne Quellen im Netz gäbe es keine Spiegelung.
--- falsch
An Kirchhoff: Beide Verfahren stellen dieselben Gleichungen auf, nur in anderer Reihenfolge. Deshalb sind auch ihre Matrizen gleich, bis auf die Einheit der Einträge.
:::
:::karte zusammenhang Welche Quelle stört welches Verfahren
Welche Quellenart stört das Maschenstromverfahren und welche das Knotenpotentialverfahren, und was tut man mit realen Quellen?
---
Stromquellen stören die Maschen, Spannungsquellen die Knoten. Reale Quellen wandelt man vorher um: für die Maschen in eine Spannungsquelle mit Reihenwiderstand, für die Knoten in eine Stromquelle mit Parallelwiderstand.
--- falsch
Spannungsquellen stören die Maschen, Stromquellen die Knoten. Reale Quellen wandelt man vorher um: für die Maschen in eine Stromquelle mit Parallelwiderstand, für die Knoten in eine Spannungsquelle mit Reihenwiderstand.
--- falsch
Stromquellen stören die Maschen, Spannungsquellen die Knoten. Reale Quellen lassen sich aber nicht umwandeln, deshalb wählt man stets das Verfahren, zu dem die Mehrzahl der Quellen im Netz passt.
--- falsch
Beide Verfahren werden von beiden Quellenarten gleich gestört. Man entfernt deshalb vor der Rechnung alle Quellen aus dem Netz und berücksichtigt sie erst am Ende durch nachträgliches Addieren.
:::
:::karte zusammenhang Reale Quelle als Zweig
Wie zählt eine reale Quelle beim Vergleich der Gleichungszahl, und warum ändert das Umwandeln nichts an $k-1$?
---
Als ein Zweig, denn für die Maschen wird sie zu Spannungsquelle und Reihenwiderstand. Vor und nach dem Umwandeln hängt sie zwischen denselben zwei Knoten, deshalb bleibt $k-1$ gleich.
--- falsch
Als zwei Zweige, Quelle und Widerstand getrennt, weil beide eigene Bauteile sind. Beim Umwandeln entsteht zwischen ihnen ein neuer Knoten, deshalb wächst $k-1$ um eins.
--- falsch
Als kein Zweig, weil Quellen keine Widerstände sind und nicht in die Matrix eingehen. Das Umwandeln ändert deshalb weder $z$ noch $k-1$, es betrifft nur die rechte Seite.
--- falsch
Als ein Zweig für das Knotenpotentialverfahren und als zwei für das Maschenstromverfahren. Beim Umwandeln ändert sich die Zahl der Knoten, je nachdem, in welche Richtung man umwandelt.
:::
:::karte zusammenhang Simulatoren rechnen mit Knoten
Warum verwenden Schaltungssimulatoren Knotenpotentiale und keine Maschenströme?
---
Die Maschen eines Netzes müsste ein Programm erst suchen, und Fenster gibt es nur, wenn sich das Netz ohne Kreuzungen zeichnen lässt. Knoten dagegen stehen schon in der Schaltungsbeschreibung.
--- falsch
Weil Knotenpotentiale genauer sind als Maschenströme. Bei Maschenströmen addieren sich die Rundungsfehler in den gemeinsamen Zweigen von Masche zu Masche, bei Potenzialen bleiben sie auf die einzelnen Knoten beschränkt.
--- falsch
Weil das Maschenstromverfahren keine Widerstände verarbeiten kann, die zu mehr als zwei Maschen gehören. In großen Schaltungen kommt das fast überall vor.
--- falsch
Weil Simulatoren nur Spannungen bestimmen können. Ströme müssten sie über zusätzliche Messwiderstände ermitteln, und die würden die Schaltung verändern.
:::
:::karte zusammenhang Wann Maschenströme gewinnen
In welchen Netzen ist das Maschenstromverfahren dem Knotenpotentialverfahren überlegen, obwohl Simulatoren es nicht nutzen?
---
Bei wenigen Maschen und vielen Knoten, etwa in langen Ketten aus Reihenschaltungen. Von Hand ist es dort kürzer, und es hält den Blick auf die Stromkreise: Man sieht, welche Ströme sich welchen Weg teilen.
--- falsch
Bei vielen Zweigen an wenigen Knoten, etwa bei vielen parallel geschalteten Quellen. Dort gibt es viele Maschen, und jede bringt eine einfache Gleichung mit, die man leicht von Hand und ganz ohne Matrix löst.
--- falsch
In großen Netzen mit Tausenden Bauteilen, weil die Widerstandsmatrix dort kleiner bleibt als die Leitwertmatrix. Simulatoren nutzen es nur aus historischen Gründen nicht.
--- falsch
In Netzen mit vielen idealen Stromquellen, weil deren Ströme auf der rechten Seite der Maschengleichungen stehen. Spannungsquellen machen das Maschenstromverfahren dagegen umständlich.
:::
:::karte zusammenhang Netze auf der Grenze
Was entscheidet über das Verfahren, wenn ein Netz genau auf der Grenze $z=2k-2$ liegt, wie die Brücke mit $k=4$ und $z=6$?
---
Dann entscheiden die Quellen. Eine ideale Spannungsquelle spricht für Maschen, denn sie steht dort einfach auf der rechten Seite, während sie in die Leitwertmatrix nicht hineinpasst.
--- falsch
Dann entscheidet die Zahl der Widerstände: Bei mehr als sechs Widerständen ist das Knotenpotentialverfahren kürzer, weil sich Leitwerte leichter addieren lassen als Widerstände.
--- falsch
Dann entscheidet die Größe der Widerstände: Bei großen Widerständen sind die Leitwerte kleine Zahlen, und das Knotenpotentialverfahren rechnet sich deshalb leichter.
--- falsch
Dann ist die Wahl beliebig, weil beide Verfahren genau dieselbe Matrix liefern. Auch die Quellen ändern daran nichts, sie stehen in beiden Verfahren auf der rechten Seite.
:::
::::
