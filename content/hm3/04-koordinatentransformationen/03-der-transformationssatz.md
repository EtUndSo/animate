---
title: Stufe 1: Der Transformationssatz
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3140300
summary: In einer Variablen ersetzt die Substitutionsregel eine Integrationsvariable durch eine andere.
tags: Funktionaldeterminante, Transformationssatz
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
In einer Variablen ersetzt die Substitutionsregel eine Integrationsvariable durch eine andere. Diese Stufe überträgt die Regel auf mehrere Variablen und bestimmt den Faktor, der dabei entsteht.
:::

**Die Idee.** Die Substitutionsregel

<span class="anker" id="gl-1-1"></span>
$$\int_{\psi(a)}^{\psi(b)}f(y)\,\mathrm{d} y=\int_a^bf(\psi(x))\,\psi'(x)\,\mathrm{d} x \tag{1.1}$$

enthält den Faktor $\psi'(x)$: Er sagt, wie stark $\psi$ ein kleines Stück $\mathrm{d} x$ streckt. In der Ebene legt eine Abbildung $\Phi$ ein Gitter über den Zielbereich $D$ (Abb. [1](#abb-1)). Jede kleine Zelle $Z$ im Bereich $B$ wird zu einer krummen Zelle $\Phi(Z)$ in $D$. Aus der Summe über $D$ wird eine Summe über $B$, und jede Zelle zählt mit ihrem Streckfaktor.

:::abbildung hm3/k4gitter 1
Die Abbildung $\Phi$ legt ein krummes Gitter über $D$. Die Zelle $Z$ wird zur Zelle $\Phi(Z)$. Die Pfeile sind die Spalten von $D\Phi$, multipliziert mit der Zellgröße. Sie spannen das Parallelogramm auf, das die krumme Zelle annähert.
:::

:::herleitung Woher der Faktor kommt
⁠**Baustein 1: Linearisieren.** Die Jacobi-Matrix $D\Phi$ aus [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) mit den Einträgen $\partial\Phi_j/\partial x_k$ ist die beste lineare Näherung von $\Phi$:

$$\Phi(\boldsymbol{x})=\Phi(\boldsymbol{x}_0)+D\Phi(\boldsymbol{x}_0)(\boldsymbol{x}-\boldsymbol{x}_0)+o(|\boldsymbol{x}-\boldsymbol{x}_0|).$$

Der Rest $o(\cdot)$ geht schneller gegen null als der Abstand. Auf einem kleinen Quader $Z$ um $\boldsymbol{x}_0$ wirkt $\Phi$ also fast wie die lineare Abbildung $D\Phi(\boldsymbol{x}_0)$ plus eine Verschiebung.

⁠**Baustein 2: Volumen einer Zelle.** Mit [(0.1)](von-grund-auf-determinante-und-volumen.html#gl-0-1) folgt für $\boldsymbol{x}_0\in Z$

$$\operatorname{vol}(\Phi(Z))\simeq|\det D\Phi(\boldsymbol{x}_0)|\,\operatorname{vol}(Z),\quad\text{falls }\operatorname{vol}(Z)\ll1.$$

⁠**Baustein 3: Riemann-Summe.** Zerlege $B$ in kleine Quader $Z_i$ mit Punkten $\boldsymbol{x}_i\in Z_i$. Die Bilder $\Phi(Z_i)$ zerlegen $D$, also

$$\int_Df(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}\approx\sum_if(\Phi(\boldsymbol{x}_i))\,\operatorname{vol}(\Phi(Z_i))\approx\sum_if(\Phi(\boldsymbol{x}_i))\,|\det D\Phi(\boldsymbol{x}_i)|\,\operatorname{vol}(Z_i).$$

Rechts steht eine Riemann-Summe, also Funktionswert mal Zellgröße, für ein Integral über $B$. Das Argument ist eine Näherung, aber es benutzt nirgends die Dimension.
:::

Die Zahl $\det D\Phi(\boldsymbol{x})$ heißt __Funktionaldeterminante__ oder Jacobi-Determinante von $\Phi$. Das exakte Ergebnis ist der __Transformationssatz__.

:::satz Satz 1.1 (Transformationssatz)
<span class="anker" id="satz-1-1"></span>

Sei $\mathcal G\subset\mathbb{R}^2$ ein Gebiet (offen und zusammenhängend) und $\Phi:\mathcal G\to\mathbb{R}^2$ stetig differenzierbar. Seien $B,D\subset\mathbb{R}^2$ reguläre Bereiche ([Teil 3](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/kurvenintegrale.html)) mit $B\subset\mathcal G$, und es gelte

$$\Phi:B\to D\text{ bijektiv}\quad\text{und}\quad\det D\Phi(\boldsymbol{x})\neq0\text{ für alle }\boldsymbol{x}\in B.$$

Dann gilt für jede stetige Funktion $f:D\to\mathbb{R}$

<span class="anker" id="gl-1-2"></span>
$$\int_Df(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}=\int_Bf(\Phi(\boldsymbol{x}))\,|\det D\Phi(\boldsymbol{x})|\,\mathrm{d}\boldsymbol{x}. \tag{1.2}$$
:::

⁠**So liest man das:** Links wird $f$ über den Zielbereich $D$ summiert. Rechts läuft $\boldsymbol{x}$ durch den bequemen Bereich $B$: $\Phi(\boldsymbol{x})$ ist der zugehörige Punkt in $D$, dort wird $f$ abgelesen, und $|\det D\Phi(\boldsymbol{x})|$ ist der Flächenfaktor der Zelle an dieser Stelle. Wegen $D=\Phi(B)$ schreibt man links auch $\int_{\Phi(B)}$. Für $f=1$ steht links die Fläche von $D$.

**Warum die Voraussetzungen.** Bijektiv heißt: Jeder Punkt von $D$ wird genau einmal getroffen, sonst zählen Zellen doppelt. Aus $\det D\Phi\neq0$ folgt, dass $\Phi$ keine Zelle zusammendrückt oder umklappt. Beides fehlt bei $\Phi(u,v)=(u^2,v)$ auf $B=[-1,1]\times[0,1]$: Die Abbildung klappt die linke Hälfte von $B$ auf die rechte, trifft $D=[0,1]^2$ also doppelt, und $\det D\Phi=2u$ verschwindet auf der Knicklinie $u=0$. Für $f=1$ gibt die linke Seite die Fläche 1, die rechte Seite $\int_0^1\!\int_{-1}^12|u|\,\mathrm{d} u\,\mathrm{d} v=2$. Die Formel ist dort falsch.

**Warum ein Betrag steht.** In [(1.1)](#gl-1-1) steht keiner, denn die Grenzen tragen das Vorzeichen mit: Fällt $\psi$, ist $\psi'<0$ und zugleich $\psi(a)>\psi(b)$. Beide Minuszeichen heben sich auf. In [(1.2)](#gl-1-2) wird dagegen über eine Menge ohne Durchlaufrichtung integriert, und jede Zelle zählt positiv.

**Beispiel.** Sei $D$ das Quadrat $0\le x+y\le2$, $0\le x-y\le2$ und $f(x,y)=x^2-y^2$. Die Ränder liegen schief, aber $u=x+y$ und $v=x-y$ laufen unabhängig von 0 bis 2, und $f=uv$. Umstellen gibt $\Phi(u,v)=\bigl(\frac{u+v}2,\frac{u-v}2\bigr)$ auf $B=[0,2]^2$ mit

$$D\Phi=\begin{pmatrix}\frac12&\frac12\\[1mm]\frac12&-\frac12\end{pmatrix},\qquad\det D\Phi=-\frac12,\qquad\int_D(x^2-y^2)\,\mathrm{d} x\,\mathrm{d} y=\frac12\int_0^2\!\!\int_0^2uv\,\mathrm{d} u\,\mathrm{d} v=2.$$

⁠**Kontrolle:** Für $f=1$ ergibt sich $\frac12\cdot4=2$. Das stimmt, denn $D$ ist ein Quadrat mit der Seitenlänge $\sqrt2$.

:::frage Ich kenne nur die neuen Variablen als Funktion der alten. Muss ich umstellen?
Für den Faktor nicht. Ist $T=\Phi^{-1}$, also $T(x,y)=(u,v)$, folgt aus $T\circ\Phi=\mathrm{id}$ mit der Kettenregel, dass $DT\,D\Phi$ die Einheitsmatrix ist, also $\det D\Phi=1/\det DT$. Im Beispiel ist $T(x,y)=(x+y,x-y)$ und $\det DT=-2$. Den Integranden musst du trotzdem in $u$ und $v$ schreiben.
:::

:::aufgabe Aufgabe 1 ★ Schiefes Parallelogramm
<span class="anker" id="aufg-1"></span>

Sei $D$ das Parallelogramm $1\le x+y\le3$, $0\le x-2y\le3$ und $T(x,y)=(x+y,\,x-2y)$.

<ol class="al">

<li>

Bestimme $\Phi=T^{-1}$ und beschreibe $B=T(D)$ durch Ungleichungen.

</li>

<li>

Berechne $|\det D\Phi|$ direkt und über $\det DT$.

</li>

<li>

Berechne $\int_D\frac{(x-2y)^2}{x+y}\,\mathrm{d} x\,\mathrm{d} y$.

</li>

</ol>

:::loesung
(a) Aus $u=x+y$, $v=x-2y$ folgt $\Phi(u,v)=\bigl(\frac{2u+v}3,\frac{u-v}3\bigr)$ und $B=\{1\le u\le3,\;0\le v\le3\}$. (b) Direkt: $\det D\Phi=\frac23\cdot(-\frac13)-\frac13\cdot\frac13=-\frac13$. Über $T$: $\det DT=-3$, also $|\det D\Phi|=\frac13$. (c) $\int_D\frac{(x-2y)^2}{x+y}\,\mathrm{d} x\,\mathrm{d} y=\frac13\int_1^3\frac{\mathrm{d} u}u\int_0^3v^2\,\mathrm{d} v=\frac13\cdot\ln3\cdot9=3\ln3\approx3{,}30$.
:::
:::

:::aufgabe Aufgabe 2 ★★ Bild eines Dreiecks
<span class="anker" id="aufg-2"></span>

Sei $B=\{(u,v):u\ge0,\;v\ge0,\;u+v\le1\}$ und $\Phi(u,v)=(u+v,\,u-v^2)$.

<ol class="al">

<li>

Berechne $\det D\Phi$. Warum ist die Determinante auf $B$ nie null?

</li>

<li>

Zeige, dass $\Phi$ auf $B$ injektiv ist. Tipp: Bilde $x-y$.

</li>

<li>

Berechne die Fläche von $\Phi(B)$.

</li>

</ol>

:::loesung
(a) $\det D\Phi=\det\begin{pmatrix}1&1\\1&-2v\end{pmatrix}=-2v-1$. Wegen $v\ge0$ ist das höchstens $-1$, also nie null. (b) Aus $x=u+v$, $y=u-v^2$ folgt $x-y=v+v^2$. Das wächst für $v\ge0$ streng, also bestimmt $x-y$ den Wert $v$, und dann ist $u=x-v$. (c) $\int_B(1+2v)\,\mathrm{d} u\,\mathrm{d} v=\int_0^1(1+2v)(1-v)\,\mathrm{d} v=\int_0^1(1+v-2v^2)\,\mathrm{d} v=1+\frac12-\frac23=\frac56$.
:::
:::
