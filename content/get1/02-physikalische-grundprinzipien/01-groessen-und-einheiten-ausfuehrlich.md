---
title: Physikalische Größen und Einheiten
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Physikalische Grundprinzipien
order: 20100
summary: Was eine physikalische Größe ist, wie die sieben Basiseinheiten des SI seit 2019 über sieben definierende Konstanten festgelegt sind, wie abgeleitete Einheiten und Vorsätze entstehen und wie man mit Einheiten rechnet und Rechnungen prüft. Ausführliche Fassung mit Geschwindigkeit und Beschleunigung als Ableitungen, dem Weg als Integral, Kraft, Gravitationsgesetz und Arbeit als Wegintegral, jeweils hergeleitet.
tags: physikalische Größe, Einheit, SI, Basisgrößen, Ampere, Einheitenvorsatz, Größengleichung, Dimensionskontrolle
stil: 3
fassung: ausfuehrlich
---

## Worum es geht

Wer die Spannung einer Steckdose angibt, schreibt 230 V und nicht 230. Die Zahl allein sagt nichts; erst die Einheit macht sie zu einer Aussage über die Welt, und mit den Einheiten lässt sich jede Rechnung prüfen. Das ganze Thema folgt aus einem Prinzip:

**Jede physikalische Größe ist Zahlenwert mal Einheit, und jede SI-Einheit ist ein Produkt von Potenzen der sieben Basiseinheiten; neue Größen entstehen, indem man bekannte multipliziert, dividiert, ableitet oder integriert, und ihre Einheiten entstehen dabei mit, so dass die Einheiten jeden Rechenfehler verraten, der die Einheit verändert.**

Vorausgesetzt werden nur Schulmathematik (Potenzen, Ableitung als Steigung, Integral als Fläche) und Schulphysik. Alles Weitere in der Elektrotechnik baut darauf auf: Im Artikel [Arbeit, Potenzial und Spannung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/arbeit-potenzial-und-spannung.html) wird die Spannung als Arbeit je Ladung eingeführt, und ihre Einheit Volt ist dann Joule durch Coulomb.

:::grafik
Szene: get1/grundprinzipien/01-einheitenbaum · Vorlage: blockschaltbild
**Abbildung 1:** Stammbaum der Einheiten. Unten die sieben Basiseinheiten des SI: Meter, Kilogramm, Sekunde, Ampere, Kelvin, Mol, Candela. Darüber die abgeleiteten Einheiten der Mechanik und Elektrotechnik, jede mit der Gleichung, aus der sie entsteht, und Pfeilen zu den Einheiten, aus denen sie gebaut ist: Newton aus F = m a (kg, m, s), Joule aus W = F s, Watt aus P = W/t, Coulomb aus Q = I t (A, s), Volt aus P = U I, Ohm aus R = U/I, Farad aus C = Q/U, Weber aus Volt mal Sekunde, Tesla aus Weber je Quadratmeter. Jede SI-Einheit ist ein Produkt von Potenzen der Basiseinheiten.
:::

## Zahlenwert und Einheit

*Was gibt eine physikalische Größe an, und warum gehört die Einheit untrennbar dazu?*

:::grafik
Szene: get1/grundprinzipien/01-zahlenwert-einheit · Vorlage: schema
**Abbildung 2:** Die Netzspannung $U$ als Produkt aus Zahlenwert und Einheit: 230 mal 1 V. Darunter dieselbe Spannung in zwei anderen Schreibweisen, 0,23 mal 1 kV und 230 000 mal 1 mV; Pfeile zeigen, dass der Zahlenwert um den Faktor 1000 kleiner bzw. größer wird, wenn die Einheit um denselben Faktor größer bzw. kleiner wird. Zahlenwert und Einheit ändern sich gegenläufig, die Größe bleibt dieselbe.
:::

Eine __physikalische Größe__ ist eine messbare Eigenschaft eines Körpers oder Vorgangs, etwa eine Länge, eine Masse oder eine Spannung. Messbar heißt: Man vergleicht sie mit einer festgelegten Vergleichsgröße, der __Einheit__, und gibt an, wie oft diese hineinpasst. Zwei Messgeräte zeigen an derselben Steckdose 230 V, gleich wer misst; ein Urteil wie „ziemlich viel Spannung“ hängt dagegen vom Beobachter ab. Eine physikalische Größe ist deshalb quantitativ und objektiv.

**Die Akteure:**

- __$G$__: eine beliebige physikalische Größe, etwa die Spannung $U$.
- __$\{G\}$__: ihr __Zahlenwert__, die Zahl vor der Einheit; bei 230 V die Zahl 230.
- __$[G]$__: ihre Einheit; bei der Spannung das Volt.

:::formel Definition
$$G = \{G\}\cdot[G]$$
:::

Man definiert eine Größe als Produkt, weil sich dann mit Zahlenwerten und Einheiten getrennt rechnen lässt wie mit Zahlen. Wechselt man die Einheit, ändert sich der Zahlenwert im umgekehrten Verhältnis, und die Größe bleibt dieselbe (Abbildung 2): 230 V sind 0,23 kV oder 230 000 mV. Nur bei Skalen mit verschobenem Nullpunkt wie Grad Celsius kommt zum Faktor eine Verschiebung hinzu. Die geschweiften und eckigen Klammern sind die Schreibweise der Norm DIN 1313; im Alltag schreibt man die Einheit hinter die Zahl.

::::beispiel Die Netzspannung in drei Schreibweisen
**Gegeben:** $U$ = 230 V; die Vorsätze k (Kilo, tausend) und m (Milli, ein Tausendstel).

**Gesucht:** Zahlenwert in Kilovolt und Millivolt.

**Rechnung:** Ein Kilovolt sind 1000 V, ein Millivolt 0,001 V:

$$U = 230\cdot 1\ \mathrm{V} = 230\cdot 0{,}001\ \mathrm{kV} = 0{,}23\ \mathrm{kV}$$

$$U = 230\cdot 1000\ \mathrm{mV} = 230\,000\ \mathrm{mV}$$

**Ergebnis:** **230 V = 0,23 kV = 230 000 mV.**

**Einordnung:** In allen drei Schreibweisen ist das Produkt aus Zahlenwert und Einheit gleich; welche man wählt, ist eine Frage der Lesbarkeit. Für eine Steckdose ist 230 V üblich, für Hochspannungsleitungen kV, für Sensorsignale mV.
::::

Die Physik sucht Gesetzmäßigkeiten zwischen solchen Größen, etwa das Ohmsche Gesetz, nach dem die Spannung an einem Widerstand das Produkt aus Widerstand und Strom ist; die Ingenieurwissenschaften wenden sie an, in Bauelementen, Schaltungen und Kraftwerken. Jede Größe hat ein festes __Formelzeichen__, einen Buchstaben, der für sie steht. Die wichtigsten des ersten Semesters:

| Gebiet | Größe und Formel­zeichen |
|---|---|
| Mechanik | Weg $s$, Länge $l$, Radius $r$, Zeit $t$, Masse $m$, Geschwindigkeit $v$, Beschleunigung $a$, Kraft $F$, Arbeit $W$ |
| Elektrizitätslehre | Ladung $Q$, Strom $I$, Span­nung $U$, Feldstärke $E$, Wider­stand $R$ |
| Wärmelehre | Tempe­ratur $T$, Wärmemenge $Q$, Entropie $S$ |

Dasselbe Zeichen steht manchmal für zwei Größen: $Q$ für die Ladung und für die Wärmemenge. Was gemeint ist, sagt der Zusammenhang; in der Elektrotechnik ist $Q$ fast immer die Ladung.

## Basisgrößen und Basiseinheiten des SI

*Aus welchen Grundbausteinen sind alle Einheiten gebaut, und wie sind diese festgelegt?*

Das __Internationale Einheitensystem__ (Système international d'unités, SI) teilt die Größen in sieben __Basisgrößen__ und alle übrigen, die __abgeleiteten Größen__. Im SI gelten die Basisgrößen als voneinander unabhängig: Keine wird durch die anderen ausgedrückt, und jede abgeleitete Größe lässt sich auf sie zurückführen. Das ist eine Festlegung; ältere Einheitensysteme kamen mit weniger Basisgrößen aus (Frage-Kasten unten).

| Basis­größe | Formel­zeichen | Einheit | Zeichen |
|---|---|---|---|
| Länge | $l$, $s$, $r$ | Meter | m |
| Masse | $m$ | Kilo­gramm | kg |
| Zeit | $t$ | Sekunde | s |
| elek­trische Strom­stärke | $I$ | Ampere | A |
| abso­lute Tempe­ratur | $T$ | Kelvin | K |
| Stoff­menge | $n$ | Mol | mol |
| Licht­stärke | $I_v$ | Candela | cd |

:::grafik
Szene: get1/grundprinzipien/01-si-konstanten · Vorlage: blockschaltbild
**Abbildung 3:** Die sieben definierenden Konstanten des SI mit ihren seit 2019 exakt festgelegten Werten und Pfeilen zu den Basiseinheiten, die sie festlegen: Cäsium-Frequenz 9 192 631 770 Hz → Sekunde; Lichtgeschwindigkeit 299 792 458 m/s → Meter (mit der Sekunde); Planck-Konstante 6,626 070 15·10⁻³⁴ J s → Kilogramm (mit Meter und Sekunde); Elementarladung 1,602 176 634·10⁻¹⁹ C → Ampere (mit der Sekunde); Boltzmann-Konstante 1,380 649·10⁻²³ J/K → Kelvin (mit Kilogramm, Meter und Sekunde); Avogadro-Konstante 6,022 140 76·10²³ /mol → Mol; photometrisches Strahlungsäquivalent für Licht der Frequenz 540·10¹² Hz, 683 lm/W → Candela (mit Kilogramm, Meter und Sekunde). Die Einheiten hängen an exakt festgelegten Konstanten, nicht mehr an Gegenständen.
:::

Wie groß eine Einheit ist, muss irgendwo festgelegt sein. Konkret: Die Sekunde ist die Dauer von genau 9 192 631 770 Schwingungen einer bestimmten Strahlung des Atoms Cäsium-133; das Meter ist die Strecke, die Licht im Vakuum in genau 1/299 792 458 Sekunde zurücklegt, 3,34 ns; ein Ampere ist ein Strom, bei dem je Sekunde genau 1/(1,602 176 634·10⁻¹⁹) __Elementarladungen__ fließen, rund 6,24·10¹⁸; die Elementarladung, der Betrag der Ladung eines Elektrons, ist dafür auf genau 1,602 176 634·10⁻¹⁹ A s festgelegt. Eine Amperesekunde heißt Coulomb, C, die Einheit der Ladung. Seit dem 20. Mai 2019 sind alle sieben Basiseinheiten so über sieben __definierende Konstanten__ festgelegt, deren Zahlenwerte vereinbart sind und nicht mehr gemessen werden (Abbildung 3); dabei greifen die Definitionen ineinander, das Kilogramm etwa braucht zusätzlich Meter und Sekunde. Vorher hing das Kilogramm an einem Metallzylinder in Sèvres bei Paris und das Ampere an der Kraft zwischen zwei stromdurchflossenen Drähten. Endgültig sind die Definitionen der Einheiten auch heute nicht; sie werden mit der Messtechnik weiterentwickelt. Seit 2019 werden vor allem die Verfahren verbessert, mit denen man die Einheiten verwirklicht; die Definitionen selbst ändern sich nur noch selten, als nächste ist eine neue Definition der Sekunde über optische Atomuhren in Vorbereitung.

::::beispiel Wie viele Elektronen sind ein Strom?
**Gegeben:** Elementarladung $e$ = 1,602 176 634·10⁻¹⁹ C (exakt); Ströme 1 A, 20 mA (eine Leuchtdiode), 80 nA (Eingangsruhestrom eines Operationsverstärkers), 1 pA.

**Gesucht:** die Zahl der Elementarladungen, die je Sekunde fließen.

**Rechnung:** Ein Coulomb ist eine Amperesekunde; je Sekunde fließen $I$ durch $e$ Ladungen:

$$\frac{1\ \mathrm{A}}{1{,}602\,176\,634\cdot10^{-19}\ \mathrm{C}} = 6{,}24\cdot10^{18}\ \frac{1}{\mathrm{s}}$$

Für die übrigen Ströme entsprechend: 20 mA ergeben 1,25·10¹⁷, 80 nA 4,99·10¹¹ und 1 pA 6,24·10⁶ Ladungen je Sekunde.

**Ergebnis:** **1 A sind 6,24·10¹⁸ Elementarladungen je Sekunde; selbst 1 pA sind noch über sechs Millionen.**

**Einordnung:** Ob man Strom als stetige Größe behandeln darf, hängt von der Zahl der Ladungen in der betrachteten Zeitspanne ab. Bei 1 pA fließen in einer Mikrosekunde im Mittel nur 6,2 Ladungen, und ihre Zahl schwankt von Mikrosekunde zu Mikrosekunde um rund 40 %; diese Körnigkeit misst man als __Schrotrauschen__. Elektrometer messen Ströme bis hinab zu Femtoampere, und 1 fA sind nur noch rund 6200 Ladungen je Sekunde. Einzeln abzählen lassen sich die Ladungen in Bauelementen, die einzelne Elektronen weiterreichen; mit ihnen lässt sich das Ampere seit 2019 unmittelbar verwirklichen.
::::

:::frage
„Warum gerade sieben Basisgrößen? Würden nicht weniger reichen?“
Die Zahl ist eine Festlegung, keine Naturnotwendigkeit. Ältere Einheitensysteme der Physik kamen für Mechanik und Elektrizität mit drei Basisgrößen aus, Länge, Masse und Zeit, und leiteten die Ladung über das Gesetz der Kraft zwischen Ladungen ab; die elektrischen Einheiten bekamen dann krumme Kombinationen wie Zentimeter hoch drei Halbe. Das SI nimmt die Stromstärke als eigene Basisgröße, weil die praktischen elektrischen Einheiten Ampere, Volt und Ohm schon verbreitet waren und eine eigene elektrische Basisgröße die gebrochenen Exponenten vermeidet. Temperatur, Stoffmenge und Lichtstärke kamen hinzu, weil Wärmelehre, Chemie und Lichttechnik sie als eigene Größen brauchen. Mit sieben Basisgrößen lassen sich die SI-Einheiten aller gebräuchlichen Größen ohne Zahlenfaktoren bilden, und für Größen, die über Produkte und Quotienten festgelegt sind, auch ohne gebrochene Exponenten.
:::

:::frage
„Warum hat man 2019 das Kilogramm neu definiert? Es hat doch funktioniert.“
Bis dahin war das Kilogramm die Masse eines Platin-Iridium-Zylinders in Sèvres. Vergleiche mit seinen Kopien zeigten über rund hundert Jahre Abweichungen von etwa 50 Mikrogramm, und ob sich das Urkilogramm oder die Kopien verändert hatten, ließ sich grundsätzlich nicht entscheiden, denn das Urkilogramm war per Definition immer genau ein Kilogramm. Seit 2019 ist stattdessen die Planck-Konstante festgelegt, eine Naturkonstante der Quantenphysik mit der Einheit J s; mit einer Wattwaage, die eine Gewichtskraft gegen eine elektromagnetische Kraft misst, lässt sich das Kilogramm überall verwirklichen, wo man eine solche Waage oder ein gleichwertiges Verfahren aufbaut, ohne Bezug auf einen Gegenstand.
:::

## Abgeleitete Einheiten

*Wie entstehen Einheiten wie Newton, Volt oder Ohm aus den Basiseinheiten?*

Ein Körper von 1 kg, der in jeder Sekunde um 1 m/s schneller wird, erfährt insgesamt eine Kraft von einem __Newton__. Weil Kraft Masse mal Beschleunigung ist, ist das Newton Kilogramm mal Meter durch Sekunde zum Quadrat. So entsteht jede abgeleitete Einheit aus der Gleichung, die ihre Größe festlegt, und viele bekommen einen eigenen Namen. Abbildung 1 zeigt die Kette von der Mechanik zur Elektrotechnik:

| Größe | Einheit | in Basis­einheiten und anderen SI-Ein­heiten |
|---|---|---|
| Kraft $F$ | Newton, N | kg m s⁻² |
| Arbeit, Energie $W$ | Joule, J | kg m² s⁻² = N m = W s |
| Leis­tung $P$ | Watt, W | kg m² s⁻³ = J/s = V A |
| Druck $p$ | Pascal, Pa | kg m⁻¹ s⁻² = N/m² |
| Ladung $Q$ | Coulomb, C | A s |
| Span­nung $U$ | Volt, V | kg m² s⁻³ A⁻¹ = W/A = J/C |
| Wider­stand $R$ | Ohm, Ω | kg m² s⁻³ A⁻² = V/A |
| Kapa­zität $C$ | Farad, F | kg⁻¹ m⁻² s⁴ A² = A s/V |
| Induk­tivität $L$ | Henry, H | kg m² s⁻² A⁻² = V s/A |
| magne­tischer Fluss $\Phi$ | Weber, Wb | kg m² s⁻² A⁻¹ = V s |
| magne­tische Fluss­dichte $B$ | Tesla, T | kg s⁻² A⁻¹ = V s/m² |

Für die Flussdichte ist auch der Name „magnetische Induktion“ üblich. Wie jede dieser Zeilen entsteht, zeigt das Volt.

:::formel Formel
$$1\ \mathrm{V} = 1\ \frac{\mathrm{W}}{\mathrm{A}} = 1\ \frac{\mathrm{kg}\,\mathrm{m}^2}{\mathrm{s}^3\,\mathrm{A}}$$
:::

**So liest man das:** Ein Volt ist ein Watt je Ampere: Eine Spannung von 1 V setzt bei einem Strom von 1 A eine Leistung von 1 W um. In Basiseinheiten stehen darin die Mechanik (Kilogramm, Meter, Sekunde), über die Leistung, und das Ampere, über den Strom.

Idee der Herleitung: Man geht die Gleichungen von der Kraft über Arbeit und Leistung bis zur elektrischen Leistung durch und setzt jeweils die schon bekannten Einheiten ein.

:::herleitung
**Ausgangspunkt:** die Gleichungen, die die Größen festlegen: Kraft ist Masse mal Beschleunigung, Arbeit ist Kraft mal Weg (Abschnitt *Arbeit*), Leistung ist Arbeit je Zeit, und die elektrische Leistung ist Spannung mal Strom.

**Annahmen:** (i) Einheiten werden wie Faktoren behandelt (Abschnitt *Rechnen mit Einheiten*). (ii) Das SI ist so gebaut, dass in diesen Gleichungen keine Zahlenfaktoren auftreten.

**Schritt 1**: Newton aus Masse mal Beschleunigung:

$$1\ \mathrm{N} = 1\ \mathrm{kg}\cdot 1\ \frac{\mathrm{m}}{\mathrm{s}^2} = 1\ \frac{\mathrm{kg}\,\mathrm{m}}{\mathrm{s}^2}$$

**Schritt 2**: Joule aus Kraft mal Weg:

$$1\ \mathrm{J} = 1\ \mathrm{N}\cdot 1\ \mathrm{m} = 1\ \frac{\mathrm{kg}\,\mathrm{m}^2}{\mathrm{s}^2}$$

**Schritt 3**: Watt aus Arbeit je Zeit:

$$1\ \mathrm{W} = 1\ \frac{\mathrm{J}}{\mathrm{s}} = 1\ \frac{\mathrm{kg}\,\mathrm{m}^2}{\mathrm{s}^3}$$

**Schritt 4** (entscheidender Schritt): Volt aus der elektrischen Leistung: Weil Leistung Spannung mal Strom ist, ist die Spannung Leistung durch Strom:

$$1\ \mathrm{V} = 1\ \frac{\mathrm{W}}{\mathrm{A}} = 1\ \frac{\mathrm{kg}\,\mathrm{m}^2}{\mathrm{s}^3\,\mathrm{A}}$$

**Ergebnis:**

$$1\ \mathrm{V} = 1\ \frac{\mathrm{W}}{\mathrm{A}} = 1\ \frac{\mathrm{kg}\,\mathrm{m}^2}{\mathrm{s}^3\,\mathrm{A}}$$

**Woher die Faktoren kommen:** Das Kilogramm und das Meter zum Quadrat stammen aus der Arbeit, die dritte Potenz der Sekunde aus Beschleunigung und Leistung, das Ampere im Nenner aus der Teilung durch den Strom.

**Proben:** Mit dem Ohmschen Gesetz ist das Ohm ein Volt je Ampere, also kg m² s⁻³ A⁻², wie in der Tabelle. Über die Ladung: Ein Joule je Coulomb ist kg m² s⁻² durch A s, wieder kg m² s⁻³ A⁻¹.

**Grenzen:** Die Rechnung zeigt nur, aus welchen Basiseinheiten eine Einheit besteht; welche Größe gemeint ist, sagt sie nicht. Drehmoment und Energie etwa haben beide kg m² s⁻².
:::

::::beispiel Ein Föhn am Netz
**Gegeben:** Föhn mit 2100 W an 230 V.

**Gesucht:** Strom, Widerstand und die Einheit des Widerstands in Basiseinheiten.

**Rechnung:** Strom aus Leistung durch Spannung:

$$I = \frac{2100\ \mathrm{W}}{230\ \mathrm{V}} = 9{,}13\ \frac{\mathrm{W}}{\mathrm{V}} = 9{,}13\ \mathrm{A}$$

Widerstand aus dem Ohmschen Gesetz:

$$R = \frac{230\ \mathrm{V}}{9{,}13\ \mathrm{A}} = 25{,}2\ \frac{\mathrm{V}}{\mathrm{A}} = 25{,}2\ \Omega$$

In Basiseinheiten ist ein Volt je Ampere kg m² s⁻³ A⁻².

**Ergebnis:** **9,13 A und 25,2 Ω; ein Ohm ist kg m² s⁻³ A⁻².**

**Einordnung:** Mit Basiseinheiten rechnet man selten; sie zeigen aber, warum W/V ein Ampere und V/A ein Ohm ist. Weil die Einheiten im SI ohne Zahlenfaktoren zusammenpassen, kommt am Ende ohne Umrechnung die richtige Einheit heraus.
::::

:::fehlvorstellung
„Haben zwei Größen dieselben Basiseinheiten, sind sie dieselbe Größe.“ Das liegt nahe, weil die Einheitenkontrolle sonst so zuverlässig ist. Das Hertz der Frequenz und das Becquerel der radioaktiven Aktivität sind aber beide eine durch Sekunde, und das Newtonmeter des Drehmoments hat dieselben Basiseinheiten wie das Joule der Energie, kg m² s⁻². Ein Drehmoment ist trotzdem keine Energie: Beim Drehmoment steht die Kraft senkrecht zum Hebelarm, bei der Arbeit wirkt sie längs des Weges (Abschnitt *Arbeit*). Deshalb schreibt man N m für Drehmomente und J für Energien, Hz nur für periodische Vorgänge und Bq nur für Zerfälle. In der Mechanik steht N m manchmal auch für Energien; rechnerisch ist das richtig, 1 J = 1 N m. Damit beide Größen unterscheidbar bleiben, schreibt die SI-Broschüre Energien in J und verwendet das Joule nie für Drehmomente.
:::

## Einheitenvorsätze

*Wie schreibt man sehr große und sehr kleine Werte, ohne lange Zehnerpotenzen?*

:::grafik
Szene: get1/grundprinzipien/01-vorsaetze · Vorlage: skala-log
**Abbildung 4:** Logarithmische Achse der Stromstärke von 1 pA bis 10 A, darüber die Vorsätze Piko, Nano, Mikro, Milli als Abschnitte je drei Zehnerpotenzen. Markiert: 1 pA (6,24 Millionen Elementarladungen je Sekunde), 20 pA (Sperrstrom der Beispieldiode aus dem Diodenkapitel bei −1 V), 80 nA (Eingangsruhestrom eines Operationsverstärkers), 20 mA (Leuchtdiode), 9,13 A (Föhn mit 2100 W an 230 V). Zwischen dem kleinsten und dem größten Strom liegen knapp dreizehn Zehnerpotenzen; Vorsätze machen sie lesbar.
:::

Ein Operationsverstärker vom Typ 741 nimmt an jedem Eingang typisch 0,000 000 080 A auf. Lesbar wird das als 80 nA: Der __Vorsatz__ n, gesprochen Nano, steht für den Faktor 10⁻⁹. Ein Vorsatz ist also ein Zahlfaktor, der vor der Einheit steht und den Zahlenwert handlich macht (Abbildung 4). Die Vorsätze des SI, seit 2022 von 10⁻³⁰ bis 10³⁰:

| Teile | Faktor | Vielfache | Faktor |
|---|---|---|---|
| Dezi d | 10⁻¹ | Deka da | 10¹ |
| Zenti c | 10⁻² | Hekto h | 10² |
| Milli m | 10⁻³ | Kilo k | 10³ |
| Mikro µ | 10⁻⁶ | Mega M | 10⁶ |
| Nano n | 10⁻⁹ | Giga G | 10⁹ |
| Piko p | 10⁻¹² | Tera T | 10¹² |
| Femto f | 10⁻¹⁵ | Peta P | 10¹⁵ |
| Atto a | 10⁻¹⁸ | Exa E | 10¹⁸ |
| Zepto z | 10⁻²¹ | Zetta Z | 10²¹ |
| Yokto y | 10⁻²⁴ | Yotta Y | 10²⁴ |
| Ronto r | 10⁻²⁷ | Ronna R | 10²⁷ |
| Quekto q | 10⁻³⁰ | Quetta Q | 10³⁰ |

Zepto, Zetta, Yokto und Yotta kamen 1991 hinzu, Ronto, Ronna, Quekto und Quetta 2022, vor allem weil die Datenmengen der Informationstechnik an die Grenze der alten Vorsätze stießen. Für ihren Gebrauch gelten wenige Regeln:

- Vorsätze für Teile werden klein geschrieben, für Vielfache ab Mega groß; Deka, Hekto und Kilo sind aus historischen Gründen klein.
- Vor einer Einheit steht höchstens ein Vorsatz: 1 nF, nicht 1 mµF.
- Vorsatz und Einheit bilden ein einziges Zeichen; eine Hochzahl gilt für beide zusammen.
- Beim Kilogramm, das schon einen Vorsatz trägt, setzt man Vorsätze vor das Gramm: 1 mg, nicht 1 µkg.
- Schaltungssimulatoren der SPICE-Familie folgen diesen Zeichen nicht: Sie unterscheiden Groß- und Kleinschreibung nicht, M und m bedeuten dort beide Milli, und Mega schreibt man MEG.

:::fehlvorstellung
„1 km² sind 1000 m².“ Das liegt nahe, weil ein Kilometer 1000 m sind. Der Vorsatz gehört aber zur Einheit, bevor quadriert wird: 1 km² ist ein Quadrat von 1 km Seitenlänge, also 1000 m mal 1000 m, eine Million Quadratmeter. Ebenso ist 1 cm³ ein Millionstel Kubikmeter, und 1 mm² Leiterquerschnitt sind 10⁻⁶ m².
:::

:::frage
„Warum schreibt man km mit kleinem k, aber MW mit großem M?“
Weil bei Vorsätzen die Groß- und Kleinschreibung Bedeutung trägt: m ist Milli, 10⁻³, und M ist Mega, 10⁶; ein Milliwatt und ein Megawatt liegen um den Faktor 10⁹ auseinander. Die Regel, Vielfache groß zu schreiben, gilt ab Mega. Kilo, Hekto und Deka sind älter als die Regel und blieben klein; ein großes K stünde zudem schon für das Kelvin.
:::

## Rechnen mit Einheiten

*Wie rechnet man mit Größen, und wie verraten Einheiten einen Rechenfehler?*

Weil eine Größe ein Produkt aus Zahlenwert und Einheit ist, sind Einheiten und Vorsätze Faktoren, und man rechnet mit ihnen nach den gewohnten Regeln für Produkte.

**Das Zusammenspiel in Schritten:**

**Schritt 1**: Ein Vorsatz ist ein Zahlfaktor und darf ausgeschrieben werden: 2 kN sind 2 mal 1000 N, also 2000 N.

**Schritt 2**: Beim Multiplizieren und Dividieren rechnet man Zahlenwerte und Einheiten getrennt: 2 A mal 12 V sind 24 A V, und weil Volt mal Ampere ein Watt ist, 24 W. Gleiche Einheiten kürzen sich wie Zahlen: 6 N m durch 3 m sind 2 N. Vorsätze multiplizieren sich mit: Mega mal Milli ist Kilo, Mikro mal Mikro ist Piko, Milli mal Kilo ist eins.

**Schritt 3**: Umrechnen heißt mit einem Bruch vom Wert 1 multiplizieren. Weil ein Kilometer 1000 m und eine Stunde 3600 s hat, sind 1000 m/km und 1 h/3600 s je gleich 1. 100 km/h mal beide Brüche ergibt 27,8 m/s; Kilometer und Stunde kürzen sich heraus.

**Schritt 4**: Addieren und Subtrahieren lassen sich nur Größen derselben Art, etwa zwei Kräfte; vorher bringt man sie auf dieselbe Einheit. 7 N plus 2 kN sind 7 N plus 2000 N, also 2007 N oder 2,007 kN, nicht 9 kN. Newton und Meter lassen sich gar nicht addieren.

**Schritt 5**: Daraus folgt die __Einheitenkontrolle__: Beide Seiten einer Gleichung haben dieselbe __Dimension__, das heißt, in SI-Basiseinheiten ohne Vorsätze geschrieben stehen links und rechts dieselben Einheiten. Wer für den Weg eines Autos, das aus dem Stand beschleunigt, Beschleunigung mal Zeit schreibt, erhält m/s² mal s, also m/s, eine Geschwindigkeit statt eines Wegs, und erkennt den Fehler, bevor er eine Zahl einsetzt. Fehler, die die Einheit nicht verändern, zeigt die Kontrolle nicht: einen falschen Zahlenfaktor wie $a\,t^2$ statt $\tfrac{1}{2}\,a\,t^2$, ein falsches Vorzeichen oder die Verwechslung zweier Größen mit derselben Einheit.

:::formel Formel
$$G_1\,G_2 = \{G_1\}\{G_2\}\cdot[G_1][G_2]$$
$$G_1 + G_2 = \big(\{G_1\} + \{G_2\}\big)\cdot[G]$$
:::

**So liest man das:** Ein Produkt zweier Größen ist immer erklärt, auch bei verschiedenen Einheiten; es entsteht eine neue Einheit, etwa A V. Eine Summe ist nur für Größen derselben Art erklärt, etwa zwei Kräfte, und ausrechnen lässt sie sich, sobald beide in derselben Einheit $[G]$ stehen.

**Kurz gesagt:** Die Einheit des Produkts ist das Produkt der Einheiten, und der Zahlenwert des Produkts ist das Produkt der Zahlenwerte. Der Zahlenwert der Summe ist die Summe der Zahlenwerte, wenn beide Größen in derselben Einheit stehen. Das gilt für alle Einheiten mit gemeinsamem Nullpunkt, nicht für Celsius-Temperaturen.

Idee der Herleitung: Man schreibt beide Größen als Zahlenwert mal Einheit und ordnet um bzw. klammert die gemeinsame Einheit aus.

:::herleitung
**Ausgangspunkt:** die Definition der Größe als Zahlenwert mal Einheit (Abschnitt *Zahlenwert und Einheit*).

**Annahmen:** (i) Einheiten verhalten sich in Produkten wie Faktoren: Die Reihenfolge ist beliebig, und ein Faktor lässt sich ausklammern. (ii) Die Einheiten sind proportionale Skalen mit gemeinsamem Nullpunkt, wie Meter, Sekunde, Volt oder Kelvin.

**Schritt 1**: Beide Größen als Produkt:

$$G_1 = \{G_1\}\cdot[G_1]$$

$$G_2 = \{G_2\}\cdot[G_2]$$

**Schritt 2**: Produkt umgeordnet, Zahlen nach vorn:

$$G_1\,G_2 = \{G_1\}\cdot[G_1]\cdot\{G_2\}\cdot[G_2] = \{G_1\}\{G_2\}\cdot[G_1][G_2]$$

**Schritt 3** (entscheidender Schritt): Summe: Ausklammern ist nur möglich, wenn in beiden Summanden derselbe Faktor steht, also für $[G_1] = [G_2] = [G]$:

$$G_1 + G_2 = \{G_1\}\cdot[G] + \{G_2\}\cdot[G] = \big(\{G_1\} + \{G_2\}\big)\cdot[G]$$

**Ergebnis:**

$$G_1\,G_2 = \{G_1\}\{G_2\}\cdot[G_1][G_2]$$

$$G_1 + G_2 = \big(\{G_1\} + \{G_2\}\big)\cdot[G]$$

**Woher die Faktoren kommen:** Das Produkt der Einheiten entsteht durch bloßes Umordnen; die gemeinsame Einheit der Summe ist der ausgeklammerte Faktor. Stehen verschiedene Einheiten in den Summanden, gibt es nichts auszuklammern.

**Proben:** 2 A mal 12 V ergibt 24 A V. 7 N plus 2000 N ergibt 2007 N. Mit verschiedenen Vorsätzen, 7 N plus 2 kN, muss man den Vorsatz erst ausschreiben, sonst stünden zwei verschiedene Faktoren da.

**Grenzen:** Annahme (ii) gilt nicht für die Celsius-Skala, deren Nullpunkt verschoben ist: 20 °C sind nicht doppelt so warm wie 10 °C. Mit Celsius-Werten rechnet man deshalb nur Temperaturdifferenzen, für alles andere nimmt man Kelvin.
:::

::::beispiel Die Energie eines Smartphone-Akkus
**Gegeben:** Akku mit 4000 mAh bei 3,85 V Nennspannung; eine Stunde hat 3600 s.

**Gesucht:** die gespeicherte Energie in Wattstunden und in Joule.

**Rechnung:** Vorsatz ausschreiben:

$$4000\ \mathrm{mAh} = 4000\cdot 10^{-3}\ \mathrm{A\,h} = 4\ \mathrm{A\,h}$$

Energie als Spannung mal Ladung, Einheiten mitmultipliziert; weil die Spannung beim Entladen sinkt, rechnet man mit der Nennspannung, einem Mittelwert, und erhält die Nennenergie, die auf dem Akku steht:

$$W = 3{,}85\ \mathrm{V}\cdot 4\ \mathrm{A\,h} = 15{,}4\ \mathrm{V\,A\,h} = 15{,}4\ \mathrm{W\,h}$$

Umrechnung mit einem Bruch vom Wert 1:

$$W = 15{,}4\ \mathrm{W\,h}\cdot\frac{3600\ \mathrm{s}}{1\ \mathrm{h}} = 55\,440\ \mathrm{W\,s} = 55{,}4\ \mathrm{kJ}$$

**Ergebnis:** **15,4 Wh oder 55,4 kJ.**

**Einordnung:** Das sind 0,0154 kWh; ein Föhn mit 2100 W setzt dieselbe Energie in 26 Sekunden um. Die Milliamperestunden auf dem Akku sind übrigens eine Ladung, keine Energie: 4000 mAh sind 14 400 C; erst mit der Spannung wird daraus Energie.
::::

:::analogie
Ein Preis ist ebenfalls Zahlenwert mal Einheit: 12 € sind 12 mal ein Euro oder 1200 Cent. Wer Euro in Cent umrechnet, multipliziert mit 100 ct je Euro, einem Bruch vom Wert 1, und wer 12 € und 50 ct zusammenzählen will, bringt erst beides auf dieselbe Einheit.

| Im Vergleich | Bei physikalischen Größen |
|---|---|
| Betrag in Euro | Zahlenwert |
| Euro, Cent | Einheit, Einheit mit Vorsatz |
| 100 ct je Euro | 3600 s je Stunde |
| nur gleiche Währung zusammenzählen | nur gleiche Ein­heiten addieren |

**Wo der Vergleich nicht stimmt:** Währungen lassen sich nicht miteinander multiplizieren, Euro mal Euro bedeutet nichts; Einheiten schon, Meter mal Meter ist eine Fläche. Außerdem schwanken Wechselkurse zwischen Währungen, während Umrechnungen zwischen SI-Einheiten exakt feststehen.
:::

## Geschwindigkeit und Beschleunigung

*Wie bestimmt man die Geschwindigkeit in einem Augenblick, und wie gewinnt man aus ihr den Weg zurück?*

:::grafik
Szene: get1/grundprinzipien/01-kinematik · Vorlage: gestapelte-zeitverlaeufe
**Abbildung 5:** Ein E-Auto beschleunigt gleichmäßig aus dem Stand und erreicht nach 6,0 s 100 km/h. Drei Diagramme über derselben Zeitachse von 0 bis 6 s. Oben der Ort $s(t)$, eine Parabel bis 83,3 m, mit der Sekante zwischen 3 s und 5 s (Steigung 18,5 m/s) und der Tangente bei 3 s (Steigung 13,9 m/s). In der Mitte die Geschwindigkeit $v(t)$, eine Gerade bis 27,8 m/s; die Fläche darunter, ein Dreieck, ist schraffiert und mit 83,3 m beschriftet. Unten die Beschleunigung $a(t)$, waagrecht bei 4,63 m/s². Die Geschwindigkeit ist die Steigung der oberen Kurve, der Weg die Fläche unter der mittleren.
:::

**Die Akteure:**

- __$t$__: Zeit; in s.
- __$s(t)$__: Ort, die Lage des Körpers auf seiner Bahn als Funktion der Zeit, mit Vorzeichen von einem festgelegten Nullpunkt aus gemessen; in m. Beim E-Auto liegt der Nullpunkt am Start, nach 6 s ist $s$ = 83,3 m.
- __$\Delta s$__, __$\Delta t$__: Änderung des Orts in einem Zeitabschnitt und dessen Länge.
- __$v(t)$__: Geschwindigkeit; in m/s; das E-Auto erreicht 27,8 m/s.
- __$a(t)$__: Beschleunigung, die Änderung der Geschwindigkeit je Zeit; in m/s²; beim E-Auto 4,63 m/s².
- __$s_0$__, __$v_0$__: Ort und Geschwindigkeit zur Zeit $t$ = 0; beim E-Auto beide null.

**Das Zusammenspiel in Schritten** (Abbildung 5):

**Schritt 1**: Das E-Auto legt in 6,0 s 83,3 m zurück. Weg durch Zeit ergibt 13,9 m/s, die mittlere Geschwindigkeit; der Tacho zeigt aber anfangs 0 und am Ende 100 km/h, also 27,8 m/s.

**Schritt 2**: Wie schnell ist es nach genau 3 s? Zwischen 3 s und 5 s legt es 37,04 m zurück, im Mittel 18,52 m/s; zwischen 3 s und 4 s sind es 16,20 m/s, zwischen 3 s und 3,1 s 14,12 m/s, zwischen 3 s und 3,01 s 13,91 m/s. Im Diagramm des Orts ist jeder dieser Quotienten die Steigung einer Geraden durch zwei Kurvenpunkte, einer __Sekante__.

**Schritt 3**: Je kürzer das Zeitstück, desto weniger ändert sich der Wert: Er nähert sich 13,89 m/s, der Steigung der __Tangente__, die die Kurve bei 3 s nur berührt. Dieser Grenzwert ist die Geschwindigkeit im Augenblick, die __Momentangeschwindigkeit__; mathematisch ist er die __Ableitung__ des Orts nach der Zeit.

**Schritt 4**: Ebenso ist die Beschleunigung die Ableitung der Geschwindigkeit nach der Zeit. Das E-Auto wird in jeder Sekunde um 4,63 m/s schneller; seine Beschleunigung ist 4,63 m/s², und ihre Einheit entsteht aus m/s geteilt durch s.

**Schritt 5**: Umgekehrt gewinnt man den Weg aus der Geschwindigkeit. In jedem kurzen Zeitstück legt das Auto Geschwindigkeit mal Zeitstück zurück, im Diagramm der Geschwindigkeit ein schmaler Streifen unter der Kurve. Alle Streifen zusammen, die Fläche, sind der Weg; mathematisch ist das das __Integral__ der Geschwindigkeit. Aus dem Stand ist die Fläche bei gleichmäßiger Beschleunigung ein Dreieck, 6,0 s mal 27,8 m/s durch 2, also 83,3 m. Weil die Höhe des Dreiecks mit der Zeit mitwächst, wächst die Fläche mit dem Quadrat der Zeit.

:::formel Definition
$$v = \frac{ds}{dt}$$
$$a = \frac{dv}{dt} = \frac{d^2 s}{dt^2}$$
:::

Man definiert die Geschwindigkeit als Grenzwert, weil nur er angibt, wie schnell sich der Ort in einem Augenblick ändert; der Quotient über ein endliches Zeitstück ist ein Mittelwert. Die Beschleunigung ist die zweite Ableitung des Orts. Dass die Zeit zweimal im Nenner steht, zeigt die Einheit m/s².

**Kurz gesagt:** Die Geschwindigkeit ist die Steigung des Orts, die Beschleunigung die Steigung der Geschwindigkeit, und die Änderung des Orts ist die Fläche unter der Geschwindigkeit (Flächen unter der Zeitachse zählen negativ). Die Einheit einer Steigung ist die Einheit der senkrechten Achse durch die der waagrechten, die Einheit einer Fläche ihr Produkt.

:::formel Formel
$$v(t) = v_0 + a\,t$$
$$s(t) = s_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2$$
:::

**So liest man das:** Bei konstanter Beschleunigung ändert sich die Geschwindigkeit gleichmäßig, und der Ort ist eine quadratische Funktion der Zeit: In der doppelten Zeit legt das Auto aus dem Stand den vierfachen Weg zurück, nach 3 s 20,8 m, nach 6 s 83,3 m. $s_0$ und $v_0$ sind die Anfangswerte; ohne sie beschreibt die Formel nur Bewegungen, die aus dem Stand am Nullpunkt beginnen.

Idee der Herleitung: Man integriert die konstante Beschleunigung einmal zur Geschwindigkeit und die Geschwindigkeit ein zweites Mal zum Ort.

:::herleitung
**Ausgangspunkt:** die Definitionen von Geschwindigkeit und Beschleunigung als Ableitungen und der Hauptsatz der Differential- und Integralrechnung aus der Schule: Die Änderung einer Größe zwischen zwei Zeitpunkten ist das Integral ihrer Ableitung.

**Annahmen:** (i) Die Beschleunigung $a$ ist konstant. (ii) Zur Zeit $t$ = 0 ist der Ort $s_0$ und die Geschwindigkeit $v_0$.

**Schritt 1**: Die Geschwindigkeit ändert sich zwischen 0 und $t$ um das Integral der Beschleunigung. Die obere Grenze ist die laufende Zeit $t$; die Variable, über die integriert wird, heißt deshalb $t'$:

$$v(t) - v_0 = \int_0^t a\,dt' = a\,t$$

**Schritt 2** (entscheidender Schritt): Der Ort ändert sich um das Integral der Geschwindigkeit, in die man Schritt 1 einsetzt:

$$s(t) - s_0 = \int_0^t v(t')\,dt' = \int_0^t (v_0 + a\,t')\,dt'$$

**Schritt 3**: Das Integral der Summe ist die Summe der Integrale, wenn beide existieren, wie hier bei stetigen Funktionen über ein endliches Zeitstück. Die Stammfunktion von $v_0$ ist $v_0\,t'$, die von $a\,t'$ ist $\tfrac{1}{2}\,a\,t'^2$; zwischen 0 und $t$ ausgewertet:

$$s(t) - s_0 = v_0\,t + \tfrac{1}{2}\,a\,t^2$$

**Ergebnis:**

$$v(t) = v_0 + a\,t$$

$$s(t) = s_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2$$

**Woher die Faktoren kommen:** $v_0\,t$ ist das Rechteck unter der Anfangsgeschwindigkeit, $\tfrac{1}{2}\,a\,t^2$ das Dreieck, das die gleichmäßig wachsende Geschwindigkeit hinzufügt; die ½ ist die halbe Grundseite mal Höhe.

**Proben:** Einheit: m plus m/s mal s plus m/s² mal s², jeweils m. Zahlenwert: 0,5 mal 4,63 m/s² mal 36 s² ergibt 83,3 m, ebenso die mittlere Geschwindigkeit 13,9 m/s mal 6 s.

**Grenzen:** Die Formel gilt nur für konstante Beschleunigung; ein reales Auto beschleunigt bei hoher Geschwindigkeit schwächer, und dann muss man die Integrale mit der tatsächlichen Beschleunigung ausrechnen.
:::

::::beispiel Ein E-Auto von 0 auf 100 km/h
**Gegeben:** Das E-Auto erreicht aus dem Stand in 6,0 s 100 km/h; die Beschleunigung sei dabei konstant.

**Gesucht:** Beschleunigung und zurückgelegter Weg.

**Rechnung:** Geschwindigkeit in m/s, mit 1 h = 3600 s:

$$100\ \frac{\mathrm{km}}{\mathrm{h}} = \frac{100\,000\ \mathrm{m}}{3600\ \mathrm{s}} = 27{,}8\ \frac{\mathrm{m}}{\mathrm{s}}$$

Beschleunigung als Geschwindigkeitsänderung je Zeit:

$$a = \frac{27{,}8\ \mathrm{m/s}}{6{,}0\ \mathrm{s}} = 4{,}63\ \frac{\mathrm{m}}{\mathrm{s}^2}$$

Weg aus dem Stand:

$$s = \tfrac{1}{2}\cdot 4{,}63\ \frac{\mathrm{m}}{\mathrm{s}^2}\cdot(6{,}0\ \mathrm{s})^2 = 83{,}3\ \mathrm{m}$$

**Ergebnis:** **4,63 m/s² und 83,3 m.**

**Einordnung:** Die Beschleunigung ist knapp die Hälfte der Fallbeschleunigung von 9,81 m/s²; auf dem Weg von 83 m wäre das Auto mit gleichbleibender Endgeschwindigkeit nur 3 s unterwegs.

**Variation:** Ein Smartphone, das aus 1,5 m Höhe fällt, beschleunigt mit 9,81 m/s² und braucht ohne Luftwiderstand 0,553 s bis zum Boden; es trifft mit 5,42 m/s auf, rund 19,5 km/h.
::::

Ein häufiger Fehler ist, den Weg von $t_0$ bis $t_1$ als zweifaches Integral mit der festen oberen Grenze $t_1$ auch im inneren Integral zu schreiben. Das innere Integral wäre dann eine feste Zahl, und für konstante Beschleunigung ergäbe sich $a\,(t_1 - t_0)^2$ statt $\tfrac{1}{2}\,a\,(t_1 - t_0)^2$, beim E-Auto mit $t_0$ = 0 also 166,7 m statt 83,3 m. Die innere Grenze muss die laufende Zeit sein, wie in Schritt 2 des Herleitungskastens. Zählt man den Anfangsort $s_0$ hinzu, erhält man den Ort zur Zeit $t_1$, nicht seine Änderung Δs.

:::fehlvorstellung
„Geschwindigkeit ist Weg durch Zeit.“ Das liegt nahe, weil man sie so in der Schule kennenlernt, und für eine gleichförmige Bewegung stimmt es. Ändert sich die Geschwindigkeit, ist Weg durch Zeit nur ihr Mittelwert über das Zeitstück, beim E-Auto 13,9 m/s, während es am Ende doppelt so schnell fährt (Schritt 1). Die Geschwindigkeit in einem Augenblick ist der Grenzwert für immer kürzere Zeitstücke, die Ableitung (Schritt 3).
:::

## Kraft und Gravitationsgesetz

*Was ist eine Kraft, und warum wirkt auf ein Kilogramm an der Erdoberfläche eine Kraft von 9,81 N?*

**Die Akteure:**

- __$\vec F$__: Kraft, ein Vektor mit Betrag und Richtung; in N. Greifen mehrere Kräfte an, zählt ihre Summe $\sum \vec F$, die __resultierende Kraft__.
- __$m$__: Masse eines Körpers; in kg.
- __$\vec a$__: Beschleunigung als Vektor; bei geradliniger Bewegung ist ihr Betrag der Betrag von $a$ aus dem vorigen Abschnitt, auf einer gekrümmten Bahn kommt ein Anteil quer zur Bahn hinzu.
- __$g$__: Fallbeschleunigung an der Erdoberfläche; 9,81 m/s².
- __$M$__, __$r$__: Masse eines zweiten Körpers und Abstand der beiden Körper. Für punktförmige und kugelsymmetrische Körper ist $r$ der Abstand ihrer Mittelpunkte; für andere Formen gilt das Gesetz nur, wenn der Abstand groß gegen ihre Ausdehnung ist.
- __$\gamma$__: Gravitationskonstante; 6,674·10⁻¹¹ m³/(kg s²).

Eine Kraft verformt einen festgehaltenen Körper oder beschleunigt einen beweglichen. Ein Körper von 1 kg, den man ohne Luftwiderstand fallen lässt, wird in jeder Sekunde um 9,81 m/s schneller; die Schwerkraft auf ihn beträgt deshalb 9,81 N, auf den Koffer von 20 kg 196,2 N.

:::formel Definition
$$\sum \vec F = m\,\vec a$$
:::

Newtons zweites Gesetz lässt sich als Festlegung der Kraft lesen: Eine Kraft ist, was eine Masse beschleunigt, und ihre Größe misst man an der Beschleunigung, die sie einer bekannten Masse erteilt. Die resultierende Kraft und die Beschleunigung zeigen in dieselbe Richtung. Hebt die Hand den Koffer gleichmäßig, heben sich Handkraft und Gewichtskraft auf, und die Beschleunigung ist null. Das Gesetz gilt so für Körper mit fester Masse, beobachtet von einem nicht beschleunigten Standpunkt aus. Üblich ist auch die Schreibweise ohne Pfeile und ohne Summe, für die Beträge einer einzelnen Kraft. Die Kraft, mit der die Erde einen Körper anzieht, heißt __Gewichtskraft__; ihr Betrag ist $m g$.

Woher die Schwerkraft kommt, sagt das __Gravitationsgesetz__: Zwei Massen ziehen einander an.

:::formel Gesetz
$$F = \gamma\,\frac{m\,M}{r^2}$$
:::

**So liest man das:** Die Anziehung ist proportional zu beiden Massen und umgekehrt proportional zum Quadrat ihres Abstands; doppelter Abstand ergibt ein Viertel der Kraft. Die Konstante ist winzig: Zwei Körper von je 1 kg in 1 m Abstand ziehen sich mit 6,7·10⁻¹¹ N an, 1,5·10¹¹-mal schwächer als die Erde jeden von ihnen. Das Gesetz ist ein Erfahrungsgesetz: Newton fand es, weil es den Fall auf der Erde und den Umlauf des Mondes mit derselben Formel erklärt. Cavendish maß 1798 mit einer Drehwaage die Anziehung zwischen Bleikugeln; aus seinen Messungen folgt die Konstante.

Setzt man die Masse $M$ und den Radius der Erde ein, folgt die Fallbeschleunigung:

$$g = \gamma\,\frac{M}{R^2}$$

Dabei ist $R$ der Erdradius, 6371 km im Mittel, und $M$ die Erdmasse, 5,97·10²⁴ kg.

Idee der Herleitung: Man setzt die Gewichtskraft gleich der Anziehung durch die Erde und kürzt die Masse des Körpers.

:::herleitung
**Ausgangspunkt:** das Gravitationsgesetz und die Gewichtskraft $m g$ aus Newtons zweitem Gesetz.

**Annahmen:** (i) Die Erde ist eine Kugel, deren Masse so wirkt, als säße sie im Mittelpunkt. (ii) Der Körper befindet sich an der Oberfläche, im Abstand $R$ vom Mittelpunkt. (iii) Die Erdrotation wird vernachlässigt.

**Schritt 1**: Gewichtskraft und Anziehung sind dieselbe Kraft:

$$m\,g = \gamma\,\frac{m\,M}{R^2}$$

**Schritt 2** (entscheidender Schritt): Die Masse $m$ des Körpers steht auf beiden Seiten und kürzt sich:

$$g = \gamma\,\frac{M}{R^2}$$

**Ergebnis:**

$$g = \gamma\,\frac{M}{R^2}$$

**Woher die Faktoren kommen:** Dass $m$ herausfällt, ist der Grund, warum alle Körper ohne Luftwiderstand gleich schnell fallen; $\gamma M/R^2$ ist die Anziehung der Erde je Kilogramm des fallenden Körpers, in N/kg, also m/s².

**Proben:** Einheit: m³/(kg s²) mal kg durch m² ergibt m/s². Zahlenwert: 6,674·10⁻¹¹ mal 5,97·10²⁴ durch (6,371·10⁶)² ergibt 9,82 m/s².

**Grenzen:** Auf Meereshöhe liegt $g$ je nach geographischer Breite zwischen 9,78 m/s² am Äquator und 9,83 m/s² an den Polen, weil die Erde rotiert und abgeplattet ist; der Normwert 9,806 65 m/s² ist ein festgelegter Rechenwert dazwischen. Mit der Höhe nimmt die Anziehung umgekehrt proportional zum Quadrat des Abstands vom Erdmittelpunkt ab, bei doppeltem Abstand auf ein Viertel.
:::

::::beispiel Die Schwerkraft aus dem Gravitationsgesetz
**Gegeben:** $\gamma$ = 6,674·10⁻¹¹ m³/(kg s²); Erdmasse 5,97·10²⁴ kg; mittlerer Erdradius 6371 km; zwei Körper von je 1 kg in 1 m Abstand.

**Gesucht:** die Fallbeschleunigung und die Anziehung der beiden Körper.

**Rechnung:**

$$g = 6{,}674\cdot10^{-11}\ \frac{\mathrm{m}^3}{\mathrm{kg}\,\mathrm{s}^2}\cdot\frac{5{,}97\cdot10^{24}\ \mathrm{kg}}{(6{,}371\cdot10^{6}\ \mathrm{m})^2} = 9{,}82\ \frac{\mathrm{m}}{\mathrm{s}^2}$$

$$F = 6{,}674\cdot10^{-11}\ \frac{\mathrm{m}^3}{\mathrm{kg}\,\mathrm{s}^2}\cdot\frac{1\ \mathrm{kg}\cdot 1\ \mathrm{kg}}{(1\ \mathrm{m})^2} = 6{,}67\cdot10^{-11}\ \mathrm{N}$$

**Ergebnis:** **9,82 m/s² und 6,67·10⁻¹¹ N.**

**Einordnung:** Die Gravitation ist die schwächste der bekannten Kräfte; spürbar wird sie erst durch die riesige Masse der Erde. Die Kraft zwischen Ladungen ist genauso gebaut, aber unvergleichlich stärker ([Das elektrische Feld und die Feldstärke](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/elektrisches-feld-und-feldstaerke.html)).
::::

## Arbeit

*Wie viel Energie überträgt eine Kraft, die einen Körper bewegt, und warum zählt dabei nur ein Teil der Bewegung?*

:::grafik
Szene: get1/grundprinzipien/01-arbeit · Vorlage: schema-zustaende
**Abbildung 6:** (a) Ein Koffer von 20 kg wird 3 m höher gebracht, links über eine Treppe, rechts über eine Rampe von 12 m Länge mit 14,5° Neigung; an jedem Treppenstück die Gewichtskraft 196,2 N nach unten und die Kraft der Hand nach oben, waagrechte Stücke mit „0 J“, senkrechte zusammen „588,6 J“; an der Rampe die Kraft der Hand längs der Rampe, 49,05 N, mal 12 m, ebenfalls 588,6 J, und senkrecht zur Rampe deren Kraft auf den Koffer, 190,0 N, die keine Arbeit verrichtet. (b) Ein Schlitten wird mit 50 N an einer Schnur unter 30° gezogen; die Kraft ist in 43,3 N längs des Bodens und 25 N senkrecht dazu zerlegt; auf 20 m 866 J. (c) Waagrecht getragener Koffer: Kraft nach oben, Weg waagrecht, 0 J; abgesetzter Koffer: Kraft nach oben, Weg nach unten, −588,6 J. Nur der Kraftanteil längs des Wegs verrichtet Arbeit.
:::

**Die Akteure:**

- __$W$__: Arbeit, die Energie, die eine Kraft auf einen Körper überträgt; in J (1 J = 1 N m).
- __$\vec s$__: Verschiebung, der Pfeil vom Anfangs- zum Endpunkt eines geraden Wegstücks; in m.
- __$\alpha$__: Winkel zwischen Kraft und Verschiebung.
- __$C$__: der Weg als Kurve vom Anfangs- zum Endpunkt; __$d\vec s$__: ein sehr kurzes Stück von ihm.
- __$h$__: Höhenunterschied; beim Koffer 3 m.

**Das Zusammenspiel in Schritten** (Abbildung 6):

**Schritt 1**: Wird der Koffer 3 m senkrecht hochgehoben, wirkt die Hand mit seinem Gewicht, 196,2 N, längs des Wegs; die Arbeit ist Kraft mal Weg, 588,6 J.

**Schritt 2**: Wirkt die Kraft schräg zum Weg, zählt nur ihr Anteil längs des Wegs. Ein Schlitten wird mit 50 N an einer Schnur gezogen, die 30° gegen den Boden geneigt ist; längs des Bodens wirken 50 N mal cos 30°, also 43,3 N, und auf 20 m sind das 866 J (Abbildung 6b). Der Anteil senkrecht zum Boden, 25 N, trägt nichts bei: Die Arbeit der ganzen Kraft ist die Summe der Arbeiten ihrer beiden Anteile, 866 J plus 0 J.

**Schritt 3**: Steht die Kraft ganz senkrecht zum Weg, ist ihr Anteil längs des Wegs null und die Arbeit ebenfalls (Abbildung 6c).

**Schritt 4**: Läuft der Weg der Kraft entgegen, ist die Arbeit negativ. Setzt man den Koffer langsam 3 m tiefer ab, wirkt die Hand nach oben, der Koffer bewegt sich nach unten, und die Hand verrichtet −588,6 J; sie nimmt Energie auf, statt sie abzugeben.

**Schritt 5**: Hat der Weg Ecken oder Kurven oder ändert sich die Kraft, zerlegt man ihn in kurze Stücke, auf denen Kraft und Richtung fast fest sind, und addiert die Beiträge; für immer kürzere Stücke wird die Summe zum __Wegintegral__. Für die Schwerkraft liefert jedes waagrechte Stück null, weil sie senkrecht wirkt, und jedes senkrechte Gewicht mal Höhe: Auf dem Weg nach oben verrichtet sie über die Treppe wie über die Rampe −588,6 J. Die Hand bringt beim langsamen Heben genau das Gegenstück auf, 588,6 J; auf der Rampe schiebt sie dafür mit 49,05 N längs der Rampe, und den Rest des Gewichts trägt die Rampe, die senkrecht zum Weg drückt und keine Arbeit verrichtet (Abbildung 6a).

:::formel Definition
$$W = \vec F\cdot\vec s = F\,s\,\cos\alpha$$
$$W = \int_C \vec F\cdot d\vec s$$
:::

Man definiert die Arbeit über das __Skalarprodukt__ zweier Vektoren, das Produkt aus der Länge des einen und dem Anteil des anderen in seiner Richtung, weil nur der Anteil der Kraft längs der Bewegung Energie überträgt: $F \cos\alpha$ ist dieser Anteil, und $\cos\alpha$ ist 1 längs des Wegs, 0 senkrecht dazu und negativ, wenn der Weg der Kraft entgegen läuft. Die zweite Zeile ist das Wegintegral aus Schritt 5.

**Kurz gesagt:** Die Arbeit über den ganzen Weg ist die Summe der Arbeiten über seine Stücke. Für eine Kraft, die nur vom Ort abhängt, wie die Schwerkraft, ist die Arbeit auf demselben Weg in Gegenrichtung das Negative der Arbeit auf dem Hinweg.

Ein häufiger Fehler ist, die erste Zeile mit einem Betrag zu schreiben, $|\vec F\cdot\vec s|$; der Betrag ist falsch, denn er könnte nicht negativ werden, die Arbeit beim Absetzen ist es aber. Die Arbeit der Schwerkraft an einem Körper ist so groß wie die Abnahme seiner __potentiellen Energie__, der Energie seiner Lage im Schwerefeld.

:::formel Formel
$$W = m\,g\,h$$
:::

**So liest man das:** Die Arbeit, um einen Körper im Schwerefeld ohne Reibung anzuheben, ist Gewicht mal Höhenunterschied und hängt nicht vom Weg ab, sofern er am Ende so schnell ist wie am Anfang; beim Absenken ist $h$ negativ und die Arbeit der Hand ebenfalls. Doppelte Masse oder doppelte Höhe ergeben die doppelte Arbeit.

Idee der Herleitung: Man berechnet die Arbeit der Schwerkraft als Wegintegral, in dem nur die senkrechten Wegstücke beitragen, und nutzt, dass die Hand sie beim langsamen Heben genau ausgleicht.

:::herleitung
**Ausgangspunkt:** die Definition der Arbeit als Wegintegral.

**Annahmen:** (i) Die Fallbeschleunigung ist auf dem ganzen Weg gleich, was für Höhen von wenigen Kilometern gilt. (ii) Der Körper wird langsam bewegt, ohne ihn zu beschleunigen; die Summe aller Kräfte auf ihn ist deshalb in jedem Augenblick null. (iii) Ohne Reibung: Eine Unterlage, auf der der Körper gleitet, wie die Rampe, drückt nur senkrecht zu ihrer Fläche und damit senkrecht zum Weg.

**Schritt 1**: Koordinaten mit $x$ waagrecht und $y$ senkrecht nach oben. Schwerkraft und kurzes Wegstück:

$$\vec F_G = (0,\ -m g)$$

$$d\vec s = (dx,\ dy)$$

**Schritt 2** (entscheidender Schritt): Im Skalarprodukt fällt der waagrechte Anteil heraus, weil die Schwerkraft keinen waagrechten Anteil hat:

$$\vec F_G\cdot d\vec s = 0\cdot dx - m g\,dy = -m g\,dy$$

**Schritt 3**: Das Wegintegral wird zu einem gewöhnlichen Integral über die Höhe, von der Anfangshöhe $y_A$ bis zur Endhöhe $y_E$, gleich wie der Weg dazwischen verläuft:

$$W_G = \int_C \vec F_G\cdot d\vec s = -\int_{y_A}^{y_E} m g\,dy = -m g\,(y_E - y_A)$$

**Schritt 4**: Weil die Summe aller Kräfte in jedem Augenblick null ist (Annahme ii), ist auch die Summe ihrer Arbeiten null. Eine Unterlage verrichtet keine Arbeit (Annahme iii), also verrichtet die Hand das Gegenstück zur Arbeit der Schwerkraft:

$$W = -W_G = m g\,(y_E - y_A)$$

**Ergebnis:** Mit $h = y_E - y_A$:

$$W = m\,g\,h$$

**Woher die Faktoren kommen:** $m g$ ist der Betrag der Schwerkraft, $h$ die Summe aller senkrechten Wegstücke; für die Schwerkraft tragen die waagrechten nichts bei, weil ihr der waagrechte Anteil fehlt.

**Proben:** Einheit: kg mal m/s² mal m ergibt J. Zahlenwert: 20 kg mal 9,81 m/s² mal 3 m ergibt 588,6 J; über die Rampe schiebt die Hand mit 49,05 N längs des Wegs von 12 m, ebenfalls 588,6 J. Absenken um 3 m: −588,6 J.

**Grenzen:** Mit Reibung muss die Hand zusätzlich die Reibungskraft längs des ganzen Wegs überwinden; dann hängt ihre Arbeit vom Weg ab. Wird der Körper schneller, steckt die Hand außerdem Bewegungsenergie in ihn hinein.
:::

::::beispiel Ein Koffer über Treppe und Rampe
**Gegeben:** Koffer mit 20 kg; Höhenunterschied 3 m; Treppe oder reibungsfreie Rampe von 12 m Länge; $g$ = 9,81 m/s².

**Gesucht:** die Arbeit auf beiden Wegen und die nötige Kraft auf der Rampe.

**Rechnung:** Über die Treppe tragen nur die senkrechten Stücke bei:

$$W = 20\ \mathrm{kg}\cdot 9{,}81\ \frac{\mathrm{m}}{\mathrm{s}^2}\cdot 3\ \mathrm{m} = 588{,}6\ \mathrm{J}$$

Auf der Rampe muss die Hand längs der Neigung nur den Anteil der Gewichtskraft aufbringen, der dem Verhältnis von Höhe zu Länge entspricht; den Rest trägt die Rampe:

$$F = 196{,}2\ \mathrm{N}\cdot\frac{3\ \mathrm{m}}{12\ \mathrm{m}} = 49{,}05\ \mathrm{N}$$

$$W = 49{,}05\ \mathrm{N}\cdot 12\ \mathrm{m} = 588{,}6\ \mathrm{J}$$

**Ergebnis:** **Auf beiden Wegen 588,6 J; die Rampe verlangt nur 49 N statt 196 N, dafür den vierfachen Weg.**

**Einordnung:** Die Rampe spart Kraft, keine Arbeit. Wer den Koffer in 5 s die Treppe hinaufträgt, bringt für ihn 118 W auf, wer ihn in 15 s die Rampe hinaufschiebt, 39 W, jeweils ohne die Leistung für den eigenen Körper; verschieden ist die Leistung, die Arbeit je Zeit, nicht die Arbeit.
::::

:::fehlvorstellung
„Wer einen schweren Koffer lange waagrecht trägt, verrichtet viel Arbeit an ihm.“ Das liegt nahe, weil das Tragen anstrengt. Die Kraft der Hand zeigt aber nach oben und der Weg waagrecht; ihr Anteil längs des Wegs ist null, und der Koffer bekommt keine Energie: Seine Höhe und seine Geschwindigkeit bleiben gleich. Anstrengend ist das Tragen, weil Muskeln auch ohne Bewegung ständig Energie in Wärme umsetzen, um gespannt zu bleiben; ein Tisch hält denselben Koffer ohne jeden Energieverbrauch.
:::

:::frage
„Hängt die Arbeit bei jeder Kraft nur von Anfangs- und Endpunkt ab?“
Nein. Kraftfelder mit dieser Eigenschaft heißen __konservativ__; bei ihnen ist die Arbeit auf jedem geschlossenen Weg null. Das Schwerefeld ist konservativ; für das gleichmäßige Feld nahe der Erdoberfläche zeigt das die Herleitung von $W = m g h$. Gleitreibung an einer ruhenden Unterlage, etwa auf der Rampe, wirkt dagegen stets der Bewegung entgegen und verrichtet auf jedem Wegstück negative Arbeit; bei gleicher Andruckkraft kostet sie auf einem längeren Weg mehr, und auf einem geschlossenen Weg ist ihre Arbeit nicht null. Das elektrische Feld ruhender Ladungen ist ebenfalls konservativ; darauf beruht das Potential ([Arbeit, Potenzial und Spannung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/arbeit-potenzial-und-spannung.html)).
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Zahlenwert und Einheit | eine Größe ist ein Produkt, die Einheit ein Faktor |
| Basis­einheiten und definierende Konstanten | die sieben Grundfaktoren, auf die sich alles zurückführen lässt |
| abgeleitete Ein­heiten | Produkte von Potenzen der Basis­einheiten |
| Vorsätze | Zahlfaktoren vor der Einheit |
| Einheitenkontrolle | auf beiden Seiten einer Gleichung, in Basis­einheiten geschrieben, derselbe Faktor |
| Geschwindigkeit und Beschleunigung | Ableiten teilt die Einheit durch die Sekunde |
| Weg und Arbeit | Integrieren multipliziert die Einheit mit der Sekunde bzw. dem Meter |

Jede physikalische Größe ist Zahlenwert mal Einheit, und jede SI-Einheit ist ein Produkt von Potenzen der sieben Basiseinheiten; neue Größen entstehen, indem man bekannte multipliziert, dividiert, ableitet oder integriert, und ihre Einheiten entstehen dabei mit, so dass die Einheiten jeden Rechenfehler verraten, der die Einheit verändert.

## Bedeutung und Ausblick

Einheiten sind das wichtigste Prüfwerkzeug beim Rechnen: Wer in jeder Zeile die Einheiten mitführt, findet vertauschte Formeln und vergessene Vorsätze, bevor eine falsche Zahl in ein Datenblatt oder eine Schaltung gelangt. Datenblätter, Messgeräte und Simulationsprogramme arbeiten überwiegend im SI; die Vorsätze von Piko bis Giga begegnen in der Elektrotechnik ständig, vom Sperrstrom einer Diode bis zur Taktfrequenz eines Prozessors.

Arbeit als Wegintegral und das Schwerefeld, in dem die Arbeit nur von Anfangs- und Endpunkt abhängt, sind das Vorbild für das elektrische Feld: Dort wirkt auf Ladungen eine Kraft, das elektrische Feld verrichtet an ihnen Arbeit, und die Arbeit je Ladung ist die elektrische Spannung, ein Joule je Coulomb ist ein Volt ([Elektrisches Feld und Feldstärke](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/elektrisches-feld-und-feldstaerke.html), [Arbeit, Potenzial und Spannung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/arbeit-potenzial-und-spannung.html)).

:::kern
- Eine Größe ist Zahlenwert mal Einheit: $G = \{G\}\cdot[G]$.
- Das SI hat sieben Basiseinheiten: m, kg, s, A, K, mol, cd; seit 2019 legen sieben exakt festgelegte Konstanten sie fest.
- Jede SI-Einheit ist ein Produkt von Potenzen der Basiseinheiten, etwa $1\ \mathrm{V} = 1\ \mathrm{kg\,m^2\,s^{-3}\,A^{-1}}$; Vorsätze und Einheiten wie die Stunde bringen einen Zahlfaktor hinzu.
- Vorsätze sind Zehnerpotenzen und gehören zur Einheit: 1 km² sind $10^6$ m².
- Addieren nur Größen derselben Art, in derselben Einheit; beim Multiplizieren Zahlenwerte und Einheiten getrennt; beide Seiten einer Gleichung haben dieselbe Dimension.
- Geschwindigkeit und Beschleunigung sind Ableitungen, $v = ds/dt$ und $a = dv/dt$; bei konstanter Beschleunigung $s = s_0 + v_0 t + \tfrac{1}{2} a t^2$.
- Die Summe aller Kräfte ist Masse mal Beschleunigung; zwei Massen ziehen sich mit $\gamma m M/r^2$ an.
- Arbeit ist $\int \vec F\cdot d\vec s$: Nur der Kraftanteil längs des Wegs zählt, und sie kann negativ sein.
:::

:::quiz
F: Warum darf man 7 N und 2 kN addieren, aber nicht 7 N und 2 m?
A: Weil man beim Addieren eine gemeinsame Einheit ausklammert. 2 kN sind 2000 N, also ist die Summe 2007 N; Newton und Meter gehören zu verschiedenen Größenarten, keine Umrechnung macht sie gleich, die Summe ist nicht erklärt.
F: Warum ist die Momentangeschwindigkeit ein Grenzwert und nicht einfach Weg durch Zeit?
A: Weg durch Zeit ist der Mittelwert über ein Zeitstück. Erst für immer kürzere Zeitstücke nähert sich der Quotient der Steigung der Tangente, der Geschwindigkeit im Augenblick; beim E-Auto bei 3 s 13,9 m/s.
F: Warum wächst der Weg bei konstanter Beschleunigung aus dem Stand mit dem Quadrat der Zeit?
A: Der Weg ist die Fläche unter der Geschwindigkeitskurve. Aus dem Stand ist sie ein Dreieck, dessen Grundseite und Höhe beide mit der Zeit wachsen, also wächst die Fläche mit dem Quadrat der Zeit.
F: Warum ist die Arbeit, einen Koffer über eine Treppe hochzubringen, dieselbe wie über eine reibungsfreie Rampe?
A: Die Schwerkraft wirkt senkrecht; für sie zählen nur die senkrechten Wegstücke, zusammen der Höhenunterschied, und sie verrichtet auf beiden Wegen −588,6 J. Beim langsamen Heben gleicht die Hand das genau aus, denn die Rampe drückt senkrecht zum Weg und verrichtet keine Arbeit. Die Rampe verlangt weniger Kraft, 49 N statt 196 N, auf längerem Weg.
F: Stimmt es, dass 1 km² 1000 m² sind?
A: Nein. Der Vorsatz gehört zur Einheit, bevor quadriert wird: 1 km² ist (1000 m)², also eine Million Quadratmeter.
F: Stimmt es, dass man beim waagrechten Tragen eines Koffers Arbeit an ihm verrichtet?
A: Nein. Die Kraft zeigt nach oben, der Weg waagrecht; der Anteil der Kraft längs des Wegs ist null. Müde wird man, weil die Muskeln Energie in Wärme umsetzen.
F: Stimmt es, dass zwei Größen mit denselben Basiseinheiten dieselbe Größe sind?
A: Nein. Drehmoment und Energie haben beide kg m² s⁻², Frequenz und radioaktive Aktivität beide 1/s; deshalb schreibt man N m und J bzw. Hz und Bq.
F: Wie viel Energie speichert ein Akku mit 4000 mAh bei 3,85 V?
A: 4 Ah mal 3,85 V sind 15,4 Wh; mit 3600 s je Stunde 55 440 J, rund 55,4 kJ.
F: Welche Beschleunigung braucht ein Auto für 0 bis 100 km/h in 6,0 s bei gleichmäßiger Beschleunigung, und welchen Weg legt es dabei zurück?
A: 27,8 m/s durch 6,0 s ergibt 4,63 m/s²; der Weg ist ½ a t², also 83,3 m.
F: Wie viele Elementarladungen fließen bei 1 A je Sekunde, und warum ist die Zahl seit 2019 fest?
A: Rund 6,24·10¹⁸. Seit 2019 ist die Elementarladung auf genau 1,602 176 634·10⁻¹⁹ C festgelegt, und das Ampere ist darüber definiert.
:::
