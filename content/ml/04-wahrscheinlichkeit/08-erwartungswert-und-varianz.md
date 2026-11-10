---
title: Erwartungswert und Varianz
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
adresse: informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit
knoten: Kapitel 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15240800
summary: Eine Verteilung besteht aus vielen Zahlen, oft aus unendlich vielen.
tags: Erwartungswert, Schwerpunkt, Indikatorvariable, Varianz, Standardabweichung, standardisierte, empirische Verteilung, Median
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Eine Verteilung besteht aus vielen Zahlen, oft aus unendlich vielen. Für viele Zwecke genügen zwei: wo die Werte im Mittel liegen und wie weit sie um diese Mitte streuen. Dieser Abschnitt führt dafür den Erwartungswert und die Varianz ein, zeigt die Rechenregeln, die sie handlich machen, und klärt, wie sie mit dem Mittelwert und der Standardabweichung eines Datensatzes aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) zusammenhängen und wie nicht.
:::

### Der Erwartungswert

<span class="anker" id="stufe-7-1"></span>

Wirft man einen fairen Würfel sehr oft und bildet den Durchschnitt aller Augenzahlen, so kommt etwa $3{,}5$ heraus. Der Grund: In $n$ Würfen fällt jede Augenzahl etwa $n/6$-mal, und der Durchschnitt ist $\frac1n\bigl(1\cdot\tfrac n6+2\cdot\tfrac n6+\dots+6\cdot\tfrac n6\bigr)=3{,}5$. Jeder Wert geht mit dem Anteil ein, mit dem er vorkommt, und dieser Anteil ist auf lange Sicht seine Wahrscheinlichkeit. Das macht man zur Definition.

:::definition Definition 7.1 (Erwartungswert)
<span class="anker" id="satz-7-1"></span>

Der __Erwartungswert__ einer diskreten Zufallsvariablen $X$ mit den Werten $x_k$ ist

<span class="anker" id="gl-7-1"></span>
$$\mathbb{E}[X]=\sum_kx_k\,P(X=x_k), \tag{7.1}$$

der einer stetig verteilten Zufallsvariablen mit der Dichte $p$ ist

<span class="anker" id="gl-7-2"></span>
$$\mathbb{E}[X]=\int_{-\infty}^\infty x\,p(x)\,\mathrm{d} x . \tag{7.2}$$

Er wird auch $\mu$ oder $\mu_X$ geschrieben.
:::

Bei unendlich vielen Werten muss die Summe oder das Integral endlich sein, genauer muss es auch mit $|x|$ statt $x$ endlich sein; sonst hat $X$ keinen Erwartungswert. Bei endlich vielen Werten gibt es ihn immer. Anschaulich ist der Erwartungswert der __Schwerpunkt__ der Verteilung: Legt man auf einen Stab an jede Stelle $x_k$ ein Gewicht $P(X=x_k)$, so liegt er bei $\mathbb{E}[X]$ im Gleichgewicht. Der Erwartungswert muss kein möglicher Wert sein; einen Würfelwurf mit $3{,}5$ Augen gibt es nicht.

Hat $X$ endlich viele Werte $v_1,\dots,v_K$ mit den Wahrscheinlichkeiten $p_k=P(X=v_k)$, so ist [(7.1)](#gl-7-1) ein Skalarprodukt aus [Grundlagen 1, Abschnitt 2.1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-1): Mit dem Wertevektor $\mathbf{v}=(v_1,\dots,v_K)^{\top}$ und dem Wahrscheinlichkeitsvektor $\mathbf{p}=(p_1,\dots,p_K)^{\top}$ ist

<span class="anker" id="gl-7-3"></span>
$$\mathbb{E}[X]=\mathbf{v}^{\top}\mathbf{p}=\sum_{k=1}^Kv_k\,p_k . \tag{7.3}$$

Das ist ein gewichteter Mittelwert der Werte, mit den Gewichten $p_k$, die nichtnegativ sind und sich zu $1$ addieren. Gerechnet wird wie bei der Stromrechnung in [Grundlagen 1, Abschnitt 2.3](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-3): dort Preis mal Menge, summiert, hier Wert mal Wahrscheinlichkeit.

::::beispiel [Rechenbeispiel 1]
Für die Anzahl $X$ der Köpfe bei drei Münzwürfen ist $\mathbf{v}=(0,\,1,\,2,\,3)^{\top}$ und $\mathbf{p}=(0{,}125;\ 0{,}375;\ 0{,}375;\ 0{,}125)^{\top}$. Abb. [7](#abb-7) rechnet $\mathbb{E}[X]=1{,}5$ Zeile für Zeile: Jeder Wert trägt sein Gewicht bei. Die Verteilung ist symmetrisch um $1{,}5$, und dort liegt ihr Schwerpunkt.

:::abbildung ml/k4rmuenzen 7
Der Erwartungswert der Anzahl der Köpfe als Skalarprodukt aus Wertevektor und Wahrscheinlichkeitsvektor: Jeder Wert geht mit seiner Wahrscheinlichkeit gewichtet ein.
:::
::::

::::beispiel [Rechenbeispiel 2]
Für einen fairen Würfel ist $P(X=k)=\tfrac16$ für $k=1,\dots,6$, und jede Augenzahl geht mit demselben Gewicht ein; der Erwartungswert ist $3{,}5$, die Mitte der sechs Werte (Abb. [8](#abb-8)). Für den gleichmäßig verteilten Eintreffzeitpunkt aus Unterabschnitt [6.4](zufallsvariablen-und-verteilungen.html#stufe-6-4) ist $\mathbb{E}[T]=\int_0^{0{,}5}t\cdot2\,\mathrm{d} t=\bigl[t^2\bigr]_0^{0{,}5}=0{,}25\,\mathrm s$, die Mitte des Intervalls.

:::abbildung ml/k4rwuerfel 8
Der Erwartungswert eines fairen Würfels: Jede Augenzahl mit der Wahrscheinlichkeit $\tfrac16$ gewichtet und summiert.
:::
::::

⁠**Kurz gesagt:** Der Erwartungswert ist der mit den Wahrscheinlichkeiten gewichtete Mittelwert der Werte, der Schwerpunkt der Verteilung; bei endlich vielen Werten ist er das Skalarprodukt $\mathbf{v}^{\top}\mathbf{p}$.

### Der Erwartungswert einer Funktion

<span class="anker" id="stufe-7-2"></span>

Oft braucht man den Erwartungswert einer Größe, die aus $X$ berechnet wird: der Fläche $X^2$ eines Quadrats mit der zufälligen Seitenlänge $X$ oder des Gewinns $g(X)$ bei einem Spiel. $g(X)$ ist wieder eine Zufallsvariable, man könnte also erst ihre Verteilung bestimmen. Das ist unnötig: Jeder Wert $x_k$ von $X$ liefert den Wert $g(x_k)$ mit derselben Wahrscheinlichkeit.

:::satz Satz 7.2 (Erwartungswert einer Funktion)
<span class="anker" id="satz-7-2"></span>

Für eine Funktion $g$ ist

<span class="anker" id="gl-7-4"></span>
$$\mathbb{E}[g(X)]=\sum_kg(x_k)\,P(X=x_k)\qquad\text{bzw.}\qquad \mathbb{E}[g(X)]=\int_{-\infty}^\infty g(x)\,p(x)\,\mathrm{d} x . \tag{7.4}$$
:::

Im diskreten Fall fasst man dafür in [(7.1)](#gl-7-1) für $g(X)$ alle $x_k$ mit demselben Wert $g(x_k)$ zusammen; ihre Wahrscheinlichkeiten addieren sich zur Wahrscheinlichkeit dieses Werts. Im stetigen Fall gilt die Formel ebenso, der Beweis braucht aber mehr Integralrechnung.

::::beispiel [Rechenbeispiel]
Für den fairen Würfel ist $\mathbb{E}[X^2]=\tfrac{91}6\approx15{,}17$ (Abb. [9](#abb-9)): Die quadrierten Augenzahlen $1,4,\dots,36$ werden mit je $\tfrac16$ gewichtet.

:::abbildung ml/k4rquadrat 9
Der Erwartungswert des Quadrats der Augenzahl: Die Werte werden erst quadriert, dann mit ihren Wahrscheinlichkeiten gewichtet.
:::
::::

:::warnung Erwartungswert der Funktion ist nicht Funktion des Erwartungswerts
Es ist $\mathbb{E}[X^2]=\tfrac{91}6\approx15{,}17$, aber $(\mathbb{E}[X])^2=3{,}5^2=12{,}25$. Im Allgemeinen ist $\mathbb{E}[g(X)]\ne g(\mathbb{E}[X])$. Gleichheit gilt für Funktionen der Form $g(x)=ax+b$, wie der nächste Unterabschnitt zeigt.
:::

⁠**Kurz gesagt:** Den Erwartungswert von $g(X)$ berechnet man, indem man die Werte $g(x_k)$ mit den Wahrscheinlichkeiten der $x_k$ gewichtet; er ist im Allgemeinen nicht $g(\mathbb{E}[X])$.

### Die Linearität des Erwartungswerts

<span class="anker" id="stufe-7-3"></span>

Rechnet man ein Gewicht von Kilogramm in Gramm um oder addiert einen festen Versatz, so sollte sich der Erwartungswert genauso ändern. Und der Erwartungswert einer Summe sollte die Summe der Erwartungswerte sein, wie beim Durchschnitt von Zahlenlisten. Beides gilt, und das Zweite sogar ohne jede Voraussetzung über das Zusammenspiel der Summanden.

Für zwei Zufallsvariablen $X$ und $Y$ auf demselben Ergebnisraum ist $X+Y$ die Zufallsvariable mit dem Wert $X(\omega)+Y(\omega)$ beim Ergebnis $\omega$.

:::satz Satz 7.3 (Linearität)
<span class="anker" id="satz-7-3"></span>

Für Zufallsvariablen $X$, $Y$ mit Erwartungswerten und Zahlen $a$, $b$ gilt

<span class="anker" id="gl-7-5"></span>
$$\mathbb{E}[aX+b]=a\,\mathbb{E}[X]+b,\qquad \mathbb{E}[X+Y]=\mathbb{E}[X]+\mathbb{E}[Y]. \tag{7.5}$$
:::

:::beweis Linearität bei endlichem Ergebnisraum
Fasst man in [(7.1)](#gl-7-1) die Ergebnisse nach dem Wert von $X$ zusammen und löst die Gruppen wieder auf, so ist $\mathbb{E}[X]=\sum_{\omega\in\Omega}X(\omega)\,P(\{\omega\})$. In dieser Form ist der Erwartungswert ein Skalarprodukt mit festem Gewichtsvektor $\bigl(P(\{\omega\})\bigr)_\omega$ und deshalb linear: $\mathbb{E}[X+Y]=\sum_\omega\bigl(X(\omega)+Y(\omega)\bigr)P(\{\omega\})=\mathbb{E}[X]+\mathbb{E}[Y]$. Ebenso ist $\mathbb{E}[aX+b]=a\sum_\omega X(\omega)P(\{\omega\})+b\sum_\omega P(\{\omega\})=a\,\mathbb{E}[X]+b$. Für allgemeine Zufallsvariablen gilt dasselbe, weil Summen und Integrale linear sind.
:::

Mit vielen Summanden ist $\mathbb{E}[X_1+\dots+X_n]=\mathbb{E}[X_1]+\dots+\mathbb{E}[X_n]$. Besonders nützlich ist das mit Zählvariablen. Die __Indikatorvariable__ eines Ereignisses $A$ ist die Zufallsvariable $\mathbb 1_A$ mit dem Wert $1$, wenn $A$ eintritt, und $0$ sonst. Ihr Erwartungswert ist $\mathbb{E}[\mathbb 1_A]=0\cdot P(A^{\mathrm c})+1\cdot P(A)=P(A)$. Eine Anzahl ist eine Summe von Indikatorvariablen, also ist ihr Erwartungswert die Summe der Wahrscheinlichkeiten.

::::beispiel [Rechenbeispiel]
Die Augensumme zweier Würfel hat den Erwartungswert $3{,}5+3{,}5=7$, ohne dass man die $36$ Paare durchgehen muss. Die Anzahl der Köpfe bei drei Münzwürfen ist $X=\mathbb 1_{A_1}+\mathbb 1_{A_2}+\mathbb 1_{A_3}$ mit $A_k$ = „Wurf $k$ zeigt Kopf“, also ist $\mathbb{E}[X]=3\cdot\tfrac12=1{,}5$, wie in Abb. [7](#abb-7). Für ein Gewicht $X$ in Kilogramm mit $\mathbb{E}[X]=0{,}25\,\mathrm{kg}$ hat die Angabe $1\,000\,X$ in Gramm den Erwartungswert $250\,\mathrm g$.
::::

⁠**Kurz gesagt:** Der Erwartungswert ist linear: Er vertauscht mit Vielfachen, Verschiebungen und Summen, auch wenn die Summanden voneinander abhängen.

### Varianz und Standardabweichung

<span class="anker" id="stufe-7-4"></span>

Zwei Waagen können denselben Erwartungswert liefern und trotzdem verschieden gut sein: Das eine streut eng um ihn, das andere weit. Man möchte messen, wie weit die Werte typischerweise von $\mu=\mathbb{E}[X]$ abweichen. Der Erwartungswert der Abweichung selbst taugt dazu nicht, denn nach der Linearität ist $\mathbb{E}[X-\mu]=\mu-\mu=0$: Positive und negative Abweichungen heben sich immer auf. Man quadriert deshalb, wie bei der Standardabweichung eines Datensatzes in [Grundlagen 1, Abschnitt 4.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-4).

:::definition Definition 7.4 (Varianz, Standardabweichung)
<span class="anker" id="satz-7-4"></span>

Die __Varianz__ einer Zufallsvariablen $X$ mit dem Erwartungswert $\mu$ ist

<span class="anker" id="gl-7-6"></span>
$$\operatorname{Var}(X)=\mathbb{E}\bigl[(X-\mu)^2\bigr]. \tag{7.6}$$

Ihre __Standardabweichung__ ist $\sigma=\sqrt{\operatorname{Var}(X)}$. Man schreibt auch $\sigma^2$ oder $\sigma_X^2$ für die Varianz.
:::

Die Varianz hat das Quadrat der Einheit von $X$, die Standardabweichung dieselbe Einheit wie $X$. Die Varianz ist nie negativ, und sie ist genau dann null, wenn $X$ mit Wahrscheinlichkeit $1$ den Wert $\mu$ hat. In [Grundlagen 3](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/ableitung-gradient-und-kettenregel.html) bezeichnete $\sigma$ die logistische Funktion; in diesem Kapitel steht $\sigma$ immer für eine Standardabweichung.

Ist $\mu=0$, etwa beim Fehler einer Waage, die im Mittel richtig anzeigt, so ist $\operatorname{Var}(X)=\mathbb{E}[X^2]$ der Erwartungswert des Quadrats, und $\sigma=\sqrt{\mathbb{E}[X^2]}$ ist das Gegenstück zum quadratischen Mittelwert aus [Grundlagen 1, Abschnitt 3.6](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-6). Deshalb ist die Varianz die natürliche Kenngröße für zufällige Fehler: Sie sagt, wie groß ihr Quadrat im Mittel ist.

::::beispiel [Rechenbeispiel]
Beim fairen Würfel mit $\mu=3{,}5$ weichen die Augenzahlen um $2{,}5$, $1{,}5$ und $0{,}5$ nach links und nach rechts vom Erwartungswert ab. Ihre Quadrate, mit je $\tfrac16$ gewichtet, ergeben $\operatorname{Var}(X)=\tfrac{35}{12}\approx2{,}917$ (Abb. [10](#abb-10)) und $\sigma=\sqrt{35/12}\approx1{,}708$. Für die Anzahl der Köpfe mit $\mu=1{,}5$ ist $\operatorname{Var}(X)=2{,}25\cdot\tfrac18+0{,}25\cdot\tfrac38+0{,}25\cdot\tfrac38+2{,}25\cdot\tfrac18=0{,}75$ und $\sigma\approx0{,}866$.

:::abbildung ml/k4rvarianz 10
Die Varianz eines fairen Würfels: die quadrierten Abweichungen vom Erwartungswert $3{,}5$, gewichtet mit den Wahrscheinlichkeiten.
:::
::::

⁠**Kurz gesagt:** Die Varianz ist der Erwartungswert der quadrierten Abweichung vom Erwartungswert, die Standardabweichung ihre Wurzel; bei $\mu=0$ ist die Varianz das mittlere Quadrat.

### Die Verschiebungsformel

<span class="anker" id="stufe-7-5"></span>

Für Rechnungen von Hand gibt es eine zweite Form der Varianz, die ohne die Abweichungen auskommt.

:::satz Satz 7.5 (Verschiebungsformel)
<span class="anker" id="satz-7-5"></span>

<span class="anker" id="gl-7-7"></span>
$$\operatorname{Var}(X)=\mathbb{E}[X^2]-\bigl(\mathbb{E}[X]\bigr)^2 . \tag{7.7}$$
:::

:::beweis Verschiebungsformel
Mit $\mu=\mathbb{E}[X]$ ist $(X-\mu)^2=X^2-2\mu X+\mu^2$. Nach der Linearität ist $\mathbb{E}\bigl[(X-\mu)^2\bigr]=\mathbb{E}[X^2]-2\mu\,\mathbb{E}[X]+\mu^2=\mathbb{E}[X^2]-2\mu^2+\mu^2=\mathbb{E}[X^2]-\mu^2$.
:::

Weil die Varianz nie negativ ist, folgt $\mathbb{E}[X^2]\ge(\mathbb{E}[X])^2$, mit Gleichheit nur, wenn $X$ fest ist. Aus der Mechanik kennt man dieselbe Rechnung als Satz von Steiner: Denkt man sich die Wahrscheinlichkeiten als Massen auf einem Stab, so ist $\mathbb{E}[X^2]$ das Trägheitsmoment um den Nullpunkt, $\operatorname{Var}(X)$ das Trägheitsmoment um den Schwerpunkt $\mu$, und der Unterschied ist Gesamtmasse $1$ mal Abstand $\mu$ zum Quadrat. Für die Zahlen eines Datensatzes ist das die Zerlegung $\operatorname{rms}(\mathbf{v})^2=\bar v^2+\operatorname{std}(\mathbf{v})^2$ aus [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) (Aufgabe [21](#aufg-21)).

::::beispiel [Rechenbeispiel]
Für den fairen Würfel ist mit Abb. [9](#abb-9) $\operatorname{Var}(X)=\tfrac{91}6-\tfrac{49}4=\tfrac{182-147}{12}=\tfrac{35}{12}$, wie in Abb. [10](#abb-10). Für die Anzahl der Köpfe ist $\mathbb{E}[X^2]=0\cdot\tfrac18+1\cdot\tfrac38+4\cdot\tfrac38+9\cdot\tfrac18=3$ und $\operatorname{Var}(X)=3-1{,}5^2=0{,}75$.
::::

:::warnung Auslöschung
Liegen die Werte von $X$ dicht beieinander und weit weg von null, so sind $\mathbb{E}[X^2]$ und $(\mathbb{E}[X])^2$ zwei große, fast gleiche Zahlen. Nach [Grundlagen 3, Abschnitt 11.3](/wissen/informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel/numerische-ableitung-und-gradientenprufung.html#stufe-11-3), verliert man beim Abziehen solcher Zahlen fast alle richtigen Stellen. Ein Beispiel: $X$ habe die Werte $10^8+1$ und $10^8+3$ mit je der Wahrscheinlichkeit $\tfrac12$. Die Varianz ist $1$, denn die Werte liegen je $1$ vom Erwartungswert $10^8+2$ entfernt. In doppelter Genauigkeit gerechnet liefert [(7.7)](#gl-7-7) aber $0$: Beide Terme sind etwa $10^{16}$, und der Unterschied von $1$ geht in der Rundung unter. Für Rechnungen am Computer benutzt man deshalb die Definition [(7.6)](#gl-7-6) und bildet zuerst die Abweichungen.
:::

⁠**Kurz gesagt:** Die Varianz ist der Erwartungswert des Quadrats minus das Quadrat des Erwartungswerts; von Hand bequem, am Rechner bei großen, eng beieinanderliegenden Werten ungenau.

### Umrechnen und Standardisieren

<span class="anker" id="stufe-7-6"></span>

Rechnet man eine Temperatur von Grad Celsius in Grad Fahrenheit um, so verschiebt sich der Erwartungswert und die Streuung wird gestreckt. Die Verschiebung ändert die Streuung nicht, denn sie verschiebt alle Werte und den Erwartungswert gleich. Die Streckung multipliziert alle Abweichungen mit dem Faktor, ihre Quadrate also mit dem Quadrat des Faktors.

:::satz Satz 7.6 (Varianz unter linearer Umrechnung)
<span class="anker" id="satz-7-6"></span>

Für Zahlen $a$ und $b$ gilt

<span class="anker" id="gl-7-8"></span>
$$\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X),\qquad \sigma_{aX+b}=|a|\,\sigma_X . \tag{7.8}$$
:::

Denn nach der Linearität ist $\mathbb{E}[aX+b]=a\mu+b$, also $(aX+b)-(a\mu+b)=a\,(X-\mu)$, und das Quadrat davon ist $a^2(X-\mu)^2$. Wählt man $a=1/\sigma$ und $b=-\mu/\sigma$, so erhält man eine Zufallsvariable mit dem Erwartungswert $0$ und der Varianz $1$.

:::definition Definition 7.7 (Standardisierte Zufallsvariable)
<span class="anker" id="satz-7-7"></span>

Für eine Zufallsvariable $X$ mit dem Erwartungswert $\mu$ und der Standardabweichung $\sigma>0$ heißt

<span class="anker" id="gl-7-9"></span>
$$Z=\frac{X-\mu}{\sigma} \tag{7.9}$$

die __standardisierte__ Zufallsvariable. Es ist $\mathbb{E}[Z]=0$ und $\operatorname{Var}(Z)=1$.
:::

Das ist dieselbe Rechnung wie das Standardisieren eines Merkmals in [Grundlagen 1, Abschnitt 4.5](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-5), nur mit Erwartungswert und Standardabweichung der Verteilung statt Mittelwert und Standardabweichung der Daten. $Z$ hat keine Einheit und misst die Abweichung vom Erwartungswert in Vielfachen der Standardabweichung.

::::beispiel [Rechenbeispiel]
Eine Temperatur $X$ in Grad Celsius habe $\mu=20$ und $\sigma=2$. In Grad Fahrenheit ist $Y=1{,}8\,X+32$ mit $\mathbb{E}[Y]=1{,}8\cdot20+32=68$ und $\sigma_Y=1{,}8\cdot2=3{,}6$. Ein Wert von $24\,{}^\circ\mathrm C$ hat standardisiert $z=(24-20)/2=2$; derselbe Wert in Fahrenheit, $75{,}2$, hat $z=(75{,}2-68)/3{,}6=2$. Die standardisierte Größe hängt nicht von der Einheit ab.
::::

⁠**Kurz gesagt:** Verschieben ändert die Varianz nicht, Strecken um $a$ multipliziert sie mit $a^2$; Standardisieren macht aus jeder Zufallsvariablen eine mit Erwartungswert $0$ und Varianz $1$.

### Mittelwert der Daten und Erwartungswert

<span class="anker" id="stufe-7-7"></span>

[Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) hat für die Flächen der vier Wohnungen $60$, $40$, $90$ und $70\,\mathrm m^2$ den Mittelwert $65\,\mathrm m^2$ und die Standardabweichung $\sqrt{325}\approx18{,}03\,\mathrm m^2$ berechnet. Dieses Kapitel hat den Erwartungswert und die Standardabweichung einer Zufallsvariablen eingeführt. Die Formeln sehen ähnlich aus. Hängen die Begriffe zusammen?

Ein Zusammenhang ist genau. Man ziehe aus dem Datensatz eine Zeile rein zufällig, jede mit der Wahrscheinlichkeit $1/N$, und nenne ihren Wert $X$. Dann ist nach [(7.1)](#gl-7-1)

$$\mathbb{E}[X]=\sum_{i=1}^Nv_i\cdot\frac1N=\bar v,\qquad \operatorname{Var}(X)=\sum_{i=1}^N(v_i-\bar v)^2\cdot\frac1N=\operatorname{std}(\mathbf{v})^2 .$$

Die Verteilung, die jedem Datenpunkt die Wahrscheinlichkeit $1/N$ gibt, heißt __empirische Verteilung__ des Datensatzes. Mittelwert und Standardabweichung eines Datensatzes sind Erwartungswert und Standardabweichung seiner empirischen Verteilung. Dass [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) durch $N$ teilt, passt genau dazu.

Der wichtigere Unterschied liegt woanders. Die vier Wohnungen sind eine Auswahl aus allen Wohnungen einer Stadt. Man kann sich die Fläche einer zufällig gewählten Wohnung der Stadt als Zufallsvariable vorstellen; ihr Erwartungswert ist eine feste, meist unbekannte Zahl. Der Mittelwert $65\,\mathrm m^2$ hängt dagegen davon ab, welche vier Wohnungen zufällig in den Datensatz gekommen sind. Eine andere Auswahl hätte einen anderen Mittelwert ergeben. Wie nahe der Mittelwert dem Erwartungswert kommt und wie das von der Zahl der Datenpunkte abhängt, beantwortet Abschnitt [13](mittelwerte-vieler-zufallsvariablen.html#stufe-13).

|  | Mittelwert eines Datensatzes | Erwartungswert einer Zufallsvariablen |
|---|---|---|
| Zeichen | $\bar v$, $\bar{\mathbf{x}}$; Standardabweichung $\operatorname{std}(\mathbf{v})$, $s_j$ | $\mathbb{E}[X]$, $\mu$; Standardabweichung $\sigma$ |
| berechnet aus | den $N$ Zahlen des Datensatzes | der Verteilung von $X$ |
| hängt vom Zufall ab | ja: andere Auswahl, anderer Wert | nein: eine feste Zahl |
| Zusammenhang | ist der Erwartungswert der empirischen Verteilung | wird vom Mittelwert vieler unabhängiger Werte angenähert (Abschnitt [13](mittelwerte-vieler-zufallsvariablen.html#stufe-13)) |

::::beispiel [Rechenbeispiel]
Für die vier Flächen hat die empirische Verteilung die Werte $60$, $40$, $90$, $70$ mit je der Wahrscheinlichkeit $\tfrac14$, also den Erwartungswert $\tfrac14\cdot260=65$ und die Varianz $\tfrac14\,(25+625+625+25)=325$, wie in [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html). Hätte der Datensatz statt der zweiten Wohnung eine mit $80\,\mathrm m^2$ enthalten, so wäre der Mittelwert $75\,\mathrm m^2$. Am Erwartungswert der Fläche aller Wohnungen der Stadt ändert das nichts.
::::

⁠**Kurz gesagt:** Mittelwert und Standardabweichung eines Datensatzes sind Erwartungswert und Standardabweichung seiner empirischen Verteilung; als Aussage über die Verteilung, aus der die Daten stammen, sind sie selbst zufällig.

:::hintergrund Median und Modus
Der Erwartungswert ist nicht die einzige Art, die Mitte einer Verteilung anzugeben. Der __Median__ ist ein Wert $m$ mit $P(X\le m)\ge\tfrac12$ und $P(X\ge m)\ge\tfrac12$: Die Hälfte der Wahrscheinlichkeit liegt links, die Hälfte rechts. Der __Modus__ ist ein Wert mit der größten Wahrscheinlichkeit oder der größten Dichte. Bei symmetrischen Verteilungen mit einem Gipfel fallen alle drei zusammen. Bei schiefen Verteilungen nicht: Einkommen haben einen Median weit unter dem Erwartungswert, weil wenige sehr hohe Einkommen den Schwerpunkt nach rechts ziehen, den Median aber kaum bewegen. Der Median ist deshalb robust gegen Ausreißer. Eine Verteilung mit zwei Gipfeln, etwa die Messwerte zweier verschieden eingestellter Maschinen in einer Kiste, hat zwei Modi, und ihr Erwartungswert liegt womöglich in einem Tal, in dem kaum Werte vorkommen. Ein Modus einer Dichte hat noch eine Schwäche: Rechnet man die Größe nichtlinear um, etwa von einer Länge in ihr Quadrat, so verschiebt sich die Lage des Gipfels, weil sich die Dichte dabei verzerrt.
:::

:::aufgabe Aufgabe 18 ★ Das Maximum zweier Würfel
<span class="anker" id="aufg-18"></span>

Zwei faire Würfel werden geworfen, $M$ sei die größere der beiden Augenzahlen.

<ol class="al">

<li>

Zeige $P(M=k)=(2k-1)/36$ für $k=1,\dots,6$.

</li>

<li>

Berechne $\mathbb{E}[M]$, $\mathbb{E}[M^2]$ und $\operatorname{Var}(M)$.

</li>

</ol>

:::loesung
(a) $M\le k$ heißt, beide Würfel zeigen höchstens $k$; das sind $k^2$ Paare. Also ist $P(M=k)=P(M\le k)-P(M\le k-1)=\frac{k^2-(k-1)^2}{36}=\frac{2k-1}{36}$.

(b)

$$\begin{aligned} \mathbb{E}[M]&=\frac{1\cdot1+2\cdot3+3\cdot5+4\cdot7+5\cdot9+6\cdot11}{36}=\frac{161}{36}\approx4{,}472,\\ \mathbb{E}[M^2]&=\frac{1\cdot1+4\cdot3+9\cdot5+16\cdot7+25\cdot9+36\cdot11}{36}=\frac{791}{36}\approx21{,}97, \end{aligned}$$

und $\operatorname{Var}(M)=\tfrac{791}{36}-\bigl(\tfrac{161}{36}\bigr)^2=\tfrac{28\,476-25\,921}{1\,296}=\tfrac{2\,555}{1\,296}\approx1{,}971$. Das Maximum liegt im Mittel fast einen Punkt über $3{,}5$ und streut weniger als ein einzelner Würfel.
:::
:::

:::aufgabe Aufgabe 19 ★★ Ein Wetterbericht mit vier Stufen
<span class="anker" id="aufg-19"></span>

Ein Wetterbericht meldet für den nächsten Tag eine von vier Windstufen $0,1,2,3$ mit den Wahrscheinlichkeiten $0{,}1$, $0{,}3$, $0{,}4$ und $0{,}2$.

<ol class="al">

<li>

Berechne den Erwartungswert als Skalarprodukt $\mathbf{v}^{\top}\mathbf{p}$.

</li>

<li>

Berechne die Varianz einmal nach der Definition und einmal nach der Verschiebungsformel.

</li>

<li>

Ein Fahrradkurier verlangt bei der Windstufe $X$ den Preis $U=0{,}5\,\text{Euro}\cdot X+1\,\text{Euro}$ je Kilometer. Gib Erwartungswert und Standardabweichung von $U$ an.

</li>

</ol>

:::loesung
(a) $\mathbb{E}[X]=(0,\,1,\,2,\,3)(0{,}1;\ 0{,}3;\ 0{,}4;\ 0{,}2)^{\top}=0+0{,}3+0{,}8+0{,}6=1{,}7$.

(b) Nach der Definition: $2{,}89\cdot0{,}1+0{,}49\cdot0{,}3+0{,}09\cdot0{,}4+1{,}69\cdot0{,}2=0{,}289+0{,}147+0{,}036+0{,}338=0{,}81$. Nach der Verschiebungsformel: $\mathbb{E}[X^2]=0+0{,}3+1{,}6+1{,}8=3{,}7$ und $3{,}7-1{,}7^2=0{,}81$. Also $\sigma=0{,}9$.

(c) $\mathbb{E}[U]=0{,}5\cdot1{,}7+1=1{,}85$ Euro und $\sigma_U=0{,}5\cdot0{,}9=0{,}45$ Euro je Kilometer.
:::
:::

:::aufgabe Aufgabe 20 ★★ Briefe in Umschlägen
<span class="anker" id="aufg-20"></span>

$n$ Briefe werden zufällig auf $n$ adressierte Umschläge verteilt, jede Zuordnung gleich wahrscheinlich. $X$ sei die Anzahl der Briefe im richtigen Umschlag.

<ol class="al">

<li>

Wie wahrscheinlich landet Brief $i$ im richtigen Umschlag?

</li>

<li>

Zeige mit Indikatorvariablen, dass $\mathbb{E}[X]=1$ für jedes $n$. Warum darf man die Linearität benutzen, obwohl die Ereignisse „Brief $i$ richtig“ voneinander abhängen?

</li>

<li>

Prüfe das Ergebnis für $n=3$, indem du alle sechs Zuordnungen aufschreibst.

</li>

</ol>

:::loesung
(a) Jeder der $n$ Umschläge ist für Brief $i$ gleich wahrscheinlich, also $\tfrac1n$.

(b) Mit $A_i$ = „Brief $i$ im richtigen Umschlag“ ist $X=\sum_i\mathbb 1_{A_i}$ und $\mathbb{E}[X]=n\cdot\tfrac1n=1$. Die Linearität des Erwartungswerts gilt ohne jede Voraussetzung über das Zusammenspiel der Summanden; der Beweis in Unterabschnitt [7.3](#stufe-7-3) benutzt nur, dass der Erwartungswert eine gewichtete Summe mit festen Gewichten ist. Die Abhängigkeit, etwa dass bei $n-1$ richtigen Briefen auch der letzte richtig ist, würde erst bei der Varianz eine Rolle spielen.

(c) Die sechs Zuordnungen haben $3$ (die richtige), dreimal $1$ (zwei vertauscht) und zweimal $0$ (alle verschoben) richtige Briefe. Der Mittelwert ist $\tfrac{3+1+1+1+0+0}6=1$.
:::
:::

:::aufgabe Aufgabe 21 ★★★ Quadratischer Mittelwert und Verschiebungsformel
<span class="anker" id="aufg-21"></span>

In [Grundlagen 1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html) galt für einen Vektor $\mathbf{v}\in\mathbb{R}^N$ die Zerlegung $\operatorname{rms}(\mathbf{v})^2=\bar v^2+\operatorname{std}(\mathbf{v})^2$.

<ol class="al">

<li>

Zeige, dass das die Verschiebungsformel [(7.7)](#gl-7-7) für die empirische Verteilung der Komponenten von $\mathbf{v}$ ist.

</li>

<li>

Deute die Zerlegung für die Tagestemperaturen eines Monats: Was beschreibt $\operatorname{rms}^2$, was $\bar v^2$, was $\operatorname{std}^2$? Warum kann ein Monat mit großem $\operatorname{rms}$ trotzdem sehr gleichmäßiges Wetter gehabt haben?

</li>

<li>

Prüfe die Zerlegung für $\mathbf{v}=(1,\,3,\,1,\,-1)^{\top}$.

</li>

</ol>

:::loesung
(a) Für die empirische Verteilung mit $P(X=v_i)=\tfrac1N$ ist $\mathbb{E}[X^2]=\tfrac1N\sum v_i^2=\operatorname{rms}(\mathbf{v})^2$, $\mathbb{E}[X]=\bar v$ und $\operatorname{Var}(X)=\operatorname{std}(\mathbf{v})^2$. Die Verschiebungsformel $\mathbb{E}[X^2]=\operatorname{Var}(X)+(\mathbb{E}[X])^2$ lautet dann $\operatorname{rms}(\mathbf{v})^2=\operatorname{std}(\mathbf{v})^2+\bar v^2$.

(b) $\operatorname{rms}^2$ ist das mittlere Quadrat der Temperaturen, $\bar v^2$ das Quadrat der Durchschnittstemperatur und $\operatorname{std}^2$ das mittlere Quadrat der Abweichungen vom Durchschnitt, also wie stark das Wetter von Tag zu Tag schwankt. Die beiden Teile addieren sich, weil die Abweichungen im Mittel null sind und das gemischte Glied deshalb verschwindet. Ein großes $\operatorname{rms}$ kann allein von einer hohen Durchschnittstemperatur kommen: Ein Monat mit jeden Tag genau $25$ Grad hat $\operatorname{rms}=25$, aber $\operatorname{std}=0$.

(c) $\bar v=1$, $\operatorname{rms}^2=\tfrac{1+9+1+1}4=3$ und $\operatorname{std}^2=\tfrac{0+4+0+4}4=2$; tatsächlich ist $3=1+2$.
:::
:::
