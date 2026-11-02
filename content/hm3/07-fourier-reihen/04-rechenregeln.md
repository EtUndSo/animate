---
title: Stufe 3: Rechenregeln
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3170400
summary: Viele Koeffizienten lassen sich ohne neues Integral bestimmen.
tags: Fourier-Reihe
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Viele Koeffizienten lassen sich ohne neues Integral bestimmen. Diese Stufe sammelt die Regeln für Summen, Symmetrien, Verschiebungen und Ableitungen.
:::

**Die Idee.** Der Mechanismus ist jeweils eine Eigenschaft des Integrals in [(2.1)](koeffizienten-und-polynome.html#gl-2-1). Das Integral ist linear. Über eine symmetrische Periode verschwindet das Integral einer ungeraden Funktion. Eine Verschiebung von $f$ dreht jeden Zeiger nur. Beim Ableiten wälzt die partielle Integration die Ableitung auf $\mathrm{e}^{-\mathrm{i}kx}$ ab, und dort entsteht ein Faktor.

:::satz Satz 3.1 (Rechenregeln)
<span class="anker" id="satz-3-1"></span>

Seien $f,g$ wie in Definition [2.1](koeffizienten-und-polynome.html#satz-2-1) mit Koeffizienten $c_k$ und $d_k$ und sei $\lambda\in\mathbb{C}$.

<ol class="rm">

<li>

Linearität: $f+\lambda g$ hat die Koeffizienten $c_k+\lambda d_k$. Dasselbe gilt für $a_k$ und $b_k$.

</li>

<li>

Ist $f$ reellwertig, sind $a_k$, $b_k$ reell, und es gilt $c_k=\overline{c_{-k}}$ für alle $k\in\mathbb{N}_0$.

</li>

<li>

Ist $f$ gerade, also $f(x)=f(-x)$ für alle $x$, gilt $b_k=0$ für alle $k\in\mathbb{N}$.

</li>

<li>

Ist $f$ ungerade, also $f(x)=-f(-x)$ für alle $x$, gilt $a_k=0$ für alle $k\in\mathbb{N}_0$.

</li>

<li>

Verschiebung: $\tilde f(x):=f(x+\tau)$ hat die Koeffizienten $\tilde c_k=\mathrm{e}^{\mathrm{i}\tau k}c_k$.

</li>

<li>

Ableitung: Ist $f$ stetig differenzierbar, hat $f'$ die Koeffizienten $\mathrm{i}k\,c_k$.

</li>

</ol>
:::

:::beweis Rechenregeln
(i) Das Integral ist linear. (ii) $a_k,b_k$ sind Integrale reeller Funktionen, und Konjugieren in [(2.1)](koeffizienten-und-polynome.html#gl-2-1) ändert nur das Vorzeichen im Exponenten. (iii) Man integriert über $(-\pi,\pi)$. Dort ist $f(x)\sin kx$ ungerade, also ist das Integral null. (iv) Ebenso mit $f(x)\cos kx$. (v) Mit $z=x+\tau$ ist $\tilde c_k=\frac1{2\pi}\int_\tau^{2\pi+\tau}f(z)\,\mathrm{e}^{-\mathrm{i}k(z-\tau)}\,\mathrm{d} z=\mathrm{e}^{\mathrm{i}k\tau}c_k$, denn jede volle Periode ist erlaubt. (vi) Partielle Integration gibt

$$\frac1{2\pi}\int_0^{2\pi}f'(x)\,\mathrm{e}^{-\mathrm{i}kx}\,\mathrm{d} x=\frac1{2\pi}\Bigl[f(x)\,\mathrm{e}^{-\mathrm{i}kx}\Bigr]_0^{2\pi}+\mathrm{i}k\,\frac1{2\pi}\int_0^{2\pi}f(x)\,\mathrm{e}^{-\mathrm{i}kx}\,\mathrm{d} x,$$

und der Randterm ist null, weil $f(2\pi)=f(0)$ gilt.
:::

⁠**So liest man das:** In (v) bleibt jeder Betrag $|c_k|$ gleich, nur die Phase ändert sich. In (vi) wird eine Schwingung beim Ableiten um den Faktor $|k|$ verstärkt, hohe Frequenzen also am stärksten. **Wozu die Voraussetzung in (vi)?** Die Regel gilt weiter, wenn $f$ stetig ist und aus endlich vielen stetig differenzierbaren Stücken besteht: Man integriert stückweise partiell, und die Randterme an den Knicken heben sich auf, weil $f$ dort stetig ist. An einem Sprung bleibt dagegen ein Randterm übrig: $q$ hat abseits der Sprünge die Ableitung 0, trotzdem ist $c_1\neq0$.

**Beispiel: das Dreieck ohne Integral.** $w$ ist gerade, also ist $b_k=0$. Weiter ist $w$ stetig, stückweise stetig differenzierbar, und $w'=q$. Aus [(2.6)](koeffizienten-und-polynome.html#gl-2-6) folgt für ungerades $k$ der Koeffizient $c_k(q)=-\mathrm{i}\,b_k/2=-\frac{2\mathrm{i}}{\pi k}$. Regel (vi) gibt $c_k(w)=c_k(q)/(\mathrm{i}k)=-\frac2{\pi k^2}$, und für gerades $k\neq0$ ist $c_k(w)=0$. Für $k=0$ sagt (vi) nichts, dort ist $c_0(w)=\frac\pi2$ der Mittelwert. Mit $a_k=2c_k$ folgt

<span class="anker" id="gl-3-1"></span>
$$T_Nw(x)=\frac\pi2-\frac4\pi\sum_{k\le N,\ k\text{ ungerade}}\frac{\cos kx}{k^2}. \tag{3.1}$$

⁠**Kontrolle:** Bei $x=0$ soll $w(0)=0$ herauskommen. Es ist $T_1w(0)=\frac\pi2-\frac4\pi\approx0{,}30$ und $T_3w(0)\approx0{,}16$. Abb. [3](#abb-3) vergleicht beide Funktionen.

:::abbildung hm3/k7regeln 3
Das Dreieck $w$ hat Knicke, seine Ableitung ist das Rechteck $q$ mit Sprüngen. Rechts die Beträge ihrer Koeffizienten für ungerade $k$: Für $q$ sind sie um den Faktor $k$ größer als für $w$. Ein Knick lässt die Koeffizienten also schneller abfallen als ein Sprung.
:::

:::definition Definition 3.2 (Formale Fourier-Reihe)
<span class="anker" id="satz-3-2"></span>

Für $f$ wie in Definition [2.1](koeffizienten-und-polynome.html#satz-2-1) heißt $Tf=\sum_{k\in\mathbb{Z}}c_k\hat{\boldsymbol{e}}_k=\sum_{k\in\mathbb{Z}}\langle f,\hat{\boldsymbol{e}}_k\rangle\,\hat{\boldsymbol{e}}_k$ die formale __Fourier-Reihe__ von $f$.
:::

„Formal“ heißt: Das ist zunächst nur eine Liste von Koeffizienten. Ob die Reihe konvergiert, in welchem Sinn und gegen was, ist offen.

:::aufgabe Aufgabe 3 ★★ Regeln statt Integrale
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Bestimme mit Regel (v) die Koeffizienten von $f(x)=q(x+\frac\pi2)$. Erkläre, warum $f$ eine reine Cosinusreihe hat, und gib $a_1$, $a_3$, $a_5$ an.

</li>

<li>

Zeige für $m\in\mathbb{Z}$: $g(x)=\mathrm{e}^{\mathrm{i}mx}f(x)$ hat die Koeffizienten $c_{k-m}$. Was ist $c_3$ von $\mathrm{e}^{2\mathrm{i}x}q(x)$?

</li>

<li>

Bestimme $c_0$, $c_1$, $c_2$ von $h=2q+3w$ ohne Integral.

</li>

</ol>

:::loesung
(a) $\tilde c_k=\mathrm{e}^{\mathrm{i}k\pi/2}\cdot\bigl(-\frac{2\mathrm{i}}{\pi k}\bigr)$ für ungerades $k$, sonst 0. $f$ ist $1$ auf $(-\frac\pi2,\frac\pi2)$ und $-1$ auf $(\frac\pi2,\frac{3\pi}2)$, also gerade, und deshalb ist $b_k=0$. Mit $a_k=2\tilde c_k$ folgt $a_1=\frac4\pi$, $a_3=-\frac4{3\pi}$, $a_5=\frac4{5\pi}$. (b) $\frac1{2\pi}\int_0^{2\pi}\mathrm{e}^{\mathrm{i}mx}f(x)\,\mathrm{e}^{-\mathrm{i}kx}\,\mathrm{d} x=\frac1{2\pi}\int_0^{2\pi}f(x)\,\mathrm{e}^{-\mathrm{i}(k-m)x}\,\mathrm{d} x=c_{k-m}$. Der Koeffizient $c_3$ von $\mathrm{e}^{2\mathrm{i}x}q$ ist also $c_1(q)=-\frac{2\mathrm{i}}\pi$. (c) Linearität: $c_0=3\cdot\frac\pi2=\frac{3\pi}2$, $c_1=2\cdot\bigl(-\frac{2\mathrm{i}}\pi\bigr)+3\cdot\bigl(-\frac2\pi\bigr)=-\frac{6+4\mathrm{i}}\pi$, $c_2=0$.
:::
:::
