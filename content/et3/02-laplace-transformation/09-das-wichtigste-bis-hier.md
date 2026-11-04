---
title: Das Wichtigste bis hier
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220900
summary: Eigenfunktionen, Pole und Nullstellen, Differentialgleichungen, Stabilität und Systemaufbau
tags: 
lang: de
---

:::kern Das Wichtigste bis hier
<ul>

<li>

$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\mathrm{e}^{pt}$, daher $\mathrm{e}^{pt}*h=H(p)\,\mathrm{e}^{pt}$ mit $H(p)=\int h(t)\mathrm{e}^{-pt}\mathrm{d} t$.

</li>

<li>

$p=\sigma+\mathrm{j}2\pi f$: $\sigma$ ist die Wachstumsrate, $f$ die Frequenz von $\mathrm{e}^{pt}$.

</li>

<li>

$S(p)=\int s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$; der Konvergenzbereich hängt nur von $\operatorname{Re} p$ ab: rechtsseitig rechts aller Pole, linksseitig links aller Pole, zweiseitig ein Streifen.

</li>

<li>

$\mathrm{e}^{p_0t}\varepsilon(t)\leftrightarrow\frac{1}{p-p_0}$ für $\operatorname{Re} p>\operatorname{Re} p_0$; $-\mathrm{e}^{p_0t}\varepsilon(-t)\leftrightarrow\frac{1}{p-p_0}$ für $\operatorname{Re} p<\operatorname{Re} p_0$.

</li>

<li>

$G(p)=S(p)H(p)$; Ableiten $\to\cdot p$, Integrieren $\to\cdot1/p$; Differentialgleichung $\to$ Polynombruch.

</li>

<li>

Partialbrüche: $A_r=\lim_{p\to p_r}(p-p_r)H(p)$; kausal $h(t)=A_0\delta(t)+\sum_rA_r\mathrm{e}^{p_rt}\varepsilon(t)$.

</li>

<li>

RLC: $p_{1,2}=-\xi\omega_0\pm\omega_0\sqrt{\xi^2-1}$; Kriechfall, Grenzfall, Schwingfall.

</li>

<li>

Kausal und stabil $\iff$ alle Pole in der linken Halbebene.

</li>

<li>

Rückkopplung: $H=\frac{H_1}{1+H_1H_2}$; Impedanzen $R$, $\frac{1}{pC}$, $pL$.

</li>

<li>

$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma_0-\mathrm{j}\infty}^{\sigma_0+\mathrm{j}\infty}S(p)\mathrm{e}^{pt}\mathrm{d} p$ mit $\sigma_0$ im Konvergenzbereich.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein LTI-System kann $\mathrm{e}^{pt}$ nur mit einer Zahl $H(p)$ multiplizieren, weil bei $\mathrm{e}^{pt}$ Verschieben dasselbe ist wie Multiplizieren.

</li>

<li>

Die Laplace-Transformierte $S(p)$ gibt an, mit welchem Gewicht $\mathrm{e}^{pt}$ im Signal steckt; deshalb wird aus der Faltung das Produkt $G(p)=H(p)\,S(p)$ und aus jeder Ableitung ein Faktor $p$.

</li>

<li>

Bei rationalem $S(p)$ ist das Signal eine endliche Summe $\sum_r A_r\mathrm{e}^{p_r t}$: Die Pole sind die Exponenten, und ihre Lage entscheidet über Abklingen, Schwingen und Stabilität.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast jedes Ergebnis dieses Kapitels folgt aus der Eigenfunktion $\mathrm{e}^{pt}$:

| Ergebnis | Woher es kommt |
|---|---|
| Übertragungsfunktion $H(p)$ | Eigenwert von $\mathrm{e}^{pt}$ (Abschnitt [1](eigenfunktionen-von-lti-systemen.html#stufe-1)) |
| Konvergenzbereich | $\vert \mathrm{e}^{-pt}\vert =\mathrm{e}^{-\sigma t}$ hängt nur von $\sigma$ ab (Abschnitt [2](beispiele-zur-laplace-transformation.html#stufe-2)) |
| Pole, Nullstellen, Produktform | $S(p)$ ist bei Exponentialimpulsen ein Polynombruch (Abschnitt [3](pole-und-nullstellen-in-der-ebene.html#stufe-3)) |
| Faltung $\to$ Produkt | jede Funktion $\mathrm{e}^{pt}$ wird mit $H(p)$ multipliziert (Abschnitt [3](pole-und-nullstellen-in-der-ebene.html#stufe-3)) |
| Ableitung $\to p$, Integral $\to 1/p$ | $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$, $\int_{-\infty}^t\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$ (Abschnitt [3](pole-und-nullstellen-in-der-ebene.html#stufe-3)) |
| Differentialgleichung $\to$ Polynombruch | jede Ableitung wird ein Faktor $p$ (Abschnitt [4](losung-von-differentialgleichungen.html#stufe-4)) |
| Partialbrüche | jeder Pol ist der Exponent einer Funktion $\mathrm{e}^{p_rt}$ (Abschnitt [4](losung-von-differentialgleichungen.html#stufe-4)) |
| Stabilität | $\mathrm{e}^{p_rt}\varepsilon(t)$ klingt nur ab, wenn $\operatorname{Re} p_r<0$ (Abschnitt [5](stabilitat.html#stufe-5)) |
| Rückkopplung, Impedanzen | im Bildbereich ist alles Multiplikation (Abschnitt [6](systemanalyse-und-synthese.html#stufe-6)) |
| Umkehrformel | Überlagerung der $\mathrm{e}^{pt}$ auf einer Geraden (Abschnitt [7](tabellen-und-umkehrformel.html#stufe-7)) |
