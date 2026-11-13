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

::::formelsammlung
**Horner-Darstellung**

$$P_n(x)=\Bigl\{\Bigl[\cdots\bigl(\{a_nx+a_{n-1}\}\cdot x+a_{n-2}\bigr)\cdot x+\dots+a_2\Bigr]\cdot x+a_1\Bigr\}\cdot x+a_0$$

Durch wiederholtes Ausklammern von $x$; von innen nach außen gelesen $c_n(x)=a_n$, $c_i(x)=c_{i+1}(x)\,x+a_i$ und am Ende $c_0(x)=P_n(x)$.

**Horner-Rekursion**

$$c_n:=a_n,\qquad c_i:=c_{i+1}\,x_0+a_i\quad\text{für }i=n-1,n-2,\dots,0$$

Für ein Polynom vom Grad $n\ge1$ und eine feste Stelle $x_0$. Im Schema stehen oben alle Koeffizienten, auch die Nullen; $n$ Multiplikationen statt $2n-1$.

**Wert und Quotient**

$$c_0=P_n(x_0),\qquad P_n(x)=(x-x_0)\,Q_{n-1}(x)+c_0$$

Mit $Q_{n-1}(x):=c_nx^{n-1}+c_{n-1}x^{n-2}+\dots+c_2x+c_1$ vom Grad $n-1$: Die $c_i$ sind Zwischenergebnisse und zugleich die Koeffizienten des Quotienten.
::::

::::lernkarten
:::karte begriff Horner-Darstellung
Was ist die Horner-Darstellung eines Polynoms $P_n$, und welche Zwischenwerte $c_i(x)$ entstehen, wenn man sie von innen nach außen liest?
---
Die Schachtelung, die aus der Summe $\sum_{i=0}^na_ix^i$ durch wiederholtes Ausklammern von $x$ entsteht. Von innen nach außen gelesen ist $c_n(x)=a_n$, $c_i(x)=c_{i+1}(x)\,x+a_i$ und am Ende $c_0(x)=P_n(x)$.
--- falsch
Die ausmultiplizierte Summe $\sum_{i=0}^na_ix^i$, Summand für Summand gelesen. Dabei ist $c_i(x)=a_ix^i$ der $i$-te Summand, und die Summe aller $c_i(x)$ ergibt am Ende $P_n(x)$.
--- falsch
Die Schachtelung, die durch wiederholtes Ausklammern von $x$ entsteht. Von innen nach außen gelesen ist $c_n(x)=a_0$, $c_i(x)=c_{i+1}(x)\,x+a_{n-i}$ und am Ende $c_0(x)=a_n$.
--- falsch
Die Schachtelung, die durch wiederholtes Ausklammern von $x$ entsteht. Von innen nach außen gelesen ist $c_n(x)=a_n$, $c_i(x)=c_{i+1}(x)+a_i\,x$ und am Ende $c_0(x)=P_n(x)$, ganz ohne Potenzen.
:::
:::karte begriff Horner-Schema
Was ist das Horner-Schema, und was liefert es für ein Polynom $P_n$ an einer Stelle $x_0$?
---
Ein Rechenverfahren in drei Zeilen: oben alle Koeffizienten, auch die Nullen, darunter die Produkte $c_{i+1}x_0$, unten die Summen $c_i$. Es liefert $c_0=P_n(x_0)$ und die Koeffizienten des Quotienten bei Division durch $x-x_0$.
--- falsch
Ein Rechenverfahren in drei Zeilen: oben die Potenzen $x_0,x_0^2,\dots,x_0^n$, darunter die Koeffizienten, unten deren Produkte. Es liefert den Wert $P_n(x_0)$ mit $2n-1$ Multiplikationen, aber keinen Quotienten.
--- falsch
Ein Rechenverfahren in drei Zeilen, das alle Nullstellen von $P_n$ auf einmal liefert: Die untere Zeile enthält die Nullstellen, und die letzte Zahl $c_0$ gibt an, wie viele es sind; $x_0$ dient nur als Startwert.
--- falsch
Ein Rechenverfahren in drei Zeilen: oben die Koeffizienten, Nullen lässt man weg, darunter die Produkte $c_{i+1}x_0$, unten die Summen $c_i$. Es liefert $c_0=P_n(x_0)$ und den Quotienten bei Division durch $x+x_0$.
:::
:::karte formel Horner an einer festen Stelle
Welche Rekursion legt das Horner-Schema für ein Polynom $P_n(x)=\sum_{k=0}^na_kx^k$ vom Grad $n\ge1$ an einer festen Stelle $x_0$ fest, und was liefert sie?
---
$c_n:=a_n$ und $c_i:=c_{i+1}\,x_0+a_i$ für $i=n-1,n-2,\dots,0$. Dann ist $c_0=P_n(x_0)$ und $P_n(x)=(x-x_0)\,Q_{n-1}(x)+c_0$ mit $Q_{n-1}(x):=c_nx^{n-1}+c_{n-1}x^{n-2}+\dots+c_2x+c_1$.
--- falsch
$c_0:=a_0$ und $c_i:=c_{i-1}\,x_0+a_i$ für $i=1,\dots,n$. Dann ist $c_n=P_n(x_0)$ und $P_n(x)=(x-x_0)\,Q_{n-1}(x)+c_n$ mit $Q_{n-1}(x):=c_0x^{n-1}+c_1x^{n-2}+\dots+c_{n-1}$.
--- falsch
$c_n:=a_n$ und $c_i:=c_{i+1}+a_i\,x_0$ für $i=n-1,\dots,0$. Dann ist $c_0=P_n(x_0)$ und $P_n(x)=(x+x_0)\,Q_{n-1}(x)+c_0$ mit $Q_{n-1}(x):=c_nx^{n-1}+c_{n-1}x^{n-2}+\dots+c_1$.
--- falsch
$c_n:=a_n$ und $c_i:=c_{i+1}\,x_0+a_i$ für $i=n-1,\dots,0$. Dann ist $c_0=P_n(x_0)$ und $P_n(x)=(x-x_0)\,Q_{n-1}(x)$ mit $Q_{n-1}(x):=c_nx^{n-1}+\dots+c_1+c_0$, ganz ohne Rest.
:::
:::karte herleitung Horner
Wie zeigt man, dass die Horner-Rekursion den Wert $c_0=P_n(x_0)$ und die Zerlegung $P_n(x)=(x-x_0)\,Q_{n-1}(x)+c_0$ liefert?
---
$c_0=P_n(x_0)$, weil die Rekursion die Horner-Darstellung bei $x=x_0$ von innen nach außen ausrechnet.
---
Ausmultiplizieren und Ordnen nach Potenzen ergibt $(x-x_0)\bigl[c_nx^{n-1}+\dots+c_1\bigr]+c_0=c_nx^n+(c_{n-1}-x_0c_n)x^{n-1}+\dots+(c_1-x_0c_2)x+(c_0-x_0c_1)$, weil jedes $c_i$ einmal mit $x$ und einmal mit $-x_0$ multipliziert wird.
---
Nach der Rekursion ist $c_n=a_n$ und jede Klammer $c_i-x_0c_{i+1}=a_i$; rechts steht also $P_n(x)$, weil genau seine Koeffizienten herauskommen.
---
Der Grad von $Q_{n-1}$ ist genau $n-1$, weil $c_n=a_n\neq0$ ist.
:::
:::karte zusammenhang Zahl der Multiplikationen
Warum braucht das Horner-Schema für den Wert $P_n(x_0)$ nur $n$ Multiplikationen statt $2n-1$?
---
Weil man wie geschrieben $n-1$ Multiplikationen für $x_0^2,\dots,x_0^n$ und $n$ für die Koeffizienten braucht. Durch wiederholtes Ausklammern von $x$ kommt jede Potenz von selbst heraus; für $n=10$ sind es 10 statt 19.
--- falsch
Weil das Horner-Schema die Potenzen $x_0^2,\dots,x_0^n$ in einer Tabelle nachschlägt, statt sie zu berechnen; nur die $n$ Multiplikationen mit den Koeffizienten bleiben übrig.
--- falsch
Weil das Horner-Schema die Hälfte der Koeffizienten überspringt: Nur jede zweite Spalte wird multipliziert, die übrigen werden nur addiert; so sind es für $n=10$ nur 10 statt 19 Multiplikationen.
--- falsch
Weil das Schema statt zu multiplizieren nur addiert: Die $n$ Multiplikationen sind die Additionen der unteren Zeile, die man als Multiplikationen zählt, weil sie gleich lange dauern.
:::
:::karte zusammenhang eine Rechnung, zwei Ergebnisse
Warum liefert eine einzige Rechnung im Horner-Schema sowohl den Wert $P_n(x_0)$ als auch den Quotienten bei Division durch $x-x_0$?
---
Weil die $c_i$ zugleich Zwischenergebnisse der Auswertung und Koeffizienten des Quotienten sind: Die letzte Zahl $c_0$ ist $P_n(x_0)$, die Zahlen davor ergeben $Q_{n-1}$. Bei $P$ und $x_0=2$: $P(x)=(x-2)(2x^2+x-9)-12$.
--- falsch
Weil man das Schema zweimal durchläuft, einmal vorwärts für den Wert und einmal rückwärts für den Quotienten; beide Durchläufe stehen nur in derselben Tabelle, damit man Platz spart.
--- falsch
Weil Wert und Quotient bei jedem Polynom übereinstimmen: Der Quotient ist das Polynom $P_n(x_0)\,x^{n-1}$, man liest also beides an derselben Zahl $c_0$ ab.
--- falsch
Weil die obere Zeile den Wert liefert und die untere den Quotienten: Die Koeffizienten $a_i$ ergeben zusammen $P_n(x_0)$, die $c_i$ sind die Koeffizienten von $Q_{n-1}$.
:::
:::karte zusammenhang Null für eine fehlende Potenz
Warum muss für eine fehlende Potenz eine Null in die obere Zeile des Horner-Schemas?
---
Weil jede Spalte zu einer Potenz gehört und das Schema die Potenzen über die Spalten zählt. Lässt man bei $S$ die Null für $x$ weg, rechnet es mit $x^3-3x^2+x+4$, und bei $x_0=2$ kommt 2 heraus statt $S(2)=0$.
--- falsch
Weil das Schema sonst eine Spalte zu wenig hat und die untere Zeile nicht aufgeht; das Ergebnis wäre zwar richtig, aber man könnte es nicht mehr an der letzten Stelle ablesen.
--- falsch
Weil die Null den Wert des Polynoms an der Stelle $x_0=0$ angibt, den man für den Quotienten braucht; ohne sie fehlt der Rest $c_0$ am Ende der unteren Zeile.
--- falsch
Weil das Schema sonst den Grad falsch bestimmt: Ohne die Null hätte $S$ den Grad 3 statt 4; der Wert $S(2)$ bliebe aber gleich, nur der Quotient wäre falsch.
:::
:::karte zusammenhang Grenzfälle des Horner-Schemas
Was liefert das Horner-Schema an den Stellen $x_0=0$ und $x_0=1$?
---
Für $x_0=0$ ist die untere Zeile die obere, $c_0=a_0=P(0)$. Für $x_0=1$ addiert das Schema alle Koeffizienten, bei $P$ ist $c_0=2-3-11+6=-6=P(1)$.
--- falsch
Für $x_0=0$ ist die untere Zeile null, weil jedes Produkt mit $0$ verschwindet, also $c_0=0$. Für $x_0=1$ ist die untere Zeile die obere, also $c_0=a_0$.
--- falsch
Für $x_0=0$ liefert es den höchsten Koeffizienten, $c_0=a_n$. Für $x_0=1$ liefert es die Anzahl der Koeffizienten, die von null verschieden sind, bei $P$ also 4.
--- falsch
Für $x_0=0$ ist die untere Zeile die obere, $c_0=a_0=P(0)$. Für $x_0=1$ multipliziert das Schema alle Koeffizienten, bei $P$ ist $c_0=2\cdot(-3)\cdot(-11)\cdot6=396$.
:::
:::karte zusammenhang Potenzen von x minus x0
Wie gewinnt man mit dem Horner-Schema die Darstellung eines Polynoms in Potenzen von $x-x_0$, etwa $d_3(x-1)^3+d_2(x-1)^2+d_1(x-1)+d_0$?
---
Man wendet das Schema wiederholt bei $x_0$ an, jedes Mal auf den neuen Quotienten: Der erste Rest ist $d_0$, der zweite $d_1$, und so weiter. Für $P$ bei $x_0=1$ ergibt das $d_0=-6$, $d_1=-11$, $d_2=3$, $d_3=2$.
--- falsch
Man wendet das Schema einmal bei $x_0$ an und liest die ganze untere Zeile ab: Ihre Zahlen sind von links nach rechts $d_3,d_2,d_1,d_0$, für $P$ bei $x_0=1$ also $2,-1,-12,-6$.
--- falsch
Man setzt $x_0$, $x_0+1$, $x_0+2$ und $x_0+3$ ein und erhält $d_0$ bis $d_3$ als die vier Werte des Polynoms; für $P$ bei $x_0=1$ ist $d_0=P(1)$, $d_1=P(2)$ und so weiter.
--- falsch
Man wendet das Schema wiederholt bei $x_0$ an, jedes Mal auf den neuen Quotienten: Der erste Rest ist $d_3$, der zweite $d_2$, und so weiter. Für $P$ bei $x_0=1$ ergibt das $d_3=-6$, $d_2=-11$, $d_1=3$, $d_0=2$.
:::
::::
