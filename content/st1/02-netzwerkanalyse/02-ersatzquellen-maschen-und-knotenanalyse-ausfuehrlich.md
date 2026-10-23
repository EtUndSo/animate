---
title: Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse
order: 33020200
summary: Wie man lineare Schaltungen systematisch berechnet, auch Kleinsignal-Ersatzschaltbilder mit gesteuerten Quellen und Wechselstromnetze mit Spulen und Kondensatoren: Ersatzquellen nach Thévenin und Norton, Maschenstrom- und Knotenpotentialanalyse. Ausführliche Fassung mit Herleitung der Linearität, der Impedanzen, der Zahl unabhängiger Gleichungen, des Satzes von der Ersatzquelle mit gesteuerten Quellen und der Matrixgleichungen beider Verfahren, durchgerechnet an einem RC-Tiefpass und einer Verstärkerstufe.
tags: Thévenin, Norton, Maschenstromanalyse, Knotenpotentialanalyse, gesteuerte Quelle
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Nach der Linearisierung im Arbeitspunkt ist eine Verstärkerschaltung für kleine Signale ein Netz aus Widerständen, Kondensatoren, Spulen und gesteuerten Quellen. Schon die Stufe mit einem einzigen Transistor in Abbildung 1 hat zwölf unbekannte Zweigströme und Zweigspannungen. Gebraucht werden Verfahren, die ein solches Netz mit möglichst wenigen Gleichungen lösen, und eine Beschreibung, die einen ganzen Schaltungsblock für den nächsten Block auf zwei Zahlen verdichtet. Beides folgt aus einem Prinzip:

**In einer linearen Schaltung hängt jede Spannung und jeder Strom linear von den unabhängigen Quellen ab; deshalb verhält sich die Schaltung an zwei Klemmen wie eine einzige Quelle mit Innenimpedanz, und ihr Gleichungssystem wird klein, wenn man als Unbekannte Knotenpotentiale oder Maschenströme wählt, weil diese eine der beiden Kirchhoffschen Regeln schon von selbst erfüllen.**

Vorausgesetzt werden die [Kirchhoffschen Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html), das Rechnen mit [Zeigern](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html) und das Kleinsignal-Ersatzschaltbild aus [Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html). Für Gleichstromnetze behandeln [Ersatzquellen – Thévenin und Norton](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html), [Das Maschenstromverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/maschenstromverfahren/maschenstromverfahren.html) und [Das Knotenpotentialverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/knotenpotentialverfahren/knotenpotentialverfahren.html) dieselben Verfahren; hier kommen Wechselgrößen und gesteuerte Quellen hinzu, die in jeder Transistorschaltung stecken. Darauf bauen die modifizierte Knotenanalyse der Schaltungssimulatoren und jede Kleinsignalrechnung an Transistorstufen auf.

:::grafik
Szene: st1/netzwerkanalyse/02-verstaerker-kleinsignal · Vorlage: schaltbild-vergleich
**Abbildung 1:** (a) Source-Schaltung mit einem n-Kanal-MOSFET im Arbeitspunkt 0,25 mA: Drainwiderstand $R_D$ = 10 kΩ an 5 V, Source-Widerstand $R_S$ = 1 kΩ, am Gate eine Signalquelle mit 10 mV Amplitude und 10 kΩ Innenwiderstand auf 1,25 V Vorspannung, am Ausgang über einen Koppelkondensator eine Last von 10 kΩ. (b) Ihr Kleinsignal-Ersatzschaltbild mit den Knoten G, D und S: Eine gesteuerte Stromquelle $g_m u_{GS}$ mit 1 mS und ein Ausgangsleitwert von 25 µS ersetzen den Transistor; Versorgung und Vorspannung werden zu Kurzschlüssen, ebenso der Koppelkondensator, dessen Impedanz bei der Signalfrequenz vernachlässigt wird. Die Zeiger der Knotenpotentiale sind 10 mV, −23,26 mV und 4,65 mV; der Drain schwingt mit 23,26 mV Amplitude gegenphasig zum Signal. (c) Vom Ausgang aus gesehen ist dieselbe Schaltung eine Quelle mit der Leerlaufspannung −43,96 mV und dem Innenwiderstand 8,90 kΩ. Eine lineare Schaltung ist durch ihre Knotenpotentiale bestimmt, und vom Ausgang aus gesehen genügen zwei Zahlen.
:::

## Lineare Schaltungen

*Was macht eine Schaltung linear, und warum gehören Spulen, Kondensatoren und gesteuerte Quellen dazu?*

Verdoppelt man in der Verstärkerstufe die Signalamplitude von 10 mV auf 20 mV, verdoppelt sich die Ausgangsspannung, als Zeiger von −23,26 mV auf −46,51 mV. Liefert die Signalquelle die Summe zweier Signale, 10 mV und −5 mV, ist die Ausgangsspannung die Summe der Ausgangsspannungen, die jedes Signal allein hervorruft: −23,26 mV und +11,63 mV ergeben −11,63 mV, genau den Wert für 5 mV. Diese beiden Eigenschaften machen eine Schaltung linear.

**Die Akteure:**

- __$x_1$__, __$x_2$__: zwei Anregungen, etwa Werte unabhängiger Quellen; in V oder A.
- __$y$__: eine beliebige Antwort der Schaltung, ein Strom oder eine Spannung, als Funktion der Anregung.
- __$\alpha_1$__, __$\alpha_2$__: beliebige Zahlen, bei Wechselgrößen auch komplexe.

:::formel Definition
$$y(\alpha_1 x_1 + \alpha_2 x_2) = \alpha_1\,y(x_1) + \alpha_2\,y(x_2)$$
:::

Man definiert Linearität so, weil genau diese Eigenschaft das Zerlegen erlaubt: Jede Anregung darf einzeln betrachtet werden, und die Antworten addieren sich. [Das Superpositionsverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/superpositionsverfahren.html) macht daraus einen Rechenweg; hier trägt dieselbe Eigenschaft den Satz von der Ersatzquelle.

**Kurz gesagt:** Die Antwort einer linearen Schaltung auf die Summe zweier Anregungen ist die Summe ihrer Antworten, und die Antwort auf das Vielfache einer Anregung ist das Vielfache der Antwort.

:::grafik
Szene: st1/netzwerkanalyse/02-quellensymbole · Vorlage: symboltabelle
**Abbildung 2:** Schaltzeichen der Quellen. Oben die unabhängigen Quellen: Gleichspannungs- und Gleichstromquelle, die den Arbeitspunkt einstellen und im Kleinsignalbild zu Kurzschluss bzw. Unterbrechung werden, und Kleinsignalquellen mit Sinuszeichen, die die Schaltung anregen. Unten die vier gesteuerten Quellen als Rauten, jede mit ihrer Steuergröße an anderer Stelle der Schaltung: spannungsgesteuerte Strom- und Spannungsquelle, stromgesteuerte Strom- und Spannungsquelle. Gleichquellen legen den Arbeitspunkt fest, Kleinsignalquellen regen an, gesteuerte Quellen beschreiben die Verstärkung.
:::

Linear ist eine Schaltung, wenn jede Zweiggleichung Ströme und Spannungen nur über feste Faktoren und Ableitungen nach der Zeit verknüpft; die Herleitung unten zeigt, warum dann die Definition gilt. Beim Widerstand ist die Spannung dem Strom proportional. Bei Spule und Kondensator verknüpft die Zweiggleichung die Spannung mit der Änderungsgeschwindigkeit des Stroms bzw. den Strom mit der Änderungsgeschwindigkeit der Spannung; weil die Ableitung einer Summe die Summe der Ableitungen ist, sind auch sie linear.

Abbildung 2 zeigt die beiden Arten von Quellen. Eine __unabhängige Quelle__ liefert eine vorgegebene Spannung oder einen vorgegebenen Strom, gleich was die Schaltung tut; ihre Werte sind die Anregung, die $x$ der Definition. Gleichquellen stellen den Arbeitspunkt ein und werden im Kleinsignalbild zu Kurzschluss bzw. Unterbrechung, weil sich ihr Wert nicht ändert; der Innenwiderstand einer realen Quelle bleibt dabei stehen ([Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html)). Eine __gesteuerte Quelle__ liefert eine Spannung oder einen Strom, die einer Spannung oder einem Strom an einer anderen Stelle der Schaltung proportional sind. Sie ist ein lineares Bauelement, aber keine Anregung: Ihr Wert folgt aus der Schaltung selbst. Es gibt vier Arten:

- __spannungsgesteuerte Stromquelle__, Faktor __Steilheit__ $g_m$ in S: der Drainstrom eines MOSFET, gesteuert von der Gate-Source-Spannung;
- __spannungsgesteuerte Spannungsquelle__, Faktor Spannungsverstärkung $v$ ohne Einheit: der Ausgang eines Operationsverstärkers;
- __stromgesteuerte Stromquelle__, Faktor Stromverstärkung $\beta$ ohne Einheit: der Kollektorstrom eines Bipolartransistors, gesteuert vom Basisstrom;
- __stromgesteuerte Spannungsquelle__, Faktor Transimpedanz $r_m$ in Ω: ein Verstärker, der den Strom einer Fotodiode in eine Spannung umsetzt.

In der Verstärkerstufe ist der Drainstrom des Transistors für kleine Signale eine spannungsgesteuerte Stromquelle: Er hängt von der Spannung zwischen Gate und Source ab, fließt aber zwischen Drain und Source. Ihre Steilheit ist die Steigung der Transistorkennlinie im Arbeitspunkt, 1 mS. Parallel dazu liegt der __Ausgangsleitwert__ $g_o$, hier mit 25 µS angenommen: Er beschreibt, dass der Drainstrom auch mit der Drain-Source-Spannung leicht steigt.

:::frage
„Ist eine Schaltung mit einem Transistor überhaupt linear?“
Für große Signale nicht: Der Drainstrom wächst mit dem Quadrat der Gate-Source-Spannung über der Schwelle. Linear ist das Kleinsignal-Ersatzschaltbild, in dem der Transistor für kleine Änderungen um den Arbeitspunkt durch eine gesteuerte Quelle mit der Steigung seiner Kennlinie ersetzt ist, hier 1 mS. Alle Verfahren dieses Themas gelten für Transistorschaltungen deshalb im Kleinsignalbetrieb; wie klein ein Signal dafür sein muss, zeigt [Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html).
:::

Idee der Herleitung: Man schreibt alle Gleichungen der Schaltung als eine lineare Vorschrift für die Unbekannten und zeigt, dass Summe und Vielfaches der Quellen zu Summe und Vielfachem der Lösungen führen.

:::herleitung
**Ausgangspunkt:** die Zweiggleichungen der Bauelemente und die Kirchhoffschen Regeln.

**Annahmen:** (i) Jede Zweiggleichung verknüpft Zweiggrößen nur über feste Faktoren und Ableitungen nach der Zeit; bei gesteuerten Quellen ist die Ausgangsgröße einer anderen Zweiggröße proportional. (ii) Die Werte der unabhängigen Quellen sind die einzigen Terme, die von keiner Unbekannten abhängen. (iii) Das Gleichungssystem hat für jede Anregung genau eine Lösung.

**Schritt 1**: Man bringt alle Zweig- und Kirchhoff-Gleichungen in die Form „Ausdruck in den Unbekannten gleich Quellenwerte“. Der Ausdruck links ist eine Vorschrift $\mathcal L$, die aus den Unbekannten $w$ (allen Zweigströmen und Zweigspannungen) nur Summen, feste Vielfache und Ableitungen bildet; rechts stehen die Quellenwerte $s$:

$$\mathcal L(w) = s$$

**Schritt 2** (entscheidender Schritt): Lösen $w_1$ und $w_2$ das System für die Anregungen $s_1$ bzw. $s_2$, so löst $\alpha_1 w_1 + \alpha_2 w_2$ das System für $\alpha_1 s_1 + \alpha_2 s_2$, denn Summen, feste Vielfache und Ableitungen reichen Summen und Vielfache unverändert durch:

$$\mathcal L(\alpha_1 w_1 + \alpha_2 w_2) = \alpha_1\,\mathcal L(w_1) + \alpha_2\,\mathcal L(w_2) = \alpha_1 s_1 + \alpha_2 s_2$$

**Schritt 3**: Weil die Lösung nach (iii) eindeutig ist, ist $\alpha_1 w_1 + \alpha_2 w_2$ die Lösung; jede einzelne Antwort, ein Bestandteil von $w$, erfüllt deshalb die Definition:

$$y(\alpha_1 x_1 + \alpha_2 x_2) = \alpha_1\,y(x_1) + \alpha_2\,y(x_2)$$

**Ergebnis:** Schaltungen aus Widerständen, Spulen, Kondensatoren, gesteuerten und unabhängigen Quellen sind linear in den Werten der unabhängigen Quellen.

**Woher die Faktoren kommen:** $\alpha_1$ und $\alpha_2$ gehen unverändert durch jede Gleichung, weil keine Gleichung eine Unbekannte quadriert oder mit einer anderen Unbekannten multipliziert.

**Proben:** Verstärkerstufe: 20 mV ergeben −46,51 mV, doppelt so viel wie 10 mV; 10 mV und −5 mV einzeln ergeben −23,26 mV und +11,63 mV, zusammen −11,63 mV wie 5 mV direkt. Gegenprobe: Eine Diode verletzt Schritt 2, weil ihr Strom exponentiell von der Spannung abhängt.

**Grenzen:** Mit nichtlinearen Bauelementen gilt die Linearität nur für ihr Kleinsignalmodell. Anfangsladungen von Kondensatoren und Anfangsströme von Spulen wirken wie zusätzliche Quellen und müssen beim Zerlegen mitgezählt werden.
:::

## Wechselgrößen: Impedanz und Admittanz

*Wie rechnet man mit Spulen und Kondensatoren, deren Zweiggleichungen Ableitungen enthalten?*

Ein Kondensator von 100 nF an einer Sinusspannung mit 1 V Amplitude und der Kreisfrequenz 10⁴ 1/s, entsprechend der Frequenz 1,59 kHz, führt einen Strom von 1 mA Amplitude, der der Spannung um eine Viertelperiode vorauseilt. Ein Widerstand von 1 kΩ führt bei derselben Spannung ebenfalls 1 mA, aber im Takt der Spannung. Für Sinusgrößen verhält sich der Kondensator also wie ein Widerstand, zu dem eine Phasenverschiebung hinzukommt.

:::grafik
Szene: st1/netzwerkanalyse/02-impedanzen · Vorlage: kennlinie-loglog
**Abbildung 3:** Betrag der Impedanz in Ω über der Kreisfrequenz von 10² bis 10⁶ 1/s, beide Achsen logarithmisch, für einen Widerstand von 1 kΩ, eine Spule von 100 mH und einen Kondensator von 100 nF; darunter der Winkel der Impedanz: 0°, +90° und −90°. Die drei Kurven schneiden sich bei 10⁴ 1/s und 1 kΩ. Spule und Kondensator verhalten sich bei Sinusgrößen wie Widerstände, deren Betrag mit der Frequenz steigt bzw. fällt, mit +90° bzw. −90° Phasenverschiebung.
:::

Den Rechenweg liefern [Zeiger](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html): Eine Sinusgröße wird durch ihre __komplexe Amplitude__ dargestellt, deren Betrag der Scheitelwert und deren Winkel die __Nullphase__ ist, die Phase zur Zeit null. Klingen in einer linearen Schaltung die Einschaltvorgänge ab, schwingen im eingeschwungenen Zustand alle Größen mit der Frequenz der Quelle. Eine Summe von Sinusgrößen gleicher Frequenz wird dann zur Summe ihrer Zeiger, und die Ableitung nach der Zeit wird zur Multiplikation mit $j\omega$. Deshalb gelten Knoten- und Maschenregel unverändert für die Zeiger.

**Die Akteure:**

- __$\underline U$__, __$\underline I$__: komplexe Amplituden von Spannung und Strom eines Zweigs; Betrag in V bzw. A gleich dem Scheitelwert, Winkel gleich der Nullphase. Unterstrichene Größen sind komplex; bei Gleichgrößen entfällt der Strich.
- __$\omega$__: Kreisfrequenz, $2\pi$ mal die Frequenz; im Beispiel 10⁴ 1/s.
- __$\underline Z$__: __Impedanz__, das Verhältnis der Zeiger von Spannung und Strom; in Ω. Ihr Betrag ist das Verhältnis der Amplituden, ihr Winkel die Phasenverschiebung der Spannung gegen den Strom.
- __$\underline Y$__: __Admittanz__, der Kehrwert der Impedanz; in S.
- __$j$__: die imaginäre Einheit, in der Elektrotechnik $j$ statt $i$, weil $i$ für Ströme steht.

:::formel Definition
$$\underline Z = \frac{\underline U}{\underline I}, \qquad \underline Y = \frac{1}{\underline Z}$$
:::

Man definiert die Impedanz so, weil sie die Zweiggleichung jedes linearen, quellenfreien Zweipols, also von Widerstand, Spule und Kondensator, in die Form des Ohmschen Gesetzes bringt; damit gelten alle Rechenverfahren für Widerstandsnetze auch für Wechselstromnetze.

:::formel Formel
$$\underline Z_R = R, \qquad \underline Z_L = j\omega L, \qquad \underline Z_C = \frac{1}{j\omega C} = -\frac{j}{\omega C}$$
:::

**So liest man das:** Bei der Spule wächst der Betrag der Impedanz proportional zur Frequenz, beim Kondensator fällt er umgekehrt proportional; bei 10⁴ 1/s haben 100 mH, 100 nF und 1 kΩ alle den Betrag 1 kΩ (Abbildung 3). Der Faktor $j$ bedeutet eine Drehung um 90°: An der Spule eilt die Spannung dem Strom um 90° voraus, am Kondensator um 90° nach. Grenzfälle: Bei Gleichstrom, ω gegen null, wird die Spule zum Kurzschluss und der Kondensator zur Unterbrechung; bei sehr hohen Frequenzen ist es umgekehrt.

**Kurz gesagt:** Für die Zeiger von Sinusgrößen im eingeschwungenen Zustand wird das Ableiten zum Multiplizieren mit $j\omega$; deshalb verhalten sich Spule und Kondensator wie Widerstände mit +90° bzw. −90° Phasenverschiebung, deren Betrag proportional zur Frequenz wächst bzw. umgekehrt proportional zu ihr fällt.

Idee der Herleitung: Man setzt die Zeiger in die Zweiggleichungen ein und ersetzt die Ableitung durch den Faktor $j\omega$.

:::herleitung
**Ausgangspunkt:** die Zweiggleichungen von Widerstand, Spule und Kondensator mit gleich gerichteten Zählpfeilen für Strom und Spannung,

$$u = R\,i, \qquad u = L\,\frac{di}{dt}, \qquad i = C\,\frac{du}{dt},$$

und die Darstellung einer Sinusgröße als Realteil ihres rotierenden Zeigers ([Zeiger und Sinussignale](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html)).

**Annahmen:** (i) eingeschwungener Zustand mit einer einzigen Kreisfrequenz ω; (ii) ideale, lineare Bauelemente.

**Schritt 1**: Spannung und Strom als Realteile ihrer rotierenden Zeiger:

$$u(t) = \mathrm{Re}\big\{\underline U\,\exp(j\omega t)\big\}, \qquad i(t) = \mathrm{Re}\big\{\underline I\,\exp(j\omega t)\big\}$$

**Schritt 2**: Ableiten nach der Zeit bringt den Faktor $j\omega$, weil die Ableitung von $\exp(j\omega t)$ gleich $j\omega\exp(j\omega t)$ ist; für die Spule folgt:

$$\mathrm{Re}\big\{\underline U\,\exp(j\omega t)\big\} = \mathrm{Re}\big\{j\omega L\,\underline I\,\exp(j\omega t)\big\}$$

**Schritt 3** (entscheidender Schritt): Stimmen zwei Realteile zu jeder Zeit überein, sind die Zeiger gleich: Zur Zeit null stimmen ihre Realteile überein, eine Viertelperiode später ihre Imaginärteile. Also:

$$\underline U = j\omega L\,\underline I$$

**Schritt 4**: Ebenso beim Kondensator, aufgelöst nach der Spannung, und beim Widerstand:

$$\underline I = j\omega C\,\underline U \quad\Rightarrow\quad \underline U = \frac{1}{j\omega C}\,\underline I$$

$$\underline U = R\,\underline I$$

**Ergebnis:**

$$\underline Z_R = R, \qquad \underline Z_L = j\omega L, \qquad \underline Z_C = \frac{1}{j\omega C} = -\frac{j}{\omega C}$$

**Woher die Faktoren kommen:** $j\omega$ stammt aus der Ableitung, beim Kondensator steht es im Nenner, weil dort der Strom die Ableitung der Spannung ist; $1/j$ ist $-j$.

**Proben:** Einheiten: 1/s mal H ist 1/s mal V s/A, also Ω; 1/(1/s mal F) ist 1/(1/s mal A s/V), also Ω. Grenzfall ω gegen null: Die Impedanz der Spule geht gegen null, die des Kondensators gegen unendlich. Zahlenwert: 10⁴ 1/s mal 0,1 H ergibt 1 kΩ, 1/(10⁴ 1/s mal 100 nF) ebenfalls.

**Grenzen:** Einschaltvorgänge und Signale aus mehreren Frequenzen gehorchen den Zeigern nur Frequenz für Frequenz; reale Spulen und Kondensatoren haben zusätzlich Verluste und parasitäre Anteile.
:::

::::beispiel Impedanzen und Admittanzen bei 10⁴ 1/s
**Gegeben:** $R$ = 1 kΩ, $L$ = 100 mH, $C$ = 100 nF, ω = 10⁴ 1/s.

**Gesucht:** Impedanz und Admittanz aller drei Bauelemente.

**Rechnung:** Spule und Kondensator:

$$\underline Z_L = j\cdot 10^4\ \tfrac{1}{\mathrm s}\cdot 0{,}1\ \mathrm H = j\cdot 1\ \mathrm{k\Omega}, \qquad \underline Y_L = \frac{1}{j\cdot 1\ \mathrm{k\Omega}} = -j\cdot 1\ \mathrm{mS}$$

$$\underline Z_C = \frac{1}{j\cdot 10^4\ \tfrac{1}{\mathrm s}\cdot 10^{-7}\ \mathrm F} = -j\cdot 1\ \mathrm{k\Omega}, \qquad \underline Y_C = j\cdot 1\ \mathrm{mS}$$

**Ergebnis:** **1 kΩ, j·1 kΩ und −j·1 kΩ; Admittanzen 1 mS, −j·1 mS und j·1 mS.**

**Einordnung:** Bei 10² 1/s sind es 10 Ω für die Spule und 100 kΩ für den Kondensator, bei 10⁶ 1/s umgekehrt: Hundertmal tiefere Frequenz macht die Spule hundertmal niederohmiger und den Kondensator hundertmal hochohmiger. Der Tiefpass in den Abschnitten zur Maschen- und Knotenanalyse arbeitet bei genau der Frequenz, bei der die Kondensatoren so hochohmig sind wie die Widerstände.
::::

## Wie viele Gleichungen eine Schaltung bestimmen

*Wie viele unbekannte Größen hat eine Schaltung, und wie viele unabhängige Gleichungen liefern Bauelemente und Kirchhoffsche Regeln?*

:::grafik
Szene: st1/netzwerkanalyse/02-topologie · Vorlage: netzwerkgraph
**Abbildung 4:** Das Kleinsignal-Ersatzschaltbild der Verstärkerstufe und sein Graph: vier Knoten (G, D, S, Masse) und sechs Zweige (Signalquelle, gesteuerte Quelle, Ausgangsleitwert, $R_D$, $R_L$, $R_S$). Hervorgehoben ist ein Baum aus drei Zweigen (Signalquelle, $R_D$, $R_S$); jeder der drei übrigen Zweige schließt mit Baumzweigen genau eine Masche. Von den Knotengleichungen ist eine überzählig, und jeder Verbindungszweig schließt genau eine neue Masche; zusammen sind es so viele unabhängige Gleichungen wie Unbekannte.
:::

**Die Akteure:**

- __Knoten__: ein Verbindungspunkt, an dem Zweige zusammenstoßen; gezählt wird jeder Punkt, an dem Bauelemente aneinandergrenzen, auch wenn sich der Strom dort nicht verzweigt, wie am Gate, an dem nur die Signalquelle endet. Punkte, die nur durch widerstandslose Leitungen verbunden sind, bilden einen einzigen Knoten. __$k$__: ihre Zahl; 4 in der Verstärkerstufe.
- __Zweig__: ein Bauelement oder eine Quelle zwischen zwei Knoten; eine reale Quelle aus Quelle und Innenwiderstand darf als ein Zweig zählen. __$z$__: ihre Zahl; 6 in der Verstärkerstufe.
- __Masche__: ein geschlossener Umlauf über Zweige.
- __Baum__: eine Auswahl von Zweigen, die alle Knoten verbindet, ohne einen Umlauf zu schließen; die übrigen Zweige heißen __Verbindungszweige__.
- __$n_K$__, __$n_M$__: Zahl der unabhängigen Knoten- bzw. Maschengleichungen.

**Das Zusammenspiel:** Jeder Zweig hat zwei Unbekannte, Strom und Spannung, zusammen also $2z$, in der Verstärkerstufe zwölf. Jeder Zweig liefert seine Zweiggleichung, das sind $z$ Gleichungen: bei einer Impedanz die Beziehung zwischen Strom und Spannung, bei einer unabhängigen Quelle den vorgegebenen Wert, bei einer gesteuerten Quelle die Verknüpfung mit ihrer Steuergröße. Die übrigen kommen von Kirchhoff, aber nicht jede Knoten- und Maschengleichung zählt: Von den $k$ Knotengleichungen ist eine die Folge der übrigen, und von den vielen möglichen Umläufen sind nur so viele unabhängig, wie es Verbindungszweige gibt. Abbildung 4 zeigt warum: Der Baum verbindet die vier Knoten mit drei Zweigen, und jeder der drei Verbindungszweige schließt genau eine neue Masche.

:::formel Satz
$$n_K = k - 1, \qquad n_M = z - k + 1, \qquad z + n_K + n_M = 2z$$
:::

**So liest man das:** Zusammen mit den Zweiggleichungen sind es genau so viele Gleichungen wie Unbekannte. Ein Verfahren, das die Unbekannten geschickt wählt, kommt mit $n_K$ oder mit $n_M$ Gleichungen aus; darauf beruhen Knoten- und Maschenanalyse. Fasst man hintereinanderliegende Bauelemente zu einem Zweig zusammen, etwa eine reale Quelle mit ihrem Innenwiderstand, verschwinden je ein Knoten und ein Zweig, und $n_M$ bleibt gleich; deshalb kommen auch Zählweisen, die nur Verzweigungspunkte als Knoten nehmen, auf dieselbe Zahl von Maschengleichungen.

**Kurz gesagt:** Eine zusammenhängende Schaltung liefert genau so viele Gleichungen wie Unbekannte: je Zweig eine Zweiggleichung, je Knoten außer einem eine unabhängige Knotengleichung und je Verbindungszweig eines Baums eine unabhängige Maschengleichung.

Idee der Herleitung: Man zählt die Zweige eines Baums und zeigt, dass die Baumzweige die Knotengleichungen und die Verbindungszweige die Maschengleichungen unabhängig machen.

:::herleitung
**Ausgangspunkt:** Knoten- und Maschenregel und der Baum eines Netzes ([Topologische Grundbegriffe](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/topologische-grundbegriffe.html)).

**Annahmen:** (i) Das Netz hängt zusammen. (ii) Jeder Zweig verbindet zwei verschiedene Knoten.

**Schritt 1**: Ein Baum mit $k$ Knoten hat $k - 1$ Zweige: Beginnt man mit einem Knoten, fügt jeder Baumzweig genau einen neuen Knoten hinzu, denn sonst schlösse er einen Umlauf.

$$z_\mathrm{Baum} = k - 1$$

**Schritt 2** (entscheidender Schritt): Jeder Verbindungszweig schließt mit Baumzweigen genau eine Masche, denn im Baum gibt es zwischen zwei Knoten genau einen Weg. Diese Maschen sind unabhängig, weil jede ihren eigenen Verbindungszweig enthält, der in keiner anderen vorkommt; jede weitere Masche ist eine Summe von ihnen. Ihre Zahl ist die Zahl der Verbindungszweige:

$$n_M = z - z_\mathrm{Baum} = z - k + 1$$

**Schritt 3**: Für die Knotenregeln arbeitet man den Baum von außen nach innen ab, beginnend bei Knoten mit nur einem Baumzweig und endend bei einem gewählten Bezugsknoten. Jede Knotengleichung enthält dabei genau einen Baumzweigstrom, der in den schon behandelten Gleichungen nicht vorkam; deshalb sind die $k - 1$ Gleichungen der übrigen Knoten unabhängig:

$$n_K = k - 1$$

**Schritt 4**: Die Gleichung des Bezugsknotens folgt aus den übrigen: Addiert man alle $k$ Knotengleichungen, kommt jeder Zweigstrom einmal als abfließend und einmal als zufließend vor.

$$\sum_{\text{alle Knoten}}\ \sum_{\text{abfließende Ströme}} \underline I = 0$$

**Ergebnis:**

$$n_K = k - 1, \qquad n_M = z - k + 1, \qquad z + n_K + n_M = 2z$$

**Woher die Faktoren kommen:** Die 1 in $k - 1$ ist der Bezugsknoten, dessen Gleichung überzählig ist; $z - k + 1$ ist die Zahl der Verbindungszweige.

**Proben:** Verstärkerstufe: $k$ = 4, $z$ = 6, also 6 + 3 + 3 = 12 Gleichungen für 12 Unbekannte. Eine einzelne Masche aus Quelle und Widerstand: $k$ = 2, $z$ = 2, eine Knoten- und eine Maschengleichung.

**Grenzen:** Entartete Anordnungen idealer Elemente machen das System singulär, obwohl die Zählung stimmt: zwei verschiedene ideale Spannungsquellen parallel (keine Lösung), zwei gleiche (unendlich viele Lösungen) oder ein verlustloser Schwingkreis aus 100 mH und 100 nF an einer Stromquelle bei 10⁴ 1/s, wo seine Admittanz null ist. Sie verletzen Annahme (iii) der Linearität, nicht die Zählung.
:::

::::beispiel Gleichungen der Verstärkerstufe und des RC-Tiefpasses gezählt
**Gegeben:** Verstärkerstufe mit $k$ = 4 und $z$ = 6; zweistufiger RC-Tiefpass aus Abbildung 7 mit der Quelle als eigenem Zweig, $k$ = 4 und $z$ = 5, oder mit Quelle und $R_1$ als einer realen Quelle, $k$ = 3 und $z$ = 4.

**Gesucht:** Zahl der Unbekannten und der unabhängigen Knoten- und Maschengleichungen.

**Rechnung:** Verstärkerstufe:

$$2z = 12, \qquad n_K = 4 - 1 = 3, \qquad n_M = 6 - 4 + 1 = 3$$

Tiefpass mit eigenem Quellenzweig und mit zusammengefasster realer Quelle:

$$2z = 10, \quad n_K = 3, \quad n_M = 2; \qquad 2z = 8, \quad n_K = 2, \quad n_M = 2$$

**Ergebnis:** **Verstärkerstufe 12 Unbekannte, je 3 Knoten- und Maschengleichungen; Tiefpass 10 bzw. 8 Unbekannte, 3 bzw. 2 Knoten- und 2 Maschengleichungen.**

**Einordnung:** Beide Verfahren lösen den Tiefpass mit zwei statt acht Gleichungen. Das Zusammenfassen einer realen Quelle spart einen Knoten; die Maschenzahl bleibt, weil Knoten und Zweig gemeinsam verschwinden.
::::

## Ersatzquellen nach Thévenin und Norton

*Warum verhält sich jedes lineare Netz an zwei Klemmen wie eine einzige Quelle mit Innenimpedanz, und wie bestimmt man die beiden Größen?*

Man belaste den Ausgang der Verstärkerstufe dreimal: offen, mit 10 kΩ und kurzgeschlossen. Die Ausgangsspannung beträgt −43,96 mV, −23,26 mV und null, der Ausgangsstrom null, −2,33 µA und −4,94 µA. Trägt man die Spannung über dem Strom auf, liegen alle drei Punkte auf einer Geraden, und jede weitere Last liefert einen Punkt auf derselben Geraden. Eine Gerade ist durch zwei Zahlen festgelegt, und eine Spannungsquelle mit Innenwiderstand hat genau eine solche Kennlinie.

:::grafik
Szene: st1/netzwerkanalyse/02-ersatzquelle-ueberlagerung · Vorlage: schaltbild-ueberlagerung
**Abbildung 5:** (a) Ein lineares Netz mit unabhängigen Quellen, einer gesteuerten Quelle und Impedanzen; die Last an den Klemmen A und B ist durch eine Stromquelle $\underline I_A$ ersetzt. (b) Nur die inneren Quellen wirken, die Klemmen sind offen: Die Klemmenspannung ist die Leerlaufspannung. (c) Die inneren unabhängigen Quellen sind null, die Spannungsquelle als Kurzschluss, die Stromquelle als Unterbrechung gezeichnet; die gesteuerte Quelle bleibt aktiv, und nur $\underline I_A$ wirkt. (d) Die beiden gleichwertigen Ersatzschaltungen mit den Werten der Verstärkerstufe: −43,96 mV in Reihe mit 8,90 kΩ bzw. −4,94 µA parallel zu 0,112 mS. Die Klemmenspannung ist die Summe zweier Beiträge, einer unabhängig vom Klemmenstrom, einer ihm proportional; deshalb beschreiben zwei Zahlen das Netz von außen vollständig.
:::

**Die Akteure:**

- __A__, __B__: die Klemmen des Netzes; in der Verstärkerstufe Drain und Masse.
- __$\underline U_{AB}$__: Klemmenspannung; __$\underline I_A$__: Klemmenstrom, der bei A aus dem Netz in die Last fließt.
- __$\underline U_{LL}$__: __Leerlaufspannung__, die Klemmenspannung bei offenen Klemmen; −43,96 mV in der Verstärkerstufe bei 10 mV Signal.
- __$\underline I_{KS}$__: __Kurzschlussstrom__, der Klemmenstrom bei kurzgeschlossenen Klemmen; −4,938 µA.
- __$\underline Z_i$__, __$\underline Y_i$__: __Innenimpedanz__ und Innenadmittanz der Ersatzquelle, Kehrwerte voneinander; 8,90 kΩ bzw. 0,112 mS.

**Das Zusammenspiel:**

**Schritt 1**: Man ersetzt die Last durch eine Stromquelle, die denselben Strom $\underline I_A$ führt (Abbildung 5a). Für das Netz ändert sich nichts, denn es bemerkt von der Last nur Strom und Spannung an den Klemmen.

**Schritt 2**: Die Klemmenspannung ist eine Antwort der linearen Schaltung auf alle unabhängigen Quellen: die inneren und die Stromquelle $\underline I_A$. Nach der Definition der Linearität ist sie die Summe der Antworten auf beide Gruppen.

**Schritt 3**: Wirken nur die inneren Quellen, ist $\underline I_A$ null, die Klemmen sind offen; die Antwort ist die Leerlaufspannung (Abbildung 5b).

**Schritt 4**: Wirkt nur $\underline I_A$, werden die inneren unabhängigen Quellen null: Spannungsquellen werden zu Kurzschlüssen, Stromquellen zu Unterbrechungen. Gesteuerte Quellen bleiben, denn sie sind keine Anregung; ihr Wert folgt aus Spannungen und Strömen des Netzes, die $\underline I_A$ ebenfalls verändert (Abbildung 5c). Übrig bleibt ein lineares Netz, dessen einzige Anregung $\underline I_A$ ist; seine Klemmenspannung ist $\underline I_A$ proportional.

**Schritt 5**: Die Summe beider Beiträge ist eine Gerade: Leerlaufspannung minus Innenimpedanz mal Klemmenstrom. Bei kurzgeschlossenen Klemmen ist die Klemmenspannung null; daraus folgt die Innenimpedanz als Quotient aus Leerlaufspannung und Kurzschlussstrom.

:::formel Satz
$$\underline U_{AB} = \underline U_{LL} - \underline Z_i\,\underline I_A, \qquad \underline Z_i = \frac{\underline U_{LL}}{\underline I_{KS}}$$
:::

**So liest man das:** Die Leerlaufspannung ist, was das Netz unbelastet liefert; die Innenimpedanz bestimmt, wie stark die Klemmenspannung unter Last einbricht. Grenzfälle: Ohne Strom liegt die Leerlaufspannung an, bei kurzgeschlossenen Klemmen fließt der Kurzschlussstrom. Die zweite Formel setzt voraus, dass der Kurzschlussstrom endlich und von null verschieden ist. Bei der Verstärkerstufe sind Leerlaufspannung und Kurzschlussstrom negativ, weil die Stufe das Signal invertiert; die Gerade gilt für die Zeiger ebenso wie für Gleichgrößen.

**Kurz gesagt:** Von außen gesehen verhält sich jedes lineare Netz an zwei Klemmen, dessen gesteuerte Quellen nur von Größen im Netz selbst gesteuert werden, wie eine Quelle mit Innenimpedanz: Seine Klemmenspannung ist die Leerlaufspannung minus Innenimpedanz mal Klemmenstrom, solange die Innenimpedanz endlich ist.

Idee der Herleitung: Man ersetzt die Last durch eine Stromquelle und zerlegt die Klemmenspannung nach der Linearität in den Beitrag der inneren Quellen und den Beitrag des Klemmenstroms.

:::herleitung
**Ausgangspunkt:** die Linearität (Abschnitt *Lineare Schaltungen*) und die Ersetzung der Last durch eine Stromquelle gleichen Stroms.

**Annahmen:** (i) Das Netz ist linear und hat für jeden Klemmenstrom genau eine Lösung. (ii) Die Steuergrößen aller gesteuerten Quellen liegen im Netz selbst, nicht in der Last.

**Schritt 1**: Ersetzt man die Last durch eine Stromquelle $\underline I_A$, ist die Klemmenspannung eine Antwort auf die inneren unabhängigen Quellen mit den Werten $\underline X_1$ bis $\underline X_m$ und auf $\underline I_A$:

$$\underline U_{AB} = \underline U_{AB}(\underline X_1, \ldots, \underline X_m, \underline I_A)$$

**Schritt 2** (entscheidender Schritt): Nach der Linearität ist sie eine Summe fester Vielfacher dieser Werte; die Faktoren $h_\mu$ und $h_A$ hängen nur vom Netz und von ω ab:

$$\underline U_{AB} = \sum_{\mu=1}^{m} h_\mu\,\underline X_\mu + h_A\,\underline I_A$$

**Schritt 3**: Bei offenen Klemmen ist $\underline I_A$ null; die Summe über die inneren Quellen ist die Leerlaufspannung:

$$\underline U_{LL} = \sum_{\mu=1}^{m} h_\mu\,\underline X_\mu$$

**Schritt 4**: Der Faktor $h_A$ ist die Klemmenspannung je Klemmenstrom bei abgeschalteten inneren unabhängigen Quellen; die gesteuerten Quellen gehören zum Netz und stecken in $h_A$. Weil $\underline I_A$ bei A aus dem Netz herausfließt, ist $h_A$ das Negative der Impedanz, die man an den Klemmen in das Netz hinein sieht:

$$\underline Z_i = -h_A$$

**Schritt 5**: Eingesetzt und für den Kurzschluss ausgewertet:

$$\underline U_{AB} = \underline U_{LL} - \underline Z_i\,\underline I_A$$

$$0 = \underline U_{LL} - \underline Z_i\,\underline I_{KS}$$

**Ergebnis:**

$$\underline U_{AB} = \underline U_{LL} - \underline Z_i\,\underline I_A, \qquad \underline Z_i = \frac{\underline U_{LL}}{\underline I_{KS}}$$

**Woher die Faktoren kommen:** Die Leerlaufspannung sammelt alle Beiträge der inneren Quellen; die Innenimpedanz ist der einzige Faktor vor dem Klemmenstrom; das Minuszeichen stammt aus der Zählrichtung von $\underline I_A$ aus dem Netz heraus.

**Proben:** Einheit: Ω mal A ist V. Verstärkerstufe mit 10 kΩ Last: Der Klemmenstrom ist −2,326 µA, und −43,96 mV minus 8,901 kΩ mal (−2,326 µA) ergibt −23,26 mV, denselben Wert wie die vollständige Rechnung im Abschnitt *Knotenpotentialanalyse*.

**Grenzen:** Steuert eine Größe in der Last eine Quelle im Netz, verletzt das Annahme (ii); dann muss die Last mitgerechnet werden. Ist die Innenimpedanz unendlich, gibt es nur die Stromform, ist sie null, nur die Spannungsform. Für große Signale an nichtlinearen Bauelementen gilt der Satz nicht.
:::

::::beispiel Ersatzquelle am Ausgang der Verstärkerstufe
**Gegeben:** das Kleinsignal-Ersatzschaltbild aus Abbildung 1 ohne Last: Signal 10 mV mit 10 kΩ Innenwiderstand, Steilheit $g_m$ = 1 mS, Ausgangsleitwert $g_o$ = 25 µS, $R_D$ = 10 kΩ ($G_D$ = 0,1 mS), $R_S$ = 1 kΩ ($G_S$ = 1 mS). Das Gate nimmt keinen Strom auf; am Gate liegt deshalb die volle Signalspannung, $\underline U_G$ = 10 mV.

**Gesucht:** Leerlaufspannung, Kurzschlussstrom und Innenimpedanz am Drain; die Ausgangsspannung an 10 kΩ und an 100 kΩ.

**Rechnung:** (a) Leerlauf. Knotenregeln an D und an S; der Strom der Transistorstrecke von D nach S ist der gesteuerte Strom plus der Strom durch $g_o$:

$$G_D\,\underline U_D + g_m(\underline U_G - \underline U_S) + g_o(\underline U_D - \underline U_S) = 0$$

$$g_m(\underline U_G - \underline U_S) + g_o(\underline U_D - \underline U_S) = G_S\,\underline U_S$$

Die Differenz beider Gleichungen, die Ströme durch $R_D$ und $R_S$ sind entgegengesetzt gleich:

$$G_D\,\underline U_D + G_S\,\underline U_S = 0 \quad\Rightarrow\quad \underline U_S = -0{,}1\,\underline U_D$$

In die erste Gleichung eingesetzt, mit Leitwerten in mS, Spannungen in mV und Strömen in µA:

$$0{,}1\,\underline U_D + 1\cdot(10 + 0{,}1\,\underline U_D) + 0{,}025\cdot 1{,}1\,\underline U_D = 0$$

$$\underline U_{LL} = \underline U_D = -\frac{10}{0{,}2275}\ \mathrm{mV} = -43{,}96\ \mathrm{mV}$$

(b) Kurzschluss: Der Drain liegt auf null, es bleibt die Knotenregel an S:

$$g_m(\underline U_G - \underline U_S) - g_o\,\underline U_S = G_S\,\underline U_S$$

$$\underline U_S = \frac{g_m\,\underline U_G}{g_m + g_o + G_S} = 4{,}938\ \mathrm{mV}$$

Der Strom der Transistorstrecke kommt aus dem Kurzschluss und fließt in den Drain hinein; der Klemmenstrom heraus ist deshalb negativ:

$$\underline I_{KS} = -\big[g_m(\underline U_G - \underline U_S) - g_o\,\underline U_S\big] = -4{,}938\ \mu\mathrm{A}$$

(c) Innenimpedanz:

$$\underline Z_i = \frac{-43{,}96\ \mathrm{mV}}{-4{,}938\ \mu\mathrm{A}} = 8{,}90\ \mathrm{k\Omega}$$

(d) Last: Mit dem Klemmenstrom $\underline U_{AB}/R_L$ im Satz wird die Ersatzquelle zum Spannungsteiler:

$$\underline U_{AB} = \underline U_{LL}\,\frac{R_L}{R_L + \underline Z_i} = -43{,}96\ \mathrm{mV}\cdot\frac{10\ \mathrm{k\Omega}}{18{,}90\ \mathrm{k\Omega}} = -23{,}26\ \mathrm{mV}$$

An 100 kΩ ergibt dieselbe Formel −40,36 mV.

**Ergebnis:** **Leerlaufspannung −43,96 mV, Kurzschlussstrom −4,938 µA, Innenimpedanz 8,90 kΩ; an 10 kΩ −23,26 mV, an 100 kΩ −40,36 mV.**

**Einordnung:** Die Last von 10 kΩ senkt den Betrag der Verstärkung von 4,40 auf 2,33, weil sie kaum größer ist als die Innenimpedanz; eine zehnmal größere Last nimmt nur 8 % weg. Für jede weitere Last genügt nun der Spannungsteiler, ohne das Netz neu zu rechnen.
::::

Löst man den Satz nach dem Klemmenstrom auf, entsteht die __Ersatzstromquelle__ nach Norton: eine Stromquelle $\underline I_{KS}$ mit der Admittanz $\underline Y_i$ parallel.

$$\underline I_A = \frac{\underline U_{LL} - \underline U_{AB}}{\underline Z_i} = \underline I_{KS} - \underline Y_i\,\underline U_{AB}$$

Beide Formen haben dieselbe Kennlinie und sind von außen nicht zu unterscheiden; die Spannungsform heißt __Ersatzspannungsquelle__ nach Thévenin (Abbildung 5d). Dieselbe Umrechnung verwandelt jede reale Spannungsquelle in eine reale Stromquelle und umgekehrt, etwa 1 V mit 1 kΩ in 1 mA mit 1 mS; Maschen- und Knotenanalyse brauchen genau diese Umwandlung. Ideale Quellen lassen sich nicht umwandeln: Eine ideale Spannungsquelle hätte als Stromquelle einen unendlichen Kurzschlussstrom, eine ideale Stromquelle als Spannungsquelle eine unendliche Leerlaufspannung.

**Kurz gesagt:** Leerlaufspannung durch Kurzschlussstrom ist die Innenimpedanz; deshalb beschreiben Spannungs- und Stromform dieselbe Quelle, solange beide Größen endlich und von null verschieden sind.

:::frage
„Ist die Ersatzquelle auch innen gleichwertig, etwa bei der Verlustleistung?“
Nein, gleichwertig ist nur das Verhalten an den Klemmen. Eine Quelle mit 1 V Amplitude und 1 kΩ verbraucht im Leerlauf in der Spannungsform nichts, denn es fließt kein Strom; die gleichwertige Stromform setzt im Leerlauf im Innenleitwert 0,5 mW um. Im Kurzschluss ist es umgekehrt. Wer die Leistung im Inneren eines Netzes wissen will, muss das Original rechnen; für alles, was an den Klemmen geschieht, genügt die Ersatzquelle ([Energieumsetzung und Leistungsanpassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/energieumsetzung-und-leistungsanpassung.html)).
:::

### Die Innenimpedanz bei gesteuerten Quellen

*Wie bestimmt man die Innenimpedanz, wenn das Netz gesteuerte Quellen enthält?*

Drei Wege führen zur Innenimpedanz. Der erste, Leerlaufspannung durch Kurzschlussstrom, funktioniert immer, wenn beide endlich und von null verschieden sind. Der zweite schaltet die inneren unabhängigen Quellen ab und fasst die übrigen Impedanzen zusammen, durch Reihen- und Parallelschaltung und wo nötig mit der [Stern-Dreieck-Transformation](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/stern-dreieck-transformation.html); er funktioniert nur ohne gesteuerte Quellen, denn eine aktive gesteuerte Quelle ist im Allgemeinen keine Impedanz und darf nicht abgeschaltet werden. Der dritte ist der allgemeine: Man schaltet die unabhängigen Quellen ab, lässt die gesteuerten aktiv, legt an die Klemmen eine __Testspannung__ $\underline U_T$ und berechnet den Strom $\underline I_T$, der in die Klemme A hineinfließt.

$$\underline Z_i = \frac{\underline U_T}{\underline I_T}$$

Das folgt aus Schritt 4 der Herleitung: Mit abgeschalteten unabhängigen Quellen ist die Klemmenspannung gleich Innenimpedanz mal hineinfließendem Strom.

::::beispiel Innenimpedanz der Verstärkerstufe mit Testquelle
**Gegeben:** die Verstärkerstufe wie oben ohne Last; Signalquelle abgeschaltet, das Gate liegt damit auf null; Testspannung $\underline U_T$ = 1 V am Drain.

**Gesucht:** der Strom in den Drain und die Innenimpedanz, mit aktiver und mit fälschlich abgeschalteter gesteuerter Quelle.

**Rechnung:** Knotenregel an S mit aktiver gesteuerter Quelle:

$$g_m(0 - \underline U_S) + g_o(\underline U_T - \underline U_S) = G_S\,\underline U_S$$

$$\underline U_S = \frac{g_o\,\underline U_T}{g_m + g_o + G_S} = 12{,}35\ \mathrm{mV}$$

Strom in den Drain, durch $R_D$ und durch die Transistorstrecke:

$$\underline I_T = G_D\,\underline U_T + g_m(0 - \underline U_S) + g_o(\underline U_T - \underline U_S)$$

$$\underline I_T = 100\ \mu\mathrm{A} - 12{,}3457\ \mu\mathrm{A} + 24{,}6914\ \mu\mathrm{A} = 112{,}3457\ \mu\mathrm{A}$$

$$\underline Z_i = \frac{1\ \mathrm V}{112{,}346\ \mu\mathrm{A}} = 8{,}90\ \mathrm{k\Omega}$$

Ohne gesteuerte Quelle bleiben $g_o$ und $R_S$ in Reihe, 41 kΩ, parallel zu $R_D$:

$$\underline I_T = 100\ \mu\mathrm{A} + \frac{1\ \mathrm V}{41\ \mathrm{k\Omega}} = 124{,}39\ \mu\mathrm{A}, \qquad \frac{1\ \mathrm V}{124{,}39\ \mu\mathrm{A}} = 8{,}04\ \mathrm{k\Omega}$$

**Ergebnis:** **8,90 kΩ, wie aus Leerlauf und Kurzschluss; mit abgeschalteter gesteuerter Quelle falsch 8,04 kΩ.**

**Einordnung:** Der Zweig aus Transistor und $R_S$ führt je Volt 12,346 µA, genau den Strom durch $R_S$; das sind 81 kΩ, knapp doppelt so viel wie die 41 kΩ ohne gesteuerte Quelle, und die Drain-Source-Strecke allein hat mit 80 kΩ genau das Doppelte von 40 kΩ. Dass $R_D$ parallel liegt, verdünnt den Unterschied auf knapp 10 %.
::::

:::grafik
Szene: st1/netzwerkanalyse/02-innenwiderstand · Vorlage: schaltbild-vergleich
**Abbildung 6:** Innenimpedanz der Verstärkerstufe mit einer Testspannung am Drain; die Signalquelle ist abgeschaltet, ihr Innenwiderstand bleibt, das Gate liegt damit auf null. (a) Richtig, mit aktiver gesteuerter Quelle: Je Volt Testspannung fließen 100 µA durch $R_D$ und 12,35 µA in den Zweig aus Transistor und $R_S$, zusammen 8,90 kΩ; dieser Zweig allein hat 81 kΩ. (b) Falsch, mit entfernter gesteuerter Quelle: Der Zweig hat nur 41 kΩ, zusammen 8,04 kΩ. Gesteuerte Quellen bleiben beim Bestimmen der Innenimpedanz aktiv; der Source-Widerstand macht die Drain-Source-Strecke doppelt so hochohmig.
:::

Abbildung 6a zeigt, warum die gesteuerte Quelle den Ausgang hochohmiger macht. Die Testspannung treibt Strom durch den Ausgangsleitwert in den Source-Knoten; der Strom durch $R_S$ hebt dessen Potential an, je Volt Testspannung um 12,35 mV. Das Gate liegt fest auf null, also wird die Gate-Source-Spannung negativ, und die gesteuerte Quelle führt 12,35 µA gegen die Richtung des Teststroms. Durch $g_o$ fließen 24,69 µA, zusammen bleiben 12,35 µA: Der Zweig aus Transistor und $R_S$ wirkt wie 81 kΩ statt wie 41 kΩ. Der Source-Widerstand wirkt hier als __Gegenkopplung__, eine Rückwirkung, die einer Änderung des Drainstroms entgegenwirkt. Wer die gesteuerte Quelle abschaltet (Abbildung 6b), unterschlägt diese Rückwirkung.

:::fehlvorstellung
„Für die Innenimpedanz setzt man alle Quellen auf null.“ Das liegt nahe, weil die Regel in Netzen ohne gesteuerte Quellen stimmt und dort so gelernt wird. Abgeschaltet werden nur die unabhängigen Quellen, denn nur sie sind Anregung; eine gesteuerte Quelle beschreibt das Verhalten eines Bauelements im Netz, etwa des Transistors, und bleibt aktiv. In der Verstärkerstufe ergibt die richtige Rechnung 8,90 kΩ, die falsche 8,04 kΩ, 9,7 % zu wenig; der Zweig aus Transistor und $R_S$ hat 81 kΩ statt 41 kΩ.
:::

## Die Maschenstromanalyse

*Wie kommt man mit z − k + 1 Gleichungen aus, und wie stellt man sie auf, ohne zuerst alle Zweigströme anzusetzen?*

Der zweistufige RC-Tiefpass in Abbildung 7 hat mit der Quelle als eigenem Zweig fünf Zweige und vier Knoten, also zehn Unbekannte. Die Maschenanalyse löst ihn mit zwei Gleichungen.

:::grafik
Szene: st1/netzwerkanalyse/02-maschenstroeme · Vorlage: schaltbild-matrix
**Abbildung 7:** Zweistufiger RC-Tiefpass: Quelle 1 V, $R_1$ und $R_2$ je 1 kΩ, $C_1$ und $C_2$ je 100 nF gegen Masse, bei 10⁴ 1/s je −j·1 kΩ. Die Maschenströme $\underline I_\mathrm{I}$ und $\underline I_\mathrm{II}$ laufen im Uhrzeigersinn; im gemeinsamen Zweig $C_1$ fließt ihre Differenz. Daneben die Matrixgleichung mit der Impedanzmatrix (1 − j, j; j, 1 − 2j) kΩ und der rechten Seite (1 V, 0). Zwei Maschenströme beschreiben alle Zweigströme; die Knotenregel ist von selbst erfüllt.
:::

**Die Akteure:**

- __$\underline U_q$__: Quellenspannung; 1 V Amplitude, Nullphase null.
- __$R_1$__, __$R_2$__: je 1 kΩ; __$C_1$__, __$C_2$__: je 100 nF, mit der Impedanz __$\underline Z_C$__ von −j·1 kΩ bei 10⁴ 1/s.
- __$\underline I_1, \ldots, \underline I_{n_M}$__: __Maschenströme__, gedachte Ströme, die je eine Masche umlaufen; in A. Im Beispiel heißen sie nach ihren Maschen $\underline I_\mathrm{I}$ und $\underline I_\mathrm{II}$.
- __$\mathbf Z$__: __Impedanzmatrix__ mit den Einträgen $\underline Z_{\mu\nu}$, Zeile μ für die Masche μ, Spalte ν für den Maschenstrom ν; in Ω.
- __$\underline U_{q\mu}$__: Summe der Quellenspannungen, die den Maschenstrom μ antreiben; in V.

**Das Zusammenspiel:**

**Schritt 1**: Man wählt $z - k + 1$ unabhängige Maschen und ordnet jeder einen Maschenstrom zu. In einer Schaltung, die sich ohne Kreuzungen zeichnen lässt, genügen die Fenster des Schaltbilds; allgemein nimmt man die Maschen der Verbindungszweige eines Baums. Die Richtung jedes Maschenstroms ist frei, der Umlaufsinn seiner Masche ist seine Richtung; eine andere Wahl kehrt nur Vorzeichen um.

**Schritt 2**: Jeder Zweigstrom ist die Summe der Maschenströme durch den Zweig, mit Vorzeichen nach ihrer Richtung: $R_1$ führt $\underline I_\mathrm{I}$, $R_2$ und $C_2$ führen $\underline I_\mathrm{II}$, $C_1$ führt die Differenz. Weil jeder Maschenstrom in jeden Knoten seines Umlaufs hinein- und wieder herausfließt, ist jede Knotenregel von selbst erfüllt.

**Schritt 3**: Für jede Masche gilt die Maschenregel: Die Spannungen an den Impedanzen in Umlaufrichtung ergeben zusammen die antreibende Quellenspannung.

**Schritt 4**: Ordnet man nach den Maschenströmen, steht auf der Diagonalen die Summe aller Impedanzen der Masche. Außerhalb stehen die gemeinsamen Impedanzen zweier Maschen, jede positiv, wenn beide Maschenströme sie in derselben Richtung durchfließen, sonst negativ. Rechts steht die Summe der Quellenspannungen der Masche, positiv für eine Quelle, die den Maschenstrom antreibt, ihn also vom Minus- zum Pluspol durch sich hindurchführt.

**Schritt 5**: Man löst die $z - k + 1$ Gleichungen; die Zweigströme folgen aus Schritt 2, die Zweigspannungen aus den Zweiggleichungen.

:::formel Satz
$$\begin{pmatrix} \underline Z_{11} & \cdots & \underline Z_{1,n_M} \\ \vdots & \ddots & \vdots \\ \underline Z_{n_M,1} & \cdots & \underline Z_{n_M,n_M} \end{pmatrix} \begin{pmatrix} \underline I_{1} \\ \vdots \\ \underline I_{n_M} \end{pmatrix} = \begin{pmatrix} \underline U_{q1} \\ \vdots \\ \underline U_{q,n_M} \end{pmatrix}$$
:::

**So liest man das:** Jeder Maschenstrom wird mit allen Impedanzen seiner eigenen Masche multipliziert, ein Nachbarstrom nur mit den gemeinsamen Impedanzen; die Zahl der Zeilen ist $n_M$. Ohne gesteuerte Quellen ist die Matrix symmetrisch, $\underline Z_{\mu\nu}$ gleich $\underline Z_{\nu\mu}$, weil jede gemeinsame Impedanz in beiden Maschengleichungen mit demselben Vorzeichen steht; das ist eine bequeme Probe. Für den Tiefpass, mit gleicher Impedanz beider Kondensatoren:

$$\begin{pmatrix} R_1 + \underline Z_C & -\underline Z_C \\ -\underline Z_C & R_2 + 2\,\underline Z_C \end{pmatrix} \begin{pmatrix} \underline I_\mathrm{I} \\ \underline I_\mathrm{II} \end{pmatrix} = \begin{pmatrix} \underline U_q \\ 0 \end{pmatrix}$$

**Kurz gesagt:** Maschenströme erfüllen die Knotenregel von selbst; deshalb genügen die $z - k + 1$ Maschengleichungen, solange jeder Zweig eine Impedanz oder eine Spannungsquelle ist.

Idee der Herleitung: Man drückt jeden Zweigstrom durch Maschenströme aus, setzt in die Maschenregel ein und ordnet nach den Maschenströmen.

:::herleitung
**Ausgangspunkt:** die Maschenregel für Zeiger und die Zweiggleichung $\underline U = \underline Z\,\underline I$ jeder Impedanz.

**Annahmen:** (i) Die Zweige enthalten nur Impedanzen und unabhängige Spannungsquellen; reale Stromquellen sind vorher in Spannungsquellen umgewandelt. (ii) Die $n_M$ gewählten Maschen sind unabhängig.

**Schritt 1**: Jeder Zweigstrom ist eine Summe von Maschenströmen; das Vorzeichen $\sigma_{\nu}$ ist +1, wenn der Maschenstrom ν den Zweig in dessen Zählrichtung durchfließt, −1 entgegen und null, wenn er ihn nicht berührt:

$$\underline I_\mathrm{Zweig} = \sum_{\nu=1}^{n_M} \sigma_{\nu}\,\underline I_\nu$$

**Schritt 2** (entscheidender Schritt): Die Knotenregel ist damit erfüllt, ohne dass man sie aufstellt: Ein Maschenstrom, der einen Knoten berührt, fließt über einen Zweig hinein und über einen anderen hinaus und trägt zur Bilanz des Knotens null bei.

$$\sum_{\text{Zweige am Knoten}} \underline I_{\mathrm{Zweig,\,ab}} = \sum_{\nu\ \text{berührt den Knoten}} (\underline I_\nu - \underline I_\nu) = 0$$

**Schritt 3**: Maschenregel für Masche μ, Spannungen in Umlaufrichtung: Die Spannung an jeder Impedanz ist die Impedanz mal dem Strom, der sie in Umlaufrichtung durchfließt; zusammen ergeben sie die antreibenden Quellenspannungen:

$$\sum_{\text{Impedanzen von }\mu} \underline Z\,\underline I_{\text{in Umlaufrichtung}} = \underline U_{q\mu}$$

**Schritt 4**: Durch jede Impedanz fließt nach Schritt 1 die Summe der Maschenströme mit ihren Vorzeichen; in Umlaufrichtung von μ gezählt, ist das $\sigma_\mu$ mal diese Summe. Ein Maschenstrom ν trägt deshalb in der Gleichung von μ mit $\sigma_\mu\sigma_\nu\,\underline Z$ bei; das Produkt der Vorzeichen ist +1, wenn μ und ν die Impedanz in derselben Richtung durchlaufen, sonst −1. Eine Impedanz kann dabei zu mehr als zwei Maschen gehören. Nach Maschenströmen geordnet:

$$\underline Z_{\mu\mu} = \sum_{\text{Impedanzen von }\mu} \underline Z$$

$$\underline Z_{\mu\nu} = \sum_{\text{gemeinsam von }\mu, \nu} \sigma_\mu\,\sigma_\nu\,\underline Z$$

**Ergebnis:** die Matrixgleichung oben.

**Woher die Faktoren kommen:** Die Diagonale entsteht, weil der eigene Maschenstrom durch alle Impedanzen seiner Masche fließt, ein Nebeneintrag, weil der Nachbarstrom durch die gemeinsamen Impedanzen fließt; das Vorzeichen ist der Richtungsvergleich aus Schritt 4. Weil das Produkt der Vorzeichen nicht von der Reihenfolge abhängt, steht in der Gleichung von ν derselbe Eintrag, daher die Symmetrie.

**Proben:** Eine einzelne Masche aus Quelle und Widerstand ergibt $R\,\underline I = \underline U_q$, das Ohmsche Gesetz. Tiefpass: Diagonale $R_1 + \underline Z_C$ und $R_2 + 2\underline Z_C$, Nebeneintrag $-\underline Z_C$, weil die beiden Maschenströme $C_1$ entgegengesetzt durchfließen.

**Grenzen:** Ideale Stromquellen lassen sich nicht umwandeln; man legt die Maschen dann so, dass nur ein Maschenstrom durch sie fließt, der damit bekannt ist. Gesteuerte Quellen fügen Einträge hinzu, die die Symmetrie im Allgemeinen brechen.
:::

::::beispiel Zweistufiger RC-Tiefpass mit Maschenströmen
**Gegeben:** $\underline U_q$ = 1 V (Nullphase null), $R_1$ = $R_2$ = 1 kΩ, $C_1$ = $C_2$ = 100 nF, ω = 10⁴ 1/s, also $\underline Z_C$ = −j·1 kΩ.

**Gesucht:** die Maschenströme und die Ausgangsspannung an $C_2$; außerdem (b) die Ausgangsspannung, wenn eine ideale Stromquelle von 1 mA den Knoten zwischen $R_1$, $C_1$ und $R_2$ speist und Spannungsquelle und $R_1$ entfallen.

**Rechnung:** (a) Matrixgleichung in kΩ und mA:

$$\begin{pmatrix} 1 - j & j \\ j & 1 - 2j \end{pmatrix} \begin{pmatrix} \underline I_\mathrm{I} \\ \underline I_\mathrm{II} \end{pmatrix} = \begin{pmatrix} 1\ \mathrm V \\ 0 \end{pmatrix}$$

Die zweite Zeile nach $\underline I_\mathrm{I}$ aufgelöst:

$$\underline I_\mathrm{I} = \frac{1 - 2j}{-j}\,\underline I_\mathrm{II} = (2 + j)\,\underline I_\mathrm{II}$$

In die erste Zeile eingesetzt:

$$\big[(1 - j)(2 + j) + j\big]\,\underline I_\mathrm{II} = 3\,\underline I_\mathrm{II} = 1\ \mathrm V \quad\Rightarrow\quad \underline I_\mathrm{II} = 0{,}333\ \mathrm{mA}, \qquad \underline I_\mathrm{I} = (0{,}667 + 0{,}333\,j)\ \mathrm{mA}$$

Ausgangsspannung:

$$\underline U_2 = \underline Z_C\,\underline I_\mathrm{II} = -j\cdot 1\ \mathrm{k\Omega}\cdot 0{,}333\ \mathrm{mA} = -0{,}333\,j\ \mathrm V$$

(b) Die ideale Stromquelle liegt nur in Masche I, also ist $\underline I_\mathrm{I}$ = 1 mA bekannt; es bleibt die Gleichung von Masche II:

$$-\underline Z_C \cdot 1\ \mathrm{mA} + (R_2 + 2\,\underline Z_C)\,\underline I_\mathrm{II} = 0$$

$$\underline I_\mathrm{II} = \frac{-j}{1 - 2j}\ \mathrm{mA} = (0{,}4 - 0{,}2\,j)\ \mathrm{mA}$$

$$\underline U_2 = -j\cdot 1\ \mathrm{k\Omega}\cdot(0{,}4 - 0{,}2\,j)\ \mathrm{mA} = (-0{,}2 - 0{,}4\,j)\ \mathrm V$$

**Ergebnis:** **(a) $\underline U_2$ = −j·0,333 V: ein Drittel der Amplitude, 90° nacheilend; (b) 0,447 V bei −116,6°.**

**Einordnung:** Bei der Frequenz, bei der Kondensator und Widerstand gleich hochohmig sind, teilt der zweistufige Tiefpass die Amplitude durch drei und dreht die Phase um eine Viertelperiode. In (b) ersetzt die ideale Stromquelle eine Gleichung: Ihr Strom ist ein bekannter Maschenstrom, und ihre Spannung, (0,2 − 0,6 j) V, folgt erst nachträglich.
::::

:::frage
„Ist ein Maschenstrom ein echter Strom, den man messen kann?“
Nur dort, wo er allein fließt. Ein Maschenstrom ist eine Rechengröße; gemessen werden Zweigströme. Im Tiefpass führen $R_1$ den Strom $\underline I_\mathrm{I}$, 0,745 mA bei +26,6°, und $R_2$ den Strom $\underline I_\mathrm{II}$, 0,333 mA bei 0°; durch $C_1$ fließt aber die Differenz, 0,471 mA bei +45°, und kein Messgerät zeigt dort einen der beiden Maschenströme an.
:::

:::fehlvorstellung
„Ideale Stromquellen muss man vor der Maschenanalyse in Spannungsquellen umwandeln.“ Das liegt nahe, weil die Regel für reale Stromquellen gilt, die man mit ihrem Innenleitwert umwandeln kann. Eine ideale Stromquelle hat keinen Innenleitwert, eine gleichwertige Spannungsquelle hätte eine unendliche Spannung. Man legt die Maschen deshalb so, dass nur ein Maschenstrom durch die Stromquelle fließt; er ist dann gleich ihrem Strom, und eine Gleichung entfällt. Im Tiefpass mit idealer Stromquelle von 1 mA bleibt so eine einzige Gleichung, und die Ausgangsspannung ist 0,447 V bei −116,6°.
:::

## Die Knotenpotentialanalyse

*Warum genügen k − 1 Gleichungen, und wie stellt man sie auf, ohne zuerst alle Zweigspannungen anzusetzen?*

Wandelt man im Tiefpass die Quelle mit $R_1$ in eine Stromquelle um, bleiben drei Knoten: zwei Unbekannte und ein Bezugsknoten.

:::grafik
Szene: st1/netzwerkanalyse/02-knotenpotentiale · Vorlage: schaltbild-matrix
**Abbildung 8:** Derselbe Tiefpass, nachdem Quelle und $R_1$ in eine Stromquelle von 1 mA mit 1 mS parallel umgewandelt sind. Knoten 1 liegt zwischen $R_1$, $C_1$ und $R_2$, Knoten 2 am Ausgang, der Bezugsknoten ist Masse; die Kondensatoren haben die Admittanz j·1 mS. Daneben die Matrixgleichung mit der Leitwertmatrix (2 + j, −1; −1, 1 + j) mS und das Ergebnis (1 − j)/3 V und −j/3 V. Zwei Knotenpotentiale beschreiben alle Spannungen; die Maschenregel ist von selbst erfüllt.
:::

**Die Akteure:**

- __Bezugsknoten__: ein beliebig gewählter Knoten mit dem Potential null, meist Masse.
- __$\underline U_1, \ldots, \underline U_{n_K}$__: __Knotenpotentiale__, die Spannungen der übrigen Knoten gegen den Bezugsknoten; in V. Im Tiefpass $\underline U_1$ und $\underline U_2$.
- __$\mathbf Y$__: __Leitwertmatrix__ (Admittanzmatrix) mit den Einträgen $\underline Y_{\mu\nu}$, Zeile μ für die Knotengleichung von μ, Spalte ν für das Potential von ν; in S.
- __$\underline I_{q\mu}$__: Summe der Quellenströme, die in den Knoten μ hineinfließen; in A. Im Tiefpass 1 mA in Knoten 1.
- __$G_1$__, __$G_2$__: Leitwerte von $R_1$ und $R_2$, je 1 mS.

**Das Zusammenspiel:**

**Schritt 1**: Man wählt den Bezugsknoten und nimmt die Potentiale der übrigen Knoten als Unbekannte. Jede Zweigspannung ist die Differenz zweier Knotenpotentiale; in jedem Umlauf heben sich diese Differenzen auf, weil man zum Ausgangsknoten zurückkehrt. Damit ist jede Maschenregel von selbst erfüllt.

**Schritt 2**: Der Strom durch eine Admittanz zwischen den Knoten μ und ν ist die Admittanz mal der Potentialdifferenz.

**Schritt 3**: Für jeden Knoten außer dem Bezugsknoten gilt die Knotenregel: Die Ströme, die über Admittanzen abfließen, sind zusammen gleich den Quellenströmen, die hineinfließen.

**Schritt 4**: Ordnet man nach den Potentialen, steht auf der Diagonalen die Summe aller Admittanzen am Knoten, auch derer zum Bezugsknoten. Außerhalb steht das Negative der Admittanz zwischen zwei Knoten, null, wenn keine Admittanz sie verbindet. Rechts stehen die hineinfließenden Quellenströme.

**Schritt 5**: Man löst die $k - 1$ Gleichungen; Zweigspannungen sind Potentialdifferenzen, Zweigströme folgen aus den Zweiggleichungen.

:::formel Satz
$$\begin{pmatrix} \underline Y_{11} & \cdots & \underline Y_{1,n_K} \\ \vdots & \ddots & \vdots \\ \underline Y_{n_K,1} & \cdots & \underline Y_{n_K,n_K} \end{pmatrix} \begin{pmatrix} \underline U_{1} \\ \vdots \\ \underline U_{n_K} \end{pmatrix} = \begin{pmatrix} \underline I_{q1} \\ \vdots \\ \underline I_{q,n_K} \end{pmatrix}$$
:::

**So liest man das:** Das Potential eines Knotens wird mit allen Admittanzen an ihm multipliziert, das eines Nachbarn nur mit der verbindenden Admittanz, und zwar negativ, weil ein höheres Nachbarpotential Strom in den Knoten hineintreibt statt hinaus; die Zahl der Zeilen ist $n_K$. Ohne gesteuerte Quellen ist die Matrix symmetrisch. Für den Tiefpass:

$$\begin{pmatrix} G_1 + G_2 + j\omega C_1 & -G_2 \\ -G_2 & G_2 + j\omega C_2 \end{pmatrix} \begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix} = \begin{pmatrix} \underline I_q \\ 0 \end{pmatrix}$$

**Kurz gesagt:** Knotenpotentiale erfüllen die Maschenregel von selbst; deshalb genügen die $k - 1$ Knotengleichungen, solange jeder Zweig eine Admittanz oder eine Stromquelle ist.

:::analogie
Knotenpotentiale verhalten sich wie Höhenangaben im Gelände. Wer eine Runde läuft und zum Ausgangspunkt zurückkehrt, steht am Ende auf derselben Höhe wie am Anfang, gleich welchen Weg er nimmt; ebenso ist die Summe der Potentialdifferenzen in jedem Umlauf null, sobald jede Spannung als Differenz zweier Potentiale geschrieben ist.

| Im Vergleich | In der Schaltung |
|---|---|
| Höhe eines Punkts über dem Meer | Knotenpotential gegen den Bezugsknoten |
| Meeresspiegel | Bezugsknoten |
| Höhenunterschied eines Wegstücks | Zweigspannung |
| Runde zum Ausgangspunkt | Masche |

**Wo der Vergleich nicht stimmt:** Höhen sind reell und ändern sich nicht von selbst; Knotenpotentiale sind bei Wechselgrößen komplexe Zeiger mit Phase. Und Höhen erklären nicht, wie viel Strom fließt; dafür braucht es die Admittanzen.
:::

Idee der Herleitung: Man drückt jeden Zweigstrom durch Potentialdifferenzen aus, setzt in die Knotenregel ein und ordnet nach den Potentialen.

:::herleitung
**Ausgangspunkt:** die Knotenregel für Zeiger und die Zweiggleichung $\underline I = \underline Y\,\underline U$ jeder Admittanz.

**Annahmen:** (i) Die Zweige enthalten nur Admittanzen und unabhängige Stromquellen; reale Spannungsquellen sind vorher in Stromquellen umgewandelt. (ii) Keine Admittanz ist unendlich.

**Schritt 1**: Jede Zweigspannung ist eine Differenz von Knotenpotentialen, das Potential des Bezugsknotens ist null:

$$\underline U_\mathrm{Zweig} = \underline U_\mu - \underline U_\nu$$

**Schritt 2** (entscheidender Schritt): Die Maschenregel ist damit erfüllt, ohne dass man sie aufstellt: In einem Umlauf über die Knoten μ₁, μ₂, …, zurück zu μ₁ hebt sich jedes Potential einmal positiv und einmal negativ auf.

$$(\underline U_{\mu_1} - \underline U_{\mu_2}) + (\underline U_{\mu_2} - \underline U_{\mu_3}) + \cdots + (\underline U_{\mu_r} - \underline U_{\mu_1}) = 0$$

**Schritt 3**: Knotenregel für Knoten μ: Über jede Admittanz, die μ mit einem Knoten ν verbindet, fließt der Strom $\underline Y(\underline U_\mu - \underline U_\nu)$ ab; zusammen sind sie gleich den hineinfließenden Quellenströmen:

$$\sum_{\nu} \underline Y_{\text{zwischen }\mu, \nu}\,(\underline U_\mu - \underline U_\nu) = \underline I_{q\mu}$$

**Schritt 4**: Nach Potentialen geordnet; Admittanzen zum Bezugsknoten tragen nur zur Diagonalen bei, weil dessen Potential null ist:

$$\underline Y_{\mu\mu} = \sum_{\text{Admittanzen an }\mu} \underline Y$$

$$\underline Y_{\mu\nu} = -\,\underline Y_{\text{zwischen }\mu, \nu}$$

**Ergebnis:** die Matrixgleichung oben.

**Woher die Faktoren kommen:** Jede Admittanz am Knoten trägt sein eigenes Potential positiv bei, das des anderen Endes negativ; dieselbe Admittanz steht in der Gleichung des anderen Knotens wieder negativ, daher die Symmetrie.

**Proben:** Ein Knoten mit einer Stromquelle und einem Leitwert gegen Masse ergibt $G\,\underline U = \underline I_q$, das Ohmsche Gesetz. Tiefpass: Diagonale 2 + j bzw. 1 + j in mS, Nebeneintrag −1 mS für $G_2$.

**Grenzen:** Ein Widerstand null oder eine ideale Spule bei ω = 0 hätte eine unendliche Admittanz; dann fasst man die beiden Knoten zu einem zusammen. Ideale Spannungsquellen lassen sich nicht umwandeln (Frage unten); gesteuerte Stromquellen fügen Einträge hinzu, die die Symmetrie im Allgemeinen brechen (Abschnitt *Gesteuerte Quellen in der Knotengleichung*).
:::

::::beispiel Zweistufiger RC-Tiefpass mit Knotenpotentialen
**Gegeben:** wie in der Maschenanalyse; die Quelle 1 V mit $R_1$ = 1 kΩ umgewandelt in $\underline I_q$ = 1 mA mit $G_1$ = 1 mS; $G_2$ = 1 mS; $j\omega C$ = j·1 mS.

**Gesucht:** die Knotenpotentiale und der Strom durch $R_1$ in der ursprünglichen Schaltung.

**Rechnung:** Matrixgleichung in mS, mA und V:

$$\begin{pmatrix} 2 + j & -1 \\ -1 & 1 + j \end{pmatrix} \begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

Die zweite Zeile ergibt das Verhältnis der Potentiale, die erste dann den Ausgang:

$$\underline U_1 = (1 + j)\,\underline U_2, \qquad \big[(2 + j)(1 + j) - 1\big]\,\underline U_2 = 3j\,\underline U_2 = 1$$

$$\underline U_2 = \frac{1}{3j}\ \mathrm V = -0{,}333\,j\ \mathrm V, \qquad \underline U_1 = (0{,}333 - 0{,}333\,j)\ \mathrm V$$

Strom durch $R_1$, aus der ursprünglichen Schaltung mit der Spannungsquelle:

$$\underline I_{R1} = \frac{\underline U_q - \underline U_1}{R_1} = \frac{(1 - 0{,}333 + 0{,}333\,j)\ \mathrm V}{1\ \mathrm{k\Omega}} = (0{,}667 + 0{,}333\,j)\ \mathrm{mA}$$

**Ergebnis:** **$\underline U_2$ = −j·0,333 V und $\underline U_1$ = 0,471 V bei −45°, wie mit den Maschenströmen; der Strom durch $R_1$ ist $\underline I_\mathrm{I}$.**

**Einordnung:** Beide Verfahren liefern dieselben Zeiger. Den Strom durch $R_1$ darf man nicht in der umgewandelten Schaltung ablesen: Dort führt der Leitwert $G_1$ den Strom $G_1\underline U_1$, 0,471 mA bei −45°; die Ersatzquelle ist nur nach außen gleichwertig.

**Variation:** Mit gleichen, aber beliebigen Bauteilwerten, $R_1$ = $R_2$ = $R$ mit $G$ = 1/$R$ und $C_1$ = $C_2$ = $C$, und dem Quellenstrom $G\,\underline U_q$ liefert dieselbe Elimination zuerst die Klammer vor $\underline U_2$ und dann das Verhältnis von Ausgang zu Eingang als Funktion der Frequenz:

$$\frac{(2G + j\omega C)(G + j\omega C)}{G} - G = \frac{G^2 - \omega^2 C^2 + 3j\,\omega C\,G}{G}$$

$$\frac{\underline U_2}{\underline U_q} = \frac{G^2}{G^2 - \omega^2 C^2 + 3j\,\omega C\,G} = \frac{1}{1 - (\omega R C)^2 + 3j\,\omega R C}$$

Bei 10³ 1/s sind es 0,967 bei −16,9°, bei 10⁵ 1/s nur 0,0097 bei −163,1°: Der Tiefpass lässt tiefe Frequenzen fast ungeschwächt durch.
::::

:::grafik
Szene: st1/netzwerkanalyse/02-zeigerbild · Vorlage: zeigerdiagramm
**Abbildung 9:** Zeiger des Tiefpasses in der komplexen Ebene. Links die Spannungen: Quelle 1 V bei 0°, Knoten 1 0,471 V bei −45°, Ausgang 0,333 V bei −90°, dazu der Spannungsabfall an $R_1$ als Differenz. Rechts die Ströme: $\underline I_\mathrm{I}$ 0,745 mA bei +26,6°, $\underline I_\mathrm{II}$ 0,333 mA bei 0° und ihre Differenz, der Strom durch $C_1$, 0,471 mA bei +45°. Beide Verfahren liefern dieselben Zeiger; bei ω = 1/(RC) eilt der Ausgang dem Eingang um 90° nach und hat ein Drittel der Amplitude.
:::

Abbildung 9 zeigt die Ergebnisse beider Verfahren als Zeiger. Links ist die Quellenspannung die Summe aus dem Spannungsabfall an $R_1$ und dem Potential von Knoten 1; rechts ist der Strom durch $C_1$ die Differenz der Maschenströme. Jede Spannung des Tiefpasses lässt sich so aus den beiden Knotenpotentialen ablesen, jeder Strom aus den beiden Maschenströmen.

:::frage
„Was macht man in der Knotenanalyse mit einer idealen Spannungsquelle?“
Liegt sie zwischen einem Knoten und dem Bezugsknoten, legt sie das Potential dieses Knotens fest; es ist keine Unbekannte mehr, und seine Gleichung entfällt. Hätte die Verstärkerstufe eine ideale Signalquelle ohne Innenwiderstand, wäre das Gate-Potential als 10 mV bekannt, und es blieben zwei Gleichungen für Drain und Source. Liegt die Quelle zwischen zwei anderen Knoten, braucht man einen Zusatz: Die modifizierte Knotenanalyse nimmt ihren Strom als weitere Unbekannte auf; sie ist das folgende Thema.
:::

### Gesteuerte Quellen in der Knotengleichung

*Wo steht eine gesteuerte Stromquelle in der Leitwertmatrix, und was folgt daraus?*

Eine spannungsgesteuerte Stromquelle zwischen den Knoten a und b, gesteuert von der Spannung zwischen den Knoten c und d, führt einen Strom von a nach b, der dieser Spannung proportional ist. Weil er von Knotenpotentialen abhängt, gehört er in die Matrix statt auf die rechte Seite.

:::grafik
Szene: st1/netzwerkanalyse/02-gesteuerte-quelle-matrix · Vorlage: schaltbild-matrix
**Abbildung 10:** Das Kleinsignal-Ersatzschaltbild der Verstärkerstufe neben seiner Leitwertmatrix in mS, Zeilen und Spalten G, D und S: (0,1; 0; 0), (1; 0,225; −1,025), (−1; −0,025; 2,025). Blau die Einträge der passiven Leitwerte, die symmetrisch stehen; orange die vier Anteile der gesteuerten Quelle, ±1 mS in den Zeilen D und S und den Spalten G und S. Eine gesteuerte Quelle steht in den Zeilen der Knoten, zwischen denen ihr Strom fließt, und in den Spalten der Knoten, deren Spannung sie steuert; deshalb ist die Matrix nicht mehr symmetrisch.
:::

**Die Akteure:**

- __a__, __b__: die Knoten, zwischen denen die gesteuerte Quelle ihren Strom treibt, von a nach b; in der Verstärkerstufe D und S.
- __c__, __d__: die Knoten der Steuerspannung; in der Verstärkerstufe G und S.
- __$G_\mathrm{sig}$__, __$\underline I_\mathrm{sig}$__: Innenleitwert und Quellenstrom der umgewandelten Signalquelle, 0,1 mS und 1 µA; __$G_D$__, __$G_L$__, __$G_S$__: Leitwerte von $R_D$, $R_L$ und $R_S$, 0,1 mS, 0,1 mS und 1 mS.

:::formel Definition
$$\underline I_{a \to b} = g_m\,(\underline U_c - \underline U_d)$$
:::

Man definiert die gesteuerte Quelle über Knotenpotentiale, weil die Steuerspannung als deren Differenz sofort in die Knotengleichungen passt.

**Das Zusammenspiel:** In der Knotengleichung von a fließt der gesteuerte Strom ab, in der von b fließt er zu. Auf die linke Seite gebracht, ergibt das vier Einträge: $+g_m$ in Zeile a, Spalte c; $-g_m$ in Zeile a, Spalte d; $-g_m$ in Zeile b, Spalte c; $+g_m$ in Zeile b, Spalte d. In Abbildung 10 sind das die orangefarbenen Einträge. Die Zeile von c, dem Gate, bekommt nichts, denn dort fließt kein Strom der Quelle; deshalb steht +1 mS in Zeile D, Spalte G, aber null in Zeile G, Spalte D. Für die Verstärkerstufe lauten die Gleichungen von Drain und Source:

$$g_m\,\underline U_G + (G_D + G_L + g_o)\,\underline U_D - (g_m + g_o)\,\underline U_S = 0$$

$$-g_m\,\underline U_G - g_o\,\underline U_D + (G_S + g_m + g_o)\,\underline U_S = 0$$

**Kurz gesagt:** Ohne gesteuerte Quellen ist die Leitwertmatrix symmetrisch, weil jede Admittanz zwischen zwei Knoten in beiden Knotengleichungen gleich vorkommt; eine einzelne gesteuerte Stromquelle, deren Steuerspannung an anderen Knoten liegt als ihr Strom, steht nur in den Zeilen ihrer Stromknoten und macht die Matrix unsymmetrisch.

::::beispiel Verstärkerstufe mit Knotenpotentialen
**Gegeben:** das Kleinsignal-Ersatzschaltbild aus Abbildung 1 mit Last: Signalquelle 10 mV mit 10 kΩ, umgewandelt in 1 µA mit $G_\mathrm{sig}$ = 0,1 mS; $g_m$ = 1 mS, $g_o$ = 25 µS, $G_D$ = $G_L$ = 0,1 mS, $G_S$ = 1 mS.

**Gesucht:** die drei Knotenpotentiale und die Verstärkung.

**Rechnung:** Matrixgleichung in mS, mV und µA:

$$\begin{pmatrix} 0{,}1 & 0 & 0 \\ 1 & 0{,}225 & -1{,}025 \\ -1 & -0{,}025 & 2{,}025 \end{pmatrix} \begin{pmatrix} \underline U_G \\ \underline U_D \\ \underline U_S \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$

Die erste Zeile ergibt $\underline U_G$ = 10 mV. Die Summe der Zeilen D und S enthält $g_m$ nicht mehr, denn der gesteuerte Strom fließt von D nach S und verlässt die beiden Knoten zusammen nicht:

$$0{,}2\,\underline U_D + 1\cdot\underline U_S = 0 \quad\Rightarrow\quad \underline U_S = -0{,}2\,\underline U_D$$

In die Zeile S eingesetzt:

$$-10 - 0{,}025\,\underline U_D - 2{,}025\cdot 0{,}2\,\underline U_D = 0$$

$$\underline U_D = -\frac{10}{0{,}43}\ \mathrm{mV} = -23{,}26\ \mathrm{mV}, \qquad \underline U_S = 4{,}65\ \mathrm{mV}$$

**Ergebnis:** **10 mV, −23,26 mV und 4,65 mV; Verstärkung −2,33, wie über die Ersatzquelle.**

**Einordnung:** Die Matrix ist unsymmetrisch: +1 mS in Zeile D, Spalte G, aber 0 in Zeile G, Spalte D. Das ist kein Rechenfehler, sondern die Verstärkung selbst: Das Gate steuert den Drain, der Drain wirkt nicht auf das Gate zurück. Ohne Source-Widerstand wären es −4,44: Der Source-Widerstand halbiert ungefähr die Verstärkung und macht dafür den Ausgang des Transistors hochohmiger, wie im Abschnitt zur Innenimpedanz gezeigt.
::::

:::fehlvorstellung
„Die Leitwertmatrix muss symmetrisch sein; ist sie es nicht, habe ich mich verrechnet.“ Das liegt nahe, weil die Symmetrie in Netzen aus Widerständen, Kondensatoren und Spulen eine bewährte Probe ist. Sicher gilt sie aber nur ohne gesteuerte Quellen. Eine gesteuerte Quelle steht in den Zeilen ihrer Stromknoten und den Spalten ihrer Steuerknoten; in der Verstärkerstufe steht +1 mS in Zeile D, Spalte G und 0 in Zeile G, Spalte D. Als Probe bleibt: Die passiven Anteile allein müssen symmetrisch sein.
:::

:::vertiefung
**Warum Netze aus Widerständen, Spulen und Kondensatoren in beide Richtungen gleich übertragen und Verstärker nicht.** Die Inverse der Leitwertmatrix, die Matrix, die das Gleichungssystem nach den Potentialen auflöst, gibt an, welche Spannung an Knoten μ entsteht, wenn man in Knoten ν einen Strom einspeist. Ist die Matrix symmetrisch, ist es auch ihre Inverse: Ein Strom in Knoten 1 erzeugt an Knoten 2 dieselbe Spannung wie derselbe Strom in Knoten 2 an Knoten 1. Diese Eigenschaft heißt __Reziprozität__. Im Tiefpass sind beide Übertragungsimpedanzen −j·333 Ω. In der Verstärkerstufe dagegen erzeugt 1 µA in das Gate −23,26 mV am Drain, 1 µA in den Drain aber null Volt am Gate. Die gesteuerte Quelle der Verstärkerstufe überträgt nur in eine Richtung, vom Gate zum Drain, und hebt damit die Reziprozität auf.
:::

## Knoten oder Maschen?

*Welches Verfahren braucht weniger Gleichungen, und warum rechnen Schaltungssimulatoren mit Knotenpotentialen?*

Die Knotenanalyse braucht $k - 1$ Gleichungen, die Maschenanalyse $z - k + 1$; die kleinere Zahl entscheidet. Bei vielen parallelen Zweigen zwischen wenigen Knoten gewinnt die Knotenanalyse, bei langen Reihenschaltungen mit vielen Knoten die Maschenanalyse:

| Netz | $k$ | $z$ | Knoten | Maschen |
|---|---|---|---|---|
| RC-Tiefpass | 3 | 4 | 2 | 2 |
| Verstärker | 4 | 6 | 3 | 3 |
| Brücke | 4 | 6 | 3 | 3 |
| 3 Quellen parallel | 2 | 4 | 1 | 3 |

Der Tiefpass ist hier mit zusammengefasster realer Quelle gezählt, die Brücke mit ihrer Quelle als sechstem Zweig, und die drei Quellen parallel speisen eine gemeinsame Last.

Neben der Zahl zählt die Art der Quellen. Unabhängige und spannungsgesteuerte Stromquellen passen ohne Umweg in die Knotengleichung, unabhängige und stromgesteuerte Spannungsquellen in die Maschengleichung. Weil Transistoren im Kleinsignalbild gesteuerte Stromquellen sind, ist die Knotenanalyse das passende Verfahren für Transistorschaltungen.

::::beispiel Drei Quellen parallel an einer Last
**Gegeben:** drei reale Spannungsquellen mit 12 V, 11 V und 10 V und den Innenwiderständen 1 Ω, 2 Ω und 4 Ω, parallel an einer Last von 10 Ω; Gleichgrößen.

**Gesucht:** die Spannung an der Last.

**Rechnung:** Zwei Knoten, also eine Knotengleichung. Umgewandelt sind die Quellen 12 A mit 1 S, 5,5 A mit 0,5 S und 2,5 A mit 0,25 S; dazu die Last mit 0,1 S:

$$(1 + 0{,}5 + 0{,}25 + 0{,}1)\ \mathrm S\cdot U = (12 + 5{,}5 + 2{,}5)\ \mathrm A$$

$$U = \frac{20\ \mathrm A}{1{,}85\ \mathrm S} = 10{,}81\ \mathrm V$$

**Ergebnis:** **10,81 V, mit einer einzigen Gleichung.**

**Einordnung:** Die Maschenanalyse bräuchte drei Gleichungen für drei Maschenströme. Die Spannung liegt unter der höchsten Quellenspannung und über der niedrigsten: Die 10-V-Quelle nimmt Strom auf, statt ihn zu liefern, denn an ihr liegen 0,81 V mehr als ihre Quellenspannung.
::::

:::frage
„Warum rechnen Schaltungssimulatoren mit Knotenpotentialen und nicht mit Maschenströmen?“
Erstens liefert die __Netzliste__, die Beschreibung einer Schaltung als Liste ihrer Bauteile mit deren Knoten, die Knoten unmittelbar: Jedes Bauteil nennt die Knoten, an denen es hängt, während Maschen erst über einen Baum gesucht werden müssten. Zweitens trägt jedes Bauteil nur zu den Zeilen und Spalten seiner eigenen Knoten bei; die Matrix lässt sich Bauteil für Bauteil füllen. Drittens sind die Modelle von Transistoren gesteuerte Stromquellen, die ohne Umweg hineinpassen. Und viertens sind Knotenpotentiale das, was man misst: Spannungen gegen Masse. Was fehlt, ideale und gesteuerte Spannungsquellen, ergänzt die modifizierte Knotenanalyse.
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Linearität | jede Antwort hängt linear von den unabhängigen Quellen ab |
| Impedanzen | Ableitungen werden für Sinusgrößen zu Faktoren; Spule und Kondensator werden lineare Zweipole wie Widerstände |
| gesteuerte Quellen | lineare Bauelemente, aber keine Anregung; sie bleiben beim Abschalten aktiv |
| Ersatzquelle | Linearität an zwei Klemmen: eine Gerade, zwei Zahlen |
| Maschenströme | Unbekannte, die die Knotenregel von selbst erfüllen |
| Knotenpotentiale | Unbekannte, die die Maschenregel von selbst erfüllen |
| unsymmetrische Leitwertmatrix | gesteuerte Quellen übertragen nur in eine Richtung |
| Verfahrenswahl | die kleinere der beiden Gleichungszahlen |

In einer linearen Schaltung hängt jede Spannung und jeder Strom linear von den unabhängigen Quellen ab; deshalb verhält sich die Schaltung an zwei Klemmen wie eine einzige Quelle mit Innenimpedanz, und ihr Gleichungssystem wird klein, wenn man als Unbekannte Knotenpotentiale oder Maschenströme wählt, weil diese eine der beiden Kirchhoffschen Regeln schon von selbst erfüllen.

## Bedeutung und Ausblick

Jede Kleinsignalrechnung an Transistorstufen benutzt diese Werkzeuge: Die Knotenanalyse liefert die Verstärkung, die Ersatzquelle den Ausgangswiderstand, mit dem man abschätzt, wie stark die nächste Stufe belastet. Am Labortisch bestimmt man die Ersatzquelle eines Ausgangs aus zwei Messungen mit verschiedenen Lasten, wie es [Ersatzquellen – Thévenin und Norton](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html) für Gleichspannungsquellen zeigt; einen Verstärkerausgang für den Kurzschlussstrom kurzzuschließen, ist riskant, weil die Stufe dabei leicht ihren linearen Bereich verlässt.

Die Verfahren haben Grenzen. Ideale Spannungsquellen zwischen zwei Knoten, von denen keiner der Bezugsknoten ist, und gesteuerte Quellen anderer Art passen nicht in die reine Knotenanalyse; die modifizierte Knotenanalyse, das folgende Thema, nimmt dafür zusätzliche Ströme als Unbekannte auf und stellt die Gleichungen systematisch Bauteil für Bauteil auf. Große Signale verlassen den linearen Bereich ([Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html)), und Einschaltvorgänge brauchen eine Rechnung im Zeitbereich statt der Zeiger.

:::kern
- Linear heißt: Die Antwort auf die Summe zweier Anregungen ist die Summe der Antworten, die auf das Vielfache einer Anregung das Vielfache der Antwort. Widerstände, Spulen, Kondensatoren und gesteuerte Quellen sind linear; unabhängige Quellen sind die Anregung.
- Für Sinusgrößen einer Frequenz im eingeschwungenen Zustand gelten Kirchhoff und Ohm für Zeiger, mit den Impedanzen $j\omega L$ und $1/(j\omega C)$.
- Eine zusammenhängende Schaltung mit $k$ Knoten und $z$ Zweigen hat $k - 1$ unabhängige Knoten- und $z - k + 1$ unabhängige Maschengleichungen.
- Ersatzquelle: $\underline U_{AB} = \underline U_{LL} - \underline Z_i\,\underline I_A$; die Stromform hat $\underline I_{KS}$ und $\underline Y_i$.
- Innenimpedanz aus Leerlaufspannung und Kurzschlussstrom oder mit Testquelle; abgeschaltet werden nur unabhängige Quellen, gesteuerte bleiben aktiv.
- Maschenanalyse: Diagonale Summe der Maschenimpedanzen, außerhalb die gemeinsamen Impedanzen mit Vorzeichen nach der Richtung, rechts die antreibenden Quellenspannungen.
- Knotenanalyse: Diagonale Summe der Admittanzen am Knoten, außerhalb − verbindende Admittanz, rechts die hineinfließenden Quellenströme; gesteuerte Stromquellen machen die Matrix im Allgemeinen unsymmetrisch.
- Man wählt das Verfahren mit weniger Gleichungen; Simulatoren nutzen Knotenpotentiale.
:::

:::quiz
F: Warum genügen zwei Zahlen, um ein lineares Netz an zwei Klemmen von außen zu beschreiben?
A: Ersetzt man die Last durch eine Stromquelle, ist die Klemmenspannung nach der Linearität die Summe aus dem Beitrag der inneren Quellen, der Leerlaufspannung, und einem Beitrag proportional zum Klemmenstrom, minus Innenimpedanz mal Strom. Eine Gerade ist durch diese zwei Zahlen festgelegt.
F: Stimmt es, dass man für die Innenimpedanz alle Quellen auf null setzt?
A: Nein. Abgeschaltet werden nur die unabhängigen Quellen; gesteuerte Quellen beschreiben Bauelemente des Netzes und bleiben aktiv. In der Verstärkerstufe ergibt das 8,90 kΩ statt fälschlich 8,04 kΩ.
F: Warum braucht die Maschenanalyse keine Knotengleichungen?
A: Jeder Maschenstrom fließt in jeden Knoten seines Umlaufs hinein und wieder heraus und trägt zur Bilanz des Knotens null bei; die Knotenregel ist deshalb von selbst erfüllt.
F: Warum braucht die Knotenanalyse keine Maschengleichungen?
A: Jede Zweigspannung ist eine Differenz von Knotenpotentialen; in einem Umlauf heben sich alle Potentiale auf, weil man zum Ausgangsknoten zurückkehrt. Die Maschenregel ist damit von selbst erfüllt.
F: Stimmt es, dass die Leitwertmatrix immer symmetrisch ist?
A: Nein. Sicher symmetrisch ist sie nur ohne gesteuerte Quellen; die gesteuerte Quelle der Verstärkerstufe steht in Zeile D, Spalte G mit +1 mS, in Zeile G, Spalte D steht null.
F: Warum macht der Source-Widerstand den Ausgang des Transistors hochohmiger?
A: Ein Strom in den Drain hebt über $R_S$ das Source-Potential an; bei festem Gate wird die Gate-Source-Spannung negativ, und die gesteuerte Quelle zieht weniger Strom. Diese Gegenkopplung macht aus den 41 kΩ des Zweigs aus Transistor und $R_S$ 81 kΩ.
F: Stimmt es, dass man ideale Stromquellen vor der Maschenanalyse in Spannungsquellen umwandeln muss?
A: Nein, das geht gar nicht, die Spannungsform hätte eine unendliche Spannung. Man legt die Maschen so, dass nur ein Maschenstrom durch die Stromquelle fließt; er ist dann bekannt, und eine Gleichung entfällt.
F: Wie groß ist die Impedanz eines Kondensators von 100 nF bei ω = 10⁴ 1/s?
A: $1/(j\omega C)$ = 1/(j · 10⁴ 1/s · 10⁻⁷ F) = −j·1 kΩ, also 1 kΩ Betrag und −90° Phase.
F: Ein Netz hat zwei Knoten und vier Zweige. Wie viele Knoten- und Maschengleichungen braucht es?
A: $k - 1$ = 1 Knotengleichung und $z - k + 1$ = 3 Maschengleichungen; die Knotenanalyse ist hier deutlich kürzer.
F: Eine Ersatzquelle hat die Leerlaufspannung −43,96 mV und die Innenimpedanz 8,90 kΩ. Welche Spannung liegt an einer Last von 10 kΩ?
A: Nach dem Spannungsteiler −43,96 mV · 10 kΩ/18,90 kΩ = −23,26 mV.
:::
