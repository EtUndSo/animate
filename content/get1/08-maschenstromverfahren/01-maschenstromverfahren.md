---
title: Das Maschenstromverfahren
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Maschenstromverfahren
order: 80100
summary: Von Grund auf – warum man ein lineares Netz statt mit allen Zweigströmen mit wenigen umlaufenden Maschenströmen berechnen kann, wie man die Gleichungen ohne Nachdenken aus dem Schaltbild abliest und warum das System immer lösbar ist. Leitbild sind Ringströme in einem Rohrnetz, die die Kontinuität an jedem Knoten von selbst erfüllen. Mit Zweigströmen als Summen von Maschenströmen, dem Verfahren in vier Schritten, der Widerstandsmatrix samt Vorzeichenregeln für Kopplungen und Quellen, ihrer Symmetrie und Lösbarkeit, der Cramerschen Regel für eine einzelne Größe und dem Umgang mit realen und idealen Stromquellen. Mit Beispiel-Seite.
tags: Maschenstromverfahren, Maschenstrom, Widerstandsmatrix, Netzwerkanalyse, Kirchhoff
---

## Anschaulich

Ein Netz mit $z$ Zweigen und $k$ Knoten hat $z$ unbekannte Zweigströme. Mit Knoten- und Maschenregel, wie im Artikel über die Kirchhoffschen Gesetze,
braucht man dafür $k - 1$ Knotengleichungen und $z - k + 1$ Maschengleichungen, zusammen $z$ Gleichungen. Das __Maschenstromverfahren__ kommt mit den
Maschengleichungen allein aus: Es wählt die Unbekannten so, dass die Knotenregel von selbst erfüllt ist.

**Das Leitbild dieses Artikels:** **Ringströme im Rohrnetz.** Ein Rohrnetz mit mehreren Schleifen, angetrieben von Pumpen. Statt für jedes Rohr einen
eigenen Durchfluss zu suchen, denkt man sich in jeder Schleife einen __Ringstrom__, Wasser, das die Schleife einmal ganz umläuft. Der Durchfluss in einem
Rohr ist dann die Summe der Ringströme der Schleifen, an denen es liegt, mit Vorzeichen je nach Drehsinn. Wasserbauer rechnen verzweigte Rohrnetze tatsächlich
so, nach einem Verfahren von Hardy Cross; weil echte Rohre nicht linear sind, iterieren sie, während bei linearen Rohren ein einziges Gleichungssystem genügt.

Drei Folgerungen:

- **Kontinuität gratis.** Ein Ringstrom fließt in jeden Knoten, den er durchläuft, hinein und wieder hinaus. An keinem Knoten sammelt sich Wasser, ganz
  gleich, wie stark die Ringströme sind.
- **Gemeinsame Rohre führen Summen.** Ein Rohr zwischen zwei Schleifen führt beide Ringströme; laufen sie dort in dieselbe Richtung, addieren sie sich,
  sonst subtrahieren sie sich.
- **Eine Gleichung pro Schleife.** Was noch fehlt, ist der Druck: Um jede Schleife herum muss der Druck wieder aufgehen. Das ist eine Gleichung je Schleife,
  so viele wie unbekannte Ringströme.

:::grafik
Szene: get1/maschenstromverfahren/01-ringstroeme · Vorlage: ringstroeme-rohrnetz
Ein Rohrnetz mit drei Schleifen nebeneinander, links eine Pumpe. In jeder Schleife ein umlaufender, halbtransparenter Ring aus Wasserteilchen mit eigenem
Drehsinn und einem Regler für seine Stärke. Die Rohre, die zu zwei Schleifen gehören, zeigen als Pfeil die Summe beziehungsweise den Unterschied der beiden
Ringe. An jedem Knoten eine Bilanzanzeige, die bei jeder Reglerstellung null zeigt. Ein Knopf „Druck prüfen" färbt jede Schleife grün, sobald der Druck
um sie herum aufgeht; erst bei einer einzigen Stellung aller drei Regler sind alle grün. Kernaussage: Ringströme erfüllen die Kontinuität von selbst, und
eine Druckbilanz je Schleife legt sie fest. (Blau = Wasser und Ringe, rot = Pumpe, orange = Summen in gemeinsamen Rohren, grau = Rohrnetz.)
:::

## Warum weniger Gleichungen genügen

Ein __Maschenstrom__ ist ein gedachter Strom, der eine Masche vollständig umläuft. Man wählt dafür so viele __unabhängige Maschen__, wie das Netz hat — nach
dem Artikel über topologische Grundbegriffe genau $m$ gleich $z - k + 1$, etwa die Maschen, die je ein Verbindungszweig eines vollständigen Baums schließt,
oder bei einem eben gezeichneten Netz die __Fenster__, die Flächen zwischen den Zweigen. In jede legt man einen Maschenstrom $I_\nu$ mit beliebigem
Umlaufsinn. Jeder Zweigstrom ist dann eine Summe von Maschenströmen:

:::formel Satz
$$I_j = \sum_{\nu=1}^{m} c_{\nu j}\,I_\nu, \qquad c_{\nu j} = \begin{cases} +1, & j \text{ in Zählrichtung durchlaufen}, \\ -1, & j \text{ entgegen durchlaufen}, \\ \ \ 0, & j \text{ nicht in Masche } \nu. \end{cases}$$
:::

**So liest man das:** Die Zahlen $c_{\nu j}$ sind die Einträge des Maschenvektors aus dem Artikel über topologische Grundbegriffe. Ein Zweig, der nur zu
einer Masche gehört, führt deren Maschenstrom, mit Vorzeichen; ein Zweig, der zwei Maschen trennt, führt die Summe oder Differenz der beiden. Mit
Maschenströmen ist die Knotenregel an jedem Knoten automatisch erfüllt, gleichgültig, welche Werte sie haben. Es bleiben die $m$ Maschengleichungen, eine
je Masche, für $m$ Unbekannte.

**Im Bild:** Der Durchfluss in einem Rohr ist die Summe der Ringströme, die es benutzen.

:::herleitung
**Knotenregel von selbst.** Ein Maschenstrom läuft auf einem geschlossenen Weg. Durchquert er einen Knoten, kommt er auf einem Zweig an und verlässt ihn auf
einem anderen; in der Knotenbilanz steht er einmal mit Plus und einmal mit Minus. Die Summe aller Zweigströme an einem Knoten ist also für jede Wahl der
Maschenströme null.

**Jede Lösung lässt sich so schreiben.** Wählt man die Maschen über einen vollständigen Baum, gehört jeder Verbindungszweig zu genau einer Masche. Seinen
Strom übernimmt der Maschenstrom dieser Masche. Die Ströme der Baumzweige folgen dann nach der Knotenregel eindeutig aus den Verbindungszweigen, wie im
Artikel über die Kirchhoffschen Gesetze; sie sind deshalb dieselben Summen von Maschenströmen. Die richtige Lösung des Netzes hat also eine Darstellung mit
Maschenströmen, und gesucht sind nur noch diese $m$ Zahlen.

**Weniger Gleichungen.** Die Knotengleichungen sind erfüllt, übrig bleiben die $m$ Maschengleichungen für $m$ Maschenströme statt $z$ Gleichungen für $z$
Zweigströme. Im Bild: Wer mit Ringströmen rechnet, muss die Kontinuität nicht mehr prüfen, nur noch den Druck.
:::

::::beispiel Die Brücke, gezählt und in Maschenströmen
Die Brücke aus dem Artikel über die Stern-Dreieck-Transformation, mit der Quelle zwischen B und A:

$$U_q = 32\,\text{V}, \qquad R_{12} = 10\,\Omega, \qquad R_{31} = 20\,\Omega, \qquad R_{23} = 20\,\Omega, \qquad R_{2B} = 26\,\Omega, \qquad R_{3B} = 12\,\Omega.$$

Hier ist A der Knoten 1, 2 und 3 sind die beiden Mittelknoten.

**Zählen.** Sechs Zweige, fünf Widerstände und die Quelle, und vier Knoten. Mit Zweigströmen wären es sechs Gleichungen, mit Maschenströmen

$$m = z - k + 1 = 6 - 4 + 1 = 3.$$

**Drei Fenster.** Die Quelle ist links neben der Brücke gezeichnet. Fenster a liegt zwischen Quelle und linker Brückenhälfte, Fenster b ist das obere
Dreieck aus $R_{12}$, $R_{23}$ und $R_{31}$, Fenster c das untere aus $R_{23}$, $R_{3B}$ und $R_{2B}$; alle drei Maschenströme laufen im Uhrzeigersinn. Die
Zweigströme, jeweils von A nach unten und von 2 nach 3 gezählt:

$$I_{12} = I_a - I_b, \qquad I_{2B} = I_a - I_c, \qquad I_{31} = I_b, \qquad I_{3B} = I_c, \qquad I_{23} = I_c - I_b.$$

**Knotenregel von selbst.** Am Knoten 2 fließt $I_{12}$ zu, $I_{2B}$ und $I_{23}$ fließen ab:

$$(I_a - I_b) - (I_a - I_c) - (I_c - I_b) = 0,$$

für alle Werte der drei Maschenströme.

**Im Bild:** Drei Ringströme, einer um die Pumpe und die linke Hälfte, zwei in den Dreiecken; die Rohre zwischen ihnen führen Unterschiede.
::::

## Das Verfahren in vier Schritten

Das Skript fasst das Vorgehen in vier Schritten zusammen:

1. Stromquellen werden in Spannungsquellen umgewandelt, wie im Artikel über ideale und reale Quellen; das Skript verweist dafür auf Kapitel 2.4.1, gemeint
   ist Abschnitt 7.4.2. Was mit idealen Stromquellen geschieht, behandelt ein eigener Abschnitt unten.
2. Man wählt $m$ gleich $z - k + 1$ unabhängige Maschen und legt in jede einen Maschenstrom; sein Umlaufsinn ist beliebig und zugleich der Umlaufsinn der
   Masche.
3. Für jede Masche stellt man die Maschenregel auf, mit den Zweigströmen als Summen von Maschenströmen.
4. Man löst das Gleichungssystem nach den Maschenströmen und berechnet daraus die gesuchten Zweigströme.

Das Gleichungssystem hat immer dieselbe Gestalt, die man direkt aus dem Schaltbild ablesen kann (Gleichung 8.1 des Skripts):

:::formel
$$\begin{pmatrix} R_{11} & R_{12} & \cdots & R_{1m} \\ R_{21} & R_{22} & \cdots & R_{2m} \\ \vdots & \vdots & \ddots & \vdots \\ R_{m1} & R_{m2} & \cdots & R_{mm} \end{pmatrix}\begin{pmatrix} I_1 \\ I_2 \\ \vdots \\ I_m \end{pmatrix} = \begin{pmatrix} U_{q1} \\ U_{q2} \\ \vdots \\ U_{qm} \end{pmatrix}.$$
:::

**So liest man das:** Die __Widerstandsmatrix__ $\mathbf R$, eine $m\times m$-Matrix, im Skript als Impedanzmatrix $\mathbf Z$ geschrieben, entsteht nach drei
Regeln:

- Auf der Diagonale steht der __Umlaufwiderstand__ $R_{\nu\nu}$, die Summe aller Widerstände der Masche $\nu$.
- Neben der Diagonale steht der __Koppelwiderstand__ $R_{\nu\mu}$ der Widerstände, die die Maschen $\nu$ und $\mu$ gemeinsam haben: positiv, wenn beide
  Maschenströme sie in derselben Richtung durchfließen, negativ, wenn in entgegengesetzter, null, wenn die Maschen keinen Zweig teilen.
- Rechts steht $U_{q\nu}$, die Summe der Quellenspannungen der Masche $\nu$, jede mit umgekehrtem Vorzeichen, wenn ihr Zählpfeil mit dem Umlaufsinn
  übereinstimmt, und mit ihrem eigenen, wenn er ihm entgegen zeigt.

Die Indizes zählen hier Maschen, nicht Knoten; $R_{12}$ in der Matrix ist ein anderes Ding als ein Bauteil namens $R_{12}$ in einem Beispiel. Die Matrix
des Skript-Beispiels zu Bild 8.1, die dort angekündigt wird, aber fehlt, lautet mit den Maschenströmen $I_1$, $I_2$, $I_3$:

$$\begin{pmatrix} R_1 + R_4 & R_4 & 0 \\ R_4 & R_2 + R_4 + R_5 & -R_5 \\ 0 & -R_5 & R_3 + R_5 \end{pmatrix}\begin{pmatrix} I_1 \\ I_2 \\ I_3 \end{pmatrix} = \begin{pmatrix} U_{q1} \\ 0 \\ U_{q3} \end{pmatrix};$$

die Gleichung 8.2 dort wiederholt nur 8.1.

**Im Bild:** Der Druckverlust um eine Schleife besteht aus dem Verlust des eigenen Ringstroms in allen ihren Rohren und aus den Anteilen der Nachbarringe in
den gemeinsamen Rohren; die Pumpen der Schleife halten dagegen.

:::herleitung
**Die Maschenregel mit Maschenströmen.** In Masche $\nu$ trägt jeder ihrer Zweige $j$ den Spannungsabfall $R_jI_j$ bei, mit $c_{\nu j}$ als Vorzeichen je nach
Umlaufrichtung, dazu die Quellenspannung $U_{qj}$ des Zweigs, die hier in der Zählrichtung des Zweigs gemessen wird. Die Maschenregel und der Satz von oben:

$$\sum_j c_{\nu j}\,\big(R_j\,I_j + U_{qj}\big) = 0, \qquad I_j = \sum_\mu c_{\mu j}\,I_\mu.$$

**Sortieren.** Eingesetzt und nach den Maschenströmen geordnet:

$$\sum_\mu \Big(\sum_j c_{\nu j}\,c_{\mu j}\,R_j\Big)\,I_\mu = -\sum_j c_{\nu j}\,U_{qj}, \qquad R_{\nu\mu} = \sum_j c_{\nu j}\,c_{\mu j}\,R_j.$$

**Die drei Regeln.** Für $\mu$ gleich $\nu$ ist $c_{\nu j}^2$ eins für jeden Zweig der Masche: die Summe ihrer Widerstände. Für zwei verschiedene Maschen bleiben
nur gemeinsame Zweige, und das Produkt $c_{\nu j}c_{\mu j}$ ist $+1$ bei gleicher und $-1$ bei entgegengesetzter Durchlaufrichtung. Rechts steht die Quelle mit
$-c_{\nu j}$: Zeigt ihr Pfeil mit dem Umlaufsinn, ändert sie das Vorzeichen, sonst nicht. Im Bild: Die Pumpe, die mit dem Ringstrom schiebt, steht auf der
anderen Seite der Bilanz.
:::

::::beispiel Ladegerät und Batterie mit zwei Maschenströmen
Ladegerät und Batterie am Kühlschrank aus dem Artikel über das Superpositionsverfahren: Ladegerät mit $U_{q1}$ und $R_{q1}$ links, Last $R_L$ in der Mitte,
Batterie mit $U_{q2}$ und $R_{q2}$ rechts, alle Pluspole oben:

$$U_{q1} = 14\,\text{V}, \qquad R_{q1} = 0{,}5\,\Omega, \qquad R_L = 2\,\Omega, \qquad U_{q2} = 12\,\text{V}, \qquad R_{q2} = 0{,}1\,\Omega.$$

Drei Zweige und zwei Knoten ergeben zwei Maschen, die beiden Fenster: $I_1$ links, $I_2$ rechts, beide im Uhrzeigersinn.

**Die Matrix aus dem Schaltbild.** Umlaufwiderstände $2{,}5\,\Omega$ und $2{,}1\,\Omega$, Koppelwiderstand $R_L$ mit Minus, weil $I_1$ ihn abwärts und $I_2$ ihn
aufwärts durchfließt. Rechts: $U_{q1}$ zeigt abwärts, gegen den Umlauf links, also $+14\,\text{V}$; $U_{q2}$ zeigt abwärts, mit dem Umlauf rechts, also
$-12\,\text{V}$:

$$\begin{pmatrix} 2{,}5 & -2 \\ -2 & 2{,}1 \end{pmatrix}\Omega\begin{pmatrix} I_1 \\ I_2 \end{pmatrix} = \begin{pmatrix} 14 \\ -12 \end{pmatrix}\text{V}.$$

**Lösen.** Die erste Gleichung nach $I_1$ aufgelöst und eingesetzt:

$$I_1 = \frac{14\,\text{V} + 2\,\Omega\cdot I_2}{2{,}5\,\Omega}, \qquad 0{,}5\,\Omega\cdot I_2 = -0{,}8\,\text{V}, \qquad I_2 = -1{,}6\,\text{A}, \qquad I_1 = 4{,}32\,\text{A}.$$

**Zurück zu den Zweigen.** Das Ladegerät liefert $4{,}32\,\text{A}$; durch die Last fließen $I_1 - I_2$, also $5{,}92\,\text{A}$ an $11{,}84\,\text{V}$; die
Batterie, abwärts durchlaufen von $I_2$, liefert aufwärts $1{,}6\,\text{A}$ — genau das Ergebnis der Überlagerung. Mit dem Umlaufsinn rechts umgedreht wird
$I_2$ zu $+1{,}6\,\text{A}$, der Koppelwiderstand positiv und $U_{q2}$ positiv; die Zweigströme bleiben dieselben.

**Im Bild:** Zwei Ringströme um zwei Pumpen; das gemeinsame Rohr in der Mitte führt ihren Unterschied.
::::

## Warum die Matrix symmetrisch und das System lösbar ist

Zwei Eigenschaften der Widerstandsmatrix machen das Verfahren zuverlässig, und das Skript nennt die erste: Koppelwiderstände, die spiegelbildlich zur
Diagonale liegen, sind gleich. Die zweite steht dort nicht, ist aber der Grund, warum man nie ein unlösbares System erhält: Die Matrix ist __positiv definit__.

:::formel Satz
$$R_{\nu\mu} = R_{\mu\nu}, \qquad \sum_{\nu,\mu} R_{\nu\mu}\,I_\nu\,I_\mu = \sum_j R_j\,I_j^2 > 0.$$
:::

**So liest man das:** Die Symmetrie ist eine Probe beim Aufstellen. Die Doppelsumme über alle Paare von Maschen ist die Leistung, die alle Widerstände
zusammen umsetzen, und die ist positiv, sobald nicht alle Maschenströme null sind. Daraus folgt, dass das Gleichungssystem für jede rechte Seite genau eine Lösung hat. Ein nützlicher
Kniff: Wählt man in einem eben gezeichneten Netz alle Maschenströme im selben Drehsinn, laufen zwei benachbarte Fenster im gemeinsamen Zweig immer
gegeneinander, und alle Koppelwiderstände werden negativ oder null. Das Skript wählt in Bild 8.1 gemischte Drehsinne, deshalb steht dort $R_4$ mit Plus.

**Im Bild:** Jedes Rohr, das zwei Schleifen teilen, gehört zu beiden Druckbilanzen gleich stark; und Ringströme, die irgendwo fließen, erwärmen die Rohre
immer, nie kühlen sie sie.

:::herleitung
**Symmetrie.** Nach der Herleitung oben ist $R_{\nu\mu}$ die Summe der $c_{\nu j}c_{\mu j}R_j$, und dieses Produkt ändert sich nicht, wenn man $\nu$ und $\mu$
vertauscht.

**Die Leistung.** Setzt man $R_{\nu\mu}$ ein und zieht die Summe über die Zweige nach außen, steht in jedem Zweig das Quadrat seines Stroms:

$$\sum_{\nu,\mu} R_{\nu\mu}\,I_\nu I_\mu = \sum_j R_j\Big(\sum_\nu c_{\nu j}I_\nu\Big)\Big(\sum_\mu c_{\mu j}I_\mu\Big) = \sum_j R_j\,I_j^2.$$

Sie ist null nur, wenn alle Zweigströme null sind; dann sind auch alle Maschenströme null, denn jeder ist der Strom eines Verbindungszweigs.

**Eindeutig lösbar.** Wäre $\mathbf R$ nicht umkehrbar, gäbe es Maschenströme, nicht alle null, für die alle linken Seiten der Gleichungen verschwinden.
Multipliziert man jede linke Seite mit ihrem Maschenstrom und addiert, erhält man genau die Leistung, und die wäre dann null — ein Widerspruch. Also ist
$\mathbf R$ umkehrbar, und jede rechte Seite hat genau eine Lösung.
:::

Um eine einzelne Größe zu berechnen, muss man nicht das ganze System lösen, wie das Skript betont. Die __Cramersche Regel__ aus der linearen Algebra gibt jeden
Maschenstrom als Quotienten zweier Determinanten: im Nenner die der Widerstandsmatrix, im Zähler die einer Matrix, in der die Spalte dieses Maschenstroms
durch die rechte Seite ersetzt ist.

$$I_\nu = \frac{\det\mathbf R_\nu}{\det\mathbf R}.$$

:::herleitung
**Für zwei Maschen.** Multipliziert man die erste Gleichung mit $R_{22}$, die zweite mit $R_{12}$ und zieht ab, fällt $I_2$ heraus:

$$(R_{11}R_{22} - R_{12}R_{21})\,I_1 = U_{q1}R_{22} - U_{q2}R_{12}, \qquad I_1 = \frac{\det\begin{pmatrix} U_{q1} & R_{12} \\ U_{q2} & R_{22} \end{pmatrix}}{\det\mathbf R}.$$

Für größere Systeme beweist die lineare Algebra dasselbe; die Rechnung bleibt ein Eliminieren der übrigen Unbekannten.
:::

::::beispiel Die Brücke, ganz gelöst
Die Brücke von oben mit den drei Maschenströmen im Uhrzeigersinn:

$$U_q = 32\,\text{V}, \qquad R_{12} = 10\,\Omega, \qquad R_{31} = 20\,\Omega, \qquad R_{23} = 20\,\Omega, \qquad R_{2B} = 26\,\Omega, \qquad R_{3B} = 12\,\Omega.$$

**Die Matrix aus dem Schaltbild.** Umlaufwiderstände $36\,\Omega$, $50\,\Omega$ und $58\,\Omega$; Koppelwiderstände $-10\,\Omega$ zwischen a und b, $-26\,\Omega$
zwischen a und c, $-20\,\Omega$ zwischen b und c; die Quelle zeigt gegen den Umlauf von a:

$$\begin{pmatrix} 36 & -10 & -26 \\ -10 & 50 & -20 \\ -26 & -20 & 58 \end{pmatrix}\Omega\begin{pmatrix} I_a \\ I_b \\ I_c \end{pmatrix} = \begin{pmatrix} 32 \\ 0 \\ 0 \end{pmatrix}\text{V}.$$

Symmetrisch, und alle Koppelwiderstände negativ, wie es der gleiche Drehsinn verlangt.

**Nach Cramer.** Die Determinante der Matrix und die drei Zählerdeterminanten:

$$\det\mathbf R = 40\,000\,\Omega^3, \qquad I_a = \frac{80\,000}{40\,000}\,\text{A} = 2\,\text{A}, \qquad I_b = \frac{35\,200}{40\,000}\,\text{A} = 0{,}88\,\text{A}, \qquad I_c = \frac{48\,000}{40\,000}\,\text{A} = 1{,}2\,\text{A}.$$

**Die Zweigströme:**

$$I_{12} = 1{,}12\,\text{A}, \qquad I_{31} = 0{,}88\,\text{A}, \qquad I_{23} = 0{,}32\,\text{A}, \qquad I_{2B} = 0{,}8\,\text{A}, \qquad I_{3B} = 1{,}2\,\text{A}.$$

Das sind dieselben Werte wie mit der Stern-Dreieck-Umwandlung.

**Probe mit der Leistung.** Die Quelle gibt $32\,\text{V}\cdot2\,\text{A}$ ab, die Widerstände nehmen zusammen dasselbe auf, die positive Summe aus dem Satz:

$$10\cdot1{,}12^2 + 20\cdot0{,}88^2 + 20\cdot0{,}32^2 + 26\cdot0{,}8^2 + 12\cdot1{,}2^2 = 64\,\text{W}.$$

**Im Bild:** Drei Ringströme von $2$, $0{,}88$ und $1{,}2\,\text{A}$; jedes Rohr führt die Summe der Ringe, die es teilen, und die Pumpe gibt genau die Wärme
aller Rohre her.
::::

:::grafik
Szene: get1/maschenstromverfahren/01-brueckenmaschen · Vorlage: maschenstrom-matrix
Die Brücke als Raute: A oben, B unten, Knoten 2 links und 3 rechts, $R_{12} = 10\,\Omega$, $R_{31} = 20\,\Omega$, $R_{23} = 20\,\Omega$ waagrecht, $R_{2B} = 26\,\Omega$,
$R_{3B} = 12\,\Omega$; links daneben die Quelle mit $32\,\text{V}$, Pluspol an A. In den drei Fenstern kreisförmige Pfeile $I_a$, $I_b$, $I_c$ im Uhrzeigersinn.
Rechts die $3\times3$-Matrix, die sich Eintrag für Eintrag füllt: Fährt man über einen Diagonaleintrag, leuchten alle Widerstände seiner Masche auf, über einen
Koppelwiderstand der gemeinsame Zweig mit den beiden gegenläufigen Pfeilen. Ein Knopf „lösen" zeigt die Maschenströme und darauf die Zweigströme als Summen,
mit $0{,}32\,\text{A}$ durch die Brücke. Kernaussage: Die Matrix lässt sich direkt aus dem Schaltbild ablesen, ihre Lösung liefert alle Zweigströme. (Rot =
Quelle, blau = Maschenströme, orange = Matrixeinträge und gemeinsame Zweige, grau = Widerstände.)
:::

## Stromquellen im Netz

Das Skript verlangt, alle Stromquellen vorab in Spannungsquellen umzuwandeln. Das geht für eine __reale__ Stromquelle, eine ideale mit einem Innenwiderstand
parallel: Sie wird zur Spannungsquelle mit der Spannung $I_q R_q$ und demselben Widerstand in Reihe. Eine __ideale__ Stromquelle hat keinen Innenwiderstand und
lässt sich nicht umwandeln. Man legt die Maschen dann so, dass nur eine einzige durch ihren Zweig läuft, etwa indem man ihn zum Verbindungszweig eines Baums
macht. Der Maschenstrom dieser Masche ist dann bekannt, und ihre Maschengleichung braucht man nicht:

$$I_\nu = \pm I_q.$$

**So liest man das:** Das Vorzeichen gibt an, ob der Umlaufsinn der Masche mit dem Pfeil der Stromquelle übereinstimmt. In den übrigen Maschengleichungen
steht dieser bekannte Maschenstrom mit seinem Koppelwiderstand und wandert auf die rechte Seite. Die Gleichung der Masche durch die Stromquelle enthält die
unbekannte Spannung an der Stromquelle und dient nur noch dazu, diese zu berechnen. Jede ideale Stromquelle spart so eine Unbekannte.

**Im Bild:** Eine Spritzenpumpe in einem Rohr legt den Durchfluss dort fest; läuft nur ein Ringstrom durch dieses Rohr, ist er gleich diesem Durchfluss.

:::herleitung
**Ein Zweig, eine Masche.** Nach dem Satz über Zweigströme ist der Strom im Zweig der Stromquelle die Summe der Maschenströme, die ihn durchlaufen. Läuft nur
die Masche $\nu$ hindurch, bleibt $c_{\nu j}I_\nu$, und das muss der Quellstrom sein; mit $c_{\nu j}$ gleich $\pm1$ folgt die Formel.

**Die überzählige Gleichung.** An einer idealen Stromquelle stellt sich jede Spannung ein. In der Maschengleichung ihrer Masche steht diese Spannung als
weitere Unbekannte, und die Gleichung legt nur sie fest. Für die übrigen Maschenströme genügen die übrigen Gleichungen.
:::

::::beispiel Eine Spannungs- und eine Stromquelle an einem Knoten
Die Schaltung aus dem Artikel über das Superpositionsverfahren: links $U_q$ über $R_a$ zum Knoten K, in der Mitte $R_b$ von K nach Masse, rechts eine
ideale Stromquelle, die über $R_s$ den Strom $I_q$ in K schiebt:

$$U_q = 10\,\text{V}, \qquad R_a = 2\,\text{k}\Omega, \qquad R_b = 3\,\text{k}\Omega, \qquad I_q = 2\,\text{mA}, \qquad R_s = 5\,\text{k}\Omega.$$

**Die Maschen.** Masche A im linken Fenster im Uhrzeigersinn, aufwärts durch die Spannungsquelle und abwärts durch $R_b$; Masche B im rechten Fenster gegen den
Uhrzeigersinn, aufwärts durch den Zweig der Stromquelle und abwärts durch $R_b$. Nur Masche B läuft durch die Stromquelle, in ihrer Richtung:

$$I_B = I_q = 2\,\text{mA}.$$

**Eine einzige Gleichung.** Beide Maschenströme durchlaufen $R_b$ abwärts, der Koppelwiderstand ist positiv; der bekannte Teil wandert nach rechts:

$$(R_a + R_b)\,I_A + R_b\,I_B = U_q, \qquad I_A = \frac{10\,\text{V} - 3\,\text{k}\Omega\cdot2\,\text{mA}}{5\,\text{k}\Omega} = 0{,}8\,\text{mA}.$$

**Was daraus folgt.** Durch $R_b$ fließen $2{,}8\,\text{mA}$, die Knotenspannung ist $8{,}4\,\text{V}$, wie bei der Überlagerung. Die übrig gebliebene Gleichung
von Masche B ergibt die Spannung an der Stromquelle samt $R_s$:

$$U_K = 3\,\text{k}\Omega\cdot2{,}8\,\text{mA} = 8{,}4\,\text{V}, \qquad U_{Iq} = R_s\,I_q + U_K = 10\,\text{V} + 8{,}4\,\text{V} = 18{,}4\,\text{V}.$$

**Im Bild:** Der Ringstrom durch die Spritzenpumpe steht fest; nur der andere muss sich nach dem Druck richten.
::::

:::grafik
Szene: get1/maschenstromverfahren/01-stromquelle · Vorlage: masche-durch-stromquelle
Die Schaltung mit drei Zweigen zwischen K und Masse: links $U_q = 10\,\text{V}$ mit $R_a = 2\,\text{k}\Omega$, Mitte $R_b = 3\,\text{k}\Omega$, rechts die
ideale Stromquelle $I_q = 2\,\text{mA}$ mit $R_s = 5\,\text{k}\Omega$. Zwei Maschenpfeile: $I_A$ im linken Fenster im Uhrzeigersinn, $I_B$ im rechten gegen den
Uhrzeigersinn, durch die Stromquelle in ihrer Pfeilrichtung. Der Zweig der Stromquelle leuchtet, und $I_B$ wird als „bekannt: $2\,\text{mA}$" markiert. Ein
Schalter legt die Maschen falsch, sodass beide durch die Stromquelle laufen; dann erscheint eine Warnung, dass der Zweigstrom eine Summe zweier Unbekannter
ist. Kernaussage: Durch eine ideale Stromquelle nur eine Masche legen, dann ist ihr Maschenstrom bekannt. (Rot = Quellen, blau = Maschenströme, orange =
festgelegter Maschenstrom, grau = Widerstände.)
:::

## Bedeutung und Ausblick

Das Maschenstromverfahren ist ein Werkzeug für die Rechnung von Hand: Man liest die Widerstandsmatrix aus dem Schaltbild ab, prüft die Symmetrie und löst ein
kleines System. Es lohnt vor allem, wenn ein Netz wenige Maschen und überwiegend Spannungsquellen hat. Das Gegenstück ist das __Knotenpotentialverfahren__ des
nächsten Artikels: Es nimmt die $k - 1$ Potenziale der Knoten als Unbekannte und erfüllt damit die Maschenregel von selbst. Welches von beiden weniger
Gleichungen braucht, entscheidet der Vergleich von $z - k + 1$ und $k - 1$.

Schaltungssimulatoren wie SPICE arbeiten mit einer Form des Knotenpotentialverfahrens; das Skript nennt in seiner Einleitung beide Verfahren als ihre
Grundlage, sagt am Ende aber richtig, dass die Maschenstromanalyse dort nicht verwendet wird. Bei Wechselstrom bleibt das Verfahren dasselbe, mit komplexen
Widerständen in der Matrix, wie es die Schreibweise $\mathbf Z$ des Skripts schon andeutet.

:::kern
- Maschenströme umlaufen unabhängige Maschen; jeder Zweigstrom ist ihre Summe mit Vorzeichen.
- Die Knotenregel ist damit von selbst erfüllt; es bleiben $m=z-k+1$ Maschengleichungen.
- Diagonale: Umlaufwiderstand der Masche; daneben: Koppelwiderstand, positiv bei gleicher und negativ bei entgegengesetzter Durchlaufrichtung.
- Rechts: Quellenspannungen der Masche, mit Minus, wenn ihr Pfeil mit dem Umlaufsinn zeigt.
- Die Widerstandsmatrix ist symmetrisch und positiv definit; das System ist immer eindeutig lösbar.
- Alle Maschen im selben Drehsinn: Alle Koppelwiderstände sind negativ oder null.
- Einzelne Maschenströme liefert die Cramersche Regel.
- Reale Stromquellen werden umgewandelt; durch eine ideale legt man nur eine Masche, deren Strom dann bekannt ist.
:::

:::quiz
F: Warum braucht das Maschenstromverfahren weniger Gleichungen als die Rechnung mit Zweigströmen?
A: Maschenströme fließen in jeden Knoten hinein und wieder heraus, die Knotenregel ist also für beliebige Werte erfüllt. Es bleiben nur die Maschengleichungen, $m=z-k+1$ statt $z$; bei der Brücke mit sechs Zweigen und vier Knoten drei statt sechs.
F: Wie setzt sich ein Zweigstrom aus Maschenströmen zusammen, und wie sieht man die Knotenregel daran?
A: $I_j=\sum_\nu c_{\nu j}I_\nu$, mit $+1$ oder $-1$ je nach Durchlaufrichtung und $0$ für Maschen ohne diesen Zweig. In der Brücke ist $I_{23}=I_c-I_b$; am Knoten 2 ergibt $(I_a-I_b)-(I_a-I_c)-(I_c-I_b)$ für alle Werte null.
F: Wie wählt man die Maschen, und warum sind sie unabhängig?
A: Man nimmt $z-k+1$ Maschen, etwa die, die je ein Verbindungszweig eines vollständigen Baums schließt, bei einem eben gezeichneten Netz einfach die Fenster. Jede so gewählte Masche enthält einen Zweig, den keine andere hat, deshalb ist keine Maschengleichung aus den übrigen ableitbar.
F: Nach welchen Regeln liest man die Widerstandsmatrix aus dem Schaltbild ab?
A: Auf der Diagonale die Summe aller Widerstände der Masche, daneben die gemeinsamen Widerstände zweier Maschen, positiv bei gleicher, negativ bei entgegengesetzter Durchlaufrichtung. Aus $R_{\nu\mu}=\sum_jc_{\nu j}c_{\mu j}R_j$ folgen beide Regeln.
F: Mit welchem Vorzeichen stehen die Quellenspannungen rechts?
A: Zeigt der Pfeil einer Quelle mit dem Umlaufsinn, steht sie mit Minus rechts, zeigt er entgegen, mit ihrem Vorzeichen, denn sie wechselt beim Herüberbringen die Seite. Bei Ladegerät und Batterie im Uhrzeigersinn sind es $+14\,\text{V}$ links und $-12\,\text{V}$ rechts, mit den Lösungen $4{,}32\,\text{A}$ und $-1{,}6\,\text{A}$.
F: Warum ist die Widerstandsmatrix symmetrisch und das System immer lösbar?
A: $R_{\nu\mu}=\sum_jc_{\nu j}c_{\mu j}R_j$ ändert sich beim Vertauschen von $\nu$ und $\mu$ nicht. Die quadratische Form $\sum R_{\nu\mu}I_\nu I_\mu$ ist die Leistung $\sum R_jI_j^2$ und positiv, sobald ein Strom fließt; deshalb können die linken Seiten nur für verschwindende Maschenströme alle null sein, und $\mathbf R$ ist umkehrbar.
F: Wie berechnet man einen einzelnen Maschenstrom, und was ergibt das für die Brücke?
A: Mit der Cramerschen Regel, $I_\nu=\det\mathbf R_\nu/\det\mathbf R$, mit der rechten Seite an Stelle der Spalte von $I_\nu$. Für die Brücke ist $\det\mathbf R=40\,000\,\Omega^3$, und es folgen $2$, $0{,}88$ und $1{,}2\,\text{A}$; durch die Brücke fließen $0{,}32\,\text{A}$, und die Leistungsprobe ergibt $64\,\text{W}$.
F: Was ändert sich, wenn man den Umlaufsinn einer Masche umdreht?
A: Ihr Maschenstrom wechselt das Vorzeichen, ebenso ihre Koppelwiderstände und die Vorzeichen ihrer Quellen auf der rechten Seite. Die Zweigströme bleiben dieselben: Bei Ladegerät und Batterie wird $I_2$ von $-1{,}6$ zu $+1{,}6\,\text{A}$, die Ströme in Last und Batterie ändern sich nicht.
F: Wie behandelt man Stromquellen?
A: Eine reale Stromquelle wandelt man in eine Spannungsquelle um. Durch eine ideale legt man genau eine Masche, deren Strom dann der Quellstrom ist; ihre Maschengleichung liefert nur die Spannung an der Quelle. Am Knoten mit $10\,\text{V}$, $2$ und $3\,\text{k}\Omega$ und $2\,\text{mA}$ bleibt eine einzige Gleichung, mit $0{,}8\,\text{mA}$, $8{,}4\,\text{V}$ am Knoten und $18{,}4\,\text{V}$ an der Stromquelle samt Vorwiderstand.
F: Welche Unstimmigkeiten hat das Skript beim Maschenstromverfahren?
A: Für die Quellenumwandlung verweist es auf Kapitel 2.4.1, gemeint ist 7.4.2. Die Matrix des Beispiels zu Bild 8.1 wird angekündigt, fehlt aber, und Gleichung 8.2 wiederholt 8.1. Ideale Stromquellen lassen sich nicht umwandeln, wie es verlangt, und seine Einleitung nennt beide Verfahren als Grundlage von Simulatoren, während am Ende richtig steht, dass die Maschenstromanalyse dort nicht verwendet wird.
:::
