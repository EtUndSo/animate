---
title: Stufe 11: Fourier und Laplace, Grenzen der Existenz
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Fourier-Reihe und -Transformation
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: Kapitel 3: Fourier-Reihe und -Transformation
order: 3231200
summary: Wann existiert das Fourier-Integral, und wie hängt es mit der Laplace-Transformation zusammen?
tags: zentralen Grenzwertsatzes
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
Wann existiert das Fourier-Integral, und wie hängt es mit der Laplace-Transformation zusammen?
:::

Hinreichend für die Existenz ist absolute Integrierbarkeit, $\int|s(t)|\mathrm{d} t<\infty$. Die Laplace-Transformation erweitert die Klasse, indem sie vorher mit $\mathrm{e}^{-\sigma t}$ gewichtet ([Kapitel 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)):

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f).$$

Sie untersucht ein Signal also auf zweierlei: auf Frequenzanteile wie die Fourier-Transformation und auf exponentielles Wachsen oder Abklingen. Liegt $\sigma=0$ im Konvergenzbereich, ist die Fourier-Transformierte die Laplace-Transformierte auf der imaginären Achse. Mit Dirac-Impulsen (Stufe [8](singulare-signale-und-linienspektren.html#stufe-8)) fasst die Fourier-Transformation aber auch Signale, die die Laplace-Transformation nicht fasst: Konstanten und Schwingungen über alle Zeiten. Allgemein genügt es, dass das Signal höchstens so schnell wächst wie eine Potenz von $t$, genauer: dass $\int|s(t)|\,(1+t^2)^{-n}\mathrm{d} t<\infty$ für ein $n\ge0$ gilt. Das erfüllen Konstanten, Schwingungen, der Sprung und $t^n$, nicht aber exponentiell wachsende Signale wie $\mathrm{e}^{t}\varepsilon(t)$; diese fasst nur die Laplace-Transformation.

:::zusatz Warum Mehrfachfaltungen gaußförmig werden
Faltet man $M$ Rechtecke $\operatorname{rect}(t)$ miteinander, ist das Spektrum $\operatorname{si}^M(\pi f)$. Für kleine $f$ ist $\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$ und $\ln(1+w)\approx w$, also

$$\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}.$$

Für große $M$ trägt nur der Bereich kleiner $f$ bei, die Näherung wird immer besser. Bei $M=4$ ist der Wert bei $t=0$ exakt $0{,}667$, die Gaußkurve gibt $0{,}691$. Das ist ein Fall des __zentralen Grenzwertsatzes__ (Teil zur Statistik): Die Faltung vieler gleicher positiver Impulse endlicher Fläche nähert sich einer Gaußkurve, sofern die Impulse schnell genug abklingen, genauer: sofern ihr zweites Moment $\int t^2s(t)\,\mathrm{d} t$ endlich ist. Ein Beispiel ist die Impulsantwort einer Kette vieler kurzer Integratoren. Ohne diese Bedingung geht es nicht: $\frac{1}{1+t^2}$ aus Aufgabe [7](die-rechenregeln-theoreme.html#aufg-7) hat ein unendliches zweites Moment, und die $M$-fache Faltung mit dem Spektrum $\pi^M\mathrm{e}^{-2\pi M|f|}$ ist wieder eine gedehnte Kurve der Form $\frac{1}{1+t^2}$.
:::

:::aufgabe Aufgabe 14 ★★★ (Vertiefung) Die Gaußnäherung prüfen
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

Vergleiche für $M=2$ den exakten Wert $\Lambda(0)=1$ mit der Gaußnäherung.

</li>

<li>

Zeige, dass die Gaußkurve $\sqrt{6/(\pi M)}\,\mathrm{e}^{-6t^2/M}$ die Fläche 1 hat. Warum muss das so sein?

</li>

</ol>

:::loesung
(a) $M=2$: $\sqrt{6/(2\pi)}=0{,}977$ statt $\Lambda(0)=1$, also 2,3 % zu wenig. Bei $M=4$: 0,691 statt 0,667, also 3,6 % zu viel. Schon nach wenigen Faltungen liegt die Gaußkurve also nahe am exakten Ergebnis. Beliebig gut wird die Näherung erst für große $M$, weil erst dann nur noch kleine $f$ zum Spektrum beitragen.

(b) $\int\mathrm{e}^{-6t^2/M}\mathrm{d} t=\sqrt{\pi M/6}$, mal $\sqrt{6/(\pi M)}$ ergibt 1. Das muss so sein: Die Fläche einer Faltung ist das Produkt der Flächen, hier $1^M=1$. Im Spektrum ist das der Wert bei $f=0$, $\operatorname{si}^M(0)=1$, und die Näherung $\mathrm{e}^{-M(\pi f)^2/6}$ hat dort ebenfalls 1.
:::
:::

::::kurzfassung
Fourier- und Laplace-Transformation erweitern die Klasse der transformierbaren Signale auf verschiedene Weise. Keine der beiden umfasst die andere.

Hinreichend für die Existenz des Fourier-Integrals ist $\int|s(t)|\,\mathrm{d} t<\infty$. Die Laplace-Transformation gewichtet das Signal vorher mit $\mathrm{e}^{-\sigma t}$:

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f).$$

Sie untersucht ein Signal damit auf Frequenzanteile und auf exponentielles Wachsen oder Abklingen. Liegt $\sigma=0$ im Konvergenzbereich, ist die Fourier-Transformierte die Laplace-Transformierte auf der imaginären Achse. Mit Dirac-Impulsen im Spektrum fasst die Fourier-Transformation dagegen Signale, die die Laplace-Transformation nicht fasst, etwa Konstanten und Schwingungen über alle Zeiten. Es genügt dann, dass ein Signal höchstens wie eine Potenz $t^n$ wächst; exponentiell wachsende Signale fasst nur die Laplace-Transformation.

Eine Vertiefung zeigt, warum Mehrfachfaltungen gaußförmig werden. Faltet man $M$ Rechtecke $\operatorname{rect}(t)$, ist das Spektrum $\operatorname{si}^M(\pi f)$. Für großes $M$ zählt nur die Umgebung von $f=0$, und dort ist es nahezu $\mathrm{e}^{-M(\pi f)^2/6}$, das Spektrum einer Gaußkurve. Das ist ein Fall des __zentralen Grenzwertsatzes__: Die Faltung vieler positiver Impulse endlicher Fläche nähert sich einer Gaußkurve, sofern die Impulse schnell genug abklingen, etwa weil sie wie das Rechteck nur auf einem endlichen Intervall von null verschieden sind.

Falle: Auf dem Rand des Konvergenzbereichs darf man nicht einfach $p=\mathrm{j}2\pi f$ einsetzen. Beim Sprung $\varepsilon(t)$ liegt die imaginäre Achse genau dort; das Einsetzen liefert nur $\frac{1}{\mathrm{j}2\pi f}$, die Linie $\tfrac12\delta(f)$ fehlt.
::::

::::formelsammlung
**Hinreichende Existenzbedingung**

$$\int|s(t)|\,\mathrm{d} t<\infty$$

Absolut integrierbares Signal. Mit Dirac-Impulsen im Spektrum genügt, dass das Signal höchstens wie eine Potenz $t^n$ wächst (Konstanten, Schwingungen, Sprung); exponentiell wachsende Signale fasst nur die Laplace-Transformation.

**Laplace-Transformation als gewichtete Fourier-Transformation**

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f)$$

$\sigma$ reell, im Konvergenzbereich. Liegt $\sigma=0$ im Konvergenzbereich, ist $S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$. Liegt die imaginäre Achse nur auf seinem Rand, wie beim Sprung, fehlen beim Einsetzen die Dirac-Anteile.

**Gaußnäherung der Mehrfachfaltung**

$$\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}$$

$\operatorname{si}^M(\pi f)$ ist das Spektrum von $M$ miteinander gefalteten Rechtecken $\operatorname{rect}(t)$. Mit $\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$ für kleine $f$; umso genauer, je größer $M$. Die Gaußkurve hat die Fläche 1 wie die Faltung der Rechtecke.
::::

::::lernkarten
:::karte formel Laplace als gewichtete Fourier-Transformation
Wie hängt die Laplace-Transformierte $S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)$ mit der Fourier-Transformation zusammen, und worauf untersucht sie ein Signal?
---
$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f)$: Sie ist die Fourier-Transformierte des vorher mit $\mathrm{e}^{-\sigma t}$ gewichteten Signals. Damit untersucht sie ein Signal auf Frequenzanteile und auf exponentielles Wachsen oder Abklingen.
--- falsch
$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\bigr\}(f)\,\mathrm{e}^{-\sigma}$: Sie ist die Fourier-Transformierte, nachträglich mit $\mathrm{e}^{-\sigma}$ gewichtet. Damit untersucht sie ein Signal nur auf Frequenzanteile, genau wie die Fourier-Transformation.
--- falsch
$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{\sigma t}\bigr\}(f)$: Sie ist die Fourier-Transformierte des mit $\mathrm{e}^{\sigma t}$ verstärkten Signals. Damit untersucht sie ein Signal nur darauf, wie schnell es für große $t$ abklingt.
--- falsch
$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\bigr\}(\sigma+f)$: Sie ist die Fourier-Transformierte, an einer verschobenen Frequenz ausgewertet. Damit untersucht sie ein Signal auf Frequenzanteile oberhalb von $\sigma$.
:::
:::karte zusammenhang Fourier aus Laplace
Wann darf man die Fourier-Transformierte durch Einsetzen von $p=\mathrm{j}2\pi f$ aus der Laplace-Transformierten gewinnen, und was geht beim Sprung schief?
---
Wenn $\sigma=0$ im Konvergenzbereich liegt; dann ist die Fourier-Transformierte die Laplace-Transformierte auf der imaginären Achse. Liegt die Achse nur auf dem Rand, wie beim Sprung $\varepsilon(t)$, liefert das Einsetzen nur $\frac{1}{\mathrm{j}2\pi f}$, und die Linie $\tfrac12\delta(f)$ fehlt.
--- falsch
Immer, denn die Laplace-Transformierte ist eine Funktion, die man überall auswerten darf, auch außerhalb ihres Konvergenzbereichs. Beim Sprung liefert das Einsetzen $\frac{1}{\mathrm{j}2\pi f}$, und das ist bereits sein vollständiges Spektrum ohne weiteren Anteil.
--- falsch
Wenn $\sigma=0$ im Konvergenzbereich liegt. Beim Sprung ist das der Fall, denn sein Konvergenzbereich schließt die imaginäre Achse ein; das Einsetzen liefert also das richtige und vollständige Spektrum $\frac{1}{\mathrm{j}2\pi f}$, ohne Linie bei $f=0$.
--- falsch
Nur bei kausalen Signalen, weil die Laplace-Transformation nur kausale Signale erfasst. Beim Sprung liefert das Einsetzen deshalb schon das ganze Spektrum $\tfrac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$, gerade weil er kausal ist und bei null beginnt.
:::
:::karte zusammenhang Existenz mit Dirac-Impulsen
Welche Signale fasst die Fourier-Transformation mit Dirac-Impulsen im Spektrum, und welche fasst nur die Laplace-Transformation?
---
Es genügt, dass das Signal höchstens so schnell wächst wie eine Potenz von $t$: $\int|s(t)|\,(1+t^2)^{-n}\mathrm{d} t<\infty$ für ein $n\ge0$. Das erfüllen Konstanten, Schwingungen, der Sprung und $t^n$. Exponentiell wachsende Signale wie $\mathrm{e}^{t}\varepsilon(t)$ fasst nur die Laplace-Transformation.
--- falsch
Nur absolut integrierbare Signale, $\int|s(t)|\mathrm{d} t<\infty$; Dirac-Impulse im Spektrum ändern daran nichts, sie sind nur eine Schreibweise. Konstanten, Schwingungen und der Sprung lassen sich deshalb nur mit der Laplace-Transformation behandeln.
--- falsch
Alle Signale, auch exponentiell wachsende wie $\mathrm{e}^{t}\varepsilon(t)$: Mit Dirac-Impulsen im Spektrum lässt sich jedes noch so schnelle Wachstum darstellen. Die Laplace-Transformation ist deshalb nur eine Rechenvereinfachung für Einschaltvorgänge.
--- falsch
Nur Signale, die beschränkt bleiben, also Konstanten, Schwingungen und der Sprung, nicht aber $t^n$. Was über alle Grenzen wächst, ob wie eine Potenz oder exponentiell, fasst ausschließlich die Laplace-Transformation mit ihrem Faktor $\mathrm{e}^{-\sigma t}$.
:::
:::karte formel Gaußnäherung der Mehrfachfaltung
Welche Form nähert die Faltung von $M$ Rechtecken $\operatorname{rect}(t)$ für großes $M$ an, und wie gewinnt man sie aus dem Spektrum?
---
Eine Gaußkurve: $\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}$, mit $\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$ und $\ln(1+w)\approx w$ für kleine $f$. Für großes $M$ trägt nur der Bereich kleiner $f$ bei.
--- falsch
Ein breites Rechteck: $\operatorname{si}^M(\pi f)\approx\operatorname{si}(\pi Mf)\;\bullet\!\!-\!\!\circ\;\frac1M\operatorname{rect}\Bigl(\frac tM\Bigr)$. Die Faltung von Rechtecken bleibt ein Rechteck, das mit jedem weiteren Schritt nur breiter und niedriger wird.
--- falsch
Eine Gaußkurve: $\operatorname{si}^M(\pi f)\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}$, aber nur für kleine $M$. Für großes $M$ wird die Näherung schlechter, weil sich die Fehler der einzelnen Faktoren aufsummieren.
--- falsch
Ein Dirac-Impuls: $\operatorname{si}^M(\pi f)$ geht für $M\to\infty$ überall gegen 1, weil die si-Funktion bei $f=0$ den Wert 1 hat. Die Faltung vieler Rechtecke zieht sich deshalb auf einen einzigen Punkt zusammen.
:::
:::karte zusammenhang zentraler Grenzwertsatz
Was geschieht, wenn man viele gleiche positive Impulse endlicher Fläche miteinander faltet, und welche Bedingung müssen die Impulse dafür erfüllen?
---
Das Ergebnis nähert sich einer Gaußkurve, ein Fall des zentralen Grenzwertsatzes. Die Impulse müssen schnell genug abklingen, genauer: Ihr zweites Moment $\int t^2s(t)\,\mathrm{d} t$ muss endlich sein.
--- falsch
Das Ergebnis nähert sich einer Gaußkurve, und zwar für jede Form der Impulse ohne weitere Bedingung. Es genügt, dass sie positiv sind und eine endliche Fläche haben; wie schnell sie abklingen, spielt für das Ergebnis keine Rolle.
--- falsch
Das Ergebnis nähert sich einem Rechteck, weil sich die Impulse beim Falten gegenseitig auffüllen und die Spitzen einebnen. Die Impulse müssen dafür eine endliche Dauer haben; nur dann wird das Rechteck mit jeder Faltung breiter.
--- falsch
Das Ergebnis nähert sich einer Gaußkurve, sofern die Impulse endliche Energie haben, das Integral von $s^2(t)$ also endlich ist. Ein Gegenbeispiel sind Impulse mit Sprüngen wie das Rechteck, die nie gaußförmig werden.
:::
:::karte zusammenhang Kein Gauß bei unendlichem zweitem Moment
Warum wird die mehrfache Faltung von $\frac{1}{1+t^2}$ mit sich selbst nicht gaußförmig?
---
Weil $\frac{1}{1+t^2}$ ein unendliches zweites Moment hat und damit die Bedingung des zentralen Grenzwertsatzes verletzt. Die $M$-fache Faltung hat das Spektrum $\pi^M\mathrm{e}^{-2\pi M|f|}$ und ist wieder eine gedehnte Kurve der Form $\frac{1}{1+t^2}$.
--- falsch
Weil $\frac{1}{1+t^2}$ nicht überall positiv ist und der zentrale Grenzwertsatz nur für positive Impulse gilt. Die $M$-fache Faltung schwingt deshalb mit jedem Schritt stärker und nähert sich keiner festen Form an, auch nicht für großes $M$.
--- falsch
Sie wird doch gaußförmig, nur langsamer: Das Spektrum $\pi^M\mathrm{e}^{-2\pi M|f|}$ nähert sich für großes $M$ einer Gaußkurve, weil die Exponentialfunktion für kleine $f$ fast linear abfällt wie ein si-Spektrum.
--- falsch
Weil $\frac{1}{1+t^2}$ eine unendliche Fläche hat und die Faltung deshalb schon nach dem ersten Schritt nicht mehr existiert. Entsprechend ist ihr Spektrum $\pi\,\mathrm{e}^{-2\pi|f|}$ bei $f=0$ unendlich groß.
:::
:::karte zusammenhang Fläche der Gaußnäherung
Warum muss die Gaußkurve $\sqrt{6/(\pi M)}\,\mathrm{e}^{-6t^2/M}$, die die Faltung von $M$ Rechtecken nähert, die Fläche 1 haben?
---
Die Fläche einer Faltung ist das Produkt der Flächen, hier $1^M=1$. Im Spektrum ist das der Wert bei $f=0$: $\operatorname{si}^M(0)=1$, und die Näherung $\mathrm{e}^{-M(\pi f)^2/6}$ hat dort ebenfalls den Wert 1.
--- falsch
Die Fläche einer Faltung ist die Summe der Flächen, hier also $M$. Die Gaußkurve hat deshalb erst nach Division durch $M$ die Fläche 1, und genau dafür steht der Vorfaktor $\sqrt{6/(\pi M)}$ vor der Exponentialfunktion.
--- falsch
Weil jede Gaußkurve die Fläche 1 hat, unabhängig von Höhe und Breite. Der Vorfaktor $\sqrt{6/(\pi M)}$ ist nur nötig, damit der Wert bei $t=0$ mit dem exakten Ergebnis der Faltung übereinstimmt.
--- falsch
Die Fläche einer Faltung ist das Produkt der Flächen, hier $1^M=1$. Im Spektrum ist das der Wert bei $f=0$, und dort ist $\operatorname{si}^M(0)=0$, weil die si-Funktion bei null eine Nullstelle hat.
:::
::::
