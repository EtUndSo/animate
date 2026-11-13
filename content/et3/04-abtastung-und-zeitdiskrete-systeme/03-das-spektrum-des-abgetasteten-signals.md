---
title: Stufe 2: Das Spektrum des abgetasteten Signals
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240300
summary: Was macht das Abtasten mit dem Spektrum?
tags: Spiegelspektren
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Was macht das Abtasten mit dem Spektrum? Diese Stufe zeigt: Es wiederholt sich periodisch.
:::

**Die Idee.** Zwei Schwingungen, deren Frequenzen sich um ein Vielfaches der Abtastrate $1/T$ unterscheiden, haben dieselben Abtastwerte:

$$\mathrm{e}^{\mathrm{j}2\pi(f_0+k/T)nT}=\mathrm{e}^{\mathrm{j}2\pi f_0nT}\cdot\underbrace{\mathrm{e}^{\mathrm{j}2\pi kn}}_{=1}.$$

Die Abtastwerte können sie nicht unterscheiden. Deshalb muss das Spektrum der Abtastwerte bei $f_0$ und bei $f_0+k/T$ gleich aussehen. Es ist periodisch.

:::satz Satz 2.1 (Spektrum des ideal abgetasteten Signals)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$S_\mathrm a(f)=\frac1T\sum_{k=-\infty}^{\infty}S\Bigl(f-\frac kT\Bigr)\qquad(T>0). \tag{2.1}$$
:::

⁠**So liest man das:** Das Spektrum des Originals erscheint unverändert in der Form, aber mit dem Faktor $1/T$ und an jedem Vielfachen der Abtastrate wiederholt. Die Kopien heißen __Spiegelspektren__.

:::herleitung Spektrum des abgetasteten Signals
Multiplikation wird Faltung ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), und das Spektrum des Dirac-Kamms ist wieder ein Kamm:

$$s(t)\cdot\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;S(f)*\frac1T\sum_k\delta\Bigl(f-\frac kT\Bigr)=\frac1T\sum_kS\Bigl(f-\frac kT\Bigr).$$

Die Faltung mit einem verschobenen Dirac-Impuls verschiebt das Spektrum.
:::

:::abbildung et3/k4spektrum 1
Ein Spektrum bis $f_\mathrm g=300$ Hz (blau, dreieckig zur Übersicht), abgetastet. Oben mit 1 kHz: Die Kopien bei Vielfachen von 1 kHz liegen getrennt. Unten mit 500 Hz: Kopien im Abstand 500 Hz überlappen, die Summe (rot) ist nicht mehr das Original. Der Faktor $1/T$ ist weggelassen.
:::

:::frage Woher „weiß“ das Spektrum, dass abgetastet wurde? Das Signal zwischen den Abtastpunkten ist doch einfach weg.
Genau deshalb. Zwischen den Abtastpunkten ist das abgetastete Signal null, außer an den Impulsen. Jede Schwingung, die an allen Punkten $nT$ dieselben Werte hat, beschreibt dieses Signal gleich gut. Das Spektrum kann sich zwischen ihnen nicht entscheiden und enthält alle: das Original und seine Kopien bei jedem Vielfachen von $1/T$.
:::

::::formelsammlung
**Gleiche Abtastwerte**

$$\mathrm{e}^{\mathrm{j}2\pi(f_0+k/T)nT}=\mathrm{e}^{\mathrm{j}2\pi f_0nT}\cdot\mathrm{e}^{\mathrm{j}2\pi kn}$$

$k$, $n$ ganzzahlig, der zweite Faktor ist also 1: Schwingungen, deren Frequenzen sich um ein Vielfaches der Abtastrate $1/T$ unterscheiden, haben dieselben Abtastwerte. Deshalb ist das Spektrum der Abtastwerte periodisch.

**Abtasten im Frequenzbereich gesehen**

$$s(t)\cdot\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;S(f)*\frac1T\sum_k\delta\Bigl(f-\frac kT\Bigr)$$

Multiplikation mit dem Dirac-Kamm wird Faltung mit einem Kamm im Abstand $1/T$; die Faltung mit jedem verschobenen Dirac-Impuls verschiebt $S(f)$.

**Spektrum des ideal abgetasteten Signals**

$$S_\mathrm a(f)=\frac1T\sum_{k=-\infty}^{\infty}S\Bigl(f-\frac kT\Bigr)$$

$T>0$, $S(f)$ Spektrum des Originals. Die Form bleibt erhalten, mit dem Faktor $1/T$ und an jedem Vielfachen der Abtastrate wiederholt; die Kopien heißen Spiegelspektren.
::::

::::lernkarten
:::karte zusammenhang Gleiche Abtastwerte
Warum haben zwei Schwingungen, deren Frequenzen sich um ein Vielfaches $k/T$ der Abtastrate unterscheiden, dieselben Abtastwerte?
---
Zu den Zeiten $nT$ gilt $\mathrm{e}^{\mathrm{j}2\pi(f_0+k/T)nT}=\mathrm{e}^{\mathrm{j}2\pi f_0nT}\cdot\mathrm{e}^{\mathrm{j}2\pi kn}$. Weil $kn$ ganzzahlig ist, ist der zweite Faktor 1: Der schnellere Zeiger hat zwischen zwei Abtastpunkten nur ganze Umdrehungen mehr gemacht.
--- falsch
Weil die schnellere Schwingung zwischen zwei Abtastpunkten genau eine halbe Umdrehung mehr macht. Ihr Zeiger steht deshalb an jedem Abtastpunkt spiegelbildlich, und die Realteile stimmen überein.
--- falsch
Sie haben nur ungefähr dieselben Abtastwerte. Der Unterschied wird mit wachsendem $k$ immer kleiner, weil schnelle Schwingungen zwischen den Abtastpunkten ihre Energie verlieren.
--- falsch
Zu den Zeiten $nT$ gilt $\mathrm{e}^{\mathrm{j}2\pi(f_0+k/T)nT}=\mathrm{e}^{\mathrm{j}2\pi f_0nT}+\mathrm{e}^{\mathrm{j}2\pi kn}$. Der zweite Summand ist bei ganzzahligem $kn$ null, deshalb bleibt nur die langsamere Schwingung übrig.
:::
:::karte zusammenhang Periodisches Spektrum
Warum muss das Spektrum der Abtastwerte periodisch mit der Abtastrate $1/T$ sein?
---
Schwingungen bei $f_0$ und bei $f_0+k/T$ haben dieselben Abtastwerte, die Abtastwerte können sie also nicht unterscheiden. Deshalb muss ihr Spektrum bei $f_0$ und bei $f_0+k/T$ gleich aussehen, für jedes $f_0$ und jedes ganze $k$.
--- falsch
Weil das Original schon periodisch ist. Jedes Signal, das man abtastet, wiederholt sich in der Zeit, und das Abtasten macht diese Periodizität im Spektrum lediglich sichtbar.
--- falsch
Weil der Abtaster die hohen Frequenzen abschneidet. Das Spektrum endet bei $1/T$ und wird dann nach außen hin fortgesetzt, damit es auf der ganzen Frequenzachse definiert bleibt.
--- falsch
Weil das Abtasten die Frequenzen des Signals mit $1/T$ multipliziert. Jede Frequenz $f_0$ wird so auf $f_0/T$ abgebildet, und diese Bilder wiederholen sich im Abstand der Abtastrate, sobald sie die halbe Abtastrate überschreiten.
:::
:::karte formel Spektrum des ideal abgetasteten Signals
Wie hängt das Spektrum $S_\mathrm a(f)$ des ideal abgetasteten Signals mit dem Spektrum $S(f)$ des Originals zusammen?
---
$S_\mathrm a(f)=\frac1T\sum_{k=-\infty}^{\infty}S\Bigl(f-\frac kT\Bigr)$ für $T>0$: Das Spektrum des Originals erscheint in unveränderter Form, mit dem Faktor $1/T$, an jedem Vielfachen der Abtastrate $1/T$ wiederholt.
--- falsch
$S_\mathrm a(f)=T\sum_{k=-\infty}^{\infty}S(f-kT)$: Das Spektrum des Originals erscheint mit dem Faktor $T$ an jedem Vielfachen des Abtastintervalls $T$ wiederholt, in unveränderter Form und Breite.
--- falsch
$S_\mathrm a(f)=\frac1T\sum_{k=-\infty}^{\infty}S\bigl(\frac kT\bigr)\,\delta\bigl(f-\frac kT\bigr)$: Das Spektrum des Originals wird an den Vielfachen der Abtastrate abgetastet, dazwischen ist es null.
--- falsch
$S_\mathrm a(f)=\frac1T\,S(f)$ für $|f|<\frac{1}{2T}$ und null sonst: Das Abtasten schneidet alle Frequenzen oberhalb der halben Abtastrate ab und schwächt den Rest mit $1/T$.
:::
:::karte begriff Spiegelspektren
Was sind die Spiegelspektren im Spektrum eines ideal abgetasteten Signals?
---
Die Kopien des Originalspektrums $S(f)$, die das Abtasten an jedem Vielfachen $k/T$ der Abtastrate erzeugt. Sie haben dieselbe Form wie das Original und tragen den Faktor $1/T$.
--- falsch
Die an der Frequenz null gespiegelten Anteile $S(-f)$ des Originals. Sie entstehen nur bei komplexen Signalen und fehlen bei reellen Signalen, deren Spektrum symmetrisch ist.
--- falsch
Störanteile, die ein realer Abtaster durch das Schalten erzeugt. Sie fehlen beim idealen Abtaster, weil dessen Dirac-Impulse unendlich kurz sind und keine Frequenzen hinzufügen.
--- falsch
Die Kopien des Originalspektrums bei den Vielfachen der Abtastrate, jedoch jede mit kleinerem Faktor, je weiter sie von $f=0$ entfernt ist. Bei großem $k$ verschwinden sie deshalb praktisch.
:::
:::karte herleitung Spektrum des abgetasteten Signals
Wie folgt aus $s_\mathrm a(t)=s(t)\sum_n\delta(t-nT)$, dass $S_\mathrm a(f)=\frac1T\sum_kS\bigl(f-\frac kT\bigr)$ ist?
---
Abtasten ist eine Multiplikation des Signals mit dem Dirac-Kamm; im Spektrum wird daraus eine Faltung, weil Multiplikation im Zeitbereich Faltung im Frequenzbereich ist ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).
---
Das Spektrum des Dirac-Kamms im Abstand $T$ ist wieder ein Kamm, $\frac1T\sum_k\delta\bigl(f-\frac kT\bigr)$, weil ein periodisches Signal nur Linien bei den Vielfachen von $1/T$ hat.
---
Man faltet $S(f)$ mit jedem Impuls dieses Kamms einzeln, weil die Faltung linear ist; die Faltung mit einem um $k/T$ verschobenen Dirac-Impuls verschiebt $S(f)$ um $k/T$.
---
Die Summe aller Verschiebungen ergibt $\frac1T\sum_kS\bigl(f-\frac kT\bigr)$, weil jeder Impuls eine Kopie liefert und den Faktor $1/T$ des Kamms mitbringt.
:::
:::karte zusammenhang Spektrum enthält alle Kopien
Woran liegt es, dass das Spektrum des abgetasteten Signals Kopien bei jedem Vielfachen von $1/T$ enthält, obwohl das Signal zwischen den Abtastpunkten einfach fehlt?
---
Gerade daran: Zwischen den Abtastpunkten ist das abgetastete Signal null. Jede Schwingung mit denselben Werten an allen Punkten $nT$ beschreibt es gleich gut. Das Spektrum kann sich nicht entscheiden und enthält alle: das Original und seine Kopien.
--- falsch
Die Kopien entstehen durch Rauschen, das beim Abtasten hinzukommt. Ein realer Abtaster misst nie exakt, und die Messfehler verteilen sich gleichmäßig auf die Vielfachen der Abtastrate, wo sie als Kopien erscheinen.
--- falsch
Das Spektrum ergänzt die fehlenden Zwischenwerte durch Interpolation. Jede Kopie entspricht einer anderen Art, die Lücken zwischen den Abtastpunkten mit Geraden oder mit Kurven zu füllen.
--- falsch
Die Kopien gehören zu den Sprüngen, mit denen das Signal an den Abtastpunkten ein- und ausgeschaltet wird. Sie verschwinden, sobald man die Abtastrate über die doppelte höchste Signalfrequenz erhöht, weil die Sprünge dann klein genug werden.
:::
:::karte zusammenhang Überlappende Kopien
Was passiert mit den Kopien im Spektrum, wenn man ein Signal mit einem Spektrum bis 300 Hz statt mit 1 kHz nur mit 500 Hz abtastet?
---
Die Kopien liegen nur noch 500 Hz auseinander, jede reicht aber 300 Hz zu beiden Seiten. Sie überlappen sich deshalb, und ihre Summe hat nicht mehr die Form des Originals.
--- falsch
Die Kopien rücken auf 500 Hz zusammen, bleiben aber getrennt, weil jede nur 300 Hz breit ist. Das Original lässt sich deshalb weiterhin mit einem Tiefpass ausschneiden.
--- falsch
Die Kopien werden schmaler, sodass jede nur noch bis 150 Hz reicht. Sie liegen dann wie vorher getrennt, nur die hohen Frequenzen des Originals gehen dabei verloren.
--- falsch
Die Kopien verschwinden ganz, weil 500 Hz unter der doppelten Signalfrequenz liegen. Übrig bleibt nur das Original mit dem Faktor $1/T$, das jedoch verzerrt ist.
:::
::::
