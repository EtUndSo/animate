---
title: Stufe 3: Abtasttheorem und Rückgewinnung
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Abtastung und zeitdiskrete Systeme
adresse: elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme
knoten: Kapitel 4: Abtastung und zeitdiskrete Systeme
order: 3240400
summary: Wann lässt sich das Original aus den Abtastwerten exakt zurückgewinnen, und wie?
tags: Tiefpasssignal, Nyquist-Rate, Alias, Anti-Aliasing-Filter
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Wann lässt sich das Original aus den Abtastwerten exakt zurückgewinnen, und wie?
:::

:::satz Satz 3.1 (Abtasttheorem)
<span class="anker" id="satz-3-1"></span>

Ein Signal, dessen Spektrum oberhalb von $f_\mathrm g$ verschwindet (__Tiefpasssignal__), ist durch seine Abtastwerte $s(nT)$ eindeutig bestimmt, wenn

<span class="anker" id="gl-3-1"></span>
$$T\le\frac{1}{2f_\mathrm g}\qquad\text{also}\qquad f_\mathrm A=\frac1T\ge2f_\mathrm g. \tag{3.1}$$

Mit dem idealen Tiefpass $H_\mathrm{TP}(f)=T\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$ gilt

<span class="anker" id="gl-3-2"></span>
$$s(t)=s_\mathrm a(t)*\bigl[2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)\bigr], \tag{3.2}$$

und bei $T=1/(2f_\mathrm g)$:

<span class="anker" id="gl-3-3"></span>
$$s(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr). \tag{3.3}$$
:::

⁠**So liest man das:** Bei $f_\mathrm A\ge2f_\mathrm g$ liegen die Kopien in Abb. [1](das-spektrum-des-abgetasteten-signals.html#abb-1) getrennt. Ein Tiefpass schneidet die Kopie bei $f=0$ aus, und die hat genau die Form des Originals. Im Zeitbereich heißt das: Jeder Abtastwert wird durch eine si-Funktion ersetzt, die an ihrem eigenen Abtastpunkt 1 ist und an allen anderen null (Abb. [2](#abb-2)). Ihre Summe trifft alle Abtastwerte und füllt die Lücken so, dass keine Frequenz über $f_\mathrm g$ entsteht. Die Mindestrate $2f_\mathrm g$ heißt __Nyquist-Rate__.

:::herleitung Rückgewinnung
Für $|f|\le f_\mathrm g$ liegt nur die Kopie $k=0$, also $S_\mathrm a(f)=\frac1TS(f)$. Mit $H_\mathrm{TP}=T\operatorname{rect}(f/2f_\mathrm g)$ ist $S_\mathrm a\cdot H_\mathrm{TP}=S$. Im Zeitbereich: $T\operatorname{rect}(f/2f_\mathrm g)\;\bullet\!\!-\!\!\circ\;2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)$ ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), Rechteck und si). Mit [(1.2)](signalklassen-und-ideale-abtastung.html#gl-1-2) und $2f_\mathrm g=1/T$ wird $s_\mathrm a*\operatorname{si}(\pi t/T)=\sum_ns(nT)\operatorname{si}(\pi(t-nT)/T)$.
:::

:::abbildung et3/k4siinterp 2
si-Interpolation: Abtastwerte $0;\ 1;\ 0{,}6;\ -0{,}4;\ 0{,}8;\ 0$ (rot), die gewichteten si-Funktionen (grau) und ihre Summe (blau). Jede si-Funktion ist an den anderen Abtastpunkten null, deshalb trifft die Summe alle Werte genau.
:::

**Aliasing.** Wird zu langsam abgetastet, überlappen die Kopien. Eine Frequenz über $f_\mathrm A/2$ erscheint nach der Rückgewinnung als eine falsche, tiefere Frequenz, ihr __Alias__. Im Rechenmodell haben ein Kosinus mit 700 Hz und einer mit 300 Hz bei $f_\mathrm A=1$ kHz exakt dieselben Abtastwerte, denn $\cos(2\pi\cdot0{,}7n)=\cos(2\pi n-2\pi\cdot0{,}3n)=\cos(2\pi\cdot0{,}3n)$ (Abb. [3](#abb-3)). Nachträglich lässt sich das nicht mehr trennen. Deshalb filtert man vor jedem Abtaster mit einem Tiefpass (__Anti-Aliasing-Filter__).

:::abbildung et3/k4alias 3
Bei $f_\mathrm A=1$ kHz fallen die Abtastwerte (schwarz) von 700 Hz und 300 Hz zusammen. Die 700 Hz sind über $f_\mathrm A/2=500$ Hz und erscheinen als Alias bei 300 Hz.
:::

:::frage Reicht nicht genau $f_\mathrm A=2f_\mathrm g$? Bei einem Sinus mit genau $f_\mathrm g$ geht das doch schief.
Ja, genau an der Grenze geht es schief: Ein Sinus mit $f_\mathrm g=f_\mathrm A/2$ kann bei ungünstiger Phase immer im Nulldurchgang abgetastet werden, und alle Abtastwerte sind null. Der Satz verlangt deshalb streng genommen, dass das Spektrum *bei* $f_\mathrm g$ keine Linie hat, oder $f_\mathrm A>2f_\mathrm g$. In der Praxis tastet man ohnehin schneller ab, weil reale Tiefpässe nicht senkrecht abfallen und Platz für ihren Übergangsbereich brauchen.
:::

:::ltspice Abtast-Halte-Glied: Aliasing sehen
⁠**Zeichnen:** Quelle `voltage` am Netz `in` mit `SINE(0 1 700 0 0 90)`, ein Kosinus mit 700 Hz. Ein Schalter `sw` (Wert `SW1`) von `in` nach `sh`, dort `cap` mit `100n` nach Masse. Den Steuereingang des Schalters treibt eine zweite Quelle mit `PULSE(0 1 0 10n 10n 1u 1m)`: Der Schalter schließt jede Millisekunde für 1 µ s ($f_\mathrm A=1$ kHz), dazwischen hält der Kondensator den Abtastwert. Hinter `sh` folgt als Tiefpass zur Rückgewinnung eine Quelle `e` mit dem Ausgang `out`. Sie ist ein Butterworth-Tiefpass 4. Ordnung (Durchlass möglichst flach) mit der Grenzfrequenz 400 Hz und hat den Wert

`Laplace=1/(((s/wg)**2+0.7654*s/wg+1)*((s/wg)**2+1.8478*s/wg+1))`

⁠**Direktiven:** `.model SW1 SW(Ron=1 Roff=1G Vt=0.5)`, `.param wg=2*pi*400`, `.tran 0 40m 0 1u`, `.options plotwinsize=0`, `.four 100 15 V(sh) V(out)`.

⁠**Was du siehst:** Die Treppe an `sh` folgt einer 300-Hz-Schwingung, und an `out` steht ein Kosinus mit 300 Hz statt 700 Hz. In `.four` ist die Linie bei 300 Hz die stärkste. Mit `SINE(0 1 300 0 0 90)` entsteht dieselbe Treppe. Stelle 1,2 kHz ein und vergleiche mit deinem Ergebnis aus Aufgabe [1](#aufg-1)(a).

⁠**Anti-Aliasing:** Setze eine zweite, gleiche `e`-Quelle vor den Schalter. Bei 700 Hz sinkt die 300-Hz-Linie an `out` auf etwa ein Zehntel, ein Eingang mit 300 Hz kommt fast ungeschwächt durch. Den Alias muss man also vor dem Abtasten verhindern: Danach ist er von einem echten 300-Hz-Signal nicht mehr zu unterscheiden.
:::

:::aufgabe Aufgabe 1 ★ Alias-Frequenzen
<span class="anker" id="aufg-1"></span>

$f_\mathrm A=1$ kHz.

<ol class="al">

<li>

Als welche Frequenz erscheint ein Kosinus mit 1,2 kHz nach der Rückgewinnung?

</li>

<li>

Welche Frequenzen ergeben dieselben Abtastwerte wie ein Kosinus mit 50 Hz?

</li>

</ol>

:::loesung
(a) 1,2 kHz liegt über $f_\mathrm A/2$. Es hat dieselben Abtastwerte wie $1{,}2-1=0{,}2$ kHz und erscheint als 200 Hz.

(b) Alle $\pm50\,\mathrm{Hz}+k\cdot1\,\mathrm{kHz}$: 950 Hz, 1050 Hz, 1950 Hz, 2050 Hz und so weiter. Beim Kosinus zählen negative und positive Frequenz gleich, deshalb gehört auch $1000-50$ dazu.
:::
:::

:::aufgabe Aufgabe 2 ★★ Abtastraten in der Praxis
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Telefonsprache wird auf 3,4 kHz begrenzt und mit 8 kHz abgetastet. Wie groß ist die Nyquist-Rate, und wozu dient der Abstand?

</li>

<li>

Eine Audio-CD tastet mit 44,1 kHz ab. Bis zu welcher Frequenz kann sie Töne speichern, und wie breit ist der Übergangsbereich für das Anti-Aliasing-Filter, wenn das Hörband bis 20 kHz reicht?

</li>

</ol>

:::loesung
(a) Nyquist-Rate $2\cdot3{,}4=6{,}8$ kHz. Mit 8 kHz liegt $f_\mathrm A/2$ bei 4 kHz. Zwischen 3,4 und 4 kHz hat das Anti-Aliasing-Filter Platz, um von Durchlass auf Sperrung überzugehen.

(b) Bis $f_\mathrm A/2=22{,}05$ kHz. Der Übergangsbereich von 20 bis 22,05 kHz ist nur 2,05 kHz breit. Deshalb braucht man steile Filter oder Überabtastung.
:::
:::

:::aufgabe Aufgabe 3 ★★ si-Interpolation von Hand
<span class="anker" id="aufg-3"></span>

Berechne mit [(3.3)](#gl-3-3) den Wert des Signals aus Abb. [2](#abb-2) bei $t=2{,}5T$. Tipp: $\operatorname{si}(\pi\cdot0{,}5)=2/\pi$ und $\operatorname{si}(\pi\cdot1{,}5)=-2/(3\pi)$. Welche Abtastwerte tragen nichts bei?

:::loesung
Bei $t=2{,}5T$ ist $\operatorname{si}(\pi(2{,}5-k))$ für $k\in\{2,3\}$ gleich $\frac2\pi$, für $k\in\{1,4\}$ gleich $-\frac{2}{3\pi}$. Die Werte bei $k=0$ und $k=5$ sind null und tragen nichts bei:

$$s(2{,}5T)=\frac2\pi\Bigl[-\tfrac13\cdot1+0{,}6-0{,}4-\tfrac13\cdot0{,}8\Bigr]=\frac2\pi\cdot(-0{,}4)=-0{,}255.$$
:::
:::
