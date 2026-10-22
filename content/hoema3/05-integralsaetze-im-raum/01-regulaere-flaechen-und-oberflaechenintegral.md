---
title: Reguläre Flächen und das Oberflächenintegral
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3050100
summary: Von Grund auf – wie man über eine gekrümmte Fläche im Raum integriert. Leitbild ist das Gummituch aus dem Transformationssatz, das als Haut über eine Form gezogen wird – ohne Falten und ohne Knicke. Jede Masche ist unter der Lupe ein Parallelogramm in der Tangentialebene, mit der Fläche $\lvert\partial_u\vec\Phi\times\partial_v\vec\Phi\rvert\,du\,dv=\sqrt{EG-F^2}\,du\,dv$. Mit regulären Flächenstücken, metrischen Koeffizienten, der Unabhängigkeit von der Parametrisierung, Flächen aus Flicken, Kugel, Rotationsflächen (Guldin) und Graphen $\sqrt{1+\lvert\nabla h\rvert^2}$. Mit Beispiel-Seite.
tags: reguläres Flächenstück, Parametrisierung, Tangentialebene, Normalenvektor, metrische Koeffizienten, Oberflächenelement, Oberflächenintegral, Flächeninhalt
---

## Anschaulich

Bisher wurde über Kurven, ebene Gebiete und Körper integriert. Jetzt kommen gekrümmte Flächen im Raum dazu: die Oberfläche
einer Kugel, ein Zeltdach, eine Membran. Wie viel Farbe braucht eine Kuppel, wie viel Ladung sitzt auf einer geladenen
Kugelschale, wie viel Feld fließt durch eine Fläche?

**Das Leitbild dieses Artikels:** Das **Gummituch** aus dem Artikel über den Transformationssatz wird zur **Haut**. Man zieht
das karierte Tuch über eine Form — eine Kugel, ein Dach, einen Kegel. Aus jedem kleinen Quadrat des Gitters wird eine
**Masche** auf der gekrümmten Fläche. Unter der Lupe liegt sie in einer Ebene, der __Tangentialebene__, und ist fast ein
Parallelogramm; seine Fläche ist der Betrag des Kreuzprodukts seiner beiden Kanten.

Ein gutes Tuch erfüllt zwei Regeln: Es liegt nirgends doppelt, schlägt also keine Falten, und es hat keine Knicke oder
Spitzen, an denen die beiden Kanten einer Masche in dieselbe Richtung zeigen. Eine geschlossene Fläche wie die Kugel lässt
sich so nicht mit einem einzigen Tuch überziehen — man näht sie wie einen Fußball aus mehreren **Flicken** zusammen.

Das __Oberflächenintegral__ zählt alle Maschen zusammen, jede mit dem Wert der Funktion dort mal ihrer Fläche.

:::grafik
Szene: hoema3/integralsaetze-im-raum/01-tuch-als-haut · Vorlage: parametrisierung-flaeche-3d
Links ein kariertes Rechteck in den Parametern $(u,v)$, rechts sein Bild als gewölbte Fläche im Raum. Eine Masche ist links und
rechts hervorgehoben; rechts liegt sie fast in der Tangentialebene, die als durchscheinendes Plättchen eingeblendet wird, mit
den Kantenpfeilen $\partial_u\vec\Phi\,du$ und $\partial_v\vec\Phi\,dv$ und dem Normalenpfeil senkrecht dazu. Ein Zähler zeigt die
Maschenfläche als Betrag des Kreuzprodukts. Ein Umschalter wechselt zur Kugel: Ein Tuch reicht nicht, erst mehrere Flicken
überziehen sie. Kernaussage: Eine Fläche integriert man Masche für Masche, jede mit ihrer echten Fläche. (Rot = Masche, blau =
Gitter, orange = Kanten und Normale, grau = Achsen.)
:::

## Reguläre Flächenstücke

**Die Akteure:** ein Gebiet $W\subseteq\mathbb{R}^2$ — offen und zusammenhängend —, eine stetig
differenzierbare Abbildung

$$\vec\Phi:W\to\mathbb{R}^3, \qquad \vec\Phi(u,v) = \big(x(u,v),\ y(u,v),\ z(u,v)\big),$$

und ein regulärer Bereich $B\subseteq W$, dessen Inneres einfach zusammenhängend ist; sein Rand ist dann eine einzige
geschlossene Kurve. Ist $\vec\Phi$ auf $B$ injektiv und gilt

$$\partial_u\vec\Phi\times\partial_v\vec\Phi\neq\vec 0 \quad\text{auf } B,$$

so heißt die Bildmenge

:::formel Definition
$$S = \big\{\vec x\in\mathbb{R}^3 : \vec x = \vec\Phi(u,v)\ \text{für ein}\ (u,v)\in B\big\}$$
:::

ein __reguläres Flächenstück__ und $\vec\Phi$ eine __reguläre Parametrisierung__ von $S$.

**So liest man das:** Die Parametrisierung nimmt zwei Zahlen $(u,v)$ und gibt einen Punkt im Raum aus. Die Ableitungen
$\partial_u\vec\Phi$ und $\partial_v\vec\Phi$ sind die __Tangentenvektoren__ an die Linien, auf denen nur $u$ bzw. nur $v$ läuft. Ihr
Kreuzprodukt ist genau dann nicht null, wenn die beiden Tangenten nicht in dieselbe Richtung zeigen.

**Im Bild:** Das Tuch über der Form. Injektiv heißt: keine Falten, das Tuch liegt nirgends doppelt. Das nicht verschwindende
Kreuzprodukt heißt: keine Knicke und keine Spitzen, jede Masche bleibt ein echtes Parallelogramm.

An jedem Punkt der Fläche entsteht daraus ein kleines Dreibein aus den normierten Tangenten und dem __Einheitsnormalenvektor__:

$$\vec t_1 = \frac{\partial_u\vec\Phi}{\lvert\partial_u\vec\Phi\rvert}, \qquad \vec t_2 = \frac{\partial_v\vec\Phi}{\lvert\partial_v\vec\Phi\rvert}, \qquad \vec n = \frac{\partial_u\vec\Phi\times\partial_v\vec\Phi}{\lvert\partial_u\vec\Phi\times\partial_v\vec\Phi\rvert}.$$

Diese drei Vektoren bilden an jedem Punkt eine **normierte Basis** des $\mathbb{R}^3$: drei Vektoren der Länge $1$, die den Raum
aufspannen. Orthonormal sind sie im Allgemeinen nicht — die beiden Tangenten dürfen schräg zueinander stehen.

:::herleitung
Weil das Kreuzprodukt nicht null ist, sind die beiden Tangenten linear unabhängig, insbesondere selbst nicht null; man darf
also durch ihre Längen teilen. Das Kreuzprodukt steht senkrecht auf beiden Tangenten. Ein Vektor, der senkrecht auf einer
Ebene steht und nicht null ist, liegt nicht in ihr. Die drei Vektoren sind also linear unabhängig und bilden eine Basis, und
nach dem Normieren hat jeder die Länge $1$.

Senkrecht stehen nur $\vec n$ und die Tangenten; der Winkel zwischen den beiden Tangenten ist beliebig.

**Im Bild:** Die zwei Kanten einer Masche liegen in der Tangentialebene, die Normale steht wie ein Fahnenmast darauf. Ist das
Gitter schief, ist es auch die Masche.
:::

::::beispiel Drei Flächenstücke und eine Spitze
**(a) Eine schiefe Ebene.** Die Parametrisierung

$$\vec\Phi(u,v) = (u+v,\ v,\ 0), \qquad \partial_u\vec\Phi = (1,\ 0,\ 0), \qquad \partial_v\vec\Phi = (1,\ 1,\ 0)$$

beschreibt ein Stück der $xy$-Ebene mit schiefem Gitter. Das Kreuzprodukt ist $(0,0,1)$, und das Dreibein besteht aus

$$\vec t_1 = (1,\ 0,\ 0), \qquad \vec t_2 = \frac{1}{\sqrt2}\,(1,\ 1,\ 0), \qquad \vec n = (0,\ 0,\ 1).$$

Die Tangenten schließen den Winkel $45^\circ$ ein: eine normierte Basis, aber keine orthonormale.

**(b) Ein Zylindermantel** vom Radius $R$:

$$\vec\Phi(\varphi,z) = (R\cos\varphi,\ R\sin\varphi,\ z), \qquad \partial_\varphi\vec\Phi\times\partial_z\vec\Phi = (R\cos\varphi,\ R\sin\varphi,\ 0).$$

Die Normale zeigt von der Achse weg, und das Kreuzprodukt hat überall die Länge $R$.

**(c) Ein Kegel mit Spitze im Ursprung.** Für

$$\vec\Phi(t,\varphi) = (t\cos\varphi,\ t\sin\varphi,\ t), \qquad \partial_t\vec\Phi\times\partial_\varphi\vec\Phi = (-t\cos\varphi,\ -t\sin\varphi,\ t)$$

ist das Kreuzprodukt bei $t=0$ null. An der Spitze ist der Kegel kein reguläres Flächenstück, abseits davon schon.

**Im Bild:** Bei (a) ist das Tuch flach, aber schief kariert. Bei (c) laufen alle Maschen an der Spitze zu einem Punkt zusammen
— dort ist das Tuch gerafft, und eine Tangentialebene gibt es nicht.
::::

## Maschen ausmessen

Wie groß ist eine Masche? Ihre beiden Kanten sind $\partial_u\vec\Phi\,du$ und $\partial_v\vec\Phi\,dv$. Ihre Längen und ihren Winkel
erfassen die __metrischen Koeffizienten__ — so heißen sie seit Gauß —, zusammengefasst im __metrischen Tensor__ $g$:

$$E = \lvert\partial_u\vec\Phi\rvert^2, \qquad F = \partial_u\vec\Phi\cdot\partial_v\vec\Phi, \qquad G = \lvert\partial_v\vec\Phi\rvert^2, \qquad g = \begin{pmatrix}E&F\\F&G\end{pmatrix}.$$

Die Funktion $\sqrt{\det g}$ heißt __Oberflächenelement__ der Fläche, und es gilt

:::formel Lemma
$$\sqrt{\det g} = \sqrt{EG-F^2} = \big\lvert\partial_u\vec\Phi\times\partial_v\vec\Phi\big\rvert.$$
:::

**So liest man das:** $E$ und $G$ sind die Quadrate der Maschenkanten pro Parameterschritt, $F$ misst, wie schief sie
zueinander stehen. Daraus ergibt sich die Maschenfläche pro Parameterfläche, ohne ein Kreuzprodukt auszurechnen.

**Im Bild:** $EG$ wäre die Fläche zum Quadrat, wenn die Masche ein Rechteck wäre. $F^2$ zieht ab, was die Schräglage kostet —
übrig bleibt das Quadrat der Parallelogrammfläche.

:::herleitung
Für zwei Vektoren $\vec p$ und $\vec q$ mit dem Winkel $\alpha$ ist nach der linearen Algebra

$$\lvert\vec p\times\vec q\rvert = \lvert\vec p\rvert\,\lvert\vec q\rvert\sin\alpha, \qquad \vec p\cdot\vec q = \lvert\vec p\rvert\,\lvert\vec q\rvert\cos\alpha.$$

Mit $\sin^2\alpha+\cos^2\alpha=1$ folgt die __Lagrange-Identität__

$$\lvert\vec p\times\vec q\rvert^2 = \lvert\vec p\rvert^2\,\lvert\vec q\rvert^2-\big(\vec p\cdot\vec q\big)^2.$$

Für die beiden Tangenten ist die rechte Seite $EG-F^2$, die Determinante von $g$. Der Betrag des Kreuzprodukts ist die Fläche des
Parallelogramms aus beiden Vektoren.
:::

::::beispiel Maschen ausmessen
**(a) Die schiefe Ebene** von eben hat

$$E = 1, \qquad F = 1, \qquad G = 2, \qquad \sqrt{EG-F^2} = \sqrt{2-1} = 1.$$

Jede Masche hat die Fläche ihres Parameterquadrats — eine Scherung wie im Artikel über den Transformationssatz.

**(b) Die Kugel** vom Radius $R$ in Kugelkoordinaten mit festem Radius:

$$\vec\Phi(\theta,\varphi) = R\,(\sin\theta\cos\varphi,\ \sin\theta\sin\varphi,\ \cos\theta), \qquad E = R^2, \qquad F = 0, \qquad G = R^2\sin^2\theta.$$

Das Oberflächenelement ist $R^2\sin\theta$ — das Produkt der Maßfaktoren $r$ und $r\sin\theta$ aus dem Artikel über krummlinige
Koordinaten, bei $r=R$.

**(c) Der Zylindermantel** hat die metrischen Koeffizienten

$$E = R^2, \qquad F = 0, \qquad G = 1,$$

also das Oberflächenelement $R$, wie das Kreuzprodukt.

**Im Bild:** Bei (b) und (c) ist das Gitter rechtwinklig, $F$ ist null. Auf der Kugel werden die Maschen zu den Polen hin
schmal, weil der Breitenkreis schrumpft.
::::

## Umparametrisieren ändert nichts

Dasselbe Flächenstück lässt sich auf viele Arten parametrisieren — dasselbe Tuch mit einem anderen Gitter bemalt. Seien
$\vec\Phi$ auf $B$ und $\vec\Phi\circ\vec\Psi$ auf $B'$ zwei reguläre Parametrisierungen von $S$, verbunden durch einen
__Parameterwechsel__: eine bijektive, stetig differenzierbare Abbildung $\vec\Psi:B'\to B$ mit $\det D\vec\Psi\neq0$. Für den
metrischen Tensor $\tilde g$ der zweiten Parametrisierung gilt

:::formel Lemma
$$\tilde g = D\vec\Psi^{\mathsf T}\,\big(g\circ\vec\Psi\big)\,D\vec\Psi, \qquad \sqrt{\det\tilde g} = \sqrt{\det\big(g\circ\vec\Psi\big)}\;\big\lvert\det D\vec\Psi\big\rvert.$$
:::

**So liest man das:** Das neue Oberflächenelement ist das alte mal dem Flächenfaktor des Parameterwechsels aus dem
Transformationssatz.

**Im Bild:** Malt man ein feineres oder schieferes Gitter auf dasselbe Tuch, werden die Parametermaschen anders groß — aber
genau um so viel, dass die echte Fläche gleich bleibt.

:::herleitung
Der metrische Tensor ist die Matrix der Skalarprodukte der Spalten von $D\vec\Phi$, also

$$g = D\vec\Phi^{\mathsf T}\,D\vec\Phi.$$

Nach der Kettenregel ist die Jacobi-Matrix der zweiten Parametrisierung $D\vec\Phi(\vec\Psi)\,D\vec\Psi$. Eingesetzt:

$$\tilde g = \big(D\vec\Phi(\vec\Psi)\,D\vec\Psi\big)^{\mathsf T}\,D\vec\Phi(\vec\Psi)\,D\vec\Psi = D\vec\Psi^{\mathsf T}\,\big(g\circ\vec\Psi\big)\,D\vec\Psi.$$

Die Determinante eines Produkts ist das Produkt der Determinanten, und eine Matrix und ihre Transponierte haben dieselbe:

$$\det\tilde g = \big(\det D\vec\Psi\big)^2\,\det\big(g\circ\vec\Psi\big).$$

Die Wurzel gibt die zweite Formel.
:::

::::beispiel Eine Kreisscheibe, zweimal kariert
Die Einheitskreisscheibe in der $xy$-Ebene, einmal mit kartesischem Gitter, einmal mit Polarkoordinaten:

$$\vec\Phi(x,y) = (x,\ y,\ 0), \qquad \vec\Psi(\varrho,\varphi) = (\varrho\cos\varphi,\ \varrho\sin\varphi).$$

Kartesisch ist $g$ die Einheitsmatrix und das Oberflächenelement $1$. Für das Polargitter gibt das Lemma

$$\tilde g = D\vec\Psi^{\mathsf T}D\vec\Psi = \begin{pmatrix}1&0\\0&\varrho^2\end{pmatrix}, \qquad \sqrt{\det\tilde g} = \varrho = 1\cdot\big\lvert\det D\vec\Psi\big\rvert.$$

Beide Gitter geben dieselbe Fläche $\pi$ — kartesisch das Integral der $1$ über die Kreisscheibe, polar wie im Artikel über den
Transformationssatz das Integral von $\varrho$ über das Rechteck.

**Im Bild:** Dasselbe flache Tuch, einmal mit Karos, einmal mit einem Spinnennetz bemalt. Die Spinnennetz-Maschen sind
außen größer, und genau das gleicht der Faktor $\varrho$ aus.
::::

## Das Oberflächenintegral

**Die Akteure:** ein reguläres Flächenstück $S=\vec\Phi(B)$ und eine Funktion $f:U\to\mathbb{R}$, die auf einer offenen Menge
$U\subseteq\mathbb{R}^3$ um $S$ stetig ist. Das __Oberflächenintegral__ von $f$ über $S$ ist

:::formel Definition
$$\int_S f\,d\sigma := \int_B f\big(\vec\Phi(u,v)\big)\,\sqrt{\det g(u,v)}\;du\,dv.$$
:::

Formal ist also

$$d\sigma = \sqrt{\det g(u,v)}\;du\,dv = \sqrt{E(u,v)\,G(u,v)-F(u,v)^2}\;du\,dv,$$

und mit $f=1$ entsteht der __Flächeninhalt__

$$\lvert S\rvert = \int_B\sqrt{E(u,v)\,G(u,v)-F(u,v)^2}\;du\,dv.$$

**So liest man das:** Rechts steht ein gewöhnliches Integral über den ebenen Parameterbereich. Das Oberflächenelement rechnet
jede Parametermasche in ihre echte Fläche um.

**Im Bild:** Die Summe über alle Maschen des Tuchs, jede mit dem Wert der Funktion mal ihrer Fläche. Bei $f=1$ misst man nur
die Haut selbst.

Die Definition hängt nicht von der Parametrisierung ab: Jede reguläre Parametrisierung desselben Flächenstücks gibt denselben
Wert.

:::herleitung
Sei $\vec\Phi\circ\vec\Psi$ eine zweite Parametrisierung auf $B'$. Nach dem Lemma über den Parameterwechsel ist ihr Integral

$$\int_{B'}f\big(\vec\Phi(\vec\Psi)\big)\sqrt{\det\tilde g}\;ds\,dt = \int_{B'}f\big(\vec\Phi(\vec\Psi)\big)\sqrt{\det\big(g\circ\vec\Psi\big)}\;\big\lvert\det D\vec\Psi\big\rvert\;ds\,dt.$$

Das ist die rechte Seite des Transformationssatzes für die Substitution $(u,v)=\vec\Psi(s,t)$ und die Funktion
$f(\vec\Phi)\sqrt{\det g}$. Also ist es gleich dem Integral über $B$ in der ersten Parametrisierung.

**Im Bild:** Ein anderes Gitter auf demselben Tuch zählt dieselbe Haut, nur in anderen Stücken.
:::

::::beispiel Eine Dachrinne
Die untere Hälfte eines Rohrs vom Radius $R$ und der Länge $L$ ist ein reguläres Flächenstück:

$$\vec\Phi(\varphi,z) = (R\cos\varphi,\ R\sin\varphi,\ z), \qquad (\varphi,z)\in[\pi,2\pi]\times[0,L].$$

Mit dem Oberflächenelement $R$ ist ihr Flächeninhalt

$$\lvert S\rvert = \int_0^L\int_\pi^{2\pi}R\,d\varphi\,dz = \pi RL.$$

Die Tiefe eines Punkts unter dem Rand ist $-y$. Ihr Integral über die Rinne ist

$$\int_S(-y)\,d\sigma = \int_0^L\int_\pi^{2\pi}\big(-R\sin\varphi\big)\,R\,d\varphi\,dz = R^2L\,\big[\cos\varphi\big]_\pi^{2\pi} = 2R^2L.$$

Geteilt durch die Fläche ist die mittlere Tiefe der Rinnenwand $\frac{2R}{\pi}\approx0{,}64\,R$.

**Im Bild:** Die Haut der Rinne zählt Masche für Masche; die Maschen am Boden sind tief, die am Rand flach, und im Mittel liegt
die Wand bei knapp zwei Dritteln des Radius.
::::

## Geschlossene Flächen aus Flicken

Reguläre Flächenstücke sind beim Integrieren handlich, aber nur eine eingeschränkte Klasse von Flächen passt hinein. Bei
geschlossenen Flächen gibt es ein __Injektivitätsdilemma__: Eine Kugel oder der Rand eines Würfels ist nicht das injektive Bild
eines einzigen Parameterbereichs mit einfach zusammenhängendem Inneren. Man setzt sie deshalb aus Stücken zusammen.

Eine __stückweise reguläre Fläche__ $S$ besteht aus endlich vielen regulären Flächenstücken $S_1,\ldots,S_N$, die sich höchstens an
ihren Rändern überlappen. Man setzt

:::formel Definition
$$\int_S f\,d\sigma := \sum_{k=1}^N\int_{S_k}f\,d\sigma.$$
:::

**So liest man das:** Man integriert über jedes Stück einzeln und addiert. Die Ränder, an denen sich die Stücke berühren, sind
Kurven und haben keine Fläche.

**Im Bild:** Der Fußball aus Flicken. Jeder Flicken ist ein eigenes, faltenfreies Tuch, und die Nähte zählen nicht.

Beispiele sind der Rand einer Kugel oder eines Quaders. Oft genügt aber doch eine einzige Parametrisierung, wenn man an
dünnen Nähten eine kleine Verletzung der Regeln zulässt — wie bei der Kugel im nächsten Abschnitt.

::::beispiel Die Würfelhaut
Der Rand des Einheitswürfels $[0,1]^3$ besteht aus sechs Quadraten. Jedes ist ein reguläres Flächenstück mit dem
Oberflächenelement $1$, zusammen also die Fläche $6$.

Für die Funktion, die jedem Punkt seine $x$-Koordinate zuordnet, tragen die sechs Seiten verschieden bei: die Seite in der
Ebene $x=0$ nichts, die gegenüberliegende ihre Fläche $1$, und die vier übrigen Seiten je das Integral von $x$ über ein
Einheitsquadrat, also $\frac12$:

$$\int_S x\,d\sigma = 0+1+4\cdot\frac12 = 3.$$

**Im Bild:** Sechs flache Flicken; die Kanten und Ecken, an denen sie zusammenstoßen, haben keine Fläche und fallen nicht ins
Gewicht.
::::

## Die Kugeloberfläche

Die Kugeloberfläche vom Radius $R$,

$$\partial K_R = \big\{\vec x\in\mathbb{R}^3 : \lvert\vec x\rvert = R\big\},$$

parametrisiert man mit Kugelkoordinaten bei festem Radius, wie beim Ausmessen der Maschen. Diese Parametrisierung ist auf
$[0,\pi]\times[0,2\pi]$ nicht injektiv und entartet an den Polen; trotzdem gilt

:::formel
$$\int_{\partial K_R}f\,d\sigma = R^2\int_0^{2\pi}\int_0^{\pi}f\big(\vec\Phi(\theta,\varphi)\big)\,\sin\theta\;d\theta\,d\varphi.$$
:::

**So liest man das:** Das Oberflächenelement der Kugel ist $R^2\sin\theta\,d\theta\,d\varphi$. Üblich ist für die Kugel auch die
Schreibweise $\partial B_R(0)$.

**Im Bild:** Das Gradnetz des Globus aus dem Artikel über
[krummlinige Koordinaten](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen/krummlinige-koordinaten.html).
Die Maschen sind am Äquator am größten und laufen zu den Polen
hin zu schmalen Zwickeln zusammen.

:::herleitung
Auf dem kleineren Rechteck $[\varepsilon,\pi-\varepsilon]\times[\varepsilon,2\pi]$ ist die Parametrisierung injektiv, und das
Kreuzprodukt hat die Länge $R^2\sin\theta$, die dort nicht null wird: ein reguläres Flächenstück, auf dem die Formel gilt. Es
fehlen nur zwei kleine Polkappen und ein schmaler Streifen längs eines Halbmeridians.

Jede Polkappe ist der Graph einer Funktion über einer kleinen Kreisscheibe vom Radius $R\sin\varepsilon$; nach der Formel für
Graphen weiter unten hat sie die Fläche $2\pi R^2(1-\cos\varepsilon)$. Der Streifen gehört zu einem Parameterstreifen der
Breite $\varepsilon$, und seine Fläche ist höchstens $2\pi R^2\varepsilon$. Beides geht für $\varepsilon\to0$ gegen null. Weil $f$
auf der Kugel beschränkt ist, verschwinden auch die Beiträge zum Integral, und die Formel gilt für die ganze Kugel.

**Im Bild:** Man schneidet am Nord- und Südpol eine winzige Kappe ab und trennt eine Naht auf — auf dem Rest liegt das Tuch
glatt, und das Abgeschnittene wird beliebig klein.
:::

::::beispiel Kugel, Erde und ein Mittelwert
**(a) Die Kugeloberfläche** mit $f=1$:

$$\lvert\partial K_R\rvert = R^2\int_0^{2\pi}\int_0^\pi\sin\theta\;d\theta\,d\varphi = R^2\cdot2\pi\cdot2 = 4\pi R^2.$$

Mit dem Erdradius $6371\,\mathrm{km}$ ist die Erdoberfläche

$$4\pi\cdot\big(6371\,\mathrm{km}\big)^2\approx5{,}10\cdot10^8\,\mathrm{km}^2.$$

**(b) Das Quadrat der Höhe** $z=R\cos\theta$:

$$\int_{\partial K_R}z^2\,d\sigma = R^4\int_0^{2\pi}\int_0^\pi\cos^2\theta\,\sin\theta\;d\theta\,d\varphi = R^4\cdot2\pi\cdot\frac23 = \frac{4\pi}{3}\,R^4.$$

Zur Probe: Auf der Kugel ist $x^2+y^2+z^2=R^2$, das Integral der Summe also $R^2\cdot4\pi R^2$; aus Symmetrie trägt jede der drei
Koordinaten ein Drittel bei.

**Im Bild:** Bei (b) zählen die Maschen in Polnähe mit großem $z^2$, sind aber schmal; die breiten Maschen am Äquator haben
kleines $z^2$. Im Mittel kommt ein Drittel von $R^2$ heraus.
::::

## Rotationsflächen

Dreht man ein Profil um die $z$-Achse, entsteht eine __Rotationsfläche__ — die Haut eines Werkstücks von der Drehbank aus dem
Artikel über Volumenintegrale. **Die Akteure:** eine stetig differenzierbare Profilkurve auf einem offenen Intervall
$I\subseteq\mathbb{R}$, mit dem Abstand $\varrho(t)$ zur Achse und der Höhe $\zeta(t)$, und ein Intervall $[a,b]\subseteq I$:

$$\vec\gamma(t) = \big(\varrho(t),\ \zeta(t)\big), \qquad \vec\Phi(t,\varphi) = \big(\varrho(t)\cos\varphi,\ \varrho(t)\sin\varphi,\ \zeta(t)\big), \qquad (t,\varphi)\in[a,b]\times[0,2\pi].$$

Der Flächeninhalt ist

:::formel
$$\lvert S\rvert = 2\pi\int_a^b\sqrt{\dot\varrho(t)^2+\dot\zeta(t)^2}\;\lvert\varrho(t)\rvert\;dt.$$
:::

**So liest man das:** $\sqrt{\dot\varrho^2+\dot\zeta^2}\,dt$ ist die Bogenlänge eines kleinen Profilstücks, $2\pi\lvert\varrho\rvert$ der Umfang
des Kreises, auf dem es um die Achse läuft. Die Fläche ist Bogenlänge mal Umfang, aufsummiert — die __Guldinsche Regel__.

**Im Bild:** Auf der Drehbank zieht jedes Stück des Profils beim Drehen ein schmales Band aus, so breit wie das Profilstück und
so lang wie sein Kreis.

:::herleitung
Die Tangenten sind

$$\partial_t\vec\Phi = \big(\dot\varrho\cos\varphi,\ \dot\varrho\sin\varphi,\ \dot\zeta\big), \qquad \partial_\varphi\vec\Phi = \big(-\varrho\sin\varphi,\ \varrho\cos\varphi,\ 0\big),$$

und die metrischen Koeffizienten

$$E = \dot\varrho^2+\dot\zeta^2, \qquad F = -\dot\varrho\,\varrho\cos\varphi\sin\varphi+\dot\varrho\,\varrho\sin\varphi\cos\varphi = 0, \qquad G = \varrho^2.$$

Das Oberflächenelement ist $\lvert\varrho\rvert\sqrt{\dot\varrho^2+\dot\zeta^2}$, und das Integral über $\varphi$ gibt den Faktor $2\pi$. An der Naht
bei $\varphi=0$ und $2\pi$ und an Stellen, an denen das Profil die Achse berührt, ist das Tuch nicht regulär; die Begründung ist
dieselbe wie bei der Kugel.
:::

::::beispiel Kugel, Torus und Kegel von der Drehbank
**(a) Die Kugel** mit dem Profil $(R\sin t,\ R\cos t)$ auf $[0,\pi]$: Die Bogenlänge pro Parameterschritt ist $R$, und

$$\lvert S\rvert = 2\pi\int_0^\pi R\cdot R\sin t\;dt = 4\pi R^2.$$

**(b) Der Torus**, die Haut eines Rettungsrings: Ein Kreis vom Radius $r_0$, dessen Mittelpunkt im Abstand $c>r_0$ von der Achse
liegt, läuft um die Achse, mit dem Profil $(c+r_0\cos t,\ r_0\sin t)$ auf $[0,2\pi]$. Die Bogenlänge pro Schritt ist $r_0$, und

$$\lvert S\rvert = 2\pi\int_0^{2\pi}r_0\,(c+r_0\cos t)\;dt = 4\pi^2c\,r_0.$$

Für einen Profilkreis vom Radius $1$ im Abstand $2$ sind das $8\pi^2\approx79$ Flächeneinheiten — Umfang des Profilkreises mal Weg
seines Mittelpunkts.

**(c) Der Kegelmantel** mit der Höhe $\ell$ und dem Grundkreisradius $R$ hat das Profil $(\frac{R}{\ell}t,\ t)$ auf $[0,\ell]$. Die
Mantellinie hat die Länge

$$m = \sqrt{R^2+\ell^2},$$

die Bogenlänge pro Schritt ist $\frac{m}{\ell}$, und

$$\lvert S\rvert = 2\pi\int_0^\ell\frac{m}{\ell}\cdot\frac{R}{\ell}\,t\;dt = \pi Rm.$$

Für einen Kegel mit dem Radius $3$ und der Höhe $4$ ist die Mantellinie $5$ lang und die Mantelfläche

$$\pi\cdot3\cdot5 = 15\pi\approx47{,}1.$$

An der Spitze liegt das Profil auf der Achse; dort integriert man erst ab einer kleinen Höhe.

**Im Bild:** Jedes Profilstück zieht auf der Drehbank sein Band aus. Beim Torus sind die Bänder außen länger als innen, im
Mittel so lang wie der Kreis des Mittelpunkts.
::::

## Graphen

Oft ist ein Flächenstück der Graph einer stetig differenzierbaren Funktion $h:W\to\mathbb{R}$ über einem Gebiet $W\subseteq\mathbb{R}^2$
— ein Dach über einem Grundriss. Die Parametrisierung und ihre Tangenten sind

$$\vec\Phi(x,y) = \big(x,\ y,\ h(x,y)\big), \qquad \partial_x\vec\Phi = \big(1,\ 0,\ \partial_xh\big), \qquad \partial_y\vec\Phi = \big(0,\ 1,\ \partial_yh\big),$$

die metrischen Koeffizienten

$$E = 1+\big(\partial_xh\big)^2, \qquad F = \partial_xh\,\partial_yh, \qquad G = 1+\big(\partial_yh\big)^2,$$

und das Oberflächenelement ist

:::formel
$$\sqrt{EG-F^2} = \sqrt{1+\lvert\nabla h(x,y)\rvert^2}.$$
:::

**So liest man das:** Über einem Grundriss-Kästchen der Fläche $dx\,dy$ liegt ein Dachstück der Fläche
$\sqrt{1+\lvert\nabla h\rvert^2}\,dx\,dy$. Der Faktor ist mindestens $1$ und genau dann $1$, wenn das Dach waagerecht ist.

**Im Bild:** Ein Zeltdach. Je steiler es ist, desto mehr Stoff steckt über demselben Stück Boden.

:::herleitung
Ausmultipliziert heben sich die gemischten Terme weg:

$$EG-F^2 = 1+\big(\partial_xh\big)^2+\big(\partial_yh\big)^2+\big(\partial_xh\big)^2\big(\partial_yh\big)^2-\big(\partial_xh\big)^2\big(\partial_yh\big)^2 = 1+\lvert\nabla h\rvert^2.$$

Zur Probe das Kreuzprodukt der Tangenten:

$$\partial_x\vec\Phi\times\partial_y\vec\Phi = \big(-\partial_xh,\ -\partial_yh,\ 1\big).$$

Seine Länge ist dieselbe Wurzel, und es zeigt nach oben.
:::

:::grafik
Szene: hoema3/integralsaetze-im-raum/01-zeltdach · Vorlage: graph-flaechenelement-3d
Ein Graph über einem karierten Grundriss; über einem markierten Kästchen liegt sein Dachstück, hervorgehoben, mit den beiden
Tangentenpfeilen und dem Normalenpfeil. Ein Regler macht das Dach steiler oder flacher, ein Zähler zeigt den Faktor
$\sqrt{1+\lvert\nabla h\rvert^2}$ und die Fläche des Dachstücks im Vergleich zum Kästchen. Kernaussage: Je steiler der Graph, desto mehr
Fläche liegt über demselben Grundriss. (Rot = Dachstück, blau = Grundriss, orange = Tangenten und Normale, grau = Achsen.)
:::

::::beispiel Eine Schüssel und eine Kuppel
**(a) Eine Schüssel**, das Paraboloid über der Einheitskreisscheibe $S_1$ mit

$$h(x,y) = x^2+y^2, \qquad \lvert\nabla h\rvert^2 = 4\big(x^2+y^2\big).$$

In Polarkoordinaten ist ihre Fläche

$$\int_{S_1}\sqrt{1+4\varrho^2}\;d(x,y) = 2\pi\int_0^1\varrho\sqrt{1+4\varrho^2}\;d\varrho = \frac{\pi}{6}\big(5\sqrt5-1\big)\approx5{,}33,$$

rund $70$ Prozent mehr als die flache Scheibe mit $\pi$.

**(b) Eine Kuppel**, die obere Halbkugel als Graph:

$$h(x,y) = \sqrt{R^2-x^2-y^2}, \qquad \sqrt{1+\lvert\nabla h\rvert^2} = \frac{R}{\sqrt{R^2-\varrho^2}}.$$

Am Rand der Kreisscheibe wird das Dach senkrecht und der Faktor unendlich; man integriert bis zum Radius $R-\delta$ und lässt
$\delta$ gegen null gehen. Das Ergebnis ist

$$2\pi\int_0^R\frac{R\,\varrho}{\sqrt{R^2-\varrho^2}}\;d\varrho = 2\pi R\,\Big[-\sqrt{R^2-\varrho^2}\,\Big]_0^R = 2\pi R^2,$$

die Hälfte der Kugeloberfläche — dasselbe wie mit Kugelkoordinaten, wie es die Unabhängigkeit von der Parametrisierung
verlangt.

**Im Bild:** Bei (b) steckt nahe am Rand viel Stoff über wenig Boden, weil die Kuppel dort fast senkrecht steht — trotzdem bleibt
die Summe endlich.
::::

## Bedeutung und Ausblick

Mit dem Oberflächenintegral lässt sich über jede Haut integrieren: Ladungen auf Elektroden, Wärmeströme durch Wände,
Strahlungsleistung durch eine Kugel um eine Antenne. Die Fläche selbst, das Oberflächenelement und die Normale sind die
Bausteine.

Der nächste Schritt sind __Flüsse__: Man integriert nicht eine Zahl, sondern die Normalkomponente eines Vektorfelds über die
Fläche. Dafür braucht die Fläche eine Orientierung — eine Wahl, nach welcher Seite die Normale zeigt. Damit formuliert der
nächste Artikel den Satz von Stokes im Raum.

:::kern
- Ein __reguläres Flächenstück__ ist das injektive Bild $\vec\Phi(B)$ eines regulären Bereichs, mit $\partial_u\vec\Phi\times\partial_v\vec\Phi\neq\vec 0$ — keine Falten, keine Knicke.
- Die Tangenten spannen die __Tangentialebene__ auf; mit der Normale bilden die normierten Tangenten eine normierte, im Allgemeinen nicht orthonormale Basis.
- __Metrische Koeffizienten__: $E$ und $G$ sind die Kantenquadrate einer Masche, $F$ misst ihre Schräglage.
- __Oberflächenelement__: $\sqrt{EG-F^2}=\lvert\partial_u\vec\Phi\times\partial_v\vec\Phi\rvert$ — die Fläche einer Masche pro Parameterfläche.
- Beim Umparametrisieren wird das Oberflächenelement mit $\lvert\det D\vec\Psi\rvert$ multipliziert; deshalb hängt das Oberflächenintegral nicht von der Parametrisierung ab.
- __Oberflächenintegral__: das Integral von $f(\vec\Phi)$ mal Oberflächenelement über den Parameterbereich; mit $f=1$ der Flächeninhalt.
- Geschlossene Flächen setzt man aus regulären Flicken zusammen; die Nähte haben keine Fläche.
- Kugel: Das Oberflächenelement ist $R^2\sin\theta$, die Fläche viermal die eines Großkreises; Rotationsflächen nach Guldin, Bogenlänge mal Umfang.
- Graph: Das Oberflächenelement ist $\sqrt{1+\lvert\nabla h\rvert^2}$ — steiler heißt mehr Fläche.
:::

:::quiz
F: Was ist ein reguläres Flächenstück, und was bedeuten die beiden Bedingungen im Bild des Tuchs?
A: Das Bild $S=\vec\Phi(B)$ eines regulären Bereichs mit einfach zusammenhängendem Inneren unter einer stetig differenzierbaren Abbildung, die auf $B$ injektiv ist und $\partial_u\vec\Phi\times\partial_v\vec\Phi\neq\vec 0$ erfüllt. Injektiv heißt: Das Tuch liegt nirgends doppelt, es schlägt keine Falten. Das Kreuzprodukt ungleich null heißt: keine Knicke oder Spitzen — am Kegel ist es an der Spitze null.
F: Bilden die normierten Tangenten und die Normale eine Orthonormalbasis?
A: Nein, nur eine normierte Basis: drei linear unabhängige Vektoren der Länge $1$. Die Normale steht senkrecht auf beiden Tangenten, die Tangenten selbst dürfen schräg zueinander stehen — bei der Parametrisierung $(u+v,v,0)$ schließen sie $45^\circ$ ein.
F: Was messen die metrischen Koeffizienten, und warum ist $\sqrt{EG-F^2}$ der Betrag des Kreuzprodukts?
A: $E=\lvert\partial_u\vec\Phi\rvert^2$ und $G=\lvert\partial_v\vec\Phi\rvert^2$ sind die Kantenquadrate einer Masche pro Parameterschritt, $F=\partial_u\vec\Phi\cdot\partial_v\vec\Phi$ misst die Schräglage. Nach der Lagrange-Identität ist $\lvert\vec p\times\vec q\rvert^2=\lvert\vec p\rvert^2\lvert\vec q\rvert^2-(\vec p\cdot\vec q)^2$, für die Tangenten also $EG-F^2$ — das Quadrat der Parallelogrammfläche.
F: Warum hängt das Oberflächenintegral nicht von der Parametrisierung ab?
A: Der metrische Tensor ist $g=D\vec\Phi^{\mathsf T}D\vec\Phi$; nach der Kettenregel wird er beim Parameterwechsel zu $D\vec\Psi^{\mathsf T}(g\circ\vec\Psi)D\vec\Psi$, und das Oberflächenelement bekommt den Faktor $\lvert\det D\vec\Psi\rvert$. Genau diesen Faktor verlangt der Transformationssatz, also stimmen beide Integrale überein — bei der Kreisscheibe geben kartesisches und Polargitter beide $\pi$.
F: Wie berechnet man ein Oberflächenintegral über eine Dachrinne?
A: Die untere Hälfte eines Rohrs, $(R\cos\varphi,R\sin\varphi,z)$ mit $\varphi\in[\pi,2\pi]$ und $z\in[0,L]$, hat das Oberflächenelement $R$ und die Fläche $\pi RL$. Das Integral der Tiefe $-y$ ist $\int\int(-R\sin\varphi)R\,d\varphi\,dz=2R^2L$, die mittlere Tiefe also $\frac{2R}{\pi}$.
F: Was ist das Injektivitätsdilemma, und wie integriert man über geschlossene Flächen?
A: Eine geschlossene Fläche wie die Kugel oder der Würfelrand ist nicht das injektive Bild eines einzigen Parameterbereichs mit einfach zusammenhängendem Inneren. Man zerlegt sie in endlich viele reguläre Flicken, die sich nur an den Rändern berühren, und addiert die Integrale. Beim Einheitswürfel gibt $\int x\,d\sigma$ so $0+1+4\cdot\frac12=3$.
F: Warum gilt die Formel für die Kugeloberfläche, obwohl die Parametrisierung an den Polen entartet?
A: Auf $[\varepsilon,\pi-\varepsilon]\times[\varepsilon,2\pi]$ ist die Parametrisierung regulär und injektiv. Es fehlen zwei Polkappen mit je $2\pi R^2(1-\cos\varepsilon)$ und ein schmaler Streifen mit höchstens $2\pi R^2\varepsilon$ Fläche, die für $\varepsilon\to0$ verschwinden. So ergibt sich die Fläche $4\pi R^2$ und etwa $\int z^2\,d\sigma=\frac{4\pi}{3}R^4$.
F: Wie berechnet man die Fläche einer Rotationsfläche, und was ergibt sich für den Torus?
A: Mit dem Profil $(\varrho(t),\zeta(t))$ sind die metrischen Koeffizienten $\dot\varrho^2+\dot\zeta^2$, $0$ und $\varrho^2$, also ist die Fläche $2\pi\int\sqrt{\dot\varrho^2+\dot\zeta^2}\,\lvert\varrho\rvert\,dt$ — Bogenlänge mal Kreisumfang (Guldin). Für den Torus mit dem Profilkreis vom Radius $r_0$ im Abstand $c$ kommt $4\pi^2c\,r_0$ heraus, für den Kegelmantel $\pi R$ mal Mantellinie.
F: Warum ist das Oberflächenelement eines Graphen $\sqrt{1+\lvert\nabla h\rvert^2}$, und was ergibt sich für die Schüssel über der Einheitskreisscheibe?
A: Mit den Tangenten $(1,0,\partial_xh)$ und $(0,1,\partial_yh)$ ist $EG-F^2=1+(\partial_xh)^2+(\partial_yh)^2$, die gemischten Terme heben sich weg. Für $h=x^2+y^2$ ist die Fläche $2\pi\int_0^1\varrho\sqrt{1+4\varrho^2}\,d\varrho=\frac{\pi}{6}(5\sqrt5-1)\approx5{,}33$, rund $70$ Prozent mehr als die flache Scheibe.
F: Wie zeigt die Kuppel, dass die Parametrisierung keine Rolle spielt?
A: Als Graph von $\sqrt{R^2-x^2-y^2}$ hat die Halbkugel das Oberflächenelement $\frac{R}{\sqrt{R^2-\varrho^2}}$, das am Rand unendlich wird; das Integral bleibt endlich und ergibt $2\pi R^2$. Mit Kugelkoordinaten kommt dieselbe Hälfte von $4\pi R^2$ heraus.
:::
