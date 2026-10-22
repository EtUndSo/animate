---
title: Das Poincaré-Lemma
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030300
summary: Von Grund auf – wann die verschwindende Rotation doch ein Potential garantiert. Leitbild ist ein Aussichtsturm, von dem aus man jeden Punkt des Geländes sieht (Sterngebiet). Dort wird aus „wirbelfrei" ein Gradientenfeld und aus „quellenfrei" ein Wirbelfeld, und die Beweise liefern die Potentiale gleich mit, als Arbeit auf der Sichtlinie vom Turm. Mit harmonischen Feldern, dem Treppenweg als Rechenmethode, Eindeutigkeit, Eichfreiheit und einer Beispiel-Seite.
tags: Poincaré-Lemma, Sterngebiet, einfach zusammenhängend, Skalarpotential, Vektorpotential, Integrabilitätsbedingung, Potentialkonstruktion, Eichfreiheit
---

## Anschaulich

Der vorige Artikel endete mit einer offenen Frage. Ein Höhenmesser — ein Potential — verlangt, dass der Wind nicht
wirbelt: Die Rotation muss null sein. Umgekehrt reicht das aber nicht. Die Wendeltreppe wirbelt nirgends und hat trotzdem
kein Potential, weil man um die Säule in der Mitte herumfahren kann.

**Das Leitbild dieses Artikels:** ein Gelände mit einem **Aussichtsturm**, von dem aus man jeden Punkt sieht. Keine Säule
steht einer Sichtlinie im Weg. Solche Gelände heißen __Sterngebiete__. Auf ihnen gilt das __Poincaré-Lemma__: Ein Wind ohne
Wirbel hat dort immer einen Höhenmesser. Und man kann ihn sogar bauen — die Höhe eines Punkts ist die Arbeit des Winds auf
der Sichtlinie vom Turm dorthin.

Das Lemma hat ein Spiegelbild. Eine Strömung ohne Quellen ist auf einem Sterngebiet immer der Wirbel einer anderen
Strömung, eines __Vektorpotentials__ — auch dieses entsteht aus Sichtlinien vom Turm. In der Elektrotechnik sind das die
beiden Potentiale der Feldtheorie: Das elektrostatische Feld ist wirbelfrei und hat ein Skalarpotential, das Magnetfeld
ist quellenfrei und hat ein Vektorpotential.

:::grafik
Szene: hoema3/kurvenintegrale/03-aussichtsturm · Vorlage: sterngebiet-sichtlinien-2d
Links ein Gelände mit einem Aussichtsturm im Punkt $\vec x_0$; von dort fächern gerade Sichtlinien zu allen Punkten aus, alle
ganz im Gelände. Über einem wirbelfreien Windfeld wird längs jeder Sichtlinie die Arbeit gemessen und als Höhe über dem
Endpunkt aufgetragen — so wächst die Landschaft des Potentials. Rechts die gelochte Ebene mit der Säule der Wendeltreppe:
Von jedem Turm aus verdeckt die Säule einen Punkt, eine Sichtlinie fehlt. Kernaussage: Wo man vom Turm aus alles sieht,
macht Wirbelfreiheit aus dem Wind ein Steigungsfeld. (Rot = Gelände und Potential, orange = Sichtlinien, blau = Feld, grau =
Säule.)
:::

## Sterngebiete: ein Turm, der alles sieht

**Die Akteure:** Eine offene Menge $G\subseteq\mathbb{R}^n$ mit $n\ge2$ heißt __Sterngebiet__, wenn es einen Punkt
$\vec x_0\in G$ gibt, von dem aus die Strecke zu jedem anderen Punkt von $G$ ganz in $G$ liegt:

:::formel Definition
$$\vec x_0+t\,(\vec x-\vec x_0)\in G \qquad\text{für alle } \vec x\in G \text{ und alle } t\in[0,1].$$
:::

**So liest man das:** Zur Zeit null steht man am Turm $\vec x_0$, zur Zeit eins am Punkt $\vec x$; dazwischen läuft man
geradeaus.
Der Turm heißt __Zentrum__ des Sterngebiets. Ein Sterngebiet ist insbesondere ein Gebiet im Sinne des vorigen Artikels —
je zwei Punkte verbindet man über das Zentrum.

**Im Bild:** Vom Turm aus sieht man jeden Punkt des Geländes, ohne dass etwas die Sicht versperrt. Ein Gelände, das von
jedem seiner Punkte aus alles sieht, heißt __konvex__ — etwa eine Kugel oder ein Quader. Konvexe Gelände sind
Sterngebiete mit beliebigem Turm.

::::beispiel Sterngebiet oder nicht?
**(a) Eine Kugel** $B_R(\vec c)$ ist konvex. Liegen $\vec x_0$ und $\vec x$ darin, so ist nach der Dreiecksungleichung

$$\big\lvert\vec x_0+t(\vec x-\vec x_0)-\vec c\big\rvert \le (1-t)\,\lvert\vec x_0-\vec c\rvert+t\,\lvert\vec x-\vec c\rvert < R,$$

die ganze Strecke liegt also in der Kugel.

**(b) Ein Kreuz.** Die Menge der Punkte im offenen Quadrat $(-3,3)^2$, deren erste **oder** zweite Koordinate betragsmäßig
kleiner als $1$ ist, ist ein Sterngebiet mit dem Zentrum $\vec 0$: Gehört ein Punkt zum waagerechten Balken, so auch jeder
Punkt der Strecke vom Ursprung zu ihm, denn die zweite Koordinate schrumpft dabei nur — beim senkrechten Balken ebenso.
Konvex ist das Kreuz nicht: Die Punkte $(2,\tfrac12)$ und $(\tfrac12,2)$ gehören dazu, ihr Mittelpunkt $(\tfrac54,\tfrac54)$
nicht.

**(c) Die gelochte Ebene** $\mathbb{R}^2\setminus\{\vec 0\}$ ist kein Sterngebiet. Für jeden möglichen Turm $\vec c\neq\vec 0$
gehört auch $-\vec c$ zur Menge, aber die Strecke von $\vec c$ nach $-\vec c$ läuft bei $t=\tfrac12$ durch den Ursprung.

**(d) Die geschlitzte Ebene**, also die Ebene ohne die Halbgerade der Punkte $(x,0)$ mit $x\le0$, ist ein Sterngebiet mit
dem Turm $(1,0)$. Liegt der Zielpunkt oberhalb oder unterhalb der $x$-Achse, so trifft die Strecke vom Turm die Achse nur
im Turm selbst, also bei positivem $x$. Liegt er auf der positiven $x$-Achse, läuft die Strecke ganz auf ihr.

**Im Bild:** Bei (c) verdeckt die Säule immer einen Punkt hinter ihr. Schneidet man das Gelände wie bei (d) längs einer
Halbgeraden auf, sieht ein Turm auf der anderen Seite alles — um die Säule herumfahren kann man dann aber nicht mehr.

:::grafik
Szene: hoema3/kurvenintegrale/03-sterngebiete · Vorlage: sterngebiet-sichtlinien-2d
Vier Gelände nebeneinander, jeweils mit einem Turm und seinen Sichtlinien: die Kugel (Turm beliebig verschiebbar, alle
Sichtlinien bleiben drin), das Kreuz (Turm im Ursprung sieht alles, eine Strecke zwischen zwei Balkenenden verlässt das
Kreuz), die gelochte Ebene (eine Sichtlinie läuft durch die Säule), die geschlitzte Ebene (Turm bei $(1,0)$ sieht alles, der
Schlitz versperrt den Weg um die Säule). Kernaussage: Ein Sterngebiet braucht nur einen Turm, der alles sieht — konvex muss
es nicht sein. (Rot = Gelände, orange = Sichtlinien, grau = Säule und Schlitz.)
:::
::::

## Wirbelfrei heißt Gradientenfeld

**Die Akteure:** ein Sterngebiet $G\subseteq\mathbb{R}^n$, hier mit dem Turm im Ursprung, und ein stetig differenzierbares
Vektorfeld $\vec F:G\to\mathbb{R}^n$, das die __Integrabilitätsbedingung__ aus dem Gradienten-Artikel erfüllt:

$$\frac{\partial F_j}{\partial x_k} = \frac{\partial F_k}{\partial x_j} \qquad\text{für alle } j,k.$$

In zwei und drei Dimensionen heißt das: Die Rotation ist null. Dann ist $\vec F$ ein Gradientenfeld, und ein Potential
lässt sich direkt angeben. Es heißt hier $\varphi$; im vorigen Artikel hieß es $h$.

:::formel Lemma
$$\vec F(\vec x) = \nabla\varphi(\vec x), \qquad \varphi(\vec x) := \int_0^1\vec F(t\vec x)\cdot\vec x\,dt.$$
:::

**So liest man das:** $\varphi(\vec x)$ ist das Kurvenintegral von $\vec F$ längs der Sichtlinie

$$\vec y(t) = t\,\vec x, \qquad \dot{\vec y}(t) = \vec x, \qquad t\in[0,1],$$

vom Turm zum Punkt $\vec x$. Eingabe ist ein Punkt, Ausgabe eine Zahl — die Höhe.

**Im Bild:** Der Höhenmesser wird gebaut, indem man auf jeder Sichtlinie die Arbeit des Winds misst. Dass diese Höhen zu
einer Landschaft zusammenpassen, deren Steigungsfeld der Wind ist, liegt an der Wirbelfreiheit: Rückt der Zielpunkt ein
wenig zur Seite, dreht sich die Sichtlinie mit — und ohne Wirbel ändert sich die Arbeit dabei genau um den Wind am Ziel mal
Verschiebung.

:::herleitung
Für einen Punkt $\vec x\in G$ liegt die ganze Sichtlinie in $G$, ebenso für alle Punkte in einer kleinen Kugel um $\vec x$.
Der Integrand ist dort in $\vec x$ stetig differenzierbar, also darf man unter dem Integral ableiten (Artikel über
Parameterintegrale). Die $k$-te partielle Ableitung des Integranden gibt mit der Produktregel und der Kettenregel

$$\frac{\partial}{\partial x_k}\sum_{j=1}^n F_j(t\vec x)\,x_j = \sum_{j=1}^n t\,\frac{\partial F_j}{\partial x_k}(t\vec x)\,x_j+F_k(t\vec x).$$

**Jetzt wirkt die Wirbelfreiheit.** Nach der Integrabilitätsbedingung darf man $\partial F_j/\partial x_k$ durch
$\partial F_k/\partial x_j$ ersetzen. Dann steht in der Summe die Ableitung von $F_k$ längs der Sichtlinie:

$$\sum_{j=1}^n\frac{\partial F_k}{\partial x_j}(t\vec x)\,x_j = \frac{d}{dt}\,F_k(t\vec x).$$

Der ganze Integrand ist damit eine volle Ableitung nach $t$, nach der Produktregel:

$$t\,\frac{d}{dt}F_k(t\vec x)+F_k(t\vec x) = \frac{d}{dt}\Big(t\,F_k(t\vec x)\Big).$$

Der Hauptsatz liefert

$$\frac{\partial\varphi}{\partial x_k}(\vec x) = \Big[t\,F_k(t\vec x)\Big]_{t=0}^{t=1} = F_k(\vec x).$$

Die Rechnung gilt in jeder Dimension. Nur im ersten Schritt nach der Produktregel wurde die Wirbelfreiheit gebraucht.
:::

::::beispiel Potentiale vom Turm aus
**(a) Das Sattelfeld** in der Ebene,

$$\vec F(x,y) = (y,\ x),$$

erfüllt die Integrabilitätsbedingung, denn beide gemischten Ableitungen sind $1$. Auf der Sichtlinie ist

$$\vec F(t\vec x)\cdot\vec x = (ty,\ tx)\cdot(x,\ y) = 2txy, \qquad \varphi(x,y) = \int_0^1 2txy\,dt = xy.$$

**(b) Ein Feld im Raum.**

$$\vec F(x,y,z) = (2xy,\ x^2+z^2,\ 2yz)$$

ist wirbelfrei:

$$\operatorname{rot}\vec F = \big(2z-2z,\ 0-0,\ 2x-2x\big) = \vec 0.$$

Auf der Sichtlinie sammelt der Integrand überall den Faktor $t^2$:

$$\vec F(t\vec x)\cdot\vec x = t^2\big(2x^2y+(x^2+z^2)\,y+2yz^2\big) = 3t^2\big(x^2y+yz^2\big),$$

$$\varphi(x,y,z) = \int_0^1 3t^2\big(x^2y+yz^2\big)\,dt = x^2y+yz^2.$$

Probe:

$$\nabla\varphi = \big(2xy,\ x^2+z^2,\ 2yz\big) = \vec F.$$

**Im Bild:** In beiden Fällen misst man die Arbeit auf der geraden Strecke vom Ursprung zum Punkt — und erhält eine
Landschaft, deren Steigungsfeld genau der gegebene Wind ist.
::::

## Quellenfrei heißt Wirbelfeld

Das Spiegelbild im $\mathbb{R}^3$: Ein Vektorfeld $\vec B$ heißt nach dem Rechenregeln-Artikel __Wirbelfeld__ oder
Rotationsfeld, wenn es die Rotation eines anderen Felds $\vec A$ ist, des __Vektorpotentials__. Dort wurde gezeigt, dass
Wirbelfelder quellenfrei sind. Auf einem Sterngebiet gilt auch die Umkehrung.

**Die Akteure:** ein Sterngebiet $G\subseteq\mathbb{R}^3$ mit dem Turm im Ursprung und ein stetig differenzierbares,
quellenfreies Vektorfeld $\vec B:G\to\mathbb{R}^3$, also mit verschwindender Divergenz. Dann ist $\vec B$ ein Wirbelfeld mit
dem Vektorpotential

:::formel Lemma
$$\vec B(\vec x) = \operatorname{rot}\vec A(\vec x), \qquad \vec A(\vec x) := \int_0^1\vec B(t\vec x)\times t\vec x\,dt.$$
:::

**So liest man das:** Wieder läuft man die Sichtlinie vom Turm zum Punkt ab. Statt des Windanteils in Fahrtrichtung sammelt
man diesmal das Kreuzprodukt des Felds mit dem Hebelarm $t\vec x$ vom Turm. Eingabe ist ein Punkt, Ausgabe ein Vektor.

**Im Bild:** Eine Strömung ohne Quellen — nirgends sprudelt Wasser hervor, nirgends versickert es — lässt sich als
Wirbelbild einer zweiten Strömung lesen. Das Kreuzprodukt mit dem Hebelarm erinnert an ein Drehmoment: Es baut aus dem Feld
längs der Sichtlinie das Kreisen auf, dessen Wirbel das Feld ist.

:::herleitung
Man leitet wieder unter dem Integral ab, jetzt mit der Rotation. Bei festem $t$ ist der Integrand das Kreuzprodukt der
Felder

$$\vec U(\vec x) = \vec B(t\vec x), \qquad \vec V(\vec x) = t\,\vec x.$$

Die Produktregel für die Rotation eines Kreuzprodukts aus dem Rechenregeln-Artikel braucht vier Bausteine:

$$\operatorname{div}\vec V = 3t, \qquad \operatorname{div}\vec U = t\,(\operatorname{div}\vec B)(t\vec x) = 0, \qquad (\vec U\cdot\nabla)\vec V = t\,\vec B(t\vec x), \qquad (\vec V\cdot\nabla)\vec U = t^2\,\frac{d}{dt}\vec B(t\vec x).$$

Die letzte Gleichung folgt aus der Kettenregel, denn $(\vec V\cdot\nabla)\vec U$ ist die Summe der Terme
$t\,x_j\cdot t\,(\partial_j\vec B)(t\vec x)$, und die Summe der $x_j\,(\partial_j\vec B)(t\vec x)$ ist die Ableitung nach $t$.
Eingesetzt in die Produktregel:

$$\operatorname{rot}(\vec U\times\vec V) = \vec U\operatorname{div}\vec V-\vec V\operatorname{div}\vec U+(\vec V\cdot\nabla)\vec U-(\vec U\cdot\nabla)\vec V = 3t\,\vec B(t\vec x)+t^2\frac{d}{dt}\vec B(t\vec x)-t\,\vec B(t\vec x).$$

Das ist wieder eine volle Ableitung nach $t$:

$$2t\,\vec B(t\vec x)+t^2\,\frac{d}{dt}\vec B(t\vec x) = \frac{d}{dt}\Big(t^2\,\vec B(t\vec x)\Big),$$

und der Hauptsatz gibt

$$\operatorname{rot}\vec A(\vec x) = \Big[t^2\,\vec B(t\vec x)\Big]_{t=0}^{t=1} = \vec B(\vec x).$$

Hier wurde die Quellenfreiheit an genau einer Stelle gebraucht: Sie lässt den Term mit $\operatorname{div}\vec U$
verschwinden.
:::

::::beispiel Vektorpotentiale vom Turm aus
**(a) Ein homogenes Magnetfeld.** Für das überall gleiche Feld

$$\vec B = (0,\ 0,\ 2)$$

ist der Integrand $t\,\vec B\times\vec x$, und mit dem Integral von $t$ über $[0,1]$:

$$\vec A(\vec x) = \frac12\,\vec B\times\vec x = \frac12\,(-2y,\ 2x,\ 0) = (-y,\ x,\ 0).$$

Das ist genau das kreisende Vektorpotential aus dem Rechenregeln-Artikel. Allgemein liefert die Formel für jedes homogene
Feld das Potential $\tfrac12\,\vec B\times\vec x$.

**(b) Eine Sattelströmung.**

$$\vec B(x,y,z) = (x,\ -y,\ 0), \qquad \operatorname{div}\vec B = 1-1 = 0.$$

Auf der Sichtlinie ist $\vec B(t\vec x)$ gleich $t\,\vec B(\vec x)$, der Integrand also

$$t^2\,\vec B(\vec x)\times\vec x = t^2\,(-yz,\ -xz,\ 2xy), \qquad \vec A(\vec x) = \frac13\,(-yz,\ -xz,\ 2xy).$$

Probe:

$$\operatorname{rot}\vec A = \frac13\,\big(2x-(-x),\ -y-2y,\ -z-(-z)\big) = (x,\ -y,\ 0) = \vec B.$$

**Im Bild:** Bei (a) wirbelt das kreisende Potential um die $z$-Achse und erzeugt das gleichmäßige Feld. Bei (b) strömt das
Wasser längs der $y$-Achse heran und längs der $x$-Achse ab, ohne irgendwo zu entspringen — und ist trotzdem der Wirbel
einer anderen, verdrehten Strömung.
::::

## Quell- und wirbelfrei: harmonische Felder

Ist ein Feld zugleich quellen- **und** wirbelfrei, so ist es noch spezieller: Für ein zweimal stetig differenzierbares
$\vec F$ auf einem Sterngebiet im $\mathbb{R}^3$ mit verschwindender Divergenz und Rotation gilt komponentenweise die
Laplace-Gleichung,

$$\Delta\vec F = \vec 0.$$

Man nennt $\vec F$ dann __harmonisch__.

**Im Bild:** Weder sprudelt die Strömung, noch dreht sie ein Schaufelrad. Nach dem Divergenz-Artikel ist jede Komponente
dann im Gleichgewicht: Ihr Wert ist genau das Mittel der Nachbarwerte.

:::herleitung
Nach dem ersten Teil ist $\vec F=\nabla\varphi$, und weil $\vec F$ zweimal stetig differenzierbar ist, ist $\varphi$ es
dreimal. Die Quellenfreiheit macht $\varphi$ harmonisch:

$$\Delta\varphi = \operatorname{div}\nabla\varphi = \operatorname{div}\vec F = 0.$$

Weil die Ableitungen vertauschen (Schwarz), ist dann auch

$$\Delta\vec F = \Delta\nabla\varphi = \nabla\Delta\varphi = \vec 0.$$
:::

::::beispiel Die Staupunktströmung
Die Sattelströmung

$$\vec B(x,y,z) = (x,\ -y,\ 0)$$

war quellenfrei. Sie ist auch wirbelfrei — jede Komponente hängt nur von ihrer eigenen Koordinate ab. Ihr Potential vom
Turm im Ursprung:

$$\vec B(t\vec x)\cdot\vec x = t\,(x^2-y^2), \qquad \varphi(x,y,z) = \int_0^1 t\,(x^2-y^2)\,dt = \frac{x^2-y^2}{2}.$$

Es ist harmonisch, und das Feld als lineares Feld ohnehin:

$$\Delta\varphi = 1-1 = 0, \qquad \Delta\vec B = \vec 0.$$

**Im Bild:** Das ist die ebene __Staupunktströmung__ — Wasser strömt längs der $y$-Achse heran, prallt im Ursprung auf eine
Wand längs der $x$-Achse und fließt zu beiden Seiten an ihr entlang ab. Sie hat ein Skalarpotential und ein Vektorpotential
zugleich.
::::

## Das Poincaré-Lemma

**Turm an beliebiger Stelle.** Steht der Turm nicht im Ursprung, sondern bei $\vec x_0$, ersetzt man die Sichtlinie durch
die Strecke von $\vec x_0$ nach $\vec x$:

$$\varphi(\vec x) = \int_0^1\vec F\big(\vec x_0+t(\vec x-\vec x_0)\big)\cdot(\vec x-\vec x_0)\,dt, \qquad \vec A(\vec x) = \int_0^1\vec B\big(\vec x_0+t(\vec x-\vec x_0)\big)\times t\,(\vec x-\vec x_0)\,dt.$$

:::herleitung
Man verschiebt das Gelände so, dass der Turm im Ursprung steht: Das Feld $\vec x\mapsto\vec F(\vec x_0+\vec x)$ ist auf der
verschobenen Menge definiert, die ein Sterngebiet mit dem Zentrum $\vec 0$ ist, und hat dieselben Ableitungen, also auch
verschwindende Rotation bzw. Divergenz. Die Formeln mit dem Turm im Ursprung, angewandt auf dieses Feld und zurückgeschoben,
sind die angegebenen.
:::

Zusammen mit den notwendigen Bedingungen aus dem Artikel über
[Rechenregeln und Identitäten](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/rechenregeln-div-rot-identitaeten.html)
ergibt sich der Satz.

:::formel Satz
$$\vec F \text{ Gradientenfeld} \iff \operatorname{rot}\vec F = \vec 0, \qquad\qquad \vec F \text{ Wirbelfeld} \iff \operatorname{div}\vec F = 0.$$
:::

**So liest man das:** Das gilt für stetig differenzierbare Vektorfelder auf Sterngebieten im $\mathbb{R}^3$ (bei der zweiten
Äquivalenz mit einem zweimal stetig differenzierbaren Vektorpotential, wie im Rechenregeln-Artikel). Die Konstruktion des
Skalarpotentials klappt auf Sterngebieten in jeder Dimension, sobald die Integrabilitätsbedingung erfüllt ist.

**Im Bild:** Wo ein Turm alles sieht, gibt es keine Säule, um die eine Wendeltreppe laufen könnte. Dann ist „wirbelfrei"
schon dasselbe wie „hat einen Höhenmesser", und „quellenfrei" dasselbe wie „ist ein Wirbelbild".

:::herleitung
**Von links nach rechts** sind das die Identitäten aus dem Rechenregeln-Artikel: Gradientenfelder wirbeln nicht, Wirbelfelder
quellen nicht. Für $\vec F=\nabla\varphi$ mit stetig differenzierbarem $\vec F$ ist $\varphi$ zweimal stetig differenzierbar,
und die Rotation verschwindet nach Schwarz. Für $\vec F=\operatorname{rot}\vec A$ mit zweimal stetig differenzierbarem
$\vec A$ ist die Divergenz null.

**Von rechts nach links** liefern die beiden Formeln des Lemmas die Potentiale, mit dem Turm des Sterngebiets als Startpunkt.
:::

**Lokal gilt es immer.** Jeder Punkt einer offenen Menge hat eine kleine Kugel um sich, und Kugeln sind Sterngebiete. Ein
wirbelfreies Feld hat also um jeden Punkt herum ein Potential — auch die Wendeltreppe. Erst wenn man um eine Säule
herumfahren kann, kann es global scheitern.

::::beispiel Die aufgeschnittene Wendeltreppe
Die Wendeltreppe

$$\vec W(x,y) = \frac{1}{x^2+y^2}\,(-y,\ x)$$

ist auf der gelochten Ebene wirbelfrei, aber nicht konservativ. Auf der geschlitzten Ebene — ohne die Halbgerade der
Punkte $(x,0)$ mit $x\le0$ — ist sie es doch: Das ist ein Sterngebiet mit dem Turm $(1,0)$, und das Poincaré-Lemma liefert
ein Potential. Es ist der Polarwinkel mit Werten zwischen $-\pi$ und $\pi$.

:::herleitung
Der Polarwinkel $\theta$ mit Werten zwischen $-\pi$ und $\pi$ lässt sich auf drei Halbebenen, die zusammen die geschlitzte
Ebene überdecken, durch Arcustangens-Ausdrücke schreiben:

$$\theta = \arctan\frac{y}{x}\ \ (x>0), \qquad \theta = \frac{\pi}{2}-\arctan\frac{x}{y}\ \ (y>0), \qquad \theta = -\frac{\pi}{2}-\arctan\frac{x}{y}\ \ (y<0).$$

Alle drei haben den Gradienten $\vec W$ — für den ersten steht die Rechnung im vorigen Artikel, für die beiden anderen
genauso:

$$\frac{\partial}{\partial x}\Big(-\arctan\frac xy\Big) = -\frac{y}{x^2+y^2}, \qquad \frac{\partial}{\partial y}\Big(-\arctan\frac xy\Big) = \frac{x}{x^2+y^2}.$$

Also ist $\theta$ auf der geschlitzten Ebene ein Potential von $\vec W$. Zwei Potentiale unterscheiden sich auf einem Gebiet
nur um eine Konstante (siehe unten), und im Turm $(1,0)$ sind beide null — das Potential des Lemmas ist also der
Polarwinkel.
:::

Eine Rundtour in der geschlitzten Ebene kann den Ursprung nicht umrunden — sie müsste den Schlitz kreuzen —, und sie bringt
deshalb die Arbeit null.

**Im Bild:** Schneidet man die Wendeltreppe längs einer Halbgeraden auf, ist sie ein ganz normaler, ansteigender Hang. Erst
wer über den Schnitt hinweg weiterläuft, landet eine Etage höher — und genau diesen Weg hat man durch das Aufschneiden
verboten.
::::

## Potentiale praktisch berechnen: der Treppenweg

Die Formel des Lemmas ist ein Kurvenintegral längs der Sichtlinie. Weil ein Gradientenfeld konservativ ist, darf man aber
jeden anderen Weg nehmen — oft ist ein **Treppenweg** längs der Koordinatenachsen bequemer, wie im vorigen Artikel.

**Die Akteure:** ein stetig differenzierbares, wirbelfreies Feld $\vec F$ auf einer Kugel $B_R(\vec x_0)\subseteq\mathbb{R}^3$
um den Punkt $\vec x_0$ mit den Koordinaten $x_0,y_0,z_0$. Dann ist

:::formel Lemma
$$\varphi(x,y,z) = \int_{x_0}^{x}F_1(t,y_0,z_0)\,dt+\int_{y_0}^{y}F_2(x,t,z_0)\,dt+\int_{z_0}^{z}F_3(x,y,t)\,dt$$
:::

ein Potential von $\vec F$ auf der Kugel.

**So liest man das:** Erst läuft man in $x$-Richtung, dann in $y$-Richtung, zuletzt in $z$-Richtung. Auf jeder Stufe zählt
nur die eine Komponente des Felds in Laufrichtung, und die schon erreichten Koordinaten stehen fest.

**Im Bild:** Statt geradeaus vom Turm zum Ziel zu laufen, nimmt man drei achsenparallele Treppenabsätze. Bei einem
Höhenmesser ist das egal — die Höhe hängt nur vom Ziel ab.

:::grafik
Szene: hoema3/kurvenintegrale/03-treppenweg · Vorlage: tetraeder-schichtung-3d
Eine Kugel um $\vec x_0$ mit einem Zielpunkt $(x,y,z)$. Zwei Wege vom Mittelpunkt zum Ziel: die gerade Sichtlinie und der
Treppenweg aus drei achsenparallelen Stücken, erst in $x$-, dann in $y$-, dann in $z$-Richtung. Auf jeder Stufe leuchtet die
zuständige Feldkomponente auf; beide Arbeitszähler enden beim selben Wert. Der Treppenweg bleibt sichtbar ganz in der
Kugel. Kernaussage: Bei einem Gradientenfeld darf man den bequemsten Weg nehmen. (Blau = Feld, orange = Wege, rot = Ziel,
grau = Kugel.)
:::

:::herleitung
Nach dem Poincaré-Lemma ist $\vec F$ auf der Kugel ein Gradientenfeld, also konservativ. Das Potential mit dem Wert $0$ im
Mittelpunkt ist dann die Arbeit auf **jedem** Weg vom Mittelpunkt zum Punkt $(x,y,z)$, der in der Kugel bleibt.

**Der Treppenweg bleibt in der Kugel.** Seine Punkte haben die Form

$$(t,\ y_0,\ z_0), \qquad (x,\ t,\ z_0), \qquad (x,\ y,\ t),$$

mit $t$ jeweils zwischen dem Start- und dem Zielwert der Koordinate. Ihr Abstand vom Mittelpunkt ist deshalb höchstens der
Abstand des Ziels, weil in jeder Koordinate die Abweichung höchstens die des Ziels ist — die noch nicht gelaufenen
Koordinaten weichen gar nicht ab.

**Die drei Stufen.** Auf der ersten läuft man mit der Geschwindigkeit $(1,0,0)$, der Integrand ist $F_1(t,y_0,z_0)$; auf der
zweiten und dritten entsprechend $F_2$ und $F_3$. Die Additivität der Etappen gibt die Summe. Bei einem Gebiet, das keine
Kugel ist, muss man nachprüfen, ob der Treppenweg darin bleibt.
:::

::::beispiel Ein Potential über den Treppenweg
Für das Feld auf ganz $\mathbb{R}^3$

$$\vec F(x,y,z) = \big(y^2\cos x,\ 2y\sin x+e^{2z},\ 2y\,e^{2z}\big)$$

verschwindet die Rotation:

$$\operatorname{rot}\vec F = \big(2e^{2z}-2e^{2z},\ 0-0,\ 2y\cos x-2y\cos x\big) = \vec 0.$$

Mit dem Start im Ursprung braucht man die Komponenten auf den drei Stufen:

$$F_1(t,0,0) = 0, \qquad F_2(x,t,0) = 2t\sin x+1, \qquad F_3(x,y,t) = 2y\,e^{2t}.$$

Die erste Stufe fällt also weg, und

$$\varphi(x,y,z) = \int_0^y\big(2t\sin x+1\big)\,dt+2y\int_0^z e^{2t}\,dt = y^2\sin x+y+y\big(e^{2z}-1\big) = y^2\sin x+y\,e^{2z}.$$

Probe:

$$\nabla\varphi = \big(y^2\cos x,\ 2y\sin x+e^{2z},\ 2y\,e^{2z}\big) = \vec F.$$

**Im Bild:** Auf dem Treppenweg sind die Integrale elementar. Die Sichtlinie vom Ursprung führte dagegen auf Integranden mit
$\sin(tx)$ und $e^{2tz}$ — dasselbe Ergebnis, mehr Arbeit.
::::

## Eindeutigkeit und Eichfreiheit

**Skalarpotentiale sind bis auf eine Konstante eindeutig.** Auf einem Gebiet $G$ haben zwei stetig differenzierbare
Funktionen $g,h$ genau dann denselben Gradienten, wenn sich sie nur um eine Konstante unterscheiden:

$$\nabla g = \nabla h \quad\Longleftrightarrow\quad g-h = \text{konstant}.$$

**Im Bild:** Man darf die ganze Landschaft anheben oder absenken, die Steigungen bleiben dieselben. Welcher Punkt die Höhe
null hat, ist Vereinbarung — etwa der Standort des Turms.

:::herleitung
Von rechts nach links: Der Gradient einer Konstanten ist null. Von links nach rechts: Die Differenz $g-h$ hat den Gradienten
$\vec 0$. Man fixiert einen Punkt $\vec x_0\in G$ und verbindet ihn mit einem beliebigen $\vec x\in G$ durch eine Kurve —
das geht, weil $G$ ein Gebiet ist. Nach dem ersten Hauptsatz ist

$$(g-h)(\vec x)-(g-h)(\vec x_0) = \int_\gamma\nabla(g-h)\cdot d\vec x = 0.$$

Die Differenz hat also überall denselben Wert wie in $\vec x_0$.
:::

**Vektorpotentiale sind viel freier.** Mit $\vec A$ ist auch $\vec A+\nabla\psi$ ein Vektorpotential desselben Felds, für
jedes zweimal stetig differenzierbare Skalarfeld $\psi$, denn Gradientenfelder wirbeln nicht — das ist die
__Eichfreiheit__ aus dem Rechenregeln-Artikel:

$$\operatorname{rot}\big(\vec A+\nabla\psi\big) = \operatorname{rot}\vec A.$$

Oft verlangt man zusätzlich ein quellenfreies Vektorpotential, die __Coulomb-Eichung__. Ist $\vec A'$ irgendein
Vektorpotential, so addiert man ein Gradientenfeld $\nabla\psi$, dessen Potential die __Poisson-Gleichung__

$$\Delta\psi = -\operatorname{div}\vec A'$$

löst. Ob sie lösbar ist, klärt erst der Artikel
[Poisson-Gleichung und Hauptsatz der Vektoranalysis](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum/poisson-gleichung-und-hauptsatz-der-vektoranalysis.html).

:::herleitung
Die Rotation des Gradientenfelds verschwindet, also bleibt das Feld dasselbe. Für die Divergenz des neuen Potentials gilt

$$\operatorname{div}\big(\vec A'+\nabla\psi\big) = \operatorname{div}\vec A'+\Delta\psi = \operatorname{div}\vec A'-\operatorname{div}\vec A' = 0.$$

Der Rechenregeln-Artikel schreibt dasselbe mit umgekehrtem Vorzeichen von $\psi$.
:::

::::beispiel Anderer Turm, andere Konstante
**(a) Skalarpotential.** Für das Feld aus dem Treppenweg-Beispiel mit dem Start im Punkt $(0,1,0)$ statt im Ursprung lauten die
drei Stufen

$$\int_0^x F_1(t,1,0)\,dt = \sin x, \qquad \int_1^y F_2(x,t,0)\,dt = (y^2-1)\sin x+y-1, \qquad \int_0^z F_3(x,y,t)\,dt = y\big(e^{2z}-1\big).$$

Zusammen:

$$\tilde\varphi(x,y,z) = y^2\sin x+y\,e^{2z}-1.$$

Das ist das Potential von vorhin minus $1$ — genau dessen Wert im neuen Startpunkt.

**(b) Vektorpotential.** Das homogene Feld $(0,0,2)$ hat vom Turm aus das Vektorpotential $(-y,x,0)$. Addiert man den
Gradienten der Sattelfläche,

$$(-y,\ x,\ 0)+\nabla(xy) = (0,\ 2x,\ 0),$$

so erhält man das zweite Vektorpotential aus dem Rechenregeln-Artikel, mit derselben Rotation.

**Im Bild:** Ein anderer Turm verschiebt die ganze Landschaft um eine Konstante. Ein anderes Vektorpotential ist eine ganz
andere Strömung — kreisend statt scherend —, die aber denselben Wirbel trägt.
::::

## Bedeutung und Ausblick

Das Poincaré-Lemma ist die Grundlage der Potentiale in der Elektrotechnik. In der Elektrostatik ist das elektrische Feld
wirbelfrei, auf jedem Sterngebiet — etwa dem ganzen Raum — hat es also ein Potential. In der Magnetostatik ist das
Magnetfeld quellenfrei und hat ein Vektorpotential. Die Beweise sind konstruktiv: Man kann die Potentiale wirklich
ausrechnen, längs Sichtlinien oder Treppenwegen.

Auf Gebieten mit Löchern gilt das Lemma nur lokal, wie die Wendeltreppe zeigt. Was dann über Rundtouren übrig bleibt, klärt
der nächste Artikel: Kurvenintegrale wirbelfreier Felder ändern sich nicht, wenn man den Weg stetig verformt
(__Homotopieinvarianz__). Wie oft eine Rundtour die Säule umrundet, ist dann alles, was zählt — das ist der Inhalt des
__zweiten Hauptsatzes__ für Kurvenintegrale.

:::kern
- Ein __Sterngebiet__ hat einen Turm, von dem aus die Strecke zu jedem Punkt im Gebiet liegt; Kugeln und Quader sind Beispiele, die gelochte Ebene nicht.
- __Poincaré-Lemma__: Auf Sterngebieten ist ein wirbelfreies Feld ein Gradientenfeld und ein quellenfreies Feld ein Wirbelfeld.
- Das Skalarpotential ist die Arbeit auf der Sichtlinie vom Turm: $\varphi(\vec x)=\int_0^1\vec F(t\vec x)\cdot\vec x\,dt$.
- Das Vektorpotential sammelt Feld mal Hebelarm auf der Sichtlinie: $\vec A(\vec x)=\int_0^1\vec B(t\vec x)\times t\vec x\,dt$.
- In beiden Beweisen macht die Wirbel- bzw. Quellenfreiheit den Integranden zu einer vollen Ableitung nach $t$.
- Quell- und wirbelfreie Felder sind __harmonisch__: $\Delta\vec F=\vec 0$.
- **Lokal** gilt das Lemma immer; global scheitert es nur, wenn man um ein Loch herumfahren kann.
- Praktisch rechnet man das Potential auf einem **Treppenweg** längs der Achsen aus.
- Skalarpotentiale sind bis auf eine Konstante eindeutig, Vektorpotentiale bis auf ein Gradientenfeld (__Eichfreiheit__).
:::

:::quiz
F: Was ist ein Sterngebiet, und warum ist die gelochte Ebene keines, die geschlitzte Ebene aber schon?
A: Eine offene Menge mit einem Zentrum, von dem aus die gerade Strecke zu jedem Punkt ganz in der Menge liegt — ein Turm, der alles sieht. In der gelochten Ebene läuft die Strecke von jedem Turm $\vec c$ zum Punkt $-\vec c$ durch den Ursprung. In der geschlitzten Ebene sieht der Turm $(1,0)$ alles, weil Strecken von ihm die negative $x$-Achse nie treffen.
F: Wie lautet die Potentialformel des Poincaré-Lemmas, und was bedeutet sie im Bild?
A: $\varphi(\vec x)=\int_0^1\vec F(t\vec x)\cdot\vec x\,dt$ ist das Kurvenintegral längs der Sichtlinie $\vec y(t)=t\vec x$ vom Turm im Ursprung zum Punkt. Man baut den Höhenmesser, indem man auf jeder Sichtlinie die Arbeit des Winds misst.
F: An welcher Stelle braucht der Beweis die Wirbelfreiheit, und was bewirkt sie?
A: Nach der Produktregel enthält $\partial\varphi/\partial x_k$ die Summe $\sum_j t\,\partial_kF_j(t\vec x)\,x_j$. Die Integrabilitätsbedingung erlaubt, $\partial_kF_j$ durch $\partial_jF_k$ zu ersetzen; dann ist die Summe $t\frac{d}{dt}F_k(t\vec x)$, und der ganze Integrand wird zur vollen Ableitung $\frac{d}{dt}(tF_k(t\vec x))$. Der Hauptsatz gibt $F_k(\vec x)$.
F: Welches Potential liefert die Formel für $\vec F=(2xy,\,x^2+z^2,\,2yz)$?
A: Das Feld ist wirbelfrei. Auf der Sichtlinie ist der Integrand $3t^2(x^2y+yz^2)$, das Integral über $t$ also $x^2y+yz^2$, und die Probe $\nabla\varphi=\vec F$ stimmt.
F: Wie entsteht das Vektorpotential eines quellenfreien Felds, und was liefert es für ein homogenes Magnetfeld?
A: $\vec A(\vec x)=\int_0^1\vec B(t\vec x)\times t\vec x\,dt$ sammelt Feld mal Hebelarm längs der Sichtlinie. Mit der Produktregel für die Rotation eines Kreuzprodukts und der Quellenfreiheit wird der Integrand zu $\frac{d}{dt}(t^2\vec B(t\vec x))$. Für ein homogenes Feld ist $\vec A=\frac12\vec B\times\vec x$, für $(0,0,2)$ also das kreisende $(-y,x,0)$.
F: Warum ist ein quell- und wirbelfreies Feld harmonisch, und welches Beispiel zeigt das?
A: Es ist $\vec F=\nabla\varphi$ mit $\Delta\varphi=\operatorname{div}\vec F=0$; weil die Ableitungen vertauschen, ist $\Delta\vec F=\nabla\Delta\varphi=\vec 0$. Die Staupunktströmung $(x,-y,0)$ ist quell- und wirbelfrei, hat das harmonische Potential $\frac{x^2-y^2}{2}$ und zugleich das Vektorpotential $\frac13(-yz,-xz,2xy)$.
F: Was besagt das Poincaré-Lemma als Satz, und in welchem Sinn gilt es lokal immer?
A: Für stetig differenzierbare Felder auf Sterngebieten im $\mathbb{R}^3$ gilt: Gradientenfeld genau dann, wenn die Rotation verschwindet; Wirbelfeld genau dann, wenn die Divergenz verschwindet. Jeder Punkt einer offenen Menge hat eine Kugel um sich, und Kugeln sind Sterngebiete — also hat ein wirbelfreies Feld um jeden Punkt ein Potential, auch die Wendeltreppe.
F: Warum hat die Wendeltreppe auf der geschlitzten Ebene ein Potential, auf der gelochten aber nicht?
A: Die geschlitzte Ebene ist ein Sterngebiet mit dem Turm $(1,0)$; dort liefert das Lemma ein Potential, den Polarwinkel zwischen $-\pi$ und $\pi$. Eine Rundtour um den Ursprung müsste den Schlitz kreuzen und ist dort nicht möglich. In der gelochten Ebene kann man die Säule umrunden und gewinnt $2\pi$ — ein Potential ist ausgeschlossen.
F: Wie berechnet man ein Potential mit dem Treppenweg, und warum bleibt der Weg in der Kugel?
A: Man integriert nacheinander $F_1$ in $x$-Richtung, $F_2$ in $y$-Richtung und $F_3$ in $z$-Richtung, jeweils mit den schon erreichten Koordinaten. Beim Feld $(y^2\cos x,\,2y\sin x+e^{2z},\,2ye^{2z})$ ergibt das $y^2\sin x+ye^{2z}$. Jeder Punkt des Treppenwegs weicht in jeder Koordinate höchstens so weit vom Mittelpunkt ab wie das Ziel, liegt also nicht weiter weg.
F: Wie eindeutig sind Skalar- und Vektorpotentiale?
A: Zwei Skalarpotentiale unterscheiden sich auf einem Gebiet um eine Konstante: Ihre Differenz hat den Gradienten null, und nach dem ersten Hauptsatz ist sie längs jeder Kurve konstant — der Start in $(0,1,0)$ statt im Ursprung verschiebt das Potential $y^2\sin x+ye^{2z}$ um $1$. Zu einem Vektorpotential darf man jedes Gradientenfeld addieren, weil es nicht wirbelt (Eichfreiheit); mit $\Delta\psi=-\operatorname{div}\vec A'$ erreicht man die Coulomb-Eichung.
:::
