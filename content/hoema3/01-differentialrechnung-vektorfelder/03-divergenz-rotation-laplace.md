---
title: Divergenz, Rotation und Laplace-Operator
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010300
summary: Von Grund auf – zwei Messgeräte in einer Strömung. Ein winziges Kästchen zählt den Netto-Ausfluss (Divergenz $\operatorname{div}\vec E=\nabla\cdot\vec E$, Quelldichte), ein winziges Schaufelrad die Zirkulation (Rotation $\operatorname{rot}\vec E=\nabla\times\vec E$, Wirbeldichte); in den Steigungspfeilen einer Landschaft zeigt das Kästchen den Laplace-Operator $\Delta=\operatorname{div}\operatorname{grad}$ – Mulde oder Kuppe. Mit radialer Divergenzformel, harmonischen Funktionen, Rotation in der Ebene, der Drehmatrix $\Omega$, $\operatorname{rot}\operatorname{grad}\phi=\vec 0$ und einer Beispiel-Seite.
tags: Divergenz, Rotation, curl, Laplace-Operator, Quelldichte, Wirbeldichte, harmonische Funktion, Nabla, rotationsfrei
---

## Anschaulich

Der Gradient hat aus einer Landschaft ein Pfeilfeld gemacht. Jetzt geht es um die umgekehrte Frage: Was kann man einem
**Pfeilfeld** selbst ansehen?

Das Leitbild dieses Artikels ist eine **Wasserströmung**: An jedem Ort hat das Wasser eine Geschwindigkeit — ein
Vektorfeld $\vec E$. In diese Strömung halten wir zwei winzige Messgeräte.

- Ein durchsichtiges **Kästchen**. Es zählt, wie viel Wasser netto herausströmt. Strömt mehr heraus als hinein, sitzt
  im Kästchen eine Quelle; strömt mehr hinein, eine Senke. Diese Kennzahl ist die __Divergenz__, eine __Quelldichte__.
- Ein kleines **Schaufelrad**. Es dreht sich, wenn die Strömung um den Punkt wirbelt — wie Wasser um einen Abfluss.
  Seine Drehachse und Drehstärke liefern die __Rotation__, eine __Wirbeldichte__.

Hält man das Kästchen in die Steigungspfeile einer Landschaft, entsteht ein dritter Operator, der
__Laplace-Operator__. Er sagt, ob ein Punkt in einer **Mulde** liegt oder auf einer **Kuppe** — tiefer oder höher als
seine Umgebung im Mittel.

Alle drei entstehen formal aus einem Symbol, dem Nabla-Operator $\nabla$. Aus ihnen bauen sich die großen
Integralsätze (Gauß, Stokes) und die Feldgleichungen der Physik (Maxwell, Wärmeleitung, Poisson) auf.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/03-nabla-operatoren · Vorlage: operatoren-uebersicht-2d
Eine Wasserströmung als Pfeilfeld mit zwei Messgeräten: an einer Stelle ein durchsichtiges Kästchen, an dessen Wänden
Zu- und Abfluss als Balken angezeigt werden (Netto-Ausfluss = Divergenz), an einer anderen ein Schaufelrad, das sich je
nach Wirbel schneller oder langsamer dreht (Rotation). In der Mitte das Nabla-Symbol mit den drei Operatoren Gradient
(Skalar → Vektor), Divergenz (Vektor → Skalar) und Rotation (Vektor → Vektor). Kernaussage: Kästchen und Schaufelrad
lesen aus einem Pfeilfeld zwei lokale Kennzahlen ab. (Blau = Strömung, orange = Messgeräte, grau = Gitter.)
:::

## Die Divergenz: das Kästchen

Sei $U\subseteq\mathbb{R}^n$ offen und $\vec E:U\to\mathbb{R}^n$ ein differenzierbares Vektorfeld mit den Komponenten
$E_1,\ldots,E_n$ — die Strömung. Die __Divergenz__ ist die Summe der „diagonalen" partiellen Ableitungen:

:::formel Definition
$$\operatorname{div}\vec E := \nabla\cdot\vec E = \sum_{j=1}^{n}\frac{\partial E_j}{\partial x_j}.$$
:::

**So liest man das:** Die Eingabe ist ein Vektorfeld, die Ausgabe eine Zahl pro Punkt, also ein Skalarfeld. Jede
Komponente $E_j$ wird nach *ihrer eigenen* Koordinate $x_j$ abgeleitet, und diese $n$ Zahlen werden addiert. Die
Schreibweise $\nabla\cdot\vec E$ ist ein formales Skalarprodukt: „$\partial/\partial x_j$ mal $E_j$", aufsummiert. In
der Jacobi-Matrix $D\vec E$ sind das genau die Diagonaleinträge — die Divergenz ist ihre __Spur__, die Summe der
Diagonale.

**Die zwei Akteure:** die Strömung $\vec E$ und ein winziges Kästchen um einen Punkt $\vec x_0\in U$.
**Das Zusammenspiel:** *Wie viel Wasser strömt netto durch die Wände des Kästchens hinaus?*

**Im Bild:** In der Ebene sei das Kästchen ein Quadrat der kleinen Seitenlänge $h$ mit Mittelpunkt $\vec x_0$. Was
netto hinausströmt, ist ungefähr die Divergenz mal Fläche:

$$\text{Netto-Ausfluss} \;\approx\; \operatorname{div}\vec E(\vec x_0)\cdot h^2.$$

Die Divergenz ist also der Netto-Ausfluss **pro Fläche** — im Raum pro Volumen —, eine Dichte von Quellen.

:::herleitung
Durch eine kurze Wand strömt pro Zeit ungefähr so viel Wasser, wie die Geschwindigkeitskomponente senkrecht zur Wand
mal Wandlänge angibt. Für die rechte Wand (Richtung nach außen $\vec e_1$) und die linke Wand (nach außen $-\vec e_1$)
zusammen ist das

$$h\,E_1\big(\vec x_0+\tfrac h2\vec e_1\big) - h\,E_1\big(\vec x_0-\tfrac h2\vec e_1\big) \;\approx\; h\cdot h\,\frac{\partial E_1}{\partial x_1}(\vec x_0).$$

Denn zwei Werte im Abstand $h$ längs einer Gitterlinie unterscheiden sich ungefähr um $h$ mal die Ableitung — das ist
die lineare Näherung aus dem ersten Artikel. Ober- und Unterwand liefern ebenso $h^2\,\partial E_2/\partial x_2$.
Zusammen:

$$\text{Netto-Ausfluss} \;\approx\; h^2\Big(\frac{\partial E_1}{\partial x_1}+\frac{\partial E_2}{\partial x_2}\Big)(\vec x_0) = h^2\,\operatorname{div}\vec E(\vec x_0).$$

**Im Bild:** Nur die **Änderung** der Strömung quer durch das Kästchen zählt. Eine gleichmäßige Strömung trägt links so
viel hinein, wie sie rechts hinausträgt. Fließt rechts mehr hinaus, als links hereinkommt, bleibt netto ein Ausfluss.
Exakt wird diese Rechnung im Gaußschen Integralsatz.
:::

Danach unterscheidet man drei Fälle:

- $\operatorname{div}\vec E>0$ — eine **Quelle**: netto strömt mehr heraus als hinein.
- $\operatorname{div}\vec E<0$ — eine **Senke**: netto strömt mehr hinein, dort verschwindet Wasser.
- $\operatorname{div}\vec E=0$ — __quellenfrei__: genauso viel hinein wie heraus.

::::beispiel Ein Kästchen in drei Strömungen
**(a) Quelle.** Die Strömung $\vec E:\mathbb{R}^2\to\mathbb{R}^2$ mit

$$\vec E(x,y) = (x,\ y)$$

läuft überall vom Ursprung weg. Ihre Divergenz ist überall positiv:

$$\operatorname{div}\vec E = \frac{\partial x}{\partial x}+\frac{\partial y}{\partial y} = 2.$$

Für das Kästchen $[-1,1]^2\subseteq\mathbb{R}^2$ lässt sich das genau nachzählen. Auf jeder der vier Wände ist die
Geschwindigkeit nach außen gleich $1$, jede Wand ist $2$ lang:

$$\text{Netto-Ausfluss} = 4\cdot(1\cdot2) = 8 = \operatorname{div}\vec E\cdot\text{Fläche} = 2\cdot4.$$

Weil das Feld linear ist, stimmt die Näherung hier sogar exakt.

**(b) Senke.** Für die Strömung

$$\vec E(x,y) = (-x,\ 0)$$

ist die Divergenz $-1$. Das Wasser strömt von beiden Seiten auf die $y$-Achse zu; durch die rechte und die linke Wand
des Kästchens kommt je $2$ herein, durch Ober- und Unterwand fließt nichts:

$$\text{Netto-Ausfluss} = -2-2 = -4 = (-1)\cdot4.$$

**(c) Quellenfrei.** Für das kreisende Feld

$$\vec E(x,y) = (-y,\ x)$$

ist die Divergenz $0+0=0$. Durch die rechte Wand etwa fließt oben Wasser hinein und unten genauso viel hinaus:

$$\int_{-1}^{1}E_1(1,y)\,dy = \int_{-1}^{1}(-y)\,dy = 0.$$

**Im Bild:** Bei (a) quillt Wasser aus jedem Punkt, bei (b) wird es überall abgesaugt, bei (c) läuft es nur im Kreis.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/03-kaestchen-fluss · Vorlage: divergenz-kaestchen-zaehlen-2d
Das Kästchen $[-1,1]^2$ nacheinander in den drei Strömungen $(x,y)$, $(-x,0)$ und $(-y,x)$. An jeder Wand zeigt ein
Balken den Fluss nach außen (positiv) oder innen (negativ), daneben die Summe: $8$, $-4$, $0$. Kernaussage: Der
Netto-Ausfluss ist Divergenz mal Fläche. (Blau = Strömung, orange = Wandflüsse, rot = Summe, grau = Kästchen.)
:::
::::

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/03-divergenz-quelle-senke · Vorlage: divergenz-kaestchen-2d
Drei Strömungsausschnitte mit je einem kleinen Kästchen: Quelle (Pfeile auswärts, mehr Ausfluss), Senke (Pfeile
einwärts), quellenfrei (gleich viel hinein wie hinaus). Ein Regler verkleinert das Kästchen; der Netto-Ausfluss geteilt
durch die Fläche nähert sich der Divergenz im Mittelpunkt. Kernaussage: Divergenz ist Netto-Ausfluss pro Fläche.
(Blau = Strömung, orange = Netto-Fluss, grau = Kästchen.)
:::

**Die Produktregel.** Gewichtet man die Strömung mit einem differenzierbaren Skalarfeld $\phi:U\to\mathbb{R}$, so gilt

$$\operatorname{div}(\phi\,\vec E) = \nabla\phi\cdot\vec E + \phi\,\operatorname{div}\vec E.$$

**Im Bild:** Ist $\phi$ die Konzentration eines Farbstoffs, der mit dem Wasser mitschwimmt, so quillt der
Farbstofffluss $\phi\vec E$ aus zwei Gründen: weil das Wasser selbst quillt, oder weil die Konzentration in
Strömungsrichtung zunimmt. Der nächste Artikel nimmt dieses Bild ausführlich auseinander.

:::herleitung
Auf jeden Summanden der Divergenz wirkt die gewöhnliche Produktregel aus HM1:

$$\operatorname{div}(\phi\,\vec E) = \sum_j\frac{\partial(\phi E_j)}{\partial x_j} = \sum_j\frac{\partial\phi}{\partial x_j}\,E_j + \phi\sum_j\frac{\partial E_j}{\partial x_j} = \nabla\phi\cdot\vec E + \phi\,\operatorname{div}\vec E.$$
:::

::::beispiel Die Produktregel nachgerechnet
Mit dem Skalarfeld und der Strömung

$$\phi(x,y) = x^2, \qquad \vec E(x,y) = (y,\ x)$$

ist das gewichtete Feld und seine Divergenz direkt

$$\phi\,\vec E = (x^2y,\ x^3), \qquad \operatorname{div}(\phi\,\vec E) = 2xy+0 = 2xy.$$

Über die Produktregel kommt dasselbe heraus, denn $\vec E$ ist selbst quellenfrei:

$$\nabla\phi\cdot\vec E = (2x,\ 0)\cdot(y,\ x) = 2xy, \qquad \phi\,\operatorname{div}\vec E = x^2\cdot0 = 0.$$

**Im Bild:** Am Punkt $(1,1)$ quillt der Farbstofffluss mit der Stärke $2$, obwohl das Wasser selbst nicht quillt —
allein weil die Konzentration $x^2$ in Strömungsrichtung zunimmt.
::::

**Radialsymmetrische Felder.** Für ein radialsymmetrisches Feld auf $\mathbb{R}^n\setminus\{\vec 0\}$ — also
$s(r)\,\vec e_r$ mit einem differenzierbaren Feldprofil $s:(0,\infty)\to\mathbb{R}$ (voriger Artikel) — gibt es eine
kompakte Formel:

:::formel
$$\operatorname{div}\big(s(r)\,\vec e_r\big) = s'(r) + (n-1)\,\frac{s(r)}{r}.$$
:::

**Im Bild:** Der erste Term zählt, wie sich die Feldstärke längs des Radius ändert. Der zweite ist rein
**geometrisch**: Radiale Pfeile laufen auseinander, und die Kugelschale, die sie durchstoßen, wächst mit $r^{n-1}$.
Selbst ein überall gleich starkes Radialfeld verteilt sich deshalb nach außen auf immer mehr Fläche — es quillt.

:::herleitung
Man schreibt das Feld als Skalarfeld mal Ortsvektor und benutzt die Produktregel:

$$\vec E = \frac{s(r)}{r}\,\vec x, \qquad \operatorname{div}\vec E = \nabla\Big(\frac{s(r)}{r}\Big)\cdot\vec x + \frac{s(r)}{r}\,\operatorname{div}\vec x.$$

Drei Bausteine. Erstens ist die Divergenz des Ortsvektors die Zahl der Koordinaten, denn jede Komponente $x_j$ hat nach
$x_j$ die Ableitung $1$. Zweitens liefert die Gradientenformel aus dem vorigen Artikel mit dem Profil $s(r)/r$ und der
Quotientenregel einen radialen Pfeil. Drittens ist das Skalarprodukt von $\vec e_r$ mit $\vec x$ die Länge $r$:

$$\operatorname{div}\vec x = n, \qquad \nabla\Big(\frac{s(r)}{r}\Big) = \frac{s'(r)\,r-s(r)}{r^2}\,\vec e_r, \qquad \vec e_r\cdot\vec x = r.$$

Eingesetzt:

$$\operatorname{div}\vec E = \frac{s'(r)\,r-s(r)}{r} + n\,\frac{s(r)}{r} = s'(r) + (n-1)\,\frac{s(r)}{r}.$$
:::

::::beispiel Drei radiale Felder
**(a) Der Ortsvektor.** Der Ortsvektor ist selbst radial, denn $\vec x$ ist $r$ mal $\vec e_r$; sein Profil ist
$s(r)=r$. Die Formel gibt

$$\operatorname{div}\vec x = 1 + (n-1)\cdot\frac rr = n,$$

genau wie direkt nachgerechnet.

**(b) Das Coulomb-Profil im Raum.** Im $\mathbb{R}^3$ mit dem Profil $s(r)=1/r^2$ heben sich beide Terme auf:

$$s'(r) + 2\,\frac{s(r)}{r} = -\frac{2}{r^3}+\frac{2}{r^3} = 0.$$

**(c) Das Feld eines Drahts in der Ebene.** In der Ebene mit dem Profil $s(r)=1/r$ ebenso:

$$s'(r) + 1\cdot\frac{s(r)}{r} = -\frac{1}{r^2}+\frac{1}{r^2} = 0.$$

**Im Bild:** Fällt das Feld genau wie $1/r^{n-1}$ ab, dann geht durch jede Kugelschale um den Ursprung gleich viel
Fluss — die wachsende Fläche gleicht die sinkende Feldstärke exakt aus. Zwischen zwei Schalen entsteht nichts und
verschwindet nichts: Das Feld ist außerhalb des Ursprungs quellenfrei.
::::

## Der Laplace-Operator: Mulde oder Kuppe?

Sei $\phi:U\to\mathbb{R}$ zweimal differenzierbar — eine Landschaft. Der __Laplace-Operator__ summiert ihre zweiten
Ableitungen längs aller Achsen:

:::formel Definition
$$\Delta\phi := \sum_{j=1}^{n}\frac{\partial^2\phi}{\partial x_j^2}.$$
:::

**So liest man das:** Eingabe und Ausgabe sind Skalarfelder. Jede zweite Ableitung $\partial^2\phi/\partial x_j^2$ ist
die Krümmung der Landschaft längs der $j$-ten Gitterlinie; $\Delta$ addiert diese $n$ Krümmungen. Weil er zweite
Ableitungen enthält, ist er ein Differentialoperator **zweiter Ordnung**.

**Erst Gradient, dann Divergenz.** Die $j$-te Komponente von $\nabla\phi$ ist $\partial\phi/\partial x_j$; leitet man sie
nach $x_j$ ab und summiert, entsteht genau $\Delta\phi$:

$$\operatorname{div}(\nabla\phi) = \sum_{j=1}^n\frac{\partial}{\partial x_j}\Big(\frac{\partial\phi}{\partial x_j}\Big) = \Delta\phi, \qquad \text{formal}\quad \Delta = \nabla\cdot\nabla = \nabla^2.$$

Auf ein Vektorfeld wendet man $\Delta$ komponentenweise an:

$$\Delta\vec F = (\Delta F_1,\ldots,\Delta F_n)^T.$$

**Im Bild: Mulde oder Kuppe?** $\Delta\phi$ ist die Quelldichte der Steigungspfeile — das Kästchen, gehalten in das
Gradientenfeld der Landschaft. Liegt ein Punkt in einer **Mulde**, zeigen die Steigungspfeile ringsum von ihm weg den
Hang hinauf: Aus dem Kästchen strömt netto etwas heraus, $\Delta\phi>0$. Auf einer **Kuppe** zeigen sie alle zum Gipfel
hin: netto strömt etwas hinein, $\Delta\phi<0$.

**Genauer: das Mittel der Nachbarn.** Auf einem Gitter der Maschenweite $h$ hat der Punkt $\vec x_0$ die $2n$ Nachbarn
$\vec x_0\pm h\,\vec e_k$. Ihr Mittelwert liegt um ungefähr $\tfrac{h^2}{2n}\Delta\phi$ über dem Wert in der Mitte:

$$\frac{1}{2n}\sum_{k=1}^{n}\Big(\phi(\vec x_0+h\vec e_k)+\phi(\vec x_0-h\vec e_k)\Big) - \phi(\vec x_0) \;\approx\; \frac{h^2}{2n}\,\Delta\phi(\vec x_0).$$

:::herleitung
Längs jeder Gitterlinie ist $\phi$ eine Funktion einer Variablen. Die Taylor-Formel aus HM1 bis zur zweiten Ordnung gibt

$$\phi(\vec x_0\pm h\vec e_k) = \phi(\vec x_0) \pm h\,\frac{\partial\phi}{\partial x_k}(\vec x_0) + \frac{h^2}{2}\,\frac{\partial^2\phi}{\partial x_k^2}(\vec x_0) + \ldots$$

Die Punkte stehen für einen Rest, der schneller als $h^2$ klein wird. Addiert man die beiden Nachbarn auf derselben
Gitterlinie, fällt der Term erster Ordnung weg:

$$\phi(\vec x_0+h\vec e_k)+\phi(\vec x_0-h\vec e_k) = 2\phi(\vec x_0) + h^2\,\frac{\partial^2\phi}{\partial x_k^2}(\vec x_0) + \ldots$$

Summiert über alle $n$ Richtungen und durch die Anzahl $2n$ der Nachbarn geteilt, entsteht ihr Mittelwert:

$$\text{Mittel der Nachbarn} = \phi(\vec x_0) + \frac{h^2}{2n}\,\Delta\phi(\vec x_0) + \ldots$$

**Im Bild:** Die Steigung hebt sich weg, weil ein Nachbar so viel höher liegt, wie der gegenüberliegende tiefer liegt.
Übrig bleibt die Krümmung — und die entscheidet, ob die Nachbarn im Mittel höher liegen (Mulde) oder tiefer (Kuppe).
:::

::::beispiel Mulde und Sattel am Mittel der Nachbarn
**(a) Die Mulde.** Für das Skalarfeld

$$\phi(x,y) = x^2+y^2$$

ist überall

$$\Delta\phi = 2+2 = 4.$$

Am Punkt $(1,0)$ mit der Maschenweite $h=1$ haben die vier Nachbarn die Werte

$$\phi(2,0) = 4, \qquad \phi(0,0) = 0, \qquad \phi(1,1) = 2, \qquad \phi(1,-1) = 2.$$

Ihr Mittel ist $2$, der Wert in der Mitte $1$. Der Unterschied passt genau zur Formel:

$$2-1 = 1 = \frac{h^2}{2n}\,\Delta\phi = \frac14\cdot4.$$

**(b) Der Sattel.** Für

$$\phi(x,y) = x^2-y^2$$

ist $\Delta\phi=2-2=0$ — die Funktion ist harmonisch. Am selben Punkt haben die Nachbarn die Werte $4$, $0$, $0$ und $0$;
ihr Mittel ist $1$, genau der Wert in der Mitte.

**Im Bild:** Der Sattel ist in $x$-Richtung eine Mulde und in $y$-Richtung eine Kuppe. Beide Krümmungen sind gleich stark
und heben sich im Mittel genau auf. Bei quadratischen Funktionen ist die Näherung sogar exakt, weil die Taylor-Formel
nach dem zweiten Glied abbricht.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/03-laplace-nachbarn · Vorlage: gitter-nachbarn-mittel-2d
Ein Gitterpunkt mit seinen vier Nachbarn über einer Landschaft; die Nachbarhöhen werden als Säulen angezeigt, ihr
Mittelwert als gestrichelte Linie, der Mittelpunkt als rote Säule. Umschalter: Mulde $x^2+y^2$ (Mittel höher als die
Mitte, $\Delta>0$), Sattel $x^2-y^2$ (Mittel gleich der Mitte, $\Delta=0$), Kuppe $-x^2-y^2$ ($\Delta<0$). Kernaussage:
Der Laplace-Operator vergleicht einen Punkt mit dem Mittel seiner Nachbarn. (Rot = Mitte, orange = Nachbarn, grau =
Gitter, gestrichelt = Mittelwert.)
:::
::::

**Harmonische Funktionen.** Eine Funktion mit $\Delta\phi=0$ heißt __harmonisch__. **Im Bild:** Jeder Punkt liegt — bis
auf Terme höherer Ordnung — genau auf dem Mittel seiner Nachbarn, weder in einer Mulde noch auf einer Kuppe. Solche
Funktionen beschreiben **Gleichgewichte**: eine stationäre Temperaturverteilung, bei der Wärme ständig vom Warmen ins
Kalte fließt und sich doch nichts mehr ändert, oder das Potential im ladungsfreien Raum. Die exakte
Mittelwerteigenschaft über ganze Kugeln folgt später aus dem Gaußschen Integralsatz.

::::beispiel Das Coulomb-Potential ist harmonisch
Für das Potential einer Punktladung $Q$ im Ursprung,

$$u(\vec x) = \frac{Q}{4\pi r}, \qquad \vec x\in\mathbb{R}^3\setminus\{\vec 0\},$$

kennen wir aus dem vorigen Artikel den Gradienten, ein radiales Feld:

$$\nabla u = s(r)\,\vec e_r, \qquad s(r) = -\frac{Q}{4\pi r^2}.$$

Die radiale Divergenzformel mit $n=3$ gibt

$$\Delta u = \operatorname{div}(\nabla u) = s'(r)+2\,\frac{s(r)}{r} = \frac{2Q}{4\pi r^3}-\frac{2Q}{4\pi r^3} = 0.$$

**Im Bild:** Außerhalb der Ladung liegt das Potential überall genau auf dem Mittel seiner Umgebung — dort sitzt keine
Quelle. Im Ursprung sitzt die Ladung selbst; dort ist $u$ nicht definiert. Wie eine Ladungsdichte als Quelle in
$\Delta u$ eingeht, zeigt später die Poisson-Gleichung.

Ebenso ist in der Ebene der Logarithmus $\ln r$ aus dem vorigen Artikel harmonisch, denn sein Gradient $\vec e_r/r$ ist
das Drahtfeld aus den drei radialen Feldern — und das ist quellenfrei.
::::

## Die Rotation: das Schaufelrad

Sei $U\subseteq\mathbb{R}^3$ offen und $\vec E:U\to\mathbb{R}^3$ ein differenzierbares Vektorfeld mit den Komponenten
$E_1,E_2,E_3$. Die __Rotation__ (englisch __curl__) ist das formale Kreuzprodukt von $\nabla$ mit $\vec E$:

:::formel Definition
$$\operatorname{rot}\vec E := \nabla\times\vec E = \begin{pmatrix} \dfrac{\partial E_3}{\partial x_2} - \dfrac{\partial E_2}{\partial x_3} \\[2mm] \dfrac{\partial E_1}{\partial x_3} - \dfrac{\partial E_3}{\partial x_1} \\[2mm] \dfrac{\partial E_2}{\partial x_1} - \dfrac{\partial E_1}{\partial x_2} \end{pmatrix}.$$
:::

**So liest man das:** Eingabe und Ausgabe sind Vektorfelder. Jede Komponente ist eine Differenz zweier Ableitungen
„über Kreuz": Die $k$-te Komponente benutzt nur die beiden **anderen** Koordinatenrichtungen.

**Die zwei Akteure:** die Strömung $\vec E$ und ein winziges Schaufelrad am Punkt $\vec x_0$, dessen Achse in Richtung
$\vec e_3$ zeigt. **Das Zusammenspiel:** *Wie stark treibt die Strömung das Rad an?*

**Im Bild:** Das Rad spürt die __Zirkulation__ — die Strömung längs eines kleinen Quadrats um seine Achse, im
Drehsinn aufsummiert. Für ein Quadrat der Seitenlänge $h$ in der $x_1$-$x_2$-Ebene ist sie ungefähr die dritte Komponente
der Rotation mal Fläche:

$$\text{Zirkulation} \;\approx\; (\operatorname{rot}\vec E)_3(\vec x_0)\cdot h^2.$$

Jede Komponente der Rotation ist so die __Wirbeldichte__ um die jeweilige Koordinatenachse. Der ganze Vektor
$\operatorname{rot}\vec E$ zeigt in die Achsenrichtung, in der ein Rad am stärksten angetrieben würde.

:::herleitung
Man umläuft das Quadrat mit Mittelpunkt $\vec x_0$ gegen den Uhrzeigersinn, von der positiven $x_3$-Achse aus gesehen. Auf
jeder Seite zählt die Strömungskomponente in Laufrichtung mal Seitenlänge — unten in $+x_1$-, rechts in $+x_2$-, oben in
$-x_1$- und links in $-x_2$-Richtung:

$$h\,E_1\big(\vec x_0-\tfrac h2\vec e_2\big) + h\,E_2\big(\vec x_0+\tfrac h2\vec e_1\big) - h\,E_1\big(\vec x_0+\tfrac h2\vec e_2\big) - h\,E_2\big(\vec x_0-\tfrac h2\vec e_1\big).$$

Fasst man gegenüberliegende Seiten zusammen, gibt die lineare Näherung

$$\text{Zirkulation} \;\approx\; h^2\Big(\frac{\partial E_2}{\partial x_1}-\frac{\partial E_1}{\partial x_2}\Big)(\vec x_0) = h^2\,(\operatorname{rot}\vec E)_3(\vec x_0).$$

**Im Bild:** Das Rad dreht sich, wenn die Strömung auf gegenüberliegenden Seiten verschieden stark in Laufrichtung
schiebt — rechts stärker nach oben als links, oder unten stärker nach rechts als oben. Exakt wird das im Stokesschen
Integralsatz.
:::

::::beispiel Ein Schaufelrad in zwei Strömungen
**(a) Starre Drehung.** Die Strömung $\vec E:\mathbb{R}^3\to\mathbb{R}^3$ mit

$$\vec E(x,y,z) = (-y,\ x,\ 0)$$

dreht das Wasser wie eine Scheibe um die $z$-Achse, mit der Winkelgeschwindigkeit $1$: Im Abstand $\rho$ von der Achse
ist das Tempo $\rho$. Ihre Rotation zeigt längs der Drehachse:

$$\operatorname{rot}\vec E = \big(\partial_y0-\partial_z x,\ \ \partial_z(-y)-\partial_x0,\ \ \partial_x x-\partial_y(-y)\big) = (0,\ 0,\ 2).$$

**(b) Scherströmung.** Für die geradlinige Strömung

$$\vec E(x,y,z) = (y,\ 0,\ 0),$$

die oben schneller fließt als unten, ist

$$\operatorname{rot}\vec E = \big(0,\ \ \partial_z y,\ \ -\partial_y y\big) = (0,\ 0,\ -1).$$

**Im Bild:** Bei (a) dreht sich ein Rad mit senkrechter Achse gegen den Uhrzeigersinn — es schwimmt einfach mit der
sich drehenden Scheibe mit. Bei (b) dreht es sich im Uhrzeigersinn, obwohl das Wasser geradeaus fließt: Seine obere Hälfte
wird stärker angeschoben als die untere. Dass das Rad bei (a) mit der Winkelgeschwindigkeit $1$ läuft, also mit der
Hälfte von $\lvert\operatorname{rot}\vec E\rvert$, erklärt der Abschnitt über die Drehmatrix.
::::

**Kompakt mit dem Levi-Civita-Symbol.** Für Indizes $i,j,k\in\{1,2,3\}$ ist das __Levi-Civita-Symbol__ das
Spatprodukt der drei Einheitsvektoren:

$$\varepsilon_{ijk} := \vec e_i\cdot(\vec e_j\times\vec e_k) \in \{-1,\,0,\,1\}.$$

Es ist $+1$ für $(1,2,3)$ und alle zyklischen Vertauschungen, $-1$, wenn man zwei Indizes tauscht, und $0$, sobald zwei
Indizes gleich sind. Damit ist jede Komponente der Rotation eine einzige Summe:

$$(\operatorname{rot}\vec E)_i = \sum_{j,k=1}^{3}\varepsilon_{ijk}\,\frac{\partial E_k}{\partial x_j}.$$

:::herleitung
Die Werte des Symbols folgen aus dem Kreuzprodukt der Einheitsvektoren: $\vec e_2\times\vec e_3$ ist $\vec e_1$, also ist
$\varepsilon_{123}$ gleich $1$; ein Tausch dreht das Kreuzprodukt um, und zwei gleiche Vektoren haben das
Kreuzprodukt $\vec 0$. Für die erste Komponente der Rotation bleiben in der Summe nur zwei Terme:

$$(\operatorname{rot}\vec E)_1 = \varepsilon_{123}\,\frac{\partial E_3}{\partial x_2} + \varepsilon_{132}\,\frac{\partial E_2}{\partial x_3} = \frac{\partial E_3}{\partial x_2} - \frac{\partial E_2}{\partial x_3}.$$

Das ist die erste Komponente der Definition; die anderen folgen zyklisch. Der nächste Artikel arbeitet mit dieser
Schreibweise ausführlich.
:::

**Die Determinanten-Merkregel.** Formal kann man die Rotation als Determinante schreiben, wenn man in die erste Spalte
die Einheitsvektoren, in die zweite die Ableitungen und in die dritte die Komponenten setzt:

$$\operatorname{rot}\vec E = \det\begin{pmatrix} \vec e_1 & \partial/\partial x_1 & E_1 \\ \vec e_2 & \partial/\partial x_2 & E_2 \\ \vec e_3 & \partial/\partial x_3 & E_3 \end{pmatrix}.$$

:::herleitung
Man entwickelt nach der ersten Spalte; dabei steht die Ableitung immer links von der Komponente, auf die sie wirkt:

$$\vec e_1\Big(\frac{\partial E_3}{\partial x_2}-\frac{\partial E_2}{\partial x_3}\Big) - \vec e_2\Big(\frac{\partial E_3}{\partial x_1}-\frac{\partial E_1}{\partial x_3}\Big) + \vec e_3\Big(\frac{\partial E_2}{\partial x_1}-\frac{\partial E_1}{\partial x_2}\Big).$$

Der mittlere Term mit seinem Minuszeichen ist genau die zweite Komponente der Definition. Eine echte Determinante ist das
nicht — die Einträge sind Vektoren, Operatoren und Funktionen —, aber eine verlässliche Gedächtnisstütze.
:::

**Stolperstein:** Die dreikomponentige Rotation gibt es nur im $\mathbb{R}^3$, denn das Kreuzprodukt ist eine
Besonderheit von drei Dimensionen. In der Ebene gibt es eine skalare Version, und in jeder Dimension die Drehmatrix des
letzten Abschnitts. Die Divergenz dagegen ist in jeder Dimension definiert.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/03-rotation-3d · Vorlage: wirbelfeld-schaufelrad-3d
Ein wirbelndes 3D-Strömungsfeld; an einem Punkt ein kleines Schaufelrad, dessen Achse sich frei ausrichten lässt. Ein
Zähler zeigt die Zirkulation um die Achse; sie ist am größten, wenn die Achse parallel zu $\operatorname{rot}\vec E$
steht, und null, wenn sie senkrecht dazu steht. Daneben die Determinanten-Merkregel. Kernaussage: Die Rotation ist die
Achse, um die die Strömung am stärksten wirbelt. (Blau = Strömung, orange = Schaufelrad, rot = Rotationsvektor.)
:::

## Die Rotation in der Ebene

Ein ebenes Feld $(E_1,E_2,0)$, das nicht von $x_3$ abhängt, hat als räumliche Rotation nur eine dritte Komponente:

$$\operatorname{rot}\begin{pmatrix} E_1 \\ E_2 \\ 0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \dfrac{\partial E_2}{\partial x_1} - \dfrac{\partial E_1}{\partial x_2} \end{pmatrix}.$$

Denn in den ersten beiden Komponenten stehen nur Ableitungen nach $x_3$ und Ableitungen der dritten Komponente, und die
sind alle null. Das motiviert für ein differenzierbares Feld $\vec E=(E_1,E_2)^T$ auf $U\subseteq\mathbb{R}^2$ die
__Rotation in 2D__ als **Zahl**:

:::formel Definition
$$\operatorname{rot}\vec E := \frac{\partial E_2}{\partial x_1} - \frac{\partial E_1}{\partial x_2}.$$
:::

**Im Bild:** Ein Schaufelrad, dessen Achse senkrecht aus der Ebene herausragt. Ist die Rotation positiv, dreht es sich
gegen den Uhrzeigersinn, ist sie negativ, im Uhrzeigersinn.

**Quelle und Wirbel sind dasselbe, um $90^\circ$ gedreht.** In der Ebene sind Divergenz und Rotation beide Zahlen, und
eine Vierteldrehung verwandelt die eine in die andere. Mit dem um $90^\circ$ gegen den Uhrzeigersinn gedrehten Feld

$$\vec F^{\perp} := (-F_2,\ F_1)$$

gilt für jedes differenzierbare ebene Feld $\vec F$:

:::formel Lemma
$$\operatorname{div}\vec F = \operatorname{rot}\vec F^{\perp}, \qquad \operatorname{div}\vec F^{\perp} = -\operatorname{rot}\vec F.$$
:::

**Im Bild:** Dreht man jeden Pfeil um $90^\circ$, wird aus einer Strömung, die radial auseinanderläuft, eine, die um das
Zentrum kreist: Das Kästchen der Quelle wird zum Schaufelrad des Wirbels.

:::herleitung
Man setzt die Komponenten des gedrehten Feldes in die Definitionen ein:

$$\operatorname{rot}\vec F^{\perp} = \frac{\partial F_1}{\partial x_1} - \frac{\partial(-F_2)}{\partial x_2} = \frac{\partial F_1}{\partial x_1}+\frac{\partial F_2}{\partial x_2} = \operatorname{div}\vec F,$$

$$\operatorname{div}\vec F^{\perp} = \frac{\partial(-F_2)}{\partial x_1} + \frac{\partial F_1}{\partial x_2} = -\Big(\frac{\partial F_2}{\partial x_1}-\frac{\partial F_1}{\partial x_2}\Big) = -\operatorname{rot}\vec F.$$
:::

::::beispiel Aus der Quelle wird ein Wirbel
Die Quellströmung $\vec F(x,y)=(x,y)$ hat Divergenz $2$ und Rotation $0$:

$$\operatorname{div}\vec F = 1+1 = 2, \qquad \operatorname{rot}\vec F = \frac{\partial y}{\partial x}-\frac{\partial x}{\partial y} = 0.$$

Um $90^\circ$ gedreht wird daraus das kreisende Feld, mit vertauschten Rollen:

$$\vec F^{\perp}(x,y) = (-y,\ x), \qquad \operatorname{div}\vec F^{\perp} = 0, \qquad \operatorname{rot}\vec F^{\perp} = 1-(-1) = 2.$$

Beide Gleichungen des Lemmas stimmen: Die Divergenz $2$ der Quelle ist die Rotation des Wirbels, und die Divergenz $0$
des Wirbels ist das Negative der Rotation $0$ der Quelle.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/03-quelle-wird-wirbel · Vorlage: feld-drehen-90-2d
Die Quellströmung $(x,y)$ mit einem Kästchen; ein Regler dreht jeden Pfeil stufenlos um bis zu $90^\circ$. Am Ende ist
daraus das kreisende Feld $(-y,x)$ geworden, und an der Stelle des Kästchens dreht sich ein Schaufelrad. Die Anzeigen
wandern dabei von Divergenz $2$, Rotation $0$ zu Divergenz $0$, Rotation $2$. Kernaussage: In der Ebene sind Quelle und
Wirbel dasselbe, um $90^\circ$ gedreht. (Blau = Feld, orange = Kästchen/Schaufelrad, grau = Gitter.)
:::
::::

## Rotation und Integrabilitätsbedingung

Für Felder $\vec F=(F_1,\ldots,F_n)^T$ in **beliebiger** Dimension gibt es eine einheitliche Form der Rotation — nicht als
Vektor, sondern als Matrix. Ihre Einträge sind

:::formel Definition
$$\omega_{jk} := \frac12\Big(\frac{\partial F_k}{\partial x_j}-\frac{\partial F_j}{\partial x_k}\Big), \qquad 1\le j,k\le n.$$
:::

Die Matrix $\Omega=(\omega_{jk})_{jk}$ ist __schiefsymmetrisch__: Spiegeln an der Diagonale kehrt das Vorzeichen um,
$\omega_{kj}=-\omega_{jk}$, und auf der Diagonale stehen Nullen. Sie ist der schiefsymmetrische Anteil der
transponierten Jacobi-Matrix $(D\vec F)^T$, deren Eintrag $(j,k)$ gerade $\partial F_k/\partial x_j$ ist.

**Die Rotation steckt darin.** Man braucht das Levi-Civita-Symbol in drei Dimensionen und sein ebenes Gegenstück mit
zwei Indizes:

$$\varepsilon_{12} = 1, \qquad \varepsilon_{21} = -1, \qquad \varepsilon_{11} = \varepsilon_{22} = 0.$$

Damit rekonstruiert man

$$(\operatorname{rot}\vec F)_i = \sum_{j,k=1}^{3}\varepsilon_{ijk}\,\omega_{jk} \quad(n=3), \qquad \operatorname{rot}\vec F = \sum_{j,k=1}^{2}\varepsilon_{jk}\,\omega_{jk} \quad(n=2).$$

:::herleitung
**Drei Dimensionen.** Man setzt $\omega_{jk}$ ein und zerlegt die Summe in zwei Teile:

$$\sum_{j,k}\varepsilon_{ijk}\,\omega_{jk} = \frac12\sum_{j,k}\varepsilon_{ijk}\,\frac{\partial F_k}{\partial x_j} - \frac12\sum_{j,k}\varepsilon_{ijk}\,\frac{\partial F_j}{\partial x_k}.$$

Im zweiten Teil benennt man die Summationsindizes $j$ und $k$ um. Dabei wird aus $\varepsilon_{ijk}$ das Symbol
$\varepsilon_{ikj}$, das wegen des Tauschs das umgekehrte Vorzeichen hat. Der zweite Teil ist also das Negative des
ersten, und die Differenz ist zweimal die Hälfte:

$$\sum_{j,k}\varepsilon_{ijk}\,\omega_{jk} = \frac12\,(\operatorname{rot}\vec F)_i + \frac12\,(\operatorname{rot}\vec F)_i = (\operatorname{rot}\vec F)_i.$$

**Zwei Dimensionen.** Nur die beiden Terme mit $j\neq k$ bleiben, und $\omega_{21}$ ist das Negative von $\omega_{12}$:

$$\varepsilon_{12}\,\omega_{12}+\varepsilon_{21}\,\omega_{21} = \omega_{12}-\omega_{21} = 2\,\omega_{12} = \frac{\partial F_2}{\partial x_1}-\frac{\partial F_1}{\partial x_2} = \operatorname{rot}\vec F.$$
:::

**Im Bild: Dehnung für das Kästchen, Drehung für das Rad.** Unter der Lupe des ersten Artikels ist die Strömung nahe
$\vec x_0$ linear, beschrieben durch die Jacobi-Matrix. Jede Matrix zerfällt in einen symmetrischen und einen
schiefsymmetrischen Anteil:

$$D\vec F = \underbrace{\tfrac12\big(D\vec F+(D\vec F)^T\big)}_{S\ \text{(Dehnung)}} + \underbrace{\tfrac12\big(D\vec F-(D\vec F)^T\big)}_{A\ \text{(Drehung)}}.$$

Der symmetrische Anteil $S$ dehnt und staucht längs zueinander senkrechter Achsen, ohne zu drehen. Der schiefsymmetrische
Anteil $A$ — das ist $\Omega$, an der Diagonale gespiegelt — dreht starr. Die beiden Messgeräte teilen sich die Arbeit:
Das Kästchen sieht nur die Dehnung, denn die Divergenz ist die Spur und $A$ hat nur Nullen auf der Diagonale. Das
Schaufelrad sieht nur die Drehung, denn die Rotation ist aus $\Omega$ gebaut. Im Raum wirkt $A$ wie eine Drehung mit der
Winkelgeschwindigkeit $\tfrac12\operatorname{rot}\vec F$:

$$A\,\vec h = \tfrac12\,\operatorname{rot}\vec F\times\vec h \qquad\text{für alle } \vec h\in\mathbb{R}^3.$$

Ein winziges, frei mitschwimmendes Rädchen dreht sich deshalb mit **der Hälfte** der Rotation.

:::herleitung
Man vergleicht die erste Komponente; die anderen folgen zyklisch. Die erste Zeile von $A$ hat die Einträge
$0$, $\tfrac12(\partial_2F_1-\partial_1F_2)$ und $\tfrac12(\partial_3F_1-\partial_1F_3)$, wobei $\partial_j$ die
partielle Ableitung nach $x_j$ abkürzt. Also

$$(A\,\vec h)_1 = \tfrac12\big(\partial_2F_1-\partial_1F_2\big)\,h_2 + \tfrac12\big(\partial_3F_1-\partial_1F_3\big)\,h_3.$$

Die erste Komponente des Kreuzprodukts ist zweite mal dritte minus dritte mal zweite Komponente:

$$\big(\tfrac12\operatorname{rot}\vec F\times\vec h\big)_1 = \tfrac12\big(\partial_3F_1-\partial_1F_3\big)\,h_3 - \tfrac12\big(\partial_1F_2-\partial_2F_1\big)\,h_2.$$

Beide Ausdrücke stimmen überein.
:::

::::beispiel Scherung ist halb Dehnung, halb Drehung
Die ebene Scherströmung $\vec F(x,y)=(y,0)$ hat die Jacobi-Matrix und die beiden Anteile

$$D\vec F = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad S = \begin{pmatrix} 0 & \tfrac12 \\ \tfrac12 & 0 \end{pmatrix}, \qquad A = \begin{pmatrix} 0 & \tfrac12 \\ -\tfrac12 & 0 \end{pmatrix}.$$

Die Drehmatrix $\Omega$ ist $A$ gespiegelt, mit $\omega_{12}=-\tfrac12$; daraus ergibt sich wie direkt die Rotation:

$$\operatorname{rot}\vec F = 2\,\omega_{12} = -1 = \frac{\partial 0}{\partial x}-\frac{\partial y}{\partial y}.$$

Die Dehnung $S$ streckt längs der Diagonale und staucht quer dazu:

$$S\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \tfrac12\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \qquad S\begin{pmatrix} 1 \\ -1 \end{pmatrix} = -\tfrac12\begin{pmatrix} 1 \\ -1 \end{pmatrix}.$$

**Im Bild:** Ein kleiner Farbklecks in der Scherströmung wird längs der Diagonale zu einer Ellipse gezogen und dreht sich
dabei im Uhrzeigersinn, mit der Winkelgeschwindigkeit $\tfrac12$. Die Divergenz ist null, denn die Dehnung längs der einen
Achse gleicht die Stauchung längs der anderen genau aus — die Fläche des Kleckses bleibt gleich.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/03-scherung-zerlegung · Vorlage: matrix-zerlegung-dehnung-drehung-2d
Ein kreisrunder Farbklecks in der Scherströmung $(y,0)$; drei Spalten zeigen seine Verformung nach kurzer Zeit: unter der
vollen Scherung, nur unter der Dehnung $S$ (Ellipse längs der Diagonale) und nur unter der Drehung $A$ (gedrehter Kreis
mit Markierung). Kernaussage: Scherung = Dehnung + Drehung; das Kästchen sieht nur die Dehnung, das Schaufelrad nur die
Drehung. (Blau = Strömung, orange = Klecks, rot = Hauptachsen, grau = Gitter.)
:::
::::

**Gradientenfelder sind wirbelfrei.** Für ein Gradientenfeld ist die Jacobi-Matrix symmetrisch (voriger Artikel) — das
ist die __Integrabilitätsbedingung__, in der Sprache dieses Abschnitts $\Omega=0$. In zwei und drei Dimensionen heißt
das: Die Rotation verschwindet.

:::formel Satz
$$\operatorname{rot}\big(\nabla\phi\big) = \vec 0 \qquad\text{für alle } \phi\in C^2(U),\ U\subseteq\mathbb{R}^3 \text{ offen}.$$
:::

**Im Bild:** In den Steigungspfeilen einer echten Landschaft dreht sich kein Schaufelrad. Die Pfeile laufen den Hang
hinauf, aber sie umkreisen nichts.

:::herleitung
Die erste Komponente von $\operatorname{rot}\nabla\phi$ ist eine Differenz gemischter zweiter Ableitungen:

$$\frac{\partial}{\partial x_2}\Big(\frac{\partial\phi}{\partial x_3}\Big) - \frac{\partial}{\partial x_3}\Big(\frac{\partial\phi}{\partial x_2}\Big) = 0.$$

Nach dem __Satz von Schwarz__ vertauschen diese für $\phi\in C^2$, die Differenz ist null; genauso verschwinden die
anderen beiden Komponenten. In der Ebene ist die Rotation $\partial_1\partial_2\phi-\partial_2\partial_1\phi$, ebenfalls
null.
:::

::::beispiel Kein Rad dreht sich in einer Landschaft
Das Feld der Sattelfläche $xy$ aus dem vorigen Artikel, räumlich aufgefasst,

$$\vec E(x,y,z) = \nabla(xy) = (y,\ x,\ 0),$$

hat keine Rotation:

$$\operatorname{rot}\vec E = \big(\partial_y0-\partial_z x,\ \ \partial_z y-\partial_x0,\ \ \partial_x x-\partial_y y\big) = (0,\ 0,\ 1-1) = \vec 0.$$

Das kreisende Feld $(-y,x,0)$ mit der Rotation $(0,0,2)$ kann dagegen kein Gradientenfeld sein — genau wie im vorigen
Artikel mit der Integrabilitätsbedingung festgestellt.
::::

**Notwendig, aber nicht hinreichend.** Ist jedes wirbelfreie Feld ein Gradientenfeld? Im Allgemeinen **nein** — es hängt
von der Gestalt des Gebiets ab. Unter welchen Voraussetzungen die Bedingung doch reicht (Gebiete ohne Löcher,
Poincaré-Lemma), klärt später der Stokessche Integralsatz.

::::beispiel Ein Wirbel, der nicht wirbelt
Das Wendeltreppen-Feld aus dem vorigen Artikel, auf $\mathbb{R}^2\setminus\{\vec 0\}$,

$$\vec W(x,y) = \frac{1}{x^2+y^2}\,(-y,\ x),$$

beschreibt Wasser, das um einen Abfluss kreist, mit dem Tempo $1/r$. Seine Rotation ist überall null, denn die beiden
gemischten Ableitungen sind gleich (voriger Artikel):

$$\operatorname{rot}\vec W = \frac{\partial W_2}{\partial x}-\frac{\partial W_1}{\partial y} = \frac{y^2-x^2}{(x^2+y^2)^2}-\frac{y^2-x^2}{(x^2+y^2)^2} = 0.$$

Trotzdem hat $\vec W$ kein Potential — ein Umlauf gewinnt die Höhe $2\pi$ (voriger Artikel).

**Im Bild:** Ein kleines Schaufelrad wird zwar im Kreis um den Abfluss getragen, dreht sich aber nicht um die eigene
Achse — seine innere Hälfte wird schneller angeströmt als die äußere, und das hebt die Drehung durch die Kreisbahn genau
auf. Physiker nennen das einen __Potentialwirbel__; die Badewanne zeigt ihn am Abfluss.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/03-potentialwirbel · Vorlage: wirbel-ohne-rotation-2d
Wasser kreist um einen Abfluss im Ursprung, innen schnell, außen langsam (Tempo $1/r$). Zwei kleine Schaufelräder werden
mitgetragen: eines im Potentialwirbel $\vec W$ (behält seine Ausrichtung, Markierung zeigt immer nach oben), zum Vergleich
eines in der starren Drehung $(-y,x)$ (dreht sich mit). Kernaussage: Kreisen ist nicht dasselbe wie Wirbeln — die
Rotation misst das Drehen am Ort. (Blau = Strömung, orange = Schaufelräder, grau = Abfluss.)
:::
::::

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/03-rot-grad-null · Vorlage: gradient-vs-wirbel-2d
Links ein Gradientenfeld (Pfeile senkrecht auf den Höhenlinien) mit einem stillstehenden Schaufelrad:
„$\operatorname{rot}\nabla\phi=\vec 0$". Rechts ein echtes Wirbelfeld mit sich drehendem Rad: „kann kein Gradientenfeld
sein". Dazwischen der Hinweis „notwendig, nicht hinreichend — Umkehrung später mit Stokes". (Rot = Gradientenfeld,
orange = Wirbelfeld und Räder, grau = Höhenlinien.)
:::

## Bedeutung und Ausblick

Mit Gradient, Divergenz und Rotation steht das vollständige Trio der Differentialoperatoren erster Ordnung, dazu der
Laplace-Operator als wichtigster Operator zweiter Ordnung. Sie sind die Vokabeln, in denen die ganze Feldphysik
formuliert ist.

In den Maxwell-Gleichungen stehen genau die beiden Messgeräte: Die Divergenz des elektrischen Feldes zählt die Ladungen,
also seine Quellen, und das Magnetfeld ist überall quellenfrei. Die Rotation des elektrischen Feldes entsteht durch
zeitlich veränderliche Magnetfelder, die Rotation des Magnetfeldes durch Ströme und zeitlich veränderliche elektrische
Felder. Die Wärmeleitungsgleichung sagt in
diesem Bild: Die Temperatur steigt dort, wo sie in einer Mulde liegt — Wärme fließt in die kälteren Punkte.

Diese Operatoren gehorchen einer Reihe eleganter **Rechenregeln und Identitäten** — etwa „ein Wirbel quillt nie" oder die
Zerlegung der doppelten Rotation. Sie sind das Handwerkszeug für alle folgenden Rechnungen und das Thema des nächsten
Artikels.

:::kern
- Aus dem Nabla-Operator entstehen __Divergenz__ (Vektor → Skalar), __Rotation__ (Vektor → Vektor) und, zusammen mit dem Gradienten, der __Laplace-Operator__.
- __Divergenz__ $\operatorname{div}\vec E=\nabla\cdot\vec E=\sum_j\partial E_j/\partial x_j$: Netto-Ausfluss pro Fläche bzw. Volumen — das Kästchen; positiv: Quelle, negativ: Senke, null: quellenfrei.
- Die Divergenz ist die Spur der Jacobi-Matrix.
- __Produktregel__: $\operatorname{div}(\phi\vec E)=\nabla\phi\cdot\vec E+\phi\operatorname{div}\vec E$.
- __Radial__: $\operatorname{div}(s(r)\vec e_r)=s'(r)+(n-1)\,s(r)/r$; Felder wie $1/r^{n-1}$ sind außerhalb des Ursprungs quellenfrei.
- __Laplace__ $\Delta\phi=\sum_j\partial^2\phi/\partial x_j^2=\operatorname{div}\nabla\phi$: positiv in einer Mulde, negativ auf einer Kuppe — das Mittel der Nachbarn minus die Mitte ist ungefähr $\tfrac{h^2}{2n}\Delta\phi$.
- __Harmonisch__ heißt $\Delta\phi=0$: Gleichgewicht, jeder Punkt auf dem Mittel seiner Nachbarn — etwa das Coulomb-Potential außerhalb der Ladung.
- __Rotation__ $\operatorname{rot}\vec E=\nabla\times\vec E$ (nur im $\mathbb{R}^3$): Zirkulation pro Fläche — das Schaufelrad; jede Komponente ist die Wirbeldichte um ihre Achse.
- In der Ebene ist die Rotation die Zahl $\partial_1E_2-\partial_2E_1$; Quelle und Wirbel gehen durch eine Vierteldrehung ineinander über, $\operatorname{div}\vec F=\operatorname{rot}\vec F^{\perp}$.
- Die Drehmatrix $\Omega$ mit $\omega_{jk}=\tfrac12(\partial_jF_k-\partial_kF_j)$ enthält die Rotation in jeder Dimension; ein mitschwimmendes Rädchen dreht sich mit der Hälfte der Rotation.
- Gradientenfelder sind wirbelfrei, $\operatorname{rot}\nabla\phi=\vec 0$ (Satz von Schwarz) — notwendig, nicht hinreichend: Der Potentialwirbel ist wirbelfrei, hat aber kein Potential.
:::

:::quiz
F: Warum misst die Divergenz den Netto-Ausfluss — erklärt mit dem Kästchen?
A: Durch gegenüberliegende Wände eines kleinen Kästchens der Seitenlänge $h$ fließt Wasser hinein und hinaus; der Unterschied ist ungefähr $h$ mal die Änderung der Normalkomponente, also $h^2\,\partial E_j/\partial x_j$ pro Wandpaar. Summiert über alle Richtungen ergibt das $h^2\operatorname{div}\vec E$: Die Divergenz ist Netto-Ausfluss pro Fläche, und nur die Änderung der Strömung quer durch das Kästchen zählt.
F: Was zeigt das Kästchen $[-1,1]^2$ in den Strömungen $(x,y)$, $(-x,0)$ und $(-y,x)$?
A: Bei $(x,y)$ ist die Divergenz $2$, und netto fließen $8$ hinaus, also $2$ mal die Fläche $4$ — eine Quelle. Bei $(-x,0)$ ist die Divergenz $-1$, netto fließen $4$ hinein — eine Senke. Beim kreisenden Feld $(-y,x)$ ist die Divergenz $0$, durch jede Wand fließt so viel hinein wie hinaus.
F: Woher kommt die radiale Divergenzformel, und warum ist das $1/r^2$-Feld im Raum außerhalb des Ursprungs quellenfrei?
A: Man schreibt $s(r)\vec e_r$ als $\frac{s(r)}{r}\vec x$ und benutzt die Produktregel mit $\operatorname{div}\vec x=n$; heraus kommt $s'(r)+(n-1)s(r)/r$. Für $s=1/r^2$ und $n=3$ heben sich $-2/r^3$ und $+2/r^3$ auf: Durch jede Kugelschale geht gleich viel Fluss, weil die Fläche mit $r^2$ wächst und die Feldstärke mit $1/r^2$ fällt.
F: Was misst der Laplace-Operator im Bild der Nachbarn, und warum hebt sich die Steigung dabei weg?
A: Das Mittel der $2n$ Gitternachbarn liegt um ungefähr $\frac{h^2}{2n}\Delta\phi$ über dem Wert in der Mitte. Nach der Taylor-Formel liegt ein Nachbar um die Steigung mal $h$ höher, der gegenüberliegende genauso viel tiefer — dieser Anteil fällt weg, übrig bleibt die Krümmung. Positiv heißt Mulde, negativ Kuppe.
F: Warum ist $x^2-y^2$ harmonisch, $x^2+y^2$ aber nicht — am Punkt $(1,0)$ gezeigt?
A: Für $x^2+y^2$ ist $\Delta\phi=4$: Die Nachbarn haben die Werte $4,0,2,2$, ihr Mittel $2$ liegt um $1$ über der Mitte $1$ — eine Mulde. Für $x^2-y^2$ ist $\Delta\phi=0$: Die Nachbarn $4,0,0,0$ haben das Mittel $1$, genau den Wert der Mitte. Der Sattel ist in $x$-Richtung Mulde, in $y$-Richtung Kuppe, und beides hebt sich auf.
F: Warum ist das Coulomb-Potential $\frac{Q}{4\pi r}$ außerhalb der Ladung harmonisch?
A: Sein Gradient ist das radiale Feld mit dem Profil $s(r)=-\frac{Q}{4\pi r^2}$. Die radiale Divergenzformel mit $n=3$ gibt $s'+2s/r=\frac{2Q}{4\pi r^3}-\frac{2Q}{4\pi r^3}=0$. Außerhalb der Ladung sitzt keine Quelle; im Ursprung ist das Potential nicht definiert, dort sitzt die Ladung selbst.
F: Wie misst ein Schaufelrad die Rotation, und warum dreht es sich in der Scherströmung $(y,0,0)$?
A: Das Rad spürt die Zirkulation um ein kleines Quadrat um seine Achse; sie ist ungefähr $h^2$ mal die zugehörige Komponente der Rotation, etwa $\partial_1E_2-\partial_2E_1$ für die senkrechte Achse. In der Scherströmung ist $\operatorname{rot}\vec E=(0,0,-1)$: Die obere Hälfte des Rades wird stärker angeschoben als die untere, es dreht sich im Uhrzeigersinn, obwohl das Wasser geradeaus fließt.
F: Wie hängen Divergenz und Rotation in der Ebene über eine Vierteldrehung zusammen?
A: Mit dem um $90^\circ$ gedrehten Feld $\vec F^{\perp}=(-F_2,F_1)$ gilt $\operatorname{div}\vec F=\operatorname{rot}\vec F^{\perp}$ und $\operatorname{div}\vec F^{\perp}=-\operatorname{rot}\vec F$, wie man durch Einsetzen sieht. So wird aus der Quelle $(x,y)$ mit Divergenz $2$ der Wirbel $(-y,x)$ mit Rotation $2$.
F: Was ist die Drehmatrix $\Omega$, und warum dreht sich ein kleines Rädchen nur mit der Hälfte der Rotation?
A: $\Omega$ hat die Einträge $\omega_{jk}=\frac12(\partial_jF_k-\partial_kF_j)$; sie ist der schiefsymmetrische Anteil der transponierten Jacobi-Matrix, und aus ihr setzt sich die Rotation zusammen. Unter der Lupe zerfällt die Strömung in Dehnung und Drehung, und der Drehanteil wirkt wie $\frac12\operatorname{rot}\vec F\times\vec h$ — eine starre Drehung mit der Winkelgeschwindigkeit $\frac12\operatorname{rot}\vec F$. Bei der starren Drehung $(-y,x,0)$ ist die Rotation $2$, das Rad läuft mit $1$, also mit dem Wasser.
F: Warum gilt $\operatorname{rot}\nabla\phi=\vec 0$, und warum folgt aus „wirbelfrei" trotzdem kein Potential?
A: Jede Komponente von $\operatorname{rot}\nabla\phi$ ist eine Differenz gemischter zweiter Ableitungen, die nach dem Satz von Schwarz verschwindet: In einer echten Landschaft dreht sich kein Rad. Die Umkehrung hängt vom Gebiet ab: Der Potentialwirbel $\vec W=\frac{(-y,x)}{x^2+y^2}$ ist auf der Ebene ohne Ursprung wirbelfrei, hat aber kein Potential, weil ein Umlauf die Höhe $2\pi$ gewinnt.
:::
