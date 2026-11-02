---
title: Stufe 4: Energiedichtespektrum
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Korrelationsfunktionen
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

⁠**So liest man das:** $|S(f)|^2$ heißt __Energiedichtespektrum__. Es ist reell, nie negativ und bei reellen Signalen gerade in $f$. Die Phase des Signals geht verloren: Alle Signale mit demselben Betragsspektrum haben dieselbe AKF. $S^*G$ heißt __Kreuzenergiedichtespektrum__. Die Herleitung braucht nur Faltungssatz, Zeitspiegelung und Konjugation: $s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$ ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)).

**Parseval.** Bei $\tau=0$ ist die AKF die Energie. Mit dem Flächensatz:

<span class="anker" id="gl-4-2"></span>
$$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f. \tag{4.2}$$

Zwei orthogonale Signale haben auch orthogonale Spektren: $\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$.

**Beispiel: der Exponentialimpuls.** $s(t)=\varepsilon(t)\mathrm{e}^{-t}$ hat $S(f)=\frac{1}{1+\mathrm{j}2\pi f}$, also $|S|^2=\frac{1}{1+(2\pi f)^2}$. Das ist zugleich $\operatorname{Re}\{S\}$, und dessen Rücktransformation ist der gerade Anteil des Signals ([Teil 3](/wissen/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)):

$$\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|},\qquad E_s=\varphi^E_{ss}(0)=\tfrac12.$$

Dasselbe gibt $\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$ im Zeitbereich und $\int\frac{\mathrm{d} f}{1+(2\pi f)^2}=\frac12$ im Frequenzbereich. Abbildung [2](#abb-2) zeigt das Signal, seine AKF und die beiden Spektren.

:::abbildung et3/k6exp 2
Exponentialimpuls ($RC=1$ s). Links das Signal und seine AKF $\frac12\mathrm{e}^{-|\tau|}$ (gerade, Maximum $=E_s=\frac12$). Rechts Betragsspektrum und Energiedichtespektrum, das schneller abfällt: Die Energie sitzt bei tiefen Frequenzen.
:::

:::aufgabe Aufgabe 4 ★ Parseval prüfen
<span class="anker" id="aufg-4"></span>

Berechne die Energie von $\operatorname{rect}(t)$ im Zeitbereich und mit [(4.2)](#gl-4-2) aus seinem Spektrum. Welches bekannte Integral über die si-Funktion folgt daraus?

:::loesung
Zeitbereich: $E=\int\operatorname{rect}^2\mathrm{d} t=1$. Frequenzbereich: $\int\operatorname{si}^2(\pi f)\mathrm{d} f$. Also folgt $\int_{-\infty}^\infty\operatorname{si}^2(\pi f)\mathrm{d} f=1$.
:::
:::
