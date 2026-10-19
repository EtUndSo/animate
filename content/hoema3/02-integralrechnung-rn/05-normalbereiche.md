---
title: Integration über Normalbereiche
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3020500
summary: Von Grund auf – wie man ein Doppel- oder Dreifachintegral über ein krummes Gebiet praktisch ausrechnet. Ein Normalbereich ist ein Gebiet, bei dem eine Koordinate zwischen zwei Funktionen der anderen eingeschlossen ist; dann wird das Flächen-/Volumenintegral zu geschachtelten 1D-Integralen mit variablen Grenzen. Kompliziertere Gebiete zerlegt man in mehrere solche Bereiche.
tags: Normalbereich, iteriertes Integral, variable Grenzen, Doppelintegral, Dreifachintegral, Fläche, Zerlegung, räumlicher Normalbereich
---

:::grafik
Einstiegs-Animation: Ein ebenes Gebiet $D$, das nach unten und oben von zwei Kurven $y=g(x)$ und $y=h(x)$
begrenzt wird. Ein senkrechter „Scanstrich" wandert von $x=a$ bis $x=b$; an jeder Stelle $x$ integriert man
längs des Strichs von $g(x)$ bis $h(x)$ (innen), und diese Scheibenwerte summiert man über $x$ (außen). Daneben
der 3D-Fall: über einem Grundgebiet $D$ spannt sich ein „Dach" $z=\psi(x,y)$ über einem „Boden" $z=\phi(x,y)$;
man integriert erst senkrecht in $z$, dann über $D$. Kernbotschaft: Ein Normalbereich macht aus dem Integral über
ein krummes Gebiet geschachtelte 1D-Integrale mit **variablen Grenzen**.
:::

:::konzept
Im vorigen Artikel haben wir Integrale über beliebige Mengen *definiert* (Fortsetzung durch null) — aber noch
nicht praktisch *ausgerechnet*. Das leisten die __Normalbereiche__: Gebiete, bei denen eine Koordinate sauber
**zwischen zwei Funktionen** der anderen eingeschlossen ist. Für sie reduziert sich das Doppel- bzw.
Dreifachintegral auf **geschachtelte eindimensionale Integrale mit variablen Grenzen** — also auf lauter
gewöhnliche Integrale aus HM1. Das ist die mit Abstand häufigste Rechenmethode für mehrdimensionale Integrale;
kompliziertere Gebiete setzt man aus mehreren Normalbereichen zusammen.
:::

**Worum es geht:** Wir definieren den __Normalbereich__ in der Ebene, rechnen das Integral darüber per iteriertem
Integral aus (Satz 2.17), zerlegen allgemeine Gebiete und übertragen alles auf __räumliche Normalbereiche__.

## Normalbereiche in der Ebene

Ein __Normalbereich__ in $\mathbb{R}^2$ ist ein Gebiet, bei dem eine Variable zwischen zwei stetigen Funktionen
der anderen liegt — in zwei Bauformen:

$$D = \{(x,y) : \alpha(y)\le x\le \beta(y),\ c\le y\le d\} \quad\text{(Typ 1)},$$
$$D = \{(x,y) : g(x)\le y\le h(x),\ a\le x\le b\} \quad\text{(Typ 2)}.$$

Bei **Typ 1** laufen für jedes feste $y$ die $x$-Werte von der linken Randkurve $\alpha(y)$ bis zur rechten
$\beta(y)$ (waagerechte Schnitte); bei **Typ 2** für jedes feste $x$ die $y$-Werte von der unteren Kurve $g(x)$
bis zur oberen $h(x)$ (senkrechte Schnitte). Der Bereich heißt __regulär__, wenn die Randfunktionen stetig
differenzierbar sind.

## Das Integral über einen Normalbereich

Für einen Normalbereich $D$ und stetiges $f:D\to\mathbb{R}$ ist das Integral wohldefiniert und wird zum
**iterierten Integral mit variablen inneren Grenzen** (Satz 2.17, hier Typ 1):

$$\int_D f(x,y)\,dx\,dy = \int_c^d\!\left(\int_{\alpha(y)}^{\beta(y)} f(x,y)\,dx\right)dy.$$

**Entscheidend:** Die **inneren** Grenzen dürfen von der äußeren Variablen abhängen ($\alpha(y),\beta(y)$), die
**äußeren** Grenzen ($c,d$) sind konstant. Für $f\equiv 1$ erhält man den **Flächeninhalt**

$$|D| = \int_c^d \ell(y)\,dy, \qquad \ell(y) = \beta(y) - \alpha(y),$$

also „Länge des Schnitts mal $dy$, aufintegriert" — das Cavalieri-Prinzip in der Ebene. Es gilt wieder die
Abschätzung $\big|\int_D f\big| \le |D|\,\sup_D|f|$.

:::grafik
Ein Typ-2-Normalbereich zwischen unterer Kurve $g(x)$ und oberer $h(x)$ über $[a,b]$; ein senkrechter Schnitt bei
$x$ von $g(x)$ bis $h(x)$ hervorgehoben (das innere Integral). Daneben die Formel $\int_D f=\int_a^b\int_{g(x)}^{h(x)}
f\,dy\,dx$ mit markierten variablen inneren und konstanten äußeren Grenzen.
:::

**Eigenes Beispiel.** Das Gebiet zwischen den Kurven $y=x^2$ (unten) und $y=x$ (oben) über $x\in[0,1]$ ist ein
Typ-2-Normalbereich $D=\{x^2\le y\le x,\ 0\le x\le 1\}$. Sein Flächeninhalt ist

$$|D| = \int_0^1 (x - x^2)\,dx = \Big[\tfrac{x^2}{2} - \tfrac{x^3}{3}\Big]_0^1 = \tfrac12 - \tfrac13 = \tfrac16.$$

Und etwa $\displaystyle\int_D (x+y)\,dx\,dy = \int_0^1\!\int_{x^2}^{x}(x+y)\,dy\,dx = \int_0^1\!\Big[xy+\tfrac{y^2}{2}\Big]_{y=x^2}^{x}dx
= \int_0^1\!\Big(\tfrac{3}{2}x^2 - x^3 - \tfrac12 x^4\Big)dx = \tfrac12 - \tfrac14 - \tfrac{1}{10} = \tfrac{3}{20}.$

## Allgemeine Gebiete: Zerlegung in Normalbereiche

Nicht jedes Gebiet ist ein einzelner Normalbereich. Gängige Integrationsbereiche lassen sich aber als
**Vereinigung endlich vieler** regulärer Normalbereiche $D_1,\ldots,D_N$ schreiben, die sich höchstens längs
ihrer Randkurven überlappen. Dann integriert man **stückweise** und addiert:

$$\int_D f\,dx = \sum_{j=1}^{N}\int_{D_j} f\,dx,$$

und das Ergebnis ist **unabhängig** von der gewählten Zerlegung. **Stolperstein:** Die abgeschlossene
Kreisscheibe $D=\{x^2+y^2\le 1\}$ ist zwar ein Normalbereich ($-\sqrt{1-y^2}\le x\le \sqrt{1-y^2}$), doch die
Randfunktionen verlieren bei $y=\pm1$ ihre Differenzierbarkeit (senkrechte Tangente). Durch geeignete Zerlegung
behandelt man sie trotzdem als regulär — oder man wechselt gleich zu Polarkoordinaten (Kapitel 4).

## Räumliche Normalbereiche

Dasselbe Prinzip trägt in drei Dimensionen. Ein __räumlicher Normalbereich__ liegt vor, wenn die Höhe $z$ über
einem ebenen Grundgebiet $D$ zwischen einem „Boden" $\phi(x,y)$ und einem „Dach" $\psi(x,y)$ eingeschlossen ist:

$$M = \{(x,y,z) : \phi(x,y)\le z\le \psi(x,y),\ (x,y)\in D\}, \qquad \int_M f\,dV = \int_D\!\left(\int_{\phi(x,y)}^{\psi(x,y)} f(x,y,z)\,dz\right)dx\,dy.$$

Man integriert also erst **senkrecht** in $z$ (von Boden zu Dach), was ein Integral über das ebene Grundgebiet
$D$ liefert — und $D$ ist selbst wieder ein (ebener) Normalbereich. So schält man ein Dreifachintegral Schicht um
Schicht zu drei gewöhnlichen Integralen ab.

**Eigenes Beispiel (Tetraeder).** Über dem Grunddreieck $D=\{x,y\ge0,\ x+y\le1\}$ liege der Körper unter der
Ebene $z=1-x-y$ (und über $z=0$). Sein Volumen ist

$$\mathrm{vol} = \int_0^1\!\int_0^{1-x}\!\int_0^{1-x-y} 1\,dz\,dy\,dx = \int_0^1\!\int_0^{1-x}(1-x-y)\,dy\,dx = \int_0^1 \tfrac{(1-x)^2}{2}\,dx = \frac16.$$

Das ist das bekannte Volumen des Einheits-Tetraeders — Schicht um Schicht per Normalbereich erschlossen.

:::grafik
Oben die Kreisscheibe als Normalbereich mit den bei $y=\pm1$ „kippenden" Randfunktionen (Hinweis Zerlegung /
Polarkoordinaten). Unten das Tetraeder über dem Grunddreieck $D=\{x,y\ge0,x+y\le1\}$ mit Dach $z=1-x-y$; die drei
geschachtelten Integrationsrichtungen ($z$, dann $y$, dann $x$) als Pfeile, Ergebnis $\mathrm{vol}=1/6$.
:::

:::kern
Ein __Normalbereich__ in $\mathbb{R}^2$ schließt eine Koordinate zwischen zwei stetigen Funktionen der anderen
ein: $D=\{\alpha(y)\le x\le\beta(y),\,c\le y\le d\}$ (Typ 1) bzw. $\{g(x)\le y\le h(x),\,a\le x\le b\}$ (Typ 2),
__regulär__ bei stetig differenzierbaren Rändern. Dann (Satz 2.17) $\int_D f = \int_c^d\int_{\alpha(y)}^{\beta(y)}
f\,dx\,dy$ — **iteriert mit variablen inneren, konstanten äußeren Grenzen**; Fläche $|D|=\int_c^d(\beta-\alpha)\,dy$.
Allgemeine Gebiete = Vereinigung endlich vieler Normalbereiche, stückweise $\int_D f=\sum_j\int_{D_j}f$
(zerlegungsunabhängig). __Räumlicher Normalbereich__: $M=\{\phi(x,y)\le z\le\psi(x,y),(x,y)\in D\}$,
$\int_M f=\int_D\int_\phi^\psi f\,dz\,dx\,dy$ (erst senkrecht in $z$, dann über $D$). Beispiele: Fläche zwischen
$y=x^2$ und $y=x$ ist $\tfrac16$; Einheits-Tetraeder hat Volumen $\tfrac16$. **Stolperstein:** richtigen Typ
wählen (einfache Grenzen), ggf. zerlegen; Kreisscheibe → besser Polarkoordinaten.
:::

Normalbereiche funktionieren gut für „kastenartige" Geometrien, werden aber bei Kreisen und Kugeln unhandlich.
Der elegante Ausweg sind **Koordinatentransformationen** (Polar-, Zylinder-, Kugelkoordinaten) — doch bevor wir
die systematisch behandeln (Kapitel 4), wenden wir uns den __Kurvenintegralen__ zu: dem Integrieren **entlang von
Wegen**, dem Herzstück der Vektoranalysis.
