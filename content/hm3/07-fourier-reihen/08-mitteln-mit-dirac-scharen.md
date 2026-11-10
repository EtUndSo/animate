---
title: Stufe 7: Mitteln mit Dirac-Scharen
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Fourier-Reihen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/fourier-reihen
knoten: Kapitel 7: Fourier-Reihen
order: 3170800
summary: Für einzelne Stellen braucht man neben der Projektion ein zweites Bild: den gleitenden Mittelwert.
tags: Glättungskern, Dirac-Schar, Faltung, Approximation der Eins, im Distributionssinn, Dirac-Distribution, Dirac-Kamm
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Für einzelne Stellen braucht man neben der Projektion ein zweites Bild: den gleitenden Mittelwert. Diese Stufe zeigt, wann er die Funktion zurückgibt, und führt Faltung und Dirac-Distribution ein.
:::

**Die Idee.** Ersetzt man den Wert $f(x)$ durch einen gewichteten Mittelwert der Werte $f(y)$ nahe bei $x$, wird die Kurve geglättet. Ist das Fenster schmal, zählen nur Werte nah bei $x$, und der Mittelwert liegt nah an $f(x)$. Macht man das Fenster schmaler und hält die Gesamtfläche des Gewichts bei 1, entsteht eine immer höhere Spitze (Abb. [7](#abb-7)).

:::abbildung hm3/k7dirac 7
Links: Gewichte mit der Fläche 1 für drei Fenster der Breite $2\varepsilon$. Die Höhe wächst wie $1/\varepsilon$. Rechts: Mittelt man das Dreieck $w$ mit $\varepsilon=0{,}8$, verschwindet der Knick. Weit weg vom Knick ändert sich nichts, weil ein gerader Abschnitt sein eigener Mittelwert ist.
:::

:::definition Definition 7.1 (Glättungskern und Dirac-Schar)
<span class="anker" id="satz-7-1"></span>

Ein __Glättungskern__ ist eine beliebig oft differenzierbare Funktion $\eta:\mathbb{R}\to[0,\infty)$ mit $\eta(x)=0$ für $|x|\ge1$ und $\int_\mathbb{R}\eta(x)\,\mathrm{d} x=1$. Für $\varepsilon>0$ heißt die Familie $\eta_\varepsilon(x):=\frac1\varepsilon\,\eta(x/\varepsilon)$ eine __Dirac-Schar__. Es gilt $\eta_\varepsilon(x)=0$ für $|x|\ge\varepsilon$ und $\int_\mathbb{R}\eta_\varepsilon(x)\,\mathrm{d} x=1$.
:::

⁠**So liest man das:** Ein Beispiel ist $\eta(x)=\frac1\kappa\exp\bigl(\frac1{x^2-1}\bigr)$ für $|x|<1$ und $\eta(x)=0$ sonst, mit $\kappa=\int_{-1}^1\exp\bigl(\frac1{y^2-1}\bigr)\,\mathrm{d} y\approx0{,}444$. Die Fläche von $\eta_\varepsilon$ bleibt 1 wegen der Substitution $t=x/\varepsilon$.

:::satz Satz 7.2 (Glätten)
<span class="anker" id="satz-7-2"></span>

Sei $f:\mathbb{R}\to\mathbb{R}$ stetig und $f_\varepsilon(x):=\int_\mathbb{R}\eta_\varepsilon(x-y)\,f(y)\,\mathrm{d} y$. Dann ist $f_\varepsilon$ für jedes $\varepsilon>0$ beliebig oft differenzierbar, und für alle $x\in\mathbb{R}$ gilt $f_\varepsilon(x)\to f(x)$ für $\varepsilon\searrow0$. Auf beschränkten Intervallen ist die Konvergenz gleichmäßig.
:::

:::beweis Glätten
⁠**Glattheit.** Für $x$ in einem beschränkten Intervall läuft das Integral nur über ein beschränktes Intervall, denn außerhalb verschwindet $\eta_\varepsilon(x-y)$. Nach dem Satz über Parameterintegrale ([Kapitel 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)) darf man also beliebig oft unter dem Integral ableiten. Alle Ableitungen fallen auf den glatten Kern, $f$ selbst muss nicht differenzierbar sein.

⁠**Konvergenz.** Weil das Gewicht die Fläche 1 hat, ist $f(x)=\int_\mathbb{R}\eta_\varepsilon(x-y)\,f(x)\,\mathrm{d} y$. Wegen $\eta_\varepsilon\ge0$ folgt

<span class="anker" id="gl-7-1"></span>
$$|f(x)-f_\varepsilon(x)|=\Bigl|\int_\mathbb{R}\eta_\varepsilon(x-y)\bigl(f(x)-f(y)\bigr)\,\mathrm{d} y\Bigr|\le\sup_{|x-y|<\varepsilon}|f(x)-f(y)|, \tag{7.1}$$

und das geht wegen der Stetigkeit gegen null. Auf einem beschränkten Intervall ist $f$ gleichmäßig stetig, die Schranke hängt dort also nicht von $x$ ab.
:::

⁠**Wozu Stetigkeit?** Für die Sprungfunktion $f=1$ auf $[0,\infty)$, $f=0$ sonst, und einen geraden Kern ist $f_\varepsilon(0)=\frac12$ für alle $\varepsilon$, also $f_\varepsilon(0)\not\to f(0)$. Das Mittel hört an der Sprungstelle auf beide Seiten.

**Faltung.** Für stetige, uneigentlich absolut integrierbare $f,g:\mathbb{R}\to\mathbb{R}$ heißt

<span class="anker" id="gl-7-2"></span>
$$(f*g)(x):=\int_\mathbb{R} f(x-y)\,g(y)\,\mathrm{d} y \tag{7.2}$$

die __Faltung__ von $f$ und $g$. Sie ist wieder stetig und absolut integrierbar. Die Substitution $z=x-y$ zeigt $f*g=g*f$. Die Faltung ist also eine Art Multiplikation, und $f_\varepsilon=\eta_\varepsilon*f$. Anders als bei der punktweisen Multiplikation gibt es aber kein Einselement: Keine Funktion $g$ erfüllt $f*g=f$ für alle $f$. Eine Dirac-Schar heißt deshalb __Approximation der Eins__: Sie kommt dem fehlenden Einselement beliebig nahe.

**Die Dirac-Distribution.** Dieselbe Abschätzung wie in [(7.1)](#gl-7-1) gibt $\int_\mathbb{R} f(y)\,\eta_\varepsilon(y)\,\mathrm{d} y\to f(0)$ für $\varepsilon\searrow0$. Eine Funktion $\delta$ mit $\int_\mathbb{R} f\delta\,\mathrm{d} y=f(0)$ für alle stetigen $f$ gibt es aber nicht. Für stetiges $\delta$ sieht man das so: Wäre $\delta(y_0)\neq0$ bei $y_0\neq0$, gäbe ein kleiner Buckel $f\ge0$ um $y_0$ ein Integral ungleich null bei $f(0)=0$. Also wäre $\delta=0$ abseits der Null, wegen der Stetigkeit überall, und das Integral stets null. Die Folge $\eta_\varepsilon$ selbst konvergiert auch nicht, ihre Spitze wächst unbegrenzt. Nur die Integrale konvergieren. Man sagt: $\eta_\varepsilon$ konvergiert __im Distributionssinn__ gegen $\delta_0$, und meint

<span class="anker" id="gl-7-3"></span>
$$\lim_{\varepsilon\searrow0}\int_\mathbb{R} f(y)\,\eta_\varepsilon(y)\,\mathrm{d} y=f(0)=:\int_\mathbb{R} f(y)\,\delta_0(\mathrm{d} y). \tag{7.3}$$

:::definition Definition 7.3 (Dirac-Distribution)
<span class="anker" id="satz-7-3"></span>

Für $x\in\mathbb{R}$, $I\subset\mathbb{R}$ und stetiges $f$ setzt man

$$\int_If(y)\,\delta_x(\mathrm{d} y):=\begin{cases}f(x)&x\in I,\\0&x\notin I,\end{cases}\qquad\delta_x(I):=\int_I\delta_x(\mathrm{d} y)=\begin{cases}1&x\in I,\\0&x\notin I.\end{cases}$$

Eine gleichwertige Schreibweise ist $\int_If\,\mathrm{d}\delta_x$. Das Objekt $\delta_x$ heißt __Dirac-Distribution__, $\delta_x(I)$ ist die zugehörige Längenmessung.
:::

⁠**So liest man das:** $\delta_x$ wertet $f$ an der Stelle $x$ aus. Es trägt einen Index und ist nicht das Kronecker-Symbol $\delta_{k\ell}$. Anders als das Riemann-Integral bemerkt dieses Integral, ob ein Intervall seinen Rand enthält: $\delta_0([0,1])=1$, aber $\delta_0((0,1))=0$.

**Fourier-Koeffizienten von $\delta_0$.** Setzt man $\delta_0$ mit der Periode $2\pi$ fort, entsteht der __Dirac-Kamm__. Über eine Periode, die $0$ genau einmal enthält, gilt formal $c_k=\frac1{2\pi}\int\mathrm{e}^{-\mathrm{i}kx}\,\delta_0(\mathrm{d} x)=\frac1{2\pi}$ für alle $k\in\mathbb{Z}$. Alle Frequenzen sind gleich stark vertreten. Das lässt vermuten, dass $\frac1{2\pi}\sum_{|k|\le N}\mathrm{e}^{\mathrm{i}kx}$ für $N\to\infty$ im Distributionssinn gegen $\delta_0$ konvergiert, dass diese Summe also ebenfalls wie eine Dirac-Schar mittelt.

:::aufgabe Aufgabe 8 ★★ Ein Kern zum Rechnen
<span class="anker" id="aufg-8"></span>

Sei $\eta(x)=\frac34(1-x^2)$ für $|x|<1$ und $\eta(x)=0$ sonst. Dieser Kern ist nicht glatt, für diese Rechnung reicht er aber.

<ol class="al">

<li>

Prüfe $\int_\mathbb{R}\eta\,\mathrm{d} x=1$. Berechne $f_\varepsilon$ für $f(x)=x^2$. Wie groß ist der Fehler, und hängt er von $x$ ab?

</li>

<li>

Bestimme $\int_{[-1,1]}\cos y\,\delta_0(\mathrm{d} y)$, $\int_{(0,2)}y^2\,\delta_1(\mathrm{d} y)$, $\int_{(0,1)}y^2\,\delta_1(\mathrm{d} y)$ und $\delta_1([0,1])$.

</li>

</ol>

:::loesung
(a) $\frac34(2-\frac23)=1$. Mit der Substitution $y\mapsto x-y$ und dem geraden Kern ist $f_\varepsilon(x)=\int\eta_\varepsilon(y)(x-y)^2\,\mathrm{d} y=x^2-2x\int y\,\eta_\varepsilon\,\mathrm{d} y+\int y^2\eta_\varepsilon\,\mathrm{d} y$. Das mittlere Integral ist null, das letzte ist $\varepsilon^2\int t^2\eta(t)\,\mathrm{d} t=\frac{\varepsilon^2}5$. Also ist $f_\varepsilon(x)=x^2+\frac{\varepsilon^2}5$. Der Fehler hängt nicht von $x$ ab. (b) $\cos0=1$; $1^2=1$, weil $1\in(0,2)$; $0$, weil $1\notin(0,1)$; $\delta_1([0,1])=1$.
:::
:::
