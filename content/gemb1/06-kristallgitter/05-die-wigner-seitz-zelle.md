---
title: Stufe 3: Die Wigner-Seitz-Zelle
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallgitter
order: 4160500
summary: Die primitive Zelle ist nicht eindeutig, schon in der Kette lässt sich die Zelle beliebig verschieben.
tags: Wigner-Seitz-Zelle
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Die primitive Zelle ist nicht eindeutig, schon in der Kette lässt sich die Zelle beliebig verschieben. Diese Stufe gibt eine Vorschrift ohne jede Wahl.
:::

**Die Idee.** Jeder Gitterpunkt bekommt sein Hoheitsgebiet: alle Orte, die ihm näher liegen als jedem anderen Gitterpunkt. Jeder Ort gehört zu seinem nächsten Gitterpunkt, also füllen die Gebiete den Raum lückenlos. Alle Punkte haben dieselbe Umgebung, also sind alle Gebiete gleich. Dieses Gebiet ist damit eine primitive Zelle.

:::definition Definition 3.1 (Wigner-Seitz-Zelle)
<span class="anker" id="satz-3-1"></span>

Die __Wigner-Seitz-Zelle__ eines Gitterpunkts enthält alle Orte, die diesem Punkt näher sind als jedem anderen Gitterpunkt. Sie entsteht so:

<ol>

<li>

Zeichne die Verbindungslinien zu den Nachbarn.

</li>

<li>

Schneide jede Verbindungslinie senkrecht durch ihre Mitte (im Raum mit einer Ebene).

</li>

<li>

Das kleinste Gebiet um den Punkt, das diese Schnitte einschließen, ist die Wigner-Seitz-Zelle.

</li>

</ol>
:::

⁠**So liest man das:** Die Mittelsenkrechte enthält genau die Orte, die von beiden Punkten gleich weit entfernt sind. Sie trennt also zwei Hoheitsgebiete. Der Inhalt der Zelle ist $\Omega$ aus [(1.2)](punktgitter-und-basis.html#gl-1-2). **Gültigkeit:** Die Vorschrift setzt ein Bravais-Gitter voraus. Bei einer Basis zeichnet man die Zelle um die Gitterpunkte und zählt dann die Atome darin.

:::abbildung gemb1/k6wigner 3
Zentriert rechteckiges Gitter. Links: Verbindungslinien (grün), ihre Mittelsenkrechten (rot) und die Wigner-Seitz-Zelle (blau) um den offenen Punkt. Rechts: drei primitive Zellen desselben Gitters mit gleicher Fläche.
:::

**Die einfachen Fälle.** In der Kette ist die Zelle eine Strecke der Länge $a$ mit je $a/2$ links und rechts vom Punkt, im rechteckigen und quadratischen Gitter das Rechteck um den Punkt, im hexagonalen Gitter ein regelmäßiges Sechseck mit der Seite $a/\sqrt3$, sonst ein ungleichseitiges Sechseck.

**Beispiel.** Ein zentriert rechteckiges Gitter hat ein Rechteck mit $a=0{,}40$ nm und $b=0{,}60$ nm (Abb. [3](#abb-3)). Das Rechteck enthält zwei Gitterpunkte, also ist $\Omega=a\,b/2=0{,}12\,\mathrm{nm^2}$. Die Schnitte ergeben ein Sechseck mit den Ecken $(\pm0{,}2;\,\pm0{,}083)$ nm und $(0;\,\pm0{,}217)$ nm. Seine Fläche ist 0,12 nm$^2$. Das Rechteck hat dagegen 0,24 nm$^2$, es ist eine Einheitszelle, aber nicht primitiv.

Ein zweites Beispiel zeigt, dass Gittervektoren nicht längs der Koordinatenachsen liegen müssen. Die Vektoren

<span class="anker" id="gl-3-1"></span>
$$\boldsymbol a_1=\frac{1}{\sqrt2}\,(a,\,a),\qquad \boldsymbol a_2=\frac{1}{\sqrt2}\,(-a,\,a) \tag{3.1}$$

haben die Länge $a$ und stehen senkrecht, denn $\boldsymbol a_1\cdot\boldsymbol a_2=0$. Sie erzeugen ein quadratisches Gitter, das um 45° gegen die Achsen gedreht ist. Seine Wigner-Seitz-Zelle ist ein Quadrat mit der Kante $a$. **Grenzfall:** Für $a=b$ im zentrierten Rechteck entsteht das gedrehte quadratische Gitter aus Stufe [2](bravais-gitter-in-einer-und-zwei-dimensionen.html#stufe-2), und das Sechseck wird zum Quadrat.

:::frage Reichen immer die nächsten Nachbarn?
Nein. Im Beispiel liegen die vier nächsten Nachbarn 0,361 nm entfernt. Ihre Schnitte schließen eine Raute von 0,141 nm$^2$ ein, und das ist mehr als $\Omega$. Die Nachbarn in 0,40 nm Abstand schneiden die Spitzen ab. Man nimmt so viele Nachbarn, bis kein weiterer Schnitt das Gebiet mehr verkleinert. Die Probe ist der Inhalt: Er muss $\Omega$ ergeben.
:::

:::aufgabe Aufgabe 3 ★★ Zellen konstruieren
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Ein hexagonales Gitter hat $a=0{,}246$ nm. Berechne Seite und Fläche der Wigner-Seitz-Zelle und vergleiche mit $\frac{\sqrt3}2a^2$.

</li>

<li>

Die Gitterpunkte aus (a) sitzen in den Mitten der Waben von Graphen. Wie viele Atome liegen in der Zelle?

</li>

<li>

Ein Gitter hat $\boldsymbol a_1=(3,0)$ nm und $\boldsymbol a_2=(1,2)$ nm. Welche sechs Nachbarn braucht man? Bestimme die Ecken der Zelle und prüfe ihre Fläche.

</li>

</ol>

:::loesung
(a) Die Mittelsenkrechten liegen $a/2$ vom Punkt entfernt. Das regelmäßige Sechseck hat die Seite $s=a/\sqrt3=0{,}142$ nm und die Fläche $6\cdot\frac{\sqrt3}4s^2=0{,}0524\,\mathrm{nm^2}$. Das ist $\frac{\sqrt3}2a^2$. (b) Die Zelle ist genau eine Wabe. Ihre sechs Ecken sind Atome, jedes gehört zu drei Waben: $6\cdot\frac13=2$ Atome. (c) Die kürzesten Gittervektoren sind $\pm(1,2)$ mit 2,24 nm, $\pm(2,-2)$ mit 2,83 nm und $\pm(3,0)$ mit 3,00 nm. Die Schnitte $x+2y=2{,}5$, $-x+y=2$, $x=1{,}5$ und ihre Gegenstücke ergeben die Ecken $(\pm1{,}5;\,\pm0{,}5)$ nm, $(0{,}5;\,-1{,}5)$ nm und $(-0{,}5;\,1{,}5)$ nm. Die Fläche ist 6 nm$^2$, wie in Aufgabe [1](punktgitter-und-basis.html#aufg-1).
:::
:::
