---
title: Differentialoperatoren in krummlinigen Koordinaten
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3040400
summary: Von Grund auf – wie Gradient, Divergenz und Laplace-Operator in Polar-, Zylinder- und Kugelkoordinaten aussehen. Leitbild sind Wegweiser auf dem Globus – „Osten" zeigt in Aachen woandershin als in Tokio, und ein Längengrad ist in Aachen nur 70 km breit. Die Wegweiser sind die normierten Koordinatenvektorfelder, die Kilometer pro Grad die Maßfaktoren $h_u=\lvert\partial_u\vec\Phi\rvert$. Mit dem Gradienten $\sum\frac{1}{h_u}\partial_u f\,\vec e_u$, der Divergenz als Spur der Jacobi-Matrix, den allgemeinen Formeln für orthogonale Koordinaten und den Laplace-Operatoren in Zylinder- und Kugelkoordinaten. Mit Beispiel-Seite.
tags: krummlinige Koordinaten, Maßfaktoren, orthogonale Koordinaten, Gradient, Divergenz, Laplace-Operator, Zylinderkoordinaten, Kugelkoordinaten
---

## Anschaulich

In einer **Schachbrettstadt** mit geraden Straßen zeigt „Osten" überall in dieselbe Richtung, und „zwei Blocks nach Osten" ist
überall dieselbe Strecke. Auf einem **Globus** ist das anders: „Osten" zeigt in Aachen in eine andere Richtung als in Tokio,
und ein Längengrad ist am Äquator 111 km breit, in Aachen nur 70 km, am Nordpol gar nichts.

**Das Leitbild dieses Artikels:** **Wegweiser auf dem Globus**. An jedem Ort steht ein Wegweiser mit drei Armen — nach oben,
nach Süden, nach Osten —, und neben jedem Arm steht, wie viele Kilometer ein Schritt der Koordinate dort bedeutet. Die Arme
sind die __normierten Koordinatenvektorfelder__, die Kilometer pro Schritt die __Maßfaktoren__.

Weil sich die Wegweiser von Ort zu Ort drehen und die Maßfaktoren sich ändern, sehen Gradient, Divergenz und
Laplace-Operator in Kugel- oder Zylinderkoordinaten anders aus als kartesisch. Ein Gefälle misst man pro Kilometer, nicht pro
Grad — deshalb teilt der Gradient durch den Maßfaktor. Und wer die Divergenz ausrechnet, muss mitzählen, dass sich die Arme
der Wegweiser mitdrehen: Daher stammen die Zusatzterme.

:::grafik
Szene: hoema3/koordinatentransformationen/04-wegweiser-globus · Vorlage: lokales-dreibein-3d
Links eine Schachbrettstadt mit gleichen Wegweisern an jeder Kreuzung, rechts ein Globus mit Wegweisern aus drei Pfeilen —
radial nach außen, nach Süden, nach Osten — an mehreren Orten. Fährt man einen Ort mit der Maus über den Globus, dreht sich
sein Wegweiser mit; ein Zähler zeigt, wie viele Kilometer ein Grad nach Osten und ein Grad nach Süden dort sind, und der
Ost-Wert schrumpft zum Pol hin auf null. Kernaussage: In krummlinigen Koordinaten drehen sich die Richtungen mit, und die
Maßfaktoren übersetzen Koordinatenschritte in echte Längen. (Blau = Wegweiser, orange = Maßfaktoren, grau = Gitter.)
:::

## Koordinatensysteme und ihre Wegweiser

**Die Akteure:** eine offene Menge $U\subseteq\mathbb{R}^3$ und eine stetig differenzierbare, injektive Abbildung
$\vec\Phi:U\to\mathbb{R}^3$, die nirgends flachdrückt:

$$\vec\Phi(u,v,w) = \big(x(u,v,w),\ y(u,v,w),\ z(u,v,w)\big), \qquad \det D\vec\Phi\neq0.$$

Dann ist $(u,v,w)$ ein __krummliniges Koordinatensystem__: Jeder Punkt von $\vec\Phi(U)$ hat genau ein Koordinatentripel. Hält man
zwei Koordinaten fest und lässt die dritte laufen, entsteht eine __Koordinatenlinie__ — auf dem Globus ein Meridian, ein
Breitenkreis oder ein Strahl nach außen.

Die partiellen Ableitungen $\partial_u\vec\Phi$, $\partial_v\vec\Phi$ und $\partial_w\vec\Phi$ — die Gitterpfeile aus dem ersten
Artikel, die Spalten der Jacobi-Matrix — heißen __natürliche Koordinatenvektorfelder__. Sie liegen tangential an den
Koordinatenlinien. Ihre Längen und ihre Richtungen bekommen eigene Namen:

:::formel Definition
$$h_u = \big\lvert\partial_u\vec\Phi\big\rvert, \qquad \vec e_u = \frac{1}{h_u}\,\partial_u\vec\Phi, \qquad\text{ebenso für } v \text{ und } w.$$
:::

**So liest man das:** Der __Maßfaktor__ $h_u$ sagt, wie lang ein Schritt der Koordinate $u$ ist: Der Schritt $du$ bewegt den
Punkt um ungefähr $h_u\,du$. Das __normierte Koordinatenvektorfeld__ $\vec e_u$ zeigt in die Richtung, in die der Punkt dabei
läuft, und hat die Länge $1$. Üblich ist auch $\hat e_u$; hier tragen alle Vektoren einen Pfeil.

**Im Bild:** Der Wegweiser am Ort $\vec\Phi(u,v,w)$ hat die drei Arme $\vec e_u$, $\vec e_v$ und $\vec e_w$, und neben jedem Arm steht
sein Maßfaktor — Kilometer pro Koordinatenschritt.

Anders als kartesische Koordinatenvektoren **drehen sich** die Wegweiser mit dem Ort, denn die Koordinatenlinien sind krumm.
Bilden sie an jedem Punkt eine Orthonormalbasis — paarweise senkrecht, jeweils der Länge $1$ —, heißt das Koordinatensystem
__orthogonal__. Zylinder- und Kugelkoordinaten sind orthogonal. Dann lässt sich jedes Vektorfeld $\vec F$ in den Wegweisern
zerlegen, mit den Komponenten

$$F_u = \vec F\cdot\vec e_u, \qquad F_v = \vec F\cdot\vec e_v, \qquad F_w = \vec F\cdot\vec e_w,$$

und es gilt

$$\vec F = F_u\,\vec e_u+F_v\,\vec e_v+F_w\,\vec e_w.$$

Das Volumenelement eines orthogonalen Systems ist das Produkt der Maßfaktoren:

$$\big\lvert\det D\vec\Phi\big\rvert = h_u\,h_v\,h_w.$$

:::herleitung
**Die Zerlegung.** In einer Orthonormalbasis ist jeder Vektor die Summe seiner Schatten auf die Basisvektoren: Setzt man den
Ansatz mit unbekannten Koeffizienten an und multipliziert mit $\vec e_u$, bleibt wegen der Orthonormalität nur der Koeffizient
von $\vec e_u$ stehen, und der ist $\vec F\cdot\vec e_u$.

**Das Volumenelement.** Die Spalten der Jacobi-Matrix sind $h_u\vec e_u$, $h_v\vec e_v$ und $h_w\vec e_w$. Die Determinante ist
linear in jeder Spalte, und eine Matrix mit orthonormalen Spalten hat die Determinante $1$ oder $-1$:

$$\big\lvert\det D\vec\Phi\big\rvert = h_u\,h_v\,h_w\,\big\lvert\det\big(\vec e_u\,\big|\,\vec e_v\,\big|\,\vec e_w\big)\big\rvert = h_u\,h_v\,h_w.$$

**Im Bild:** Ein Klötzchen zwischen den Koordinatenflächen ist fast ein Quader mit den Kanten $h_u\,du$, $h_v\,dv$ und $h_w\,dw$ —
die Volumenfaktoren aus dem Artikel über Volumenintegrale.
:::

::::beispiel Wegweiser in Polar-, Zylinder- und Kugelkoordinaten
**(a) Zylinderkoordinaten** $(\varrho,\varphi,z)$ wie im Artikel über Volumenintegrale.
Die natürlichen Koordinatenvektorfelder sind

$$\partial_\varrho\vec\Phi = (\cos\varphi,\ \sin\varphi,\ 0), \qquad \partial_\varphi\vec\Phi = (-\varrho\sin\varphi,\ \varrho\cos\varphi,\ 0), \qquad \partial_z\vec\Phi = (0,\ 0,\ 1).$$

Sie stehen paarweise senkrecht, das System ist orthogonal, und die Maßfaktoren sind $1$, $\varrho$ und $1$. Ohne die $z$-Richtung
sind das die ebenen Polarkoordinaten.

**(b) Kugelkoordinaten** $(r,\theta,\varphi)$: Die Spalten der Jacobi-Matrix aus dem Artikel über Volumenintegrale stehen
paarweise senkrecht und haben die Längen

$$h_r = 1, \qquad h_\theta = r, \qquad h_\varphi = r\sin\theta.$$

Ihr Produkt ist der Volumenfaktor $r^2\sin\theta$.

**(c) Der Globus in Zahlen.** Mit dem Erdradius $6371\,\mathrm{km}$ ist ein Grad nach Süden überall

$$h_\theta\cdot\frac{\pi}{180} = 6371\,\mathrm{km}\cdot\frac{\pi}{180}\approx111{,}2\,\mathrm{km}.$$

Ein Grad nach Osten hängt vom Polarwinkel ab. Aachen liegt auf $50{,}8^\circ$ nördlicher Breite, also beim Polarwinkel $39{,}2^\circ$:

$$h_\varphi\cdot\frac{\pi}{180} = 6371\,\mathrm{km}\cdot\sin39{,}2^\circ\cdot\frac{\pi}{180}\approx70{,}3\,\mathrm{km}.$$

Am Nordkap sind es nur noch $35{,}9\,\mathrm{km}$, am Pol null.

**Im Bild:** Die Ost-Arme der Wegweiser sind überall gleich lang, aber ein Grad Ost wird zum Pol hin immer kürzer — der
Maßfaktor $r\sin\theta$ ist der Radius des Breitenkreises.
::::

## Der Gradient

Für eine stetig differenzierbare Funktion $f$ schreibt man

$$\tilde f = f\circ\vec\Phi$$

für dieselbe Funktion in den neuen Koordinaten; $\tilde f$ hängt von $u$, $v$ und $w$ ab. In einem orthogonalen
Koordinatensystem ist der Gradient am Punkt $\vec\Phi(u,v,w)$

:::formel
$$\nabla f = \frac{1}{h_u}\frac{\partial\tilde f}{\partial u}\,\vec e_u+\frac{1}{h_v}\frac{\partial\tilde f}{\partial v}\,\vec e_v+\frac{1}{h_w}\frac{\partial\tilde f}{\partial w}\,\vec e_w.$$
:::

**So liest man das:** Jede Ableitung nach einer Koordinate wird durch den Maßfaktor dieser Koordinate geteilt. Die Formel gilt
genauso in der Ebene, mit zwei Koordinaten. Die Auswertung am Punkt $\vec\Phi(u,v,w)$ auf der linken Seite lassen wir ab
hier stillschweigend mitlaufen.

**Im Bild:** Der Gradient misst Gefälle pro Kilometer, nicht pro Grad. Ein Grad nach Osten ist in Aachen nur $70\,\mathrm{km}$
lang; wer das Gefälle pro Grad kennt, muss durch diese $70\,\mathrm{km}$ teilen.

:::herleitung
Nach der Kettenregel aus dem ersten Artikel ist die Ableitung von $\tilde f$ nach $u$ die Ableitung von $f$ längs der
Koordinatenlinie:

$$\frac{\partial\tilde f}{\partial u} = \nabla f\big(\vec\Phi\big)\cdot\partial_u\vec\Phi = h_u\,\nabla f\cdot\vec e_u.$$

Die Komponente des Gradienten in Richtung $\vec e_u$ ist also

$$\nabla f\cdot\vec e_u = \frac{1}{h_u}\frac{\partial\tilde f}{\partial u},$$

und nach der Zerlegung in der Orthonormalbasis folgt die Formel.
:::

::::beispiel Gefälle pro Meter
**(a) Die Höhe** über der $xy$-Ebene ist in Kugelkoordinaten

$$f(x,y,z) = z, \qquad \tilde f = r\cos\theta,$$

und ihr Gradient ist

$$\nabla f = \cos\theta\,\vec e_r+\frac1r\,(-r\sin\theta)\,\vec e_\theta = \cos\theta\,\vec e_r-\sin\theta\,\vec e_\theta.$$

Mit den Wegweisern aus dem Artikel über Volumenintegrale ist das der Einheitsvektor nach oben:

$$\cos\theta\,(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta)-\sin\theta\,(\cos\theta\cos\varphi,\ \cos\theta\sin\varphi,\ -\sin\theta) = (0,\ 0,\ 1).$$

**(b) Ein Temperaturfeld** über Aachen steigt um $1\,\mathrm{K}$ pro Grad nach Osten und hängt sonst von nichts ab. Pro Grad ist
die Ableitung nach dem Azimut $1\,\mathrm{K}$, pro Radiant also $\frac{180}{\pi}\,\mathrm{K}$, und der Gradient zeigt nach Osten mit dem
Betrag

$$\frac{1}{h_\varphi}\cdot\frac{180}{\pi}\,\mathrm{K} = \frac{1\,\mathrm{K}}{70{,}3\,\mathrm{km}}\approx0{,}014\,\frac{\mathrm{K}}{\mathrm{km}}.$$

**Im Bild:** Bei (a) setzt sich der senkrechte Pfeil aus zwei gedrehten Wegweiser-Armen zusammen. Bei (b) ist das Gefälle pro
Grad überall gleich, das Gefälle pro Kilometer aber in Aachen größer als am Äquator, weil ein Grad dort kürzer ist.
::::

## Die Divergenz

Für ein stetig differenzierbares Vektorfeld $\vec F$ ergibt sich aus der Kettenregel, Komponente für Komponente, die
Jacobi-Matrix in den Wegweisern; die Summe läuft über die drei Koordinaten:

$$D\vec F = \sum_u\frac{1}{h_u}\,\partial_u\big(\vec F\circ\vec\Phi\big)\otimes\vec e_u.$$

Dabei ist $\vec p\otimes\vec q$ für zwei Vektoren die Matrix mit den Einträgen $p_iq_j$; sie bildet einen Vektor $\vec y$ auf
$\vec p\,(\vec q\cdot\vec y)$ ab. Die Divergenz ist die Spur der Jacobi-Matrix, und die Spur von $\vec p\otimes\vec q$ ist das Skalarprodukt
$\vec p\cdot\vec q$. Mit der Produktregel folgt:

$$\operatorname{div}\vec F = \sum_{u}\frac{1}{h_u}\Big(\partial_u\big(\vec F\circ\vec\Phi\big)\cdot\vec e_u\Big), \qquad \partial_u\big(\vec F\circ\vec\Phi\big)\cdot\vec e_u = \frac{\partial F_u}{\partial u}-\big(\vec F\circ\vec\Phi\big)\cdot\partial_u\vec e_u.$$

Die Summe läuft über die drei Koordinaten. Der zweite Term ist neu, der Drehterm: Er kommt daher, dass sich die Wegweiser
mitdrehen.

:::herleitung
**Die Jacobi-Matrix.** Nach der Kettenregel ist die Ableitung längs einer Koordinatenlinie

$$\partial_u\big(\vec F\circ\vec\Phi\big) = D\vec F\,\partial_u\vec\Phi = h_u\,D\vec F\,\vec e_u.$$

Die Matrix bildet also $\vec e_u$ auf $\frac{1}{h_u}\partial_u(\vec F\circ\vec\Phi)$ ab, ebenso für $v$ und $w$. Zerlegt man einen beliebigen
Vektor $\vec y$ in der Orthonormalbasis, ist

$$D\vec F\,\vec y = \sum_u\big(\vec e_u\cdot\vec y\big)\,D\vec F\,\vec e_u = \Big(\sum_u\frac{1}{h_u}\,\partial_u\big(\vec F\circ\vec\Phi\big)\otimes\vec e_u\Big)\,\vec y.$$

Die Diagonaleinträge in der Wegweiser-Basis sind $\frac{1}{h_u}\,\partial_u(\vec F\circ\vec\Phi)\cdot\vec e_u$; das sind die Summanden der
Divergenz.

**Die Spur.** Die Spur ist die Summe der Diagonaleinträge und hängt nicht von der Basis ab. Für $\vec p\otimes\vec q$ ist sie
$\sum_ip_iq_i$, also $\vec p\cdot\vec q$.

**Die Produktregel.** Die Komponente ist das Skalarprodukt mit dem Wegweiser, und abgeleitet nach $u$ entstehen zwei Terme:

$$\frac{\partial F_u}{\partial u} = \partial_u\big(\vec F\circ\vec\Phi\big)\cdot\vec e_u+\big(\vec F\circ\vec\Phi\big)\cdot\partial_u\vec e_u.$$

**Im Bild:** Die Komponente $F_u$ kann sich auf zwei Arten ändern — weil sich das Feld ändert oder weil sich der Wegweiser
dreht, an dem man es misst. Nur die erste Art ist eine echte Quelle.
:::

**Wie sich die Wegweiser drehen.** Die Ableitungen der Wegweiser sind wieder Vektoren und lassen sich in den Wegweisern
zerlegen. Bemerkenswert ist: Der Anteil in Richtung des abgeleiteten Wegweisers selbst ist immer null, also

$$\vec e_u\cdot\partial_u\vec e_u = 0.$$

$\partial_u\vec e_u$ ist eine Mischung aus $\vec e_v$ und $\vec e_w$, mit im Allgemeinen veränderlichen Koeffizienten.

:::herleitung
Der Wegweiser hat überall die Länge $1$. Leitet man diese Gleichung ab, folgt mit der Produktregel

$$0 = \partial_u\big(\vec e_u\cdot\vec e_u\big) = 2\,\vec e_u\cdot\partial_u\vec e_u.$$

**Im Bild:** Ein Pfeil fester Länge kann sich nur drehen, nicht wachsen; seine Änderung steht senkrecht auf ihm.
:::

**Die allgemeine Formel.** Ist $\vec\Phi$ zweimal stetig differenzierbar, lassen sich die Drehungen der Wegweiser ganz durch die
Maßfaktoren ausdrücken. Für orthogonale Koordinaten entsteht

:::formel Satz
$$\begin{aligned}\operatorname{div}\vec F = \frac{1}{h_uh_vh_w}\Big(&\frac{\partial}{\partial u}\big(h_vh_w\,F_u\big)+\frac{\partial}{\partial v}\big(h_uh_w\,F_v\big)\\ &+\frac{\partial}{\partial w}\big(h_uh_v\,F_w\big)\Big).\end{aligned}$$
:::

**So liest man das:** Jede Komponente wird mit den beiden anderen Maßfaktoren multipliziert, nach ihrer Koordinate
abgeleitet, und alles wird durch das Volumenelement $h_uh_vh_w$ geteilt. Kartesisch sind alle Maßfaktoren $1$, und es bleibt die
bekannte Summe der Ableitungen.

**Im Bild:** Die Divergenz ist der Ausfluss aus einem Klötzchen pro Volumen. Durch die beiden Seitenflächen senkrecht zu
$\vec e_u$ fließt $F_u$ mal Fläche, und die Fläche ist $h_vh_w\,dv\,dw$. Geht man in $u$-Richtung weiter, ändert sich nicht nur das
Feld, sondern auch die Fläche — deshalb steht $h_vh_w$ innerhalb der Ableitung.

:::grafik
Szene: hoema3/koordinatentransformationen/04-kloetzchen-fluss · Vorlage: fluss-quader-3d
Ein Klötzchen der Zwiebel zwischen zwei Schalen, zwei Breitenkreisen und zwei Spalten, mit Feldpfeilen eines radialen Felds.
Die innere und die äußere Seitenfläche sind hervorgehoben und mit ihren Flächen $h_\theta h_\varphi\,d\theta\,d\varphi$ beschriftet; die
äußere ist größer. Zwei Zähler zeigen den Fluss durch beide Flächen und ihre Differenz, ein dritter den Quotienten aus
Differenz und Volumen. Ein Umschalter wechselt zwischen einem Feld mit gleichem Betrag, dessen Fluss außen größer ist, und dem
Coulomb-Feld, bei dem beide Flüsse gleich sind. Kernaussage: In krummlinigen Koordinaten zählen bei der Divergenz Feld und
Fläche. (Rot = Seitenflächen, blau = Feldpfeile, orange = Zähler, grau = Gitter.)
:::

:::herleitung
**Schritt 1: die Drehung durch Maßfaktoren.** Nach dem Satz von Schwarz vertauschen die Ableitungen von $\vec\Phi$, und für zwei
verschiedene Koordinaten $u$ und $k$ ist

$$\partial_k\big(h_u\,\vec e_u\big) = \partial_k\partial_u\vec\Phi = \partial_u\partial_k\vec\Phi = \partial_u\big(h_k\,\vec e_k\big).$$

Man multipliziert mit $\vec e_u$. Links bleibt $\partial_kh_u$, denn $\vec e_u\cdot\partial_k\vec e_u$ ist null — dieselbe Rechnung wie oben,
nur nach $k$ statt nach $u$ abgeleitet. Rechts bleibt
$h_k\,\vec e_u\cdot\partial_u\vec e_k$, denn $\vec e_u\cdot\vec e_k$ ist null. Weil auch die Ableitung von $\vec e_u\cdot\vec e_k$ null ist,
folgt

$$\vec e_k\cdot\partial_u\vec e_u = -\vec e_u\cdot\partial_u\vec e_k = -\frac{1}{h_k}\,\partial_kh_u.$$

**Schritt 2: einsetzen.** Zerlegt man das Feld in den Wegweisern, ist der Drehterm

$$\big(\vec F\circ\vec\Phi\big)\cdot\partial_u\vec e_u = \sum_{k\neq u}F_k\,\vec e_k\cdot\partial_u\vec e_u = -\sum_{k\neq u}\frac{F_k}{h_k}\,\partial_kh_u,$$

und die Divergenz wird

$$\operatorname{div}\vec F = \sum_u\frac{1}{h_u}\Big(\frac{\partial F_u}{\partial u}+\sum_{k\neq u}\frac{F_k}{h_k}\,\partial_kh_u\Big).$$

**Schritt 3: sortieren.** Man sammelt alle Terme mit $F_u$. Aus dem Summanden zu $u$ kommt $\frac{1}{h_u}\partial_uF_u$, aus den
Summanden zu den beiden anderen Koordinaten $v$ und $w$ kommen $\frac{F_u}{h_uh_v}\partial_uh_v$ und $\frac{F_u}{h_uh_w}\partial_uh_w$.
Zusammen ist das nach der Produktregel

$$\frac{1}{h_u}\Big(\frac{\partial F_u}{\partial u}+F_u\,\frac{\partial_uh_v}{h_v}+F_u\,\frac{\partial_uh_w}{h_w}\Big) = \frac{1}{h_uh_vh_w}\,\frac{\partial}{\partial u}\big(h_vh_w\,F_u\big).$$

Dasselbe für $v$ und $w$ gibt die Formel.
:::

::::beispiel Zwei Proben für die Divergenz
**(a) Kartesisch** sind alle Maßfaktoren $1$, und die Formel wird zur gewohnten Summe

$$\operatorname{div}\vec F = \frac{\partial F_1}{\partial x}+\frac{\partial F_2}{\partial y}+\frac{\partial F_3}{\partial z}.$$

**(b) Das Ortsvektorfeld** $\vec x$ hat in Kugelkoordinaten nur die Komponente $r$ in Richtung $\vec e_r$. Mit dem Volumenelement
$r^2\sin\theta$ und dem Produkt $h_\theta h_\varphi=r^2\sin\theta$ ist

$$\operatorname{div}\vec x = \frac{1}{r^2\sin\theta}\,\frac{\partial}{\partial r}\big(r^2\sin\theta\cdot r\big) = \frac{3r^2\sin\theta}{r^2\sin\theta} = 3,$$

wie kartesisch, wo jede der drei Ableitungen $1$ ist.

**Im Bild:** Bei (b) strömt das Feld radial nach außen. Die Seitenflächen der Zwiebel-Klötzchen wachsen mit $r^2$ und das Feld mit
$r$ — zusammen wächst der Fluss wie $r^3$, und pro Volumen bleibt überall dieselbe Quelldichte $3$.
::::

**Der Laplace-Operator** ist die Divergenz des Gradienten. Setzt man die Komponenten des Gradienten ein, also
$\frac{1}{h_u}\partial_u\tilde f$ für $F_u$, ergibt sich für orthogonale Koordinaten

:::formel Satz
$$\begin{aligned}\Delta f = \frac{1}{h_uh_vh_w}\Big(&\frac{\partial}{\partial u}\Big(\frac{h_vh_w}{h_u}\,\frac{\partial\tilde f}{\partial u}\Big)\\ &+\frac{\partial}{\partial v}\Big(\frac{h_uh_w}{h_v}\,\frac{\partial\tilde f}{\partial v}\Big)\\ &+\frac{\partial}{\partial w}\Big(\frac{h_uh_v}{h_w}\,\frac{\partial\tilde f}{\partial w}\Big)\Big).\end{aligned}$$
:::

**So liest man das:** Zweimal dieselbe Regel: Erst teilt der Gradient jede Ableitung durch ihren Maßfaktor, dann multipliziert
die Divergenz mit den beiden anderen und teilt am Ende durch das Volumenelement.

**Im Bild:** Der Laplace-Operator misst, wie viel Gefälle aus einem Klötzchen herausströmt — in krummlinigen Koordinaten mit
den gewachsenen oder geschrumpften Seitenflächen.

:::herleitung
Der Gradient hat nach seiner Formel die Komponenten

$$\big(\nabla f\big)_u = \frac{1}{h_u}\frac{\partial\tilde f}{\partial u}, \qquad \big(\nabla f\big)_v = \frac{1}{h_v}\frac{\partial\tilde f}{\partial v}, \qquad \big(\nabla f\big)_w = \frac{1}{h_w}\frac{\partial\tilde f}{\partial w}.$$

In die allgemeine Divergenzformel eingesetzt, wird aus $h_vh_wF_u$ der Ausdruck $\frac{h_vh_w}{h_u}\partial_u\tilde f$, ebenso für $v$ und
$w$. Dafür braucht man $f$ zweimal stetig differenzierbar.
:::

::::beispiel Zwei Quadrate
**(a) Das Abstandsquadrat** $r^2$ in Kugelkoordinaten hängt nur von $r$ ab. Mit den Maßfaktoren $1$, $r$, $r\sin\theta$ bleibt der
erste Summand:

$$\Delta\big(r^2\big) = \frac{1}{r^2\sin\theta}\,\frac{\partial}{\partial r}\big(r^2\sin\theta\cdot2r\big) = \frac{6r^2}{r^2} = 6.$$

Kartesisch ist $r^2=x^2+y^2+z^2$, und jede der drei zweiten Ableitungen ist $2$ — auch $6$.

**(b) Das Quadrat des Abstands zur Achse** $\varrho^2$ in Zylinderkoordinaten, mit den Maßfaktoren $1$, $\varrho$, $1$:

$$\Delta\big(\varrho^2\big) = \frac1\varrho\,\frac{\partial}{\partial\varrho}\big(\varrho\cdot2\varrho\big) = \frac{4\varrho}{\varrho} = 4.$$

Kartesisch ist $\varrho^2=x^2+y^2$ mit zwei zweiten Ableitungen $2$ — auch $4$.

**Im Bild:** In beiden Fällen ist das Gefälle radial, es wächst wie der Abstand, und die Klötzchen-Seitenflächen wachsen mit;
pro Volumen bleibt der Ausfluss konstant.
::::

## Zylinderkoordinaten

Die Zylinderkoordinaten rechnen wir ausführlich durch, auf dem Weg über die sich drehenden Wegweiser. Die Koordinaten
laufen dabei durch offene Intervalle, damit $\vec\Phi$ injektiv ist und nirgends flachdrückt:

$$\vec\Phi(\varrho,\varphi,z) = (\varrho\cos\varphi,\ \varrho\sin\varphi,\ z), \qquad \varrho\in(0,\infty),\quad \varphi\in(0,2\pi),\quad z\in\mathbb{R}.$$

Die Wegweiser und ihre Ableitungen sind

$$\vec e_\varrho = (\cos\varphi,\ \sin\varphi,\ 0), \qquad \vec e_\varphi = (-\sin\varphi,\ \cos\varphi,\ 0), \qquad \vec e_z = (0,\ 0,\ 1),$$

$$\partial_\varphi\vec e_\varrho = \vec e_\varphi, \qquad \partial_\varphi\vec e_\varphi = -\vec e_\varrho,$$

und alle übrigen Ableitungen der Wegweiser sind null. Damit sind der Gradient einer Funktion $f$, die Divergenz eines
Vektorfelds $\vec E$ mit den Komponenten $E_\varrho$, $E_\varphi$, $E_z$ und der Laplace-Operator

$$\nabla f = \frac{\partial\tilde f}{\partial\varrho}\,\vec e_\varrho+\frac1\varrho\,\frac{\partial\tilde f}{\partial\varphi}\,\vec e_\varphi+\frac{\partial\tilde f}{\partial z}\,\vec e_z,$$

$$\begin{aligned}\operatorname{div}\vec E &= \frac{\partial E_\varrho}{\partial\varrho}+\frac1\varrho\,\frac{\partial E_\varphi}{\partial\varphi}+\frac1\varrho\,E_\varrho+\frac{\partial E_z}{\partial z}\\ &= \frac1\varrho\Big(\frac{\partial}{\partial\varrho}\big(\varrho\,E_\varrho\big)+\frac{\partial E_\varphi}{\partial\varphi}\Big)+\frac{\partial E_z}{\partial z},\end{aligned}$$

$$\Delta f = \frac{\partial^2\tilde f}{\partial\varrho^2}+\frac1\varrho\,\frac{\partial\tilde f}{\partial\varrho}+\frac{1}{\varrho^2}\,\frac{\partial^2\tilde f}{\partial\varphi^2}+\frac{\partial^2\tilde f}{\partial z^2}.$$

**Im Bild:** Auf einem Karussell zeigt „nach außen" immer vom Mittelpunkt weg. Dreht man sich ein Stück weiter, kippt der
Außen-Arm in die alte Umlaufrichtung und der Umlauf-Arm nach innen — das sagen die beiden Ableitungen.

:::grafik
Szene: hoema3/koordinatentransformationen/04-karussell-wegweiser · Vorlage: polar-basis-2d
Draufsicht auf ein Karussell mit Wegweisern an mehreren Stellen eines Kreises: ein Pfeil nach außen und einer in
Umlaufrichtung. Ein Regler schiebt einen Wegweiser um einen kleinen Winkel weiter; die Änderung beider Pfeile wird als kurzer
Differenzpfeil gezeichnet — beim Außen-Pfeil in Umlaufrichtung, beim Umlauf-Pfeil nach innen. Daneben die Divergenz eines
radialen Felds als Summe aus der Änderung des Betrags und dem Auseinanderlaufen der Linien. Kernaussage: Die Zusatzterme der
Zylinderkoordinaten kommen von den sich drehenden Wegweisern. (Blau = Wegweiser, orange = Änderungen, rot = Feld, grau =
Kreis.)
:::

:::herleitung
**Die Wegweiser.** Die natürlichen Koordinatenvektorfelder aus dem ersten Beispiel, geteilt durch ihre Maßfaktoren $1$,
$\varrho$ und $1$, sind die drei Wegweiser. Abgeleitet nach $\varphi$ wird $(\cos\varphi,\sin\varphi,0)$ zu $(-\sin\varphi,\cos\varphi,0)$ und
dieses zu $(-\cos\varphi,-\sin\varphi,0)$. Von $\varrho$ und $z$ hängt kein Wegweiser ab.

**Die Divergenz über den Drehterm.** In der Summe aus Ableitung und Drehterm tragen die drei Koordinaten bei:

$$\frac{\partial E_\varrho}{\partial\varrho}-\vec E\cdot\partial_\varrho\vec e_\varrho = \frac{\partial E_\varrho}{\partial\varrho}, \qquad \frac1\varrho\Big(\frac{\partial E_\varphi}{\partial\varphi}-\vec E\cdot\partial_\varphi\vec e_\varphi\Big) = \frac1\varrho\Big(\frac{\partial E_\varphi}{\partial\varphi}+E_\varrho\Big), \qquad \frac{\partial E_z}{\partial z}.$$

Der Zusatzterm $\frac1\varrho E_\varrho$ ist der Drehterm: $\partial_\varphi\vec e_\varphi$ zeigt nach innen, und sein Skalarprodukt mit dem Feld ist
$-E_\varrho$. Zusammengefasst ist $\partial_\varrho E_\varrho+\frac1\varrho E_\varrho$ nach der Produktregel $\frac1\varrho\partial_\varrho(\varrho E_\varrho)$ — genau
die allgemeine Formel mit den Maßfaktoren $1$, $\varrho$, $1$.

**Der Laplace-Operator.** Man setzt den Gradienten ein, also die Komponenten $\partial_\varrho\tilde f$, $\frac1\varrho\partial_\varphi\tilde f$ und
$\partial_z\tilde f$:

$$\Delta f = \frac1\varrho\,\frac{\partial}{\partial\varrho}\Big(\varrho\,\frac{\partial\tilde f}{\partial\varrho}\Big)+\frac{1}{\varrho^2}\,\frac{\partial^2\tilde f}{\partial\varphi^2}+\frac{\partial^2\tilde f}{\partial z^2},$$

und die Produktregel im ersten Term gibt $\partial_\varrho^2\tilde f+\frac1\varrho\partial_\varrho\tilde f$.
:::

::::beispiel Linienladung, Wirbel und Logarithmus
**(a) Das Feld einer Linienladung** auf der $z$-Achse zeigt von der Achse weg und fällt mit dem Abstand, bei der Ladung $1$ pro
Länge ohne Feldkonstante:

$$\vec E = \frac{1}{2\pi\varrho}\,\vec e_\varrho, \qquad \operatorname{div}\vec E = \frac1\varrho\,\frac{\partial}{\partial\varrho}\Big(\varrho\cdot\frac{1}{2\pi\varrho}\Big) = 0.$$

Auf dem Weg über den Drehterm heben sich zwei Terme weg:

$$\frac{\partial E_\varrho}{\partial\varrho}+\frac1\varrho\,E_\varrho = -\frac{1}{2\pi\varrho^2}+\frac{1}{2\pi\varrho^2} = 0.$$

**(b) Der Wirbel** um die Achse, das Feld der Wendeltreppe aus dem Artikel
[Der erste Hauptsatz und konservative Felder](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/erster-hauptsatz-konservative-felder.html), hat nur eine
Umlaufkomponente, die nicht vom Winkel abhängt:

$$\vec E = \frac1\varrho\,\vec e_\varphi, \qquad \operatorname{div}\vec E = \frac1\varrho\,\frac{\partial}{\partial\varphi}\Big(\frac1\varrho\Big) = 0.$$

**(c) Der Logarithmus** des Abstands zur Achse ist harmonisch:

$$\Delta\big(\ln\varrho\big) = \frac1\varrho\,\frac{\partial}{\partial\varrho}\Big(\varrho\cdot\frac1\varrho\Big) = 0.$$

Er ist bis auf den Faktor $-\frac{1}{2\pi}$ das Potential der Linienladung aus (a).

**Im Bild:** Bei (a) laufen die Feldlinien auseinander — das ist der Zusatzterm $\frac1\varrho E_\varrho$ —, während der Betrag fällt.
Beides gleicht sich genau aus, und außerhalb der Achse gibt es keine Quellen.
::::

## Kugelkoordinaten

Mit den Maßfaktoren $1$, $r$ und $r\sin\theta$ und dem Volumenelement $r^2\sin\theta$ geben die allgemeinen Formeln die Operatoren in
Kugelkoordinaten. Die Wegweiser — nach außen, nach Süden, nach Osten — sind

$$\vec e_r = (\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta), \qquad \vec e_\theta = (\cos\theta\cos\varphi,\ \cos\theta\sin\varphi,\ -\sin\theta), \qquad \vec e_\varphi = (-\sin\varphi,\ \cos\varphi,\ 0).$$

Gradient, Divergenz und Laplace-Operator sind

$$\nabla f = \frac{\partial\tilde f}{\partial r}\,\vec e_r+\frac1r\,\frac{\partial\tilde f}{\partial\theta}\,\vec e_\theta+\frac{1}{r\sin\theta}\,\frac{\partial\tilde f}{\partial\varphi}\,\vec e_\varphi,$$

$$\operatorname{div}\vec F = \frac{1}{r^2}\,\frac{\partial}{\partial r}\big(r^2F_r\big)+\frac{1}{r\sin\theta}\,\frac{\partial}{\partial\theta}\big(\sin\theta\,F_\theta\big)+\frac{1}{r\sin\theta}\,\frac{\partial F_\varphi}{\partial\varphi},$$

$$\Delta f = \frac{1}{r^2}\,\frac{\partial}{\partial r}\Big(r^2\,\frac{\partial\tilde f}{\partial r}\Big)+\frac{1}{r^2\sin\theta}\,\frac{\partial}{\partial\theta}\Big(\sin\theta\,\frac{\partial\tilde f}{\partial\theta}\Big)+\frac{1}{r^2\sin^2\theta}\,\frac{\partial^2\tilde f}{\partial\varphi^2}.$$

Hängt $f$ nur vom Abstand ab, bleibt vom Laplace-Operator nur der erste Term — die radiale Form aus dem Artikel
[Divergenz, Rotation und Laplace-Operator](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/divergenz-rotation-laplace.html)
und aus dem Artikel über das Newtonpotential.

**Im Bild:** Die Wegweiser des Globus. Der Faktor $\frac{1}{r\sin\theta}$ vor der Ostrichtung ist der Kehrwert des Breitenkreisradius:
Nahe am Pol ist ein Grad Ost kurz, und ein kleiner Unterschied pro Grad ist ein großes Gefälle pro Kilometer.

:::herleitung
**Die Wegweiser** sind die Spalten der Jacobi-Matrix aus dem Artikel über Volumenintegrale, geteilt durch ihre Längen $1$, $r$
und $r\sin\theta$. Dass sie paarweise senkrecht stehen, zeigt das Ausmultiplizieren; etwa ist

$$\vec e_r\cdot\vec e_\theta = \sin\theta\cos\theta\,\big(\cos^2\varphi+\sin^2\varphi\big)-\cos\theta\sin\theta = 0.$$

**Der Gradient** ist die allgemeine Formel mit den drei Maßfaktoren.

**Die Divergenz.** Das Produkt der Maßfaktoren ist $r^2\sin\theta$, und die allgemeine Formel gibt

$$\operatorname{div}\vec F = \frac{1}{r^2\sin\theta}\Big(\frac{\partial}{\partial r}\big(r^2\sin\theta\,F_r\big)+\frac{\partial}{\partial\theta}\big(r\sin\theta\,F_\theta\big)+\frac{\partial}{\partial\varphi}\big(r\,F_\varphi\big)\Big).$$

Konstante Faktoren zieht man vor die Ableitungen und kürzt.

**Der Laplace-Operator.** In der allgemeinen Formel stehen die Faktoren

$$\frac{h_\theta h_\varphi}{h_r} = r^2\sin\theta, \qquad \frac{h_rh_\varphi}{h_\theta} = \sin\theta, \qquad \frac{h_rh_\theta}{h_\varphi} = \frac{1}{\sin\theta},$$

und nach dem Kürzen mit $r^2\sin\theta$ entsteht die angegebene Form.
:::

::::beispiel Harmonische Funktionen im Raum
**(a) Das Coulomb-Potential** hängt nur von $r$ ab:

$$\tilde f = \frac{1}{4\pi r}, \qquad r^2\,\frac{\partial\tilde f}{\partial r} = -\frac{1}{4\pi}, \qquad \Delta f = \frac{1}{r^2}\,\frac{\partial}{\partial r}\Big(-\frac{1}{4\pi}\Big) = 0.$$

Sein Feld $\frac{1}{4\pi r^2}\vec e_r$ hat entsprechend die Divergenz $\frac{1}{r^2}\partial_r(\frac{1}{4\pi})$, also null.

**(b) Die Höhe** $z$ ist in Kugelkoordinaten $r\cos\theta$. Beide Terme des Laplace-Operators sind nicht null, heben sich aber weg:

$$\frac{1}{r^2}\,\frac{\partial}{\partial r}\big(r^2\cos\theta\big) = \frac{2\cos\theta}{r}, \qquad \frac{1}{r^2\sin\theta}\,\frac{\partial}{\partial\theta}\big(\sin\theta\cdot(-r\sin\theta)\big) = -\frac{2\cos\theta}{r}.$$

**(c) Das Dipolpotential** $\frac{\cos\theta}{r^2}$, kartesisch $\frac{z}{r^3}$, ist ebenfalls harmonisch:

$$\frac{1}{r^2}\,\frac{\partial}{\partial r}\Big(r^2\cdot\frac{-2\cos\theta}{r^3}\Big) = \frac{2\cos\theta}{r^4}, \qquad \frac{1}{r^2\sin\theta}\,\frac{\partial}{\partial\theta}\Big(\sin\theta\cdot\frac{-\sin\theta}{r^2}\Big) = -\frac{2\cos\theta}{r^4}.$$

**(d) Ein Gegenbeispiel:** Der Logarithmus des Abstands ist im Raum nicht harmonisch, anders als in der Ebene:

$$\Delta\big(\ln r\big) = \frac{1}{r^2}\,\frac{\partial}{\partial r}\Big(r^2\cdot\frac1r\Big) = \frac{1}{r^2}.$$

**Im Bild:** Bei (b) und (c) liefern die Richtungen nach außen und nach Süden Beiträge mit entgegengesetztem Vorzeichen, die
sich genau aufheben. Bei (d) wachsen die Zwiebelschalen schneller, als das Gefälle fällt, und es bleibt ein Ausfluss.
::::

## Bedeutung und Ausblick

Mit den Maßfaktoren übersetzt man jeden Differentialoperator in das Koordinatensystem, das zur Symmetrie eines Problems passt:
Zylinderkoordinaten für Leiter, Koaxialkabel und Spulen, Kugelkoordinaten für Punktladungen, Antennen und Atome. Die
Zusatzterme sind keine Willkür; sie zählen, dass sich die Wegweiser drehen und die Klötzchen-Flächen wachsen.

Es gibt noch einen zweiten Weg zu diesen Formeln, der das Ableiten der Wegweiser umgeht: den Transformationssatz
zusammen mit den Integralsätzen von Gauß und Stokes im Raum. Diese Integralsätze sind das Thema der Artikel
[Der Satz von Stokes im Raum](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum/satz-von-stokes-im-raum.html)
und [Der Satz von Gauß im Raum](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralsatze-im-raum/satz-von-gauss-im-raum.html);
mit ihnen wird auch das Bild vom Ausfluss aus einem Klötzchen zur Rechnung.

:::kern
- __Krummlinige Koordinaten__: Eine injektive, nirgends flachdrückende Abbildung $\vec\Phi(u,v,w)$ gibt jedem Punkt ein Koordinatentripel.
- __Maßfaktor__ und __Wegweiser__: $h_u=\lvert\partial_u\vec\Phi\rvert$ ist die Länge eines Koordinatenschritts, $\vec e_u$ seine Richtung.
- Die Wegweiser drehen sich mit dem Ort; bilden sie überall eine Orthonormalbasis, heißt das System __orthogonal__.
- Orthogonal ist das Volumenelement das Produkt der Maßfaktoren — für die Kugel $r^2\sin\theta$.
- __Gradient__: Jede Ableitung wird durch ihren Maßfaktor geteilt — Gefälle pro Kilometer, nicht pro Grad.
- __Divergenz__ ist die Spur der Jacobi-Matrix; die Zusatzterme kommen von den sich drehenden Wegweisern.
- Allgemein orthogonal: $\operatorname{div}\vec F=\frac{1}{h_uh_vh_w}\sum_u\partial_u(h_vh_wF_u)$ — der Fluss durch wachsende Klötzchen-Flächen.
- __Laplace-Operator__: In Zylinderkoordinaten kommt der Zusatzterm $\frac1\varrho\partial_\varrho\tilde f$ hinzu, in Kugelkoordinaten steht im radialen Teil ein Faktor $r^2$ innerhalb der Ableitung.
- Coulomb-Potential, Höhe und Dipolpotential sind im Raum harmonisch, der Logarithmus des Abstands nur in der Ebene.
:::

:::quiz
F: Was sind natürliche und normierte Koordinatenvektorfelder und Maßfaktoren, und was bedeuten sie auf dem Globus?
A: Die natürlichen Koordinatenvektorfelder sind die partiellen Ableitungen $\partial_u\vec\Phi$, die Spalten der Jacobi-Matrix; sie liegen tangential an den Koordinatenlinien. Ihre Längen sind die Maßfaktoren $h_u$, ihre Richtungen die normierten Felder $\vec e_u$. Auf dem Globus sind das die Arme eines Wegweisers und die Kilometer pro Grad — nach Süden überall $111{,}2\,\mathrm{km}$, nach Osten in Aachen $70{,}3\,\mathrm{km}$.
F: Warum drehen sich die Wegweiser mit, und was heißt orthogonal?
A: Die Wegweiser liegen tangential an den Koordinatenlinien, und die sind krumm — Kreise, Meridiane, Breitenkreise. Deshalb ändert sich ihre Richtung von Ort zu Ort, während kartesische Basisvektoren überall gleich sind. Orthogonal heißt das System, wenn die drei Wegweiser an jedem Punkt paarweise senkrecht stehen; dann zerlegt man jedes Feld als $\vec F=\sum F_u\vec e_u$ mit $F_u=\vec F\cdot\vec e_u$.
F: Warum ist das Volumenelement eines orthogonalen Systems das Produkt der Maßfaktoren?
A: Die Spalten der Jacobi-Matrix sind $h_u\vec e_u$, $h_v\vec e_v$, $h_w\vec e_w$. Weil die Determinante linear in den Spalten ist und eine Matrix mit orthonormalen Spalten die Determinante $\pm1$ hat, ist $\lvert\det D\vec\Phi\rvert=h_uh_vh_w$. Für die Kugel ist das $1\cdot r\cdot r\sin\theta=r^2\sin\theta$.
F: Warum steht im Gradienten der Faktor $\frac{1}{h_u}$?
A: Nach der Kettenregel ist $\partial_u\tilde f=\nabla f\cdot\partial_u\vec\Phi=h_u\,\nabla f\cdot\vec e_u$; die Komponente des Gradienten ist also $\frac{1}{h_u}\partial_u\tilde f$. Anschaulich misst der Gradient Gefälle pro Länge, und ein Koordinatenschritt $du$ ist $h_u\,du$ lang — ein Temperaturanstieg von $1\,\mathrm{K}$ pro Grad Ost ist in Aachen etwa $0{,}014\,\mathrm{K}$ pro Kilometer.
F: Wie hängt die Divergenz mit der Jacobi-Matrix zusammen, und woher kommt der Drehterm?
A: Die Jacobi-Matrix ist $\sum\frac{1}{h_u}\partial_u(\vec F\circ\vec\Phi)\otimes\vec e_u$, und die Divergenz ist ihre Spur, $\sum\frac{1}{h_u}\partial_u(\vec F\circ\vec\Phi)\cdot\vec e_u$. Weil $F_u$ das Skalarprodukt mit einem sich drehenden Wegweiser ist, gibt die Produktregel $\partial_uF_u-(\vec F\circ\vec\Phi)\cdot\partial_u\vec e_u$ — der zweite Term zählt die Drehung des Wegweisers heraus.
F: Warum ist $\vec e_u\cdot\partial_u\vec e_u=0$, und wie drehen sich die Wegweiser der Zylinderkoordinaten?
A: Ein Wegweiser hat überall die Länge $1$; die Ableitung von $\vec e_u\cdot\vec e_u=1$ gibt $2\vec e_u\cdot\partial_u\vec e_u=0$ — ein Pfeil fester Länge kann sich nur drehen. In Zylinderkoordinaten ist $\partial_\varphi\vec e_\varrho=\vec e_\varphi$ und $\partial_\varphi\vec e_\varphi=-\vec e_\varrho$, alle anderen Ableitungen sind null — wie die Arme eines Wegweisers auf einem Karussell.
F: Wie lautet die allgemeine Divergenzformel für orthogonale Koordinaten, und warum steht $h_vh_w$ in der Ableitung?
A: $\operatorname{div}\vec F=\frac{1}{h_uh_vh_w}(\partial_u(h_vh_wF_u)+\partial_v(h_uh_wF_v)+\partial_w(h_uh_vF_w))$. Die Seitenfläche eines Klötzchens senkrecht zu $\vec e_u$ ist $h_vh_w\,dv\,dw$, und beim Weitergehen in $u$ ändern sich Feld und Fläche. Hergeleitet wird sie mit dem Satz von Schwarz, der die Drehung der Wegweiser durch Ableitungen der Maßfaktoren ausdrückt; die Probe $\operatorname{div}\vec x=3$ gelingt auch in Kugelkoordinaten.
F: Wie sehen Divergenz und Laplace-Operator in Zylinderkoordinaten aus, und was zeigen Linienladung und Logarithmus?
A: $\operatorname{div}\vec E=\frac1\varrho(\partial_\varrho(\varrho E_\varrho)+\partial_\varphi E_\varphi)+\partial_zE_z$ und $\Delta f=\partial_\varrho^2\tilde f+\frac1\varrho\partial_\varrho\tilde f+\frac{1}{\varrho^2}\partial_\varphi^2\tilde f+\partial_z^2\tilde f$. Das Feld $\frac{1}{2\pi\varrho}\vec e_\varrho$ einer Linienladung ist außerhalb der Achse quellenfrei, weil das Auseinanderlaufen den Abfall genau ausgleicht, und $\ln\varrho$ ist harmonisch. Die Probe $\Delta(\varrho^2)=4$ stimmt mit der kartesischen Rechnung überein.
F: Wie sieht der Laplace-Operator in Kugelkoordinaten aus, und was folgt für das Coulomb-Potential?
A: $\Delta f=\frac{1}{r^2}\partial_r(r^2\partial_r\tilde f)+\frac{1}{r^2\sin\theta}\partial_\theta(\sin\theta\,\partial_\theta\tilde f)+\frac{1}{r^2\sin^2\theta}\partial_\varphi^2\tilde f$, aus den Faktoren $r^2\sin\theta$, $\sin\theta$ und $\frac{1}{\sin\theta}$ der allgemeinen Formel. Für $\frac{1}{4\pi r}$ ist $r^2\partial_r\tilde f$ konstant, also $\Delta f=0$; auch $\Delta(r^2)=6$ stimmt mit der kartesischen Rechnung überein.
F: Welche Funktionen sind im Raum harmonisch, und warum ist der Logarithmus des Abstands es nicht?
A: Das Coulomb-Potential $\frac{1}{4\pi r}$, die Höhe $r\cos\theta$ und das Dipolpotential $\frac{\cos\theta}{r^2}$ — bei den beiden letzten heben sich der radiale und der Polarwinkel-Teil genau auf. Für $\ln r$ ist dagegen $\Delta(\ln r)=\frac{1}{r^2}$: Die Zwiebelschalen wachsen schneller, als das Gefälle fällt. In der Ebene ist $\ln\varrho$ harmonisch.
:::
