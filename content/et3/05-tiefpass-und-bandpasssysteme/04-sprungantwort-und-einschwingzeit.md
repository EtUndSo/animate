---
title: Stufe 3: Sprungantwort und Einschwingzeit
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3250400
summary: Wie reagiert der ideale Tiefpass auf einen Sprung?
tags: Integralsinus, Einschwingzeit
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Wie reagiert der ideale Tiefpass auf einen Sprung? Wie schnell steigt er, und wie weit schießt er über?
:::

Die Sprungantwort ist das laufende Integral der Impulsantwort ([Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). Mit dem __Integralsinus__

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Si}(x)=\int_0^x\operatorname{si}(\xi)\,\mathrm{d}\xi,\qquad\operatorname{Si}(-x)=-\operatorname{Si}(x),\qquad\operatorname{Si}(\infty)=\frac\pi2 \tag{3.1}$$

ergibt sich

<span class="anker" id="gl-3-2"></span>
$$h_\varepsilon(t)=\int_{-\infty}^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\,\mathrm{d}\tau=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt). \tag{3.2}$$

:::herleitung Sprungantwort
Das Integral bis $t$ teilt man bei 0. Der Teil von $-\infty$ bis 0 ist die halbe Fläche von $h$, also $\frac12H(0)=\frac12$, weil $h$ gerade ist. Für den Rest substituiert man $\xi=2\pi f_\mathrm g\tau$, $\mathrm{d}\tau=\mathrm{d}\xi/(2\pi f_\mathrm g)$: $\int_0^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\mathrm{d}\tau=\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$. Den Wert $\operatorname{Si}(\infty)=\frac\pi2$ liefert der Flächensatz: $\int_{-\infty}^\infty\operatorname{si}(\pi u)\mathrm{d} u=1$, also $\int_0^\infty\operatorname{si}(\xi)\mathrm{d}\xi=\frac\pi2$.
:::

⁠**So liest man das:** Bei $t=0$ ist die Antwort genau $\frac12$, sie beginnt schon vorher (nicht kausal) und strebt gegen 1. Die __Einschwingzeit__ $t_e$ definiert man als Anstiegszeit einer Rampe mit der größten Steigung der Sprungantwort. Die größte Steigung ist $h(0)=2f_\mathrm g$, also

<span class="anker" id="gl-3-3"></span>
$$t_e=\frac{h_\varepsilon(\infty)}{\max\dot h_\varepsilon}=\frac{1}{2f_\mathrm g}. \tag{3.3}$$

Die Sprungantwort schießt um $8{,}95\,\%$ über (bei $t=\frac{1}{2f_\mathrm g}$). Das ist das Gibbs-Phänomen aus [Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): Ein größeres $f_\mathrm g$ verkürzt die Einschwingzeit, das Überschwingen bleibt (Abb. [1](#abb-1)).

:::abbildung et3/k5sprung 1
Sprungantwort des idealen Tiefpasses für $f_\mathrm g=1$ Hz und 2 Hz. Gestrichelt die Rampe mit der größten Steigung: Ihre Anstiegszeit ist $t_e=1/(2f_\mathrm g)=0{,}5$ s. Beide Kurven schießen gleich weit über, auf 1,0895.
:::

:::frage Ein Tiefpass mit mehr Bandbreite ist doch „besser“. Warum wird das Überschwingen dann nicht kleiner?
Weil es von der *Form* des Frequenzgangs kommt, nicht von seiner Breite. Das Überschwingen entsteht an der senkrechten Kante bei $f_\mathrm g$: Alle Frequenzen bis dorthin kommen voll an, alle darüber gar nicht. Verschiebt man die Kante, bleibt sie senkrecht, und die Sprungantwort wird nur zeitlich gestaucht. Kleiner wird das Überschwingen erst, wenn die Kante weich wird (Stufe [5](echomethode-und-pulsformfilter.html#stufe-5)).
:::

:::aufgabe Aufgabe 3 ★★ Integralsinus
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Zeige $h_\varepsilon(0)=\frac12$ und $h_\varepsilon(\infty)=1$ mit [(3.1)](#gl-3-1).

</li>

<li>

Wo liegt das Maximum der Sprungantwort? Tipp: Die Ableitung der Sprungantwort ist die Impulsantwort.

</li>

</ol>

:::loesung
(a) $h_\varepsilon(0)=\frac12+\frac1\pi\operatorname{Si}(0)=\frac12$, $h_\varepsilon(\infty)=\frac12+\frac1\pi\cdot\frac\pi2=1$.

(b) Die Steigung der Sprungantwort ist $h(t)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gt)$. Sie wird zum ersten Mal bei $2\pi f_\mathrm gt=\pi$ null und wechselt dort von positiv zu negativ. Das Maximum liegt also bei $t=\frac{1}{2f_\mathrm g}$ und ist $\frac12+\frac{\operatorname{Si}(\pi)}{\pi}=\frac12+\frac{1{,}852}{\pi}=1{,}0895$.
:::
:::

::::formelsammlung
**Integralsinus**

$$\operatorname{Si}(x)=\int_0^x\operatorname{si}(\xi)\,\mathrm{d}\xi,\qquad\operatorname{Si}(-x)=-\operatorname{Si}(x),\qquad\operatorname{Si}(\infty)=\frac\pi2$$

Integral der si-Funktion; ungerade. Den Grenzwert liefert der Flächensatz.

**Sprungantwort des idealen Tiefpasses**

$$h_\varepsilon(t)=\int_{-\infty}^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\,\mathrm{d}\tau=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$$

Laufendes Integral der Impulsantwort. Bei $t=0$ genau $\frac12$, beginnt schon vorher (nicht kausal) und strebt gegen 1.

**Einschwingzeit**

$$t_e=\frac{h_\varepsilon(\infty)}{\max\dot h_\varepsilon}=\frac{1}{2f_\mathrm g}$$

Anstiegszeit einer Rampe mit der größten Steigung der Sprungantwort; diese ist $h(0)=2f_\mathrm g$.

**Maximum der Sprungantwort**

$$\frac12+\frac{\operatorname{Si}(\pi)}{\pi}=\frac12+\frac{1{,}852}{\pi}=1{,}0895$$

Bei $t=\frac{1}{2f_\mathrm g}$, wo die Impulsantwort zum ersten Mal null wird: 8,95 % Überschwingen (Gibbs-Phänomen), unabhängig von $f_\mathrm g$.
::::

::::lernkarten
:::karte begriff Integralsinus
Wie ist der Integralsinus definiert, den man für die Sprungantwort des idealen Tiefpasses braucht, und welche Eigenschaften hat er?
---
Der Integralsinus ist das Integral der si-Funktion von 0 bis $x$: $\operatorname{Si}(x)=\int_0^x\operatorname{si}(\xi)\,\mathrm{d}\xi$. Er ist ungerade, $\operatorname{Si}(-x)=-\operatorname{Si}(x)$, und strebt gegen $\operatorname{Si}(\infty)=\frac\pi2$.
--- falsch
Der Integralsinus ist das Integral der Sinusfunktion von 0 bis $x$, also $1-\cos x$. Er ist gerade, $\operatorname{Si}(-x)=\operatorname{Si}(x)$, und schwankt für große $x$ dauerhaft zwischen 0 und 2.
--- falsch
Der Integralsinus ist das Integral der si-Funktion von 0 bis $x$. Er ist gerade, $\operatorname{Si}(-x)=\operatorname{Si}(x)$, und wächst für große $x$ unbegrenzt, weil die Fläche unter der si-Funktion immer weiter zunimmt.
--- falsch
Der Integralsinus ist die Ableitung der si-Funktion nach ihrem Argument. Er ist ungerade, $\operatorname{Si}(-x)=-\operatorname{Si}(x)$, und strebt für große $x$ gegen 1, weil die si-Funktion dann flach wird.
:::
:::karte formel Sprungantwort des idealen Tiefpasses
Wie lautet die Sprungantwort des idealen Tiefpasses, ausgedrückt mit dem Integralsinus?
---
$h_\varepsilon(t)=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$: Sie ist das laufende Integral der Impulsantwort, hat bei $t=0$ genau den Wert $\frac12$, beginnt schon vorher und strebt gegen 1.
--- falsch
$h_\varepsilon(t)=\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$ für $t\ge0$: Sie beginnt bei $t=0$ mit dem Wert null, weil das System vorher nichts gesehen hat, und strebt gegen $\frac12$.
--- falsch
$h_\varepsilon(t)=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$: Sie ist die Ableitung der Impulsantwort, beginnt erst bei $t=0$ mit dem Wert $\frac12$ und strebt ohne Überschwingen gegen 1.
--- falsch
$h_\varepsilon(t)=1-\mathrm{e}^{-2\pi f_\mathrm gt}$ für $t\ge0$: Sie steigt wie beim RC-Glied exponentiell an, ist bei $t=0$ null und erreicht nach der Zeit $1/(2\pi f_\mathrm g)$ etwa 63 %.
:::
:::karte herleitung Sprungantwort
Wie folgt aus $h_\varepsilon(t)=\int_{-\infty}^t2f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)\,\mathrm{d}\tau$ die Form $\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$?
---
Man teilt das Integral bei 0, weil der Teil von $-\infty$ bis 0 für jedes $t$ derselbe ist.
---
Dieser Teil ist die halbe Fläche von $h$, also $\frac12H(0)=\frac12$, weil $h$ gerade ist.
---
Im Rest substituiert man $\xi=2\pi f_\mathrm g\tau$, $\mathrm{d}\tau=\mathrm{d}\xi/(2\pi f_\mathrm g)$, weil das Argument der si-Funktion dann einfach $\xi$ ist; es bleibt $\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$.
---
Den Grenzwert $\operatorname{Si}(\infty)=\frac\pi2$ liefert der Flächensatz, weil $\int_{-\infty}^\infty\operatorname{si}(\pi u)\mathrm{d} u=1$ ist; damit strebt die Sprungantwort gegen 1.
:::
:::karte zusammenhang Werte der Sprungantwort
Welche Werte hat die Sprungantwort $h_\varepsilon(t)=\frac12+\frac1\pi\operatorname{Si}(2\pi f_\mathrm gt)$ bei $t=0$ und für sehr große $t$, und warum?
---
$h_\varepsilon(0)=\frac12$, weil $\operatorname{Si}(0)=0$ ist: Die Hälfte der Fläche der geraden Impulsantwort liegt vor $t=0$. Für sehr große $t$ ist $h_\varepsilon(\infty)=\frac12+\frac1\pi\cdot\frac\pi2=1$, weil $\operatorname{Si}(\infty)=\frac\pi2$ ist.
--- falsch
$h_\varepsilon(0)=0$, weil die Antwort erst mit dem Sprung beginnt, und $h_\varepsilon(\infty)=1$, weil $\operatorname{Si}(\infty)=\pi$ ist und der Faktor $\frac1\pi$ diesen Wert genau auf 1 bringt.
--- falsch
$h_\varepsilon(0)=\frac12$, weil $\operatorname{Si}(0)=\frac\pi2$ ist, und $h_\varepsilon(\infty)=\frac12$, weil der Integralsinus für große Argumente wieder auf null zurückfällt und nur der konstante Anteil übrig bleibt.
--- falsch
$h_\varepsilon(0)=1$, weil die größte Steigung bei $t=0$ liegt, und $h_\varepsilon(\infty)=\frac12$, weil sich die Nebenschwingungen der si-Funktion im Mittel zur Hälfte aufheben.
:::
:::karte begriff Einschwingzeit
Wie ist die Einschwingzeit $t_e$ einer Sprungantwort definiert, und welchen Wert hat sie beim idealen Tiefpass?
---
Die Einschwingzeit ist die Anstiegszeit einer Rampe mit der größten Steigung der Sprungantwort: $t_e=\frac{h_\varepsilon(\infty)}{\max\dot h_\varepsilon}$. Beim idealen Tiefpass ist die größte Steigung $h(0)=2f_\mathrm g$, also $t_e=\frac{1}{2f_\mathrm g}$.
--- falsch
Die Einschwingzeit ist die Zeit, bis die Sprungantwort von 10 % auf 90 % ihres Endwerts gestiegen ist. Beim idealen Tiefpass ist sie unendlich, weil die Antwort schon lange vor $t=0$ beginnt und nie ganz zur Ruhe kommt.
--- falsch
Die Einschwingzeit ist die Zeit, nach der das Überschwingen der Sprungantwort vollständig abgeklungen ist. Beim idealen Tiefpass ist $t_e=\frac{1}{f_\mathrm g}$, weil die si-Funktion nach einer Periode der Grenzfrequenz verschwindet.
--- falsch
Die Einschwingzeit ist die Anstiegszeit einer Rampe mit der mittleren Steigung der Sprungantwort zwischen $t=0$ und ihrem Maximum. Beim idealen Tiefpass ist deshalb $t_e=\frac{1}{4f_\mathrm g}$.
:::
:::karte zusammenhang Überschwingen der Sprungantwort
Wie weit schießt die Sprungantwort des idealen Tiefpasses über, und wo liegt ihr Maximum?
---
Das Maximum liegt bei $t=\frac{1}{2f_\mathrm g}$, wo die Impulsantwort als Steigung zum ersten Mal null wird. Es ist $\frac12+\frac{\operatorname{Si}(\pi)}{\pi}=1{,}0895$, also 8,95 % über dem Endwert.
--- falsch
Das Maximum liegt bei $t=0$, wo die Steigung am größten ist; dort erreicht die Antwort 1,217, sie schießt also um 21,7 % über, genau so weit wie die Impulsantwort.
--- falsch
Das Maximum liegt bei $t=\frac{1}{f_\mathrm g}$, nach einer ganzen Periode der Grenzfrequenz; dort erreicht die Antwort 1,0895, danach fällt sie ohne weitere Schwingungen auf 1.
--- falsch
Die Sprungantwort schießt nicht über: Sie ist das Integral der Impulsantwort und steigt deshalb monoton von 0 auf 1, weil ein Integral über eine positive Fläche nie abnimmt.
:::
:::karte zusammenhang Mehr Bandbreite, gleiches Überschwingen
Warum wird das Überschwingen der Sprungantwort nicht kleiner, wenn man die Grenzfrequenz des idealen Tiefpasses erhöht?
---
Weil es von der Form des Frequenzgangs kommt, nicht von seiner Breite: Die Kante bei $f_\mathrm g$ bleibt senkrecht, die Sprungantwort wird nur zeitlich gestaucht. Kleiner wird das Überschwingen erst, wenn die Kante weich wird.
--- falsch
Weil das Überschwingen von der Höhe des Durchlassbereichs abhängt: Erst wenn man den Betrag im Durchlassbereich deutlich unter 1 senkt, sinkt auch das Überschwingen, ganz unabhängig davon, wie steil die Kante ist.
--- falsch
Es wird kleiner, nur sehr langsam: Mit jeder Verdopplung von $f_\mathrm g$ sinkt es um etwa ein Zehntel, weil mehr Frequenzen beteiligt sind und die Kante des Sprungs feiner nachbilden.
--- falsch
Weil die Grenzfrequenz nur die Höhe der Sprungantwort ändert: Ein größeres $f_\mathrm g$ macht den Endwert größer, das Überschwingen wächst im gleichen Verhältnis mit und bleibt deshalb prozentual gleich.
:::
::::
