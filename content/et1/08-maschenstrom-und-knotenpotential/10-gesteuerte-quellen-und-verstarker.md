---
title: Stufe 8: Gesteuerte Quellen und Verstärker
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Maschenstrom- und Knotenpotentialverfahren
order: 1181000
summary: Verstärker enthalten gesteuerte Quellen (Teil 6).
tags: spannungsgesteuerte Stromquelle, Steilheit, Spannungsverstärkung, Gegenkopplung, Transimpedanz
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Verstärker enthalten gesteuerte Quellen ([Teil 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Diese Stufe gibt ihnen einen Stempel und zeigt, was das für die Matrix bedeutet.
:::

**Die Idee.** Eine __spannungsgesteuerte Stromquelle__ ([Teil 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)) ist ein verallgemeinerter Leitwert. Bei einem Leitwert steuert die eigene Spannung $U_{ik}$ den Strom von $i$ nach $k$. Bei der Quelle steuert eine fremde Spannung $U_{pq}$. Die Zeilen bleiben, weil der Strom an denselben Knoten ab- und zufließt. Die Spalten wandern von $i$, $k$ nach $p$, $q$, weil sie die steuernden Potenziale zählen. Die Symmetrie geht dabei verloren. Das ist Physik: Der Eingang wirkt auf den Ausgang, aber nicht umgekehrt.

:::satz Satz 8.1 (Stempel der spannungsgesteuerten Stromquelle)
<span class="anker" id="satz-8-1"></span>

Eine Quelle mit $I=g\,(U_p-U_q)$ von $i$ nach $k$ addiert $+g$ auf $(i,p)$ und $(k,q)$ und $-g$ auf $(i,q)$ und $(k,p)$.
:::

⁠**So liest man das:** $g$ ist die __Steilheit__, Strom je Steuerspannung in Siemens, im Modell 50 mS. **Gültigkeit:** Die Quelle soll linear sein. Transistoren sind es nur für kleine Änderungen um einen Arbeitspunkt ([Teil 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).

::::beispiel ohne Gegenkopplung
Eine Stromquelle $I_\mathrm q=20$ µ A mit $G_\mathrm q=0{,}5$ mS speist Knoten 1. Dort liegt $G_\mathrm i=0{,}5$ mS nach Masse. Die Quelle $g\,U_1$ zieht Strom aus Knoten 2 in die Masse, dort hängen auch $G_\mathrm o=0{,}05$ mS und $G_\mathrm L=0{,}2$ mS. Die Stempel ergeben

<span class="anker" id="gl-8-1"></span>
$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0\\g&G_\mathrm o+G_\mathrm L\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\end{pmatrix}. \tag{8.1}$$

$Y_{12}=0$, aber $Y_{21}=g$. Mit $D=(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)$, $D_1=(G_\mathrm o+G_\mathrm L)\,I_\mathrm q$ und $D_2=-g\,I_\mathrm q$ wird

<span class="anker" id="gl-8-2"></span>
$$U_1=\frac{I_\mathrm q}{G_\mathrm q+G_\mathrm i},\qquad U_2=-\frac{g\,I_\mathrm q}{(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)},\qquad A_u=\frac{U_2}{U_1}=-\frac{g}{G_\mathrm o+G_\mathrm L}. \tag{8.2}$$

Im Modell sind $D=0{,}25$, $U_1=20$ mV, $U_2=-4$ V und die __Spannungsverstärkung__ $A_u=-200$, wie in [Teil 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html). Das Minus entsteht, weil der gesteuerte Strom aus Knoten 2 herausfließt.
::::

**Mit Gegenkopplung.** Der gemeinsame untere Punkt von Eingang und Ausgang heißt Fußpunkt. Trennt man ihn von der Masse und fügt dort $R_\mathrm S=1\,\mathrm{k\Omega}$ ein, entsteht Knoten 3 (Abb. [8](#abb-8)). Der Ausgangsstrom läuft nun durch $R_\mathrm S$ und hebt $U_3$ an. Dadurch sinkt die Steuerspannung $U_1-U_3$, und der Ausgangsstrom wird kleiner. Diese Rückwirkung des Ausgangs auf den eigenen Eingang heißt __Gegenkopplung__.

:::abbildung et1/k8verstaerker 8
Verstärker mit Gegenkopplung. Die Quelle $g\,(U_1-U_3)$ führt von Knoten 2 nach Knoten 3, $G_\mathrm i$ und $G_\mathrm o$ enden an Knoten 3. Der rote Pfad zeigt den Ausgangsstrom: Er hebt Knoten 3 und verkleinert so die Steuerspannung. Für $G_\mathrm S\to\infty$ fällt Knoten 3 auf die Masse.
:::

Die Stempel von $G_\mathrm q$, $G_\mathrm i$, $G_\mathrm S$, $G_\mathrm o$, $G_\mathrm L$ und $g\,(U_1-U_3)$ von 2 nach 3 ergeben

<span class="anker" id="gl-8-3"></span>
$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0&-G_\mathrm i\\g&G_\mathrm o+G_\mathrm L&-g-G_\mathrm o\\-g-G_\mathrm i&-G_\mathrm o&G_\mathrm S+g+G_\mathrm i+G_\mathrm o\end{pmatrix} \begin{pmatrix}U_1\\U_2\\U_3\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\\0\end{pmatrix}. \tag{8.3}$$

:::herleitung Die Determinanten
Mit $A=G_\mathrm q+G_\mathrm i$ und $B=G_\mathrm o+G_\mathrm L$ liefert die Entwicklung nach der ersten Zeile

$$\begin{aligned} D&=A\,[B\,(G_\mathrm S+G_\mathrm i)+G_\mathrm L\,(g+G_\mathrm o)]-G_\mathrm i\,[B\,G_\mathrm i+G_\mathrm L\,g]\\ &=B\,[A\,G_\mathrm S+G_\mathrm qG_\mathrm i]+G_\mathrm L\,[A\,G_\mathrm o+G_\mathrm q\,g]. \end{aligned}$$

$D_2$ entwickelt man nach Spalte 2, in der nur $I_\mathrm q$ steht: $D_2=-I_\mathrm q\,[g\,(G_\mathrm S+g+G_\mathrm i+G_\mathrm o)-(g+G_\mathrm o)(g+G_\mathrm i)]=(G_\mathrm iG_\mathrm o-g\,G_\mathrm S)\,I_\mathrm q$.
:::

Damit ist die __Transimpedanz__, die Ausgangsspannung je Eingangsstrom,

<span class="anker" id="gl-8-4"></span>
$$\frac{U_2}{I_\mathrm q}=\frac{G_\mathrm iG_\mathrm o-g\,G_\mathrm S}{(G_\mathrm o+G_\mathrm L)\,[(G_\mathrm q+G_\mathrm i)\,G_\mathrm S+G_\mathrm qG_\mathrm i]+G_\mathrm L\,[(G_\mathrm q+G_\mathrm i)\,G_\mathrm o+G_\mathrm q\,g]}. \tag{8.4}$$

Im Modell mit $G_\mathrm S=1$ mS sind $D=5{,}3225$ und $D_2/I_\mathrm q=-49{,}975$, also $U_2/I_\mathrm q=-9{,}39\,\mathrm{k\Omega}$. Aus 20 µ A werden $U_1=39{,}0$ mV, $U_2=-188$ mV und $A_u=-4{,}81$. **Grenzfall:** Für $G_\mathrm S\to\infty$ bleiben nur die Glieder mit $G_\mathrm S$, und [(8.4)](#gl-8-4) geht in $-g/[(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)]=-200\,\mathrm{k\Omega}$ über, das Ergebnis aus [(8.2)](#gl-8-2). Der Fußpunkt liegt dann wieder auf Masse.

:::ltspice Verstärker mit Gegenkopplung
⁠**Zeichnen:** `current` mit `20u` von Masse nach `1`, `Rq 2k` von `1` nach Masse, `Ri 2k` von `1` nach `3`, `RS 1k` von `3` nach Masse. Die gesteuerte Stromquelle `g` mit `50m`: Ausgang von `2` nach `3`, Steuereingang von `1` nach `3`. `Ro 20k` von `2` nach `3`, `RL 5k` von `2` nach Masse.

⁠**Direktiven:** `.op`, `.meas op u1 FIND V(1)`, `.meas op u2 FIND V(2)`, `.meas op au PARAM u2/u1`.

⁠**Was du siehst:** $\mathtt{u1}=39{,}0$ mV, $\mathtt{u2}=-188$ mV, $\mathtt{au}=-4{,}81$. Setze `RS` auf `1u`: Dann sind $\mathtt{u2}=-4$ V und $\mathtt{au}=-200$. Prüfe mit `V(3)` dein Ergebnis aus Aufgabe [10](#aufg-10).
:::

:::frage Warum verringert man die Verstärkung freiwillig?
Weil sie dann kaum noch von der Steilheit abhängt, und $g$ schwankt bei Transistoren stark. Verdoppelt man im Modell $g$, geht $A_u$ von $-4{,}81$ nur auf $-4{,}90$. Ohne $R_\mathrm S$ würde aus $-200$ dagegen $-400$. Das Ergebnis liegt nahe bei $-R_\mathrm L/R_\mathrm S=-5$, also bei zwei genauen Widerständen. [Teil 11](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html) nutzt das beim Operationsverstärker.
:::

:::aufgabe Aufgabe 10 ★★★ Der Eingangswiderstand steigt
<span class="anker" id="aufg-10"></span>

Betrachte den Verstärker aus Abb. [8](#abb-8) mit $G_\mathrm S=1$ mS.

<ol class="al">

<li>

Zeige $D_1=[(G_\mathrm o+G_\mathrm L)(G_\mathrm S+G_\mathrm i)+G_\mathrm L\,(g+G_\mathrm o)]\,I_\mathrm q$ und berechne $U_1/I_\mathrm q$.

</li>

<li>

Der Eingangsleitwert ohne $G_\mathrm q$ ist $Y_\mathrm{ein}=I_\mathrm q/U_1-G_\mathrm q$. Wie groß ist der Eingangswiderstand $1/Y_\mathrm{ein}$? Vergleiche mit 2 k$\Omega$ ohne $R_\mathrm S$.

</li>

<li>

Erkläre den Mechanismus: Wie groß ist $U_3$, und welcher Strom fließt deshalb noch durch $G_\mathrm i$?

</li>

</ol>

:::loesung
(a) Ersetzt man Spalte 1 durch $(I_\mathrm q,0,0)$, bleibt $D_1=I_\mathrm q\,[(G_\mathrm o+G_\mathrm L)(G_\mathrm S+g+G_\mathrm i+G_\mathrm o)-(g+G_\mathrm o)\,G_\mathrm o]$. Ausmultipliziert ist die Klammer die angegebene. Zahlen: $0{,}25\cdot1{,}5+0{,}2\cdot50{,}05=10{,}385$. Mit $D=5{,}3225$ ist $U_1/I_\mathrm q=1{,}95\,\mathrm{k\Omega}$.

(b) $Y_\mathrm{ein}=1/(1{,}951\,\mathrm{k\Omega})-0{,}5\,\mathrm{mS}=0{,}0125$ mS, also $R_\mathrm{ein}=79{,}9\,\mathrm{k\Omega}$, das Vierzigfache.

(c) $U_3=38{,}05$ mV liegt nur 0,98 mV unter $U_1=39{,}02$ mV. Das Potenzial am anderen Ende von $R_\mathrm i$ läuft fast mit. An $R_\mathrm i$ liegen deshalb knapp 1 mV, und statt 10 µ A fließen 0,49 µ A. Wenig Strom bei gleicher Spannung heißt großer Eingangswiderstand.
:::
:::
