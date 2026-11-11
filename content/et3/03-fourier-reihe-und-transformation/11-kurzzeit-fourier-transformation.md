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
