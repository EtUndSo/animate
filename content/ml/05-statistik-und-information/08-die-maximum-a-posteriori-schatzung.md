---
title: Die Maximum-a-posteriori-Schätzung
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Statistik und Information
knoten: Grundlagen 5: Statistik und Information
nachschlagen: ja
order: 15250800
summary: Der Posterior enthält alles, was man nach den Daten über den Parameter weiß.
tags: Maximum-a-posteriori-Schätzer, Strafterm
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Der Posterior enthält alles, was man nach den Daten über den Parameter weiß. Oft braucht man trotzdem eine einzige Zahl. Dieser Abschnitt nimmt dafür die Stelle, an der der Posterior am größten ist, zeigt, dass der Prior dabei wie ein Zusatzterm zur Log-Likelihood wirkt, und vergleicht die verschiedenen Schätzer.
:::

### Der MAP-Schätzer

<span class="anker" id="stufe-7-1"></span>

Maximum Likelihood nimmt den Gipfel der Likelihood. Nimmt man stattdessen den Gipfel des Posteriors, so fließt der Prior ein.

:::definition Definition 7.1 (Maximum-a-posteriori-Schätzer)
<span class="anker" id="satz-7-1"></span>

Der __Maximum-a-posteriori-Schätzer__, kurz MAP-Schätzer, ist

<span class="anker" id="gl-7-1"></span>
$$\hat\theta_{\mathrm{MAP}}=\operatorname*{arg\,max}_\theta\,p(\theta\mid\mathcal D)=\operatorname*{arg\,max}_\theta\bigl[\ell(\theta)+\ln p(\theta)\bigr] . \tag{7.1}$$
:::

Die zweite Form folgt aus [(6.5)](prior-und-posterior.html#gl-6-5): Die Evidenz $P(\mathcal D)$ hängt nicht von $\theta$ ab und verschiebt das Maximum nicht, und weil $\ln$ streng monoton wächst, liegt das Maximum von $\mathcal L(\theta)\,p(\theta)$ dort, wo $\ln\mathcal L(\theta)+\ln p(\theta)$ am größten ist. Den Posterior selbst braucht man also nicht; Likelihood und Prior genügen.

⁠**Rechenbeispiel:** Beim Prior $\mathrm{Beta}(\alpha_1,\alpha_0)$ ist der Posterior nach [(6.7)](prior-und-posterior.html#gl-6-7) $\mathrm{Beta}(\alpha_1+N_1,\alpha_0+N_0)$, und sein Modus ist nach dem Satz in Unterabschnitt [6.4](prior-und-posterior.html#stufe-6-4)

<span class="anker" id="gl-7-2"></span>
$$\hat\theta_{\mathrm{MAP}}=\frac{N_1+\alpha_1-1}{N+\alpha_1+\alpha_0-2} . \tag{7.2}$$

Für die verbogene Münze mit dem Prior $\mathrm{Beta}(2,2)$ ist das $\frac{7+1}{10+2}=\frac23\approx0{,}667$. Der Maximum-Likelihood-Schätzer ist $0{,}7$, der Posterior-Mittelwert $\frac9{14}\approx0{,}643$: drei verschiedene Zahlen aus denselben Daten (Abb. [12](prior-und-posterior.html#abb-12)). Mit dem gleichförmigen Prior $\mathrm{Beta}(1,1)$ ist $\ln p(\theta)=0$, und der MAP-Schätzer ist gleich dem Maximum-Likelihood-Schätzer.

:::warnung Gleiche Formel, verschiedene Schätzer
Der MAP-Schätzer mit dem Prior $\mathrm{Beta}(2,2)$ ist $(N_1+1)/(N+2)$, dieselbe Formel wie die Laplace-Regel [(6.10)](prior-und-posterior.html#gl-6-10). Das ist ein Zufall der gewählten Parameter. Die Laplace-Regel ist der Erwartungswert des Posteriors beim Prior $\mathrm{Beta}(1,1)$, der MAP-Schätzer der Gipfel des Posteriors beim Prior $\mathrm{Beta}(2,2)$. Mit anderen Priors fallen die beiden auseinander.
:::

⁠**Kurz gesagt:** Der MAP-Schätzer ist der Gipfel des Posteriors; man findet ihn als Maximum von Log-Likelihood plus Logarithmus des Priors.

### Der Prior als Strafterm

<span class="anker" id="stufe-7-2"></span>

Die Form [(7.1)](#gl-7-1) zeigt, was der Prior beim MAP-Schätzer tut: Er addiert zur Log-Likelihood einen Term, der nur vom Parameter abhängt, nicht von den Daten. Wo der Prior klein ist, ist sein Logarithmus stark negativ, und dieser Term zieht die Bewertung nach unten. Man nennt ihn deshalb auch einen __Strafterm__: Parameterwerte, die man vorher für unplausibel hielt, werden bestraft.

⁠**Rechenbeispiel:** Für den Prior $\mathrm{Beta}(2,2)$ ist $\ln p(\theta)=\ln6+\ln\theta+\ln(1-\theta)$. Bei $\theta=\tfrac12$ ist das $\ln6-2\ln2\approx0{,}405$, bei $\theta=0{,}9$ schon $\ln6+\ln0{,}9+\ln0{,}1\approx-0{,}616$, und für $\theta\to0$ oder $\theta\to1$ fällt es unter jede Schranke. Bei drei Würfen mit dreimal Kopf liegt das Maximum der Log-Likelihood $3\ln\theta$ am Rand $\theta=1$. Zusammen mit dem Strafterm ist das Maximum von $4\ln\theta+\ln(1-\theta)$ nach [(7.2)](#gl-7-2) bei $\tfrac45$. Wächst die Datenmenge, so wächst die Log-Likelihood als Summe mit, der Strafterm aber nicht. Bei $70$ Köpfen in $100$ Würfen ist der MAP-Schätzer $\tfrac{71}{102}\approx0{,}696$, kaum noch vom Maximum-Likelihood-Schätzer $0{,}7$ zu unterscheiden; bei $30$ Köpfen in $30$ Würfen ist er $\tfrac{31}{32}\approx0{,}969$.

⁠**Kurz gesagt:** Beim MAP-Schätzer wirkt der Logarithmus des Priors als Strafterm, der zur Log-Likelihood addiert wird; mit wachsender Datenmenge verliert er an Gewicht.

:::hintergrund Warum ein Strafterm Vorwissen ist, und nicht jeder Strafterm ein Prior
Man kann die Rechnung auch rückwärts lesen. Wer zur Log-Likelihood einen Strafterm $s(\theta)$ addiert, um unplausible Werte zu meiden, rechnet genau dann einen MAP-Schätzer aus, wenn $\mathrm{e}^{s(\theta)}$ nach Normieren eine Wahrscheinlichkeitsdichte ist, die nicht von den Daten abhängt. Dann ist $s(\theta)$ bis auf eine Konstante der Logarithmus eines Priors, und der Strafterm hat eine klare Bedeutung: Er drückt aus, was man vor den Daten für plausibel hielt. Hängt der Strafterm von den Daten ab oder lässt sich $\mathrm{e}^{s}$ nicht normieren, so ist er kein Prior, und die Rechnung hat keine bayessche Deutung. Weil ein fester Strafterm gegen eine mit $N$ wachsende Summe antritt, verschiebt er den Schätzer bei kleinen Datenmengen deutlich und bei großen kaum. Meist macht er den Schätzer stabiler, das heißt, er senkt dessen Varianz, und er macht ihn dafür verzerrt, wie der geschrumpfte Schätzer in Unterabschnitt [2.3](wie-gut-ist-ein-schatzer.html#stufe-2-3).
:::

### Ein Gauß-Prior für einen Mittelwert

<span class="anker" id="stufe-7-3"></span>

Dieselbe Idee funktioniert bei stetigen Daten. Ein Sensor misst eine Spannung mit einem unbekannten Versatz $\mu$; jede Messung ist $x_i=\mu+\nu_i$ mit Rauschen $\nu_i\sim\mathcal N(0,\sigma^2)$ wie in [Grundlagen 4, Abschnitt 8.7](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wichtige-verteilungen.html#stufe-8-7), und die Standardabweichung $\sigma$ des Rauschens ist bekannt. Aus dem Datenblatt weiß man außerdem, dass der Versatz solcher Sensoren um $0$ streut, mit einer Standardabweichung $\tau$. Das ist ein Prior $\mu\sim\mathcal N(\mu_0,\tau^2)$ mit $\mu_0=0$.

:::satz Satz 7.2 (MAP-Schätzer mit Gauß-Prior)
<span class="anker" id="satz-7-2"></span>

Sind die Messwerte $\mathcal N(\mu,\sigma^2)$-verteilt mit bekanntem $\sigma^2$ und ist der Prior $\mathcal N(\mu_0,\tau^2)$, so ist

<span class="anker" id="gl-7-3"></span>
$$\hat\mu_{\mathrm{MAP}}=\frac{\dfrac N{\sigma^2}\,\bar x+\dfrac1{\tau^2}\,\mu_0}{\dfrac N{\sigma^2}+\dfrac1{\tau^2}} . \tag{7.3}$$
:::

:::herleitung MAP-Schätzer mit Gauß-Prior
Nach [(5.4)](die-maximum-likelihood-schatzung.html#gl-5-4) und [Grundlagen 4, Abschnitt 8.5](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wichtige-verteilungen.html#stufe-8-5), ist bis auf Summanden, die nicht von $\mu$ abhängen,

$$\ell(\mu)+\ln p(\mu)=-\frac1{2\sigma^2}\sum_{i=1}^N(x_i-\mu)^2-\frac1{2\tau^2}(\mu-\mu_0)^2 .$$

Die Ableitung nach $\mu$ ist $\frac1{\sigma^2}\sum_i(x_i-\mu)-\frac1{\tau^2}(\mu-\mu_0)=\frac N{\sigma^2}(\bar x-\mu)-\frac1{\tau^2}(\mu-\mu_0)$. Sie fällt mit wachsendem $\mu$ und ist null, wenn $\mu\,\bigl(\frac N{\sigma^2}+\frac1{\tau^2}\bigr)=\frac N{\sigma^2}\bar x+\frac1{\tau^2}\mu_0$ ist. Nach dem Satz über den Vorzeichenwechsel ist das der höchste Punkt.
:::

Der MAP-Schätzer ist ein gewichtetes Mittel aus dem Mittelwert der Messungen und dem Erwartungswert des Priors. Die Gewichte sind die Kehrwerte der Varianzen: $N/\sigma^2$ ist der Kehrwert von $\operatorname{Var}(\bar X)=\sigma^2/N$, und $1/\tau^2$ der Kehrwert der Prior-Varianz. Der Prior wirkt also wie eine zusätzliche Messung mit der Varianz $\tau^2$, genau wie bei den zwei Messgeräten in Aufgabe [5](wie-gut-ist-ein-schatzer.html#aufg-5). Der Strafterm $-(\mu-\mu_0)^2/(2\tau^2)$ ist quadratisch: Er bestraft den Abstand von $\mu_0$ umso stärker, je kleiner $\tau$ ist.

⁠**Rechenbeispiel:** Es sei $\sigma=2\,\mathrm{mV}$, $\tau=1\,\mathrm{mV}$ und $\mu_0=0$. Aus $N=4$ Messungen ergibt sich $\bar x=1{,}5\,\mathrm{mV}$. Die Gewichte sind $N/\sigma^2=4/4=1\,\mathrm{mV}^{-2}$ und $1/\tau^2=1\,\mathrm{mV}^{-2}$, also ist $\hat\mu_{\mathrm{MAP}}=\frac{1\cdot1{,}5+1\cdot0}{1+1}=0{,}75\,\mathrm{mV}$. Mit $N=36$ Messungen und demselben Mittelwert ist das Gewicht der Daten $9$, und $\hat\mu_{\mathrm{MAP}}=\frac{9\cdot1{,}5}{9+1}=1{,}35\,\mathrm{mV}$. Mit wachsender Zahl der Messungen rückt der MAP-Schätzer an den Maximum-Likelihood-Schätzer $\bar x$ heran.

⁠**Kurz gesagt:** Mit einem Gauß-Prior ist der MAP-Schätzer des Erwartungswerts ein Mittel aus Messmittelwert und Prior-Erwartungswert, gewichtet mit den Kehrwerten der Varianzen.

:::hintergrund Auch der Posterior ist normal
Der Logarithmus von Likelihood mal Prior ist im Beispiel eine nach unten geöffnete Parabel in $\mu$. Ergänzt man quadratisch wie in [Grundlagen 2, Abschnitt 5.4](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-4), so schreibt er sich als $-\frac1{2s^2}(\mu-\hat\mu_{\mathrm{MAP}})^2$ plus eine Konstante, mit $\frac1{s^2}=\frac N{\sigma^2}+\frac1{\tau^2}$. Der Posterior ist also die Normalverteilung $\mathcal N(\hat\mu_{\mathrm{MAP}},s^2)$: Die Normalverteilung ist zu sich selbst konjugiert. Bei ihr fallen Gipfel und Erwartungswert zusammen, MAP-Schätzer und Posterior-Mittelwert sind hier gleich. Die Kehrwerte der Varianzen addieren sich: Jede Informationsquelle macht den Posterior schmaler. Im Beispiel mit $N=4$ ist $1/s^2=2\,\mathrm{mV}^{-2}$, also $s\approx0{,}71\,\mathrm{mV}$, schmaler als der Standardfehler $1\,\mathrm{mV}$ des Mittelwerts allein und als die Prior-Standardabweichung $1\,\mathrm{mV}$.
:::

### Drei Schätzer im Vergleich

<span class="anker" id="stufe-7-4"></span>

Aus denselben Daten und demselben Modell sind drei Schätzer entstanden: der Maximum-Likelihood-Schätzer, der MAP-Schätzer und der Posterior-Mittelwert. Tabelle [3](#tab-3) stellt sie für das Bernoulli-Modell mit dem Prior $\mathrm{Beta}(2,2)$ nebeneinander.

<span class="anker" id="tab-3"></span>

**Tabelle 3:** Drei Schätzer für das Bernoulli-Modell, die beiden letzten mit dem Prior $\mathrm{Beta}(2,2)$.

| Schätzer | Formel | $7$ von $10$ | $3$ von $3$ | $N\to\infty$ |
|---|---|---|---|---|
| Maximum Likelihood | $\dfrac{N_1}N$ | $0{,}7$ | $1$ | $N_1/N$ |
| [2mm] MAP | $\dfrac{N_1+1}{N+2}$ | $\tfrac23\approx0{,}667$ | $\tfrac45=0{,}8$ | nähert sich $N_1/N$ |
| [2mm] Posterior-Mittelwert | $\dfrac{N_1+2}{N+4}$ | $\tfrac9{14}\approx0{,}643$ | $\tfrac57\approx0{,}714$ | nähert sich $N_1/N$ |

Bei vielen Daten liefern alle drei fast dieselbe Zahl, denn das Gewicht des Priors geht gegen null. Bei wenigen Daten unterscheiden sie sich. Maximum Likelihood nimmt die Daten wörtlich, die beiden anderen ziehen das Ergebnis zum Prior hin. MAP-Schätzer und Posterior-Mittelwert fallen auseinander, sobald der Posterior schief ist; bei einem symmetrischen Posterior wie im Gauß-Beispiel fallen sie zusammen.

Zwei Eigenschaften unterscheiden sie grundsätzlich. Erstens verträgt der MAP-Schätzer keine Umrechnung des Parameters. Er ist der Gipfel einer Dichte, und nach dem Hintergrund-Kasten in Unterabschnitt [5.5](die-maximum-likelihood-schatzung.html#stufe-5-5) verschiebt eine nichtlineare Umrechnung den Gipfel einer Dichte. Der Maximum-Likelihood-Schätzer hat dieses Problem nach dem Satz in Unterabschnitt [5.5](die-maximum-likelihood-schatzung.html#stufe-5-5) nicht. Zweitens fasst jede einzelne Zahl den Posterior nur zusammen. Wie breit er ist, also wie unsicher man nach den Daten noch ist, sagt keiner der beiden bayesschen Schätzer.

⁠**Rechenbeispiel:** Nach zehn Würfen mit dem Prior $\mathrm{Beta}(2,2)$ ist der Posterior $\mathrm{Beta}(9,5)$ mit dem Gipfel bei $\tfrac23$. Fragt man nach der Chance $\theta/(1-\theta)$, so liefert der Maximum-Likelihood-Schätzer $\tfrac{0{,}7}{0{,}3}=\tfrac73$, also die umgerechnete Zahl. Der Gipfel des Posteriors, umgerechnet auf die Chance, ist $\tfrac{2/3}{1/3}=2$. Rechnet man aber die Dichte selbst auf eine andere Größe um und sucht dort den Gipfel, so landet man bei einem anderen $\theta$; der Hintergrund-Kasten rechnet das vor.

⁠**Kurz gesagt:** Maximum Likelihood, MAP und Posterior-Mittelwert stimmen bei vielen Daten überein und unterscheiden sich bei wenigen; nur der Maximum-Likelihood-Schätzer verträgt jede umkehrbare Umrechnung des Parameters.

:::hintergrund Derselbe Posterior, ein anderer Gipfel
Man beschreibe die Münze statt mit $\theta$ mit $\eta=\ln\frac\theta{1-\theta}$, dem Logarithmus der Chance. Diese Umrechnung ist die Umkehrung der logistischen Funktion aus [Grundlagen 3, Abschnitt 2.4](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/die-kettenregel.html#stufe-2-4), also ist $\theta=\sigma(\eta)$ und nach der dortigen Ableitungsregel $\frac{\mathrm{d}\theta}{\mathrm{d}\eta}=\theta(1-\theta)$. Nach dem Variablenwechsel aus [Grundlagen 4, Abschnitt 8.6](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wichtige-verteilungen.html#stufe-8-6), hat $\eta$ unter dem Posterior $\mathrm{Beta}(9,5)$ die Dichte

$$p_\eta(\eta)=p\bigl(\theta(\eta)\mid\mathcal D\bigr)\cdot\theta(1-\theta)\propto\theta^8(1-\theta)^4\cdot\theta(1-\theta)=\theta^9(1-\theta)^5 .$$

Weil $\theta(\eta)$ mit $\eta$ wächst, liegt der Gipfel von $p_\eta$ dort, wo $\theta^9(1-\theta)^5$ am größten ist, nach dem Satz in Unterabschnitt [5.2](die-maximum-likelihood-schatzung.html#stufe-5-2) bei $\theta=\tfrac9{14}\approx0{,}643$. Derselbe Posterior hat also in der Beschreibung durch $\theta$ den Gipfel bei $\tfrac23$ und in der Beschreibung durch $\eta$ einen Gipfel, der zu $\theta=\tfrac9{14}$ gehört. Der Faktor $\theta(1-\theta)$ aus dem Variablenwechsel hat ihn verschoben. Dass dabei gerade der Posterior-Mittelwert herauskommt, ist ein Zufall dieses Beispiels. Die Likelihood bekommt beim Umrechnen keinen solchen Faktor, weil sie keine Dichte über dem Parameter ist.
:::

:::aufgabe Aufgabe 28 ★ Drei Schätzer für die Reißzwecke
<span class="anker" id="aufg-28"></span>

Die Reißzwecke landete in acht Würfen fünfmal auf dem Rücken. Der Prior sei $\mathrm{Beta}(3,3)$.

<ol class="al">

<li>

Gib den Posterior an.

</li>

<li>

Berechne den Maximum-Likelihood-Schätzer, den MAP-Schätzer und den Posterior-Mittelwert.

</li>

</ol>

:::loesung
(a) $\mathrm{Beta}(3+5,\,3+3)=\mathrm{Beta}(8,6)$.

(b) $\hat\theta_{\mathrm{ML}}=\tfrac58=0{,}625$, $\hat\theta_{\mathrm{MAP}}=\tfrac{8-1}{14-2}=\tfrac7{12}\approx0{,}583$, Posterior-Mittelwert $\tfrac8{14}=\tfrac47\approx0{,}571$.
:::
:::

:::aufgabe Aufgabe 29 ★★ Der Strafterm verliert
<span class="anker" id="aufg-29"></span>

Es sei der Prior $\mathrm{Beta}(2,2)$.

<ol class="al">

<li>

Zeige: $\hat\theta_{\mathrm{MAP}}-\hat\theta_{\mathrm{ML}}=\dfrac{N-2N_1}{N(N+2)}$.

</li>

<li>

Wie groß kann der Unterschied bei $N=100$ höchstens werden? Für welches $N_1$?

</li>

</ol>

:::loesung
(a) $\frac{N_1+1}{N+2}-\frac{N_1}N=\frac{N(N_1+1)-N_1(N+2)}{N(N+2)}=\frac{N-2N_1}{N(N+2)}$.

(b) Der Betrag $|N-2N_1|$ ist am größten für $N_1=0$ oder $N_1=N$, dann ist er $N$. Der Unterschied ist höchstens $\frac1{N+2}=\frac1{102}\approx0{,}0098$. Bei $N_1=50$ ist er null, denn dort stimmen Prior-Gipfel und Maximum-Likelihood-Schätzer überein.
:::
:::

:::aufgabe Aufgabe 30 ★★ Kalibrieren mit Vorwissen
<span class="anker" id="aufg-30"></span>

Ein Thermometer hat eine unbekannte Abweichung $\mu$; der Hersteller gibt einen Prior $\mathcal N(0;\ (0{,}5\,\mathrm K)^2)$ an. Neun Messungen in einem Bad mit genau bekannter Temperatur ergeben Abweichungen mit dem Mittelwert $0{,}8\,\mathrm K$; das Rauschen einer Messung hat $\sigma=1{,}5\,\mathrm K$.

<ol class="al">

<li>

Berechne den MAP-Schätzer der Abweichung.

</li>

<li>

Wie viele Messungen bräuchte man, damit das Gewicht der Daten $90\,\%$ beträgt?

</li>

</ol>

:::loesung
(a) Das Gewicht der Daten ist $N/\sigma^2=9/2{,}25=4\,\mathrm K^{-2}$, das des Priors $1/0{,}5^2=4\,\mathrm K^{-2}$. Also ist $\hat\mu_{\mathrm{MAP}}=\frac{4\cdot0{,}8+4\cdot0}{8}=0{,}4\,\mathrm K$.

(b) Verlangt ist $\frac{N/2{,}25}{N/2{,}25+4}=0{,}9$, also $N/2{,}25=36$ und $N=81$.
:::
:::

:::aufgabe Aufgabe 31 ★★ Eigene Reißzwecke, Abschluss (praktisch)
<span class="anker" id="aufg-31"></span>

Nimm deine $20$ Würfe aus Aufgabe [15](die-likelihood.html#aufg-15) und den Prior $\mathrm{Beta}(2,2)$.

<ol class="al">

<li>

Gib den Posterior an, den MAP-Schätzer und den Posterior-Mittelwert, und vergleiche mit deinem Maximum-Likelihood-Schätzer aus Aufgabe [22](die-maximum-likelihood-schatzung.html#aufg-22).

</li>

<li>

Skizziere Prior und Posterior wie in Abb. [12](prior-und-posterior.html#abb-12).

</li>

</ol>

:::loesung
(a) Mit $N_1$ Rückenlagen in $20$ Würfen ist der Posterior $\mathrm{Beta}(N_1+2,\,22-N_1)$, der MAP-Schätzer $\frac{N_1+1}{22}$ und der Posterior-Mittelwert $\frac{N_1+2}{24}$. Im Beispiel mit $N_1=12$: $\mathrm{Beta}(14,10)$, MAP $\tfrac{13}{22}\approx0{,}591$, Mittelwert $\tfrac{14}{24}\approx0{,}583$, Maximum Likelihood $0{,}6$. Alle drei liegen nahe beieinander, der Prior zieht etwas zur Mitte.

(b) Der Prior ist der flache Hügel $6\theta(1-\theta)$; der Posterior ist schmaler und hat seinen Gipfel bei $\tfrac{N_1+1}{22}$.
:::
:::

:::aufgabe Aufgabe 32 ★★★ Der Gipfel einer umgerechneten Dichte
<span class="anker" id="aufg-32"></span>

Die Gleichverteilung $\mathrm{Beta}(1,1)$ hat keinen einzelnen Gipfel. Rechne sie auf $\eta=\ln\frac\theta{1-\theta}$ um.

<ol class="al">

<li>

Zeige, dass $\eta$ die Dichte $p_\eta(\eta)=\sigma(\eta)\bigl(1-\sigma(\eta)\bigr)$ hat, mit der logistischen Funktion $\sigma$.

</li>

<li>

Wo liegt ihr Gipfel? Was lernt man daraus über die Aussage „der Prior bevorzugt keinen Wert“?

</li>

</ol>

:::loesung
(a) Mit $\theta=\sigma(\eta)$ und $\mathrm{d}\theta/\mathrm{d}\eta=\sigma(\eta)(1-\sigma(\eta))$ ist nach dem Variablenwechsel $p_\eta(\eta)=1\cdot\sigma(\eta)(1-\sigma(\eta))$.

(b) Nach [Grundlagen 3, Abschnitt 2.4](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/die-kettenregel.html#stufe-2-4), ist $\sigma(1-\sigma)$ am größten bei $\eta=0$, mit dem Wert $\tfrac14$. Die Dichte von $\eta$ hat also einen Gipfel bei $\eta=0$, also bei $\theta=\tfrac12$, obwohl die Dichte von $\theta$ überall gleich ist. „Keine Vorliebe“ ist keine Eigenschaft eines Priors allein, sondern hängt davon ab, mit welcher Größe man den Parameter beschreibt.
:::
:::
