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

::::formelsammlung
**Testfolgen**

$$x_n\in(a,b),\quad x_n\ne x_0\quad\forall\,n\in\mathbb{N},\qquad\lim_{n\to\infty}x_n=x_0$$

$f$ ist auf $(a,b)$ erklärt, außer vielleicht in $x_0$.

**Grenzwert einer Funktion**

$$\lim\limits_{x\to x_0}f(x)=y_0$$

Bedeutet: $\lim_{n\to\infty}f(x_n)=y_0$ für jede Testfolge. Der Wert $f(x_0)$ darf fehlen und spielt keine Rolle.

**Einseitige Grenzwerte**

$$\lim\limits_{x\nearrow x_0}f(x)=y_0,\qquad\lim\limits_{x\searrow x_0}f(x)=y_0$$

Linksseitig bzw. rechtsseitig: nur Testfolgen mit zusätzlich $x_n<x_0$ bzw. $x_n>x_0$. Der Grenzwert existiert genau dann, wenn beide existieren und gleich sind.

**Summe und Produkt**

$$\lim_{x\to x_0}[\alpha f(x)+\beta g(x)]=\alpha y_0+\beta w_0,\qquad\lim_{x\to x_0}[f(x)\cdot g(x)]=y_0\cdot w_0$$

Für $\lim_{x\to x_0}f(x)=y_0$, $\lim_{x\to x_0}g(x)=w_0$ und alle $\alpha,\beta\in\mathbb{R}$.

**Quotient**

$$\lim_{x\to x_0}\frac{f(x)}{g(x)}=\frac{y_0}{w_0}$$

Falls $w_0\ne0$.

**Polynome**

$$\lim_{x\to x_0}P_n(x)=P_n(x_0)$$

Grenzwert durch Einsetzen.

**Rationale Funktionen**

$$\lim_{x\to x_0}P_n(x)/Q_m(x)=\tilde P_{n-1}(x_0)/\tilde Q_{m-1}(x_0)$$

Für $P_n(x)=(x-x_0)\tilde P_{n-1}(x)$ und $Q_m(x)=(x-x_0)\tilde Q_{m-1}(x)$ mit $\tilde Q_{m-1}(x_0)\ne0$: kürzen, dann einsetzen.

**Vergleichskriterium**

$$\lim_{x\to x_0}g(x)=\lim_{x\to x_0}h(x)=y_0\quad\Longrightarrow\quad\lim_{x\to x_0}f(x)=y_0$$

Falls $g(x)\le f(x)\le h(x)$ für alle $x\in\dot U_\eta(x_0)$; bei $x_0$ selbst muss das nicht gelten.

**Exponentialfunktion nahe null**

$$1-|x|\le\frac{\mathrm{e}^x-1}x\le\frac1{1-|x|},\qquad\text{also}\qquad\lim_{x\to0}\frac{\mathrm{e}^x-1}x=1$$

Für $0<|x|<1$.

**Grenzwert im Unendlichen**

$$\lim_{x\to\infty}x^n\mathrm{e}^{-x}=0$$

Für jedes feste $n$. Dabei heißt $\lim_{x\to\infty}f(x)=y_0$: Für jede Folge mit $x_n\to\infty$ gilt $f(x_n)\to y_0$.
::::

::::lernkarten
:::karte zusammenhang Grenzwert
Wie wird der Grenzwert $\lim_{x\to x_0}f(x)=y_0$ einer Funktion in $x_0\in(a,b)$ auf Grenzwerte von Folgen zurückgeführt?
---
Für jede Folge mit $x_n\in(a,b)$, $x_n\ne x_0$ und $\lim_{n\to\infty}x_n=x_0$ muss $\lim_{n\to\infty}f(x_n)=y_0$ gelten. Der Wert $f(x_0)$ darf fehlen und spielt keine Rolle.
--- falsch
Es genügt eine Folge mit $x_n\ne x_0$ und $\lim_{n\to\infty}x_n=x_0$, deren Bilder gegen $y_0$ laufen; weitere Folgen muss man nicht prüfen, weil alle dasselbe liefern.
--- falsch
Für jede Folge mit $\lim_{n\to\infty}x_n=x_0$, auch mit $x_n=x_0$, muss $\lim_{n\to\infty}f(x_n)=y_0$ gelten. Deshalb muss $f(x_0)$ erklärt und gleich $y_0$ sein.
--- falsch
Für jede Folge, deren Bilder $f(x_n)$ gegen $y_0$ laufen, muss $\lim_{n\to\infty}x_n=x_0$ gelten. Der Wert $f(x_0)$ darf dabei fehlen und spielt keine Rolle.
:::
:::karte begriff linksseitiger Grenzwert und rechtsseitiger Grenzwert
Wann besitzt $f$ in $x_0$ den linksseitigen Grenzwert $y_0$, und wann den rechtsseitigen?
---
Linksseitig, falls $\lim_{n\to\infty}f(x_n)=y_0$ für jede Testfolge mit $x_n\ne x_0$, $x_n\to x_0$ und zusätzlich $x_n<x_0$ gilt, geschrieben $\lim\limits_{x\nearrow x_0}f(x)=y_0$; rechtsseitig ebenso mit $x_n>x_0$, geschrieben $\lim\limits_{x\searrow x_0}f(x)=y_0$.
--- falsch
Linksseitig, falls $\lim_{n\to\infty}f(x_n)=y_0$ für jede Testfolge mit $x_n\to x_0$ und zusätzlich $f(x_n)<y_0$ gilt; rechtsseitig ebenso mit $f(x_n)>y_0$. Die Werte nähern sich also von unten oder von oben.
--- falsch
Linksseitig, falls $\lim_{n\to\infty}f(x_n)=y_0$ für jede Testfolge mit $x_n\to x_0$ und zusätzlich $x_n>x_0$ gilt, geschrieben $\lim\limits_{x\nearrow x_0}f(x)=y_0$; rechtsseitig ebenso mit $x_n<x_0$, weil der Pfeil die Richtung angibt, in die man schaut.
--- falsch
Linksseitig, falls es eine einzige Folge mit $x_n<x_0$ und $x_n\to x_0$ gibt, für die $\lim_{n\to\infty}f(x_n)=y_0$ gilt; rechtsseitig ebenso mit einer einzigen Folge mit $x_n>x_0$. Weitere Folgen muss man nicht prüfen.
:::
:::karte zusammenhang einseitige Grenzwerte
Wann existiert der Grenzwert einer Funktion in $x_0$, wenn man ihre einseitigen Grenzwerte dort kennt?
---
Genau dann, wenn der linksseitige und der rechtsseitige Grenzwert existieren und denselben Wert $y_0$ haben. Denn eine Testfolge von beiden Seiten zerfällt in eine linke und eine rechte.
--- falsch
Sobald einer der beiden einseitigen Grenzwerte existiert; der andere ergibt sich dann von selbst, weil eine Funktion links und rechts von $x_0$ dasselbe Verhalten zeigt.
--- falsch
Wenn beide einseitigen Grenzwerte existieren, auch bei verschiedenen Werten; der Grenzwert ist dann ihr Mittelwert, wie beim Schalter $H$ mit dem Grenzwert $\frac12$ bei 0.
--- falsch
Wenn beide einseitigen Grenzwerte existieren und mit dem Funktionswert $f(x_0)$ übereinstimmen; ohne den Wert $f(x_0)$ gibt es keinen Grenzwert, weil der Vergleich fehlt.
:::
:::karte zusammenhang Sprung
Warum hat der Schalter $H$ mit $H(x)=0$ für $x<0$ und $H(x)=1$ für $x\ge0$ bei 0 keinen Grenzwert?
---
Für $x_n=-\frac1n$ ist $H(x_n)=0$, für $x_n=\frac1n$ ist $H(x_n)=1$. Also ist $\lim_{x\nearrow0}H(x)=0$ und $\lim_{x\searrow0}H(x)=1$; zwei Testfolgen enden bei verschiedenen Werten.
--- falsch
Weil $H$ bei 0 einen Funktionswert hat: Ein Grenzwert existiert nur an Stellen, an denen die Funktion nicht erklärt ist, wie bei der Lücke $L$ bei 2.
--- falsch
Weil $H$ in jeder Umgebung von 0 nur die Werte 0 und 1 annimmt; eine Funktion mit nur endlich vielen Werten hat an keiner Stelle einen Grenzwert.
--- falsch
Weil die Testfolge $x_n=\frac1n$ die Bilder $H(x_n)=1$ hat und das nicht mit $H(0)=0$ übereinstimmt; bei einem Grenzwert müssen alle Bilder gegen $H(0)$ laufen.
:::
:::karte zusammenhang Lücke
Warum hat die Lücke $L(x)=\frac{x^2-4}{x-2}$ bei 2 den Grenzwert 4, obwohl $L(2)$ nicht erklärt ist?
---
Für $x\ne2$ ist $L(x)=x+2$, und Testfolgen treffen 2 nie. Also gilt $L(x_n)=x_n+2\to4$ für jede Folge mit $x_n\to2$, $x_n\ne2$; der fehlende Wert spielt keine Rolle.
--- falsch
Weil man in $\frac{x^2-4}{x-2}$ einfach $x=2$ einsetzen darf: Zähler und Nenner sind dann null, und den Ausdruck $\frac00$ setzt man bei einer Lücke gleich dem Zähler-Koeffizienten 4.
--- falsch
Weil $L$ bei 2 stetig ist: Eine rationale Funktion ist an jeder Stelle stetig, auch an Nullstellen des Nenners, und der Grenzwert ist deshalb einfach der Funktionswert.
--- falsch
Weil für $x\ne2$ zwar $L(x)=x+2$ gilt, man aber nur Testfolgen von rechts nehmen darf; von links ist der Nenner negativ, und der linksseitige Grenzwert ist $-4$.
:::
:::karte zusammenhang Schwingen
Können auch einseitige Grenzwerte fehlen, wie es die Funktion $w(x)=(-1)^{\lfloor1/x\rfloor}$ für $x>0$ an der Stelle 0 zeigt?
---
Ja: Bei $x_n=\frac1{2n}$ ist $w(x_n)=1$, bei $x_n=\frac1{2n+1}$ ist $w(x_n)=-1$. Beide Folgen laufen von rechts gegen 0, also gibt es keinen rechtsseitigen Grenzwert.
--- falsch
Nein: Für $x>0$ nähert man sich 0 nur von rechts, und Folgen von einer Seite liefern immer einen Grenzwert; $w$ hat bei 0 den rechtsseitigen Grenzwert 0.
--- falsch
Ja, aber nur, wenn die Funktion bei $x_0$ nicht erklärt ist; bei $w$ fehlt der Wert $w(0)$, und deshalb fehlt dort auch der rechtsseitige Grenzwert.
--- falsch
Nein: $w$ nimmt nur die Werte $1$ und $-1$ an, ihr rechtsseitiger Grenzwert bei 0 ist deshalb der Mittelwert 0 dieser beiden Werte, um den sie schwingt.
:::
:::karte formel Rechnen mit Grenzwerten von Funktionen
Was gilt nach den Rechenregeln, wenn $\lim_{x\to x_0}f(x)=y_0$ und $\lim_{x\to x_0}g(x)=w_0$ ist?
---
$\lim_{x\to x_0}[\alpha f(x)+\beta g(x)]=\alpha y_0+\beta w_0$ für alle $\alpha,\beta\in\mathbb{R}$, $\lim_{x\to x_0}[f(x)\cdot g(x)]=y_0\cdot w_0$ und, falls $w_0\ne0$, $\lim_{x\to x_0}\frac{f(x)}{g(x)}=\frac{y_0}{w_0}$.
--- falsch
$\lim_{x\to x_0}[\alpha f(x)+\beta g(x)]=\alpha y_0+\beta w_0$ und $\lim_{x\to x_0}[f(x)\cdot g(x)]=y_0\cdot w_0$; der Quotient $\frac{y_0}{w_0}$ gilt auch für $w_0=0$, er ist dann unendlich.
--- falsch
$\lim_{x\to x_0}[f(x)+g(x)]=y_0+w_0$, aber für Produkte und Quotienten gibt es keine solche Regel, weil man sie bei Funktionen anders bildet.
--- falsch
Sie gelten nur, wenn $f$ und $g$ in $x_0$ erklärt sind mit $f(x_0)=y_0$ und $g(x_0)=w_0$; sonst fehlt die Verbindung zu den Rechenregeln für Folgen.
:::
:::karte formel Grenzwert von Polynomen
Wie bestimmt man den Grenzwert eines Polynoms $P_n$ an einer Stelle $x_0$, und warum darf man das?
---
Durch Einsetzen: $\lim_{x\to x_0}P_n(x)=P_n(x_0)$. Für $Q_1(x)=x$ gilt das sofort, für $Q_n(x)=x\cdot Q_{n-1}(x)$ per Induktion mit der Produktregel, und die Summenregel setzt jedes Polynom daraus zusammen.
--- falsch
Durch Einsetzen, aber nur bei Polynomen vom Grad höchstens 2; bei höherem Grad muss man Testfolgen einzeln durchrechnen, weil die Induktion über den Grad dort nicht mehr greift.
--- falsch
Durch Kürzen mit der höchsten Potenz: $\lim_{x\to x_0}P_n(x)$ ist der höchste Koeffizient, weil die höchste Potenz nahe jeder Stelle $x_0$ alle anderen Potenzen überwiegt.
--- falsch
Durch Einsetzen: $\lim_{x\to x_0}P_n(x)=P_n(x_0)$, aber nur für $x_0\ne0$; bei $x_0=0$ verschwinden alle Potenzen von $x$, und man muss Testfolgen einzeln betrachten.
:::
:::karte formel Grenzwerte rationaler Funktionen
Wie bestimmt man $\lim_{x\to x_0}P_n(x)/Q_m(x)$, wenn $x_0$ Nullstelle des Zählers und einfache Nullstelle des Nenners ist?
---
Man spaltet den Linearfaktor ab, $P_n(x)=(x-x_0)\tilde P_{n-1}(x)$ und $Q_m(x)=(x-x_0)\tilde Q_{m-1}(x)$ mit $\tilde Q_{m-1}(x_0)\ne0$, und kürzt: Der Grenzwert ist $\tilde P_{n-1}(x_0)/\tilde Q_{m-1}(x_0)$.
--- falsch
Man setzt $x_0$ in Zähler und Nenner ein und teilt: Der Grenzwert ist $P_n(x_0)/Q_m(x_0)$, weil die Quotientenregel an jeder Stelle gilt, an der beide Polynome erklärt sind.
--- falsch
Kürzen ist verboten, weil man damit bei $x=x_0$ durch null teilen würde; man muss Testfolgen von beiden Seiten einzeln durchrechnen und die beiden Ergebnisse vergleichen.
--- falsch
Es gibt keinen Grenzwert: Hat der Nenner bei $x_0$ eine Nullstelle, wächst der Bruch dort immer ohne Grenze, gleich was der Zähler an dieser Stelle macht.
:::
:::karte formel Vergleichskriterium für Grenzwerte von Funktionen
Was folgt nach dem Vergleichskriterium aus $g(x)\le f(x)\le h(x)$ für alle $x\in\dot U_\eta(x_0)$, und muss die Ungleichung bei $x_0$ selbst gelten?
---
Aus $\lim_{x\to x_0}g(x)=\lim_{x\to x_0}h(x)=y_0$ folgt $\lim_{x\to x_0}f(x)=y_0$. Bei $x_0$ selbst muss die Ungleichung nicht gelten; es ist das Sandwich-Lemma für jede Testfolge.
--- falsch
Aus $\lim_{x\to x_0}g(x)=\lim_{x\to x_0}h(x)=y_0$ folgt $\lim_{x\to x_0}f(x)=y_0$, aber nur, wenn die Ungleichung auch bei $x_0$ gilt und alle drei Funktionen dort den Wert $y_0$ haben.
--- falsch
Aus $\lim_{x\to x_0}g(x)=y_0$ und $\lim_{x\to x_0}h(x)=w_0$ folgt stets ein Grenzwert von $f$ zwischen $y_0$ und $w_0$. Bei $x_0$ selbst muss die Ungleichung nicht gelten.
--- falsch
Aus $\lim_{x\to x_0}g(x)=\lim_{x\to x_0}h(x)=y_0$ folgt $\lim_{x\to x_0}f(x)=y_0$, sofern die Ungleichung für alle $x\in\mathbb{R}$ gilt; auf einer punktierten Umgebung allein reicht sie nicht.
:::
:::karte formel Exponentialfunktion nahe null
Zwischen welchen Schranken liegt $\frac{\mathrm{e}^x-1}x$ für $0<|x|<1$, und welcher Grenzwert folgt daraus für $x\to0$?
---
$1-|x|\le\frac{\mathrm{e}^x-1}x\le\frac1{1-|x|}$ für $0<|x|<1$. Beide Schranken laufen gegen 1, das Vergleichskriterium gibt $\lim_{x\to0}\frac{\mathrm{e}^x-1}x=1$.
--- falsch
$0\le\frac{\mathrm{e}^x-1}x\le|x|$ für $0<|x|<1$. Beide Schranken laufen gegen 0, also ist $\lim_{x\to0}\frac{\mathrm{e}^x-1}x=0$.
--- falsch
$1\le\frac{\mathrm{e}^x-1}x\le\mathrm{e}$ für $0<|x|<1$. Der Grenzwert für $x\to0$ lässt sich damit nicht genau bestimmen, er liegt irgendwo zwischen 1 und $\mathrm{e}$.
--- falsch
$1-|x|\le\frac{\mathrm{e}^x-1}x\le\frac1{1-|x|}$ nur für $0<x<1$. Für $x<0$ gibt es keine Schranken, deshalb existiert nur der rechtsseitige Grenzwert 1.
:::
:::karte herleitung Schranken für den Bruch nahe null
Wie folgen die Schranken $1-|x|\le\frac{\mathrm{e}^x-1}x\le\frac1{1-|x|}$ für $0<|x|<1$ aus den Eigenschaften der Exponentialfunktion?
---
Für $0<x<1$ ist der Bruch mindestens $1\ge1-|x|$, weil $\mathrm{e}^x\ge1+x$ den Zähler $\mathrm{e}^x-1$ mindestens $x$ macht.
---
Nach oben ist er für $0<x<1$ höchstens $\frac1{1-x}$, weil $|\mathrm{e}^x-1|\le\frac{|x|}{1-|x|}$ gilt und man durch $x>0$ teilt.
---
Für $x=-t$ mit $0<t<1$ ist der Bruch $\frac{1-\mathrm{e}^{-t}}t$, weil man Zähler und Nenner mit $-1$ erweitert.
---
Oben gilt $1-\mathrm{e}^{-t}\le t$, weil $\mathrm{e}^{-t}\ge1-t$ nach $\mathrm{e}^x\ge1+x$ ist; der Bruch ist also höchstens $1\le\frac1{1-|x|}$.
---
Unten gilt $1-\mathrm{e}^{-t}=\mathrm{e}^{-t}(\mathrm{e}^t-1)\ge(1-t)\,t$, weil beide Faktoren nach $\mathrm{e}^x\ge1+x$ abgeschätzt werden; der Bruch ist also mindestens $1-t=1-|x|$.
:::
:::karte formel Grenzwerte im Unendlichen
Was bedeutet $\lim_{x\to\infty}f(x)=y_0$ für eine Funktion $f:\mathbb{R}^+\to\mathbb{R}$, und welcher Grenzwert folgt für $x^n\mathrm{e}^{-x}$?
---
Für jede Folge mit $x_n\to\infty$ gilt $f(x_n)\to y_0$. Für $x>4(n+1)^2$ ist $0<x^n\mathrm{e}^{-x}<\frac1x$, also $\lim_{x\to\infty}x^n\mathrm{e}^{-x}=0$ für jedes feste $n$.
--- falsch
Es gibt eine Folge mit $x_n\to\infty$ und $f(x_n)\to y_0$. Für $x^n\mathrm{e}^{-x}$ wächst der Faktor $x^n$ ohne Grenze, also ist $\lim_{x\to\infty}x^n\mathrm{e}^{-x}=\infty$ für $n\ge1$.
--- falsch
Für jede Folge mit $x_n\to\infty$ gilt $f(x_n)\to y_0$. Für $x^n\mathrm{e}^{-x}$ heben sich Wachsen und Fallen auf, deshalb ist $\lim_{x\to\infty}x^n\mathrm{e}^{-x}=1$.
--- falsch
Für jede Folge mit $x_n\to\infty$ gilt $f(x_n)\to y_0$. Für $x^n\mathrm{e}^{-x}$ ist der Grenzwert 0 nur für $n\le3$; für größere $n$ überwiegt die Potenz.
:::
::::
