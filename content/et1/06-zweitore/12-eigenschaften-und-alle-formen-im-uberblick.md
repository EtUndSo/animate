---
title: Stufe 10: Eigenschaften und alle Formen im Überblick
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1161200
summary: Die vier Zahlen verraten mehr als das Verhalten an den Toren.
tags: umkehrbar, aktiv, passiv, Kleinsignalbetrieb
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Die vier Zahlen verraten mehr als das Verhalten an den Toren. Diese Stufe liest daran drei Eigenschaften ab: Wirkt das Zweitor in beide Richtungen gleich? Wirkt es überhaupt zurück? Kann es Leistung gewinnen? Zum Schluss stehen alle Formen nebeneinander.
:::

**Die Idee.** Ein Widerstand kennt keine Richtung, sein Strom hängt nur von der Spannungsdifferenz seiner beiden Enden ab. Darum wirkt ein Netzwerk aus Widerständen von Tor 1 nach Tor 2 genauso stark wie umgekehrt: Vertauscht man Ursache und Wirkungsort, bleibt der Quotient gleich. Eine gesteuerte Quelle hat dagegen eine Richtung. Sie wirkt von der Steuergröße auf ihren Ausgang, nie zurück. Nur sie kann die Symmetrie brechen. Sie allein kann auch Energie von außen zuführen.

:::definition Definition 10.1 (Umkehrbar, rückwirkungsfrei, aktiv)
<span class="anker" id="satz-10-1"></span>

Ein Zweitor heißt __umkehrbar__ (auch reziprok, übertragungssymmetrisch), wenn gleiche Ursache in beiden Richtungen gleiche Wirkung zeigt. Es heißt rückwirkungsfrei, wenn der Eingang nicht vom Ausgang abhängt:

<span class="anker" id="gl-10-1"></span>
<span class="anker" id="gl-10-2"></span>
$$\begin{aligned} \text{umkehrbar:}\quad&Z_{12}=Z_{21},\quad Y_{12}=Y_{21},\quad H_{12}=-H_{21},\quad\det\mathbf A=1,\\ \text{rückwirkungsfrei:}\quad&Z_{12}=0,\quad Y_{12}=0,\quad H_{12}=0,\quad\det\mathbf A=0. \end{aligned} \tag{10.1|10.2}$$

Die vom Zweitor aufgenommene Leistung ist mit $P_1=U_1I_1$ und der abgegebenen Leistung $P_2=-U_2I_2$

<span class="anker" id="gl-10-3"></span>
$$P=P_1-P_2=U_1I_1+U_2I_2=Y_{11}U_1^2+(Y_{12}+Y_{21})U_1U_2+Y_{22}U_2^2. \tag{10.3}$$

Das Zweitor ist __aktiv__, wenn in einem Betriebszustand $P<0$ möglich ist, und __passiv__, wenn immer $P\ge0$ gilt.
:::

⁠**So liest man das:** Erzeugt 1 A in Tor 1 am offenen Tor 2 eine Spannung, erzeugt beim umkehrbaren Zweitor 1 A in Tor 2 am offenen Tor 1 dieselbe Spannung (Abb. [12](#abb-12)). Das ist $Z_{21}=Z_{12}$. In den Knotengleichungen ([Kapitel 8](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren/maschenstrom-und-knotenpotential.html)) trägt jeder Widerstand seinen Leitwert an zwei gespiegelten Stellen ein, deshalb bleibt die Matrix symmetrisch. Umkehrbar heißt nicht spiegelgleich: Das T-Zweitor hat $Z_{11}\neq Z_{22}$ und ist trotzdem umkehrbar. Weil der vierte Parameter festliegt, hat ein umkehrbares Zweitor nur drei freie Parameter, passend zu den drei Elementen von T und $\pi$. Es lässt sich stets durch eine quellenfreie T- oder $\pi$-Schaltung nachbilden, die Elementwerte dürfen dabei negativ sein. Rückwirkungsfrei sind ebenfalls drei Zahlen frei: Eingangswiderstand, Ausgangswiderstand, Steuergröße. Das ist die Grundform des Verstärkers. Die Bedingungen für $\mathbf A$ und $\mathbf H$ folgen aus den Umrechnungen unten. In [(10.3)](#gl-10-3) steht das Minus bei $P_2$, weil $I_2$ hineinzeigt. Die letzte Form entsteht durch Einsetzen von [(5.1)](admittanzform-und-kurzschlussversuch.html#gl-5-1).

:::abbildung et1/k6umkehr 12
Links: T-Zweitor. 100 mA ergeben am offenen anderen Tor in beiden Richtungen 2 V, obwohl $R_\mathrm{a}\neq R_\mathrm{c}$. Rechts: Verstärkermodell. 1 µ A an Tor 1 ergibt $-2$ V an Tor 2, 1 µ A an Tor 2 ergibt 0 V an Tor 1.
:::

::::beispiel
Das T-Zweitor nimmt $P_1=7{,}75\,\mathrm{V}\cdot250\,\mathrm{mA}=1{,}9375$ W auf und gibt $P_2=3\,\mathrm{V}\cdot50\,\mathrm{mA}=0{,}15$ W ab. Die Differenz $P=1{,}7875$ W ist genau die Wärme in den Widerständen: $0{,}9375+0{,}8+0{,}05$ W. Jeder Widerstand nimmt $I^2R\geq0$ auf, deshalb ist ein Zweitor aus Widerständen immer passiv. Das gilt auch mit Kondensatoren und Spulen. Passive Zweitore dürfen sogar gesteuerte Quellen enthalten, entscheidend ist allein $P$. Das Verstärkermodell nimmt $P_1=20\,\mathrm{mV}\cdot10\,\mu\text{A}=0{,}2$ µ W auf und gibt $P_2=4\,\mathrm{V}\cdot0{,}8\,\mathrm{mA}=3{,}2$ mW an die Last, 16 000-mal mehr. Es ist aktiv. Die Energie kommt nicht aus dem Eingangssignal, sondern aus einer Hilfsquelle zur Stromversorgung, die im Zweitor-Modell nicht auftaucht. Dieses Modell gilt für kleine Signale um einen festen Gleichstromzustand (__Kleinsignalbetrieb__, [Kapitel 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).
::::

⁠**Grenzfälle:** Für $U_1=U_2=0$ ist $P=0$. Ein Zweitor aus idealen Drähten hat $P=0$ in jedem Zustand, es ist passiv, und nichts geht verloren.

:::ltspice Woher die Leistung kommt
⁠**Zeichnen:** Quelle `voltage` mit `20m` von `1` nach Masse, `Rein` mit `2k` von `1` nach Masse. Die gesteuerte Stromquelle `g` mit `50m`: Ausgang von `2` nach Masse, Steuereingang von `1` nach Masse. `res` mit `20k` und `res` mit `5k` von `2` nach Masse. Der Wert ist $Y_{21}=H_{21}/H_{11}$.

⁠**Direktiven:** `.op`, `.meas op Ua FIND V(2)`, `.meas op Pein PARAM V(1)*I(Rein)`, `.meas op Plast PARAM V(2)*V(2)/5000`, `.meas op Pg PARAM V(2)*I(G1)`.

⁠**Was du siehst:** $\mathtt{Ua}=-4$ V, `Pein` $=0{,}2$ µ W, `Plast` $=3{,}2$ mW, `Pg` $=-4$ mW. Die gesteuerte Quelle gibt 4 mW ab, davon 3,2 mW an die Last, der Rest erwärmt die 20 k$\Omega$. Stelle für Aufgabe [10](#aufg-10)(b) die Werte `10m`, `1k`, `50m`, `50k` und `10k` ein: $\mathtt{Ua}=-4{,}17$ V.
:::

**Alle Formen im Überblick.** Dieselben vier Größen, vier Wahlen der Ursachen:

| Form | Ursachen | Wirkungen | T-Zweitor |
|---|---|---|---|
| Z (Widerstandsmatrix) | $I_1$, $I_2$ | $U_1$, $U_2$ | $Z_{11}=35\,\Omega$, $Z_{12}=Z_{21}=20\,\Omega$, $Z_{22}=40\,\Omega$ |
| Y (Leitwertmatrix) | $U_1$, $U_2$ | $I_1$, $I_2$ | $Y_{11}=40$ mS, $Y_{12}=Y_{21}=-20$ mS, $Y_{22}=35$ mS |
| H (Reihenparallelmatrix) | $I_1$, $U_2$ | $U_1$, $I_2$ | $H_{11}=25\,\Omega$, $H_{12}=0{,}5$, $H_{21}=-0{,}5$, $H_{22}=25$ mS |
| A (Kettenmatrix) | $U_2$, $-I_2$ | $U_1$, $I_1$ | $A_{11}=1{,}75$, $A_{12}=50\,\Omega$, $A_{21}=50$ mS, $A_{22}=2$ |

Die Umrechnung entsteht jedes Mal durch Auflösen der beiden Gleichungen nach den neuen Größen. Zum Nachschlagen, jeweils die gesuchte Matrix aus den drei anderen:

$$\mathbf Z=\begin{pmatrix}\frac{Y_{22}}{\det\mathbf Y}&\frac{-Y_{12}}{\det\mathbf Y}\\[3pt]\frac{-Y_{21}}{\det\mathbf Y}&\frac{Y_{11}}{\det\mathbf Y}\end{pmatrix} =\begin{pmatrix}\frac{\det\mathbf H}{H_{22}}&\frac{H_{12}}{H_{22}}\\[3pt]\frac{-H_{21}}{H_{22}}&\frac{1}{H_{22}}\end{pmatrix} =\begin{pmatrix}\frac{A_{11}}{A_{21}}&\frac{\det\mathbf A}{A_{21}}\\[3pt]\frac{1}{A_{21}}&\frac{A_{22}}{A_{21}}\end{pmatrix},$$

$$\mathbf Y=\begin{pmatrix}\frac{Z_{22}}{\det\mathbf Z}&\frac{-Z_{12}}{\det\mathbf Z}\\[3pt]\frac{-Z_{21}}{\det\mathbf Z}&\frac{Z_{11}}{\det\mathbf Z}\end{pmatrix} =\begin{pmatrix}\frac{1}{H_{11}}&\frac{-H_{12}}{H_{11}}\\[3pt]\frac{H_{21}}{H_{11}}&\frac{\det\mathbf H}{H_{11}}\end{pmatrix} =\begin{pmatrix}\frac{A_{22}}{A_{12}}&\frac{-\det\mathbf A}{A_{12}}\\[3pt]\frac{-1}{A_{12}}&\frac{A_{11}}{A_{12}}\end{pmatrix},$$

$$\mathbf H=\begin{pmatrix}\frac{\det\mathbf Z}{Z_{22}}&\frac{Z_{12}}{Z_{22}}\\[3pt]\frac{-Z_{21}}{Z_{22}}&\frac{1}{Z_{22}}\end{pmatrix} =\begin{pmatrix}\frac{1}{Y_{11}}&\frac{-Y_{12}}{Y_{11}}\\[3pt]\frac{Y_{21}}{Y_{11}}&\frac{\det\mathbf Y}{Y_{11}}\end{pmatrix} =\begin{pmatrix}\frac{A_{12}}{A_{22}}&\frac{\det\mathbf A}{A_{22}}\\[3pt]\frac{-1}{A_{22}}&\frac{A_{21}}{A_{22}}\end{pmatrix},$$

$$\mathbf A=\begin{pmatrix}\frac{Z_{11}}{Z_{21}}&\frac{\det\mathbf Z}{Z_{21}}\\[3pt]\frac{1}{Z_{21}}&\frac{Z_{22}}{Z_{21}}\end{pmatrix} =\begin{pmatrix}\frac{-Y_{22}}{Y_{21}}&\frac{-1}{Y_{21}}\\[3pt]\frac{-\det\mathbf Y}{Y_{21}}&\frac{-Y_{11}}{Y_{21}}\end{pmatrix} =\begin{pmatrix}\frac{-\det\mathbf H}{H_{21}}&\frac{-H_{11}}{H_{21}}\\[3pt]\frac{-H_{22}}{H_{21}}&\frac{-1}{H_{21}}\end{pmatrix}.$$

Aus $\mathbf A$ folgt die Bedingung in [(10.1)](#gl-10-1) und [(10.2)](#gl-10-2): Mit der ersten Zeile ist $Z_{12}=\det\mathbf A/A_{21}$ und $Z_{21}=1/A_{21}$, also $\det\mathbf A=Z_{12}/Z_{21}$. Das ist 1 bei Umkehrbarkeit und 0 bei Rückwirkungsfreiheit. Ebenso ist $Z_{12}=H_{12}/H_{22}$ und $Z_{21}=-H_{21}/H_{22}$, daher $H_{12}=-H_{21}$.

:::frage Nicht umkehrbar heißt also aktiv?
Nein. Umkehrbarkeit ist eine Aussage über Symmetrie, Aktivität eine über Leistung. Beides hängt zwar an gesteuerten Quellen, ist aber nicht dasselbe. Aufgabe [10](#aufg-10)(d) zeigt ein Zweitor mit $Z_{12}\neq Z_{21}$, das nie Leistung gewinnt.
:::

:::aufgabe Aufgabe 10 ★★ Eigenschaften ablesen
<span class="anker" id="aufg-10"></span>

Prüfe für jedes Zweitor: Ist es umkehrbar? Rückwirkungsfrei? Aktiv oder passiv?

<ol class="al">

<li>

$Y_{11}=2$ mS, $Y_{12}=Y_{21}=-1$ mS, $Y_{22}=3$ mS. Tipp: Zeichne die $\pi$-Schaltung.

</li>

<li>

$H_{11}=1$ k$\Omega$, $H_{12}=0$, $H_{21}=50$, $H_{22}=20$ µ S, Last 10 k$\Omega$, $U_1=10$ mV.

</li>

<li>

$A_{11}=2$, $A_{12}=30\,\Omega$, $A_{21}=0{,}1$ S, $A_{22}=2$.

</li>

<li>

$Z_{11}=Z_{22}=10\,\Omega$, $Z_{12}=5\,\Omega$, $Z_{21}=-5\,\Omega$. Berechne dazu $P$ aus $U_1I_1+U_2I_2$.

</li>

</ol>

:::loesung
(a) Umkehrbar, $Y_{12}=Y_{21}$, nicht rückwirkungsfrei. $\pi$-Schaltung mit $G_2=1$ mS, $G_1=1$ mS, $G_3=2$ mS, alle positiv: Widerstände, also passiv.

(b) $H_{12}=0$: rückwirkungsfrei, nicht umkehrbar ($H_{21}\neq-H_{12}$). $I_1=10$ µ A, der Ausgang treibt 0,5 mA in $50\,\text{k}\Omega\parallel10\,\text{k}\Omega=8{,}33$ k$\Omega$, $U_2=-4{,}17$ V. $P_1=0{,}1$ µ W, $P_2=U_2^2/R_\mathrm{L}=1{,}74$ mW. Aktiv.

(c) $\det\mathbf A=4-3=1$: umkehrbar, nicht rückwirkungsfrei. Mit $Z_{11}=Z_{22}=20\,\Omega$, $Z_{12}=Z_{21}=10\,\Omega$ ein T aus positiven Widerständen 10, 10, 10 $\Omega$: passiv, wegen $A_{11}=A_{22}$ sogar spiegelgleich.

(d) $Z_{12}=5\,\Omega\neq Z_{21}=-5\,\Omega$: nicht umkehrbar, nicht rückwirkungsfrei. $P=I_1(10I_1+5I_2)+I_2(-5I_1+10I_2)=10\,\Omega\,(I_1^2+I_2^2)\geq0$: passiv. Die gemischten Glieder heben sich auf. Das ist ein nicht umkehrbares, aber passives Zweitor.
:::
:::

::::formelsammlung
**Umkehrbar**

$$Z_{12}=Z_{21},\quad Y_{12}=Y_{21},\quad H_{12}=-H_{21},\quad\det\mathbf A=1$$

Gleiche Ursache zeigt in beiden Richtungen gleiche Wirkung (auch reziprok, übertragungssymmetrisch). Nur drei freie Parameter; stets durch eine quellenfreie T- oder $\pi$-Schaltung nachzubilden, die Elementwerte dürfen negativ sein. Umkehrbar heißt nicht spiegelgleich.

**Rückwirkungsfrei**

$$Z_{12}=0,\quad Y_{12}=0,\quad H_{12}=0,\quad\det\mathbf A=0$$

Der Eingang hängt nicht vom Ausgang ab. Frei bleiben Eingangswiderstand, Ausgangswiderstand und Steuergröße: die Grundform des Verstärkers.

**Leistung**

$$P=P_1-P_2=U_1I_1+U_2I_2=Y_{11}U_1^2+(Y_{12}+Y_{21})U_1U_2+Y_{22}U_2^2$$

Aufgenommen $P_1=U_1I_1$, abgegeben $P_2=-U_2I_2$; das Minus steht, weil $I_2$ hineinzeigt. Aktiv, wenn in einem Betriebszustand $P<0$ möglich ist; passiv, wenn immer $P\ge0$ gilt. Ein Zweitor aus Widerständen ist passiv.

**Bedingung in der Kettenform**

$$\det\mathbf A=Z_{12}/Z_{21}$$

Aus $Z_{12}=\det\mathbf A/A_{21}$ und $Z_{21}=1/A_{21}$: 1 bei Umkehrbarkeit, 0 bei Rückwirkungsfreiheit. Ebenso ist $Z_{12}=H_{12}/H_{22}$ und $Z_{21}=-H_{21}/H_{22}$, daher $H_{12}=-H_{21}$.

**Z-Matrix aus Y, H und A**

$$\mathbf Z=\begin{pmatrix}\frac{Y_{22}}{\det\mathbf Y}&\frac{-Y_{12}}{\det\mathbf Y}\\[3pt]\frac{-Y_{21}}{\det\mathbf Y}&\frac{Y_{11}}{\det\mathbf Y}\end{pmatrix} =\begin{pmatrix}\frac{\det\mathbf H}{H_{22}}&\frac{H_{12}}{H_{22}}\\[3pt]\frac{-H_{21}}{H_{22}}&\frac{1}{H_{22}}\end{pmatrix} =\begin{pmatrix}\frac{A_{11}}{A_{21}}&\frac{\det\mathbf A}{A_{21}}\\[3pt]\frac{1}{A_{21}}&\frac{A_{22}}{A_{21}}\end{pmatrix}$$

Z: Ursachen $I_1$, $I_2$. Jede Umrechnung entsteht durch Auflösen der beiden Gleichungen nach den neuen Größen.

**Y-Matrix aus Z, H und A**

$$\mathbf Y=\begin{pmatrix}\frac{Z_{22}}{\det\mathbf Z}&\frac{-Z_{12}}{\det\mathbf Z}\\[3pt]\frac{-Z_{21}}{\det\mathbf Z}&\frac{Z_{11}}{\det\mathbf Z}\end{pmatrix} =\begin{pmatrix}\frac{1}{H_{11}}&\frac{-H_{12}}{H_{11}}\\[3pt]\frac{H_{21}}{H_{11}}&\frac{\det\mathbf H}{H_{11}}\end{pmatrix} =\begin{pmatrix}\frac{A_{22}}{A_{12}}&\frac{-\det\mathbf A}{A_{12}}\\[3pt]\frac{-1}{A_{12}}&\frac{A_{11}}{A_{12}}\end{pmatrix}$$

Y: Ursachen $U_1$, $U_2$.

**H-Matrix aus Z, Y und A**

$$\mathbf H=\begin{pmatrix}\frac{\det\mathbf Z}{Z_{22}}&\frac{Z_{12}}{Z_{22}}\\[3pt]\frac{-Z_{21}}{Z_{22}}&\frac{1}{Z_{22}}\end{pmatrix} =\begin{pmatrix}\frac{1}{Y_{11}}&\frac{-Y_{12}}{Y_{11}}\\[3pt]\frac{Y_{21}}{Y_{11}}&\frac{\det\mathbf Y}{Y_{11}}\end{pmatrix} =\begin{pmatrix}\frac{A_{12}}{A_{22}}&\frac{\det\mathbf A}{A_{22}}\\[3pt]\frac{-1}{A_{22}}&\frac{A_{21}}{A_{22}}\end{pmatrix}$$

H: Ursachen $I_1$, $U_2$.

**A-Matrix aus Z, Y und H**

$$\mathbf A=\begin{pmatrix}\frac{Z_{11}}{Z_{21}}&\frac{\det\mathbf Z}{Z_{21}}\\[3pt]\frac{1}{Z_{21}}&\frac{Z_{22}}{Z_{21}}\end{pmatrix} =\begin{pmatrix}\frac{-Y_{22}}{Y_{21}}&\frac{-1}{Y_{21}}\\[3pt]\frac{-\det\mathbf Y}{Y_{21}}&\frac{-Y_{11}}{Y_{21}}\end{pmatrix} =\begin{pmatrix}\frac{-\det\mathbf H}{H_{21}}&\frac{-H_{11}}{H_{21}}\\[3pt]\frac{-H_{22}}{H_{21}}&\frac{-1}{H_{21}}\end{pmatrix}$$

A: Ursachen $U_2$, $-I_2$.
::::

::::lernkarten
:::karte begriff umkehrbar
Wann heißt ein Zweitor umkehrbar, und welche anderen Namen hat diese Eigenschaft?
---
Wenn gleiche Ursache in beiden Richtungen gleiche Wirkung zeigt: 1 A in Tor 1 erzeugt am offenen Tor 2 dieselbe Spannung wie 1 A in Tor 2 am offenen Tor 1. Es heißt auch reziprok oder übertragungssymmetrisch.
--- falsch
Wenn man Eingang und Ausgang vertauschen kann, ohne dass sich an den Toren irgendetwas ändert, also auch $Z_{11}=Z_{22}$ gilt und beide Seiten gleich aussehen. Es heißt auch spiegelgleich oder übertragungssymmetrisch.
--- falsch
Wenn es Energie in beide Richtungen übertragen kann, von Tor 1 nach Tor 2 und auch wieder zurück. Es heißt auch reziprok, weil die Energie den umgekehrten Weg nehmen kann.
--- falsch
Wenn sich seine Matrix invertieren lässt, also die Determinante nicht null ist. Es heißt auch reziprok, weil man jederzeit zur inversen Matrix übergehen kann.
:::
:::karte formel Umkehrbarkeit in allen Formen
Woran erkennt man in den vier Parameterformen, dass ein Zweitor umkehrbar ist, und wie viele Parameter sind dann frei?
---
$Z_{12}=Z_{21}$, $Y_{12}=Y_{21}$, $H_{12}=-H_{21}$, $\det\mathbf A=1$. Weil der vierte Parameter festliegt, sind nur drei frei, passend zu den drei Elementen von T und Pi.
--- falsch
$Z_{12}=Z_{21}$, $Y_{12}=Y_{21}$, $H_{12}=H_{21}$, $\det\mathbf A=1$. In jeder Form sind die beiden Transfergrößen gleich, und es bleiben drei freie Parameter übrig.
--- falsch
$Z_{12}=Z_{21}$, $Y_{12}=Y_{21}$, $H_{12}=-H_{21}$, $\det\mathbf A=0$. Weil der vierte Parameter festliegt, sind nur drei frei, passend zu den drei Elementen von T und Pi.
--- falsch
$Z_{11}=Z_{22}$, $Y_{11}=Y_{22}$, $H_{11}=H_{22}$, $A_{11}=A_{22}$. Die beiden Diagonalelemente jeder Form sind gleich, und es bleiben drei freie Parameter übrig.
:::
:::karte formel Rückwirkungsfreiheit in allen Formen
Woran erkennt man in den vier Parameterformen, dass ein Zweitor rückwirkungsfrei ist, und welche Zahlen bleiben frei?
---
$Z_{12}=0$, $Y_{12}=0$, $H_{12}=0$, $\det\mathbf A=0$. Frei bleiben drei Zahlen: Eingangswiderstand, Ausgangswiderstand und Steuergröße. Das ist die Grundform des Verstärkers.
--- falsch
$Z_{21}=0$, $Y_{21}=0$, $H_{21}=0$, $\det\mathbf A=0$. Frei bleiben drei Zahlen: Eingangswiderstand, Ausgangswiderstand und Steuergröße. Das ist die Grundform des Verstärkers.
--- falsch
$Z_{12}=0$, $Y_{12}=0$, $H_{12}=0$, $\det\mathbf A=1$. Frei bleiben drei Zahlen, passend zu den drei Elementen einer T- oder Pi-Schaltung aus Widerständen.
--- falsch
$Z_{12}=Z_{21}=0$, $Y_{12}=Y_{21}=0$, $H_{12}=H_{21}=0$. Dann wirkt weder der Ausgang auf den Eingang noch der Eingang auf den Ausgang, und beide Seiten sind getrennt.
:::
:::karte zusammenhang Warum Widerstandsnetze umkehrbar sind
Warum ist jedes Netzwerk aus Widerständen umkehrbar, und welches Bauteil kann diese Symmetrie brechen?
---
Ein Widerstand kennt keine Richtung, sein Strom hängt nur von der Spannungsdifferenz seiner Enden ab; vertauscht man Ursache und Wirkungsort, bleibt der Quotient gleich. Nur eine gesteuerte Quelle hat eine Richtung.
--- falsch
Weil ein Widerstandsnetz immer spiegelbildlich aufgebaut ist. Die Symmetrie bricht, sobald die Widerstände auf beiden Seiten verschieden sind, etwa mit $R_\mathrm{a}\neq R_\mathrm{c}$ im T-Zweitor, denn dann wirkt eine Seite stärker als die andere.
--- falsch
Weil Widerstände nur Energie aufnehmen und keine abgeben. Die Symmetrie bricht jedes Bauteil, das Energie abgibt, also jede Quelle, auch eine unabhängige Quelle mit festem Wert.
--- falsch
Weil der Strom durch einen Widerstand in beide Richtungen gleich groß ist. Die Symmetrie brechen erst Kondensatoren und Spulen, weil sie Energie speichern und verzögert wieder abgeben.
:::
:::karte zusammenhang Umkehrbar ist nicht spiegelgleich
Ist das T-Zweitor mit $R_\mathrm{a}=15\,\Omega$, $R_\mathrm{b}=20\,\Omega$ und $R_\mathrm{c}=20\,\Omega$ umkehrbar, obwohl seine beiden Seiten verschieden sind?
---
Ja. 100 mA ergeben am offenen anderen Tor in beiden Richtungen 2 V, weil $Z_{12}=Z_{21}=20\,\Omega$ ist. Umkehrbar heißt nicht spiegelgleich, $Z_{11}\neq Z_{22}$ ist erlaubt.
--- falsch
Nein. Umkehrbar verlangt, dass beide Tore denselben Leerlaufwiderstand zeigen; mit 35 $\Omega$ an Tor 1 und 40 $\Omega$ an Tor 2 ist diese Bedingung hier nicht erfüllt.
--- falsch
Nein. 100 mA in Tor 1 ergeben am offenen Tor 2 eine andere Spannung als 100 mA in Tor 2 am offenen Tor 1, nämlich 2 V und 4 V.
--- falsch
Ja, aber nur wegen seiner Masseleitung. Ohne Masseleitung wäre eine Schaltung mit verschiedenen Längswiderständen nicht umkehrbar.
:::
:::karte zusammenhang Nachbildung durch T oder Pi
Warum lässt sich jedes umkehrbare Zweitor durch eine T- oder Pi-Schaltung ohne Quellen nachbilden?
---
Weil der vierte Parameter festliegt, hat es nur drei freie Parameter, passend zu den drei Elementen von T und Pi. Die Elementwerte dürfen dabei negativ sein.
--- falsch
Weil jedes umkehrbare Zweitor aus genau drei Widerständen besteht. Mehr Bauteile würden die Umkehrbarkeit zerstören, weniger reichen nicht für die Parameter.
--- falsch
Weil die Determinante eines umkehrbaren Zweitors eins ist. T und Pi sind die einzigen Schaltungen, deren Matrizen genau diese Determinante haben.
--- falsch
Weil es nur drei freie Parameter hat. Die Elementwerte sind dabei stets positiv, weil ein umkehrbares Zweitor immer auch passiv ist.
:::
:::karte formel Leistung des Zweitors
Wie groß ist die vom Zweitor aufgenommene Leistung $P$, ausgedrückt durch die Torgrößen und durch die Y-Parameter?
---
$P=P_1-P_2=U_1I_1+U_2I_2=Y_{11}U_1^2+(Y_{12}+Y_{21})U_1U_2+Y_{22}U_2^2$, mit $P_1=U_1I_1$ und der abgegebenen Leistung $P_2=-U_2I_2$. Das Minus bei $P_2$ steht, weil $I_2$ hineinzeigt.
--- falsch
$P=P_1+P_2=U_1I_1-U_2I_2=Y_{11}U_1^2-(Y_{12}+Y_{21})U_1U_2+Y_{22}U_2^2$, mit $P_1=U_1I_1$ und $P_2=U_2I_2$. Das Minus steht, weil die abgegebene Leistung das Zweitor verlässt.
--- falsch
$P=U_1I_1+U_2I_2=Y_{11}U_1^2+Y_{12}Y_{21}U_1U_2+Y_{22}U_2^2$, mit $P_1=U_1I_1$ und der abgegebenen Leistung $P_2=-U_2I_2$. Das Minus bei $P_2$ steht, weil $I_2$ hineinzeigt.
--- falsch
$P=P_1-P_2=U_1I_1+U_2I_2=Y_{11}U_1^2+(Y_{12}+Y_{21})U_1U_2+Y_{22}U_2^2$, mit $P_2=U_2I_2$. Das Minus steht, weil die Last die abgegebene Leistung aufnimmt.
:::
:::karte begriff aktiv und passiv
Wann heißt ein Zweitor aktiv, wann passiv?
---
Aktiv, wenn in einem Betriebszustand $P<0$ möglich ist, das Zweitor also mehr Leistung abgibt, als es aufnimmt. Passiv, wenn immer $P\ge0$ gilt.
--- falsch
Aktiv, wenn es eine gesteuerte Quelle enthält. Passiv, wenn es nur aus Widerständen, Kondensatoren und Spulen besteht, gleich wie groß $P$ ist.
--- falsch
Aktiv, wenn es nicht umkehrbar ist, also $Z_{12}\neq Z_{21}$ gilt. Passiv, wenn $Z_{12}=Z_{21}$ gilt, weil nur gesteuerte Quellen die Symmetrie brechen.
--- falsch
Aktiv, wenn immer $P>0$ gilt, das Zweitor also ständig Leistung aufnimmt und umsetzt. Passiv, wenn $P=0$ ist und nichts umgesetzt wird.
:::
:::karte zusammenhang Zweitore aus Widerständen sind passiv
Warum ist ein Zweitor aus Widerständen immer passiv?
---
Jeder Widerstand nimmt $I^2R\geq0$ auf, also kann die Summe $P$ nie negativ werden. Beim T-Zweitor im Betrieb ist $P=1{,}7875$ W genau die Wärme in den drei Widerständen.
--- falsch
Weil es umkehrbar ist. Jedes umkehrbare Zweitor ist passiv, und jedes nicht umkehrbare Zweitor ist aktiv, weil es dafür eine gesteuerte Quelle enthalten muss.
--- falsch
Weil sein Ausgangsstrom kleiner ist als sein Eingangsstrom. Ein Zweitor ist passiv, sobald der Betrag von $I_2$ kleiner ist als der Betrag von $I_1$.
--- falsch
Weil es keine Masseleitung braucht. Nur Zweitore mit Masseleitung können Leistung aus der Erde beziehen und so mehr abgeben, als sie aufnehmen.
:::
:::karte zusammenhang Woher die Leistung des Verstärkers kommt
Das Verstärkermodell gibt an die Last 16 000-mal mehr Leistung ab, als es am Eingang aufnimmt. Woher kommt diese Leistung?
---
Nicht aus dem Eingangssignal, sondern aus einer Hilfsquelle zur Stromversorgung, die im Zweitor-Modell nicht auftaucht. Das Modell ist deshalb aktiv.
--- falsch
Aus dem Eingangssignal: Die gesteuerte Quelle sammelt dessen Leistung über die Zeit und gibt sie gebündelt an die Last ab. Das Modell ist deshalb passiv.
--- falsch
Aus der Last: Sie gibt Energie an die gesteuerte Quelle zurück, die diese verstärkt wieder an die Last weiterreicht, wie in einem Kreislauf.
--- falsch
Aus dem Widerstand von 20 k$\Omega$ am Ausgang, der als Energiespeicher wirkt und den Strom der gesteuerten Quelle antreibt.
:::
:::karte begriff Kleinsignalbetrieb
Was versteht man unter Kleinsignalbetrieb, für den das lineare Verstärkermodell gilt?
---
Den Betrieb mit kleinen Signalen um einen festen Gleichstromzustand. Für solche kleinen Änderungen gilt das lineare Zweitor-Modell des Verstärkers.
--- falsch
Den Betrieb mit sehr kleinen Gleichströmen, bei denen der Verstärker keine Hilfsquelle braucht. Nur dann gilt das lineare Modell, weil die Kennlinien bei so kleinen Strömen gerade sind.
--- falsch
Den Betrieb eines kleinen, also leistungsschwachen Verstärkers. Große Verstärker beschreibt man dagegen mit nichtlinearen Modellen.
--- falsch
Den Betrieb ohne Last. Ohne Last bleiben die Signale am Ausgang klein, und das lineare Modell gilt, solange kein Strom entnommen wird.
:::
:::karte zusammenhang Nicht umkehrbar heißt nicht aktiv
Ist ein Zweitor, das nicht umkehrbar ist, automatisch aktiv?
---
Nein. Umkehrbarkeit ist eine Aussage über Symmetrie, Aktivität eine über Leistung. Mit $Z_{11}=Z_{22}=10\,\Omega$, $Z_{12}=5\,\Omega$, $Z_{21}=-5\,\Omega$ ist $P=10\,\Omega\,(I_1^2+I_2^2)\geq0$: nicht umkehrbar, aber passiv.
--- falsch
Ja. Nur gesteuerte Quellen brechen die Symmetrie, und jede gesteuerte Quelle führt dem Zweitor Energie von außen zu; ein nicht umkehrbares Zweitor gibt deshalb in jedem Betrieb mehr ab, als es aufnimmt.
--- falsch
Ja, denn ein passives Zweitor besteht nur aus Widerständen, und Netzwerke aus Widerständen sind immer umkehrbar. Was nicht umkehrbar ist, muss deshalb eine Quelle enthalten und Leistung gewinnen.
--- falsch
Nein, aber nur, wenn es zusätzlich rückwirkungsfrei ist. Ein nicht umkehrbares Zweitor mit Rückwirkung ist immer aktiv, weil die Rückwirkung Leistung an den Eingang zurückliefert.
:::
:::karte herleitung Umkehrbarkeit in der Kettenform
Leite aus der Umrechnung der Kettenmatrix in die Z-Matrix her, warum ein umkehrbares Zweitor $\det\mathbf A=1$ und ein rückwirkungsfreies $\det\mathbf A=0$ hat.
---
Die Umrechnung ergibt $Z_{12}=\det\mathbf A/A_{21}$ und $Z_{21}=1/A_{21}$, weil man die Kettengleichungen nach den Spannungen auflöst.
---
Daraus folgt $\det\mathbf A=Z_{12}/Z_{21}$, weil man beide Ausdrücke durcheinander teilt und sich $A_{21}$ kürzt.
---
Bei Umkehrbarkeit ist $Z_{12}=Z_{21}$, also $\det\mathbf A=1$, weil der Quotient zweier gleicher Zahlen eins ist.
---
Bei Rückwirkungsfreiheit ist $Z_{12}=0$, also $\det\mathbf A=0$, weil dann der Zähler null ist.
---
Ebenso ist $Z_{12}=H_{12}/H_{22}$ und $Z_{21}=-H_{21}/H_{22}$; aus $Z_{12}=Z_{21}$ wird deshalb $H_{12}=-H_{21}$, weil sich $H_{22}$ kürzt.
:::
::::
