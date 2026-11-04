---
title: Das Skalarprodukt
pfad: Informatik / Machine Learning / Vektoren und Matrizen
order: 6210300
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

⁠**Rechenbeispiel:** Für $\mathbf{u}=(1,\,2,\,3)^{\top}$ und $\mathbf{v}=(4,\,-1,\,2)^{\top}$ ist $\mathbf{u}^{\top}\mathbf{v}=4-2+6=8$ und $\mathbf{v}^{\top}\mathbf{u}=4-2+6=8$. Außerdem ist $\mathbf{u}^{\top}\mathbf{u}=1+4+9=14$.

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

⁠**Rechenbeispiel:** Die Maklerin benutzt die Gewichte $\mathbf{w}=(3,\,10,\,-4)^{\top}$ in Tausend Euro pro Quadratmeter, pro Zimmer und pro Kilometer. Für Wohnung 1 ist

$$\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=3\cdot60+10\cdot2+(-4)\cdot3=180+20-12=188 ,$$

also $188$ Tausend Euro. Für die übrigen Wohnungen ergibt sich ebenso $\hat y_2=126$, $\hat y_3=286$ und $\hat y_4=232$. Jedes Produkt $w_jx_j$ hat die Einheit Tausend Euro, weil sich die Einheit des Merkmals gegen die Einheit im Nenner des Gewichts kürzt. Nur deshalb darf man die drei Produkte addieren.

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

Drei weitere Rechnungen dieser Art: Das Skalarprodukt mit einem Einheitsvektor wählt eine Komponente aus, $\mathbf{e}_j^{\top}\mathbf{v}=v_j$. Das Skalarprodukt eines Vektors mit sich selbst ist die Summe der Quadrate, $\mathbf{v}^{\top}\mathbf{v}=\sum_iv_i^2$. Und Mengen mal Preise, aufsummiert, sind der Rechnungsbetrag.

⁠**Rechenbeispiel:** Für den Stromverbrauch $\mathbf{u}=(200,\,250,\,300)^{\top}$ kWh von Wohnung 1 ist

$$\mathbf 1^{\top}\mathbf{u}=750\ \text{kWh},\qquad \bar u=\tfrac13\cdot750=250\ \text{kWh},\qquad \mathbf{e}_2^{\top}\mathbf{u}=250\ \text{kWh}.$$

Die zweite Zahl ist der durchschnittliche Monatsverbrauch, die dritte der Verbrauch im Februar. Kostet die Kilowattstunde in den drei Monaten $0{,}32$, $0{,}30$ und $0{,}28$ Euro, so ist die Stromrechnung das Skalarprodukt aus Preisen und Mengen:

$$\begin{pmatrix}0{,}32&0{,}30&0{,}28\end{pmatrix}\begin{pmatrix}200\\250\\300\end{pmatrix}=64+75+84=223\ \text{Euro}.$$

⁠**Kurz gesagt:** Summe, Mittelwert, Auswahl einer Komponente und Quadratsumme sind Skalarprodukte mit $\mathbf 1$, $\tfrac1n\mathbf 1$, $\mathbf{e}_j$ und dem Vektor selbst.

### Das Skalarprodukt als Mustervergleich

<span class="anker" id="stufe-2-4"></span>

Ein Messsignal soll darauf geprüft werden, ob es von Abtastwert zu Abtastwert hin und her springt. Dafür schreibt man das gesuchte Muster als Vektor auf, hier $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$, und bildet das Skalarprodukt mit dem Signal.

Was dabei passiert, zeigt Abb. [3](#abb-3). Jeder Abtastwert wird mit dem Musterwert an derselben Stelle multipliziert. Hat das Signal an einer Stelle dasselbe Vorzeichen wie das Muster, ist das Produkt positiv; hat es das entgegengesetzte Vorzeichen, ist es negativ. Folgt das Signal dem Muster überall, sammeln sich lauter positive Beiträge zu einer großen Summe. Hat das Signal mit dem Muster nichts zu tun, heben sich positive und negative Beiträge gegenseitig auf.

:::abbildung ml/k1muster 3
Mustervergleich mit dem Skalarprodukt. Oben das Muster $\mathbf{w}=(1,-1,1,-1)^{\top}$, in der Mitte zwei Signale, unten die Produkte an jeder Stelle. Links springt das Signal $\mathbf{x}=(2,-1,3,-2)^{\top}$ im Takt des Musters: Alle Produkte sind positiv, die Summe ist $8$. Rechts steigt $\mathbf{x}'=(2,2,3,3)^{\top}$ gleichmäßig: Die Produkte heben sich auf, die Summe ist $0$.
:::

Genau gesagt: Der Beitrag der Stelle $j$ zum Skalarprodukt $\mathbf{w}^{\top}\mathbf{x}$ ist $w_jx_j$. Er ist positiv, wenn $w_j$ und $x_j$ dasselbe Vorzeichen haben, und negativ, wenn sie entgegengesetzte Vorzeichen haben. Je größer die Beträge an Stellen mit übereinstimmendem Vorzeichen, desto größer das Skalarprodukt.

Aus der Signalverarbeitung kennt man diese Rechnung als Korrelation. Die Kreuzkorrelation zweier reeller Folgen $x[n]$ und $y[n]$ an der Verschiebung null ist $\sum_nx[n]\,y[n]$. Schreibt man die Abtastwerte zweier Signale endlicher Länge als Vektoren $\mathbf{x}$ und $\mathbf{y}$, ist das genau das Skalarprodukt $\mathbf{x}^{\top}\mathbf{y}$. Die Energie eines Signals, $\sum_nx[n]^2$, ist ebenso $\mathbf{x}^{\top}\mathbf{x}$. Der Mustervergleich ist also kein neues Werkzeug, sondern dasselbe, mit dem ein Korrelator ein bekanntes Muster in einem Signal sucht.

⁠**Rechenbeispiel:** Mit dem Wechselmuster $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$ ist $\mathbf{w}^{\top}\mathbf{x}=2+1+3+2=8$ für $\mathbf{x}=(2,\,-1,\,3,\,-2)^{\top}$ und $\mathbf{w}^{\top}\mathbf{x}'=2-2+3-3=0$ für $\mathbf{x}'=(2,\,2,\,3,\,3)^{\top}$. Mit dem Gleichmuster $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ ist es umgekehrt: $\mathbf 1^{\top}\mathbf{x}=2$, aber $\mathbf 1^{\top}\mathbf{x}'=10$. Das Signal $\mathbf{x}$ wechselt also vor allem, $\mathbf{x}'$ ist vor allem gleichbleibend.

Auch die gewichtete Summe der Maklerin ist ein Mustervergleich. Ihr Muster $\mathbf{w}=(3,\,10,\,-4)^{\top}$ beschreibt, was eine Wohnung wertvoll macht: viel Fläche, viele Zimmer, wenig Entfernung. Je besser eine Wohnung zu diesem Muster passt, desto höher ihre Vorhersage.

⁠**Kurz gesagt:** Das Skalarprodukt $\mathbf{w}^{\top}\mathbf{x}$ ist groß, wenn $\mathbf{x}$ dort große Werte hat, wo das Muster $\mathbf{w}$ große Werte mit demselben Vorzeichen hat; es ist die Korrelation an der Verschiebung null.

:::hintergrund Die Korrelationsfunktion besteht aus lauter Skalarprodukten
Die Kreuzkorrelation vergleicht ein Signal nicht nur an einer Stelle mit einem Muster, sondern für jede mögliche Verschiebung. Für jede Verschiebung $k$ ist ihr Wert ein Skalarprodukt: das Signal mit dem um $k$ Takte verschobenen Muster. Die ganze Korrelationsfunktion ist also eine Reihe von Skalarprodukten, eines je Verschiebung. Wo das Muster im Signal steckt, sammeln sich die positiven Beiträge, und die Korrelationsfunktion hat dort ihren größten Wert. So findet ein Radarempfänger das Echo seines eigenen Pulses und ein Funkempfänger den Anfang eines bekannten Datenrahmens. Im maschinellen Lernen bleibt die Verschiebung meist fest bei null: Man vergleicht ein Beispiel als Ganzes mit einem Muster.
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

(c) Die Beiträge bei Wohnung 1 sind $w_1x_{11}=180$, $w_2x_{12}=20$ und $w_3x_{13}=-12$. Den weitaus größten Beitrag liefert die Fläche, obwohl ihr Gewicht das kleinste ist. Die Aussage des Kollegen verwechselt das Gewicht pro Einheit mit dem Beitrag zur Vorhersage; die Fläche hat sehr viele Einheiten.
:::
:::

:::aufgabe Aufgabe 6 ★★ Ein Muster für steigende Signale
<span class="anker" id="aufg-6"></span>

Ein Signal mit vier Abtastwerten soll darauf geprüft werden, ob es ansteigt. Als Muster wird $\mathbf{w}=(-3,\,-1,\,1,\,3)^{\top}$ vorgeschlagen.

<ol class="al">

<li>

Berechne $\mathbf{w}^{\top}\mathbf{x}$ für $\mathbf{x}=(1,2,3,4)^{\top}$, $(4,3,2,1)^{\top}$, $(5,5,5,5)^{\top}$ und $(1,3,2,4)^{\top}$ und deute die Ergebnisse.

</li>

<li>

Warum liefert jedes konstante Signal $c\,\mathbf1$ genau null? Benutze $\mathbf 1^{\top}\mathbf{w}$.

</li>

</ol>

:::loesung
(a) $\mathbf{w}^{\top}(1,2,3,4)^{\top}=-3-2+3+12=10$: Das Signal steigt, das Ergebnis ist deutlich positiv. $\mathbf{w}^{\top}(4,3,2,1)^{\top}=-12-3+2+3=-10$: Das Signal fällt, das Ergebnis ist ebenso deutlich negativ. $\mathbf{w}^{\top}(5,5,5,5)^{\top}=-15-5+5+15=0$: konstant, kein Anstieg. $\mathbf{w}^{\top}(1,3,2,4)^{\top}=-3-3+2+12=8$: Das Signal steigt im Ganzen, mit einem Rücksprung in der Mitte, und das Ergebnis ist etwas kleiner als beim gleichmäßigen Anstieg. Das Muster wiegt die frühen Werte negativ und die späten positiv; es reagiert also darauf, ob die späten Werte größer sind als die frühen.

(b) $\mathbf 1^{\top}\mathbf{w}=-3-1+1+3=0$. Für ein konstantes Signal ist deshalb $\mathbf{w}^{\top}(c\,\mathbf 1)=c\,\mathbf{w}^{\top}\mathbf 1=c\cdot0=0$. Weil die Gewichte sich zu null addieren, ignoriert das Muster einen gemeinsamen Gleichanteil ganz: Es misst nur Unterschiede zwischen den Abtastwerten.
:::
:::
