---
title: Stufe 5: Polynome und Koeffizienten
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Funktionen und Polynome
order: 1230700
summary: Die allgemeine Theorie steht.
tags: Grad, Koeffizienten, Koeffizientenvergleichs, Mitternachtsformel, Diskriminante
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Die allgemeine Theorie steht. Jetzt folgt die wichtigste Familie von Funktionen: Polynome, gebaut nur aus Addition und Multiplikation. Das erste Problem lautet: Dasselbe Polynom kann ganz verschieden aussehen. Wann sind zwei Polynome gleich?
:::

**Die Idee.** Ein Polynom ist durch endlich viele Zahlen festgelegt. Nahe $x=0$ sieht man sie der Reihe nach: Der Wert bei null ist die letzte Zahl, die Steigung dort die nächste, denn die höheren Potenzen sind für kleine $|x|$ winzig (Abb. [6](#abb-6)). Zwei Polynome, die überall gleich sind, müssen deshalb Zahl für Zahl übereinstimmen.

:::definition Definition 5.1 (Polynom)
<span class="anker" id="satz-5-1"></span>

Eine Funktion $f:\mathbb{R}\to\mathbb{R}$ heißt Polynom vom __Grad__ $n\in\mathbb{N}_0$, wenn es reelle Zahlen $a_0,\dots,a_n$ mit $a_n\neq0$ gibt, so dass

<span class="anker" id="gl-5-1"></span>
$$f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+a_1x+a_0=\sum_{i=0}^na_ix^i. \tag{5.1}$$

Man schreibt $P_n:=f$ und $\operatorname{grad}P_n:=n$. Die Zahlen $a_0,\dots,a_n$ heißen __Koeffizienten__ von $P_n$.
:::

⁠**So liest man das:** Der Index an $P_n$ nennt den Grad. Für alle $x$ gilt $x^0=1$, also ist $a_0$ der Summand ohne $x$. Im Rechenmodell ist $a_3=2$, $a_2=-3$, $a_1=-11$, $a_0=6$, bei $S$ ist $a_1=0$. Es gilt immer $\mathcal D(f)=\mathbb{R}$, aber $\mathcal W(f)$ kann kleiner sein ($x^2$). Eine Konstante $c\neq0$ hat Grad 0. Die Funktion $0$ hat keine solche Darstellung und daher in dieser Definition keinen Grad.

:::satz Satz 5.2 (Identitätssatz für Polynome)
<span class="anker" id="satz-5-2"></span>

Seien $P_n(x)=\sum_{k=0}^na_kx^k$ und $Q_n(x)=\sum_{k=0}^nb_kx^k$ Polynome vom Grad $\le n$ (also $a_n=0$ oder $b_n=0$ erlaubt). Dann gilt

<span class="anker" id="gl-5-2"></span>
$$P_n(x)=Q_n(x)\text{ für alle }x\in\mathbb{R}\quad\Leftrightarrow\quad a_k=b_k\text{ für }k=0,\dots,n. \tag{5.2}$$
:::

:::beweis Identitätssatz
„$\Leftarrow$“: Gleiche Koeffizienten ergeben gleiche Werte.

„$\Rightarrow$“: Bei $x=0$ steht $a_0=b_0$. Abziehen und Teilen durch $x\neq0$ ergibt für alle $x\neq0$

$$a_1+a_2x+\dots+a_nx^{n-1}=b_1+b_2x+\dots+b_nx^{n-1}.$$

Hier darf man $x=0$ nicht einsetzen, denn durch $x$ wurde geteilt. Stattdessen benutzt man kleine $x$: Aus der Gleichung folgt $a_1-b_1=x\bigl[(b_2-a_2)+(b_3-a_3)x+\dots+(b_n-a_n)x^{n-2}\bigr]$. Für $0<|x|\le1$ sind alle Potenzen von $|x|$ höchstens 1, also liefert die Dreiecksungleichung $|u+v|\le|u|+|v|$

$$|a_1-b_1|\le C\,|x|\quad\text{mit}\quad C:=\sum_{k=2}^n\bigl(|a_k|+|b_k|\bigr).$$

$C$ hängt nur von den Koeffizienten ab, $|x|$ darf beliebig klein sein. Also ist $|a_1-b_1|<\varepsilon$ für jedes $\varepsilon>0$. Eine Zahl $a$ mit $|a|<\varepsilon$ für alle $\varepsilon>0$ ist null, denn $|a|>0$ ergäbe mit $\varepsilon=|a|/2$ den Widerspruch $|a|<|a|/2$. Also $a_1=b_1$. Abziehen von $a_0+a_1x$ und Teilen durch $x^2$ ergibt ebenso $a_2=b_2$, und so weiter bis $a_n=b_n$.
:::

⁠**So liest man das:** Der Satz ist die Grundlage des __Koeffizientenvergleichs__: Um zwei Polynome als Funktionen zu vergleichen, vergleicht man ihre Koeffizienten. Polynome verschiedenen Grades sind daher immer verschieden. **Warum „für alle $x$“ nötig ist:** $x^2-x$ und $0$ stimmen bei $x=0$ und $x=1$ überein, die Koeffizienten aber nicht.

:::abbildung hm1/k3nahnull 6
Links $P$ im Großen. Rechts der Ausschnitt um $x=0$ mit der Geraden $a_0+a_1x=6-11x$: Bei $x=0{,}1$ weicht sie nur um 0,028 ab, die höheren Potenzen fallen nahe null kaum ins Gewicht.
:::

**Beispiel.** Wann ist $ax^2+bx+c=a(x-x_1)(x-x_2)$ für alle $x$? Ausmultiplizieren ergibt rechts $ax^2-a(x_1+x_2)x+ax_1x_2$, der Koeffizientenvergleich also

<span class="anker" id="gl-5-3"></span>
$$b=-a(x_1+x_2),\qquad c=a\,x_1x_2. \tag{5.3}$$

Diese beiden Gleichungen löst für $a\neq0$ und $D:=b^2-4ac\ge0$ die __Mitternachtsformel__

<span class="anker" id="gl-5-4"></span>
$$x_{1}=\frac{-b+\sqrt D}{2a},\qquad x_{2}=\frac{-b-\sqrt D}{2a}. \tag{5.4}$$

Einsetzen bestätigt es: $-a(x_1+x_2)=-a\cdot\frac{-2b}{2a}=b$ und $ax_1x_2=\frac{1}{4a}\bigl(b^2-D\bigr)=c$. Die Zahl $D$ heißt __Diskriminante__. Für $Q$ ist $D=1+8=9$, also $x_{1}=2$, $x_{2}=-1$, und $x_1+x_2=1=-b/a$, $x_1x_2=-2=c/a$. **Grenzfälle:** $D=0$ ergibt $x_1=x_2$. Für $D<0$ gibt es keine reelle Nullstelle, denn dann ist $ax^2+bx+c=a\bigl[(x+\frac{b}{2a})^2-\frac{D}{4a^2}\bigr]$, und die Klammer ist positiv. Also hat $x^2+\beta x+\gamma$ genau dann keine reelle Nullstelle, wenn $\beta^2-4\gamma<0$ ist.

:::frage Warum setzt der Beweis nach dem Teilen durch $x$ nicht gleich $x=0$ ein? Da steht doch wieder ein Polynom.
Links und rechts stehen Polynome, das stimmt. Die Gleichung ist aber nur für $x\neq0$ hergeleitet, und daraus folgt nicht sofort etwas über die Stelle 0. Der Umweg über kleine $|x|$ schließt genau diese Lücke. [Teil 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html) nennt den dahinter liegenden Begriff Stetigkeit.
:::

:::aufgabe Aufgabe 6 ★★ Koeffizientenvergleich
<span class="anker" id="aufg-6"></span>

(a) Bestimme $a,b,c$ so, dass $2x^2-x+3=a(x-1)^2+b(x-1)+c$ für alle $x$ gilt. (b) $x^3+a_2x^2+a_1x+a_0$ habe die Nullstellen $-1$, $2$, $4$. Bestimme die Koeffizienten durch Ausmultiplizieren und drücke sie durch die Nullstellen aus.

:::loesung
(a) Rechts steht $ax^2+(b-2a)x+(a-b+c)$. Vergleich: $a=2$, $b-4=-1$, also $b=3$, und $2-3+c=3$, also $c=4$. (b) $(x+1)(x-2)(x-4)=x^3-5x^2+2x+8$. Also $a_2=-5=-(x_1+x_2+x_3)$, $a_1=2=x_1x_2+x_1x_3+x_2x_3$, $a_0=8=-x_1x_2x_3$.
:::
:::
