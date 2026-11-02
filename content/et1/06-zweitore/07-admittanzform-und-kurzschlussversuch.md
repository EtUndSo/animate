---
title: Stufe 5: Admittanzform und Kurzschlussversuch
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Zweitore
order: 1160700
summary: Die zweite Wahl: Die Spannungen sind die Ursachen.
tags: Y-Parameter, Admittanz, Kurzschlusseingangsleitwert, Kurzschlussausgangsleitwert, Kurzschlussübertragungsleitwert, Steilheit, Eingangskennlinie, Übertragungskennlinie
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Die zweite Wahl: Die Spannungen sind die Ursachen. Diese Stufe überträgt alles und zeigt, warum nun der Kurzschluss die Rolle des Leerlaufs übernimmt.
:::

**Die Idee.** Sind die Spannungen die Ursachen, muss eine Spannung verschwinden, damit der andere Anteil allein bleibt. Eine Spannung ist null, wenn ein Draht das Tor überbrückt. Der Leerlauf setzt einen Strom null, der Kurzschluss eine Spannung. Welcher Versuch der richtige ist, folgt allein aus der Wahl der Ursachen.

:::definition Definition 5.1 (Admittanzform, Y-Form)
<span class="anker" id="satz-5-1"></span>

Die Admittanzform, auch Leitwertform, nimmt die Spannungen als Ursachen:

<span class="anker" id="gl-5-1"></span>
$$I_1=Y_{11}U_1+Y_{12}U_2,\quad I_2=Y_{21}U_1+Y_{22}U_2,\qquad\text{kurz}\quad\mathbf I=\mathbf Y\cdot\mathbf U,\quad\mathbf Y=\begin{pmatrix}Y_{11}&Y_{12}\\Y_{21}&Y_{22}\end{pmatrix}. \tag{5.1}$$

Die __Y-Parameter__ folgen aus zwei Kurzschlussversuchen:

<span class="anker" id="gl-5-2"></span>
$$Y_{11}=\left.\frac{I_1}{U_1}\right|_{U_2=0},\quad Y_{21}=\left.\frac{I_2}{U_1}\right|_{U_2=0},\quad Y_{12}=\left.\frac{I_1}{U_2}\right|_{U_1=0},\quad Y_{22}=\left.\frac{I_2}{U_2}\right|_{U_1=0}. \tag{5.2}$$

Bei Belastung mit dem Leitwert $Y_\mathrm{L}$ an Tor 2, $I_2=-Y_\mathrm{L}U_2$, gilt

<span class="anker" id="gl-5-3"></span>
$$U_2=-\frac{Y_{21}}{Y_{22}+Y_\mathrm{L}}\,U_1,\qquad Y_1=\frac{I_1}{U_1}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}+Y_\mathrm{L}}, \tag{5.3}$$

mit den Grenzfällen

<span class="anker" id="gl-5-4"></span>
$$Y_{1,\mathrm{KS}}=Y_{11},\qquad Y_{1,\mathrm{LL}}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}}. \tag{5.4}$$
:::

⁠**So liest man das:** $Y$ steht für die __Admittanz__, den Kehrwert der Impedanz; hier sind es reelle Leitwerte in Siemens, typisch Mikro- bis Millisiemens, $Y_{ii}=G_{ii}$. $Y_{11}$ ist der __Kurzschlusseingangsleitwert__, $Y_{22}$ der __Kurzschlussausgangsleitwert__. $Y_{21}$ ist der __Kurzschlussübertragungsleitwert__ vorwärts, beim Transistor heißt er __Steilheit__, allgemein Transadmittanz: der Durchgriff der Eingangsspannung auf den Ausgangsstrom. $Y_{12}$ ist derselbe Leitwert rückwärts, der Durchgriff der Ausgangsspannung auf den Eingangsstrom. Das Ersatzschaltbild (Abb. [6](#abb-6) links) ist das Gegenstück zur Z-Form: Eine Summe von Strömen ist eine Parallelschaltung aus Leitwert und spannungsgesteuerter Stromquelle (VCCS). [(5.3)](#gl-5-3) entsteht wie in Stufe [4](das-zweitor-im-betrieb.html#stufe-4), nur mit der Knotenregel am rechten und linken Knoten statt der Maschenregel.

:::abbildung et1/k6yesb 6
Links: Ersatzschaltbild der Y-Form. Rechts: Kurzschlussversuch an Tor 2 mit eingeprägter Spannung $U_\mathrm{q}$. Wegen $U_2=0$ fällt die Quelle $Y_{12}U_2$ weg, und $Y_{22}$ führt keinen Strom. Es bleiben $Y_{11}$ am Eingang und die Stromquelle $Y_{21}U_1$, deren Strom durch den Draht fließt.
:::

**Beispiel.** Am T-Zweitor liegen 9 V an Tor 1, Tor 2 ist kurzgeschlossen. Der Draht legt $R_\mathrm{c}$ parallel zu $R_\mathrm{b}$, der Gesamtwiderstand ist $15\,\Omega+10\,\Omega=25\,\Omega$, also $I_1=360$ mA. Dieser Strom teilt sich hälftig auf, $I_2=-180$ mA, negativ, weil er aus Tor 2 herausfließt. Mit 9 V an Tor 2 und Kurzschluss an Tor 1 ist der Gesamtwiderstand $20\,\Omega+15\,\Omega\parallel20\,\Omega$, $I_2=315$ mA und $I_1=-180$ mA. Das ergibt

$$\mathbf Y=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS}.$$

Probe mit dem Betrieb aus Stufe [4](das-zweitor-im-betrieb.html#stufe-4): $I_1=40\,\mathrm{mS}\cdot7{,}75\,\mathrm{V}-20\,\mathrm{mS}\cdot3\,\mathrm{V}=250$ mA. Die Last $Y_\mathrm{L}=16{,}67$ mS ergibt $Y_1=40\,\mathrm{mS}-400\,\mathrm{mS^2}/51{,}67\,\mathrm{mS}=32{,}26$ mS, das ist $1/(31\,\Omega)$. **Grenzfälle:** $Y_{1,\mathrm{KS}}=40$ mS ist $1/(25\,\Omega)$, $Y_{1,\mathrm{LL}}=28{,}57$ mS ist $1/(35\,\Omega)$, wie in Stufe [4](das-zweitor-im-betrieb.html#stufe-4).

**Kennlinien.** Man kann die Y-Gleichungen auch zeichnen. Die __Eingangskennlinie__ ist $I_1=f_1(U_1)$ bei festem $U_2$, die __Übertragungskennlinie__ $I_2=f_2(U_1)$ bei festem $U_2$, die __Ausgangskennlinie__ $I_2=f_3(U_2)$ bei festem $U_1$. Beim linearen Zweitor sind es Geraden (Abb. [7](#abb-7)): Ihre Steigung ist ein Y-Parameter, der feste Wert verschiebt sie parallel. Jeder Wert des festen Parameters ergibt eine Gerade, zusammen entsteht eine Kurvenschar.

:::abbildung et1/k6kennlinien 7
Kennlinien des T-Zweitors. Links Eingangskennlinie: Steigung $Y_{11}=40$ mS, jedes Volt an $U_2$ schiebt sie um $Y_{12}\cdot1\,\mathrm{V}=-20$ mA. Mitte Übertragungskennlinie: Steigung $Y_{21}=-20$ mS. Rechts Ausgangskennlinie: Steigung $Y_{22}=35$ mS. Beim Transistor sind diese Kurven gekrümmt ([Teil 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).
:::

:::frage Warum ist $Y_{11}$ nicht $1/Z_{11}$? Beides beschreibt doch den Eingang.
Beides beschreibt den Eingang, aber bei verschiedenem Abschluss: $Z_{11}$ gilt bei offenem Ausgang, $Y_{11}$ bei kurzgeschlossenem. Im T-Zweitor sind das 35 $\Omega$ und 25 $\Omega$. $1/Y_{11}=Z_{11}$ gilt nur, wenn $Z_{12}$ oder $Z_{21}$ null ist.
:::

:::aufgabe Aufgabe 5 ★★ Eine $\pi$-Schaltung
<span class="anker" id="aufg-5"></span>

Eine $\pi$-Schaltung hat die Querleitwerte $G_1=10$ mS am Eingang und $G_3=20$ mS am Ausgang und den Längsleitwert $G_2=40$ mS.

<ol class="al">

<li>

Bestimme $\mathbf Y$ aus Kurzschlussversuchen. Welche Ströme fließen bei 2 V an Tor 1?

</li>

<li>

Berechne $Y_{1,\mathrm{LL}}$ und prüfe das Ergebnis mit einer direkten Widerstandsrechnung.

</li>

<li>

Sage voraus: Wie groß ist $I_1$ für $U_1=0$, $U_2=5$ V, und in welche Richtung fließt er?

</li>

</ol>

:::loesung
(a) Tor 2 kurz: $Y_{11}=G_1+G_2=50$ mS, $Y_{21}=-G_2=-40$ mS. Tor 1 kurz: $Y_{22}=G_2+G_3=60$ mS, $Y_{12}=-40$ mS. Bei 2 V: $I_1=100$ mA, $I_2=-80$ mA. (b) $Y_{1,\mathrm{LL}}=50\,\mathrm{mS}-1600\,\mathrm{mS^2}/60\,\mathrm{mS}=23{,}33$ mS, das sind 42,86 $\Omega$. Direkt: $100\,\Omega\parallel(25\,\Omega+50\,\Omega)=42{,}86\,\Omega$. (c) $I_1=Y_{12}U_2=-200$ mA. Tor 1 ist kurzgeschlossen, der Strom läuft von Tor 2 durch $G_2$ und verlässt das Zweitor an Klemme 1.
:::
:::
