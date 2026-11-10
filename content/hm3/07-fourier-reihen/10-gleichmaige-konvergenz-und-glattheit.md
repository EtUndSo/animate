---
title: Stufe 9: Gleichmäßige Konvergenz und Glattheit
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Fourier-Reihen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/fourier-reihen
knoten: Kapitel 7: Fourier-Reihen
order: 3171000
summary: Wann konvergiert die Reihe überall gleich schnell, und was verraten die Koeffizienten über die Glattheit?
tags: 
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Wann konvergiert die Reihe überall gleich schnell, und was verraten die Koeffizienten über die Glattheit? Beides hilft bei Differentialgleichungen.
:::

**Die Idee.** Es ist $|c_k\mathrm{e}^{\mathrm{i}kx}|=|c_k|$. Ist $\sum_k|c_k|$ endlich, greift der M-Test, und die Konvergenz ist gleichmäßig. Jede Ableitung bringt einen Faktor $\mathrm{i}k$. Je schneller die $c_k$ fallen, desto öfter darf man also gliedweise ableiten. Ein Sprung verhindert gleichmäßige Konvergenz: Der Abstand zwischen $T_Nq$ und $q$ bleibt dicht neben dem Sprung immer 1, weil $T_Nq(0)=0$ ist und $T_Nq$ stetig.

:::satz Satz 9.1 (Gleichmäßige Konvergenz)
<span class="anker" id="satz-9-1"></span>

Sei $f$ $2\pi$-periodisch, stetig und stückweise stetig differenzierbar. Dann konvergieren die Fourier-Polynome $T_Nf$ gleichmäßig gegen $f$.
:::

:::beweis Summierbare Koeffizienten
Seien $d_k$ die Koeffizienten von $f'$. Nach der Bemerkung zu Satz [3.1](rechenregeln.html#satz-3-1) (vi) ist $d_k=\mathrm{i}k\,c_k$. Für $k\neq0$ gibt $ab\le\frac12(a^2+b^2)$

$$|c_k|=|d_k|\cdot\frac1{|k|}\le\frac12\Bigl(|d_k|^2+\frac1{k^2}\Bigr).$$

Nach der Besselschen Ungleichung für $f'$ ist $\sum|d_k|^2$ endlich, und $\sum\frac1{k^2}$ ist es auch. Also ist $\sum_k|c_k|<\infty$. Der M-Test gibt gleichmäßige Konvergenz von $T_Nf$, und der Grenzwert ist nach Satz [8.3](punktweise-konvergenz.html#satz-8-3) gleich $f$.
:::

⁠**So liest man das:** Ein Knick schadet nicht, ein Sprung schon. Hat $f$ Sprünge, zeigt der Beweis von Satz [8.3](punktweise-konvergenz.html#satz-8-3) noch etwas: Auf abgeschlossenen Intervallen ohne Sprungstelle geht $I_N=I_N(x)$ gleichmäßig gegen null. Der Sägezahn zeigt das.

:::satz Satz 9.2 (Glattheit aus den Koeffizienten)
<span class="anker" id="satz-9-2"></span>

Sei $(c_k)_{k\in\mathbb{Z}}$ eine Folge komplexer Zahlen.

<ol class="rm">

<li>

Ist $\sum_{k\in\mathbb{Z}}|c_k|<\infty$, konvergiert die Reihe gleichmäßig, und $f(x):=\sum_{k\in\mathbb{Z}}c_k\mathrm{e}^{\mathrm{i}kx}$ ist stetig.

</li>

<li>

Ist $\sum_{k\in\mathbb{Z}}|k|^m|c_k|<\infty$, konvergieren auch die Reihen der Ableitungen bis zur Ordnung $m$ gleichmäßig, $f$ ist $m$-mal stetig differenzierbar, und für $1\le\ell\le m$ gilt

<span class="anker" id="gl-9-1"></span>
$$\frac{\mathrm{d}^\ell}{\mathrm{d} x^\ell}f(x)=\sum_{k\in\mathbb{Z}}(\mathrm{i}k)^\ell c_k\,\mathrm{e}^{\mathrm{i}kx}. \tag{9.1}$$

</li>

</ol>
:::

:::beweis Glattheit aus den Koeffizienten
(i) M-Test mit $M_k=|c_k|$. Der gleichmäßige Grenzwert stetiger Funktionen ist stetig ([Kapitel 6](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen/konvergenz-von-funktionenfolgen.html)). (ii) Die $\ell$-te Ableitung des Summanden hat den Betrag $|k|^\ell|c_k|\le|k|^m|c_k|$ für $k\neq0$. Der M-Test gibt gleichmäßige Konvergenz aller abgeleiteten Reihen, und nach dem Satz über gliedweises Ableiten ([Kapitel 6](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen/konvergenz-von-funktionenfolgen.html)) ist [(9.1)](#gl-9-1) richtig.
:::

⁠**So liest man das:** Wegen der gleichmäßigen Konvergenz darf man in $\langle f,\hat{\boldsymbol{e}}_k\rangle$ Summe und Integral tauschen. Die $c_k$ sind also wirklich die Fourier-Koeffizienten von $f$. Die Voraussetzungen sind hinreichend, nicht notwendig. Beim Dreieck ist $|c_k|=\frac2{\pi k^2}$ für ungerades $k$: (i) greift, also ist $w$ stetig. Für $m=1$ divergiert die Summe, und tatsächlich hat $w$ Knicke. Beim Rechteck divergiert schon $\sum|c_k|$, und $q$ springt.

::::beispiel eine periodische Differentialgleichung
Gesucht ist die $2\pi$-periodische Lösung von $u''+\frac14u=w$. Setzt man $u=\sum_ku_k\mathrm{e}^{\mathrm{i}kx}$ ein, gibt jeder Baustein für sich die Gleichung $(\frac14-k^2)\,u_k=c_k(w)$. Eine Differentialgleichung wird so zu unendlich vielen Divisionen. Mit [(3.1)](rechenregeln.html#gl-3-1) folgt

$$u(x)=2\pi+\frac{16}\pi\sum_{k\text{ ungerade}}\frac{\cos kx}{k^2(4k^2-1)}.$$

Der erste Term ist $c_0(w)/\frac14$, der Faktor bei $\cos x$ ist $\frac{16}{3\pi}\approx1{,}70$. Wegen $|u_k|\sim1/k^4$ ist $\sum k^2|u_k|<\infty$. Nach Satz [9.2](#satz-9-2) ist $u$ zweimal stetig differenzierbar, und das gliedweise Ableiten beim Einsetzen war erlaubt. In der Elektrotechnik ist das die Zeigerrechnung, angewandt auf jede Frequenz $k$.
::::

⁠**Grenzfall:** Steht statt $\frac14$ eine Zahl $\mu^2$ mit $\mu\in\mathbb{N}$, ist der Faktor $\mu^2-k^2$ bei $k=\pm\mu$ null, und für $c_\mu(w)\neq0$ gibt es keine periodische Lösung. Das ist Resonanz. Abb. [9](#abb-9) zeigt rechts die Lösung, links den Unterschied zwischen stetig und springend.

:::abbildung hm3/k7glatt 9
Links: Der größte Abstand zwischen $f$ und $T_Nf$. Für das stetige Dreieck $w$ fällt er gegen null, für das springende Rechteck $q$ bleibt er 1. Rechts: Die periodische Lösung $u$ von $u''+\frac14u=w$. Die Antwort läuft der Anregung entgegen, weil der Faktor $\frac14-k^2$ für $k\ge1$ negativ ist.
:::

:::aufgabe Aufgabe 11 ★★ Ablesen und lösen
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Wie oft ist $f=\sum_kc_k\mathrm{e}^{\mathrm{i}kx}$ nach Satz [9.2](#satz-9-2) sicher stetig differenzierbar für $c_k=\frac1{1+k^4}$ und für $c_k=2^{-|k|}$?

</li>

<li>

Bestimme die $2\pi$-periodische Lösung von $u''+2u'+5u=10\cos2x$ mit Fourier-Koeffizienten.

</li>

<li>

Sei nun die rechte Seite $q$. Welches $m$ liefert Satz [9.2](#satz-9-2) für die Lösung, und warum kann es nicht größer sein?

</li>

</ol>

:::loesung
(a) $\sum|k|^m\frac1{1+k^4}$ konvergiert genau für $m<3$, also sicher zweimal stetig differenzierbar. $\sum|k|^m2^{-|k|}$ konvergiert für jedes $m$, also beliebig oft. (b) Baustein für Baustein: $(5-k^2+2\mathrm{i}k)\,u_k=c_k$ mit $c_{\pm2}=5$, sonst 0. Also $u_2=\frac5{1+4\mathrm{i}}=\frac5{17}(1-4\mathrm{i})$, $u_{-2}=\overline{u_2}$, und

$$u(x)=2\operatorname{Re}\bigl(u_2\mathrm{e}^{2\mathrm{i}x}\bigr)=\frac{10}{17}\bigl(\cos2x+4\sin2x\bigr).$$

Der Faktor $5-k^2+2\mathrm{i}k$ ist für kein $k\in\mathbb{Z}$ null, also gibt es keine weitere periodische Lösung. (c) $|u_k|=\frac{|c_k(q)|}{|5-k^2+2\mathrm{i}k|}\sim\frac2{\pi|k|^3}$. Die Summe $\sum|k|^m|u_k|$ konvergiert für $m=1$, nicht für $m=2$, also $m=1$. Mehr geht nicht: Aus $u''=q-2u'-5u$ folgt, dass $u''$ dort springt, wo $q$ springt.
:::
:::
