---
title: Stufe 6: Konvergenz im quadratischen Mittel
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3170700
summary: Die Energie von T Nf bleibt unter der von f .
tags: Treppenfunktionen, Parseval-Identität
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Energie von $T_Nf$ bleibt unter der von $f$. Diese Stufe zeigt, dass im Grenzwert nichts fehlt: Die Bausteine reichen für jede Riemann-integrierbare Funktion.
:::

**Die Idee.** Nach Satz [5.1](die-beste-naherung.html#satz-5-1) (iii) ist $\|f-T_Nf\|_2^2=\|f\|_2^2-\sum_{|k|\le N}|c_k|^2$. Konvergenz im quadratischen Mittel heißt also $\sum_{k\in\mathbb{Z}}|c_k|^2=\|f\|_2^2$. Das zeigt man zuerst für eine einzelne Stufe, und zwar mit [(4.2)](der-sagezahn-zu-fu.html#gl-4-2). Daraus folgen __Treppenfunktionen__, also stückweise konstante Funktionen, und schließlich alle Riemann-integrierbaren Funktionen, weil Treppen sie beliebig genau annähern (Abb. [6](#abb-6)).

:::abbildung hm3/k7energie 6
Links: Die Energie von $T_Nq$ steigt gegen die Energie von $q$. Rechts: Der relative Fehler im quadratischen Mittel, logarithmisch. Für das Dreieck $w$ fällt er viel schneller als für das Rechteck $q$, denn $|c_k(w)|^2$ fällt wie $1/k^4$, $|c_k(q)|^2$ nur wie $1/k^2$.
:::

:::satz Satz 6.1 (Konvergenz im quadratischen Mittel)
<span class="anker" id="satz-6-1"></span>

Sei $f$ wie in Definition [2.1](koeffizienten-und-polynome.html#satz-2-1). Dann gilt $\|f-T_Nf\|_2\to0$ für $N\to\infty$ und die __Parseval-Identität__

<span class="anker" id="gl-6-1"></span>
$$\frac1{2\pi}\int_0^{2\pi}|f(x)|^2\,\mathrm{d} x=\sum_{k\in\mathbb{Z}}|c_k|^2. \tag{6.1}$$
:::

:::beweis Von der Stufe zur Riemann-integrierbaren Funktion
⁠**Schritt 1: eine Stufe.** Für $\beta\in(0,2\pi)$ sei $\chi_\beta=1$ auf $[0,\beta]$ und $\chi_\beta=0$ auf $(\beta,2\pi)$. Dann ist $c_0=\frac\beta{2\pi}$, $\|\chi_\beta\|_2^2=\frac\beta{2\pi}$, und für $k\neq0$ gilt

$$c_k=\frac1{2\pi}\int_0^\beta\mathrm{e}^{-\mathrm{i}kx}\,\mathrm{d} x=\frac{\mathrm{i}}{2\pi k}\bigl(\mathrm{e}^{-\mathrm{i}k\beta}-1\bigr),\qquad|c_k|^2=\frac{1-\cos k\beta}{2\pi^2k^2}.$$

Subtrahiert man [(4.2)](der-sagezahn-zu-fu.html#gl-4-2) bei $x=\beta$ von [(4.2)](der-sagezahn-zu-fu.html#gl-4-2) bei $x=0$, fällt $C$ weg:

$$\sum_{k\ge1}\frac{1-\cos k\beta}{k^2}=\frac{\pi^2-(\pi-\beta)^2}4=\frac{2\pi\beta-\beta^2}4.$$

Also ist $\sum_{k\in\mathbb{Z}}|c_k|^2=\frac{\beta^2}{4\pi^2}+\frac1{\pi^2}\sum_{k\ge1}\frac{1-\cos k\beta}{k^2}=\frac\beta{2\pi}=\|\chi_\beta\|_2^2$. Mit Satz [5.1](die-beste-naherung.html#satz-5-1) (iii) folgt $T_N\chi_\beta\to\chi_\beta$ im quadratischen Mittel.

⁠**Schritt 2: Treppen.** Eine Verschiebung $\chi_\beta(x+\tau)$ hat nach Satz [3.1](rechenregeln.html#satz-3-1) (v) dieselben $|c_k|$, also gilt für sie dasselbe. Jede periodische Treppenfunktion $\psi$ ist, bis auf endlich viele Stellen, eine endliche Linearkombination solcher Verschiebungen und der Konstanten. Weil $T_N$ linear ist, folgt mit der Dreiecksungleichung $\|\psi-T_N\psi\|_2\to0$.

⁠**Schritt 3: allgemein.** Real- und Imaginärteil lassen sich getrennt behandeln, also sei $f$ reell mit $|f|\le M$. Zu $\varepsilon>0$ gibt es nach Definition des Riemann-Integrals Treppenfunktionen $\psi\le f\le\psi^+$ mit $|\psi|,|\psi^+|\le M$ und $\frac1{2\pi}\int_0^{2\pi}(\psi^+-\psi)\,\mathrm{d} x\le\varepsilon^2/(2M)$. Dann ist

$$\|f-\psi\|_2^2=\frac1{2\pi}\int_0^{2\pi}|f-\psi|^2\,\mathrm{d} x\le2M\cdot\frac1{2\pi}\int_0^{2\pi}(\psi^+-\psi)\,\mathrm{d} x\le\varepsilon^2.$$

Weil $T_N\psi\in\mathcal V_N$ ist, gibt Satz [5.1](die-beste-naherung.html#satz-5-1) (ii) für große $N$

$$\|f-T_Nf\|_2\le\|f-T_N\psi\|_2\le\|f-\psi\|_2+\|\psi-T_N\psi\|_2\le2\varepsilon.$$
:::

⁠**So liest man das:** Die mittlere Leistung einer Funktion ist die Summe der Leistungen ihrer Schwingungen, keine Frequenz fehlt. Mit $|c_k|^2+|c_{-k}|^2=\frac12(|a_k|^2+|b_k|^2)$ lautet die Identität reell

<span class="anker" id="gl-6-2"></span>
$$\begin{aligned} \frac1\pi\int_0^{2\pi}|f(x)|^2\,\mathrm{d} x&=\frac12|a_0|^2+\sum_{n=1}^\infty\bigl(|a_n|^2+|b_n|^2\bigr),\\ \frac1\pi\int_0^{2\pi}f(x)^2\,\mathrm{d} x&=\frac12a_0^2+\sum_{n=1}^\infty\bigl(a_n^2+b_n^2\bigr)\quad\text{für reelles }f. \end{aligned} \tag{6.2}$$

:::satz Satz 6.2 (Allgemeine Parseval-Identität)
<span class="anker" id="satz-6-2"></span>

Haben $f,g$ wie in Definition [2.1](koeffizienten-und-polynome.html#satz-2-1) die Koeffizienten $c_k$ und $d_k$, so gilt

<span class="anker" id="gl-6-3"></span>
$$\frac1{2\pi}\int_0^{2\pi}f(x)\,\overline{g(x)}\,\mathrm{d} x=\sum_{k\in\mathbb{Z}}c_k\overline{d_k}. \tag{6.3}$$
:::

:::beweis Allgemeine Parseval-Identität
Für die Polynome gilt wie in [(5.1)](die-beste-naherung.html#gl-5-1) $\langle T_Nf,T_Ng\rangle=\sum_{|k|\le N}c_k\overline{d_k}$. Die Summe konvergiert für $N\to\infty$ absolut, denn $|c_k\overline{d_k}|\le\frac12(|c_k|^2+|d_k|^2)$. Für die linke Seite gibt Cauchy-Schwarz ([Teil 6](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen/konvergenz-von-funktionenfolgen.html)) zusammen mit Bessel

$$|\langle f,g\rangle-\langle T_Nf,T_Ng\rangle|\le\|f-T_Nf\|_2\,\|g\|_2+\|f\|_2\,\|g-T_Ng\|_2\to0.$$
:::

⁠**So liest man das:** Das Skalarprodukt zweier Funktionen rechnet man in den Koeffizienten aus wie in $\mathbb{C}^n$. Für $g=f$ steht dort [(6.1)](#gl-6-1).

::::beispiel Reihenwerte
Für den Sägezahn ist $a_k=0$, $b_k=\frac1k$. Aus [(6.2)](#gl-6-2) folgt

<span class="anker" id="gl-6-4"></span>
$$\sum_{k=1}^\infty\frac1{k^2}=\frac1\pi\int_0^{2\pi}\Bigl(\frac{\pi-x}2\Bigr)^2\,\mathrm{d} x=\frac{\pi^2}6. \tag{6.4}$$

Damit ist auch die Zahl aus Stufe [4](der-sagezahn-zu-fu.html#stufe-4) bekannt: $C=\frac{\pi^2}4-\frac{\pi^2}6$, also $\sum_{k\ge1}\frac{(-1)^{k+1}}{k^2}=\frac{\pi^2}{12}$. **Kontrolle:** Für $f=1$ ist $c_0=1$, und beide Seiten von [(6.1)](#gl-6-1) sind 1.
::::

**Der passende Raum.** Die Theorie legt den Vektorraum $\mathcal V=\{f=\sum_{k\in\mathbb{Z}}c_k\hat{\boldsymbol{e}}_k:c_k\in\mathbb{C},\ \sum_{k\in\mathbb{Z}}|c_k|^2<\infty\}$ nahe. Er ist unendlichdimensional, und die $\hat{\boldsymbol{e}}_k$ bilden eine Orthonormalbasis. Nach Satz [6.1](#satz-6-1) enthält er die Riemann-integrierbaren Funktionen, er ist aber größer. Weil die Konvergenz nur im quadratischen Mittel stattfindet, sind seine Elemente im Allgemeinen nicht punktweise definiert. Man kann ihn mit dem Hilbertraum $L^2((0,2\pi);\mathbb{C})$ aus [Teil 6](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen/konvergenz-von-funktionenfolgen.html) gleichsetzen. Dieselbe Theorie gilt mit einem passenden Skalarprodukt für andere Orthonormalsysteme, etwa Legendre-, Laguerre- und Tschebyschow-Polynome.

:::frage Folgt daraus, dass $T_Nf(x)$ an jeder Stelle gegen $f(x)$ strebt?
Nein. Ändert man $f$ an einer einzigen Stelle, ändert sich kein Integral, also kein $c_k$. Die Reihe kann den Wert an dieser Stelle gar nicht kennen. Das quadratische Mittel sieht nur das Ganze.
:::

:::aufgabe Aufgabe 6 ★★ Reihenwerte aus Parseval
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Folgere aus $q$ den Wert von $\sum_{k\text{ ungerade}}\frac1{k^2}$. Prüfe das Ergebnis mit [(6.4)](#gl-6-4).

</li>

<li>

Folgere aus $w$ den Wert von $\sum_{k\text{ ungerade}}\frac1{k^4}$ und daraus $\sum_{k\ge1}\frac1{k^4}$.

</li>

</ol>

:::loesung
(a) $\frac1\pi\int_0^{2\pi}q^2\,\mathrm{d} x=2=\sum_{k\text{ ungerade}}\frac{16}{\pi^2k^2}$ gibt $\sum_{k\text{ ungerade}}\frac1{k^2}=\frac{\pi^2}8$. Die geraden $k$ liefern $\frac14\cdot\frac{\pi^2}6=\frac{\pi^2}{24}$, und $\frac{\pi^2}8+\frac{\pi^2}{24}=\frac{\pi^2}6$. (b) $\frac1\pi\int_{-\pi}^\pi x^2\,\mathrm{d} x=\frac{2\pi^2}3=\frac{\pi^2}2+\sum_{k\text{ ungerade}}\frac{16}{\pi^2k^4}$ gibt $\sum_{k\text{ ungerade}}\frac1{k^4}=\frac{\pi^4}{96}$. Sei $Z=\sum_{k\ge1}\frac1{k^4}$. Die geraden $k$ liefern $\frac Z{16}$, also $Z=\frac{16}{15}\cdot\frac{\pi^4}{96}=\frac{\pi^4}{90}$.
:::
:::

:::aufgabe Aufgabe 7 ★★★ Parseval für zwei Funktionen
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Leite aus [(6.3)](#gl-6-3) die reelle Form $\frac1\pi\int_0^{2\pi}fg\,\mathrm{d} x=\frac12a_0a_0'+\sum_{n\ge1}(a_na_n'+b_nb_n')$ her und berechne damit $\sum_{k\text{ ungerade}}\frac1{k^2}$ aus $f=q$, $g=s$.

</li>

<li>

Integriere [(4.2)](der-sagezahn-zu-fu.html#gl-4-2) mit dem nun bekannten $C$ von $0$ bis $x$, und bestimme $\sum_{j\ge0}\frac{(-1)^j}{(2j+1)^3}$.

</li>

</ol>

:::loesung
(a) Für reelle $f,g$ ist $c_k\overline{d_k}+c_{-k}\overline{d_{-k}}=\frac12(a_ka_k'+b_kb_k')$, und der Summand zu $k=0$ ist $\frac14a_0a_0'$. Multiplikation von [(6.3)](#gl-6-3) mit 2 gibt die Form. Es ist $\int_0^{2\pi}qs\,\mathrm{d} x=\int_0^\pi\frac{\pi-x}2\,\mathrm{d} x-\int_\pi^{2\pi}\frac{\pi-x}2\,\mathrm{d} x=\frac{\pi^2}2$, also $\frac\pi2=\sum_{k\text{ ungerade}}\frac4{\pi k}\cdot\frac1k$ und damit wieder $\frac{\pi^2}8$. (b) Die gleichmäßige Konvergenz erlaubt gliedweises Integrieren:

$$\sum_{k\ge1}\frac{\sin kx}{k^3}=\int_0^x\Bigl(\frac{(\pi-y)^2}4-\frac{\pi^2}{12}\Bigr)\,\mathrm{d} y=\frac{\pi^3-(\pi-x)^3-\pi^2x}{12}.$$

Bei $x=\frac\pi2$ ist die linke Seite die gesuchte Reihe, die rechte $\frac{\pi^3}{12}(1-\frac18-\frac12)=\frac{\pi^3}{32}$.
:::
:::
