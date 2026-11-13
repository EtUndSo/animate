---
title: Stufe 5: Polynome und Koeffizienten
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
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

::::beispiel
Wann ist $ax^2+bx+c=a(x-x_1)(x-x_2)$ für alle $x$? Ausmultiplizieren ergibt rechts $ax^2-a(x_1+x_2)x+ax_1x_2$, der Koeffizientenvergleich also

<span class="anker" id="gl-5-3"></span>
$$b=-a(x_1+x_2),\qquad c=a\,x_1x_2. \tag{5.3}$$

Diese beiden Gleichungen löst für $a\neq0$ und $D:=b^2-4ac\ge0$ die __Mitternachtsformel__

<span class="anker" id="gl-5-4"></span>
$$x_{1}=\frac{-b+\sqrt D}{2a},\qquad x_{2}=\frac{-b-\sqrt D}{2a}. \tag{5.4}$$

Einsetzen bestätigt es: $-a(x_1+x_2)=-a\cdot\frac{-2b}{2a}=b$ und $ax_1x_2=\frac{1}{4a}\bigl(b^2-D\bigr)=c$. Die Zahl $D$ heißt __Diskriminante__. Für $Q$ ist $D=1+8=9$, also $x_{1}=2$, $x_{2}=-1$, und $x_1+x_2=1=-b/a$, $x_1x_2=-2=c/a$.
::::

⁠**Grenzfälle:** $D=0$ ergibt $x_1=x_2$. Für $D<0$ gibt es keine reelle Nullstelle, denn dann ist $ax^2+bx+c=a\bigl[(x+\frac{b}{2a})^2-\frac{D}{4a^2}\bigr]$, und die Klammer ist positiv. Also hat $x^2+\beta x+\gamma$ genau dann keine reelle Nullstelle, wenn $\beta^2-4\gamma<0$ ist.

:::frage Warum setzt der Beweis nach dem Teilen durch $x$ nicht gleich $x=0$ ein? Da steht doch wieder ein Polynom.
Links und rechts stehen Polynome, das stimmt. Die Gleichung ist aber nur für $x\neq0$ hergeleitet, und daraus folgt nicht sofort etwas über die Stelle 0. Der Umweg über kleine $|x|$ schließt genau diese Lücke. [Kapitel 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html) nennt den dahinter liegenden Begriff Stetigkeit.
:::

:::aufgabe Aufgabe 6 ★★ Koeffizientenvergleich
<span class="anker" id="aufg-6"></span>

(a) Bestimme $a,b,c$ so, dass $2x^2-x+3=a(x-1)^2+b(x-1)+c$ für alle $x$ gilt. (b) $x^3+a_2x^2+a_1x+a_0$ habe die Nullstellen $-1$, $2$, $4$. Bestimme die Koeffizienten durch Ausmultiplizieren und drücke sie durch die Nullstellen aus.

:::loesung
(a) Rechts steht $ax^2+(b-2a)x+(a-b+c)$. Vergleich: $a=2$, $b-4=-1$, also $b=3$, und $2-3+c=3$, also $c=4$. (b) $(x+1)(x-2)(x-4)=x^3-5x^2+2x+8$. Also $a_2=-5=-(x_1+x_2+x_3)$, $a_1=2=x_1x_2+x_1x_3+x_2x_3$, $a_0=8=-x_1x_2x_3$.
:::
:::

::::formelsammlung
**Polynom**

$$f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+a_1x+a_0=\sum_{i=0}^na_ix^i$$

Für $f:\mathbb{R}\to\mathbb{R}$ mit reellen Koeffizienten $a_0,\dots,a_n$ und $a_n\neq0$; man schreibt $P_n:=f$ und $\operatorname{grad}P_n:=n$. Eine Konstante $c\neq0$ hat Grad 0, die Funktion $0$ hat keinen Grad.

**Identitätssatz für Polynome**

$$P_n(x)=Q_n(x)\text{ für alle }x\in\mathbb{R}\quad\Leftrightarrow\quad a_k=b_k\text{ für }k=0,\dots,n$$

Für $P_n(x)=\sum_{k=0}^na_kx^k$ und $Q_n(x)=\sum_{k=0}^nb_kx^k$ vom Grad $\le n$ (also $a_n=0$ oder $b_n=0$ erlaubt); Grundlage des Koeffizientenvergleichs. Polynome verschiedenen Grades sind verschieden.

**Koeffizienten und Nullstellen bei Grad 2**

$$b=-a(x_1+x_2),\qquad c=a\,x_1x_2$$

Koeffizientenvergleich in $ax^2+bx+c=a(x-x_1)(x-x_2)$.

**Mitternachtsformel**

$$x_{1}=\frac{-b+\sqrt D}{2a},\qquad x_{2}=\frac{-b-\sqrt D}{2a}$$

Für $a\neq0$ und die Diskriminante $D:=b^2-4ac\ge0$; bei $D=0$ ist $x_1=x_2$.

**Keine reelle Nullstelle**

$$ax^2+bx+c=a\bigl[(x+\frac{b}{2a})^2-\frac{D}{4a^2}\bigr]$$

Für $D<0$ ist die Klammer positiv. Also hat $x^2+\beta x+\gamma$ genau dann keine reelle Nullstelle, wenn $\beta^2-4\gamma<0$ ist.
::::

::::lernkarten
:::karte begriff Polynom
Wann heißt eine Funktion $f:\mathbb{R}\to\mathbb{R}$ ein Polynom vom Grad $n$, und wie schreibt man es?
---
Wenn es reelle Zahlen $a_0,\dots,a_n$ mit $a_n\neq0$ gibt, so dass $f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+a_1x+a_0=\sum_{i=0}^na_ix^i$ für alle $x$ gilt; man schreibt $P_n:=f$.
--- falsch
Wenn es reelle Zahlen $a_0,\dots,a_n$ gibt, so dass $f(x)=\sum_{i=0}^na_ix^i$ gilt, wobei auch $a_n=0$ erlaubt ist; der Grad ist dann die Zahl $n$ der Summanden ohne $a_0$.
--- falsch
Wenn sich $f$ aus Potenzen von $x$ mit beliebigen reellen Exponenten zusammensetzt, etwa $x^{1/2}+3x^2$; der Grad ist der größte vorkommende Exponent, man schreibt $P_n$.
--- falsch
Wenn es reelle Zahlen $a_0,\dots,a_n$ mit $a_0\neq0$ gibt, so dass $f(x)=\sum_{i=0}^na_ix^i$ gilt; der Grad ist $n$, und der Summand ohne $x$ darf nie fehlen.
:::
:::karte begriff Grad
Was gibt der Grad $\operatorname{grad}P_n$ eines Polynoms an, und welchen Grad haben Konstanten und die Nullfunktion?
---
Die höchste Potenz $n$ mit Koeffizient $a_n\neq0$, $\operatorname{grad}P_n:=n$. Eine Konstante $c\neq0$ hat Grad 0; die Funktion $0$ hat keine solche Darstellung und daher keinen Grad.
--- falsch
Die Zahl der Summanden des Polynoms, also $n+1$. Eine Konstante $c\neq0$ hat Grad 1, die Funktion $0$ hat Grad 0, weil sie keinen einzigen Summanden hat.
--- falsch
Die höchste Potenz $n$, die in der Formel vorkommt, auch wenn ihr Koeffizient null ist. Konstanten und die Funktion $0$ haben beide Grad 0, weil kein $x$ vorkommt.
--- falsch
Die Zahl der Nullstellen des Polynoms, $\operatorname{grad}P_n:=n$. Eine Konstante $c\neq0$ hat deshalb Grad 0, die Funktion $0$ einen unendlichen Grad, weil sie überall null ist.
:::
:::karte begriff Koeffizienten
Welche Zahlen heißen die Koeffizienten eines Polynoms $P_n$, und welcher von ihnen gehört zum Summanden ohne $x$?
---
Die festen Zahlen $a_0,\dots,a_n$ vor den Potenzen. Wegen $x^0=1$ ist $a_0$ der Summand ohne $x$; im Rechenmodell $P$ ist $a_3=2$, $a_2=-3$, $a_1=-11$, $a_0=6$.
--- falsch
Die Exponenten $0,\dots,n$ der Potenzen von $x$. Der Exponent $0$ gehört zum Summanden ohne $x$; im Rechenmodell $P$ sind die Koeffizienten also $3$, $2$, $1$ und $0$.
--- falsch
Die festen Zahlen $a_0,\dots,a_n$ vor den Potenzen. Der Summand ohne $x$ zählt nicht dazu, weil er keine Potenz von $x$ trägt; im Rechenmodell $P$ sind es $2$, $-3$ und $-11$.
--- falsch
Die Nullstellen des Polynoms, aus denen es sich zusammensetzt. Im Rechenmodell $P$ sind es $3$, $\tfrac12$ und $-2$; der Summand ohne $x$ ist dann ihr Produkt.
:::
:::karte formel Identitätssatz für Polynome
Was besagt der Identitätssatz für zwei Polynome $P_n(x)=\sum_{k=0}^na_kx^k$ und $Q_n(x)=\sum_{k=0}^nb_kx^k$ vom Grad höchstens $n$?
---
$P_n(x)=Q_n(x)$ für alle $x\in\mathbb{R}$ $\Leftrightarrow$ $a_k=b_k$ für $k=0,\dots,n$. Die Gleichheit muss für alle $x$ gelten; $a_n=0$ oder $b_n=0$ ist erlaubt.
--- falsch
$P_n(x)=Q_n(x)$ an einer Stelle $x\in\mathbb{R}$ $\Leftrightarrow$ $a_k=b_k$ für $k=0,\dots,n$. Eine einzige gemeinsame Stelle genügt, weil ein Polynom durch einen Wert festgelegt ist.
--- falsch
$P_n(x)=Q_n(x)$ für alle $x\in\mathbb{R}$ $\Leftrightarrow$ $a_0=b_0$. Es genügt, die Summanden ohne $x$ zu vergleichen, weil die übrigen bei $x=0$ verschwinden.
--- falsch
$P_n(x)=Q_n(x)$ für alle $x\in\mathbb{R}$ $\Leftrightarrow$ $a_k=b_k$ für $k=0,\dots,n$, aber nur, wenn beide Polynome genau den Grad $n$ haben, also $a_n\neq0$ und $b_n\neq0$.
:::
:::karte begriff Koeffizientenvergleich
Was versteht man unter einem Koeffizientenvergleich, und worauf beruht er?
---
Um zwei Polynome als Funktionen zu vergleichen, vergleicht man ihre Koeffizienten Potenz für Potenz. Er beruht auf dem Identitätssatz: Gleich für alle $x$ heißt gleiche Koeffizienten.
--- falsch
Man vergleicht zwei Polynome an einigen gewählten Stellen; stimmen die Werte dort überein, sind die Koeffizienten gleich. Er beruht darauf, dass Polynome durch wenige Werte festliegen.
--- falsch
Man vergleicht die höchsten Koeffizienten $a_n$ und $b_n$ zweier Polynome; sind sie gleich, sind die Polynome gleich. Er beruht darauf, dass die höchste Potenz das Verhalten bestimmt.
--- falsch
Man vergleicht die Koeffizienten eines Polynoms untereinander, um die größte Potenz zu finden. Er beruht darauf, dass der größte Koeffizient den Grad des Polynoms festlegt.
:::
:::karte herleitung Identitätssatz
Wie folgt aus $P_n(x)=Q_n(x)$ für alle $x\in\mathbb{R}$, dass alle Koeffizienten der beiden Polynome übereinstimmen?
---
Bei $x=0$ steht $a_0=b_0$, weil dort alle Potenzen von $x$ verschwinden.
---
Abziehen von $a_0$ und Teilen durch $x\neq0$ ergibt $a_1+a_2x+\dots+a_nx^{n-1}=b_1+b_2x+\dots+b_nx^{n-1}$ für alle $x\neq0$; $x=0$ darf man hier nicht einsetzen, weil durch $x$ geteilt wurde.
---
Für $0<|x|\le1$ folgt $|a_1-b_1|\le C\,|x|$ mit $C:=\sum_{k=2}^n\bigl(|a_k|+|b_k|\bigr)$, weil alle Potenzen von $|x|$ höchstens 1 sind und die Dreiecksungleichung gilt.
---
Da $|x|$ beliebig klein sein darf, ist $|a_1-b_1|<\varepsilon$ für jedes $\varepsilon>0$, also $a_1=b_1$, weil eine Zahl $a$ mit $|a|<\varepsilon$ für alle $\varepsilon>0$ null ist: $|a|>0$ ergäbe mit $\varepsilon=|a|/2$ den Widerspruch $|a|<|a|/2$.
---
Abziehen von $a_0+a_1x$ und Teilen durch $x^2$ ergibt ebenso $a_2=b_2$, und so weiter bis $a_n=b_n$, weil sich derselbe Schluss wiederholt.
:::
:::karte formel Mitternachtsformel
Wie lauten die Lösungen $x_1,x_2$ der Mitternachtsformel für $ax^2+bx+c$, und unter welchen Bedingungen gilt sie?
---
$x_{1}=\frac{-b+\sqrt D}{2a}$ und $x_{2}=\frac{-b-\sqrt D}{2a}$ mit der Diskriminante $D:=b^2-4ac$, für $a\neq0$ und $D\ge0$. Dann ist $ax^2+bx+c=a(x-x_1)(x-x_2)$ für alle $x$.
--- falsch
$x_{1}=\frac{-b+\sqrt D}{2a}$ und $x_{2}=\frac{-b-\sqrt D}{2a}$ mit $D:=b^2+4ac$, für $a\neq0$ und jedes $D$. Für $D<0$ nimmt man einfach den Betrag $|D|$ unter der Wurzel.
--- falsch
$x_{1}=\frac{-b+\sqrt D}{a}$ und $x_{2}=\frac{-b-\sqrt D}{a}$ mit der Diskriminante $D:=b^2-4ac$, für $a\neq0$ und $D\ge0$; der Faktor 2 entfällt, weil $a$ schon vor $x^2$ steht.
--- falsch
$x_{1}=\frac{b+\sqrt D}{2a}$ und $x_{2}=\frac{b-\sqrt D}{2a}$ mit der Diskriminante $D:=b^2-4ac$, für $a\neq0$ und $D\ge0$. Dann ist $ax^2+bx+c=a(x+x_1)(x+x_2)$ für alle $x$.
:::
:::karte formel Nullstellen und Koeffizienten
Wie hängen bei $ax^2+bx+c=a(x-x_1)(x-x_2)$ die Koeffizienten $b$ und $c$ mit $x_1$ und $x_2$ zusammen, und woher kommt das?
---
$b=-a(x_1+x_2)$ und $c=a\,x_1x_2$, also $x_1+x_2=-b/a$ und $x_1x_2=c/a$. Das liefert der Koeffizientenvergleich nach dem Ausmultiplizieren der rechten Seite.
--- falsch
$b=a(x_1+x_2)$ und $c=a\,x_1x_2$, also $x_1+x_2=b/a$ und $x_1x_2=c/a$. Das liefert der Koeffizientenvergleich nach dem Ausmultiplizieren der rechten Seite.
--- falsch
$b=-a\,x_1x_2$ und $c=a(x_1+x_2)$, also ist $b$ das Produkt und $c$ die Summe der Nullstellen, bis auf den Faktor $a$; das liefert Einsetzen von $x=1$.
--- falsch
$b=-(x_1+x_2)$ und $c=x_1x_2$, unabhängig von $a$, weil sich $a$ beim Ausmultiplizieren herauskürzt; das liefert der Koeffizientenvergleich beider Seiten.
:::
:::karte zusammenhang Diskriminante
Was sagt die Diskriminante $D:=b^2-4ac$ darüber, ob $ax^2+bx+c$ mit $a\neq0$ reelle Nullstellen hat, und warum?
---
Für $D\ge0$ liefert die Mitternachtsformel $x_1$ und $x_2$, bei $D=0$ fallen sie zusammen. Für $D<0$ gibt es keine, weil $ax^2+bx+c=a\bigl[(x+\frac{b}{2a})^2-\frac{D}{4a^2}\bigr]$ ist und die Klammer dann positiv ist.
--- falsch
Für $D>0$ gibt es zwei Nullstellen, für $D<0$ ebenfalls zwei, nur mit vertauschtem Vorzeichen, weil die Wurzel aus $D$ dann $\sqrt{-D}$ ist. Nur $D=0$ ergibt keine reelle Nullstelle.
--- falsch
Für $D\ge0$ liefert die Mitternachtsformel $x_1$ und $x_2$, bei $D=0$ gibt es keine, weil der Nenner $2a$ dann null wird. Für $D<0$ gibt es genau eine, nämlich $-\frac{b}{2a}$.
--- falsch
Die Diskriminante entscheidet nur über das Vorzeichen der Nullstellen: Für $D>0$ sind beide positiv, für $D<0$ beide negativ, für $D=0$ ist eine davon null.
:::
:::karte zusammenhang Gleichheit für alle x
Warum genügt es für einen Koeffizientenvergleich nicht, dass zwei Polynome an einigen Stellen übereinstimmen?
---
Weil der Identitätssatz Gleichheit für alle $x$ verlangt: $x^2-x$ und $0$ stimmen bei $x=0$ und $x=1$ überein, ihre Koeffizienten aber nicht. Erst die Gleichheit überall legt jeden Koeffizienten fest.
--- falsch
Es genügt doch: Stimmen zwei Polynome an zwei Stellen überein, haben sie gleiche Koeffizienten. $x^2-x$ und $0$ stimmen bei $x=0$ und $x=1$ überein und sind deshalb dasselbe Polynom.
--- falsch
Weil Polynome an einzelnen Stellen gar nicht erklärt sein müssen; erst als Funktion auf ganz $\mathbb{R}$ hat ein Polynom Koeffizienten, an einzelnen Stellen nur Werte ohne Koeffizienten.
--- falsch
Weil die Stellen nahe null liegen müssen, denn nur dort sieht man die Koeffizienten. Stimmen zwei Polynome an zwei Stellen nahe null überein, sind ihre Koeffizienten gleich.
:::
:::karte zusammenhang verschiedener Grad
Warum sind zwei Polynome verschiedenen Grades nie dieselbe Funktion?
---
Wegen des Identitätssatzes: Gleiche Funktionen haben gleiche Koeffizienten. Beim Polynom höheren Grades $n$ ist $a_n\neq0$, beim anderen ist der Koeffizient von $x^n$ null.
--- falsch
Weil Polynome verschiedenen Grades verschiedene Definitionsbereiche haben: Ein Polynom vom Grad $n$ ist nur auf $\mathbb{R}_0^+$ erklärt, wenn $n$ gerade ist, sonst auf ganz $\mathbb{R}$.
--- falsch
Sie können durchaus dieselbe Funktion sein, wenn ihre Werte an genügend vielen Stellen übereinstimmen; der Grad hängt nur von der Schreibweise ab, nicht von der Funktion.
--- falsch
Weil ihre Graphen verschieden steil sind: Ein Polynom höheren Grades wächst überall schneller als eines kleineren Grades, also unterscheiden sich ihre Werte an jeder Stelle $x$.
:::
:::karte zusammenhang Umweg über kleine x
Warum setzt der Beweis des Identitätssatzes nach dem Teilen durch $x$ nicht einfach $x=0$ ein, obwohl dort wieder Polynome stehen?
---
Weil die Gleichung nach dem Teilen nur für $x\neq0$ hergeleitet ist; daraus folgt nicht sofort etwas über die Stelle 0. Der Umweg über kleine $|x|$ schließt genau diese Lücke.
--- falsch
Weil man $x=0$ zwar einsetzen dürfte, dabei aber alle Koeffizienten außer $a_0$ verloren gingen; der Umweg über kleine $|x|$ ist nur ein Rechentrick, der Schreibarbeit spart.
--- falsch
Weil Polynome bei $x=0$ nicht erklärt sind, wenn ihr Grad größer als null ist; erst für kleine $|x|$ mit $x\neq0$ sind die Potenzen von $x$ überhaupt definiert.
--- falsch
Weil beim Einsetzen von $x=0$ der Ausdruck $0/0$ entstünde; der Umweg über kleine $|x|$ ersetzt $0/0$ durch den Wert $1$, den man für kleine $|x|$ beobachtet.
:::
:::karte zusammenhang Koeffizienten nahe null
Warum sieht man die Koeffizienten eines Polynoms nahe $x=0$ der Reihe nach, zuerst $a_0$ und dann $a_1$?
---
Weil der Wert bei null $a_0$ ist und die höheren Potenzen für kleine $|x|$ winzig sind; nahe null verhält sich $P$ wie die Gerade $a_0+a_1x$. Bei $P$ weicht $6-11x$ bei $x=0{,}1$ nur um 0,028 ab.
--- falsch
Weil ein Polynom nahe null mit seinem höchsten Koeffizienten beginnt: Zuerst sieht man $a_n$, dann $a_{n-1}$; die kleinen Potenzen fallen nahe null kaum ins Gewicht.
--- falsch
Weil nahe null alle Potenzen gleich groß sind, nämlich etwa 1; deshalb trägt jeder Koeffizient gleich viel bei, und man liest sie in der Reihenfolge ab, in der sie geschrieben sind.
--- falsch
Weil der Wert bei null $a_1$ ist und die Steigung dort $a_0$; die höheren Potenzen sind für kleine $|x|$ winzig, und $P$ verhält sich nahe null wie die Gerade $a_1+a_0x$.
:::
::::
