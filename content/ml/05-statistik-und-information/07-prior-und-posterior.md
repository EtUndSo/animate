---
title: Prior und Posterior
pfad: Informatik / Machine Learning / Statistik und Information
order: 6250700
summary: Wer eine Münze aus der Geldbörse wirft, ist schon vor dem ersten Wurf ziemlich sicher, dass sie etwa gleich oft Kopf und Zahl zeigt.
tags: bayessche, Prior, Beta-Verteilung, Posterior, Evidenz, konjugiert, Pseudobeobachtungen, Laplace-Regel
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Wer eine Münze aus der Geldbörse wirft, ist schon vor dem ersten Wurf ziemlich sicher, dass sie etwa gleich oft Kopf und Zahl zeigt. Dieser Abschnitt baut solches Vorwissen mit dem Satz von Bayes aus [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html) in die Schätzung ein: Der unbekannte Parameter bekommt selbst eine Verteilung, und die Daten verschieben sie.
:::

### Der Satz von Bayes für Parameter

<span class="anker" id="stufe-6-1"></span>

In der frequentistischen Sicht aus Abschnitt [1](schatzen-aus-einer-stichprobe.html#stufe-1) ist der Parameter eine feste Zahl, und Wahrscheinlichkeiten gibt es nur für die Daten. Es gibt eine zweite Sicht, nach dem englischen Mathematiker Thomas Bayes die __bayessche__ genannt. In ihr misst eine Wahrscheinlichkeit, wie sicher man sich einer Sache ist, und deshalb darf auch ein unbekannter Parameter eine Verteilung haben. Sie drückt aus, welche Werte man für plausibel hält. Neue Daten ändern diese Verteilung nach dem Satz von Bayes aus [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 4.1. Es gibt Lagen, in denen beide Sichten sich einig sind, weil der Parameter tatsächlich durch einen Zufall bestimmt wurde. Mit einer solchen Lage beginnt dieser Abschnitt.

⁠**Rechenbeispiel: die Münzkiste.** In einer Kiste liegen vier Münzen: eine, die mit der Wahrscheinlichkeit $\tfrac14$ Kopf zeigt, zwei faire und eine, die mit der Wahrscheinlichkeit $\tfrac34$ Kopf zeigt. Man zieht blind eine Münze und wirft sie viermal: Kopf, Kopf, Zahl, Kopf. Welche Münze war es? Vor den Würfen hat $\theta$ die Werte $\tfrac14$, $\tfrac12$, $\tfrac34$ mit den Wahrscheinlichkeiten $\tfrac14$, $\tfrac12$, $\tfrac14$. Die Likelihood der Würfe ist $\theta^3(1-\theta)$, also

$$\mathcal L(\tfrac14)=\tfrac1{64}\cdot\tfrac34=\tfrac3{256},\qquad \mathcal L(\tfrac12)=\tfrac1{16}=\tfrac{16}{256},\qquad \mathcal L(\tfrac34)=\tfrac{27}{64}\cdot\tfrac14=\tfrac{27}{256} .$$

Nach dem Satz von Bayes mit der totalen Wahrscheinlichkeit aus [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 3.4, ist

<span class="anker" id="gl-6-1"></span>
$$P(\theta=\theta_k\mid\mathcal D)=\frac{P(\mathcal D\mid\theta_k)\,P(\theta=\theta_k)}{P(\mathcal D)},\qquad P(\mathcal D)=\sum_kP(\mathcal D\mid\theta_k)\,P(\theta=\theta_k) . \tag{6.1}$$

Die Wahrscheinlichkeit der Daten ist $P(\mathcal D)=\tfrac{31}{512}$ (Abb. [10](#abb-10)). Nach den Würfen hat $\theta$ also die Werte $\tfrac14$, $\tfrac12$, $\tfrac34$ mit den Wahrscheinlichkeiten

$$\frac{3/1024}{31/512}=\frac3{62}\approx0{,}048,\qquad \frac{16/512}{31/512}=\frac{16}{31}\approx0{,}516,\qquad \frac{27/1024}{31/512}=\frac{27}{62}\approx0{,}435 .$$

Die größte Likelihood hat die Münze mit $\theta=\tfrac34$; der Maximum-Likelihood-Schätzer unter den drei Werten wäre also $\tfrac34$. Trotzdem ist nach den Würfen eine faire Münze am wahrscheinlichsten, weil es doppelt so viele faire Münzen in der Kiste gibt. Vier Würfe reichen nicht, um diesen Vorsprung ganz aufzuholen.

:::abbildung ml/k5rbayes 10
Die Wahrscheinlichkeit der Würfe Kopf, Kopf, Zahl, Kopf mit einer zufällig gezogenen Münze aus der Kiste: die Likelihood jeder Münzsorte, gewichtet mit dem Anteil dieser Sorte in der Kiste.
:::

⁠**Kurz gesagt:** Gibt man dem Parameter eine Verteilung, so liefert der Satz von Bayes seine Verteilung nach den Daten: Likelihood mal Wahrscheinlichkeit vor den Daten, geteilt durch die Wahrscheinlichkeit der Daten.

:::hintergrund Zwei Deutungen von Wahrscheinlichkeit
In der frequentistischen Deutung ist eine Wahrscheinlichkeit der Grenzwert einer relativen Häufigkeit bei vielen Wiederholungen, wie in [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 2.1. Für eine Münze im Geldbeutel gibt es keine Wiederholungen ihres $\theta$; es hat einen festen Wert, und von seiner Wahrscheinlichkeit zu sprechen, ergibt in dieser Deutung keinen Sinn. In der bayesschen Deutung ist eine Wahrscheinlichkeit ein Grad der Überzeugung, der sich an dieselben Rechenregeln hält. Dass diese Regeln für Überzeugungen gelten sollen, begründet man damit, dass jemand, der sich bei Wetten nicht an sie hält, gegen eine geschickte Kombination von Wetten mit Sicherheit verliert. Bei der Münzkiste sind beide Deutungen einig, denn das Ziehen der Münze ist ein echter Zufall mit bekannten Häufigkeiten. Der Streit beginnt erst dort, wo die Verteilung vor den Daten nur das Vorwissen einer Person ausdrückt. Thomas Bayes' Arbeit zu diesem Schluss erschien 1763, zwei Jahre nach seinem Tod.
:::

### Die Prior-Verteilung

<span class="anker" id="stufe-6-2"></span>

Bei der Münzkiste war die Verteilung von $\theta$ vor den Würfen durch den Inhalt der Kiste gegeben. Bei einer einzelnen Münze aus dem Geldbeutel gibt es keine Kiste, aber Vorwissen: Münzen sind fast immer nahezu fair. Dieses Vorwissen schreibt man als Verteilung auf, und weil $\theta$ jeden Wert zwischen $0$ und $1$ haben kann, als Dichte.

:::definition Definition 6.1 (Prior)
<span class="anker" id="satz-6-1"></span>

Die Verteilung, die man dem Parameter gibt, bevor man die Daten kennt, heißt __Prior__ oder a-priori-Verteilung. Hat der Parameter endlich viele mögliche Werte, besteht sie aus Wahrscheinlichkeiten $P(\theta=\theta_k)$; kann er alle Werte eines Intervalls annehmen, aus einer Dichte $p(\theta)$.
:::

Der Prior übernimmt die Rolle, die in [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 4.1 und 4.3, die Ausgangswahrscheinlichkeit und die Basisrate hatten. Das lateinische *a priori* heißt „vom Früheren her“, hier: vor den Daten.

⁠**Rechenbeispiel:** Der Prior $p(\theta)=1$ für $0\le\theta\le1$ ist die Gleichverteilung aus [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 8.4. Er bevorzugt keinen Wert. Der Prior $p(\theta)=6\theta(1-\theta)$ hat die Fläche $6\,(\tfrac12-\tfrac13)=1$ und ist bei $\theta=\tfrac12$ am höchsten. Mit der Stammfunktion $3\theta^2-2\theta^3$ gibt er dem Bereich $0{,}25\le\theta\le0{,}75$ die Wahrscheinlichkeit $(1{,}6875-0{,}84375)-(0{,}1875-0{,}03125)=0{,}6875$. Er drückt also aus: Die Münze ist eher fair, aber auch deutlich unfaire Münzen sind nicht ausgeschlossen.

⁠**Kurz gesagt:** Der Prior ist die Verteilung des Parameters vor den Daten; er hält fest, welche Werte man aus Vorwissen für plausibel hält.

:::warnung Ein Prior von null ist endgültig
Gibt der Prior einem Wert die Wahrscheinlichkeit oder Dichte null, so bleibt sie nach dem Satz von Bayes für jede Datenmenge null, denn der Zähler ist das Produkt aus Likelihood und Prior. Wer einen Wert vorher für unmöglich erklärt, kann durch keine Beobachtung umgestimmt werden. Den Wert $0$ oder $1$ gibt man deshalb nur Aussagen, die logisch sicher falsch oder wahr sind. Der Statistiker Dennis Lindley hat diese Regel nach Oliver Cromwell benannt, der 1650 an eine Kirchenversammlung schrieb, sie möge es für möglich halten, sich zu irren.
:::

### Was du dafür brauchst: Ein Integral über Potenzen

<span class="anker" id="stufe-6-3"></span>

Likelihood und Prior einer Münze sind Produkte aus Potenzen von $\theta$ und $1-\theta$. Ihre Fläche braucht man, um eine Dichte auf die Gesamtfläche $1$ zu bringen. Dafür gibt es eine geschlossene Formel.

:::satz Satz 6.2 (Integral über Potenzen von $\theta$ und $1-\theta$)
<span class="anker" id="satz-6-2"></span>

Für natürliche Zahlen $m,n\ge0$ ist

<span class="anker" id="gl-6-2"></span>
$$\int_0^1\theta^m(1-\theta)^n\,\mathrm{d}\theta=\frac{m!\,n!}{(m+n+1)!} . \tag{6.2}$$
:::

:::herleitung Integral über Potenzen
Es sei $I(m,n)$ das Integral. Für $n=0$ ist $I(m,0)=\int_0^1\theta^m\,\mathrm{d}\theta=\frac1{m+1}=\frac{m!\,0!}{(m+1)!}$. Für $n\ge1$ integriert man partiell mit $u=(1-\theta)^n$ und $v'=\theta^m$, also $u'=-n(1-\theta)^{n-1}$ und $v=\theta^{m+1}/(m+1)$:

$$I(m,n)=\Bigl[\frac{\theta^{m+1}}{m+1}(1-\theta)^n\Bigr]_0^1+\frac n{m+1}\int_0^1\theta^{m+1}(1-\theta)^{n-1}\,\mathrm{d}\theta=\frac n{m+1}\,I(m+1,n-1) .$$

Der Randterm ist null, weil bei $\theta=0$ der erste und bei $\theta=1$ der zweite Faktor verschwindet. Wendet man das $n$-mal an, so wandert jedes Mal eine Potenz von $1-\theta$ zu $\theta$:

$$I(m,n)=\frac n{m+1}\cdot\frac{n-1}{m+2}\cdots\frac1{m+n}\;I(m+n,0)=\frac{n!\,m!}{(m+n)!}\cdot\frac1{m+n+1}=\frac{m!\,n!}{(m+n+1)!} .$$
:::

⁠**Rechenbeispiel:** Für $m=7$ und $n=3$ ist das Integral $\frac{7!\,3!}{11!}=\frac{6}{8\cdot9\cdot10\cdot11}=\frac6{7920}=\frac1{1320}$, wie in Unterabschnitt [4.2](die-likelihood.html#stufe-4-2) durch Ausmultiplizieren berechnet. Für $m=n=1$ ist es $\frac{1\cdot1}{3!}=\frac16$; daher kommt der Faktor $6$ im Prior $6\theta(1-\theta)$.

⁠**Kurz gesagt:** $\int_0^1\theta^m(1-\theta)^n\,\mathrm{d}\theta=\frac{m!\,n!}{(m+n+1)!}$; man beweist es durch wiederholtes partielles Integrieren.

:::hintergrund Ein Beweis ohne Rechnung
Die Formel hat eine Deutung durch Zufallszahlen, die auf Thomas Bayes zurückgeht. Man wählt $m+n+1$ Zahlen unabhängig und gleichverteilt aus $[0,\,1]$ und fragt: Wie wahrscheinlich liegen die ersten $m$ links von der letzten und die folgenden $n$ rechts von ihr? Hat die letzte den Wert $\theta$, so ist das $\theta^m(1-\theta)^n$; mittelt man über alle $\theta$, erhält man das Integral. Andererseits sind alle $(m+n+1)!$ Anordnungen der Zahlen gleich wahrscheinlich. Günstig sind die, in denen die letzte Zahl an Platz $m+1$ steht, die ersten $m$ Zahlen in beliebiger Reihenfolge davor und die übrigen $n$ in beliebiger Reihenfolge danach. Das sind $m!\,n!$ Anordnungen, also ist die Wahrscheinlichkeit $\frac{m!\,n!}{(m+n+1)!}$.
:::

### Die Beta-Verteilung

<span class="anker" id="stufe-6-4"></span>

Der Prior $6\theta(1-\theta)$ hat dieselbe Form wie die Likelihood einer Münze: eine Potenz von $\theta$ mal eine Potenz von $1-\theta$. Dichten dieser Form bilden eine eigene Familie. Sie eignet sich gut für Parameter, die zwischen $0$ und $1$ liegen.

:::definition Definition 6.3 (Beta-Verteilung)
<span class="anker" id="satz-6-3"></span>

Für natürliche Zahlen $\alpha_1,\alpha_0\ge1$ heißt die Verteilung mit der Dichte

<span class="anker" id="gl-6-3"></span>
$$p(\theta)=\frac{\theta^{\alpha_1-1}(1-\theta)^{\alpha_0-1}}{B(\alpha_1,\alpha_0)}\quad\text{für }0\le\theta\le1,\qquad B(\alpha_1,\alpha_0)=\frac{(\alpha_1-1)!\,(\alpha_0-1)!}{(\alpha_1+\alpha_0-1)!}, \tag{6.3}$$

und $p(\theta)=0$ sonst, die __Beta-Verteilung__ $\mathrm{Beta}(\alpha_1,\alpha_0)$.
:::

Nach [(6.2)](#gl-6-2) mit $m=\alpha_1-1$ und $n=\alpha_0-1$ ist $B(\alpha_1,\alpha_0)$ genau die Fläche unter dem Zähler, die Dichte hat also die Gesamtfläche $1$. Die Indizes deuten an, dass $\alpha_1$ zur Potenz von $\theta$ gehört, der Wahrscheinlichkeit einer Eins, und $\alpha_0$ zur Potenz von $1-\theta$; der nächste Unterabschnitt zeigt, dass sie sich wie Anzahlen von Einsen und Nullen verhalten. Viele Bücher schreiben $\mathrm{Beta}(a,b)$ oder $\mathrm{Beta}(\alpha,\beta)$.

:::satz Satz 6.4 (Erwartungswert und Modus der Beta-Verteilung)
<span class="anker" id="satz-6-4"></span>

Für $\theta\sim\mathrm{Beta}(\alpha_1,\alpha_0)$ ist

<span class="anker" id="gl-6-4"></span>
$$\mathbb{E}[\theta]=\frac{\alpha_1}{\alpha_1+\alpha_0}, \tag{6.4}$$

und für $\alpha_1+\alpha_0>2$ liegt das Maximum der Dichte, der Modus, bei $\dfrac{\alpha_1-1}{\alpha_1+\alpha_0-2}$.
:::

:::herleitung Erwartungswert und Modus
Der Erwartungswert ist $\int_0^1\theta\,p(\theta)\,\mathrm{d}\theta$. Der Faktor $\theta$ erhöht die Potenz von $\theta$ um eins, also ist nach [(6.2)](#gl-6-2)

$$\mathbb{E}[\theta]=\frac{B(\alpha_1+1,\alpha_0)}{B(\alpha_1,\alpha_0)}=\frac{\alpha_1!\,(\alpha_0-1)!}{(\alpha_1+\alpha_0)!}\cdot\frac{(\alpha_1+\alpha_0-1)!}{(\alpha_1-1)!\,(\alpha_0-1)!}=\frac{\alpha_1}{\alpha_1+\alpha_0} .$$

Für den Modus maximiert man den Logarithmus der Dichte, $(\alpha_1-1)\ln\theta+(\alpha_0-1)\ln(1-\theta)$ plus eine Konstante. Das ist die Log-Likelihood [(4.7)](die-likelihood.html#gl-4-7) mit $N_1=\alpha_1-1$ und $N_0=\alpha_0-1$, und nach dem Satz in Unterabschnitt [5.2](die-maximum-likelihood-schatzung.html#stufe-5-2) liegt ihr Maximum bei $N_1/(N_1+N_0)=(\alpha_1-1)/(\alpha_1+\alpha_0-2)$.
:::

⁠**Rechenbeispiel:** $\mathrm{Beta}(1,1)$ hat die Dichte $1$, ist also die Gleichverteilung, mit dem Erwartungswert $\tfrac12$ und ohne einzelnen Modus. $\mathrm{Beta}(2,2)$ hat $B=\frac{1!\,1!}{3!}=\frac16$, also die Dichte $6\theta(1-\theta)$ aus Unterabschnitt [6.2](#stufe-6-2), mit Erwartungswert und Modus $\tfrac12$. $\mathrm{Beta}(5,2)$ hat die Dichte $30\,\theta^4(1-\theta)$, den Erwartungswert $\tfrac57\approx0{,}714$ und den Modus $\tfrac45$. $\mathrm{Beta}(9,5)$ hat den Erwartungswert $\tfrac9{14}\approx0{,}643$ und den Modus $\tfrac8{12}=\tfrac23$. Abb. [11](#abb-11) zeigt die vier Dichten. Je größer $\alpha_1+\alpha_0$, desto schmaler die Kurve; bei schiefen Kurven liegt der Erwartungswert näher an der Mitte als der Modus.

:::abbildung ml/k5beta 11
Vier Beta-Dichten. $\mathrm{Beta}(1,1)$ ist die Gleichverteilung, $\mathrm{Beta}(2,2)$ ein flacher Hügel um $\tfrac12$. $\mathrm{Beta}(5,2)$ ist nach rechts verschoben, mit dem Gipfel bei $0{,}8$. $\mathrm{Beta}(9,5)$ ist schmaler, mit dem Gipfel bei $\tfrac23$ und dem Wert $3{,}10$ dort.
:::

⁠**Kurz gesagt:** Die Beta-Verteilung $\mathrm{Beta}(\alpha_1,\alpha_0)$ hat eine Dichte proportional zu $\theta^{\alpha_1-1}(1-\theta)^{\alpha_0-1}$, den Erwartungswert $\alpha_1/(\alpha_1+\alpha_0)$ und den Modus $(\alpha_1-1)/(\alpha_1+\alpha_0-2)$.

:::hintergrund Nicht ganzzahlige Parameter
Die Beta-Verteilung ist auch für alle reellen $\alpha_1,\alpha_0>0$ erklärt. Man ersetzt dann die Fakultäten durch die Gammafunktion, die die Fakultät auf reelle Zahlen fortsetzt: $\Gamma(n)=(n-1)!$ für natürliche $n$. Der Erwartungswert bleibt $\alpha_1/(\alpha_1+\alpha_0)$. Für Parameter unter $1$ wird die Dichte am Rand unendlich groß; $\mathrm{Beta}(\tfrac12,\tfrac12)$ hat die Form eines U und hält Werte nahe $0$ und $1$ für plausibler als die Mitte. Dieses Kapitel kommt mit ganzzahligen Parametern aus.
:::

### Die Posterior-Verteilung

<span class="anker" id="stufe-6-5"></span>

Bei der Münzkiste lieferte der Satz von Bayes die Verteilung von $\theta$ nach den Würfen. Mit einem Prior, der eine Dichte ist, geht dieselbe Rechnung, nur wird die Summe über die möglichen Werte von $\theta$ zu einem Integral.

:::definition Definition 6.5 (Posterior)
<span class="anker" id="satz-6-5"></span>

Die Verteilung des Parameters nach den Daten heißt __Posterior__ oder a-posteriori-Verteilung. Für einen Prior mit der Dichte $p(\theta)$ hat sie die Dichte

<span class="anker" id="gl-6-5"></span>
$$p(\theta\mid\mathcal D)=\frac{\mathcal L(\theta)\,p(\theta)}{P(\mathcal D)},\qquad P(\mathcal D)=\int\mathcal L(\theta)\,p(\theta)\,\mathrm{d}\theta . \tag{6.5}$$
:::

Der Nenner $P(\mathcal D)$ ist die Wahrscheinlichkeit der Daten, gemittelt über alle Parameterwerte mit dem Prior als Gewicht, und wird oft __Evidenz__ genannt. Er hängt nicht von $\theta$ ab und sorgt nur dafür, dass der Posterior die Fläche $1$ hat. Man schreibt deshalb kurz

<span class="anker" id="gl-6-6"></span>
$$p(\theta\mid\mathcal D)\propto\mathcal L(\theta)\,p(\theta) , \tag{6.6}$$

gelesen „proportional zu“: gleich bis auf einen Faktor, der nicht von $\theta$ abhängt. In Worten: Posterior ist Likelihood mal Prior, auf die Fläche $1$ gebracht.

⁠**Rechenbeispiel:** Für die verbogene Münze mit dem Prior $\mathrm{Beta}(2,2)$ und sieben Köpfen in zehn Würfen ist

$$p(\theta\mid\mathcal D)\propto\theta^7(1-\theta)^3\cdot\theta(1-\theta)=\theta^8(1-\theta)^4 .$$

Das ist bis auf den Faktor die Dichte von $\mathrm{Beta}(9,5)$, und weil beide die Fläche $1$ haben, ist der Posterior genau $\mathrm{Beta}(9,5)$. Das Integral im Nenner muss man dafür gar nicht ausrechnen; nach [(6.2)](#gl-6-2) wäre es $P(\mathcal D)=6\cdot\frac{8!\,4!}{13!}=\frac6{6435}\approx0{,}000932$. Abb. [12](#abb-12) zeigt Prior, Likelihood und Posterior zusammen. Der Posterior liegt zwischen dem Prior, der $\tfrac12$ bevorzugt, und der Likelihood, deren Maximum bei $0{,}7$ liegt, und er ist schmaler als beide.

:::abbildung ml/k5posterior 12
Prior, Likelihood und Posterior für sieben Köpfe in zehn Würfen. Die Likelihood ist mit $1320$ multipliziert, damit sie wie eine Dichte die Fläche $1$ hat. Der Posterior ist Likelihood mal Prior, auf die Fläche $1$ gebracht. Gepunktet die Stellen $0{,}7$ (Maximum der Likelihood), $\tfrac23$ (Maximum des Posteriors) und $\tfrac9{14}\approx0{,}643$ (Erwartungswert des Posteriors).
:::

⁠**Kurz gesagt:** Der Posterior ist die Verteilung des Parameters nach den Daten; er ist proportional zu Likelihood mal Prior.

### Konjugierte Prior-Verteilungen

<span class="anker" id="stufe-6-6"></span>

Im Beispiel war der Prior eine Beta-Verteilung und der Posterior wieder eine. Das ist kein Zufall: Likelihood und Beta-Dichte bestehen aus denselben Bausteinen, und beim Multiplizieren addieren sich nur die Hochzahlen.

:::satz Satz 6.6 (Beta-Prior und Bernoulli-Daten)
<span class="anker" id="satz-6-6"></span>

Ist der Prior $\mathrm{Beta}(\alpha_1,\alpha_0)$ und enthalten die Daten $N_1$ Einsen und $N_0$ Nullen, so ist der Posterior

<span class="anker" id="gl-6-7"></span>
$$\mathrm{Beta}(\alpha_1+N_1,\ \alpha_0+N_0) . \tag{6.7}$$
:::

:::beweis Beta-Prior
Nach [(6.6)](#gl-6-6) und [(4.5)](die-likelihood.html#gl-4-5) ist $p(\theta\mid\mathcal D)\propto\theta^{N_1}(1-\theta)^{N_0}\cdot\theta^{\alpha_1-1}(1-\theta)^{\alpha_0-1}=\theta^{\alpha_1+N_1-1}(1-\theta)^{\alpha_0+N_0-1}$. Das ist bis auf den Faktor die Dichte von $\mathrm{Beta}(\alpha_1+N_1,\alpha_0+N_0)$, und zwei Dichten, die sich nur um einen festen Faktor unterscheiden und beide die Fläche $1$ haben, sind gleich.
:::

:::definition Definition 6.7 (Konjugierter Prior)
<span class="anker" id="satz-6-7"></span>

Ein Prior heißt __konjugiert__ zu einem Modell, wenn der Posterior aus derselben Familie von Verteilungen stammt wie der Prior.
:::

Die Beta-Verteilungen sind also konjugiert zum Bernoulli-Modell. Der Satz zeigt auch, wie man die Parameter des Priors deuten kann. Die Daten erhöhen $\alpha_1$ um die Zahl der Einsen und $\alpha_0$ um die Zahl der Nullen. Der Prior wirkt deshalb wie eine Anzahl gedachter Würfe, die man schon vor den echten gemacht hat; man spricht von __Pseudobeobachtungen__. Wie viele es genau sind, hängt davon ab, was man aus dem Posterior ausliest: Für den Erwartungswert zählen $\alpha_1$ und $\alpha_0$ als Einsen und Nullen, für den Modus $\alpha_1-1$ und $\alpha_0-1$.

⁠**Rechenbeispiel:** Man kann den Posterior Wurf für Wurf aktualisieren: Der Posterior nach einem Wurf ist der Prior für den nächsten. Für die Würfe $1,0,1,1,0,1,1,0,1,1$ mit dem Prior $\mathrm{Beta}(2,2)$ ergibt sich nacheinander

$$\begin{gathered} \mathrm{Beta}(3,2),\ \mathrm{Beta}(3,3),\ \mathrm{Beta}(4,3),\ \mathrm{Beta}(5,3),\ \mathrm{Beta}(5,4),\\ \mathrm{Beta}(6,4),\ \mathrm{Beta}(7,4),\ \mathrm{Beta}(7,5),\ \mathrm{Beta}(8,5),\ \mathrm{Beta}(9,5) . \end{gathered}$$

Nach dem ersten Wurf ist der Erwartungswert von $\tfrac24$ auf $\tfrac35$ gestiegen. Am Ende steht derselbe Posterior wie bei der Auswertung aller Würfe auf einmal, und die Reihenfolge der Würfe spielt keine Rolle.

⁠**Kurz gesagt:** Ein konjugierter Prior führt auf einen Posterior derselben Familie; beim Bernoulli-Modell zählt die Beta-Verteilung die Einsen und Nullen einfach weiter.

:::hintergrund Weitere konjugierte Paare
Zu vielen Modellen gibt es konjugierte Prior-Verteilungen. Für den Erwartungswert normalverteilter Daten mit bekannter Varianz ist es wieder eine Normalverteilung; Abschnitt [7](die-maximum-a-posteriori-schatzung.html#stufe-7) rechnet damit. Für die kategorische Verteilung mit $K$ Kategorien ist es eine Verallgemeinerung der Beta-Verteilung auf $K$ Wahrscheinlichkeiten, die Dirichlet-Verteilung, die ebenfalls die Beobachtungen jeder Kategorie zu ihrem Parameter addiert. Konjugierte Paare sind bequem, aber nicht nötig: Die Formel [(6.5)](#gl-6-5) gilt für jeden Prior. Ohne konjugierten Prior lässt sich nur das Integral $P(\mathcal D)$ meist nicht mehr von Hand ausrechnen.
:::

### Der Posterior-Mittelwert und die Laplace-Regel

<span class="anker" id="stufe-6-7"></span>

Der Posterior enthält alles, was man nach den Daten über $\theta$ weiß. Eine naheliegende Frage an ihn ist: Mit welcher Wahrscheinlichkeit zeigt der nächste Wurf Kopf?

:::satz Satz 6.8 (Vorhersage des nächsten Werts)
<span class="anker" id="satz-6-8"></span>

Sind die Würfe bei gegebenem $\theta$ unabhängig, so ist die Wahrscheinlichkeit, dass der nächste Wurf eine Eins ergibt, der Erwartungswert des Posteriors:

<span class="anker" id="gl-6-8"></span>
$$P(X_{N+1}=1\mid\mathcal D)=\int_0^1\theta\,p(\theta\mid\mathcal D)\,\mathrm{d}\theta=\mathbb{E}[\theta\mid\mathcal D] . \tag{6.8}$$

Beim Prior $\mathrm{Beta}(\alpha_1,\alpha_0)$ ist das

<span class="anker" id="gl-6-9"></span>
$$\mathbb{E}[\theta\mid\mathcal D]=\frac{\alpha_1+N_1}{\alpha_1+\alpha_0+N}=w\,\frac{\alpha_1}{\alpha_1+\alpha_0}+(1-w)\,\frac{N_1}N,\qquad w=\frac{\alpha_1+\alpha_0}{\alpha_1+\alpha_0+N} . \tag{6.9}$$
:::

:::herleitung Vorhersage
Man zerlegt nach dem unbekannten Wert von $\theta$, wie bei der totalen Wahrscheinlichkeit aus [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 3.4, mit einem Integral statt einer Summe. Bei gegebenem $\theta$ hat der nächste Wurf die Wahrscheinlichkeit $\theta$ für eine Eins, unabhängig von den bisherigen Würfen; das ist die bedingte Unabhängigkeit aus [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 5.4. Gewichtet mit dem Posterior ergibt das [(6.8)](#gl-6-8). Der Posterior ist nach [(6.7)](#gl-6-7) $\mathrm{Beta}(\alpha_1+N_1,\alpha_0+N_0)$, und [(6.4)](#gl-6-4) liefert den ersten Ausdruck in [(6.9)](#gl-6-9). Den zweiten rechnet man nach: $w\,\alpha_1/(\alpha_1+\alpha_0)=\alpha_1/(\alpha_1+\alpha_0+N)$ und $(1-w)\,N_1/N=N_1/(\alpha_1+\alpha_0+N)$.
:::

Der Posterior-Mittelwert ist also ein gewichtetes Mittel aus dem Erwartungswert des Priors und dem Maximum-Likelihood-Schätzer $N_1/N$. Das Gewicht $w$ des Priors ist der Anteil der Pseudobeobachtungen an allen Beobachtungen. Mit wachsendem $N$ geht es gegen null, und die Daten bestimmen das Ergebnis.

Mit dem gleichförmigen Prior $\mathrm{Beta}(1,1)$ entsteht die __Laplace-Regel__

<span class="anker" id="gl-6-10"></span>
$$P(X_{N+1}=1\mid\mathcal D)=\frac{N_1+1}{N+2} . \tag{6.10}$$

Sie wirkt so, als hätte man vor den Daten schon eine Eins und eine Null gesehen.

⁠**Rechenbeispiel:** Für die verbogene Münze mit dem Prior $\mathrm{Beta}(2,2)$ ist $\mathbb{E}[\theta\mid\mathcal D]=\frac{2+7}{4+10}=\frac9{14}\approx0{,}643$. Das Gewicht des Priors ist $w=\tfrac4{14}$, und tatsächlich ist $\tfrac4{14}\cdot\tfrac12+\tfrac{10}{14}\cdot0{,}7=\tfrac{2+7}{14}$. Mit der Laplace-Regel ist die Vorhersage $\frac8{12}=\frac23$. Bei drei Würfen mit dreimal Kopf liefert die Laplace-Regel $\frac45$ statt der $1$ des Maximum-Likelihood-Schätzers: Zahl bleibt möglich.

⁠**Kurz gesagt:** Der Erwartungswert des Posteriors ist die Wahrscheinlichkeit für eine Eins im nächsten Versuch; beim Beta-Prior ist er ein gewichtetes Mittel aus Prior-Erwartungswert und $N_1/N$, mit gleichförmigem Prior die Laplace-Regel $(N_1+1)/(N+2)$.

:::hintergrund Wird die Sonne morgen aufgehen?
Der französische Mathematiker Pierre-Simon Laplace hat die Regel im 18. Jahrhundert hergeleitet und in seinem „Philosophischen Versuch über die Wahrscheinlichkeiten“ von 1814 an einem berühmten Beispiel vorgeführt. Wer annimmt, die Sonne sei seit etwa $5000$ Jahren an jedem Tag aufgegangen, und sonst nichts über sie weiß, erhält nach [(6.10)](#gl-6-10) eine Chance von etwa $1{,}8$ Millionen zu eins, dass sie auch morgen aufgeht. Laplace fügte selbst hinzu, dass diese Zahl viel zu klein ist, denn man weiß über die Sonne weit mehr als die Liste der bisherigen Tage: Die Regel setzt voraus, dass man außer den Beobachtungen kein Vorwissen hat. Das Beispiel zeigt den Kern der bayesschen Rechnung. Das Ergebnis hängt vom Prior ab, und wer echtes Vorwissen hat, sollte es in den Prior schreiben.
:::

:::aufgabe Aufgabe 23 ★ Noch einmal die Münzkiste
<span class="anker" id="aufg-23"></span>

Mit einer Münze aus der Kiste von Unterabschnitt [6.1](#stufe-6-1) fällt viermal Kopf.

<ol class="al">

<li>

Berechne die Likelihood der drei Münzsorten und die Wahrscheinlichkeit der Daten.

</li>

<li>

Berechne die Wahrscheinlichkeiten der drei Sorten nach den Würfen. Welche Sorte ist jetzt am wahrscheinlichsten?

</li>

</ol>

:::loesung
(a) $\mathcal L(\theta)=\theta^4$: $\tfrac1{256}$, $\tfrac{16}{256}$, $\tfrac{81}{256}$. Mit den Anteilen $\tfrac14,\tfrac12,\tfrac14$ ist $P(\mathcal D)=\tfrac{1/4+8+81/4}{256}=\tfrac{28{,}5}{256}=\tfrac{57}{512}\approx0{,}111$.

(b) $\frac{1/1024}{57/512}=\tfrac1{114}\approx0{,}009$, $\frac{16/512}{57/512}=\tfrac{16}{57}\approx0{,}281$, $\frac{81/1024}{57/512}=\tfrac{81}{114}\approx0{,}711$. Jetzt ist die Münze mit $\theta=\tfrac34$ am wahrscheinlichsten: Vier Köpfe sprechen deutlich genug gegen eine faire Münze, um den doppelten Anteil fairer Münzen in der Kiste aufzuwiegen.
:::
:::

:::aufgabe Aufgabe 24 ★ Beta-Verteilungen
<span class="anker" id="aufg-24"></span>

<ol class="al">

<li>

Gib die Dichte von $\mathrm{Beta}(3,5)$ mit ausgerechnetem Vorfaktor an. Berechne Erwartungswert und Modus.

</li>

<li>

Welche Beta-Verteilung hat den Erwartungswert $0{,}5$ und den Modus $0{,}5$ und entspricht $18$ Pseudobeobachtungen im Sinn des Modus?

</li>

</ol>

:::loesung
(a) $B(3,5)=\frac{2!\,4!}{7!}=\frac{48}{5040}=\frac1{105}$, also $p(\theta)=105\,\theta^2(1-\theta)^4$. Erwartungswert $\tfrac38=0{,}375$, Modus $\tfrac26=\tfrac13$.

(b) Erwartungswert und Modus $\tfrac12$ verlangen $\alpha_1=\alpha_0$. Im Sinn des Modus zählen $\alpha_1-1$ und $\alpha_0-1$ als Pseudobeobachtungen, zusammen $18$, also $\alpha_1=\alpha_0=10$: $\mathrm{Beta}(10,10)$.
:::
:::

:::aufgabe Aufgabe 25 ★★ Wurf für Wurf
<span class="anker" id="aufg-25"></span>

Der Prior sei $\mathrm{Beta}(1,1)$, die Würfe ergeben nacheinander $1$, $1$, $0$.

<ol class="al">

<li>

Gib nach jedem Wurf den Posterior und die Vorhersage für den nächsten Wurf an.

</li>

<li>

Prüfe, dass die Auswertung aller drei Würfe auf einmal dasselbe ergibt, und dass die Reihenfolge $0$, $1$, $1$ ebenfalls dasselbe ergibt.

</li>

</ol>

:::loesung
(a) Nach der ersten $1$: $\mathrm{Beta}(2,1)$, Vorhersage $\tfrac23$. Nach der zweiten $1$: $\mathrm{Beta}(3,1)$, Vorhersage $\tfrac34$. Nach der $0$: $\mathrm{Beta}(3,2)$, Vorhersage $\tfrac35$.

(b) Alle drei Würfe auf einmal: $N_1=2$, $N_0=1$, also $\mathrm{Beta}(1+2,\,1+1)=\mathrm{Beta}(3,2)$. In der Reihenfolge $0,1,1$: $\mathrm{Beta}(1,2)$, $\mathrm{Beta}(2,2)$, $\mathrm{Beta}(3,2)$. Am Ende steht dasselbe, weil beim Multiplizieren die Reihenfolge der Faktoren keine Rolle spielt.
:::
:::

:::aufgabe Aufgabe 26 ★★ Wie stark wiegt der Prior?
<span class="anker" id="aufg-26"></span>

Die verbogene Münze zeigt siebenmal Kopf in zehn Würfen.

<ol class="al">

<li>

Berechne den Posterior-Mittelwert mit dem Prior $\mathrm{Beta}(5,5)$ und mit dem Prior $\mathrm{Beta}(50,50)$, jeweils mit dem Gewicht $w$ des Priors.

</li>

<li>

Wie viele Würfe braucht man beim Prior $\mathrm{Beta}(5,5)$ mindestens, damit das Gewicht des Priors höchstens $0{,}1$ ist?

</li>

<li>

Welcher der beiden Priors passt zu einer Münze aus dem Geldbeutel, welcher zu einer Münze, deren Rand man selbst verbogen hat?

</li>

</ol>

:::loesung
(a) Mit $\mathrm{Beta}(5,5)$: Posterior $\mathrm{Beta}(12,8)$, Mittelwert $\tfrac{12}{20}=0{,}6$, Gewicht $w=\tfrac{10}{20}=0{,}5$. Mit $\mathrm{Beta}(50,50)$: Posterior $\mathrm{Beta}(57,53)$, Mittelwert $\tfrac{57}{110}\approx0{,}518$, Gewicht $w=\tfrac{100}{110}\approx0{,}909$. Probe für den ersten Fall: $0{,}5\cdot0{,}5+0{,}5\cdot0{,}7=0{,}6$.

(b) $w=\frac{10}{10+N}\le0{,}1$ verlangt $N\ge90$.

(c) Eine Münze aus dem Geldbeutel ist mit großer Sicherheit fast fair; dazu passt der starke Prior $\mathrm{Beta}(50,50)$. Über eine selbst verbogene Münze weiß man wenig; dazu passt der schwache Prior $\mathrm{Beta}(5,5)$, der nur andeutet, dass sie wohl nicht extrem unfair ist.
:::
:::

:::aufgabe Aufgabe 27 ★★★ Zweimal Kopf
<span class="anker" id="aufg-27"></span>

Der Posterior sei $\mathrm{Beta}(\alpha_1',\alpha_0')$.

<ol class="al">

<li>

Zeige: Die Wahrscheinlichkeit, dass die nächsten beiden Würfe Kopf zeigen, ist $\mathbb{E}[\theta^2\mid\mathcal D]=\dfrac{\alpha_1'(\alpha_1'+1)}{(\alpha_1'+\alpha_0')(\alpha_1'+\alpha_0'+1)}$.

</li>

<li>

Berechne sie für $\mathrm{Beta}(9,5)$ und vergleiche mit dem Quadrat von $P(X_{N+1}=1\mid\mathcal D)$. Warum ist sie größer?

</li>

</ol>

:::loesung
(a) Bei gegebenem $\theta$ zeigen beide Würfe mit der Wahrscheinlichkeit $\theta^2$ Kopf. Zerlegt nach $\theta$ wie in der Herleitung zu [(6.8)](#gl-6-8) ist die Wahrscheinlichkeit $\mathbb{E}[\theta^2\mid\mathcal D]$. Nach [(6.2)](#gl-6-2) ist

$$\mathbb{E}[\theta^2\mid\mathcal D]=\frac{B(\alpha_1'+2,\alpha_0')}{B(\alpha_1',\alpha_0')}=\frac{(\alpha_1'+1)!\,(\alpha_1'+\alpha_0'-1)!}{(\alpha_1'-1)!\,(\alpha_1'+\alpha_0'+1)!}=\frac{\alpha_1'(\alpha_1'+1)}{(\alpha_1'+\alpha_0')(\alpha_1'+\alpha_0'+1)} .$$

(b) Für $\mathrm{Beta}(9,5)$: $\frac{9\cdot10}{14\cdot15}=\frac37\approx0{,}429$, das Quadrat der Einzelvorhersage ist $(\tfrac9{14})^2\approx0{,}413$. Nach der Verschiebungsformel ist $\mathbb{E}[\theta^2]=\mathbb{E}[\theta]^2+\operatorname{Var}(\theta)$, und die Varianz des Posteriors ist positiv. Anschaulich: Zeigt der erste der beiden Würfe Kopf, so spricht das für ein größeres $\theta$ und macht den zweiten Kopf wahrscheinlicher; die beiden Würfe sind ohne Kenntnis von $\theta$ nicht unabhängig.
:::
:::
