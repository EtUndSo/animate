---
title: Stufe 9: Die modifizierte Knotenanalyse
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Maschenstrom- und Knotenpotentialverfahren
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren
knoten: Kapitel 8: Maschenstrom- und Knotenpotentialverfahren
order: 1181100
summary: Eine ideale Spannungsquelle hat keinen Leitwert und keine Stromquellenform (Kapitel 5).
tags: Stromverstärkung, Transitfrequenz
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Eine ideale Spannungsquelle hat keinen Leitwert und keine Stromquellenform ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Diese Stufe nimmt die letzte Einschränkung weg. So rechnet SPICE jede Schaltung.
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

::::formelsammlung
**Modifizierte Knotenanalyse**

$$\begin{pmatrix}\mathbf Y&\mathbf C\\\mathbf B&0\end{pmatrix}\begin{pmatrix}\mathbf U\\I_V\end{pmatrix}=\begin{pmatrix}\mathbf I_\mathrm q\\U_\mathrm q\end{pmatrix}$$

$n$ Knoten neben dem Bezugsknoten, ideale Spannungsquelle zwischen $i$ und $k$. $\mathbf C$ ist die neue Spalte mit $+1$ in Zeile $i$ und $-1$ in Zeile $k$, $\mathbf B$ die neue Zeile mit $+1$ in Spalte $i$ und $-1$ in Spalte $k$. $I_V$ zählt von $i$ durch die Quelle nach $k$ und ist negativ, wenn die Quelle Leistung abgibt. Für jede weitere Spannungsquelle kommen eine Zeile und eine Spalte hinzu. Lösbar, solange das Netz eindeutig ist; zwei ideale Quellen parallel sind es nicht.

**Zeile der Spannungsquelle**

$$U_i-U_k=U_\mathrm q$$

Die neue Zeile rechnet in Volt, die neue Spalte in Ampere; die Einsen haben keine Einheit. Mit $U_\mathrm q=0$ wirkt die Quelle wie ein Draht, und die MNA liefert ihren Strom: Sie ist ein Strommesser.

**Stromverstärkung**

$$\frac{I_\mathrm{aus}}{I_\mathrm{ein}}=-\frac{g}{G_\mathrm i}$$

Der Ausgang ist über eine 0-V-Quelle mit Masse verbunden, $I_\mathrm{aus}$ fließt von Knoten 2 durch die Quelle nach Masse. Wegen $U_2=0$ fließt durch $G_\mathrm o$ nichts. Die Frequenz, bei der der Betrag auf 1 fällt, ist die Transitfrequenz.

**Spannungsverstärkung an idealer Quelle**

$$A_u=\frac{U_\mathrm o}{U_\mathrm q}=-\frac gG=-g\,R$$

Am Eingang liegt die ideale Spannung $U_\mathrm q$; $G=G_\mathrm o+G_\mathrm L$ und $R=1/G$.

**Grundregel der Spannungsverstärkung**

$$\text{Spannungsverstärkung}=-\text{Steilheit}\cdot\text{Lastwiderstand}$$

Der Lastwiderstand ist die Parallelschaltung aller Widerstände am Ausgangsknoten. Speisen mehrere Quellen mit derselben Steuerspannung den Ausgang, addieren sich ihre Steilheiten. Zum Abschätzen und zum Prüfen einer Rechnung. Ohne Last und mit $G_\mathrm o\to0$ wächst $A_u$ ohne Grenze, dann begrenzt in Wirklichkeit die Versorgungsspannung.
::::

::::lernkarten
:::karte begriff modifizierte Knotenanalyse
Was ist die modifizierte Knotenanalyse, mit der SPICE jede Schaltung rechnet?
---
Die Knotenanalyse, ergänzt um den Strom jeder Spannungsquelle als zusätzliche Unbekannte. Die zusätzliche Gleichung liefert die Quelle selbst: Die Potenzialdifferenz an ihr ist $U_\mathrm q$.
--- falsch
Die Knotenanalyse, bei der man jede Spannungsquelle vorher in eine Stromquelle umwandelt. Dafür ergänzt man zu jeder Quelle einen kleinen Reihenwiderstand, damit die Umwandlung auch bei idealen Quellen gelingt.
--- falsch
Eine Mischung beider Verfahren, bei der man für jede Masche einen Maschenstrom und für jeden Knoten ein Potenzial ansetzt. Die Matrix hat dann $z$ Zeilen, je eine für jeden Zweig des Netzes.
--- falsch
Die Knotenanalyse, ergänzt um die Spannung jeder Stromquelle als zusätzliche Unbekannte. Die zusätzliche Gleichung liefert die Quelle selbst: Ihr Strom ist $I_\mathrm q$. So kehrt je Stromquelle eine Maschengleichung zurück.
:::
:::karte formel Gleichungssystem der modifizierten Knotenanalyse
Wie sieht das Gleichungssystem der modifizierten Knotenanalyse für ein Netz mit einer idealen Spannungsquelle zwischen den Knoten $i$ und $k$ aus?
---
$\begin{pmatrix}\mathbf Y&\mathbf C\\\mathbf B&0\end{pmatrix}\begin{pmatrix}\mathbf U\\I_V\end{pmatrix}=\begin{pmatrix}\mathbf I_\mathrm q\\U_\mathrm q\end{pmatrix}$. $\mathbf C$ ist die neue Spalte mit $+1$ in Zeile $i$ und $-1$ in Zeile $k$, $\mathbf B$ die neue Zeile mit $+1$ in Spalte $i$ und $-1$ in Spalte $k$. $\mathbf Y$ bleibt, wie sie ist.
--- falsch
Man ergänzt $\mathbf Y$ um eine Zeile und eine Spalte, beide mit $+1$ bei $i$ und $+1$ bei $k$, weil die Quelle beide Knoten gleich belastet. Auf der neuen Diagonale steht $U_\mathrm q$, auf der rechten Seite unten null.
--- falsch
Man trägt die Quelle als sehr großen Leitwert zwischen $i$ und $k$ in $\mathbf Y$ ein und schreibt $U_\mathrm q$ mal diesen Leitwert in die Zeilen $i$ und $k$ der rechten Seite. Die Matrix behält dabei ihre Größe, und $I_V$ wird nicht gebraucht.
--- falsch
Man streicht die Zeilen und Spalten von $i$ und $k$ aus $\mathbf Y$, weil ihre Potenziale durch die Quelle festliegen, und setzt $U_\mathrm q$ als bekannten Wert in die rechte Seite der übrigen Zeilen ein.
:::
:::karte formel Zeile der Spannungsquelle
Welche Gleichung bringt eine ideale Spannungsquelle zwischen den Knoten $i$ und $k$ in die modifizierte Knotenanalyse ein, und in welcher Einheit rechnet diese Zeile?
---
$U_i-U_k=U_\mathrm q$: Die Potenzialdifferenz an der Quelle ist ihre Quellenspannung. Die Einsen haben keine Einheit, die neue Zeile rechnet in Volt, die neue Spalte in Ampere.
--- falsch
$U_i+U_k=U_\mathrm q$: Die Potenziale beider Anschlüsse ergeben zusammen die Quellenspannung. Die neue Zeile rechnet in Ampere, weil sie zu den Knotengleichungen gehört.
--- falsch
$I_V=U_\mathrm q\,G$: Der Strom der Quelle ist ihre Spannung mal dem Leitwert am Knoten. Die neue Zeile rechnet deshalb in Ampere, die neue Spalte in Volt.
--- falsch
$U_i-U_k=U_\mathrm q$: Die Potenzialdifferenz an der Quelle ist ihre Quellenspannung. Die Einsen tragen die Einheit Siemens, damit die Zeile wie die übrigen in Ampere rechnet.
:::
:::karte zusammenhang Strom der Spannungsquelle als Unbekannte
Warum wird der Strom einer idealen Spannungsquelle in der modifizierten Knotenanalyse zur Unbekannten?
---
Eine Spannungsquelle legt nur die Spannung zwischen zwei Knoten fest. Ihr Strom stellt sich erst durch das Netz ein, ist also unbekannt, und als Leitwert lässt sich die Quelle nicht schreiben.
--- falsch
Weil ihr Strom stets gleich dem Quellenstrom der benachbarten Stromquelle ist und man ihn deshalb erst nach deren Wert eintragen kann. Ohne Stromquelle bleibt er null.
--- falsch
Eine Spannungsquelle legt ihren Strom selbst fest, aber dieser Wert ist dem Programm vorher nicht bekannt, weil er nicht in der Netzliste steht. Man berechnet ihn deshalb als Hilfsgröße mit.
--- falsch
Weil ihre Spannung unbekannt ist, solange das Netz nicht gelöst ist. Der Strom ist nur ein Hilfswert, aus dem man am Ende die tatsächliche Spannung zurückrechnet.
:::
:::karte zusammenhang Vorzeichen des Quellenstroms
Was bedeutet ein negativer Wert von $I_V$, wenn $I_V$ von $i$ durch die Quelle nach $k$ zählt?
---
Die Quelle gibt Leistung ab: Ihr Strom fließt von Minus nach Plus durch sie hindurch, also gegen die Zählrichtung von $I_V$. Genau so zeigt SPICE den Strom als `I(V1)` an.
--- falsch
Die Quelle nimmt Leistung auf und wird geladen: Ihr Strom fließt von Plus nach Minus durch sie hindurch. SPICE zeigt solche Ströme deshalb immer mit positivem Vorzeichen an.
--- falsch
Die Rechnung ist fehlerhaft, weil der Strom einer Spannungsquelle stets in Richtung ihres Spannungspfeils fließt. Man muss dann die Quelle in der Netzliste umdrehen.
--- falsch
Die Quelle gibt Leistung ab, weil ihr Strom von Plus nach Minus durch sie hindurchfließt, also in Zählrichtung von $I_V$. SPICE zeigt solche Ströme mit umgekehrtem Vorzeichen an.
:::
:::karte zusammenhang Null auf der Diagonale
Bleibt das Gleichungssystem der modifizierten Knotenanalyse lösbar, obwohl auf seiner Diagonale eine Null steht?
---
Ja, solange das Netz eindeutig ist; für jede weitere Spannungsquelle kommen einfach eine Zeile und eine Spalte hinzu. Nicht eindeutig sind etwa zwei ideale Spannungsquellen parallel.
--- falsch
Nein, eine Null auf der Diagonale macht die Determinante stets null. Man setzt deshalb dort einen kleinen Leitwert ein, damit sich das System lösen lässt.
--- falsch
Ja, aber nur, wenn das Netz höchstens eine Spannungsquelle enthält. Jede weitere Quelle bringt eine weitere Null auf die Diagonale, und dann versagt die Rechnung.
--- falsch
Ja, immer, denn die Null steht nur in der neuen Zeile, die keine Knotengleichung ist. Auch zwei ideale Spannungsquellen parallel lassen sich so ohne Weiteres berechnen, ihr Strom teilt sich gleichmäßig.
:::
:::karte zusammenhang Innenwiderstand gegen null
Was geschieht im Knotenpotentialverfahren und in der modifizierten Knotenanalyse, wenn der Innenwiderstand $R_1$ der Batterie gegen null geht?
---
Die Batterie wird zur idealen Quelle direkt an Knoten 1. Das Knotenpotentialverfahren versagt, weil sich die Quelle nicht mehr umwandeln lässt; die MNA rechnet weiter, denn sie nimmt den Quellenstrom als Unbekannte.
--- falsch
Beide Verfahren versagen, weil eine ideale Spannungsquelle unendlich viel Strom liefern kann. Man muss deshalb in jeder Rechnung einen kleinen Innenwiderstand stehen lassen, auch in SPICE.
--- falsch
Das Knotenpotentialverfahren rechnet weiter, weil der Leitwert $G_1$ dann einfach unendlich wird und ein Knotenpotential festlegt; die MNA versagt, weil ihr Strom $I_V$ dann unbestimmt bleibt und die Determinante null wird.
--- falsch
Beide Verfahren rechnen weiter: Das Knotenpotentialverfahren wandelt in eine Stromquelle mit $I_\mathrm q=U_\mathrm q/R_1$ um, und die MNA nimmt den Strom der Quelle als Unbekannte.
:::
:::karte zusammenhang Ersetzen durch eine ideale Quelle
Warum ändert sich im übrigen Netz nichts, wenn man einen Zweig durch eine ideale Quelle ersetzt, die genau die Spannung liefert, die vorher an seinem Knoten lag?
---
Das übrige Netz spürt nur Spannung und Strom an diesem Knoten. Eine ideale Quelle mit genau dieser Spannung erzwingt denselben Zustand, ihr Strom stellt sich wie vorher ein.
--- falsch
Weil eine ideale Quelle den Strom ihres Zweigs nicht ändert. Sie übernimmt den Strom des alten Zweigs und gibt ihn unverändert weiter, gleich welche Spannung sie liefert.
--- falsch
Es ändert sich doch etwas: Eine ideale Quelle hat keinen Innenwiderstand, deshalb steigen alle Ströme im übrigen Netz etwas an, auch wenn die Spannung am Knoten selbst gleich bleibt.
--- falsch
Weil das übrige Netz nur die Leistung des Zweigs spürt. Liefert die ideale Quelle dieselbe Leistung wie vorher Batterie und Widerstand zusammen, bleibt alles gleich.
:::
:::karte zusammenhang Quelle mit 0 V als Strommesser
Wozu setzt man in der modifizierten Knotenanalyse eine ideale Spannungsquelle mit $U_\mathrm q=0$ ein?
---
Als Strommesser: Sie wirkt wie ein Draht, die MNA liefert aber ihren Strom als Unbekannte. So misst man etwa den Ausgangsstrom eines Verstärkers mit kurzgeschlossenem Ausgang.
--- falsch
Als Spannungsmesser: Sie wirkt wie eine offene Klemme, an der kein Strom fließt, und die MNA liefert die Spannung zwischen ihren beiden Knoten als zusätzliche Unbekannte.
--- falsch
Als Platzhalter für eine Quelle, die man noch nicht kennt. Sie trägt nichts zur Matrix bei und wird beim Lösen des Systems einfach übersprungen.
--- falsch
Als Schutz gegen eine Null auf der Diagonale: Eine Quelle ohne Spannung bringt eine zusätzliche Zeile, die das Gleichungssystem erst lösbar macht.
:::
:::karte begriff Stromverstärkung
Was gibt die Stromverstärkung eines Verstärkers an, und wie groß ist sie im Verstärkermodell mit kurzgeschlossenem Ausgang?
---
Das Verhältnis von Ausgangs- zu Eingangsstrom bei kurzgeschlossenem Ausgang, $\frac{I_\mathrm{aus}}{I_\mathrm{ein}}=-\frac{g}{G_\mathrm i}$, im Modell $-100$. Weil $U_2=0$ ist, fließt durch $G_\mathrm o$ nichts, und der ganze gesteuerte Strom geht durch den Strommesser.
--- falsch
Das Verhältnis von Ausgangs- zu Eingangsstrom bei offenem Ausgang, $\frac{I_\mathrm{aus}}{I_\mathrm{ein}}=-\frac{g}{G_\mathrm o}$, im Modell $-1000$. Der gesteuerte Strom fließt dann ganz durch $G_\mathrm o$ und erzeugt dort die Ausgangsspannung, die man misst.
--- falsch
Das Verhältnis von Ausgangs- zu Eingangsspannung bei kurzgeschlossenem Ausgang, $-g/G_\mathrm i$, im Modell $-100$. Weil $U_2=0$ ist, stimmt sie dort mit der Spannungsverstärkung überein.
--- falsch
Das Verhältnis von Ausgangs- zu Eingangsstrom bei kurzgeschlossenem Ausgang, $\frac{I_\mathrm{aus}}{I_\mathrm{ein}}=-g\,G_\mathrm i$, im Modell $-25$. Ein Teil des gesteuerten Stroms fließt dabei durch $G_\mathrm o$.
:::
:::karte begriff Transitfrequenz
Was gibt die Transitfrequenz eines Transistors an, und was sagt sie über ihn aus?
---
Die Frequenz, bei der der Betrag der Stromverstärkung auf 1 fällt; bei hohen Frequenzen sinkt dieser Betrag. Sie kennzeichnet, wie schnell ein Transistor ist.
--- falsch
Die Frequenz, bei der die Stromverstärkung ihren größten Wert erreicht; darüber und darunter ist sie kleiner. Sie kennzeichnet die beste Betriebsfrequenz eines Transistors.
--- falsch
Die Frequenz, bei der der Betrag der Spannungsverstärkung auf die Hälfte fällt. Sie kennzeichnet, bis zu welcher Frequenz ein Transistor als linear gelten darf.
--- falsch
Die Frequenz, mit der die Ladungsträger den Transistor durchlaufen. Je höher sie ist, desto größer ist die Stromverstärkung bei niedrigen Frequenzen.
:::
:::karte formel Spannungsverstärkung an idealer Quelle
Welche Spannungsverstärkung ergibt die modifizierte Knotenanalyse für den Verstärker, wenn an seinem Eingang die ideale Spannung $U_\mathrm q$ liegt?
---
$A_u=\frac{U_\mathrm o}{U_\mathrm q}=-\frac gG=-g\,R$ mit $G=G_\mathrm o+G_\mathrm L$ und $R=1/G$. Die Steuerspannung ist direkt $U_\mathrm q$, und der gesteuerte Strom fließt ganz über $G$ ab. Im Modell sind das $-50\,\mathrm{mS}\cdot4\,\mathrm{k\Omega}=-200$.
--- falsch
$A_u=\frac{U_\mathrm o}{U_\mathrm q}=-\frac Gg$ mit $G=G_\mathrm o+G_\mathrm L$, weil der Ausgangsleitwert die Spannung treibt und die Steilheit sie bremst. Im Modell sind das $-0{,}005$, also fast keine Verstärkung.
--- falsch
$A_u=\frac{U_\mathrm o}{U_\mathrm q}=-\frac{g}{G_\mathrm i}$, weil nur der Eingangsleitwert bestimmt, wie viel Steuerspannung ankommt. Im Modell sind das $-50\,\mathrm{mS}/0{,}5\,\mathrm{mS}=-100$.
--- falsch
$A_u=\frac{U_\mathrm o}{U_\mathrm q}=-g\,R$ mit $R=1/G_\mathrm o$ allein, weil die Last außerhalb des Verstärkers liegt und ihn nicht beeinflusst. Im Modell sind das $-50\,\mathrm{mS}\cdot20\,\mathrm{k\Omega}=-1000$.
:::
:::karte formel Grundregel der Spannungsverstärkung
Welche Grundregel für die Spannungsverstärkung kehrt bei fast allen Verstärkern wieder, und was zählt dabei als Lastwiderstand?
---
Spannungsverstärkung $=-$ Steilheit $\cdot$ Lastwiderstand. Der Lastwiderstand ist die Parallelschaltung aller Widerstände am Ausgangsknoten. Speisen mehrere Quellen mit derselben Steuerspannung den Ausgang, addieren sich ihre Steilheiten.
--- falsch
Spannungsverstärkung $=-$ Steilheit $\cdot$ Lastwiderstand. Der Lastwiderstand ist nur der äußere Widerstand $R_\mathrm L$, denn der Ausgangswiderstand gehört zum Verstärker selbst. Speisen mehrere Quellen den Ausgang, zählt nur die Quelle mit der größten Steilheit.
--- falsch
Spannungsverstärkung $=-$ Steilheit $/$ Lastwiderstand. Der Lastwiderstand ist die Reihenschaltung aller Widerstände am Ausgangsknoten, im Modell 25 k$\Omega$. Mehrere Quellen teilen sich dieselbe Steilheit.
--- falsch
Spannungsverstärkung $=-$ Steilheit $\cdot$ Eingangswiderstand, also die Parallelschaltung aller Widerstände am Eingangsknoten, im Modell 2 k$\Omega$. Speisen mehrere Quellen den Ausgang, addieren sich ihre Steilheiten.
:::
:::karte zusammenhang Warum SPICE mit Knoten rechnet
Warum rechnet SPICE mit der modifizierten Knotenanalyse und nicht mit Maschen, obwohl es Spannungsquellen ohnehin berücksichtigen muss?
---
Die MNA ergänzt nur für jede Spannungsquelle eine Zeile, Maschen müsste das Programm erst suchen. Netze haben meist wenige Spannungsquellen und sehr viele Bauteile, die Matrix wird also kaum größer und bleibt dünn besetzt.
--- falsch
Weil Maschengleichungen bei Spannungsquellen nicht lösbar sind. Eine Spannungsquelle in einer Masche macht die Determinante der Widerstandsmatrix null, deshalb muss SPICE auf Knoten ausweichen.
--- falsch
Weil die MNA für jedes Bauteil eine eigene Zeile ergänzt und so alle Ströme auf einmal liefert. Die Matrix wird dadurch zwar groß, ist aber voll besetzt und deshalb mit der cramerschen Regel schnell lösbar.
--- falsch
Weil Netze meist viele Spannungsquellen und wenige Bauteile haben. Mit Maschen bräuchte jede Quelle eine eigene Masche, mit Knoten genügt eine einzige Zeile für alle Quellen gemeinsam.
:::
::::
