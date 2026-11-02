---
title: Stufe 7: Der ideale Bandpass und sein äquivalenter Tiefpass
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
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

Die Impulsantwort ist eine Schwingung mit $f_0$, deren Hüllkurve die Impulsantwort eines Tiefpasses der Bandbreite $\Delta f/2$ ist. Die Modulationsregel aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html) erklärt es: Ein Tiefpass, dessen Spektrum nach $\pm f_0$ verschoben wird.

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
