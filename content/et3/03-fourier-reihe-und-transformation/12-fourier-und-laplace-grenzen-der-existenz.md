---
title: Stufe 11: Fourier und Laplace, Grenzen der Existenz
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Fourier-Reihe und -Transformation
order: 3231200
summary: Wann existiert das Fourier-Integral, und wie hängt es mit der Laplace-Transformation zusammen?
tags: zentralen Grenzwertsatzes
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
Wann existiert das Fourier-Integral, und wie hängt es mit der Laplace-Transformation zusammen?
:::

Hinreichend für die Existenz ist absolute Integrierbarkeit, $\int|s(t)|\mathrm{d} t<\infty$. Die Laplace-Transformation erweitert die Klasse, indem sie vorher mit $\mathrm{e}^{-\sigma t}$ gewichtet ([Teil 2](/wissen/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)):

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f).$$

Sie untersucht ein Signal also auf zweierlei: auf Frequenzanteile wie die Fourier-Transformation und auf exponentielles Wachsen oder Abklingen. Liegt $\sigma=0$ im Konvergenzbereich, ist die Fourier-Transformierte die Laplace-Transformierte auf der imaginären Achse. Mit Dirac-Impulsen (Stufe [8](singulare-signale-und-linienspektren.html#stufe-8)) fasst die Fourier-Transformation aber auch Signale, die die Laplace-Transformation nicht fasst: Konstanten und Schwingungen über alle Zeiten. Allgemein genügt es, dass $\int|s(t)|\mathrm{e}^{-c|t|}\mathrm{d} t<\infty$ für jedes $c>0$ gilt. Dann darf das Signal wie eine Potenz $t^n$ wachsen, aber nicht exponentiell.

:::zusatz Warum Mehrfachfaltungen gaußförmig werden
Faltet man $M$ Rechtecke $\operatorname{rect}(t)$ miteinander, ist das Spektrum $\operatorname{si}^M(\pi f)$. Für kleine $f$ ist $\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$ und $\ln(1+w)\approx w$, also

$$\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}.$$

Für große $M$ trägt nur der Bereich kleiner $f$ bei, die Näherung wird immer besser. Bei $M=4$ ist der Wert bei $t=0$ exakt $0{,}667$, die Gaußkurve gibt $0{,}691$. Das ist ein Fall des __zentralen Grenzwertsatzes__ (Teil zur Statistik): Die Faltung vieler positiver Impulse endlicher Fläche nähert sich einer Gaußkurve. Ein Beispiel ist die Impulsantwort einer Kette vieler kurzer Integratoren.
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
