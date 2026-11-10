---
title: Stufe 7: Das Horner-Schema
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
order: 1230900
summary: Für den Teiler x-x 0 ist die Division so regelmäßig, dass ein Schema mit drei Zeilen genügt.
tags: Horner-Darstellung
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Für den Teiler $x-x_0$ ist die Division so regelmäßig, dass ein Schema mit drei Zeilen genügt. Es liefert zugleich den Wert $P(x_0)$ mit nur $n$ Multiplikationen. Deshalb werten Computer Polynome meist so aus.
:::

**Die Idee.** Rechnet man $P_n(x_0)$ wie geschrieben, braucht man $n-1$ Multiplikationen für $x_0^2,\dots,x_0^n$, $n$ weitere für die Koeffizienten und $n$ Additionen, zusammen $2n-1$ Multiplikationen. Klammert man wiederholt $x$ aus, kommt jede Potenz von selbst heraus, und $n$ Multiplikationen reichen. Für $n=10$ sind das 10 statt 19.

:::definition Definition 7.1 (Horner-Darstellung)
<span class="anker" id="satz-7-1"></span>

Durch wiederholtes Ausklammern von $x$ entsteht aus [(5.1)](polynome-und-koeffizienten.html#gl-5-1) die __Horner-Darstellung__

<span class="anker" id="gl-7-1"></span>
$$P_n(x)=\Bigl\{\Bigl[\cdots\bigl(\underbrace{\{a_nx+a_{n-1}\}}_{=\,c_{n-1}(x)}\cdot x+a_{n-2}\bigr)\cdot x+\dots+a_2\Bigr]\cdot x+a_1\Bigr\}\cdot x+a_0. \tag{7.1}$$

Von innen nach außen gelesen ist $c_n(x)=a_n$, $c_i(x)=c_{i+1}(x)\,x+a_i$ und am Ende $c_0(x)=P_n(x)$.
:::

:::satz Satz 7.2 (Horner bei $x_0$)
<span class="anker" id="satz-7-2"></span>

Sei $P_n(x)=\sum_{k=0}^na_kx^k$ ein Polynom vom Grad $n\ge1$ und $x_0\in\mathbb{R}$ fest. Setze

<span class="anker" id="gl-7-2"></span>
$$c_n:=a_n,\qquad c_i:=c_{i+1}\,x_0+a_i\quad\text{für }i=n-1,n-2,\dots,0. \tag{7.2}$$

Dann gilt

<span class="anker" id="gl-7-3"></span>
$$c_0=P_n(x_0),\qquad P_n(x)=(x-x_0)\,Q_{n-1}(x)+c_0 \tag{7.3}$$

mit $Q_{n-1}(x):=c_nx^{n-1}+c_{n-1}x^{n-2}+\dots+c_2x+c_1$ und $\operatorname{grad}Q_{n-1}=n-1$.
:::

:::beweis Horner
$c_0=P_n(x_0)$: Die Rekursion [(7.2)](#gl-7-2) rechnet [(7.1)](#gl-7-1) bei $x=x_0$ von innen nach außen aus. Für die zweite Gleichung multipliziert man aus und ordnet nach Potenzen:

$$(x-x_0)\bigl[c_nx^{n-1}+\dots+c_1\bigr]+c_0=c_nx^n+(c_{n-1}-x_0c_n)x^{n-1}+\dots+(c_1-x_0c_2)x+(c_0-x_0c_1).$$

Nach [(7.2)](#gl-7-2) ist $c_n=a_n$ und jede Klammer $c_i-x_0c_{i+1}=a_i$, rechts steht also $P_n(x)$. Wegen $c_n=a_n\neq0$ ist der Grad von $Q_{n-1}$ genau $n-1$.
:::

⁠**So liest man das:** Die $c_i$ sind Zwischenergebnisse der Rechnung und zugleich die Koeffizienten des Quotienten. Das ist der Grund, warum eine Rechnung beides liefert. Das Schema ordnet sie so:

|  | $a_n$ | $a_{n-1}$ | $a_{n-2}$ | $\cdots$ | $a_1$ | $a_0$ |
|---|---|---|---|---|---|---|
| $x_0$ |  | $c_nx_0$ | $c_{n-1}x_0$ | $\cdots$ | $c_2x_0$ | $c_1x_0$ |
|  | $c_n$ | $c_{n-1}$ | $c_{n-2}$ | $\cdots$ | $c_1$ | $c_0$ |

Die erste Zeile enthält alle Koeffizienten, auch die Nullen. Man schreibt $a_n$ nach unten, multipliziert mit $x_0$, schreibt das Ergebnis in die nächste Spalte, addiert, und so weiter.

:::abbildung hm1/k3horner 8
Horner-Schema für $P$ an der Stelle $x_0=2$. Die Pfeile zeigen den Ablauf: mal 2, dann addieren. Letzte Zahl: $P(2)=-12$. Die Zahlen davor sind die Koeffizienten des Quotienten: $P(x)=(x-2)(2x^2+x-9)-12$.
:::

::::beispiel
Abb. [8](#abb-8) rechnet mit 3 Multiplikationen $P(2)=-12$, direkt: $2\cdot8-3\cdot4-11\cdot2+6=-12$. Für $x_0=3$ lautet die untere Zeile $2,\ 3,\ -2,\ 0$: Es ist $P(3)=0$ und $P(x)=(x-3)(2x^2+3x-2)$.
::::

⁠**Grenzfälle:** Für $x_0=0$ ist die untere Zeile die obere, $c_0=a_0=P(0)$. Für $x_0=1$ addiert das Schema alle Koeffizienten, $c_0=2-3-11+6=-6=P(1)$. Wiederholt man das Schema mit dem Quotienten, entsteht die Darstellung in Potenzen von $x-x_0$ (Aufgabe [8](#aufg-8)).

:::frage Warum muss die Null für eine fehlende Potenz ins Schema?
Jede Spalte gehört zu einer Potenz, das Schema zählt die Potenzen über die Spalten. Lässt man bei $S$ die Null für $x$ weg, rechnet es mit $1,-3,1,4$, also mit $x^3-3x^2+x+4$. Bei $x_0=2$ kommt dann 2 heraus statt $S(2)=0$.
:::

:::aufgabe Aufgabe 8 ★ Horner rechnen
<span class="anker" id="aufg-8"></span>

(a) Berechne für $3x^4-2x^3+5x-7$ den Wert bei $x_0=-2$ und den Quotienten. (b) Wie viele Multiplikationen spart das Schema bei Grad 20? (c) Schreibe $P$ in der Form $d_3(x-1)^3+d_2(x-1)^2+d_1(x-1)+d_0$. Tipp: Das Schema wiederholt bei $x_0=1$ anwenden; $d_0$ ist der erste Rest, $d_1$ der zweite.

:::loesung
(a) Obere Zeile $3,-2,0,5,-7$ mit der Null für $x^2$, untere Zeile $3,-8,16,-27,47$. Also Wert 47 (direkt: $48+16-10-7=47$), Quotient $3x^3-8x^2+16x-27$. (b) $2\cdot20-1=39$ gegen 20: 19 Multiplikationen weniger, fast die Hälfte. (c) Bei $x_0=1$: $2,-1,-12,-6$; dann für den Quotienten: $2,1,-11$; dann $2,3$. Also $d_0=-6$, $d_1=-11$, $d_2=3$, $d_3=2$. Probe bei $x=0$: $-2+3+11-6=6=P(0)$.
:::
:::
