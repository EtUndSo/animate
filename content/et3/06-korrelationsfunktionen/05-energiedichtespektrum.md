---
title: Stufe 4: Energiedichtespektrum
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Korrelationsfunktionen
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: Kapitel 6: Korrelationsfunktionen
order: 3260500
summary: Was ist die Fourier-Transformierte einer Korrelationsfunktion?
tags: Energiedichtespektrum, Kreuzenergiedichtespektrum
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Was ist die Fourier-Transformierte einer Korrelationsfunktion? Sie zeigt, wie sich die Energie über die Frequenzen verteilt.
:::

:::satz Satz 4.1 (Wiener-Khintchine für Energiesignale)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,S(f)=|S(f)|^2,\qquad\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,G(f). \tag{4.1}$$
:::

⁠**So liest man das:** $|S(f)|^2$ heißt __Energiedichtespektrum__. Es ist reell, nie negativ und bei reellen Signalen gerade in $f$. Die Phase des Signals geht verloren: Alle Signale mit demselben Betragsspektrum haben dieselbe AKF. $S^*G$ heißt __Kreuzenergiedichtespektrum__. Die Herleitung braucht nur Faltungssatz, Zeitspiegelung und Konjugation: $s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$ ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).

**Parseval.** Bei $\tau=0$ ist die AKF die Energie. Mit dem Flächensatz:

<span class="anker" id="gl-4-2"></span>
$$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f. \tag{4.2}$$

Zwei orthogonale Signale haben auch orthogonale Spektren: $\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$.

::::beispiel der Exponentialimpuls
$s(t)=\varepsilon(t)\mathrm{e}^{-t}$ hat $S(f)=\frac{1}{1+\mathrm{j}2\pi f}$, also $|S|^2=\frac{1}{1+(2\pi f)^2}$. Das ist zugleich $\operatorname{Re}\{S\}$, und dessen Rücktransformation ist der gerade Anteil des Signals ([Kapitel 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)):

$$\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|},\qquad E_s=\varphi^E_{ss}(0)=\tfrac12.$$

Dasselbe gibt $\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$ im Zeitbereich und $\int\frac{\mathrm{d} f}{1+(2\pi f)^2}=\frac12$ im Frequenzbereich. Abbildung [2](#abb-2) zeigt das Signal, seine AKF und die beiden Spektren.

:::abbildung et3/k6exp 2
Exponentialimpuls ($RC=1$ s). Links das Signal und seine AKF $\frac12\mathrm{e}^{-|\tau|}$ (gerade, Maximum $=E_s=\frac12$). Rechts Betragsspektrum und Energiedichtespektrum, das schneller abfällt: Die Energie sitzt bei tiefen Frequenzen.
:::
::::

:::aufgabe Aufgabe 4 ★ Parseval prüfen
<span class="anker" id="aufg-4"></span>

Berechne die Energie von $\operatorname{rect}(t)$ im Zeitbereich und mit [(4.2)](#gl-4-2) aus seinem Spektrum. Welches bekannte Integral über die si-Funktion folgt daraus?

:::loesung
Zeitbereich: $E=\int\operatorname{rect}^2\mathrm{d} t=1$. Frequenzbereich: $\int\operatorname{si}^2(\pi f)\mathrm{d} f$. Also folgt $\int_{-\infty}^\infty\operatorname{si}^2(\pi f)\mathrm{d} f=1$.
:::
:::

::::formelsammlung
**Wiener-Khintchine für Energiesignale**

$$\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,S(f)=|S(f)|^2,\qquad\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,G(f)$$

$|S(f)|^2$ ist das Energiedichtespektrum: reell, nie negativ, bei reellen Signalen gerade in $f$; die Phase des Signals geht verloren. $S^*G$ ist das Kreuzenergiedichtespektrum. Grundlage: Faltungssatz und $s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$.

**Parseval**

$$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f$$

Bei $\tau=0$ ist die AKF die Energie; mit dem Flächensatz ist das die Fläche des Energiedichtespektrums.

**Orthogonale Signale**

$$\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$$

Zwei orthogonale Signale haben auch orthogonale Spektren.

**AKF des Exponentialimpulses**

$$|S|^2=\frac{1}{1+(2\pi f)^2},\qquad\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|},\qquad E_s=\varphi^E_{ss}(0)=\tfrac12$$

Für $s(t)=\varepsilon(t)\mathrm{e}^{-t}$ mit $S(f)=\frac{1}{1+\mathrm{j}2\pi f}$. $|S|^2$ ist zugleich $\operatorname{Re}\{S\}$, dessen Rücktransformation der gerade Anteil des Signals ist.
::::

::::lernkarten
:::karte formel Wiener-Khintchine für Energiesignale
Was besagt der Satz von Wiener-Khintchine über die Fourier-Transformierten der AKF und der KKF von Energiesignalen?
---
$\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,S(f)=|S(f)|^2$ und $\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,G(f)$: Die AKF gehört zum Betragsquadrat des Spektrums, die KKF zum Produkt $S^*G$.
--- falsch
$\varphi^E_{ss}(\tau)\;\circ\!\!-\!\!\bullet\;S^2(f)$ und $\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S(f)\,G(f)$: Die AKF gehört zum Quadrat des Spektrums, weil die Korrelation eine Faltung ist und Faltung zum Produkt wird.
--- falsch
$\varphi^E_{ss}(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|$ und $\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|\,|G(f)|$: Die AKF gehört zum Betragsspektrum, die KKF zum Produkt der Betragsspektren.
--- falsch
$\varphi^E_{ss}(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2$ und $\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S(f)\,G^*(f)$: Bei der KKF wird das Spektrum des zweiten Signals konjugiert, weil dieses Signal um $\tau$ verschoben wird.
:::
:::karte herleitung Wiener-Khintchine
Wie folgt aus $\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)$, dass die AKF das Spektrum $|S(f)|^2$ hat?
---
Man transformiert das gespiegelte, konjugierte Signal: $s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$, weil Zeitspiegelung und Konjugation zusammen das konjugierte Spektrum ergeben.
---
Man wendet den Faltungssatz an und erhält $S^*(f)\,S(f)$, weil die AKF eine Faltung ist und eine Faltung im Zeitbereich zum Produkt der Spektren wird.
---
Es bleibt $S^*(f)\,S(f)=|S(f)|^2$, weil das Produkt einer komplexen Zahl mit ihrer Konjugierten ihr Betragsquadrat ist.
---
Ebenso gehört die KKF $\varphi^E_{sg}(\tau)=s^*(-\tau)*g(\tau)$ zu $S^*(f)\,G(f)$, weil dort nur das zweite Signal $g$ statt $s$ in die Faltung eingeht.
:::
:::karte begriff Energiedichtespektrum
Was gibt das Energiedichtespektrum $|S(f)|^2$ eines Energiesignals an, und welche Eigenschaften hat es?
---
Die Fourier-Transformierte der AKF; es zeigt, wie sich die Energie des Signals auf die Frequenzen verteilt. Es ist reell, nie negativ und bei reellen Signalen gerade in $f$.
--- falsch
Die Fourier-Transformierte des Signals selbst; es zeigt Betrag und Phase jeder Frequenz. Es ist im Allgemeinen komplex und bei reellen Signalen ungerade in $f$.
--- falsch
Die Fourier-Transformierte der AKF; es zeigt, wie sich die Energie über die Zeit verteilt. Es ist reell, kann aber negativ werden, wenn das Signal sein Vorzeichen wechselt.
--- falsch
Das Quadrat $S^2(f)$ des Spektrums; es zeigt, wie sich die Energie auf die Frequenzen verteilt, und enthält zusätzlich die Phase des Signals in doppelter Größe, sodass das Signal daraus eindeutig folgt.
:::
:::karte begriff Kreuzenergiedichtespektrum
Was bezeichnet man als Kreuzenergiedichtespektrum zweier Energiesignale $s$ und $g$?
---
Das Produkt $S^*(f)\,G(f)$, die Fourier-Transformierte ihrer KKF $\varphi^E_{sg}(\tau)$. Sein Integral über alle Frequenzen ist $\int s^*g\,\mathrm{d} t$, der Wert der KKF bei $\tau=0$.
--- falsch
Das Produkt $S(f)\,G(f)$, die Fourier-Transformierte der Faltung $s*g$. Es ist bei allen Signalen reell und nie negativ, genau wie das Energiedichtespektrum.
--- falsch
Die Summe $|S(f)|^2+|G(f)|^2$ der beiden Energiedichtespektren. Sein Integral über alle Frequenzen ist die gemeinsame Energie $E_s+E_g$ der beiden Signale.
--- falsch
Das Produkt $S^*(f)\,G(f)$, die Fourier-Transformierte der AKF von $s$. Es zeigt, wie sich die Energie von $s$ auf die Frequenzen verteilt, wenn man $g$ als Filter verwendet.
:::
:::karte formel Parseval
Was besagt der Satz von Parseval für Energiesignale, und wie folgt er aus der AKF?
---
$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f$: Bei $\tau=0$ ist die AKF die Energie, und nach dem Flächensatz ist ihr Wert bei null die Fläche ihres Spektrums $|S|^2$.
--- falsch
$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|\,\mathrm{d} f$: Die Energie ist die Fläche unter dem Betragsspektrum, weil die AKF bei $\tau=0$ mit dem Betragsspektrum übereinstimmt.
--- falsch
$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=|S(0)|^2$: Die Energie ist das Energiedichtespektrum bei $f=0$, weil der Flächensatz den Wert bei null mit der Fläche verbindet.
--- falsch
$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=2\pi\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f$: Beim Wechsel in den Frequenzbereich kommt der Faktor $2\pi$ hinzu, weil die Kreisfrequenz $\omega=2\pi f$ ist und über $f$ integriert wird.
:::
:::karte zusammenhang Phase geht verloren
Warum geht in der AKF die Phase des Signals verloren, und was folgt daraus für Signale mit demselben Betragsspektrum?
---
Weil die AKF zum Energiedichtespektrum $S^*(f)\,S(f)=|S(f)|^2$ gehört und im Betragsquadrat die Phase herausfällt. Alle Signale mit demselben Betragsspektrum haben deshalb dieselbe AKF.
--- falsch
Weil die AKF bei reellen Signalen gerade ist und gerade Funktionen keine Phase haben. Signale mit demselben Betragsspektrum haben trotzdem verschiedene AKFs, wenn ihre Phasen verschieden sind.
--- falsch
Weil man bei der Korrelation das zweite Signal nicht spiegelt; nur die Faltung, die spiegelt, bewahrt die Phase. Signale mit demselben Betragsspektrum haben deshalb zueinander gespiegelte AKFs.
--- falsch
Die Phase geht nicht verloren, sie steckt in der Lage des Maximums der AKF. Signale mit demselben Betragsspektrum unterscheiden sich daher in der Lage dieses Maximums.
:::
:::karte zusammenhang Orthogonale Spektren
Was folgt aus dem Satz von Wiener-Khintchine für die Spektren zweier orthogonaler Signale?
---
Sie sind ebenfalls orthogonal: $\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$. Denn der Wert der KKF bei $\tau=0$ ist zugleich das Integral über das Kreuzenergiedichtespektrum $S^*G$.
--- falsch
Ihre Spektren liegen in getrennten Frequenzbereichen: Orthogonale Signale können sich spektral nicht überlappen, sonst wäre ihr Kreuzenergiedichtespektrum irgendwo von null verschieden.
--- falsch
Ihre Spektren sind gleich, nur in der Phase um $90^\circ$ gegeneinander gedreht: Orthogonal heißt im Frequenzbereich senkrecht, also gilt $G(f)=\mathrm{j}\,S(f)$.
--- falsch
Über ihre Spektren sagt die Orthogonalität nichts: $\int s^*g\,\mathrm{d} t=0$ gilt nur im Zeitbereich, weil das Kreuzenergiedichtespektrum keine endliche Fläche hat.
:::
:::karte formel AKF des Exponentialimpulses
Welche AKF und welche Energie hat der Exponentialimpuls $\varepsilon(t)\mathrm{e}^{-t}$, und wie bestimmt man die AKF aus seinem Spektrum?
---
$|S|^2=\frac{1}{1+(2\pi f)^2}$ ist zugleich $\operatorname{Re}\{S\}$, dessen Rücktransformation der gerade Anteil des Signals ist: $\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|}$, also $E_s=\varphi^E_{ss}(0)=\tfrac12$.
--- falsch
$|S|^2=\frac{1}{1+(2\pi f)^2}$, und seine Rücktransformation ist das Signal selbst: $\varphi^E_{ss}(\tau)=\varepsilon(\tau)\mathrm{e}^{-\tau}$ mit der Energie $E_s=1$, dem Wert der AKF bei $\tau=0$.
--- falsch
$|S|^2=\frac{1}{1+2\pi f}$, und seine Rücktransformation ist $\varphi^E_{ss}(\tau)=\mathrm{e}^{-|\tau|}$; die Energie ist der Wert dieser AKF bei $\tau=0$, also $E_s=1$.
--- falsch
$|S|^2=\frac{1}{1+(2\pi f)^2}$ gehört zur AKF $\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|}$; die Energie ist deren Fläche über alle $\tau$, also $E_s=1$, denn die AKF verteilt die Energie über die Verschiebungen.
:::
:::karte zusammenhang Energie bei tiefen Frequenzen
Warum fällt beim Exponentialimpuls das Energiedichtespektrum $|S(f)|^2$ schneller ab als das Betragsspektrum $|S(f)|$, und was bedeutet das für die Energie?
---
Weil $|S(f)|\le1$ ist und das Quadrat kleine Werte noch kleiner macht. Die Energie des Impulses sitzt deshalb vor allem bei tiefen Frequenzen.
--- falsch
Weil das Quadrat die Phase entfernt, die bei hohen Frequenzen den größten Teil des Spektrums ausmacht. Die Energie verteilt sich trotzdem gleichmäßig über alle Frequenzen.
--- falsch
Weil die AKF doppelt so breit ist wie der Impuls und ihr Spektrum deshalb doppelt so schmal. Die Energie sitzt dann vor allem bei hohen Frequenzen, wo das Spektrum flach ist.
--- falsch
Weil $|S(f)|^2$ zum gespiegelten Signal gehört, das schneller abklingt als das ursprüngliche. Die Energie sitzt deshalb vor allem bei hohen Frequenzen.
:::
::::
