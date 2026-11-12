---
title: Stufe 5: Das Knotenpotentialverfahren
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1180700
summary: Die Maschenregel ist erledigt, k-1 Knotenregeln mit k-1 Unbekannten bleiben.
tags: Koppelleitwert
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Die Maschenregel ist erledigt, $k-1$ Knotenregeln mit $k-1$ Unbekannten bleiben. Diese Stufe stellt sie auf und löst dasselbe Netz ein zweites Mal.
:::

**Die Idee.** Der Strom, der über einen Leitwert $G$ vom Knoten $\mu$ zum Nachbarn $\nu$ abfließt, ist $G\,(U_\mu-U_\nu)$. Addiert man alle abfließenden Ströme eines Knotens und ordnet nach Potenzialen, steht vor dem eigenen Potenzial die Summe aller Leitwerte am Knoten. Vor einem fremden Potenzial steht nur der Leitwert zum eigenen Knoten, mit Minus: Hebt man den Nachbarn an, fließt weniger ab. Abb. [5](#abb-5) zeigt das als Versuch.

:::definition Definition 5.1 (Knotenpotentialverfahren)
<span class="anker" id="satz-5-1"></span>

Das Verfahren hat vier Schritte:

<ol>

<li>

Reale Spannungsquellen in reale Stromquellen umwandeln: $I_\mathrm q=U_\mathrm q/R$, derselbe Widerstand parallel ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)).

</li>

<li>

Einen Bezugsknoten festlegen, die Potenziale der übrigen Knoten als Spannungen gegen ihn eintragen. Widerstände als Leitwerte schreiben.

</li>

<li>

Für die $k-1$ übrigen Knoten die Knotenregel aufstellen oder die Matrix direkt ablesen.

</li>

<li>

Das System nach den Knotenpotentialen lösen, daraus Zweigspannungen und Zweigströme berechnen.

</li>

</ol>
:::

:::satz Satz 5.2 (Matrixform des Knotenpotentialverfahrens)
<span class="anker" id="satz-5-2"></span>

Mit $n=k-1$ erfüllen die Knotenpotentiale $\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$:

<span class="anker" id="gl-5-1"></span>
$$\begin{pmatrix}Y_{11}&Y_{12}&\dots&Y_{1n}\\Y_{21}&Y_{22}&\dots&Y_{2n}\\\vdots&\vdots&\ddots&\vdots\\Y_{n1}&Y_{n2}&\dots&Y_{nn}\end{pmatrix} \begin{pmatrix}U_1\\U_2\\\vdots\\U_n\end{pmatrix}= \begin{pmatrix}I_\mathrm{q1}\\I_\mathrm{q2}\\\vdots\\I_{\mathrm qn}\end{pmatrix}. \tag{5.1}$$

<ul>

<li>

$Y_{\mu\mu}$ ist die Summe aller Leitwerte, die am Knoten $\mu$ hängen.

</li>

<li>

$Y_{\mu\nu}=Y_{\nu\mu}$ ist der negative __Koppelleitwert__, also minus die Summe der Leitwerte, die direkt zwischen den Knoten $\mu$ und $\nu$ liegen. Ohne direkte Verbindung steht dort null.

</li>

<li>

$I_{\mathrm q\mu}$ ist die Summe der Quellenströme am Knoten, positiv, wenn sie in den Knoten hineinfließen.

</li>

</ul>
:::

:::herleitung Von der Knotenregel zur Matrix
Am Knoten $\mu$ fließt über jeden Leitwert $G_a$ zum Nachbarn $\nu$ der Strom $G_a\,(U_\mu-U_\nu)$ ab, zum Bezugsknoten $G_a\,U_\mu$. Die Summe dieser Ströme ist gleich dem eingespeisten $I_{\mathrm q\mu}$. Ordnen ergibt vor $U_\mu$ die Summe aller $G_a$ und vor $U_\nu$ minus die Summe der Leitwerte zwischen $\mu$ und $\nu$. Knoten $\nu$ erhält denselben Eintrag, denn ein Leitwert kennt keine Richtung. Deshalb ist $\mathbf Y$ symmetrisch.
:::

⁠**So liest man das:** Die Zeile $\mu$ ist die Knotenregel: Links stehen alle über Leitwerte abfließenden Ströme, rechts das, was die Quellen hineinschieben. Die Spalte $\nu$ sagt: Hält man Knoten $\nu$ auf 1 V und alle anderen auf 0 V, muss man an Knoten $\nu$ den Strom $Y_{\nu\nu}$ einspeisen und an jedem Nachbarn $\mu$ den Strom $-Y_{\mu\nu}$ entnehmen. Das ist genau der Kurzschlussversuch aus [Kapitel 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html). **Gültigkeit:** Das Netz enthält Leitwerte und feste Stromquellen. Eine ideale Spannungsquelle passt nicht hinein, sie hat keinen endlichen Leitwert (Stufe [9](die-modifizierte-knotenanalyse.html#stufe-9)).

:::abbildung et1/k8yspalte 5
Links: das Rechenmodell für das Knotenpotentialverfahren, die Batterie ist in eine Stromquelle umgewandelt. Rechts: Die Quellen sind entfernt, Knoten 1 liegt auf 1 V, Knoten 2 auf 0 V. Über $G_1$, $G_2$, $G_3$ fließen $1+0{,}25+0{,}5=1{,}75$ mA ab, das ist $Y_{11}$. Die 0,5 mA kommen an Knoten 2 an und müssen dort entnommen werden, das ist $Y_{21}=-0{,}5$ mS.
:::

::::beispiel
Links wird $I_\mathrm{q1}=U_\mathrm q/R_1=9$ mA mit $G_1=1$ mS parallel. Die Leitwerte sind $G_2=0{,}25$ mS, $G_3=0{,}5$ mS, $G_4=0{,}1$ mS und $G_5=0{,}2$ mS (Abb. [5](#abb-5)). Die Knotenregeln lauten

$$\begin{aligned} \text{Knoten 1:}\quad&(G_1+G_2)\,U_1+G_3\,(U_1-U_2)-I_\mathrm{q1}=0,\\ \text{Knoten 2:}\quad&G_3\,(U_2-U_1)+(G_4+G_5)\,U_2-I_\mathrm q=0. \end{aligned}$$

Geordnet, in mS, V und mA:

$$\begin{pmatrix}G_1+G_2+G_3&-G_3\\-G_3&G_3+G_4+G_5\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}= \begin{pmatrix}1{,}75&-0{,}5\\-0{,}5&0{,}8\end{pmatrix}\begin{pmatrix}U_1\\U_2\end{pmatrix}=\begin{pmatrix}9\\4\end{pmatrix}.$$

Mit $D=1{,}4-0{,}25=1{,}15$, $D_1=7{,}2+2=9{,}2$ und $D_2=7+4{,}5=11{,}5$ folgen $U_1=8$ V und $U_2=10$ V. Das ist dasselbe Ergebnis wie aus den drei Maschen, mit einer $2\times2$- statt einer $3\times3$-Rechnung.

Die Ströme kommen aus den Differenzen, und zwar im *ursprünglichen* Netz: $(U_\mathrm q-U_1)/R_1=1$ mA, $U_1/R_2=2$ mA, $(U_2-U_1)/R_3=1$ mA, $U_2/R_4=1$ mA, $U_2/R_5=2$ mA. **Kontrollen:** An Knoten 2 sind $4=1+1+2$ mA. Die Quellen liefern $9\,\mathrm{V}\cdot1\,\mathrm{mA}+10\,\mathrm{V}\cdot4\,\mathrm{mA}=49$ mW, die Widerstände nehmen $1+16+2+10+20=49$ mW auf.
::::

⁠**Grenzfall:** Für $G_3\to0$ verschwindet die Nebendiagonale, und beide Seiten rechnen getrennt (Aufgabe [7](#aufg-7)).

:::frage In $\mathbf Z$ hängt das Vorzeichen von den Pfeilen ab. Warum steht in $\mathbf Y$ immer ein Minus?
Maschenströme haben eine Richtung, die man wählt, also auch zwei Möglichkeiten im gemeinsamen Zweig. Knotenpotentiale haben keine Richtung, alle zählen zum selben Bezugsknoten. Am Leitwert zwischen zwei Knoten steht deshalb immer die Differenz, und das fremde Potenzial trägt immer ein Minus.
:::

:::frage Nach dem Umwandeln fließen durch $R_5$ im Maschenbild 2 mA nach oben, im Originalnetz 2 mA nach unten. Was stimmt?
Das Originalnetz. Ersatzquellen stimmen nur an den Klemmen ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). An Knoten 2 und an der Masse liefern beide Formen dasselbe, im Inneren der Quelle bedeutet der Strom Verschiedenes. Innere Größen rechnet man deshalb im ursprünglichen Netz aus den Klemmenspannungen.
:::

:::aufgabe Aufgabe 6 ★★ Drei Knoten und ein Bezug
<span class="anker" id="aufg-6"></span>

Ein Netz hat die Knoten 0 (Bezug), 1, 2, 3. Widerstände: 1 k$\Omega$ von 1 nach 0, 1 k$\Omega$ von 1 nach 2, 500 $\Omega$ von 2 nach 0, 1 k$\Omega$ von 2 nach 3, 1 k$\Omega$ von 3 nach 0. Stromquellen schieben 6 mA in Knoten 1 und 3 mA in Knoten 2.

<ol class="al">

<li>

Lies $\mathbf Y$ und $\mathbf I_\mathrm q$ ab. Warum ist $Y_{13}=0$?

</li>

<li>

Berechne die Knotenpotentiale mit der cramerschen Regel.

</li>

<li>

Berechne alle Widerstandsströme und mache die Probe an Knoten 2.

</li>

<li>

Wie viele Maschenströme braucht man nach dem Umwandeln der beiden Quellen? Welches Verfahren wäre hier kürzer?

</li>

</ol>

:::loesung
(a) Mit 1 mS, 1 mS, 2 mS, 1 mS, 1 mS:

$$\mathbf Y=\begin{pmatrix}2&-1&0\\-1&4&-1\\0&-1&2\end{pmatrix}\mathrm{mS},\qquad\mathbf I_\mathrm q=\begin{pmatrix}6\\3\\0\end{pmatrix}\mathrm{mA}.$$

$Y_{13}=0$, weil zwischen 1 und 3 kein Widerstand liegt.

(b) $D=2\cdot7+1\cdot(-2)=12$, $D_1=48$, $D_2=24$, $D_3=12$. Also $U_1=4$ V, $U_2=2$ V, $U_3=1$ V.

(c) $I_{10}=4$ mA, $I_{12}=2$ mA, $I_{20}=4$ mA, $I_{23}=1$ mA, $I_{30}=1$ mA. Knoten 2: $3+2=4+1$ mA.

(d) Jede Stromquelle wird mit ihrem Parallelwiderstand ein Zweig. Dann sind $z=5$ und $k=4$, also $m=2$ gegen $k-1=3$. Das Maschenstromverfahren wäre mit zwei Gleichungen kürzer. Knoten 3 ist in Wahrheit kein Knoten, sondern eine Reihenschaltung.
:::
:::

:::aufgabe Aufgabe 7 ★★ Grenzfälle am Koppelleitwert
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

$R_3$ im Rechenmodell wird entfernt ($G_3=0$). Was wird aus $\mathbf Y$? Berechne $U_1$ und $U_2$.

</li>

<li>

Vorhersage: $R_3$ wird durch einen Draht ersetzt. Warum geht das in $\mathbf Y$ nicht direkt? Fasse die Knoten zusammen und bestimme die gemeinsame Spannung und den Strom im Draht.

</li>

</ol>

:::loesung
(a) Die Nebendiagonale wird null, die Gleichungen entkoppeln: $U_1=9\,\mathrm{mA}/1{,}25\,\mathrm{mS}=7{,}2$ V und $U_2=4\,\mathrm{mA}/0{,}3\,\mathrm{mS}=13{,}3$ V. Das sind zwei getrennte Netze.

(b) $G_3\to\infty$ lässt sich nicht als Zahl eintragen. Der Draht macht aus beiden Knoten einen: $U=(9+4)\,\mathrm{mA}/(1+0{,}25+0{,}1+0{,}2)\,\mathrm{mS}=8{,}39$ V. Der Strom im Draht folgt aus Knoten 2: $4\,\mathrm{mA}-0{,}3\,\mathrm{mS}\cdot8{,}39\,\mathrm{V}=1{,}48$ mA von 2 nach 1. Stufe [9](die-modifizierte-knotenanalyse.html#stufe-9) löst dieselbe Lage mit einer 0-V-Quelle.
:::
:::

::::formelsammlung
**Umwandeln einer realen Spannungsquelle**

$$I_\mathrm q=U_\mathrm q/R$$

Derselbe Widerstand $R$ liegt danach parallel. Erster Schritt des Knotenpotentialverfahrens.

**Strom über einen Leitwert**

$$G_a\,(U_\mu-U_\nu)$$

Strom, der am Knoten $\mu$ über den Leitwert $G_a$ zum Nachbarn $\nu$ abfließt; zum Bezugsknoten fließt $G_a\,U_\mu$ ab.

**Matrixform des Knotenpotentialverfahrens**

$$\begin{pmatrix}Y_{11}&Y_{12}&\dots&Y_{1n}\\Y_{21}&Y_{22}&\dots&Y_{2n}\\\vdots&\vdots&\ddots&\vdots\\Y_{n1}&Y_{n2}&\dots&Y_{nn}\end{pmatrix} \begin{pmatrix}U_1\\U_2\\\vdots\\U_n\end{pmatrix}= \begin{pmatrix}I_\mathrm{q1}\\I_\mathrm{q2}\\\vdots\\I_{\mathrm qn}\end{pmatrix}$$

Kurz $\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$ mit $n=k-1$. $Y_{\mu\mu}$ ist die Summe aller Leitwerte, die am Knoten $\mu$ hängen. $I_{\mathrm q\mu}$ ist die Summe der Quellenströme am Knoten, positiv, wenn sie hineinfließen. Zeile $\mu$ ist die Knotenregel des Knotens $\mu$, Einheit Siemens. Gilt für Leitwerte und feste Stromquellen; eine ideale Spannungsquelle passt nicht hinein.

**Koppelleitwert**

$$Y_{\mu\nu}=Y_{\nu\mu}$$

Minus die Summe der Leitwerte, die direkt zwischen den Knoten $\mu$ und $\nu$ liegen; ohne direkte Verbindung null. Immer mit Minus, weil alle Knotenpotentiale zum selben Bezugsknoten zählen.
::::

::::lernkarten
:::karte begriff Knotenpotentialverfahren
Was ist das Knotenpotentialverfahren, und in welchen Schritten berechnet man damit ein Netz?
---
Ein Verfahren mit den $k-1$ Knotenpotentialen als Unbekannten, bei dem nur Knotenregeln aufzustellen sind. Schritte: reale Spannungsquellen in Stromquellen umwandeln, Bezugsknoten festlegen, Matrix ablesen, lösen.
--- falsch
Ein Verfahren mit den $k-1$ Knotenpotentialen als Unbekannten, sodass nur Maschenregeln aufzustellen sind. Schritte: reale Stromquellen in Spannungsquellen umwandeln, Bezugsknoten festlegen, Maschenregeln aufstellen, lösen.
--- falsch
Ein Verfahren mit allen $k$ Knotenpotentialen als Unbekannten, auch dem des Bezugsknotens. Schritte: Quellen umwandeln, für jeden der $k$ Knoten eine Knotenregel aufstellen, alle $k$ Gleichungen gemeinsam lösen.
--- falsch
Ein Verfahren mit den Zweigströmen an jedem Knoten als Unbekannten, sodass Knoten- und Maschenregeln nötig sind. Schritte: Bezugsknoten festlegen, Ströme eintragen, alle Regeln aufstellen, lösen.
:::
:::karte formel Matrixform des Knotenpotentialverfahrens
Welche Matrixgleichung erfüllen die $n=k-1$ Knotenpotentiale eines Netzes, und was steht auf der Diagonale, daneben und rechts?
---
$\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$. $Y_{\mu\mu}$ ist die Summe aller Leitwerte am Knoten $\mu$, $Y_{\mu\nu}=Y_{\nu\mu}$ der negative Koppelleitwert, $I_{\mathrm q\mu}$ die Summe der Quellenströme, die in den Knoten hineinfließen. Das gilt für Leitwerte und feste Stromquellen.
--- falsch
$\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$. $Y_{\mu\mu}$ ist die Summe aller Leitwerte am Knoten $\mu$, $Y_{\mu\nu}=Y_{\nu\mu}$ der positive Koppelleitwert, $I_{\mathrm q\mu}$ die Summe der Quellenströme, die aus dem Knoten herausfließen.
--- falsch
$\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$. $Y_{\mu\mu}$ ist der Leitwert vom Knoten $\mu$ zum Bezugsknoten, $Y_{\mu\nu}$ der negative Koppelleitwert, $I_{\mathrm q\mu}$ die Summe der hineinfließenden Quellenströme. Das gilt auch für ideale Spannungsquellen, deren Leitwert man unendlich setzt.
--- falsch
$\mathbf U=\mathbf Y\,\mathbf I_\mathrm q$. $Y_{\mu\mu}$ ist die Summe aller Widerstände am Knoten $\mu$, $Y_{\mu\nu}$ der negative Koppelwiderstand, rechts stehen die Quellenströme. Das gilt für Leitwerte und feste Stromquellen.
:::
:::karte begriff Leitwertmatrix
Was steht in der Leitwertmatrix $\mathbf Y$ des Knotenpotentialverfahrens, und welche Einheit hat sie?
---
Auf der Diagonale die Summe der Leitwerte an einem Knoten, daneben der negative Leitwert zwischen zwei Knoten. Jede Zeile ist die Knotenregel eines Knotens, die Matrix ist symmetrisch, ihre Einheit ist Siemens.
--- falsch
Auf der Diagonale die Summe der Widerstände einer Masche, daneben die gemeinsamen Widerstände zweier Maschen. Jede Zeile ist die Maschenregel einer Masche, ihre Einheit ist Ohm.
--- falsch
Auf der Diagonale die Summe der Leitwerte an einem Knoten, daneben der positive Leitwert zwischen zwei Knoten, weil Leitwerte nie negativ sind. Jede Zeile ist die Knotenregel eines Knotens, ihre Einheit ist Siemens.
--- falsch
Auf der Diagonale nur der Leitwert vom Knoten zum Bezugsknoten, daneben der negative Leitwert zwischen zwei Knoten. Jede Zeile ist eine Knotenregel, ihre Einheit ist Ampere.
:::
:::karte begriff Koppelleitwert
Was ist der Koppelleitwert zweier Knoten, und mit welchem Vorzeichen steht er in der Leitwertmatrix?
---
Die Summe der Leitwerte, die direkt zwischen den Knoten $\mu$ und $\nu$ liegen. In $\mathbf Y$ steht er immer mit Minus, $Y_{\mu\nu}=Y_{\nu\mu}$; ohne direkte Verbindung steht dort null.
--- falsch
Die Summe der Leitwerte, die direkt zwischen den Knoten $\mu$ und $\nu$ liegen. In $\mathbf Y$ steht er mit Plus oder Minus, je nachdem, in welche Richtung man den Strom zwischen den Knoten zählt.
--- falsch
Die Summe aller Leitwerte an beiden Knoten zusammen. In $\mathbf Y$ steht er immer mit Minus, $Y_{\mu\nu}=Y_{\nu\mu}$; ohne direkte Verbindung steht dort der Leitwert über den Bezugsknoten.
--- falsch
Der Leitwert des Wegs zwischen den Knoten $\mu$ und $\nu$ über den Bezugsknoten. In $\mathbf Y$ steht er immer mit Minus; liegen die Knoten direkt nebeneinander, steht dort null.
:::
:::karte formel Umwandeln einer realen Spannungsquelle
Wie bringt man eine reale Spannungsquelle mit der Quellenspannung $U_\mathrm q$ und dem Reihenwiderstand $R$ in eine Form, die das Knotenpotentialverfahren verarbeiten kann?
---
Man wandelt sie in eine reale Stromquelle um: $I_\mathrm q=U_\mathrm q/R$, derselbe Widerstand liegt danach parallel. Im Rechenmodell wird so $I_\mathrm{q1}=U_\mathrm q/R_1=9$ mA mit $G_1=1$ mS parallel.
--- falsch
Man wandelt sie in eine reale Stromquelle um: $I_\mathrm q=U_\mathrm q/R$, derselbe Widerstand bleibt in Reihe zur Stromquelle, weil er auch vorher in Reihe lag. So werden aus 9 V und 1 k$\Omega$ 9 mA.
--- falsch
Man ersetzt sie durch einen Kurzschluss und rechnet nur mit $R$, weil Spannungsquellen in der Leitwertmatrix keinen Platz haben. Die 9 V setzt man am Ende als Knotenpotential ein.
--- falsch
Man wandelt sie in eine ideale Stromquelle um: $I_\mathrm q=U_\mathrm q/R$, den Widerstand lässt man weg, weil er im Quellenstrom schon enthalten ist. So werden aus 9 V und 1 k$\Omega$ 9 mA.
:::
:::karte formel Strom über einen Leitwert
Welcher Strom fließt am Knoten $\mu$ über einen Leitwert $G_a$ zum Nachbarknoten $\nu$ ab, und welcher zum Bezugsknoten?
---
$G_a\,(U_\mu-U_\nu)$ zum Nachbarn und $G_a\,U_\mu$ zum Bezugsknoten. Die Spannung am Leitwert ist die Differenz der Knotenpotentiale, und der Bezugsknoten hat das Potenzial null.
--- falsch
$G_a\,(U_\mu+U_\nu)$ zum Nachbarn und $G_a\,U_\mu$ zum Bezugsknoten. Beide Knotenpotentiale treiben den Strom gemeinsam, weil sie gegen denselben Bezugsknoten zählen und sich deshalb addieren.
--- falsch
$G_a\,(U_\nu-U_\mu)$ zum Nachbarn und $-G_a\,U_\mu$ zum Bezugsknoten. Strom fließt vom niedrigeren zum höheren Potenzial, deshalb zählt das eigene Potenzial negativ.
--- falsch
$(U_\mu-U_\nu)/G_a$ zum Nachbarn und $U_\mu/G_a$ zum Bezugsknoten. Die Spannung am Leitwert ist die Differenz der Knotenpotentiale, geteilt durch den Leitwert.
:::
:::karte herleitung Von der Knotenregel zur Matrix
Leite aus der Knotenregel am Knoten $\mu$ die Einträge der Leitwertmatrix her und zeige, dass $\mathbf Y$ symmetrisch ist.
---
Über jeden Leitwert $G_a$ fließt zum Nachbarn $\nu$ der Strom $G_a\,(U_\mu-U_\nu)$ ab, zum Bezugsknoten $G_a\,U_\mu$, weil die Spannung am Leitwert die Differenz der Knotenpotentiale ist.
---
Die Summe dieser abfließenden Ströme ist gleich dem eingespeisten $I_{\mathrm q\mu}$, weil nach der Knotenregel abfließt, was die Quellen hineinschieben.
---
Ordnet man nach Potenzialen, steht vor $U_\mu$ die Summe aller $G_a$ am Knoten, weil das eigene Potenzial in jedem dieser Ströme vorkommt.
---
Vor $U_\nu$ steht minus die Summe der Leitwerte zwischen $\mu$ und $\nu$, weil das fremde Potenzial nur im Strom über diese Leitwerte vorkommt, und dort mit Minus.
---
Knoten $\nu$ erhält denselben Eintrag, weil ein Leitwert keine Richtung kennt. Deshalb ist $\mathbf Y$ symmetrisch.
:::
:::karte zusammenhang Minus vor dem fremden Potenzial
Warum steht in einer Knotengleichung vor dem Potenzial eines Nachbarknotens ein Minus?
---
Weil über den Leitwert zum Nachbarn der Strom $G\,(U_\mu-U_\nu)$ abfließt. Das fremde Potenzial wirkt also gegen den Abfluss: Hebt man den Nachbarn an, fließt weniger ab.
--- falsch
Weil das Potenzial des Nachbarknotens in umgekehrter Richtung gegen den Bezugsknoten gezählt wird. Sein Pfeil zeigt vom Bezugsknoten zum Nachbarn, also zählt es negativ.
--- falsch
Weil über den Leitwert zum Nachbarn der Strom $G\,(U_\mu-U_\nu)$ abfließt. Hebt man den Nachbarn an, fließt mehr ab, und das Minus gleicht diesen Zuwachs aus.
--- falsch
Weil der Strom vom Nachbarn immer in den Knoten hineinfließt und Zuflüsse auf der linken Seite negativ zählen. Das gilt unabhängig davon, welches Potenzial höher liegt.
:::
:::karte zusammenhang Vorzeichen in Z und Y
Warum hängt das Vorzeichen neben der Diagonale in $\mathbf Z$ von der Wahl der Pfeile ab, während in $\mathbf Y$ immer ein Minus steht?
---
Maschenströme haben eine gewählte Richtung, im gemeinsamen Zweig gibt es also zwei Möglichkeiten. Knotenpotentiale haben keine Richtung, alle zählen zum selben Bezugsknoten, deshalb trägt das fremde Potenzial immer ein Minus.
--- falsch
Weil Leitwerte immer negativ und Widerstände immer positiv sind. In $\mathbf Z$ entscheidet deshalb die Richtung über das Vorzeichen, in $\mathbf Y$ das Vorzeichen des Leitwerts selbst.
--- falsch
Weil in $\mathbf Y$ alle Ströme vom Bezugsknoten wegfließen müssen. Die Richtung ist dort durch die Quellen vorgegeben, in $\mathbf Z$ dagegen frei wählbar, also mit beliebigem Vorzeichen.
--- falsch
Maschenströme haben eine Richtung, die man wählt. Knotenpotentiale haben auch eine, aber man wählt sie stets vom Knoten weg zum Nachbarn, und dann ergibt sich beim Nachbarn jedes Mal ein Minus, gleich wie die Zweige liegen.
:::
:::karte zusammenhang Spalte der Leitwertmatrix
Welchen Versuch beschreibt die Spalte $\nu$ der Leitwertmatrix?
---
Man hält Knoten $\nu$ auf 1 V und alle anderen auf 0 V. Dann muss man an Knoten $\nu$ den Strom $Y_{\nu\nu}$ einspeisen und an jedem Nachbarn $\mu$ den Strom $-Y_{\mu\nu}$ entnehmen. Das ist der Kurzschlussversuch.
--- falsch
Man speist an Knoten $\nu$ den Strom 1 mA ein und lässt alle anderen Knoten offen. Die Spalte gibt dann die Potenziale an, die sich an allen Knoten einstellen. Das ist der Leerlaufversuch.
--- falsch
Man hält Knoten $\nu$ auf 1 V und alle anderen auf 0 V. Dann muss man an Knoten $\nu$ den Strom $Y_{\nu\nu}$ entnehmen und an jedem Nachbarn $\mu$ den Strom $Y_{\mu\nu}$ einspeisen. Das ist der Leerlaufversuch.
--- falsch
Man entfernt Knoten $\nu$ aus dem Netz und misst, wie sich die übrigen Potenziale dadurch ändern. Die Spalte gibt diese Änderungen je Volt an. Das ist der Kurzschlussversuch.
:::
:::karte zusammenhang Ideale Spannungsquelle
Warum passt eine ideale Spannungsquelle nicht in das Gleichungssystem $\mathbf Y\,\mathbf U=\mathbf I_\mathrm q$?
---
Weil sie keinen endlichen Leitwert hat und sich auch nicht in eine Stromquelle umwandeln lässt. Eine reale Spannungsquelle wandelt man vorher in eine Stromquelle mit parallelem Widerstand um.
--- falsch
Weil ihr Leitwert null ist und eine Null auf der Diagonale die Determinante null macht. Man ersetzt sie deshalb durch einen sehr großen Widerstand und rechnet mit diesem Ersatz ganz normal weiter.
--- falsch
Sie passt hinein: Man trägt ihre Spannung $U_\mathrm q$ einfach auf der rechten Seite ein, wie beim Maschenstromverfahren, und rechnet unverändert weiter.
--- falsch
Weil ihr Strom immer null ist und sie deshalb in keiner Knotenregel vorkommt. Man lässt sie weg und setzt ihre Spannung am Ende als Knotenpotential ein.
:::
:::karte zusammenhang Innere Größen im ursprünglichen Netz
Warum berechnet man nach dem Umwandeln einer Quelle den Strom in ihrem Widerstand im ursprünglichen Netz und nicht in der umgewandelten Quelle?
---
Weil Ersatzquellen nur an den Klemmen stimmen. An den Anschlussknoten liefern beide Formen dasselbe, im Inneren der Quelle bedeutet der Strom Verschiedenes. Innere Größen rechnet man deshalb aus den Klemmenspannungen im ursprünglichen Netz.
--- falsch
Weil das Umwandeln die Knotenpotentiale verfälscht. Nach dem Umwandeln stimmen nur die Ströme im Inneren der Quelle, die Klemmenspannungen muss man im ursprünglichen Netz neu berechnen.
--- falsch
Das ist nicht nötig, denn umgewandelte Quellen sind in jeder Hinsicht gleichwertig. Der Strom im Widerstand der Quelle ist in beiden Formen gleich groß und gleich gerichtet, man kann ihn deshalb direkt an der umgewandelten Quelle ablesen.
--- falsch
Weil die umgewandelte Quelle mehr Leistung liefert als die ursprüngliche. Ihr Widerstand führt deshalb einen größeren Strom, den man im ursprünglichen Netz um den Überschuss verkleinern muss.
:::
:::karte zusammenhang Entkoppelte Knoten
Was geschieht mit den Knotengleichungen, wenn man den einzigen Leitwert zwischen zwei Knoten entfernt?
---
Die Einträge neben der Diagonale werden null, und die Gleichungen entkoppeln. Beide Seiten rechnen getrennt wie zwei Netze; im Rechenmodell wird $U_1=9\,\mathrm{mA}/1{,}25\,\mathrm{mS}=7{,}2$ V.
--- falsch
Die Diagonale wird null, weil an den Knoten kein Leitwert mehr hängt, und das System ist nicht mehr lösbar. Man muss die beiden Knoten deshalb zu einem zusammenfassen.
--- falsch
Die Einträge neben der Diagonale werden unendlich, weil der Widerstand zwischen den Knoten unendlich groß ist. Beide Potenziale werden dadurch gleich groß.
--- falsch
Die Einträge neben der Diagonale werden null, aber die Gleichungen bleiben gekoppelt, weil beide Knoten über den Bezugsknoten verbunden sind und sich ihre Ströme teilen.
:::
::::
