---
title: Stufe 5: Die Regel und die virtuelle Masse
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Operationsverstärker
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
