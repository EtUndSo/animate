---
title: Stufe 10: Eigenschaften und alle Formen im Überblick
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Zweitore
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

⁠**So liest man das:** Erzeugt 1 A in Tor 1 am offenen Tor 2 eine Spannung, erzeugt beim umkehrbaren Zweitor 1 A in Tor 2 am offenen Tor 1 dieselbe Spannung (Abb. [12](#abb-12)). Das ist $Z_{21}=Z_{12}$. In den Knotengleichungen ([Teil 8](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren/maschenstrom-und-knotenpotential.html)) trägt jeder Widerstand seinen Leitwert an zwei gespiegelten Stellen ein, deshalb bleibt die Matrix symmetrisch. Umkehrbar heißt nicht spiegelgleich: Das T-Zweitor hat $Z_{11}\neq Z_{22}$ und ist trotzdem umkehrbar. Weil der vierte Parameter festliegt, hat ein umkehrbares Zweitor nur drei freie Parameter, passend zu den drei Elementen von T und $\pi$. Es lässt sich stets durch eine quellenfreie T- oder $\pi$-Schaltung nachbilden, die Elementwerte dürfen dabei negativ sein. Rückwirkungsfrei sind ebenfalls drei Zahlen frei: Eingangswiderstand, Ausgangswiderstand, Steuergröße. Das ist die Grundform des Verstärkers. Die Bedingungen für $\mathbf A$ und $\mathbf H$ folgen aus den Umrechnungen unten. In [(10.3)](#gl-10-3) steht das Minus bei $P_2$, weil $I_2$ hineinzeigt. Die letzte Form entsteht durch Einsetzen von [(5.1)](admittanzform-und-kurzschlussversuch.html#gl-5-1).

:::abbildung et1/k6umkehr 12
Links: T-Zweitor. 100 mA ergeben am offenen anderen Tor in beiden Richtungen 2 V, obwohl $R_\mathrm{a}\neq R_\mathrm{c}$. Rechts: Verstärkermodell. 1 µ A an Tor 1 ergibt $-2$ V an Tor 2, 1 µ A an Tor 2 ergibt 0 V an Tor 1.
:::

**Beispiel.** Das T-Zweitor nimmt $P_1=7{,}75\,\mathrm{V}\cdot250\,\mathrm{mA}=1{,}9375$ W auf und gibt $P_2=3\,\mathrm{V}\cdot50\,\mathrm{mA}=0{,}15$ W ab. Die Differenz $P=1{,}7875$ W ist genau die Wärme in den Widerständen: $0{,}9375+0{,}8+0{,}05$ W. Jeder Widerstand nimmt $I^2R\geq0$ auf, deshalb ist ein Zweitor aus Widerständen immer passiv. Das gilt auch mit Kondensatoren und Spulen. Passive Zweitore dürfen sogar gesteuerte Quellen enthalten, entscheidend ist allein $P$. Das Verstärkermodell nimmt $P_1=20\,\mathrm{mV}\cdot10\,\mu\text{A}=0{,}2$ µ W auf und gibt $P_2=4\,\mathrm{V}\cdot0{,}8\,\mathrm{mA}=3{,}2$ mW an die Last, 16 000-mal mehr. Es ist aktiv. Die Energie kommt nicht aus dem Eingangssignal, sondern aus einer Hilfsquelle zur Stromversorgung, die im Zweitor-Modell nicht auftaucht. Dieses Modell gilt für kleine Signale um einen festen Gleichstromzustand (__Kleinsignalbetrieb__, [Teil 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)). **Grenzfälle:** Für $U_1=U_2=0$ ist $P=0$. Ein Zweitor aus idealen Drähten hat $P=0$ in jedem Zustand, es ist passiv, und nichts geht verloren.

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
