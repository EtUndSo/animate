---
title: Stufe 8: Die Maschenregel ist Energieerhaltung
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom, Widerstand und Kirchhoff
order: 1120900
summary: Die zweite Gleichungsart: Was verlangt die Erhaltung der Energie längs eines geschlossenen Wegs?
tags: 
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Die zweite Gleichungsart: Was verlangt die Erhaltung der Energie längs eines geschlossenen Wegs? Mit ihr lässt sich das Netz vollständig lösen.
:::

**Die Idee.** Jeder Punkt eines Netzes hat ein Potenzial ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Wer einmal im Kreis läuft, kommt am selben Punkt an, also auf demselben Potenzial (Abb. [9](#abb-9)). Für eine Ladung heißt das: Was sie in der Quelle an Energie gewinnt, gibt sie in den Widerständen wieder ab. In der Batterie heben chemische Kräfte die Ladung gegen das Feld auf das höhere Potenzial.

:::analogie
Eine Rundwanderung endet am Ausgangspunkt. Alle Anstiege zusammen sind genauso hoch wie alle Abstiege, gleich welcher Weg gewählt wurde. Die Analogie endet, wenn sich ein Magnetfeld ändert: Dann hat ein Ort keine feste „Höhe“ mehr ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)).
:::

:::satz Satz 8.1 (Maschenregel, zweites kirchhoffsches Gesetz)
<span class="anker" id="satz-8-1"></span>

Die Summe aller Zweigspannungen längs einer Masche ist in jedem Umlaufsinn und in jedem Zeitpunkt null:

<span class="anker" id="gl-8-1"></span>
$$\sum_{\nu=1}^{N}U_\nu=0,\qquad U_\nu\text{ positiv mit dem Umlauf, negativ gegen den Umlauf gezählt.} \tag{8.1}$$

Für ein Netz sind $z-k+1$ dieser Gleichungen unabhängig, alle anderen sind dann erfüllt.
:::

⁠**So liest man das:** $U_\nu$ ist die Spannung eines Zweigs, mit seinem Pfeil. Der Umlaufsinn ist frei, er ändert nur das Gesamtvorzeichen. **Gültigkeit:** Der magnetische Fluss durch die Masche darf sich nicht ändern, sonst ist das Feld nicht wirbelfrei ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). In Schaltungen sitzt dieser Fluss fast ganz in Spulen. Die Regel gilt auch für Wege über offene Klemmen, denn ein Weg muss keinem Draht folgen.

:::herleitung Maschenregel aus dem Potenzial
Nach [Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) ist $U_{12}=\varphi_1-\varphi_2=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s$ wegunabhängig, also $\oint\vec E\cdot\mathrm{d}\vec s=0$. Für Punkte $P_1,\dots,P_N$ längs einer Masche ergibt das

$$(\varphi_1-\varphi_2)+(\varphi_2-\varphi_3)+\dots+(\varphi_N-\varphi_1)=0.$$

Jedes Potenzial tritt einmal mit $+$ und einmal mit $-$ auf. Mit der Ladung $Q$ multipliziert ist das die Energiebilanz eines Umlaufs: Die Summe aller $Q\,U_\nu$ ist null.
:::

:::abbildung et1/k2masche 9
Potenzial im gelösten Netz längs zweier Maschen. Eine positive Spannung senkt das Potenzial, wenn man ihrem Pfeil folgt, gegen den Pfeil hebt sie es. Links: Quelle hebt, $R_\mathrm a$ und $R_\mathrm b$ senken um $4+5=9$ V. Rechts läuft der Umlauf ohne Quelle: Der Rückweg durch $R_\mathrm b$ gegen den Strom hebt das Potenzial. Beide Umläufe enden auf dem Startwert.
:::

::::beispiel das Netz lösen
Die Spannungspfeile an den Widerständen liegen im VZS, also von oben nach unten und $U_\mathrm e$ von $K_2$ nach $K_3$. $U_0=9$ V zeigt von $K_1$ nach $K_4$ (GZS). Die drei Maschen aus Abb. [7](knoten-zweige-maschen.html#abb-7) ergeben

$$M_1:\ U_\mathrm a+U_\mathrm b-U_0=0,\qquad M_2:\ U_\mathrm c+U_\mathrm d-U_0=0,\qquad M_3:\ U_\mathrm e+U_\mathrm d-U_\mathrm b=0.$$

Mit dem ohmschen Gesetz und den Knotengleichungen $I_\mathrm b=I_\mathrm a-I_\mathrm e$, $I_\mathrm d=I_\mathrm c+I_\mathrm e$ bleiben drei Unbekannte (in mA, $\mathrm{k\Omega}$, V):

$$7\,I_\mathrm a-5\,I_\mathrm e=9,\qquad4\,I_\mathrm c+I_\mathrm e=9,\qquad-5\,I_\mathrm a+I_\mathrm c+8\,I_\mathrm e=0.$$

Die ersten beiden liefern $I_\mathrm a=(9+5\,I_\mathrm e)/7$ und $I_\mathrm c=(9-I_\mathrm e)/4$. In die dritte eingesetzt und mit 28 multipliziert entsteht $117\,I_\mathrm e=117$, also $I_\mathrm e=1$ mA. Damit ist

| Zweig | 0 | a | b | c | d | e |
|---|---|---|---|---|---|---|
| $I$ in mA | 4 | 2 | 1 | 2 | 3 | 1 |
| $U$ in V | 9 | 4 | 5 | 6 | 3 | 2 |

Die Potenziale gegen $K_4$ sind 9, 5, 3 und 0 V. **Kontrollen:** Eine vierte Masche durch $K_1$, $K_2$, $K_3$ muss von selbst stimmen: $U_\mathrm a+U_\mathrm e-U_\mathrm c=4+2-6=0$. Energie: Die Quelle liefert $9\,\mathrm{V}\cdot4\,\mathrm{mA}=36$ mW, die Widerstände nehmen $8+5+12+9+2=36$ mW auf. Liegen zwei Wege zwischen denselben Punkten, etwa $R_1$, $R_2$ in Reihe neben $R_3$, folgt $U_1+U_2-U_3=0$.
::::

:::ltspice Das Netz nachrechnen
⁠**Zeichnen:** Quelle `voltage` mit `9` von `k1` nach Masse, also ist $K_4$ die Masse. `res`: `Ra 2k` von `k1` nach `k2`, `Rb 5k` von `k2` nach Masse, `Rc 3k` von `k1` nach `k3`, `Rd 1k` von `k3` nach Masse, `Re 2k` von `k2` nach `k3`.

⁠**Direktiven:** `.op`, dazu `.meas op p2 FIND V(k2)`, `.meas op ie FIND I(Re)` und ebenso für die anderen Größen. Die Ergebnisse stehen im SPICE Error Log.

⁠**Was du siehst:** $\mathtt{V(k2)}=5$ V, $\mathtt{V(k3)}=3$ V, $\mathtt{I(Ra)}=\mathtt{I(Rc)}=2$ mA, $\mathtt{I(Rb)}=\mathtt{I(Re)}=1$ mA, $\mathtt{I(Rd)}=3$ mA. $\mathtt{I(V1)}=-4$ mA: SPICE zählt den Quellenstrom im VZS, deshalb negativ. Baue danach Aufgabe [8](#aufg-8) nach.
:::

:::frage Woher „weiß“ der Strom, wie er sich aufteilen muss?
Er weiß nichts. Beim Einschalten sammeln sich an den Knoten winzige Ladungen und verschieben deren Potenziale so lange, bis an jedem Knoten nichts mehr hängen bleibt. Das geschieht in Nanosekunden. Das Ergebnis ist die einzige Lösung, die beide Regeln zugleich erfüllt.
:::

:::aufgabe Aufgabe 8 ★★ Masche und Knoten zusammen
<span class="anker" id="aufg-8"></span>

Eine 12-V-Quelle speist $R_1=1{,}5\,\mathrm{k\Omega}$, dahinter liegen $R_2=3\,\mathrm{k\Omega}$ und ein unbekannter Widerstand $R_3$ nebeneinander. Gemessen wird $U_1=9$ V.

<ol class="al">

<li>

Bestimme mit der Maschenregel $U_2$ und $U_3$.

</li>

<li>

Bestimme alle Ströme und $R_3$.

</li>

<li>

Prüfe die Energiebilanz.

</li>

<li>

Vorhersage: Durch die Masche aus Quelle, $R_1$ und $R_2$ tritt ein Stabmagnet, der sich bewegt. Was stimmt nun nicht mehr?

</li>

</ol>

:::loesung
(a) Masche Quelle, $R_1$, $R_2$: $U_2=12\,\mathrm{V}-9\,\mathrm{V}=3$ V. Masche $R_2$, $R_3$: $U_3=U_2=3$ V.

(b) $I_1=9\,\mathrm{V}/1{,}5\,\mathrm{k\Omega}=6$ mA, $I_2=3\,\mathrm{V}/3\,\mathrm{k\Omega}=1$ mA. Knotenregel: $I_3=5$ mA, also $R_3=3\,\mathrm{V}/5\,\mathrm{mA}=600\,\Omega$. Kontrolle: $R_2\parallel R_3=500\,\Omega$, gesamt $2\,\mathrm{k\Omega}$, $12\,\mathrm{V}/2\,\mathrm{k\Omega}=6$ mA.

(c) Die Quelle gibt $12\,\mathrm{V}\cdot6\,\mathrm{mA}=72$ mW ab, die Widerstände nehmen $54+3+15=72$ mW auf.

(d) Die Maschenregel. Der sich ändernde Fluss erzeugt längs der Masche ein Wirbelfeld, $\oint\vec E\cdot\mathrm{d}\vec s$ ist nicht null, und die Summe der Spannungen wird gleich der Induktionsspannung. Die Knotenregel bleibt gültig.
:::
:::
