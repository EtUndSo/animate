---
title: Stufe 10: Faltung ganz ohne System
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / LTI-Systeme und Faltung
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Kapitel 1: LTI-Systeme und Faltung
order: 3211100
summary: Warum die Antwort auf einen einzigen Stoß das ganze System beschreibt
tags: 
lang: de
---

<span class="anker" id="stufe-10"></span>

:::frage Die Faltung wird meist an einem System erklärt, durch das ein Signal läuft. Was bedeutet sie, wenn gar kein System im Spiel ist?
Die Faltung ist eine Rechenoperation mit einer eigenen, allgemeinen Bedeutung: *Für jede Art, ein Ergebnis in zwei Anteile aufzuteilen, multipliziert man die Gewichte der beiden Anteile und summiert über alle Aufteilungen.* Das System ist eine Deutung davon (Anteil 1: wann kam der Stoß, Anteil 2: wie alt ist er), nicht die einzige.

⁠**Beispiel ohne System und ohne Zeit: zwei Würfel.** Mit welcher Wahrscheinlichkeit ist die Augensumme $k$? Jede Aufteilung $k=i+(k-i)$ trägt bei, mit der Wahrscheinlichkeit $P_1(i)\,P_2(k-i)$:

$$P(k)=\sum_iP_1(i)\,P_2(k-i).$$

Das ist eine Faltung, mit genau derselben Struktur wie $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau$: $\tau$ entspricht der Augenzahl des ersten Würfels, $t$ der Summe, $t-\tau$ der Augenzahl des zweiten. Zwei gleichverteilte Würfel („Rechtecke“) ergeben eine Dreieckverteilung, genau wie $\operatorname{rect}*\operatorname{rect}=\Lambda$ in Aufgabe [5](die-faltung-ausrechnen.html#aufg-5). Die 7 ist am häufigsten, weil sie die meisten Aufteilungen hat (Abb. [9](#abb-9)).

Weitere Beispiele: Ein gleitender Mittelwert über Messwerte ist eine Faltung mit einem Rechteck. Ein unscharfes Foto ist das scharfe Bild, gefaltet mit dem Lichtfleck, den die Optik aus einem Punkt macht. Und wer zwei Polynome multipliziert, faltet ihre Koeffizienten (Aufgabe [11](#aufg-11)).
:::

:::abbildung et3/k1wuerfel 9
Wahrscheinlichkeiten der Augensumme. Jede Verteilung ist die Faltung der vorigen mit der eines einzelnen Würfels. Aus dem Rechteck wird ein Dreieck ($P(7)=6/36$), daraus eine glockenförmige Kurve ($P(10)=P(11)=27/216$).
:::

:::zusatz Warum Faltungen so oft auftreten
Faltet man immer mehr gleiche Verteilungen, nähert sich das Ergebnis einer Gaußkurve, fast unabhängig von der Ausgangsform (zentraler Grenzwertsatz). Deshalb ist Rauschen, die Summe vieler kleiner unabhängiger Einflüsse, so oft gaußverteilt.
:::

:::aufgabe Aufgabe 11 ★ Faltung mit Würfeln und Polynomen
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Berechne $P(7)$ und $P(4)$ für zwei Würfel aus der Faltungssumme. Welche Aufteilungen tragen jeweils bei?

</li>

<li>

Berechne $P(10)$ für drei Würfel, indem du die Verteilung zweier Würfel mit der eines Würfels faltest.

</li>

<li>

Multipliziere $(1+2x)(3+x)$ aus. Zeige, dass die Koeffizientenfolge des Ergebnisses die Faltung der Folgen $(1,2)$ und $(3,1)$ ist.

</li>

</ol>

:::loesung
(a) $P(7)$: Aufteilungen $1+6,\,2+5,\dots,6+1$, sechs Stück, jede mit $\frac16\cdot\frac16$: $P(7)=\frac{6}{36}=\frac16$. $P(4)$: $1+3,\,2+2,\,3+1$: $\frac{3}{36}=\frac{1}{12}$.

(b) $P_3(10)=\sum_{j=1}^6P_2(10-j)\cdot\frac16=\frac16\bigl[P_2(9)+P_2(8)+P_2(7)+P_2(6)+P_2(5)+P_2(4)\bigr]=\frac16\cdot\frac{4+5+6+5+4+3}{36}=\frac{27}{216}=\frac18$.

(c) $(1+2x)(3+x)=3+x+6x+2x^2=3+7x+2x^2$. Der Koeffizient von $x^k$ sammelt alle Paare von Potenzen $i+j=k$: $c_0=1\cdot3=3$, $c_1=1\cdot1+2\cdot3=7$, $c_2=2\cdot1=2$. Das ist die Faltungssumme $c_k=\sum_ia_ib_{k-i}$, dieselbe Struktur wie bei den Würfeln.
:::
:::

::::kurzfassung
Die Faltung ist eine Rechenoperation mit einer eigenen, allgemeinen Bedeutung: Für jede Art, ein Ergebnis in zwei Anteile aufzuteilen, multipliziert man die Gewichte der beiden Anteile und summiert über alle Aufteilungen.

Ein System ist nur eine Deutung davon, mit dem Zeitpunkt $\tau$ eines Stoßes als erstem und seinem Alter $t-\tau$ als zweitem Anteil. Ein Beispiel ohne System und ohne Zeit ist die Augensumme $k$ zweier Würfel. Jede Aufteilung $k=i+(k-i)$ trägt mit der Wahrscheinlichkeit $P_1(i)\,P_2(k-i)$ bei:

$$P(k)=\sum_iP_1(i)\,P_2(k-i).$$

Darin sind $P_1$ und $P_2$ die Wahrscheinlichkeiten der Augenzahlen des ersten und des zweiten Würfels. Ebenso ist ein gleitender Mittelwert über Messwerte eine Faltung mit einem Rechteck. Ein unscharfes Foto ist das scharfe Bild, gefaltet mit dem Lichtfleck, den die Optik aus einem Punkt macht. Wer zwei Polynome multipliziert, faltet ihre Koeffizienten.

Der Grund für die Form der Ergebnisse: Zwei gleichverteilte Würfel, also zwei „Rechtecke“, ergeben eine Dreieckverteilung, genau wie $\operatorname{rect}*\operatorname{rect}=\Lambda$. Die 7 ist am häufigsten, weil sie die meisten Aufteilungen hat. Faltet man immer mehr gleiche Verteilungen, nähert sich das Ergebnis einer Gaußkurve, fast unabhängig von der Ausgangsform.

Falle: Das Produkt $P_1(i)\,P_2(k-i)$ setzt voraus, dass die beiden Würfel einander nicht beeinflussen. Nur dann multiplizieren sich die Wahrscheinlichkeiten der Anteile.
::::

::::formelsammlung
**Augensumme zweier Würfel**

$$P(k)=\sum_iP_1(i)\,P_2(k-i)$$

$P_1$, $P_2$ Wahrscheinlichkeiten der Augenzahlen des ersten und zweiten Würfels, die einander nicht beeinflussen; Summe über alle Aufteilungen $k=i+(k-i)$. Dieselbe Struktur wie $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau$: $\tau$ entspricht $i$, $t$ entspricht $k$, $t-\tau$ entspricht $k-i$.

**Zwei Rechtecke ergeben ein Dreieck**

$$\operatorname{rect}*\operatorname{rect}=\Lambda$$

Ebenso ergeben zwei gleichverteilte Würfel eine Dreieckverteilung.
::::

::::lernkarten
:::karte zusammenhang Faltung ohne System
Was bedeutet die Faltung, wenn gar kein System im Spiel ist, durch das ein Signal läuft?
---
Sie ist eine Rechenoperation mit eigener Bedeutung: Für jede Aufteilung eines Ergebnisses in zwei Anteile multipliziert man deren Gewichte und summiert über alle Aufteilungen. Das System ist nur eine Deutung davon.
--- falsch
Ohne System hat sie keine Bedeutung: Sie ist als Antwort eines LTI-Systems auf einen Eingang definiert und braucht dafür eine Zeitachse, eine Impulsantwort und ein Signal, das durch das System läuft.
--- falsch
Sie bildet für jede Art, ein Ergebnis in zwei Anteile aufzuteilen, die Summe der Gewichte beider Anteile und nimmt davon den größten Wert. Das System ist nur eine Deutung davon, nicht die einzige.
--- falsch
Sie multipliziert zwei Funktionen Punkt für Punkt und integriert das Produkt über alle Zeiten. Der Wert gibt an, wie ähnlich die beiden Funktionen einander sind, ganz ohne ein System.
:::
:::karte formel Augensumme zweier Würfel
Wie berechnet man die Wahrscheinlichkeit $P(k)$, dass zwei Würfel zusammen die Augensumme $k$ zeigen?
---
$P(k)=\sum_iP_1(i)\,P_2(k-i)$: Jede Aufteilung $k=i+(k-i)$ trägt mit der Wahrscheinlichkeit $P_1(i)\,P_2(k-i)$ bei. Das ist eine Faltung mit derselben Struktur wie $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau$.
--- falsch
$P(k)=P_1(k)\,P_2(k)$: Beide Würfel müssen die Zahl $k$ zeigen, und weil sie einander nicht beeinflussen, multipliziert man ihre Wahrscheinlichkeiten. Eine Faltung ist dafür nicht nötig.
--- falsch
$P(k)=\sum_iP_1(i)\,P_2(k+i)$: Jede Aufteilung trägt bei, und das Pluszeichen kommt daher, dass sich die Augenzahlen der beiden Würfel addieren. Das ist eine Faltung wie beim Faltungsintegral.
--- falsch
$P(k)=\frac{1}{11}$ für jedes $k$ von 2 bis 12: Jede Augensumme ist gleich wahrscheinlich, weil jeder einzelne Würfel gleichverteilt ist und die Summe diese Eigenschaft von ihnen erbt.
:::
:::karte zusammenhang Entsprechung zum Faltungsintegral
Welchen Größen beim Würfeln entsprechen $\tau$, $t$ und $t-\tau$ im Faltungsintegral?
---
$\tau$ entspricht der Augenzahl des ersten Würfels, $t$ der Augensumme und $t-\tau$ der Augenzahl des zweiten Würfels.
--- falsch
$\tau$ entspricht der Augensumme, $t$ der Augenzahl des ersten Würfels und $t-\tau$ der Augenzahl des zweiten Würfels.
--- falsch
$\tau$ entspricht dem Zeitpunkt des ersten Wurfs, $t$ dem des zweiten Wurfs und $t-\tau$ der Pause zwischen beiden Würfen.
--- falsch
$\tau$ entspricht der Augenzahl des ersten Würfels, $t$ der des zweiten und $t-\tau$ dem Unterschied zwischen beiden Augenzahlen.
:::
:::karte zusammenhang Die Sieben am häufigsten
Warum ist bei zwei Würfeln die Augensumme 7 am wahrscheinlichsten?
---
Weil sie die meisten Aufteilungen hat: $1+6$, $2+5$ bis $6+1$, sechs Stück, jede mit $\frac16\cdot\frac16$. Also ist $P(7)=\frac{6}{36}=\frac16$; die 4 hat nur drei Aufteilungen und $\frac{3}{36}$.
--- falsch
Weil sie die meisten Aufteilungen hat, nämlich zwölf, wenn man jede Reihenfolge doppelt zählt, jede mit $\frac16\cdot\frac16$. Also ist $P(7)=\frac{12}{36}=\frac13$; die 4 hat sechs Aufteilungen.
--- falsch
Weil 7 die Mitte zwischen 2 und 12 ist; die mittlere Summe ist immer am wahrscheinlichsten, auch bei Würfeln, deren Augenzahlen ungleich häufig sind. Das folgt allein aus der Symmetrie der Summe.
--- falsch
Weil jeder einzelne Würfel am häufigsten 3 oder 4 zeigt, denn diese Zahlen liegen in der Mitte; die Summe der beiden häufigsten Augenzahlen ergibt 7. Also ist $P(7)=\frac{2}{6}$.
:::
:::karte zusammenhang Dreieckverteilung
Welche Verteilung ergibt die Augensumme zweier gleichverteilter Würfel, und welches Faltungsergebnis entspricht dem?
---
Eine Dreieckverteilung, genau wie $\operatorname{rect}*\operatorname{rect}=\Lambda$: Die Faltung zweier Rechtecke ergibt ein Dreieck.
--- falsch
Wieder eine Gleichverteilung, wie $\operatorname{rect}*\operatorname{rect}=\operatorname{rect}$: Die Faltung erhält die Form eines Rechtecks.
--- falsch
Eine Gaußverteilung, denn schon die Summe zweier Würfel ist genau gaußförmig, wie $\operatorname{rect}*\operatorname{rect}=\mathrm{e}^{-\pi t^2}$.
--- falsch
Eine Dreieckverteilung mit der Spitze bei 12, weil die Summe mit der Augenzahl wächst; das entspricht $\operatorname{rect}*\Lambda$.
:::
:::karte zusammenhang Drei Würfel
Wie erhält man die Verteilung der Augensumme dreier Würfel, und welche Form hat sie?
---
Man faltet die Verteilung zweier Würfel mit der eines einzelnen Würfels. Aus dem Dreieck wird eine glockenförmige Kurve mit $P(10)=P(11)=27/216$.
--- falsch
Man multipliziert die Verteilung zweier Würfel Punkt für Punkt mit der eines einzelnen. Das Ergebnis ist wieder ein Dreieck, nur schmaler.
--- falsch
Man faltet die Verteilung zweier Würfel mit der eines einzelnen. Das Ergebnis ist wieder ein Dreieck, weil Falten mit einem Rechteck die Form erhält.
--- falsch
Man addiert die Verteilungen dreier einzelner Würfel. Das Ergebnis ist ein Rechteck von 3 bis 18 mit derselben Wahrscheinlichkeit für jede Summe.
:::
:::karte zusammenhang Unscharfes Foto
Wie lässt sich ein unscharfes Foto als Faltung beschreiben?
---
Als das scharfe Bild, gefaltet mit dem Lichtfleck, den die Optik aus einem einzelnen Punkt macht.
--- falsch
Als das scharfe Bild, multipliziert mit dem Lichtfleck der Optik; je größer der Fleck, desto heller das Foto.
--- falsch
Als das scharfe Bild, gefaltet mit sich selbst; die Unschärfe entsteht, weil sich das Bild in der Optik überlagert.
--- falsch
Als das scharfe Bild, gefaltet mit einem Dirac-Impuls; der Impuls verschmiert jeden Bildpunkt zu einem kleinen Fleck.
:::
:::karte formel Polynome multiplizieren
Wie hängt das Ausmultiplizieren zweier Polynome mit der Faltung zusammen, etwa bei $(1+2x)(3+x)$?
---
Die Koeffizientenfolge des Produkts ist die Faltung der beiden Folgen, $c_k=\sum_ia_ib_{k-i}$. Aus $(1,2)$ und $(3,1)$ wird $3+7x+2x^2$, denn $c_1=1\cdot1+2\cdot3=7$.
--- falsch
Die Koeffizienten werden stellenweise multipliziert, $c_k=a_kb_k$, weil nur gleiche Potenzen zusammenpassen. Aus $(1,2)$ und $(3,1)$ wird so $3+2x$, ohne ein Glied mit $x^2$.
--- falsch
Die Koeffizientenfolge des Produkts ist die Summe der beiden Folgen, $c_k=a_k+b_k$, weil sich die Potenzen beim Multiplizieren addieren. Aus $(1,2)$ und $(3,1)$ wird $4+3x$.
--- falsch
Die Koeffizientenfolge ist eine Faltung, aber mit $c_k=\sum_ia_ib_{k+i}$, weil die Exponenten zusammengezählt werden. Aus $(1,2)$ und $(3,1)$ wird so $5+x$.
:::
:::karte zusammenhang zentraler Grenzwertsatz
Warum ist Rauschen so oft gaußverteilt?
---
Faltet man immer mehr gleiche Verteilungen, nähert sich das Ergebnis einer Gaußkurve, fast unabhängig von der Ausgangsform (zentraler Grenzwertsatz). Rauschen ist die Summe vieler kleiner unabhängiger Einflüsse.
--- falsch
Weil jeder einzelne Einfluss schon gaußverteilt ist; Summen gaußverteilter Einflüsse bleiben gaußverteilt, und andere Verteilungen kommen bei elektrischen Störungen praktisch nicht vor, weder bei Bauteilen noch bei Leitungen.
--- falsch
Weil Rauschen von einem einzigen großen Einfluss stammt, dessen Verteilung gaußförmig ist; viele kleine unabhängige Einflüsse würden sich dagegen gegenseitig aufheben und kein Rauschen ergeben.
--- falsch
Weil die Gaußkurve als einzige Verteilung die Fläche 1 hat; jede Verteilung von Messwerten muss die Fläche 1 haben und wird deshalb mit der Zeit gaußförmig, gleich woher das Rauschen stammt.
:::
::::
