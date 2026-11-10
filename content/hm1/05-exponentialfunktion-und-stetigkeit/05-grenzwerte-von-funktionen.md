---
title: Stufe 3: Grenzwerte von Funktionen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1250500
summary: Bisher läuft nur der Index n gegen unendlich.
tags: linksseitigen Grenzwert, rechtsseitigen Grenzwert
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Bisher läuft nur der Index $n$ gegen unendlich. Jetzt läuft $x$ gegen eine Stelle $x_0$. Das klärt, welchen Wert die Lücke $L$ bei 2 haben sollte und woran man einen Sprung erkennt.
:::

**Die Idee.** Man schickt Testfolgen los, die gegen $x_0$ laufen, ohne $x_0$ zu treffen, und beobachtet die Bilder. Enden alle Bilderfolgen beim selben Wert, ist das der Grenzwert. Der Wert $f(x_0)$ darf fehlen und spielt keine Rolle.

:::definition Definition 3.1 (Grenzwert einer Funktion)
<span class="anker" id="satz-3-1"></span>

Sei $x_0\in(a,b)$ und $f$ auf $(a,b)$ erklärt, außer vielleicht in $x_0$. Man betrachtet Folgen mit

<span class="anker" id="gl-3-1"></span>
$$x_n\in(a,b),\quad x_n\ne x_0\quad\forall\,n\in\mathbb{N},\qquad\lim_{n\to\infty}x_n=x_0. \tag{3.1}$$

<ol class="rm">

<li>

$f$ besitzt in $x_0$ den Grenzwert $y_0$, falls für jede Folge mit [(3.1)](#gl-3-1) gilt

<span class="anker" id="gl-3-2"></span>
$$\lim_{n\to\infty}f(x_n)=y_0. \tag{3.2}$$

Man schreibt $\lim\limits_{x\to x_0}f(x)=y_0$.

</li>

<li>

$f$ besitzt in $x_0$ den __linksseitigen Grenzwert__ $y_0$, $\lim\limits_{x\nearrow x_0}f(x)=y_0$, falls [(3.2)](#gl-3-2) für jede Folge mit [(3.1)](#gl-3-1) und zusätzlich $x_n<x_0$ gilt.

</li>

<li>

$f$ besitzt in $x_0$ den __rechtsseitigen Grenzwert__ $y_0$, $\lim\limits_{x\searrow x_0}f(x)=y_0$, falls [(3.2)](#gl-3-2) für jede Folge mit [(3.1)](#gl-3-1) und zusätzlich $x_n>x_0$ gilt.

</li>

</ol>
:::

⁠**So liest man das:** Das Wort *jede* trägt die Definition, eine einzelne Folge beweist nichts. Endlich viele Glieder kann man weglassen, es genügen also Folgen in einer punktierten Umgebung $\dot U_\eta(x_0)$. (i) ist gleichbedeutend mit (ii) und (iii) mit demselben $y_0$, denn eine Folge von beiden Seiten zerfällt in eine linke und eine rechte.

::::beispiel [Beispiele (Abb. [3](#abb-3))]
⁠*Lücke:* Für $x\ne2$ ist $L(x)=x+2$. Für jede Folge mit $x_n\to2$, $x_n\ne2$ gilt also $L(x_n)=x_n+2\to4$. Damit ist $\lim_{x\to2}L(x)=4$, obwohl $L(2)$ nicht erklärt ist. *Sprung:* Für $x_n=-\frac1n$ ist $H(x_n)=0$, für $x_n=\frac1n$ ist $H(x_n)=1$. Also ist $\lim_{x\nearrow0}H(x)=0$ und $\lim_{x\searrow0}H(x)=1$, und der beidseitige Grenzwert existiert nicht. *Schwingen:* Auch einseitige Grenzwerte können fehlen. $w(x):=(-1)^{\lfloor1/x\rfloor}$ für $x>0$ ist bei $x_n=\frac1{2n}$ gleich $1$, bei $x_n=\frac1{2n+1}$ gleich $-1$. Beide Folgen laufen von rechts gegen 0.
::::

:::abbildung hm1/k5grenzwert 3
Links hat $L$ bei 2 den Grenzwert 4, nur der Wert fehlt. Mitte: Die einseitigen Grenzwerte von $H$ bei 0 sind verschieden. Rechts wechselt $w$ nahe 0 immer schneller zwischen $1$ und $-1$.
:::

:::satz Satz 3.2 (Rechnen mit Grenzwerten von Funktionen)
<span class="anker" id="satz-3-2"></span>

Aus $\lim_{x\to x_0}f(x)=y_0$ und $\lim_{x\to x_0}g(x)=w_0$ folgt: (i) $\lim_{x\to x_0}[\alpha f(x)+\beta g(x)]=\alpha y_0+\beta w_0$ für alle $\alpha,\beta\in\mathbb{R}$, (ii) $\lim_{x\to x_0}[f(x)\cdot g(x)]=y_0\cdot w_0$, (iii) falls $w_0\ne0$: $\lim_{x\to x_0}\frac{f(x)}{g(x)}=\frac{y_0}{w_0}$.
:::

⁠**So liest man das:** Auf eine Testfolge angewandt sind das die Rechenregeln für Folgen aus [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html), mehr ist nicht zu beweisen. Für Polynome folgt daraus der Grenzwert durch Einsetzen:

<span class="anker" id="gl-3-3"></span>
$$\lim_{x\to x_0}P_n(x)=P_n(x_0). \tag{3.3}$$

Denn für $Q_1(x)=x$ gilt das sofort, für $Q_n(x)=x\cdot Q_{n-1}(x)$ per Induktion mit (ii), und (i) setzt daraus jedes Polynom zusammen.

Hat der Nenner bei $x_0$ eine Nullstelle, greift (iii) nicht. Ist $x_0$ auch Nullstelle des Zählers, spaltet man den Linearfaktor ab ([Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)).

:::satz Satz 3.3 (Grenzwerte rationaler Funktionen)
<span class="anker" id="satz-3-3"></span>

Sei $P_n$ Polynom vom Grad $n$ mit Nullstelle $x_0$, also $P_n(x)=(x-x_0)\tilde P_{n-1}(x)$, und $Q_m$ Polynom vom Grad $m$ mit einfacher Nullstelle $x_0$, also $Q_m(x)=(x-x_0)\tilde Q_{m-1}(x)$ mit $\tilde Q_{m-1}(x_0)\ne0$. Dann gilt

<span class="anker" id="gl-3-4"></span>
$$\lim_{x\to x_0}P_n(x)/Q_m(x)=\tilde P_{n-1}(x_0)/\tilde Q_{m-1}(x_0). \tag{3.4}$$
:::

⁠**So liest man das:** Für $x\ne x_0$ darf man den Faktor kürzen, und [(3.1)](#gl-3-1) verlangt genau $x_n\ne x_0$. Danach geben [(3.3)](#gl-3-3) und (iii) das Ergebnis.

::::beispiel
$\frac{x^3-8}{x^2-4}=\frac{(x-2)(x^2+2x+4)}{(x-2)(x+2)}$ hat bei 2 den Grenzwert $\frac{12}4=3$.
::::

:::satz Satz 3.4 (Vergleichskriterium für Grenzwerte von Funktionen)
<span class="anker" id="satz-3-4"></span>

Für ein $\eta>0$ gelte $g(x)\le f(x)\le h(x)$ für alle $x\in\dot U_\eta(x_0)$. Dann gilt:

$$\lim_{x\to x_0}g(x)=\lim_{x\to x_0}h(x)=y_0\quad\Longrightarrow\quad\lim_{x\to x_0}f(x)=y_0.$$
:::

⁠**So liest man das:** Das ist das Sandwich-Lemma für jede Testfolge. Bei $x_0$ selbst muss die Ungleichung nicht gelten.

::::beispiel mit dem Rechenmodell
Für $0<|x|<1$ gilt

<span class="anker" id="gl-3-5"></span>
$$1-|x|\le\frac{\mathrm{e}^x-1}x\le\frac1{1-|x|},\qquad\text{also}\qquad\lim_{x\to0}\frac{\mathrm{e}^x-1}x=1. \tag{3.5}$$

Für $0<x<1$ folgt das aus Satz [2.1](wachstum-logarithmus-allgemeine-potenz.html#satz-2-1) (i) und (iii). Für $x=-t$, $0<t<1$, ist der Bruch $\frac{1-\mathrm{e}^{-t}}t$. Oben gilt $1-\mathrm{e}^{-t}\le t$ wieder nach (i), unten $1-\mathrm{e}^{-t}=\mathrm{e}^{-t}(\mathrm{e}^t-1)\ge(1-t)\,t$. Beide Schranken laufen gegen 1. Zahlen: Bei $x=0{,}1$ ist der Bruch $1{,}0517$, bei $x=0{,}01$ ist er $1{,}0050$. Für die Prüffunktion folgt $\lim_{x\to0}\frac{k(x)-1}x=\lim_{x\to0}\bigl(\frac{\mathrm{e}^x-1}x+1\bigr)=2$.
::::

**Grenzwerte für $x\to\infty$.** Für $f:\mathbb{R}^+\to\mathbb{R}$ heißt $\lim_{x\to\infty}f(x)=y_0$: Für jede Folge mit $x_n\to\infty$ gilt $f(x_n)\to y_0$. Beispiel: Für $x>4(n+1)^2$ ist $0<x^n\mathrm{e}^{-x}<\frac1x$ nach Satz [2.1](wachstum-logarithmus-allgemeine-potenz.html#satz-2-1) (iv), also $\lim_{x\to\infty}x^n\mathrm{e}^{-x}=0$ für jedes feste $n$.

:::aufgabe Aufgabe 3 ★★ Grenzwerte bestimmen
<span class="anker" id="aufg-3"></span>

(a) $\lim_{x\to3}\frac{x^2-9}{x-3}$, (b) $\lim_{x\to1}\frac{x^3-1}{x^2-1}$, (c) die einseitigen Grenzwerte von $\frac{|x|}x$ bei 0, (d) $\lim_{x\to0}\frac{\mathrm{e}^{2x}-1}x$; setze $u=2x$ in [(3.5)](#gl-3-5), (e) $\lim_{x\to\infty}\frac{3x+\mathrm{e}^{-x}}{x+1}$.

:::loesung
(a) Kürzen gibt $x+3\to6$. (b) $\frac{(x-1)(x^2+x+1)}{(x-1)(x+1)}\to\frac32$. (c) Für $x<0$ ist der Bruch $-1$, für $x>0$ ist er $1$. Linksseitig $-1$, rechtsseitig $1$, kein beidseitiger Grenzwert. (d) Aus $x_n\to0$, $x_n\ne0$ folgt $u_n=2x_n\to0$, $u_n\ne0$. Also $\frac{\mathrm{e}^{2x}-1}x=2\,\frac{\mathrm{e}^u-1}u\to2$. (e) Kürzen mit $x$: $\frac{3+\mathrm{e}^{-x}/x}{1+1/x}\to3$.
:::
:::
