---
title: Stufe 8: Zwischenwerte, Nullstellen, Umkehrfunktion
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1251000
summary: Maximum und Minimum werden angenommen.
tags: Nullstelle, Intervallhalbierungsmethode, Sekantenverfahren, Sekante, Fixpunkt
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Maximum und Minimum werden angenommen. Offen ist, was dazwischen geschieht: Wird jeder Wert getroffen? Das liefert Nullstellen, ein Rechenverfahren für sie und stetige Umkehrfunktionen ohne Formel.
:::

**Die Idee.** Ist $f$ links negativ und rechts positiv, behält man beim Halbieren die Hälfte mit Vorzeichenwechsel. Die Intervalle schrumpfen auf einen Punkt $x_0$, beliebig nah daneben liegen Stellen mit $f<0$ und mit $f>0$. Stetigkeit lässt für $f(x_0)$ nur die 0.

:::satz Satz 8.1 (Zwischenwertsatz von Bolzano)
<span class="anker" id="satz-8-1"></span>

Sei $f:[a,b]\to\mathbb{R}$ stetig.

<ol class="rm">

<li>

Wenn $f(a)\cdot f(b)<0$, dann hat $f$ eine __Nullstelle__ in $(a,b)$: Es gibt $x_0\in(a,b)$ mit $f(x_0)=0$.

</li>

<li>

Mit $m:=\inf\mathcal W(f)$ und $M:=\sup\mathcal W(f)$ gilt

<span class="anker" id="gl-8-1"></span>
$$\mathcal W(f)=[m,M], \tag{8.1}$$

das heißt: Zu jedem $\mu\in[m,M]$ gibt es ein $x\in[a,b]$ mit $f(x)=\mu$.

</li>

</ol>
:::

:::beweis Halbieren (i), Verschieben (ii)
(i) Sei etwa $f(a)<0<f(b)$ (sonst betrachte $-f$). Ist $f(\frac{a+b}2)=0$, sind wir fertig. Ist der Wert positiv, nimm $[a_1,b_1]:=[a,\frac{a+b}2]$, ist er negativ, $[a_1,b_1]:=[\frac{a+b}2,b]$. In jedem Fall gilt wieder $f(a_1)<0<f(b_1)$. Fortsetzen ergibt entweder nach endlich vielen Schritten eine Nullstelle oder eine Intervallschachtelung mit $f(a_n)<0<f(b_n)$ und $b_n-a_n=2^{-n}(b-a)$. Sie definiert ein $x_0\in[a,b]$ mit $a_n\to x_0$, $b_n\to x_0$. Die Folgenstetigkeit gibt

$$0\ge\lim_{n\to\infty}f(a_n)=f(x_0)=\lim_{n\to\infty}f(b_n)\ge0.$$

Also ist $f(x_0)=0$, und wegen $f(a),f(b)\ne0$ liegt $x_0$ in $(a,b)$.

(ii) „$\subset$“ gilt nach Definition von $m$ und $M$. „$\supset$“: Nach dem Satz vom Maximum gibt es $x_0,x_1$ mit $f(x_0)=m$, $f(x_1)=M$, also $m,M\in\mathcal W(f)$. Sei $\mu\in(m,M)$ und etwa $x_0<x_1$. Dann ist $g(x):=f(x)-\mu$ auf $[x_0,x_1]$ stetig mit $g(x_0)<0<g(x_1)$, und (i) gibt $\bar x$ mit $g(\bar x)=0$, also $f(\bar x)=\mu$.
:::

⁠**So liest man das:** (ii) sagt: Das Bild eines abgeschlossenen Intervalls ist wieder ein abgeschlossenes Intervall.

::::beispiel [Beispiele]
$k$ ist stetig mit $k(0)=1<2<3{,}718=k(1)$. Also gibt es $x^*\in(0,1)$ mit $k(x^*)=2$. Eindeutig wird es erst dadurch, dass $k$ streng wächst. Auch die Surjektivität von $\exp$ aus Stufe [2](wachstum-logarithmus-allgemeine-potenz.html#stufe-2) folgt so: Zu $y>0$ gibt es $n$ mit $\mathrm{e}^{-n}<y$, und es ist $\mathrm{e}^y>y$. Also hat $\mathrm{e}^x-y$ auf $[-n,y]$ eine Nullstelle. **Voraussetzungen nötig:** Ohne Stetigkeit: $H$ auf $[-1,1]$ lässt den Wert $\frac12$ aus. Ohne Intervall: $1/x$ auf $[-1,0)\cup(0,1]$ ist stetig, wechselt das Vorzeichen und hat keine Nullstelle.
::::

⁠**Grenzfall:** $f(a)=0$ gibt eine Nullstelle am Rand, deshalb verlangt (i) ein echtes $<$.

**Polynome ungeraden Grades.** Jedes reelle Polynom $P_{2n-1}$, $n\in\mathbb{N}$, hat mindestens eine reelle Nullstelle. Ist der führende Koeffizient positiv, gilt $P(x)\to+\infty$ für $x\to\infty$ und $P(x)\to-\infty$ für $x\to-\infty$, weil die höchste Potenz überwiegt. Es gibt also $a<b$ mit $P(a)<0<P(b)$, und (i) greift. Sonst betrachtet man $-P$. Bei geradem Grad geht das nicht: $x^2+1$ hat keine.

:::satz Satz 8.2 (Stetigkeit der Umkehrfunktion)
<span class="anker" id="satz-8-2"></span>

Sei $f:[a,b]\to\mathbb{R}$ stetig und streng monoton wachsend. Setze $A:=f(a)$, $B:=f(b)$. Dann ist $f:[a,b]\to[A,B]$ bijektiv, und die Umkehrfunktion $g=f^{-1}:[A,B]\to[a,b]$ ist ebenfalls streng monoton wachsend und stetig.
:::

:::beweis Surjektiv durch Zwischenwerte, stetig durch Einklemmen
Aus $a<x<b$ folgt $A<f(x)<B$, also $\mathcal W(f)\subset[A,B]$, und [(8.1)](#gl-8-1) gibt $\mathcal W(f)=[A,B]$. Bijektivität und Monotonie von $g$ sind aus [Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html) bekannt. Stetigkeit bei $y_0\in(A,B)$, $x_0:=g(y_0)$: Sei $\varepsilon>0$ so klein, dass $[x_0-\varepsilon,x_0+\varepsilon]\subset[a,b]$. Dann ist $f(x_0-\varepsilon)<y_0<f(x_0+\varepsilon)$, und $\delta_0:=\min\{y_0-f(x_0-\varepsilon),\ f(x_0+\varepsilon)-y_0\}>0$. Für $|y-y_0|<\delta_0$ gilt $f(x_0-\varepsilon)<y<f(x_0+\varepsilon)$, und Anwenden von $g$ gibt $x_0-\varepsilon<g(y)<x_0+\varepsilon$. Am Rand läuft es einseitig genauso.
:::

⁠**So liest man das:** Anders als in [Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html) muss man die Surjektivität nicht fordern. Für streng fallende $f$ gilt alles entsprechend. Ebenso für $f:(a,b)\to\mathbb{R}$ stetig und streng monoton, auch mit $a=-\infty$ oder $b=\infty$: Man schöpft $(a,b)$ durch Intervalle $[a_n,b_n]$ aus.

::::beispiel [Beispiele]
$\log$ ist auf $\mathbb{R}^+$ stetig, denn $\exp$ ist stetig und streng wachsend. $\sqrt[n]{x}$ ist auf $\mathbb{R}_0^+$ stetig. Auch $k^{-1}:[1;\ 3{,}718]\to[0,1]$ ist stetig (Abb. [8](#abb-8)), obwohl die bisherigen Funktionen keine Formel dafür liefern. **Voraussetzungen nötig:** Ohne Intervall kann $g$ springen: $f(x)=x$ auf $[0,1]$, $f(x)=x-1$ auf $(2,3]$ ist stetig und streng wachsend mit $\mathcal W(f)=[0,2]$, aber $g$ springt bei $y=1$ von 1 auf 2. Ohne strenge Monotonie gibt es keine Umkehrfunktion: $x^2$ auf $[-1,1]$.

:::abbildung hm1/k5zws 8
Links trifft $k$ den Wert $\mu=2$ bei $x^*=0{,}4429$. Rechts $k$ und die Spiegelung $k^{-1}$ an $y=x$.
:::
::::

**Nullstellen berechnen.** Das Halbieren aus dem Beweis, die __Intervallhalbierungsmethode__, ist anders als der Beweis des Satzes vom Maximum konstruktiv: Der neue Rand $\frac{a_{n-1}+b_{n-1}}2$ ist berechenbar, $[a_n,b_n]\subset[a_{n-1},b_{n-1}]$, und $\lim a_n=\lim b_n$ liefert die Nullstelle. Der Fehler nach $n$ Schritten ist höchstens $2^{-n}(b-a)$, zehn Schritte geben drei Dezimalstellen.

Das __Sekantenverfahren__ (regula falsi) wählt die Teilstelle geschickter: Statt $f$ bei $\frac{a+b}2$ wertet man $f$ an der Nullstelle $\alpha$ der __Sekante__ aus, der Geraden durch $(a\,|\,f(a))$ und $(b\,|\,f(b))$:

<span class="anker" id="gl-8-2"></span>
$$P_1(x):=f(a)+\frac{f(b)-f(a)}{b-a}\,(x-a),\qquad\alpha:=a-\frac{b-a}{f(b)-f(a)}\cdot f(a). \tag{8.2}$$

Dann setzt man $[a_1,b_1]:=[a,\alpha]$, falls $f(a)\cdot f(\alpha)<0$, und $[a_1,b_1]:=[\alpha,b]$, falls $f(\alpha)\cdot f(b)<0$.

::::beispiel mit dem Rechenmodell
Für $p(x)=k(x)-2$ auf $[0,1]$ ist $p(0)=-1$, $p(1)=\mathrm{e}-1=1{,}718$, und der erste Sekantenschritt gibt $\alpha=\frac{1}{\mathrm{e}}=0{,}3679$.

| Schritt | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Halbieren, neuer Punkt | 0,5 | 0,25 | 0,375 | 0,4375 | 0,4688 | 0,4531 |
| Sekante, neuer Punkt | 0,3679 | 0,4301 | 0,4407 | 0,4425 | 0,4428 | 0,4428 |

Die Lösung ist $x^*=0{,}44285$. Nach sechs Schritten liegt die Sekante nur $1{,}1\cdot10^{-5}$ daneben, die Halbierung kennt $x^*$ auf $0{,}016$ genau. Dafür ist ihr Fehler vorab bekannt (Abb. [9](#abb-9)).

:::abbildung hm1/k5nullstelle 9
Links die ersten vier Intervalle der Halbierung für $p$. Mitte die zwei ersten Sekanten mit den Achsenschnitten $0{,}3679$ und $0{,}4301$. Rechts schneidet $\mathrm{e}^{-x}$ die Winkelhalbierende im Fixpunkt $0{,}5671$.
:::
::::

:::definition Definition 8.3 (Fixpunkt)
<span class="anker" id="satz-8-3"></span>

Sei $f:M\to\mathbb{R}$, $M\subset\mathbb{R}$ und $x_0\in M$. Dann heißt $x_0$ __Fixpunkt__ von $f$, wenn

<span class="anker" id="gl-8-3"></span>
$$f(x_0)=x_0. \tag{8.3}$$
:::

⁠**So liest man das:** Fixpunkte sind die Schnittpunkte des Graphen mit der Winkelhalbierenden $\{y=x\}$. $x_0$ ist genau dann Fixpunkt, wenn $g(x):=f(x)-x$ dort eine Nullstelle hat.

:::satz Satz 8.4 (Fixpunktsatz)
<span class="anker" id="satz-8-4"></span>

Sei $f:[a,b]\to\mathbb{R}$ stetig mit $\mathcal W(f)\subset[a,b]$. Dann hat $f$ mindestens einen Fixpunkt.
:::

:::beweis Zwischenwertsatz für $g=f-x$
$g(x):=f(x)-x$ ist stetig. Wegen $f(a)\ge a$ und $f(b)\le b$ ist $g(a)\ge0\ge g(b)$. Ist eine davon 0, ist der Rand ein Fixpunkt. Sonst gibt Satz [8.1](#satz-8-1) (i) ein $x_0$ mit $g(x_0)=0$.
:::

⁠**So liest man das:** Der Graph startet über der Winkelhalbierenden und endet unter ihr.

::::beispiel
$f(x)=\mathrm{e}^{-x}$ bildet $[0,1]$ auf $[\frac{1}{\mathrm{e}},1]$ ab, der Fixpunkt ist $0{,}5671$ (Abb. [9](#abb-9), rechts). **Voraussetzungen nötig:** $x+1$ auf $[0,1]$ verlässt das Intervall, $1-H(x-\frac12)$ auf $[0,1]$ springt über die Winkelhalbierende. Beide haben keinen Fixpunkt.
::::

:::aufgabe Aufgabe 8 ★★ Nullstellen einschließen
<span class="anker" id="aufg-8"></span>

(a) Berechne für $P(x)=x^5-3x+1$ die Werte $P(-2)$, $P(0)$, $P(1)$, $P(2)$. Wie viele Nullstellen sichert der Zwischenwertsatz? (b) Warum ist $f(x)=x^3+x$ auf $[0,2]$ umkehrbar? Berechne $f^{-1}(2)$ und gib den Definitionsbereich von $f^{-1}$ an.

:::loesung
(a) $P(-2)=-25$, $P(0)=1$, $P(1)=-1$, $P(2)=27$. Drei Vorzeichenwechsel in $(-2,0)$, $(0,1)$, $(1,2)$: mindestens drei Nullstellen. (b) $f$ ist stetig und streng wachsend, $A=0$, $B=10$. $f(1)=2$, also $f^{-1}(2)=1$, und $f^{-1}:[0,10]\to[0,2]$.
:::
:::

:::aufgabe Aufgabe 9 ★★ Beide Verfahren von Hand
<span class="anker" id="aufg-9"></span>

Sei $f(x)=x^3+x-1$ auf $[0,1]$. (a) Führe drei Halbierungsschritte aus. (b) Führe zwei Sekantenschritte aus. (c) Wie viele Halbierungen sichern einen Fehler unter $10^{-6}$?

:::loesung
(a) $f(0)=-1$, $f(1)=1$. $f(0{,}5)=-0{,}375$: $[0{,}5;1]$. $f(0{,}75)=0{,}1719$: $[0{,}5;\,0{,}75]$. $f(0{,}625)=-0{,}1309$: $[0{,}625;\,0{,}75]$. (b) $\alpha_1=0-\frac1{2}\cdot(-1)=0{,}5$ mit $f=-0{,}375$: $[0{,}5;1]$. $\alpha_2=0{,}5+\frac{0{,}5}{1{,}375}\cdot0{,}375=0{,}6364$ mit $f=-0{,}1059$. (c) $2^{-n}<10^{-6}$ verlangt $n\ge20$, denn $2^{20}=1048576$.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Fixpunkt und Gleichmäßigkeit
<span class="anker" id="aufg-10"></span>

(a) Zeige, dass $f(x)=\frac{x^2+1}3$ das Intervall $[0,1]$ in sich abbildet, und berechne den Fixpunkt. (b) Warum hat $g(x)=\frac12(1+x)$ auf $[0,1)$ keinen Fixpunkt? Welche Voraussetzung fehlt? (c) Zeige mit $x=n$, $y=n+\frac1n$, dass $x^2$ auf $\mathbb{R}$ nicht gleichmäßig stetig ist.

:::loesung
(a) Auf $[0,1]$ ist $\frac13\le f(x)\le\frac23$, also $\mathcal W(f)\subset[0,1]$. $x^2-3x+1=0$ gibt $x=\frac{3-\sqrt5}2=0{,}382$; die zweite Lösung $2{,}618$ liegt außerhalb. (b) $g(x)=x$ gibt $x=1\notin[0,1)$. Das Intervall ist nicht abgeschlossen. (c) $|x-y|=\frac1n\to0$, aber $|x^2-y^2|=2+\frac1{n^2}\ge2$. Für $\varepsilon=2$ gewinnt kein $\delta_0$.
:::
:::

::::formelsammlung
**Zwischenwertsatz: Nullstelle**

$$f(a)\cdot f(b)<0\quad\Longrightarrow\quad f(x_0)=0\ \text{für ein }x_0\in(a,b)$$

Für $f:[a,b]\to\mathbb{R}$ stetig. Beweis durch Halbieren.

**Zwischenwertsatz: Wertebereich**

$$\mathcal W(f)=[m,M]$$

Mit $m:=\inf\mathcal W(f)$ und $M:=\sup\mathcal W(f)$: Zu jedem $\mu\in[m,M]$ gibt es ein $x\in[a,b]$ mit $f(x)=\mu$.

**Fehler der Intervallhalbierung**

$$b_n-a_n=2^{-n}(b-a)$$

Neuer Rand $\frac{a_{n-1}+b_{n-1}}2$; der Fehler nach $n$ Schritten ist höchstens $2^{-n}(b-a)$.

**Sekante**

$$P_1(x):=f(a)+\frac{f(b)-f(a)}{b-a}\,(x-a),\qquad\alpha:=a-\frac{b-a}{f(b)-f(a)}\cdot f(a)$$

Dann $[a_1,b_1]:=[a,\alpha]$, falls $f(a)\cdot f(\alpha)<0$, und $[a_1,b_1]:=[\alpha,b]$, falls $f(\alpha)\cdot f(b)<0$.

**Stetigkeit der Umkehrfunktion**

$$g=f^{-1}:[A,B]\to[a,b]$$

Für $f:[a,b]\to\mathbb{R}$ stetig und streng monoton wachsend, $A:=f(a)$, $B:=f(b)$: $f:[a,b]\to[A,B]$ ist bijektiv, $g$ streng monoton wachsend und stetig.

**Fixpunkt**

$$f(x_0)=x_0$$

Schnittpunkt des Graphen mit der Winkelhalbierenden; gleichbedeutend hat $g(x):=f(x)-x$ dort eine Nullstelle.

**Fixpunktsatz**

$$\mathcal W(f)\subset[a,b]$$

Ist $f:[a,b]\to\mathbb{R}$ stetig mit $\mathcal W(f)\subset[a,b]$, so hat $f$ mindestens einen Fixpunkt.
::::

::::lernkarten
:::karte formel Zwischenwertsatz
Was besagt der Zwischenwertsatz von Bolzano für eine stetige Funktion $f:[a,b]\to\mathbb{R}$?
---
(i) Aus $f(a)\cdot f(b)<0$ folgt eine Nullstelle $x_0\in(a,b)$. (ii) Mit $m:=\inf\mathcal W(f)$ und $M:=\sup\mathcal W(f)$ gilt $\mathcal W(f)=[m,M]$: Das Bild eines abgeschlossenen Intervalls ist wieder ein abgeschlossenes Intervall.
--- falsch
(i) Aus $f(a)\cdot f(b)<0$ folgt eine Nullstelle in $(a,b)$. (ii) Jeder Wert zwischen $f(a)$ und $f(b)$ wird angenommen, aber keiner außerhalb: $\mathcal W(f)$ ist genau das Intervall zwischen $f(a)$ und $f(b)$.
--- falsch
(i) Aus $f(a)\cdot f(b)>0$ folgt, dass $f$ in $(a,b)$ keine Nullstelle hat. (ii) Mit $m:=\inf\mathcal W(f)$ und $M:=\sup\mathcal W(f)$ gilt $\mathcal W(f)=(m,M)$, die beiden Ränder werden nicht angenommen.
--- falsch
(i) Aus $f(a)\cdot f(b)<0$ folgt genau eine Nullstelle in $(a,b)$. (ii) Mit $m:=\inf\mathcal W(f)$ und $M:=\sup\mathcal W(f)$ gilt $\mathcal W(f)=[m,M]$, und jeder Wert wird genau einmal angenommen.
:::
:::karte herleitung Halbieren bis zur Nullstelle
Wie beweist man durch Halbieren, dass eine stetige Funktion mit $f(a)<0<f(b)$ eine Nullstelle in $(a,b)$ hat?
---
Ist $f(\frac{a+b}2)=0$, ist man fertig; ist der Wert positiv, nimmt man $[a,\frac{a+b}2]$, ist er negativ, $[\frac{a+b}2,b]$, weil dann wieder $f(a_1)<0<f(b_1)$ gilt.
---
Fortsetzen liefert eine Nullstelle oder eine Intervallschachtelung mit $f(a_n)<0<f(b_n)$ und $b_n-a_n=2^{-n}(b-a)$, weil jeder Schritt die Länge halbiert.
---
Sie definiert ein $x_0\in[a,b]$ mit $a_n\to x_0$ und $b_n\to x_0$, weil geschachtelte Intervalle mit Längen gegen 0 genau einen Punkt enthalten.
---
Die Folgenstetigkeit gibt $0\ge\lim_{n\to\infty}f(a_n)=f(x_0)=\lim_{n\to\infty}f(b_n)\ge0$, weil alle $f(a_n)$ negativ und alle $f(b_n)$ positiv sind; also ist $f(x_0)=0$.
---
$x_0$ liegt in $(a,b)$, weil $f(a)\ne0$ und $f(b)\ne0$ ist.
:::
:::karte zusammenhang Nullstelle
Warum verlangt der Zwischenwertsatz in (i) das echte $f(a)\cdot f(b)<0$, um eine Nullstelle in $(a,b)$ zu sichern?
---
Bei $f(a)=0$ liegt eine Nullstelle am Rand; im Inneren $(a,b)$ muss es dann keine geben. Mit dem echten $<$ sind $f(a)$ und $f(b)$ nicht null und haben verschiedene Vorzeichen, also liegt die gefundene Nullstelle im Inneren.
--- falsch
Weil bei $f(a)\cdot f(b)=0$ die Funktion auf ganz $[a,b]$ null ist; der Satz wäre dann trivial, und man schließt diesen Fall nur der Übersicht halber aus, ohne dass sich an der Aussage etwas ändern würde.
--- falsch
Weil das Produkt bei einer Nullstelle am Rand positiv wird; mit $\le0$ würde man deshalb Funktionen ohne jeden Vorzeichenwechsel zulassen, die im ganzen Intervall nie eine Nullstelle haben.
--- falsch
Weil die Halbierung bei $f(a)\cdot f(b)=0$ nicht startet: Man weiß dann nicht, welche Hälfte man behalten soll, und das Verfahren findet die Nullstelle am Rand deshalb nie, auch nicht nach vielen Schritten.
:::
:::karte zusammenhang Voraussetzungen des Zwischenwertsatzes
Welche Beispiele zeigen, dass der Zwischenwertsatz die Stetigkeit und ein Intervall als Definitionsbereich braucht?
---
Ohne Stetigkeit: $H$ auf $[-1,1]$ lässt den Wert $\frac12$ aus. Ohne Intervall: $1/x$ auf $[-1,0)\cup(0,1]$ ist stetig, wechselt das Vorzeichen und hat keine Nullstelle.
--- falsch
Ohne Stetigkeit: $x^2+1$ auf $[-1,1]$ hat keine Nullstelle. Ohne Intervall: $H$ auf $[-1,1]$ lässt den Wert $\frac12$ aus, weil die Stelle 0 im Definitionsbereich fehlt.
--- falsch
Ohne Stetigkeit: $1/x$ auf $[-1,0)\cup(0,1]$ springt bei 0 und hat keine Nullstelle. Ohne Intervall: $x^2$ auf $[-1,1]$ nimmt die negativen Werte nicht an.
--- falsch
Es gibt keine solchen Beispiele: Jede Funktion mit Werten beider Vorzeichen hat eine Nullstelle; die Voraussetzungen erleichtern nur den Beweis durch Halbieren.
:::
:::karte zusammenhang Polynome ungeraden Grades
Warum hat jedes reelle Polynom ungeraden Grades mindestens eine reelle Nullstelle, eines geraden Grades aber nicht unbedingt?
---
Bei positivem führenden Koeffizienten überwiegt die höchste Potenz: $P(x)\to+\infty$ für $x\to\infty$ und $P(x)\to-\infty$ für $x\to-\infty$. Also gibt es $a<b$ mit $P(a)<0<P(b)$, und der Zwischenwertsatz greift. Bei geradem Grad geht das nicht: $x^2+1$ hat keine.
--- falsch
Weil Polynome ungeraden Grades streng monoton sind und deshalb jeden reellen Wert genau einmal annehmen, also auch die Null. Bei geradem Grad sind sie nie monoton und verfehlen deshalb die Null, sobald ihr Scheitel oberhalb der Achse liegt.
--- falsch
Weil ein Polynom ungeraden Grades nur ungerade Potenzen enthält und deshalb $P(0)=0$ gilt. Bei geradem Grad kommt ein konstantes Glied hinzu, das den Graphen nach oben oder unten verschiebt und die Nullstelle dabei verlieren kann.
--- falsch
Weil der Zwischenwertsatz für Polynome ungeraden Grades schon auf $[0,1]$ greift: $P(0)$ und $P(1)$ haben bei ungeradem Grad stets verschiedene Vorzeichen. Bei geradem Grad haben sie dasselbe Vorzeichen, und der Satz greift nicht.
:::
:::karte formel Stetigkeit der Umkehrfunktion
Was gilt nach dem Satz über die Stetigkeit der Umkehrfunktion für eine stetige, streng monoton wachsende Funktion $f:[a,b]\to\mathbb{R}$?
---
Mit $A:=f(a)$, $B:=f(b)$ ist $f:[a,b]\to[A,B]$ bijektiv, und die Umkehrfunktion $g=f^{-1}:[A,B]\to[a,b]$ ist ebenfalls streng monoton wachsend und stetig.
--- falsch
Mit $A:=f(a)$, $B:=f(b)$ ist $f:[a,b]\to[A,B]$ bijektiv, die Umkehrfunktion $g=f^{-1}$ ist streng monoton wachsend, aber nicht unbedingt stetig; dafür braucht $f$ eine Formel.
--- falsch
$f$ ist injektiv, die Surjektivität auf $[A,B]$ muss man aber zusätzlich fordern; ist sie gegeben, so ist $g=f^{-1}:[A,B]\to[a,b]$ stetig und streng monoton fallend.
--- falsch
Mit $A:=f(a)$, $B:=f(b)$ ist $f:[a,b]\to[A,B]$ bijektiv, und $g=f^{-1}$ ist stetig, aber streng monoton fallend, weil die Spiegelung an $y=x$ die Richtung umkehrt.
:::
:::karte zusammenhang Umkehrfunktion
Warum muss man im Satz über die Stetigkeit der Umkehrfunktion die Surjektivität nicht fordern, anders als in [Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)?
---
Weil der Zwischenwertsatz sie liefert: Aus $a<x<b$ folgt $A<f(x)<B$, also $\mathcal W(f)\subset[A,B]$, und $\mathcal W(f)=[m,M]$ gibt $\mathcal W(f)=[A,B]$. Jeder Wert zwischen $A$ und $B$ wird getroffen.
--- falsch
Weil streng monotone Funktionen immer surjektiv auf $\mathbb{R}$ sind: Sie wachsen über jede Grenze und treffen deshalb jeden reellen Wert, auch ohne Stetigkeit und ohne Intervall.
--- falsch
Weil die Umkehrfunktion nur auf $\mathcal W(f)$ erklärt wird und $\mathcal W(f)$ ohnehin $[A,B]$ ist, gleich ob $f$ stetig ist; die Stetigkeit von $f$ braucht man nur für die Stetigkeit von $g$.
--- falsch
Weil strenge Monotonie die Surjektivität schon enthält: Eine streng wachsende Funktion kann keinen Wert auslassen, weil sie sonst an dieser Stelle konstant sein müsste.
:::
:::karte zusammenhang Umkehrfunktion ohne Intervall
Warum kann die Umkehrfunktion einer stetigen, streng wachsenden Funktion springen, wenn deren Definitionsbereich kein Intervall ist?
---
$f(x)=x$ auf $[0,1]$, $f(x)=x-1$ auf $(2,3]$ ist stetig und streng wachsend mit $\mathcal W(f)=[0,2]$. Die Umkehrfunktion $g$ springt aber bei $y=1$ von 1 auf 2, weil im Definitionsbereich die Stellen zwischen 1 und 2 fehlen.
--- falsch
Sie kann nicht springen: Ist $f$ stetig und streng wachsend, so ist $g$ immer stetig, gleich wie der Definitionsbereich aussieht; Lücken im Definitionsbereich überträgt die Spiegelung nicht.
--- falsch
Weil $f$ an der Lücke selbst springen muss: Eine Funktion auf $[0,1]\cup(2,3]$ ist an der Lücke zwischen 1 und 2 unstetig, und dieser Sprung von $f$ geht beim Spiegeln an $g$ über.
--- falsch
Weil $\mathcal W(f)$ dann ebenfalls eine Lücke hat, in der $g$ nicht erklärt ist; $g$ springt über diese Lücke im Wertebereich, obwohl $g$ auf jedem Teilstück für sich stetig bleibt.
:::
:::karte begriff Intervallhalbierungsmethode
Wie arbeitet die Intervallhalbierungsmethode zur Berechnung einer Nullstelle, und wie groß ist ihr Fehler nach $n$ Schritten?
---
Ein konstruktives Verfahren: Man berechnet den neuen Rand $\frac{a_{n-1}+b_{n-1}}2$, behält die Hälfte mit Vorzeichenwechsel, und $\lim a_n=\lim b_n$ ist die Nullstelle. Der Fehler nach $n$ Schritten ist höchstens $2^{-n}(b-a)$.
--- falsch
Ein Näherungsverfahren ohne Fehlerschranke: Man halbiert das Intervall und behält die Hälfte mit dem kleineren Funktionswert; wie genau das Ergebnis ist, weiß man erst, wenn die Rechnung beendet ist.
--- falsch
Ein konstruktives Verfahren: Man halbiert das Intervall und behält die Hälfte mit Vorzeichenwechsel. Der Fehler nach $n$ Schritten ist höchstens $\frac{b-a}{n}$, er sinkt also in jedem Schritt um denselben Betrag.
--- falsch
Ein konstruktives Verfahren: Man halbiert das Intervall und behält die Hälfte mit Vorzeichenwechsel. Der Fehler nach $n$ Schritten ist höchstens $2^{-n}(b-a)$, und schon zehn Schritte geben zehn Dezimalstellen.
:::
:::karte begriff Sekante und Sekantenverfahren
Was ist das Sekantenverfahren zur Nullstellenberechnung, und welche Gerade heißt dabei Sekante?
---
Ein Verfahren, das das Intervall statt bei $\frac{a+b}2$ an der Nullstelle $\alpha$ der Sekante teilt und das Teilintervall mit Vorzeichenwechsel behält. Die Sekante ist die Gerade durch $(a\,|\,f(a))$ und $(b\,|\,f(b))$.
--- falsch
Ein Verfahren, das das Intervall an der Stelle teilt, an der die Tangente in $a$ die Achse schneidet. Die Sekante ist dabei die Gerade, die den Graphen im Punkt $(a\,|\,f(a))$ nur berührt.
--- falsch
Ein Verfahren, das das Intervall stets bei $\frac{a+b}2$ teilt und die Sekante nur zur Kontrolle zeichnet. Die Sekante ist die Gerade durch die Achsenpunkte $(a\,|\,0)$ und $(b\,|\,0)$.
--- falsch
Ein Verfahren, das das Intervall an der Nullstelle $\alpha$ der Sekante teilt und immer das linke Teilintervall $[a,\alpha]$ behält. Die Sekante ist die Gerade durch $(a\,|\,f(a))$ und $(b\,|\,f(b))$.
:::
:::karte formel Nullstelle der Sekante
Wie lauten die Sekante $P_1$ durch $(a\,|\,f(a))$ und $(b\,|\,f(b))$ und ihre Nullstelle $\alpha$, und welches Teilintervall behält man?
---
$P_1(x):=f(a)+\frac{f(b)-f(a)}{b-a}\,(x-a)$ und $\alpha:=a-\frac{b-a}{f(b)-f(a)}\cdot f(a)$. Man nimmt $[a,\alpha]$, falls $f(a)\cdot f(\alpha)<0$, und $[\alpha,b]$, falls $f(\alpha)\cdot f(b)<0$.
--- falsch
$P_1(x):=f(a)+\frac{b-a}{f(b)-f(a)}\,(x-a)$ und $\alpha:=a-\frac{f(b)-f(a)}{b-a}\cdot f(a)$. Man nimmt $[a,\alpha]$, falls $f(a)\cdot f(\alpha)<0$, und $[\alpha,b]$, falls $f(\alpha)\cdot f(b)<0$.
--- falsch
$P_1(x):=f(a)+\frac{f(b)-f(a)}{b-a}\,(x-a)$ und $\alpha:=\frac{a+b}2$. Man nimmt $[a,\alpha]$, falls $f(a)\cdot f(\alpha)>0$, und $[\alpha,b]$, falls $f(\alpha)\cdot f(b)>0$.
--- falsch
$P_1(x):=f(a)+\frac{f(b)-f(a)}{b-a}\,(x-a)$ und $\alpha:=a+\frac{b-a}{f(b)-f(a)}\cdot f(a)$. Man nimmt stets $[\alpha,b]$, weil die Nullstelle rechts vom Schnittpunkt der Sekante liegt.
:::
:::karte zusammenhang Halbieren und Sekante im Vergleich
Welches der beiden Verfahren kommt bei der Gleichung $k(x)=2$ schneller an die Lösung, und welchen Vorteil hat das andere?
---
Die Sekante: Nach sechs Schritten liegt sie nur $1{,}1\cdot10^{-5}$ neben $x^*=0{,}44285$, die Halbierung kennt $x^*$ nur auf $0{,}016$ genau. Dafür ist der Fehler der Halbierung vorab bekannt, höchstens $2^{-n}(b-a)$.
--- falsch
Die Halbierung: Nach sechs Schritten kennt sie $x^*$ auf $10^{-5}$ genau, die Sekante liegt noch $0{,}016$ daneben. Dafür braucht die Sekante keine Prüfung der Vorzeichen an den Rändern.
--- falsch
Beide sind gleich schnell, weil beide in jedem Schritt das Intervall genau halbieren; die Sekante hat nur den Vorteil, dass ihr Fehler nach $n$ Schritten vorab bekannt ist.
--- falsch
Die Sekante: Nach sechs Schritten liegt sie nur $1{,}1\cdot10^{-5}$ daneben, und ihr Fehler ist wie bei der Halbierung vorab bekannt, höchstens $2^{-n}(b-a)$; die Halbierung hat keinen Vorteil.
:::
:::karte begriff Fixpunkt
Was ist ein Fixpunkt einer Funktion $f:M\to\mathbb{R}$, und wie erkennt man ihn am Graphen?
---
Eine Stelle $x_0\in M$ mit $f(x_0)=x_0$. Am Graphen ist das ein Schnittpunkt mit der Winkelhalbierenden $\{y=x\}$; gleichbedeutend hat $g(x):=f(x)-x$ dort eine Nullstelle.
--- falsch
Eine Stelle $x_0\in M$ mit $f(x_0)=0$. Am Graphen ist das ein Schnittpunkt mit der $x$-Achse; gleichbedeutend hat $f$ dort eine Nullstelle mit Vorzeichenwechsel.
--- falsch
Eine Stelle $x_0\in M$, an der $f$ ihr Maximum annimmt. Am Graphen ist das der höchste Punkt; dort bleibt der Wert fest, wenn man $x$ ein wenig ändert.
--- falsch
Eine Stelle $x_0\in M$ mit $f(x_0)=f(-x_0)$. Am Graphen ist das ein Punkt, der beim Spiegeln an der $y$-Achse fest bleibt; gerade Funktionen haben nur solche.
:::
:::karte formel Fixpunktsatz
Unter welchen Voraussetzungen hat eine Funktion nach dem Fixpunktsatz mindestens einen Fixpunkt, und wie folgt das aus dem Zwischenwertsatz?
---
$f:[a,b]\to\mathbb{R}$ stetig mit $\mathcal W(f)\subset[a,b]$. Dann ist $g(x):=f(x)-x$ stetig mit $g(a)\ge0\ge g(b)$; ist kein Rand Nullstelle, liefert der Zwischenwertsatz ein $x_0$ mit $g(x_0)=0$.
--- falsch
$f:[a,b]\to\mathbb{R}$ stetig, sonst nichts: Jede stetige Funktion auf einem abgeschlossenen Intervall schneidet die Winkelhalbierende, weil $g(x):=f(x)-x$ immer das Vorzeichen wechselt.
--- falsch
$f:[a,b]\to\mathbb{R}$ mit $\mathcal W(f)\subset[a,b]$, Stetigkeit ist nicht nötig: Ein Graph, der im Quadrat $[a,b]\times[a,b]$ bleibt, muss die Diagonale treffen, auch wenn er springt.
--- falsch
$f:[a,b]\to\mathbb{R}$ stetig und streng monoton wachsend mit $\mathcal W(f)\subset[a,b]$: Ohne Monotonie kann $g(x):=f(x)-x$ mehrfach das Vorzeichen wechseln, und der Satz greift dann nicht.
:::
:::karte zusammenhang Voraussetzungen des Fixpunktsatzes
Warum haben $x+1$ auf $[0,1]$ und $1-H(x-\frac12)$ auf $[0,1]$ keinen Fixpunkt?
---
$x+1$ verlässt das Intervall, es fehlt $\mathcal W(f)\subset[a,b]$. $1-H(x-\frac12)$ bleibt in $[0,1]$, springt aber über die Winkelhalbierende; es fehlt die Stetigkeit.
--- falsch
Beide sind nicht stetig: $x+1$ springt am Rand 1 aus dem Intervall heraus, und $1-H(x-\frac12)$ springt bei $\frac12$ über die Winkelhalbierende hinweg.
--- falsch
Beide verlassen das Intervall $[0,1]$: $x+1$ nimmt Werte bis 2 an, und $1-H(x-\frac12)$ nimmt ab der Stelle $\frac12$ den Wert $-1$ an.
--- falsch
Beide haben doch einen Fixpunkt: $x+1$ bei $x=1$, weil der Rand mitzählt, und $1-H(x-\frac12)$ bei $x=\frac12$, weil dort der Sprung liegt.
:::
::::
