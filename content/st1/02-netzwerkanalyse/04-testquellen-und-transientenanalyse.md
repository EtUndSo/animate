---
title: Testquellen und Transientenanalyse linearer Schaltungen
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse
order: 33020400
summary: Wie man Eingangs- und Ausgangsimpedanz und Übertragungsfunktionen einer Schaltung mit Testquellen bestimmt, ohne die Schaltung zu verändern, und wie ein Simulator ihren zeitlichen Verlauf mit Zeitschritten und Begleitmodellen berechnet. Kompakte Fassung mit hergeleiteter Impedanz als Diagonaleintrag der Inversen, Übertragung zwischen Knoten, Euler-Verfahren mit Fehler und Stabilität und Begleitmodell des Kondensators; die ausführliche enthält zusätzlich das Ersatzzweitor mit Herleitung, die Trapezregel, die Spule, die exakte Sprungantwort und nichtlineare Schaltungen mit Newton-Verfahren.
tags: Testquelle, Eingangswiderstand, Ausgangswiderstand, Transientenanalyse, Zeitkonstante
stil: 3
fassung: kompakt
---

## Worum es geht

Eine entworfene Schaltung muss man befragen können: Wie stark belastet sie ihre Quelle, wie stark gibt ihr Ausgang unter Last nach, wie viel Signal kommt an, und wie verläuft die Spannung nach dem Einschalten? Eine Messung, die dafür die Schaltung umbaut, misst eine andere Schaltung, und den zeitlichen Verlauf vieler Kondensatoren kann man nur Schritt für Schritt numerisch berechnen. Beides beruht auf einem Prinzip:

**Die Matrix des Gleichungssystems beschreibt die Schaltung, die rechte Seite ihre Anregung: Testquellen fragen die Schaltung ab, ohne die Matrix zu verändern, und in der Zeit bringt das Begleitmodell jedes Kondensators und jeder Spule die Vorgeschichte als Stromquelle auf die rechte Seite, sodass jeder Zeitschritt wieder ein lineares Gleichungssystem ist.**

Vorausgesetzt werden das Rechnen mit [Zeigern](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html), die modifizierte Knotenanalyse mit Cramerscher Regel aus [Netzwerkgleichungen systematisch aufstellen: modifizierte Knotenanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/modifizierte-knotenanalyse.html), die Ersatzquelle aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html), der Arbeitspunkt aus [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html) und das [Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html). So rechnen Schaltungssimulatoren wie SPICE, und darauf bauen die Vierpole auf, Schaltungen mit zwei Anschlusspaaren, die man durch vier Kenngrößen beschreibt.

:::grafik
Szene: st1/netzwerkanalyse/04-uebersicht · Vorlage: schaltbild-matrix
**Abbildung 1:** (a) Eine Schaltung mit einer Testspannungsquelle am Eingang, Knoten 1, und einer Teststromquelle am Ausgang, Knoten 2; darunter ihr Gleichungssystem: eine feste Matrix und drei rechte Seiten, Lauf A mit 1 V am Eingang und Teststrom null für Eingangsadmittanz und Übertragung, Lauf B mit 0 V am Eingang und 1 A Teststrom für die Ausgangsimpedanz, dazu der Betrieb mit dem Signal. (b) Ein Kondensator im Zeitschritt h als Leitwert C/h parallel zu einer Stromquelle, die die Spannung des vorigen Schritts fortschreibt; darunter die Zeitachse mit den Schritten t₀, t₁, t₂, t₃. Testquellen und Zeitschritte mit fester Schrittweite ändern nur die rechte Seite des Gleichungssystems; die Schaltung bleibt dieselbe.
:::

## Teststromquellen: die Impedanz an einem Knoten

*Wie bestimmt man die Impedanz, die man in einen Knoten hineinsieht, ohne die Schaltung zu verändern?*

Als Beispiel dient die Verstärkerstufe aus [Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse.html), eine Source-Schaltung mit der Steilheit $g_m$ = 1 mS, dem Ausgangsleitwert $g_o$ = 25 µS, $R_D$ = 10 kΩ, $R_S$ = 1 kΩ und einer Signalquelle mit 10 kΩ Innenwiderstand; gerechnet wird mit ihrem __Kleinsignal-Ersatzschaltbild__, dem linearen Modell für kleine Änderungen um den Arbeitspunkt. Wie stark eine Last am Drain die Spannung einbrechen lässt, bestimmt die Impedanz, die man in den Drain hineinsieht. Man speist dazu einen bekannten Strom ein und liest die Spannung ab, die er hervorruft: Ein Mikroampere erzeugt 8,90 mV, die Impedanz ist 8,90 kΩ, die Innenimpedanz der Ersatzquelle am Drain. Eingespeist wird mit einer __Teststromquelle__, einer idealen Stromquelle, die nur dazu dient, die Schaltung abzufragen (Abbildung 2).

:::grafik
Szene: st1/netzwerkanalyse/04-teststrom-ausgang · Vorlage: schaltbild-matrix
**Abbildung 2:** (a) Kleinsignal-Ersatzschaltbild der Verstärkerstufe ohne Last: Signalquelle abgeschaltet, ihr Innenleitwert 0,1 mS bleibt am Gate; gesteuerte Quelle 1 mS, $g_o$ = 25 µS, $R_D$ = 10 kΩ, $R_S$ = 1 kΩ; eine Teststromquelle speist 1 µA vom Bezugsknoten in den Drain. (b) Das Gleichungssystem in mS, mV und µA: Leitwertmatrix mit den Zeilen (0,1; 0; 0), (1; 0,125; −1,025), (−1; −0,025; 2,025), rechte Seite (0; 1; 0); die Lösung (0; 8,90; 0,110) mV ist die Spalte D der Inversen, der Matrix, die das System für jede rechte Seite löst; Determinante 0,02275 mS³, Unterdeterminante 0,2025 mS². (c) Im Simulator mit 1 A: 8901 V, zahlenmäßig die Impedanz in Ω. Eine Teststromquelle erscheint nur auf der rechten Seite; die Antwort auf den Teststrom ist eine Spalte der Inversen, ihr Diagonaleintrag die Impedanz.
:::

**Die Akteure:**

- __$\underline I_T$__: __Teststrom__, vom Bezugsknoten in den Knoten μ eingespeist, ein Zeiger; in A; 1 µA im Beispiel, in Simulatoren meist 1 A.
- __μ__: Knoten des Teststroms; __κ__: ein beliebiger Knoten, an dem man die Antwort abliest.
- __$\underline Z_\mu$__: die Impedanz zwischen Knoten μ und Bezugsknoten, __Eingangsimpedanz__ an einem Eingang, __Ausgangsimpedanz__ an einem Ausgang; in Ω.
- __$\mathbf Y^{-1}$__: die __Inverse__ der Leitwertmatrix $\mathbf Y$, die Matrix, deren Produkt mit $\mathbf Y$ die Einheitsmatrix ergibt, also Einsen auf der Diagonalen und sonst Nullen; sie löst das System für jede rechte Seite auf einmal; Einträge in Ω.
- __$\vec e_\mu$__: die Spalte mit einer 1 in Zeile μ und sonst Nullen.

**Das Zusammenspiel:**

**Schritt 1**: Die Matrix beschreibt die Schaltung; auf der rechten Seite stehen nur die unabhängigen Quellen, deren Wert von keiner Spannung und keinem Strom der Schaltung abhängt.

**Schritt 2**: Eine ideale Stromquelle in den Knoten μ liefert ihren Strom unabhängig von jedem Potential. Sie trägt nichts in die Matrix ein, nur $+\underline I_T$ in Zeile μ der rechten Seite.

**Schritt 3**: Mit dem Wert null verschwindet auch dieser Eintrag: Eine abgeschaltete Stromquelle ist ein __Leerlauf__, durch den kein Strom fließt, und darf in jedem Betriebsfall angeschlossen bleiben.

**Schritt 4**: Alle übrigen unabhängigen Quellen schaltet man ab, indem man ihre Einträge rechts null setzt: Eine Stromquelle wird zum Leerlauf, eine Spannungsquelle mit 0 V zum __Kurzschluss__, weil ihre Zeile dann gleiche Potentiale an beiden Anschlüssen verlangt. Gesteuerte Quellen bleiben aktiv, denn sie gehören zur Matrix.

**Schritt 5**: Die Lösung ist die Spalte μ der Inversen mal $\underline I_T$; ihr Eintrag in Zeile μ, geteilt durch den Teststrom, ist die Impedanz.

:::formel Formel
$$\underline Z_\mu = \frac{\underline U_\mu}{\underline I_T} = \big(\mathbf Y^{-1}\big)_{\mu\mu} = \frac{\det\mathbf Y^{(\mu\mu)}}{\det\mathbf Y}$$
:::

**So liest man das:** Die Impedanz an einem Knoten ist der Diagonaleintrag der Inversen, nach der Cramerschen Regel die Determinante der Streichungsmatrix $\mathbf Y^{(\mu\mu)}$ ohne Zeile und Spalte μ, geteilt durch die Determinante. Die übrigen Einträge derselben Spalte geben die Spannung an Knoten κ je Ampere in Knoten μ an. Mit der Matrix der modifizierten Knotenanalyse gilt dasselbe.

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
**Gegeben:** Verstärkerstufe ohne Last, Signalquelle abgeschaltet, ihr Innenleitwert $G_\mathrm{sig}$ = 0,1 mS bleibt am Gate; $g_m$ = 1 mS, $g_o$ = 0,025 mS, $G_D$ = 0,1 mS, $G_S$ = 1 mS; 1 µA in den Drain.

**Gesucht:** die Impedanz am Drain.

**Rechnung:** In mS, mV und µA, Zeilen und Spalten G, D, S:

$$\begin{pmatrix} 0{,}1 & 0 & 0 \\ 1 & 0{,}125 & -1{,}025 \\ -1 & -0{,}025 & 2{,}025 \end{pmatrix}\begin{pmatrix} \underline U_G \\ \underline U_D \\ \underline U_S \end{pmatrix} = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$$

$$\det\mathbf Y = 0{,}1\cdot(0{,}125\cdot 2{,}025 - 1{,}025\cdot 0{,}025) = 0{,}02275\ \mathrm{mS^3}, \qquad \det\mathbf Y^{(DD)} = 0{,}1\cdot 2{,}025 = 0{,}2025\ \mathrm{mS^2}$$

$$\underline Z_D = \frac{0{,}2025}{0{,}02275}\ \mathrm{k\Omega} = 8{,}90\ \mathrm{k\Omega}$$

**Ergebnis:** **8,90 kΩ; 1 µA erzeugt am Drain 8,90 mV.**

**Einordnung:** Das ist die Innenimpedanz der Ersatzquelle am Drain, hier mit einer einzigen rechten Seite gewonnen. Ein Simulator mit 1 A zeigt 8901 V, zahlenmäßig die Impedanz in Ohm. Mit der Last von 10 kΩ ergeben sich 4,71 kΩ, die Parallelschaltung.
::::

:::frage
„Muss der Teststrom 1 A sein, und hält die Schaltung das aus?“
Der Wert ist beliebig, denn das Kleinsignal-Ersatzschaltbild ist linear und der Quotient bleibt gleich. Mit 1 A ist die Spannung in Volt zahlenmäßig die Impedanz in Ohm. Die 8901 V am Drain sind eine Rechengröße des linearisierten Modells; an der wirklichen Schaltung muss ein Teststrom klein bleiben gegen die 0,25 mA des Arbeitspunkts.
:::

## Testspannungsquelle am Eingang: Eingangsadmittanz, Übertragung und Ausgangsimpedanz

*Wie bestimmt man, wie stark eine Schaltung ihre Quelle belastet, wie viel Signal am Ausgang ankommt und wie stark der Ausgang unter Last nachgibt?*

Der RC-Tiefpass aus den beiden vorigen Artikeln wird am Knoten 1 von einer idealen Spannungsquelle angesteuert, $R_1$ = $R_2$ = 1 kΩ, $C_1$ = $C_2$ = 100 nF, ω = 10⁴ 1/s. Ein Teststrom am Knoten 1 flösse ganz in die abgeschaltete, also kurzschließende Spannungsquelle. Am Eingang dient deshalb die Spannungsquelle selbst als __Testspannungsquelle__; mit ihrem Zusatzstrom gehört sie ohnehin zur Matrix der modifizierten Knotenanalyse, und ihr Wert steht rechts. Zwei Läufe mit derselben Matrix beantworten alle drei Fragen (Abbildung 3).

:::grafik
Szene: st1/netzwerkanalyse/04-testspannung-eingang · Vorlage: schaltbild-matrix
**Abbildung 3:** (a) RC-Tiefpass mit idealer Spannungsquelle am Knoten 1 als Testspannungsquelle und einer Teststromquelle am Ausgang, Knoten 3; $R_1$ = $R_2$ = 1 kΩ, $C_1$ = $C_2$ = 100 nF, ω = 10⁴ 1/s. (b) Dieselbe Matrix der modifizierten Knotenanalyse mit zwei rechten Seiten: Lauf A mit 1 V an der Quelle und Teststrom null liefert den Eingangsstrom (0,667 + 0,333j) mA und die Ausgangsspannung −j/3 V; Lauf B mit 0 V an der Quelle und 1 mA Teststrom liefert am Ausgang (0,333 − 0,667j) V. (c) Falsch: Quelle entfernt statt kurzgeschlossen, die Ausgangsimpedanz wäre (0,2 − 0,6j) kΩ. Zwei Läufe an derselben Matrix ergeben Eingangsadmittanz, Übertragung und Ausgangsimpedanz; abgeschaltet ist die Spannungsquelle ein Kurzschluss, kein Leerlauf.
:::

**Die Akteure:**

- __$\underline U_q$__: Spannung der Testspannungsquelle, Pluspol am Eingangsknoten; 1 V in Lauf A, null in Lauf B.
- __$\underline I_\mathrm{ein}$__: Strom, den die Quelle in den Eingang liefert, gleich $-\underline I_z$, weil der Zusatzstrom __$\underline I_z$__ in den Pluspol hinein gezählt wird.
- __$\underline U_\mathrm{aus}$__: Potential des Ausgangsknotens, im Tiefpass $\underline U_3$.

:::formel Definition
$$\underline Y_\mathrm{ein} = \frac{\underline I_\mathrm{ein}}{\underline U_q}\ \ \text{bei}\ \underline I_T = 0$$

$$\underline A_V = \frac{\underline U_\mathrm{aus}}{\underline U_q}\ \ \text{bei}\ \underline I_T = 0$$

$$\underline Z_\mathrm{aus} = \frac{\underline U_\mathrm{aus}}{\underline I_T}\ \ \text{bei}\ \underline U_q = 0$$
:::

**So liest man das:** Die __Eingangsadmittanz__ ist der Strom, den die Schaltung je Volt aus der Quelle zieht. Die __Spannungsübertragungsfunktion__ $\underline A_V$ gilt bei offenem Ausgang, denn der abgeschaltete Teststrom ist ein Leerlauf; bei Verstärkern heißt sie __Leerlaufverstärkung__. Die Ausgangsimpedanz gilt bei kurzgeschlossenem Eingang. Man definiert die Größen so, weil zwei Läufe ohne Umbau sie liefern: Lauf A die ersten beiden und zugleich die Übertragung zu jedem inneren Knoten, Lauf B die dritte; die Matrix eliminiert ein Simulator dabei nur einmal.

:::frage
„Ist der Strom der Testspannungsquelle nicht der Zusatzstrom aus der Lösung?“
Bis auf das Vorzeichen: Der Zusatzstrom zählt in den Pluspol hinein. Im Tiefpass ergibt Lauf A −(0,667 + 0,333j) mA, die Quelle liefert also (0,667 + 0,333j) mA in die Schaltung. Mit falschem Vorzeichen erhielte man einen Eingangsleitwert mit negativem Realteil, (−0,667 − 0,333j) mS, den ein Netz aus Widerständen und Kondensatoren nicht haben kann, weil es dann im Mittel Leistung an die Quelle abgäbe.
:::

::::beispiel Eingangsadmittanz, Übertragung und Ausgangsimpedanz des RC-Tiefpasses
**Gegeben:** RC-Tiefpass mit idealer Quelle an Knoten 1, $R_1$ = $R_2$ = 1 kΩ, $j\omega C_1$ = $j\omega C_2$ = j·1 mS; Ausgang Knoten 3.

**Gesucht:** $\underline Y_\mathrm{ein}$, $\underline A_V$ und $\underline Z_\mathrm{aus}$.

**Rechnung:** In mS, kΩ, V und mA, Unbekannte $\underline U_1$, $\underline U_2$, $\underline U_3$, $\underline I_z$; die Matrix mit der Determinante −3j:

$$\mathbf M = \begin{pmatrix} 1 & -1 & 0 & 1 \\ -1 & 2 + j & -1 & 0 \\ 0 & -1 & 1 + j & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}$$

Lauf A, rechts (0; 0; 0; 1 V), gelöst wie im Artikel über die modifizierte Knotenanalyse:

$$\underline I_z = -\frac{2 + j}{3}\ \mathrm{mA}, \qquad \underline Y_\mathrm{ein} = \frac{2 + j}{3}\ \mathrm{mS}, \qquad \underline A_V = -\frac{j}{3}$$

Lauf B, rechts (0; 0; 1 mA; 0); entwickelt nach der ersetzten Spalte 3 und danach nach der Zeile (1; 0; 0):

$$\underline U_3 = \frac{-(2 + j)}{-3j}\ \mathrm V = \frac{1 - 2j}{3}\ \mathrm V, \qquad \underline Z_\mathrm{aus} = (0{,}333 - 0{,}667\,j)\ \mathrm{k\Omega}$$

**Ergebnis:** **$\underline Y_\mathrm{ein}$ = (0,667 + 0,333j) mS, also 1,34 kΩ Eingangsimpedanz im Betrag; $\underline A_V$ = −j/3; $\underline Z_\mathrm{aus}$ = (0,333 − 0,667j) kΩ.**

**Einordnung:** Die Quelle sieht mehr als die 1 kΩ von $R_1$, weil dahinter der Rest des Netzes liegt; der Strom eilt ihr um 26,6° voraus. Am Ausgang liegt bei kurzgeschlossenem Eingang $C_2$ parallel zum Rest, deshalb ist $\underline Z_\mathrm{aus}$ kapazitiv.
::::

:::fehlvorstellung
„Für die Ausgangsimpedanz nimmt man die Eingangsquelle aus der Schaltung heraus.“ Das liegt nahe, weil „abschalten“ nach „entfernen“ klingt. Eine abgeschaltete Spannungsquelle hat aber 0 V und ist ein Kurzschluss; ihre Zeile bleibt in der Matrix. Entfernt man sie, hängt $R_1$ frei, und der Tiefpass hätte am Ausgang (0,2 − 0,6j) kΩ statt (0,333 − 0,667j) kΩ.
:::

## Übertragung zwischen beliebigen Knoten

*Warum speist man an inneren Knoten einen Strom ein und keine Spannung?*

In der Verstärkerstufe liegt die Source im Arbeitspunkt auf 0,25 V, der Drain auf 2,5 V, und durch den Transistor fließen 0,25 mA; er arbeitet im __Sättigungsbereich__, in dem sein Strom fast nur von der Gate-Source-Spannung abhängt. Eine Spannungsquelle zwischen Source und Masse, die nur ein Signal liefern soll, hielte die Source auch für Gleichspannung fest, auf ihren Gleichanteil null. Die Gate-Source-Spannung stiege dann von 1 V auf 1,25 V, und der Transistor ginge in den __Triodenbereich__, in dem er wie ein gesteuerter Widerstand wirkt: 0,457 mA, am Drain 0,426 V, ein Ausgangsleitwert von 0,648 mS statt 25 µS. Das Kleinsignalmodell des Arbeitspunkts gälte nicht mehr. In den Gleichungen heißt das: Eine Spannungsquelle bringt eine Zeile und eine Spalte mit und verändert die Matrix, eine Stromquelle ohne Gleichanteil ändert nur die rechte Seite. Ein Simulator bestimmt Arbeitspunkt und Kleinsignalverhalten an derselben Schaltung; was zum Testen angeschlossen ist, wirkt auch im Arbeitspunkt. Am Eingang ist eine Spannungsquelle dagegen richtig, weil dort im Betrieb ohnehin eine sitzt, die das Gate auf seine Vorspannung von 1,25 V legt.

:::merke
Abgeschaltete Testquellen dürfen die Schaltung nicht verändern: Eine Teststromquelle ist dann ein Leerlauf, eine Testspannungsquelle ein Kurzschluss. Teststromquellen kommen deshalb parallel zu dem Anschlusspaar, dessen Impedanz man sucht, meist zwischen einen Knoten und Masse; Testspannungsquellen nur dorthin, wo ein Kurzschluss nichts ändert, an die Stelle einer vorhandenen Spannungsquelle oder in Reihe in einen Zweig. Zwischen Arbeitspunktbestimmung und Kleinsignalrechnung bleibt die Schaltung dieselbe.
:::

Mit der Teststromquelle am Knoten μ liefert ein Lauf alle Potentiale, und die Übertragung zu einem anderen Knoten ist ihr Verhältnis.

**Die Akteure:**

- __$\underline A_{\kappa\mu}$__: Spannungsübertragung von Knoten μ zu Knoten κ, das Potential an κ je Volt an μ; ohne Einheit; −2,33 vom Gate zum Drain der Stufe mit Last.

:::formel Formel
$$\underline A_{\kappa\mu} = \frac{\underline U_\kappa}{\underline U_\mu} = \frac{\big(\mathbf Y^{-1}\big)_{\kappa\mu}}{\big(\mathbf Y^{-1}\big)_{\mu\mu}}$$
:::

**So liest man das:** Die Übertragung ist das Verhältnis zweier Einträge derselben Spalte der Inversen; der Teststrom kürzt sich heraus. Sie ist dieselbe wie bei einer Spannungsquelle an μ, weil die Gleichungen aller übrigen Knoten in beiden Fällen keine Quelle enthalten und gleich sind. In der Verstärkerstufe mit Last ergibt ein Teststrom ins Gate −2,33 zum Drain und 0,465 zur Source, genau die Verhältnisse, die die Signalquelle erzeugt.

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

:::frage
„Warum bestimmt man die Ausgangsimpedanz nicht aus Leerlaufspannung und Kurzschlussstrom?“
Im Kleinsignal-Ersatzschaltbild geht das und ergibt dieselben 8,90 kΩ. An der wirklichen Schaltung und im Simulator wäre der Kurzschluss aber auch einer für Gleichstrom: Drain und Source lägen auf 0 V, durch den Transistor flösse kein Strom, seine Steilheit wäre null, und der Signalanteil des Kurzschlussstroms wäre null; durch den Kurzschluss flösse nur der Gleichstrom von 0,5 mA aus $R_D$. Die Teststromquelle ohne Gleichanteil lässt den Arbeitspunkt unberührt.
:::

## Drei Kenngrößen für eine ganze Stufe

*Wie fasst man eine Verstärkerstufe in wenigen Zahlen zusammen?*

Treibt man das Gate der Stufe mit einer idealen Testspannungsquelle, liefern zwei Läufe an derselben Matrix drei Zahlen: Die Quelle gibt keinen Strom ab, die Eingangsadmittanz ist null; bei offenem Drain kommen je Volt am Gate −4,40 V heraus; bei kurzgeschlossenem Gate sieht man in den Drain 8,90 kΩ. Damit ist die Stufe an ihren Anschlüssen ein __Ersatzzweitor__ mit je einem Eingangs- und Ausgangsanschlusspaar ([Zweitore und ihre Parameter](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/zweitore.html)): am Eingang eine Admittanz, am Ausgang eine gesteuerte Spannungsquelle mit −4,40 mal der Eingangsspannung in Reihe mit 8,90 kΩ, die Ersatzquelle nach Thévenin. Eine Last von 10 kΩ teilt die Leerlaufspannung im Verhältnis 10 zu 18,90 auf, die Verstärkung wird −2,33, und bei 10 mV entstehen −23,26 mV wie in der vollständigen Knotenanalyse. Der Kurzschlussstrom je Volt am Eingang, aus dem Drain heraus gezählt, ist −4,40 durch 8,90 kΩ, also −0,494 mS: Je Volt am Gate fließen 0,494 mA in den Drain hinein. Das ist die wirksame Steilheit der Stufe, 0,494 mS, rund halb so groß wie $g_m$, weil der Source-Widerstand gegenkoppelt, also einer Änderung des Drainstroms entgegenwirkt. Vollständig ist diese Beschreibung nur, wenn der Ausgang nicht auf den Eingang zurückwirkt; im RC-Tiefpass sinkt die Eingangsadmittanz mit 1 kΩ Last um 10 %, und man braucht die vier Parameter eines Vierpols.

## Transientenanalyse: Zeitschritte statt Differentialgleichungen

*Wie berechnet man den Spannungsverlauf nach dem Einschalten, wenn sich die Differentialgleichungen nicht mehr von Hand lösen lassen?*

Ein RC-Glied aus $R$ = 1 kΩ und $C$ = 100 nF liegt ab $t$ = 0 an einer Quelle mit $U_q$ = 1 V; seine Zeitkonstante τ, das Produkt aus $R$ und $C$, ist 0,1 ms. Der Strom durch $R$ lädt den Kondensator, und sein Strom ist nach [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html) die Änderung seiner Ladung $CU$; das ergibt die Differentialgleichung und ihre Lösung aus [Laden und Entladen des Kondensators](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/kondensator/laden-und-entladen.html), 0,632 V nach einer Zeitkonstante:

$$\frac{dU}{dt} = \frac{U_q - U}{\tau}$$

$$U(t) = U_q\,\big(1 - \exp(-t/\tau)\big)$$

Eine integrierte Schaltung mit Tausenden gewollter und __parasitärer__, also unvermeidlich mitentstehender, Kapazitäten lässt sich so nicht mehr lösen. Ein Simulator berechnet die Spannungen deshalb nur zu einzelnen Zeitpunkten, Schritt für Schritt aus dem vorigen Zustand; das heißt __Transientenanalyse__, nach dem englischen transient für den Übergangsvorgang. Man geht vom bekannten Wert mit einer Steigung über den Zeitschritt weiter, mit der am Anfang oder der am Ende des Schritts (Abbildung 4).

:::grafik
Szene: st1/netzwerkanalyse/04-euler-verfahren · Vorlage: zeitverlauf-schritte
**Abbildung 4:** (a) Ladekurve des RC-Glieds, $U_q$ = 1 V, τ = 0,1 ms, über $t$ von 0 bis 4τ, dazu die Werte beider Euler-Verfahren mit dem Zeitschritt τ/2: explizit 0,500 V, 0,750 V und 0,875 V bei 0,5τ, τ und 1,5τ, oberhalb der Kurve; implizit 0,333 V, 0,556 V und 0,704 V, unterhalb; exakt 0,393 V, 0,632 V und 0,777 V. Am ersten Schritt die Tangente im Startpunkt mit der Steigung $U_q/\tau$, 10 V/ms, und die Gerade mit der Steigung, die zum Endpunkt des Schritts gehört. (b) Die Folgen mit dem Zeitschritt 3τ: explizit 3 V, −3 V, 9 V, −15 V, 33 V, implizit 0,750 V, 0,938 V, 0,984 V, 0,996 V. Das explizite Verfahren nimmt die Steigung am Anfang des Schritts, das implizite die am Ende; bei großen Schritten schaukelt sich das explizite auf, das implizite bleibt stabil.
:::

**Die Akteure:**

- __$t_n$__: die Zeitpunkte, $n$ = 0, 1, 2, …; __$h$__: __Schrittweite__, ihr Abstand; in s; 10 µs, also τ/10, im Beispiel.
- __$U_n$__: der berechnete Näherungswert der Kondensatorspannung zum Zeitpunkt $t_n$; $U_0$ = 0.
- __τ__: Zeitkonstante, 0,1 ms; __$U_q$__: Quellenspannung und Endwert, 1 V.

:::formel Formel
$$U_{n+1} = U_n + h\,\left.\frac{dU}{dt}\right|_{t_n}$$

$$U_{n+1} = U_n + h\,\left.\frac{dU}{dt}\right|_{t_{n+1}}$$
:::

**So liest man das:** Die erste Zeile ist das __explizite Euler-Verfahren__ mit der Steigung am Schrittanfang, die aus dem bekannten $U_n$ folgt; der neue Wert ergibt sich direkt. Die zweite ist das __implizite Euler-Verfahren__ mit der Steigung am Schrittende, die vom gesuchten Wert abhängt; der Schritt ist eine Gleichung. Beim RC-Glied lauten die Vorschriften:

$$U_{n+1} = U_n + \frac{h}{\tau}\,\big(U_q - U_n\big)$$

$$U_{n+1} = \frac{U_n + (h/\tau)\,U_q}{1 + h/\tau}$$

Mit τ/10 ergeben sich nach zehn Schritten 0,651 V und 0,614 V gegen exakt 0,632 V; die Fehler, +0,019 V und −0,018 V, sind annähernd gleich groß mit entgegengesetztem Vorzeichen, und mit τ/20 halbieren sie sich ungefähr. Der Fehler eines einzelnen Schritts wächst mit dem Quadrat der Schrittweite, über eine feste Zeit summieren sich aber entsprechend mehr Schritte; Verfahren mit einem Gesamtfehler proportional zur Schrittweite heißen __von erster Ordnung__.

:::frage
„Woher kennt das implizite Verfahren die Steigung am Ende des Schritts, bevor es den Wert dort kennt?“
Es kennt sie nicht im Voraus; der Schritt wird zu einer Gleichung für den neuen Wert, beim RC-Glied linear und in einer Zeile gelöst. In einer Schaltung ist es ein lineares Gleichungssystem für alle Knotenpotentiale. Ein Simulator löst in jedem Schritt ohnehin ein solches System, deshalb kostet ihn das implizite Verfahren kaum mehr.
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

Bei großen Schritten zeigt sich der eigentliche Unterschied (Abbildung 4b); er hängt nur davon ab, was ein Schritt mit der Abweichung vom Endwert macht.

**Die Akteure:**

- __$\delta_n$__: Abweichung vom Endwert, $U_n$ minus $U_q$; in V; −1 V am Anfang.

**Das Zusammenspiel:**

**Schritt 1**: Weil das RC-Glied linear ist und der Endwert fest, multipliziert jeder Schritt die Abweichung mit einem festen Faktor; exakt wäre er $\exp(-h/\tau)$, immer zwischen 0 und 1.

**Schritt 2**: Beim expliziten Verfahren liegt der Faktor für Schritte unter τ zwischen 0 und 1; zwischen τ und 2τ ist er negativ, die Folge springt abwechselnd über den Endwert, klingt aber ab.

**Schritt 3**: Oberhalb von 2τ ist sein Betrag größer als 1, und die Abweichung wächst: Mit 3τ entstehen 3 V, −3 V, 9 V, −15 V, 33 V.

**Schritt 4**: Beim impliziten Verfahren liegt der Faktor für jede Schrittweite zwischen 0 und 1; mit 3τ entstehen 0,750 V, 0,938 V, 0,984 V. Ein Verfahren, bei dem Abweichungen an einem abklingenden Vorgang ebenfalls abklingen, heißt __stabil__.

:::formel Formel
$$\delta_{n+1} = \Big(1 - \frac{h}{\tau}\Big)\,\delta_n$$

$$\delta_{n+1} = \frac{\delta_n}{1 + h/\tau}$$
:::

**So liest man das:** Oben steht der Faktor des expliziten, unten der des impliziten Verfahrens; nach $n$ Schritten ist die Abweichung seine $n$-te Potenz mal der Anfangsabweichung. Mit wachsender Schrittweite wird der implizite Faktor kleiner, während der explizite ins Negative wandert und bei 2τ den Betrag 1 überschreitet.

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

:::fehlvorstellung
„Das implizite Euler-Verfahren ist genauer als das explizite.“ Das liegt nahe, weil es die Steigung am Ende nutzt und bei großen Schritten so viel besser aussieht. Beide sind aber von erster Ordnung, mit annähernd gleich großen Fehlern: Mit τ/10 liegen sie nach einer Zeitkonstante um +0,019 V und −0,018 V daneben. Der Vorteil des impliziten Verfahrens ist die Stabilität, nicht die Genauigkeit.
:::

## Das Begleitmodell: der Kondensator im Zeitschritt

*Wie wird aus der Differentialgleichung eines Kondensators in jedem Zeitschritt wieder eine Knotengleichung?*

Beim RC-Glied mit $h$ = 10 µs verlangt das implizite Euler-Verfahren, dass der Kondensatorstrom am Ende des Schritts $C$ mal die Spannungsänderung im Schritt geteilt durch $h$ ist. Der Teil mit der neuen Spannung wirkt wie ein Leitwert $C/h$ = 10 mS, der Teil mit der alten Spannung ist bekannt und wirkt wie eine Stromquelle. Damit ist der Knoten eine gewöhnliche Knotengleichung mit 1 mS und 10 mS, und sie liefert 90,9 mV, 173,6 mV und nach zehn Schritten 0,614 V, die Werte des impliziten Verfahrens. Diese Ersatzschaltung heißt __Begleitmodell__ des Kondensators (Abbildung 5). Der Leitwert allein genügte nicht: Ohne die Stromquelle vergäße der Kondensator seine Ladung, und das RC-Glied stünde nach jedem Schritt wieder auf 90,9 mV.

:::grafik
Szene: st1/netzwerkanalyse/04-begleitmodell-kondensator · Vorlage: schaltbild-ersatz
**Abbildung 5:** (a) Kondensator $C$ zwischen den Knoten a und b mit Spannung $U_{n+1}$ und Strom $I_{n+1}$ im Schritt $n + 1$. (b) Sein Begleitmodell: der Leitwert $G_C = C/h$ parallel zu einer Stromquelle $G_C U_n$, die in den Knoten a einspeist. (c) Eintrag in die Matrix: $G_C$ an denselben vier Plätzen wie $j\omega C$ in der Wechselstromanalyse, die Stromquelle auf der rechten Seite mit plus in Zeile a und minus in Zeile b. (d) RC-Glied mit $h$ = 10 µs: 10 mS parallel zur Stromquelle; 90,9 mV, 173,6 mV, nach zehn Schritten 0,614 V gegen exakt 0,632 V. Im Zeitschritt wird der Kondensator zu einem Leitwert, und seine Vorgeschichte steht als Stromquelle auf der rechten Seite.
:::

**Die Akteure:**

- __$U_n$__, __$I_n$__: Spannung und Strom des Kondensators zum Zeitpunkt $t_n$, beide von a nach b gezählt.
- __$G_C$__: Leitwert des Begleitmodells, $C/h$; 10 mS bei 100 nF und 10 µs; üblich ist auch $G_\mathrm{eq}$.

**Das Zusammenspiel:**

**Schritt 1**: Der Strom des Kondensators ist die Änderung seiner Ladung $CU$.

**Schritt 2**: Das implizite Euler-Verfahren braucht die Steigung der Spannung am Schrittende; dort ist sie der unbekannte Strom geteilt durch $C$.

**Schritt 3**: Nach dem Strom aufgelöst, bleibt der Strom $G_C U_{n+1}$ eines Leitwerts und der bekannte Teil $G_C U_n$, den eine Stromquelle in den Knoten a einspeist.

**Schritt 4**: Beide sind Eintragsmuster der modifizierten Knotenanalyse: der Leitwert an den vier Plätzen zwischen a und b, die Stromquelle rechts in den Zeilen a und b. Jeder Zeitschritt ist damit ein lineares Gleichungssystem wie eine Gleichstromrechnung.

**Schritt 5**: Die neue Spannung wird zur Vorgeschichte des nächsten Schritts; der Wert der Stromquelle ändert sich, bei fester Schrittweite die Matrix nicht.

:::formel Formel
$$I_{n+1} = G_C\,U_{n+1} - G_C\,U_n$$

$$G_C = \frac{C}{h}$$
:::

**So liest man das:** Je größer die Kapazität oder je kleiner der Schritt, desto größer $G_C$; in einem kurzen Schritt ändert ein Kondensator seine Spannung kaum. Für sehr große Schritte geht $G_C$ gegen null, und der Kondensator wird zum Leerlauf wie in der Gleichstromrechnung. Für eine Spule entsteht ebenso ein Leitwert, $h/L$, parallel zu einer Stromquelle, die ihren bisherigen Strom weiterführt.

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
**Gegeben:** Quelle 1 V ab $t$ = 0 über $R$ = 1 kΩ an $C$ = 100 nF; $h$ = 10 µs; $U_0$ = 0.

**Gesucht:** $U_1$, $U_2$ und $U_{10}$.

**Rechnung:** In mS, V und mA:

$$G_C = \frac{100\ \mathrm{nF}}{10\ \mu\mathrm s} = 10\ \mathrm{mS}$$

$$11\,U_{n+1} = 1 + 10\,U_n$$

$$U_1 = \frac{1}{11}\ \mathrm V = 0{,}0909\ \mathrm V, \qquad U_2 = \frac{1 + 0{,}909}{11}\ \mathrm V = 0{,}1736\ \mathrm V$$

$$U_{10} = 1\ \mathrm V\cdot\Big(1 - \big(\tfrac{10}{11}\big)^{10}\Big) = 0{,}614\ \mathrm V$$

**Ergebnis:** **90,9 mV, 173,6 mV und 0,614 V gegen exakt 0,632 V bei 0,1 ms.**

**Einordnung:** Die Folge ist die des impliziten Euler-Verfahrens; das Begleitmodell ist dieses Verfahren in Schaltungsform. Im zweiten Schritt speist die Stromquelle 0,909 mA ein, 10 mS mal 90,9 mV, und hält den Kondensator so auf seiner alten Spannung.
::::

## Eine Schaltung im Zeitschritt: die Verstärkerstufe

*Wie sieht ein Zeitschritt in einer Schaltung mit gesteuerter Quelle aus, und wie groß darf er sein?*

Die Verstärkerstufe ohne Source-Widerstand bekommt 100 fF Gate-Source-Kapazität und eine Lastkapazität von 10 pF am Drain. Bei $t$ = 0 springt die Signalspannung auf 10 mV, die umgewandelte Signalquelle speist 1 µA parallel zu 0,1 mS in das Gate. Gesucht sind die Änderungen $u_G$ und $u_D$ der Potentiale gegenüber dem Arbeitspunkt, als Kleinsignalgrößen klein geschrieben. Das Gate lädt sich mit einer Zeitkonstante von 1 ns auf 10 mV auf, der Drain folgt mit 44,4 ns gegen −44,4 mV (Abbildung 6).

:::grafik
Szene: st1/netzwerkanalyse/04-verstaerker-transiente · Vorlage: schaltbild-kurve
**Abbildung 6:** (a) Kleinsignal-Ersatzschaltbild der Stufe ohne Source-Widerstand nach dem Sprung: 1 µA parallel zu 0,1 mS am Gate, $C_{gs}$ = 100 fF, gesteuerte Quelle 1 mS, 0,225 mS und $C_L$ = 10 pF am Drain; darunter dieselbe Schaltung im Zeitschritt $h$ = 5 ns mit den Begleitmodellen 0,02 mS und 2 mS samt Stromquellen und der Matrix (0,12; 0 / 1; 2,225) mS. (b) $u_G$ und $u_D$ von 0 bis 300 ns: exakt als Kurven, das implizite Verfahren mit $h$ = 5 ns als Punkte, $u_D$ = −3,75 mV nach 5 ns gegen exakt −3,82 mV, −28,79 mV bei 50 ns gegen −29,68 mV, −44,37 mV bei 300 ns gegen −44,39 mV; Endwert −44,4 mV, Anstiegszeit von 10 % auf 90 % des Endwerts 97,7 ns. (c) Das explizite Verfahren mit derselben Schrittweite am Gate: 50 mV, −150 mV, 650 mV, −2550 mV. Die Matrix ist in jedem Schritt dieselbe; die schnelle Zeitkonstante von 1 ns macht das explizite Verfahren bei 5 ns instabil, das implizite rechnet stabil weiter.
:::

**Die Akteure:**

- __$u_{G,n}$__, __$u_{D,n}$__: die Änderungen der Potentiale von Gate und Drain zum Zeitpunkt $t_n$; in mV.
- __$C_{gs}$__, __$C_L$__: Gate-Source- und Lastkapazität, 100 fF und 10 pF; __$G_\mathrm{sig}$__: Innenleitwert der Signalquelle, 0,1 mS; __$G_D$__, __$G_L$__: Leitwerte von $R_D$ und der Last, je 0,1 mS; mit $g_o$ hat der Drain zusammen 0,225 mS.
- __$\tau_G$__, __$\tau_D$__: Zeitkonstanten von Gate und Drain.

**Das Zusammenspiel:** Jeder der beiden Knoten verhält sich wie ein RC-Glied, ein Kondensator gegen den Leitwert am Knoten, und seine Zeitkonstante ist Kapazität durch Leitwert:

$$\tau_G = \frac{C_{gs}}{G_\mathrm{sig}} = 1\ \mathrm{ns}$$

$$\tau_D = \frac{C_L}{G_D + G_L + g_o} = 44{,}4\ \mathrm{ns}$$

Beide Kondensatoren liegen gegen Masse, ihre Begleitmodelle stehen nur auf der Diagonalen; die gesteuerte Quelle trägt $g_m$ in Zeile D, Spalte G ein. Mit $h$ = 5 ns ist jeder Zeitschritt in mS, mV und µA das System:

$$\begin{pmatrix} 0{,}12 & 0 \\ 1 & 2{,}225 \end{pmatrix}\begin{pmatrix} u_{G,n+1} \\ u_{D,n+1} \end{pmatrix} = \begin{pmatrix} 1 + 0{,}02\,u_{G,n} \\ 2\,u_{D,n} \end{pmatrix}$$

Die Matrix ist in jedem Schritt dieselbe; ein Simulator eliminiert sie einmal und löst danach 60 Schritte bis 300 ns nur mit wechselnden rechten Seiten. Der Drain liegt bei 50 ns auf −28,79 mV gegen exakt −29,68 mV; der größte Fehler, 0,90 mV, sinkt mit 1 ns Schrittweite auf 0,19 mV.

Für das Gate sind 5 ns das Fünffache seiner Zeitkonstante. Das explizite Verfahren multipliziert die Abweichung dort in jedem Schritt mit −4: 50 mV, −150 mV, 650 mV, −2550 mV; stabil wäre es erst unter 2 ns, und bis 300 ns bräuchte es mehr als 150 Schritte, obwohl sich das Gate nach wenigen Nanosekunden nicht mehr ändert. Schaltungen mit so verschiedenen Zeitkonstanten heißen __steif__; in integrierten Schaltungen reichen sie von Femtosekunden bis zu Millisekunden. Simulatoren rechnen deshalb implizit, und die Schrittweite richtet sich nach der Genauigkeit des langsamen Vorgangs. Die beiden Zeitkonstanten sind die Kehrwerte der Eckkreisfrequenzen, die der Frequenzgang derselben Stufe zeigt, 10⁹ 1/s und 2,25·10⁷ 1/s.

::::beispiel Die ersten Zeitschritte der Verstärkerstufe mit 5 ns
**Gegeben:** $G_\mathrm{sig}$ = 0,1 mS, $C_{gs}$ = 100 fF, $g_m$ = 1 mS, 0,225 mS am Drain, $C_L$ = 10 pF; 1 µA ab $t$ = 0; $h$ = 5 ns.

**Gesucht:** $u_G$ und $u_D$ nach einem und nach zwei Schritten.

**Rechnung:** Begleitmodelle 0,02 mS und 2 mS; erst die Gate-Zeile, dann die Drain-Zeile, in mS, mV und µA:

$$u_{G,1} = \frac{1}{0{,}12}\ \mathrm{mV} = 8{,}333\ \mathrm{mV}, \qquad u_{D,1} = \frac{-1\cdot 8{,}333}{2{,}225}\ \mathrm{mV} = -3{,}745\ \mathrm{mV}$$

$$u_{G,2} = \frac{1 + 0{,}02\cdot 8{,}333}{0{,}12}\ \mathrm{mV} = 9{,}722\ \mathrm{mV}$$

$$u_{D,2} = \frac{2\cdot(-3{,}745) - 1\cdot 9{,}722}{2{,}225}\ \mathrm{mV} = -7{,}736\ \mathrm{mV}$$

**Ergebnis:** **Gate 8,33 mV und 9,72 mV, Drain −3,75 mV und −7,74 mV; exakt 9,93 und 10,00 mV bzw. −3,82 und −8,14 mV.**

**Einordnung:** Beim impliziten Verfahren klingt der schnelle Vorgang am Gate zu langsam ab, mit dem Faktor 1/6 je Schritt statt exakt 0,007, aber ohne zu schwingen; das explizite lieferte an derselben Stelle 50 mV und −150 mV.
::::

Enthält eine Schaltung Dioden oder Transistoren, bleibt in jedem Zeitschritt eine nichtlineare Gleichung. Ein Simulator löst sie mit dem Newton-Verfahren aus [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html), das auch diese Bauelemente durch Leitwert und Stromquelle ersetzt: Außen läuft die Zeit, innen das Newton-Verfahren, und jeder innere Durchlauf löst ein lineares Gleichungssystem. Für eine MOS-Diode, einen Transistor mit verbundenem Gate und Drain, an einer realen Stromquelle mit 0,5 mA und 0,25 mS und mit 1 nF parallel genügen bei 0,1 µs Schrittweite zwei bis vier Durchläufe je Zeitschritt.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Teststromquelle | sie ändert nur die rechte Seite und ist abgeschaltet ein Leerlauf |
| Impedanz und Übertragung | die Antwort auf einen Teststrom ist eine Spalte der Inversen |
| keine Spannungsquelle an inneren Knoten | sie würde die Matrix und damit den Arbeitspunkt verändern |
| Euler-Verfahren und Stabilität | der zeitliche Verlauf wird zu einer Folge von Schritten |
| Begleitmodell | der Kondensator wird Leitwert, seine Vorgeschichte Stromquelle auf der rechten Seite |

Die Matrix des Gleichungssystems beschreibt die Schaltung, die rechte Seite ihre Anregung: Testquellen fragen die Schaltung ab, ohne die Matrix zu verändern, und in der Zeit bringt das Begleitmodell jedes Kondensators und jeder Spule die Vorgeschichte als Stromquelle auf die rechte Seite, sodass jeder Zeitschritt wieder ein lineares Gleichungssystem ist.

## Bedeutung und Ausblick

Schaltungssimulatoren bestimmen Eingangs- und Ausgangsimpedanz, Verstärkung und Übertragung mit Testquellen in der Wechselstromanalyse und berechnen Einschwingvorgänge und Pulsantworten mit Begleitmodellen, meist mit der Trapezregel, die den Mittelwert der Steigungen am Anfang und am Ende des Schritts nimmt, und einer Schrittweite nach dem geschätzten Fehler. Eine ungeeignete Schrittweite kann Schwingungen vortäuschen oder kurze Vorgänge übergehen, und drei Kenngrößen beschreiben eine Schaltung nur ohne Rückwirkung; die vollständige Beschreibung mit vier Parametern behandelt das folgende Thema, die Vierpole.

**In der ausführlichen Fassung:** die Analogie zu Voltmeter und Amperemeter, die Verschiebung des Arbeitspunkts mit Abbildung, Beispiele zur Übertragung zwischen Knoten, das Ersatzzweitor mit Formel, Herleitung und Rückwirkungsgrenze, Beispiele zu Genauigkeit und Stabilität der Euler-Verfahren, die Trapezregel, das Begleitmodell der Spule mit Herleitung, die exakte Sprungantwort der Verstärkerstufe und die Transientenanalyse nichtlinearer Schaltungen mit Newton-Verfahren, Ablaufdiagramm und durchgerechnetem Zeitschritt. [Zur ausführlichen Fassung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/testquellen-und-transientenanalyse-ausfuehrlich.html)

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
F: Ein Teststrom von 1 µA erzeugt am Drain der Verstärkerstufe 8,90 mV. Wie groß ist die Ausgangsimpedanz, und was zeigt ein Simulator mit 1 A?
A: 8,90 kΩ; der Simulator zeigt 8901 V, zahlenmäßig die Impedanz in Ohm.
F: Stimmt es, dass man für die Ausgangsimpedanz die Eingangsquelle aus der Schaltung entfernt?
A: Nein. Eine abgeschaltete Spannungsquelle ist ein Kurzschluss und bleibt in der Matrix. Entfernt man sie im RC-Tiefpass, erhält man (0,2 − 0,6j) kΩ statt (0,333 − 0,667j) kΩ.
F: Warum speist man an einem inneren Knoten mit einer Stromquelle ein und nicht mit einer Spannungsquelle?
A: Die Spannungsquelle legt auch die Gleichspannung des Knotens fest und verschiebt den Arbeitspunkt; an der Source der Stufe ginge der Transistor in den Triodenbereich, und der Ausgangsleitwert stiege von 25 µS auf 0,648 mS. Eine Stromquelle ohne Gleichanteil ist ein Leerlauf, und die Übertragung ist dieselbe wie bei Spannungsanregung.
F: Stimmt es, dass das implizite Euler-Verfahren genauer ist als das explizite?
A: Nein. Beide sind von erster Ordnung; mit τ/10 liegen sie nach einer Zeitkonstante um +0,019 V und −0,018 V daneben. Der Vorteil des impliziten ist die Stabilität: Sein Faktor je Schritt liegt für jede Schrittweite zwischen 0 und 1, der explizite überschreitet oberhalb von 2τ den Betrag 1.
F: Warum braucht das Begleitmodell des Kondensators neben dem Leitwert $C/h$ eine Stromquelle?
A: Sie trägt die Spannung des vorigen Schritts und damit die gespeicherte Ladung weiter. Ohne sie stünde das RC-Glied mit 10 µs Schrittweite nach jedem Schritt wieder auf 90,9 mV.
:::
