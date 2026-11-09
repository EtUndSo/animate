---
title: Stufe 10: Zufallsvektoren mit Dichte
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3181100
summary: Zwei stetige Messgrößen bilden einen zufälligen Punkt in der Ebene.
tags: gemeinsame Dichte, Randdichten, Faltung
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Zwei stetige Messgrößen bilden einen zufälligen Punkt in der Ebene. Diese Stufe beschreibt ihn durch eine Dichte über der Ebene und liest daraus die einzelnen Verteilungen und die Unabhängigkeit ab.
:::

**Die Idee.** Die Dichte eines Paars ist eine Landschaft über der Ebene. Das Volumen unter ihr über einem Gebiet ist die Wahrscheinlichkeit dieses Gebiets. Wer nur $X$ betrachtet, integriert quer zur $x$-Achse auf.

:::definition Definition 10.1 (Absolut stetiger Zufallsvektor)
<span class="anker" id="satz-10-1"></span>

$(X,Y)$ heißt absolut stetig, wenn es eine integrierbare Funktion $f_{X,Y}:\mathbb{R}^2\to[0,\infty)$ gibt, die __gemeinsame Dichte__, mit

<span class="anker" id="gl-10-1"></span>
$$F_{X,Y}(x,y)=\int_{-\infty}^x\!\!\int_{-\infty}^yf_{X,Y}(s,t)\,\mathrm{d} t\,\mathrm{d} s. \tag{10.1}$$
:::

Notwendig gilt $\int_{\mathbb{R}^2}f_{X,Y}(x,y)\,\mathrm{d} x\,\mathrm{d} y=1$. Für ein Gebiet $M$ ist $\mathbb{P}((X,Y)\in M)=\int_Mf_{X,Y}\,\mathrm{d} x\,\mathrm{d} y$.

:::satz Satz 10.2 (Randdichten und Unabhängigkeit)
<span class="anker" id="satz-10-2"></span>

Besitzt $(X,Y)$ die Dichte $f=f_{X,Y}$, dann gilt:

<ol class="rm">

<li>

$X$ und $Y$ sind absolut stetig, ihre Dichten sind die __Randdichten__

<span class="anker" id="gl-10-2"></span>
$$f_X(x)=\int_{-\infty}^\infty f(x,y)\,\mathrm{d} y,\qquad f_Y(y)=\int_{-\infty}^\infty f(x,y)\,\mathrm{d} x. \tag{10.2}$$

</li>

<li>

$X$ und $Y$ sind genau dann unabhängig, wenn $f(x,y)=f_X(x)\,f_Y(y)$ für alle $x,y\in\mathbb{R}$.

</li>

</ol>
:::

:::beweis Randdichten und Unabhängigkeit
(i) Ausintegrieren gibt

$$F_X(x)=\mathbb{P}(X\le x,\,Y<\infty)=\int_{-\infty}^x\Bigl(\int_{-\infty}^\infty f(s,t)\,\mathrm{d} t\Bigr)\mathrm{d} s,$$

und die Klammer ist $f_X(s)$. Für $Y$ geht es genauso.

(ii) Gilt $f=f_Xf_Y$, gibt Integration über $s\le x$, $t\le y$ die Gleichung $F_{X,Y}=F_XF_Y$. Umgekehrt: Ist $F_{X,Y}$ zweimal stetig differenzierbar, gibt Ableiten von $F_{X,Y}=F_XF_Y$ nach $x$ und $y$ die Produktform.
:::

⁠**So liest man das:** Unabhängig heißt, die Landschaft ist das Produkt ihrer Profile. Sind $X,Y$ unabhängig mit Dichten, hat $(X,Y)$ die Dichte $f_Xf_Y$. Für abhängige $X,Y$ muss es keine gemeinsame Dichte geben: Für $Y=X$ liegt alles auf der Diagonale, die die Fläche null hat.

Aus der gemeinsamen Dichte lässt sich der Erwartungswert des Produkts berechnen:

<span class="anker" id="gl-10-3"></span>
$$\mathbb{E}(XY)=\int_{-\infty}^\infty\!\!\int_{-\infty}^\infty xy\,f(x,y)\,\mathrm{d} x\,\mathrm{d} y. \tag{10.3}$$

Für unabhängige $X,Y$ zerfällt das Integral nach (ii) und gibt wieder $\mathbb{E}(XY)=\mathbb{E}(X)\,\mathbb{E}(Y)$.

::::beispiel
Sei $f(x,y)=x+y$ auf $[0,1]^2$ und 0 sonst. Die Normierung stimmt: $\frac12+\frac12=1$. Aus [(10.2)](#gl-10-2) folgt $f_X(x)=x+\frac12$ auf $[0,1]$, und genauso für $Y$. Das Produkt der Randdichten ist nicht $x+y$, also sind $X,Y$ abhängig. Mit $\mathbb{E}(X)=\mathbb{E}(Y)=\frac7{12}$ und $\mathbb{E}(XY)=\frac13$ ist $\operatorname{Cov}(X,Y)=\frac13-\frac{49}{144}=-\frac1{144}$.
::::

**Zweidimensionale Normalverteilung.** Sind $X,Y\sim\mathcal N(0,1)$ unabhängig, hat $(X,Y)$ die Dichte

<span class="anker" id="gl-10-4"></span>
$$f_{X,Y}(x,y)=f_X(x)\,f_Y(y)=\frac1{2\pi}\exp\Bigl(-\frac{x^2+y^2}2\Bigr), \tag{10.4}$$

und heißt standard-normalverteilt. Die Höhenlinien sind Kreise (Abb. [10](#abb-10)). Für $0\le\rho<1$ koppelt ein gemischter Term die beiden Variablen:

<span class="anker" id="gl-10-5"></span>
$$f_{X,Y}(x,y)=\frac1{2\pi\sqrt{1-\rho^2}}\exp\Bigl(-\frac{x^2-2\rho xy+y^2}{2(1-\rho^2)}\Bigr). \tag{10.5}$$

:::herleitung Die Randdichte bei $\rho\neq0$
Quadratische Ergänzung gibt $x^2-2\rho xy+y^2=(y-\rho x)^2+(1-\rho^2)x^2$. Also ist

$$f_X(x)=\frac{\mathrm{e}^{-x^2/2}}{2\pi\sqrt{1-\rho^2}}\int_{-\infty}^\infty\exp\Bigl(-\frac{(y-\rho x)^2}{2(1-\rho^2)}\Bigr)\mathrm{d} y=\frac1{\sqrt{2\pi}}\mathrm{e}^{-x^2/2},$$

denn die Substitution $v=(y-\rho x)/\sqrt{1-\rho^2}$ gibt für das Integral $\sqrt{1-\rho^2}\,\sqrt{2\pi}$.
:::

Für jedes $\rho$ sind $X$ und $Y$ also standard-normalverteilt. Unabhängig sind sie aber nur im **Grenzfall** $\rho=0$, denn nur dann ist [(10.5)](#gl-10-5) das Produkt [(10.4)](#gl-10-4).

:::abbildung hm3/k8hoehen 10
Höhenlinien von [(10.5)](#gl-10-5). Links Kreise: $x$ sagt nichts über $y$. Rechts schräge Ellipsen: Große $x$ gehen mit großen $y$ einher.
:::

:::aufgabe Aufgabe 15 ★★ Randdichten
<span class="anker" id="aufg-15"></span>

$(X,Y)$ habe auf $[-1,1]^2$ die Dichte $f(x,y)=c\,(1+xy)$, sonst 0. Bestimme $c$, die Randdichten, $\mathbb{E}(X)$, $\operatorname{Var}(X)$ und $\operatorname{Cov}(X,Y)$. Sind $X,Y$ unabhängig?

:::loesung
$\int_{[-1,1]^2}(1+xy)\,\mathrm{d} x\,\mathrm{d} y=4$, also $c=\frac14$. Der Term $xy$ integriert sich in $y$ zu null: $f_X=f_Y=\frac12$ auf $[-1,1]$, gleichverteilt. Also $\mathbb{E}(X)=0$, $\operatorname{Var}(X)=\frac{2^2}{12}=\frac13$. $\operatorname{Cov}(X,Y)=\mathbb{E}(XY)=\frac14\int\!\!\int x^2y^2\,\mathrm{d} x\,\mathrm{d} y=\frac14\cdot\frac23\cdot\frac23=\frac19$. Abhängig, denn $f_Xf_Y=\frac14\neq f$.
:::
:::

:::aufgabe Aufgabe 16 ★★ Kollision zweier Pulse
<span class="anker" id="aufg-16"></span>

Zwei Pulse kommen unabhängig voneinander zu gleichverteilten Zeiten $X,Y\in[0,1]$ an. Sie stören sich, wenn $|X-Y|<\frac15$ ist. Berechne die Wahrscheinlichkeit als Fläche im Einheitsquadrat und bestimme $\mathbb{E}(|X-Y|)$.

:::loesung
$(X,Y)$ hat auf $[0,1]^2$ die Dichte 1. Das Gegenereignis sind zwei Dreiecke mit Kathete $\frac45$, zusammen $\frac{16}{25}$. Ergebnis: $\frac9{25}$. Außerdem $\mathbb{E}(|X-Y|)=2\int_0^1\!\int_0^x(x-y)\,\mathrm{d} y\,\mathrm{d} x=\int_0^1x^2\,\mathrm{d} x=\frac13$.
:::
:::

:::aufgabe Aufgabe 17 ★★★ Die Dichte einer Summe
<span class="anker" id="aufg-17"></span>

Für unabhängige $X,Y$ mit Dichten und $Z=X+Y$ ist $F_Z(z)=\int_{x+y\le z}f_X(x)f_Y(y)\,\mathrm{d} x\,\mathrm{d} y$. Zeige $f_Z(z)=\int_\mathbb{R} f_X(x)\,f_Y(z-x)\,\mathrm{d} x$, die __Faltung__. Berechne $f_Z$ für zwei LEDs, die nacheinander brennen, und prüfe $\mathbb{E}(Z)=4$.

:::loesung
Mit Fubini ist $F_Z(z)=\int_\mathbb{R} f_X(x)\int_{-\infty}^{z-x}f_Y(y)\,\mathrm{d} y\,\mathrm{d} x$. Ableiten nach $z$ gibt die Faltung. Für $z\ge0$ läuft $x$ von 0 bis $z$, und die Exponenten addieren sich zu $-z/2$: $f_Z(z)=\int_0^z\frac14\mathrm{e}^{-z/2}\,\mathrm{d} x=\frac z4\mathrm{e}^{-z/2}$. $\mathbb{E}(Z)=\frac14\int_0^\infty z^2\mathrm{e}^{-z/2}\,\mathrm{d} z=\frac14\cdot16=4$.
:::
:::
