---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Fourier-Reihe und -Transformation
order: 3231300
summary: Jedes Signal als Überlagerung von Schwingungen
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein periodisches Signal ist eine Summe von Schwingungen bei Vielfachen der Grundfrequenz (Fourier-Reihe), ein einmaliges Signal ein Integral über alle Frequenzen (Fourier-Integral).

</li>

<li>

Jede Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ ist eine Eigenfunktion: Ein LTI-System multipliziert sie mit $H(f)$, deshalb wird aus der Faltung das Produkt $G(f)=S(f)\,H(f)$.

</li>

<li>

Alle Rechenregeln (Verschiebung, Dehnung, Modulation, Symmetrie) folgen daraus, was die jeweilige Operation mit einer einzelnen Schwingung macht.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

$\mathrm{e}^{\mathrm{j}2\pi ft}*h=H(f)\mathrm{e}^{\mathrm{j}2\pi ft}$; $H(f)=\int h\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$.

</li>

<li>

Reihe: $s_p=\sum S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$, $S_p(k)=\frac1T\int_Ts_p\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t$; reell: $S_p(-k)=S_p^*(k)$.

</li>

<li>

Parseval: $\frac1T\int_T|s_p|^2=\sum|S_p(k)|^2$; Gibbs: etwa 9 % Überschwingen an Sprüngen; LTI: $G_p(k)=S_p(k)H(kF)$.

</li>

<li>

$S(f)=\int s\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$, $s=\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$; $s*h\leftrightarrow SH$, $s_1s_2\leftrightarrow S_1*S_2$.

</li>

<li>

Reell: $S(-f)=S^*(f)$; gerade $\leftrightarrow\operatorname{Re} S$, ungerade $\leftrightarrow\mathrm{j}\operatorname{Im} S$.

</li>

<li>

$s(bt)\leftrightarrow\frac1{|b|}S(f/b)$; $s(t-t_0)\leftrightarrow S\mathrm{e}^{-\mathrm{j}2\pi ft_0}$; $\frac{\mathrm{d}}{\mathrm{d} t}\leftrightarrow\mathrm{j}2\pi f$; $\mathrm{e}^{\mathrm{j}2\pi Ft}s\leftrightarrow S(f-F)$; $S(t)\leftrightarrow s(-f)$.

</li>

<li>

$\operatorname{rect}(t/T)\leftrightarrow|T|\operatorname{si}(\pi Tf)$; $\Lambda\leftrightarrow\operatorname{si}^2$; $\delta\leftrightarrow1$; $1\leftrightarrow\delta(f)$; $\cos\leftrightarrow\frac12[\delta(f+F)+\delta(f-F)]$.

</li>

<li>

Kamm $\leftrightarrow$ Kamm: $\sum\delta(t-nT)\leftrightarrow\frac1{|T|}\sum\delta(f-k/T)$; $\varepsilon\leftrightarrow\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$.

</li>

<li>

Hilbert: $h=\frac{1}{\pi t}$, $H=-\mathrm{j}\operatorname{sgn}(f)$; $s_+=\frac12(s+\mathrm{j}\hat s)$, $s=2\operatorname{Re} s_+$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.**

| Ergebnis | Woher es kommt |
|---|---|
| Frequenzgang $H(f)$ | Eigenwert der Schwingung $\mathrm{e}^{\mathrm{j}2\pi ft}$ (Stufe [1](schwingungen-als-eigenfunktionen.html#stufe-1)) |
| Fourier-Reihe, nur Vielfache von $F$ | nur diese Schwingungen haben die Periode $T$ (Stufe [2](periodische-signale-die-fourier-reihe.html#stufe-2)) |
| Analyseformel der Reihe | Schwingungen verschiedener Frequenz sind orthogonal (Stufe [2](periodische-signale-die-fourier-reihe.html#stufe-2)) |
| Parseval, Gibbs, LTI mit periodischem Eingang | jede Harmonische für sich (Stufe [3](leistung-konvergenz-und-lti-systeme.html#stufe-3)) |
| Fourier-Integral | Periode $\to\infty$, die Linien rücken zusammen (Stufe [4](vom-periodischen-zum-einmaligen-signal.html#stufe-4)) |
| $S(-f)=S^*(f)$ bei reellen Signalen | Schwingungen treten in konjugierten Paaren auf (Stufe [5](symmetrien-im-signal-und-im-spektrum.html#stufe-5)) |
| Verschiebung, Dehnung, Ableitung, Modulation | was die Operation mit $\mathrm{e}^{\mathrm{j}2\pi ft}$ macht (Stufe [6](die-rechenregeln-theoreme.html#stufe-6)) |
| Symmetrie (Dualität) | Hin- und Rücktransformation unterscheiden sich nur im Vorzeichen (Stufe [6](die-rechenregeln-theoreme.html#stufe-6)) |
| Linienspektren, Dirac-Kamm, Sprung | Grenzfälle mit Dirac-Impulsen (Stufe [8](singulare-signale-und-linienspektren.html#stufe-8)) |
| Hilbert-Transformation | ein kausales Signal ist durch eine Hälfte festgelegt (Stufe [9](hilbert-transformation-und-analytisches-signal.html#stufe-9)) |
| Kurzzeit-Fourier | Spektrum eines Ausschnitts (Stufe [10](kurzzeit-fourier-transformation.html#stufe-10)) |
