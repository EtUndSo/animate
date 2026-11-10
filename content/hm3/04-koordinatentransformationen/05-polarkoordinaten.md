---
title: Stufe 3: Polarkoordinaten
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Koordinatentransformationen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/koordinatentransformationen
knoten: Kapitel 4: Koordinatentransformationen
order: 3140500
summary: Kreise werden zu Rechtecken.
tags: Polarkoordinaten, Gauß-Integral
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Kreise werden zu Rechtecken. Diese Stufe bestimmt den Faktor dafür, zeigt, warum die Formel trotz verletzter Voraussetzungen gilt, und löst damit ein Integral, das in einer Variablen nicht gelingt.
:::

**Die Idee.** Jeder Punkt der Ebene hat einen Abstand $r$ vom Nullpunkt und einen Winkel $\varphi$ zur $x$-Achse. Das Rechteck der Werte $(r,\varphi)$ überdeckt die Kreisscheibe (Abb. [3](#abb-3)). Eine Zelle mit den Kanten $\mathrm{d} r$ und $\mathrm{d}\varphi$ wird zu einem Ringstück mit der radialen Länge $\mathrm{d} r$ und der Bogenlänge $r\,\mathrm{d}\varphi$. Weit außen sind die Zellen also breiter, ihre Fläche ist $r\,\mathrm{d} r\,\mathrm{d}\varphi$.

:::abbildung hm3/k4polar 3
Das Rechteck der Werte $(r,\varphi)$ überdeckt die Kreisscheibe. Die blaue Zelle wird zum Ringstück mit den Kanten $\mathrm{d} r$ und $r\,\mathrm{d}\varphi$. Orange: Streifen der Breite $\varepsilon$ am Rand des Rechtecks und ihr Bild, ein kleiner Kreis und ein schmaler Keil.
:::

:::definition Definition 3.1 (Polarkoordinaten)
<span class="anker" id="satz-3-1"></span>

Die __Polarkoordinaten__ der Kreisscheibe $\overline{B_R(0)}=\{(x,y)\in\mathbb{R}^2:x^2+y^2\le R^2\}$ sind

<span class="anker" id="gl-3-1"></span>
$$\Phi(r,\varphi)=\begin{pmatrix}r\cos\varphi\\r\sin\varphi\end{pmatrix},\qquad(r,\varphi)\in[0,R]\times[0,2\pi]. \tag{3.1}$$
:::

Zum Beispiel gehört $(r,\varphi)=(2,\frac\pi2)$ zum Punkt $(0,2)$. Aus [(3.1)](#gl-3-1) folgt

$$D\Phi(r,\varphi)=\begin{pmatrix}\cos\varphi&-r\sin\varphi\\\sin\varphi&r\cos\varphi\end{pmatrix},\qquad\det D\Phi(r,\varphi)=r\cos^2\varphi+r\sin^2\varphi=r.$$

Für diese Determinante schreibt man auch $\dfrac{\partial(x,y)}{\partial(r,\varphi)}$. Für stetiges $f:\mathbb{R}^2\to\mathbb{R}$ gilt

<span class="anker" id="gl-3-2"></span>
$$\int_{B_R(0)}f(x,y)\,\mathrm{d} x\,\mathrm{d} y=\int_0^R\!\!\int_0^{2\pi}f(\Phi(r,\varphi))\,r\,\mathrm{d}\varphi\,\mathrm{d} r. \tag{3.2}$$

**Die Voraussetzungen sind verletzt.** Auf $[0,R]\times[0,2\pi]$ ist $\Phi$ nicht injektiv: Die ganze Kante $r=0$ geht in den Nullpunkt, und $\varphi=0$, $\varphi=2\pi$ geben denselben Strahl. Außerdem ist $\det D\Phi=0$ bei $r=0$. Die Formel gilt trotzdem: Auf $[\varepsilon,R]\times[\varepsilon,2\pi]$ sind alle Voraussetzungen erfüllt, und dort fehlen nur ein kleiner Kreis und ein schmaler Keil mit der Fläche höchstens $\pi\varepsilon^2+\frac12\varepsilon R^2$. Mit $|f|\le M$ ist der fehlende Beitrag höchstens $M$ mal diese Fläche und geht für $\varepsilon\searrow0$ gegen null. Ausnahmemengen ohne Fläche stören also nicht.

::::beispiel die Scheibe
Für $R=2$ gibt [(3.2)](#gl-3-2) mit $f=1$ die Fläche $2\pi\int_0^2r\,\mathrm{d} r=4\pi$, wie erwartet. Mit $f=x^2+y^2=r^2$ folgt $\int(x^2+y^2)\,\mathrm{d} x\,\mathrm{d} y=2\pi\int_0^2r^3\,\mathrm{d} r=8\pi$. Ohne den Faktor $r$ käme $\frac{16\pi}3$ heraus: Die äußeren Zellen, in denen $f$ groß ist, würden zu schwach zählen.
::::

**Das Gauß-Integral.** Für $\mathrm{e}^{-x^2}$ gibt es keine Stammfunktion in geschlossener Form. Der Umweg über ein Mehrfachintegral liefert trotzdem das __Gauß-Integral__

<span class="anker" id="gl-3-3"></span>
$$\int_{-\infty}^\infty\mathrm{e}^{-x^2}\,\mathrm{d} x=\sqrt\pi. \tag{3.3}$$

:::herleitung Gauß-Integral
⁠**Schritt 1: Polarkoordinaten.** Der Faktor $r$ macht das Integral lösbar, denn $r\,\mathrm{e}^{-r^2}$ hat die Stammfunktion $-\frac12\mathrm{e}^{-r^2}$:

$$\int_{B_R(0)}\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d} x\,\mathrm{d} y=\int_0^{2\pi}\!\!\int_0^R\mathrm{e}^{-r^2}\,r\,\mathrm{d} r\,\mathrm{d}\varphi=\pi\bigl(1-\mathrm{e}^{-R^2}\bigr)\xrightarrow{R\to\infty}\pi.$$

⁠**Schritt 2: Quadrat einschließen.** Für $I(R)=\int_{-R}^R\mathrm{e}^{-x^2}\,\mathrm{d} x$ gilt nach Fubini $I(R)^2=\int_{[-R,R]^2}\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d} x\,\mathrm{d} y$. Das Quadrat liegt zwischen $B_R(0)$ und $B_{\sqrt2R}(0)$, und der Integrand ist positiv. Also

$$\int_{B_R(0)}\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d} x\,\mathrm{d} y\le\Bigl(\int_{-R}^R\mathrm{e}^{-x^2}\,\mathrm{d} x\Bigr)^2\le\int_{B_{\sqrt2R}(0)}\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d} x\,\mathrm{d} y.$$

⁠**Schritt 3: Grenzwert.** Beide Ränder gehen gegen $\pi$, also auch $I(R)^2$. Wegen $I(R)>0$ folgt die Behauptung. **Kontrolle** für $R=2$: Die Kette lautet $3{,}084\le3{,}112\le3{,}141$.
:::

:::frage Muss $\varphi$ immer von 0 bis $2\pi$ laufen?
Nein. Jedes Intervall der Länge $2\pi$ überdeckt den Kreis genau einmal, ein kürzeres gibt einen Sektor. Läuft $\varphi$ dagegen über $[0,4\pi]$, wird die Scheibe doppelt getroffen, und $\Phi$ ist nicht mehr injektiv: Die Formel ergäbe die doppelte Fläche. Der Mittelpunkt darf auch woanders liegen: $\Phi(r,\varphi)=(x_0+r\cos\varphi,\,y_0+r\sin\varphi)$ hat ebenfalls den Faktor $r$.
:::

:::aufgabe Aufgabe 4 ★ Viertelring
<span class="anker" id="aufg-4"></span>

Sei $D$ der Teil des Rings $1\le x^2+y^2\le4$ mit $x,y\ge0$. Gib das Rechteck $B$ an und berechne $\int_D\frac{xy}{x^2+y^2}\,\mathrm{d} x\,\mathrm{d} y$.

:::loesung
$B=[1,2]\times[0,\frac\pi2]$. Der Integrand ist $\cos\varphi\sin\varphi$, also $\int_1^2\!\int_0^{\pi/2}\cos\varphi\sin\varphi\;r\,\mathrm{d}\varphi\,\mathrm{d} r=\frac32\cdot\frac12=\frac34$.
:::
:::

:::aufgabe Aufgabe 5 ★★ Gauß-Integrale
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Berechne $\int_{-\infty}^\infty\mathrm{e}^{-x^2/2}\,\mathrm{d} x$ mit einer Substitution aus [(3.3)](#gl-3-3).

</li>

<li>

Berechne $\int_{\mathbb{R}^2}(x^2+y^2)\,\mathrm{e}^{-(x^2+y^2)}\,\mathrm{d} x\,\mathrm{d} y$ als Grenzwert über Kreisscheiben. Tipp: $w=r^2$.

</li>

</ol>

:::loesung
(a) Mit $x=\sqrt2\,t$ ist $\mathrm{d} x=\sqrt2\,\mathrm{d} t$, also $\int_{-\infty}^\infty\mathrm{e}^{-x^2/2}\,\mathrm{d} x=\sqrt2\,\sqrt\pi=\sqrt{2\pi}\approx2{,}51$. (b) $2\pi\int_0^Rr^3\,\mathrm{e}^{-r^2}\,\mathrm{d} r=\pi\int_0^{R^2}w\,\mathrm{e}^{-w}\,\mathrm{d} w$ mit $w=r^2$. Für $R\to\infty$ geht $\int_0^{R^2}w\,\mathrm{e}^{-w}\,\mathrm{d} w$ gegen 1. Der Wert ist $\pi$.
:::
:::
