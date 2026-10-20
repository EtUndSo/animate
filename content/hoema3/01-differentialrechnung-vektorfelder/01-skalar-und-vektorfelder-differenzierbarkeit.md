---
title: Skalarfelder, Vektorfelder und die Jacobi-Matrix
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010100
summary: Von Grund auf – wie die Differentialrechnung von einer Variablen auf Abbildungen $\vec F:\mathbb{R}^n\to\mathbb{R}^m$ erweitert wird. Leitbild ist ein Gitter auf einem Gummituch unter der Lupe – bei starker Vergrößerung wird jede glatte Verzerrung linear, und die Matrix dahinter ist die Jacobi-Matrix $D\vec F$; ihre Spalten sind die Gitterpfeile, die partiellen Ableitungen. Mit totaler Differenzierbarkeit samt zwei Gegenbeispielen, dem Kriterium „stetige partielle Ableitungen", dem Satz von Schwarz samt Gegenbeispiel und der Kettenregel $D(\vec F\circ\vec G)=D\vec F\,D\vec G$.
tags: Skalarfeld, Vektorfeld, partielle Ableitung, Jacobi-Matrix, totale Differenzierbarkeit, lineare Approximation, Kettenregel, stetig differenzierbar, Satz von Schwarz
---

## Anschaulich

Stell dir zwei Landkarten vor. Auf der ersten steht an jedem Ort eine **Zahl** — die Temperatur. Das ist ein
__Skalarfeld__. Auf der zweiten steht an jedem Ort ein **Pfeil** — Windrichtung und Windstärke. Das ist ein
__Vektorfeld__.

Die Höhere Mathematik III beginnt mit der Frage: Was ist die **Ableitung** eines solchen Feldes?

In HM1 war die Ableitung einer Funktion $f:\mathbb{R}\to\mathbb{R}$ eine einzige Zahl $f'(x)$, die Steigung der
Tangente. Dahinter steckt eine tiefere Idee: Hält man eine **Lupe** an den Graphen und vergrößert immer stärker, sieht
er aus wie eine **Gerade**. Die Ableitung beschreibt diese beste **lineare Näherung**.

**Das Leitbild dieses Artikels: das Gitter unter der Lupe.** Zeichne ein feines Karogitter auf ein Gummituch und
verzerre das Tuch — ziehe, drehe, beule es. Jeder Punkt des Tuchs wandert an einen neuen Ort, und die Gitterlinien
werden krumm. Das ist eine Abbildung der Ebene in die Ebene.

Hält man nun die Lupe an einen Punkt und vergrößert genug, werden die krummen Gitterlinien wieder **gerade** und
gleichabständig. Aus den kleinen Quadraten sind lauter gleiche **Parallelogramme** geworden. Eine Abbildung, die ein
Quadratgitter so in ein Parallelogramm-Gitter verwandelt, ist — vom verschobenen Mittelpunkt abgesehen — **linear**.
Und eine lineare Abbildung ist eine **Matrix**. Diese Matrix ist die __Jacobi-Matrix__, die Ableitung der Abbildung an
diesem Punkt.

Dieses Bild — Gitter, Gummituch und Lupe — begleitet uns durch den ganzen Artikel. Auf diesem einen Baustein ruht die
ganze Vektoranalysis: Gradient, Divergenz, Rotation und die Integralsätze.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-feld-und-jacobi · Vorlage: feld-linearisierung-2d
Ein Karogitter auf einem Gummituch wird durch eine Abbildung $\vec F:\mathbb{R}^2\to\mathbb{R}^2$ verzerrt; die
Gitterlinien werden krumm. Eine Lupe über dem Bildpunkt $\vec F(\vec x_0)$ zoomt stufenlos hinein: Die krummen Maschen
werden gerade, und das Bild deckt sich immer besser mit dem Parallelogramm-Gitter der Matrix $D\vec F(\vec x_0)$, das als
Overlay eingeblendet wird. Kernaussage: Unter der Lupe wird jede glatte Abbildung linear — und diese lineare Abbildung
ist die Jacobi-Matrix. (Rot = Bildgitter von $\vec F$, orange = Parallelogramm-Gitter von $D\vec F$, grau =
Ausgangsgitter, gestrichelt = Lupenrand.)
:::

## Was ist ein Feld?

Ein __Feld__ ordnet jedem Punkt eines Bereichs eine Größe zu. Formal ist es eine **Abbildung**

$$\vec F:U\to\mathbb{R}^m, \qquad \vec x=(x_1,\ldots,x_n)\;\mapsto\;\vec F(\vec x)=\big(F_1(\vec x),\ldots,F_m(\vec x)\big),$$

definiert auf einer offenen Menge $U\subseteq\mathbb{R}^n$ (was „offen" heißt, folgt gleich).

**So liest man diese Zeile:** Der Pfeil $\to$ nennt die Räume — Eingaben aus $U$, Ausgaben in $\mathbb{R}^m$. Der Pfeil
$\mapsto$ nennt die Zuordnung. Die **Eingabe** ist ein Punkt $\vec x$ mit $n$ Koordinaten; für einen Ort im Raum ist
$n=3$. Die **Ausgabe** ist ein Vektor mit $m$ Komponenten. Jede Komponente $F_j:U\to\mathbb{R}$ ist eine gewöhnliche
reellwertige Funktion mehrerer Veränderlicher.

Je nach Art der Ausgabe unterscheidet man:

- __Skalarfeld__ ($m=1$): jedem Ort eine **Zahl**. Wir schreiben es klein und ohne Pfeil, $f:U\to\mathbb{R}$.
  Beispiele: die Temperatur oder das elektrische Potential $\varphi(x,y,z)$.
- __Vektorfeld__ ($m=n$): jedem Ort ein **Pfeil** im selben Raum. Beispiele: die Strömungsgeschwindigkeit einer
  Flüssigkeit oder das elektrische Feld $\vec E(x,y,z)\in\mathbb{R}^3$.

Allgemein heißt $\vec F$ eine __vektorwertige Abbildung__ — auch dann, wenn $m$ und $n$ verschieden sind, etwa bei einer
Kurve, die jeder Zeit $t\in\mathbb{R}$ einen Ort im $\mathbb{R}^3$ zuordnet. Für die Differentialrechnung macht das keinen
Unterschied. Wir schreiben Vektorfelder und vektorwertige Abbildungen groß und mit Pfeil ($\vec F$, $\vec G$, $\vec E$);
nur Kurven heißen traditionell klein, $\vec\gamma$.

**Im Bild: zwei Lesarten derselben Abbildung.** Für $m=n$ kann man den Vektor $\vec F(\vec x)$ auf zwei Arten lesen:
als **Pfeil**, den man an den Punkt $\vec x$ heftet (die Windkarte), oder als **neuen Ort**, an den der Punkt $\vec x$
wandert (das Gummituch). Mathematisch ist es dasselbe Objekt mit derselben Ableitung. Für das Leitbild benutzen wir meist
die zweite Lesart, weil man dort das Gitter sieht.

**Offene Mengen.** Für einen Punkt $\vec x\in\mathbb{R}^n$ und einen Radius $\varepsilon>0$ ist die __offene Kugel__ um
$\vec x$ die Menge aller Punkte, deren Abstand von $\vec x$ kleiner als $\varepsilon$ ist:

$$B_\varepsilon(\vec x) = \big\{\,\vec z\in\mathbb{R}^n \;:\; \lvert\vec z-\vec x\rvert<\varepsilon\,\big\}.$$

Eine Menge $U\subseteq\mathbb{R}^n$ heißt __offen__, wenn um jeden ihrer Punkte noch eine solche Kugel ganz in $U$ liegt —
wenn es also zu jedem $\vec x\in U$ einen Radius $\varepsilon>0$ gibt mit

$$B_\varepsilon(\vec x)\subseteq U.$$

**Im Bild:** Um jeden Punkt von $U$ passt noch ein ganzes kleines Gitterstück. Von jedem Punkt aus hat man also in
**jede** Richtung ein Stückchen Platz — genau das braucht man, um Differenzenquotienten in allen Richtungen zu bilden.
Die offene Einheitskreisscheibe $B_1(\vec 0)\subseteq\mathbb{R}^2$ ist offen. Nimmt man den Randkreis dazu, ist sie es
nicht mehr: Um einen Randpunkt ragt jede noch so kleine Kreisscheibe hinaus.

:::herleitung
Zu einem Punkt $\vec x$ der offenen Kreisscheibe wählt man als Radius seinen Abstand zum Rand:

$$\varepsilon = 1-\lvert\vec x\rvert > 0.$$

Für jeden Punkt $\vec z\in B_\varepsilon(\vec x)$ gilt dann nach der Dreiecksungleichung

$$\lvert\vec z\rvert \le \lvert\vec x\rvert + \lvert\vec z-\vec x\rvert < \lvert\vec x\rvert + \varepsilon = 1.$$

Die ganze Kugel $B_\varepsilon(\vec x)$ liegt also in der Kreisscheibe. Ein Randpunkt $\vec x$ vom Betrag $1$ hat dagegen
in jeder Kugel um sich den Punkt $(1+\tfrac\varepsilon2)\,\vec x$: Er hat von $\vec x$ den Abstand $\tfrac\varepsilon2$,
liegt aber mit dem Betrag $1+\tfrac\varepsilon2$ außerhalb der Scheibe.
:::

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-skalarfeld-vs-vektorfeld · Vorlage: feld-vergleich-2d
Drei Bilder über demselben Ausschnitt der Ebene: links ein Skalarfeld als Farbkarte (Temperatur, eine Zahl pro Punkt),
in der Mitte ein Vektorfeld als Pfeilgitter (Wind, ein Pfeil pro Punkt), rechts dieselbe Abbildung als Gummituch — jeder
Gitterpunkt $\vec x$ wandert an den Ort $\vec F(\vec x)$. Ein Umschalter überblendet zwischen „Pfeil anheften" und
„Punkt verschieben". Kernaussage: Ein Vektorfeld und eine Verzerrung der Ebene sind dasselbe mathematische Objekt.
(Rot = Feldwerte bzw. Bildpunkte, blau = Pfeile, grau = Gitter.)
:::

## Partielle Ableitungen: die Gitterpfeile

Bei $f:\mathbb{R}\to\mathbb{R}$ gibt es nur eine Richtung. Bei $\vec F:U\to\mathbb{R}^m$ gibt es $n$
Koordinatenrichtungen, in die man gehen kann, und $m$ Komponenten, die sich dabei ändern.

Der erste Baustein: Man bewegt sich nur entlang **einer** Gitterlinie. Die __Einheitsvektoren__
$\vec e_1,\ldots,\vec e_n$ zeigen in die Achsenrichtungen; $\vec e_k$ hat an Position $k$ eine $1$ und sonst nur
Nullen. Die $k$-te Gitterlinie durch $\vec x$ ist die Gerade

$$t\;\mapsto\;\vec x+t\,\vec e_k \qquad (t\in\mathbb{R}),$$

auf der sich nur die $k$-te Koordinate ändert; für kleine $t$ liegt sie in $U$, weil $U$ offen ist. Die __partielle
Ableitung__ der Komponente $F_j$ nach $x_k$ ist die gewöhnliche HM1-Ableitung längs dieser Linie:

$$\frac{\partial F_j}{\partial x_k}(\vec x) = \lim_{t\to0}\frac{F_j(\vec x+t\,\vec e_k)-F_j(\vec x)}{t}.$$

Man hält also alle anderen Koordinaten fest; nur die $k$-te ist „lebendig". Rechnerisch leitet man nach $x_k$ ab und
behandelt die übrigen Variablen wie Konstanten. Existieren alle diese Grenzwerte, heißt $\vec F$ __partiell
differenzierbar__.

**Im Bild:** Das Gummituch biegt die $k$-te Gitterlinie durch $\vec x$ zu einer Bildkurve
$t\mapsto\vec F(\vec x+t\,\vec e_k)$. Fasst man die Ableitungen aller Komponenten zu einem Vektor zusammen,

$$\frac{\partial\vec F}{\partial x_k}(\vec x) = \Big(\frac{\partial F_1}{\partial x_k}(\vec x),\ldots,\frac{\partial F_m}{\partial x_k}(\vec x)\Big)^{T},$$

so ist das die Geschwindigkeit, mit der diese Bildkurve bei $t=0$ durchlaufen wird — ein **Tangentenpfeil** an die
verbogene Gitterlinie. Wir nennen ihn den $k$-ten **Gitterpfeil**. Ein Gitterschritt der kleinen Länge $t$ in Richtung
$\vec e_k$ wird ungefähr auf den Pfeil $t\,\partial\vec F/\partial x_k$ abgebildet; unter der Lupe ist das eine Kante
der kleinen Parallelogramm-Masche.

**Zahlenbeispiel: das „Quadrieren".** Wir betrachten die Abbildung $\vec F:\mathbb{R}^2\to\mathbb{R}^2$ mit

$$\vec F(x_1,x_2) = \big(x_1^2-x_2^2,\;2x_1x_2\big).$$

Man hält zuerst $x_2$ fest und leitet nach $x_1$ ab, dann umgekehrt. Das ergibt die beiden Gitterpfeile

$$\frac{\partial\vec F}{\partial x_1}(\vec x) = \begin{pmatrix} 2x_1 \\ 2x_2 \end{pmatrix}, \qquad \frac{\partial\vec F}{\partial x_2}(\vec x) = \begin{pmatrix} -2x_2 \\ 2x_1 \end{pmatrix}.$$

Am Punkt $(1,0)$ sind es $(2,0)$ und $(0,2)$: Beide Gitterrichtungen bleiben, wie sie waren, nur doppelt so lang. Am
Punkt $(0,1)$ sind es $(0,2)$ und $(-2,0)$: Beide Richtungen sind zusätzlich um $90^\circ$ gedreht.

Den Namen erklären die komplexen Zahlen: Quadriert man $x_1+\mathrm i\,x_2$, so sind Real- und Imaginärteil genau die
beiden Komponenten,

$$(x_1+\mathrm i\,x_2)^2 = \underbrace{x_1^2-x_2^2}_{F_1} + \mathrm i\,\underbrace{2x_1x_2}_{F_2}.$$

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-gitterpfeile · Vorlage: gitterlinien-tangenten-2d
Links das Ausgangsgitter mit dem Punkt $\vec x$ und den beiden Gitterlinien durch ihn (waagerecht in Richtung
$\vec e_1$, senkrecht in Richtung $\vec e_2$). Rechts ihre Bildkurven unter dem Quadrieren $\vec F$, mit den
Tangentenpfeilen $\partial\vec F/\partial x_1$ und $\partial\vec F/\partial x_2$ am Bildpunkt. Ein Schieberegler bewegt
$\vec x$ auf dem Einheitskreis: Die Gitterpfeile drehen sich mit dem Polarwinkel mit und bleiben gleich lang.
Kernaussage: Partielle Ableitungen sind die Tangentenpfeile der verbogenen Gitterlinien. (Rot = Bildkurven, orange =
Gitterpfeile, grau = Gitter.)
:::

Für die vollständige lokale Änderung braucht man **alle** Gitterpfeile — jede der $m$ Komponenten nach jeder der $n$
Koordinaten abgeleitet. Das sind $m\cdot n$ Zahlen, und die ordnet man in einer **Matrix** an.

## Die Jacobi-Matrix

Für eine partiell differenzierbare Abbildung $\vec F$ mit den Komponenten $F_1,\ldots,F_m$ heißt die Matrix aller
ersten partiellen Ableitungen die __Jacobi-Matrix__:

:::formel Definition
$$D\vec F = \left(\frac{\partial F_j}{\partial x_k}\right)_{jk} = \begin{pmatrix} \dfrac{\partial F_1}{\partial x_1} & \cdots & \dfrac{\partial F_1}{\partial x_n} \\[2mm] \vdots & \ddots & \vdots \\[1mm] \dfrac{\partial F_m}{\partial x_1} & \cdots & \dfrac{\partial F_m}{\partial x_n} \end{pmatrix} \in \mathbb{R}^{m \times n}.$$
:::

**So liest man sie:** Der Eintrag in Zeile $j$, Spalte $k$ ist $\partial F_j/\partial x_k$. Die Form passt zur
Abbildung: $m$ Zeilen, so viele wie Ausgabe-Komponenten, und $n$ Spalten, so viele wie Eingabe-Koordinaten. Ausgewertet
an einem Punkt $\vec x\in U$ ist $D\vec F(\vec x)$ eine Matrix aus Zahlen; die Zuordnung $\vec x\mapsto D\vec F(\vec x)$
macht aus jedem Punkt eine Matrix.

**Im Bild: Die Spalten sind die Gitterpfeile.** Spalte $k$ enthält die Ableitungen aller Komponenten nach $x_k$ — genau
den $k$-ten Gitterpfeil. Das passt zu dem, was eine Matrix tut: Multipliziert man sie mit $\vec e_k$, bleibt von jeder
Zeile nur der $k$-te Eintrag übrig, also die $k$-te Spalte:

$$D\vec F(\vec x)\,\vec e_k = \frac{\partial\vec F}{\partial x_k}(\vec x).$$

Die Jacobi-Matrix ist also die lineare Abbildung, die jede Gitterrichtung $\vec e_k$ auf ihren Gitterpfeil schickt.

**Wozu das Ganze? Die lineare Näherung.** Ein kleiner Schritt $\vec h=(h_1,\ldots,h_n)$ im $\mathbb{R}^n$ setzt sich aus
Gitterschritten zusammen:

$$\vec h = h_1\,\vec e_1+\cdots+h_n\,\vec e_n.$$

Unter der Lupe wird jeder Gitterschritt $\vec e_k$ zu seinem Gitterpfeil. Also sollte der Schritt $\vec h$ ungefähr auf
dieselbe Kombination der Gitterpfeile abgebildet werden — und die ist genau „Matrix mal Schritt":

$$\vec F(\vec x_0+\vec h) \;\approx\; \vec F(\vec x_0) + \sum_{k=1}^n h_k\,\frac{\partial\vec F}{\partial x_k}(\vec x_0) = \vec F(\vec x_0) + D\vec F(\vec x_0)\,\vec h.$$

Links steht der neue Funktionswert, ein Vektor in $\mathbb{R}^m$. Rechts steht der alte Wert plus „Matrix mal Schritt":
Eine $m\times n$-Matrix mal einem Vektor aus $\mathbb{R}^n$ ergibt einen Vektor aus $\mathbb{R}^m$. Wann dieses
„$\approx$" wirklich gilt und wie gut es sein muss, klärt der Abschnitt über totale Differenzierbarkeit — dort zeigt sich
auch, dass es nicht immer gilt.

**Der Spezialfall Skalarfeld** ($m=1$). Dann hat $Df$ nur **eine Zeile**, ist also ein Zeilenvektor in
$\mathbb{R}^{1\times n}$. Seinen transponierten Spaltenvektor nennt man den __Gradienten__:

$$\nabla f := \operatorname{grad} f = \left(\frac{\partial f}{\partial x_1},\ldots,\frac{\partial f}{\partial x_n}\right)^{\!T} \in \mathbb{R}^n, \qquad \nabla f = (Df)^{T}.$$

Das Symbol $\nabla$ („Nabla") ist formal selbst ein Spaltenvektor aus Ableitungsoperatoren:

$$\nabla = \left(\frac{\partial}{\partial x_1},\ldots,\frac{\partial}{\partial x_n}\right)^{T}.$$

„Multipliziert" man ihn mit einer Funktion $f$, entsteht der Gradient. Ein __Differentialoperator__ ist eine Vorschrift,
die aus einer Funktion durch Ableiten eine neue macht; weil der Gradient nur erste Ableitungen enthält, ist er einer
**erster Ordnung**. Er macht aus einer differenzierbaren Funktion ein Vektorfeld.

**Im Bild:** Bei einem Skalarfeld zeigt die Lupe statt eines Gitters eine **Landschaft**: Der Graph von $f$ über der
Ebene wird unter starker Vergrößerung zu einer **schiefen Ebene**. Die lineare Näherung lautet hier

$$f(\vec x_0+\vec h) \;\approx\; f(\vec x_0) + Df(\vec x_0)\,\vec h = f(\vec x_0) + \nabla f(\vec x_0)\cdot\vec h.$$

Das letzte Gleichheitszeichen ist nur Umschreiben: Zeile mal Spalte ist dasselbe wie das Skalarprodukt der beiden als
Spalten gelesenen Vektoren. Für $n=2$ enthält der Gradient die beiden Steigungen der schiefen Ebene — in $x_1$- und in
$x_2$-Richtung.

**Gradient und Jacobi-Matrix sind zu unterscheiden.** Sie enthalten dieselben Zahlen, spielen aber verschiedene Rollen.
$Df$ ist eine **Zeile** und wird als lineare Abbildung benutzt: Von links an einen Schritt $\vec h$ (eine Spalte)
multipliziert, liefert sie eine Zahl — die Höhenänderung. Der Gradient $\nabla f$ ist eine **Spalte**, also ein Vektor im
selben Raum wie die Punkte, und wird als Pfeil gedeutet: als Richtung des steilsten Anstiegs (nächster Artikel).

**Die Zeilen der Jacobi-Matrix sind Gradienten.** Zeile $j$ von $D\vec F$ sammelt die Ableitungen **einer** Komponente
$F_j$ nach allen Koordinaten. Das ist genau der transponierte Gradient dieser Komponente:

$$D\vec F = \begin{pmatrix} (\nabla F_1)^T \\ \vdots \\ (\nabla F_m)^T \end{pmatrix}.$$

**Im Bild:** Jede Komponente $F_j$ ist für sich eine Landschaft, und ihre Zeile enthält deren Steigungen. Die Spalten
lesen die Matrix nach Gitterrichtungen, die Zeilen nach Komponenten.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-jacobi-aufbau · Vorlage: matrix-schema
Die Jacobi-Matrix als $m\times n$-Kasten. Ein Umschalter hebt entweder Spalte $k$ hervor — daneben der zugehörige
Gitterpfeil $\partial\vec F/\partial x_k$ als Tangente an die verbogene Gitterlinie — oder Zeile $j$ — daneben die
Landschaft der Komponente $F_j$ mit ihrem Gradienten $\nabla F_j$. Darunter der Skalar-Spezialfall: eine einzelne Zeile
$Df\in\mathbb{R}^{1\times n}$ und ihr transponierter Gradient $\nabla f\in\mathbb{R}^n$ als Spalte. Kernaussage: Spalten
sind Gitterpfeile, Zeilen sind Gradienten der Komponenten. (Orange = hervorgehobene Spalte/Zeile, rot = Gitterpfeil bzw.
Gradient, grau = übrige Einträge.)
:::

## Zahlenbeispiel: das „Quadrieren" in der Ebene

Beim Quadrieren bilden die beiden Gitterpfeile die Spalten der Jacobi-Matrix:

$$D\vec F(\vec x) = \begin{pmatrix} 2x_1 & -2x_2 \\[1mm] 2x_2 & 2x_1 \end{pmatrix}.$$

An jedem Punkt ist $D\vec F$ eine andere Matrix. Was sie mit einer winzigen Masche anstellt, sieht man an zwei
konkreten Punkten:

$$D\vec F(1,0) = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}, \qquad D\vec F(0,1) = \begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix} = 2\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$

**Im Bild:** Bei $(1,0)$ ist das eine reine **Streckung** um den Faktor $2$: Eine winzige Gittermasche wird doppelt so
breit und doppelt so hoch, aber nicht gedreht. Bei $(0,1)$ steht rechts das Doppelte der Drehmatrix um $90^\circ$: Die
Masche wird um $90^\circ$ **gedreht** und zugleich um den Faktor $2$ **gestreckt**.

**Allgemein dreht und streckt $D\vec F$.** Schreibt man einen Punkt $\vec x\neq\vec 0$ in Polarkoordinaten — Abstand
$r>0$ vom Ursprung, Winkel $\theta$ zur $x_1$-Achse —, so ist

$$\vec x = (r\cos\theta,\ r\sin\theta), \qquad D\vec F(\vec x) = 2r\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$

Die Matrix rechts ist die Drehung um den Winkel $\theta$. Unter der Lupe wird also jede kleine Masche um den Polarwinkel
ihres Punktes gedreht und um den Faktor $2r$ gestreckt — sie bleibt ein Quadrat.

:::herleitung
Man setzt die Polarkoordinaten in die Einträge der Jacobi-Matrix ein:

$$2x_1 = 2r\cos\theta, \qquad 2x_2 = 2r\sin\theta.$$

Jeder Eintrag von $D\vec F$ wird damit $2r$ mal der entsprechende Eintrag der Drehmatrix; den gemeinsamen Faktor $2r$
zieht man vor die Matrix.

**Im Bild:** Die Drehmatrix dreht beide Gitterrichtungen um denselben Winkel und lässt ihre Längen gleich; der Faktor
$2r$ streckt beide gleich stark. Deshalb bleibt ein Quadrat ein Quadrat.
:::

**Zahlenprobe der linearen Näherung.** Wir gehen vom Punkt $(1,0)$ einen kleinen Schritt nach oben:

$$\vec x_0 = (1,0), \qquad \vec h = \big(0,\ \tfrac1{10}\big).$$

Der echte Wert und die lineare Näherung sind

$$\vec F\big(1,\tfrac1{10}\big) = \big(\tfrac{99}{100},\ \tfrac15\big), \qquad \vec F(1,0)+D\vec F(1,0)\,\vec h = (1,0)+\big(0,\ \tfrac15\big) = \big(1,\ \tfrac15\big).$$

Der Fehler ist der Unterschied der beiden:

$$\vec F\big(1,\tfrac1{10}\big) - \Big(\vec F(1,0)+D\vec F(1,0)\,\vec h\Big) = \big(-\tfrac1{100},\ 0\big).$$

Er hat die Länge $\tfrac1{100}$ — bei einer Schrittlänge von $\tfrac1{10}$. Der Fehler ist also viel kleiner als der
Schritt selbst. Der nächste Abschnitt macht aus dieser Beobachtung die Definition der Differenzierbarkeit.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-quadrieren-gitter · Vorlage: abbildung-gitter-2d
Links die Ebene mit zwei kleinen Gittermaschen bei $(1,0)$ und $(0,1)$; rechts ihre Bilder unter dem Quadrieren
$\vec F$. Die Masche bei $(1,0)$ wird nur gestreckt (Faktor 2), die bei $(0,1)$ zusätzlich um $90^\circ$ gedreht.
Daneben jeweils die Matrix $D\vec F$ am Punkt. Ein Zoom-Regler verkleinert die Maschen: Der Abstand zwischen echter
Bildmasche und Parallelogramm von $D\vec F$ schrumpft quadratisch (Anzeige „Fehler $=|\vec h|^2$"). Kernaussage: Die
Jacobi-Matrix dreht und streckt jede kleine Masche, und der Fehler wird schneller klein als die Masche. (Grau =
Ausgangsgitter, rot = Bild unter $\vec F$, orange = lineare Näherung $D\vec F$.)
:::

## Totale Differenzierbarkeit: was die Lupe verspricht

Die bloße Existenz aller partiellen Ableitungen ist noch **nicht** die eigentliche Differenzierbarkeit. Partielle
Ableitungen sehen nur die Gitterlinien. Das wahre Kriterium verlangt die lineare Näherung in **alle** Richtungen
zugleich — und sagt genau, wie gut sie sein muss.

**Die zwei Akteure:** die Abbildung $\vec F:U\to\mathbb{R}^m$ auf der offenen Menge $U\subseteq\mathbb{R}^n$ — das
verzerrte Gummituch — und eine Matrix $A\in\mathbb{R}^{m\times n}$ — ein Parallelogramm-Gitter, das das Tuch nahe dem
Punkt $\vec x_0\in U$ ersetzen soll.

**Das Zusammenspiel:** *Wird der Unterschied zwischen Tuch und Ersatzgitter unter der Lupe unsichtbar?*

Die Abbildung $\vec F$ heißt __(total) differenzierbar__ an der Stelle $\vec x_0$, wenn es eine Matrix $A$ gibt, sodass
der Fehler der linearen Näherung **schneller als linear** verschwindet:

:::formel Definition
$$\lim_{\vec x \to \vec x_0} \frac{\lvert \vec F(\vec x) - \vec F(\vec x_0) - A\,(\vec x - \vec x_0)\rvert}{\lvert \vec x - \vec x_0\rvert} = 0.$$
:::

Ist $\vec F$ an jeder Stelle von $U$ differenzierbar, heißt $\vec F$ __differenzierbar auf $U$__.

**Stück für Stück gelesen:** Im Zähler steht der Fehler der linearen Näherung — der Abstand zwischen dem echten Wert
$\vec F(\vec x)$ und der Ersatzrechnung $\vec F(\vec x_0)+A(\vec x-\vec x_0)$. Der Nenner misst diesen Fehler
**relativ** zum Abstand vom Punkt.

**Im Bild: genau das Versprechen der Lupe.** Schaut man auf Punkte im Abstand $\lvert\vec x-\vec x_0\rvert$ und
vergrößert so stark, dass dieser Abstand auf dem Bildschirm die Länge $1$ hat, so wird auch der Fehler um diesen Faktor
vergrößert. Der Quotient in der Definition ist also genau der **Fehler, wie man ihn unter der Lupe sieht**. Die
Definition verlangt, dass er gegen null geht: Mit wachsender Vergrößerung lassen sich echtes Bildgitter und
Parallelogramm-Gitter immer weniger unterscheiden. Eine bloß „ungefähr passende" Matrix würde unter der Lupe einen
sichtbaren Rest übrig lassen.

**Beispiel: Beim Quadrieren ist der Fehler genau $\lvert\vec h\rvert^2$.** Für einen beliebigen Punkt $\vec x_0$ und
einen beliebigen Schritt $\vec h=(h_1,h_2)$ ist der Fehler der linearen Näherung das Quadrieren des Schritts selbst:

$$\vec F(\vec x_0+\vec h)-\vec F(\vec x_0)-D\vec F(\vec x_0)\,\vec h = \big(h_1^2-h_2^2,\;2h_1h_2\big) = \vec F(\vec h).$$

Seine Länge ist exakt das Quadrat der Schrittlänge, der relative Fehler also die Schrittlänge selbst:

$$\big\lvert\vec F(\vec h)\big\rvert = \lvert\vec h\rvert^2, \qquad \frac{\lvert\vec F(\vec h)\rvert}{\lvert\vec h\rvert} = \lvert\vec h\rvert \;\to\; 0.$$

Das Quadrieren ist also an jeder Stelle total differenzierbar, mit $A=D\vec F(\vec x_0)$. Die Zahlenprobe oben passt
dazu: Schritt $\tfrac1{10}$, Fehler $\tfrac1{100}$.

:::herleitung
Mit $\vec x_0=(x_1,x_2)$ multipliziert man die erste Komponente aus und sortiert nach der Ordnung in $\vec h$:

$$(x_1+h_1)^2-(x_2+h_2)^2 = \underbrace{x_1^2-x_2^2}_{F_1(\vec x_0)} + \underbrace{2x_1h_1-2x_2h_2}_{\text{1. Zeile von } D\vec F(\vec x_0)\,\vec h} + \underbrace{h_1^2-h_2^2}_{\text{Rest}}.$$

Ebenso die zweite Komponente:

$$2(x_1+h_1)(x_2+h_2) = \underbrace{2x_1x_2}_{F_2(\vec x_0)} + \underbrace{2x_2h_1+2x_1h_2}_{\text{2. Zeile von } D\vec F(\vec x_0)\,\vec h} + \underbrace{2h_1h_2}_{\text{Rest}}.$$

Die Länge des Rests berechnet man mit der binomischen Formel:

$$\lvert\vec F(\vec h)\rvert^2 = (h_1^2-h_2^2)^2+4h_1^2h_2^2 = h_1^4+2h_1^2h_2^2+h_2^4 = (h_1^2+h_2^2)^2 = \lvert\vec h\rvert^4.$$

**Im Bild:** Der Rest ist von zweiter Ordnung. Halbiert man die Maschenweite, viertelt sich der Fehler, während sich die
Masche selbst nur halbiert — unter der Lupe verschwindet er deshalb.
:::

## Warum daraus Eindeutigkeit und Stetigkeit folgen

**Die Matrix ist automatisch die Jacobi-Matrix.** Ist $\vec F$ in $\vec x_0$ differenzierbar, so existieren dort alle
partiellen Ableitungen, und die Matrix aus der Definition ist eindeutig:

$$A = D\vec F(\vec x_0).$$

**Im Bild:** Ein Parallelogramm-Gitter ist durch seine Kanten festgelegt. Und seine Kanten müssen die Gitterpfeile sein,
weil die Definition auch für Annäherungen entlang der Gitterlinien gilt.

:::herleitung
Man nähert sich $\vec x_0$ nur entlang der $k$-ten Gitterlinie, setzt also für reelle $t\to0$

$$\vec x = \vec x_0 + t\,\vec e_k, \qquad \text{sodass} \quad \lvert\vec x-\vec x_0\rvert = \lvert t\rvert.$$

Eingesetzt in die Definition wird der Quotient zu

$$\left\lvert\frac{\vec F(\vec x_0+t\,\vec e_k)-\vec F(\vec x_0)}{t} - A\,\vec e_k\right\rvert \;\longrightarrow\; 0 \qquad (t\to0).$$

Der erste Term ist — komponentenweise — der Differenzenquotient der partiellen Ableitung nach $x_k$. Er konvergiert
also, und zwar gegen $A\,\vec e_k$, die $k$-te Spalte von $A$.

Damit existiert die partielle Ableitung nach $x_k$, und sie ist die $k$-te Spalte von $A$. Spalte für Spalte stimmt $A$
mit der Jacobi-Matrix überein; ein zweites solches $A$ kann es also nicht geben.
:::

**Differenzierbar heißt auch stetig.** Ist $\vec F$ in $\vec x_0$ differenzierbar, so ist $\vec F$ dort stetig.
**Im Bild:** Wo die Lupe ein Parallelogramm-Gitter zeigt, kann das Tuch nicht gerissen sein.

:::herleitung
**Vorweg eine Abschätzung für Matrizen.** Für $A\in\mathbb{R}^{m\times n}$ mit den Einträgen $a_{jk}$ und
$\vec h\in\mathbb{R}^n$ ist die $j$-te Komponente von $A\vec h$ das Skalarprodukt der $j$-ten Zeile mit $\vec h$. Nach
der Cauchy-Schwarz-Ungleichung ist ihr Betrag höchstens die Länge der Zeile mal $\lvert\vec h\rvert$. Quadriert und über
alle Zeilen summiert, ergibt das

$$\lvert A\vec h\rvert \le c\,\lvert\vec h\rvert \qquad\text{mit}\qquad c = \Big(\sum_{j,k}a_{jk}^2\Big)^{1/2}.$$

**Im Bild:** Eine Matrix vergrößert Längen höchstens um einen festen Faktor — ein Parallelogramm-Gitter ist nie unendlich
gestreckt.

Damit zerlegt man die Änderung von $\vec F$ in den linearen Anteil und den Fehler:

$$\vec F(\vec x)-\vec F(\vec x_0) = \underbrace{A\,(\vec x-\vec x_0)}_{\text{Länge}\;\le\;c\,|\vec x-\vec x_0|} + \underbrace{\vec F(\vec x)-\vec F(\vec x_0)-A\,(\vec x-\vec x_0)}_{\text{klein gegen } |\vec x-\vec x_0|}.$$

Beide Teile gehen für $\vec x\to\vec x_0$ gegen null, nach der Dreiecksungleichung also auch ihre Summe
$\vec F(\vec x)-\vec F(\vec x_0)$.
:::

## Wann partielle Ableitungen genügen

**Stolperstein — partielle Ableitungen allein reichen nicht.** Sie sehen nur, was entlang der Gitterlinien passiert.
Das klassische Gegenbeispiel ist die Funktion $f:\mathbb{R}^2\to\mathbb{R}$ mit

$$f(x,y) = \begin{cases} \dfrac{xy}{x^2+y^2}, & (x,y)\neq(0,0),\\[2mm] 0, & (x,y)=(0,0). \end{cases}$$

Entlang beider Achsen ist $f$ konstant null:

$$f(x,0) = 0, \qquad f(0,y) = 0 \qquad \text{für alle } x,y\in\mathbb{R}.$$

Deshalb sind beide Differenzenquotienten im Ursprung identisch null, und beide partiellen Ableitungen existieren:

$$\frac{\partial f}{\partial x}(0,0) = \lim_{t\to0}\frac{f(t,0)-f(0,0)}{t} = 0, \qquad \frac{\partial f}{\partial y}(0,0) = \lim_{t\to0}\frac{f(0,t)-f(0,0)}{t} = 0.$$

Die Jacobi-Matrix im Ursprung ist also die Nullmatrix — beide Gitterpfeile sind null.

Entlang der Diagonale ist $f$ dagegen konstant $\tfrac12$:

$$f(t,t) = \frac{t\cdot t}{t^2+t^2} = \frac12 \qquad (t\neq0).$$

Nähert man sich dem Ursprung auf der Diagonale, strebt $f$ also gegen $\tfrac12$ — der Funktionswert im Ursprung ist aber
$0$. Die Funktion ist dort nicht einmal **stetig** und nach dem vorigen Abschnitt erst recht nicht differenzierbar.

**Im Bild: Hier hilft keine Lupe.** Streckt man die Koordinaten um einen Faktor $\lambda>0$, ändert sich der Wert nicht:

$$f(\lambda x,\lambda y) = \frac{\lambda^2\,xy}{\lambda^2\,(x^2+y^2)} = f(x,y) \qquad \big((x,y)\neq(0,0)\big).$$

Jeder noch so kleine Ausschnitt um den Ursprung sieht deshalb vergrößert genauso aus wie der große: ein Grat auf Höhe
$\tfrac12$ über der Diagonale, eine Rinne auf Höhe $-\tfrac12$ über der Gegendiagonale und dazwischen flache Achsen. Eine
schiefe Ebene erscheint nie.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-gegenbeispiel-xy · Vorlage: flaeche-3d
Der Graph von $f=\frac{xy}{x^2+y^2}$ über der Ebene: entlang der Achsen flach auf Höhe $0$, entlang der Diagonale ein
Grat auf Höhe $\tfrac12$, entlang der Gegendiagonale eine Rinne auf Höhe $-\tfrac12$; im Ursprung „zerreißt" die
Fläche. Die beiden Achsenschnitte (partielle Ableitungen $0$) und die Diagonale sind hervorgehoben. Ein Lupen-Regler
zoomt auf den Ursprung — das Bild bleibt bei jeder Vergrößerung exakt gleich. Kernaussage: Partielle Ableitungen sehen
nur die Achsen; die Lupe zeigt hier nie eine Ebene. (Rot = Achsenschnitte, orange = Diagonale, grau = Fläche.)
:::

**Noch schärfer: Auch Stetigkeit hilft nicht.** Die Funktion $g:\mathbb{R}^2\to\mathbb{R}$ mit

$$g(x,y) = \begin{cases} \dfrac{x^2y}{x^2+y^2}, & (x,y)\neq(0,0),\\[2mm] 0, & (x,y)=(0,0) \end{cases}$$

ist im Ursprung stetig, ihre beiden partiellen Ableitungen dort sind null — und trotzdem ist sie dort nicht
differenzierbar.

:::herleitung
**Stetig:** Weil $x^2$ höchstens $x^2+y^2$ ist, ist der Bruch höchstens $1$, also

$$\lvert g(x,y)\rvert = \frac{x^2}{x^2+y^2}\,\lvert y\rvert \le \lvert y\rvert \;\longrightarrow\; 0 \qquad \big((x,y)\to(0,0)\big).$$

**Partielle Ableitungen:** Auf beiden Achsen ist $g$ null, also sind die Differenzenquotienten im Ursprung null wie beim
ersten Beispiel.

**Nicht differenzierbar:** Wäre $g$ im Ursprung differenzierbar, müsste $A$ die Jacobi-Matrix sein, also die Nullmatrix.
Der relative Fehler wäre dann einfach $\lvert g\rvert$ geteilt durch den Abstand. Auf der Diagonale ist er aber konstant:

$$\frac{\lvert g(t,t)\rvert}{\lvert(t,t)\rvert} = \frac{\lvert t\rvert/2}{\sqrt2\,\lvert t\rvert} = \frac{1}{2\sqrt2} \qquad (t\neq0).$$

Er geht also nicht gegen null, die Definition ist verletzt.

**Im Bild:** Diesmal skaliert die Funktion mit:

$$g(\lambda x,\lambda y) = \lambda\,g(x,y).$$

Die Lupe vergrößert Höhen und Breiten gleich stark, also sieht man unter jeder Vergrößerung dieselbe gefaltete Fläche —
stetig, aber mit Falten durch den Ursprung, keine Ebene.
:::

**Die Rettung: stetige partielle Ableitungen.** Existieren alle partiellen Ableitungen auf $U$ und sind sie dort
**stetig**, heißt $\vec F$ __stetig partiell differenzierbar__. Die Menge dieser Abbildungen schreibt man
$C^1(U;\mathbb{R}^m)$. Für sie ist die totale Differenzierbarkeit garantiert:

:::formel Satz
$$\vec F\in C^1(U;\mathbb{R}^m) \quad\Longrightarrow\quad \vec F \text{ ist auf } U \text{ total differenzierbar}.$$
:::

Man nennt solche Abbildungen deshalb einfach __stetig differenzierbar__. In der Praxis ist das der übliche Weg:
partielle Ableitungen ausrechnen, ihre Stetigkeit ansehen — fertig.

**Im Bild:** Stetige partielle Ableitungen heißen: Die Gitterpfeile ändern sich von Punkt zu Punkt nur wenig. Dann ist
ein kleines Gitterstück überall fast gleich verzerrt — und genau das ist ein Parallelogramm-Gitter.

:::herleitung
Wir zeigen es für ein Skalarfeld $f$ zweier Variablen; der allgemeine Fall geht genauso, komponentenweise und mit mehr
Summanden. Für einen kleinen Schritt $\vec h=(h_1,h_2)$ läuft man von $\vec x_0$ aus eine **Treppe** entlang der
Gitterlinien — erst in $x_1$-, dann in $x_2$-Richtung. Weil $U$ offen ist, liegt die Treppe für kleine $\vec h$ in einer
Kugel um $\vec x_0$, die ganz in $U$ enthalten ist:

$$f(\vec x_0+\vec h)-f(\vec x_0) = \big[f(\vec x_0+h_1\vec e_1)-f(\vec x_0)\big] + \big[f(\vec x_0+h_1\vec e_1+h_2\vec e_2)-f(\vec x_0+h_1\vec e_1)\big].$$

Auf jeder Stufe ändert sich nur eine Variable. Der Mittelwertsatz aus HM1 liefert deshalb eine Zwischenstelle
$\vec\xi_1$ auf der ersten Stufe und eine Zwischenstelle $\vec\xi_2$ auf der zweiten:

$$f(\vec x_0+\vec h)-f(\vec x_0) = \frac{\partial f}{\partial x_1}(\vec\xi_1)\,h_1 + \frac{\partial f}{\partial x_2}(\vec\xi_2)\,h_2.$$

Für $\vec h\to\vec 0$ rücken beide Zwischenstellen an $\vec x_0$ heran. Weil die partiellen Ableitungen **stetig** sind,
gehen ihre Abweichungen von den Werten in $\vec x_0$ gegen null:

$$\rho_1 := \frac{\partial f}{\partial x_1}(\vec\xi_1)-\frac{\partial f}{\partial x_1}(\vec x_0) \;\to\; 0, \qquad \rho_2 := \frac{\partial f}{\partial x_2}(\vec\xi_2)-\frac{\partial f}{\partial x_2}(\vec x_0) \;\to\; 0.$$

Damit ist der Fehler der linearen Näherung klein gegen $\lvert\vec h\rvert$, denn $\lvert h_1\rvert$ und
$\lvert h_2\rvert$ sind höchstens $\lvert\vec h\rvert$:

$$f(\vec x_0+\vec h)-f(\vec x_0)-\nabla f(\vec x_0)\cdot\vec h = \rho_1h_1+\rho_2h_2, \qquad \frac{\lvert\rho_1h_1+\rho_2h_2\rvert}{\lvert\vec h\rvert}\le\lvert\rho_1\rvert+\lvert\rho_2\rvert\;\to\;0.$$

Das ist genau die Definition der totalen Differenzierbarkeit, mit der Zeile $Df(\vec x_0)$ als Matrix.

**Im Bild:** Auf jeder Treppenstufe zählt der Gitterpfeil an einer Zwischenstelle. Sind die Gitterpfeile stetig,
unterscheiden sich diese kaum von denen in $\vec x_0$. Ohne Stetigkeit können sie beliebig abweichen.
:::

**Probe am ersten Gegenbeispiel.** Beim ersten Gegenbeispiel muss also eine partielle Ableitung im Ursprung unstetig
sein. Außerhalb des Ursprungs liefert die Quotientenregel

$$\frac{\partial f}{\partial x}(x,y) = \frac{y\,(x^2+y^2)-xy\cdot2x}{(x^2+y^2)^2} = \frac{y\,(y^2-x^2)}{(x^2+y^2)^2}.$$

Auf der $y$-Achse ist das

$$\frac{\partial f}{\partial x}(0,y) = \frac{y^3}{y^4} = \frac1y \qquad (y\neq0).$$

Nahe am Ursprung wird dieser Gitterpfeil also beliebig groß, obwohl er im Ursprung selbst null ist. Er ist dort
unstetig, und der Satz greift nicht — kein Widerspruch.

## Der Satz von Schwarz

**Höhere Ableitungen.** Partielle Ableitungen kann man erneut partiell ableiten. Für die zweite Ableitung „zuerst nach
$x_k$, dann nach $x_j$" schreibt man

$$\frac{\partial^2 f}{\partial x_j\,\partial x_k} := \frac{\partial}{\partial x_j}\Big(\frac{\partial f}{\partial x_k}\Big).$$

Eine Abbildung heißt __$\ell$-mal stetig differenzierbar__, wenn alle partiellen Ableitungen bis zur Ordnung $\ell$
existieren und stetig sind. Die Menge dieser Abbildungen ist

$$C^\ell(U;\mathbb{R}^m) = \big\{\, \vec F:U\to\mathbb{R}^m \;\big|\; \vec F \text{ ist } \ell\text{-mal stetig differenzierbar} \,\big\};$$

für Skalarfelder schreibt man kurz $C^\ell(U)$. Im Skript heißt die Ordnung $k$; hier ist $k$ schon ein Index.

Bei zweiten Ableitungen stellt sich eine neue Frage: Spielt die Reihenfolge eine Rolle? Für $C^2$-Funktionen nicht —
das ist der __Satz von Schwarz__ (im Skript „Lemma von Schwarz"):

:::formel Satz
$$\frac{\partial^2 f}{\partial x_j\,\partial x_k} = \frac{\partial^2 f}{\partial x_k\,\partial x_j} \qquad \text{für } f\in C^2(U),\ U\subseteq\mathbb{R}^n \text{ offen}.$$
:::

Allgemein dürfen für $f\in C^\ell(U)$ alle partiellen Ableitungen bis zur Ordnung $\ell$ beliebig vertauscht werden:
Jede Umordnung entsteht durch wiederholtes Tauschen zweier benachbarter Ableitungen, und jeder solche Tausch ist der
Satz, angewandt auf eine Ableitung niedrigerer Ordnung, die noch zweimal stetig differenzierbar ist. Für Vektorfelder
gilt alles komponentenweise. Die nächsten Artikel brauchen diesen Satz ständig.

**Zahlenbeispiel.** Für das Skalarfeld

$$f(x,y) = x^2y^3$$

erhält man in beiden Reihenfolgen dasselbe:

$$\frac{\partial f}{\partial x} = 2xy^3,\quad \frac{\partial}{\partial y}\Big(\frac{\partial f}{\partial x}\Big) = 6xy^2; \qquad \frac{\partial f}{\partial y} = 3x^2y^2,\quad \frac{\partial}{\partial x}\Big(\frac{\partial f}{\partial y}\Big) = 6xy^2.$$

**Im Bild:** Man vergleicht die vier Ecken einer kleinen Gittermasche. Wie sich die Steigung in der einen
Gitterrichtung ändert, wenn man in der anderen weitergeht, ist dasselbe wie umgekehrt — beide messen dieselbe
**Verwindung** der Fläche über der Masche.

:::herleitung
Sei $j\neq k$. Man betrachtet die Funktionswerte an den vier Ecken einer kleinen quadratischen Gittermasche der
Seitenlänge $t>0$ in der $x_j$-$x_k$-Ebene; weil $U$ offen ist, liegt sie für kleine $t$ ganz in $U$. Daraus bildet man
die __Doppeldifferenz__

$$q(t) = f(\vec x+t\,\vec e_j+t\,\vec e_k) - f(\vec x+t\,\vec e_j) - f(\vec x+t\,\vec e_k) + f(\vec x).$$

Sie ist **symmetrisch** in $j$ und $k$: Vertauscht man die beiden Rollen, ändert sich nichts. **Im Bild:**
Gegenüberliegende Ecken tragen dasselbe Vorzeichen — $+$ an der Startecke und an der diagonal gegenüberliegenden, $-$
an den beiden anderen.

**Erste Reihenfolge.** Mit der Hilfsfunktion

$$w(s) = f(\vec x+s\,\vec e_j+t\,\vec e_k) - f(\vec x+s\,\vec e_j) \qquad (0\le s\le t)$$

ist die Doppeldifferenz gerade $w(t)-w(0)$. Der Mittelwertsatz liefert ein $\sigma$ zwischen $0$ und $t$ mit

$$q(t) = t\,w'(\sigma) = t\,\Big[\frac{\partial f}{\partial x_j}(\vec x+\sigma\,\vec e_j+t\,\vec e_k) - \frac{\partial f}{\partial x_j}(\vec x+\sigma\,\vec e_j)\Big].$$

Die Klammer ist wieder eine Differenz längs einer Gitterlinie, diesmal in $x_k$-Richtung. Ein zweiter Mittelwertsatz
ergibt ein $\tau$ zwischen $0$ und $t$. Mit der Zwischenstelle

$$\vec\xi = \vec x+\sigma\,\vec e_j+\tau\,\vec e_k$$

in der Masche ist dann

$$q(t) = t^2\,\frac{\partial}{\partial x_k}\Big(\frac{\partial f}{\partial x_j}\Big)(\vec\xi).$$

**Andere Reihenfolge.** Genauso, nur mit vertauschten Rollen von $j$ und $k$, erhält man eine Zwischenstelle
$\vec\eta$ in der Masche mit

$$q(t) = t^2\,\frac{\partial}{\partial x_j}\Big(\frac{\partial f}{\partial x_k}\Big)(\vec\eta).$$

**Grenzübergang.** Beide Darstellungen beschreiben dieselbe Zahl $q(t)$; nach Division durch $t^2$ sind also die beiden
gemischten Ableitungen an den Stellen $\vec\xi$ und $\vec\eta$ gleich. Für $t\to0$ rücken $\vec\xi$ und $\vec\eta$ an
$\vec x$ heran, und weil die zweiten Ableitungen **stetig** sind, stimmen beide gemischten Ableitungen im Punkt $\vec x$
überein.
:::

**Gegenbeispiel: Ohne Stetigkeit geht es schief.** Für die Funktion $\psi:\mathbb{R}^2\to\mathbb{R}$ mit

$$\psi(x,y) = \begin{cases} \dfrac{xy\,(x^2-y^2)}{x^2+y^2}, & (x,y)\neq(0,0),\\[2mm] 0, & (x,y)=(0,0) \end{cases}$$

existieren beide gemischten Ableitungen im Ursprung, sind aber verschieden:

$$\frac{\partial}{\partial y}\Big(\frac{\partial\psi}{\partial x}\Big)(0,0) = -1, \qquad \frac{\partial}{\partial x}\Big(\frac{\partial\psi}{\partial y}\Big)(0,0) = +1.$$

Ein Widerspruch zum Satz ist das nicht. Es zeigt nur, dass die zweiten Ableitungen von $\psi$ im Ursprung nicht stetig
sein können — sonst wären die beiden Werte nach dem Satz gleich.

:::herleitung
Zuerst die ersten Ableitungen auf den Achsen. Für festes $y$ ist der Differenzenquotient in $x$-Richtung am Punkt
$(0,y)$

$$\frac{\psi(t,y)-\psi(0,y)}{t} = \frac{y\,(t^2-y^2)}{t^2+y^2} \;\longrightarrow\; -y \qquad (t\to0).$$

Für $y\neq0$ darf man im Bruch einfach $t$ durch $0$ ersetzen; auf der $x$-Achse ist der Quotient ohnehin null. Ebenso
ist für festes $x$

$$\frac{\psi(x,t)-\psi(x,0)}{t} = \frac{x\,(x^2-t^2)}{x^2+t^2} \;\longrightarrow\; x \qquad (t\to0).$$

Die ersten Ableitungen auf den Achsen sind also

$$\frac{\partial\psi}{\partial x}(0,y) = -y, \qquad \frac{\partial\psi}{\partial y}(x,0) = x.$$

Leitet man diese ein zweites Mal ab, folgt

$$\frac{\partial}{\partial y}\Big(\frac{\partial\psi}{\partial x}\Big)(0,0) = \frac{d}{dy}(-y) = -1, \qquad \frac{\partial}{\partial x}\Big(\frac{\partial\psi}{\partial y}\Big)(0,0) = \frac{d}{dx}\,x = +1.$$

**Im Bild:** Für eine rechteckige Masche mit den Seiten $\alpha$ (in $x$-Richtung) und $\beta$ (in $y$-Richtung) an der
Ecke im Ursprung ist die Doppeldifferenz einfach $\psi(\alpha,\beta)$, weil $\psi$ auf beiden Achsen null ist. Die
gemessene Verwindung pro Maschenfläche hängt dann von der **Form** der Masche ab:

$$\frac{\psi(\alpha,\beta)}{\alpha\,\beta} = \frac{\alpha^2-\beta^2}{\alpha^2+\beta^2}.$$

Breite, flache Maschen ($\beta$ viel kleiner als $\alpha$) messen fast $+1$, schmale, hohe ($\alpha$ viel kleiner als
$\beta$) fast $-1$, Quadrate genau $0$. Die beiden gemischten Ableitungen sind genau diese beiden Grenzfälle: Wer zuerst
nach $x$ ableitet, lässt zuerst $\alpha$ gegen null gehen — schmale, hohe Maschen.
:::

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-schwarz-masche · Vorlage: gittermasche-vier-ecken-2d
Eine kleine Gittermasche über einer Fläche, die vier Ecken mit den Vorzeichen $+,-,-,+$ der Doppeldifferenz
beschriftet. Zwei Animationen laufen nebeneinander: links werden erst die Kanten in $x_j$-, dann in $x_k$-Richtung
verglichen, rechts umgekehrt — beide landen bei derselben Zahl. Ein zweiter Modus zeigt das Gegenbeispiel $\psi$: Ein
Regler ändert die Form der Masche am Ursprung von flach und breit über quadratisch zu schmal und hoch, die Anzeige
$\psi(\alpha,\beta)/(\alpha\beta)$ wandert von $+1$ über $0$ nach $-1$. Kernaussage: Bei stetigen zweiten Ableitungen
ist die Verwindung unabhängig von der Reihenfolge. (Orange = verglichene Kanten, rot = Doppeldifferenz, grau = Fläche.)
:::

## Die Kettenregel: zwei Lupen hintereinander

Der große Vorteil der Matrix-Schreibweise zeigt sich beim Verketten. Gegeben seien zwei Abbildungen

$$\vec G:U\to\mathbb{R}^m \ \ (U\subseteq\mathbb{R}^n \text{ offen}), \qquad \vec F:V\to\mathbb{R}^p \ \ (V\subseteq\mathbb{R}^m \text{ offen}), \qquad \vec G(U)\subseteq V.$$

Erst bildet $\vec G$ einen Punkt $\vec x\in U$ auf den Punkt $\vec G(\vec x)$ im Zwischenraum $\mathbb{R}^m$ ab, dann
$\vec F$ diesen weiter nach $\mathbb{R}^p$. Die Bedingung $\vec G(U)\subseteq V$ sorgt dafür, dass $\vec F$ dort auch
definiert ist. Die Koordinaten im Zwischenraum heißen $y_1,\ldots,y_m$.

Ist $\vec G$ in $\vec x$ und $\vec F$ im Bildpunkt $\vec G(\vec x)$ differenzierbar, so ist auch die Verkettung
$\vec F\circ\vec G$ in $\vec x$ differenzierbar. Ihre Ableitung ist — wie „äußere mal innere Ableitung" in HM1 — ein
**Matrizenprodukt**:

:::formel Satz
$$D(\vec F\circ\vec G)(\vec x) = D\vec F\big(\vec G(\vec x)\big)\,D\vec G(\vec x).$$
:::

**Dimensionen:** Links steht eine $p\times n$-Matrix. Rechts wird die $p\times m$-Matrix $D\vec F$ — ausgewertet am
Zwischenpunkt $\vec G(\vec x)$, nicht bei $\vec x$! — mit der $m\times n$-Matrix $D\vec G$ multipliziert. Das innere Maß
$m$ passt genau zusammen.

**Im Bild: zwei Gummitücher, zwei Lupen.** $\vec G$ verzerrt das erste Gitter, $\vec F$ verzerrt das Ergebnis ein
zweites Mal. Unter der Lupe macht $\vec G$ aus einer kleinen Masche ein Parallelogramm, beschrieben durch
$D\vec G(\vec x)$. Dieses kleine Parallelogramm liegt am Zwischenpunkt $\vec G(\vec x)$, und dort macht $\vec F$ daraus
wieder ein Parallelogramm, beschrieben durch $D\vec F(\vec G(\vec x))$. Zwei lineare Abbildungen hintereinander sind das
Matrixprodukt.

:::herleitung
Die Idee in einem Satz: **Die Linearisierung der Verkettung ist die Verkettung der Linearisierungen.**

Für einen kleinen Schritt $\vec h\in\mathbb{R}^n$ gilt nach Definition der Differenzierbarkeit

$$\vec G(\vec x+\vec h) = \vec G(\vec x) + D\vec G(\vec x)\,\vec h + \vec R_G(\vec h),$$

wobei der Rest $\vec R_G(\vec h)$ klein gegen $\lvert\vec h\rvert$ ist. Ebenso gilt mit dem Zwischenpunkt
$\vec y=\vec G(\vec x)$ für einen kleinen Schritt $\vec u\in\mathbb{R}^m$ im Zwischenraum

$$\vec F(\vec y+\vec u) = \vec F(\vec y) + D\vec F(\vec y)\,\vec u + \vec R_F(\vec u),$$

mit einem Rest $\vec R_F(\vec u)$, der klein gegen $\lvert\vec u\rvert$ ist. Jetzt setzt man für $\vec u$ genau den
Schritt ein, den $\vec G$ tatsächlich macht:

$$\vec u = \vec G(\vec x+\vec h)-\vec G(\vec x) = D\vec G(\vec x)\,\vec h + \vec R_G(\vec h).$$

Das ergibt

$$\vec F\big(\vec G(\vec x+\vec h)\big) = \vec F\big(\vec G(\vec x)\big) + D\vec F(\vec y)\,D\vec G(\vec x)\,\vec h + \underbrace{D\vec F(\vec y)\,\vec R_G(\vec h) + \vec R_F(\vec u)}_{\text{Rest}}.$$

**Der Rest ist klein gegen $\lvert\vec h\rvert$.** Für den ersten Teil folgt das aus der Matrix-Abschätzung im Abschnitt
über die Stetigkeit: $D\vec F(\vec y)$ vergrößert die kleine Länge $\lvert\vec R_G(\vec h)\rvert$ nur um einen festen
Faktor. Für den zweiten Teil ist der Schritt $\vec u$ höchstens proportional zu $\lvert\vec h\rvert$, mit dem festen
Faktor $c$ der Matrix $D\vec G(\vec x)$:

$$\lvert\vec u\rvert \le c\,\lvert\vec h\rvert + \lvert\vec R_G(\vec h)\rvert.$$

Also geht $\vec u$ mit $\vec h$ gegen null, und für $\vec u\neq\vec 0$ zerlegt man

$$\frac{\lvert\vec R_F(\vec u)\rvert}{\lvert\vec h\rvert} = \underbrace{\frac{\lvert\vec R_F(\vec u)\rvert}{\lvert\vec u\rvert}}_{\to\,0}\cdot\underbrace{\frac{\lvert\vec u\rvert}{\lvert\vec h\rvert}}_{\text{beschränkt}} \;\longrightarrow\; 0.$$

Ist $\vec u$ der Nullvektor, ist der Rest ohnehin null. Der lineare Anteil in $\vec h$ ist also das Produkt
$D\vec F(\vec y)\,D\vec G(\vec x)$ — und nach der Eindeutigkeit der Ableitung ist das $D(\vec F\circ\vec G)(\vec x)$.
:::

**Komponentenweise.** Der Eintrag in Zeile $i$, Spalte $k$ eines Matrixprodukts ist Zeile $i$ der ersten Matrix mal
Spalte $k$ der zweiten. Ausgeschrieben ist die Kettenregel deshalb eine Summe über alle Zwischenkoordinaten $y_j$ — so
steht sie im Skript:

$$\frac{\partial (\vec F\circ\vec G)_i}{\partial x_k}(\vec x) = \sum_{j=1}^{m} \frac{\partial F_i}{\partial y_j}\big(\vec G(\vec x)\big)\,\frac{\partial G_j}{\partial x_k}(\vec x).$$

Ist die äußere Abbildung ein Skalarfeld, fällt der Index $i$ einfach weg.

**Im Bild:** Jeder Summand ist ein **Umweg** von $x_k$ über eine Zwischenkoordinate $y_j$ zu $F_i$: wie stark $y_j$ auf
$x_k$ reagiert, mal wie stark $F_i$ auf $y_j$ reagiert. Die Gesamtwirkung ist die Summe aller Umwege.

**Zahlenbeispiel: erst Polarkoordinaten, dann Quadrieren.** Die Polarkoordinaten-Abbildung

$$\vec G:U\to\mathbb{R}^2, \qquad \vec G(r,\theta) = (r\cos\theta,\ r\sin\theta), \qquad U = (0,\infty)\times\mathbb{R}\subseteq\mathbb{R}^2,$$

bildet das Rechteckgitter der $(r,\theta)$-Ebene auf Kreise und Strahlen ab. Ihre Jacobi-Matrix ist

$$D\vec G(r,\theta) = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix}.$$

**Im Bild:** Der erste Gitterpfeil $(\cos\theta,\sin\theta)$ zeigt radial nach außen und hat die Länge $1$. Der zweite
zeigt tangential und hat die Länge $r$: Ein Winkelschritt bewegt den Punkt auf einem Kreis vom Radius $r$, also umso
weiter, je größer $r$ ist. Eine kleine Masche mit den Seiten $\Delta r$ und $\Delta\theta$ wird deshalb zu einem fast
rechteckigen Stück mit den Seiten $\Delta r$ und $r\,\Delta\theta$.

Danach quadrieren wir. Direkt ausgerechnet verdoppelt die Verkettung den Winkel und quadriert den Radius:

$$(\vec F\circ\vec G)(r,\theta) = \big(r^2\cos^2\theta-r^2\sin^2\theta,\ 2r^2\cos\theta\sin\theta\big) = \big(r^2\cos2\theta,\ r^2\sin2\theta\big).$$

Der zweite Schritt benutzt die Doppelwinkelformeln

$$\cos^2\theta-\sin^2\theta = \cos2\theta, \qquad 2\sin\theta\cos\theta = \sin2\theta.$$

Direkt abgeleitet ist die Jacobi-Matrix der Verkettung

$$D(\vec F\circ\vec G)(r,\theta) = \begin{pmatrix} 2r\cos2\theta & -2r^2\sin2\theta \\ 2r\sin2\theta & 2r^2\cos2\theta \end{pmatrix}.$$

Die Kettenregel liefert dasselbe als Produkt. Am Zwischenpunkt $\vec G(r,\theta)$ ist $D\vec F$ nach dem Quadrier-Beispiel
$2r$ mal die Drehung um $\theta$:

$$D\vec F\big(\vec G(r,\theta)\big)\,D\vec G(r,\theta) = 2r\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}\begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix} = 2r\begin{pmatrix} \cos2\theta & -r\sin2\theta \\ \sin2\theta & r\cos2\theta \end{pmatrix}.$$

Beim Ausmultiplizieren braucht man wieder nur die Doppelwinkelformeln, und das Ergebnis ist genau die direkt berechnete
Matrix.

**Im Bild:** Die erste Lupe macht aus der kleinen $(r,\theta)$-Masche ein Rechteck mit den Seiten $\Delta r$ (radial) und
$r\,\Delta\theta$ (tangential). Die zweite Lupe dreht es um $\theta$ und streckt es um $2r$. Danach zeigt die radiale
Seite in Richtung $2\theta$ — das Quadrieren verdoppelt den Winkel.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-kettenregel-polar · Vorlage: zwei-abbildungen-gitter-2d
Drei Ebenen nebeneinander: das Rechteckgitter der $(r,\theta)$-Ebene, sein Bild unter $\vec G$ (Kreise und Strahlen) und
dessen Bild unter dem Quadrieren $\vec F$ (Kreise mit quadriertem Radius, Strahlen mit verdoppeltem Winkel). Eine kleine
Masche wird durch beide Abbildungen verfolgt; zwei Lupen zeigen die Parallelogramme von $D\vec G$ und von $D\vec F$ am
Zwischenpunkt, eine dritte das Produkt. Kernaussage: Die Ableitung einer Verkettung ist das Produkt der beiden
Lupen-Matrizen. (Grau = Ausgangsgitter, blau = Zwischengitter, rot = Endgitter, orange = Parallelogramme.)
:::

## Ein Feld entlang einer Kurve

Der wichtigste Spezialfall der Kettenregel verkettet eine Kurve mit einem Skalarfeld. Die nächsten Artikel brauchen ihn
ständig — für Richtungsableitungen, Höhenlinien und Kurvenintegrale.

**Was ist eine Kurve?** Eine __Kurve__ ist eine Abbildung $\vec\gamma:I\to\mathbb{R}^n$ auf einem offenen Intervall
$I\subseteq\mathbb{R}$. Die Eingabe ist eine Zahl $t$, etwa die Zeit, die Ausgabe ein Ort $\vec\gamma(t)$. Ihre Ableitung
— der Punkt bedeutet die Ableitung nach $t$ — ist der __Geschwindigkeitsvektor__

$$\dot{\vec\gamma}(t) = \big(\dot\gamma_1(t),\ldots,\dot\gamma_n(t)\big)^{T}.$$

Er ist zugleich die Jacobi-Matrix der Kurve: eine Spalte mit $n$ Einträgen, weil es nur eine Eingabe-Koordinate gibt.
**Im Bild:** ein Wanderer, der zur Zeit $t$ am Ort $\vec\gamma(t)$ ist; $\dot{\vec\gamma}(t)$ zeigt, wohin und wie schnell
er gerade läuft.

Sei nun $\vec\gamma:I\to U$ eine differenzierbare Kurve in der offenen Menge $U\subseteq\mathbb{R}^n$ und
$f:U\to\mathbb{R}$ ein differenzierbares Skalarfeld. Dann ist $t\mapsto f(\vec\gamma(t))$ eine Funktion **einer**
Variablen — im Bild die Temperatur, die der Wanderer gerade spürt. Die Kettenregel liefert ihre Ableitung:

:::formel
$$\frac{d}{dt}\,f(\vec\gamma(t)) = Df(\vec\gamma(t))\,\dot{\vec\gamma}(t) = \nabla f(\vec\gamma(t))\cdot\dot{\vec\gamma}(t).$$
:::

Hier ist $Df$ eine $1\times n$-Zeile und $\dot{\vec\gamma}$ eine $n\times1$-Spalte. Ihr Produkt ist eine Zahl — das
**Skalarprodukt** aus Gradient und Geschwindigkeit.

:::herleitung
Die Kurve spielt die Rolle der inneren Abbildung $\vec G$ — mit nur einer Eingabe-Koordinate $t$ —, das Skalarfeld die
der äußeren mit nur einer Ausgabe-Komponente. Die komponentenweise Kettenregel besteht dann aus einer einzigen Summe:

$$\frac{d}{dt}\,f(\vec\gamma(t)) = \sum_{j=1}^n\frac{\partial f}{\partial x_j}(\vec\gamma(t))\,\dot\gamma_j(t).$$

Das ist genau das Skalarprodukt von $\nabla f(\vec\gamma(t))$ mit $\dot{\vec\gamma}(t)$. **Im Bild:** Jeder Summand ist ein
Umweg — wie schnell sich die $j$-te Koordinate des Wanderers ändert, mal wie stark die Temperatur auf diese Koordinate
reagiert.
:::

**Zahlenbeispiel.** Wir nehmen auf $\mathbb{R}^2$ ein Skalarfeld und eine Kurve:

$$f(x,y) = xy, \qquad \vec\gamma(t) = (t,\,t^2).$$

Direkt eingesetzt ergibt sich

$$f(\vec\gamma(t)) = t\cdot t^2 = t^3, \qquad \frac{d}{dt}\,f(\vec\gamma(t)) = 3t^2.$$

Über die Kettenregel braucht man den Gradienten am Kurvenpunkt und die Geschwindigkeit:

$$\nabla f(x,y) = (y,\,x), \qquad \nabla f(\vec\gamma(t)) = (t^2,\,t), \qquad \dot{\vec\gamma}(t) = (1,\,2t).$$

Ihr Skalarprodukt bestätigt das Ergebnis:

$$\nabla f(\vec\gamma(t))\cdot\dot{\vec\gamma}(t) = t^2\cdot1 + t\cdot2t = 3t^2.$$

**Im Bild:** Wie schnell sich die gespürte Temperatur ändert, hängt davon ab, wie gut Gradient und Laufrichtung
zusammenpassen. Läuft der Wanderer senkrecht zum Gradienten, ist das Skalarprodukt null, und die Temperatur bleibt
gleich — so entstehen die Höhenlinien des nächsten Artikels.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/01-gradient-kurve · Vorlage: skalarfeld-kurve-2d
Ein Wanderer läuft auf der Kurve $\vec\gamma(t)=(t,t^2)$ durch die farbige Temperaturkarte $f=xy$; an seinem Ort sind der
Geschwindigkeitsvektor $\dot{\vec\gamma}$ und der Gradient $\nabla f$ eingezeichnet, dazu der Winkel zwischen ihnen. Ein
Zeitstrahl darunter zeigt die gespürte Temperatur $f(\vec\gamma(t))=t^3$ und ihre Änderungsrate
$\nabla f\cdot\dot{\vec\gamma}=3t^2$. Kernaussage: Die Änderung längs der Kurve ist das Skalarprodukt aus Gradient und
Geschwindigkeit — maximal in Gradientenrichtung, null senkrecht dazu. (Rot = Kurve, orange = Gradient, blau =
Geschwindigkeit, grau = Höhenlinien.)
:::

## Bedeutung und Ausblick

Die Jacobi-Matrix ist das mehrdimensionale Gegenstück zur Ableitung: Sie ist das, was die Lupe zeigt — die lineare
Abbildung, die ein Feld nahe einem Punkt ersetzt. Auf dieser Linearisierung bauen alle Werkzeuge der Vektoranalysis auf,
und in der Elektrotechnik steckt sie hinter jedem Feld, ob elektrisches Feld, Strömung oder Temperatur.

In Kapitel 4 kehrt sie als __Jacobi-Determinante__ $\det D\vec F$ zurück. Unter der Lupe ist ihr Betrag der Faktor, um den
sich der **Flächeninhalt** einer kleinen Masche ändert — die Fläche eines Parallelogramms ist der Betrag der Determinante
seiner Kantenvektoren (lineare Algebra). Beim Quadrieren und bei den Polarkoordinaten ist sie

$$\det D\vec F(\vec x) = 4x_1^2+4x_2^2 = 4\lvert\vec x\rvert^2, \qquad \det D\vec G(r,\theta) = r\cos^2\theta+r\sin^2\theta = r.$$

Beim Quadrieren passt das zur Streckung um $2\lvert\vec x\rvert$ in beide Richtungen. Bei den Polarkoordinaten ist $r$
genau das Verhältnis der Flächen $\Delta r\cdot r\,\Delta\theta$ und $\Delta r\,\Delta\theta$ — der berühmte Faktor $r$
beim Integrieren in Polarkoordinaten.

Der Spezialfall des Skalarfelds hat uns schon den __Gradienten__ geliefert. Er zeigt in die Richtung des steilsten
Anstiegs und erzeugt aus einem Potential ein Vektorfeld. Seine Geometrie und die Klasse der __Gradientenfelder__ — samt
der Symmetrie ihrer Jacobi-Matrix, die aus dem Satz von Schwarz folgt — sind das Thema des nächsten Artikels.

:::kern
- __Felder__ sind Abbildungen $\vec F:U\to\mathbb{R}^m$ auf offenen Mengen $U\subseteq\mathbb{R}^n$: __Skalarfeld__ $f$ ($m=1$, Zahl pro Punkt), __Vektorfeld__ ($m=n$, Pfeil pro Punkt).
- __Offen__: Um jeden Punkt liegt noch eine kleine Kugel in $U$ — Platz für Differenzenquotienten in jede Richtung.
- Die __partielle Ableitung__ $\partial F_j/\partial x_k$ ist die HM1-Ableitung längs der $k$-ten Gitterlinie; der Vektor $\partial\vec F/\partial x_k$ ist der Tangentenpfeil an die verbogene Gitterlinie (**Gitterpfeil**).
- Die __Jacobi-Matrix__ $D\vec F=(\partial F_j/\partial x_k)_{jk}\in\mathbb{R}^{m\times n}$: Spalten sind die Gitterpfeile, Zeilen die transponierten Gradienten der Komponenten.
- Lineare Näherung unter der Lupe: $\vec F(\vec x_0+\vec h)\approx\vec F(\vec x_0)+D\vec F(\vec x_0)\,\vec h$.
- Für ein Skalarfeld ist $Df$ eine Zeile und der __Gradient__ $\nabla f=(Df)^T$ die zugehörige Spalte.
- __Total differenzierbar__: Der Fehler der linearen Näherung ist klein gegen den Abstand — unter der Lupe verschwindet er (beim Quadrieren ist er genau $|\vec h|^2$).
- Dann ist die Matrix eindeutig die Jacobi-Matrix, und $\vec F$ ist stetig.
- Partielle Ableitungen allein genügen **nicht** (Gegenbeispiel $\tfrac{xy}{x^2+y^2}$: unter jeder Lupe dasselbe Bild); **stetige** partielle Ableitungen ($C^1$) genügen.
- __Satz von Schwarz__: Für $f\in C^2(U)$ ist die Reihenfolge gemischter zweiter Ableitungen egal — ohne Stetigkeit nicht (Gegenbeispiel $\psi$).
- __Kettenregel__: $D(\vec F\circ\vec G)(\vec x)=D\vec F(\vec G(\vec x))\,D\vec G(\vec x)$ — zwei Lupen hintereinander.
- Längs einer Kurve: $\tfrac{d}{dt}f(\vec\gamma(t))=\nabla f(\vec\gamma(t))\cdot\dot{\vec\gamma}(t)$; null, wenn man senkrecht zum Gradienten läuft.
:::

:::quiz
F: Warum ist die Ableitung einer Abbildung $\vec F:\mathbb{R}^n\to\mathbb{R}^m$ eine Matrix — im Bild des Gitters unter der Lupe?
A: Unter einer starken Lupe werden die verbogenen Gitterlinien gerade und gleichabständig, aus den Maschen werden lauter gleiche Parallelogramme. Eine solche Abbildung ist (vom verschobenen Mittelpunkt abgesehen) linear, und eine lineare Abbildung von $\mathbb{R}^n$ nach $\mathbb{R}^m$ ist eine $m\times n$-Matrix — die Jacobi-Matrix mit allen $m\cdot n$ partiellen Ableitungen.
F: Was bedeutet die $k$-te Spalte der Jacobi-Matrix geometrisch, und warum ergibt „Matrix mal Schritt" die lineare Näherung?
A: Sie ist der $k$-te Gitterpfeil $\partial\vec F/\partial x_k$, der Tangentenpfeil an die Bildkurve der $k$-ten Gitterlinie. Eine Matrix schickt $\vec e_k$ auf ihre $k$-te Spalte. Ein Schritt $\vec h=\sum_k h_k\vec e_k$ geht deshalb auf dieselbe Kombination der Gitterpfeile, und die ist $D\vec F(\vec x_0)\,\vec h$.
F: Was macht die Jacobi-Matrix des Quadrierens $\vec F(x_1,x_2)=(x_1^2-x_2^2,\,2x_1x_2)$ mit einer kleinen Masche?
A: In Polarkoordinaten ist $D\vec F(\vec x)$ gleich $2r$ mal die Drehmatrix zum Winkel $\theta$. Jede kleine Masche wird um den Polarwinkel ihres Punktes gedreht, um $2r$ gestreckt und bleibt ein Quadrat — bei $(1,0)$ nur gestreckt (Faktor 2), bei $(0,1)$ zusätzlich um $90^\circ$ gedreht.
F: Gradient und Jacobi-Matrix eines Skalarfelds enthalten dieselben Zahlen — worin unterscheiden sie sich?
A: In Form und Rolle: $Df$ ist eine Zeile und wird als lineare Abbildung benutzt; von links an einen Schritt $\vec h$ multipliziert, liefert sie die Höhenänderung. Der Gradient $\nabla f=(Df)^T$ ist eine Spalte, ein Vektor im Raum der Punkte, und wird als Pfeil gedeutet — als Richtung des steilsten Anstiegs.
F: Was drückt der Quotient in der Definition der totalen Differenzierbarkeit im Bild der Lupe aus — und wie groß ist er beim Quadrieren?
A: Vergrößert man so stark, dass der Abstand $|\vec x-\vec x_0|$ die Länge 1 hat, wird der Fehler der linearen Näherung um denselben Faktor vergrößert. Der Quotient ist also der Fehler, wie man ihn unter der Lupe sieht, und er muss gegen null gehen. Beim Quadrieren ist der Fehler genau $\vec F(\vec h)$ mit der Länge $|\vec h|^2$, der Quotient also $|\vec h|$.
F: Warum ist die Matrix $A$ aus der Definition automatisch die Jacobi-Matrix, und warum ist eine differenzierbare Abbildung stetig?
A: Nähert man sich entlang der $k$-ten Gitterlinie, wird die Definition zu „Differenzenquotient nach $x_k$ minus $A\vec e_k$ geht gegen null" — die $k$-te Spalte von $A$ ist die partielle Ableitung. Stetig ist $\vec F$, weil der lineare Anteil gegen null geht (eine Matrix vergrößert Längen höchstens um einen festen Faktor) und der Fehler ohnehin.
F: Warum ist $f=\frac{xy}{x^2+y^2}$ (mit $f(0,0)=0$) im Ursprung nicht differenzierbar, obwohl beide partiellen Ableitungen existieren — und was zeigt die Lupe?
A: Auf den Achsen ist $f$ null, also sind beide partiellen Ableitungen im Ursprung null. Auf der Diagonale ist $f$ aber konstant $\tfrac12$, also ist $f$ dort nicht einmal stetig. Wegen $f(\lambda x,\lambda y)=f(x,y)$ zeigt jede noch so starke Lupe dasselbe Bild mit Grat und Rinne — eine schiefe Ebene erscheint nie.
F: Warum reichen stetige partielle Ableitungen für die totale Differenzierbarkeit?
A: Man läuft den Schritt $\vec h$ als Treppe entlang der Gitterlinien und wendet auf jeder Stufe den Mittelwertsatz an; dabei zählen die Gitterpfeile an Zwischenstellen. Sind sie stetig, weichen sie für $\vec h\to\vec 0$ immer weniger von denen in $\vec x_0$ ab, und der Fehler wird klein gegen $|\vec h|$. Beim ersten Gegenbeispiel ist $\partial f/\partial x(0,y)=1/y$ nahe dem Ursprung unbeschränkt — dort fehlt die Stetigkeit.
F: Wie beweist man den Satz von Schwarz an einer Gittermasche, und was zeigt das Gegenbeispiel $\psi$?
A: Die Doppeldifferenz der vier Maschenecken ist symmetrisch in den beiden Richtungen. Zweimal Mittelwertsatz schreibt sie in beiden Reihenfolgen als $t^2$ mal eine gemischte Ableitung an einer Zwischenstelle; mit stetigen zweiten Ableitungen folgt für $t\to0$ die Gleichheit. Bei $\psi$ hängt die gemessene Verwindung von der Form der Masche ab (flach fast $+1$, hoch fast $-1$); die gemischten Ableitungen im Ursprung sind $-1$ und $+1$, also sind die zweiten Ableitungen dort unstetig.
F: Warum ist die Kettenregel ein Matrixprodukt, und was ergibt sie für ein Skalarfeld längs einer Kurve?
A: Die Linearisierung der Verkettung ist die Verkettung der Linearisierungen: Unter zwei Lupen hintereinander macht erst $D\vec G(\vec x)$, dann $D\vec F$ am Zwischenpunkt $\vec G(\vec x)$ aus der Masche ein Parallelogramm, und hintereinander ausgeführte lineare Abbildungen multiplizieren ihre Matrizen. Für $f\circ\vec\gamma$ entsteht $\frac{d}{dt}f(\vec\gamma(t))=\nabla f(\vec\gamma(t))\cdot\dot{\vec\gamma}(t)$; bei $f=xy$ und $\vec\gamma=(t,t^2)$ kommt $3t^2$ heraus.
:::
