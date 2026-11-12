---
title: Stufe 8: Kettenform
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1161000
summary: Oft schaltet man Zweitore hintereinander.
tags: A-Parameter, Kette
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Oft schaltet man Zweitore hintereinander. Der Ausgang des einen speist den Eingang des nächsten. Diese Stufe wählt die Ausgangsgrößen als Ursachen und macht daraus ein Matrixprodukt.
:::

**Die Idee.** Hängt ein Zweitor hinter dem anderen, sind die Ausgangsgrößen des ersten genau die Eingangsgrößen des zweiten. Beschreibt eine Form die Eingangsgrößen durch die Ausgangsgrößen, kann man sie aneinanderhängen: Man startet an der Last und rechnet Stufe für Stufe zur Quelle zurück. Genau das tut die Kettenform. Das Minus vor $I_2$ ist der Grund, warum sie passt: Der Strom, der ein Zweitor verlässt, ist der Strom, der in das nächste hineinfließt.

:::definition Definition 8.1 (Kettenform, A-Form)
<span class="anker" id="satz-8-1"></span>

Die Kettenform nimmt $U_2$ und $-I_2$ als Ursachen:

<span class="anker" id="gl-8-1"></span>
$$U_1=A_{11}U_2+A_{12}(-I_2),\quad I_1=A_{21}U_2+A_{22}(-I_2),\qquad\text{kurz}\quad \begin{pmatrix}U_1\\I_1\end{pmatrix}=\mathbf A\begin{pmatrix}U_2\\-I_2\end{pmatrix}. \tag{8.1}$$

Die __A-Parameter__ folgen aus Versuchen am Ausgang:

<span class="anker" id="gl-8-2"></span>
$$A_{11}=\left.\frac{U_1}{U_2}\right|_{I_2=0},\quad A_{21}=\left.\frac{I_1}{U_2}\right|_{I_2=0},\quad A_{12}=\left.-\frac{U_1}{I_2}\right|_{U_2=0},\quad A_{22}=\left.-\frac{I_1}{I_2}\right|_{U_2=0}. \tag{8.2}$$

Für zwei Zweitore in __Kette__ gilt $\mathbf A=\mathbf A'\mathbf A''$.
:::

⁠**So liest man das:** $A_{11}$ ist die reziproke Leerlaufspannungsübersetzung vorwärts, $A_{21}$ der Leerlaufübertragungsleitwert vorwärts, $A_{12}$ der Kurzschluss-Übertragungswiderstand vorwärts, $A_{22}$ die reziproke Kurzschlussstromübersetzung vorwärts. Reziprok heißt: Es ist Eingang durch Ausgang, also der Kehrwert der gewohnten Übersetzung. $A_{11}$ und $A_{22}$ haben keine Einheit, $A_{12}$ hat $\Omega$, $A_{21}$ hat S. Ein Dämpfungsglied hat $A_{11}>1$. **Gültigkeit:** Die Kette verlangt die Reihenfolge $\mathbf A'\mathbf A''$, die Quelle sitzt links.

:::herleitung Warum die Kette ein Matrixprodukt ist
Mit Strich das erste, mit zwei Strichen das zweite Zweitor. Die Verbindung erzwingt $U_2'=U_1''$ und $-I_2'=I_1''$. Einsetzen:

$$\begin{pmatrix}U_1'\\I_1'\end{pmatrix}=\mathbf A'\begin{pmatrix}U_2'\\-I_2'\end{pmatrix}=\mathbf A'\begin{pmatrix}U_1''\\I_1''\end{pmatrix}=\mathbf A'\mathbf A''\begin{pmatrix}U_2''\\-I_2''\end{pmatrix}.$$
:::

:::abbildung et1/k6kette 10
Oben: Zwei Zweitore in Kette. Ausgang des ersten und Eingang des zweiten teilen Spannung und Strom. Unten: Das T-Zweitor als Kette aus drei Elementarzweitoren, Längswiderstand, Querleitwert, Längswiderstand.
:::

::::beispiel
Die einfachsten Bausteine sind der Längswiderstand und der Querleitwert. Beim Längswiderstand ist $U_1=U_2+R(-I_2)$ und $I_1=-I_2$, beim Querleitwert $U_1=U_2$ und $I_1=G\,U_2+(-I_2)$:

$$\mathbf A_R=\begin{pmatrix}1&R\\0&1\end{pmatrix},\qquad \mathbf A_G=\begin{pmatrix}1&0\\G&1\end{pmatrix}.$$

Das T-Zweitor ist eine Kette aus $R_\mathrm{a}$, $G_\mathrm{b}=1/R_\mathrm{b}=50$ mS und $R_\mathrm{c}$ (Abb. [10](#abb-10) unten):

$$\mathbf A=\begin{pmatrix}1&15\,\Omega\\0&1\end{pmatrix}\begin{pmatrix}1&0\\50\,\mathrm{mS}&1\end{pmatrix}\begin{pmatrix}1&20\,\Omega\\0&1\end{pmatrix}=\begin{pmatrix}1{,}75&50\,\Omega\\50\,\mathrm{mS}&2\end{pmatrix}.$$

Rückwärts von der Last, mit $U_2=3$ V und $-I_2=50$ mA: $U_1=5{,}25\,\mathrm{V}+2{,}5\,\mathrm{V}=7{,}75$ V und $I_1=150\,\mathrm{mA}+100\,\mathrm{mA}=250$ mA. Das sind die Werte aus Stufe [4](das-zweitor-im-betrieb.html#stufe-4), ohne Gleichungssystem.
::::

Die gleichwertige $\pi$-Schaltung mit den Querleitwerten $G_1$, $G_3$ und dem Längsleitwert $G_2$ ergibt allgemein

<span class="anker" id="gl-8-3"></span>
$$A_{11}=1+\frac{G_3}{G_2},\qquad A_{21}=G_1+G_3+\frac{G_1G_3}{G_2},\qquad A_{12}=\frac{1}{G_2},\qquad A_{22}=1+\frac{G_1}{G_2}, \tag{8.3}$$

zum Beispiel $A_{11}=1+15/20=1{,}75$. Bei offenem Ausgang bilden $G_2$ und $G_3$ einen Spannungsteiler, $U_2=U_1\,G_2/(G_2+G_3)$, daher $A_{11}$. Die übrigen folgen ebenso aus [(8.2)](#gl-8-2).

⁠**Grenzfälle:** $R=0$ und $G=0$ ergeben die Einheitsmatrix, ein Zweitor, das nichts tut. Zwei gleiche T-Zweitore in Kette haben $A_{11}=5{,}56$, nicht $1{,}75^2=3{,}06$. Das zweite belastet das erste, die Zwischenspannung sinkt dadurch unter den Leerlaufwert.

:::frage Das Signal läuft vorwärts. Warum rechnet die Kettenform rückwärts?
Weil sie eine Rechenvorschrift ist, kein Ablauf. Am Ausgang legt die Last mit $U_2$ auch $-I_2$ fest. Von dort liefert jede Stufe ohne Gleichungssystem die Größen davor. Physikalisch stellt sich alles gemeinsam ein.
:::

:::ltspice Die Kette belastet sich selbst
⁠**Zeichnen:** Quelle `voltage` mit `9` von `1` nach Masse. Erstes T: `Ra1` mit `15` von `1` nach `m1`, `Rb1` mit `20` von `m1` nach Masse, `Rc1` mit `20` von `m1` nach `k`. Zweites T genauso von `k` über `m2` nach `3`. `RL` mit `1G` von `3` nach Masse, also fast Leerlauf.

⁠**Direktiven:** `.op`, `.meas op Uk FIND V(k)`, `.meas op Ua FIND V(3)`, `.meas op Ie FIND I(Ra1)`.

⁠**Was du siehst:** $\mathtt{V(3)}=1{,}618$ V, also $9\,\mathrm{V}/1{,}618\,\mathrm{V}=5{,}56$, wie $A_{11}$ von $\mathbf A\mathbf A$. Am Punkt `k` stehen 2,83 V statt der 5,14 V, die ein einzelnes T im Leerlauf hätte. Setze `RL` auf 60 und prüfe Aufgabe [8](#aufg-8)(c): $\mathtt{V(3)}=1{,}036$ V.
:::

:::aufgabe Aufgabe 8 ★★★ Die Reihenfolge zählt
<span class="anker" id="aufg-8"></span>

Ein Längswiderstand von 30 $\Omega$ und das T-Zweitor werden in Kette geschaltet.

<ol class="al">

<li>

Berechne $\mathbf A$ für „T, dann Längswiderstand“ und für „Längswiderstand, dann T“.

</li>

<li>

Erkläre den Unterschied in $A_{11}$ mit Strömen und Spannungsteilern, ohne Matrizen.

</li>

<li>

Zwei gleiche T-Zweitore in Kette liegen an einer idealen 9-V-Quelle und speisen die Last 60 $\Omega$. Wie groß ist $U_2$? Rechne mit $\mathbf A\mathbf A$.

</li>

</ol>

:::loesung
(a) T, dann Längswiderstand: $A_{11}=1{,}75$, $A_{12}=102{,}5\,\Omega$, $A_{21}=50$ mS, $A_{22}=3{,}5$. Längswiderstand, dann T: $A_{11}=3{,}25$, $A_{12}=110\,\Omega$, $A_{21}=50$ mS, $A_{22}=2$.

(b) $A_{11}$ gilt bei offenem Ausgang. Im ersten Fall hängt der Längswiderstand offen am Ende, er führt keinen Strom, $A_{11}$ bleibt 1,75. Im zweiten liegt er vor dem Eingang des T, der 35 $\Omega$ zeigt. Er bildet mit ihm einen Spannungsteiler, $65/35=1{,}857$, und $1{,}857\cdot1{,}75=3{,}25$.

(c) $\mathbf A\mathbf A$ hat $A_{11}=5{,}5625$, $A_{12}=187{,}5\,\Omega$, $A_{21}=187{,}5$ mS, $A_{22}=6{,}5$. Mit $-I_2=U_2/60\,\Omega$ ist $U_1=(5{,}5625+187{,}5/60)\,U_2=8{,}6875\,U_2$, also $U_2=1{,}036$ V.
:::
:::

::::formelsammlung
**Kettenform (A-Form)**

$$U_1=A_{11}U_2+A_{12}(-I_2),\quad I_1=A_{21}U_2+A_{22}(-I_2),\qquad\text{kurz}\quad \begin{pmatrix}U_1\\I_1\end{pmatrix}=\mathbf A\begin{pmatrix}U_2\\-I_2\end{pmatrix}$$

Ursachen sind die Ausgangsgrößen $U_2$ und $-I_2$, der Strom, der das Zweitor verlässt.

**A-Parameter**

$$A_{11}=\left.\frac{U_1}{U_2}\right|_{I_2=0},\quad A_{21}=\left.\frac{I_1}{U_2}\right|_{I_2=0},\quad A_{12}=\left.-\frac{U_1}{I_2}\right|_{U_2=0},\quad A_{22}=\left.-\frac{I_1}{I_2}\right|_{U_2=0}$$

$A_{11}$ reziproke Leerlaufspannungsübersetzung, $A_{21}$ Leerlaufübertragungsleitwert in S, $A_{12}$ Kurzschluss-Übertragungswiderstand in $\Omega$, $A_{22}$ reziproke Kurzschlussstromübersetzung, alle vorwärts. Reziprok heißt Eingang durch Ausgang. Ein Dämpfungsglied hat $A_{11}>1$.

**Kette**

$$\mathbf A=\mathbf A'\mathbf A''$$

Die Verbindung erzwingt $U_2'=U_1''$ und $-I_2'=I_1''$. Reihenfolge: Das Zweitor an der Quelle steht links.

**Längswiderstand und Querleitwert**

$$\mathbf A_R=\begin{pmatrix}1&R\\0&1\end{pmatrix},\qquad \mathbf A_G=\begin{pmatrix}1&0\\G&1\end{pmatrix}$$

Längswiderstand: $U_1=U_2+R(-I_2)$, $I_1=-I_2$. Querleitwert: $U_1=U_2$, $I_1=G\,U_2+(-I_2)$. Für $R=0$ und $G=0$ entsteht die Einheitsmatrix.

**Pi-Schaltung**

$$A_{11}=1+\frac{G_3}{G_2},\qquad A_{21}=G_1+G_3+\frac{G_1G_3}{G_2},\qquad A_{12}=\frac{1}{G_2},\qquad A_{22}=1+\frac{G_1}{G_2}$$

Querleitwerte $G_1$, $G_3$, Längsleitwert $G_2$. $A_{11}$ folgt aus dem Spannungsteiler aus $G_2$ und $G_3$ bei offenem Ausgang.
::::

::::lernkarten
:::karte begriff Kettenform
Was ist die Kettenform eines Zweitors, und welche Größen sind darin die Ursachen?
---
Die Form der Zweitorgleichungen, die die Eingangsgrößen durch die Ausgangsgrößen $U_2$ und $-I_2$ ausdrückt: $U_1=A_{11}U_2+A_{12}(-I_2)$, $I_1=A_{21}U_2+A_{22}(-I_2)$. Sie heißt auch A-Form.
--- falsch
Die Form, die die Ausgangsgrößen durch die Eingangsgrößen ausdrückt: $U_2=A_{11}U_1+A_{12}I_1$, $-I_2=A_{21}U_1+A_{22}I_1$, weil das Signal vom Eingang zum Ausgang läuft und die Quelle am Eingang sitzt.
--- falsch
Die Form mit $U_2$ und $I_2$ als Ursachen: $U_1=A_{11}U_2+A_{12}I_2$, $I_1=A_{21}U_2+A_{22}I_2$. Ein Minus ist hier nicht nötig, weil $I_2$ ohnehin in das Zweitor zeigt.
--- falsch
Die Form $U_1=A_{11}U_2+A_{12}(-I_2)$, $I_1=A_{21}U_2+A_{22}(-I_2)$ mit $U_1$ und $I_1$ als Ursachen, weil am Eingang die Quelle sitzt, die alles antreibt.
:::
:::karte zusammenhang Kettenform für hintereinandergeschaltete Zweitore
Warum eignet sich die Kettenform für Zweitore, die hintereinandergeschaltet sind?
---
Die Ausgangsgrößen des ersten Zweitors sind genau die Eingangsgrößen des zweiten. Drückt eine Form die Eingangsgrößen durch die Ausgangsgrößen aus, rechnet man von der Last Stufe für Stufe zur Quelle zurück.
--- falsch
Weil in einer Kette durch alle Zweitore derselbe Strom fließt. Die Kettenform fasst deshalb alle Zweitore der Kette in einer gemeinsamen Z-Matrix zusammen, die man nur einmal für die ganze Kette bestimmen muss.
--- falsch
Weil sie die Ausgangsgrößen durch die Eingangsgrößen beschreibt. So kann man an der Quelle starten und Stufe für Stufe vorwärts bis zur Last rechnen, in Richtung des Signals.
--- falsch
Weil sie nur für die letzte Stufe einer Kette gilt, an der die Last hängt. Die übrigen Stufen rechnet man mit der Z-Form und setzt deren Ergebnisse in die Kettenform ein.
:::
:::karte zusammenhang Das Minus vor dem Ausgangsstrom
Warum steht in der Kettenform $-I_2$ statt $I_2$?
---
Weil $I_2$ in das Zweitor zeigt und der Strom, der es verlässt, deshalb $-I_2$ ist. Genau dieser Strom fließt in das nächste Zweitor hinein und ist dort der Eingangsstrom.
--- falsch
Weil der Ausgangsstrom im Zweitor seine Richtung umkehrt. Ohne das Minus wäre die Kettenform nur für Verstärker gültig, nicht für passive Zweitore aus Widerständen.
--- falsch
Weil die Kettenform rückwärts rechnet. Ströme, die man von der Last zur Quelle zurückverfolgt, bekommen dabei immer ein negatives Vorzeichen.
--- falsch
Weil die Last einen Teil des Stroms in das Zweitor zurückschickt. Dieser Rückstrom muss vom Ausgangsstrom abgezogen werden, daher das Minus.
:::
:::karte formel A-Parameter aus Versuchen am Ausgang
Wie sind die A-Parameter durch Versuche am Ausgang festgelegt?
---
$A_{11}=\left.\frac{U_1}{U_2}\right|_{I_2=0}$ und $A_{21}=\left.\frac{I_1}{U_2}\right|_{I_2=0}$ bei offenem Ausgang, $A_{12}=\left.-\frac{U_1}{I_2}\right|_{U_2=0}$ und $A_{22}=\left.-\frac{I_1}{I_2}\right|_{U_2=0}$ bei kurzgeschlossenem Ausgang.
--- falsch
$A_{11}=\left.\frac{U_2}{U_1}\right|_{I_2=0}$ und $A_{21}=\left.\frac{U_2}{I_1}\right|_{I_2=0}$ bei offenem Ausgang, $A_{12}=\left.-\frac{I_2}{U_1}\right|_{U_2=0}$ und $A_{22}=\left.-\frac{I_2}{I_1}\right|_{U_2=0}$ bei kurzgeschlossenem Ausgang.
--- falsch
$A_{11}$ und $A_{21}$ bei kurzgeschlossenem Ausgang, $A_{12}$ und $A_{22}$ bei offenem Ausgang, jeweils als Quotient aus einer Eingangsgröße und einer Ausgangsgröße, ohne Minuszeichen.
--- falsch
$A_{12}=\left.\frac{U_1}{I_2}\right|_{U_2=0}$ und $A_{22}=\left.\frac{I_1}{I_2}\right|_{U_2=0}$ ohne Minus, $A_{11}$ und $A_{21}$ bei offenem Ausgang; das Minus steht nur in den Gleichungen, nicht in den Parametern.
:::
:::karte begriff A-Parameter
Wie heißen die vier A-Parameter, und welche Einheiten haben sie?
---
$A_{11}$ reziproke Leerlaufspannungsübersetzung, $A_{21}$ Leerlaufübertragungsleitwert, $A_{12}$ Kurzschluss-Übertragungswiderstand, $A_{22}$ reziproke Kurzschlussstromübersetzung, alle vorwärts. $A_{11}$, $A_{22}$ ohne Einheit, $A_{12}$ in $\Omega$, $A_{21}$ in S.
--- falsch
$A_{11}$ reziproke Leerlaufspannungsübersetzung, $A_{12}$ Leerlaufübertragungsleitwert, $A_{21}$ Kurzschluss-Übertragungswiderstand, $A_{22}$ reziproke Kurzschlussstromübersetzung, alle vorwärts. $A_{11}$, $A_{22}$ ohne Einheit, $A_{12}$ in S, $A_{21}$ in $\Omega$.
--- falsch
Alle vier heißen Kettenwiderstände und haben die Einheit $\Omega$, weil die Kettenform wie die Impedanzform Spannungen aus Strömen berechnet und Widerstände dafür die passende Einheit haben.
--- falsch
$A_{11}$ ist die Leerlaufspannungsübersetzung, Ausgang durch Eingang, $A_{22}$ die Kurzschlussstromübersetzung, ebenso Ausgang durch Eingang; beide ohne Einheit, $A_{12}$ hat $\Omega$, $A_{21}$ hat S.
:::
:::karte zusammenhang Reziproke Übersetzung beim Dämpfungsglied
Was bedeutet das Wort reziprok in den Namen von $A_{11}$ und $A_{22}$, und warum hat ein Dämpfungsglied $A_{11}>1$?
---
Reziprok heißt: Eingang durch Ausgang, der Kehrwert der gewohnten Übersetzung. Ein Dämpfungsglied gibt am offenen Ausgang weniger Spannung ab, als am Eingang liegt, also ist $U_1$ durch $U_2$ größer als eins.
--- falsch
Reziprok heißt: Ausgang durch Eingang. Ein Dämpfungsglied hat $A_{11}>1$, weil sein Ausgang ohne Last mehr Spannung zeigt als sein Eingang, denn im Leerlauf staut sich die Spannung am offenen Tor ein wenig auf.
--- falsch
Reziprok heißt: mit negativem Vorzeichen, wegen des Minus vor $I_2$. Ein Dämpfungsglied hat $A_{11}>1$, weil es mehr Strom aufnimmt, als es an seinem Ausgang wieder abgibt.
--- falsch
Reziprok heißt: Eingang durch Ausgang. Ein Dämpfungsglied hat trotzdem $A_{11}<1$, weil es die Spannung auf dem Weg vom Eingang zum Ausgang verkleinert.
:::
:::karte begriff Kette
Was ist eine Kette von Zweitoren, und wie erhält man ihre Kettenmatrix?
---
Hintereinandergeschaltete Zweitore: Der Ausgang des einen speist den Eingang des nächsten. Ihre Kettenmatrix ist $\mathbf A=\mathbf A'\mathbf A''$; die Reihenfolge zählt, das Zweitor an der Quelle steht links.
--- falsch
Zweitore, die hintereinandergeschaltet sind. Die Kettenmatrix ist die Summe $\mathbf A=\mathbf A'+\mathbf A''$; die Reihenfolge ist gleichgültig, weil die Addition von Matrizen vertauschbar ist.
--- falsch
Zweitore, die hintereinandergeschaltet sind. Die Kettenmatrix ist das Produkt $\mathbf A=\mathbf A''\mathbf A'$; das Zweitor an der Last steht links, weil die Kettenform von der Last aus zur Quelle zurückrechnet.
--- falsch
Zweitore, deren Eingänge alle an derselben Quelle liegen. Die Kettenmatrix ist das Produkt $\mathbf A=\mathbf A'\mathbf A''$; die Reihenfolge ist gleichgültig, weil alle dieselbe Spannung haben.
:::
:::karte herleitung Kette als Matrixprodukt
Leite aus den Kettengleichungen zweier verbundener Zweitore her, dass die Kette die Kettenmatrix $\mathbf A'\mathbf A''$ hat.
---
Die Verbindung erzwingt $U_2'=U_1''$ und $-I_2'=I_1''$, weil Ausgang des ersten und Eingang des zweiten dieselben Klemmen teilen und der Strom, der das erste verlässt, in das zweite fließt.
---
Für das erste Zweitor gilt $\begin{pmatrix}U_1'\\I_1'\end{pmatrix}=\mathbf A'\begin{pmatrix}U_2'\\-I_2'\end{pmatrix}$, weil das seine Kettenform ist.
---
Mit der Verbindung wird daraus $\mathbf A'\begin{pmatrix}U_1''\\I_1''\end{pmatrix}$, weil die Ausgangsspalte des ersten gleich der Eingangsspalte des zweiten ist.
---
Die Kettenform des zweiten ersetzt diese Spalte durch $\mathbf A''\begin{pmatrix}U_2''\\-I_2''\end{pmatrix}$, also ergibt sich $\mathbf A'\mathbf A''\begin{pmatrix}U_2''\\-I_2''\end{pmatrix}$, weil das zweite Zweitor seine Eingangsgrößen ebenso durch seine Ausgangsgrößen ausdrückt.
:::
:::karte formel Längswiderstand und Querleitwert
Wie lauten die Kettenmatrizen der einfachsten Bausteine, eines Längswiderstands $R$ und eines Querleitwerts $G$?
---
$\mathbf A_R=\begin{pmatrix}1&R\\0&1\end{pmatrix}$, weil $U_1=U_2+R(-I_2)$ und $I_1=-I_2$ gilt; $\mathbf A_G=\begin{pmatrix}1&0\\G&1\end{pmatrix}$, weil $U_1=U_2$ und $I_1=G\,U_2+(-I_2)$ gilt.
--- falsch
$\mathbf A_R=\begin{pmatrix}1&0\\mathbb{R}&1\end{pmatrix}$, weil $I_1=R\,U_2+(-I_2)$ gilt; $\mathbf A_G=\begin{pmatrix}1&G\\0&1\end{pmatrix}$, weil am Querleitwert $U_1=U_2+G(-I_2)$ und $I_1=-I_2$ gilt.
--- falsch
$\mathbf A_R=\begin{pmatrix}R&0\\0&1\end{pmatrix}$ und $\mathbf A_G=\begin{pmatrix}1&0\\0&G\end{pmatrix}$, weil jeder Baustein nur eine Größe verändert, der Längswiderstand die Spannung und der Querleitwert den Strom.
--- falsch
$\mathbf A_R=\begin{pmatrix}1&R\\0&1\end{pmatrix}$, weil $U_1=U_2+R(-I_2)$ gilt, und $\mathbf A_G=\begin{pmatrix}1&G\\0&1\end{pmatrix}$, weil am Querleitwert ebenso $U_1=U_2+G(-I_2)$ gilt.
:::
:::karte zusammenhang Kette belastet sich selbst
Warum hat eine Kette aus zwei gleichen T-Zweitoren $A_{11}=5{,}56$ und nicht $1{,}75^2=3{,}06$?
---
Das zweite T belastet das erste. Die Zwischenspannung sinkt dadurch unter den Leerlaufwert, den ein einzelnes T hätte. Das Matrixprodukt erfasst diese Belastung, das bloße Quadrieren von $A_{11}$ nicht.
--- falsch
Weil im Matrixprodukt auch $A_{12}$ und $A_{21}$ vorkommen. Diese Rechenregel hat keine physikalische Bedeutung, sie folgt allein aus der Mathematik der Matrizen und lässt sich nicht anschaulich deuten.
--- falsch
Weil zwischen den beiden T-Zweitoren eine zusätzliche Verbindungsleitung liegt, deren Widerstand die Spannung ein weiteres Mal teilt und so die Übersetzung erhöht.
--- falsch
Weil das zweite T rückwärts betrieben wird und rückwärts eine größere Übersetzung hat. Vorwärts betrieben hätte es wieder genau 1,75, und das Quadrat wäre richtig.
:::
:::karte zusammenhang Warum rückwärts gerechnet wird
Das Signal läuft vom Eingang zum Ausgang. Warum rechnet die Kettenform trotzdem von der Last zur Quelle zurück?
---
Weil sie eine Rechenvorschrift ist, kein Ablauf. Die Last legt mit $U_2$ auch $-I_2$ fest, und von dort liefert jede Stufe ohne Gleichungssystem die Größen davor. Physikalisch stellt sich alles gemeinsam ein.
--- falsch
Weil sich die Energie in einem Zweitor rückwärts ausbreitet, von der Last zur Quelle. Das Signal läuft vorwärts, die Energie aber zurück, und die Kettenform folgt dem Weg der Energie durch alle Stufen von hinten nach vorn.
--- falsch
Weil das Signal am Ausgang zuerst ankommt und sich die Eingangsgrößen erst danach einstellen, wenn die Last ihren Strom aufgenommen hat und das Zweitor zur Ruhe kommt.
--- falsch
Weil die Quelle meist unbekannt ist. Ist sie bekannt, muss man vorwärts rechnen, sonst erhält man mit der Kettenform falsche Werte für die Größen am Ausgang.
:::
::::
