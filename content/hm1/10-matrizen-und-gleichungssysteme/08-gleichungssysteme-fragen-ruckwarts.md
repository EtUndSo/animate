---
title: Stufe 6: Gleichungssysteme fragen rückwärts
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
order: 1300800
summary: Bisher lief die Frage vorwärts: Zu x wird Ax gesucht.
tags: lineares Gleichungssystem, Unbekannten, rechte Seite, homogen, inhomogen, Lösungsmenge, Rang, lösbar
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Bisher lief die Frage vorwärts: Zu $x$ wird $Ax$ gesucht. Jetzt rückwärts: Zu $b$ werden alle $x$ mit $Ax=b$ gesucht. Es gibt drei Fragen: Gibt es eine Lösung? Wie viele? Wie berechnet man sie? Diese Stufe beantwortet die ersten beiden.
:::

**Die Idee.** Allgemein lautet die Aufgabe: Zu $L\in\operatorname{Lin}(V,W)$ und $w\in W$ suche $v$ mit $Lv=w$. In Koordinaten wird daraus $Ax=b$ mit $A=\mathcal L$ nach Satz [4.5](koordinaten-und-darstellungsmatrix.html#satz-4-5). Wer so denkt, kennt die Antworten schon: Lösbar heißt, $b$ liegt im Bild. Mehrdeutig heißt, der Kern ist nicht trivial.

:::definition Definition 6.1 (Lineares Gleichungssystem)
<span class="anker" id="satz-6-1"></span>

Zu $A=(a_{ij})\in\mathbb K^{m\times n}$ und $b\in\mathbb K^m$ heißt

<span class="anker" id="gl-6-1"></span>
$$A\cdot\begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}=b\quad\iff\quad\left\{\begin{aligned}a_{11}x_1+a_{12}x_2+\dots+a_{1n}x_n&=b_1\\&\ \,\vdots\\a_{m1}x_1+a_{m2}x_2+\dots+a_{mn}x_n&=b_m\end{aligned}\right. \tag{6.1}$$

ein __lineares Gleichungssystem__ mit $m$ Gleichungen und $n$ __Unbekannten__ $x_1,\dots,x_n$. Die $a_{ij}$ heißen Koeffizienten, $b$ heißt __rechte Seite__. Für $b=0$ heißt es __homogen__, sonst __inhomogen__. Die __Lösungsmenge__ ist $\mathbb L(A,b):=\{x\in\mathbb K^n:Ax=b\}$.
:::

:::definition Definition 6.2 (Bild, Kern und Rang)
<span class="anker" id="satz-6-2"></span>

Für $A\in\mathbb K^{m\times n}$ mit $L_A:x\mapsto Ax$ ist $\operatorname{im}A:=\operatorname{im}L_A=\{y\in\mathbb K^m:\exists\,x\text{ mit }Ax=y\}$ und $\ker A:=\ker L_A=\{x\in\mathbb K^n:Ax=0\}$. Der __Rang__ ist $\operatorname{rg}(A):=\dim(\operatorname{im}A)$, und für $L\in\operatorname{Lin}(V,W)$ ist $\operatorname{rg}(L):=\dim(\operatorname{im}L)$.
:::

⁠**So liest man das:** $\operatorname{im}A\subset\mathbb K^m$ und $\ker A\subset\mathbb K^n$ sind Unterräume. Der Dimensionssatz lautet hier $n=\dim\ker A+\operatorname{rg}(A)$. Der Rang hängt nicht von den Basen ab: Wegen $\mathcal L=\Phi_{\mathcal C}^{-1}\circ L\circ\Phi_{\mathcal B}$ ist $\operatorname{im}\mathcal L=\Phi_{\mathcal C}^{-1}(\operatorname{im}L)$, und die bijektive Abbildung $\Phi_{\mathcal C}^{-1}$ erhält die Dimension. Alle Matrizen derselben Abbildung $L$ haben also denselben Rang. Der Kern $\ker A$ ist genau die Lösungsmenge des homogenen Systems.

:::satz Satz 6.3 (Lösbarkeit und Lösungsstruktur)
<span class="anker" id="satz-6-3"></span>

<ol class="rm">

<li>

$Ax=b$ ist genau dann __lösbar__ (es gibt ein $x$ mit $Ax=b$), wenn $b\in\operatorname{im}A$.

</li>

<li>

Ist $x_{\mathrm{part}}$ eine feste Lösung von $Ax=b$ (__partikuläre Lösung__), so gilt

<span class="anker" id="gl-6-2"></span>
$$\mathbb L(A,b)=x_{\mathrm{part}}+\ker A=\{x_{\mathrm{part}}+\tilde x:\tilde x\in\ker A\}. \tag{6.2}$$

</li>

</ol>
:::

:::beweis Lösungsstruktur
(i) ist die Definition von $\operatorname{im}A$. (ii) Sei $x$ eine weitere Lösung. Dann ist $A(x-x_{\mathrm{part}})=Ax-Ax_{\mathrm{part}}=b-b=0$, also $\tilde x:=x-x_{\mathrm{part}}\in\ker A$ und $x=x_{\mathrm{part}}+\tilde x$. Umgekehrt ist für $\tilde x\in\ker A$ auch $A(x_{\mathrm{part}}+\tilde x)=b+0=b$.
:::

⁠**So liest man das:** Kurz gesagt: Ist das System lösbar, ist die Lösungsmenge der an eine Lösung verschobene Kern. Das sind die Parallelen in Abb. [3](kern-bild-und-die-bilanz-der-dimensionen.html#abb-3): Die blaue Gerade ist $\mathbb L(P,(3,6))$. Eine Zahl von Lösungen wie „genau zwei“ ist unmöglich: Ein Kernvektor $\tilde x\ne0$ liefert mit allen Vielfachen $t\tilde x$ unendlich viele Lösungen.

| Fall | Bedingung | Lösungsmenge |
|---|---|---|
| keine Lösung | $b\notin\operatorname{im}A$ | $\mathbb L=\emptyset$ |
| genau eine Lösung | $b\in\operatorname{im}A$, $\ker A=\{0\}$ | $\mathbb L=\{x_{\mathrm{part}}\}$ |
| unendlich viele Lösungen | $b\in\operatorname{im}A$, $\ker A\ne\{0\}$ | $\mathbb L=x_{\mathrm{part}}+\ker A$ |

Für zwei Gleichungen mit zwei Unbekannten sind das zwei Geraden (Abb. [7](#abb-7)). Beispiel mit der flachen Matrix: Es ist $Q(2,0,1)=(3,7,10)$, also $\mathbb L(Q,(3,7,10))=\{(2,0,1)+t(-2,1,0):t\in\mathbb{R}\}$. Für $b=(3,7,11)$ gibt es keine Lösung. Der Grund: Zeile 3 von $Q$ ist die Summe der Zeilen 1 und 2, also gilt für jedes $y\in\operatorname{im}Q$ die Beziehung $y_3=y_1+y_2$, und das verletzt $11\ne3+7$.

:::abbildung hm1/k10faelle 7
Die blaue Gerade ist $x_1+x_2=3$. Links schneidet die rote Gerade $2x_1-x_2=3$ sie in $(2,1)$. Mitte: Bei $2x_1+2x_2=2$ sind beide parallel. Rechts: $2x_1+2x_2=6$ ist dieselbe Gerade, jeder Punkt löst das System. Mitte und rechts haben dieselbe Matrix, nur die rechte Seite ist anders.
:::

:::satz Satz 6.4 (Existenz und Eindeutigkeit)
<span class="anker" id="satz-6-4"></span>

Sei $A\in\mathbb K^{m\times n}$.

<ol class="rm">

<li>

(Existenz) Ist $\operatorname{rg}(A)=m$, so gibt es zu jedem $b\in\mathbb K^m$ mindestens eine Lösung.

</li>

<li>

(Eindeutigkeit) Ist $\operatorname{rg}(A)=n$, so gibt es zu jedem $b\in\mathbb K^m$ höchstens eine Lösung.

</li>

</ol>
:::

:::beweis Existenz und Eindeutigkeit
(i) $\dim(\operatorname{im}A)=m=\dim\mathbb K^m$ ergibt $\operatorname{im}A=\mathbb K^m$, also ist jedes $b$ im Bild. (ii) Der Dimensionssatz gibt $\dim\ker A=n-\operatorname{rg}(A)=0$, also $\ker A=\{0\}$. Nach [(6.2)](#gl-6-2) besteht $\mathbb L(A,b)$ dann aus höchstens einem Vektor.
:::

⁠**So liest man das:** Am Rang entscheidet sich alles. Es ist immer $\operatorname{rg}(A)\le\min(m,n)$. Für $\operatorname{rg}(A)<m$ ist $\operatorname{im}A\ne\mathbb K^m$, also gibt es rechte Seiten ohne Lösung. Für $m=n=\operatorname{rg}(A)$ gibt es zu jedem $b$ genau eine Lösung. **Warum die Bedingung nötig ist:** $Q$ hat Rang $2<3$, und für $(3,7,11)$ fehlt die Lösung, für $(3,7,10)$ gibt es unendlich viele.

In der Elektrotechnik entstehen genau solche Systeme: Das Knotenpotentialverfahren und das Maschenstromverfahren liefern $Ax=b$ mit Leitwerten oder Widerständen in $A$, den Quellen in $b$ und den gesuchten Potentialen oder Maschenströmen in $x$.

:::frage Bedeuten mehr Unbekannte als Gleichungen immer unendlich viele Lösungen?
Nein. Richtig ist: Bei $n>m$ ist $\dim\ker A\ge n-m>0$, eine eindeutige Lösung ist also unmöglich. Aber es kann auch gar keine geben: $x_1+x_2+x_3=1$, $x_1+x_2+x_3=2$ widersprechen sich.
:::

:::aufgabe Aufgabe 9 ★★ Geraden und Lösungsmengen
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Drei Gleichungen, zwei Unbekannte: $x_1+x_2=2$, $x_1-x_2=0$, $2x_1+x_2=3$. Löse das System und deute es als drei Geraden. Was ändert sich, wenn die letzte rechte Seite 4 ist?

</li>

<li>

Sei $A\in\mathbb{R}^{2\times3}$. Warum hat $Ax=b$ nie genau eine Lösung?

</li>

<li>

Ein System hat die Lösung $(1,1,0)$, und es ist $\ker A=\operatorname{span}\{(1,-1,1)\}$. Sind $(3,-1,2)$ und $(2,0,0)$ Lösungen?

</li>

</ol>

:::loesung
(a) Die ersten beiden Gleichungen ergeben $x=(1,1)$, und $2+1=3$ passt: Die drei Geraden gehen durch einen Punkt. Mit rechter Seite 4 gehen sie nicht mehr durch einen Punkt, es gibt keine Lösung. Die erweiterte Matrix hat dann Rang 3, $A$ hat Rang 2. (b) Es ist $\dim\ker A=3-\operatorname{rg}(A)\ge1$, und ein nichttrivialer Kern schließt eine einzige Lösung aus. (c) $(3,-1,2)-(1,1,0)=(2,-2,2)=2(1,-1,1)$ liegt im Kern, also Lösung. $(2,0,0)-(1,1,0)=(1,-1,0)$ ist kein Vielfaches von $(1,-1,1)$, also keine Lösung.
:::
:::
