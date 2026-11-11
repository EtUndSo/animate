---
title: Stufe 4: Vom periodischen zum einmaligen Signal
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3230500
summary: Ein einzelner Impuls ist nicht periodisch.
tags: Spektraldichte
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Ein einzelner Impuls ist nicht periodisch. Man kann ihn aber als periodisches Signal mit unendlich langer Periode auffassen. Dabei wird aus der Summe ein Integral.
:::

**Die Idee.** Man setzt einen Impuls $s(t)$ der Dauer kleiner als $T$ periodisch fort. Die Koeffizienten der Reihe sind dann Werte einer festen Funktion:

$$S_p(k)=\frac1T\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=F\cdot S(kF),\qquad S(f)=\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t.$$

Verdoppelt man die Periode, halbiert sich der Linienabstand $F$, und die Linien tasten dieselbe Hüllkurve $S(f)$ doppelt so dicht ab (Abb. [4](#abb-4)). Im Grenzfall $T\to\infty$ wird aus dem Abstand $F$ das Differential $\mathrm{d} f$ und aus der Summe $\sum_kS(kF)\mathrm{e}^{\mathrm{j}2\pi kFt}F$ das Integral.

:::abbildung et3/k3grenz 4
Ein Rechteckimpuls $\operatorname{rect}(t)$, periodisch fortgesetzt mit $T=2$ s und $T=4$ s. Die mit $T$ multiplizierten Fourier-Koeffizienten liegen auf derselben Hüllkurve $S(f)=\operatorname{si}(\pi f)$, mit dem Abstand $1/T$. Für $T\to\infty$ füllen sie die Kurve lückenlos.
:::

:::satz Satz 4.1 (Fourier-Transformation)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t,\qquad s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f. \tag{4.1}$$

Kurzschreibweise: $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ oder $S(f)=\mathcal{F}\{s(t)\}$.
:::

⁠**So liest man das:** $S(f)$ ist eine __Spektraldichte__: Gewicht pro Frequenzintervall. Ist $s$ eine Spannung in V, hat $S$ die Einheit V/Hz. Die Rücktransformation setzt das Signal aus allen Schwingungen zusammen, jede mit dem Gewicht $S(f)\,\mathrm{d} f$. Hinreichend für die Existenz ist $\int|s(t)|\mathrm{d} t<\infty$. Die Fourier-Transformierte ist die Laplace-Transformierte auf der imaginären Achse, $S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$, sofern diese im Konvergenzbereich liegt ([Kapitel 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)).

⁠**Faltung wird Produkt.** Wie in [Kapitel 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html): $s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$. Aus $s*\delta=s$ folgt $S(f)\cdot\mathcal{F}\{\delta\}=S(f)$, also $\delta(t)\;\circ\!\!-\!\!\bullet\;1$: Der Dirac-Impuls enthält alle Frequenzen mit gleichem Gewicht.

::::beispiel der Exponentialimpuls
Die Impulsantwort des RC-Glieds, $h(t)=\frac1{RC}\varepsilon(t)\mathrm{e}^{-t/RC}$:

$$H(f)=\frac1{RC}\int_0^\infty\mathrm{e}^{-(1/RC+\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{1+\mathrm{j}2\pi f\,RC}.$$

Das ist derselbe Frequenzgang wie aus der Wechselstromrechnung ([Kapitel 1](/wissen/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)). Die Impulsantwort enthält also die ganze Information über das Frequenzverhalten.
::::

:::frage Was ist der Unterschied zwischen $S_p(k)$ und $S(f)$, außer dass das eine diskret ist?
Die Einheit. $S_p(k)$ ist eine Amplitude (V): Die $k$-te Harmonische hat wirklich diese Stärke. $S(f)$ ist eine Dichte (V/Hz): Bei einem einmaligen Signal hat keine einzelne Frequenz eine endliche Amplitude, erst ein Frequenzband $\Delta f$ trägt etwa $S(f)\,\Delta f$. Deshalb ist $S_p(k)=F\cdot S(kF)$: Jede Linie vertritt ein Band der Breite $F$.
:::

:::aufgabe Aufgabe 4 ★ Der zweiseitige Exponentialimpuls
<span class="anker" id="aufg-4"></span>

Berechne $\mathcal{F}\{\mathrm{e}^{-a|t|}\}$ für $a>0$, indem du das Integral in $t<0$ und $t>0$ teilst. Zeige, dass das Ergebnis reell und gerade ist, und begründe das mit der Symmetrie des Signals.

:::loesung
$$\int_{-\infty}^0\mathrm{e}^{at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t+\int_0^\infty\mathrm{e}^{-at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{1}{a-\mathrm{j}2\pi f}+\frac{1}{a+\mathrm{j}2\pi f}=\frac{2a}{a^2+(2\pi f)^2}.$$

Reell und gerade in $f$. Das muss so sein: Das Signal ist reell und gerade, also ist sein ungerader Anteil null und damit auch $\operatorname{Im} S$ (Stufe [5](symmetrien-im-signal-und-im-spektrum.html#stufe-5)).
:::
:::

::::kurzfassung
Ein einmaliges Signal ist der Grenzfall eines periodischen Signals mit unendlich langer Periode. Aus der Fourier-Reihe wird dabei ein Integral über alle Frequenzen.

Setzt man einen Impuls $s(t)$ mit der Periode $T$ fort, sind die Koeffizienten Werte einer festen Funktion an den Stellen $kF$: $S_p(k)=F\cdot S(kF)$. Für $T\to\infty$ rücken die Linien zusammen, der Abstand $F$ wird zu $\mathrm{d} f$ und die Summe zum Integral. Das ergibt die __Fourier-Transformation__ und ihre Rücktransformation:

$$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t,\qquad s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f.$$

Man schreibt kurz $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ oder $S(f)=\mathcal{F}\{s(t)\}$. $S(f)$ ist eine __Spektraldichte__, ein Gewicht pro Frequenzintervall; zu einer Spannung in V gehört ein Spektrum in V/Hz. Hinreichend für die Existenz ist $\int|s(t)|\,\mathrm{d} t<\infty$. Liegt die imaginäre Achse im Konvergenzbereich der Laplace-Transformierten, gilt $S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$. Wie dort wird die Faltung zum Produkt, $s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$, und aus $s*\delta=s$ folgt $\delta(t)\;\circ\!\!-\!\!\bullet\;1$.

Der Grund für die Dichte: Bei einem einmaligen Signal hat keine einzelne Frequenz eine endliche Amplitude. Erst ein Band der Breite $\Delta f$ trägt etwa $S(f)\,\Delta f$, so wie jede Linie der Reihe ein Band der Breite $F$ vertritt.

Falle: $S_p(k)$ und $S(f)$ haben verschiedene Einheiten, V und V/Hz. Wer eine Linienhöhe mit einem Wert der Dichte vergleicht, muss die Dichte mit $F$ multiplizieren.
::::

::::formelsammlung
**Koeffizienten der periodischen Fortsetzung**

$$S_p(k)=F\cdot S(kF)$$

Impuls $s(t)$, kürzer als $T$, mit der Periode $T=1/F$ fortgesetzt; $S(f)$ seine Fourier-Transformierte. Jede Linie vertritt ein Band der Breite $F$.

**Fourier-Transformation und Rücktransformation**

$$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t,\qquad s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f$$

Kurzschreibweise $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ oder $S(f)=\mathcal{F}\{s(t)\}$. $S(f)$ ist eine Spektraldichte: Ist $s$ eine Spannung in V, hat $S$ die Einheit V/Hz.

**Hinreichende Existenzbedingung**

$$\int|s(t)|\,\mathrm{d} t<\infty$$

Absolut integrierbares Signal; Integral über alle Zeiten.

**Zusammenhang mit der Laplace-Transformierten**

$$S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$$

Sofern die imaginäre Achse im Konvergenzbereich der Laplace-Transformierten liegt.

**Faltungssatz**

$$s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$$

Faltung im Zeitbereich wird Produkt im Frequenzbereich.

**Dirac-Impuls**

$$\delta(t)\;\circ\!\!-\!\!\bullet\;1$$

Aus $s*\delta=s$. Der Dirac-Impuls enthält alle Frequenzen mit gleichem Gewicht.

**Exponentialimpuls (Impulsantwort des RC-Glieds)**

$$h(t)=\frac1{RC}\varepsilon(t)\mathrm{e}^{-t/RC},\qquad H(f)=\frac{1}{1+\mathrm{j}2\pi f\,RC}$$

Derselbe Frequenzgang wie aus der Wechselstromrechnung: Die Impulsantwort enthält die ganze Information über das Frequenzverhalten.

**Zweiseitiger Exponentialimpuls**

$$\mathcal{F}\{\mathrm{e}^{-a|t|}\}=\frac{2a}{a^2+(2\pi f)^2}$$

Für $a>0$. Reell und gerade in $f$, weil das Signal reell und gerade ist.
::::
