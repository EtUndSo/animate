---
title: Volumenintegrale: Zylinder- und Kugelkoordinaten
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3040200
summary: Von Grund auf – der Transformationssatz im Raum und seine beiden Arbeitspferde. Leitbild ist ein Gummiklotz mit einem Gitter aus kleinen Würfeln, die räumliche Fassung des Gummituchs – Zylinderkoordinaten machen daraus einen Baumstamm mit Jahresringen, Kugelkoordinaten eine Zwiebel. Mit den Volumenelementen $\varrho\,d\varrho\,d\varphi\,dz$ und $r^2\sin\theta\,dr\,d\theta\,d\varphi$, der Formel $\pi\int p(z)^2\,dz$ für Rotationskörper, Kugel, Kegel und Trägheitsmomenten – und dem Satz, warum singuläre Funktionen wie das Coulomb-Potential im Raum integrierbar sind: Die innersten Zwiebelschalen sind winzig. Mit Beispiel-Seite.
tags: Volumenintegral, Zylinderkoordinaten, Kugelkoordinaten, Jacobi-Determinante, Rotationskörper, Kugelvolumen, singuläre radiale Funktion, Coulomb-Potential
---

## Anschaulich

Wie viel Kupfer steckt in einem Rohr, wie träge ist eine rotierende Kugel, wie viel Ladung sitzt in einer Wolke um einen
Kern? Solche Volumenintegrale sind kartesisch mühsam, denn Zylinder und Kugeln haben krumme Ränder. In angepassten
Koordinaten werden sie zu Quadern: Ein Zylinder ist ein Quader aus Abstand zur Achse, Winkel und Höhe, eine Kugel einer aus
Abstand zum Mittelpunkt und zwei Winkeln.

**Das Leitbild dieses Artikels:** ein **Gummiklotz**, die räumliche Fassung des Gummituchs aus dem vorigen Artikel. Im Klotz
steckt ein Gitter aus kleinen, gleich großen Würfeln. Eine Abbildung $\vec\Phi$ verformt den Klotz, und aus jedem Würfel wird
ein krummes **Klötzchen**. Unter der Lupe ist es fast ein schiefer Quader, und sein Volumen ist das Würfelvolumen mal dem
Betrag der Jacobi-Determinante — der __Volumenfaktor__.

Zylinderkoordinaten machen aus dem Gitter einen **Baumstamm**: Jahresringe gleichen Abstands von der Achse, radiale Schnitte
wie bei einer Torte und waagerechte Baumscheiben. Kugelkoordinaten machen daraus eine **Zwiebel**: Schalen gleichen Abstands
vom Mittelpunkt, Spalten wie bei einer Orange und Breitenkreise wie auf einem Globus.

Das Zwiebelbild erklärt am Ende auch eine überraschende Tatsache. Das Coulomb-Potential einer Punktladung wird am Ort der
Ladung unendlich groß — und trotzdem ist sein Integral über eine Kugel endlich. Die innersten Zwiebelschalen sind so winzig,
dass sie die Singularität zähmen.

:::grafik
Szene: hoema3/koordinatentransformationen/02-klotz-stamm-zwiebel · Vorlage: gitter-verzerrung-3d
Links ein Würfelgitter in den neuen Koordinaten, rechts sein Bild; ein Umschalter wählt zwischen dem Baumstamm (Jahresringe,
radiale Schnitte, Baumscheiben) und der Zwiebel (Schalen, Spalten, Breitenkreise). Ein markiertes Klötzchen wird
hervorgehoben und seine Kanten beschriftet — beim Stamm $d\varrho$, $\varrho\,d\varphi$ und $dz$, bei der Zwiebel $dr$,
$r\,d\theta$ und $r\sin\theta\,d\varphi$ —; ein Zähler zeigt sein Volumen. Zieht man das Klötzchen zur Achse oder zu einem Pol,
schrumpft es. Kernaussage: Jedes Klötzchen zählt mit dem Volumenfaktor $\lvert\det D\vec\Phi\rvert$. (Rot = Klötzchen, blau =
Gitter, orange = Kantenlängen, grau = Achsen.)
:::

## Der Transformationssatz im Raum

Der Transformationssatz des vorigen Artikels gilt in jeder Dimension, insbesondere im Raum. **Die Akteure** sind dieselben
wie in der Ebene: ein Gebiet $G\subseteq\mathbb{R}^3$, eine stetig differenzierbare Abbildung $\vec\Phi:G\to\mathbb{R}^3$ und ein
regulärer Bereich $B\subseteq G$, dessen Bild $\vec\Phi(B)$ wieder ein regulärer Bereich ist. Die Abbildung nimmt einen Punkt
der neuen Koordinaten und gibt einen Punkt des Raums aus:

$$\vec u = (u_1,u_2,u_3) \;\mapsto\; \vec x = \vec\Phi(\vec u) = (x,y,z).$$

Wie in der Ebene muss $\vec\Phi$ auf $B$ injektiv sein und darf nirgends flachdrücken:

$$\det D\vec\Phi(\vec u)\neq0 \quad\text{für alle } \vec u\in B.$$

Ein __regulärer Bereich__ im Raum ist beschränkt und abgeschlossen, und sein Rand besteht aus regulären Flächen. Genau
definiert werden diese Flächen erst im Artikel
[Reguläre Flächen und das Oberflächenintegral](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum/regulaere-flaechen-und-oberflaechenintegral.html);
für diesen Artikel reichen Quader, Zylinder, Kugeln, Kegel und Rotationskörper.

Dann gilt für jede stetige Funktion $f:\vec\Phi(B)\to\mathbb{R}$

:::formel Satz
$$\int_{\vec\Phi(B)}f(\vec x)\,d^3x = \int_B f\big(\vec\Phi(\vec u)\big)\,\big\lvert\det D\vec\Phi(\vec u)\big\rvert\,d^3u.$$
:::

**So liest man das:** Links steht das Volumenintegral über den krummen Körper in kartesischen Koordinaten, rechts das
Integral über den einfachen Parameterbereich, gewichtet mit dem Volumenfaktor $\lvert\det D\vec\Phi\rvert$.

**Im Bild:** Jedes Klötzchen des verformten Klotzes ist unter der Lupe ein Parallelotop, das aus einem Würfel des Gitters
entstand. Sein Volumen ist das Würfelvolumen mal $\lvert\det D\vec\Phi\rvert$.

:::herleitung
Die Begründung des vorigen Artikels gilt wörtlich im Raum. Dort wurde das Lemma über den Volumenfaktor linearer Abbildungen
in jeder Dimension hergeleitet, mit dem Gauß-Verfahren, Scherungen und Fubini:

$$\mathrm{vol}(AQ) = \lvert\det A\rvert\;\mathrm{vol}(Q).$$

Unter der Lupe ist $\vec\Phi$ nahe jedem Punkt fast linear, mit der Jacobi-Matrix als linearer Näherung. Ein kleiner Würfel
wird deshalb fast auf ein Parallelotop abgebildet, dessen Volumen das Würfelvolumen mal $\lvert\det D\vec\Phi\rvert$ ist.
Riemann-Summen über feine Würfelgitter ergeben die beiden Seiten des Satzes.

Einen vollständigen Beweis im Raum führen wir hier nicht; wir rechnen mit dem Satz.

**Im Bild:** Links zählt man die Klötzchen des verformten Klotzes mit ihrem echten Volumen, rechts die Würfel des Gitters mit
ihrem Volumenfaktor.
:::

::::beispiel Ein Ellipsoid aus der Kugel
Die abgeschlossene Einheitskugel $K_1$ ist die Menge der Punkte des Raums mit dem Abstand höchstens $1$ vom Ursprung. Die
Abbildung

$$\vec\Phi(\vec u) = (u_1,\ 2u_2,\ 3u_3), \qquad \det D\vec\Phi = 1\cdot2\cdot3 = 6,$$

bildet sie injektiv auf das Ellipsoid

$$M = \Big\{(x,y,z)\in\mathbb{R}^3 : x^2+\frac{y^2}{4}+\frac{z^2}{9}\le1\Big\}$$

mit den Halbachsen $1$, $2$ und $3$ ab, denn für den Bildpunkt ist

$$x^2+\frac{y^2}{4}+\frac{z^2}{9} = u_1^2+u_2^2+u_3^2.$$

Das Volumen der Einheitskugel, $\frac43\pi$, kennt man aus dem Artikel über Integration über Mengen. Mit $f=1$ gibt der Satz

$$\mathrm{vol}(M) = \int_{K_1}6\,d^3u = 6\cdot\frac43\pi = 8\pi.$$

**Im Bild:** Der Gummiklotz wird in den drei Achsenrichtungen um $1$, $2$ und $3$ gestreckt; jedes Klötzchen wird sechsmal so
groß.
::::

## Zylinderkoordinaten

Zylinderkoordinaten sind die Polarkoordinaten der $xy$-Ebene, ergänzt um die unveränderte Höhe $z$. Den Abstand von der
$z$-Achse nennen wir hier $\varrho$, wie in der Elektrotechnik üblich. Oft schreibt man dafür auch $r$, aber $r$ ist in diesem
Artikel der Abstand vom Ursprung, wie in den Kugelkoordinaten weiter unten.

**Die Akteure:** ein Radius $R>0$, zwei Höhen $a<b$ und der Zylinder

$$Z = \big\{(x,y,z)\in\mathbb{R}^3 : x^2+y^2\le R^2,\ a\le z\le b\big\}.$$

Er ist das Bild des Quaders der Zylinderkoordinaten:

$$\vec\Phi(\varrho,\varphi,z) = (\varrho\cos\varphi,\ \varrho\sin\varphi,\ z), \qquad (\varrho,\varphi,z)\in[0,R]\times[0,2\pi]\times[a,b].$$

Die Jacobi-Matrix und ihre Determinante sind

$$D\vec\Phi(\varrho,\varphi,z) = \begin{pmatrix}\cos\varphi & -\varrho\sin\varphi & 0\\ \sin\varphi & \varrho\cos\varphi & 0\\ 0&0&1\end{pmatrix}, \qquad \det D\vec\Phi(\varrho,\varphi,z) = \varrho.$$

:::herleitung
Die ersten beiden Spalten sind die Ableitungen nach $\varrho$ und $\varphi$ — dieselben wie bei den Polarkoordinaten, mit einer
Null für die Höhe. Die dritte ist die Ableitung nach $z$, der Einheitsvektor nach oben. Entwickelt man die Determinante nach
der letzten Zeile, bleibt die Determinante der Polarkoordinaten:

$$\det D\vec\Phi = 1\cdot\det\begin{pmatrix}\cos\varphi & -\varrho\sin\varphi\\ \sin\varphi & \varrho\cos\varphi\end{pmatrix} = \varrho\cos^2\varphi+\varrho\sin^2\varphi = \varrho.$$

**Im Bild:** Die Höhe wird nicht verzerrt. Der Stamm ist ein Stapel gleicher Baumscheiben, und in jeder Scheibe gilt das
Spinnennetz des vorigen Artikels.
:::

Für stetiges $f:Z\to\mathbb{R}$ gilt deshalb

:::formel
$$\begin{aligned}\int_Z f(x,y,z)\,d(x,y,z) &= \int_a^b\int_0^R\int_0^{2\pi}f(\varrho\cos\varphi,\ \varrho\sin\varphi,\ z)\\ &\qquad\cdot\varrho\,d\varphi\,d\varrho\,dz.\end{aligned}$$
:::

**So liest man das:** Das Volumenelement in Zylinderkoordinaten ist $\varrho\,d\varrho\,d\varphi\,dz$. Auf der $z$-Achse und an
der Halbebene, an der der Winkel von $2\pi$ auf $0$ springt, sind die Voraussetzungen des Satzes verletzt — wie bei den
Polarkoordinaten. Die Formel gilt trotzdem.

**Im Bild:** Ein Klötzchen des Baumstamms zwischen zwei Jahresringen, zwei radialen Schnitten und zwei Baumscheiben ist fast
ein Quader mit den Kanten $d\varrho$, dem Bogen $\varrho\,d\varphi$ und $dz$.

:::herleitung
Die Begründung ist die der Polarkoordinaten, mit der Höhe als zusätzlichem Faktor. Auf dem Quader
$[\varepsilon,R]\times[\varepsilon,2\pi]\times[a,b]$ ist $\vec\Phi$ injektiv, und die Determinante ist mindestens $\varepsilon$; dort
gilt der Satz. Seinem Bild fehlen ein dünner Zylinder um die Achse und ein schmaler Keil, zusammen höchstens mit dem Volumen

$$\pi\varepsilon^2\,(b-a)+\frac{\varepsilon}{2}\,R^2\,(b-a).$$

Dem Parameterquader fehlen zwei Platten mit zusammen höchstens dem Volumen

$$(2\pi\varepsilon+R\varepsilon)\,(b-a).$$

Weil $f$ auf $Z$ beschränkt ist, gehen beide Unterschiede für $\varepsilon\to0$ gegen null.

**Im Bild:** Man bohrt den Kern des Stamms aus und sägt einen schmalen Keil heraus; beide werden beliebig dünn.
:::

::::beispiel Rohr und Walze
**(a) Ein Rohr** mit dem Innenradius $R_1$, dem Außenradius $R_2$ und der Länge $H$: Der Abstand von der Achse läuft von $R_1$
bis $R_2$, mit derselben Begründung, und das Volumen ist

$$\int_0^H\int_{R_1}^{R_2}\int_0^{2\pi}\varrho\,d\varphi\,d\varrho\,dz = 2\pi\cdot\frac{R_2^2-R_1^2}{2}\cdot H = \pi\big(R_2^2-R_1^2\big)H.$$

Ein Kupferrohr mit $7\,\mathrm{mm}$ Innen- und $8\,\mathrm{mm}$ Außenradius und $1\,\mathrm{m}$ Länge enthält

$$\pi\big(8^2-7^2\big)\,\mathrm{mm}^2\cdot1000\,\mathrm{mm} = 15\,000\,\pi\,\mathrm{mm}^3\approx47{,}1\,\mathrm{cm}^3$$

Kupfer — bei rund $9\,\mathrm{g}$ pro Kubikzentimeter gut $400\,\mathrm{g}$.

**(b) Das Trägheitsmoment einer Walze.** Ein gleichmäßig gefüllter Vollzylinder der Masse $m$, mit dem Radius $R$ und der Länge
$H$, ist der Zylinder $Z$ mit den Höhen $0$ und $H$. Sein Trägheitsmoment um die Achse ist das Integral des Abstandsquadrats
zur Achse über die Masse:

$$J = \frac{m}{\pi R^2H}\int_Z\big(x^2+y^2\big)\,d(x,y,z) = \frac{m}{\pi R^2H}\int_0^H\int_0^R\int_0^{2\pi}\varrho^2\cdot\varrho\,d\varphi\,d\varrho\,dz.$$

Die drei Integrale geben $2\pi$, $\frac{R^4}{4}$ und $H$, also

$$J = \frac{m}{\pi R^2H}\cdot\frac{\pi R^4H}{2} = \frac{mR^2}{2}.$$

**Im Bild:** Die Walze ist ein Stapel gleicher Baumscheiben. Jede hat nach dem vorigen Artikel das Trägheitsmoment ihrer
Masse mal dem halben Radiusquadrat, und deshalb kürzt sich die Länge heraus.
::::

## Rotationskörper

Dreht man ein Profil um die $z$-Achse, entsteht ein __Rotationskörper__ — wie das Werkstück auf der Drehbank aus dem Artikel
über Integration über Mengen. **Die Akteure:** zwei Höhen $a<b$ und ein stetig differenzierbares __Profil__
$p:[a,b]\to\mathbb{R}$ ohne Nullstelle. Der Körper ist

$$W = \big\{(x,y,z)\in\mathbb{R}^3 : a\le z\le b,\ x^2+y^2\le p(z)^2\big\}.$$

In der Höhe $z$ ist sein Querschnitt die Kreisscheibe vom Radius $\lvert p(z)\rvert$.

Statt bis zu einem festen Radius läuft man in jeder Höhe bis zum Profil, mit dem Anteil $t\in[0,1]$ des Profilradius. Das
sind die __verallgemeinerten Zylinderkoordinaten__:

$$\vec\Phi(t,\varphi,z) = \big(t\,p(z)\cos\varphi,\ t\,p(z)\sin\varphi,\ z\big), \qquad (t,\varphi,z)\in[0,1]\times[0,2\pi]\times[a,b].$$

Ihre Determinante ist

$$\det D\vec\Phi(t,\varphi,z) = t\,p(z)^2.$$

Für das konstante Profil $1$ entstehen die Zylinderkoordinaten des Zylinders vom Radius $1$.

:::herleitung
Die Spalten der Jacobi-Matrix sind die Ableitungen nach $t$, $\varphi$ und $z$:

$$\frac{\partial\vec\Phi}{\partial t} = \big(p\cos\varphi,\ p\sin\varphi,\ 0\big), \qquad \frac{\partial\vec\Phi}{\partial\varphi} = \big(-t\,p\sin\varphi,\ t\,p\cos\varphi,\ 0\big), \qquad \frac{\partial\vec\Phi}{\partial z} = \big(t\,p'\cos\varphi,\ t\,p'\sin\varphi,\ 1\big).$$

Die letzte Zeile der Matrix ist damit $(0,\ 0,\ 1)$. Entwickelt man nach ihr, fallen die dritte Spalte und mit ihr die Ableitung
$p'$ heraus:

$$\det D\vec\Phi = \det\begin{pmatrix}p\cos\varphi & -t\,p\sin\varphi\\ p\sin\varphi & t\,p\cos\varphi\end{pmatrix} = t\,p^2\cos^2\varphi+t\,p^2\sin^2\varphi = t\,p(z)^2.$$

Weil $p$ keine Nullstelle hat, ist die Determinante für $t>0$ positiv.

**Im Bild:** In jeder Baumscheibe wird das Spinnennetz des Einheitskreises um den Faktor $\lvert p(z)\rvert$ gestreckt, seine
Maschen also um $p(z)^2$. Die dritte Spalte sagt, dass das Gitter beim Hochfahren zur Seite rückt, wenn das Profil breiter oder
schmaler wird. Das ist eine Scherung, und eine Scherung ändert kein Volumen.
:::

Mit $f=1$ folgt die Volumenformel für Rotationskörper:

:::formel
$$\mathrm{vol}(W) = \pi\int_a^b p(z)^2\,dz.$$
:::

**So liest man das:** Das Volumen ist das Integral der Querschnittsflächen $\pi p(z)^2$ über die Höhe.

**Im Bild:** Die Drehbank. Jede Baumscheibe des Werkstücks ist eine Kreisscheibe vom Radius $\lvert p(z)\rvert$, und das
Volumen ist die Summe ihrer Flächen mal Dicke — genau wie mit Cavalieri im Artikel über Integration über Mengen.

:::herleitung
Mit der Determinante trennen sich die Integrale:

$$\mathrm{vol}(W) = \int_a^b\int_0^1\int_0^{2\pi}t\,p(z)^2\,d\varphi\,dt\,dz = \int_a^b 2\pi\cdot\frac12\,p(z)^2\,dz = \pi\int_a^b p(z)^2\,dz.$$

Wie bei den Zylinderkoordinaten sind die Voraussetzungen auf der Achse und an der Naht des Winkels verletzt, und dieselbe
Begründung rettet die Formel. Hat das Profil an einem Ende eine Nullstelle oder eine unendliche Steigung, wie an einer
Kegelspitze, integriert man zuerst bis zu einem kleinen Abstand $\delta$ vor diesem Ende. Das fehlende Stück liegt in einem
Zylinder der Höhe $\delta$, und für $\delta\to0$ verschwindet es.
:::

:::grafik
Szene: hoema3/koordinatentransformationen/02-drehbank-profil · Vorlage: rotationskoerper-3d
Links das Profil $p$ über dem Intervall $[a,b]$ der $z$-Achse, rechts der Rotationskörper, der beim Drehen um die $z$-Achse
entsteht. Eine waagerechte Baumscheibe in der Höhe $z$ ist hervorgehoben; darin liegt das Spinnennetz des Einheitskreises, um
den Faktor $\lvert p(z)\rvert$ gestreckt. Ein Regler fährt die Scheibe auf und ab, ein Zähler zeigt ihre Fläche $\pi p(z)^2$ und
das bis dahin aufsummierte Volumen. Kernaussage: Das Volumen ist das Integral der Querschnittsflächen. (Rot = Querschnitt,
blau = Profil, orange = Spinnennetz, grau = Achsen.)
:::

::::beispiel Kegel, runder Laib und Kugel von der Drehbank
**(a) Der Kegel** mit der Spitze im Ursprung, der Höhe $h$ und dem Grundkreisradius $R$ hat das Profil

$$p(z) = \frac{R}{h}\,z, \qquad z\in[0,h],$$

und das Volumen

$$\pi\int_0^h\frac{R^2}{h^2}\,z^2\,dz = \pi\,\frac{R^2}{h^2}\cdot\frac{h^3}{3} = \frac{\pi R^2h}{3}.$$

An der Spitze hat das Profil eine Nullstelle; man integriert erst ab einer kleinen Höhe $\delta$ und lässt sie gegen null gehen.
Heraus kommt das bekannte „Grundfläche mal Höhe durch drei".

**(b) Der runde Laib** aus dem Artikel über Mehrfachintegrale liegt unter der Fläche $z=1-x^2-y^2$ über der
Einheitskreisscheibe. In der Höhe $z\in[0,1]$ ist sein Querschnitt die Kreisscheibe mit

$$x^2+y^2\le1-z, \qquad p(z) = \sqrt{1-z}.$$

Sein Volumen ist

$$\pi\int_0^1(1-z)\,dz = \frac{\pi}{2}$$

— derselbe Wert wie mit Scheiben, mit Cavalieri und mit Polarkoordinaten.

**(c) Die Kugel** vom Radius $R$ hat das Profil $\sqrt{R^2-z^2}$ auf $[-R,R]$:

$$\pi\int_{-R}^{R}\big(R^2-z^2\big)\,dz = \pi\Big(2R^3-\frac{2R^3}{3}\Big) = \frac43\pi R^3.$$

**Im Bild:** Die Drehbank dreht drei verschiedene Profile — eine Gerade, eine Parabel und einen Halbkreis. Das Volumen ist
jedes Mal das Integral der Querschnittsflächen.
::::

## Kugelkoordinaten

**Die Akteure:** ein Radius $R>0$ und die abgeschlossene Kugel

$$K_R = \big\{\vec x\in\mathbb{R}^3 : \lvert\vec x\rvert\le R\big\}.$$

Ihre Punkte beschreibt man durch drei Zahlen: den Abstand $r\in[0,R]$ vom Ursprung, den __Polarwinkel__ $\theta\in[0,\pi]$
gegen die positive $z$-Achse und den __Azimut__ $\varphi\in[0,2\pi]$, den Winkel der Projektion in die $xy$-Ebene gegen die
$x$-Achse — wie bei den Polarkoordinaten. In der Elektrotechnik schreibt man den Polarwinkel oft $\vartheta$.

$$\vec\Phi(r,\theta,\varphi) = \big(r\sin\theta\cos\varphi,\ r\sin\theta\sin\varphi,\ r\cos\theta\big), \qquad (r,\theta,\varphi)\in[0,R]\times[0,\pi]\times[0,2\pi].$$

**Im Bild:** In der Zwiebel wählt $r$ die Schale, $\theta$ den Breitenkreis — vom Nordpol über den Äquator bei
$\theta=\frac{\pi}{2}$ bis zum Südpol — und $\varphi$ die Spalte.

:::herleitung
In der Halbebene zum Azimut $\varphi$ — einer Spalte der Zwiebel — hat der Punkt den Abstand $r\sin\theta$ von der $z$-Achse und
die Höhe $r\cos\theta$. Das sind ebene Polarkoordinaten, mit dem Winkel gegen die $z$-Achse gemessen. Setzt man diesen Abstand
und diese Höhe in die Zylinderkoordinaten ein, entsteht $\vec\Phi$. Der Abstand vom Ursprung ist tatsächlich $r$:

$$\lvert\vec\Phi(r,\theta,\varphi)\rvert^2 = r^2\sin^2\theta\,\big(\cos^2\varphi+\sin^2\varphi\big)+r^2\cos^2\theta = r^2.$$

Umgekehrt erreicht man jeden Punkt $\vec x\neq\vec 0$ der Kugel: $r$ ist sein Abstand vom Ursprung, $\theta$ der Winkel
zwischen $\vec x$ und der positiven $z$-Achse und $\varphi$ der Polarwinkel des Punktes $(x,y)$.
:::

Die Jacobi-Matrix hat als Spalten die Ableitungen nach $r$, $\theta$ und $\varphi$:

$$D\vec\Phi = \begin{pmatrix}\sin\theta\cos\varphi & r\cos\theta\cos\varphi & -r\sin\theta\sin\varphi\\ \sin\theta\sin\varphi & r\cos\theta\sin\varphi & r\sin\theta\cos\varphi\\ \cos\theta & -r\sin\theta & 0\end{pmatrix}, \qquad \det D\vec\Phi = r^2\sin\theta.$$

:::herleitung
**Über die Zylinderkoordinaten.** Kugelkoordinaten sind Zylinderkoordinaten, in die man die ebenen Polarkoordinaten der
Halbebene einsetzt. Mit der Abbildung der Zylinderkoordinaten $\vec\Phi_{\mathrm{Zyl}}$ von oben ist

$$\vec\Phi = \vec\Phi_{\mathrm{Zyl}}\circ\vec\Psi, \qquad \vec\Psi(r,\theta,\varphi) = \big(r\sin\theta,\ \varphi,\ r\cos\theta\big).$$

Nach der Kettenregel aus dem Artikel [Skalarfelder, Vektorfelder und die Jacobi-Matrix](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/skalar-und-vektorfelder-differenzierbarkeit.html) ist die Jacobi-Matrix das Produkt der beiden Jacobi-Matrizen, und die
Determinante eines Produkts ist das Produkt der Determinanten:

$$\det D\vec\Phi(r,\theta,\varphi) = \det D\vec\Phi_{\mathrm{Zyl}}\big(\vec\Psi(r,\theta,\varphi)\big)\cdot\det D\vec\Psi(r,\theta,\varphi) = r\sin\theta\cdot r.$$

Der erste Faktor ist der Zylinderfaktor $\varrho$ an der Stelle $r\sin\theta$. Den zweiten rechnet man aus, entwickelt nach der
mittleren Zeile — die Eins steht dort an der Stelle mit dem Vorzeichen minus:

$$D\vec\Psi = \begin{pmatrix}\sin\theta & r\cos\theta & 0\\ 0&0&1\\ \cos\theta & -r\sin\theta & 0\end{pmatrix}, \qquad \det D\vec\Psi = -\det\begin{pmatrix}\sin\theta & r\cos\theta\\ \cos\theta & -r\sin\theta\end{pmatrix} = r.$$

**Direkt**, entwickelt nach der letzten Zeile von $D\vec\Phi$, kommt dasselbe heraus:

$$\det D\vec\Phi = \cos\theta\cdot r^2\sin\theta\cos\theta+r\sin\theta\cdot r\sin^2\theta = r^2\sin\theta\,\big(\cos^2\theta+\sin^2\theta\big) = r^2\sin\theta.$$

**Im Bild:** In einer Spalte bilden Schalen und Breitenkreise ein Spinnennetz mit dem Flächenfaktor $r$. Dreht man die Spalte
um die Achse, legt ein Punkt im Abstand $r\sin\theta$ von der Achse beim Winkelschritt $d\varphi$ den Bogen $r\sin\theta\,d\varphi$
zurück. Beide Faktoren zusammen ergeben $r^2\sin\theta$.
:::

Für stetiges $f:K_R\to\mathbb{R}$ gilt deshalb

:::formel
$$\begin{aligned}\int_{K_R}f(x,y,z)\,d(x,y,z) &= \int_0^R\int_0^{\pi}\int_0^{2\pi}f\big(\vec\Phi(r,\theta,\varphi)\big)\\ &\qquad\cdot r^2\sin\theta\,d\varphi\,d\theta\,dr.\end{aligned}$$
:::

**So liest man das:** Das Volumenelement in Kugelkoordinaten ist $r^2\sin\theta\,dr\,d\theta\,d\varphi$. In Koordinaten schreibt
man die Jacobi-Determinante auch als

$$\frac{\partial(x,y,z)}{\partial(r,\theta,\varphi)} = r^2\sin\theta.$$

**Im Bild:** Ein Klötzchen der Zwiebel zwischen zwei Schalen, zwei Breitenkreisen und zwei Spalten ist fast ein Quader mit
den Kanten $dr$, dem Meridianbogen $r\,d\theta$ und dem Breitenkreisbogen $r\sin\theta\,d\varphi$. Der Breitenkreis hat nur den
Radius $r\sin\theta$ — an den Polen null, am Äquator $r$ —; deshalb werden die Klötzchen zu den Polen hin schmal.

**Der Haken.** Wie in der Ebene sind die Voraussetzungen des Satzes verletzt: Die ganze Seite des Quaders mit $r=0$ geht auf
den Ursprung, und die beiden Seiten an den Polen — Polarwinkel $0$ und $\pi$ — gehen auf die $z$-Achse. Dort ist die
Determinante null. Die Azimute $0$ und $2\pi$ treffen dieselbe Halbebene. Die Formel gilt trotzdem.

:::herleitung
Wie in der Ebene schneidet man dünne Stücke heraus. Für kleines $\varepsilon>0$ ist $\vec\Phi$ auf dem Quader

$$B_\varepsilon = [\varepsilon,R]\times[\varepsilon,\pi-\varepsilon]\times[\varepsilon,2\pi]$$

injektiv: Der Abstand ist positiv, der Polarwinkel bleibt von den Polen weg, und der Azimut überdeckt weniger als eine volle
Umdrehung. Die Determinante ist dort mindestens $\varepsilon^2\sin\varepsilon$, also positiv, und der Satz gilt auf $B_\varepsilon$.

Dem Bild $\vec\Phi(B_\varepsilon)$ fehlen drei dünne Stücke der Kugel, und jedes passt in einen Körper mit kleinem Volumen:

- die kleine Kugel vom Radius $\varepsilon$ in den Würfel $[-\varepsilon,\varepsilon]^3$;
- der schmale Doppelkegel um die $z$-Achse — Polarwinkel unter $\varepsilon$ oder über $\pi-\varepsilon$ — in den Zylinder vom
  Radius $R\sin\varepsilon$ und der Höhe $2R$, denn dort ist der Abstand zur Achse höchstens $R\sin\varepsilon$;
- der Keil mit dem Azimut zwischen $0$ und $\varepsilon$ in das Prisma der Höhe $2R$ über einem Kreissektor mit dem Winkel
  $\varepsilon$ und dem Radius $R$.

Zusammen haben diese Körper das Volumen

$$8\varepsilon^3+2\pi R^3\sin^2\varepsilon+\varepsilon R^3.$$

Dem Parameterquader fehlen drei Platten mit zusammen höchstens dem Volumen

$$2\pi^2\varepsilon+4\pi R\varepsilon+\pi R\varepsilon.$$

Der Integrand ist links und rechts beschränkt. Die Unterschiede zwischen den Integralen sind deshalb höchstens eine Schranke
mal diese Volumina, sie gehen für $\varepsilon\to0$ gegen null, und aus dem Satz für $B_\varepsilon$ wird die Formel.

**Im Bild:** Man schält aus der Zwiebel den Kern, einen dünnen Stab längs der Achse und eine schmale Spalte heraus. Auf dem
Rest ist alles in Ordnung, und das Herausgeschnittene wird beliebig klein.
:::

::::beispiel Kugel, Schale, Kreisel und Gaußwolke
**(a) Das Kugelvolumen** mit $f=1$: Die drei Integrale trennen sich,

$$\int_0^R\int_0^\pi\int_0^{2\pi}r^2\sin\theta\,d\varphi\,d\theta\,dr = \int_0^{2\pi}d\varphi\cdot\int_0^\pi\sin\theta\,d\theta\cdot\int_0^R r^2\,dr.$$

Das mittlere Integral ist $[-\cos\theta]_0^\pi$, also $2$, und

$$2\pi\cdot2\cdot\frac{R^3}{3} = \frac43\pi R^3$$

— wie mit Cavalieri und mit der Drehbank.

**(b) Eine Kugelschale** zwischen den Radien $R_1$ und $R_2$, mit derselben Begründung:

$$\int_{R_1}^{R_2}\int_0^\pi\int_0^{2\pi}r^2\sin\theta\,d\varphi\,d\theta\,dr = \frac43\pi\big(R_2^3-R_1^3\big).$$

Für eine dünne Schale vom Radius $r$ und der Dicke $\Delta r$ ist das

$$\frac43\pi\big((r+\Delta r)^3-r^3\big) = 4\pi r^2\,\Delta r+4\pi r\,\Delta r^2+\frac43\pi\,\Delta r^3.$$

Bei kleiner Dicke zählt nur der erste Term: Kugeloberfläche $4\pi r^2$ mal Dicke.

**(c) Ein Kreisel.** Eine gleichmäßig gefüllte Vollkugel der Masse $m$ dreht sich um die $z$-Achse. Der Abstand eines Punktes
zur Achse ist $r\sin\theta$, und ihr Trägheitsmoment ist

$$J = \frac{m}{\frac43\pi R^3}\int_{K_R}\big(x^2+y^2\big)\,d(x,y,z) = \frac{3m}{4\pi R^3}\int_0^R\int_0^\pi\int_0^{2\pi}r^2\sin^2\theta\cdot r^2\sin\theta\,d\varphi\,d\theta\,dr.$$

Die drei Integrale sind $2\pi$, $\frac43$ und $\frac{R^5}{5}$, das mittlere wegen

$$\int_0^\pi\sin^3\theta\,d\theta = \int_0^\pi\big(1-\cos^2\theta\big)\sin\theta\,d\theta = \Big[-\cos\theta+\frac{\cos^3\theta}{3}\Big]_0^\pi = \frac43.$$

Zusammen:

$$J = \frac{3m}{4\pi R^3}\cdot2\pi\cdot\frac43\cdot\frac{R^5}{5} = \frac25\,mR^2.$$

Die Kugel ist bei gleicher Masse und gleichem Radius weniger träge als die Walze mit ihrem $\frac12mR^2$, weil mehr von ihrer
Masse nahe der Achse sitzt.

**(d) Die Gaußwolke** $e^{-\lvert\vec x\rvert^2}$, eine räumliche Glocke. Über der Kugel ist

$$\int_{K_R}e^{-(x^2+y^2+z^2)}\,d(x,y,z) = 4\pi\int_0^R r^2e^{-r^2}\,dr.$$

Für $R\to\infty$ gibt partielle Integration, mit dem Gauß-Integral des vorigen Artikels für die halbe Glocke,

$$\int_0^\infty r^2e^{-r^2}\,dr = \Big[-\frac{r}{2}\,e^{-r^2}\Big]_0^\infty+\frac12\int_0^\infty e^{-r^2}\,dr = \frac12\cdot\frac{\sqrt\pi}{2} = \frac{\sqrt\pi}{4}.$$

Das Integral über den ganzen Raum ist also

$$4\pi\cdot\frac{\sqrt\pi}{4} = \pi^{3/2}.$$

Kartesisch, über Würfel $[-R,R]^3$, gibt Fubini das Produkt dreier Gauß-Integrale, $(\sqrt\pi)^3$ — dasselbe, denn die Würfel
liegen zwischen den Kugeln vom Radius $R$ und $\sqrt3\,R$.

**Im Bild:** Bei (a) und (b) zählt jedes Klötzchen der Zwiebel mit $r^2\sin\theta$, bei (c) zusätzlich mit dem Quadrat seines
Abstands zur Achse, bei (d) mit der Dichte der Wolke.
::::

## Singuläre Integranden: die innersten Zwiebelschalen

Das Coulomb-Potential einer Punktladung im Ursprung wird zur Mitte hin beliebig groß; am Ursprung selbst ist es nicht
definiert. Ein Integral über eine Kugel um die Ladung ist deshalb zunächst nicht erklärt. Man schneidet eine kleine Kugel um
den Ursprung heraus und lässt sie schrumpfen: Für eine stetige Funktion $f:\mathbb{R}^3\setminus\{\vec 0\}\to\mathbb{R}$ setzt man

$$\int_{K_R}f(\vec x)\,d^3x := \lim_{\varepsilon\searrow0}\int_{\{\varepsilon\le\lvert\vec x\rvert\le R\}}f(\vec x)\,d^3x,$$

wenn der Grenzwert existiert. Auf jeder Kugelschale ist $f$ stetig und damit integrierbar; die Frage ist nur, ob die Integrale
zur Mitte hin zur Ruhe kommen. Existiert auch der Grenzwert für $\lvert f\rvert$, heißt das Integral __absolut konvergent__.

**Die Akteure:** eine solche Funktion $f$, eine Konstante $c>0$ und ein Exponent $\alpha<3$ mit

$$\lvert f(\vec x)\rvert\le\frac{c}{\lvert\vec x\rvert^{\alpha}} \quad\text{für alle } \vec x\neq\vec 0.$$

Die rechte Seite heißt __Majorante__ — eine einfache radiale Funktion, die $f$ von oben begrenzt. Dann existiert für jedes
$R>0$ das Integral von $f$ über $K_R$, sogar absolut, und

:::formel Satz
$$\int_{K_R}\lvert f(\vec x)\rvert\,d^3x \le \frac{4\pi c}{3-\alpha}\,R^{3-\alpha}.$$
:::

**So liest man das:** Eine Singularität im Ursprung schadet nicht, solange sie schwächer ist als $\lvert\vec x\rvert^{-3}$. Das
ist ein __Majorantenkriterium__ wie bei Reihen: Ist die Majorante integrierbar, dann auch $f$.

**Im Bild:** Die Zwiebel. Eine dünne Schale vom Radius $r$ und der Dicke $dr$ hat etwa das Volumen $4\pi r^2\,dr$, und der
Integrand ist dort höchstens $c\,r^{-\alpha}$. Ihr Beitrag ist also höchstens $4\pi c\,r^{2-\alpha}\,dr$: Zur Mitte hin wächst der
Integrand, aber die Schalen schrumpfen wie $r^2$. Für $\alpha<3$ gewinnen die Schalen.

:::herleitung
**Schritt 1: die Majorante selbst.** In Kugelkoordinaten — auf der Kugelschale gilt die Formel mit derselben Begründung wie
auf der Kugel — ist für $0<\varepsilon<R$

$$\int_{\{\varepsilon\le\lvert\vec x\rvert\le R\}}\frac{c}{\lvert\vec x\rvert^{\alpha}}\,d^3x = \int_\varepsilon^R\int_0^{\pi}\int_0^{2\pi}\frac{c}{r^{\alpha}}\,r^2\sin\theta\,d\varphi\,d\theta\,dr = 4\pi c\int_\varepsilon^R r^{2-\alpha}\,dr.$$

Weil der Exponent $2-\alpha$ größer als $-1$ ist, hat $r^{2-\alpha}$ die Stammfunktion $\frac{r^{3-\alpha}}{3-\alpha}$, und

$$4\pi c\int_\varepsilon^R r^{2-\alpha}\,dr = \frac{4\pi c}{3-\alpha}\big(R^{3-\alpha}-\varepsilon^{3-\alpha}\big) \le \frac{4\pi c}{3-\alpha}\,R^{3-\alpha}.$$

**Schritt 2: eine Cauchy-Folge.** Für $0<\varepsilon<R$ sei

$$s(\varepsilon) := \int_{\{\varepsilon\le\lvert\vec x\rvert\le R\}}f(\vec x)\,d^3x,$$

und $(\varepsilon_k)$ sei eine Nullfolge. Für $\varepsilon_k<\varepsilon_\ell$ unterscheiden sich $s(\varepsilon_k)$ und
$s(\varepsilon_\ell)$ nur um das Integral über die dünne Schale zwischen den beiden Radien. Mit der Monotonie des Integrals und
der Rechnung aus Schritt 1 folgt

$$\big\lvert s(\varepsilon_k)-s(\varepsilon_\ell)\big\rvert \le \int_{\{\varepsilon_k\le\lvert\vec x\rvert\le\varepsilon_\ell\}}\lvert f(\vec x)\rvert\,d^3x \le 4\pi c\int_{\varepsilon_k}^{\varepsilon_\ell}r^{2-\alpha}\,dr \le \frac{4\pi c}{3-\alpha}\,\varepsilon_\ell^{\,3-\alpha}.$$

Die rechte Seite geht gegen null, wenn die Radien es tun. Die Folge $s(\varepsilon_k)$ ist also eine Cauchy-Folge und
konvergiert. Mischt man zwei Nullfolgen zu einer, sieht man, dass der Grenzwert nicht von der Folge abhängt. Dasselbe gilt für
$\lvert f\rvert$ statt $f$, und die Schranke aus Schritt 1 bleibt im Grenzwert erhalten.

**Im Bild:** Die innersten Zwiebelschalen tragen fast nichts bei. Die Schale zwischen zwei kleinen Radien hat ein so kleines
Volumen, dass auch der große Integrand dort wenig ausmacht.
:::

:::grafik
Szene: hoema3/koordinatentransformationen/02-zwiebelschalen · Vorlage: schalen-summe-3d
Eine aufgeschnittene Zwiebel um den Ursprung, deren Schalen sich nach innen jeweils im Radius halbieren. Daneben ein
Balkendiagramm: pro Schale der Beitrag „Integrand mal Schalenvolumen" für die Majorante $c\,r^{-\alpha}$, darüber die laufende
Summe. Ein Regler für $\alpha$: Unter $3$ schrumpfen die Balken nach innen geometrisch, und die Summe nähert sich einem festen
Wert; bei $\alpha=3$ trägt jede Schale gleich viel bei, und die Summe wächst ohne Grenze. Kernaussage: Die winzigen inneren
Schalen zähmen jede Singularität, die schwächer als $r^{-3}$ ist. (Rot = Schalen, orange = Beiträge, blau = laufende Summe,
grau = Achsen.)
:::

::::beispiel Coulomb-Potential und Coulomb-Feld
Das Coulomb-Potential der Einheitsladung, oft $\varphi$ geschrieben, heißt hier $g$, weil $\varphi$ schon der Azimut ist:

$$g(\vec x) = \frac{1}{4\pi\lvert\vec x\rvert}.$$

Es erfüllt die Voraussetzung des Satzes mit der Konstante $\frac{1}{4\pi}$ und dem Exponenten $1$. In Kugelkoordinaten ist

$$\int_{\{\varepsilon\le\lvert\vec x\rvert\le R\}}g\,d^3x = \int_\varepsilon^R\frac{1}{4\pi r}\cdot4\pi r^2\,dr = \frac{R^2-\varepsilon^2}{2},$$

und für $\varepsilon\to0$ bleibt $\frac{R^2}{2}$. Die Schranke des Satzes wird hier genau erreicht, weil $g$ selbst die Majorante
ist:

$$\frac{4\pi c}{3-\alpha}\,R^{3-\alpha} = \frac{4\pi}{4\pi\cdot2}\,R^2 = \frac{R^2}{2}.$$

**Das Coulomb-Feld.** Nach dem Artikel über Gradienten und radialsymmetrische Felder ist

$$\nabla g(\vec x) = -\frac{\vec x}{4\pi\lvert\vec x\rvert^3}, \qquad \lvert\partial_jg(\vec x)\rvert\le\frac{1}{4\pi\lvert\vec x\rvert^2},$$

denn jede Komponente von $\vec x$ ist betragsmäßig höchstens $\lvert\vec x\rvert$. Die partiellen Ableitungen erfüllen die
Voraussetzung also mit dem Exponenten $2$, und der Satz gibt

$$\int_{K_R}\lvert\partial_jg\rvert\,d^3x \le \frac{4\pi}{4\pi\cdot1}\,R = R.$$

**Im Bild:** Das Potential wächst zur Mitte hin wie $\frac1r$, die Zwiebelschalen schrumpfen wie $r^2$; ihr Produkt geht wie $r$
gegen null. Beim Feld bleibt das Produkt beschränkt: Jede Schale der Dicke $dr$ trägt höchstens $dr$ bei, zusammen höchstens $R$.
::::

## Warum die Schwelle bei der Dimension liegt

Die Drei im Satz ist die Raumdimension. Entscheidend ist, wie schnell die Schalen um den Nullpunkt mit ihrem Radius
schrumpfen. Auf der Zahlengeraden besteht die „Schale" vom Radius $r$ aus zwei Punkten, in der Ebene ist sie ein Kreis der
Länge $2\pi r$, im Raum eine Kugeloberfläche der Größe $4\pi r^2$. Für die Potenzen des Abstands gibt das

$$\int_{\{\varepsilon\le\lvert x\rvert\le R\}}\frac{dx}{\lvert x\rvert^{\alpha}} = 2\int_\varepsilon^R r^{-\alpha}\,dr, \qquad \int_{\{\varepsilon\le\lvert\vec x\rvert\le R\}}\frac{d^2x}{\lvert\vec x\rvert^{\alpha}} = 2\pi\int_\varepsilon^R r^{1-\alpha}\,dr, \qquad \int_{\{\varepsilon\le\lvert\vec x\rvert\le R\}}\frac{d^3x}{\lvert\vec x\rvert^{\alpha}} = 4\pi\int_\varepsilon^R r^{2-\alpha}\,dr.$$

Diese Integrale bleiben für $\varepsilon\to0$ genau dann beschränkt, wenn $\alpha$ kleiner als die Dimension ist: auf der
Geraden kleiner als $1$, in der Ebene kleiner als $2$, im Raum kleiner als $3$.

**Im Bild:** Je mehr Dimensionen, desto schneller verschwinden die inneren Schalen, und desto stärkere Singularitäten verkraftet
das Integral.

:::herleitung
**Die drei Gleichungen.** Auf der Geraden besteht die Menge aus den Intervallen $[-R,-\varepsilon]$ und $[\varepsilon,R]$, die
aus Symmetrie dasselbe beitragen. In der Ebene rechnet man mit Polarkoordinaten auf dem Kreisring wie im vorigen Artikel; der
Winkel gibt den Faktor $2\pi$. Im Raum geben Kugelkoordinaten auf der Schale die Faktoren $2\pi$ und $2$.

**Wann ein radiales Integral beschränkt bleibt.** Für einen Exponenten $\beta$ ist

$$\int_\varepsilon^R r^{\beta}\,dr = \frac{R^{\beta+1}-\varepsilon^{\beta+1}}{\beta+1} \quad\text{für } \beta\neq-1, \qquad \int_\varepsilon^R\frac{dr}{r} = \ln\frac{R}{\varepsilon}.$$

Ist $\beta$ größer als $-1$, geht $\varepsilon^{\beta+1}$ gegen null, und das Integral bleibt beschränkt. Ist $\beta$ kleiner als
$-1$, wächst $\varepsilon^{\beta+1}$ über alle Grenzen, und bei $\beta=-1$ tut es der Logarithmus. In der Dimension $n$ ist der
Exponent $n-1-\alpha$, und die Bedingung, dass er größer als $-1$ ist, heißt: $\alpha$ ist kleiner als $n$.
:::

::::beispiel An der Schwelle und darüber
**(a) Genau an der Schwelle.** Für den Exponenten $3$ ist

$$\int_{\{\varepsilon\le\lvert\vec x\rvert\le1\}}\frac{d^3x}{\lvert\vec x\rvert^3} = 4\pi\int_\varepsilon^1\frac{dr}{r} = 4\pi\ln\frac1\varepsilon.$$

Das wächst langsam, aber ohne Grenze:

$$\varepsilon = 10^{-3}:\ \ 4\pi\ln10^3\approx86{,}8, \qquad \varepsilon = 10^{-6}:\ \ 4\pi\ln10^6\approx173{,}6.$$

Jede weitere Schale mit halbem Radius bringt denselben Betrag $4\pi\ln2\approx8{,}7$ hinzu.

**(b) Die Feldenergie einer Punktladung.** In den Einheiten des Artikels über Gradienten — ohne die Feldkonstante — hat eine
Punktladung $q$ im Ursprung das Feld

$$\vec E(\vec x) = \frac{q}{4\pi\lvert\vec x\rvert^2}\,\vec e_r,$$

mit dem Einheitsvektor $\vec e_r$, der vom Ursprung weg zeigt. Die Energiedichte des Felds ist $\frac12\lvert\vec E\rvert^2$. Sie
wächst zur Mitte hin wie die vierte Potenz des Kehrwerts des Abstands, also über der Schwelle. In der Schale zwischen
$\varepsilon$ und $R$ steckt die Energie

$$\int_{\{\varepsilon\le\lvert\vec x\rvert\le R\}}\frac12\lvert\vec E\rvert^2\,d^3x = 4\pi\int_\varepsilon^R\frac{q^2}{32\pi^2r^4}\,r^2\,dr = \frac{q^2}{8\pi}\Big(\frac1\varepsilon-\frac1R\Big).$$

Für $\varepsilon\to0$ wächst sie über alle Grenzen: Eine wirklich punktförmige Ladung hätte unendliche Feldenergie — ein
bekanntes Problem der klassischen Elektrodynamik. Mit der Feldkonstante ändert sich nur ein Vorfaktor.

**(c) In der Ebene** liegt die Schwelle schon bei $2$. Dort ist $\lvert\vec x\rvert^{-1}$ noch integrierbar,
$\lvert\vec x\rvert^{-2}$ nicht mehr:

$$\int_{\{\varepsilon\le\lvert\vec x\rvert\le1\}}\frac{d^2x}{\lvert\vec x\rvert} = 2\pi\,(1-\varepsilon), \qquad \int_{\{\varepsilon\le\lvert\vec x\rvert\le1\}}\frac{d^2x}{\lvert\vec x\rvert^2} = 2\pi\ln\frac1\varepsilon.$$

Was im Raum harmlos ist, ist in der Ebene schon zu stark.

**Im Bild:** Bei (a) trägt jede Zwiebelschale mit halbem Radius gleich viel bei, und unendlich viele gleiche Beiträge ergeben
unendlich viel. Bei (b) wächst der Integrand schneller, als die Schalen schrumpfen. Bei (c) schrumpfen die Ringe in der Ebene
nur wie $r$, nicht wie $r^2$.
::::

## Bedeutung und Ausblick

Zylinder- und Kugelkoordinaten machen Volumenintegrale über symmetrische Körper zu Integralen über Quader, in denen sich die
Variablen oft trennen. In der Elektrotechnik sind sie die Arbeitspferde für Leiter und Koaxialkabel (Zylinder) und für
Punktladungen, geladene Kugeln und Strahlungsfelder (Kugel) — immer mit dem Volumenfaktor, der so leicht vergessen wird.

Der Satz über singuläre Integranden ist der Schlüssel zum nächsten Artikel. Dort entsteht das Potential einer ganzen
Ladungsverteilung als Integral über lauter Coulomb-Potentiale, eines für jeden Ort der Ladung — das __Newtonpotential__. Dass
dieses Integral trotz der Singularität jedes Summanden existiert, sichert genau die Abschätzung dieses Abschnitts.

:::kern
- Der __Transformationssatz__ gilt im Raum: $\int_{\vec\Phi(B)}f\,d^3x=\int_B f(\vec\Phi)\,\lvert\det D\vec\Phi\rvert\,d^3u$ — jedes Klötzchen zählt mit seinem Volumenfaktor.
- __Zylinderkoordinaten__ sind Polarkoordinaten plus unverzerrte Höhe; das Volumenelement ist $\varrho\,d\varrho\,d\varphi\,dz$ (Baumstamm).
- __Rotationskörper__: Das Volumen ist das Integral der Querschnitte, $\mathrm{vol}(W)=\pi\int_a^b p(z)^2\,dz$ (Drehbank).
- __Kugelkoordinaten__: Das Volumenelement ist $r^2\sin\theta\,dr\,d\theta\,d\varphi$ — Schalendicke mal Meridianbogen mal Breitenkreisbogen (Zwiebel).
- Kugelkoordinaten sind Zylinderkoordinaten nach Polarkoordinaten in der Halbebene; ihre Volumenfaktoren multiplizieren sich.
- Am Ursprung, auf der Achse und an der Naht sind die Voraussetzungen verletzt; die Formeln gelten trotzdem, weil die herausgeschnittenen Stücke beliebig klein werden.
- __Singuläre Integranden__ mit einer Majorante $c/\lvert\vec x\rvert^{\alpha}$ sind über Kugeln integrierbar, wenn der Exponent unter $3$ liegt — die innersten Zwiebelschalen sind winzig.
- Die Schwelle ist die Dimension: auf der Geraden $1$, in der Ebene $2$, im Raum $3$; genau an der Schwelle wächst das Integral logarithmisch.
- Coulomb-Potential und Coulomb-Feld sind im Raum integrierbar, die Feldenergiedichte einer Punktladung nicht.
:::

:::quiz
F: Was besagt der Transformationssatz im Raum, und was bedeutet er im Bild des Gummiklotzes?
A: Ist $\vec\Phi$ stetig differenzierbar, auf dem regulären Bereich $B$ injektiv mit $\det D\vec\Phi\neq0$ und $\vec\Phi(B)$ wieder regulär, so ist $\int_{\vec\Phi(B)}f\,d^3x=\int_B f(\vec\Phi(\vec u))\,\lvert\det D\vec\Phi(\vec u)\rvert\,d^3u$. Jedes Klötzchen des verformten Klotzes ist unter der Lupe ein Parallelotop mit dem Würfelvolumen mal $\lvert\det D\vec\Phi\rvert$. Das Ellipsoid mit den Halbachsen $1$, $2$, $3$ hat deshalb das Sechsfache des Volumens der Einheitskugel, $8\pi$.
F: Warum ist der Volumenfaktor der Zylinderkoordinaten $\varrho$, und warum heißt der Abstand zur Achse hier nicht $r$?
A: Zylinderkoordinaten sind Polarkoordinaten der $xy$-Ebene mit unverzerrter Höhe; entwickelt man die Determinante nach der letzten Zeile, bleibt die der Polarkoordinaten, $\varrho$. Ein Klötzchen des Baumstamms hat die Kanten $d\varrho$, $\varrho\,d\varphi$ und $dz$. Der Buchstabe $r$ ist in diesem Artikel der Abstand vom Ursprung; deshalb heißt der Abstand von der Achse $\varrho$, wie in der Elektrotechnik üblich.
F: Wie viel Kupfer steckt in einem Rohr, und warum hängt das Trägheitsmoment einer Walze nicht von ihrer Länge ab?
A: Das Rohr hat das Volumen $\pi(R_2^2-R_1^2)H$; bei $7$ und $8\,\mathrm{mm}$ Radius und $1\,\mathrm{m}$ Länge sind das etwa $47\,\mathrm{cm}^3$, gut $400\,\mathrm{g}$ Kupfer. Die Walze hat $J=\frac{m}{\pi R^2H}\int\varrho^2\,dV=\frac{mR^2}{2}$: Sie ist ein Stapel gleicher Scheiben, jede mit ihrer Masse mal dem halben Radiusquadrat, und die Länge kürzt sich heraus.
F: Wie entsteht die Volumenformel für Rotationskörper, und warum fällt die Ableitung des Profils heraus?
A: Die verallgemeinerten Zylinderkoordinaten $(t\,p(z)\cos\varphi,\ t\,p(z)\sin\varphi,\ z)$ mit $t\in[0,1]$ haben die Determinante $t\,p(z)^2$. Die letzte Zeile der Jacobi-Matrix ist $(0,0,1)$, und $p'$ steht nur in der dritten Spalte, die bei der Entwicklung wegfällt — sie beschreibt eine Scherung. Die Integrale über $t$ und $\varphi$ geben $\frac12\cdot2\pi=\pi$, übrig bleibt $\pi\int_a^b p(z)^2\,dz$.
F: Was ergeben Kegel, runder Laib und Kugel mit der Rotationskörper-Formel?
A: Der Kegel mit dem Profil $\frac{R}{h}z$ hat das Volumen $\frac{\pi R^2h}{3}$; an der Spitze integriert man erst ab einer kleinen Höhe $\delta$. Der Laib mit $p(z)^2=1-z$ auf $[0,1]$ hat $\frac{\pi}{2}$, wie mit Scheiben, Cavalieri und Polarkoordinaten. Die Kugel mit $p(z)^2=R^2-z^2$ hat $\frac43\pi R^3$.
F: Woher kommt der Faktor $r^2\sin\theta$ in Kugelkoordinaten?
A: Ein Klötzchen der Zwiebel hat die Kanten $dr$, den Meridianbogen $r\,d\theta$ und den Breitenkreisbogen $r\sin\theta\,d\varphi$, denn der Breitenkreis hat nur den Radius $r\sin\theta$. Rechnerisch sind Kugelkoordinaten Zylinderkoordinaten nach ebenen Polarkoordinaten in der Halbebene; nach der Kettenregel multiplizieren sich die Determinanten $\varrho=r\sin\theta$ und $r$.
F: Warum gelten die Formeln für Zylinder- und Kugelkoordinaten, obwohl die Voraussetzungen des Satzes verletzt sind?
A: Am Ursprung, auf der $z$-Achse und an der Naht des Azimuts ist $\vec\Phi$ nicht injektiv oder die Determinante null. Auf einem etwas kleineren Quader gilt der Satz; es fehlen nur ein Kern, ein dünner Stab um die Achse und eine schmale Spalte, die in Würfel, Zylinder und Prismen mit beliebig kleinem Volumen passen. Weil der Integrand beschränkt ist, verschwinden die Unterschiede für $\varepsilon\to0$.
F: Wie berechnet man das Trägheitsmoment einer Vollkugel und das Integral der Gaußwolke?
A: Mit dem Abstand $r\sin\theta$ zur Achse ist $J=\frac{3m}{4\pi R^3}\int r^2\sin^2\theta\cdot r^2\sin\theta=\frac{3m}{4\pi R^3}\cdot2\pi\cdot\frac43\cdot\frac{R^5}{5}=\frac25mR^2$, weniger als bei der Walze. Die Gaußwolke $e^{-\lvert\vec x\rvert^2}$ gibt $4\pi\int_0^\infty r^2e^{-r^2}\,dr=4\pi\cdot\frac{\sqrt\pi}{4}=\pi^{3/2}$ — dasselbe wie $(\sqrt\pi)^3$ über Würfel.
F: Was besagt der Satz über singuläre Integranden, und wie beweist man ihn?
A: Ist $f$ stetig auf $\mathbb{R}^3\setminus\{\vec 0\}$ mit $\lvert f(\vec x)\rvert\le c/\lvert\vec x\rvert^{\alpha}$ und $\alpha<3$, so existiert $\int_{K_R}f$ als Grenzwert der Integrale über die Schalen $\{\varepsilon\le\lvert\vec x\rvert\le R\}$, sogar absolut, und $\int_{K_R}\lvert f\rvert\le\frac{4\pi c}{3-\alpha}R^{3-\alpha}$. In Kugelkoordinaten ist das Integral der Majorante $4\pi c\int r^{2-\alpha}\,dr$; die Schalenintegrale bilden eine Cauchy-Folge, weil die dünne Schale zwischen zwei kleinen Radien höchstens $\frac{4\pi c}{3-\alpha}\varepsilon^{3-\alpha}$ beiträgt.
F: Warum liegt die Schwelle bei $3$, und was folgt für Coulomb-Potential, Coulomb-Feld und Feldenergie?
A: Die Schalen schrumpfen im Raum wie $r^2$, deshalb wird aus $r^{-\alpha}$ der radiale Integrand $r^{2-\alpha}$, der für $\alpha<3$ integrierbar ist; bei $\alpha=3$ wächst $4\pi\ln\frac1\varepsilon$ ohne Grenze, in der Ebene liegt die Schwelle bei $2$, auf der Geraden bei $1$. Das Potential $\frac{1}{4\pi\lvert\vec x\rvert}$ hat über $K_R$ das Integral $\frac{R^2}{2}$, das Feld wächst nur wie $\lvert\vec x\rvert^{-2}$ und ist ebenfalls integrierbar. Die Energiedichte wächst wie $\lvert\vec x\rvert^{-4}$: Eine Punktladung hätte unendliche Feldenergie.
:::
