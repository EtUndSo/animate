---
title: Stufe 10: Kurzzeit-Fourier-Transformation
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3231100
summary: Das Spektrum S(f) beschreibt ein Signal über alle Zeiten.
tags: Hann-Fenster, Spektrogramm
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Das Spektrum $S(f)$ beschreibt ein Signal über alle Zeiten. Sprache oder Musik ändern ihre Frequenzen aber laufend. Die Kurzzeit-Fourier-Transformation fragt: Welche Frequenzen enthält das Signal *um den Zeitpunkt $t$*?
:::

**Die Idee.** Man schneidet um $t$ einen Ausschnitt heraus und transformiert nur ihn. Mit einem Rechteckfenster der Breite $T_0$:

$$s_T(\tau,t)=s(\tau)\operatorname{rect}\Bigl(\frac{\tau-t}{T_0}\Bigr)\;\circ\!\!-\!\!\bullet\;S_T(f,t)=S(f)*\bigl[T_0\operatorname{si}(\pi T_0f)\,\mathrm{e}^{-\mathrm{j}2\pi tf}\bigr].$$

Das Spektrum des Ausschnitts ist das wahre Spektrum, verschmiert mit dem si-Spektrum des Fensters. Ein kurzes Fenster lokalisiert gut in der Zeit, verschmiert aber stark in der Frequenz (Ähnlichkeitssatz). Die harten Kanten des Rechtecks erzeugen zudem langsam abfallende Nebenzipfel. Weiche Fenster sind deshalb besser, zum Beispiel das __Hann-Fenster__

<span class="anker" id="gl-10-1"></span>
$$w(\tau)=\tfrac12\Bigl[1+\cos\Bigl(\frac{2\pi\tau}{T_0}\Bigr)\Bigr]\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)=\cos^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr). \tag{10.1}$$

:::satz Satz 10.1 (Kurzzeit-Fourier-Transformation)
<span class="anker" id="satz-10-1"></span>

<span class="anker" id="gl-10-2"></span>
$$S_T(f,t)=\int_{-\infty}^{\infty}s(\tau)\,w(\tau-t)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau. \tag{10.2}$$

Ergänzen sich die um $T$ verschobenen Fenster zu einer Konstanten, $\sum_nw(\tau-nT)=c$, dann gilt

<span class="anker" id="gl-10-3"></span>
$$s(\tau)=\frac1c\sum_ns(\tau)\,w(\tau-nT),\qquad S(f)=\frac1c\sum_nS_T(f,nT). \tag{10.3}$$
:::

⁠**So liest man das:** $S_T(f,t)$ ist ein Spektrum, das von der Zeit abhängt. Trägt man $|S_T|$ über $t$ und $f$ auf, entsteht ein __Spektrogramm__. Beim Hann-Fenster mit dem Versatz $T=T_0/2$ ist $c=1$, weil $\cos^2x+\sin^2x=1$ ist (Abb. [8](#abb-8)): Die Ausschnitte setzen sich lückenlos zum ganzen Signal zusammen, und die Summe ihrer Spektren ist das ganze Spektrum.

:::abbildung et3/k3hann 8
Hann-Fenster der Breite $T_0=2$ s, jeweils um $T=1$ s versetzt (blau). Ihre Summe ist überall genau 1 (rot).
:::

:::aufgabe Aufgabe 13 ★ Hann-Fenster
<span class="anker" id="aufg-13"></span>

Zeige: Für $T=T_0/2$ ist $\sum_nw(\tau-nT)=1$. Tipp: In jedem Punkt überlappen genau zwei Fenster. Schreibe das zweite mit $\cos^2(x-\frac\pi2)$.

:::loesung
Für $\tau$ zwischen $nT$ und $(n+1)T$ mit $T=T_0/2$ sind genau die Fenster $n$ und $n+1$ von null verschieden. Mit $x=\pi(\tau-nT)/T_0$:

$$w(\tau-nT)+w(\tau-(n+1)T)=\cos^2x+\cos^2\Bigl(x-\frac\pi2\Bigr)=\cos^2x+\sin^2x=1.$$
:::
:::

::::kurzfassung
Das Spektrum $S(f)$ beschreibt ein Signal über alle Zeiten. Die Kurzzeit-Fourier-Transformation fragt dagegen, welche Frequenzen das Signal um einen bestimmten Zeitpunkt $t$ enthält.

Man schneidet mit einem __Fenster__ $w$ einen Ausschnitt um $t$ heraus und transformiert nur ihn. Das ergibt die __Kurzzeit-Fourier-Transformation__

$$S_T(f,t)=\int_{-\infty}^{\infty}s(\tau)\,w(\tau-t)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau,$$

ein Spektrum, das von der Zeit abhängt. Dabei ist $\tau$ die Zeit des Signals und $t$ die Lage des Fensters. Trägt man $|S_T|$ über $t$ und $f$ auf, entsteht ein __Spektrogramm__. Ergänzen sich die um $T$ verschobenen Fenster zu einer Konstanten, $\sum_nw(\tau-nT)=c$, setzen sich die Ausschnitte lückenlos zum Signal zusammen, und es gilt $S(f)=\frac1c\sum_nS_T(f,nT)$. Das weiche __Hann-Fenster__ der Breite $T_0$, $w(\tau)=\cos^2\bigl(\frac{\pi\tau}{T_0}\bigr)\operatorname{rect}\bigl(\frac{\tau}{T_0}\bigr)$, erfüllt das mit $T=T_0/2$ und $c=1$.

Der Grund für die Verschmierung: Das Fenster multipliziert das Signal, im Frequenzbereich wird also das Spektrum mit dem Spektrum des Fensters gefaltet. Beim Rechteckfenster der Breite $T_0$ ist das $T_0\operatorname{si}(\pi T_0f)$. Seine harten Kanten erzeugen langsam abfallende __Nebenzipfel__, die Nebenmaxima neben dem Hauptmaximum; weiche Fenster dämpfen sie.

Falle: Ein kurzes Fenster lokalisiert gut in der Zeit, verschmiert aber stark in der Frequenz, denn nach dem Ähnlichkeitssatz ist sein Spektrum breit. Beides zugleich beliebig scharf geht nicht.
::::

::::formelsammlung
**Ausschnitt mit Rechteckfenster**

$$s_T(\tau,t)=s(\tau)\operatorname{rect}\Bigl(\frac{\tau-t}{T_0}\Bigr)\;\circ\!\!-\!\!\bullet\;S_T(f,t)=S(f)*\bigl[T_0\operatorname{si}(\pi T_0f)\,\mathrm{e}^{-\mathrm{j}2\pi tf}\bigr]$$

Fenster der Breite $T_0$ um den Zeitpunkt $t$, transformiert wird nach $\tau$. Das wahre Spektrum wird mit dem si-Spektrum des Fensters verschmiert; ein kurzes Fenster lokalisiert gut in der Zeit und verschmiert stark in der Frequenz.

**Hann-Fenster**

$$w(\tau)=\tfrac12\Bigl[1+\cos\Bigl(\frac{2\pi\tau}{T_0}\Bigr)\Bigr]\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)=\cos^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)$$

Breite $T_0$. Weiche Kanten statt der harten Kanten des Rechtecks, deshalb schneller abfallende Nebenzipfel.

**Kurzzeit-Fourier-Transformation**

$$S_T(f,t)=\int_{-\infty}^{\infty}s(\tau)\,w(\tau-t)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau$$

Fenster $w$, um $t$ verschoben. $|S_T|$ über $t$ und $f$ aufgetragen ergibt das Spektrogramm.

**Zusammensetzen aus Ausschnitten**

$$s(\tau)=\frac1c\sum_ns(\tau)\,w(\tau-nT),\qquad S(f)=\frac1c\sum_nS_T(f,nT)$$

Bedingung: Die um $T$ verschobenen Fenster ergänzen sich zu einer Konstanten, $\sum_nw(\tau-nT)=c$.

**Hann-Fenster mit halbem Versatz**

$$\sum_nw(\tau-nT)=1$$

Für $T=T_0/2$, also $c=1$, weil $\cos^2x+\sin^2x=1$.
::::

::::lernkarten
:::karte begriff Kurzzeit-Fourier-Transformation
Was berechnet die Kurzzeit-Fourier-Transformation $S_T(f,t)$ eines Signals, und wie ist sie definiert?
---
Das Spektrum eines Ausschnitts um den Zeitpunkt $t$: $S_T(f,t)=\int_{-\infty}^{\infty}s(\tau)\,w(\tau-t)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau$. Das Fenster $w$ wird um $t$ verschoben, $\tau$ ist die Zeit des Signals. Es entsteht ein Spektrum, das von der Zeit abhängt.
--- falsch
Das Spektrum des ganzen Signals, ausgewertet zur Zeit $t$: $S_T(f,t)=S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}$. Es beschreibt, welchen Wert jede Schwingung zum Zeitpunkt $t$ hat, und kommt deshalb ganz ohne Fenster aus.
--- falsch
Das Spektrum eines Ausschnitts um den Zeitpunkt $t$: $S_T(f,t)=\int_{-\infty}^{\infty}s(\tau-t)\,w(\tau)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d}\tau$. Das Signal wird um $t$ verschoben, das Fenster bleibt fest, und im Exponenten steht die Lage $t$ des Ausschnitts.
--- falsch
Die Fourier-Transformation eines kurzen Signals, das nur zwischen $0$ und $T$ von null verschieden ist: $S_T(f)=\int_0^Ts(\tau)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau$. Für lange Signale ist sie nicht erklärt, sie braucht ein kurzes Signal.
:::
:::karte begriff Fenster
Welche Aufgabe hat das Fenster $w$ bei der Kurzzeit-Fourier-Transformation, und welches ist das einfachste?
---
Mit dem Fenster multipliziert man das Signal, um einen Ausschnitt um den Zeitpunkt $t$ herauszuschneiden; nur dieser wird transformiert. Das einfachste ist das Rechteckfenster der Breite $T_0$, $\operatorname{rect}\Bigl(\frac{\tau-t}{T_0}\Bigr)$.
--- falsch
Mit dem Fenster faltet man das Signal, um es zu glätten; transformiert wird danach das ganze geglättete Signal über alle Zeiten. Das einfachste ist das Rechteckfenster, das jeweils über die Breite $T_0$ mittelt.
--- falsch
Mit dem Fenster multipliziert man das Spektrum, um ein Frequenzband herauszuschneiden; nur dieses wird zurücktransformiert. Das einfachste ist das Rechteck $\operatorname{rect}(f/T_0)$ der Breite $T_0$ um die Frequenz null.
--- falsch
Mit dem Fenster addiert man zum Signal eine Rampe, damit es an den Rändern des Ausschnitts auf null abfällt. Das einfachste ist das Dreieckfenster, weil es die Ränder des Ausschnitts gleichmäßig linear absenkt.
:::
:::karte zusammenhang Verschmierung durch das Fenster
Warum ist das Spektrum eines Ausschnitts nicht das wahre Spektrum $S(f)$, sondern eine verschmierte Fassung davon?
---
Das Fenster multipliziert das Signal, im Frequenzbereich wird das Spektrum also mit dem Spektrum des Fensters gefaltet. Beim Rechteckfenster ist $S_T(f,t)=S(f)*\bigl[T_0\operatorname{si}(\pi T_0f)\,\mathrm{e}^{-\mathrm{j}2\pi tf}\bigr]$.
--- falsch
Weil der Ausschnitt weniger Energie enthält als das ganze Signal. Das Spektrum wird deshalb gleichmäßig um den Faktor $T_0$ kleiner, behält aber seine Form, und Linien im Spektrum bleiben scharfe Linien.
--- falsch
Das Fenster multipliziert das Signal, im Frequenzbereich wird das Spektrum also mit dem Spektrum des Fensters multipliziert: Bei den Nullstellen der si-Funktion des Rechteckfensters fehlen deshalb Frequenzen ganz.
--- falsch
Weil man nur über eine endliche Zeit integriert und das Integral deshalb nicht konvergiert. Die Verschmierung ist ein Rundungsfehler, der mit feinerer Abtastung des Ausschnitts beliebig klein wird.
:::
:::karte zusammenhang Kurzes und langes Fenster
Was passiert mit der Auflösung in Zeit und Frequenz, wenn man das Fenster der Kurzzeit-Fourier-Transformation kürzer macht?
---
Die Zeitauflösung wird besser, die Frequenzauflösung schlechter: Nach dem Ähnlichkeitssatz hat ein kurzes Fenster ein breites Spektrum und verschmiert das wahre Spektrum stark. Beides zugleich beliebig scharf geht nicht.
--- falsch
Beide Auflösungen werden besser: Ein kurzes Fenster lokalisiert genauer in der Zeit, und weil es weniger Signal enthält, sind auch weniger Frequenzen überlagert, sodass das Spektrum des Ausschnitts schärfer wird.
--- falsch
Die Frequenzauflösung wird besser, die Zeitauflösung schlechter: Ein kurzes Fenster hat nach dem Ähnlichkeitssatz ein schmales Spektrum, verschmiert also wenig, verwischt aber die Lage in der Zeit.
--- falsch
Nur die Zeitauflösung ändert sich; die Frequenzauflösung hängt allein von der Form des Fensters ab, nicht von seiner Länge. Ein kurzes Hann-Fenster trennt Frequenzen deshalb genauso gut wie ein langes.
:::
:::karte begriff Nebenzipfel
Was sind Nebenzipfel im Spektrum eines Fensters, und warum erzeugt das Rechteckfenster besonders störende?
---
Die Nebenmaxima neben dem Hauptmaximum des Fensterspektrums. Die harten Kanten des Rechtecks erzeugen langsam abfallende Nebenzipfel; weiche Fenster wie das Hann-Fenster dämpfen sie.
--- falsch
Die Nebenmaxima neben dem Hauptmaximum des Fensterspektrums. Das Rechteckfenster erzeugt besonders störende, weil es zu kurz ist; ein längeres Rechteckfenster hat gar keine Nebenzipfel mehr.
--- falsch
Die Teile des Signals, die außerhalb des Fensters liegen und deshalb im Ausschnitt fehlen. Beim Rechteckfenster sind sie besonders groß, weil es keine Übergangszone zwischen innen und außen hat.
--- falsch
Die Nullstellen des Fensterspektrums zwischen den Maxima. Das Rechteckfenster erzeugt besonders viele davon, weil seine Kanten senkrecht sind; weiche Fenster haben dagegen keine Nullstellen.
:::
:::karte begriff Hann-Fenster
Wie ist das Hann-Fenster der Breite $T_0$ definiert, und warum ist es dem Rechteckfenster meist vorzuziehen?
---
$w(\tau)=\tfrac12\Bigl[1+\cos\Bigl(\frac{2\pi\tau}{T_0}\Bigr)\Bigr]\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)=\cos^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)$. Es hat weiche statt harter Kanten, deshalb fallen seine Nebenzipfel schneller ab.
--- falsch
$w(\tau)=\cos\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)$, eine halbe Kosinuswelle. Es ist schmaler als das Rechteckfenster gleicher Breite, deshalb lokalisiert es zugleich besser in der Zeit und in der Frequenz.
--- falsch
$w(\tau)=\tfrac12\Bigl[1-\cos\Bigl(\frac{2\pi\tau}{T_0}\Bigr)\Bigr]\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)=\sin^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)$. Es betont die Ränder des Ausschnitts.
--- falsch
$w(\tau)=\Lambda\Bigl(\frac{\tau}{T_0}\Bigr)$, ein Dreieck. Es hat Knicke statt Sprüngen und ist deshalb besser als das Rechteck, aber seine Nebenzipfel fallen noch langsamer ab als beim Rechteck, weil es spitz zuläuft.
:::
:::karte formel Zusammensetzen aus Ausschnitten
Unter welcher Bedingung setzen sich die Ausschnitte der Kurzzeit-Fourier-Transformation wieder zum ganzen Signal und ihre Spektren zum ganzen Spektrum zusammen?
---
Wenn sich die um $T$ verschobenen Fenster zu einer Konstanten ergänzen, $\sum_nw(\tau-nT)=c$. Dann ist $s(\tau)=\frac1c\sum_ns(\tau)\,w(\tau-nT)$ und $S(f)=\frac1c\sum_nS_T(f,nT)$.
--- falsch
Wenn sich die um $T$ verschobenen Fenster nirgends überlappen. Dann ist $S(f)=\sum_nS_T(f,nT)$, allerdings nur für das Rechteckfenster, weil sich weiche Fenster immer überlappen und Teile doppelt zählen würden.
--- falsch
Wenn jedes Fenster die Fläche 1 hat, das Integral über $w$ also 1 ist. Dann ist $S(f)=\sum_nS_T(f,nT)$ für jeden beliebigen Versatz $T$, weil jeder Ausschnitt genau sein Gewicht beiträgt.
--- falsch
Wenn sich die um $T$ verschobenen Fenster zu einer Konstanten ergänzen, $\sum_nw(\tau-nT)=c$. Dann ist $S(f)=c\sum_nS_T(f,nT)$, denn die Summe der Fenster multipliziert das Signal mit $c$.
:::
:::karte herleitung Hann-Fenster mit halbem Versatz
Wie zeigt man, dass sich Hann-Fenster der Breite $T_0$ mit dem Versatz $T=T_0/2$ überall zu 1 ergänzen?
---
Zwischen $nT$ und $(n+1)T$ sind genau die Fenster $n$ und $n+1$ von null verschieden, weil jedes Fenster doppelt so breit ist wie der Versatz.
---
Mit $x=\pi(\tau-nT)/T_0$ ist das erste Fenster $\cos^2x$, weil das Hann-Fenster $\cos^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)$ ist, hier um $nT$ verschoben.
---
Das zweite Fenster ist $\cos^2\Bigl(x-\frac\pi2\Bigr)$, also $\sin^2x$, weil es um $T=T_0/2$ weiter verschoben ist und das im Argument $\frac\pi2$ ausmacht.
---
Die Summe ist $\cos^2x+\sin^2x=1$, weil das für jeden Winkel gilt. Also ist $c=1$, und die Ausschnitte setzen sich lückenlos zusammen.
:::
:::karte begriff Spektrogramm
Was zeigt ein Spektrogramm, und woraus entsteht es?
---
Wie sich die Frequenzen eines Signals mit der Zeit ändern: Man trägt den Betrag $|S_T|$ der Kurzzeit-Fourier-Transformation über der Zeit $t$ und der Frequenz $f$ auf.
--- falsch
Wie sich die Frequenzen eines Signals mit der Zeit ändern: Man trägt das Signal über der Zeit und darunter seinen Spektralbetrag $|S(f)|$ über der Frequenz auf, beide getrennt.
--- falsch
Welche Leistung jede Harmonische eines periodischen Signals trägt: Man trägt $|S_p(k)|^2$ über der Nummer $k$ auf, als Balken bei den Vielfachen der Grundfrequenz.
--- falsch
Wie sich die Phase des Spektrums über der Frequenz ändert: Man trägt den Winkel von $S(f)$ über $f$ auf und liest an der Steigung die Verzögerung des Signals ab.
:::
::::
