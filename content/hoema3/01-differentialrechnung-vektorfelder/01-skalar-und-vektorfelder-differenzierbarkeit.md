---
title: Skalarfelder, Vektorfelder und die Jacobi-Matrix
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010100
summary: Von Grund auf – wie die Differentialrechnung von einer Variablen auf Abbildungen $f:\mathbb{R}^n\to\mathbb{R}^m$ erweitert wird. Aus der einen Ableitung $f'(x)$ wird eine Matrix, die Jacobi-Matrix $Df$, die das Feld nahe einem Punkt linear annähert. Mit totaler Differenzierbarkeit samt Gegenbeispiel, dem Kriterium „stetige partielle Ableitungen", dem Satz von Schwarz und der Kettenregel $D(f\circ g)=Df\,Dg$.
tags: Skalarfeld, Vektorfeld, partielle Ableitung, Jacobi-Matrix, totale Differenzierbarkeit, lineare Approximation, Kettenregel, stetig differenzierbar, Satz von Schwarz
---

## Anschaulich

Stell dir zwei Landkarten vor. Auf der ersten steht an jedem Ort eine **Zahl** — die Temperatur. Das ist ein
__Skalarfeld__. Auf der zweiten steht an jedem Ort ein **Pfeil** — Windrichtung und Windstärke. Das ist ein
__Vektorfeld__.

Die Höhere Mathematik III beginnt mit der Frage: Was ist die **Ableitung** eines solchen Feldes?

In HM1 war die Ableitung einer Funktion $f:\mathbb{R}\to\mathbb{R}$ eine einzige Zahl $f'(x)$, die Steigung der
Tangente. Dahinter steckt eine tiefere Idee: Zoomt man weit genug in den Graphen hinein, sieht er aus wie eine
**Gerade**. Die Ableitung beschreibt diese beste **lineare Näherung** der Funktion an der Stelle $x$.

Genau diese Idee trägt in höhere Dimensionen. Zoomt man nah genug an einen Punkt heran, verhält sich jede glatte
Abbildung wie eine **lineare Abbildung**: Sie dreht, streckt und schert ein winziges Gitter. Eine lineare
Abbildung ist aber nichts anderes als eine **Matrix** — und diese Matrix ist die __Jacobi-Matrix__, die Ableitung
des Feldes.

Auf diesem einen Baustein ruht die ganze Vektoranalysis: Gradient, Divergenz, Rotation und die Integralsätze.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-feld-und-jacobi · Vorlage: feld-linearisierung-2d
Links ein Skalarfeld als Farb-/Höhenkarte (Temperatur, Zahl pro Punkt), rechts ein Vektorfeld als Pfeilgitter
(Strömung, Pfeil pro Punkt). In der Mitte eine Abbildung $f:\mathbb{R}^2\to\mathbb{R}^2$: Ein kleines Gitterquadrat
um $x_0$ wird von $f$ auf ein leicht gekrümmtes Viereck abgebildet; ein daneben durch $Df(x_0)$ **linear**
verzerrtes Gitter deckt sich beim Hineinzoomen immer besser damit. Kernaussage: Die Ableitung einer vektorwertigen
Abbildung ist eine Matrix, die das Feld lokal linear macht. (Rot = Abbildung $f$, orange = lineare Näherung $Df$,
grau = Ausgangsgitter.)
:::

## Skalarfelder und Vektorfelder

Ein __Feld__ ordnet jedem Punkt eines Bereichs eine Größe zu. Formal ist es eine **Abbildung**

$$f:U\to\mathbb{R}^m, \qquad x=(x_1,\ldots,x_n)\;\mapsto\; f(x)=\big(f_1(x),\ldots,f_m(x)\big),$$

definiert auf einer offenen Menge $U\subseteq\mathbb{R}^n$.

**So liest man diese Zeile:** Die **Eingabe** ist ein Punkt $x$ mit $n$ Koordinaten — für einen Ort im Raum ist
$n=3$. Die **Ausgabe** ist ein Vektor mit $m$ Komponenten. Jede Komponente $f_j:U\to\mathbb{R}$ ist eine
gewöhnliche reellwertige Funktion mehrerer Veränderlicher.

Je nach Zahl der Ausgabe-Komponenten unterscheidet man zwei Typen:

- __Skalarfeld__ ($m=1$): jedem Ort eine **Zahl**. Beispiele: die Temperatur $T(x,y,z)$ oder das elektrische
  Potential $\varphi(x,y,z)$.
- __Vektorfeld__ ($m\ge2$, meist $m=n$): jedem Ort einen **Vektor**. Beispiele: die Strömungsgeschwindigkeit
  einer Flüssigkeit oder das elektrische Feld $\vec E(x,y,z)\in\mathbb{R}^3$.

„__Offen__" heißt: Um jeden Punkt von $U$ liegt noch eine kleine Kugel ganz in $U$. Von jedem Punkt aus hat man also
in jede Richtung ein Stückchen „Platz" — genau das braucht man, um Differenzenquotienten bilden zu können.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-skalarfeld-vs-vektorfeld · Vorlage: feld-vergleich-2d
Zwei Felder über demselben Ausschnitt der Ebene: links ein Skalarfeld als Farbkarte (Temperatur), rechts ein
Vektorfeld als Pfeilgitter (Strömung). Beschriftung: „Skalarfeld $f:U\to\mathbb{R}$ — Zahl pro Punkt" vs.
„Vektorfeld $f:U\to\mathbb{R}^m$ — Vektor pro Punkt". (Rot = Feldwerte, grau = Gitter.)
:::

## Partielle Ableitungen: eine Richtung nach der anderen

Bei $f:\mathbb{R}\to\mathbb{R}$ gibt es nur eine Richtung. Bei $f:\mathbb{R}^n\to\mathbb{R}^m$ gibt es $n$
Koordinatenrichtungen, in die man gehen kann, und $m$ Komponenten, die sich dabei ändern.

Der erste Baustein ist die __partielle Ableitung__: Man bewegt sich nur entlang **einer** Koordinatenachse und hält
alle anderen Koordinaten fest.

$$\frac{\partial f_j}{\partial x_k}(x) = \lim_{h\to0}\frac{f_j(x+h\,e_k)-f_j(x)}{h}.$$

Dabei ist $e_k$ der $k$-te __Einheitsvektor__: An Position $k$ steht eine $1$, sonst nur Nullen. Der Punkt
$x+h\,e_k$ entsteht aus $x$, indem man **nur** die $k$-te Koordinate um die Zahl $h$ verschiebt.

Das ist nichts Neues: Es ist die gewöhnliche HM1-Ableitung der Funktion $t\mapsto f_j(x_1,\ldots,t,\ldots,x_n)$, in
der nur die $k$-te Variable „lebendig" ist.

Für die vollständige lokale Änderung braucht man **alle** diese Ableitungen: jede der $m$ Komponenten nach jeder der
$n$ Koordinaten. Das sind $m\cdot n$ Zahlen — und die ordnet man natürlicherweise in einer **Matrix** an.

## Die Jacobi-Matrix

Für eine partiell differenzierbare Abbildung $f$ mit Komponenten $f_1,\ldots,f_m$ heißt die Matrix aller ersten
partiellen Ableitungen die __Jacobi-Matrix__:

:::formel Definition
$$Df = \left(\frac{\partial f_j}{\partial x_k}\right)_{jk} = \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\[2mm] \vdots & \ddots & \vdots \\[1mm] \dfrac{\partial f_m}{\partial x_1} & \cdots & \dfrac{\partial f_m}{\partial x_n} \end{pmatrix} \in \mathbb{R}^{m \times n}.$$
:::

**So liest man sie:** Der Eintrag in **Zeile $j$, Spalte $k$** ist $\partial f_j/\partial x_k$. Zeile $j$ sammelt die
Ableitungen **einer** Komponente $f_j$ nach allen Koordinaten; Spalte $k$ die Ableitungen **aller** Komponenten nach
der einen Koordinate $x_k$.

Die Form passt genau zur Abbildung: $m$ Zeilen (so viele wie Ausgabe-Komponenten), $n$ Spalten (so viele wie
Eingabe-Koordinaten).

**Wozu das Ganze?** Die Jacobi-Matrix soll leisten, was $f'(x_0)$ in HM1 geleistet hat. Für einen kleinen Schritt
$h\in\mathbb{R}^n$ soll gelten:

$$f(x_0+h) \;\approx\; f(x_0) + Df(x_0)\,h.$$

Links steht der neue Funktionswert, ein Vektor in $\mathbb{R}^m$. Rechts steht der alte Wert plus „Matrix mal
Schritt": Eine $m\times n$-Matrix mal einem Vektor aus $\mathbb{R}^n$ ergibt wieder einen Vektor aus $\mathbb{R}^m$.
Wann dieses „$\approx$" wirklich gilt und wie gut es sein muss, klärt der Abschnitt über totale Differenzierbarkeit.

**Der Spezialfall Skalarfeld** ($m=1$) ist besonders wichtig. Dann hat $Df$ nur **eine Zeile**, ist also ein
Zeilenvektor in $\mathbb{R}^{1\times n}$. Seinen transponierten Spaltenvektor nennt man den __Gradienten__:

$$\nabla f := \operatorname{grad} f = \left(\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_n}\right)^{\!T} \in \mathbb{R}^n, \qquad \nabla f = (Df)^{T}.$$

Das Symbol $\nabla$ („Nabla") ist dabei formal selbst ein Spaltenvektor aus Ableitungsoperatoren:

$$\nabla = \left(\frac{\partial}{\partial x_1},\ldots,\frac{\partial}{\partial x_n}\right)^{T}.$$

Weil der Gradient nur erste Ableitungen enthält, nennt man ihn einen __Differentialoperator erster Ordnung__: Er
macht aus einer differenzierbaren Funktion ein Vektorfeld.

**Gradient und Jacobi-Matrix sind zu unterscheiden.** Sie enthalten dieselben Zahlen, spielen aber verschiedene
Rollen. $Df$ ist eine **Zeile** und wird als lineare Abbildung benutzt: Sie wird von links an einen Schritt $h$ (eine
Spalte) multipliziert. Der Gradient $\nabla f$ ist eine **Spalte** und wird als Richtungspfeil gedeutet — als
Richtung des steilsten Anstiegs (nächster Artikel).

Allgemeiner sind die Zeilen der Jacobi-Matrix gerade die transponierten Gradienten der Komponenten $f_j$.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-jacobi-aufbau · Vorlage: matrix-schema
Aufbau der Jacobi-Matrix als Schema: ein $m\times n$-Kasten; Zeile $j$ hervorgehoben als „Gradient von $f_j$",
Spalte $k$ als „Ableitungen aller Komponenten nach $x_k$". Daneben der Skalar-Spezialfall: eine einzelne Zeile
$Df\in\mathbb{R}^{1\times n}$ und ihr transponierter Gradient $\nabla f\in\mathbb{R}^n$. (Orange = die gerade
betrachtete Zeile/Spalte, grau = übrige Einträge.)
:::

## Zahlenbeispiel: das „Quadrieren" in der Ebene

Betrachte die Abbildung

$$f:\mathbb{R}^2\to\mathbb{R}^2, \qquad f(x_1,x_2) = \big(x_1^2-x_2^2,\;2x_1x_2\big).$$

Die vier partiellen Ableitungen sind schnell gebildet:

$$Df(x) = \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1} & \dfrac{\partial f_1}{\partial x_2} \\[2mm] \dfrac{\partial f_2}{\partial x_1} & \dfrac{\partial f_2}{\partial x_2} \end{pmatrix} = \begin{pmatrix} 2x_1 & -2x_2 \\[1mm] 2x_2 & 2x_1 \end{pmatrix}.$$

An jedem Punkt ist $Df$ eine andere Matrix. Was sie mit einem winzigen Quadrat anstellt, sieht man an zwei konkreten
Punkten:

$$Df(1,0) = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}, \qquad Df(0,1) = \begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix} = 2\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$

Bei $(1,0)$ ist das eine reine **Streckung** um den Faktor $2$: Ein winziges Quadrat wird doppelt so groß, aber nicht
gedreht.

Bei $(0,1)$ steht rechts das Doppelte der Drehmatrix um $90^\circ$: Das Quadrat wird um $90^\circ$ **gedreht** und
zugleich um den Faktor $2$ **gestreckt**.

Allgemein dreht $Df(x)$ um den Polarwinkel des Punktes $x$ und streckt um den Faktor $2|x|$. Wer komplexe Zahlen
kennt, erkennt das Quadrieren $z\mapsto z^2$ wieder: Seine Ableitung $2z$ wirkt als Multiplikation genau so — drehen
und strecken.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-quadrieren-gitter · Vorlage: abbildung-gitter-2d
Links die Ebene mit zwei kleinen Gitterquadraten bei $(1,0)$ und $(0,1)$; rechts ihre Bilder unter
$f(x_1,x_2)=(x_1^2-x_2^2,\,2x_1x_2)$. Das Quadrat bei $(1,0)$ wird nur gestreckt (Faktor 2), das bei $(0,1)$
zusätzlich um $90^\circ$ gedreht. Daneben jeweils die Matrix $Df$ am Punkt. (Grau = Ausgangsgitter, rot = Bild unter
$f$, orange = lineare Näherung $Df$.)
:::

## Totale Differenzierbarkeit: die lineare Näherung präzise

Die bloße Existenz aller partiellen Ableitungen ist noch **nicht** die eigentliche Differenzierbarkeit. Das wahre
Kriterium knüpft an den Kern des Ableitungsbegriffs an: die **lokale lineare Näherung** — und zwar in **alle**
Richtungen zugleich, nicht nur entlang der Achsen.

Die Abbildung $f$ heißt __(total) differenzierbar__ an der Stelle $x_0\in U$, wenn es eine Matrix
$A\in\mathbb{R}^{m\times n}$ gibt, sodass der Fehler der linearen Näherung **schneller als linear** verschwindet:

:::formel Definition
$$\lim_{x \to x_0} \frac{\lvert f(x) - f(x_0) - A\,(x - x_0)\rvert}{\lvert x - x_0\rvert} = 0.$$
:::

**Stück für Stück gelesen:** Im Zähler steht der Fehler der linearen Näherung — der Unterschied zwischen dem echten
Wert $f(x)$ und der Ersatzrechnung $f(x_0)+A(x-x_0)$. Der Nenner $\lvert x-x_0\rvert$ misst diesen Fehler **relativ**
zum Abstand vom Punkt.

Dass der relative Fehler gegen null geht, macht $A$ zur besten linearen Näherung. Eine bloß „ungefähr passende"
Matrix würde einen relativen Fehler übrig lassen.

**Die Matrix ist automatisch die Jacobi-Matrix.** Gibt es so ein $A$, dann ist es eindeutig, nämlich

$$A = Df(x_0).$$

Insbesondere existieren dann alle partiellen Ableitungen von $f$ in $x_0$.

:::herleitung
Man nähert sich $x_0$ nur entlang der $k$-ten Koordinatenachse, setzt also

$$x = x_0 + h\,e_k \qquad (h\in\mathbb{R},\ h\to0), \qquad \text{sodass} \quad \lvert x-x_0\rvert = \lvert h\rvert.$$

Eingesetzt in die Definition ergibt das

$$\frac{f(x_0+h\,e_k)-f(x_0)}{h} - A\,e_k \;\longrightarrow\; 0 \qquad (h\to0).$$

Der erste Term ist — komponentenweise — genau der Differenzenquotient der partiellen Ableitung nach $x_k$. Er
konvergiert also, und zwar gegen $A\,e_k$, die $k$-te Spalte von $A$.

Damit existiert die partielle Ableitung nach $x_k$ und ist die $k$-te Spalte von $A$. Spalte für Spalte stimmt $A$
also mit der Jacobi-Matrix überein — insbesondere kann es nur ein einziges solches $A$ geben.
:::

**Differenzierbar heißt auch stetig.** Aus der Definition folgt, dass $f$ in $x_0$ stetig ist. Man zerlegt die
Änderung in den linearen Anteil und den Fehler:

$$f(x)-f(x_0) = \underbrace{A\,(x-x_0)}_{\to\,0} + \underbrace{\big(f(x)-f(x_0)-A\,(x-x_0)\big)}_{\to\,0\ \text{(sogar schneller als } |x-x_0|)}.$$

Beide Teile verschwinden für $x\to x_0$, also auch die Differenz $f(x)-f(x_0)$.

## Wann partielle Ableitungen genügen

**Stolperstein — partielle Ableitungen allein reichen nicht.** Sie „sehen" nur, was entlang der Koordinatenachsen
passiert. Das klassische Gegenbeispiel ist

$$f(x,y) = \begin{cases} \dfrac{xy}{x^2+y^2}, & (x,y)\neq(0,0),\\[2mm] 0, & (x,y)=(0,0). \end{cases}$$

Entlang beider Achsen ist $f$ konstant null:

$$f(x,0) = 0, \qquad f(0,y) = 0 \qquad \text{für alle } x,y.$$

Deshalb existieren beide partiellen Ableitungen im Ursprung, und beide sind null. Die Jacobi-Matrix im Ursprung ist
also die Nullmatrix.

Entlang der Diagonale $y=x$ ist $f$ dagegen konstant $\tfrac12$:

$$f(t,t) = \frac{t\cdot t}{t^2+t^2} = \frac12 \qquad (t\neq0).$$

Nähert man sich dem Ursprung auf der Diagonale, strebt $f$ also gegen $\tfrac12$ — der Funktionswert im Ursprung ist
aber $0$. Die Funktion ist dort nicht einmal **stetig** und damit erst recht nicht differenzierbar.

Die lineare Näherung aus dem Jacobi-Abschnitt — hier mit der Nullmatrix — versagt in schrägen Richtungen völlig.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-gegenbeispiel-xy · Vorlage: flaeche-3d
Der Graph von $f=\frac{xy}{x^2+y^2}$ über der Ebene: entlang der Achsen flach auf Höhe $0$, entlang der Diagonale
$y=x$ ein Grat auf Höhe $\tfrac12$, entlang $y=-x$ eine Rinne auf Höhe $-\tfrac12$; im Ursprung „zerreißt" die
Fläche. Die beiden Achsenschnitte (partielle Ableitungen $0$) und die Diagonale sind hervorgehoben. (Rot =
Achsenschnitte, orange = Diagonale, grau = Fläche.)
:::

**Die Rettung: stetige partielle Ableitungen.** Sind alle partiellen Ableitungen nicht nur vorhanden, sondern auch
**stetig**, so ist $f$ total differenzierbar. Man nennt $f$ dann __stetig differenzierbar__.

:::herleitung
Wir zeigen es für eine reellwertige Funktion zweier Variablen; der allgemeine Fall geht genauso (komponentenweise
und mit mehr Summanden). Für einen kleinen Schritt $h=(h_1,h_2)$ zerlegt man die Änderung in zwei Achsenschritte —
erst in $x_1$-, dann in $x_2$-Richtung:

$$f(x_0+h)-f(x_0) = \big[f(x_0+h_1e_1+h_2e_2)-f(x_0+h_1e_1)\big] + \big[f(x_0+h_1e_1)-f(x_0)\big].$$

In jeder Klammer ändert sich nur eine Variable. Der Mittelwertsatz aus HM1 liefert deshalb eine Zwischenstelle
$\xi_2$ auf der Strecke der ersten Klammer und eine Zwischenstelle $\xi_1$ auf der Strecke der zweiten:

$$f(x_0+h)-f(x_0) = \frac{\partial f}{\partial x_2}(\xi_2)\,h_2 + \frac{\partial f}{\partial x_1}(\xi_1)\,h_1.$$

Für $h\to0$ rücken $\xi_1$ und $\xi_2$ an $x_0$ heran. Weil die partiellen Ableitungen **stetig** sind, weichen sie
dort nur um kleine Fehler $\varepsilon_1,\varepsilon_2$ von ihren Werten in $x_0$ ab, und diese Fehler gehen gegen
null. Damit ist

$$f(x_0+h)-f(x_0)-\nabla f(x_0)\cdot h = \varepsilon_1h_1+\varepsilon_2h_2, \qquad \frac{\lvert\varepsilon_1h_1+\varepsilon_2h_2\rvert}{\lvert h\rvert}\le\lvert\varepsilon_1\rvert+\lvert\varepsilon_2\rvert\to0.$$

Das ist genau die Definition der totalen Differenzierbarkeit. Ohne Stetigkeit könnten die Ableitungen an den
Zwischenstellen beliebig von denen in $x_0$ abweichen — beim Gegenbeispiel oben passiert genau das: Dort ist die
partielle Ableitung nach $x$ in jeder Umgebung des Ursprungs unbeschränkt.
:::

**Höhere Ableitungen.** $f$ heißt __$k$-mal stetig differenzierbar__, wenn alle partiellen Ableitungen bis zur
Ordnung $k$ existieren und stetig sind. Die Menge dieser Abbildungen schreibt man

$$C^k(U;\mathbb{R}^m) = \big\{\, f:U\to\mathbb{R}^m \;\big|\; f \text{ ist } k\text{-mal stetig differenzierbar} \,\big\}.$$

Bei zweiten Ableitungen stellt sich eine neue Frage: Spielt es eine Rolle, ob man zuerst nach $x_j$ und dann nach
$x_k$ ableitet oder umgekehrt? Für $C^2$-Funktionen nicht — das ist der __Satz von Schwarz__:

:::formel Satz
$$\frac{\partial^2 f}{\partial x_j\,\partial x_k} = \frac{\partial^2 f}{\partial x_k\,\partial x_j} \qquad \text{für } f\in C^2.$$
:::

Allgemein dürfen für $f\in C^k$ alle partiellen Ableitungen bis zur Ordnung $k$ beliebig vertauscht werden. Die
nächsten Artikel brauchen diesen Satz ständig.

:::herleitung
Man betrachtet die Funktionswerte an den vier Ecken eines kleinen Quadrats der Seitenlänge $h$ in der
$x_j$-$x_k$-Ebene und bildet daraus die __Doppeldifferenz__

$$\Delta(h) = f(x+h\,e_j+h\,e_k) - f(x+h\,e_j) - f(x+h\,e_k) + f(x).$$

Dieser Ausdruck ist **symmetrisch** in $j$ und $k$: Vertauscht man die beiden Rollen, ändert sich nichts.

Wendet man den Mittelwertsatz zuerst in $x_j$-Richtung und danach in $x_k$-Richtung an, erhält man mit einer
Zwischenstelle $\xi$ im Quadrat

$$\Delta(h) = h^2\,\frac{\partial}{\partial x_k}\!\left(\frac{\partial f}{\partial x_j}\right)\!(\xi).$$

In umgekehrter Reihenfolge ergibt sich ebenso, mit einer Zwischenstelle $\eta$,

$$\Delta(h) = h^2\,\frac{\partial}{\partial x_j}\!\left(\frac{\partial f}{\partial x_k}\right)\!(\eta).$$

Teilt man durch $h^2$ und lässt $h\to0$ gehen, rücken $\xi$ und $\eta$ an $x$ heran. Weil die zweiten Ableitungen
**stetig** sind, stimmen beide gemischten Ableitungen im Punkt $x$ überein.
:::

## Die Kettenregel als Matrixprodukt

Der große Vorteil der Matrix-Schreibweise zeigt sich beim Verketten zweier Abbildungen:

$$g:U\to\mathbb{R}^m \ \ (U\subseteq\mathbb{R}^n), \qquad f:V\to\mathbb{R}^p \ \ (V\subseteq\mathbb{R}^m), \qquad g(U)\subseteq V.$$

Erst bildet $g$ einen Punkt $x\in\mathbb{R}^n$ auf einen Punkt in $\mathbb{R}^m$ ab, dann $f$ diesen weiter nach
$\mathbb{R}^p$. Ist $g$ in $x$ und $f$ im Bildpunkt $g(x)$ differenzierbar, so ist auch die Verkettung $f\circ g$ in
$x$ differenzierbar. Ihre Ableitung ist — wie „äußere mal innere Ableitung" in HM1, nur jetzt als
**Matrizenprodukt**:

:::formel Satz
$$D(f\circ g)(x) = Df\big(g(x)\big)\,Dg(x).$$
:::

**Dimensionen:** Links steht eine $p\times n$-Matrix. Rechts wird die $p\times m$-Matrix $Df$ — ausgewertet am
Zwischenpunkt $g(x)$, nicht bei $x$! — mit der $m\times n$-Matrix $Dg$ multipliziert. Das „innere Maß" $m$ passt
genau zusammen.

:::herleitung
Die Idee in einem Satz: **Die Linearisierung der Verkettung ist die Verkettung der Linearisierungen.**

Für einen kleinen Schritt $h\in\mathbb{R}^n$ gilt nach Definition der Differenzierbarkeit

$$g(x+h) = g(x) + Dg(x)\,h + r_g(h),$$

wobei der Rest $r_g(h)$ schneller als $\lvert h\rvert$ verschwindet. Ebenso gilt mit $y=g(x)$ für einen kleinen
Schritt $k\in\mathbb{R}^m$

$$f(y+k) = f(y) + Df(y)\,k + r_f(k).$$

Jetzt setzt man für $k$ genau den Schritt ein, den $g$ tatsächlich macht:

$$k = g(x+h)-g(x) = Dg(x)\,h + r_g(h).$$

Das ergibt

$$f\big(g(x+h)\big) = f\big(g(x)\big) + Df(y)\,Dg(x)\,h + \underbrace{Df(y)\,r_g(h) + r_f(k)}_{\text{schneller als } |h| \text{ klein}}.$$

Der Rest ist klein, weil $r_g(h)$ es ist und weil der Schritt $k$ höchstens proportional zu $\lvert h\rvert$ wächst.
Der lineare Anteil in $h$ ist also das Produkt $Df(y)\,Dg(x)$ — und nach der Eindeutigkeit der Ableitung ist das
$D(f\circ g)(x)$.

Komponentenweise ausgeschrieben ist das Matrixprodukt eine Summe über alle Zwischenvariablen $y_j$:

$$\frac{\partial (f\circ g)_i}{\partial x_k}(x) = \sum_{j=1}^{m} \frac{\partial f_i}{\partial y_j}\big(g(x)\big)\,\frac{\partial g_j}{\partial x_k}(x).$$

Jeder Summand ist ein „Umweg": wie stark $f_i$ auf $y_j$ reagiert, mal wie stark $y_j$ auf $x_k$ reagiert.
:::

**Wichtiger Spezialfall: ein Feld entlang einer Kurve.** Sei $\gamma:[a,b]\to U$ eine differenzierbare Kurve und
$\varphi:U\to\mathbb{R}$ ein differenzierbares Skalarfeld auf $U\subseteq\mathbb{R}^n$. Dann ist
$t\mapsto\varphi(\gamma(t))$ eine Funktion **einer** Variablen, und die Kettenregel liefert:

$$\frac{d}{dt}\,\varphi(\gamma(t)) = D\varphi(\gamma(t))\,\dot\gamma(t) = \nabla\varphi(\gamma(t))\cdot\dot\gamma(t).$$

Hier ist $D\varphi$ eine $1\times n$-Zeile und $\dot\gamma$ eine $n\times1$-Spalte. Ihr Produkt ist eine Zahl — das
**Skalarprodukt** aus Gradient und Geschwindigkeit.

**Zahlenbeispiel.** Wir nehmen ein Skalarfeld und eine Kurve:

$$\varphi(x,y) = xy, \qquad \gamma(t) = (t,\,t^2).$$

Direkt eingesetzt ergibt sich

$$\varphi(\gamma(t)) = t\cdot t^2 = t^3, \qquad \frac{d}{dt}\,\varphi(\gamma(t)) = 3t^2.$$

Über die Kettenregel braucht man den Gradienten am Kurvenpunkt und die Geschwindigkeit:

$$\nabla\varphi(x,y) = (y,\,x) \;\Rightarrow\; \nabla\varphi(\gamma(t)) = (t^2,\,t), \qquad \dot\gamma(t) = (1,\,2t).$$

Ihr Skalarprodukt bestätigt das Ergebnis:

$$\nabla\varphi(\gamma(t))\cdot\dot\gamma(t) = t^2\cdot1 + t\cdot2t = 3t^2. \quad\checkmark$$

Anschaulich: Wie schnell sich der Feldwert ändert, hängt davon ab, wie gut der Gradient (Richtung des steilsten
Anstiegs) und die Bewegungsrichtung zusammenpassen. Läuft man senkrecht zum Gradienten, ändert sich nichts — das
sind später die Niveaulinien.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-gradient-kurve · Vorlage: skalarfeld-kurve-2d
Eine Kurve $\gamma(t)$ läuft durch eine farbige Skalarfeld-Landschaft $\varphi$; an einem Punkt sind der
Geschwindigkeitsvektor $\dot\gamma$ und der Gradient $\nabla\varphi$ eingezeichnet, dazu der Winkel zwischen ihnen.
Beschriftung $\frac{d}{dt}\varphi(\gamma(t))=\nabla\varphi\cdot\dot\gamma$: maximal in Gradientenrichtung, null
senkrecht dazu. (Rot = Kurve, orange = Gradient, grau = Höhenlinien.)
:::

## Bedeutung und Ausblick

Die Jacobi-Matrix ist das mehrdimensionale Gegenstück zur Ableitung: Sie linearisiert ein Feld lokal, und auf dieser
Linearisierung bauen alle Werkzeuge der Vektoranalysis auf. In der Elektrotechnik steckt sie hinter jedem Feld — ob
E-Feld, Strömung oder Wärme.

In Kapitel 4 kehrt sie als __Jacobi-Determinante__ zurück. Dort misst sie, wie stark eine Koordinatentransformation
(etwa auf Polar- oder Kugelkoordinaten) Flächen und Volumina verzerrt.

Der Spezialfall des Skalarfelds hat uns schon den __Gradienten__ geliefert. Er zeigt in die Richtung des steilsten
Anstiegs und erzeugt aus einem Potential ein Vektorfeld. Seine Geometrie und die Klasse der __Gradientenfelder__ sind
das Thema des nächsten Artikels.

:::kern
- __Felder__ sind Abbildungen $f:U\to\mathbb{R}^m$ auf offenen Mengen $U\subseteq\mathbb{R}^n$: __Skalarfeld__ ($m=1$, Zahl pro Punkt), __Vektorfeld__ ($m\ge2$, Vektor pro Punkt).
- Die __partielle Ableitung__ $\partial f_j/\partial x_k$ leitet nur entlang der $x_k$-Achse ab; alle anderen Koordinaten bleiben fest.
- Die __Jacobi-Matrix__ $Df=(\partial f_j/\partial x_k)_{jk}\in\mathbb{R}^{m\times n}$ sammelt alle ersten partiellen Ableitungen; ihre Zeilen sind die Gradienten der Komponenten.
- Für ein Skalarfeld ist $Df$ eine Zeile und der __Gradient__ $\nabla f=(Df)^T$ die zugehörige Spalte.
- __Total differenzierbar__ heißt: Der Fehler der linearen Näherung $f(x_0)+A(x-x_0)$ verschwindet schneller als $|x-x_0|$.
- Die Matrix ist dann eindeutig die Jacobi-Matrix, und $f$ ist in $x_0$ stetig.
- Partielle Ableitungen allein genügen **nicht** (Gegenbeispiel $\tfrac{xy}{x^2+y^2}$ im Ursprung); **stetige** partielle Ableitungen ($f\in C^1$) genügen.
- __Satz von Schwarz__: Für $f\in C^2$ ist die Reihenfolge gemischter zweiter Ableitungen egal.
- __Kettenregel__: $D(f\circ g)(x)=Df(g(x))\,Dg(x)$ — Verkettung der Linearisierungen ist Matrixprodukt.
- Entlang einer Kurve: $\tfrac{d}{dt}\varphi(\gamma(t))=\nabla\varphi\cdot\dot\gamma$.
:::

:::quiz
F: Warum genügt bei einer Abbildung $f:\mathbb{R}^n\to\mathbb{R}^m$ eine einzelne Zahl als Ableitung nicht mehr — und wie kommt man gerade auf eine Matrix?
A: Die Ableitung ist die beste **lineare** Näherung, und eine lineare Abbildung von $\mathbb{R}^n$ nach $\mathbb{R}^m$ ist genau eine $m\times n$-Matrix. Es gibt $n$ Eingangsrichtungen und $m$ Komponenten, also $m\cdot n$ partielle Ableitungen, die man in der Jacobi-Matrix anordnet. Eine einzelne Zahl könnte nur eine Richtung und eine Komponente beschreiben.
F: Was bedeutet die Jacobi-Matrix $Df(x_0)$ geometrisch — etwa beim „Quadrieren" $f(x_1,x_2)=(x_1^2-x_2^2,\,2x_1x_2)$?
A: Sie ist die lineare Abbildung, die $f$ nahe $x_0$ am besten annähert; sie zeigt, wie $f$ ein winziges Gitterquadrat dreht, streckt und schert. Beim Quadrieren ist $Df(1,0)$ eine reine Streckung um den Faktor $2$, während $Df(0,1)$ zusätzlich um $90^\circ$ dreht.
F: Wieso stehen die Gradienten der Komponentenfunktionen gerade in den **Zeilen** der Jacobi-Matrix?
A: Zeile $j$ sammelt alle Ableitungen $\partial f_j/\partial x_k$ **einer** Komponente $f_j$ nach allen Koordinaten — das ist genau der (transponierte) Gradient von $f_j$. Eine Spalte bündelt dagegen die Ableitungen **aller** Komponenten nach **einer** Koordinate.
F: Gradient und Jacobi-Matrix eines Skalarfelds enthalten dieselben Zahlen — worin unterscheiden sie sich trotzdem?
A: In Form und Rolle: $Df$ ist eine Zeile ($1\times n$) und wird als **lineare Abbildung** benutzt, die von links an einen Schritt $h$ (eine Spalte) multipliziert wird. Der Gradient $\nabla f=(Df)^T$ ist die zugehörige **Spalte** und wird als Richtungspfeil gedeutet.
F: Warum ist $f(x,y)=\frac{xy}{x^2+y^2}$ (mit $f(0,0)=0$) im Ursprung nicht differenzierbar, obwohl beide partiellen Ableitungen dort existieren?
A: Entlang der Achsen ist $f$ konstant $0$, also sind beide partiellen Ableitungen im Ursprung $0$. Auf der Diagonale $y=x$ ist $f$ aber konstant $\tfrac12$ — die Funktion ist im Ursprung nicht einmal stetig. Differenzierbare Funktionen sind stetig, also ist $f$ dort nicht differenzierbar; die partiellen Ableitungen „sehen" nur die Achsen.
F: Was drückt der Grenzwert $\lim_{x\to x_0}\frac{|f(x)-f(x_0)-A(x-x_0)|}{|x-x_0|}=0$ aus, und warum steht $|x-x_0|$ im Nenner?
A: Er fordert, dass der Fehler der linearen Näherung **schneller als linear** verschwindet. Der Nenner misst den Fehler **relativ** zum Abstand: Erst wenn dieser relative Fehler gegen null geht, ist $A$ die beste lineare Näherung und nicht bloß irgendeine ungefähr passende Matrix.
F: Warum ist die Matrix $A$ aus der Definition der totalen Differenzierbarkeit automatisch die Jacobi-Matrix?
A: Nähert man sich $x_0$ entlang der $k$-ten Achse, also mit $x=x_0+h\,e_k$, wird die Definition zu „Differenzenquotient nach $x_k$ minus $A\,e_k$ geht gegen null". Also ist die $k$-te Spalte von $A$ die partielle Ableitung nach $x_k$ — Spalte für Spalte stimmt $A$ mit $Df(x_0)$ überein, und $A$ ist eindeutig.
F: Welche Rolle spielt die Stetigkeit der partiellen Ableitungen im Beweis von „stetig partiell differenzierbar ⇒ total differenzierbar"?
A: Man zerlegt die Änderung in Achsenschritte und wendet den Mittelwertsatz an; dabei tauchen die Ableitungen an **Zwischenstellen** auf. Erst die Stetigkeit garantiert, dass sich diese Werte für $h\to0$ den Werten in $x_0$ annähern — die Fehler $\varepsilon_1,\varepsilon_2$ gehen gegen null, und der Rest wird schneller als $|h|$ klein.
F: Warum ist die Ableitung einer Verkettung gerade das Matrixprodukt $Df(g(x))\,Dg(x)$?
A: Weil die Linearisierung der Verkettung die Verkettung der Linearisierungen ist: Erst nähert $Dg(x)$ den Schritt von $g$ an, dann $Df(g(x))$ die Reaktion von $f$ darauf. Lineare Abbildungen hintereinander auszuführen heißt, ihre Matrizen zu multiplizieren — in 1D ist das „äußere mal innere Ableitung".
F: Warum ist die Änderung eines Skalarfelds längs einer Kurve gerade $\frac{d}{dt}\varphi(\gamma(t))=\nabla\varphi\cdot\dot\gamma$, und wann ist sie null?
A: Es ist die Kettenregel für $\varphi\circ\gamma$: Die Zeile $D\varphi$ mal die Spalte $\dot\gamma$ ergibt das Skalarprodukt $\nabla\varphi\cdot\dot\gamma$ (beim Beispiel $\varphi=xy$, $\gamma=(t,t^2)$ kommt $3t^2$ heraus). Null wird es, wenn man **senkrecht** zum Gradienten läuft — entlang einer Niveaulinie.
:::
