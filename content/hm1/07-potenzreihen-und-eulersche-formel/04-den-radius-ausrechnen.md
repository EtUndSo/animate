---
title: Stufe 2: Den Radius ausrechnen
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1270400
summary: Stufe 1 sagt nicht, wie groß der Radius ist.
tags: Häufungspunkt, Teilfolge, Limes superior
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Stufe [1](der-konvergenzkreis.html#stufe-1) sagt nicht, wie groß der Radius ist. Diese Stufe liest ihn aus den Koeffizienten ab und zeigt, dass eine Potenzreihe im Inneren stetig ist.
:::

**Die Idee.** Ändert sich $|a_n|$ für große $n$ in jedem Schritt etwa um den Faktor $A$, verhält sich $|a_nx^n|$ wie eine geometrische Folge mit dem Faktor $A|x|$. Die Reihe konvergiert also, wenn $A|x|<1$ ist, und das heißt $|x|<1/A$.

:::satz Satz 2.1 (Quotientenkriterium und Wurzelkriterium für Potenzreihen)
<span class="anker" id="satz-2-1"></span>

Sei $\sum a_nx^n$ eine Potenzreihe. Man setzt $1/\infty:=0$ und $1/0:=\infty$.

<ol class="rm">

<li>

Sei $a_n\ne0$ für alle $n\ge n_0$ und $A:=\lim_{n\to\infty}\bigl|\frac{a_{n+1}}{a_n}\bigr|$. Dann ist $R=\frac1A$.

</li>

<li>

Sei $B:=\lim_{n\to\infty}\sqrt[n]{|a_n|}$. Dann ist $R=\frac1B$.

</li>

</ol>
:::

⁠**So liest man das:** $A$ und $B$ messen, wie schnell die Koeffizienten geometrisch wachsen. $A=0$ heißt: Sie fallen schneller als jede geometrische Folge, und $R=\infty$. $A=\infty$ ergibt $R=0$. **Gültigkeit:** Der Grenzwert muss existieren, und bei (i) darf ab $n_0$ kein Koeffizient null sein, sonst steht eine Division durch 0 da.

:::beweis Rückführung auf die Kriterien für Reihen
(i) Sei $x\ne0$ und $b_n:=a_nx^n$. Dann ist $|b_{n+1}/b_n|=|x|\,|a_{n+1}/a_n|\to|x|A=:\alpha$. Nach dem Quotientenkriterium ist die Reihe für $\alpha<1$, also $|x|<1/A$, absolut konvergent und für $\alpha>1$, also $|x|>1/A$, divergent. Das heißt $R=1/A$. Für $A=0$ ist $\alpha=0$ bei jedem $x$. Für $A=\infty$ wachsen die Quotienten bei jedem $x\ne0$ über 1, die Glieder sind keine Nullfolge.

(ii) Ebenso mit $\sqrt[n]{|b_n|}=|x|\sqrt[n]{|a_n|}\to|x|B$.
:::

::::beispiel
Für $f$ ist $a_n=\frac1{n2^n}$, also

$$\Bigl|\frac{a_{n+1}}{a_n}\Bigr|=\frac{n\,2^n}{(n+1)\,2^{n+1}}=\frac n{2(n+1)}\to\frac12\quad\Rightarrow\quad R=2,$$

wie in Stufe [1](der-konvergenzkreis.html#stufe-1), bei $n=100$ ist der Quotient schon $0{,}495$. Die Wurzel gibt dasselbe, $\sqrt[n]{|a_n|}=\frac1{2\sqrt[n]{n}}\to\frac12$ ([Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)), aber langsamer: $0{,}477$ bei $n=100$.
::::

**Wenn der Grenzwert fehlt.** Bei $g$ ist $a_{2n}=4^{-n}$ und $a_{2n+1}=0$. Der Quotient ist nicht erklärt, und $\sqrt[n]{|a_n|}$ springt zwischen $\frac12$ und $0$ (Abb. [2](#abb-2)). Trotzdem hat $g$ einen Radius: Mit $y=x^2$ ist $g$ die geometrische Reihe $\sum(y/4)^n$, sie konvergiert für $|y|<4$, also für $|x|<2$.

:::abbildung hm1/k7limsup 2
Die Werte $\sqrt[n]{|a_n|}$. Links nähert sich $f$ der Grenze $\frac12$. Rechts springt $g$ zwischen 0 und $\frac12$: Es gibt keinen Grenzwert, aber zwei Häufungspunkte, und der größere bestimmt den Radius.
:::

Aus [Teil 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html): Ein __Häufungspunkt__ von $\{c_n\}$ ist ein Wert, gegen den eine __Teilfolge__ konvergiert (eine Auswahl unendlich vieler Glieder in der alten Reihenfolge). Der __Limes superior__ $\limsup_{n\to\infty}c_n$ ist der größte Häufungspunkt, für nach oben unbeschränkte Folgen $\infty$. Jede beschränkte Folge hat einen (Bolzano-Weierstraß).

:::satz Satz 2.2 (Wurzelkriterium, allgemeine Form)
<span class="anker" id="satz-2-2"></span>

Für jede Potenzreihe gilt mit $B:=\limsup_{n\to\infty}\sqrt[n]{|a_n|}$: $R=\frac1B$.
:::

⁠**So liest man das:** Diese Form gilt immer, bei einer konvergenten Folge ist $B$ ihr Grenzwert. Bei $g$ ist $B=\frac12$ und $R=2$.

:::beweis Wie beim Wurzelkriterium
Sei $x\ne0$ und $|x|B<1$. Wähle $q$ mit $|x|B<q<1$. Nur endlich viele $n$ haben $\sqrt[n]{|a_n|}>q/|x|$, denn sonst hätten diese Glieder nach Bolzano-Weierstraß einen Häufungspunkt größer als $B$. Ab einer Stelle ist also $|a_nx^n|\le q^n$, die geometrische Reihe ist Majorante. Sei $|x|B>1$. Dann gilt $\sqrt[n]{|a_n|}\,|x|>1$ für unendlich viele $n$, diese Glieder sind größer als 1, also keine Nullfolge.
:::

:::satz Satz 2.3 (Stetigkeit von Potenzreihen)
<span class="anker" id="satz-2-3"></span>

Sei $f(x)=\sum_{n=0}^\infty a_nx^n$ eine Potenzreihe mit Konvergenzradius $R>0$. Dann ist $f:(-R,R)\to\mathbb{R}$ stetig.
:::

⁠**So liest man das:** Eine Potenzreihe springt im Inneren nirgends. **Warum das nicht von selbst gilt:** Die Teilsummen von $\sum_{n=0}^\infty(1-x)x^n$ sind die stetigen Funktionen $1-x^{N+1}$, ihr Grenzwert springt aber: 1 für $0\le x<1$, 0 für $x=1$. Bei Potenzreihen lassen sich die Reste für alle $x$ gemeinsam abschätzen.

:::beweis Polynom plus kleiner Rest
Seien $\varepsilon>0$ und $|x_0|<R$. Wähle $y_0$ mit $|x_0|<y_0<R$. Bei $y_0$ konvergiert die Reihe absolut, es gibt also $N_0$ mit $\sum_{n>N_0}|a_n|y_0^n<\frac\varepsilon4$. Für alle $y$ mit $|y|\le y_0$ folgt

$$\Bigl|\sum_{n>N_0}a_ny^n\Bigr|\le\sum_{n>N_0}|a_n|\,y_0^n<\frac\varepsilon4.$$

Das Polynom $P(x):=\sum_{n=0}^{N_0}a_nx^n$ ist stetig. Es gibt also $\delta>0$ mit $|P(x)-P(x_0)|<\frac\varepsilon2$ für $|x-x_0|<\delta$, und $\delta$ darf so klein sein, dass dabei $|x|\le y_0$ bleibt. Für diese $x$ ist

$$|f(x)-f(x_0)|\le|P(x)-P(x_0)|+\Bigl|\sum_{n>N_0}a_nx^n\Bigr|+\Bigl|\sum_{n>N_0}a_nx_0^n\Bigr|<\frac\varepsilon2+\frac\varepsilon4+\frac\varepsilon4=\varepsilon.$$
:::

:::frage Warum entscheidet bei $g$ der größte Häufungspunkt und nicht der Mittelwert?
Glieder mit $a_n=0$ retten nichts. Divergenz entsteht, sobald unendlich viele Glieder groß bleiben, und das entscheiden die größten Koeffizienten.
:::

:::aufgabe Aufgabe 2 ★★ Radien berechnen
<span class="anker" id="aufg-2"></span>

Bestimme $R$: (a) $\sum_{n=1}^\infty n^2\,3^{-n}x^n$, (b) $\sum_{n=1}^\infty\frac{n!}{(2n)^n}x^n$, (c) $\sum_{n=0}^\infty(2+(-1)^n)^nx^n$. Warum versagen bei (c) beide Formen aus dem ersten Satz dieser Stufe?

:::loesung
(a) $\bigl|\frac{a_{n+1}}{a_n}\bigr|=\frac{(n+1)^2}{3n^2}\to\frac13$, also $R=3$. (b) $\bigl|\frac{a_{n+1}}{a_n}\bigr|=\frac{(n+1)!}{n!}\cdot\frac{(2n)^n}{(2n+2)^{n+1}}=\frac{n+1}{2n+2}\Bigl(\frac n{n+1}\Bigr)^n=\frac12\cdot\frac1{(1+\frac1n)^n}\to\frac1{2\mathrm{e}}$, also $R=2\mathrm{e}\approx5{,}44$. (c) $\sqrt[n]{|a_n|}=2+(-1)^n$ ist 3 für gerade und 1 für ungerade $n$. Die Häufungspunkte sind 1 und 3, also $B=3$ und $R=\frac13$. Die Wurzel hat keinen Grenzwert, der Quotient auch nicht: Er ist $3^{n+1}$ für ungerade und $3^{-n}$ für gerade $n$.
:::
:::
