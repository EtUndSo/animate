---
title: Stufe 7: Stempel und Netzliste
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1180900
summary: Ein Programm sieht keine Maschen und formt nichts um.
tags: Stempel, Netzliste, dünn besetzt
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Ein Programm sieht keine Maschen und formt nichts um. Diese Stufe zeigt, wie die Matrix Bauteil für Bauteil entsteht, ohne dass ein Bauteil die anderen kennen muss.
:::

**Die Idee.** Ein Bauteil berührt nur seine zwei Knoten. Sein Strom kommt deshalb in genau zwei Knotengleichungen vor, in der einen mit Plus, in der anderen mit Minus. Jedes Bauteil hat also ein festes Eintragsmuster, seinen __Stempel__ (Abb. [7](#abb-7)). Man beginnt mit einer Matrix voller Nullen und addiert Bauteil für Bauteil seinen Stempel. Die Reihenfolge ist gleichgültig.

:::abbildung et1/k8stempel 7
Eintragsmuster in Zeilen und Spalten der Knoten. Links: Leitwert $G$ zwischen $i$ und $k$. Mitte: feste Stromquelle, die $I_\mathrm q$ von $k$ nach $i$ schiebt, sie trägt nur rechts ein. Rechts: spannungsgesteuerte Stromquelle $g\,U_{pq}$ von $i$ nach $k$. Sie steht in den Zeilen $i$, $k$, aber in den Spalten $p$, $q$ (Stufe [8](gesteuerte-quellen-und-verstarker.html#stufe-8)).
:::

:::satz Satz 7.1 (Stempel von Leitwert und Stromquelle)
<span class="anker" id="satz-7-1"></span>

Jede Zeile ist die Knotenregel „abfließende Ströme = eingeprägte Ströme“.

<ul>

<li>

Ein Leitwert $G$ zwischen $i$ und $k$ führt den Strom $I_Y=G\,(U_i-U_k)$ von $i$ nach $k$. Er addiert $+G$ auf die Plätze $(i,i)$ und $(k,k)$ und $-G$ auf $(i,k)$ und $(k,i)$.

</li>

<li>

Eine feste Stromquelle, die $I_\mathrm q$ durch sich von $k$ nach $i$ schiebt, addiert $+I_\mathrm q$ in Zeile $i$ und $-I_\mathrm q$ in Zeile $k$ der rechten Seite. In $\mathbf Y$ trägt sie nichts ein, denn ihr Strom hängt von keiner Spannung ab.

</li>

</ul>
:::

⁠**So liest man das:** Zuerst bekommt jeder der $k$ Knoten eine Zeile und eine Spalte, auch der Bezugsknoten. Diese volle Matrix hat die Determinante null, weil alle Zeilen die Summe null haben: Hebt man alle Potenziale gemeinsam an, fließt nirgends ein zusätzlicher Strom. Physikalisch bestimmt ein Netz nur Differenzen. Erst das Festlegen von $U_0=0$ macht die Lösung eindeutig: Man streicht die Spalte 0, weil ihre Unbekannte null ist, und die Zeile 0, weil sie aus den übrigen Knotenregeln folgt ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Übrig bleibt $\mathbf Y$ aus Stufe [5](das-knotenpotentialverfahren.html#stufe-5). **Gültigkeit:** Die Stempel gelten für lineare Bauteile. Spannungsquellen folgen in Stufe [9](die-modifizierte-knotenanalyse.html#stufe-9).

**Netzliste.** Ein Schaltplan wird als __Netzliste__ gespeichert: je Bauteil eine Zeile aus Name, Knoten und Wert. Bei SPICE heißt `R3 1 2 2k`: Widerstand zwischen den Knoten 1 und 2. `I2 0 2 4m` heißt: 4 mA durch die Quelle von Knoten 0 nach Knoten 2. Das Programm geht die Liste Zeile für Zeile durch und stempelt. Taucht ein neuer Knotenname auf, wächst die Matrix um eine Zeile und eine Spalte. Ihre Größe muss vorher niemand kennen. Das starre Format stammt aus den 1970er-Jahren, als SPICE in FORTRAN geschrieben war und jede Zeile eine Lochkarte belegte.

::::beispiel
Das Rechenmodell mit umgewandelter Batterie ergibt diese Liste:

| Zeile | Wert | Eintrag |
|---|---|---|
| `R1 1 0 1k` | $G_1=1$ | $+1$ auf $(1,1)$, $(0,0)$; $-1$ auf $(1,0)$, $(0,1)$ |
| `R2 1 0 4k` | $G_2=0{,}25$ | $+0{,}25$ auf $(1,1)$, $(0,0)$; $-0{,}25$ auf $(1,0)$, $(0,1)$ |
| `R3 1 2 2k` | $G_3=0{,}5$ | $+0{,}5$ auf $(1,1)$, $(2,2)$; $-0{,}5$ auf $(1,2)$, $(2,1)$ |
| `R4 2 0 10k` | $G_4=0{,}1$ | $+0{,}1$ auf $(2,2)$, $(0,0)$; $-0{,}1$ auf $(2,0)$, $(0,2)$ |
| `R5 2 0 5k` | $G_5=0{,}2$ | $+0{,}2$ auf $(2,2)$, $(0,0)$; $-0{,}2$ auf $(2,0)$, $(0,2)$ |
| `I1 0 1 9m` | $I=9$ | rechts $+9$ in Zeile 1, $-9$ in Zeile 0 |
| `I2 0 2 4m` | $I=4$ | rechts $+4$ in Zeile 2, $-4$ in Zeile 0 |

Mit den Zeilen und Spalten in der Folge 0, 1, 2 entsteht

$$\begin{pmatrix}1{,}55&-1{,}25&-0{,}3\\-1{,}25&1{,}75&-0{,}5\\-0{,}3&-0{,}5&0{,}8\end{pmatrix} \begin{pmatrix}U_0\\U_1\\U_2\end{pmatrix}=\begin{pmatrix}-13\\9\\4\end{pmatrix}.$$

Jede Zeile summiert sich zu null. Streicht man Zeile und Spalte 0, bleibt das System aus Stufe [5](das-knotenpotentialverfahren.html#stufe-5). **Kontrolle:** Im gestrichenen $\mathbf Y$ ist die Zeilensumme der Leitwert nach Masse: $1{,}75-0{,}5=1{,}25=G_1+G_2$ und $0{,}8-0{,}5=0{,}3=G_4+G_5$.
::::

⁠**Grenzfall:** Ein Knoten ohne Zweig zur Masse hat die Zeilensumme null.

**Große Netze.** Ein Knoten hängt meist nur an zwei bis fünf Nachbarn, deshalb sind fast alle Plätze einer großen Matrix null. Sie heißt __dünn besetzt__. Der Simulator speichert nur die Einträge ungleich null und löst das System durch schrittweises Eliminieren. Die cramersche Regel wäre dafür unbrauchbar: Eine Determinante mit 20 Zeilen hat nach dem Muster von [(0.1)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-1) rund $2{,}4\cdot10^{18}$ Produkte.

:::zusatz Wechselstrom, Kondensator, Diode
Bei sinusförmigen Größen rechnet man mit komplexen Leitwerten, den Admittanzen. Daher kommen die Buchstaben $Y$ und $Z$. Ein Kondensator hat denselben Stempel wie ein Leitwert. Eine Impedanz $Z$ lässt sich nur als $Y=1/Z$ eintragen, solange sie nicht null ist, eine Spule bei Frequenz null sprengt das. Stufe [9](die-modifizierte-knotenanalyse.html#stufe-9) löst dieses Problem. Nichtlineare Bauteile wie Dioden ([Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) ersetzt der Simulator durch die Tangente ihrer Kennlinie, stempelt diese und wiederholt das, bis sich nichts mehr ändert.
:::

:::frage Warum darf man ausgerechnet die Zeile des Bezugsknotens streichen?
Jede der $k$ Knotengleichungen folgt aus den anderen ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Man könnte jede streichen. Die Zeile des Bezugsknotens streicht man, weil zusammen mit seiner Spalte wieder eine symmetrische Matrix entsteht und weil der Strom in die Masse selten interessiert.
:::

:::aufgabe Aufgabe 9 ★★ Von der Netzliste zur Lösung
<span class="anker" id="aufg-9"></span>

Gegeben ist die Liste `R1 1 0 1k`, `R2 1 2 2k`, `R3 2 0 2k`, `I1 0 1 7m`, `I2 2 1 1m`.

<ol class="al">

<li>

Stemple die volle $3\times3$-Matrix und die rechte Seite. Prüfe die Zeilensummen.

</li>

<li>

Streiche den Bezugsknoten und löse.

</li>

<li>

Probe: Welcher Strom fließt über die Widerstände in die Masse, und welcher kommt aus ihr?

</li>

</ol>

:::loesung
(a) Mit den Leitwerten 1, 0,5, 0,5 mS und Zeilen 0, 1, 2:

$$\begin{pmatrix}1{,}5&-1&-0{,}5\\-1&1{,}5&-0{,}5\\-0{,}5&-0{,}5&1\end{pmatrix}\begin{pmatrix}U_0\\U_1\\U_2\end{pmatrix}=\begin{pmatrix}-7\\8\\-1\end{pmatrix}.$$

`I2 2 1 1m` schiebt 1 mA von 2 nach 1, also $+1$ in Zeile 1 und $-1$ in Zeile 2. Alle Zeilensummen sind null, auch rechts ist die Summe null.

(b) $\begin{pmatrix}1{,}5&-0{,}5\\-0{,}5&1\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}8\\-1\end{pmatrix}$ mit $D=1{,}25$, $D_1=7{,}5$, $D_2=2{,}5$. Also $U_1=6$ V, $U_2=2$ V.

(c) Über `R1` fließen 6 mA in die Masse, über `R3` 1 mA, zusammen 7 mA. Aus der Masse holt `I1` genau 7 mA.
:::
:::

::::formelsammlung
**Stempel eines Leitwerts**

$$I_Y=G\,(U_i-U_k)$$

Leitwert $G$ zwischen den Knoten $i$ und $k$, Strom von $i$ nach $k$. Er addiert $+G$ auf die Plätze $(i,i)$ und $(k,k)$ und $-G$ auf $(i,k)$ und $(k,i)$.

**Stempel einer festen Stromquelle**

$$+I_\mathrm q\ \text{in Zeile } i,\qquad -I_\mathrm q\ \text{in Zeile } k$$

Die Quelle schiebt $I_\mathrm q$ durch sich von $k$ nach $i$. Sie trägt nur auf der rechten Seite ein, in $\mathbf Y$ nichts, denn ihr Strom hängt von keiner Spannung ab. Jede Zeile ist die Knotenregel „abfließende Ströme = eingeprägte Ströme“.

**Bezugsknoten festlegen**

$$U_0=0$$

In der vollen Matrix aller $k$ Knoten hat jede Zeile die Summe null, die Determinante ist null. Mit $U_0=0$ streicht man Spalte 0 (ihre Unbekannte ist null) und Zeile 0 (sie folgt aus den übrigen Knotenregeln); übrig bleibt $\mathbf Y$. Kontrolle: Im gestrichenen $\mathbf Y$ ist die Zeilensumme der Leitwert vom Knoten nach Masse.
::::

::::lernkarten
:::karte begriff Stempel
Was versteht man unter dem Stempel eines Bauteils, wenn ein Programm die Knotengleichungen aufstellt?
---
Das feste Eintragsmuster eines Bauteils in Matrix und rechter Seite. Ein Bauteil berührt nur seine zwei Knoten, sein Strom steht deshalb in genau zwei Knotengleichungen, einmal mit Plus und einmal mit Minus.
--- falsch
Die Zeile der Netzliste, mit der ein Bauteil beschrieben wird: Name, Knoten und Wert. Das Programm liest den Stempel und leitet daraus die Maschen ab, in denen das Bauteil liegt.
--- falsch
Das feste Eintragsmuster, das ein Bauteil in die Matrix einträgt. Es hängt aber von allen anderen Bauteilen am selben Knoten ab, deshalb muss das Programm die Bauteile in einer festen Reihenfolge stempeln.
--- falsch
Der Wert, den ein Bauteil auf der Diagonale der Matrix hinterlässt. Einträge neben der Diagonale entstehen erst, wenn das Programm am Ende alle Stempel miteinander verrechnet.
:::
:::karte formel Stempel eines Leitwerts
Welche Einträge addiert ein Leitwert $G$ zwischen den Knoten $i$ und $k$ in die Knotenmatrix, und welchen Strom führt er?
---
Er führt $I_Y=G\,(U_i-U_k)$ von $i$ nach $k$. Er addiert $+G$ auf die Plätze $(i,i)$ und $(k,k)$ und $-G$ auf die Plätze $(i,k)$ und $(k,i)$.
--- falsch
Er führt $I_Y=G\,(U_i-U_k)$ von $i$ nach $k$. Er addiert $+G$ auf die Plätze $(i,k)$ und $(k,i)$ und $-G$ auf die Plätze $(i,i)$ und $(k,k)$.
--- falsch
Er führt $I_Y=G\,(U_i-U_k)$ von $i$ nach $k$. Er addiert nur $+G$ auf den Platz $(i,i)$ und $-G$ auf $(k,k)$, weil der Strom bei $i$ abfließt und bei $k$ zufließt.
--- falsch
Er führt $I_Y=G\,(U_i+U_k)$ von $i$ nach $k$. Er addiert $+G$ auf alle vier Plätze $(i,i)$, $(k,k)$, $(i,k)$ und $(k,i)$, weil er beide Knoten gleich belastet.
:::
:::karte formel Stempel einer festen Stromquelle
Wo trägt eine feste Stromquelle etwas ein, die den Strom $I_\mathrm q$ durch sich von Knoten $k$ nach Knoten $i$ schiebt?
---
Nur auf der rechten Seite: $+I_\mathrm q$ in Zeile $i$ und $-I_\mathrm q$ in Zeile $k$. In $\mathbf Y$ trägt sie nichts ein, denn ihr Strom hängt von keiner Spannung ab.
--- falsch
Nur auf der rechten Seite: $-I_\mathrm q$ in Zeile $i$ und $+I_\mathrm q$ in Zeile $k$, weil ihr Strom aus Knoten $k$ in die Quelle hineinfließt. In $\mathbf Y$ trägt sie nichts ein.
--- falsch
In $\mathbf Y$ und auf der rechten Seite: $+I_\mathrm q$ auf $(i,i)$ und $(k,k)$, dazu $I_\mathrm q$ in Zeile $i$ rechts, weil die Quelle wie ein Leitwert zwischen ihren Knoten liegt.
--- falsch
Nur auf der rechten Seite, und zwar $+I_\mathrm q$ in Zeile $i$. Zeile $k$ bleibt leer, weil eine Quelle nur dort einspeist, wohin ihr Pfeil zeigt, und dem anderen Knoten nichts entzieht.
:::
:::karte begriff Netzliste
Wie ist eine Netzliste aufgebaut, in der ein Schaltplan für SPICE gespeichert wird?
---
Je Bauteil eine Zeile aus Name, Knoten und Wert. `R3 1 2 2k` heißt: Widerstand mit 2 k$\Omega$ zwischen den Knoten 1 und 2. `I2 0 2 4m` heißt: 4 mA durch die Quelle von Knoten 0 nach Knoten 2.
--- falsch
Je Masche eine Zeile aus Name, Bauteilen und Umlaufsinn. `R3 1 2 2k` heißt: Widerstand mit 2 k$\Omega$, der zu den Maschen 1 und 2 gehört. `I2 0 2 4m` heißt: Masche 2 führt 4 mA.
--- falsch
Je Bauteil eine Zeile aus Name, Knoten und Wert. `R3 1 2 2k` heißt: Widerstand mit 2 k$\Omega$ zwischen den Knoten 1 und 2. `I2 0 2 4m` heißt: 4 mA durch die Quelle von Knoten 2 nach Knoten 0.
--- falsch
Je Knoten eine Zeile mit allen Bauteilen, die dort hängen. `R3 1 2 2k` heißt: An Knoten 1 hängen zwei Bauteile mit zusammen 2 k$\Omega$. Die Länge der Liste muss vorher feststehen.
:::
:::karte zusammenhang Matrix aus der Netzliste
Wie entsteht aus einer Netzliste die Matrix, ohne dass das Programm ihre Größe vorher kennen muss?
---
Das Programm beginnt mit einer Matrix voller Nullen und addiert Zeile für Zeile den Stempel des Bauteils, in beliebiger Reihenfolge. Taucht ein neuer Knotenname auf, wächst die Matrix um eine Zeile und eine Spalte.
--- falsch
Das Programm zählt zuerst alle Maschen der Schaltung und legt eine Matrix dieser Größe an. Danach trägt es jedes Bauteil in die Maschen ein, durch die es läuft, streng in der Reihenfolge der Liste.
--- falsch
Das Programm liest zuerst die ganze Liste und sortiert die Bauteile nach Knoten. Erst danach legt es die Matrix an, weil ein Stempel nur stimmt, wenn alle Nachbarn eines Bauteils bekannt sind.
--- falsch
Das Programm beginnt mit einer Matrix voller Nullen und addiert Bauteil für Bauteil seinen Stempel. Taucht ein neuer Knotenname auf, wird er dem nächstgelegenen Knoten zugeschlagen, damit die Größe gleich bleibt.
:::
:::karte zusammenhang Volle Matrix ohne Lösung
Warum hat die volle Knotenmatrix, in der auch der Bezugsknoten eine Zeile und eine Spalte hat, die Determinante null?
---
Weil alle Zeilen die Summe null haben: Hebt man alle Potenziale gemeinsam an, fließt nirgends ein zusätzlicher Strom. Ein Netz bestimmt nur Differenzen, erst das Festlegen von $U_0=0$ macht die Lösung eindeutig.
--- falsch
Weil der Bezugsknoten keinen Strom führt und seine Zeile deshalb nur Nullen enthält. Eine Nullzeile macht jede Determinante null, darum muss man diese Zeile samt ihrer Spalte vor dem Lösen in jedem Fall streichen.
--- falsch
Weil jeder Leitwert zweimal positiv und zweimal negativ eingetragen wird. Dadurch heben sich alle Einträge gegenseitig auf, und die volle Matrix ist im Ganzen gleich null.
--- falsch
Weil sie symmetrisch ist. Symmetrische Matrizen haben stets die Determinante null, deshalb streicht man eine Zeile und eine Spalte, damit die Symmetrie verschwindet.
:::
:::karte zusammenhang Bezugsknoten streichen
Warum darf man in der vollen Knotenmatrix die Zeile und die Spalte des Bezugsknotens streichen?
---
Die Spalte, weil ihre Unbekannte $U_0=0$ ist. Die Zeile, weil jede Knotengleichung aus den übrigen folgt; man streicht gerade sie, weil dann wieder eine symmetrische Matrix entsteht und der Strom in die Masse selten interessiert.
--- falsch
Die Zeile, weil am Bezugsknoten keine Bauteile hängen, und die Spalte, weil sein Potenzial unbekannt bleiben darf. Übrig bleibt eine Matrix, die zwar nicht mehr symmetrisch ist, sich aber trotzdem eindeutig lösen lässt.
--- falsch
Weil nur die Zeile des Bezugsknotens aus den anderen folgt. Die übrigen Knotengleichungen sind voneinander unabhängig, deshalb darf man keine andere Zeile streichen als diese.
--- falsch
Die Spalte, weil ihre Unbekannte $U_0=0$ ist. Die Zeile muss dagegen bleiben, weil sie den Strom in die Masse enthält, ohne den das Gleichungssystem nicht lösbar wäre.
:::
:::karte zusammenhang Zeilensumme als Kontrolle
Was gibt im gestrichenen $\mathbf Y$ die Summe einer Zeile an, und wozu nutzt man das?
---
Den Leitwert vom Knoten nach Masse, denn nach dem Streichen fehlt nur dessen negativer Eintrag in Spalte 0. Im Rechenmodell ist $1{,}75-0{,}5=1{,}25=G_1+G_2$; ein Knoten ohne Zweig zur Masse hat die Zeilensumme null.
--- falsch
Den Strom, der aus dem Knoten in die Masse fließt, denn jede Zeile ist eine Knotenregel. Im Rechenmodell sind das 1,25 mA an Knoten 1. Ein Knoten ohne Zweig zur Masse hat deshalb stets die Zeilensumme eins.
--- falsch
Den Leitwert zu den Nachbarknoten, denn die Diagonale enthält nur die Leitwerte nach Masse. Im Rechenmodell sind das 0,5 mS an Knoten 1. Damit kontrolliert man die Koppelleitwerte.
--- falsch
Nichts Besonderes, denn im gestrichenen $\mathbf Y$ ist jede Zeilensumme null, wie in der vollen Matrix. Ist eine Summe ungleich null, wurde beim Stempeln ein Fehler gemacht.
:::
:::karte begriff dünn besetzt
Wann nennt man die Matrix eines großen Netzes dünn besetzt, und wie nutzt ein Simulator das?
---
Wenn fast alle Plätze null sind, weil ein Knoten meist nur an zwei bis fünf Nachbarn hängt. Der Simulator speichert nur die Einträge ungleich null und löst das System durch schrittweises Eliminieren.
--- falsch
Wenn fast alle Plätze auf der Diagonale null sind, weil viele Knoten keinen Zweig zur Masse haben. Der Simulator ergänzt dort kleine Leitwerte, damit das System lösbar bleibt.
--- falsch
Wenn fast alle Plätze null sind, weil ein Knoten meist nur wenige Nachbarn hat. Der Simulator löst das System dann mit der cramerschen Regel, die bei vielen Nullen in der Matrix besonders schnell ist.
--- falsch
Wenn die Matrix weniger Zeilen als Spalten hat, weil manche Knoten keine eigene Gleichung bekommen. Der Simulator füllt die fehlenden Zeilen mit Maschengleichungen auf.
:::
:::karte zusammenhang Cramersche Regel in großen Netzen
Warum ist die cramersche Regel für die großen Netze eines Simulators unbrauchbar?
---
Weil die Zahl der Produkte mit der Größe rasant wächst: Eine Determinante mit 20 Zeilen hat nach dem Muster der Entwicklung nach der ersten Zeile rund $2{,}4\cdot10^{18}$ Produkte. Der Simulator eliminiert stattdessen schrittweise.
--- falsch
Weil sie nur für symmetrische Matrizen gilt und große Netze fast immer unsymmetrische Matrizen haben. Der Simulator verwendet deshalb das Maschenstromverfahren, das ohne Determinanten auskommt.
--- falsch
Weil eine Determinante mit 20 Zeilen nur rund 400 Produkte hat, jedes mit 20 Faktoren. Das wäre schnell genug, aber die vielen Faktoren machen das Ergebnis für einen Rechner zu ungenau, deshalb eliminiert der Simulator schrittweise.
--- falsch
Weil Determinanten großer Matrizen immer null sind. Mit vielen Zeilen heben sich die positiven und negativen Produkte gegenseitig auf, und die Regel müsste dann durch null teilen.
:::
:::karte zusammenhang Nichtlineare Bauteile im Simulator
Wie behandelt ein Simulator ein nichtlineares Bauteil wie eine Diode, für das es keinen festen Stempel gibt?
---
Er ersetzt es durch die Tangente seiner Kennlinie, stempelt diese und löst das System. Das wiederholt er mit der neuen Lösung, bis sich nichts mehr ändert.
--- falsch
Er ersetzt es durch einen festen Widerstand mit dem Wert der Kennlinie bei 1 V und stempelt diesen einmal. Für kleine Spannungen ist das genau genug.
--- falsch
Er lässt das Bauteil zunächst weg, löst das lineare Netz und setzt es am Ende als Stromquelle mit seinem Nennstrom wieder ein.
--- falsch
Er stempelt die ganze Kennlinie als Tabelle in die Matrix. Jeder Punkt der Tabelle bekommt einen eigenen Platz, deshalb wächst die Matrix mit jedem nichtlinearen Bauteil.
:::
::::
