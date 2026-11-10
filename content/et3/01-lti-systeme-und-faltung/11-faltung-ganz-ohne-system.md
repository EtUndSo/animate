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
