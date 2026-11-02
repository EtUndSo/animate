---
title: Stufe 8: Punktweise Konvergenz
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3170900
summary: Konvergiert T Nf(x) an einer festen Stelle x , und gegen welchen Wert?
tags: Dirichlet-Kern, periodische Faltung, stückweise stetig differenzierbar
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Konvergiert $T_Nf(x)$ an einer festen Stelle $x$, und gegen welchen Wert? Stufe [6](konvergenz-im-quadratischen-mittel.html#stufe-6) sagt dazu nichts. Diese Stufe gibt die Antwort für stückweise glatte Funktionen.
:::

**Die Idee.** Setzt man die $c_k$ in $T_Nf$ ein, wird das Fourier-Polynom selbst ein gewichteter Mittelwert von $f$:

<span class="anker" id="gl-8-1"></span>
$$T_Nf(x)=\sum_{|k|\le N}\Bigl(\frac1{2\pi}\int_0^{2\pi}f(y)\,\mathrm{e}^{-\mathrm{i}ky}\,\mathrm{d} y\Bigr)\mathrm{e}^{\mathrm{i}kx}=\frac1{2\pi}\int_0^{2\pi}D_N(x-y)\,f(y)\,\mathrm{d} y \tag{8.1}$$

mit dem __Dirichlet-Kern__ $D_N(x):=\sum_{|k|\le N}\mathrm{e}^{\mathrm{i}kx}$. Für $2\pi$-periodische Funktionen heißt $(f\circledast g)(x):=\frac1{2\pi}\int_0^{2\pi}f(x-y)\,g(y)\,\mathrm{d} y$ die __periodische Faltung__, und [(8.1)](#gl-8-1) lautet $T_Nf=D_N\circledast f$. Spielt $D_N$ die Rolle einer Dirac-Schar? Nur zum Teil: $D_N$ hat eine schmale, hohe Spitze, aber es wird auch negativ, und seine Seitenschwingungen klingen nicht ab (Abb. [8](#abb-8)).

:::abbildung hm3/k7dirichlet 8
Links: Dirichlet-Kerne. Die Spitze hat die Höhe $2N+1$ und wird schmaler, aber die Seitenschwingungen behalten ihre Größe und werden nur dichter. Rechts: Am Sprung von $q$ laufen alle Fourier-Polynome durch den Mittelwert $0$ der beiden Seiten.
:::

:::satz Satz 8.1 (Dirichlet-Kern)
<span class="anker" id="satz-8-1"></span>

Für $N\in\mathbb{N}$ ist $D_N:\mathbb{R}\to\mathbb{R}$ gerade, $2\pi$-periodisch und stetig mit $D_N(0)=2N+1$ und $D_N(x)=\sin\bigl((N+\frac12)x\bigr)/\sin\frac x2$ für $x\in(0,2\pi)$. Ferner gilt

<ol class="rm">

<li>

$\frac1{2\pi}\int_0^{2\pi}D_N(x)\,\mathrm{d} x=1$,

</li>

<li>

$T_Nf(x)=\frac1{2\pi}\int_0^{2\pi}D_N(y)\,f(x\pm y)\,\mathrm{d} y$.

</li>

</ol>
:::

:::beweis Dirichlet-Kern
Die Formel ist [(4.1)](der-sagezahn-zu-fu.html#gl-4-1), und bei $x=0$ zählt die Definition $2N+1$ Einsen. Ersetzt man $k$ durch $-k$, wird $D_N(-x)=D_N(x)$, und zusammen ist $D_N=1+2\sum_{k=1}^N\cos kx$ reell und stetig. (i) Bei der Integration überlebt nur $k=0$. (ii) In [(8.1)](#gl-8-1) substituiert man $y=x-z$ und benutzt die Periodizität: Das gibt das Vorzeichen $-$. Weil $D_N$ gerade ist, gibt $y=x+z$ das Vorzeichen $+$.
:::

⁠**So liest man das:** (i) ist die Fläche 1 einer Dirac-Schar, (ii) das Mitteln um die Stelle $x$. Bei einer Dirac-Schar ist die Fläche aber zugleich die Fläche des Betrags, das benutzt die Abschätzung [(7.1)](mitteln-mit-dirac-scharen.html#gl-7-1). Hier gilt dagegen

<span class="anker" id="gl-8-2"></span>
$$\int_0^{2\pi}|D_N(x)|\,\mathrm{d} x\to\infty\qquad\text{für }N\to\infty. \tag{8.2}$$

Denn wegen $\sin\frac x2\le\frac x2$ ist $|D_N(x)|\ge\frac2x|\sin((N+\frac12)x)|$ auf $(0,\pi)$, und $u=(N+\frac12)x$ gibt die untere Schranke $2\int_0^{(N+1/2)\pi}\frac{|\sin u|}u\,\mathrm{d} u$, die wie die harmonische Reihe wächst. Deshalb reicht Stetigkeit von $f$ für diesen Weg nicht, man braucht mehr. Fourier selbst behauptete, jede stetige periodische Funktion werde punktweise dargestellt. Du Bois-Reymond widerlegte das mit einem Gegenbeispiel. Eine Lipschitz-Bedingung $|f(x)-f(y)|\le c\,|x-y|$ reicht dagegen aus, ebenso die folgende Bedingung.

:::definition Definition 8.2 (Stückweise stetig differenzierbar)
<span class="anker" id="satz-8-2"></span>

Eine $2\pi$-periodische Funktion heißt __stückweise stetig differenzierbar__, wenn sich $[0,2\pi]$ in endlich viele Intervalle zerlegen lässt, in deren Innerem $f$ stetig differenzierbar ist und an deren Enden $f$ und $f'$ einseitige Grenzwerte haben. In jedem Punkt existieren dann

$$f(x^\pm)=\lim_{h\searrow0}f(x\pm h),$$

$$f'(x^+)=\lim_{y\searrow0}\frac{f(x+y)-f(x^+)}y,\qquad f'(x^-)=\lim_{y\searrow0}\frac{f(x^-)-f(x-y)}y.$$
:::

:::satz Satz 8.3 (Punktweise Konvergenz)
<span class="anker" id="satz-8-3"></span>

Sei $f$ $2\pi$-periodisch und stückweise stetig differenzierbar. Dann gilt für alle $x\in\mathbb{R}$

<span class="anker" id="gl-8-3"></span>
$$T_Nf(x)\to Tf(x)=\tfrac12\bigl(f(x^+)+f(x^-)\bigr)\qquad\text{für }N\to\infty. \tag{8.3}$$
:::

⁠**So liest man das:** Wo $f$ stetig ist, steht rechts $f(x)$. An einem Sprung steht rechts die Mitte zwischen den beiden einseitigen Werten, egal welchen Wert $f$ dort selbst hat.

:::beweis Der Fehler ist ein Fourier-Koeffizient
⁠**Schritt 1: symmetrisieren.** Das Mittel der beiden Formeln (ii) ist $T_Nf(x)=\frac1{2\pi}\int_0^{2\pi}\frac{f(x+y)+f(x-y)}2D_N(y)\,\mathrm{d} y$.

⁠**Schritt 2: Ziel abziehen.** Mit (i) schreibt man $\frac12(f(x^+)+f(x^-))$ als Integral und erhält für die Differenz $I_N:=T_Nf(x)-\frac12(f(x^+)+f(x^-))$

$$I_N=\frac1{2\pi}\int_0^{2\pi}\frac{f(x+y)-f(x^+)+f(x-y)-f(x^-)}2\,D_N(y)\,\mathrm{d} y.$$

⁠**Schritt 3: Kern einsetzen.** Für festes $x$ ist also $I_N=\frac1{2\pi}\int_0^{2\pi}h(y)\sin\bigl((N+\frac12)y\bigr)\,\mathrm{d} y$ mit

$$h(y)=\frac{f(x+y)-f(x^+)+f(x-y)-f(x^-)}{2\sin\frac y2}.$$

⁠**Schritt 4: $h$ ist harmlos.** Für kleine $y$ ist $2\sin\frac y2\approx y$, also existiert $\lim_{y\searrow0}h(y)=f'(x^+)-f'(x^-)$. Hier geht die Differenzierbarkeit ein. Wegen der Periodizität gilt $h(2\pi-y)=h(y)$, am oberen Ende ist also alles genauso. Damit ist $h$ stückweise stetig und beschränkt, also Riemann-integrierbar.

⁠**Schritt 5: Riemann-Lebesgue.** Das Additionstheorem $\sin\bigl((N+\frac12)y\bigr)=\cos\frac y2\sin Ny+\sin\frac y2\cos Ny$ gibt

$$I_N=\frac1{2\pi}\int_0^{2\pi}h(y)\cos\tfrac y2\,\sin Ny\,\mathrm{d} y+\frac1{2\pi}\int_0^{2\pi}h(y)\sin\tfrac y2\,\cos Ny\,\mathrm{d} y.$$

Das sind, bis auf den Faktor $\frac12$, die Koeffizienten $b_N$ von $h\cos\frac y2$ und $a_N$ von $h\sin\frac y2$, beide periodisch fortgesetzt. Beide Funktionen sind Riemann-integrierbar, also gehen die Koeffizienten nach [(5.3)](die-beste-naherung.html#gl-5-3) gegen null.
:::

**Beispiele.** Für das Rechteck ist $T_Nq(0)=0=\frac12(1+(-1))$ für alle $N$, und bei $x=\frac\pi2$ folgt $\frac4\pi(1-\frac13+\frac15-\dots)=1$. Der Sägezahn ist der Prototyp: In den glatten Bereichen konvergiert die Reihe gleichmäßig, an den Sprüngen punktweise gegen den Mittelwert.

:::zusatz Gibbs-Phänomen
Die erste Spitze neben einem Sprung bleibt für große $N$ bei rund $9\,\%$ der Sprunghöhe und rückt nur näher an den Sprung. An jeder festen Stelle zieht sie vorbei, das verträgt sich also mit [(8.3)](#gl-8-3).
:::

:::aufgabe Aufgabe 9 ★★★ Exponentialfunktion mit Sprung
<span class="anker" id="aufg-9"></span>

Sei $f$ $2\pi$-periodisch mit $f(x)=\mathrm{e}^x$ auf $(-\pi,\pi)$ und $f(\pi)=0$.

<ol class="al">

<li>

Zeige $c_k=(-1)^k\frac{\sinh\pi}{\pi(1-\mathrm{i}k)}$.

</li>

<li>

Gegen welche Werte konvergiert $T_Nf$ bei $x=0$ und bei $x=\pi$?

</li>

<li>

Folgere aus dem Wert bei $x=\pi$ die Summe $\sum_{k\in\mathbb{Z}}\frac1{1+k^2}$.

</li>

</ol>

:::loesung
(a) Mit $x_0=-\pi$: $c_k=\frac1{2\pi}\int_{-\pi}^\pi\mathrm{e}^{(1-\mathrm{i}k)x}\,\mathrm{d} x=\frac{\mathrm{e}^{(1-\mathrm{i}k)\pi}-\mathrm{e}^{-(1-\mathrm{i}k)\pi}}{2\pi(1-\mathrm{i}k)}=\frac{(-1)^k(\mathrm{e}^\pi-\mathrm{e}^{-\pi})}{2\pi(1-\mathrm{i}k)}$. (b) Bei $x=0$ ist $f$ stetig, der Grenzwert ist $1$. Bei $x=\pi$ springt $f$, der Grenzwert ist $\frac12(\mathrm{e}^{-\pi}+\mathrm{e}^\pi)=\cosh\pi$. Der Funktionswert $f(\pi)=0$ spielt keine Rolle. (c) Bei $x=\pi$ ist $\mathrm{e}^{\mathrm{i}k\pi}=(-1)^k$, also $\cosh\pi=\lim_{N\to\infty}\frac{\sinh\pi}\pi\sum_{|k|\le N}\frac1{1-\mathrm{i}k}=\lim_{N\to\infty}\frac{\sinh\pi}\pi\sum_{|k|\le N}\frac{1+\mathrm{i}k}{1+k^2}$. Die Imaginärteile heben sich paarweise auf. Es folgt $\sum_{k\in\mathbb{Z}}\frac1{1+k^2}=\pi\coth\pi\approx3{,}153$.
:::
:::

:::aufgabe Aufgabe 10 ★★ Faltung und Koeffizienten
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Zeige für stückweise stetige $2\pi$-periodische $f,g$ mit Koeffizienten $c_k$ und $d_k$: $f\circledast g$ hat die Koeffizienten $c_kd_k$.

</li>

<li>

Berechne daraus die Koeffizienten von $q\circledast q$ und zeige durch Vergleich, dass $q\circledast q$ und $\frac2\pi w-1$ dieselben Koeffizienten haben. Prüfe bei $x=0$ direkt.

</li>

</ol>

:::loesung
(a) Integrale tauschen und $z=x-y$ substituieren, dabei ist $\mathrm{e}^{-\mathrm{i}kx}=\mathrm{e}^{-\mathrm{i}kz}\mathrm{e}^{-\mathrm{i}ky}$:

$$\frac1{2\pi}\int_0^{2\pi}(f\circledast g)(x)\,\mathrm{e}^{-\mathrm{i}kx}\,\mathrm{d} x=\frac1{2\pi}\int_0^{2\pi}g(y)\,\mathrm{e}^{-\mathrm{i}ky}\Bigl(\frac1{2\pi}\int_0^{2\pi}f(z)\,\mathrm{e}^{-\mathrm{i}kz}\,\mathrm{d} z\Bigr)\mathrm{d} y=c_kd_k.$$

Für stückweise stetige Funktionen ist das Vertauschen erlaubt. (b) Für ungerades $k$ ist $c_k(q)^2=\bigl(-\frac{2\mathrm{i}}{\pi k}\bigr)^2=-\frac4{\pi^2k^2}$, sonst 0. Für $\frac2\pi w-1$ gibt es für ungerades $k$ ebenfalls $\frac2\pi\cdot\bigl(-\frac2{\pi k^2}\bigr)=-\frac4{\pi^2k^2}$, für gerades $k\neq0$ den Wert 0, und $c_0=\frac2\pi\cdot\frac\pi2-1=0$. Bei $x=0$: $\frac1{2\pi}\int_0^{2\pi}q(-y)\,q(y)\,\mathrm{d} y=-1$, denn $q$ ist ungerade, und $\frac2\pi w(0)-1=-1$.
:::
:::
