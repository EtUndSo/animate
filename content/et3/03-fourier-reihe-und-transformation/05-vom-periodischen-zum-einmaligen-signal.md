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

::::lernkarten
:::karte formel Koeffizienten der periodischen Fortsetzung
Wie hängen die Fourier-Koeffizienten eines Impulses, der mit der Periode $T=1/F$ fortgesetzt wird, mit der Fourier-Transformierten $S(f)$ des einzelnen Impulses zusammen?
---
$S_p(k)=F\cdot S(kF)$, sofern der Impuls kürzer als $T$ ist: Die Linien sind die Werte der festen Hüllkurve $S(f)$ an den Stellen $kF$, mal $F$. Jede Linie vertritt ein Band der Breite $F$.
--- falsch
$S_p(k)=S(kF)/F$: Die Linien sind die Werte der Hüllkurve $S(f)$ an den Stellen $kF$, geteilt durch $F$. Je länger die Periode, desto kleiner $F$ und desto höher die Linien, bis sie für $T\to\infty$ unendlich sind.
--- falsch
$S_p(k)=S(k/F)$: Die Linien sind die Werte der Hüllkurve an den Stellen $k/F$, also bei Vielfachen der Periode. Verlängert man die Periode, rücken die Linien deshalb auseinander und tasten die Hüllkurve gröber ab.
--- falsch
$S_p(k)=F\cdot S(kF)$, aber die Hüllkurve $S(f)$ hängt von der Periode ab: Verdoppelt man $T$, ändert sich ihre Form, und die neuen Linien liegen auf einer anderen Kurve als die alten.
:::
:::karte zusammenhang Von der Reihe zum Integral
Was passiert mit den Linien der Fourier-Reihe eines periodisch fortgesetzten Impulses, wenn die Periode $T$ gegen unendlich geht?
---
Der Linienabstand $F=1/T$ schrumpft, und die Linien tasten dieselbe Hüllkurve $S(f)$ immer dichter ab. Im Grenzfall wird aus dem Abstand $F$ das Differential $\mathrm{d} f$ und aus der Summe $\sum_kS(kF)\mathrm{e}^{\mathrm{j}2\pi kFt}F$ das Fourier-Integral.
--- falsch
Der Linienabstand $F=1/T$ wächst, und die Linien rücken auseinander, bis nur noch der Gleichanteil übrig bleibt. Im Grenzfall besteht das Spektrum eines einzelnen Impulses deshalb aus einer einzigen Linie bei $f=0$.
--- falsch
Der Linienabstand bleibt gleich, aber die Linien werden immer höher, weil jede Periode mehr Energie enthält. Im Grenzfall werden alle Linien unendlich hoch, und ein Spektrum lässt sich nicht mehr angeben.
--- falsch
Der Linienabstand $F=1/T$ schrumpft, die Hüllkurve wird dabei aber immer schmaler, bis sie für $T\to\infty$ zu einer einzigen Linie bei $f=0$ zusammenfällt. Aus dieser Linie entsteht das Integral.
:::
:::karte begriff Fourier-Transformation
Wie sind die Fourier-Transformation eines einmaligen Signals $s(t)$ und ihre Rücktransformation definiert, und wie schreibt man sie kurz?
---
$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t$ und $s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f$. Kurz: $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ oder $S(f)=\mathcal{F}\{s(t)\}$.
--- falsch
$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} t$ und $s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f$, mit demselben Vorzeichen im Exponenten. Kurz: $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$.
--- falsch
$S(f)=\frac1T\int_{0}^{T}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t$ und $s(t)=\sum_kS(kF)\,\mathrm{e}^{\mathrm{j}2\pi kFt}$, gemittelt über eine Periode. Kurz: $s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ oder $S(f)=\mathcal{F}\{s(t)\}$.
--- falsch
$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t$ und $s(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f$, mit dem Faktor $\frac{1}{2\pi}$ vor der Rücktransformation.
:::
:::karte begriff Spektraldichte
Was bedeutet es, dass die Fourier-Transformierte $S(f)$ eines einmaligen Signals eine Spektraldichte ist, und welche Einheit hat sie bei einer Spannung?
---
$S(f)$ ist ein Gewicht pro Frequenzintervall: Keine einzelne Frequenz hat eine endliche Amplitude, erst ein Band der Breite $\Delta f$ trägt etwa $S(f)\,\Delta f$. Ist $s$ eine Spannung in V, hat $S$ die Einheit V/Hz.
--- falsch
$S(f)$ ist die Amplitude der Schwingung mit der Frequenz $f$: Jede einzelne Frequenz trägt genau den Anteil $S(f)$. Ist $s$ eine Spannung in V, hat $S$ ebenfalls die Einheit V, wie die Fourier-Koeffizienten.
--- falsch
$S(f)$ ist ein Gewicht pro Zeitintervall: Erst ein Zeitabschnitt der Dauer $\Delta t$ trägt etwa $S(f)\,\Delta t$ zum Signal bei. Ist $s$ eine Spannung in V, hat $S$ deshalb die Einheit V/s.
--- falsch
$S(f)$ ist eine Leistung pro Frequenzintervall: Ein Band der Breite $\Delta f$ trägt etwa die Leistung $S(f)\,\Delta f$. Ist $s$ eine Spannung in V, hat $S$ deshalb die Einheit $\mathrm V^2$/Hz.
:::
:::karte zusammenhang Spektrum
Wie setzt die Rücktransformation ein Signal aus seinem Spektrum $S(f)$ zusammen, und was legt $S(f)$ dabei für jede Frequenz fest?
---
Sie setzt das Signal aus allen Schwingungen $\mathrm{e}^{\mathrm{j}2\pi ft}$ zusammen, jede mit dem komplexen Gewicht $S(f)\,\mathrm{d} f$. Das Spektrum sagt damit, mit welcher Amplitude und Phase jede Frequenz im Signal steckt.
--- falsch
Sie setzt das Signal aus verschobenen Dirac-Impulsen zusammen, einen für jede Frequenz. $S(f)$ legt fest, zu welcher Zeit der Impuls mit der Nummer $f$ auftritt; Amplitude und Phase spielen dabei keine Rolle.
--- falsch
Sie setzt das Signal aus allen Schwingungen $\mathrm{e}^{\mathrm{j}2\pi ft}$ zusammen, jede mit dem reellen Gewicht $|S(f)|\,\mathrm{d} f$. Das Spektrum legt damit nur die Amplituden fest; die Phasen aller Schwingungen sind null.
--- falsch
Sie setzt das Signal nur aus den Schwingungen mit $S(f)\neq0$ zusammen, jede mit dem Gewicht 1. $S(f)$ entscheidet also nur, ob eine Frequenz vorkommt, nicht, wie stark sie im Signal vertreten ist.
:::
:::karte formel Hinreichende Existenzbedingung
Welche Bedingung an ein einmaliges Signal $s(t)$ reicht aus, damit seine Fourier-Transformierte $S(f)$ als Integral existiert?
---
$\int|s(t)|\mathrm{d} t<\infty$: Das Signal ist absolut integrierbar, das Integral seines Betrags über alle Zeiten ist endlich. Diese Bedingung ist hinreichend für die Existenz des Fourier-Integrals.
--- falsch
$\int s(t)\,\mathrm{d} t=0$: Die Fläche unter dem Signal muss verschwinden. Sonst wächst das Fourier-Integral bei $f=0$ über alle Grenzen, und die Fourier-Transformierte existiert für kein $f$.
--- falsch
$|s(t)|<\infty$ für alle $t$: Das Signal muss nur beschränkt sein, also nirgends unendlich werden. Wie lange es dauert, spielt keine Rolle, weil der Faktor $\mathrm{e}^{-\mathrm{j}2\pi ft}$ für die Konvergenz sorgt.
--- falsch
$\int|s(t)|\mathrm{d} t<\infty$, aber nur über eine Periode genommen: Das Signal muss periodisch sein und in jeder Periode eine endliche Fläche haben, sonst gibt es keine Fourier-Transformierte.
:::
:::karte formel Faltungssatz und Dirac-Impuls
Was wird bei der Fourier-Transformation aus der Faltung $s(t)*h(t)$, und welches Spektrum folgt daraus für den Dirac-Impuls?
---
$s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$: Faltung wird Produkt. Aus $s*\delta=s$ folgt $S(f)\cdot\mathcal{F}\{\delta\}=S(f)$, also $\delta(t)\;\circ\!\!-\!\!\bullet\;1$: Der Dirac-Impuls enthält alle Frequenzen mit gleichem Gewicht.
--- falsch
$s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)*H(f)$: Faltung bleibt Faltung. Aus $s*\delta=s$ folgt, dass $\mathcal{F}\{\delta\}$ selbst ein Dirac-Impuls ist, $\delta(t)\;\circ\!\!-\!\!\bullet\;\delta(f)$: Er enthält nur die Frequenz null.
--- falsch
$s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$: Faltung wird Produkt. Aus $s*\delta=s$ folgt $\mathcal{F}\{\delta\}=0$, denn der Dirac-Impuls ist nur in einem einzigen Punkt von null verschieden und enthält keine Frequenzen.
--- falsch
$s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)+H(f)$: Faltung wird Summe. Aus $s*\delta=s$ folgt $\mathcal{F}\{\delta\}=0$; der Dirac-Impuls enthält also keine Frequenzen, weil er keine Dauer hat, in der er schwingen könnte.
:::
:::karte formel Exponentialimpuls
Welche Fourier-Transformierte hat die Impulsantwort $h(t)=\frac1{RC}\varepsilon(t)\mathrm{e}^{-t/RC}$ des RC-Glieds, und was zeigt der Vergleich mit der Wechselstromrechnung?
---
$H(f)=\frac{1}{1+\mathrm{j}2\pi f\,RC}$, derselbe Frequenzgang wie aus der Wechselstromrechnung. Die Impulsantwort enthält also die ganze Information über das Frequenzverhalten.
--- falsch
$H(f)=\frac{RC}{1+\mathrm{j}2\pi f\,RC}$, also der Frequenzgang aus der Wechselstromrechnung mal der Zeitkonstanten. Die Impulsantwort enthält das Frequenzverhalten nur bis auf einen Faktor.
--- falsch
$H(f)=\frac{1}{1-\mathrm{j}2\pi f\,RC}$, also der konjugierte Frequenzgang der Wechselstromrechnung. Die Impulsantwort enthält das Frequenzverhalten, aber mit umgekehrtem Vorzeichen der Phase.
--- falsch
$H(f)=\frac{1}{1+\mathrm{j}2\pi f\,RC}$, aber nur für $f>0$; für negative Frequenzen existiert das Integral nicht. Die Impulsantwort enthält also nur einen Teil der Information über das Frequenzverhalten.
:::
:::karte formel Zweiseitiger Exponentialimpuls
Welche Fourier-Transformierte hat der zweiseitige Exponentialimpuls $\mathrm{e}^{-a|t|}$ mit $a>0$, und welche Eigenschaften hat sie?
---
$\mathcal{F}\{\mathrm{e}^{-a|t|}\}=\frac{2a}{a^2+(2\pi f)^2}$, die Summe der Beiträge von $t<0$ und $t>0$. Sie ist reell und gerade in $f$, so wie das Signal reell und gerade in $t$ ist.
--- falsch
$\mathcal{F}\{\mathrm{e}^{-a|t|}\}=\frac{1}{a+\mathrm{j}2\pi f}$, wie beim einseitigen Impuls, weil der Anteil für $t<0$ dasselbe Integral liefert. Sie ist komplex, nur ihr Betrag ist gerade in $f$.
--- falsch
$\mathcal{F}\{\mathrm{e}^{-a|t|}\}=\frac{2a}{a^2-(2\pi f)^2}$, die Summe der Beiträge von $t<0$ und $t>0$. Sie ist reell und gerade in $f$, hat aber bei $2\pi f=a$ einen Pol.
--- falsch
$\mathcal{F}\{\mathrm{e}^{-a|t|}\}=\frac{-\mathrm{j}4\pi f}{a^2+(2\pi f)^2}$, die Differenz der Beiträge von $t>0$ und $t<0$. Sie ist rein imaginär und ungerade in $f$, weil das Signal bei $t=0$ einen Knick hat.
:::
::::
