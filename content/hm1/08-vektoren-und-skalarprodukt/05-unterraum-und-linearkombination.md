---
title: Stufe 3: Unterraum und Linearkombination
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Vektoren und Skalarprodukt
order: 1280500
summary: Eine Gerade durch den Ursprung verhält sich wie ein kleiner Vektorraum, eine Gerade daneben nicht.
tags: Teilraum, linearer Unterraum, Linearkombination, lineare Hülle, Aufspann, Erzeugendensystem, Koeffizienten
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Eine Gerade durch den Ursprung verhält sich wie ein kleiner Vektorraum, eine Gerade daneben nicht. Diese Stufe sagt, woran man das erkennt und wie man solche Teilmengen aus Vektoren baut.
:::

**Die Idee.** Die Vielfachen von $\vec a$ liegen auf einer Geraden durch $O$. Addieren oder Strecken führt nicht heraus, denn $\lambda_1\vec a+\lambda_2\vec a=(\lambda_1+\lambda_2)\vec a$. Die Gerade $(0,2)+t\,\vec a$ scheitert schon am Strecken mit 0: Sie enthält den Nullvektor nicht (Abb. [4](#abb-4)).

:::definition Definition 3.1 (Unterraum)
<span class="anker" id="satz-3-1"></span>

Sei $V$ ein Vektorraum über $\mathbb K=\mathbb{R}$ oder $\mathbb{C}$. Eine Teilmenge $U\ne\emptyset$ von $V$ heißt __Teilraum__ oder __linearer Unterraum__ von $V$, wenn gilt:

<ul>

<li>

⁠**(U1)** $\vec0\in U$,

</li>

<li>

⁠**(U2)** $\vec x,\vec y\in U\implies\vec x+\vec y\in U$,

</li>

<li>

⁠**(U3)** $\vec x\in U\implies\alpha\cdot\vec x\in U$ für alle $\alpha\in\mathbb K$.

</li>

</ul>
:::

⁠**So liest man das:** Vektoren aus $U$ bleiben beim Addieren und Strecken in $U$. Darum ist $U$ selbst ein Vektorraum, die Rechenregeln erbt es von $V$. Wegen (U1) geht jeder Unterraum durch den Ursprung. **Beispiel:** $U=\{\lambda\,\vec a:\lambda\in\mathbb{R}\}$ erfüllt (U1) mit $\lambda=0$, (U2) wie oben und (U3) nach (V3), denn $\alpha(\lambda\vec a)=(\alpha\lambda)\vec a$. **Polynome:** Alle Polynome $a_0+a_1x+a_2x^2+a_3x^3$ bilden einen Unterraum. Die Polynome vom Grad *genau* 3 bilden keinen: $(x^3+x)+(-x^3+x^2)=x^2+x$ hat Grad 2, (U2) ist verletzt, und die Nullfunktion fehlt. **Grenzfälle:** $\{\vec0\}$ und $V$ selbst sind Unterräume.

:::definition Definition 3.2 (Linearkombination, Aufspann)
<span class="anker" id="satz-3-2"></span>

Seien $\vec a_1,\dots,\vec a_n\in V$. Dann heißt

<span class="anker" id="gl-3-1"></span>
$$\vec y:=\alpha_1\cdot\vec a_1+\dots+\alpha_n\cdot\vec a_n=\sum_{i=1}^n\alpha_i\cdot\vec a_i\in V \tag{3.1}$$

mit $\alpha_1,\dots,\alpha_n\in\mathbb K$ eine __Linearkombination__ der Vektoren $\vec a_1,\dots,\vec a_n$. Die Menge aller Linearkombinationen

$$\operatorname{span}\{\vec a_1,\dots,\vec a_n\}:=\Bigl\{\vec y\in V:\ \text{es gibt }\alpha_1,\dots,\alpha_n\in\mathbb K\text{ mit }\vec y=\sum_{i=1}^n\alpha_i\vec a_i\Bigr\}\subset V$$

heißt __lineare Hülle__ oder __Aufspann__ (englisch *span*) von $\vec a_1,\dots,\vec a_n$, und $\vec a_1,\dots,\vec a_n$ heißen __Erzeugendensystem__ dieser Menge.
:::

⁠**So liest man das:** Die Zahlen $\alpha_i$ heißen __Koeffizienten__, sie sagen, wie stark jeder Vektor eingeht. Im Modell ist $(5,0)=2\vec a-\vec b$ eine Linearkombination von $\vec a$ und $\vec b$. Ein Erzeugendensystem ist nicht eindeutig: $\operatorname{span}\{\vec a\}=\operatorname{span}\{-2\vec a\}$.

:::satz Satz 3.3 (Der Aufspann ist ein Unterraum)
<span class="anker" id="satz-3-3"></span>

$\operatorname{span}\{\vec a_1,\dots,\vec a_n\}$ ist immer ein linearer Unterraum von $V$.
:::

:::beweis Die drei Bedingungen
(U1): $\alpha_1=\dots=\alpha_n=0$ gibt $\vec0$. (U2): $\sum_i\alpha_i\vec a_i+\sum_i\beta_i\vec a_i=\sum_i(\alpha_i+\beta_i)\vec a_i$ nach (A1), (A2) und (V3). (U3): $\alpha\sum_i\alpha_i\vec a_i=\sum_i(\alpha\alpha_i)\vec a_i$ nach (V2) und (V3).
:::

:::abbildung hm1/k8span 4
Links $\operatorname{span}\{\vec a\}$, eine Gerade durch $O$, und die parallele Gerade $(0,2)+t\,\vec a$, die $O$ verfehlt und deshalb kein Unterraum ist. Rechts das schräge Gitter aller Kombinationen $s\vec a+t\vec b$ mit ganzen $s,t$. Der Punkt $(5,0)$ ist $2\vec a-\vec b$. Mit reellen $s,t$ wird die ganze Ebene erreicht.
:::

**Beispiel.** Jeder Punkt $(x_1,x_2)$ liegt in $\operatorname{span}\{\vec a,\vec b\}$. Komponentenweise verlangt $s\vec a+t\vec b=(x_1,x_2)$ die Gleichungen $3s+t=x_1$ und $s+2t=x_2$. Daraus folgt $s=\frac15(2x_1-x_2)$ und $t=\frac15(3x_2-x_1)$. Für $(5,0)$ ist das $s=2$, $t=-1$. Also ist $\operatorname{span}\{\vec a,\vec b\}=\mathbb{R}^2$. Die ungeraden Polynome $\alpha_1x+\alpha_2x^3+\alpha_3x^5$ sind der Unterraum $\operatorname{span}\{x,x^3,x^5\}$, das sind alle Polynome vom Grad $\le5$ mit $p(-x)=-p(x)$. In der Elektrotechnik bilden die Zweigströme, die alle Knotenregeln erfüllen, einen Unterraum: Summe und Vielfaches zulässiger Stromverteilungen sind wieder zulässig.

:::frage Ist jede Gerade ein Unterraum?
Nur die Geraden durch $O$. Für $\vec w=\vec p+t\vec v$ gilt das genau dann, wenn $\vec0$ auf der Geraden liegt, also wenn $\vec p\in\operatorname{span}\{\vec v\}$. Eine Gerade daneben ist ein verschobener Unterraum.
:::

:::aufgabe Aufgabe 3 ★★ Unterraum oder nicht
<span class="anker" id="aufg-3"></span>

Begründe für jede Menge: (a) $\{\vec x\in\mathbb{R}^3:x_1+x_2+x_3=0\}$, (b) $\{\vec x\in\mathbb{R}^3:x_1+x_2+x_3=1\}$, (c) $\{\vec x\in\mathbb{R}^3:x_1x_2=0\}$, (d) alle Polynome mit $p(2)=0$, (e) alle Polynome mit $p(0)=1$, (f) die Gerade $(6,2)+t\,\vec a$.

:::loesung
(a) Ja. $\vec0$ erfüllt die Gleichung, Summen und Vielfache von Lösungen sind Lösungen. (b) Nein, $\vec0$ fehlt. (c) Nein. $(1,0,0)$ und $(0,1,0)$ liegen darin, ihre Summe $(1,1,0)$ nicht. (d) Ja. $(p+q)(2)=0$ und $(\alpha p)(2)=0$, die Nullfunktion gehört dazu. (e) Nein, die Nullfunktion fehlt. (f) Ja, denn $t=-2$ gibt $\vec0$. Die Gerade ist $\operatorname{span}\{\vec a\}$.
:::
:::

:::aufgabe Aufgabe 4 ★★ Im Aufspann?
<span class="anker" id="aufg-4"></span>

Liegen $(2,3,4)$ und $(1,3,4)$ in $\operatorname{span}\{\vec c,\vec d\}$? Gib falls möglich die Koeffizienten an. Beschreibe $\operatorname{span}\{\vec c,\vec d\}$ durch eine einzige Gleichung für $x_1,x_2,x_3$ und prüfe sie an $\vec f$.

:::loesung
$s\vec c+t\vec d=(2s,s+t,2t)$. Für $(2,3,4)$ ist $s=1$, $t=2$, und $s+t=3$ passt: $(2,3,4)=\vec c+2\vec d$. Für $(1,3,4)$ ist $s=\frac12$, $t=2$, aber $s+t=\frac52\ne3$: nein. Aus $s=\frac{x_1}2$, $t=\frac{x_3}2$ folgt $x_2=\frac{x_1+x_3}2$, also die Gleichung $x_1-2x_2+x_3=0$. Für $\vec f$: $4-2-2=0$.
:::
:::
