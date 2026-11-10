---
title: Die Likelihood
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Statistik und Information
adresse: informatik/machine-learning/mathematische-grundlagen/statistik-und-information
knoten: Kapitel 5: Statistik und Information
nachschlagen: ja
order: 15250500
summary: Bisher wurden Schätzer vorgegeben und dann geprüft.
tags: streng monoton wachsend, Likelihood, suffiziente Statistik, Log-Likelihood
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Bisher wurden Schätzer vorgegeben und dann geprüft. Dieser Abschnitt dreht die Frage um und bewertet jeden möglichen Wert des Parameters danach, wie wahrscheinlich er die tatsächlich beobachteten Daten macht. Diese Bewertung heißt Likelihood; ihr Logarithmus lässt sich leichter berechnen und ableiten.
:::

### Was du dafür brauchst: Logarithmen

<span class="anker" id="stufe-4-1"></span>

Wahrscheinlichkeiten von Datensätzen sind Produkte vieler Faktoren. Der Logarithmus macht aus Produkten Summen. Dieser Unterabschnitt stellt zusammen, was das Kapitel über ihn benutzt.

**Der natürliche Logarithmus.** Für $x>0$ ist $\ln x$ die Zahl, für die $\mathrm{e}^{\ln x}=x$ ist. Er macht die e-Funktion rückgängig, und nach [Kapitel 3, Abschnitt 1.4](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/die-ableitung.html#stufe-1-4), hat er die Ableitung $1/x$. Weil diese Ableitung für alle $x>0$ positiv ist, ist $\ln$ __streng monoton wachsend__: Aus $a<b$ folgt $\ln a<\ln b$. Es ist $\ln1=0$; für Zahlen zwischen $0$ und $1$ ist der Logarithmus negativ, und für $x\to0$ fällt er unter jede Schranke.

**Rechenregeln.** Aus $\mathrm{e}^{a+b}=\mathrm{e}^a\,\mathrm{e}^b$ folgen für $a,b>0$ und jede reelle Zahl $k$

<span class="anker" id="gl-4-1"></span>
$$\ln(ab)=\ln a+\ln b,\qquad \ln\frac ab=\ln a-\ln b,\qquad \ln(a^k)=k\ln a . \tag{4.1}$$

Insbesondere ist $\ln\frac1a=-\ln a$.

**Der Logarithmus zur Basis 2.** Für $x>0$ ist $\log_2x$ die Zahl, für die $2^{\log_2x}=x$ ist. Es ist $\log_22=1$, $\log_28=3$ und $\log_2\frac18=-3$. Wegen $2=\mathrm{e}^{\ln2}$ ist $x=2^{\log_2x}=\mathrm{e}^{\ln2\cdot\log_2x}$, also

<span class="anker" id="gl-4-2"></span>
$$\log_2x=\frac{\ln x}{\ln2},\qquad \ln2\approx0{,}6931 . \tag{4.2}$$

Für $\log_2$ gelten dieselben Rechenregeln [(4.1)](#gl-4-1). Dieses Kapitel schreibt immer $\ln$ oder $\log_2$, nie $\log$ ohne Basis.

::::beispiel [Rechenbeispiel]
Mit den Rechenregeln ist

$$\ln\bigl(0{,}7^7\cdot0{,}3^3\bigr)=7\ln0{,}7+3\ln0{,}3\approx7\cdot(-0{,}3567)+3\cdot(-1{,}2040)\approx-6{,}109 .$$

Zur Probe: $0{,}7^7\cdot0{,}3^3\approx0{,}0022236$, und der Taschenrechner liefert $\ln0{,}0022236\approx-6{,}109$. Ferner ist $\log_2\frac1{1024}=-10$, denn $2^{10}=1024$, und $\log_23=\ln3/\ln2\approx1{,}0986/0{,}6931\approx1{,}585$.
::::

⁠**Kurz gesagt:** Der Logarithmus macht Produkte zu Summen und Potenzen zu Vielfachen, er wächst streng monoton, und $\log_2x=\ln x/\ln2$.

### Die Likelihood

<span class="anker" id="stufe-4-2"></span>

Bei der verbogenen Münze liegen die Daten fest: die Folge $\mathcal D=(1,0,1,1,0,1,1,0,1,1)$ mit sieben Köpfen. Für jeden denkbaren Wert von $\theta$ kann man ausrechnen, wie wahrscheinlich genau diese Folge gewesen wäre. Nach Unterabschnitt [1.2](schatzen-aus-einer-stichprobe.html#stufe-1-2) ist das $\theta^7(1-\theta)^3$. Für $\theta=0{,}5$ ergibt sich $0{,}5^{10}\approx0{,}000977$, für $\theta=0{,}7$ ergibt sich $0{,}00222$. Der Wert $0{,}7$ macht die beobachteten Würfe also etwa $2{,}3$-mal so wahrscheinlich wie der Wert $0{,}5$ und passt in diesem Sinn besser zu ihnen. Diese Zahl, als Funktion von $\theta$ gelesen, bekommt einen eigenen Namen.

:::definition Definition 4.1 (Likelihood)
<span class="anker" id="satz-4-1"></span>

Es sei $\mathcal D$ ein beobachteter Datensatz und $P(\mathcal D\mid\theta)$ seine Wahrscheinlichkeit im Modell. Bei festen Daten, als Funktion des Parameters gelesen, heißt

<span class="anker" id="gl-4-3"></span>
$$\mathcal L(\theta)=P(\mathcal D\mid\theta) \tag{4.3}$$

die __Likelihood__ von $\theta$. Bei stetigen Daten steht an der Stelle von $P(\mathcal D\mid\theta)$ die gemeinsame Dichte der Daten.
:::

Das englische Wort *likelihood* bedeutet etwa Plausibilität; es wird im Deutschen meist unübersetzt benutzt. Dieselbe Formel $P(\mathcal D\mid\theta)$ hat also zwei Lesarten. Hält man $\theta$ fest und lässt die Daten variieren, ist sie eine Wahrscheinlichkeitsverteilung über die Daten, wie in [Kapitel 4](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wahrscheinlichkeit.html). Hält man die Daten fest und lässt $\theta$ variieren, ist sie die Likelihood. Abb. [7](#abb-7) (a) zeigt die Likelihood der zehn Würfe.

:::abbildung ml/k5likelihood 7
(a) Die Likelihood der zehn Würfe mit sieben Köpfen als Funktion von $\theta$. Sie ist bei $\theta=0{,}7$ am größten (rot), mit dem Wert $0{,}00222$; bei $\theta=0{,}5$ (grau) ist sie $0{,}000977$. Für $\theta=0$ und $\theta=1$ ist sie null, denn dann wären Zahl beziehungsweise Kopf unmöglich. (b) Ihr Logarithmus. Er hat sein Maximum an derselben Stelle, mit dem Wert $-6{,}109$.
:::

:::warnung Die Likelihood ist keine Verteilung über $\theta$
Die Likelihood sagt nicht, wie wahrscheinlich ein Wert von $\theta$ ist. Sie ist die Wahrscheinlichkeit der Daten unter diesem Wert. Man spricht deshalb von der Likelihood des Parameters, nie von der Likelihood der Daten. Insbesondere hat die Fläche unter ihrer Kurve keine Bedeutung und ist nicht $1$: Mit $(1-\theta)^3=1-3\theta+3\theta^2-\theta^3$ ist

$$\int_0^1\theta^7(1-\theta)^3\,\mathrm{d}\theta=\frac18-\frac39+\frac3{10}-\frac1{11}=\frac{495-1320+1188-360}{3960}=\frac1{1320} .$$

Wie man aus Daten tatsächlich eine Verteilung über $\theta$ gewinnt, zeigt Abschnitt [6](prior-und-posterior.html#stufe-6).
:::

::::beispiel [Rechenbeispiel]
Für die zehn Würfe ist $\mathcal L(0{,}5)\approx0{,}000977$, $\mathcal L(0{,}6)\approx0{,}00179$, $\mathcal L(0{,}7)\approx0{,}00222$ und $\mathcal L(0{,}8)\approx0{,}00168$. Am Verhältnis zweier Werte liest man ab, wie viel besser der eine Parameterwert die Daten erklärt als der andere: $\mathcal L(0{,}7)/\mathcal L(0{,}5)\approx2{,}28$.
::::

⁠**Kurz gesagt:** Die Likelihood ist die Wahrscheinlichkeit der beobachteten Daten, gelesen als Funktion des Parameters; sie bewertet Parameterwerte, ist aber keine Verteilung über sie.

:::hintergrund Herkunft des Begriffs
Das Verfahren, den Parameter mit der größten Wahrscheinlichkeit der Daten zu wählen, stellte der englische Statistiker Ronald A. Fisher 1912 als Rechenvorschrift vor. 1921 prägte er dafür den Begriff *likelihood* und grenzte ihn ausdrücklich von der Wahrscheinlichkeit ab: Von der Likelihood einer beobachtbaren Größe zu sprechen, habe keinen Sinn, und anders als eine Dichte lasse sich die Likelihood nicht sinnvoll integrieren. 1922 folgte die systematische Darstellung als Methode der maximalen Likelihood. Fisher wollte damit Schlüsse auf Parameter ziehen, ohne eine Verteilung für den Parameter annehmen zu müssen, wie sie Abschnitt [6](prior-und-posterior.html#stufe-6) braucht.
:::

### Die Likelihood einer Stichprobe

<span class="anker" id="stufe-4-3"></span>

Für eine i.i.d. Stichprobe zerfällt die Wahrscheinlichkeit des Datensatzes nach [(1.1)](schatzen-aus-einer-stichprobe.html#gl-1-1) in ein Produkt. Also zerfällt auch die Likelihood.

:::satz Satz 4.2 (Likelihood einer Stichprobe)
<span class="anker" id="satz-4-2"></span>

Für eine Stichprobe $x_1,\dots,x_N$ aus einem Modell mit den Wahrscheinlichkeiten $P(X=x\mid\theta)$ ist

<span class="anker" id="gl-4-4"></span>
$$\mathcal L(\theta)=\prod_{i=1}^NP(X=x_i\mid\theta) . \tag{4.4}$$

Bei stetigen Daten mit der Dichte $p(x\mid\theta)$ ist $\mathcal L(\theta)=\prod_{i=1}^Np(x_i\mid\theta)$.
:::

Für das Bernoulli-Modell ist jeder Faktor $\theta^{x_i}(1-\theta)^{1-x_i}$. Multipliziert man sie, addieren sich die Hochzahlen: Die Hochzahlen von $\theta$ ergeben zusammen $N_1$, die von $1-\theta$ ergeben $N_0$. Also ist

<span class="anker" id="gl-4-5"></span>
$$\mathcal L(\theta)=\theta^{N_1}(1-\theta)^{N_0} . \tag{4.5}$$

Die Likelihood hängt nur von der Anzahl der Einsen ab, nicht von ihrer Reihenfolge.

::::beispiel [Rechenbeispiel]
Für die zehn Würfe und $\theta=0{,}7$ hat jede $1$ den Faktor $0{,}7$ und jede $0$ den Faktor $0{,}3$. Abb. [8](#abb-8) multipliziert die zehn Faktoren.

:::abbildung ml/k5rprodukt 8
Die Likelihood von $\theta=0{,}7$ für die Würfe $\mathcal D=(1,0,1,1,0,1,1,0,1,1)$ als Produkt: ein Faktor je Wurf, $0{,}7$ für Kopf und $0{,}3$ für Zahl.
:::
::::

Bei stetigen Daten sind die Faktoren Dichtewerte, keine Wahrscheinlichkeiten. Das ändert am Vergleich zweier Parameterwerte nichts. Nach [Kapitel 4, Abschnitt 6.4](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/zufallsvariablen-und-verteilungen.html#stufe-6-4), ist die Wahrscheinlichkeit, dass ein Wert in ein kurzes Intervall der Länge $\Delta$ um $x_i$ fällt, etwa $p(x_i\mid\theta)\,\Delta$. Die Wahrscheinlichkeit, dass alle $N$ Werte in ihre Intervalle fallen, ist dann etwa $\mathcal L(\theta)\,\Delta^N$. Der Faktor $\Delta^N$ hängt nicht von $\theta$ ab und ändert nicht, welcher Parameterwert die Daten wahrscheinlicher macht.

⁠**Kurz gesagt:** Für eine i.i.d. Stichprobe ist die Likelihood das Produkt der Wahrscheinlichkeiten oder Dichten der einzelnen Werte; im Bernoulli-Modell ist sie $\theta^{N_1}(1-\theta)^{N_0}$.

:::hintergrund Was die Daten über $\theta$ verraten
Im Bernoulli-Modell geht der ganze Datensatz nur über die eine Zahl $N_1$ in die Likelihood ein. Zwei Datensätze mit gleich vielen Einsen ergeben dieselbe Likelihood, gleich in welcher Reihenfolge die Einsen kommen. Was immer man aus der Likelihood über $\theta$ schließt, hängt also nur von $N_1$ ab. Eine Größe mit dieser Eigenschaft heißt __suffiziente Statistik__: Sie fasst alles zusammen, was die Daten über den Parameter sagen. Beim Normalverteilungsmodell sind es, wie Unterabschnitt [5.3](die-maximum-likelihood-schatzung.html#stufe-5-3) zeigt, der Mittelwert und die Quadratsumme der Abweichungen vom Mittelwert. Die Reihenfolge kann trotzdem etwas verraten, nämlich dass das Modell falsch ist: Kommen alle Einsen am Anfang und alle Nullen am Ende, so passt die Annahme unabhängiger, gleich verteilter Würfe schlecht.
:::

### Die Log-Likelihood

<span class="anker" id="stufe-4-4"></span>

Ein Produkt aus vielen Faktoren ist unhandlich: Ableiten verlangt die Produktregel für jeden Faktor, und die Zahlen werden winzig. Der Logarithmus macht aus dem Produkt eine Summe.

:::definition Definition 4.3 (Log-Likelihood)
<span class="anker" id="satz-4-3"></span>

Die __Log-Likelihood__ ist der natürliche Logarithmus der Likelihood. Für eine Stichprobe ist sie die Summe

<span class="anker" id="gl-4-6"></span>
$$\ell(\theta)=\ln\mathcal L(\theta)=\sum_{i=1}^N\ln P(X=x_i\mid\theta) , \tag{4.6}$$

bei stetigen Daten mit $\ln p(x_i\mid\theta)$ statt $\ln P(X=x_i\mid\theta)$.
:::

Für das Bernoulli-Modell ist nach den Rechenregeln [(4.1)](#gl-4-1)

<span class="anker" id="gl-4-7"></span>
$$\ell(\theta)=N_1\ln\theta+N_0\ln(1-\theta) . \tag{4.7}$$

Weil alle Wahrscheinlichkeiten höchstens $1$ sind, ist die Log-Likelihood diskreter Daten nie positiv.

::::beispiel [Rechenbeispiel]
Für die zehn Würfe ist $\ell(0{,}7)=7\ln0{,}7+3\ln0{,}3\approx-6{,}109$ (Abb. [9](#abb-9)) und $\ell(0{,}5)=10\ln0{,}5\approx-6{,}931$. Der Unterschied $0{,}823$ ist der Logarithmus des Verhältnisses $2{,}28$ aus dem vorigen Unterabschnitt. Abb. [7](#abb-7) (b) zeigt die ganze Kurve.

:::abbildung ml/k5rloglik 9
Die Log-Likelihood von $\theta=0{,}7$ für dieselben zehn Würfe als Summe: ein Summand je Wurf, $\ln0{,}7$ für Kopf und $\ln0{,}3$ für Zahl.
:::
::::

⁠**Kurz gesagt:** Die Log-Likelihood ist der Logarithmus der Likelihood und für eine Stichprobe eine Summe mit einem Summanden je Datenpunkt.

:::hintergrund Warum man logarithmiert
Drei Gründe machen die Log-Likelihood zum üblichen Werkzeug. Erstens wird aus dem Produkt eine Summe. Jeder Datenpunkt trägt einen eigenen Summanden bei, und die Ableitung einer Summe ist die Summe der Ableitungen; beim Produkt bräuchte man die Produktregel aus [Kapitel 3, Abschnitt 1.4](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/die-ableitung.html#stufe-1-4), für jeden Faktor. Zweitens bleibt die Stelle des Maximums dieselbe. Weil $\ln$ streng monoton wächst, ist $\mathcal L(\theta_1)<\mathcal L(\theta_2)$ genau dann, wenn $\ell(\theta_1)<\ell(\theta_2)$; die Reihenfolge aller Parameterwerte bleibt erhalten, nur die Werte selbst ändern sich. Drittens bleiben die Zahlen darstellbar. Eine Gleitkommazahl aus [Kapitel 3, Abschnitt 11.3](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/numerische-ableitung-und-gradientenprufung.html#stufe-11-3), ist eine Ziffernfolge mal einer Zweierpotenz, und auch die Hochzahl dieser Zweierpotenz hat nur einen begrenzten Bereich. Die kleinste darstellbare positive Zahl doppelter Genauigkeit ist $2^{-1074}\approx4{,}9\cdot10^{-324}$. Schon $0{,}5^{1075}$ wird deshalb zu null gerundet. Bei $1000$ Datenpunkten mit Wahrscheinlichkeiten um $0{,}3$ hätte die Likelihood die Größenordnung $10^{-523}$, würde also für jeden Parameterwert null, und man könnte keine zwei Werte mehr unterscheiden. Die Log-Likelihood ist dann etwa $-1204$, eine ganz gewöhnliche Zahl.
:::

:::aufgabe Aufgabe 11 ★ Rechnen mit Logarithmen
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Berechne $\ln\bigl(0{,}2^3\cdot0{,}8^2\bigr)$ mit den Rechenregeln aus $\ln0{,}2$ und $\ln0{,}8$.

</li>

<li>

Bestimme $\log_2\frac1{64}$, $\log_232$ und $\log_2\frac13$.

</li>

<li>

Für welche Zahl $x$ ist $2^x=10$?

</li>

</ol>

:::loesung
(a) $\ln(0{,}2^3\cdot0{,}8^2)=3\ln0{,}2+2\ln0{,}8\approx3\cdot(-1{,}6094)+2\cdot(-0{,}2231)\approx-4{,}8283-0{,}4463=-5{,}2746$.

(b) $\log_2\frac1{64}=-6$, $\log_232=5$, $\log_2\frac13=-\log_23\approx-1{,}585$.

(c) $x=\log_210=\ln10/\ln2\approx2{,}3026/0{,}6931\approx3{,}322$.
:::
:::

:::aufgabe Aufgabe 12 ★ Die Likelihood einer Reißzwecke
<span class="anker" id="aufg-12"></span>

Die Reißzwecke aus Aufgabe [1](schatzen-aus-einer-stichprobe.html#aufg-1) landete in acht Würfen fünfmal auf dem Rücken.

<ol class="al">

<li>

Schreibe die Likelihood und die Log-Likelihood auf.

</li>

<li>

Berechne beide für $\theta=0{,}5$, $\theta=0{,}625$ und $\theta=0{,}8$. Welcher der drei Werte erklärt die Daten am besten?

</li>

</ol>

:::loesung
(a) $\mathcal L(\theta)=\theta^5(1-\theta)^3$ und $\ell(\theta)=5\ln\theta+3\ln(1-\theta)$.

(b) $\mathcal L(0{,}5)=0{,}5^8\approx0{,}00391$ mit $\ell\approx-5{,}545$; $\mathcal L(0{,}625)\approx0{,}00503$ mit $\ell\approx-5{,}293$; $\mathcal L(0{,}8)\approx0{,}00262$ mit $\ell\approx-5{,}944$. Am besten erklärt der Wert $0{,}625$ die Daten, der Anteil $5/8$.
:::
:::

:::aufgabe Aufgabe 13 ★★ Zwei Lesarten derselben Formel
<span class="anker" id="aufg-13"></span>

Eine Münze wird zweimal geworfen; das Modell ist $\mathrm{Ber}(\theta)$.

<ol class="al">

<li>

Halte $\theta$ fest und addiere $P(\mathcal D\mid\theta)$ über alle vier möglichen Datensätze. Was kommt heraus, und warum?

</li>

<li>

Halte den Datensatz $\mathcal D=(1,1)$ fest und berechne $\int_0^1\mathcal L(\theta)\,\mathrm{d}\theta$. Warum muss hier nicht $1$ herauskommen?

</li>

</ol>

:::loesung
(a) Die vier Datensätze haben die Wahrscheinlichkeiten $\theta^2$, $\theta(1-\theta)$, $(1-\theta)\theta$, $(1-\theta)^2$, zusammen $(\theta+1-\theta)^2=1$. Bei festem $\theta$ ist $P(\mathcal D\mid\theta)$ eine Wahrscheinlichkeitsverteilung über alle möglichen Datensätze.

(b) $\int_0^1\theta^2\,\mathrm{d}\theta=\tfrac13$. Hier wird über die Parameterwerte integriert, und die Likelihood ist keine Verteilung über sie; nichts verlangt, dass die Fläche $1$ ist.
:::
:::

:::aufgabe Aufgabe 14 ★★ Folge oder Anzahl
<span class="anker" id="aufg-14"></span>

Statt der ganzen Folge der zehn Würfe sei nur die Anzahl $N_1=7$ der Köpfe überliefert. Ihre Wahrscheinlichkeit ist nach [Kapitel 4, Abschnitt 8.3](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wichtige-verteilungen.html#stufe-8-3), $\binom{10}7\theta^7(1-\theta)^3$.

<ol class="al">

<li>

Vergleiche diese Likelihood mit [(4.5)](#gl-4-5). Wie unterscheiden sich die beiden Log-Likelihoods?

</li>

<li>

Warum führen beide auf dieselben Schlüsse über $\theta$?

</li>

</ol>

:::loesung
(a) Die Likelihood aus der Anzahl ist $\binom{10}7$-mal so groß, also $120\,\theta^7(1-\theta)^3$. Die Log-Likelihoods unterscheiden sich um die Konstante $\ln120\approx4{,}79$.

(b) Ein fester Faktor ändert nicht, welche Parameterwerte größere und welche kleinere Likelihood haben, und auch nicht das Verhältnis zweier Werte. Alle Vergleiche und die Stelle des Maximums sind gleich. Das passt zum Hintergrund-Kasten in Unterabschnitt [4.3](#stufe-4-3): Die Anzahl $N_1$ enthält alles, was die Folge über $\theta$ sagt.
:::
:::

:::aufgabe Aufgabe 15 ★★ Eigene Reißzwecke (praktisch)
<span class="anker" id="aufg-15"></span>

Wirf eine Reißzwecke $20$-mal und notiere, wie oft sie auf dem Rücken landet.

<ol class="al">

<li>

Berechne die Log-Likelihood deiner Daten für $\theta=0{,}1;\ 0{,}2;\ \dots;\ 0{,}9$ und skizziere sie.

</li>

<li>

Bei welchem dieser Werte ist sie am größten? Bewahre deine Daten auf; die Aufgaben [22](die-maximum-likelihood-schatzung.html#aufg-22) und [31](die-maximum-a-posteriori-schatzung.html#aufg-31) rechnen mit ihnen weiter.

</li>

</ol>

:::loesung
(a) Hast du $N_1$ Rückenlagen in $20$ Würfen beobachtet, so ist $\ell(\theta)=N_1\ln\theta+(20-N_1)\ln(1-\theta)$. Ein Beispiel mit $N_1=12$: $\ell(0{,}5)\approx-13{,}86$, $\ell(0{,}6)\approx-13{,}46$, $\ell(0{,}7)\approx-13{,}91$. Die Kurve steigt von $\theta=0{,}1$ an, hat ein flaches Maximum und fällt zu $\theta=0{,}9$ steil ab.

(b) Das Maximum liegt bei geradem $N_1$ genau bei dem Gitterwert $N_1/20$, bei ungeradem $N_1$ bei einem der beiden Gitterwerte daneben; im Beispiel bei $0{,}6$. Abschnitt [5](die-maximum-likelihood-schatzung.html#stufe-5) zeigt, dass das genaue Maximum bei $N_1/20$ liegt.
:::
:::
