---
title: Wichtige Verteilungen
pfad: Informatik / Machine Learning / Wahrscheinlichkeit
order: 6240900
summary: Einige Verteilungen kommen so oft vor, dass sie Namen haben.
tags: Bernoulli-verteilt, Kategorien, kategorisch verteilt, One-Hot-Kodierung, Binomialkoeffizient, binomialverteilt, gleichverteilt, Histogramm
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Einige Verteilungen kommen so oft vor, dass sie Namen haben. Dieser Abschnitt stellt fünf davon vor: die Verteilung eines Ja-Nein-Ausgangs, die Verteilung einer Kategorie aus mehreren, die Anzahl der Erfolge in mehreren Versuchen, die gleichmäßige Verteilung auf einem Intervall und die Normalverteilung. Jede bekommt ihre Formel, ihren Erwartungswert und ihre Varianz und eine typische Anwendung. Am Ende steht das einfachste Modell für verrauschte Messwerte.
:::

### Die Bernoulli-Verteilung

<span class="anker" id="stufe-8-1"></span>

Viele Experimente haben nur zwei Ausgänge: Ein Bauteil ist defekt oder nicht, ein Prüfgerät gibt Alarm oder nicht, eine Münze zeigt Kopf oder Zahl. Man kodiert den einen Ausgang mit $1$ und nennt ihn Erfolg, den anderen mit $0$. Dann bestimmt eine einzige Zahl die ganze Verteilung, die Wahrscheinlichkeit des Erfolgs.

:::definition Definition 8.1 (Bernoulli-Verteilung)
<span class="anker" id="satz-8-1"></span>

Eine Zufallsvariable $X$ mit den Werten $0$ und $1$ und

<span class="anker" id="gl-8-1"></span>
$$P(X=1)=\theta,\qquad P(X=0)=1-\theta \tag{8.1}$$

für eine Zahl $\theta\in[0,\,1]$ heißt __Bernoulli-verteilt__ mit dem Parameter $\theta$, kurz $X\sim\mathrm{Ber}(\theta)$.
:::

Beide Fälle passen in eine Formel: $P(X=x)=\theta^x(1-\theta)^{1-x}$ für $x\in\{0,1\}$, denn für $x=1$ bleibt $\theta$ und für $x=0$ bleibt $1-\theta$. Den Parameter nennt dieses Kapitel $\theta$, weil $\pi$ die Kreiszahl bleiben soll und $\mu$ schon für Erwartungswerte steht. Jede Indikatorvariable $\mathbb 1_A$ aus Unterabschnitt [7.3](erwartungswert-und-varianz.html#stufe-7-3) ist Bernoulli-verteilt mit $\theta=P(A)$.

:::satz Satz 8.2 (Erwartungswert und Varianz der Bernoulli-Verteilung)
<span class="anker" id="satz-8-2"></span>

Für $X\sim\mathrm{Ber}(\theta)$ ist $\mathbb{E}[X]=\theta$ und $\operatorname{Var}(X)=\theta\,(1-\theta)$.
:::

Denn $\mathbb{E}[X]=0\cdot(1-\theta)+1\cdot\theta=\theta$, und weil $X^2=X$ für die Werte $0$ und $1$ gilt, ist $\mathbb{E}[X^2]=\theta$ und nach der Verschiebungsformel $\operatorname{Var}(X)=\theta-\theta^2$. Die Varianz ist am größten, nämlich $\tfrac14$, bei $\theta=\tfrac12$, und null bei $\theta=0$ und $\theta=1$: Am unsichersten ist ein Ja-Nein-Ausgang, wenn beide Ausgänge gleich wahrscheinlich sind.

⁠**Rechenbeispiel:** Ob das Prüfgerät aus Unterabschnitt [4.2](der-satz-von-bayes.html#stufe-4-2) bei einem intakten Teil Alarm gibt, ist $\mathrm{Ber}(0{,}05)$-verteilt. Der Erwartungswert ist $0{,}05$, die Varianz $0{,}05\cdot0{,}95=0{,}0475$ und die Standardabweichung etwa $0{,}218$.

⁠**Kurz gesagt:** Eine Bernoulli-verteilte Größe ist $1$ mit der Wahrscheinlichkeit $\theta$ und sonst $0$; Erwartungswert $\theta$, Varianz $\theta(1-\theta)$.

### Die kategorische Verteilung

<span class="anker" id="stufe-8-2"></span>

Hat ein Experiment mehr als zwei Ausgänge ohne natürliche Reihenfolge, etwa die Farbe eines Bauteils oder die Sorte einer Frucht, so verallgemeinert man die Bernoulli-Verteilung. Die Ausgänge heißen __Kategorien__; man nummeriert sie $1,\dots,K$, aber die Nummern sind nur Namen.

:::definition Definition 8.3 (Kategorische Verteilung)
<span class="anker" id="satz-8-3"></span>

Eine Zufallsvariable mit den Werten $1,\dots,K$ und $P(\text{Kategorie }k)=\theta_k$, wobei $\theta_k\ge0$ und $\sum_{k=1}^K\theta_k=1$, heißt __kategorisch verteilt__ mit dem Parametervektor $\boldsymbol{\theta}=(\theta_1,\dots,\theta_K)^{\top}$.
:::

Rechnen lässt sich besser mit einer Darstellung als Vektor. Die __One-Hot-Kodierung__ schreibt die Kategorie $k$ als Einheitsvektor $\mathbf{e}_k\in\mathbb{R}^K$ aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 1.6: eine $1$ an der Stelle $k$, sonst Nullen. Ist $\mathbf{y}$ die so kodierte Kategorie, so ist $P(\mathbf{y})=\prod_{k=1}^K\theta_k^{y_k}$, denn im Produkt bleibt nur der Faktor mit $y_k=1$ übrig. Jede Komponente $y_k$ ist eine Indikatorvariable der Kategorie $k$ und hat den Erwartungswert $\theta_k$. Die Bernoulli-Verteilung ist der Fall $K=2$.

:::warnung Kategorien haben keinen Erwartungswert
Nummeriert man die Farben Rot, Grün und Blau mit $1$, $2$ und $3$, so ist der „Erwartungswert“ der Nummer eine Zahl ohne Bedeutung: Eine andere Nummerierung ergäbe eine andere Zahl, und die Farbe „$1{,}7$“ gibt es nicht. Erwartungswerte und Varianzen bildet man nur für Zahlen, die wirklich Größen messen. Für Kategorien rechnet man mit den Wahrscheinlichkeiten $\theta_k$ oder mit der One-Hot-Kodierung.
:::

⁠**Rechenbeispiel:** Bauteile sind mit den Wahrscheinlichkeiten $0{,}5$, $0{,}3$ und $0{,}2$ rot, grün oder blau. Ein grünes Teil hat die One-Hot-Kodierung $\mathbf{y}=(0,\,1,\,0)^{\top}$ und $P(\mathbf{y})=0{,}5^0\cdot0{,}3^1\cdot0{,}2^0=0{,}3$. Die kodierten Vektoren haben komponentenweise die Erwartungswerte $(0{,}5;\ 0{,}3;\ 0{,}2)^{\top}=\boldsymbol{\theta}$.

⁠**Kurz gesagt:** Die kategorische Verteilung gibt jeder von $K$ Kategorien eine Wahrscheinlichkeit $\theta_k$; mit der One-Hot-Kodierung ist sie $\prod_k\theta_k^{y_k}$.

### Die Binomialverteilung

<span class="anker" id="stufe-8-3"></span>

Aus einer laufenden Fertigung mit $5\,\%$ Ausschuss prüft man $10$ Teile. Wie viele defekte sind dabei? Jedes Teil ist ein Bernoulli-Versuch, und die Versuche beeinflussen sich nicht. Gefragt ist die Verteilung der Anzahl der Erfolge.

Dafür braucht man eine Abzählung. Die Anzahl der Möglichkeiten, aus $n$ Plätzen $m$ auszuwählen, ohne auf die Reihenfolge zu achten, ist der __Binomialkoeffizient__

$$\binom nm=\frac{n!}{m!\,(n-m)!}=\frac{n\,(n-1)\cdots(n-m+1)}{m!},$$

mit $n!=1\cdot2\cdots n$ und $0!=1$. Man wählt den ersten Platz auf $n$ Arten, den zweiten auf $n-1$ und so fort; die $m!$ Reihenfolgen derselben Auswahl zählt man nur einmal. Zum Beispiel ist $\binom42=\frac{4\cdot3}{2}=6$.

:::definition Definition 8.4 (Binomialverteilung)
<span class="anker" id="satz-8-4"></span>

Es seien $n$ unabhängige Versuche gegeben, jeder mit der Erfolgswahrscheinlichkeit $\theta$. Die Anzahl $X$ der Erfolge hat

<span class="anker" id="gl-8-2"></span>
$$P(X=m)=\binom nm\theta^m(1-\theta)^{n-m},\qquad m=0,1,\dots,n . \tag{8.2}$$

$X$ heißt __binomialverteilt__, kurz $X\sim\mathrm{Bin}(n,\theta)$.
:::

Jede bestimmte Folge mit $m$ Erfolgen und $n-m$ Misserfolgen hat wegen der Unabhängigkeit die Wahrscheinlichkeit $\theta^m(1-\theta)^{n-m}$, und es gibt $\binom nm$ solcher Folgen, je eine für jede Auswahl der Erfolgsplätze. $X$ ist die Summe von $n$ Indikatorvariablen mit dem Erwartungswert $\theta$, also ist nach der Linearität

<span class="anker" id="gl-8-3"></span>
$$\mathbb{E}[X]=n\,\theta . \tag{8.3}$$

Die Anzahl der Köpfe bei drei Münzwürfen aus Unterabschnitt [6.1](zufallsvariablen-und-verteilungen.html#stufe-6-1) ist $\mathrm{Bin}(3,\tfrac12)$-verteilt: $\binom3m\cdot\tfrac18$ ergibt $\tfrac18,\tfrac38,\tfrac38,\tfrac18$.

⁠**Rechenbeispiel:** Für $10$ Teile bei $5\,\%$ Ausschuss ist $X\sim\mathrm{Bin}(10;\ 0{,}05)$. Es ist $P(X=0)=0{,}95^{10}\approx0{,}599$, $P(X=1)=10\cdot0{,}05\cdot0{,}95^9\approx0{,}315$ und $P(X\ge2)=1-0{,}599-0{,}315\approx0{,}086$. Im Mittel findet man $\mathbb{E}[X]=10\cdot0{,}05=0{,}5$ defekte Teile.

⁠**Kurz gesagt:** Die Anzahl der Erfolge in $n$ unabhängigen Versuchen mit Erfolgswahrscheinlichkeit $\theta$ ist binomialverteilt mit $P(X=m)=\binom nm\theta^m(1-\theta)^{n-m}$ und $\mathbb{E}[X]=n\theta$.

### Die Gleichverteilung

<span class="anker" id="stufe-8-4"></span>

Weiß man über eine Größe nur, dass sie in einem Intervall liegt, und gibt es keinen Grund, einen Teil des Intervalls zu bevorzugen, so verteilt man die Wahrscheinlichkeit gleichmäßig. Der Eintreffzeitpunkt aus Unterabschnitt [6.4](zufallsvariablen-und-verteilungen.html#stufe-6-4) war so verteilt.

:::definition Definition 8.5 (Gleichverteilung)
<span class="anker" id="satz-8-5"></span>

$X$ heißt __gleichverteilt__ auf dem Intervall $[a,\,b]$ mit $a<b$, kurz $X\sim\mathcal U(a,b)$, wenn $X$ die Dichte

<span class="anker" id="gl-8-4"></span>
$$p(x)=\frac1{b-a}\quad\text{für }a\le x\le b,\qquad p(x)=0\quad\text{sonst} \tag{8.4}$$

hat.
:::

Die Höhe $1/(b-a)$ sorgt für die Gesamtfläche $1$. Die Wahrscheinlichkeit eines Teilintervalls ist sein Anteil an der Länge von $[a,\,b]$.

:::satz Satz 8.6 (Erwartungswert und Varianz der Gleichverteilung)
<span class="anker" id="satz-8-6"></span>

Für $X\sim\mathcal U(a,b)$ ist $\mathbb{E}[X]=\dfrac{a+b}2$ und $\operatorname{Var}(X)=\dfrac{(b-a)^2}{12}$.
:::

:::herleitung Varianz der Gleichverteilung
Der Erwartungswert ist die Mitte, weil die Dichte symmetrisch um sie ist. Für die Varianz verschiebt man so, dass die Mitte bei $0$ liegt; das ändert die Varianz nach [(7.8)](erwartungswert-und-varianz.html#gl-7-8) nicht. Mit $h=(b-a)/2$ ist $Y=X-\tfrac{a+b}2$ gleichverteilt auf $[-h,\,h]$ mit der Dichte $1/(2h)$, also

$$\operatorname{Var}(X)=\mathbb{E}[Y^2]=\int_{-h}^hy^2\,\frac1{2h}\,\mathrm{d} y=\frac1{2h}\cdot\frac{2h^3}3=\frac{h^2}3=\frac{(b-a)^2}{12} .$$
:::

⁠**Rechenbeispiel: Quantisierungsrauschen.** Ein Analog-Digital-Umsetzer rundet jede Spannung auf das nächste Vielfache einer Stufe $\Delta$. Der Rundungsfehler liegt zwischen $-\Delta/2$ und $\Delta/2$. Ändert sich das Signal über viele Stufen, so ist kein Fehlerwert bevorzugt, und man beschreibt ihn als gleichverteilt auf $[-\Delta/2,\,\Delta/2]$. Er hat dann den Erwartungswert $0$ und die Varianz $\Delta^2/12$, die Leistung des Quantisierungsrauschens. Bei $\Delta=1\,\mathrm{mV}$ ist seine Standardabweichung $1\,\mathrm{mV}/\sqrt{12}\approx0{,}289\,\mathrm{mV}$.

⁠**Kurz gesagt:** Die Gleichverteilung auf $[a,\,b]$ hat die konstante Dichte $1/(b-a)$, den Erwartungswert in der Mitte und die Varianz $(b-a)^2/12$.

### Die Normalverteilung

<span class="anker" id="stufe-8-5"></span>

Misst man dieselbe Größe oft, so häufen sich die Messwerte um einen mittleren Wert, werden nach beiden Seiten gleichmäßig seltener, und sehr große Abweichungen kommen praktisch nicht vor. Teilt man die Zahlengerade in gleich breite Intervalle und zeichnet über jedem einen Balken, so hoch wie die Zahl der Messwerte darin, so entsteht ein __Histogramm__, und es sieht aus wie eine Glocke. Dieselbe Glockenform zeigen das Rauschen eines Widerstands, die Streuung von Bauteilwerten in einer Fertigung und Mittelwerte vieler Messungen. Abschnitt [13](mittelwerte-vieler-zufallsvariablen.html#stufe-13) erklärt, warum. Die Glocke hat eine feste mathematische Form.

:::definition Definition 8.7 (Normalverteilung)
<span class="anker" id="satz-8-7"></span>

$X$ heißt __normalverteilt__ mit den Parametern $\mu\in\mathbb{R}$ und $\sigma^2>0$, kurz $X\sim\mathcal N(\mu,\sigma^2)$, wenn $X$ die Dichte

<span class="anker" id="gl-8-5"></span>
$$p(x)=\frac1{\sqrt{2\pi\sigma^2}}\,\exp\Bigl(-\frac{(x-\mu)^2}{2\sigma^2}\Bigr) \tag{8.5}$$

hat. Mit $\mu=0$ und $\sigma^2=1$ heißt sie __Standardnormalverteilung__.
:::

Die Dichte hängt von $x$ nur über die quadrierte Abweichung $(x-\mu)^2$ ab, gemessen in Einheiten von $\sigma^2$. Sie ist deshalb symmetrisch um $\mu$ und dort am höchsten, mit dem Wert $1/(\sigma\sqrt{2\pi})$. Bei $\mu\pm\sigma$ ist sie auf $\mathrm{e}^{-1/2}\approx0{,}61$ ihres Höchstwerts gefallen; dort wechselt die Krümmung ihr Vorzeichen. Weil $\mathrm{e}^{-t^2/2}$ sehr schnell gegen null geht, fällt die Dichte jenseits von $\mu\pm3\sigma$ kaum noch ins Gewicht. Der Vorfaktor $1/\sqrt{2\pi\sigma^2}$ sorgt für die Gesamtfläche $1$.

:::satz Satz 8.8 (Erwartungswert und Varianz der Normalverteilung)
<span class="anker" id="satz-8-8"></span>

Für $X\sim\mathcal N(\mu,\sigma^2)$ ist $\mathbb{E}[X]=\mu$ und $\operatorname{Var}(X)=\sigma^2$. Die Wahrscheinlichkeiten für Abweichungen von höchstens einer, zwei und drei Standardabweichungen sind

<span class="anker" id="gl-8-6"></span>
$$P(|X-\mu|\le\sigma)\approx0{,}683,\qquad P(|X-\mu|\le2\sigma)\approx0{,}954,\qquad P(|X-\mu|\le3\sigma)\approx0{,}997 . \tag{8.6}$$
:::

Die Zahlen [(8.6)](#gl-8-6) heißen __68-95-99,7-Regel__ (Abb. [11](#abb-11)). Sie gelten für jede Normalverteilung, gleich welche Parameter sie hat; Unterabschnitt [8.6](#stufe-8-6) zeigt, warum.

:::abbildung ml/k4normal 11
Die Dichte der Normalverteilung $\mathcal N(\mu,\sigma^2)$. Zwischen $\mu-\sigma$ und $\mu+\sigma$ liegt die Fläche $0{,}683$, zwischen $\mu\pm2\sigma$ die Fläche $0{,}954$, zwischen $\mu\pm3\sigma$ die Fläche $0{,}997$. An den Stellen $\mu\pm\sigma$ wechselt die Kurve von nach unten gekrümmt zu nach oben gekrümmt.
:::

:::herleitung Warum der Vorfaktor $1/\sqrt{2\pi}$ ist
Es genügt, $I=\int_{-\infty}^\infty\mathrm{e}^{-x^2/2}\,\mathrm{d} x=\sqrt{2\pi}$ zu zeigen; die Substitution $x=(t-\mu)/\sigma$ führt die allgemeine Dichte darauf zurück. Eine Stammfunktion von $\mathrm{e}^{-x^2/2}$ lässt sich nicht mit den üblichen Funktionen hinschreiben. Man berechnet deshalb $I^2$ als Integral über die Ebene:

$$I^2=\int_{-\infty}^\infty\mathrm{e}^{-x^2/2}\,\mathrm{d} x\int_{-\infty}^\infty\mathrm{e}^{-y^2/2}\,\mathrm{d} y=\iint_{\mathbb{R}^2}\mathrm{e}^{-(x^2+y^2)/2}\,\mathrm{d} x\,\mathrm{d} y .$$

Der Integrand hängt nur vom Abstand $r=\sqrt{x^2+y^2}$ zum Nullpunkt ab. In Polarkoordinaten wird das Flächenstück $\mathrm{d} x\,\mathrm{d} y$ zu $r\,\mathrm{d} r\,\mathrm{d}\varphi$, mit dem Flächenfaktor $r$ aus dem Hintergrund-Kasten in [Teil 3](/wissen/informatik/machine-learning/ableitung-gradient-und-kettenregel/ableitung-gradient-und-kettenregel.html), Abschnitt 5.4. Damit ist

$$I^2=\int_0^{2\pi}\!\!\int_0^\infty\mathrm{e}^{-r^2/2}\,r\,\mathrm{d} r\,\mathrm{d}\varphi=2\pi\Bigl[-\mathrm{e}^{-r^2/2}\Bigr]_0^\infty=2\pi ,$$

denn der Faktor $r$ macht den Integranden zur Ableitung von $-\mathrm{e}^{-r^2/2}$. Also ist $I=\sqrt{2\pi}$. Der Erwartungswert ist $\mu$, weil die Dichte symmetrisch um $\mu$ ist. Für die Varianz integriert man $\int x^2\mathrm{e}^{-x^2/2}\,\mathrm{d} x$ partiell mit $u=x$ und $v'=x\,\mathrm{e}^{-x^2/2}$, $v=-\mathrm{e}^{-x^2/2}$; das ergibt wieder $I$, also $\operatorname{Var}=1$ für die Standardnormalverteilung und $\sigma^2$ nach Strecken um $\sigma$.
:::

⁠**Rechenbeispiel:** Widerstände einer Fertigung mit dem Sollwert $100\,\Omega$ seien normalverteilt mit $\mu=100\,\Omega$ und $\sigma=1\,\Omega$. Dann liegen $95{,}4\,\%$ zwischen $98$ und $102\,\Omega$ und $99{,}7\,\%$ zwischen $97$ und $103\,\Omega$. Die Dichte hat bei $100\,\Omega$ den Wert $1/\sqrt{2\pi}\approx0{,}399$ pro Ohm. Nach [(6.3)](zufallsvariablen-und-verteilungen.html#gl-6-3) liegen also etwa $0{,}399\cdot0{,}1\approx4\,\%$ der Widerstände zwischen $99{,}95$ und $100{,}05\,\Omega$.

⁠**Kurz gesagt:** Die Normalverteilung $\mathcal N(\mu,\sigma^2)$ ist die symmetrische Glocke um $\mu$ mit der Standardabweichung $\sigma$; innerhalb von $\pm\sigma$, $\pm2\sigma$, $\pm3\sigma$ liegen $68{,}3$, $95{,}4$ und $99{,}7\,\%$.

### Standardisieren und die Verteilungsfunktion $\Phi$

<span class="anker" id="stufe-8-6"></span>

Für jede Wahrscheinlichkeit einer normalverteilten Größe braucht man ein Integral über [(8.5)](#gl-8-5), und dieses Integral hat keine Formel mit den üblichen Funktionen. Man braucht aber nur eine einzige Tabelle, die der Standardnormalverteilung, denn jede Normalverteilung lässt sich auf sie zurückführen.

:::satz Satz 8.9 (Standardisieren einer Normalverteilung)
<span class="anker" id="satz-8-9"></span>

Ist $X\sim\mathcal N(\mu,\sigma^2)$, so ist $Z=(X-\mu)/\sigma\sim\mathcal N(0,1)$. Mit der Verteilungsfunktion der Standardnormalverteilung

<span class="anker" id="gl-8-7"></span>
$$\Phi(z)=\int_{-\infty}^z\frac1{\sqrt{2\pi}}\,\mathrm{e}^{-t^2/2}\,\mathrm{d} t \tag{8.7}$$

ist $P(X\le x)=\Phi\bigl((x-\mu)/\sigma\bigr)$.
:::

:::beweis Standardisieren
$P(Z\le z)=P(X\le\mu+\sigma z)=\int_{-\infty}^{\mu+\sigma z}\frac1{\sqrt{2\pi}\,\sigma}\,\mathrm{e}^{-(x-\mu)^2/(2\sigma^2)}\,\mathrm{d} x$. Mit der Substitution $t=(x-\mu)/\sigma$, $\mathrm{d} x=\sigma\,\mathrm{d} t$, wird die obere Grenze zu $z$, und der Faktor $\sigma$ kürzt sich gegen das $\sigma$ im Nenner. Übrig bleibt $\Phi(z)$.
:::

Nach Unterabschnitt [7.6](erwartungswert-und-varianz.html#stufe-7-6) hat $Z$ den Erwartungswert $0$ und die Varianz $1$ für jede Verteilung von $X$. Neu ist hier, dass die Verteilung von $Z$ wieder eine Normalverteilung ist. Deshalb hängen die Wahrscheinlichkeiten in [(8.6)](#gl-8-6) nicht von $\mu$ und $\sigma$ ab: $P(|X-\mu|\le k\sigma)=P(|Z|\le k)=2\Phi(k)-1$. Weil die Dichte symmetrisch ist, gilt $\Phi(-z)=1-\Phi(z)$. Einige Werte, die man immer wieder braucht:

|  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| $z$ | $0$ | $1$ | $1{,}645$ | $1{,}960$ | $2$ | $3$ |
| $\Phi(z)$ | $0{,}5$ | $0{,}8413$ | $0{,}950$ | $0{,}975$ | $0{,}9772$ | $0{,}99865$ |

Insbesondere liegen $95\,\%$ einer Normalverteilung zwischen $\mu-1{,}96\,\sigma$ und $\mu+1{,}96\,\sigma$.

⁠**Rechenbeispiel:** Für die Widerstände mit $\mu=100\,\Omega$ und $\sigma=1\,\Omega$ und den Widerstandswert $X$ ist $P(X>102\,\Omega)=1-\Phi(2)\approx0{,}0228$ und $P(X\le101\,\Omega)=\Phi(1)\approx0{,}841$. Toleriert man $\pm2{,}5\,\Omega$, so liegen $2\Phi(2{,}5)-1\approx0{,}988$ der Widerstände im Toleranzband.

⁠**Kurz gesagt:** Jede Normalverteilung wird durch $Z=(X-\mu)/\sigma$ zur Standardnormalverteilung; deshalb genügt die eine Funktion $\Phi$ für alle Wahrscheinlichkeiten.

:::hintergrund Dichten unter Umrechnung: der Variablenwechsel
Der Beweis oben ist ein Fall einer allgemeinen Regel. Ist $Y=g(X)$ mit einer streng monotonen, differenzierbaren Funktion $g$, so ist $P(y\le Y\le y+\Delta y)=P(x\le X\le x+\Delta x)$ für die zugehörigen Intervalle, mit $y=g(x)$. Nach [(6.3)](zufallsvariablen-und-verteilungen.html#gl-6-3) ist also $p_Y(y)\,|\Delta y|\approx p_X(x)\,|\Delta x|$, und im Grenzfall

$$p_Y(y)=p_X(x)\,\Bigl|\frac{\mathrm{d} x}{\mathrm{d} y}\Bigr|,\qquad x=g^{-1}(y).$$

Der Betrag steht da, weil eine fallende Funktion die Intervalle umdreht. Die Dichte wird nicht einfach mitgenommen: Wo $g$ Intervalle staucht, steigt die Dichte, wo $g$ sie streckt, sinkt sie. Ein häufiger Fehler ist, den Faktor zu vergessen. Für $X\sim\mathcal U(0,1)$ und $Y=X/2$ ergäbe $p_Y(y)=p_X(2y)=1$ auf $[0,\,\tfrac12]$ eine Gesamtfläche von nur $\tfrac12$; richtig ist $p_Y=2$. Für Zufallsvektoren tritt an die Stelle von $|\mathrm{d} x/\mathrm{d} y|$ der Betrag der Determinante der Jacobi-Matrix der Umkehrabbildung, der Flächen- oder Volumenfaktor aus [Teil 3](/wissen/informatik/machine-learning/ableitung-gradient-und-kettenregel/ableitung-gradient-und-kettenregel.html), Abschnitt 5.4. Eine Anwendung erzeugt Zufallszahlen: Ist $U\sim\mathcal U(0,1)$ und $F$ eine stetige, streng steigende Verteilungsfunktion, so hat $X=F^{-1}(U)$ die Verteilungsfunktion $F$, denn $P(X\le x)=P(U\le F(x))=F(x)$. So machen Rechner aus gleichverteilten Zufallszahlen Zufallszahlen beliebiger Verteilung.
:::

### Rauschen als Zufallsvariable

<span class="anker" id="stufe-8-7"></span>

Mit den Verteilungen lässt sich beschreiben, was eine Messung liefert. Ein Sensor soll eine Temperatur $w$ messen. Er liefert aber $w$ plus eine kleine, zufällige Störung, die bei jeder Messung anders ausfällt. Man trennt den Messwert in einen festen und einen zufälligen Teil.

:::definition Definition 8.10 (Additives Rauschen)
<span class="anker" id="satz-8-10"></span>

Ein Messwert mit __additivem Rauschen__ ist eine Zufallsvariable

<span class="anker" id="gl-8-8"></span>
$$Y=w+\nu, \tag{8.8}$$

wobei $w$ der feste wahre Wert ist und die Zufallsvariable $\nu$, das __Rauschen__, den Erwartungswert $0$ hat. Ist $\nu\sim\mathcal N(0,\sigma^2)$, so heißt das Rauschen __normalverteilt__; dann ist $Y\sim\mathcal N(w,\sigma^2)$.
:::

Wie beim Funkkanal mit mehreren Antennen in [Teil 2](/wissen/informatik/machine-learning/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html), Abschnitt 9.8, heißt das Rauschen $\nu$ (gesprochen „nü“); es trägt als skalare Zufallsvariable ausnahmsweise einen kleinen Buchstaben, weil $N$ schon die Zahl der Datenpunkte ist. Der Erwartungswert $0$ bedeutet, dass das Gerät im Mittel richtig misst; einen festen Versatz würde man zu $w$ zählen und durch Kalibrieren entfernen. Die Standardabweichung $\sigma$ beschreibt die Güte des Geräts. Viele Verfahren, die aus Daten lernen, beschreiben ihre Daten genau so: als einen Anteil, den man erklären möchte, plus Rauschen. Die Normalverteilung ist dabei die Standardannahme für das Rauschen; Abschnitt [13](mittelwerte-vieler-zufallsvariablen.html#stufe-13) begründet sie.

⁠**Rechenbeispiel:** Ein Temperatursensor habe normalverteiltes Rauschen mit $\sigma=0{,}5\,\mathrm K$. Der wahre Wert sei $20\,{}^\circ\mathrm C$. Ein Messwert weicht dann mit der Wahrscheinlichkeit $P(|\nu|>1\,\mathrm K)=P(|Z|>2)=1-0{,}954=0{,}046$ um mehr als $1\,\mathrm K$ ab, also bei etwa jeder zweiundzwanzigsten Messung.

⁠**Kurz gesagt:** Ein verrauschter Messwert ist wahrer Wert plus eine Zufallsvariable mit Erwartungswert $0$; meist nimmt man für sie eine Normalverteilung an.

:::aufgabe Aufgabe 22 ★ Ausschuss in einer Stichprobe
<span class="anker" id="aufg-22"></span>

Aus einer Fertigung mit $10\,\%$ Ausschuss werden $20$ Teile unabhängig geprüft.

<ol class="al">

<li>

Wie wahrscheinlich ist kein Teil defekt, wie wahrscheinlich höchstens eines?

</li>

<li>

Wie viele defekte Teile erwartet man?

</li>

</ol>

:::loesung
(a) $X\sim\mathrm{Bin}(20;\ 0{,}1)$: $P(X=0)=0{,}9^{20}\approx0{,}122$ und $P(X=1)=20\cdot0{,}1\cdot0{,}9^{19}\approx0{,}270$, also $P(X\le1)\approx0{,}392$.

(b) $\mathbb{E}[X]=20\cdot0{,}1=2$.
:::
:::

:::aufgabe Aufgabe 23 ★★ Widerstände
<span class="anker" id="aufg-23"></span>

Widerstände seien normalverteilt mit $\mu=100\,\Omega$ und $\sigma=2\,\Omega$.

<ol class="al">

<li>

Berechne für den Widerstandswert $X$ die Wahrscheinlichkeiten $P(X<97\,\Omega)$ und $P(96\,\Omega\le X\le104\,\Omega)$.

</li>

<li>

In welchem symmetrischen Intervall um $100\,\Omega$ liegen $95\,\%$ der Widerstände?

</li>

<li>

Die Fertigung wird verbessert, sodass $\sigma=1\,\Omega$ ist. Wie viel Prozent liegen jetzt außerhalb von $96$ bis $104\,\Omega$?

</li>

</ol>

:::loesung
(a) $P(X<97\,\Omega)=\Phi\bigl((97-100)/2\bigr)=\Phi(-1{,}5)=1-\Phi(1{,}5)\approx0{,}067$. $P(96\,\Omega\le X\le104\,\Omega)=P(|Z|\le2)=2\Phi(2)-1\approx0{,}954$.

(b) $100\pm1{,}96\cdot2\,\Omega$, also von etwa $96{,}08$ bis $103{,}92\,\Omega$.

(c) Mit $\sigma=1\,\Omega$ sind die Grenzen $\pm4\sigma$ entfernt, und $P(|Z|>4)=2\,(1-\Phi(4))\approx6{,}3\cdot10^{-5}$, etwa $0{,}006\,\%$. Halbe Streuung bedeutet hier gut siebenhundertmal weniger Ausschuss als die $4{,}6\,\%$ aus (a), weil die Glocke an den Rändern so schnell abfällt.
:::
:::

:::aufgabe Aufgabe 24 ★★ Runden oder Abschneiden
<span class="anker" id="aufg-24"></span>

Ein Umsetzer mit der Stufe $\Delta$ kann runden oder die Nachkommastellen abschneiden. Beim Runden ist der Fehler gleichverteilt auf $[-\Delta/2,\,\Delta/2]$, beim Abschneiden auf $[0,\,\Delta]$ (der angezeigte Wert ist zu klein).

<ol class="al">

<li>

Berechne für beide Fälle Erwartungswert und Varianz des Fehlers.

</li>

<li>

Welches Verfahren ist besser, und warum zeigt die Varianz allein den Unterschied nicht?

</li>

<li>

Ein Umsetzer mit $8$ Bit teilt den Bereich von $0$ bis $5\,\mathrm V$ in $256$ Stufen. Wie groß ist die Standardabweichung des Rundungsfehlers?

</li>

</ol>

:::loesung
(a) Runden: $\mathbb{E}=0$ und $\operatorname{Var}=\Delta^2/12$ nach Unterabschnitt [8.4](#stufe-8-4). Abschneiden: Gleichverteilung auf $[0,\,\Delta]$ mit $\mathbb{E}=\Delta/2$ und ebenfalls $\operatorname{Var}=\Delta^2/12$, denn die Länge des Intervalls ist dieselbe.

(b) Runden ist besser. Beim Abschneiden ist der Fehler im Mittel $\Delta/2$: Alle Werte sind systematisch zu klein. Die Varianz misst nur die Streuung um den Erwartungswert und sieht diesen Versatz nicht. Den ganzen Fehler misst der Erwartungswert seines Quadrats; nach der Verschiebungsformel ist er die Varianz plus das Quadrat des Erwartungswerts, beim Runden $\Delta^2/12$, beim Abschneiden $\Delta^2/12+\Delta^2/4=\Delta^2/3$, viermal so viel.

(c) $\Delta=5\,\mathrm V/256\approx19{,}5\,\mathrm{mV}$ und $\sigma=\Delta/\sqrt{12}\approx5{,}64\,\mathrm{mV}$.
:::
:::

:::aufgabe Aufgabe 25 ★★★ Die Form der Glocke
<span class="anker" id="aufg-25"></span>

<ol class="al">

<li>

Zeige mit der ersten und zweiten Ableitung, dass die Dichte [(8.5)](#gl-8-5) ihr Maximum bei $\mu$ hat und ihre Krümmung genau bei $\mu\pm\sigma$ das Vorzeichen wechselt.

</li>

<li>

Um welchen Faktor ist die Dichte bei $\mu+2\sigma$ und bei $\mu+3\sigma$ kleiner als bei $\mu$?

</li>

<li>

Zeige mit der Substitution $t=(x-\mu)/\sigma$, dass die Gesamtfläche für jedes $\sigma$ gleich $1$ ist, wenn sie es für $\sigma=1$ ist.

</li>

</ol>

:::loesung
(a) Mit $u=(x-\mu)/\sigma$ ist $p=c\,\mathrm{e}^{-u^2/2}$ mit $c=1/(\sigma\sqrt{2\pi})$. Dann ist $p'=-\frac u\sigma\,p$, null genau bei $u=0$, positiv links und negativ rechts davon: Maximum bei $\mu$. Weiter ist $p''=\frac1{\sigma^2}(u^2-1)\,p$, negativ für $|u|<1$ und positiv für $|u|>1$; das Vorzeichen wechselt genau bei $u=\pm1$, also bei $x=\mu\pm\sigma$.

(b) Das Verhältnis zum Höchstwert ist $\mathrm{e}^{-u^2/2}$: bei $u=2$ ist es $\mathrm{e}^{-2}\approx0{,}135$, die Dichte ist etwa $7{,}4$-mal kleiner; bei $u=3$ ist es $\mathrm{e}^{-4{,}5}\approx0{,}011$, etwa $90$-mal kleiner.

(c) Mit $t=(x-\mu)/\sigma$ ist $\mathrm{d} x=\sigma\,\mathrm{d} t$, und $\int\frac1{\sigma\sqrt{2\pi}}\mathrm{e}^{-(x-\mu)^2/(2\sigma^2)}\,\mathrm{d} x=\int\frac1{\sqrt{2\pi}}\mathrm{e}^{-t^2/2}\,\mathrm{d} t$: Das $\sigma$ im Vorfaktor hebt sich gegen das $\sigma$ aus $\mathrm{d} x$ weg.
:::
:::
