---
title: Stufe 7: Der ideale Bandpass und sein äquivalenter Tiefpass
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3250800
summary: Ein Bandpass lässt ein Band um die Mittenfrequenz f 0 durch.
tags: äquivalente Tiefpass, symmetrisch
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Ein Bandpass lässt ein Band um die Mittenfrequenz $f_0$ durch. Diese Stufe zeigt, dass man ihn vollständig durch einen Tiefpass und die Frequenz $f_0$ beschreiben kann.
:::

**Idealer Bandpass.** Zwei Rechtecke der Breite $\Delta f$ bei $\pm f_0$ ($f_0>\Delta f/2$):

<span class="anker" id="gl-7-1"></span>
$$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]\;\bullet\!\!-\!\!\circ\;h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\cdot2\cos(2\pi f_0t). \tag{7.1}$$

Die Impulsantwort ist eine Schwingung mit $f_0$, deren Hüllkurve die Impulsantwort eines Tiefpasses der Bandbreite $\Delta f/2$ ist. Die Modulationsregel aus [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html) erklärt es: Ein Tiefpass, dessen Spektrum nach $\pm f_0$ verschoben wird.

**Äquivalenter Tiefpass.** Bei reeller Impulsantwort ist $H(-f)=H^*(f)$, die negative Hälfte enthält nichts Neues. Man behält nur die positiven Frequenzen, verdoppelt sie und schiebt sie um eine Trägerfrequenz $f_0$ nach links. Das Ergebnis ist der __äquivalente Tiefpass__ $H_T(f)$:

<span class="anker" id="gl-7-2"></span>
$$H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0),\qquad H_T(f)=0\ \text{für}\ f\le-f_0. \tag{7.2}$$

$H_T$ muss nicht symmetrisch um $f=0$ sein, seine Impulsantwort $h_T(t)$ kann also komplex sein. Gibt es ein $f_0$, für das $H_T(-f)=H_T^*(f)$ gilt (und $h_T$ damit reell ist), heißt der Bandpass __symmetrisch__. Beim idealen Bandpass mit $f_0$ in der Mitte ist $H_T(f)=2\operatorname{rect}(f/\Delta f)$ und $h_T(t)=2\Delta f\operatorname{si}(\pi\Delta f\,t)$, reell und gerade. Das ist ein Sonderfall: Auch symmetrische Bandpässe haben in der Regel einen Imaginärteil im Spektrum.

:::aufgabe Aufgabe 7 ★★ Äquivalenter Tiefpass mit anderem Bezug
<span class="anker" id="aufg-7"></span>

Idealer Bandpass von 9 bis 11 Hz.

<ol class="al">

<li>

Bestimme $H_T$ und $h_T$ für $f_0=10$ Hz.

</li>

<li>

Bestimme $H_T$ und $h_T$ für $f_0=9$ Hz. Warum ist $h_T$ jetzt komplex? Beschreiben beide denselben Bandpass?

</li>

</ol>

:::loesung
(a) $f_0=10$ Hz: Das Band liegt nach dem Verschieben symmetrisch von $-1$ bis $1$ Hz. $H_T=2\operatorname{rect}(f/2)$, $h_T=4\operatorname{si}(2\pi t)$, reell.

(b) $f_0=9$ Hz: Das Band liegt von 0 bis 2 Hz. $H_T=2\operatorname{rect}\bigl(\frac{f-1}{2}\bigr)$, $h_T=4\operatorname{si}(2\pi t)\,\mathrm{e}^{\mathrm{j}2\pi t}$. Komplex, weil $H_T$ nicht symmetrisch um $f=0$ ist. Beide beschreiben denselben Bandpass: $\operatorname{Re}\{4\operatorname{si}(2\pi t)\mathrm{e}^{\mathrm{j}2\pi t}\mathrm{e}^{\mathrm{j}2\pi9t}\}=4\operatorname{si}(2\pi t)\cos(2\pi\cdot10t)$, dasselbe wie in (a) und wie [(7.1)](#gl-7-1).
:::
:::

::::formelsammlung
**Idealer Bandpass**

$$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]\;\bullet\!\!-\!\!\circ\;h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\cdot2\cos(2\pi f_0t)$$

Zwei Rechtecke der Breite $\Delta f$ bei $\pm f_0$, $f_0>\Delta f/2$. Nach der Modulationsregel ein Tiefpass der Bandbreite $\Delta f/2$, dessen Spektrum nach $\pm f_0$ verschoben ist.

**Äquivalenter Tiefpass**

$$H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0),\qquad H_T(f)=0\ \text{für}\ f\le-f_0$$

Bei reeller Impulsantwort ($H(-f)=H^*(f)$): positive Frequenzen behalten, verdoppeln und um $f_0$ nach links schieben. $h_T(t)$ kann komplex sein.

**Symmetrischer Bandpass**

$$H_T(-f)=H_T^*(f)$$

Gibt es ein $f_0$, für das dies gilt, heißt der Bandpass symmetrisch; dann ist $h_T$ reell.

**Äquivalenter Tiefpass des idealen Bandpasses**

$$H_T(f)=2\operatorname{rect}(f/\Delta f),\qquad h_T(t)=2\Delta f\operatorname{si}(\pi\Delta f\,t)$$

Mit $f_0$ in der Mitte des Bandes; reell und gerade. Ein anderer Bezug, etwa $f_0$ am Bandrand, gibt eine komplexe $h_T$, beschreibt aber denselben Bandpass.
::::

::::lernkarten
:::karte formel Idealer Bandpass
Wie lauten Frequenzgang und Impulsantwort des idealen Bandpasses mit der Mittenfrequenz $f_0$ und der Bandbreite $\Delta f$?
---
$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]$ und $h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\cdot2\cos(2\pi f_0t)$ für $f_0>\Delta f/2$: zwei Rechtecke bei $\pm f_0$, im Zeitbereich eine Schwingung mit si-förmiger Hüllkurve.
--- falsch
$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)\cdot\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]$ und $h(t)=2\cos(2\pi f_0t)$: Das Produkt mit den Dirac-Impulsen greift zwei Linien bei $\pm f_0$ heraus, die Impulsantwort ist deshalb ein reiner Kosinus.
--- falsch
$H(f)=\operatorname{rect}\Bigl(\frac{f-f_0}{\Delta f}\Bigr)$ und $h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)\,\mathrm{e}^{\mathrm{j}2\pi f_0t}$: Ein einziges Rechteck bei $+f_0$ genügt, weil die negativen Frequenzen bei einer reellen Impulsantwort keine Rolle spielen.
--- falsch
$H(f)=\operatorname{rect}\Bigl(\frac{f}{\Delta f}\Bigr)*\bigl[\delta(f+f_0)+\delta(f-f_0)\bigr]$ und $h(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)+2\cos(2\pi f_0t)$: Die Impulsantwort ist die Summe aus einer si-Funktion und einem Kosinus der Mittenfrequenz.
:::
:::karte zusammenhang Bandpass als verschobener Tiefpass
Warum ist die Impulsantwort des idealen Bandpasses eine Schwingung mit $f_0$, deren Hüllkurve die Form einer Tiefpass-Impulsantwort hat?
---
Nach der Modulationsregel ist der ideale Bandpass ein Tiefpass der Bandbreite $\Delta f/2$, dessen Spektrum nach $\pm f_0$ verschoben wird. Im Zeitbereich wird die Tiefpass-Impulsantwort deshalb mit $2\cos(2\pi f_0t)$ multipliziert.
--- falsch
Nach dem Faltungssatz ist der ideale Bandpass ein Tiefpass in Reihe mit einem Schwingkreis: Die Tiefpass-Impulsantwort wird mit dem Kosinus $2\cos(2\pi f_0t)$ gefaltet, und das ergibt die Schwingung.
--- falsch
Weil der Bandpass bei $f_0$ schwingt wie ein Schwingkreis: Die Hüllkurve ist die abklingende Exponentialfunktion seiner Dämpfung, die man nur der Einfachheit halber näherungsweise als si-Funktion zeichnet.
--- falsch
Nach der Modulationsregel ist der Bandpass ein Tiefpass, dessen Spektrum nach $\pm f_0$ verschoben ist. Im Zeitbereich addiert man deshalb zur Tiefpass-Impulsantwort der Bandbreite $\Delta f/2$ einen Kosinus der Frequenz $f_0$.
:::
:::karte begriff äquivalenter Tiefpass
Was ist der äquivalente Tiefpass $H_T(f)$ eines Bandpasses mit reeller Impulsantwort, und wie gewinnt man ihn?
---
Man behält von $H(f)$ nur die positiven Frequenzen, verdoppelt sie und schiebt sie um eine Trägerfrequenz $f_0$ nach links. Die negative Hälfte enthält nichts Neues, weil bei reeller Impulsantwort $H(-f)=H^*(f)$ gilt.
--- falsch
Man behält von $H(f)$ nur die negativen Frequenzen und schiebt sie um $f_0$ nach rechts; die positiven sind überflüssig, weil sie beim Schieben über den Ursprung hinaus doppelt gezählt würden.
--- falsch
Man schiebt den ganzen Frequenzgang $H(f)$ samt beider Hälften um $f_0$ nach links. Die Hälfte bei $-f_0$ landet dabei bei $-2f_0$ und bleibt als zweites, gleichberechtigtes Band im äquivalenten Tiefpass erhalten.
--- falsch
Man ersetzt den Bandpass durch einen idealen Tiefpass mit der Grenzfrequenz $f_0$ und derselben Bandbreite. Die Lage des Bandes geht dabei verloren, weil für das Signal nur seine Breite zählt.
:::
:::karte formel Bandpass aus dem äquivalenten Tiefpass
Wie setzt man den Frequenzgang $H(f)$ eines Bandpasses aus seinem äquivalenten Tiefpass $H_T(f)$ zusammen, und welche Bedingung erfüllt $H_T$?
---
$H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0)$ mit $H_T(f)=0$ für $f\le-f_0$. Der erste Summand ist das nach $+f_0$ verschobene Band, der zweite sein konjugiertes Spiegelbild bei $-f_0$.
--- falsch
$H(f)=H_T(f-f_0)+H_T(-f-f_0)$ mit $H_T(f)=0$ für $f<0$: Beide Hälften werden ohne Faktor und ohne Konjugation übernommen, weil der äquivalente Tiefpass stets reell ist.
--- falsch
$H(f)=\tfrac12H_T(f-f_0)+\tfrac12H_T^*(-f-f_0)$ mit $H_T(f)=0$ für $f\le-f_0$. Der zweite Summand ist ein zweites, unabhängiges Band, das man frei wählen kann, um den Bandpass unsymmetrisch zu machen.
--- falsch
$H(f)=\tfrac12H_T(f+f_0)+\tfrac12H_T^*(f-f_0)$ ohne weitere Bedingung: Der äquivalente Tiefpass wird einmal nach links und einmal nach rechts verschoben, und jede Form von $H_T$ ist erlaubt.
:::
:::karte begriff symmetrisch
Wann heißt ein Bandpass symmetrisch, und was folgt daraus für die Impulsantwort seines äquivalenten Tiefpasses?
---
Ein Bandpass heißt symmetrisch, wenn es ein $f_0$ gibt, für das $H_T(-f)=H_T^*(f)$ gilt. Dann ist die Impulsantwort $h_T(t)$ des äquivalenten Tiefpasses reell.
--- falsch
Ein Bandpass heißt symmetrisch, wenn sein Frequenzgang gerade ist, $H(-f)=H(f)$. Das gilt für jeden Bandpass mit reeller Impulsantwort, deshalb ist $h_T(t)$ stets reell.
--- falsch
Ein Bandpass heißt symmetrisch, wenn sein Durchlassbereich genau in der Mitte zwischen 0 und der höchsten Frequenz liegt. Dann ist $h_T(t)$ rein imaginär, weil das Band keinen Gleichanteil hat.
--- falsch
Ein Bandpass heißt symmetrisch, wenn $H_T(f)$ rein reell und gerade ist. Nur dann ist $h_T(t)$ reell; jeder Imaginärteil im Spektrum macht den Bandpass unsymmetrisch.
:::
:::karte formel Äquivalenter Tiefpass des idealen Bandpasses
Welchen äquivalenten Tiefpass hat der ideale Bandpass, wenn man $f_0$ in die Mitte des Bandes legt?
---
$H_T(f)=2\operatorname{rect}(f/\Delta f)$ und $h_T(t)=2\Delta f\operatorname{si}(\pi\Delta f\,t)$, reell und gerade. Das ist ein Sonderfall: Auch symmetrische Bandpässe haben in der Regel einen Imaginärteil im Spektrum.
--- falsch
$H_T(f)=\operatorname{rect}(f/\Delta f)$ und $h_T(t)=\Delta f\operatorname{si}(\pi\Delta f\,t)$, reell und gerade: Beim Verschieben bleibt die Höhe des Bandes erhalten, ein Faktor 2 entsteht dabei nicht.
--- falsch
$H_T(f)=2\operatorname{rect}(f/\Delta f)$ und $h_T(t)=2\Delta f\operatorname{si}(\pi\Delta f\,t)\cos(2\pi f_0t)$: Der äquivalente Tiefpass enthält den Träger noch, weil er dieselbe Impulsantwort hat wie der Bandpass.
--- falsch
$H_T(f)=2\operatorname{rect}(f/\Delta f)$ mit einer komplexen Impulsantwort $h_T(t)$: Weil der Bandpass zwei Rechtecke hat, bleibt nach dem Verschieben stets ein Imaginärteil übrig, auch bei $f_0$ in der Mitte.
:::
:::karte zusammenhang Anderer Bezug, derselbe Bandpass
Was ändert sich am äquivalenten Tiefpass des idealen Bandpasses von 9 bis 11 Hz, wenn man $f_0=9$ Hz statt der Mitte 10 Hz wählt?
---
Das Band liegt dann von 0 bis 2 Hz, $H_T$ ist nicht mehr symmetrisch um $f=0$, und $h_T=4\operatorname{si}(2\pi t)\,\mathrm{e}^{\mathrm{j}2\pi t}$ wird komplex. Beide Wahlen beschreiben trotzdem denselben Bandpass.
--- falsch
Das Band liegt dann von 0 bis 2 Hz, $H_T$ bleibt symmetrisch um $f=0$, und $h_T$ bleibt reell; der Bezug schneidet aber die halbe Breite ab, sodass nur noch ein Bandpass von 9 bis 10 Hz beschrieben wird.
--- falsch
Nichts: Der äquivalente Tiefpass hängt nur von der Bandbreite ab, nicht von der Wahl von $f_0$; $h_T=4\operatorname{si}(2\pi t)$ bleibt reell, weil der Bandpass selbst unverändert bleibt.
--- falsch
Das Band liegt dann von 0 bis 2 Hz, und $h_T$ wird komplex. Damit beschreibt $H_T$ einen anderen Bandpass mit komplexer Impulsantwort, der sich nicht mehr als reales System bauen lässt.
:::
::::
