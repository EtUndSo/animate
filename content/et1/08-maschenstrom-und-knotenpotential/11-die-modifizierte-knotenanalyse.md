---
title: Stufe 9: Die modifizierte Knotenanalyse
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Maschenstrom- und Knotenpotentialverfahren
order: 1181100
summary: Eine ideale Spannungsquelle hat keinen Leitwert und keine Stromquellenform (Teil 5).
tags: Stromverstärkung, Transitfrequenz
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Eine ideale Spannungsquelle hat keinen Leitwert und keine Stromquellenform ([Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Diese Stufe nimmt die letzte Einschränkung weg. So rechnet SPICE jede Schaltung.
:::

**Die Idee.** Eine Spannungsquelle legt die Spannung zwischen zwei Knoten fest. Ihr Strom stellt sich erst durch das Netz ein, er ist also unbekannt. Man nimmt ihn als zusätzliche Unbekannte. Eine zusätzliche Unbekannte verlangt eine zusätzliche Gleichung, und die liefert die Quelle selbst: Die Potenzialdifferenz ist $U_\mathrm q$. So kehrt je Spannungsquelle genau eine Maschengleichung zurück, alles andere bleibt Knotenanalyse (Abb. [9](#abb-9)).

:::abbildung et1/k8mna 9
Modifizierte Knotenanalyse. Die Quelle zwischen $i$ und $k$ bekommt eine neue Spalte für ihren Strom $I_V$ (grün) und eine neue Zeile für ihre Spannung (rot). $\mathbf Y$ bleibt, wie sie ist.
:::

:::satz Satz 9.1 (Modifizierte Knotenanalyse, MNA)
<span class="anker" id="satz-9-1"></span>

Ein Netz mit $n$ Knoten neben dem Bezugsknoten und einer idealen Spannungsquelle zwischen $i$ und $k$ erfüllt

<span class="anker" id="gl-9-1"></span>
$$\begin{pmatrix}\mathbf Y&\mathbf C\\\mathbf B&0\end{pmatrix}\begin{pmatrix}\mathbf U\\I_V\end{pmatrix}=\begin{pmatrix}\mathbf I_\mathrm q\\U_\mathrm q\end{pmatrix}. \tag{9.1}$$

$\mathbf C$ ist die neue Spalte mit $+1$ in Zeile $i$ und $-1$ in Zeile $k$. $\mathbf B$ ist die neue Zeile mit $+1$ in Spalte $i$ und $-1$ in Spalte $k$. $I_V$ zählt von $i$ durch die Quelle nach $k$. Die neue Zeile lautet

<span class="anker" id="gl-9-2"></span>
$$U_i-U_k=U_\mathrm q. \tag{9.2}$$

Für jede weitere Spannungsquelle kommt eine Zeile und eine Spalte hinzu.
:::

⁠**So liest man das:** $I_V$ fließt bei $i$ ab und bei $k$ zu, deshalb steht es in Zeile $i$ mit $+1$ und in Zeile $k$ mit $-1$, wie die abfließenden Ströme eines Leitwerts. Gibt die Quelle Leistung ab, fließt ihr Strom von Minus nach Plus durch sie hindurch, und $I_V$ ist negativ. Genau das zeigt SPICE als `I(V1)`. Die Einsen haben keine Einheit, die neue Zeile rechnet in Volt, die neue Spalte in Ampere. **Gültigkeit:** Auf der Diagonale steht nun eine Null, das System bleibt aber lösbar, solange das Netz eindeutig ist. Zwei ideale Quellen parallel sind es nicht. **Kurz gesagt:** Jedes Netzelement hat seinen eigenen Stempel, und alle lassen sich unabhängig voneinander eintragen.

::::beispiel das Rechenmodell, wie SPICE es sieht
SPICE wandelt nichts um. Die Batterie ist eine ideale Quelle $U_\mathrm q$ zwischen dem neuen Knoten 3 und Masse, dahinter liegt $R_1$ von 3 nach 1. Die Stromquelle und $R_5$ bleiben, wie sie sind. Unbekannt sind $U_1$, $U_2$, $U_3$ und $I_V$:

$$\begin{pmatrix}1{,}75&-0{,}5&-1&0\\-0{,}5&0{,}8&0&0\\-1&0&1&1\\0&0&1&0\end{pmatrix} \begin{pmatrix}U_1\\U_2\\U_3\\I_V\end{pmatrix}=\begin{pmatrix}0\\4\\0\\9\end{pmatrix}.$$

Die letzte Zeile gibt $U_3=9$ V, wodurch die ersten beiden Zeilen das System aus Stufe [5](das-knotenpotentialverfahren.html#stufe-5) werden: $U_1=8$ V, $U_2=10$ V. Die dritte Zeile liefert $I_V=G_1\,(U_1-U_3)=-1$ mA. Das sind die Ergebnisse beider Verfahren, ohne jedes Umwandeln.
::::

⁠**Grenzfall:** Für $R_1\to0$ wird Knoten 3 zu Knoten 1. Das Knotenpotentialverfahren versagt dort, die MNA nicht (Aufgabe [11](#aufg-11)).

:::ltspice Das Rechenmodell, wie SPICE es löst
⁠**Zeichnen:** `voltage` mit `9` von `3` nach Masse, `R1 1k` von `3` nach `1`, `R2 4k` von `1` nach Masse, `R3 2k` von `1` nach `2`, `R4 10k` und `R5 5k` von `2` nach Masse, `current` mit `4m` von Masse nach `2`.

⁠**Direktiven:** `.op`, `.meas op u1 FIND V(1)`, `.meas op u2 FIND V(2)`, `.meas op u3 FIND V(3)`, `.meas op iv FIND I(V1)`.

⁠**Was du siehst:** $\mathtt{u1}=8$ V, $\mathtt{u2}=10$ V, $\mathtt{u3}=9$ V, $\mathtt{iv}=-1$ mA. Das sind genau die vier Unbekannten der Matrix oben. `I(V1)` zählt vom Plus- zum Minusanschluss durch die Quelle, wie $I_V$. Ersetze danach die Batterie wie in Aufgabe [11](#aufg-11).
:::

**Eine Quelle mit 0 V ist ein Strommesser.** Eine ideale Spannungsquelle mit $U_\mathrm q=0$ wirkt wie ein Draht, die MNA liefert aber ihren Strom. Das nutzt man zur Messung der __Stromverstärkung__. Am Verstärker speist $I_\mathrm{ein}$ den Knoten 1 mit $G_\mathrm i$, der Ausgang 2 ist über die 0-V-Quelle mit Masse verbunden. Mit $I_\mathrm{aus}$ von Knoten 2 durch die Quelle nach Masse ist

<span class="anker" id="gl-9-3"></span>
$$\begin{pmatrix}G_\mathrm i&0&0\\g&G_\mathrm o&1\\0&1&0\end{pmatrix}\begin{pmatrix}U_1\\U_2\\I_\mathrm{aus}\end{pmatrix}=\begin{pmatrix}I_\mathrm{ein}\\0\\0\end{pmatrix},\qquad \frac{I_\mathrm{aus}}{I_\mathrm{ein}}=\frac{1}{I_\mathrm{ein}}\cdot\frac{g\,I_\mathrm{ein}}{-G_\mathrm i}=-\frac{g}{G_\mathrm i}. \tag{9.3}$$

Im Modell ist das $-100$. Weil $U_2=0$ ist, fließt durch $G_\mathrm o$ nichts, und der ganze gesteuerte Strom geht durch den Strommesser. Bei hohen Frequenzen sinkt dieser Betrag. Die Frequenz, bei der er auf 1 fällt, heißt __Transitfrequenz__ und kennzeichnet, wie schnell ein Transistor ist.

**Der Verstärker an einer idealen Quelle.** Liegt am Eingang die ideale Spannung $U_\mathrm q$, wird die Rechnung kürzer als in [(8.2)](gesteuerte-quellen-und-verstarker.html#gl-8-2). Mit $I_V$ von Knoten 1 durch die Quelle zur Masse und $G=G_\mathrm o+G_\mathrm L$ gilt

<span class="anker" id="gl-9-4"></span>
$$\begin{pmatrix}G_\mathrm i&0&1\\g&G&0\\1&0&0\end{pmatrix}\begin{pmatrix}U_\mathrm i\\U_\mathrm o\\I_V\end{pmatrix}=\begin{pmatrix}0\\0\\U_\mathrm q\end{pmatrix},\qquad A_u=\frac{U_\mathrm o}{U_\mathrm q}=\frac{1}{U_\mathrm q}\cdot\frac{g\,U_\mathrm q}{-G}=-\frac gG=-g\,R, \tag{9.4}$$

mit $R=1/G$. Das ist eine Grundstruktur, die bei fast allen Verstärkern wiederkehrt:

<span class="anker" id="gl-9-5"></span>
$$\text{Spannungsverstärkung}=-\text{Steilheit}\cdot\text{Lastwiderstand}. \tag{9.5}$$

Der Lastwiderstand ist die Parallelschaltung aller Widerstände am Ausgangsknoten, im Modell $20\,\mathrm{k\Omega}\parallel5\,\mathrm{k\Omega}=4\,\mathrm{k\Omega}$, also $A_u=-50\,\mathrm{mS}\cdot4\,\mathrm{k\Omega}=-200$. Speisen mehrere Quellen mit derselben Steuerspannung den Ausgang, addieren sich ihre Steilheiten. Die Regel eignet sich zum Abschätzen und zum Prüfen einer Rechnung. **Grenzfall:** Ohne Last und mit $G_\mathrm o\to0$ wächst $A_u$ ohne Grenze, dann begrenzt in Wirklichkeit die Versorgungsspannung.

:::frage Warum rechnet SPICE nicht mit Maschen, wenn es doch ohnehin Spannungsquellen braucht?
Weil die MNA nur für jede Spannungsquelle eine Zeile ergänzt, während Maschen erst gesucht werden müssten. Ein Netz hat meist wenige Spannungsquellen und sehr viele Bauteile. Außerdem wird die Matrix durch die Ergänzung kaum größer und bleibt dünn besetzt.
:::

:::aufgabe Aufgabe 11 ★★★ Ersetzen ohne Änderung
<span class="anker" id="aufg-11"></span>

Ersetze im Rechenmodell Batterie und $R_1$ durch eine ideale Quelle mit 8 V von Knoten 1 nach Masse.

<ol class="al">

<li>

Stelle das MNA-System für $U_1$, $U_2$, $I_V$ auf und löse es mit der cramerschen Regel.

</li>

<li>

Warum ändert sich gegenüber dem ursprünglichen Netz nichts außerhalb des ersetzten Zweigs?

</li>

<li>

Nun liefert die ideale Quelle 9 V. Wie groß sind $U_2$ und $I_V$?

</li>

</ol>

:::loesung
(a) Unbekannte $U_1$, $U_2$, $I_V$. Es bleiben $G_2$, $G_3$, $G_4$, $G_5$ und die Stromquelle:

$$\begin{pmatrix}0{,}75&-0{,}5&1\\-0{,}5&0{,}8&0\\1&0&0\end{pmatrix}\begin{pmatrix}U_1\\U_2\\I_V\end{pmatrix}=\begin{pmatrix}0\\4\\8\end{pmatrix}.$$

$D=-0{,}8$, $D_1=-6{,}4$, $D_2=-8$, $D_3=0{,}8$. Also $U_1=8$ V, $U_2=10$ V, $I_V=-1$ mA.

(b) An Knoten 1 lagen schon 8 V, und der Zweig führte 1 mA in den Knoten. Eine ideale Quelle mit genau dieser Spannung erzwingt denselben Zustand. Das übrige Netz spürt nur Spannung und Strom an diesem Knoten.

(c) $U_1=9$ V. Zeile 2: $U_2=(4+0{,}5\cdot9)/0{,}8=10{,}6$ V. Zeile 1: $I_V=-0{,}75\cdot9+0{,}5\cdot10{,}625=-1{,}44$ mA.
:::
:::
