---
title: Stufe 7: Stempel und Netzliste
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Maschenstrom- und Knotenpotentialverfahren
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

⁠**So liest man das:** Zuerst bekommt jeder der $k$ Knoten eine Zeile und eine Spalte, auch der Bezugsknoten. Diese volle Matrix hat die Determinante null, weil alle Zeilen die Summe null haben: Hebt man alle Potenziale gemeinsam an, fließt nirgends ein zusätzlicher Strom. Physikalisch bestimmt ein Netz nur Differenzen. Erst das Festlegen von $U_0=0$ macht die Lösung eindeutig: Man streicht die Spalte 0, weil ihre Unbekannte null ist, und die Zeile 0, weil sie aus den übrigen Knotenregeln folgt ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Übrig bleibt $\mathbf Y$ aus Stufe [5](das-knotenpotentialverfahren.html#stufe-5). **Gültigkeit:** Die Stempel gelten für lineare Bauteile. Spannungsquellen folgen in Stufe [9](die-modifizierte-knotenanalyse.html#stufe-9).

**Netzliste.** Ein Schaltplan wird als __Netzliste__ gespeichert: je Bauteil eine Zeile aus Name, Knoten und Wert. Bei SPICE heißt `R3 1 2 2k`: Widerstand zwischen den Knoten 1 und 2. `I2 0 2 4m` heißt: 4 mA durch die Quelle von Knoten 0 nach Knoten 2. Das Programm geht die Liste Zeile für Zeile durch und stempelt. Taucht ein neuer Knotenname auf, wächst die Matrix um eine Zeile und eine Spalte. Ihre Größe muss vorher niemand kennen. Das starre Format stammt aus den 1970er-Jahren, als SPICE in FORTRAN geschrieben war und jede Zeile eine Lochkarte belegte.

**Beispiel.** Das Rechenmodell mit umgewandelter Batterie ergibt diese Liste:

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

Jede Zeile summiert sich zu null. Streicht man Zeile und Spalte 0, bleibt das System aus Stufe [5](das-knotenpotentialverfahren.html#stufe-5). **Kontrolle:** Im gestrichenen $\mathbf Y$ ist die Zeilensumme der Leitwert nach Masse: $1{,}75-0{,}5=1{,}25=G_1+G_2$ und $0{,}8-0{,}5=0{,}3=G_4+G_5$. **Grenzfall:** Ein Knoten ohne Zweig zur Masse hat die Zeilensumme null.

**Große Netze.** Ein Knoten hängt meist nur an zwei bis fünf Nachbarn, deshalb sind fast alle Plätze einer großen Matrix null. Sie heißt __dünn besetzt__. Der Simulator speichert nur die Einträge ungleich null und löst das System durch schrittweises Eliminieren. Die cramersche Regel wäre dafür unbrauchbar: Eine Determinante mit 20 Zeilen hat nach dem Muster von [(0.1)](von-grund-auf-drei-gleichungen-drei-unbekannte.html#gl-0-1) rund $2{,}4\cdot10^{18}$ Produkte.

:::zusatz Wechselstrom, Kondensator, Diode
Bei sinusförmigen Größen rechnet man mit komplexen Leitwerten, den Admittanzen. Daher kommen die Buchstaben $Y$ und $Z$. Ein Kondensator hat denselben Stempel wie ein Leitwert. Eine Impedanz $Z$ lässt sich nur als $Y=1/Z$ eintragen, solange sie nicht null ist, eine Spule bei Frequenz null sprengt das. Stufe [9](die-modifizierte-knotenanalyse.html#stufe-9) löst dieses Problem. Nichtlineare Bauteile wie Dioden ([Teil 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) ersetzt der Simulator durch die Tangente ihrer Kennlinie, stempelt diese und wiederholt das, bis sich nichts mehr ändert.
:::

:::frage Warum darf man ausgerechnet die Zeile des Bezugsknotens streichen?
Jede der $k$ Knotengleichungen folgt aus den anderen ([Teil 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Man könnte jede streichen. Die Zeile des Bezugsknotens streicht man, weil zusammen mit seiner Spalte wieder eine symmetrische Matrix entsteht und weil der Strom in die Masse selten interessiert.
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
