---
title: Das Skalarprodukt
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Vektoren und Matrizen
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: Kapitel 1: Vektoren und Matrizen
nachschlagen: ja
order: 15210300
summary: Zwei Vektoren gleicher Länge ergeben eine einzige Zahl, wenn man ihre Komponenten paarweise multipliziert und addiert.
tags: Skalarprodukt, Gewicht, gewichtete Summe, Modell, Vorhersage, Einsvektor, Mittelwert
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Zwei Vektoren gleicher Länge ergeben eine einzige Zahl, wenn man ihre Komponenten paarweise multipliziert und addiert. Diese Rechnung ist die häufigste im ganzen maschinellen Lernen: Sie macht aus Messwerten eine Schätzung und vergleicht Daten mit einem Muster.
:::

### Das Skalarprodukt zweier Vektoren

<span class="anker" id="stufe-2-1"></span>

Eine Einkaufsrechnung geht so: Menge mal Preis für jeden Artikel, dann alles zusammenzählen. Dieselbe Rechnung mit zwei beliebigen Vektoren heißt Skalarprodukt.

Man kann sie sich als Begegnung einer Zeile mit einer Spalte vorstellen. Der erste Vektor wird als Zeile hingeschrieben, der zweite als Spalte daneben. Dann multipliziert man das erste Element der Zeile mit dem ersten der Spalte, das zweite mit dem zweiten und so weiter, und addiert:

$$\begin{pmatrix}1&2&3\end{pmatrix}\begin{pmatrix}4\\-1\\2\end{pmatrix}=1\cdot4+2\cdot(-1)+3\cdot2=8 .$$

:::definition Definition 2.1 (Skalarprodukt)
<span class="anker" id="satz-2-1"></span>

Das __Skalarprodukt__ zweier Vektoren $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ ist die Zahl

<span class="anker" id="gl-2-1"></span>
$$\mathbf{u}^{\top}\mathbf{v}=\sum_{j=1}^{d}u_j\,v_j=u_1v_1+u_2v_2+\dots+u_dv_d . \tag{2.1}$$
:::

Die Schreibweise $\mathbf{u}^{\top}\mathbf{v}$ sagt genau, was passiert: $\mathbf{u}^{\top}$ ist $\mathbf{u}$ als Zeile, und die Zeile trifft auf die Spalte $\mathbf{v}$. Das Ergebnis ist ein Skalar, daher der Name.

:::satz Satz 2.2 (Rechenregeln des Skalarprodukts)
<span class="anker" id="satz-2-2"></span>

Für alle $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ und jeden Skalar $c$ gilt:

<ol class="rm">

<li>

$\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$ (symmetrisch);

</li>

<li>

$(c\,\mathbf{u})^{\top}\mathbf{v}=c\,(\mathbf{u}^{\top}\mathbf{v})$ und $(\mathbf{u}+\mathbf{q})^{\top}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}+\mathbf{q}^{\top}\mathbf{v}$ (linear, ebenso im zweiten Vektor);

</li>

<li>

$\mathbf{u}^{\top}\mathbf{u}=\sum_ju_j^2\ge0$, und $\mathbf{u}^{\top}\mathbf{u}=0$ nur für $\mathbf{u}=\mathbf{0}$.

</li>

</ol>
:::

:::beweis Rechenregeln des Skalarprodukts
(i) folgt aus $u_jv_j=v_ju_j$ für jede Komponente. (ii) ist die Summenregel [(1.2)](vektoren-daten-als-zahlenlisten.html#gl-1-2): $\sum_j(c\,u_j)v_j=c\sum_ju_jv_j$ und $\sum_j(u_j+q_j)v_j=\sum_ju_jv_j+\sum_jq_jv_j$. (iii) Jeder Summand $u_j^2$ ist nicht negativ. Die Summe ist nur dann null, wenn jeder Summand null ist, also jedes $u_j=0$.
:::

::::beispiel [Rechenbeispiel]
Für $\mathbf{u}=(1,\,2,\,3)^{\top}$ und $\mathbf{v}=(4,\,-1,\,2)^{\top}$ ist $\mathbf{u}^{\top}\mathbf{v}=8$ und $\mathbf{u}^{\top}\mathbf{u}=14$ (Abb. [6](#abb-6)). In umgekehrter Reihenfolge ergibt sich dieselbe Zahl, $\mathbf{v}^{\top}\mathbf{u}=4\cdot1+(-1)\cdot2+2\cdot3=8$, wie es die Symmetrie verlangt.

:::abbildung ml/k1rskp 6
Zwei Skalarprodukte Schritt für Schritt: Komponente mal Komponente, dann die Summe der Produkte. Das Skalarprodukt eines Vektors mit sich selbst ist die Summe der Quadrate seiner Komponenten.
:::
::::

⁠**Kurz gesagt:** Das Skalarprodukt multipliziert zwei Vektoren Komponente für Komponente und addiert die Produkte; es ist eine Zahl.

:::hintergrund Andere Schreibweisen für dasselbe
In vielen Büchern steht $\mathbf{u}\cdot\mathbf{v}$ oder $\langle\mathbf{u},\mathbf{v}\rangle$ statt $\mathbf{u}^{\top}\mathbf{v}$; auf Englisch heißt es *dot product* oder *inner product*. Gemeint ist dieselbe Zahl. Diese Reihe schreibt $\mathbf{u}^{\top}\mathbf{v}$, weil man so an der Schreibweise sieht, dass eine Zeile auf eine Spalte trifft. Das zahlt sich aus, sobald Tabellen von Zahlen ins Spiel kommen.
:::

### Gewichte und gewichtete Summen

<span class="anker" id="stufe-2-2"></span>

Eine Maklerin schätzt den Preis einer Wohnung im Kopf ungefähr so: Jeder Quadratmeter ist etwa $3$ Tausend Euro wert, jedes Zimmer bringt noch einmal $10$ Tausend Euro, und jeder Kilometer Entfernung vom Zentrum zieht $4$ Tausend Euro ab. Sie nimmt also jedes Merkmal mit einem eigenen Faktor und zählt alles zusammen.

Die Zahl, mit der ein Merkmal in eine solche Rechnung eingeht, heißt sein __Gewicht__. Ein großes positives Gewicht heißt: Jede Einheit dieses Merkmals erhöht das Ergebnis stark. Ein negatives Gewicht heißt: Das Merkmal senkt das Ergebnis.

:::definition Definition 2.3 (Gewichtete Summe)
<span class="anker" id="satz-2-3"></span>

Für einen Vektor von Gewichten $\mathbf{w}=(w_1,\dots,w_d)^{\top}$ und ein Beispiel $\mathbf{x}\in\mathbb{R}^d$ ist die __gewichtete Summe__

<span class="anker" id="gl-2-2"></span>
$$\hat y=\mathbf{w}^{\top}\mathbf{x}=\sum_{j=1}^{d}w_j\,x_j . \tag{2.2}$$
:::

Eine feste Rechenvorschrift, die aus den Merkmalen eines Beispiels eine Zahl berechnet, heißt ein __Modell__. Die Zahl, die das Modell für ein Beispiel liefert, heißt seine __Vorhersage__. Das Dach über dem $y$ in $\hat y$ zeigt an, dass es sich um einen berechneten Schätzwert handelt und nicht um einen gemessenen Wert. In diesem Kapitel sind die Gewichte immer vorgegeben; woher gute Gewichte kommen, ist eine eigene Frage.

::::beispiel [Rechenbeispiel]
Die Maklerin benutzt die Gewichte $\mathbf{w}=(3,\,10,\,-4)^{\top}$ in Tausend Euro pro Quadratmeter, pro Zimmer und pro Kilometer. Für Wohnung 1 ist $\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$ (Abb. [7](#abb-7)), also $188$ Tausend Euro.

:::abbildung ml/k1rgewicht 7
Die Schätzung der Maklerin für Wohnung 1: jedes Merkmal mal sein Gewicht, dann die Summe. Die Beiträge der drei Merkmale sind $180$, $20$ und $-12$ Tausend Euro.
:::

Für die übrigen Wohnungen ergibt sich ebenso $\hat y_2=126$, $\hat y_3=286$ und $\hat y_4=232$. Jedes Produkt $w_jx_j$ hat die Einheit Tausend Euro, weil sich die Einheit des Merkmals gegen die Einheit im Nenner des Gewichts kürzt. Nur deshalb darf man die drei Produkte addieren.
::::

⁠**Kurz gesagt:** Eine gewichtete Summe ist das Skalarprodukt $\mathbf{w}^{\top}\mathbf{x}$ aus Gewichten und Merkmalen; sie ist das einfachste Modell, das aus Merkmalen eine Vorhersage macht.

:::hintergrund Ein großes Gewicht heißt nicht, dass das Merkmal wichtig ist
Bei der Maklerin ist das Gewicht der Zimmer mit $10$ mehr als dreimal so groß wie das der Fläche mit $3$. Trotzdem trägt die Fläche bei Wohnung 1 $180$ Tausend Euro bei und die Zimmerzahl nur $20$. Der Grund: Ein Gewicht gilt pro Einheit des Merkmals, und die Fläche hat viele Einheiten. Misst man die Fläche in Einheiten von $10\,\mathrm m^2$, ist Wohnung 1 nur noch $6$ Einheiten groß, und dasselbe Modell braucht das Gewicht $30$ Tausend Euro pro $10\,\mathrm m^2$. Die Vorhersage bleibt gleich, nur das Gewicht ist zehnmal so groß geworden. Wie groß ein Gewicht ist, hängt also an der gewählten Einheit. Will man wissen, wie viel ein Merkmal zur Vorhersage beiträgt, muss man das Produkt $w_jx_j$ ansehen, nicht das Gewicht allein.
:::

### Summe und Mittelwert als Skalarprodukt

<span class="anker" id="stufe-2-3"></span>

Viele alltägliche Rechnungen sind Skalarprodukte mit einem besonders einfachen zweiten Vektor. Am häufigsten braucht man die Summe und den Durchschnitt aller Komponenten.

Der __Einsvektor__ $\mathbf 1\in\mathbb{R}^n$ hat lauter Einsen als Komponenten. Das Skalarprodukt mit ihm addiert einfach alle Komponenten: $\mathbf 1^{\top}\mathbf{v}=v_1+\dots+v_n$.

:::definition Definition 2.4 (Mittelwert)
<span class="anker" id="satz-2-4"></span>

Der __Mittelwert__ der Komponenten eines Vektors $\mathbf{v}\in\mathbb{R}^n$ ist

<span class="anker" id="gl-2-3"></span>
$$\bar v=\frac1n\sum_{i=1}^nv_i=\frac1n\,\mathbf 1^{\top}\mathbf{v} . \tag{2.3}$$
:::

Weitere Rechnungen dieser Art: Das Skalarprodukt mit einem Einheitsvektor wählt eine Komponente aus, $\mathbf{e}_j^{\top}\mathbf{v}=v_j$, denn alle anderen Produkte enthalten eine Null. Das Skalarprodukt eines Vektors mit sich selbst ist die Summe der Quadrate, $\mathbf{v}^{\top}\mathbf{v}=\sum_iv_i^2$. Mengen mal Preise, aufsummiert, sind der Rechnungsbetrag. Und ein Polynom $p(t)=c_1+c_2t+\dots+c_nt^{n-1}$ an einer Stelle $t$ auszuwerten heißt, das Skalarprodukt $\mathbf{c}^{\top}\mathbf{z}$ seiner Koeffizienten $\mathbf{c}=(c_1,\dots,c_n)^{\top}$ mit den Potenzen $\mathbf{z}=(1,\,t,\,t^2,\dots,t^{n-1})^{\top}$ zu bilden. Für $p(t)=1+2t+3t^2$ an der Stelle $t=2$ ist das $(1,\,2,\,3)\,(1,\,2,\,4)^{\top}=1+4+12=17$.

::::beispiel [Rechenbeispiel]
Wohnung 1 hat von Januar bis März $\mathbf{u}=(200,\,250,\,300)^{\top}$ kWh Strom verbraucht (Unterabschnitt [1.4](vektoren-daten-als-zahlenlisten.html#stufe-1-4)). Zusammen sind das $\mathbf 1^{\top}\mathbf{u}=750$ kWh, im Mittel $\bar u=250$ kWh pro Monat (Abb. [8](#abb-8)). Der Verbrauch im Februar ist $\mathbf{e}_2^{\top}\mathbf{u}=250$ kWh.

:::abbildung ml/k1rmittel 8
Summe und Mittelwert des Stromverbrauchs als Skalarprodukt mit dem Einsvektor, in kWh.
:::

Kostet die Kilowattstunde in den drei Monaten $\mathbf{p}=(0{,}32;\ 0{,}34;\ 0{,}28)^{\top}$ Euro, so ist die Stromrechnung das Skalarprodukt aus Preisen und Mengen: $\mathbf{p}^{\top}\mathbf{u}=233$ Euro (Abb. [9](#abb-9)). Jedes Produkt $p_ju_j$ ist der Betrag für einen Monat, in Euro pro kWh mal kWh, also in Euro.

:::abbildung ml/k1rstrom 9
Die Stromrechnung als Skalarprodukt: Preis mal Menge für jeden Monat, dann die Summe, in Euro.
:::
::::

⁠**Kurz gesagt:** Summe, Mittelwert, Auswahl einer Komponente und Quadratsumme sind Skalarprodukte mit $\mathbf 1$, $\tfrac1n\mathbf 1$, $\mathbf{e}_j$ und dem Vektor selbst.

### Das Skalarprodukt als Mustervergleich

<span class="anker" id="stufe-2-4"></span>

Die Temperatur draußen wird alle zwölf Stunden abgelesen, abwechselnd mittags und um Mitternacht. Vier Werte hintereinander bilden einen Vektor, hier ein *Verlauf* genannt. Er soll darauf geprüft werden, ob er von Wert zu Wert hin und her springt, wie es der Wechsel von Tag und Nacht erwarten lässt. Dafür schreibt man das gesuchte Muster als Vektor auf, hier $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$, und bildet das Skalarprodukt mit dem Verlauf.

Was dabei passiert, zeigt Abb. [10](#abb-10). Jeder Wert wird mit dem Musterwert an derselben Stelle multipliziert. Hat der Verlauf an einer Stelle dasselbe Vorzeichen wie das Muster, ist das Produkt positiv; hat er das entgegengesetzte Vorzeichen, ist es negativ. Folgt der Verlauf dem Muster überall, sammeln sich lauter positive Beiträge zu einer großen Summe. Hat der Verlauf mit dem Muster nichts zu tun, heben sich positive und negative Beiträge gegenseitig auf.

:::abbildung ml/k1muster 10
Mustervergleich mit dem Skalarprodukt. Oben das Muster $\mathbf{w}=(1,-1,1,-1)^{\top}$, in der Mitte zwei Temperaturverläufe in Grad Celsius, unten die Produkte $w_j\,x_j$ an jeder Stelle $j$. Links springt der Verlauf $\mathbf{x}=(2,-1,3,-2)^{\top}$ im Takt des Musters: Alle Produkte sind positiv, die Summe ist $8$. Rechts steigt $\mathbf{x}'=(2,2,3,3)^{\top}$ gleichmäßig: Die Produkte heben sich auf, die Summe ist $0$.
:::

Genau gesagt: Der Beitrag der Stelle $j$ zum Skalarprodukt $\mathbf{w}^{\top}\mathbf{x}$ ist $w_jx_j$. Er ist positiv, wenn $w_j$ und $x_j$ dasselbe Vorzeichen haben, und negativ, wenn sie entgegengesetzte Vorzeichen haben. Je größer die Beträge an Stellen mit übereinstimmendem Vorzeichen, desto größer das Skalarprodukt.

Für Zahlenfolgen hat diese Rechnung einen eigenen Namen. Die Summe $\sum_nx[n]\,y[n]$ zweier reeller Folgen $x[n]$ und $y[n]$ heißt ihre Kreuzkorrelation an der Verschiebung null. Schreibt man die Werte zweier Folgen endlicher Länge als Vektoren $\mathbf{x}$ und $\mathbf{y}$, ist das genau das Skalarprodukt $\mathbf{x}^{\top}\mathbf{y}$. Die Quadratsumme einer Folge, $\sum_nx[n]^2$, ist ebenso $\mathbf{x}^{\top}\mathbf{x}$. Der Mustervergleich ist also kein neues Werkzeug, sondern dieselbe Rechnung, mit der man in einer langen Zahlenfolge nach einem bekannten Muster sucht.

::::beispiel [Rechenbeispiel]
Mit dem Wechselmuster $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$ ist $\mathbf{w}^{\top}\mathbf{x}=8$ für $\mathbf{x}=(2,\,-1,\,3,\,-2)^{\top}$ und $\mathbf{w}^{\top}\mathbf{x}'=0$ für $\mathbf{x}'=(2,\,2,\,3,\,3)^{\top}$ (Abb. [11](#abb-11)). Mit dem Gleichmuster $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ ist es umgekehrt: $\mathbf 1^{\top}\mathbf{x}=2$, aber $\mathbf 1^{\top}\mathbf{x}'=10$. Der Verlauf $\mathbf{x}$ wechselt also vor allem zwischen Tag und Nacht, $\mathbf{x}'$ ist vor allem gleichbleibend.

:::abbildung ml/k1rmuster 11
Das Wechselmuster $\mathbf{w}$ mit zwei Verläufen. Oben folgt $\mathbf{x}$ dem Muster: Alle vier Produkte sind positiv. Unten steigt $\mathbf{x}'$ gleichmäßig: Die Produkte heben sich paarweise auf.
:::
::::

Auch die gewichtete Summe der Maklerin ist ein Mustervergleich. Ihr Muster $\mathbf{w}=(3,\,10,\,-4)^{\top}$ beschreibt, was eine Wohnung wertvoll macht: viel Fläche, viele Zimmer, wenig Entfernung. Je besser eine Wohnung zu diesem Muster passt, desto höher ihre Vorhersage.

⁠**Kurz gesagt:** Das Skalarprodukt $\mathbf{w}^{\top}\mathbf{x}$ ist groß, wenn $\mathbf{x}$ dort große Werte hat, wo das Muster $\mathbf{w}$ große Werte mit demselben Vorzeichen hat; es ist die Korrelation an der Verschiebung null.

:::hintergrund Die Korrelationsfunktion besteht aus lauter Skalarprodukten
Die Kreuzkorrelation vergleicht eine Folge nicht nur an einer Stelle mit einem Muster, sondern für jede mögliche Verschiebung. Für jede Verschiebung $k$ ist ihr Wert ein Skalarprodukt: die Folge mit dem um $k$ Stellen verschobenen Muster. Die ganze Korrelationsfunktion ist also eine Reihe von Skalarprodukten, eines je Verschiebung. Wo das Muster in der Folge steckt, sammeln sich die positiven Beiträge, und die Korrelationsfunktion ist dort besonders groß. So findet man in einer langen Tonaufnahme die Stelle, an der ein bekanntes Geräusch vorkommt, etwa ein Gong, und in einem Foto die Stellen, die einem kleinen Bildausschnitt ähneln. Im maschinellen Lernen bleibt die Verschiebung meist fest bei null: Man vergleicht ein Beispiel als Ganzes mit einem Muster.
:::

:::aufgabe Aufgabe 4 ★ Rechenregeln nachprüfen
<span class="anker" id="aufg-4"></span>

Es seien $\mathbf{u}=(1,\,0,\,2)^{\top}$, $\mathbf{v}=(3,\,-1,\,1)^{\top}$ und $\mathbf{q}=(0,\,2,\,1)^{\top}$. Berechne $\mathbf{u}^{\top}\mathbf{v}$, $\mathbf{v}^{\top}\mathbf{u}$, $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})$, $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}$, $(3\mathbf{u})^{\top}\mathbf{v}$ und $\mathbf{u}^{\top}\mathbf{u}$. Welche Rechenregel zeigt jeder Vergleich?

:::loesung
Es ist $\mathbf{u}^{\top}\mathbf{v}=3+0+2=5$ und $\mathbf{v}^{\top}\mathbf{u}=3+0+2=5$: Das Skalarprodukt ist symmetrisch, Regel (i). Mit $\mathbf{v}+\mathbf{q}=(3,\,1,\,2)^{\top}$ ist $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})=3+0+4=7$, und $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}=5+(0+0+2)=7$: Linearität im zweiten Vektor, Regel (ii). Ferner ist $(3\mathbf{u})^{\top}\mathbf{v}=(3,0,6)\,(3,-1,1)^{\top}=9+0+6=15=3\cdot5$, ebenfalls Regel (ii). Schließlich ist $\mathbf{u}^{\top}\mathbf{u}=1+0+4=5>0$, wie Regel (iii) für $\mathbf{u}\ne\mathbf{0}$ verlangt.
:::
:::

:::aufgabe Aufgabe 5 ★★ Die Schätzung der Maklerin
<span class="anker" id="aufg-5"></span>

Benutze die Gewichte $\mathbf{w}=(3,\,10,\,-4)^{\top}$ aus Unterabschnitt [2.2](#stufe-2-2).

<ol class="al">

<li>

Berechne die Vorhersagen für alle vier Wohnungen. Welche Einheit haben sie?

</li>

<li>

In Wohnung 2 wird eine Wand eingezogen, sie hat danach zwei Zimmer bei gleicher Fläche. Wie ändert sich die Vorhersage, und warum hängt die Änderung nicht von der Fläche ab?

</li>

<li>

Ein Kollege sagt: „Bei der Maklerin zählen die Zimmer am meisten, sie haben das größte Gewicht.“ Prüfe die Aussage an Wohnung 1, indem du die drei Beiträge $w_jx_{1j}$ vergleichst.

</li>

</ol>

:::loesung
(a) Wie in Unterabschnitt [2.2](#stufe-2-2): $188$, $126$, $286$ und $232$, jeweils in Tausend Euro. Die Einheit ist Tausend Euro, weil jedes Gewicht die Einheit „Tausend Euro pro Einheit des Merkmals“ hat und sich die Merkmalseinheit im Produkt herauskürzt.

(b) Wohnung 2 wird zu $(40,\,2,\,1)^{\top}$. Die Vorhersage steigt von $126$ auf $120+20-4=136$, also um $10$. Allgemein ändert sich die gewichtete Summe bei einer Änderung $\Delta x_2$ des zweiten Merkmals um $w_2\,\Delta x_2$, denn $\mathbf{w}^{\top}(\mathbf{x}+\Delta x_2\,\mathbf{e}_2)=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,\mathbf{w}^{\top}\mathbf{e}_2=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,w_2$. Die anderen Merkmale spielen dafür keine Rolle. Das ist die Linearität des Skalarprodukts: Jedes Merkmal trägt für sich bei, ohne Wechselwirkung mit den anderen.

(c) Die Beiträge bei Wohnung 1 sind $w_1x_{11}=180$, $w_2x_{12}=20$ und $w_3x_{13}=-12$. Den weitaus größten Beitrag liefert die Fläche, obwohl ihr Gewicht dem Betrag nach das kleinste ist. Die Aussage des Kollegen verwechselt das Gewicht pro Einheit mit dem Beitrag zur Vorhersage; die Fläche hat sehr viele Einheiten.
:::
:::

:::aufgabe Aufgabe 6 ★★ Ein Muster für steigende Verläufe
<span class="anker" id="aufg-6"></span>

Ein Verlauf mit vier Werten, etwa die Temperatur an vier Tagen hintereinander, soll darauf geprüft werden, ob er ansteigt. Als Muster wird $\mathbf{w}=(-3,\,-1,\,1,\,3)^{\top}$ vorgeschlagen.

<ol class="al">

<li>

Berechne $\mathbf{w}^{\top}\mathbf{x}$ für $\mathbf{x}=(1,2,3,4)^{\top}$, $(4,3,2,1)^{\top}$, $(5,5,5,5)^{\top}$ und $(1,3,2,4)^{\top}$ und deute die Ergebnisse.

</li>

<li>

Warum liefert jeder konstante Verlauf $c\,\mathbf1$ genau null? Benutze $\mathbf 1^{\top}\mathbf{w}$.

</li>

</ol>

:::loesung
(a) $\mathbf{w}^{\top}(1,2,3,4)^{\top}=-3-2+3+12=10$: Der Verlauf steigt, das Ergebnis ist deutlich positiv. $\mathbf{w}^{\top}(4,3,2,1)^{\top}=-12-3+2+3=-10$: Der Verlauf fällt, das Ergebnis ist ebenso deutlich negativ. $\mathbf{w}^{\top}(5,5,5,5)^{\top}=-15-5+5+15=0$: konstant, kein Anstieg. $\mathbf{w}^{\top}(1,3,2,4)^{\top}=-3-3+2+12=8$: Der Verlauf steigt im Ganzen, mit einem Rücksprung in der Mitte, und das Ergebnis ist etwas kleiner als beim gleichmäßigen Anstieg. Das Muster wiegt die frühen Werte negativ und die späten positiv; es reagiert also darauf, ob die späten Werte größer sind als die frühen.

(b) $\mathbf 1^{\top}\mathbf{w}=-3-1+1+3=0$. Für einen konstanten Verlauf ist deshalb $\mathbf{w}^{\top}(c\,\mathbf 1)=c\,\mathbf{w}^{\top}\mathbf 1=c\cdot0=0$. Weil die Gewichte sich zu null addieren, ignoriert das Muster einen festen Betrag, der zu allen Werten addiert wird, ganz: Es misst nur Unterschiede zwischen den Werten. Ob es an allen vier Tagen $10$ Grad wärmer ist, ändert das Ergebnis nicht.
:::
:::
