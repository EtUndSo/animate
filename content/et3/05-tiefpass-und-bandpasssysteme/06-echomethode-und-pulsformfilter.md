---
title: Stufe 5: Echomethode und Pulsformfilter
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Tiefpass- und Bandpasssysteme
order: 3250600
summary: Wie entwirft man einen Tiefpass mit weniger Überschwingen?
tags: Echo, Cosine-Rolloff-Filter
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Wie entwirft man einen Tiefpass mit weniger Überschwingen? Man setzt die Impulsantwort aus verschobenen si-Funktionen zusammen und wählt deren Gewichte.
:::

**Echomethode.** Jede Impulsantwort eines Tiefpasses bis $f_\mathrm g=\frac{1}{2T}$ ist nach dem Abtasttheorem eine si-Reihe:

<span class="anker" id="gl-5-1"></span>
$$h(t)=\sum_nh(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$h(nT)=\int_{-f_\mathrm g}^{f_\mathrm g}H(f)\,\mathrm{e}^{\mathrm{j}2\pi nTf}\,\mathrm{d} f. \tag{5.2}$$

Jeder Abtastwert $h(nT)$ ist ein __Echo__: eine um $nT$ verschobene si-Funktion. Im Spektrum wird daraus eine Fourier-Reihe in $f$. Ist $h$ reell und gerade, ist $H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\cos(2\pi nTf)\bigr]$.

**Pulsformfilter.** Zur Hauptkomponente $\operatorname{si}(\pi t/T)$ kommen zwei Echos mit der Amplitude $a$ im Abstand $\pm T$. Bei $a=\frac12$ heben sich die Nebenschwingungen weitgehend auf, und das Spektrum bekommt eine kosinusförmige, weiche Flanke:

<span class="anker" id="gl-5-3"></span>
$$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t+T}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t-T}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]. \tag{5.3}$$

Das ist das __Cosine-Rolloff-Filter__. Sein Überschwingen ist 2,7 % statt 21,7 %, dafür ist die Hauptkeule doppelt so breit (erste Nullstelle bei $2T$ statt $T$). Abbildung [3](#abb-3) zeigt beide Impulsantworten auf gleiche Fläche normiert.

:::abbildung et3/k5pulsform 3
Impulsantworten des idealen Tiefpasses und des Pulsformfilters (beide mit der Fläche $T$). Das Pulsformfilter klingt viel schneller ab: Sein größtes Nebenmaximum ist 2,7 % des Hauptmaximums statt 21,7 %.
:::

**Transversalfilter.** Eine Summe verzögerter, gewichteter Kopien baut man mit einer Kette von Verzögerungsgliedern, deren Abgriffe gewichtet und addiert werden. Damit kein Glied in die Zukunft greifen muss, verzögert man alles gemeinsam. Das ist dieselbe Struktur wie ein FIR-Filter ([Teil 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)).

:::aufgabe Aufgabe 5 ★★ Das Cosine-Rolloff-Filter
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Leite $H(f)$ in [(5.3)](#gl-5-3) aus [(5.1)](#gl-5-1) her.

</li>

<li>

Welchen Wert hat $H$ bei $f=0$ und bei $f=f_\mathrm g=\frac{1}{2T}$? Warum ist die Flanke dort glatt?

</li>

</ol>

:::loesung
(a) Bei $t=mT$ ist $\operatorname{si}(\pi(t\pm T)/T)$ nur für $m=\mp1$ gleich 1, sonst null. Also $h(0)=1$, $h(\pm T)=\frac12$, alle anderen $h(nT)=0$. Nach [(5.1)](#gl-5-1): $H=T\operatorname{rect}(Tf)\bigl[1+\frac12\mathrm{e}^{\mathrm{j}2\pi Tf}+\frac12\mathrm{e}^{-\mathrm{j}2\pi Tf}\bigr]=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]$.

(b) $H(0)=2T$, $H(\frac{1}{2T})=T(1+\cos\pi)=0$. Auch die Steigung $-2\pi T^2\sin(2\pi Tf)$ ist bei $f=\frac{1}{2T}$ null. Der Frequenzgang geht ohne Sprung und ohne Knick auf null. Je glatter das Spektrum, desto schneller klingt die Impulsantwort ab ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).
:::
:::
