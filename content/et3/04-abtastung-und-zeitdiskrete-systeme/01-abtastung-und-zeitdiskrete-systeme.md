---
title: Abtastung und zeitdiskrete Systeme
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Abtastung und zeitdiskrete Systeme
order: 3240100
summary: Vom kontinuierlichen Signal zur Zahlenfolge: Abtasttheorem, diskrete Faltung, DFT, FFT und z-Transformation
tags: Abtastwerten, analoges, zeitdiskretes, digitales, ideale Abtaster, Spiegelspektren, Tiefpasssignal, Nyquist-Rate
lang: de
---

## Worum es geht

Ein Rechner kann keine Funktion $s(t)$ speichern, nur eine Folge von Zahlen. Man misst das Signal deshalb im festen Takt $T$ und arbeitet mit den __Abtastwerten__ $s(nT)$. Zwei Fragen bestimmen dieser Artikel: *Geht dabei Information verloren?* Und: *Wie rechnet man mit Zahlenfolgen so, wie die [Teile 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html) bis 3 mit Funktionen gerechnet haben?*

:::merke Die Antwort in drei Sätzen (am Ende des Artikels sollen sie selbstverständlich sein)
<ol>

<li>

Abtasten ist Multiplizieren mit einem Dirac-Kamm. Im Spektrum wird daraus eine Faltung mit einem Kamm: Das Spektrum wiederholt sich periodisch mit der Abtastrate.

</li>

<li>

Liegen die Wiederholungen nicht übereinander (Abtastrate über der doppelten höchsten Frequenz), lässt sich das Signal mit einem idealen Tiefpass exakt zurückgewinnen. Andernfalls entsteht Aliasing.

</li>

<li>

Für Zahlenfolgen gelten dieselben Werkzeuge wie für Funktionen: Faltung als Summe, Fourier-Transformation mit periodischem Spektrum, DFT als deren Abtastwerte, z-Transformation als Gegenstück zur Laplace-Transformation.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen: Diskret in einem Bereich heißt periodisch im anderen.**

| Ergebnis | Woher es kommt |
|---|---|
| periodisches Spektrum nach Abtastung | Zeit diskret $\Rightarrow$ Spektrum periodisch (Stufe [2](#stufe-2)) |
| Abtasttheorem, Aliasing | ob sich die periodischen Kopien überlappen (Stufe [3](#stufe-3)) |
| si-Interpolation | idealer Tiefpass schneidet eine Kopie aus (Stufe [3](#stufe-3)) |
| Fourier-Reihe | Spektrum diskret $\Rightarrow$ Zeit periodisch (Stufe [4](#stufe-4)) |
| diskrete Faltung | Faltungsintegral über Dirac-gewichtete Abtastwerte (Stufe [5](#stufe-5)) |
| zeitdiskrete Fourier-Transformation | Spektrum der Abtastwerte, periodisch mit 1 (Stufe [7](#stufe-7)) |
| DFT | beides diskret $\Rightarrow$ beides periodisch (Stufe [8](#stufe-8)) |
| Dezimation, Interpolation | Abtasten einer schon abgetasteten Folge (Stufe [10](#stufe-10)) |
| z-Transformation | Laplace-Gedanke für Folgen: erst gewichten, dann transformieren (Stufe [11](#stufe-11)) |

**So arbeitest du mit dem Artikel.** Jede Stufe hat die Idee, typische Fragen mit aufklappbaren Antworten und Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.

:::merke Das Rechenmodell für diesen Artikel
<ul>

<li>

⁠**Abtastrate** $f_\mathrm A=1/T=1$ kHz ($T=1$ ms). Testsignale: Kosinusschwingungen mit 300 Hz und 700 Hz.

</li>

<li>

Bei Folgen wird die Frequenz auf die Abtastrate bezogen: $f=1$ entspricht $f_\mathrm A$. Bei $f_\mathrm A=1$ kHz bedeutet $f=0{,}3$ also 300 Hz.

</li>

<li>

⁠**Rekursives System** $g(n)=s(n)+0{,}6\,g(n-1)$.

</li>

<li>

⁠**DFT-Beispiel** $s_d=(1,\,2,\,0,\,-1)$.

</li>

</ul>

Die Zahlen und Kurven rechnet `rechnung_kap4.py` nach.
:::

## Stufe 1: Signalklassen und ideale Abtastung

<span class="anker" id="stufe-1"></span>

:::zweck
Welche Arten von Signalen gibt es, und wie beschreibt man das Abtasten mathematisch?
:::

**Vier Klassen.** Zeit und Amplitude können jeweils kontinuierlich oder diskret sein. Ein __analoges__ Signal ist in beiden kontinuierlich. Ein __zeitdiskretes__ Signal hat Werte nur zu den Zeiten $nT$, diese aber beliebig genau. Ein __digitales__ Signal ist zusätzlich in der Amplitude gestuft (quantisiert), weil ein Rechner nur endlich viele Zahlen darstellen kann. Dieser Artikel behandelt die Diskretisierung der Zeit. Die Quantisierung der Amplitude ist ein eigenes Thema.

**Vom realen zum idealen Abtaster.** Ein realer Abtaster schließt in jedem Takt für die kurze Zeit $T_0$ einen Schalter:

<span class="anker" id="gl-1-1"></span>
$$s_0(t)=s(t)\sum_{n=-\infty}^{\infty}\operatorname{rect}\Bigl(\frac{t-nT}{T_0}\Bigr)=s(t)\Bigl[\operatorname{rect}\Bigl(\frac{t}{T_0}\Bigr)*\sum_n\delta(t-nT)\Bigr]. \tag{1.1}$$

Macht man $T_0$ immer kürzer, bleiben nur noch die Werte $s(nT)$ übrig. Mathematisch ersetzt man das Rechteck durch einen Dirac-Impuls. Das ist der __ideale Abtaster__:

<span class="anker" id="gl-1-2"></span>
$$s_\mathrm a(t)=s(t)\sum_{n=-\infty}^{\infty}\delta(t-nT)=\sum_{n=-\infty}^{\infty}s(nT)\,\delta(t-nT). \tag{1.2}$$

Das abgetastete Signal ist eine Folge von Dirac-Impulsen, jeder mit einem Abtastwert als Gewicht. Der zweite Schritt ist die Siebeigenschaft $s(t)\delta(t-nT)=s(nT)\delta(t-nT)$. In dieser Form lassen sich abgetastete Signale mit allen Werkzeugen für kontinuierliche Signale behandeln.

## Stufe 2: Das Spektrum des abgetasteten Signals

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
Multiplikation wird Faltung ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), und das Spektrum des Dirac-Kamms ist wieder ein Kamm:

$$s(t)\cdot\sum_n\delta(t-nT)\;\circ\!\!-\!\!\bullet\;S(f)*\frac1T\sum_k\delta\Bigl(f-\frac kT\Bigr)=\frac1T\sum_kS\Bigl(f-\frac kT\Bigr).$$

Die Faltung mit einem verschobenen Dirac-Impuls verschiebt das Spektrum.
:::

:::abbildung et3/k4spektrum
Ein Spektrum bis $f_\mathrm g=300$ Hz (blau, dreieckig zur Übersicht), abgetastet. Oben mit 1 kHz: Die Kopien bei Vielfachen von 1 kHz liegen getrennt. Unten mit 500 Hz: Kopien im Abstand 500 Hz überlappen, die Summe (rot) ist nicht mehr das Original. Der Faktor $1/T$ ist weggelassen.
:::

:::frage Woher „weiß“ das Spektrum, dass abgetastet wurde? Das Signal zwischen den Abtastpunkten ist doch einfach weg.
Genau deshalb. Zwischen den Abtastpunkten ist das abgetastete Signal null, außer an den Impulsen. Jede Schwingung, die an allen Punkten $nT$ dieselben Werte hat, beschreibt dieses Signal gleich gut. Das Spektrum kann sich zwischen ihnen nicht entscheiden und enthält alle: das Original und seine Kopien bei jedem Vielfachen von $1/T$.
:::

## Stufe 3: Abtasttheorem und Rückgewinnung

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

⁠**So liest man das:** Bei $f_\mathrm A\ge2f_\mathrm g$ liegen die Kopien in Abb. [1](#abb-1) getrennt. Ein Tiefpass schneidet die Kopie bei $f=0$ aus, und die hat genau die Form des Originals. Im Zeitbereich heißt das: Jeder Abtastwert wird durch eine si-Funktion ersetzt, die an ihrem eigenen Abtastpunkt 1 ist und an allen anderen null (Abb. [2](#abb-2)). Ihre Summe trifft alle Abtastwerte und füllt die Lücken so, dass keine Frequenz über $f_\mathrm g$ entsteht. Die Mindestrate $2f_\mathrm g$ heißt __Nyquist-Rate__.

:::herleitung Rückgewinnung
Für $|f|\le f_\mathrm g$ liegt nur die Kopie $k=0$, also $S_\mathrm a(f)=\frac1TS(f)$. Mit $H_\mathrm{TP}=T\operatorname{rect}(f/2f_\mathrm g)$ ist $S_\mathrm a\cdot H_\mathrm{TP}=S$. Im Zeitbereich: $T\operatorname{rect}(f/2f_\mathrm g)\;\bullet\!\!-\!\!\circ\;2f_\mathrm gT\operatorname{si}(2\pi f_\mathrm gt)$ ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html), Rechteck und si). Mit [(1.2)](#gl-1-2) und $2f_\mathrm g=1/T$ wird $s_\mathrm a*\operatorname{si}(\pi t/T)=\sum_ns(nT)\operatorname{si}(\pi(t-nT)/T)$.
:::

:::abbildung et3/k4siinterp
si-Interpolation: Abtastwerte $0;\ 1;\ 0{,}6;\ -0{,}4;\ 0{,}8;\ 0$ (rot), die gewichteten si-Funktionen (grau) und ihre Summe (blau). Jede si-Funktion ist an den anderen Abtastpunkten null, deshalb trifft die Summe alle Werte genau.
:::

**Aliasing.** Wird zu langsam abgetastet, überlappen die Kopien. Eine Frequenz über $f_\mathrm A/2$ erscheint nach der Rückgewinnung als eine falsche, tiefere Frequenz, ihr __Alias__. Im Rechenmodell haben ein Kosinus mit 700 Hz und einer mit 300 Hz bei $f_\mathrm A=1$ kHz exakt dieselben Abtastwerte, denn $\cos(2\pi\cdot0{,}7n)=\cos(2\pi n-2\pi\cdot0{,}3n)=\cos(2\pi\cdot0{,}3n)$ (Abb. [3](#abb-3)). Nachträglich lässt sich das nicht mehr trennen. Deshalb filtert man vor jedem Abtaster mit einem Tiefpass (__Anti-Aliasing-Filter__).

:::abbildung et3/k4alias
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

## Stufe 4: Abtastung im Frequenzbereich

<span class="anker" id="stufe-4"></span>

:::zweck
Dasselbe Prinzip gilt mit vertauschten Rollen: Tastet man das Spektrum ab, wird das Signal periodisch.
:::

Ein Spektrum, das nur bei den Frequenzen $kF$ bekannt ist, ist ein Kamm gewichteter Dirac-Impulse. Mit dem Faktor $F$ sind die Gewichte genau die Fourier-Koeffizienten aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html):

<span class="anker" id="gl-4-1"></span>
$$S_p(f)=F\sum_kS(kF)\,\delta(f-kF)=F\,S(f)\cdot\sum_k\delta(f-kF)\;\bullet\!\!-\!\!\circ\;s_p(t)=\sum_ns\Bigl(t-\frac nF\Bigr). \tag{4.1}$$

Das zugehörige Signal ist das Original, periodisch mit $1/F$ wiederholt. Ist das Signal kürzer als $1/F$, überlappen sich die Wiederholungen nicht. Dann gewinnt man es mit einem Zeitfenster zurück, und das Spektrum mit si-Funktionen:

<span class="anker" id="gl-4-2"></span>
$$s(t)=s_p(t)\cdot\operatorname{rect}(Ft)\qquad\Longrightarrow\qquad S(f)=\sum_kS(kF)\operatorname{si}\Bigl(\pi\frac{f-kF}{F}\Bigr). \tag{4.2}$$

⁠**Kurz gesagt:** Diskret in der Zeit heißt periodisch im Spektrum, diskret im Spektrum heißt periodisch in der Zeit. Das zweite ist die Fourier-Reihe aus [Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html): Ihre Koeffizienten sind Abtastwerte des Spektrums eines Einzelimpulses, $S_p(k)=F\cdot S(kF)$.

## Stufe 5: Zeitdiskrete Signale und die diskrete Faltung

<span class="anker" id="stufe-5"></span>

:::zweck
Ab jetzt rechnet man nur noch mit den Zahlenfolgen $s(n)$. Diese Stufe überträgt Faltung, Elementarsignale und LTI-Systeme auf Folgen.
:::

**Faltung der Abtastwerte.** Sind Eingang $s$ und Impulsantwort $h$ eines Systems Tiefpasssignale und wird mit der Nyquist-Rate abgetastet, lässt sich jedes als si-Reihe [(3.3)](#gl-3-3) schreiben. Weil $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$ ist ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)), folgt für die Abtastwerte des Ausgangs allein

$$g(nT)=T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr).$$

Normiert auf $T=1$ ist das die __diskrete Faltung__:

<span class="anker" id="gl-5-1"></span>
$$g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n-m)=s(n)*h(n). \tag{5.1}$$

**Elementarfolgen.**

$$\delta(n)=\begin{cases}1&n=0\\0&n\neq0\end{cases},\qquad \varepsilon(n)=\sum_{m=-\infty}^n\delta(m)=\begin{cases}0&n<0\\1&n\ge0\end{cases},\qquad \varepsilon(n)\,a^n,\qquad \mathrm{e}^{\mathrm{j}2\pi Fn}.$$

Der __Einheitsimpuls__ $\delta(n)$ ist eine gewöhnliche Folge, keine Distribution: Er hat bei $n=0$ den Wert 1. Er ist das Einselement der diskreten Faltung, $s(n)*\delta(n)=s(n)$. Ein Rechteck aus $2M+1$ Einsen um $n=0$ ist $\varepsilon(n+M)-\varepsilon(n-M-1)$.

**Linear und verschiebungsinvariant.** Ein zeitdiskretes System heißt linear, wenn der Überlagerungssatz gilt, und __verschiebungsinvariant__, wenn $\operatorname{Tr}\{s(n-m)\}=g(n-m)$ für jede ganze Zahl $m$. Zusammen heißt es __LSI-System__. Mit der __Impulsantwort__ $h(n)=\operatorname{Tr}\{\delta(n)\}$ folgt wie in [Teil 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html):

$$g(n)=\operatorname{Tr}\Bigl\{\sum_ms(m)\delta(n-m)\Bigr\}=\sum_ms(m)\operatorname{Tr}\{\delta(n-m)\}=\sum_ms(m)\,h(n-m).$$

Hier braucht man keinen Grenzübergang: Eine Folge *ist* schon eine Summe gewichteter, verschobener Einheitsimpulse.

**Differenz und Summe.** Das Gegenstück zur Ableitung ist die __Differenz__ $g(n)=s(n)-s(n-1)$, also $h(n)=\delta(n)-\delta(n-1)$. Das Gegenstück zum Integral ist die __Akkumulation__ $g(n)=\sum_{m\le n}s(m)=s(n)*\varepsilon(n)$. Beide heben sich auf: $[\delta(n)-\delta(n-1)]*\varepsilon(n)=\varepsilon(n)-\varepsilon(n-1)=\delta(n)$.

**Differenzengleichungen, FIR und IIR.** Statt Differentialgleichungen beschreiben Differenzengleichungen zeitdiskrete Systeme:

<span class="anker" id="gl-5-2"></span>
$$g(n)=\underbrace{\sum_{q=0}^{Q}a_q\,s(n-q)}_{\text{FIR-Teil}}+\underbrace{\sum_{p=1}^{P}b_p\,g(n-p)}_{\text{IIR-Teil}}. \tag{5.2}$$

Der Ausgang ist eine gewichtete Summe vergangener Eingangs- und Ausgangswerte. Hängt er nur von Eingangswerten ab ($b_p=0$), ist die Impulsantwort nach $Q+1$ Werten zu Ende: ein __FIR-Filter__ (finite impulse response). Mit Rückkopplung ($b_p\neq0$) kann die Impulsantwort unendlich lang sein: ein __IIR-Filter__ (infinite impulse response). Gebaut wird beides aus Verzögerungsgliedern (Speicher für einen Takt), Multiplizierern und Addierern (Abb. [4](#abb-4)).

:::abbildung et3/k4block
System erster Ordnung $g(n)=a_0s(n)+a_1s(n-1)+b_1g(n-1)$. Das Kästchen $T$ speichert einen Wert für einen Takt. Links der nichtrekursive Teil, rechts die Rückkopplung des Ausgangs.
:::

:::aufgabe Aufgabe 4 ★ Diskrete Faltung von Hand
<span class="anker" id="aufg-4"></span>

Falte $s=(1,1,1)$ mit $h=(1,2)$, beide beginnend bei $n=0$. Wie lang ist das Ergebnis, und warum?

:::loesung
$g(0)=1$, $g(1)=1\cdot2+1\cdot1=3$, $g(2)=3$, $g(3)=1\cdot2=2$: $(1,3,3,2)$. Länge $3+2-1=4$: Der letzte von null verschiedene Wert entsteht, wenn der letzte Wert von $h$ auf den letzten Wert von $s$ trifft.
:::
:::

## Stufe 6: Ein rekursives System

<span class="anker" id="stufe-6"></span>

:::zweck
Am einfachsten IIR-System sieht man, wie Rückkopplung eine unendlich lange Impulsantwort erzeugt und wann das System stabil ist.
:::

Das System $g(n)=s(n)+b\,g(n-1)$ addiert zum Eingang den mit $b$ gewichteten letzten Ausgang. Für $s=\delta$ und Ruhe vor $n=0$:

<span class="anker" id="gl-6-1"></span>
$$h(n)=\delta(n)+b\,h(n-1)\quad\Longrightarrow\quad h(0)=1,\ h(1)=b,\ h(2)=b^2,\dots\quad\Longrightarrow\quad h(n)=\varepsilon(n)\,b^n. \tag{6.1}$$

Der Stoß läuft in der Rückkopplung immer wieder herum und wird jedes Mal mit $b$ multipliziert. Das System ist __kausal__ ($h(n)=0$ für $n<0$). Es ist __stabil__, wenn $\sum_n|h(n)|<\infty$ (das diskrete Gegenstück zu [Teil 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)), hier also genau für $|b|<1$, mit $\sum_n|b|^n=\frac{1}{1-|b|}$.

**Antwort auf eine Rechteckfolge.** Eingang $s(n)=\varepsilon(n)-\varepsilon(n-M)$ ($M$ Einsen). Mit der Faltungssumme und der geometrischen Summenformel $\sum_{k=0}^nq^k=\frac{1-q^{n+1}}{1-q}$:

<span class="anker" id="gl-6-2"></span>
$$g(n)=\begin{cases}0&n<0,\\[2pt]\displaystyle\sum_{m=0}^{n}b^{n-m}=\frac{1-b^{n+1}}{1-b}&0\le n<M,\\[8pt]\displaystyle\sum_{m=0}^{M-1}b^{n-m}=\frac{b^{n-M+1}-b^{n+1}}{1-b}&n\ge M.\end{cases} \tag{6.2}$$

Im Rechenmodell ($b=0{,}6$, $M=4$): $g=1;\ 1{,}6;\ 1{,}96;\ 2{,}176$, danach $1{,}306;\ 0{,}783;\ 0{,}470;\dots$, jeder Wert das 0,6-Fache des vorigen (Abb. [5](#abb-5)). Das ist das diskrete Gegenstück zur Rechteckantwort des RC-Glieds in [Teil 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html).

:::abbildung et3/k4rek
Das rekursive System mit $b=0{,}6$. Links die Impulsantwort. Rechts die Antwort auf vier Einsen: Sie steigt bis 2,176 an und klingt danach mit dem Faktor 0,6 je Takt ab.
:::

:::aufgabe Aufgabe 5 ★★ Das rekursive System untersuchen
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Bestätige die ersten fünf Werte von $g(n)$ im Rechenmodell direkt mit der Rekursion.

</li>

<li>

Gegen welchen Wert strebt der Ausgang bei einer unendlich langen Folge von Einsen ($M\to\infty$)? Vergleiche mit $\sum_nh(n)$.

</li>

<li>

Wie sieht $h(n)$ für $b=-0{,}6$ und für $b=1{,}1$ aus? Welches System ist stabil?

</li>

</ol>

:::loesung
(a) $g(0)=1$, $g(1)=1+0{,}6=1{,}6$, $g(2)=1+0{,}96=1{,}96$, $g(3)=1+1{,}176=2{,}176$, $g(4)=0+0{,}6\cdot2{,}176=1{,}306$.

(b) $\frac{1}{1-b}=2{,}5$. Das ist $\sum_nh(n)=\sum0{,}6^n=2{,}5$: Bei konstantem Eingang 1 summiert die Faltung alle Werte der Impulsantwort. Es ist auch $H_\mathrm a(0)=2{,}5$.

(c) $b=-0{,}6$: $1;\ -0{,}6;\ 0{,}36;\ -0{,}216;\dots$, wechselndes Vorzeichen, abklingend, stabil. $b=1{,}1$: $1;\ 1{,}1;\ 1{,}21;\dots$, wachsend, instabil.
:::
:::

:::aufgabe Aufgabe 6 ★★ System erster Ordnung
<span class="anker" id="aufg-6"></span>

$g(n)=s(n)+0{,}5\,s(n-1)+0{,}6\,g(n-1)$ (Abb. [4](#abb-4) mit $a_0=1$, $a_1=0{,}5$, $b_1=0{,}6$).

<ol class="al">

<li>

Berechne $h(0)$ bis $h(3)$ mit der Rekursion.

</li>

<li>

Zeige, dass $h(n)=\frac{11}{6}\,0{,}6^n\varepsilon(n)-\frac56\delta(n)$ ist.

</li>

</ol>

:::loesung
(a) $h(0)=1$, $h(1)=0{,}5+0{,}6\cdot1=1{,}1$, $h(2)=0{,}6\cdot1{,}1=0{,}66$, $h(3)=0{,}396$.

(b) Die Formel gibt $h(0)=\frac{11}{6}-\frac56=1$ und $h(1)=\frac{11}{6}\cdot0{,}6=1{,}1$. Ab $n=2$ ist der Eingang null, die Rekursion lautet $h(n)=0{,}6\,h(n-1)$, und die Formel erfüllt sie, weil $\frac{11}{6}0{,}6^n=0{,}6\cdot\frac{11}{6}0{,}6^{n-1}$. (Mit der z-Transformation folgt die Formel aus der Zerlegung $H(z)=-\frac56+\frac{11/6}{1-0{,}6z^{-1}}$.)
:::
:::

## Stufe 7: Fourier-Transformation zeitdiskreter Signale

<span class="anker" id="stufe-7"></span>

:::zweck
Welches Spektrum hat eine Zahlenfolge? Es ist das Spektrum des ideal abgetasteten Signals, direkt aus den Abtastwerten berechnet.
:::

Setzt man $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ in das Fourier-Integral ein, bleibt mit der Siebeigenschaft eine Summe. Normiert auf $T=1$:

:::satz Satz 7.1 (Fourier-Transformation zeitdiskreter Signale)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf},\qquad s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f. \tag{7.1}$$
:::

⁠**So liest man das:** $S_\mathrm a(f)$ ist periodisch mit der Periode 1, das ist die Abtastrate. Eine Periode, $|f|\le\frac12$, enthält alles. Deshalb integriert die Rücktransformation nur über ein Intervall der Länge 1. Die Summe ist eine Fourier-Reihe in $f$, mit den Abtastwerten als Koeffizienten.

**Beispiel.** Für $s(n)=\varepsilon(n)\,b^n$ mit $|b|<1$ (geometrische Reihe):

<span class="anker" id="gl-7-2"></span>
$$S_\mathrm a(f)=\sum_{n=0}^{\infty}\bigl(b\,\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)^n=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}},\qquad|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}. \tag{7.2}$$

Das ist zugleich der Frequenzgang $H_\mathrm a(f)$ des rekursiven Systems aus Stufe [6](#stufe-6). Für $b=0{,}6$: $|H_\mathrm a|=2{,}5$ bei $f=0$, $1{,}60$ bei $f=0{,}1$, $0{,}86$ bei $f=0{,}25$, $0{,}625$ bei $f=0{,}5$ (Abb. [6](#abb-6)). Das System ist ein Tiefpass, aber mit periodischem Frequenzgang: Bei $f=1$ verstärkt es wieder so stark wie bei $f=0$.

:::abbildung et3/k4dtft
Betrag des Frequenzgangs des rekursiven Systems mit $b=0{,}6$. Er ist periodisch mit der Abtastrate. Zwischen den roten Linien liegt die eine Periode, die alles beschreibt.
:::

**Faltung und Multiplikation.** Wie bei Funktionen gilt $s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$. Das Produkt zweier Folgen ergibt die __periodische Faltung__ der Spektren über eine Periode:

<span class="anker" id="gl-7-3"></span>
$$s(n)\cdot h(n)\;\circ\!\!-\!\!\bullet\;\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu. \tag{7.3}$$

:::aufgabe Aufgabe 7 ★ Gleitender Mittelwert
<span class="anker" id="aufg-7"></span>

$h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$ mittelt drei aufeinanderfolgende Werte.

<ol class="al">

<li>

Zeige $H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

</li>

<li>

Bei welcher Frequenz ist $H_\mathrm a=0$? Welche Schwingung löscht das Filter also vollständig aus, und warum (Tipp: Summe dreier Werte einer Schwingung mit der Periode 3)?

</li>

</ol>

:::loesung
(a) $\frac13\bigl(1+\mathrm{e}^{-\mathrm{j}2\pi f}+\mathrm{e}^{-\mathrm{j}4\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl(\mathrm{e}^{\mathrm{j}2\pi f}+1+\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

(b) $\cos(2\pi f)=-\frac12$, also $f=\frac13$ (bei $f_\mathrm A=1$ kHz: 333 Hz). Eine Schwingung mit drei Werten je Periode besteht aus drei Zeigern im Abstand $120^\circ$. Ihre Summe ist null, das Filter sieht in jedem Fenster genau eine ganze Periode.
:::
:::

## Stufe 8: Die diskrete Fourier-Transformation (DFT)

<span class="anker" id="stufe-8"></span>

:::zweck
$S_\mathrm a(f)$ ist eine stetige Funktion, ein Rechner braucht aber endlich viele Zahlen. Für eine Folge endlicher Länge genügen endlich viele Abtastwerte des Spektrums.
:::

**Die Idee.** Ist $s(n)$ auf $M$ Werte begrenzt, genügen nach Stufe [4](#stufe-4) Abtastwerte des Spektrums im Abstand $F=1/M$. Dazu gehört das mit $M$ periodisch wiederholte Signal $s_d(n)$. Weil auch das Spektrum periodisch ist (Zeit diskret), reichen $M$ Spektralwerte. Beide Seiten sind jetzt diskret und periodisch.

:::satz Satz 8.1 (Diskrete Fourier-Transformation)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
$$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\,\mathrm{e}^{-\mathrm{j}2\pi kn/M},\qquad s_d(n)=\frac1M\sum_{k=0}^{M-1}S_d(k)\,\mathrm{e}^{\mathrm{j}2\pi kn/M},\qquad k,n=0,\dots,M-1. \tag{8.1}$$
:::

⁠**So liest man das:** $S_d(k)$ ist der Wert des Spektrums $S_\mathrm a(f)$ bei $f=k/M$. Der Index $k$ zählt Schwingungen, die in die $M$ Werte genau $k$-mal passen. Die Rücktransformation ist eine Fourier-Reihe mit $M$ Gliedern. Die Theoreme gelten sinngemäß, etwa die Verschiebung $s_d(n-m)\;\circ\!\!-\!\!\bullet\;S_d(k)\mathrm{e}^{-\mathrm{j}2\pi mk/M}$ (zyklisch: Was hinten herausgeschoben wird, kommt vorne wieder herein) und Parseval $\sum_n|s_d(n)|^2=\frac1M\sum_k|S_d(k)|^2$.

**Beispiel.** $s_d=(1,\,2,\,0,\,-1)$, $M=4$, $\mathrm{e}^{-\mathrm{j}2\pi/4}=-\mathrm{j}$:

$$S_d(k)=\sum_{n=0}^{3}s_d(n)(-\mathrm{j})^{kn}:\qquad S_d(0)=2,\quad S_d(1)=1-3\mathrm{j},\quad S_d(2)=0,\quad S_d(3)=1+3\mathrm{j}.$$

Probe: $S_d(3)=S_d^*(1)$, weil das Signal reell ist ($k=3$ entspricht $k=-1$). Parseval: $1+4+0+1=6=\frac14(4+10+0+10)$.

:::aufgabe Aufgabe 8 ★★ DFT von Hand
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Rechne $S_d(1)$ für $s_d=(1,2,0,-1)$ nach.

</li>

<li>

Bestimme mit dem Verschiebungssatz die DFT der zyklisch verschobenen Folge $(-1,1,2,0)$ und prüfe $S_d(1)$ direkt.

</li>

</ol>

:::loesung
(a) $S_d(1)=1+2(-\mathrm{j})+0\cdot(-1)+(-1)(-\mathrm{j})^3=1-2\mathrm{j}-\mathrm{j}=1-3\mathrm{j}$, weil $(-\mathrm{j})^3=\mathrm{j}$.

(b) Verschiebung um $m=1$: $S_d(k)\,(-\mathrm{j})^k$, also $(2,\;(1-3\mathrm{j})(-\mathrm{j}),\;0,\;(1+3\mathrm{j})\mathrm{j})=(2,\;-3-\mathrm{j},\;0,\;-3+\mathrm{j})$. Direkt: $S_d(1)=-1+1\cdot(-\mathrm{j})+2\cdot(-1)+0=-3-\mathrm{j}$.
:::
:::

## Stufe 9: FFT und schnelle Faltung

<span class="anker" id="stufe-9"></span>

:::zweck
Die DFT braucht $M^2$ Multiplikationen. Die FFT kommt mit ungefähr $M\,\mathrm{lb}\,M$ aus. Damit wird auch die Faltung über den Frequenzbereich schnell.
:::

**Die Idee der FFT.** Mit $W_M=\mathrm{e}^{-\mathrm{j}2\pi/M}$ ist $S_d(k)=\sum_ns_d(n)W_M^{kn}$. Für gerades $M$ teilt man in Werte mit geradem und ungeradem Index:

<span class="anker" id="gl-9-1"></span>
$$S_d(k)=\underbrace{\sum_{n=0}^{M/2-1}s_d(2n)\,W_{M/2}^{kn}}_{S_{d,1}(k)}+W_M^k\underbrace{\sum_{n=0}^{M/2-1}s_d(2n+1)\,W_{M/2}^{kn}}_{S_{d,2}(k)}, \tag{9.1}$$

denn $W_M^{2kn}=W_{M/2}^{kn}$. Statt einer DFT der Länge $M$ braucht man zwei der Länge $M/2$ und $M$ Multiplikationen mit $W_M^k$, also $2(M/2)^2+M$ statt $M^2$. Beide Teil-DFTs sind periodisch mit $M/2$, deshalb liefern sie auch die Werte für $k\ge M/2$. Ist $M$ eine Zweierpotenz, wiederholt man die Teilung $\mathrm{lb}\,M$-mal. Der Aufwand sinkt auf etwa $M\,\mathrm{lb}\,M$. Bei $M=1024$ sind das 10 240 statt 1 048 576 Multiplikationen, rund hundertmal weniger. Das ist die __schnelle Fourier-Transformation__ (FFT).

**Zyklische Faltung.** Für periodische Folgen der Periode $M$ gilt die __zyklische__ (periodische) Faltung

<span class="anker" id="gl-9-2"></span>
$$g_d(n)=\sum_{m=0}^{M-1}s_d(m)\,h_d\bigl((n-m)\bmod M\bigr)\;\circ\!\!-\!\!\bullet\;G_d(k)=S_d(k)\,H_d(k). \tag{9.2}$$

Sie ist das periodisch wiederholte Ergebnis der gewöhnlichen Faltung. Ist $M$ zu klein, überlappen die Wiederholungen. Für $s=(1,1,1)$ und $h=(1,2)$ ist die gewöhnliche Faltung $(1,3,3,2)$ mit vier Werten. Mit $M=3$ fällt der letzte Wert auf den ersten: $(3,3,3)$. Mit $M=4$ stimmt es: $(1,3,3,2)$. Allgemein muss $M\ge M_1+M_2-1$ sein ($M_1$, $M_2$: Längen der beiden Folgen), dazu füllt man mit Nullen auf.

**Schnelle Faltung.** Statt die Faltungssumme direkt auszurechnen, transformiert man beide Folgen mit der FFT, multipliziert und transformiert zurück. Ein beliebig langes Signal zerlegt man in Blöcke, faltet jeden Block einzeln und addiert die Ergebnisse. Das ist erlaubt, weil die Faltung distributiv ist:

$$s(n)*h(n)=\Bigl[\sum_is_i(n)\Bigr]*h(n)=\sum_i\bigl[s_i(n)*h(n)\bigr].$$

:::aufgabe Aufgabe 9 ★★ Zyklisch oder linear
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Rechne die zyklische Faltung von $(1,1,1)$ und $(1,2,0)$ mit $M=3$ von Hand. Welcher Wert der linearen Faltung ist wohin gewandert?

</li>

<li>

Ein Signal mit 1000 Werten soll mit einem Filter mit 25 Werten über die DFT gefaltet werden. Wie lang muss die DFT mindestens sein?

</li>

</ol>

:::loesung
(a) $g(0)=s_0h_0+s_1h_2+s_2h_1=1+0+2=3$, $g(1)=s_0h_1+s_1h_0+s_2h_2=2+1+0=3$, $g(2)=s_0h_2+s_1h_1+s_2h_0=0+2+1=3$. Der vierte Wert der linearen Faltung (2 bei $n=3$) ist zyklisch auf $n=0$ gewandert: $1+2=3$.

(b) Mindestens $1000+25-1=1024$. Das ist praktischerweise eine Zweierpotenz.
:::
:::

## Stufe 10: Abtastrate ändern, Dezimation und Interpolation

<span class="anker" id="stufe-10"></span>

:::zweck
Eine Folge lässt sich nachträglich mit niedrigerer oder höherer Rate darstellen. Für das Spektrum gelten dieselben Regeln wie beim ersten Abtasten.
:::

**Herabtasten um den Faktor $c$.** Man behält nur jeden $c$-ten Wert. Gedanklich erst mit einem Kamm aus Einheitsimpulsen multiplizieren, dann die Nullen weglassen:

$$s_c(n)=s(n)\sum_m\delta(n-mc),\qquad s_u(n)=s(nc).$$

Die Multiplikation mit dem Kamm erzeugt $c$ Kopien des Spektrums im Abstand $1/c$, das Weglassen der Nullen dehnt die Frequenzachse um $c$:

<span class="anker" id="gl-10-1"></span>
$$S_{c,\mathrm a}(f)=\frac1c\sum_{k=0}^{c-1}S_\mathrm a\Bigl(f-\frac kc\Bigr),\qquad S_{u,\mathrm a}(f)=S_{c,\mathrm a}\Bigl(\frac fc\Bigr). \tag{10.1}$$

Reicht das Spektrum bis $f_\mathrm g$ (bezogen auf die alte Rate), reicht es nach dem Herabtasten bis $cf_\mathrm g$. Kein Aliasing gibt es nur, wenn $cf_\mathrm g\le\frac12$. Sonst muss vorher ein digitaler Tiefpass das Band begrenzen.

**Hochtasten um den Faktor $c$.** Man fügt zwischen je zwei Werte $c-1$ Nullen ein, $s_\uparrow(n)=s(n/c)$ für durch $c$ teilbare $n$, sonst 0. Das Spektrum wird um $c$ gestaucht, $S_{\uparrow,\mathrm a}(f)=S_\mathrm a(cf)$, und enthält jetzt $c-1$ Spiegelspektren in der Periode. Ein Tiefpass mit der Grenzfrequenz $\frac{1}{2c}$ und der Verstärkung $c$ entfernt sie. Dabei füllt er die Nullen mit interpolierten Werten (die si-Interpolation aus Stufe [3](#stufe-3) in diskreter Form), die ursprünglichen Werte bleiben erhalten. Herab- und Hochtasten nacheinander ändern die Rate um einen rationalen Faktor $c_1/c_2$.

:::abbildung et3/k4rate
Spektren (Frequenz bezogen auf die jeweilige Rate) beim Ändern der Abtastrate. Herabtasten dehnt das Band, Hochtasten staucht es und erzeugt Spiegelspektren, die ein Interpolationsfilter entfernt.
:::

:::aufgabe Aufgabe 10 ★★ Herabtasten
<span class="anker" id="aufg-10"></span>

Eine Folge hat ein Spektrum bis $f_\mathrm g=0{,}2$.

<ol class="al">

<li>

Darf man sie ohne Vorfilter um $c=2$ herabtasten? Um $c=3$?

</li>

<li>

Was muss vor dem Herabtasten um $c=3$ geschehen, und was verliert man dabei?

</li>

</ol>

:::loesung
(a) $c=2$: Das Band reicht danach bis $0{,}4\le0{,}5$, kein Aliasing. $c=3$: bis $0{,}6>0{,}5$, Aliasing.

(b) Vorher mit einem digitalen Tiefpass auf $\frac{1}{2c}=\frac16\approx0{,}167$ begrenzen. Die Anteile zwischen 0,167 und 0,2 gehen dabei verloren. Das ist der Preis der niedrigeren Rate.
:::
:::

## Stufe 11: Die z-Transformation

<span class="anker" id="stufe-11"></span>

:::zweck
Wie die Laplace-Transformation die Fourier-Transformation erweitert ([Teil 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)), so erweitert die z-Transformation die Fourier-Transformation zeitdiskreter Signale: erst exponentiell gewichten, dann transformieren.
:::

**Die Idee.** Man multipliziert die Folge mit $\rho^{-n}$ ($\rho>0$) und transformiert: $\sum_ns(n)\rho^{-n}\mathrm{e}^{-\mathrm{j}2\pi fn}$. Mit $z=\rho\,\mathrm{e}^{\mathrm{j}2\pi f}$ wird daraus eine Potenzreihe in $z^{-1}$. Gleichwertig: $z^n$ ist eine Eigenfunktion jedes LSI-Systems, denn $z^{n-k}=z^{-k}z^n$, und der Eigenwert ist $H(z)$:

$$z^n*h(n)=\sum_kh(k)z^{n-k}=z^n\sum_kh(k)z^{-k}=H(z)\,z^n.$$

:::satz Satz 11.1 (z-Transformation)
<span class="anker" id="satz-11-1"></span>

<span class="anker" id="gl-11-1"></span>
$$S(z)=\sum_{n=-\infty}^{\infty}s(n)\,z^{-n},\qquad s(n)=\frac{1}{2\pi\mathrm{j}}\oint S(z)\,z^{n-1}\,\mathrm{d} z, \tag{11.1}$$

wobei das Kurvenintegral einen Kreis $|z|=\rho$ im Konvergenzbereich gegen den Uhrzeigersinn umläuft.
:::

⁠**So liest man das:** Auf dem Kreis $|z|=\rho$ steht eine Periode des Spektrums der gewichteten Folge $s(n)\rho^{-n}$. Auf dem __Einheitskreis__ $|z|=1$ ist $S(z)$ das gewöhnliche Spektrum $S_\mathrm a(f)$, sofern er im Konvergenzbereich liegt. Die Ebene der Laplace-Transformation wird so auf die z-Ebene abgebildet: Die imaginäre Achse wird zum Einheitskreis, die linke Halbebene zu seinem Inneren.

**Grundpaare und Konvergenzbereich.** Mit der geometrischen Reihe:

<span class="anker" id="gl-11-2"></span>
$$\varepsilon(n)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{1}{1-bz^{-1}}=\frac{z}{z-b},\quad|z|>|b|;\qquad -\varepsilon(-n-1)\,b^n\;\circ\!\!-\!\!\bullet\;\frac{z}{z-b},\quad|z|<|b|. \tag{11.2}$$

Wie bei Laplace gehört derselbe Ausdruck zu zwei Signalen, erst der Konvergenzbereich entscheidet. Bei rechtsseitigen Folgen liegt er außerhalb des Kreises durch den äußersten Pol, bei linksseitigen innerhalb des Kreises durch den innersten Pol, bei zweiseitigen ist er ein Ring. Für $b^{|n|}$ mit $0<b<1$ ist das der Ring $b<|z|<1/b$.

**Rechenregeln.** Faltung wird Produkt: $g=s*h\;\circ\!\!-\!\!\bullet\;G(z)=S(z)H(z)$. Verzögerung um $n_0$ Takte wird Multiplikation mit $z^{-n_0}$. Damit wird aus der Differenzengleichung [(5.2)](#gl-5-2)

<span class="anker" id="gl-11-3"></span>
$$H(z)=\frac{G(z)}{S(z)}=\frac{\sum_{q=0}^{Q}a_q\,z^{-q}}{1-\sum_{p=1}^{P}b_p\,z^{-p}}. \tag{11.3}$$

Für das System aus Aufgabe [6](#aufg-6) ist $H(z)=\frac{1+0{,}5z^{-1}}{1-0{,}6z^{-1}}$: Nullstelle bei $z=-0{,}5$, Pol bei $z=0{,}6$.

:::satz Satz 11.2 (Stabilität)
<span class="anker" id="satz-11-2"></span>

Ein kausales LSI-System ist genau dann stabil, wenn alle Pole von $H(z)$ im Inneren des Einheitskreises liegen.
:::

⁠**Warum:** Kausal heißt Konvergenzbereich außerhalb des äußersten Pols. Stabil heißt $\sum|h(n)|<\infty$, dann konvergiert $H(z)$ auf dem Einheitskreis, er gehört also zum Konvergenzbereich. Beides zusammen geht nur, wenn der äußerste Pol innerhalb des Einheitskreises liegt. Für das rekursive System mit $H(z)=\frac{1}{1-bz^{-1}}$ heißt das wieder $|b|<1$.

**Beispiel.** $s(n)=0{,}5^n\cos(\pi n/3)\,\varepsilon(n)$. Mit $\cos=\frac12(\mathrm{e}^{\mathrm{j}\pi n/3}+\mathrm{e}^{-\mathrm{j}\pi n/3})$ und [(11.2)](#gl-11-2) für $b=0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}$:

$$S(z)=\frac12\Bigl[\frac{1}{1-0{,}5\mathrm{e}^{\mathrm{j}\pi/3}z^{-1}}+\frac{1}{1-0{,}5\mathrm{e}^{-\mathrm{j}\pi/3}z^{-1}}\Bigr]=\frac{1-0{,}25z^{-1}}{1-0{,}5z^{-1}+0{,}25z^{-2}},\qquad|z|>0{,}5.$$

Pole bei $0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}=0{,}25\pm0{,}433\mathrm{j}$, Nullstellen bei $z=0$ und $z=0{,}25$ (Abb. [8](#abb-8)). Der Betrag der Pole gibt das Abklingen je Takt an (0,5), ihr Winkel die Schwingung ($\pi/3$ je Takt, also sechs Takte je Periode).

:::abbildung et3/k4zebene
z-Ebene des Beispiels: Pole (Kreuze) bei $0{,}5\mathrm{e}^{\pm\mathrm{j}\pi/3}$, Nullstellen (Kreise) bei 0 und 0,25. Der Konvergenzbereich (blau) liegt außerhalb des Kreises durch die Pole und enthält den Einheitskreis. Als Impulsantwort gelesen, beschreibt die Folge ein kausales und stabiles System.
:::

:::aufgabe Aufgabe 11 ★★ z-Transformation anwenden
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Bestätige den Zähler und Nenner von $S(z)$ im Beispiel, indem du die beiden Brüche auf den Hauptnenner bringst.

</li>

<li>

Existiert das Spektrum $S_\mathrm a(f)$ des Beispielsignals? Begründe mit dem Konvergenzbereich.

</li>

</ol>

:::loesung
(a) Hauptnenner $(1-az^{-1})(1-a^*z^{-1})=1-(a+a^*)z^{-1}+|a|^2z^{-2}$ mit $a=0{,}5\mathrm{e}^{\mathrm{j}\pi/3}$: $a+a^*=2\cdot0{,}25=0{,}5$, $|a|^2=0{,}25$. Zähler $\frac12[2-(a+a^*)z^{-1}]=1-0{,}25z^{-1}$.

(b) Ja. Der Konvergenzbereich $|z|>0{,}5$ enthält den Einheitskreis.
:::
:::

:::aufgabe Aufgabe 12 ★★ Kausal oder stabil
<span class="anker" id="aufg-12"></span>

$H(z)=\dfrac{1}{1-2z^{-1}}$.

<ol class="al">

<li>

Welche Impulsantwort gehört zum Konvergenzbereich $|z|>2$, welche zu $|z|<2$?

</li>

<li>

Welche der beiden ist stabil, welche kausal? Gibt es eine, die beides ist?

</li>

</ol>

:::loesung
(a) $|z|>2$: $h(n)=2^n\varepsilon(n)$. $|z|<2$: $h(n)=-2^n\varepsilon(-n-1)$, also $-\frac12,-\frac14,\dots$ für $n=-1,-2,\dots$

(b) Die erste ist kausal, aber instabil (wächst). Die zweite ist stabil ($\sum_{n\le-1}2^n=1$), aber antikausal. Beides zugleich geht nicht: Der Pol bei $z=2$ liegt außerhalb des Einheitskreises, und dann kann der Konvergenzbereich nicht zugleich außerhalb des Pols liegen und den Einheitskreis enthalten.
:::
:::

:::kern Das Wichtigste
<ul>

<li>

Ideale Abtastung: $s_\mathrm a=\sum s(nT)\delta(t-nT)$; Spektrum $\frac1T\sum_kS(f-k/T)$, periodisch mit $1/T$.

</li>

<li>

Abtasttheorem: $f_\mathrm A\ge2f_\mathrm g$; Rückgewinnung $s(t)=\sum s(nT)\operatorname{si}(\pi(t-nT)/T)$; sonst Aliasing.

</li>

<li>

Diskret im einen Bereich heißt periodisch im anderen.

</li>

<li>

Diskrete Faltung $g(n)=\sum_ms(m)h(n-m)$; $h(n)=\operatorname{Tr}\{\delta(n)\}$; stabil: $\sum|h(n)|<\infty$.

</li>

<li>

Rekursiv $g(n)=s(n)+bg(n-1)$: $h(n)=b^n\varepsilon(n)$, $H_\mathrm a=\frac{1}{1-b\mathrm{e}^{-\mathrm{j}2\pi f}}$.

</li>

<li>

$S_\mathrm a(f)=\sum s(n)\mathrm{e}^{-\mathrm{j}2\pi nf}$, Periode 1; $s(n)=\int_{-1/2}^{1/2}S_\mathrm a\mathrm{e}^{\mathrm{j}2\pi nf}\mathrm{d} f$.

</li>

<li>

DFT: $S_d(k)=\sum_{n=0}^{M-1}s_d(n)\mathrm{e}^{-\mathrm{j}2\pi kn/M}$, $s_d=\frac1M\sum S_d\mathrm{e}^{\mathrm{j}2\pi kn/M}$; FFT $\approx M\,\mathrm{lb}\,M$; zyklische Faltung $\leftrightarrow S_dH_d$.

</li>

<li>

Herabtasten dehnt das Band (Aliasing, wenn $cf_\mathrm g>\frac12$), Hochtasten erzeugt Spiegelspektren.

</li>

<li>

$S(z)=\sum s(n)z^{-n}$; $z^{-n_0}$ = Verzögerung; $H(z)=\frac{\sum a_qz^{-q}}{1-\sum b_pz^{-p}}$; kausal und stabil: alle Pole in $|z|<1$.

</li>

</ul>
:::
