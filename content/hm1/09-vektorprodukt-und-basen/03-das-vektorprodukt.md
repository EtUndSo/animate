---
title: Stufe 1: Das Vektorprodukt
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Vektorprodukt und Basen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/vektorprodukt-und-basen
knoten: Kapitel 9: Vektorprodukt und Basen
order: 1290300
summary: Zwei Richtungen im Raum spannen eine Ebene auf.
tags: Bilinearität, Parallelogramms, Rechtssystem, Rechte-Hand-Regel, Vektorprodukt, Kreuzprodukt, Regel von Sarrus, Lagrange-Identität
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Zwei Richtungen im Raum spannen eine Ebene auf. Gesucht ist eine Rechenvorschrift, die daraus die Richtung senkrecht zur Ebene macht, und zwar als Vektor, dessen Länge die Fläche angibt.
:::

**Die Idee.** Gesucht ist eine Abbildung $\mathbb{R}^3\times\mathbb{R}^3\to\mathbb{R}^3$, $(\vec u,\vec v)\mapsto\vec u\times\vec v$: Vektor mal Vektor ergibt Vektor. Sie soll vier Forderungen erfüllen (Abb. [1](#abb-1)):

<ul>

<li>

⁠**(E1)** __Bilinearität__: In jedem Eingang darf man Summen auseinanderziehen und Zahlen ausklammern,

$$(\vec u+\vec w)\times\vec v=(\vec u\times\vec v)+(\vec w\times\vec v),\qquad(\lambda\vec u)\times\vec v=\lambda(\vec u\times\vec v),$$

$$\vec u\times(\vec w+\vec v)=(\vec u\times\vec w)+(\vec u\times\vec v),\qquad\vec u\times(\lambda\vec v)=\lambda(\vec u\times\vec v).$$

</li>

<li>

⁠**(E2)** $\vec u\times\vec v$ steht senkrecht auf $\vec u$ und auf $\vec v$, also auf ganz $\operatorname{span}\{\vec u,\vec v\}$.

</li>

<li>

⁠**(E3)** $\|\vec u\times\vec v\|=\|\vec u\|\,\|\vec v\|\sin\alpha$ mit dem Winkel $\alpha\in[0,\pi]$ zwischen $\vec u$ und $\vec v$. Das ist die Fläche $A$ des aufgespannten __Parallelogramms__: Grundseite $\|\vec u\|$ mal Höhe $h=\|\vec v\|\sin\alpha$.

</li>

<li>

⁠**(E4)** Für linear unabhängige $\vec u,\vec v$ bilden $(\vec u,\vec v,\vec u\times\vec v)$ ein __Rechtssystem__. So heißen drei linear unabhängige Vektoren, die in dieser Reihenfolge wie Daumen, Zeigefinger und Mittelfinger der rechten Hand liegen (__Rechte-Hand-Regel__). Auch $(\vec e_1,\vec e_2,\vec e_3)$ ist eines.

</li>

</ul>

:::abbildung hm1/k9kreuz 1
Links im Raum: $\vec u$ und $\vec v$ spannen ein Parallelogramm auf, $\vec u\times\vec v=(2,-4,2)$ steht senkrecht darauf. Rechts der Blick senkrecht auf das Parallelogramm: Die Höhe $h$ ist der Rest der Projektion von $\vec v$ auf $\vec u$. Die Länge des Pfeils $\vec u\times\vec v$ ist die Maßzahl der Fläche: $\sqrt{24}=4{,}899$.
:::

Die Forderungen legen die Formel fest.

:::herleitung Die Formel aus den Forderungen
Nach (E3) ist $\vec e_i\times\vec e_i=\vec0$. Der Vektor $\vec e_1\times\vec e_2$ steht nach (E2) senkrecht auf $\vec e_1$ und $\vec e_2$, ist also ein Vielfaches von $\vec e_3$. Er hat nach (E3) die Länge 1 und ist nach (E4) gleich $+\vec e_3$. Ebenso folgen $\vec e_2\times\vec e_3=\vec e_1$ und $\vec e_3\times\vec e_1=\vec e_2$, die Indizes laufen zyklisch weiter. Vertauschte Faktoren geben das Minuszeichen, denn $\vec0=(\vec e_i+\vec e_j)\times(\vec e_i+\vec e_j)=\vec e_i\times\vec e_j+\vec e_j\times\vec e_i$. Nun zerlegt man $\vec u=\sum_iu_i\vec e_i$, $\vec v=\sum_jv_j\vec e_j$ und multipliziert mit (E1) aus:

$$\vec u\times\vec v=\sum_{i,j=1}^3u_iv_j\,(\vec e_i\times\vec e_j)=(u_2v_3-u_3v_2)\vec e_1+(u_3v_1-u_1v_3)\vec e_2+(u_1v_2-u_2v_1)\vec e_3.$$
:::

:::definition Definition 1.1 (Vektorprodukt)
<span class="anker" id="satz-1-1"></span>

Für $\vec u=(u_1,u_2,u_3)$ und $\vec v=(v_1,v_2,v_3)$ aus $\mathbb{R}^3$ heißt

<span class="anker" id="gl-1-1"></span>
$$\vec u\times\vec v:=\begin{pmatrix}u_2v_3-u_3v_2\\u_3v_1-u_1v_3\\u_1v_2-u_2v_1\end{pmatrix}\in\mathbb{R}^3 \tag{1.1}$$

das __Vektorprodukt__ oder __Kreuzprodukt__ von $\vec u$ und $\vec v$.
:::

⁠**So liest man das:** Das Ergebnis ist ein Vektor, anders als beim Skalarprodukt. Die erste Komponente benutzt die Indizes 2 und 3, die zweite 3 und 1, die dritte 1 und 2. Im Modell ist $\vec u\times\vec v=(1\cdot2-0\cdot1,\ 0\cdot0-2\cdot2,\ 2\cdot1-1\cdot0)=(2,-4,2)$.

⁠**Merkregel.** Man schreibt die Spalten $\vec e,\vec u,\vec v$ auf und wiederholt rechts die ersten beiden (__Regel von Sarrus__, formal, denn in der ersten Spalte stehen Vektoren). Die drei Diagonalen nach rechts unten zählen mit Plus, die drei nach rechts oben mit Minus:

$$\begin{array}{ccc|cc}\vec e_1&u_1&v_1&\vec e_1&u_1\\\vec e_2&u_2&v_2&\vec e_2&u_2\\\vec e_3&u_3&v_3&\vec e_3&u_3\end{array} \qquad \begin{aligned}\vec u\times\vec v={}&\vec e_1u_2v_3+u_1v_2\vec e_3+v_1\vec e_2u_3\\&-\vec e_3u_2v_1-u_3v_2\vec e_1-v_3\vec e_2u_1.\end{aligned}$$

:::satz Satz 1.2 (Eigenschaften des Vektorprodukts)
<span class="anker" id="satz-1-2"></span>

Das Vektorprodukt [(1.1)](#gl-1-1) erfüllt (E1) bis (E4). Außerdem gilt die __Lagrange-Identität__

<span class="anker" id="gl-1-2"></span>
$$\|\vec u\times\vec v\|^2+\langle\vec u,\vec v\rangle^2=\|\vec u\|^2\,\|\vec v\|^2. \tag{1.2}$$
:::

⁠**So liest man das:** Die Forderungen waren Wünsche, der Satz sagt, dass die Formel sie erfüllt. [(1.2)](#gl-1-2) ist $\sin^2\alpha+\cos^2\alpha=1$ in Vektorform. Im Modell: $24+1=5\cdot5$.

:::beweis Nachrechnen
(E1): Jedes Produkt in [(1.1)](#gl-1-1) enthält genau eine Komponente von $\vec u$ und genau eine von $\vec v$, also ist jede Komponente in beiden Eingängen linear.

(E2): Einsetzen ergibt $\langle\vec u\times\vec v,\vec u\rangle=(u_2v_3-u_3v_2)u_1+(u_3v_1-u_1v_3)u_2+(u_1v_2-u_2v_1)u_3=0$. Der Mechanismus: Von den sechs Produkten heben sich je zwei auf, zum Beispiel $u_2v_3u_1$ und $-u_1v_3u_2$. Für $\vec v$ geht es gleich.

Lagrange: Die Summanden mit $i=j$ fallen weg, die übrigen gehören paarweise zusammen:

$$\|\vec u\|^2\|\vec v\|^2-\langle\vec u,\vec v\rangle^2=\sum_{i,j}\bigl(u_i^2v_j^2-u_iv_iu_jv_j\bigr)=\sum_{i<j}\bigl(u_iv_j-u_jv_i\bigr)^2=\|\vec u\times\vec v\|^2.$$

(E3): Für $\vec u,\vec v\ne\vec0$ gibt [(1.2)](#gl-1-2) mit $\langle\vec u,\vec v\rangle=\|\vec u\|\|\vec v\|\cos\alpha$ sofort $\|\vec u\times\vec v\|^2=\|\vec u\|^2\|\vec v\|^2(1-\cos^2\alpha)=\|\vec u\|^2\|\vec v\|^2\sin^2\alpha$, und $\sin\alpha\ge0$. Ist ein Vektor $\vec0$, sind beide Seiten 0.

(E4), nur die Idee: Man dreht $\vec u$ und $\vec v$ so, dass $\vec u=\lambda\vec e_1$ mit $\lambda>0$ und $\vec v=\beta\vec e_1+\gamma\vec e_2$ mit $\gamma\ne0$ wird. Dass das Vektorprodukt bei der Drehung mitdreht, ist nicht trivial und wird hier nicht bewiesen. Dann gilt $\vec u\times\vec v=\lambda\gamma\,\vec e_3$. Für $\gamma>0$ zeigen $\vec v$ zur Seite von $\vec e_2$ und $\vec u\times\vec v$ nach oben, für $\gamma<0$ zeigen beide zur anderen Seite. In beiden Fällen sitzen die drei Vektoren wie Daumen, Zeigefinger und Mittelfinger.
:::

**Warum der Betrag eine Fläche ist.** Die Höhe über $\vec u$ ist die Länge des Rests der Projektion von $\vec v$ auf $\vec u$. Nach Pythagoras gilt $h^2=\|\vec v\|^2-\frac{\langle\vec u,\vec v\rangle^2}{\|\vec u\|^2}$. Mit $\|\vec u\|^2$ multipliziert steht dort $A^2=\|\vec u\|^2\|\vec v\|^2-\langle\vec u,\vec v\rangle^2$, und das ist nach [(1.2)](#gl-1-2) gerade $\|\vec u\times\vec v\|^2$. Im Modell ist $h^2=5-\frac15=\frac{24}5$, also $h=2{,}191$ und $A=\sqrt5\cdot2{,}191=4{,}899$. **Grenzfälle:** Für $\vec v=\vec u$ ist $\alpha=0$ und das Parallelogramm flach, $\vec u\times\vec u=\vec0$. Für $\vec u\perp\vec v$ ist $\sin\alpha=1$, und die Fläche wird das Rechteck $\|\vec u\|\,\|\vec v\|$. Im Modell liegen $\vec u,\vec v$ nahe an diesem Fall: $\alpha=78{,}46^\circ$, $\sin\alpha=0{,}980$.

:::frage Warum gibt es das Vektorprodukt nur im $\mathbb{R}^3$?
(E2) legt die Richtung nur fest, wenn senkrecht zu einer Ebene genau eine Richtung bleibt. Im $\mathbb{R}^2$ bleibt keine, im $\mathbb{R}^4$ bleibt eine ganze Ebene. Das trifft nur für den $\mathbb{R}^3$ zu.
:::

:::aufgabe Aufgabe 1 ★ Rechnen und vorhersagen
<span class="anker" id="aufg-1"></span>

Sei $\vec r=(1,0,2)$, $\vec s=(3,1,-1)$. (a) Berechne $\vec r\times\vec s$ und prüfe (E2) und [(1.2)](#gl-1-2). (b) Wie groß ist die Fläche des Parallelogramms? (c) Sage ohne Rechnung $\vec s\times\vec r$ und $(2,-1,3)\times(-4,2,-6)$ voraus.

:::loesung
(a) $\vec r\times\vec s=(0\cdot(-1)-2\cdot1,\ 2\cdot3-1\cdot(-1),\ 1\cdot1-0\cdot3)=(-2,7,1)$. Probe: $\langle(-2,7,1),\vec r\rangle=-2+2=0$, $\langle(-2,7,1),\vec s\rangle=-6+7-1=0$. Lagrange: $54+1=5\cdot11$. (b) $\sqrt{54}=7{,}348$. (c) $\vec s\times\vec r=(2,-7,-1)$ nach Satz [2.1](rechenregeln-und-geometrie-im-raum.html#satz-2-1) (ii). Wegen $(-4,2,-6)=-2\,(2,-1,3)$ ist das zweite Produkt $\vec0$.
:::
:::
