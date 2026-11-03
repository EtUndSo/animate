---
title: Das Wichtigste bis hier
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Laplace-Transformation
order: 3220900
summary: Jedes Signal als Überlagerung von $\mathrm{e}^{pt}$, und warum ein LTI-System daraus eine Multiplikation macht
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein LTI-System kann den Baustein $\mathrm{e}^{pt}$ nur mit einer Zahl $H(p)$ multiplizieren, weil bei $\mathrm{e}^{pt}$ Verschieben dasselbe ist wie Multiplizieren.

</li>

<li>

Jedes Signal mit Konvergenzbereich ist eine Überlagerung solcher Bausteine. $S(p)$ gibt an, mit welchem Gewicht der Baustein $\mathrm{e}^{pt}$ im Signal steckt.

</li>

<li>

Deshalb wird aus der Faltung eine Multiplikation, $G(p)=H(p)\,S(p)$. Bei rationalem $S(p)$ ist das Signal eine endliche Summe $\sum_r A_r\mathrm{e}^{p_r t}$ mit den Polen als Exponenten.

</li>

</ol>
:::

:::kern Das Wichtigste bis hier
<ul>

<li>

$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\mathrm{e}^{pt}$, daher $\mathrm{e}^{pt}*h=H(p)\,\mathrm{e}^{pt}$ mit $H(p)=\int h(t)\mathrm{e}^{-pt}\mathrm{d} t$.

</li>

<li>

$p=\sigma+\mathrm{j}2\pi f$: $\sigma$ ist die Wachstumsrate, $f$ die Frequenz des Bausteins.

</li>

<li>

$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\mathrm{e}^{pt}\mathrm{d} p$, $\sigma$ im Konvergenzbereich; jede solche Linie liefert dasselbe $s(t)$.

</li>

<li>

$S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}$; für $\sigma=0$ die Fourier-Transformation.

</li>

<li>

Konvergenzbereich: hängt nur von $\sigma$ ab; rechtsseitig eine rechte Halbebene, linksseitig eine linke, zweiseitig ein Streifen.

</li>

<li>

$\mathrm{e}^{p_0t}\varepsilon(t)\leftrightarrow\frac{1}{p-p_0}$ für $\operatorname{Re} p>\operatorname{Re} p_0$; $-\mathrm{e}^{p_0t}\varepsilon(-t)\leftrightarrow\frac{1}{p-p_0}$ für $\operatorname{Re} p<\operatorname{Re} p_0$.

</li>

<li>

$G(p)=S(p)H(p)$; Ableiten $\to p$, Integrieren $\to1/p$.

</li>

<li>

Rational und rechtsseitig: $s(t)=A_0\delta(t)+\sum_rA_r\mathrm{e}^{p_rt}\varepsilon(t)$, Pole = Exponenten. Kausal und stabil: alle Pole links.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast jedes Ergebnis zur Laplace-Transformation ist eine Folge dieser drei Sätze. Die Tabelle ordnet zu, die Stufen erklären.

| Ergebnis | Woher es kommt |
|---|---|
| Eigenfunktion $\mathrm{e}^{pt}$, Übertragungsfunktion $H(p)$ | Verschieben von $\mathrm{e}^{pt}$ ist Multiplizieren mit $\mathrm{e}^{-p\tau}$ (Stufe [1](warum-gerade.html#stufe-1)) |
| Laplace-Transformierte $S(p)$ | Gewicht des Bausteins $\mathrm{e}^{pt}$ im Signal (Stufe [2](ein-signal-aus-lauter-bausteinen.html#stufe-2)) |
| Konvergenzbereich | die Dämpfungen $\sigma$, mit denen $s(t)\mathrm{e}^{-\sigma t}$ absolut integrierbar wird (Abschnitt [2.3](konvergenzbereich-welche-dampfungen-funktionieren.html#stufe-2-3)) |
| Faltung $\to$ Produkt, Kettenschaltung | jeder Baustein wird mit $H(p)$ multipliziert (Stufe [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3)) |
| Ableitung $\to p$, Integral $\to 1/p$ | $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ und $\int_{-\infty}^t\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$ (Stufe [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3)) |
| Differentialgleichung $\to$ Polynombruch | jede Ableitung wird ein Faktor $p$ (Stufe [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3)) |
| Pole, Partialbrüche | die Exponenten und Gewichte der endlich vielen Bausteine (Stufe [4](aus-dem-integral-wird-eine-summe.html#stufe-4)) |
| Stabilität | ein kausaler Baustein $\mathrm{e}^{p_r t}$ klingt nur ab, wenn $\operatorname{Re} p_r<0$ (Stufe [4](aus-dem-integral-wird-eine-summe.html#stufe-4)) |
| Fourier-Transformation | dieselbe Überlagerung auf der Linie $\sigma=0$ (Stufe [2](ein-signal-aus-lauter-bausteinen.html#stufe-2)) |
