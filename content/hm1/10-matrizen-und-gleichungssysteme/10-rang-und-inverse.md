---
title: Stufe 8: Rang und Inverse
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
adresse: elektrotechnik/1-semester/hohere-mathematik-1/matrizen-und-lineare-gleichungssysteme
knoten: Kapitel 10: Matrizen und lineare Gleichungssysteme
order: 1301000
summary: Die Treppe hat r Stufen.
tags: Zeilenrang, Spaltenrang, Inverse, obere Dreiecksform
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Die Treppe hat $r$ Stufen. Diese Stufe zeigt, was $r$ misst: den Rang, und zwar sowohl in den Spalten als auch in den Zeilen. Damit wird Lösbarkeit zur Rechenaufgabe, und die Inverse einer Matrix lässt sich mit demselben Verfahren berechnen.
:::

**Die Idee.** In Zeilenstufenform kann man Abhängigkeiten ablesen (Abb. [9](#abb-9)). Keine der $r$ Pivotzeilen lässt sich aus den anderen bauen, denn jede hat ihr Pivot dort, wo die Zeilen darunter Nullen haben. Für die Pivotspalten gilt dasselbe. Beide Zählungen ergeben also $r$.

:::abbildung hm1/k10stufen 9
Zeilenstufenform mit $m=4$, $n=6$. Unter der roten Treppe stehen nur Nullen. Die Pivots sind von null verschieden, die Sterne ergeben sich aus der Rechnung. Spalten ohne Pivot gehören zu freien Variablen.
:::

:::definition Definition 8.1 (Zeilenrang und Spaltenrang)
<span class="anker" id="satz-8-1"></span>

Für $A\in\mathbb K^{m\times n}$ heißt

$$\operatorname{Zrg}(A):=\dim\operatorname{span}\{A_{1\bullet},\dots,A_{m\bullet}\},\qquad\operatorname{Srg}(A):=\dim\operatorname{span}\{A_{\bullet1},\dots,A_{\bullet n}\}$$

__Zeilenrang__ und __Spaltenrang__. Das ist die Höchstzahl linear unabhängiger Zeilen beziehungsweise Spalten.
:::

⁠**So liest man das:** Bei $Q$ ist Zeile 3 die Summe der Zeilen 1 und 2, die ersten beiden sind unabhängig, also $\operatorname{Zrg}(Q)=2$. Spalte 2 ist das Doppelte von Spalte 1, und die Spalten 1 und 3 sind unabhängig, also $\operatorname{Srg}(Q)=2$. Dass beide Zahlen übereinstimmen, ist kein Zufall. Bei großen Formaten sieht man das einer Matrix nicht an.

:::satz Satz 8.2 (Zeilenrang gleich Spaltenrang)
<span class="anker" id="satz-8-2"></span>

Für jede Matrix $A$ mit Zeilenstufenform $\tilde A$ mit $r$ Stufen gilt $\operatorname{Zrg}(A)=\operatorname{Srg}(A)=\operatorname{rg}(A)=\operatorname{rg}(\tilde A)=r$.
:::

:::beweis Zeilenrang gleich Spaltenrang
Wegen [(2.1)](die-spalten-sind-die-bilder.html#gl-2-1) ist $\operatorname{im}A$ der Aufspann der Spalten, also $\operatorname{rg}(A)=\operatorname{Srg}(A)$.

⁠*Zeilenumformungen ändern beide Ränge nicht.* Eine neue Zeile ist eine Linearkombination alter Zeilen, und wegen der Umkehrbarkeit gilt das auch umgekehrt. Der Aufspann der Zeilen bleibt also gleich. Nach Satz [7.1](der-gau-algorithmus.html#satz-7-1) bleibt $\ker A$ gleich, nach dem Dimensionssatz also auch $\operatorname{rg}(A)=n-\dim\ker A$.

⁠*In Stufenform ist alles ablesbar.* Sei $\tilde A$ die Stufenform. Für eine Nullkombination der Pivotzeilen sieht man im ersten Pivot, dass der erste Koeffizient null ist, denn die Zeilen darunter haben dort Nullen. Dann folgt das Gleiche für den zweiten und so weiter. Also sind die $r$ Pivotzeilen unabhängig und $\operatorname{Zrg}(\tilde A)=r$. Genauso sind die Pivotspalten unabhängig: Hier beginnt man mit der letzten Pivotzeile. Alle Spalten haben in den letzten $m-r$ Zeilen Nullen, liegen also in einem Raum der Dimension $r$. Damit ist $\operatorname{Srg}(\tilde A)=r$.
:::

⁠**So liest man das:** Den Rang bestimmt man durch Gauß und Zählen der Stufen, nicht durch Prüfen aller Spaltenkombinationen. Für $Q$ ist $r=2$, für $H$ ist $r=3$, für $P$ ist $r=1$.

:::satz Satz 8.3 (Lösbarkeitstest)
<span class="anker" id="satz-8-3"></span>

$Ax=b$ ist genau dann lösbar, wenn $\operatorname{rg}(A)=\operatorname{rg}(A\,|\,b)$, wobei $(A\,|\,b)\in\mathbb K^{m\times(n+1)}$ die um die Spalte $b$ erweiterte Matrix ist.
:::

:::beweis Lösbarkeitstest
Lösbar heißt $b\in\operatorname{im}A=\operatorname{span}\{A_{\bullet1},\dots,A_{\bullet n}\}$. Genau dann vergrößert die zusätzliche Spalte $b$ den Aufspann nicht. Sonst steigt seine Dimension um 1.
:::

⁠**So liest man das:** Im Tableau heißt das: Es gibt keine Zeile der Form $0=\tilde b_i\ne0$. Bei $Q$ steigt der Rang für $b=(3,7,11)$ von 2 auf 3, für $b=(3,7,10)$ bleibt er 2. Zusammen mit Stufe [7](der-gau-algorithmus.html#stufe-7) ergibt das die vollständige Antwort:

| Ränge | Lösungen | Grund |
|---|---|---|
| $\operatorname{rg}(A)<\operatorname{rg}(A\,\vert \,b)$ | keine | Eine Zeile lautet $0=\tilde b_i\ne0$ |
| $\operatorname{rg}(A)=\operatorname{rg}(A\,\vert \,b)=n$ | genau eine | Jede Spalte hat ein Pivot, keine freie Variable |
| $\operatorname{rg}(A)=\operatorname{rg}(A\,\vert \,b)<n$ | unendlich viele | $n-r$ freie Variablen, $\dim\ker A=n-r$ |

**Die Inverse.** Sei $A\in\mathbb K^{n\times n}$ mit $\operatorname{rg}(A)=n$. Dann ist $L_A$ bijektiv (Satz [3.5](kern-bild-und-die-bilanz-der-dimensionen.html#satz-3-5) (c)), und $L_A^{-1}$ ist linear (Satz [4.2](koordinaten-und-darstellungsmatrix.html#satz-4-2)). Ihre Matrix heißt __Inverse__ $A^{-1}$. Aus $L_A\circ L_A^{-1}=L_A^{-1}\circ L_A=\operatorname{Id}$ folgt $AA^{-1}=A^{-1}A=E_n$. Nach Stufe [2](die-spalten-sind-die-bilder.html#stufe-2) ist die $j$-te Spalte von $A^{-1}$ das Bild von $e_j$ unter $L_A^{-1}$, also die Lösung von $Ax=e_j$. Das sind $n$ Gleichungssysteme mit derselben linken Seite. Man löst sie zusammen:

<span class="anker" id="gl-8-1"></span>
$$(A\,|\,E_n)\iff\dots\iff(E_n\,|\,A^{-1}). \tag{8.1}$$

Dafür bringt man $A$ durch Vorwärtselimination in __obere Dreiecksform__ (unter der Hauptdiagonale nur Nullen, auf ihr Pivots $\ne0$), erzeugt von unten nach oben Nullen über den Pivots und teilt zuletzt durch die Pivots. Dann ist links $E_n$ erreicht, und rechts stehen die Lösungen. Für eine einzelne rechte Seite ergibt das $(A\,|\,b)\iff(E_n\,|\,z)$, und $z$ ist die Lösung.

::::beispiel
Für $H$ rechnet man $Z_2-2Z_1$, $Z_3-Z_1$, $Z_3-2Z_2$, dann $Z_2-Z_3$, $Z_1-Z_3$, zuletzt $Z_1-Z_2$ und $\frac12Z_1$:

$$\left(\begin{array}{ccc|ccc}2&1&1&1&0&0\\4&3&3&0&1&0\\2&3&4&0&0&1\end{array}\right)\iff\left(\begin{array}{ccc|ccc}2&1&1&1&0&0\\0&1&1&-2&1&0\\0&0&1&3&-2&1\end{array}\right)\iff\left(\begin{array}{ccc|ccc}1&0&0&\frac32&-\frac12&0\\0&1&0&-5&3&-1\\0&0&1&3&-2&1\end{array}\right).$$

Probe: $H^{-1}(3,7,4)=(\frac92-\frac72,\ -15+21-4,\ 9-14+4)=(1,2,-1)$.
::::

⁠**Grenzfall:** Für $\operatorname{rg}(A)<n$ entsteht links eine Nullzeile, und das Verfahren bricht ab. So zeigt sich, dass die Inverse fehlt, etwa bei $P$: Dort ergibt $Z_2-2Z_1$ die Zeile $(0,0)$.

:::frage Bekomme ich die Inverse, wenn ich jeden Eintrag durch seinen Kehrwert ersetze?
Nein. $A^{-1}$ macht die Abbildung rückgängig, nicht die Einträge, denn das Produkt rechnet „Zeile mal Spalte“ und nicht Eintrag mal Eintrag. Bei $H$ steht in Zeile 2, Spalte 1 eine 4, in $H^{-1}$ steht dort $-5$.
:::

:::aufgabe Aufgabe 12 ★★ Rang und Inverse
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Bestimme den Rang von $\begin{pmatrix}2&1&0&3\\4&2&1&7\\2&1&1&4\end{pmatrix}$. Welche Spalten sind Pivotspalten? Welche Zeile lässt sich aus den beiden anderen bauen?

</li>

<li>

Sage $D^{-1}$ und $S^{-1}$ aus der Geometrie vorher und prüfe mit dem Produkt.

</li>

<li>

Berechne die Inverse von $J=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}$ und löse damit $Jx=(2,4,6)$.

</li>

</ol>

:::loesung
(a) $Z_2-2Z_1$ und $Z_3-Z_1$ ergeben beide $(0,0,1,1)$, $Z_3-Z_2$ eine Nullzeile. Also $r=2$, Pivotspalten 1 und 3. Es gilt $Z_2=Z_1+Z_3$. (b) Rückwärts drehen und rückwärts scheren: $D^{-1}=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$, $S^{-1}=\bigl(\begin{smallmatrix}1&-1\\0&1\end{smallmatrix}\bigr)$. Beide Produkte ergeben $E_2$. (c) $J^{-1}=\dfrac12\begin{pmatrix}1&-1&1\\1&1&-1\\-1&1&1\end{pmatrix}$ und $x=J^{-1}(2,4,6)=(2,0,4)$. Probe: $J(2,0,4)=(2,4,6)$.
:::
:::
