---
title: Reguläre Flächen und das Oberflächenintegral
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3050100
summary: Von Grund auf – wie man über eine gekrümmte Fläche im Raum integriert. Eine Parametrisierung $x(u,v)$ bildet ein ebenes Gebiet auf die Fläche ab; das Oberflächenelement $d\sigma=\sqrt{EG-F^2}\,du\,dv=|\partial_u x\times\partial_v x|\,du\,dv$ misst, wie stark ein Koordinatenkästchen zum Flächenstück verzerrt wird. Damit folgen Oberflächenintegral, Flächeninhalt (Kugel $4\pi R^2$) und das Element für Graphen $\sqrt{1+|\nabla H|^2}$.
tags: reguläres Flächenstück, Parametrisierung, Tangentialebene, Normalenvektor, metrische Koeffizienten, Oberflächenelement, Oberflächenintegral, Flächeninhalt
---

:::grafik
Einstiegs-Animation: Ein ebenes Parametergebiet $(u,v)$ wird durch $x(u,v)$ auf eine gewölbte Fläche im Raum
abgebildet. Ein kleines Kästchen $du\times dv$ geht dabei in ein **Parallelogramm** über, aufgespannt von den
Tangentenvektoren $\partial_u x$ und $\partial_v x$; seine Fläche ist $|\partial_u x\times\partial_v x|\,du\,dv$ —
das __Oberflächenelement__ $d\sigma$. Senkrecht darauf steht der Normalenvektor $n$. Für die Kugel sieht man, wie
die Maschen zu den Polen hin schrumpfen (Faktor $\sin\vartheta$). Kernbotschaft: Integrieren über eine Fläche
heißt, lauter solche verzerrten Kästchen aufzusummieren — gewichtet mit $d\sigma$.
:::

:::konzept
Bisher haben wir über Kurven (1D) und über ebene/räumliche Gebiete integriert. Jetzt kommt das Integrieren über
**gekrümmte Flächen** im Raum — die Oberfläche einer Kugel, ein Funktionsgraph, eine Membran. Die Herausforderung:
Was ist das richtige „Flächenstück" $d\sigma$? Es ergibt sich aus der Parametrisierung: Ein winziges
Koordinatenkästchen wird auf ein Parallelogramm in der **Tangentialebene** abgebildet, dessen Fläche die
__metrischen Koeffizienten__ liefern. Dieses Oberflächenintegral ist die Grundlage für **Flüsse** durch Flächen
und damit für die großen Integralsätze (Stokes, Gauß) im Raum — das Herzstück der Feldtheorie.
:::

**Worum es geht:** Wir definieren das __reguläre Flächenstück__ mit Tangentialebene und Normale, die __metrischen
Koeffizienten__ $E,F,G$ und das __Oberflächenelement__ $d\sigma$, und berechnen __Oberflächenintegrale__ und
Flächeninhalte (Kugel, Graph, Rotationsfläche).

## Reguläre Flächenstücke

Ein __reguläres Flächenstück__ $\mathcal{F}$ ist das Bild einer stetig differenzierbaren Parametrisierung
$x=x(u,v)=\Phi(u,v)\in\mathbb{R}^3$ über einem regulären Parameterbereich $B\subset\mathbb{R}^2$, die **injektiv**
ist und deren Tangentenvektoren überall **linear unabhängig** sind:

$$\frac{\partial x}{\partial u}\times\frac{\partial x}{\partial v} \neq (0,0,0).$$

Die beiden Tangentenvektoren $\partial_u x$ und $\partial_v x$ spannen in jedem Punkt die __Tangentialebene__ auf.
Ihr normiertes Kreuzprodukt ist der __Einheitsnormalenvektor__

$$n = \frac{\partial_u x\times\partial_v x}{\lvert\partial_u x\times\partial_v x\rvert},$$

und zusammen mit den normierten Tangenten bildet $n$ in jedem Flächenpunkt eine Orthonormalbasis des $\mathbb{R}^3$.
Die Regularitätsbedingung $\partial_u x\times\partial_v x\ne0$ garantiert, dass die Fläche nirgends „entartet"
(keine Spitzen, keine zusammenfallenden Tangenten).

## Metrische Koeffizienten und das Oberflächenelement

Wie groß ist das Flächenstück, auf das ein kleines Koordinatenkästchen $du\times dv$ abgebildet wird? Es wird zu
einem **Parallelogramm** mit den Kanten $\partial_u x\,du$ und $\partial_v x\,dv$. Dessen Größe steckt in den
__metrischen Koeffizienten__

$$E = \lvert\partial_u x\rvert^2, \qquad F = \partial_u x\cdot\partial_v x, \qquad G = \lvert\partial_v x\rvert^2,$$

zusammengefasst zum __metrischen Tensor__ $g=\begin{pmatrix}E&F\\F&G\end{pmatrix}$. Die Fläche des Parallelogramms
ist die Wurzel seiner Gram-Determinante — und die ist gerade der Betrag des Kreuzprodukts:

$$\sqrt{\det g} = \sqrt{EG - F^2} = \lvert\partial_u x\times\partial_v x\rvert.$$

Das ist das __Oberflächenelement__ $d\sigma = \sqrt{EG-F^2}\,du\,dv$. Es spielt dieselbe Rolle wie der Betrag der
Jacobi-Determinante beim Volumenintegral: der lokale Flächen-Streckfaktor beim Übergang vom Parametergebiet zur
echten Fläche.

:::grafik
Ein Koordinatenkästchen $du\times dv$ wird auf ein Parallelogramm mit Kanten $\partial_u x\,du$, $\partial_v x\,dv$
in der Tangentialebene abgebildet; seine Fläche $|\partial_u x\times\partial_v x|\,du\,dv=\sqrt{EG-F^2}\,du\,dv$ ist
hervorgehoben, der Normalenvektor $n$ steht senkrecht. Beschriftung der metrischen Koeffizienten $E,F,G$.
:::

## Das Oberflächenintegral

Für eine in einer Umgebung der Fläche stetige Funktion $f$ ist das __Oberflächenintegral__

$$\int_{\mathcal{F}} f\,d\sigma := \int_B f(x(u,v))\,\sqrt{EG - F^2}\,du\,dv.$$

Der Spezialfall $f\equiv1$ gibt den __Flächeninhalt__ $A(\mathcal{F})=\int_B\sqrt{EG-F^2}\,du\,dv$. Wichtig: Dank der
Transformationsformel für den metrischen Tensor ($\sqrt{\det g'}=\sqrt{\det(g\circ\Psi)}\,|\det D\Psi|$) ist das
Oberflächenintegral **unabhängig von der Wahl der Parametrisierung** — es ist eine echte geometrische Größe. Für
geschlossene Flächen (Kugel, Quaderrand) setzt man die Fläche aus endlich vielen regulären __Flächenstücken__
zusammen und summiert die Integrale (das löst das „Injektivitätsdilemma" geschlossener Flächen).

## Beispiele

**Kugeloberfläche.** Die Sphäre $\partial B_R(0)$ parametrisiert man über Kugelkoordinaten mit festem $r=R$,
$x(\vartheta,\varphi)=R(\sin\vartheta\cos\varphi,\ \sin\vartheta\sin\varphi,\ \cos\vartheta)$. Das Oberflächenelement
wird $d\sigma=R^2\sin\vartheta\,d\vartheta\,d\varphi$, also

$$\int_{\partial B_R(0)} f\,d\sigma = R^2\int_0^{2\pi}\!\int_0^{\pi} f(x(\vartheta,\varphi))\,\sin\vartheta\,d\vartheta\,d\varphi.$$

**Eigenes Beispiel (Kugelfläche):** Mit $f\equiv1$ ist $A = R^2\int_0^{2\pi}\!\int_0^{\pi}\sin\vartheta\,d\vartheta
\,d\varphi = R^2\cdot 2\pi\cdot 2 = 4\pi R^2$ — die bekannte Kugeloberfläche.

**Graphenflächen.** Ist die Fläche der Graph einer Funktion $H(x,y)$, also $x(x,y)=(x,y,H(x,y))$, so sind
$E=1+H_x^2$, $F=H_x H_y$, $G=1+H_y^2$, und das Oberflächenelement vereinfacht sich zu

$$d\sigma = \sqrt{1 + \lvert\nabla H\rvert^2}\,dx\,dy.$$

Der Faktor $\sqrt{1+|\nabla H|^2}\ge1$ ist anschaulich: Je steiler der Graph, desto mehr Fläche steckt über
demselben Grundriss-Kästchen.

**Rotationsflächen.** Rotiert man ein Profil $(x(t),z(t))$ um die $z$-Achse, so hat die entstehende Fläche den
Inhalt $A=2\pi\int_a^b \sqrt{\dot x(t)^2+\dot z(t)^2}\,\lvert x(t)\rvert\,dt$ (die Guldinsche Mantelformel: Bogenlänge
mal Umfang des Kreises, den der Punkt beschreibt).

:::grafik
Drei Flächen mit ihrem Oberflächenelement: (1) Kugel mit $d\sigma=R^2\sin\vartheta\,d\vartheta\,d\varphi$ (Maschen
schrumpfen zu den Polen); (2) Graph $z=H(x,y)$ mit $d\sigma=\sqrt{1+|\nabla H|^2}\,dx\,dy$ (steiler → mehr Fläche);
(3) Rotationsfläche mit Profil $(x(t),z(t))$ und Guldin-Formel.
:::

:::kern
Ein __reguläres Flächenstück__ ist das Bild einer injektiven, stetig differenzierbaren Parametrisierung
$x(u,v)$ mit $\partial_u x\times\partial_v x\ne0$; die Tangenten $\partial_u x,\partial_v x$ spannen die
__Tangentialebene__ auf, $n=\frac{\partial_u x\times\partial_v x}{|\partial_u x\times\partial_v x|}$ ist die
Einheitsnormale. Die __metrischen Koeffizienten__ $E=|\partial_u x|^2$, $F=\partial_u x\cdot\partial_v x$,
$G=|\partial_v x|^2$ liefern das __Oberflächenelement__ $d\sigma=\sqrt{EG-F^2}\,du\,dv=|\partial_u x\times\partial_v x|
\,du\,dv$ (lokaler Flächen-Streckfaktor). __Oberflächenintegral__ $\int_{\mathcal F}f\,d\sigma=\int_B f(x(u,v))
\sqrt{EG-F^2}\,du\,dv$ (parametrisierungsunabhängig; $f\equiv1$ → Flächeninhalt; geschlossene Flächen stückweise).
Beispiele: Kugel $d\sigma=R^2\sin\vartheta\,d\vartheta\,d\varphi$ ($A=4\pi R^2$); Graph $d\sigma=\sqrt{1+|\nabla H|^2}
\,dx\,dy$; Rotationsfläche $A=2\pi\int\sqrt{\dot x^2+\dot z^2}\,|x(t)|\,dt$.
:::

Mit dem Oberflächenintegral können wir **Flüsse** von Vektorfeldern durch Flächen messen — und damit die großen
räumlichen Integralsätze formulieren. Der erste ist der __Satz von Stokes im Raum__, der die Zirkulation längs der
Randkurve einer Fläche mit dem Rotationsfluss durch die Fläche verbindet: das Thema des nächsten Artikels.

:::quiz
F: Warum braucht man für eine gekrümmte Fläche überhaupt ein eigenes „Flächenelement" $d\sigma$ und nicht einfach $du\,dv$?
A: Weil die Parametrisierung ein ebenes Kästchen $du\times dv$ auf ein verzerrtes Parallelogramm auf der Fläche abbildet, dessen echte Fläche größer oder kleiner ist. $d\sigma$ ist der lokale Streckfaktor, der jedes Parameterkästchen auf seinen tatsächlichen Flächeninhalt umrechnet.
F: Was bedeutet die Regularitätsbedingung $\partial_u x\times\partial_v x\ne0$ anschaulich?
A: Sie garantiert, dass die beiden Tangentenvektoren linear unabhängig sind, also wirklich eine Ebene (die Tangentialebene) aufspannen. Verschwindet das Kreuzprodukt, fallen die Tangenten zusammen oder einer wird null — die Fläche entartet zu einer Spitze oder Kante.
F: Warum ist das Oberflächenelement gerade der Betrag des Kreuzprodukts $|\partial_u x\times\partial_v x|$?
A: Der Betrag eines Kreuzprodukts zweier Vektoren ist genau die Fläche des von ihnen aufgespannten Parallelogramms. Die Kanten des Bildkästchens sind $\partial_u x\,du$ und $\partial_v x\,dv$, also ist dessen Fläche $|\partial_u x\times\partial_v x|\,du\,dv$.
F: Wie hängen die metrischen Koeffizienten $E,F,G$ mit dem Kreuzprodukt zusammen, und warum?
A: Es gilt $\sqrt{EG-F^2}=|\partial_u x\times\partial_v x|$ (Lagrange-Identität). $EG$ ist das Produkt der Kantenlängen-Quadrate, und $F^2$ zieht den Anteil ab, der auf den Winkel zwischen den Tangenten (die Scherung) entfällt — übrig bleibt die reine Parallelogrammfläche.
F: Welche Rolle spielt $F=\partial_u x\cdot\partial_v x$ geometrisch?
A: $F$ misst, wie schief die beiden Tangentenrichtungen zueinander stehen (ihr Skalarprodukt). Bei orthogonalen Koordinatenlinien ist $F=0$, und das Flächenelement vereinfacht sich zu $\sqrt{EG}$; $F\ne0$ bedeutet, die Parameterlinien schneiden sich schräg.
F: Warum ist das Oberflächenintegral unabhängig von der gewählten Parametrisierung?
A: Bei einem Parameterwechsel $\Psi$ transformiert sich $\sqrt{\det g}$ gerade mit $|\det D\Psi|$, und dieser Faktor wird vom Transformationssatz für das $du\,dv$-Integral exakt kompensiert. Übrig bleibt derselbe Wert — das Integral ist eine echte geometrische Größe der Fläche.
F: Warum schrumpfen die Flächenmaschen der Kugel zu den Polen hin, und wie zeigt sich das im $d\sigma$?
A: Das Oberflächenelement der Kugel ist $R^2\sin\vartheta\,d\vartheta\,d\varphi$; der Faktor $\sin\vartheta$ geht an den Polen ($\vartheta=0,\pi$) gegen null. Das spiegelt, dass die Breitenkreise zu den Polen hin zusammenlaufen, ein Azimutschritt $d\varphi$ dort also kaum Fläche überstreicht.
F: Warum ist das Graphen-Flächenelement $\sqrt{1+|\nabla H|^2}\,dx\,dy$ immer mindestens so groß wie $dx\,dy$?
A: Der Graph liegt über dem Grundriss-Kästchen geneigt; je steiler (größer $|\nabla H|$), desto mehr geneigte Fläche steckt über derselben Grundfläche. Da $|\nabla H|^2\ge0$, ist der Faktor $\sqrt{1+|\nabla H|^2}\ge1$ — bei waagerechtem Graphen ($\nabla H=0$) genau $1$.
F: Wie berechnet man die Kugeloberfläche $4\pi R^2$ aus dem Oberflächenintegral?
A: Mit $f\equiv1$ und $d\sigma=R^2\sin\vartheta\,d\vartheta\,d\varphi$ separiert das Integral: $R^2\int_0^{2\pi}d\varphi\int_0^\pi\sin\vartheta\,d\vartheta=R^2\cdot2\pi\cdot2=4\pi R^2$. Das Radialintegral entfällt, weil der Radius auf $R$ festgehalten ist.
F: Wie geht man mit geschlossenen Flächen (Kugel, Quaderrand) um, obwohl eine einzige Parametrisierung dort nicht injektiv sein kann?
A: Man zerlegt die geschlossene Fläche in endlich viele reguläre Flächenstücke, integriert über jedes einzeln und summiert. So umgeht man das „Injektivitätsdilemma", denn jedes Teilstück besitzt eine saubere injektive Parametrisierung.
:::
