---
title: Schätzen aus einer Stichprobe
pfad: Informatik / Machine Learning / Statistik und Information
order: 6250200
summary: Daten sind nur ein Ausschnitt dessen, was hätte geschehen können.
tags: Statistik, statistisches Modell, Parameter, Parameterbereich, Datensatz, Schätzer, Schätzwert, Stichprobenverteilung
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Daten sind nur ein Ausschnitt dessen, was hätte geschehen können. Dieser Abschnitt legt fest, was es heißt, aus Daten eine unbekannte Größe zu schätzen, und zeigt, dass jede Schätzung selbst eine Zufallsvariable ist: Mit anderen Daten käme ein anderer Wert heraus.
:::

### Wahrscheinlichkeitsrechnung und Statistik

<span class="anker" id="stufe-1-1"></span>

[Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html) hat in eine Richtung gerechnet: Die Verteilung war gegeben, gefragt waren Wahrscheinlichkeiten für Daten. Wirft man eine Münze, die mit der Wahrscheinlichkeit $\theta=0{,}7$ Kopf zeigt, zehnmal, so ist die Anzahl der Köpfe nach [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 8.3, binomialverteilt, und genau sieben Köpfe kommen mit der Wahrscheinlichkeit $\binom{10}7\,0{,}7^7\,0{,}3^3\approx0{,}267$ vor. Dieses Kapitel rechnet in die Gegenrichtung (Abb. [1](#abb-1)). Gegeben sind zehn Würfe einer Münze mit verbogenem Rand, siebenmal Kopf, und gefragt ist, welches $\theta$ diese Münze hat. Ein solcher Schluss von beobachteten Daten auf die Verteilung, die sie erzeugt hat, heißt __Statistik__.

:::abbildung ml/k5richtung 1
Zwei Richtungen. Die Wahrscheinlichkeitsrechnung geht von einer bekannten Verteilung zu den Wahrscheinlichkeiten möglicher Daten. Die Statistik geht von beobachteten Daten zurück zu der unbekannten Verteilung, die sie erzeugt hat.
:::

Die Gegenrichtung ist schwerer, weil sie keine eindeutige Antwort hat. Siebenmal Kopf in zehn Würfen kann von einer fairen Münze stammen, ebenso von einer Münze mit $\theta=0{,}8$. Man kann nur sagen, welche Werte von $\theta$ besser und welche schlechter zu den Daten passen. Damit das eine überschaubare Frage wird, legt man vorher fest, unter welchen Verteilungen man sucht.

:::definition Definition 1.1 (Statistisches Modell)
<span class="anker" id="satz-1-1"></span>

Eine Familie von Verteilungen $P(X=x\mid\theta)$, die von einer unbekannten Größe $\theta$ abhängen, heißt __statistisches Modell__. Die Größe $\theta$ heißt __Parameter__, die Menge ihrer zulässigen Werte __Parameterbereich__ $\Theta$. Bei stetigen Daten tritt an die Stelle von $P(X=x\mid\theta)$ eine Dichte $p(x\mid\theta)$.
:::

Der senkrechte Strich wird wie in [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 3.2, „gegeben“ gelesen: $P(X=x\mid\theta)$ ist die Wahrscheinlichkeit von $X=x$, wenn der Parameter den Wert $\theta$ hat. Ob $\theta$ dabei selbst zufällig ist, lässt die Schreibweise offen; Abschnitt [6](prior-und-posterior.html#stufe-6) kommt darauf zurück. Besteht der Parameter aus mehreren Zahlen, schreibt man ihn als Vektor $\boldsymbol{\theta}$. In den Definitionen steht $\theta$ für einen beliebigen Parameter; in den Rechenbeispielen ist $\theta$ ohne weiteren Zusatz der Parameter einer Bernoulli-Verteilung, wie in [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 8.1.

⁠**Rechenbeispiel:** Für Münzwürfe mit Kopf $=1$ und Zahl $=0$ ist das Bernoulli-Modell

$$P(X=x\mid\theta)=\theta^x(1-\theta)^{1-x},\qquad x\in\{0,1\},\qquad \Theta=[0,\,1] .$$

Für Messwerte einer Spannung mit Rauschen ist ein übliches Modell die Normalverteilung aus [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 8.5, mit der Dichte $p(x\mid\mu,\sigma^2)$ und dem Parametervektor $\boldsymbol{\theta}=(\mu,\,\sigma^2)^{\top}$. Hier ist $\mu$ der wahre Wert der Spannung, $\sigma^2$ die Varianz des Rauschens und der Parameterbereich die Menge aller Paare mit $\sigma^2>0$.

⁠**Kurz gesagt:** Die Statistik schließt von Daten auf die Verteilung, die sie erzeugt hat; dafür beschränkt man sich auf ein Modell, eine Familie von Verteilungen mit einem unbekannten Parameter.

:::hintergrund Warum man sich auf ein Modell beschränkt
Ohne Modell müsste man aus zehn Würfen auf die ganze Verteilung schließen, die hinter einer Münze steht, und aus vier Messwerten auf eine beliebige Dichte über allen reellen Zahlen. Das ist hoffnungslos: Zu wenigen Daten passen unüberschaubar viele Verteilungen. Ein Modell schrumpft die Frage auf wenige Zahlen. Bei der Münze ist das eine Annahme, die man kaum bezweifeln kann, denn ein Ja-Nein-Ergebnis ist immer Bernoulli-verteilt. Bei der Spannung ist die Normalverteilung eine echte Annahme, begründet durch den zentralen Grenzwertsatz aus [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 13.4. Abschnitt [10](die-grote-entropie.html#stufe-10) liefert einen zweiten Grund. Ist das Modell falsch, so beantwortet die Statistik eine falsche Frage, und das sieht man den Zahlen nicht an. Jede Schätzung in diesem Kapitel gilt deshalb unter der Voraussetzung, dass das gewählte Modell die Daten richtig beschreibt.
:::

### Rückblick: Die Stichprobe

<span class="anker" id="stufe-1-2"></span>

Nach [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 9.6, fasst man einen Datensatz als Stichprobe auf: Die Werte $x_1,\dots,x_N$ sind Ergebnisse von $N$ Zufallsvariablen $X_1,\dots,X_N$, die unabhängig sind und alle dieselbe Verteilung haben, kurz i.i.d. Dieses Kapitel schreibt die Anzahl der Werte mit $N$, wie die Zahl der Beispiele in [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html); [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html) hat für dieselbe Rolle $n$ benutzt. Große Buchstaben stehen wie in [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html) für die Zufallsvariablen, kleine für die beobachteten Werte. Die beobachteten Werte zusammen heißen der __Datensatz__ $\mathcal D=(x_1,\dots,x_N)$.

Weil die Zufallsvariablen unabhängig sind, ist die Wahrscheinlichkeit eines ganzen Datensatzes nach [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 9.5, das Produkt der einzelnen Wahrscheinlichkeiten:

<span class="anker" id="gl-1-1"></span>
$$P(X_1=x_1,\dots,X_N=x_N\mid\theta)=\prod_{i=1}^NP(X=x_i\mid\theta) . \tag{1.1}$$

Dabei ist $\prod_{i=1}^N$ das Produktzeichen: Es multipliziert die Faktoren für $i=1$ bis $N$, so wie das Summenzeichen sie addiert.

⁠**Rechenbeispiel:** Die verbogene Münze aus dem vorigen Unterabschnitt hat in zehn Würfen die Folge

$$\mathcal D=(1,\,0,\,1,\,1,\,0,\,1,\,1,\,0,\,1,\,1)$$

ergeben, also siebenmal Kopf. Hätte sie $\theta=0{,}7$, so hätte genau diese Folge nach [(1.1)](#gl-1-1) die Wahrscheinlichkeit $0{,}7\cdot0{,}3\cdot0{,}7\cdot0{,}7\cdot0{,}3\cdot0{,}7\cdot0{,}7\cdot0{,}3\cdot0{,}7\cdot0{,}7=0{,}7^7\cdot0{,}3^3\approx0{,}00222$. Die Wahrscheinlichkeit $0{,}267$ aus dem vorigen Unterabschnitt ist $120$-mal so groß, weil es $\binom{10}7=120$ Folgen mit sieben Köpfen gibt.

⁠**Kurz gesagt:** Ein Datensatz ist eine Stichprobe aus $N$ unabhängigen, gleich verteilten Zufallsvariablen; seine Wahrscheinlichkeit ist das Produkt der Einzelwahrscheinlichkeiten.

### Schätzer

<span class="anker" id="stufe-1-3"></span>

Wer $\theta$ wissen will, braucht ein Rezept, das aus den Daten eine Zahl macht. Ein naheliegendes Rezept für die Münze ist der Anteil der Köpfe, $7/10$. Aber auch andere Rezepte sind denkbar, und zunächst ist keines verboten.

:::definition Definition 1.2 (Schätzer, Schätzwert)
<span class="anker" id="satz-1-2"></span>

Ein __Schätzer__ für einen Parameter $\theta$ ist eine Vorschrift $g$, die jeder möglichen Stichprobe eine Zahl zuordnet:

<span class="anker" id="gl-1-2"></span>
$$\hat\theta=g(X_1,\dots,X_N) . \tag{1.2}$$

Setzt man die beobachteten Werte ein, so heißt die Zahl $g(x_1,\dots,x_N)$ der __Schätzwert__.
:::

Der Hut über dem Buchstaben bedeutet wie bei der Vorhersage $\hat y$ aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 2.2, eine aus Daten berechnete Größe. Viele Texte schreiben für den Schätzer und für den Schätzwert dasselbe Zeichen $\hat\theta$; ob die Vorschrift mit zufälligen $X_i$ oder die Zahl aus den beobachteten $x_i$ gemeint ist, sagt der Zusammenhang. Die Definition verlangt nicht, dass der Schätzer in der Nähe von $\theta$ landet. Wie gut er das tut, ist eine eigene Frage, und Abschnitt [2](wie-gut-ist-ein-schatzer.html#stufe-2) misst es.

Für Daten aus Nullen und Einsen bezeichnet dieses Kapitel die Anzahl der Einsen mit $N_1=\sum_ix_i$ und die Anzahl der Nullen mit $N_0=N-N_1$.

⁠**Rechenbeispiel:** Für die zehn Würfe mit $N_1=7$ liefern vier verschiedene Schätzer für $\theta$:

<ul>

<li>

den Anteil der Köpfe $N_1/N=7/10=0{,}7$;

</li>

<li>

den ersten Wurf $x_1=1$;

</li>

<li>

die feste Zahl $0{,}5$, gleichgültig, was die Daten sagen;

</li>

<li>

den Bruch $(N_1+1)/(N+2)=8/12\approx0{,}667$.

</li>

</ul>

Alle vier sind Schätzer im Sinn der Definition. Der zweite und der dritte wirken unvernünftig, und der vierte hat noch keine Begründung; die Abschnitte [2](wie-gut-ist-ein-schatzer.html#stufe-2) und [6](prior-und-posterior.html#stufe-6) kommen auf sie zurück.

⁠**Kurz gesagt:** Ein Schätzer ist eine Vorschrift, die aus den Daten eine Zahl für einen unbekannten Parameter macht; der Schätzwert ist diese Zahl für die beobachteten Daten.

### Die Stichprobenverteilung

<span class="anker" id="stufe-1-4"></span>

Hätte man die Münze ein zweites Mal zehnmal geworfen, so wären vielleicht sechs oder acht Köpfe herausgekommen, und der Anteil der Köpfe hätte einen anderen Wert gehabt. Ein Schätzer hängt von zufälligen Daten ab und ist deshalb selbst eine Zufallsvariable. Man stellt sich vor, das ganze Experiment würde sehr oft wiederholt, jedes Mal mit $N$ neuen Werten, und notiert jedes Mal den Wert des Schätzers. Wie diese Werte verteilt sind, entscheidet über die Güte des Schätzers.

:::definition Definition 1.3 (Stichprobenverteilung)
<span class="anker" id="satz-1-3"></span>

Die Verteilung eines Schätzers $\hat\theta=g(X_1,\dots,X_N)$ heißt seine __Stichprobenverteilung__.
:::

Sie hängt vom wahren Parameter ab, von der Vorschrift $g$ und von der Zahl $N$ der Werte. Der wahre Parameter ist dabei fest; zufällig sind nur die Daten.

⁠**Rechenbeispiel:** Eine Zufallsvariable $X$ nehme die Werte $1$, $2$ und $3$ je mit der Wahrscheinlichkeit $\tfrac13$ an; man kann sich einen Würfel vorstellen, dessen Seiten die Zahlen $1,1,2,2,3,3$ tragen. Ihr Erwartungswert ist $\mu=2$, ihre Varianz $\sigma^2=\tfrac13(1+0+1)=\tfrac23$. Aus ihr wird eine Stichprobe vom Umfang $N=2$ gezogen, und geschätzt wird $\mu$ mit dem Mittelwert $\bar X=\tfrac12(X_1+X_2)$. Es gibt nur $3\cdot3=9$ mögliche Stichproben, und wegen der Unabhängigkeit hat jede die Wahrscheinlichkeit $\tfrac13\cdot\tfrac13=\tfrac19$. Tabelle [1](#tab-1) zählt sie alle auf.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Alle neun Stichproben vom Umfang $2$ aus den Werten $1$, $2$, $3$, jede mit der Wahrscheinlichkeit $\tfrac19$, und ihr Mittelwert $\bar x$.

| Stichprobe $(x_1,x_2)$ | $(1,1)$ | $(1,2)$ | $(1,3)$ | $(2,1)$ | $(2,2)$ | $(2,3)$ | $(3,1)$ | $(3,2)$ | $(3,3)$ |
|---|---|---|---|---|---|---|---|---|---|
| Mittelwert $\bar x$ | $1$ | $1{,}5$ | $2$ | $1{,}5$ | $2$ | $2{,}5$ | $2$ | $2{,}5$ | $3$ |

Zählt man ab, wie oft jeder Mittelwert vorkommt, erhält man die Stichprobenverteilung von $\bar X$: die Werte $1$; $1{,}5$; $2$; $2{,}5$; $3$ mit den Wahrscheinlichkeiten $\tfrac19,\tfrac29,\tfrac39,\tfrac29,\tfrac19$ (Abb. [2](#abb-2)). Ihr Erwartungswert und ihre Varianz sind nach [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 7.1 und 7.4, Summen über diese fünf Werte (Abb. [3](#abb-3)):

$$\mathbb{E}[\bar X]=2,\qquad \operatorname{Var}(\bar X)=\tfrac13 .$$

Das passt zu [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 13.1: Der Mittelwert hat den Erwartungswert $\mu=2$ und die Varianz $\sigma^2/N=\tfrac23/2=\tfrac13$.

:::abbildung ml/k5stichprobe 2
(a) Die Verteilung einer Zufallsvariablen mit den Werten $1$, $2$, $3$ je mit der Wahrscheinlichkeit $\tfrac13$. (b) Die Stichprobenverteilung des Mittelwerts $\bar X$ aus zwei unabhängigen solchen Werten. Sie hat denselben Erwartungswert $2$, aber nur die halbe Varianz, und ist um die Mitte zusammengezogen.
:::

:::abbildung ml/k5rerwartung 3
Erwartungswert und Varianz des Schätzers $\bar X$ als Summen über seine Stichprobenverteilung: jeder mögliche Wert, gewichtet mit seiner Wahrscheinlichkeit.
:::

⁠**Kurz gesagt:** Ein Schätzer ist eine Zufallsvariable; seine Verteilung über alle möglichen Stichproben heißt Stichprobenverteilung, und an ihr misst man, wie gut er ist.

:::hintergrund Die Stichprobenverteilung sieht man nie
In der Praxis hat man genau einen Datensatz und damit genau einen Wert des Schätzers. Die Stichprobenverteilung beschreibt gedachte Wiederholungen, die nie stattfinden. Trotzdem lässt sich über sie viel sagen: In kleinen Beispielen zählt man wie oben alle Stichproben ab; für Mittelwerte liefern [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 13.1, und der zentrale Grenzwertsatz ihre Varianz und ihre Form; und mit einem Rechner kann man sehr viele Datensätze aus einem angenommenen Modell erzeugen und die Werte des Schätzers auszählen. In dieser Sichtweise ist der Parameter eine feste, unbekannte Zahl, und alle Wahrscheinlichkeiten beziehen sich auf die Daten. Sie heißt __frequentistisch__, weil sie Wahrscheinlichkeiten als Häufigkeiten bei Wiederholungen deutet, wie [Teil 4](/wissen/informatik/machine-learning/wahrscheinlichkeit/wahrscheinlichkeit.html), Abschnitt 2.1. Abschnitt [6](prior-und-posterior.html#stufe-6) stellt ihr eine zweite Sichtweise gegenüber.
:::

:::aufgabe Aufgabe 1 ★ Modelle und Schätzer
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Eine Reißzwecke landet entweder auf dem Rücken oder auf der Seite. Gib ein statistisches Modell für einen Wurf an. Was ist der Parameter, was der Parameterbereich?

</li>

<li>

Acht Würfe ergeben $\mathcal D=(1,\,0,\,1,\,1,\,0,\,1,\,1,\,0)$, dabei steht $1$ für „Rücken“. Berechne die vier Schätzwerte aus dem Rechenbeispiel in Unterabschnitt [1.3](#stufe-1-3).

</li>

<li>

Wie wahrscheinlich ist genau diese Folge, wenn der Parameter $0{,}5$ ist? Wie wahrscheinlich, wenn er $0{,}6$ ist?

</li>

</ol>

:::loesung
(a) Ein Wurf hat zwei Ausgänge, also ist er Bernoulli-verteilt: $P(X=x\mid\theta)=\theta^x(1-\theta)^{1-x}$ für $x\in\{0,1\}$, mit $x=1$ für „Rücken“. Der Parameter $\theta$ ist die Wahrscheinlichkeit, auf dem Rücken zu landen, der Parameterbereich ist $\Theta=[0,\,1]$. Anders als bei einer Münze gibt es keinen Grund, $\theta=\tfrac12$ zu erwarten; die Form der Zwecke bestimmt $\theta$.

(b) Es ist $N=8$ und $N_1=5$. Die vier Schätzwerte sind $N_1/N=5/8=0{,}625$, der erste Wurf $x_1=1$, die feste Zahl $0{,}5$ und $(N_1+1)/(N+2)=6/10=0{,}6$.

(c) Unter $\theta$ hat die Folge die Wahrscheinlichkeit $\theta^5(1-\theta)^3$. Für $\theta=0{,}5$ ist das $0{,}5^8=\tfrac1{256}\approx0{,}00391$, für $\theta=0{,}6$ ist es $0{,}6^5\cdot0{,}4^3\approx0{,}07776\cdot0{,}064\approx0{,}00498$.
:::
:::

:::aufgabe Aufgabe 2 ★★ Eine Stichprobenverteilung abzählen
<span class="anker" id="aufg-2"></span>

Eine faire Münze ($\theta=\tfrac12$) wird dreimal geworfen, und $\theta$ wird mit dem Anteil der Köpfe $\hat\theta=N_1/3$ geschätzt.

<ol class="al">

<li>

Schreibe alle acht möglichen Folgen auf und gib die Stichprobenverteilung von $\hat\theta$ an.

</li>

<li>

Berechne $\mathbb{E}[\hat\theta]$ und $\operatorname{Var}(\hat\theta)$ und vergleiche mit $\theta$ und mit $\theta(1-\theta)/N$.

</li>

<li>

Wie wahrscheinlich ist es, dass der Schätzwert um mindestens $0{,}3$ neben $\theta$ liegt?

</li>

</ol>

:::loesung
(a) Die acht Folgen sind $000$, $001$, $010$, $100$, $011$, $101$, $110$, $111$, jede mit der Wahrscheinlichkeit $\tfrac18$. Der Anteil der Köpfe ist $0$ für eine Folge, $\tfrac13$ für drei, $\tfrac23$ für drei und $1$ für eine. Die Stichprobenverteilung von $\hat\theta$ hat also die Werte $0,\tfrac13,\tfrac23,1$ mit den Wahrscheinlichkeiten $\tfrac18,\tfrac38,\tfrac38,\tfrac18$.

(b) $\mathbb{E}[\hat\theta]=\tfrac18\,(0+3\cdot\tfrac13+3\cdot\tfrac23+1)=\tfrac18\cdot4=\tfrac12=\theta$. Weiter ist $\mathbb{E}[\hat\theta^2]=\tfrac18\,(0+3\cdot\tfrac19+3\cdot\tfrac49+1)=\tfrac18\cdot\tfrac83=\tfrac13$, also $\operatorname{Var}(\hat\theta)=\tfrac13-\tfrac14=\tfrac1{12}$. Das ist $\theta(1-\theta)/N=\tfrac14/3=\tfrac1{12}$.

(c) Die Werte $\tfrac13$ und $\tfrac23$ liegen nur $\tfrac16\approx0{,}167$ neben $\tfrac12$, die Werte $0$ und $1$ liegen $0{,}5$ daneben. Die Wahrscheinlichkeit ist also $\tfrac18+\tfrac18=\tfrac14$.
:::
:::
