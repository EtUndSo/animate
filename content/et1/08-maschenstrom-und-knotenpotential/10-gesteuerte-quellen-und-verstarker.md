---
title: Stufe 8: Gesteuerte Quellen und Verstärker
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1181000
summary: Verstärker enthalten gesteuerte Quellen (Kapitel 6).
tags: spannungsgesteuerte Stromquelle, Steilheit, Spannungsverstärkung, Gegenkopplung, Transimpedanz
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Verstärker enthalten gesteuerte Quellen ([Kapitel 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)). Diese Stufe gibt ihnen einen Stempel und zeigt, was das für die Matrix bedeutet.
:::

**Die Idee.** Eine __spannungsgesteuerte Stromquelle__ ([Kapitel 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)) ist ein verallgemeinerter Leitwert. Bei einem Leitwert steuert die eigene Spannung $U_{ik}$ den Strom von $i$ nach $k$. Bei der Quelle steuert eine fremde Spannung $U_{pq}$. Die Zeilen bleiben, weil der Strom an denselben Knoten ab- und zufließt. Die Spalten wandern von $i$, $k$ nach $p$, $q$, weil sie die steuernden Potenziale zählen. Die Symmetrie geht dabei verloren. Das ist Physik: Der Eingang wirkt auf den Ausgang, aber nicht umgekehrt.

:::satz Satz 8.1 (Stempel der spannungsgesteuerten Stromquelle)
<span class="anker" id="satz-8-1"></span>

Eine Quelle mit $I=g\,(U_p-U_q)$ von $i$ nach $k$ addiert $+g$ auf $(i,p)$ und $(k,q)$ und $-g$ auf $(i,q)$ und $(k,p)$.
:::

⁠**So liest man das:** $g$ ist die __Steilheit__, Strom je Steuerspannung in Siemens, im Modell 50 mS. **Gültigkeit:** Die Quelle soll linear sein. Transistoren sind es nur für kleine Änderungen um einen Arbeitspunkt ([Kapitel 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).

::::beispiel ohne Gegenkopplung
Eine Stromquelle $I_\mathrm q=20$ µ A mit $G_\mathrm q=0{,}5$ mS speist Knoten 1. Dort liegt $G_\mathrm i=0{,}5$ mS nach Masse. Die Quelle $g\,U_1$ zieht Strom aus Knoten 2 in die Masse, dort hängen auch $G_\mathrm o=0{,}05$ mS und $G_\mathrm L=0{,}2$ mS. Die Stempel ergeben

<span class="anker" id="gl-8-1"></span>
$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0\\g&G_\mathrm o+G_\mathrm L\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\end{pmatrix}. \tag{8.1}$$

$Y_{12}=0$, aber $Y_{21}=g$. Mit $D=(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)$, $D_1=(G_\mathrm o+G_\mathrm L)\,I_\mathrm q$ und $D_2=-g\,I_\mathrm q$ wird

<span class="anker" id="gl-8-2"></span>
$$U_1=\frac{I_\mathrm q}{G_\mathrm q+G_\mathrm i},\qquad U_2=-\frac{g\,I_\mathrm q}{(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)},\qquad A_u=\frac{U_2}{U_1}=-\frac{g}{G_\mathrm o+G_\mathrm L}. \tag{8.2}$$

Im Modell sind $D=0{,}25$, $U_1=20$ mV, $U_2=-4$ V und die __Spannungsverstärkung__ $A_u=-200$, wie in [Kapitel 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html). Das Minus entsteht, weil der gesteuerte Strom aus Knoten 2 herausfließt.
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
Weil sie dann kaum noch von der Steilheit abhängt, und $g$ schwankt bei Transistoren stark. Verdoppelt man im Modell $g$, geht $A_u$ von $-4{,}81$ nur auf $-4{,}90$. Ohne $R_\mathrm S$ würde aus $-200$ dagegen $-400$. Das Ergebnis liegt nahe bei $-R_\mathrm L/R_\mathrm S=-5$, also bei zwei genauen Widerständen. [Kapitel 11](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html) nutzt das beim Operationsverstärker.
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

::::formelsammlung
**Stempel der spannungsgesteuerten Stromquelle**

$$I=g\,(U_p-U_q)$$

Quelle von $i$ nach $k$, gesteuert von der Spannung zwischen $p$ und $q$. Sie addiert $+g$ auf $(i,p)$ und $(k,q)$ und $-g$ auf $(i,q)$ und $(k,p)$; die Matrix wird dadurch unsymmetrisch. $g$ ist die Steilheit in Siemens. Gilt für lineare Quellen, bei Transistoren nur für kleine Änderungen um einen Arbeitspunkt.

**Verstärker ohne Gegenkopplung**

$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0\\g&G_\mathrm o+G_\mathrm L\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\end{pmatrix}$$

Die Stromquelle $I_\mathrm q$ mit $G_\mathrm q$ speist Knoten 1, dort liegt $G_\mathrm i$ nach Masse. Die Quelle $g\,U_1$ zieht Strom aus Knoten 2 in die Masse, dort hängen auch $G_\mathrm o$ und $G_\mathrm L$. $Y_{12}=0$, aber $Y_{21}=g$.

**Spannungsverstärkung ohne Gegenkopplung**

$$U_1=\frac{I_\mathrm q}{G_\mathrm q+G_\mathrm i},\qquad U_2=-\frac{g\,I_\mathrm q}{(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)},\qquad A_u=\frac{U_2}{U_1}=-\frac{g}{G_\mathrm o+G_\mathrm L}$$

Das Minus entsteht, weil der gesteuerte Strom aus Knoten 2 herausfließt.

**Verstärker mit Gegenkopplung**

$$\begin{pmatrix}G_\mathrm q+G_\mathrm i&0&-G_\mathrm i\\g&G_\mathrm o+G_\mathrm L&-g-G_\mathrm o\\-g-G_\mathrm i&-G_\mathrm o&G_\mathrm S+g+G_\mathrm i+G_\mathrm o\end{pmatrix} \begin{pmatrix}U_1\\U_2\\U_3\end{pmatrix}=\begin{pmatrix}I_\mathrm q\\0\\0\end{pmatrix}$$

Zwischen dem Fußpunkt (Knoten 3) und Masse liegt $R_\mathrm S$ mit dem Leitwert $G_\mathrm S$. Die Quelle $g\,(U_1-U_3)$ führt von Knoten 2 nach Knoten 3, $G_\mathrm i$ und $G_\mathrm o$ enden an Knoten 3.

**Transimpedanz mit Gegenkopplung**

$$\frac{U_2}{I_\mathrm q}=\frac{G_\mathrm iG_\mathrm o-g\,G_\mathrm S}{(G_\mathrm o+G_\mathrm L)\,[(G_\mathrm q+G_\mathrm i)\,G_\mathrm S+G_\mathrm qG_\mathrm i]+G_\mathrm L\,[(G_\mathrm q+G_\mathrm i)\,G_\mathrm o+G_\mathrm q\,g]}$$

Ausgangsspannung je Eingangsstrom. Für $G_\mathrm S\to\infty$ bleiben nur die Glieder mit $G_\mathrm S$, und sie geht in $-g/[(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)]$ über, das Ergebnis ohne Gegenkopplung. Mit Gegenkopplung hängt die Verstärkung kaum noch von $g$ ab und liegt im Modell nahe bei $-R_\mathrm L/R_\mathrm S$.
::::

::::lernkarten
:::karte begriff spannungsgesteuerte Stromquelle
Was ist eine spannungsgesteuerte Stromquelle, und warum kann man sie als verallgemeinerten Leitwert auffassen?
---
Eine Stromquelle, deren Strom von einer Spannung an anderer Stelle des Netzes abhängt, $I=g\,(U_p-U_q)$ von $i$ nach $k$. Bei einem Leitwert steuert die eigene Spannung $U_{ik}$ den Strom, bei dieser Quelle eine fremde Spannung $U_{pq}$.
--- falsch
Eine Stromquelle, deren Strom von ihrer eigenen Klemmenspannung abhängt, $I=g\,(U_i-U_k)$ von $i$ nach $k$. Sie ist ein gewöhnlicher Leitwert, nur mit dem Formelzeichen $g$ statt $G$ und mit größerem Wert.
--- falsch
Eine Spannungsquelle, deren Spannung von einem Strom an anderer Stelle des Netzes abhängt, $U=g\,I_{pq}$. Sie ist ein verallgemeinerter Widerstand, weil sie einen Strom in eine Spannung umsetzt.
--- falsch
Eine Stromquelle, deren Strom fest ist, solange überhaupt eine Steuerspannung anliegt. Sie ist ein verallgemeinerter Leitwert, weil ihr Strom wie bei einem Leitwert von ihren beiden Klemmen und deren Potenzialen abhängt.
:::
:::karte formel Stempel der spannungsgesteuerten Stromquelle
Welche Einträge addiert eine Quelle mit $I=g\,(U_p-U_q)$, die von Knoten $i$ nach Knoten $k$ treibt, in die Knotenmatrix?
---
$+g$ auf $(i,p)$ und $(k,q)$, $-g$ auf $(i,q)$ und $(k,p)$. Die Zeilen bleiben bei $i$ und $k$, weil der Strom dort ab- und zufließt. Die Spalten wandern nach $p$ und $q$, weil sie die steuernden Potenziale zählen.
--- falsch
$+g$ auf $(i,i)$ und $(k,k)$, $-g$ auf $(i,k)$ und $(k,i)$, genau wie bei einem Leitwert. Die steuernden Knoten $p$ und $q$ kommen nicht vor, weil die Quelle dort keinen Strom ab- oder zuführt, sondern nur die Spannung abgreift.
--- falsch
$+g$ auf $(p,i)$ und $(q,k)$, $-g$ auf $(q,i)$ und $(p,k)$. Die Zeilen wandern nach $p$ und $q$, weil dort gesteuert wird. Die Spalten bleiben bei $i$ und $k$, weil dort der Strom fließt.
--- falsch
$+g$ auf $(i,p)$ und $(k,q)$, $-g$ auf $(i,q)$ und $(k,p)$, dazu dieselben Einträge gespiegelt auf $(p,i)$, $(q,k)$, $(q,i)$ und $(p,k)$, damit die Matrix symmetrisch bleibt.
:::
:::karte zusammenhang Gesteuerte Quellen brechen die Symmetrie
Warum ist die Knotenmatrix einer Schaltung mit gesteuerter Quelle nicht mehr symmetrisch?
---
Weil die Quelle in den Zeilen ihrer Ausgangsknoten, aber in den Spalten der steuernden Knoten einträgt, und das Spiegelbild fehlt. Das ist Physik: Der Eingang wirkt auf den Ausgang, aber nicht umgekehrt.
--- falsch
Weil die Steilheit $g$ viel größer ist als die übrigen Leitwerte. Die großen Einträge verschieben das Gleichgewicht der Matrix zur Ausgangsseite hin, Ein- und Ausgang wirken dabei aber gleich stark aufeinander.
--- falsch
Weil gesteuerte Quellen negative Leitwerte haben. Ein negativer Eintrag auf der Diagonale macht die Matrix unsymmetrisch, obwohl Ein- und Ausgang gleich stark gekoppelt sind.
--- falsch
Weil gesteuerte Quellen den Bezugsknoten verschieben. Seine Zeile lässt sich dann nicht mehr streichen, und die Matrix verliert dadurch ihre Symmetrie.
:::
:::karte begriff Steilheit
Was gibt die Steilheit $g$ einer spannungsgesteuerten Stromquelle an, und in welcher Einheit misst man sie?
---
Den Strom je Steuerspannung, in Siemens, im Verstärkermodell 50 mS. Bei Transistoren gilt dieses lineare Modell nur für kleine Änderungen um einen Arbeitspunkt.
--- falsch
Die Spannung je Steuerstrom, in Ohm, im Verstärkermodell 50 k$\Omega$. Bei Transistoren gilt dieses lineare Modell für jede Aussteuerung, weil die Quelle linear ist.
--- falsch
Das Verhältnis von Ausgangs- zu Eingangsspannung, ohne Einheit, im Verstärkermodell 50. Bei Transistoren gilt das nur für kleine Änderungen um einen Arbeitspunkt.
--- falsch
Den Strom je Steuerspannung, in Siemens, im Verstärkermodell 50 mS. Bei Transistoren ist $g$ eine sehr genaue Größe, deshalb bestimmt sie die Verstärkung zuverlässig.
:::
:::karte begriff Spannungsverstärkung
Was gibt die Spannungsverstärkung eines Verstärkers an, und warum ist sie im Verstärkermodell negativ?
---
Das Verhältnis von Ausgangs- zu Eingangsspannung, $A_u=\frac{U_2}{U_1}$. Sie ist negativ, weil der gesteuerte Strom aus dem Ausgangsknoten 2 herausfließt und dessen Potenzial deshalb unter die Masse senkt.
--- falsch
Das Verhältnis von Ausgangs- zu Eingangsspannung, $A_u=\frac{U_2}{U_1}$. Sie ist negativ, weil am Eingang eine Stromquelle statt einer Spannungsquelle speist und den Eingang umpolt.
--- falsch
Das Verhältnis von Ausgangsstrom zu Eingangsstrom. Sie ist negativ, weil der Ausgangsstrom gegen die Zählrichtung des Eingangsstroms gezählt wird, also nur wegen der Wahl der Pfeile am Ausgang.
--- falsch
Das Verhältnis von Ausgangs- zu Eingangsspannung, $A_u=\frac{U_2}{U_1}$. Sie ist negativ, weil die Last am Ausgang Leistung aufnimmt und die Spannung dabei ihr Vorzeichen wechselt.
:::
:::karte formel Verstärker ohne Gegenkopplung
Welche Spannungsverstärkung hat der Verstärker ohne Gegenkopplung, wenn die Quelle $g\,U_1$ Strom aus Knoten 2 in die Masse zieht und dort $G_\mathrm o$ und $G_\mathrm L$ hängen?
---
$A_u=\frac{U_2}{U_1}=-\frac{g}{G_\mathrm o+G_\mathrm L}$. Mit $g=50$ mS, $G_\mathrm o=0{,}05$ mS und $G_\mathrm L=0{,}2$ mS ist $A_u=-200$. In der Matrix ist dabei $Y_{12}=0$, aber $Y_{21}=g$.
--- falsch
$A_u=\frac{U_2}{U_1}=-\frac{g}{G_\mathrm q+G_\mathrm i}$, weil die Eingangsleitwerte bestimmen, wie viel Steuerspannung entsteht. Mit den Werten des Modells ist $A_u=-50$. In der Matrix ist $Y_{12}=Y_{21}=g$.
--- falsch
$A_u=\frac{U_2}{U_1}=-g\,(G_\mathrm o+G_\mathrm L)$. Mit $g=50$ mS, $G_\mathrm o=0{,}05$ mS und $G_\mathrm L=0{,}2$ mS ist $A_u=-12{,}5$. In der Matrix ist dabei $Y_{12}=g$, aber $Y_{21}=0$.
--- falsch
$A_u=\frac{U_2}{U_1}=+\frac{g}{G_\mathrm o+G_\mathrm L}$. Mit $g=50$ mS, $G_\mathrm o=0{,}05$ mS und $G_\mathrm L=0{,}2$ mS ist $A_u=+200$. In der Matrix ist dabei $Y_{12}=0$, aber $Y_{21}=g$.
:::
:::karte begriff Gegenkopplung
Was versteht man unter Gegenkopplung, und wie entsteht sie im Verstärker mit dem Widerstand $R_\mathrm S$ am Fußpunkt?
---
Die Rückwirkung des Ausgangs auf den eigenen Eingang. Der Ausgangsstrom läuft durch $R_\mathrm S$ und hebt $U_3$ an. Dadurch sinkt die Steuerspannung $U_1-U_3$, und der Ausgangsstrom wird kleiner.
--- falsch
Die Rückwirkung des Ausgangs auf den eigenen Eingang. Der Ausgangsstrom läuft durch $R_\mathrm S$ und senkt $U_3$ ab. Dadurch steigt die Steuerspannung $U_1-U_3$, und der Ausgangsstrom wird größer.
--- falsch
Die Kopplung zweier Verstärker, deren Ausgänge gegeneinander geschaltet sind. Der Widerstand $R_\mathrm S$ begrenzt den Strom zwischen ihnen, damit sich die Ausgänge nicht kurzschließen.
--- falsch
Die Wirkung der Last auf den Ausgang: $R_\mathrm S$ liegt parallel zur Last und senkt so die Ausgangsspannung. Die Steuerspannung $U_1-U_3$ bleibt dabei unverändert.
:::
:::karte begriff Transimpedanz
Was gibt die Transimpedanz eines Verstärkers an, der von einer Stromquelle gespeist wird?
---
Die Ausgangsspannung je Eingangsstrom, $U_2/I_\mathrm q$, in Ohm. Im Verstärkermodell ist sie mit Gegenkopplung $-9{,}39\,\mathrm{k\Omega}$, ohne Gegenkopplung $-200\,\mathrm{k\Omega}$.
--- falsch
Die Ausgangsspannung je Eingangsspannung, $U_2/U_1$, ohne Einheit. Im Verstärkermodell ist sie mit Gegenkopplung $-4{,}81$, ohne Gegenkopplung $-200$.
--- falsch
Den Ausgangsstrom je Eingangsspannung, in Siemens. Im Verstärkermodell ist sie mit und ohne Gegenkopplung 50 mS, weil die Steilheit gleich bleibt.
--- falsch
Den Widerstand, den der Verstärker der speisenden Stromquelle bietet, $U_1/I_\mathrm q$, in Ohm. Im Verstärkermodell ist er mit Gegenkopplung rund 2 k$\Omega$.
:::
:::karte herleitung Transimpedanz mit Gegenkopplung
Leite aus der Knotenmatrix des Verstärkers mit Gegenkopplung die Transimpedanz $U_2/I_\mathrm q$ mit der cramerschen Regel her.
---
Nach der cramerschen Regel ist $U_2$ der Quotient aus $D_2$ und $D$, weil $U_2$ die zweite Unbekannte ist. $D_2$ entsteht, wenn man Spalte 2 durch die rechte Seite ersetzt, in der nur $I_\mathrm q$ steht.
---
$D_2$ entwickelt man nach Spalte 2, weil dort nur $I_\mathrm q$ steht. Es ergibt sich $D_2=(G_\mathrm iG_\mathrm o-g\,G_\mathrm S)\,I_\mathrm q$.
---
$D$ entwickelt man nach der ersten Zeile, weil dort eine Null steht. Mit $A=G_\mathrm q+G_\mathrm i$ und $B=G_\mathrm o+G_\mathrm L$ folgt $D=B\,[A\,G_\mathrm S+G_\mathrm qG_\mathrm i]+G_\mathrm L\,[A\,G_\mathrm o+G_\mathrm q\,g]$.
---
Teilt man $D_2$ durch $D$ und durch $I_\mathrm q$, entsteht die Transimpedanz, weil $D_2$ den Faktor $I_\mathrm q$ enthält und $D$ nicht von der Quelle abhängt. Im Zähler steht $G_\mathrm iG_\mathrm o-g\,G_\mathrm S$, im Nenner $D$ mit eingesetztem $A$ und $B$.
:::
:::karte zusammenhang Grenzfall großer Leitwert am Fußpunkt
Was wird aus dem Verstärker mit Gegenkopplung, wenn $G_\mathrm S\to\infty$ geht?
---
Der Fußpunkt liegt dann wieder auf Masse. In der Transimpedanz bleiben nur die Glieder mit $G_\mathrm S$, und sie geht in $-g/[(G_\mathrm q+G_\mathrm i)(G_\mathrm o+G_\mathrm L)]=-200\,\mathrm{k\Omega}$ über, das Ergebnis ohne Gegenkopplung.
--- falsch
Dann fließt der ganze Ausgangsstrom durch $R_\mathrm S$, und die Gegenkopplung wird so stark wie möglich. Die Transimpedanz geht gegen null, weil die Steuerspannung $U_1-U_3$ ganz verschwindet.
--- falsch
Dann ist Knoten 3 vom übrigen Netz getrennt, und der Ausgangsstrom kann nicht mehr fließen. Die Transimpedanz geht gegen null, weil die gesteuerte Quelle keinen Strom mehr treiben kann.
--- falsch
Der Fußpunkt liegt dann wieder auf Masse. Die Transimpedanz wächst aber über alle Grenzen, weil der Ausgang ohne Widerstand am Fußpunkt keinen Strom mehr begrenzt.
:::
:::karte zusammenhang Verstärkung freiwillig verringern
Warum verringert man die Verstärkung eines Verstärkers freiwillig durch Gegenkopplung?
---
Weil sie dann kaum noch von der Steilheit abhängt, die bei Transistoren stark schwankt. Verdoppelt man im Modell $g$, geht $A_u$ nur von $-4{,}81$ auf $-4{,}90$. Das Ergebnis liegt nahe bei $-R_\mathrm L/R_\mathrm S=-5$.
--- falsch
Weil eine hohe Verstärkung den Transistor überlastet. Mit Gegenkopplung fließt weniger Ausgangsstrom, die Steilheit $g$ bleibt dadurch konstant, und die Verstärkung ist dann unabhängig von der Last genau $-g\,R_\mathrm L$.
--- falsch
Weil die Ausgangsspannung sonst ihr Vorzeichen wechselt. Ohne $R_\mathrm S$ ist $A_u$ negativ, mit Gegenkopplung wird sie positiv, und das Signal kommt mit derselben Polung am Ausgang an.
--- falsch
Weil sie dann stärker von der Steilheit abhängt und sich durch die Wahl des Transistors genau einstellen lässt. Verdoppelt man im Modell $g$, verdoppelt sich mit Gegenkopplung auch $A_u$.
:::
:::karte zusammenhang Eingangswiderstand mit Gegenkopplung
Warum steigt der Eingangswiderstand des Verstärkers, wenn man am Fußpunkt den Widerstand $R_\mathrm S$ einfügt?
---
Weil das Potenzial $U_3$ am anderen Ende von $R_\mathrm i$ fast mitläuft. An $R_\mathrm i$ liegt deshalb nur knapp 1 mV, und es fließt wenig Strom. Wenig Strom bei gleicher Spannung heißt großer Eingangswiderstand.
--- falsch
Weil $R_\mathrm S$ in Reihe zu $R_\mathrm i$ liegt und sich die beiden Widerstände einfach addieren. Mit $R_\mathrm S=1\,\mathrm{k\Omega}$ steigt der Eingangswiderstand deshalb von 2 k$\Omega$ auf 3 k$\Omega$.
--- falsch
Weil die Gegenkopplung den Ausgangsstrom verkleinert und so weniger Strom über $R_\mathrm o$ zum Eingang zurückfließt. Der Eingang wird dadurch entlastet, und sein Widerstand verdoppelt sich etwa.
--- falsch
Weil das Potenzial $U_3$ durch den Ausgangsstrom unter die Masse sinkt. Die speisende Quelle muss dann gegen eine größere Spannung anarbeiten, und ein Eingang, der mehr Spannung verlangt, wirkt wie ein großer Widerstand.
:::
::::
