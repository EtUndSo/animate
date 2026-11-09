---
title: Die Maximum-Likelihood-Schätzung
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Statistik und Information
knoten: Grundlagen 5: Statistik und Information
nachschlagen: ja
order: 15250600
summary: Der Parameterwert, unter dem die beobachteten Daten am wahrscheinlichsten sind, ist ein naheliegender Schätzer.
tags: Maximum-Likelihood-Schätzer
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Der Parameterwert, unter dem die beobachteten Daten am wahrscheinlichsten sind, ist ein naheliegender Schätzer. Dieser Abschnitt bestimmt ihn mit der Ableitung, für die Bernoulli- und für die Normalverteilung, und zeigt, dass er sich mit Umrechnungen des Parameters verträgt.
:::

### Was du dafür brauchst: Der höchste Punkt einer Kurve

<span class="anker" id="stufe-5-1"></span>

Gesucht ist die Stelle, an der eine Funktion am größten ist. Man schreibt sie $\operatorname*{arg\,max}_xf(x)$, gelesen „die Stelle $x$, an der $f(x)$ am größten ist“; der Name kommt vom englischen *argument of the maximum*. Für differenzierbare Funktionen findet man sie mit der Ableitung.

:::satz Satz 5.1 (Waagrechte Tangente am höchsten Punkt)
<span class="anker" id="satz-5-1"></span>

Die Funktion $f$ sei auf einem offenen Intervall $I$ differenzierbar, und an der Stelle $x^*\in I$ sei $f(x^*)\ge f(x)$ für alle $x\in I$. Dann ist $f'(x^*)=0$.
:::

:::beweis Waagrechte Tangente
Weil $I$ offen ist, liegen Stellen $x^*+t$ mit kleinem $t$ auf beiden Seiten noch in $I$. Für $t>0$ ist $f(x^*+t)-f(x^*)\le0$, also ist der Differenzenquotient $\bigl(f(x^*+t)-f(x^*)\bigr)/t$ nicht positiv, und sein Grenzwert $f'(x^*)$ aus [Grundlagen 3, Abschnitt 1.2](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/die-ableitung.html#stufe-1-2), auch nicht. Für $t<0$ ist der Zähler ebenfalls nicht positiv, der Nenner aber negativ, der Quotient also nicht negativ, und damit $f'(x^*)\ge0$. Beides zusammen ergibt $f'(x^*)=0$.
:::

Anschaulich: Wäre die Steigung am höchsten Punkt nicht null, so ginge es nach der linearen Näherung aus [Grundlagen 3, Abschnitt 1.3](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/die-ableitung.html#stufe-1-3), in eine Richtung noch weiter bergauf. Die Umkehrung gilt nicht. Eine Nullstelle der Ableitung kann ein höchster Punkt sein, ein tiefster oder keins von beiden, wie bei $x^3$ an der Stelle $0$. Ob es ein höchster Punkt ist, entscheidet das Vorzeichen der Ableitung in der Umgebung.

:::satz Satz 5.2 (Vorzeichenwechsel der Ableitung)
<span class="anker" id="satz-5-2"></span>

Die Funktion $f$ sei auf einem Intervall $I$ differenzierbar, und $x^*$ liege in $I$. Ist $f'(x)>0$ für alle $x<x^*$ in $I$ und $f'(x)<0$ für alle $x>x^*$ in $I$, so ist $x^*$ die einzige Stelle von $I$, an der $f$ am größten ist.
:::

Dahinter steht die Tatsache aus der Schule, dass eine Funktion mit positiver Ableitung wächst und eine mit negativer Ableitung fällt. Links von $x^*$ steigt $f$ also bis $x^*$ an, rechts davon fällt $f$ wieder ab.

::::beispiel [Rechenbeispiel]
Für $f(x)=\ln x-x$ auf $x>0$ ist $f'(x)=1/x-1$. Die Ableitung ist null bei $x=1$, positiv für $x<1$ und negativ für $x>1$. Also ist $x=1$ der höchste Punkt, mit $f(1)=-1$. Für jedes $x>0$ ist deshalb $\ln x-x\le-1$, also

<span class="anker" id="gl-5-1"></span>
$$\ln x\le x-1 , \tag{5.1}$$

mit Gleichheit nur bei $x=1$. Diese Ungleichung wird in Abschnitt [9](kreuzentropie-und-kl-divergenz.html#stufe-9) wichtig.
::::

⁠**Kurz gesagt:** Am höchsten Punkt im Inneren eines Intervalls ist die Ableitung null; wechselt sie dort von positiv zu negativ, ist es tatsächlich der höchste Punkt.

### Der Maximum-Likelihood-Schätzer

<span class="anker" id="stufe-5-2"></span>

Die Likelihood bewertet jeden Parameterwert. Der beste nach dieser Bewertung ist der, unter dem die Daten am wahrscheinlichsten sind.

:::definition Definition 5.3 (Maximum-Likelihood-Schätzer)
<span class="anker" id="satz-5-3"></span>

Der __Maximum-Likelihood-Schätzer__ ist

<span class="anker" id="gl-5-2"></span>
$$\hat\theta_{\mathrm{ML}}=\operatorname*{arg\,max}_{\theta\in\Theta}\mathcal L(\theta)=\operatorname*{arg\,max}_{\theta\in\Theta}\ell(\theta) . \tag{5.2}$$
:::

Die beiden Ausdrücke sind gleich, weil $\ln$ streng monoton wächst. Üblich ist die englische Abkürzung ML, für den Schätzer auch MLE, von *maximum likelihood estimator*. Meist rechnet man mit $\ell$, weil sich die Summe leichter ableiten lässt.

:::satz Satz 5.4 (Maximum Likelihood für die Bernoulli-Verteilung)
<span class="anker" id="satz-5-4"></span>

Im Bernoulli-Modell ist der Maximum-Likelihood-Schätzer der Anteil der Einsen:

<span class="anker" id="gl-5-3"></span>
$$\hat\theta_{\mathrm{ML}}=\frac{N_1}N . \tag{5.3}$$
:::

:::herleitung Maximum Likelihood für die Bernoulli-Verteilung
Es sei zuerst $0<N_1<N$. Für $\theta=0$ oder $\theta=1$ ist $\mathcal L(\theta)=0$, dort liegt also kein Maximum. Auf dem offenen Intervall $0<\theta<1$ ist $\ell(\theta)=N_1\ln\theta+N_0\ln(1-\theta)$ mit der Ableitung

$$\ell'(\theta)=\frac{N_1}\theta-\frac{N_0}{1-\theta} .$$

Sie ist null, wenn $N_1(1-\theta)=N_0\,\theta$ ist, also $N_1=(N_0+N_1)\,\theta=N\theta$. Beide Summanden von $\ell'$ fallen mit wachsendem $\theta$, also fällt auch $\ell'$: Die Ableitung ist links von $N_1/N$ positiv und rechts davon negativ. Nach dem Satz über den Vorzeichenwechsel ist $N_1/N$ der höchste Punkt. Ist $N_1=N$, so ist $\mathcal L(\theta)=\theta^N$ am größten bei $\theta=1=N_1/N$; ist $N_1=0$, so ist $\mathcal L(\theta)=(1-\theta)^N$ am größten bei $\theta=0=N_1/N$.
:::

::::beispiel [Rechenbeispiel]
Für die zehn Würfe ist $\hat\theta_{\mathrm{ML}}=7/10=0{,}7$, die Stelle des Maximums in Abb. [7](die-likelihood.html#abb-7). Zur Probe ist $\ell'(0{,}7)=7/0{,}7-3/0{,}3=10-10=0$. Der Anteil der Köpfe, in Abschnitt [1](schatzen-aus-einer-stichprobe.html#stufe-1) nur ein naheliegendes Rezept, ist damit begründet: Er ist der Parameterwert, unter dem die beobachteten Würfe am wahrscheinlichsten sind.
::::

:::warnung Wenige Daten
Zeigt eine Münze in drei Würfen dreimal Kopf, so ist $\hat\theta_{\mathrm{ML}}=1$. Das Modell mit diesem Parameter hält Zahl für unmöglich. Ein einziger späterer Wurf mit Zahl hätte unter ihm die Wahrscheinlichkeit null. Maximum Likelihood nimmt kleine Datensätze wörtlich. Abschnitt [6](prior-und-posterior.html#stufe-6) zeigt, wie Vorwissen über Münzen solche Schlüsse abmildert.
:::

⁠**Kurz gesagt:** Der Maximum-Likelihood-Schätzer ist der Parameterwert, unter dem die Daten am wahrscheinlichsten sind; im Bernoulli-Modell ist er der Anteil der Einsen $N_1/N$.

:::hintergrund Das Modell, das von den Daten am wenigsten überrascht wird
Die Zahl $-\ln P(X=x_i\mid\theta)$ misst, wie überrascht ein Modell mit dem Parameter $\theta$ vom Datenpunkt $x_i$ ist. Für einen Ausgang, den das Modell für sicher hält, ist sie null; je seltener es den Ausgang erwartet, desto größer wird sie. Nach [(4.6)](die-likelihood.html#gl-4-6) ist $-\ell(\theta)$ die Summe dieser Überraschungen über alle Datenpunkte. Maximum Likelihood wählt also das Modell, das von den Daten insgesamt am wenigsten überrascht wird. Bei der verbogenen Münze ist das Modell $\theta=0{,}5$ von jedem Wurf um $\ln2\approx0{,}693$ überrascht, zusammen $6{,}93$. Das Modell $\theta=0{,}7$ ist von einem Kopf nur um $0{,}357$ überrascht und von einer Zahl um $1{,}204$, zusammen $6{,}11$. Das Modell $\theta=0{,}9$ erwartet Kopf noch sicherer, $0{,}105$ je Kopf, wird aber von den drei Zahlen mit je $2{,}303$ so stark überrascht, dass es auf $7{,}65$ kommt. Abschnitt [8](informationsgehalt-und-entropie.html#stufe-8) macht aus dieser Überraschung ein eigenes Maß.
:::

### Die Normalverteilung: der Mittelwert

<span class="anker" id="stufe-5-3"></span>

Vier Messungen derselben Spannung ergeben $4{,}9$, $5{,}3$, $5{,}1$ und $4{,}7\,\mathrm V$. Das Modell sei die Normalverteilung $\mathcal N(\mu,\sigma^2)$ aus [Grundlagen 4, Abschnitt 8.5](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wichtige-verteilungen.html#stufe-8-5): $\mu$ ist der wahre Wert, $\sigma^2$ die Varianz des Rauschens. Gesucht ist der Maximum-Likelihood-Schätzer für $\mu$.

Logarithmiert man die Dichte $p(x\mid\mu,\sigma^2)=\frac1{\sqrt{2\pi\sigma^2}}\exp\bigl(-\frac{(x-\mu)^2}{2\sigma^2}\bigr)$ mit den Rechenregeln [(4.1)](die-likelihood.html#gl-4-1), so bleibt $\ln p(x\mid\mu,\sigma^2)=-\tfrac12\ln(2\pi\sigma^2)-\frac{(x-\mu)^2}{2\sigma^2}$. Summiert über alle Werte ist die Log-Likelihood

<span class="anker" id="gl-5-4"></span>
$$\ell(\mu,\sigma^2)=-\frac N2\ln(2\pi\sigma^2)-\frac1{2\sigma^2}\sum_{i=1}^N(x_i-\mu)^2 . \tag{5.4}$$

Mit der Zerlegung $\sum_i(x_i-\mu)^2=\sum_i(x_i-\bar x)^2+N(\bar x-\mu)^2$ aus dem Hintergrund in Unterabschnitt [3.1](die-varianz-schatzen.html#stufe-3-1) hängt die Log-Likelihood von den Daten nur über den Mittelwert $\bar x$ und die Quadratsumme $\sum_i(x_i-\bar x)^2$ ab.

:::satz Satz 5.5 (Maximum Likelihood für den Erwartungswert der Normalverteilung)
<span class="anker" id="satz-5-5"></span>

Für jeden festen Wert von $\sigma^2$ ist $\ell(\mu,\sigma^2)$ am größten bei

<span class="anker" id="gl-5-5"></span>
$$\hat\mu_{\mathrm{ML}}=\bar x=\frac1N\sum_{i=1}^Nx_i . \tag{5.5}$$
:::

:::herleitung Maximum Likelihood für $\mu$
In [(5.4)](#gl-5-4) hängt nur der zweite Summand von $\mu$ ab, und er ist die Quadratsumme $Q(\mu)=\sum_i(x_i-\mu)^2$ mal der negativen Zahl $-1/(2\sigma^2)$. Die Log-Likelihood ist also genau dort am größten, wo $Q(\mu)$ am kleinsten ist. Es ist $Q'(\mu)=-2\sum_i(x_i-\mu)=-2\,(N\bar x-N\mu)$. Diese Ableitung ist negativ für $\mu<\bar x$, null bei $\mu=\bar x$ und positiv für $\mu>\bar x$. Also hat $Q$ bei $\bar x$ den tiefsten Punkt, und $\ell$ dort den höchsten.
:::

Bemerkenswert ist, dass die Antwort nicht von $\sigma^2$ abhängt: Wie stark das Rauschen auch ist, der plausibelste wahre Wert ist der Mittelwert.

::::beispiel [Rechenbeispiel]
Für die vier Spannungen ist $\hat\mu_{\mathrm{ML}}=\tfrac14(4{,}9+5{,}3+5{,}1+4{,}7)=5{,}0\,\mathrm V$. [Grundlagen 2, Abschnitt 11.4](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-pseudoinverse.html#stufe-11-4), hat den Mittelwert mehrerer Messungen schon als beste Näherungslösung des Gleichungssystems „$x=x_i$ für alle $i$“ gefunden. Jetzt hat derselbe Wert eine zweite Bedeutung: Er ist der wahre Wert, der die Messungen am wahrscheinlichsten macht, wenn das Rauschen normalverteilt ist.
::::

⁠**Kurz gesagt:** Bei normalverteilten Daten ist der Maximum-Likelihood-Schätzer für den Erwartungswert der Mittelwert, weil die Log-Likelihood bis auf Konstanten die negative Quadratsumme der Abweichungen ist.

:::hintergrund Warum gerade der Mittelwert
Der Mittelwert kommt heraus, weil die Normalverteilung die quadrierte Abweichung im Exponenten trägt. Der Logarithmus holt sie heraus, und aus „Likelihood maximieren“ wird „Quadratsumme minimieren“. Mit einer anderen Form des Rauschens ergibt sich ein anderer Schätzer. Hat das Rauschen etwa die Dichte $\frac1{2s}\exp(-|x-\mu|/s)$ mit einer Breite $s>0$, die sogenannte Laplace-Verteilung, so ist die Log-Likelihood bis auf eine Konstante $-\frac1s\sum_i|x_i-\mu|$. Diese Summe der Beträge ist am Median der Daten am kleinsten, den [Grundlagen 4, Abschnitt 7.7](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-7), vorgestellt hat (Aufgabe [20](#aufg-20)). Die Laplace-Verteilung hat dickere Ausläufer als die Normalverteilung, große Abweichungen sind unter ihr also weniger überraschend. Ein Ausreißer zieht den Median deshalb kaum. Kommt zu den vier Spannungen eine Fehlmessung von $9{,}0\,\mathrm V$ hinzu, so springt der Mittelwert auf $5{,}8\,\mathrm V$, der Median nur auf $5{,}1\,\mathrm V$. Welches Mittel das beste ist, entscheidet also die angenommene Form des Rauschens.
:::

### Die Normalverteilung: die Varianz

<span class="anker" id="stufe-5-4"></span>

Jetzt fehlt noch $\sigma^2$. Weil $\bar x$ für jeden Wert von $\sigma^2$ der beste Wert von $\mu$ ist, gilt $\ell(\mu,\sigma^2)\le\ell(\bar x,\sigma^2)$ für alle $\mu$ und $\sigma^2$. Das Maximum über beide Parameter findet man also, indem man $\mu=\bar x$ einsetzt und dann nur noch über $\sigma^2$ maximiert.

:::satz Satz 5.6 (Maximum Likelihood für die Varianz der Normalverteilung)
<span class="anker" id="satz-5-6"></span>

Ist die Quadratsumme $Q=\sum_i(x_i-\bar x)^2$ positiv, so ist der Maximum-Likelihood-Schätzer für $\sigma^2$

<span class="anker" id="gl-5-6"></span>
$$\hat\sigma^2_{\mathrm{ML}}=\frac1N\sum_{i=1}^N(x_i-\bar x)^2=\hat\sigma^2_N . \tag{5.6}$$
:::

:::herleitung Maximum Likelihood für $\sigma^2$
Mit $v=\sigma^2>0$ ist nach [(5.4)](#gl-5-4) $f(v)=\ell(\bar x,v)=-\frac N2\ln(2\pi v)-\frac Q{2v}$. Mit $\ln(2\pi v)=\ln(2\pi)+\ln v$ ist die Ableitung

$$f'(v)=-\frac N{2v}+\frac Q{2v^2}=\frac{Q-Nv}{2v^2} .$$

Sie ist positiv für $v<Q/N$, null bei $v=Q/N$ und negativ für $v>Q/N$. Nach dem Satz über den Vorzeichenwechsel ist $v=Q/N$ der höchste Punkt.
:::

Der Maximum-Likelihood-Schätzer für die Varianz ist also genau der Schätzer mit dem Nenner $N$ aus Abschnitt [3](die-varianz-schatzen.html#stufe-3), der die Varianz im Mittel um den Faktor $(N-1)/N$ unterschätzt. Maximum Likelihood garantiert keine Erwartungstreue.

::::beispiel [Rechenbeispiel]
Für die vier Spannungen ist $Q=0{,}01+0{,}09+0{,}01+0{,}09=0{,}2\,\mathrm V^2$ und $\hat\sigma^2_{\mathrm{ML}}=0{,}2/4=0{,}05\,\mathrm V^2$. Die Standardabweichung mit dem Nenner $N$, die [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) für Datensätze benutzt hat, ist also unter dem Normalverteilungsmodell die Maximum-Likelihood-Schätzung von $\sigma$; das zeigt der nächste Unterabschnitt. Hier ist sie $\sqrt{0{,}05}\approx0{,}224\,\mathrm V$.
::::

⁠**Kurz gesagt:** Bei normalverteilten Daten schätzt Maximum Likelihood die Varianz mit dem Nenner $N$, also verzerrt.

### Umrechnen eines Maximum-Likelihood-Schätzers

<span class="anker" id="stufe-5-5"></span>

Oft interessiert nicht der Parameter selbst, sondern eine Größe, die aus ihm folgt: die Standardabweichung statt der Varianz, oder bei einer Münze die Chance, das Verhältnis $\theta/(1-\theta)$ von Kopf zu Zahl. Muss man für sie neu maximieren? Nein, wenn die Umrechnung umkehrbar ist.

:::satz Satz 5.7 (Maximum Likelihood verträgt Umrechnungen)
<span class="anker" id="satz-5-7"></span>

Es sei $g$ eine umkehrbare Funktion und $\eta=g(\theta)$ ein neuer Parameter. Dann ist der Maximum-Likelihood-Schätzer für $\eta$

<span class="anker" id="gl-5-7"></span>
$$\hat\eta_{\mathrm{ML}}=g(\hat\theta_{\mathrm{ML}}) . \tag{5.7}$$
:::

:::beweis Umrechnung
Schreibt man das Modell mit $\eta$ statt mit $\theta$, so hat der Datensatz unter $\eta$ dieselbe Wahrscheinlichkeit wie unter $\theta=g^{-1}(\eta)$. Die Likelihood als Funktion von $\eta$ ist also $\mathcal L(g^{-1}(\eta))$. Sie nimmt dieselben Werte an wie $\mathcal L$, nur unter anderen Namen. Ihr größter Wert ist derselbe, und er gehört zum Namen $\eta=g(\hat\theta_{\mathrm{ML}})$.
:::

::::beispiel [Rechenbeispiel]
Weil $\sigma=\sqrt{\sigma^2}$ für positive Zahlen umkehrbar ist, ist die Maximum-Likelihood-Schätzung der Standardabweichung der vier Spannungen $\hat\sigma_{\mathrm{ML}}=\sqrt{0{,}05}\approx0{,}224\,\mathrm V$. Für die Münze ist die Chance $\theta/(1-\theta)$ umkehrbar, ihr Maximum-Likelihood-Schätzer also $0{,}7/0{,}3=7/3\approx2{,}33$: Kopf ist etwa $2{,}3$-mal so wahrscheinlich wie Zahl. Erwartungstreue übersteht solche Umrechnungen dagegen nicht. Nach Unterabschnitt [3.3](die-varianz-schatzen.html#stufe-3-3) ist $\hat\sigma^2_{N-1}$ erwartungstreu, seine Wurzel aber nicht.
::::

⁠**Kurz gesagt:** Rechnet man den Parameter umkehrbar um, so rechnet man den Maximum-Likelihood-Schätzer einfach mit um.

:::hintergrund Warum die Likelihood das Umbenennen übersteht
Die Likelihood ist eine Funktion des Parameters, keine Dichte über ihm. Benennt man die Parameterwerte um, so wandert jeder Funktionswert unverändert zu seinem neuen Namen, und der höchste bleibt der höchste. Bei einer Dichte wäre das anders. Rechnet man eine Zufallsgröße nichtlinear um, so wird ihre Dichte nach dem Variablenwechsel aus [Grundlagen 4, Abschnitt 8.6](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wichtige-verteilungen.html#stufe-8-6), mit dem Betrag der Ableitung der Umrechnung multipliziert, und dieser Faktor kann die Lage des Gipfels verschieben; [Grundlagen 4, Abschnitt 7.7](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-7), hat das beim Modus bemerkt. Diese Unterscheidung wird in Abschnitt [7](die-maximum-a-posteriori-schatzung.html#stufe-7) wichtig, wo eine Dichte über den Parameter ins Spiel kommt.
:::

:::aufgabe Aufgabe 16 ★ Höchste Punkte
<span class="anker" id="aufg-16"></span>

Bestimme mit der Ableitung und dem Vorzeichenwechsel die Stelle des Maximums und den größten Wert von

<ol class="al">

<li>

$f(x)=x\,\mathrm{e}^{-x}$ für $x>0$;

</li>

<li>

$g(\theta)=\theta^2(1-\theta)$ für $0<\theta<1$.

</li>

</ol>

:::loesung
(a) $f'(x)=\mathrm{e}^{-x}-x\,\mathrm{e}^{-x}=(1-x)\,\mathrm{e}^{-x}$. Weil $\mathrm{e}^{-x}>0$ ist, ist $f'$ positiv für $x<1$ und negativ für $x>1$. Das Maximum liegt bei $x=1$, mit $f(1)=\mathrm{e}^{-1}\approx0{,}368$.

(b) $g'(\theta)=2\theta(1-\theta)-\theta^2=\theta(2-3\theta)$, auf $0<\theta<1$ positiv für $\theta<\tfrac23$ und negativ für $\theta>\tfrac23$. Das Maximum liegt bei $\theta=\tfrac23$, mit $g(\tfrac23)=\tfrac49\cdot\tfrac13=\tfrac4{27}\approx0{,}148$. Das ist die Likelihood von zwei Einsen und einer Null, und ihr Maximum ist der Anteil $2/3$.
:::
:::

:::aufgabe Aufgabe 17 ★ Maximum Likelihood für die Reißzwecke
<span class="anker" id="aufg-17"></span>

Die Reißzwecke landete in acht Würfen fünfmal auf dem Rücken.

<ol class="al">

<li>

Bestimme $\hat\theta_{\mathrm{ML}}$ und prüfe $\ell'(\hat\theta_{\mathrm{ML}})=0$.

</li>

<li>

Gib die Maximum-Likelihood-Schätzung der Chance $\theta/(1-\theta)$ an.

</li>

<li>

Gib den geschätzten Standardfehler von $\hat\theta_{\mathrm{ML}}$ an.

</li>

</ol>

:::loesung
(a) $\hat\theta_{\mathrm{ML}}=5/8=0{,}625$. Probe: $\ell'(\theta)=5/\theta-3/(1-\theta)$, und $5/0{,}625-3/0{,}375=8-8=0$.

(b) Nach dem Satz in Unterabschnitt [5.5](#stufe-5-5): $0{,}625/0{,}375=5/3\approx1{,}67$.

(c) $\sqrt{0{,}625\cdot0{,}375/8}\approx0{,}171$.
:::
:::

:::aufgabe Aufgabe 18 ★★ Zählereignisse
<span class="anker" id="aufg-18"></span>

Ein Zählrohr registriert in fünf gleich langen Zeitabschnitten $2$, $0$, $3$, $1$ und $4$ Zerfälle. Die Anzahl $X$ in einem Abschnitt beschreibt man mit der Poisson-Verteilung $P(X=k\mid\theta)=\theta^k\mathrm{e}^{-\theta}/k!$ für $k=0,1,2,\dots$ mit einem Parameter $\theta>0$; in vielen Büchern heißt er $\lambda$.

<ol class="al">

<li>

Schreibe die Log-Likelihood für beliebige Zählwerte $k_1,\dots,k_N$ auf.

</li>

<li>

Zeige, dass der Maximum-Likelihood-Schätzer der Mittelwert der Zählwerte ist, und berechne ihn für die Daten.

</li>

</ol>

:::loesung
(a) Mit $\ln\bigl(\theta^k\mathrm{e}^{-\theta}/k!\bigr)=k\ln\theta-\theta-\ln k!$ ist $\ell(\theta)=\bigl(\sum_ik_i\bigr)\ln\theta-N\theta-\sum_i\ln k_i!$.

(b) $\ell'(\theta)=\frac1\theta\sum_ik_i-N$. Sie ist positiv für $\theta<\bar k$ und negativ für $\theta>\bar k$, mit $\bar k=\frac1N\sum_ik_i$. Also ist $\hat\theta_{\mathrm{ML}}=\bar k$, für die Daten $(2+0+3+1+4)/5=2$. Das ist vernünftig, weil der Parameter der Poisson-Verteilung ihr Erwartungswert ist.
:::
:::

:::aufgabe Aufgabe 19 ★★ Bekannter Erwartungswert
<span class="anker" id="aufg-19"></span>

Bei der Normalverteilung sei $\mu$ bekannt, gesucht ist nur $\sigma^2$.

<ol class="al">

<li>

Bestimme den Maximum-Likelihood-Schätzer für $\sigma^2$.

</li>

<li>

Ist er erwartungstreu? Vergleiche mit Aufgabe [9](die-varianz-schatzen.html#aufg-9).

</li>

</ol>

:::loesung
(a) Mit bekanntem $\mu$ ist $\ell(v)=-\frac N2\ln(2\pi v)-\frac Q{2v}$ mit $v=\sigma^2$ und $Q=\sum_i(x_i-\mu)^2$. Wie in der Herleitung in Unterabschnitt [5.4](#stufe-5-4) liegt das Maximum bei $v=Q/N$, also $\hat\sigma^2_{\mathrm{ML}}=\frac1N\sum_i(x_i-\mu)^2$.

(b) Ja: Das ist der Schätzer $\tilde\sigma^2$ aus Aufgabe [9](die-varianz-schatzen.html#aufg-9), und er ist erwartungstreu. Die Verzerrung im Fall mit unbekanntem $\mu$ kommt nur vom Einsetzen von $\bar x$.
:::
:::

:::aufgabe Aufgabe 20 ★★ Median statt Mittelwert
<span class="anker" id="aufg-20"></span>

Für Zahlen $x_1<x_2<x_3$ sei $S(m)=|x_1-m|+|x_2-m|+|x_3-m|$.

<ol class="al">

<li>

Zeige: Für $m$ zwischen $x_1$ und $x_2$ hat $S$ die Steigung $-1$, für $m$ zwischen $x_2$ und $x_3$ die Steigung $+1$. Wo ist $S$ am kleinsten?

</li>

<li>

Berechne $S$ für die Werte $4{,}7$; $5{,}1$; $9{,}0$ an den Stellen $5{,}1$ und $6{,}267$, dem Mittelwert.

</li>

</ol>

:::loesung
(a) Für $x_1<m<x_2$ ist $S(m)=(m-x_1)+(x_2-m)+(x_3-m)$; nach $m$ abgeleitet ergibt das $1-1-1=-1$. Für $x_2<m<x_3$ ist $S(m)=(m-x_1)+(m-x_2)+(x_3-m)$ mit der Steigung $1+1-1=+1$. $S$ fällt also bis $x_2$ und steigt danach; außerhalb von $[x_1,x_3]$ hat $S$ die Steigung $-3$ beziehungsweise $+3$. Das Minimum liegt beim mittleren Wert $x_2$, dem Median.

(b) $S(5{,}1)=0{,}4+0+3{,}9=4{,}3$ und $S(6{,}267)\approx1{,}567+1{,}167+2{,}733\approx5{,}467$. Der Median hat die kleinere Summe der Beträge, der Mittelwert $6{,}267$ wird vom Ausreißer $9{,}0$ weggezogen.
:::
:::

:::aufgabe Aufgabe 21 ★★★ Wenn die Ableitung nicht hilft
<span class="anker" id="aufg-21"></span>

Messwerte seien gleichverteilt auf $[0,\,\theta]$ mit unbekanntem $\theta>0$. Beobachtet wurden $0{,}8$; $2{,}1$ und $1{,}5$.

<ol class="al">

<li>

Zeige: $\mathcal L(\theta)=\theta^{-3}$ für $\theta\ge2{,}1$ und $\mathcal L(\theta)=0$ für $\theta<2{,}1$. Skizziere $\mathcal L$.

</li>

<li>

Bestimme $\hat\theta_{\mathrm{ML}}$. Warum findet man ihn nicht über $\mathcal L'(\theta)=0$?

</li>

<li>

Für $N$ Werte ist $\hat\theta_{\mathrm{ML}}$ der größte Wert $M$. Zeige $P(M\le m)=(m/\theta)^N$ für $0\le m\le\theta$ und daraus $\mathbb{E}[M]=\frac N{N+1}\,\theta$. Ist der Schätzer erwartungstreu?

</li>

</ol>

:::loesung
(a) Die Dichte ist $1/\theta$ auf $[0,\,\theta]$ und sonst null. Ist $\theta\ge2{,}1$, so liegen alle drei Werte im Intervall, und $\mathcal L(\theta)=\theta^{-3}$. Ist $\theta<2{,}1$, so hat der Wert $2{,}1$ die Dichte null, und $\mathcal L(\theta)=0$. Die Skizze ist null bis $2{,}1$, springt dort auf $2{,}1^{-3}\approx0{,}108$ und fällt danach wie $\theta^{-3}$ ab.

(b) $\hat\theta_{\mathrm{ML}}=2{,}1$, der größte Wert. Die Likelihood hat dort einen Sprung und keine waagrechte Tangente; rechts davon fällt sie überall. Der Satz über die waagrechte Tangente setzt voraus, dass das Maximum im Inneren eines Intervalls liegt, auf dem die Funktion differenzierbar ist; hier liegt es am Rand des Bereichs, in dem $\mathcal L$ nicht null ist.

(c) $M\le m$ heißt, dass alle $N$ unabhängigen Werte höchstens $m$ sind; jeder ist es mit der Wahrscheinlichkeit $m/\theta$, also $P(M\le m)=(m/\theta)^N$. Abgeleitet ergibt das nach [Grundlagen 4, Abschnitt 6.5](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/zufallsvariablen-und-verteilungen.html#stufe-6-5), die Dichte $N\,m^{N-1}/\theta^N$, und $\mathbb{E}[M]=\int_0^\theta m\cdot\frac{Nm^{N-1}}{\theta^N}\,\mathrm{d} m=\frac N{N+1}\,\theta$. Der Schätzer ist also nicht erwartungstreu, er unterschätzt $\theta$ um den Faktor $N/(N+1)$; der Schätzer $\frac{N+1}NM$ wäre erwartungstreu.
:::
:::

:::aufgabe Aufgabe 22 ★★ Eigene Reißzwecke, Fortsetzung (praktisch)
<span class="anker" id="aufg-22"></span>

Nimm deine $20$ Würfe aus Aufgabe [15](die-likelihood.html#aufg-15).

<ol class="al">

<li>

Berechne $\hat\theta_{\mathrm{ML}}$ und den geschätzten Standardfehler.

</li>

<li>

Gib das Intervall $\hat\theta_{\mathrm{ML}}\pm2\,\widehat{\operatorname{SE}}$ an. Liegt $0{,}5$ darin?

</li>

</ol>

:::loesung
(a) Mit $N_1$ Rückenlagen in $20$ Würfen ist $\hat\theta_{\mathrm{ML}}=N_1/20$ und $\widehat{\operatorname{SE}}=\sqrt{\hat\theta(1-\hat\theta)/20}$. Im Beispiel mit $N_1=12$ ist $\hat\theta=0{,}6$ und $\widehat{\operatorname{SE}}=\sqrt{0{,}24/20}\approx0{,}110$.

(b) Im Beispiel ist das Intervall $0{,}6\pm0{,}22$, also etwa von $0{,}38$ bis $0{,}82$, und $0{,}5$ liegt darin. Zwanzig Würfe reichen dann nicht, um eine Reißzwecke von einer fairen Münze zu unterscheiden.
:::
:::
