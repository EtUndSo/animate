---
title: Stufe 5: Echomethode und Pulsformfilter
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
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

**Transversalfilter.** Eine Summe verzögerter, gewichteter Kopien baut man mit einer Kette von Verzögerungsgliedern, deren Abgriffe gewichtet und addiert werden. Damit kein Glied in die Zukunft greifen muss, verzögert man alles gemeinsam. Das ist dieselbe Struktur wie ein FIR-Filter ([Kapitel 4](/wissen/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)).

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

(b) $H(0)=2T$, $H(\frac{1}{2T})=T(1+\cos\pi)=0$. Auch die Steigung $-2\pi T^2\sin(2\pi Tf)$ ist bei $f=\frac{1}{2T}$ null. Der Frequenzgang geht ohne Sprung und ohne Knick auf null. Je glatter das Spektrum, desto schneller klingt die Impulsantwort ab ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).
:::
:::

::::formelsammlung
**Echomethode**

$$h(t)=\sum_nh(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}$$

Für jeden Tiefpass bis $f_\mathrm g=\frac{1}{2T}$ (Abtasttheorem). Jeder Abtastwert $h(nT)$ gewichtet ein Echo, eine um $nT$ verschobene si-Funktion; im Spektrum entsteht eine Fourier-Reihe in $f$.

**Gewichte der Echos**

$$h(nT)=\int_{-f_\mathrm g}^{f_\mathrm g}H(f)\,\mathrm{e}^{\mathrm{j}2\pi nTf}\,\mathrm{d} f$$

Aus dem gewünschten Frequenzgang im Durchlassbereich.

**Reelle, gerade Impulsantwort**

$$H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\cos(2\pi nTf)\bigr]$$

Je zwei gleiche Echos links und rechts von $t=0$ fassen sich zu einem Kosinus zusammen; $H$ ist dann reell.

**Cosine-Rolloff-Filter**

$$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t+T}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t-T}{T}\Bigr)\;\circ\!\!-\!\!\bullet\;H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]$$

Pulsformfilter: Hauptkomponente und zwei Echos der Amplitude $\frac12$ im Abstand $\pm T$. Kosinusförmige, weiche Flanke, $H$ und seine Steigung sind bei $f=\frac{1}{2T}$ null. Überschwingen 2,7 % statt 21,7 %, dafür erste Nullstelle bei $2T$ statt $T$.
::::

::::lernkarten
:::karte formel Echomethode
Wie stellt die Echomethode die Impulsantwort eines Tiefpasses bis $f_\mathrm g=\frac{1}{2T}$ dar, und welcher Frequenzgang gehört dazu?
---
Als si-Reihe der Abtastwerte: $h(t)=\sum_nh(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)$ mit $H(f)=T\operatorname{rect}(Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}$. Das folgt aus dem Abtasttheorem; im Spektrum entsteht eine Fourier-Reihe in $f$.
--- falsch
Als Summe von Rechteckimpulsen: $h(t)=\sum_nh(nT)\operatorname{rect}\Bigl(\frac{t-nT}{T}\Bigr)$ mit $H(f)=T\operatorname{si}(\pi Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}$; jeder Abtastwert wird für die Dauer $T$ festgehalten.
--- falsch
Als si-Reihe der Abtastwerte, die aber nur für kausale Systeme gilt: $h(t)=\sum_{n\ge0}h(nT)\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)$; der Frequenzgang ist dann eine Treppe aus Rechtecken der Breite $\frac1T$.
--- falsch
Als Summe von Dirac-Impulsen: $h(t)=\sum_nh(nT)\,\delta(t-nT)$ mit $H(f)=\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}$; der Frequenzgang ist auf $|f|\le f_\mathrm g$ begrenzt, weil nur Abtastwerte vorkommen.
:::
:::karte begriff Echo
Was bezeichnet man bei der Echomethode als Echo, und welche Rolle spielt der Abtastwert $h(nT)$ dabei?
---
Ein Echo ist eine um $nT$ verschobene si-Funktion in der si-Reihe der Impulsantwort. Ihr Gewicht ist der Abtastwert $h(nT)$; im Spektrum liefert jedes Echo einen Summanden $h(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}$ der Fourier-Reihe.
--- falsch
Ein Echo ist eine Nebenschwingung der si-Funktion, also eines ihrer Nebenmaxima. Der Abtastwert $h(nT)$ gibt die Höhe des $n$-ten Nebenmaximums an, das man für weniger Überschwingen verkleinert.
--- falsch
Ein Echo ist eine um $nT$ verschobene Kopie des Eingangssignals am Ausgang. Ihr Gewicht $h(nT)$ ist stets kleiner als das der Hauptkomponente, weil jede Wiederholung im System schwächer wird als die vorige.
--- falsch
Ein Echo ist ein Anteil der Impulsantwort jenseits der Grenzfrequenz, der bei $f=n/T$ liegt. Der Abtastwert $h(nT)$ gibt an, wie stark dieser Anteil durch das Rechteck $T\operatorname{rect}(Tf)$ gedämpft wird.
:::
:::karte formel Reelle, gerade Impulsantwort
Welche Form hat der Frequenzgang aus der Echomethode, wenn die Impulsantwort $h$ reell und gerade ist?
---
$H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\cos(2\pi nTf)\bigr]$: Weil die Echos links und rechts von $t=0$ gleich sind, fassen sich je zwei zu einem Kosinus zusammen, und der Frequenzgang wird reell.
--- falsch
$H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\sin(2\pi nTf)\bigr]$: Weil die Echos links und rechts von $t=0$ gleich sind, fassen sich je zwei zu einem Sinus zusammen, und der Frequenzgang wird ungerade.
--- falsch
$H(f)=T\operatorname{rect}(Tf)\sum_{n\ge0}h(nT)\cos(2\pi nTf)$: Weil $h$ gerade ist, braucht man nur die Echos mit $n\ge0$; die anderen tragen nichts bei, weil sie sich gegenseitig aufheben.
--- falsch
$H(f)=T\operatorname{rect}(Tf)\bigl[h(0)+2\sum_{n\ge1}h(nT)\cos(2\pi nTf)\bigr]$: Weil $h$ gerade ist, ist der Frequenzgang rein imaginär, und die Echos verschieben nur die Phase, nicht den Betrag.
:::
:::karte begriff Cosine-Rolloff-Filter
Was ist das Cosine-Rolloff-Filter, das man mit der Echomethode aus drei si-Funktionen zusammensetzt?
---
Ein Pulsformfilter aus der Hauptkomponente $\operatorname{si}(\pi t/T)$ und zwei Echos der Amplitude $\frac12$ im Abstand $\pm T$. Dabei heben sich die Nebenschwingungen weitgehend auf, und das Spektrum bekommt eine kosinusförmige, weiche Flanke.
--- falsch
Ein Tiefpass aus der Hauptkomponente $\operatorname{si}(\pi t/T)$ und zwei Echos der Amplitude $-\frac12$ im Abstand $\pm T$. Dabei verstärken sich die Nebenschwingungen gegenseitig, und das Spektrum bekommt eine besonders steile, senkrechte Flanke.
--- falsch
Ein Filter, dessen Impulsantwort ein einzelner Kosinus der Periode $2T$ ist. Sein Spektrum besteht deshalb aus zwei Linien bei $\pm\frac{1}{2T}$, zwischen denen keine Frequenz durchgelassen wird.
--- falsch
Ein Pulsformfilter aus der Hauptkomponente $\operatorname{si}(\pi t/T)$ und zwei Echos der Amplitude $\frac12$ im Abstand $\pm T$. Sein Spektrum bleibt dabei ein scharfes Rechteck mit senkrechter Kante, nur doppelt so hoch wie zuvor.
:::
:::karte formel Pulsformfilter
Wie lauten Impulsantwort und Frequenzgang des Pulsformfilters mit zwei Echos der Amplitude $\frac12$ im Abstand $\pm T$?
---
$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t+T}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t-T}{T}\Bigr)$ mit $H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]$: Die beiden Echos liefern zusammen den Kosinus.
--- falsch
$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t+T}{T}\Bigr)+\tfrac12\operatorname{si}\Bigl(\pi\frac{t-T}{T}\Bigr)$ mit $H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]\mathrm{e}^{-\mathrm{j}2\pi Tf}$: Die Echos verzögern das Filter zusätzlich um $T$.
--- falsch
$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)\cos\Bigl(\frac{\pi t}{T}\Bigr)$ mit $H(f)=T\operatorname{rect}(Tf)\cos(\pi Tf)$: Die Echos entstehen, weil man die si-Funktion der Hauptkomponente mit einem Kosinus moduliert.
--- falsch
$h(t)=\operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)+\tfrac12\delta(t+T)+\tfrac12\delta(t-T)$ mit $H(f)=T\operatorname{rect}(Tf)+\cos(2\pi Tf)$: Die Echos sind kurze Impulse im Abstand $\pm T$ neben der Hauptkomponente.
:::
:::karte zusammenhang Weniger Überschwingen, breitere Hauptkeule
Was gewinnt man mit dem Cosine-Rolloff-Filter gegenüber dem idealen Tiefpass, und was kostet es?
---
Das Überschwingen der Impulsantwort sinkt von 21,7 % auf 2,7 %, weil sich die Nebenschwingungen weitgehend aufheben. Dafür ist die Hauptkeule doppelt so breit: Die erste Nullstelle liegt bei $2T$ statt bei $T$.
--- falsch
Das Überschwingen sinkt von 21,7 % auf 2,7 %, und die Hauptkeule wird zugleich halb so breit: Die erste Nullstelle liegt bei $T/2$ statt bei $T$, das Filter ist also in jeder Hinsicht besser als der ideale Tiefpass.
--- falsch
Das Überschwingen bleibt bei 21,7 %, weil es nach dem Gibbs-Phänomen nicht von der Form des Spektrums abhängt; man gewinnt nur eine doppelt so breite Hauptkeule mit der ersten Nullstelle bei $2T$.
--- falsch
Das Überschwingen sinkt auf 8,95 %, weil die weiche Flanke wie eine Sprungantwort wirkt; dafür verdoppelt sich die Grenzfrequenz, und die erste Nullstelle rückt von $T$ auf $T/2$.
:::
:::karte zusammenhang Glatte Flanke, schnelles Abklingen
Warum klingt die Impulsantwort des Cosine-Rolloff-Filters viel schneller ab als die des idealen Tiefpasses?
---
Weil sein Frequenzgang bei $f_\mathrm g=\frac{1}{2T}$ ohne Sprung und ohne Knick auf null geht: Wert und Steigung sind dort null. Je glatter das Spektrum, desto schneller klingt die Impulsantwort ab.
--- falsch
Weil seine Grenzfrequenz doppelt so hoch ist wie die des idealen Tiefpasses: Eine größere Bandbreite verkürzt nach dem Ähnlichkeitssatz die Antwortdauer, und die Nebenschwingungen klingen schneller ab.
--- falsch
Weil sein Frequenzgang bei $f_\mathrm g=\frac{1}{2T}$ senkrecht auf null fällt: Eine möglichst steile Kante sorgt dafür, dass keine Frequenzen über $f_\mathrm g$ durchkommen und die Antwort schnell endet.
--- falsch
Weil die Echos die Impulsantwort nach der Zeit $2T$ hart abschneiden: Danach ist sie exakt null, und das Spektrum bleibt trotzdem ein scharfes Rechteck mit derselben senkrechten Kante.
:::
:::karte zusammenhang Transversalfilter
Wie baut man eine Summe verzögerter, gewichteter Kopien als Transversalfilter, und warum verzögert man dabei alles gemeinsam?
---
Mit einer Kette von Verzögerungsgliedern, deren Abgriffe gewichtet und addiert werden; das ist dieselbe Struktur wie ein FIR-Filter. Alles wird gemeinsam verzögert, damit kein Glied in die Zukunft greifen muss.
--- falsch
Mit einer Rückkopplung, die den Ausgang verzögert, gewichtet und wieder zum Eingang addiert; das ist die Struktur eines IIR-Filters. Die gemeinsame Verzögerung sorgt dafür, dass die Rückkopplung stabil bleibt.
--- falsch
Mit parallel geschalteten Bandpässen, deren Ausgänge gewichtet und addiert werden; jeder liefert ein Echo. Alles wird gemeinsam verzögert, damit die Bandpässe gleichzeitig einschwingen.
--- falsch
Mit einer Kette von Verzögerungsgliedern, deren Abgriffe gewichtet und addiert werden. Eine gemeinsame Verzögerung braucht man nicht, weil die Echos mit negativem $n$ bei jedem Tiefpass ohnehin null sind.
:::
:::karte herleitung Frequenzgang des Cosine-Rolloff-Filters
Wie folgt aus der Echomethode der Frequenzgang $H(f)=T\operatorname{rect}(Tf)\bigl[1+\cos(2\pi Tf)\bigr]$ des Pulsformfilters?
---
Man bestimmt die Abtastwerte $h(nT)$, weil sie in der Echomethode die Gewichte sind: Bei $t=mT$ ist $\operatorname{si}(\pi(t\pm T)/T)$ nur für $m=\mp1$ gleich 1, sonst null.
---
Also ist $h(0)=1$, $h(\pm T)=\frac12$, und alle anderen $h(nT)$ sind null, weil jede si-Funktion nur an ihrem eigenen Abtastpunkt von null verschieden ist.
---
Man setzt in $H(f)=T\operatorname{rect}(Tf)\sum_nh(nT)\,\mathrm{e}^{-\mathrm{j}2\pi nTf}$ ein, weil das der Frequenzgang zur si-Reihe ist, und erhält $T\operatorname{rect}(Tf)\bigl[1+\frac12\mathrm{e}^{\mathrm{j}2\pi Tf}+\frac12\mathrm{e}^{-\mathrm{j}2\pi Tf}\bigr]$.
---
Die beiden Exponentialfunktionen ergeben zusammen $\cos(2\pi Tf)$, weil nach Euler die halbe Summe zweier Exponentialfunktionen mit entgegengesetztem Exponenten der Kosinus ist.
:::
::::
