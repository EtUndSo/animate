---
title: Stufe 6: Potenzreihen
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen
knoten: Kapitel 6: Konvergenz von Funktionenfolgen
order: 3160800
summary: Diese Stufe bestimmt, wo Potenzreihen konvergieren, und zeigt, warum sie dort stetig sind und gliedweise abgeleitet werden dürfen.
tags: Potenzreihe, Koeffizienten, Entwicklungspunkt, Konvergenzradius, Formel von Cauchy-Hadamard, Limes superior, Konvergenzkreis, formale Ableitung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Diese Stufe bestimmt, wo Potenzreihen konvergieren, und zeigt, warum sie dort stetig sind und gliedweise abgeleitet werden dürfen.
:::

**Die Idee.** Eine __Potenzreihe__ ist $\sum_{k=0}^\infty c_k(x-x_0)^k$ mit __Koeffizienten__ $c_k$ und __Entwicklungspunkt__ $x_0$. Ihre Partialsummen sind Polynome. Jedes Glied enthält den geometrischen Faktor $(x-x_0)^k$, und je weiter $x$ von $x_0$ entfernt ist, desto stärker wächst er. Deshalb gibt es eine scharfe Grenze: Innerhalb eines Abstands konvergiert die Reihe, außerhalb nicht.

:::definition Definition 6.1 (Konvergenzradius)
<span class="anker" id="satz-6-1"></span>

Der __Konvergenzradius__ von $\sum_{k=0}^\infty c_k(x-x_0)^k$ ist

<span class="anker" id="gl-6-1"></span>
$$R:=\sup\Bigl\{|y|:\sum_{k=0}^\infty c_ky^k\text{ konvergiert}\Bigr\}, \tag{6.1}$$

wobei $R=\infty$ erlaubt ist.
:::

:::satz Satz 6.2 (Konvergenzbereich)
<span class="anker" id="satz-6-2"></span>

Für $|x-x_0|<R$ konvergiert die Potenzreihe absolut, für $|x-x_0|>R$ divergiert sie, die Ränder $|x-x_0|=R$ sind gesondert zu prüfen. Außerdem gilt

<span class="anker" id="gl-6-2"></span>
$$R=\sup\Bigl\{r>0:\sum_{k=0}^\infty|c_k|\,r^k\text{ konvergiert}\Bigr\} \tag{6.2}$$

und die __Formel von Cauchy-Hadamard__

<span class="anker" id="gl-6-3"></span>
$$R=\frac{1}{\limsup\limits_{k\to\infty}\sqrt[k]{|c_k|}}, \tag{6.3}$$

mit $1/0=\infty$ und $1/\infty=0$ (leere Menge in [(6.2)](#gl-6-2): $R=0$).
:::

⁠**So liest man das:** Der __Limes superior__ $\limsup_{k\to\infty}s_k:=\lim_{k\to\infty}\sup_{j\ge k}s_j$ ist der größte Wert, dem eine Folge immer wieder beliebig nahe kommt. Er existiert auch für Folgen, die nicht konvergieren. Bei $\sum_k(2+(-1)^k)^kx^k$ ist $\sqrt[k]{|c_k|}$ abwechselnd $1$ und $3$, also $\limsup=3$ und $R=\frac13$.

:::herleitung Konvergenzbereich
Konvergiert $\sum_kc_ky^k$, sind die Glieder eine Nullfolge, also $|c_ky^k|\le C$ für eine Zahl $C$. Für $0<r<|y|$ folgt $|c_k|\,r^k\le C\,(r/|y|)^k$, und das ist eine konvergente geometrische Reihe. Das gibt die absolute Konvergenz für $|x-x_0|<R$. Umgekehrt konvergiert die Reihe bei $y=r$, wenn $\sum_k|c_k|\,r^k$ konvergiert, also gilt [(6.2)](#gl-6-2). Für $|x-x_0|>R$ divergiert die Reihe nach [(6.1)](#gl-6-1).

Für [(6.3)](#gl-6-3) sei $L$ der Limes superior. Ist $rL<1$, gibt es ein $q<1$ mit $|c_k|\,r^k<q^k$ für alle großen $k$, die Reihe konvergiert also. Ist $rL>1$, gilt $|c_k|\,r^k>1$ für unendlich viele $k$. Die Glieder streben dann nicht gegen null.
:::

| Reihe | $R$ | bei $x=1$ | bei $x=-1$ |
|---|---|---|---|
| $\sum x^k$ | $1$ | divergiert | divergiert |
| $\sum x^k/k$ | $1$ | divergiert | konvergiert |
| $\sum x^k/k^2$ | $1$ | konvergiert | konvergiert |

Gleicher Radius, verschiedenes Verhalten am Rand: $R$ sagt über den Rand nichts. Die Extreme sind $\sum x^k/k!$ mit $R=\infty$ und $\sum k!\,x^k$ mit $R=0$.

**Komplexe Potenzreihen.** Der Name Radius stammt aus dem Komplexen. Für $\sum_kc_k(z-z_0)^k$ mit $c_k,z,z_0\in\mathbb{C}$ definiert man $R$ wie in [(6.1)](#gl-6-1), mit $y\in\mathbb{C}$. Die Reihe konvergiert im __Konvergenzkreis__ $B_R(z_0)=\{z\in\mathbb{C}:|z-z_0|<R\}$ absolut und divergiert für $|z-z_0|>R$. Am Rand ist keine pauschale Aussage möglich.

:::satz Satz 6.3 (Gleichmäßig im Inneren)
<span class="anker" id="satz-6-3"></span>

Die Potenzreihe habe den Konvergenzradius $R>0$, und sei $0<r<R$. Dann konvergiert

$$f_n(x)=\sum_{k=0}^nc_k(x-x_0)^k$$

gleichmäßig für alle $x$ mit $|x-x_0|\le r$. Folglich konvergiert die Potenzreihe in $|x-x_0|<R$ gegen eine stetige Funktion. Dasselbe gilt für komplexe Potenzreihen in $|z-z_0|<R$.
:::

:::beweis M-Test mit geometrischem Vergleich
Für $|x-x_0|\le r$ ist $|c_k(x-x_0)^k|\le|c_k|\,r^k=:M_k$, und $\sum_kM_k<\infty$ nach [(6.2)](#gl-6-2). Der M-Test gibt die gleichmäßige Konvergenz. Als gleichmäßiger Grenzwert von Polynomen ist die Summe nach Satz [3.1](stetigkeit-und-integral-bleiben-erhalten.html#satz-3-1) stetig in $|x-x_0|\le r$. Jedes $x$ mit $|x-x_0|<R$ liegt in einem solchen Bereich, denn $r$ reicht beliebig nahe an $R$ heran. Für komplexe Reihen ist der Beweis wörtlich gleich.
:::

:::abbildung hm3/k6radius 6
Links der Konvergenzkreis: Die Reihe konvergiert im Kreis mit Radius $R$, gleichmäßig aber nur auf der kleineren Scheibe mit Radius $r<R$. Rechts die Partialsummen $f_2$, $f_5$, $f_{10}$ der geometrischen Reihe gegen $1/(1-x)$: Nahe $x=1$ lösen sie sich von der Summe.
:::

⁠**So liest man das:** Die Bedingung $r<R$ lässt sich nicht weglassen (Abb. [6](#abb-6)). Bei der geometrischen Reihe ist $\frac{1}{1-x}-f_n(x)=\frac{x^{n+1}}{1-x}$. Auf $(-1,1)$ ist das für jedes $n$ unbeschränkt. Auf $|x|\le\frac12$ ist es höchstens $2^{-n}$.

:::satz Satz 6.4 (Potenzreihen gliedweise ableiten)
<span class="anker" id="satz-6-4"></span>

Hat $f(x)=\sum_{k=0}^\infty c_k(x-x_0)^k$ den Konvergenzradius $R>0$, so hat die __formale Ableitung__ $\sum_{k=1}^\infty k\,c_k(x-x_0)^{k-1}$ denselben Konvergenzradius, und in $|x-x_0|<R$ ist $f$ stetig differenzierbar mit

<span class="anker" id="gl-6-4"></span>
$$f'(x)=\frac{\mathrm{d}}{\mathrm{d} x}\Bigl[\sum_{k=0}^\infty c_k(x-x_0)^k\Bigr]=\sum_{k=1}^\infty k\,c_k(x-x_0)^{k-1}. \tag{6.4}$$

Induktiv ist $f$ dort beliebig oft differenzierbar.
:::

:::beweis Radius und Grenzübergang
Ein Faktor $(x-x_0)$ ändert die Konvergenz nicht, man darf also $\sum_kk\,c_k(x-x_0)^k$ betrachten. Wegen $\sqrt[k]{k}\to1$ haben $\sqrt[k]{k|c_k|}$ und $\sqrt[k]{|c_k|}$ denselben Limes superior, und [(6.3)](#gl-6-3) gibt denselben Radius. Sei $0<r<R$. Auf $|x-x_0|\le r$ konvergieren die Polynome $f_n$ punktweise, und ihre Ableitungen sind die Partialsummen der formalen Ableitung. Diese konvergieren nach Satz [6.3](#satz-6-3) gleichmäßig. Satz [4.1](die-ableitung-braucht-mehr.html#satz-4-1) gibt [(6.4)](#gl-6-4). Die rechte Seite ist wieder eine Potenzreihe mit Radius $R$, also wiederholt sich das Argument.
:::

::::beispiel
Die Reihe $f(x)=\sum_{k=1}^\infty x^k/k$ hat $R=1$. Gliedweises Ableiten gibt $f'(x)=\sum_{k=1}^\infty x^{k-1}=\frac{1}{1-x}$. Mit $f(0)=0$ folgt $f(x)=-\ln(1-x)$ für $|x|<1$. Bei $x=\frac12$ ist das $\ln2=\sum_kk^{-1}2^{-k}$. Fünf Glieder geben $0{,}6885$, der Wert ist $0{,}6931$.
::::

⁠**Grenzfall am Rand:** $\sum_kx^k/k^2$ konvergiert nach Stufe [5](funktionenreihen-und-der-m-test.html#stufe-5) noch bei $x=1$, ihre formale Ableitung $\sum_kx^{k-1}/k$ dort nicht. Der Radius ist derselbe, das Verhalten am Rand nicht.

:::aufgabe Aufgabe 7 ★★ Radien umrechnen
<span class="anker" id="aufg-7"></span>

$\sum_kc_kx^k$ habe den Radius $0<R<\infty$. Bestimme den Radius von (a) $\sum_kc_kx^{3k}$, (b) $\sum_k2^kc_kx^k$, (c) $\sum_kc_k^3x^k$. (d) Bestimme den Konvergenzbereich von $\sum_{k\ge1}x^k/(k\,2^k)$ mit Randpunkten.

:::loesung
(a) Mit $y=x^3$ konvergiert die Reihe für $|x|^3<R$ und divergiert für $|x|^3>R$, also $R^{1/3}$. (b) Mit $y=2x$ ergibt sich $R/2$. (c) $\limsup_k\sqrt[k]{|c_k|^3}=(\limsup_k\sqrt[k]{|c_k|})^3=R^{-3}$, also $R^3$. (d) $\sqrt[k]{1/(k2^k)}\to\frac12$, also $R=2$. Bei $x=2$ steht $\sum_k1/k$, das divergiert. Bei $x=-2$ steht $\sum_k(-1)^k/k$, das konvergiert. Der Bereich ist $[-2,2)$.
:::
:::

:::aufgabe Aufgabe 8 ★★ Eine Summe durch Ableiten finden
<span class="anker" id="aufg-8"></span>

Sei $f(x)=\sum_{k=0}^\infty\frac{x^{2k+1}}{2k+1}$.

<ol class="al">

<li>

Bestimme den Konvergenzradius und $f'(x)$.

</li>

<li>

Zeige $f(x)=\frac12\ln\frac{1+x}{1-x}$ für $|x|<1$.

</li>

<li>

Vergleiche $f(\frac13)$ mit der Summe der ersten drei Glieder.

</li>

</ol>

:::loesung
(a) Die Koeffizienten sind $1/j$ für ungerades $j$ und 0 für gerades, der Limes superior ist 1, also $R=1$. Gliedweises Ableiten gibt $f'(x)=\sum_{k\ge0}x^{2k}=1/(1-x^2)$. (b) Die Ableitung von $\frac12\ln\frac{1+x}{1-x}$ ist $\frac12\bigl(\frac1{1+x}+\frac1{1-x}\bigr)=\frac{1}{1-x^2}$, und beide Seiten sind bei $x=0$ null. (c) $f(\frac13)=\frac12\ln2\approx0{,}34657$. Die ersten drei Glieder geben $\frac13+\frac1{81}+\frac1{1215}\approx0{,}34650$.
:::
:::
