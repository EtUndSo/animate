---
title: Netzwerkgleichungen systematisch aufstellen: modifizierte Knotenanalyse
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse
order: 33020300
summary: Wie man das Gleichungssystem jeder linearen Schaltung Bauteil für Bauteil nach festen Eintragsmustern aufstellt, auch mit idealen Spannungsquellen, Kurzschlüssen, gesteuerten Spannungsquellen und idealen Operationsverstärkern, und wie man es mit der Cramerschen Regel löst. Kompakte Fassung mit hergeleiteten Mustern, Determinantenformeln und Cramerscher Regel; die ausführliche enthält zusätzlich eine Analogie zur vollständigen Matrix, die Herleitung des Rechenaufwands, die Inverse, Spule und Schwingkreis, die Herleitung der stromgesteuerten Quellen mit Strommesser und Transitfrequenz und den Frequenzgang mit Bode-Diagramm.
tags: Leitwertmatrix, modifizierte Knotenpotentialanalyse, Cramersche Regel, Determinante
stil: 3
fassung: kompakt
---

## Worum es geht

Wer eine große Schaltung von Hand in Knotengleichungen zerlegt, braucht Stunden und macht Vorzeichenfehler; ein Schaltungssimulator muss dasselbe für Millionen Knoten können, ohne die Schaltung anzusehen. Außerdem scheitert die Knotenanalyse an idealen Spannungsquellen, Kurzschlüssen und Strommessern, Spulen bei Gleichstrom, gesteuerten Spannungsquellen und idealen Operationsverstärkern. Beides löst ein Prinzip:

**Jedes Bauelement schreibt seinen Beitrag als festes Muster in eine Matrix, ohne den Rest der Schaltung zu kennen; Elemente, deren Strom sich weder aus den Knotenpotentialen noch aus einem schon als Unbekannte geführten Strom ergibt, bringen diesen Strom als zusätzliche Unbekannte und ihre Zweiggleichung als zusätzliche Zeile mit, und das so entstehende quadratische System liefert, wenn es eindeutig lösbar ist, jede Größe als Quotient zweier Determinanten.**

Vorausgesetzt werden die Knotenpotentialanalyse mit Leitwertmatrix und gesteuerten Stromquellen aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html), das Rechnen mit [Zeigern](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html) und für ein Beispiel [der ideale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html). Auf dem Verfahren beruhen Arbeitspunkt-, Wechselstrom- und Zeitbereichsanalyse der meisten Schaltungssimulatoren, etwa SPICE.

:::grafik
Szene: st1/netzwerkanalyse/03-netzliste-matrix · Vorlage: netzliste-matrix
**Abbildung 1:** (a) RC-Tiefpass mit idealer Spannungsquelle 1 V zwischen Knoten 1 und Masse, $R_1$ und $R_2$ je 1 kΩ, $C_1$ und $C_2$ je 100 nF, bei ω = 10⁴ 1/s. (b) Seine Netzliste, eine Zeile je Bauteil mit Knoten und Wert. (c) Die Matrix der modifizierten Knotenanalyse in mS, kΩ, V und mA, Zeilen (1; −1; 0; 1), (−1; 2 + j; −1; 0), (0; −1; 1 + j; 0), (1; 0; 0; 0), jeder Eintrag in der Farbe des Bauteils, das ihn liefert. Jedes Bauteil schreibt ein festes Muster in die Zeilen und Spalten seiner Knoten; die Matrix ist die Summe dieser Muster.
:::

## Die Matrix Bauteil für Bauteil

*Wie füllt man die Leitwertmatrix, ohne die Knotengleichungen einzeln aufzuschreiben?*

Als Beispiel dient die Verstärkerstufe aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html), eine Source-Schaltung mit einem MOSFET; ihr Kleinsignal-Ersatzschaltbild enthält eine Signalquelle von 10 mV mit 10 kΩ, Drain- und Lastwiderstand von je 10 kΩ, einen Source-Widerstand von 1 kΩ, die gesteuerte Stromquelle mit der __Steilheit__ $g_m$ = 1 mS und den __Ausgangsleitwert__ $g_o$ = 25 µS zwischen Drain und Source, der beschreibt, dass der Drainstrom mit der Drain-Source-Spannung leicht steigt. Vom Drain zur Source gezählt, fließt der Strom von $g_o$ aus dem Drain ab und in die Source hinein; er steht also nur in diesen beiden Knotengleichungen. Nach Potentialen geordnet, ergibt das +0,025 mS auf den Plätzen (D, D) und (S, S) und −0,025 mS auf (D, S) und (S, D); vom Rest der Schaltung braucht man dafür nichts zu wissen. Diesen festen Beitrag eines Bauelements nennt man sein __Eintragsmuster__, englisch stamp. Abbildung 2 zeigt die drei Muster der Knotenanalyse.

:::grafik
Szene: st1/netzwerkanalyse/03-eintragsmuster-knoten · Vorlage: musterkarten
**Abbildung 2:** Eintragsmuster für die Knotenanalyse. Links eine Admittanz zwischen den Knoten a und b: +Y auf den Plätzen (a, a) und (b, b), −Y auf (a, b) und (b, a). Mitte eine spannungsgesteuerte Stromquelle, deren Strom von a nach b fließt und von der Spannung zwischen c und d gesteuert wird: ±g in den Zeilen a, b und den Spalten c, d. Rechts eine unabhängige Stromquelle, die in a hineinspeist: nur die rechte Seite, +I in Zeile a, −I in Zeile b. Am Rand jeder Karte die Vorzeichen der Zeilen und Spalten, deren Produkt im Feld steht. Ein Bauelement erscheint nur in den Zeilen der Knoten, zwischen denen sein Strom fließt, und in den Spalten der Knoten, deren Spannung diesen Strom bestimmt.
:::

**Die Akteure:**

- __Bezugsknoten__ 0 und die übrigen Knoten; __$n_K$__: Zahl der übrigen Knoten und der Unbekannten; 3 in der Verstärkerstufe (G, D, S).
- __$\underline U_\nu$__: Potential des Knotens ν gegen den Bezugsknoten, ein Zeiger; in V.
- __$\mathbf Y$__: __Leitwertmatrix__; Zeile μ ist die Knotengleichung von μ, und der Eintrag __$\underline Y_{\mu\nu}$__ ist der Strom, der in dieser Gleichung je Volt am Knoten ν abfließt; in S.
- __$\underline I_{q\mu}$__: Summe der Ströme unabhängiger Quellen in den Knoten μ hinein; in A; die rechte Seite.
- __a__, __b__: Knoten, zwischen denen der Strom eines Bauelements fließt, gezählt von a nach b, bei der unabhängigen Stromquelle durch die Quelle von b nach a, sodass sie in a einspeist; __c__, __d__: Knoten der Steuerspannung einer gesteuerten Quelle, c am Pluspol.
- __$\underline Y$__: Admittanz eines Zweipols, $G$ oder $j\omega C$; __$g$__: Steilheit einer spannungsgesteuerten Stromquelle, beim Transistor $g_m$ = 1 mS; __$\underline I_q$__: Strom einer unabhängigen Stromquelle.

**Das Zusammenspiel:**

**Schritt 1**: Jede Zeile sagt: Die über Bauelemente abfließenden Ströme sind zusammen gleich den eingespeisten Quellenströmen.

**Schritt 2**: Ein Bauelement trägt nur zu den Zeilen a und b bei, in a als Abfluss, in b als Zufluss.

**Schritt 3**: Sein Strom ist ein festes Vielfaches der Potentiale, die ihn treiben, und die Faktoren stehen in den Spalten dieser Potentiale: bei der Admittanz in a und b, bei der gesteuerten Stromquelle in c und d; die unabhängige Stromquelle hängt von keinem Potential ab und steht nur rechts.

**Schritt 4**: Weil jede Knotengleichung eine Summe über alle Bauelemente ist, addieren sich die Muster Eintrag für Eintrag.

:::formel Formel
$$\begin{array}{c|cc} & a & b \\ \hline a & +\underline Y & -\underline Y \\ b & -\underline Y & +\underline Y \end{array}$$

$$\begin{array}{c|cc} & c & d \\ \hline a & +g & -g \\ b & -g & +g \end{array}$$

$$\begin{array}{c|c} & \text{rechts} \\ \hline a & +\underline I_q \\ b & -\underline I_q \end{array}$$
:::

**So liest man das:** Oben das Muster der Admittanz, darunter das der spannungsgesteuerten Stromquelle und das der unabhängigen Stromquelle, die in a hineinspeist. Jedes Vorzeichen ist ein Produkt aus zwei Faktoren: +1 in der Zeile des Knotens, den der Strom in Zählrichtung verlässt, −1 in der, in die er fließt; +1 in der Spalte des Knotens, dessen Potential in der Zweiggleichung mit plus steht, −1 beim anderen. Bei der Admittanz sind Strom- und Steuerknoten dieselben, daher plus auf der Diagonalen. Eine gesteuerte Stromquelle gehört in die Matrix und nicht auf die rechte Seite, denn ihr Strom hängt von unbekannten Potentialen ab.

**Kurz gesagt:** Die Leitwertmatrix einer Schaltung ist die Summe der Eintragsmuster ihrer Bauelemente, und jedes Muster hängt nur vom Bauelement und den Knoten ab, an denen es hängt.

:::fehlvorstellung
„Beim Eintragen muss man wissen, in welche Richtung der Strom wirklich fließt.“ Das liegt nahe, weil das Muster mit einer Zählrichtung aufgeschrieben ist. Bei einer Admittanz ist sie frei: Zählt man von b nach a, vertauschen sich a und b, und das Muster bleibt dasselbe. Wie der Strom zur Zählrichtung liegt, zeigt erst das Vorzeichen der Lösung; durch $R_D$ der Verstärkerstufe fließen, von D nach Masse gezählt, −2,33 µA, gegenphasig zur Signalspannung. Nur bei Quellen ist die Zählrichtung vorgegeben.
:::

Idee der Herleitung: Man schreibt die Knotengleichungen als Summe der Ströme aller Bauelemente und ordnet jeden Strom nach den Potentialen, die ihn bestimmen.

:::herleitung
**Ausgangspunkt:** die Knotenregel für Zeiger und die Zweiggleichungen der Bauelemente, für die Admittanz und die spannungsgesteuerte Stromquelle mit dem Strom $\underline I$ von a nach b; eine unabhängige Stromquelle hat den festen Strom $\underline I_q$:

$$\underline I = \underline Y\,(\underline U_a - \underline U_b), \qquad \underline I = g\,(\underline U_c - \underline U_d)$$

**Annahmen:** (i) Alle Bauelemente sind Zweipole mit endlicher Admittanz oder spannungsgesteuerte Stromquellen, ihre Ströme also feste Vielfache von Potentialdifferenzen, oder unabhängige Stromquellen. (ii) Gezählt werden die über Bauelemente abfließenden Ströme; Ströme unabhängiger Quellen stehen mit dem Vorzeichen ihres Zuflusses rechts.

**Schritt 1**: Die Knotengleichung von μ ist die Summe über alle Bauelemente, die μ berühren:

$$\sum_{\text{Bauelemente an }\mu} \underline I_{\mu,\mathrm{ab}} = \underline I_{q\mu}$$

**Schritt 2** (entscheidender Schritt): Ein Bauelement zwischen a und b trägt nur zu den Gleichungen von a und b bei: in a mit $+\underline I$, weil sein Strom dort abfließt, in b mit $-\underline I$, weil er dort ankommt. In allen anderen Knotengleichungen kommt es nicht vor.

$$\text{Zeile } a: \ +\underline I$$

$$\text{Zeile } b: \ -\underline I$$

**Schritt 3**: Für die Admittanz eingesetzt und nach Potentialen geordnet:

$$+\underline I = +\underline Y\,\underline U_a - \underline Y\,\underline U_b$$

$$-\underline I = -\underline Y\,\underline U_a + \underline Y\,\underline U_b$$

**Schritt 4**: Für die gesteuerte Stromquelle stehen statt $\underline U_a$ und $\underline U_b$ die Steuerpotentiale:

$$+\underline I = +g\,\underline U_c - g\,\underline U_d$$

$$-\underline I = -g\,\underline U_c + g\,\underline U_d$$

**Schritt 5**: Eine unabhängige Stromquelle, die in a hineinspeist, ist Zufluss in a und Abfluss aus b; auf der rechten Seite steht sie deshalb mit $+\underline I_q$ in Zeile a und $-\underline I_q$ in Zeile b.

**Ergebnis:** die drei Muster oben; die Matrix ist ihre Summe über alle Bauelemente.

**Woher die Faktoren kommen:** Das Vorzeichen der Zeile stammt aus Schritt 2 (Abfluss oder Zufluss), das der Spalte aus der Zweiggleichung (mit welchem Vorzeichen das Potential dort steht); ihr Produkt steht im Feld.

**Proben:** Einheit: S mal V ist A, wie in einer Knotengleichung. Zahlenwert: $g_o$ zwischen D und S liefert ±0,025 mS an den vier Plätzen aus D und S; $g_m$ liefert +1 mS in Zeile D, Spalte G, wie in der Matrix der Verstärkerstufe. Vorzeichen: Vertauscht man bei der Admittanz a und b, ändert sich kein Eintrag.

**Grenzen:** Elemente, deren Strom kein festes Vielfaches von Potentialen ist, etwa ideale Spannungsquellen, haben kein solches Muster; sie nimmt der Abschnitt *Die modifizierte Knotenanalyse* auf.
:::

Trägt man die Muster für alle Knoten ein, auch für die Masse, entsteht die vollständige Matrix; für die Verstärkerstufe hat sie vier Zeilen und Spalten. In ihr ist jede Zeilensumme null, weil nur Potentialdifferenzen Ströme treiben, und jede Spaltensumme null, weil jeder Strom, den eine Zeile als Abfluss bucht, in einer anderen als Zufluss steht. Die Potentiale sind deshalb nur bis auf eine gemeinsame Konstante bestimmt, und eine Gleichung ist überzählig. Man wählt einen __Bezugsknoten__ mit dem Potential null und streicht seine Zeile und seine Spalte; ein Bauelement zwischen a und dem Bezugsknoten hinterlässt dann nur $+\underline Y$ auf dem Platz (a, a).

**Kurz gesagt:** In der vollständigen Matrix ist jede Zeilensumme null, weil nur Potentialdifferenzen Ströme treiben, und jede Spaltensumme null, weil jeder Strom, der einen Knoten verlässt, in einen anderen hineinfließt.

Idee der Herleitung: Man prüft die Summen an jedem Muster einzeln, denn die Matrix ist ihre Summe, und folgert daraus, welche Zeile und Spalte überzählig sind.

:::herleitung
**Ausgangspunkt:** die Eintragsmuster aus dem Abschnitt *Die Matrix Bauteil für Bauteil*, eingetragen für alle Knoten einschließlich des Bezugsknotens.

**Annahmen:** (i) Die Schaltung hängt zusammen. (ii) Sie enthält nur Bauelemente mit diesen Mustern.

**Schritt 1**: Zeilensummen eines Musters. In Zeile a stehen bei der Admittanz +Y und −Y, bei der gesteuerten Quelle +g und −g; ebenso in Zeile b mit umgekehrtem Vorzeichen. Jede Zeile eines Musters summiert sich zu null:

$$(+\underline Y) + (-\underline Y) = 0, \qquad (+g) + (-g) = 0$$

**Schritt 2**: Spaltensummen eines Musters. In jeder Spalte steht derselbe Betrag einmal in Zeile a mit plus und einmal in Zeile b mit minus; auch die rechte Seite einer Stromquelle summiert sich zu null.

$$\sum_{\mu} \underline Y_{\mu\nu} = 0, \qquad \sum_{\nu} \underline Y_{\mu\nu} = 0, \qquad \sum_{\mu} \underline I_{q\mu} = 0$$

**Schritt 3** (entscheidender Schritt): Weil die vollständige Matrix die Summe der Muster ist, gelten beide Summen auch für sie. Die Zeilensummen null bedeuten, dass gleiches Anheben aller Potentiale um eine beliebige Spannung $\Delta\underline U$ keine Gleichung ändert:

$$\sum_{\nu} \underline Y_{\mu\nu}\,(\underline U_\nu + \Delta\underline U) = \sum_{\nu} \underline Y_{\mu\nu}\,\underline U_\nu$$

**Schritt 4**: Die Spaltensummen null bedeuten, dass die Summe aller Zeilen die Nullzeile ist; die Zeile des Bezugsknotens ist das Negative der Summe der übrigen und liefert keine neue Information.

**Schritt 5**: Setzt man das Potential des Bezugsknotens null, multiplizieren alle Einträge seiner Spalte null; Zeile und Spalte entfallen.

**Ergebnis:** In der vollständigen Matrix sind alle Zeilen- und Spaltensummen null; nach Streichen der Zeile und Spalte des Bezugsknotens bleibt die Leitwertmatrix mit $n_K$ Zeilen und Spalten.

**Woher die Faktoren kommen:** Die Zeilensumme null stammt aus den Potentialdifferenzen in den Zweiggleichungen, die Spaltensumme null aus dem Paar Abfluss und Zufluss jedes Stroms.

**Proben:** Verstärkerstufe: Zeile 0 der vollständigen Matrix, (1,3; −0,1; −0,2; −1), ist das Negative der Summe der Zeilen G, D und S. Eine einzelne Admittanz zwischen a und Masse: vollständig (Y; −Y / −Y; Y), gestrichen bleibt Y.

**Grenzen:** Hängt die Schaltung nicht zusammen, braucht jedes Teilnetz seinen eigenen Bezugsknoten. Für die Zusatzzeilen der modifizierten Knotenanalyse gelten die Summen nicht, weil dort Zweiggleichungen stehen.
:::

::::beispiel Leitwertmatrix der Verstärkerstufe aus den Mustern
**Gegeben:** Kleinsignal-Ersatzschaltbild der Verstärkerstufe: Signalquelle 10 mV mit 10 kΩ, als Stromquelle 1 µA in G parallel zu $G_\mathrm{sig}$ = 0,1 mS; $G_D$ = $G_L$ = 0,1 mS von D nach Masse; $G_S$ = 1 mS von S nach Masse; $g_o$ = 0,025 mS zwischen D und S; gesteuerte Quelle $g_m$ = 1 mS, Strom von D nach S, gesteuert von der Spannung zwischen G und S.

**Gesucht:** die vollständige Matrix, die Leitwertmatrix und die Knotenpotentiale.

**Rechnung:** In mS, mV und µA, Reihenfolge 0, G, D, S. Die Leitwerte tragen ihre Muster ein: 0,1 an den Plätzen aus 0 und G, 0,2 aus 0 und D, 1 aus 0 und S, 0,025 aus D und S. Die gesteuerte Quelle trägt +1 auf (D, G) und (S, S) und −1 auf (D, S) und (S, G) ein. Vollständige Matrix:

$$\begin{pmatrix} 1{,}3 & -0{,}1 & -0{,}2 & -1 \\ -0{,}1 & 0{,}1 & 0 & 0 \\ -0{,}2 & 1 & 0{,}225 & -1{,}025 \\ -1 & -1 & -0{,}025 & 2{,}025 \end{pmatrix}$$

Jede Zeile und jede Spalte summiert sich zu null, etwa Zeile D:

$$-0{,}2 + 1 + 0{,}225 - 1{,}025 = 0$$

Ohne Zeile und Spalte 0, mit der rechten Seite +1 µA in Zeile G:

$$\begin{pmatrix} 0{,}1 & 0 & 0 \\ 1 & 0{,}225 & -1{,}025 \\ -1 & -0{,}025 & 2{,}025 \end{pmatrix} \begin{pmatrix} \underline U_G \\ \underline U_D \\ \underline U_S \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$

**Ergebnis:** **Die Leitwertmatrix wie beim Aufstellen nach Augenschein; Lösung 10 mV, −23,26 mV und 4,65 mV.**

**Einordnung:** Die Muster liefern die Matrix ohne Nachdenken an den Knoten; die gestrichene Zeile der Masse dient als Probe, denn mit der Lösung ergibt sie den Strom −1 µA, mit dem die Signalquelle die Masse belastet.
::::

## Lösen mit Determinanten: die Cramersche Regel

*Wie berechnet man eine einzelne Knotenspannung, ohne das ganze System umzuformen?*

Zwei Gleichungen mit zwei Unbekannten löst man durch Elimination: Für

$$a_{11}\,x_1 + a_{12}\,x_2 = b_1$$

$$a_{21}\,x_1 + a_{22}\,x_2 = b_2$$

multipliziert man die erste mit $a_{21}$, die zweite mit $a_{11}$, zieht ab, und $x_1$ fällt heraus:

$$x_2 = \frac{a_{11}\,b_2 - a_{21}\,b_1}{a_{11}\,a_{22} - a_{12}\,a_{21}}$$

Im RC-Tiefpass, dessen Quelle samt $R_1$ in eine Stromquelle von 1 mA parallel zu 1 mS umgewandelt ist, sind die Einträge in mS 2 + j, −1, −1 und 1 + j, rechts stehen 1 mA und 0. Unbekannte sind die Potentiale $\underline U_2$ und $\underline U_3$ der Knoten 2 und 3 aus Abbildung 1, und für die Ausgangsspannung $\underline U_3$ ergibt sich:

$$\underline U_3 = \frac{(2 + j)\cdot 0 - (-1)\cdot 1}{(2 + j)(1 + j) - (-1)(-1)}\ \mathrm V = \frac{1}{3j}\ \mathrm V = -\frac{j}{3}\ \mathrm V$$

Der Nenner hängt nur von der Matrix ab; der Zähler ist derselbe Ausdruck für die Matrix, in der die Spalte von $x_2$ durch die rechte Seite ersetzt ist. Ein solcher Ausdruck heißt __Determinante__; für mehr Unbekannte führt man sie schrittweise auf kleinere zurück (Abbildung 3).

:::grafik
Szene: st1/netzwerkanalyse/03-cramer-laplace · Vorlage: matrix-schema
**Abbildung 3:** (a) Leitwertmatrix der Verstärkerstufe in mS, Zeilen (0,1; 0; 0), (1; 0,225; −1,025), (−1; −0,025; 2,025), daneben dieselbe Matrix mit Spalte D durch die rechte Seite (1; 0; 0) µA ersetzt. (b) Entwicklung nach der ersetzten Spalte: Das Schachbrett der Vorzeichen liegt über der Matrix, der einzige Eintrag ungleich null, 1 µA oben, trägt minus, seine Unterdeterminante (1; −1,025 / −1; 2,025) ist 1, das Ergebnis −1. (c) Sarrus-Schema für die Determinante: drei absteigende Diagonalen mit plus, drei aufsteigende mit minus, zusammen 0,043 mS³. Darunter die Drainspannung, −1 durch 0,043 in mV, also −23,26 mV. Jede Unbekannte ist ein Quotient zweier Determinanten mit demselben Nenner; man entwickelt nach der Zeile oder Spalte mit den meisten Nullen.
:::

**Die Akteure:**

- __$\mathbf A$__: quadratische Matrix mit $n$ Zeilen und Spalten und den Einträgen __$a_{\mu\nu}$__, reell oder komplex; hier die Leitwertmatrix oder später die Matrix der modifizierten Knotenanalyse.
- __$\vec x$__: Spalte der Unbekannten $x_1, \ldots, x_n$; __$\vec b$__: rechte Seite.
- __$\det\mathbf A$__: Determinante, eine reelle oder komplexe Zahl; bei der Verstärkerstufe 0,043 mS³.
- __$\mathbf A^{(\mu\nu)}$__: __Streichungsmatrix__ ohne Zeile μ und Spalte ν; ihre Determinante heißt __Unterdeterminante__.
- __$\mathbf A_\nu$__: $\mathbf A$ mit Spalte ν durch $\vec b$ ersetzt.

:::formel Definition
$$\det\mathbf A = \sum_{\nu=1}^{n} (-1)^{1+\nu}\,a_{1\nu}\,\det\mathbf A^{(1\nu)}$$
:::

Für eine Zeile ist die Determinante der Eintrag selbst. Man definiert sie so, weil genau dieser Ausdruck bei der Elimination im Nenner entsteht und sich jede Determinante damit auf kleinere zurückführen lässt. Für zwei und drei Zeilen folgen daraus die Formeln, die zweite ist die __Regel von Sarrus__:

$$\det\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = a_{11}\,a_{22} - a_{12}\,a_{21}$$

$$\begin{aligned} \det\mathbf A = {} & a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} \\ & - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} \end{aligned}$$

Statt nach der ersten Zeile darf man nach jeder Zeile und jeder Spalte entwickeln:

:::formel Satz
$$\det\mathbf A = \sum_{\nu=1}^{n} (-1)^{\mu+\nu}\,a_{\mu\nu}\,\det\mathbf A^{(\mu\nu)} \qquad \text{für jede Zeile } \mu$$

$$\det\mathbf A = \sum_{\mu=1}^{n} (-1)^{\mu+\nu}\,a_{\mu\nu}\,\det\mathbf A^{(\mu\nu)} \qquad \text{für jede Spalte } \nu$$
:::

**So liest man das:** Jeder Eintrag der gewählten Zeile oder Spalte wird mit seiner Unterdeterminante multipliziert und bekommt das Vorzeichen eines Schachbretts, plus oben links und abwechselnd nach rechts und unten. Jede Null spart eine ganze Unterdeterminante; man nimmt deshalb die Zeile oder Spalte mit den meisten Nullen, in Schaltungsmatrizen oft die Zeile einer Quelle oder die durch die rechte Seite ersetzte Spalte. Eine Determinante mit vier Zeilen zerfällt in vier mit drei Zeilen.

**Kurz gesagt:** Die Entwicklung nach jeder Zeile und jeder Spalte ergibt dieselbe Determinante.

Idee der Herleitung: Man wendet die Definition auf zwei und drei Zeilen an und zeigt für den allgemeinen Fall, dass jede Entwicklung dieselben Produkte nur anders zusammenfasst.

:::herleitung
**Ausgangspunkt:** die Definition der Determinante durch Entwicklung nach der ersten Zeile.

**Annahmen:** (i) $\mathbf A$ ist quadratisch mit reellen oder komplexen Einträgen. (ii) Die Determinante einer Matrix mit einer Zeile ist ihr Eintrag.

**Schritt 1**: Zwei Zeilen. Die Streichungsmatrizen sind die Einträge $a_{22}$ und $a_{21}$:

$$\det\mathbf A = (+1)\,a_{11}\,a_{22} + (-1)\,a_{12}\,a_{21}$$

**Schritt 2**: Drei Zeilen. Die drei Streichungsmatrizen der ersten Zeile haben zwei Zeilen und werden nach Schritt 1 ausgerechnet:

$$\begin{aligned} \det\mathbf A = {} & a_{11}(a_{22}a_{33} - a_{23}a_{32}) \\ & - a_{12}(a_{21}a_{33} - a_{23}a_{31}) \\ & + a_{13}(a_{21}a_{32} - a_{22}a_{31}) \end{aligned}$$

**Schritt 3**: Ausmultipliziert ergeben sich die sechs Produkte der Regel von Sarrus, drei mit plus und drei mit minus:

$$\begin{aligned} \det\mathbf A = {} & a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} \\ & - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} \end{aligned}$$

**Schritt 4** (entscheidender Schritt): Jedes der sechs Produkte enthält aus jeder Zeile und aus jeder Spalte genau einen Eintrag. Fasst man sie nach den Einträgen der zweiten Zeile zusammen, entsteht die Entwicklung nach der zweiten Zeile, nach den Einträgen der ersten Spalte die nach der ersten Spalte, jeweils mit dem Schachbrettvorzeichen:

$$\begin{aligned} \det\mathbf A = {} & -a_{21}(a_{12}a_{33} - a_{13}a_{32}) \\ & + a_{22}(a_{11}a_{33} - a_{13}a_{31}) \\ & - a_{23}(a_{11}a_{32} - a_{12}a_{31}) \end{aligned}$$

**Schritt 5**: Allgemein liefert die wiederholte Entwicklung nach der Definition $n!$ Produkte, jedes mit genau einem Eintrag aus jeder Zeile und jeder Spalte und einem Vorzeichen, das nur von ihrer Anordnung abhängt (Leibniz-Formel). Diese Form behandelt Zeilen und Spalten gleich und zeichnet keine Zeile aus; jede Entwicklung gruppiert nur dieselben Produkte nach den Einträgen einer anderen Zeile oder Spalte. Den vollständigen Beweis mit der Buchführung der Vorzeichen führt die lineare Algebra.

**Ergebnis:**

$$\det\mathbf A = \sum_{\nu=1}^{n} (-1)^{\mu+\nu}\,a_{\mu\nu}\,\det\mathbf A^{(\mu\nu)} \qquad \text{für jede Zeile } \mu$$

$$\det\mathbf A = \sum_{\mu=1}^{n} (-1)^{\mu+\nu}\,a_{\mu\nu}\,\det\mathbf A^{(\mu\nu)} \qquad \text{für jede Spalte } \nu$$

**Woher die Faktoren kommen:** Das Vorzeichen $(-1)^{\mu+\nu}$ ist das Schachbrettmuster; es sorgt dafür, dass jedes der Produkte bei jeder Entwicklung mit demselben Vorzeichen erscheint.

**Proben:** Leitwertmatrix der Verstärkerstufe in mS: Entwicklung nach Zeile G ergibt 0,1 · 0,43, nach Zeile D 0,04556 − 0,00256, nach Spalte S ebenfalls 0,04556 − 0,00256, nach Sarrus 0,0455625 − 0,0025625; jedes Mal 0,043 mS³. Einheit: jedes Produkt enthält einen Eintrag je Zeile, bei drei Zeilen also S³.

**Grenzen:** Die Entwicklung ist für jede Größe richtig, aber teuer: Eine Determinante mit $n$ Zeilen hat $n!$ Produkte; große Systeme löst man deshalb durch Elimination.
:::

**Das Zusammenspiel:** So rechnet man eine einzelne Unbekannte aus:

**Schritt 1**: Die Determinante der Matrix berechnen, nach der Zeile oder Spalte mit den meisten Nullen.

**Schritt 2**: Die Spalte der gesuchten Unbekannten durch die rechte Seite ersetzen.

**Schritt 3**: Die Determinante dieser Matrix berechnen, am besten nach der ersetzten Spalte.

**Schritt 4**: Die zweite Determinante durch die erste teilen.

Dass das stimmt, sagt ein Satz, der das Muster vom Anfang des Abschnitts für jede Zahl von Unbekannten ausspricht:

:::formel Satz
$$x_\nu = \frac{\det\mathbf A_\nu}{\det\mathbf A}, \qquad \nu = 1, \ldots, n$$
:::

**So liest man das:** Zähler und Nenner unterscheiden sich nur in Spalte ν, im Zähler steht dort die rechte Seite (Abbildung 3a). Wer eine einzige Knotenspannung braucht, rechnet zwei Determinanten. Die Regel heißt __Cramersche Regel__ und gilt, solange $\det\mathbf A$ nicht null ist; genau dann hat das System genau eine Lösung.

**Kurz gesagt:** Ist die Determinante der Matrix nicht null, ist jede Unbekannte der Quotient zweier Determinanten, und der Nenner ist für alle Unbekannten derselbe.

Idee der Herleitung: Man schreibt die rechte Seite als Summe der Spalten von $\mathbf A$, gewichtet mit den Unbekannten, setzt sie in Spalte ν ein und nutzt, dass eine Determinante in jeder Spalte linear ist und mit zwei gleichen Spalten verschwindet.

:::herleitung
**Ausgangspunkt:** die Definition der Determinante und der Entwicklungssatz (oben).

**Annahmen:** (i) $\mathbf A$ ist quadratisch und $\det\mathbf A$ nicht null. (ii) $\vec x$ löst das System mit der rechten Seite $\vec b$.

**Schritt 1**: Mit $\vec a_\kappa$ für die Spalte κ von $\mathbf A$ besagt das System, dass die rechte Seite die Summe der Spalten ist, jede mit ihrer Unbekannten multipliziert:

$$\vec b = \sum_{\kappa=1}^{n} x_\kappa\,\vec a_\kappa$$

**Schritt 2**: Eine Determinante ist in jeder Spalte linear. Entwickelt man nach Spalte ν, enthält jeder Summand genau einen Eintrag dieser Spalte als Faktor, und die Unterdeterminanten hängen von ihr nicht ab; für Zahlen $\lambda_1$, $\lambda_2$ und Spalten $\vec u$, $\vec w$ an der Stelle ν gilt deshalb:

$$\begin{aligned} & \det(\ldots, \lambda_1\vec u + \lambda_2\vec w, \ldots) \\ & \quad = \lambda_1\det(\ldots, \vec u, \ldots) + \lambda_2\det(\ldots, \vec w, \ldots) \end{aligned}$$

**Schritt 3**: Eine Determinante mit zwei gleichen Spalten ist null. Bei zwei Zeilen haben beide Spalten die Einträge $y_1$ und $y_2$, und die Determinante ist $y_1y_2 - y_1y_2$, also null. Bei mehr Zeilen entwickelt man nach einer dritten Spalte; jede Streichungsmatrix enthält dann noch beide gleichen Spalten, und ihre Determinante ist nach demselben Argument mit einer Zeile weniger null.

**Schritt 4** (entscheidender Schritt): In $\mathbf A_\nu$ steht an der Stelle ν die rechte Seite. Nach Schritt 1 und 2 zerfällt die Determinante in $n$ Summanden, in denen an der Stelle ν die Spalte $\vec a_\kappa$ steht. Für κ ungleich ν kommt $\vec a_\kappa$ dann zweimal vor, der Summand verschwindet nach Schritt 3; übrig bleibt κ gleich ν:

$$\det\mathbf A_\nu = \sum_{\kappa=1}^{n} x_\kappa\,\det(\ldots, \vec a_\kappa, \ldots) = x_\nu\,\det\mathbf A$$

**Ergebnis:**

$$x_\nu = \frac{\det\mathbf A_\nu}{\det\mathbf A}, \qquad \nu = 1, \ldots, n$$

**Woher die Faktoren kommen:** Der Zähler enthält die rechte Seite, weil nur der Summand mit der eigenen Spalte überlebt; der Nenner ist die unveränderte Matrix und deshalb für alle Unbekannten gleich.

**Proben:** Zwei Zeilen: Die Regel gibt für $x_2$ genau den Bruch, den die Elimination am Anfang des Abschnitts geliefert hat. Tiefpass: 1/(3j) V, also −j/3 V wie mit Knoten- und Maschenanalyse. Einheit bei der Leitwertmatrix: Zähler S^(n−1) · A, Nenner Sⁿ, Quotient V.

**Grenzen:** Ist $\det\mathbf A$ null, versagt die Division; das System hat dann keine oder unendlich viele Lösungen. Für viele Unbekannte ist der Weg zu teuer; dort rechnet man mit Elimination.
:::

::::beispiel Knotenspannungen der Verstärkerstufe mit der Cramerschen Regel
**Gegeben:** die Leitwertmatrix der Verstärkerstufe in mS, Zeilen und Spalten G, D, S: (0,1; 0; 0), (1; 0,225; −1,025), (−1; −0,025; 2,025); rechte Seite (1; 0; 0) µA.

**Gesucht:** die Determinante und die Spannungen an Drain und Source.

**Rechnung:** Determinante nach Zeile G, die nur einen Eintrag hat:

$$\det\mathbf Y = 0{,}1\cdot\det\begin{pmatrix} 0{,}225 & -1{,}025 \\ -0{,}025 & 2{,}025 \end{pmatrix} = 0{,}1\cdot 0{,}43 = 0{,}043\ \mathrm{mS^3}$$

Die rechte Seite in Spalte D hat nur oben eine 1, Schachbrettvorzeichen minus; in Spalte S oben eine 1 mit plus:

$$\det\mathbf Y_D = -1\cdot\det\begin{pmatrix} 1 & -1{,}025 \\ -1 & 2{,}025 \end{pmatrix} = -1\ \mathrm{mS^2\,\mu A}$$

$$\det\mathbf Y_S = +1\cdot\det\begin{pmatrix} 1 & 0{,}225 \\ -1 & -0{,}025 \end{pmatrix} = 0{,}2\ \mathrm{mS^2\,\mu A}$$

Quotienten, µA/mS gleich mV:

$$\underline U_D = \frac{-1}{0{,}043}\ \mathrm{mV} = -23{,}26\ \mathrm{mV}, \qquad \underline U_S = \frac{0{,}2}{0{,}043}\ \mathrm{mV} = 4{,}65\ \mathrm{mV}$$

**Ergebnis:** **Determinante 0,043 mS³; Drain −23,26 mV, Source 4,65 mV.**

**Einordnung:** Jeder Zähler kostete nur eine Unterdeterminante mit zwei Zeilen, weil die rechte Seite einen einzigen Eintrag hat. Nach Sarrus ergibt sich dieselbe Determinante; nur zwei der sechs Produkte, 0,0455625 und −0,0025625 mS³, sind ungleich null.
::::

Der gemeinsame Nenner bestimmt auch, wie eine Schaltung auf die Frequenz reagiert. Mit Kondensatoren ist die Determinante ein Polynom in $j\omega$; zerfällt sie in Faktoren der Form $1 + j\omega/\omega_p$, knicken alle Knotenspannungen, in deren Zähler sich der Faktor nicht kürzt, bei der __Eckkreisfrequenz__ $\omega_p$ ab. Ersetzt man $j\omega$ durch eine beliebige komplexe Zahl $s$, wird ein solcher Faktor bei $s$ gleich $-\omega_p$ null; an dieser Nullstelle der Determinante wächst jede dieser Knotenspannungen über alle Grenzen, und die Stelle heißt ihr __Pol__. In der Verstärkerstufe ohne Source-Widerstand mit 100 fF am Gate und 10 pF Last am Drain liegen die Eckfrequenzen bei 3,58 MHz und 159 MHz.

:::frage
„Warum rechnen Schaltungssimulatoren dann nicht mit der Cramerschen Regel?“
Weil Determinanten durch Entwicklung zu teuer werden: Eine Determinante mit $n$ Zeilen hat $n!$ Produkte. Bei zwanzig Unbekannten braucht die Cramersche Regel rund 8,8·10¹⁹ Multiplikationen und Divisionen, bei 10⁹ je Sekunde 2800 Jahre; die Gauß-Elimination, die Vielfache von Zeilen abzieht, bis eine Dreiecksform entsteht, schafft es mit 3060. Simulatoren eliminieren deshalb und nutzen dabei, dass fast alle Einträge einer Schaltungsmatrix null sind. Die Cramersche Regel bleibt das Werkzeug für Formeln und kleine Systeme.
:::

## Die modifizierte Knotenanalyse

*Warum lässt sich eine ideale Spannungsquelle nicht in die Leitwertmatrix eintragen, und wie nimmt man sie trotzdem auf?*

Im RC-Tiefpass liegt eine Quelle von 1 V zwischen Knoten 1 und Masse. Ihren Strom, 0,745 mA bei +26,6°, bestimmen $R_1$, $C_1$, $R_2$ und $C_2$; die Quelle selbst legt nur die Spannung fest und lässt bei ihr jeden Strom zu. Ein Eintragsmuster der Knotenanalyse verlangt aber einen Strom, der ein festes Vielfaches von Potentialen ist, und eine Umwandlung in eine Stromquelle ergäbe ohne Innenwiderstand einen unendlichen Strom. Dasselbe gilt für alles mit unendlicher Admittanz, Strommesser, Drahtbrücken und Spulen bei Gleichstrom, und für gesteuerte Spannungsquellen und ideale Operationsverstärker, die eine Spannung festlegen (Abbildung 4).

:::grafik
Szene: st1/netzwerkanalyse/03-mna-spannungsquelle · Vorlage: schaltbild-matrix
**Abbildung 4:** Links die Kennlinien eines Leitwerts von 1 mS, eine Gerade durch den Ursprung, und einer idealen Spannungsquelle von 1 V, eine Linie bei 1 V, die jeden Strom zulässt. Mitte eine ideale Spannungsquelle zwischen den Knoten a (Pluspol) und b an einem übrigen Netz, Strompfeil von a in die Quelle hinein. Rechts die Leitwertmatrix als grauer Block, ergänzt um eine Spalte für den Quellenstrom mit +1 in Zeile a und −1 in Zeile b und um eine Zeile mit +1 in Spalte a, −1 in Spalte b und der Quellenspannung rechts. Der Strom der Quelle wird zur Unbekannten und bekommt eine Spalte, ihre Zweiggleichung wird zur neuen Zeile.
:::

**Die Akteure:**

- __$\underline I_z$__: __Zusatzstrom__, ein Strom, der als zusätzliche Unbekannte geführt wird, weil er sich aus den übrigen Unbekannten nicht ergibt; gezählt von a durch das Element nach b, bei einer Spannungsquelle also in ihren Pluspol hinein; in A.
- __$\underline U_q$__: Quellenspannung, Pluspol an a; 1 V im Tiefpass.
- __$m$__: Zahl der Zusatzströme; __$\mathbf M$__: Matrix der __modifizierten Knotenanalyse__ mit $n_K + m$ Zeilen und Spalten, die Leitwertmatrix ergänzt um eine Spalte je Zusatzstrom und eine Zeile je Zweiggleichung.

**Das Zusammenspiel:**

**Schritt 1**: Der Strom des Elements wird als Unbekannte $\underline I_z$ hinter die Knotenpotentiale gesetzt.

**Schritt 2**: In den Knotengleichungen fließt $\underline I_z$ bei a ab und bei b zu; seine Spalte bekommt +1 in Zeile a und −1 in Zeile b.

**Schritt 3**: Die zusätzliche Gleichung ist die Zweiggleichung des Elements, bei der idealen Quelle:

$$\underline U_a - \underline U_b = \underline U_q$$

**Schritt 4**: Unbekannte und Gleichungen wachsen gleich; das System bleibt quadratisch und liefert den Strom der Quelle mit.

:::formel Formel
$$\begin{array}{c|ccc|c} & a & b & \underline I_z & \text{rechts} \\ \hline a & & & +1 & \\ b & & & -1 & \\ \text{Zweig} & +1 & -1 & 0 & \underline U_q \end{array}$$
:::

**So liest man das:** Die Spalte bucht den Strom der Quelle in die Knotengleichungen ihrer Anschlüsse, die Zeile ist ihre Zweiggleichung mit der Quellenspannung rechts; in der Ecke steht null, weil die Spannung einer idealen Quelle nicht von ihrem Strom abhängt. Liegt b am Bezugsknoten, entfallen dort Zeile und Spalte. Bei unabhängigen Spannungsquellen ist die Zusatzzeile das Spiegelbild der Zusatzspalte; eine symmetrische Leitwertmatrix bleibt deshalb symmetrisch.

**Kurz gesagt:** Für jeden Zusatzstrom kommt genau eine Zeile hinzu, die Zweiggleichung seines Elements; das System bleibt deshalb quadratisch.

:::fehlvorstellung
„Der Zusatzstrom ist der Strom, den die Quelle abgibt.“ Das liegt nahe, weil man bei Quellen an den abgegebenen Strom denkt. Gezählt wird aber wie bei Admittanzen und gesteuerten Quellen von a durch das Element nach b, also in den Pluspol hinein. Im RC-Tiefpass ist der Zusatzstrom −(0,667 + 0,333j) mA; abgegeben werden 0,745 mA bei +26,6°. Schaltungssimulatoren zeigen deshalb für eine Versorgung, die Strom liefert, einen negativen Strom an.
:::

Idee der Herleitung: Man ergänzt die Unbekannten um den Strom der Quelle, bucht ihn in die Knotengleichungen ihrer Anschlüsse und nimmt ihre Zweiggleichung als zusätzliche Zeile.

:::herleitung
**Ausgangspunkt:** die Knotenregel und die Zweiggleichung der idealen Spannungsquelle, deren Pluspol an a liegt.

**Annahmen:** (i) Die übrigen Bauelemente sind mit ihren Mustern eingetragen. (ii) Der Strom $\underline I_z$ wird von a durch die Quelle nach b gezählt.

**Schritt 1**: Die Unbekannten werden um den Strom der Quelle ergänzt:

$$(\underline U_1, \ldots, \underline U_{n_K}, \underline I_z)$$

**Schritt 2**: Knotengleichung von a: Zu den übrigen abfließenden Strömen kommt $\underline I_z$ hinzu, in der von b kommt er als zufließender Strom mit minus hinzu:

$$\sum_{\nu} \underline Y_{a\nu}\,\underline U_\nu + \underline I_z = \underline I_{qa}$$

$$\sum_{\nu} \underline Y_{b\nu}\,\underline U_\nu - \underline I_z = \underline I_{qb}$$

**Schritt 3** (entscheidender Schritt): Die Quelle legt keinen Strom fest, wohl aber eine Spannung; diese Zweiggleichung ist die fehlende Gleichung. Sie enthält die Potentiale von a und b und nicht den Strom:

$$1\cdot\underline U_a - 1\cdot\underline U_b + 0\cdot\underline I_z = \underline U_q$$

**Schritt 4**: Damit stehen $n_K + 1$ Gleichungen für $n_K + 1$ Unbekannte; jede weitere Quelle fügt eine Spalte und eine Zeile hinzu.

**Ergebnis:** das Muster oben: +1 und −1 in der Spalte des Zusatzstroms, +1 und −1 in der Zeile der Zweiggleichung, null in der Ecke, $\underline U_q$ rechts.

**Woher die Faktoren kommen:** Die Einsen der Spalte stammen aus der Knotenregel, Abfluss bei a und Zufluss bei b; die der Zeile aus der Potentialdifferenz der Zweiggleichung; die Null in der Ecke aus dem fehlenden Innenwiderstand.

**Proben:** Einheiten: In den Knotengleichungen steht $\underline I_z$ mit dem Faktor 1 neben Strömen, in der Zusatzzeile stehen Spannungen. Tiefpass: Matrix mit vier Zeilen, symmetrisch; Lösung wie mit Knoten- und Maschenanalyse (Beispiel unten).

**Grenzen:** Zwei ideale Spannungsquellen parallel oder ein Umlauf aus idealen Spannungsquellen machen Zeilen voneinander abhängig; die Determinante ist dann null.
:::

::::beispiel RC-Tiefpass mit idealer Spannungsquelle
**Gegeben:** ideale Quelle $\underline U_q$ = 1 V zwischen Knoten 1 und Masse, $R_1$ = $R_2$ = 1 kΩ, $C_1$ = $C_2$ = 100 nF, ω = 10⁴ 1/s, also $j\omega C$ = j·1 mS (Abbildung 1).

**Gesucht:** Ausgangsspannung $\underline U_3$ und Strom der Quelle.

**Rechnung:** In mS, kΩ, V und mA, Unbekannte $\underline U_1$, $\underline U_2$, $\underline U_3$, $\underline I_z$:

$$\begin{pmatrix} 1 & -1 & 0 & 1 \\ -1 & 2 + j & -1 & 0 \\ 0 & -1 & 1 + j & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} \underline U_1 \\ \underline U_2 \\ \underline U_3 \\ \underline I_z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}$$

Entwickelt nach der Quellenzeile, die nur eine 1 hat, und danach nach der letzten Spalte:

$$\det\mathbf M = (-1)^{4+1}\cdot\big[(2 + j)(1 + j) - 1\big] = -3j$$

Für $\underline U_3$ und $\underline I_z$ ersetzt die rechte Seite Spalte 3 bzw. 4; entwickelt nach dieser Spalte, deren einzige 1 unten steht:

$$\det\mathbf M_3 = -1, \qquad \underline U_3 = \frac{-1}{-3j}\ \mathrm V = -\frac{j}{3}\ \mathrm V$$

$$\det\mathbf M_4 = \det\begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 + j & -1 \\ 0 & -1 & 1 + j \end{pmatrix} = -1 + 2j, \qquad \underline I_z = \frac{-1 + 2j}{-3j}\ \mathrm{mA} = -\frac{2 + j}{3}\ \mathrm{mA}$$

**Ergebnis:** **$\underline U_3$ = −j/3 V; der Zusatzstrom ist −(0,667 + 0,333j) mA, die Quelle gibt 0,745 mA bei +26,6° ab.**

**Einordnung:** Dieselben Zahlen liefern Maschen- und Knotenanalyse, hier aber ohne Umwandlung der Quelle und mit dem Quellenstrom als Teil der Lösung. Die Matrix ist symmetrisch, wie in jedem Netz aus Widerständen, Kondensatoren, Spulen und unabhängigen Quellen; gesteuerte Quellen machen sie im Allgemeinen unsymmetrisch.

**Variation:** Als Tor aus Quelle und $R_1$ eingetragen (Abschnitt *Impedanzen und reale Quellen*) entfällt Knoten 1; das System hat drei Zeilen, (1 + j; −1; 1), (−1; 1 + j; 0) und (1; 0; −1) mit 1 V rechts in der letzten, die Determinante ist wieder −3j und die Lösung dieselbe.
::::

:::frage
„Geht es bei einer idealen Spannungsquelle nicht auch ohne zusätzliche Unbekannte?“
Von Hand oft ja. Liegt die Quelle an Masse wie im Tiefpass, ist das Potential ihres Pluspols bekannt, und zwei Gleichungen genügen statt vier. Liegt sie zwischen zwei anderen Knoten, fasst man beide zu einem __Superknoten__ mit einer gemeinsamen Knotengleichung zusammen, in der sich der Quellenstrom heraushebt, und nimmt ihre Zweiggleichung dazu ([Das Knotenpotentialverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/knotenpotentialverfahren/knotenpotentialverfahren.html)). Das spart eine Unbekannte, verlangt aber einen Blick auf die Schaltung und liefert den Quellenstrom nicht; die Muster arbeiten ohne Blick, und der Strom, im Tiefpass 0,745 mA, fällt mit an.
:::

## Eintragsmuster weiterer Bauelemente

*Welche Muster haben Impedanzen, reale Spannungsquellen, gesteuerte Quellen und der ideale Operationsverstärker?*

Alle Elemente, deren Strom sich weder aus den Knotenpotentialen noch aus einem schon geführten Strom ergibt, bekommen dasselbe Gerüst wie die Spannungsquelle: eine Spalte für ihren Strom mit +1 und −1 in den Zeilen ihrer Anschlüsse und eine Zeile für ihre Zweiggleichung. Verschieden ist nur, was in dieser Zeile steht (Abbildung 5); die stromgesteuerte Stromquelle braucht das Gerüst nicht, weil ihr Strom ein Vielfaches eines geführten Stroms ist.

:::grafik
Szene: st1/netzwerkanalyse/03-eintragsmuster-mna · Vorlage: musterkarten
**Abbildung 5:** Eintragsmuster der modifizierten Knotenanalyse. Impedanz Z: Zusatzspalte +1/−1, Zusatzzeile +1/−1 und −Z in der Ecke, rechts null; der Sonderfall Z gleich null ist ein Kurzschluss oder Strommesser. Tor aus Quelle und Innenimpedanz: wie die Impedanz, rechts die Quellenspannung. Spannungsgesteuerte Spannungsquelle mit dem Faktor v: Zusatzzeile +1, −1 in den Spalten a, b und −v, +v in den Spalten c, d. Stromgesteuerte Stromquelle: ±β in der Spalte des Steuerstroms, keine eigene Zeile. Stromgesteuerte Spannungsquelle: Zusatzzeile mit $-r_m$ in der Spalte des Steuerstroms. Nullor: Zusatzspalte am Ausgang, Zusatzzeile mit +1 und −1 in den Spalten der Eingänge. Alle Elemente, deren Strom sich weder aus den Knotenpotentialen noch aus einem schon geführten Strom ergibt, haben dasselbe Gerüst: eine Spalte für ihren Strom und eine Zeile für ihre Zweiggleichung.
:::

### Impedanzen und reale Quellen

*Wie trägt man ein Element ein, dessen Impedanz null werden kann?*

Eine Impedanz zwischen a und b, deren Strom man als Unbekannte führt, verlangt: Potential von a minus Potential von b gleich Impedanz mal Strom. Eine reale Spannungsquelle, eine ideale Spannungsquelle in Reihe mit einer Impedanz, verbindet das mit der Quellenspannung; eine solche Anschlussstelle, über die man eine Schaltung anregt oder misst, heißt __Tor__.

**Die Akteure:**

- __$\underline Z$__: Impedanz des Zweigs, $R$, $j\omega L$ oder $1/(j\omega C)$, beim Tor die Innenimpedanz; in Ω; null ist erlaubt.
- __$\underline U_q$__: Quellenspannung des Tors, Pluspol zur Seite von a; null bei einer reinen Impedanz.

:::formel Formel
$$\underline U_a - \underline U_b - \underline Z\,\underline I_z = \underline U_q$$
:::

**So liest man das:** Die Zusatzzeile hat +1 und −1 in den Spalten von a und b, $-\underline Z$ in der Spalte des eigenen Stroms und rechts $\underline U_q$. Mit $\underline Z$ gleich null ist das die ideale Quelle, mit $\underline U_q$ gleich null eine Impedanz, mit beidem null ein Kurzschluss, dessen Strom man mitbekommt. Weil die Impedanz statt ihres Kehrwerts eingetragen wird, bleiben null Ohm und eine Spule bei Gleichstrom endliche Einträge. Die Signalquelle der Verstärkerstufe lässt sich so samt 10 kΩ als Tor eintragen: Der Drain liegt wieder bei −23,26 mV, und der Strom der Quelle ist null, weil das Gate keinen Strom aufnimmt.

Idee der Herleitung: Man setzt die Spannung des Zweigs aus Quellenspannung und Spannung an der Impedanz zusammen und bringt den Strom auf die linke Seite.

:::herleitung
**Ausgangspunkt:** die Maschenregel entlang des Zweigs und die Zweiggleichung der Impedanz mit gleich gerichteten Zählpfeilen für Strom und Spannung.

**Annahmen:** (i) Der Strom $\underline I_z$ fließt von a durch die Impedanz und die Quelle nach b. (ii) Der Pluspol der Quelle liegt auf der Seite von a.

**Schritt 1**: Die Spannung zwischen a und b ist die Summe der Spannungen an Impedanz und Quelle:

$$\underline U_a - \underline U_b = \underline U_Z + \underline U_q$$

**Schritt 2**: Die Impedanz verknüpft ihre Spannung mit dem Strom, der sie in Richtung des Spannungspfeils durchfließt:

$$\underline U_Z = \underline Z\,\underline I_z$$

**Schritt 3** (entscheidender Schritt): Eingesetzt und den Strom nach links gebracht; die Unbekannten stehen links, der feste Wert rechts:

$$\underline U_a - \underline U_b - \underline Z\,\underline I_z = \underline U_q$$

**Schritt 4**: Die Spalte des Zusatzstroms entsteht wie bei der idealen Quelle aus der Knotenregel, +1 in Zeile a, −1 in Zeile b.

**Ergebnis:**

$$\underline U_a - \underline U_b - \underline Z\,\underline I_z = \underline U_q$$

**Woher die Faktoren kommen:** −Z stammt aus dem Herüberbringen des Spannungsabfalls auf die linke Seite; die Einsen aus der Potentialdifferenz.

**Proben:** Einheit: Ω mal A ist V. Grenzfälle: $\underline Z$ null gibt die ideale Quelle, $\underline U_q$ null die Impedanz. Tiefpass als Tor: Determinante −3j wie mit idealer Quelle und $R_1$ als eigenem Zweig. Verstärkerstufe: Strom der Signalquelle null, Drain −23,26 mV.

**Grenzen:** Eine unendliche Impedanz, eine offene Leitung, führt keinen Strom; man lässt den Zweig dann weg, statt ihn einzutragen.
:::

:::frage
„Wozu braucht man ein Bauteil mit null Ohm?“
Öfter, als man denkt: Ein __Strommesser__ ist ein Zweig mit null Ohm, dessen Strom man wissen will, und eine Spannungsquelle von 0 V tut dasselbe, ohne eine Spannung der Schaltung zu ändern. Eine Spule hat bei Gleichstrom die Impedanz null; bei jeder Arbeitspunktberechnung ist sie ein Kurzschluss. Die Leitwertmatrix bräuchte dort einen unendlichen Leitwert, schon bei 1 1/s wären es für 100 mH 10 S; im Muster der Impedanz steht in der Ecke nur null, und die Zeile verlangt gleiche Potentiale an beiden Enden.
:::

### Gesteuerte Spannungsquellen und stromgesteuerte Quellen

*Wie werden Quellen eingetragen, die von einer Spannung oder einem Strom an anderer Stelle abhängen?*

Eine __spannungsgesteuerte Spannungsquelle__ legt die Spannung zwischen a und b auf das v-Fache der Spannung zwischen c und d fest, mit der Spannungsverstärkung __$v$__ ohne Einheit; ihr Strom folgt aus der übrigen Schaltung. Sie bekommt einen Zusatzstrom, und ihre Zweiggleichung wird zur Zeile:

:::formel Formel
$$\underline U_a - \underline U_b - v\,(\underline U_c - \underline U_d) = 0$$
:::

**So liest man das:** In der Zusatzzeile stehen +1 und −1 in den Spalten a und b, −v und +v in den Spalten c und d, rechts null. Die Zeile ist nicht das Spiegelbild ihrer Spalte, die Matrix wird unsymmetrisch. Stromgesteuerte Quellen brauchen ihren Steuerstrom als Unbekannte; ist er keine, schaltet man in den steuernden Zweig eine Spannungsquelle von 0 V in Reihe, deren Zusatzstrom er dann ist. Die stromgesteuerte Stromquelle mit dem Faktor β trägt ±β in den Zeilen a und b der Spalte dieses Stroms ein, die stromgesteuerte Spannungsquelle mit der Transimpedanz $r_m$ bekommt eine Zeile mit $-r_m$ in dieser Spalte.

Idee der Herleitung: Man schreibt die Zweiggleichung so, dass alle Unbekannten links stehen, und bucht den Strom der Quelle wie jeden anderen in die Knotengleichungen.

:::herleitung
**Ausgangspunkt:** die Definition der spannungsgesteuerten Spannungsquelle, die Spannung zwischen a und b ist das v-Fache der Spannung zwischen c und d, und die Knotenregel.

**Annahmen:** (i) v ist ein fester Faktor. (ii) Der Strom der Quelle wird von a durch die Quelle nach b gezählt.

**Schritt 1**: Zweiggleichung:

$$\underline U_a - \underline U_b = v\,(\underline U_c - \underline U_d)$$

**Schritt 2** (entscheidender Schritt): Alle Potentiale sind Unbekannte und gehören nach links; rechts bleibt null:

$$\underline U_a - \underline U_b - v\,\underline U_c + v\,\underline U_d = 0$$

**Schritt 3**: Der Strom der Quelle hängt von keiner Gleichung ab, die man schon hat; er wird Zusatzstrom mit +1 in Zeile a und −1 in Zeile b.

**Ergebnis:**

$$\underline U_a - \underline U_b - v\,(\underline U_c - \underline U_d) = 0$$

**Woher die Faktoren kommen:** Die Einsen stammen aus der Ausgangsspannung, −v und +v aus der Steuerspannung, die auf die linke Seite gebracht wird.

**Proben:** Mit v gleich null ist die Quelle ein Kurzschluss zwischen a und b, das Muster der Impedanz null. Invertierender Verstärker mit v gleich 200 000: Verstärkung −9,99945 (Beispiel im Abschnitt *Der ideale Operationsverstärker als Nullor*).

**Grenzen:** Für eine Quelle, deren Ausgang selbst steuert, etwa c gleich a, bleibt das Muster gültig; die Einträge addieren sich dann auf denselben Plätzen.
:::

### Der ideale Operationsverstärker als Nullor

*Wie trägt man einen Verstärker mit unendlicher Verstärkung ein?*

Ein Operationsverstärker ist eine spannungsgesteuerte Spannungsquelle mit sehr großem Faktor, der __Leerlaufverstärkung__ $v_D$, beim Typ 741 typisch 200 000 ([Der ideale OPV und die Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html)). Im invertierenden Verstärker mit 10 kΩ und 100 kΩ und 0,1 V am Eingang liegen damit nur 5 µV zwischen den Eingängen. Für unendliche Verstärkung bleibt von der Zweiggleichung nur die Bedingung, dass diese Spannung null ist, während der Ausgang jeden Strom liefert, den die Schaltung verlangt. Das Modell setzt voraus, dass die Schaltung __gegengekoppelt__ ist: Der Ausgang wirkt, hier über $R_2$, so auf den Minuseingang zurück, dass er eine Abweichung zwischen den Eingängen verkleinert; nur dann stellt sich die Lösung der Gleichungen tatsächlich ein.

Dieses Grenzmodell heißt __Nullor__: ein __Nullator__ zwischen den Eingängen, der Spannung null und Strom null zugleich erzwingt, und ein __Norator__ zwischen Ausgang und Masse, dessen Spannung und Strom sich aus der übrigen Schaltung ergeben (Abbildung 6). Der Nullator liefert eine Gleichung, aber keinen Strom, der Norator einen Strom, aber keine Gleichung.

:::grafik
Szene: st1/netzwerkanalyse/03-nullor-verstaerker · Vorlage: schaltbild-matrix
**Abbildung 6:** (a) Invertierender Verstärker: Quelle 0,1 V mit $R_1$ = 10 kΩ am Minuseingang (Knoten 1), $R_2$ = 100 kΩ zum Ausgang A, Pluseingang an Masse; der Verstärker als Nullor, Nullator zwischen den Eingängen, Norator zwischen Ausgang und Masse. (b) Die Matrix mit den Spalten $U_1$, $U_A$, $I_E$, $I_A$ in mS, kΩ, V und mA: (0,01; −0,01; 1; 0), (−0,01; 0,01; 0; 1), (1; 0; −10; 0) mit 0,1 V rechts, (−1; 0; 0; 0); die Nullator-Zeile orange, die Norator-Spalte grün; darunter Determinante −0,1, Ausgang −1 V. Ein Nullor bringt eine Zeile für die Bedingung an seinem Eingang und eine Spalte für den Strom an seinem Ausgang mit; die Ausgangsspannung ergibt sich aus der übrigen Schaltung.
:::

:::formel Formel
$$\underline U_c - \underline U_d = 0$$
:::

**So liest man das:** Die Zusatzzeile hat +1 in der Spalte des Pluseingangs c und −1 in der des Minuseingangs d; die Zusatzspalte gehört zum Norator, mit +1 in der Zeile des Ausgangs a und −1 in der seines Bezugs b. Zeile und Spalte gehören zu verschiedenen Anschlusspaaren, die Zeile zum Eingang, die Spalte zum Ausgang; die Ausgangsspannung bestimmt die übrige Schaltung.

**Kurz gesagt:** Ein Nullor hält die Spannung an seinem Eingang auf null, ohne dort Strom aufzunehmen, und liefert an seinem Ausgang jeden Strom und jede Spannung, die die Schaltung verlangt.

Idee der Herleitung: Man teilt die Zeile der gesteuerten Spannungsquelle durch ihren Faktor und lässt ihn gegen unendlich gehen.

:::herleitung
**Ausgangspunkt:** die Zeile der spannungsgesteuerten Spannungsquelle (Abschnitt *Gesteuerte Spannungsquellen und stromgesteuerte Quellen*), Ausgang zwischen a und b, Eingang zwischen c und d.

**Annahmen:** (i) Der Ausgang ist so auf den Eingang zurückgeführt, dass die Ausgangsspannung endlich bleibt, während v wächst. (ii) In die Eingänge fließt kein Strom.

**Schritt 1**: Zweiggleichung der gesteuerten Quelle mit dem Faktor v:

$$\underline U_a - \underline U_b - v\,(\underline U_c - \underline U_d) = 0$$

**Schritt 2**: Eine Gleichung darf man durch eine Zahl ungleich null teilen, ohne ihre Lösungen zu ändern; geteilt durch −v:

$$(\underline U_c - \underline U_d) - \frac{1}{v}\,(\underline U_a - \underline U_b) = 0$$

**Schritt 3** (entscheidender Schritt): Für v gegen unendlich verschwindet der zweite Summand, weil die Ausgangsspannung endlich bleibt:

$$\underline U_c - \underline U_d = 0$$

**Schritt 4**: Der Ausgangsstrom bleibt eine Unbekannte mit +1 in Zeile a und −1 in Zeile b; der Eingang nimmt keinen Strom auf und erscheint in keiner Knotengleichung.

**Ergebnis:**

$$\underline U_c - \underline U_d = 0$$

**Woher die Faktoren kommen:** Die Einsen der Zeile stammen aus der Steuerspannung, die übrig bleibt; die Einsen der Spalte aus dem Ausgangsstrom, der wie jeder Strom gebucht wird.

**Proben:** Invertierender Verstärker: Verstärkung −10, also −$R_2/R_1$, wie mit den goldenen Regeln. Mit v gleich 200 000 ergibt die Zeile vor dem Grenzübergang −9,99945, mit einer Million −9,99989.

**Grenzen:** Ob die Rückführung eine Gegenkopplung ist, die die Schaltung stabil hält, zeigen die Gleichungen nicht. Vertauscht man im invertierenden Verstärker die Eingänge, liefert der Nullor wieder −1 V und die gesteuerte Quelle mit 200 000 die endliche Verstärkung −10,00055, obwohl die Schaltung nun mitgekoppelt ist; dort wächst jede kleine Abweichung an, bis die Versorgung den Ausgang begrenzt, und der Verstärker arbeitet als Komparator. Das Modell setzt deshalb eine gegengekoppelte, stabile Schaltung voraus, und das prüft man an der Schaltung selbst.
:::

::::beispiel Invertierender Verstärker mit Nullor
**Gegeben:** Quelle $U_E$ = 0,1 V mit $R_1$ = 10 kΩ als Tor am Minuseingang (Knoten 1), $R_2$ = 100 kΩ zwischen Knoten 1 und dem Ausgang A, Pluseingang an Masse, idealer Operationsverstärker als Nullor (Abbildung 6).

**Gesucht:** Ausgangsspannung, Verstärkung und die Ströme.

**Rechnung:** In mS, kΩ, V und mA, Unbekannte $U_1$, $U_A$, Torstrom $I_E$ von Knoten 1 in das Tor und Norator-Strom $I_A$; Zeilen: Knoten 1, Ausgang, Tor, Nullator mit c an Masse und d an Knoten 1:

$$\begin{pmatrix} 0{,}01 & -0{,}01 & 1 & 0 \\ -0{,}01 & 0{,}01 & 0 & 1 \\ 1 & 0 & -10 & 0 \\ -1 & 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} U_1 \\ U_A \\ I_E \\ I_A \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0{,}1 \\ 0 \end{pmatrix}$$

Nach der Nullator-Zeile entwickelt, dann nach der Spalte des Norator-Stroms, ergibt sich die Determinante; der Zähler für $U_A$ auf dieselbe Weise:

$$\det\mathbf M = -0{,}1, \qquad \det\mathbf M_2 = 0{,}1, \qquad U_A = \frac{0{,}1}{-0{,}1}\ \mathrm V = -1\ \mathrm V$$

Aus der Nullator-Zeile ist $U_1$ null; Tor- und Ausgangszeile liefern die Ströme:

$$I_E = \frac{U_1 - U_E}{R_1} = -10\ \mu\mathrm A, \qquad I_A = -0{,}01\ \mathrm{mS}\cdot(U_A - U_1) = 10\ \mu\mathrm A$$

**Ergebnis:** **Ausgang −1 V, Verstärkung −10; die 10 µA der Quelle fließen durch $R_1$ und $R_2$ in den Ausgang.**

**Einordnung:** Die Verstärkung ist −$R_2/R_1$ wie mit den goldenen Regeln des idealen Verstärkers ([Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html)), hier ohne Überlegung aus den Mustern. Mit der gesteuerten Spannungsquelle und $v_D$ = 200 000 statt des Nullors ergibt sich −9,99945, 0,0055 % weniger.
::::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Eintragsmuster und Bezugsknoten | jedes Bauelement schreibt seinen Beitrag, ohne den Rest zu kennen |
| Cramersche Regel | jede Größe ist ein Quotient zweier Determinanten mit gemeinsamem Nenner |
| ideale Spannungsquelle | ihr Strom wird zur Unbekannten, ihre Zweiggleichung zur Zeile |
| Impedanz, Tor, gesteuerte Spannungsquelle | dasselbe Gerüst, verschieden ist nur die Zeile |
| Nullor | Zeile für den Eingang, Spalte für den Ausgangsstrom |

Jedes Bauelement schreibt seinen Beitrag als festes Muster in eine Matrix, ohne den Rest der Schaltung zu kennen; Elemente, deren Strom sich weder aus den Knotenpotentialen noch aus einem schon als Unbekannte geführten Strom ergibt, bringen diesen Strom als zusätzliche Unbekannte und ihre Zweiggleichung als zusätzliche Zeile mit, und das so entstehende quadratische System liefert, wenn es eindeutig lösbar ist, jede Größe als Quotient zweier Determinanten.

## Bedeutung und Ausblick

Schaltungssimulatoren wie SPICE arbeiten genau so: Aus der Netzliste tragen sie die Muster ein und lösen das dünn besetzte System durch Elimination, für die Wechselstromanalyse bei jeder Frequenz und für den Arbeitspunkt in jedem Schritt des Newton-Verfahrens. Grenzen setzen die Linearität und idealisierte Elemente, deren Umläufe oder Resonanzen die Determinante null machen. Im Zeitbereich werden Kondensatoren und Spulen in jedem Zeitschritt ebenfalls zu Leitwert und Stromquelle; das ist zusammen mit den Testquellen das folgende Thema.

**In der ausführlichen Fassung:** eine Analogie zur vollständigen Matrix, die Herleitung des Rechenaufwands der Cramerschen Regel gegenüber der Elimination, die Inverse über die Adjunkte und die transponierte Matrix, die Spule bei Gleichstrom und der Schwingkreis bei Resonanz, die Herleitung der Muster stromgesteuerter Quellen mit Strommesser und Transitfrequenz, Fehlvorstellungen und Fragen zum Nullor, der Frequenzgang mit Polen und Bode-Diagramm und das Begleitmodell des Newton-Verfahrens als Muster. [Zur ausführlichen Fassung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/modifizierte-knotenanalyse-ausfuehrlich.html)

:::kern
- Jede Zeile der Leitwertmatrix ist die Knotengleichung eines Knotens; die Matrix ist die Summe der Eintragsmuster aller Bauelemente.
- Admittanz: +Y auf den Diagonalplätzen ihrer Knoten, −Y auf den Kreuzungsplätzen; gesteuerte Stromquelle: Zeilen der Stromknoten, Spalten der Steuerknoten; unabhängige Stromquelle: nur rechte Seite.
- In der vollständigen Matrix ist jede Zeilen- und Spaltensumme null; Zeile und Spalte des Bezugsknotens werden gestrichen.
- Cramersche Regel: $x_\nu = \det\mathbf A_\nu / \det\mathbf A$; entwickelt wird nach der Zeile oder Spalte mit den meisten Nullen.
- Modifizierte Knotenanalyse: Ein Element, dessen Strom sich nicht aus vorhandenen Unbekannten ergibt, bekommt seinen Strom als Unbekannte (Spalte +1, −1) und seine Zweiggleichung als Zeile.
- Tor: $\underline U_a - \underline U_b - \underline Z\,\underline I_z = \underline U_q$; ideale Quelle mit Z gleich null, Impedanz mit $\underline U_q$ gleich null.
- Nullor: Zeile $\underline U_c - \underline U_d = 0$ für den Eingang, Spalte für den Strom des Ausgangs.
- Die Determinante steht im Nenner aller Knotenspannungen; sind die Einträge Polynome in der komplexen Frequenz, ist jeder Pol eine Nullstelle von ihr.
:::

:::quiz
F: Warum darf man jedes Bauelement für sich eintragen, ohne den Rest der Schaltung zu kennen?
A: Jede Knotengleichung ist eine Summe über die Ströme aller Bauelemente, und ein Bauelement kommt nur in den Gleichungen seiner Knoten vor, mit Faktoren in den Spalten der Potentiale, die seinen Strom bestimmen. Die Beiträge addieren sich deshalb Eintrag für Eintrag.
F: Stimmt es, dass man beim Eintragen einer Admittanz die wirkliche Stromrichtung kennen muss?
A: Nein. Mit umgekehrter Zählrichtung vertauschen sich a und b, und das Muster bleibt gleich; wie der Strom zur Zählrichtung liegt, zeigt das Vorzeichen der Lösung, etwa −2,33 µA durch $R_D$, von D nach Masse gezählt.
F: Warum lässt sich eine ideale Spannungsquelle nicht in die Leitwertmatrix eintragen?
A: Ihr Strom ist kein festes Vielfaches von Potentialen; bei ihrer Spannung lässt sie jeden Strom zu, und die Umwandlung in eine Stromquelle ergäbe ohne Innenwiderstand einen unendlichen Strom. Deshalb wird ihr Strom zur Unbekannten und ihre Zweiggleichung zur Zeile.
F: Stimmt es, dass der Zusatzstrom einer Spannungsquelle der Strom ist, den sie abgibt?
A: Nein. Gezählt wird von a durch die Quelle nach b, also in den Pluspol hinein; im RC-Tiefpass ist der Zusatzstrom −(0,667 + 0,333j) mA, abgegeben werden 0,745 mA bei +26,6°.
F: Warum ist jede Knotenspannung ein Quotient zweier Determinanten mit demselben Nenner?
A: Setzt man die rechte Seite als Summe der Spalten, gewichtet mit den Unbekannten, in Spalte ν ein, überlebt nach Linearität nur der Summand mit der eigenen Spalte; er ist die Unbekannte mal der Determinante der Matrix, die deshalb in jedem Nenner steht, sofern sie nicht null ist.
F: Eine Leitwertmatrix hat die Determinante 0,043 mS³, die Matrix mit der Spalte des Drains durch die rechte Seite ersetzt −1 mS²·µA. Wie groß ist die Drainspannung?
A: Nach Cramer −1/0,043 mV, also −23,26 mV.
:::
