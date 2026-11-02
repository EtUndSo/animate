---
title: Stufe 4: Lokale Majoranten und Transformierte
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120600
summary: Für viele wichtige Parameterintegrale gibt es keine Majorante, die für alle Parameter zugleich gilt.
tags: lokal, Laplace-Transformierte, Gamma-Funktion, Fourier-Transformierte
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Für viele wichtige Parameterintegrale gibt es keine Majorante, die für alle Parameter zugleich gilt. Diese Stufe zeigt, warum eine Majorante in der Nähe jedes Punktes genügt, und wendet das auf die drei wichtigsten Fälle an.
:::

**Die Idee.** Stetigkeit und Differenzierbarkeit in einem Punkt entscheiden sich in einer beliebig kleinen Umgebung dieses Punkts. Man nennt solche Eigenschaften __lokal__. Es genügt also, zu jedem $\boldsymbol{x}_0\in\mathcal U$ eine offene Umgebung $\mathcal V(\boldsymbol{x}_0)\subset\mathcal U$ zu finden, auf der eine Majorante gilt. Verschiedene Punkte dürfen verschiedene Majoranten haben.

Die Abklingkurve zeigt den Nutzen. Auf $(0,\infty)$ ist $\int_0^\infty\mathrm{e}^{-xt}\,\mathrm{d} t=1/x$. Für festes $t$ ist $\sup_{x>0}\mathrm{e}^{-xt}=1$, und die Eins ist auf $(0,\infty)$ nicht integrierbar. Eine Majorante für alle $x$ gibt es also nicht. Aber für $x>x_0/2$ gilt $\mathrm{e}^{-xt}\le\mathrm{e}^{-x_0t/2}$, und das ist integrierbar (Abb. [4](#abb-4)).

:::abbildung hm3/k2majorante 4
Für $x_0=1$ liegen alle Kurven $\mathrm{e}^{-xt}$ mit $x>\frac12$ unter der Majorante $g(t)=\mathrm{e}^{-t/2}$. Die Kurve zu $x=0{,}2$ gehört nicht zu dieser Umgebung und läuft darüber. Sie bekommt ihre eigene Majorante.
:::

**Laplace-Transformation.** Sei $f:[0,\infty)\to\mathbb{R}$ stetig mit höchstens polynomialem Wachstum, also $|f(t)|\le C(1+t^m)$ mit Konstanten $C$ und $m$. Die reelle __Laplace-Transformierte__ von $f$ ist

<span class="anker" id="gl-4-1"></span>
$$F(x)=\mathcal{L} f(x)=\int_0^\infty f(t)\,\mathrm{e}^{-xt}\,\mathrm{d} t,\qquad x>0. \tag{4.1}$$

Das Integral konvergiert für jedes $x>0$, $F$ ist beliebig oft differenzierbar in $(0,\infty)$, und für alle $k\in\mathbb{N}$ gilt

<span class="anker" id="gl-4-2"></span>
$$F^{(k)}(x)=\int_0^\infty(-t)^kf(t)\,\mathrm{e}^{-xt}\,\mathrm{d} t,\quad\text{also}\quad\frac{\mathrm{d}^k}{\mathrm{d} x^k}(\mathcal{L} f)(x)=\mathcal{L}\bigl((-t)^kf(t)\bigr)(x). \tag{4.2}$$

:::herleitung Lokale Majorante
Sei $x_0>0$ und $\mathcal V(x_0)=(\frac{x_0}2,\infty)$. Es gibt eine Konstante $C_1>0$, so dass für alle $x\in\mathcal V(x_0)$ gilt:

$$|f(t)\,\mathrm{e}^{-xt}|\le|f(t)|\exp\bigl(-\tfrac12x_0t\bigr)\le C_1\exp\bigl(-\tfrac14x_0t\bigr)=:g(t),$$

denn $|f(t)|\exp(-\frac14x_0t)$ ist beschränkt: Ein Polynom verliert gegen die Exponentialfunktion. Da $g$ über $(0,\infty)$ integrierbar ist, folgt aus dem Majorantenkriterium die Stetigkeit von $F$ in $\mathcal V(x_0)$. Da $x_0>0$ beliebig ist, ist $F$ auf ganz $(0,\infty)$ stetig. Für die Ableitungen wiederholt man das Argument: $(-t)^kf(t)$ wächst wieder höchstens polynomial, und $\partial_x\mathrm{e}^{-xt}=-t\,\mathrm{e}^{-xt}$.
:::

⁠**So liest man das:** Jede Ableitung nach $x$ zieht den Faktor $-t$ aus dem Exponenten. Aus $\mathcal{L} 1(x)=1/x$ folgt sofort $\mathcal{L}(t^k)(x)=k!/x^{k+1}$. Bei $k=1$, $x=2$ ist das $\int_0^\infty t\,\mathrm{e}^{-2t}\,\mathrm{d} t=\frac14$.

**Gamma-Funktion.** Für $x>0$ ist die __Gamma-Funktion__

<span class="anker" id="gl-4-3"></span>
$$\Gamma(x):=\int_0^\infty\mathrm{e}^{-t}\,t^{x-1}\,\mathrm{d} t,\qquad\text{und es gilt}\qquad\Gamma'(x)=\int_0^\infty\mathrm{e}^{-t}\,t^{x-1}\ln t\,\mathrm{d} t. \tag{4.3}$$

Der Parameter steckt im Exponenten, deshalb entsteht beim Ableiten $\partial_xt^{x-1}=t^{x-1}\ln t$. $\Gamma$ ist stetig differenzierbar auf $(0,\infty)$. Eine lokale Majorante auf $\mathcal V(x_0)=(\frac{x_0}2,2x_0)$ ist $g(t)=\mathrm{e}^{-t}\bigl(t^{x_0/2-1}+t^{2x_0-1}\bigr)$: Der erste Summand deckelt den Bereich $t\le1$, er ist dort wegen $x_0/2>0$ integrierbar. Der zweite deckelt $t\ge1$. **Grenzfall:** $\Gamma(1)=\int_0^\infty\mathrm{e}^{-t}\,\mathrm{d} t=1$.

**Fourier-Transformation.** Für stetiges $f:\mathbb{R}\to\mathbb{C}$ mit $\int_\mathbb{R}|f(x)|\,\mathrm{d} x<\infty$ ist die __Fourier-Transformierte__

<span class="anker" id="gl-4-4"></span>
$$\hat f(\xi)=\frac1{\sqrt{2\pi}}\int_\mathbb{R} f(x)\,\mathrm{e}^{-\mathrm i\xi x}\,\mathrm{d} x \tag{4.4}$$

stetig und beschränkt. Hier ist $\xi$ der Parameter und $x$ die Integrationsvariable. Wegen $|\mathrm{e}^{-\mathrm i\xi x}|=1$ ist $g(x)=|f(x)|/\sqrt{2\pi}$ eine Majorante, die nicht von $\xi$ abhängt. Das Kriterium gilt für Real- und Imaginärteil, und es folgt auch $|\hat f(\xi)|\le\int_\mathbb{R} g\,\mathrm{d} x$. Sind für $k\in\mathbb{N}$ und $0\le\ell\le k$ die Funktionen $x\mapsto x^\ell f(x)$ absolut integrierbar, ist $\hat f$ $k$-mal stetig differenzierbar, und $\hat f^{(\ell)}$ ist die Fourier-Transformierte von $x\mapsto(-\mathrm ix)^\ell f(x)$. Der Mechanismus ist derselbe wie bei Laplace: Jede Ableitung nach $\xi$ zieht $-\mathrm ix$ aus dem Exponenten.

Beispiel: Für $f(x)=\mathrm{e}^{-|x|}$ fällt der ungerade Sinusanteil weg, und mit dem Beispiel aus Stufe [3](bis-ins-unendliche.html#stufe-3) ist $\hat f(\xi)=\frac{2}{\sqrt{2\pi}}\int_0^\infty\mathrm{e}^{-x}\cos(\xi x)\,\mathrm{d} x=\sqrt{\frac2\pi}\,\frac{1}{1+\xi^2}$.

:::frage Gelten die Formeln dann auch am Rand, bei $x=0$?
Nein. Lokal heißt: Jeder Punkt der offenen Menge hat seine eigene Umgebung. Der Rand gehört nicht dazu. $\mathcal{L}1(x)=1/x$ hat bei $x\to0$ keinen endlichen Grenzwert, und $\Gamma(x)$ wächst dort ebenfalls unbeschränkt.
:::

:::aufgabe Aufgabe 5 ★★ Gamma und Laplace
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Zeige $\Gamma(x+1)=x\,\Gamma(x)$ für $x>0$ und folgere $\Gamma(n+1)=n!$ für $n\in\mathbb{N}$.

</li>

<li>

Gib für $\partial_x(\mathrm{e}^{-t}t^{x-1})$ eine Majorante auf $\mathcal V(x_0)=(\frac{x_0}2,2x_0)$ an.

</li>

<li>

Berechne $\mathcal{L}(t\sin t)(x)$ aus $\mathcal{L}(\sin t)(x)=1/(1+x^2)$.

</li>

</ol>

:::loesung
(a) Partielle Integration: $\Gamma(x+1)=\int_0^\infty\mathrm{e}^{-t}t^x\,\mathrm{d} t=\bigl[-\mathrm{e}^{-t}t^x\bigr]_0^\infty+x\int_0^\infty\mathrm{e}^{-t}t^{x-1}\,\mathrm{d} t=x\,\Gamma(x)$. Mit $\Gamma(1)=1$ folgt $\Gamma(n+1)=n\,\Gamma(n)=\dots=n!$. (b) $|\partial_x(\mathrm{e}^{-t}t^{x-1})|=\mathrm{e}^{-t}t^{x-1}|\ln t|\le G(t):=\mathrm{e}^{-t}\bigl(t^{x_0/2-1}+t^{2x_0-1}\bigr)|\ln t|$ auf $\mathcal V(x_0)$. $G$ ist integrierbar: Nahe 0 ist $t^{x_0/4}|\ln t|$ beschränkt, es bleibt $t^{x_0/4-1}$. Für große $t$ gewinnt $\mathrm{e}^{-t}$. (c) Aus [(4.2)](#gl-4-2) mit $k=1$ folgt $\mathcal{L}(t\sin t)(x)=-\frac{\mathrm{d}}{\mathrm{d} x}\frac1{1+x^2}=\frac{2x}{(1+x^2)^2}$.
:::
:::

:::aufgabe Aufgabe 6 ★★★ Kosinus unter der Glocke
<span class="anker" id="aufg-6"></span>

Sei $K(x)=\int_0^\infty\mathrm{e}^{-t^2}\cos(xt)\,\mathrm{d} t$ für $x\in\mathbb{R}$. Bekannt ist $\int_0^\infty\mathrm{e}^{-t^2}\,\mathrm{d} t=\sqrt\pi/2$.

<ol class="al">

<li>

Zeige mit Majoranten, dass $K$ stetig differenzierbar ist, und gib $K'$ als Integral an.

</li>

<li>

Zeige durch partielle Integration $K'(x)=-\frac x2K(x)$.

</li>

<li>

Löse diese Gleichung mit dem Startwert $K(0)$. Welchen Wert hat $K(2)$?

</li>

</ol>

:::loesung
(a) $|\mathrm{e}^{-t^2}\cos(xt)|\le\mathrm{e}^{-t^2}$ und $|\partial_x(\mathrm{e}^{-t^2}\cos(xt))|\le t\,\mathrm{e}^{-t^2}$, beide integrierbar und unabhängig von $x$. Also ist $K'(x)=-\int_0^\infty t\,\mathrm{e}^{-t^2}\sin(xt)\,\mathrm{d} t$. (b) Mit der Stammfunktion $-\frac12\mathrm{e}^{-t^2}$ von $t\,\mathrm{e}^{-t^2}$ ist

$$K'(x)=\Bigl[\tfrac12\mathrm{e}^{-t^2}\sin(xt)\Bigr]_0^\infty-\frac x2\int_0^\infty\mathrm{e}^{-t^2}\cos(xt)\,\mathrm{d} t=-\frac x2K(x).$$

(c) Trennen der Variablen gibt $K(x)=K(0)\,\mathrm{e}^{-x^2/4}=\frac{\sqrt\pi}2\mathrm{e}^{-x^2/4}$. Also ist $K(2)=\frac{\sqrt\pi}{2\mathrm{e}}\approx0{,}326$. Die Glockenkurve bleibt also eine Glockenkurve.
:::
:::
