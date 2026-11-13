---
title: Stufe 8: Jede Nullstelle spaltet einen Linearfaktor ab
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
order: 1231000
summary: Jetzt lässt sich die Frage vom Anfang beantworten: Warum gehört zu jeder Lösung von P(x)=0 ein Faktor, und wie viele Lösungen kann es geben?
tags: m-fache Nullstelle, Vielfachheit
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Jetzt lässt sich die Frage vom Anfang beantworten: Warum gehört zu jeder Lösung von $P(x)=0$ ein Faktor, und wie viele Lösungen kann es geben?
:::

**Die Idee.** Der Satz [7.2](das-horner-schema.html#satz-7-2) schreibt jedes Polynom als $P(x)=(x-x_0)\,Q(x)+c_0$. Setzt man $x=x_0$ ein, verschwindet der erste Summand, weil sein Faktor $x-x_0$ null ist. Es bleibt $P(x_0)=c_0$. Ist $x_0$ eine Nullstelle, ist der Rest null, und $x-x_0$ steckt als Faktor in $P$. **Kurz gesagt:** Der Rest der Division durch $x-x_0$ ist der Funktionswert an der Stelle $x_0$.

:::definition Definition 8.1 (Nullstelle und Vielfachheit)
<span class="anker" id="satz-8-1"></span>

$x_0\in\mathbb{R}$ heißt Nullstelle der reellen Funktion $f$, wenn $f(x_0)=0$ ist. $x_0$ heißt __$m$-fache Nullstelle__ des Polynoms $P_n$, wenn es ein Polynom $Q_{n-m}$ gibt mit

<span class="anker" id="gl-8-1"></span>
$$P_n(x)=(x-x_0)^m\,Q_{n-m}(x)\quad\text{und}\quad Q_{n-m}(x_0)\neq0. \tag{8.1}$$

$m$ heißt die __Vielfachheit__ der Nullstelle $x_0$.
:::

⁠**So liest man das:** $m$ zählt, wie oft der Faktor $x-x_0$ in $P_n$ steckt. Es ist $m\le n$, denn der Grad $n-m$ von $Q_{n-m}$ kann nicht negativ sein.

:::satz Satz 8.2 (Linearfaktor)
<span class="anker" id="satz-8-2"></span>

Sei $P_n$ ein Polynom vom Grad $n\ge1$ und $x_0\in\mathbb{R}$. Dann gilt

<span class="anker" id="gl-8-2"></span>
$$P_n(x_0)=0\quad\Leftrightarrow\quad P_n(x)=(x-x_0)\,Q_{n-1}(x)\text{ mit einem Polynom }Q_{n-1}. \tag{8.2}$$

Deshalb hat $P_n$ höchstens $n$ Nullstellen, auch wenn man jede mit ihrer Vielfachheit zählt.
:::

:::beweis Linearfaktor
„$\Rightarrow$“: In [(7.3)](das-horner-schema.html#gl-7-3) ist $c_0=P_n(x_0)=0$. „$\Leftarrow$“: Einsetzen von $x_0$ ergibt den Faktor 0. **Anzahl:** Ein Produkt ist genau dann null, wenn ein Faktor null ist. Jede weitere Nullstelle von $P_n$ ist also eine Nullstelle von $Q_{n-1}$. Mit jeder abgespaltenen Nullstelle sinkt der Grad um 1, nach höchstens $n$ Schritten bleibt eine Konstante $a_n\neq0$ ohne Nullstelle.
:::

⁠**So liest man das:** Der *Linearfaktor* $x-x_0$ hat Grad 1 und ist genau bei $x_0$ null. **Warum $x_0\in\mathbb{R}$ nötig ist:** $x^2+1$ hat keine reelle Nullstelle und keinen reellen Linearfaktor. **Folge für den Identitätssatz:** Stimmen zwei Polynome vom Grad $\le n$ an $n+1$ Stellen überein, sind sie gleich, denn ihre Differenz hätte sonst zu viele Nullstellen.

**Zwei Darstellungen.** Spaltet man alle Nullstellen ab, entsteht eine Form, an der man sie direkt abliest:

<span class="anker" id="gl-8-3"></span>
$$P_n(x)=a_n(x-x_1)(x-x_2)\cdots(x-x_n), \tag{8.3}$$

mit $a_n\neq0$ und den Nullstellen $x_1,\dots,x_n\in\mathbb{R}$. Eine mehrfache Nullstelle steht mehrfach in der Liste. Hat ein Rest keine reelle Nullstelle mehr, bleiben quadratische Faktoren stehen:

<span class="anker" id="gl-8-4"></span>
$$P_n(x)=a_n(x^2+\beta_1x+\gamma_1)\cdots(x^2+\beta_kx+\gamma_k)\,(x-x_{2k+1})\cdots(x-x_n), \tag{8.4}$$

wobei $\beta_i^2-4\gamma_i<0$ ist, die quadratischen Faktoren also keine reellen Nullstellen haben. Die festen Zahlen $\beta_1,\dots,\beta_k,\gamma_1,\dots,\gamma_k,x_{2k+1},\dots,x_n$ sind $n$ Stück, wie die Koeffizienten $a_0,\dots,a_{n-1}$. Die $n-2k$ Zahlen $x_i$ sind die Nullstellen. Umgekehrt legen diese Zahlen $P_n$ durch Ausmultiplizieren eindeutig fest, für $n=4$ und $a_4=1$ in [(8.3)](#gl-8-3) ist

<span class="anker" id="gl-8-5"></span>
$$\begin{aligned} a_3&=-(x_1+x_2+x_3+x_4), & a_2&=x_1x_2+x_1x_3+x_1x_4+x_2x_3+x_2x_4+x_3x_4,\\ a_1&=-(x_1x_2x_3+x_1x_2x_4+x_1x_3x_4+x_2x_3x_4), & a_0&=x_1x_2x_3x_4. \end{aligned} \tag{8.5}$$

Nicht jedes reelle Polynom hat die Form [(8.3)](#gl-8-3), wie $x^2+1$ zeigt. Dass die Form [(8.4)](#gl-8-4) immer existiert, ist schwieriger und wird hier nicht bewiesen.

:::zusatz Warum quadratische Faktoren genügen
In den komplexen Zahlen ([Kapitel 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)) hat jedes Polynom vom Grad $n\ge1$ eine Nullstelle (Fundamentalsatz der Algebra). Bei reellen Koeffizienten ist mit $z$ auch $\overline{z}$ eine Nullstelle, und $(x-z)(x-\overline{z})=x^2-2\operatorname{Re}(z)\,x+|z|^2$ ist reell. Für $x^2+x+1$ ist $z=-\frac12+\frac{\sqrt3}{2}\,\mathrm{i}$.
:::

::::beispiel
Bei $S$ ergibt das Schema bei $x_0=2$ die Zeile $1,-1,-1,-2,0$, also $S(x)=(x-2)(x^3-x^2-x-2)$. Nochmals bei $x_0=2$: $1,1,1,0$, also $S(x)=(x-2)^2(x^2+x+1)$. Beim dritten Mal: $1,3,7$, der Rest $7\neq0$ beendet die Suche. Die Vielfachheit ist 2, und wegen $1-4=-3<0$ ist [(8.4)](#gl-8-4) erreicht, mit $n=4$, $k=1$.
::::

⁠**Grenzfall:** Für $m=n$ ist $P_n(x)=a_n(x-x_0)^n$, das Polynom mit nur einer Nullstelle.

**Was die Vielfachheit bewirkt.** Nahe $x_0$ ändert $Q_{n-m}(x)$ sein Vorzeichen nicht, es ist dort ja nicht null. Das Vorzeichen von $P_n$ bestimmt also $(x-x_0)^m$: Für ungerades $m$ wechselt es, der Graph kreuzt die Achse. Für gerades $m$ wechselt es nicht, der Graph berührt sie nur (Abb. [9](#abb-9)).

:::abbildung hm1/k3vielfach 9
Die Funktionen $(x-1)^m(x+2)$ für $m=1,2,3$ im selben Maßstab, jeweils mit der $m$-fachen Nullstelle $x_0=1$: Bei $m=1$ kreuzt der Graph die Achse, bei $m=2$ berührt er sie, bei $m=3$ kreuzt er sie flach.
:::

:::frage Ich finde eine Nullstelle. Woher weiß ich, ob es noch mehr gibt?
Der Quotient sagt es. Nach dem Abspalten liegt ein Polynom kleineren Grades vor, jede weitere Nullstelle von $P$ steckt in ihm. Bei Grad 2 hilft die Mitternachtsformel, bei $P$ etwa $2x^2+3x-2$ mit $D=25$ und den Nullstellen $\frac12$ und $-2$. Bei höherem Grad probiert man im Quotienten weiter. Bei ganzen Koeffizienten und $a_n=1$ kommen als ganze Nullstellen nur die Teiler von $a_0$ in Frage, denn $a_0$ ist bis aufs Vorzeichen das Produkt der Nullstellen.
:::

:::aufgabe Aufgabe 9 ★★ Zerlegen
<span class="anker" id="aufg-9"></span>

(a) Zeige, dass $x_0=1$ eine Nullstelle von $U(x)=x^4-x^3-3x^2+5x-2$ ist, bestimme ihre Vielfachheit und die Form [(8.3)](#gl-8-3). (b) Bringe $x^3-8$ in die Form [(8.4)](#gl-8-4). (c) Vorhersage: Ein Polynom vom Grad 5 enthält zwei quadratische Faktoren ohne reelle Nullstelle. Wie viele reelle Nullstellen hat es?

:::loesung
(a) Schema bei 1: $1,0,-3,2,0$, dann $1,1,-2,0$, dann $1,2,0$, dann $1,3$ mit Rest $3\neq0$. Vielfachheit 3, und $U(x)=(x-1)^3(x+2)$. (b) $x_0=2$ ist Nullstelle, das Schema mit $1,0,0,-8$ ergibt $1,2,4,0$. Also $x^3-8=(x-2)(x^2+2x+4)$ mit $\beta^2-4\gamma=4-16=-12<0$. (c) Die beiden Faktoren haben zusammen Grad 4, es bleibt ein Linearfaktor: genau eine reelle Nullstelle.
:::
:::

::::formelsammlung
**Nullstelle**

$$f(x_0)=0$$

$x_0\in\mathbb{R}$ heißt dann Nullstelle der reellen Funktion $f$.

**$m$-fache Nullstelle**

$$P_n(x)=(x-x_0)^m\,Q_{n-m}(x)\quad\text{und}\quad Q_{n-m}(x_0)\neq0$$

$m$ ist die Vielfachheit, $m\le n$. Ungerades $m$: Der Graph kreuzt die Achse; gerades $m$: Er berührt sie nur.

**Linearfaktor**

$$P_n(x_0)=0\quad\Leftrightarrow\quad P_n(x)=(x-x_0)\,Q_{n-1}(x)\text{ mit einem Polynom }Q_{n-1}$$

Für ein Polynom vom Grad $n\ge1$ und $x_0\in\mathbb{R}$; der Rest der Division durch $x-x_0$ ist $P_n(x_0)$. Deshalb hat $P_n$ höchstens $n$ Nullstellen, mit Vielfachheit gezählt, und zwei Polynome vom Grad $\le n$, die an $n+1$ Stellen übereinstimmen, sind gleich.

**Zerlegung in Linearfaktoren**

$$P_n(x)=a_n(x-x_1)(x-x_2)\cdots(x-x_n)$$

Mit $a_n\neq0$ und den Nullstellen $x_1,\dots,x_n\in\mathbb{R}$, eine mehrfache Nullstelle mehrfach gelistet. Nicht jedes reelle Polynom hat diese Form, etwa $x^2+1$.

**Zerlegung mit quadratischen Faktoren**

$$P_n(x)=a_n(x^2+\beta_1x+\gamma_1)\cdots(x^2+\beta_kx+\gamma_k)\,(x-x_{2k+1})\cdots(x-x_n)$$

Mit $\beta_i^2-4\gamma_i<0$; die $n-2k$ Zahlen $x_i$ sind die Nullstellen. In den komplexen Zahlen ist bei reellen Koeffizienten mit $z$ auch $\overline{z}$ Nullstelle, und $(x-z)(x-\overline{z})=x^2-2\operatorname{Re}(z)\,x+|z|^2$ ist reell.

**Koeffizienten aus den Nullstellen**

$$a_3=-(x_1+x_2+x_3+x_4),\qquad a_0=x_1x_2x_3x_4$$

Für $n=4$ und $a_4=1$ in der Zerlegung in Linearfaktoren; außerdem $a_2=x_1x_2+x_1x_3+x_1x_4+x_2x_3+x_2x_4+x_3x_4$ und $a_1=-(x_1x_2x_3+x_1x_2x_4+x_1x_3x_4+x_2x_3x_4)$.
::::

::::lernkarten
:::karte begriff Nullstelle
Wann heißt eine Zahl $x_0\in\mathbb{R}$ eine Nullstelle einer reellen Funktion $f$?
---
Wenn $f(x_0)=0$ ist. Bei einem Polynom $P$ ist eine Nullstelle also eine Lösung der Gleichung $P(x)=0$, im Rechenmodell etwa $3$, $\frac12$ und $-2$.
--- falsch
Wenn $f(0)=x_0$ ist, also wenn $x_0$ der Wert der Funktion an der Stelle null ist; man liest ihn am Schnittpunkt des Graphen mit der $y$-Achse ab.
--- falsch
Wenn $f(x_0)=0$ ist und der Graph dort die Achse kreuzt; eine Stelle, an der der Graph die Achse nur berührt, ist keine Nullstelle, sondern ein tiefster Punkt.
--- falsch
Wenn $f$ an der Stelle $x_0$ nicht erklärt ist, weil dort durch null geteilt würde; bei einer rationalen Funktion sind das die Stellen, an denen der Nenner verschwindet.
:::
:::karte begriff Linearfaktor
Was ist der Linearfaktor, der zu einer Nullstelle $x_0$ eines Polynoms gehört, und welche Eigenschaften hat er?
---
Der Faktor $x-x_0$ ersten Grades: Er hat Grad 1 und ist genau bei $x_0$ null. Ist $x_0$ eine Nullstelle von $P_n$, steckt er als Faktor in $P_n$, $P_n(x)=(x-x_0)\,Q_{n-1}(x)$.
--- falsch
Der Faktor $x+x_0$ ersten Grades: Er hat Grad 1 und ist genau bei $x_0$ null. Ist $x_0$ eine Nullstelle von $P_n$, steckt er als Faktor in $P_n$, $P_n(x)=(x+x_0)\,Q_{n-1}(x)$.
--- falsch
Der höchste Koeffizient $a_n$, durch den man das Polynom teilen muss, damit die Nullstelle sichtbar wird; er ist bei jeder Nullstelle derselbe und hat keinen Grad.
--- falsch
Ein linearer Teil $ax+b$ des Polynoms, der für große $|x|$ das Verhalten bestimmt; bei $P$ ist er $-11x+6$, und er ist genau bei der Nullstelle $x_0$ gleich eins.
:::
:::karte begriff m-fache Nullstelle und Vielfachheit
Wann heißt $x_0$ eine $m$-fache Nullstelle des Polynoms $P_n$, und was gibt die Vielfachheit $m$ an?
---
Wenn es ein Polynom $Q_{n-m}$ gibt mit $P_n(x)=(x-x_0)^m\,Q_{n-m}(x)$ und $Q_{n-m}(x_0)\neq0$. Die Vielfachheit $m$ zählt, wie oft der Faktor $x-x_0$ in $P_n$ steckt; es ist $m\le n$.
--- falsch
Wenn es ein Polynom $Q_{n-m}$ gibt mit $P_n(x)=(x-x_0)^m\,Q_{n-m}(x)$, ohne weitere Bedingung. Die Vielfachheit ist jede Zahl $m$, für die das gelingt, bei einer doppelten Nullstelle also auch $m=1$.
--- falsch
Wenn $P_n$ genau $m$ verschiedene Nullstellen hat, unter denen $x_0$ ist. Die Vielfachheit $m$ zählt also alle Nullstellen des Polynoms, nicht nur die bei $x_0$; es ist $m\le n$.
--- falsch
Wenn $P_n(x_0)=m$ ist, der Wert an der Stelle $x_0$ also $m$ beträgt. Die Vielfachheit gibt an, wie weit der Graph bei $x_0$ über der Achse liegt; $m=0$ heißt einfache Nullstelle.
:::
:::karte formel Abspalten eines Linearfaktors
Was besagt der Satz über den Linearfaktor für ein Polynom $P_n$ vom Grad $n\ge1$ und eine Zahl $x_0\in\mathbb{R}$, und was folgt für die Zahl der Nullstellen?
---
$P_n(x_0)=0$ $\Leftrightarrow$ $P_n(x)=(x-x_0)\,Q_{n-1}(x)$ mit einem Polynom $Q_{n-1}$. Deshalb hat $P_n$ höchstens $n$ Nullstellen, auch wenn man jede mit ihrer Vielfachheit zählt.
--- falsch
$P_n(x_0)=0$ $\Leftrightarrow$ $P_n(x)=(x-x_0)\,Q_{n-1}(x)$ mit einem Polynom $Q_{n-1}$. Deshalb hat $P_n$ genau $n$ reelle Nullstellen, wenn man jede mit ihrer Vielfachheit zählt.
--- falsch
$P_n(x_0)=0$ $\Leftrightarrow$ $P_n(x)=(x+x_0)\,Q_{n-1}(x)$ mit einem Polynom $Q_{n-1}$. Deshalb hat $P_n$ höchstens $n$ Nullstellen, aber nur, wenn man mehrfache nur einmal zählt.
--- falsch
$P_n(x_0)=0$ $\Rightarrow$ $P_n(x)=(x-x_0)+Q_{n-1}(x)$ mit einem Polynom $Q_{n-1}$; die Umkehrung gilt nicht. Die Zahl der Nullstellen ist dadurch nicht beschränkt.
:::
:::karte herleitung höchstens n Nullstellen
Wie folgt aus dem Satz über das Horner-Schema, dass jede Nullstelle $x_0$ einen Linearfaktor abspaltet und ein Polynom vom Grad $n$ höchstens $n$ Nullstellen hat?
---
Nach dem Satz über das Horner-Schema ist $P_n(x)=(x-x_0)\,Q_{n-1}(x)+c_0$ mit $c_0=P_n(x_0)$; ist $x_0$ Nullstelle, verschwindet der Rest, weil er der Funktionswert ist.
---
Umgekehrt ergibt Einsetzen von $x_0$ in $(x-x_0)\,Q_{n-1}(x)$ null, weil der Faktor $x-x_0$ dort null ist.
---
Jede weitere Nullstelle von $P_n$ ist eine Nullstelle von $Q_{n-1}$, weil ein Produkt genau dann null ist, wenn ein Faktor null ist.
---
Mit jeder abgespaltenen Nullstelle sinkt der Grad um 1; nach höchstens $n$ Schritten bleibt eine Konstante $a_n\neq0$ ohne Nullstelle, weil der Grad nicht negativ werden kann.
:::
:::karte formel Zerlegung in Linearfaktoren
Welche Form entsteht, wenn man von einem Polynom $P_n$ alle $n$ Nullstellen abspaltet, und hat jedes reelle Polynom diese Form?
---
$P_n(x)=a_n(x-x_1)(x-x_2)\cdots(x-x_n)$ mit $a_n\neq0$ und den Nullstellen $x_1,\dots,x_n\in\mathbb{R}$, mehrfache mehrfach gelistet. Nicht jedes reelle Polynom hat diese Form, wie $x^2+1$ zeigt.
--- falsch
$P_n(x)=(x-x_1)(x-x_2)\cdots(x-x_n)$ mit den Nullstellen $x_1,\dots,x_n\in\mathbb{R}$, jede nur einmal gelistet; jedes reelle Polynom hat diese Form, denn jedes hat $n$ reelle Nullstellen.
--- falsch
$P_n(x)=a_n(x+x_1)(x+x_2)\cdots(x+x_n)$ mit den Nullstellen $x_1,\dots,x_n\in\mathbb{R}$, mehrfache mehrfach gelistet; jedes reelle Polynom hat diese Form, wenn man $a_n$ passend wählt.
--- falsch
$P_n(x)=a_n(x-x_1)(x-x_2)\cdots(x-x_n)$ mit $a_n\neq0$ und den Nullstellen $x_1,\dots,x_n\in\mathbb{R}$; jedes reelle Polynom hat diese Form, mehrfache Nullstellen lässt man dabei weg.
:::
:::karte formel Zerlegung mit quadratischen Faktoren
Welche Form hat ein reelles Polynom $P_n$, wenn nach dem Abspalten der reellen Nullstellen ein Rest ohne reelle Nullstelle bleibt?
---
$P_n(x)=a_n(x^2+\beta_1x+\gamma_1)\cdots(x^2+\beta_kx+\gamma_k)\,(x-x_{2k+1})\cdots(x-x_n)$ mit $\beta_i^2-4\gamma_i<0$: Die quadratischen Faktoren haben keine reellen Nullstellen, die $n-2k$ Zahlen $x_i$ sind die Nullstellen.
--- falsch
$P_n(x)=a_n(x^2+\beta_1x+\gamma_1)\cdots(x^2+\beta_kx+\gamma_k)\,(x-x_{2k+1})\cdots(x-x_n)$ mit $\beta_i^2-4\gamma_i>0$: Jeder quadratische Faktor hat zwei reelle Nullstellen, die man nur nicht abgespalten hat.
--- falsch
$P_n(x)=a_n(x^2+\beta_1x+\gamma_1)\cdots(x^2+\beta_kx+\gamma_k)\,(x-x_{2k+1})\cdots(x-x_n)$ mit $\beta_i^2-4\gamma_i<0$: Die quadratischen Faktoren haben keine reellen Nullstellen, die $n-k$ Zahlen $x_i$ sind die Nullstellen.
--- falsch
$P_n(x)=a_n(x^3+\beta_1x+\gamma_1)\cdots(x^3+\beta_kx+\gamma_k)\,(x-x_{3k+1})\cdots(x-x_n)$: Ohne reelle Nullstelle bleiben kubische Faktoren stehen, denn quadratische lassen sich immer weiter zerlegen.
:::
:::karte formel Koeffizienten aus den Nullstellen
Wie hängen für $n=4$ und $a_4=1$ in der Form $P_n(x)=a_n(x-x_1)(x-x_2)\cdots(x-x_n)$ die Koeffizienten $a_3,a_2,a_1,a_0$ mit den Nullstellen zusammen?
---
$a_3=-(x_1+x_2+x_3+x_4)$, $a_2=x_1x_2+x_1x_3+x_1x_4+x_2x_3+x_2x_4+x_3x_4$, $a_1=-(x_1x_2x_3+x_1x_2x_4+x_1x_3x_4+x_2x_3x_4)$, $a_0=x_1x_2x_3x_4$.
--- falsch
$a_3=x_1+x_2+x_3+x_4$, $a_2=x_1x_2+x_1x_3+x_1x_4+x_2x_3+x_2x_4+x_3x_4$, $a_1=x_1x_2x_3+x_1x_2x_4+x_1x_3x_4+x_2x_3x_4$, $a_0=x_1x_2x_3x_4$; alle Vorzeichen sind positiv.
--- falsch
$a_3=-(x_1+x_2+x_3+x_4)$, $a_2=x_1x_2+x_1x_3+x_1x_4+x_2x_3+x_2x_4+x_3x_4$, $a_1=-(x_1x_2x_3+x_1x_2x_4+x_1x_3x_4+x_2x_3x_4)$, $a_0=-x_1x_2x_3x_4$.
--- falsch
$a_3=-(x_1+x_2+x_3+x_4)$, $a_2=x_1^2+x_2^2+x_3^2+x_4^2$, $a_1=-(x_1^3+x_2^3+x_3^3+x_4^3)$, $a_0=x_1^4+x_2^4+x_3^4+x_4^4$; jeder Koeffizient ist eine Summe von Potenzen.
:::
:::karte zusammenhang Rest und Funktionswert
Warum ist der Rest der Division eines Polynoms $P$ durch $x-x_0$ gleich dem Funktionswert $P(x_0)$?
---
Weil $P(x)=(x-x_0)\,Q(x)+c_0$ gilt und beim Einsetzen von $x=x_0$ der erste Summand verschwindet, da sein Faktor $x-x_0$ null ist. Es bleibt $P(x_0)=c_0$.
--- falsch
Weil der Rest immer der Summand ohne $x$ ist, also $a_0$, und $a_0$ ist bei jedem Polynom gleich dem Funktionswert; deshalb ist der Rest $P(x_0)$ für jede Stelle $x_0$.
--- falsch
Weil man beim Teilen durch $x-x_0$ die Stelle $x_0$ in den Quotienten einsetzt: $Q(x_0)$ ist der Rest, und $Q(x_0)=P(x_0)$, weil $Q$ und $P$ dieselben Werte haben.
--- falsch
Weil der Rest der Wert des Quotienten an der Stelle null ist und $P(0)=P(x_0)$ für jede Nullstelle gilt; für andere Stellen $x_0$ stimmt die Aussage nicht.
:::
:::karte zusammenhang kreuzen oder berühren
Woran liegt es, dass der Graph eines Polynoms die Achse an einer Nullstelle ungerader Vielfachheit kreuzt und bei gerader Vielfachheit nur berührt?
---
Nahe $x_0$ ändert $Q_{n-m}(x)$ sein Vorzeichen nicht, weil $Q_{n-m}(x_0)\neq0$ ist. Das Vorzeichen von $P_n$ bestimmt also $(x-x_0)^m$: Für ungerades $m$ wechselt es, für gerades $m$ nicht.
--- falsch
Nahe $x_0$ wechselt $Q_{n-m}(x)$ sein Vorzeichen genau dann, wenn $m$ gerade ist; dieser Wechsel hebt den Wechsel von $(x-x_0)^m$ auf, deshalb berührt der Graph dann nur.
--- falsch
Es liegt am höchsten Koeffizienten $a_n$: Ist er positiv, kreuzt der Graph die Achse, ist er negativ, berührt er sie nur. Die Vielfachheit sagt nur, wie oft das geschieht.
--- falsch
Bei gerader Vielfachheit ist auch $Q_{n-m}(x_0)=0$, und diese zweite Nullstelle bei $x_0$ hebt den Vorzeichenwechsel wieder auf; bei ungerader Vielfachheit fehlt sie.
:::
:::karte zusammenhang n plus eins Stellen
Warum sind zwei Polynome vom Grad höchstens $n$ schon gleich, wenn sie an $n+1$ Stellen übereinstimmen?
---
Weil ihre Differenz sonst ein Polynom vom Grad höchstens $n$ mit $n+1$ Nullstellen wäre, also mit zu vielen Nullstellen. Deshalb ist die Differenz die Funktion $0$.
--- falsch
Weil an $n+1$ Stellen jeder Koeffizient einzeln sichtbar wird: Der Wert an der ersten Stelle ist $a_0$, der an der zweiten $a_1$, und so weiter bis zum Wert $a_n$ an der letzten Stelle.
--- falsch
Das stimmt nicht: Zwei Polynome sind nur gleich, wenn sie an allen Stellen übereinstimmen; $x^2-x$ und $0$ stimmen an zwei Stellen überein und sind trotzdem verschieden.
--- falsch
Weil die Differenz an $n+1$ Stellen null ist und deshalb den Grad $n+1$ hat; ein Polynom vom Grad $n+1$ kann aber nicht die Differenz zweier Polynome vom Grad $n$ sein.
:::
:::karte zusammenhang weitere Nullstellen suchen
Wie findet man nach dem Abspalten einer Nullstelle eines Polynoms $P$ heraus, ob es weitere Nullstellen gibt?
---
Man untersucht den Quotienten, denn jede weitere Nullstelle von $P$ steckt in ihm; bei Grad 2 hilft die Mitternachtsformel. Bei ganzen Koeffizienten und $a_n=1$ kommen als ganze Nullstellen nur Teiler von $a_0$ in Frage.
--- falsch
Man setzt die gefundene Nullstelle erneut in $P$ ein; ist der Wert wieder null, gibt es eine weitere. Bei ganzen Koeffizienten kommen als Nullstellen nur die Teiler von $a_n$ in Frage.
--- falsch
Man zählt die Vorzeichenwechsel der Koeffizienten: Jeder Wechsel zeigt genau eine weitere Nullstelle an, bei $P$ also zwei. Den Quotienten braucht man dafür nicht.
--- falsch
Man untersucht den Quotienten, doch er enthält nur die Nullstellen, die größer sind als die gefundene; die kleineren muss man im ursprünglichen Polynom $P$ suchen, am besten durch Einsetzen ganzer Zahlen.
:::
:::karte zusammenhang Vielfachheit mit dem Horner-Schema
Wie bestimmt man mit dem Horner-Schema die Vielfachheit einer Nullstelle $x_0$, etwa bei $S(x)=x^4-3x^3+x^2+4$ und $x_0=2$?
---
Man wendet das Schema bei $x_0$ wiederholt auf den jeweiligen Quotienten an, bis der Rest nicht mehr null ist; die Zahl der Reste null ist die Vielfachheit. Bei $S$: Reste $0$, $0$, $7$, also Vielfachheit 2.
--- falsch
Man wendet das Schema einmal an und zählt die Nullen in der unteren Zeile; ihre Zahl ist die Vielfachheit. Bei $S$ steht dort eine Null, also ist $x_0=2$ eine einfache Nullstelle.
--- falsch
Man wendet das Schema bei $x_0$ wiederholt auf das ursprüngliche Polynom $S$ an; jeder Durchlauf mit Rest null erhöht die Vielfachheit, und da der Rest immer $S(2)=0$ ist, ist sie unbegrenzt.
--- falsch
Man wendet das Schema bei $x_0$ wiederholt auf den Quotienten an, bis der Rest nicht mehr null ist; die Zahl aller Durchläufe ist die Vielfachheit. Bei $S$: Reste $0$, $0$, $7$, also Vielfachheit 3.
:::
:::karte zusammenhang warum quadratische Faktoren genügen
Warum genügen bei einem reellen Polynom quadratische Faktoren für den Teil ohne reelle Nullstellen?
---
In den komplexen Zahlen hat jedes Polynom vom Grad $n\ge1$ eine Nullstelle, und bei reellen Koeffizienten ist mit $z$ auch $\overline{z}$ eine. $(x-z)(x-\overline{z})=x^2-2\operatorname{Re}(z)\,x+|z|^2$ ist reell.
--- falsch
Weil jedes Polynom vom Grad über 2 eine reelle Nullstelle hat; nur Polynome vom Grad 2 können ohne reelle Nullstelle sein. Deshalb bleibt höchstens ein quadratischer Faktor übrig.
--- falsch
In den komplexen Zahlen hat jedes Polynom eine Nullstelle $z$, und $(x-z)^2=x^2-2zx+z^2$ ist immer reell. Deshalb fasst man jede komplexe Nullstelle mit sich selbst zusammen.
--- falsch
Weil man quadratische Faktoren mit der Mitternachtsformel immer weiter in reelle Linearfaktoren zerlegen kann, wenn man die Diskriminante durch ihren Betrag ersetzt.
:::
::::
