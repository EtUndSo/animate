---
title: Das Knotenpotentialverfahren
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Knotenpotentialverfahren
order: 90100
summary: Von Grund auf – warum man ein lineares Netz mit den Spannungen seiner Knoten gegen einen Bezugsknoten berechnen kann, wie man die Leitwertmatrix ohne Nachdenken aus dem Schaltbild abliest und warum das System immer lösbar ist. Leitbild sind Standrohre an den Knoten eines Rohrnetzes, deren Pegel die Druckbilanz um jede Schleife von selbst erfüllen. Mit Zweigspannungen als Differenzen, dem Verfahren in vier Schritten, den Regeln für Knoten- und Koppelleitwerte und Quellströme, Ersatzstromquellen und dem Satz von Millman, Symmetrie und Lösbarkeit, dem Vergleich mit dem Maschenstromverfahren, idealen Spannungsquellen über Bezugsknoten und Superknoten sowie dem Exkurs zu Eintragsmustern, gesteuerten Quellen, Netzlisten und der modifizierten Knotenpotentialanalyse. Mit Beispiel-Seite.
tags: Knotenpotentialverfahren, Knotenpotential, Bezugsknoten, Leitwertmatrix, Netzwerkanalyse
---

## Anschaulich

Ein Netz mit $z$ Zweigen und $k$ Knoten hat $z$ unbekannte Zweigströme. Das Maschenstromverfahren des vorigen Artikels kommt mit $z - k + 1$
Maschengleichungen aus, weil seine Unbekannten, die Maschenströme, die Knotenregel von selbst erfüllen. Das __Knotenpotentialverfahren__ geht den
umgekehrten Weg: Es nimmt die Potenziale der Knoten als Unbekannte. Damit ist die Maschenregel von selbst erfüllt, und es bleiben $k - 1$ Knotengleichungen.

**Das Leitbild dieses Artikels:** **Standrohre an den Knoten.** Dasselbe Rohrnetz wie bei den Ringströmen, mit Pumpen und Rohren verschiedener Weite. An
jeden Knoten steckt man ein senkrechtes, oben offenes Glasrohr, ein __Standrohr__. Das Wasser steigt darin so hoch, wie der Druck am Knoten es trägt; die
Höhe des Spiegels, der __Pegel__, misst den Druck. Abgelesen wird an einer gemeinsamen Nullmarke. Durch jedes Rohr fließt Wasser vom höheren zum
niedrigeren Pegel, umso mehr, je größer der Unterschied und je weiter das Rohr ist.

Wasserbauer kennen auch diese Sicht. Hardy Cross, dessen Ringstrom-Verfahren im vorigen Artikel vorkam, gab 1936 zugleich ein Verfahren an, das die
Druckhöhen an den Knoten schrittweise ausgleicht, bis an jedem Knoten so viel ab- wie zufließt.

Drei Folgerungen:

- **Druckbilanz gratis.** Wer eine Schleife abläuft und die Pegelunterschiede ihrer Rohre addiert, kommt beim Ausgangspegel wieder an. Die Summe ist
  null, wie auch immer die Pegel stehen.
- **Ein Rohr, zwei Pegel.** Der Durchfluss eines Rohres folgt aus seiner Weite und den Pegeln an seinen beiden Enden. Mehr braucht man über das Rohr nicht
  zu wissen.
- **Eine Gleichung pro Knoten.** Was noch fehlt, ist die Kontinuität: An jedem Knoten muss so viel abfließen, wie zufließt. Das ist eine Gleichung je
  Knoten außer dem an der Nullmarke, so viele, wie es unbekannte Pegel gibt.

Die Ringströme des vorigen Artikels erfüllen die Kontinuität von selbst und brauchen eine Druckbilanz je Schleife. Die Pegel erfüllen die Druckbilanz von
selbst und brauchen eine Kontinuitätsbilanz je Knoten. Die beiden Verfahren sind __dual__ zueinander: Das eine geht aus dem anderen hervor, wenn man
Knoten und Masche, Strom und Spannung, Widerstand und Leitwert vertauscht.

Die Quellen kennt man aus dem Artikel über ideale und reale Quellen. Eine Spritzenpumpe drückt einen festen Volumenstrom in einen Knoten, ganz gleich,
welcher Druck dort herrscht; das ist die ideale Stromquelle, und sie passt unmittelbar in die Kontinuitätsbilanz. Ein Wasserturm hält einen festen Pegel,
ganz gleich, wie viel entnommen wird; das ist die ideale Spannungsquelle, und für sie braucht das Verfahren einen eigenen Kniff.

:::grafik
Szene: get1/knotenpotentialverfahren/01-standrohre · Vorlage: standrohre-rohrnetz
Das Rohrnetz aus dem vorigen Artikel mit drei Schleifen, links ein Wasserturm, rechts eine Spritzenpumpe; ein Knoten unten trägt die Nullmarke. Auf jedem
anderen Knoten steht ein gläsernes Standrohr mit Wasserspiegel und einem Regler für seinen Pegel. Die Rohre zeigen den Durchfluss als Pfeil vom höheren
zum niedrigeren Pegel, seine Dicke ist Rohrweite mal Pegelunterschied. Ein Knopf „Schleife ablaufen“ fährt eine Schleife ab und addiert die
Pegelunterschiede; die Summe zeigt bei jeder Reglerstellung null. An jedem Knoten eine Bilanzanzeige „Zufluss minus Abfluss“; erst bei einer einzigen
Stellung aller Regler zeigen alle null. Kernaussage: Pegel erfüllen die Druckbilanz um jede Schleife von selbst, und eine Kontinuitätsbilanz je Knoten
legt sie fest. (Blau = Wasser und Pegel, rot = Turm und Pumpe, orange = Bilanzanzeigen und Durchflusspfeile, grau = Rohrnetz, gestrichelt = Nullmarke.)
:::

## Knotenpotenziale: die Maschenregel gratis

Nach dem Artikel über Arbeit, Potenzial und Spannung hat jeder Punkt eines Netzes ein __Potenzial__ $\varphi$, die Spannung von diesem Punkt zu einem
gewählten Bezugspunkt; die Spannung zwischen zwei Punkten ist die Differenz ihrer Potenziale. Das Netz sei zusammenhängend: Von jedem Knoten führt ein Weg
über Zweige zu jedem anderen.

Man wählt einen Knoten als __Bezugsknoten__ und gibt ihm das Potenzial null; im Schaltbild trägt er oft das Massezeichen. Er bekommt die Nummer 0, die
übrigen Knoten die Nummern 1 bis $n$, mit

$$n = k - 1.$$

Die __Knotenspannung__ $U_\nu$ des Knotens $\nu$ ist die Spannung vom Knoten $\nu$ zum Bezugsknoten, mit dem Zählpfeil vom Knoten zum Bezugsknoten. Weil
der Bezugsknoten das Potenzial null hat, ist sie zugleich das Potenzial des Knotens; deshalb heißt sie auch __Knotenpotential__:

$$U_\nu = \varphi_\nu - \varphi_0 = \varphi_\nu, \qquad \nu = 1, \dots, n.$$

**Im Bild:** Der Bezugsknoten ist die Nullmarke, $U_\nu$ die Höhe des Spiegels im Standrohr des Knotens $\nu$ über ihr. Wo man die Nullmarke anbringt, ist
gleichgültig, denn Durchflüsse hängen nur von Unterschieden ab.

Zwischen zwei Knoten $\mu$ und $\nu$ liegt ein Zweig mit dem __Leitwert__ $G_{\mu\nu}$, dem Kehrwert seines Widerstands, gemessen in Siemens (S).
Liegen mehrere Leitwerte parallel zwischen denselben Knoten, ist $G_{\mu\nu}$ ihre Summe, wie im Artikel über die Zusammenschaltung von Widerständen;
fehlt ein solcher Zweig, ist $G_{\mu\nu}$ null. Der Leitwert ist derselbe, von welcher Seite man ihn liest, und $G_{\nu0}$ ist der Leitwert vom Knoten
$\nu$ zum Bezugsknoten.

:::formel Satz
$$U_{\mu\nu} = U_\mu - U_\nu, \qquad I_{\mu\nu} = G_{\mu\nu}\,(U_\mu - U_\nu).$$
:::

**So liest man das:** $U_{\mu\nu}$ ist die Zweigspannung von $\mu$ nach $\nu$, $I_{\mu\nu}$ der Strom, der im Leitwert von $\mu$ nach $\nu$ fließt. Jede
Zweigspannung ist die Differenz zweier Knotenspannungen, und mit dem Ohmschen Gesetz folgt aus ihr der Zweigstrom. Für einen Zweig zum Bezugsknoten ist
$U_0$ null; durch $G_{\nu0}$ fließt dann der Strom $G_{\nu0}U_\nu$. Kennt man die $n$ Knotenspannungen, kennt man alle Zweigspannungen und alle Ströme in
Leitwerten. Die Maschenregel ist für jede Wahl der Knotenspannungen erfüllt.

**Im Bild:** Der Durchfluss durch ein Rohr ist seine Weite mal dem Pegelunterschied an seinen Enden.

:::herleitung
**Zweigspannung als Differenz.** Die Spannung zwischen zwei Punkten ist die Differenz ihrer Potenziale; mit $\varphi_0 = 0$ sind die Potenziale der
Knoten ihre Knotenspannungen:

$$U_{\mu\nu} = \varphi_\mu - \varphi_\nu = U_\mu - U_\nu.$$

**Maschenregel von selbst.** Eine Masche laufe über die Knoten $\nu_1, \nu_2, \dots, \nu_r$ und zurück zu $\nu_1$. Die Summe ihrer Zweigspannungen ist eine
Teleskopsumme, in der jede Knotenspannung einmal mit Plus und einmal mit Minus steht:

$$(U_{\nu_1} - U_{\nu_2}) + (U_{\nu_2} - U_{\nu_3}) + \dots + (U_{\nu_r} - U_{\nu_1}) = 0.$$

**Jede Lösung lässt sich so schreiben.** In der wirklichen Lösung des Netzes gilt die Maschenregel. Man setzt $U_\nu$ gleich der Summe der Zweigspannungen
längs eines Weges vom Knoten $\nu$ zum Bezugsknoten. Zwei verschiedene solche Wege bilden zusammen einen geschlossenen Umlauf, auf dem die Maschenregel gilt;
deshalb liefert jeder Weg denselben Wert. Dann ist jede Zweigspannung die Differenz der Werte an ihren Enden, und gesucht sind nur noch die $n$
Knotenspannungen.

**Der Zweigstrom.** Das Ohmsche Gesetz gibt den Strom im Leitwert, in der Richtung der Spannung gezählt. Im Bild: Ein Rohr weiß nichts von den übrigen
Rohren, es sieht nur die beiden Pegel an seinen Enden; und weil jeder Knoten genau einen Pegel hat, geht die Druckbilanz um jede Schleife auf.
:::

::::beispiel Die Brücke in Pegeln
Die Brücke aus den Artikeln über die Stern-Dreieck-Transformation und das Maschenstromverfahren, mit der Quelle zwischen B und A, Pluspol an A:

$$U_q = 32\,\text{V}, \qquad R_{12} = 10\,\Omega, \qquad R_{31} = 20\,\Omega, \qquad R_{23} = 20\,\Omega, \qquad R_{2B} = 26\,\Omega, \qquad R_{3B} = 12\,\Omega.$$

A ist der Knoten 1, 2 und 3 sind die beiden Mittelknoten, B wird Bezugsknoten.

**Zählen.** Vier Knoten, also drei Knotenspannungen $U_1$, $U_2$ und $U_3$ statt sechs Zweigströmen. Die Quelle hält A um $32\,\text{V}$ über B:

$$U_1 = 32\,\text{V}.$$

**Die Pegel.** Durch $R_{2B}$ und $R_{3B}$ flossen nach dem Maschenstromverfahren $0{,}8\,\text{A}$ und $1{,}2\,\text{A}$ nach B; damit liegen die
Mittelknoten auf

$$U_2 = 26\,\Omega\cdot0{,}8\,\text{A} = 20{,}8\,\text{V}, \qquad U_3 = 12\,\Omega\cdot1{,}2\,\text{A} = 14{,}4\,\text{V}.$$

**Alle übrigen Ströme aus den Pegeln.** Nach dem Satz, jeweils von A nach unten und von 2 nach 3 gezählt:

$$I_{12} = \frac{32\,\text{V} - 20{,}8\,\text{V}}{10\,\Omega} = 1{,}12\,\text{A}, \qquad I_{31} = \frac{32\,\text{V} - 14{,}4\,\text{V}}{20\,\Omega} = 0{,}88\,\text{A}, \qquad I_{23} = \frac{20{,}8\,\text{V} - 14{,}4\,\text{V}}{20\,\Omega} = 0{,}32\,\text{A}.$$

Das sind die Zweigströme aus dem vorigen Artikel.

**Maschenregel von selbst.** Um das obere Dreieck aus A, 2 und 3:

$$(U_1 - U_2) + (U_2 - U_3) + (U_3 - U_1) = 11{,}2\,\text{V} + 6{,}4\,\text{V} - 17{,}6\,\text{V} = 0.$$

Weil die Quelle zwischen A und dem Bezugsknoten liegt, ist $U_1$ schon vor jeder Rechnung bekannt; zu bestimmen sind nur zwei Knotenspannungen. Wie man
das ausnutzt, zeigt der Abschnitt über ideale Spannungsquellen.

**Im Bild:** Drei Standrohre, das an A vom Turm auf 32 gehalten, die beiden in der Mitte auf 20,8 und 14,4. Jedes Rohr führt Wasser vom höheren zum
niedrigeren Spiegel, und um jede Schleife gehen die Unterschiede auf.
::::

## Das Verfahren in vier Schritten

Das Skript gliedert das Vorgehen in vier Schritte:

1. Reale Spannungsquellen werden in reale Stromquellen umgewandelt, die Ersatzstromquellen aus dem Artikel über Ersatzquellen; Widerstände schreibt man
   als Leitwerte. Warum das nötig ist und was mit idealen Spannungsquellen geschieht, zeigen eigene Abschnitte unten.
2. Ein Knoten wird Bezugsknoten mit dem Potenzial null. Die Knotenspannungen der übrigen Knoten bekommen Zählpfeile zum Bezugsknoten; an einem Zweig, der
   den Bezugsknoten nicht berührt, steht die Differenz zweier Knotenspannungen.
3. Für die übrigen $n$ Knoten stellt man die Knotenregel auf, mit den Zweigströmen aus dem Satz oben.
4. Man löst das Gleichungssystem nach den Knotenspannungen und berechnet daraus die Zweigspannungen und Zweigströme.

Die Knotenregel am Knoten $\nu$ sagt dann: Was über die Leitwerte abfließt, speisen die Stromquellen ein. Nach den Knotenspannungen geordnet, hat das
System immer dieselbe Gestalt, die man direkt aus dem Schaltbild abliest (Gleichungen 9.1 und 9.2 des Skripts).

**Die drei Akteure:**

- der Vektor der Knotenspannungen $\vec U \in \mathbb R^n$, mit den Komponenten $U_\nu$ in Volt;
- die __Knotenleitwertmatrix__ $\mathbf Y \in \mathbb R^{n\times n}$ mit den Einträgen $Y_{\nu\mu}$ in Siemens. Das Skript nennt sie auch Admittanz- oder
  Knotenadmittanzmatrix: Eine __Admittanz__ ist ein verallgemeinerter Leitwert, der bei Wechselstrom komplex wird; in Gleichstromnetzen ist sie einfach
  der Leitwert;
- der Vektor der __Quellströme__ $\vec I_q \in \mathbb R^n$, mit den Komponenten $I_{q\nu}$ in Ampere: der gesamte Strom, den Stromquellen in den Knoten
  $\nu$ hineinschieben.

**Das Zusammenspiel:** *Welche Knotenspannungen sorgen dafür, dass an jedem Knoten genau der eingespeiste Quellstrom über die Leitwerte abfließt?*

:::formel
$$\begin{pmatrix} Y_{11} & Y_{12} & \cdots & Y_{1n} \\ Y_{21} & Y_{22} & \cdots & Y_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ Y_{n1} & Y_{n2} & \cdots & Y_{nn} \end{pmatrix}\begin{pmatrix} U_1 \\ U_2 \\ \vdots \\ U_n \end{pmatrix} = \begin{pmatrix} I_{q1} \\ I_{q2} \\ \vdots \\ I_{qn} \end{pmatrix}, \qquad \mathbf Y\,\vec U = \vec I_q.$$
:::

**So liest man das:** Eingabe sind die $n$ Knotenspannungen, ein Vektor; die Matrix macht daraus die $n$ Ströme, die an den Knoten über Leitwerte abfließen,
und die müssen gleich den Quellströmen sein. Die Matrix entsteht nach drei Regeln:

- Auf der Diagonale steht der __Knotenleitwert__ $Y_{\nu\nu}$: die Summe aller Leitwerte, die am Knoten $\nu$ angeschlossen sind, auch der zum
  Bezugsknoten.
- Neben der Diagonale steht der __Koppelleitwert__ $G_{\nu\mu}$ der beiden Knoten mit Minus, und null, wenn kein Leitwert sie direkt verbindet. Anders als
  beim Maschenstromverfahren gibt es hier keine Wahl: Das Vorzeichen ist immer negativ.
- Rechts steht $I_{q\nu}$, die Summe der Quellströme, die in den Knoten $\nu$ hineinfließen; ein Quellstrom, der aus ihm herausfließt, zählt negativ.

In Formeln, mit der Summe über alle Knoten $\mu$ außer $\nu$ selbst, den Bezugsknoten eingeschlossen:

$$Y_{\nu\nu} = \sum_{\mu \ne \nu} G_{\nu\mu}, \qquad Y_{\nu\mu} = -G_{\nu\mu}.$$

Die Einheiten passen: Siemens mal Volt ergibt Ampere. Das Skript schreibt die Einträge in der Matrix als $Y$, im Text als $G_{\nu\nu}$ und $G_{\mu\nu}$; dann
ist $G_{\mu\nu}$ zugleich Matrixeintrag und, mit umgekehrtem Vorzeichen, Koppelleitwert. Hier heißen deshalb die Einträge $Y$ und die Leitwerte der
Bauteile $G$.

**Im Bild:** Der Abfluss aus einem Knoten wächst mit seinem eigenen Pegel, durch alle angeschlossenen Rohre zugleich; das ist die Diagonale. Ein hoher
Nachbarpegel drückt Wasser zurück und verringert den Abfluss; das ist der negative Koppeleintrag. Die Pumpen speisen ein; das ist die rechte Seite.

:::herleitung
**Die Knotenregel in Knotenspannungen.** Am Knoten $\nu$ summiert man die Ströme, die über Leitwerte abfließen, und setzt sie gleich den Quellströmen, die
hineinfließen. Durch den Leitwert zum Knoten $\mu$ fließt nach dem Satz der Strom $G_{\nu\mu}(U_\nu - U_\mu)$ ab, zum Bezugsknoten mit $U_0 = 0$ der Strom
$G_{\nu0}U_\nu$:

$$\sum_{\mu \ne \nu} G_{\nu\mu}\,(U_\nu - U_\mu) = I_{q\nu}.$$

**Sortieren.** Ausmultipliziert steht $U_\nu$ mit der Summe aller angeschlossenen Leitwerte da, jede andere Knotenspannung $U_\mu$ mit $-G_{\nu\mu}$. Der
Term des Bezugsknotens trägt nur zur Summe bei, weil $U_0$ null ist:

$$\Big(\sum_{\mu \ne \nu} G_{\nu\mu}\Big)\,U_\nu - \sum_{\mu = 1,\ \mu \ne \nu}^{n} G_{\nu\mu}\,U_\mu = I_{q\nu}.$$

**Die drei Regeln.** Der Faktor vor $U_\nu$ ist der Diagonaleintrag, der vor $U_\mu$ der Koppeleintrag, die rechte Seite der Quellstrom. Das Minus hat einen
einfachen Grund: Alle Knotenspannungen zählen zum selben Bezugsknoten, und eine höhere Spannung am Nachbarknoten treibt Strom zum Knoten $\nu$ hin; das
verringert, was $\nu$ selbst abgeben muss. Im Bild: Steigt ein Nachbarpegel, fließt durch das Verbindungsrohr weniger ab.

**Warum $n$ Gleichungen genügen.** Die Knotenregel am Bezugsknoten wird nicht gebraucht. Addiert man die Knotenregeln aller $k$ Knoten, kommt jeder
Zweigstrom einmal abfließend und einmal zufließend vor, und die Summe ist null. Die Gleichung des Bezugsknotens folgt also aus den übrigen, wie im Artikel
über die Kirchhoffschen Gesetze. Im Bild: Geht die Bilanz an allen Knoten bis auf einen auf, geht sie auch am letzten auf, denn Wasser verschwindet nicht.
:::

Für eine einzelne Knotenspannung muss man, wie im vorigen Artikel, nicht das ganze System lösen. Die __Cramersche Regel__ gibt sie als Quotienten zweier
Determinanten; im Zähler steht die Determinante der Matrix $\mathbf Y_\nu$, in der die Spalte $\nu$ durch die rechte Seite ersetzt ist:

$$U_\nu = \frac{\det\mathbf Y_\nu}{\det\mathbf Y}.$$

:::herleitung
**Für zwei Knoten.** Man multipliziert die erste Gleichung mit $Y_{22}$, die zweite mit $Y_{12}$ und zieht ab; $U_2$ fällt heraus:

$$(Y_{11}Y_{22} - Y_{12}Y_{21})\,U_1 = I_{q1}Y_{22} - I_{q2}Y_{12}, \qquad U_1 = \frac{\det\begin{pmatrix} I_{q1} & Y_{12} \\ I_{q2} & Y_{22} \end{pmatrix}}{\det\mathbf Y}.$$

Für größere Systeme beweist die lineare Algebra dasselbe, wie im Artikel über das Maschenstromverfahren. Dass $\det\mathbf Y$ nicht null ist, zeigt der
Abschnitt über Symmetrie und Lösbarkeit.
:::

::::beispiel Drei Knoten, zwei Stromquellen
Ein Netz mit den Knoten 1, 2, 3 und dem Bezugsknoten 0. Die Leitwerte zwischen den Knoten und zum Bezugsknoten, also Widerstände von $1\,\text{k}\Omega$,
$500\,\Omega$, $1\,\text{k}\Omega$, $500\,\Omega$, $250\,\Omega$ und $500\,\Omega$:

$$G_{10} = 1\,\text{mS}, \qquad G_{12} = 2\,\text{mS}, \qquad G_{13} = 1\,\text{mS}, \qquad G_{23} = 2\,\text{mS}, \qquad G_{20} = 4\,\text{mS}, \qquad G_{30} = 2\,\text{mS}.$$

Die Stromquelle A schiebt einen Strom aus dem Bezugsknoten in den Knoten 1, die Stromquelle B einen aus dem Knoten 3 in den Knoten 2:

$$I_{qA} = 15\,\text{mA}, \qquad I_{qB} = 4\,\text{mA}.$$

**Die Matrix aus dem Schaltbild.** Knotenleitwerte: am Knoten 1 die Summe von $G_{10}$, $G_{12}$ und $G_{13}$, also $4\,\text{mS}$, am Knoten 2 entsprechend
$8\,\text{mS}$, am Knoten 3 $5\,\text{mS}$. Die Koppelleitwerte stehen mit Minus daneben. Rechts fließt $I_{qA}$ in den Knoten 1, $I_{qB}$ in den Knoten 2
hinein und aus dem Knoten 3 heraus:

$$\begin{pmatrix} 4 & -2 & -1 \\ -2 & 8 & -2 \\ -1 & -2 & 5 \end{pmatrix}\text{mS}\begin{pmatrix} U_1 \\ U_2 \\ U_3 \end{pmatrix} = \begin{pmatrix} 15 \\ 4 \\ -4 \end{pmatrix}\text{mA}.$$

Die Matrix ist symmetrisch, alle Koppeleinträge sind negativ.

**Nach Cramer.** Entwickelt nach der ersten Zeile, mit den Unterdeterminanten $36$, $-12$ und $12$:

$$\det\mathbf Y = 4\cdot36 - (-2)\cdot(-12) + (-1)\cdot12 = 108\,\text{mS}^3.$$

Ebenso ergeben die drei Zählerdeterminanten, in $\text{mS}^2\,\text{mA}$, die Knotenspannungen:

$$U_1 = \frac{540}{108}\,\text{V} = 5\,\text{V}, \qquad U_2 = \frac{216}{108}\,\text{V} = 2\,\text{V}, \qquad U_3 = \frac{108}{108}\,\text{V} = 1\,\text{V}.$$

**Probe an jedem Knoten.** Die Zweigströme nach dem Satz, jeweils vom ersten zum zweiten Index gezählt:

$$I_{10} = 5\,\text{mA}, \qquad I_{12} = 6\,\text{mA}, \qquad I_{13} = 4\,\text{mA}, \qquad I_{23} = 2\,\text{mA}, \qquad I_{20} = 8\,\text{mA}, \qquad I_{30} = 2\,\text{mA}.$$

An den drei Knoten geht die Bilanz auf, links jeweils der Zufluss, rechts der Abfluss:

$$I_{qA} = I_{10} + I_{12} + I_{13}, \qquad I_{12} + I_{qB} = I_{20} + I_{23}, \qquad I_{13} + I_{23} = I_{30} + I_{qB}.$$

In Zahlen sind das $15$, $10$ und $6\,\text{mA}$ auf beiden Seiten.

**Im Bild:** Drei Standrohre mit den Pegeln 5, 2 und 1. Die Pumpe B hebt Wasser vom niedrigeren Pegel 1 auf den höheren Pegel 2, gegen den Unterschied.
::::

:::grafik
Szene: get1/knotenpotentialverfahren/01-leitwertmatrix · Vorlage: knoten-matrix
Das Netz mit drei Knoten: oben nebeneinander die Knoten 1, 2 und 3, unten die Bezugsleitung 0 mit Massezeichen. Senkrecht nach unten $G_{10} = 1\,\text{mS}$,
$G_{20} = 4\,\text{mS}$ und $G_{30} = 2\,\text{mS}$; waagrecht $G_{12} = 2\,\text{mS}$ und $G_{23} = 2\,\text{mS}$; $G_{13} = 1\,\text{mS}$ als Bogen über
den Knoten 2. Links die Stromquelle A mit $15\,\text{mA}$ von 0 nach 1, zwischen 3 und 2 parallel zu $G_{23}$ die Stromquelle B mit $4\,\text{mA}$, Pfeil
von 3 nach 2. Von jedem Knoten ein Zählpfeil $U_1$, $U_2$, $U_3$ zur Bezugsleitung. Rechts die leere $3\times3$-Matrix und der Quellvektor: Fährt man über
einen Diagonaleintrag, leuchten alle Leitwerte des Knotens auf und der Eintrag füllt sich mit ihrer Summe; über einen Koppeleintrag leuchtet der
verbindende Leitwert und der Eintrag erscheint mit Minus; über einen Eintrag des Quellvektors leuchten die Quellen des Knotens, mit Plus für Pfeile hinein
und Minus für Pfeile hinaus. Ein Knopf „lösen“ lässt über den Knoten Standrohre mit den Pegeln 5, 2 und 1 V aufsteigen und zeigt an jedem Leitwert seinen
Strom. Kernaussage: Die Leitwertmatrix lässt sich Knoten für Knoten aus dem Schaltbild ablesen; ihre Lösung sind die Pegel. (Rot = Quellen, blau =
Knotenspannungen und Pegel, orange = Matrixeinträge und hervorgehobene Leitwerte, grau = Leitwerte und Bezugsleitung.)
:::

## Quellen in der Knotengleichung

Das Verfahren bilanziert Ströme. Eine ideale Stromquelle passt unmittelbar hinein: Ihr Strom hängt von keiner Knotenspannung ab und steht nur rechts. Eine
Spannungsquelle dagegen legt eine Spannung fest, aber keinen Strom; ihr Strom stellt sich nach dem übrigen Netz ein, und kein Satz gibt ihn aus den
Knotenspannungen. Deshalb verlangt das Skript, Spannungsquellen zuerst in Stromquellen umzuwandeln.

**Die reale Spannungsquelle.** Eine reale Spannungsquelle mit der Quellenspannung $U_q$ und dem Innenwiderstand $R_q$ liege zwischen dem Knoten $\nu$ an
ihrem Pluspol und dem Knoten $\mu$. Für das Verfahren ist sie eine ideale Stromquelle, die ihren Kurzschlussstrom in den Knoten $\nu$ schiebt, parallel zu
ihrem Innenleitwert $G_q$ — die Ersatzstromquelle aus dem Artikel über Ersatzquellen:

:::formel
$$I_q = \frac{U_q}{R_q} = G_q\,U_q, \qquad G_q = \frac{1}{R_q}.$$
:::

**So liest man das:** In die Matrix kommt $G_q$ wie jeder andere Leitwert zwischen $\nu$ und $\mu$, auf die rechte Seite der Kurzschlussstrom $G_qU_q$, mit
Plus am Knoten $\nu$ und mit Minus am Knoten $\mu$. Zeichnen muss man die Umwandlung nicht: Sie ergibt sich von selbst, wenn man den Zweigstrom der Quelle in
die Knotenregel einsetzt.

**Im Bild:** Ein Wasserturm mit enger Zuleitung wirkt am Knoten wie eine Spritzenpumpe, die so viel einspeist, wie bei Pegel null ankäme, zusammen mit
einem Rohr, durch das bei höherem Pegel ein Teil wieder zurückläuft.

:::herleitung
**Der Zweigstrom der Quelle.** In der Quelle fließe der Strom $I$ vom Knoten $\mu$ zum Knoten $\nu$, also aus ihrem Pluspol heraus in den Knoten $\nu$.
Längs des Zweigs steigt das Potenzial in der Quelle um $U_q$ und fällt am Innenwiderstand um $R_qI$:

$$U_\nu - U_\mu = U_q - R_q\,I, \qquad I = G_q\,U_q - G_q\,(U_\nu - U_\mu).$$

**In der Knotenregel.** Am Knoten $\nu$ fließt $I$ zu. Der Anteil $G_q(U_\nu - U_\mu)$ hat die Form eines Leitwertstroms von $\nu$ nach $\mu$ und gehört in die
Matrix. Der Anteil $G_qU_q$ hängt von keiner Knotenspannung ab und steht wie ein Quellstrom rechts. Am Knoten $\mu$ fließt $I$ ab, dort steht $G_qU_q$ mit
Minus. Das ist genau eine Stromquelle mit parallelem Leitwert.

**Im Bild:** Der Zufluss vom Turm ist der Zufluss bei Pegel null, vermindert um das, was der eigene Pegel des Knotens zurückdrückt.
:::

Hat ein Netz außer dem Bezugsknoten nur einen einzigen Knoten, bleibt eine einzige Gleichung. Zwischen diesem Knoten 1 und dem Bezugsknoten liegen dann
nur Zweige; der Zweig $j$ bestehe aus einer Quelle $U_{qj}$, Pluspol zum Knoten 1, in Reihe mit dem Leitwert $G_j$, und ein reiner Leitwert hat $U_{qj} = 0$. Die Knotenspannung ist
dann das mit den Leitwerten gewichtete Mittel der Quellenspannungen, der __Satz von Millman__:

$$U_1 = \frac{\sum_j G_j\,U_{qj}}{\sum_j G_j}.$$

:::herleitung
Jeder Zweig wird zur Ersatzstromquelle mit dem Kurzschlussstrom $G_jU_{qj}$ in den Knoten 1. Die einzige Knotengleichung hat links den Knotenleitwert, die
Summe aller $G_j$, rechts die Summe der Kurzschlussströme:

$$\Big(\sum_j G_j\Big)\,U_1 = \sum_j G_j\,U_{qj}.$$

Teilen durch den Knotenleitwert ergibt die Formel. Im Bild: Mehrere Türme mit verschieden weiten Zuleitungen an einem Knoten; sein Pegel stellt sich
zwischen ihren Pegeln ein, am nächsten bei dem Turm mit der weitesten Leitung.
:::

::::beispiel Ladegerät und Batterie mit einer Gleichung
Ladegerät und Batterie am Kühlschrank aus den Artikeln über das Superpositions- und das Maschenstromverfahren: links das Ladegerät, in der Mitte die Last,
rechts die Batterie, alle Pluspole oben:

$$U_{q1} = 14\,\text{V}, \qquad R_{q1} = 0{,}5\,\Omega, \qquad R_L = 2\,\Omega, \qquad U_{q2} = 12\,\text{V}, \qquad R_{q2} = 0{,}1\,\Omega.$$

**Ein Knoten.** Die untere Leitung wird Bezugsknoten, die obere ist der Knoten 1. Drei Zweige, zwei Knoten: eine Knotengleichung statt zwei
Maschengleichungen. Die Leitwerte:

$$G_{q1} = 2\,\text{S}, \qquad G_{q2} = 10\,\text{S}, \qquad G_L = 0{,}5\,\text{S}.$$

**Nach Millman.** Die Last hat keine Quelle und zählt nur im Nenner:

$$U_1 = \frac{2\,\text{S}\cdot14\,\text{V} + 10\,\text{S}\cdot12\,\text{V}}{2\,\text{S} + 10\,\text{S} + 0{,}5\,\text{S}} = \frac{148\,\text{A}}{12{,}5\,\text{S}} = 11{,}84\,\text{V}.$$

**Die Ströme.** Das Ladegerät liefert $I_1$, die Batterie $I_2$, beide in den Knoten hinein; durch die Last fließt $I_L$:

$$I_1 = 2\,\text{S}\cdot(14 - 11{,}84)\,\text{V} = 4{,}32\,\text{A}, \qquad I_2 = 10\,\text{S}\cdot(12 - 11{,}84)\,\text{V} = 1{,}6\,\text{A}, \qquad I_L = 0{,}5\,\text{S}\cdot11{,}84\,\text{V} = 5{,}92\,\text{A}.$$

Dieselben Werte wie mit Überlagerung und mit Maschenströmen. Die Batterie wird nicht geladen, sie liefert $1{,}6\,\text{A}$ mit.

**Im Bild:** Zwei Türme, 14 und 12 hoch, an einem Knoten mit einem Abfluss. Die Zuleitung der Batterie ist fünfmal so weit wie die des Ladegeräts, deshalb
liegt der Pegel 11,84 dicht unter ihren 12.
::::

**Die ideale Stromquelle mit Vorwiderstand.** Eine ideale Stromquelle legt den Strom ihres Zweiges fest, ganz gleich, was sonst in diesem Zweig liegt. Ein
Widerstand $R_s$ in Reihe zu ihr ändert diesen Strom nicht; er kommt deshalb in der Matrix nicht vor. Er zeigt sich nur in der Spannung $U_I$ an der Quelle
selbst. Schiebt die Quelle $I_q$ vom Knoten $\mu$ über $R_s$ in den Knoten $\nu$, gilt, mit $U_I$ vom Anschluss an $R_s$ zum Knoten $\mu$ gezählt:

$$U_I = U_\nu - U_\mu + R_s\,I_q.$$

:::herleitung
**Der Strom bleibt.** Der Zweigstrom ist $I_q$, wie groß $R_s$ auch ist. In den Knotenregeln steht der Zweig nur als Quellstrom, mit $+I_q$ am Knoten $\nu$
und $-I_q$ am Knoten $\mu$; $R_s$ tritt in keiner Gleichung für die Knotenspannungen auf.

**Die Spannung an der Quelle.** Vom Anschluss der Quelle an $R_s$ bis zum Knoten $\nu$ fällt an $R_s$ die Spannung $R_sI_q$ ab. Der Anschluss liegt also
um $R_sI_q$ höher als der Knoten $\nu$, und von ihm bis zum Knoten $\mu$ sind es die Zweigspannung und dieser Abfall zusammen. Im Bild: Eine Spritzenpumpe
vor einem engen Rohr fördert dieselbe Menge, sie muss nur stärker drücken.
:::

::::beispiel Eine Spannungs- und eine Stromquelle an einem Knoten
Die Schaltung aus den Artikeln über das Superpositions- und das Maschenstromverfahren: links $U_q$ über $R_a$ zum Knoten K, in der Mitte $R_b$ von K nach
Masse, rechts eine ideale Stromquelle, die über $R_s$ den Strom $I_q$ in K schiebt:

$$U_q = 10\,\text{V}, \qquad R_a = 2\,\text{k}\Omega, \qquad R_b = 3\,\text{k}\Omega, \qquad I_q = 2\,\text{mA}, \qquad R_s = 5\,\text{k}\Omega.$$

**Eine einzige Gleichung.** Masse ist Bezugsknoten, K der einzige weitere Knoten. Die reale Spannungsquelle wird zur Ersatzstromquelle mit $5\,\text{mA}$;
der Knotenleitwert besteht aus den Leitwerten von $R_a$ und $R_b$, und $R_s$ kommt nicht vor:

$$\Big(\frac{1}{2\,\text{k}\Omega} + \frac{1}{3\,\text{k}\Omega}\Big)\,U_K = \frac{10\,\text{V}}{2\,\text{k}\Omega} + 2\,\text{mA}, \qquad \frac{5}{6}\,\text{mS}\cdot U_K = 7\,\text{mA}, \qquad U_K = 8{,}4\,\text{V}.$$

**Was daraus folgt.** Die Ströme durch $R_a$ zum Knoten und durch $R_b$ nach Masse, und die Spannung an der Stromquelle:

$$I_a = \frac{10\,\text{V} - 8{,}4\,\text{V}}{2\,\text{k}\Omega} = 0{,}8\,\text{mA}, \qquad I_b = \frac{8{,}4\,\text{V}}{3\,\text{k}\Omega} = 2{,}8\,\text{mA}, \qquad U_I = 8{,}4\,\text{V} + 5\,\text{k}\Omega\cdot2\,\text{mA} = 18{,}4\,\text{V}.$$

Dasselbe Ergebnis wie mit Maschenströmen, aber aus einer Gleichung und ohne eine Masche durch die Stromquelle legen zu müssen. Der Vorwiderstand taucht erst
in der Spannung an der Quelle auf.

**Im Bild:** Ein Turm über eine Leitung und eine Spritzenpumpe hinter einem engen Rohr füllen denselben Knoten. Die Pumpe fördert ihre $2\,\text{mA}$, ob das
Rohr eng ist oder nicht.
::::

## Warum die Matrix symmetrisch und das System lösbar ist

Wie die Widerstandsmatrix des vorigen Artikels hat die Knotenleitwertmatrix zwei Eigenschaften, die das Verfahren zuverlässig machen. Das Skript nennt die
erste, die Symmetrie; die zweite, die __positive Definitheit__, ist der Grund, warum man nie ein unlösbares System erhält. Sie besagt, dass die Doppelsumme
unten für alle Knotenspannungen positiv ist, die nicht sämtlich null sind. Die Symmetrie gilt für jedes Netz aus Leitwerten und unabhängigen Quellen, die
positive Definitheit, wenn außerdem alle Leitwerte positiv sind und jeder Knoten über einen Weg aus Leitwerten mit dem Bezugsknoten verbunden ist. Die Summe
rechts läuft über alle Leitwerte $G_j$ des Netzes, mit ihren Zweigspannungen $U_j$:

:::formel Satz
$$Y_{\nu\mu} = Y_{\mu\nu}, \qquad \sum_{\nu,\mu} Y_{\nu\mu}\,U_\nu\,U_\mu = \sum_j G_j\,U_j^2 > 0.$$
:::

**So liest man das:** Die Symmetrie ist eine Probe beim Aufstellen. Die Doppelsumme über alle Paare von Knoten macht aus den Knotenspannungen eine einzige
Zahl: die Leistung, die alle Leitwerte zusammen umsetzen. Sie ist positiv, sobald nicht alle Knotenspannungen null sind. Daraus folgt, dass das
Gleichungssystem für jede rechte Seite genau eine Lösung hat. Weil $\mathbf Y\vec U$ die Quellströme sind, ist dieselbe Doppelsumme auch die Leistung, die
die Stromquellen abgeben.

Die Voraussetzung ist wesentlich. Hängt ein Knoten nur an Stromquellen, steht in seiner Zeile kein Leitwert, die Zeile ist null und die Matrix singulär.
Ein solcher Knoten __schwebt__: Ideale Stromquellen nehmen jede Spannung an, und nichts legt sein Potenzial fest. Auch gesteuerte Quellen, die im Exkurs
unten vorkommen, heben den Satz auf.

**Im Bild:** Jedes Rohr zwischen zwei Knoten zählt in beiden Bilanzen gleich stark. Und Wasser, das von höherem zu niedrigerem Pegel fließt, erzeugt in
den Rohren immer Reibungswärme, nie Kälte.

:::herleitung
**Symmetrie.** Neben der Diagonale steht $-G_{\nu\mu}$, und der Leitwert zwischen $\nu$ und $\mu$ ist derselbe wie zwischen $\mu$ und $\nu$.

**Die Doppelsumme als Summe über Zweige.** Ein Leitwert $G_j$ zwischen den Knoten $\alpha$ und $\beta$ bringt in die Zeile $\alpha$ den abfließenden Strom
$G_j(U_\alpha - U_\beta)$ und in die Zeile $\beta$ denselben mit Minus. Multipliziert man jede Zeile mit ihrer Knotenspannung und addiert, steht für diesen
Zweig das Quadrat seiner Zweigspannung $U_j$:

$$\begin{aligned} &U_\alpha\,G_j\,(U_\alpha - U_\beta) - U_\beta\,G_j\,(U_\alpha - U_\beta) \\ &= G_j\,(U_\alpha - U_\beta)^2 = G_j\,U_j^2. \end{aligned}$$

Für einen Zweig zum Bezugsknoten fehlt die Zeile $\beta$, und mit $U_\beta = 0$ steht dasselbe da.

**Positiv.** Die Summe ist null nur, wenn die Spannung an jedem Leitwert null ist. Weil jeder Knoten über einen Weg aus Leitwerten mit dem Bezugsknoten
verbunden ist, folgt dann Zweig für Zweig längs dieses Weges, dass alle Knotenspannungen null sind.

**Eindeutig lösbar.** Wäre $\mathbf Y$ nicht umkehrbar, gäbe es Knotenspannungen, nicht alle null, für die alle linken Seiten verschwinden. Multipliziert
man jede linke Seite mit ihrer Knotenspannung und addiert, erhielte man die Leistung null, ein Widerspruch. Also hat das System für jede rechte Seite genau
eine Lösung.

**Die Leistung der Quellen.** Mit $\mathbf Y\vec U = \vec I_q$ ist die Doppelsumme auch die Summe der $U_\nu I_{q\nu}$. Eine Stromquelle, die $I$ vom Knoten
$\beta$ in den Knoten $\alpha$ schiebt, steht mit $+I$ in der Zeile $\alpha$ und mit $-I$ in der Zeile $\beta$; sie trägt $I(U_\alpha - U_\beta)$ bei, die
Leistung, die sie abgibt. Im Bild: Die Pumpen bringen genau die Energie auf, die in den Rohren als Reibungswärme verloren geht.
:::

::::beispiel Leistungsprobe und ein schwebender Knoten
**(a) Die Leistungsprobe.** Das Netz mit drei Knoten und zwei Stromquellen von oben, mit den Knotenspannungen 5, 2 und 1 V. Die Doppelsumme ist die Leistung
der Quellen:

$$\sum_\nu U_\nu\,I_{q\nu} = 5\,\text{V}\cdot15\,\text{mA} + 2\,\text{V}\cdot4\,\text{mA} - 1\,\text{V}\cdot4\,\text{mA} = 79\,\text{mW}.$$

Die sechs Leitwerte nehmen zusammen dasselbe auf, jeder $G_jU_j^2$, in mS mal V², also mW:

$$1\cdot5^2 + 2\cdot3^2 + 1\cdot4^2 + 2\cdot1^2 + 4\cdot2^2 + 2\cdot1^2 = 79.$$

Die Quelle A gibt davon $75\,\text{mW}$ ab, die Quelle B, die vom Pegel $1\,\text{V}$ auf $2\,\text{V}$ hebt, $4\,\text{mW}$. Die Matrix ist symmetrisch, und
die Leistung ist positiv, wie der Satz verlangt.

**(b) Ein schwebender Knoten.** Zwei ideale Stromquellen in Reihe: Die eine schiebt $1\,\text{mA}$ aus dem Bezugsknoten in den Knoten 2, die andere dieselben
$1\,\text{mA}$ aus dem Knoten 2 in den Knoten 1; vom Knoten 1 führt $G_{10} = 1\,\text{mS}$ zum Bezugsknoten zurück. Am Knoten 2 hängt kein Leitwert, und
sein Quellstrom ist $1\,\text{mA} - 1\,\text{mA}$:

$$\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}\text{mS}\begin{pmatrix} U_1 \\ U_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}\text{mA}, \qquad \det\mathbf Y = 0.$$

Die erste Zeile legt $U_1$ auf $1\,\text{V}$ fest, die zweite lautet null gleich null: Jede Spannung $U_2$ ist eine Lösung. Ein Simulator meldet hier eine
singuläre Matrix. Abhilfe schafft, was jede reale Stromquelle ohnehin hat, ein Leitwert parallel.

**Im Bild:** Ein Knoten, an dem nur zwei Spritzenpumpen hängen, hat keinen bestimmten Pegel. Die Pumpen fördern bei jedem Druck dieselbe Menge, und kein Rohr
verbindet ihn mit der Nullmarke.
::::

## Knoten oder Maschen?

Beide Verfahren lösen dasselbe Netz, aber verschieden schnell. Das Knotenpotentialverfahren braucht $k - 1$ Gleichungen, das Maschenstromverfahren
$z - k + 1$. Das Skript hält fest, wann das Knotenpotentialverfahren kürzer ist:

$$k - 1 < z - k + 1 \iff z > 2k - 2.$$

**So liest man das:** Das Knotenpotentialverfahren gewinnt bei Netzen, deren Knoten über viele Zweige miteinander verbunden sind; das Maschenstromverfahren
bei Netzen mit vielen Knoten, aber wenigen Schleifen, etwa langen Ketten. Ideale Quellen verschieben die Rechnung: Jede ideale Spannungsquelle, deren einer
Pol am Bezugsknoten liegt, macht eine Knotenspannung bekannt, wie der nächste Abschnitt zeigt; jede ideale Stromquelle macht einen Maschenstrom bekannt.

Das Skript schreibt zu Beginn des Kapitels, die Maschenstromanalyse sei nur für Schaltungen mit Spannungsquellen geeignet, und im Knotenpotentialverfahren
könnten nur Stromquellen berücksichtigt werden. Beides ist zu streng: Der vorige Artikel hat gezeigt, wie Maschenströme mit idealen Stromquellen umgehen,
und der nächste Abschnitt zeigt, wie Knotenspannungen mit idealen Spannungsquellen umgehen.

**Im Bild:** Ein dicht vermaschtes Netz mit wenigen Verzweigungen hat viele Schleifen, aber wenige Standrohre; eine lange Leitung mit vielen Abzweigen hat
viele Standrohre, aber kaum Schleifen.

:::herleitung
**Die Ungleichung.** Auf beiden Seiten $k - 1$ addiert:

$$k - 1 < z - k + 1 \iff 2k - 2 < z.$$

**Zweige je Knoten.** Jeder Zweig hat zwei Enden, an einem Knoten enden also im Mittel $2z/k$ Zweige. Multipliziert man die Bedingung mit $2/k$, wird sie
zu einer Aussage über diesen Mittelwert:

$$\frac{2z}{k} > 4 - \frac{4}{k}.$$

Weil die rechte Seite stets unter vier liegt, ist das Knotenpotentialverfahren immer kürzer, wenn an einem Knoten im Mittel mehr als vier Zweige enden;
bei vier Knoten genügen schon mehr als drei. Bei sehr vielen Knoten ist vier auch die Grenze.
:::

::::beispiel Fünf Netze gezählt
Zweige $z$, Knoten $k$, Maschengleichungen $m$ und Knotengleichungen $n$ der Netze dieses und des vorigen Artikels, dazu zwei Grenzfälle:

| Netz | $z$ | $k$ | $m$ | $n$ | kürzer |
|---|---|---|---|---|---|
| Ladegerät, Batterie und Last | 3 | 2 | 2 | 1 | Knoten |
| Brücke mit Quelle | 6 | 4 | 3 | 3 | gleich |
| drei Knoten, zwei Stromquellen | 8 | 4 | 5 | 3 | Knoten |
| Reihenkreis aus Quelle und vier Widerständen | 5 | 5 | 1 | 4 | Maschen |
| fünf Knoten, jeder mit jedem verbunden | 10 | 5 | 6 | 4 | Knoten |

**Die Brücke.** Hier ist $z$ genau $2k - 2$, beide Verfahren brauchen drei Gleichungen. Den Ausschlag gibt die ideale Spannungsquelle: Legt man den
Bezugsknoten an einen ihrer Pole, ist eine Knotenspannung bekannt, und es bleiben zwei Gleichungen.

**Ideale Stromquellen.** Im Netz mit drei Knoten läuft durch jede der beiden idealen Stromquellen nur eine Masche, wenn man die Maschen so legt; dann sind
zwei Maschenströme bekannt, und es bleiben ebenfalls drei Unbekannte. Die Knotenspannungen sind trotzdem bequemer, weil man keine Maschen wählen muss.

**Im Bild:** Der Reihenkreis ist eine einzige Schleife mit vier Standrohren, ein Ringstrom genügt. Das dicht vermaschte Netz hat sechs Schleifen, aber nur
vier Standrohre außer der Nullmarke.
::::

## Ideale Spannungsquellen

In der Zusammenfassung des Skripts heißt es, ideale Spannungsquellen und Widerstände von $0\,\Omega$ könnten im Knotenpotentialverfahren nicht
berücksichtigt werden. Für die Leitwertmatrix stimmt das: Eine ideale Spannungsquelle hat keinen Innenwiderstand, ihr Strom hängt von keiner
Knotenspannung ab, und eine Ersatzstromquelle hätte den Kurzschlussstrom $U_q/0$. Für die Rechnung von Hand gibt es aber zwei einfache Wege; den dritten, den
Simulatoren gehen, zeigt der Exkurs unten.

**Ein Pol am Bezugsknoten.** Liegt die Quelle zwischen dem Knoten $\nu$ an ihrem Pluspol und dem Bezugsknoten, ist die Knotenspannung bekannt:

$$U_\nu = U_q.$$

**So liest man das:** Die Gleichung des Knotens $\nu$ entfällt. Sie enthält den unbekannten Strom der Quelle und dient nur noch dazu, ihn hinterher
auszurechnen. In den Gleichungen der Nachbarknoten steht $U_q$ mit seinem Koppeleintrag und wandert nach rechts, als speiste dort eine Stromquelle den
Strom $G_{\mu\nu}U_q$ ein. Jede solche Quelle spart eine Unbekannte, dual zur idealen Stromquelle im Maschenstromverfahren. Bei mehreren Spannungsquellen
legt man den Bezugsknoten deshalb dorthin, wo die meisten von ihnen einen Pol haben.

**Im Bild:** Ein Wasserturm hält den Pegel seines Knotens fest. Wie viel er dafür liefern muss, zeigt sich erst, wenn die übrigen Pegel bekannt sind.

:::herleitung
**Bekannte Knotenspannung.** Die Quelle legt die Spannung zwischen ihren Polen fest, und ihr Minuspol liegt am Bezugsknoten mit dem Potenzial null.

**Die Gleichung des Knotens $\nu$.** In ihr steht der Strom der Quelle. Er hängt von keiner Knotenspannung ab und richtet sich nach dem übrigen Netz; er ist
eine zusätzliche Unbekannte, die nur in dieser einen Gleichung vorkommt. Die Gleichung legt also nur ihn fest.

**Die übrigen Gleichungen.** In der Gleichung eines Nachbarknotens $\mu$ steht der Term $-G_{\mu\nu}U_\nu$ mit bekanntem $U_\nu$. Auf die rechte Seite
gebracht, mit der Summe über die übrigen, unbekannten Knotenspannungen:

$$\sum_{\lambda \ne \nu} Y_{\mu\lambda}\,U_\lambda = I_{q\mu} + G_{\mu\nu}\,U_q.$$

Es bleiben $n - 1$ Gleichungen für $n - 1$ Unbekannte. Im Bild: Wo ein Turm den Pegel hält, muss man kein Standrohr ablesen.
:::

::::beispiel Die Brücke mit zwei Gleichungen
Die Brücke von oben, B als Bezugsknoten, die Quelle hält A auf $32\,\text{V}$:

$$U_q = 32\,\text{V}, \qquad R_{12} = 10\,\Omega, \qquad R_{31} = 20\,\Omega, \qquad R_{23} = 20\,\Omega, \qquad R_{2B} = 26\,\Omega, \qquad R_{3B} = 12\,\Omega.$$

**Zwei Knotengleichungen.** Mit bekanntem $U_1$ bleiben die Knoten 2 und 3. Ihre Knotenleitwerte sind die Leitwerte von $R_{12}$, $R_{23}$ und $R_{2B}$
beziehungsweise von $R_{31}$, $R_{23}$ und $R_{3B}$; der bekannte Anteil von A steht rechts:

$$\Big(\frac{1}{10} + \frac{1}{20} + \frac{1}{26}\Big)\text{S}\cdot U_2 - \frac{1}{20}\,\text{S}\cdot U_3 = \frac{32\,\text{V}}{10\,\Omega} = 3{,}2\,\text{A},$$

$$-\frac{1}{20}\,\text{S}\cdot U_2 + \Big(\frac{1}{20} + \frac{1}{20} + \frac{1}{12}\Big)\text{S}\cdot U_3 = \frac{32\,\text{V}}{20\,\Omega} = 1{,}6\,\text{A}.$$

**Lösen.** Die erste Zeile mal $260\,\Omega$, die zweite mal $60\,\Omega$ macht die Zahlen ganz; die Symmetrie geht dabei verloren, die Lösung nicht:

$$49\,U_2 - 13\,U_3 = 832\,\text{V}, \qquad -3\,U_2 + 11\,U_3 = 96\,\text{V}.$$

Nach Cramer, mit der Determinante $49\cdot11 - 13\cdot3$, also $500$:

$$U_2 = \frac{832\cdot11 + 13\cdot96}{500}\,\text{V} = 20{,}8\,\text{V}, \qquad U_3 = \frac{49\cdot96 + 3\cdot832}{500}\,\text{V} = 14{,}4\,\text{V}.$$

**Der Quellstrom.** Die übrig gebliebene Gleichung des Knotens A: Was über $R_{12}$ und $R_{31}$ abfließt, liefert die Quelle:

$$I = \frac{32\,\text{V} - 20{,}8\,\text{V}}{10\,\Omega} + \frac{32\,\text{V} - 14{,}4\,\text{V}}{20\,\Omega} = 1{,}12\,\text{A} + 0{,}88\,\text{A} = 2\,\text{A}.$$

Dieselben Werte wie mit der Stern-Dreieck-Umwandlung und mit drei Maschenströmen, aber aus zwei Gleichungen.

**Im Bild:** Der Turm hält A auf 32. Abzulesen sind nur die Standrohre in der Mitte, und was der Turm dafür hergeben muss, zeigt die Bilanz an A.
::::

**Zwischen zwei Knoten: der Superknoten.** Liegt die Quelle zwischen zwei Knoten $\mu$ und $\nu$, von denen keiner der Bezugsknoten ist, Pluspol an $\mu$,
legt sie nur den Unterschied ihrer Spannungen fest. Man umschließt beide Knoten samt Quelle mit einer gedachten Hülle, dem __Superknoten__, und stellt die
Knotenregel für die ganze Hülle auf. Der Strom der Quelle fließt innerhalb der Hülle und fällt heraus. Die Summen laufen über alle anderen Knoten, den
Bezugsknoten eingeschlossen:

:::formel
$$U_\mu - U_\nu = U_q, \qquad \sum_{\lambda \ne \mu} G_{\mu\lambda}\,(U_\mu - U_\lambda) + \sum_{\lambda \ne \nu} G_{\nu\lambda}\,(U_\nu - U_\lambda) = I_{q\mu} + I_{q\nu}.$$
:::

**So liest man das:** Die erste Gleichung ist die Quellengleichung, die zweite die Knotenregel der Hülle: Alles, was aus $\mu$ und $\nu$ zusammen über
Leitwerte abfließt, speisen die Stromquellen dieser beiden Knoten ein. Zusammen mit den Gleichungen der übrigen Knoten sind es wieder $n$ Gleichungen für $n$
Unbekannte. Den Strom der Spannungsquelle gibt hinterher die Knotenregel an $\mu$ oder $\nu$ allein. Ein Widerstand von $0\,\Omega$ ist eine Quelle mit
$0\,\text{V}$: Seine beiden Knoten haben dieselbe Spannung und werden einfach zu einem Knoten zusammengefasst.

**Im Bild:** Eine __Druckerhöhungspumpe__, wie sie in Wassernetzen den Druck anhebt, hier idealisiert um einen festen Betrag, wie viel auch durchfließt,
verbindet zwei Knoten. Ihre beiden Standrohre steigen und fallen gemeinsam, im festen Abstand, und für die Bilanz zählen sie wie ein einziger großer Knoten.

:::herleitung
**Der Unterschied.** Die Quelle legt die Spannung zwischen ihren Polen fest, und die ist nach dem Satz über Zweigspannungen die Differenz der
Knotenspannungen.

**Die Hülle.** Der Strom $I_V$ der Spannungsquelle fließe am Knoten $\mu$ in die Quelle ab und komme am Knoten $\nu$ aus ihr an. Die Knotenregeln der beiden
Knoten enthalten ihn mit entgegengesetztem Vorzeichen; addiert man sie, fällt er heraus:

$$\begin{aligned} &\Big(\sum_{\lambda \ne \mu} G_{\mu\lambda}\,(U_\mu - U_\lambda) + I_V\Big) \\ &+ \Big(\sum_{\lambda \ne \nu} G_{\nu\lambda}\,(U_\nu - U_\lambda) - I_V\Big) \\ &= I_{q\mu} + I_{q\nu}. \end{aligned}$$

Ein Leitwert direkt zwischen $\mu$ und $\nu$ steht in beiden Summen mit entgegengesetztem Vorzeichen und fällt ebenfalls heraus; sein Strom bleibt in der
Hülle.

**Abzählen.** Die Quellengleichung und die Gleichung der Hülle ersetzen die beiden Knotenregeln, die den unbekannten Strom enthielten. Im Bild: Was die
Druckerhöhungspumpe innerhalb des Doppelknotens umwälzt, ändert nichts an seiner Bilanz.
:::

::::beispiel Eine schwebende Spannungsquelle
Zwei Knoten über Widerständen an Masse, dazwischen eine ideale Spannungsquelle mit Pluspol am Knoten 2; eine ideale Stromquelle schiebt $I_q$ aus Masse in
den Knoten 1. Die Spannungsquelle berührt den Bezugsknoten nicht:

$$R_1 = 2\,\text{k}\Omega, \qquad R_2 = 4\,\text{k}\Omega, \qquad U_q = 6\,\text{V}, \qquad I_q = 3\,\text{mA}.$$

**Der Superknoten.** Die Hülle um die Knoten 1 und 2 samt Quelle: Über $R_1$ und $R_2$ fließt ab, was die Stromquelle einspeist; dazu die Quellengleichung:

$$\frac{U_1}{2\,\text{k}\Omega} + \frac{U_2}{4\,\text{k}\Omega} = 3\,\text{mA}, \qquad U_2 - U_1 = 6\,\text{V}.$$

**Lösen.** $U_2$ in die erste Gleichung eingesetzt:

$$0{,}5\,\text{mS}\cdot U_1 + 0{,}25\,\text{mS}\cdot(U_1 + 6\,\text{V}) = 3\,\text{mA}, \qquad 0{,}75\,\text{mS}\cdot U_1 = 1{,}5\,\text{mA}, \qquad U_1 = 2\,\text{V}, \qquad U_2 = 8\,\text{V}.$$

**Der Strom der Spannungsquelle.** Wie in der Herleitung zählt $I_V$ vom Pluspol, dem Knoten 2, durch die Quelle zum Knoten 1. Die Knotenregel am Knoten 1
allein: Über $R_1$ fließt ab, was die Stromquelle und $I_V$ zuführen:

$$\frac{2\,\text{V}}{2\,\text{k}\Omega} = 3\,\text{mA} + I_V, \qquad I_V = -2\,\text{mA}.$$

Das Minus heißt, dass die $2\,\text{mA}$ in Wirklichkeit vom Knoten 1 durch die Quelle zum Knoten 2 fließen, vom Minus- zum Pluspol. Am Knoten 2 fließen
genau diese $2\,\text{mA}$ über $R_2$ ab, denn $8\,\text{V}$ an $4\,\text{k}\Omega$ ergeben $2\,\text{mA}$. Die Spannungsquelle gibt also Leistung ab:

$$P_V = 6\,\text{V}\cdot2\,\text{mA} = 12\,\text{mW}, \qquad P_I = 2\,\text{V}\cdot3\,\text{mA} = 6\,\text{mW}, \qquad P_R = 2\,\text{mW} + 16\,\text{mW} = 18\,\text{mW}.$$

Beide Quellen zusammen geben ab, was die Widerstände aufnehmen.

**Im Bild:** Eine Druckerhöhungspumpe hält den Pegel 2 um 6 über dem Pegel 1. Die Spritzenpumpe füllt beide, und sie stellen sich gemeinsam auf 2 und 8 ein.
::::

:::grafik
Szene: get1/knotenpotentialverfahren/01-superknoten · Vorlage: superknoten-huelle
Zwei Hälften nebeneinander. Links die Brücke als Raute mit A oben, B unten als Bezugsknoten und der Quelle $32\,\text{V}$ links daneben: Das Standrohr an A ist
vom Turm auf 32 festgehalten und hat keinen Regler; die Gleichung des Knotens A blendet sich aus der Matrix aus und erscheint unten als „Quellstrom
$2\,\text{A}$“. Die Standrohre an 2 und 3 haben Regler und stellen sich nach „lösen“ auf $20{,}8$ und $14{,}4\,\text{V}$ ein. Rechts die schwebende
Spannungsquelle $6\,\text{V}$ zwischen den Knoten 1 und 2, $R_1 = 2\,\text{k}\Omega$ und $R_2 = 4\,\text{k}\Omega$ nach Masse, die Stromquelle
$3\,\text{mA}$ in den Knoten 1. Eine gestrichelte Hülle umschließt beide Knoten samt Quelle. Zieht man am Regler von $U_1$, folgt $U_2$ im festen Abstand von
$6\,\text{V}$. Die Ströme über $R_1$, $R_2$ und aus der Stromquelle kreuzen die Hülle als Pfeile; der Strom der Spannungsquelle bleibt innen und ist blass. Eine
Bilanzanzeige an der Hülle zeigt Zufluss minus Abfluss und wird bei $U_1 = 2\,\text{V}$ null. Kernaussage: Eine ideale Spannungsquelle am Bezugsknoten macht
eine Knotenspannung bekannt, eine schwebende verbindet zwei Knoten zu einem Superknoten. (Rot = Quellen, blau = Pegel, orange = Hülle und Bilanzanzeige,
grau = Widerstände, gestrichelt = Hülle.)
:::

## Exkurs: Die Matrix Bauteil für Bauteil

Das Skript schließt das Kapitel mit einem Abschnitt über die modifizierte Knotenpotentialanalyse, eine Erweiterung des Verfahrens, die auch ideale
Spannungsquellen fasst, und sagt selbst, sie gehöre nicht zu GET1, sondern zur Schaltungstechnik 1 im dritten Semester. Wer nur die Rechnung von Hand braucht, kann bei der Bedeutung am Ende weiterlesen. Die beiden Exkurse zeigen, wie
ein Schaltungssimulator dieselbe Matrix aufbaut, ohne über das Netz nachzudenken.

Die Idee: Jedes Bauteil liefert einen festen Beitrag zur Matrix, unabhängig von allen anderen Bauteilen, sein __Eintragsmuster__ (englisch stamp, Stempel).
Ein Programm beginnt mit einer Nullmatrix und einem Nullvektor, geht die Bauteile nacheinander durch und addiert ihre Muster. Das Skript nimmt dabei
zunächst auch den Bezugsknoten als Knoten 0 mit; die Matrix hat dann $n + 1$ Zeilen und Spalten, und am Ende streicht man Zeile und Spalte 0.

Neben Leitwerten und unabhängigen Stromquellen kommen __spannungsgesteuerte Stromquellen__ vor, wie im Artikel über Zweitore: Quellen, deren Strom
proportional zu einer Spannung an anderer Stelle des Netzes ist. Der Faktor $g_m$ heißt __Steilheit__ und wird in Siemens gemessen. Die Quelle liege
zwischen den Knoten $\nu$ und $\mu$; ihr Strom $I_g$ fließe vom Knoten $\nu$ durch die Quelle zum Knoten $\mu$ und werde von der Spannung zwischen den
Knoten $\rho$ und $\sigma$ gesteuert:

$$I_g = g_m\,U_{\rho\sigma} = g_m\,(U_\rho - U_\sigma).$$

Die drei Muster, jeweils mit den betroffenen Zeilen links und den Spalten oben: ein Leitwert $G$ zwischen $\nu$ und $\mu$, eine unabhängige Stromquelle, die
$I_q$ vom Knoten $\mu$ in den Knoten $\nu$ schiebt, und die gesteuerte Quelle:

:::formel
$$\begin{array}{ccc} & \nu & \mu \\ \nu & +G & -G \\ \mu & -G & +G \end{array} \qquad \begin{array}{cc} & \vec I_q \\ \nu & +I_q \\ \mu & -I_q \end{array} \qquad \begin{array}{ccc} & \rho & \sigma \\ \nu & +g_m & -g_m \\ \mu & -g_m & +g_m \end{array}$$
:::

**So liest man das:** Der Leitwert steht in den Zeilen und Spalten seiner beiden Knoten, mit $+G$ auf der Diagonale und $-G$ daneben: die Regeln von oben,
Bauteil für Bauteil gelesen. Die unabhängige Stromquelle steht nur im Quellvektor, mit Plus in der Zeile des Knotens, in den sie einspeist. Die gesteuerte
Quelle steht in den Zeilen $\nu$ und $\mu$ wie ein Leitwert, aber in den Spalten $\rho$ und $\sigma$ der steuernden Knoten. Einträge in Zeile oder Spalte 0
fallen beim Streichen weg; ein Bauteil am Bezugsknoten hinterlässt deshalb nur einen Teil seines Musters.

**Im Bild:** Jedes Rohr meldet seinen Beitrag an die Bilanzen seiner beiden Knoten, ohne die übrigen Rohre zu kennen. Eine gesteuerte Quelle ist eine Pumpe,
deren Fördermenge ein Fühler an zwei anderen Standrohren einstellt.

:::herleitung
**Leitwert.** Der Strom $G(U_\nu - U_\mu)$ fließt aus dem Knoten $\nu$ ab und in den Knoten $\mu$ hinein. In der Zeile $\nu$ steht er mit Plus, in der Zeile
$\mu$ mit Minus; ausmultipliziert ergibt das die vier Einträge.

**Unabhängige Stromquelle.** Ihr Strom hängt von keiner Knotenspannung ab und steht deshalb nur rechts: mit Plus in der Zeile $\nu$, in die er hineinfließt,
mit Minus in der Zeile $\mu$, aus der er kommt.

**Gesteuerte Quelle.** Ihr Strom $g_m(U_\rho - U_\sigma)$ fließt aus $\nu$ ab und in $\mu$ hinein, mit denselben Vorzeichen wie beim Leitwert; er
multipliziert aber die Spannungen der Knoten $\rho$ und $\sigma$, deshalb stehen die Einträge in deren Spalten. Ein Leitwert ist der Sonderfall einer
Quelle, die von ihrer eigenen Spannung gesteuert wird, mit $\rho$ gleich $\nu$ und $\sigma$ gleich $\mu$.

**Zeilen und Spalten summieren sich zu null.** Jedes Muster hat in jeder Zeile und in jeder Spalte einmal $+x$ und einmal $-x$. In der Matrix mit dem
Bezugsknoten ist deshalb jede Zeilen- und jede Spaltensumme null, eine Probe beim Aufstellen.

**Streichen.** Die Spalte 0 multipliziert $U_0 = 0$ und kann weg. Die Zeile 0 ist die Knotenregel am Bezugsknoten, die aus den übrigen folgt. Übrig bleibt
$\mathbf Y$. Im Bild: Die Nullmarke braucht weder ein Standrohr noch eine eigene Bilanz.
:::

Eine gesteuerte Quelle macht die Matrix unsymmetrisch: Sie trägt in der Zeile $\nu$ etwas in der Spalte $\rho$ ein, aber in der Zeile $\rho$ nichts in der
Spalte $\nu$. Der Satz über Symmetrie und Lösbarkeit gilt dann nicht mehr, denn eine gesteuerte Quelle kann Leistung abgeben. Meist ist das System trotzdem
lösbar, aber nicht immer.

Im __Kleinsignalersatzschaltbild__ eines Verstärkers, dem linearen Modell dafür, wie er auf kleine Änderungen um seinen Arbeitspunkt reagiert, den
Ruhezustand, um den die Signale schwanken, liegt am
Eingang, dem Knoten 1, der Eingangsleitwert $G_i$ nach Masse. Am Ausgang, dem Knoten 2, zieht eine von $U_1$ gesteuerte Quelle den Strom $g_mU_1$ nach Masse,
parallel zum Ausgangsleitwert $G_o$ und zur Last $G_L$. Das ist das Y-Ersatzschaltbild aus dem Artikel über Zweitore, ohne Rückwirkung vom Ausgang auf den
Eingang. Für diese Grundstruktur gilt die Regel, die das Skript für nahezu alle Verstärker hervorhebt, Spannungsverstärkung gleich minus Steilheit mal
Lastwiderstand:

:::formel
$$A_u = \frac{U_2}{U_1} = -\frac{g_m}{G_o + G_L} = -g_m\,(R_o \parallel R_L).$$
:::

**So liest man das:** Die __Spannungsverstärkung__ $A_u$ ist das Verhältnis von Ausgangs- zu Eingangsspannung, eine Zahl ohne Einheit. Das Minus heißt, dass
die Ausgangsspannung sinkt, wenn die Eingangsspannung steigt. $R_o \parallel R_L$ ist die Parallelschaltung von Ausgangs- und Lastwiderstand, allgemein aller
Widerstände, die am Ausgangsknoten nach Masse liegen. Speisen mehrere von $U_1$ gesteuerte Quellen in den Ausgangsknoten, addieren sich ihre Steilheiten.

**Im Bild:** Eine Pumpe am Ausgangsknoten, die ein Fühler am Eingangspegel steuert, zieht Wasser ab. Der Ausgangspegel sinkt unter die Nullmarke, bis durch
die Rohre ebenso viel von unten nachfließt; je enger die Rohre, desto tiefer.

:::herleitung
**Die Zeile des Ausgangsknotens.** Die gesteuerte Quelle zieht $g_mU_1$ ab, die beiden Leitwerte $(G_o + G_L)U_2$; Quellströme gibt es dort keine:

$$g_m\,U_1 + (G_o + G_L)\,U_2 = 0, \qquad U_2 = -\frac{g_m}{G_o + G_L}\,U_1.$$

**Parallelschaltung.** Leitwerte, die parallel am Ausgang liegen, addieren sich; der Kehrwert ihrer Summe ist die Parallelschaltung der Widerstände. Weil
der Ausgang nicht auf den Eingang zurückwirkt, hat die Zeile des Eingangs keinen Eintrag in der Spalte von $U_2$, und das Verhältnis gilt, wie auch immer
der Eingang angesteuert wird.
:::

::::beispiel Ein Verstärker aus der Netzliste
**(a) Ohne Gegenkopplung.** Ein Verstärker im Kleinsignalersatzschaltbild, beschrieben durch eine __Netzliste__: eine Zeile je Bauteil mit Name, Knoten und
Wert, bei der gesteuerten Quelle erst die beiden Knoten, zwischen denen ihr Strom fließt, dann die beiden steuernden Knoten. Einheiten schreibt eine
Netzliste nicht, nur Vorsätze: `2u` für $2\,\mu\text{A}$, `2.5k` für $2{,}5\,\text{k}\Omega$, `40m` für $40\,\text{mS}$.

```
Iq  0 1      2u
Rq  1 0      2.5k
Ri  1 0      2.5k
Gm  2 0 1 0  40m
Ro  2 0      20k
RL  2 0      5k
```

Die Stromquelle schiebt ihren Strom aus Masse in den Eingang, die gesteuerte Quelle führt ihren vom Knoten 2 nach Masse. Als Leitwerte:

$$I_q = 2\,\mu\text{A}, \qquad G_q = G_i = 0{,}4\,\text{mS}, \qquad g_m = 40\,\text{mS}, \qquad G_o = 0{,}05\,\text{mS}, \qquad G_L = 0{,}2\,\text{mS}.$$

**Die Muster eintragen.** Mit dem Bezugsknoten 0 als erster Zeile und Spalte, in mS und mA. Die Stromquelle bringt $-0{,}002$ in die Zeile 0 und $+0{,}002$
in die Zeile 1 des Quellvektors. $R_q$ und $R_i$ tragen je $\pm0{,}4$ an den Plätzen der Knoten 0 und 1 ein, $R_o$ und $R_L$ zusammen $\pm0{,}25$ an denen
der Knoten 0 und 2. Die gesteuerte Quelle führt ihren Strom von 2 nach 0 und wird von 1 und 0 gesteuert: $+40$ in der Zeile 2 unter der Spalte 1, $-40$ unter der
Spalte 0, und in der Zeile 0 dieselben Zahlen mit umgekehrtem Vorzeichen:

$$\begin{pmatrix} 41{,}05 & -40{,}8 & -0{,}25 \\ -0{,}8 & 0{,}8 & 0 \\ -40{,}25 & 40 & 0{,}25 \end{pmatrix}\text{mS}\begin{pmatrix} U_0 \\ U_1 \\ U_2 \end{pmatrix} = \begin{pmatrix} -0{,}002 \\ 0{,}002 \\ 0 \end{pmatrix}\text{mA}.$$

Jede Zeile und jede Spalte summiert sich zu null. Nach dem Streichen von Zeile und Spalte 0 bleibt

$$\begin{pmatrix} 0{,}8 & 0 \\ 40 & 0{,}25 \end{pmatrix}\text{mS}\begin{pmatrix} U_1 \\ U_2 \end{pmatrix} = \begin{pmatrix} 0{,}002 \\ 0 \end{pmatrix}\text{mA},$$

unsymmetrisch: Die $40$ unten links hat oben rechts kein Gegenstück.

**Lösen.** Die erste Zeile gibt $U_1$, die zweite die Regel für die Verstärkung, mit der Parallelschaltung von $20$ und $5\,\text{k}\Omega$, also
$4\,\text{k}\Omega$:

$$U_1 = \frac{0{,}002\,\text{mA}}{0{,}8\,\text{mS}} = 2{,}5\,\text{mV}, \qquad A_u = -40\,\text{mS}\cdot4\,\text{k}\Omega = -160, \qquad U_2 = -160\cdot2{,}5\,\text{mV} = -0{,}4\,\text{V}.$$

**(b) Mit Gegenkopplung.** Zwischen den unteren Anschluss der gesteuerten Quelle und Masse kommt ein Widerstand $R_E$, wie der Emitterwiderstand eines
Transistors. Dadurch entsteht der Knoten 3: $R_i$ und $R_o$ enden jetzt an ihm statt an Masse, die gesteuerte Quelle führt ihren Strom von 2 nach 3, und
ihre Steuerspannung ist $U_1 - U_3$. Die geänderten und neuen Zeilen der Netzliste:

```
Ri  1 3      2.5k
Gm  2 3 1 3  40m
Ro  2 3      20k
RE  3 0      500
```

Mit dem Leitwert $G_E = 2\,\text{mS}$ von $R_E$ kommen jetzt alle Muster ganz vor, die gesteuerte Quelle mit vier Einträgen in den Spalten 1 und 3:

$$\begin{pmatrix} 0{,}8 & 0 & -0{,}4 \\ 40 & 0{,}25 & -40{,}05 \\ -40{,}4 & -0{,}05 & 42{,}45 \end{pmatrix}\text{mS}\begin{pmatrix} U_1 \\ U_2 \\ U_3 \end{pmatrix} = \begin{pmatrix} 0{,}002 \\ 0 \\ 0 \end{pmatrix}\text{mA}.$$

Nach Cramer, mit der Determinante $3{,}648\,\text{mS}^3$:

$$U_1 = 4{,}72\,\text{mV}, \qquad U_2 = -43{,}85\,\text{mV}, \qquad A_u = \frac{U_2}{U_1} = -9{,}29.$$

Die Verstärkung ist auf ein Siebzehntel gesunken, liegt aber nahe bei $-R_L/R_E$, also $-10$, und hängt kaum noch vom Transistor ab: Mit doppelter Steilheit,
$80\,\text{mS}$, ergibt dieselbe Rechnung $-9{,}63$, ohne Gegenkopplung würden aus $-160$ dagegen $-320$. Das ist der Zweck der __Gegenkopplung__: Der Strom
durch $R_E$ hebt den Knoten 3 an und verringert die Steuerspannung, die Wirkung bremst ihre eigene Ursache.

:::herleitung
**Warum $-R_L/R_E$.** Bei großer Steilheit genügt eine kleine Steuerspannung, hier $0{,}28\,\text{mV}$; der Knoten 3 folgt dem Eingang fast genau. Durch
$R_E$ fließt dann etwa $U_1/R_E$, und fast dieser ganze Strom kommt über die gesteuerte Quelle aus dem Knoten 2, der ihn über $R_L$ nachzieht, solange $R_o$
groß ist:

$$I_E \approx \frac{U_1}{R_E}, \qquad U_2 \approx -R_L\,I_E = -\frac{R_L}{R_E}\,U_1.$$

Im Bild: Die gebremste Pumpe fördert so viel, wie das Rohr unter ihr abführt, und das bestimmt der Eingangspegel, nicht die Pumpe.
:::

**(c) Mitkopplung.** Am Knoten 1 liege ein Leitwert $G = 1\,\text{mS}$ nach Masse und eine gesteuerte Quelle, die den Strom $g_mU_1$ mit
$g_m = 1\,\text{mS}$ aus Masse in den Knoten 1 schiebt, also in ihren eigenen Steuerknoten. Ihr Strom fließt von 0 nach 1 und wird von 1 und 0 gesteuert;
ihr Muster bringt deshalb in der Zeile 1 unter der Spalte 1 den Eintrag $-g_m$:

$$Y_{11} = G - g_m = 0.$$

Die Matrix ist singulär, jede Spannung $U_1$ erfüllt die Gleichung, denn die Quelle liefert bei jeder Spannung genau so viel, wie der Leitwert abführt. Das
widerspricht dem Satz über die Lösbarkeit nicht, denn eine gesteuerte Quelle ist kein Leitwert. Eine solche __Mitkopplung__, bei der die Wirkung ihre
eigene Ursache verstärkt, steht an der Grenze zur Instabilität.

**Im Bild:** Eine Pumpe, die ein Fühler am Eingangspegel steuert, zieht am Ausgang Wasser ab (a). Ein Rohr unter ihr hebt ihren Fußpunkt an und bremst sie
(b). Eine Pumpe, die in ihr eigenes Standrohr fördert, hält jeden Pegel (c).
::::

Das Skript rechnet dieselben beiden Schaltungen mit Buchstaben, in den Beispielen zu Bild 9.5 und Bild 9.7. Im ersten steht im Zähler von Gleichung 9.5 oben
links $G_q$ statt $G_q + G_i$, ohne Folgen, weil der Eintrag mit null multipliziert wird; die Steilheit heißt mal $g$, mal $g_m$. Im zweiten sagt Schritt 6,
$G_o + G_L$ werde bei $Y_{22}$, $Y_{33}$, $Y_{23}$ und $Y_{32}$ eingetragen. $G_L$ liegt aber zwischen dem Knoten 2 und Masse und gehört nur nach $Y_{22}$;
die Matrix 9.12 ist trotzdem richtig. Die Determinanten 9.13 und 9.14 rechnen dagegen mit Einträgen, die nicht zu 9.12 passen, mit $+G_L$ in $Y_{23}$,
$Y_{32}$ und $Y_{33}$, und das Ergebnis 9.15 ist falsch. Richtig ist, in den Bezeichnungen des Skripts mit $G_s$ für den Gegenkopplungsleitwert, hier
$G_E$:

$$\frac{U_2}{I_q} = \frac{G_i\,G_o - g_m\,G_s}{D},$$

$$\begin{aligned} D = {}& \big[(G_q + G_i)\,G_s + G_i\,G_q\big](G_o + G_L) \\ &+ G_L\big[G_q\,(g_m + G_o) + G_i\,G_o\big]. \end{aligned}$$

:::herleitung
**Die Determinante.** Mit drei Abkürzungen für die Diagonale der Matrix 9.12:

$$a = G_q + G_i, \qquad b = G_o + G_L, \qquad c = G_s + g_m + G_i + G_o.$$

Entwickelt nach der ersten Zeile:

$$D = a\,\big[b\,c - G_o\,(g_m + G_o)\big] - G_i\,\big[b\,(g_m + G_i) - g_m\,G_o\big].$$

Nach $G_o$ und $G_L$ sortiert, mit $b$ ausgeschrieben:

$$D = G_o\,\big[a\,(G_s + G_i) - G_i^2\big] + G_L\,\big[a\,c - G_i\,(g_m + G_i)\big].$$

Die beiden Klammern ausmultipliziert:

$$a\,(G_s + G_i) - G_i^2 = (G_q + G_i)\,G_s + G_i\,G_q,$$

$$\begin{aligned} a\,c - G_i\,(g_m + G_i) = {}& (G_q + G_i)\,G_s + G_i\,G_q \\ &+ G_q\,(g_m + G_o) + G_i\,G_o. \end{aligned}$$

Das ist $D$ aus der Formel.

**Die Zählerdeterminante.** In der zweiten Spalte steht jetzt die rechte Seite mit $I_q$ oben und sonst Nullen; entwickelt nach dieser Spalte:

$$\begin{aligned} D_2 &= -I_q\,\big[g_m\,c - (g_m + G_o)(g_m + G_i)\big] \\ &= (G_i\,G_o - g_m\,G_s)\,I_q. \end{aligned}$$

**Die Probe.** Mit kurzgeschlossenem Ausgang, $G_L$ gegen unendlich, muss $U_2$ verschwinden. Die richtige Formel geht dann gegen null, die des Skripts gegen
$G_i/[(G_q + G_i)G_s + G_iG_q]$. Mit den Zahlen des Verstärkers ergibt die richtige Formel $-21{,}92\,\text{k}\Omega$, wie die Lösung des
Gleichungssystems. Den Grenzwert für $G_s$ gegen unendlich, den das Skript prüft, erfüllen beide Formeln. Im Bild: Ein kurzgeschlossener Ausgang hängt fest
an der Nullmarke, sein Pegel kann nicht ausschlagen.
:::

So arbeiten Schaltungssimulatoren. Aus dem gezeichneten Schaltplan erzeugen sie eine Netzliste und daraus Zeile für Zeile die Matrix. Wie groß sie wird,
muss vorher niemand wissen: Taucht ein neuer Knoten auf, wächst sie um eine Zeile und eine Spalte. Das Format stammt von SPICE, einem Simulator, der Anfang
der 1970er-Jahre an der University of California in Berkeley entstand, in FORTRAN geschrieben und mit Lochkarten gefüttert; fast alle Simulatoren lesen es
bis heute. Die Matrizen großer Schaltungen sind __dünn besetzt__, englisch sparse: Jeder Knoten ist nur mit wenigen anderen verbunden, fast alle Einträge
sind null. Simulatoren speichern nur die übrigen und lösen mit Verfahren, die das ausnutzen. Für kleine Systeme von Hand, bis zur Größe vier, empfiehlt das
Skript die Cramersche Regel.

:::grafik
Szene: get1/knotenpotentialverfahren/01-eintragsmuster · Vorlage: stamp-matrix
Links die Netzliste des Verstärkers als sechs Textzeilen, rechts daneben das Schaltbild mit den Knoten 0, 1 und 2, darunter eine leere $3\times3$-Matrix mit
den Zeilen und Spalten 0, 1, 2 und einem Quellvektor. Ein Cursor geht die Netzliste Zeile für Zeile durch: Das gelesene Bauteil leuchtet im Schaltbild auf,
und sein Muster fliegt als kleines Kärtchen in die Matrix, beim Leitwert auf die vier Plätze seiner Knoten, bei der gesteuerten Quelle in die Zeilen 2 und 0,
aber unter die Spalten 1 und 0 der steuernden Knoten, bei der Stromquelle nur in den Vektor; Einträge am selben Platz addieren sich sichtbar. Neben jeder
Zeile und unter jeder Spalte eine Summenanzeige, die immer null zeigt. Am Ende werden Zeile und Spalte 0 grau durchgestrichen, übrig bleibt die
$2\times2$-Matrix mit der hervorgehobenen $40$ ohne Gegenstück. Ein zweiter Durchlauf zeigt die Netzliste mit Gegenkopplung und die $3\times3$-Matrix mit dem
vollständigen Muster der gesteuerten Quelle. Kernaussage: Jedes Bauteil trägt unabhängig von allen anderen ein festes Muster ein; so baut ein Simulator die
Matrix. (Rot = gerade gelesenes Bauteil, blau = Knotenspannungen, orange = Muster und Einträge, grau = gestrichene Zeile und Spalte.)
:::

## Exkurs: Die modifizierte Knotenpotentialanalyse

Was die Leitwertmatrix nicht fassen kann, sind ideale Spannungsquellen, denn ihr Strom hängt von keiner Spannung ab. Die __modifizierte
Knotenpotentialanalyse__, englisch modified nodal analysis, kurz MNA, nimmt ihn deshalb als weitere Unbekannte auf und die Quellengleichung als weitere
Gleichung. Für jede ideale Spannungsquelle wächst das System um eine Zeile und eine Spalte; die Ströme der Quellen bilden den Vektor $\vec I_V$, ihre
Quellenspannungen den Vektor $\vec U_q$. Der Strom einer Quelle zählt wie im Skript vom Knoten an ihrem Pluspol durch die Quelle zum Knoten an ihrem
Minuspol:

:::formel
$$\begin{pmatrix} \mathbf Y & \mathbf C \\ \mathbf B & \mathbf 0 \end{pmatrix}\begin{pmatrix} \vec U \\ \vec I_V \end{pmatrix} = \begin{pmatrix} \vec I_q \\ \vec U_q \end{pmatrix}, \qquad \mathbf C = \mathbf B^{\mathsf T}.$$
:::

**So liest man das:** Die oberen Zeilen sind die Knotenregeln wie bisher. In der Spalte einer Spannungsquelle steht $+1$ in der Zeile ihres Pluspols, aus
dem ihr Strom in die Quelle abfließt, und $-1$ in der Zeile ihres Minuspols, in den er aus ihr ankommt; das ist die Matrix $\mathbf C$. Die unteren Zeilen
sind die Quellengleichungen, die Differenz der Knotenspannungen an den Polen ist die Quellenspannung. Ihre Koeffizienten $+1$ und $-1$ bilden die Matrix
$\mathbf B$, und $\mathbf C$ ist $\mathbf B$ an der Diagonale gespiegelt, __transponiert__. Liegt ein Pol am Bezugsknoten, fällt sein Eintrag weg.

Ein Widerstand von $0\,\Omega$ und ein idealer Strommesser sind Spannungsquellen mit $0\,\text{V}$; in der MNA wird ihr Strom zur Unbekannten. Ebenso
behandeln Simulatoren eine Spule, die bei Gleichstrom wie ein Kurzschluss wirkt und deren Leitwert dort unendlich wäre. Das ist die Lösung, die das Skript
für __Impedanzen__ ankündigt, die verallgemeinerten Widerstände, wenn sie zu null werden.

**Im Bild:** Für jede Druckerhöhungspumpe führt man ihren Durchfluss als weitere Unbekannte mit und schreibt ihren festen Pegelunterschied als weitere
Gleichung dazu.

:::herleitung
**Die Knotenregeln.** Am Knoten des Pluspols fließt zusätzlich der Strom der Quelle in sie ab, am Knoten des Minuspols kommt er aus ihr an. In diesen
beiden Zeilen steht er deshalb mit $+1$ und $-1$; das ist die Spalte der Quelle in $\mathbf C$.

**Die Quellengleichung.** Nach dem Satz über Zweigspannungen ist die Spannung zwischen den Polen die Differenz der Knotenspannungen, mit $\nu$ am Pluspol
und $\mu$ am Minuspol:

$$U_\nu - U_\mu = U_q.$$

Ihre Koeffizienten bilden die Zeile der Quelle in $\mathbf B$, und weil kein Quellenstrom in ihr vorkommt, steht rechts unten die Null. Dieselben Zahlen
$+1$ und $-1$ stehen in Zeile und Spalte, also ist $\mathbf C$ das Transponierte von $\mathbf B$. Im Bild: Der Durchfluss der Pumpe zählt in den Bilanzen
ihrer beiden Knoten, ihr Pegelunterschied ist eine eigene Gleichung.
:::

::::beispiel Schwebende Quelle und Strommesser in der MNA
**(a) Die schwebende Spannungsquelle.** Das Netz von oben mit $R_1$ und $R_2$ nach Masse, der Quelle $U_q$ zwischen den Knoten 1 und 2 mit Pluspol am
Knoten 2 und der Stromquelle $I_q$ in den Knoten 1:

$$R_1 = 2\,\text{k}\Omega, \qquad R_2 = 4\,\text{k}\Omega, \qquad U_q = 6\,\text{V}, \qquad I_q = 3\,\text{mA}.$$

Unbekannt sind $U_1$, $U_2$ und der Strom $I_V$, der am Knoten 2 in den Pluspol fließt. Leitwerte in mS, Spannungen in V, Ströme in mA:

$$\begin{pmatrix} 0{,}5 & 0 & -1 \\ 0 & 0{,}25 & 1 \\ -1 & 1 & 0 \end{pmatrix}\begin{pmatrix} U_1 \\ U_2 \\ I_V \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ 6 \end{pmatrix}.$$

Die Spalte der Quelle hat $+1$ beim Pluspol, dem Knoten 2, und $-1$ beim Minuspol, dem Knoten 1; die letzte Zeile ist die Quellengleichung. Die Lösung:

$$U_1 = 2\,\text{V}, \qquad U_2 = 8\,\text{V}, \qquad I_V = -2\,\text{mA}.$$

Dasselbe wie mit dem Superknoten. Das Minus heißt: Der Strom kommt am Pluspol aus der Quelle heraus, sie gibt Leistung ab.

**(b) Ein Strommesser aus 0 V.** Der Verstärker von oben ohne Gegenkopplung, am Eingang nur die ideale Stromquelle $I_{in}$ und $R_i$, am Ausgang statt $R_L$
eine ideale Spannungsquelle mit $0\,\text{V}$, Pluspol am Knoten 2. Sie ist ein idealer Strommesser:

$$I_{in} = 2\,\mu\text{A}, \qquad G_i = 0{,}4\,\text{mS}, \qquad g_m = 40\,\text{mS}, \qquad G_o = 0{,}05\,\text{mS}.$$

Ihr Minuspol liegt am Bezugsknoten und hat keinen Eintrag; die letzte Zeile hält den Ausgang auf null:

$$\begin{pmatrix} 0{,}4 & 0 & 0 \\ 40 & 0{,}05 & 1 \\ 0 & 1 & 0 \end{pmatrix}\begin{pmatrix} U_1 \\ U_2 \\ I_V \end{pmatrix} = \begin{pmatrix} 0{,}002 \\ 0 \\ 0 \end{pmatrix}.$$

Die Lösung und die Stromverstärkung:

$$U_1 = 5\,\text{mV}, \qquad U_2 = 0, \qquad I_V = -0{,}2\,\text{mA}, \qquad \frac{I_V}{I_{in}} = -100 = -\frac{g_m}{G_i}.$$

Der Ausgang liegt fest auf $0\,\text{V}$, durch $R_o$ fließt nichts; den ganzen Strom der gesteuerten Quelle liefert der Strommesser, daher das Minus. Das
Verhältnis $g_m/G_i$, hier 100, ist die Stromverstärkung bei kurzgeschlossenem Ausgang, eine Kenngröße von Transistoren. Die Frequenz, bei der sie auf eins
sinkt, heißt __Transitfrequenz__ und beschreibt, wie schnell ein Transistor ist; dafür braucht das Modell Kapazitäten, die hier fehlen.

**Im Bild:** Die Druckerhöhungspumpe bekommt ihren eigenen Durchflussmesser als Unbekannte (a). Ein Strommesser ist eine Pumpe mit dem Pegelunterschied
null, die anzeigt, wie viel durch sie fließt (b).
::::

Treibt man den Eingang statt mit einer Stromquelle mit einer idealen Spannungsquelle, wie in Bild 9.11 des Skripts, liefert die MNA die Verstärkung in
einem Schritt. Das Skript erhält dort $-g_m/G_o$, weil Bild 9.11 die Last $G_L$ weglässt, obwohl es den Verstärker aus Bild 9.5 analysieren will; mit ihr
ergibt sich wieder $-g_m/(G_o + G_L)$ wie in seiner Gleichung 9.11.

## Bedeutung und Ausblick

Das Knotenpotentialverfahren ist das Werkzeug der Wahl für Netze mit wenigen Knoten und vielen parallelen Zweigen. Man liest die Leitwertmatrix aus dem
Schaltbild ab, prüft die Symmetrie und löst ein kleines System; reale Spannungsquellen werden zu Ersatzstromquellen, ideale erledigt der Bezugsknoten an
ihrem Pol oder ein Superknoten. Ob Knoten oder Maschen schneller sind, entscheidet der Vergleich von $k - 1$ und $z - k + 1$.

In der Form der modifizierten Knotenpotentialanalyse ist es die Grundlage praktisch aller Schaltungssimulatoren. Dort muss niemand Maschen wählen oder
Quellen umwandeln, jedes Bauteil trägt sein Muster unabhängig von den anderen ein. Bei Wechselstrom bleibt das Verfahren dasselbe, nur stehen komplexe
Admittanzen in der Matrix; deshalb schreibt das Skript $\mathbf Y$.

Die folgenden Kapitel verlassen die linearen Netze. Halbleiterbauelemente wie die Diode haben gekrümmte Kennlinien. Ein Simulator ersetzt sie in einem
angenommenen Arbeitspunkt durch Leitwerte und Quellen, löst das lineare System, verbessert den Arbeitspunkt und wiederholt das, bis er sich nicht mehr
ändert; jeder dieser Schritte ist ein Knotenpotentialverfahren wie hier. Der nächste Artikel beginnt mit den Grundlagen: Halbleiter und das Bändermodell.

:::kern
- Die Knotenspannungen gegen einen Bezugsknoten sind die Unbekannten; jede Zweigspannung ist eine Differenz von ihnen.
- Damit ist die Maschenregel von selbst erfüllt, und es bleiben $n=k-1$ Knotengleichungen.
- Diagonale: Summe aller Leitwerte am Knoten; daneben: der Koppelleitwert, immer mit Minus.
- Rechts: Quellströme in den Knoten hinein mit Plus, hinaus mit Minus.
- Reale Spannungsquelle: Kurzschlussstrom $G_qU_q$ am Knoten des Pluspols, $G_q$ in die Matrix.
- Ein einziger Knoten: das leitwertgewichtete Mittel der Quellenspannungen, der Satz von Millman.
- Ein Vorwiderstand einer idealen Stromquelle fällt aus der Matrix heraus.
- Ohne gesteuerte Quellen ist $\mathbf Y$ symmetrisch und positiv definit; das System ist eindeutig lösbar, solange kein Knoten schwebt.
- Das Knotenpotentialverfahren ist kürzer, wenn $z>2k-2$.
- Ideale Spannungsquelle: Bezugsknoten an einen ihrer Pole, sonst Superknoten; die MNA nimmt ihren Strom als Unbekannte.
- Jedes Bauteil hat ein Eintragsmuster; gesteuerte Quellen stehen in den Spalten ihrer Steuerknoten und machen $\mathbf Y$ unsymmetrisch.
- Spannungsverstärkung gleich minus Steilheit mal Lastwiderstand: $A_u=-g_m\,(R_o\parallel R_L)$.
:::

:::quiz
F: Warum braucht das Knotenpotentialverfahren nur $k-1$ Gleichungen?
A: Mit den Knotenspannungen als Unbekannten ist jede Zweigspannung eine Differenz, und um jede Masche ergibt sich eine Teleskopsumme null: Die Maschenregel gilt von selbst. Es bleiben die Knotenregeln der $k-1$ Knoten außer dem Bezugsknoten, dessen Gleichung aus den übrigen folgt; bei der Brücke drei Knotenspannungen statt sechs Zweigströmen.
F: Nach welchen Regeln liest man die Knotenleitwertmatrix ab, und warum sind die Koppeleinträge immer negativ?
A: Auf der Diagonale steht die Summe aller Leitwerte am Knoten, daneben der Koppelleitwert mit Minus, rechts die Quellströme in den Knoten. Negativ, weil alle Knotenspannungen zum selben Bezugsknoten zählen und eine höhere Nachbarspannung Strom zum Knoten hin treibt. Beim Netz mit drei Knoten stehen $4$, $8$ und $5\,\text{mS}$ auf der Diagonale, und es ergeben sich $5$, $2$ und $1\,\text{V}$.
F: Wie geht eine reale Spannungsquelle ins Verfahren ein, und was sagt der Satz von Millman?
A: Als Ersatzstromquelle: ihr Kurzschlussstrom $G_qU_q$ rechts beim Knoten am Pluspol, ihr Innenleitwert in der Matrix; das folgt aus ihrem Zweigstrom. Hat das Netz nur einen Knoten, ist dessen Spannung das leitwertgewichtete Mittel der Quellenspannungen; für Ladegerät, Batterie und Last $148\,\text{A}/12{,}5\,\text{S}=11{,}84\,\text{V}$ aus einer einzigen Gleichung.
F: Warum taucht der Vorwiderstand einer idealen Stromquelle in der Matrix nicht auf?
A: Die ideale Stromquelle legt den Zweigstrom fest, wie groß der Widerstand in Reihe auch ist; der Zweig steht nur als Quellstrom rechts. Der Widerstand zeigt sich erst in der Spannung an der Quelle: Am Knoten mit $10\,\text{V}$, $2$ und $3\,\text{k}\Omega$ und $2\,\text{mA}$ ergeben sich $8{,}4\,\text{V}$, an der Quelle samt $5\,\text{k}\Omega$ dann $18{,}4\,\text{V}$.
F: Warum ist das System eindeutig lösbar, und wann versagt das?
A: Die Matrix ist symmetrisch, und $\sum Y_{\nu\mu}U_\nu U_\mu$ ist die Leistung $\sum G_jU_j^2$ der Leitwerte, positiv, sobald eine Knotenspannung nicht null ist; deshalb ist $\mathbf Y$ umkehrbar. Das setzt voraus, dass jeder Knoten über Leitwerte am Bezugsknoten hängt: Ein Knoten nur zwischen Stromquellen schwebt, seine Zeile ist null. Auch gesteuerte Quellen heben den Satz auf, etwa bei Mitkopplung mit $g_m$ gleich $G$.
F: Wann ist das Knotenpotentialverfahren kürzer als das Maschenstromverfahren?
A: Wenn $k-1<z-k+1$ ist, also $z>2k-2$, das heißt, wenn an den Knoten im Mittel mehr als $4-4/k$ Zweige enden. Ein Reihenkreis aus Quelle und vier Widerständen braucht eine Maschen-, aber vier Knotengleichungen; Ladegerät, Batterie und Last brauchen eine Knoten-, aber zwei Maschengleichungen.
F: Wie behandelt man ideale Spannungsquellen von Hand?
A: Liegt ein Pol am Bezugsknoten, ist die Knotenspannung am anderen bekannt, und die Gleichung dieses Knotens liefert nur noch den Quellstrom; bei der Brücke bleiben zwei Gleichungen mit $20{,}8$ und $14{,}4\,\text{V}$ und $2\,\text{A}$ aus der Quelle. Liegt die Quelle zwischen zwei anderen Knoten, bildet man einen Superknoten aus Quellengleichung und Knotenregel der Hülle, in der ihr Strom herausfällt; im Beispiel ergeben sich $2$ und $8\,\text{V}$ und $2\,\text{mA}$ durch die Quelle.
F: Was ist ein Eintragsmuster, und was ändern gesteuerte Quellen an der Matrix?
A: Der feste Beitrag eines Bauteils, unabhängig von allen anderen: Ein Leitwert trägt $\pm G$ an die vier Plätze seiner Knoten ein, eine unabhängige Stromquelle nur in den Quellvektor. Eine spannungsgesteuerte Stromquelle steht in den Zeilen ihrer Knoten, aber in den Spalten der steuernden Knoten, und macht $\mathbf Y$ unsymmetrisch. Für den Verstärker folgt $A_u=-g_m(R_o\parallel R_L)=-160$, mit Gegenkopplung über $500\,\Omega$ nur noch $-9{,}29$, nahe bei $-R_L/R_E$.
F: Wie macht die modifizierte Knotenpotentialanalyse ideale Spannungsquellen rechenbar?
A: Sie nimmt den Strom jeder idealen Spannungsquelle als weitere Unbekannte und ihre Quellengleichung als weitere Zeile auf; in der neuen Spalte und der neuen Zeile stehen $+1$ und $-1$ bei den Knoten ihrer Pole. So werden auch Kurzschlüsse und Strommesser zu 0-V-Quellen; am Verstärker misst eine solche Quelle die Stromverstärkung $-g_m/G_i=-100$.
F: Welche Unstimmigkeiten hat das Skript in Kapitel 9?
A: Es sagt, im Knotenpotentialverfahren gingen nur Stromquellen; ideale Spannungsquellen und Widerstände von $0\,\Omega$ lassen sich aber mit Bezugsknoten, Superknoten oder Zusammenfassen von Knoten behandeln. $G_{\mu\nu}$ ist zugleich Matrixeintrag und Koppelleitwert. In 9.5 steht $G_q$ statt $G_q+G_i$; im gegengekoppelten Beispiel trägt Schritt 6 $G_L$ falsch ein, die Determinanten 9.13 und 9.14 passen nicht zur Matrix 9.12, und das Ergebnis 9.15 ist falsch, es ergäbe bei kurzgeschlossenem Ausgang eine Spannung. Bild 9.11 lässt die Last weg.
:::
