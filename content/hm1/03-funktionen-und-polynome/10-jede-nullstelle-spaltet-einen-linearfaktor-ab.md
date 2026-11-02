---
title: Stufe 8: Jede Nullstelle spaltet einen Linearfaktor ab
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Funktionen und Polynome
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
In den komplexen Zahlen ([Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)) hat jedes Polynom vom Grad $n\ge1$ eine Nullstelle (Fundamentalsatz der Algebra). Bei reellen Koeffizienten ist mit $z$ auch $\overline{z}$ eine Nullstelle, und $(x-z)(x-\overline{z})=x^2-2\operatorname{Re}(z)\,x+|z|^2$ ist reell. Für $x^2+x+1$ ist $z=-\frac12+\frac{\sqrt3}{2}\,\mathrm{i}$.
:::

**Beispiel.** Bei $S$ ergibt das Schema bei $x_0=2$ die Zeile $1,-1,-1,-2,0$, also $S(x)=(x-2)(x^3-x^2-x-2)$. Nochmals bei $x_0=2$: $1,1,1,0$, also $S(x)=(x-2)^2(x^2+x+1)$. Beim dritten Mal: $1,3,7$, der Rest $7\neq0$ beendet die Suche. Die Vielfachheit ist 2, und wegen $1-4=-3<0$ ist [(8.4)](#gl-8-4) erreicht, mit $n=4$, $k=1$. **Grenzfall:** Für $m=n$ ist $P_n(x)=a_n(x-x_0)^n$, das Polynom mit nur einer Nullstelle.

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
