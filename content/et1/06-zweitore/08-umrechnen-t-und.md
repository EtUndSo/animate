---
title: Stufe 6: Umrechnen, T und $\pi$
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Zweitore
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

Setzt man beide gleich, entstehen $G_2=-Y_{12}$, $G_1=Y_{11}+Y_{12}$ und $G_3=Y_{22}+Y_{21}$. Für $G_3=0$ wird aus $\mathbf Y_\pi$ das Paar $I_1=(G_1+G_2)U_1-G_2U_2$, $I_2=-G_2U_1+G_2U_2$. Das ist die Stern-Dreieck-Transformation aus [Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html): T ist der Stern, $\pi$ das Dreieck. Die Beschreibung mit Z-Parametern führt von selbst auf die T-Schaltung, die mit Y-Parametern auf die dazu duale $\pi$-Schaltung. Umgekehrt gehört zu jedem Zweitor mit $Z_{12}=Z_{21}$ eine T- und eine $\pi$-Ersatzschaltung ohne Quellen (Stufe [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10)).

:::abbildung et1/k6tpi 8
Zwei Schaltungen, dasselbe Zweitor. Links die T-Schaltung mit 15, 20 und 20 $\Omega$, rechts die gleichwertige $\pi$-Schaltung mit 50, 50 und 66,7 $\Omega$. Beide haben $\det\mathbf Z=1000\,\Omega^2$. An den Toren lassen sie sich durch keine Messung unterscheiden.
:::

**Beispiel.** Es ist $\det\mathbf Z=35\cdot40\,\Omega^2-20\cdot20\,\Omega^2=1000\,\Omega^2$, also

$$\mathbf Y=\frac{1}{1000\,\Omega^2}\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\Omega=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS},$$

genau das Ergebnis der Kurzschlussversuche. Die $\pi$-Schaltung hat $G_2=20$ mS, $G_1=40\,\mathrm{mS}-20\,\mathrm{mS}=20$ mS, $G_3=15$ mS, also 50 $\Omega$, 50 $\Omega$ und 66,7 $\Omega$. Mit derselben Quelle und Last ergibt sie wieder 7,75 V und 3 V.

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
