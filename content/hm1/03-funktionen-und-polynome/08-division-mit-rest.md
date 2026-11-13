---
title: Stufe 6: Division mit Rest
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
order: 1230800
summary: Summe, Differenz und Produkt von Polynomen sind wieder Polynome, der Quotient meist nicht.
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Summe, Differenz und Produkt von Polynomen sind wieder Polynome, der Quotient meist nicht. Die Division mit Rest zerlegt ihn in ein Polynom und einen möglichst kleinen Rest, wie $17:5=3$ Rest $2$.
:::

**Die Idee.** Bei Zahlen zieht man so oft Vielfache des Teilers ab, bis der Rest kleiner ist als der Teiler. Bei Polynomen misst der Grad die Größe. Man zieht ein Vielfaches des Nenners ab, das genau die höchste Potenz des Zählers auslöscht, und wiederholt das, bis der Grad des Rests kleiner ist als der des Nenners (Abb. [7](#abb-7)).

:::definition Definition 6.1 (Rationale Funktion)
<span class="anker" id="satz-6-1"></span>

Für Polynome $P_n$ und $Q_m$ vom Grad $n$ und $m$ heißt

<span class="anker" id="gl-6-1"></span>
$$R(x):=\frac{P_n(x)}{Q_m(x)},\qquad\mathcal D(R):=\{x\in\mathbb{R}:Q_m(x)\neq0\} \tag{6.1}$$

rationale Funktion.
:::

⁠**So liest man das:** Die Nullstellen des Nenners gehören nicht zu $\mathcal D(R)$. Im Rechenmodell fehlen $x=2$ und $x=-1$.

:::satz Satz 6.2 (Division mit Rest)
<span class="anker" id="satz-6-2"></span>

Sei $R(x)=P_n(x)/Q_m(x)$ mit $n\ge m\ge1$. Dann gibt es Polynome $S_{n-m}$ und $T_k$ mit $\operatorname{grad}S_{n-m}=n-m$, so dass für alle $x\in\mathcal D(R)$

<span class="anker" id="gl-6-2"></span>
$$R(x)=S_{n-m}(x)+\frac{T_k(x)}{Q_m(x)}, \tag{6.2}$$

wobei $\operatorname{grad}T_k=k<m$ oder $T_k=0$ ist. Nach Multiplikation mit $Q_m$ heißt das für alle $x\in\mathbb{R}$

<span class="anker" id="gl-6-3"></span>
$$P_n(x)=S_{n-m}(x)\,Q_m(x)+T_k(x). \tag{6.3}$$
:::

:::beweis Division mit Rest
Seien $a_n$, $b_m\neq0$ die höchsten Koeffizienten von $P_n$, $Q_m$. Setze

$$\widetilde P(x):=P_n(x)-\frac{a_n}{b_m}x^{n-m}\,Q_m(x).$$

Der abgezogene Term beginnt mit $\frac{a_n}{b_m}x^{n-m}\cdot b_mx^m=a_nx^n$, also hebt sich $x^n$ weg, und es ist $\widetilde P=0$ oder $\operatorname{grad}\widetilde P\le n-1$. Teilen durch $Q_m$ ergibt

$$\frac{P_n(x)}{Q_m(x)}=\frac{a_n}{b_m}x^{n-m}+\frac{\widetilde P(x)}{Q_m(x)}.$$

Ist $\widetilde P=0$ oder $\operatorname{grad}\widetilde P<m$, ist man fertig mit $T_k=\widetilde P$. Sonst macht man denselben Schritt mit $\widetilde P$ statt $P_n$. Der Grad sinkt jedes Mal um mindestens 1, nach höchstens $n-m+1$ Schritten endet das Verfahren. Die Summe aller Vorfaktoren ist $S_{n-m}$, der erste bestimmt seinen Grad $n-m$.
:::

⁠**So liest man das:** $S_{n-m}$ ist der Polynomteil, $T_k$ der Rest. $b_m\neq0$ ist nötig, denn man teilt durch $b_m$. Für $n<m$ gibt es nichts zu teilen, dann ist $S=0$ und $T=P_n$. Das Beispiel $x^2:x$ zeigt den glatten Fall $T=0$.

::::beispiel
Für $P:Q$ löscht $2x\cdot Q$ den Term $2x^3$ aus, danach $-1\cdot Q$ den Term $-x^2$:

$$\begin{array}{lrrrr} & 2x^3 & -3x^2 & -11x & +6\\ -2x\cdot Q: & -2x^3 & +2x^2 & +4x & \\ \hline & & -x^2 & -7x & +6\\ +1\cdot Q: & & +x^2 & -x & -2\\ \hline & & & -8x & +4 \end{array}$$

Also ist $R(x)=2x-1+\dfrac{-8x+4}{x^2-x-2}$, mit $n-m=1$ und $k=1<2$. **Probe** nach [(6.3)](#gl-6-3) bei $x=3$: $5\cdot4+(-20)=0=P(3)$.
::::

:::abbildung hm1/k3division 7
Die Division $P:Q$ als Koeffizienten je Potenz. In jedem Schritt verschwindet die höchste Potenz, der Grad sinkt von 3 auf 2 und auf 1. Dann ist er kleiner als der Grad 2 von $Q$, und das Verfahren endet.
:::

:::frage Warum darf der Rest den Grad 1 haben, wenn $Q$ den Grad 2 hat? Bei Zahlen ist der Rest doch eine Zahl.
Der Rest ist ein Polynom, seine Größe misst der Grad. „Kleiner als der Teiler“ heißt hier: kleinerer Grad, also $k<m$. Nur beim Teiler $x-x_0$ mit $m=1$ ist der Rest eine Konstante. Genau das nutzt Stufe [8](jede-nullstelle-spaltet-einen-linearfaktor-ab.html#stufe-8).
:::

:::aufgabe Aufgabe 7 ★★ Division mit Rest
<span class="anker" id="aufg-7"></span>

(a) Berechne $(x^4-3x^2+2x+5):(x^2+x-1)$ mit Rest. Achte auf die fehlende Potenz $x^3$. (b) Mache die Probe bei $x=2$. (c) Grenzfall: Was ergibt $(x+1):(x^2+1)$?

:::loesung
(a) Mit $x^4+0x^3-3x^2+2x+5$: $x^2\cdot(x^2+x-1)$ abziehen lässt $-x^3-2x^2+2x+5$, $-x\cdot(x^2+x-1)$ abziehen lässt $-x^2+x+5$, $-1\cdot(x^2+x-1)$ abziehen lässt $2x+4$. Ergebnis: $S(x)=x^2-x-1$, Rest $2x+4$. (b) Links $16-12+4+5=13$. Rechts $1\cdot5+8=13$. (c) Hier ist $n=1<m=2$, es gibt nichts zu teilen: Polynomteil 0, Rest $x+1$.
:::
:::

::::formelsammlung
**Rationale Funktion**

$$R(x):=\frac{P_n(x)}{Q_m(x)},\qquad\mathcal D(R):=\{x\in\mathbb{R}:Q_m(x)\neq0\}$$

Für Polynome $P_n$ und $Q_m$ vom Grad $n$ und $m$; die Nullstellen des Nenners gehören nicht zu $\mathcal D(R)$.

**Division mit Rest**

$$R(x)=S_{n-m}(x)+\frac{T_k(x)}{Q_m(x)},\qquad P_n(x)=S_{n-m}(x)\,Q_m(x)+T_k(x)$$

Für $n\ge m\ge1$, mit $\operatorname{grad}S_{n-m}=n-m$ und $\operatorname{grad}T_k=k<m$ oder $T_k=0$; die erste Form für $x\in\mathcal D(R)$, die zweite für alle $x\in\mathbb{R}$. Für $n<m$ ist $S=0$ und $T=P_n$.

**Ein Schritt der Division**

$$\widetilde P(x):=P_n(x)-\frac{a_n}{b_m}x^{n-m}\,Q_m(x)$$

$a_n$ und $b_m\neq0$ sind die höchsten Koeffizienten von $P_n$ und $Q_m$; der abgezogene Term beginnt mit $a_nx^n$, der Grad sinkt um mindestens 1. Man wiederholt den Schritt, bis der Grad kleiner als $m$ ist.
::::

::::lernkarten
:::karte begriff rationale Funktion
Was ist eine rationale Funktion, und welche Stellen gehören nicht zu ihrem Definitionsbereich?
---
Ein Quotient zweier Polynome, $R(x):=\frac{P_n(x)}{Q_m(x)}$ mit $\mathcal D(R):=\{x\in\mathbb{R}:Q_m(x)\neq0\}$. Die Nullstellen des Nenners gehören nicht zu $\mathcal D(R)$, im Rechenmodell $x=2$ und $x=-1$.
--- falsch
Ein Quotient zweier Polynome, $R(x):=\frac{P_n(x)}{Q_m(x)}$ mit $\mathcal D(R):=\{x\in\mathbb{R}:P_n(x)\neq0\}$. Die Nullstellen des Zählers gehören nicht dazu, im Rechenmodell $3$, $\frac12$ und $-2$.
--- falsch
Ein Polynom mit rationalen Koeffizienten, etwa $\frac12x^2-\frac34$. Ihr Definitionsbereich ist ganz $\mathbb{R}$, weil man in jedes Polynom jede reelle Zahl einsetzen kann.
--- falsch
Ein Quotient zweier Polynome, $R(x):=\frac{P_n(x)}{Q_m(x)}$, erklärt auf ganz $\mathbb{R}$; an den Nullstellen des Nenners setzt man $R$ gleich null, damit keine Stelle fehlt.
:::
:::karte formel Division mit Rest
Was liefert die Division mit Rest für $R(x)=P_n(x)/Q_m(x)$ mit $n\ge m\ge1$, und welche Bedingung erfüllt der Rest?
---
Polynome $S_{n-m}$ und $T_k$ mit $\operatorname{grad}S_{n-m}=n-m$ und $R(x)=S_{n-m}(x)+\frac{T_k(x)}{Q_m(x)}$, also $P_n(x)=S_{n-m}(x)\,Q_m(x)+T_k(x)$ für alle $x$; dabei ist $\operatorname{grad}T_k=k<m$ oder $T_k=0$.
--- falsch
Polynome $S_{n-m}$ und $T_k$ mit $R(x)=S_{n-m}(x)+T_k(x)$, also $P_n(x)=S_{n-m}(x)\,Q_m(x)+T_k(x)\,Q_m(x)$; der Rest $T_k$ ist stets eine Konstante, weil man teilt, bis kein $x$ mehr übrig ist.
--- falsch
Polynome $S_{n-m}$ und $T_k$ mit $\operatorname{grad}S_{n-m}=n+m$ und $P_n(x)=S_{n-m}(x)\,Q_m(x)+T_k(x)$ für alle $x$; dabei ist $\operatorname{grad}T_k\le n$, weil der Rest aus dem Zähler stammt.
--- falsch
Polynome $S_{n-m}$ und $T_k$ mit $\operatorname{grad}S_{n-m}=n-m$ und $P_n(x)=S_{n-m}(x)\,Q_m(x)+T_k(x)$ für alle $x$; dabei ist $\operatorname{grad}T_k=k<n-m$, der Rest ist also kleiner als der Polynomteil.
:::
:::karte herleitung Division mit Rest
Wie gewinnt man bei der Division mit Rest Schritt für Schritt Polynomteil und Rest, und warum endet das Verfahren?
---
Mit den höchsten Koeffizienten $a_n$ und $b_m\neq0$ setzt man $\widetilde P(x):=P_n(x)-\frac{a_n}{b_m}x^{n-m}\,Q_m(x)$, weil der abgezogene Term mit $\frac{a_n}{b_m}x^{n-m}\cdot b_mx^m=a_nx^n$ beginnt und $x^n$ auslöscht.
---
Also ist $\widetilde P=0$ oder $\operatorname{grad}\widetilde P\le n-1$, und Teilen durch $Q_m$ ergibt $\frac{P_n(x)}{Q_m(x)}=\frac{a_n}{b_m}x^{n-m}+\frac{\widetilde P(x)}{Q_m(x)}$, weil man nur umgestellt hat.
---
Ist $\widetilde P=0$ oder $\operatorname{grad}\widetilde P<m$, ist man fertig mit $T_k=\widetilde P$; sonst wiederholt man den Schritt mit $\widetilde P$ statt $P_n$, weil dessen Grad noch zu groß ist.
---
Das Verfahren endet nach höchstens $n-m+1$ Schritten, weil der Grad jedes Mal um mindestens 1 sinkt.
---
Die Summe aller Vorfaktoren ist $S_{n-m}$, und ihr erster bestimmt den Grad $n-m$, weil die späteren Vorfaktoren kleinere Potenzen haben.
:::
:::karte zusammenhang Grad des Rests
Warum darf der Rest bei der Division durch ein Polynom $Q$ vom Grad 2 den Grad 1 haben, wo bei Zahlen der Rest doch eine Zahl ist?
---
Weil die Größe eines Polynoms an seinem Grad gemessen wird: „Kleiner als der Teiler“ heißt $k<m$. Nur beim Teiler $x-x_0$ mit $m=1$ ist der Rest eine Konstante.
--- falsch
Weil die Division hier noch nicht fertig ist: Ein Rest vom Grad 1 lässt sich weiter durch $Q$ teilen, bis eine Zahl übrig bleibt; erst dann ist das Verfahren beendet.
--- falsch
Weil der Rest immer einen Grad kleiner ist als der Zähler: Bei einem Zähler vom Grad 2 bleibt ein Rest vom Grad 1, unabhängig vom Grad des Nenners $Q$.
--- falsch
Weil der Rest denselben Grad haben muss wie der Polynomteil: Bei $P:Q$ hat der Polynomteil $2x-1$ den Grad 1, also auch der Rest $-8x+4$; das ist bei Polynomen die Regel.
:::
:::karte zusammenhang Zähler kleineren Grades
Was ergibt die Division mit Rest, wenn der Grad $n$ des Zählers kleiner ist als der Grad $m$ des Nenners?
---
Es gibt nichts zu teilen: Der Polynomteil ist $S=0$ und der Rest $T=P_n$. So ergibt $(x+1):(x^2+1)$ den Polynomteil 0 und den Rest $x+1$.
--- falsch
Man vertauscht Zähler und Nenner und teilt dann wie gewohnt: $(x+1):(x^2+1)$ ergibt so den Polynomteil $x-1$ und den Rest $2$, wegen $x^2+1=(x+1)(x-1)+2$.
--- falsch
Die Division ist dann nicht erklärt: Der Satz verlangt $n\ge m$, und für $(x+1):(x^2+1)$ gibt es weder einen Polynomteil noch einen Rest.
--- falsch
Der Polynomteil ist der Zähler, $S=P_n$, und der Rest ist $T=0$, weil der Zähler schon kleiner ist als der Nenner. So ergibt $(x+1):(x^2+1)$ den Polynomteil $x+1$.
:::
:::karte zusammenhang Probe der Division
Wie prüft man das Ergebnis einer Division mit Rest, ohne die ganze Rechnung zu wiederholen?
---
Man setzt eine beliebige Zahl in $P_n(x)=S_{n-m}(x)\,Q_m(x)+T_k(x)$ ein, denn diese Gleichung gilt für alle $x\in\mathbb{R}$, und vergleicht beide Seiten. Für $P:Q$ bei $x=3$: $5\cdot4+(-20)=0=P(3)$.
--- falsch
Man setzt eine Zahl in Polynomteil plus Rest ein, ohne den Nenner: Polynomteil und Rest müssen zusammen den Wert des Zählers an dieser Stelle ergeben.
--- falsch
Man prüft, ob der Grad des Rests kleiner ist als der Grad des Nenners; ist das so, stimmt die Rechnung, denn ein falscher Schritt würde stets den Grad des Rests erhöhen.
--- falsch
Man multipliziert nur die höchsten Koeffizienten: $a_n$ muss gleich dem höchsten Koeffizienten von $S$ mal dem von $Q$ sein. Stimmt das, sind auch alle übrigen richtig.
:::
:::karte zusammenhang Quotient zweier Polynome
Warum braucht man für den Quotienten zweier Polynome eine Division mit Rest, für Summe, Differenz und Produkt aber nicht?
---
Weil Summe, Differenz und Produkt von Polynomen wieder Polynome sind, der Quotient meist nicht. Die Division mit Rest zerlegt ihn in ein Polynom und einen kleinen Rest, wie $17:5=3$ Rest $2$.
--- falsch
Weil der Quotient zweier Polynome stets ein Polynom ist, das man aber nur mit der Division mit Rest ausrechnen kann; bei Summe, Differenz und Produkt rechnet man direkt.
--- falsch
Weil beim Teilen der Grad wächst: Der Quotient zweier Polynome hat den Grad $n+m$, und die Division mit Rest bringt ihn auf einen Grad unter $m$ herunter, wie beim Kürzen.
--- falsch
Weil Summe, Differenz und Produkt von Polynomen nur für Polynome gleichen Grades erklärt sind, der Quotient dagegen für beliebige; die Division mit Rest gleicht die Grade von Zähler und Nenner an.
:::
:::karte zusammenhang höchster Koeffizient des Nenners
Warum braucht jeder Schritt der Division mit Rest den höchsten Koeffizienten $b_m\neq0$ des Nenners?
---
Weil man durch $b_m$ teilt: Der Vorfaktor $\frac{a_n}{b_m}x^{n-m}$ ist so gewählt, dass $\frac{a_n}{b_m}x^{n-m}\cdot b_mx^m=a_nx^n$ die höchste Potenz des Zählers auslöscht.
--- falsch
Weil sonst der Rest nicht kleiner würde: Hätte der Nenner keinen höchsten Koeffizienten, hätte der Rest immer den Grad des Zählers, und teilen müsste man dabei nie.
--- falsch
Weil $b_m$ der Rest des ersten Schritts ist: Der erste Rest ist stets der höchste Koeffizient des Nenners, und ein Rest null würde das Verfahren sofort beenden.
--- falsch
Weil man durch $a_n$ teilt: Der Vorfaktor ist $\frac{b_m}{a_n}x^{m-n}$, und ohne $b_m$ wäre er null, sodass in jedem Schritt nichts abgezogen würde und der Grad nie sinkt.
:::
::::
