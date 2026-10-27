---
title: Kleinsignalmodell des MOSFET
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / MOS-Feldeffekttransistoren
order: 33030500
summary: Wie man den MOSFET für kleine Änderungen um einen Arbeitspunkt durch ein lineares Ersatzschaltbild ersetzt und woher Steilheit, Ausgangsleitwert und Substratsteilheit kommen. Kompakte Fassung mit Linearisierung und Fehlergrenze, den drei Kleinsignalgrößen, der Substratsteilheit am Sourcefolger und dem statischen und dynamischen Ersatzschaltbild, durchgerechnet am Beispieltransistor.
tags: Steilheit, Ausgangsleitwert, Substratsteilheit, Kleinsignalersatzschaltbild, SPICE-Modell
stil: 3
fassung: kompakt
---

## Worum es geht

In einem Verstärker liegt der Transistor in einem festen Arbeitspunkt, und das Signal ändert die Spannungen nur um wenige Millivolt. Für solche kleinen Änderungen verhält sich der MOSFET linear: Man ersetzt ihn durch ein Ersatzschaltbild aus gesteuerten Quellen, Leitwerten und Kondensatoren und rechnet mit den Verfahren der Netzwerkanalyse, statt jedes Mal die nichtlinearen Kennliniengleichungen zu lösen. Alles hängt an einem Prinzip:

**Um einen festen Arbeitspunkt ersetzt man jede Kennlinie des MOSFET durch ihre Tangente: Gate, Drain und Bulk steuern den Drainstrom dann linear, jeder mit einer eigenen Steilheit, die vom Arbeitspunkt abhängt, und für schnelle Änderungen kommen die Kapazitäten zwischen den Anschlüssen hinzu.**

Vorausgesetzt werden die Linearisierung aus [Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html), das Großsignalmodell aus [Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien.html), der Substrateffekt aus [PMOS-Transistor, Substrateffekt und Latch-Up](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/pmos-substrateffekt-latch-up.html) und die Kapazitäten aus [Parasitäre Kapazitäten des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/parasitaere-kapazitaeten.html). Darauf bauen alle Transistorgrundschaltungen, ihr Frequenzgang und der Differenzverstärker auf.

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-tangenten-uebersicht · Vorlage: kennlinien-tangenten-esb
**Abbildung 1:** Drei kleine Diagramme des Beispiel-NMOS im Arbeitspunkt $U_{GS}$ = 1 V, $U_{DS}$ = 1 V, $U_{BS}$ = 0 mit 0,275 mA, jeweils mit Tangente: (a) Drainstrom über $U_{GS}$, Steigung 1,1 mS; (b) über $U_{DS}$, Steigung 25 µS; (c) über $U_{BS}$, Steigung 0,36 mS. Daneben das Kleinsignal-Ersatzschaltbild: Gate offen, zwischen Drain und Source die gesteuerten Quellen $g_m u_{GS}$ und $g_{mB} u_{BS}$ und der Leitwert $g_o$; jede Steigung führt mit einem Pfeil zu ihrem Bauelement. Jede Steigung im Arbeitspunkt wird ein Bauelement des Ersatzschaltbilds.
:::

## Von Grund auf: Arbeitspunkt, Tangente und gesteuerte Quelle

*Welche drei Vorstellungen braucht man, bevor man den Transistor linearisieren kann?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-grundlagen-tangente · Vorlage: kennlinie-tangente-zoom
**Abbildung 2:** (a) Übertragungskennlinie des Beispiel-NMOS bei $U_{DS}$ = 1 V, Drainstrom über $U_{GS}$ von 0,5 bis 1,5 V, mit dem Arbeitspunkt bei 1 V und 0,275 mA (rot) und der Tangente dort (orange), Steigung 1,1 mS. (b) Ausschnitt um den Arbeitspunkt, ±100 mV: Kurve und Tangente liegen fast aufeinander; bei +10 mV gibt die Kurve 11,11 µA mehr Strom, die Tangente 11,00 µA, bei +100 mV 121 gegen 110 µA. (c) Das Schaltzeichen der spannungsgesteuerten Stromquelle: eine Raute mit dem Strom $g_m u_{GS}$ und einer gestrichelten Zuordnung zur Spannung $u_{GS}$ an anderer Stelle. Nahe am Arbeitspunkt ist die Kennlinie ihre Tangente, und die Steigung wird zum Strom einer gesteuerten Quelle.
:::

### Der Arbeitspunkt: ein fester Betriebszustand

Feste Gleichspannungen am Transistor ergeben einen festen Gleichstrom: den __Arbeitspunkt__, beim Beispiel-NMOS $U_{GS}$ = 1 V, $U_{DS}$ = 1 V und 0,275 mA (Abbildung 2a), geschrieben mit Großbuchstaben. Ein Signal ändert die Spannungen nur um wenige Millivolt um diesen Punkt; er selbst bleibt fest ([Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html)).

### Die Tangente: die Steigung einer Kennlinie an einem Punkt

In einem kleinen Ausschnitt sieht jede glatte Kurve wie eine Gerade aus, die __Tangente__ im Arbeitspunkt (Abbildung 2b). Ihre Steigung ist eine Leitwertgröße, beim Beispiel 1,1 mS: 10 mV mehr am Gate geben nach der Tangente 11,00 µA, nach der Kennlinie 11,11 µA mehr Strom, 1 % Unterschied; bei 100 mV sind es 10 %, und in einem anderen Arbeitspunkt ist die Steigung eine andere. Die Tangente gilt nur nahe an ihrem Punkt.

### Die gesteuerte Stromquelle

Eine __gesteuerte Stromquelle__ ist ein Netzwerkelement, dessen Strom eine Spannung an anderer Stelle festlegt, gezeichnet als Raute mit gestrichelter Zuordnung zur Steuerspannung (Abbildung 2c). Die Tangentensteigung wird genau zu einer solchen Quelle: Der Strom zwischen Drain und Source ändert sich um 1,1 mS mal der Änderung der Gate-Source-Spannung, und das Gate führt keinen Strom. Der Rest des Artikels wendet das auf alle drei Spannungen an, die den Drainstrom steuern, bis das vollständige Ersatzschaltbild steht.


## Linearisierung im Arbeitspunkt

*Wie wird aus den nichtlinearen Kennlinien ein lineares Modell für kleine Änderungen?*

Der Beispieltransistor arbeitet mit $U_{GS}$ = 1 V und $U_{DS}$ = 1 V im Abschnürbereich, Source und Bulk an Masse, und führt 0,275 mA. Hebt man das Gate um 10 mV an, steigt der Strom um 11,11 µA, fast genau so viel, wie die Tangente mit 1,1 mS angibt, 11,00 µA. 100 mV mehr am Drain bringen 2,5 µA, 100 mV weniger am Bulk kosten 34 µA. Jede Spannung wirkt mit ihrer eigenen Steigung, und kleine Wirkungen addieren sich ([Nichtlineare Bauelemente, Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html)). Die __Kleinsignalgrößen__ sind diese Steigungen im Arbeitspunkt, je eine für jede Spannung, während die beiden anderen fest bleiben.

**Die Akteure:**

- __$u_{GS}$__, __$u_{DS}$__, __$u_{BS}$__, __$i_D$__: kleine Änderungen der drei Spannungen und des Drainstroms gegenüber dem Arbeitspunkt; Kleinbuchstaben kennzeichnen sie, der Arbeitspunkt trägt Großbuchstaben.
- __$g_m$__: __Steilheit__, Änderung des Drainstroms je Volt Gate-Source-Spannung; 1,1 mS im Arbeitspunkt.
- __$g_o$__: __Ausgangsleitwert__, Änderung je Volt Drain-Source-Spannung; 25 µS, auch $g_{DS}$ geschrieben; sein Kehrwert, der __Ausgangswiderstand__ $r_o$, ist 40 kΩ.
- __$g_{mB}$__: __Substratsteilheit__, Änderung je Volt Bulk-Source-Spannung; 0,36 mS.

:::formel Definition
$$g_m = \frac{\partial I_D}{\partial U_{GS}}, \qquad g_o = \frac{\partial I_D}{\partial U_{DS}}, \qquad g_{mB} = \frac{\partial I_D}{\partial U_{BS}}$$
:::

So definiert, wird jede Steigung im linearisierten Modell ein lineares Bauelement: die nach der eigenen Spannung des Drain-Source-Pfads ein Leitwert, die übrigen gesteuerte Quellen. Für kleine Änderungen gilt

:::formel Formel
$$i_D = g_m\,u_{GS} + g_o\,u_{DS} + g_{mB}\,u_{BS}$$
:::

**So liest man das:** Jede Spannungsänderung trägt mit ihrer Steigung bei, die Beiträge addieren sich, und der Gleichstrom des Arbeitspunkts kommt nicht mehr vor. Die drei Steigungen gelten nur für den Arbeitspunkt, in dem sie berechnet sind.

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
Die Kennliniengleichung ist nichtlinear, und jede Schaltung mit ihr führt auf ein Gleichungssystem, das sich nur schrittweise lösen lässt. Das Kleinsignalmodell ist linear: Signale überlagern sich, und Verstärkung, Eingangs- und Ausgangswiderstand folgen in einer Zeile. Den Arbeitspunkt rechnet man einmal nichtlinear, das Signal danach linear; für 10 mV am Gate des Beispieltransistors kostet das 1 % Genauigkeit.
:::

Wie klein „klein“ ist, legt die Übersteuerung $U_{GS} - U_{th}$ fest, um die die Gatespannung über der Schwelle liegt. Im Abschnürbereich wächst der Strom mit ihrem Quadrat; neben dem linearen Anteil entsteht deshalb ein quadratischer, und die relative Abweichung von der Tangente ist

$$\frac{\Delta I_D - g_m\,u_{GS}}{g_m\,u_{GS}} = \frac{u_{GS}}{2\,\big(U_{GS} - U_{th}\big)}$$

**So liest man das:** Bei 0,5 V Übersteuerung sind es 1 % für 10 mV und 10 % für 100 mV, mit dem Vorzeichen des Signals. Je kleiner die Übersteuerung, desto kleiner muss das Signal sein.

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

**Gesucht:** die exakte Stromänderung und die Abweichung von der Tangente für $u_{GS}$ = 10 mV und ±100 mV.

**Rechnung:** Exakte Änderung für 10 mV:

$$\Delta I_D = 1\ \mathrm{mA/V^2}\cdot\big(0{,}51^2 - 0{,}5^2\big)\ \mathrm{V^2}\cdot1{,}1 = 11{,}11\ \mathrm{\mu A}$$

Abweichung von $g_m u_{GS}$ = 11,00 µA:

$$\frac{u_{GS}}{2\,U_\text{ü}} = \frac{10\ \mathrm{mV}}{1\ \mathrm V} = 1\,\%$$

Für ±100 mV ergibt dieselbe Rechnung 121 µA bzw. −99 µA gegen ±110 µA, also +10 % und −10 %.

**Ergebnis:** **10 mV: 11,11 µA statt 11,00 µA, 1 % Abweichung; 100 mV: 10 %.**

**Einordnung:** Bei einigen Millivolt ist das Modell praktisch exakt, bei 100 mV merklich falsch. Die Grenze setzt die Übersteuerung: Bei 0,1 V Übersteuerung verträgt derselbe Transistor nur ein Fünftel des Signals.
::::

## Die Steilheit

*Wie stark steuert das Gate den Drainstrom im Arbeitspunkt, und wovon hängt das ab?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-steilheit · Vorlage: kennlinie-tangente-gestapelt
**Abbildung 3:** Zwei gestapelte Diagramme über $U_{GS}$ von 0 bis 2 V bei $U_{DS}$ = 1 V. Oben der Drainstrom: null bis zur Schwelle 0,5 V, 0,275 mA bei 1 V, 1,1 mA bei 1,5 V; die Tangente in 1 V mit 1,1 mS trifft die Spannungsachse bei 0,75 V; schattiert die Abweichung der Kurve von der Tangente bei ±10 mV (±1 %) und ±100 mV (±10 %). Unten die Steilheit: null unterhalb der Schwelle, dann linear auf 1,1 mS bei 1 V und 2,2 mS bei 1,5 V, gestrichelt die Näherung ohne den Faktor 1,1. Die Steilheit ist die Steigung der Übertragungskennlinie im Arbeitspunkt und wächst mit der Übersteuerung.
:::

Im Abschnürbereich wächst der Strom mit dem Quadrat der Übersteuerung, weil die Ladung an der Source und die Spannung längs des Kanals beide mit ihr wachsen ([Kennlinien des NMOS-Transistors](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kennlinien.html)). Die Steigung dieser Parabel wächst linear: 1,1 mS bei 0,5 V Übersteuerung, 2,2 mS bei 1 V (Abbildung 3). Im ohmschen Bereich legt $U_{DS}$ die Spannung längs des Kanals fest, nur die Ladung wächst mit dem Gate, und die Steilheit ist bei 0,1 V nur 0,202 mS.

**Die Akteure:**

- __$K$__: Steilheitskoeffizient $K' W/L$ mit $K' = \mu_n C'_\mathrm{ox}$; 2 mA/V².
- __$U_\text{ü}$__: Übersteuerung im Arbeitspunkt, $U_{GS} - U_{th}$; 0,5 V bei $U_{GS}$ = 1 V.
- __$\lambda$__: Kanallängenmodulationsfaktor; 0,1 1/V.

:::formel Formel
Abschnürbereich:

$$g_m = K\,U_\text{ü}\,\big(1 + \lambda\,U_{DS}\big) = \frac{2\,I_D}{U_\text{ü}}$$

Ohmscher Bereich:

$$g_m = K\,U_{DS}\,\big(1 + \lambda\,U_{DS}\big)$$
:::

**So liest man das:** $K U_\text{ü}$ zeigt, dass ein breiterer Transistor bei gleicher Übersteuerung mehr Steilheit hat; $2I_D/U_\text{ü}$, dass ein Milliampere umso mehr Steilheit bringt, je kleiner die Übersteuerung ist. Ohne Kanallängenmodulation ist die Steilheit auch die Wurzel aus $2 K I_D$, mit ihr nur näherungsweise. An der Grenze der Bereiche, bei 0,5 V, ergeben beide Formeln 1,05 mS. In Handrechnungen lässt man den Faktor $(1 + \lambda U_{DS})$ oft weg; die Netzwerkanalyse dieser Reihe rechnet so mit 1 mS statt 1,1 mS.

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

**Gesucht:** die Steilheit in allen drei Arbeitspunkten.

**Rechnung:** (a) Abschnürbereich:

$$g_m = 2\ \mathrm{mA/V^2}\cdot0{,}5\ \mathrm V\cdot1{,}1 = 1{,}1\ \mathrm{mS}, \qquad \frac{2\cdot0{,}275\ \mathrm{mA}}{0{,}5\ \mathrm V} = 1{,}1\ \mathrm{mS}$$

(b) Übersteuerung 1 V, Abschnürbereich, Strom 1,1 mA:

$$g_m = 2\ \mathrm{mA/V^2}\cdot1\ \mathrm V\cdot1{,}1 = 2{,}2\ \mathrm{mS}$$

(c) Ohmscher Bereich:

$$g_m = 2\ \mathrm{mA/V^2}\cdot0{,}1\ \mathrm V\cdot1{,}01 = 0{,}202\ \mathrm{mS}$$

**Ergebnis:** **(a) 1,1 mS; (b) 2,2 mS; (c) 0,202 mS.**

**Einordnung:** Viermal so viel Strom bringt in (b) nur die doppelte Steilheit, weil sich auch die Übersteuerung verdoppelt hat. Im ohmschen Bereich hat derselbe Transistor bei gleicher Gatespannung nur ein Fünftel der Steilheit.
::::

:::fehlvorstellung
„Die Steilheit ist eine feste Eigenschaft des Transistors, wie seine Weite.“ Das liegt nahe, weil Datenblätter einen Wert nennen; er gilt aber nur im dort angegebenen Arbeitspunkt. Beim Beispieltransistor sind es 1,1 mS bei 0,275 mA, 2,2 mS bei 1,1 mA und 0,202 mS im ohmschen Bereich. Fest ist nur der Steilheitskoeffizient $K$.
:::

## Der Ausgangsleitwert

*Wie stark wirkt die Drainspannung auf den Drainstrom zurück?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-ausgangsleitwert · Vorlage: kennlinie-tangente-gestapelt
**Abbildung 4:** Oben der Drainstrom über $U_{DS}$ bei $U_{GS}$ = 1 V, von −10 V bis 2,5 V mit Achsenbruch zwischen −10 V und 0: ohmscher Bereich bis 0,5 V, danach Abschnürbereich mit der Steigung 25 µS, 0,275 mA bei 1 V und 0,3 mA bei 2 V; die Tangente bei 1 V trifft die Spannungsachse bei −10 V. Unten Steilheit und Ausgangsleitwert über $U_{DS}$ von 0 bis 2,5 V: $g_o$ fällt von 1 mS bei 0 über 0,817 mS bei 0,1 V und 0,433 mS bei 0,3 V auf 25 µS ab 0,5 V, $g_m$ steigt von 0 über 0,202 mS und 0,618 mS auf 1,05 mS bei 0,5 V und 1,1 mS bei 1 V; beide Kurven ohne Sprung an der Abschnürgrenze. Im Abschnürbereich ist der Ausgangsleitwert klein und die Steilheit groß, im ohmschen Bereich umgekehrt.
:::

Im Abschnürbereich fällt der Teil der Drainspannung, der über die Übersteuerung hinausgeht, über der kurzen verarmten Zone vor dem Drain ab und erreicht den Kanal nicht. Nur die __Kanallängenmodulation__, die Verkürzung des Kanals, weil der Abschnürpunkt mit wachsender Drainspannung zur Source wandert, lässt den Strom leicht steigen: 25 µS beim Beispiel, ein Ausgangswiderstand von 40 kΩ (Abbildung 4). Im ohmschen Bereich ist der Kanal ein Widerstand, und die Drainspannung treibt den Strom unmittelbar: bei 0,1 V 0,817 mS.

**Die Akteure:**

- __$U_A$__: Early-Spannung, der Kehrwert von λ; 10 V. Die Tangenten im Abschnürbereich treffen die Spannungsachse bei $-U_A$.

:::formel Formel
Abschnürbereich:

$$g_o = \frac{\lambda K}{2}\,U_\text{ü}^2 = \frac{I_D}{U_A + U_{DS}}$$

Ohmscher Bereich:

$$\begin{aligned} g_o &= K\Big[\Big(U_\text{ü} - \frac{U_{DS}}{2}\Big)\big(1 + 2\lambda U_{DS}\big) - \frac{U_{DS}}{2}\,\big(1 + \lambda U_{DS}\big)\Big] \\ &\approx K\,\big(U_\text{ü} - U_{DS}\big) \end{aligned}$$
:::

**So liest man das:** Im Abschnürbereich ist $g_o$ der Strom geteilt durch den Abstand des Arbeitspunkts vom Schnittpunkt bei $-U_A$, 0,275 mA durch 11 V; die verbreitete Näherung $\lambda I_D$ liegt bei 1 V um 10 % zu hoch. Im ohmschen Bereich ist $g_o$ etwa der Leitwert des Kanals mit der Übersteuerung am Drain-Ende; er fällt bis zur Abschnürgrenze, und die exakten Ausdrücke beider Bereiche liefern dort ohne Sprung 25 µS.

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

Das Verhältnis $g_m/g_o$ heißt __Eigenverstärkung__: Mit einer idealen Stromquelle am Drain verstärkt eine Source-Schaltung um diesen Faktor, und mehr erreicht ein einzelner Transistor nicht. Beim Beispiel ist es 44, genähert 40; im ohmschen Bereich bei 0,1 V nur 0,25. Deshalb arbeiten Verstärkertransistoren im Abschnürbereich, Schalter im ohmschen Bereich.

::::beispiel Ausgangsleitwert und Eigenverstärkung des Beispieltransistors
**Gegeben:** Beispiel-NMOS mit $K$ = 2 mA/V², $U_{th}$ = 0,5 V, λ = 0,1 1/V, also $U_A$ = 10 V; (a) $U_{GS}$ = 1 V, $U_{DS}$ = 1 V mit 0,275 mA und $g_m$ = 1,1 mS; (b) $U_{GS}$ = 1 V, $U_{DS}$ = 0,1 V mit $g_m$ = 0,202 mS.

**Gesucht:** Ausgangsleitwert, Ausgangswiderstand und Eigenverstärkung.

**Rechnung:** (a) Abschnürbereich:

$$g_o = \frac{0{,}275\ \mathrm{mA}}{10\ \mathrm V + 1\ \mathrm V} = 25\ \mathrm{\mu S}, \qquad r_o = 40\ \mathrm{k\Omega}, \qquad \frac{g_m}{g_o} = \frac{1{,}1\ \mathrm{mS}}{25\ \mathrm{\mu S}} = 44$$

(b) Ohmscher Bereich:

$$g_o = 2\ \mathrm{mA/V^2}\cdot\big[0{,}45\cdot1{,}02 - 0{,}05\cdot1{,}01\big]\ \mathrm V = 0{,}817\ \mathrm{mS}, \qquad \frac{g_m}{g_o} = \frac{0{,}202}{0{,}817} = 0{,}25$$

**Ergebnis:** **(a) 25 µS, 40 kΩ, Eigenverstärkung 44; (b) 0,817 mS, Eigenverstärkung 0,25.**

**Einordnung:** Im Abschnürbereich steuert das Gate den Strom 44-mal stärker als der Drain; im ohmschen Bereich steuert der Drain viermal stärker als das Gate, der Transistor ist dort ein spannungsgesteuerter Widerstand.
::::

## Die Substratsteilheit

*Wie wirkt der Bulk auf den Drainstrom, und in welche Richtung?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-substratsteilheit · Vorlage: kennlinie-tangente-gestapelt
**Abbildung 5:** Oben der Drainstrom über $U_{BS}$ von −2,5 V bis +0,3 V bei $U_{GS}$ = 1 V und $U_{DS}$ = 1 V: praktisch null bei −2,5 V, 0,059 mA bei −1 V, 0,138 mA bei −0,5 V, 0,275 mA bei 0 und 0,406 mA bei +0,3 V; die Tangente bei 0 hat die Steigung 0,36 mS; der Bereich über 0 ist grau hinterlegt, dort beginnt die Diode zwischen Bulk und Source zu leiten. Unten η über $U_{SB}$ von 0 bis 2 V: 0,327, 0,264, 0,227, 0,202 und 0,184. Der Bulk steuert den Strom wie ein zweites, schwächeres Gate; sein Anteil η sinkt mit der Sperrspannung.
:::

**Die Akteure:**

- __$\gamma$__, __$2\Phi_F$__: Substratsteuerfaktor und Oberflächenpotential an der Schwelle aus [PMOS-Transistor, Substrateffekt und Latch-Up](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/pmos-substrateffekt-latch-up.html); 0,629 √V und 0,923 V.
- __$U_{SB}$__: Sperrspannung zwischen Source und Bulk, das Negative von $U_{BS}$; 0 im Arbeitspunkt.
- __$\eta$__: Verhältnis von Substrat- zu Gatesteilheit, zugleich das Kapazitätsverhältnis $C'_\mathrm{dep}/C'_\mathrm{ox}$; 0,327.

**Das Zusammenspiel:**

**Schritt 1**: Der Bulk wirkt über die Verarmungszone unter dem Kanal wie ein zweites Gate: Liegt er tiefer als die Source, wird die Zone breiter, und die Schwelle steigt (Abbildung 5, oben).

**Schritt 2**: Hebt man den Bulk um $u_{BS}$ an, sinkt die Schwelle um $\eta\,u_{BS}$, beim Beispiel um 3,3 mV je 10 mV.

**Schritt 3** (entscheidender Schritt): Eine tiefere Schwelle wirkt wie eine höhere Gatespannung, denn beide gehen nur über die Übersteuerung ein. Die Substratsteilheit ist deshalb η-mal die Steilheit, 0,36 mS, in beiden Bereichen und mit demselben Vorzeichen.

**Schritt 4**: Mit wachsender Sperrspannung wird die Zone tiefer, und η sinkt, auf 0,227 bei 1 V (Abbildung 5, unten).

:::formel Formel
$$g_{mB} = \eta\,g_m, \qquad \eta = \frac{\gamma}{2\,\sqrt{2\Phi_F + U_{SB}}}$$
:::

**So liest man das:** Je höher die Dotierung unter dem Gate und je dicker das Oxid, desto größer η; üblich sind 0,1 bis 0,4. Liegt der Bulk an der Source, ist $u_{BS}$ null, und die Substratsteilheit spielt keine Rolle.

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
„Die Substratsteilheit ist negativ, denn der Substrateffekt verringert doch die Verstärkung.“ Das liegt nahe, weil der Substrateffekt in vielen Schaltungen Verstärkung kostet. Die Substratsteilheit selbst ist aber positiv, 0,36 mS: Steigt der Bulk, sinkt die Schwelle, und der Strom steigt. Verstärkung kostet sie erst, wenn in einer Schaltung die Source steigt und der Bulk fest an Masse liegt, sodass $u_{BS}$ negativ wird (Abschnitt *Die Substratsteilheit im Sourcefolger*).
:::

## Das statische Kleinsignal-Ersatzschaltbild

*Wie sieht der linearisierte Transistor als Schaltung aus?*

Die Gleichung für $i_D$ ergibt das __Kleinsignal-Ersatzschaltbild__ in Abbildung 1. Das Gate ist ein offener Anschluss, denn durch das Oxid fließt kein Gleichstrom, und bei langsamen Änderungen ist auch der Umladestrom der Gatekapazität vernachlässigbar. Zwischen Drain und Source liegen zwei __spannungsgesteuerte Stromquellen__, Quellen, deren Strom von einer Spannung an anderer Stelle abhängt: $g_m u_{GS}$ und $g_{mB} u_{BS}$, beide vom Drain zur Source gerichtet wie der Drainstrom. Parallel liegt der Leitwert $g_o$. In der Schaltung werden Gleichspannungsquellen zu Kurzschlüssen und Gleichstromquellen zu Unterbrechungen, weil sich ihre Spannung bzw. ihr Strom nicht ändert; liegt der Bulk an der Source, entfällt die Quelle $g_{mB} u_{BS}$.

:::frage
„Gilt das Ersatzschaltbild auch für den PMOS, bei dem doch alles negativ ist?“
Ja, mit denselben Richtungen und positiven Parametern. Zählt man den Drainstrom wie beim NMOS in den Drain hinein, wird der negative Strom größer, wenn das Gate steigt; die Ableitung nach $U_{GS}$ ist also positiv. Beim Beispiel-PMOS bei −1 V/−1 V sind es 1,1 mS, 25 µS und mit $\eta_p$ = 0,321 (aus γ = 0,615 √V und 2Φ_F = 0,921 V des Beispiel-PMOS) 0,353 mS. Gezeichnet wird der Drain nur auf der Seite des niedrigeren Potentials.
:::

## Die Substratsteilheit im Sourcefolger

*Warum kostet die Substratsteilheit in manchen Schaltungen Verstärkung, obwohl sie positiv ist?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-sourcefolger-kleinsignal · Vorlage: schaltung-mit-ersatz
**Abbildung 6:** (a) NMOS-Sourcefolger: Drain an 2,5 V, Source über eine ideale Stromquelle von 0,25 mA an Masse, Bulk an Masse; bei 2 V am Gate liegt der Ausgang bei 0,783 V. (b) Sein Kleinsignal-Ersatzschaltbild: Der Drain liegt an der festen Versorgung und wird zur Masse, die Stromquelle wird eine Unterbrechung; $u_{GS}$ ist $u_\mathrm{ein} - u_\mathrm{aus}$ und $u_{BS}$ ist $-u_\mathrm{aus}$. Daneben umgezeichnet: Die Quelle $g_{mB} u_{BS}$ wirkt wie ein Leitwert von 0,241 mS von der Source nach Masse. (c) Ergebnis: Verstärkung 0,806 und Ausgangswiderstand 806 Ω statt 1 und 1 kΩ. Weil der Bulk festliegt, wirkt die Substratsteilheit im Folger wie ein zusätzlicher Leitwert am Ausgang.
:::

**Das Zusammenspiel:**

**Schritt 1**: Im __Sourcefolger__ ist das Gate der Eingang und die Source der Ausgang (Abbildung 6a); der Bulk liegt an Masse, der Drain an der Versorgung.

**Schritt 2**: Steigt der Ausgang um $u_\mathrm{aus}$, sinkt $u_{BS}$ um denselben Betrag, weil der Bulk liegen bleibt.

**Schritt 3** (entscheidender Schritt): Die Quelle $g_{mB} u_{BS}$ liefert dann $-g_{mB} u_\mathrm{aus}$ in den Ausgang: ein Strom, der mit der eigenen Knotenspannung abfließt, also ein Leitwert von der Source nach Masse (Abbildung 6b).

**Schritt 4**: Er belastet den Ausgang, und die Verstärkung sinkt unter 1, beim Beispiel mit η = 0,241 auf 0,806, genau die Steigung der Großsignalrechnung des Folgers.

**Die Akteure:**

- __$u_\mathrm{ein}$__, __$u_\mathrm{aus}$__: Kleinsignalspannung am Gate bzw. an der Source gegen Masse.
- __$G_L$__: Leitwert einer Last am Ausgang; null ohne Last.
- __$A_V$__: Spannungsverstärkung $u_\mathrm{aus}/u_\mathrm{ein}$.

:::formel Formel
$$A_V = \frac{g_m}{g_m + g_{mB} + g_o + G_L}, \qquad r_\mathrm{aus} = \frac{1}{g_m + g_{mB} + g_o}$$
:::

**So liest man das:** Im Nenner stehen alle Leitwerte, die den Ausgang belasten, darunter $g_{mB}$. Ohne Last und mit vernachlässigtem $g_o$ bleibt $1/(1 + \eta)$; der Ausgangswiderstand sinkt dabei von $1/g_m$ auf $1/((1 + \eta) g_m)$.

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

$$A_V = 1, \qquad r_\mathrm{aus} = \frac{1}{1\ \mathrm{mS}} = 1\ \mathrm{k\Omega}$$

**Ergebnis:** **(a) η = 0,241, Verstärkung 0,806, 806 Ω; (b) η = 0, Verstärkung 1, 1 kΩ.**

**Einordnung:** Die 0,806 sind genau die Steigung der Großsignalkennlinie des NMOS-Folgers. Ein Fünftel des Signals geht verloren, weil der festliegende Bulk wie ein zweites Gate gegen den Ausgang arbeitet; beim PMOS in eigener Wanne lässt sich das vermeiden.
::::

## Das dynamische Kleinsignal-Ersatzschaltbild

*Was kommt für schnelle Änderungen hinzu?*

:::grafik
Szene: st1/mos-feldeffekttransistoren/05-esb-dynamisch · Vorlage: ersatzschaltbild-paar
**Abbildung 7:** (a) Vollständiges dynamisches Kleinsignal-Ersatzschaltbild: das statische Ersatzschaltbild zwischen inneren Knoten, außen die Bahnwiderstände $R_G$, $R_D$, $R_S$ und $R_B$; dazu die Kapazitäten $C_{GS}$ = 49,5 fF, $C_{GD}$ = 3,45 fF, $C_{GB}$ ≈ 0, $C_{SB}$ = 53,1 fF (dazu rund 15 fF zwischen Kanal und Bulk) und $C_{DB}$ = 37,8 fF, Werte im Abschnürbereich bei 1 V/1 V. (b) Vereinfacht für Bulk an Source: $C_{GS}$ und $C_{GD}$ am Gate, $g_m u_{GS}$ und $g_o$ zwischen Drain und Source, $C_{DB}$ zwischen Drain und Source. Für schnelle Änderungen kommen zum statischen Modell die Kapazitäten hinzu; die meisten Bahnwiderstände sind vernachlässigbar, der Gatewiderstand nicht immer.
:::

Für schnelle Änderungen bekommt das Ersatzschaltbild die Kapazitäten aus [Parasitäre Kapazitäten des MOSFET](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/parasitaere-kapazitaeten.html) (Abbildung 7): $C_{GS}$ und $C_{GD}$, im Abschnürbereich 49,5 fF und 3,45 fF; $C_{GB}$, oberhalb der Schwelle praktisch null; $C_{SB}$ und $C_{DB}$, 53,1 fF und 37,8 fF. Dazu kommen die __Bahnwiderstände__ der Zuleitungen in den Transistor. Der Widerstand des Source-Gebiets, rund 20 Ω, ist klein gegen $1/g_m$ = 909 Ω und kostet 2 % Steilheit; ihn und die Widerstände von Drain und Bulk lässt man weg. Der Gatewiderstand bildet dagegen mit der Eingangskapazität einen Tiefpass: 2 kΩ eines Gates aus Polysilizium ohne Silizid mit 53 fF ergeben 106 ps.

Schaltungssimulatoren wie SPICE rechnen mit genau diesem Modell: Aus einer Modellkarte mit Schwelle, Prozessparameter, Substratsteuerfaktor, Kanallängenmodulation, Oxiddicke und den Kapazitätsbelägen bestimmen sie den Arbeitspunkt und linearisieren an ihm.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Steilheit $2I_D/U_\text{ü}$ | Steigung der Übertragungskennlinie, sie wächst mit der Übersteuerung |
| kleiner Ausgangsleitwert im Abschnürbereich | Steigung der flachen Ausgangskennlinie |
| Substratsteilheit η $g_m$ und Folger 0,806 | Steigung nach der Bulkspannung; festliegender Bulk wirkt als Leitwert |
| Fehler $u_{GS}/(2U_\text{ü})$ | die Tangente gilt nur nahe am Arbeitspunkt |
| Kapazitäten im dynamischen Modell | für schnelle Änderungen kommt die Ladung im Transistor hinzu |

Um einen festen Arbeitspunkt ersetzt man jede Kennlinie des MOSFET durch ihre Tangente: Gate, Drain und Bulk steuern den Drainstrom dann linear, jeder mit einer eigenen Steilheit, die vom Arbeitspunkt abhängt, und für schnelle Änderungen kommen die Kapazitäten zwischen den Anschlüssen hinzu.

## Bedeutung und Ausblick

Mit dem Kleinsignal-Ersatzschaltbild berechnet man alle Transistorgrundschaltungen in wenigen Zeilen, von der Source-Schaltung bis zum Differenzverstärker. Es gilt für kleine Signale und Frequenzen weit unter der Grenze, bei der die Kanalladung nicht mehr folgt. Der nächste Teil der Reihe behandelt den Bipolartransistor und sein Kleinsignalmodell.

**In der ausführlichen Fassung:** die zweite Harmonische kleiner Signale, warum man den Faktor der Kanallängenmodulation oft weglässt, die Steilheit je Strom bis unter die Schwelle, das Ersatzschaltbild von NMOS und PMOS als eigene Abbildung, die Bahnwiderstände mit Zahlen, die Transitfrequenz mit Herleitung und die SPICE-Modellkarte des Beispieltransistors mit allen Parametern ([Kleinsignalmodell des MOSFET, ausführlich](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/mos-feldeffekttransistoren/kleinsignalmodell-ausfuehrlich.html)).

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
A: Der Drainstrom wächst mit dem Quadrat der Übersteuerung, weil Ladung und Spannung längs des Kanals beide mit ihr wachsen; die Steigung einer Parabel wächst linear. Beim Beispiel 1,1 mS bei 0,5 V und 2,2 mS bei 1 V Übersteuerung.
F: Warum verstärkt ein NMOS-Sourcefolger mit Bulk an Masse nur 0,806-fach?
A: Steigt der Ausgang, sinkt $u_{BS}$ um denselben Betrag, weil der Bulk festliegt. Die Quelle $g_{mB} u_{BS}$ wirkt dann wie ein Leitwert vom Ausgang nach Masse, und die Verstärkung wird $1/(1 + \eta)$, mit η = 0,241 also 0,806.
F: Stimmt es, dass die Steilheit eine feste Eigenschaft des Transistors ist?
A: Nein. Sie hängt vom Arbeitspunkt ab: 1,1 mS bei 0,275 mA, 2,2 mS bei 1,1 mA und 0,202 mS im ohmschen Bereich bei 0,1 V. Fest ist nur $K$.
F: Stimmt es, dass die Substratsteilheit negativ ist, weil der Substrateffekt Verstärkung kostet?
A: Nein. Sie ist positiv, 0,36 mS beim Beispiel; Verstärkung kostet sie erst, wenn die Source steigt und der Bulk festliegt, sodass $u_{BS}$ negativ wird.
F: Warum arbeiten Verstärkertransistoren im Abschnürbereich?
A: Dort ist die Steilheit groß und der Ausgangsleitwert klein, ihr Verhältnis beim Beispiel 44; im ohmschen Bereich bei 0,1 V nur 0,25, dort steuert der Drain den Strom stärker als das Gate.
F: Wie groß sind Steilheit und Ausgangsleitwert des Beispieltransistors bei $U_{GS}$ = 1,5 V und $U_{DS}$ = 1 V?
A: Übersteuerung 1 V, Strom 1,1 mA: $g_m$ = 2 mA/V² · 1 V · 1,1 = 2,2 mS, $g_o$ = 1,1 mA / 11 V = 100 µS.
:::
