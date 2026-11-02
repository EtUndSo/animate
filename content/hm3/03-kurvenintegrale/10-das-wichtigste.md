---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3131000
summary: Wann zählen nur Start und Ziel, und wann der ganze Weg?
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

Länge: $\mathcal L=\int_a^b|\dot\gamma|\,\mathrm{d} t$, Graph $\int_a^b\sqrt{1+f'^2}\,\mathrm{d} x$. Einfach heißt: $\gamma(s)=\gamma(t)$ mit $s<t$ nur für $s=a$, $t=b$.

</li>

<li>

Kurvenintegral: $\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_a^b\boldsymbol{F}(\gamma)\cdot\dot\gamma\,\mathrm{d} t=\int_\gamma\boldsymbol{F}\cdot\boldsymbol{t}\,\mathrm{d} s$. Abschätzung: $|\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}|\le\sup|\boldsymbol{F}|\,\mathcal L$.

</li>

<li>

Parameterinvarianz: Tempo ändern ändert nichts. Rückwärts wechselt das Arbeitsintegral das Vorzeichen, das Integral über die Bogenlänge nicht.

</li>

<li>

Erster Hauptsatz: $\int_\gamma\nabla\varphi\cdot\mathrm{d}\boldsymbol{x}=\varphi(\boldsymbol{x}_1)-\varphi(\boldsymbol{x}_0)$. Konservativ $\iff$ Gradientenfeld $\iff$ alle Rundwege null.

</li>

<li>

$\operatorname{rot}\boldsymbol{F}=0$ ist notwendig, aber allein nicht hinreichend: $\boldsymbol{H}$ auf $\mathbb{R}^2\setminus\{0\}$ hat $\oint=2\pi$.

</li>

<li>

Poincaré: Auf Sterngebieten folgt aus $\operatorname{rot}\boldsymbol{F}=0$ ein Skalarpotential und aus $\operatorname{div}\boldsymbol{F}=0$ ein Vektorpotential. Mit dem Zentrum 0 ist $\boldsymbol{F}=\nabla\int_0^1\boldsymbol{F}(t\boldsymbol{x})\cdot\boldsymbol{x}\,\mathrm{d} t$ beziehungsweise $\boldsymbol{F}=\operatorname{rot}\int_0^1\boldsymbol{F}(t\boldsymbol{x})\times t\boldsymbol{x}\,\mathrm{d} t$.

</li>

<li>

Rechnen: Potential längs der Achsen, [(6.1)](potentiale-berechnen.html#gl-6-1). Es ist bis auf eine Konstante bestimmt, ein Vektorpotential bis auf ein Gradientenfeld.

</li>

<li>

Zweiter Hauptsatz: Auf einfach zusammenhängenden Gebieten gilt konservativ $\iff$ Integrabilitätsbedingungen.

</li>

<li>

Green: $\int_D(\partial_xQ-\partial_yP)\,\mathrm{d} x\,\mathrm{d} y=\int_{\partial D}P\,\mathrm{d} x+Q\,\mathrm{d} y$, $D$ liegt links. Gauß: $\int_D\operatorname{div}\boldsymbol{F}\,\mathrm{d}\boldsymbol{x}=\int_{\partial D}\boldsymbol{F}\cdot\boldsymbol\nu\,\mathrm{d} s$.

</li>

<li>

Fläche: $|D|=\frac12\int_a^b\det(\gamma|\dot\gamma)\,\mathrm{d} t$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Das Kurvenintegral summiert den Anteil des Felds in Laufrichtung längs des Wegs, hängt nicht vom Tempo ab und wechselt beim Rückwärtslaufen das Vorzeichen.

</li>

<li>

Nur Start und Ziel zählen genau bei Gradientenfeldern, und das folgt aus $\operatorname{rot}\boldsymbol{F}=0$, sobald sich im Gebiet jede geschlossene Kurve auf einen Punkt zusammenziehen lässt.

</li>

<li>

Für allgemeine ebene Felder ist die Zirkulation um einen Rand das Integral von $\operatorname{rot}\boldsymbol{F}$ über die umrandete Fläche, und genauso ist der Fluss durch den Rand das Integral von $\operatorname{div}\boldsymbol{F}$.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alle Sätze dieses Kapitels sind der Hauptsatz $\int f'=f(b)-f(a)$: Steht unter dem Integral eine volle Ableitung, bleiben nur die Randwerte übrig.

| Ergebnis | Woher es kommt |
|---|---|
| Parameterinvarianz | Tempofaktor $\tau'$ wird von $\mathrm{d} t=\tau'\,\mathrm{d} u$ verbraucht (Stufe [3](warum-die-parametrisierung-egal-ist.html#stufe-3)) |
| Erster Hauptsatz | $\boldsymbol{F}\cdot\dot\gamma$ ist die volle Ableitung $\frac{\mathrm{d}}{\mathrm{d} t}\varphi(\gamma)$ (Stufe [4](wann-nur-start-und-ziel-zahlen.html#stufe-4)) |
| Poincaré-Lemma | Integrabilität macht den Integranden zu $\frac{\mathrm{d}}{\mathrm{d} t}[tF_k(t\boldsymbol{x})]$ (Stufe [5](das-poincare-lemma.html#stufe-5)) |
| Potential längs der Achsen | Integrabilität plus Hauptsatz in jeder Koordinate (Stufe [6](potentiale-berechnen.html#stufe-6)) |
| Homotopieinvarianz | Änderung des Integrals ist eine volle $t$-Ableitung, also Randterm (Stufe [7](verformen-und-zweiter-hauptsatz.html#stufe-7)) |
| Green und Gauß | Hauptsatz in $x$ und $y$, Innenkanten heben sich auf (Stufe [8](integralsatze-in-der-ebene.html#stufe-8)) |
