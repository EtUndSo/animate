---
title: Stufe 5: Stetigkeit vererben
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1250700
summary: varepsilon - delta für jede Funktion einzeln zu führen, ist mühsam.
tags: folgenstetig
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
$\varepsilon$-$\delta$ für jede Funktion einzeln zu führen, ist mühsam. Diese Stufe baut neue stetige Funktionen aus bekannten und zeigt so, dass $k$, $\exp$ und alle rationalen Funktionen stetig sind.
:::

**Die Idee.** Stetigkeit erlaubt, Grenzwert und Funktion zu vertauschen. Dazu lässt man bei den Testfolgen auch $x_0$ selbst zu. Das ist bei Verkettungen nötig: $f(x_n)$ kann $f(x_0)$ treffen, selbst wenn $x_n\ne x_0$ ist.

:::definition Definition 5.1 (Folgenstetigkeit)
<span class="anker" id="satz-5-1"></span>

$f:(a,b)\to\mathbb{R}$ heißt in $x_0\in(a,b)$ __folgenstetig__, falls für alle reellen Folgen $\{x_n\}_{n\in\mathbb{N}}$ in $(a,b)$ gilt:

<span class="anker" id="gl-5-1"></span>
$$\bigl(x_n\to x_0\text{ für }n\to\infty\bigr)\quad\Longrightarrow\quad\bigl(f(x_n)\to f(x_0)\text{ für }n\to\infty\bigr). \tag{5.1}$$

In dieser Situation gilt also

<span class="anker" id="gl-5-2"></span>
$$\lim_{n\to\infty}f(x_n)=f\Bigl(\lim_{n\to\infty}x_n\Bigr). \tag{5.2}$$
:::

:::satz Satz 5.2 (Stetig heißt folgenstetig)
<span class="anker" id="satz-5-2"></span>

$f$ ist in $x_0\in(a,b)$ genau dann stetig, wenn $f$ dort folgenstetig ist.
:::

:::beweis Beide Richtungen
„$\Leftarrow$“: [(5.1)](#gl-5-1) verlangt für mehr Folgen dasselbe wie die Stetigkeit. „$\Rightarrow$“: Der Beweisteil „$\Leftarrow$“ von Satz [4.2](stetigkeit-und-epsilon-delta.html#satz-4-2) braucht $x_n\ne x_0$ nirgends, denn [(4.1)](stetigkeit-und-epsilon-delta.html#gl-4-1) gilt auch für $x=x_0$.
:::

⁠**So liest man das:** Man darf den Grenzwert in die stetige Funktion hineinziehen. Für $f$ stetig auf $[a,b]$ gilt [(5.1)](#gl-5-1) ebenso für Folgen in $[a,b]$, auch mit $x_0=a$ oder $x_0=b$. Abb. [5](#abb-5) zeigt den Unterschied zum Sprung.

:::abbildung hm1/k5folgenstetig 5
Links läuft eine Folge gegen $x_0=0{,}5$, ihre Bilder laufen gegen $k(0{,}5)=2{,}149$. Rechts laufen $x_n=-\frac1n$ gegen 0, ihre Bilder bleiben bei 0, nicht bei $H(0)=1$.
:::

:::satz Satz 5.3 (Verknüpfungen stetiger Funktionen)
<span class="anker" id="satz-5-3"></span>

<ol class="rm">

<li>

Sind $f,g:(a,b)\to\mathbb{R}$ in $x_0$ stetig, sind auch $f+g$, $f\cdot g$ und, sofern $g(x_0)\ne0$, $f/g$ in $x_0$ stetig.

</li>

<li>

Seien $f:(a,b)\to\mathbb{R}$, $g:(c,d)\to\mathbb{R}$ mit $\mathcal W(f)\subset(c,d)$. Ist $f$ in $x_0\in(a,b)$ stetig und $g$ in $y_0:=f(x_0)$ stetig, dann ist $g\circ f:(a,b)\to\mathbb{R}$ in $x_0$ stetig.

</li>

</ol>
:::

:::beweis Rechenregeln und Folgen
(i) Das sind die Rechenregeln aus Satz [3.2](grenzwerte-von-funktionen.html#satz-3-2) mit $y_0=f(x_0)$, $w_0=g(x_0)$. (ii) Sei $x_n\to x_0$. Weil $f$ in $x_0$ folgenstetig ist, gilt $y_n:=f(x_n)\to y_0$. Weil $g$ in $y_0$ folgenstetig ist, gilt $g(y_n)\to g(y_0)$. Also $(g\circ f)(x_n)\to(g\circ f)(x_0)$.
:::

⁠**So liest man das:** Eine kleine Änderung bleibt klein, während sie durch beide Funktionen läuft.

::::beispiel [Beispiele]
<ol class="rm">

<li>

⁠**Rationale Funktionen** $R=P_n/Q_m$ sind auf $\mathcal D(R)=\{x:Q_m(x)\ne0\}$ stetig: Polynome sind stetig, Satz [5.3](#satz-5-3) (i) gibt den Quotienten.

</li>

<li>

⁠**$\exp$ ist auf $\mathbb{R}$ stetig.** Bei $x_0=0$: Für $|x|<1$ gilt nach Satz [2.1](wachstum-logarithmus-allgemeine-potenz.html#satz-2-1) (i), (iii)

$$1+x\le\mathrm{e}^x\le\frac1{1-|x|}.$$

Beide Schranken laufen für $x\to0$ gegen 1, das Vergleichskriterium gibt $\lim_{x\to0}\mathrm{e}^x=1=\mathrm{e}^0$. Bei $x_0\ne0$ schreibt man $\mathrm{e}^x=\mathrm{e}^{x_0}\cdot\mathrm{e}^{x-x_0}$. Das ist die Konstante $\mathrm{e}^{x_0}$ mal der Verkettung von $x\mapsto x-x_0$ (stetig in $x_0$) mit $\exp$ (stetig in 0). Der Mechanismus: Die Funktionalgleichung verschiebt jede Stelle nach 0.

</li>

<li>

⁠**$k(x)=\mathrm{e}^x+x$** ist als Summe stetig, $a^x=\mathrm{e}^{x\log a}$ als Verkettung.

</li>

</ol>
::::

⁠**Grenzfall:** Die Umkehrung von Satz [5.3](#satz-5-3) gilt nicht: $H$ und $1-H$ springen beide bei 0, ihre Summe ist die stetige Funktion 1.

:::aufgabe Aufgabe 5 ★★ Passend machen
<span class="anker" id="aufg-5"></span>

(a) Für welches $c$ ist $f(x)=cx+1$ für $x\le2$, $f(x)=x^2-1$ für $x>2$ überall stetig? (b) Ergänze $g(x)=\frac{x^3-x}{x-1}$ bei 1 stetig. (c) Sage vorher: Ist $u(x)=\mathrm{e}^{-1/x^2}$ bei 0 stetig ergänzbar? Ist es $v(x)=\mathrm{e}^{1/x}$? Rechne mit Testfolgen $x_n=\pm\frac1n$.

:::loesung
(a) Der linke Grenzwert $2c+1$ muss gleich dem rechten $3$ sein, also $c=1$. (b) $g(x)=x(x+1)$ für $x\ne1$, also $\tilde g(1)=2$. (c) $u(\pm\frac1n)=\mathrm{e}^{-n^2}\to0$. Allgemein ist für $x\to 0$ auch $1/x^2\to\infty$ und $\mathrm{e}^{-1/x^2}\le x^2\to0$ wegen $\mathrm{e}^t\ge1+t>t$, also $\tilde u(0)=0$. $v(\frac1n)=\mathrm{e}^n$ ist unbeschränkt, $v$ ist nicht stetig ergänzbar.
:::
:::

::::formelsammlung
**Folgenstetigkeit**

$$\bigl(x_n\to x_0\text{ für }n\to\infty\bigr)\quad\Longrightarrow\quad\bigl(f(x_n)\to f(x_0)\text{ für }n\to\infty\bigr)$$

Für alle Folgen in $(a,b)$, auch mit $x_n=x_0$. Gleichwertig zur Stetigkeit in $x_0$.

**Vertauschen von Grenzwert und Funktion**

$$\lim_{n\to\infty}f(x_n)=f\Bigl(\lim_{n\to\infty}x_n\Bigr)$$

Für $f$ stetig in $x_0$ und $x_n\to x_0$.

**Verknüpfungen**

$$f+g,\qquad f\cdot g,\qquad f/g$$

Stetig in $x_0$, wenn $f,g:(a,b)\to\mathbb{R}$ in $x_0$ stetig sind; der Quotient nur, sofern $g(x_0)\ne0$.

**Verkettung**

$$g\circ f:(a,b)\to\mathbb{R}$$

Stetig in $x_0$, wenn $f$ in $x_0$ und $g$ in $y_0:=f(x_0)$ stetig ist; dabei $\mathcal W(f)\subset(c,d)$ für $g:(c,d)\to\mathbb{R}$.

**Rationale Funktionen**

$$\mathcal D(R)=\{x:Q_m(x)\ne0\}$$

$R=P_n/Q_m$ ist auf $\mathcal D(R)$ stetig.

**Stetigkeit der Exponentialfunktion**

$$1+x\le\mathrm{e}^x\le\frac1{1-|x|},\qquad\mathrm{e}^x=\mathrm{e}^{x_0}\cdot\mathrm{e}^{x-x_0}$$

Links für $|x|<1$: Stetigkeit in 0. Rechts: Die Funktionalgleichung verschiebt jede Stelle nach 0. Ebenso stetig: $k(x)=\mathrm{e}^x+x$ als Summe, $a^x=\mathrm{e}^{x\log a}$ als Verkettung.
::::

::::lernkarten
:::karte begriff folgenstetig
Wann heißt $f:(a,b)\to\mathbb{R}$ in $x_0\in(a,b)$ folgenstetig, und welche Folgen sind dabei zugelassen?
---
Wenn für alle reellen Folgen $\{x_n\}$ in $(a,b)$ gilt: Aus $x_n\to x_0$ folgt $f(x_n)\to f(x_0)$. Anders als bei den Testfolgen des Grenzwerts ist auch $x_n=x_0$ zugelassen.
--- falsch
Wenn es eine Folge $\{x_n\}$ in $(a,b)$ mit $x_n\to x_0$ und $f(x_n)\to f(x_0)$ gibt. Zugelassen sind nur Folgen mit $x_n\ne x_0$, wie bei den Testfolgen des Grenzwerts.
--- falsch
Wenn für alle Folgen $\{x_n\}$ in $(a,b)$ gilt: Aus $f(x_n)\to f(x_0)$ folgt $x_n\to x_0$. Zugelassen sind auch Folgen mit $x_n=x_0$, anders als beim Grenzwert.
--- falsch
Wenn für alle Folgen $\{x_n\}$ in $(a,b)$ mit $x_n\to x_0$ die Bildfolge $f(x_n)$ überhaupt konvergiert, gleich wogegen. Zugelassen ist dabei auch $x_n=x_0$.
:::
:::karte formel Vertauschen von Grenzwert und Funktion
Welche Vertauschung von Grenzwert und Funktion erlaubt eine in $x_0$ folgenstetige Funktion $f$?
---
$\lim_{n\to\infty}f(x_n)=f\Bigl(\lim_{n\to\infty}x_n\Bigr)$ für jede Folge in $(a,b)$ mit $x_n\to x_0$: Man darf den Grenzwert in die stetige Funktion hineinziehen.
--- falsch
$\lim_{n\to\infty}f(x_n)=\lim_{n\to\infty}x_n$ für jede Folge in $(a,b)$ mit $x_n\to x_0$: Bei einer stetigen Funktion haben Eingangsfolge und Bildfolge denselben Grenzwert.
--- falsch
$\lim_{n\to\infty}f(x_n)=f\Bigl(\lim_{n\to\infty}x_n\Bigr)$ für jede Funktion und jede konvergente Folge: Die Vertauschung ist eine Rechenregel für Grenzwerte und braucht keine Stetigkeit.
--- falsch
$f\Bigl(\lim_{n\to\infty}x_n\Bigr)=f(x_0)\cdot\lim_{n\to\infty}x_n$ für jede Folge mit $x_n\to x_0$: Man darf den Funktionswert als Faktor vor den Grenzwert ziehen.
:::
:::karte zusammenhang Stetig heißt folgenstetig
Wie hängen Stetigkeit und Folgenstetigkeit in $x_0$ zusammen, und warum gilt das in beiden Richtungen?
---
Sie sind gleichwertig. Folgenstetig verlangt dasselbe für mehr Folgen; umgekehrt braucht der Beweis über das Epsilon-Delta-Kriterium $x_n\ne x_0$ nirgends, weil das Kriterium auch für $x=x_0$ gilt.
--- falsch
Folgenstetig ist schwächer: Aus der Stetigkeit folgt die Folgenstetigkeit, aber nicht umgekehrt, weil die Folgenstetigkeit weniger Folgen prüft als der Grenzwert, nämlich nur solche mit $x_n=x_0$.
--- falsch
Sie sind unabhängig: Stetigkeit betrifft den Funktionswert, Folgenstetigkeit nur das Verhalten von Folgen; eine Funktion kann in $x_0$ stetig sein, ohne dort folgenstetig zu sein, und umgekehrt.
--- falsch
Folgenstetig ist stärker: Aus ihr folgt die Stetigkeit, aber nicht umgekehrt, weil eine stetige Funktion bei Folgen mit $x_n=x_0$ versagen kann; der Grenzwert prüft solche Folgen ja nicht.
:::
:::karte zusammenhang Verkettung und Testfolgen
Warum lässt man bei der Folgenstetigkeit auch Folgen mit $x_n=x_0$ zu?
---
Weil das bei Verkettungen nötig ist: Die Bildfolge $f(x_n)$ kann $f(x_0)$ treffen, selbst wenn $x_n\ne x_0$ ist. Als Eingangsfolge der äußeren Funktion muss sie trotzdem zählen.
--- falsch
Weil Folgen mit $x_n\ne x_0$ bei stetigen Funktionen nie gegen $x_0$ laufen; ohne $x_n=x_0$ gäbe es gar keine Folgen, mit denen man die Stetigkeit prüfen könnte.
--- falsch
Weil man damit den Wert $f(x_0)$ mitprüft: Folgen mit $x_n=x_0$ zeigen, ob $f$ in $x_0$ erklärt ist, und mehr als das verlangt die Stetigkeit nicht.
--- falsch
Weil konstante Folgen am leichtesten zu berechnen sind; man prüft die Stetigkeit dann nur noch mit der Folge $x_n=x_0$ und spart sich alle anderen Folgen.
:::
:::karte formel Verknüpfungen stetiger Funktionen
Welche Verknüpfungen zweier in $x_0$ stetiger Funktionen $f,g:(a,b)\to\mathbb{R}$ sind wieder in $x_0$ stetig?
---
$f+g$, $f\cdot g$ und, sofern $g(x_0)\ne0$, auch $f/g$. Das sind die Rechenregeln für Grenzwerte von Funktionen mit $y_0=f(x_0)$ und $w_0=g(x_0)$.
--- falsch
$f+g$ und $f-g$, aber nicht $f\cdot g$ und $f/g$: Beim Multiplizieren können sich kleine Änderungen so stark verstärken, dass Sprünge entstehen.
--- falsch
$f+g$, $f\cdot g$ und $f/g$, auch wenn $g(x_0)=0$ ist: Der Quotient wird dann zwar groß, aber eine kleine Änderung am Eingang bleibt eine kleine Änderung.
--- falsch
$f+g$, $f\cdot g$ und, sofern $g(x_0)\ne0$, auch $f/g$; das gilt aber nur, wenn $f$ und $g$ auf ganz $(a,b)$ stetig sind, nicht bloß in $x_0$.
:::
:::karte formel Verkettung stetiger Funktionen
Unter welchen Voraussetzungen ist die Verkettung $g\circ f$ in $x_0$ stetig?
---
Für $f:(a,b)\to\mathbb{R}$, $g:(c,d)\to\mathbb{R}$ mit $\mathcal W(f)\subset(c,d)$: Ist $f$ in $x_0\in(a,b)$ stetig und $g$ in $y_0:=f(x_0)$ stetig, dann ist $g\circ f:(a,b)\to\mathbb{R}$ in $x_0$ stetig.
--- falsch
Für $f:(a,b)\to\mathbb{R}$, $g:(c,d)\to\mathbb{R}$ mit $\mathcal W(f)\subset(c,d)$: Ist $f$ in $x_0$ stetig und $g$ ebenfalls in derselben Stelle $x_0$ stetig, dann ist $g\circ f$ in $x_0$ stetig.
--- falsch
Für $f:(a,b)\to\mathbb{R}$, $g:(c,d)\to\mathbb{R}$: Ist $g$ in $y_0:=f(x_0)$ stetig, dann ist $g\circ f$ in $x_0$ stetig, gleich ob $f$ in $x_0$ stetig ist, denn die äußere Funktion glättet.
--- falsch
Für $f:(a,b)\to\mathbb{R}$, $g:(c,d)\to\mathbb{R}$ mit $\mathcal W(f)\subset(c,d)$: Ist $f$ in $x_0$ stetig, dann ist $g\circ f$ in $x_0$ stetig, auch wenn $g$ springt, weil $f$ die Werte vorher glättet.
:::
:::karte herleitung Verkettung über Folgen
Wie zeigt man mit der Folgenstetigkeit, dass $g\circ f$ in $x_0$ stetig ist, wenn $f$ in $x_0$ und $g$ in $y_0=f(x_0)$ stetig ist?
---
Man nimmt eine Folge $x_n\to x_0$ in $(a,b)$, weil Stetigkeit gleichwertig zur Folgenstetigkeit ist und man diese für jede Folge zeigen muss.
---
Es gilt $y_n:=f(x_n)\to y_0$, weil $f$ in $x_0$ folgenstetig ist.
---
Es gilt $g(y_n)\to g(y_0)$, weil $g$ in $y_0$ folgenstetig ist; dabei darf $y_n=y_0$ vorkommen, weil die Folgenstetigkeit solche Glieder zulässt.
---
Also gilt $(g\circ f)(x_n)\to(g\circ f)(x_0)$, weil $(g\circ f)(x_n)=g(y_n)$ ist.
:::
:::karte herleitung Stetigkeit der Exponentialfunktion
Wie zeigt man, dass $\exp$ auf ganz $\mathbb{R}$ stetig ist, erst bei 0 und dann an jeder Stelle $x_0$?
---
Für $|x|<1$ gilt $1+x\le\mathrm{e}^x\le\frac1{1-|x|}$, weil $\mathrm{e}^x\ge1+x$ und $|\mathrm{e}^x-1|\le\frac{|x|}{1-|x|}$ gelten.
---
Beide Schranken laufen für $x\to0$ gegen 1, also gibt das Vergleichskriterium $\lim_{x\to0}\mathrm{e}^x=1=\mathrm{e}^0$, weil $\mathrm{e}^x$ zwischen ihnen eingeklemmt ist.
---
Bei $x_0\ne0$ schreibt man $\mathrm{e}^x=\mathrm{e}^{x_0}\cdot\mathrm{e}^{x-x_0}$, weil die Funktionalgleichung so jede Stelle nach 0 verschiebt.
---
Das ist die Konstante $\mathrm{e}^{x_0}$ mal der Verkettung von $x\mapsto x-x_0$ (stetig in $x_0$) mit $\exp$ (stetig in 0), also stetig in $x_0$, weil Verkettung und Produkt die Stetigkeit erhalten.
:::
:::karte zusammenhang rationale Funktion
Warum ist jede rationale Funktion $R=P_n/Q_m$ auf $\mathcal D(R)=\{x:Q_m(x)\ne0\}$ stetig?
---
Polynome sind stetig, weil ihr Grenzwert durch Einsetzen entsteht. Der Quotient zweier in $x_0$ stetiger Funktionen ist dort stetig, sofern der Nenner nicht null ist, und auf $\mathcal D(R)$ gilt $Q_m(x)\ne0$.
--- falsch
Weil rationale Funktionen keine Pole haben können: Zähler und Nenner sind Polynome, und ein Quotient von Polynomen bleibt überall beschränkt und ist damit auch überall stetig.
--- falsch
Weil man jede rationale Funktion kürzen kann, bis der Nenner keine Nullstelle mehr hat; danach ist sie ein Polynom und damit auf ganz $\mathbb{R}$ stetig, auch an den früheren Nullstellen.
--- falsch
Sie ist es nur dort, wo auch der Zähler nicht null ist: An Nullstellen des Zählers springt der Quotient, deshalb muss man auch sie aus dem Definitionsbereich $\mathcal D(R)$ entfernen.
:::
:::karte zusammenhang Umkehrung der Verknüpfungssätze
Folgt aus der Stetigkeit der Summe $f+g$, dass $f$ und $g$ einzeln stetig sind?
---
Nein: $H$ und $1-H$ springen beide bei 0, ihre Summe ist die stetige Funktion 1. Die Sätze über Verknüpfungen gelten nur in einer Richtung, von den Teilen zum Ganzen.
--- falsch
Ja: Ein Sprung von $f$ bei $x_0$ bliebe in der Summe sichtbar, denn die Sätze über Verknüpfungen gelten in beiden Richtungen, vom Ganzen zu den Teilen ebenso wie umgekehrt.
--- falsch
Ja, sofern auch das Produkt $f\cdot g$ stetig ist: Summe und Produkt zusammen legen $f$ und $g$ fest, und die Stetigkeit überträgt sich dann auf beide Funktionen.
--- falsch
Ja, wenn $f$ und $g$ beschränkt sind: Dann kann keine der beiden einen Sprung haben, den die andere ausgleicht, weil ein solcher Ausgleich unbeschränkte Werte bräuchte.
:::
:::karte zusammenhang Prüffunktion und allgemeine Potenz
Warum sind die Prüffunktion $k(x)=\mathrm{e}^x+x$ und die allgemeine Potenz $a^x$ stetig?
---
$k$ ist als Summe der stetigen Funktionen $\mathrm{e}^x$ und $x$ stetig. $a^x=\mathrm{e}^{x\log a}$ ist die Verkettung der stetigen Funktion $x\mapsto x\log a$ mit der stetigen Funktion $\exp$.
--- falsch
$k$ ist stetig, weil $k(0)=1$ und $k(1)=\mathrm{e}+1$ beide endlich sind. $a^x$ ist stetig, weil $a^x$ für jedes $x$ positiv ist und positive Funktionen nicht springen können.
--- falsch
$k$ ist stetig, weil $k$ streng wächst und streng wachsende Funktionen nicht springen können. $a^x$ ist stetig, weil $a^x$ für $a>1$ ebenfalls streng wächst.
--- falsch
$k$ ist als Summe stetig. $a^x=\mathrm{e}^{x\log a}$ ist dagegen nur an rationalen Stellen stetig, weil die Potenz für irrationale $x$ erst über einen Grenzwert erklärt ist.
:::
::::
