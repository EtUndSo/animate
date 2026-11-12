---
title: Stufe 10: Parallelschaltung, Stromteiler und Belastung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom, Widerstand und Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Kapitel 2: Strom, Widerstand und Kirchhoff
order: 1121100
summary: Das zweite Grundmuster: nebeneinanderliegende Widerstände.
tags: Parallelschaltung, Stromteiler, Lastwiderstand
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Das zweite Grundmuster: nebeneinanderliegende Widerstände. Damit lässt sich beantworten, was mit einem Spannungsteiler geschieht, dem man Strom entnimmt.
:::

**Die Idee.** Alle Widerstände hängen an denselben zwei Knoten, also an derselben Spannung. Jeder zusätzliche Widerstand öffnet einen zusätzlichen Weg, und die Knotenregel addiert die Ströme. Deshalb addieren sich die Leitwerte, wie sich Querschnitte nebeneinanderliegender Drähte addieren.

:::satz Satz 10.1 (Parallelschaltung und Stromteiler)
<span class="anker" id="satz-10-1"></span>

Für $N$ Widerstände in __Parallelschaltung__ gilt

<span class="anker" id="gl-10-1"></span>
<span class="anker" id="gl-10-2"></span>
$$\begin{aligned} U&=U_1=\dots=U_N,\qquad I=I_1+\dots+I_N,\qquad I_i=G_i\,U=\frac{U}{R_i},\\ G_\mathrm{ges}&=\frac{1}{R_\mathrm{ges}}=\sum_{i=1}^{N}G_i=\sum_{i=1}^{N}\frac{1}{R_i},\qquad R_\mathrm{ges}=\Bigl(\sum_{i=1}^N\frac1{R_i}\Bigr)^{-1}. \end{aligned} \tag{10.1|10.2}$$

Für zwei Widerstände schreibt man $R_1\parallel R_2$:

<span class="anker" id="gl-10-3"></span>
$$R_1\parallel R_2=\frac{R_1\,R_2}{R_1+R_2},\qquad I_1=I_\mathrm{ges}\,\frac{G_1}{G_1+G_2}=I_\mathrm{ges}\,\frac{R_2}{R_1+R_2},\quad I_2=I_\mathrm{ges}\,\frac{G_2}{G_1+G_2}. \tag{10.3}$$
:::

⁠**So liest man das:** Die Ströme teilen sich im Verhältnis der Leitwerte, der __Stromteiler__. Im Ausdruck für $I_1$ steht oben $R_2$: Der Strom bevorzugt den kleineren Widerstand. **Gültigkeit:** Beide Widerstände liegen zwischen denselben zwei Knoten, die Zuleitungen sind ideal.

:::herleitung Gesamtleitwert und Stromteiler
Die Knotenregel gibt $I=\sum I_i$, mit gleichem $U$ also $I=(G_1+\dots+G_N)\,U$. Für zwei Zweige ist $U=I_\mathrm{ges}/(G_1+G_2)$ und damit $I_1=G_1\,U$. Mit $G=1/R$ wird

$$I_1=I_\mathrm{ges}\,\frac{1/R_1}{1/R_1+1/R_2}=I_\mathrm{ges}\,\frac{R_2}{R_1+R_2}.$$
:::

::::beispiel
$R_1$ und $R_2$ der Kette parallel an 9 V: $G_\mathrm{ges}=0{,}5+1=1{,}5$ mS, also $R_\mathrm{ges}=667\,\Omega$, weniger als der kleinere Wert, und $I=13{,}5$ mA. Der Stromteiler gibt $I_1=13{,}5\,\mathrm{mA}\cdot1/3=4{,}5$ mA, $I_2=9$ mA. Gemischte Netze fasst man von innen nach außen zusammen: $6\,\mathrm{k\Omega}$ parallel zu $1\,\mathrm{k\Omega}+2\,\mathrm{k\Omega}$ ergibt $6\parallel3=2\,\mathrm{k\Omega}$.
::::

⁠**Grenzfälle:** $R_2\to\infty$ ergibt $R_1$, der offene Zweig zählt nicht. $R_2\to0$ ergibt 0, der Kurzschluss übernimmt den ganzen Strom. $R_1=R_2$ ergibt $R_1/2$.

**Der belastete Spannungsteiler.** Die Spannung eines Teilers soll eine weitere Stufe versorgen, der __Lastwiderstand__ $R_\mathrm L$ liegt parallel zu $R_2$ (Abb. [11](#abb-11)). Der Mechanismus: Am Mittelknoten öffnet sich ein zusätzlicher Weg, der Gesamtwiderstand sinkt, der Strom durch $R_1$ steigt, an $R_1$ fällt mehr ab, und das Mittelpotenzial sinkt. Mit $R_2'=R_2\parallel R_\mathrm L$ in [(9.3)](reihenschaltung-und-spannungsteiler.html#gl-9-3):

<span class="anker" id="gl-10-4"></span>
$$\frac{U_2}{U}=\frac{R_2\parallel R_\mathrm L}{R_1+R_2\parallel R_\mathrm L}=\frac{R_2\,R_\mathrm L}{R_1\,(R_2+R_\mathrm L)+R_2\,R_\mathrm L},\quad I_\mathrm L=\frac{U_2}{R_\mathrm L}=\frac{U\,R_2}{R_1\,(R_2+R_\mathrm L)+R_2\,R_\mathrm L}. \tag{10.4}$$

⁠**Grenzfälle:** $R_\mathrm L\to\infty$ ergibt $I_\mathrm L\to0$ und die unbelastete Regel. $R_\mathrm L=R_2$ ergibt $U_2/U=R_2/(2R_1+R_2)=\frac12R_2/(R_1+\frac12R_2)$.

:::abbildung et1/k2belastung 11
Links: belasteter Spannungsteiler. Rechts: $U_2$ über $R_\mathrm L$ für $R_1=2\,\mathrm{k\Omega}$, $R_2=1\,\mathrm{k\Omega}$, $U=9$ V, nach [(10.4)](#gl-10-4). Mit $R_\mathrm L=1\,\mathrm{k\Omega}$ bleiben 1,8 V, mit $10\,\mathrm{k\Omega}$ sind es 2,81 V. Erst weit oberhalb von $R_1\parallel R_2=667\,\Omega$ ist die Last unmerklich.
:::

::::beispiel
Für die Kette ist der relative Fehler $\delta=(U_{2,0}-U_2)/U_{2,0}$ gegen die unbelasteten 3 V: $R_\mathrm L=1\,\mathrm{k\Omega}$ ergibt 40 %, $10\,\mathrm{k\Omega}$ ergibt 6,3 %, $100\,\mathrm{k\Omega}$ ergibt 0,66 %. Der Fehler ist $\delta=R_\mathrm i/(R_\mathrm i+R_\mathrm L)$ mit $R_\mathrm i=R_1\parallel R_2$ (Aufgabe [11](#aufg-11)). Der Teiler wirkt also wie eine Quelle mit dem Innenwiderstand $R_\mathrm i$ ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)).
::::

:::ltspice Belastung messen
⁠**Zeichnen:** Quelle `voltage` mit `9` von `in` nach Masse, `res` `R1 2k` von `in` nach `mid`, `R2 1k` von `mid` nach Masse, `RL` mit Wert `{RL}` von `mid` nach Masse.

⁠**Direktiven:** `.step param RL list 1k 2k 6k 10k 100k`, `.tran 1m`, `.meas tran u2 FIND V(mid) AT=1m`.

⁠**Was du siehst:** Das SPICE Error Log nennt für jeden Schritt $U_2$: 1,80 V; 2,25 V; 2,70 V; 2,81 V; 2,98 V. Vergleiche den Wert für $6\,\mathrm{k\Omega}$ mit Aufgabe [11](#aufg-11)(b).
:::

**Anwendung: R-2R-Leiter.** Der Stromteiler trägt einen zweiten D/A-Wandler (Abb. [12](#abb-12)). Der Trick ist Selbstähnlichkeit: Am letzten Knoten liegt $2R\parallel2R=R$. Mit dem $R$ davor ergibt das wieder $2R$. So blickt jeder Knoten nach rechts und nach unten auf je $2R$, sein Strom teilt sich 1:1, und von Knoten zu Knoten halbiert sich die Spannung (Teiler aus $R$ und $2R\parallel2R$). Die Quelle liefert $I_\mathrm{ref}=U_\mathrm{ref}/R$, und es entstehen die binär gewichteten Ströme $I_\mathrm{ref}/2$, $I_\mathrm{ref}/4$, $I_\mathrm{ref}/8$ und so weiter. Eine äußere Schaltung ([Kapitel 11](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html)) hält die Sammelschiene auf dem Massepotenzial. Deshalb sehen alle $2R$ unten dasselbe Potenzial, ob sie nun zur Schiene oder zur Masse schalten, und die Ströme ändern sich beim Umschalten nicht. Das Bit nahe der Quelle ist das höchstwertige (MSB, most significant bit), das am Ende das niederwertigste (LSB). $I_\mathrm{aus}$ ist die Summe der eingeschalteten Ströme.

:::abbildung et1/k2r2r 12
R-2R-Leiter mit $R=1\,\mathrm{k\Omega}$ an $U_\mathrm{ref}=8$ V. Rot die Knotenspannungen, blau die Zweigströme. Die Schalter stehen auf der Zahl 1010: Zur Sammelschiene laufen $4\,\mathrm{mA}+1\,\mathrm{mA}=5$ mA.
:::

:::frage Wie kann der Widerstand sinken, wenn ein weiterer dazukommt?
Mit „mehr Widerstand“ ist hier mehr Wege gemeint. Der vorhandene Zweig führt weiter denselben Strom, der neue führt zusätzlichen. Bei gleicher Spannung fließt insgesamt mehr, also ist $U/I$ kleiner.
:::

:::aufgabe Aufgabe 10 ★★ Parallel und gemischt
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Berechne $R_\mathrm{ges}$ für $2$, $3$ und $6\,\mathrm{k\Omega}$ parallel, und alle Ströme bei 12 V.

</li>

<li>

10 mA teilen sich auf $1\,\mathrm{k\Omega}$ und $9\,\mathrm{k\Omega}$ auf. Wie groß sind beide Ströme?

</li>

<li>

$1\,\mathrm{k\Omega}$ liegt in Reihe mit $4\,\mathrm{k\Omega}\parallel(1\,\mathrm{k\Omega}+3\,\mathrm{k\Omega})$ an 9 V. Bestimme $R_\mathrm{ges}$ und alle Ströme.

</li>

</ol>

:::loesung
(a) $G_\mathrm{ges}=0{,}5+0{,}333+0{,}167=1$ mS, also $R_\mathrm{ges}=1\,\mathrm{k\Omega}$. Ströme 6, 4 und 2 mA, Summe 12 mA. (b) $I_1=10\,\mathrm{mA}\cdot9/10=9$ mA, $I_2=1$ mA. Der kleine Widerstand führt das Neunfache. (c) $1+3=4\,\mathrm{k\Omega}$, $4\parallel4=2\,\mathrm{k\Omega}$, $R_\mathrm{ges}=3\,\mathrm{k\Omega}$. Gesamtstrom 3 mA, in beiden gleichen Zweigen je 1,5 mA.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Belastung beherrschen
<span class="anker" id="aufg-11"></span>

Der Teiler ist $R_1=2\,\mathrm{k\Omega}$, $R_2=1\,\mathrm{k\Omega}$ an 9 V.

<ol class="al">

<li>

Zeige aus [(10.4)](#gl-10-4): $\delta=R_\mathrm i/(R_\mathrm i+R_\mathrm L)$ mit $R_\mathrm i=R_1\parallel R_2$.

</li>

<li>

Welches $R_\mathrm L$ ergibt $\delta=10\,\%$? Wie groß ist dann $U_2$?

</li>

<li>

Ein Teiler aus $200\,\Omega$ und $100\,\Omega$ hat dasselbe Verhältnis. Berechne $U_2$ an $R_\mathrm L=1\,\mathrm{k\Omega}$. Was kostet die bessere Spannung?

</li>

<li>

Grenzfall: Wie groß ist $I_\mathrm L$ für $R_\mathrm L\to0$ beim ursprünglichen Teiler?

</li>

</ol>

:::loesung
(a) Unbelastet ist $U_{2,0}=U\,R_2/(R_1+R_2)$. Aus [(10.4)](#gl-10-4) folgt

$$\frac{U_2}{U_{2,0}}=\frac{R_\mathrm L\,(R_1+R_2)}{R_1R_2+R_\mathrm L\,(R_1+R_2)}=\frac{R_\mathrm L}{R_\mathrm i+R_\mathrm L},\qquad\delta=1-\frac{U_2}{U_{2,0}}=\frac{R_\mathrm i}{R_\mathrm i+R_\mathrm L}.$$

(b) $\delta=0{,}1$ ergibt $R_\mathrm L=9\,R_\mathrm i=6\,\mathrm{k\Omega}$ und $U_2=2{,}7$ V.

(c) $R_\mathrm i=66{,}7\,\Omega$, $U_2=2{,}81$ V, derselbe Fehler wie zuvor bei $10\,\mathrm{k\Omega}$. Dafür fließen im Teiler 30 mA statt 3 mA, er setzt 270 mW statt 27 mW um.

(d) $R_\mathrm L\to0$ schließt $R_2$ kurz: $I_\mathrm L=9\,\mathrm{V}/2\,\mathrm{k\Omega}=4{,}5$ mA.
:::
:::

:::aufgabe Aufgabe 12 ★★★ R-2R-Leiter
<span class="anker" id="aufg-12"></span>

Eine Leiter mit vier Knoten wie in Abb. [12](#abb-12) hat $R=10\,\mathrm{k\Omega}$ und $U_\mathrm{ref}=5$ V.

<ol class="al">

<li>

Welchen Widerstand sieht die Quelle? Wie groß sind $I_\mathrm{ref}$ und die Knotenspannungen?

</li>

<li>

Wie groß sind die vier Ströme durch die oberen $2R$?

</li>

<li>

Wie groß ist $I_\mathrm{aus}$ bei der Zahl 1001, und wie groß die kleinste Stufe?

</li>

</ol>

:::loesung
(a) Die Quelle sieht $2R\parallel2R=R=10\,\mathrm{k\Omega}$, also $I_\mathrm{ref}=0{,}5$ mA. Knotenspannungen 5; 2,5; 1,25; 0,625 V. (b) 0,25; 0,125; 0,0625; 0,03125 mA. (c) Zahl 1001: $0{,}25+0{,}03125=0{,}281$ mA. Die kleinste Stufe ist 31,25 µ A.
:::
:::

::::formelsammlung
**Parallelschaltung**

$$U=U_1=\dots=U_N,\qquad I=I_1+\dots+I_N,\qquad I_i=G_i\,U=\frac{U}{R_i}$$

$N$ Widerstände zwischen denselben zwei Knoten.

**Gesamtleitwert und Gesamtwiderstand**

$$G_\mathrm{ges}=\frac{1}{R_\mathrm{ges}}=\sum_{i=1}^{N}G_i=\sum_{i=1}^{N}\frac{1}{R_i},\qquad R_\mathrm{ges}=\Bigl(\sum_{i=1}^N\frac1{R_i}\Bigr)^{-1}$$

Die Leitwerte addieren sich wie die Querschnitte nebeneinanderliegender Drähte.

**Zwei parallele Widerstände**

$$R_1\parallel R_2=\frac{R_1\,R_2}{R_1+R_2}$$

Grenzfälle: $R_2\to\infty$ ergibt $R_1$, $R_2\to0$ ergibt 0, $R_1=R_2$ ergibt $R_1/2$.

**Stromteiler**

$$I_1=I_\mathrm{ges}\,\frac{G_1}{G_1+G_2}=I_\mathrm{ges}\,\frac{R_2}{R_1+R_2},\quad I_2=I_\mathrm{ges}\,\frac{G_2}{G_1+G_2}$$

Die Ströme teilen sich im Verhältnis der Leitwerte, der Strom bevorzugt den kleineren Widerstand. Beide Widerstände liegen zwischen denselben zwei Knoten, die Zuleitungen sind ideal.

**Belasteter Spannungsteiler**

$$\frac{U_2}{U}=\frac{R_2\parallel R_\mathrm L}{R_1+R_2\parallel R_\mathrm L}=\frac{R_2\,R_\mathrm L}{R_1\,(R_2+R_\mathrm L)+R_2\,R_\mathrm L}$$

Lastwiderstand $R_\mathrm L$ parallel zu $R_2$; $R_\mathrm L\to\infty$ ergibt die unbelastete Regel.

**Laststrom**

$$I_\mathrm L=\frac{U_2}{R_\mathrm L}=\frac{U\,R_2}{R_1\,(R_2+R_\mathrm L)+R_2\,R_\mathrm L}$$

Strom durch den Lastwiderstand am Abgriff.

**Fehler durch Belastung**

$$\delta=(U_{2,0}-U_2)/U_{2,0}=R_\mathrm i/(R_\mathrm i+R_\mathrm L),\qquad R_\mathrm i=R_1\parallel R_2$$

$U_{2,0}$ unbelastete Teilspannung. Der Teiler wirkt wie eine Quelle mit dem Innenwiderstand $R_\mathrm i$; die Last ist erst unmerklich, wenn $R_\mathrm L$ weit über $R_\mathrm i$ liegt.

**R-2R-Leiter**

$$I_\mathrm{ref}=U_\mathrm{ref}/R,\qquad I_\mathrm{ref}/2,\ I_\mathrm{ref}/4,\ I_\mathrm{ref}/8,\ \dots$$

Selbstähnlichkeit: $2R\parallel2R=R$, jeder Knoten blickt nach rechts und nach unten auf je $2R$, sein Strom teilt sich 1:1. Es entstehen binär gewichtete Ströme; $I_\mathrm{aus}$ ist die Summe der eingeschalteten.
::::

::::lernkarten
:::karte begriff Parallelschaltung
Was kennzeichnet eine Parallelschaltung von Widerständen?
---
Alle Widerstände hängen an denselben zwei Knoten, also an derselben Spannung, $U=U_1=\dots=U_N$. Die Ströme addieren sich, $I=I_1+\dots+I_N$.
--- falsch
Alle Widerstände liegen hintereinander zwischen zwei Knoten, also fließt durch alle derselbe Strom. Die Spannungen addieren sich.
--- falsch
Alle Widerstände liegen nebeneinander und haben denselben Wert, also führen sie denselben Strom. Die Spannungen addieren sich.
--- falsch
Alle Widerstände hängen an derselben Quelle, jeder über eigene Knoten. Die Spannung teilt sich im Verhältnis der Widerstände auf.
:::
:::karte formel Gesamtleitwert
Wie berechnet man den Gesamtwiderstand von $N$ parallelen Widerständen?
---
Über die Leitwerte: $G_\mathrm{ges}=\frac{1}{R_\mathrm{ges}}=\sum_{i=1}^{N}G_i=\sum_{i=1}^{N}\frac{1}{R_i}$. Der Gesamtwiderstand ist kleiner als der kleinste einzelne.
--- falsch
Über die Widerstände: $R_\mathrm{ges}=\sum_{i=1}^{N}R_i$. Der Gesamtwiderstand ist größer als der größte einzelne, weil jeder Zweig bremst.
--- falsch
Über die Leitwerte: $G_\mathrm{ges}=\sum_{i=1}^{N}G_i$, und $R_\mathrm{ges}=\sum_{i=1}^{N}\frac{1}{G_i}$. Der Gesamtwiderstand liegt zwischen dem kleinsten und dem größten.
--- falsch
Über die Kehrwerte: $\frac{1}{R_\mathrm{ges}}=\sum_{i=1}^{N}R_i$. Der Gesamtwiderstand sinkt, wenn einer der Widerstände wächst.
:::
:::karte formel Zwei parallele Widerstände
Wie groß ist der Gesamtwiderstand $R_1\parallel R_2$ zweier paralleler Widerstände?
---
$R_1\parallel R_2=\frac{R_1\,R_2}{R_1+R_2}$, Produkt durch Summe. Für $R_1=R_2$ ergibt das $R_1/2$.
--- falsch
$R_1\parallel R_2=\frac{R_1+R_2}{R_1\,R_2}$, Summe durch Produkt. Für $R_1=R_2$ ergibt das $2/R_1$.
--- falsch
$R_1\parallel R_2=R_1+R_2$, die Summe. Für $R_1=R_2$ ergibt das $2R_1$.
--- falsch
$R_1\parallel R_2=\frac{R_1\,R_2}{R_1+R_2}$, Produkt durch Summe. Für $R_1=R_2$ ergibt das $2R_1$.
:::
:::karte begriff Stromteiler
Was beschreibt der Stromteiler, und welcher Anteil des Gesamtstroms $I_\mathrm{ges}$ fließt durch $R_1$?
---
Die Aufteilung im Verhältnis der Leitwerte: $I_1=I_\mathrm{ges}\,\frac{G_1}{G_1+G_2}=I_\mathrm{ges}\,\frac{R_2}{R_1+R_2}$. Der Strom bevorzugt den kleineren Widerstand.
--- falsch
Die Aufteilung des Stroms im Verhältnis der Widerstände: $I_1=I_\mathrm{ges}\,\frac{R_1}{R_1+R_2}$. Der Strom bevorzugt den größeren Widerstand.
--- falsch
Die Aufteilung zu gleichen Teilen: $I_1=I_2=I_\mathrm{ges}/2$. Beide Zweige liegen an derselben Spannung und führen deshalb auch denselben Strom.
--- falsch
Die Aufteilung im Verhältnis der Leitwerte: $I_1=I_\mathrm{ges}\,\frac{G_2}{G_1+G_2}=I_\mathrm{ges}\,\frac{R_1}{R_1+R_2}$. Der Strom bevorzugt den größeren Widerstand.
:::
:::karte herleitung Stromteiler
Leite für zwei parallele Widerstände die Stromteilerregel $I_1=I_\mathrm{ges}\,\frac{R_2}{R_1+R_2}$ her.
---
Die Knotenregel gibt $I=\sum I_i$, weil sich der Strom am gemeinsamen Knoten auf die Zweige aufteilt.
---
Mit gleichem $U$ ist $I=(G_1+\dots+G_N)\,U$, weil jeder Zweig an derselben Spannung liegt und $I_i=G_i\,U$ führt.
---
Für zwei Zweige ist $U=I_\mathrm{ges}/(G_1+G_2)$ und damit $I_1=G_1\,U$, weil man die Gleichung nach $U$ auflöst.
---
Mit $G=1/R$ wird $I_1=I_\mathrm{ges}\,\frac{1/R_1}{1/R_1+1/R_2}=I_\mathrm{ges}\,\frac{R_2}{R_1+R_2}$, weil man Zähler und Nenner mit $R_1R_2$ erweitert.
:::
:::karte zusammenhang Mehr Widerstände, weniger Widerstand
Wie kann der Gesamtwiderstand sinken, wenn ein weiterer Widerstand parallel dazukommt?
---
Der neue Widerstand öffnet einen zusätzlichen Weg: Der alte Zweig führt weiter denselben Strom, der neue zusätzlichen. Bei gleicher Spannung fließt mehr, also ist $U/I$ kleiner.
--- falsch
Der neue Widerstand nimmt dem vorhandenen einen Teil der Spannung ab. Mit weniger Spannung führt jeder Zweig weniger Strom, und der Widerstand sinkt.
--- falsch
Er sinkt nur, wenn der neue Widerstand kleiner ist als der vorhandene. Ein größerer paralleler Widerstand erhöht dagegen den Gesamtwiderstand, weil er den Strom zusätzlich bremst.
--- falsch
Der neue Widerstand kühlt den vorhandenen, weil sich die Wärme auf zwei Bauteile verteilt. Kühlere Widerstände leiten besser.
:::
:::karte begriff Lastwiderstand
Was ist der Lastwiderstand an einem Spannungsteiler, und wo liegt er?
---
Der Widerstand $R_\mathrm L$ der Stufe, die mit der Teilspannung versorgt werden soll. Er liegt parallel zu $R_2$ und entnimmt dem Abgriff den Strom $I_\mathrm L$.
--- falsch
Der Widerstand, der in Reihe vor $R_1$ liegt und den Strom aus der Quelle begrenzt. Er schützt den Teiler vor zu großem Strom.
--- falsch
Der Innenwiderstand der Quelle, die den Teiler speist. Er liegt in Reihe mit der Quelle und senkt ihre Spannung ab.
--- falsch
Der Widerstand $R_\mathrm L$ der Stufe, die mit der Teilspannung versorgt werden soll. Er liegt in Reihe mit $R_2$ und führt deshalb denselben Strom wie $R_1$.
:::
:::karte formel Belasteter Spannungsteiler
Welche Teilspannung $U_2$ liefert ein Spannungsteiler aus $R_1$ und $R_2$, wenn der Lastwiderstand $R_\mathrm L$ parallel zu $R_2$ liegt?
---
$\frac{U_2}{U}=\frac{R_2\parallel R_\mathrm L}{R_1+R_2\parallel R_\mathrm L}$: Man setzt $R_2\parallel R_\mathrm L$ statt $R_2$ in die Teilerregel ein. Für $R_\mathrm L\to\infty$ folgt die unbelastete Regel.
--- falsch
$\frac{U_2}{U}=\frac{R_2}{R_1+R_2}$, gleich wie groß $R_\mathrm L$ ist: Die Last liegt parallel zu $R_2$ und erhält deshalb dieselbe Spannung wie ohne jede Last.
--- falsch
$\frac{U_2}{U}=\frac{R_2+R_\mathrm L}{R_1+R_2+R_\mathrm L}$: Man setzt $R_2+R_\mathrm L$ statt $R_2$ ein. Mit der Last steigt die Teilspannung also.
--- falsch
$\frac{U_2}{U}=\frac{R_2\parallel R_\mathrm L}{R_1+R_2\parallel R_\mathrm L}$: Man setzt $R_2\parallel R_\mathrm L$ statt $R_2$ ein. Für $R_\mathrm L\to0$ folgt die unbelastete Regel.
:::
:::karte zusammenhang Belastung senkt die Teilspannung
Warum sinkt die Spannung am Mittelknoten eines Spannungsteilers, wenn man ihn belastet?
---
Am Mittelknoten öffnet sich ein zusätzlicher Weg: Der Gesamtwiderstand sinkt, der Strom durch $R_1$ steigt, an $R_1$ fällt mehr ab, das Mittelpotenzial sinkt.
--- falsch
Weil der Lastwiderstand Spannung verbraucht: Was die Last an Spannung aufnimmt, fehlt danach an $R_2$, und $U_2$ sinkt um genau diesen Betrag.
--- falsch
Weil der Strom durch $R_1$ sinkt: Ein Teil des Stroms fließt nun durch die Last, und für $R_1$ bleibt weniger Strom übrig.
--- falsch
Weil die Quelle mit der Last mehr Strom liefern muss und ihre Spannung deshalb sinkt. Mit einer idealen Quelle ohne diese Schwäche bliebe $U_2$ gleich.
:::
:::karte formel Fehler durch Belastung
Wie groß ist der relative Fehler $\delta$ der Teilspannung, den ein Lastwiderstand $R_\mathrm L$ verursacht?
---
Mit $\delta=(U_{2,0}-U_2)/U_{2,0}$ ist $\delta=R_\mathrm i/(R_\mathrm i+R_\mathrm L)$, wobei $R_\mathrm i=R_1\parallel R_2$. Der Teiler wirkt wie eine Quelle mit dem Innenwiderstand $R_\mathrm i$.
--- falsch
$\delta=R_\mathrm L/(R_\mathrm i+R_\mathrm L)$ mit $R_\mathrm i=R_1\parallel R_2$. Der Fehler wird also umso kleiner, je kleiner der Lastwiderstand ist.
--- falsch
$\delta=R_\mathrm i/(R_\mathrm i+R_\mathrm L)$ mit $R_\mathrm i=R_1+R_2$. Die Last ist unmerklich, sobald $R_\mathrm L$ größer ist als die Summe der beiden Teilerwiderstände $R_1$ und $R_2$.
--- falsch
$\delta=R_2/R_\mathrm L$, unabhängig von $R_1$. Der Fehler hängt nur davon ab, wie groß die Last im Vergleich zum unteren Widerstand ist.
:::
:::karte zusammenhang Teiler aus kleineren Widerständen
Was ändert sich, wenn man einen Spannungsteiler im selben Verhältnis aus zehnmal kleineren Widerständen aufbaut?
---
$R_\mathrm i=R_1\parallel R_2$ wird zehnmal kleiner, und der Fehler unter Last sinkt. Dafür fließt im Teiler der zehnfache Strom, und er setzt die zehnfache Leistung in Wärme um.
--- falsch
Nichts: Das Verhältnis bleibt gleich, also auch die Teilspannung, der Fehler unter Last, der Strom und die Leistung im Teiler.
--- falsch
$R_\mathrm i$ wird zehnmal kleiner, und der Fehler unter Last sinkt. Strom und Leistung im Teiler bleiben aber gleich, weil die Quellenspannung und das Verhältnis gleich bleiben.
--- falsch
$R_\mathrm i$ wird zehnmal größer, und der Fehler unter Last steigt. Dafür sinken Strom und Leistung im Teiler auf ein Zehntel.
:::
:::karte zusammenhang R-2R-Leiter
Warum halbiert sich in einer R-2R-Leiter der Strom von Knoten zu Knoten?
---
Wegen der Selbstähnlichkeit: Am letzten Knoten liegt $2R\parallel2R=R$, mit dem $R$ davor wieder $2R$. So blickt jeder Knoten nach rechts und nach unten auf je $2R$, und sein Strom teilt sich 1:1.
--- falsch
Weil jeder Widerstand $2R$ doppelt so groß ist wie der Widerstand $R$ davor. Der Strom halbiert sich, weil sich der Widerstand der Zweige von Knoten zu Knoten jeweils verdoppelt.
--- falsch
Weil an jedem Knoten die Hälfte des Stroms in Wärme umgesetzt wird. Nur die andere Hälfte erreicht den nächsten Knoten der Leiter.
--- falsch
Weil die Schalter jeden zweiten Strom abschalten. Je nach Zahl am Eingang halbiert oder verdoppelt sich der Strom von Knoten zu Knoten.
:::
::::
