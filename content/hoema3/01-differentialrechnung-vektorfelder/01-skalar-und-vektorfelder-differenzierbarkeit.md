---
title: Skalarfelder, Vektorfelder und die Jacobi-Matrix
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010100
summary: Von Grund auf – wie die Differentialrechnung von einer Variablen auf Abbildungen $f:\mathbb{R}^n\to\mathbb{R}^m$ erweitert wird. Aus der einen Ableitung $f'(x)$ wird eine Matrix, die Jacobi-Matrix $Df$, die das Feld nahe einem Punkt linear annähert. Mit totaler Differenzierbarkeit und der Kettenregel $D(f\circ g)=Df\,Dg$ steht das Fundament der Vektoranalysis.
tags: Skalarfeld, Vektorfeld, partielle Ableitung, Jacobi-Matrix, totale Differenzierbarkeit, lineare Approximation, Kettenregel, stetig differenzierbar
---

## Anschaulich

Stell dir zwei Landkarten vor. Auf der ersten steht an jedem Ort eine **Zahl** — die Temperatur. Das ist ein
__Skalarfeld__. Auf der zweiten steht an jedem Ort ein **Pfeil** — die Windrichtung und -stärke. Das ist ein
__Vektorfeld__.

Die Höhere Mathematik III beginnt mit der Frage: Was ist die **Ableitung** eines solchen Feldes? In HM1 war die
Ableitung einer Funktion $f:\mathbb{R}\to\mathbb{R}$ eine einzige Zahl $f'(x)$ — eine Steigung.

Bei einem Feld gibt es aber viele Richtungen, in die man gehen, und viele Komponenten, die sich ändern können.
Die Ableitung wird deshalb zu einer **Matrix**: der __Jacobi-Matrix__. Ihre Aufgabe bleibt dieselbe wie in HM1 —
sie nähert das Feld nahe einem Punkt durch eine **lineare** Abbildung an. Auf diesem einen Baustein ruht die
ganze Vektoranalysis (Gradient, Divergenz, Rotation, Integralsätze).

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-feld-und-jacobi · Vorlage: feld-linearisierung-2d
Links ein Skalarfeld als Farb-/Höhenkarte (Temperatur, Zahl pro Punkt), rechts ein Vektorfeld als Pfeilgitter
(Strömung, Pfeil pro Punkt). In der Mitte eine Abbildung $f:\mathbb{R}^2\to\mathbb{R}^2$: ein kleines
Gitterquadrat um $x_0$ wird von $f$ auf ein leicht verzerrtes Viereck abgebildet; ein daneben durch $Df(x_0)$
**linear** verzerrtes Gitter deckt sich im Grenzfall kleiner Quadrate immer besser damit. Kernaussage: Die
Ableitung einer vektorwertigen Abbildung ist eine Matrix, die das Feld lokal linear macht. (Rot = Abbildung $f$,
orange = lineare Näherung $Df$, grau = Gitter.)
:::

## Skalarfelder und Vektorfelder

Ein __Feld__ ordnet jedem Punkt des Raumes eine Größe zu. Formal ist es eine **Abbildung** $f:U\to\mathbb{R}^m$
auf einer offenen Menge $U\subset\mathbb{R}^n$. Je nach Zielgröße unterscheidet man zwei Typen:

- __Skalarfeld__ ($m=1$): jedem Ort eine **Zahl**, $f:U\to\mathbb{R}$. Beispiel: die Temperatur $T(x,y,z)$ oder
  das elektrische Potential $\varphi(x,y,z)$.
- __Vektorfeld__ ($m\ge2$): jedem Ort einen **Vektor**, $f=(f_1,\ldots,f_m)$. Beispiel: die
  Strömungsgeschwindigkeit oder das elektrische Feld $\vec E(x,y,z)\in\mathbb{R}^3$.

Ein Punkt des Definitionsbereichs ist $x=(x_1,\ldots,x_n)$. Die Abbildung hat Komponentenfunktionen
$f=(f_1,\ldots,f_m)$, wobei jedes $f_j=f_j(x_1,\ldots,x_n)$ eine gewöhnliche skalare Funktion mehrerer
Veränderlicher ist.

„**Offen**" heißt: Um jeden Punkt von $U$ liegt noch eine kleine Kugel ganz in $U$. So hat man in jeder Richtung
„Platz" zum Ableiten — eine stillschweigende, aber nötige Voraussetzung.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-skalarfeld-vs-vektorfeld · Vorlage: feld-vergleich-2d
Zwei Felder über demselben Ausschnitt der Ebene: links ein Skalarfeld als Farbkarte (Temperatur), rechts ein
Vektorfeld als Pfeilgitter (Strömung). Beschriftung: „Skalarfeld $f:U\to\mathbb{R}$ — Zahl pro Punkt" vs.
„Vektorfeld $f:U\to\mathbb{R}^m$ — Vektor pro Punkt".
:::

## Warum eine einzige Ableitung nicht reicht

In einer Dimension misst $f'(x)$ eine einzige Steigung. Bei einer Abbildung $f:\mathbb{R}^n\to\mathbb{R}^m$ gibt
es dagegen $n$ Richtungen, in die man ableiten kann, und $m$ Komponenten, die sich ändern.

Der erste Baustein ist die __partielle Ableitung__ $\dfrac{\partial f_j}{\partial x_k}$: Man leitet die Komponente
$f_j$ nach **einer** Koordinate $x_k$ ab und hält alle anderen fest. Das ist nichts Neues — es ist die gewöhnliche
Ableitung, bei der nur eine Variable „lebendig" ist.

Für die vollständige lokale Änderung braucht man **alle** diese Ableitungen: jede der $m$ Komponenten nach jeder
der $n$ Koordinaten. Das sind $m\cdot n$ Zahlen — und die ordnet man natürlicherweise in einer **Matrix** an.

## Die Jacobi-Matrix

Für eine partiell differenzierbare Abbildung $f=(f_1,\ldots,f_m)$ heißt die Matrix aller ersten partiellen
Ableitungen die __Jacobi-Matrix__:

:::formel Definition
$$Df = \left(\frac{\partial f_j}{\partial x_k}\right)_{jk} = \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\[2mm] \vdots & \ddots & \vdots \\[1mm] \dfrac{\partial f_m}{\partial x_1} & \cdots & \dfrac{\partial f_m}{\partial x_n} \end{pmatrix} \in \mathbb{R}^{m \times n}.$$
:::

**So liest man sie:** Der Eintrag in **Zeile $j$, Spalte $k$** ist $\partial f_j/\partial x_k$. Zeile $j$ sammelt
also die Ableitungen **einer** Komponente $f_j$ nach allen Koordinaten; Spalte $k$ die Ableitungen **aller**
Komponenten nach $x_k$.

Die Form passt genau zur Abbildung: $m$ Zeilen (so viele wie Ziel-Komponenten), $n$ Spalten (so viele wie
Eingangs-Koordinaten). Als lineare Abbildung schickt $Df$ einen Vektor aus $\mathbb{R}^n$ nach $\mathbb{R}^m$ —
dieselben Räume wie $f$ selbst.

**Der Spezialfall Skalarfeld** ($m=1$) ist besonders wichtig. Dann hat $Df$ nur **eine Zeile**, ist also ein
Zeilenvektor in $\mathbb{R}^{1\times n}$. Seinen transponierten Spaltenvektor nennt man den __Gradienten__:

$$\nabla f := \operatorname{grad} f = \left(\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_n}\right)^{\!T} \in \mathbb{R}^n, \qquad \nabla f = (Df)^{T}.$$

Das Symbol $\nabla$ („Nabla") ist dabei selbst ein Spaltenvektor von Ableitungsoperatoren,
$\nabla=\left(\frac{\partial}{\partial x_1},\ldots,\frac{\partial}{\partial x_n}\right)^{T}$.

**Gradient und Jacobi-Matrix sind zu unterscheiden:** Der Gradient ist ein (Spalten-)Vektor, die Jacobi-Matrix
eines Skalarfelds der zugehörige Zeilenvektor. Allgemeiner sind die Zeilen der Jacobi-Matrix gerade die
(transponierten) Gradienten der Komponenten $f_j$. (Die volle Geometrie des Gradienten kommt im nächsten Artikel.)

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-jacobi-aufbau · Vorlage: matrix-schema
Aufbau der Jacobi-Matrix als Schema: ein $m\times n$-Kasten; Zeile $j$ hervorgehoben als „Gradient von $f_j$",
Spalte $k$ als „Ableitungen aller Komponenten nach $x_k$". Daneben der Skalar-Spezialfall: eine einzelne Zeile
$Df\in\mathbb{R}^{1\times n}$ und ihr transponierter Gradient $\nabla f\in\mathbb{R}^n$. (Orange = die gerade
betrachtete Zeile/Spalte.)
:::

**Eigenes Beispiel.** Für $f:\mathbb{R}^2\to\mathbb{R}^2$ mit $f(x_1,x_2)=(x_1^2-x_2^2,\;2x_1x_2)$ (das
„Quadrieren" in der Ebene) sind die vier partiellen Ableitungen schnell gebildet:

$$Df = \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1} & \dfrac{\partial f_1}{\partial x_2} \\[2mm] \dfrac{\partial f_2}{\partial x_1} & \dfrac{\partial f_2}{\partial x_2} \end{pmatrix} = \begin{pmatrix} 2x_1 & -2x_2 \\[1mm] 2x_2 & 2x_1 \end{pmatrix}.$$

An jedem Punkt ist $Df$ eine andere $2\times2$-Matrix — sie beschreibt, wie $f$ eine winzige Umgebung dieses
Punktes dreht und streckt.

## Totale Differenzierbarkeit: die lineare Approximation

Die bloße Existenz aller partiellen Ableitungen ist noch **nicht** die eigentliche Differenzierbarkeit. Das wahre
Kriterium knüpft an den Kern des Ableitungsbegriffs an: die **lokale lineare Näherung**.

Die Abbildung $f$ heißt __(total) differenzierbar__ an der Stelle $x_0$, wenn es eine Matrix
$A\in\mathbb{R}^{m\times n}$ gibt, die $f$ nahe $x_0$ so gut linear annähert, dass der Fehler **schneller als
linear** verschwindet:

:::formel Definition
$$\lim_{x \to x_0} \frac{\lvert f(x) - f(x_0) - A\,(x - x_0)\rvert}{\lvert x - x_0\rvert} = 0.$$
:::

**Stück für Stück gelesen:** Im Zähler steht der **Fehler** der linearen Näherung $f(x)\approx
f(x_0)+A\,(x-x_0)$. Der Nenner $\lvert x-x_0\rvert$ misst diesen Fehler **relativ** zum Abstand vom Punkt. Nur wenn
dieser relative Fehler gegen null geht, ist $A$ wirklich „die Ableitung" und nicht bloß irgendeine grobe Gerade.

Existiert so ein $A$, dann ist es **eindeutig** und gerade die Jacobi-Matrix, $A=Df(x_0)$. Insbesondere existieren
dann alle partiellen Ableitungen.

**Stolperstein — die Umkehrung gilt nicht.** Aus der Existenz aller partiellen Ableitungen folgt im Allgemeinen
**nicht** die totale Differenzierbarkeit.

Der Grund: Partielle Ableitungen „sehen" nur, was entlang der Koordinatenachsen passiert. Ein Feld kann dort glatt
aussehen und in schrägen Richtungen trotzdem springen.

Eine **hinreichende** Bedingung rettet den Fall: Sind alle partiellen Ableitungen nicht nur vorhanden, sondern
auch **stetig**, so ist $f$ total differenzierbar. Man nennt $f$ dann __stetig differenzierbar__.

Allgemeiner heißt $f$ __$k$-mal stetig differenzierbar__ ($f\in C^k(U;\mathbb{R}^m)$), wenn alle partiellen
Ableitungen bis zur Ordnung $k$ stetig sind. Für $k\ge2$ sorgt der __Satz von Schwarz__ dafür, dass gemischte
Ableitungen vertauschen: $\frac{\partial^2 f}{\partial x_j\partial x_k}=\frac{\partial^2 f}{\partial x_k\partial x_j}$.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-tangentialebene · Vorlage: flaeche-tangentialebene-3d
Eine gekrümmte Fläche $f$ über der Umgebung von $x_0$ und die Tangentialebene $f(x_0)+Df(x_0)(x-x_0)$. Ein Pfeil
markiert den Abstand „Fläche − Tangentialebene"; Notiz: dieser Abstand geht schneller als $\lvert x-x_0\rvert$
gegen null. Kleines Gegenbeispiel-Icon: „partielle Ableitungen existieren, aber nicht differenzierbar". (Rot =
Fläche $f$, orange = Tangentialebene $Df$.)
:::

## Die Kettenregel als Matrixprodukt

Der Vorteil der Matrix-Schreibweise zeigt sich bei verketteten Abbildungen. Sind $g=(g_1,\ldots,g_m)$ (in $x$)
und $f=f(y_1,\ldots,y_m)$ differenzierbar, so ist die Verkettung $(f\circ g)(x)=f(g(x))$ differenzierbar. Ihre
Ableitung ist — wie in HM1 „äußere mal innere Ableitung", nur jetzt als **Matrizenprodukt**:

:::formel Satz
$$D(f\circ g)(x) = Df\big(g(x)\big)\,Dg(x).$$
:::

Links steht die $N\times n$-Matrix der Verkettung, rechts das Produkt der $N\times m$-Matrix $Df$ (ausgewertet am
Zwischenpunkt $g(x)$) mit der $m\times n$-Matrix $Dg$. Die Dimensionen passen genau zusammen — „inneres Maß" $m$.

:::herleitung
Nach der Definition der Matrixmultiplikation ist der Eintrag in Zeile $i$, Spalte $k$ das Produkt „Zeile $i$ von
$Df$ mal Spalte $k$ von $Dg$". Ausgeschrieben ist das die Summe über alle Zwischenvariablen $y_j$:

$$\frac{\partial (f\circ g)_i}{\partial x_k}(x) = \sum_{j=1}^{m} \frac{\partial f_i}{\partial y_j}\big(g(x)\big)\,\frac{\partial g_j}{\partial x_k}(x).$$

Jeder Summand ist ein Beitrag über einen Umweg: „wie stark $f_i$ auf $y_j$ reagiert" mal „wie stark $y_j$ auf
$x_k$ reagiert". Aufsummiert über alle Zwischenvariablen ergibt das die gesamte Änderung — genau die eindimensionale
Kettenregel, nur mit mehreren Wegen.
:::

**Wichtiger Spezialfall (Feld entlang einer Kurve).** Läuft man mit einer differenzierbaren Kurve
$\gamma:[a,b]\to U$ durch ein Skalarfeld $h$, so ist die Änderung des Feldwerts längs der Kurve nach der
Kettenregel das **Skalarprodukt** aus Gradient und Geschwindigkeit:

$$\frac{d}{dt}\,h(\gamma(t)) = \nabla h(\gamma(t)) \cdot \dot\gamma(t).$$

Anschaulich: Wie schnell sich der Feldwert ändert, hängt davon ab, wie gut der Gradient (Richtung des steilsten
Anstiegs) und die Bewegungsrichtung $\dot\gamma$ zusammenpassen. Läuft man senkrecht zum Gradienten, ändert sich
nichts — das sind später die Niveaulinien.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-gradient-kurve · Vorlage: skalarfeld-kurve-2d
Eine Kurve $\gamma(t)$ läuft durch eine farbige Skalarfeld-Landschaft $h$; an einem Punkt sind der
Geschwindigkeitsvektor $\dot\gamma$ und der Gradient $\nabla h$ eingezeichnet, dazu der Winkel zwischen ihnen.
Beschriftung $\frac{d}{dt}h(\gamma(t))=\nabla h\cdot\dot\gamma$: maximal in Gradientenrichtung, null senkrecht
dazu. (Rot = Kurve, orange = Gradient, grau = Höhenlinien.)
:::

## Bedeutung und Ausblick

Die Jacobi-Matrix ist das mehrdimensionale Gegenstück zur Ableitung: Sie linearisiert ein Feld lokal, und auf
dieser Linearisierung bauen alle Werkzeuge der Vektoranalysis auf. In der Elektrotechnik steckt sie hinter jedem
Feld — ob E-Feld, Strömung oder Wärme.

Der Spezialfall des Skalarfelds hat uns schon den __Gradienten__ geliefert. Er ist der wichtigste erste
Differentialoperator: Er zeigt in die Richtung des steilsten Anstiegs und erzeugt aus einem Potential ein
Vektorfeld. Seine Geometrie und die besondere Klasse der __Gradientenfelder__ sind das Thema des nächsten Artikels.

:::kern
- __Felder__ sind Abbildungen $f:U\subset\mathbb{R}^n\to\mathbb{R}^m$ auf offenen Mengen: __Skalarfelder__ ($m=1$, Zahl pro Punkt) und __Vektorfelder__ ($m\ge2$, Vektor pro Punkt).
- Die Ableitung ist die __Jacobi-Matrix__ $Df=\left(\tfrac{\partial f_j}{\partial x_k}\right)_{jk}\in\mathbb{R}^{m\times n}$; die Zeilen sind die Gradienten der Komponenten.
- Für ein Skalarfeld ist $Df$ ein Zeilenvektor und $\nabla f=(Df)^T$ der __Gradient__ (Spaltenvektor).
- __Total differenzierbar__ an $x_0$ = lineare Näherung $f(x_0)+Df(x_0)(x-x_0)$ mit überlinear kleinem Fehler. **Vorsicht:** partielle Ableitungen allein genügen nicht; **stetige** partielle Ableitungen ($f\in C^1$) reichen.
- Für $C^k$, $k\ge2$, vertauschen gemischte Ableitungen (__Satz von Schwarz__).
- __Kettenregel__ als Matrixprodukt $D(f\circ g)=Df(g(x))\,Dg(x)$; entlang einer Kurve folgt $\tfrac{d}{dt}h(\gamma(t))=\nabla h\cdot\dot\gamma$.
:::

:::quiz
F: Warum genügt bei einer Abbildung $f:\mathbb{R}^n\to\mathbb{R}^m$ eine einzelne Zahl als Ableitung nicht mehr — und wie kommt man gerade auf eine Matrix?
A: Die Ableitung ist die beste **lineare** Näherung. Eine lineare Abbildung von $\mathbb{R}^n$ nach $\mathbb{R}^m$ ist genau eine $m\times n$-Matrix: Es gibt $n$ Eingangsrichtungen und $m$ Komponenten, deren lokale Änderung man erfassen muss — das sind $m\cdot n$ Zahlen, angeordnet in der Jacobi-Matrix. Eine Zahl kann nur eine Richtung/Komponente beschreiben.
F: Was bedeutet die Jacobi-Matrix $Df(x_0)$ geometrisch?
A: Sie ist die lineare Abbildung, die $f$ in einer kleinen Umgebung von $x_0$ am besten annähert — sie beschreibt, wie $f$ ein winziges Gitterquadrat dreht, streckt und schert. „Ableitung" heißt hier: lokale Linearisierung.
F: Wieso stehen die Gradienten der Komponentenfunktionen gerade in den **Zeilen** der Jacobi-Matrix?
A: Zeile $j$ sammelt alle Ableitungen $\partial f_j/\partial x_k$ **einer** Komponente $f_j$ nach allen Koordinaten $x_k$ — und das ist genau der (transponierte) Gradient von $f_j$. Eine Spalte bündelt hingegen die Ableitungen **aller** Komponenten nach **einer** Koordinate.
F: Gradient und Jacobi-Matrix eines Skalarfelds enthalten dieselben Zahlen — worin unterscheiden sie sich trotzdem?
A: In Rolle und Form: $Df$ ist ein Zeilenvektor ($1\times n$) und wird als **lineare Abbildung** verwendet; der Gradient $\nabla f=(Df)^T$ ist der zugehörige **Spaltenvektor** und wird als Richtung (steilster Anstieg) gedeutet. Das Unterscheiden verhindert Fehler beim Multiplizieren (Zeile·Spalte).
F: Warum ist die bloße Existenz **aller** partiellen Ableitungen noch nicht die (totale) Differenzierbarkeit?
A: Partielle Ableitungen „sehen" nur das Verhalten entlang der Koordinatenachsen. Ein Feld kann dort völlig glatt aussehen und in schrägen Richtungen trotzdem springen. Total differenzierbar heißt, dass **eine** lineare Näherung in **alle** Richtungen gleichzeitig gilt — mit überlinear kleinem Fehler.
F: Was drückt der Grenzwert $\lim_{x\to x_0}\frac{|f(x)-f(x_0)-A(x-x_0)|}{|x-x_0|}=0$ aus, und warum steht $|x-x_0|$ im Nenner?
A: Er fordert, dass der Fehler der linearen Näherung **schneller als linear** verschwindet. Der Nenner misst den Fehler **relativ** zum Abstand: Nur wenn dieser relative Fehler gegen null geht, ist $A$ wirklich die Ableitung und nicht bloß eine grobe lineare Näherung.
F: Welche Zusatzeigenschaft macht aus partiellen Ableitungen sicher totale Differenzierbarkeit — und warum ist sie nur hinreichend, nicht notwendig?
A: **Stetigkeit** aller partiellen Ableitungen ($f\in C^1$) genügt. Notwendig ist sie nicht: Es gibt differenzierbare Abbildungen, deren partielle Ableitungen nicht stetig sind. „Hinreichend" heißt: $C^1\Rightarrow$ differenzierbar, aber nicht umgekehrt.
F: Warum vertauschen bei einem $C^2$-Feld die gemischten zweiten Ableitungen, und wie heißt diese Aussage?
A: Das ist der **Satz von Schwarz**: Sind die zweiten partiellen Ableitungen stetig, gilt $\frac{\partial^2 f}{\partial x_j\partial x_k}=\frac{\partial^2 f}{\partial x_k\partial x_j}$. Die Reihenfolge des Ableitens spielt keine Rolle — die zweite Ableitung ist symmetrisch.
F: Inwiefern ist die Kettenregel $D(f\circ g)=Df(g(x))\,Dg(x)$ dieselbe Idee wie „äußere mal innere Ableitung" aus HM1?
A: Exakt dieselbe Idee: In 1D ist $(f(g(x)))'=f'(g(x))\cdot g'(x)$. Hier sind die Ableitungen **Matrizen** und „mal" ist die **Matrizenmultiplikation**. Die komponentenweise Summe über die Zwischenvariablen $y_j$ ist nichts anderes als das Zeile-mal-Spalte-Produkt.
F: Warum ist die Änderung eines Skalarfelds längs einer Kurve gerade $\frac{d}{dt}h(\gamma(t))=\nabla h\cdot\dot\gamma$, und wann ist sie null?
A: Es ist die Kettenregel für $h\circ\gamma$: die Zeile $Dh=\nabla h^{T}$ mal die Spalte $\dot\gamma$ ergibt das Skalarprodukt $\nabla h\cdot\dot\gamma$. Null wird sie, wenn man **senkrecht** zum Gradienten läuft ($\dot\gamma\perp\nabla h$) — entlang einer Niveaulinie; maximal, wenn man in Gradientenrichtung läuft.
:::
