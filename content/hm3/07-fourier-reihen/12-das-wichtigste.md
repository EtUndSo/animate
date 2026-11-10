---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Fourier-Reihen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/fourier-reihen
knoten: Kapitel 7: Fourier-Reihen
order: 3171200
summary: Wie eine periodische Kurve in reine Schwingungen zerfällt
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

$\hat{\boldsymbol{e}}_k(x)=\mathrm{e}^{\mathrm{i}kx}$, $\langle\hat{\boldsymbol{e}}_k,\hat{\boldsymbol{e}}_\ell\rangle=\delta_{k\ell}$, $c_k=\langle f,\hat{\boldsymbol{e}}_k\rangle$, $T_Nf=\sum_{|k|\le N}c_k\hat{\boldsymbol{e}}_k$.

</li>

<li>

Reell: $c_k=\frac12(a_k-\mathrm{i}\,b_k)$, $T_Nf=\frac{a_0}2+\sum_{k=1}^N(a_k\cos kx+b_k\sin kx)$. Gerade: $b_k=0$. Ungerade: $a_k=0$.

</li>

<li>

Verschiebung um $\tau$: $\mathrm{e}^{\mathrm{i}\tau k}c_k$. Ableitung: $\mathrm{i}k\,c_k$, auch bei Knicken, nicht bei Sprüngen.

</li>

<li>

Bestapproximation: $\|f-S_N\|_2^2=\|f-T_Nf\|_2^2+\|T_Nf-S_N\|_2^2$. Bessel gibt $c_k\to0$.

</li>

<li>

Parseval: $\frac1{2\pi}\int_0^{2\pi}|f|^2\mathrm{d} x=\sum_{k\in\mathbb{Z}}|c_k|^2$, reell $\frac1\pi\int_0^{2\pi}f^2\mathrm{d} x=\frac12a_0^2+\sum_{n\ge1}(a_n^2+b_n^2)$, allgemein $\langle f,g\rangle=\sum c_k\overline{d_k}$. So folgen $\sum\frac1{k^2}=\frac{\pi^2}6$ und $\sum\frac{(-1)^{k+1}}{k^2}=\frac{\pi^2}{12}$.

</li>

<li>

Dirac-Schar: $\eta_\varepsilon\ge0$, Fläche 1, $\eta_\varepsilon*f\to f$. Grenzwert ist keine Funktion: $\int f\,\mathrm{d}\delta_0=f(0)$.

</li>

<li>

Dirichlet-Kern: $D_N(x)=\sin((N+\frac12)x)/\sin\frac x2$, $T_Nf=D_N\circledast f$, aber $\int|D_N|\to\infty$.

</li>

<li>

Stückweise stetig differenzierbar: $T_Nf(x)\to\frac12(f(x^+)+f(x^-))$. Zusätzlich stetig: gleichmäßig. $\sum|k|^m|c_k|<\infty$: $f$ ist $m$-mal stetig differenzierbar, Ableitungen gliedweise.

</li>

<li>

Dirichlet-Problem: $u(r\mathrm{e}^{\mathrm{i}\varphi})=\sum_kc_kr^{|k|}\mathrm{e}^{\mathrm{i}k\varphi}$, Poisson-Kern $P_r(\varphi)=\frac{1-r^2}{1-2r\cos\varphi+r^2}$. Eindeutig nach dem Maximumprinzip.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Die Schwingungen $\mathrm{e}^{\mathrm{i}kx}$ stehen senkrecht aufeinander, deshalb liest ein Skalarprodukt den Anteil jeder Schwingung ab, und das Fourier-Polynom ist die Projektion von $f$, also die beste Näherung im quadratischen Mittel.

</li>

<li>

Im quadratischen Mittel geht nichts verloren: Für jede Riemann-integrierbare Funktion ist die Energie von $f$ die Summe der Energien ihrer Schwingungen.

</li>

<li>

An einzelnen Stellen entscheidet die Glattheit: Fourier-Polynome mitteln mit einem oszillierenden Kern, stückweise glatte $f$ werden punktweise dargestellt, Sprünge durch ihre Mitte, und je schneller die $c_k$ fallen, desto glatter ist $f$.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Fast alles in diesem Kapitel folgt aus zwei Tatsachen: Die Bausteine sind orthonormal, und ein Fourier-Polynom ist ein gewichteter Mittelwert.

| Ergebnis | Woher es kommt |
|---|---|
| $\langle\hat{\boldsymbol{e}}_k,\hat{\boldsymbol{e}}_\ell\rangle=\delta_{k\ell}$ | Stammfunktion von $\mathrm{e}^{\mathrm{i}(k-\ell)x}$ ist periodisch (Stufe [1](schwingungen-als-bausteine.html#stufe-1)) |
| Regeln für $c_k$ | Symmetrie und partielle Integration im Integral (Stufe [3](rechenregeln.html#stufe-3)) |
| Reihe des Sägezahns | geschlossene Summe der $\mathrm{e}^{\mathrm{i}kx}$, Integration gibt $1/N$ (Stufe [4](der-sagezahn-zu-fu.html#stufe-4)) |
| Bestapproximation, Bessel | Lot auf den Unterraum, Pythagoras (Stufe [5](die-beste-naherung.html#stufe-5)) |
| Parseval | eine Stufe exakt, dann Treppen (Stufe [6](konvergenz-im-quadratischen-mittel.html#stufe-6)) |
| $\eta_\varepsilon*f\to f$ | Fläche 1 und Gewicht $\ge0$ auf kleinem Fenster (Stufe [7](mitteln-mit-dirac-scharen.html#stufe-7)) |
| Mitte am Sprung | Bessel für $h$, also Riemann-Lebesgue (Stufe [8](punktweise-konvergenz.html#stufe-8)) |
| Gleichmäßige Konvergenz | $\vert c_k\vert \le\frac12(\vert d_k\vert ^2+k^{-2})$ und M-Test (Stufe [9](gleichmaige-konvergenz-und-glattheit.html#stufe-9)) |
| Poisson-Formel | Potenzansatz, geometrische Reihe (Stufe [10](das-dirichlet-problem.html#stufe-10)) |
| Eindeutigkeit | Spur der Hesse-Matrix im Maximum (Stufe [10](das-dirichlet-problem.html#stufe-10)) |
