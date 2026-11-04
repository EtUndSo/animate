---
title: Vektoren: Daten als Zahlenlisten
pfad: Informatik / Machine Learning / Vektoren und Matrizen
order: 6210200
summary: Ein Rechner kann nur mit Zahlen umgehen.
tags: Index, Summenzeichen, Laufindex, Doppelsumme, Merkmal, Beispiel, Datensatz, Vektor
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Rechner kann nur mit Zahlen umgehen. Dieser Abschnitt klärt, wie man ein Ding aus der wirklichen Welt durch eine Liste von Zahlen beschreibt und welche Rechnungen mit solchen Listen erlaubt sind.
:::

### Was du dafür brauchst: Summenzeichen und Indizes

<span class="anker" id="stufe-1-1"></span>

In diesem Kapitel werden ständig viele Zahlen addiert. Damit man nicht jedes Mal „$a_1+a_2+\dots$“ ausschreiben muss, gibt es eine Kurzschrift.

**Indizes.** Hat man mehrere Zahlen derselben Art, nummeriert man sie durch: $a_1,a_2,\dots,a_n$. Die tiefgestellte Nummer heißt __Index__. Sie sagt nur, die wievielte Zahl gemeint ist, und hat mit dem Wert der Zahl nichts zu tun.

**Das Summenzeichen.** Für die Summe von $a_1$ bis $a_n$ schreibt man

<span class="anker" id="gl-1-1"></span>
$$\sum_{i=1}^{n} a_i = a_1+a_2+\dots+a_n , \tag{1.1}$$

gelesen „Summe über $a_i$ für $i$ von $1$ bis $n$“. Das große griechische Sigma heißt __Summenzeichen__. Der Buchstabe $i$ darunter ist der __Laufindex__: Er nimmt nacheinander die Werte $1,2,\dots,n$ an, und für jeden Wert kommt ein Summand dazu. Der Laufindex ist ein Platzhalter. Ob man ihn $i$, $j$ oder $k$ nennt, ändert die Summe nicht: $\sum_{i=1}^n a_i=\sum_{j=1}^n a_j$.

**Zwei Rechenregeln.** Weil Addition und Multiplikation für jeden einzelnen Summanden gelten, darf man einen gemeinsamen Faktor vor die Summe ziehen und eine Summe von Summen aufteilen:

<span class="anker" id="gl-1-2"></span>
$$\sum_{i=1}^n c\,a_i=c\sum_{i=1}^n a_i ,\qquad \sum_{i=1}^n (a_i+b_i)=\sum_{i=1}^n a_i+\sum_{i=1}^n b_i . \tag{1.2}$$

Die erste Regel ist das Ausklammern, die zweite das Umsortieren der Summanden.

**Doppelsummen.** Zahlen, die in einer Tabelle stehen, bekommen zwei Indizes: $a_{ij}$ ist die Zahl in Zeile $i$ und Spalte $j$. Die Summe aller Einträge einer Tabelle mit $m$ Zeilen und $n$ Spalten schreibt man als __Doppelsumme__

$$\sum_{i=1}^{m}\sum_{j=1}^{n}a_{ij} .$$

Man liest sie von innen nach außen: Für jede Zeile $i$ addiert die innere Summe die Zahlen dieser Zeile, die äußere Summe addiert die Zeilensummen. Weil es bei endlich vielen Summanden auf die Reihenfolge nicht ankommt, darf man die beiden Summenzeichen vertauschen und zuerst spaltenweise addieren.

⁠**Rechenbeispiel:** Für $a_1=2$, $a_2=5$, $a_3=1$ ist

$$\sum_{i=1}^3 a_i=2+5+1=8,\qquad \sum_{i=1}^3 a_i^2=4+25+1=30,\qquad \sum_{j=1}^{3}j=1+2+3=6 .$$

Die Tabelle mit den Zeilen $(1,\,2)$ und $(3,\,4)$ hat die Einträge $a_{11}=1$, $a_{12}=2$, $a_{21}=3$, $a_{22}=4$. Zeilenweise ist $\sum_{i=1}^2\sum_{j=1}^2a_{ij}=(1+2)+(3+4)=10$, spaltenweise $(1+3)+(2+4)=10$.

⁠**Kurz gesagt:** $\sum_{i=1}^n a_i$ ist die Summe von $a_1$ bis $a_n$; der Laufindex $i$ ist nur ein Platzhalter.

### Beispiele und Merkmale

<span class="anker" id="stufe-1-2"></span>

Wer aus Daten lernen will, hat zuerst eine Sammlung gleichartiger Dinge vor sich: Wohnungen, Patienten, Briefe, Messungen an einer Maschine. Jedes Ding beschreibt man durch dieselben Messgrößen. Wohnungen zum Beispiel durch ihre Fläche, die Zahl der Zimmer und die Entfernung zum Stadtzentrum. Schreibt man das für mehrere Wohnungen auf, entsteht eine Tabelle (Tabelle [1](#tab-1)). Sie begleitet das ganze Kapitel.

<span class="anker" id="tab-1"></span>

**Tabelle 1:** Der Wohnungsdatensatz dieses Kapitels: vier Wohnungen, jede durch drei Merkmale beschrieben. Die Zahlen sind erfunden.

|  | Fläche in $\mathrm{m}^2$ | Zimmer | Entfernung zum Zentrum in km |
|---|---|---|---|
| Wohnung 1 | 60 | 2 | 3 |
| Wohnung 2 | 40 | 1 | 1 |
| Wohnung 3 | 90 | 4 | 6 |
| Wohnung 4 | 70 | 3 | 2 |

Jede Zeile der Tabelle gehört zu einem Ding, jede Spalte zu einer Messgröße. Für beides gibt es feste Wörter.

:::definition Definition 1.1 (Merkmal, Beispiel, Datensatz)
<span class="anker" id="satz-1-1"></span>

Ein __Merkmal__ ist eine Eigenschaft, die sich durch eine reelle Zahl angeben lässt.

Ein __Beispiel__ ist ein einzelnes Ding, das durch die Werte von $d$ Merkmalen beschrieben ist.

Ein __Datensatz__ ist eine Sammlung von $N$ Beispielen, die alle durch dieselben $d$ Merkmale beschrieben sind.
:::

In der ganzen Reihe gilt: $N$ ist die Zahl der Beispiele und $d$ die Zahl der Merkmale. Die Beispiele werden mit $i=1,\dots,N$ durchnummeriert, die Merkmale mit $j=1,\dots,d$.

Zwei Hinweise zu den Wörtern. In Datenbanken heißt eine einzelne Zeile einer Tabelle oft „Datensatz“; hier ist der Datensatz die ganze Sammlung. Und das Wort „Beispiel“ meint in diesem Kapitel immer ein Ding aus einem Datensatz; durchgerechnete Aufgaben heißen deshalb „Rechenbeispiel“.

⁠**Rechenbeispiel:** Der Wohnungsdatensatz hat $N=4$ Beispiele und $d=3$ Merkmale. Merkmal 2 ist die Zimmerzahl. Bei Wohnung 3 hat es den Wert $4$.

Nicht jede Eigenschaft ist von sich aus eine Zahl. Der Stadtteil einer Wohnung ist ein Name. Solche Eigenschaften muss man erst in Zahlen übersetzen, bevor man mit ihnen rechnen kann. In diesem Kapitel sind alle Merkmale schon Zahlen.

⁠**Kurz gesagt:** Ein Datensatz besteht aus $N$ Beispielen, und jedes Beispiel ist durch dieselben $d$ Merkmale beschrieben.

:::hintergrund Dieselben Dinge mit anderen Namen
In englischsprachigen Texten heißt ein Beispiel *example*, *sample*, *instance* oder *data point*, ein Merkmal *feature* oder *attribute* und der Datensatz *dataset*. Auch auf Deutsch sind „Datenpunkt“ und „Stichprobe“ für ein Beispiel verbreitet. Gemeint ist immer dasselbe: eine Zeile der Tabelle.
:::

### Vektoren

<span class="anker" id="stufe-1-3"></span>

Eine Wohnung ist für den Rechner nichts anderes als ihre drei Zahlen. Damit man mit diesen drei Zahlen wie mit einem einzigen Gegenstand rechnen kann, fasst man sie zu einer Liste zusammen. Die Reihenfolge ist dabei fest: zuerst die Fläche, dann die Zimmer, dann die Entfernung.

Eine solche Liste kann man auch zeichnen, wenn sie nur zwei Zahlen enthält. Nimmt man von Wohnung 4 nur die Zimmerzahl $3$ und die Entfernung $2$, so ist das der Punkt mit den Koordinaten $(3,\,2)$ in einer Ebene, deren waagerechte Achse die Zimmer und deren senkrechte Achse die Kilometer zählt. Man kann sich dieselbe Liste auch als Pfeil vorstellen, der vom Nullpunkt zu diesem Punkt führt (Abb. [1](#abb-1)). Beide Bilder beschreiben dieselben zwei Zahlen.

:::abbildung ml/k1punktpfeil 1
Der Vektor $\mathbf{x}=(3,\,2)^{\top}$, links als Punkt, rechts als Pfeil vom Nullpunkt zu diesem Punkt. Hier steht $x_1$ für die Zimmerzahl und $x_2$ für die Entfernung zum Zentrum in km von Wohnung 4.
:::

:::definition Definition 1.2 (Vektor)
<span class="anker" id="satz-1-2"></span>

Ein __Vektor__ $\mathbf{x}$ mit $d$ Komponenten ist eine geordnete Liste von $d$ reellen Zahlen $x_1,\dots,x_d$, untereinander geschrieben:

$$\mathbf{x}=\begin{pmatrix}x_1\\\vdots\\x_d\end{pmatrix}.$$

Die Zahl $x_j$ heißt die $j$-te __Komponente__ von $\mathbf{x}$. Die Menge aller Vektoren mit $d$ Komponenten heißt $\mathbb{R}^d$. Zwei Vektoren sind gleich, wenn sie gleich viele Komponenten haben und alle Komponenten an derselben Stelle übereinstimmen.
:::

Vektoren werden fett und klein geschrieben, ihre Komponenten mager. Eine einzelne reelle Zahl nennt man im Unterschied zum Vektor einen __Skalar__.

**Spalte und Zeile.** In dieser Reihe ist ein Vektor immer eine Spalte. Im Fließtext kostet eine Spalte viel Platz. Man schreibt deshalb die Zahlen nebeneinander und setzt ein hochgestelltes $\top$ dahinter: $(x_1,\dots,x_d)^{\top}$ bedeutet dieselben Zahlen als Spalte. Das Zeichen heißt __transponiert__. Es macht aus einer Zeile eine Spalte und aus einer Spalte eine Zeile. Umgekehrt ist $\mathbf{x}^{\top}=(x_1,\,\dots,\,x_d)$ der Vektor $\mathbf{x}$ als Zeile geschrieben.

**Die Beispiele eines Datensatzes.** Das Beispiel Nummer $i$ ist der Vektor $\mathbf{x}_i\in\mathbb{R}^d$. Den Vektor eines Beispiels nennt man auch seinen __Merkmalsvektor__. Seine Komponenten bekommen zwei Indizes: $x_{ij}$ ist der Wert von Merkmal $j$ bei Beispiel $i$. Ein fetter Buchstabe mit einem Index ist also ein ganzer Vektor aus einer Liste von Vektoren, ein magerer Buchstabe mit zwei Indizes eine einzelne Zahl.

⁠**Rechenbeispiel:** Wohnung 1 ist der Vektor $\mathbf{x}_1=(60,\,2,\,3)^{\top}\in\mathbb{R}^3$. Ihre zweite Komponente ist $x_{12}=2$. Der Vektor $(2,\,60,\,3)^{\top}$ enthält dieselben Zahlen, ist aber ein anderer Vektor: An der ersten Stelle steht jetzt die Zahl $2$, und die würde man als Fläche lesen.

⁠**Kurz gesagt:** Ein Vektor ist eine geordnete Liste von Zahlen, die man als Punkt oder als Pfeil zeichnen kann; ein Beispiel mit $d$ Merkmalen ist ein Vektor im $\mathbb{R}^d$.

:::hintergrund Was ein Vektor eigentlich ist
Eine Liste von Zahlen ist der Vektor, mit dem man rechnet. Mathematisch ist der Begriff weiter gefasst: Ein Vektor ist alles, was man addieren und mit einer Zahl multiplizieren kann, ohne dabei die Art des Gegenstands zu verlassen. Pfeile in der Ebene gehören dazu, aber auch Signale. Ein Signal, das $n$-mal abgetastet wurde, ist die Liste seiner Abtastwerte $x[0],\dots,x[n-1]$, also ein Vektor im $\mathbb{R}^n$. Zwei Signale zu addieren heißt, sie zu überlagern, und ein Signal mit einer Zahl zu multiplizieren heißt, es zu verstärken; beides liefert wieder ein Signal derselben Länge.

Auch ein Bild ist ein Vektor. Ein Graustufenbild mit $28\times28$ Bildpunkten besteht aus $784$ Helligkeitswerten. Liest man sie Zeile für Zeile hintereinander, ist das Bild ein Punkt im $\mathbb{R}^{784}$. Diese Vorstellung lässt sich nicht mehr zeichnen, aber man rechnet damit genauso wie mit zwei oder drei Komponenten.
:::

### Addition und Vielfaches

<span class="anker" id="stufe-1-4"></span>

Mit Listen von Messwerten will man rechnen: den Stromverbrauch zweier Wohnungen zusammenzählen, Kilowattstunden in Megawattstunden umrechnen oder nachsehen, um wie viel sich zwei Wohnungen unterscheiden. All das geschieht Komponente für Komponente.

Im Bild der Pfeile heißt Addieren: Man hängt den zweiten Pfeil an die Spitze des ersten. Der Pfeil vom Nullpunkt zur neuen Spitze ist die Summe (Abb. [2](#abb-2), links). Mit einer Zahl multiplizieren heißt, den Pfeil zu strecken oder zu stauchen; ein negativer Faktor dreht ihn zusätzlich um (Abb. [2](#abb-2), rechts).

:::abbildung ml/k1addition 2
Links: $\mathbf{u}=(3,\,1)^{\top}$ plus $\mathbf{v}=(1,\,2)^{\top}$. Hängt man $\mathbf{v}$ an die Spitze von $\mathbf{u}$ (oder $\mathbf{u}$ an die Spitze von $\mathbf{v}$, gestrichelt), endet man bei $\mathbf{u}+\mathbf{v}=(4,\,3)^{\top}$. Rechts: $\mathbf{u}=(2,\,1)^{\top}$, das Doppelte $2\mathbf{u}=(4,\,2)^{\top}$ (grau) und $-\mathbf{u}=(-2,\,-1)^{\top}$.
:::

:::definition Definition 1.3 (Addition und Vielfaches)
<span class="anker" id="satz-1-3"></span>

Für zwei Vektoren $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ und einen Skalar $c$ sind die __Summe__ $\mathbf{u}+\mathbf{v}$ und das __Vielfache__ $c\,\mathbf{u}$ die Vektoren mit den Komponenten

<span class="anker" id="gl-1-3"></span>
$$(\mathbf{u}+\mathbf{v})_j=u_j+v_j ,\qquad (c\,\mathbf{u})_j=c\,u_j ,\qquad j=1,\dots,d. \tag{1.3}$$

Der __Nullvektor__ $\mathbf{0}$ hat lauter Nullen als Komponenten. Man schreibt $-\mathbf{u}$ für $(-1)\,\mathbf{u}$ und $\mathbf{u}-\mathbf{v}$ für $\mathbf{u}+(-\mathbf{v})$.
:::

Addieren kann man nur Vektoren mit gleich vielen Komponenten. Sinnvoll ist es außerdem nur, wenn an derselben Stelle dieselbe Größe steht: Kilowattstunden zu Kilowattstunden, nicht Quadratmeter zu Zimmern.

Weil jede Komponente für sich eine gewöhnliche Rechnung mit Zahlen ist, gelten die bekannten Regeln: $\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}$, $(\mathbf{u}+\mathbf{v})+\mathbf{q}=\mathbf{u}+(\mathbf{v}+\mathbf{q})$, $c\,(\mathbf{u}+\mathbf{v})=c\,\mathbf{u}+c\,\mathbf{v}$, $(c+c')\,\mathbf{u}=c\,\mathbf{u}+c'\,\mathbf{u}$ und $\mathbf{u}+\mathbf{0}=\mathbf{u}$ für alle Vektoren $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ und Skalare $c,c'$.

Die Differenz $\mathbf{u}-\mathbf{v}$ hat eine eigene Anschauung. Sie ist der Pfeil, der von der Spitze von $\mathbf{v}$ zur Spitze von $\mathbf{u}$ führt, denn $\mathbf{v}+(\mathbf{u}-\mathbf{v})=\mathbf{u}$. Bei zwei Beispielen gibt sie an, um wie viel sie sich in jedem Merkmal unterscheiden.

⁠**Rechenbeispiel:** Wohnung 1 hat von Januar bis März $\mathbf{u}=(200,\,250,\,300)^{\top}$ Kilowattstunden Strom verbraucht, Wohnung 2 im selben Haus $\mathbf{v}=(150,\,100,\,120)^{\top}$. Zusammen verbrauchen sie

$$\mathbf{u}+\mathbf{v}=(350,\,350,\,420)^{\top}\ \text{kWh}.$$

Den Verbrauch von Wohnung 1 in Megawattstunden liefert das Vielfache $0{,}001\,\mathbf{u}=(0{,}2,\,0{,}25,\,0{,}3)^{\top}$. Die Differenz $\mathbf{u}-\mathbf{v}=(50,\,150,\,180)^{\top}$ sagt, wie viele Kilowattstunden Wohnung 1 in jedem Monat mehr verbraucht als Wohnung 2. Im Wohnungsdatensatz ist $\mathbf{x}_3-\mathbf{x}_1=(30,\,2,\,3)^{\top}$: Wohnung 3 ist $30\,\mathrm m^2$ größer, hat zwei Zimmer mehr und liegt $3$ km weiter draußen als Wohnung 1.

⁠**Kurz gesagt:** Vektoren addiert man und multipliziert sie mit einer Zahl, indem man es Komponente für Komponente tut.

### Linearkombinationen

<span class="anker" id="stufe-1-5"></span>

Fast jede Rechnung in diesem Kapitel nimmt mehrere Vektoren, multipliziert jeden mit einer eigenen Zahl und addiert die Ergebnisse. Ein Durchschnitt ist so eine Rechnung, eine Mischung auch.

Im Bild der Pfeile: Man geht $c_1$-mal die Strecke $\mathbf{v}_1$, dann $c_2$-mal die Strecke $\mathbf{v}_2$ und so weiter. Wo man ankommt, ist das Ergebnis.

:::definition Definition 1.4 (Linearkombination)
<span class="anker" id="satz-1-4"></span>

Für Vektoren $\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ und Skalare $c_1,\dots,c_k$ heißt

<span class="anker" id="gl-1-4"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\sum_{l=1}^{k}c_l\,\mathbf{v}_l \tag{1.4}$$

eine __Linearkombination__ der Vektoren $\mathbf{v}_1,\dots,\mathbf{v}_k$. Die Zahlen $c_l$ heißen ihre __Koeffizienten__.
:::

Achtung beim Lesen: $\mathbf{v}_l$ ist fett, also der $l$-te Vektor der Liste, nicht die $l$-te Komponente eines Vektors.

⁠**Rechenbeispiel 1:** $(1,\,2)^{\top}+3\,(0,\,1)^{\top}=(1,\,2)^{\top}+(0,\,3)^{\top}=(1,\,5)^{\top}$.

⁠**Rechenbeispiel 2: der Mittelpunkt.** Die Linearkombination $\tfrac12\mathbf{x}_1+\tfrac12\mathbf{x}_2$ der Wohnungen 1 und 2 ist

$$\tfrac12\,(60,\,2,\,3)^{\top}+\tfrac12\,(40,\,1,\,1)^{\top}=(50,\,1{,}5,\,2)^{\top}.$$

Das ist eine gedachte Wohnung, die in jedem Merkmal genau zwischen den beiden liegt. Der Punkt liegt in der Mitte der Verbindungsstrecke.

⁠**Rechenbeispiel 3: der Mittelwert der Beispiele.** Nimmt man alle $N$ Beispiele mit dem Koeffizienten $1/N$, entsteht der __Mittelwert der Beispiele__

<span class="anker" id="gl-1-5"></span>
$$\bar{\mathbf{x}}=\frac1N\sum_{i=1}^{N}\mathbf{x}_i . \tag{1.5}$$

Für den Wohnungsdatensatz ist $\bar{\mathbf{x}}=\tfrac14\bigl[(60,2,3)^{\top}+(40,1,1)^{\top}+(90,4,6)^{\top}+(70,3,2)^{\top}\bigr]=(65,\,2{,}5,\,3)^{\top}$, die „Durchschnittswohnung“.

⁠**Kurz gesagt:** Eine Linearkombination multipliziert jeden Vektor mit einer eigenen Zahl und addiert alles.

:::hintergrund Wo die Mischungen zweier Punkte liegen
Wählt man bei zwei Vektoren $\mathbf{x}_1,\mathbf{x}_2$ die Koeffizienten so, dass ihre Summe $1$ ist, also $(1-t)\,\mathbf{x}_1+t\,\mathbf{x}_2$ mit einer Zahl $t$, so liegt das Ergebnis immer auf der Geraden durch die beiden Punkte. Denn man kann es umschreiben zu

$$(1-t)\,\mathbf{x}_1+t\,\mathbf{x}_2=\mathbf{x}_1+t\,(\mathbf{x}_2-\mathbf{x}_1) .$$

Das heißt: vom Punkt $\mathbf{x}_1$ aus das $t$-Fache des Verbindungspfeils $\mathbf{x}_2-\mathbf{x}_1$ gehen. Für $t=0$ ist man bei $\mathbf{x}_1$, für $t=1$ bei $\mathbf{x}_2$, für $t=\tfrac12$ in der Mitte. Alle $t$ zwischen $0$ und $1$ ergeben die Punkte der Verbindungsstrecke. Solche Mischungen braucht man immer dann, wenn man zwischen zwei Datenpunkten Zwischenwerte bilden will.
:::

### Die Einheitsvektoren

<span class="anker" id="stufe-1-6"></span>

Die einfachsten Vektoren haben eine einzige Komponente $1$ und sonst lauter Nullen. Bei einem Beispiel hieße das: Nur ein Merkmal ist „eingeschaltet“, und zwar mit dem Wert $1$. In der Ebene sind es die beiden Pfeile der Länge $1$ längs der Achsen.

:::definition Definition 1.5 (Einheitsvektor)
<span class="anker" id="satz-1-5"></span>

Der $j$-te __Einheitsvektor__ $\mathbf{e}_j\in\mathbb{R}^d$ hat an der Stelle $j$ eine $1$ und an allen anderen Stellen eine $0$.
:::

Im $\mathbb{R}^2$ ist $\mathbf{e}_1=(1,\,0)^{\top}$ und $\mathbf{e}_2=(0,\,1)^{\top}$. Jeder Vektor ist eine Linearkombination der Einheitsvektoren, und die Koeffizienten sind genau seine Komponenten:

<span class="anker" id="gl-1-6"></span>
$$\mathbf{x}=x_1\mathbf{e}_1+x_2\mathbf{e}_2+\dots+x_d\mathbf{e}_d=\sum_{j=1}^d x_j\,\mathbf{e}_j . \tag{1.6}$$

Man sieht das, wenn man die rechte Seite Komponente für Komponente ausrechnet: An der Stelle $j$ trägt nur der Summand $x_j\mathbf{e}_j$ etwas bei, und zwar $x_j\cdot1$. Andere Koeffizienten sind nicht möglich, denn sie würden an irgendeiner Stelle eine andere Zahl ergeben.

⁠**Rechenbeispiel:** $\mathbf{x}_1=(60,\,2,\,3)^{\top}=60\,\mathbf{e}_1+2\,\mathbf{e}_2+3\,\mathbf{e}_3$, also $60$-mal „ein Quadratmeter“ plus $2$-mal „ein Zimmer“ plus $3$-mal „ein Kilometer“.

⁠**Kurz gesagt:** Der Einheitsvektor $\mathbf{e}_j$ hat an der Stelle $j$ eine Eins und sonst Nullen; jeder Vektor ist die Summe $\sum_jx_j\mathbf{e}_j$.

:::aufgabe Aufgabe 1 ★ Summen lesen und schreiben
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Berechne $\sum_{i=1}^{5}(2i-1)$ und $\sum_{i=1}^{2}\sum_{j=1}^{3}i\,j$.

</li>

<li>

Schreibe $3+6+9+12$ mit einem Summenzeichen.

</li>

<li>

Es sei $a_i$ die Fläche von Wohnung $i$ aus Tabelle [1](#tab-1). Was bedeuten $\sum_{i=1}^4a_i$ und $\frac14\sum_{i=1}^4a_i$, und welche Zahlen kommen heraus?

</li>

</ol>

:::loesung
(a) Der Laufindex $i$ nimmt die Werte $1$ bis $5$ an, die Summanden sind die ungeraden Zahlen $1,3,5,7,9$:

$$\sum_{i=1}^{5}(2i-1)=1+3+5+7+9=25 .$$

In der Doppelsumme ist für jedes feste $i$ die innere Summe $\sum_{j=1}^3i\,j=i\,(1+2+3)=6i$; der Faktor $i$ hängt nicht von $j$ ab und darf nach [(1.2)](#gl-1-2) vor die innere Summe. Danach ist $\sum_{i=1}^2 6i=6+12=18$.

(b) Die Summanden sind die Vielfachen von $3$: $3+6+9+12=\sum_{i=1}^43i$. Ebenso richtig ist $3\sum_{i=1}^4i$, nach der Regel für gemeinsame Faktoren.

(c) $\sum_{i=1}^4a_i=60+40+90+70=260$ ist die Gesamtfläche aller vier Wohnungen in $\mathrm m^2$, und $\frac14\sum_{i=1}^4a_i=65$ ist die durchschnittliche Fläche einer Wohnung.
:::
:::

:::aufgabe Aufgabe 2 ★ Mit Vektoren rechnen
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Berechne $2\mathbf{u}-3\mathbf{v}$ für $\mathbf{u}=(1,\,-1,\,0)^{\top}$ und $\mathbf{v}=(0,\,1,\,2)^{\top}$.

</li>

<li>

Schreibe $(4,\,-1,\,2)^{\top}$ als Linearkombination der Einheitsvektoren des $\mathbb{R}^3$.

</li>

<li>

Finde Zahlen $c_1,c_2$ mit $c_1(1,\,2)^{\top}+c_2(2,\,1)^{\top}=(3,\,3)^{\top}$. Zeichne die Lösung mit Pfeilen.

</li>

<li>

Berechne $\mathbf{x}_3-\mathbf{x}_2$ für den Wohnungsdatensatz und beschreibe in Worten, was der Vektor aussagt.

</li>

</ol>

:::loesung
(a) Komponente für Komponente: $2\mathbf{u}=(2,\,-2,\,0)^{\top}$ und $3\mathbf{v}=(0,\,3,\,6)^{\top}$, also $2\mathbf{u}-3\mathbf{v}=(2,\,-5,\,-6)^{\top}$.

(b) Nach [(1.6)](#gl-1-6) sind die Koeffizienten die Komponenten: $(4,\,-1,\,2)^{\top}=4\,\mathbf{e}_1-\mathbf{e}_2+2\,\mathbf{e}_3$.

(c) Komponentenweise lautet die Bedingung $c_1+2c_2=3$ und $2c_1+c_2=3$. Zieht man die erste Gleichung zweimal von der zweiten ab, bleibt $-3c_2=-3$, also $c_2=1$ und dann $c_1=1$. Probe: $(1,\,2)^{\top}+(2,\,1)^{\top}=(3,\,3)^{\top}$. In der Zeichnung hängt man den Pfeil $(2,\,1)^{\top}$ an die Spitze von $(1,\,2)^{\top}$ und landet bei $(3,\,3)^{\top}$.

(d) $\mathbf{x}_3-\mathbf{x}_2=(90-40,\ 4-1,\ 6-1)^{\top}=(50,\,3,\,5)^{\top}$: Wohnung 3 ist $50\,\mathrm m^2$ größer als Wohnung 2, hat drei Zimmer mehr und liegt $5$ km weiter vom Zentrum entfernt. Der Vektor ist der Pfeil vom Punkt $\mathbf{x}_2$ zum Punkt $\mathbf{x}_3$.
:::
:::

:::aufgabe Aufgabe 3 ★ Ein eigener Datensatz
<span class="anker" id="aufg-3"></span>

Wähle vier Dinge aus deinem Alltag, zum Beispiel Lebensmittel, Fahrräder oder Lieder, und drei Eigenschaften, die du für jedes Ding als Zahl angeben kannst. Miss oder recherchiere die Werte.

<ol class="al">

<li>

Lege die Tabelle an. Was sind $N$ und $d$? Schreibe das zweite Beispiel als Vektor $\mathbf{x}_2$.

</li>

<li>

Welche Eigenschaft, die dich auch interessieren würde, ist keine Zahl? Wie könnte man sie in Zahlen übersetzen?

</li>

<li>

Berechne den Mittelwert der Beispiele $\bar{\mathbf{x}}$. Gibt es ein Ding, das genau so aussieht?

</li>

</ol>

:::loesung
Eine mögliche Lösung: vier Äpfel mit den Merkmalen Masse in g, Durchmesser in cm und Preis in Cent.

(a) Die Tabelle habe die Zeilen $(180,\,7{,}5,\,45)$, $(150,\,7{,}0,\,40)$, $(210,\,8{,}0,\,55)$ und $(165,\,7{,}2,\,40)$. Dann ist $N=4$ und $d=3$, und $\mathbf{x}_2=(150;\ 7{,}0;\ 40)^{\top}$. Wichtig ist nur, dass jedes Ding durch dieselben drei Merkmale in derselben Reihenfolge beschrieben ist.

(b) Die Sorte ist ein Name, keine Zahl. Man kann sie übersetzen, indem man für jede Sorte ein eigenes Merkmal einführt, das $1$ ist, wenn der Apfel zu dieser Sorte gehört, und sonst $0$. Einfach die Sorten durchzunummerieren ist dagegen meist keine gute Idee: Die Nummern täuschen eine Reihenfolge und Abstände vor, die es zwischen Sorten nicht gibt.

(c) Der Mittelwert der Beispiele ist Komponente für Komponente der Durchschnitt, hier $\bar{\mathbf{x}}=(176{,}25;\ 7{,}425;\ 45)^{\top}$. Einen Apfel mit genau diesen Werten gibt es in der Tabelle nicht. Der Mittelwert ist ein gedachtes Beispiel, kein gemessenes, und bei einer Eigenschaft wie der Zimmerzahl kann er sogar ein Wert sein, den kein echtes Ding annehmen kann, etwa $2{,}5$ Zimmer.
:::
:::
