---
title: Stufe 9: Bandpasssignal durch Bandpasssystem
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Tiefpass- und Bandpasssysteme
adresse: elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme
knoten: Kapitel 5: Tiefpass- und Bandpasssysteme
order: 3251000
summary: Der Nutzen der Hüllkurven: Wie ein Bandpass auf ein Bandpasssignal wirkt, rechnet man vollständig im Tiefpassbereich.
tags: 
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Der Nutzen der Hüllkurven: Wie ein Bandpass auf ein Bandpasssignal wirkt, rechnet man vollständig im Tiefpassbereich.
:::

:::satz Satz 9.1 (Übertragung im äquivalenten Tiefpassbereich)
<span class="anker" id="satz-9-1"></span>

Erfüllen $S_T$ und $H_T$ beide [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) (nichts unterhalb von $-f_0$), dann gilt für die Hüllkurve des Ausgangs

<span class="anker" id="gl-9-1"></span>
$$G_T(f)=\tfrac12S_T(f)\,H_T(f)\qquad\bullet\!\!-\!\!\circ\qquad g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr],\qquad g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}. \tag{9.1}$$
:::

:::herleitung Übertragung
$G=S\cdot H$ mit beiden Darstellungen [(7.2)](der-ideale-bandpass-und-sein-aquivalenter-tiefpass.html#gl-7-2) ausmultipliziert gibt vier Produkte. Die gemischten, etwa $S_T(f-f_0)H_T^*(-f-f_0)$, sind null: Der erste Faktor lebt bei positiven, der zweite bei negativen Frequenzen. Es bleibt $G=\frac14S_T(f-f_0)H_T(f-f_0)+\frac14S_T^*(-f-f_0)H_T^*(-f-f_0)$. Der Vergleich mit $G=\frac12G_T(f-f_0)+\frac12G_T^*(-f-f_0)$ gibt $G_T=\frac12S_TH_T$.
:::

⁠**So liest man das:** Der Faktor $\frac12$ gleicht aus, dass $S_T$ und $H_T$ beide verdoppelt wurden. Sonst ist es der gewohnte Faltungssatz, nur für die Hüllkurven. Der Träger muss gar nicht mitgerechnet werden.

::::beispiel eingeschalteter Kosinus durch den idealen Bandpass
$s(t)=\varepsilon(t)\cos(2\pi f_0t)$ mit $f_0=10$ Hz, Bandpass mit $\Delta f=2$ Hz um $f_0$. Die Hüllkurve des Eingangs ist $s_T\approx\varepsilon(t)$. (Näherung: Das Spektrum des Sprungs ist nicht auf $f>-f_0$ begrenzt, im Durchlassbereich $|f|\le\Delta f/2\ll f_0$ stimmt es aber.) Mit $h_T=2\Delta f\operatorname{si}(\pi\Delta f\,t)$:

$$g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t),\qquad g(t)\approx\Bigl[\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)\Bigr]\cos(2\pi f_0t).$$

Die Hüllkurve ist die Sprungantwort eines idealen Tiefpasses mit $f_\mathrm g=\Delta f/2$: Einschwingzeit $1/\Delta f=0{,}5$ s, Überschwingen 8,95 % (Abb. [5](#abb-5)). Ein schmaler Bandpass braucht lange, bis er „eingeschwungen“ ist.

:::abbildung et3/k5bandpass 5
Antwort des idealen Bandpasses ($f_0=10$ Hz, $\Delta f=2$ Hz) auf einen bei $t=0$ eingeschalteten Kosinus der Mittenfrequenz. Blau das Ausgangssignal, rot die Einhüllende $\pm g_T(t)$. Sie steigt in etwa 0,5 s an und schwingt auf 1,09 über.
:::
::::

:::ltspice Eingeschalteter Träger durch einen Schwingkreis
Einen idealen Bandpass kann man nicht bauen, einen Reihenschwingkreis schon. **Zeichnen:** Quelle `voltage` am Netz `in`, dann in Reihe `ind` mit `{L}`, `cap` mit `{1/((2*pi*f0)**2*L)}` und `res` mit `{2*pi*df*L}` nach Masse. Der Ausgang `out` ist die Spannung am Widerstand. Mit `.param f0=10 df=2 L=1` ist die Mittenfrequenz 10 Hz und die Bandbreite zwischen den $-3$-dB-Punkten 2 Hz.

⁠**Kontrolle:** Quellwert `AC 1` und `.ac lin 2001 5 15` zeigen das Maximum 1 bei 10 Hz und die $-3$-dB-Punkte bei 9,05 Hz und 11,05 Hz.

⁠**Versuch:** Quelle `SINE(0 1 10 0 0 90)`, das ist $\varepsilon(t)\cos(2\pi f_0t)$, und `.tran 0 3 0 0.1m`. Die Hüllkurve steigt ohne Überschwingen an: Die Spitzen des Trägers erreichen 0,72 bei 0,2 s, 0,96 bei 0,5 s und praktisch 1 nach 1 s, fast genau wie $1-\mathrm{e}^{-t/0{,}16\,\mathrm s}$. Der ideale Bandpass schwingt dagegen auf 1,09 über (Abb. [5](#abb-5)). Der Grund ist derselbe wie beim Tiefpass in Stufe [3](sprungantwort-und-einschwingzeit.html#stufe-3): Die Flanken des Schwingkreises sind weich, die des idealen Bandpasses senkrecht.
:::

::::formelsammlung
**Übertragung im äquivalenten Tiefpassbereich**

$$G_T(f)=\tfrac12S_T(f)\,H_T(f)\qquad\bullet\!\!-\!\!\circ\qquad g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr],\qquad g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$$

Gilt, wenn $S_T$ und $H_T$ unterhalb von $-f_0$ null sind. Der Faktor $\frac12$ gleicht aus, dass $S_T$ und $H_T$ beide verdoppelt wurden; den Träger rechnet man nicht mit.

**Eingeschalteter Kosinus durch den idealen Bandpass**

$$g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)$$

Eingang $\varepsilon(t)\cos(2\pi f_0t)$ mit $s_T\approx\varepsilon(t)$, Bandpass der Breite $\Delta f$ um $f_0$. Die Hüllkurve ist die Sprungantwort eines idealen Tiefpasses mit $f_\mathrm g=\Delta f/2$: Einschwingzeit $1/\Delta f$, Überschwingen 8,95 %.
::::

::::lernkarten
:::karte formel Übertragung im äquivalenten Tiefpassbereich
Wie berechnet man die Hüllkurve des Ausgangs, wenn ein Bandpasssignal mit der Hüllkurve $s_T$ durch einen Bandpass mit dem äquivalenten Tiefpass $h_T$ läuft?
---
$G_T(f)=\tfrac12S_T(f)\,H_T(f)$ bzw. $g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr]$, und der Ausgang ist $g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$. Voraussetzung: $S_T$ und $H_T$ sind unterhalb von $-f_0$ null. Den Träger muss man nicht mitrechnen.
--- falsch
$G_T(f)=S_T(f)\,H_T(f)$ bzw. $g_T(t)=s_T(t)*h_T(t)$, genau wie beim gewöhnlichen Faltungssatz; ein zusätzlicher Faktor entsteht nicht, weil nichts verdoppelt wurde.
--- falsch
$G_T(f)=\tfrac12S_T(f)*H_T(f)$ bzw. $g_T(t)=\tfrac12s_T(t)\,h_T(t)$: Im Tiefpassbereich multipliziert man die Hüllkurven, weil der Träger die Rollen von Zeit und Frequenz vertauscht.
--- falsch
$G_T(f)=\tfrac12S_T(f)\,H_T(f)$ bzw. $g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr]$, aber der Träger muss mitgefaltet werden: Der Ausgang ist $g(t)=g_T(t)*\cos(2\pi f_0t)$, nicht der Realteil eines Produkts.
:::
:::karte zusammenhang Der Faktor ein Halb
Warum steht in $g_T(t)=\tfrac12\bigl[s_T(t)*h_T(t)\bigr]$ der Faktor $\frac12$?
---
Er gleicht aus, dass $S_T$ und $H_T$ beide durch Verdoppeln der positiven Frequenzen entstanden sind; ihr Produkt enthält den Faktor 2 also doppelt. Sonst ist es der gewohnte Faltungssatz, nur für die Hüllkurven.
--- falsch
Er berücksichtigt, dass nur die Hälfte der Signalleistung im Durchlassbereich des Bandpasses liegt; die andere Hälfte liegt bei den negativen Frequenzen und geht bei der Übertragung verloren.
--- falsch
Er kommt vom Realteil: Weil der Realteil einer komplexen Zahl der Mittelwert aus ihr und ihrem Konjugierten ist, halbiert seine Bildung jede Hüllkurve, und dieser Verlust steckt schon in der Faltung.
--- falsch
Er gleicht aus, dass der Träger beim Multiplizieren eine zweite Komponente bei $2f_0$ erzeugt; die Hälfte der Energie landet dort und fehlt deshalb im Tiefpassbereich.
:::
:::karte herleitung Hüllkurve des Ausgangs
Wie folgt aus $G=S\cdot H$ und der Darstellung aller drei Spektren durch äquivalente Tiefpässe, dass $G_T=\frac12S_TH_T$ gilt?
---
Man schreibt $S$ und $H$ als Summe aus verschobenem Band und konjugiertem Spiegelbild und multipliziert aus, weil $G=S\cdot H$ gilt; es entstehen vier Produkte.
---
Die gemischten Produkte wie $S_T(f-f_0)H_T^*(-f-f_0)$ sind null, weil der erste Faktor nur bei positiven und der zweite nur bei negativen Frequenzen lebt.
---
Es bleibt $G=\frac14S_T(f-f_0)H_T(f-f_0)+\frac14S_T^*(-f-f_0)H_T^*(-f-f_0)$, weil sich die Faktoren $\frac12$ der beiden Darstellungen multiplizieren.
---
Der Vergleich mit $G=\frac12G_T(f-f_0)+\frac12G_T^*(-f-f_0)$ liefert $G_T=\frac12S_TH_T$, weil auch der Ausgang durch seinen äquivalenten Tiefpass dargestellt wird.
:::
:::karte zusammenhang Rechnen ohne Träger
Warum lohnt es sich, die Übertragung eines Bandpasssignals durch einen Bandpass im äquivalenten Tiefpassbereich zu rechnen?
---
Weil man dort nur die Hüllkurven $s_T$ und $h_T$ faltet, also Tiefpasssignale, und den Träger gar nicht mitrechnen muss. Erst am Ende setzt man ihn mit $g(t)=\operatorname{Re}\bigl\{g_T(t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}$ wieder auf.
--- falsch
Weil im Tiefpassbereich gar keine Faltung nötig ist: Die Hüllkurve des Ausgangs ist einfach das Produkt $s_T(t)\,h_T(t)$, das man Punkt für Punkt ausrechnen kann, ohne je ein Integral zu bilden.
--- falsch
Weil der Tiefpassbereich die Bandbreite verdoppelt: Das Signal wird dort mit doppelter Auflösung dargestellt, und deshalb werden die Rechenfehler am Träger und an der Hüllkurve kleiner.
--- falsch
Weil der Träger im Tiefpassbereich seine Frequenz auf $2f_0$ verdoppelt und dadurch vom Signal getrennt ist; man filtert ihn am Ende einfach mit einem Tiefpass heraus und behält die Hüllkurve.
:::
:::karte formel Eingeschalteter Kosinus durch den idealen Bandpass
Welche Hüllkurve hat der Ausgang des idealen Bandpasses mit der Bandbreite $\Delta f$, wenn am Eingang ein bei $t=0$ eingeschalteter Kosinus der Mittenfrequenz liegt?
---
Mit $s_T\approx\varepsilon(t)$ ist $g_T(t)\approx\tfrac12\bigl[\varepsilon(t)*2\Delta f\operatorname{si}(\pi\Delta f\,t)\bigr]=\frac12+\frac1\pi\operatorname{Si}(\pi\Delta f\,t)$: die Sprungantwort eines idealen Tiefpasses mit $f_\mathrm g=\Delta f/2$, Einschwingzeit $1/\Delta f$, Überschwingen 8,95 %.
--- falsch
Mit $s_T\approx\varepsilon(t)$ ist $g_T(t)\approx1-\mathrm{e}^{-\pi\Delta f\,t}$ für $t\ge0$: Die Hüllkurve steigt ohne Überschwingen an, weil der ideale Bandpass wie ein Schwingkreis wirkt; die Zeitkonstante ist $1/(\pi\Delta f)$.
--- falsch
Mit $s_T\approx\varepsilon(t)$ ist $g_T(t)\approx\varepsilon(t)$: Der Kosinus liegt genau bei der Mittenfrequenz und kommt deshalb sofort und unverändert durch, ganz ohne Einschwingen und ohne Überschwingen der Hüllkurve.
--- falsch
Mit $s_T\approx\varepsilon(t)$ ist $g_T(t)\approx\frac12+\frac1\pi\operatorname{Si}(2\pi f_0t)$: die Sprungantwort eines idealen Tiefpasses mit der Grenzfrequenz $f_0$, die Einschwingzeit ist also $1/(2f_0)$ und damit sehr kurz.
:::
:::karte zusammenhang Schmaler Bandpass schwingt langsam ein
Warum braucht ein schmaler Bandpass lange, bis er eingeschwungen ist?
---
Seine Hüllkurve verhält sich wie die Sprungantwort eines idealen Tiefpasses mit $f_\mathrm g=\Delta f/2$, und deren Einschwingzeit ist $1/\Delta f$. Je kleiner die Bandbreite, desto länger dauert das Einschwingen, unabhängig von $f_0$.
--- falsch
Weil die Einschwingzeit von der Mittenfrequenz abhängt: Ein Bandpass braucht etwa $1/f_0$, und schmale Bandpässe liegen meist bei tiefen Mittenfrequenzen, deshalb schwingen sie langsam ein.
--- falsch
Weil ein schmaler Bandpass stärker überschwingt: Das Überschwingen wächst, je schmaler das Band ist, und das System braucht entsprechend länger, bis die großen Ausschläge wieder abgeklungen sind.
--- falsch
Weil der Träger erst durch alle Perioden der Bandbreite laufen muss: Die Einschwingzeit ist $\Delta f/f_0$, also umso größer, je mehr Trägerperioden in einer Periode der Bandbreite liegen.
:::
:::karte zusammenhang Schwingkreis ohne Überschwingen
Warum steigt die Hüllkurve am Ausgang eines Reihenschwingkreises ohne Überschwingen an, während der ideale Bandpass auf 1,09 überschwingt?
---
Weil die Flanken des Schwingkreises weich sind, die des idealen Bandpasses aber senkrecht. Der Grund ist derselbe wie beim Tiefpass: Das Überschwingen entsteht an senkrechten Kanten des Frequenzgangs.
--- falsch
Weil der Schwingkreis eine kleinere Bandbreite hat als der ideale Bandpass: Bei gleicher Mittenfrequenz und gleicher Bandbreite würde auch er genau auf 1,09 überschwingen.
--- falsch
Weil der Schwingkreis Energie in Spule und Kondensator speichert: Diese Speicher dämpfen jede Änderung, während der ideale Bandpass keine Speicher hat und deshalb überschwingt.
--- falsch
Weil der Schwingkreis bei der Mittenfrequenz eine Phase von $90^\circ$ hat: Die Phasendrehung verschiebt das Überschwingen in den Träger, sodass es in der Hüllkurve nicht zu sehen ist.
:::
::::
