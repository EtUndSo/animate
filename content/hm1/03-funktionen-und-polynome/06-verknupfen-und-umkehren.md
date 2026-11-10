---
title: Stufe 4: Verknüpfen und Umkehren
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
order: 1230600
summary: Stufe 3 sagt, wann f(x)=y genau eine Lösung hat.
tags: Summe, Differenz, Produkt, Quotient, Komposition, n-te Wurzel
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Stufe [3](ruckwarts-injektiv-surjektiv-bijektiv.html#stufe-3) sagt, wann $f(x)=y$ genau eine Lösung hat. Diese Stufe macht aus der Lösung eine Funktion. Dazu muss man Funktionen hintereinander ausführen können.
:::

**Die Idee.** Die Umkehrfunktion macht rückgängig, was $f$ tut: Erst $f$, dann $g$ führt zurück zum Anfang, und erst $g$, dann $f$ ebenso (Abb. [5](#abb-5), links). Aus Funktionen entstehen so neue Funktionen, wie aus Zahlen durch Rechnen neue Zahlen.

:::definition Definition 4.1 (Verknüpfungen)
<span class="anker" id="satz-4-1"></span>

Für reelle Funktionen $f,g$ sei $M:=\mathcal D(f)\cap\mathcal D(g)$ und $M':=\{x\in M:g(x)\neq0\}$. Dann sind __Summe__, __Differenz__ und __Produkt__ auf $M$ und der __Quotient__ auf $M'$ erklärt durch

<span class="anker" id="gl-4-1"></span>
$$(f\pm g)(x):=f(x)\pm g(x),\qquad(f\cdot g)(x):=f(x)\cdot g(x),\qquad\Bigl(\frac fg\Bigr)(x):=\frac{f(x)}{g(x)}. \tag{4.1}$$

Für $f:A\to B$ und $g:B\to C$ ist die __Komposition__ oder Hintereinanderausführung $g\circ f:A\to C$ erklärt durch

<span class="anker" id="gl-4-2"></span>
$$(g\circ f)(x):=g\bigl(f(x)\bigr)\quad\text{für alle }x\in A. \tag{4.2}$$
:::

⁠**So liest man das:** $g\circ f$ spricht man „$g$ nach $f$“: $f$ wirkt zuerst, $f(x)$ liegt in $B$, dort darf $g$ wirken. Der Graph ist $\{(x,y)\in A\times C:\text{es gibt }z\in B\text{ mit }f(x)=z,\ g(z)=y\}$. Die Reihenfolge zählt: Für $f(x)=2x$, $g(x)=x+1$ ist $(g\circ f)(1)=3$, aber $(f\circ g)(1)=4$. Summe und Produkt rechnet man Stelle für Stelle aus, etwa $(h/b)(2)=-1/0{,}2=-5$.

:::satz Satz 4.2 (Charakterisierung von injektiv, surjektiv, bijektiv)
<span class="anker" id="satz-4-2"></span>

Sei $f:A\to B$ eine Funktion, $A$ nicht leer. Dann gilt:

<ol class="rm">

<li>

$f$ injektiv $\Leftrightarrow$ es gibt $g:B\to A$ mit $(g\circ f)(x)=x$ für alle $x\in A$ (I).

</li>

<li>

$f$ surjektiv $\Leftrightarrow$ es gibt $g:B\to A$ mit $(f\circ g)(y)=y$ für alle $y\in B$ (S).

</li>

<li>

$f$ bijektiv $\Leftrightarrow$ es gibt genau eine Funktion $g:B\to A$ mit (I) und (S).

</li>

</ol>
:::

:::beweis Charakterisierung
(i) „$\Leftarrow$“: Aus $f(x_1)=f(x_2)$ folgt $x_1=g(f(x_1))=g(f(x_2))=x_2$. „$\Rightarrow$“ als Idee: $g$ gibt jedem $y\in\mathcal W(f)$ sein einziges Urbild und allen anderen $y$ einen festen Wert aus $A$.

(ii) „$\Leftarrow$“: Zu $y\in B$ setze $z:=g(y)\in A$, dann ist $f(z)=(f\circ g)(y)=y$, also $y\in\mathcal W(f)$. „$\Rightarrow$“ als Idee: $g$ wählt zu jedem $y$ eines seiner Urbilder.

(iii) „$\Leftarrow$“: (I) ergibt injektiv, (S) ergibt surjektiv. „$\Rightarrow$“: Bijektiv heißt, jedes $y$ hat genau ein Urbild $g(y)$, dieses $g$ erfüllt (I) und (S). Erfüllt auch $\hat g$ beide, ist $\hat g(y)=\hat g\bigl(f(g(y))\bigr)=g(y)$ nach (S) für $g$ und (I) für $\hat g$.
:::

⁠**So liest man das:** Merkhilfe: Bei „surjektiv“ geht es um die Bilder, also steht (S) für alle $y\in B$. **Warum „bijektiv“ für die Eindeutigkeit nötig ist:** $h:\mathbb{R}\to[-1,\infty)$ ist nur surjektiv, und sowohl $g_1(y)=2+\sqrt{y+1}$ als auch $g_2(y)=2-\sqrt{y+1}$ erfüllen (S). $h:[2,\infty)\to\mathbb{R}$ ist nur injektiv, und $g(y)=2+\sqrt{y+1}$ für $y\ge-1$, $g(y)=c$ für $y<-1$ erfüllt (I) für jedes feste $c\ge2$.

:::definition Definition 4.3 (Umkehrfunktion und Wurzel)
<span class="anker" id="satz-4-3"></span>

Die Funktion $g$ aus Satz [4.2](#satz-4-2)(iii) heißt Umkehrfunktion von $f$, geschrieben $f^{-1}:=g$. Für alle $x\in A$, $y\in B$ gilt

<span class="anker" id="gl-4-3"></span>
$$f(x)=y\ \Leftrightarrow\ x=f^{-1}(y),\qquad f^{-1}\bigl(f(x)\bigr)=x,\qquad f\bigl(f^{-1}(y)\bigr)=y. \tag{4.3}$$

Die Umkehrfunktion von $x\mapsto x^n$ (auf $\mathbb{R}_0^+$ für gerades $n$, auf $\mathbb{R}$ für ungerades $n$) heißt __$n$-te Wurzel__, $f^{-1}(y)=\sqrt[n]{y}=y^{1/n}$.
:::

⁠**So liest man das:** Die erste Aussage sagt: $f^{-1}$ löst die Gleichung $f(x)=y$. Beweis: Aus $f(x)=y$ folgt $x=g(f(x))=g(y)$ nach (I), aus $g(y)=x$ folgt $y=f(g(y))=f(x)$ nach (S). Für die Wurzel lauten die beiden anderen Aussagen $\sqrt[n]{y^n}=y$ und $(\sqrt[n]{y})^n=y$. **Achtung:** $f^{-1}(y)$ ist nicht $1/f(y)$. Für $h$ auf $[2,\infty)$ ist $h^{-1}(8)=5$, aber $1/h(8)=1/35$.

**Der Graph.** Wegen [(4.3)](#gl-4-3) ist $\mathcal G(f)=\{(x,f(x))\}=\{(g(y),y):y\in B\}$, während $\mathcal G(g)=\{(y,g(y)):y\in B\}$ ist. Die Paare sind vertauscht, und Vertauschen der Koordinaten ist die Spiegelung an der Winkelhalbierenden $\{(x,y)\in\mathbb{R}^2:x=y\}$ (Abb. [5](#abb-5), rechts).

:::abbildung hm1/k3spiegel 5
Links der Hin- und Rückweg für $h$ auf $[2,\infty)$: $h(5)=8$ und $h^{-1}(8)=5$. Rechts die Graphen von $h$ und $h^{-1}(y)=2+\sqrt{y+1}$: Der Punkt $(4\,|\,3)$ geht durch Spiegeln an der gestrichelten Geraden in $(3\,|\,4)$ über.
:::

:::satz Satz 4.4 (Monotonie vererbt sich)
<span class="anker" id="satz-4-4"></span>

Sei $f:A\to B$ reell, surjektiv und streng monoton wachsend (fallend). Dann existiert $g=f^{-1}:B\to A$ und ist ebenfalls streng monoton wachsend (fallend).
:::

:::beweis Monotonie vererbt sich
Für wachsendes $f$ (fallend geht gleich): $f$ ist injektiv wie in Satz [3.2](ruckwarts-injektiv-surjektiv-bijektiv.html#satz-3-2) und surjektiv, also existiert $g$. Sei $y_1<y_2$. Wäre $g(y_1)\ge g(y_2)$, ergäbe Anwenden von $f$ den Widerspruch $y_1\ge y_2$. Also $g(y_1)<g(y_2)$.
:::

⁠**So liest man das und warum die Voraussetzungen nötig sind:** Ohne „surjektiv“ fehlt $g$ für manche $y\in B$. Ohne Monotonie gibt es auch nichts zu vererben. **Anwendung:** $\sqrt[n]{y}$ ist streng monoton wachsend. **Grenzfall:** Für $f(x)=x$ ist $f^{-1}=f$, der Graph liegt auf der Spiegelachse.

:::frage Warum steht in [(4.3)](#gl-4-3) für die Wurzel nicht $\sqrt{y^2}=y$ für alle $y$?
Weil die Umkehrung nur zur Funktion auf $\mathbb{R}_0^+$ gehört. Für $y=-3$ ist $\sqrt{(-3)^2}=3$, also allgemein $\sqrt{y^2}=|y|$. Der Fehler entsteht, wenn man den Definitionsbereich vergisst, in dem $f$ umkehrbar ist.
:::

:::aufgabe Aufgabe 4 ★★ Eine Umkehrfunktion bestimmen
<span class="anker" id="aufg-4"></span>

Sei $f:[2,\infty)\to(2,5]$, $f(x)=\dfrac{2x+1}{x-1}=2+\dfrac{3}{x-1}$. (a) Zeige, dass $f$ streng monoton fällt. (b) Bestimme $f^{-1}$. (c) Vergleiche $f^{-1}(4)$ mit $1/f(4)$. (d) Vorhersage: Ist $f^{-1}$ wachsend oder fallend? Prüfe mit $y=3$ und $y=4$.

:::loesung
(a) Aus $2\le x_1<x_2$ folgt $0<x_1-1<x_2-1$, also $\frac{3}{x_1-1}>\frac{3}{x_2-1}$ und $f(x_1)>f(x_2)$. (b) Aus $y=2+\frac{3}{x-1}$ folgt $x-1=\frac{3}{y-2}$, also $f^{-1}(y)=1+\frac{3}{y-2}=\frac{y+1}{y-2}$ für $y\in(2,5]$. (c) $f^{-1}(4)=\frac52$ (Probe: $f(\frac52)=6/1{,}5=4$), dagegen $1/f(4)=\frac13$. (d) Fallend nach Satz [4.4](#satz-4-4): $f^{-1}(3)=4>f^{-1}(4)=\frac52$.
:::
:::

:::aufgabe Aufgabe 5 ★★★ Umkehren einer Kette
<span class="anker" id="aufg-5"></span>

Seien $f(x)=2x+1$, $g(x)=x^3$ auf $\mathbb{R}$. (a) Berechne $(g\circ f)(1)$ und $(f\circ g)(1)$. (b) Zeige allgemein für bijektive $f:A\to B$, $g:B\to C$: $(g\circ f)^{-1}=f^{-1}\circ g^{-1}$. Warum dreht sich die Reihenfolge um? (c) Bestimme $(g\circ f)^{-1}(y)$ und prüfe mit $y=27$.

:::loesung
(a) $(g\circ f)(1)=g(3)=27$, $(f\circ g)(1)=f(1)=3$. (b) $f^{-1}\bigl(g^{-1}(g(f(x)))\bigr)=f^{-1}(f(x))=x$, ebenso in der anderen Reihenfolge für $y\in C$. Damit gelten (I) und (S), und nach Satz [4.2](#satz-4-2)(iii) gibt es nur eine solche Funktion. Der Rückweg muss den letzten Schritt zuerst rückgängig machen. (c) $g^{-1}(y)=\sqrt[3]{y}$, $f^{-1}(y)=\frac{y-1}{2}$, also $(g\circ f)^{-1}(y)=\frac{\sqrt[3]{y}-1}{2}$. Bei $y=27$: $(3-1)/2=1$.
:::
:::
