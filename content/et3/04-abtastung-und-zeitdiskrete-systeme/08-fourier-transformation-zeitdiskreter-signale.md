---
title: Stufe 7: Fourier-Transformation zeitdiskreter Signale
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Abtastung und zeitdiskrete Systeme
order: 3240800
summary: Welches Spektrum hat eine Zahlenfolge?
tags: periodische Faltung
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Welches Spektrum hat eine Zahlenfolge? Es ist das Spektrum des ideal abgetasteten Signals, direkt aus den Abtastwerten berechnet.
:::

Setzt man $s_\mathrm a(t)=\sum_ns(nT)\delta(t-nT)$ in das Fourier-Integral ein, bleibt mit der Siebeigenschaft eine Summe. Normiert auf $T=1$:

:::satz Satz 7.1 (Fourier-Transformation zeitdiskreter Signale)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$S_\mathrm a(f)=\sum_{n=-\infty}^{\infty}s(n)\,\mathrm{e}^{-\mathrm{j}2\pi nf},\qquad s(n)=\int_{-1/2}^{1/2}S_\mathrm a(f)\,\mathrm{e}^{\mathrm{j}2\pi nf}\,\mathrm{d} f. \tag{7.1}$$
:::

⁠**So liest man das:** $S_\mathrm a(f)$ ist periodisch mit der Periode 1, das ist die Abtastrate. Eine Periode, $|f|\le\frac12$, enthält alles. Deshalb integriert die Rücktransformation nur über ein Intervall der Länge 1. Die Summe ist eine Fourier-Reihe in $f$, mit den Abtastwerten als Koeffizienten.

::::beispiel
Für $s(n)=\varepsilon(n)\,b^n$ mit $|b|<1$ (geometrische Reihe):

<span class="anker" id="gl-7-2"></span>
$$S_\mathrm a(f)=\sum_{n=0}^{\infty}\bigl(b\,\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)^n=\frac{1}{1-b\,\mathrm{e}^{-\mathrm{j}2\pi f}},\qquad|S_\mathrm a(f)|^2=\frac{1}{1+b^2-2b\cos(2\pi f)}. \tag{7.2}$$

Das ist zugleich der Frequenzgang $H_\mathrm a(f)$ des rekursiven Systems aus Stufe [6](ein-rekursives-system.html#stufe-6). Für $b=0{,}6$: $|H_\mathrm a|=2{,}5$ bei $f=0$, $1{,}60$ bei $f=0{,}1$, $0{,}86$ bei $f=0{,}25$, $0{,}625$ bei $f=0{,}5$ (Abb. [6](#abb-6)). Das System ist ein Tiefpass, aber mit periodischem Frequenzgang: Bei $f=1$ verstärkt es wieder so stark wie bei $f=0$.

:::abbildung et3/k4dtft 6
Betrag des Frequenzgangs des rekursiven Systems mit $b=0{,}6$. Er ist periodisch mit der Abtastrate. Zwischen den roten Linien liegt die eine Periode, die alles beschreibt.
:::
::::

**Faltung und Multiplikation.** Wie bei Funktionen gilt $s(n)*h(n)\;\circ\!\!-\!\!\bullet\;S_\mathrm a(f)H_\mathrm a(f)$. Das Produkt zweier Folgen ergibt die __periodische Faltung__ der Spektren über eine Periode:

<span class="anker" id="gl-7-3"></span>
$$s(n)\cdot h(n)\;\circ\!\!-\!\!\bullet\;\int_{-1/2}^{1/2}S_\mathrm a(\nu)\,H_\mathrm a(f-\nu)\,\mathrm{d}\nu. \tag{7.3}$$

:::aufgabe Aufgabe 7 ★ Gleitender Mittelwert
<span class="anker" id="aufg-7"></span>

$h(n)=\frac13\bigl[\delta(n)+\delta(n-1)+\delta(n-2)\bigr]$ mittelt drei aufeinanderfolgende Werte.

<ol class="al">

<li>

Zeige $H_\mathrm a(f)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

</li>

<li>

Bei welcher Frequenz ist $H_\mathrm a=0$? Welche Schwingung löscht das Filter also vollständig aus, und warum (Tipp: Summe dreier Werte einer Schwingung mit der Periode 3)?

</li>

</ol>

:::loesung
(a) $\frac13\bigl(1+\mathrm{e}^{-\mathrm{j}2\pi f}+\mathrm{e}^{-\mathrm{j}4\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl(\mathrm{e}^{\mathrm{j}2\pi f}+1+\mathrm{e}^{-\mathrm{j}2\pi f}\bigr)=\frac13\mathrm{e}^{-\mathrm{j}2\pi f}\bigl[1+2\cos(2\pi f)\bigr]$.

(b) $\cos(2\pi f)=-\frac12$, also $f=\frac13$ (bei $f_\mathrm A=1$ kHz: 333 Hz). Eine Schwingung mit drei Werten je Periode besteht aus drei Zeigern im Abstand $120^\circ$. Ihre Summe ist null, das Filter sieht in jedem Fenster genau eine ganze Periode.
:::
:::
