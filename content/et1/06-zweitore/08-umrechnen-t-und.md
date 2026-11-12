---
title: Stufe 6: Umrechnen, T und $\pi$
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1160800
summary: Z-Form und Y-Form beschreiben dasselbe Zweitor.
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Z-Form und Y-Form beschreiben dasselbe Zweitor. Diese Stufe zeigt, wie man von der einen zur anderen kommt, und wann eine Form gar nicht existiert.
:::

**Die Idee.** Y-Form und Z-Form sind dieselben zwei Gleichungen. Die eine ist nach den Spannungen aufgelöst, die andere nach den Strömen. Der Übergang ist also das Lösen eines Gleichungssystems, und das leistet die inverse Matrix aus dem Abschnitt „Von Grund auf“.

:::satz Satz 6.1 (Umrechnung Z und Y)
<span class="anker" id="satz-6-1"></span>

Die Leitwert- und die Widerstandsmatrix sind zueinander invers, $\mathbf Y\cdot\mathbf Z=\mathbf 1$:

<span class="anker" id="gl-6-1"></span>
$$\mathbf Y=\mathbf Z^{-1}=\frac{1}{\det\mathbf Z}\begin{pmatrix}Z_{22}&-Z_{12}\\-Z_{21}&Z_{11}\end{pmatrix},\qquad \mathbf Z=\mathbf Y^{-1}=\frac{1}{\det\mathbf Y}\begin{pmatrix}Y_{22}&-Y_{12}\\-Y_{21}&Y_{11}\end{pmatrix} \tag{6.1}$$

mit $\det\mathbf Z=Z_{11}Z_{22}-Z_{12}Z_{21}$ und $\det\mathbf Y=Y_{11}Y_{22}-Y_{12}Y_{21}$.
:::

⁠**So liest man das:** Es wird die ganze Matrix invertiert, nicht jede Zahl einzeln. Zu jedem Element gehört der ganze Nenner, deshalb hängt jeder Y-Parameter von allen Z-Parametern ab. **Gültigkeit:** Die Determinante darf nicht null sein.

:::herleitung Zwei Wege zur Inversen
⁠**Mit Matrizen.** Aus $\mathbf I=\mathbf Y\mathbf U$ und $\mathbf U=\mathbf Z\mathbf I$ folgt $\mathbf I=\mathbf Y\mathbf Z\,\mathbf I$ für jedes $\mathbf I$, also $\mathbf Y\mathbf Z=\mathbf 1$.

⁠**Mit Kurzschlussversuchen am Z-Ersatzschaltbild.** Bei $U_2=0$ gilt $Z_{21}I_1=-Z_{22}I_2$, also $I_2=-\frac{Z_{21}}{Z_{22}}I_1$ und $U_1=\bigl(Z_{11}-Z_{12}\frac{Z_{21}}{Z_{22}}\bigr)I_1$. Damit ist

$$Y_{11}=\frac{I_1}{U_1}=\frac{Z_{22}}{Z_{11}Z_{22}-Z_{12}Z_{21}},\qquad Y_{21}=\frac{I_2}{U_1}=-\frac{Z_{21}}{Z_{11}Z_{22}-Z_{12}Z_{21}}.$$

Bei $U_1=0$ gilt $-Z_{11}I_1=Z_{12}I_2$, also $I_1=-\frac{Z_{12}}{Z_{11}}I_2$ und $U_2=\bigl(Z_{22}-Z_{21}\frac{Z_{12}}{Z_{11}}\bigr)I_2$. Das ergibt

$$Y_{12}=-\frac{Z_{12}}{Z_{11}Z_{22}-Z_{12}Z_{21}},\qquad Y_{22}=\frac{Z_{11}}{Z_{11}Z_{22}-Z_{12}Z_{21}}.$$
:::

**T und $\pi$.** Die Z-Matrix der T-Schaltung aus Stufe [3](impedanzform-und-leerlaufversuch.html#stufe-3) lässt sich mit [(6.1)](#gl-6-1) invertieren, die Y-Matrix der $\pi$-Schaltung liest man direkt aus Kurzschlussversuchen ab. Mit $D=R_\mathrm{a}R_\mathrm{b}+R_\mathrm{a}R_\mathrm{c}+R_\mathrm{b}R_\mathrm{c}=\det\mathbf Z$ und den Leitwerten $G_1$, $G_3$ quer, $G_2$ längs gilt

<span class="anker" id="gl-6-2"></span>
$$\mathbf Y_\mathrm{T}=\frac1D\begin{pmatrix}R_\mathrm{b}+R_\mathrm{c}&-R_\mathrm{b}\\-R_\mathrm{b}&R_\mathrm{a}+R_\mathrm{b}\end{pmatrix},\qquad \mathbf Y_\pi=\begin{pmatrix}G_1+G_2&-G_2\\-G_2&G_2+G_3\end{pmatrix}. \tag{6.2}$$

Setzt man beide gleich, entstehen $G_2=-Y_{12}$, $G_1=Y_{11}+Y_{12}$ und $G_3=Y_{22}+Y_{21}$. Für $G_3=0$ wird aus $\mathbf Y_\pi$ das Paar $I_1=(G_1+G_2)U_1-G_2U_2$, $I_2=-G_2U_1+G_2U_2$. Das ist die Stern-Dreieck-Transformation aus [Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html): T ist der Stern, $\pi$ das Dreieck. Die Beschreibung mit Z-Parametern führt von selbst auf die T-Schaltung, die mit Y-Parametern auf die dazu duale $\pi$-Schaltung. Umgekehrt gehört zu jedem Zweitor mit $Z_{12}=Z_{21}$ eine T- und eine $\pi$-Ersatzschaltung ohne Quellen (Stufe [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10)).

:::abbildung et1/k6tpi 8
Zwei Schaltungen, dasselbe Zweitor. Links die T-Schaltung mit 15, 20 und 20 $\Omega$, rechts die gleichwertige $\pi$-Schaltung mit 50, 50 und 66,7 $\Omega$. Beide haben $\det\mathbf Z=1000\,\Omega^2$. An den Toren lassen sie sich durch keine Messung unterscheiden.
:::

::::beispiel
Es ist $\det\mathbf Z=35\cdot40\,\Omega^2-20\cdot20\,\Omega^2=1000\,\Omega^2$, also

$$\mathbf Y=\frac{1}{1000\,\Omega^2}\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\Omega=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS},$$

genau das Ergebnis der Kurzschlussversuche. Die $\pi$-Schaltung hat $G_2=20$ mS, $G_1=40\,\mathrm{mS}-20\,\mathrm{mS}=20$ mS, $G_3=15$ mS, also 50 $\Omega$, 50 $\Omega$ und 66,7 $\Omega$. Mit derselben Quelle und Last ergibt sie wieder 7,75 V und 3 V.
::::

⁠**Grenzfälle: Nicht jede Form existiert.** Ein Längswiderstand $R$ und ein Querwiderstand $R$, jeweils allein zwischen den Toren, haben

$$\mathbf Y_\text{längs}=G\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad\mathbf Z_\text{quer}=R\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

Beide Determinanten sind null. Der Längswiderstand hat keine Z-Form: Dort gilt immer $I_2=-I_1$, die Ströme sind nicht frei wählbar, also taugen sie nicht als Ursachen. Der Querwiderstand hat keine Y-Form, weil immer $U_1=U_2$ gilt. Dasselbe trifft die ideale stromgesteuerte Stromquelle: Ihre Ströme sind fest gekoppelt.

:::frage Warum ist $Y_{11}$ positiv, $Y_{21}$ aber negativ?
Das liegt an den Zählpfeilen. Bei $U_2=0$ treibt eine positive Spannung an Tor 1 einen Strom hinein, $Y_{11}>0$. Dieser Strom kommt am anderen Tor heraus, gezählt wird aber hinein. Deshalb sind die Transfer-Leitwerte passiver Schaltungen wie T und $\pi$ negativ.
:::

:::aufgabe Aufgabe 6 ★ Hin und zurück
<span class="anker" id="aufg-6"></span>

Ein Zweitor hat $Z_{11}=20\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$, $Z_{22}=55\,\Omega$.

<ol class="al">

<li>

Berechne $\mathbf Y$.

</li>

<li>

Bestimme die Widerstände der T- und der $\pi$-Schaltung.

</li>

<li>

Schreibe $\mathbf Y$ eines Längswiderstands von 100 $\Omega$ auf. Warum scheitert $\mathbf Z=\mathbf Y^{-1}$?

</li>

</ol>

:::loesung
(a) $\det\mathbf Z=20\cdot55\,\Omega^2-10\cdot10\,\Omega^2=1000\,\Omega^2$, also $Y_{11}=55$ mS, $Y_{12}=Y_{21}=-10$ mS, $Y_{22}=20$ mS. (b) T: $R_\mathrm{b}=10\,\Omega$, $R_\mathrm{a}=10\,\Omega$, $R_\mathrm{c}=45\,\Omega$. $\pi$: $G_2=10$ mS, $G_1=45$ mS, $G_3=10$ mS, also 100 $\Omega$ längs, 22,2 $\Omega$ und 100 $\Omega$ quer. (c) $Y_{11}=Y_{22}=10$ mS, $Y_{12}=Y_{21}=-10$ mS, $\det\mathbf Y=0$. Es gibt keine Inverse, weil immer $I_2=-I_1$ gilt und die Ströme nicht frei wählbar sind.
:::
:::

::::formelsammlung
**Umrechnung zwischen Z und Y**

$$\mathbf Y=\mathbf Z^{-1}=\frac{1}{\det\mathbf Z}\begin{pmatrix}Z_{22}&-Z_{12}\\-Z_{21}&Z_{11}\end{pmatrix},\qquad \mathbf Z=\mathbf Y^{-1}=\frac{1}{\det\mathbf Y}\begin{pmatrix}Y_{22}&-Y_{12}\\-Y_{21}&Y_{11}\end{pmatrix}$$

Mit $\det\mathbf Z=Z_{11}Z_{22}-Z_{12}Z_{21}$ und $\det\mathbf Y=Y_{11}Y_{22}-Y_{12}Y_{21}$; es gilt $\mathbf Y\cdot\mathbf Z=\mathbf 1$. Die ganze Matrix wird invertiert, nicht jede Zahl einzeln. Die Determinante darf nicht null sein.

**T- und Pi-Schaltung**

$$\mathbf Y_\mathrm{T}=\frac1D\begin{pmatrix}R_\mathrm{b}+R_\mathrm{c}&-R_\mathrm{b}\\-R_\mathrm{b}&R_\mathrm{a}+R_\mathrm{b}\end{pmatrix},\qquad \mathbf Y_\pi=\begin{pmatrix}G_1+G_2&-G_2\\-G_2&G_2+G_3\end{pmatrix}$$

$D=R_\mathrm{a}R_\mathrm{b}+R_\mathrm{a}R_\mathrm{c}+R_\mathrm{b}R_\mathrm{c}=\det\mathbf Z$. $G_1$, $G_3$ sind die Querleitwerte, $G_2$ der Längsleitwert. T entspricht dem Stern, $\pi$ dem Dreieck.

**Pi-Ersatzschaltung aus der Y-Matrix**

$$G_2=-Y_{12},\qquad G_1=Y_{11}+Y_{12},\qquad G_3=Y_{22}+Y_{21}$$

Aus dem Gleichsetzen mit $\mathbf Y_\pi$. Zu jedem Zweitor mit $Z_{12}=Z_{21}$ gehört eine T- und eine $\pi$-Ersatzschaltung ohne Quellen.

**Längswiderstand und Querwiderstand allein**

$$\mathbf Y_\text{längs}=G\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad\mathbf Z_\text{quer}=R\begin{pmatrix}1&1\\1&1\end{pmatrix}$$

Beide Determinanten sind null. Der Längswiderstand hat keine Z-Form, weil immer $I_2=-I_1$ gilt und die Ströme nicht frei wählbar sind; der Querwiderstand hat keine Y-Form, weil immer $U_1=U_2$ gilt. Auch bei der idealen stromgesteuerten Stromquelle sind die Ströme fest gekoppelt.
::::

::::lernkarten
:::karte formel Umrechnung zwischen Z und Y
Wie rechnet man die Z-Matrix eines Zweitors in seine Y-Matrix um, und wann geht das nicht?
---
$\mathbf Y=\mathbf Z^{-1}=\frac{1}{\det\mathbf Z}\begin{pmatrix}Z_{22}&-Z_{12}\\-Z_{21}&Z_{11}\end{pmatrix}$ mit $\det\mathbf Z=Z_{11}Z_{22}-Z_{12}Z_{21}$. Es wird die ganze Matrix invertiert; die Determinante darf nicht null sein.
--- falsch
$Y_{11}=1/Z_{11}$, $Y_{12}=1/Z_{12}$, $Y_{21}=1/Z_{21}$, $Y_{22}=1/Z_{22}$. Man kehrt jede Zahl einzeln um, weil Leitwerte Kehrwerte von Widerständen sind; das geht nicht, wenn ein Z-Parameter null ist.
--- falsch
$\mathbf Y=\frac{1}{\det\mathbf Z}\begin{pmatrix}Z_{11}&-Z_{12}\\-Z_{21}&Z_{22}\end{pmatrix}$ mit $\det\mathbf Z=Z_{11}Z_{22}-Z_{12}Z_{21}$. Die Diagonale bleibt an ihrem Platz; die Determinante darf nicht null sein.
--- falsch
$\mathbf Y=\mathbf Z^{-1}=\frac{1}{\det\mathbf Z}\begin{pmatrix}Z_{22}&-Z_{12}\\-Z_{21}&Z_{11}\end{pmatrix}$ mit $\det\mathbf Z=Z_{11}Z_{22}+Z_{12}Z_{21}$. Es wird die ganze Matrix invertiert; das geht immer.
:::
:::karte zusammenhang Warum Y die Inverse von Z ist
Warum ist die Y-Matrix eines Zweitors die Inverse seiner Z-Matrix?
---
Y-Form und Z-Form sind dieselben zwei Gleichungen, einmal nach den Strömen, einmal nach den Spannungen aufgelöst. Aus $\mathbf I=\mathbf Y\mathbf U$ und $\mathbf U=\mathbf Z\mathbf I$ folgt $\mathbf I=\mathbf Y\mathbf Z\,\mathbf I$ für jedes $\mathbf I$, also $\mathbf Y\mathbf Z=\mathbf 1$.
--- falsch
Weil Leitwerte die Kehrwerte von Widerständen sind. Die Inverse einer Matrix ist die Matrix aus den Kehrwerten ihrer Elemente, also gilt für jedes Zweitor $\mathbf Y=\mathbf Z^{-1}$.
--- falsch
Weil die Y-Parameter aus Kurzschlussversuchen und die Z-Parameter aus Leerlaufversuchen stammen. Kurzschluss und Leerlauf sind entgegengesetzte Zustände, also sind die beiden Matrizen zueinander invers.
--- falsch
Weil beide Matrizen symmetrisch sind. Nur für symmetrische Matrizen gilt $\mathbf Y\mathbf Z=\mathbf 1$; bei allen anderen Zweitoren gibt es keine Umrechnung zwischen den beiden Formen.
:::
:::karte formel Längswiderstand und Querwiderstand allein
Wie lauten die Y-Matrix eines Längswiderstands $R$ und die Z-Matrix eines Querwiderstands $R$, jeweils allein zwischen den Toren, und welche Form fehlt ihnen?
---
$\mathbf Y_\text{längs}=G\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ und $\mathbf Z_\text{quer}=R\begin{pmatrix}1&1\\1&1\end{pmatrix}$. Beide Determinanten sind null: Der Längswiderstand hat keine Z-Form, der Querwiderstand keine Y-Form.
--- falsch
$\mathbf Y_\text{längs}=G\begin{pmatrix}1&1\\1&1\end{pmatrix}$ und $\mathbf Z_\text{quer}=R\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$. Beide Determinanten sind null, deshalb hat keiner der beiden eine Z-Form oder eine Y-Form.
--- falsch
$\mathbf Y_\text{längs}=\begin{pmatrix}G&0\\0&G\end{pmatrix}$ und $\mathbf Z_\text{quer}=\begin{pmatrix}R&0\\0&R\end{pmatrix}$. Beide Determinanten sind von null verschieden, also haben beide jede der vier Formen.
--- falsch
$\mathbf Y_\text{längs}=G\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ und $\mathbf Z_\text{quer}=R\begin{pmatrix}1&1\\1&1\end{pmatrix}$. Beide Determinanten sind null: Der Längswiderstand hat keine Y-Form, der Querwiderstand keine Z-Form.
:::
:::karte zusammenhang Wann eine Form fehlt
Woran liegt es, dass ein einzelner Längswiderstand zwischen den Toren keine Z-Form hat?
---
Bei ihm gilt immer $I_2=-I_1$. Die Ströme sind nicht frei wählbar und taugen deshalb nicht als Ursachen; rechnerisch ist $\det\mathbf Y=0$, die Y-Matrix lässt sich nicht invertieren.
--- falsch
Weil bei ihm immer $U_1=U_2$ gilt. Die Spannungen sind dann nicht frei wählbar, deshalb taugen auch die Ströme nicht als Ursachen, und die Z-Matrix hat die Determinante null.
--- falsch
Weil sein Widerstand zu klein ist. Erst ab einigen Ohm ergeben die Leerlaufversuche messbare Spannungen und damit eine vollständige Z-Matrix; darunter bleibt sie unbestimmt.
--- falsch
Weil er keinen Querwiderstand hat. Z-Parameter sind nur für Schaltungen mit Querzweig festgelegt, und aus demselben Grund fehlt ihm auch die Y-Form, also jede Beschreibung.
:::
:::karte formel Y-Matrix der Pi-Schaltung
Wie lautet die Y-Matrix einer Pi-Schaltung mit den Querleitwerten $G_1$ am Eingang, $G_3$ am Ausgang und dem Längsleitwert $G_2$, und wie findet man sie?
---
$\mathbf Y_\pi=\begin{pmatrix}G_1+G_2&-G_2\\-G_2&G_2+G_3\end{pmatrix}$. Man liest sie direkt aus Kurzschlussversuchen ab: Bei kurzgeschlossenem Tor 2 liegen $G_1$ und $G_2$ am Eingang, der Strom durch $G_2$ verlässt das Zweitor an Tor 2.
--- falsch
$\mathbf Y_\pi=\begin{pmatrix}G_1&G_2\\G_2&G_3\end{pmatrix}$. Jeder Querleitwert gehört zu seinem eigenen Tor, und der Längsleitwert verknüpft als Transfergröße die beiden Seiten des Zweitors miteinander.
--- falsch
$\mathbf Y_\pi=\begin{pmatrix}G_1+G_2&G_2\\G_2&G_2+G_3\end{pmatrix}$. Die Transfergrößen sind positiv, weil der Längsleitwert den Strom von Tor zu Tor leitet und dieser Strom in das andere Tor hineinfließt, wie die Zählpfeile es verlangen.
--- falsch
$\mathbf Y_\pi=\begin{pmatrix}G_1+G_2&-G_2\\-G_2&G_2+G_3\end{pmatrix}$. Man erhält sie nur über die Z-Matrix, weil sich Leitwerte nicht direkt aus Versuchen an den Toren ablesen lassen, sondern nur Widerstände.
:::
:::karte formel Y-Matrix der T-Schaltung
Wie lautet die Y-Matrix der T-Schaltung mit $R_\mathrm{a}$, $R_\mathrm{b}$ und $R_\mathrm{c}$, und was steht im Nenner?
---
$\mathbf Y_\mathrm{T}=\frac1D\begin{pmatrix}R_\mathrm{b}+R_\mathrm{c}&-R_\mathrm{b}\\-R_\mathrm{b}&R_\mathrm{a}+R_\mathrm{b}\end{pmatrix}$ mit $D=R_\mathrm{a}R_\mathrm{b}+R_\mathrm{a}R_\mathrm{c}+R_\mathrm{b}R_\mathrm{c}=\det\mathbf Z$. Sie entsteht durch Invertieren der Z-Matrix der T-Schaltung.
--- falsch
$\mathbf Y_\mathrm{T}=\begin{pmatrix}1/(R_\mathrm{a}+R_\mathrm{b})&1/R_\mathrm{b}\\1/R_\mathrm{b}&1/(R_\mathrm{b}+R_\mathrm{c})\end{pmatrix}$, die Kehrwerte der Elemente der Z-Matrix. Ein gemeinsamer Nenner kommt dabei nicht vor.
--- falsch
$\mathbf Y_\mathrm{T}=\frac1D\begin{pmatrix}R_\mathrm{a}+R_\mathrm{b}&-R_\mathrm{b}\\-R_\mathrm{b}&R_\mathrm{b}+R_\mathrm{c}\end{pmatrix}$ mit $D=R_\mathrm{a}R_\mathrm{b}+R_\mathrm{a}R_\mathrm{c}+R_\mathrm{b}R_\mathrm{c}$. Beim Invertieren bleibt die Diagonale der Z-Matrix an ihrem Platz.
--- falsch
$\mathbf Y_\mathrm{T}=\frac1D\begin{pmatrix}R_\mathrm{b}+R_\mathrm{c}&-R_\mathrm{b}\\-R_\mathrm{b}&R_\mathrm{a}+R_\mathrm{b}\end{pmatrix}$ mit $D=R_\mathrm{a}+R_\mathrm{b}+R_\mathrm{c}$, der Summe aller drei Widerstände, wie beim Umfangswiderstand eines Dreiecks.
:::
:::karte formel Pi-Ersatzschaltung aus der Y-Matrix
Wie bestimmt man aus der Y-Matrix eines Zweitors die Leitwerte der gleichwertigen Pi-Schaltung, und für welche Zweitore gibt es sie ohne Quellen?
---
$G_2=-Y_{12}$, $G_1=Y_{11}+Y_{12}$ und $G_3=Y_{22}+Y_{21}$, aus dem Gleichsetzen mit $\mathbf Y_\pi$. Ohne Quellen gibt es sie für jedes Zweitor mit $Z_{12}=Z_{21}$.
--- falsch
$G_2=Y_{12}$, $G_1=Y_{11}-Y_{12}$ und $G_3=Y_{22}-Y_{21}$, weil die Transfergrößen direkt den Längsleitwert angeben. Ohne Quellen gibt es sie für jedes Zweitor.
--- falsch
$G_1=Y_{11}$, $G_2=-Y_{12}$ und $G_3=Y_{22}$, weil die Diagonalelemente direkt die Querleitwerte angeben. Ohne Quellen gibt es sie für jedes Zweitor mit $Z_{12}=Z_{21}$.
--- falsch
$G_2=-Y_{12}$, $G_1=Y_{11}+Y_{12}$ und $G_3=Y_{22}+Y_{21}$, aus dem Gleichsetzen mit $\mathbf Y_\pi$. Ohne Quellen gibt es sie nur für Zweitore mit $\det\mathbf Y=0$.
:::
:::karte zusammenhang T und Pi als Stern und Dreieck
Wie hängen T-Schaltung und Pi-Schaltung mit der Stern-Dreieck-Transformation zusammen, und lassen sich gleichwertige T- und Pi-Schaltungen an den Toren unterscheiden?
---
T ist der Stern, Pi das Dreieck. Die Z-Parameter führen von selbst auf die T-Schaltung, die Y-Parameter auf die dazu duale Pi-Schaltung. Gleichwertige T- und Pi-Schaltungen lassen sich an den Toren durch keine Messung unterscheiden.
--- falsch
T ist das Dreieck, Pi der Stern. Die Z-Parameter führen auf die Pi-Schaltung, die Y-Parameter auf die T-Schaltung. An den Toren unterscheiden sich gleichwertige Schaltungen deshalb schon durch ihre Leerlaufspannungen am offenen Ausgang.
--- falsch
Gar nicht: Die Stern-Dreieck-Transformation gilt nur für drei Klemmen, ein Zweitor hat aber vier. T- und Pi-Schaltung sind deshalb nie gleichwertig, sondern nur ähnlich aufgebaut.
--- falsch
T ist der Stern, Pi das Dreieck, aber die Gleichwertigkeit gilt nur, solange keine Last angeschlossen ist. Im Betrieb verteilen sich die Ströme verschieden, und die Torspannungen weichen ab.
:::
:::karte zusammenhang Vorzeichen der Transferleitwerte
Warum ist bei passiven Schaltungen wie T und Pi der Parameter $Y_{11}$ positiv, $Y_{21}$ aber negativ?
---
Das liegt an den Zählpfeilen. Bei $U_2=0$ treibt eine positive Spannung an Tor 1 einen Strom hinein, also ist $Y_{11}>0$. Dieser Strom kommt am anderen Tor heraus, gezählt wird aber hinein.
--- falsch
Weil der Strom im Zweitor Energie verliert. Der Ausgangsstrom wird dadurch kleiner als null, sobald irgendwelche Widerstände zwischen den beiden Toren liegen und dort Wärme entsteht.
--- falsch
Weil $Y_{21}$ der Kehrwert von $Z_{21}$ mit umgekehrtem Vorzeichen ist. Ein positiver Widerstand ergibt deshalb immer einen negativen Transferleitwert.
--- falsch
Weil der Kurzschlussdraht die Stromrichtung im Zweitor umkehrt. Ohne Kurzschluss an Tor 2 wäre $Y_{21}$ ebenso positiv wie $Y_{11}$.
:::
:::karte herleitung Y aus Z mit Kurzschlussversuchen
Leite aus den Gleichungen der Z-Form mit einem Kurzschlussversuch an Tor 2 die Parameter $Y_{11}$ und $Y_{21}$ her.
---
Bei kurzgeschlossenem Tor 2 ist $U_2=0$, also $Z_{21}I_1=-Z_{22}I_2$, weil die zweite Gleichung $U_2=Z_{21}I_1+Z_{22}I_2$ dann null ergibt.
---
Daraus folgt $I_2=-\frac{Z_{21}}{Z_{22}}I_1$, weil man durch $Z_{22}$ teilt.
---
Eingesetzt in die erste Gleichung wird $U_1=\bigl(Z_{11}-Z_{12}\frac{Z_{21}}{Z_{22}}\bigr)I_1$, weil $I_2$ jetzt durch $I_1$ ausgedrückt ist.
---
Also ist $Y_{11}=\frac{I_1}{U_1}=\frac{Z_{22}}{Z_{11}Z_{22}-Z_{12}Z_{21}}$, weil man den Kehrwert der Klammer bildet und mit $Z_{22}$ erweitert.
---
Ebenso ist $Y_{21}=\frac{I_2}{U_1}=-\frac{Z_{21}}{Z_{11}Z_{22}-Z_{12}Z_{21}}$, weil $I_2$ den Faktor $-\frac{Z_{21}}{Z_{22}}$ vor $I_1$ trägt.
:::
::::
