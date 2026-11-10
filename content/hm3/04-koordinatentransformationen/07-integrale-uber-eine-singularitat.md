---
title: Stufe 5: Integrale über eine Singularität
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Koordinatentransformationen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen
knoten: Kapitel 4: Koordinatentransformationen
order: 3140700
summary: Das Potential einer Punktladung wächst am Ort der Ladung über alle Grenzen.
tags: Singularität, Coulomb-Potential, lokal integrierbar
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Das Potential einer Punktladung wächst am Ort der Ladung über alle Grenzen. Diese Stufe zeigt, wann ein Integral über eine solche Stelle trotzdem endlich ist: Der Faktor $r^2$ der Kugelkoordinaten dämpft sie.
:::

**Die Idee.** Eine Stelle, an der eine Funktion über alle Grenzen wächst, heißt __Singularität__. Das Integral von $1/|\boldsymbol{x}|^\alpha$ um den Nullpunkt summiert dünne Kugelschalen. Eine Schale mit Radius $r$ und Dicke $\mathrm{d} r$ hat das Volumen $4\pi r^2\,\mathrm{d} r$. Nahe null steigt also der Funktionswert, aber das Volumen fällt. Es entscheidet das Produkt $r^{2-\alpha}$ (Abb. [5](#abb-5)).

:::abbildung hm3/k4singulaer 5
Der Integrand $r^{2-\alpha}$, der nach dem Abspalten der Winkel übrig bleibt. Für $\alpha=\frac52$ wächst er bei $r\to0$, die Fläche darunter bleibt aber endlich. Für $\alpha=3$ ist sie unendlich.
:::

:::satz Satz 5.1 (Majorantenkriterium bei einer Singularität)
<span class="anker" id="satz-5-1"></span>

Sei $f:\mathbb{R}^3\setminus\{0\}\to\mathbb{R}$ stetig, und es gelte $|f(\boldsymbol{x})|\le c/|\boldsymbol{x}|^\alpha$ für alle $\boldsymbol{x}\neq0$ mit einem $\alpha<3$ und einer Konstanten $c>0$. Dann konvergiert für alle $R>0$ das Integral

<span class="anker" id="gl-5-1"></span>
$$\int_{B_R(0)}f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}:=\lim_{\varepsilon\searrow0}\int_{\{\varepsilon\le|\boldsymbol{x}|\le R\}}f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} \tag{5.1}$$

absolut, und es gilt

<span class="anker" id="gl-5-2"></span>
$$\int_{B_R(0)}|f(\boldsymbol{x})|\,\mathrm{d}\boldsymbol{x}\le c\,\frac{4\pi R^{3-\alpha}}{3-\alpha}. \tag{5.2}$$
:::

⁠**So liest man das:** [(5.1)](#gl-5-1) schneidet die Singularität mit einer kleinen Kugel aus und lässt sie schrumpfen, das ist ein uneigentliches Integral. Absolut heißt: Es konvergiert auch mit $|f|$ statt $f$, Vorzeichenwechsel werden also nicht gebraucht. Die Funktion $c/|\boldsymbol{x}|^\alpha$ ist eine Majorante wie in [Kapitel 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html), also eine obere Schranke, die das Integral beherrscht.

:::beweis Majorantenkriterium
⁠**Schritt 1.** Sei $\varepsilon_k\searrow0$ eine Nullfolge und $I(\varepsilon_k)=\int_{\{\varepsilon_k\le|\boldsymbol{x}|\le R\}}f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$.

⁠**Schritt 2.** Für $0<\varepsilon_k<\varepsilon_\ell$ unterscheiden sich $I(\varepsilon_k)$ und $I(\varepsilon_\ell)$ nur um die Schale dazwischen. Mit der Monotonie des Integrals und Kugelkoordinaten folgt

$$|I(\varepsilon_k)-I(\varepsilon_\ell)|\le\int_{\{\varepsilon_k\le|\boldsymbol{x}|\le\varepsilon_\ell\}}|f(\boldsymbol{x})|\,\mathrm{d}\boldsymbol{x}\le4\pi c\int_{\varepsilon_k}^{\varepsilon_\ell}r^{2-\alpha}\,\mathrm{d} r.$$

⁠**Schritt 3.** Wegen $\alpha<3$ ist $3-\alpha>0$, also

$$4\pi c\int_{\varepsilon_k}^{\varepsilon_\ell}r^{2-\alpha}\,\mathrm{d} r=4\pi c\,\frac{\varepsilon_\ell^{3-\alpha}-\varepsilon_k^{3-\alpha}}{3-\alpha}\le\frac{4\pi c}{3-\alpha}\,\varepsilon_\ell^{3-\alpha}\xrightarrow{\ell\to\infty}0.$$

Die Folge $I(\varepsilon_k)$ ist also eine Cauchy-Folge: Ihre Glieder rücken beliebig nah zusammen, und in $\mathbb{R}$ hat eine solche Folge einen Grenzwert. Er hängt nicht von der Nullfolge ab, weil die Abschätzung für je zwei Radien gilt.

⁠**Schritt 4.** Dieselbe Rechnung mit $|f|$ auf $\{\varepsilon\le|\boldsymbol{x}|\le R\}$ gibt die Schranke $\frac{4\pi c}{3-\alpha}(R^{3-\alpha}-\varepsilon^{3-\alpha})$ für jedes $\varepsilon>0$. Das ist [(5.2)](#gl-5-2).
:::

**Warum $\alpha<3$ nötig ist.** Für $f=1/|\boldsymbol{x}|^3$ ist $\int_{\{\varepsilon\le|\boldsymbol{x}|\le R\}}f\,\mathrm{d}\boldsymbol{x}=4\pi\int_\varepsilon^Rr^{-1}\,\mathrm{d} r=4\pi\ln(R/\varepsilon)$, und das wächst für $\varepsilon\searrow0$ über alle Grenzen.

::::beispiel das Coulomb-Potential
Das __Coulomb-Potential__ $\phi(\boldsymbol{x})=\dfrac{1}{4\pi|\boldsymbol{x}|}$ ist das Potential einer Punktquelle im Nullpunkt. Hier ist $c=\frac1{4\pi}$ und $\alpha=1$. Für die Modellkugel ist $\int_{B_2(0)}\frac{1}{|\boldsymbol{x}|}\,\mathrm{d}\boldsymbol{x}=4\pi\int_0^2r\,\mathrm{d} r=8\pi$, und die Schranke mit $c=1$ gibt genau denselben Wert. Die ersten Ableitungen $\partial\phi/\partial x_j=-x_j/(4\pi|\boldsymbol{x}|^3)$ sind bei $\boldsymbol{x}=0$ stärker singulär, sie wachsen wie $1/|\boldsymbol{x}|^2$. Wegen $|\nabla\phi|=\frac1{4\pi|\boldsymbol{x}|^2}$ gilt hier $\alpha=2<3$. Auch sie sind also über jede Kugel um den Nullpunkt integrierbar. Man sagt: $\phi$ und $\nabla\phi$ sind __lokal integrierbar__.
::::

:::frage Wie kann ein Integral endlich sein, wenn die Funktion unendlich wird?
Das gibt es schon in einer Variablen: $\int_0^1x^{-1/2}\,\mathrm{d} x=2$. Der Punkt selbst hat kein Volumen, und die Stücke nahe null sind so klein, dass ihre Beiträge summierbar bleiben. Auf der Zahlengeraden lautet die Grenze $\alpha<1$. Im $\mathbb{R}^3$ kommt der Faktor $r^2$ hinzu, deshalb ist dort mehr erlaubt.
:::

:::aufgabe Aufgabe 9 ★★ Singularitäten abschätzen
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Für welche $\alpha$ ist $\int_{B_1(0)}|\boldsymbol{x}|^{-\alpha}\,\mathrm{d}\boldsymbol{x}$ im $\mathbb{R}^3$ endlich? Berechne den Wert für $\alpha=\frac52$.

</li>

<li>

Sei $f(\boldsymbol{x})=x_1/|\boldsymbol{x}|^3$. Schätze $\int_{B_2(0)}|f|\,\mathrm{d}\boldsymbol{x}$ mit [(5.2)](#gl-5-2) ab und berechne den Wert exakt.

</li>

<li>

Welche Bedingung ergibt sich in der Ebene für $\int_{B_1(0)}|\boldsymbol{x}|^{-\alpha}\,\mathrm{d}\boldsymbol{x}$? Warum ist sie strenger?

</li>

</ol>

:::loesung
(a) $\int_{B_1(0)}|\boldsymbol{x}|^{-\alpha}\,\mathrm{d}\boldsymbol{x}=4\pi\int_0^1r^{2-\alpha}\,\mathrm{d} r$ ist genau für $\alpha<3$ endlich. Für $\alpha=\frac52$: $4\pi\int_0^1r^{-1/2}\,\mathrm{d} r=8\pi$. (b) $|f|\le1/|\boldsymbol{x}|^2$, also $c=1$, $\alpha=2$, und [(5.2)](#gl-5-2) gibt $4\pi\cdot2=8\pi$. Exakt ist $|f|=|\sin\theta\cos\varphi|/r^2$, also

$$\int_{B_2(0)}|f|\,\mathrm{d}\boldsymbol{x}=\int_0^2\mathrm{d} r\int_0^\pi\sin^2\theta\,\mathrm{d}\theta\int_0^{2\pi}|\cos\varphi|\,\mathrm{d}\varphi=2\cdot\frac\pi2\cdot4=4\pi.$$

(c) In der Ebene ist das Integral $2\pi\int_0^1r^{1-\alpha}\,\mathrm{d} r$, endlich genau für $\alpha<2$. Dort dämpft nur der Faktor $r$, nicht $r^2$.
:::
:::
