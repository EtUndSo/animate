---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralsätze im Raum
order: 3151200
summary: Was im Inneren geschieht, lässt sich am Rand ablesen
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Eine Fläche integriert man, indem man sie aus einem ebenen Bereich $B$ hervorgehen lässt: Das kleine Rechteck $\mathrm{d} u\,\mathrm{d} v$ wird zum Parallelogramm mit der Fläche $|\boldsymbol{x}_u\times\boldsymbol{x}_v|\,\mathrm{d} u\,\mathrm{d} v$.

</li>

<li>

Stokes: Die Wirbelstärke $\operatorname{rot}\boldsymbol{F}$, summiert über eine Fläche, ist die Zirkulation am Rand. Gauß: Die Quellstärke $\operatorname{div}\boldsymbol{F}$, summiert über einen Körper, ist der Fluss durch die Oberfläche.

</li>

<li>

Beide Sätze gelten aus demselben Grund: Man zerlegt in kleine Zellen, auf gemeinsamen Innenwänden heben sich die Beiträge auf, und nur der äußere Rand bleibt übrig.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Oberflächenelement: $\mathrm{d}\sigma=|\boldsymbol{x}_u\times\boldsymbol{x}_v|\,\mathrm{d} u\,\mathrm{d} v=\sqrt{EG-F^2}\,\mathrm{d} u\,\mathrm{d} v$. Graph: $\sqrt{1+|\nabla H|^2}\,\mathrm{d} x\,\mathrm{d} y$. Kugel: $R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$. Rotationsfläche: $2\pi|x|\sqrt{\dot x^2+\dot z^2}\,\mathrm{d} t$.

</li>

<li>

Fluss: $\int_{\mathcal F}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=\int_B\boldsymbol{F}\cdot(\boldsymbol{x}_u\times\boldsymbol{x}_v)\,\mathrm{d} u\,\mathrm{d} v$, Richtung immer prüfen.

</li>

<li>

Parameterinvarianz: Der Wert hängt nicht von der Parametrisierung ab. Kehrt sich die Richtung um, wechseln Arbeit und Fluss das Vorzeichen, Länge und $\int f\,\mathrm{d}\sigma$ nicht.

</li>

<li>

Stokes: $\int_{\mathcal F}\operatorname{rot}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}=\int_{\partial\mathcal F}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$, Rechtsschraube. Nur der Rand zählt, die Fläche darf man ersetzen.

</li>

<li>

Gauß: $\int_V\operatorname{div}\boldsymbol{F}\,\mathrm{d}\boldsymbol{x}=\int_{\partial V}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}$, Normale nach außen. Offene Flächen mit einem Deckel schließen.

</li>

<li>

Rand-Regel: $\int_V\boldsymbol{E}\cdot\nabla\varphi=\int_{\partial V}\varphi\,\boldsymbol{E}\cdot\mathrm{d}\boldsymbol{S}-\int_V\varphi\,\operatorname{div}\boldsymbol{E}$.

</li>

<li>

Gradient: nötig $\operatorname{rot}\boldsymbol{F}=0$, störendes Loch ist eine Achse. Rotation: nötig $\operatorname{div}\boldsymbol{F}=0$, störendes Loch ist ein Punkt.

</li>

<li>

Poisson: $-\Delta u=f$ hat die Lösung $u=\phi*f$ mit $\phi=1/(4\pi r)$.

</li>

<li>

Helmholtz: $\boldsymbol{F}=\nabla u+\nabla\times\boldsymbol{A}$.

</li>

</ul>
:::

**Welches Werkzeug wann.**

| Aufgabe enthält | Vorgehen |
|---|---|
| $\int_{\mathcal F}f\,\mathrm{d}\sigma$, $f$ skalar | parametrisieren, $\mathrm{d}\sigma$ einsetzen, Symmetrie nutzen |
| $\int_{\mathcal F}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}$, Fläche geschlossen | Gauß, wenn $\operatorname{div}\boldsymbol{F}$ einfach ist |
| $\int_{\mathcal F}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}$, Fläche offen, $\operatorname{div}\boldsymbol{F}=0$ | mit Deckel schließen, Fluss durch den Deckel rechnen |
| $\int_{\mathcal F}\operatorname{rot}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{S}$ | Stokes: Rand rechnen oder einfachere Fläche wählen |
| $\oint\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$ im Raum | Stokes, wenn $\operatorname{rot}\boldsymbol{F}$ einfach ist |
| $\Delta$ unter dem Integral | Greensche Formeln |

**Wie es weitergeht.** Die Sätze hier gelten für feste Felder. Der nächste Teil fragt, was passiert, wenn sich Funktionen Schritt für Schritt einer anderen Funktion nähern.

**Ein Prinzip hinter allen Ergebnissen.** Alle Sätze dieses Kapitels sind derselbe Satz in verschiedener Dimension: Das Integral einer Ableitung über ein Gebiet ist das Integral der Funktion über den Rand.

| Ergebnis | Gebiet und Rand | Woher es kommt |
|---|---|---|
| Hauptsatz | Intervall, zwei Punkte | Ableitung von $f$ |
| Kurvenintegral | Kurve, zwei Punkte | $\nabla\varphi$ integriert sich zu $\varphi(\text{Ende})-\varphi(\text{Anfang})$ (Teil 3) |
| Green in der Ebene | ebener Bereich, Randkurve | $\partial_xQ-\partial_yP$ (Teil 3) |
| Stokes im Raum | Fläche, Randkurve | Green im Parameterbereich (Stufe [6](der-satz-von-stokes.html#stufe-6)) |
| Gauß | Körper, Oberfläche | Hauptsatz in jeder Achsenrichtung (Stufe [8](der-satz-von-gau.html#stufe-8)) |
| Poisson-Lösung | $\mathbb{R}^3$ ohne kleine Kugel | Gauß mit Rand um den Aufpunkt (Stufe [9](poisson-gleichung.html#stufe-9)) |
| Helmholtz | ganz $\mathbb{R}^3$ | Poisson plus Vektorpotential (Stufe [10](der-hauptsatz-der-vektoranalysis.html#stufe-10)) |
