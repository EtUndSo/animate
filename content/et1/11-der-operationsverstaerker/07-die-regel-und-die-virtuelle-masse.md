---
title: Stufe 5: Die Regel und die virtuelle Masse
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
order: 1210700
summary: Stufe 4 rechnete mit A .
tags: invertierenden Verstärker
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Stufe [4](gegenkopplung.html#stufe-4) rechnete mit $A$. Die Abweichung ist aber winzig. Diese Stufe macht daraus eine Regel für alle gegengekoppelten Schaltungen und wendet sie auf den wichtigsten Fall an: den Eingang am Minus-Anschluss.
:::

**Die Idee.** In jeder Schaltung gilt $|U_\mathrm{D}|\le11\,\mathrm{V}/100000=110$ µ V, solange der Ausgang nicht anschlägt. Gegen Spannungen im Voltbereich ist das nichts. Rechnet man also mit $U_\mathrm{D}=0$, macht man einen Fehler von der Größe $1/(A\beta)$. Damit braucht man $A$ nicht mehr.

:::satz Satz 5.1 (Die Regel für den gegengekoppelten OPV)
<span class="anker" id="satz-5-1"></span>

Solange $U_\mathrm{A,min}<U_\mathrm{A}<U_\mathrm{A,max}$ ist, gilt

<ol>

<li>

$\varphi_+=\varphi_-$: Der Ausgang stellt sich so ein, dass die Differenz verschwindet.

</li>

<li>

$I_+=I_-=0$: In die Eingänge fließt kein Strom.

</li>

<li>

Der Ausgang liefert jeden nötigen Strom. Für den Ausgangsknoten stellt man keine Knotengleichung auf.

</li>

</ol>

Man setzt die Knotenregel am Minus-Eingang an, löst nach $U_\mathrm{A}$ auf und prüft zuletzt die Grenzen.
:::

Beim __invertierenden Verstärker__ liegt der Plus-Eingang an Masse, $U_\mathrm{E}$ kommt über $R_1$ an den Minus-Eingang, $R_2$ führt vom Ausgang zurück (Abb. [7](#abb-7)). Aus $\varphi_-=\varphi_+=0$ und $I_-=0$ folgt

<span class="anker" id="gl-5-1"></span>
$$\frac{U_\mathrm{E}}{R_1}+\frac{U_\mathrm{A}}{R_2}=0\quad\Rightarrow\quad U_\mathrm{A}=-\frac{R_2}{R_1}\,U_\mathrm{E},\qquad R_\mathrm{ein}=\frac{U_\mathrm{E}}{I_1}=R_1. \tag{5.1}$$

⁠**So liest man das:** $I_1$ ist der Strom durch $R_1$. $R_\mathrm{ein}$ ist der Widerstand, den die Quelle sieht: nur $R_1$, weil dessen rechtes Ende fest auf 0 V liegt. Mit endlichem $A$ ist $G=-(R_2/R_1)\big/\bigl(1+1/(A\beta)\bigr)$ mit demselben $\beta=R_1/(R_1+R_2)$. **Gültigkeit:** wie die Regel, und $A\beta\gg1$.

:::herleitung Endliches $A$ beim Invertierer
Die Überlagerung am Teiler aus $R_1$ und $R_2$ ergibt $\varphi_-=(R_2\,U_\mathrm{E}+R_1\,U_\mathrm{A})/(R_1+R_2)$. Mit $\varphi_+=0$ ist $U_\mathrm{D}=-\varphi_-$, also $U_\mathrm{A}=-A\,\varphi_-$. Auflösen: $U_\mathrm{A}(1+A\beta)=-A\,(1-\beta)\,U_\mathrm{E}$ mit $1-\beta=R_2/(R_1+R_2)$. Wegen $A(1-\beta)=A\beta\cdot R_2/R_1$ folgt die Formel. Die Schleife sieht $U_\mathrm{E}$ als festen Wert, daher ist $\beta$ derselbe Teiler wie in Stufe [4](gegenkopplung.html#stufe-4).
:::

**Der Mechanismus der virtuellen Masse.** Bei $U_\mathrm{E}=1$ V treibt die Spannung an $R_1$ einen Strom von 100 µ A zum Minus-Eingang. In den OPV kann er nicht. Er muss also durch $R_2$. Für 100 µ A durch 40 k$\Omega$ muss das rechte Ende von $R_2$ um 4 V tiefer liegen, also geht der Ausgang auf $-4$ V. Der Strom läuft weiter in den Ausgang und durch den unteren Ausgangstransistor nach $U_\mathrm{B-}$ (rote Linie in Abb. [7](#abb-7)). Am Knoten bleibt nur die winzige Spannung $\varphi_-=-U_\mathrm{D}=U_\mathrm{A}/(-A)=+40$ µ V stehen. Der Knoten verhält sich wie eine Masse, ist aber keine:

<ul>

<li>

Eine echte Masse nimmt Strom auf. Die virtuelle reicht ihn an $R_2$ weiter, zwischen Knoten und Masse fließt nichts.

</li>

<li>

Eine echte Masse bleibt immer auf 0 V. Die virtuelle hält ihr Potenzial nur, weil der Ausgang ständig nachregelt. Steht er am Anschlag, ist sie weg (Abb. [7](#abb-7) unten).

</li>

<li>

Verbindet man den Knoten mit einem Draht zur Masse, fließen die 100 µ A dorthin, $R_2$ wird stromlos und $U_\mathrm{A}=0$.

</li>

</ul>

**Warum trotzdem kein Eingangsstrom fließt.** Zwischen den Eingängen liegt fast keine Spannung, aber auch kein Leiter. Sie haben gleiches Potenzial, sind aber nicht verbunden: 40 µ V über $r_\mathrm{e}=1$ M$\Omega$ ergeben 40 pA, 2,5 Millionen Mal weniger als $I_1$. Beides zusammen wirkt: Die Differenzstufe ist hochohmig, und die Schleife lässt ihr fast keine Spannung.

:::frage Bei 0 V am Knoten und ankommendem Strom müsste der Minus-Eingang doch den Widerstand null haben?
So wirkt er für die Quelle: Hinter $R_1$ sieht sie einen Punkt, der sein Potenzial hält, egal welcher Strom ankommt. Das leistet aber der Ausgang über $R_2$. Der Eingang selbst bleibt hochohmig mit 1 M$\Omega$.
:::

:::abbildung et1/k11invert 7
Oben der invertierende Verstärker, in Rot der Strompfad bei $U_\mathrm{E}=+1$ V. Unten die Grenze: $\hat u_\mathrm{E}=3{,}5$ V ergäbe 14 V, der Ausgang schlägt bei $\pm11$ V an. Dann hebt sich $\varphi_-$ bis 0,6 V, die virtuelle Masse ist fort.
:::

::::beispiel
$U_\mathrm{A}=-4\cdot1\,\mathrm{V}=-4$ V, mit endlichem $A$ genauer $-3{,}9998$ V. $R_\mathrm{ein}=10$ k$\Omega$. An einer Last von 2 k$\Omega$ gegen Masse fließen 2 mA, der Ausgang nimmt 2,1 mA auf: Last plus Rückführung. Die Quelle $U_\mathrm{E}$ merkt davon nichts.
::::

⁠**Grenzfälle:** $R_2=R_1$ kehrt nur das Vorzeichen um. $R_2\to0$ ergibt $U_\mathrm{A}=0$.

**Die erste Grenze.** Die Regel 1 setzt voraus, dass der Ausgang die verlangte Spannung erreicht. Bei $G=-4$ endet das bei $|U_\mathrm{E}|=11\,\mathrm{V}/4=2{,}75$ V. Darüber ist $U_\mathrm{A}=\mp11$ V fest, die Schleife ist offen, und der Teiler aus $R_1$ und $R_2$ bestimmt den Knoten: $\varphi_-=0{,}8\,U_\mathrm{E}+0{,}2\,U_\mathrm{A}$, bei 3,5 V also $+0{,}6$ V.

:::aufgabe Aufgabe 5 ★★ Invertierender Verstärker
<span class="anker" id="aufg-5"></span>

$R_1=4{,}7$ k$\Omega$, $R_2=47$ k$\Omega$, $U_\mathrm{E}=0{,}5$ V. (a) Bestimme $U_\mathrm{A}$, $I_1$ und $R_\mathrm{ein}$. (b) Wie groß sind bei $A=100000$ der Wert $\varphi_-$ und das exakte $G$? (c) Eine Last von 1 k$\Omega$ hängt am Ausgang. Wie groß ist der Ausgangsstrom, und woher kommt er? (d) Bis zu welchem $U_\mathrm{E}$ reicht der Ausgang? Wie groß ist $\varphi_-$ bei $U_\mathrm{E}=2$ V?

:::loesung
(a) $U_\mathrm{A}=-10\cdot0{,}5\,\mathrm{V}=-5$ V, $I_1=106{,}4$ µ A, $R_\mathrm{ein}=4{,}7$ k$\Omega$. (b) $\varphi_-=5\,\mathrm{V}/A=50$ µ V. Mit $\beta=4{,}7/51{,}7=0{,}0909$ ist $G=-10/(1+1{,}1\cdot10^{-4})=-9{,}9989$. (c) Die Last führt 5 mA, die Rückführung 0,106 mA. In den Ausgang fließen 5,11 mA, weiter nach $U_\mathrm{B-}$. (d) $|U_\mathrm{E}|\le1{,}1$ V. Bei 2 V ist $U_\mathrm{A}=-11$ V und $\varphi_-=(47\cdot2-4{,}7\cdot11)\,\mathrm{V}/51{,}7=0{,}818$ V.
:::
:::

::::formelsammlung
**Regel für den gegengekoppelten OPV**

$$\varphi_+=\varphi_-,\qquad I_+=I_-=0$$

Gilt für $U_\mathrm{A,min}<U_\mathrm{A}<U_\mathrm{A,max}$. Der Ausgang liefert jeden nötigen Strom; Knotenregel am Minus-Eingang, nach $U_\mathrm{A}$ auflösen, zuletzt die Grenzen prüfen. Der Fehler hat die Größe $1/(A\beta)$.

**Invertierender Verstärker**

$$\frac{U_\mathrm{E}}{R_1}+\frac{U_\mathrm{A}}{R_2}=0\quad\Rightarrow\quad U_\mathrm{A}=-\frac{R_2}{R_1}\,U_\mathrm{E},\qquad R_\mathrm{ein}=\frac{U_\mathrm{E}}{I_1}=R_1$$

Plus-Eingang an Masse, $U_\mathrm{E}$ über $R_1$ am Minus-Eingang (virtuelle Masse), $R_2$ vom Ausgang zurück; $I_1$ ist der Strom durch $R_1$. Gilt wie die Regel und für $A\beta\gg1$.

**Invertierender Verstärker bei endlicher Leerlaufverstärkung**

$$G=-(R_2/R_1)\big/\bigl(1+1/(A\beta)\bigr)$$

Mit demselben $\beta=R_1/(R_1+R_2)$ wie beim nicht-invertierenden Verstärker.
::::

::::lernkarten
:::karte formel Regel für den gegengekoppelten OPV
Welche Regel gilt für einen gegengekoppelten OPV, solange sein Ausgang nicht anschlägt, und wie rechnet man damit?
---
$\varphi_+=\varphi_-$ und $I_+=I_-=0$; der Ausgang liefert jeden nötigen Strom. Man setzt die Knotenregel am Minus-Eingang an und prüft zuletzt die Grenzen.
--- falsch
$\varphi_+=\varphi_-=0$ und $I_+=I_-=0$; der Ausgang liegt auf Masse. Man setzt die Knotenregel am Ausgang an und prüft zuletzt die Potenziale der Eingänge gegen Masse.
--- falsch
$\varphi_+=\varphi_-$ und $I_+=I_-$, aber ungleich null: Der Strom, der in den Plus-Eingang fließt, kommt am Minus-Eingang wieder heraus und fließt durch die Rückführung.
--- falsch
$\varphi_+=\varphi_-$ und $I_+=I_-=0$, in jeder OPV-Schaltung, auch ohne Rückführung; die Grenzen des Ausgangs muss man dabei nie prüfen.
:::
:::karte zusammenhang Warum die Regel genügt
Warum darf man bei einem gegengekoppelten OPV mit $U_\mathrm{D}=0$ rechnen, obwohl die Differenz nie genau null ist?
---
Solange der Ausgang nicht anschlägt, ist $|U_\mathrm{D}|\le11\,\mathrm{V}/100000=110$ µ V. Der Fehler hat die Größe $1/(A\beta)$, und $A$ wird nicht mehr gebraucht.
--- falsch
Weil die Gegenkopplung die Differenz exakt auf null regelt; der Ausgang braucht keine Differenz, er hält seinen Wert aus der inneren Kapazität.
--- falsch
Weil die Differenz höchstens 110 mV beträgt; gegen 11 V ist das 1 %, und diese Genauigkeit genügt für die meisten Schaltungen.
--- falsch
Weil der Fehler mit $A\beta$ wächst; bei großem $A$ ist er zwar groß, wirkt aber nur auf den Ausgangsstrom und nicht auf die Spannungen.
:::
:::karte begriff invertierenden Verstärker
Wie ist der invertierende Verstärker beschaltet, und was macht er mit der Eingangsspannung?
---
Der Plus-Eingang liegt an Masse, $U_\mathrm{E}$ kommt über $R_1$ an den Minus-Eingang, und $R_2$ führt zurück. Er verstärkt um $-R_2/R_1$, kehrt also das Vorzeichen um.
--- falsch
$U_\mathrm{E}$ liegt am Plus-Eingang, ein Teiler aus $R_2$ und $R_1$ führt auf den Minus-Eingang zurück. Er verstärkt um $1+R_2/R_1$, mit gleichem Vorzeichen.
--- falsch
Der Minus-Eingang liegt an Masse, $U_\mathrm{E}$ kommt über $R_1$ an den Plus-Eingang, und $R_2$ führt vom Ausgang zurück. Er verstärkt um $-R_2/R_1$.
--- falsch
Der Plus-Eingang liegt an Masse, $U_\mathrm{E}$ kommt über $R_1$ an den Minus-Eingang, und $R_2$ führt zurück. Er verstärkt um $-R_1/R_2$.
:::
:::karte formel Knotenregel am invertierenden Verstärker
Welche Gleichung liefert die Knotenregel am Minus-Eingang eines invertierenden Verstärkers, und welchen Eingangswiderstand sieht die Quelle?
---
$\frac{U_\mathrm{E}}{R_1}+\frac{U_\mathrm{A}}{R_2}=0\quad\Rightarrow\quad U_\mathrm{A}=-\frac{R_2}{R_1}\,U_\mathrm{E}$. Die Quelle sieht $R_\mathrm{ein}=\frac{U_\mathrm{E}}{I_1}=R_1$, weil das rechte Ende von $R_1$ fest auf 0 V liegt.
--- falsch
$\frac{U_\mathrm{E}}{R_1}=\frac{U_\mathrm{A}}{R_2}$, also $U_\mathrm{A}=\frac{R_2}{R_1}\,U_\mathrm{E}$; die Quelle sieht $R_1+R_2$, weil beide Widerstände zwischen ihr und dem Ausgang in Reihe liegen.
--- falsch
$\frac{U_\mathrm{E}}{R_1}+\frac{U_\mathrm{A}}{R_2}=0$, also $U_\mathrm{A}=-\frac{R_2}{R_1}\,U_\mathrm{E}$; die Quelle sieht 1 M$\Omega$, weil ihr Strom in den Minus-Eingang fließt.
--- falsch
$\frac{U_\mathrm{E}}{R_1}+\frac{U_\mathrm{A}}{R_2}=0$, also $U_\mathrm{A}=-\frac{R_1}{R_2}\,U_\mathrm{E}$; die Quelle sieht $R_2$, weil ihr Strom durch $R_2$ weiterfließt.
:::
:::karte herleitung Endliche Leerlaufverstärkung beim Invertierer
Wie folgt beim invertierenden Verstärker mit endlichem $A$ die Verstärkung $G=-(R_2/R_1)\big/\bigl(1+1/(A\beta)\bigr)$?
---
Die Überlagerung am Teiler aus $R_1$ und $R_2$ ergibt $\varphi_-=(R_2\,U_\mathrm{E}+R_1\,U_\mathrm{A})/(R_1+R_2)$, weil kein Strom in den Eingang fließt und beide Spannungen über den Teiler wirken.
---
Mit $\varphi_+=0$ ist $U_\mathrm{D}=-\varphi_-$, also $U_\mathrm{A}=-A\,\varphi_-$, weil der Plus-Eingang an Masse liegt.
---
Einsetzen und Auflösen ergibt $U_\mathrm{A}(1+A\beta)=-A\,(1-\beta)\,U_\mathrm{E}$ mit $1-\beta=R_2/(R_1+R_2)$, weil $\beta=R_1/(R_1+R_2)$ der Anteil von $U_\mathrm{A}$ am Knoten ist.
---
Wegen $A(1-\beta)=A\beta\cdot R_2/R_1$ folgt die Formel, weil man Zähler und Nenner durch $A\beta$ teilen kann.
---
$\beta$ ist derselbe Teiler wie beim nicht-invertierenden Verstärker, weil die Schleife $U_\mathrm{E}$ als festen Wert sieht.
:::
:::karte begriff virtuelle Masse
Was ist die virtuelle Masse am Minus-Eingang eines invertierenden Verstärkers?
---
Ein Knoten auf 0 V ohne Verbindung zur Masse. Er hält sein Potenzial nur, weil der Ausgang über die Rückführung ständig nachregelt; zwischen Knoten und Masse fließt kein Strom.
--- falsch
Ein Knoten, der im OPV über einen sehr kleinen Widerstand mit Masse verbunden ist. Der Strom aus $R_1$ fließt über diesen Widerstand nach Masse ab.
--- falsch
Ein Knoten auf 0 V ohne Verbindung zur Masse. Er bleibt auch dann auf 0 V, wenn der Ausgang am Anschlag steht, weil die Eingänge gleiche Potenziale erzwingen, ganz ohne Hilfe des Ausgangs.
--- falsch
Der Masseanschluss des OPV, den man im Schaltbild weglässt. Über ihn fließt der Strom aus $R_1$ in die Versorgung, deshalb liegt der Knoten auf 0 V.
:::
:::karte zusammenhang Strompfad am invertierenden Verstärker
Wohin fließt bei einem invertierenden Verstärker mit $U_\mathrm{E}=1$ V der Strom von 100 µ A, der durch $R_1$ zum Minus-Eingang kommt?
---
In den OPV kann er nicht, also muss er durch $R_2$. Dafür geht der Ausgang auf $-4$ V, und der Strom läuft weiter in den Ausgang nach $U_\mathrm{B-}$.
--- falsch
In den Minus-Eingang und von dort über den Eingangswiderstand $r_\mathrm{e}$ nach Masse; deshalb liegt der Knoten auf 0 V.
--- falsch
In die virtuelle Masse und von dort direkt nach Masse; durch $R_2$ fließt kein Strom, weil seine beiden Enden auf 0 V liegen.
--- falsch
Durch $R_2$ zum Ausgang und von dort über den oberen Ausgangstransistor nach $U_\mathrm{B+}$, weil der Ausgang dabei auf $+4$ V steht.
:::
:::karte zusammenhang Draht zur echten Masse
Was passiert mit dem invertierenden Verstärker, wenn man die virtuelle Masse mit einem Draht zur echten Masse verbindet?
---
Die 100 µ A aus $R_1$ fließen dann über den Draht nach Masse, $R_2$ wird stromlos, und $U_\mathrm{A}=0$. Die virtuelle Masse hatte diesen Strom nur an $R_2$ weitergereicht.
--- falsch
Nichts ändert sich, weil der Knoten schon auf 0 V liegt; der Draht führt keinen Strom, und $U_\mathrm{A}$ bleibt bei $-4$ V.
--- falsch
Der Ausgang läuft an den Anschlag bei $-11$ V, weil der Draht den Minus-Eingang kurzschließt und die Gegenkopplung damit verstärkt.
--- falsch
Die Verstärkung verdoppelt sich, weil der Strom aus $R_1$ nun zusätzlich über den Draht fließt und $R_2$ den doppelten Strom führt.
:::
:::karte zusammenhang Kein Eingangsstrom
Warum fließt kein Strom in den Minus-Eingang, obwohl er wie eine Masse auf 0 V liegt?
---
Zwischen den Eingängen liegt fast keine Spannung: Sie haben gleiches Potenzial, sind aber nicht verbunden. 40 µ V über $r_\mathrm{e}=1$ M$\Omega$ ergeben 40 pA.
--- falsch
Weil der Minus-Eingang innen mit dem Plus-Eingang verbunden ist; der Strom fließt durch diese innere Verbindung zum Plus-Eingang nach Masse und nicht in den OPV.
--- falsch
Weil der Minus-Eingang den Widerstand null hat; an null Ohm fällt keine Spannung ab, also kann auch kein Strom in ihn hineinfließen.
--- falsch
Weil der Strom aus $R_1$ zu klein ist; erst ab rund 1 mA fließt ein merklicher Teil in den Eingang, und dann gilt die Regel nicht mehr.
:::
:::karte zusammenhang Widerstand null für die Quelle
Warum wirkt der Minus-Eingang eines invertierenden Verstärkers für die Quelle wie ein Widerstand null, obwohl der Eingang selbst 1 M$\Omega$ hat?
---
Hinter $R_1$ sieht die Quelle einen Punkt, der sein Potenzial hält, egal welcher Strom ankommt. Das leistet aber der Ausgang über $R_2$.
--- falsch
Weil $r_\mathrm{e}$ und $R_2$ parallel liegen und der kleinere Widerstand $R_2$ bestimmt; der Eingang ist also tatsächlich niederohmig.
--- falsch
Weil die Gegenkopplung den Widerstand des Eingangs selbst um $1+A\beta$ verkleinert; aus 1 M$\Omega$ werden so rund 50 $\Omega$.
--- falsch
Weil der Strom aus $R_1$ ganz in den Eingang fließt und im OPV nach Masse abgeleitet wird; die 1 M$\Omega$ gelten nur ohne Rückführung.
:::
:::karte zusammenhang Grenze des invertierenden Verstärkers
Was passiert mit einem invertierenden Verstärker mit $G=-4$, wenn $|U_\mathrm{E}|$ größer als 2,75 V wird?
---
Der Ausgang steht fest auf $\mp11$ V. Die Schleife ist offen, der Teiler bestimmt den Knoten, $\varphi_-=0{,}8\,U_\mathrm{E}+0{,}2\,U_\mathrm{A}$: Die virtuelle Masse ist fort.
--- falsch
Der Ausgang folgt weiter mit $-4\,U_\mathrm{E}$, bei 3,5 V also mit $-14$ V; die virtuelle Masse bleibt auf 0 V, weil die Regel für jede Spannung gilt.
--- falsch
Der Ausgang steht auf $\mp11$ V, aber der Knoten bleibt auf 0 V; der Strom, den $R_2$ nicht mehr aufnimmt, fließt in den Minus-Eingang.
--- falsch
Die Verstärkung sinkt stetig auf $-2$, weil der OPV seine Leerlaufverstärkung bei großen Spannungen halbiert; der Knoten bleibt dabei auf 0 V.
:::
::::
