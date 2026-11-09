---
title: Stufe 8: Zwischenwerte, Nullstellen, Umkehrfunktion
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
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
Aus $a<x<b$ folgt $A<f(x)<B$, also $\mathcal W(f)\subset[A,B]$, und [(8.1)](#gl-8-1) gibt $\mathcal W(f)=[A,B]$. Bijektivität und Monotonie von $g$ sind aus [Teil 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html) bekannt. Stetigkeit bei $y_0\in(A,B)$, $x_0:=g(y_0)$: Sei $\varepsilon>0$ so klein, dass $[x_0-\varepsilon,x_0+\varepsilon]\subset[a,b]$. Dann ist $f(x_0-\varepsilon)<y_0<f(x_0+\varepsilon)$, und $\delta_0:=\min\{y_0-f(x_0-\varepsilon),\ f(x_0+\varepsilon)-y_0\}>0$. Für $|y-y_0|<\delta_0$ gilt $f(x_0-\varepsilon)<y<f(x_0+\varepsilon)$, und Anwenden von $g$ gibt $x_0-\varepsilon<g(y)<x_0+\varepsilon$. Am Rand läuft es einseitig genauso.
:::

⁠**So liest man das:** Anders als in [Teil 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html) muss man die Surjektivität nicht fordern. Für streng fallende $f$ gilt alles entsprechend. Ebenso für $f:(a,b)\to\mathbb{R}$ stetig und streng monoton, auch mit $a=-\infty$ oder $b=\infty$: Man schöpft $(a,b)$ durch Intervalle $[a_n,b_n]$ aus.

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
