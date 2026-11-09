---
title: Stufe 6: Division mit Rest
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Funktionen und Polynome
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
