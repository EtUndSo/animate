---
title: Netzwerkgleichungen systematisch aufstellen: modifizierte Knotenanalyse
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse
order: 33020300
summary: Wie man das Gleichungssystem jeder linearen Schaltung Bauteil für Bauteil nach festen Eintragsmustern aufstellt, auch mit idealen Spannungsquellen, Kurzschlüssen, Spulen bei Gleichstrom, gesteuerten Spannungsquellen und idealen Operationsverstärkern, und wie man es mit Determinanten löst. Ausführliche Fassung mit Herleitung der Muster, der Determinantenformeln, der Cramerschen Regel, des Rechenaufwands, der Inversen über die Adjunkte und der Pole als Nullstellen der Determinante, durchgerechnet an RC-Tiefpass, Verstärkerstufe, Schwingkreis, Transitfrequenz, invertierendem Verstärker und Bode-Diagramm.
tags: Leitwertmatrix, modifizierte Knotenpotentialanalyse, Cramersche Regel, Determinante
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Eine Schaltung mit hundert Knoten von Hand in Knotengleichungen zu zerlegen, kostet Stunden und lädt zu Vorzeichenfehlern ein; ein Schaltungssimulator muss dasselbe für Millionen Knoten leisten, ohne die Schaltung anzusehen. Dazu kommt, dass die Knotenanalyse an alltäglichen Elementen scheitert: an idealen Spannungsquellen, an Kurzschlüssen und Strommessern, an Spulen bei Gleichstrom, an gesteuerten Spannungsquellen und am idealen Operationsverstärker. Beides löst ein Prinzip:

**Jedes Bauelement schreibt seinen Beitrag als festes Muster in eine Matrix, ohne den Rest der Schaltung zu kennen; Elemente, deren Strom sich weder aus den Knotenpotentialen noch aus einem schon als Unbekannte geführten Strom ergibt, bringen diesen Strom als zusätzliche Unbekannte und ihre Zweiggleichung als zusätzliche Zeile mit, und das so entstehende quadratische System liefert, wenn es eindeutig lösbar ist, jede Größe als Quotient zweier Determinanten.**

Vorausgesetzt werden die Knotenpotentialanalyse mit Leitwertmatrix und gesteuerten Stromquellen aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html), das Rechnen mit [Zeigern](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html) und für ein Beispiel [der ideale Operationsverstärker](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html). Auf dem Verfahren beruhen die Arbeitspunkt-, Wechselstrom- und Zeitbereichsanalyse der meisten Schaltungssimulatoren, etwa SPICE.

:::grafik
Szene: st1/netzwerkanalyse/03-netzliste-matrix · Vorlage: netzliste-matrix
**Abbildung 1:** (a) RC-Tiefpass mit idealer Spannungsquelle 1 V zwischen Knoten 1 und Masse, $R_1$ und $R_2$ je 1 kΩ, $C_1$ und $C_2$ je 100 nF, bei ω = 10⁴ 1/s. (b) Seine Netzliste, eine Zeile je Bauteil mit Knoten und Wert. (c) Die Matrix der modifizierten Knotenanalyse in mS, kΩ, V und mA, Zeilen (1; −1; 0; 1), (−1; 2 + j; −1; 0), (0; −1; 1 + j; 0), (1; 0; 0; 0), jeder Eintrag in der Farbe des Bauteils, das ihn liefert. Jedes Bauteil schreibt ein festes Muster in die Zeilen und Spalten seiner Knoten; die Matrix ist die Summe dieser Muster.
:::

## Die Matrix Bauteil für Bauteil

*Wie füllt man die Leitwertmatrix, ohne die Knotengleichungen einzeln aufzuschreiben?*

Als durchgehendes Beispiel dient die Verstärkerstufe aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html), eine Source-Schaltung mit einem MOSFET. Ihr Kleinsignal-Ersatzschaltbild enthält eine Signalquelle von 10 mV mit 10 kΩ Innenwiderstand am Gate, Drain- und Lastwiderstand von je 10 kΩ, einen Source-Widerstand von 1 kΩ, die gesteuerte Stromquelle des Transistors mit der __Steilheit__ $g_m$ = 1 mS und den __Ausgangsleitwert__ $g_o$ = 25 µS zwischen Drain und Source, der beschreibt, dass der Drainstrom auch mit der Drain-Source-Spannung leicht steigt. Der Strom von $g_o$, vom Drain zur Source gezählt, verlässt in dieser Zählrichtung den Drain und erreicht die Source; er kommt deshalb in genau zwei Knotengleichungen vor, in der des Drains als abfließender und in der der Source als zufließender Strom. Nach den Potentialen geordnet, liefert er vier Einträge: +0,025 mS an den Plätzen (D, D) und (S, S), −0,025 mS an (D, S) und (S, D). Keine andere Stelle der Matrix hängt von $g_o$ ab, und um sie zu schreiben, braucht man vom Rest der Schaltung nichts zu wissen.

Diesen festen Beitrag eines Bauelements nennt man sein __Eintragsmuster__, englisch stamp: die Einträge, die es in die Matrix und in die rechte Seite schreibt, ausgedrückt durch seinen Wert und die Namen seiner Knoten. Die Matrix der ganzen Schaltung ist die Summe der Muster aller ihrer Bauelemente; Abbildung 2 zeigt die drei Muster, aus denen eine reine Knotenanalyse besteht.

:::grafik
Szene: st1/netzwerkanalyse/03-eintragsmuster-knoten · Vorlage: musterkarten
**Abbildung 2:** Eintragsmuster für die Knotenanalyse. Links eine Admittanz zwischen den Knoten a und b: +Y auf den Plätzen (a, a) und (b, b), −Y auf (a, b) und (b, a). Mitte eine spannungsgesteuerte Stromquelle, deren Strom von a nach b fließt und von der Spannung zwischen c und d gesteuert wird: ±g in den Zeilen a, b und den Spalten c, d. Rechts eine unabhängige Stromquelle, die in a hineinspeist: nur die rechte Seite, +I in Zeile a, −I in Zeile b. Am Rand jeder Karte die Vorzeichen der Zeilen und Spalten, deren Produkt im Feld steht. Ein Bauelement erscheint nur in den Zeilen der Knoten, zwischen denen sein Strom fließt, und in den Spalten der Knoten, deren Spannung diesen Strom bestimmt.
:::

**Die Akteure:**

- __Bezugsknoten__ 0 und die übrigen Knoten; __$n_K$__: Zahl der übrigen Knoten und damit der Unbekannten; 3 in der Verstärkerstufe (Gate G, Drain D, Source S).
- __$\underline U_\nu$__: Potential des Knotens ν gegen den Bezugsknoten, ein Zeiger; in V.
- __$\mathbf Y$__: __Leitwertmatrix__ mit $n_K$ Zeilen und Spalten. Zeile μ ist die Knotengleichung des Knotens μ, Spalte ν gehört zum Potential des Knotens ν; der Eintrag __$\underline Y_{\mu\nu}$__ ist der Strom, der in der Gleichung von μ je Volt am Knoten ν abfließt; in S.
- __$\underline I_{q\mu}$__: Summe der Ströme unabhängiger Quellen, die in den Knoten μ hineinfließen; in A. Sie bilden die rechte Seite.
- __a__, __b__: die beiden Knoten, zwischen denen der Strom eines Bauelements fließt; gezählt wird er von a nach b, nur bei der unabhängigen Stromquelle durch die Quelle von b nach a, sodass sie in a einspeist.
- __c__, __d__: die Knoten der Steuerspannung einer gesteuerten Quelle, c am Pluspol.
- __$\underline Y$__: Admittanz eines Zweipols, $G$ für einen Widerstand, $j\omega C$ für einen Kondensator; __$g$__: Steilheit einer spannungsgesteuerten Stromquelle, beim Transistor $g_m$ = 1 mS; __$\underline I_q$__: Strom einer unabhängigen Stromquelle.

**Das Zusammenspiel:**

**Schritt 1**: Jede Zeile ist eine Knotengleichung in der Form „Summe der über Bauelemente abfließenden Ströme gleich Summe der eingespeisten Quellenströme“.

**Schritt 2**: Ein Bauelement liefert einen Summanden nur in den Gleichungen der Knoten, die sein Strom berührt, also in den Zeilen a und b, und zwar in a als abfließenden, in b als zufließenden Strom.

**Schritt 3**: Dieser Strom ist ein festes Vielfaches der Potentiale, die ihn treiben, und die Faktoren stehen in den Spalten dieser Potentiale: bei der Admittanz in den Spalten a und b, weil die Spannung zwischen a und b selbst den Strom treibt, bei der gesteuerten Stromquelle in den Spalten c und d. Eine unabhängige Stromquelle hängt von keinem Potential ab und erscheint nur auf der rechten Seite.

**Schritt 4**: Weil jede Knotengleichung eine Summe über alle Bauelemente ist, addieren sich die Beiträge Eintrag für Eintrag; die Reihenfolge des Eintragens ist gleichgültig, und kein Muster hängt von einem anderen ab.

:::formel Formel
$$\begin{array}{c|cc} & a & b \\ \hline a & +\underline Y & -\underline Y \\ b & -\underline Y & +\underline Y \end{array}$$

$$\begin{array}{c|cc} & c & d \\ \hline a & +g & -g \\ b & -g & +g \end{array}$$

$$\begin{array}{c|c} & \text{rechts} \\ \hline a & +\underline I_q \\ b & -\underline I_q \end{array}$$
:::

**So liest man das:** Das erste Muster gehört zur Admittanz, das zweite zur spannungsgesteuerten Stromquelle, das dritte zur unabhängigen Stromquelle, die in a hineinspeist; Zeilen sind Knotengleichungen, Spalten Potentiale. Jedes Vorzeichen ist das Produkt zweier Faktoren: In der Zeile steht +1 für den Knoten, den der Strom in Zählrichtung verlässt, und −1 für den, in den er hineinfließt; in der Spalte steht +1 für den Knoten, dessen Potential in der Zweiggleichung mit plus steht, $\underline U_a$ bei der Admittanz und $\underline U_c$ bei der gesteuerten Quelle, und −1 für den anderen. Bei der Admittanz sind Strom- und Steuerknoten dieselben, daher plus auf der Diagonalen und minus auf den Kreuzungsplätzen. Hängt ein Anschluss am Bezugsknoten, entfallen seine Zeile und Spalte, wie im Abschnitt *Der Bezugsknoten* gezeigt.

**Kurz gesagt:** Die Leitwertmatrix einer Schaltung ist die Summe der Eintragsmuster ihrer Bauelemente, und jedes Muster hängt nur vom Bauelement und den Knoten ab, an denen es hängt.

Eine gesteuerte Stromquelle gehört deshalb in die Matrix und nicht auf die rechte Seite: Ihr Strom hängt von unbekannten Potentialen ab, er ist keine Anregung ([Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html), Abschnitt *Gesteuerte Quellen in der Knotengleichung*).

:::fehlvorstellung
„Beim Eintragen muss man wissen, in welche Richtung der Strom wirklich fließt, sonst stimmen die Vorzeichen nicht.“ Das liegt nahe, weil das Muster mit einer Zählrichtung von a nach b aufgeschrieben ist. Für eine Admittanz ist diese Richtung aber frei wählbar: Wer von b nach a zählt, vertauscht a und b, und das Muster bleibt dasselbe, denn plus steht weiter auf beiden Diagonalplätzen und minus auf beiden Kreuzungsplätzen. Wie der Strom zur gewählten Zählrichtung liegt, zeigt erst das Vorzeichen der Lösung: Durch $R_D$ der Verstärkerstufe fließen, von D nach Masse gezählt, −2,33 µA, in der Gegenrichtung gezählt also +2,33 µA. Bei Gleichgrößen ist das die Richtung des Stroms, bei Zeigern seine Phasenlage, bezogen auf die Zählrichtung; hier ist der von D nach Masse gezählte Strom gegenphasig zur Signalspannung. Vorgegeben ist die Zählrichtung nur bei Quellen, denn dort gehört sie zur Angabe.
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

### Der Bezugsknoten

*Warum hat die Matrix eine Zeile und eine Spalte weniger, als die Schaltung Knoten hat?*

Trägt man die Muster ein, ohne einen Knoten auszunehmen, bekommt auch die Masse ihre Zeile und Spalte. Für die Verstärkerstufe entsteht so eine Matrix mit vier Zeilen und Spalten, 0, G, D und S (Abbildung 3). In ihr ist jede Zeilensumme null und jede Spaltensumme null.

:::grafik
Szene: st1/netzwerkanalyse/03-vollstaendige-matrix · Vorlage: schaltbild-matrix
**Abbildung 3:** Links das Kleinsignal-Ersatzschaltbild der Verstärkerstufe mit Signalquelle als Stromquelle 1 µA parallel zu 0,1 mS, $G_D$ und $G_L$ je 0,1 mS, $G_S$ 1 mS, $g_o$ 0,025 mS und der gesteuerten Quelle 1 mS. Rechts die vollständige Matrix mit den Zeilen und Spalten 0, G, D, S in mS: (1,3; −0,1; −0,2; −1), (−0,1; 0,1; 0; 0), (−0,2; 1; 0,225; −1,025), (−1; −1; −0,025; 2,025); am Rand alle Zeilen- und Spaltensummen null; Zeile und Spalte 0 gestrichen. In der vollständigen Matrix ist jede Zeilen- und Spaltensumme null; streicht man Zeile und Spalte des Bezugsknotens, bleibt die lösbare Leitwertmatrix.
:::

Die Zeilensummen verschwinden, weil nur Potentialdifferenzen Ströme treiben: Hebt man alle Potentiale um denselben Betrag an, ändert sich kein Strom, also auch keine Knotengleichung. Die Spaltensummen verschwinden, weil jeder Strom, der einen Knoten verlässt, in einen anderen hineinfließt: Addiert man alle Knotengleichungen, hebt sich jeder Strom heraus.

Beides hat dieselbe Folge. Die vollständige Matrix legt die Potentiale nur bis auf eine gemeinsame Konstante fest, und eine ihrer Gleichungen folgt aus den übrigen; ihre Determinante ist null. Wählt man einen Knoten als __Bezugsknoten__ mit dem Potential null, multipliziert seine Spalte nur noch null und entfällt, und seine Zeile entfällt, weil sie die negative Summe der anderen ist. Übrig bleibt die Leitwertmatrix mit $n_K$ Zeilen und Spalten. Ein Bauelement zwischen a und dem Bezugsknoten hinterlässt deshalb nur einen Eintrag, $+\underline Y$ auf dem Diagonalplatz (a, a).

**Kurz gesagt:** In der vollständigen Matrix ist jede Zeilensumme null, weil nur Potentialdifferenzen Ströme treiben, und jede Spaltensumme null, weil jeder Strom, der einen Knoten verlässt, in einen anderen hineinfließt.

:::analogie
Das Eintragen gleicht der doppelten Buchführung. Jeder Geschäftsvorfall wird zweimal gebucht, auf einem Konto als Abgang und auf einem anderen als Zugang; deshalb ist die Summe über alle Konten stets null, und ein Konto lässt sich aus den übrigen berechnen. Ebenso bucht jedes Bauelement seinen Strom als Abgang am einen und als Zugang am anderen Knoten.

| Im Vergleich | In der Schaltung |
|---|---|
| Konto | Knoten mit seiner Knotengleichung |
| Buchung als Abgang und Zugang | Strom in Zeile a mit plus, in Zeile b mit minus |
| Summe aller Konten gleich null | Spaltensummen der vollständigen Matrix gleich null |
| ein Konto ist überzählig | die Zeile des Bezugsknotens entfällt |

**Wo der Vergleich nicht stimmt:** Eine Buchung hat einen festen Betrag; ein Bauelementstrom ist erst bekannt, wenn die Potentiale berechnet sind, deshalb stehen in der Matrix seine Faktoren je Volt, in den Spalten der Potentiale, die ihn bestimmen. Und eine gesteuerte Quelle bucht ihren Strom an anderen Knoten als denen, die seine Höhe bestimmen.
:::

:::frage
„Wozu schreibt man Zeile und Spalte der Masse überhaupt hin, wenn man sie danach streicht?“
Ein Programm trägt so jedes Bauelement nach demselben Muster ein, ohne prüfen zu müssen, ob ein Anschluss an Masse liegt. Die vollständige Matrix liefert außerdem eine Probe: Ihre Zeilen- und Spaltensummen müssen null sein; in der Verstärkerstufe ist 1,3 mS in der Ecke genau die Summe 0,1 + 0,2 + 1 mS aller Leitwerte an Masse. Und sie lässt die Wahl des Bezugsknotens offen: Streicht man Zeile und Spalte eines anderen Knotens, erhält man die Potentiale gegen diesen Knoten. In der Literatur heißt sie deshalb auch unbestimmte Leitwertmatrix.
:::

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

::::beispiel Leitwertmatrix der Verstärkerstufe Bauteil für Bauteil
**Gegeben:** das Kleinsignal-Ersatzschaltbild der Verstärkerstufe (Abbildung 3): Signalquelle 10 mV mit 10 kΩ, als Stromquelle 1 µA in G parallel zu $G_\mathrm{sig}$ = 0,1 mS; $G_D$ = $G_L$ = 0,1 mS von D nach Masse; $G_S$ = 1 mS von S nach Masse; $g_o$ = 0,025 mS zwischen D und S; gesteuerte Quelle mit $g_m$ = 1 mS, Strom von D nach S, gesteuert von der Spannung zwischen G und S.

**Gesucht:** die vollständige Matrix aus den Mustern, die Leitwertmatrix und die Knotenpotentiale.

**Rechnung:** In mS, mV und µA, Zeilen und Spalten in der Reihenfolge 0, G, D, S. Die Signalquelle trägt 0,1 auf (0, 0) und (G, G) und −0,1 auf (0, G) und (G, 0) ein, rechts +1 in Zeile G und −1 in Zeile 0. $G_D$ und $G_L$ zusammen tragen 0,2 auf (0, 0) und (D, D) und −0,2 auf (0, D) und (D, 0) ein, $G_S$ ebenso 1 an den Plätzen aus 0 und S. $g_o$ liefert ±0,025 an den Plätzen aus D und S, die gesteuerte Quelle +1 auf (D, G) und (S, S) und −1 auf (D, S) und (S, G). Die Summe ist die vollständige Matrix:

$$\begin{pmatrix} 1{,}3 & -0{,}1 & -0{,}2 & -1 \\ -0{,}1 & 0{,}1 & 0 & 0 \\ -0{,}2 & 1 & 0{,}225 & -1{,}025 \\ -1 & -1 & -0{,}025 & 2{,}025 \end{pmatrix}$$

Die rechte Seite in µA, in derselben Reihenfolge:

$$\begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix}$$

Probe der Summen, Zeile D und Spalte G als Beispiele:

$$-0{,}2 + 1 + 0{,}225 - 1{,}025 = 0, \qquad -0{,}1 + 0{,}1 + 1 - 1 = 0$$

Streichen von Zeile und Spalte 0 ergibt die Leitwertmatrix und das System:

$$\begin{pmatrix} 0{,}1 & 0 & 0 \\ 1 & 0{,}225 & -1{,}025 \\ -1 & -0{,}025 & 2{,}025 \end{pmatrix} \begin{pmatrix} \underline U_G \\ \underline U_D \\ \underline U_S \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$

**Ergebnis:** **Dieselbe Leitwertmatrix wie beim Aufstellen nach Augenschein; Lösung 10 mV, −23,26 mV und 4,65 mV.**

**Einordnung:** Die Muster liefern die Matrix, ohne dass man an einem Knoten überlegt, welche Leitwerte dort zusammenkommen. Die gestrichene Zeile 0 dient als Probe: Setzt man die Lösung ein, ergibt ihre linke Seite −1 µA, genau ihre rechte Seite, denn der Strom von 1 µA, den die Signalquelle aus der Masse holt, muss über die Leitwerte dorthin zurückkehren.
::::

## Lösen mit Determinanten: die Cramersche Regel

*Wie berechnet man eine einzelne Knotenspannung, ohne das ganze System umzuformen?*

Ein System mit zwei Unbekannten löst man durch Elimination. Für die Gleichungen

$$a_{11}\,x_1 + a_{12}\,x_2 = b_1$$

$$a_{21}\,x_1 + a_{22}\,x_2 = b_2$$

multipliziert man die erste mit $a_{21}$, die zweite mit $a_{11}$ und zieht sie voneinander ab; $x_1$ fällt heraus:

$$x_2 = \frac{a_{11}\,b_2 - a_{21}\,b_1}{a_{11}\,a_{22} - a_{12}\,a_{21}}$$

Beim RC-Tiefpass, dessen Quelle samt $R_1$ in eine Stromquelle von 1 mA parallel zu 1 mS umgewandelt ist, sind das in mS, V und mA die Einträge 2 + j, −1, −1, 1 + j und rechts die Werte 1 und 0. Unbekannte sind die Potentiale $\underline U_2$ und $\underline U_3$ der Knoten 2 und 3 aus Abbildung 1, und für die Ausgangsspannung $\underline U_3$, die zweite Unbekannte, ergibt sich:

$$\underline U_3 = \frac{(2 + j)\cdot 0 - (-1)\cdot 1}{(2 + j)(1 + j) - (-1)(-1)}\ \mathrm V = \frac{1}{3j}\ \mathrm V = -\frac{j}{3}\ \mathrm V$$

Zwei Dinge fallen auf: Der Nenner hängt nur von der Matrix ab, und der Zähler ist derselbe Ausdruck, gebildet aus der Matrix, in der die Spalte von $x_2$ durch die rechte Seite ersetzt ist.

Ein solcher Ausdruck aus den Einträgen einer quadratischen Matrix heißt __Determinante__. Sie entscheidet, ob ein lineares Gleichungssystem genau eine Lösung hat, und jede Unbekannte ist der Quotient zweier Determinanten. Für mehr als zwei Unbekannte führt man sie schrittweise auf kleinere zurück.

:::grafik
Szene: st1/netzwerkanalyse/03-cramer-laplace · Vorlage: matrix-schema
**Abbildung 4:** (a) Leitwertmatrix der Verstärkerstufe in mS, Zeilen (0,1; 0; 0), (1; 0,225; −1,025), (−1; −0,025; 2,025), daneben dieselbe Matrix mit Spalte D durch die rechte Seite (1; 0; 0) µA ersetzt. (b) Entwicklung nach der ersetzten Spalte: Das Schachbrett der Vorzeichen liegt über der Matrix, der einzige Eintrag ungleich null, 1 µA oben, trägt minus, seine Unterdeterminante (1; −1,025 / −1; 2,025) ist 1, das Ergebnis −1. (c) Sarrus-Schema für die Determinante: drei absteigende Diagonalen mit plus, drei aufsteigende mit minus, zusammen 0,043 mS³. Darunter die Drainspannung, −1 durch 0,043 in mV, also −23,26 mV. Jede Unbekannte ist ein Quotient zweier Determinanten mit demselben Nenner; man entwickelt nach der Zeile oder Spalte mit den meisten Nullen.
:::

**Die Akteure:**

- __$\mathbf A$__: quadratische Matrix mit $n$ Zeilen und Spalten und den Einträgen __$a_{\mu\nu}$__ (Zeile μ, Spalte ν), reell oder komplex; in diesem Thema die Leitwertmatrix oder die Matrix der modifizierten Knotenanalyse.
- __$\vec x$__: Spalte der Unbekannten $x_1, \ldots, x_n$; __$\vec b$__: rechte Seite mit den Einträgen $b_1, \ldots, b_n$.
- __$\det\mathbf A$__: Determinante von $\mathbf A$, eine reelle oder komplexe Zahl; für die Leitwertmatrix in Sⁿ, bei der Verstärkerstufe 0,043 mS³.
- __$\mathbf A^{(\mu\nu)}$__: __Streichungsmatrix__, $\mathbf A$ ohne Zeile μ und Spalte ν, mit $n - 1$ Zeilen und Spalten; ihre Determinante heißt __Unterdeterminante__.
- __$\mathbf A_\nu$__: die Matrix $\mathbf A$, deren Spalte ν durch $\vec b$ ersetzt ist.

:::formel Definition
$$\det\mathbf A = \sum_{\nu=1}^{n} (-1)^{1+\nu}\,a_{1\nu}\,\det\mathbf A^{(1\nu)}$$
:::

Für $n$ = 1 ist die Determinante der einzige Eintrag. Man definiert sie so, weil genau dieser Ausdruck bei der Elimination im Nenner entsteht, für zwei Unbekannte als $a_{11}a_{22} - a_{12}a_{21}$, und weil sich mit der Vorschrift jede Determinante auf Determinanten mit einer Zeile weniger zurückführen lässt. Für zwei und drei Zeilen folgen daraus die bekannten Formeln, die zweite heißt __Regel von Sarrus__:

$$\det\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix} = a_{11}\,a_{22} - a_{12}\,a_{21}$$

$$\begin{aligned} \det\mathbf A = {} & a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} \\ & - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33} \end{aligned}$$

Die Definition entwickelt nach der ersten Zeile. Tatsächlich darf man jede Zeile und jede Spalte nehmen:

:::formel Satz
$$\det\mathbf A = \sum_{\nu=1}^{n} (-1)^{\mu+\nu}\,a_{\mu\nu}\,\det\mathbf A^{(\mu\nu)} \qquad \text{für jede Zeile } \mu$$

$$\det\mathbf A = \sum_{\mu=1}^{n} (-1)^{\mu+\nu}\,a_{\mu\nu}\,\det\mathbf A^{(\mu\nu)} \qquad \text{für jede Spalte } \nu$$
:::

**So liest man das:** Man wählt eine Zeile oder Spalte, multipliziert jeden ihrer Einträge mit der Unterdeterminante ohne seine Zeile und Spalte und gibt dem Produkt das Vorzeichen eines Schachbretts: plus oben links, nach rechts und nach unten abwechselnd. Am wenigsten Arbeit macht die Zeile oder Spalte mit den meisten Nullen, denn jeder Nulleintrag spart eine ganze Unterdeterminante. In Schaltungsmatrizen sind das oft die Zeile einer Quelle oder eine durch die rechte Seite ersetzte Spalte, die nur einen Eintrag ungleich null hat. Eine Determinante mit vier Zeilen zerfällt so in vier mit drei Zeilen, die man nach Sarrus ausrechnet. Abbildung 4 zeigt beide Wege an der Verstärkerstufe.

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

**Schritt 1**: Die Determinante der Matrix berechnen, entwickelt nach der Zeile oder Spalte mit den meisten Nullen.

**Schritt 2**: Die Spalte der gesuchten Unbekannten durch die rechte Seite ersetzen.

**Schritt 3**: Die Determinante dieser Matrix berechnen, am besten nach der ersetzten Spalte; hat die rechte Seite nur einen Eintrag, bleibt eine einzige Unterdeterminante.

**Schritt 4**: Die zweite Determinante durch die erste teilen.

Dass das stimmt, sagt ein Satz, der das Muster vom Anfang des Abschnitts für jede Zahl von Unbekannten ausspricht:

:::formel Satz
$$x_\nu = \frac{\det\mathbf A_\nu}{\det\mathbf A}, \qquad \nu = 1, \ldots, n$$
:::

**So liest man das:** Zähler und Nenner unterscheiden sich nur in der Spalte ν, im Zähler steht dort die rechte Seite (Abbildung 4a). Wer nur eine Knotenspannung braucht, rechnet zwei Determinanten und lässt den Rest des Systems unberührt. Die Regel heißt __Cramersche Regel__; sie gilt, solange $\det\mathbf A$ nicht null ist, und genau dann hat das System für jede rechte Seite genau eine Lösung. Ist $\det\mathbf A$ null, gibt es keine oder unendlich viele.

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
**Gegeben:** die Leitwertmatrix der Verstärkerstufe in mS mit Zeilen und Spalten G, D, S, (0,1; 0; 0), (1; 0,225; −1,025), (−1; −0,025; 2,025), und die rechte Seite (1; 0; 0) µA.

**Gesucht:** die Determinante und die drei Knotenspannungen.

**Rechnung:** Determinante nach Zeile G, die nur einen Eintrag hat:

$$\det\mathbf Y = 0{,}1\cdot\det\begin{pmatrix} 0{,}225 & -1{,}025 \\ -0{,}025 & 2{,}025 \end{pmatrix} = 0{,}1\cdot 0{,}43 = 0{,}043\ \mathrm{mS^3}$$

Für den Drain ersetzt die rechte Seite Spalte D; diese Spalte hat nur oben eine 1, mit dem Schachbrettvorzeichen minus:

$$\begin{aligned} \det\mathbf Y_D &= \det\begin{pmatrix} 0{,}1 & 1 & 0 \\ 1 & 0 & -1{,}025 \\ -1 & 0 & 2{,}025 \end{pmatrix} \\ &= -1\cdot\det\begin{pmatrix} 1 & -1{,}025 \\ -1 & 2{,}025 \end{pmatrix} = -1\ \mathrm{mS^2\,\mu A} \end{aligned}$$

Ebenso für die Source, Vorzeichen plus, und für das Gate:

$$\det\mathbf Y_S = +1\cdot\det\begin{pmatrix} 1 & 0{,}225 \\ -1 & -0{,}025 \end{pmatrix} = 0{,}2\ \mathrm{mS^2\,\mu A}, \qquad \det\mathbf Y_G = 1\cdot 0{,}43 = 0{,}43\ \mathrm{mS^2\,\mu A}$$

Quotienten, mit µA/mS gleich mV:

$$\underline U_D = \frac{-1}{0{,}043}\ \mathrm{mV} = -23{,}26\ \mathrm{mV}, \qquad \underline U_S = \frac{0{,}2}{0{,}043}\ \mathrm{mV} = 4{,}65\ \mathrm{mV}, \qquad \underline U_G = 10\ \mathrm{mV}$$

**Ergebnis:** **Determinante 0,043 mS³; Knotenspannungen 10 mV, −23,26 mV und 4,65 mV.**

**Einordnung:** Jede Zählerdeterminante kostete hier nur eine Unterdeterminante mit zwei Zeilen, weil die rechte Seite einen einzigen Eintrag hat. Nach Sarrus ergibt sich dieselbe Determinante, 0,0455625 − 0,0025625 mS³; nur zwei der sechs Produkte sind ungleich null.
::::

### Wie viel Rechenarbeit eine Determinante kostet

*Warum lösen Schaltungssimulatoren ihre Gleichungen nicht mit der Cramerschen Regel?*

:::grafik
Szene: st1/netzwerkanalyse/03-rechenaufwand · Vorlage: kennlinie-semilog
**Abbildung 5:** Zahl der Multiplikationen und Divisionen über der Zahl der Unbekannten von 2 bis 25, senkrechte Achse logarithmisch. Rot die Cramersche Regel mit Entwicklung: 39 bei drei Unbekannten, 6,9·10⁷ bei zehn, 8,8·10¹⁹ bei zwanzig. Blau die Gauß-Elimination: 17, 430 und 3060. Gestrichelt die Rechenzeiten bei 10⁹ Operationen je Sekunde: eine Sekunde, eine Stunde, ein Jahr. Determinanten durch Entwicklung kosten rund n! Rechenschritte, die Elimination rund n³/3; die Cramersche Regel lohnt sich nur für kleine Systeme und für Formeln.
:::

Die Entwicklung führt eine Determinante mit $n$ Zeilen auf $n$ Determinanten mit $n - 1$ Zeilen zurück, jede von ihnen auf $n - 1$ kleinere und so fort; die Cramersche Regel braucht $n + 1$ solche Determinanten. Die __Gauß-Elimination__ zieht dagegen Vielfache einer Zeile von den Zeilen darunter ab, bis unter der Diagonalen nur Nullen stehen, und rechnet die Unbekannten danach von unten nach oben aus. Mit __$N_\mathrm{Entw}(n)$__ für die Multiplikationen einer Determinante mit $n$ Zeilen und __$N_\mathrm{Elim}(n)$__ für die Multiplikationen und Divisionen, mit denen die Elimination ein System mit $n$ Unbekannten löst, gilt:

$$N_\mathrm{Entw}(n) = n\,\big(N_\mathrm{Entw}(n - 1) + 1\big) \approx 1{,}72\cdot n!, \qquad N_\mathrm{Elim}(n) = \frac{n^3 - n}{3} + n^2$$

Abbildung 5 zeigt, was das bedeutet. Bei drei Unbekannten liegen beide Wege mit 39 und 17 Operationen noch nahe beieinander. Bei zwanzig Unbekannten braucht die Cramersche Regel 8,8·10¹⁹ Operationen, bei 10⁹ Operationen je Sekunde rund 2800 Jahre; die Elimination ist nach 3060 Operationen, also 3 µs, fertig. Schaltungssimulatoren verwenden deshalb die Elimination, in einer Form, die die Nullen der Matrix ausnutzt: Jedes Bauelement hängt an zwei bis vier Knoten; eine Zeile hat deshalb außer dem Diagonaleintrag nur Einträge für die Knoten, mit denen ihr Knoten über ein Bauelement verbunden ist oder die einen Strom an ihm steuern. Eine vollbesetzte Matrix mit einer Million Knoten bräuchte rund 3·10¹⁷ Multiplikationen, gut zehn Jahre; die __dünn besetzte__ Matrix einer echten Schaltung, in der fast alle Einträge null sind, lösen Simulatoren um Größenordnungen schneller.

Die Cramersche Regel bleibt das Werkzeug für Formeln: Sie liefert eine Knotenspannung als geschlossenen Ausdruck in den Bauteilwerten, und für Systeme mit bis zu vier Unbekannten, wie sie beim Rechnen von Hand vorkommen, ist sie schnell genug.

Idee der Herleitung: Man zählt die Multiplikationen der Entwicklung rekursiv und die der Elimination Schritt für Schritt.

:::herleitung
**Ausgangspunkt:** die Definition der Determinante durch Entwicklung und das Vorgehen der Gauß-Elimination.

**Annahmen:** (i) Gezählt werden Multiplikationen und Divisionen; Additionen fallen etwa gleich oft an und ändern das Wachstum nicht. (ii) Die Matrix ist vollbesetzt; Nullen werden nicht ausgenutzt.

**Schritt 1**: Die Entwicklung hat $n$ Summanden, jeder braucht eine Unterdeterminante mit $n - 1$ Zeilen und eine Multiplikation; für zwei Zeilen sind es zwei Multiplikationen:

$$N_\mathrm{Entw}(n) = n\,\big(N_\mathrm{Entw}(n - 1) + 1\big), \qquad N_\mathrm{Entw}(2) = 2$$

**Schritt 2**: Teilt man durch $n!$, wird daraus eine Summe; für großes $n$ strebt sie gegen $\exp(1) - 1$, also 1,718:

$$\frac{N_\mathrm{Entw}(n)}{n!} = \frac{N_\mathrm{Entw}(n-1)}{(n-1)!} + \frac{1}{(n-1)!}$$

$$\frac{N_\mathrm{Entw}(n)}{n!} = 1 + \frac{1}{2!} + \frac{1}{3!} + \cdots + \frac{1}{(n-1)!}$$

**Schritt 3**: Die Cramersche Regel braucht $n + 1$ Determinanten und $n$ Divisionen:

$$(n + 1)\,N_\mathrm{Entw}(n) + n$$

**Schritt 4** (entscheidender Schritt): Die Elimination macht im Schritt $k$ die Einträge unter der Diagonalen der Spalte $k$ zu null. Jede der $n - k$ Zeilen darunter braucht eine Division für ihren Faktor und $n - k$ Multiplikationen für ihre restlichen Einträge:

$$\sum_{k=1}^{n-1} (n - k)(n - k + 1) = \frac{n^3 - n}{3}$$

**Schritt 5**: Die rechte Seite mitzuführen und von unten nach oben einzusetzen kostet zusammen $n^2$ Operationen:

$$N_\mathrm{Elim}(n) = \frac{n^3 - n}{3} + n^2$$

**Ergebnis:**

$$N_\mathrm{Entw}(n) \approx 1{,}72\cdot n!, \qquad N_\mathrm{Elim}(n) = \frac{n^3 - n}{3} + n^2$$

**Woher die Faktoren kommen:** Das $n!$ stammt aus der Rekursion, die bei jedem Schritt mit der Zahl der Zeilen multipliziert; das $n^3/3$ aus der Summe der Quadrate $1^2 + 2^2 + \cdots$, mit der die bearbeitete Restmatrix schrumpft.

**Proben:** Zwei Unbekannte: Die Cramersche Regel braucht 3 · 2 + 2, also 8 Operationen, drei Determinanten mit je zwei Multiplikationen und zwei Divisionen. Die Elimination braucht 2 + 4, also 6: eine Division für den Faktor $a_{21}/a_{11}$, je eine Multiplikation für den neuen Eintrag an der Stelle (2, 2) und für $b_2$, eine Division für $x_2$ sowie eine Multiplikation und eine Division für $x_1$. Zwanzig Unbekannte: 8,8·10¹⁹ gegen 3060.

**Grenzen:** In dünn besetzten Matrizen sinken beide Zahlen stark; die Elimination profitiert mehr, wenn man die Reihenfolge der Zeilen und Spalten so wählt, dass wenige neue Einträge ungleich null entstehen. Für numerische Genauigkeit tauscht man außerdem Zeilen so, dass durch große Einträge geteilt wird.
:::

### Die Inverse und die transponierte Matrix

*Wie erhält man die Lösung für jede rechte Seite auf einmal?*

Löst man das System für die rechte Seite, die nur in Zeile μ eine 1 hat, erhält man die Spalte μ der __Inversen__ $\mathbf A^{-1}$, der Matrix, deren Produkt mit $\mathbf A$ die __Einheitsmatrix__ ergibt, die Matrix mit Einsen auf der Diagonalen und sonst Nullen. Bei der Leitwertmatrix enthält diese Spalte die Knotenspannungen, die ein Strom von 1 A in den Knoten μ erzeugt. Nach der Cramerschen Regel ist jeder Eintrag der Inversen eine Unterdeterminante mit Schachbrettvorzeichen, geteilt durch die Determinante; man nennt $(-1)^{\mu+\nu}\det\mathbf A^{(\mu\nu)}$ den __Kofaktor__ zum Platz (μ, ν) und die an der Diagonalen gespiegelte Matrix der Kofaktoren die __Adjunkte__ adj $\mathbf A$.

:::formel Satz
$$(\mathbf A^{-1})_{\nu\mu} = \frac{(-1)^{\mu+\nu}\,\det\mathbf A^{(\mu\nu)}}{\det\mathbf A}, \qquad \mathbf A^{-1} = \frac{\mathrm{adj}\,\mathbf A}{\det\mathbf A}$$
:::

**So liest man das:** Der Eintrag in Zeile ν und Spalte μ der Inversen gehört zum Kofaktor des gespiegelten Platzes (μ, ν). Für zwei Zeilen vertauscht man die Diagonaleinträge und ändert das Vorzeichen der beiden anderen; bei drei Zeilen ist jeder der neun Einträge eine Unterdeterminante mit zwei Zeilen.

$$\begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}^{-1} = \frac{1}{a_{11}a_{22} - a_{12}a_{21}}\begin{pmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{pmatrix}$$

Beim Transponieren, dem Spiegeln an der Diagonalen, bleibt die Determinante gleich:

$$\det\mathbf A^\mathsf{T} = \det\mathbf A$$

Ein System mit der transponierten Matrix löst man deshalb mit den Determinanten von $\mathbf A$ selbst: Im Zähler für $x_\nu$ steht $\mathbf A$, in der die Zeile ν durch die rechte Seite ersetzt ist.

**Kurz gesagt:** Transponieren ändert die Determinante nicht; ist sie nicht null, ist die Inverse die gespiegelte Matrix der Kofaktoren, geteilt durch die Determinante.

Idee der Herleitung: Man wendet die Cramersche Regel auf die rechten Seiten mit einer einzigen 1 an und entwickelt den Zähler nach der ersetzten Spalte.

:::herleitung
**Ausgangspunkt:** die Cramersche Regel und der Entwicklungssatz (oben).

**Annahmen:** (i) $\det\mathbf A$ ist nicht null. (ii) __$\vec e_\mu$__ ist die Spalte mit einer 1 in Zeile μ und sonst Nullen.

**Schritt 1**: Spalte μ der Inversen ist die Lösung für die rechte Seite $\vec e_\mu$, denn $\mathbf A$ mal dieser Spalte ergibt die Spalte μ der Einheitsmatrix. Nach Cramer ist ihr Eintrag ν:

$$(\mathbf A^{-1})_{\nu\mu} = \frac{\det\mathbf A_\nu}{\det\mathbf A} \quad \text{mit } \vec e_\mu \text{ in Spalte } \nu$$

**Schritt 2** (entscheidender Schritt): Die ersetzte Spalte enthält nur die 1 in Zeile μ. Entwickelt nach dieser Spalte, bleibt ein Summand: die 1 mit dem Vorzeichen $(-1)^{\mu+\nu}$ und der Unterdeterminante ohne Zeile μ und Spalte ν, die in $\mathbf A$ und $\mathbf A_\nu$ dieselbe ist:

$$\det\mathbf A_\nu = (-1)^{\mu+\nu}\,\det\mathbf A^{(\mu\nu)}$$

**Schritt 3**: Zwei Zeilen: Die Unterdeterminanten sind die einzelnen Einträge; mit den Vorzeichen ergibt sich die Formel mit vertauschter Diagonale und negierten Nebeneinträgen.

**Schritt 4**: Transponierte. Nach der Leibniz-Formel aus der Herleitung des Entwicklungssatzes ist die Determinante die Summe der $n!$ Produkte mit genau einem Eintrag aus jeder Zeile und jeder Spalte. Transponieren vertauscht nur die Rollen von Zeilen und Spalten: Es entstehen dieselben Produkte, und jedes behält sein Vorzeichen, weil eine Anordnung und ihre Umkehrung gleich viele Vertauschungen brauchen. Auf derselben Gleichbehandlung von Zeilen und Spalten beruht die Entwicklung nach Spalten; für die erste Spalte lautet die Gleichheit, mit demselben Argument für die kleineren Streichungsmatrizen:

$$\begin{aligned} \det\mathbf A^\mathsf{T} &= \sum_{\nu=1}^{n} (-1)^{1+\nu}\,a_{\nu 1}\,\det\big(\mathbf A^{(\nu 1)}\big)^\mathsf{T} \\ &= \sum_{\nu=1}^{n} (-1)^{\nu+1}\,a_{\nu 1}\,\det\mathbf A^{(\nu 1)} = \det\mathbf A \end{aligned}$$

**Schritt 5**: Transponiertes System. Ersetzt man in $\mathbf A^\mathsf{T}$ die Spalte ν durch die rechte Seite, ist das die transponierte Matrix von $\mathbf A$ mit ersetzter Zeile ν; nach Schritt 4 haben beide dieselbe Determinante.

**Ergebnis:**

$$(\mathbf A^{-1})_{\nu\mu} = \frac{(-1)^{\mu+\nu}\,\det\mathbf A^{(\mu\nu)}}{\det\mathbf A}, \qquad \det\mathbf A^\mathsf{T} = \det\mathbf A$$

**Woher die Faktoren kommen:** Die Vertauschung der Indizes stammt daraus, dass die Spalte μ der Inversen zur rechten Seite $\vec e_\mu$ gehört, also zur Zeile μ von $\mathbf A$; die Unterdeterminante entfernt genau diese Zeile.

**Proben:** Tiefpass: Die Inverse aus der Adjunkte stimmt mit dem Ergebnis der Knotenanalyse überein (Beispiel unten). Verstärkerstufe: Adjunkte in mS² mit den Zeilen (0,43; 0; 0), (−1; 0,2025; 0,1025), (0,2; 0,0025; 0,0225); ihre erste Spalte, geteilt durch 0,043 mS³, gibt die Knotenspannungen je µA in das Gate, 10, −23,26 und 4,65 mV. Die Determinante der transponierten Leitwertmatrix ist ebenfalls 0,043 mS³.

**Grenzen:** Ohne Determinante ungleich null gibt es keine Inverse; für große Matrizen berechnet man auch die Inverse durch Elimination.
:::

::::beispiel Inverse der Leitwertmatrix des RC-Tiefpasses
**Gegeben:** die Leitwertmatrix des RC-Tiefpasses mit umgewandelter Quelle in mS, Zeilen und Spalten für die Knoten 2 und 3: (2 + j; −1) und (−1; 1 + j), bei ω = 10⁴ 1/s.

**Gesucht:** die Inverse und ihre Bedeutung.

**Rechnung:** Determinante und Adjunkte:

$$\det\mathbf Y = (2 + j)(1 + j) - 1 = 3j\ \mathrm{mS^2}, \qquad \mathrm{adj}\,\mathbf Y = \begin{pmatrix} 1 + j & 1 \\ 1 & 2 + j \end{pmatrix}\ \mathrm{mS}$$

Geteilt durch die Determinante, mit 1/(3j) gleich −j/3:

$$\mathbf Y^{-1} = \frac{1}{3}\begin{pmatrix} 1 - j & -j \\ -j & 1 - 2j \end{pmatrix}\ \mathrm{k\Omega}$$

**Ergebnis:** **Die Inverse hat die Einträge (1 − j)/3 kΩ, −j/3 kΩ, −j/3 kΩ und (1 − 2j)/3 kΩ.**

**Einordnung:** Die erste Spalte enthält die Knotenspannungen bei 1 mA in Knoten 2: (1 − j)/3 V und −j/3 V, genau die Lösung der Knotenanalyse. Die beiden Nebeneinträge sind gleich, −j·333 Ω: Ein Strom in Knoten 2 erzeugt an Knoten 3 dieselbe Spannung wie derselbe Strom in Knoten 3 an Knoten 2, die Reziprozität eines Netzes aus Widerständen und Kondensatoren.
::::

## Die modifizierte Knotenanalyse

*Warum lässt sich eine ideale Spannungsquelle nicht in die Leitwertmatrix eintragen, und wie nimmt man sie trotzdem auf?*

Im RC-Tiefpass liegt die Quelle von 1 V zwischen Knoten 1 und Masse. Welchen Strom sie liefert, 0,745 mA bei +26,6°, bestimmen $R_1$, $C_1$, $R_2$ und $C_2$; ändert man $R_2$, ändert sich der Strom, die Spannung bleibt 1 V. Ein Eintragsmuster der Knotenanalyse setzt aber voraus, dass der Strom eines Elements ein festes Vielfaches von Potentialen ist. Für die ideale Spannungsquelle gibt es kein solches Vielfaches, denn bei ihrer Spannung lässt sie jeden Strom zu (Abbildung 6, links). Auch die Umwandlung in eine Stromquelle scheitert: Ohne Innenwiderstand wäre deren Strom unendlich.

Dasselbe Hindernis haben alle Elemente, deren Admittanz unendlich wäre: ein Widerstand von null Ohm, wie ihn ein Strommesser oder eine Drahtbrücke darstellt, und eine Spule bei Gleichstrom, deren Impedanz $j\omega L$ bei ω gleich null verschwindet. Ebenso gesteuerte Spannungsquellen und der ideale Operationsverstärker: Sie legen eine Spannung fest, ihr Strom folgt aus der übrigen Schaltung.

:::grafik
Szene: st1/netzwerkanalyse/03-mna-spannungsquelle · Vorlage: schaltbild-matrix
**Abbildung 6:** Links die Kennlinien eines Leitwerts von 1 mS, eine Gerade durch den Ursprung, und einer idealen Spannungsquelle von 1 V, eine Linie bei 1 V, die jeden Strom zulässt. Mitte eine ideale Spannungsquelle zwischen den Knoten a (Pluspol) und b an einem übrigen Netz, Strompfeil von a in die Quelle hinein. Rechts die Leitwertmatrix als grauer Block, ergänzt um eine Spalte für den Quellenstrom mit +1 in Zeile a und −1 in Zeile b und um eine Zeile mit +1 in Spalte a, −1 in Spalte b und der Quellenspannung rechts. Der Strom der Quelle wird zur Unbekannten und bekommt eine Spalte, ihre Zweiggleichung wird zur neuen Zeile.
:::

**Die Akteure:**

- __$\underline I_z$__: __Zusatzstrom__, ein Strom, der als zusätzliche Unbekannte geführt wird, weil er sich aus den übrigen Unbekannten nicht ergibt; gezählt von a durch das Element nach b, bei einer Spannungsquelle also in ihren Pluspol hinein; in A.
- __$\underline U_q$__: Quellenspannung, Pluspol an a; in V; 1 V im Tiefpass.
- __$m$__: Zahl der Zusatzströme; 1 im Tiefpass.
- __$\mathbf M$__: Matrix der __modifizierten Knotenanalyse__ mit $n_K + m$ Zeilen und Spalten: oben links die Leitwertmatrix, rechts daneben eine Spalte je Zusatzstrom, darunter eine Zeile je Zweiggleichung.

**Das Zusammenspiel:**

**Schritt 1**: Man nimmt den Strom des Elements als zusätzliche Unbekannte $\underline I_z$ auf und setzt ihn hinter die Knotenpotentiale.

**Schritt 2**: In den Knotengleichungen ist $\underline I_z$ ein abfließender Strom bei a und ein zufließender bei b. In seiner Spalte steht deshalb +1 in Zeile a und −1 in Zeile b, wie bei jedem Strom, der von a nach b gezählt wird.

**Schritt 3**: Eine neue Unbekannte braucht eine neue Gleichung. Das ist die Zweiggleichung des Elements, bei der idealen Spannungsquelle die Vorgabe, dass das Potential von a um $\underline U_q$ über dem von b liegt; sie wird zur neuen Zeile:

$$\underline U_a - \underline U_b = \underline U_q$$

**Schritt 4**: Unbekannte und Gleichungen wachsen um dieselbe Zahl; das System bleibt quadratisch und wird gelöst wie jedes andere, etwa mit der Cramerschen Regel. Der Strom der Quelle ist danach Teil der Lösung.

:::formel Formel
$$\begin{array}{c|ccc|c} & a & b & \underline I_z & \text{rechts} \\ \hline a & & & +1 & \\ b & & & -1 & \\ \text{Zweig} & +1 & -1 & 0 & \underline U_q \end{array}$$
:::

**So liest man das:** Die Spalte von $\underline I_z$ bucht den Strom der Quelle in die Knotengleichungen von a und b, die neue Zeile ist die Zweiggleichung mit der Quellenspannung rechts. In der Ecke steht null, weil die Spannung einer idealen Quelle nicht von ihrem Strom abhängt. Liegt b am Bezugsknoten, entfallen dort Zeile und Spalte. Bei unabhängigen Spannungsquellen ist die Zusatzzeile das Spiegelbild der Zusatzspalte; eine symmetrische Leitwertmatrix bleibt deshalb symmetrisch, und das ist eine bequeme Probe.

**Kurz gesagt:** Für jeden Zusatzstrom kommt genau eine Zeile hinzu, die Zweiggleichung seines Elements; das System bleibt deshalb quadratisch.

:::fehlvorstellung
„Der Zusatzstrom ist der Strom, den die Quelle in die Schaltung liefert.“ Das liegt nahe, weil man bei einer Quelle an den abgegebenen Strom denkt und viele Schaltbilder den Pfeil aus dem Pluspol heraus zeichnen. Gezählt wird aber wie bei Admittanzen und gesteuerten Quellen von a durch das Element nach b, also in den Pluspol hinein. Im RC-Tiefpass ergibt sich deshalb −(0,667 + 0,333j) mA; abgegeben werden +(0,667 + 0,333j) mA, 0,745 mA bei +26,6°. Schaltungssimulatoren zählen ebenso und zeigen für eine Versorgungsquelle, die Strom liefert, einen negativen Strom an.
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
**Gegeben:** RC-Tiefpass wie in Abbildung 1: ideale Quelle $\underline U_q$ = 1 V zwischen Knoten 1 und Masse, $R_1$ = $R_2$ = 1 kΩ, $C_1$ = $C_2$ = 100 nF, ω = 10⁴ 1/s, also $j\omega C$ = j·1 mS.

**Gesucht:** das System der modifizierten Knotenanalyse, die Ausgangsspannung $\underline U_3$ und der Strom der Quelle.

**Rechnung:** In mS, kΩ, V und mA, Unbekannte $\underline U_1$, $\underline U_2$, $\underline U_3$ und $\underline I_z$:

$$\begin{pmatrix} 1 & -1 & 0 & 1 \\ -1 & 2 + j & -1 & 0 \\ 0 & -1 & 1 + j & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} \underline U_1 \\ \underline U_2 \\ \underline U_3 \\ \underline I_z \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}$$

Determinante nach der Quellenzeile, die nur in Spalte 1 eine 1 hat; die Streichungsmatrix wird nach ihrer letzten Spalte entwickelt:

$$\begin{aligned} \det\mathbf M &= (-1)^{4+1}\cdot\det\begin{pmatrix} -1 & 0 & 1 \\ 2 + j & -1 & 0 \\ -1 & 1 + j & 0 \end{pmatrix} \\ &= -\big[(2 + j)(1 + j) - 1\big] = -3j \end{aligned}$$

Für $\underline U_3$ ersetzt die rechte Seite Spalte 3; entwickelt nach dieser Spalte, deren einzige 1 unten steht, bleibt eine Unterdeterminante mit dem Wert 1:

$$\det\mathbf M_3 = (-1)^{4+3}\cdot\det\begin{pmatrix} 1 & -1 & 1 \\ -1 & 2 + j & 0 \\ 0 & -1 & 0 \end{pmatrix} = -1, \qquad \underline U_3 = \frac{-1}{-3j}\ \mathrm V = -\frac{j}{3}\ \mathrm V$$

Ebenso für den Strom der Quelle, Spalte 4 ersetzt:

$$\det\mathbf M_4 = \det\begin{pmatrix} 1 & -1 & 0 \\ -1 & 2 + j & -1 \\ 0 & -1 & 1 + j \end{pmatrix} = 3j - (1 + j) = -1 + 2j$$

$$\underline I_z = \frac{-1 + 2j}{-3j}\ \mathrm{mA} = -\frac{2 + j}{3}\ \mathrm{mA} = -(0{,}667 + 0{,}333\,j)\ \mathrm{mA}$$

**Ergebnis:** **$\underline U_3$ = −j/3 V, ein Drittel der Amplitude, 90° nacheilend; die Quelle gibt 0,745 mA bei +26,6° ab.**

**Einordnung:** Dieselben Zahlen liefern Maschen- und Knotenanalyse, hier aber ohne die Quelle umzuwandeln, und der Quellenstrom fällt als Teil der Lösung mit an. Die Matrix ist symmetrisch, wie in jedem Netz aus Widerständen, Kondensatoren, Spulen und unabhängigen Quellen; gesteuerte Quellen machen sie im Allgemeinen unsymmetrisch. Probe über die Leistung: Die Quelle gibt im Mittel 0,333 mW ab, $R_1$ nimmt 0,278 mW auf, $R_2$ 0,056 mW, die Kondensatoren im Mittel nichts.

**Variation:** Fasst man Quelle und $R_1$ zu einem Tor zusammen (Abschnitt *Impedanzen und reale Quellen*), entfallen Knoten 1 und eine Unbekannte; das System hat drei Zeilen, (1 + j; −1; 1), (−1; 1 + j; 0) und (1; 0; −1), die rechte Seite (0; 0; 1 V), die Determinante ist wieder −3j und die Lösung dieselbe.
::::

:::frage
„Geht es bei einer idealen Spannungsquelle nicht auch ohne zusätzliche Unbekannte?“
Von Hand oft ja. Liegt die Quelle an Masse wie im Tiefpass, ist das Potential ihres Pluspols bekannt, und zwei Gleichungen für die Knoten 2 und 3 genügen statt vier. Liegt sie zwischen zwei anderen Knoten, fasst man beide zu einem __Superknoten__ zusammen: eine gemeinsame Knotengleichung, in der sich der Strom der Quelle heraushebt, dazu ihre Zweiggleichung ([Das Knotenpotentialverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/knotenpotentialverfahren/knotenpotentialverfahren.html)). Das spart die Unbekannte, verlangt aber einen Blick auf die Schaltung und liefert den Quellenstrom nicht; die Eintragsmuster arbeiten ohne Blick, und der Strom, im Tiefpass 0,745 mA, fällt mit an.
:::

## Eintragsmuster weiterer Bauelemente

*Welche Muster haben Impedanzen, reale Spannungsquellen, gesteuerte Quellen und der ideale Operationsverstärker?*

Jedes Element, dessen Strom sich weder aus Potentialen noch aus einem schon geführten Strom ergibt, bekommt dasselbe Gerüst wie die Spannungsquelle: eine Spalte für seinen Strom mit +1 und −1 in den Zeilen seiner Anschlüsse und eine Zeile für seine Zweiggleichung. Die Elemente unterscheiden sich nur darin, was in dieser Zeile steht (Abbildung 7); die stromgesteuerte Stromquelle braucht das Gerüst nicht, weil ihr Strom ein Vielfaches eines geführten Stroms ist.

:::grafik
Szene: st1/netzwerkanalyse/03-eintragsmuster-mna · Vorlage: musterkarten
**Abbildung 7:** Eintragsmuster der modifizierten Knotenanalyse. Impedanz Z: Zusatzspalte +1/−1, Zusatzzeile +1/−1 und −Z in der Ecke, rechts null; der Sonderfall Z gleich null ist ein Kurzschluss oder Strommesser. Tor aus Quelle und Innenimpedanz: wie die Impedanz, rechts die Quellenspannung. Spannungsgesteuerte Spannungsquelle mit dem Faktor v: Zusatzzeile +1, −1 in den Spalten a, b und −v, +v in den Spalten c, d. Stromgesteuerte Stromquelle: ±β in der Spalte des Steuerstroms, keine eigene Zeile. Stromgesteuerte Spannungsquelle: Zusatzzeile mit $-r_m$ in der Spalte des Steuerstroms. Nullor: Zusatzspalte am Ausgang, Zusatzzeile mit +1 und −1 in den Spalten der Eingänge. Alle Elemente, deren Strom sich weder aus den Knotenpotentialen noch aus einem schon geführten Strom ergibt, haben dasselbe Gerüst: eine Spalte für ihren Strom und eine Zeile für ihre Zweiggleichung.
:::

### Impedanzen und reale Quellen

*Wie trägt man ein Element ein, dessen Impedanz null werden kann?*

Führt man den Strom einer Impedanz $\underline Z$ zwischen a und b als Unbekannte, lautet ihre Zweiggleichung: Potential von a minus Potential von b gleich $\underline Z$ mal Strom. Eine reale Spannungsquelle, eine ideale Spannungsquelle in Reihe mit einer Impedanz, verbindet beides; man nennt eine solche Anschlussstelle, über die eine Schaltung angeregt oder gemessen wird, ein __Tor__.

**Die Akteure:**

- __$\underline Z$__: Impedanz des Zweigs, $R$, $j\omega L$ oder $1/(j\omega C)$, beim Tor die Innenimpedanz; in Ω; null ist erlaubt.
- __$\underline U_q$__: Quellenspannung des Tors, Pluspol zur Seite von a; null bei einer reinen Impedanz.

:::formel Formel
$$\underline U_a - \underline U_b - \underline Z\,\underline I_z = \underline U_q$$
:::

**So liest man das:** In der Zusatzzeile stehen +1 und −1 in den Spalten von a und b und $-\underline Z$ in der Spalte des eigenen Stroms, rechts $\underline U_q$. Mit $\underline Z$ gleich null ist das die ideale Spannungsquelle, mit $\underline U_q$ gleich null eine Impedanz, mit beiden gleich null ein Kurzschluss, dessen Strom die Lösung mitliefert. Weil $\underline Z$ in der Matrix steht und nicht sein Kehrwert, bleiben ein Widerstand von null Ohm und eine Spule bei Gleichstrom endliche Einträge. Die Signalquelle der Verstärkerstufe lässt sich so samt Innenwiderstand als Tor eintragen, ohne sie umzuwandeln: Mit $\underline U_G$, $\underline U_D$, $\underline U_S$ und ihrem Strom hat die Matrix vier Zeilen und die Determinante −0,43 mS², der Drain liegt wieder bei −23,26 mV, und der Strom der Quelle ist null, weil das Gate keinen Strom aufnimmt.

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
Es kommt öfter vor, als man denkt. Ein __Strommesser__ ist ein Zweig mit null Ohm, dessen Strom man wissen will; eine Spannungsquelle von 0 V tut dasselbe und ändert keine Spannung der Schaltung. Eine Spule hat bei Gleichstrom die Impedanz null, und bei der Berechnung eines Arbeitspunkts ist jede Spule ein solcher Kurzschluss. In der Leitwertmatrix stünde dort ein unendlicher Leitwert; im Muster der Impedanz steht in der Ecke nur −Z, also null, und die Zeile verlangt gleiche Potentiale an beiden Enden. Im Schwingkreis unten fließt so bei Gleichstrom der ganze Quellenstrom von 1 mA durch die Spule.
:::

:::grafik
Szene: st1/netzwerkanalyse/03-schwingkreis · Vorlage: schaltbild-kurve
**Abbildung 8:** (a) Stromquelle 1 mA in Knoten 1, parallel dazu C = 100 nF und L = 100 mH gegen Masse. (b) Oben die Determinante der Matrix mit dem Spulenstrom als Unbekannter, ω²LC − 1, über ω von 0 bis 2·10⁴ 1/s: −1 bei Gleichstrom, −0,75 bei 5000 1/s, null bei 10⁴ 1/s, 3 bei 2·10⁴ 1/s. Unten der Betrag der Spannung am Knoten: 0 bei Gleichstrom, 0,667 V bei 5000 und bei 2·10⁴ 1/s, unbegrenzt bei 10⁴ 1/s. Mit der Spule als Impedanz bleibt die Determinante bei Gleichstrom endlich; bei der Resonanzfrequenz wird sie null, und die verlustlose Schaltung hat keine eindeutige Lösung.
:::

::::beispiel Schwingkreis bei Gleichstrom und bei 5000 1/s
**Gegeben:** Stromquelle $\underline I_q$ = 1 mA in Knoten 1; parallel $C$ = 100 nF und $L$ = 100 mH gegen Masse (Abbildung 8); Kreisfrequenzen 0 und 5000 1/s.

**Gesucht:** Spannung am Knoten und Strom der Spule, mit der Spule als Impedanz eingetragen.

**Rechnung:** In mS, kΩ, V und mA, Unbekannte $\underline U_1$ und $\underline I_L$; Knotengleichung und Zweiggleichung der Spule:

$$\begin{pmatrix} j\omega C & 1 \\ 1 & -j\omega L \end{pmatrix}\begin{pmatrix} \underline U_1 \\ \underline I_L \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \qquad \det\mathbf M = \omega^2 LC - 1$$

Gleichstrom: Die Matrix enthält nur die beiden Einsen, die Determinante ist −1:

$$\underline U_1 = \frac{\det\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}}{-1} = 0, \qquad \underline I_L = \frac{\det\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}}{-1}\ \mathrm{mA} = 1\ \mathrm{mA}$$

Bei 5000 1/s sind $j\omega C$ = j·0,5 mS und $j\omega L$ = j·0,5 kΩ, die Determinante ist 0,25 − 1, also −0,75:

$$\underline U_1 = \frac{-j\cdot 0{,}5}{-0{,}75}\ \mathrm V = j\cdot 0{,}667\ \mathrm V, \qquad \underline I_L = \frac{-1}{-0{,}75}\ \mathrm{mA} = 1{,}333\ \mathrm{mA}$$

**Ergebnis:** **Bei Gleichstrom 0 V und 1 mA durch die Spule; bei 5000 1/s j·0,667 V und 1,333 mA durch die Spule.**

**Einordnung:** Bei Gleichstrom ist die Spule ein Kurzschluss und trägt den ganzen Strom; in der reinen Knotenanalyse stünde dort ein unendlicher Leitwert, schon bei ω = 1 1/s wären es 10 S. Bei 5000 1/s führt die Spule mehr Strom, als die Quelle liefert: Der Kondensator führt −0,333 mA, und beide zusammen ergeben 1 mA. Bei 10⁴ 1/s wird die Determinante null; dort heben sich die Ströme von Spule und Kondensator für jede Spannung auf.
::::

:::frage
„Was bedeutet es, wenn die Determinante null wird?“
Das Gleichungssystem hat dann keine oder unendlich viele Lösungen: Die Schaltung legt ihre Spannungen und Ströme nicht eindeutig fest. Hinter einer verschwindenden Determinante steckt fast immer ein idealisiertes Element. Zwei ideale Spannungsquellen von 1 V und 2 V parallel widersprechen sich, es gibt keine Lösung; zwei von je 1 V lassen offen, wie sie sich den Strom teilen. Der verlustlose Schwingkreis bei 10⁴ 1/s hätte bei jeder Spannung die Stromsumme null und kann den Quellenstrom nicht aufnehmen; seine Spannung würde nach dem Einschalten ohne Grenze wachsen. In einer realen Schaltung sorgen Verluste und Innenwiderstände dafür, dass die Determinante von null verschieden bleibt.
:::

### Gesteuerte Spannungsquellen und stromgesteuerte Quellen

*Wie werden Quellen eingetragen, die von einer Spannung oder einem Strom an anderer Stelle abhängen?*

Eine __spannungsgesteuerte Spannungsquelle__ legt die Spannung zwischen a und b auf das v-Fache der Spannung zwischen c und d fest; ihr Strom stellt sich nach der übrigen Schaltung ein. Sie bekommt deshalb einen Zusatzstrom, und ihre Zweiggleichung wird zur Zeile. Ein Operationsverstärker mit endlicher Verstärkung wird oft so beschrieben.

**Die Akteure:**

- __$v$__: Spannungsverstärkung der gesteuerten Spannungsquelle, ohne Einheit.
- __$\underline I_\mathrm{St}$__: __Steuerstrom__ einer stromgesteuerten Quelle, der Strom eines anderen Zweigs; in A.
- __$\beta$__: Stromverstärkung der stromgesteuerten Stromquelle, ohne Einheit; __$r_m$__: Transimpedanz der stromgesteuerten Spannungsquelle, in Ω.

:::formel Formel
$$\underline U_a - \underline U_b - v\,(\underline U_c - \underline U_d) = 0$$
:::

**So liest man das:** In der Zusatzzeile stehen +1 und −1 in den Spalten a und b, −v und +v in den Spalten c und d; die rechte Seite ist null, weil die Quelle keine eigene Spannung vorgibt. Diese Zeile ist nicht das Spiegelbild ihrer Spalte, die Matrix wird unsymmetrisch wie bei der gesteuerten Stromquelle. Hat die Quelle eine Innenimpedanz, kommt wie beim Tor $-\underline Z$ in die Ecke.

:::grafik
Szene: st1/netzwerkanalyse/03-strommesser-transitfrequenz · Vorlage: schaltbild-kurve
**Abbildung 9:** (a) Kleinsignal-Ersatzschaltbild eines Transistors mit Stromquelle in das Gate, $C_{gs}$ = 100 fF, gestrichelt $C_{gd}$ = 20 fF, gesteuerter Quelle 1 mS und $g_o$ = 25 µS am Drain und einer Spannungsquelle von 0 V als Strommesser zwischen Drain und Masse. (b) Betrag der Stromverstärkung über der Frequenz von 10 MHz bis 10 GHz, beide Achsen logarithmisch: 159 bei 10 MHz, 15,9 bei 100 MHz, 1 bei 1,59 GHz; gestrichelt die Kurve mit $C_{gd}$: 133 bei 10 MHz, 1 bei 1,345 GHz, oberhalb einiger GHz flacher, 0,213 bei 10 GHz, gegen 0,167 strebend. Die Spannungsquelle von 0 V schließt den Ausgang kurz, wie es die Definition der Transitfrequenz verlangt, und liefert den Kurzschlussstrom als Unbekannte; ohne $C_{gd}$ fällt die Stromverstärkung mit 1/f und erreicht 1 bei der Transitfrequenz.
:::

Eine stromgesteuerte Quelle braucht ihren Steuerstrom als Unbekannte. Ist er noch keine, schaltet man in den Zweig, dessen Strom steuert, eine Spannungsquelle von 0 V in Reihe; sie ändert keine Spannung und keinen Strom, und ihr Zusatzstrom ist genau der Steuerstrom. Ein Strommesser ist dasselbe; in Abbildung 9a liegt er zwischen Drain und Masse und schließt dort zugleich den Ausgang kurz. Die __stromgesteuerte Stromquelle__, deren Strom $\beta\,\underline I_\mathrm{St}$ von a nach b fließt, trägt dann +β in Zeile a und −β in Zeile b ein, in der Spalte des Steuerstroms; eine eigene Zeile braucht sie nicht, denn ihr Strom ist durch eine vorhandene Unbekannte schon festgelegt. Die __stromgesteuerte Spannungsquelle__ bekommt einen eigenen Zusatzstrom und die Zeile:

$$\underline U_a - \underline U_b - r_m\,\underline I_\mathrm{St} = 0$$

**Kurz gesagt:** Eine gesteuerte Spannungsquelle bringt eine Zeile und eine Spalte mit; eine stromgesteuerte Stromquelle bringt nur Einträge in der Spalte ihres Steuerstroms, sofern dieser schon eine Unbekannte ist, sonst zusätzlich die Zeile und Spalte einer Spannungsquelle von 0 V, die ihn führt.

Idee der Herleitung: Man schreibt die Zweiggleichung jeder Quelle so, dass alle Unbekannten links stehen, und bucht ihren Strom wie jeden anderen in die Knotengleichungen.

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

Idee der Herleitung: Man macht den Steuerstrom zur Unbekannten einer 0-V-Quelle und bucht den gesteuerten Strom bzw. die gesteuerte Spannung in Abhängigkeit von dieser Unbekannten.

:::herleitung
**Ausgangspunkt:** die Definitionen der stromgesteuerten Quellen, Strom $\beta\,\underline I_\mathrm{St}$ bzw. Spannung $r_m\,\underline I_\mathrm{St}$, und das Muster des Tors.

**Annahmen:** (i) Der Steuerstrom ist Zusatzstrom eines Elements, nötigenfalls einer Spannungsquelle von 0 V in Reihe mit dem steuernden Zweig. (ii) Zählrichtungen von a nach b.

**Schritt 1**: Eine Quelle von 0 V ist ein Tor mit $\underline Z$ und $\underline U_q$ gleich null: Ihre Zeile verlangt gleiche Potentiale an beiden Enden, sie ändert also keine Spannung, und ihr Zusatzstrom ist der Strom des Zweigs.

**Schritt 2**: Stromgesteuerte Stromquelle. Ihr Strom $\beta\,\underline I_\mathrm{St}$ fließt in Zeile a ab und in Zeile b zu; er ist ein festes Vielfaches einer Unbekannten:

$$\text{Zeile } a: \ +\beta\,\underline I_\mathrm{St}$$

$$\text{Zeile } b: \ -\beta\,\underline I_\mathrm{St}$$

**Schritt 3** (entscheidender Schritt): Weil dieser Strom durch eine vorhandene Unbekannte festgelegt ist, entsteht keine neue Unbekannte und keine neue Zeile.

**Schritt 4**: Stromgesteuerte Spannungsquelle. Ihre Spannung ist vorgegeben, ihr Strom nicht; sie bekommt einen Zusatzstrom und die Zweiggleichung mit allen Unbekannten links:

$$\underline U_a - \underline U_b - r_m\,\underline I_\mathrm{St} = 0$$

**Ergebnis:** stromgesteuerte Stromquelle: ±β in der Spalte des Steuerstroms; stromgesteuerte Spannungsquelle: Zusatzspalte ±1 und Zusatzzeile mit +1, −1 und $-r_m$ in der Spalte des Steuerstroms.

**Woher die Faktoren kommen:** β und $r_m$ stehen in der Spalte des Steuerstroms, weil er die steuernde Unbekannte ist, genau wie g in den Spalten der Steuerpotentiale steht.

**Proben:** Ein Strom von 1 µA durch 1 kΩ steuert eine stromgesteuerte Spannungsquelle mit 5 kΩ: An ihrem Ausgang liegen 5 mV. Steuert er stattdessen eine stromgesteuerte Stromquelle mit β gleich 100, deren Strom vom Lastknoten durch die Quelle nach Masse gezählt wird und an der eine Last von 10 kΩ gegen Masse liegt, zieht sie 100 µA aus der Last, und an der Last liegen −1 V.

**Grenzen:** Hängt der Steuerstrom von der gesteuerten Quelle selbst ab, bleibt das Muster richtig, das System kann dann aber singulär werden.
:::

::::beispiel Stromverstärkung und Transitfrequenz mit einem Strommesser
**Gegeben:** Kleinsignal-Ersatzschaltbild eines Transistors (Abbildung 9): Stromquelle $\underline I_\mathrm{ein}$ in das Gate, Gate-Source-Kapazität $C_{gs}$ = 100 fF zwischen Gate und Masse, gesteuerte Stromquelle $g_m$ = 1 mS vom Drain nach Masse, Ausgangsleitwert $g_o$ = 25 µS; zwischen Drain und Masse eine Spannungsquelle von 0 V als Strommesser.

**Gesucht:** die Stromverstärkung $\underline I_\mathrm{aus}/\underline I_\mathrm{ein}$ bei kurzgeschlossenem Ausgang und die Frequenz, bei der ihr Betrag 1 ist, die __Transitfrequenz__.

**Rechnung:** Unbekannte $\underline U_G$, $\underline U_D$ und der Strom $\underline I_\mathrm{aus}$ des Strommessers; dessen Zeile verlangt $\underline U_D$ gleich null:

$$\begin{pmatrix} j\omega C_{gs} & 0 & 0 \\ g_m & g_o & 1 \\ 0 & 1 & 0 \end{pmatrix}\begin{pmatrix} \underline U_G \\ \underline U_D \\ \underline I_\mathrm{aus} \end{pmatrix} = \begin{pmatrix} \underline I_\mathrm{ein} \\ 0 \\ 0 \end{pmatrix}$$

Entwickelt nach der Zeile des Strommessers:

$$\det\mathbf M = -j\omega C_{gs}$$

$$\det\mathbf M_3 = -\det\begin{pmatrix} j\omega C_{gs} & \underline I_\mathrm{ein} \\ g_m & 0 \end{pmatrix} = g_m\,\underline I_\mathrm{ein}$$

$$\frac{\underline I_\mathrm{aus}}{\underline I_\mathrm{ein}} = \frac{g_m}{-j\omega C_{gs}} = j\,\frac{g_m}{\omega C_{gs}}$$

Betrag 1 bei:

$$\omega_T = \frac{g_m}{C_{gs}} = \frac{10^{-3}\ \mathrm S}{10^{-13}\ \mathrm F} = 10^{10}\ \tfrac{1}{\mathrm s}, \qquad f_T = \frac{\omega_T}{2\pi} = 1{,}59\ \mathrm{GHz}$$

**Ergebnis:** **Der Betrag der Stromverstärkung ist 15,9 bei 100 MHz bei einem Winkel von +90° und fällt umgekehrt proportional zur Frequenz; Transitfrequenz 1,59 GHz.**

**Einordnung:** Der Strommesser hält den Drain auf 0 V, deshalb führt $g_o$ keinen Strom, und der gemessene Strom ist der Strom der gesteuerten Quelle mit umgekehrtem Vorzeichen: Was die Quelle aus dem Drain zieht, liefert der Strommesser aus der Masse nach. Eine Last, die das Ergebnis verfälschen könnte, gibt es nicht. Oberhalb von $f_T$ verstärkt der Transistor den Strom nicht mehr; die Frequenz kennzeichnet, wie schnell ein Transistor ist.

**Variation:** Mit einer Gate-Drain-Kapazität von 20 fF liegt diese am Gate parallel zu $C_{gs}$, weil der Strommesser den Drain auf 0 V hält, und der Strommesser führt außer dem gesteuerten Strom auch ihren Strom; die Stromverstärkung lautet dann

$$\frac{\underline I_\mathrm{aus}}{\underline I_\mathrm{ein}} = -\frac{g_m - j\omega C_{gd}}{j\omega\,(C_{gs} + C_{gd})}$$

und ihr Betrag erreicht 1 bei 1,345 GHz; die übliche Abschätzung mit $g_m$ geteilt durch $2\pi(C_{gs} + C_{gd})$ ergibt 1,326 GHz, 1,4 % weniger.
::::

### Der ideale Operationsverstärker als Nullor

*Wie trägt man einen Verstärker mit unendlicher Verstärkung ein?*

Ein Operationsverstärker ist eine spannungsgesteuerte Spannungsquelle mit sehr großem Faktor, der __Leerlaufverstärkung__ $v_D$, beim Typ 741 typisch 200 000 ([Der ideale OPV und die Rückkopplung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/idealer-opv-und-rueckkopplung.html)). Im invertierenden Verstärker mit 10 kΩ und 100 kΩ und 0,1 V am Eingang liegen damit nur 5 µV zwischen den Eingängen, bei einer Million noch 1 µV. Im Grenzfall unendlicher Verstärkung bleibt von der Zweiggleichung nur die Bedingung, dass die Spannung zwischen den Eingängen null ist; der Ausgang liefert dabei jeden Strom, den die Schaltung verlangt. Das Modell setzt voraus, dass die Schaltung __gegengekoppelt__ ist: Der Ausgang wirkt, hier über $R_2$, so auf den Minuseingang zurück, dass er eine Abweichung zwischen den Eingängen verkleinert; nur dann stellt sich die Lösung der Gleichungen tatsächlich ein.

Dieses Grenzmodell heißt __Nullor__. Er besteht aus einem __Nullator__ zwischen den Eingängen, der Spannung null und Strom null zugleich erzwingt, und einem __Norator__ zwischen Ausgang und Masse, dessen Spannung und Strom beliebig sind und sich aus der übrigen Schaltung ergeben (Abbildung 10). Für das Eintragen heißt das: Der Nullator liefert eine Gleichung, aber keinen Strom, der Norator einen Strom, aber keine Gleichung.

:::grafik
Szene: st1/netzwerkanalyse/03-nullor-verstaerker · Vorlage: schaltbild-matrix
**Abbildung 10:** (a) Invertierender Verstärker: Quelle 0,1 V mit $R_1$ = 10 kΩ am Minuseingang (Knoten 1), $R_2$ = 100 kΩ zum Ausgang A, Pluseingang an Masse; der Verstärker als Nullor, Nullator zwischen den Eingängen, Norator zwischen Ausgang und Masse. (b) Die Matrix mit den Spalten $U_1$, $U_A$, $I_E$, $I_A$ in mS, kΩ, V und mA: (0,01; −0,01; 1; 0), (−0,01; 0,01; 0; 1), (1; 0; −10; 0) mit 0,1 V rechts, (−1; 0; 0; 0); die Nullator-Zeile orange, die Norator-Spalte grün; darunter Determinante −0,1, Ausgang −1 V. Ein Nullor bringt eine Zeile für die Bedingung an seinem Eingang und eine Spalte für den Strom an seinem Ausgang mit; die Ausgangsspannung ergibt sich aus der übrigen Schaltung.
:::

:::formel Formel
$$\underline U_c - \underline U_d = 0$$
:::

**So liest man das:** Die Zusatzzeile hat +1 in der Spalte des Pluseingangs c und −1 in der des Minuseingangs d und keinen Eintrag in der Spalte des Zusatzstroms; diese Spalte gehört zum Norator, mit +1 in der Zeile des Ausgangs a und −1 in der seines Bezugs b. Zeile und Spalte gehören damit zu verschiedenen Anschlusspaaren, die Zeile zum Eingang, die Spalte zum Ausgang. Weil in die Eingänge kein Strom fließt, erscheint der Nullator in keiner Knotengleichung.

**Kurz gesagt:** Ein Nullor hält die Spannung an seinem Eingang auf null, ohne dort Strom aufzunehmen, und liefert an seinem Ausgang jeden Strom und jede Spannung, die die Schaltung verlangt.

:::fehlvorstellung
„Die Zusatzzeile des Nullors legt die Ausgangsspannung des Verstärkers fest.“ Das liegt nahe, weil bei der gesteuerten Spannungsquelle die Ausgangsspannung in ihrer Zeile steht und der Nullor deren Grenzfall ist. Im Grenzfall verschwindet aber gerade dieser Teil: Teilt man die Zeile durch v und lässt v wachsen, bleibt nur die Eingangsbedingung. Die Ausgangsspannung bestimmt die übrige Schaltung; im invertierenden Verstärker folgt sie aus der Knotengleichung am Minuseingang zu −1 V, weil der Strom von 10 µA durch $R_1$ auch durch $R_2$ fließen muss.
:::

:::frage
„Ist ein Nullor ein echtes Bauteil?“
Nein. Nullator und Norator sind Grenzmodelle: Der Nullator verlangt Spannung null und Strom null zugleich, der Norator lässt jede Spannung und jeden Strom zu; einzeln gibt es keines von beiden. Zusammen beschreiben sie jedes Bauelement mit unendlicher Verstärkung in einer gegengekoppelten Schaltung, den idealen Operationsverstärker, aber auch einen idealen Transistor mit unendlicher Steilheit. Wie gut das Modell trifft, zeigt die endliche Leerlaufverstärkung: Mit 200 000 statt unendlich ändert sich die Verstärkung des Beispiels unten um 0,0055 %.
:::

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
**Gegeben:** Quelle $U_E$ = 0,1 V mit $R_1$ = 10 kΩ als Tor am Minuseingang (Knoten 1), $R_2$ = 100 kΩ zwischen Knoten 1 und dem Ausgang A, Pluseingang an Masse, idealer Operationsverstärker als Nullor (Abbildung 10).

**Gesucht:** Ausgangsspannung, Verstärkung und die Ströme.

**Rechnung:** In mS, kΩ, V und mA, Unbekannte $U_1$, $U_A$, Torstrom $I_E$ von Knoten 1 in das Tor und Norator-Strom $I_A$ vom Ausgang in den Norator; Zeilen: Knoten 1, Ausgang, Tor, Nullator mit c an Masse und d an Knoten 1:

$$\begin{pmatrix} 0{,}01 & -0{,}01 & 1 & 0 \\ -0{,}01 & 0{,}01 & 0 & 1 \\ 1 & 0 & -10 & 0 \\ -1 & 0 & 0 & 0 \end{pmatrix}\begin{pmatrix} U_1 \\ U_A \\ I_E \\ I_A \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0{,}1 \\ 0 \end{pmatrix}$$

Entwickelt nach der Nullator-Zeile, dann nach der Spalte des Norator-Stroms:

$$\begin{aligned} \det\mathbf M &= (-1)^{4+1}\cdot(-1)\cdot\det\begin{pmatrix} -0{,}01 & 1 & 0 \\ 0{,}01 & 0 & 1 \\ 0 & -10 & 0 \end{pmatrix} \\ &= -\det\begin{pmatrix} -0{,}01 & 1 \\ 0 & -10 \end{pmatrix} = -0{,}1 \end{aligned}$$

Zähler für $U_A$, Spalte 2 durch die rechte Seite ersetzt, auf dieselbe Weise entwickelt:

$$\det\mathbf M_2 = \det\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0{,}1 & -10 & 0 \end{pmatrix} = 0{,}1, \qquad U_A = \frac{0{,}1}{-0{,}1}\ \mathrm V = -1\ \mathrm V$$

Aus der Nullator-Zeile ist $U_1$ null, aus der Torzeile und der Ausgangszeile folgen die Ströme:

$$I_E = \frac{U_1 - U_E}{R_1} = -10\ \mu\mathrm A, \qquad I_A = -0{,}01\ \mathrm{mS}\cdot(U_A - U_1) = 10\ \mu\mathrm A$$

**Ergebnis:** **Ausgang −1 V, Verstärkung −10; die Quelle gibt 10 µA ab, die durch $R_1$ und $R_2$ in den Ausgang fließen.**

**Einordnung:** Die Verstärkung ist −$R_2/R_1$, wie mit den goldenen Regeln des idealen Verstärkers ([Die OPV-Grundschaltungen](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/operationsverstarker/opv-grundschaltungen.html)), hier aber ohne Überlegung aus den Mustern. Der Minuseingang liegt auf 0 V, ohne mit der Masse verbunden zu sein; das ist die virtuelle Masse.

**Variation:** Mit der gesteuerten Spannungsquelle statt des Nullors lautet die vierte Zeile ($v_D$; 1; 0; 0) mit der Null rechts. Bei $v_D$ = 200 000 ergibt sich die Verstärkung −9,99945 und am Minuseingang 5 µV, bei 1000 noch −9,891 und 989 µV.
::::

## Was die Determinante über den Frequenzgang verrät

*Warum haben alle Spannungen einer Schaltung dieselben Eckfrequenzen?*

Die Verstärkerstufe mit Source an Masse, also ohne Source-Widerstand, bekommt nun die Kapazitäten, die bei hohen Frequenzen mitwirken: 100 fF zwischen Gate und Source und eine Last von 10 pF am Drain, etwa der Eingang der nächsten Stufe oder eines Tastkopfs (Abbildung 11). Am Gate liegen die Signalquelle mit 0,1 mS und $C_{gs}$ parallel. Bei tiefen Frequenzen liegen dort die vollen 10 mV. Bei 10⁹ 1/s ist der Leitwert des Kondensators, $\omega C_{gs}$, so groß wie die 0,1 mS der Quelle, die Amplitude ist auf das 1/√2-Fache gesunken, 7,07 mV, und darüber fällt sie umgekehrt proportional zur Frequenz, weil der Kondensator den Strom der Quelle immer mehr übernimmt.

:::grafik
Szene: st1/netzwerkanalyse/03-bode · Vorlage: bode
**Abbildung 11:** (a) Verstärkerstufe ohne Source-Widerstand mit Signalquelle 1 µA parallel zu 0,1 mS, $C_{gs}$ = 100 fF am Gate, gesteuerter Quelle 1 mS, 0,225 mS und $C_L$ = 10 pF am Drain. (b) Bode-Diagramm von 100 kHz bis 10 GHz: oben der Betrag der Drainspannung je Signalspannung in dB, 12,96 dB bei tiefen Frequenzen, Knick bei 3,58 MHz, −20 dB je Dekade bis 159 MHz, danach −40 dB je Dekade; dazu die Gatespannung mit nur einem Knick bei 159 MHz; unten der Winkel, 180° bei tiefen Frequenzen, 133,7° bei 3,58 MHz, gegen 0° bei hohen. Die Eckfrequenzen gehören zu den Polen, den Nullstellen der Determinante; oberhalb jeder fällt der Betrag um weitere 20 dB pro Dekade.
:::

Steht im Nenner einer __Übertragungsfunktion__, des Verhältnisses einer Ausgangs- zu einer Eingangsgröße als Funktion der Frequenz, ein Faktor $1 + j\omega/\omega_p$, so heißt $\omega_p$ seine __Eckkreisfrequenz__ und $\omega_p/(2\pi)$ seine Eckfrequenz. Ersetzt man $j\omega$ durch eine beliebige komplexe Zahl $s$, die __komplexe Frequenz__, wird der Faktor bei $s$ gleich $-\omega_p$ null; diese Stelle heißt __Pol__ der Übertragungsfunktion. Beträge gibt man dabei in __Dezibel__ an, als 20 lg des Betrags, lg für den Zehnerlogarithmus: Ein Faktor 10 sind 20 dB, ein Faktor 1/√2 sind −3,01 dB. Das __Bode-Diagramm__ zeigt den Betrag in dB und den Winkel über der Frequenz auf einer logarithmischen Achse, auf der jede __Dekade__, ein Faktor 10 in der Frequenz, gleich lang ist.

**Die Akteure:**

- __$C_{gs}$__: Gate-Source-Kapazität, 100 fF; __$C_L$__: Lastkapazität am Drain, 10 pF.
- __$G_\mathrm{sig}$__, __$\underline I_\mathrm{sig}$__: Innenleitwert und Quellenstrom der umgewandelten Signalquelle, 0,1 mS und 1 µA bei der Signalspannung __$\underline U_\mathrm{sig}$__ = 10 mV.
- __$\omega_G$__, __$\omega_D$__: Eckkreisfrequenzen des Gate- und des Drainknotens; in 1/s.

**Das Zusammenspiel:** Nach der Cramerschen Regel ist jede Knotenspannung ein Quotient mit der Determinante im Nenner, und dieser Nenner ist für alle Knoten derselbe. Mit Kondensatoren ist jeder Eintrag der Leitwertmatrix eine Summe aus einem Leitwert und einem Vielfachen von $j\omega$, die Determinante also ein Polynom in $j\omega$. Spulen trägt man dafür wie im Abschnitt *Impedanzen und reale Quellen* mit ihrem Strom als Unbekannter ein; dann steht $j\omega L$ in der Matrix und nicht sein Kehrwert, und die Einträge bleiben Polynome. In der Stufe ohne Source-Widerstand steht über der Diagonalen eine Null, denn kein Bauelement führt vom Drain zum Gate zurück; die Determinante ist das Produkt der beiden Diagonaleinträge:

$$\det\mathbf Y = (G_\mathrm{sig} + j\omega C_{gs})\,(G_D + G_L + g_o + j\omega C_L)$$

Die Drainspannung hat beide Faktoren im Nenner. In der Gatespannung kürzt sich der zweite, weil er auch in ihrem Zähler steht: Ein Pol zeigt sich in allen Spannungen, deren Zähler ihn nicht aufhebt.

:::formel Formel
$$\frac{\underline U_D}{\underline U_\mathrm{sig}} = -\frac{g_m}{G_D + G_L + g_o}\cdot\frac{1}{(1 + j\omega/\omega_G)\,(1 + j\omega/\omega_D)}$$

$$\omega_G = \frac{G_\mathrm{sig}}{C_{gs}}, \qquad \omega_D = \frac{G_D + G_L + g_o}{C_L}$$
:::

**So liest man das:** Bei tiefen Frequenzen ist das Verhältnis −4,44, also 12,96 dB, wie ohne Kapazitäten. Oberhalb von $\omega_D$, 2,25·10⁷ 1/s oder 3,58 MHz, fällt der Betrag um 20 dB je Dekade, oberhalb von $\omega_G$, 10⁹ 1/s oder 159 MHz, um 40 dB je Dekade. An jeder Eckfrequenz liegt er 3 dB unter den Geraden, und jeder Pol dreht den Winkel dort um 45° und insgesamt um 90°. Je größer die Lastkapazität, desto tiefer liegt $\omega_D$.

**Kurz gesagt:** Alle Knotenspannungen einer Schaltung haben die Determinante als gemeinsamen Nenner; sind alle Einträge der Matrix Polynome in der komplexen Frequenz, ist jeder Pol einer Knotenspannung eine Nullstelle dieser einen Determinante. Weit oberhalb seiner Eckfrequenz senkt jeder reelle Pol den Betrag um weitere 20 dB je Dekade.

Idee der Herleitung: Man rechnet die Knotenspannungen der dreieckigen Matrix mit der Cramerschen Regel aus, klammert die Leitwerte aus und wertet einen einzelnen Pol für kleine und große Frequenzen aus.

:::herleitung
**Ausgangspunkt:** die Cramersche Regel und die Leitwertmatrix der Stufe mit Source an Masse; die Signalquelle ist als Stromquelle $\underline I_\mathrm{sig}$, gleich $G_\mathrm{sig}\,\underline U_\mathrm{sig}$, mit dem Leitwert $G_\mathrm{sig}$ eingetragen.

**Annahmen:** (i) Die Source liegt an Masse. (ii) Zwischen Gate und Drain liegt kein Bauelement, insbesondere keine Kapazität. (iii) Eingeschwungener Zustand mit einer Kreisfrequenz ω.

**Schritt 1**: Leitwertmatrix mit den Zeilen und Spalten G und D:

$$\mathbf Y = \begin{pmatrix} G_\mathrm{sig} + j\omega C_{gs} & 0 \\ g_m & G_D + G_L + g_o + j\omega C_L \end{pmatrix}$$

**Schritt 2**: Die Determinante einer Matrix mit einer Null über der Diagonalen ist das Produkt der Diagonaleinträge, denn der zweite Summand der Formel für zwei Zeilen enthält die Null.

**Schritt 3**: Zähler nach Cramer, rechte Seite $(\underline I_\mathrm{sig}; 0)$:

$$\det\mathbf Y_D = -g_m\,\underline I_\mathrm{sig}, \qquad \det\mathbf Y_G = \underline I_\mathrm{sig}\,(G_D + G_L + g_o + j\omega C_L)$$

**Schritt 4** (entscheidender Schritt): Im Quotienten für das Gate kürzt sich der Drainfaktor. Für den Drain klammert man in jedem Faktor den Leitwert aus und setzt $\underline I_\mathrm{sig}$ gleich $G_\mathrm{sig}\,\underline U_\mathrm{sig}$:

$$\frac{\underline U_D}{\underline U_\mathrm{sig}} = \frac{-g_m\,G_\mathrm{sig}}{G_\mathrm{sig}\,(1 + j\omega/\omega_G)\,(G_D + G_L + g_o)\,(1 + j\omega/\omega_D)}$$

**Schritt 5**: Ein einzelner Pol in Dezibel und sein Winkel:

$$20\lg\left|\frac{1}{1 + j\omega/\omega_p}\right| = -10\lg\Big(1 + \frac{\omega^2}{\omega_p^2}\Big), \qquad \varphi = -\arctan\frac{\omega}{\omega_p}$$

Weit unterhalb von $\omega_p$ ist das null; bei $\omega_p$ sind es −10 lg 2, also −3,01 dB und −45°; weit oberhalb ist es −20 lg(ω/ω_p), also −20 dB je Dekade, und der Winkel nähert sich −90°.

**Ergebnis:**

$$\frac{\underline U_D}{\underline U_\mathrm{sig}} = -\frac{g_m}{G_D + G_L + g_o}\cdot\frac{1}{(1 + j\omega/\omega_G)\,(1 + j\omega/\omega_D)}$$

**Woher die Faktoren kommen:** Die Verstärkung bei tiefen Frequenzen stammt aus den Leitwerten, jede Eckkreisfrequenz aus dem Verhältnis von Leitwert zu Kapazität an einem Knoten; das Minuszeichen aus der Richtung der gesteuerten Quelle.

**Proben:** Einheit: S durch F ist 1/s. Zahlenwerte: 10⁻⁴ S durch 10⁻¹³ F ergibt 10⁹ 1/s, 2,25·10⁻⁴ S durch 10⁻¹¹ F ergibt 2,25·10⁷ 1/s. Grenzfall tiefe Frequenzen: −1 mS/0,225 mS, also −4,44, der Wert der Stufe ohne Source-Widerstand. Die numerische Lösung des Systems bei 10 MHz ergibt denselben Betrag 1,495 wie die Formel.

**Grenzen:** Mit einer Kapazität zwischen Gate und Drain steht über der Diagonalen keine Null mehr; dann wirkt der Drain auf das Gate zurück, und die Determinante zerfällt nicht mehr in Knotenfaktoren. Dasselbe gilt mit Source-Widerstand (Variation im Beispiel).
:::

::::beispiel Bode-Diagramm der Verstärkerstufe mit Kapazitäten
**Gegeben:** Verstärkerstufe ohne Source-Widerstand (Abbildung 11): $G_\mathrm{sig}$ = 0,1 mS, $C_{gs}$ = 100 fF, $g_m$ = 1 mS, $G_D + G_L + g_o$ = 0,225 mS, $C_L$ = 10 pF.

**Gesucht:** die Eckfrequenzen, Betrag und Winkel bei 10 MHz und die Frequenz, bei der der Betrag 1 ist.

**Rechnung:** Eckfrequenzen:

$$f_D = \frac{2{,}25\cdot 10^{7}\ \tfrac{1}{\mathrm s}}{2\pi} = 3{,}58\ \mathrm{MHz}, \qquad f_G = \frac{10^{9}\ \tfrac{1}{\mathrm s}}{2\pi} = 159\ \mathrm{MHz}$$

Bei 10 MHz sind die Frequenzverhältnisse 10/3,58, also 2,793, und 10/159, also 0,0628:

$$\left|\frac{\underline U_D}{\underline U_\mathrm{sig}}\right| = \frac{4{,}444}{\sqrt{1 + 2{,}793^2}\cdot\sqrt{1 + 0{,}0628^2}} = \frac{4{,}444}{2{,}966\cdot 1{,}002} = 1{,}495$$

$$\begin{aligned} \varphi &= 180^\circ - \arctan 2{,}793 - \arctan 0{,}0628 \\ &= 180^\circ - 70{,}3^\circ - 3{,}6^\circ = 106{,}1^\circ \end{aligned}$$

Den Betrag 1 erreicht die Formel, numerisch gelöst, bei 15,4 MHz.

**Ergebnis:** **Eckfrequenzen 3,58 MHz und 159 MHz; bei 10 MHz Betrag 1,495 (3,50 dB) und Winkel 106,1°; Betrag 1 bei 15,4 MHz.**

**Einordnung:** Verstärkung bei tiefen Frequenzen mal untere Eckfrequenz ergibt 4,444 · 3,58 MHz, also 15,9 MHz. Der Leitwert am Drain steht in der Verstärkung im Nenner und in der Eckfrequenz im Zähler und kürzt sich; das Produkt ist $g_m/(2\pi C_L)$ und hängt von den Widerständen nicht ab. Ein doppelt so großer Leitwert am Drain, $G_D + G_L + g_o$ zusammen, halbiert deshalb die Verstärkung und verdoppelt die Eckfrequenz; verdoppelt man nur $G_L$, sinkt die Verstärkung auf 3,08, die Eckfrequenz steigt auf 5,17 MHz, und das Produkt bleibt 15,9 MHz.

**Variation:** Mit Source-Widerstand von 1 kΩ, $C_{gs}$ zwischen Gate und Source, hat die Leitwertmatrix drei Zeilen und keine Dreiecksform mehr. Ihre Determinante ist ein Polynom zweiten Grades in $j\omega$, dessen Faktoren die Eckfrequenzen 3,38 MHz und 287 MHz haben; die Verstärkung bei tiefen Frequenzen ist −2,33.
::::

:::frage
„Warum heißt diese Stelle Pol, und warum knickt der Betrag gerade bei der Eckfrequenz ab?“
Der Name kommt aus der Funktionentheorie: Wo der Nenner null wird, wächst der Betrag der Übertragungsfunktion über alle Grenzen; über der Ebene der komplexen Frequenz aufgetragen, ragt er dort als Spitze unbegrenzt nach oben, und eine solche Stelle heißt Polstelle. Auf der Achse der wirklichen Frequenzen, wo $s$ gleich $j\omega$ ist, ist der Betrag des Faktors der Abstand von $j\omega$ zum Pol, geteilt durch $\omega_p$: Er bleibt nahe 1, solange ω klein gegen $\omega_p$ ist, und wächst proportional zu ω, sobald ω groß dagegen ist. Der Knick bei $\omega_p$ trennt diese beiden Bereiche. Die Systemtheorie rechnet durchgehend mit dieser komplexen Frequenz.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Eintragsmuster | jedes Bauelement schreibt seinen Beitrag, ohne den Rest der Schaltung zu kennen |
| Bezugsknoten streichen | jeder Strom wird zweimal gebucht, deshalb ist eine Knotengleichung überzählig |
| Cramersche Regel | jede Größe ist ein Quotient zweier Determinanten mit gemeinsamem Nenner |
| ideale Spannungsquelle | ihr Strom wird zur Unbekannten, ihre Zweiggleichung zur Zeile |
| Impedanz, Tor, Spule bei Gleichstrom | dasselbe Gerüst, die Impedanz steht in der Ecke statt ihres Kehrwerts |
| gesteuerte Spannungsquelle, Nullor | Zeile mit den Steuerknoten, Spalte für den Ausgangsstrom |
| Frequenzgang | der gemeinsame Nenner legt die Pole aller Spannungen fest |
| Rechenaufwand | gefüllt wird nach Mustern, gelöst wird großes durch Elimination |

Jedes Bauelement schreibt seinen Beitrag als festes Muster in eine Matrix, ohne den Rest der Schaltung zu kennen; Elemente, deren Strom sich weder aus den Knotenpotentialen noch aus einem schon als Unbekannte geführten Strom ergibt, bringen diesen Strom als zusätzliche Unbekannte und ihre Zweiggleichung als zusätzliche Zeile mit, und das so entstehende quadratische System liefert, wenn es eindeutig lösbar ist, jede Größe als Quotient zweier Determinanten.

## Bedeutung und Ausblick

Schaltungssimulatoren wie SPICE arbeiten genau so. Die Netzliste nennt für jedes Bauelement seine Knoten und Werte, das Programm trägt die Muster ein und löst das dünn besetzte System durch Elimination; die Wechselstromanalyse wiederholt das für jede Frequenz mit komplexen Einträgen. Auch die Arbeitspunktanalyse benutzt dieselben Muster: Jeder Schritt des Newton-Verfahrens ersetzt ein nichtlineares Bauelement durch sein Begleitmodell, einen Leitwert parallel zu einer Stromquelle ([Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html)). Bei der MOS-Diode an einer Stromquelle von 0,5 mA mit 0,25 mS wird sie bei der Schätzung 2 V zum Leitwert 3 mS und zu einer Stromquelle, die 3,75 mA in den Knoten speist; die Muster ergeben 3,25 mS mal Spannung gleich 4,25 mA, also die nächste Schätzung 1,3077 V.

Die Grenzen liegen bei der Linearität und bei idealisierten Elementen. Nichtlineare Bauelemente gehen nur über die Linearisierung ein, und Umläufe aus idealen Spannungsquellen oder verlustlose Resonanzen machen die Determinante null. Stehen Einträge sehr verschiedener Größe nebeneinander, Femtofarad neben Kiloohm, rechnet ein Simulator mit begrenzter Genauigkeit und wählt die Reihenfolge der Elimination entsprechend. Im Zeitbereich ersetzt er Kondensatoren und Spulen in jedem Zeitschritt ebenfalls durch Leitwert und Stromquelle; das ist zusammen mit den Testquellen für Ein- und Ausgangswiderstände das folgende Thema.

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
A: Jede Knotengleichung ist eine Summe über die Ströme aller Bauelemente, und ein Bauelement kommt nur in den Gleichungen der Knoten vor, die sein Strom berührt, mit Faktoren in den Spalten der Potentiale, die ihn bestimmen. Die Beiträge addieren sich deshalb Eintrag für Eintrag.
F: Warum ist in der vollständigen Matrix mit allen Knoten jede Zeilen- und Spaltensumme null?
A: Zeilen: Nur Potentialdifferenzen treiben Ströme, gleiches Anheben aller Potentiale ändert nichts. Spalten: Jeder Strom verlässt einen Knoten und erreicht einen anderen, er steht einmal mit plus und einmal mit minus da. Deshalb ist eine Zeile überzählig, und die vollständige Matrix ist singulär, solange man keinen Bezugsknoten wählt und seine Zeile und Spalte streicht.
F: Stimmt es, dass man beim Eintragen einer Admittanz die wirkliche Stromrichtung kennen muss?
A: Nein. Vertauscht man die Zählrichtung, vertauschen sich a und b, und das Muster bleibt gleich; wie der Strom zur Zählrichtung liegt, zeigt das Vorzeichen der Lösung, etwa −2,33 µA durch $R_D$ der Verstärkerstufe, von D nach Masse gezählt.
F: Warum ist jede Knotenspannung ein Quotient zweier Determinanten mit demselben Nenner?
A: Ersetzt man die Spalte der Unbekannten durch die rechte Seite, zerfällt deren Determinante nach Linearität in Summanden, von denen nur der mit der eigenen Spalte überlebt; er ist die Unbekannte mal der Determinante der Matrix. Der Nenner ist deshalb immer die Determinante der unveränderten Matrix, sofern sie nicht null ist.
F: Warum lässt sich eine ideale Spannungsquelle nicht in die Leitwertmatrix eintragen?
A: Ihr Strom ist kein festes Vielfaches von Potentialen; bei ihrer Spannung lässt sie jeden Strom zu, und eine Umwandlung in eine Stromquelle ergäbe ohne Innenwiderstand einen unendlichen Strom. Die modifizierte Knotenanalyse macht den Strom deshalb zur Unbekannten und die Zweiggleichung zur Zeile.
F: Stimmt es, dass der Zusatzstrom einer Spannungsquelle der Strom ist, den sie abgibt?
A: Nein. Er wird wie bei Admittanzen und gesteuerten Quellen von a durch das Element nach b gezählt, also in den Pluspol hinein. Im RC-Tiefpass ist er −(0,667 + 0,333j) mA; abgegeben werden 0,745 mA bei +26,6°.
F: Wie trägt man eine Spule bei Gleichstrom ein, deren Admittanz unendlich wäre?
A: Mit ihrem Strom als Unbekannter und dem Muster der Impedanz, in dessen Ecke $-j\omega L$ steht; bei ω gleich null ist das null, und die Zeile verlangt gleiche Potentiale an beiden Enden. Im Schwingkreis fließt so der ganze Strom von 1 mA durch die Spule.
F: Stimmt es, dass die Zusatzzeile des Nullors die Ausgangsspannung festlegt?
A: Nein. Die Zeile verlangt gleiche Potentiale an den Eingängen; die Spalte gehört zum Ausgangsstrom. Die Ausgangsspannung folgt aus der übrigen Schaltung, im invertierenden Verstärker −1 V bei 0,1 V am Eingang.
F: Eine Leitwertmatrix hat die Determinante 0,043 mS³, die Matrix mit der Spalte des Drains durch die rechte Seite ersetzt −1 mS²·µA. Wie groß ist die Drainspannung?
A: Nach Cramer −1/0,043 mV, also −23,26 mV.
F: Warum rechnen Schaltungssimulatoren nicht mit der Cramerschen Regel?
A: Determinanten durch Entwicklung kosten rund 1,7·n! Multiplikationen, bei zwanzig Unbekannten 8,8·10¹⁹ für die ganze Regel, gegen 3060 bei der Gauß-Elimination; Simulatoren eliminieren und nutzen die Nullen der dünn besetzten Matrix.
:::

