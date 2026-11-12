---
title: Stufe 5: Admittanzform und Kurzschlussversuch
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
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

::::beispiel
Am T-Zweitor liegen 9 V an Tor 1, Tor 2 ist kurzgeschlossen. Der Draht legt $R_\mathrm{c}$ parallel zu $R_\mathrm{b}$, der Gesamtwiderstand ist $15\,\Omega+10\,\Omega=25\,\Omega$, also $I_1=360$ mA. Dieser Strom teilt sich hälftig auf, $I_2=-180$ mA, negativ, weil er aus Tor 2 herausfließt. Mit 9 V an Tor 2 und Kurzschluss an Tor 1 ist der Gesamtwiderstand $20\,\Omega+15\,\Omega\parallel20\,\Omega$, $I_2=315$ mA und $I_1=-180$ mA. Das ergibt

$$\mathbf Y=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS}.$$

Probe mit dem Betrieb aus Stufe [4](das-zweitor-im-betrieb.html#stufe-4): $I_1=40\,\mathrm{mS}\cdot7{,}75\,\mathrm{V}-20\,\mathrm{mS}\cdot3\,\mathrm{V}=250$ mA. Die Last $Y_\mathrm{L}=16{,}67$ mS ergibt $Y_1=40\,\mathrm{mS}-400\,\mathrm{mS^2}/51{,}67\,\mathrm{mS}=32{,}26$ mS, das ist $1/(31\,\Omega)$.
::::

⁠**Grenzfälle:** $Y_{1,\mathrm{KS}}=40$ mS ist $1/(25\,\Omega)$, $Y_{1,\mathrm{LL}}=28{,}57$ mS ist $1/(35\,\Omega)$, wie in Stufe [4](das-zweitor-im-betrieb.html#stufe-4).

**Kennlinien.** Man kann die Y-Gleichungen auch zeichnen. Die __Eingangskennlinie__ ist $I_1=f_1(U_1)$ bei festem $U_2$, die __Übertragungskennlinie__ $I_2=f_2(U_1)$ bei festem $U_2$, die __Ausgangskennlinie__ $I_2=f_3(U_2)$ bei festem $U_1$. Beim linearen Zweitor sind es Geraden (Abb. [7](#abb-7)): Ihre Steigung ist ein Y-Parameter, der feste Wert verschiebt sie parallel. Jeder Wert des festen Parameters ergibt eine Gerade, zusammen entsteht eine Kurvenschar.

:::abbildung et1/k6kennlinien 7
Kennlinien des T-Zweitors. Links Eingangskennlinie: Steigung $Y_{11}=40$ mS, jedes Volt an $U_2$ schiebt sie um $Y_{12}\cdot1\,\mathrm{V}=-20$ mA. Mitte Übertragungskennlinie: Steigung $Y_{21}=-20$ mS. Rechts Ausgangskennlinie: Steigung $Y_{22}=35$ mS. Beim Transistor sind diese Kurven gekrümmt ([Kapitel 10](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)).
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

::::formelsammlung
**Admittanzform (Y-Form)**

$$I_1=Y_{11}U_1+Y_{12}U_2,\quad I_2=Y_{21}U_1+Y_{22}U_2,\qquad\text{kurz}\quad\mathbf I=\mathbf Y\cdot\mathbf U,\quad\mathbf Y=\begin{pmatrix}Y_{11}&Y_{12}\\Y_{21}&Y_{22}\end{pmatrix}$$

Die Spannungen sind die Ursachen; auch Leitwertform. Alle $Y$ in S, hier reelle Leitwerte, $Y_{ii}=G_{ii}$.

**Y-Parameter aus Kurzschlussversuchen**

$$Y_{11}=\left.\frac{I_1}{U_1}\right|_{U_2=0},\quad Y_{21}=\left.\frac{I_2}{U_1}\right|_{U_2=0},\quad Y_{12}=\left.\frac{I_1}{U_2}\right|_{U_1=0},\quad Y_{22}=\left.\frac{I_2}{U_2}\right|_{U_1=0}$$

Ein Draht setzt die Spannung seines Tors null. $Y_{11}$ Kurzschlusseingangsleitwert, $Y_{22}$ Kurzschlussausgangsleitwert, $Y_{21}$ Kurzschlussübertragungsleitwert vorwärts (beim Transistor Steilheit), $Y_{12}$ derselbe Leitwert rückwärts.

**Eingangsleitwert bei Last**

$$U_2=-\frac{Y_{21}}{Y_{22}+Y_\mathrm{L}}\,U_1,\qquad Y_1=\frac{I_1}{U_1}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}+Y_\mathrm{L}}$$

Lastleitwert $Y_\mathrm{L}$ an Tor 2 mit $I_2=-Y_\mathrm{L}U_2$. Entsteht wie der Eingangswiderstand, mit der Knotenregel statt der Maschenregel.

**Kurzschluss- und Leerlaufeingangsleitwert**

$$Y_{1,\mathrm{KS}}=Y_{11},\qquad Y_{1,\mathrm{LL}}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}}$$

Grenzfälle Kurzschluss und Leerlauf an Tor 2. $1/Y_{11}=Z_{11}$ gilt nur, wenn $Z_{12}$ oder $Z_{21}$ null ist, denn $Z_{11}$ gilt bei offenem, $Y_{11}$ bei kurzgeschlossenem Ausgang.

**Kennlinien**

$$I_1=f_1(U_1),\qquad I_2=f_2(U_1),\qquad I_2=f_3(U_2)$$

Eingangskennlinie bei festem $U_2$, Übertragungskennlinie bei festem $U_2$, Ausgangskennlinie bei festem $U_1$. Beim linearen Zweitor Geraden mit den Steigungen $Y_{11}$, $Y_{21}$, $Y_{22}$; der feste Wert verschiebt sie parallel.
::::

::::lernkarten
:::karte begriff Admittanzform
Was ist die Admittanzform eines Zweitors, und welche Torgrößen sind darin die Ursachen?
---
Die Form der Zweitorgleichungen mit den Spannungen als Ursachen: $I_1=Y_{11}U_1+Y_{12}U_2$, $I_2=Y_{21}U_1+Y_{22}U_2$, kurz $\mathbf I=\mathbf Y\cdot\mathbf U$. Sie heißt auch Leitwertform oder Y-Form.
--- falsch
Die Form mit den Strömen als Ursachen: $U_1=Y_{11}I_1+Y_{12}I_2$, $U_2=Y_{21}I_1+Y_{22}I_2$, kurz $\mathbf U=\mathbf Y\cdot\mathbf I$. Sie heißt auch Leitwertform oder Y-Form.
--- falsch
Die Form $I_1=Y_{11}U_1+Y_{12}U_2$, $I_2=Y_{21}U_1+Y_{22}U_2$, kurz $\mathbf I=\mathbf Y\cdot\mathbf U$, mit den Strömen als Ursachen, weil sie links stehen und die Spannungen bestimmen.
--- falsch
Die Form mit den Spannungen als Ursachen: $I_1=Y_{11}U_1$, $I_2=Y_{22}U_2$, kurz $\mathbf I=\mathbf Y\cdot\mathbf U$. Jeder Strom hängt nur von der Spannung seines eigenen Tors ab, die Tore beeinflussen sich nicht.
:::
:::karte formel Y-Parameter
Wie bestimmt man die Y-Parameter eines Zweitors durch Versuche an den Toren?
---
Aus zwei Kurzschlussversuchen: $Y_{11}=\left.\frac{I_1}{U_1}\right|_{U_2=0}$ und $Y_{21}=\left.\frac{I_2}{U_1}\right|_{U_2=0}$ bei kurzgeschlossenem Tor 2, $Y_{12}=\left.\frac{I_1}{U_2}\right|_{U_1=0}$ und $Y_{22}=\left.\frac{I_2}{U_2}\right|_{U_1=0}$ bei kurzgeschlossenem Tor 1.
--- falsch
Aus zwei Leerlaufversuchen: $Y_{11}=\left.\frac{I_1}{U_1}\right|_{I_2=0}$ und $Y_{21}=\left.\frac{I_2}{U_1}\right|_{I_2=0}$ bei offenem Tor 2, $Y_{12}$ und $Y_{22}$ ebenso bei offenem Tor 1, genau wie bei der Z-Form.
--- falsch
Als Kehrwerte der Z-Parameter aus denselben Leerlaufversuchen: $Y_{11}=1/Z_{11}$, $Y_{12}=1/Z_{12}$, $Y_{21}=1/Z_{21}$ und $Y_{22}=1/Z_{22}$, weil Leitwerte die Kehrwerte von Widerständen sind.
--- falsch
Aus zwei Kurzschlussversuchen mit denselben Quotienten, aber anders verteilt: Bei kurzgeschlossenem Tor 2 misst man $Y_{11}$ und $Y_{12}$, bei kurzgeschlossenem Tor 1 dagegen $Y_{21}$ und $Y_{22}$.
:::
:::karte zusammenhang Kurzschluss statt Leerlauf
Warum bestimmt man die Y-Parameter mit Kurzschlussversuchen und nicht mit Leerlaufversuchen?
---
Weil nun die Spannungen die Ursachen sind. Um einen Anteil allein zu sehen, muss die andere Spannung null sein, und eine Spannung ist null, wenn ein Draht das Tor überbrückt.
--- falsch
Weil Leitwerte im Leerlauf unendlich groß werden und sich deshalb nicht messen lassen. Im Kurzschluss bleiben sie endlich und lassen sich direkt am Strommesser ablesen.
--- falsch
Weil der Kurzschluss den größten Strom liefert und Leitwerte nur bei großen Strömen genau messbar sind. Mit Leerlaufversuchen ginge es grundsätzlich auch.
--- falsch
Weil die Ströme die Ursachen sind und ein Kurzschluss einen Strom null setzt. Ein offenes Tor würde dagegen eine Spannung null setzen und nichts freilegen.
:::
:::karte begriff Admittanz
Wofür steht der Buchstabe $Y$ in der Admittanzform, und welche Einheit haben die Y-Parameter bei Gleichgrößen?
---
Für die Admittanz, den Kehrwert der Impedanz. Bei Gleichgrößen sind die Y-Parameter reelle Leitwerte in Siemens, typisch Mikro- bis Millisiemens, und es gilt $Y_{ii}=G_{ii}$.
--- falsch
Für die Admittanz, einen anderen Namen der Impedanz bei Wechselgrößen. Die Y-Parameter haben deshalb wie die Z-Parameter die Einheit $\Omega$, typisch Ohm bis Megaohm.
--- falsch
Für die Admittanz, den Kehrwert der Impedanz. Bei Gleichgrößen sind die Y-Parameter trotzdem reelle Widerstände in $\Omega$, weil man den Kehrwert erst bei Wechselgrößen bildet.
--- falsch
Für die Admittanz, den durchgelassenen Anteil einer Spannung. Die Y-Parameter haben keine Einheit und geben an, welcher Teil der Spannung von Tor zu Tor gelangt.
:::
:::karte begriff Kurzschlusseingangsleitwert und Kurzschlussausgangsleitwert
Was geben der Kurzschlusseingangsleitwert $Y_{11}$ und der Kurzschlussausgangsleitwert $Y_{22}$ eines Zweitors an?
---
$Y_{11}$ ist der Leitwert an Tor 1 bei kurzgeschlossenem Tor 2, $Y_{22}$ der Leitwert an Tor 2 bei kurzgeschlossenem Tor 1, beide in Siemens.
--- falsch
$Y_{11}$ ist der Leitwert an Tor 1 bei offenem Tor 2, $Y_{22}$ der an Tor 2 bei offenem Tor 1; sie sind die Kehrwerte von $Z_{11}$ und $Z_{22}$.
--- falsch
$Y_{11}$ ist der Strom bei kurzgeschlossenem Tor 1, $Y_{22}$ der Strom bei kurzgeschlossenem Tor 2, jeweils in Ampere, wenn am anderen Tor 1 V liegt.
--- falsch
$Y_{11}$ und $Y_{22}$ sind die Leitwerte der Drähte, mit denen man beim Versuch Tor 2 bzw. Tor 1 kurzschließt; sie müssen sehr groß sein.
:::
:::karte begriff Kurzschlussübertragungsleitwert und Steilheit
Was gibt der Kurzschlussübertragungsleitwert $Y_{21}$ an, und wie heißt er beim Transistor?
---
Den Durchgriff der Eingangsspannung auf den Ausgangsstrom bei kurzgeschlossenem Tor 2, vorwärts, in Siemens. Beim Transistor heißt er Steilheit, allgemein Transadmittanz. $Y_{12}$ ist derselbe Leitwert rückwärts.
--- falsch
Den Durchgriff der Ausgangsspannung auf den Eingangsstrom bei kurzgeschlossenem Tor 1, in Siemens. Beim Transistor heißt er Steilheit, und $Y_{12}$ ist derselbe Leitwert in Vorwärtsrichtung.
--- falsch
Das Verhältnis von Ausgangsstrom zu Eingangsstrom bei kurzgeschlossenem Tor 2, ohne Einheit. Beim Transistor heißt er Steilheit, weil er dort die Stromverstärkung angibt, also wie steil der Ausgangsstrom ansteigt.
--- falsch
Den Leitwert der Verbindung zwischen Tor 1 und Tor 2 bei offenem Ausgang, in Siemens. Beim Transistor heißt er Steilheit, weil er die Kennlinie steiler macht.
:::
:::karte formel Eingangsleitwert bei Last
Wie groß ist der Eingangsleitwert $Y_1$ eines Zweitors mit dem Lastleitwert $Y_\mathrm{L}$ an Tor 2, und welche Grenzfälle hat er?
---
$Y_1=\frac{I_1}{U_1}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}+Y_\mathrm{L}}$, mit $I_2=-Y_\mathrm{L}U_2$. Im Kurzschluss ist $Y_{1,\mathrm{KS}}=Y_{11}$, im Leerlauf $Y_{1,\mathrm{LL}}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}}$.
--- falsch
$Y_1=\frac{I_1}{U_1}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}+Y_\mathrm{L}}$, mit $I_2=-Y_\mathrm{L}U_2$. Im Leerlauf ist $Y_{1,\mathrm{LL}}=Y_{11}$, im Kurzschluss $Y_{1,\mathrm{KS}}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}}$.
--- falsch
$Y_1=Y_{11}+Y_\mathrm{L}$, weil der Lastleitwert über das Zweitor parallel zum Eingang liegt. Im Leerlauf ist $Y_1=Y_{11}$, im Kurzschluss wird er unendlich groß.
--- falsch
$Y_1=\frac{I_1}{U_1}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{11}+Y_\mathrm{L}}$, mit $I_2=-Y_\mathrm{L}U_2$. Im Kurzschluss ist $Y_{1,\mathrm{KS}}=Y_{11}$, im Leerlauf $Y_{1,\mathrm{LL}}=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{11}}$.
:::
:::karte zusammenhang Ersatzschaltbild der Y-Form
Wie sieht das Ersatzschaltbild der Y-Form aus, und warum gerade so?
---
An jedem Tor ein Leitwert parallel zu einer spannungsgesteuerten Stromquelle (VCCS). Ströme addieren sich parallel; der Anteil der eigenen Spannung ist ein Leitwert, der der fremden Spannung eine gesteuerte Quelle.
--- falsch
An jedem Tor ein Widerstand in Reihe mit einer stromgesteuerten Spannungsquelle (CCVS), genau wie bei der Z-Form, weil beide Formen dasselbe Zweitor beschreiben und deshalb auch dasselbe Ersatzschaltbild haben müssen.
--- falsch
An jedem Tor ein Leitwert parallel zu einer stromgesteuerten Stromquelle (CCCS), weil die Wirkungen Ströme sind und deshalb auch die Steuergröße der Quelle ein Strom sein muss.
--- falsch
An jedem Tor ein Leitwert in Reihe mit einer spannungsgesteuerten Stromquelle (VCCS), weil sich die Ströme der beiden Bauteile in einer Reihenschaltung zum Torstrom addieren.
:::
:::karte begriff Eingangskennlinie und Ausgangskennlinie
Was zeigen die Eingangskennlinie und die Ausgangskennlinie eines Zweitors in der Darstellung mit Y-Parametern?
---
Die Eingangskennlinie ist $I_1=f_1(U_1)$ bei festem $U_2$, die Ausgangskennlinie $I_2=f_3(U_2)$ bei festem $U_1$. Beim linearen Zweitor sind es Geraden mit den Steigungen $Y_{11}$ und $Y_{22}$.
--- falsch
Die Eingangskennlinie ist $I_1=f_1(U_1)$ bei festem $I_2$, die Ausgangskennlinie $I_2=f_3(U_2)$ bei festem $I_1$. Beim linearen Zweitor sind es Geraden, die stets durch den Ursprung gehen.
--- falsch
Die Eingangskennlinie zeigt $U_1$ über der Zeit, die Ausgangskennlinie $U_2$ über der Zeit. Beim linearen Zweitor sind es Sinuskurven gleicher Frequenz, aber verschiedener Höhe.
--- falsch
Die Eingangskennlinie ist $I_2$ über $U_1$, die Ausgangskennlinie $I_1$ über $U_2$, jeweils bei festem anderem Strom. Beim linearen Zweitor sind es Geraden mit den Steigungen $Y_{21}$ und $Y_{12}$.
:::
:::karte begriff Übertragungskennlinie
Was zeigt die Übertragungskennlinie eines Zweitors, und was bewirkt der feste Wert von $U_2$?
---
Sie ist $I_2=f_2(U_1)$ bei festem $U_2$, beim linearen Zweitor eine Gerade mit der Steigung $Y_{21}$. Der feste Wert verschiebt sie parallel; jeder Wert ergibt eine Gerade, zusammen eine Kurvenschar.
--- falsch
Sie ist $U_2$ über $U_1$ bei offenem Ausgang, beim linearen Zweitor eine Gerade mit der Steigung $Z_{21}$. Ein fester Wert von $U_2$ kommt darin gar nicht vor, er wäre ein Widerspruch zum offenen Ausgang.
--- falsch
Sie ist $I_2=f_2(U_1)$ bei festem $U_2$, eine Gerade mit der Steigung $Y_{22}$. Der feste Wert dreht sie um den Ursprung, jeder Wert ergibt also eine andere Steigung.
--- falsch
Sie zeigt, wie viel Leistung vom Eingang zum Ausgang übertragen wird, abhängig von $U_1$. Beim linearen Zweitor ist sie eine Parabel, deren Höhe vom festen Wert abhängt.
:::
:::karte zusammenhang Eingangsleitwert und Eingangsleerlaufwiderstand
Warum ist $Y_{11}$ im Allgemeinen nicht der Kehrwert von $Z_{11}$, obwohl beide den Eingang beschreiben?
---
Sie gelten bei verschiedenem Abschluss: $Z_{11}$ bei offenem Ausgang, $Y_{11}$ bei kurzgeschlossenem. Im T-Zweitor sind das 35 $\Omega$ und 25 $\Omega$. $1/Y_{11}=Z_{11}$ gilt nur, wenn $Z_{12}$ oder $Z_{21}$ null ist.
--- falsch
Er ist es doch: $Y_{11}=1/Z_{11}$ gilt immer, weil Leitwert und Widerstand Kehrwerte voneinander sind. Abweichungen im T-Zweitor entstehen nur durch Rundung der Zwischenergebnisse.
--- falsch
Weil $Y_{11}$ bei offenem Ausgang gilt und $Z_{11}$ bei kurzgeschlossenem. Im T-Zweitor sind das 25 $\Omega$ und 35 $\Omega$; $1/Y_{11}=Z_{11}$ gilt nur, wenn $Z_{22}$ null ist.
--- falsch
Weil $Y_{11}$ zusätzlich den Lastleitwert enthält, $Z_{11}$ aber nicht. Ohne angeschlossene Last wären beide Parameter genau Kehrwerte voneinander.
:::
::::
