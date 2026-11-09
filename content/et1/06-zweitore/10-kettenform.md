---
title: Stufe 8: Kettenform
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Zweitore
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
