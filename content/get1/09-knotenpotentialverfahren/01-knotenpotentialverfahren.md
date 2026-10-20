---
title: Das Knotenpotentialverfahren
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Knotenpotentialverfahren
order: 90100
summary: Das Gegenstück zum Maschenstromverfahren – statt umlaufender Ströme wählt man die Potenziale der Knoten als Unbekannte und baut daraus eine ebenso systematische Leitwertmatrix.
tags: Knotenpotentialverfahren, Knotenpotential, Bezugsknoten, Leitwertmatrix, Netzwerkanalyse
---

:::konzept
Das **Knotenpotentialverfahren** ist das Spiegelbild des Maschenstromverfahrens. Dort waren die Unbekannten
umlaufende Ströme, hier sind es die **Potenziale der Knoten**. Man legt einen Knoten als Nullpunkt fest und
fragt für jeden anderen: „Auf welcher Spannung liegt er?" Weil jede Zweigspannung einfach die Differenz zweier
Knotenpotenziale ist, ist die Maschenregel dann **automatisch** erfüllt — man muss nur noch die Knotenregel an
jedem Knoten ansetzen und ein Gleichungssystem lösen.
:::

**Worum es geht:** Für Netze mit vielen Zweigen zwischen wenigen Knoten ist dieses Verfahren besonders effizient.
Es führt — wie das Maschenstromverfahren — auf ein lineares Gleichungssystem in Matrixform, nur mit Leitwerten
statt Widerständen.

## Die Idee: Knotenpotenziale statt Zweigströme

Man wählt einen __Bezugsknoten__ und setzt sein __Potenzial__ auf null ($\varphi = 0$) — er ist das „Nullniveau",
gegen das alles gemessen wird. Die Unbekannten sind dann die Potenziale der übrigen $k-1$ Knoten.

Der Clou ist dual zum Maschenstromverfahren: Eine __Zweigspannung__ ist immer die Differenz zweier
Knotenpotenziale, $U = \varphi_a - \varphi_b$. Läuft man eine Masche ab, heben sich diese Differenzen von selbst
auf — die __Maschenregel__ ist also automatisch erfüllt. Es bleiben nur die $k-1$ __Knotengleichungen__.

Vorbereitung (dual zur Mascheanalyse): Alle __Spannungsquellen__ werden zuvor in __Stromquellen__ umgewandelt,
und alle Widerstände in __Leitwerte__ $G = 1/R$ umgerechnet — dann lässt sich an jedem Knoten bequem die
Strombilanz aufstellen.

:::grafik
Ein Netzwerk mit einem unten markierten Bezugsknoten ($\varphi = 0$, Masse-Symbol) und zwei darüberliegenden
Knoten mit unbekannten Potenzialen $\varphi_1, \varphi_2$. Eine Zweigspannung ist als Differenz
$\varphi_1 - \varphi_2$ beschriftet.
:::

## Die Gleichungen: die Leitwertmatrix

Auch hier eine feste Struktur. Für $k-1$ Knoten schreibt man

$$\mathbf{G}\cdot\vec{\varphi} = \vec{I},$$

mit der __Leitwertmatrix__ $\mathbf{G}$, dem Vektor der Knotenpotenziale $\vec{\varphi}$ und dem Vektor der
eingespeisten Quellenströme $\vec{I}$. Die Einträge folgen der zum Maschenstromverfahren spiegelbildlichen
Regel:

- __$G_{ii}$__ (Diagonale): die __Summe aller Leitwerte__, die an Knoten $i$ angeschlossen sind (positiv).
- __$G_{ij}$__ (außerhalb der Diagonale): der __Koppelleitwert__ zwischen Knoten $i$ und $j$, also der direkt
  verbindende Leitwert, mit **negativem** Vorzeichen.
- __$I_i$__ (rechte Seite): die __Summe der Quellenströme__, die in Knoten $i$ hineinfließen.

Wie beim Maschenstromverfahren ist die Matrix **symmetrisch** ($G_{ij} = G_{ji}$) — denn der verbindende
Leitwert zwischen zwei Knoten ist in beide Richtungen derselbe.

## Rezept und Beispiel

**Schritt 1** — Bezugsknoten wählen ($\varphi = 0$), Spannungsquellen in Stromquellen umwandeln, Widerstände in
Leitwerte $G = 1/R$ umrechnen.

**Schritt 2** — die Leitwertmatrix aufstellen. Für zwei Knoten, die über $G_2$ verbunden sind (an Knoten 1
zusätzlich $G_1$ zum Bezug und der Einspeisestrom $I_\text{q}$, an Knoten 2 zusätzlich $G_3$ zum Bezug):

$$\begin{aligned}
(G_1 + G_2)\,\varphi_1 \;-\; G_2\,\varphi_2 &= I_\text{q},\\
-\,G_2\,\varphi_1 \;+\; (G_2 + G_3)\,\varphi_2 &= 0.
\end{aligned}$$

**Schritt 3** — das Gleichungssystem nach den Knotenpotenzialen $\varphi_1, \varphi_2$ auflösen.

**Schritt 4** — die gesuchten Größen zurückgewinnen: Jede __Zweigspannung__ ist die Differenz der beteiligten
Knotenpotenziale, und der zugehörige __Zweigstrom__ folgt daraus mit dem Ohmschen Gesetz, $I = G\cdot U$.

:::grafik
Die 2×2-Leitwertmatrix des Beispiels mit hervorgehobener Struktur: Diagonale $G_1+G_2$ und $G_2+G_3$ (Summe der
Leitwerte je Knoten, positiv), Nebendiagonale $-G_2$ (Koppelleitwert, negativ), rechte Seite $I_\text{q}$ und
$0$. Daneben die Spiegelung zum Maschenstromverfahren: „R ↔ G, Masche ↔ Knoten, Strom ↔ Spannung".
:::

## Maschenstrom oder Knotenpotenzial?

Beide Verfahren lösen dasselbe Netz, sind aber unterschiedlich aufwändig. Das Maschenstromverfahren braucht
$m = z-(k-1)$ Gleichungen, das Knotenpotentialverfahren $k-1$. Man wählt das Verfahren mit den **wenigsten**
Unbekannten: bei wenigen Maschen das Maschenstromverfahren, bei wenigen Knoten (und vielen parallelen Zweigen)
das Knotenpotentialverfahren.

:::kern
Das __Knotenpotentialverfahren__ nutzt die __Knotenpotenziale__ (gegen einen __Bezugsknoten__ mit $\varphi=0$)
als Unbekannte — dadurch ist die Maschenregel automatisch erfüllt und es bleiben $k-1$ Gleichungen. Nach
Umwandlung aller Spannungsquellen in Stromquellen und der Widerstände in Leitwerte schreibt man
$\mathbf{G}\,\vec{\varphi} = \vec{I}$ mit $G_{ii}$ = Summe der Leitwerte am Knoten, $G_{ij}$ = −(Koppelleitwert),
$I_i$ = Summe der eingespeisten Ströme; die Matrix ist symmetrisch. Es ist das **Duale** zum
Maschenstromverfahren (R↔G, Masche↔Knoten) — man wählt das Verfahren mit den wenigsten Unbekannten.
:::

Damit sind die systematischen Verfahren für Gleichstromnetze abgeschlossen. Die folgenden Kapitel verlassen die
reinen Widerstandsnetze und wenden sich den __Halbleiterbauelementen__ zu — zuerst der Diode.

:::quiz
F: Was sind beim Knotenpotentialverfahren die Unbekannten?
A: Die Potenziale der Knoten, gemessen gegen einen frei gewählten Bezugsknoten mit $\varphi=0$. Statt Strömen bestimmt man also „auf welcher Spannung" jeder Knoten liegt.
F: Warum ist die Maschenregel beim Knotenpotentialverfahren automatisch erfüllt?
A: Jede Zweigspannung ist die Differenz zweier Knotenpotenziale ($U=\varphi_a-\varphi_b$). Läuft man eine Masche ab, heben sich diese Differenzen von selbst auf, sodass keine Maschengleichung mehr nötig ist.
F: Wozu dient der Bezugsknoten?
A: Er legt das Nullniveau fest ($\varphi=0$), gegen das alle anderen Potenziale gemessen werden. Ohne diesen Bezugspunkt wären nur Differenzen definiert und das System unterbestimmt.
F: Warum wandelt man vorab Spannungsquellen in Stromquellen und Widerstände in Leitwerte um?
A: Das Verfahren bilanziert an jedem Knoten Ströme (Knotenregel), und Stromquellen plus Leitwerte fügen sich direkt in diese Strombilanz ein. $I=G\,U$ macht die Gleichungen linear in den Potenzialen.
F: Was bedeutet der Diagonaleintrag $G_{ii}$ der Leitwertmatrix?
A: Die Summe aller Leitwerte, die an Knoten $i$ angeschlossen sind, mit positivem Vorzeichen. Sie geben an, wie „stark" der Knoten mit seiner Umgebung verbunden ist.
F: Was bedeutet der Außerdiagonaleintrag $G_{ij}$, und warum negativ?
A: Er ist der Koppelleitwert, der die Knoten $i$ und $j$ direkt verbindet, und steht mit Minuszeichen. Das Vorzeichen folgt daraus, dass ein höheres Nachbarpotenzial Strom in den Knoten treibt.
F: Warum ist auch die Leitwertmatrix symmetrisch?
A: Der verbindende Leitwert zwischen zwei Knoten ist in beide Richtungen derselbe, also $G_{ij}=G_{ji}$. Wie beim Maschenstromverfahren dient die Symmetrie als Kontrolle.
F: Wie gewinnt man nach dem Lösen die Zweigströme zurück?
A: Jede Zweigspannung ist die Differenz der beteiligten Knotenpotenziale, und daraus folgt der Strom mit $I=G\,U$. So rechnet man von den Potenzialen auf alle gesuchten Zweiggrößen zurück.
F: In welchem Sinn ist das Knotenpotential- das Duale zum Maschenstromverfahren?
A: Es vertauscht systematisch die Rollen: Widerstand ↔ Leitwert, Masche ↔ Knoten, Maschenstrom ↔ Knotenpotenzial. Beide führen auf eine symmetrische Matrixgleichung mit derselben Bauregel.
F: Nach welchem Kriterium wählt man zwischen den beiden Verfahren?
A: Nach der kleineren Zahl von Unbekannten: Das Maschenstromverfahren braucht $m=z-(k-1)$ Gleichungen, das Knotenpotentialverfahren $k-1$. Bei wenigen Maschen nimmt man ersteres, bei wenigen Knoten (vielen parallelen Zweigen) letzteres.
:::
