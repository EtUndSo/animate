---
title: Integration über Normalbereiche
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020500
summary: Von Grund auf – wie man ein Doppel- oder Dreifachintegral über ein krummes Gebiet praktisch ausrechnet. Ein Normalbereich ist ein Gebiet, bei dem eine Koordinate zwischen zwei Funktionen der anderen eingeschlossen ist; dann wird das Flächen-/Volumenintegral zu geschachtelten 1D-Integralen mit variablen Grenzen. Kompliziertere Gebiete zerlegt man in mehrere solche Bereiche.
tags: Normalbereich, iteriertes Integral, variable Grenzen, Doppelintegral, Dreifachintegral, Fläche, Zerlegung, räumlicher Normalbereich
---

## Anschaulich

Im vorigen Artikel haben wir Integrale über beliebige Mengen *definiert* (Fortsetzung durch null) — aber noch
nicht praktisch *ausgerechnet*.

Das leisten die __Normalbereiche__: Gebiete, bei denen eine Koordinate sauber **zwischen zwei Funktionen** der
anderen eingeschlossen ist.

Stell dir in der Ebene einen senkrechten „Scanstrich" vor, der von $x=a$ bis $x=b$ wandert. An jeder Stelle $x$
integriert man längs des Strichs von der unteren Kurve $g(x)$ bis zur oberen $h(x)$ (das innere Integral), und
diese Scheibenwerte summiert man über $x$ (das äußere Integral).

So reduziert sich das Doppel- bzw. Dreifachintegral auf **geschachtelte eindimensionale Integrale mit variablen
Grenzen** — also auf lauter gewöhnliche Integrale aus HM1. Das ist die häufigste Rechenmethode überhaupt;
kompliziertere Gebiete setzt man aus mehreren Normalbereichen zusammen.

:::grafik
Szene: hoema3/integralrechnung-rn/05-scanstrich · Vorlage: normalbereich-scan-2d
Ein ebenes Gebiet $D$ zwischen unterer Kurve $g(x)$ und oberer $h(x)$ über $[a,b]$; ein senkrechter „Scanstrich"
wandert von $a$ bis $b$, an jeder Stelle $x$ das innere Integral von $g(x)$ bis $h(x)$. Daneben der 3D-Fall: über
einem Grundgebiet $D$ ein „Dach" $\psi(x,y)$ über einem „Boden" $\phi(x,y)$. (Rot = Gebiet, orange = Scanstrich/Säule,
grau = Randkurven.)
:::

## Normalbereiche in der Ebene

Ein __Normalbereich__ in $\mathbb{R}^2$ ist ein Gebiet, bei dem eine Variable zwischen zwei stetigen Funktionen
der anderen liegt — in zwei Bauformen:

:::formel Definition
$$D = \{(x,y) : \alpha(y)\le x\le\beta(y),\ c\le y\le d\}\ \text{(Typ 1)}, \qquad D = \{(x,y) : g(x)\le y\le h(x),\ a\le x\le b\}\ \text{(Typ 2)}.$$
:::

Bei **Typ 1** laufen für jedes feste $y$ die $x$-Werte von der linken Randkurve $\alpha(y)$ bis zur rechten
$\beta(y)$ (waagerechte Schnitte). Bei **Typ 2** für jedes feste $x$ die $y$-Werte von der unteren Kurve $g(x)$
bis zur oberen $h(x)$ (senkrechte Schnitte).

Es ist dieselbe Idee mit vertauschten Rollen von $x$ und $y$. Der Bereich heißt __regulär__, wenn die
Randfunktionen stetig differenzierbar sind.

## Das Integral über einen Normalbereich

Für einen Normalbereich $D$ und stetiges $f:D\to\mathbb{R}$ wird das Integral zum **iterierten Integral mit
variablen inneren Grenzen** (hier Typ 2):

:::formel Satz
$$\int_D f(x,y)\,dx\,dy = \int_a^b\!\left(\int_{g(x)}^{h(x)} f(x,y)\,dy\right)dx.$$
:::

**Entscheidend:** Die **inneren** Grenzen dürfen von der äußeren Variablen abhängen ($g(x),h(x)$), die **äußeren**
Grenzen ($a,b$) sind konstant — am Ende muss ja eine Zahl herauskommen.

Für $f\equiv1$ erhält man den **Flächeninhalt** als Integral der Schnittlängen $\ell(x)=h(x)-g(x)$:

$$|D| = \int_a^b \big(h(x)-g(x)\big)\,dx.$$

Das ist das Cavalieri-Prinzip in der Ebene. Es gilt wieder die Abschätzung $\big|\int_D f\big|\le|D|\,\sup_D|f|$.

**Eigenes Beispiel.** Das Gebiet zwischen $y=x^2$ (unten) und $y=x$ (oben) über $x\in[0,1]$ ist ein
Typ-2-Normalbereich. Sein Flächeninhalt ist

$$|D| = \int_0^1 (x-x^2)\,dx = \Big[\tfrac{x^2}{2}-\tfrac{x^3}{3}\Big]_0^1 = \tfrac12-\tfrac13 = \tfrac16.$$

:::herleitung
Ein Funktionsintegral über dasselbe Gebiet, Schritt für Schritt:

$$\int_D (x+y)\,dx\,dy = \int_0^1\!\int_{x^2}^{x}(x+y)\,dy\,dx.$$

Das innere Integral (nach $y$, $x$ fest):

$$\int_{x^2}^{x}(x+y)\,dy = \Big[xy+\tfrac{y^2}{2}\Big]_{y=x^2}^{x} = \Big(x^2+\tfrac{x^2}{2}\Big) - \Big(x^3+\tfrac{x^4}{2}\Big) = \tfrac{3}{2}x^2 - x^3 - \tfrac12 x^4.$$

Dann das äußere:

$$\int_0^1\!\Big(\tfrac{3}{2}x^2-x^3-\tfrac12 x^4\Big)dx = \tfrac12 - \tfrac14 - \tfrac{1}{10} = \tfrac{3}{20}.$$
:::

:::grafik
Szene: hoema3/integralrechnung-rn/05-typ2-beispiel · Vorlage: flaeche-zwischen-kurven-2d
Der Typ-2-Normalbereich zwischen $y=x^2$ und $y=x$ über $[0,1]$; ein senkrechter Schnitt bei $x$ von $x^2$ bis $x$
hervorgehoben (das innere Integral). Formel $\int_D f=\int_0^1\int_{x^2}^{x} f\,dy\,dx$ mit markierten variablen
inneren und konstanten äußeren Grenzen. (Rot = Gebiet, orange = Schnitt, grau = Kurven.)
:::

## Allgemeine Gebiete: Zerlegung in Normalbereiche

Nicht jedes Gebiet ist ein einzelner Normalbereich. Gängige Bereiche lassen sich aber als **Vereinigung endlich
vieler** regulärer Normalbereiche $D_1,\ldots,D_N$ schreiben, die sich höchstens längs ihrer Randkurven
überlappen. Dann integriert man **stückweise** und addiert:

$$\int_D f\,dx = \sum_{j=1}^{N}\int_{D_j} f\,dx.$$

Das Ergebnis ist **unabhängig** von der gewählten Zerlegung — die Überlappungen sind Randkurven, also Nullmengen.

**Stolperstein:** Die abgeschlossene Kreisscheibe $D=\{x^2+y^2\le1\}$ ist zwar ein Normalbereich
($-\sqrt{1-y^2}\le x\le\sqrt{1-y^2}$), doch die Randfunktionen verlieren bei $y=\pm1$ ihre Differenzierbarkeit
(senkrechte Tangente). Man zerlegt dann geeignet — oder wechselt gleich zu Polarkoordinaten (Kapitel 4).

## Räumliche Normalbereiche

Dasselbe Prinzip trägt in drei Dimensionen. Ein __räumlicher Normalbereich__ liegt vor, wenn die Höhe $z$ über
einem ebenen Grundgebiet $D$ zwischen einem „Boden" $\phi(x,y)$ und einem „Dach" $\psi(x,y)$ eingeschlossen ist:

$$\int_M f\,dV = \int_D\!\left(\int_{\phi(x,y)}^{\psi(x,y)} f(x,y,z)\,dz\right)dx\,dy, \qquad M=\{\phi\le z\le\psi,\ (x,y)\in D\}.$$

Man integriert erst **senkrecht** in $z$ (von Boden zu Dach), was ein Integral über das ebene Grundgebiet $D$
liefert — und $D$ ist selbst wieder ein (ebener) Normalbereich. So schält man ein Dreifachintegral Schicht um
Schicht zu drei gewöhnlichen Integralen ab.

**Eigenes Beispiel (Tetraeder).** Über dem Grunddreieck $D=\{x,y\ge0,\ x+y\le1\}$ liege der Körper unter der
Ebene $z=1-x-y$.

:::herleitung
$$\mathrm{vol} = \int_0^1\!\int_0^{1-x}\!\int_0^{1-x-y} 1\,dz\,dy\,dx.$$

Innerstes Integral (nach $z$): $\int_0^{1-x-y}1\,dz = 1-x-y$. Mittleres (nach $y$):

$$\int_0^{1-x}(1-x-y)\,dy = \Big[(1-x)y-\tfrac{y^2}{2}\Big]_0^{1-x} = \tfrac{(1-x)^2}{2}.$$

Äußeres (nach $x$): $\int_0^1 \tfrac{(1-x)^2}{2}\,dx = \tfrac16$ — das bekannte Volumen des Einheits-Tetraeders.
:::

:::grafik
Szene: hoema3/integralrechnung-rn/05-tetraeder · Vorlage: tetraeder-schichtung-3d
Das Tetraeder über dem Grunddreieck $D=\{x,y\ge0,x+y\le1\}$ mit Dach $z=1-x-y$; die drei geschachtelten
Integrationsrichtungen ($z$, dann $y$, dann $x$) als Pfeile, Ergebnis $\mathrm{vol}=1/6$. (Rot = Körper, orange =
Säule in $z$, grau = Grunddreieck.)
:::

## Bedeutung und Ausblick

Mit Normalbereichen rechnet man die allermeisten Flächen- und Volumenintegrale der Praxis aus — ohne neue Theorie,
nur mit geschachtelten HM1-Integralen und sauber gewählten Grenzen.

Normalbereiche funktionieren gut für „kastenartige" Geometrien, werden bei Kreisen und Kugeln aber unhandlich. Der
elegante Ausweg sind **Koordinatentransformationen** (Polar-, Zylinder-, Kugelkoordinaten, Kapitel 4). Zuvor
wenden wir uns den __Kurvenintegralen__ zu — dem Integrieren **entlang von Wegen**, dem Herzstück der
Vektoranalysis.

:::kern
- Ein __Normalbereich__ in $\mathbb{R}^2$ schließt eine Koordinate zwischen zwei stetigen Funktionen der anderen ein: Typ 1 $\{\alpha(y)\le x\le\beta(y),\,c\le y\le d\}$, Typ 2 $\{g(x)\le y\le h(x),\,a\le x\le b\}$; __regulär__ bei stetig differenzierbaren Rändern.
- Integral als **iteriertes Integral mit variablen inneren, konstanten äußeren Grenzen**: $\int_D f=\int_a^b\int_{g(x)}^{h(x)} f\,dy\,dx$; Fläche $|D|=\int_a^b(h-g)\,dx$ (Cavalieri in der Ebene).
- Allgemeine Gebiete = Vereinigung endlich vieler Normalbereiche, $\int_D f=\sum_j\int_{D_j}f$ (zerlegungsunabhängig).
- __Räumlicher Normalbereich__: $\int_M f=\int_D\int_{\phi}^{\psi} f\,dz\,dx\,dy$ (erst senkrecht in $z$, dann über $D$).
- Beispiele: Fläche zwischen $y=x^2$ und $y=x$ ist $\tfrac16$; Einheits-Tetraeder hat Volumen $\tfrac16$.
- **Stolperstein:** richtigen Typ wählen (einfache Grenzen/Stammfunktion), ggf. zerlegen; Kreisscheibe → besser Polarkoordinaten.
:::

:::quiz
F: Was ist ein Normalbereich, und worin unterscheiden sich Typ 1 und Typ 2?
A: Ein Gebiet, bei dem eine Koordinate zwischen zwei stetigen Funktionen der anderen eingeschlossen ist. Typ 1: $\alpha(y)\le x\le\beta(y)$ bei festem $y$ (waagerechte Schnitte); Typ 2: $g(x)\le y\le h(x)$ bei festem $x$ (senkrechte Schnitte). Dieselbe Idee mit vertauschten Rollen von $x$ und $y$.
F: Warum dürfen die **inneren** Integrationsgrenzen von der äußeren Variablen abhängen, die **äußeren** aber nicht?
A: Das innere Integral wird bei festem äußeren Wert gebildet — dort beschreiben die Randkurven $g(x),h(x)$ den erlaubten Bereich, dürfen also von $x$ abhängen. Nach dem äußeren Integral muss eine **Zahl** herauskommen, daher müssen dessen Grenzen konstant sein.
F: Warum reduziert ein Normalbereich das Doppelintegral auf gewöhnliche 1D-Integrale?
A: Man integriert zuerst entlang eines Schnitts (eine Variable bei festem anderem) — ein gewöhnliches HM1-Integral mit variablen Grenzen — und summiert die Schnittwerte über die zweite Variable, wieder ein 1D-Integral. So wird aus dem Flächenintegral eine Schachtelung eindimensionaler Integrale.
F: Wie hängt die Flächenformel $|D|=\int_a^b(h-g)\,dx$ mit dem Cavalieri-Prinzip zusammen?
A: $h(x)-g(x)$ ist die **Länge** des senkrechten Schnitts bei $x$. Die Fläche ist das Integral dieser Schnittlängen — genau das Cavalieri-Prinzip in der Ebene (Fläche = Integral der „Querschnitte").
F: Warum ist die Wahl des richtigen Normalbereich-Typs praktisch wichtig?
A: Je nach Typ sind die Randkurven und die innere Stammfunktion unterschiedlich einfach; eine Reihenfolge kann elementar sein, die andere unhandlich. Manche Gebiete lassen sich zudem nur in einem Typ **ohne** Zerlegung beschreiben.
F: Wie integriert man über ein Gebiet, das kein einzelner Normalbereich ist?
A: Man zerlegt es in endlich viele reguläre Normalbereiche $D_1,\dots,D_N$, die sich nur längs ihrer Ränder überlappen, integriert über jeden einzeln und addiert: $\int_D f=\sum_j\int_{D_j}f$.
F: Warum ist die abgeschlossene Kreisscheibe ein problematischer Normalbereich, obwohl sie formal einer ist?
A: Mit $-\sqrt{1-y^2}\le x\le\sqrt{1-y^2}$ ist sie ein Normalbereich, aber die Randfunktionen haben bei $y=\pm1$ eine **senkrechte Tangente** und sind dort nicht differenzierbar (nicht regulär). Man zerlegt deshalb geeignet — oder wechselt gleich zu Polarkoordinaten.
F: In welcher Reihenfolge „schält" man ein Dreifachintegral über einen räumlichen Normalbereich ab?
A: Zuerst **senkrecht in $z$** von Boden $\phi(x,y)$ bis Dach $\psi(x,y)$; das ergibt ein Integral über das ebene Grundgebiet $D$. Da $D$ selbst ein Normalbereich ist, folgen zwei weitere 1D-Integrale — insgesamt drei gewöhnliche Integrale.
F: Warum liefert $\int_M 1\,dV$ über einen räumlichen Normalbereich gerade das Volumen zwischen Boden und Dach?
A: Das innerste Integral $\int_{\phi}^{\psi}1\,dz=\psi-\phi$ ist die **Höhe** der Säule über $(x,y)$. Integriert man diese Höhe über das Grundgebiet $D$, summiert man lauter Säulenvolumina — das Gesamtvolumen.
F: Warum ist das Ergebnis unabhängig davon, wie man das Gebiet in Normalbereiche zerlegt?
A: Das Integral über die Menge ist bereits eindeutig definiert (Fortsetzung durch null); die Zerlegung ist nur ein Rechenweg. Die Überlappungen der Teilbereiche sind Randkurven — Nullmengen, die nichts beitragen —, daher kommt jede zulässige Zerlegung auf denselben Wert.
:::
