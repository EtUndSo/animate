---
title: Stufe 2: Die Spalten sind die Bilder
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
order: 1300400
summary: Eine lineare Abbildung mathbb K ntomathbb K m bildet unendlich viele Vektoren ab.
tags: Koeffizienten, Matrix, Zeilenvektor, Spaltenvektor, quadratisch, transponiert, Einheitsmatrix, Hauptdiagonale
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Eine lineare Abbildung $\mathbb K^n\to\mathbb K^m$ bildet unendlich viele Vektoren ab. Diese Stufe zeigt, dass endlich viele Zahlen sie vollständig festlegen.
:::

**Die Idee.** Jeder Vektor ist eine Summe gestreckter Einheitsvektoren: $x=x_1e_1+\dots+x_ne_n$. Nach Satz [1.2](lineare-abbildungen.html#satz-1-2) (b) ist deshalb $L(x)=x_1L(e_1)+\dots+x_nL(e_n)$. Wer die $n$ Bilder $L(e_j)$ kennt, kennt $L$. Diese Bilder schreibt man als Spalten nebeneinander.

**An Zahlen.** Die Drehung schickt $e_1$ auf $e_2=(0,1)$ und $e_2$ auf $-e_1=(-1,0)$. Das sind die Spalten von $D$. Die Scherung lässt $e_1$ fest und schickt $e_2$ auf $(1,1)$, das sind die Spalten von $S$ (Abb. [2](#abb-2)). Für $x=(2,1)$ folgt $Dx=2(0,1)+1(-1,0)=(-1,2)$ und $Sx=2(1,0)+1(1,1)=(3,1)$.

:::abbildung hm1/k10quadrat 2
Links das Einheitsquadrat mit den Basisvektoren. Mitte und rechts sein Bild. Die roten und grünen Pfeile sind die erste und die zweite Spalte der Matrix. Das Bild des ganzen Quadrats folgt aus diesen zwei Pfeilen.
:::

:::definition Definition 2.1 (Matrix)
<span class="anker" id="satz-2-1"></span>

Ein Schema aus $m$ Zeilen und $n$ Spalten

$$A=\begin{pmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{pmatrix}=(a_{ij})_{\substack{i=1,\dots,m\\j=1,\dots,n}}$$

mit festen Einträgen $a_{ij}\in\mathbb K$ (__Koeffizienten__) heißt $m\times n$-__Matrix__, kurz $A\in\mathbb K^{m\times n}$. Der __Zeilenvektor__ $A_{i\bullet}=(a_{i1},\dots,a_{in})$ ist die $i$-te Zeile, der __Spaltenvektor__ $A_{\bullet j}=(a_{1j},\dots,a_{mj})$ die $j$-te Spalte. Für $m=n$ heißt $A$ __quadratisch__.
:::

⁠**So liest man das:** Zuerst steht immer die Zeile. In $T=\bigl(\begin{smallmatrix}1&0&2\\3&1&0\end{smallmatrix}\bigr)\in\mathbb{R}^{2\times3}$ ist der Eintrag in Zeile 2, Spalte 1 gleich 3, der in Zeile 1, Spalte 3 gleich 2.

:::definition Definition 2.2 (Produkt von Matrix und Vektor)
<span class="anker" id="satz-2-2"></span>

Für $A\in\mathbb K^{m\times n}$ und $x\in\mathbb K^n$ ist

<span class="anker" id="gl-2-1"></span>
$$A\cdot x:=\begin{pmatrix}a_{11}x_1+a_{12}x_2+\dots+a_{1n}x_n\\\vdots\\a_{m1}x_1+a_{m2}x_2+\dots+a_{mn}x_n\end{pmatrix}=x_1A_{\bullet1}+\dots+x_nA_{\bullet n}\in\mathbb K^m. \tag{2.1}$$
:::

⁠**So liest man das:** Es gibt zwei gleichwertige Sichten. *Spaltenweise* ist $Ax$ eine Linearkombination der Spalten, $x_j$ sagt, wie viel von Spalte $j$ eingeht. *Zeilenweise* ist die $i$-te Komponente „Zeile $i$ mal $x$“. Für $\mathbb K=\mathbb{R}$ ist das das Skalarprodukt $\langle A_{i\bullet}^T,x\rangle$; dabei macht das hochgestellte $T$ (__transponiert__) aus einer Zeile die gleiche Spalte. Die Spaltenzahl von $A$ muss die Länge von $x$ sein. Beispiel: $T\cdot(2,1,1)=(1\cdot2+0+2\cdot1,\ 3\cdot2+1+0)=(4,7)$, oder spaltenweise $2(1,3)+1(0,1)+1(2,0)=(4,7)$.

:::satz Satz 2.3 (Matrizen sind genau die linearen Abbildungen)
<span class="anker" id="satz-2-3"></span>

<ol class="rm">

<li>

Für $A\in\mathbb K^{m\times n}$ ist $L_A:\mathbb K^n\to\mathbb K^m$, $x\mapsto Ax$ linear.

</li>

<li>

Zu jedem $L\in\operatorname{Lin}(\mathbb K^n,\mathbb K^m)$ gibt es genau eine Matrix $A$ mit $L=L_A$. Ihre Spalten sind $A_{\bullet j}=L(e_j)$.

</li>

</ol>
:::

:::beweis Matrizen und lineare Abbildungen
(i) Für die $i$-te Komponente gilt $\sum_ja_{ij}(\alpha x_j+y_j)=\alpha\sum_ja_{ij}x_j+\sum_ja_{ij}y_j$, weil man in $\mathbb K$ ausmultiplizieren darf. Also ist $A(\alpha x+y)=\alpha Ax+Ay$. Mit $\alpha=1$ folgt (L1), mit $y=0$ folgt (L2).

(ii) Setze $A_{\bullet j}:=L(e_j)$. Dann ist $L(x)=L(\sum_jx_je_j)=\sum_jx_jL(e_j)=\sum_jx_jA_{\bullet j}=Ax$ nach Satz [1.2](lineare-abbildungen.html#satz-1-2) (b) und [(2.1)](#gl-2-1). Eindeutig: Aus [(2.1)](#gl-2-1) folgt $Ae_j=A_{\bullet j}$, die Spalten sind also durch $L$ erzwungen.
:::

⁠**So liest man das:** Kurz gesagt: Die $j$-te Spalte ist das Bild des $j$-ten Basisvektors. **Grenzfälle:** Die Nullmatrix $0\in\mathbb K^{m\times n}$ gehört zur Nullabbildung. Für $m=n=1$ ist $A=(b)$ und $L_A(x)=bx$. Die __Einheitsmatrix__ $E_n$ hat die Spalten $e_1,\dots,e_n$, also Einsen auf der __Hauptdiagonale__ $a_{11},a_{22},\dots$ und sonst Nullen. Sie gehört zu $\operatorname{Id}$: $E_nx=x$.

:::frage Warum stehen die Bilder in den Spalten und nicht in den Zeilen?
Weil der Eingang $x$ die Spalten gewichtet, wie [(2.1)](#gl-2-1) zeigt. Schriebe man die Bilder in Zeilen, müsste $x$ links von der Matrix stehen. Das ist eine Vereinbarung, die alle Rechenregeln dieses Kapitels festlegt.
:::

:::aufgabe Aufgabe 2 ★★ Matrizen aus Bildern
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Bestimme aus den Bildern von $e_1$ und $e_2$ die Matrix der Drehung um den Winkel $\varphi$ gegen den Uhrzeigersinn. Prüfe, dass sich für $\varphi=\pi/2$ die Matrix $D$ ergibt.

</li>

<li>

Bestimme die Matrizen der Spiegelung an der $x_1$-Achse und der Projektion $(x_1,x_2)\mapsto(x_1,0)$.

</li>

<li>

Berechne $Y\cdot(3,-2)$ für $Y=\begin{pmatrix}2&-1\\1&3\\0&4\end{pmatrix}$ zeilenweise und spaltenweise. Aus welchem Raum in welchen bildet $Y$ ab?

</li>

</ol>

:::loesung
(a) $e_1$ geht auf $(\cos\varphi,\sin\varphi)$, $e_2$ auf $(-\sin\varphi,\cos\varphi)$, also $\begin{pmatrix}\cos\varphi&-\sin\varphi\\\sin\varphi&\cos\varphi\end{pmatrix}$. Für $\varphi=\pi/2$ ist das $D$. (b) $\bigl(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr)$ und $\bigl(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\bigr)$, denn $e_2$ geht auf $-e_2$ beziehungsweise auf 0. (c) Zeilenweise: $(2\cdot3+1\cdot2,\ 3-6,\ -8)=(8,-3,-8)$. Spaltenweise: $3(2,1,0)-2(-1,3,4)=(8,-3,-8)$. $Y$ bildet $\mathbb{R}^2$ in den $\mathbb{R}^3$ ab.
:::
:::
