---
title: Mehrere Zufallsvariablen
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
knoten: Grundlagen 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15241000
summary: Ein Datenpunkt besteht aus mehreren Zahlen, die vom selben Zufall abhängen: Fläche und Miete derselben Wohnung, zwei Abtastwerte desselben Signals.
tags: Doppelintegral, gemeinsame Wahrscheinlichkeitsfunktion, gemeinsame Dichte, Randverteilung, marginalisiert, bedingte Verteilung, bedingte Dichte, bedingter Erwartungswert
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Ein Datenpunkt besteht aus mehreren Zahlen, die vom selben Zufall abhängen: Fläche und Miete derselben Wohnung, zwei Abtastwerte desselben Signals. Dieser Abschnitt beschreibt mehrere Zufallsvariablen zugleich durch ihre gemeinsame Verteilung, gewinnt daraus die Verteilungen der einzelnen und die bedingten Verteilungen und überträgt die Unabhängigkeit von Ereignissen auf Zufallsvariablen. Am Ende steht die Vorstellung, mit der das maschinelle Lernen einen Datensatz beschreibt: als viele unabhängige Ziehungen aus derselben Verteilung.
:::

### Was du dafür brauchst: Doppelintegrale

<span class="anker" id="stufe-9-1"></span>

Für zwei stetig verteilte Größen braucht man Integrale über Flächen. Für eine Funktion $f(x,y)\ge0$ auf einem Rechteck $[a,\,b]\times[c,\,d]$ ist das __Doppelintegral__ $\iint f(x,y)\,\mathrm{d} x\,\mathrm{d} y$ das Volumen zwischen der Fläche $z=f(x,y)$ und der Ebene $z=0$. Man berechnet es als zwei gewöhnliche Integrale nacheinander: zuerst über $y$ bei festem $x$, dann über $x$,

$$\iint_{[a,b]\times[c,d]}f(x,y)\,\mathrm{d} x\,\mathrm{d} y=\int_a^b\Bigl(\int_c^df(x,y)\,\mathrm{d} y\Bigr)\mathrm{d} x .$$

Das innere Integral ist die Fläche eines Schnitts bei festem $x$; summiert man die Schnittflächen mal ihrer Dicke $\mathrm{d} x$, erhält man das Volumen. Für stetige Funktionen ist die Reihenfolge gleichgültig. Ist $f(x,y)=g(x)\,h(y)$ ein Produkt, so zerfällt das Doppelintegral in das Produkt $\int g\,\mathrm{d} x\cdot\int h\,\mathrm{d} y$.

⁠**Rechenbeispiel:** Für $f(x,y)=x+y$ auf $[0,\,1]\times[0,\,1]$ ist das innere Integral $\int_0^1(x+y)\,\mathrm{d} y=x+\tfrac12$ und das äußere $\int_0^1(x+\tfrac12)\,\mathrm{d} x=\tfrac12+\tfrac12=1$.

⁠**Kurz gesagt:** Ein Doppelintegral ist ein Volumen; man rechnet es als zwei gewöhnliche Integrale nacheinander aus.

### Die gemeinsame Verteilung

<span class="anker" id="stufe-9-2"></span>

Die Zähltabelle aus Unterabschnitt [3.1](bedingte-wahrscheinlichkeit.html#stufe-3-1) lässt sich mit zwei Zufallsvariablen beschreiben: $S=1$, wenn die Sonne scheint, sonst $0$, und $R=1$, wenn die Person Rad fährt, sonst $0$. Die vier Zellen sind die Wahrscheinlichkeiten der vier Wertepaare. Diese Angabe beschreibt beide Größen zusammen vollständig.

:::definition Definition 9.1 (Gemeinsame Verteilung)
<span class="anker" id="satz-9-1"></span>

Für zwei diskrete Zufallsvariablen $X$ und $Y$ heißt die Zuordnung $(x,y)\mapsto P(X=x,\,Y=y)$ ihre __gemeinsame Wahrscheinlichkeitsfunktion__; dabei steht das Komma für „und“. Zwei Zufallsvariablen haben eine __gemeinsame Dichte__ $p(x,y)\ge0$, wenn für jeden Bereich $B$ der Ebene

<span class="anker" id="gl-9-1"></span>
$$P\bigl((X,Y)\in B\bigr)=\iint_Bp(x,y)\,\mathrm{d} x\,\mathrm{d} y . \tag{9.1}$$
:::

Die gemeinsame Wahrscheinlichkeitsfunktion summiert sich über alle Paare zu $1$, die gemeinsame Dichte hat das Volumen $1$. Eine gemeinsame Dichte ist eine Wahrscheinlichkeit pro Flächeneinheit; nach dem Muster von [(6.3)](zufallsvariablen-und-verteilungen.html#gl-6-3) ist $P(x\le X\le x+\Delta x,\ y\le Y\le y+\Delta y)\approx p(x,y)\,\Delta x\,\Delta y$.

⁠**Rechenbeispiel:** Aus Tabelle [1](bedingte-wahrscheinlichkeit.html#tab-1) ist $P(S=1,R=1)=0{,}3$, $P(S=1,R=0)=0{,}1$, $P(S=0,R=1)=0{,}1$ und $P(S=0,R=0)=0{,}5$. Stetig: $p(x,y)=x+y$ auf dem Einheitsquadrat und $0$ sonst ist eine gemeinsame Dichte, denn sie ist nichtnegativ und hat nach Unterabschnitt [9.1](#stufe-9-1) das Volumen $1$. Die Wahrscheinlichkeit, dass beide Größen höchstens $\tfrac12$ sind, ist $\int_0^{1/2}\!\int_0^{1/2}(x+y)\,\mathrm{d} y\,\mathrm{d} x=\int_0^{1/2}\bigl(\tfrac x2+\tfrac18\bigr)\mathrm{d} x=\tfrac1{16}+\tfrac1{16}=\tfrac18$.

⁠**Kurz gesagt:** Die gemeinsame Verteilung gibt für jede Kombination von Werten an, wie wahrscheinlich sie ist; diskret als Tabelle, stetig als Dichte über der Ebene.

### Randverteilungen

<span class="anker" id="stufe-9-3"></span>

Aus der gemeinsamen Verteilung erhält man die Verteilung jeder einzelnen Größe, wie in der Zähltabelle die Randsummen. Man fasst alle Werte der anderen Größe zusammen.

:::satz Satz 9.2 (Randverteilung)
<span class="anker" id="satz-9-2"></span>

Die __Randverteilung__ von $X$ ist

<span class="anker" id="gl-9-2"></span>
$$P(X=x)=\sum_yP(X=x,\,Y=y)\qquad\text{bzw.}\qquad p_X(x)=\int_{-\infty}^\infty p(x,y)\,\mathrm{d} y . \tag{9.2}$$
:::

Im diskreten Fall ist das die Summenregel aus Unterabschnitt [3.1](bedingte-wahrscheinlichkeit.html#stufe-3-1), denn die Ereignisse $\{Y=y\}$ zerlegen $\Omega$. Im stetigen Fall integriert man über alle $y$ einen Streifen der Breite $\Delta x$; das Integral über $y$ ergibt seine Wahrscheinlichkeit pro Breite. Man sagt, man __marginalisiert__ die andere Größe heraus. Die Randverteilungen allein legen die gemeinsame Verteilung nicht fest: Wie die Größen zusammenhängen, geht beim Summieren verloren. Bei vielen Größen wird das Marginalisieren teuer: Wer aus der gemeinsamen Verteilung von $30$ Ja-Nein-Größen die Randverteilung einer einzigen bestimmt, summiert für jeden ihrer beiden Werte über $2^{29}\approx5{,}4\cdot10^8$ Kombinationen der übrigen.

⁠**Rechenbeispiel:** $P(S=1)=0{,}3+0{,}1=0{,}4$ und $P(R=1)=0{,}3+0{,}1=0{,}4$. Für die Dichte $p(x,y)=x+y$ auf dem Einheitsquadrat ist $p_X(x)=\int_0^1(x+y)\,\mathrm{d} y=x+\tfrac12$ für $0\le x\le1$; ebenso ist $p_Y(y)=y+\tfrac12$.

⁠**Kurz gesagt:** Die Randverteilung einer Größe entsteht aus der gemeinsamen Verteilung, indem man über alle Werte der anderen Größe summiert oder integriert.

### Bedingte Verteilungen

<span class="anker" id="stufe-9-4"></span>

Kennt man den Wert einer Größe, so ändert sich, was man über die andere weiß. Weiß man, dass die Sonne scheint, so ist die Fahrradfahrt mit $0{,}75$ wahrscheinlich statt mit $0{,}4$. Das ist eine ganze Verteilung für $R$, eine für jeden Wert von $S$.

:::definition Definition 9.3 (Bedingte Verteilung)
<span class="anker" id="satz-9-3"></span>

Für $P(X=x)>0$ ist die __bedingte Verteilung__ von $Y$ gegeben $X=x$

<span class="anker" id="gl-9-3"></span>
$$P(Y=y\mid X=x)=\frac{P(X=x,\,Y=y)}{P(X=x)} . \tag{9.3}$$

Im stetigen Fall ist die __bedingte Dichte__ $p(y\mid x)=p(x,y)/p_X(x)$ für $p_X(x)>0$.
:::

Für festes $x$ ist das eine Verteilung in $y$: nichtnegativ und mit der Summe oder dem Integral $1$, denn der Nenner ist nach [(9.2)](#gl-9-2) genau die Summe des Zählers über $y$. Man nimmt aus der gemeinsamen Verteilung die Zeile oder den Schnitt bei $x$ und skaliert ihn auf die Gesamtwahrscheinlichkeit $1$. Umgestellt ergibt sich die Produktregel für Verteilungen, $p(x,y)=p(y\mid x)\,p_X(x)$. Der Erwartungswert einer bedingten Verteilung heißt __bedingter Erwartungswert__ und wird $\mathbb{E}[Y\mid X=x]$ geschrieben.

Bedingte Verteilungen sind die Sprache für Vorhersagen. Wer aus der Fläche einer Wohnung ihre Miete vorhersagen möchte, fragt nach der Verteilung der Miete gegeben die Fläche. Dass diese Verteilung im Allgemeinen nicht auf einem einzigen Wert sitzt, ist die fehlende Information aus „Worum es geht“: Gleiche Fläche, verschiedene Mieten.

⁠**Rechenbeispiel:** Die bedingte Verteilung von $R$ gegeben $S=1$ ist $P(R=1\mid S=1)=0{,}75$, $P(R=0\mid S=1)=0{,}25$; gegeben $S=0$ ist sie $\tfrac16$ und $\tfrac56$. Die bedingten Erwartungswerte sind $\mathbb{E}[R\mid S=1]=0{,}75$ und $\mathbb{E}[R\mid S=0]=\tfrac16$. Für die Dichte $x+y$ ist $p(y\mid x)=(x+y)/(x+\tfrac12)$ auf $[0,\,1]$. Bei $x=0$ ist das $2y$: Kleine $y$ sind dann selten, große häufig.

⁠**Kurz gesagt:** Die bedingte Verteilung von $Y$ gegeben $X=x$ ist der Schnitt der gemeinsamen Verteilung bei $x$, skaliert auf die Gesamtwahrscheinlichkeit $1$.

### Unabhängige Zufallsvariablen

<span class="anker" id="stufe-9-5"></span>

Zwei Zufallsvariablen sind unabhängig, wenn jede Aussage über die eine unabhängig von jeder Aussage über die andere ist. Dann ändert der Wert der einen nichts an der Verteilung der anderen, und die gemeinsame Verteilung ist das Produkt der Randverteilungen.

:::definition Definition 9.4 (Unabhängige Zufallsvariablen)
<span class="anker" id="satz-9-4"></span>

Zwei Zufallsvariablen $X$ und $Y$ heißen __unabhängig__, wenn für alle Zahlen $x$ und $y$ die Ereignisse $\{X\le x\}$ und $\{Y\le y\}$ unabhängig sind. Für diskrete Zufallsvariablen ist das gleichbedeutend mit

<span class="anker" id="gl-9-4"></span>
$$P(X=x,\,Y=y)=P(X=x)\,P(Y=y)\quad\text{für alle }x,y, \tag{9.4}$$

für stetig verteilte mit $p(x,y)=p_X(x)\,p_Y(y)$. Mehrere Zufallsvariablen heißen unabhängig, wenn ihre gemeinsame Verteilung in dieser Weise in das Produkt aller Randverteilungen zerfällt.
:::

Für unabhängige Zufallsvariablen ist die bedingte Verteilung gleich der Randverteilung, $P(Y=y\mid X=x)=P(Y=y)$. Daraus folgt eine Rechenregel für Produkte.

:::satz Satz 9.5 (Erwartungswert eines Produkts)
<span class="anker" id="satz-9-5"></span>

Sind $X$ und $Y$ unabhängig, so ist $\mathbb{E}[XY]=\mathbb{E}[X]\,\mathbb{E}[Y]$.
:::

Im diskreten Fall ist $\mathbb{E}[XY]=\sum_{x,y}xy\,P(X=x)P(Y=y)=\sum_xx\,P(X=x)\cdot\sum_yy\,P(Y=y)$, weil die Doppelsumme eines Produkts in das Produkt der Summen zerfällt. Ohne Unabhängigkeit gilt die Regel im Allgemeinen nicht.

⁠**Rechenbeispiel:** Für zwei faire Würfel ist $P(X=a,\,Y=b)=\tfrac1{36}=\tfrac16\cdot\tfrac16$ für alle Paare, also sind sie unabhängig, und $\mathbb{E}[XY]=3{,}5^2=12{,}25$. $S$ und $R$ sind abhängig, denn $P(S=1,R=1)=0{,}3\ne0{,}4\cdot0{,}4$. Dort ist $\mathbb{E}[SR]=P(S=1,R=1)=0{,}3$, aber $\mathbb{E}[S]\,\mathbb{E}[R]=0{,}16$. Die Dichte $x+y$ zerfällt nicht in eine Funktion von $x$ mal eine Funktion von $y$: $(x+\tfrac12)(y+\tfrac12)\ne x+y$, etwa bei $x=y=0$.

⁠**Kurz gesagt:** Unabhängige Zufallsvariablen haben als gemeinsame Verteilung das Produkt ihrer Randverteilungen; dann ist auch der Erwartungswert eines Produkts das Produkt der Erwartungswerte.

### Unabhängig und identisch verteilt

<span class="anker" id="stufe-9-6"></span>

Ein Datensatz entsteht oft so: Man wählt zufällig Wohnungen aus, misst wiederholt mit demselben Gerät oder prüft Teile aus einer laufenden Fertigung. Jede Zeile des Datensatzes ist dann das Ergebnis desselben Zufallsexperiments, und die Zeilen beeinflussen sich nicht. Diese Vorstellung ist die Grundannahme der meisten Verfahren, die aus Daten lernen.

:::definition Definition 9.6 (i.i.d., Stichprobe)
<span class="anker" id="satz-9-6"></span>

Zufallsvariablen $X_1,\dots,X_n$ heißen __unabhängig und identisch verteilt__, kurz __i.i.d.__ (vom englischen *independent and identically distributed*), wenn sie unabhängig sind und alle dieselbe Verteilung haben. Ihre Werte $x_1,\dots,x_n$ heißen eine __Stichprobe__ aus dieser Verteilung.
:::

Für Datenpunkte mit mehreren Merkmalen gilt dasselbe: Die Zeilen $\mathbf{x}_1,\dots,\mathbf{x}_N$ einer Datenmatrix sind in diesem Bild $N$ unabhängige Ziehungen aus derselben gemeinsamen Verteilung der Merkmale. Die Verteilung, aus der sie stammen, ist unbekannt; die Daten sind das Einzige, was man von ihr sieht. Das ist der genaue Sinn der Aussage, ein Datensatz sei eine zufällige Auswahl: Ein anderer Datensatz derselben Größe wäre eine andere Stichprobe aus derselben Verteilung.

Die Annahme ist nicht immer erfüllt, und man muss sie prüfen. Aufeinanderfolgende Abtastwerte eines Signals hängen meist voneinander ab, weil sich das Signal zwischen zwei Abtastzeitpunkten nur wenig ändert. Zehn Messungen an derselben Person sind sich ähnlicher als zehn Messungen an zehn Personen. Und wenn sich eine Fertigung im Lauf des Tages verstellt, sind die Teile vom Abend anders verteilt als die vom Morgen.

⁠**Rechenbeispiel:** Zehn Würfe eines fairen Würfels sind i.i.d. Jede bestimmte Folge, etwa $(3,1,4,1,5,6,2,6,5,3)$, hat die Wahrscheinlichkeit $(\tfrac16)^{10}\approx1{,}65\cdot10^{-8}$, weil die gemeinsame Wahrscheinlichkeitsfunktion das Produkt der zehn Randverteilungen ist. Zieht man aus dem Datensatz der vier Wohnungen mit Zurücklegen, jedes Mal jede Wohnung mit $\tfrac14$, so sind die Ziehungen i.i.d. mit der empirischen Verteilung aus Unterabschnitt [7.7](erwartungswert-und-varianz.html#stufe-7-7).

⁠**Kurz gesagt:** i.i.d. heißt unabhängig und mit derselben Verteilung; ein Datensatz wird als Stichprobe solcher Zufallsvariablen aufgefasst, aus einer unbekannten Verteilung.

:::aufgabe Aufgabe 26 ★ Erster Wurf und Gesamtzahl
<span class="anker" id="aufg-26"></span>

Eine faire Münze wird dreimal geworfen. $X$ sei $1$, wenn der erste Wurf Kopf zeigt, sonst $0$; $Y$ sei die Anzahl der Köpfe in allen drei Würfen.

<ol class="al">

<li>

Stelle die gemeinsame Wahrscheinlichkeitsfunktion als Tabelle auf und berechne die Randverteilungen.

</li>

<li>

Gib die bedingte Verteilung von $Y$ gegeben $X=1$ und den bedingten Erwartungswert $\mathbb{E}[Y\mid X=1]$ an.

</li>

<li>

Sind $X$ und $Y$ unabhängig?

</li>

</ol>

:::loesung
(a) Die acht Ergebnisse ergeben:

|  | $Y=0$ | $Y=1$ | $Y=2$ | $Y=3$ | Summe |
|---|---|---|---|---|---|
| $X=0$ | $\tfrac18$ | $\tfrac28$ | $\tfrac18$ | $0$ | $\tfrac12$ |
| $X=1$ | $0$ | $\tfrac18$ | $\tfrac28$ | $\tfrac18$ | $\tfrac12$ |
| Summe | $\tfrac18$ | $\tfrac38$ | $\tfrac38$ | $\tfrac18$ | $1$ |

Die Randverteilung von $Y$ ist $\mathrm{Bin}(3,\tfrac12)$, die von $X$ ist $\mathrm{Ber}(\tfrac12)$.

(b) Die Zeile $X=1$ geteilt durch $\tfrac12$: $P(Y=1\mid X=1)=\tfrac14$, $P(Y=2\mid X=1)=\tfrac12$, $P(Y=3\mid X=1)=\tfrac14$. $\mathbb{E}[Y\mid X=1]=\tfrac14+1+\tfrac34=2$: ein sicherer Kopf plus im Mittel einer aus den zwei übrigen Würfen.

(c) Nein: $P(X=1,Y=0)=0$, aber $P(X=1)P(Y=0)=\tfrac1{16}$.
:::
:::

:::aufgabe Aufgabe 27 ★★ Eine gemeinsame Dichte
<span class="anker" id="aufg-27"></span>

Es sei $p(x,y)=c\,xy$ für $0\le x\le1$, $0\le y\le2$ und $0$ sonst.

<ol class="al">

<li>

Bestimme $c$.

</li>

<li>

Berechne die Randdichten $p_X$ und $p_Y$. Sind $X$ und $Y$ unabhängig?

</li>

<li>

Berechne $P(X\le\tfrac12,\ Y\le1)$.

</li>

</ol>

:::loesung
(a) $\int_0^1\!\int_0^2c\,xy\,\mathrm{d} y\,\mathrm{d} x=c\int_0^1x\,\mathrm{d} x\int_0^2y\,\mathrm{d} y=c\cdot\tfrac12\cdot2=c$, also $c=1$.

(b) $p_X(x)=\int_0^2xy\,\mathrm{d} y=2x$ auf $[0,\,1]$ und $p_Y(y)=\int_0^1xy\,\mathrm{d} x=\tfrac y2$ auf $[0,\,2]$. Es ist $p_X(x)\,p_Y(y)=xy=p(x,y)$: unabhängig.

(c) Wegen der Unabhängigkeit ist $P(X\le\tfrac12,\ Y\le1)=\int_0^{1/2}2x\,\mathrm{d} x\cdot\int_0^1\tfrac y2\,\mathrm{d} y=\tfrac14\cdot\tfrac14=\tfrac1{16}$.
:::
:::

:::aufgabe Aufgabe 28 ★★ Ist das i.i.d.?
<span class="anker" id="aufg-28"></span>

Beurteile, ob die folgenden Datensätze sinnvoll als i.i.d. Stichprobe aufgefasst werden können, und begründe.

<ol class="al">

<li>

$1\,000$ Wohnungen, zufällig aus dem Melderegister einer Stadt gezogen.

</li>

<li>

$1\,000$ aufeinanderfolgende Abtastwerte eines Mikrofonsignals bei $48\,\mathrm{kHz}$.

</li>

<li>

Je zehn Blutdruckmessungen an $100$ Personen, als $1\,000$ Zeilen gespeichert.

</li>

<li>

Die Messwerte eines Sensors, einer pro Tag, über ein Jahr.

</li>

</ol>

:::loesung
(a) Ja, in guter Näherung. Die Ziehung ist zufällig, und bei einer großen Stadt ändert das Ziehen von $1\,000$ Wohnungen die Verteilung der übrigen kaum.

(b) Nein. Bei $48\,\mathrm{kHz}$ liegen zwei Abtastwerte $21\,\mu\mathrm s$ auseinander; in dieser Zeit ändert sich ein Schallsignal nur wenig, und benachbarte Werte sind stark korreliert. Außerdem decken $1\,000$ Werte nur etwa $21\,\mathrm{ms}$ ab.

(c) Nein. Die zehn Messungen derselben Person hängen voneinander ab, weil sie den Blutdruck dieser Person messen. Unabhängig sind eher die $100$ Personen untereinander; jede Person ist dann ein Datenpunkt mit zehn Messungen.

(d) Nur eingeschränkt. Messwerte im Abstand eines Tages können durch das Wetter, die Jahreszeit oder eine langsame Drift des Sensors zusammenhängen; im Sommer sind sie anders verteilt als im Winter. Man müsste prüfen, ob es solche Abhängigkeiten gibt.
:::
:::
