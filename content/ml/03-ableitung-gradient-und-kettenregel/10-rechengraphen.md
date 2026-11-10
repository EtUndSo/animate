---
title: Rechengraphen
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Ableitung, Gradient und Kettenregel
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Kapitel 3: Ableitung, Gradient und Kettenregel
nachschlagen: ja
order: 15231000
summary: Lange Formeln wertet ein Rechner Schritt für Schritt aus, und jeder Schritt ist eine einfache Operation mit bekannter Ableitung.
tags: Rechengraph, Vorwärtsrechnung, lokale Ableitung
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Lange Formeln wertet ein Rechner Schritt für Schritt aus, und jeder Schritt ist eine einfache Operation mit bekannter Ableitung. Ein Rechengraph macht diese Schritte und ihre Abhängigkeiten sichtbar. Dieser Abschnitt zeichnet einen solchen Graphen, rechnet ihn als Tabelle vorwärts aus und schreibt an jede Kante ihre lokale Ableitung. Damit ist alles vorbereitet, um die Ableitungen des Ergebnisses nach allen Eingängen mechanisch zu berechnen.
:::

### Zwischenergebnisse

<span class="anker" id="stufe-9-1"></span>

Mit den Regeln aus Abschnitt [1.4](die-ableitung.html#stufe-1-4) kann man jede Formel ableiten, die aus Grundrechenarten und bekannten Funktionen besteht. Schreibt man das Ergebnis als Formel aus, wird es aber oft viel länger als die Funktion selbst. Ein Produkt aus $n$ Faktoren hat nach der Produktregel eine Ableitung aus $n$ Summanden mit je $n$ Faktoren; die Formel wächst also mit $n^2$, während die Funktion nur $n$ Faktoren hat. Mit Zwischenergebnissen bleibt die Rechnung dagegen klein. Man merkt sich nach jedem Schritt den bisherigen Wert und die bisherige Ableitung und rechnet mit Zahlen weiter, nicht mit Formeln.

::::beispiel [Rechenbeispiel]
Es sei $p(x)=(x+1)(x+2)(x+3)(x+4)$ und gesucht ist $p'(0)$. Die ausgeschriebene Produktregel ergibt vier Summanden, in denen jeweils ein Faktor durch seine Ableitung $1$ ersetzt ist:

$$p'(0)=2\cdot3\cdot4+1\cdot3\cdot4+1\cdot2\cdot4+1\cdot2\cdot3=24+12+8+6=50$$

(Abb. [17](#abb-17)). Schrittweise mit den Zwischenprodukten $p_1=x+1$, $p_k=p_{k-1}\cdot(x+k)$ und der Produktregel $p_k'=p_{k-1}'\cdot(x+k)+p_{k-1}\cdot1$ geht es so:

$$\begin{gathered} p_1=1,\quad p_1'=1;\qquad p_2=1\cdot2=2,\quad p_2'=1\cdot2+1\cdot1=3;\\ p_3=2\cdot3=6,\quad p_3'=3\cdot3+2\cdot1=11;\qquad p_4=6\cdot4=24,\quad p_4'=11\cdot4+6\cdot1=50 . \end{gathered}$$

Jeder Schritt kostet zwei Multiplikationen und eine Addition, gleich wie viele Faktoren schon verarbeitet sind.

:::abbildung ml/k3rvierfaktoren 17
Die ausgeschriebene Produktregel für $p(x)=(x+1)(x+2)(x+3)(x+4)$ an der Stelle $0$: Im Summanden $k$ ist der Faktor $x+k$ durch seine Ableitung $1$ ersetzt.
:::
::::

⁠**Kurz gesagt:** Ausgeschriebene Ableitungsformeln werden schnell viel länger als die Funktion; mit Zwischenergebnissen, als Zahlen gespeichert, bleibt der Aufwand je Schritt klein.

### Der Rechengraph

<span class="anker" id="stufe-9-2"></span>

Welche Zwischenergebnisse eine Rechnung hat und wovon jedes abhängt, zeigt am übersichtlichsten ein Bild aus Knoten und Pfeilen. Ein Pfeil von einem Knoten $a$ zu einem Knoten $b$ bedeutet: $a$ wird gebraucht, um $b$ auszurechnen.

:::definition Definition 9.1 (Rechengraph)
<span class="anker" id="satz-9-1"></span>

Ein __Rechengraph__ besteht aus Knoten und gerichteten Kanten, also Pfeilen zwischen Knoten. Jeder Knoten steht für eine Zahl oder, in größeren Rechnungen, für einen ganzen Vektor oder eine Matrix. Die Eingangsknoten sind die Eingänge der Rechnung; jeder andere Knoten $v$ entsteht durch eine Grundoperation aus den Knoten, von denen eine Kante zu $v$ führt. Diese heißen Vorgänger von $v$, und $v$ heißt ihr Nachfolger. Folgt man den Kanten, kommt man nie zu einem Knoten zurück, an dem man schon war; ein solcher Graph heißt kreisfrei. Ein ausgezeichneter Knoten ist das Ergebnis.
:::

Grundoperationen sind die Grundrechenarten und Funktionen einer Variablen wie das Quadrat, die e-Funktion oder die logistische Funktion. Weil der Graph kreisfrei ist, kann man die Knoten immer so anordnen, dass jeder Knoten nach seinen Vorgängern kommt; in dieser Reihenfolge rechnet man. Ein Rechenprogramm mit Schleifen und Verzweigungen ergibt für bestimmte Eingangswerte ebenfalls einen solchen Graphen: Eine Schleife, die dreimal durchlaufen wird, liefert dreimal hintereinander dieselben Knoten.

::::beispiel [Rechenbeispiel]
Das Beispiel dieses und des nächsten Abschnitts ist

<span class="anker" id="gl-9-1"></span>
$$f(x_1,x_2,x_3)=(x_1+x_2)\,(x_2+x_3) \tag{9.1}$$

mit den Zwischenergebnissen $v_1=x_1+x_2$ und $v_2=x_2+x_3$ und dem Ergebnis $f=v_1\cdot v_2$. Der Graph hat drei Eingangsknoten, zwei Additionsknoten und einen Multiplikationsknoten, verbunden durch sechs Kanten (Abb. [18](#abb-18)). Der Eingang $x_2$ hat zwei Nachfolger; der Graph verzweigt sich dort.

:::abbildung ml/k3graph 18
Der Rechengraph von $f=(x_1+x_2)\,(x_2+x_3)$. Die Pfeile zeigen in Rechenrichtung, die Kreise enthalten die Grundoperation. Grün stehen die Werte der Vorwärtsrechnung an der Stelle $(1,\,2,\,3)$.
:::
::::

⁠**Kurz gesagt:** Ein Rechengraph zerlegt eine Rechnung in Grundoperationen; seine Kanten zeigen, welcher Wert in welchen anderen eingeht, und weil er kreisfrei ist, gibt es immer eine Reihenfolge, in der man ihn ausrechnen kann.

### Die Vorwärtsrechnung

<span class="anker" id="stufe-9-3"></span>

Einen Rechengraphen auszuwerten heißt, die Knoten in einer Reihenfolge zu berechnen, in der jeder Knoten nach seinen Vorgängern kommt. Schreibt man die Schritte untereinander, entsteht eine Tabelle, die man auch für die Ableitungen braucht: Alle Werte werden gespeichert, nicht nur das Ergebnis.

:::definition Definition 9.2 (Vorwärtsrechnung)
<span class="anker" id="satz-9-2"></span>

Die __Vorwärtsrechnung__ eines Rechengraphen berechnet alle Knoten in einer Reihenfolge, in der jeder Knoten nach seinen Vorgängern kommt, und speichert jeden Wert.
:::

::::beispiel [Rechenbeispiel]
Für [(9.1)](#gl-9-1) an der Stelle $(1,\,2,\,3)$ ergibt sich Tabelle [3](#tab-3).

<span class="anker" id="tab-3"></span>

**Tabelle 3:** Die Vorwärtsrechnung für $f=(x_1+x_2)\,(x_2+x_3)$ an der Stelle $(1,\,2,\,3)$.

| Knoten | Rechnung | Wert |
|---|---|---|
| $x_1$ | Eingang | $1$ |
| $x_2$ | Eingang | $2$ |
| $x_3$ | Eingang | $3$ |
| $v_1$ | $x_1+x_2$ | $3$ |
| $v_2$ | $x_2+x_3$ | $5$ |
| $f$ | $v_1\cdot v_2$ | $15$ |
::::

⁠**Kurz gesagt:** Die Vorwärtsrechnung wertet den Graphen Knoten für Knoten aus und speichert jeden Zwischenwert.

### Lokale Ableitungen

<span class="anker" id="stufe-9-4"></span>

Jede Kante verbindet einen Knoten mit einem Nachfolger, der durch eine Grundoperation aus ihm entsteht. Wie stark der Nachfolger auf eine kleine Änderung dieses einen Vorgängers reagiert, ist eine gewöhnliche partielle Ableitung der Grundoperation.

:::definition Definition 9.3 (Lokale Ableitung)
<span class="anker" id="satz-9-3"></span>

Für eine Kante von $a$ nach $b$ heißt die partielle Ableitung $\partial b/\partial a$ der Grundoperation, die $b$ berechnet, nach ihrem Eingang $a$ die __lokale Ableitung__ der Kante. Sie wird mit den gespeicherten Werten der Vorwärtsrechnung ausgewertet.
:::

Für die Grundoperationen sind die lokalen Ableitungen einfach (Tabelle [4](#tab-4)). Bemerkenswert ist, wie wenig sie brauchen: Bei der e-Funktion und der logistischen Funktion genügt der gespeicherte Wert des Nachfolgers selbst. Der Maximum-Knoten hat einen Knick, wenn beide Eingänge gleich sind; dort benutzt man einen der beiden einseitigen Werte.

<span class="anker" id="tab-4"></span>

**Tabelle 4:** Lokale Ableitungen der Grundoperationen, ausgedrückt durch gespeicherte Werte.

| Operation | lokale Ableitungen | benötigte Werte |
|---|---|---|
| $b=a_1+a_2$ | $\partial b/\partial a_1=1$, $\ \partial b/\partial a_2=1$ | keine |
| $b=a_1\cdot a_2$ | $\partial b/\partial a_1=a_2$, $\ \partial b/\partial a_2=a_1$ | die Eingänge |
| $b=a^2$ | $\partial b/\partial a=2a$ | der Eingang |
| $b=\mathrm{e}^a$ | $\partial b/\partial a=\mathrm{e}^a=b$ | der Ausgang |
| $b=\sigma(a)$ | $\partial b/\partial a=b\,(1-b)$ | der Ausgang |
| $b=\max(a_1,a_2)$ | $1$ für den größeren Eingang, $0$ für den anderen | welcher größer ist |

Mit den lokalen Ableitungen ist die Kettenregel aus Abschnitt [6.2](die-kettenregel-fur-mehrere-variablen.html#stufe-6-2) eine reine Zählaufgabe: Die Ableitung des Ergebnisses nach einem Eingang ist die Summe über alle Wege vom Eingang zum Ergebnis, und entlang jedes Wegs multipliziert man die lokalen Ableitungen seiner Kanten.

::::beispiel [Rechenbeispiel]
Im Graphen von Abb. [18](#abb-18) haben die vier Kanten von den Eingängen zu den Additionsknoten die lokale Ableitung $1$. Die Kante von $v_1$ zum Ergebnis hat $\partial f/\partial v_1=v_2=5$, die von $v_2$ hat $\partial f/\partial v_2=v_1=3$. Von $x_1$ führt ein Weg zum Ergebnis, von $x_3$ ebenfalls, von $x_2$ führen zwei. Also ist

$$\frac{\partial f}{\partial x_1}=1\cdot5=5,\qquad \frac{\partial f}{\partial x_2}=1\cdot5+1\cdot3=8,\qquad \frac{\partial f}{\partial x_3}=1\cdot3=3 .$$

Probe: Ausmultipliziert ist $f=x_1x_2+x_1x_3+x_2^2+x_2x_3$ mit den partiellen Ableitungen $x_2+x_3=5$, $x_1+2x_2+x_3=8$ und $x_1+x_2=3$.
::::

⁠**Kurz gesagt:** Jede Kante trägt die lokale Ableitung ihrer Grundoperation, ausgewertet mit den gespeicherten Werten; die Ableitung des Ergebnisses ist die Summe über alle Wege der Produkte dieser Zahlen.

:::aufgabe Aufgabe 32 ★ Ein Graph mit einem Quadrat
<span class="anker" id="aufg-32"></span>

Es sei $f(x_1,x_2,x_3)=(x_1x_2+x_3)^2$.

<ol class="al">

<li>

Zeichne den Rechengraphen mit den Zwischenergebnissen $v_1=x_1x_2$, $v_2=v_1+x_3$ und $f=v_2^2$.

</li>

<li>

Stelle die Tabelle der Vorwärtsrechnung an der Stelle $(1,\,2,\,3)$ auf und schreibe an jede Kante ihre lokale Ableitung.

</li>

<li>

Berechne alle drei partiellen Ableitungen als Summen über die Wege und mache die Probe.

</li>

</ol>

:::loesung
(a) Eingänge $x_1,x_2,x_3$; ein Multiplikationsknoten $v_1$ mit Kanten von $x_1$ und $x_2$; ein Additionsknoten $v_2$ mit Kanten von $v_1$ und $x_3$; ein Quadratknoten $f$ mit einer Kante von $v_2$.

(b) Vorwärts: $x_1=1$, $x_2=2$, $x_3=3$, $v_1=2$, $v_2=5$, $f=25$. Lokale Ableitungen: $\partial v_1/\partial x_1=x_2=2$, $\partial v_1/\partial x_2=x_1=1$, $\partial v_2/\partial v_1=1$, $\partial v_2/\partial x_3=1$, $\partial f/\partial v_2=2v_2=10$.

(c) Von jedem Eingang führt genau ein Weg zum Ergebnis:

$$\frac{\partial f}{\partial x_1}=2\cdot1\cdot10=20,\qquad \frac{\partial f}{\partial x_2}=1\cdot1\cdot10=10,\qquad \frac{\partial f}{\partial x_3}=1\cdot10=10 .$$

Probe: $\partial_1f=2\,(x_1x_2+x_3)\,x_2=20$, $\partial_2f=2\,(x_1x_2+x_3)\,x_1=10$, $\partial_3f=2\,(x_1x_2+x_3)=10$.
:::
:::

:::aufgabe Aufgabe 33 ★★ Fünf Faktoren
<span class="anker" id="aufg-33"></span>

Es sei $p(x)=(x+1)(x+2)(x+3)(x+4)(x+5)$.

<ol class="al">

<li>

Berechne $p'(1)$ schrittweise mit Zwischenprodukten wie im Rechenbeispiel zu Abschnitt [9.1](#stufe-9-1).

</li>

<li>

Wie viele Multiplikationen braucht die ausgeschriebene Produktregel, wie viele die schrittweise Rechnung? Wie wächst beides mit der Zahl $n$ der Faktoren?

</li>

</ol>

:::loesung
(a) An der Stelle $1$ sind die Faktoren $2,3,4,5,6$. Schrittweise:

$$\begin{aligned} p_1&=2, & p_1'&=1,\\ p_2&=2\cdot3=6, & p_2'&=1\cdot3+2\cdot1=5,\\ p_3&=6\cdot4=24, & p_3'&=5\cdot4+6\cdot1=26,\\ p_4&=24\cdot5=120, & p_4'&=26\cdot5+24\cdot1=154,\\ p_5&=120\cdot6=720, & p_5'&=154\cdot6+120\cdot1=1044 . \end{aligned}$$

Also ist $p'(1)=1044$. Probe: $p'(1)=p(1)\bigl(\tfrac12+\tfrac13+\tfrac14+\tfrac15+\tfrac16\bigr)=720\cdot\tfrac{87}{60}=1044$.

(b) Ausgeschrieben hat die Produktregel $n$ Summanden mit je $n-1$ Faktoren, also $n\,(n-2)$ Multiplikationen; für $n=5$ sind das $15$. Schrittweise braucht jeder der $n-1$ Schritte zwei Multiplikationen, für $n=5$ also $8$. Die ausgeschriebene Formel wächst mit $n^2$, die schrittweise Rechnung mit $n$.
:::
:::

:::aufgabe Aufgabe 34 ★★ Eine Schleife als Graph
<span class="anker" id="aufg-34"></span>

Ein Programm setzt $y=x$ und quadriert $y$ dann dreimal hintereinander.

<ol class="al">

<li>

Zeichne den Rechengraphen und gib die Funktion $y(x)$ an.

</li>

<li>

Berechne an der Stelle $x=2$ alle Zwischenwerte und die lokalen Ableitungen und daraus $y'(2)$. Vergleiche mit der Ableitung der Formel aus (a).

</li>

</ol>

:::loesung
(a) Der Graph ist eine Kette $x\to y_1\to y_2\to y_3$ aus drei Quadratknoten, $y_k=y_{k-1}^2$. Es ist $y=((x^2)^2)^2=x^8$.

(b) An der Stelle $2$: $y_1=4$, $y_2=16$, $y_3=256$. Die lokalen Ableitungen sind $2\cdot2=4$, $2\cdot4=8$ und $2\cdot16=32$, ihr Produkt $4\cdot8\cdot32=1024$. Die Formel ergibt $8x^7=8\cdot128=1024$.
:::
:::
