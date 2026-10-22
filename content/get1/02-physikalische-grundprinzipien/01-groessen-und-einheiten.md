---
title: Physikalische Größen und Einheiten
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Physikalische Grundprinzipien
order: 20100
summary: Was eine physikalische Größe ist, wie die sieben Basiseinheiten des SI festgelegt sind, wie abgeleitete Einheiten und Vorsätze entstehen und wie man mit Einheiten rechnet und Rechnungen prüft; dazu Geschwindigkeit und Beschleunigung als Ableitungen, Kraft, Gravitationsgesetz und Arbeit als Wegintegral, jeweils hergeleitet. Kompakte Fassung; die ausführliche enthält zusätzlich die definierenden Konstanten im Einzelnen, Größen mit gleichen Basiseinheiten, weitere Beispiele und Hintergründe.
tags: physikalische Größe, Einheit, SI, Basisgrößen, Ampere, Einheitenvorsatz, Größengleichung, Dimensionskontrolle
stil: 3
fassung: kompakt
---

## Worum es geht

Wer die Spannung einer Steckdose angibt, schreibt 230 V und nicht 230: Erst die Einheit macht die Zahl zu einer Aussage über die Welt, und an den Einheiten lässt sich jede Rechnung prüfen. Das Thema folgt aus einem Prinzip:

**Jede physikalische Größe ist Zahlenwert mal Einheit, und jede SI-Einheit ist ein Produkt von Potenzen der sieben Basiseinheiten; neue Größen entstehen, indem man bekannte multipliziert, dividiert, ableitet oder integriert, und ihre Einheiten entstehen dabei mit, so dass die Einheiten jeden Rechenfehler verraten, der die Einheit verändert.**

Vorausgesetzt werden Schulmathematik (Potenzen, Ableitung als Steigung, Integral als Fläche) und Schulphysik. Darauf baut der Artikel [Arbeit, Potenzial und Spannung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/arbeit-potenzial-und-spannung.html) auf, in dem die Spannung als Arbeit je Ladung eingeführt wird.

:::grafik
Szene: get1/grundprinzipien/01-einheitenbaum · Vorlage: blockschaltbild
**Abbildung 1:** Stammbaum der Einheiten. Unten die sieben Basiseinheiten des SI: Meter, Kilogramm, Sekunde, Ampere, Kelvin, Mol, Candela. Darüber die abgeleiteten Einheiten der Mechanik und Elektrotechnik, jede mit der Gleichung, aus der sie entsteht, und Pfeilen zu den Einheiten, aus denen sie gebaut ist: Newton aus F = m a (kg, m, s), Joule aus W = F s, Watt aus P = W/t, Coulomb aus Q = I t (A, s), Volt aus P = U I, Ohm aus R = U/I, Farad aus C = Q/U, Weber aus Volt mal Sekunde, Tesla aus Weber je Quadratmeter. Jede SI-Einheit ist ein Produkt von Potenzen der Basiseinheiten.
:::

## Zahlenwert und Einheit

*Was gibt eine physikalische Größe an, und warum gehört die Einheit dazu?*

:::grafik
Szene: get1/grundprinzipien/01-zahlenwert-einheit · Vorlage: schema
**Abbildung 2:** Die Netzspannung $U$ als Produkt aus Zahlenwert und Einheit: 230 mal 1 V. Darunter dieselbe Spannung in zwei anderen Schreibweisen, 0,23 mal 1 kV und 230 000 mal 1 mV; Pfeile zeigen, dass der Zahlenwert um den Faktor 1000 kleiner bzw. größer wird, wenn die Einheit um denselben Faktor größer bzw. kleiner wird. Zahlenwert und Einheit ändern sich gegenläufig, die Größe bleibt dieselbe.
:::

Eine __physikalische Größe__ ist eine messbare Eigenschaft eines Körpers oder Vorgangs, etwa eine Länge oder eine Spannung. Gemessen wird sie, indem man sie mit einer festgelegten Vergleichsgröße, der __Einheit__, vergleicht und angibt, wie oft diese hineinpasst. Das Ergebnis ist ein Zahlenwert zu einer festgelegten Einheit und hängt deshalb nicht davon ab, wer misst.

**Die Akteure:**

- __$G$__: eine physikalische Größe, etwa die Spannung $U$.
- __$\{G\}$__: ihr __Zahlenwert__; bei 230 V die Zahl 230.
- __$[G]$__: ihre Einheit; bei der Spannung das Volt.

:::formel Definition
$$G = \{G\}\cdot[G]$$
:::

Die Größe ist ein Produkt; deshalb rechnet man mit Zahlenwert und Einheit wie mit zwei Faktoren. Wählt man eine tausendmal größere Einheit, wird der Zahlenwert tausendmal kleiner, und die Größe bleibt gleich: 230 V sind 0,23 kV oder 230 000 mV (Abbildung 2).

Jede Größe hat ein festes __Formelzeichen__:

| Gebiet | Größe und Formel­zeichen |
|---|---|
| Mechanik | Weg $s$, Zeit $t$, Masse $m$, Geschwindigkeit $v$, Beschleunigung $a$, Kraft $F$, Arbeit $W$ |
| Elektrizitätslehre | Ladung $Q$, Strom $I$, Span­nung $U$, Feldstärke $E$, Wider­stand $R$ |
| Wärmelehre | Tempe­ratur $T$, Wärmemenge $Q$, Entropie $S$ |

$Q$ steht also für zwei Größen; in der Elektrotechnik ist fast immer die Ladung gemeint.

## Basisgrößen und Basiseinheiten des SI

*Aus welchen Grundbausteinen sind alle Einheiten gebaut, und wie sind sie festgelegt?*

Das __Internationale Einheitensystem__ (SI) teilt die Größen in sieben __Basisgrößen__ und die übrigen, __abgeleiteten Größen__. Im SI gelten die Basisgrößen als voneinander unabhängig, eine Festlegung: Keine wird durch die anderen ausgedrückt, und jede abgeleitete Größe lässt sich auf sie zurückführen.

| Basis­größe | Formel­zeichen | Einheit | Zeichen |
|---|---|---|---|
| Länge | $l$, $s$, $r$ | Meter | m |
| Masse | $m$ | Kilo­gramm | kg |
| Zeit | $t$ | Sekunde | s |
| elek­trische Strom­stärke | $I$ | Ampere | A |
| abso­lute Tempe­ratur | $T$ | Kelvin | K |
| Stoff­menge | $n$ | Mol | mol |
| Licht­stärke | $I_v$ | Candela | cd |

Festgelegt sind die Basiseinheiten seit dem 20. Mai 2019 über sieben __definierende Konstanten__ mit vereinbarten, exakten Zahlenwerten. Die Sekunde etwa ist die Dauer von genau 9 192 631 770 Schwingungen einer bestimmten Strahlung des Atoms Cäsium-133. Das Ampere hängt an der __Elementarladung__, dem Betrag der Ladung eines Elektrons, festgelegt auf genau 1,602 176 634·10⁻¹⁹ A s; eine Amperesekunde heißt Coulomb, C, die Einheit der Ladung. Bei 1 A fließen deshalb je Sekunde rund 6,24·10¹⁸ Elementarladungen, bei 1 pA noch über sechs Millionen. Strom darf man deshalb als stetige Größe behandeln, solange in der betrachteten Zeitspanne sehr viele Ladungen fließen; die Körnigkeit bleibt als kleine Schwankung sichtbar, das __Schrotrauschen__.

:::frage
„Warum hängen die Einheiten an Konstanten und nicht mehr an Gegenständen?“
Bis 2019 war das Kilogramm die Masse eines Metallzylinders in Sèvres bei Paris. Seine Kopien wichen über rund hundert Jahre um etwa 50 Mikrogramm von ihm ab, und welcher Zylinder sich verändert hatte, ließ sich nicht entscheiden: Das Urkilogramm war per Definition immer genau ein Kilogramm. Eine Konstante ändert sich nicht und ist überall verfügbar. Mit dem festen Wert der Planck-Konstante, einer Naturkonstante der Quantenphysik, lässt sich das Kilogramm mit einer Wattwaage, die eine Gewichtskraft gegen eine elektromagnetische Kraft misst, oder einem gleichwertigen Verfahren verwirklichen, ohne Bezug auf einen Gegenstand.
:::

## Abgeleitete Einheiten

*Wie entstehen Einheiten wie Newton, Volt oder Ohm aus den Basiseinheiten?*

Ein Körper von 1 kg, der in jeder Sekunde um 1 m/s schneller wird, erfährt insgesamt eine Kraft von einem __Newton__; weil Kraft Masse mal Beschleunigung ist, ist das Newton kg m s⁻². So entsteht jede abgeleitete Einheit aus der Gleichung ihrer Größe, und viele bekommen einen eigenen Namen (Abbildung 1):

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

Für die Flussdichte ist auch der Name „magnetische Induktion“ üblich. Wie eine Zeile der Tabelle entsteht, zeigt das Volt:

:::formel Formel
$$1\ \mathrm{V} = 1\ \frac{\mathrm{W}}{\mathrm{A}} = 1\ \frac{\mathrm{kg}\,\mathrm{m}^2}{\mathrm{s}^3\,\mathrm{A}}$$
:::

**So liest man das:** Ein Volt ist ein Watt je Ampere: 1 V setzt bei 1 A eine Leistung von 1 W um. In den Basiseinheiten steckt die Mechanik, über die Leistung, und das Ampere, über den Strom.

Idee der Herleitung: Man geht von der Kraft über Arbeit und Leistung zur elektrischen Leistung und setzt jeweils die schon bekannten Einheiten ein.

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

## Einheitenvorsätze

*Wie schreibt man sehr große und sehr kleine Werte handlich?*

:::grafik
Szene: get1/grundprinzipien/01-vorsaetze · Vorlage: skala-log
**Abbildung 3:** Logarithmische Achse der Stromstärke von 1 pA bis 10 A, darüber die Vorsätze Piko, Nano, Mikro, Milli als Abschnitte je drei Zehnerpotenzen. Markiert: 1 pA (6,24 Millionen Elementarladungen je Sekunde), 20 pA (Sperrstrom der Beispieldiode aus dem Diodenkapitel bei −1 V), 80 nA (Eingangsruhestrom eines Operationsverstärkers), 20 mA (Leuchtdiode), 9,13 A (Föhn mit 2100 W an 230 V). Zwischen dem kleinsten und dem größten Strom liegen knapp dreizehn Zehnerpotenzen; Vorsätze machen sie lesbar.
:::

Ein Operationsverstärker vom Typ 741 nimmt an jedem Eingang typisch 0,000 000 080 A auf, lesbar als 80 nA: Der __Vorsatz__ n (Nano) steht für den Faktor 10⁻⁹. Ein Vorsatz ist ein Zahlfaktor vor der Einheit (Abbildung 3). Die Vorsätze des SI reichen seit 2022 von 10⁻³⁰ bis 10³⁰:

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

Teile schreibt man klein, Vielfache ab Mega groß; Deka, Hekto und Kilo sind aus historischen Gründen klein. Die Schreibweise trägt Bedeutung, denn m ist Milli und M ist Mega; nur Schaltungssimulatoren der SPICE-Familie unterscheiden Groß- und Kleinschreibung nicht, dort bedeutet auch M Milli, und Mega schreibt man MEG. Vor einer Einheit steht höchstens ein Vorsatz, 1 nF und nicht 1 mµF, und Vorsatz und Einheit bilden ein einziges Zeichen, für das eine Hochzahl als Ganzes gilt.

:::fehlvorstellung
„1 km² sind 1000 m².“ Das liegt nahe, weil ein Kilometer 1000 m sind. Die Hochzahl gilt aber für Vorsatz und Einheit zusammen: 1 km² ist ein Quadrat von 1000 m mal 1000 m, also eine Million Quadratmeter. Ebenso sind 1 mm² Leiterquerschnitt 10⁻⁶ m².
:::

## Rechnen mit Einheiten

*Wie rechnet man mit Größen, und wie verraten Einheiten einen Rechenfehler?*

Weil eine Größe ein Produkt ist, sind Einheiten und Vorsätze Faktoren, und es gelten die gewohnten Regeln für Produkte.

**Das Zusammenspiel in Schritten** (Abbildung 2):

**Schritt 1**: Ein Vorsatz ist ein Zahlfaktor: 2 kN sind 2000 N.

**Schritt 2**: Beim Multiplizieren und Dividieren rechnet man Zahlenwerte und Einheiten getrennt: 2 A mal 12 V sind 24 A V, also 24 W; 6 N m durch 3 m sind 2 N. Auch Vorsätze multiplizieren sich, Mega mal Milli ist Kilo.

**Schritt 3**: Umrechnen heißt mit einem Bruch vom Wert 1 multiplizieren: 100 km/h mal 1000 m/km mal 1 h/3600 s sind 27,8 m/s.

**Schritt 4**: Addieren lassen sich nur Größen derselben Art, und erst, wenn beide in derselben Einheit stehen: 7 N plus 2 kN sind 7 N plus 2000 N, also 2007 N, nicht 9 kN; Newton und Meter lassen sich gar nicht addieren.

**Schritt 5**: Daraus folgt die __Einheitenkontrolle__: Beide Seiten einer Gleichung haben dieselbe __Dimension__, das heißt, in SI-Basiseinheiten geschrieben dieselben Einheiten. Wer den Weg eines Autos aus dem Stand als Beschleunigung mal Zeit ansetzt, erhält m/s statt m und sieht den Fehler, bevor er rechnet. Einen falschen Zahlenfaktor wie $a\,t^2$ statt $\tfrac{1}{2}\,a\,t^2$ oder ein falsches Vorzeichen zeigt die Kontrolle nicht, denn die Einheit bleibt dabei gleich.

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

**Rechnung:** Vorsatz ausschreiben, dann Energie als Spannung mal Ladung; weil die Spannung beim Entladen sinkt, rechnet man mit der Nennspannung, einem Mittelwert, und erhält die Nennenergie:

$$W = 3{,}85\ \mathrm{V}\cdot 4000\cdot 10^{-3}\ \mathrm{A\,h} = 15{,}4\ \mathrm{V\,A\,h} = 15{,}4\ \mathrm{W\,h}$$

Umrechnung mit einem Bruch vom Wert 1:

$$W = 15{,}4\ \mathrm{W\,h}\cdot\frac{3600\ \mathrm{s}}{1\ \mathrm{h}} = 55\,440\ \mathrm{W\,s} = 55{,}4\ \mathrm{kJ}$$

**Ergebnis:** **15,4 Wh oder 55,4 kJ.**

**Einordnung:** Ein Föhn mit 2100 W setzt diese Energie in 26 Sekunden um. Die Milliamperestunden allein sind eine Ladung, 14 400 C; erst mit der Spannung wird daraus eine Energie.
::::

## Geschwindigkeit und Beschleunigung

*Wie bestimmt man die Geschwindigkeit in einem Augenblick, und wie gewinnt man aus ihr den Weg?*

:::grafik
Szene: get1/grundprinzipien/01-kinematik · Vorlage: gestapelte-zeitverlaeufe
**Abbildung 4:** Ein E-Auto beschleunigt gleichmäßig aus dem Stand und erreicht nach 6,0 s 100 km/h. Drei Diagramme über derselben Zeitachse von 0 bis 6 s. Oben der Ort $s(t)$, eine Parabel bis 83,3 m, mit der Sekante zwischen 3 s und 5 s (Steigung 18,5 m/s) und der Tangente bei 3 s (Steigung 13,9 m/s). In der Mitte die Geschwindigkeit $v(t)$, eine Gerade bis 27,8 m/s; die Fläche darunter, ein Dreieck, ist schraffiert und mit 83,3 m beschriftet. Unten die Beschleunigung $a(t)$, waagrecht bei 4,63 m/s². Die Geschwindigkeit ist die Steigung der oberen Kurve, der Weg die Fläche unter der mittleren.
:::

**Die Akteure:**

- __$t$__: Zeit; in s.
- __$s(t)$__: Ort, die Lage des Körpers auf seiner Bahn als Funktion der Zeit, mit Vorzeichen von einem festgelegten Nullpunkt aus gemessen; in m. Beim E-Auto liegt der Nullpunkt am Start, nach 6 s ist $s$ = 83,3 m.
- __$v(t)$__: Geschwindigkeit; in m/s; das E-Auto erreicht 27,8 m/s.
- __$a(t)$__: Beschleunigung, die Änderung der Geschwindigkeit je Zeit; in m/s²; beim E-Auto 4,63 m/s².
- __$s_0$__, __$v_0$__: Ort und Geschwindigkeit zur Zeit $t$ = 0; beim E-Auto beide null.

**Das Zusammenspiel in Schritten** (Abbildung 4):

**Schritt 1**: Ein E-Auto beschleunigt aus dem Stand gleichmäßig auf 100 km/h, also 27,8 m/s, und legt dabei in 6,0 s 83,3 m zurück. Weg durch Zeit ergibt 13,9 m/s, aber nur als Mittelwert: Der Tacho zeigt anfangs 0 und am Ende 27,8 m/s. Geschwindigkeit ist nur bei gleichförmiger Bewegung Weg durch Zeit.

**Schritt 2**: Für die Geschwindigkeit nach genau 3 s nimmt man immer kürzere Zeitstücke ab 3 s. Bis 5 s ergibt Weg durch Zeit 18,52 m/s, bis 4 s 16,20 m/s, bis 3,1 s 14,12 m/s, bis 3,01 s 13,91 m/s. Jeder Wert ist die Steigung einer __Sekante__, einer Geraden durch zwei Punkte der Ortskurve.

**Schritt 3**: Die Werte nähern sich 13,89 m/s, der Steigung der __Tangente__, die die Kurve bei 3 s berührt. Dieser Grenzwert ist die __Momentangeschwindigkeit__, mathematisch die __Ableitung__ des Orts nach der Zeit.

**Schritt 4**: Ebenso ist die Beschleunigung die Ableitung der Geschwindigkeit: Das E-Auto wird je Sekunde um 4,63 m/s schneller, seine Beschleunigung ist 4,63 m/s².

**Schritt 5**: Umgekehrt ist der Weg die Fläche unter der Geschwindigkeitskurve, mathematisch das __Integral__, denn in jedem kurzen Zeitstück legt das Auto Geschwindigkeit mal Zeitstück zurück. Aus dem Stand ist die Fläche ein Dreieck, 6,0 s mal 27,8 m/s durch 2, also 83,3 m; weil seine Höhe mit der Zeit wächst, wächst der Weg mit dem Quadrat der Zeit.

:::formel Definition
$$v = \frac{ds}{dt}$$
$$a = \frac{dv}{dt} = \frac{d^2 s}{dt^2}$$
:::

Nur der Grenzwert sagt, wie schnell sich der Ort in einem Augenblick ändert. In der zweiten Ableitung steht die Zeit zweimal im Nenner, daher m/s².

**Kurz gesagt:** Die Geschwindigkeit ist die Steigung des Orts, die Beschleunigung die Steigung der Geschwindigkeit, und die Änderung des Orts ist die Fläche unter der Geschwindigkeit (Flächen unter der Zeitachse zählen negativ). Die Einheit einer Steigung ist die Einheit der senkrechten Achse durch die der waagrechten, die Einheit einer Fläche ihr Produkt.

:::formel Formel
$$v(t) = v_0 + a\,t$$
$$s(t) = s_0 + v_0\,t + \tfrac{1}{2}\,a\,t^2$$
:::

**So liest man das:** Bei konstanter Beschleunigung ändert sich die Geschwindigkeit gleichmäßig, und der Ort ist eine quadratische Funktion der Zeit: In der doppelten Zeit legt das Auto aus dem Stand den vierfachen Weg zurück, nach 3 s 20,8 m, nach 6 s 83,3 m. $s_0$ und $v_0$ sind die Werte zu Beginn.

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

Ein häufiger Fehler ist, beim zweifachen Integral für den Weg von $t_0$ bis $t_1$ auch das innere Integral bis zur festen Zeit $t_1$ laufen zu lassen; das ergäbe $a\,(t_1 - t_0)^2$, beim E-Auto mit $t_0$ = 0 also 166,7 m statt 83,3 m. Innen gehört die laufende Zeit hin, wie in Schritt 2 des Kastens. Zählt man den Anfangsort $s_0$ hinzu, erhält man den Ort zur Zeit $t_1$, nicht seine Änderung Δs.

::::beispiel Ein E-Auto von 0 auf 100 km/h
**Gegeben:** Das E-Auto erreicht aus dem Stand in 6,0 s 100 km/h; die Beschleunigung sei dabei konstant.

**Gesucht:** Beschleunigung und zurückgelegter Weg.

**Rechnung:** Geschwindigkeit in m/s, mit 1 h = 3600 s:

$$100\ \frac{\mathrm{km}}{\mathrm{h}} = \frac{100\,000\ \mathrm{m}}{3600\ \mathrm{s}} = 27{,}8\ \frac{\mathrm{m}}{\mathrm{s}}$$

Beschleunigung als Geschwindigkeitsänderung je Zeit, dann der Weg aus dem Stand:

$$a = \frac{27{,}8\ \mathrm{m/s}}{6{,}0\ \mathrm{s}} = 4{,}63\ \frac{\mathrm{m}}{\mathrm{s}^2}$$

$$s = \tfrac{1}{2}\cdot 4{,}63\ \frac{\mathrm{m}}{\mathrm{s}^2}\cdot(6{,}0\ \mathrm{s})^2 = 83{,}3\ \mathrm{m}$$

**Ergebnis:** **4,63 m/s² und 83,3 m.**

**Einordnung:** Das ist knapp die Hälfte der Fallbeschleunigung von 9,81 m/s². Mit gleichbleibender Endgeschwindigkeit wäre das Auto auf denselben 83 m nur 3 s unterwegs.
::::

## Kraft und Gravitationsgesetz

*Was ist eine Kraft, und warum wirkt auf ein Kilogramm an der Erdoberfläche eine Kraft von 9,81 N?*

**Die Akteure:**

- __$\vec F$__: Kraft, ein Vektor mit Betrag und Richtung; in N. Greifen mehrere Kräfte an, zählt ihre Summe $\sum \vec F$, die __resultierende Kraft__.
- __$m$__: Masse eines Körpers; in kg.
- __$\vec a$__: Beschleunigung als Vektor; bei geradliniger Bewegung ist ihr Betrag der Betrag von $a$ aus dem vorigen Abschnitt.
- __$g$__: Fallbeschleunigung an der Erdoberfläche; 9,81 m/s².
- __$M$__, __$r$__: Masse eines zweiten Körpers und Abstand der beiden Körper. Für punktförmige und kugelsymmetrische Körper ist $r$ der Abstand ihrer Mittelpunkte; für andere Formen gilt das Gesetz nur, wenn der Abstand groß gegen ihre Ausdehnung ist.
- __$\gamma$__: Gravitationskonstante; 6,674·10⁻¹¹ m³/(kg s²).

Eine Kraft verformt einen festgehaltenen Körper oder beschleunigt einen beweglichen; gemessen wird sie an der Beschleunigung, die sie einer bekannten Masse erteilt.

:::formel Definition
$$\sum \vec F = m\,\vec a$$
:::

Ein Körper von 1 kg, der ohne Luftwiderstand fällt, spürt nur die Schwerkraft und wird in jeder Sekunde um 9,81 m/s schneller; die __Gewichtskraft__ auf ihn ist deshalb 9,81 N, allgemein $m g$, auf einen Koffer von 20 kg 196,2 N. Hebt die Hand den Koffer gleichmäßig, hält sie ihm mit 196,2 N das Gleichgewicht: Die Summe der Kräfte ist null, und er wird nicht schneller. Woher die Gewichtskraft kommt, sagt das __Gravitationsgesetz__:

:::formel Gesetz
$$F = \gamma\,\frac{m\,M}{r^2}$$
:::

**So liest man das:** Zwei Massen ziehen einander an, proportional zu beiden Massen und umgekehrt proportional zum Quadrat ihres Abstands; doppelter Abstand ergibt ein Viertel der Kraft. Zwei Körper von je 1 kg in 1 m Abstand ziehen sich nur mit 6,7·10⁻¹¹ N an; spürbar wird die Gravitation erst durch die riesige Masse der Erde. Das Gesetz ist ein Erfahrungsgesetz und wird nicht hergeleitet.

Mit der Erdmasse $M$ = 5,97·10²⁴ kg und dem mittleren Erdradius $R$ = 6371 km als Abstand folgt die Fallbeschleunigung:

$$g = \gamma\,\frac{M}{R^2}$$

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

## Arbeit

*Wie viel Energie überträgt eine Kraft auf einen Körper, den sie bewegt, und warum zählt dabei nur ein Teil der Bewegung?*

:::grafik
Szene: get1/grundprinzipien/01-arbeit · Vorlage: schema-zustaende
**Abbildung 5:** (a) Ein Koffer von 20 kg wird 3 m höher gebracht, links über eine Treppe, rechts über eine Rampe von 12 m Länge mit 14,5° Neigung; an jedem Treppenstück die Gewichtskraft 196,2 N nach unten und die Kraft der Hand nach oben, waagrechte Stücke mit „0 J“, senkrechte zusammen „588,6 J“; an der Rampe die Kraft der Hand längs der Rampe, 49,05 N, mal 12 m, ebenfalls 588,6 J, und senkrecht zur Rampe deren Kraft auf den Koffer, 190,0 N, die keine Arbeit verrichtet. (b) Ein Schlitten wird mit 50 N an einer Schnur unter 30° gezogen; die Kraft ist in 43,3 N längs des Bodens und 25 N senkrecht dazu zerlegt; auf 20 m 866 J. (c) Waagrecht getragener Koffer: Kraft nach oben, Weg waagrecht, 0 J; abgesetzter Koffer: Kraft nach oben, Weg nach unten, −588,6 J. Nur der Kraftanteil längs des Wegs verrichtet Arbeit.
:::

**Die Akteure:**

- __$W$__: Arbeit, die Energie, die eine Kraft auf einen Körper überträgt; in J (1 J = 1 N m).
- __$\vec s$__: Verschiebung, der Pfeil vom Anfangs- zum Endpunkt eines geraden Wegstücks; in m.
- __$\alpha$__: Winkel zwischen Kraft und Verschiebung.
- __$C$__: der Weg als Kurve vom Anfangs- zum Endpunkt; __$d\vec s$__: ein sehr kurzes Stück von ihm.
- __$h$__: Höhenunterschied; beim Koffer 3 m.

**Das Zusammenspiel in Schritten** (Abbildung 5):

**Schritt 1**: Hebt man den Koffer von 20 kg senkrecht um 3 m, wirkt die Hand mit seinem Gewicht, 196,2 N, längs des Wegs; die Arbeit ist Kraft mal Weg, 588,6 J.

**Schritt 2**: Wirkt die Kraft schräg zum Weg, zählt nur ihr Anteil längs des Wegs. Zieht man einen Schlitten mit 50 N an einer Schnur, die 30° gegen den Boden geneigt ist, wirken längs des Bodens 50 N mal cos 30°, also 43,3 N, auf 20 m 866 J; der Anteil senkrecht zum Boden, 25 N, trägt nichts bei.

**Schritt 3**: Steht die Kraft ganz senkrecht zum Weg, ist die Arbeit deshalb null (Abbildung 5c).

**Schritt 4**: Läuft der Weg der Kraft entgegen, ist die Arbeit negativ: Setzt die Hand den Koffer langsam 3 m tiefer ab, wirkt sie nach oben, während er sich nach unten bewegt; sie verrichtet −588,6 J und nimmt Energie auf.

**Schritt 5**: Hat der Weg Ecken oder Kurven, zerlegt man ihn in kurze Stücke, auf denen Kraft und Richtung fast fest sind, und addiert die Beiträge; für immer kürzere Stücke wird die Summe zum __Wegintegral__. Für die Schwerkraft liefert jedes waagrechte Stück null, weil sie senkrecht wirkt, und jedes senkrechte Gewicht mal Höhe: Auf dem Weg nach oben verrichtet sie über die Treppe wie über die Rampe −588,6 J. Die Hand bringt beim langsamen Heben genau das Gegenstück auf, 588,6 J; auf der Rampe schiebt sie dafür mit 49,05 N längs der Rampe, und den Rest des Gewichts trägt die Rampe, die senkrecht zum Weg drückt und keine Arbeit verrichtet (Abbildung 5a).

:::formel Definition
$$W = \vec F\cdot\vec s = F\,s\,\cos\alpha$$
$$W = \int_C \vec F\cdot d\vec s$$
:::

Das __Skalarprodukt__ zweier Vektoren, das Produkt aus der Länge des einen und dem Anteil des anderen in seiner Richtung, wählt genau den Kraftanteil längs der Bewegung aus: $\cos\alpha$ ist 1 längs des Wegs, 0 senkrecht dazu und negativ, wenn der Weg der Kraft entgegen läuft. Die zweite Zeile ist das Wegintegral aus Schritt 5.

**Kurz gesagt:** Die Arbeit über den ganzen Weg ist die Summe der Arbeiten über seine Stücke. Für eine Kraft, die nur vom Ort abhängt, wie die Schwerkraft, ist die Arbeit auf demselben Weg in Gegenrichtung das Negative der Arbeit auf dem Hinweg.

Ein häufiger Fehler ist, die erste Zeile mit Betragsstrichen zu schreiben, $|\vec F\cdot\vec s|$. Mit dem Betrag könnte die Arbeit nie negativ werden; beim Absetzen ist sie es aber. Die Arbeit der Schwerkraft an einem Körper ist so groß wie die Abnahme seiner __potentiellen Energie__, der Energie seiner Lage im Schwerefeld.

:::formel Formel
$$W = m\,g\,h$$
:::

**So liest man das:** Einen Körper im Schwerefeld ohne Reibung um $h$ anzuheben kostet Gewicht mal Höhenunterschied, gleich auf welchem Weg, sofern er am Ende so schnell ist wie am Anfang; beim Absenken ist $h$ negativ und die Arbeit der Hand ebenfalls. Doppelte Masse oder doppelte Höhe ergeben die doppelte Arbeit.

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
„Wer einen schweren Koffer lange waagrecht trägt, verrichtet viel Arbeit an ihm.“ Das liegt nahe, weil das Tragen anstrengt. Die Kraft der Hand zeigt aber nach oben und der Weg waagrecht; der Koffer gewinnt weder Höhe noch Geschwindigkeit, also keine Energie. Anstrengend ist das Tragen, weil gespannte Muskeln laufend Energie in Wärme umsetzen; ein Tisch hält denselben Koffer ohne jeden Energieverbrauch.
:::

:::frage
„Hängt die Arbeit bei jeder Kraft nur von Anfangs- und Endpunkt ab?“
Nein. Kraftfelder mit dieser Eigenschaft heißen __konservativ__; bei ihnen ist die Arbeit auf jedem geschlossenen Weg null. Das Schwerefeld ist konservativ; für das gleichmäßige Feld nahe der Erdoberfläche zeigt das die Herleitung von $W = m g h$. Gleitreibung an einer ruhenden Unterlage, etwa auf der Rampe, wirkt dagegen stets der Bewegung entgegen und verrichtet auf jedem Wegstück negative Arbeit; bei gleicher Andruckkraft kostet sie auf einem längeren Weg mehr, und auf einem geschlossenen Weg ist ihre Arbeit nicht null. Das elektrische Feld ruhender Ladungen ist ebenfalls konservativ; darauf beruht das Potential ([Arbeit, Potenzial und Spannung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/arbeit-potenzial-und-spannung.html)).
:::

## Alles hängt an einem Prinzip

| Einzelheit | welche Seite des Prinzips sie zeigt |
|---|---|
| Zahlenwert, Einheit und Vorsatz | eine Größe ist ein Produkt, Einheit und Vorsatz sind Faktoren |
| Basis­einheiten und abgeleitete Ein­heiten | jede SI-Einheit ist ein Produkt von Potenzen der sieben Grundfaktoren |
| Einheitenkontrolle | auf beiden Seiten einer Gleichung, in Basis­einheiten geschrieben, derselbe Faktor |
| Geschwindigkeit und Beschleunigung | Ableiten teilt die Einheit durch die Sekunde |
| Weg und Arbeit | Integrieren multipliziert die Einheit mit der Sekunde bzw. dem Meter |

Jede physikalische Größe ist Zahlenwert mal Einheit, und jede SI-Einheit ist ein Produkt von Potenzen der sieben Basiseinheiten; neue Größen entstehen, indem man bekannte multipliziert, dividiert, ableitet oder integriert, und ihre Einheiten entstehen dabei mit, so dass die Einheiten jeden Rechenfehler verraten, der die Einheit verändert.

## Bedeutung und Ausblick

Wer in jeder Zeile die Einheiten mitführt, findet vertauschte Formeln und vergessene Vorsätze, bevor eine falsche Zahl in eine Schaltung gelangt. Ebenso verrichtet das elektrische Feld Arbeit an Ladungen, und die Arbeit je Ladung ist die Spannung, ein Joule je Coulomb ist ein Volt ([Arbeit, Potenzial und Spannung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/elektrische-feldstarke-und-potenzial/arbeit-potenzial-und-spannung.html)).

**In der ausführlichen Fassung:** die sieben definierenden Konstanten im Einzelnen, warum es gerade sieben Basisgrößen sind, Größen mit denselben Basiseinheiten (Drehmoment und Energie, Hertz und Becquerel), die Schreibweise der Vorsätze, ein Vergleich der Einheiten mit Währungen und weitere Rechenbeispiele vom Föhn bis zur Gravitation zweier Körper. [Zur ausführlichen Fassung](/wissen/elektrotechnik/1-semester/grundgebiete-der-elektrotechnik-1/physikalische-grundprinzipien/groessen-und-einheiten-ausfuehrlich.html)

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
F: Warum ist die Arbeit, einen Koffer über eine Treppe hochzubringen, dieselbe wie über eine reibungsfreie Rampe?
A: Die Schwerkraft wirkt senkrecht; für sie zählen nur die senkrechten Wegstücke, zusammen der Höhenunterschied, und sie verrichtet auf beiden Wegen −588,6 J. Beim langsamen Heben gleicht die Hand das genau aus, denn die Rampe drückt senkrecht zum Weg und verrichtet keine Arbeit. Die Rampe verlangt weniger Kraft, 49 N statt 196 N, auf längerem Weg.
F: Stimmt es, dass 1 km² 1000 m² sind?
A: Nein. Die Hochzahl gilt für Vorsatz und Einheit zusammen: 1 km² ist (1000 m)², also eine Million Quadratmeter.
F: Stimmt es, dass man beim waagrechten Tragen eines Koffers Arbeit an ihm verrichtet?
A: Nein. Die Kraft zeigt nach oben, der Weg waagrecht; der Anteil der Kraft längs des Wegs ist null. Müde wird man, weil die Muskeln Energie in Wärme umsetzen.
F: Welche Beschleunigung braucht ein Auto für 0 bis 100 km/h in 6,0 s bei gleichmäßiger Beschleunigung, und welchen Weg legt es dabei zurück?
A: 27,8 m/s durch 6,0 s ergibt 4,63 m/s²; der Weg ist ½ a t², also 83,3 m.
:::
