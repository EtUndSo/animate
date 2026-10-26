---
title: Kleinsignalmodell des MOSFET
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030500
summary: Wie man den MOSFET für kleine Änderungen um einen Arbeitspunkt durch ein lineares Ersatzschaltbild ersetzt und woher Steilheit, Ausgangsleitwert und Substratsteilheit kommen. Ausführliche Fassung mit der Linearisierung und ihrer Fehlergrenze, den drei Kleinsignalgrößen im Abschnür- und im ohmschen Bereich, der Richtung der Substratsteilheit am Sourcefolger, dem statischen und dynamischen Ersatzschaltbild mit Bahnwiderständen, Transitfrequenz, Steilheit je Strom und der SPICE-Modellkarte des Beispieltransistors.
tags: Steilheit, Ausgangsleitwert, Substratsteilheit, Kleinsignalersatzschaltbild, SPICE-Modell
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Ein Verstärker legt den Transistor mit Gleichspannungen in einen Arbeitspunkt und überlagert ihm ein kleines Signal, wenige Millivolt am Gate. Um zu berechnen, was am Ausgang ankommt, bräuchte man mit den Kennliniengleichungen jedes Mal ein nichtlineares Gleichungssystem. Für kleine Änderungen geht es kürzer: Der Transistor verhält sich dann linear und lässt sich durch ein Ersatzschaltbild aus gesteuerten Quellen, Leitwerten und Kondensatoren ersetzen, mit dem die Netzwerkanalyse rechnet. Alles hängt an einem Prinzip:

**Um einen festen Arbeitspunkt ersetzt man jede Kennlinie des MOSFET durch ihre Tangente: Gate, Drain und Bulk steuern den Drainstrom dann linear, jeder mit einer eigenen Steilheit, die vom Arbeitspunkt abhängt, und für schnelle Änderungen kommen die Kapazitäten zwischen den Anschlüssen hinzu.**

Vorausgesetzt werden die Linearisierung aus [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html), das Großsignalmodell aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html), der Substrateffekt aus [PMOS-Transistor, Substrateffekt und Latch-Up](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/pmos-substrateffekt-latch-up-ausfuehrlich.html) und die Kapazitäten aus [Parasitäre Kapazitäten des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/parasitaere-kapazitaeten-ausfuehrlich.html). Auf diesem Artikel bauen alle Transistorgrundschaltungen, ihr Frequenzgang und der Differenzverstärker auf.

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-tangenten-uebersicht · Vorlage: kennlinien-tangenten-esb
**Abbildung 1:** Drei kleine Diagramme des Beispiel-NMOS im Arbeitspunkt $U_{GS}$ = 1 V, $U_{DS}$ = 1 V, $U_{BS}$ = 0 mit 0,275 mA, jeweils mit Tangente: (a) Drainstrom über $U_{GS}$, Steigung 1,1 mS; (b) über $U_{DS}$, Steigung 25 µS; (c) über $U_{BS}$, Steigung 0,36 mS. Daneben das Kleinsignal-Ersatzschaltbild: Gate offen, zwischen Drain und Source die gesteuerten Quellen $g_m u_{GS}$ und $g_{mB} u_{BS}$ und der Leitwert $g_o$; jede Steigung führt mit einem Pfeil zu ihrem Bauelement. Jede Steigung im Arbeitspunkt wird ein Bauelement des Ersatzschaltbilds.
:::

## Linearisierung im Arbeitspunkt

*Wie wird aus den nichtlinearen Kennlinien ein lineares Modell für kleine Änderungen?*

Der Beispieltransistor arbeitet mit $U_{GS}$ = 1 V und $U_{DS}$ = 1 V im Abschnürbereich, Source und Bulk an Masse; es fließen 0,275 mA. Hebt man das Gate um 10 mV an, steigt der Drainstrom um 11,11 µA; die Tangente an die Übertragungskennlinie, 1,1 mS, sagt 11,00 µA voraus. Hebt man stattdessen den Drain um 100 mV an, steigt der Strom um 2,5 µA, und senkt man den Bulk um 100 mV, sinkt er um 34 µA. Jede der drei Spannungen wirkt mit ihrer eigenen Steigung, und für kleine Änderungen addieren sich die Wirkungen ([Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html)).

In Worten: Die __Kleinsignalgrößen__ des MOSFET sind die Steigungen seiner Kennlinien im Arbeitspunkt, je eine für jede der drei Spannungen, von denen der Drainstrom abhängt; dabei bleiben jeweils die beiden anderen Spannungen fest.

**Die Akteure:**

- __$u_{GS}$__, __$u_{DS}$__, __$u_{BS}$__, __$i_D$__: kleine Änderungen der drei Spannungen und des Drainstroms gegenüber dem Arbeitspunkt; Kleinbuchstaben kennzeichnen diese Änderungen. Der Arbeitspunkt selbst trägt Großbuchstaben, beim Beispiel 1 V, 1 V, 0 V und 0,275 mA.
- __$g_m$__: __Steilheit__, auch Transkonduktanz, die Änderung des Drainstroms je Volt Gate-Source-Spannung; 1,1 mS im Arbeitspunkt.
- __$g_o$__: __Ausgangsleitwert__, die Änderung des Drainstroms je Volt Drain-Source-Spannung; 25 µS. Üblich ist auch $g_{DS}$; der Kehrwert $r_o$, 40 kΩ, heißt __Ausgangswiderstand__.
- __$g_{mB}$__: __Substratsteilheit__, die Änderung des Drainstroms je Volt Bulk-Source-Spannung; 0,36 mS.

:::formel Definition
$$g_m = \frac{\partial I_D}{\partial U_{GS}}, \qquad g_o = \frac{\partial I_D}{\partial U_{DS}}, \qquad g_{mB} = \frac{\partial I_D}{\partial U_{BS}}$$
:::

Man definiert sie so, weil im linearisierten Modell jede Steigung die Rolle eines linearen Bauelements übernimmt: Die Steigung nach der eigenen Spannung des Drain-Source-Pfads, $g_o$, wird ein Leitwert; die Steigungen nach Spannungen an anderen Anschlüssen werden gesteuerte Quellen. Mit ihnen gilt für kleine Änderungen

:::formel Formel
$$i_D = g_m\,u_{GS} + g_o\,u_{DS} + g_{mB}\,u_{BS}$$
:::

**So liest man das:** Eingaben sind die drei kleinen Spannungsänderungen, Ausgabe die Änderung des Drainstroms. Jede Spannung trägt mit ihrer eigenen Steigung bei, und die Beiträge addieren sich. Alle drei Steigungen gelten nur für den Arbeitspunkt, in dem sie berechnet sind; den Gleichstrom 0,275 mA enthält die Formel nicht mehr.

**Kurz gesagt:** Für kleine Änderungen ist die Änderung des Drainstroms die Summe der Änderungen, die jede der drei Spannungen allein bewirken würde.

Idee der Herleitung: Man ersetzt den Strom in der Nähe des Arbeitspunkts durch die Tangentialebene, also durch die ersten Glieder seiner Taylor-Entwicklung.

:::herleitung
**Ausgangspunkt:** die Linearisierung bei mehreren Steuergrößen aus [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html), dort hergeleitet: Ändert man mehrere Steuerspannungen ein wenig, ändert sich der Strom um die Summe der partiellen Ableitungen mal den Änderungen, bis auf einen Rest, der mit dem Quadrat der Änderungen wächst. Dazu das Großsignalmodell $I_D(U_{GS}, U_{DS}, U_{BS})$ aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html) mit der Schwelle aus dem Substrateffekt.

**Annahmen:**
(i) Die Änderungen sind so klein, dass der quadratische Rest vernachlässigbar ist;
(ii) der Arbeitspunkt liegt innerhalb eines Bereichs; auf der Grenze zwischen ohmschem Bereich und Abschnürbereich sind die Steigungen zwar stetig, die Fehlerabschätzung unten gilt dort aber nicht.

**Schritt 1**: Der Strom an der Stelle Arbeitspunkt plus Änderung, mit dem Index A für den Arbeitspunkt:

$$I_D = I_D\big(U_{GS,A} + u_{GS},\ U_{DS,A} + u_{DS},\ U_{BS,A} + u_{BS}\big)$$

**Schritt 2** (entscheidender Schritt): Linearisierung nach allen drei Spannungen, die Ableitungen im Arbeitspunkt genommen:

$$I_D \approx I_{D,A} + \frac{\partial I_D}{\partial U_{GS}}\,u_{GS} + \frac{\partial I_D}{\partial U_{DS}}\,u_{DS} + \frac{\partial I_D}{\partial U_{BS}}\,u_{BS}$$

**Schritt 3**: Die Änderung des Stroms ist $I_D$ minus $I_{D,A}$; mit den Namen der Definition folgt

$$i_D = g_m\,u_{GS} + g_o\,u_{DS} + g_{mB}\,u_{BS}$$

**Ergebnis:**

$$i_D = g_m\,u_{GS} + g_o\,u_{DS} + g_{mB}\,u_{BS}$$

**Woher die Faktoren kommen:** Jeder Faktor ist eine Steigung im Arbeitspunkt; der Gleichanteil fällt heraus, weil man nur Änderungen betrachtet.

**Proben:** Einheit S · V = A. Beim Beispiel: 1,1 mS · 10 mV = 11,0 µA gegen 11,11 µA nach der Großsignalgleichung; 25 µS · 100 mV = 2,5 µA, genau. Grenzfall: Ohne Änderungen ist $i_D$ null.

**Grenzen:** Größere Änderungen erzeugen den quadratischen Rest, im Abschnürbereich relativ $u_{GS}/(2(U_{GS} - U_{th}))$, siehe unten. An der Grenze zwischen den Bereichen springen die Steigungen nicht, wohl aber die Krümmung; die Fehlerabschätzung mit dem quadratischen Rest gilt dort nicht mehr.
:::

:::merke
Alle Kleinsignalgrößen gehören zu genau einem Arbeitspunkt. Man bestimmt zuerst den Arbeitspunkt mit den Großsignalgleichungen und rechnet erst dann mit dem Kleinsignalmodell; ändert sich der Arbeitspunkt, ändern sich auch Steilheit, Ausgangsleitwert und Substratsteilheit.
:::

:::frage
„Wozu ein Kleinsignalmodell, wenn ich doch die Kennliniengleichung habe?“
Die Kennliniengleichung ist nichtlinear; jede Schaltung mit ihr führt auf ein Gleichungssystem, das man nur schrittweise lösen kann. Das Kleinsignalmodell ist linear: Ströme und Spannungen überlagern sich, man kann mit Knotenanalyse, Impedanzen und Zeigern rechnen und Verstärkung, Eingangs- und Ausgangswiderstand in einer Zeile angeben. Die Arbeit teilt sich in zwei Schritte: den Arbeitspunkt einmal nichtlinear bestimmen, dann das Signal linear rechnen. Für 10 mV am Gate des Beispieltransistors kostet das nur 1 % Genauigkeit.
:::

Wie klein ein Signal sein muss, zeigt der Vergleich mit der Großsignalgleichung. Im Abschnürbereich wächst der Strom mit dem Quadrat der Übersteuerung $U_{GS} - U_{th}$, um die die Gatespannung über der Schwelle liegt; eine Änderung $u_{GS}$ liefert deshalb neben dem linearen Anteil einen quadratischen. Beim Beispiel mit 0,5 V Übersteuerung weicht der wirkliche Strom bei 10 mV um 1 % von der Tangente ab, bei 100 mV um 10 %; maßgeblich ist das Verhältnis der Signalspannung zur doppelten Übersteuerung:

$$\frac{\Delta I_D - g_m\,u_{GS}}{g_m\,u_{GS}} = \frac{u_{GS}}{2\,\big(U_{GS} - U_{th}\big)}$$

**So liest man das:** Die relative Abweichung wächst linear mit der Signalspannung und hat ihr Vorzeichen: Bei steigendem Gate ist der Strom größer, bei fallendem kleiner als die Tangente angibt. Je kleiner die Übersteuerung, desto kleiner muss das Signal sein; bei 0,1 V Übersteuerung ergäben 10 mV schon 5 %.

Idee der Herleitung: Man entwickelt das Quadratgesetz exakt und vergleicht mit dem linearen Glied.

:::herleitung
**Ausgangspunkt:** das Quadratgesetz mit Kanallängenmodulation aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html):

$$I_D = \frac{K}{2}\,\big(U_{GS} - U_{th}\big)^2\,\big(1 + \lambda\,U_{DS}\big)$$

**Annahmen:**
(i) Abschnürbereich vor und nach der Änderung;
(ii) nur die Gatespannung ändert sich.

**Schritt 1**: Mit der Übersteuerung im Arbeitspunkt, kurz $U_\text{ü}$ für $U_{GS} - U_{th}$, ist die exakte Stromänderung

$$\Delta I_D = \frac{K}{2}\Big[\big(U_\text{ü} + u_{GS}\big)^2 - U_\text{ü}^2\Big]\big(1 + \lambda\,U_{DS}\big)$$

**Schritt 2**: Ausmultipliziert:

$$\Delta I_D = K\,U_\text{ü}\,\big(1 + \lambda\,U_{DS}\big)\,u_{GS} + \frac{K}{2}\,\big(1 + \lambda\,U_{DS}\big)\,u_{GS}^2$$

**Schritt 3** (entscheidender Schritt): Der erste Summand ist $g_m u_{GS}$; der zweite, geteilt durch den ersten, ergibt die relative Abweichung:

$$\frac{\Delta I_D - g_m\,u_{GS}}{g_m\,u_{GS}} = \frac{u_{GS}}{2\,U_\text{ü}}$$

**Ergebnis:** die Formel oben, mit $U_{GS} - U_{th}$ statt $U_\text{ü}$.

**Woher die Faktoren kommen:** Die 2 im Nenner stammt aus der Ableitung des Quadrats; der Faktor $(1 + \lambda U_{DS})$ kürzt sich heraus.

**Proben:** Einheit V/V. Bei 10 mV und 0,5 V: 0,01/1 = 1 %; die Großsignalgleichung ergibt 11,11 µA statt 11,00 µA. Bei −100 mV: −10 %, 99 µA statt 110 µA.

**Grenzen:** Gilt nur im Abschnürbereich; im ohmschen Bereich und nahe der Schwelle ist die Kennlinie anders gekrümmt.
:::

::::beispiel Wie klein ein kleines Signal sein muss
**Gegeben:** Beispiel-NMOS mit $K$ = 2 mA/V², $U_{th}$ = 0,5 V, λ = 0,1 1/V im Arbeitspunkt $U_{GS}$ = 1 V, $U_{DS}$ = 1 V, also mit der Übersteuerung $U_\text{ü}$ = 0,5 V; Steilheit dort 1,1 mS.

**Gesucht:** die exakte Stromänderung und die Abweichung von der Tangente für $u_{GS}$ = 10 mV, 100 mV und −100 mV; der Anteil der zweiten Harmonischen bei einem Sinus von 10 mV Amplitude.

**Rechnung:** Exakte Änderung für 10 mV:

$$\Delta I_D = 1\ \mathrm{mA/V^2}\cdot\big(0{,}51^2 - 0{,}5^2\big)\ \mathrm{V^2}\cdot1{,}1 = 11{,}11\ \mathrm{\mu A}$$

Abweichung von $g_m u_{GS}$ = 11,00 µA:

$$\frac{u_{GS}}{2\,U_\text{ü}} = \frac{10\ \mathrm{mV}}{1\ \mathrm V} = 1\,\%$$

Für ±100 mV ergibt dieselbe Rechnung 121 µA bzw. −99 µA gegen ±110 µA, also +10 % und −10 %. Bei einem Sinus mit der Amplitude $\hat u$ wird aus dem quadratischen Glied ein Anteil mit doppelter Frequenz, die zweite Harmonische; ihr Verhältnis zur Grundwelle ist halb so groß wie die Abweichung bei der Amplitude:

$$\frac{\hat u}{4\,U_\text{ü}} = \frac{10\ \mathrm{mV}}{2\ \mathrm V} = 0{,}5\,\%$$

**Ergebnis:** **10 mV: 11,11 µA statt 11,00 µA, 1 % Abweichung, 0,5 % zweite Harmonische; 100 mV: 10 % Abweichung.**

**Einordnung:** Bei einigen Millivolt ist das Kleinsignalmodell praktisch exakt, bei 100 mV schon merklich falsch. Die Grenze setzt die Übersteuerung, nicht die Gatespannung selbst: Derselbe Transistor mit 0,1 V Übersteuerung verträgt nur ein Fünftel des Signals.
::::

## Die Steilheit

*Wie stark steuert das Gate den Drainstrom im Arbeitspunkt, und wovon hängt das ab?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-steilheit · Vorlage: kennlinie-tangente-gestapelt
**Abbildung 2:** Zwei gestapelte Diagramme über $U_{GS}$ von 0 bis 2 V bei $U_{DS}$ = 1 V. Oben der Drainstrom: null bis zur Schwelle 0,5 V, 0,275 mA bei 1 V, 1,1 mA bei 1,5 V; die Tangente in 1 V mit 1,1 mS trifft die Spannungsachse bei 0,75 V; schattiert die Abweichung der Kurve von der Tangente bei ±10 mV (±1 %) und ±100 mV (±10 %). Unten die Steilheit: null unterhalb der Schwelle, dann linear auf 1,1 mS bei 1 V und 2,2 mS bei 1,5 V, gestrichelt die Näherung ohne den Faktor 1,1. Die Steilheit ist die Steigung der Übertragungskennlinie im Arbeitspunkt und wächst mit der Übersteuerung.
:::

Im Abschnürbereich wächst der Drainstrom mit dem Quadrat der Übersteuerung, weil zwei Größen mit ihr wachsen: die Ladung im Kanal an der Source und die Spannung, die längs des Kanals bis zum Abschnürpunkt abfällt ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html)). Die Steigung einer Parabel wächst linear: Bei doppelter Übersteuerung ist die Steilheit doppelt so groß, beim Beispiel 2,2 mS bei $U_{GS}$ = 1,5 V statt 1,1 mS bei 1 V (Abbildung 2). Im ohmschen Bereich legt dagegen die Drain-Source-Spannung den Spannungsabfall längs des Kanals fest; eine höhere Gatespannung vermehrt nur die Ladung, und die Steilheit ist proportional zu $U_{DS}$, bei 0,1 V nur 0,202 mS.

**Die Akteure:**

- __$K$__: Steilheitskoeffizient, $K' W/L$ mit dem Prozessparameter $K' = \mu_n C'_\mathrm{ox}$; 2 mA/V² beim Beispieltransistor.
- __$U_\text{ü}$__: Übersteuerung im Arbeitspunkt, $U_{GS} - U_{th}$; 0,5 V bei $U_{GS}$ = 1 V.
- __$\lambda$__: Kanallängenmodulationsfaktor; 0,1 1/V.

:::formel Formel
Abschnürbereich:

$$g_m = K\,U_\text{ü}\,\big(1 + \lambda\,U_{DS}\big) = \frac{2\,I_D}{U_\text{ü}}$$

Ohmscher Bereich:

$$g_m = K\,U_{DS}\,\big(1 + \lambda\,U_{DS}\big)$$
:::

**So liest man das:** Im Abschnürbereich gibt es drei Lesarten derselben Größe. $K U_\text{ü}$ zeigt, dass ein breiterer Transistor bei gleicher Übersteuerung mehr Steilheit hat; $2I_D/U_\text{ü}$, dass ein Milliampere Strom umso mehr Steilheit bringt, je kleiner die Übersteuerung ist. Ohne Kanallängenmodulation ist die Steilheit außerdem die Wurzel aus $2 K I_D$: Bei festem Transistor wächst sie nur mit der Wurzel des Stroms. Mit dem Faktor $(1 + \lambda U_{DS})$ ist diese dritte Form nur genähert, 1,049 mS statt 1,1 mS beim Beispiel. Im ohmschen Bereich wächst $g_m$ mit $U_{DS}$; an der Grenze, bei $U_{DS}$ = 0,5 V, liefern beide Ausdrücke 1,05 mS, die Steilheit springt also nicht.

**Kurz gesagt:** Im Abschnürbereich wächst die Steilheit bei fester Übersteuerung proportional zum Drainstrom.

Idee der Herleitung: Man leitet die Stromgleichung des jeweiligen Bereichs nach $U_{GS}$ ab und hält $U_{DS}$ fest.

:::herleitung
**Ausgangspunkt:** das Großsignalmodell aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html):

$$I_D = \frac{K}{2}\,U_\text{ü}^2\,\big(1 + \lambda\,U_{DS}\big) \quad \text{(Abschnürbereich)}$$

$$I_D = K\,U_{DS}\,\Big(U_\text{ü} - \frac{U_{DS}}{2}\Big)\big(1 + \lambda\,U_{DS}\big) \quad \text{(ohmscher Bereich)}$$

**Annahmen:**
(i) Bulk an Source, die Schwelle ist fest;
(ii) $U_{GS}$ ändert $U_\text{ü}$ Volt für Volt.

**Schritt 1**: Abschnürbereich, nach $U_\text{ü}$ abgeleitet:

$$g_m = \frac{K}{2}\cdot2\,U_\text{ü}\,\big(1 + \lambda\,U_{DS}\big) = K\,U_\text{ü}\,\big(1 + \lambda\,U_{DS}\big)$$

**Schritt 2** (entscheidender Schritt): Teilt man $g_m$ durch $I_D$, kürzen sich $K$ und der Faktor der Kanallängenmodulation:

$$\frac{g_m}{I_D} = \frac{K\,U_\text{ü}\,\big(1 + \lambda U_{DS}\big)}{\tfrac{K}{2}\,U_\text{ü}^2\,\big(1 + \lambda U_{DS}\big)} = \frac{2}{U_\text{ü}}$$

**Schritt 3**: Ohne Kanallängenmodulation ist $U_\text{ü}$ gleich $\sqrt{2 I_D/K}$, also

$$g_m = K\,\sqrt{\frac{2\,I_D}{K}} = \sqrt{2\,K\,I_D}$$

**Schritt 4**: Ohmscher Bereich: In der Klammer hängt nur $U_\text{ü}$ von $U_{GS}$ ab, mit der Ableitung 1:

$$g_m = K\,U_{DS}\,\big(1 + \lambda\,U_{DS}\big)$$

**Ergebnis:** die Formeln oben.

**Woher die Faktoren kommen:** Die 2 in $2I_D/U_\text{ü}$ ist der Exponent des Quadratgesetzes; im ohmschen Bereich steht $U_{DS}$ an der Stelle der Übersteuerung, weil dort die Spannung längs des Kanals fest ist.

**Proben:** Einheit A/V² · V = S. Bei 1 V/1 V: 2 mA/V² · 0,5 V · 1,1 = 1,1 mS; 2 · 0,275 mA / 0,5 V = 1,1 mS. An der Grenze $U_{DS}$ = $U_\text{ü}$ stimmen beide Bereiche überein, 1,05 mS bei 0,5 V.

**Grenzen:** Mit Substrateffekt hängt $U_{th}$ von $U_{BS}$ ab, das ändert die Formel für $g_m$ nicht, kommt aber als eigene Steilheit hinzu (Abschnitt *Die Substratsteilheit*). Bei kurzen Kanälen sättigt die Geschwindigkeit der Elektronen, und $g_m$ wächst schwächer als linear mit der Übersteuerung.
:::

::::beispiel Steilheit des Beispieltransistors
**Gegeben:** Beispiel-NMOS mit $K$ = 2 mA/V², $U_{th}$ = 0,5 V, λ = 0,1 1/V; (a) $U_{GS}$ = 1 V, $U_{DS}$ = 1 V mit 0,275 mA; (b) $U_{GS}$ = 1,5 V, $U_{DS}$ = 1 V; (c) $U_{GS}$ = 1 V, $U_{DS}$ = 0,1 V.

**Gesucht:** die Steilheit in allen drei Arbeitspunkten, in (a) in allen drei Formen.

**Rechnung:** (a) Abschnürbereich, weil 1 V über 0,5 V liegt:

$$g_m = 2\ \mathrm{mA/V^2}\cdot0{,}5\ \mathrm V\cdot1{,}1 = 1{,}1\ \mathrm{mS}, \qquad \frac{2\cdot0{,}275\ \mathrm{mA}}{0{,}5\ \mathrm V} = 1{,}1\ \mathrm{mS}$$

$$\sqrt{2\cdot2\ \mathrm{mA/V^2}\cdot0{,}275\ \mathrm{mA}} = 1{,}049\ \mathrm{mS}$$

(b) Übersteuerung 1 V, wieder Abschnürbereich, Strom 1,1 mA:

$$g_m = 2\ \mathrm{mA/V^2}\cdot1\ \mathrm V\cdot1{,}1 = 2{,}2\ \mathrm{mS}$$

(c) Ohmscher Bereich, weil 0,1 V unter 0,5 V liegt:

$$g_m = 2\ \mathrm{mA/V^2}\cdot0{,}1\ \mathrm V\cdot1{,}01 = 0{,}202\ \mathrm{mS}$$

**Ergebnis:** **(a) 1,1 mS, mit der Wurzelform 1,049 mS; (b) 2,2 mS; (c) 0,202 mS.**

**Einordnung:** Viermal so viel Strom bringt in (b) nur die doppelte Steilheit, denn die Übersteuerung hat sich ebenfalls verdoppelt. Im ohmschen Bereich hat derselbe Transistor bei gleicher Gatespannung nur ein Fünftel der Steilheit. In Handrechnungen lässt man den Faktor 1,1 oft weg und rechnet mit 1 mS, wie in der Netzwerkanalyse dieser Reihe.
::::

:::fehlvorstellung
„Die Steilheit ist eine feste Eigenschaft des Transistors, wie seine Weite.“ Das liegt nahe, weil Datenblätter für Einzeltransistoren einen Wert der Steilheit nennen. Er gilt aber nur für den dort angegebenen Arbeitspunkt. Beim Beispieltransistor sind es 1,1 mS bei 0,275 mA, 2,2 mS bei 1,1 mA und im ohmschen Bereich bei 0,1 V nur 0,202 mS. Fest ist nur der Steilheitskoeffizient $K$; die Steilheit folgt aus ihm und dem Arbeitspunkt.
:::

:::frage
„Warum lässt man den Faktor $(1 + \lambda U_{DS})$ oft weg, wenn er bei 1 V schon 10 % ausmacht?“
Weil er Steilheit und Strom gleichermaßen vergrößert und in Handrechnungen meist andere Unsicherheiten überwiegen: λ selbst ist ein Modellwert, und die Schwellenspannung streut von Exemplar zu Exemplar. Rechnet man mit dem gemessenen oder berechneten Strom, ist die Form $2I_D/U_\text{ü}$ ohnehin exakt, auch mit Kanallängenmodulation. Die Werte 1 mS und 25 µS, mit denen die Netzwerkanalyse dieser Reihe rechnet, sind diese Handrechnungswerte; genau sind es im Arbeitspunkt 1 V/1 V 1,1 mS und 25 µS.
:::

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-gm-id · Vorlage: kennlinie-semilog
**Abbildung 3:** Steilheit je Strom $g_m/I_D$ in 1/V über $U_{GS}$ von 0,2 bis 1,5 V bei $U_{DS}$ = 1 V. Unterhalb der Schwelle fast waagerecht bei 27,9 1/V, gestrichelt die Grenze $1/U_T$ = 38,7 1/V; oberhalb fällt sie wie $2/(U_{GS} - U_{th})$: 20 1/V bei 0,6 V, 8 1/V bei 0,75 V, 4 1/V bei 1 V und 2 1/V bei 1,5 V; der Übergang um die Schwelle ist als „im Modell nicht beschrieben“ markiert. Je kleiner die Übersteuerung, desto mehr Steilheit bringt ein Milliampere Strom; unterhalb der Schwelle ist das Verhältnis am größten.
:::

:::vertiefung
**Wie man mit wenig Strom viel Steilheit bekommt.** Das Verhältnis $g_m/I_D$ ist $2/U_\text{ü}$, beim Beispiel 4 1/V bei 0,5 V Übersteuerung: Für 1 mS braucht man 0,25 mA. Bei 0,1 V Übersteuerung sind es 20 1/V, für 1 mS also nur 50 µA, dafür muss der Transistor fünfmal so breit sein und hat fünfmal so viel Kapazität (Abbildung 3). Unterhalb der Schwelle wächst der Strom exponentiell mit der Gatespannung, um eine Dekade je 83 mV ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html)); dort ist $g_m/I_D$ fest, beim Beispiel 27,9 1/V, unterhalb der Grenze $1/U_T$ = 38,7 1/V, die auch der Bipolartransistor erreicht. Ein Transistor, der so breit ist, dass er bei 36 µA noch unterhalb der Schwelle arbeitet, liefert 1 mS. Entwürfe für geringe Leistung legen deshalb die Übersteuerung bewusst klein und wählen sie nach dem Verhältnis $g_m/I_D$ statt nach der Gatespannung.
:::

## Der Ausgangsleitwert

*Wie stark wirkt die Drainspannung auf den Drainstrom zurück?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-ausgangsleitwert · Vorlage: kennlinie-tangente-gestapelt
**Abbildung 4:** Oben der Drainstrom über $U_{DS}$ bei $U_{GS}$ = 1 V, von −10 V bis 2,5 V mit Achsenbruch zwischen −10 V und 0: ohmscher Bereich bis 0,5 V, danach Abschnürbereich mit der Steigung 25 µS, 0,275 mA bei 1 V und 0,3 mA bei 2 V; die Tangente bei 1 V trifft die Spannungsachse bei −10 V. Unten Steilheit und Ausgangsleitwert über $U_{DS}$ von 0 bis 2,5 V: $g_o$ fällt von 1 mS bei 0 über 0,817 mS bei 0,1 V und 0,433 mS bei 0,3 V auf 25 µS ab 0,5 V, $g_m$ steigt von 0 über 0,202 mS und 0,618 mS auf 1,05 mS bei 0,5 V und 1,1 mS bei 1 V; beide Kurven ohne Sprung an der Abschnürgrenze. Im Abschnürbereich ist der Ausgangsleitwert klein und die Steilheit groß, im ohmschen Bereich umgekehrt.
:::

Im Abschnürbereich erreicht der Teil der Drainspannung, der über die Übersteuerung hinausgeht, den Kanal nicht mehr; er fällt über der kurzen verarmten Zone vor dem Drain ab. Nur weil sich der Abschnürpunkt mit wachsender Drainspannung ein wenig zur Source verschiebt und der Kanal kürzer wird, steigt der Strom noch leicht, die __Kanallängenmodulation__ ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien-ausfuehrlich.html)). Der Ausgangsleitwert ist deshalb klein, beim Beispiel 25 µS, der Ausgangswiderstand 40 kΩ (Abbildung 4). Im ohmschen Bereich ist der Kanal dagegen ein Widerstand zwischen Source und Drain, und die Drainspannung treibt den Strom unmittelbar: Bei 0,1 V sind es 0,817 mS, mehr als die Steilheit.

**Die Akteure:**

- __$U_A$__: Early-Spannung, der Kehrwert von λ; 10 V. Die Tangenten an die Ausgangskennlinien im Abschnürbereich treffen die Spannungsachse bei $-U_A$.
- __$r_o$__: Ausgangswiderstand, der Kehrwert von $g_o$; 40 kΩ im Arbeitspunkt.

:::formel Formel
Abschnürbereich:

$$g_o = \frac{\lambda K}{2}\,U_\text{ü}^2 = \frac{I_D}{U_A + U_{DS}}$$

Ohmscher Bereich:

$$\begin{aligned} g_o &= K\Big[\Big(U_\text{ü} - \frac{U_{DS}}{2}\Big)\big(1 + 2\lambda U_{DS}\big) - \frac{U_{DS}}{2}\,\big(1 + \lambda U_{DS}\big)\Big] \\ &\approx K\,\big(U_\text{ü} - U_{DS}\big) \end{aligned}$$
:::

**So liest man das:** Im Abschnürbereich ist $g_o$ der Strom geteilt durch den Abstand des Arbeitspunkts vom Schnittpunkt der Tangente bei $-U_A$, beim Beispiel 0,275 mA durch 11 V. Die oft benutzte Näherung $\lambda I_D$ liegt um den Faktor $1 + \lambda U_{DS}$ zu hoch, bei 1 V um 10 %. Im ohmschen Bereich ist $g_o$ ohne Kanallängenmodulation $K(U_\text{ü} - U_{DS})$, der Leitwert, den der Kanal hätte, wenn er überall so dünn wäre wie an seinem Drain-Ende; ohne Kanallängenmodulation fällt er bis zur Abschnürgrenze auf null, wie dort auch der Wert des Abschnürbereichs; mit Kanallängenmodulation liefern die exakten Ausdrücke beider Bereiche an der Grenze 25 µS, der Übergang ist ohne Sprung.

**Kurz gesagt:** Im Abschnürbereich ist der Ausgangsleitwert der Drainstrom geteilt durch die Summe aus Early-Spannung und Drain-Source-Spannung.

Idee der Herleitung: Man leitet die Stromgleichungen nach $U_{DS}$ ab und hält $U_{GS}$ fest.

:::herleitung
**Ausgangspunkt:** die beiden Stromgleichungen aus der vorigen Herleitung und die Early-Spannung $U_A$ als Kehrwert von λ.

**Annahmen:**
(i) Bulk an Source;
(ii) $U_{GS}$ und damit $U_\text{ü}$ fest.

**Schritt 1**: Abschnürbereich; nur der Faktor $(1 + \lambda U_{DS})$ hängt von $U_{DS}$ ab:

$$g_o = \frac{K}{2}\,U_\text{ü}^2\,\lambda$$

**Schritt 2** (entscheidender Schritt): Mit dem Strom selbst ausgedrückt, durch λ erweitert:

$$g_o = \frac{\lambda\,I_D}{1 + \lambda\,U_{DS}} = \frac{I_D}{1/\lambda + U_{DS}} = \frac{I_D}{U_A + U_{DS}}$$

**Schritt 3**: Ohmscher Bereich, Produktregel für die drei Faktoren $U_{DS}$, $(U_\text{ü} - U_{DS}/2)$ und $(1 + \lambda U_{DS})$:

$$\begin{aligned} g_o &= K\Big[\Big(U_\text{ü} - \frac{U_{DS}}{2}\Big)\big(1 + \lambda U_{DS}\big) - \frac{U_{DS}}{2}\big(1 + \lambda U_{DS}\big) \\ &\qquad + \lambda\,U_{DS}\Big(U_\text{ü} - \frac{U_{DS}}{2}\Big)\Big] \end{aligned}$$

**Schritt 4**: Der erste und der dritte Summand zusammengefasst ergeben $(U_\text{ü} - U_{DS}/2)(1 + 2\lambda U_{DS})$; ohne λ bleibt

$$g_o \approx K\,\Big(U_\text{ü} - \frac{U_{DS}}{2} - \frac{U_{DS}}{2}\Big) = K\,\big(U_\text{ü} - U_{DS}\big)$$

**Ergebnis:** die Formeln oben.

**Woher die Faktoren kommen:** Im Abschnürbereich steckt λ allein in $g_o$; im ohmschen Bereich ist $U_\text{ü} - U_{DS}$ die Übersteuerung am Drain-Ende des Kanals.

**Proben:** Einheit 1/V · A/V² · V² = S. Bei 1 V/1 V: 0,1 · 1 mA/V² · 0,25 V² = 25 µS, und 0,275 mA / 11 V = 25 µS. Bei 0,1 V ohmsch: 2 mA/V² · (0,45 · 1,02 − 0,05 · 1,01) V = 0,817 mS, genähert 0,8 mS. An der Grenze $U_{DS}$ = $U_\text{ü}$ ergibt der ohmsche Ausdruck $\lambda K U_\text{ü}^2/2$, also wieder 25 µS.

**Grenzen:** λ ist ein Modellwert; bei kurzen Kanälen wächst der Strom im Abschnürbereich stärker, und $g_o$ hängt deutlicher vom Arbeitspunkt ab.
:::

Das Verhältnis aus Steilheit und Ausgangsleitwert heißt __Eigenverstärkung__. Hängt der Drain an einer idealen Stromquelle, verstärkt eine Source-Schaltung mit diesem Faktor, mehr ist mit einem einzelnen Transistor nicht möglich ([Parasitäre Kapazitäten des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/parasitaere-kapazitaeten-ausfuehrlich.html), Abschnitt *Umladen und Miller-Effekt*). Im Abschnürbereich ist sie $2(1 + \lambda U_{DS})/(\lambda U_\text{ü})$, beim Beispiel 44, genähert 40; im ohmschen Bereich bei 0,1 V nur 0,25. Deshalb arbeiten Verstärkertransistoren im Abschnürbereich und Schalter im ohmschen Bereich.

::::beispiel Ausgangsleitwert und Eigenverstärkung des Beispieltransistors
**Gegeben:** Beispiel-NMOS mit $K$ = 2 mA/V², $U_{th}$ = 0,5 V, λ = 0,1 1/V, also $U_A$ = 10 V; (a) $U_{GS}$ = 1 V, $U_{DS}$ = 1 V mit 0,275 mA und $g_m$ = 1,1 mS; (b) $U_{GS}$ = 1 V, $U_{DS}$ = 0,1 V mit $g_m$ = 0,202 mS.

**Gesucht:** Ausgangsleitwert, Ausgangswiderstand und Eigenverstärkung.

**Rechnung:** (a) Abschnürbereich:

$$g_o = \frac{0{,}275\ \mathrm{mA}}{10\ \mathrm V + 1\ \mathrm V} = 25\ \mathrm{\mu S}, \qquad r_o = 40\ \mathrm{k\Omega}, \qquad \frac{g_m}{g_o} = \frac{1{,}1\ \mathrm{mS}}{25\ \mathrm{\mu S}} = 44$$

(b) Ohmscher Bereich:

$$g_o = 2\ \mathrm{mA/V^2}\cdot\big[0{,}45\cdot1{,}02 - 0{,}05\cdot1{,}01\big]\ \mathrm V = 0{,}817\ \mathrm{mS}, \qquad \frac{g_m}{g_o} = \frac{0{,}202}{0{,}817} = 0{,}25$$

**Ergebnis:** **(a) 25 µS, 40 kΩ, Eigenverstärkung 44; (b) 0,817 mS, Eigenverstärkung 0,25.**

**Einordnung:** Die Näherung λ$I_D$ ergäbe in (a) 27,5 µS, 10 % zu viel. Im Abschnürbereich steuert das Gate den Strom 44-mal stärker als der Drain, im ohmschen Bereich umgekehrt der Drain viermal stärker als das Gate: Dort ist der Transistor ein spannungsgesteuerter Widerstand, kein Verstärker.
::::

## Die Substratsteilheit

*Wie wirkt der Bulk auf den Drainstrom, und in welche Richtung?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-substratsteilheit · Vorlage: kennlinie-tangente-gestapelt
**Abbildung 5:** Oben der Drainstrom über $U_{BS}$ von −2,5 V bis +0,3 V bei $U_{GS}$ = 1 V und $U_{DS}$ = 1 V: praktisch null bei −2,5 V, 0,059 mA bei −1 V, 0,138 mA bei −0,5 V, 0,275 mA bei 0 und 0,406 mA bei +0,3 V; die Tangente bei 0 hat die Steigung 0,36 mS; der Bereich über 0 ist grau hinterlegt, dort beginnt die Diode zwischen Bulk und Source zu leiten. Unten η über $U_{SB}$ von 0 bis 2 V: 0,327, 0,264, 0,227, 0,202 und 0,184. Der Bulk steuert den Strom wie ein zweites, schwächeres Gate; sein Anteil η sinkt mit der Sperrspannung.
:::

**Die Akteure:**

- __$\gamma$__: Substratsteuerfaktor aus [PMOS-Transistor, Substrateffekt und Latch-Up](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/pmos-substrateffekt-latch-up-ausfuehrlich.html); 0,629 √V beim Beispiel-NMOS.
- __$2\Phi_F$__: das Oberflächenpotential an der Schwelle gegenüber dem Inneren; 0,923 V.
- __$U_{SB}$__: Sperrspannung zwischen Source und Bulk, das Negative von $U_{BS}$; 0 im Arbeitspunkt.
- __$\eta$__: Verhältnis von Substrat- zu Gatesteilheit, zugleich das Kapazitätsverhältnis $C'_\mathrm{dep}/C'_\mathrm{ox}$ von Verarmungszone und Oxid; 0,327 bei $U_{SB}$ = 0.

**Das Zusammenspiel:**

**Schritt 1**: Der Bulk wirkt über die Verarmungszone unter dem Kanal wie ein zweites Gate: Liegt er tiefer als die Source, muss die Oberfläche höher angehoben werden, die Zone wird breiter, und die Schwelle steigt (Abbildung 5, oben, links von 0).

**Schritt 2**: Für eine kleine Änderung zählt die Steigung dieses Zusammenhangs: Hebt man den Bulk um $u_{BS}$ an, sinkt die Schwelle um $\eta\,u_{BS}$, beim Beispiel um 3,3 mV je 10 mV.

**Schritt 3** (entscheidender Schritt): Eine um $\eta u_{BS}$ tiefere Schwelle wirkt auf den Strom wie eine um $\eta u_{BS}$ höhere Gatespannung, denn beide gehen nur über die Übersteuerung ein. Die Substratsteilheit ist deshalb η-mal die Steilheit, 0,36 mS beim Beispiel, in beiden Bereichen und mit demselben Vorzeichen wie $g_m$.

**Schritt 4**: Mit wachsender Sperrspannung wird die Verarmungszone tiefer, ihre Kapazität kleiner, und η sinkt: 0,227 bei 1 V, 0,184 bei 2 V (Abbildung 5, unten).

:::formel Formel
$$g_{mB} = \eta\,g_m, \qquad \eta = \frac{\gamma}{2\,\sqrt{2\Phi_F + U_{SB}}}$$
:::

**So liest man das:** Eingaben sind die Steilheit und die Sperrspannung zwischen Source und Bulk, Ausgabe die Substratsteilheit. Je höher die Dotierung unter dem Gate und je dicker das Oxid, desto größer γ und η; übliche Werte liegen zwischen 0,1 und 0,4, beim Beispiel mit seiner hohen Dotierung 0,33. Liegt der Bulk an der Source, ist $u_{BS}$ null, und die Substratsteilheit spielt keine Rolle.

**Kurz gesagt:** Der Bulk steuert den Drainstrom η-mal so stark wie das Gate.

Idee der Herleitung: Man leitet den Strom über die Schwellenspannung nach $U_{BS}$ ab (Kettenregel).

:::herleitung
**Ausgangspunkt:** die Schwellenspannung mit Substrateffekt aus [PMOS-Transistor, Substrateffekt und Latch-Up](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/pmos-substrateffekt-latch-up-ausfuehrlich.html), mit $U_{SB}$ als Negativem von $U_{BS}$:

$$U_{th} = U_{th0} + \gamma\,\Big(\sqrt{2\Phi_F + U_{SB}} - \sqrt{2\Phi_F}\Big)$$

dazu die Stromgleichungen, in denen $U_{th}$ nur über die Übersteuerung $U_{GS} - U_{th}$ vorkommt.

**Annahmen:**
(i) $U_{BS}$ höchstens wenig über null, sodass die Diode zwischen Bulk und Source sperrt;
(ii) $U_{GS}$ und $U_{DS}$ fest.

**Schritt 1**: Kettenregel: Der Strom hängt über $U_\text{ü}$ von $U_{BS}$ ab, und $U_\text{ü}$ ändert sich um das Negative der Schwellenänderung:

$$g_{mB} = \frac{\partial I_D}{\partial U_\text{ü}}\cdot\frac{\partial U_\text{ü}}{\partial U_{BS}} = g_m\cdot\Big(-\frac{\partial U_{th}}{\partial U_{BS}}\Big)$$

**Schritt 2**: Die Ableitung der Schwelle nach $U_{BS}$, mit $U_{SB}$ gleich $-U_{BS}$:

$$-\frac{\partial U_{th}}{\partial U_{BS}} = \frac{\partial U_{th}}{\partial U_{SB}} = \frac{\gamma}{2\,\sqrt{2\Phi_F + U_{SB}}} = \eta$$

**Schritt 3** (entscheidender Schritt): Eingesetzt; das gilt im Abschnürbereich und im ohmschen Bereich gleichermaßen, weil $\partial I_D/\partial U_\text{ü}$ in beiden die Steilheit ist:

$$g_{mB} = \eta\,g_m$$

**Ergebnis:**

$$g_{mB} = \eta\,g_m, \qquad \eta = \frac{\gamma}{2\,\sqrt{2\Phi_F + U_{SB}}}$$

**Woher die Faktoren kommen:** Die 1/2 und die Wurzel kommen aus der Ableitung der Wurzel in der Schwellenspannung; dass η zugleich $C'_\mathrm{dep}/C'_\mathrm{ox}$ ist, folgt, weil γ die Wurzel aus $2 e \varepsilon_\mathrm{Si} N_A$ geteilt durch $C'_\mathrm{ox}$ ist und die Verarmungszone als Plattenkondensator pro Fläche die Permittivität des Siliziums durch ihre Tiefe als Kapazität hat.

**Proben:** Einheit √V/√V, dimensionslos. Bei $U_{SB}$ = 0: 0,629/(2 · √0,923) = 0,327, und 0,327 · 1,1 mS = 0,36 mS; die Steigung der Kurve $I_D(U_{BS})$ bei null ergibt ebenfalls 0,360 mS. Bei $U_{SB}$ = 1 V: 0,629/(2 · √1,923) = 0,227.

**Grenzen:** Liegt der Bulk mehr als einige hundert Millivolt über der Source, leitet die Diode zwischen beiden, und das Modell gilt nicht mehr.
:::

:::fehlvorstellung
„Die Substratsteilheit ist negativ, denn der Substrateffekt verringert doch die Verstärkung.“ Das liegt nahe, weil der Substrateffekt in vielen Schaltungen tatsächlich Verstärkung kostet. Die Substratsteilheit selbst ist aber positiv, 0,36 mS beim Beispiel: Hebt man den Bulk an, sinkt die Schwelle, und der Strom steigt, wie bei einer höheren Gatespannung. Die Verstärkung sinkt erst in der Schaltung, weil dort meist die Source steigt, während der Bulk fest an Masse liegt; dann ist $u_{BS}$ negativ, und die Quelle nimmt Strom weg (Abschnitt *Die Substratsteilheit im Sourcefolger*).
:::

## Das statische Kleinsignal-Ersatzschaltbild

*Wie sieht der linearisierte Transistor als Schaltung aus?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-esb-statisch · Vorlage: ersatzschaltbild-paar
**Abbildung 6:** (a) Kleinsignal-Ersatzschaltbild des NMOS: Das Gate ist offen; zwischen Drain und Source liegen die gesteuerten Stromquellen $g_m u_{GS}$ und $g_{mB} u_{BS}$, beide vom Drain zur Source gerichtet, und parallel der Leitwert $g_o$; die Spannungen $u_{GS}$, $u_{DS}$ und $u_{BS}$ sind zur Source gezählt, $i_D$ in den Drain hinein. Werte im Beispiel-Arbeitspunkt: 1,1 mS, 0,36 mS und 25 µS. (b) Dasselbe Bild für den PMOS, den Drain unten gezeichnet, weil er tiefer liegt als die Source; Werte bei −1 V/−1 V: 1,1 mS, 0,353 mS und 25 µS, alle positiv. NMOS und PMOS haben dasselbe Kleinsignal-Ersatzschaltbild mit positiven Parametern.
:::

Die Gleichung für $i_D$ lässt sich als Schaltung zeichnen, das __Kleinsignal-Ersatzschaltbild__ (Abbildung 6). Das Gate ist ein offener Anschluss, denn durch das Oxid fließt kein Gleichstrom, und bei langsamen Änderungen ist auch der Strom, der die Gatekapazität umlädt, vernachlässigbar. Zwischen Drain und Source liegen zwei __spannungsgesteuerte Stromquellen__, Quellen, deren Strom von einer Spannung an anderer Stelle abhängt: $g_m u_{GS}$ und $g_{mB} u_{BS}$, beide vom Drain zur Source gerichtet, also in derselben Richtung wie der Drainstrom. Parallel dazu liegt der Leitwert $g_o$, denn ein Strom, der von der Spannung an den eigenen Anschlüssen abhängt, ist ein Leitwert.

In einer Schaltung ersetzt man den Transistor durch dieses Bild und den Rest der Schaltung durch sein Kleinsignal-Ersatzschaltbild ([Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung-ausfuehrlich.html)): Gleichspannungsquellen werden Kurzschlüsse, weil ihre Spannung sich nicht ändert, Gleichstromquellen werden Unterbrechungen, weil ihr Strom sich nicht ändert. Liegt der Bulk an der Source, ist $u_{BS}$ null, und die Quelle $g_{mB} u_{BS}$ entfällt.

:::frage
„Gilt das Ersatzschaltbild auch für den PMOS, bei dem doch alles negativ ist?“
Ja, mit denselben Richtungen und positiven Parametern. Zählt man den Drainstrom wie beim NMOS in den Drain hinein, nimmt sein Betrag ab, wenn das Gate steigt; der negative Strom wird also größer, und die Ableitung nach $U_{GS}$ ist positiv. Beim Beispiel-PMOS bei $U_{GS}$ = −1 V und $U_{DS}$ = −1 V sind es $g_m$ = 1,1 mS, $g_o$ = 25 µS und mit $\eta_p$ = 0,321 (aus γ = 0,615 √V und 2Φ_F = 0,921 V des Beispiel-PMOS) $g_{mB}$ = 0,353 mS. Die Kleinsignalspannungen sind Änderungen und dürfen positiv oder negativ sein; gezeichnet wird der Drain nur auf der Seite des niedrigeren Potentials.
:::

## Die Substratsteilheit im Sourcefolger

*Warum kostet die Substratsteilheit in manchen Schaltungen Verstärkung, obwohl sie positiv ist?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-sourcefolger-kleinsignal · Vorlage: schaltung-mit-ersatz
**Abbildung 7:** (a) NMOS-Sourcefolger: Drain an 2,5 V, Source über eine ideale Stromquelle von 0,25 mA an Masse, Bulk an Masse; bei 2 V am Gate liegt der Ausgang bei 0,783 V. (b) Sein Kleinsignal-Ersatzschaltbild: Der Drain liegt an der festen Versorgung und wird zur Masse, die Stromquelle wird eine Unterbrechung; $u_{GS}$ ist $u_\mathrm{ein} - u_\mathrm{aus}$ und $u_{BS}$ ist $-u_\mathrm{aus}$. Daneben umgezeichnet: Die Quelle $g_{mB} u_{BS}$ wirkt wie ein Leitwert von 0,241 mS von der Source nach Masse. (c) Ergebnis: Verstärkung 0,806 und Ausgangswiderstand 806 Ω statt 1 und 1 kΩ. Weil der Bulk festliegt, wirkt die Substratsteilheit im Folger wie ein zusätzlicher Leitwert am Ausgang.
:::

**Das Zusammenspiel:**

**Schritt 1**: Im __Sourcefolger__ ist das Gate der Eingang und die Source der Ausgang; die Source folgt dem Gate im Abstand von Schwelle plus Übersteuerung (Abbildung 7a). Der Bulk liegt an Masse, der Drain an der Versorgung.

**Schritt 2**: Steigt der Ausgang um $u_\mathrm{aus}$, sinkt $u_{BS}$ um denselben Betrag, denn der Bulk bleibt liegen: $u_{BS}$ ist $-u_\mathrm{aus}$.

**Schritt 3** (entscheidender Schritt): Die Quelle $g_{mB} u_{BS}$ liefert dann den Strom $-g_{mB} u_\mathrm{aus}$ in den Ausgangsknoten. Ein Strom, der proportional zur eigenen Knotenspannung abfließt, ist ein Leitwert: Für die Schaltung liegt $g_{mB}$ wie ein Widerstand von der Source nach Masse (Abbildung 7b).

**Schritt 4**: Dieser Leitwert belastet den Ausgang zusätzlich zu $g_m$ und $g_o$, und die Verstärkung sinkt unter 1. Mit $\eta$ = 0,241 bei 0,783 V Sperrspannung zwischen Source und Bulk ergibt sich 0,806, genau die Steigung, die die Großsignalrechnung des Folgers liefert ([PMOS-Transistor, Substrateffekt und Latch-Up](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/pmos-substrateffekt-latch-up-ausfuehrlich.html)).

**Die Akteure:**

- __$u_\mathrm{ein}$__, __$u_\mathrm{aus}$__: Kleinsignalspannung am Gate bzw. an der Source gegen Masse.
- __$G_L$__: Leitwert einer Last am Ausgang; null bei idealer Stromquelle ohne Last.
- __$A_V$__: Spannungsverstärkung des Folgers, $u_\mathrm{aus}/u_\mathrm{ein}$.

:::formel Formel
$$A_V = \frac{g_m}{g_m + g_{mB} + g_o + G_L}, \qquad r_\mathrm{aus} = \frac{1}{g_m + g_{mB} + g_o}$$
:::

**So liest man das:** Der Zähler ist der Strom, den das Gate steuert; im Nenner stehen alle Leitwerte, die den Ausgang belasten, darunter $g_{mB}$. Ohne Substrateffekt, ohne Last und mit vernachlässigtem $g_o$ wäre die Verstärkung 1. Mit $g_{mB} = \eta g_m$ bleibt $1/(1 + \eta)$; der Ausgangswiderstand $r_\mathrm{aus}$, den eine Last am Ausgang sieht, sinkt von $1/g_m$ auf $1/((1 + \eta) g_m)$.

**Kurz gesagt:** Im Folger mit Bulk an Masse wirkt die Substratsteilheit wie ein zusätzlicher Leitwert vom Ausgang nach Masse.

Idee der Herleitung: Man stellt die Knotengleichung am Ausgang auf und setzt $u_{BS}$ als $-u_\mathrm{aus}$ ein.

:::herleitung
**Ausgangspunkt:** das statische Kleinsignal-Ersatzschaltbild und die Knotenregel: Die Summe der Ströme, die in einen Knoten fließen, ist null.

**Annahmen:**
(i) Abschnürbereich, kleine Signale;
(ii) Drain an fester Versorgung, im Kleinsignalbild an Masse; Bulk an Masse;
(iii) die Stromquelle in der Source ist ideal, also im Kleinsignalbild eine Unterbrechung; eine Last $G_L$ liegt vom Ausgang nach Masse.

**Schritt 1**: Spannungen am Transistor, alle zur Source gezählt:

$$u_{GS} = u_\mathrm{ein} - u_\mathrm{aus}$$

$$u_{DS} = u_{BS} = -u_\mathrm{aus}$$

**Schritt 2**: Der Transistorstrom fließt vom Drain in die Source, also in den Ausgangsknoten hinein; durch die Last fließt $G_L u_\mathrm{aus}$ hinaus:

$$g_m\big(u_\mathrm{ein} - u_\mathrm{aus}\big) - g_{mB}\,u_\mathrm{aus} - g_o\,u_\mathrm{aus} - G_L\,u_\mathrm{aus} = 0$$

**Schritt 3** (entscheidender Schritt): Nach $u_\mathrm{aus}$ aufgelöst; $g_{mB}$ steht neben $g_o$ und $G_L$ wie ein Leitwert:

$$A_V = \frac{u_\mathrm{aus}}{u_\mathrm{ein}} = \frac{g_m}{g_m + g_{mB} + g_o + G_L}$$

**Schritt 4**: Ausgangswiderstand: Eingang festgehalten, $u_\mathrm{ein}$ null, ein Teststrom in den Ausgang; ohne $G_L$ fließt er durch die drei Leitwerte $g_m$, $g_{mB}$ und $g_o$:

$$r_\mathrm{aus} = \frac{1}{g_m + g_{mB} + g_o}$$

**Ergebnis:** die Formeln oben.

**Woher die Faktoren kommen:** $g_m$ steht doppelt, im Zähler als Steuerung durch den Eingang und im Nenner, weil $u_{GS}$ mit dem Ausgang sinkt; $g_{mB}$ steht nur im Nenner, weil der Bulk nicht mit dem Eingang verbunden ist.

**Proben:** Einheit S/S. Mit $g_m$ = 1 mS, η = 0,241, ohne $g_o$ und Last: 1/1,241 = 0,806 und 1/(1,241 mS) = 806 Ω; der Großsignal-Differenzenquotient zwischen 1,99 V und 2,01 V am Eingang ist ebenfalls 0,806. Mit 10 kΩ Last: 1/(1,241 + 0,1) = 0,746. Grenzfall η = 0: Verstärkung 1, $r_\mathrm{aus}$ = 1 kΩ.

**Grenzen:** Bei hohen Frequenzen kommen $C_{GS}$ zwischen Ein- und Ausgang und die Kapazitäten am Ausgang hinzu.
:::

::::beispiel Sourcefolger mit und ohne Substrateffekt
**Gegeben:** Beispiel-NMOS als Folger, Arbeitspunkt mit 0,25 mA aus einer idealen Stromquelle, λ = 0; Übersteuerung 0,5 V, also $g_m$ = 1 mS; Eingang 2 V, Ausgang 0,783 V, Bulk an Masse; γ = 0,629 √V, 2Φ_F = 0,923 V. (b) Derselbe Folger mit einem PMOS gleicher Kenngröße $K$ in eigener, mit der Source verbundener Wanne.

**Gesucht:** η, Verstärkung und Ausgangswiderstand in beiden Fällen.

**Rechnung:** (a) Sperrspannung zwischen Source und Bulk ist der Ausgang, 0,783 V:

$$\eta = \frac{0{,}629\ \sqrt{\mathrm V}}{2\,\sqrt{0{,}923\ \mathrm V + 0{,}783\ \mathrm V}} = 0{,}241$$

$$A_V = \frac{1}{1 + 0{,}241} = 0{,}806, \qquad r_\mathrm{aus} = \frac{1}{1{,}241\ \mathrm{mS}} = 806\ \Omega$$

(b) Mit der Wanne an der Source ist $u_{BS}$ null, also η = 0:

$$A_V = \frac{g_m}{g_m} = 1, \qquad r_\mathrm{aus} = \frac{1}{1\ \mathrm{mS}} = 1\ \mathrm{k\Omega}$$

**Ergebnis:** **(a) η = 0,241, Verstärkung 0,806, 806 Ω; (b) η = 0, Verstärkung 1, 1 kΩ.**

**Einordnung:** Die 0,806 sind genau die Steigung der Großsignalkennlinie des NMOS-Folgers; das Kleinsignalmodell gibt sie in einer Zeile wieder. Ein Fünftel des Signals geht verloren, weil der festliegende Bulk wie ein zweites Gate gegen den Ausgang arbeitet. Der kleinere Ausgangswiderstand ist dagegen ein Nebengewinn.
::::

## Das dynamische Kleinsignal-Ersatzschaltbild

*Was kommt für schnelle Änderungen hinzu?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-esb-dynamisch · Vorlage: ersatzschaltbild-paar
**Abbildung 8:** (a) Vollständiges dynamisches Kleinsignal-Ersatzschaltbild: das statische Ersatzschaltbild zwischen inneren Knoten, außen die Bahnwiderstände $R_G$, $R_D$, $R_S$ und $R_B$; dazu die Kapazitäten $C_{GS}$ = 49,5 fF, $C_{GD}$ = 3,45 fF, $C_{GB}$ ≈ 0, $C_{SB}$ = 53,1 fF (dazu rund 15 fF zwischen Kanal und Bulk) und $C_{DB}$ = 37,8 fF, Werte im Abschnürbereich bei 1 V/1 V. (b) Vereinfacht für Bulk an Source: $C_{GS}$ und $C_{GD}$ am Gate, $g_m u_{GS}$ und $g_o$ zwischen Drain und Source, $C_{DB}$ zwischen Drain und Source. Für schnelle Änderungen kommen zum statischen Modell die Kapazitäten hinzu; die meisten Bahnwiderstände sind vernachlässigbar, der Gatewiderstand nicht immer.
:::

Für schnelle Änderungen müssen die Ladungen im Transistor mitwandern, und das Ersatzschaltbild bekommt die Kapazitäten aus [Parasitäre Kapazitäten des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/parasitaere-kapazitaeten-ausfuehrlich.html) (Abbildung 8a): $C_{GS}$ und $C_{GD}$ zwischen Gate und Source bzw. Drain, im Abschnürbereich 49,5 fF und 3,45 fF; $C_{GB}$, oberhalb der Schwelle praktisch null, weil der Kanal den Bulk abschirmt; $C_{SB}$ und $C_{DB}$, die Sperrschichten von Source und Drain, 53,1 fF und 37,8 fF. Liegt der Bulk an der Source, fällt $C_{SB}$ heraus, und $C_{DB}$ liegt zwischen Drain und Source (Abbildung 8b).

Dazu kommen die __Bahnwiderstände__, die Widerstände der Zuleitungen in den Transistor: $R_S$ und $R_D$ durch die n⁺-Gebiete, $R_B$ durch das Substrat und $R_G$ längs des Gates. Ein Source-Gebiet von 2 µm Länge und 10 µm Weite besteht, in Stromrichtung gezählt, aus 0,2 Quadraten; bei einem __Schichtwiderstand__ von 100 Ω je Quadrat, dem Widerstand eines quadratischen Stücks der Schicht gleich welcher Größe, wie er ohne __Silizid__ üblich ist, eine Metall-Silizium-Verbindung, die man zur Senkung des Widerstands auf Gate und Diffusionsgebiete aufbringt, sind das 20 Ω; gegen $1/g_m$ = 909 Ω mindert das die wirksame Steilheit nur um 2,2 %. $R_S$, $R_D$ und $R_B$ lässt man deshalb meist weg. Der Gatewiderstand dagegen bildet mit der Eingangskapazität einen Tiefpass: Ein Gate aus Polysilizium ohne Silizid, 10 µm weit und 1 µm lang, also zehn Quadrate zu 200 Ω, hat 2 kΩ von Ende zu Ende; mit 53 fF ergibt das als obere Abschätzung eine Zeitkonstante von 106 ps, mit den 80,6 fF des Miller-Eingangs einer Verstärkerstufe mit der Verstärkung −8 ([Parasitäre Kapazitäten des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/parasitaere-kapazitaeten-ausfuehrlich.html)) 161 ps. Weil der Widerstand längs des Gates verteilt ist, wirkt bei einseitigem Anschluss nur etwa ein Drittel davon. Mit einer Silizidschicht sind es 80 Ω und 4 ps; bei breiten Transistoren teilt man das Gate in mehrere kurze Finger.

### Die Transitfrequenz

*Bis zu welcher Frequenz verstärkt ein Transistor überhaupt Strom?*

Das gebräuchlichste Maß für die Geschwindigkeit eines Transistors ist die Frequenz, bei der der Strom ins Gate so groß wird wie der gesteuerte Drainstrom. Bei kurzgeschlossenem Drain fließt ins Gate der Strom, der $C_{GS}$ und $C_{GD}$ umlädt; er wächst mit der Frequenz, während der Drainstrom $g_m u_{GS}$ gleich bleibt. Die Frequenz, bei der beide gleich sind, heißt __Transitfrequenz__:

$$f_T = \frac{g_m}{2\pi\,\big(C_{GS} + C_{GD}\big)}$$

**So liest man das:** Je mehr Steilheit je Kapazität, desto schneller der Transistor. Beim Beispiel sind es mit 1,1 mS und 52,9 fF 3,3 GHz; bei 1 GHz ist die Stromverstärkung noch 3,3. Für einen langen Kanal ohne Überlappung, mit der Steilheit $K U_\text{ü}$ und zwei Dritteln von $C_\mathrm{ox}$ als $C_{GS}$, wächst $f_T$ mit der Übersteuerung und fällt mit dem Quadrat der Kanallänge, beim Beispiel 3,46 GHz; kurze Kanäle sind deshalb schnell.

Idee der Herleitung: Man vergleicht im Kleinsignalbild mit kurzgeschlossenem Drain den Gatestrom mit dem Drainstrom.

:::herleitung
**Ausgangspunkt:** das vereinfachte dynamische Ersatzschaltbild und die Kondensatorgleichung in komplexer Form: Ein Kondensator $C$ nimmt bei der Kreisfrequenz ω den Strom $j\omega C$ mal Spannung auf.

**Annahmen:**
(i) Drain im Kleinsignalbild an Masse, Source an Masse;
(ii) der Strom durch $C_{GD}$ in den Drain ist klein gegen $g_m u_{GS}$;
(iii) quasistatisch, die Kapazitäten gelten bei der betrachteten Frequenz.

**Schritt 1**: Gatestrom: $C_{GS}$ und $C_{GD}$ liegen beide zwischen Gate und Masse:

$$\underline I_G = j\omega\,\big(C_{GS} + C_{GD}\big)\,\underline U_{GS}$$

**Schritt 2**: Drainstrom nach Annahme (ii):

$$\underline I_D \approx g_m\,\underline U_{GS}$$

**Schritt 3** (entscheidender Schritt): Die Stromverstärkung ist der Quotient; ihr Betrag wird 1 bei

$$\Big|\frac{\underline I_D}{\underline I_G}\Big| = \frac{g_m}{\omega\,\big(C_{GS} + C_{GD}\big)} = 1 \quad\Rightarrow\quad \omega_T = \frac{g_m}{C_{GS} + C_{GD}}$$

**Schritt 4**: Für den langen Kanal ohne Überlappung und ohne Kanallängenmodulation ist $K$ gleich $\mu_n C'_\mathrm{ox} W/L$, die Steilheit $K U_\text{ü}$ und $C_{GS}$ zwei Drittel von $C'_\mathrm{ox} W L$, $C_{GD}$ null:

$$f_T = \frac{K\,U_\text{ü}}{2\pi\cdot\tfrac23\,C'_\mathrm{ox}\,W L} = \frac{3\,\mu_n\,U_\text{ü}}{4\pi\,L^2}$$

**Ergebnis:**

$$f_T = \frac{g_m}{2\pi\,\big(C_{GS} + C_{GD}\big)}$$

**Woher die Faktoren kommen:** $2\pi$ wandelt die Kreisfrequenz in die Frequenz; im Langkanalausdruck ergibt der Kehrwert der zwei Drittel von $C_{GS}$ zusammen mit $1/(2\pi)$ den Faktor $3/(4\pi)$, und $W$ sowie $C'_\mathrm{ox}$ kürzen sich.

**Proben:** Einheit S/F = 1/s. Beim Beispiel 1,1 mS / (2π · 52,95 fF) = 3,31 GHz; mit 1 mS 3,0 GHz. Langkanal: 3 · 290 cm²/(V s) · 0,5 V / (4π · 10⁻⁸ cm²) = 3,46 GHz.

**Grenzen:** Annahme (iii) ist bei $f_T$ schon knapp erfüllt: Die Elektronen brauchen bei $U_{GS}$ = 1 V für den Weg durch den Kanal 92 ps; als Zeitkonstante gelesen entspricht das einer Grenzfrequenz von 1,7 GHz. Die Transitfrequenz ist deshalb ein Maß für den Vergleich von Transistoren, keine genaue Grenze; in Schaltungen arbeitet man weit darunter.
:::

## Das Modell im Schaltungssimulator

*Wie gibt man einem Schaltungssimulator den Beispieltransistor, und was macht er daraus?*

Schaltungssimulatoren wie SPICE beschreiben den Transistor durch eine __Modellkarte__, eine Liste von Parametern, aus denen sie Großsignalgleichungen und Kapazitäten berechnen. Das grundlegende Modell, Level 1, enthält genau die Gleichungen dieser Artikelreihe. Für eine Wechselspannungsanalyse bestimmt der Simulator zuerst den Arbeitspunkt und linearisiert dann an ihm, wie in diesem Artikel; er rechnet also mit demselben Kleinsignal-Ersatzschaltbild, nur mit allen Kapazitäten.

| Parameter | Bedeutung und Wert beim Beispiel-NMOS |
|---|---|
| VTO | Schwellenspannung ohne Substrateffekt, 0,5 V |
| KP | Prozessparameter $K' = \mu_n C'_\mathrm{ox}$, 200 µA/V²; gleichwertig UO = 290 cm²/(V s) |
| GAMMA, PHI | Substratsteuerfaktor 0,63 √V und Oberflächenpotential an der Schwelle $2\Phi_F$ = 0,92 V |
| LAMBDA | Kanallängenmodulation, 0,1 1/V |
| TOX | Oxiddicke, 5 nm; daraus die Gatekapazitäten |
| LD | Überlappung je Seite, 50 nm; wirksame Länge = gezeichnete Länge minus 2 LD |
| CGSO, CGDO | Überlappungskapazität pro Weite, 3,45·10⁻¹⁰ F/m, also 0,345 fF/µm |
| CJ, MJ | Sperrschichtkapazität des Bodens, 2,14·10⁻³ F/m², also 2,14 fF/µm², Exponent 0,5 |
| CJSW, MJSW | Sperrschichtkapazität des Randes, 4,28·10⁻¹⁰ F/m, also 0,428 fF/µm, Exponent 0,5 |
| PB | Diffusionsspannung der Übergänge, 1,03 V |

Zu jedem einzelnen Transistor gibt man die Abmessungen an: Weite W = 10 µm, gezeichnete Länge L = 1,1 µm, die mit LD = 50 nm die wirksame Länge 1 µm ergibt, sowie Fläche und Umfang von Drain und Source, AD = AS = 20 µm² und PD = PS = 24 µm. Daraus berechnet der Simulator $K$ = 2 mA/V², alle Kapazitäten und im Arbeitspunkt die Steilheiten dieses Artikels.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Steilheit $2I_D/U_\text{ü}$ | Steigung der Übertragungskennlinie im Arbeitspunkt, sie wächst mit der Übersteuerung |
| kleiner Ausgangsleitwert im Abschnürbereich | Steigung der flachen Ausgangskennlinie, die nur der kürzer werdende Kanal kippt |
| Substratsteilheit η $g_m$ | Steigung nach der Bulkspannung, der Bulk als zweites, schwächeres Gate |
| Fehler $u_{GS}/(2U_\text{ü})$ | die Tangente gilt nur nahe am Arbeitspunkt |
| ohmscher Bereich kein Verstärker | dort ist die Tangente nach $U_{DS}$ steiler als die nach $U_{GS}$ |
| Folger 0,806 | festliegender Bulk: die Bulk-Tangente wirkt als Leitwert am Ausgang |
| Kapazitäten und Transitfrequenz | für schnelle Änderungen kommt die Ladung im Transistor hinzu |
| SPICE-Karte | der Simulator linearisiert im Arbeitspunkt wie von Hand |

Um einen festen Arbeitspunkt ersetzt man jede Kennlinie des MOSFET durch ihre Tangente: Gate, Drain und Bulk steuern den Drainstrom dann linear, jeder mit einer eigenen Steilheit, die vom Arbeitspunkt abhängt, und für schnelle Änderungen kommen die Kapazitäten zwischen den Anschlüssen hinzu.

## Bedeutung und Ausblick

Mit dem Kleinsignal-Ersatzschaltbild lassen sich alle Transistorgrundschaltungen in wenigen Zeilen berechnen: Verstärkung, Eingangs- und Ausgangswiderstand der Source-, Drain- und Gate-Schaltung, die Kaskode und der Differenzverstärker. Datenblätter einzelner Feldeffekttransistoren nennen Steilheit und Ausgangsleitwert deshalb für einen angegebenen Arbeitspunkt, und Schaltungssimulatoren liefern sie im Ausdruck des Arbeitspunkts mit. Gemessen werden sie wie im Beispiel: Man ändert eine Spannung um wenige Millivolt und teilt die Stromänderung durch die Spannungsänderung.

Das Modell gilt für kleine Signale und Frequenzen weit unter der Transitfrequenz; für große Signale braucht man die Großsignalgleichungen, für sehr kurze Kanäle genauere Modelle mit gesättigter Elektronengeschwindigkeit. Der nächste Teil der Reihe behandelt den Bipolartransistor mit seinem Transportmodell und danach sein Kleinsignalmodell, das dieselbe Form mit anderen Steilheiten hat.

:::kern
- Die Kleinsignalgrößen sind die Steigungen der Kennlinien im Arbeitspunkt: $i_D = g_m u_{GS} + g_o u_{DS} + g_{mB} u_{BS}$.
- Das Modell gilt für Signale klein gegen die Übersteuerung: Die relative Abweichung ist $u_{GS}/(2U_\text{ü})$, 1 % bei 10 mV und 0,5 V.
- Im Abschnürbereich ist $g_m = 2I_D/U_\text{ü}$; im ohmschen Bereich ist die Steilheit viel kleiner und der Ausgangsleitwert groß.
- Im Abschnürbereich ist $g_o = I_D/(U_A + U_{DS})$ klein; die Eigenverstärkung $g_m/g_o$ beträgt beim Beispiel 44, genähert 40.
- Die Substratsteilheit $g_{mB} = \eta g_m$ ist positiv; Verstärkung kostet sie erst, wenn der Bulk festliegt und sich die Source bewegt, im Folger 0,806 statt 1.
- Statisches Ersatzschaltbild: Gate offen, $g_m u_{GS}$ und $g_{mB} u_{BS}$ vom Drain zur Source, $g_o$ parallel; für NMOS und PMOS gleich.
- Dynamisches Ersatzschaltbild: dazu $C_{GS}$, $C_{GD}$, $C_{SB}$, $C_{DB}$ und die Bahnwiderstände, von denen meist nur der Gatewiderstand zählt.
:::

:::quiz
F: Warum ist die Steilheit im Abschnürbereich proportional zur Übersteuerung?
A: Der Drainstrom wächst dort mit dem Quadrat der Übersteuerung, weil Ladung und Spannung längs des Kanals beide mit ihr wachsen; die Steigung einer Parabel wächst linear. Beim Beispiel sind es 1,1 mS bei 0,5 V und 2,2 mS bei 1 V Übersteuerung.
F: Warum ist der Ausgangsleitwert im Abschnürbereich so klein?
A: Der Teil der Drainspannung oberhalb der Übersteuerung fällt über der verarmten Zone vor dem Drain ab und erreicht den Kanal nicht; nur die Verkürzung des Kanals durch den wandernden Abschnürpunkt lässt den Strom leicht steigen. Beim Beispiel sind es 25 µS gegen 1,1 mS Steilheit.
F: Warum hat die Substratsteilheit dasselbe Vorzeichen wie die Steilheit?
A: Hebt man den Bulk an, sinkt die Schwelle um η mal die Änderung; das vergrößert die Übersteuerung wie eine höhere Gatespannung, und der Strom steigt. Deshalb ist $g_{mB}$ gleich η $g_m$ und positiv.
F: Warum verstärkt ein NMOS-Sourcefolger mit Bulk an Masse nur 0,806-fach?
A: Steigt der Ausgang, sinkt $u_{BS}$ um denselben Betrag, weil der Bulk festliegt. Die Quelle $g_{mB} u_{BS}$ wirkt dann wie ein Leitwert von der Source nach Masse, und die Verstärkung wird $1/(1 + \eta)$, mit η = 0,241 also 0,806.
F: Warum arbeiten Verstärkertransistoren im Abschnürbereich und nicht im ohmschen Bereich?
A: Im Abschnürbereich ist die Steilheit groß und der Ausgangsleitwert klein, ihr Verhältnis beim Beispiel 44. Im ohmschen Bereich ist es bei 0,1 V nur 0,25: Der Drain steuert den Strom stärker als das Gate.
F: Stimmt es, dass die Steilheit eine feste Eigenschaft des Transistors ist?
A: Nein. Sie hängt vom Arbeitspunkt ab: beim Beispiel 1,1 mS bei 0,275 mA, 2,2 mS bei 1,1 mA und 0,202 mS im ohmschen Bereich bei 0,1 V. Fest ist nur der Steilheitskoeffizient $K$.
F: Stimmt es, dass die Substratsteilheit negativ ist, weil der Substrateffekt Verstärkung kostet?
A: Nein. Sie ist positiv, 0,36 mS beim Beispiel. Verstärkung kostet sie erst in der Schaltung, wenn die Source steigt und der Bulk festliegt, sodass $u_{BS}$ negativ wird.
F: Stimmt es, dass das Kleinsignalmodell für jedes Signal am Gate gilt?
A: Nein. Die relative Abweichung von der Tangente ist $u_{GS}/(2U_\text{ü})$: beim Beispiel 1 % bei 10 mV, aber 10 % bei 100 mV.
F: Wie groß sind Steilheit und Ausgangsleitwert des Beispieltransistors bei $U_{GS}$ = 1,5 V und $U_{DS}$ = 1 V?
A: Übersteuerung 1 V, Strom 1,1 mA: $g_m$ = 2 mA/V² · 1 V · 1,1 = 2,2 mS, $g_o$ = 1,1 mA / 11 V = 100 µS.
F: Warum vernachlässigt man meist die Bahnwiderstände von Source und Drain, den Gatewiderstand aber nicht immer?
A: Der Source-Bahnwiderstand von rund 20 Ω ist klein gegen $1/g_m$ = 909 Ω und mindert die Steilheit nur um 2 %. Der Gatewiderstand bildet dagegen mit der Eingangskapazität einen Tiefpass, ohne Silizid 2 kΩ mit 53 fF, als obere Abschätzung also 106 ps.
:::
