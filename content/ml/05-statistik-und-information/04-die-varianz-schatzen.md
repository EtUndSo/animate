---
title: Die Varianz schätzen
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Statistik und Information
knoten: Grundlagen 5: Statistik und Information
nachschlagen: ja
order: 15250400
summary: Grundlagen 1 hat die Quadratsumme der Abweichungen durch die Anzahl N der Werte geteilt; viele Texte und Taschenrechner teilen durch N-1 .
tags: Bessel-Korrektur, Freiheitsgrade
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
[Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) hat die Quadratsumme der Abweichungen durch die Anzahl $N$ der Werte geteilt; viele Texte und Taschenrechner teilen durch $N-1$. Dieser Abschnitt zeigt, warum: Teilen durch $N$ unterschätzt die Varianz der Verteilung im Mittel um genau den Faktor $(N-1)/N$, und Teilen durch $N-1$ gleicht das aus. Dass „im Mittel richtig“ nicht dasselbe ist wie „möglichst genau“, zeigt der letzte Unterabschnitt.
:::

### Teilen durch $N$ unterschätzt die Varianz

<span class="anker" id="stufe-3-1"></span>

[Grundlagen 1, Abschnitt 4.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-4), hat die Standardabweichung eines Datensatzes mit dem Nenner $N$ gebildet, und [Grundlagen 4, Abschnitt 7.7](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-7), hat gezeigt, dass ihr Quadrat die Varianz der empirischen Verteilung ist. Will man aus der Stichprobe die Varianz $\sigma^2$ der Verteilung schätzen, aus der sie stammt, so liegt es nahe, dieselbe Formel zu nehmen.

:::definition Definition 3.1 (Varianzschätzer mit Nenner $N$)
<span class="anker" id="satz-3-1"></span>

Für eine Stichprobe $X_1,\dots,X_N$ mit dem Mittelwert $\bar X$ ist

<span class="anker" id="gl-3-1"></span>
$$\hat\sigma^2_N=\frac1N\sum_{i=1}^N(X_i-\bar X)^2 . \tag{3.1}$$
:::

Der Index $N$ gibt den Nenner an. Dass dieser Schätzer systematisch zu klein ausfällt, zeigt schon das kleine Beispiel aus Unterabschnitt [1.4](schatzen-aus-einer-stichprobe.html#stufe-1-4).

::::beispiel [Rechenbeispiel]
Für die neun Stichproben aus den Werten $1$, $2$, $3$ mit $N=2$ ist die Quadratsumme $\sum_i(x_i-\bar x)^2$ einfach $\tfrac12(x_1-x_2)^2$, denn beide Werte liegen um $\tfrac12|x_1-x_2|$ neben ihrem Mittelwert. Tabelle [2](#tab-2) führt sie auf.

<span class="anker" id="tab-2"></span>

**Tabelle 2:** Die neun Stichproben aus Tabelle [1](schatzen-aus-einer-stichprobe.html#tab-1) mit der Quadratsumme $q=\sum_i(x_i-\bar x)^2$ und dem Varianzschätzer $\hat\sigma^2_N=q/2$. Die wahre Varianz ist $\sigma^2=\tfrac23$.

| Stichprobe $(x_1,x_2)$ | $(1,1)$ | $(1,2)$ | $(1,3)$ | $(2,1)$ | $(2,2)$ | $(2,3)$ | $(3,1)$ | $(3,2)$ | $(3,3)$ |
|---|---|---|---|---|---|---|---|---|---|
| Quadratsumme $q$ | $0$ | $0{,}5$ | $2$ | $0{,}5$ | $0$ | $0{,}5$ | $2$ | $0{,}5$ | $0$ |
| $\hat\sigma^2_N=q/2$ | $0$ | $0{,}25$ | $1$ | $0{,}25$ | $0$ | $0{,}25$ | $1$ | $0{,}25$ | $0$ |

Der Schätzer nimmt also den Wert $0$ mit der Wahrscheinlichkeit $\tfrac39$ an, den Wert $0{,}25$ mit $\tfrac49$ und den Wert $1$ mit $\tfrac29$. Sein Erwartungswert ist $\tfrac13$ (Abb. [6](#abb-6)), nur halb so groß wie die wahre Varianz $\tfrac23$.

:::abbildung ml/k5rbessel 6
Die Erwartungswerte der beiden Varianzschätzer als Summen über ihre Stichprobenverteilung aus Tabelle [2](#tab-2). Mit dem Nenner $N=2$ kommt im Mittel nur die Hälfte der wahren Varianz heraus, mit dem Nenner $N-1=1$ genau die wahre Varianz.
:::
::::

Das Ergebnis ist kein Zufall dieses Beispiels.

:::satz Satz 3.2 (Verzerrung von $\hat\sigma^2_N$)
<span class="anker" id="satz-3-2"></span>

Sind $X_1,\dots,X_N$ i.i.d. mit der Varianz $\sigma^2$, so ist

<span class="anker" id="gl-3-2"></span>
$$\mathbb{E}[\hat\sigma^2_N]=\frac{N-1}N\,\sigma^2 . \tag{3.2}$$
:::

:::herleitung Verzerrung von $\hat\sigma^2_N$
Es sei $\mu$ der Erwartungswert. Man schreibt jede Abweichung vom wahren Erwartungswert als Abweichung vom Mittelwert plus Abweichung des Mittelwerts: $X_i-\mu=(X_i-\bar X)+(\bar X-\mu)$. Quadriert und summiert ergibt das

<span class="anker" id="gl-3-3"></span>
$$\sum_{i=1}^N(X_i-\mu)^2=\sum_{i=1}^N(X_i-\bar X)^2+2\,(\bar X-\mu)\sum_{i=1}^N(X_i-\bar X)+N\,(\bar X-\mu)^2 . \tag{3.3}$$

Das mittlere Glied ist null, weil sich die Abweichungen vom Mittelwert nach [Grundlagen 1, Abschnitt 4.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-3), zu null summieren. Jetzt bildet man Erwartungswerte. Links steht $N$-mal $\mathbb{E}[(X_i-\mu)^2]=\sigma^2$, also $N\sigma^2$. Rechts ist $\mathbb{E}[(\bar X-\mu)^2]=\operatorname{Var}(\bar X)=\sigma^2/N$ nach [Grundlagen 4, Abschnitt 13.1](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/mittelwerte-vieler-zufallsvariablen.html#stufe-13-1), das letzte Glied hat also den Erwartungswert $\sigma^2$. Damit ist

$$\mathbb{E}\Bigl[\sum_{i=1}^N(X_i-\bar X)^2\Bigr]=N\sigma^2-\sigma^2=(N-1)\,\sigma^2 ,$$

und Teilen durch $N$ ergibt [(3.2)](#gl-3-2).
:::

Die Verzerrung ist $\mathbb{E}[\hat\sigma^2_N]-\sigma^2=-\sigma^2/N$. Sie geht mit wachsendem $N$ gegen null, aber bei kleinen Stichproben ist sie erheblich.

::::beispiel [Rechenbeispiel]
Für die Flächen der vier Wohnungen, $60$, $40$, $90$ und $70\,\mathrm m^2$, ist die Quadratsumme $25+625+625+25=1300$ und $\hat\sigma^2_N=325\,\mathrm m^4$, das Quadrat der Standardabweichung $18{,}03\,\mathrm m^2$ aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html). Als Schätzung für die Varianz der Flächen aller Wohnungen der Stadt ist diese Zahl im Mittel um den Faktor $\tfrac34$ zu klein.
::::

⁠**Kurz gesagt:** Der Varianzschätzer mit dem Nenner $N$ hat den Erwartungswert $\tfrac{N-1}N\,\sigma^2$; er unterschätzt die Varianz systematisch.

:::hintergrund Warum die Abweichungen vom eigenen Mittelwert zu klein sind
Der Mittelwert $\bar x$ wird aus denselben Daten berechnet, deren Abweichungen man danach misst, und er liegt deshalb mitten zwischen ihnen. Genauer: Ersetzt man in [(3.3)](#gl-3-3) die Zahl $\mu$ durch eine beliebige Zahl $a$, so gilt dieselbe Rechnung, und es ist $\sum_i(x_i-a)^2=\sum_i(x_i-\bar x)^2+N(\bar x-a)^2$. Die Quadratsumme um $a$ ist also am kleinsten für $a=\bar x$; das ist die Aussage aus [Grundlagen 2, Abschnitt 11.4](/wissen/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/die-pseudoinverse.html#stufe-11-4), dass der Mittelwert die beste Näherungslösung von „$a=x_i$ für alle $i$“ ist. Insbesondere ist die Quadratsumme um $\bar x$ höchstens so groß wie die um den wahren Erwartungswert $\mu$, den man nicht kennt. Der Fehlbetrag ist genau $N(\bar x-\mu)^2$, und sein Erwartungswert ist $\sigma^2$: Im Mittel geht genau die Streuung eines einzelnen Werts verloren. Kennt man $\mu$ und misst die Abweichungen von $\mu$ statt von $\bar x$, verschwindet die Verzerrung (Aufgabe [9](#aufg-9)).
:::

### Die Bessel-Korrektur

<span class="anker" id="stufe-3-2"></span>

Wenn ein Schätzer im Mittel um einen bekannten Faktor zu klein ist, multipliziert man mit dem Kehrwert dieses Faktors.

:::definition Definition 3.3 (Bessel-Korrektur)
<span class="anker" id="satz-3-3"></span>

Für $N\ge2$ ist

<span class="anker" id="gl-3-4"></span>
$$\hat\sigma^2_{N-1}=\frac{N}{N-1}\,\hat\sigma^2_N=\frac1{N-1}\sum_{i=1}^N(X_i-\bar X)^2 . \tag{3.4}$$

Der Faktor $N/(N-1)$ heißt __Bessel-Korrektur__.
:::

Nach [(3.2)](#gl-3-2) ist $\mathbb{E}[\hat\sigma^2_{N-1}]=\tfrac N{N-1}\cdot\tfrac{N-1}N\,\sigma^2=\sigma^2$: Der korrigierte Schätzer ist erwartungstreu. Viele Taschenrechner bieten beide Fassungen an, oft unter den Bezeichnungen $\sigma_n$ und $\sigma_{n-1}$ oder $\sigma$ und $s$. Für große $N$ ist der Unterschied klein: Bei $N=100$ unterscheiden sich die beiden Varianzschätzer um $1\,\%$ und ihre Wurzeln um $0{,}5\,\%$.

Welche Fassung richtig ist, hängt von der Frage ab. Beschreibt man einen Datensatz selbst, etwa um ihn zu standardisieren wie in [Grundlagen 1, Abschnitt 4.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-5), so ist die Varianz der empirischen Verteilung gemeint, und der Nenner $N$ ist richtig. Will man die Varianz der Verteilung schätzen, aus der die Daten stammen, und soll die Schätzung im Mittel stimmen, nimmt man den Nenner $N-1$.

::::beispiel [Rechenbeispiel]
Im Beispiel aus Tabelle [2](#tab-2) ist $\hat\sigma^2_{N-1}=q$, also doppelt so groß wie $\hat\sigma^2_N$, mit den Werten $0$, $0{,}5$ und $2$. Sein Erwartungswert ist $\tfrac23=\sigma^2$ (Abb. [6](#abb-6), zweite Zeile). Für die Wohnungen ist $\hat\sigma^2_{N-1}=1300/3\approx433{,}3\,\mathrm m^4$ und seine Wurzel $20{,}82\,\mathrm m^2$.
::::

⁠**Kurz gesagt:** Teilt man die Quadratsumme durch $N-1$ statt durch $N$, wird der Varianzschätzer erwartungstreu; das ist die Bessel-Korrektur.

:::hintergrund Freiheitsgrade und der Name
Eine anschauliche Begründung des Nenners $N-1$: Die $N$ Abweichungen $x_i-\bar x$ summieren sich immer zu null. Kennt man $N-1$ von ihnen, ist die letzte festgelegt. Es gibt also nur $N-1$ frei veränderliche Abweichungen, man sagt: $N-1$ __Freiheitsgrade__. Teilt man durch die Zahl der Freiheitsgrade statt durch die Zahl der Summanden, so mittelt man nur über das, was wirklich frei streuen kann. Bei $N=1$ ist die einzige Abweichung immer null; dann gibt es keinen Freiheitsgrad, und aus einem einzigen Wert lässt sich über die Streuung nichts lernen. Das ist eine Plausibilitätsbetrachtung; der eigentliche Grund ist die Rechnung im vorigen Unterabschnitt. Benannt ist die Korrektur nach dem Astronomen Friedrich Wilhelm Bessel. Benutzt hat den Faktor schon Carl Friedrich Gauß in seiner Arbeit von 1823 über das Ausgleichen fehlerbehafteter Messungen.
:::

### Erwartungstreu heißt nicht genauer

<span class="anker" id="stufe-3-3"></span>

Die Bessel-Korrektur beseitigt die Verzerrung, aber sie vergrößert den Schätzer und damit auch seine Schwankungen. Nach dem Satz in Unterabschnitt [2.3](wie-gut-ist-ein-schatzer.html#stufe-2-3) zählt für die Genauigkeit beides.

::::beispiel [Rechenbeispiel]
Im Beispiel aus Tabelle [2](#tab-2) hat $\hat\sigma^2_N$ die Verzerrung $\tfrac13-\tfrac23=-\tfrac13$. Seine Varianz ist nach der Verschiebungsformel $\mathbb{E}[(\hat\sigma^2_N)^2]-\tfrac19=\tfrac{0+4\cdot0{,}0625+2\cdot1}9-\tfrac19=\tfrac14-\tfrac19=\tfrac5{36}$. Also ist

$$\operatorname{MSE}(\hat\sigma^2_N)=\tfrac19+\tfrac5{36}=\tfrac14,\qquad \operatorname{MSE}(\hat\sigma^2_{N-1})=\operatorname{Var}(\hat\sigma^2_{N-1})=2^2\cdot\tfrac5{36}=\tfrac59 .$$

Der korrigierte Schätzer ist unverzerrt, liegt aber im quadratischen Mittel mehr als doppelt so weit neben der wahren Varianz. Der Grund: Er ist hier das Doppelte von $\hat\sigma^2_N$, und nach [Grundlagen 4, Abschnitt 7.6](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-6), vervierfacht das die Varianz. Allgemein multipliziert die Bessel-Korrektur die Varianz mit $\bigl(N/(N-1)\bigr)^2$.
::::

Auch die Wurzel bereitet Mühe. Selbst wenn $\hat\sigma^2_{N-1}$ erwartungstreu für $\sigma^2$ ist, unterschätzt seine Wurzel $\hat\sigma_{N-1}$ die Standardabweichung $\sigma$. Nach der Verschiebungsformel ist nämlich

$$\mathbb{E}[\hat\sigma_{N-1}]^2=\mathbb{E}[\hat\sigma^2_{N-1}]-\operatorname{Var}(\hat\sigma_{N-1})=\sigma^2-\operatorname{Var}(\hat\sigma_{N-1}),$$

und das ist kleiner als $\sigma^2$, sobald $\hat\sigma_{N-1}$ überhaupt schwankt. Im Beispiel nimmt $\hat\sigma_{N-1}$ die Werte $0$, $\sqrt{0{,}5}\approx0{,}707$ und $\sqrt2\approx1{,}414$ an, mit dem Erwartungswert $\tfrac{4\cdot0{,}707+2\cdot1{,}414}9\approx0{,}629$, während $\sigma=\sqrt{2/3}\approx0{,}816$ ist.

⁠**Kurz gesagt:** Erwartungstreue ist nur eine Eigenschaft unter mehreren: Der unverzerrte Varianzschätzer streut stärker und kann im mittleren quadratischen Fehler schlechter sein, und seine Wurzel ist für die Standardabweichung wieder verzerrt.

:::hintergrund Welcher Nenner den kleinsten Fehler hat
Für normalverteilte Daten lässt sich die Frage genau beantworten. Dort hat die Quadratsumme $Q=\sum_i(X_i-\bar X)^2$ den Erwartungswert $(N-1)\sigma^2$ und, wie man mit Mitteln außerhalb dieses Kapitels zeigt, die Varianz $2(N-1)\sigma^4$. Ein Schätzer $c\,Q$ mit einer festen Zahl $c$ hat dann nach dem Satz in Unterabschnitt [2.3](wie-gut-ist-ein-schatzer.html#stufe-2-3) den mittleren quadratischen Fehler

$$\operatorname{MSE}(c\,Q)=\sigma^4\bigl[\,2(N-1)\,c^2+\bigl((N-1)\,c-1\bigr)^2\,\bigr] .$$

Das ist eine nach oben geöffnete Parabel in $c$, mit dem Scheitel bei $c=1/(N+1)$. Der genaueste Schätzer dieser Form teilt also durch $N+1$, mit dem Fehler $2\sigma^4/(N+1)$; der Nenner $N$ liefert $(2N-1)\sigma^4/N^2$, der Nenner $N-1$ liefert $2\sigma^4/(N-1)$. Für $N=10$ sind das $0{,}182\,\sigma^4$, $0{,}19\,\sigma^4$ und $0{,}222\,\sigma^4$. Für andere Verteilungen liegt der beste Nenner woanders: Im Beispiel mit den Werten $1$, $2$, $3$ hat der Nenner $N+1=3$ den Fehler $\tfrac7{27}\approx0{,}259$, mehr als die $\tfrac14$ des Nenners $N$. Der Nenner $N-1$ ist also nicht der genaueste, sondern der, der im Mittel stimmt.
:::

:::aufgabe Aufgabe 7 ★ Vier Spannungsmessungen
<span class="anker" id="aufg-7"></span>

Ein Messgerät zeigt bei vier Messungen derselben Spannung $4{,}9$, $5{,}3$, $5{,}1$ und $4{,}7\,\mathrm V$.

<ol class="al">

<li>

Berechne den Mittelwert, die Quadratsumme der Abweichungen, $\hat\sigma^2_N$ und $\hat\sigma^2_{N-1}$.

</li>

<li>

Berechne beide Standardabweichungen. Um wie viel Prozent unterscheiden sie sich?

</li>

</ol>

:::loesung
(a) $\bar x=5{,}0\,\mathrm V$. Die Abweichungen sind $-0{,}1$; $0{,}3$; $0{,}1$; $-0{,}3$, ihre Quadratsumme ist $0{,}01+0{,}09+0{,}01+0{,}09=0{,}2\,\mathrm V^2$. Also ist $\hat\sigma^2_N=0{,}05\,\mathrm V^2$ und $\hat\sigma^2_{N-1}=0{,}2/3\approx0{,}0667\,\mathrm V^2$.

(b) $\hat\sigma_N\approx0{,}224\,\mathrm V$ und $\hat\sigma_{N-1}\approx0{,}258\,\mathrm V$. Ihr Verhältnis ist $\sqrt{4/3}\approx1{,}155$, sie unterscheiden sich also um gut $15\,\%$; bei vier Werten ist die Wahl des Nenners also nicht gleichgültig.
:::
:::

:::aufgabe Aufgabe 8 ★★ Die Verzerrung bei einer Münze abzählen
<span class="anker" id="aufg-8"></span>

Eine faire Münze mit Kopf $=1$ und Zahl $=0$ wird zweimal geworfen.

<ol class="al">

<li>

Berechne die Varianz $\sigma^2$ eines Wurfs.

</li>

<li>

Bestimme für alle vier möglichen Stichproben $\hat\sigma^2_N$ und $\hat\sigma^2_{N-1}$ und berechne ihre Erwartungswerte. Prüfe [(3.2)](#gl-3-2).

</li>

</ol>

:::loesung
(a) Nach [Grundlagen 4, Abschnitt 8.1](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/wichtige-verteilungen.html#stufe-8-1), ist $\sigma^2=\theta(1-\theta)=\tfrac14$.

(b) Für $(0,0)$ und $(1,1)$ ist die Quadratsumme $0$, für $(0,1)$ und $(1,0)$ ist $\bar x=\tfrac12$ und die Quadratsumme $\tfrac14+\tfrac14=\tfrac12$. Also ist $\hat\sigma^2_N$ gleich $0$ oder $\tfrac14$, je mit der Wahrscheinlichkeit $\tfrac12$, und $\mathbb{E}[\hat\sigma^2_N]=\tfrac18=\tfrac12\cdot\tfrac14=\tfrac{N-1}N\,\sigma^2$, wie [(3.2)](#gl-3-2) verlangt. $\hat\sigma^2_{N-1}$ ist gleich $0$ oder $\tfrac12$ und hat den Erwartungswert $\tfrac14=\sigma^2$.
:::
:::

:::aufgabe Aufgabe 9 ★★ Wenn der Erwartungswert bekannt ist
<span class="anker" id="aufg-9"></span>

Ist der Erwartungswert $\mu$ bekannt, so kann man die Varianz mit $\tilde\sigma^2=\frac1N\sum_i(X_i-\mu)^2$ schätzen.

<ol class="al">

<li>

Zeige, dass $\tilde\sigma^2$ erwartungstreu ist, ohne Korrektur.

</li>

<li>

Erkläre mit dem Hintergrund in Unterabschnitt [3.1](#stufe-3-1), warum hier nichts korrigiert werden muss.

</li>

<li>

Berechne $\tilde\sigma^2$ für die Wohnungsflächen mit dem angenommenen Erwartungswert $\mu=60\,\mathrm m^2$ und prüfe die Zerlegung $\sum_i(x_i-\mu)^2=\sum_i(x_i-\bar x)^2+N(\bar x-\mu)^2$.

</li>

</ol>

:::loesung
(a) Es ist $\mathbb{E}[(X_i-\mu)^2]=\sigma^2$ für jedes $i$, also $\mathbb{E}[\tilde\sigma^2]=\tfrac1N\cdot N\sigma^2=\sigma^2$.

(b) Die Verzerrung von $\hat\sigma^2_N$ entsteht, weil $\bar x$ aus denselben Daten berechnet wird und deshalb näher an ihnen liegt als $\mu$; der Fehlbetrag $N(\bar x-\mu)^2$ fehlt in der Quadratsumme. Misst man von $\mu$ aus, gibt es keinen solchen Fehlbetrag. In der Sprache der Freiheitsgrade: Kein Freiheitsgrad wird für das Schätzen des Mittelwerts verbraucht.

(c) $\sum_i(x_i-60)^2=0+400+900+100=1400$, also $\tilde\sigma^2=350\,\mathrm m^4$. Zerlegung: $\sum_i(x_i-65)^2=1300$ und $N(\bar x-60)^2=4\cdot25=100$, zusammen $1400$.
:::
:::

:::aufgabe Aufgabe 10 ★★ Zweimal würfeln (praktisch)
<span class="anker" id="aufg-10"></span>

Ein gewöhnlicher Würfel hat die Varianz $\sigma^2=\tfrac{35}{12}\approx2{,}917$ ([Grundlagen 4, Abschnitt 7.4](/wissen/informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit/erwartungswert-und-varianz.html#stufe-7-4)).

<ol class="al">

<li>

Würfle zweimal und berechne $\hat\sigma^2_N$. Wiederhole das zehnmal und mittle die zehn Werte.

</li>

<li>

Welchen Mittelwert erwartest du nach [(3.2)](#gl-3-2)? Liegt dein Ergebnis näher an diesem Wert oder an $\sigma^2$?

</li>

<li>

Welchen Mittelwert hätten die zehn Werte von $\hat\sigma^2_{N-1}$ ergeben?

</li>

</ol>

:::loesung
(a) Die Ergebnisse sind zufällig; ein Beispiel: Die Paare $(3,5)$, $(6,6)$, $(1,4)$ ergeben $\hat\sigma^2_N=1$, $0$ und $2{,}25$. Allgemein ist für zwei Werte $\hat\sigma^2_N=\tfrac14(x_1-x_2)^2$.

(b) Nach [(3.2)](#gl-3-2) mit $N=2$ ist der Erwartungswert $\tfrac12\cdot\tfrac{35}{12}=\tfrac{35}{24}\approx1{,}458$. Mit zehn Wiederholungen streut der Mittelwert noch merklich, liegt aber typischerweise näher an $1{,}46$ als an $2{,}92$.

(c) $\hat\sigma^2_{N-1}$ ist für $N=2$ das Doppelte von $\hat\sigma^2_N$; der Mittelwert der zehn Werte ist also das Doppelte deines Ergebnisses aus (a), und sein Erwartungswert ist $\tfrac{35}{12}\approx2{,}917$.
:::
:::
