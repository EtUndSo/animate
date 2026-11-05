---
title: Die Kettenregel
pfad: Informatik / Machine Learning / Ableitung, Gradient und Kettenregel
order: 6230300
summary: Viele Funktionen entstehen, indem man eine Funktion in eine andere einsetzt.
tags: Verkettung, logistische Funktion
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Viele Funktionen entstehen, indem man eine Funktion in eine andere einsetzt. Die Kettenregel sagt, wie sich die Ableitung einer solchen Verkettung aus den Ableitungen der Teile ergibt: Die Faktoren der einzelnen Stufen werden multipliziert. Das gilt für Ketten aus beliebig vielen Gliedern. Am Ende steht die logistische Funktion, deren Ableitung sich durch die Funktion selbst ausdrücken lässt.
:::

### Verkettung

<span class="anker" id="stufe-2-1"></span>

Die Funktion $(3x+1)^2$ rechnet man in zwei Schritten aus: zuerst $u=3x+1$, dann $u^2$. Viele Formeln sind so gebaut, als Hintereinanderausführung einfacher Schritte. Wer diese Bauweise erkennt, kann die Ableitung aus den Ableitungen der Schritte zusammensetzen.

:::definition Definition 2.1 (Verkettung)
<span class="anker" id="satz-2-1"></span>

Sind $g$ und $f$ Funktionen und liegt jeder Wert $g(x)$ dort, wo $f$ erklärt ist, so heißt die Funktion

$$(f\circ g)(x)=f\bigl(g(x)\bigr)$$

die __Verkettung__ von $f$ und $g$, gelesen „$f$ nach $g$“. Die zuerst angewandte Funktion $g$ heißt innere Funktion, $f$ heißt äußere Funktion.
:::

⁠**Rechenbeispiel:** Für $F(x)=(3x+1)^2$ ist die innere Funktion $g(x)=3x+1$ und die äußere $f(u)=u^2$, also $F=f\circ g$. An der Stelle $1$ ist $g(1)=4$ und $F(1)=f(4)=16$. Die Reihenfolge zählt: $(g\circ f)(x)=g(f(x))=3x^2+1$ ist eine andere Funktion, mit dem Wert $4$ an der Stelle $1$.

⁠**Kurz gesagt:** Eine Verkettung $f\circ g$ wendet zuerst $g$ und dann $f$ an; die Reihenfolge ist nicht vertauschbar.

### Die Kettenregel

<span class="anker" id="stufe-2-2"></span>

Wie reagiert $F=f\circ g$ auf eine kleine Änderung von $x$? Man verfolgt die Änderung durch die beiden Stufen. Die erste Stufe gibt eine kleine Änderung $\Delta x$ nach der linearen Näherung ungefähr als $\Delta u\approx g'(x)\,\Delta x$ weiter. Die zweite Stufe gibt diese Änderung als $\Delta y\approx f'(u)\,\Delta u$ weiter. Zusammen ist $\Delta y\approx f'(u)\,g'(x)\,\Delta x$. Wie bei einem Getriebe aus zwei Übersetzungsstufen multiplizieren sich die Faktoren der Stufen (Abb. [4](#abb-4)).

:::abbildung ml/k3getriebe 4
Die Kettenregel als Getriebe für $y=(3x+1)^2$ an der Stelle $1$. Alle drei Zahlenstrahlen haben denselben Maßstab. Das Stück $\Delta x=0{,}01$ (blau) wird von der ersten Stufe auf das Dreifache gestreckt, $\Delta u=0{,}03$ (orange), und von der zweiten Stufe auf ungefähr das Achtfache davon, $\Delta y=0{,}2409\approx0{,}24$ (rot).
:::

:::satz Satz 2.2 (Kettenregel)
<span class="anker" id="satz-2-2"></span>

Ist $g$ an der Stelle $x$ differenzierbar und $f$ an der Stelle $g(x)$ differenzierbar, so ist $f\circ g$ an der Stelle $x$ differenzierbar, und

<span class="anker" id="gl-2-1"></span>
$$(f\circ g)'(x)=f'\bigl(g(x)\bigr)\cdot g'(x). \tag{2.1}$$
:::

Wichtig ist, wo die Ableitungen ausgewertet werden: $g'$ an der Stelle $x$, $f'$ aber an der Stelle $u=g(x)$, also dort, wo die äußere Funktion tatsächlich arbeitet. Mit $u=g(x)$ und $y=f(u)$ schreibt man die Regel oft als $\frac{\mathrm{d} y}{\mathrm{d} x}=\frac{\mathrm{d} y}{\mathrm{d} u}\cdot\frac{\mathrm{d} u}{\mathrm{d} x}$. Das sieht aus, als kürze sich $\mathrm{d} u$ heraus. Als Merkhilfe ist das nützlich, als Begründung nicht, denn die Zeichen sind keine Brüche, sondern Grenzwerte.

:::beweis Kettenregel
Es sei $u=g(x)$. Nach der linearen Näherung [(1.4)](die-ableitung.html#gl-1-4) ist $g(x+h)=u+g'(x)\,h+r_g(h)$ mit $r_g(h)/h\to0$ und $f(u+k)=f(u)+f'(u)\,k+r_f(k)$ mit $r_f(k)/k\to0$; dabei sei $r_f(0)=0$. Man setzt $k=g(x+h)-u=g'(x)\,h+r_g(h)$. Dann ist

$$f\bigl(g(x+h)\bigr)-f(u)=f'(u)\,k+r_f(k)=f'(u)\,g'(x)\,h+f'(u)\,r_g(h)+r_f(k).$$

Nach Division durch $h$ geht der mittlere Summand gegen $0$. Für den letzten schreibt man $r_f(k)/h=\bigl(r_f(k)/k\bigr)\cdot(k/h)$, solange $k\ne0$ ist; der erste Faktor geht gegen $0$, weil mit $h$ auch $k$ gegen $0$ geht, und der zweite gegen $g'(x)$. Ist $k=0$, so ist der Summand ohnehin $0$. Übrig bleibt $f'(u)\,g'(x)$.
:::

⁠**Rechenbeispiel:** Für $F(x)=(3x+1)^2$ ist $g'(x)=3$ und $f'(u)=2u$. An der Stelle $1$ ist $u=g(1)=4$, also

$$F'(1)=f'(4)\cdot g'(1)=8\cdot3=24 .$$

Probe: Ausmultipliziert ist $F(x)=9x^2+6x+1$, also $F'(x)=18x+6$ und $F'(1)=24$. Abb. [4](#abb-4) zeigt dasselbe mit Zahlen: $F(1{,}01)=4{,}03^2=16{,}2409$, die lineare Näherung sagt $16+24\cdot0{,}01=16{,}24$ voraus.

⁠**Kurz gesagt:** Bei einer Verkettung multiplizieren sich die Ableitungen der Stufen, jede an der Stelle ausgewertet, an der ihre Stufe arbeitet: $(f\circ g)'(x)=f'(g(x))\,g'(x)$.

### Ketten aus vielen Gliedern

<span class="anker" id="stufe-2-3"></span>

Die meisten Rechnungen bestehen aus mehr als zwei Schritten. Die Kettenregel lässt sich wiederholt anwenden: Bei drei Stufen ist $f_3\circ f_2\circ f_1=f_3\circ(f_2\circ f_1)$, und zweimal angewandt ergibt [(2.1)](#gl-2-1) ein Produkt aus drei Faktoren. Bei beliebig vielen Stufen gilt dasselbe.

:::satz Satz 2.3 (Kettenregel für viele Glieder)
<span class="anker" id="satz-2-3"></span>

Es sei $u_0=x$ und $u_k=f_k(u_{k-1})$ für $k=1,\dots,L$, und jede Funktion $f_k$ sei an der Stelle $u_{k-1}$ differenzierbar. Dann ist

<span class="anker" id="gl-2-2"></span>
$$\frac{\mathrm{d} u_L}{\mathrm{d} x}=f_L'(u_{L-1})\cdot f_{L-1}'(u_{L-2})\cdots f_1'(u_0). \tag{2.2}$$
:::

Für die Rechnung folgt daraus eine Reihenfolge. Jeder Faktor braucht den Wert, an dem seine Stufe arbeitet. Man rechnet deshalb zuerst die Zwischenwerte $u_1,u_2,\dots$ aus, wie bei der gewöhnlichen Auswertung, und erst dann die Faktoren. In welcher Reihenfolge man die Faktoren danach multipliziert, ist bei Zahlen gleichgültig.

⁠**Rechenbeispiel:** Es sei $y=\dfrac1{(x^2+1)^3}$ an der Stelle $x=1$. Die Kette hat drei Glieder:

$$u_1=x^2+1=2,\qquad u_2=u_1^3=8,\qquad y=\frac1{u_2}=\frac18 .$$

Die Faktoren sind $\frac{\mathrm{d} u_1}{\mathrm{d} x}=2x=2$, $\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=3u_1^2=12$ und $\frac{\mathrm{d} y}{\mathrm{d} u_2}=-\frac1{u_2^2}=-\frac1{64}$, also

$$\frac{\mathrm{d} y}{\mathrm{d} x}=2\cdot12\cdot\Bigl(-\frac1{64}\Bigr)=-\frac{24}{64}=-0{,}375 .$$

Probe: $y=(x^2+1)^{-3}$ hat nach Potenz- und Kettenregel die Ableitung $-3\,(x^2+1)^{-4}\cdot2x$, an der Stelle $1$ also $-6/16=-0{,}375$.

⁠**Kurz gesagt:** Bei einer langen Kette ist die Ableitung das Produkt der Ableitungen aller Glieder; zuerst berechnet man die Zwischenwerte, dann die Faktoren.

### Die logistische Funktion

<span class="anker" id="stufe-2-4"></span>

Manche Größen sollen glatt zwischen zwei Grenzen liegen, etwa ein Anteil zwischen $0$ und $1$. Eine Funktion, die jede reelle Zahl in diesen Bereich abbildet, ohne Sprung und ohne Knick und stets wachsend, ist die logistische Funktion. Sie beschreibt auch Wachstum mit Sättigung: Eine Größe wächst zuerst fast exponentiell und nähert sich dann einer Obergrenze. Ihre Ableitung ist ein schönes Beispiel für die Kettenregel und hat eine bemerkenswerte Form.

:::definition Definition 2.4 (Logistische Funktion)
<span class="anker" id="satz-2-4"></span>

Die Funktion

<span class="anker" id="gl-2-3"></span>
$$\sigma(x)=\frac1{1+\mathrm{e}^{-x}} \tag{2.3}$$

heißt __logistische Funktion__.
:::

Für große positive $x$ ist $\mathrm{e}^{-x}$ fast $0$ und $\sigma(x)$ fast $1$. Für große negative $x$ ist $\mathrm{e}^{-x}$ riesig und $\sigma(x)$ fast $0$. An der Stelle $0$ ist $\sigma(0)=\tfrac12$. Außerdem gilt $\sigma(-x)=1-\sigma(x)$, denn $\frac1{1+\mathrm{e}^{x}}=\frac{\mathrm{e}^{-x}}{\mathrm{e}^{-x}+1}=1-\frac1{1+\mathrm{e}^{-x}}$; der Graph ist also punktsymmetrisch zum Punkt $(0,\,\tfrac12)$ (Abb. [5](#abb-5)).

:::satz Satz 2.5 (Ableitung der logistischen Funktion)
<span class="anker" id="satz-2-5"></span>

Es gilt

<span class="anker" id="gl-2-4"></span>
$$\sigma'(x)=\sigma(x)\,\bigl(1-\sigma(x)\bigr). \tag{2.4}$$

Die Ableitung ist überall positiv und höchstens $\tfrac14$; den größten Wert $\tfrac14$ hat sie an der Stelle $0$.
:::

:::herleitung Die Ableitung der logistischen Funktion
Die Funktion ist eine Kette aus drei Gliedern: $u_1=-x$, $u_2=1+\mathrm{e}^{u_1}$, $\sigma=1/u_2$. Die Faktoren sind $-1$, $\mathrm{e}^{u_1}=\mathrm{e}^{-x}$ und $-1/u_2^2$. Nach [(2.2)](#gl-2-2) ist

$$\sigma'(x)=-\frac1{(1+\mathrm{e}^{-x})^2}\cdot\mathrm{e}^{-x}\cdot(-1)=\frac{\mathrm{e}^{-x}}{(1+\mathrm{e}^{-x})^2}=\frac1{1+\mathrm{e}^{-x}}\cdot\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}} .$$

Der erste Faktor ist $\sigma(x)$. Der zweite ist $\frac{(1+\mathrm{e}^{-x})-1}{1+\mathrm{e}^{-x}}=1-\sigma(x)$. Weil $\sigma(x)$ zwischen $0$ und $1$ liegt, sind beide Faktoren positiv. Für eine Zahl $p$ zwischen $0$ und $1$ ist $p\,(1-p)=\tfrac14-(p-\tfrac12)^2\le\tfrac14$, mit Gleichheit genau für $p=\tfrac12$, also für $x=0$.
:::

:::abbildung ml/k3logistisch 5
Die logistische Funktion $\sigma$ (blau) steigt von $0$ nach $1$, am steilsten an der Stelle $0$. Ihre Ableitung (rot) hat dort den größten Wert $\tfrac14$ und wird zu beiden Seiten schnell klein. Markiert sind die Werte an den Stellen $0$ und $2$ aus dem Rechenbeispiel.
:::

⁠**Rechenbeispiel:** An der Stelle $2$ ist $\mathrm{e}^{-2}\approx0{,}1353$, also $\sigma(2)\approx1/1{,}1353\approx0{,}8808$ und

$$\sigma'(2)=\sigma(2)\,\bigl(1-\sigma(2)\bigr)\approx0{,}8808\cdot0{,}1192\approx0{,}1050 .$$

Ist $\sigma(2)$ einmal ausgerechnet, kostet die Ableitung nur noch eine Subtraktion und eine Multiplikation, keine weitere e-Funktion. An der Stelle $10$ ist $\sigma(10)\approx0{,}99995$ und $\sigma'(10)\approx0{,}0000454$: Weit draußen ist die Funktion fast waagrecht, kleine Änderungen der Eingabe kommen kaum noch am Ausgang an.

⁠**Kurz gesagt:** Die logistische Funktion $\sigma(x)=1/(1+\mathrm{e}^{-x})$ bildet jede Zahl glatt in das Intervall zwischen $0$ und $1$ ab; ihre Ableitung ist $\sigma(1-\sigma)$, höchstens $\tfrac14$, und lässt sich aus dem Funktionswert allein berechnen.

:::aufgabe Aufgabe 5 ★ Glockenkurve
<span class="anker" id="aufg-5"></span>

Es sei $f(x)=\mathrm{e}^{-x^2}$.

<ol class="al">

<li>

Bestimme innere und äußere Funktion und berechne $f'(x)$.

</li>

<li>

Berechne $f'(0)$, $f'(1)$ und $f'(-1)$ und deute die Vorzeichen am Graphen.

</li>

</ol>

:::loesung
(a) Die innere Funktion ist $u=-x^2$ mit $u'=-2x$, die äußere $\mathrm{e}^u$ mit der Ableitung $\mathrm{e}^u$. Nach der Kettenregel ist $f'(x)=\mathrm{e}^{-x^2}\cdot(-2x)=-2x\,\mathrm{e}^{-x^2}$.

(b) $f'(0)=0$: Der Graph hat an der Stelle $0$ eine waagrechte Tangente, er hat dort seinen Gipfel. $f'(1)=-2/\mathrm{e}\approx-0{,}7358$: Rechts vom Gipfel fällt er. $f'(-1)=2/\mathrm{e}\approx0{,}7358$: Links vom Gipfel steigt er. Weil $f(-x)=f(x)$ ist, sind die Steigungen an den Stellen $\pm1$ entgegengesetzt gleich.
:::
:::

:::aufgabe Aufgabe 6 ★★ Eine Kette aus drei Gliedern
<span class="anker" id="aufg-6"></span>

Es sei $y=\sqrt{1+x^4}$.

<ol class="al">

<li>

Zerlege die Funktion in drei Glieder $u_1$, $u_2$, $y$ und berechne an der Stelle $x=1$ zuerst alle Zwischenwerte, dann alle Faktoren.

</li>

<li>

Berechne $\frac{\mathrm{d} y}{\mathrm{d} x}$ an der Stelle $1$ als Produkt der Faktoren und mache die Probe mit der Kettenregel in einem Schritt.

</li>

</ol>

:::loesung
(a) Die Glieder sind $u_1=x^4$, $u_2=1+u_1$ und $y=\sqrt{u_2}$. An der Stelle $1$ sind die Zwischenwerte $u_1=1$, $u_2=2$ und $y=\sqrt2\approx1{,}4142$. Die Faktoren sind $\frac{\mathrm{d} u_1}{\mathrm{d} x}=4x^3=4$, $\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=1$ und $\frac{\mathrm{d} y}{\mathrm{d} u_2}=\frac1{2\sqrt{u_2}}=\frac1{2\sqrt2}\approx0{,}3536$.

(b) Das Produkt ist $4\cdot1\cdot\frac1{2\sqrt2}=\frac2{\sqrt2}=\sqrt2\approx1{,}4142$. In einem Schritt: $y'=\frac1{2\sqrt{1+x^4}}\cdot4x^3$, an der Stelle $1$ also $\frac4{2\sqrt2}=\sqrt2$.
:::
:::

:::aufgabe Aufgabe 7 ★★ Eigenschaften der logistischen Funktion
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Zeige mit [(2.4)](#gl-2-4) und $\sigma(-x)=1-\sigma(x)$, dass $\sigma'(-x)=\sigma'(x)$ ist. Was bedeutet das für den Graphen von $\sigma'$?

</li>

<li>

Berechne $\sigma(1)$ und $\sigma'(1)$ auf vier Stellen.

</li>

<li>

Berechne die zweite Ableitung $\sigma''$, ausgedrückt durch $\sigma$, und bestimme ihr Vorzeichen für $x>0$ und für $x<0$. Was sagt das über die Krümmung des Graphen von $\sigma$?

</li>

</ol>

:::loesung
(a) Mit $\sigma(-x)=1-\sigma(x)$ ist $\sigma'(-x)=\sigma(-x)\,\bigl(1-\sigma(-x)\bigr)=\bigl(1-\sigma(x)\bigr)\,\sigma(x)=\sigma'(x)$. Der Graph von $\sigma'$ ist spiegelsymmetrisch zur senkrechten Achse, wie Abb. [5](#abb-5) zeigt.

(b) $\mathrm{e}^{-1}\approx0{,}3679$, also $\sigma(1)=1/1{,}3679\approx0{,}7311$ und $\sigma'(1)\approx0{,}7311\cdot0{,}2689\approx0{,}1966$.

(c) Mit der Produkt- und der Kettenregel: $\sigma''=(\sigma-\sigma^2)'=\sigma'-2\sigma\sigma'=\sigma'\,(1-2\sigma)=\sigma(1-\sigma)(1-2\sigma)$. Für $x>0$ ist $\sigma>\tfrac12$, also $1-2\sigma<0$ und $\sigma''<0$: Der Graph biegt sich dort nach unten. Für $x<0$ ist $\sigma''>0$, und er biegt sich nach oben. An der Stelle $0$ wechselt die Krümmung ihr Vorzeichen; dort ist die Steigung am größten.
:::
:::

:::aufgabe Aufgabe 8 ★★★ Die Ableitung einer Umkehrfunktion
<span class="anker" id="aufg-8"></span>

Für $x>0$ gilt $\mathrm{e}^{\ln x}=x$.

<ol class="al">

<li>

Leite beide Seiten mit der Kettenregel nach $x$ ab und folgere $(\ln x)'=1/x$, unter der Annahme, dass $\ln$ differenzierbar ist.

</li>

<li>

Verfahre ebenso mit $(\sqrt x)^2=x$ und vergleiche mit der Potenzregel.

</li>

<li>

Die Umkehrfunktion der logistischen Funktion ist $\ell(p)=\ln\frac{p}{1-p}$ für $0<p<1$. Prüfe $\ell(\sigma(x))=x$ und berechne $\ell'(p)$ einmal direkt und einmal über $\sigma'$.

</li>

</ol>

:::loesung
(a) Die linke Seite ist eine Verkettung mit der inneren Funktion $\ln x$ und der äußeren $\mathrm{e}^u$. Nach der Kettenregel ist ihre Ableitung $\mathrm{e}^{\ln x}\cdot(\ln x)'=x\cdot(\ln x)'$. Die rechte Seite hat die Ableitung $1$. Also ist $x\,(\ln x)'=1$ und $(\ln x)'=1/x$.

(b) Aus $(\sqrt x)^2=x$ folgt $2\sqrt x\cdot(\sqrt x)'=1$, also $(\sqrt x)'=\frac1{2\sqrt x}=\tfrac12x^{-1/2}$, genau die Potenzregel mit $n=\tfrac12$.

(c) Es ist $1-\sigma(x)=\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}}$, also $\frac{\sigma(x)}{1-\sigma(x)}=\frac1{\mathrm{e}^{-x}}=\mathrm{e}^x$ und $\ell(\sigma(x))=\ln\mathrm{e}^x=x$. Direkt ist $\ell(p)=\ln p-\ln(1-p)$ und

$$\ell'(p)=\frac1p+\frac1{1-p}=\frac{1}{p\,(1-p)} .$$

Über $\sigma'$: Ableiten von $\ell(\sigma(x))=x$ ergibt $\ell'(\sigma(x))\cdot\sigma'(x)=1$, also $\ell'(p)=\frac1{\sigma'(x)}=\frac1{p(1-p)}$ mit $p=\sigma(x)$. Wo $\sigma$ flach ist, ist ihre Umkehrfunktion steil.
:::
:::
