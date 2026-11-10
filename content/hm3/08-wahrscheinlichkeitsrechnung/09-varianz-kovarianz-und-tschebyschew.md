---
title: Stufe 8: Varianz, Kovarianz und Tschebyschew
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
adresse: elektrotechnik/3-semester/hohere-mathematik-3/wahrscheinlichkeitsrechnung
knoten: Kapitel 8: Wahrscheinlichkeitsrechnung
order: 3180900
summary: Der Erwartungswert sagt nicht, wie weit X von ihm entfernt liegt.
tags: Varianz, Standardabweichung, Kovarianz, Korrelationskoeffizient
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Der Erwartungswert sagt nicht, wie weit $X$ von ihm entfernt liegt. Diese Stufe misst die Streuung, rechnet sie für Summen aus und schätzt damit große Abweichungen ab.
:::

**Die Idee.** Die Abweichung $X-\mu$ hat den Mittelwert null, weil sich positive und negative Werte aufheben. Ihr Quadrat kann das nicht, sein Mittelwert misst die Breite der Verteilung.

:::definition Definition 8.1 (Varianz)
<span class="anker" id="satz-8-1"></span>

Sei $X$ eine Zufallsvariable, für die $\mathbb{E}(X^2)$ existiert. Dann heißt $\operatorname{Var}(X):=\mathbb{E}\bigl((X-\mathbb{E}(X))^2\bigr)$ __Varianz__ und $\sigma_X=\sqrt{\operatorname{Var}(X)}$ __Standardabweichung__ von $X$.
:::

Ausmultiplizieren mit $\mu=\mathbb{E}(X)$ gibt mit [(7.1)](der-erwartungswert.html#gl-7-1) $\mathbb{E}(X^2)-2\mu^2+\mu^2$, also

<span class="anker" id="gl-8-1"></span>
$$\operatorname{Var}(X)=\mathbb{E}(X^2)-\mathbb{E}(X)^2. \tag{8.1}$$

Dabei ist $\mathbb{E}(X^2)=\sum_iX(\omega_i)^2\,\mathbb{P}(\omega_i)$ im diskreten Fall und $\int_\mathbb{R} x^2f_X(x)\,\mathrm{d} x$ im absolut stetigen Fall nach [(7.3)](der-erwartungswert.html#gl-7-3).

::::beispiel [Beispiele]
$\mathbb{E}(W_1^2)=\frac{30}4$, also $\operatorname{Var}(W_1)=\frac{15}2-\frac{25}4=\frac54$. Die LED hat $\operatorname{Var}(X)=8-4=4$, also $\sigma_X=2$. Die Gleichverteilung auf $[a,b]$ hat $\operatorname{Var}(X)=(b-a)^2/12$.
::::

⁠**Grenzfall:** Für $X\equiv c$ ist die Varianz null.

:::herleitung Poisson und Normalverteilung
Poisson: Mit $k^2=k(k-1)+k$ und $\mathbb{E}(X)=\lambda$ ist

$$\operatorname{Var}(X)=-\lambda^2+\mathrm{e}^{-\lambda}\sum_{k=2}^\infty\lambda^2\frac{\lambda^{k-2}}{(k-2)!}+\mathrm{e}^{-\lambda}\sum_{k=1}^\infty\lambda\frac{\lambda^{k-1}}{(k-1)!}=-\lambda^2+\lambda^2+\lambda=\lambda.$$

Normal: Es ist $x^2=(x-\mu)^2+2\mu(x-\mu)+\mu^2$. Der mittlere Term integriert sich wegen der Punktsymmetrie zu null, der letzte hebt $-\mu^2$ auf. Mit $y=(x-\mu)/\sigma$ bleibt

$$\operatorname{Var}(X)=\frac{\sigma^2}{\sqrt{2\pi}}\int_\mathbb{R} y^2\mathrm{e}^{-y^2/2}\,\mathrm{d} y=\frac{\sigma^2}{\sqrt{2\pi}}\int_\mathbb{R} y\Bigl(-\frac{\mathrm{d}}{\mathrm{d} y}\mathrm{e}^{-y^2/2}\Bigr)\mathrm{d} y=\frac{\sigma^2}{\sqrt{2\pi}}\int_\mathbb{R}\mathrm{e}^{-y^2/2}\,\mathrm{d} y=\sigma^2,$$

wobei die partielle Integration wieder auf das Gauß-Integral führt.
:::

:::satz Satz 8.2 (Varianz von Vielfachen und Summen)
<span class="anker" id="satz-8-2"></span>

Seien $X,Y$ Zufallsvariablen auf demselben Wahrscheinlichkeitsraum, für die $\mathbb{E}(X^2)$ und $\mathbb{E}(Y^2)$ existieren, und $c\in\mathbb{R}$. Dann gilt

<span class="anker" id="gl-8-2"></span>
$$\operatorname{Var}(cX)=c^2\operatorname{Var}(X),\qquad\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y) \tag{8.2}$$

mit der __Kovarianz__

<span class="anker" id="gl-8-3"></span>
$$\operatorname{Cov}(X,Y):=\mathbb{E}\bigl[(X-\mathbb{E}(X))(Y-\mathbb{E}(Y))\bigr]=\mathbb{E}(XY)-\mathbb{E}(X)\,\mathbb{E}(Y). \tag{8.3}$$
:::

:::beweis Varianz von Summen
Es ist $(cX-c\mu)^2=c^2(X-\mu)^2$. Für die Summe bilde mit $a=X-\mathbb{E}(X)$, $b=Y-\mathbb{E}(Y)$ den Erwartungswert von $(a+b)^2=a^2+b^2+2ab$. Die zweite Form von $\operatorname{Cov}$ folgt durch Ausmultiplizieren.
:::

⁠**So liest man das:** Die Varianz ist quadratisch, nicht linear. $\operatorname{Cov}(X,Y)>0$ heißt, dass $X$ und $Y$ tendenziell gemeinsam über oder unter ihrem Mittel liegen.

::::beispiel
$\mathbb{E}(W_1W_2)=\frac1{16}\sum_{i,j}ij=\frac{25}4=\mathbb{E}(W_1)\,\mathbb{E}(W_2)$, also $\operatorname{Cov}(W_1,W_2)=0$ und $\operatorname{Var}(S)=\frac52$. Dagegen ist $\operatorname{Cov}(W_1,S)=\operatorname{Var}(W_1)=\frac54$: Eine hohe erste Augenzahl macht eine hohe Summe wahrscheinlicher.
::::

:::satz Satz 8.3 (Tschebyschew-Ungleichung)
<span class="anker" id="satz-8-3"></span>

Sei $X$ eine Zufallsvariable mit $\mathbb{E}(X)=\mu$ und $\operatorname{Var}(X)=\sigma^2$. Dann gilt für alle $\varepsilon>0$

<span class="anker" id="gl-8-4"></span>
$$\mathbb{P}(|X-\mu|\ge\varepsilon)\le\frac{\sigma^2}{\varepsilon^2}. \tag{8.4}$$
:::

:::beweis Tschebyschew
Im diskreten Fall lässt man nichtnegative Summanden weg und verkleinert die übrigen, denn dort ist $(x_i-\mu)^2\ge\varepsilon^2$:

$$\begin{aligned} \sigma^2=\sum_i(x_i-\mu)^2\,\mathbb{P}(X=x_i)&\ge\sum_{|x_i-\mu|\ge\varepsilon}(x_i-\mu)^2\,\mathbb{P}(X=x_i)\\ &\ge\varepsilon^2\sum_{|x_i-\mu|\ge\varepsilon}\mathbb{P}(X=x_i)=\varepsilon^2\,\mathbb{P}(|X-\mu|\ge\varepsilon). \end{aligned}$$

Im absolut stetigen Fall steht statt der Summen $\int(x-\mu)^2f(x)\,\mathrm{d} x$, und derselbe Schluss gilt.
:::

⁠**So liest man das:** Für große $\varepsilon$ fällt die Schranke quadratisch. Für $\varepsilon\le\sigma$ ist sie mindestens 1 und sagt nichts, denn $\mathbb{P}(A)\le1$ gilt immer. Der Grenzfall $\varepsilon=\sigma$ zeigt, dass $\sigma$ die Größe der typischen Abweichung angibt.

::::beispiel
Für die LED ist $\mathbb{P}(|X-2|\ge4)=\mathbb{P}(X\ge6)=\mathrm{e}^{-3}\approx0{,}05$, die Schranke gibt $\frac4{16}=0{,}25$. Sie ist grob (Abb. [8](#abb-8)), gilt dafür aber für jede Verteilung.

:::abbildung hm3/k8tscheb 8
Abweichung um mindestens $k\sigma$: die Schranke $1/k^2$ und die wahren Werte für Normalverteilung und LED. Unter $k=1$ sagt die Schranke nichts.
:::
::::

:::aufgabe Aufgabe 12 ★★ Schranke und Wirklichkeit
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Für die Dichte aus Aufgabe [9](dichten.html#aufg-9): Berechne $\mathbb{E}(X)$ und $\operatorname{Var}(X)$. Vergleiche die Schranke für $\mathbb{P}(|X-1|\ge\frac34)$ mit dem wahren Wert.

</li>

<li>

Sei $X$ Poisson-verteilt mit $\lambda>0$. Zeige $\mathbb{P}(X\ge2\lambda)\le1/\lambda$.

</li>

</ol>

:::loesung
(a) Die Dichte ist symmetrisch um 1, also $\mathbb{E}(X)=1$. $\mathbb{E}(X^2)=\frac34\int_0^2(2x^3-x^4)\,\mathrm{d} x=\frac34(8-\frac{32}5)=\frac65$, also $\operatorname{Var}(X)=\frac15$. Schranke: $\frac15/\frac9{16}=\frac{16}{45}\approx0{,}356$. Wahr: $2F_X(\frac14)=\frac{11}{128}\approx0{,}086$. (b) $\{X\ge2\lambda\}\subset\{|X-\lambda|\ge\lambda\}$. Mit [(8.4)](#gl-8-4) und $\sigma^2=\lambda$ folgt $\lambda/\lambda^2=1/\lambda$.
:::
:::

:::aufgabe Aufgabe 13 ★★★ Korrelation
<span class="anker" id="aufg-13"></span>

Seien $X,Y$ Zufallsvariablen mit positiven, endlichen Varianzen.

<ol class="al">

<li>

Zeige $\operatorname{Cov}(aX+b,\,cY+d)=ac\operatorname{Cov}(X,Y)$.

</li>

<li>

Zeige $|\operatorname{Cov}(X,Y)|\le\sigma_X\sigma_Y$. Tipp: $\operatorname{Var}(Y-tX)\ge0$ für alle $t\in\mathbb{R}$ ist eine Parabel in $t$ ohne zwei Nullstellen.

</li>

<li>

Der __Korrelationskoeffizient__ $\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$ liegt also in $[-1,1]$. Berechne ihn für $W_1$ und $S$.

</li>

</ol>

:::loesung
(a) $aX+b-\mathbb{E}(aX+b)=a(X-\mathbb{E}(X))$, ebenso für $Y$. (b) Mit (a) und [(8.2)](#gl-8-2) ist $\operatorname{Var}(Y-tX)=\sigma_Y^2-2t\operatorname{Cov}(X,Y)+t^2\sigma_X^2\ge0$. Eine Parabel ohne zwei Nullstellen hat eine Diskriminante $\le0$: $4\operatorname{Cov}(X,Y)^2-4\sigma_X^2\sigma_Y^2\le0$. (c) $\frac{5/4}{\sqrt{5/4}\,\sqrt{5/2}}=\frac1{\sqrt2}\approx0{,}707$.
:::
:::
