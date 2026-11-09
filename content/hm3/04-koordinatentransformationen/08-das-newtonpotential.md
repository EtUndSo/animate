---
title: Stufe 6: Das Newtonpotential
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3140800
summary: Eine verteilte Ladung oder Masse erzeugt ein Potential.
tags: kompaktem Träger, Newtonpotential, Poisson-Gleichung, Kugelschale, Schalensatz
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Eine verteilte Ladung oder Masse erzeugt ein Potential. Diese Stufe summiert die Beiträge aller Punktquellen zu einem Integral, nennt die Gleichung, die es löst, und rechnet den wichtigsten Fall aus: die homogen geladene Kugelschale.
:::

**Die Idee.** Das Volumenstück $\mathrm{d}\boldsymbol{y}$ am Ort $\boldsymbol{y}$ enthält die Quellstärke $f(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}$. Am Ort $\boldsymbol{x}$ erzeugt es nach Stufe [5](integrale-uber-eine-singularitat.html#stufe-5) das Potential $f(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}/(4\pi|\boldsymbol{x}-\boldsymbol{y}|)$. Potentiale addieren sich, also ist das Gesamtpotential ein Integral über $\boldsymbol{y}$, das noch vom Parameter $\boldsymbol{x}$ abhängt. Allgemein heißt das ein singuläres Parameterintegral $u(\boldsymbol{x})=\int_{\mathbb{R}^n}K(\boldsymbol{x}-\boldsymbol{y})\,f(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}$ mit einem Kern $K$, der bei 0 singulär ist. Man versteht es wie in Stufe [5](integrale-uber-eine-singularitat.html#stufe-5) durch Abschneiden der Singularität und einen Grenzübergang.

:::satz Satz 6.1 (Newtonpotential)
<span class="anker" id="satz-6-1"></span>

Sei $f:\mathbb{R}^3\to\mathbb{R}$ stetig differenzierbar mit __kompaktem Träger__, also null außerhalb einer beschränkten Menge. Dann existiert für alle $\boldsymbol{x}\in\mathbb{R}^3$ das __Newtonpotential__

<span class="anker" id="gl-6-1"></span>
$$u(\boldsymbol{x})=\frac1{4\pi}\int_{\mathbb{R}^3}\frac{f(\boldsymbol{y})}{|\boldsymbol{x}-\boldsymbol{y}|}\,\mathrm{d}\boldsymbol{y}. \tag{6.1}$$

Die Funktion $u:\mathbb{R}^3\to\mathbb{R}$ ist zweimal stetig differenzierbar und erfüllt die __Poisson-Gleichung__

<span class="anker" id="gl-6-2"></span>
$$-\Delta u=f\quad\text{in }\mathbb{R}^3\qquad\text{mit}\qquad u(\boldsymbol{x})\to0\quad\text{für }|\boldsymbol{x}|\to\infty. \tag{6.2}$$
:::

⁠**So liest man das:** $f$ ist die Quelldichte, etwa Ladung oder Masse je Volumen, $u$ ist das zugehörige Potential, und $\Delta=\operatorname{div}\nabla$ ist der Laplace-Operator aus [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html). Der Satz wird hier ohne Beweis benutzt. Die Existenz folgt aus Stufe [5](integrale-uber-eine-singularitat.html#stufe-5): Nach der Verschiebung $\boldsymbol{y}\mapsto\boldsymbol{x}-\boldsymbol{y}$ ist der Integrand $f(\boldsymbol{x}-\boldsymbol{y})/|\boldsymbol{y}|$ beschränkt durch $c/|\boldsymbol{y}|$ mit $c=\max|f|$, also ist $\alpha=1<3$. Ersetzt man im Nenner $|\boldsymbol{x}-\boldsymbol{y}|$ durch $\max\{|\boldsymbol{x}-\boldsymbol{y}|,\varepsilon\}$, ist der Integrand für jedes $\varepsilon>0$ stetig mit kompaktem Träger. Die Bedingungen lassen sich abschwächen: Statt des kompakten Trägers genügt ein passendes Abklingen von $f(\boldsymbol{x})$ für $|\boldsymbol{x}|\to\infty$.

::::beispiel die Kugelschale
Für $0\le R_1<R_2$ sei $\mathcal S=\{\boldsymbol{y}:R_1\le|\boldsymbol{y}|\le R_2\}$ eine __Kugelschale__ mit konstanter Dichte $\rho>0$. Die Dichte springt am Rand, Satz [6.1](#satz-6-1) ist also nicht direkt anwendbar. Außerhalb von $\mathcal S$ hat das Integral aber gar keine Singularität, und das Potential ist

<span class="anker" id="gl-6-3"></span>
$$u(\boldsymbol{x})=\frac\rho{4\pi}\int_{\mathcal S}\frac{\mathrm{d}\boldsymbol{y}}{|\boldsymbol{x}-\boldsymbol{y}|},\qquad\boldsymbol{x}\notin\mathcal S. \tag{6.3}$$

Die Schale ist drehsymmetrisch, also hängt $u$ nur vom Abstand ab. Lege $\boldsymbol{x}=(0,0,a)$ mit $a>0$ auf die $z$-Achse und schreibe $\boldsymbol{y}$ in Kugelkoordinaten (Abb. [6](#abb-6)). Der Kosinussatz gibt $|\boldsymbol{x}-\boldsymbol{y}|=\sqrt{r^2-2ra\cos\theta+a^2}$.
::::

:::herleitung Potential der Kugelschale
⁠**Schritt 1: Winkel.** $\varphi$ kommt im Integranden nicht vor und gibt $2\pi$:

$$u(\boldsymbol{x})=\frac\rho2\int_{R_1}^{R_2}\Bigl(\int_0^\pi\frac{\sin\theta\,\mathrm{d}\theta}{\sqrt{r^2-2ra\cos\theta+a^2}}\Bigr)r^2\,\mathrm{d} r.$$

⁠**Schritt 2: inneres Integral.** Die Substitution $s=\cos\theta$, $\mathrm{d} s=-\sin\theta\,\mathrm{d}\theta$ gibt

$$\begin{aligned} \int_{-1}^1\frac{\mathrm{d} s}{\sqrt{r^2-2ras+a^2}}&=\Bigl[-\frac1{ra}\sqrt{r^2-2ras+a^2}\Bigr]_{s=-1}^{1}=\frac{(r+a)-|r-a|}{ra}\\ &=\begin{cases}2/a&\text{für }a\ge r,\\2/r&\text{für }a\le r.\end{cases} \end{aligned}$$

Die Fallunterscheidung kommt aus $\sqrt{(r-a)^2}=|r-a|$.

⁠**Schritt 3: radiales Integral.** Außen ist $a\ge R_2\ge r$, innen ist $a\le R_1\le r$. Einsetzen gibt

<span class="anker" id="gl-6-4"></span>
$$u(\boldsymbol{x})=\rho\begin{cases}\dfrac{R_2^3-R_1^3}{3a}&\text{für }a\ge R_2,\\[2mm]\dfrac{R_2^2-R_1^2}{2}&\text{für }a\le R_1.\end{cases} \tag{6.4}$$
:::

:::abbildung hm3/k4schale 6
Links: der Aufpunkt $\boldsymbol{x}$ im Abstand $a$ und ein Punkt $\boldsymbol{y}$ der Schale. Rechts: das Potential für $R_1=1$, $R_2=2$, $\rho=1$. Im Hohlraum ist es konstant, außen folgt es der Kurve einer Punktquelle derselben Stärke, die gestrichelt weiterläuft.
:::

⁠**So liest man das:** Für die Vollkugel, $R_2=R$ und $R_1=0$, wird außen $u(\boldsymbol{x})=\dfrac{Q}{4\pi a}$ mit $Q=\rho|B_R|$, wobei $|B_R|=\frac43\pi R^3$ das Kugelvolumen ist. Das ist genau das Potential einer Punktquelle der Stärke $Q$ im Nullpunkt. Von außen lässt sich also nicht entscheiden, ob Masse oder Ladung homogen in der Kugel verteilt oder in einem Punkt konzentriert ist. Im Hohlraum ist $u$ konstant, also verschwindet die Kraft $-\nabla u$. Das ist der __Schalensatz__. **Modell:** Die Kugel mit $R=2$ und $\rho=1$ hat $Q=\frac{32}3\pi$, also außen $u=\frac8{3a}$ und am Rand $u=\frac43$.

:::frage Warum hebt sich die Kraft im Hohlraum genau auf?
Der nahe Teil der Schale zieht stärker, aber der ferne Teil enthält mehr Ladung. Die Rechnung zeigt, dass beides exakt zusammenpasst: Das Winkelintegral hängt für $a\le r$ nicht von $a$ ab.
:::

:::aufgabe Aufgabe 10 ★★★ Im Inneren der Schale
<span class="anker" id="aufg-10"></span>

Sei $R_1=1$, $R_2=2$, $\rho=1$.

<ol class="al">

<li>

Berechne $u$ für $a=4$ und für $a=\frac12$.

</li>

<li>

Für $R_1\le a\le R_2$ zerfällt das $r$-Integral bei $r=a$. Zeige $u=\rho\bigl(\frac{R_2^2}2-\frac{a^2}6-\frac{R_1^3}{3a}\bigr)$. Warum existiert das Integral, obwohl $\boldsymbol{x}$ in der Schale liegt?

</li>

<li>

Prüfe die Stetigkeit bei $a=1$ und $a=2$.

</li>

<li>

Was ergibt sich in der Vollkugel mit $R_1=0$, $R_2=2$?

</li>

</ol>

:::loesung
(a) $u(4)=\frac{8-1}{3\cdot4}=\frac7{12}$, und für $a=\frac12$ ist $u=\frac{4-1}2=\frac32$. (b) Für $r<a$ ist das Winkelintegral $2/a$, für $r>a$ ist es $2/r$:

$$u=\frac\rho2\Bigl(\int_{R_1}^a\frac2ar^2\,\mathrm{d} r+\int_a^{R_2}\frac2rr^2\,\mathrm{d} r\Bigr)=\rho\Bigl(\frac{a^3-R_1^3}{3a}+\frac{R_2^2-a^2}2\Bigr)=\rho\Bigl(\frac{R_2^2}2-\frac{a^2}6-\frac{R_1^3}{3a}\Bigr).$$

Das Integral existiert nach Stufe [5](integrale-uber-eine-singularitat.html#stufe-5), denn der Kern verhält sich wie $1/|\boldsymbol{x}-\boldsymbol{y}|$, also $\alpha=1<3$. (c) Für $a=1$: $2-\frac16-\frac13=\frac32$, wie im Hohlraum. Für $a=2$: $2-\frac23-\frac16=\frac76$, und außen ist $\frac7{3\cdot2}=\frac76$. (d) $u=2-\frac{a^2}6$ für $a\le2$. Am Rand ist das $\frac43$, wie außen, in der Mitte 2.
:::
:::

Warum die Formel [(6.1)](#gl-6-1) die Poisson-Gleichung löst, zeigt [Teil 5](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum/integralsaetze-im-raum.html).
