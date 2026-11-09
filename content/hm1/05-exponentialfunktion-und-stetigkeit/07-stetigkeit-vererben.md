---
title: Stufe 5: Stetigkeit vererben
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
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
