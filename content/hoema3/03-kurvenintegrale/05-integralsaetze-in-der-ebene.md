---
title: Die Integralsätze in der Ebene (Green und Gauß)
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3030500
summary: Von Grund auf – wie ein Randintegral (längs der geschlossenen Randkurve) mit einem Flächenintegral über das eingeschlossene Gebiet zusammenhängt. Der Satz von Stokes/Green verbindet die Zirkulation am Rand mit dem Rotationsintegral, der Satz von Gauß den Ausfluss durch den Rand mit dem Divergenzintegral. Daraus folgen die koordinatenfreie Deutung von div und rot sowie eine elegante Flächenformel.
tags: Satz von Green, Satz von Stokes, Satz von Gauß, Divergenz, Rotation, Randorientierung, Flächenformel, Planimeter
---

:::grafik
Einstiegs-Animation: Ein ebenes Gebiet $D$ mit seiner geschlossenen Randkurve $\partial D$ (positiv orientiert —
beim Durchlaufen liegt das Innere **links**). Zwei gekoppelte Bilder: (1) __Green/Stokes__: Entlang des Randes
wird die **Zirkulation** $\oint_{\partial D}F\cdot dx$ aufsummiert; im Inneren drehen sich lauter kleine
Wirbelrädchen $\operatorname{rot}F$, deren Summe $\iint_D\operatorname{rot}F\,dA$ genau denselben Wert ergibt —
die inneren Wirbel heben sich paarweise auf, nur der Rand bleibt. (2) __Gauß__: Der **Ausfluss**
$\oint_{\partial D}F\cdot\nu\,ds$ durch den Rand gleicht der Summe aller Quellen $\iint_D\operatorname{div}F\,dA$.
Kernbotschaft: Was im Inneren eines Gebiets passiert (Wirbel, Quellen), zeigt sich vollständig an seinem Rand.
:::

:::konzept
Jetzt der Höhepunkt der ebenen Vektoranalysis: die Brücke zwischen einem **Randintegral** (über die geschlossene
Kurve) und einem **Flächenintegral** (über das eingeschlossene Gebiet). Zwei berühmte Sätze, zwei Seiten
derselben Medaille: Der __Satz von Stokes/Green__ setzt die **Zirkulation** eines Feldes längs des Randes gleich
dem Integral seiner **Rotation** über die Fläche; der __Satz von Gauß__ setzt den **Ausfluss** durch den Rand
gleich dem Integral der **Divergenz**. Diese Sätze sind das Fundament der Feldtheorie (Maxwell-Gleichungen in
Integralform) und geben nebenbei der Divergenz und Rotation ihre endgültige, koordinatenfreie Bedeutung.
:::

**Worum es geht:** Wir definieren den __regulären Bereich__ und die __Randorientierung__, formulieren und beweisen
den __Satz von Green/Stokes__, leiten den __Satz von Gauß__ ab, deuten div und rot **koordinatenfrei** und gewinnen
eine __Flächenformel__.

## Regulärer Bereich und Randorientierung

Ein __regulärer Bereich__ $D\subset\mathbb{R}^2$ ist eine beschränkte, abgeschlossene Menge mit
zusammenhängendem Inneren, deren Rand aus **endlich vielen geschlossenen regulären Kurven** besteht. Entscheidend
für die Integralsätze ist die **Durchlaufrichtung** des Randes: Der Rand $\partial D$ heißt __positiv
orientiert__, wenn beim Durchlaufen das **Innere von $D$ stets links** liegt.

- Bei einer **Kreisscheibe** heißt das: der Rand wird **gegen den Uhrzeigersinn** durchlaufen.
- Bei einem **Ringgebiet** läuft der **äußere** Kreis gegen, der **innere** Kreis im Uhrzeigersinn (damit das
  Material des Rings jeweils links liegt).

:::grafik
Links eine Kreisscheibe mit ccw-Randpfeil (Inneres links). Rechts ein Ringgebiet: äußerer Rand ccw, innerer Rand
cw, jeweils mit dem Hinweis „Inneres liegt links". 
:::

## Der Satz von Stokes/Green in der Ebene

Für einen regulären Bereich $D$ mit positiv orientiertem Rand und ein in einer Umgebung stetig differenzierbares
Feld $F$ gilt der __Stokessche Integralsatz in der Ebene__:

$$\int_D \operatorname{rot}F(x)\,dx = \oint_{\partial D} F\cdot dx.$$

In Komponenten $F=(P,Q)$ ist das die vertraute __Greensche Formel__ (mit $\operatorname{rot}F=\partial_x Q -
\partial_y P$):

$$\oint_{\partial D} \big(P\,dx + Q\,dy\big) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dx\,dy.$$

In Worten: Die **Zirkulation** des Feldes längs des Randes gleich dem **Rotationsfluss** durch die Fläche.

**Beweisidee.** Es genügt, einen Normalbereich $D=\{\alpha(y)\le x\le\beta(y),\ c\le y\le d\}$ zu betrachten
(allgemeine Gebiete zerlegt man). Für den $Q$-Term liefert der Hauptsatz der Differential- und Integralrechnung
$\iint_D \partial_x Q\,dx\,dy = \int_c^d\big(Q(\beta(y),y)-Q(\alpha(y),y)\big)dy$, und für den $P$-Term die
Leibnizregel. Setzt man die vier Randstücke zur geschlossenen Randkurve zusammen, addieren sich die Terme gerade
zu $\oint_{\partial D}F\cdot dx$. $\square$

Als Nebenprodukt erhält man einen zweiten Beweis des **2. Hauptsatzes**: Ist $\operatorname{rot}F=0$ und $D$ von
der geschlossenen Kurve berandet, so ist $\oint_{\partial D}F\cdot dx=\iint_D 0\,dA=0$.

## Der Satz von Gauß in der Ebene

Dreht man das Feld um $90^\circ$, wird aus Green der __Gaußsche Integralsatz__. Dazu braucht man das __äußere
Einheitsnormalenfeld__ $\nu$ längs $\partial D$ — es steht senkrecht auf dem Tangentialvektor $\tau$ und zeigt
**nach außen**, formal $\tau = \nu^{\perp}$ mit $\nu^{\perp}=(-\nu_2,\nu_1)^T$. Dann gilt:

$$\int_D \operatorname{div}F(x)\,dx = \oint_{\partial D} F\cdot\nu\,ds.$$

In Worten: Der gesamte **Ausfluss** des Feldes durch den Rand (Fluss in Normalenrichtung) gleich dem Integral der
**Quelldichte** $\operatorname{div}F$ über das Gebiet. Green und Gauß sind in der Ebene **äquivalent**: Ersetzt man
in Green $F$ durch das um $90^\circ$ gedrehte Feld, geht die Tangentialkomponente in die Normalkomponente über —
und $\operatorname{rot}$ in $\operatorname{div}$.

:::grafik
Dasselbe Gebiet $D$ zweimal: links Green (Tangentialkomponente $F\cdot\tau$ längs Rand = $\iint\operatorname{rot}F$),
rechts Gauß (Normalkomponente $F\cdot\nu$ längs Rand = $\iint\operatorname{div}F$); dazwischen der Dreh-Pfeil
„$\tau=\nu^\perp$, Feld um 90° drehen".
:::

## Koordinatenfreie Deutung von Divergenz und Rotation

Jetzt zahlt sich die Mühe anschaulich aus. Zieht man ein winziges Kreisscheibchen $B_R(x)$ auf einen Punkt
zusammen, liefern die Integralsätze **koordinatenfreie** Definitionen — genau die „Dichten", die wir in Kapitel 1
nur behauptet hatten:

$$\operatorname{div}F(x) = \lim_{R\to 0}\frac{1}{|B_R(x)|}\oint_{\partial B_R(x)} F\cdot\nu\,ds \quad(\text{Quelldichte}),$$

$$\operatorname{rot}F(x) = \lim_{R\to 0}\frac{1}{|B_R(x)|}\oint_{\partial B_R(x)} F\cdot\tau\,ds \quad(\text{Wirbeldichte}).$$

Die **Divergenz** ist also der Ausfluss pro Fläche (wie stark ein Punkt „quillt"), die **Rotation** die
Zirkulation pro Fläche (wie stark ein Punkt „wirbelt") — unabhängig von jedem Koordinatensystem. Das ist die
präzise Rechtfertigung der Bilder „Quelle/Senke" und „Wirbel" aus dem Differential-Kapitel.

## Eine Flächenformel aus Green

Setzt man in die Greensche Formel das Feld $P=-y/2$, $Q=x/2$ ein (dann ist $\partial_x Q-\partial_y P=1$), so wird
das Flächenintegral zu $\iint_D 1\,dA=|D|$, und man erhält den Flächeninhalt als **reines Randintegral**:

$$|D| = \frac{1}{2}\oint_{\partial D}\big(x\,dy - y\,dx\big) = \frac{1}{2}\int_a^b \det\big(\gamma(t)\,\big|\,\dot\gamma(t)\big)\,dt.$$

Das ist das Prinzip des **Planimeters** — ein Gerät, das Flächen misst, indem es nur die Randkurve abfährt.

**Eigene Beispiele.** Für den Kreis $\gamma(t)=(R\cos t, R\sin t)$, $t\in[0,2\pi]$, ist
$\tfrac12\int_0^{2\pi}\big(R\cos t\cdot R\cos t - R\sin t\cdot(-R\sin t)\big)dt = \tfrac12\int_0^{2\pi}R^2\,dt =
\pi R^2$. Für die **Ellipse** $\gamma(t)=(a\cos t, b\sin t)$ ergibt dieselbe Formel $|E| = \tfrac12\int_0^{2\pi}
ab\,dt = \pi a b$ — der Flächeninhalt fällt mühelos, während der **Umfang** der Ellipse auf viel schwierigere
(elliptische) Integrale führt.

:::grafik
Eine Ellipse mit Randparametrisierung $\gamma(t)=(a\cos t,b\sin t)$; das Dreieck „Ursprung–$\gamma$–$\gamma+d\gamma$"
der Fläche $\tfrac12\det(\gamma|\dot\gamma)\,dt$, über den Umlauf aufsummiert zu $|E|=\pi ab$. Beschriftung
„Fläche nur aus der Randkurve (Planimeter)".
:::

:::kern
Ein __regulärer Bereich__ $D\subset\mathbb{R}^2$ hat einen Rand aus endlich vielen geschlossenen Kurven; __positiv
orientiert__ = Inneres liegt links (Scheibe ccw, Ring außen ccw/innen cw). __Satz von Stokes/Green__:
$\int_D\operatorname{rot}F\,dA=\oint_{\partial D}F\cdot dx$, in Komponenten $\oint(P\,dx+Q\,dy)=\iint(\partial_x Q-
\partial_y P)\,dA$ (Zirkulation = Rotationsfluss; Beweis via Normalbereich + Hauptsatz + Leibniz). __Satz von
Gauß__: $\int_D\operatorname{div}F\,dA=\oint_{\partial D}F\cdot\nu\,ds$ (Ausfluss = Quellintegral; äußere Normale
$\nu$, $\tau=\nu^\perp$) — äquivalent zu Green (Feld um 90° drehen). __Koordinatenfrei__:
$\operatorname{div}F=\lim_{R\to0}\tfrac1{|B_R|}\oint_{\partial B_R}F\cdot\nu\,ds$ (Quelldichte),
$\operatorname{rot}F=\lim\tfrac1{|B_R|}\oint F\cdot\tau\,ds$ (Wirbeldichte). __Flächenformel__ $|D|=\tfrac12\oint(x\,dy
-y\,dx)$ (Planimeter); Kreis $\pi R^2$, Ellipse $\pi ab$.
:::

Die Integralsätze in der Ebene verbinden Rand und Fläche. In drei Dimensionen gibt es die mächtigeren Gegenstücke
— den Satz von Stokes über Flächen im Raum und den Satz von Gauß für Volumina. Bevor wir sie angehen, brauchen wir
aber ein Werkzeug, um Integrale über krumme Gebiete (Kreise, Kugeln) überhaupt bequem zu berechnen: die
__Koordinatentransformationen__, das nächste Kapitel.

:::quiz
F: Was ist die gemeinsame Grundidee der ebenen Integralsätze?
A: Sie verbinden ein **Randintegral** (über die geschlossene Randkurve) mit einem **Flächenintegral** (über das eingeschlossene Gebiet). Alles, was im Inneren passiert — Wirbel bzw. Quellen —, zeigt sich vollständig am Rand.
F: Was bedeutet „positiv orientierter Rand", und wie sieht das bei einem Ringgebiet aus?
A: Positiv orientiert heißt: beim Durchlaufen liegt das Innere stets **links**. Bei der Scheibe ist das gegen den Uhrzeigersinn; beim Ring läuft der äußere Rand gegen, der innere Rand im Uhrzeigersinn — so liegt das Ringmaterial jeweils links.
F: Was besagt der Satz von Green/Stokes anschaulich?
A: Die **Zirkulation** eines Feldes längs des Randes ist gleich dem Integral seiner **Rotation** über die Fläche: $\oint_{\partial D}F\cdot dx=\iint_D\operatorname{rot}F\,dA$. Die vielen kleinen inneren Wirbel summieren sich genau zur Randzirkulation.
F: Warum heben sich die „inneren Wirbel" paarweise auf, sodass nur der Rand übrig bleibt?
A: Zerlegt man das Gebiet in kleine Zellen, wird jede innere Kante von den beiden angrenzenden Zellen **gegenläufig** durchlaufen — ihre Beiträge löschen sich. Nur die Kanten am äußeren Rand haben keinen Partner und bleiben als $\oint_{\partial D}$ stehen.
F: Welche Rolle spielen Hauptsatz und Leibnizregel im Beweis am Normalbereich?
A: Für den $Q$-Term liefert der Hauptsatz der Differential- und Integralrechnung die Differenz der Randwerte in $x$-Richtung, für den $P$-Term die Leibnizregel (variable Grenzen) in $y$-Richtung. Setzt man die vier Randstücke zusammen, ergeben sie genau $\oint_{\partial D}F\cdot dx$.
F: Wie folgt der zweite Hauptsatz ($\operatorname{rot}F=0\Rightarrow\oint=0$) aus Green?
A: Ist $\operatorname{rot}F=0$ und berandet die geschlossene Kurve das Gebiet $D$, so ist $\oint_{\partial D}F\cdot dx=\iint_D\operatorname{rot}F\,dA=\iint_D 0\,dA=0$. Green liefert also einen zweiten, direkten Beweis der Wegunabhängigkeit.
F: Warum sind Green und Gauß in der Ebene äquivalent?
A: Dreht man das Feld um $90°$, geht die Tangentialkomponente $F\cdot\tau$ in die Normalkomponente $F\cdot\nu$ über (wegen $\tau=\nu^\perp$) und $\operatorname{rot}$ in $\operatorname{div}$. Damit wird aus der Green-Aussage (Zirkulation = Rotationsfluss) genau die Gauß-Aussage (Ausfluss = Quellintegral).
F: Was besagt der Satz von Gauß in der Ebene, und was ist $\nu$?
A: $\iint_D\operatorname{div}F\,dA=\oint_{\partial D}F\cdot\nu\,ds$: Der gesamte **Ausfluss** durch den Rand (Fluss in Richtung der äußeren Einheitsnormale $\nu$) gleicht dem Integral der Quelldichte $\operatorname{div}F$ über das Gebiet.
F: Wie liefern die Integralsätze eine koordinatenfreie Deutung von Divergenz und Rotation?
A: Zieht man ein kleines Kreisscheibchen auf einen Punkt zusammen, ist $\operatorname{div}F=\lim\frac{1}{|B_R|}\oint F\cdot\nu\,ds$ (Ausfluss pro Fläche) und $\operatorname{rot}F=\lim\frac{1}{|B_R|}\oint F\cdot\tau\,ds$ (Zirkulation pro Fläche). Das rechtfertigt die Bilder „Quelldichte" und „Wirbeldichte" ohne jedes Koordinatensystem.
F: Wie gewinnt man aus Green eine Flächenformel, und warum fällt bei der Ellipse die Fläche $\pi ab$ mühelos, der Umfang aber nicht?
A: Mit $P=-y/2,\,Q=x/2$ ist $\partial_x Q-\partial_y P=1$, also $|D|=\frac12\oint_{\partial D}(x\,dy-y\,dx)$ — die Fläche als reines Randintegral (Planimeter). Für die Ellipse gibt das $\frac12\int_0^{2\pi}ab\,dt=\pi ab$; der Umfang hingegen ist $\int|\dot\gamma|\,dt$ und führt auf nicht-elementare elliptische Integrale.
:::
