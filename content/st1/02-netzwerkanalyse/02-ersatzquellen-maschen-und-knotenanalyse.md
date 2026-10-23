---
title: Ersatzquellen, Maschenstrom- und Knotenpotentialanalyse
pfad: Elektrotechnik / 3. Semester / Schaltungstechnik 1 / Netzwerkanalyse
order: 33020200
summary: Wie man lineare Schaltungen systematisch berechnet, von Wechselstromnetzen mit Spulen und Kondensatoren bis zu Kleinsignal-Ersatzschaltbildern mit gesteuerten Quellen: Ersatzquellen nach Thévenin und Norton, Maschenstrom- und Knotenpotentialanalyse. Kompakte Fassung mit hergeleiteter Linearität, Impedanz, Gleichungszahl, Ersatzquelle und den Matrixgleichungen beider Verfahren; die ausführliche enthält zusätzlich die Schaltzeichen aller Quellen, den Graph der Verstärkerstufe, ideale Stromquellen in der Maschenanalyse, das Zeigerbild, die Reziprozität und die Wahl des Verfahrens an Beispielen.
tags: Thévenin, Norton, Maschenstromanalyse, Knotenpotentialanalyse, gesteuerte Quelle
stil: 3
fassung: kompakt
---

## Worum es geht

Nach der Linearisierung im Arbeitspunkt ist jede Verstärkerschaltung für kleine Signale ein Netz aus Widerständen, Kondensatoren, Spulen und gesteuerten Quellen; die Stufe mit einem Transistor in Abbildung 1 hat bereits zwölf unbekannte Ströme und Spannungen. Zwei Werkzeuge machen solche Netze beherrschbar: Gleichungssysteme mit möglichst wenigen Unbekannten und die Ersatzquelle, die einen Schaltungsblock auf zwei Zahlen verdichtet. Beide folgen aus einem Prinzip:

**In einer linearen Schaltung hängt jede Spannung und jeder Strom linear von den unabhängigen Quellen ab; deshalb verhält sich die Schaltung an zwei Klemmen wie eine einzige Quelle mit Innenimpedanz, und ihr Gleichungssystem wird klein, wenn man als Unbekannte Knotenpotentiale oder Maschenströme wählt, weil diese eine der beiden Kirchhoffschen Regeln schon von selbst erfüllen.**

Vorausgesetzt werden die [Kirchhoffschen Gesetze](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/strome-und-spannungen-in-netzen/kirchhoffsche-gesetze.html), das Rechnen mit [Zeigern](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html) und das Kleinsignal-Ersatzschaltbild aus [Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html). Die Gleichstromfassungen der Verfahren behandeln [Ersatzquellen – Thévenin und Norton](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/analyse-linearer-netzwerke/ersatzquellen-thevenin-norton.html), [Das Maschenstromverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/maschenstromverfahren/maschenstromverfahren.html) und [Das Knotenpotentialverfahren](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/knotenpotentialverfahren/knotenpotentialverfahren.html); hier kommen Wechselgrößen und gesteuerte Quellen hinzu. Darauf bauen die modifizierte Knotenanalyse und alle Kleinsignalrechnungen an Transistorstufen auf.

:::grafik
Szene: st1/netzwerkanalyse/02-verstaerker-kleinsignal · Vorlage: schaltbild-vergleich
**Abbildung 1:** (a) Source-Schaltung mit einem n-Kanal-MOSFET im Arbeitspunkt 0,25 mA: Drainwiderstand $R_D$ = 10 kΩ an 5 V, Source-Widerstand $R_S$ = 1 kΩ, am Gate eine Signalquelle mit 10 mV Amplitude und 10 kΩ Innenwiderstand auf 1,25 V Vorspannung, am Ausgang über einen Koppelkondensator eine Last von 10 kΩ. (b) Ihr Kleinsignal-Ersatzschaltbild mit den Knoten G, D und S: Eine gesteuerte Stromquelle $g_m u_{GS}$ mit 1 mS und ein Ausgangsleitwert von 25 µS ersetzen den Transistor; Versorgung und Vorspannung werden zu Kurzschlüssen, ebenso der Koppelkondensator, dessen Impedanz bei der Signalfrequenz vernachlässigt wird. Die Zeiger der Knotenpotentiale sind 10 mV, −23,26 mV und 4,65 mV; der Drain schwingt mit 23,26 mV Amplitude gegenphasig zum Signal. (c) Vom Ausgang aus gesehen ist dieselbe Schaltung eine Quelle mit der Leerlaufspannung −43,96 mV und dem Innenwiderstand 8,90 kΩ. Eine lineare Schaltung ist durch ihre Knotenpotentiale bestimmt, und vom Ausgang aus gesehen genügen zwei Zahlen.
:::

## Lineare Schaltungen

*Was macht eine Schaltung linear, und welche Bauelemente gehören dazu?*

Bei 10 mV Signal liefert die Verstärkerstufe am Ausgang −23,26 mV, bei 20 mV genau das Doppelte, −46,51 mV. Besteht das Signal aus zwei Teilen, 10 mV und −5 mV, ist der Ausgang die Summe der Ausgänge beider Teile: −23,26 mV und +11,63 mV ergeben −11,63 mV. Das ist Linearität.

**Die Akteure:**

- __$x_1$__, __$x_2$__: zwei Anregungen, etwa Werte unabhängiger Quellen; in V oder A.
- __$y$__: eine beliebige Antwort der Schaltung, ein Strom oder eine Spannung, als Funktion der Anregung.
- __$\alpha_1$__, __$\alpha_2$__: beliebige Zahlen, bei Wechselgrößen auch komplexe.

:::formel Definition
$$y(\alpha_1 x_1 + \alpha_2 x_2) = \alpha_1\,y(x_1) + \alpha_2\,y(x_2)$$
:::

Man definiert Linearität so, weil sie das Zerlegen erlaubt: Jede Anregung darf einzeln betrachtet werden, und die Antworten addieren sich.

**Kurz gesagt:** Die Antwort einer linearen Schaltung auf die Summe zweier Anregungen ist die Summe ihrer Antworten, und die Antwort auf das Vielfache einer Anregung ist das Vielfache der Antwort.

Linear ist eine Schaltung, wenn jede Zweiggleichung Ströme und Spannungen nur über feste Faktoren und Ableitungen verknüpft: beim Widerstand die Proportionalität, bei Spule und Kondensator die Ableitung, die Summen in Summen überführt. Die Werte der __unabhängigen Quellen__, die eine vorgegebene Spannung oder einen vorgegebenen Strom liefern, unabhängig von der übrigen Schaltung, sind die Anregung. Eine __gesteuerte Quelle__ liefert eine Spannung oder einen Strom proportional zu einer Größe an anderer Stelle der Schaltung; sie ist linear, aber keine Anregung, denn ihr Wert folgt aus der Schaltung. Es gibt sie spannungs- und stromgesteuert, jeweils als Strom- oder Spannungsquelle. Im Kleinsignalbild eines MOSFET ist der Drainstrom eine spannungsgesteuerte Stromquelle: gesteuert von der Gate-Source-Spannung, mit der __Steilheit__ $g_m$ als Faktor, hier 1 mS. Parallel dazu liegt der __Ausgangsleitwert__ $g_o$, hier mit 25 µS angenommen: Er beschreibt, dass der Drainstrom auch mit der Drain-Source-Spannung leicht steigt.

:::frage
„Ist eine Schaltung mit einem Transistor überhaupt linear?“
Für große Signale nicht, denn der Drainstrom wächst mit dem Quadrat der Gate-Source-Spannung über der Schwelle. Linear ist das Kleinsignal-Ersatzschaltbild: Für kleine Änderungen um den Arbeitspunkt wird der Transistor zur gesteuerten Quelle mit der Steigung seiner Kennlinie, 1 mS in der Verstärkerstufe. Die Verfahren dieses Themas gelten für Transistorschaltungen deshalb im Kleinsignalbetrieb ([Arbeitspunkt und Linearisierung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/arbeitspunkt-und-linearisierung.html)).
:::

Idee der Herleitung: Man schreibt alle Gleichungen als eine lineare Vorschrift für die Unbekannten und zeigt, dass Summen und Vielfache von Quellen zu Summen und Vielfachen von Lösungen führen.

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

Ein Kondensator von 100 nF führt bei einer Sinusspannung von 1 V Amplitude und der Kreisfrequenz 10⁴ 1/s einen Strom von 1 mA Amplitude, eine Viertelperiode voraus; ein Widerstand von 1 kΩ führt ebenfalls 1 mA, im Takt der Spannung. Mit [Zeigern](/wissen/elektrotechnik/1-semester/mathematische-methoden-der-elektrotechnik/komplexe-zahlen-und-zeiger/zeiger-und-sinussignale.html) wird daraus eine Rechnung wie mit Widerständen: Jede Sinusgröße wird durch ihre __komplexe Amplitude__ dargestellt, mit dem Scheitelwert als Betrag und der __Nullphase__, der Phase zur Zeit null, als Winkel. Im eingeschwungenen Zustand schwingen alle Größen mit der Frequenz der Quelle, Summen werden zu Zeigersummen und Ableitungen zu Faktoren $j\omega$; Knoten- und Maschenregel gelten deshalb für Zeiger.

:::grafik
Szene: st1/netzwerkanalyse/02-impedanzen · Vorlage: kennlinie-loglog
**Abbildung 2:** Betrag der Impedanz in Ω über der Kreisfrequenz von 10² bis 10⁶ 1/s, beide Achsen logarithmisch, für einen Widerstand von 1 kΩ, eine Spule von 100 mH und einen Kondensator von 100 nF; darunter der Winkel der Impedanz: 0°, +90° und −90°. Die drei Kurven schneiden sich bei 10⁴ 1/s und 1 kΩ. Spule und Kondensator verhalten sich bei Sinusgrößen wie Widerstände, deren Betrag mit der Frequenz steigt bzw. fällt, mit +90° bzw. −90° Phasenverschiebung.
:::

**Die Akteure:**

- __$\underline U$__, __$\underline I$__: komplexe Amplituden von Spannung und Strom eines Zweigs; Betrag in V bzw. A. Unterstrichene Größen sind komplex; bei Gleichgrößen entfällt der Strich.
- __$\omega$__: Kreisfrequenz, $2\pi$ mal die Frequenz; im Beispiel 10⁴ 1/s, entsprechend der Frequenz 1,59 kHz.
- __$\underline Z$__: __Impedanz__, das Verhältnis der Zeiger von Spannung und Strom; in Ω. __$\underline Y$__: __Admittanz__, ihr Kehrwert; in S.
- __$j$__: die imaginäre Einheit, in der Elektrotechnik $j$, weil $i$ für Ströme steht.

:::formel Definition
$$\underline Z = \frac{\underline U}{\underline I}, \qquad \underline Y = \frac{1}{\underline Z}$$
:::

Man definiert die Impedanz so, weil sie die Zweiggleichung von Widerstand, Spule und Kondensator in die Form des Ohmschen Gesetzes bringt; damit gelten die Verfahren für Widerstandsnetze auch für Wechselstromnetze.

:::formel Formel
$$\underline Z_R = R, \qquad \underline Z_L = j\omega L, \qquad \underline Z_C = \frac{1}{j\omega C} = -\frac{j}{\omega C}$$
:::

**So liest man das:** Der Betrag der Spulenimpedanz wächst proportional zur Frequenz, der des Kondensators fällt umgekehrt proportional; bei 10⁴ 1/s haben 100 mH, 100 nF und 1 kΩ alle 1 kΩ (Abbildung 2). Der Faktor $j$ ist eine Drehung um 90°. Bei Gleichstrom wird die Spule zum Kurzschluss und der Kondensator zur Unterbrechung.

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

## Wie viele Gleichungen eine Schaltung bestimmen

*Wie viele unbekannte Größen hat eine Schaltung, und wie viele unabhängige Gleichungen liefern Bauelemente und Kirchhoffsche Regeln?*

**Die Akteure:**

- __Knoten__: ein Verbindungspunkt, an dem Bauelemente aneinandergrenzen, auch wenn sich der Strom dort nicht verzweigt; durch widerstandslose Leitungen verbundene Punkte bilden einen Knoten. __$k$__: ihre Zahl; 4 in der Verstärkerstufe (G, D, S, Masse).
- __Zweig__: ein Bauelement oder eine Quelle zwischen zwei Knoten; eine reale Quelle samt Innenwiderstand darf als ein Zweig zählen. __$z$__: ihre Zahl; 6 in der Verstärkerstufe.
- __Masche__: ein geschlossener Umlauf über Zweige.
- __Baum__: eine Auswahl von Zweigen, die alle Knoten verbindet, ohne einen Umlauf zu schließen; die übrigen Zweige heißen __Verbindungszweige__.
- __$n_K$__, __$n_M$__: Zahl der unabhängigen Knoten- bzw. Maschengleichungen.

**Das Zusammenspiel:** Jeder Zweig trägt zwei Unbekannte bei, Strom und Spannung, und eine Zweiggleichung. Die übrigen Gleichungen liefern die Kirchhoffschen Regeln, aber nur zum Teil unabhängig. Im Ersatzschaltbild der Verstärkerstufe (Abbildung 1b) verbindet ein Baum aus Signalquelle, $R_D$ und $R_S$ die vier Knoten; jeder der drei übrigen Zweige schließt mit Baumzweigen genau eine neue Masche.

:::formel Satz
$$n_K = k - 1, \qquad n_M = z - k + 1, \qquad z + n_K + n_M = 2z$$
:::

**So liest man das:** Mit den Zweiggleichungen sind es genau so viele Gleichungen wie Unbekannte; in der Verstärkerstufe 6 Zweig-, 3 Knoten- und 3 Maschengleichungen für 12 Unbekannte. Wer die Unbekannten geschickt wählt, braucht nur $n_K$ oder $n_M$ Gleichungen.

**Kurz gesagt:** Eine zusammenhängende Schaltung liefert genau so viele Gleichungen wie Unbekannte: je Zweig eine Zweiggleichung, je Knoten außer einem eine unabhängige Knotengleichung und je Verbindungszweig eines Baums eine unabhängige Maschengleichung.

:::frage
„Warum ist eine der Knotengleichungen überflüssig?“
Addiert man alle Knotengleichungen, kommt jeder Zweigstrom zweimal vor, einmal als zufließend und einmal als abfließend; die Summe ist null. Die Gleichung des letzten Knotens folgt deshalb aus den übrigen: In der Verstärkerstufe ergibt sich die Strombilanz der Masse aus den Bilanzen von G, D und S. Diesen Knoten wählt man als Bezugsknoten und lässt seine Gleichung weg.
:::

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

## Ersatzquellen nach Thévenin und Norton

*Warum verhält sich jedes lineare Netz an zwei Klemmen wie eine Quelle mit Innenimpedanz, und wie bestimmt man die beiden Größen?*

Offen liefert der Ausgang der Verstärkerstufe −43,96 mV, an 10 kΩ −23,26 mV, und kurzgeschlossen fließt ein Strom von −4,94 µA. Trägt man die Spannung über dem Strom auf, liegen diese drei Punkte, wie die jeder weiteren Last, auf einer Geraden; dieselbe Kennlinie hat eine Spannungsquelle mit Innenwiderstand.

:::grafik
Szene: st1/netzwerkanalyse/02-ersatzquelle-ueberlagerung · Vorlage: schaltbild-ueberlagerung
**Abbildung 3:** (a) Ein lineares Netz mit unabhängigen Quellen, einer gesteuerten Quelle und Impedanzen; die Last an den Klemmen A und B ist durch eine Stromquelle $\underline I_A$ ersetzt. (b) Nur die inneren Quellen wirken, die Klemmen sind offen: Die Klemmenspannung ist die Leerlaufspannung. (c) Die inneren unabhängigen Quellen sind null, die Spannungsquelle als Kurzschluss, die Stromquelle als Unterbrechung gezeichnet; die gesteuerte Quelle bleibt aktiv, und nur $\underline I_A$ wirkt. (d) Die beiden gleichwertigen Ersatzschaltungen mit den Werten der Verstärkerstufe: −43,96 mV in Reihe mit 8,90 kΩ bzw. −4,94 µA parallel zu 0,112 mS. Die Klemmenspannung ist die Summe zweier Beiträge, einer unabhängig vom Klemmenstrom, einer ihm proportional; deshalb beschreiben zwei Zahlen das Netz von außen vollständig.
:::

**Die Akteure:**

- __A__, __B__: die Klemmen des Netzes; in der Verstärkerstufe Drain und Masse.
- __$\underline U_{AB}$__: Klemmenspannung; __$\underline I_A$__: Klemmenstrom, der bei A aus dem Netz in die Last fließt.
- __$\underline U_{LL}$__: __Leerlaufspannung__ bei offenen Klemmen; −43,96 mV in der Verstärkerstufe bei 10 mV Signal.
- __$\underline I_{KS}$__: __Kurzschlussstrom__ bei kurzgeschlossenen Klemmen; −4,938 µA.
- __$\underline Z_i$__, __$\underline Y_i$__: __Innenimpedanz__ und Innenadmittanz, Kehrwerte voneinander; 8,90 kΩ bzw. 0,112 mS.

**Das Zusammenspiel:**

**Schritt 1**: Man ersetzt die Last durch eine Stromquelle mit demselben Strom $\underline I_A$ (Abbildung 3a); das Netz bemerkt den Tausch nicht, denn es spürt von der Last nur Strom und Spannung an den Klemmen.

**Schritt 2**: Nach der Linearität ist die Klemmenspannung die Summe zweier Antworten: auf die inneren unabhängigen Quellen und auf $\underline I_A$.

**Schritt 3**: Die inneren Quellen allein, bei offenen Klemmen, liefern die Leerlaufspannung (Abbildung 3b).

**Schritt 4**: $\underline I_A$ allein, mit abgeschalteten inneren unabhängigen Quellen, Spannungsquellen als Kurzschluss und Stromquellen als Unterbrechung, liefert eine Spannung proportional zu $\underline I_A$. Gesteuerte Quellen bleiben aktiv, denn sie gehören zum Netz und sind keine Anregung (Abbildung 3c). Die Summe ist eine Gerade.

:::formel Satz
$$\underline U_{AB} = \underline U_{LL} - \underline Z_i\,\underline I_A, \qquad \underline Z_i = \frac{\underline U_{LL}}{\underline I_{KS}}$$
:::

**So liest man das:** Die Leerlaufspannung ist der unbelastete Wert, die Innenimpedanz das Maß für den Einbruch unter Last; bei kurzgeschlossenen Klemmen fließt der Kurzschlussstrom, und die zweite Formel setzt voraus, dass er endlich und von null verschieden ist. Nach dem Klemmenstrom aufgelöst, entsteht die __Ersatzstromquelle__ nach Norton, eine Stromquelle $\underline I_{KS}$ mit der Admittanz $\underline Y_i$ parallel; die Spannungsform heißt __Ersatzspannungsquelle__ nach Thévenin (Abbildung 3d).

$$\underline I_A = \frac{\underline U_{LL} - \underline U_{AB}}{\underline Z_i} = \underline I_{KS} - \underline Y_i\,\underline U_{AB}$$

Dieselbe Umrechnung macht aus jeder realen Spannungsquelle eine reale Stromquelle, etwa aus 1 V mit 1 kΩ einen Strom von 1 mA mit 1 mS. Ideale Quellen lassen sich nicht umwandeln, ihr Kurzschlussstrom bzw. ihre Leerlaufspannung wäre unendlich.

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

### Die Innenimpedanz bei gesteuerten Quellen

*Wie bestimmt man die Innenimpedanz, wenn das Netz gesteuerte Quellen enthält?*

Leerlaufspannung durch Kurzschlussstrom liefert die Innenimpedanz immer dann, wenn beide endlich und von null verschieden sind, auch mit gesteuerten Quellen. Kürzer ist oft, die unabhängigen Quellen abzuschalten und die verbleibenden Impedanzen zusammenzufassen, aber nur ohne gesteuerte Quellen: Eine aktive gesteuerte Quelle ist im Allgemeinen keine Impedanz und darf nicht abgeschaltet werden. Mit gesteuerten Quellen schaltet man die unabhängigen Quellen ab, lässt die gesteuerten aktiv, legt eine __Testspannung__ $\underline U_T$ an die Klemmen und berechnet den Strom $\underline I_T$, der in die Klemme A hineinfließt.

$$\underline Z_i = \frac{\underline U_T}{\underline I_T}$$

Das ist Schritt 4 der Herleitung: Ohne unabhängige Quellen ist die Klemmenspannung gleich Innenimpedanz mal hineinfließendem Strom.

::::beispiel Ersatzquelle am Ausgang der Verstärkerstufe
**Gegeben:** das Kleinsignal-Ersatzschaltbild aus Abbildung 1 ohne Last: Signal 10 mV mit 10 kΩ, $g_m$ = 1 mS, $g_o$ = 25 µS, $R_D$ = 10 kΩ ($G_D$ = 0,1 mS), $R_S$ = 1 kΩ ($G_S$ = 1 mS). Das Gate nimmt keinen Strom auf, am Gate liegen deshalb die vollen 10 mV.

**Gesucht:** Leerlaufspannung, Kurzschlussstrom und Innenimpedanz, diese auch mit Testquelle; die Spannung an einer Last von 10 kΩ.

**Rechnung:** (a) Leerlauf: Der Strom der Transistorstrecke fließt von $R_D$ nach $R_S$, die Ströme durch beide sind entgegengesetzt gleich; mit der Knotenregel an D folgt, in mS, mV und µA:

$$\underline U_S = -0{,}1\,\underline U_D$$

$$0{,}1\,\underline U_D + 1\cdot(10 + 0{,}1\,\underline U_D) + 0{,}025\cdot 1{,}1\,\underline U_D = 0$$

$$\underline U_{LL} = \underline U_D = -\frac{10}{0{,}2275}\ \mathrm{mV} = -43{,}96\ \mathrm{mV}$$

(b) Kurzschluss: Der Drain liegt auf null; die Knotenregel an S liefert das Source-Potential, daraus der Strom der Transistorstrecke. Er kommt aus dem Kurzschluss und fließt in den Drain hinein; der Klemmenstrom aus D heraus ist deshalb negativ:

$$\underline U_S = \frac{g_m \cdot 10\ \mathrm{mV}}{g_m + g_o + G_S} = 4{,}938\ \mathrm{mV}$$

$$\underline I_{KS} = -\big[g_m(10\ \mathrm{mV} - \underline U_S) - g_o\,\underline U_S\big] = -4{,}938\ \mu\mathrm{A}$$

(c) Innenimpedanz:

$$\underline Z_i = \frac{-43{,}96\ \mathrm{mV}}{-4{,}938\ \mu\mathrm{A}} = 8{,}90\ \mathrm{k\Omega}$$

(d) Testquelle: Signal abgeschaltet, 1 V am Drain. Die Knotenregel an S liefert das Source-Potential; der Strom in den Drain setzt sich aus dem Strom durch $R_D$, dem gesteuerten Strom und dem Strom durch $g_o$ zusammen:

$$\underline U_S = \frac{g_o \cdot 1\ \mathrm V}{g_m + g_o + G_S} = 12{,}35\ \mathrm{mV}$$

$$\underline I_T = 100\ \mu\mathrm{A} - 12{,}3457\ \mu\mathrm{A} + 24{,}6914\ \mu\mathrm{A} = 112{,}3457\ \mu\mathrm{A}$$

$$\underline Z_i = \frac{1\ \mathrm V}{112{,}346\ \mu\mathrm{A}} = 8{,}90\ \mathrm{k\Omega}$$

Mit abgeschalteter gesteuerter Quelle lägen $g_o$ und $R_S$ in Reihe, 41 kΩ, parallel zu $R_D$: 8,04 kΩ.

(e) Last:

$$\underline U_{AB} = \underline U_{LL}\,\frac{R_L}{R_L + \underline Z_i} = -43{,}96\ \mathrm{mV}\cdot\frac{10}{18{,}90} = -23{,}26\ \mathrm{mV}$$

**Ergebnis:** **−43,96 mV, −4,938 µA und 8,90 kΩ auf beiden Wegen; an 10 kΩ −23,26 mV. Mit abgeschalteter gesteuerter Quelle falsch 8,04 kΩ.**

**Einordnung:** Der Zweig aus Transistor und $R_S$ führt je Volt 12,346 µA, das sind 81 kΩ statt 41 kΩ. Die Last senkt den Betrag der Verstärkung fast auf die Hälfte, von 4,40 auf 2,33, weil sie kaum größer ist als die Innenimpedanz; für jede andere Last genügt der Spannungsteiler.
::::

:::grafik
Szene: st1/netzwerkanalyse/02-innenwiderstand · Vorlage: schaltbild-vergleich
**Abbildung 4:** Innenimpedanz der Verstärkerstufe mit einer Testspannung am Drain; die Signalquelle ist abgeschaltet, ihr Innenwiderstand bleibt, das Gate liegt damit auf null. (a) Richtig, mit aktiver gesteuerter Quelle: Je Volt Testspannung fließen 100 µA durch $R_D$ und 12,35 µA in den Zweig aus Transistor und $R_S$, zusammen 8,90 kΩ; dieser Zweig allein hat 81 kΩ. (b) Falsch, mit entfernter gesteuerter Quelle: Der Zweig hat nur 41 kΩ, zusammen 8,04 kΩ. Gesteuerte Quellen bleiben beim Bestimmen der Innenimpedanz aktiv; der Source-Widerstand macht die Drain-Source-Strecke doppelt so hochohmig.
:::

Warum die gesteuerte Quelle den Ausgang hochohmiger macht, zeigt Abbildung 4a: Die Testspannung treibt Strom durch den Ausgangsleitwert in den Source-Knoten und hebt dessen Potential über $R_S$ an, je Volt um 12,35 mV. Bei festem Gate wird die Gate-Source-Spannung dadurch negativ, und die gesteuerte Quelle führt 12,35 µA gegen die Richtung des Teststroms; von den 24,69 µA durch $g_o$ bleibt die Hälfte. Der Source-Widerstand wirkt als __Gegenkopplung__, eine Rückwirkung, die einer Änderung des Drainstroms entgegenwirkt; wer die gesteuerte Quelle abschaltet (Abbildung 4b), unterschlägt sie.

:::fehlvorstellung
„Für die Innenimpedanz setzt man alle Quellen auf null.“ Das liegt nahe, weil die Regel in Netzen ohne gesteuerte Quellen stimmt. Abgeschaltet werden aber nur die unabhängigen Quellen, die Anregung; gesteuerte Quellen beschreiben Bauelemente wie den Transistor und bleiben aktiv. In der Verstärkerstufe ergibt die richtige Rechnung 8,90 kΩ, die falsche 8,04 kΩ; der Zweig aus Transistor und $R_S$ hat 81 kΩ statt 41 kΩ.
:::

## Die Maschenstromanalyse

*Wie kommt man mit z − k + 1 Gleichungen aus, und wie stellt man sie direkt auf?*

Der zweistufige RC-Tiefpass in Abbildung 5 hat mit der Quelle als eigenem Zweig fünf Zweige und vier Knoten, also zehn Unbekannte; zwei Maschenströme genügen.

:::grafik
Szene: st1/netzwerkanalyse/02-maschenstroeme · Vorlage: schaltbild-matrix
**Abbildung 5:** Zweistufiger RC-Tiefpass: Quelle 1 V, $R_1$ und $R_2$ je 1 kΩ, $C_1$ und $C_2$ je 100 nF gegen Masse, bei 10⁴ 1/s je −j·1 kΩ. Die Maschenströme $\underline I_\mathrm{I}$ und $\underline I_\mathrm{II}$ laufen im Uhrzeigersinn; im gemeinsamen Zweig $C_1$ fließt ihre Differenz. Daneben die Matrixgleichung mit der Impedanzmatrix (1 − j, j; j, 1 − 2j) kΩ und der rechten Seite (1 V, 0). Zwei Maschenströme beschreiben alle Zweigströme; die Knotenregel ist von selbst erfüllt.
:::

**Die Akteure:**

- __$\underline U_q$__: Quellenspannung; 1 V Amplitude, Nullphase null. __$R_1$__, __$R_2$__: je 1 kΩ; __$C_1$__, __$C_2$__: je 100 nF, mit der Impedanz __$\underline Z_C$__ von −j·1 kΩ.
- __$\underline I_1, \ldots, \underline I_{n_M}$__: __Maschenströme__, gedachte Ströme, die je eine Masche umlaufen; in A. Im Beispiel $\underline I_\mathrm{I}$ und $\underline I_\mathrm{II}$.
- __$\mathbf Z$__: __Impedanzmatrix__ mit den Einträgen $\underline Z_{\mu\nu}$; in Ω.
- __$\underline U_{q\mu}$__: Summe der Quellenspannungen, die den Maschenstrom μ antreiben; in V.

**Das Zusammenspiel:**

**Schritt 1**: Man wählt $z - k + 1$ unabhängige Maschen, in einem kreuzungsfrei gezeichneten Schaltbild etwa dessen Fenster, und gibt jeder einen Maschenstrom mit frei gewählter Richtung.

**Schritt 2**: Jeder Zweigstrom ist die Summe der Maschenströme durch den Zweig, mit Vorzeichen nach der Richtung; durch $C_1$ fließt die Differenz. Weil jeder Maschenstrom in jeden Knoten seines Umlaufs hinein- und wieder herausfließt, ist jede Knotenregel von selbst erfüllt.

**Schritt 3**: Je Masche gilt die Maschenregel: Die Spannungen an den Impedanzen in Umlaufrichtung ergeben die antreibende Quellenspannung.

**Schritt 4**: Nach Maschenströmen geordnet, steht auf der Diagonalen die Summe der Impedanzen der Masche, außerhalb die gemeinsamen Impedanzen zweier Maschen, jede positiv bei gleicher und negativ bei entgegengesetzter Richtung der beiden Maschenströme; rechts stehen die antreibenden Quellenspannungen, positiv, wenn die Quelle den Maschenstrom vom Minus- zum Pluspol durch sich hindurchführt.

:::formel Satz
$$\begin{pmatrix} \underline Z_{11} & \cdots & \underline Z_{1,n_M} \\ \vdots & \ddots & \vdots \\ \underline Z_{n_M,1} & \cdots & \underline Z_{n_M,n_M} \end{pmatrix} \begin{pmatrix} \underline I_{1} \\ \vdots \\ \underline I_{n_M} \end{pmatrix} = \begin{pmatrix} \underline U_{q1} \\ \vdots \\ \underline U_{q,n_M} \end{pmatrix}$$
:::

**So liest man das:** Jeder Maschenstrom wird mit allen Impedanzen seiner Masche multipliziert, ein Nachbarstrom nur mit den gemeinsamen; ohne gesteuerte Quellen ist die Matrix deshalb symmetrisch. Für den Tiefpass:

$$\begin{pmatrix} R_1 + \underline Z_C & -\underline Z_C \\ -\underline Z_C & R_2 + 2\,\underline Z_C \end{pmatrix} \begin{pmatrix} \underline I_\mathrm{I} \\ \underline I_\mathrm{II} \end{pmatrix} = \begin{pmatrix} \underline U_q \\ 0 \end{pmatrix}$$

Eine ideale Stromquelle lässt sich nicht in eine Spannungsquelle umwandeln; man legt die Maschen dann so, dass nur ein Maschenstrom durch sie fließt, und dieser ist gleich ihrem Strom.

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
**Gegeben:** $\underline U_q$ = 1 V, $R_1$ = $R_2$ = 1 kΩ, $C_1$ = $C_2$ = 100 nF, ω = 10⁴ 1/s, also $\underline Z_C$ = −j·1 kΩ.

**Gesucht:** die Maschenströme und die Ausgangsspannung an $C_2$.

**Rechnung:** In kΩ und mA:

$$\begin{pmatrix} 1 - j & j \\ j & 1 - 2j \end{pmatrix} \begin{pmatrix} \underline I_\mathrm{I} \\ \underline I_\mathrm{II} \end{pmatrix} = \begin{pmatrix} 1\ \mathrm V \\ 0 \end{pmatrix}$$

Die zweite Zeile ergibt das Verhältnis der Maschenströme, die erste dann ihren Wert:

$$\underline I_\mathrm{I} = (2 + j)\,\underline I_\mathrm{II}, \qquad \big[(1 - j)(2 + j) + j\big]\,\underline I_\mathrm{II} = 3\,\underline I_\mathrm{II} = 1\ \mathrm V$$

$$\underline I_\mathrm{II} = 0{,}333\ \mathrm{mA}, \qquad \underline I_\mathrm{I} = (0{,}667 + 0{,}333\,j)\ \mathrm{mA}$$

$$\underline U_2 = \underline Z_C\,\underline I_\mathrm{II} = -0{,}333\,j\ \mathrm V$$

**Ergebnis:** **Ausgang −j·0,333 V: ein Drittel der Amplitude, 90° nacheilend.**

**Einordnung:** Bei der Frequenz, bei der Kondensator und Widerstand gleich hochohmig sind, drittelt der zweistufige Tiefpass die Amplitude und verzögert um eine Viertelperiode.
::::

## Die Knotenpotentialanalyse

*Warum genügen k − 1 Gleichungen, und wie stellt man sie direkt auf?*

Wandelt man im Tiefpass die Quelle mit $R_1$ in eine Stromquelle um, bleiben außer Masse zwei Knoten (Abbildung 6).

:::grafik
Szene: st1/netzwerkanalyse/02-knotenpotentiale · Vorlage: schaltbild-matrix
**Abbildung 6:** Derselbe Tiefpass, nachdem Quelle und $R_1$ in eine Stromquelle von 1 mA mit 1 mS parallel umgewandelt sind. Knoten 1 liegt zwischen $R_1$, $C_1$ und $R_2$, Knoten 2 am Ausgang, der Bezugsknoten ist Masse; die Kondensatoren haben die Admittanz j·1 mS. Daneben die Matrixgleichung mit der Leitwertmatrix (2 + j, −1; −1, 1 + j) mS und das Ergebnis (1 − j)/3 V und −j/3 V. Zwei Knotenpotentiale beschreiben alle Spannungen; die Maschenregel ist von selbst erfüllt.
:::

**Die Akteure:**

- __Bezugsknoten__: ein gewählter Knoten mit dem Potential null, meist Masse.
- __$\underline U_1, \ldots, \underline U_{n_K}$__: __Knotenpotentiale__, die Spannungen der übrigen Knoten gegen den Bezugsknoten; in V.
- __$\mathbf Y$__: __Leitwertmatrix__ mit den Einträgen $\underline Y_{\mu\nu}$; in S.
- __$\underline I_{q\mu}$__: Summe der Quellenströme in den Knoten μ hinein; in A, im Tiefpass 1 mA in Knoten 1. __$G_1$__, __$G_2$__: die Leitwerte von $R_1$ und $R_2$, je 1 mS.

**Das Zusammenspiel:**

**Schritt 1**: Mit den Knotenpotentialen als Unbekannten ist jede Zweigspannung eine Differenz zweier Potentiale; in jedem Umlauf heben sich diese auf, denn man kehrt zum Ausgangsknoten zurück. Jede Maschenregel ist damit von selbst erfüllt.

**Schritt 2**: Der Strom durch eine Admittanz ist die Admittanz mal der Potentialdifferenz ihrer Knoten.

**Schritt 3**: Je Knoten außer dem Bezugsknoten gilt die Knotenregel: Was über Admittanzen abfließt, fließt aus Quellen zu.

**Schritt 4**: Nach Potentialen geordnet, steht auf der Diagonalen die Summe aller Admittanzen am Knoten, außerhalb das Negative der Admittanz zwischen zwei Knoten, rechts der hineinfließende Quellenstrom.

:::formel Satz
$$\begin{pmatrix} \underline Y_{11} & \cdots & \underline Y_{1,n_K} \\ \vdots & \ddots & \vdots \\ \underline Y_{n_K,1} & \cdots & \underline Y_{n_K,n_K} \end{pmatrix} \begin{pmatrix} \underline U_{1} \\ \vdots \\ \underline U_{n_K} \end{pmatrix} = \begin{pmatrix} \underline I_{q1} \\ \vdots \\ \underline I_{q,n_K} \end{pmatrix}$$
:::

**So liest man das:** Das eigene Potential zählt mit allen Admittanzen am Knoten, ein Nachbarpotential nur mit der verbindenden Admittanz, negativ, weil ein höheres Nachbarpotential Strom hineintreibt statt hinaus. Ohne gesteuerte Quellen ist die Matrix symmetrisch. Für den Tiefpass:

$$\begin{pmatrix} G_1 + G_2 + j\omega C_1 & -G_2 \\ -G_2 & G_2 + j\omega C_2 \end{pmatrix} \begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix} = \begin{pmatrix} \underline I_q \\ 0 \end{pmatrix}$$

**Kurz gesagt:** Knotenpotentiale erfüllen die Maschenregel von selbst; deshalb genügen die $k - 1$ Knotengleichungen, solange jeder Zweig eine Admittanz oder eine Stromquelle ist.

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
**Gegeben:** die Quelle 1 V mit $R_1$ = 1 kΩ umgewandelt in 1 mA mit $G_1$ = 1 mS; $G_2$ = 1 mS; $j\omega C$ = j·1 mS für beide Kondensatoren.

**Gesucht:** die Knotenpotentiale und der Strom durch $R_1$.

**Rechnung:** In mS, mA und V:

$$\begin{pmatrix} 2 + j & -1 \\ -1 & 1 + j \end{pmatrix} \begin{pmatrix} \underline U_1 \\ \underline U_2 \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$$

Aus der zweiten Zeile das Verhältnis, aus der ersten der Ausgang:

$$\underline U_1 = (1 + j)\,\underline U_2, \qquad \big[(2 + j)(1 + j) - 1\big]\,\underline U_2 = 3j\,\underline U_2 = 1$$

$$\underline U_2 = -0{,}333\,j\ \mathrm V, \qquad \underline U_1 = (0{,}333 - 0{,}333\,j)\ \mathrm V$$

Der Strom durch $R_1$ folgt aus der ursprünglichen Schaltung:

$$\underline I_{R1} = \frac{\underline U_q - \underline U_1}{R_1} = (0{,}667 + 0{,}333\,j)\ \mathrm{mA}$$

**Ergebnis:** **Dieselben Werte wie mit Maschenströmen: −j·0,333 V am Ausgang, und durch $R_1$ fließt $\underline I_\mathrm{I}$.**

**Einordnung:** Den Strom durch $R_1$ muss man in der ursprünglichen Schaltung berechnen; in der umgewandelten führt $G_1$ einen anderen Strom, 0,471 mA bei −45°, denn die Ersatzquelle ist nur nach außen gleichwertig.
::::

:::frage
„Was macht man in der Knotenanalyse mit einer idealen Spannungsquelle?“
Liegt sie zwischen einem Knoten und dem Bezugsknoten, legt sie dessen Potential fest; es ist keine Unbekannte mehr, und seine Gleichung entfällt. Mit einer idealen Signalquelle ohne Innenwiderstand wäre das Gate der Verstärkerstufe auf 10 mV festgelegt, und es blieben zwei Gleichungen. Eine ideale Spannungsquelle zwischen zwei anderen Knoten braucht die modifizierte Knotenanalyse, die ihren Strom als weitere Unbekannte aufnimmt; sie ist das folgende Thema.
:::

### Gesteuerte Quellen in der Knotengleichung

*Wo steht eine gesteuerte Stromquelle in der Leitwertmatrix, und was folgt daraus?*

Der Strom einer spannungsgesteuerten Stromquelle hängt von Knotenpotentialen ab; er gehört deshalb in die Matrix, nicht zu den Quellenströmen der rechten Seite.

:::grafik
Szene: st1/netzwerkanalyse/02-gesteuerte-quelle-matrix · Vorlage: schaltbild-matrix
**Abbildung 7:** Das Kleinsignal-Ersatzschaltbild der Verstärkerstufe neben seiner Leitwertmatrix in mS, Zeilen und Spalten G, D und S: (0,1; 0; 0), (1; 0,225; −1,025), (−1; −0,025; 2,025). Blau die Einträge der passiven Leitwerte, die symmetrisch stehen; orange die vier Anteile der gesteuerten Quelle, ±1 mS in den Zeilen D und S und den Spalten G und S. Eine gesteuerte Quelle steht in den Zeilen der Knoten, zwischen denen ihr Strom fließt, und in den Spalten der Knoten, deren Spannung sie steuert; deshalb ist die Matrix nicht mehr symmetrisch.
:::

**Die Akteure:**

- __a__, __b__: die Knoten, zwischen denen die gesteuerte Quelle ihren Strom von a nach b treibt; in der Verstärkerstufe D und S. __c__, __d__: die Knoten der Steuerspannung; G und S.
- __$G_\mathrm{sig}$__, __$\underline I_\mathrm{sig}$__: Innenleitwert und Quellenstrom der umgewandelten Signalquelle, 0,1 mS und 1 µA; __$G_D$__, __$G_L$__, __$G_S$__: die Leitwerte von $R_D$, $R_L$ und $R_S$, 0,1 mS, 0,1 mS und 1 mS.

:::formel Definition
$$\underline I_{a \to b} = g_m\,(\underline U_c - \underline U_d)$$
:::

Man schreibt die Steuerspannung als Differenz von Knotenpotentialen, weil sie so unmittelbar in die Knotengleichungen passt.

**Das Zusammenspiel:** In der Gleichung von a fließt der gesteuerte Strom ab, in der von b fließt er zu. Auf die linke Seite gebracht, ergibt das $+g_m$ in Zeile a, Spalte c, $-g_m$ in Zeile a, Spalte d, $-g_m$ in Zeile b, Spalte c und $+g_m$ in Zeile b, Spalte d, die orangefarbenen Einträge in Abbildung 7. Die Zeile des Gates bekommt nichts, denn dort fließt kein Strom der Quelle. Für Drain und Source der Verstärkerstufe:

$$g_m\,\underline U_G + (G_D + G_L + g_o)\,\underline U_D - (g_m + g_o)\,\underline U_S = 0$$

$$-g_m\,\underline U_G - g_o\,\underline U_D + (G_S + g_m + g_o)\,\underline U_S = 0$$

**Kurz gesagt:** Ohne gesteuerte Quellen ist die Leitwertmatrix symmetrisch, weil jede Admittanz zwischen zwei Knoten in beiden Knotengleichungen gleich vorkommt; eine einzelne gesteuerte Stromquelle, deren Steuerspannung an anderen Knoten liegt als ihr Strom, steht nur in den Zeilen ihrer Stromknoten und macht die Matrix unsymmetrisch.

::::beispiel Verstärkerstufe mit Knotenpotentialen
**Gegeben:** das Ersatzschaltbild aus Abbildung 1 mit Last: Signalquelle umgewandelt in 1 µA mit $G_\mathrm{sig}$ = 0,1 mS; $g_m$ = 1 mS, $g_o$ = 25 µS, $G_D$ = $G_L$ = 0,1 mS, $G_S$ = 1 mS.

**Gesucht:** die Knotenpotentiale und die Verstärkung.

**Rechnung:** In mS, mV und µA:

$$\begin{pmatrix} 0{,}1 & 0 & 0 \\ 1 & 0{,}225 & -1{,}025 \\ -1 & -0{,}025 & 2{,}025 \end{pmatrix} \begin{pmatrix} \underline U_G \\ \underline U_D \\ \underline U_S \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$$

Zeile G ergibt 10 mV am Gate. Die Summe der Zeilen D und S enthält $g_m$ nicht, denn der gesteuerte Strom fließt nur zwischen diesen beiden Knoten; mit Zeile S folgt:

$$0{,}2\,\underline U_D + \underline U_S = 0, \qquad -10 - 0{,}025\,\underline U_D + 2{,}025\,\underline U_S = 0$$

$$\underline U_D = -23{,}26\ \mathrm{mV}, \qquad \underline U_S = 4{,}65\ \mathrm{mV}$$

**Ergebnis:** **10 mV, −23,26 mV und 4,65 mV; Verstärkung −2,33, wie über die Ersatzquelle.**

**Einordnung:** +1 mS in Zeile D, Spalte G, aber 0 in Zeile G, Spalte D: Das Gate steuert den Drain, der Drain wirkt nicht auf das Gate zurück. Ohne Source-Widerstand wären es −4,44; er halbiert ungefähr die Verstärkung und macht dafür den Ausgang des Transistors hochohmiger.
::::

:::fehlvorstellung
„Die Leitwertmatrix muss symmetrisch sein; ist sie es nicht, habe ich mich verrechnet.“ Das liegt nahe, weil die Symmetrie in Netzen aus Widerständen, Kondensatoren und Spulen eine gute Probe ist. Sicher gilt sie aber nur ohne gesteuerte Quellen: In der Verstärkerstufe steht +1 mS in Zeile D, Spalte G und 0 in Zeile G, Spalte D. Als Probe bleibt, dass die passiven Anteile allein symmetrisch sein müssen.
:::

## Knoten oder Maschen?

*Welches Verfahren braucht weniger Gleichungen?*

Die kleinere der beiden Zahlen $k - 1$ und $z - k + 1$ entscheidet. Drei reale Spannungsquellen parallel an einer Last haben zwei Knoten und vier Zweige: eine Knotengleichung gegen drei Maschengleichungen. Beim Tiefpass und bei der Verstärkerstufe sind beide Zahlen gleich; dort entscheidet die Art der Quellen. Unabhängige und spannungsgesteuerte Stromquellen passen ohne Umweg in die Knotengleichung. Weil Transistoren im Kleinsignalbild gesteuerte Stromquellen sind, rechnet man Transistorschaltungen mit Knotenpotentialen, und Schaltungssimulatoren tun es ebenso.

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Linearität und Impedanzen | jede Antwort hängt linear von den unabhängigen Quellen ab, auch mit Spulen und Kondensatoren |
| Ersatzquelle | Linearität an zwei Klemmen: eine Gerade, zwei Zahlen |
| gesteuerte Quellen | lineare Bauelemente, aber keine Anregung; sie bleiben beim Abschalten aktiv |
| Maschenströme | Unbekannte, die die Knotenregel von selbst erfüllen |
| Knotenpotentiale | Unbekannte, die die Maschenregel von selbst erfüllen |

In einer linearen Schaltung hängt jede Spannung und jeder Strom linear von den unabhängigen Quellen ab; deshalb verhält sich die Schaltung an zwei Klemmen wie eine einzige Quelle mit Innenimpedanz, und ihr Gleichungssystem wird klein, wenn man als Unbekannte Knotenpotentiale oder Maschenströme wählt, weil diese eine der beiden Kirchhoffschen Regeln schon von selbst erfüllen.

## Bedeutung und Ausblick

Jede Kleinsignalrechnung an Transistorstufen benutzt diese Werkzeuge: die Knotenanalyse für die Verstärkung, die Ersatzquelle für den Ausgangswiderstand und die Belastung durch die nächste Stufe. Ideale Spannungsquellen zwischen zwei Knoten, von denen keiner der Bezugsknoten ist, und andere gesteuerte Quellen passen nicht in die reine Knotenanalyse; die modifizierte Knotenanalyse, das folgende Thema, ergänzt sie und stellt die Gleichungen Bauteil für Bauteil auf.

**In der ausführlichen Fassung:** die Schaltzeichen aller Quellen und die vier Arten gesteuerter Quellen mit Beispielen, Impedanzen und Gleichungszahlen an Beispielen, der Graph der Verstärkerstufe mit Baum, die Verlustleistung in Ersatzquellen, ideale Stromquellen in der Maschenanalyse, der Unterschied zwischen Maschen- und Zweigstrom, eine Analogie für Knotenpotentiale, das Zeigerbild und der Frequenzgang des Tiefpasses, die Reziprozität von Netzen aus Widerständen, Spulen und Kondensatoren, die Wahl des Verfahrens mit Tabelle und Beispiel und warum Simulatoren mit Knotenpotentialen rechnen. [Zur ausführlichen Fassung](/wissen/elektrotechnik/3-semester/schaltungstechnik-1/netzwerkanalyse/ersatzquellen-maschen-und-knotenanalyse-ausfuehrlich.html)

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
F: Eine Ersatzquelle hat die Leerlaufspannung −43,96 mV und die Innenimpedanz 8,90 kΩ. Welche Spannung liegt an einer Last von 10 kΩ?
A: Nach dem Spannungsteiler −43,96 mV · 10 kΩ/18,90 kΩ = −23,26 mV.
:::
