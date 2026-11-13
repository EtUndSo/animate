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

::::formelsammlung
**Abtasttheorem**

$$T\le\frac{1}{2f_\mathrm g}\qquad\text{also}\qquad f_\mathrm A=\frac1T\ge2f_\mathrm g$$

Für ein Tiefpasssignal (Spektrum verschwindet oberhalb von $f_\mathrm g$): Dann ist es durch $s(nT)$ eindeutig bestimmt. Die Mindestrate $2f_\mathrm g$ heißt Nyquist-Rate. Genau an der Grenze darf das Spektrum bei $f_\mathrm g$ keine Linie haben, sonst braucht man $f_\mathrm A>2f_\mathrm g$. Bei zu langsamer Abtastung erscheint eine Frequenz über $f_\mathrm A/2$ als tiefere Frequenz, ihr Alias.

**Idealer Tiefpass zur Rückgewinnung**

$$H_\mathrm{TP}(f)=T\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$$

Schneidet aus $S_\mathrm a(f)$ die Kopie bei $f=0$ aus; der Faktor $T$ hebt das $1/T$ auf.

**Rückgewinnung im Zeitbereich**

$$s(t)=s_\mathrm a(t)*\bigl[2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)\bigr]$$

Faltung mit der Impulsantwort des idealen Tiefpasses; gilt, solange das Abtasttheorem erfüllt ist.

**si-Interpolation**

$$s(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)$$

Bei $T=1/(2f_\mathrm g)$. Jede si-Funktion ist an ihrem eigenen Abtastpunkt 1 und an allen anderen null; die Summe trifft alle Abtastwerte und enthält keine Frequenz über $f_\mathrm g$.
::::

::::lernkarten
:::karte begriff Tiefpasssignal
Was ist ein Tiefpasssignal im Sinne des Abtasttheorems?
---
Ein Signal, dessen Spektrum oberhalb einer Grenzfrequenz $f_\mathrm g$ verschwindet. Es enthält also keine Anteile mit Frequenzen über $f_\mathrm g$.
--- falsch
Ein Signal, das bereits durch einen Tiefpass gelaufen ist und deshalb zeitlich glatt verläuft. Sein Spektrum darf beliebig hohe Frequenzen enthalten, solange sie schwach sind.
--- falsch
Ein Signal, dessen Spektrum unterhalb einer Grenzfrequenz $f_\mathrm g$ verschwindet. Es enthält also nur Anteile mit Frequenzen über $f_\mathrm g$.
--- falsch
Ein Signal, dessen Frequenzen alle unter der Abtastrate liegen. Die Grenze ist also $f_\mathrm A$ selbst, und jedes Signal mit tieferen Frequenzen lässt sich exakt zurückgewinnen.
:::
:::karte formel Abtasttheorem
Unter welcher Bedingung ist ein Tiefpasssignal mit der Grenzfrequenz $f_\mathrm g$ durch seine Abtastwerte $s(nT)$ eindeutig bestimmt?
---
Wenn $T\le\frac{1}{2f_\mathrm g}$ ist, also $f_\mathrm A=\frac1T\ge2f_\mathrm g$: Die Abtastrate muss mindestens doppelt so hoch sein wie die höchste Frequenz. Genau an der Grenze darf das Spektrum bei $f_\mathrm g$ keine Linie haben.
--- falsch
Wenn $T\le\frac{1}{f_\mathrm g}$ ist, also $f_\mathrm A\ge f_\mathrm g$: Die Abtastrate muss mindestens so hoch sein wie die höchste Frequenz, damit jede Schwingung mindestens einmal je Periode erfasst und so eindeutig erkannt wird.
--- falsch
Wenn $T\ge\frac{1}{2f_\mathrm g}$ ist, also $f_\mathrm A\le2f_\mathrm g$: Die Abtastrate darf höchstens doppelt so hoch sein wie die höchste Frequenz, sonst überlappen die Kopien im Spektrum.
--- falsch
Wenn $T\le\frac{1}{2f_\mathrm g}$ ist und das Signal zusätzlich periodisch ist. Nur dann wiederholen sich die Abtastwerte, und das Signal lässt sich aus einer einzigen Periode eindeutig bestimmen.
:::
:::karte begriff Nyquist-Rate
Was gibt die Nyquist-Rate eines Tiefpasssignals mit der Grenzfrequenz $f_\mathrm g$ an?
---
Die Mindestabtastrate $2f_\mathrm g$, die das Abtasttheorem verlangt. Mit ihr liegen die Kopien im Spektrum gerade noch getrennt nebeneinander.
--- falsch
Die höchste Frequenz $f_\mathrm g$ im Signal selbst. Die Abtastrate muss genau diesen Wert haben, damit die Kopien im Spektrum lückenlos aneinanderstoßen.
--- falsch
Die halbe Abtastrate $f_\mathrm A/2$. Frequenzen darüber werden bei der Rückgewinnung als tiefere Frequenzen gedeutet, Frequenzen darunter bleiben unverändert.
--- falsch
Die Abtastrate $4f_\mathrm g$, die man in der Praxis wählt. Sie lässt dem Anti-Aliasing-Filter genug Platz, weil reale Filter nicht senkrecht abfallen.
:::
:::karte formel Rückgewinnung mit dem idealen Tiefpass
Wie gewinnt man ein Tiefpasssignal aus dem ideal abgetasteten Signal $s_\mathrm a(t)$ zurück, wenn $f_\mathrm A\ge2f_\mathrm g$ ist?
---
Mit dem idealen Tiefpass $H_\mathrm{TP}(f)=T\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$. Er schneidet die Kopie bei $f=0$ aus; im Zeitbereich ist das die Faltung $s(t)=s_\mathrm a(t)*\bigl[2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)\bigr]$.
--- falsch
Mit dem idealen Tiefpass $H_\mathrm{TP}(f)=\operatorname{rect}\bigl(\frac{f}{f_\mathrm g}\bigr)$. Er schneidet alle Kopien bis zur Frequenz $f_\mathrm g$ aus; im Zeitbereich multipliziert man $s_\mathrm a(t)$ dazu mit einer si-Funktion.
--- falsch
Mit einem Hochpass, der die Kopie bei $f=0$ entfernt. Übrig bleiben die Kopien bei den Vielfachen der Abtastrate, deren Summe im Zeitbereich wieder das ursprüngliche Signal ergibt.
--- falsch
Mit dem idealen Tiefpass $H_\mathrm{TP}(f)=T\operatorname{rect}\bigl(\frac{f}{2f_\mathrm g}\bigr)$. Er schneidet die Kopie bei $f=0$ aus; im Zeitbereich hält man dazu jeden Abtastwert bis zum nächsten fest, das ergibt genau das Original.
:::
:::karte formel si-Interpolation
Wie berechnet man ein mit $T=1/(2f_\mathrm g)$ abgetastetes Tiefpasssignal $s(t)$ für jede Zeit $t$ aus seinen Abtastwerten?
---
Mit der si-Interpolation $s(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\operatorname{si}\Bigl(\pi\frac{t-nT}{T}\Bigr)$: Jeder Abtastwert wird durch eine si-Funktion ersetzt, die an ihrem Abtastpunkt 1 und an allen anderen null ist.
--- falsch
Mit der linearen Interpolation: Zwischen zwei benachbarten Abtastwerten $s(nT)$ und $s((n+1)T)$ verbindet man die Werte durch eine Gerade. Bei einem Tiefpasssignal ist das exakt.
--- falsch
Mit $s(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\operatorname{si}\bigl(\pi\frac{t-nT}{T}\bigr)$, wobei jede si-Funktion an allen Abtastpunkten den Wert 1 hat. Die Summe ist deshalb an jedem Abtastpunkt die Summe aller Abtastwerte.
--- falsch
Mit $s(t)=\sum_{n=-\infty}^{\infty}s(nT)\,\operatorname{rect}\bigl(\frac{t-nT}{T}\bigr)$: Jeder Abtastwert wird für die Dauer $T$ festgehalten. Diese Treppe enthält keine Frequenz über $f_\mathrm g$.
:::
:::karte herleitung Rückgewinnung
Wie folgt aus dem periodischen Spektrum $S_\mathrm a(f)$, dass bei $2f_\mathrm g=1/T$ die si-Interpolation $\sum_ns(nT)\operatorname{si}(\pi(t-nT)/T)$ das Original liefert?
---
Für $|f|\le f_\mathrm g$ liegt nur die Kopie $k=0$, also $S_\mathrm a(f)=\frac1TS(f)$, weil die Kopien bei $f_\mathrm A\ge2f_\mathrm g$ getrennt liegen.
---
Man multipliziert mit $H_\mathrm{TP}=T\operatorname{rect}(f/2f_\mathrm g)$ und erhält $S_\mathrm a\cdot H_\mathrm{TP}=S$, weil der Tiefpass alle übrigen Kopien wegschneidet und der Faktor $T$ das $1/T$ aufhebt.
---
Im Zeitbereich wird daraus eine Faltung von $s_\mathrm a$ mit $2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)$, weil Rechteck und si-Funktion ein Fourier-Paar sind ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)) und ein Produkt der Spektren einer Faltung entspricht.
---
Mit $2f_\mathrm g=1/T$ wird dieser Kern zu $\operatorname{si}(\pi t/T)$, weil dann der Vorfaktor $2f_\mathrm gT$ gleich 1 ist.
---
Die Faltung von $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ mit dem Kern setzt ihn an jeden Abtastpunkt, weil die Faltung mit $\delta(t-nT)$ um $nT$ verschiebt; es entsteht die si-Interpolation.
:::
:::karte zusammenhang si-Funktionen treffen die Abtastwerte
Warum trifft die Summe der gewichteten si-Funktionen bei der si-Interpolation jeden Abtastwert genau?
---
Jede si-Funktion $\operatorname{si}\bigl(\pi\frac{t-nT}{T}\bigr)$ ist an ihrem eigenen Abtastpunkt $nT$ gleich 1 und an allen anderen Abtastpunkten null. An einem Abtastpunkt trägt deshalb nur der Summand dieses Punktes bei, mit seinem Gewicht $s(nT)$.
--- falsch
Weil die si-Funktionen so schmal sind, dass sie sich nicht überlappen. Jede wirkt nur in einem Intervall der Breite $T$ um ihren eigenen Abtastpunkt, und dort ist sie gleich 1.
--- falsch
Weil man die Gewichte nachträglich so anpasst, dass die Summe stimmt. Die Gewichte sind nicht die Abtastwerte selbst, sondern werden aus einem Gleichungssystem für alle Abtastpunkte bestimmt, das man vor der Interpolation lösen muss.
--- falsch
Sie trifft sie nur näherungsweise, weil sich die Ausläufer der si-Funktionen an jedem Abtastpunkt aufsummieren. Erst bei unendlich hoher Abtastrate verschwindet dieser Fehler ganz.
:::
:::karte begriff Alias
Was ist der Alias einer Frequenz, die beim Abtasten über der halben Abtastrate $f_\mathrm A/2$ liegt?
---
Die falsche, tiefere Frequenz, als die sie nach der Rückgewinnung erscheint. Sie hat dieselben Abtastwerte wie die ursprüngliche Frequenz, etwa 300 Hz statt 700 Hz bei $f_\mathrm A=1$ kHz.
--- falsch
Eine zusätzliche Frequenz, die neben der ursprünglichen erscheint. Nach der Rückgewinnung sind beide vorhanden, etwa 700 Hz und zusätzlich 300 Hz bei $f_\mathrm A=1$ kHz.
--- falsch
Die höhere Frequenz, als die sie nach der Rückgewinnung erscheint. Sie liegt um die Abtastrate darüber, etwa 1700 Hz statt 700 Hz bei $f_\mathrm A=1$ kHz.
--- falsch
Die ursprüngliche Frequenz selbst, die nach der Rückgewinnung nur gedämpft erscheint. Der Tiefpass schwächt sie ab, weil sie über der halben Abtastrate $f_\mathrm A/2$ liegt, lässt ihre Frequenz aber unverändert.
:::
:::karte zusammenhang Alias bei 700 Hz
Warum lassen sich bei $f_\mathrm A=1$ kHz ein Kosinus mit 700 Hz und einer mit 300 Hz an ihren Abtastwerten nicht unterscheiden?
---
Mit der Frequenz bezogen auf die Abtastrate gilt $\cos(2\pi\cdot0{,}7n)=\cos(2\pi n-2\pi\cdot0{,}3n)=\cos(2\pi\cdot0{,}3n)$, weil $2\pi n$ ganze Umdrehungen sind und der Kosinus gerade ist. Die Abtastwerte sind exakt gleich.
--- falsch
Weil 700 Hz und 300 Hz zusammen die Abtastrate ergeben und sich ihre Abtastwerte deshalb gegenseitig auslöschen. Übrig bleibt eine Folge aus Nullen, die zu beiden Frequenzen passt.
--- falsch
Sie lassen sich unterscheiden, nur nicht mit einem Tiefpass. Die Abtastwerte des 700-Hz-Kosinus haben das umgekehrte Vorzeichen, und erst nach einer Gleichrichtung sind sie gleich.
--- falsch
Weil sich ihre Abtastwerte nur in der Phase unterscheiden: $\cos(2\pi\cdot0{,}7n)=\sin(2\pi\cdot0{,}3n)$. Ein Rechner wertet jedoch nur die Beträge aus, und die stimmen bei beiden überein.
:::
:::karte begriff Anti-Aliasing-Filter
Was ist ein Anti-Aliasing-Filter, und warum sitzt es vor dem Abtaster und nicht dahinter?
---
Ein Tiefpass vor dem Abtaster, der Frequenzen über $f_\mathrm A/2$ entfernt. Er muss vorher wirken, weil ein Alias nach dem Abtasten dieselben Abtastwerte hat wie ein echtes Signal und sich nicht mehr abtrennen lässt.
--- falsch
Ein Tiefpass hinter dem Abtaster, der die Kopien im Spektrum entfernt. Er könnte auch davor sitzen, hinter dem Abtaster arbeitet er aber genauer, weil die Frequenzen dort schon getrennt vorliegen.
--- falsch
Ein Hochpass vor dem Abtaster, der tiefe Frequenzen entfernt. Er muss vorher wirken, weil tiefe Frequenzen sonst in die Kopien bei den Vielfachen der Abtastrate überlaufen würden und dort nicht mehr zu trennen wären.
--- falsch
Ein Tiefpass vor dem Abtaster, der die Abtastrate erhöht, bis kein Alias mehr entsteht. Er muss vorher wirken, weil der Abtaster seinen Takt aus der Grenzfrequenz des Filters ableitet.
:::
:::karte zusammenhang Abtasten genau an der Grenze
Warum genügt $f_\mathrm A=2f_\mathrm g$ nicht, wenn das Signal einen Sinus mit genau der Frequenz $f_\mathrm g$ enthält?
---
Ein Sinus mit $f_\mathrm g=f_\mathrm A/2$ kann bei ungünstiger Phase immer im Nulldurchgang abgetastet werden, dann sind alle Abtastwerte null. Das Theorem verlangt deshalb, dass das Spektrum bei $f_\mathrm g$ keine Linie hat, oder $f_\mathrm A>2f_\mathrm g$.
--- falsch
Weil der Sinus dann zwischen zwei Abtastpunkten genau eine ganze Periode durchläuft. Alle Abtastwerte sind deshalb gleich, und der Sinus erscheint nach der Rückgewinnung als Gleichanteil mit dem Wert, den er im ersten Abtastpunkt hatte.
--- falsch
Es genügt durchaus; das Problem tritt nur bei realen Abtastern auf, deren Schließzeit $T_0$ den Sinus verschmiert. Ein idealer Abtaster erfasst auch den Sinus an der Grenze stets fehlerfrei.
--- falsch
Weil ein Sinus mit $f_\mathrm g=f_\mathrm A/2$ bei der si-Interpolation doppelt gezählt wird. Die Kopien bei $\pm f_\mathrm g$ fallen übereinander, und die Amplitude erscheint verdoppelt, unabhängig von der Phase.
:::
:::karte zusammenhang Schneller abtasten als nötig
Warum tastet man in der Praxis schneller ab als mit der Nyquist-Rate, etwa Telefonsprache, die auf 3,4 kHz begrenzt ist, mit 8 kHz?
---
Reale Tiefpässe fallen nicht senkrecht ab und brauchen Platz für ihren Übergangsbereich. Bei 8 kHz liegt $f_\mathrm A/2$ bei 4 kHz, und zwischen 3,4 und 4 kHz kann das Anti-Aliasing-Filter von Durchlass auf Sperrung übergehen.
--- falsch
Weil die Nyquist-Rate nur für periodische Signale gilt. Sprache ist nicht periodisch, deshalb verlangt das Abtasttheorem für sie eine um etwa ein Fünftel höhere Abtastrate, und 8 kHz erfüllen genau diese Forderung.
--- falsch
Weil der Rechner sonst nicht schnell genug rechnet. Bei der Nyquist-Rate muss jeder Wert sofort verarbeitet werden, mit höherer Rate bleibt ihm mehr Zeit für jeden einzelnen Wert.
--- falsch
Weil schnelleres Abtasten die Kopien im Spektrum schmaler macht. Bei 8 kHz reicht jede Kopie nur noch bis 3,4 kHz, und der ideale Tiefpass trennt sie dann ohne jeden Übergangsbereich.
:::
::::
