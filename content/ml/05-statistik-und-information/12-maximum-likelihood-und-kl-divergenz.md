---
title: Maximum Likelihood und KL-Divergenz
pfad: Informatik / Machine Learning / Statistik und Information
order: 6251200
summary: Die Maximum-Likelihood-Schätzung aus Abschnitt 5 und die KL-Divergenz aus Abschnitt 9 beantworten verschiedene Fragen: die nach dem Parameter, der die Daten am wahrscheinlichsten macht, und die nach dem Mehraufwand durch eine falsche Verteilung.
tags: negative Log-Likelihood
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
Die Maximum-Likelihood-Schätzung aus Abschnitt [5](die-maximum-likelihood-schatzung.html#stufe-5) und die KL-Divergenz aus Abschnitt [9](kreuzentropie-und-kl-divergenz.html#stufe-9) beantworten verschiedene Fragen: die nach dem Parameter, der die Daten am wahrscheinlichsten macht, und die nach dem Mehraufwand durch eine falsche Verteilung. Dieser Abschnitt zeigt, dass beide Fragen dieselbe Antwort haben.
:::

### Rückblick: Die empirische Verteilung

<span class="anker" id="stufe-11-1"></span>

Nach [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 7.7, gibt die empirische Verteilung eines Datensatzes jedem der $N$ Datenpunkte die Wahrscheinlichkeit $1/N$. Fallen die Daten in $K$ Kategorien und kommt die Kategorie $k$ genau $N_k$-mal vor, so hat die empirische Verteilung die Wahrscheinlichkeiten

<span class="anker" id="gl-11-1"></span>
$$\hat p_k=\frac{N_k}N,\qquad\hat{\mathbf{p}}=(\hat p_1,\dots,\hat p_K)^{\top} . \tag{11.1}$$

Sie besteht aus den relativen Häufigkeiten. Das Modell gebe der Kategorie $k$ die Wahrscheinlichkeit $q_k(\boldsymbol{\theta})$; zusammen bilden sie die Verteilung $\mathbf{q}(\boldsymbol{\theta})$.

⁠**Rechenbeispiel:** Für die zehn Würfe der verbogenen Münze mit den Kategorien Kopf und Zahl ist $\hat{\mathbf{p}}=(0{,}7;\ 0{,}3)^{\top}$ und im Bernoulli-Modell $\mathbf{q}(\theta)=(\theta,\ 1-\theta)^{\top}$. Von $20$ Bauteilen, die wie im Beispiel der kategorischen Verteilung in [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 8.2, rot, grün oder blau sind, seien $12$ rot, $5$ grün und $3$ blau. Ihre empirische Verteilung ist $\hat{\mathbf{p}}=(0{,}6;\ 0{,}25;\ 0{,}15)^{\top}$.

⁠**Kurz gesagt:** Die empirische Verteilung eines Datensatzes mit $K$ Kategorien besteht aus den relativen Häufigkeiten $N_k/N$.

### Die Log-Likelihood als Kreuzentropie

<span class="anker" id="stufe-11-2"></span>

Die Log-Likelihood ist eine Summe über die Datenpunkte, ein Summand je Datenpunkt. Datenpunkte derselben Kategorie liefern denselben Summanden. Fasst man sie zusammen, so wird aus der Summe über die Daten eine Summe über die Kategorien, gewichtet mit den Häufigkeiten.

:::satz Satz 11.1 (Log-Likelihood und Kreuzentropie)
<span class="anker" id="satz-11-1"></span>

Für kategorische Daten mit der empirischen Verteilung $\hat{\mathbf{p}}$ und ein Modell $\mathbf{q}(\boldsymbol{\theta})$ ist

<span class="anker" id="gl-11-2"></span>
$$-\frac1N\,\ell(\boldsymbol{\theta})=\sum_{k=1}^K\hat p_k\ln\frac1{q_k(\boldsymbol{\theta})}=H\bigl(\hat{\mathbf{p}},\mathbf{q}(\boldsymbol{\theta})\bigr)\quad\text{nat}. \tag{11.2}$$
:::

:::beweis Log-Likelihood und Kreuzentropie
Fällt der Datenpunkt $i$ in die Kategorie $k_i$, so ist $\ell(\boldsymbol{\theta})=\sum_{i=1}^N\ln q_{k_i}(\boldsymbol{\theta})$. Der Summand $\ln q_k(\boldsymbol{\theta})$ kommt genau $N_k$-mal vor, also ist $\ell(\boldsymbol{\theta})=\sum_kN_k\ln q_k(\boldsymbol{\theta})$. Teilt man durch $-N$, so entsteht mit $N_k/N=\hat p_k$ die Kreuzentropie in nat.
:::

Die Zahl $-\ell(\boldsymbol{\theta})$ heißt __negative Log-Likelihood__. Nach dem Hintergrund-Kasten in Unterabschnitt [5.2](die-maximum-likelihood-schatzung.html#stufe-5-2) ist sie die gesamte Überraschung des Modells über die Daten, also nach Unterabschnitt [8.1](informationsgehalt-und-entropie.html#stufe-8-1) die Summe der Informationsgehalte aller Datenpunkte in nat. Geteilt durch $N$ ist sie die mittlere Überraschung je Datenpunkt.

⁠**Rechenbeispiel:** Für die verbogene Münze ist $\ell(0{,}5)=-6{,}931$ und $\ell(0{,}7)=-6{,}109$. Geteilt durch $-10$ ergibt das $0{,}693$ und $0{,}611$, und das sind die Kreuzentropien (Abb. [22](#abb-22)).

:::abbildung ml/k5rkreuzml 22
Die Kreuzentropie der empirischen Verteilung $\hat{\mathbf{p}}=(0{,}7;\ 0{,}3)^{\top}$ der zehn Würfe zu zwei Modellen. Sie ist die negative Log-Likelihood je Wurf: $6{,}931/10$ und $6{,}109/10$.
:::

⁠**Kurz gesagt:** Die negative Log-Likelihood je Datenpunkt ist die Kreuzentropie der empirischen Verteilung zum Modell, gemessen in nat.

### Maximum Likelihood heißt kleinste KL-Divergenz

<span class="anker" id="stufe-11-3"></span>

Nach [(9.2)](kreuzentropie-und-kl-divergenz.html#gl-9-2) ist die Kreuzentropie die Entropie plus die KL-Divergenz. Die Entropie der empirischen Verteilung hängt aber nur von den Daten ab, nicht vom Parameter.

:::satz Satz 11.2 (Maximum Likelihood und KL-Divergenz)
<span class="anker" id="satz-11-2"></span>

Für kategorische Daten ist

<span class="anker" id="gl-11-3"></span>
$$-\frac1N\,\ell(\boldsymbol{\theta})=H(\hat{\mathbf{p}})+D_{\mathrm{KL}}\bigl(\hat{\mathbf{p}}\,\|\,\mathbf{q}(\boldsymbol{\theta})\bigr) . \tag{11.3}$$

Der Maximum-Likelihood-Schätzer ist deshalb der Parameter, dessen Modellverteilung die kleinste KL-Divergenz von der empirischen Verteilung hat:

<span class="anker" id="gl-11-4"></span>
$$\hat{\boldsymbol{\theta}}_{\mathrm{ML}}=\operatorname*{arg\,min}_{\boldsymbol{\theta}}D_{\mathrm{KL}}\bigl(\hat{\mathbf{p}}\,\|\,\mathbf{q}(\boldsymbol{\theta})\bigr) . \tag{11.4}$$
:::

:::beweis Maximum Likelihood und KL-Divergenz
[(11.3)](#gl-11-3) ist [(11.2)](#gl-11-2) zusammen mit $H(\mathbf{p},\mathbf{q})=H(\mathbf{p})+D_{\mathrm{KL}}(\mathbf{p}\,\|\,\mathbf{q})$ aus [(9.2)](kreuzentropie-und-kl-divergenz.html#gl-9-2). Der erste Summand hängt nicht von $\boldsymbol{\theta}$ ab. Die Log-Likelihood ist also genau dort am größten, wo die KL-Divergenz am kleinsten ist.
:::

⁠**Rechenbeispiel:** Für die verbogene Münze ist $H(\hat{\mathbf{p}})=0{,}611$ nat, die Kreuzentropie zu $\mathbf{q}(0{,}7)$ aus Abb. [22](#abb-22). Zum Modell $\theta=0{,}5$ ist $D_{\mathrm{KL}}=0{,}693-0{,}611=0{,}082$ nat, zum Modell $\theta=0{,}7$ ist sie null. Der Maximum-Likelihood-Schätzer $0{,}7$ ist also der Parameter, dessen Modellverteilung mit der empirischen Verteilung übereinstimmt.

⁠**Kurz gesagt:** Maximum Likelihood wählt das Modell, das von der empirischen Verteilung der Daten die kleinste KL-Divergenz hat.

:::hintergrund Warum beide Fragen dieselbe Antwort haben
Die Zerlegung [(11.3)](#gl-11-3) trennt die mittlere Überraschung des Modells über die Daten in zwei Teile. $H(\hat{\mathbf{p}})$ ist die Überraschung, die bleibt, selbst wenn das Modell die Häufigkeiten in den Daten genau trifft; sie ist eine Eigenschaft der Daten, und keine Wahl des Parameters kann sie verkleinern. $D_{\mathrm{KL}}(\hat{\mathbf{p}}\,\|\,\mathbf{q}(\boldsymbol{\theta}))$ ist die zusätzliche Überraschung, weil das Modell die Häufigkeiten anders erwartet, als sie sind; nur sie hängt vom Parameter ab. Dieselbe Trennung in einen unbeeinflussbaren und einen beeinflussbaren Teil hat [Teil 2](/wissen/informatik/machine-learning/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html), Abschnitt 3.4, bei der besten Näherungslösung gesehen: Dort zerfiel das Fehlerquadrat nach Pythagoras in das senkrechte Residuum und einen Teil im Spaltenraum. Hier tritt an die Stelle von Pythagoras die Zerlegung der Kreuzentropie, und an die Stelle des rechten Winkels die Gibbs-Ungleichung, die den beeinflussbaren Teil nie negativ werden lässt.
:::

### Die kategorische Verteilung

<span class="anker" id="stufe-11-4"></span>

Für die kategorische Verteilung aus [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 8.2, mit freien Wahrscheinlichkeiten $\theta_1,\dots,\theta_K$ ist der Maximum-Likelihood-Schätzer mit Ableitungen mühsam zu finden, weil die Wahrscheinlichkeiten nicht unabhängig voneinander sind: Sie müssen sich zu $1$ summieren. Mit dem Satz des vorigen Unterabschnitts braucht man keine Ableitung.

:::satz Satz 11.3 (Maximum Likelihood für die kategorische Verteilung)
<span class="anker" id="satz-11-3"></span>

Für das Modell $\mathbf{q}(\boldsymbol{\theta})=\boldsymbol{\theta}$ mit $\theta_k\ge0$ und $\sum_k\theta_k=1$ ist

<span class="anker" id="gl-11-5"></span>
$$\hat\theta_{k,\mathrm{ML}}=\frac{N_k}N,\qquad k=1,\dots,K . \tag{11.5}$$
:::

:::beweis Kategorische Verteilung
Nach [(11.4)](#gl-11-4) ist der Schätzer die Verteilung $\boldsymbol{\theta}$ mit der kleinsten KL-Divergenz $D_{\mathrm{KL}}(\hat{\mathbf{p}}\,\|\,\boldsymbol{\theta})$. Nach der Gibbs-Ungleichung ist diese nie negativ und genau für $\boldsymbol{\theta}=\hat{\mathbf{p}}$ null. Weil $\hat{\mathbf{p}}$ selbst eine zulässige Verteilung ist, ist sie der Schätzer.
:::

⁠**Rechenbeispiel:** Für die $20$ Bauteile sind die Maximum-Likelihood-Schätzungen die relativen Häufigkeiten, also $\hat{\boldsymbol{\theta}}=(0{,}6;\ 0{,}25;\ 0{,}15)^{\top}$. Für $K=2$ ergibt sich noch einmal der Anteil der Einsen $N_1/N$ aus Unterabschnitt [5.2](die-maximum-likelihood-schatzung.html#stufe-5-2), diesmal ohne Ableitung.

⁠**Kurz gesagt:** Bei der kategorischen Verteilung sind die Maximum-Likelihood-Schätzer die relativen Häufigkeiten; das folgt direkt aus der Gibbs-Ungleichung.

### Stetige Daten: Normalverteilung und Quadratsumme

<span class="anker" id="stufe-11-5"></span>

Bei stetigen Daten gibt es keine Kategorien, aber die mittlere negative Log-Likelihood lässt sich ebenso hinschreiben. Für das Normalverteilungsmodell ist sie nach [(5.4)](die-maximum-likelihood-schatzung.html#gl-5-4)

<span class="anker" id="gl-11-6"></span>
$$-\frac1N\,\ell(\mu,\sigma^2)=\tfrac12\ln(2\pi\sigma^2)+\frac1{2\sigma^2}\cdot\frac1N\sum_{i=1}^N(x_i-\mu)^2 . \tag{11.6}$$

Für einen festen Wert von $\sigma^2$ ist der erste Summand eine Konstante, und der zweite ist bis auf den positiven Faktor $1/(2\sigma^2)$ die mittlere quadratische Abweichung der Daten von $\mu$. Unter dem Normalverteilungsmodell heißt „die Likelihood maximieren“ also dasselbe wie „die mittlere quadratische Abweichung minimieren“: Beide haben dieselbe Lösung, auch wenn ihre Werte verschieden sind. Auch hier nennt man die mittlere negative Log-Likelihood eine Kreuzentropie zwischen der empirischen Verteilung und dem Modell, im Sinn des Hintergrund-Kastens unten.

⁠**Rechenbeispiel:** Für die vier Spannungen mit $\bar x=5{,}0\,\mathrm V$ und $\hat\sigma^2_{\mathrm{ML}}=0{,}05\,\mathrm V^2$ ist der kleinste Wert von [(11.6)](#gl-11-6) gleich $\tfrac12\ln(2\pi\cdot0{,}05)+\tfrac12=\tfrac12\ln(2\pi\mathrm{e}\cdot0{,}05)\approx-0{,}079$ nat. Er ist negativ, weil die angepasste Normalverteilung schmal ist: Ihre Dichte ist an zwei der vier Messwerte etwa $1{,}61$ und an den beiden anderen etwa $0{,}73$, und die Logarithmen dieser Werte sind im Mittel positiv. Zugleich ist er nach [(10.3)](die-grote-entropie.html#gl-10-3) die differentielle Entropie der angepassten Normalverteilung (Aufgabe [48](#aufg-48)).

⁠**Kurz gesagt:** Bei normalverteilten Daten mit fester Varianz ist Maximum Likelihood dasselbe wie die kleinste mittlere quadratische Abweichung; die mittlere negative Log-Likelihood heißt auch dann Kreuzentropie zum Modell.

:::hintergrund Die empirische Verteilung stetiger Daten
Bei stetigen Daten ist die empirische Verteilung keine Dichte: Sie setzt in jeden Datenpunkt eine unendlich schmale Spitze mit der Wahrscheinlichkeit $1/N$. Mittelt man eine Funktion mit ihr, so erhält man den Mittelwert der Funktionswerte an den Datenpunkten. In diesem Sinn ist $-\frac1N\ell=\frac1N\sum_i\ln\frac1{p(x_i\mid\boldsymbol{\theta})}$ die Kreuzentropie der empirischen Verteilung zur Modelldichte. Ihre eigene Entropie ist dagegen nicht endlich, denn eine Spitze ist unendlich schmal, wie der Hintergrund-Kasten in Unterabschnitt [10.2](die-grote-entropie.html#stufe-10-2) für $\Delta\to0$ gezeigt hat. Die Zerlegung [(11.3)](#gl-11-3) gilt deshalb bei stetigen Daten nur in dem Sinn, dass man eine unendliche, vom Parameter unabhängige Konstante abzieht, die man nie ausrechnet. Die Aussage, dass Maximum Likelihood die Kreuzentropie zum Modell minimiert, bleibt dagegen genau richtig.
:::

:::aufgabe Aufgabe 46 ★ Die Reißzwecke als Kreuzentropie
<span class="anker" id="aufg-46"></span>

Die Reißzwecke landete in acht Würfen fünfmal auf dem Rücken.

<ol class="al">

<li>

Gib die empirische Verteilung an und berechne $H(\hat{\mathbf{p}})$ in nat.

</li>

<li>

Berechne $H(\hat{\mathbf{p}},\mathbf{q}(0{,}5))$ und $D_{\mathrm{KL}}(\hat{\mathbf{p}}\,\|\,\mathbf{q}(0{,}5))$ und prüfe $-\ell(0{,}5)/8=H(\hat{\mathbf{p}},\mathbf{q}(0{,}5))$.

</li>

</ol>

:::loesung
(a) $\hat{\mathbf{p}}=(0{,}625;\ 0{,}375)^{\top}$ und $H(\hat{\mathbf{p}})=0{,}625\ln\frac1{0{,}625}+0{,}375\ln\frac1{0{,}375}\approx0{,}294+0{,}368=0{,}662$ nat.

(b) $H(\hat{\mathbf{p}},\mathbf{q}(0{,}5))=\ln2\approx0{,}693$ nat und $D_{\mathrm{KL}}\approx0{,}693-0{,}662=0{,}032$ nat. Zur Probe ist $\ell(0{,}5)=8\ln0{,}5$, also $-\ell(0{,}5)/8=\ln2$.
:::
:::

:::aufgabe Aufgabe 47 ★★ Ist der Würfel fair?
<span class="anker" id="aufg-47"></span>

Ein Würfel zeigt in $30$ Würfen die Augenzahlen $1$ bis $6$ genau $3$-, $4$-, $5$-, $6$-, $5$- und $7$-mal.

<ol class="al">

<li>

Gib die Maximum-Likelihood-Schätzung der sechs Wahrscheinlichkeiten an.

</li>

<li>

Berechne $D_{\mathrm{KL}}(\hat{\mathbf{p}}\,\|\,\mathbf{u})$ in nat zur Gleichverteilung $\mathbf{u}$.

</li>

<li>

Zeige mit [(11.3)](#gl-11-3): $\ell(\hat{\boldsymbol{\theta}})-\ell(\mathbf{u})=N\cdot D_{\mathrm{KL}}(\hat{\mathbf{p}}\,\|\,\mathbf{u})$. Um welchen Faktor ist die Likelihood des geschätzten Modells größer als die des fairen Würfels?

</li>

</ol>

:::loesung
(a) $\hat{\boldsymbol{\theta}}=(0{,}1;\ 0{,}133;\ 0{,}167;\ 0{,}2;\ 0{,}167;\ 0{,}233)^{\top}$, die relativen Häufigkeiten $3/30,\dots,7/30$.

(b) $D_{\mathrm{KL}}(\hat{\mathbf{p}}\,\|\,\mathbf{u})=\sum_k\hat p_k\ln(6\hat p_k)\approx0{,}0341$ nat.

(c) Nach [(11.3)](#gl-11-3) ist $-\ell(\boldsymbol{\theta})=N\,H(\hat{\mathbf{p}})+N\,D_{\mathrm{KL}}(\hat{\mathbf{p}}\,\|\,\mathbf{q}(\boldsymbol{\theta}))$. Für $\hat{\boldsymbol{\theta}}=\hat{\mathbf{p}}$ ist die Divergenz null, also ist $\ell(\hat{\boldsymbol{\theta}})-\ell(\mathbf{u})=N\,D_{\mathrm{KL}}(\hat{\mathbf{p}}\,\|\,\mathbf{u})\approx30\cdot0{,}0341\approx1{,}02$. Die Likelihood des geschätzten Modells ist um den Faktor $\mathrm{e}^{1{,}02}\approx2{,}8$ größer. Das ist wenig, denn das geschätzte Modell passt sich mit fünf freien Wahrscheinlichkeiten den Zufällen der Daten an. Dreißig Würfe sprechen nicht deutlich gegen einen fairen Würfel.
:::
:::

:::aufgabe Aufgabe 48 ★★★ Die kleinste negative Log-Likelihood
<span class="anker" id="aufg-48"></span>

Setze in [(11.6)](#gl-11-6) $\mu=\bar x$.

<ol class="al">

<li>

Zeige, dass der Ausdruck als Funktion von $\sigma^2$ bei $\hat\sigma^2_N$ am kleinsten ist, und dass sein kleinster Wert $\tfrac12\ln(2\pi\mathrm{e}\,\hat\sigma^2_N)$ ist.

</li>

<li>

Deute das Ergebnis mit [(10.3)](die-grote-entropie.html#gl-10-3). Was sagt es über Daten mit kleiner Streuung?

</li>

</ol>

:::loesung
(a) Mit $\mu=\bar x$ ist der Ausdruck $g(v)=\tfrac12\ln(2\pi v)+\frac{\hat\sigma^2_N}{2v}$ mit $v=\sigma^2$, denn $\frac1N\sum_i(x_i-\bar x)^2=\hat\sigma^2_N$. Die Ableitung $g'(v)=\frac1{2v}-\frac{\hat\sigma^2_N}{2v^2}=\frac{v-\hat\sigma^2_N}{2v^2}$ ist negativ für $v<\hat\sigma^2_N$ und positiv danach, das Minimum liegt also bei $\hat\sigma^2_N$, und dort ist $g=\tfrac12\ln(2\pi\hat\sigma^2_N)+\tfrac12=\tfrac12\ln(2\pi\mathrm{e}\,\hat\sigma^2_N)$.

(b) Nach [(10.3)](die-grote-entropie.html#gl-10-3) ist das die differentielle Entropie der angepassten Normalverteilung $\mathcal N(\bar x,\hat\sigma^2_N)$. Die kleinste mittlere Überraschung, die das Normalverteilungsmodell über die Daten haben kann, ist also so groß wie die Ausbreitung der Daten, gemessen mit der Entropie. Daten mit kleiner Streuung lassen sich mit einer schmalen Dichte beschreiben, deren Werte groß sind; ihre mittlere negative Log-Likelihood ist klein und kann negativ werden, wie bei den vier Spannungen mit $-0{,}079$ nat.
:::
:::
