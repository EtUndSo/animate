---
title: Testquellen und Transientenanalyse linearer Schaltungen
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse
order: 33020400
summary: Wie man Eingangs- und Ausgangsimpedanz, Übertragungsfunktionen und Ersatzzweitore einer Schaltung mit Testquellen bestimmt, ohne die Schaltung zu verändern, und wie ein Simulator ihren zeitlichen Verlauf mit Zeitschritten und Begleitmodellen berechnet. Ausführliche Fassung mit Herleitung der Impedanz als Diagonaleintrag der Inversen, der Übertragung unabhängig von der Anregungsart, des Ersatzzweitors, der Euler-Verfahren mit Fehler und Stabilität, der Begleitmodelle von Kondensator und Spule und der Sprungantwort, durchgerechnet an Verstärkerstufe, RC-Tiefpass, RC- und RL-Glied und MOS-Diode.
tags: Testquelle, Eingangswiderstand, Ausgangswiderstand, Transientenanalyse, Zeitkonstante
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Wer eine Schaltung entworfen hat, muss sie befragen können: Wie stark belastet sie ihre Quelle, wie stark bricht ihr Ausgang unter Last ein, wie viel Signal kommt an, und wie verläuft die Spannung nach dem Einschalten? Eine Messung, die dafür die Schaltung umbaut, etwa den Ausgang kurzschließt, misst eine andere Schaltung. Den zeitlichen Verlauf beschreiben gekoppelte Differentialgleichungen; schon bei wenigen Kondensatoren wird ihre geschlossene Lösung mühsam, bei vielen löst man sie nur noch Schritt für Schritt numerisch. Beides beruht auf einem Prinzip:

**Die Matrix des Gleichungssystems beschreibt die Schaltung, die rechte Seite ihre Anregung: Testquellen fragen die Schaltung ab, ohne die Matrix zu verändern, und in der Zeit bringt das Begleitmodell jedes Kondensators und jeder Spule die Vorgeschichte als Stromquelle auf die rechte Seite, sodass jeder Zeitschritt wieder ein lineares Gleichungssystem ist.**

Vorausgesetzt werden das Rechnen mit [Zeigern](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html), die modifizierte Knotenanalyse mit Cramerscher Regel und Inverse aus [Netzwerkgleichungen systematisch aufstellen: modifizierte Knotenanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/modifizierte-knotenanalyse-ausfuehrlich.html), die Ersatzquelle aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html), Arbeitspunkt und Newton-Verfahren aus [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html) und das [Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html). Darauf bauen die Vierpole auf, Schaltungen mit zwei Anschlusspaaren, die man durch vier Kenngrößen beschreibt, und so rechnen Schaltungssimulatoren wie SPICE.

:::grafik
Szene: st1/netzwerkanalyse/04-uebersicht · Vorlage: schaltbild-matrix
**Abbildung 1:** (a) Eine Schaltung mit einer Testspannungsquelle am Eingang, Knoten 1, und einer Teststromquelle am Ausgang, Knoten 2; darunter ihr Gleichungssystem: eine feste Matrix und drei rechte Seiten, Lauf A mit 1 V am Eingang und Teststrom null für Eingangsadmittanz und Übertragung, Lauf B mit 0 V am Eingang und 1 A Teststrom für die Ausgangsimpedanz, dazu der Betrieb mit dem Signal. (b) Ein Kondensator im Zeitschritt h als Leitwert C/h parallel zu einer Stromquelle, die die Spannung des vorigen Schritts fortschreibt; darunter die Zeitachse mit den Schritten t₀, t₁, t₂, t₃. Testquellen und Zeitschritte mit fester Schrittweite ändern nur die rechte Seite des Gleichungssystems; die Schaltung bleibt dieselbe.
:::

## Teststromquellen: die Impedanz an einem Knoten

*Wie bestimmt man die Impedanz, die man in einen Knoten hineinsieht, ohne die Schaltung zu verändern?*

Als Beispiel dient wieder die Verstärkerstufe aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html), eine Source-Schaltung mit der Steilheit $g_m$ = 1 mS, dem Ausgangsleitwert $g_o$ = 25 µS, $R_D$ = 10 kΩ, $R_S$ = 1 kΩ und einer Signalquelle mit 10 kΩ Innenwiderstand am Gate. Gerechnet wird mit ihrem __Kleinsignal-Ersatzschaltbild__, dem linearen Modell für kleine Änderungen um den Arbeitspunkt. Am Drain hängt im Betrieb eine Last. Wie stark deren Spannung einbricht, bestimmt die Impedanz, die man vom Lastanschluss aus in den Drain hineinsieht. Man misst sie, indem man in den Drain einen bekannten Strom einspeist und die Spannung abliest, die er dort hervorruft: Ein Mikroampere erzeugt 8,90 mV, die Impedanz ist 8,90 kΩ, genau die Innenimpedanz der Ersatzquelle, die die Stufe nach dem Artikel über Ersatzquellen am Drain darstellt. Eingespeist wird mit einer __Teststromquelle__, einer idealen Stromquelle, die nur dazu dient, die Schaltung abzufragen (Abbildung 2).

:::grafik
Szene: st1/netzwerkanalyse/04-teststrom-ausgang · Vorlage: schaltbild-matrix
**Abbildung 2:** (a) Kleinsignal-Ersatzschaltbild der Verstärkerstufe ohne Last: Signalquelle abgeschaltet, ihr Innenleitwert 0,1 mS bleibt am Gate; gesteuerte Quelle 1 mS, $g_o$ = 25 µS, $R_D$ = 10 kΩ, $R_S$ = 1 kΩ; eine Teststromquelle speist 1 µA vom Bezugsknoten in den Drain. (b) Das Gleichungssystem in mS, mV und µA: Leitwertmatrix mit den Zeilen (0,1; 0; 0), (1; 0,125; −1,025), (−1; −0,025; 2,025), rechte Seite (0; 1; 0); die Lösung (0; 8,90; 0,110) mV ist die Spalte D der Inversen, der Matrix, die das System für jede rechte Seite löst; Determinante 0,02275 mS³, Unterdeterminante 0,2025 mS². (c) Im Simulator mit 1 A: 8901 V, zahlenmäßig die Impedanz in Ω. Eine Teststromquelle erscheint nur auf der rechten Seite; die Antwort auf den Teststrom ist eine Spalte der Inversen, ihr Diagonaleintrag die Impedanz.
:::

**Die Akteure:**

- __$\underline I_T$__: __Teststrom__, von einer idealen Stromquelle vom Bezugsknoten in den Knoten μ eingespeist, ein Zeiger; in A; 1 µA im Beispiel, in Simulatoren meist 1 A.
- __μ__: der Knoten, in den der Teststrom fließt; __κ__: ein beliebiger Knoten, an dem man die Antwort abliest.
- __$\underline Z_\mu$__: die Impedanz, die man zwischen Knoten μ und Bezugsknoten in die Schaltung hineinsieht; in Ω. Ist μ ein Eingang, heißt sie __Eingangsimpedanz__, ist μ ein Ausgang, __Ausgangsimpedanz__; 8,90 kΩ am Drain der Stufe.
- __$\mathbf Y^{-1}$__: die __Inverse__ der Leitwertmatrix $\mathbf Y$, die Matrix, deren Produkt mit $\mathbf Y$ die Einheitsmatrix ergibt; sie löst das System für jede rechte Seite auf einmal. Ihre Einträge haben die Einheit Ω.
- __$\vec e_\mu$__: die Spalte mit einer 1 in Zeile μ und sonst Nullen.

**Das Zusammenspiel:**

**Schritt 1**: Die Matrix des Gleichungssystems beschreibt die Schaltung; jedes Bauelement trägt dort sein Muster ein. Auf der rechten Seite stehen nur die unabhängigen Quellen, also Quellen, deren Wert nicht von Spannungen oder Strömen der Schaltung abhängt.

**Schritt 2**: Eine ideale Stromquelle vom Bezugsknoten in den Knoten μ liefert ihren Strom unabhängig von jedem Potential, ihr Innenleitwert ist null. Sie trägt deshalb nichts in die Matrix ein und erscheint nur mit $+\underline I_T$ in Zeile μ der rechten Seite.

**Schritt 3**: Mit dem Wert null fällt auch dieser Eintrag weg, und die Gleichungen sind genau die der Schaltung ohne die Quelle. Eine abgeschaltete Stromquelle ist ein __Leerlauf__, eine offene Verbindung, durch die kein Strom fließt; sie kann deshalb in jedem Betriebsfall angeschlossen bleiben.

**Schritt 4**: Alle übrigen unabhängigen Quellen schaltet man ab, indem man ihre Einträge auf der rechten Seite null setzt: Eine Stromquelle wird zum Leerlauf, eine Spannungsquelle mit 0 V zum __Kurzschluss__, denn ihre Zeile verlangt dann gleiche Potentiale an beiden Anschlüssen. Gesteuerte Quellen bleiben aktiv, denn sie gehören zur Matrix. Die Matrix ändert sich dabei nicht.

**Schritt 5**: Die Lösung ist $\mathbf Y^{-1}\,\vec e_\mu\,\underline I_T$, also die Spalte μ der Inversen, mal den Teststrom. Ihr Eintrag in Zeile μ, geteilt durch den Teststrom, ist die gesuchte Impedanz.

:::formel Formel
$$\underline Z_\mu = \frac{\underline U_\mu}{\underline I_T} = \big(\mathbf Y^{-1}\big)_{\mu\mu} = \frac{\det\mathbf Y^{(\mu\mu)}}{\det\mathbf Y}$$
:::

**So liest man das:** Die Impedanz an einem Knoten ist der Diagonaleintrag der Inversen. Nach der Cramerschen Regel ist er die Unterdeterminante ohne Zeile und Spalte μ, geteilt durch die Determinante; $\mathbf Y^{(\mu\mu)}$ ist die Streichungsmatrix aus dem Artikel über die modifizierte Knotenanalyse. Die übrigen Einträge derselben Spalte, $(\mathbf Y^{-1})_{\kappa\mu}$, geben die Spannung an Knoten κ je Ampere in Knoten μ an und heißen __Übertragungsimpedanzen__. Mit der modifizierten Knotenanalyse gilt dasselbe für deren Matrix.

**Kurz gesagt:** Die Antwort auf einen Teststrom von 1 A in den Knoten μ ist die Spalte μ der inversen Matrix, und die in den Knoten hineingesehene Impedanz ist ihr Diagonaleintrag.

Liegt die Teststromquelle zwischen zwei Knoten a und b, etwa an einem Tor ohne Verbindung zur Masse, steht ihr Strom mit plus in Zeile a und minus in Zeile b der rechten Seite. Die Impedanz zwischen a und b ist dann die Differenz der beiden Potentiale je Ampere, gebildet aus den Spalten a und b der Inversen.

Idee der Herleitung: Man setzt die rechte Seite mit dem Teststrom ein, löst mit der Cramerschen Regel und entwickelt den Zähler nach der ersetzten Spalte.

:::herleitung
**Ausgangspunkt:** die Knotengleichungen $\mathbf Y\,\underline{\vec U} = \underline{\vec I}_q$ mit den Knotenpotentialen $\underline{\vec U}$ und den Quellenströmen $\underline{\vec I}_q$ sowie die Cramersche Regel.

**Annahmen:** (i) Die Schaltung ist linear, im Kleinsignal-Ersatzschaltbild also im Arbeitspunkt linearisiert. (ii) Außer der Teststromquelle sind alle unabhängigen Quellen abgeschaltet. (iii) $\det\mathbf Y$ ist nicht null.

**Schritt 1**: Die Teststromquelle ist die einzige Anregung; die rechte Seite hat nur in Zeile μ einen Eintrag:

$$\underline{\vec I}_q = \underline I_T\,\vec e_\mu$$

**Schritt 2**: Weil die Determinante nicht null ist, existiert die Inverse, und die Lösung ist ihr Produkt mit der rechten Seite. $\mathbf Y^{-1}\vec e_\mu$ greift aus der Inversen die Spalte μ heraus:

$$\underline{\vec U} = \mathbf Y^{-1}\,\underline I_T\,\vec e_\mu$$

**Schritt 3** (entscheidender Schritt): Nach der Cramerschen Regel ist $\underline U_\mu$ der Quotient aus der Determinante der Matrix, deren Spalte μ durch die rechte Seite ersetzt ist, und $\det\mathbf Y$. Die ersetzte Spalte enthält nur $\underline I_T$ in Zeile μ; entwickelt nach dieser Spalte bleibt ein Summand mit dem Vorzeichen $(-1)^{\mu+\mu} = +1$ und der Unterdeterminante ohne Zeile und Spalte μ:

$$\underline U_\mu = \frac{\underline I_T\,\det\mathbf Y^{(\mu\mu)}}{\det\mathbf Y}$$

**Schritt 4**: Geteilt durch den Teststrom:

$$\frac{\underline U_\mu}{\underline I_T} = \frac{\det\mathbf Y^{(\mu\mu)}}{\det\mathbf Y} = \big(\mathbf Y^{-1}\big)_{\mu\mu}$$

**Ergebnis:**

$$\underline Z_\mu = \frac{\underline U_\mu}{\underline I_T} = \big(\mathbf Y^{-1}\big)_{\mu\mu} = \frac{\det\mathbf Y^{(\mu\mu)}}{\det\mathbf Y}$$

**Woher die Faktoren kommen:** Dass nur eine Unterdeterminante übrig bleibt, liegt an der rechten Seite mit einem einzigen Eintrag; das positive Vorzeichen daran, dass der Eintrag auf der Diagonalen steht.

**Proben:** Einheit: Bei $n_K$ Knoten außer dem Bezugsknoten hat die Unterdeterminante $n_K - 1$ Zeilen und die Einheit $\mathrm S^{n_K-1}$, die Determinante $\mathrm S^{n_K}$, der Quotient 1/S, also Ω. Grenzfall: Ein einzelner Knoten mit dem Leitwert $\underline Y$ gegen Masse hat die Gleichung $\underline Y\,\underline U_\mu = \underline I_T$, und die Impedanz ist $1/\underline Y$. Zahlenwert: Verstärkerstufe 0,2025 mS² durch 0,02275 mS³, also 8,90 kΩ.

**Grenzen:** Ist die Determinante null, etwa weil ein Teil der Schaltung keine Verbindung zum Bezugsknoten hat, gibt es keine Inverse, und die Formel ist nicht anwendbar. Hängt Knoten μ selbst frei, findet der Teststrom keinen Rückweg, und die Impedanz ist unendlich.
:::

::::beispiel Ausgangsimpedanz der Verstärkerstufe mit einem Teststrom von 1 µA
**Gegeben:** das Kleinsignal-Ersatzschaltbild der Verstärkerstufe ohne Last; Signalquelle abgeschaltet, ihr Innenleitwert $G_\mathrm{sig}$ = 0,1 mS bleibt am Gate; $g_m$ = 1 mS, $g_o$ = 0,025 mS, $G_D$ = 0,1 mS, $G_S$ = 1 mS; Teststrom 1 µA in den Drain.

**Gesucht:** die Impedanz am Drain.

**Rechnung:** In mS, mV und µA, Zeilen und Spalten G, D, S; die Leitwertmatrix ohne Last und die rechte Seite:

$$\begin{pmatrix} 0{,}1 & 0 & 0 \\ 1 & 0{,}125 & -1{,}025 \\ -1 & -0{,}025 & 2{,}025 \end{pmatrix}\begin{pmatrix} \underline U_G \\ \underline U_D \\ \underline U_S \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$$

Determinante nach Zeile G, Unterdeterminante ohne Zeile und Spalte D:

$$\begin{aligned} \det\mathbf Y &= 0{,}1\cdot(0{,}125\cdot 2{,}025 - 1{,}025\cdot 0{,}025) \\ &= 0{,}1\cdot 0{,}2275 = 0{,}02275\ \mathrm{mS^3} \end{aligned}$$

$$\det\mathbf Y^{(DD)} = 0{,}1\cdot 2{,}025 - 0\cdot(-1) = 0{,}2025\ \mathrm{mS^2}$$

$$\underline Z_D = \frac{0{,}2025}{0{,}02275}\ \mathrm{k\Omega} = 8{,}90\ \mathrm{k\Omega}, \qquad \underline U_D = 8{,}90\ \mathrm{mV}$$

**Ergebnis:** **Die Impedanz am Drain ist 8,90 kΩ; 1 µA erzeugt dort 8,90 mV, an der Source 0,110 mV, am Gate nichts.**

**Einordnung:** Das ist die Innenimpedanz der Ersatzquelle am Drain, dort über Leerlaufspannung und Kurzschlussstrom gewonnen; hier genügt eine einzige rechte Seite. Ein Simulator mit 1 A Teststrom zeigt am Drain 8901 V, zahlenmäßig die Impedanz in Ohm. Das Gate bleibt auf null, weil es keinen Strom aufnimmt und die gesteuerte Quelle nicht auf das Gate zurückwirkt.

**Variation:** Mit der Last von 10 kΩ ergibt dieselbe Rechnung 4,71 kΩ, die Parallelschaltung von 8,90 kΩ und 10 kΩ. Speist man den Teststrom stattdessen ins Gate, liest man 10 kΩ ab, den Innenwiderstand der abgeschalteten Signalquelle; die Stufe selbst nimmt am Gate keinen Strom auf.
::::

:::frage
„Muss der Teststrom 1 A sein, und hält die Schaltung das aus?“
Der Wert ist beliebig, denn das Kleinsignal-Ersatzschaltbild ist linear: Doppelter Teststrom, doppelte Antwort, und der Quotient bleibt. Simulatoren nehmen 1 A, weil dann die Spannung in Volt zahlenmäßig die Impedanz in Ohm ist. Die 8901 V am Drain sind eine Rechengröße des linearisierten Modells, keine Spannung, die an der wirklichen Schaltung auftritt. Misst man an der wirklichen Schaltung, muss der Teststrom klein bleiben gegen die Ströme des Arbeitspunkts, hier also deutlich unter 0,25 mA, damit die Linearisierung gilt.
:::

## Testspannungsquelle am Eingang: Eingangsadmittanz, Übertragung und Ausgangsimpedanz

*Wie bestimmt man, wie stark eine Schaltung ihre Quelle belastet, wie viel Signal am Ausgang ankommt und wie stark der Ausgang unter Last nachgibt?*

Der RC-Tiefpass aus den beiden vorigen Artikeln wird am Knoten 1 von einer idealen Spannungsquelle angesteuert, $R_1$ = $R_2$ = 1 kΩ, $C_1$ = $C_2$ = 100 nF, bei ω = 10⁴ 1/s. Eine Teststromquelle am Knoten 1 würde nichts messen, denn die abgeschaltete Spannungsquelle schließt diesen Knoten kurz. Am Eingang dient deshalb die Spannungsquelle selbst als __Testspannungsquelle__: Sie ist mit ihrem Strom als Zusatzstrom ohnehin Teil der Matrix der modifizierten Knotenanalyse, und ihr Wert steht auf der rechten Seite. Zwei Läufe mit derselben Matrix beantworten alle drei Fragen (Abbildung 3).

:::grafik
Szene: st1/netzwerkanalyse/04-testspannung-eingang · Vorlage: schaltbild-matrix
**Abbildung 3:** (a) RC-Tiefpass mit idealer Spannungsquelle am Knoten 1 als Testspannungsquelle und einer Teststromquelle am Ausgang, Knoten 3; $R_1$ = $R_2$ = 1 kΩ, $C_1$ = $C_2$ = 100 nF, ω = 10⁴ 1/s. (b) Dieselbe Matrix der modifizierten Knotenanalyse mit zwei rechten Seiten: Lauf A mit 1 V an der Quelle und Teststrom null liefert den Eingangsstrom (0,667 + 0,333j) mA und die Ausgangsspannung −j/3 V; Lauf B mit 0 V an der Quelle und 1 mA Teststrom liefert am Ausgang (0,333 − 0,667j) V. (c) Falsch: Quelle entfernt statt kurzgeschlossen, die Ausgangsimpedanz wäre (0,2 − 0,6j) kΩ. Zwei Läufe an derselben Matrix ergeben Eingangsadmittanz, Übertragung und Ausgangsimpedanz; abgeschaltet ist die Spannungsquelle ein Kurzschluss, kein Leerlauf.
:::

**Die Akteure:**

- __$\underline U_q$__: Spannung der Testspannungsquelle am Eingang, Pluspol am Eingangsknoten; 1 V in Lauf A, null in Lauf B.
- __$\underline I_\mathrm{ein}$__: Strom, den die Quelle in den Eingang liefert. Der Zusatzstrom __$\underline I_z$__ der Quelle wird in den Pluspol hinein gezählt; deshalb ist $\underline I_\mathrm{ein}$ gleich $-\underline I_z$.
- __$\underline U_\mathrm{aus}$__: Potential des Ausgangsknotens; im Tiefpass das Potential $\underline U_3$ von Knoten 3.

:::formel Definition
$$\underline Y_\mathrm{ein} = \frac{\underline I_\mathrm{ein}}{\underline U_q}\ \ \text{bei}\ \underline I_T = 0$$

$$\underline A_V = \frac{\underline U_\mathrm{aus}}{\underline U_q}\ \ \text{bei}\ \underline I_T = 0$$

$$\underline Z_\mathrm{aus} = \frac{\underline U_\mathrm{aus}}{\underline I_T}\ \ \text{bei}\ \underline U_q = 0$$
:::

**So liest man das:** Die __Eingangsadmittanz__ $\underline Y_\mathrm{ein}$ ist der Strom, den die Schaltung je Volt aus ihrer Quelle zieht; ihr Kehrwert ist die Eingangsimpedanz. Die __Spannungsübertragungsfunktion__ $\underline A_V$ ist die Ausgangsspannung je Volt am Eingang bei offenem Ausgang, denn der abgeschaltete Teststrom ist ein Leerlauf; bei Verstärkern heißt sie __Leerlaufverstärkung__. Die Ausgangsimpedanz $\underline Z_\mathrm{aus}$ ist die Impedanz am Ausgang bei kurzgeschlossenem Eingang, denn die abgeschaltete Spannungsquelle ist ein Kurzschluss. Man definiert die drei Größen so, weil sie mit genau zwei Läufen ohne Umbau der Schaltung zu gewinnen sind: Lauf A liefert $\underline Y_\mathrm{ein}$ und $\underline A_V$ und zugleich die Übertragung zu jedem inneren Knoten, Lauf B liefert $\underline Z_\mathrm{aus}$.

Weil die Matrix in beiden Läufen dieselbe ist, eliminiert ein Simulator sie nur einmal. Nach der Zählung im Artikel über die modifizierte Knotenanalyse wächst der Aufwand der Elimination mit der dritten Potenz der Zeilenzahl, das Behandeln einer weiteren rechten Seite nur mit der zweiten: Bei tausend Zeilen kostet die Elimination rund 3,3·10⁸ Operationen, jeder zusätzliche Lauf rund 10⁶.

:::frage
„Ist der Strom der Testspannungsquelle nicht der Zusatzstrom aus der Lösung?“
Bis auf das Vorzeichen. Der Zusatzstrom wird vom Anschluss a durch die Quelle zum Anschluss b gezählt, bei einer Spannungsquelle mit dem Pluspol an a also in den Pluspol hinein; im Tiefpass ergibt Lauf A $\underline I_z$ = −(0,667 + 0,333j) mA. Die Quelle liefert also (0,667 + 0,333j) mA in die Schaltung. Wer das Vorzeichen vergisst, erhält einen Eingangsleitwert mit negativem Realteil, −0,667 mS. Ein Netz aus Widerständen und Kondensatoren kann das nicht haben, denn es würde dann im Mittel Leistung an die Quelle abgeben.
:::

::::beispiel Eingangsadmittanz, Übertragung und Ausgangsimpedanz des RC-Tiefpasses
**Gegeben:** RC-Tiefpass mit idealer Quelle an Knoten 1, $R_1$ = $R_2$ = 1 kΩ, $C_1$ = $C_2$ = 100 nF, ω = 10⁴ 1/s, also $j\omega C$ = j·1 mS; Ausgang Knoten 3.

**Gesucht:** $\underline Y_\mathrm{ein}$, $\underline Z_\mathrm{ein}$, $\underline A_V$ und $\underline Z_\mathrm{aus}$.

**Rechnung:** In mS, kΩ, V und mA; Unbekannte $\underline U_1$, $\underline U_2$, $\underline U_3$ und $\underline I_z$; dieselbe Matrix in beiden Läufen, mit der Determinante −3j:

$$\mathbf M = \begin{pmatrix} 1 & -1 & 0 & 1 \\ -1 & 2 + j & -1 & 0 \\ 0 & -1 & 1 + j & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}$$

Lauf A, rechte Seite (0; 0; 0; 1 V), gelöst wie im Artikel über die modifizierte Knotenanalyse:

$$\underline I_z = -\frac{2 + j}{3}\ \mathrm{mA}, \qquad \underline U_3 = -\frac{j}{3}\ \mathrm V$$

$$\underline Y_\mathrm{ein} = \frac{-\underline I_z}{\underline U_q} = \frac{2 + j}{3}\ \mathrm{mS}, \qquad \underline Z_\mathrm{ein} = \frac{3}{2 + j}\ \mathrm{k\Omega} = (1{,}2 - 0{,}6\,j)\ \mathrm{k\Omega}$$

Lauf B, rechte Seite (0; 0; 1 mA; 0). Für $\underline U_3$ ersetzt sie Spalte 3; entwickelt nach dieser Spalte bleibt die Unterdeterminante ohne Zeile und Spalte 3, und diese, entwickelt nach ihrer letzten Zeile (1; 0; 0), ist −(2 + j):

$$\det\mathbf M_3 = \det\begin{pmatrix} 1 & -1 & 1 \\ -1 & 2 + j & 0 \\ 1 & 0 & 0 \end{pmatrix} = -(2 + j)$$

$$\underline U_3 = \frac{-(2 + j)}{-3j}\ \mathrm V = \frac{1 - 2j}{3}\ \mathrm V, \qquad \underline Z_\mathrm{aus} = (0{,}333 - 0{,}667\,j)\ \mathrm{k\Omega}$$

**Ergebnis:** **$\underline Y_\mathrm{ein}$ = (0,667 + 0,333j) mS, also $\underline Z_\mathrm{ein}$ = (1,2 − 0,6j) kΩ, Betrag 1,34 kΩ; $\underline A_V$ = −j/3; $\underline Z_\mathrm{aus}$ = (0,333 − 0,667j) kΩ, Betrag 0,745 kΩ.**

**Einordnung:** Die Quelle sieht mehr als ihre 1 kΩ in Reihe, weil hinter $R_1$ noch der Rest des Netzes liegt; der kapazitive Anteil −0,6j kΩ lässt den Strom der Spannung um 26,6° vorauseilen. Der Ausgang ist kapazitiv, denn bei kurzgeschlossenem Eingang liegt $C_2$ parallel zu $R_2$ und dem Rest. $\underline Z_\mathrm{aus}$ ist zugleich der Eintrag (3, 3) der Inversen der umgewandelten Leitwertmatrix, (1 − 2j)/3 kΩ, im Artikel über die modifizierte Knotenanalyse auf anderem Weg berechnet.
::::

:::fehlvorstellung
„Für die Ausgangsimpedanz nimmt man die Eingangsquelle aus der Schaltung heraus.“ Das liegt nahe, weil „abschalten“ nach „entfernen“ klingt. Eine abgeschaltete Spannungsquelle hat aber 0 V; ihre Zeile verlangt weiter gleiche Potentiale an beiden Anschlüssen, sie ist ein Kurzschluss und bleibt in der Matrix. Wer sie entfernt, lässt Knoten 1 offen, $R_1$ hängt frei, und der Tiefpass hat am Ausgang (0,2 − 0,6j) kΩ statt (0,333 − 0,667j) kΩ, im Betrag 0,632 kΩ statt 0,745 kΩ. Abgeschaltet wird nur der Wert der Quelle; ein Innenwiderstand einer realen Quelle bleibt stehen.
:::

## Übertragung zwischen beliebigen Knoten

*Warum speist man an inneren Knoten einen Strom ein und keine Spannung?*

In der Verstärkerstufe liegt die Source im Arbeitspunkt auf 0,25 V und der Drain auf 2,5 V; durch den Transistor fließen 0,25 mA. Er arbeitet im __Sättigungsbereich__, in dem sein Drainstrom fast nur von der Gate-Source-Spannung abhängt und er wie eine gesteuerte Stromquelle wirkt. Um die Übertragung von der Source zum Drain zu bestimmen, liegt eine Spannungsquelle zwischen Source und Masse nahe, die nur das Signal liefert. Sie hält die Source aber auch für Gleichspannung fest, auf ihren Gleichanteil null. Dann fehlen die 0,25 V an $R_S$, die Gate-Source-Spannung steigt von 1 V auf 1,25 V, und der Transistor würde in Sättigung 0,563 mA führen; das ergäbe an $R_D$ einen Abfall von 5,6 V, mehr als die Versorgung von 5 V. Er geht deshalb in den __Triodenbereich__ über, in dem er wie ein von der Gate-Source-Spannung gesteuerter Widerstand wirkt: Es stellen sich 0,457 mA und am Drain 0,426 V ein, die Steilheit sinkt auf 0,852 mS, und der Ausgangsleitwert steigt von 25 µS auf 0,648 mS, auf das 26-Fache. Das Kleinsignalmodell des Arbeitspunkts gilt nicht mehr (Abbildung 4). Eine Teststromquelle ohne Gleichanteil ist für Gleichstrom dagegen ein Leerlauf, und der Arbeitspunkt bleibt.

:::grafik
Szene: st1/netzwerkanalyse/04-innerer-knoten · Vorlage: schaltbild-vergleich
**Abbildung 4:** Die Verstärkerstufe mit Gleichgrößen, Versorgung 5 V, $R_D$ = 10 kΩ, $R_S$ = 1 kΩ, Gate auf 1,25 V. Links eine Teststromquelle am Source-Knoten, deren Gleichanteil null ist: Arbeitspunkt unverändert, $U_S$ = 0,25 V, $U_D$ = 2,5 V, $I_D$ = 0,25 mA, Steilheit 1 mS, Ausgangsleitwert 25 µS. Rechts eine Spannungsquelle ohne Gleichanteil am selben Knoten: Sie hält die Source auf 0 V, der Transistor geht in den Triodenbereich, $U_D$ = 0,426 V, $I_D$ = 0,457 mA, Steilheit 0,852 mS, Ausgangsleitwert 0,648 mS. Eine Spannungsquelle an einem inneren Knoten legt auch dessen Gleichspannung fest und verschiebt den Arbeitspunkt; eine Stromquelle ohne Gleichanteil ist für Gleichstrom ein Leerlauf.
:::

In den Gleichungen ausgedrückt: Eine Spannungsquelle bringt eine Zeile und eine Spalte mit und verändert die Matrix, also die Schaltung; eine Stromquelle ändert nur die rechte Seite. Ein Simulator bestimmt zuerst den Arbeitspunkt und linearisiert dann die Schaltung um ihn herum, beides an derselben Schaltung. Was für die Kleinsignalrechnung angeschlossen ist, ist deshalb auch bei der Arbeitspunktbestimmung angeschlossen. Am Eingang ist eine Spannungsquelle dagegen richtig, denn dort sitzt im Betrieb ohnehin eine, die das Gate auf seine Vorspannung von 1,25 V legt; als Testspannungsquelle bekommt sie diesen Gleichanteil und dazu das Testsignal.

:::merke
Abgeschaltete Testquellen dürfen die Schaltung nicht verändern: Eine Teststromquelle ist dann ein Leerlauf, eine Testspannungsquelle ein Kurzschluss. Teststromquellen kommen deshalb parallel zu dem Anschlusspaar, dessen Impedanz man sucht, meist zwischen einen Knoten und Masse; Testspannungsquellen nur dorthin, wo ein Kurzschluss nichts ändert, an die Stelle einer vorhandenen Spannungsquelle oder in Reihe in einen Zweig. Zwischen Arbeitspunktbestimmung und Kleinsignalrechnung bleibt die Schaltung dieselbe.
:::

:::analogie
Testquellen folgen derselben Regel wie Messgeräte. Ein ideales Voltmeter ist ein Leerlauf und wird deshalb parallel angeschlossen, ein ideales Amperemeter ist ein Kurzschluss und wird in Reihe geschaltet; nur so verändern beide die Schaltung nicht. Eine abgeschaltete Teststromquelle ist ebenfalls ein Leerlauf und sitzt parallel zwischen Knoten und Masse; eine abgeschaltete Testspannungsquelle ist ein Kurzschluss und gehört dorthin, wo ein Kurzschluss nichts ändert.

| Im Vergleich | In der Schaltung |
|---|---|
| ideales Voltmeter, parallel angeschlossen | Test mit einer Stromquelle zwischen Knoten und Masse |
| ideales Amperemeter, in Reihe geschaltet | Test mit einer Spannungsquelle, ebenso der Strommesser aus einer Quelle von 0 V |
| Rückwirkung des Geräts auf die Schaltung | veränderte Matrix, verschobener Arbeitspunkt |

**Wo der Vergleich nicht stimmt:** Ein Messgerät beobachtet nur; eine eingeschaltete Testquelle regt die Schaltung selbst an. Leerlauf oder Kurzschluss ist sie nur im abgeschalteten Zustand.
:::

Mit der Teststromquelle am Knoten μ liefert ein einziger Lauf alle Knotenpotentiale, und die Übertragung von μ zu einem anderen Knoten κ ist ihr Verhältnis.

**Die Akteure:**

- __$\underline A_{\kappa\mu}$__: Spannungsübertragung von Knoten μ zu Knoten κ, das Potential an κ je Volt an μ; ohne Einheit; −2,33 vom Gate zum Drain der Stufe mit Last.

:::formel Formel
$$\underline A_{\kappa\mu} = \frac{\underline U_\kappa}{\underline U_\mu} = \frac{\big(\mathbf Y^{-1}\big)_{\kappa\mu}}{\big(\mathbf Y^{-1}\big)_{\mu\mu}}$$
:::

**So liest man das:** Die Übertragung ist das Verhältnis zweier Einträge derselben Spalte der Inversen; der Teststrom kürzt sich heraus. Derselbe Lauf liefert zugleich die Impedanz an μ. Im Betrieb wird Knoten μ aber meist nicht von einer Stromquelle angeregt. Die Übertragung ist trotzdem dieselbe, solange die Anregung nur an μ angreift: Die Gleichungen aller übrigen Knoten enthalten dann in beiden Fällen keine Quelle, sind gleich und legen deren Potentiale als feste Vielfache von $\underline U_\mu$ fest.

**Kurz gesagt:** Wird nur Knoten μ angeregt, überträgt sich eine Spannung von μ zu jedem anderen Knoten gleich, ob man μ mit einer Strom- oder einer Spannungsquelle anregt, sofern die Schaltung mit der Stromquelle lösbar ist und die übrigen Potentiale durch $\underline U_\mu$ eindeutig festgelegt sind.

Idee der Herleitung: Man trennt die Gleichung von Knoten μ ab und zeigt, dass die übrigen Gleichungen bei beiden Anregungsarten dieselben sind.

:::herleitung
**Ausgangspunkt:** die Knotengleichungen $\mathbf Y\,\underline{\vec U} = \underline{\vec I}_q$, aufgeteilt in die Zeile μ und die übrigen Zeilen, und die Eintragsmuster von Strom- und Spannungsquelle aus dem Artikel über die modifizierte Knotenanalyse.

**Annahmen:** (i) Die einzige Anregung greift zwischen Knoten μ und dem Bezugsknoten an, als Strom- oder als Spannungsquelle. (ii) Die Streichungsmatrix $\mathbf Y^{(\mu\mu)}$, also $\mathbf Y$ ohne Zeile und Spalte μ, hat eine Determinante ungleich null. (iii) $\det\mathbf Y$ ist nicht null, sodass die Anregung mit dem Teststrom eine Lösung hat.

**Schritt 1**: In jeder Zeile κ ungleich μ steht rechts null, denn dort speist keine Quelle ein. Bringt man den Beitrag des Potentials von μ nach rechts, bleibt mit einem Summationsindex λ über alle Knoten außer μ:

$$\sum_{\lambda \ne \mu} \underline Y_{\kappa\lambda}\,\underline U_\lambda = -\underline Y_{\kappa\mu}\,\underline U_\mu, \qquad \kappa \ne \mu$$

**Schritt 2** (entscheidender Schritt): Diese Zeilen sind bei beiden Anregungsarten dieselben. Eine Stromquelle an μ ändert nur Zeile μ der rechten Seite. Eine Spannungsquelle an μ bringt eine Spalte mit, die nur in Zeile μ einen Eintrag hat, und eine eigene Zeile, die $\underline U_\mu$ festlegt; die Zeilen κ ungleich μ berührt sie nicht.

**Schritt 3**: Die Matrix links ist $\mathbf Y^{(\mu\mu)}$; nach Annahme (ii) ist das System eindeutig lösbar. Weil seine rechte Seite proportional zu $\underline U_\mu$ ist, ist es auch seine Lösung, mit Faktoren, die nur von den Leitwerten abhängen:

$$\underline U_\kappa = \underline A_{\kappa\mu}\,\underline U_\mu, \qquad \kappa \ne \mu$$

**Schritt 4**: Bei Anregung mit dem Teststrom sind beide Potentiale Einträge der Spalte μ der Inversen mal $\underline I_T$, und ihr Quotient ist der Faktor aus Schritt 3:

$$\underline A_{\kappa\mu} = \frac{\big(\mathbf Y^{-1}\big)_{\kappa\mu}\,\underline I_T}{\big(\mathbf Y^{-1}\big)_{\mu\mu}\,\underline I_T} = \frac{\big(\mathbf Y^{-1}\big)_{\kappa\mu}}{\big(\mathbf Y^{-1}\big)_{\mu\mu}}$$

**Ergebnis:**

$$\underline A_{\kappa\mu} = \frac{\underline U_\kappa}{\underline U_\mu} = \frac{\big(\mathbf Y^{-1}\big)_{\kappa\mu}}{\big(\mathbf Y^{-1}\big)_{\mu\mu}}$$

und derselbe Wert gilt bei Anregung mit einer Spannungsquelle an μ.

**Woher die Faktoren kommen:** Die Einträge $\underline Y_{\kappa\mu}$ koppeln Knoten μ an den Rest der Schaltung; wie sich diese Kopplung verteilt, bestimmt allein $\mathbf Y^{(\mu\mu)}$.

**Proben:** Verstärkerstufe mit Last, Teststrom ins Gate: $\underline U_D/\underline U_G$ = −2,326 und $\underline U_S/\underline U_G$ = 0,465; mit der Signalquelle ergeben sich −23,26 mV und 4,65 mV bei 10 mV am Gate, dieselben Verhältnisse. RC-Tiefpass bei kurzgeschlossenem Eingang, Teststrom in Knoten 2: $\underline U_3/\underline U_2$ = (1 − j)/2; bei Anregung mit der Quelle an Knoten 1 ist das Verhältnis (−j/3) zu (1 − j)/3, ebenfalls (1 − j)/2; die Quelle wirkt dabei über $R_1$ wie eine Stromquelle in Knoten 2, die Anregung greift also nur an μ an. Einheit: V durch V.

**Grenzen:** Greift eine zweite Anregung an einem anderen Knoten an, überlagern sich die Antworten, und die Gleichheit gilt nicht mehr. Ist $\det\mathbf Y$ null, etwa wenn Knoten μ und die von ihm abhängenden Knoten keine Verbindung zur Masse haben, findet der Teststrom keinen Rückweg, während eine Spannungsquelle an μ die Potentiale trotzdem festlegt. Ist $\det\mathbf Y^{(\mu\mu)}$ null, etwa wenn die Schaltung mit geerdetem Knoten μ einen verlustlosen Schwingkreis in Resonanz enthält, legt $\underline U_\mu$ die übrigen Potentiale nicht fest.
:::

::::beispiel Übertragungen in der Verstärkerstufe und im Tiefpass mit Teststrom
**Gegeben:** (a) Verstärkerstufe mit der Last von 10 kΩ, Signalquelle abgeschaltet, ihr Innenleitwert 0,1 mS bleibt; Leitwertmatrix in mS mit den Zeilen (0,1; 0; 0), (1; 0,225; −1,025), (−1; −0,025; 2,025); Teststrom 1 µA ins Gate. (b) RC-Tiefpass mit kurzgeschlossenem Eingang, Knoten 2 und 3, Leitwertmatrix in mS mit den Zeilen (2 + j; −1) und (−1; 1 + j); Teststrom 1 mA in Knoten 2.

**Gesucht:** (a) $\underline U_D/\underline U_G$ und $\underline U_S/\underline U_G$; (b) $\underline U_3/\underline U_2$.

**Rechnung:** (a) In mS, mV und µA. Die Gate-Zeile ergibt $\underline U_G$ = 1/0,1 mV = 10 mV. In den Zeilen D und S wandert der Beitrag des Gates nach rechts:

$$\begin{pmatrix} 0{,}225 & -1{,}025 \\ -0{,}025 & 2{,}025 \end{pmatrix}\begin{pmatrix} \underline U_D \\ \underline U_S \end{pmatrix} = \begin{pmatrix} -10 \\ 10 \end{pmatrix}$$

Mit der Determinante 0,225 · 2,025 − 1,025 · 0,025 = 0,43:

$$\underline U_D = \frac{-10\cdot 2{,}025 + 1{,}025\cdot 10}{0{,}43}\ \mathrm{mV} = -23{,}26\ \mathrm{mV}, \qquad \underline U_S = \frac{0{,}225\cdot 10 - 0{,}025\cdot 10}{0{,}43}\ \mathrm{mV} = 4{,}65\ \mathrm{mV}$$

(b) In mS, V und mA, Determinante 3j:

$$\underline U_2 = \frac{1 + j}{3j}\ \mathrm V = \frac{1 - j}{3}\ \mathrm V, \qquad \underline U_3 = \frac{1}{3j}\ \mathrm V = -\frac{j}{3}\ \mathrm V$$

$$\frac{\underline U_3}{\underline U_2} = \frac{-j}{1 - j} = \frac{1 - j}{2}$$

**Ergebnis:** **(a) −2,33 vom Gate zum Drain, 0,465 vom Gate zur Source; (b) (1 − j)/2, Betrag 0,707 bei −45°.**

**Einordnung:** (a) Die Signalquelle mit 10 mV erzeugt genau diese Potentiale, −23,26 mV und 4,65 mV; der Teststrom ersetzt sie, ohne die Übertragung zu ändern. (b) Von Knoten 2 zu Knoten 3 bilden nur $R_2$ und $C_2$ einen Spannungsteiler, $-j/(1 - j)$; was vor Knoten 2 liegt, spielt für das Verhältnis keine Rolle.
::::

:::frage
„Warum bestimmt man die Ausgangsimpedanz nicht aus Leerlaufspannung und Kurzschlussstrom?“
Im Kleinsignal-Ersatzschaltbild geht das und ergibt dieselben 8,90 kΩ, aus −43,96 mV und −4,94 µA bei 10 mV Signal. An der wirklichen Schaltung und im Simulator wäre der Kurzschluss aber auch einer für Gleichstrom: Der Drain läge auf 0 V statt auf 2,5 V, die Source ebenfalls, durch den Transistor flösse kein Strom, und seine Steilheit wäre null; der Signalanteil des Kurzschlussstroms wäre null, und durch den Kurzschluss flösse nur der Gleichstrom von 0,5 mA aus $R_D$. Ein Kurzschluss nur für das Signal über einen großen Kondensator ließe den Arbeitspunkt stehen, ist aber ein zusätzliches Bauelement. Die Teststromquelle braucht weder das eine noch das andere.
:::

## Das Ersatzzweitor aus drei Kenngrößen

*Wie fasst man eine ganze Verstärkerstufe in wenigen Zahlen zusammen, und wann reicht das?*

Treibt man das Gate der Verstärkerstufe mit einer idealen Testspannungsquelle statt der Signalquelle mit ihren 10 kΩ, so liefern zwei Läufe drei Zahlen. Die Quelle gibt keinen Strom ab, $\underline Y_\mathrm{ein}$ ist null. Bei offenem Drain kommt je Volt am Gate −4,40 V heraus, $\underline A_V$ ist −4,40. Bei kurzgeschlossenem Gate sieht man in den Drain 8,90 kΩ. Damit verhält sich die Stufe an ihren Anschlüssen wie ein __Ersatzzweitor__, eine Schaltung mit einem Eingangs- und einem Ausgangstor, deren Inneres durch wenige Kenngrößen ersetzt ist; ein __Tor__ ist ein Anschlusspaar, in das ebenso viel Strom hineinfließt, wie wieder herauskommt ([Zweitore und ihre Parameter](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/zweitore.html)). Am Eingang steht eine Admittanz, am Ausgang eine gesteuerte Spannungsquelle mit Innenimpedanz, die Ersatzquelle nach Thévenin aus dem Artikel über Ersatzquellen (Abbildung 5).

:::grafik
Szene: st1/netzwerkanalyse/04-ersatzzweitor · Vorlage: schaltbild
**Abbildung 5:** (a) Ersatzzweitor in Thévenin-Form: am Eingang die Admittanz $\underline Y_\mathrm{ein}$, am Ausgang eine spannungsgesteuerte Spannungsquelle $\underline A_V \underline U_\mathrm{ein}$ in Reihe mit $\underline Z_\mathrm{aus}$; daneben grau die Testquellen, mit denen man die drei Größen bestimmt. (b) Dasselbe in Norton-Form: eine gesteuerte Stromquelle $(\underline A_V/\underline Z_\mathrm{aus})\,\underline U_\mathrm{ein}$, die in den Ausgangsknoten einspeist, parallel zu $\underline Z_\mathrm{aus}$. (c) Werte der Verstärkerstufe: $\underline Y_\mathrm{ein}$ = 0, $\underline A_V$ = −4,40, $\underline Z_\mathrm{aus}$ = 8,90 kΩ, $\underline A_V/\underline Z_\mathrm{aus}$ = −0,494 mS; mit 10 kΩ Last −2,33, also −23,26 mV bei 10 mV. Drei Kenngrößen aus zwei Läufen derselben Matrix beschreiben eine rückwirkungsfreie Stufe vollständig.
:::

**Die Akteure:**

- __$\underline U_\mathrm{ein}$__: Spannung am Eingangstor; bei einer idealen Quelle gleich $\underline U_q$.
- __$\underline I_\mathrm{aus}$__: Strom aus dem Ausgang in die Last; __$R_L$__: Last, 10 kΩ an der Verstärkerstufe.

:::formel Formel
$$\underline I_\mathrm{ein} = \underline Y_\mathrm{ein}\,\underline U_\mathrm{ein}$$

$$\underline U_\mathrm{aus} = \underline A_V\,\underline U_\mathrm{ein} - \underline Z_\mathrm{aus}\,\underline I_\mathrm{aus}$$
:::

**So liest man das:** $\underline A_V \underline U_\mathrm{ein}$ ist die Leerlaufspannung des Ausgangs und $\underline Z_\mathrm{aus}$ seine Innenimpedanz. Mit einer Last teilt sich die Leerlaufspannung zwischen $\underline Z_\mathrm{aus}$ und $R_L$ auf; bei der Stufe mit 10 kΩ Last ergibt das −2,33:

$$\underline U_\mathrm{aus} = \underline A_V\,\underline U_\mathrm{ein}\,\frac{R_L}{R_L + \underline Z_\mathrm{aus}}$$

Nach $\underline I_\mathrm{aus}$ aufgelöst entsteht die Norton-Form, eine gesteuerte Stromquelle parallel zu $\underline Z_\mathrm{aus}$:

$$\underline I_\mathrm{aus} = \frac{\underline A_V}{\underline Z_\mathrm{aus}}\,\underline U_\mathrm{ein} - \frac{\underline U_\mathrm{aus}}{\underline Z_\mathrm{aus}}$$

Bei der Stufe ist $\underline A_V/\underline Z_\mathrm{aus}$ gleich −0,494 mS: Bei kurzgeschlossenem Ausgang fließen je Volt am Gate 0,494 mA in den Drain hinein. Das ist die wirksame Steilheit der ganzen Stufe, rund die Hälfte von $g_m$, weil der Source-Widerstand gegenkoppelt.

**Kurz gesagt:** Der aus dem Ausgang herausfließende Kurzschlussstrom je Volt am Eingang ist die Leerlaufverstärkung geteilt durch die Ausgangsimpedanz.

:::fehlvorstellung
„Eingangsadmittanz, Verstärkung und Ausgangsimpedanz beschreiben jede Schaltung vollständig.“ Das liegt nahe, weil die drei Zahlen bei der Verstärkerstufe genügen. Sie genügen dort, weil nichts vom Drain auf das Gate zurückwirkt: Der Eingangsstrom hängt nicht davon ab, was am Ausgang geschieht. Im RC-Tiefpass wirkt der Ausgang dagegen auf den Eingang zurück. Mit einer Last von 1 kΩ an Knoten 3 sinkt seine Eingangsadmittanz von (0,667 + 0,333j) mS auf (0,600 + 0,300j) mS, um 10 %, während das Ersatzzweitor den Wert ohne Last behielte. Die Ausgangsspannung, (0,1 − 0,2j) V, sagt es dagegen richtig voraus, denn der Ausgang ist bei ideal getriebenem Eingang immer eine Ersatzquelle. Für Schaltungen mit Rückwirkung braucht man vier Kenngrößen, die Parameter eines Vierpols.
:::

Idee der Herleitung: Man wendet am Ausgang den Satz von der Ersatzquelle an und erkennt Leerlaufspannung und Innenimpedanz in den beiden Läufen wieder.

:::herleitung
**Ausgangspunkt:** die Ersatzquelle nach Thévenin für ein Klemmenpaar einer linearen Schaltung, mit Leerlaufspannung $\underline U_\mathrm{LL}$ und Innenimpedanz $\underline Z_i$ ([Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html)), und die Definitionen von $\underline A_V$ und $\underline Z_\mathrm{aus}$.

**Annahmen:** (i) Die Schaltung ist linear und enthält außer der Quelle am Eingang keine unabhängigen Quellen. (ii) Eine ideale Spannungsquelle treibt den Eingang. (iii) Für die Eingangsgleichung: Der Eingangsstrom hängt nicht vom Ausgangsstrom ab.

**Schritt 1**: Bei festem $\underline U_\mathrm{ein}$ ist der Ausgang ein Klemmenpaar einer linearen Schaltung mit einer einzigen inneren Quelle, also eine Ersatzquelle:

$$\underline U_\mathrm{aus} = \underline U_\mathrm{LL} - \underline Z_i\,\underline I_\mathrm{aus}$$

**Schritt 2**: Die Leerlaufspannung ist die Ausgangsspannung bei $\underline I_\mathrm{aus}$ = 0, bei offenem Ausgang wie in Lauf A. Sie ist proportional zur einzigen Anregung, und der Faktor ist nach Definition $\underline A_V$:

$$\underline U_\mathrm{LL} = \underline A_V\,\underline U_\mathrm{ein}$$

**Schritt 3** (entscheidender Schritt): Die Innenimpedanz ist die Impedanz am Ausgang bei abgeschalteter innerer Quelle, also bei $\underline U_\mathrm{ein}$ = 0 mit kurzgeschlossenem Eingang, genau wie in Lauf B. Weil die Quelle ideal ist, hängt sie nicht vom Wert von $\underline U_\mathrm{ein}$ ab:

$$\underline Z_i = \underline Z_\mathrm{aus}$$

**Schritt 4**: Eingesetzt ergibt sich die Ausgangsgleichung; teilt man sie durch $\underline Z_\mathrm{aus}$ und löst nach $\underline I_\mathrm{aus}$ auf, entsteht die Norton-Form:

$$\underline U_\mathrm{aus} = \underline A_V\,\underline U_\mathrm{ein} - \underline Z_\mathrm{aus}\,\underline I_\mathrm{aus}$$

**Schritt 5**: Am Eingang ist der Strom proportional zu $\underline U_\mathrm{ein}$ mit dem Faktor aus Lauf A, solange er nicht vom Ausgangsstrom abhängt (Annahme iii); sonst kommt ein Glied mit $\underline I_\mathrm{aus}$ hinzu.

**Ergebnis:**

$$\underline I_\mathrm{ein} = \underline Y_\mathrm{ein}\,\underline U_\mathrm{ein}$$

$$\underline U_\mathrm{aus} = \underline A_V\,\underline U_\mathrm{ein} - \underline Z_\mathrm{aus}\,\underline I_\mathrm{aus}$$

**Woher die Faktoren kommen:** $\underline A_V$ stammt aus dem Lauf mit offenem Ausgang, $\underline Z_\mathrm{aus}$ aus dem Lauf mit kurzgeschlossenem Eingang; das Minuszeichen daher, dass $\underline I_\mathrm{aus}$ aus dem Ausgang heraus gezählt wird.

**Proben:** Verstärkerstufe mit 10 kΩ Last: −4,396 mal 10 kΩ, geteilt durch 18,901 kΩ, ergibt −2,326, also −23,26 mV bei 10 mV wie in der vollständigen Knotenanalyse; Norton-Form: −0,4938 mS mal 8,901 kΩ parallel 10 kΩ, also 4,709 kΩ, ergibt ebenfalls −2,326. Grenzfall unendlicher Last: Die Ausgangsspannung ist die Leerlaufspannung. Einheit: $\underline A_V/\underline Z_\mathrm{aus}$ in S.

**Grenzen:** Mit Rückwirkung hängt die Eingangsadmittanz von der Last ab und die Ausgangsimpedanz vom Innenwiderstand der treibenden Quelle; dann beschreiben erst die vier Parameter eines Vierpols die Schaltung vollständig.
:::

::::beispiel Ersatzzweitor der Verstärkerstufe aus zwei Läufen
**Gegeben:** Verstärkerstufe ohne Last, $g_m$ = 1 mS, $g_o$ = 0,025 mS, $G_D$ = 0,1 mS, $G_S$ = 1 mS; ideale Testspannungsquelle am Gate, Teststromquelle am Drain.

**Gesucht:** $\underline Y_\mathrm{ein}$, $\underline A_V$, $\underline Z_\mathrm{aus}$, die Norton-Form und die Ausgangsspannung an 10 kΩ bei 10 mV.

**Rechnung:** In mS, mV und µA; Spalten $\underline U_G$, $\underline U_D$, $\underline U_S$ und der Zusatzstrom $\underline I_z$ der Testspannungsquelle; Zeilen G, D, S und die Zeile der Quelle:

$$\mathbf M = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 1 & 0{,}125 & -1{,}025 & 0 \\ -1 & -0{,}025 & 2{,}025 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}$$

Lauf A, rechte Seite (0; 0; 0; 1 mV): Die Quellenzeile setzt $\underline U_G$ = 1 mV, die Gate-Zeile ergibt $\underline I_z$ = 0. In den Zeilen D und S wandert das Gate nach rechts, Determinante 0,125 · 2,025 − 1,025 · 0,025 = 0,2275:

$$\underline U_D = \frac{-1\cdot 2{,}025 + 1{,}025\cdot 1}{0{,}2275}\ \mathrm{mV} = -4{,}396\ \mathrm{mV}$$

Lauf B, rechte Seite (0; 1 µA; 0; 0): Die Quellenzeile hält das Gate auf null:

$$\underline U_D = \frac{1\cdot 2{,}025}{0{,}2275}\ \mathrm{mV} = 8{,}901\ \mathrm{mV}$$

Kenngrößen, Norton-Form und Last:

$$\underline Y_\mathrm{ein} = 0, \qquad \underline A_V = -4{,}396, \qquad \underline Z_\mathrm{aus} = 8{,}901\ \mathrm{k\Omega}$$

$$\frac{\underline A_V}{\underline Z_\mathrm{aus}} = -0{,}4938\ \mathrm{mS}, \qquad \underline U_\mathrm{aus} = -4{,}396\cdot\frac{10}{18{,}901}\cdot 10\ \mathrm{mV} = -23{,}26\ \mathrm{mV}$$

**Ergebnis:** **$\underline Y_\mathrm{ein}$ = 0, $\underline A_V$ = −4,40, $\underline Z_\mathrm{aus}$ = 8,90 kΩ; Norton −0,494 mS; an 10 kΩ −23,26 mV.**

**Einordnung:** Die wirksame Steilheit 0,494 mS ist $g_m G_S/(g_m + g_o + G_S)$ = 1/2,025 mS: Der Source-Widerstand nimmt einen Teil der Gate-Spannung weg, wie im Artikel über Ersatzquellen beschrieben. Weil $\underline Y_\mathrm{ein}$ null ist, spielen die 10 kΩ der wirklichen Signalquelle keine Rolle; deshalb stimmen die −23,26 mV mit der vollständigen Knotenanalyse überein.
::::

## Transientenanalyse: Zeitschritte statt Differentialgleichungen

*Wie berechnet man den Spannungsverlauf nach dem Einschalten, wenn sich die Differentialgleichungen nicht mehr von Hand lösen lassen?*

Ein RC-Glied aus $R$ = 1 kΩ und $C$ = 100 nF liegt ab $t$ = 0 an einer Quelle mit $U_q$ = 1 V. Seine Zeitkonstante τ ist das Produkt aus $R$ und $C$, hier 0,1 ms. Die Knotenregel am Kondensator ergibt seine Differentialgleichung: Der Strom durch $R$ lädt ihn, und sein Strom ist nach [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html) die Änderung seiner Ladung $CU$:

$$\frac{dU}{dt} = \frac{U_q - U}{\tau}$$

Ihre Lösung, hergeleitet in [Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html), erreicht nach einer Zeitkonstante 0,632 V:

$$U(t) = U_q\,\big(1 - \exp(-t/\tau)\big)$$

Eine integrierte Schaltung enthält Tausende gewollter und __parasitärer__ Kapazitäten, also solcher, die zwischen Leitungen und Bauelementen unvermeidlich mitentstehen; ihre gekoppelten Differentialgleichungen lassen sich nicht mehr geschlossen lösen. Ein Simulator berechnet die Spannungen deshalb nur zu einzelnen Zeitpunkten, Schritt für Schritt aus dem jeweils vorigen Zustand. Dieses Verfahren heißt __Transientenanalyse__, nach dem englischen transient für den Einschwing- oder Übergangsvorgang. Den nächsten Wert erhält man, indem man vom bekannten Wert mit einer Steigung über den Zeitschritt weitergeht; offen ist nur, mit welcher Steigung: der am Anfang des Schritts oder der am Ende (Abbildung 6).

:::grafik
Szene: st1/netzwerkanalyse/04-euler-verfahren · Vorlage: zeitverlauf-schritte
**Abbildung 6:** (a) Ladekurve des RC-Glieds, $U_q$ = 1 V, τ = 0,1 ms, über $t$ von 0 bis 4τ, dazu die Werte beider Euler-Verfahren mit dem Zeitschritt τ/2: explizit 0,500 V, 0,750 V und 0,875 V bei 0,5τ, τ und 1,5τ, oberhalb der Kurve; implizit 0,333 V, 0,556 V und 0,704 V, unterhalb; exakt 0,393 V, 0,632 V und 0,777 V. Am ersten Schritt die Tangente im Startpunkt mit der Steigung $U_q/\tau$, 10 V/ms, und die Gerade mit der Steigung, die zum Endpunkt des Schritts gehört. (b) Die Folgen mit dem Zeitschritt 3τ: explizit 3 V, −3 V, 9 V, −15 V, 33 V, implizit 0,750 V, 0,938 V, 0,984 V, 0,996 V. Das explizite Verfahren nimmt die Steigung am Anfang des Schritts, das implizite die am Ende; bei großen Schritten schaukelt sich das explizite auf, das implizite bleibt stabil.
:::

**Die Akteure:**

- __$t_n$__: die Zeitpunkte, an denen gerechnet wird, $n$ = 0, 1, 2, …; __$h$__: __Schrittweite__, der Abstand zweier Zeitpunkte; in s; 10 µs, also τ/10, im Beispiel.
- __$U_n$__: der berechnete Näherungswert der Kondensatorspannung zum Zeitpunkt $t_n$; in V; $U_0$ = 0.
- __τ__: Zeitkonstante des RC-Glieds, 0,1 ms; __$U_q$__: Quellenspannung nach dem Einschalten, 1 V, zugleich der Endwert.

:::formel Formel
$$U_{n+1} = U_n + h\,\left.\frac{dU}{dt}\right|_{t_n}$$

$$U_{n+1} = U_n + h\,\left.\frac{dU}{dt}\right|_{t_{n+1}}$$
:::

**So liest man das:** Die erste Zeile ist das __explizite Euler-Verfahren__: Es nimmt die Steigung am Anfang des Schritts, die sich aus dem bekannten $U_n$ ausrechnen lässt, und liefert den neuen Wert direkt. Die zweite ist das __implizite Euler-Verfahren__: Es nimmt die Steigung am Ende des Schritts, die vom gesuchten $U_{n+1}$ abhängt; der neue Wert ist die Lösung einer Gleichung. Beim RC-Glied lauten die beiden Rechenvorschriften:

$$U_{n+1} = U_n + \frac{h}{\tau}\,\big(U_q - U_n\big)$$

$$U_{n+1} = \frac{U_n + (h/\tau)\,U_q}{1 + h/\tau}$$

Mit $h$ = τ/10 ergeben sich nach zehn Schritten, bei $t$ = τ, 0,651 V und 0,614 V gegen exakt 0,632 V: Die Fehler, +0,019 V und −0,018 V, sind annähernd gleich groß und haben entgegengesetzte Vorzeichen. Halbe Schrittweite halbiert beide annähernd, auf +0,0094 V und −0,0090 V. Der Fehler eines einzelnen Schritts wächst dagegen mit dem Quadrat der Schrittweite, 4,8 mV beim ersten Schritt mit τ/10 und ein Viertel davon mit τ/20; über eine feste Zeit summieren sich aber doppelt so viele solcher Schritte. Verfahren, deren Gesamtfehler so proportional zur Schrittweite ist, heißen __von erster Ordnung__.

:::frage
„Woher kennt das implizite Verfahren die Steigung am Ende des Schritts, bevor es den Wert dort kennt?“
Es kennt sie nicht im Voraus. Die Steigung am Ende hängt vom gesuchten Wert ab, und der Schritt wird zu einer Gleichung für $U_{n+1}$; beim RC-Glied ist sie linear und in einer Zeile gelöst, mit τ/10 ergibt der erste Schritt 90,9 mV. In einer Schaltung ist diese Gleichung ein lineares Gleichungssystem für alle Knotenpotentiale. Ein Simulator löst in jedem Schritt ohnehin ein solches System, deshalb kostet ihn das implizite Verfahren kaum mehr als das explizite.
:::

Idee der Herleitung: Man entwickelt die exakte Lösung um den Anfang bzw. das Ende des Schritts bis zum quadratischen Glied und lässt dieses weg.

:::herleitung
**Ausgangspunkt:** die Taylor-Entwicklung, die eine Funktion in der Nähe eines Punkts aus ihren Ableitungen dort aufbaut. Bricht man sie nach dem linearen Glied ab und nimmt die zweite Ableitung an einem passenden Zwischenpunkt ξ zwischen $t$ und $t + h$, gilt sie für eine zweimal stetig differenzierbare Funktion exakt:

$$U(t + h) = U(t) + h\,\frac{dU}{dt}(t) + \frac{h^2}{2}\,\frac{d^2U}{dt^2}(\xi)$$

**Annahmen:** (i) $U(t)$ ist im Schritt zweimal stetig differenzierbar, die Quelle springt also nicht innerhalb eines Schritts. (ii) Für den Fehler eines Schritts ist der Startwert exakt, $U_n$ gleich $U(t_n)$.

**Schritt 1**: Entwicklung um den Anfang des Schritts, mit einem Zwischenpunkt $\xi_1$:

$$U(t_{n+1}) = U(t_n) + h\,\frac{dU}{dt}(t_n) + \frac{h^2}{2}\,\frac{d^2U}{dt^2}(\xi_1)$$

**Schritt 2**: Lässt man das quadratische Glied weg, entsteht das explizite Verfahren; der Fehler eines Schritts ist das weggelassene Glied, $(h^2/2)$ mal die zweite Ableitung bei $\xi_1$.

**Schritt 3** (entscheidender Schritt): Entwicklung um das Ende des Schritts, rückwärts um $h$, mit einem Zwischenpunkt $\xi_2$, und umgestellt:

$$U(t_n) = U(t_{n+1}) - h\,\frac{dU}{dt}(t_{n+1}) + \frac{h^2}{2}\,\frac{d^2U}{dt^2}(\xi_2)$$

$$U(t_{n+1}) = U(t_n) + h\,\frac{dU}{dt}(t_{n+1}) - \frac{h^2}{2}\,\frac{d^2U}{dt^2}(\xi_2)$$

**Schritt 4**: Ohne das quadratische Glied ist das das implizite Verfahren, sofern man die Steigung am Ende mit dem berechneten statt mit dem exakten Wert bildet. Sein Fehler je Schritt ist deshalb nur in führender Ordnung ebenso groß, also bis auf Glieder mit höheren Potenzen von $h$, und hat das umgekehrte Vorzeichen.

**Schritt 5**: Über eine feste Zeit $T$ sind es $T/h$ Schritte. Bei einem abklingenden Vorgang und einer Schrittweite, bei der Abweichungen von Schritt zu Schritt schrumpfen, wird jeder Fehler in den folgenden Schritten weitergereicht und dabei gedämpft; der Betrag des Gesamtfehlers ist deshalb höchstens die Summe der Beträge der Einzelfehler und proportional zu $h$:

$$\frac{T}{h}\cdot\frac{h^2}{2}\,\max\left|\frac{d^2U}{dt^2}\right| = \frac{T\,h}{2}\,\max\left|\frac{d^2U}{dt^2}\right|$$

**Ergebnis:**

$$U_{n+1} = U_n + h\,\left.\frac{dU}{dt}\right|_{t_n}$$

$$U_{n+1} = U_n + h\,\left.\frac{dU}{dt}\right|_{t_{n+1}}$$

mit einem Fehler je Schritt von in führender Ordnung $\pm(h^2/2)$ mal der zweiten Ableitung, über eine feste Zeit proportional zu $h$.

**Woher die Faktoren kommen:** Das $h^2/2$ ist das quadratische Glied der Taylor-Entwicklung; das Vorzeichen hängt davon ab, ob vorwärts oder rückwärts entwickelt wird.

**Proben:** RC-Glied: Am Anfang ist die zweite Ableitung $-U_q/\tau^2$, der Fehler des ersten Schritts also rund $h^2/(2\tau^2)$ mal 1 V, 5 mV bei $h$ = τ/10; gerechnet sind es +4,8 mV explizit (0,100 V gegen 0,0952 V) und −4,3 mV implizit (0,0909 V). Einheit: s² mal V/s² ergibt V.

**Grenzen:** Springt eine Quelle innerhalb eines Schritts, ist die Annahme (i) verletzt und der Fehler viel größer; Simulatoren legen deshalb an jeden Sprung einen Zeitpunkt. Wo sich die Spannungen schnell ändern, ist die zweite Ableitung groß, und die Schrittweite muss kleiner werden.
:::

::::beispiel Ladekurve des RC-Glieds mit beiden Euler-Verfahren
**Gegeben:** $R$ = 1 kΩ, $C$ = 100 nF, τ = 0,1 ms; Quelle 1 V ab $t$ = 0; Schrittweite $h$ = 10 µs, also τ/10.

**Gesucht:** $U_1$, $U_2$ und $U_{10}$ mit beiden Verfahren, die Fehler bei $t$ = τ.

**Rechnung:** Mit $h/\tau$ = 0,1, explizit:

$$U_1 = 0 + 0{,}1\cdot(1 - 0)\ \mathrm V = 0{,}100\ \mathrm V, \qquad U_2 = 0{,}1 + 0{,}1\cdot 0{,}9\ \mathrm V = 0{,}190\ \mathrm V$$

Allgemein bleibt nach jedem Schritt das 0,9-Fache der Abweichung vom Endwert, nach zehn Schritten also:

$$U_{10} = 1\ \mathrm V\cdot\big(1 - 0{,}9^{10}\big) = 0{,}651\ \mathrm V$$

Implizit:

$$U_1 = \frac{0 + 0{,}1}{1{,}1}\ \mathrm V = 0{,}0909\ \mathrm V, \qquad U_2 = \frac{0{,}0909 + 0{,}1}{1{,}1}\ \mathrm V = 0{,}174\ \mathrm V$$

$$U_{10} = 1\ \mathrm V\cdot\big(1 - 1{,}1^{-10}\big) = 0{,}614\ \mathrm V$$

Exakt bei $t$ = τ:

$$U(\tau) = 1\ \mathrm V\cdot\big(1 - \exp(-1)\big) = 0{,}632\ \mathrm V$$

**Ergebnis:** **Explizit 0,651 V, implizit 0,614 V, exakt 0,632 V; Fehler +0,019 V und −0,018 V.**

**Einordnung:** Im ersten Schritt liegt das explizite Verfahren über der Kurve, weil die Steigung am Schrittanfang die größte im Schritt ist, und das implizite darunter, weil es die kleinste nimmt. Dass die ganzen Folgen darüber bzw. darunter bleiben, zeigen die Faktoren je Schritt: Die Abweichung vom Endwert schrumpft explizit mit 0,9, exakt mit 0,905 und implizit mit 0,909. Mit $h$ = τ/20 schrumpfen beide Fehler auf +0,0094 V und −0,0090 V, die Hälfte, wie es ein Verfahren erster Ordnung verlangt.
::::

Bei großen Schritten zeigt sich der eigentliche Unterschied (Abbildung 6b). Er hängt nur davon ab, was ein Schritt mit der Abweichung vom Endwert macht.

**Die Akteure:**

- __$\delta_n$__: Abweichung des Näherungswerts vom Endwert, $U_n$ minus $U_q$; in V; −1 V am Anfang.

**Das Zusammenspiel:**

**Schritt 1**: Weil das RC-Glied linear ist und sich der Endwert nicht ändert, multipliziert jeder Schritt die Abweichung mit einem festen Faktor. Exakt wäre er $\exp(-h/\tau)$, für jede Schrittweite zwischen 0 und 1.

**Schritt 2**: Beim expliziten Verfahren liegt der Faktor für Schritte unter τ zwischen 0 und 1, und die Folge nähert sich dem Endwert von einer Seite. Zwischen τ und 2τ ist er negativ: Die Folge springt abwechselnd über den Endwert, klingt aber ab.

**Schritt 3**: Bei 2τ ist der Faktor −1, und die Spannung springt ohne Ende zwischen 2 V und 0 V. Darüber ist sein Betrag größer als 1, und die Abweichung wächst: Mit 3τ entstehen 3 V, −3 V, 9 V, −15 V, 33 V.

**Schritt 4**: Beim impliziten Verfahren liegt der Faktor für jede Schrittweite zwischen 0 und 1; mit 3τ entstehen 0,750 V, 0,938 V, 0,984 V, im Verlauf ungenau, aber ohne jedes Aufschaukeln. Ein Verfahren, bei dem Abweichungen an einem abklingenden Vorgang ebenfalls abklingen, heißt __stabil__.

:::formel Formel
$$\delta_{n+1} = \Big(1 - \frac{h}{\tau}\Big)\,\delta_n$$

$$\delta_{n+1} = \frac{\delta_n}{1 + h/\tau}$$
:::

**So liest man das:** Die obere Zeile gilt für das explizite, die untere für das implizite Verfahren; nach $n$ Schritten ist die Abweichung die $n$-te Potenz des Faktors mal der Anfangsabweichung. Je größer die Schrittweite im Verhältnis zur Zeitkonstante, desto kleiner wird der implizite Faktor, während der explizite durch null hindurch ins Negative wandert und bei 2τ den Betrag 1 überschreitet.

**Kurz gesagt:** Bei einem Vorgang, der mit einer Zeitkonstante abklingt, wächst die Abweichung beim expliziten Euler-Verfahren, sobald der Zeitschritt größer als die doppelte Zeitkonstante ist; beim impliziten schrumpft sie bei jedem Zeitschritt.

Idee der Herleitung: Man setzt die Differentialgleichung des RC-Glieds in beide Verfahren ein und zieht den Endwert ab.

:::herleitung
**Ausgangspunkt:** die Differentialgleichung des RC-Glieds und die beiden Euler-Verfahren.

**Annahmen:** (i) Ein Vorgang erster Ordnung mit der Zeitkonstante τ größer null und konstanter Quellenspannung nach dem Einschalten. (ii) Feste Schrittweite $h$.

**Schritt 1**: Explizit: Die Steigung am Schrittanfang ist $(U_q - U_n)/\tau$. Zieht man auf beiden Seiten $U_q$ ab, bleibt die Abweichung:

$$\delta_{n+1} = \delta_n - \frac{h}{\tau}\,\delta_n = \Big(1 - \frac{h}{\tau}\Big)\,\delta_n$$

**Schritt 2**: Implizit: Die Steigung am Schrittende ist $(U_q - U_{n+1})/\tau$; nach Abziehen von $U_q$ steht die gesuchte Abweichung auf beiden Seiten:

$$\delta_{n+1} = \delta_n - \frac{h}{\tau}\,\delta_{n+1}$$

$$\delta_{n+1} = \frac{\delta_n}{1 + h/\tau}$$

**Schritt 3** (entscheidender Schritt): Nach $n$ Schritten ist die Abweichung die $n$-te Potenz des Faktors mal $\delta_0$. Sie geht genau dann gegen null, wenn der Betrag des Faktors kleiner als 1 ist: explizit für $h$ zwischen 0 und 2τ, implizit für jedes positive $h$, denn $1 + h/\tau$ ist dann größer als 1.

**Schritt 4**: Vergleich mit dem exakten Faktor über die Reihe der Exponentialfunktion, mit $x$ gleich $h/\tau$:

$$\exp(-x) = 1 - x + \frac{x^2}{2} - \ldots, \qquad \frac{1}{1 + x} = 1 - x + x^2 - \ldots$$

Beide Verfahren treffen ihn bis zum linearen Glied und weichen im quadratischen um $x^2/2$ ab, mit entgegengesetztem Vorzeichen.

**Ergebnis:**

$$\delta_{n+1} = \Big(1 - \frac{h}{\tau}\Big)\,\delta_n$$

$$\delta_{n+1} = \frac{\delta_n}{1 + h/\tau}$$

explizit stabil für $h$ unter 2τ, implizit für jedes $h$.

**Woher die Faktoren kommen:** $1 - h/\tau$ stammt aus der Steigung am Anfang, die mit dem alten Wert gerechnet wird; die Division durch $1 + h/\tau$ aus der Unbekannten am Ende, die man auf eine Seite bringt.

**Proben:** $h$ = 3τ: explizit Faktor −2, die Abweichungen −1, 2, −4, 8 V ergeben 0, 3, −3, 9 V; implizit Faktor 0,25, also 0,750 V und 0,938 V. $h$ = 2τ: Faktor −1, abwechselnd 2 V und 0 V. $h$ = τ/10: $0{,}9^{10}$ = 0,349 und $1{,}1^{-10}$ = 0,386 gegen $\exp(-1)$ = 0,368.

**Grenzen:** Für Vorgänge, die schwingen, etwa in Schwingkreisen, und für nichtlineare Schaltungen sehen die Stabilitätsbereiche anders aus; der Grundgedanke, dass ein Faktor je Schritt über Wachsen oder Schrumpfen entscheidet, bleibt.
:::

::::beispiel Große Schritte am RC-Glied
**Gegeben:** RC-Glied wie oben, τ = 0,1 ms, Quelle 1 V; Schrittweite $h$ = 0,3 ms, also 3τ.

**Gesucht:** die ersten fünf Werte beider Verfahren.

**Rechnung:** Faktoren je Schritt:

$$1 - \frac{h}{\tau} = -2, \qquad \frac{1}{1 + h/\tau} = 0{,}25$$

Mit $U_n$ gleich 1 V plus Faktor hoch $n$ mal −1 V:

$$U_n = 1\ \mathrm V\cdot\big(1 - (-2)^n\big): \quad 3;\ -3;\ 9;\ -15;\ 33\ \mathrm V$$

$$U_n = 1\ \mathrm V\cdot\big(1 - 0{,}25^n\big): \quad 0{,}750;\ 0{,}938;\ 0{,}984;\ 0{,}996;\ 0{,}999\ \mathrm V$$

**Ergebnis:** **Explizit 3 V, −3 V, 9 V, −15 V, 33 V; implizit 0,750 V bis 0,999 V.**

**Einordnung:** Nach drei Schritten, bei 9τ, liegt das implizite Verfahren mit 0,984 V um 16 mV unter dem exakten Wert, das explizite ist unbrauchbar. Beim einzelnen RC-Glied wählt niemand einen so großen Schritt. In Schaltungen mit sehr verschiedenen Zeitkonstanten ist ein Schritt von mehreren Zeitkonstanten für die schnellsten Vorgänge aber unvermeidlich, wenn die langsamen in vertretbarer Schrittzahl berechnet werden sollen.
::::

:::fehlvorstellung
„Das implizite Euler-Verfahren ist genauer als das explizite.“ Das liegt nahe, weil es die Steigung am Ende nutzt, die Information also neuer scheint, und weil es bei großen Schritten so viel besser aussieht. Beide Verfahren sind aber von erster Ordnung, und ihre Fehler sind annähernd gleich groß: Mit τ/10 liegen sie nach einer Zeitkonstante um +0,019 V und −0,018 V daneben. Der Vorteil des impliziten Verfahrens ist die Stabilität, nicht die Genauigkeit. Genauer wird erst ein Verfahren höherer Ordnung, etwa die Trapezregel.
:::

:::vertiefung
**Die Trapezregel: zweite Ordnung und ihr Preis.** Nimmt man den Mittelwert der Steigungen am Anfang und am Ende des Schritts, entsteht die __Trapezregel__:

$$U_{n+1} = U_n + \frac{h}{2}\left(\frac{U_q - U_n}{\tau} + \frac{U_q - U_{n+1}}{\tau}\right)$$

Zieht man $U_q$ ab und bringt die neue Abweichung auf eine Seite, folgt der Faktor je Schritt:

$$\delta_{n+1} = \frac{1 - h/(2\tau)}{1 + h/(2\tau)}\,\delta_n$$

Seine Reihe stimmt mit $\exp(-h/\tau)$ bis zum quadratischen Glied überein; das Verfahren ist von zweiter Ordnung. Mit τ/10 ist der Fehler nach einer Zeitkonstante +0,3 mV statt 18 mV, mit τ/20 ein Viertel davon. Der Betrag des Faktors bleibt für jede Schrittweite unter 1, die Trapezregel ist stabil; oberhalb von 2τ wird der Faktor aber negativ, und die Folge schwingt abklingend um den Endwert, mit 3τ 1,2 V, 0,96 V, 1,008 V. Auch die Trapezregel ergibt für den Kondensator ein Begleitmodell; aus dem Kondensatorgesetz und der Trapezregel für die Spannung folgen der doppelte Leitwert und eine Stromquelle, die auch den Strom des vorigen Schritts enthält:

$$U_{n+1} = U_n + \frac{h}{2C}\,\big(I_n + I_{n+1}\big)$$

$$I_{n+1} = \frac{2C}{h}\,U_{n+1} - \Big(\frac{2C}{h}\,U_n + I_n\Big)$$

Beim RC-Glied mit 10 µs sind das 20 mS, und nach zehn Schritten liegen 0,6324 V an. Schaltungssimulatoren wie SPICE rechnen meist mit der Trapezregel oder mit Verfahren nach Gear, die mehrere zurückliegende Schritte nutzen. Sie wählen die Schrittweite laufend nach dem geschätzten Fehler eines Schritts und rechnen nach dem Sprung einer Quelle zunächst mit dem impliziten Euler-Verfahren weiter, das nicht schwingt.
:::

## Das Begleitmodell: der Kondensator im Zeitschritt

*Wie wird aus der Differentialgleichung eines Kondensators in jedem Zeitschritt wieder eine Knotengleichung?*

Beim RC-Glied mit $h$ = 10 µs verlangt das implizite Euler-Verfahren, dass der Kondensatorstrom am Ende des Schritts gleich $C$ mal der Spannungsänderung im Schritt geteilt durch $h$ ist. Der Teil mit der neuen Spannung verhält sich wie ein Leitwert von $C/h$ = 10 mS, also 100 Ω. Der Teil mit der alten Spannung ist aus dem vorigen Schritt bekannt und wirkt wie eine Stromquelle. Mit diesen beiden Ersatzelementen ist der Knoten eine gewöhnliche Knotengleichung, 1 mS durch $R$ und 10 mS im Kondensatorzweig:

$$(1\ \mathrm{mS} + 10\ \mathrm{mS})\,U_{n+1} = 1\ \mathrm{mS}\cdot 1\ \mathrm V + 10\ \mathrm{mS}\cdot U_n$$

Sie liefert 90,9 mV, 173,6 mV und nach zehn Schritten 0,614 V, genau die Werte des impliziten Euler-Verfahrens. Diese Ersatzschaltung heißt __Begleitmodell__ des Kondensators, so wie beim Newton-Verfahren die Ersatzschaltung eines nichtlinearen Bauelements für einen Iterationsschritt (Abbildung 7).

:::grafik
Szene: st1/netzwerkanalyse/04-begleitmodell-kondensator · Vorlage: schaltbild-ersatz
**Abbildung 7:** (a) Kondensator $C$ zwischen den Knoten a und b mit Spannung $U_{n+1}$ und Strom $I_{n+1}$ im Schritt $n + 1$. (b) Sein Begleitmodell: der Leitwert $G_C = C/h$ parallel zu einer Stromquelle $G_C U_n$, die in den Knoten a einspeist. (c) Eintrag in die Matrix: $G_C$ an denselben vier Plätzen wie $j\omega C$ in der Wechselstromanalyse, die Stromquelle auf der rechten Seite mit plus in Zeile a und minus in Zeile b. (d) RC-Glied mit $h$ = 10 µs: 10 mS parallel zur Stromquelle; 90,9 mV, 173,6 mV, nach zehn Schritten 0,614 V gegen exakt 0,632 V. Im Zeitschritt wird der Kondensator zu einem Leitwert, und seine Vorgeschichte steht als Stromquelle auf der rechten Seite.
:::

**Die Akteure:**

- __$U_n$__, __$I_n$__: Spannung und Strom des Kondensators zum Zeitpunkt $t_n$, die Spannung von a nach b, der Strom von a durch den Kondensator nach b gezählt.
- __$G_C$__: Leitwert des Begleitmodells, $C/h$; in S; 10 mS bei 100 nF und 10 µs. Üblich ist auch die Bezeichnung $G_\mathrm{eq}$.

**Das Zusammenspiel:**

**Schritt 1**: Der Kondensator speichert die Ladung $CU$; sein Strom ist ihre Änderung, $C$ mal die Änderungsrate der Spannung.

**Schritt 2**: Das implizite Euler-Verfahren braucht die Steigung der Spannung am Ende des Schritts. Dort ist sie der unbekannte Strom geteilt durch $C$.

**Schritt 3**: Löst man nach dem Strom auf, zerfällt er in zwei Teile: $G_C U_{n+1}$, den Strom eines Leitwerts bei der neuen Spannung, und den bekannten Teil $G_C U_n$, den eine Stromquelle in den Knoten a einspeist.

**Schritt 4**: Beide Teile sind Eintragsmuster aus dem Artikel über die modifizierte Knotenanalyse: der Leitwert an den vier Plätzen zwischen a und b, die Stromquelle mit plus in Zeile a und minus in Zeile b der rechten Seite. Der Kondensator verschwindet aus den Gleichungen; jeder Zeitschritt ist ein lineares Gleichungssystem wie eine Gleichstromrechnung.

**Schritt 5**: Nach dem Lösen ist $U_{n+1}$ bekannt und wird zur Vorgeschichte des nächsten Schritts. Der Wert der Stromquelle ändert sich, der Leitwert nicht; bei fester Schrittweite bleibt die Matrix in allen Schritten dieselbe.

:::formel Formel
$$I_{n+1} = G_C\,U_{n+1} - G_C\,U_n$$

$$G_C = \frac{C}{h}$$
:::

**So liest man das:** Je größer die Kapazität oder je kleiner der Schritt, desto größer $G_C$. In einem kurzen Schritt ändert ein Kondensator seine Spannung kaum; er wirkt wie eine Spannungsquelle $U_n$ mit dem kleinen Innenwiderstand $h/C$. Für sehr große Schritte geht $G_C$ gegen null, und der Kondensator wird zum Leerlauf wie in der Gleichstromrechnung. Behält er seine Spannung, fließt kein Strom: Die Stromquelle liefert dann genau den Strom, den der Leitwert aufnimmt.

**Kurz gesagt:** Beim impliziten Euler-Verfahren steht im Zeitschritt $C/h$ an den Plätzen, an denen in der Wechselstromanalyse $j\omega C$ steht; die Vorgeschichte kommt als Stromquelle auf die rechte Seite.

Idee der Herleitung: Man wendet das implizite Euler-Verfahren auf die Kondensatorspannung an, drückt die Steigung durch den Strom aus und löst nach dem Strom auf.

:::herleitung
**Ausgangspunkt:** das Ladungsgesetz des Kondensators und die Definition des Stroms als Änderung der Ladung, wie in [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html):

$$Q = C\,U, \qquad I = \frac{dQ}{dt}$$

**Annahmen:** (i) Linearer Kondensator, $C$ fest. (ii) Spannung und Strom gleichsinnig von a nach b gezählt. (iii) Implizites Euler-Verfahren mit der Schrittweite $h$.

**Schritt 1**: Mit festem $C$ ist der Strom $C$ mal die Ableitung der Spannung:

$$I = C\,\frac{dU}{dt}$$

**Schritt 2**: Implizites Euler-Verfahren für die Spannung; die Steigung am Schrittende ist nach Schritt 1 der Strom dort durch $C$:

$$U_{n+1} = U_n + \frac{h}{C}\,I_{n+1}$$

**Schritt 3** (entscheidender Schritt): Nach dem Strom aufgelöst:

$$I_{n+1} = \frac{C}{h}\,U_{n+1} - \frac{C}{h}\,U_n$$

**Schritt 4**: Der erste Summand ist der Strom eines Leitwerts $G_C$ zwischen a und b bei der Spannung $U_{n+1}$. Der zweite hängt nur vom bekannten $U_n$ ab: Ein Strom $-G_C U_n$ von a nach b ist dasselbe wie eine Stromquelle $G_C U_n$, deren Strom durch das Element von b nach a fließt, die also in a einspeist. Nach dem Muster der unabhängigen Stromquelle steht sie mit $+G_C U_n$ in Zeile a und $-G_C U_n$ in Zeile b der rechten Seite.

**Ergebnis:**

$$I_{n+1} = G_C\,U_{n+1} - G_C\,U_n$$

$$G_C = \frac{C}{h}$$

**Woher die Faktoren kommen:** $C/h$ ist die Ladung, die je Volt Spannungsänderung in einem Schritt fließt, geteilt durch die Dauer des Schritts; das Minuszeichen der Stromquelle stammt aus der alten Spannung, die vom Strom abgezogen wird.

**Proben:** Einheit: F/s = S. RC-Glied, erster Schritt: 1 mS mal 1 V, geteilt durch 11 mS, ergibt 90,9 mV; in den Kondensator fließen dabei 10 mS mal 90,9 mV, also 0,909 mA, derselbe Strom, den die restlichen 0,909 V durch 1 kΩ treiben. Grenzfall sehr großer Schritt: $G_C$ und Stromquelle gehen gegen null, der Kondensator ist ein Leerlauf. Grenzfall gleichbleibender Spannung: kein Strom.

**Grenzen:** Hängt die Kapazität von der Spannung ab, gilt der Ausgangspunkt mit einer Ladung $Q(U)$; das Begleitmodell wird dann in jedem Newton-Durchlauf neu aufgestellt. Der Fehler ist der des impliziten Euler-Verfahrens.
:::

::::beispiel RC-Glied mit dem Begleitmodell des Kondensators
**Gegeben:** Quelle 1 V ab $t$ = 0 über $R$ = 1 kΩ an $C$ = 100 nF; Schrittweite $h$ = 10 µs; $U_0$ = 0.

**Gesucht:** $U_1$, $U_2$, $U_{10}$ und der Strom im ersten Schritt.

**Rechnung:** Begleitmodell und Knotengleichung in mS, V und mA:

$$G_C = \frac{100\ \mathrm{nF}}{10\ \mu\mathrm s} = 10\ \mathrm{mS}$$

$$11\,U_{n+1} = 1 + 10\,U_n$$

$$U_1 = \frac{1}{11}\ \mathrm V = 0{,}0909\ \mathrm V, \qquad U_2 = \frac{1 + 0{,}909}{11}\ \mathrm V = 0{,}1736\ \mathrm V$$

Nach jedem Schritt bleibt das 10/11-Fache der Abweichung vom Endwert:

$$U_{10} = 1\ \mathrm V\cdot\Big(1 - \big(\tfrac{10}{11}\big)^{10}\Big) = 0{,}614\ \mathrm V$$

$$I_1 = G_C\,(U_1 - U_0) = 10\ \mathrm{mS}\cdot 0{,}0909\ \mathrm V = 0{,}909\ \mathrm{mA}$$

**Ergebnis:** **90,9 mV, 173,6 mV und 0,614 V; im ersten Schritt fließen 0,909 mA in den Kondensator.**

**Einordnung:** Die Folge ist genau die des impliziten Euler-Verfahrens, denn das Begleitmodell ist dieses Verfahren in Schaltungsform. Im zweiten Schritt speist die Stromquelle 0,909 mA ein, 10 mS mal 90,9 mV; sie hält den Kondensator auf seiner alten Spannung, bis neuer Strom sie ändert.
::::

:::fehlvorstellung
„Im Zeitschritt wird der Kondensator zu einem bloßen Widerstand.“ Das liegt nahe, weil der Leitwert $C/h$ den auffälligen Teil des Modells bildet. Ohne die Stromquelle vergäße der Kondensator aber in jedem Schritt seine Ladung: Das RC-Glied stünde nach jedem Schritt wieder auf den 90,9 mV des ersten Schritts, statt über 173,6 mV und 248,7 mV weiter zu steigen. Erst die Stromquelle $G_C U_n$ trägt die gespeicherte Ladung von Schritt zu Schritt weiter.
:::

### Die Spule

*Wie sieht das Begleitmodell einer Spule aus?*

An einer Spule ist die Spannung die Änderung der Flussverkettung, und diese ist bei einer linearen Spule $L$ mal Strom. Das implizite Euler-Verfahren, diesmal auf den Strom angewandt, macht aus ihr einen Leitwert $h/L$ parallel zu einer Stromquelle, die den bisherigen Strom $I_n$ in Richtung des Spulenstroms weiterführt (Abbildung 8):

$$I_{n+1} = \frac{h}{L}\,U_{n+1} + I_n$$

Die Rollen sind gegenüber dem Kondensator vertauscht. Ein kurzer Schritt macht den Leitwert klein, und die Spule hält ihren Strom; ein sehr langer macht ihn groß, und die Spule wird zum Kurzschluss wie in der Gleichstromrechnung. Ein RL-Glied aus 1 kΩ und 100 mH hat dieselbe Zeitkonstante 0,1 ms wie das RC-Glied. Mit $h$ = 10 µs ist der Leitwert 0,1 mS; im ersten Schritt liegen 0,909 V an der Spule, und es fließen 0,0909 mA, im zweiten 0,1736 mA, nach zehn Schritten 0,614 mA gegen exakt 0,632 mA. Es sind dieselben Zahlen wie beim Kondensator, in mA statt in V, weil beide Glieder dieselbe Differentialgleichung erster Ordnung mit derselben Zeitkonstante haben.

:::grafik
Szene: st1/netzwerkanalyse/04-begleitmodell-spule · Vorlage: schaltbild-ersatz
**Abbildung 8:** (a) Spule $L$ zwischen a und b mit $U_{n+1}$ und $I_{n+1}$ von a nach b. (b) Ihr Begleitmodell: Leitwert $h/L$ parallel zu einer Stromquelle $I_n$, deren Strom durch das Element von a nach b fließt. (c) Eintrag: $h/L$ an den Plätzen eines Leitwerts, die Stromquelle mit minus in Zeile a und plus in Zeile b der rechten Seite. (d) RL-Glied 1 kΩ und 100 mH mit $h$ = 10 µs: 0,1 mS; 0,909 V und 0,0909 mA im ersten Schritt, 0,614 mA nach zehn gegen exakt 0,632 mA. Die Spule wird zu einem kleinen Leitwert, und eine Stromquelle führt ihren bisherigen Strom weiter.
:::

Idee der Herleitung: Man wendet das implizite Euler-Verfahren auf den Spulenstrom an und drückt seine Steigung durch die Spannung aus.

:::herleitung
**Ausgangspunkt:** das Induktionsgesetz und die lineare Flussverkettung, wie in [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html):

$$U = \frac{d\Psi}{dt}, \qquad \Psi = L\,I$$

**Annahmen:** (i) Lineare Spule, $L$ fest. (ii) Spannung und Strom gleichsinnig von a nach b. (iii) Implizites Euler-Verfahren für den Strom.

**Schritt 1**: Mit festem $L$:

$$U = L\,\frac{dI}{dt}$$

**Schritt 2** (entscheidender Schritt): Implizites Euler-Verfahren für den Strom; die Steigung am Schrittende ist $U_{n+1}/L$:

$$I_{n+1} = I_n + \frac{h}{L}\,U_{n+1}$$

**Schritt 3**: Der Summand mit $U_{n+1}$ ist der Strom eines Leitwerts $h/L$; der bekannte Strom $I_n$ fließt von a nach b, also mit $-I_n$ in Zeile a und $+I_n$ in Zeile b der rechten Seite.

**Ergebnis:**

$$I_{n+1} = \frac{h}{L}\,U_{n+1} + I_n$$

**Woher die Faktoren kommen:** $h/L$ ist die Stromänderung je Volt in einem Schritt; $I_n$ ist der Strom, den die Spule ohne Spannung beibehielte.

**Proben:** Einheit: s/H = S. RL-Glied, erster Schritt: Die Knotengleichung mit 1,1 mS links und 1 mA rechts ergibt 0,909 V an der Spule und den Strom 0,1 mS mal 0,909 V, also 0,0909 mA. Grenzfall sehr großer Schritt: Der Leitwert wächst über alle Grenzen, die Spule wird zum Kurzschluss.

**Grenzen:** Wie beim Kondensator: Erste Ordnung; bei einer stromabhängigen Induktivität wird das Modell in jedem Newton-Durchlauf neu aufgestellt.
:::

## Eine Schaltung im Zeitschritt: die Verstärkerstufe

*Wie sieht ein Zeitschritt in einer Schaltung mit gesteuerter Quelle aus, und wie groß darf er sein?*

Die Verstärkerstufe ohne Source-Widerstand bekommt wie im Frequenzgang-Abschnitt des Artikels über die modifizierte Knotenanalyse 100 fF Gate-Source-Kapazität und eine Lastkapazität von 10 pF am Drain. Bei $t$ = 0 springt die Signalspannung von 0 auf 10 mV; die umgewandelte Signalquelle speist dann 1 µA parallel zu 0,1 mS in das Gate. Gesucht sind die Änderungen der Potentiale von Gate und Drain gegenüber dem Arbeitspunkt; als Kleinsignalgrößen werden sie klein geschrieben, $u_G$ und $u_D$. Das Gate lädt sich mit einer Zeitkonstante von 1 ns auf 10 mV auf, der Drain folgt mit 44,4 ns gegen −44,4 mV und braucht von 10 % auf 90 % des Endwerts 97,7 ns, die __Anstiegszeit__ (Abbildung 9).

:::grafik
Szene: st1/netzwerkanalyse/04-verstaerker-transiente · Vorlage: schaltbild-kurve
**Abbildung 9:** (a) Kleinsignal-Ersatzschaltbild der Stufe ohne Source-Widerstand nach dem Sprung: 1 µA parallel zu 0,1 mS am Gate, $C_{gs}$ = 100 fF, gesteuerte Quelle 1 mS, 0,225 mS und $C_L$ = 10 pF am Drain; darunter dieselbe Schaltung im Zeitschritt $h$ = 5 ns mit den Begleitmodellen 0,02 mS und 2 mS samt Stromquellen und der Matrix (0,12; 0 / 1; 2,225) mS. (b) $u_G$ und $u_D$ von 0 bis 300 ns: exakt als Kurven, das implizite Verfahren mit $h$ = 5 ns als Punkte, $u_D$ = −3,75 mV nach 5 ns gegen exakt −3,82 mV, −28,79 mV bei 50 ns gegen −29,68 mV, −44,37 mV bei 300 ns gegen −44,39 mV; Endwert −44,4 mV, Anstiegszeit von 10 % auf 90 % des Endwerts 97,7 ns. (c) Das explizite Verfahren mit derselben Schrittweite am Gate: 50 mV, −150 mV, 650 mV, −2550 mV. Die Matrix ist in jedem Schritt dieselbe; die schnelle Zeitkonstante von 1 ns macht das explizite Verfahren bei 5 ns instabil, das implizite rechnet stabil weiter.
:::

**Die Akteure:**

- __$u_{G,n}$__, __$u_{D,n}$__: die Änderungen der Potentiale von Gate und Drain zum Zeitpunkt $t_n$; in mV.
- __$C_{gs}$__, __$C_L$__: Gate-Source- und Lastkapazität, 100 fF und 10 pF; __$G_\mathrm{sig}$__: Innenleitwert der Signalquelle, 0,1 mS; __$G_D$__, __$G_L$__: Leitwerte von $R_D$ und der Last, je 0,1 mS; mit $g_o$ hat der Drain zusammen 0,225 mS.
- __$\tau_G$__, __$\tau_D$__: Zeitkonstanten von Gate und Drain.

**Das Zusammenspiel:** Jeder der beiden Knoten verhält sich wie ein RC-Glied, ein Kondensator gegen den Leitwert am Knoten, und seine Zeitkonstante ist Kapazität durch Leitwert:

$$\tau_G = \frac{C_{gs}}{G_\mathrm{sig}} = 1\ \mathrm{ns}$$

$$\tau_D = \frac{C_L}{G_D + G_L + g_o} = 44{,}4\ \mathrm{ns}$$

Beide Kondensatoren liegen gegen Masse; ihre Begleitmodelle tragen deshalb nur auf der Diagonalen ein, $C_{gs}/h$ beim Gate und $C_L/h$ beim Drain. Die gesteuerte Quelle trägt $g_m$ in Zeile D, Spalte G ein wie in jeder Knotenanalyse. Mit $h$ = 5 ns sind die Leitwerte der Begleitmodelle 0,02 mS und 2 mS, und jeder Zeitschritt ist in mS, mV und µA das System:

$$\begin{pmatrix} 0{,}12 & 0 \\ 1 & 2{,}225 \end{pmatrix}\begin{pmatrix} u_{G,n+1} \\ u_{D,n+1} \end{pmatrix} = \begin{pmatrix} 1 + 0{,}02\,u_{G,n} \\ 2\,u_{D,n} \end{pmatrix}$$

Die Matrix ist in jedem Schritt dieselbe; ein Simulator eliminiert sie einmal und löst danach nur noch mit wechselnden rechten Seiten, 60 Schritte bis 300 ns. Die Werte liegen nahe an der exakten Lösung: −3,75 mV nach dem ersten Schritt gegen −3,82 mV, −28,79 mV bei 50 ns gegen −29,68 mV, −44,37 mV bei 300 ns gegen −44,39 mV. Der größte Fehler, 0,90 mV bei 45 ns, sinkt mit $h$ = 1 ns auf 0,19 mV, wie es die erste Ordnung erwarten lässt.

Die Schrittweite von 5 ns ist für das Gate das Fünffache seiner Zeitkonstante. Das explizite Verfahren multipliziert die Abweichung am Gate dann in jedem Schritt mit −4: 50 mV, −150 mV, 650 mV, −2550 mV. Stabil wäre es erst unter 2 ns, genau erst bei Bruchteilen einer Nanosekunde, und für 300 ns bräuchte es mehr als 150 Schritte, obwohl sich das Gate nach wenigen Nanosekunden nicht mehr ändert. Eine Schaltung, deren Zeitkonstanten so weit auseinanderliegen, heißt __steif__; in integrierten Schaltungen reichen sie von Femtosekunden an parasitären Knoten bis zu Millisekunden in Versorgungsfiltern. Simulatoren rechnen deshalb mit impliziten Verfahren: Die Schrittweite richtet sich dann nach der Genauigkeit des langsamen Vorgangs und nicht nach der Stabilität des schnellsten.

Die Zeitkonstanten sind die Kehrwerte der Eckkreisfrequenzen, die der Frequenzgang derselben Stufe zeigt: 1 ns zu 10⁹ 1/s, 44,4 ns zu 2,25·10⁷ 1/s, also zu den Eckfrequenzen 159 MHz und 3,58 MHz. Allgemein gehört zu einem reellen Pol bei $s$ gleich $-\omega_p$ mit positivem $\omega_p$ im Zeitbereich ein Anteil, der mit $\exp(-\omega_p t)$ abklingt; die Laplace-Transformation, die einen Zeitverlauf in eine Funktion der komplexen Frequenz $s$ überführt, verbindet beide Beschreibungen. Die exakte Sprungantwort des Drains, mit der die Werte oben verglichen sind, hat den Endwert __$u_{D\infty}$__ = −44,4 mV:

:::formel Satz
$$u_D(t) = u_{D\infty}\left[1 - \frac{\tau_D\,\exp(-t/\tau_D) - \tau_G\,\exp(-t/\tau_G)}{\tau_D - \tau_G}\right]$$
:::

**So liest man das:** Zu Beginn ist der Klammerausdruck null, denn der Drain kann wegen $C_L$ nicht springen; danach dominiert der langsame Anteil mit $\tau_D$, weil der schnelle nach wenigen Nanosekunden abgeklungen ist. Wäre $\tau_G$ null, bliebe der Ladevorgang mit $\tau_D$ allein übrig. Der Endwert ist die Verstärkung bei tiefen Frequenzen, −4,44, mal 10 mV.

Idee der Herleitung: Man löst zuerst die Gleichung des Gates und setzt dessen Spannung als Anregung in die Gleichung des Drains ein.

:::herleitung
**Ausgangspunkt:** die Knotenregel an Gate und Drain mit den Kondensatorströmen $C\,du/dt$, als Kleinsignalgrößen.

**Annahmen:** (i) Kleinsignal-Ersatzschaltbild ohne Source-Widerstand und ohne Kapazität zwischen Gate und Drain. (ii) Bei $t$ = 0 sind beide Kondensatoren entladen, danach liegt die Signalspannung $u_\mathrm{sig}$ = 10 mV an. (iii) $\tau_G$ ist von $\tau_D$ verschieden.

**Schritt 1**: Gate: Der Quellenstrom $G_\mathrm{sig} u_\mathrm{sig}$ teilt sich auf den Innenleitwert und $C_{gs}$ auf; geteilt durch $G_\mathrm{sig}$ ist das ein Ladevorgang mit $\tau_G$:

$$\tau_G\,\frac{du_G}{dt} + u_G = u_\mathrm{sig}, \qquad u_G(t) = u_\mathrm{sig}\big(1 - \exp(-t/\tau_G)\big)$$

**Schritt 2**: Drain: Der Strom der gesteuerten Quelle, $g_m u_G$, fließt vom Drain nach Masse; der Leitwert am Drain und $C_L$ liefern ihn. Geteilt durch $G_D + G_L + g_o$:

$$\tau_D\,\frac{du_D}{dt} + u_D = -\frac{g_m}{G_D + G_L + g_o}\,u_G$$

Für große $t$ ist $u_G$ gleich $u_\mathrm{sig}$ und die Ableitung null; daraus folgt der Endwert:

$$u_{D\infty} = -\frac{g_m}{G_D + G_L + g_o}\,u_\mathrm{sig}$$

**Schritt 3** (entscheidender Schritt): Die Anregung enthält den Anteil $-u_\mathrm{sig}\exp(-t/\tau_G)$; ein Ansatz mit demselben Zeitverlauf, $u_{D\infty} + B\exp(-t/\tau_G)$, eingesetzt, ergibt für die Exponentialglieder:

$$B\,\Big(1 - \frac{\tau_D}{\tau_G}\Big) = -u_{D\infty}, \qquad B = u_{D\infty}\,\frac{\tau_G}{\tau_D - \tau_G}$$

**Schritt 4**: Dazu kommt die Lösung ohne Anregung, $K\exp(-t/\tau_D)$. Der Anfangswert null legt $K$ fest:

$$u_{D\infty} + B + K = 0, \qquad K = -u_{D\infty}\,\frac{\tau_D}{\tau_D - \tau_G}$$

**Ergebnis:**

$$u_D(t) = u_{D\infty}\left[1 - \frac{\tau_D\,\exp(-t/\tau_D) - \tau_G\,\exp(-t/\tau_G)}{\tau_D - \tau_G}\right]$$

**Woher die Faktoren kommen:** Die Gewichte $\tau_D$ und $\tau_G$ der beiden Exponentialglieder stammen aus dem Anfangswert und aus der Anregung durch das Gate; der Nenner $\tau_D - \tau_G$ aus dem Ansatz in Schritt 3.

**Proben:** Bei $t$ = 0 sind beide Exponentialfunktionen 1, der Bruch ist 1, und der Drain startet bei null. Für große $t$ bleibt der Endwert, −4,44 mal 10 mV, also −44,4 mV. Zahlenwerte: −3,82 mV bei 5 ns, −29,68 mV bei 50 ns, −39,65 mV bei 100 ns. Grenzfall $\tau_G$ gegen null: der Ladevorgang mit $\tau_D$ allein.

**Grenzen:** Mit einer Kapazität zwischen Gate und Drain sind die Knoten gekoppelt, und die Zeitkonstanten gehören nicht mehr zu einzelnen Knoten. Bei gleichen Zeitkonstanten wird der Bruch unbestimmt; sein Grenzwert enthält dann ein Glied $t\exp(-t/\tau_D)$.
:::

::::beispiel Die ersten Zeitschritte der Verstärkerstufe mit 5 ns
**Gegeben:** $G_\mathrm{sig}$ = 0,1 mS, $C_{gs}$ = 100 fF, $g_m$ = 1 mS, Leitwert am Drain 0,225 mS, $C_L$ = 10 pF; Sprung der Signalquelle auf 1 µA bei $t$ = 0; $h$ = 5 ns; Start bei null.

**Gesucht:** $u_G$ und $u_D$ nach einem und nach zwei Schritten.

**Rechnung:** Begleitmodelle 100 fF/5 ns = 0,02 mS und 10 pF/5 ns = 2 mS; in mS, mV und µA wird zuerst die Gate-Zeile gelöst, dann die Drain-Zeile:

$$u_{G,1} = \frac{1}{0{,}12}\ \mathrm{mV} = 8{,}333\ \mathrm{mV}, \qquad u_{D,1} = \frac{2\cdot 0 - 1\cdot 8{,}333}{2{,}225}\ \mathrm{mV} = -3{,}745\ \mathrm{mV}$$

$$u_{G,2} = \frac{1 + 0{,}02\cdot 8{,}333}{0{,}12}\ \mathrm{mV} = 9{,}722\ \mathrm{mV}$$

$$u_{D,2} = \frac{2\cdot(-3{,}745) - 1\cdot 9{,}722}{2{,}225}\ \mathrm{mV} = -7{,}736\ \mathrm{mV}$$

**Ergebnis:** **Gate 8,33 mV und 9,72 mV, Drain −3,75 mV und −7,74 mV; exakt 9,93 mV und 10,00 mV bzw. −3,82 mV und −8,14 mV.**

**Einordnung:** Das Gate braucht drei Schritte, bis es nahe 10 mV liegt, obwohl es exakt schon nach 5 ns 99,3 % erreicht: Beim impliziten Verfahren klingt der schnelle Vorgang zu langsam ab, mit dem Faktor 1/6 je Schritt statt exakt 0,007, aber ohne zu schwingen. Das explizite Verfahren lieferte an derselben Stelle 50 mV und −150 mV.
::::

:::frage
„Warum wird bei 5 ns gerade das Gate instabil und nicht der Drain?“
Beim expliziten Verfahren bekommt jeder Knoten mit eigener Zeitkonstante seinen eigenen Faktor je Schritt. Am Drain ist er 0,89, die Abweichung schrumpft; am Gate ist er −4. Weil der Drain vom Gate gesteuert wird, reißt die wachsende Gate-Spannung ihn mit: −25 mV, 52,8 mV, −278 mV. Über die Stabilität entscheidet die kleinste Zeitkonstante, auch wenn ihr Vorgang längst abgeklungen ist.
:::

## Nichtlineare Schaltungen: Zeitschritte und Newton-Verfahren

*Wie berechnet ein Simulator den zeitlichen Verlauf, wenn die Schaltung Dioden oder Transistoren enthält?*

Die MOS-Diode aus [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html), ein Transistor mit verbundenem Gate und Drain, erreicht an einer realen Stromquelle mit 0,5 mA und 0,25 mS ihren Arbeitspunkt bei 1,0 V. Liegt ein Kondensator von 1 nF parallel und wird die Quelle bei $t$ = 0 eingeschaltet, steigt die Spannung von 0 V dorthin. In jedem Zeitschritt wird der Kondensator zum Begleitmodell; übrig bleibt eine nichtlineare Gleichung, die das Newton-Verfahren löst, indem es auch die Diode durch ein Begleitmodell ersetzt und so lange neu schätzt, bis sich die Lösung nicht mehr ändert.

**Die Akteure:**

- __$I_q$__, __$G_q$__: Strom und Innenleitwert der realen Stromquelle, 0,5 mA und 0,25 mS.
- __$U^{(\nu)}$__: die ν-te Newton-Schätzung für die Spannung am Ende des Zeitschritts; __$g(U^{(\nu)})$__, __$I_{\mathrm{eq},\nu}$__: Leitwert und Stromquelle des Begleitmodells der Diode bei dieser Schätzung, wie im Artikel über den Arbeitspunkt.
- __$G_C$__: Leitwert des Kondensator-Begleitmodells, 1 nF durch 0,1 µs, also 10 mS.

:::formel Formel
$$\big(G_q + G_C + g(U^{(\nu)})\big)\,U^{(\nu+1)} = I_q + G_C\,U_n - I_{\mathrm{eq},\nu}$$
:::

**So liest man das:** Links stehen alle Leitwerte am Knoten: der der Quelle, der des Kondensator-Begleitmodells und der der Diode bei der aktuellen Schätzung. Rechts stehen die Quellenströme: der der Quelle, die Vorgeschichte des Kondensators und die Stromquelle der Diode. Unterhalb der Schwelle von 0,5 V ist die Diode gesperrt, $g$ und $I_{\mathrm{eq},\nu}$ sind null, und die Gleichung ist linear: Ein Durchlauf löst sie, ein zweiter bestätigt das. Darüber braucht jeder Zeitschritt drei bis vier Durchläufe. Die Schwelle wird nach 1,15 µs erreicht, in der Rechnung mit $h$ = 0,1 µs im Schritt von 1,1 auf 1,2 µs; nach 5 µs liegen 0,991 V an, nach 142 Durchläufen in 50 Zeitschritten. Die Zeitkonstante ändert sich dabei von 4 µs, 1 nF an 0,25 mS, auf 0,8 µs am Arbeitspunkt, wo die Diode 1 mS beiträgt.

Abbildung 10 zeigt den Ablauf, den Schaltungssimulatoren daraus machen.

:::grafik
Szene: st1/netzwerkanalyse/04-spice-ablauf · Vorlage: blockbild
**Abbildung 10:** Ablauf der Transientenanalyse in einem Schaltungssimulator: Arbeitspunkt als Startzustand; Begleitmodelle der nichtlinearen Bauelemente aus der aktuellen Schätzung; Leitwerte und Ströme in das Gleichungssystem eintragen; lösen; konvergiert? Nein: neue Schätzung und zurück zu den Begleitmodellen, die innere Schleife des Newton-Verfahrens. Ja: Zeitschritt $h$ wählen, $t_{n+1} = t_n + h$; Endzeit erreicht? Nein: Begleitmodelle der Kondensatoren und Spulen aus dem neuen Zustand und zurück, die äußere Schleife der Zeit. Daneben die MOS-Diode mit 1 nF und $h$ = 0,1 µs: Spannung von 0 auf 0,991 V in 5 µs, Newton-Durchläufe je Zeitschritt 2 unterhalb der Schwelle bei 1,15 µs, danach 3 bis 4. Außen läuft die Zeit, innen das Newton-Verfahren; beide führen jede Rechnung auf ein lineares Gleichungssystem zurück.
:::

**Das Zusammenspiel:**

**Schritt 1**: Der Startzustand ist der Arbeitspunkt vor dem Einschalten, mit dem Newton-Verfahren berechnet; im Beispiel 0 V, weil die Quelle aus ist.

**Schritt 2**: Der Simulator wählt einen Zeitschritt und stellt die Begleitmodelle der Kondensatoren und Spulen aus dem Zustand des letzten Schritts auf.

**Schritt 3**: In der inneren Schleife ersetzt er die nichtlinearen Bauelemente durch ihre Begleitmodelle bei der aktuellen Schätzung, trägt alles in die Matrix ein und löst; das wiederholt er, bis sich die Lösung nicht mehr ändert. Als erste Schätzung dient der Wert des vorigen Zeitschritts, der sich von der Lösung nur wenig unterscheidet; deshalb genügen wenige Durchläufe.

**Schritt 4**: Der konvergierte Zustand ist der neue Zeitpunkt. Ist die Endzeit nicht erreicht, folgt der nächste Zeitschritt mit Schritt 2.

Beide Schleifen ersetzen, was nicht linear ist, durch einen Leitwert und eine Stromquelle, und jeder innere Durchlauf löst ein lineares, dünn besetztes Gleichungssystem nach den Eintragsmustern aus dem Artikel über die modifizierte Knotenanalyse. Seine Matrix enthält die Ableitungen aller Knotenströme nach den Potentialen bei der aktuellen Schätzung und heißt deshalb auch __Jacobi-Matrix__.

::::beispiel Ein Zeitschritt der MOS-Diode mit Kondensator
**Gegeben:** MOS-Diode mit $I$ = $k(U - U_\mathrm{th})^2$ oberhalb der Schwelle, $k$ = 1 mA/V², $U_\mathrm{th}$ = 0,5 V, darunter kein Strom; reale Stromquelle 0,5 mA mit 0,25 mS; 1 nF parallel; $h$ = 0,1 µs; bei 1,1 µs ist $U_n$ = 0,47571 V.

**Gesucht:** die Spannung bei 1,2 µs mit den Newton-Durchläufen.

**Rechnung:** In mS, V und mA ist $G_C$ = 10 mS; der feste Teil der rechten Seite, 0,5 mA plus 10 mS mal 0,47571 V, beträgt 5,2571 mA. Erste Schätzung ist $U^{(0)}$ = 0,47571 V, unter der Schwelle, also ohne Diode:

$$U^{(1)} = \frac{5{,}2571}{0{,}25 + 10}\ \mathrm V = 0{,}512888\ \mathrm V$$

Diese Schätzung liegt über der Schwelle; das Begleitmodell der Diode dort:

$$g(U^{(1)}) = 2k\,(U^{(1)} - U_\mathrm{th}) = 0{,}025776\ \mathrm{mS}, \qquad I_{\mathrm{eq},1} = k\,(U^{(1)} - U_\mathrm{th})^2 - g\,U^{(1)} = -0{,}013054\ \mathrm{mA}$$

$$U^{(2)} = \frac{5{,}2571 + 0{,}013054}{10{,}25 + 0{,}025776}\ \mathrm V = 0{,}512872\ \mathrm V$$

Ein dritter Durchlauf mit dem Begleitmodell bei $U^{(2)}$ ändert die siebte Stelle nicht mehr.

**Ergebnis:** **Bei 1,2 µs liegen 0,512872 V an, nach drei Durchläufen.**

**Einordnung:** Der erste Durchlauf rechnet noch ohne Diode und schießt deshalb um 16 µV über; der zweite korrigiert das mit dem Begleitmodell. Der Kondensator mit 10 mS dominiert die Gleichung, weil sich die Spannung in 0,1 µs wenig ändert; deshalb ist die Startschätzung aus dem vorigen Schritt so gut.
::::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Teststromquelle | sie ändert nur die rechte Seite und ist abgeschaltet ein Leerlauf |
| Impedanz an einem Knoten | die Antwort auf einen Teststrom ist eine Spalte der Inversen |
| Spannungsquelle am Eingang | sie gehört ohnehin zur Matrix; die Läufe unterscheiden sich nur rechts |
| keine Spannungsquelle an inneren Knoten | sie würde die Matrix und damit den Arbeitspunkt verändern |
| Ersatzzweitor | drei Kenngrößen aus zwei rechten Seiten derselben Matrix |
| Euler-Verfahren und Stabilität | der zeitliche Verlauf wird zu einer Folge von Schritten |
| Begleitmodell | der Kondensator wird Leitwert, seine Vorgeschichte Stromquelle auf der rechten Seite |
| nichtlineare Transiente | Newton innen, Zeit außen, jedes Mal ein lineares System |

Die Matrix des Gleichungssystems beschreibt die Schaltung, die rechte Seite ihre Anregung: Testquellen fragen die Schaltung ab, ohne die Matrix zu verändern, und in der Zeit bringt das Begleitmodell jedes Kondensators und jeder Spule die Vorgeschichte als Stromquelle auf die rechte Seite, sodass jeder Zeitschritt wieder ein lineares Gleichungssystem ist.

## Bedeutung und Ausblick

Schaltungssimulatoren nutzen beides ständig. In der Wechselstromanalyse setzt man an einen Knoten eine Stromquelle mit dem Wechselanteil 1 A und liest die Impedanz direkt als Spannung ab; Eingangs- und Ausgangsimpedanz, Verstärkung und Ersatzzweitor eines Verstärkers entstehen so aus wenigen Läufen, ohne die Schaltung umzubauen. Im Labor gilt dieselbe Regel: Ein Messsignal muss klein bleiben gegen den Arbeitspunkt, und das Messgerät darf die Schaltung nicht verändern. Die Transientenanalyse berechnet Einschwingvorgänge, Pulsantworten und das Umschalten digitaler Gatter mit Begleitmodellen, meist mit der Trapezregel und einer Schrittweite, die sich nach dem geschätzten Fehler richtet.

Die Grenzen liegen bei der Linearität und bei der Numerik. Große Signale verlangen in jedem Zeitschritt das Newton-Verfahren, und eine ungeeignete Schrittweite kann Schwingungen vortäuschen oder Vorgänge übergehen, die kürzer als ein Schritt sind. Ein Ersatzzweitor aus drei Kenngrößen gilt nur ohne Rückwirkung; die vollständige Beschreibung mit vier Parametern und die Zusammenschaltung solcher Blöcke sind das folgende Thema, die Vierpole.

:::kern
- Die Matrix beschreibt die Schaltung, die rechte Seite die Anregung; Abschalten setzt nur den Eintrag einer Quelle rechts null (Stromquelle Leerlauf, Spannungsquelle Kurzschluss).
- Teststromquelle in Knoten μ: $\underline Z_\mu = (\mathbf Y^{-1})_{\mu\mu}$, die Antwort auf 1 A ist die Spalte μ der Inversen.
- Eingangsadmittanz und Übertragung mit der Testspannungsquelle am Eingang, Ausgangsimpedanz mit Teststrom bei kurzgeschlossenem Eingang, an derselben Matrix.
- An inneren Knoten nur Teststromquellen: Eine Spannungsquelle verschiebt den Arbeitspunkt; die Übertragung ist bei Strom- und Spannungsanregung gleich.
- Ersatzzweitor: am Ausgang eine Quelle mit der Leerlaufspannung $\underline A_V$ mal Eingangsspannung hinter der Innenimpedanz $\underline Z_\mathrm{aus}$; vollständig nur ohne Rückwirkung.
- Beide Euler-Verfahren sind von erster Ordnung; das explizite ist nur für Schritte unter 2τ stabil, das implizite für jeden.
- Begleitmodell beim impliziten Euler-Verfahren: Kondensator als Leitwert $G_C = C/h$ parallel zur Stromquelle $G_C U_n$, Spule als $h/L$ parallel zu $I_n$.
- Nichtlineare Schaltungen: Newton-Verfahren in jedem Zeitschritt; jeder Durchlauf löst ein lineares Gleichungssystem.
:::

:::quiz
F: Warum verändert eine Teststromquelle die Schaltung nicht?
A: Ihr Strom hängt von keinem Potential ab; sie trägt nichts in die Matrix ein, nur einen Eintrag in die rechte Seite. Abgeschaltet ist sie ein Leerlauf, und die Gleichungen sind die der Schaltung ohne sie.
F: Warum ist die Impedanz an einem Knoten ein Diagonaleintrag der Inversen?
A: Ein Teststrom in Knoten μ ist die rechte Seite $\underline I_T\,\vec e_\mu$; die Lösung ist die Spalte μ der Inversen mal $\underline I_T$, und ihr Eintrag in Zeile μ, geteilt durch $\underline I_T$, ist die Impedanz.
F: Ein Teststrom von 1 µA erzeugt am Drain der Verstärkerstufe 8,90 mV. Wie groß ist die Ausgangsimpedanz, und was zeigt ein Simulator mit 1 A?
A: 8,90 kΩ; der Simulator zeigt 8901 V, zahlenmäßig die Impedanz in Ohm.
F: Stimmt es, dass man für die Ausgangsimpedanz die Eingangsquelle aus der Schaltung entfernt?
A: Nein. Eine abgeschaltete Spannungsquelle ist ein Kurzschluss und bleibt in der Matrix. Entfernt man sie im RC-Tiefpass, erhält man (0,2 − 0,6j) kΩ statt (0,333 − 0,667j) kΩ.
F: Warum speist man an einem inneren Knoten mit einer Stromquelle ein und nicht mit einer Spannungsquelle?
A: Die Spannungsquelle legt auch die Gleichspannung des Knotens fest und verschiebt den Arbeitspunkt; an der Source der Stufe ginge der Transistor in den Triodenbereich, und der Ausgangsleitwert stiege von 25 µS auf 0,648 mS. Eine Stromquelle ohne Gleichanteil ist ein Leerlauf, und die Übertragung ist dieselbe wie bei Spannungsanregung.
F: Stimmt es, dass Eingangsadmittanz, Leerlaufverstärkung und Ausgangsimpedanz jede Schaltung vollständig beschreiben?
A: Nein, nur ohne Rückwirkung. Im RC-Tiefpass sinkt die Eingangsadmittanz mit 1 kΩ Last um 10 %, das Ersatzzweitor behielte den Wert ohne Last; vollständig beschreiben erst die vier Parameter eines Vierpols.
F: Stimmt es, dass das implizite Euler-Verfahren genauer ist als das explizite?
A: Nein. Beide sind von erster Ordnung; mit τ/10 liegen sie nach einer Zeitkonstante um +0,019 V und −0,018 V daneben. Der Vorteil des impliziten Verfahrens ist die Stabilität bei großen Schritten.
F: Warum wird das explizite Euler-Verfahren bei Zeitschritten über der doppelten Zeitkonstante instabil?
A: Jeder Schritt multipliziert die Abweichung vom Endwert mit $1 - h/\tau$; oberhalb von 2τ ist der Betrag dieses Faktors größer als 1, mit 3τ genau −2, und die Abweichung wächst. Beim impliziten Verfahren ist der Faktor $1/(1 + h/\tau)$ für jede Schrittweite kleiner als 1.
F: Warum braucht das Begleitmodell des Kondensators neben dem Leitwert $C/h$ eine Stromquelle?
A: Sie trägt die Spannung des vorigen Schritts und damit die gespeicherte Ladung weiter. Ohne sie stünde das RC-Glied mit 10 µs Schrittweite nach jedem Schritt wieder auf 90,9 mV.
F: Warum rechnen Schaltungssimulatoren mit impliziten Verfahren?
A: Schaltungen sind oft steif: In der Verstärkerstufe liegen 1 ns und 44,4 ns nebeneinander, in integrierten Schaltungen Femtosekunden und Millisekunden. Explizit müsste der Schritt unter der doppelten kleinsten Zeitkonstante bleiben; implizit richtet er sich nach der Genauigkeit des langsamen Vorgangs.
:::
