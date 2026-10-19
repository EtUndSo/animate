---
title: Skalarfelder, Vektorfelder und die Jacobi-Matrix
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010100
summary: Von Grund auf – wie die Differentialrechnung von einer Variablen auf Abbildungen $f:\mathbb{R}^n\to\mathbb{R}^m$ erweitert wird. Aus der einen Ableitung $f'(x)$ wird eine ganze Matrix, die Jacobi-Matrix $Df$, die das Feld in der Nähe eines Punktes linear annähert. Mit der totalen Differenzierbarkeit und der Kettenregel $D(f\circ g)=Df\,Dg$ steht das Fundament der gesamten Vektoranalysis.
tags: Skalarfeld, Vektorfeld, partielle Ableitung, Jacobi-Matrix, totale Differenzierbarkeit, lineare Approximation, Kettenregel, stetig differenzierbar
---

:::grafik
Einstiegs-Animation: Links ein __Skalarfeld__ — ein Raum, dessen Temperatur ortsabhängig als Farbverlauf
gezeigt wird (jedem Punkt eine **Zahl**). Rechts ein __Vektorfeld__ — an jedem Punkt ein kleiner Pfeil, die
Strömungsgeschwindigkeit einer Flüssigkeit (jedem Punkt ein **Pfeil**). In der Mitte wird eine allgemeine
Abbildung $f:\mathbb{R}^n\to\mathbb{R}^m$ gezeigt: Ein kleines Gitterquadrat um einen Punkt $x_0$ wird durch $f$
auf ein leicht verzerrtes Viereck abgebildet — und ein danebenliegendes, durch die **Jacobi-Matrix** $Df(x_0)$
exakt *linear* verzerrtes Gitter deckt sich im Grenzfall kleiner Quadrate immer besser damit. Kernbotschaft:
Die Ableitung einer vektorwertigen Abbildung ist eine **Matrix**, die das Feld lokal linear macht.
:::

:::konzept
Die Höhere Mathematik III beginnt damit, die vertraute Differentialrechnung aus HM1 — Funktionen einer Variablen
$f:\mathbb{R}\to\mathbb{R}$ — auf **Felder** zu erweitern: Größen, die von mehreren Ortskoordinaten abhängen und
selbst mehrere Komponenten haben können. Die entscheidende Verallgemeinerung: Die Ableitung ist nicht mehr eine
Zahl $f'(x)$, sondern eine **Matrix**, die __Jacobi-Matrix__. Sie leistet dasselbe wie die eindimensionale
Ableitung — sie nähert die Abbildung in der Nähe eines Punktes durch eine **lineare** Abbildung an. Auf diesem
Baustein ruht die ganze Vektoranalysis (Gradient, Divergenz, Rotation, die Integralsätze), die den roten Faden
dieses Moduls bildet und in der Elektrotechnik hinter jedem Feld (E-Feld, Strömung, Wärme) steht.
:::

**Worum es geht:** Wir klären, was __Skalarfelder__ und __Vektorfelder__ sind, *warum* eine einzige Ableitung
nicht mehr genügt, führen die __Jacobi-Matrix__ und die __totale Differenzierbarkeit__ (lineare Approximation)
ein und verallgemeinern die __Kettenregel__ zur Matrixmultiplikation.

## Skalarfelder und Vektorfelder

Ein __Feld__ ordnet jedem Punkt des Raumes eine Größe zu. Je nachdem, ob diese Größe eine Zahl oder ein Vektor
ist, unterscheidet man zwei Typen — formal sind beide **Abbildungen** $f: U \to \mathbb{R}^m$ auf einer offenen
Menge $U \subset \mathbb{R}^n$:

- __Skalarfeld__ ($m = 1$): jedem Ort eine **Zahl**, $f: U \to \mathbb{R}$. Beispiel: die Temperatur
  $T(x,y,z)$ in einem Raum oder das elektrische Potential $\varphi(x,y,z)$.
- __Vektorfeld__ ($m \ge 2$): jedem Ort einen **Vektor**, $f = (f_1,\ldots,f_m)$. Beispiel: die
  Strömungsgeschwindigkeit einer Flüssigkeit oder das elektrische Feld $E(x,y,z) \in \mathbb{R}^3$.

Ein Punkt des Definitionsbereichs ist $x = (x_1,\ldots,x_n)$, die Abbildung hat Komponentenfunktionen
$f = (f_1,\ldots,f_m)$, wobei jedes $f_j = f_j(x_1,\ldots,x_n)$ eine gewöhnliche skalare Funktion mehrerer
Veränderlicher ist. „Offen" heißt dabei: Um jeden Punkt von $U$ liegt noch eine kleine Kugel ganz in $U$ — so hat
man in jeder Richtung „Platz" zum Ableiten.

:::grafik
Zwei Felder nebeneinander über demselben Ausschnitt der Ebene: links ein Skalarfeld als Höhen-/Farbkarte
(Temperatur), rechts ein Vektorfeld als Pfeilgitter (Strömung). Beschriftung: „Skalarfeld $f:U\to\mathbb{R}$ —
Zahl pro Punkt" vs. „Vektorfeld $f:U\to\mathbb{R}^m$ — Vektor pro Punkt".
:::

## Warum eine einzige Ableitung nicht mehr reicht

In einer Dimension misst die Ableitung $f'(x)$ eine einzige Steigung. Bei einer Abbildung $f:\mathbb{R}^n\to
\mathbb{R}^m$ gibt es aber viele Richtungen, in die man ableiten kann, und viele Komponenten, die sich ändern.
Der erste Baustein ist die __partielle Ableitung__ $\dfrac{\partial f_j}{\partial x_k}$: Man leitet die
Komponente $f_j$ nach **einer** Koordinate $x_k$ ab und hält alle anderen Koordinaten fest. Das ist nichts Neues
— es ist die gewöhnliche Ableitung einer Funktion, bei der nur eine Variable „lebendig" ist.

Für eine vollständige Beschreibung der lokalen Änderung braucht man **alle** solchen Ableitungen: jede der $m$
Komponenten nach jeder der $n$ Koordinaten. Das sind $m \cdot n$ Zahlen — und die ordnet man natürlicherweise in
einer **Matrix** an.

## Die Jacobi-Matrix

Für eine partiell differenzierbare Abbildung $f = (f_1,\ldots,f_m)$ heißt die Matrix aller ersten partiellen
Ableitungen die __Jacobi-Matrix__:

$$Df = \left(\frac{\partial f_j}{\partial x_k}\right)_{jk} = \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\[2mm] \vdots & \ddots & \vdots \\[1mm] \dfrac{\partial f_m}{\partial x_1} & \cdots & \dfrac{\partial f_m}{\partial x_n} \end{pmatrix} \in \mathbb{R}^{m \times n}.$$

Man liest sie zeilenweise: In **Zeile $j$** stehen die Ableitungen der Komponente $f_j$ nach allen Koordinaten,
in **Spalte $k$** die Ableitungen aller Komponenten nach $x_k$. Die Matrix hat $m$ Zeilen (so viele wie
Ziel-Komponenten) und $n$ Spalten (so viele wie Eingangs-Koordinaten).

**Der Spezialfall Skalarfeld** ($m=1$) ist besonders wichtig. Dann hat $Df$ nur **eine Zeile**, ist also ein
Zeilenvektor in $\mathbb{R}^{1\times n}$. Seinen transponierten Spaltenvektor nennt man den __Gradienten__:

$$\nabla f := \operatorname{grad} f = \left(\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_n}\right)^{\!T} \in \mathbb{R}^n, \qquad \nabla f = (Df)^{T}.$$

Das Symbol $\nabla$ (gesprochen „Nabla") ist dabei formal selbst ein Spaltenvektor von Ableitungsoperatoren,
$\nabla = \left(\frac{\partial}{\partial x_1},\ldots,\frac{\partial}{\partial x_n}\right)^{T}$. **Gradient und
Jacobi-Matrix sind zu unterscheiden**: Der Gradient ist ein (Spalten-)Vektor, die Jacobi-Matrix eines Skalarfelds
der zugehörige Zeilenvektor. Allgemeiner sind die Zeilen der Jacobi-Matrix gerade die (transponierten) Gradienten
der Komponentenfunktionen $f_j$. (Der Gradient bekommt im nächsten Artikel seine volle geometrische Bedeutung.)

:::grafik
Aufbau der Jacobi-Matrix als Schema: ein $m\times n$-Kasten; Zeile $j$ hervorgehoben als „Gradient von $f_j$",
Spalte $k$ hervorgehoben als „Ableitungen aller Komponenten nach $x_k$". Daneben der Skalar-Spezialfall: eine
einzelne Zeile $Df\in\mathbb{R}^{1\times n}$ und ihr transponierter Gradient $\nabla f\in\mathbb{R}^n$.
:::

**Eigenes Beispiel.** Für $f:\mathbb{R}^2\to\mathbb{R}^2$ mit $f(x_1,x_2) = (x_1^2 - x_2^2,\; 2x_1 x_2)$
(das ist das „Quadrieren" in der Ebene) sind die vier partiellen Ableitungen schnell gebildet:

$$Df = \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1} & \dfrac{\partial f_1}{\partial x_2} \\[2mm] \dfrac{\partial f_2}{\partial x_1} & \dfrac{\partial f_2}{\partial x_2} \end{pmatrix} = \begin{pmatrix} 2x_1 & -2x_2 \\[1mm] 2x_2 & 2x_1 \end{pmatrix}.$$

An jedem Punkt ist $Df$ also eine andere $2\times2$-Matrix — sie beschreibt, wie $f$ eine winzige Umgebung dieses
Punktes dreht und streckt.

## Totale Differenzierbarkeit: die lineare Approximation

Die bloße Existenz aller partiellen Ableitungen ist noch **nicht** die eigentliche Differenzierbarkeit. Das
wahre Kriterium knüpft an den Kern des Ableitungsbegriffs an: **lokale lineare Näherung**. Die Abbildung $f$
heißt __(total) differenzierbar__ an der Stelle $x_0$, wenn es eine Matrix $A \in \mathbb{R}^{m\times n}$ gibt,
die $f$ in der Nähe von $x_0$ linear annähert — und zwar so gut, dass der Fehler **schneller** als linear
verschwindet:

$$\lim_{x \to x_0} \frac{\lvert f(x) - f(x_0) - A\,(x - x_0)\rvert}{\lvert x - x_0\rvert} = 0.$$

In Worten: $f(x) \approx f(x_0) + A\,(x-x_0)$, und der Restfehler geht, relativ zum Abstand $\lvert x-x_0\rvert$,
gegen null. Existiert so ein $A$, dann ist es **eindeutig** und gerade die Jacobi-Matrix, $A = Df(x_0)$.
Insbesondere existieren dann alle partiellen Ableitungen.

**Stolperstein — die Umkehrung gilt nicht.** Aus der bloßen Existenz aller partiellen Ableitungen folgt im
Allgemeinen **nicht** die totale Differenzierbarkeit. Die partiellen Ableitungen „sehen" nämlich nur, was entlang
der Koordinatenachsen passiert; ein Feld kann dort glatt aussehen und trotzdem in schrägen Richtungen springen.
Eine **hinreichende** Bedingung, die den Fall rettet: Sind alle partiellen Ableitungen nicht nur vorhanden,
sondern auch **stetig**, so ist $f$ total differenzierbar. Man nennt $f$ dann __stetig differenzierbar__.

Allgemeiner heißt $f$ __$k$-mal stetig differenzierbar__, wenn alle partiellen Ableitungen bis zur Ordnung $k$
stetig sind; den Raum dieser Abbildungen auf $U$ schreibt man $C^k(U;\mathbb{R}^n)$. Für $k \ge 2$ sorgt der
__Satz von Schwarz__ dafür, dass die Reihenfolge der partiellen Ableitungen egal ist — gemischte Ableitungen
vertauschen, $\frac{\partial^2 f}{\partial x_j \partial x_k} = \frac{\partial^2 f}{\partial x_k \partial x_j}$.

:::grafik
Zum Differenzierbarkeits-Kriterium: eine gekrümmte Fläche $f$ über der $x_0$-Umgebung und die **Tangentialebene**
$f(x_0)+Df(x_0)(x-x_0)$. Ein Pfeil markiert den Abstand „Fläche − Tangentialebene", daneben die Notiz, dass
dieser Abstand schneller als $\lvert x-x_0\rvert$ gegen null geht. Zusätzlich ein kleines Gegenbeispiel-Icon:
„partielle Ableitungen existieren, aber nicht differenzierbar".
:::

## Die Kettenregel als Matrixprodukt

Der große Vorteil der Matrix-Schreibweise zeigt sich bei verketteten Abbildungen. Sind $g = (g_1,\ldots,g_m)$
(in $x$) und $f = f(y_1,\ldots,y_m)$ differenzierbar, so ist die Verkettung $(f\circ g)(x) = f(g(x))$
differenzierbar, und ihre Ableitung ist — ganz wie im Eindimensionalen „äußere mal innere Ableitung", nur jetzt
als **Matrizenprodukt** — die __Kettenregel__:

$$D(f\circ g)(x) = Df\big(g(x)\big)\,Dg(x).$$

Komponentenweise ausgeschrieben ist das die Summe über alle Zwischenvariablen $y_j$:

$$\frac{\partial (f\circ g)_i}{\partial x_k}(x) = \sum_{j=1}^{m} \frac{\partial f_i}{\partial y_j}\big(g(x)\big)\,\frac{\partial g_j}{\partial x_k}(x).$$

Das ist nichts anderes als die bekannte Regel „Zeile $i$ von $Df$ mal Spalte $k$ von $Dg$" der
Matrizenmultiplikation — die Zwischenvariablen $y_j$ sind der Summationsindex.

**Wichtiger Spezialfall (Feld entlang einer Kurve).** Läuft man mit einer differenzierbaren Kurve
$\gamma:[a,b]\to U$ durch ein Skalarfeld $h$, so ist die Änderung des Feldwerts längs der Kurve nach der
Kettenregel das **Skalarprodukt** aus Gradient und Geschwindigkeit:

$$\frac{d}{dt}\,h(\gamma(t)) = \nabla h(\gamma(t)) \cdot \dot\gamma(t).$$

Anschaulich: Wie schnell sich der Feldwert ändert, hängt davon ab, wie stark der Gradient (die Richtung des
steilsten Anstiegs) und die Bewegungsrichtung $\dot\gamma$ zusammenpassen. Läuft man senkrecht zum Gradienten,
ändert sich nichts — genau das sind später die Niveaulinien.

:::grafik
Eine Kurve $\gamma(t)$, die durch eine farbige Skalarfeld-Landschaft $h$ läuft; an einem Punkt der
Geschwindigkeitsvektor $\dot\gamma$ und der Gradient $\nabla h$ eingezeichnet, dazu der Winkel zwischen ihnen.
Beschriftung $\frac{d}{dt}h(\gamma(t))=\nabla h\cdot\dot\gamma$: maximal in Gradientenrichtung, null senkrecht dazu.
:::

:::kern
Die HM3-Differentialrechnung behandelt __Felder__, also Abbildungen $f:U\subset\mathbb{R}^n\to\mathbb{R}^m$ auf
offenen Mengen: __Skalarfelder__ ($m=1$, Zahl pro Punkt) und __Vektorfelder__ ($m\ge2$, Vektor pro Punkt). Die
Ableitung ist die __Jacobi-Matrix__ $Df=\left(\tfrac{\partial f_j}{\partial x_k}\right)_{jk}\in\mathbb{R}^{m\times n}$
(Zeilen = Gradienten der Komponenten). Für ein Skalarfeld ist $Df$ ein Zeilenvektor und $\nabla f=(Df)^T$ der
__Gradient__. __Totale Differenzierbarkeit__ an $x_0$ heißt: $f$ wird durch $f(x_0)+Df(x_0)(x-x_0)$ linear
approximiert mit überlinear kleinem Fehler ($\lim \tfrac{|f(x)-f(x_0)-Df(x_0)(x-x_0)|}{|x-x_0|}=0$); **Vorsicht**:
Existenz der partiellen Ableitungen allein genügt nicht, aber **stetige** partielle Ableitungen ($f\in C^1$)
reichen. Für $C^k$, $k\ge2$, vertauschen gemischte Ableitungen (__Schwarz__). Die __Kettenregel__ ist das
Matrixprodukt $D(f\circ g)=Df(g(x))\,Dg(x)$; entlang einer Kurve folgt $\tfrac{d}{dt}h(\gamma(t))=\nabla h\cdot\dot\gamma$.
:::

Die Jacobi-Matrix eines Skalarfelds hat uns schon den __Gradienten__ geliefert. Er ist der wichtigste erste
Differentialoperator der Vektoranalysis — er zeigt in die Richtung des steilsten Anstiegs und erzeugt aus einem
Potential ein Vektorfeld. Seine Geometrie und die besondere Klasse der __Gradientenfelder__ sind das Thema des
nächsten Artikels.
